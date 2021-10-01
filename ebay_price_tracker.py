from bs4 import BeautifulSoup
import requests
import time
import sys
from send_email import send
from time_machine import trigger


URL_from_args = sys.argv[1]
PRICE_from_args = sys.argv[2]
INPUT_time = int(sys.argv[3])    #for now, it's accepting seconds
PRICE_from_args_modified = "US ${0}".format(PRICE_from_args)



URL = 'https://www.ebay.com/itm/373661492896?_trkparms=ispr%3D1&hash=item56fff5e6a0:g:TwQAAOSwYEdg~3IU&amdata=enc%3AAQAGAAACkPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsSafTQYbq3L7RBVAMi0K9cw88Gfl1Q%252FV1rcTb%252BrXc6Zjh6aAi6j9qVzGe5EiHICRgq47bldCIWLEIc0ULLmJUS78B8%252F2QGL08e8%252FoGIpx18hv8Wt%252BY7bc8rSU0uOCC5tdB9%252BSQC4SISH84K26rtqvyLu1e4bvwnpz3HGOHzu7DAF2AZz%252BItsWuJjd%252Bh4RZ8%252BTZPyLnn1Vfip8uiaCCAk7mO6C6UhUmwh%252FtFiAfBcrUsgltR%252FgX%252FAhv8TVERwTWqt3HKWjCAiINNDoz3vZI%252F4tIdz51BjMbXSUyX%252FtJ4q9qpzzgEJQTvzOwq2cyiyX28EoQ%252BNvWFqcBZK%252BMp8pDiFufT3EU%252FMHrnRva%252FoF4k0BCsBboUJDV03j%252FjhaciVhHXE%252FJWplmQ4zYQmhxvYUcYs05p50CMN6L7bjn8mCnXclhkd0cOrnlyw%252BwC57zMYURf%252F07eZF9B%252Bizf4GZkMxGWovZQyVcwMcKfxCjfxO2rZkvNXBUWynEOVuAte0iwlOjnE%252BDBrc%252FXFqEWDCD%252FB0PHvwqnhqT%252BNaeZ1ZTUVt8arY1jRVdAcqWEky%252BK%252F3W%252FB18qayiEaHOzuQf0T0E0a7edP60p4vFDuURL8Z%252B8FiIxKwdt467TklmgEfIWOiNliNuNyERi%252Ff3D81%252BsBAVzn7t5YNPtdTRi%252BksQphl%252BfOUlcUyzSNbkPC8FUN6npNgjtOUUaecsRlTwLe%252Bh%252ByPheQNYwCMFc3zAKShN3elawKyBQ%252B2obiSgtzvOPvYjg%252BtXLONC13KO3kBI4G04JKHw68PQ2iCha5Vd1wuH7mMH5VXe4i%252FXGh47AVpKrRDCH11huWL9Amh%7Campid%3APL_CLK%7Cclp%3A2334524'

URL_2 = 'https://www.ebay.com/itm/254877542786?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908105057%26meid%3D2190290f2352429ca520da3398a45121%26pid%3D100675%26rk%3D3%26rkt%3D3%26sd%3D373661492896%26itm%3D254877542786%26pmt%3D1%26noa%3D1%26pg%3D2380057%26brand%3DUnbranded&_trksid=p2380057.c100675.m4236&_trkparms=pageci%3Af1914f7c-fc99-11eb-b509-c61544e88061%7Cparentrq%3A4225a20d17b0a0f2cc9ae22dffd83c42%7Ciid%3A1'

URL_3 = 'https://www.ebay.com/itm/224460576161?_trkparms=aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20200721145842%26meid%3D5819f32b4f53477588a632cfcf96694b%26pid%3D101259%26rk%3D1%26rkt%3D1%26itm%3D224460576161%26pmt%3D1%26noa%3D1%26pg%3D2380057%26algv%3DPersonalizedTopicsV2WithMLR%26brand%3DUnder+armour&_trksid=p2380057.c101259.m47269&_trkparms=pageci%3Ae9b86080-fca5-11eb-812e-7e4731ddc4d4%7Cparentrq%3A4274131717b0ad39306b6aa1ffccfd50%7Ciid%3A2'

