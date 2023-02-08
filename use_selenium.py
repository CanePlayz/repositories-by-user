import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_repo_info(name):

    # Create variables

    repos = []
    stars = []

    # Setup driver

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    # Get number of repositories

    number_repos = "0"

    driver.get("https://github.com/{}".format(name))
    spans = driver.find_elements("xpath", "//span")

    time.sleep(2)

    for span in spans:
        if span.get_attribute("class") == "Counter js-profile-repository-count":
            number_repos = span.text
            break
        else:
            continue

    # Convert to number of pages

    try:
        number_converted = int(number_repos)

    except ValueError:
        n = float(number_repos[:-1])
        number_converted = int(n * 1000)

    number_pages = number_converted // 30 + 1

    # Go through all pages

    for i in range(1, number_pages + 1):

        # Go to the necessary page

        driver.get(
            "https://github.com/orgs/{}/repositories?language=&page={}&q=&sort=name&type=all".format(
                name, i))

        # Find all boxes

        repositories_li = driver.find_elements(
            By.CSS_SELECTOR, "[class='Box-row']")

        # Go through all boxes

        for repo in repositories_li:

            title = repo.find_element(
                By.CSS_SELECTOR, "[itemprop='name codeRepository']").text

            repos.append(title)

            try:
                test = f"[href='/{name}/{title}/stargazers']"
                star = repo.find_element(
                    By.CSS_SELECTOR, test).text

            except NoSuchElementException:
                star = repo.find_element(
                    By.CSS_SELECTOR, f"[class='mr-3 color-fg-muted']").text

            stars.append(star)

    # Format list for dataframe

    list_for_df = []

    for i in range(len(repos)):
        list_for_df.insert(i, [repos[i], stars[i]])

    return (list_for_df)
