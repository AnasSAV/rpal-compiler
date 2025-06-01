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
| `test.rpal`      | Sample RPAL program                                               |

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
python myrpal.py test.rpal        # Run and evaluate the RPAL program
python myrpal.py -ast test.rpal   # Display the AST without executing
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