# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run Streamlit when the container launches
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
