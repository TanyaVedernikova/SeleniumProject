from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def main():
    name_of_animal = []
    driver = webdriver.Chrome()
    count_of_metrs = []
    driver.get("https://neal.fun/deep-sea/")
    elem = driver.find_elements_by_class_name("eNQuho")
    for i in elem:
        name_of_animal.append(i.text)
        actions = ActionChains(driver)
        actions.move_to_element(i).perform()
        metrs = driver.find_elements_by_class_name('hobqQZ')
        for m in metrs:
            count_of_metrs.append(m.text)
        


    print(count_of_metrs)
    print(len(name_of_animal))
    print(len(count_of_metrs))
    print(name_of_animal)





main()