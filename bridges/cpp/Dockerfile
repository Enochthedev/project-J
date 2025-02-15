FROM gcc:latest

WORKDIR /app
COPY . /app
RUN g++ -shared -o libcompute.so -fPIC compute.cpp

CMD ["/bin/bash"]