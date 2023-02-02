from selenium.webdriver.common.by import By
import time
from Features.Pages.BasePage import BasePage


class BmiPage (BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.age_xpath = "//input[@id='cage']"
        self.height_xpath = "//input[@id='cheightmeter']"
        self.weight_xpath = "//input[@id='ckg']"
        self.calculatebtn_xpath = "//input[@value='Calculate']"
        self.actual_result_xpath = "//body[1]/div[3]/div[1]/div[4]/div[1]/b[1]"

    def age_input(self, Age):
        AgeInput = self.driver.find_element(By.XPATH, self.age_xpath)
        AgeInput.clear()
        AgeInput.send_keys(Age)
        time.sleep(2)

    def gender_radio(self, Gender):
        try:
            MaleGender = self.driver.find_element(By.XPATH, "//label[normalize-space()='" + Gender + "']")
            MaleGender.click()
            time.sleep(2)
        except:
            FemaleGender = self.driver.find_element(By.XPATH, "//label[normalize-space()='" + Gender + "']")
            FemaleGender.click()
            time.sleep(3)

    def height_input(self, height):
        HeightInput = self.driver.find_element(By.XPATH, self.height_xpath)
        HeightInput.clear()
        HeightInput.send_keys(height)
        time.sleep(3)

    def weight_input(self, weight):
        WeightInput = self.driver.find_element(By.XPATH, self.weight_xpath)
        WeightInput.clear()
        WeightInput.send_keys(weight)
        time.sleep(3)

    def calculatebtn_click(self):
        Calculatebtn = self.driver.find_element(By.XPATH, "//input[@value='Calculate']")
        Calculatebtn.click()
        time.sleep(3)

    def result_validation(self, expresult):
        try:
            Result = self.driver.find_element(By.XPATH, "//body[1]/div[3]/div[1]/div[4]/div[1]/b[1]")
            Actualresult = Result.text
            Expectedresult = expresult
            assert Actualresult == Expectedresult, "Expected Result Matched"
            time.sleep(5)
        except:
            self.driver.close()
            assert False, "Expected Result mismatched"
