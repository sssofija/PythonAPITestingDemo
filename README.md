
#  Python API Testing Demo

This repository contains a demo of real-world API tests written in Python using `pytest` and `allure`.  
It showcases examples of test parametrization, fixtures, token handling, and generating detailed reports.

## 📂 Overview

The tests are built with the following technologies:

- `pytest` — Python testing framework  
- `allure-pytest` — for rich, visual test reports  
- `faker` — to generate dynamic test data  
- Custom fixtures and parametrized test cases  
- A project structure resembling real production test suites  

## ⚙️ Requirements

- Python 3.9 or higher  
- Dependencies installed via:

  ```bash
  pip install -r requirements.txt
⚠️ To run the tests, a .env file is required in the root directory.
It should contain environment-specific variables (e.g. base URLs, credentials, tokens).

## How to Run the Tests

Make sure the `.env` file is created with proper values.

### ✅ Clear previous Allure results:

```bash
rm -rf allure-results
````

### ✅ Run the tests:

```bash
pytest -m categ --alluredir=allure-results
```

### ✅ Generate and view the Allure report:

```bash
allure serve allure-results
```

## 📝 Note

This project is intended for demonstration purposes only and is a part of my personal portfolio.
It does not contain any sensitive information and is used solely to showcase my testing approach.

```

