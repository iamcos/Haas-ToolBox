from requests_html import HTMLSession
import pyppdf.patch_pyppeteer
session = HTMLSession()

page = session.get('https://app.haasonline.com/')
page = page.html.render()
print(page.html.search('#email'))