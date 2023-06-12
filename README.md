# Flask Blog Web App

This repository contains a Flask web application for a blog. The web app is built using the Flask framework and organized using the blueprint pattern. It consists of multiple modules, including the main module and the register module, each with their own `__init__.py` file. The app includes separate routes for the home page, blog page, and contact page.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The Flask Blog Web App is a simple blogging platform that allows users to read and publish blog posts. It provides an intuitive user interface for easy navigation and interaction. The web app is built using the Flask framework, which is a lightweight and flexible web framework for Python.

## Features

The Flask Blog Web App includes the following features:

- Home Page: Displays the latest blog posts and provides links to read the full posts.
- Blog Page: Displays all published blog posts with options to view individual posts.
- Contact Page: Allows users to send messages or inquiries through a contact form.
- Blog Creation and Editing: Allows registered users to create, edit, and delete their own blog posts.
- Responsive Design: The web app is designed to be mobile-friendly and responsive on different devices.

## Repository Structure

This repository has the following structure:

```
|- app/
  |- static/              # Static files (CSS, JavaScript, etc.)
  |- templates/           # HTML templates
  |- __init__.py          # Package initialization
|- main/
  |- __init__.py          # Main module initialization
  |- routes.py             # Routes for the main module
|- register/
  |- __init__.py          # Register module initialization
  |- routes.py             # Routes for the register module
|- __init__.py            # Application initialization
|- app.py                 # Entry point to run the web app
|- requirements.txt       # List of dependencies
|- README.md              # Project Readme file
```

## Dependencies

The Flask Blog Web App requires the following dependencies:

- Python (3.6+)
- Flask (2.0+)
- Flask-WTF (0.15+)
- WTForms (2.3+)

You can install the required packages by running the following command:

```
pip install -r requirements.txt
```

## Usage

To use the Flask Blog Web App, follow these steps:

1. Configure the application: Update the configuration settings in the `app/__init__.py` file according to your needs. This includes setting the secret key, database configurations, etc.

2. Start the web app: Run the `app.py` script to start the Flask development server. The web app will be accessible at `http://localhost:5000`.

3. Explore the web app: Open your web browser and navigate to the home page (`http://localhost:5000`) to explore the blog, read posts, and access other features.

4. Customize the web app: Modify the templates and static files in the `app/templates/` and `app/static/` directories to customize the appearance and functionality of the web app.

## Contributing

Contributions to this repository are always welcome. If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.
