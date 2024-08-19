from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

siteUrl = "https://codeforces.com/problemset/"
pageTitle = "Problemset - Codeforces"

questionNameList = []
questionLinkList = []
questionDifficultyList = []

def writeToFile():
    file = open('questionsLinkCodeforces.txt','w')
    for x in range(questionLinkList.__len__()):
        file.write(questionLinkList[x]+"\n")
    file.close()

def openBrowser(url):
    print("    ----------->  Opening Browser")
    Options = webdriver.ChromeOptions()
    Options.add_argument("--ignore-certificate-errors")
    Options.add_experimental_option("excludeSwitches", ["enable-logging"])
    Options.add_argument("--incognito")
    Options.add_argument("--headless")
    
    #normal - browser opens
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    
    #headless - browser runs in background
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=Options)
    
    driver.get(url)
    driver.maximize_window()
    return driver

def closeBrowser(browser):
    print("    ----------->  Closing Browser")
    browser.quit()
    
def fetchPageData(pageUrl):
    browser = openBrowser(pageUrl)
    time.sleep(3)
    pageSource = browser.page_source
    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_contains(pageTitle))
    
    if (browser.title == pageTitle):
        
        print(
            "    ----------->  parsing data "
        )
        
        newSoup = BeautifulSoup(pageSource, "html.parser")
        QuestionBlock = newSoup.find('table',class_="problems")
        QuestionList = QuestionBlock.find_all('tr')
        
        for i in range(1, QuestionList.__len__()):
            questionUrl = QuestionList[i].find('a')['href']
            questionUrl = "https://codeforces.com" + questionUrl  
            # print(questionUrl)
            questionLinkList.append(questionUrl)  
            
        print("    ----------->  saving data ")
        time.sleep(1)
        print("    ----------->  done ")
        closeBrowser(browser)
    else :
        print("    ----------->  connection failed ")
        return
    
def getData():
    try:
        browser = openBrowser(siteUrl)
        time.sleep(2)
        pageSource = browser.page_source
        # print(browser.title)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.title_contains(pageTitle))
        soup = BeautifulSoup(pageSource, "html.parser")
        
        if (browser.title == pageTitle):
            
            #fetching total number of pages
            totalQuestions = soup.find('div',class_="pagination").find_all('span')
            index = totalQuestions.__len__() - 1
            # print(index)
            totalPages = int(totalQuestions[index].text)
            print("Total Pages : ", totalPages)
            # return
            closeBrowser(browser)
            
            #Fetching data from each page
            for page in range(1, totalPages+1):
                print(
                    f"    ----------->  Fetching data from page : {page} of {totalPages} \n\n"
                )
                pageUrl = siteUrl + 'page/' + str(page)
                fetchPageData(pageUrl)  
            
            print("    ----------->  done all pages")
            print(f" total {questionLinkList.__len__()} question fetched")  
            writeToFile()
        
        else :
            print("    ----------->  connection failed ")
            return
            
    except Exception as e:
        print("    ----------->  Error in getData() : ", e)
        return    
    

if __name__ == "__main__":
    getData()