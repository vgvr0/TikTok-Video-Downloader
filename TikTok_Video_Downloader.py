from tiktok_scraper import TikTokScraper

# URL of the TikTok video you want to download
video_url = "https://www.tiktok.com/@username/video/123456789"

# Destination directory where the downloaded video will be saved
output_dir = "/path/to/directory"

# Create an instance of TikTokScraper
scraper = TikTokScraper()

# Download the video
video_path = scraper.download_video(video_url, output_dir)

print("Downloaded video:", video_path)
