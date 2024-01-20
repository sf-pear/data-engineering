DIR = $(shell pwd)

print_dir:
	@echo "Dir is $(DIR)"

mamba_create:
	mamba env create -n dez --file env.yaml

mamba_update:
	mamba env update -n dez --file env.yaml

.PHONY: mamba_create mamba_update