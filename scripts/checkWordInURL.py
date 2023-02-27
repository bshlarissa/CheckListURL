from bs4 import BeautifulSoup

from scripts.webDriver import SeleniumWebDriver

import pandas as pd


class CheckWordInURL:
    def __init__(self,word_list:list,url:str) -> None:
        self.driver=SeleniumWebDriver(isHeadlessOn=True)._driver()

        self.word_list=word_list
        self.url=url
        self.list_words_in_url=[]
        self.list_url=[]


    def __is_word_in_url(self,soup,word:str) -> bool:
        matched_tags = soup.find_all(lambda tag: len(tag.find_all()) == 0 and word in tag.text.lower())

        for matched_tag in matched_tags:        
            if matched_tag != "":
                return True
            else:
                return False
            
    def _get_words_in_url(self) -> pd.DataFrame:
        self.driver.get(self.url)

        #with BeautifulSoup
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        for word in self.word_list: 
            if self.__is_word_in_url(soup,word):
                self.list_words_in_url.append(word)
                self.list_url.append(self.url)

        return pd.DataFrame(data={
            "palavras_chave":self.list_words_in_url,
            "url":self.list_url
            })