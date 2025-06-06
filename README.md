# RPAL Compiler

A compiler implementation for the **RPAL (Right-reference Pedagogical Algorithmic Language)** programming language that transforms RPAL source code into an executable form using a **CSE (Control Structure Evaluator)** machine.

---

## 📘 Project Overview

This project implements a full compiler pipeline for the RPAL language with the following components:

1. **Scanner** (`scanner.py`): Performs lexical analysis to convert source code into tokens.
2. **Parser** (`ASTParser.py`): Converts tokens into an Abstract Syntax Tree (AST).
3. **Standardizer** (`standardizer.py`): Transforms the AST into a Standardized Tree (ST) with simplified constructs.
4. **CSE Machine** (`standardizer.py`): Executes the ST code using a control-stack-based evaluator.

---

## 📁 File Structure

| File             | Description                                                       |
|------------------|-------------------------------------------------------------------|
| `ASTNode.py`     | Defines the Abstract Syntax Tree (AST) node class                 |
| `ASTParser.py`   | Implements the recursive descent parser                           |
| `scanner.py`     | Implements the lexical analyzer                                   |
| `standardizer.py`| Transforms AST and implements the CSE machine                     |
| `environment.py` | Defines the environment structure for variable scoping            |
| `myrpal.py`      | Main driver script                                                |
| `Makefile`       | Build automation for testing                                     |
| `tests/`         | Comprehensive test suite with 20+ RPAL test programs             |

---

## ✨ Features

- ✅ Full implementation of RPAL language constructs
- 🧠 AST visualization with `-ast` flag
- ♻️ Support for:
  - Lambda expressions and closures
  - Recursive functions
  - Higher-order functions
  - Tuples and tuple operations
  - Conditional expressions
  - Built-in functions: `Print`, `Stem`, `Stern`, `Conc`, etc.

---

## ▶️ Usage

Run from the command line:

```bash
python myrpal.py [-ast] file.rpal
```

### Options:
- `-ast`: Display the Abstract Syntax Tree (AST) of the input RPAL program.

### Examples:

```bash
python myrpal.py test.rpal                    # Run and evaluate the RPAL program
python myrpal.py -ast test.rpal               # Display the AST without executing
python myrpal.py tests/test_factorial.rpal    # Run a test from the test suite
python myrpal.py -ast tests/test_tuples.rpal  # View AST for tuple operations
```

---

## 🧪 Sample Program (`test.rpal`)

```rpal
let Sum(A) = Psum(A, Order A)
  where rec Psum(T, N) = N eq 0 -> 0 
                       | Psum(T, N-1) + T N
in Print( Sum(1,2,3,4,5) )
```

This defines a `Sum` function using a recursive helper `Psum` to compute the sum of a tuple. Executing this program prints:

```
15
```

---

## ⚙️ Compilation Process

1. **Scanning**: Tokenizes the source code.
2. **Parsing**: Builds the AST from tokens.
3. **Standardization**: Converts AST into simplified ST.
4. **Control Structure Generation**: Wraps ST into control structures.
5. **Execution**: CSE machine executes the control structures.

---

## 💡 Implementation Details

### 📌 Scanner
- Identifies tokens: keywords, operators, identifiers, numbers, symbols.

### 📌 Parser
- Implements recursive descent parsing for RPAL grammar rules.

### 📌 Standardizer
- Transforms high-level constructs (e.g., `let`, `where`, `rec`) into pure functional representations using `lambda`, `gamma`, and `tau`.

### 📌 CSE Machine
- Uses:
  - **Control Stack**: Instructions to execute.
  - **Value Stack**: Operands/results.
  - **Environment Stack**: Variable scoping.

---

## 🌐 RPAL Language Overview

RPAL is a functional language inspired by ML, Lisp, and Scheme.

- First-class functions and higher-order functions
- Pattern matching with conditional expressions
- Lexical scoping and recursive definitions
- Tuple operations and built-in library

---

## 🧪 Testing

The `tests/` directory contains comprehensive test cases covering various RPAL language features:

### Test Categories

#### Basic Language Features
- [`test_basic_let.rpal`](tests/test_basic_let.rpal) - Basic let expressions and arithmetic
- [`test_conditional.rpal`](tests/test_conditional.rpal) - Conditional expressions
- [`test_string.rpal`](tests/test_string.rpal) - String literals and operations
- [`test_where.rpal`](tests/test_where.rpal) - Where clauses

#### Function Features
- [`test_function_definitions.rpal`](tests/test_function_definitions.rpal) - Function definitions with `within` clause
- [`test_lambda_function.rpal`](tests/test_lambda_function.rpal) - Lambda expressions (fn notation)
- [`test_function_parameter.rpal`](tests/test_function_parameter.rpal) - Passing functions as parameters
- [`test_function_return.rpal`](tests/test_function_return.rpal) - Returning functions from functions
- [`test_conditional_function.rpal`](tests/test_conditional_function.rpal) - Selecting functions using conditionals
- [`test_nary_function.rpal`](tests/test_nary_function.rpal) - N-ary functions using tuples

#### Recursion & Scope
- [`test_factorial.rpal`](tests/test_factorial.rpal) - Recursive factorial function
- [`test_nested_scopes.rpal`](tests/test_nested_scopes.rpal) - Nested scope behavior
- [`test_simultaneous_definitions.rpal`](tests/test_simultaneous_definitions.rpal) - Simultaneous definitions with 'and'
- [`test_string_length.rpal`](tests/test_string_length.rpal) - Recursive string length calculation
- [`test_perfect_square.rpal`](tests/test_perfect_square.rpal) - Perfect square detection using recursion

#### Data Structures
- [`test_tuples.rpal`](tests/test_tuples.rpal) - Basic tuple operations and nested data structures
- [`test_arrays.rpal`](tests/test_arrays.rpal) - Array-like tuple structures with indexing
- [`test_multidimensional_arrays.rpal`](tests/test_multidimensional_arrays.rpal) - Tuples of tuples (matrices)
- [`test_triangular_array.rpal`](tests/test_triangular_array.rpal) - Triangular array data structure
- [`test_tuple_function.rpal`](tests/test_tuple_function.rpal) - Functions stored in tuples

#### Advanced Features
- [`test_normal_order.rpal`](tests/test_normal_order.rpal) - Normal order vs PL order evaluation
- [`test_at_operator.rpal`](tests/test_at_operator.rpal) - The @ operator for function application
- [`test_sum_list.rpal`](tests/test_sum_list.rpal) - List summation with partial functions
- [`test_vector_sum.rpal`](tests/test_vector_sum.rpal) - Vector addition operations

### Running Tests

**Using Make (Recommended):**
```bash
make all                    # Run all tests
make test_basic_let         # Run specific test
make test-basic             # Run basic language feature tests
make test-functions         # Run function-related tests
make test-recursion         # Run recursion-related tests
make test-data-structures   # Run data structure tests
make test-advanced          # Run advanced feature tests
make ast-all                # Run all tests with AST output
make list                   # List all available tests
```

**Direct Python Execution:**
```bash
python myrpal.py tests/test_factorial.rpal
python myrpal.py -ast tests/test_lambda_function.rpal
```

---

## 🤖 Extending the Project

Future enhancements may include:

- Adding more built-in functions
- Type checking and error recovery
- Debugging and trace output
- Optimizing the CSE machine

---

## 📦 Requirements

- Python 3.6+

---

## 📄 License

This project is provided for educational purposes.

---

## 👨‍💻 Authors

- University project implementation by Anas Hussaindeen & Tumasha Deshan