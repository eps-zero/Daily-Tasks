# Daily-Tasks-Tkinter

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Creating .exe file](#creating-.exe-file)

## Description

The **Daily Tasks Application** is a Python program built using the Tkinter library that allows users to manage their daily tasks. Users can add, delete, and edit tasks, and the application stores this data in a SQLite database.

## Features

- Add tasks with due dates.
- View a list of tasks along with their creation and due dates.
- Delete tasks.
- Edit existing tasks, including changing the task name and due date.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.x
- SQLite3
- Other required packages (see [requirements.txt](requirements.txt))

### Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/eps-zero/Daily-Tasks-Tkinter.git
   ```

2. Navigate to the project directory:

   ```shell
   cd Daily-Tasks-Tkinter
   ```

3. Install the required packages using pip:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Run the application by executing the following command:

   ```shell
   python main.py
   ```

2. The application window will open, allowing you to add, delete, and edit tasks.

3. To add a new task, enter the task name and due date, and click the "Add" button.

4. To delete a task, select it in the list and click the "Delete" button.

5. To edit a task, select it in the list and click the "Edit" button. You can then modify the task name and due date.

6. Press Enter in the task name entry field to quickly add a task, or press Delete to delete a selected task.

## Creating .exe file

You can create .exe file just by typing this command:
```shell
python setup.py build
```
