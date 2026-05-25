# WhileIRest 🤖

Automation scripts that do the boring stuff for you — built with Python.

## Projects

### Day 1 — File Organiser
Automatically sorts your Downloads folder into subfolders by file type.
- Images, PDFs, Videos, Music, Code, Others
- Built with: `os`, `shutil`

## Day 2 — Email Reminder Bot

Sends scheduled daily reminder emails automatically.

- Morning, afternoon and evening reminders
- Bot runs in background watching the clock
- Built with: `smtplib`, `schedule`

### How to run
1. Generate a Gmail App Password (myaccount.google.com/apppasswords)
2. Create `config.py` with your credentials
3. Run: `python day2_emailbot.py`

### What I learned
- SMTP protocol — how emails actually travel
- try/except error handling
- List of dictionaries — Lecture 3 + 4
- while True loop keeping bot alive — Lecture 5
- Functions for reusable logic — Lecture 6

## Coming soon
- [ ] Day 3: Web Scraper
