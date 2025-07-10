## 🛠️ How to Set Up This Project on Windows Using WSL2

Follow the steps below to configure this project on **Windows 10/11** using **WSL2 (Windows Subsystem for Linux 2)** and **Docker Desktop**.

---

### ✅ 1. Install WSL2

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

This installs:

- WSL2 backend
- Ubuntu (default distribution)
- Required kernel updates

> 🔁 Reboot your PC if prompted.

After reboot, confirm Ubuntu is using WSL2:

```bash
wsl --list --verbose
```

If it shows version 1, upgrade with:

```bash
wsl --set-version Ubuntu 2
```

---

### 🐳 2. Install Docker Desktop for Windows

1. Download and install Docker Desktop:\
   👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

2. After installing, go to:

   - **Settings → General**\
     ✅ Enable “Use the WSL2 based engine”
   - **Settings → Resources → WSL Integration**\
     ✅ Enable Docker integration for your Ubuntu distro

3. Start Docker Desktop and keep it running in the background.

---

### 🧱 3. Open Ubuntu via WSL2

Launch Ubuntu via the Start Menu or by running in PowerShell:

```powershell
wsl
```

This will open a Linux terminal where you’ll set up the project.

---

### 🔧 4. Install Git Inside Ubuntu

Run the following commands to install Git:

```bash
sudo apt update && sudo apt install -y git
```
