# API Testing with Postman and Newman

This repository contains a Postman collection for testing one of the REST API resources available on [GoRest](https://gorest.co.in/) and to be more specific related to `/users`.

## API Testing Approach

1. The Postman collection covers various testing levels and types, including functional, negative, and edge cases.
2. The tests are designed to catch potential critical defects and ensure the reliability of the API.
3. The collection includes tests for all the main operations (GET, POST, PUT, DELETE) on the selected resource.

## Execution Instructions

### Local Execution

To run the tests locally, you need to have [Postman](https://www.postman.com/) and [Newman](https://www.npmjs.com/package/newman) installed.

1. Import the Postman collection into your Postman application.
2. Configure the necessary environment variables, such as the authentication token.
3. Run the tests within Postman or use Newman to execute the tests from the command line:
   `newman run path/to/your/e2e_user_flow.postman_collection.json`

### CI/CD Pipeline Execution

The tests can be executed as part of a CI/CD pipeline using [GitHub Actions](https://github.com/features/actions). The provided `.github/workflows/newman-tests.yml` workflow file is configured to run the tests on each push or pull request to the `master` branch.

To set up the CI/CD pipeline:

1. Push the `.github` directory and your Postman collection JSON file to your GitHub repository.
2. GitHub Actions will automatically run the tests whenever there is a push or pull request to the `master` branch.
3. Be sure to update the token variable with your own authentication token in `environment-file.json`.

### Python Execution

There is simple tests for python, the same which was use in Postman

1. Update token in `go_test.py` file.
2. Install `pip install requests` and create virtual environment `python -m venv venv`
3. Activate the virtual environment `source venv/bin/activate` (for Unix-based systems) or `venv\Scripts\activate` (for Windows)
4. Run `python go_test.py` to execute the Python tests.

## Final Solution

The final solution includes a comprehensive Postman collection for testing one of the REST API resources on GoRest, along with a GitHub Actions workflow to execute the tests in a CI/CD pipeline. Also few python tests for some request, but not for all. This ensures that any changes made to the API are automatically tested, improving the overall reliability and stability of the API.
