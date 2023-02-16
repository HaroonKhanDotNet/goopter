from selenium import webdriver
from selenium.webdriver.common.by import By




def GiftCard_main(chromeBrowser):
     chromeBrowser.get('https://admin-dev.goopter.com/giftCards')


def giftcard_link(chromeBrowser):     
     giftcard_link = chromeBrowser.find_element(By.XPATH,"//li[8]")
     giftcard_link().click
def three_dots()