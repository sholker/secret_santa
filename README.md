# Employee Couples Generator for Secret Santa Game

This Python program generates pairs of employees for a Secret Santa game using multiprocessing for efficiency.

## Features

- **Employee Class**: Defines an `Employee` class with attributes for department, name, and age.
- **Multiprocessing**: Utilizes Python's `multiprocessing.Pool` to parallelize the creation of employee pairs.
- **Random Pairing**: Shuffles the list of employees and generates pairs to ensure randomness.

## How to Use

1. **Data Input**: Prepare employee data in JSON format and save it as `data2.json`.
   Example JSON format:
   ```json
   [
       {"department": "R&D", "name": "Nikolas Porter", "age": 46},
       {"department": "Sales", "name": "Alice Smith", "age": 35},
       {"department": "Marketing", "name": "John Doe", "age": 42}
       ...
   ]


## Files

- **sol.py**: Contains the main solution to the problem.
- **sol_bonus.py**: Contains an additional solution for the bonus task.

`sol.py` implements the primary solution to address the problem statement.
On the other hand, `sol_bonus.py` extends the functionality to handle the bonus task associated with the project.
