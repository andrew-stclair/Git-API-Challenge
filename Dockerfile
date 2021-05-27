# Use latest debian image as base for github runner
FROM debian:latest

# Copy in repository
COPY . /app

# Set workdir, entrypoint and script, and expose port 80
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["main.py"]
EXPOSE 80

# Install Python and requirements
RUN apt update && apt install git python3 python3-pip -y && pip3 install -r requirements.txt

# Healthcheck
HEALTHCHECK --interval=15s --timeout=3s \
CMD curl -f http://localhost/health || exit 1