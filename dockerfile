# Start with a base Python image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable to configure Flask
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Run Gunicorn to serve the Flask app; adjust the number of workers as necessary
CMD ["gunicorn", "-b", ":8000", "app:app", "--workers=1"]
