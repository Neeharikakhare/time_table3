# College Timetable Management System

A comprehensive web-based system designed to manage college academic schedules, faculty details, course catalogs, and faculty load distribution.

## Features

- **Faculty Register:** Manage faculty records, including adding them manually or via bulk Excel import.
- **Course Catalog:** Maintain a repository of subjects and courses, with support for manual entry or Excel import.
- **Academic Mapping:** Assign courses to specific faculty members, calculate required lectures, and manage lab batches.
- **Schedule Generator:** An interactive grid to allocate assigned subjects to specific time slots.
- **Substitute Manager:** Identify and suggest substitute faculty members based on availability when a primary faculty member is absent.
- **Faculty Load Distribution:** A dedicated module (`load_distribution.html`) to calculate and export teaching load credits and hours into CSV format.

## Tech Stack

- **Frontend:** HTML, CSS (Vanilla), JavaScript, SheetJS (for Excel parsing)
- **Backend:** Python, Flask, Flask-CORS
- **Database:** SQLite (`timetable.db`)

## Project Structure

- `app.py`: The Flask application serving the backend REST API.
- `index.html`: The main user interface for the timetable management system.
- `load_distribution.html`: A standalone data entry form for calculating and exporting faculty load distribution.
- `timetable.db`: SQLite database storing all application data (created automatically upon running).

## How to Run Locally

### Prerequisites
Make sure you have Python installed on your system. 

### Installation
1. Clone or download this project folder.
2. Open a terminal or command prompt in the project folder.
3. Install the required Python packages:
   ```bash
   pip install flask flask-cors
   ```

### Running the Application
1. Start the Flask backend server:
   ```bash
   python app.py
   ```
   The backend API will run at `http://127.0.0.1:5000`.

2. Open the frontend interfaces in your web browser:
   - Double-click `index.html` to open the main Timetable Management System.
   - Double-click `load_distribution.html` to open the Faculty Load Distribution form.

## Notes
- Ensure the Flask backend (`app.py`) is running before trying to add or fetch data in `index.html`, as the frontend relies on the backend for all database operations.
