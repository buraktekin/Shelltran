#   author:	 Burak Tekin
#   Contact: iletisim@buraktekin.net
#   Created: 17 November 2013

#import to be able to use command-line
import urllib2, lxml.html, codecs
import sys
	
''' 
	When we request to get command-line arguments by using python, it returns us
	a list of word; which is made up of words you entered in command-line. In this
	project I just want command-line to return one word even if user enters more.

			> sys.argv[1] - is what we want.

	Yes, I am caling the word that is in index 1, not zero! Because, we are compiling
	python codes in this way;
			> python /PATH/<filename>.py

	So, as you see first element of arguments list is "<filename>.py". We do not want
	it.
'''

# Class of Text Colors

class text_colors:
    title = '\033[92m'
    words = '\033[91m'
    finish_color = '\033[0m'

    def disable(self):
        self.title = ''
        self.words = ''
        self.finish_color = ''

#End of Class


#show error and usage if no word is entered. 
if len(sys.argv) < 2:
	print text_colors.words + \
		"\n***** ERROR *****\n Please enter a word.\n<USAGE: sheltran <a word want to search>\n" \
		+ text_colors.finish_color
	exit()
	
	
# Addressing the word to site where searching will be done.
generate_link_for_word = "http://m.tureng.com/search/{}".format(sys.argv[1])


#if word is made up of two seperated word then reform the string structure.
if len(sys.argv) >= 2:
	for count in range(2,len(sys.argv)):
		generate_link_for_word += "%20" + sys.argv[count] #Search query is reformed here.
	content = urllib2.urlopen(generate_link_for_word).read().decode("utf8",'replace') #The greatest challenge! Encoding problem achieved here when contents are reading.
	

html = lxml.html.fromstring(content)
result = html.xpath('//a[@data-ajax="false"]') #filter results
head = html.xpath('//li[@data-role="list-divider"][position() = 1]') #filter title to display


print "\n***** RESULTS ({} found) *****\n".format(sys.argv[1], len(result))
#print title for description and display some warns.
for title in head:
	if "?" in title.text_content().strip():
		print text_colors.title + title.text_content().strip() + text_colors.finish_color


#print searching results 
for means in result:
	print text_colors.words + str(result.index(means) + 1) + ". " + means.text_content().strip() + text_colors.finish_color
	
	
print "\nSearched in tureng.com\n "
