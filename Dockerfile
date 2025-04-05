FROM ubuntu:22.04

# Base dependencies
RUN apt-get update && apt-get install -y \
    tor \
    curl \
    gnupg \
    lsb-release \
    python3 \
    python3-pip \
    net-tools \
    && pip3 install requests beautifulsoup4 stem

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set up working directory
WORKDIR /app

# Copy LLM config + crawler
COPY Modelfile /app/
COPY darkweb_crawler.py /app/

# Expose Ollama API
EXPOSE 11434

# Start both Tor and Ollama when container boots
CMD service tor start && ollama serve
