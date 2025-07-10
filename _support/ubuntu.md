# Installing Git and Docker Desktop on Ubuntu

This guide will help you install **Git** and **Docker Desktop** on an Ubuntu system.

---

## 1. Update your system packages

Open a terminal and run:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 2. Install Git

To install Git, run:

```bash
sudo apt install git -y
```

Verify the installation:

```bash
git --version
```

You should see the installed Git version.

---

## 3. Install Docker Desktop

Docker Desktop is officially supported on Ubuntu 22.04 and later.

### Step 3.1: Remove old Docker versions (if any)

```bash
sudo apt remove docker docker-engine docker.io containerd runc
```

### Step 3.2: Install required dependencies

```bash
sudo apt install ca-certificates curl gnupg lsb-release -y
```

### Step 3.3: Add Docker’s official GPG key

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### Step 3.4: Set up the Docker repository

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Step 3.5: Install Docker Engine and Docker CLI

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
```

### Step 3.6: Download and install Docker Desktop

Go to the [Docker Desktop for Linux releases page](https://docs.docker.com/desktop/install/ubuntu/) and download the latest `.deb` package, or run the following command to download the latest version (replace the URL with the latest release if necessary):

```bash
curl -LO https://desktop.docker.com/linux/main/amd64/docker-desktop-<version>-amd64.deb
```

Then install the package (replace `<version>` with the actual version number):

```bash
sudo dpkg -i docker-desktop-<version>-amd64.deb
sudo apt-get install -f
```

### Step 3.7: Start Docker Desktop

Run:

```bash
systemctl --user start docker-desktop
systemctl --user enable docker-desktop
```

To run Docker commands without `sudo`, add your user to the `docker` group:

```bash
sudo usermod -aG docker $USER
```

Log out and log back in for the group change to take effect.

---

## 4. Verify Docker installation

```bash
docker --version
docker run hello-world
```

If everything works, Docker Desktop is installed and running successfully.

---

# References

- [Git Documentation](https://git-scm.com/doc)
- [Docker Desktop for Ubuntu](https://docs.docker.com/desktop/install/ubuntu/)
