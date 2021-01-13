# SupremeBot
Use Python scripts to checkout Supreme merchandise as soon as it drops. 

**Author: Christopher Chen**

#### 1. Configuration Instructions

Download ChromeDriver from https://chromedriver.chromium.org/downloads and set it in your PATH.

You do this on Mac by opening Terminal and running, sudo nano /etc/paths, it'll prompt you for your password because you are using the sudo command,
then you're essentially accessing the files in your /usr/local/bin folder, thus enabling you to type in the filepath of the ChromeDriver you just downloaded.
I suppose it'll be in your downloads, so you'll type something like, /Users/your_user_name/Downloads/chromedriver

Since I'm using Chrome 86 on my browser, I also use ChromeDriver 86.0.4240.22.

Using whatever version ChromeDriver associated with your Chrome version should be fine, as I doubt much of the utility will be depreciated.

#### 2. Installation Instructions

beautifulsoup4==4.9.3
bs4==0.0.1
certifi==2020.12.5
chardet==4.0.0
idna==2.10
lxml==4.6.2
regex==2020.11.13
requests==2.25.1
selenium==3.141.0
soupsieve==2.1
urllib3==1.26.2

#### 3. Operating Intructions

Change directory in the SupremeBot folder, then run, python3 main.py, from terminal.

#### 4. Known Bugs

**a) Infinite Loop**

If the product does not drop, you will be stuck in an infinite loop (but it's easy to end with 
a keyboard interrupt), so make sure your cook groups are high quality!

**NOTE:** This updated version has only been tested on products that are already present on the site,
so even though I believe it should work (wait for the product to drop before continuing the rest of the script),
the error which may arise is that it will try to execute the rest of the script before the product drops. I used a 
'has-a' relationship in the design of the code, so that may need to be changed into something more dependent. 

**b) Site Change - NoSuchElementException**

Rather than a current bug, this is a bug that **will** occur if the site change's their HTML code. It'll force you 
to update a lot of the bot's source code related to autofill and clicks. 

Since this script is meant to bypass some of Supreme New York's Bot Protection, you can expect that, without sufficient upkeep,
the effectiveness of the program will degrade over time. As I don't plan on continuing development of this project, contact me if 
you want more information, to collaborate, or want to improve it. 

#### 5. Future Improvements...

**a) Product Name Matching**

Using Regular Expressions to take inputted words and match it to the parsed HTML is likely the path that should be taken for as fast 
as possible Name Matching. However, one issue which will likely come up is only returning the product that has the most matches of 
regexes. By this I mean, if one product is named, "Snakeskin Jacket" but another product is named "Snakeskin Pants", then the program
must be able to return the product with the *most* matches, not the first match.

**b) Loading the Driver Directly to the Checkout Page***

If this feature is made, it will seriously improve the time it takes for a full checkout. The issue currently is that unless the 
driver/session has an item added to cart, you are unable to access the Checkout Page. The solution I can think of that may bypass this 
antibot would need to be done in steps:

**NOTE:** The time for this process is not counted in the total time of a product checkout, so be aware this should be done before the 
new merchandise drops.

*I.* On the first get method of the driver, navigate to the view/edit cart page then store this cookie.

*II.* Next, navigate the driver to a random product url (probably through another get method) and add this product to cart.

*III.* Now you'd click the Checkout Now button and autofill your information so that as soon as the product drops, you'll be able 
to click Process Payment.

*IV.* Take that first cookie you stored and pass it your Requests Session.

*V.* Follow the same process as in my code until you get to the point where you are adding the ATCCookie to the driver.

*VI.* Now, instead of adding that cookie to the driver, first you have to clear the cookies on the driver, then add the ATCCookie (because
it contains all the information from starting at the view/edit cart page all the way to the Add to Cart of the item that just dropped).

*VII.* Then, either you'll be able to click Process Payment and purchase the item within 2-3 seconds of it dropping, or you'll have to reload the page costing you another second, and if once you reload the page your information is deleted then you'll have to autofill it again, costing you another 2 seconds. 

The point of this improvement is to avoid reloading pages during cook time **as much as possible.**

**c) CAPTCHA**

This is a hefty, hefty task to tackle. It's far too much for me to explain, but this link might help you understand just how in depth Google's ReCAPTCHA canvases your browser fingerprint: https://www.blackhat.com/docs/asia-16/materials/asia-16-Sivakorn-Im-Not-a-Human-Breaking-the-Google-reCAPTCHA-wp.pdf

**d) Load Time**

Supreme automatically throttles my connection to their checkout page. I've ran dozens of tests and noticed that no matter how fast my program was in passing cookies and refreshing view/edit cart pages, it would always take about 3 seconds to load into the Checkout Page. This was added sometime between 8/20-12/20, because it was previously not an issue. I can only assume their antibot techniques will improve, but I haven't been able to speed the load time into the Checkout Page since this feature was added.
