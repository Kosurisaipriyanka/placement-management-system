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

## API Endpoints
- GET /students/ → Get all students  
- POST /students/ → Add new student  
- PUT /students/{id}/ → Update student  
- DELETE /students/{id}/ → Delete student  

## Project Structure
- `placement_project/` – Django project settings  
- `placements/` – App containing models, views, URLs, templates, and static files  

## How to Run the Project
1. Clone the repository  
   ```bash
   git clone https://github.com/kosurisaipriyanka/placement-management-system.git
