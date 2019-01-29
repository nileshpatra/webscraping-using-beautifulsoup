from bs4 import BeautifulSoup
import requests
import pandas as pd 

r = requests.get('https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f299869f-a183-4a64-a887-6491356429b6&pf_rd_r=8FTWTF61Z05KPGH4T0X1&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_1')
soup = BeautifulSoup(r.text , 'lxml')

names= []
links = []
ratings = []
div = soup.find('div' , {'class' :'lister'})
rows = div.find_all('tr')
for row in rows[1:]:
	req_cols = row.find_all('td')
	#appending names
	req_col = req_cols[1]
	names.append(req_col.a.text)
	#appending links
	links.append('https://www.imdb.com/' + req_col.a.get('href'))
	#ratings
	req_col = req_cols[2]
	ratings.append(req_col.strong.text)

data = pd.DataFrame({'Name' : names , 'links' : links , 'Rating' : ratings})
data.to_csv('rating_file.csv' , sep = ',' , header = True , index = False)