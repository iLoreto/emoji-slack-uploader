'''
Created on Apr 10, 2016

@author: iloreto
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os.path
from os import listdir
from os.path import isfile,join
if __name__ == '__main__':
    print("start")
    binaryPath = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
    profilePath = "/Users/[username]/Library/Application Support/Firefox/Profiles/20wd5tda.default"
    sourcepath = "/Users/[username]/Downloads/hubot-ingress-master/badges/"
    team_url = "https://[teamname].slack.com/customize/emoji"
    
    inputNameID = "emojiname"  
    inputImgID = "emojiimg"
    saveButtonPath = "/html/body/div/div[1]/section/div/form/div[2]/p[4]/input"
    
    profile = FirefoxProfile(profilePath)
    binary =  FirefoxBinary(binaryPath)
    browser = webdriver.Firefox(firefox_binary=binary,firefox_profile=profile)  
    browser.get(team_url) 
    browser.implicitly_wait(3)
    browser.switch_to_active_element()
    try:
        onlyfiles = [f for f in listdir(sourcepath) if isfile(join(sourcepath, f))]
        for fileinfo in onlyfiles:  
            fname = os.path.splitext(fileinfo)[0] 
            browser.switch_to_active_element()  
            browser.implicitly_wait(1)
            nameInput = browser.find_element_by_id(inputNameID)
            nameInput.send_keys(fname)
            imgInput = browser.find_element_by_id(inputImgID)
            imgInput.send_keys(sourcepath+fileinfo)
            saveButton = browser.find_element_by_xpath(saveButtonPath)
            saveButton.click()
    except (NoSuchElementException, TimeoutException):
        print("not logged in")
    browser.quit()
    print("stop")