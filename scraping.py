from bs4 import BeautifulSoup as bsoup
import requests 

my_url='https://summerofcode.withgoogle.com/archive/2017/organizations/'
original = "https://summerofcode.withgoogle.com"

response = requests.get(my_url)
html = response.content
soup = bsoup(html,"html.parser")
w, h = 300,20;
array1= [[0 for x in range(w)] for y in range(h)] 
array2= [[0 for x in range(w)] for y in range(h)] 
organizations = soup.findAll("li",{'class': 'organization-card__container'})
k=0,l=0
for organization in organizations:
	page_url=organization.find('a',{'class':'organization-card__link'})
	organization_name=organization['aria-label']

	about=organization.find('div',{'class':'organization-card__tagline font-black-54'})
	about.text

	page_link=original+page_url['href']
	response1 = requests.get(page_link)
	html1=response1.content
	soup1=bsoup(html1,"html.parser")

	organization_link=soup1.find("a",{"class":"org__link md-soc-theme"})
	organization_link=organization_link.text

	technologies=soup1.findAll("li",{"class":"organization__tag organization__tag--technology"})
	i=0
	for t in technologies:
		array1[k][i]=t.text
		i=i+1
	k=k+1
	j=0

	major_topics=soup1.findAll("li",{"class":"organization__tag organization__tag--topic"})

	for q in major_topics.text:
		array2[l][j]=q.text
		j=j+1
	k=l+1

	contact=soup1.find("a",{"class":"md-primary org__meta-button md-button md-ink-ripple md-soc-theme"})
	contact=contact.text

