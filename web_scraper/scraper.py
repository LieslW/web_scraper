from bs4 import BeautifulSoup
import requests


url = 'https://en.wikipedia.org/wiki/History_of_the_Internet'


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(title='Wikipedia:Citation needed')
    counter = 0

    for cites_needed in results:
        counter += 1

    print(f"The Wikipedia page at url: {url} needs {counter} citations!")
    return counter


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(title="Wikipedia:Citation needed")
    text_cites_needed_for = []
    for result in results:
        text_cites_needed_for.append(result.parent.parent.parent.text)

    print("The follow text needs citation verification")
    for item in text_cites_needed_for:
        print(item)


get_citations_needed_count(url)
get_citations_needed_report(url)






############################################ NOTES BELOW #########################################################


# # results = soup.find(class_="course-details")
# #
# # ^^ COURSE DETAILS part is just some customization but results does the same thing
#
#
# ###############
# # step 1
# # Let's scrape Code Fellows site to get a quick feel for what's covered in 401 Python Course.
# #
# # Big Note: I checked with owners of the web site about scraping. That's not legally required (there was even a Supreme Court case about it!) but it's a best practice.
# # In this case I was steered toward the staging site vs. live one so our experemints didn't confuse their analytics.
# #
# # We need an http client to make an http request and get access to web page content.
# # In earlier courses you probably used axios or superagent
# # In Python the most popular client is called requests
# # pip install requests
# ###############
#
#
# # URL = "https://testing-www.codefellows.org/courses/code-400/"
#
#
# ###############
# # step 2
# # Once we have the content it will be in raw html form, which is great for a browser, but not as easy for a human being to read.
# # So let's see if we can make sense of the raw html by parsing it
# ###############
#
#
# # BeautifulSoup can parse many types of content.
# # We're parsing html so let BeautifulSoup know
# # conventionally you store the BeatifulSoup instance in a variable named soup
#
# ###############
# # step 3
# # The soup instance has powerful capabilities for finding one or many elements based on different criteria
# ###############
#
# # here we're finding the first element with the given class
# # NOTE: use class_ since class by itself is a Python keyword
#
# # calling prettify method makes output a lot easier to read
# # print(results.prettify())
#
# ###############
# # step 4
# # We can then perform finds on previously found items
# # In this case we want to find all instead of just one
# ###############
#
# titles = results.find_all("h3")
#
# ###############
# # step 5
# # result of find_all is iterable and can be used in for loops
# ###############
# # for title in titles:
# #     print(title.text)
#
# ###############
# # step 6
# ###############
#
# # find_all is so common there's a shortcut
# anchors = results("a")
#
# # for anchor in anchors:
# #     print(anchor)
#
# ###############
# # step 7
# ###############
#
# # ResultSets are iterable and can be used in comprehensions
# links = [anchor["href"] for anchor in anchors]
#
# # print(links)
#
# ###############
# # step 8
# ###############
# python_link = links[1]
# python_url = "https://testing-www.codefellows.org" + python_link
# python_response = requests.get(python_url)
# python_soup = BeautifulSoup(python_response.content, "html.parser")
# article = python_soup("article")[1]
# list_items = article.select("ul li ul li")
#
# # get details about the object you're working with
# # print(dir(titles[1]))
#
# print(titles[1].text)
# for li in list_items:
#     print(li.text)