response = requests.get(URL_3)
test_path = '/Users/steveliang/Desktop/Project/ebay_price_tracker/test_page.html'

# soup = BeautifulSoup(response.content, 'html.parser')
with open(test_path) as test:
    soup = BeautifulSoup(test, 'html.parser')


#getting title of the item
product_description = soup.find('h1', id='itemTitle').get_text()
product = 'Product Name: {0}'.format(product_description[16:])
print('Product Name: {0}'.format(product_description[16:]))

#getting price
price_description = soup.find('span', id='prcIsum').get_text()
current_price_num = float(price_description[4:8])
price = 'Price: {0}'.format(price_description)
print('Price: {0}'.format(price_description))

#getting shipping/return availability
# shipping_return_avalability = []
# for itemText in soup.findAll('div', {'class': 'w2b-cnt w2b-3 w2b-brdr'}):
#     shipping_return_avalability.append(itemText.find('span', class_="w2b-sgl").get_text())
# print('Shipping/Return Avalability: {0}'.format(shipping_return_avalability[1]))

#getting shipping details
shipping_info_0 = soup.find('span', id='fshippingCost').get_text().strip()
shipping_info_1 = soup.find('span', id='fShippingSvc').get_text().strip()
shipping_description = shipping_info_0 + ' ' + shipping_info_1
shipping = 'Shipping: {0}'.format(shipping_description)
print('Shipping: {0}'.format(shipping_description))

#getting return availability
return_description = soup.find('span', id='vi-ret-accrd-txt').get_text().strip()
_return = 'Return: {0}'.format(return_description)
print('Return: {0}'.format(return_description))


# #compare price changes
# check_price_frequency = 20   #5 seconds
# processing_time = 15
# print('Old Price: {0}'.format(current_price_str))
# print('Fetching Newest Updated Price...')
# time.sleep(check_price_frequency)

#TODO: figure out how to fetch the update price
update_price_str = soup.find('span', id='prcIsum').get_text()
update_price_num = float(update_price_str[4:8])

# print('Fetching is Done...')
# time.sleep(processing_time)
# print('Updated Price: {0}'.format(update_price_str))
# print('Price comparing...') 
# time.sleep(processing_time)

#LOGIC: if prices are different, show the difference and show the new price #phrase 1
#LOGIC: if prices are different, send the information as email/sms  #phrase 2
# price_difference = update_price_num - current_price_num
# print('Price Difference: {0}'.format(price_difference))
# if price_difference == 0:
#     print('The price of the item has not changed yet. Please run the script and check again later.')
# elif price_difference < 0:
#     print('The price of the item has been DROPPED! Price dropped for {0}. The updated price is {1}'.format(abs(price_difference), update_price_str))
# elif price_difference > 0:
#     print('The price of the item has been INCREASED! Price increased for {0}. The updated price is {1}'.format(abs(price_difference), update_price_str))

#print("Item price: {0}, Desire price: {1}".format(price_description, PRICE_from_args_modified))

desire_description = "Item price: {0}, Desire price: {1}".format(price_description, PRICE_from_args_modified)
_desire_description = "Item price: xxx, Desire price: xxx."
print(desire_description)

_list = [
    "Current price of the item is higher than your desire price. It's a wait!",
    "Current price is lower than or matching your desire price. It's a buy!"
]


email_text_0 =  """\

%s
%s
%s
%s
%s
%s

"""%(product, price, shipping, _return, desire_description, _list[0])

email_text_1 =  """\

%s
%s
%s
%s
%s
%s

"""%(product, price, shipping, _return, desire_description, _list[1])


# print("Item price: {0}, Desire price: {1}".format(current_price_str, PRICE_from_args_modified))

#comparing section
if current_price_num >= float(PRICE_from_args):
    #TODO: send notification to email/sms with current price of the item is higher than your desire price
    #send(email_text_0)
    #send()
    trigger(send, email_text_0, INPUT_time)
    print("Current price of the item is higher than your desire price. It's a wait!")
    # pass
elif current_price_num <= float(PRICE_from_args):
    #TODO: send notification to email/sms with price is lower than or matching your desire price
    trigger(send, email_text_1, INPUT_time)
    # pass
    #send(email_text_1)
    #send()
    print("Current price is lower than or matching your desire price. It's a buy!")
    
