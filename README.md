# test-ai
Test AI project

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/hello (docs at `/docs`).

## Test

```
python -m pytest
```
