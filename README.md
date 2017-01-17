# Price Formatter

Thank you for using my script for formatting prices! 

# Description

Script gets a price as input and formats it beautifully, adding spaces between thousands and showing 
2 digits after dot if they exist:
<pre>
$ python3 format_price.py 32568734
32 568 734

$ python3 format_price.py 32568734.12
32 568 734.12

$ python3 format_price.py 32568734.12.456
None
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
$ python3 tests.py
</pre>

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
