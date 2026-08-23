# Use slim Python image
FROM python:3.11-slim

# Install Google Chrome and dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y google-chrome-stable \
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
ENTRYPOINT ["sh", "-c", "while ! curl -s http://app:3000 > /dev/null; do echo '⏳ Waiting for Next.js app...'; sleep 2; done; echo '✅ App is ready! Running Selenium tests...'; pytest --browser=chrome --headless --app-url=http://app:3000 -v --html=reports/report_docker.html --self-contained-html"]
