# Notes App

A modern web application for creating and managing notes, built with FastAPI and MongoDB.

## Features

- Create, view, and delete notes
- Mark notes as important
- Modern and responsive UI
- Real-time updates
- MongoDB database integration

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repository-url>
cd notes-app
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with your MongoDB connection string:
```
MONGO_URI=your_mongodb_connection_string
```

5. Run the application:
```bash
uvicorn index:app --reload
```

The application will be available at `http://localhost:8000`

## Deployment

This application can be deployed on Render.com:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following environment variables:
   - `MONGO_URI`: Your MongoDB connection string
4. Deploy!

## Technologies Used

- FastAPI
- MongoDB
- Python
- HTML/CSS/JavaScript
- Bootstrap 5
- Font Awesome

## License

MIT 