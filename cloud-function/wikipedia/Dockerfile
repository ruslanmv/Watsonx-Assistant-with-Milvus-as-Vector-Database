# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app will run on
EXPOSE 8080

# Run the Flask command to start the app
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]
