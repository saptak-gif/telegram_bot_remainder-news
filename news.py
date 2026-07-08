import feedparser

RSS_FEEDS = {
    "🌍 BBC World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "💻 BBC Technology": "https://feeds.bbci.co.uk/news/technology/rss.xml",
}

def get_news():
    message = "📰 Daily Briefing\n\n"

    for category, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        # Debug output (visible in GitHub Actions logs)
        print(f"{category}: {len(feed.entries)} articles found")

        message += f"{category}\n"

        if not feed.entries:
            message += "• No news available.\n\n"
            continue

        for article in feed.entries[:3]:
            message += f"• {article.title}\n"

        message += "\n"

    return message
