# Study Buddy

Study Buddy is a Django-based web application that facilitates group discussions on various topics. Users can create rooms, join discussions, and contribute to conversations on specific study topics.

### Brief intro
This is a project I embarked on while in my second year of study at ``JKUAT`` to teach myself backend web development using django

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)
    - [Django forms](./notes/DjangoForms)
        - [CRUD operations with forms](./notes/crud.md)
        - [Searching & Filtering](./notes/searchingandfiltering.md/)

## Features
- **User Authentication:** Users can sign up, log in, and manage their profiles.
- **Room Creation:** Users can create discussion rooms on specific study topics.
- **Room Updating:** Users can delete and wdit the name and topic of the rooms they created
- **Searching:** Users can search for rooms based off certain topics and the rooms will be filtered down
- **Real-time Chat:** Real-time chat functionality for users within each room.
- **Join and Contribute:** Users can join existing rooms and contribute to ongoing discussions.


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

## Notes
In this notes section I will be taking you through some of the steps I went thruough in impelementation of the feartures and the things I also learnt.Brace yourself for a qonderful experience and be ready to learn with me
1. [Django forms](./notes/DjangoForms)
    1. [CRUD operations](./notes/crud.md)
    1. [Searching & Filtering](./notes/searchingandfiltering.md/)

Credits to ``@Denis Ivy`` and ``@Traversy Media`` for their wonderful course 
You can checkout the course for yourself on their [Youtube Django Course](https://www.youtube.com/watch?v=PtQiiknWUcI&t=8432s)