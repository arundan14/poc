#!/usr/bin/python
keys = ['owner','name','forsale','price']
items = [{'owner': {'username': 'Arun'},'name': 'book','forsale': 'N','price': '20'},{'owner': {'username': 'Mercy'},'name': 'music','forsale': 'Y','price': '20'}]
newitem = [{'owner': {'username': 'Arun123'},'name': 'book123','forsale': 'N','price': '200'}]
for item in items:
	if item['owner']['username'] == 'Arun' and item['forsale'] == 'N':
	 if item['name']:
			newitem.append(dict(item))
#			newitem = item.copy()
#			values=[item['owner'],item['name'],item['forsale'],item['price']]
#			newitem.append(dict(zip(keys,values)))
			print item
#			print newitem['owner']['username']
#			print newitem
	 else:
		print 'No items for sale'
print len(newitem)
#print 'Updating items'
#print newitem
for itemx in newitem:
        if itemx['owner']['username'] == 'Arun' and itemx['forsale'] == 'N':
		print itemx

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
#print item

new_item['owner'] = {'username': 'Arun'}
new_item['name'] = 'new book'
new_item['price'] = '10'
new_item['forsale'] = 'N'

item = updated(new_item)
#print item

	
