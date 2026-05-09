# Placement Management System

## Overview
Placement Management System is a Django-based web application developed to manage student placement information efficiently. The project provides REST APIs for handling student records and placement-related operations using Django and SQLite.

---

## Features
- Admin authentication using Django Admin Panel  
- Add, update, view, and delete student records  
- REST APIs for student and placement management  
- Display student details through web pages  
- Organized using Django MVT architecture  
- Database management using Django ORM and SQLite  

---

## Technologies Used
- Python  
- Django  
- SQLite  
- HTML  
- CSS  

---

## Functionalities
- Student record management  
- Placement data handling  
- CRUD operations using REST APIs  
- Admin dashboard for monitoring records  

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students/` | Retrieve all students |
| POST | `/students/` | Add a new student |
| PUT | `/students/{id}/` | Update student details |
| DELETE | `/students/{id}/` | Delete student record |

---

## Project Structure

```text
placement-management-system/
│── placement_project/      # Django project settings
│── placements/             # Main application
│── templates/              # HTML templates
│── static/                 # CSS and static files
│── db.sqlite3              # Database
│── manage.py
│── README.md
