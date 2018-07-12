#!/usr/bin/python

items = [{'owner': {'username': 'Arun'},'name': 'book','forsale': 'N','price': '20'},{'owner': {'username': 'Mercy'},'name': 'music','forsale': 'Y','price': '20'}]

#for item in items:
#	if item['owner']['username'] == 'Arun' and item['forsale'] == 'Y':
#		if item['name']:
#			print item['name']
#	else:
#		print 'No items for sale'

#print 'Updating items'

#for item in items:
#        if item['owner']['username'] == 'Arun' and item['forsale'] == 'N':
#		item['forsale']='Y'

#print 'Updated'

#for item in items:
#        if item['owner']['username'] == 'Arun' and item['forsale'] == 'Y':
#                if item['name']:
#                        print item['name']
#        else:
#
#                print 'No items for sale'
new_item = {}

def updated(new_item):

	items.append(dict(new_item))
	return items
item = updated(new_item)
print item

new_item['owner'] = {'username': 'Arun'}
new_item['name'] = 'new book'
new_item['price'] = '10'
new_item['forsale'] = 'N'

item = updated(new_item)
print item
				
