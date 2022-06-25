from finvizfinance.quote import finvizfinance
from finvizfinance.screener.overview import Overview
import pandas as pd
import hvplot.pandas

class Calculator:
    def __init__(self):
        
        self.data = self.screener()
        self.new_data = self.create_df()
        self.cov = self.get_df()
        self.get = self.get_all()
        self.base = self.convert()

        

        
#     create new df
    def create_df(self):
        newdf = pd.DataFrame()
        
        return newdf
    
    
    
    def calc(self,sector):
        data = self.data[self.data.Sector == sector]
    
        calc = data[['Market Cap']].sum()[0]
                
            
        # self.new_data.loc[self.new_data["Sector"] == row[1]['Sector']] 
        
        self.new_data[sector]=[calc]
        
        return self.new_data
    
    
    def get_all(self):
        Sectors = ['Technology','Consumer Cyclical','Healthcare','Consumer Cyclical','Financial','Communication Services','Energy','Industrials','Basic Materials','Real Estate','Consumer Defensive','Utilities']
        pd.set_option('display.float_format', lambda x: '%.2f' % x)
        
        for x in Sectors:
            a = self.calc(x)
        return a
            
            
        
    def get_df(self):
        
        Group_Sector_market = self.data[['Sector',]]
        b = Group_Sector_market.drop_duplicates(subset=['Sector'])
        return b
    
    def convert(self):
        Sectors = ['Technology','Consumer Cyclical','Healthcare','Consumer Cyclical','Financial','Communication Services','Energy','Industrials','Basic Materials','Real Estate','Consumer Defensive','Utilities']
        now = pd.Timestamp.now()
        self.cov['MarketCap']= 0
        self.cov['Date']= now
        
        a = self.cov.set_index('Sector')
        for x in Sectors:
            b = a.MarketCap[x]=self.get[x][0]
            a = a.sort_values(by='MarketCap',ascending=False)
          
                
        return a.reset_index()

        
        
        
    
    def screener(self):

        foverview = Overview()
        filters_dict = {'Index':'Any','Sector':'Any'}
        foverview.set_filter(filters_dict=filters_dict)
        df = foverview.screener_view().copy()
        
        return df
    
    
#     def build(self):
#         self.base.reset_index(inplace=True)
#         datetime = self.base.set_index('Date')
#         return datetime
    
    
    def create(self):
      
        for x in  self.base['Sector']:
            df =  self.base[ self.base.Sector == x]
            # .reset_index().drop(columns=['index'])
            df.to_csv(f"DATABASE/{x}.csv",mode="a",index=False,header=False)
        
    
    