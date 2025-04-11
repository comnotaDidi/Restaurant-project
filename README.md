# Panorama Sky Bar – Restaurant Website

Welcome to the repository of the Panorama Sky Bar website — a stylish and modern cocktail bar located on the 40th floor of the Warsaw Presidential Hotel, offering a panoramic view of Warsaw. This website was created to showcase the atmosphere of the venue, present the menu and gallery, and provide an easy way to make table reservations.

## Preview

![Main page screenshot](./path_to_your_screenshot.jpg)

## Technologies Used

- Django – backend framework
- HTML5, CSS3, Bootstrap 5 – responsive layout
- JavaScript – animations and interactive elements
- SQLite/PostgreSQL – database (depending on the environment)
- Django Templates – template engine

## Main Features

- Home page with bar introduction
- Gallery with image zoom effect on hover
- Table reservation system
- Menu page with food and drinks
- Contact form
- User authentication and admin panel

## Project Structure


## Installation and Launch

```bash
git clone https://github.com/your-username/skybar.git
cd skybar
python -m venv venv
source venv/bin/activate  # for Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
