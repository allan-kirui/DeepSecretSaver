# Deep Secret Saver
<p align="center">
Deep Secret Saver is a simple command-line application that allows users to securely store and retrieve their secrets. It provides basic functionalities such as creating an account, logging in, retrieving secrets, and modifying secrets.</p>

The project was inspired by <a href="https://robertheaton.com/2019/08/12/programming-projects-for-advanced-beginners-user-logins/">
  Robert Heaton
</a>

## Features
### 1. Account Management
<li> Users can create a new account by providing a username and a secure password. </li>
<li> Passwords are securely hashed using SHA-256 before being stored in the database. </li>

### 2. Login
<li> Users can log in using their username and password. </li>
<li> The application checks the entered credentials against the stored hashed passwords in the database. </li>

### 3. Secret Retrieval and Modification
<li> Once logged in, users can retrieve their stored secret or modify it. </li>
<li> The secrets are stored securely in the database. </li>

### 4. Secure Database Management
<li> The application uses SQLite as the database backend. </li>
<li> Database actions include creating tables, checking tables, and showing the number of rows in each table. </li>

## How to Use
### Run the Application
Execute the main script (main.py) to start the Deep Secret Saver application.

### Choose Action
Welcome prompts will guide you to choose between logging in, creating an account, or quitting the application.

### Login
If you choose to log in, enter your username and password.

### Create Account
If you choose to create an account, enter a new username and password.

### Retrieve or Modify Secret
Once logged in, you can choose to retrieve your secret, modify it, or log out.

### Quit
To exit the application, choose the option to quit.

## Dependencies
Please perform 'pip install -r requirements' to get all the dependencies

## Configuration
<li> Database configuration is stored in config.yaml. </li>
<li> Default database name is specified in the configuration file. </li>

## Notes
<li> Passwords are securely hashed before being stored in the database. </li>
<li> The application checks for the existence of the database and tables and provides options to recreate them if needed. </li>
<br>
<b> Disclaimer:</b> This application is created for educational purposes, and security best practices should be followed for production environments.