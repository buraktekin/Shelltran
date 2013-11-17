Shelltran
=========
A python script to translate words from English to Turkish and vice versa.

## How it works?
The script takes the input -a word- from command-line as a parameter, and generates a HTML-request to "tureng.com". Tureng
generates results by using the word that user is requested and generates a result page in html-format. Shelltran reaches the
source of this html formatted page and filters it according to specified tags which search results exist.

## Filtering
- *import lxml.html*
- *result = html.xpath('//a[@data-ajax="false"]')*

The lines you see above, are the codes for filtering results in between hundreds of lines.
* //a - refers to 'a' tag in HTML and,
* [@something=something] - refers to a feature of html-object. Actually you do not have to write this part.
This is for shrinking the field that we are working on.

For instance; in example we have 'data-ajax="false"' property. However, you can use "id" or "class" properties if you want. 
a[@class="example"]  -  it means that you can reach datas which are surrounded by the structure like below.
* <a class="example"... - HTML-side

## Installation
* Download files to your computer,
* Open Terminal and type the commands below,
* $ cd Path/to/folder/
* $ chmod +x install.sh
* $ ./install.sh
