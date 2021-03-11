from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def main():
    name_of_animal_and_count_of_metrs = {}
    driver = webdriver.Chrome()
    driver.get("https://neal.fun/deep-sea/")
    elem = driver.find_elements_by_class_name("eNQuho")
    for i in range(len(elem)):
        actions = ActionChains(driver)
        actions.move_to_element(elem[i]).perform()
        metrs = driver.find_elements_by_class_name('hobqQZ')
        for m in metrs:
            name_of_animal_and_count_of_metrs.update({elem[i].text : m.text})
            if  name_of_animal_and_count_of_metrs.get(elem[i]) == name_of_animal_and_count_of_metrs.get(elem[i-1]):
                actions = ActionChains(driver)
                header = driver.find_elements_by_class_name("jZUSDr")
                for h in header:
                    actions.move_to_element(h).perform()
                    actions = ActionChains(driver)
                    actions.move_to_element(elem[i]).perform()
                    name_of_animal_and_count_of_metrs.update({elem[i].text: m.text})



    print(name_of_animal_and_count_of_metrs)
    print(len(name_of_animal_and_count_of_metrs))





main()