from bs4 import BeautifulSoup
import requests
import time


def locate(category, name):
    '''
    Purpose: Find the product as soon as it drops and return the url_suffix (the part that
    come after 'https://www.supremenewyork.com').

    Very simple function that just takes the category of the product and name of it.
    I used Requests to send a get request to the Supreme Shop and I use the category
    to get to a page where there are a lot less items to parse. Then I use BeautifulSoup
    to parse through all the 'a' tags in the get request's response text, from there
    matching name of the product directly to the string of the 'a' tag (imagine something
    like: <a id='outbound-link' href='google.com'>click here to leave</a>, so here the 'a' tag
    has 'click here to leave' as the string, and 'google.com' as the href. So the locate function
    uses the 'click here to leave' strings on the Supreme site to find a match to the argument I
    passed called name, and once it does, it returns the VALUE of the href attribute in the 'a' tag,
    meaning it would return 'google.com', except in the Supreme Site, the href attribute has the
    product url as the href.


    I don't bother using conditionals because if the product isn't found, then an error will rise
    anyways, so it just seemed easier to catch and handle the error directly.
    '''

    resp = requests.get(f'https://www.supremenewyork.com/shop/all/{category}')
    soup = BeautifulSoup(resp.text, 'lxml')

    while True:
        try:
            link = soup.find('a', string=name)['href']
            return link

        except TypeError:
            print('Target not dropped yet...')
            time.sleep(1)
            continue
