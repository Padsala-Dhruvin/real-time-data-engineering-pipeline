# Step 1: Use an official Python image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements first (to optimize caching)
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the code and the .env file
COPY . .

# Step 6: Command to run the script
CMD ["python", "ingest_data.py"]