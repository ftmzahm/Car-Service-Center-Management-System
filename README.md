# 🚗 Car Service Center Management System

A desktop application for managing a car service center. The project handles customers, vehicles, services, appointments, payments, reviews, and users.

This was my final project for my Python course. I built it to practice Python, OOP, MVC, Tkinter, MySQL, SQL, and input validation in one project.

---

## Features

### Customer Management

* Add, update, delete, and search customers
* Validate customer information

### Vehicle Management

* Add vehicles and connect them to customers
* Store brand, model, year, and plate number

### Service Management

* Add and manage services
* Search for services by name

### Appointment Management

* Book appointments
* Select a service and appointment date
* Change appointment status

### Payment Management

* Calculate the final service price
* Manage payment information

### Reviews

* Add, edit, and delete reviews
* Rating validation

### User & Admin

* User registration and login
* Admin panel
* User management

---

## Technologies

* Python
* Tkinter
* MySQL
* mysql-connector-python
* OOP
* MVC
* Regular Expressions (Regex)

---

## Project Structure

```text
Car-Service-Center-Management-System/
│
├── controller.py
├── model.py
├── view.py
├── images/
├── MySQL Queries/
└── .gitignore
```

### controller.py

Contains the application logic and input validation.

### model.py

Handles the database operations and communication with MySQL.

### view.py

Contains the Tkinter GUI.

---

## Database

The project uses MySQL and includes several related tables:

* Users
* Customers
* Vehicles
* Services
* Appointments
* Payments
* Reviews

The tables are connected using relationships such as primary keys and foreign keys.

---

## SQL

I used SQL for creating, retrieving, updating, and deleting data.

Some of the SQL concepts used in the project:

* SELECT
* INSERT
* UPDATE
* DELETE
* WHERE
* JOIN
* GROUP BY
* ORDER BY
* Aggregate functions
* Subqueries


---

## What I Learned

While working on this project, I practiced:

* Building a Python application using OOP
* Working with MySQL from Python
* Designing relationships between database tables
* Writing SQL queries
* Using MVC to organize a project
* Building a GUI with Tkinter
* Using Regex for input validation
* Debugging and fixing errors

---

## About

This is my final Python course project and one of my first projects where I combined Python, a GUI, and a relational database into one application.
