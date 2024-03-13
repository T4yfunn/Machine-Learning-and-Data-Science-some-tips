# -*- coding: utf-8 -*-
"""
filling the missing datas with mean values

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer

datas = pd.read_csv("the_data_set_name.csv")


imputer = SimpleImputer(missing_values = np.nan , strategy = "mean")

columns = datas.iloc("first raw" : "last raw" , "first column" :"last column" ).values "colums for numeric values btw"

imputer = imputer.fit(columns["first raw" : "last raw" , "first column" :"last column" ])

column["first raw" : "last raw" , "first column" :"last column" ] = imputer.transform(column["first raw" : "last raw" , "first column" :"last column" ])
