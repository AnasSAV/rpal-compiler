# Makefile for RPAL Compiler Tests
# Usage:
#   make all          - Run all tests
#   make test_<name>  - Run a specific test
#   make clean        - Clean up output files
#   make list         - List all available tests

# Detect operating system
ifeq ($(OS),Windows_NT)
    DETECTED_OS := Windows
    PYTHON = python
    RM = del /Q
    RMDIR = rmdir /S /Q
    PATHSEP = \\
    NULL_DEVICE = nul
    SHELL = cmd
else
    DETECTED_OS := $(shell uname -s)
    PYTHON = python3
    RM = rm -f
    RMDIR = rm -rf
    PATHSEP = /
    NULL_DEVICE = /dev/null
endif

# Main compiler script
COMPILER = myrpal.py

# Test directory
TEST_DIR = tests

# Find all .rpal test files
TEST_FILES := $(wildcard $(TEST_DIR)/*.rpal)
TEST_NAMES := $(basename $(notdir $(TEST_FILES)))

# Default target
.PHONY: all
all: $(TEST_NAMES)

# Rule to run individual tests
.PHONY: $(TEST_NAMES)
$(TEST_NAMES): %: $(TEST_DIR)/%.rpal
	@echo "=== Running test: $@ ==="
	@$(PYTHON) $(COMPILER) $(TEST_DIR)/$*.rpal
	@echo ""

# Rule to run all tests with a summary
.PHONY: test-all
test-all:
	@echo "Running all RPAL tests..."
	@echo "========================="
ifeq ($(DETECTED_OS),Windows)
	@for %%t in ($(TEST_NAMES)) do @(echo === Running test: %%t === && $(PYTHON) $(COMPILER) $(TEST_DIR)/%%t.rpal && echo.)
else
	@for test in $(TEST_NAMES); do \
		echo "=== Running test: $$test ==="; \
		$(PYTHON) $(COMPILER) $(TEST_DIR)/$$test.rpal; \
		echo ""; \
	done
endif
	@echo "All tests completed!"

# Rule to run tests with AST output
.PHONY: ast-all
ast-all:
	@echo "Running all RPAL tests with AST output..."
	@echo "========================================="
ifeq ($(DETECTED_OS),Windows)
	@for %%t in ($(TEST_NAMES)) do @(echo === Running test with AST: %%t === && $(PYTHON) $(COMPILER) -ast $(TEST_DIR)/%%t.rpal && echo.)
else
	@for test in $(TEST_NAMES); do \
		echo "=== Running test with AST: $$test ==="; \
		$(PYTHON) $(COMPILER) -ast $(TEST_DIR)/$$test.rpal; \
		echo ""; \
	done
endif

# Rule to run individual test with AST
.PHONY: $(addsuffix -ast,$(TEST_NAMES))
$(addsuffix -ast,$(TEST_NAMES)): %-ast: $(TEST_DIR)/%.rpal
	@echo "=== Running test with AST: $* ==="
	@$(PYTHON) $(COMPILER) -ast $(TEST_DIR)/$*.rpal
	@echo ""

# List all available tests
.PHONY: list
list:
	@echo "Available tests:"
	@echo "================"
ifeq ($(DETECTED_OS),Windows)
	@for %%t in ($(TEST_NAMES)) do @echo   make %%t
else
	@for test in $(TEST_NAMES); do \
		echo "  make $$test"; \
	done
endif
	@echo ""
	@echo "Additional targets:"
	@echo "  make all         - Run all tests"
	@echo "  make test-all    - Run all tests with summary"
	@echo "  make ast-all     - Run all tests with AST output"
	@echo "  make <test>-ast  - Run specific test with AST output"
	@echo "  make clean       - Clean up output files"

# Clean target (if there are any output files to clean)
.PHONY: clean
clean:
	@echo "Cleaning up..."
ifeq ($(DETECTED_OS),Windows)
	@if exist "*.pyc" del /Q *.pyc 2>$(NULL_DEVICE) || echo.>$(NULL_DEVICE)
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /S /Q "%%d" 2>$(NULL_DEVICE) || echo.>$(NULL_DEVICE)
else
	@find . -name "*.pyc" -delete 2>$(NULL_DEVICE) || true
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>$(NULL_DEVICE) || true
endif
	@echo "Clean completed!"

# Help target
.PHONY: help
help: list

# Test specific categories
.PHONY: test-basic
test-basic: test_basic_let test_conditional test_string test_where

.PHONY: test-functions
test-functions: test_function_definitions test_lambda_function test_function_parameter test_function_return test_conditional_function test_nary_function

.PHONY: test-recursion
test-recursion: test_factorial test_string_length test_perfect_square

.PHONY: test-data-structures
test-data-structures: test_tuples test_arrays test_multidimensional_arrays test_triangular_array

.PHONY: test-advanced
test-advanced: test_nested_scopes test_simultaneous_definitions test_normal_order test_at_operator test_sum_list test_vector_sum

# Validate all test files exist
.PHONY: validate
validate:
	@echo "Validating test files..."
ifeq ($(DETECTED_OS),Windows)
	@for %%t in ($(TEST_NAMES)) do @if not exist "$(TEST_DIR)\\%%t.rpal" (echo Error: Test file $(TEST_DIR)\\%%t.rpal not found! && exit 1)
else
	@for test in $(TEST_NAMES); do \
		if [ ! -f "$(TEST_DIR)/$$test.rpal" ]; then \
			echo "Error: Test file $(TEST_DIR)/$$test.rpal not found!"; \
			exit 1; \
		fi; \
	done
endif
	@echo "All test files validated successfully!"

# Run tests in parallel (be careful with output formatting)
.PHONY: parallel
parallel:
	@echo "Running tests in parallel..."
	@echo "============================="
ifeq ($(DETECTED_OS),Windows)
	@echo "Note: Parallel execution on Windows runs sequentially"
	@for %%t in ($(TEST_NAMES)) do @(echo === %%t === && $(PYTHON) $(COMPILER) $(TEST_DIR)/%%t.rpal)
else
	@for test in $(TEST_NAMES); do \
		(echo "=== $$test ==="; $(PYTHON) $(COMPILER) $(TEST_DIR)/$$test.rpal) & \
	done; \
	wait
endif
