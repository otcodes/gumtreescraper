#import the necessary module for scraping#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS

filepath = "C:\\Users\\Public\\Documents\\the urls.txt"#path to text file where the scraper saves the links#
numpath = "C:\\Users\\Public\\Documents\\numbers.txt"#path to text file where the numbers are saved
allurls =[]#variable used to store the links from each page result#
totalpage = 0#variable used for iteration of the result page

#function to check if the ads page has a phone number on it#
def looking():
    try:
        browser.implicitly_wait(10)#letting selenium wait for 10 seconds for carrying out other action on the function#
        reveal = browser.find_element_by_id("reply-panel-reveal-btn")#locating the reveal button on the page#
        browser.execute_script("arguments[0].click();", reveal)#using javascript to click on the button#
        browser.implicitly_wait(20)#waiting for 10 seconds more#
        thepagen = BS(browser.page_source, 'lxml')#parsing the source code with beautifulsoup#
        thenum = thepagen.select('.txt-large.txt-emphasis.form-row-label')
        thenumber = thenum[0].text
        then.write("%s\n" % thenumber.text)#adding the number to the file#
    except:
        print("no number on this page")#print this if no number is found on the page#


options = webdriver.ChromeOptions()#setting options for the chrome browser#
options.add_argument('--ignore-certificate-errors')#tells chrome to ignore any certificate error. added this course my internet connection is slow#
browser = webdriver.Chrome(chrome_options=options)#making use of the option set#
browser.set_page_load_timeout(300)#timeout of page load set to 5 minutes(300 seconds)
browser.get("https://www.gumtree.com/property-to-share?seller_type=private")#visiting the result page#
browser.implicitly_wait(3)#tells the page to wait for 3 seconds#
theurls = open(filepath, 'a')#opening the file with append option#
#clearing the file of previous contents#
theurls.seek(0)
theurls.truncate()
theurls.close()#closing the file#
#creating a loop to copy the urls for the results#
while totalpage < 9:
    element=BS(browser.page_source, 'lxml')#parsing the page with beautifulsoup#
    allurls = element.findAll('a',{'class':'listing-link'})#collecting all result the urls on the page#
    #loop to add the urls to the file#
    for item in allurls:
        theurls = open(filepath, 'a')#opening up the url file with append option#
        theurls.write("%s\n" % item.get('href'))#adding the url to the file#
    theurls.close()#close file#
    #finding and clicking on the next button#
    nextbtn = browser.find_element_by_class_name("pagination-next")
    nextbtn.click()
    #waiting for the results to be present#
    WDW(browser, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "natural")))
    browser.implicitly_wait(3)#waiting another 3 seconds#
    totalpage += 1#adding 1 to the totalpage value#
#opening the number file and clearing it#
then = open(numpath, 'a')
then.seek(0)
then.truncate()
#collecting the urls from the url file and adding them to a list#
with open(filepath) as f:
    thefile = f.read().splitlines()#seperating them at every new line it detects#
f.close()
thefile = [x for x in thefile if x != ""]#removing empty values from the url list#
lenthefile = len(thefile)#getting the length of the url list#
lenthefile -= 1#subtract 1 from the length of the url list
#loop to open each urls and retrieve the nunbers#
while lenthefile >= 0:
    browser.set_page_load_timeout(300)#setting timeout for page load#
    browser.get("http://www.gumtree.com" + thefile[lenthefile])#opening the url#
    looking()#calling the function#
    lenthefile -= 1#subtracting 1 from the lenght of the url list#
then.close()#close the file containing the numbers#
browser.quit()#quit the browser#
quit#end the program#
