# Git-API-Challenge

# Building and running

Build the image:

`docker build --pull --rm -f "Dockerfile" -t gitapichallenge:latest "."`

Run the image:

`docker run -d -p 80:80 gitapichallenge:latest`