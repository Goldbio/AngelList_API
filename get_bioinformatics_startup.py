
import requests, re


def get_search( query) :
	page=1
	result=[]
	while 1:
		r=requests.get('https://api.angel.co/1/tags/'+str(query)+'/startups?page='+str(page) )
		r_json=r.json()
		result.append( r_json['startups'] )
		if r_json['last_page'] == r_json['page'] :
			return result 
		else :
			page+=1
		


### MAIN  ###

market_tag = 182 # 182 = Bioinformatics 
res=get_search( market_tag )


for page in res:
	for s in page:
		if 'name' in s:
			followers=s['follower_count']
			name = s['name']
			date = re.sub( "T.*","", s['created_at'])
			quality = s['quality']
			concept = s['high_concept']
			markets =[  str( m['name'] ) for m in s['markets'] ]
			locations =[ str( l['name'] ) for l in  s['locations'] ]
			company_size= s['company_size']
			fund_raising=0				
			valuation=0
			if 'fundraising' in s:
				if s['fundraising'] != False:
					if 'raising_amount' in s['fundraising']:
						fund_raising= s['fundraising']['raising_amount']
					if 'pre_money_valuation' in s['fundraising']:
						valuation = s['fundraising']['pre_money_valuation']
			
			print name,'\t', fund_raising,'\t', valuation,'\t',quality, '\t', date,'\t',locations,'\t', company_size,'\t',followers,'\t',concept,'\t', markets

