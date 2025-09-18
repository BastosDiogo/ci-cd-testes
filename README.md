# arionkoder-advanced-meta-programming
This repository contains the implementation for the 'Advanced Meta-Programming' exercise.

# Usage Options
After cloning the project using the command `git clone https://github.com/BastosDiogo/arionkoder-advanced-meta-programming.git`,choose one of the two options below to run the project:

1-) Fully containerized application:
    • Build the container image with the following command: `sudo docker build -t generic-services-api .`
    • Then, create and run the container with the following command: `sudo docker run -it --rm generic-services-api /bin/bash`

2-) Running locally:
    • Create a Python virtual environment using the appropriate command for your OS (Linux or Windows) and activate it.

# Running the application
• To run the unit tests: Navigate to the `app` folder with the command: `cd app`. Then run the following command: `python3.12 -m unittest tests.test_generic_class`
