# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY dist/ ./
COPY static ./static
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir *.tar.gz

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
# ENV host=
# ENV database=
# ENV user=
# ENV password=
# ENV port=
# Run app.py when the container launches
CMD ["uvicorn", "fast_api_app.app:app", "--host", "0.0.0.0", "--port", "8000"]
