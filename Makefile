DIR = $(shell pwd)

print_dir:
	@echo "Dir is $(DIR)"

mamba_create:
	mamba env create -n dez --file env.yaml

mamba_update:
	mamba env update -n dez --file env.yaml

db_start:
	docker-compose -f $(DIR)/modules/1_intro_prereqs/code/docker-compose.yaml up -d

db_pgcli:
	pgcli -h localhost -p 5432 -u root -d ny_taxi

.PHONY: mamba_create mamba_update db_start db_pgcli