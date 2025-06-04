# Chat Application

A simple real-time chat application built with Flask and WebSocket technology.

## Features

- Real-time messaging using WebSocket
- Simple and clean interface
- Server-side event handling

## Requirements

- Python 3.x
- Flask
- Flask-SocketIO

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- On Windows:
```bash
.venv\Scripts\activate
```
- On macOS/Linux:
```bash
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the application:
```bash
python app.py
```
3. Open your browser and navigate to `http://localhost:5000`

## Project Structure

- `app.py`: Main application file containing Flask routes and WebSocket handlers
- `templates/`: Directory containing HTML templates
- `requirements.txt`: Project dependencies
- `.gitignore`: Git ignore file
- `.venv/`: Virtual environment directory (not tracked by git)
