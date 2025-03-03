# Use a smaller Python base image
FROM python:3.9-alpine3.18

# Set the working directory
WORKDIR /home/data

# Install only pandas (without numpy) to reduce size
RUN pip install --no-cache-dir pandas

# Copy only necessary files
COPY scripts.py IF-1.txt AlwaysRememberUsThisWay-1.txt /home/data/

# Run the Python script
CMD ["python", "/home/data/scripts.py"]
