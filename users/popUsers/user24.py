import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def findKeyword(driver, keyword)->bool:
    print(driver.page_source.lower())
    return keyword.lower() in driver.page_source.lower()

def countTagElem(driver, tag_name)->int:
    count = 0
    for tags in tag_name:
        count += len(driver.find_elements(By.TAG_NAME, tags))
    return count

def clickLink(driver, tag_name):
    links = driver.find_elements(By.TAG_NAME, tag_name)
    for link in links:
        link.click()

def userActions(action, driver, rewardTime, reqList)->float:
    totalRewardTime = 0
    if action.upper() == "KEYWORD":
        for keyword in reqList:
            if findKeyword(driver, keyword):
                print("found", keyword)
                totalRewardTime += rewardTime
                time.sleep(rewardTime)
            else:
                print(keyword, "not found")
    elif action.upper() == "ELEMENT":
        numImages = countTagElem(driver, reqList)
        totalRewardTime += numImages*rewardTime
        time.sleep(totalRewardTime)
    elif action.upper() == "LINK":
        numLinks = countTagElem(driver, reqList)
        totalRewardTime += rewardTime*numLinks
        time.sleep(rewardTime)
        time.sleep(totalRewardTime)
    return totalRewardTime

def userAction(driver):
    #Initialize browser
    rewardTime = 10
    totalRewardTime = 0
    keywords = ["student", "CSUSB"]
    tagNames = ["img"]
    link = ["a"]
    totalRewardTime += userActions("KEYWORD", driver, rewardTime, keywords)
    totalRewardTime += userActions("IMAGE", driver, rewardTime, tagNames)
    totalRewardTime += userActions("LINK", driver, rewardTime, link)

    print("Presence Time", totalRewardTime)

if __name__ == "__main__":
    main()
