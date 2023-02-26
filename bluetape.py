import os 
import pandas as pd 

from scripts.webDriver import SeleniumWebDriver

class GetDataCheckList:

    def __init__(self) -> None:
        self.folder_project=os.getcwd()

    def _get_dados_parametros(self) -> pd.DataFrame:
        planilha=pd.read_excel(f"{self.folder_project}/planilhas/parametros.xlsx")
        return planilha

    def _find_word_in_url(self,url:str):
        pass
        

planilha=GetDataCheckList()._get_dados_parametros()
print(planilha)


