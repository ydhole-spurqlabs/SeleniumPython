from selenium.webdriver.common.by import By
import time
from Pages.BasePage import BasePage


class CalculatorPage (BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context

        self.calculatebtn_xpath = "//span[text()= '=']"
        self.result_id = "sciOutPut"

    def enter_number(self, table):
        num1 = table[0][0]
        print(num1)
        operator = table[0][1]
        num2 = table[0][2]
        for i in range(0, len(num1)):
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//span[text()= '" + num1[i] + "']").click()
            time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()= '" + operator + "']").click()
        time.sleep(2)
        for j in range(0, len(num2)):
            self.driver.find_element(By.XPATH, "//span[text()= '" + num2[j] + "']").click()
            time.sleep(2)

    def calculatebtn_click(self):
        self.driver.find_element(By.XPATH, self.calculatebtn_xpath).click()

    def verify_result(self):
        try:
            act_result = self.driver.find_element(By.ID, "sciOutPut").text()
            print(act_result)
            exp_result = " 352456"
            assert act_result == exp_result, "Test passed"
            self.driver.close()
        except:
            self.driver.close()
            assert False, "Test failed"
