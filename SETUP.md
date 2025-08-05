# 🚀 Quick Setup Guide

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `today-in-history-logger` (or any name you prefer)
3. Make it **Public** (required for GitHub Actions to work)
4. **Don't** initialize with README, .gitignore, or license (we already have these)

## Step 2: Push to GitHub

Run these commands in your terminal:

```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/today-in-history-logger.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Actions

1. Go to your repository on GitHub
2. Click on the **"Actions"** tab
3. You should see "Daily History Logger" workflow
4. Click on it and then click **"Run workflow"** to test it manually
5. The workflow will now run automatically every day at 5 AM UTC

## Step 4: Verify It's Working

1. After running the workflow manually, check the **"history"** folder
2. You should see a new markdown file with today's date
3. Check your GitHub profile - you should see a green square for today! 🟢

## 🎯 What Happens Next

- **Daily at 5 AM UTC**: GitHub Actions will automatically run
- **New commit**: A new historical events file will be created and committed
- **Green squares**: Your GitHub activity streak will be maintained
- **Historical knowledge**: You'll build a collection of daily historical events

## 🔧 Customization Options

### Change Schedule
Edit `.github/workflows/history.yml`:
```yaml
schedule:
  - cron: '0 5 * * *'  # Change to your preferred time
```

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

## 🆘 Troubleshooting

### If GitHub Actions doesn't run:
1. Check if the repository is **public**
2. Go to Settings → Actions → General → Allow all actions
3. Make sure the workflow file is in `.github/workflows/`

### If you get permission errors:
1. Go to Settings → Actions → General → Workflow permissions
2. Select "Read and write permissions"

---

**🎉 You're all set! Your GitHub activity streak is now automated!** 