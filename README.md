<p align="center">
  <img src="https://cdn.discordapp.com/attachments/857714045251878972/977153774206476318/revenge_hotlinenct_dream.gif">
</p>

<p align="center">
  <a href="https://github.com/RandomTechrate/Discord-Server-Leaver/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-important">
  </a>
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.9%20%7C%203.11-informational.svg">
  </a>
  <a href="https://github.com/RandomTechrate">
    <img src="https://komarev.com/ghpvc/?username=RandomTechrate&style=flat&color=blue">
  </a>
</p>

<p align="center">
⚠️ <strong>Notice:</strong> This script is provided as-is, without any warranty. Use at your own risk.
</p>

---

## 📌 About

**Discord Server Leaver** is a simple Python script that allows you to automatically leave multiple Discord servers using account tokens, while supporting exceptions and basic rate-limit handling.

This project is intended for educational and personal use.

---

## ⚙️ Requirements

* Python **3.9 or 3.11**
* `requests` library

Install dependencies if needed:

```bash
pip install requests
```

---

## 🛠️ Installation

1. Clone or download the repository
   (for extra safety, download from the Releases page)

2. Add your Discord token(s) to:

   ```
   tokens.txt
   ```

   * One token per line

3. Add server IDs you **do NOT** want to leave to:

   ```
   exceptions.txt
   ```

   * One server ID per line

---

## 🚀 Running the Script

```bash
python main.py
```

The script will:

* Fetch all servers for each token
* Skip servers listed in `exceptions.txt`
* Leave all remaining servers

---

## 🧩 Known Issues

* If you are in **many servers**, you may need to run the script multiple times with a few minutes between runs due to Discord API rate limits.
* Servers **you own** cannot be left programmatically. The script may still report a success in these cases.

---

## ⭐ Support & Contribution

* Star the repository if you find it useful
* Contributions, improvements, and pull requests are welcome
* If the project gains enough interest, future versions may include:

  * Async performance improvements
  * Better rate-limit handling
  * Cleaner logging and configuration

---

## 📄 License

This project is licensed under the **MIT License**.
