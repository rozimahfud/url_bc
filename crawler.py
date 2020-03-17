import re
import urllib.request
from bs4 import BeautifulSoup

def getJsUrl(url):
	try:
		html = urllib.request.urlopen(url)
		src = html.read()
		soup = BeautifulSoup(src, features="lxml")
		scripts = soup.findAll("script", src=re.compile("\\.js"))
		list_url = []
		for tag in scripts:
			jsHref = tag.get("src")
			jsHref = jsHref.split("?")[0]
			if "http" not in jsHref:
				jsHref = "http:" + jsHref
			list_url.append(jsHref)
		return list_url
	except Exception as data:
		print(data)
		return []

def getJsCode(url):
	try:
		page = urllib.request.urlopen(url)
		src = page.read().decode("utf-8")
		return src
	except Exception as data:
		print(data)
		return ""

def getInsideCode(url):
	try:
		page = urllib.request.urlopen(url)
		src = page.read()
		soup = BeautifulSoup(src, features="lxml")
		scripts = soup.findAll("script",type="text/javascript")
		list_js = []
		for s in scripts:
			if s:
				list_js.append(s.text)
		return list_js
	except Exception as data:
		print(data)
		return []