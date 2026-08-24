# Use slim Python image
FROM python:3.11-slim

# Install Google Chrome and dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /automation

# Copy Python dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire automation framework
COPY automation/ automation/
COPY pytest.ini .

# Create necessary directories
RUN mkdir -p reports screenshots logs

# Entrypoint script: wait for app to be healthy, then run tests
ENTRYPOINT ["sh", "-c", "while ! curl -s http://webapp:3000 > /dev/null; do echo '⏳ Waiting for Next.js app...'; sleep 2; done; echo '✅ App is ready! Running Selenium tests...'; pytest --browser=chrome --headless --app-url=http://webapp:3000 -v --html=reports/report_docker.html --self-contained-html"]
