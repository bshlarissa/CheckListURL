from bs4 import BeautifulSoup

from scripts.webDriver import SeleniumWebDriver


class CheckWordInURL:
    def __init__(self,word_list:list,url:str) -> None:
        self.driver=SeleniumWebDriver(isHeadlessOn=True)._driver()

        self.word_list=word_list
        self.url=url
        self.list_words_in_url=[]


    def __is_word_in_url(self,soup,word:str) -> bool:
        matched_tags = soup.find_all(lambda tag: len(tag.find_all()) == 0 and word in tag.text)

        for matched_tag in matched_tags:        
            if matched_tag != "":
                return True
            else:
                return False
            
    def _get_word_in_url(self) -> list:
        self.driver.get(self.url)

        #with BeautifulSoup
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        for word in self.word_list: 
            string = word.capitalize()
            if self.__is_word_in_url(soup,string):
                print(f"{string} encontrado")
