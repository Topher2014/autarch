.PHONY: dev run test

dev:
	conda activate -n autarch bash -c "source venv/bin/activate && exec bash"

run:
	@conda run -n autarch bash -c "source venv/bin/activate && python -m autarch $(ARGS)"

test:
	@conda run -n autarch bash -c "source venv/bin/activate && python -m autarch --help"
