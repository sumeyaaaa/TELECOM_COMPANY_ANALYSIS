# Use the official Python image from the Docker Hub
FROM python:3.12.4

# Set the working directory inside the container
WORKDIR /app




# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install streamlit==1.32.0 scikit-learn==1.4.2

#RUN pip install  joblib== 1.4.2

# Copy the rest of your application code into the container
COPY / ./

# Expose the port that Streamlit will run on
EXPOSE 8501

# Define the command to run the app
CMD ["streamlit", "run", "model_deploy_app.py"]