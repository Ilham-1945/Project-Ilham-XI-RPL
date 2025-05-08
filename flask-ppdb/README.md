# flask-ppdb/README.md

# PPDB Application

This is a simple Flask application for Penerimaan Peserta Didik Baru (PPDB). It allows new students to register and provides a dashboard for logged-in users.

## Project Structure

```
flask-ppdb
├── app
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── student.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── main.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── register.html
│   │   └── dashboard.html
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   └── config.py
├── migrations
│   └── __init__.py
├── run.py
├── requirements.txt
└── config.py
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-ppdb
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python run.py
   ```

## Usage

- Navigate to `http://localhost:5000` to access the application.
- Use the registration page to sign up new students.
- Access the dashboard after logging in.

## License

This project is licensed under the MIT License.