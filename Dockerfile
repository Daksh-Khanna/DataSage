# Use official Python image as the base
FROM python:3.11.9

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your project into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Define the command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]