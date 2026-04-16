# HNG Stage One - FastAPI Deployment

A minimal REST API built with Python/FastAPI and deployed on a VPS with Nginx as a reverse proxy.

## How to Run Locally

### Prerequisites
- Python 3.x installed

### Steps
1. Clone the repository
   git clone https://github.com/Zmmayin/HNG_stage_one.git
   cd HNG_stage_one

2. Create and activate a virtual environment
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install fastapi uvicorn

4. Run the app
   uvicorn main:app --reload

5. Visit http://localhost:8000

## Endpoints

| Method | Endpoint  | Response |
|--------|-----------|----------|
| GET    | /         | `{"message": "API is running"}` |
| GET    | /health   | `{"message": "healthy"}` |
| GET    | /me       | `{"name": "Emmanuel Ifelowo", "email": "eifelowo@gmail.com", "github": "https://github.com/Zmmayin"}` |

## Live URL
https://zmmayin.duckdns.org
