import time
from selenium import webdriver
import collections
import csv

def writeToCSV(filename: str, metrics: dict):
    with open(filename, mode="w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=metrics.keys())
        writer.writeheader()

       
        writer.writerow(metrics)


def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")
    
    metrics = collections.defaultdict(list)
    
    # Track presence time 
    SAMPLE_SIZE = 10
    start_time = time.time()
    
    for _ in range(SAMPLE_SIZE):
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
        metrics["Presence time (Seconds)"].append(presence_time)
            
        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")  
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")
        metrics["Scrolling (Pixels)"].append(current_scroll / scroll_height)
        
        time.sleep(2) 

    driver.quit()
    print(metrics)
    writeToCSV("metrics.csv", metrics)


if __name__ == "__main__":
    main()
