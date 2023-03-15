
import sys, os   
from sys import platform                                                        
from PySide2.QtWidgets import QApplication, QPushButton, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
import darkdetect as d            
import qdarktheme  
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def resetAllReg():
    # sets registers from 0 - 12  to 0
    regNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for rNum in regNum:

        driver.find_element('id', f'reg_value_r{rNum}').click()
        # sets register to 0
        ActionChains(driver)\
            .send_keys("0000000")\
            .send_keys(Keys.RETURN)\
            .perform()

def nextAddress(address, h, index):
    """
    address is the address being modified.
    h is what is the new character inserted at index.
    """
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    
    return address[:index] + hex[h] + address[index + 1:]

def clearHorizonMem(elem):

    # clear horizontally @ address
    ActionChains(driver)\
                .move_to_element(elem)\
                .click()\
                .send_keys("aa")\
                .send_keys(Keys.RETURN)\
                .move_by_offset(70, 0)\
                .click()\
                .perform()
    
    for i in range(0, 15):
        
        ActionChains(driver)\
                .send_keys("aa")\
                .send_keys(Keys.RETURN)\
                .move_by_offset(26, 0)\
                .click()\
                .perform()
    
def clearMem():
    # assuming memory address starts at 0x00000000
    initAddress = '0000000'

    driver.find_element(By.XPATH, "//i [@class='fas fa-search']").click() # makes sure on memory element
    driver.find_element(By.XPATH, "//input [@class='addr_box ui-autocomplete-input']").send_keys(initAddress)
    driver.find_element(By.XPATH, "//input [@class='addr_box ui-autocomplete-input']").send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, "//input [@class='addr_box ui-autocomplete-input']").clear()
    
    address = initAddress
    index = [0, 6] # index[0] = h, index[1] = slice index
    for j in range(0, 3): # 0x00000000 - 0x000000f0
        xpath = f"//div[@class='CodeMirror-gutter-elt' and contains(text(),'{address}')]"
        elem = driver.find_element(By.XPATH, xpath)

        clearHorizonMem(elem)
        
        index[0] += 1 # increment the h
        address = nextAddress(address, index[0], index[1])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'code.png'))
        self.setWindowTitle('CPUlator Solution')
        self.statusBar().showMessage('Created by: Sebastian Corcino')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)
        
        # decides window theme by computer settings
        if (d.theme() == 'Dark'):
            qdarktheme.setup_theme()
            self.setStyleSheet("QPushButton { color: White}")
        else:
            qdarktheme.setup_theme('light')
            self.setStyleSheet("QPushButton { color: Black}")
        
        # determine if mac os 
        if (platform == 'darwin'):
            self.move(QDesktopWidget().availableGeometry().topRight()) # move window to top right of the screen
        else:
            self.move(QDesktopWidget().availableGeometry().center()) # move window to top right of the screen

        self.resetRegBtn = QPushButton('Reset Register', clicked=lambda: resetAllReg())
        self.clearMemBtn = QPushButton('Clear Memory', clicked=lambda: clearMem())
        self.quitBtn = QPushButton('Quit', clicked=lambda: self.close())

        self.layout.addWidget(self.resetRegBtn)
        self.layout.addWidget(self.clearMemBtn)
        self.layout.addWidget(self.quitBtn)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

    def close(self):
        driver.quit()
        app.quit()
        
if __name__ == "__main__":

    # allows chrome to be run on docker image, http://localhost:4444
    # vnc view password: secret
    # options = webdriver.ChromeOptions()
    # options.add_argument('-ignore-ssl-errors=yes')
    # options.add_argument('-ignore-certificate-errors')
    # driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options) 

    driver = webdriver.Chrome() #.Chrome or .FireFox, to use local browser
    driver.maximize_window()
    driver.get('https://cpulator.01xz.net/?sys=arm')

    driver.implicitly_wait(10)

    # set size of memory to byte
    word = Select(driver.find_element('id', 'settings_numsize'))
    word.select_by_value("0")

    # set memory element to right stack
    memElem = driver.find_element(By.XPATH, "(//div [@class='tab-handle-text'])[10]")

    targetXPath = "//div [@class = 'dock-container dock-container-fill document-manager splitter-container-horizontal']"
    target = driver.find_element(By.XPATH, targetXPath)

    ActionChains(driver)\
            .click_and_hold(memElem)\
            .move_to_element_with_offset(target, 20, -5)\
            .release()\
            .perform()

    # adjust register view
    splitter = driver.find_element(By.XPATH, "//div [@class= 'splitbar-vertical']")

    # reset view to editor view 
    driver.find_element(By.XPATH, "(//div [@class='tab-handle-text'])[8]").click()

    ActionChains(driver)\
            .click_and_hold(splitter)\
            .move_by_offset(92, 0)\
            .release()\
            .perform()

    # create button window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())