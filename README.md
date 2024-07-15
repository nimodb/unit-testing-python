# Unit Testing Python
Unit testing is a software testing technique where individual units or components of a software are tested in isolation from the rest of the application. In Python, unit testing is commonly done using the `unittest` module, which is part of the standard library. This module provides a framework for creating and running tests, making it easier to ensure that individual parts of your code behave as expected.

Key Concepts in Unit Testing

- Test Case: A test case is a single unit of testing that checks a specific aspect of the code. It has one or more test methods.
- Test Suite: A collection of test cases that can be executed together.
- Test Runner: A component that runs tests and provides the results.
- Assertions: Statements that check if a condition is true. If the condition is false, the test fails.


## [Basic Example](https://github.com/nimodb/unit-testing-python/tree/main/simpleEx)


## [Complex Example](https://github.com/nimodb/unit-testing-python/tree/main/complexEx)

### Explanation of complex example

**BankAccount Class:**

- The `__init__` method initializes the balance.
- The `deposit` method adds to the balance if the amount is positive, otherwise raises a `ValueError`.
- The `withdraw` method subtracts from the balance if the amount is positive and does not exceed the current balance, otherwise raises a `ValueError`.
- The `get_balance` method returns the current balance.

**TestBankAccount Class:**

- `setUp`: This method is called before each test. It creates a `BankAccount` instance with an initial balance of 100.
- Each test method checks a specific aspect of the `BankAccount` class, using assertions to verify the expected outcomes.


## [Django Example](https://github.com/nimodb/unit-testing-python/tree/main/djangoEx)

### [Explanation of Library Project](https://github.com/nimodb/unit-testing-python/tree/main/djangoEx/library_project)
A Django-based library catalog application where users can view and add books to the catalog.

You can generate dummy books with German authors by running the following management command:
```sh
python manage.py generate_books
```