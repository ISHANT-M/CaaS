# 🎓 CaaS: CGPA as a Service

**CaaS** is an automated monitoring tool designed to track your academic progress on the Webkiosk portal. It runs strictly in the cloud using **GitHub Actions**, checks for updates to your CGPA at set intervals, and instantly notifies you via **Telegram** if any changes are detected.

It uses a smart persistence system (`value_updates` branch) to remember your previous data, so you only get alerted when something *actually* changes.

---

## 🚀 Features

- **Automated Monitoring**: Runs every 5 minutes automatically via GitHub Actions.
- **Instant Alerts**: Sends a Telegram message the moment a new grade or CGPA update drops.
- **Zero Cost**: Runs entirely on GitHub's free tier—no VPS or server required.
- **Smart Persistence**: Saves data between runs to a clean separate branch to prevent data loss between runs.

---

## 🛠️ Project Structure

**CaaS**<br>
|<br>
|-main.py<br>
|-src/<br>
|<br>
|-data.txt<br>
|-requirements.txt<br>
|-.env<br>
|

---

## ⚙️ Setup Guide


### 1. Fork the Repository
Click the **Fork** button in the top-right corner of this repository to create your own copy under your GitHub account.

### 2. Configure Telegram Credentials
You need two things from Telegram: **Bot Token** and your **Chat ID**.

#### A. Get Bot Token
1. Open Telegram and search for **@BotFather**.
2. Send the command `/newbot`.
3. Follow the instructions to name your bot.
4. BotFather will give you a **HTTP API Token** (e.g., `123456:ABC-DEF1234...`). **Copy this.**

#### B. Get Chat ID
1. Search for your new bot's username in Telegram and click **Start**.
2. Search for **@userinfobot** (or any ID echo bot).
3. Click **Start**. It will reply with your `Id` (e.g., `123456789`). **Copy this.**

### 3. Add GitHub Secrets
To keep your passwords safe, we use GitHub Secrets. **Do not put your password in the code.**

1. Go to your forked repository.
2. Navigate to **Settings** > **Secrets and variables** > **Actions**.
3. Click **New repository secret**.
4. Add the following four secrets:

| Secret Name | Value | Description |
| :--- | :--- | :--- |
| `USSR_ID` | `102xxxxxx` | Your College Roll Number |
| `PIN` | `*****` | Your Webkiosk Password |
| `TELEGRAM_TOKEN` | `123456:ABC...` | The token from BotFather |
| `TELEGRAM_CHAT_ID` | `123456789` | Your numeric Chat ID |

### 4. Enable Read/Write Permissions
The bot needs permission to write updates (save the new `data.txt`) to your repository.

1. Go to **Settings** > **Actions** > **General**.
2. Scroll down to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Click **Save**.

### 5. Activate the Workflow
By default, workflows in forked repositories are disabled.

1. Go to the **Actions** tab.
2. Click the button to **I understand my workflows, go ahead and enable them**.
3. To start it immediately, click on the **CG Fetcher Automation** workflow on the left, then click **Run workflow**.

---

## 🖥️ How It Works (Under the Hood)

1. **Trigger**: The workflow wakes up every 5 minutes or so (or on manual trigger).
2. **Environment Setup**: It creates a temporary `.env` file using the Secrets you provided.
3. **Restore State**: It fetches the `data.txt` file from the `value_updates` branch (this is where the "memory" lives).
4. **Execution**: It runs `main.py`, which:
   - Logs into Webkiosk.
   - Scrapes the latest Grade/CGPA data.
   - Compares it with `data.txt`.
   - If changed -> Sends Telegram Message & Updates `data.txt`.
5. **Save State**: If `data.txt` was updated, the workflow pushes the new file back to the `value_updates` branch using `git-auto-commit`, ready for the next run.
