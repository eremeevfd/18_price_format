# Price Formatter

Thank you for using my script for formatting prices! 

# Description

Script gets a price as input and formats it beautifully, adding spaces between thousands and showing 
2 digits after dot if they exist:
<pre>
3213123
3 213 123
---------
2313123.123123
2 313 123.12
</pre>
If script can't handle input data it returns None:
<pre>
asdasd
None
</pre>

# Installation

You can use it standalone:
* Download entire project or just __format_price.py__
* In terminal go: <code>$ python3 format_price.py </code>

Or you can import _format_price_ function to your project.

# Tests

Project includes unit-testing. Checks common inputs and outputs. 
You can run it with typing in terminal:
<pre>
/18_price_format $ python3 tests.py
</pre>

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
