# Use the official Python image
FROM python:3.12.4

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "model_deploy_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
