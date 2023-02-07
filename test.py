from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.maximize_window()


driver.get(
    "https://github.com/orgs/powershell/repositories?language=&page=1&q=&sort=name&type=all")

# Find all links on the page

""" links = driver.find_elements(
    "xpath", "//a[.//svg[.//path[d='M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z']]]")

print(len(links))


for link in links:
    print(link.get_attribute("href")) """

user = "PowerShell"

repositories_li = driver.find_elements(By.CSS_SELECTOR, "[class='Box-row']")

for repo in repositories_li:

    title = repo.find_element(
        By.CSS_SELECTOR, "[itemprop='name codeRepository']").text

    try:
        test = f"[href='/{user}/{title}/stargazers']"
        star = repo.find_element(
            By.CSS_SELECTOR, test).text

    except NoSuchElementException:
        star = repo.find_element(
            By.CSS_SELECTOR, f"[class='mr-3 color-fg-muted']").text

    print(title, star)
