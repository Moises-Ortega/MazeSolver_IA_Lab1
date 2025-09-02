# MazeSolver_IA_Lab1
This project implements a maze-solving program in Python that navigates a maze represented as a matrix, where 1 denotes a wall, 0 a free path, S the start, and M the goal.

## Prerequisites

Ensure Python is installed (python --version or python3 --version).
Ensure git is installed (git --version).
A terminal (Command Prompt, PowerShell, or Git Bash on Windows; Terminal on macOS/Linux).

## Steps

### Clone the GitHub Repository

Open a terminal and navigate to the directory where you want to clone the repository.
For example:
```cd ~/Desktop/projects```

Clone the repository using the git clone command: 

```git clone https://github.com/Moises-Ortega/MazeSolver_IA_Lab1.git```

Navigate to the cloned repository's directory:

```cd MazeSolver_IA_Lab1```

### Create a Virtual EnvironmentA virtual environment isolates project dependencies to prevent conflicts.

In the repository's directory, create a virtual environment named venv:

```python -m venv venv```

This creates a venv folder containing the virtual environment.

Activate the virtual environment:

On Windows:
```.\venv\Scripts\activate```

On macOS/Linux:
```source venv/bin/activate```


After activation, you’ll see (venv) at the start of your terminal prompt, indicating the virtual environment is active.



### Install Dependencies from requirements.txt

Ensure the requirements.txt file exists in the repository directory. This file lists the project’s required dependencies.
With the virtual environment activated, run the following command to install dependencies:

```pip install -r requirements.txt```

This installs all libraries specified in requirements.txt into the virtual environment.


### Run the main.py Script

Verify that the main.py file exists in the repository directory.
Execute the script with:
```python main.py```


### Deactivate the Virtual Environment (Optional)

When you’re done working on the project, deactivate the virtual environment with:
```deactivate```




