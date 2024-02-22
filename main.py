import pygsheets
import pandas as pd
from tkinter import *

gc = pygsheets.authorize(service_file='Credential.json')

df = pd.DataFrame()

df['Name'] = ['John', 'Steve', 'Sarah', 'Mike']
sh = gc.open('store_data')

wks = sh[0]

wks.set_dataframe(df,(1,1))
