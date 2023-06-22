# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the contents of the current directory on the host machine into the container's /app directory
COPY . /app

# Install the packages specified in requirements.txt using pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose ports 8000 and 8501 to allow access from outside the container
EXPOSE 8000
EXPOSE 8501

# Start both applications that is the fastapi and streamlit
CMD ["bash", "-c", "uvicorn app_fastapi:app --host 0.0.0.0 --port 8000 --workers 4 & streamlit run --server.enableCORS=false Home.py --browser.serverAddress=0.0.0.0 --server.port=8501"]

# Define an environment variable named NAME with the value "World"
ENV NAME World
