from python:3.9
WORKDIR /app
COPY docker/ ./

RUN pip install -r requirements.txt

# Run the python application
CMD uvicorn main:app --reload --host 0.0.0.0