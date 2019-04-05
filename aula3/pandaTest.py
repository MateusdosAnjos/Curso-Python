import numpy as np
import pandas as pd


def main():
	data = pd.read_csv("googleplaystore.csv") 
	print(list(data.columns.values))
	print(data['App'])
main()	
