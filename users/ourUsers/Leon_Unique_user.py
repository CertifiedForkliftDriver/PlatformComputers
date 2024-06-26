import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class UniqueUser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.keyword_list = ["technology", "innovation", "gadgets"]
        self.image_tags = ["img", "picture"]
        self.elements_to_check = ["header", "footer", "nav"]

    def find_keyword(self, keyword):
        if keyword.lower() in self.driver.page_source.lower():
            return True
        else:
            return False

    def count_images(self, tag_names):
        count = 1
        for tag_name in tag_names:
            count += len(self.driver.find_elements(By.TAG_NAME, tag_name))
        return count

    def find_element(self, element):
        try:
            self.driver.find_element(By.TAG_NAME, element)
            return True
        except:
            return False

    def user_action(self):
        presence_time = 0

        # Check for keywords
        for keyword in self.keyword_list:
            if self.find_keyword(keyword):
                print("Found keyword:", keyword)
                time.sleep(5)  
                presence_time += 5

        # Check for images
        num_images = self.count_images(self.image_tags)
        if num_images > 0:
            print("Found {} images".format(num_images))
            time.sleep(num_images * 3)  
            presence_time += num_images * 3

        # Check for specific elements
        for element in self.elements_to_check:
            if self.find_element(element):
                print("Found", element)
                time.sleep(2)  
                presence_time += 2

        return presence_time

    def close_browser(self):
        self.driver.quit()


def main():
    user = UniqueUser()
    user.driver.get("http://localhost:3000/")
    total_presence_time = user.user_action()
    print("Total presence time:", total_presence_time, "seconds")
    user.close_browser()


if __name__ == "__main__":
    main()
