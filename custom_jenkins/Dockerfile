# Use the official Jenkins LTS image as the base
FROM jenkins/jenkins:lts

# Switch to the root user to install necessary packages
USER root

# Install prerequisites and the Docker client packages using modern key management
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg && \
    \
    # 1. Create directory for Docker GPG keys
    install -m 0755 -d /etc/apt/keyrings && \
    \
    # 2. Download Docker's official GPG key and store it in the keyrings folder
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    \
    # 3. Add the Docker repository using the 'signed-by' keyrings syntax (modern approach)
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    \
    # Install Docker packages (only CLI components are needed)
    apt-get update -y && \
    apt-get install -y docker-ce-cli && \
    \
    # Clean up APT caches to reduce image size
    apt-get clean

# Create the docker group and add the jenkins user to it
RUN groupadd -g 999 docker || true && \
    usermod -aG docker jenkins

# Switch back to the jenkins user
USER jenkins