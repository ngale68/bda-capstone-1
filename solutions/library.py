
def download_video(url):
    from pathlib import Path
    import yt_dlp
    Path("videos").mkdir(exist_ok=True)

    # Save inside videos/ using the video title as the filename
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

def read_video_urls(csv_path):
    import csv
    with open(csv_path, newline='') as file:
        reader = csv.DictReader(file)
        url_list = []
        
        for row in reader:
            url_list.append(row['url'])
        
        return url_list
    
#def time.perf_counter():
    #import time
    #start = time.perf_counter()

    

    #end = time.perf_counter()
    #elapsed = end - start
    
    #serial_time = round(elapsed, 2)
    #print(f"Serial execution: {serial_time}")
