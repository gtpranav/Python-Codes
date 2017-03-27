import urllib

def read_text():
    quotes = open("F:\quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_curse_words(contents_of_file)

def check_curse_words(open_text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+open_text)
    output = connection.read()
    print(output)
    connection.close()

read_text()
