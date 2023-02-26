import os 
import pandas as pd 

from scripts.checkWordInURL import CheckWordInURL

class GetDataCheckList:

    def __init__(self) -> None:
        self.folder_project=os.getcwd()
        self.planilha=self.__get_dados_parametros()
        self.word_list=self.__get_list_word_from_parametros()
        self.url_list=self.__get_list_url_from_parametros()


    def __get_dados_parametros(self) -> pd.DataFrame:
        planilha=pd.read_excel(f"{self.folder_project}/planilhas/parametros.xlsx")
        return planilha


    def _find_word_in_url(self,url:str):
        result=CheckWordInURL(word_list=self.word_list,url=url)._get_word_in_url()


    def __get_list_word_from_parametros(self) -> list:
        return self.planilha['palavras_chave'].to_list()
    

    def __get_list_url_from_parametros(self) -> list:
        self.planilha['urls'].to_list()

planilha=GetDataCheckList()._find_word_in_url(url="https://www.ofertaesperta.com/")