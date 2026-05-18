
def download_video(url):
    from pathlib import Path
    import yt_dlp
    Path("videos").mkdir(exist_ok=True)

    # Save inside videos/ using the video title as the filename
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s",
        "quiet": True,
        "socket_timeout": 30,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([url])

        return {
            "url": url,
            "status": "success",
            "error": "",
        }

    except Exception as error:
        return {
            "url": url,
            "status": "failed",
            "error": str(error),
        }
    



def read_video_urls(csv_path):
    import csv
    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        url_list = []
        
        for row in reader:
            url_list.append(row['url'])
        
        return url_list
    
def get_video_metadata(url):
    import yt_dlp
    ydl_options = {
        "quiet": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(url, download=False)

    return {
        "title": info.get("title"),
        "duration": info.get("duration"),
        "uploader": info.get("uploader"),
        "view_count": info.get("view_count"),
        "ext": info.get("ext"),
        "url": url,
    }


