# Use the official Jenkins LTS image as the base
FROM jenkins/jenkins:lts

# Switch to the root user to install necessary packages
USER root

# === STEP 1: Install Prerequisites, Python, Docker CLI, and GCloud SDK ===
# Combine all package installations into a single efficient layer.
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg python3 python3-venv && \
    \
    # --- Docker CLI Setup ---
    # 1. Create directory for Docker GPG keys
    install -m 0755 -d /etc/apt/keyrings && \
    \
    # 2. Download Docker's official GPG key and store it
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    \
    # 3. Add the Docker repository (using 'signed-by' syntax)
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    \
    # --- Google Cloud SDK Setup ---
    # 4. Add Google Cloud public key and repository
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl -sSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && \
    \
    # --- Final Installation and Cleanup ---
    # Refresh apt cache and install Docker CLI and Google Cloud CLI
    apt-get update -y && \
    apt-get install -y docker-ce-cli google-cloud-cli && \
    \
    # Clean up to reduce image size
    apt-get clean

# === STEP 2: Setup Jenkins User Permissions ===
# Create the docker group (GID 999 is common) and add the jenkins user to it.
RUN groupadd -g 999 docker || true && \
    usermod -aG docker jenkins

# Switch back to the jenkins user
USER jenkins