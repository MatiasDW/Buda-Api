# Use an official Python base image.
FROM python:3.8-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the application code into the container.
COPY ./app /app

# Copy the tests into the container.
COPY ./tests /tests

# Copy the requirements file into the container.
COPY requirements.txt .

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run.
EXPOSE 5000

# Define the command to run the application.
CMD ["python", "./main.py"]
