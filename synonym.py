
import urllib.request, ssl, os, sys
from bs4 import BeautifulSoup

headers = {'User-Agent': 'URL-PYTHON-EXAMPLE'}

# do not verify the HTTPS certificate
ssl._create_default_https_context = ssl._create_unverified_context

debugFlag = False  # setting to True will cause 

# TODO: Debug/finish Thesaurus class
#class Thesaurus:
#    def __init__(self):

#        self._thes = {}  # Dictionary for holding offline thesaurus entries.

#        try:
#            self.f = open("OfflineThesaurus.txt", "r")  # try to open my offline thesaurus in current dir
#            # Parse thesaurus file into a dict. Each line in file contains word then synonyms separated by spaces.
#            self._thes = {key:value for (line[0], list(line[1:])) in self.f}
#        except FileNotFoundError:
#            self.f = open("OfflineThesaurus.txt", "w")  # create thesaurus file if it doesn't exist

#    def getSynonyms(self, word):
#        if self._thes:  # if thesaurus not empty
#            try:
#                return _thes[key]
#            except KeyError:
#                return None
#        else: return None  # don't waste resources searching through thesaurus if it's empty

#    def setSynonyms(self, word, *synonyms):
#        self._thes[word] = synonyms

#    def saveToFile(self):
#        #  TODO: Seek through file and update lines using fileinput.
#        for word, synonyms in _thes:
#            synonyms = " ".join(synonyms)
#            self.f.write(f'{k} {synonyms}\n')
#        f.close()


def getSynonym(argsList):
    for word in argsList:
        try:
            if debugFlag:
                f = open('testWord2.txt', 'r', encoding="utf-8")
                content = f.read()
            else:
                url = f'https://www.thesaurus.com/browse/{word}'
                req = urllib.request.Request(url, headers=headers)
                f = urllib.request.urlopen(req)
                content = str(f.read())
            page = BeautifulSoup(content, "html.parser")
            wordGridList = page.find_all(attrs={"data-testid": "word-grid-container"})

            wordLinkList = wordGridList[0].find_all('a')
            wordList = [wordLink.contents[0] for wordLink in wordLinkList]
            print(word + ":\n" + ", ".join(wordList))
        except urllib.error.HTTPError:
            print(f'No synonyms could be found for {word}.')
        except Exception as e: print(e)
        if len(argsList) > 1:
            print("\n")


#myThes = Thesaurus()
getSynonym(sys.argv[1:])