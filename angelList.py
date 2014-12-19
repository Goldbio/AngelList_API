
import requests, re


def get_search( query, search_type ):
	r=requests.get( 'https://api.angel.co/1/search?query='+str(query)+'&type='+search_type  )
	return r.json()



def get_tag( query, search_type) :
	# search_type : children , parents , startups, users 
	page=1
	result=[]
	while 1:
		r=requests.get('https://api.angel.co/1/tags/'+str(query)+'/'+search_type+'?page='+str(page) )
		r_json=r.json()
		result.append( r_json[ search_type ] )
		if r_json['last_page'] == r_json['page'] :
			return result 
		else :
			page+=1
		

	return result 
