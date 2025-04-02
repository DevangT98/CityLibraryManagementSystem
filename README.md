# City Library Management System

## Overview

The **City Library Management System** is a Python-based application designed to manage the operations of a city library. It provides functionalities for both administrators and readers, facilitating efficient management of books and user interactions.

## Features

- **Admin Page (`admin_page.py`)**: Allows library administrators to add, update, delete, and manage books and user information.
- **Reader Page (`reader_page.py`)**: Enables readers to search for books, view book details, and check availability.
- **Main Page (`main_page.py`)**: Serves as the central hub, directing users to either the admin or reader functionalities.
- **MySQL Database Integration (`mysql_connection.py`)**: Handles database connections and operations, ensuring data is stored and retrieved efficiently.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **MySQL Database**: Set up a MySQL database to store library data.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/DevangT98/CityLibraryManagementSystem.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd CityLibraryManagementSystem
   ```

3. **Install Required Python Packages**:

   ```bash
   pip install mysql-connector-python
   ```

4. **Set Up the Database**:

   - Create a new MySQL database named `librarydb`.
   - Import the `librarydb_1.sql` file to set up the necessary tables and data:

     ```bash
     mysql -u [username] -p librarydb < librarydb_1.sql
     ```

5. **Configure Database Connection**:

   - Update the `mysql_connection.py` file with your MySQL database credentials:

     ```python
     db = mysql.connector.connect(
         host="your_host",
         user="your_username",
         password="your_password",
         database="librarydb"
     )
     ```

6. **Run the Application**:

   ```bash
   python main.py
   ```

## Usage

- **Admin Functions**: Access the admin panel to manage books and user accounts.
- **Reader Functions**: Browse and search for books, view details, and check availability.

---

*Note: Ensure that your MySQL server is running before starting the application. For any issues or feature requests, please open an issue in the repository.*
