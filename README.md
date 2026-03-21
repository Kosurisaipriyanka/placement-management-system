# Placement Management System

A Django-based backend application with REST APIs to manage student placement data.

## Features
- Admin login using Django admin panel
- Add, edit, and delete student records (CRUD operations)
- Display student details on a web page
- Developed REST APIs for managing student and placement data
- Uses Django MVT architecture
- Database handled using Django ORM (SQLite)

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
