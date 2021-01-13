from buy import Buy

Purchase_Object = Buy('/Users/chris/Downloads/chromedriver 3',
                      'shirts', 'Snakeskin Corduroy Zip Up Shirt')

Purchase_Object.Purchase('https://www.supremenewyork.com/shop/cart', 'Medium')

'''
There is suspect lag between Driver to Checkout Page and the end of Autofill. It always occurs which makes me believe
Supreme is throttling the speed at which you're allowed to START filling out the form. Test it for yourself and you'll see,
or maybe my IP Address has just been banned after all this time...
'''
