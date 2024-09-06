# Use a lightweight base image
FROM python:3.10-slim

# Install necessary dependencies
RUN pip install Flask

# Create a simple Flask app
COPY app.py /app/app.py
WORKDIR /app

# Expose port 8080
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]
