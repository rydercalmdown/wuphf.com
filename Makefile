.PHONY: run
run:
	@echo "Running local client";
	@cd client && make run

.PHONY: install
install:
	@echo "Installing local client";
	@cd client && make install
