# -Docker
Docker


Project Title: End-to-End Docker Container for Automated Text File Processing  

Objective:  
The primary objective of this project was to create an end-to-end Docker container that automates the process of reading, processing, and generating output from text files. The container was built to execute a Python script within a lightweight Docker image, aiming for an optimized image size of under 200MB.  

Tools & Technologies Used:
Docker Desktop: For containerization and image management.  
Python: For scripting and data processing.  
Lightweight Base Image: (e.g., `python:3.9-slim`) to minimize the Docker image size.  
Kubernetes/Docker Swarm (Optional): For extra credit, container orchestration was implemented with Kubernetes/Docker Swarm to manage multiple container replicas.  

Project Implementation:

1. Docker Setup: 
  Installed Docker Desktop and verified the setup by running a container. A screenshot of the running container is included in the submission.  

2. Dockerfile Creation:
     Built a Dockerfile using a lightweight base image (`python:3.9-slim`).  
     The Dockerfile installs only the required dependencies to keep the image size minimal.  

3. Python Script Development: 
       Implemented a Python script to perform the following tasks:  
       Read two text files (`IF-1.txt` and `AlwaysRememberUsThisWay-1.txt`) from the `/home/data` directory within the container.  
       Count the total number of words in each file.  
       Calculate the grand total of words across both files.  
       Identify the top 3 most frequent words in `IF-1.txt`.  
       Handle contractions in `AlwaysRememberUsThisWay-1.txt` and determine the top 3 most frequent words.  
       Retrieve the IP address of the container's host machine.  
       Write all results to an output file (`/home/data/output/result.txt`).  
       Display the contents of `result.txt` in the container's console output before exiting.  

4. Optimization:  
     Utilized multi-stage builds and minimized dependencies to reduce the Docker image size to under 200MB.  

5.   Testing & Validation:  
     Executed the container locally to ensure the script ran as expected, the output was correctly generated, and the container terminated without issues.  
     Created a tar file of the final Docker image (`[YourEmail].tar`) for submission.  

6.  Extra Credit (Optional): 
    Deployed the container using Kubernetes/Docker Swarm to create and manage at least two replicas.  
    Submitted the orchestration configuration (YAML for Kubernetes or Docker Swarm config) and provided the output from the `kubectl get pods` command.  

Conclusion:  
This project demonstrated the use of Docker for containerization, optimized image building, and automated script execution within a containerized environment. The extra credit implementation showcased container orchestration and scaling using Kubernetes/Docker Swarm.  

