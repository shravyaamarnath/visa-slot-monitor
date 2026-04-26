# Visa Slot Monitor

## The Problem

In 2026, getting an H1B visa stamping appointment in India is extremely competitive. Slots open up and disappear within minutes. Manually refreshing visa availability websites throughout the day is impractical — by the time you notice a slot, it's gone.

I also couldn't monitor the official US visa appointment website directly. If it flagged my activity as automated, it could block my account — which would mean losing the ability to book at all, with serious consequences for my visa status.

So I needed a way to monitor third-party websites that track and publish visa slot availability, and get an instant alert the moment something opens up.

## How It Works

The monitor runs automatically every 5 minutes on GitHub's free cloud infrastructure (GitHub Actions), so it works 24/7 without needing my laptop to be on.

Here's what happens each run:

1. **Visit the pages** — A headless Chrome browser silently opens each tracking website, just like a real user would. It's configured to look like a normal browser so it isn't blocked.

2. **Extract the content** — It strips out ads, navbars, and other noise, leaving just the meaningful text on the page.

3. **Compare to last time** — It takes a fingerprint (hash) of the text and compares it to what was saved from the previous run. If they match, nothing changed. If they don't, something is new.

4. **Alert instantly** — If a change is detected, a Telegram message is sent immediately with details on what changed and a link to the page.

**Sites monitored:** All 5 US consulate locations in India (New Delhi, Mumbai, Chennai, Hyderabad, Kolkata) for both H1B Biometrics and Interview slots — 10 URLs in total, plus a general H1B availability tracker.

## Tech Stack
**Built using Claude Code**
- **Python + Playwright** — browser automation
- **GitHub Actions** — free cloud scheduler (runs every 5 min)
- **Telegram Bot API** — instant notifications
 
