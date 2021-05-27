# Git-API-Challenge

# Building

Build the image:

`docker build --pull --rm -f "Dockerfile" -t gitapichallenge:latest "."`

# Running

Run the image:

`docker run -d -p 80:80 gitapichallenge:latest`

# Push to DockerHub

Create a tag for the image:

`docker tag gitapichallenge andrew-stclair/gitapichallenge`

Push the image:

`docker push andrew-stclair/gitapichallenge`

Now log into docker hub and verify whether the image was pushed and is available or not.