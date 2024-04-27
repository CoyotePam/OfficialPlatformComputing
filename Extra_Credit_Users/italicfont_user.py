import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def count_elem(driver, tag_name):
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")
    
    # Define the tag name to search for
    tag = "i"
    
    total_reward_time = 0
    
    # Reward time for each tag
    reward_time = 10
    
    # Count the occurrences of italic font
    num_italic_fonts = count_elem(driver, tag)
    
    # Calculate the total reward time based on the number of italic fonts found
    total_reward_time = reward_time * num_italic_fonts
    
    # Simulate user presence for the total reward time
    time.sleep(total_reward_time)
    
    # Quit the browser
    driver.quit()
    
    print("Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()
