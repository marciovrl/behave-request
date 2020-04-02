  
all: help

.PHONY: help
help: ## list options	
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY: test
test:  ## run tests
	behave 