# Blog Web App

This is a simple blog web app developed using HTML, CSS, and Flask. The main file for this project is `app.py`.

## Features

- User registration and login
- Create, edit, and delete blog posts
- View and comment on blog posts

## Requirements

- Python 3.x
- Flask
- Flask-WTF
- SQLite (for development)
- SQLAlchemy (for production)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/imprasukjain/imprasukjain.github.io.git
   ```

2. Navigate to the project directory:

   ```bash
   cd web_app
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your web browser and visit `http://localhost:5000` to access the blog web app.

## File Structure

The project has the following structure:

```
├── app.py
├── static
│   ├── css
│   │   └── style.css
│   └── images
│       └── avatar.png
├── templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── post.html
│   ├── profile.html
│   ├── register.html
│   └── write.html
└── README.md
```

- `app.py`: This is the main file that contains the Flask application logic.
- `static/css/style.css`: CSS file for styling the web pages.
- `templates`: This directory contains the HTML templates for different web pages.
- `README.md`: This file provides information about the project.

## Contributing

If you'd like to contribute to this project, you can follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch and make your changes.
4. Commit and push your changes to your forked repository.
5. Submit a pull request to the original repository.

## The app is still in development mode , I uploaded a pertial version of app
Complete app will be uploaded soon.
