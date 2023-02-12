# Spiff Data Engineering Candidate Coding Exercises

## Information
The project here contains 2 main files: `calculator.py` and `main.py`. `calculator.py` contains the code for the commission
calculations. `main.py` can be used to see output of running some simple commission calculations

There is a `tests/` folder that contains a single file for unit testing with `pytest`. Steps for running tests are written below.

## Running
Follow the steps below to run the program
1. In a terminal, navigate to the project directory: `cd path/to/spiff_de_project`
2. If you want to create a virtual environment so the packages don't clutter up your global Python environment run these commands in a terminal:
   1. `python -m venv /venv`
   2. `venv/bin/Activate`
      1. This will activate your virtual environment
3. Run `pip install -r requirements.txt`
4. Run `python main.py`
5. If you would like to run unit tests:
   1.  In the same terminal, run `pytest`
   2. This will run the test suite in the `tests` folder. The tests will print out any failures and successes
