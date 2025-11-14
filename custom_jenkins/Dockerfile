# Use the official Jenkins LTS image as the base
FROM jenkins/jenkins:lts

# Switch to the root user to install necessary packages
USER root

# === STEP 1: Install Prerequisites, Python, Docker CLI, and GCloud SDK ===
# Combine all package installations and setup steps into a single efficient layer.
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
    # 3. Add the Docker repository
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

# ---

# === STEP 2: Setup Jenkins User Permissions (Final GID Fix for GID 1000) ===
# This script ensures the 'docker' group has GID 1000 (matching the host's socket)
# and adds the 'jenkins' user to it, handling conflicts if GID 1000 is taken by another group.
RUN DOCKER_GID=1000; \
    CURRENT_GROUP=$(getent group $DOCKER_GID | cut -d: -f1); \
    # If GID 1000 is taken by a group that IS NOT 'docker', rename/renumber that group
    if [ "$CURRENT_GROUP" != "" ] && [ "$CURRENT_GROUP" != "docker" ]; then \
        echo "Renumbering conflicting group $CURRENT_GROUP from GID 1000 to 2500"; \
        groupmod -g 2500 $CURRENT_GROUP; \
    fi; \
    # Ensure the 'docker' group exists and has GID 1000
    if ! getent group docker > /dev/null; then \
        echo "Creating docker group with GID 1000"; \
        groupadd -g $DOCKER_GID docker; \
    fi; \
    # Finally, add the jenkins user to the docker group
    usermod -aG docker jenkins

# Switch back to the jenkins user
USER jenkins