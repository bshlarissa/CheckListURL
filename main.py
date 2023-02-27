import os 
import pandas as pd 

from scripts.checkWordInURL import CheckWordInURL

import warnings
warnings.filterwarnings("ignore") #Remove Warning desnecessário

class GetDataCheckList:

    def __init__(self) -> None:
        self.folder_project=os.getcwd()
        self.folder_planilhas=f"{self.folder_project}/planilhas"
        self.planilha=self.__get_dados_parametros()
        self.word_list=self.__get_list_word_from_parametros()
        self.url_list=self.__get_list_url_from_parametros()
        
        self.__get_result()


    def __get_dados_parametros(self) -> pd.DataFrame:
        return pd.read_excel(f"{self.folder_planilhas}/parametros.xlsx")


    def __get_result(self):
        result=self.__find_words_in_url()
        print(result)
        result.to_excel(f"{self.folder_planilhas}/result.xlsx",index=False)


    def __find_words_in_url(self) -> pd.DataFrame:
        result = pd.DataFrame()
        for url in self.url_list:
            print(f"\nProcurando palavras na URL: {url}")
            word_result=CheckWordInURL(word_list=self.word_list,url=url)._get_words_in_url()
            result=result.append(word_result)

        return result



    def __get_list_word_from_parametros(self) -> list:
        return self.planilha['palavras_chave'].dropna().to_list()

    

    def __get_list_url_from_parametros(self) -> list:
        return self.planilha['urls'].dropna().to_list()

GetDataCheckList()