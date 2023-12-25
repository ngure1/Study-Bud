# Study Buddy

Study Buddy is a Django-based web application that facilitates group discussions on various topics. Users can create rooms, join discussions, and contribute to conversations on specific study topics.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features
- **User Authentication:** Users can sign up, log in, and manage their profiles.
- **Room Creation:** Users can create discussion rooms on specific study topics.
- **Real-time Chat:** Real-time chat functionality for users within each room.
- **Join and Contribute:** Users can join existing rooms and contribute to ongoing discussions.
- **Notification System:** Users receive notifications for new messages and room updates.
- **Responsive Design:** A responsive and user-friendly interface for desktop and mobile devices.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/study-buddy.git
    cd study-buddy
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
    ```or bash
    virtualenv venv    
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

## Usage
1. Access the application using the provided URL.
2. Sign up or log in to your account.
3. Create a new room or join an existing one.
4. Contribute to discussions by sending messages.
5. Enjoy collaborative studying with Study Buddy!


