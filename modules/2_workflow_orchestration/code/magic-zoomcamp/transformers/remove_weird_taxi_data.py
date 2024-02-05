if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print('[Preprocessing] rows with zero passenger_count:', data['passenger_count'].isin([0]).sum())
    print('[Preprocessing] rows with zero trip_distance:', data['trip_distance'].isin([0]).sum())
    
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0.0)]

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.rename(columns={'VendorID': 'vendor_id', 'RatecodeID': 'rate_code_id', 'PULocationID': 'pu_laction_id', 'DOLocationID': 'do_laction_id'}, inplace=True)

    # print(data['vendor_id'].value_counts())

    return data


@test
def test_trip_distance(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance.'

@test
def test_passenger_count(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passangers.'

@test
def test_vendor_id(output, *args) -> None:
    assert "vendor_id" in output.columns, 'There is no column called vendor_id'