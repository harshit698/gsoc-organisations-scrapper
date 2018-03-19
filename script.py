from flask import Flask,jsonify
from flask import render_template
import requests
from bs4 import BeautifulSoup as bsoup

import json

app=Flask(__name__)

@app.route('/orgs')
def orgs():
	my_url='https://summerofcode.withgoogle.com/archive/2017/organizations/'
	original ="https://summerofcode.withgoogle.com"

	result = list()

	response = requests.get(my_url)
	html = response.content
	soup = bsoup(html,"html.parser")
	organizations = soup.findAll("li",{'class': 'organization-card__container'})

	counter = 0
	for organization in organizations:
		page_url=organization.find('a',{'class':'organization-card__link'})
		organization_name=organization['aria-label']

		about=organization.find('div',{'class':'organization-card__tagline font-black-54'})
		about=about.text
		page_link=original+page_url['href']
		page = requests.get(page_link)
		if page.status_code != 200:
			break
		page_link=original+page_url['href']
		response1 = requests.get(page_link)
		html1=response1.content
		soup1=bsoup(html1,"html.parser")
		organization_link=soup1.find("a",{"class":"org__link"})
		organization_link=organization_link.text

		technologies=soup1.findAll("li",{"class":"organization__tag organization__tag--technology"})
		tech = []
		for t in technologies:
			tech.append(t.text)

		major_topics=soup1.findAll("li",{"class":"organization__tag organization__tag--topic"})

		topics = []
		for q in major_topics:
			topics.append(q.text)

		# contact=soup1.find("a",{"class":"md-primary org__meta-button md-button md-ink-ripple md-soc-theme"})
		# contact=contact.text
		counter += 1
		print(counter)
		result.append({
			'organization_name': organization_name,
			'description': about,
			'link': organization_link,
			'technologies':tech,
			'topics': topics
			})
		# if(counter == 20):
		# 	break
	print("~")
	print(result)
	return json.dumps(result)
if __name__ == "__main__":
	app.run(debug=True)