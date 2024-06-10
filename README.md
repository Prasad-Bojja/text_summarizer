# Text Summarization App

## Objective:
The objective of this assignment is to evaluate proficiency in Django and Django Rest Framework (DRF) by building a simple Django project. The project involves creating the backend for an application that summarizes text for logged-in users.

## Features:
1. **Authentication and User Management**:
   - Implement user registration and authentication using Django's built-in authentication system.
   - Users should be able to log in and log out securely.
   - APIs should be available to edit, delete, and create a user.

2. **Text Summarization**:
   - The API should ingest a large text field.
   - Utilize any third-party API to summarize the text and return the summarized version.

3. **Find Users**:
   - Implement an API for search functionality to return a list of users for the provided search term.
   - Include a field called `nameEmail`, which combines the first name, last name, and email of each user.

## Technologies Used:
- Django
- Django Rest Framework (DRF)
- Third-party text summarization API (e.g., Hugging Face Transformers)
- HTML, CSS, Bootstrap (for user interface, if applicable)

## Installation:
1. Clone the repository:
   ```bash
   git clone: https://github.com/Prasad-Bojja/text_summarizer

2. Install dependencies:
   pip install -r requirements.txt

3. Run migrations:
   python manage.py migrate

4. Start the development server:
   python manage.py runserver

## Usage:
1. Register a new user or log in with existing credentials.
2. Access the text summarization feature by providing a large text input.
3. Search for users using the provided search term to get a list of matching users.

   
