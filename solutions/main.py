from library import download_video
from library import read_video_urls
from library import get_video_metadata

csv_path = "data/video_urls.csv"
metadata_csv_path = "data/video_metadata.csv"

# def sequential_download():
#    import time
#    start = time.perf_counter()

#    for url in read_video_urls(csv_path):
#        download_video(url)

#    end = time.perf_counter()

#    elapsed = end - start

#    serial_time = round(elapsed, 2)
#    print(f"Serial execution: {serial_time}")

# def parallel_download():
#     from multiprocessing import Pool
#     import time
    
#     start = time.perf_counter()
    
#     urls = read_video_urls(csv_path)
    
#     with Pool() as pool:
#         results = pool.map(download_video, urls)

#     end = time.perf_counter()
#     elapsed = end - start

#     parallel_time = round(elapsed, 2)
#     print(f"Parallel execution: {parallel_time}")


if __name__ == "__main__":
    #sequential_download()
    #parallel_download()
    from multiprocessing import Pool
    import time
    
    start = time.perf_counter()
    
    urls = read_video_urls(csv_path)
    
    with Pool() as pool:
        results = pool.map(download_video, urls)
    
    metadata_rows = []

    for url in urls:
        metadata = get_video_metadata(url)
        metadata_rows.append(metadata)

    # create the new CSV after the loop finishes

    import csv

    with open("data/video_metadata.csv", "w", newline="") as file:
        fieldnames = ["title", "duration", "uploader", "view_count", "ext", "url"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(metadata_rows)
    
    results = []
    
    for url in urls:
        result = download_video(url)
        results.append(result)
    print("Successful downloads:", len(results))

    for result in results:
        fail = 0
        if result["status"] == "failed":
            fail += 1
    print("Failed downloads:", fail)

    end = time.perf_counter()
    elapsed = end - start

    parallel_time = round(elapsed, 2)
    print(f"Parallel execution: {parallel_time}")