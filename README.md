# Task Management System

**🚀 Live Demo:** [https://task-management-system-one-chi.vercel.app](https://task-management-system-one-chi.vercel.app)

A sleek, responsive web application for assigning and tracking employee tasks using a Manager-Employee workflow. Built with **Python (Flask)**, **SQLite**, and vanilla CSS utilizing modern design principles like glassmorphism.

## Features

- **Admin Authentication:** Secure login for managers.
- **Task Dashboard:** A central view for managers to assign tasks and view statuses.
- **Dynamic Assignments:** A dynamically generated drop-down list populated from the database.
- **Status Toggling:** Managers can easily mark tasks as "Pending" or "Completed" using a smooth toggle switch.
- **Premium UI:** Designed with a vibrant, modern aesthetic, micro-animations, and glassmorphism elements.
- **Relational Database:** Robust underlying SQLite schema with `Task_Titles` and `Task_Management` tables.

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML5, CSS3 (Vanilla)
- **Design Highlights:** Glassmorphism, CSS Gradients, Custom Animations, Google Fonts (Outfit)

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd task-management-system
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install Flask Flask-Session
   ```

4. **Initialize the Database:**
   This script creates the database (`task_management.db`) and pre-populates it with sample task titles.
   ```bash
   python database.py
   ```

5. **Run the Application:**
   ```bash
   python app.py
   ```

6. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:5000/`

## Default Admin Credentials

- **Username:** `admin`
- **Password:** `password123`

## Directory Structure

```text
├── app.py                # Main Flask Server
├── database.py           # DB Initialization Script
├── static/
│   └── style.css         # Premium CSS Stylesheet
├── templates/
│   ├── dashboard.html    # Dashboard View
│   └── login.html        # Authentication View
└── README.md             # Project Documentation
```
