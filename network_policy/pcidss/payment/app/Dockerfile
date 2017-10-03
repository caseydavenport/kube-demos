FROM ubuntu:latest

# Install dependencies.
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Copy the code into the container.
COPY ./ /payment
WORKDIR /payment

# Install python dependencies.
RUN pip install -r requirements.txt 

# Set the entrypoint to execute the code.
ENTRYPOINT ["python"]
CMD ["payment.py"]
