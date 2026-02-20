# Sweet Delights Bakery

A beautiful Django web application for managing cakes and baker profiles with a modern, responsive design.

## Features

- **Homepage** - Browse all available cakes with beautiful cards showing image, name, price, weight, description, and baker
- **Add Cakes** - Create new cakes with name, description, price, weight, image, and baker assignment
- **Edit Cakes** - Modify existing cake information
- **Delete Cakes** - Remove cakes from the catalog
- **Baker Management** - Each cake can be assigned to a specific baker
- **Responsive Design** - Works great on desktop and mobile devices
- **Modern UI** - Clean, colorful design with hover effects and smooth transitions

## Screenshots

### Homepage
![Homepage](Screenshot%202026-02-20%20123204.png)

### Add New Cake
![Add Cake](Screenshot%202026-02-20%20123223.png)

### Edit Cake
![Edit Cake](Screenshot%202026-02-20%20123308.png)

## Technology Stack

- **Backend**: Django 5.2
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite
- **Images**: Pillow for image handling

## Setup

1. Install dependencies:
   ```bash
   pip install django Pillow
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and visit `http://127.0.0.1:8000`

## Project Structure

```
django_cake_app/
├── cakes/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── cakes_app/             # Main application
│   ├── models.py          # Cake and Baker models
│   ├── views.py           # View functions
│   ├── forms.py           # Django forms
│   └── admin.py           # Admin configuration
├── templates/             # HTML templates
│   ├── index.html         # Homepage
│   └── details.html       # Add/Edit form
├── media/                 # Uploaded cake images
└── README.md
```

## Usage

- Visit the homepage to browse all cakes
- Click "Add Cake" to create a new cake
- Click "Edit" on any cake card to modify it
- Click "Delete" to remove a cake
- All cakes display their price, weight, description, and assigned baker

## About

This project was developed as a laboratory exercise for the subject **Design of Human Computer Interaction** at FCSE (FINKI).
