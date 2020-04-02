  
all: help

.PHONY: help
help: ## list options	
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY: pip
pip:  ## install dependencies
	pip install -r requirements.txt 

.PHONY: test
test:  ## run all tests
	behave

.PHONY: test
test:  ## run tests by tags, e.g. = tag=run
	behave --tags="$(tag)"