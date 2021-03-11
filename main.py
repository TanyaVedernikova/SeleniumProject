from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pandas import DataFrame, ExcelWriter
import pandas as pd

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

    for key, val in  name_of_animal_and_count_of_metrs.items():
       if val == '':
           name_of_animal_and_count_of_metrs.update({key : 2})
       else:
           val_new = val.replace(' METERS DEEP', '')
           name_of_animal_and_count_of_metrs.update({key: int(val_new) + 12})

    name_of_animal_and_count_of_metrs.update({'MANATEE': 6})


#    df = pd.DataFrame(data = name_of_animal_and_count_of_metrs,index = [0])
#    df = (df.T)
#    df.to_excel('C:/Users/tatyana.vedernikova/Desktop/New/file111.xlsx')

    for key, val in  name_of_animal_and_count_of_metrs.items():
        print(key, '   ', val)



main()