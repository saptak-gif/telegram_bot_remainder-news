import feedparser

RSS_FEEDS = {
    "🌍 World News": "https://feeds.reuters.com/reuters/topNews",
    "💻 Technology": "https://feeds.reuters.com/reuters/technologyNews",
}

def get_news():
    message = "📰 Daily Briefing\n\n"

    for category, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        message += f"{category}\n"

        if len(feed.entries) == 0:
            message += "• No news available.\n\n"
            continue

        for article in feed.entries[:3]:
            message += f"• {article.title}\n"

        message += "\n"

    return message
