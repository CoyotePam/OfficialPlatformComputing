import time
from selenium import webdriver


c
def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0
    keywords = ["Ontario","Iowa"]
    for key in keywords:
        if findKeyword(driver,key):
            total_reward_time += reward_time
            time.sleep(reward_time)
    

    driver.quit()
    print("Presence Time:", total_reward_time)
    

if __name__ == "__main__":
    main()
