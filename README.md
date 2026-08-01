# FeedbackBoard

FeedbackBoard is a Django-based web application for collecting and analysing user feedback. Users can submit responses through a feedback form, while the dashboard displays the collected feedback using interactive charts.

## Features

- Feedback form with four questions
- Stores submitted responses in a database
- Dashboard for viewing feedback results
- Interactive charts using Google Charts
- Responsive interface using Bootstrap
- Django-based backend

## Technologies Used

- Python
- Django
- HTML
- Bootstrap
- JavaScript
- Google Charts
- SQLite

## Project Structure

```text
FeedbackBoard/
├── feedback/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── feedback_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── .gitignore
├── README.md
├── manage.py
└── requirements.txt
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/TavishaBudhiraja/FeedbackBoard.git
```

### 2. Open the project folder

```bash
cd FeedbackBoard
```

### 3. Create a virtual environment

```bash
python -m venv f1
```

### 4. Activate the virtual environment

On Windows:

```bash
.\f1\Scripts\activate
```

On macOS or Linux:

```bash
source f1/bin/activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

### 8. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

## Application Pages

### Feedback Form

Users can submit feedback anonymously by answering four questions. The responses are stored in the database without requiring users to provide personal details.

### Dashboard

The dashboard provides a visual summary of submitted feedback through bar graphs, pie charts, response counts and feedback records.

## Author

**Tavisha Budhiraja**
