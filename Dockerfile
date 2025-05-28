# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Remove any existing files in /app before copying new ones
RUN rm -rf /app/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# Create a requirements.txt if it doesn't exist, and add Flask to it
RUN echo "Flask" > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 443
EXPOSE 443

# Define environment variable
ENV FLASK_APP=leemdiversapi.py

# Run newtest.py when the container launches
# Assuming newtest.py contains a Flask application that can be run directly
CMD ["python", "leemdiversapi.py"]
