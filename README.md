# Python OOP 1 Lab

## Overview

This project demonstrates basic Object-Oriented Programming (OOP) concepts in Python by creating two classes:

* `Book`
* `Coffee`

The lab focuses on:

* Class creation
* Constructors (`__init__`)
* Properties
* Validation
* Instance methods
* Running tests with `pytest`

---

## Project Structure

```bash
lib/
├── book.py
├── coffee.py
└── testing/
    ├── book_test.py
    └── coffee_test.py
```

---

## Features

### Book Class

* Stores a book title
* Stores a page count
* Validates that `page_count` is an integer
* Includes a `turn_page()` method

### Coffee Class

* Stores coffee size
* Stores coffee price
* Validates coffee sizes:

  * Small
  * Medium
  * Large
* Includes a `tip()` method that:

  * prints a message
  * increases price by 1

---

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd python-oop1-lab
```

Install dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Expected output:

```bash
7 passed
```

---

## Technologies Used

* Python 3
* Pytest
* Pipenv

---

## Author

Steven Rouse
