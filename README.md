 # Today in History Logger 📚

An automated GitHub repository that logs historical events for each day, creating a daily commit to maintain your GitHub activity streak! 🎯

---
## 🌟 Features

- **Daily Historical Events**: Fetches 3 random historical events for each day
- **Automatic Commits**: GitHub Actions runs daily at 5 AM UTC
- **Markdown Format**: Clean, readable format for each day's events
- **Manual Trigger**: Can be triggered manually via GitHub Actions
  
---

## 📁 Project Structure

```
today-in-history-logger/
│
├── history_logger.py     ← Main Python script
├── requirements.txt      ← Python dependencies
├── README.md            ← This file
├── history/             ← Contains daily markdown files
└── .github/
    └── workflows/
        └── history.yml  ← GitHub Action (runs daily)
```
---

## 🚀 How It Works

1. **Daily Execution**: GitHub Actions runs every day at 5 AM UTC
2. **API Fetch**: Fetches historical data from the History API
3. **Random Selection**: Picks 3 random events from the day's historical events
4. **Markdown Generation**: Creates a formatted markdown file

## 📅 Sample Output

Each day generates a file like `history/2025-01-15.md`:

```markdown
# Today in History - January 15

## Event 1
📅 Year: 1759  
📝 Event: The British Museum opens to the public in London

## Event 2
📅 Year: 1929  
📝 Event: Martin Luther King Jr. is born in Atlanta, Georgia

## Event 3
📅 Year: 2001  
📝 Event: Wikipedia is launched by Jimmy Wales and Larry Sanger
```
---

## 🛠️ Setup Instructions

### 1. Fork or Clone This Repository

```bash
git clone https://github.com/yourusername/today-in-history-logger.git
cd today-in-history-logger
```

### 2. Push to GitHub

```bash
git add .
git commit -m "Initial commit: Today in History Logger"
git push origin main
```

### 3. Enable GitHub Actions

- Go to your repository on GitHub
- Navigate to the "Actions" tab
- The workflow will automatically start running daily

### 4. Manual Testing (Optional)

You can test the script locally:

```bash
pip install -r requirements.txt
python history_logger.py
```
---

## ⚙️ Configuration

### GitHub Actions Schedule

The workflow runs daily at 5 AM UTC. To change the schedule, edit `.github/workflows/history.yml`:

```yaml
schedule:
  - cron: '0 5 * * *'  # Change this to your preferred time
```
---

### Manual Trigger

You can manually trigger the workflow:
1. Go to the "Actions" tab in your repository
2. Click on "Daily History Logger"
3. Click "Run workflow"

---

## 🔧 Customization

### Change Number of Events

Edit `history_logger.py` line 23:
```python
selected_events = random.sample(events, 3)  # Change 3 to your preferred number
```

### Change Commit Message

Edit `.github/workflows/history.yml` line 25:
```yaml
git commit -m "📚 Update Today in History for $(date +'%Y-%m-%d')"
```
### Add More Historical Data Sources

You can modify the API URL in `history_logger.py` to use different historical data sources.

---
## 🤝 Contributing

Feel free to fork this repository and customize it for your needs!

