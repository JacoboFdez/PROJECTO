
import sys 
sys.path.append("../")
import src.support as sp 
import pandas as pd 
import numpy as np





def porcentaje_nulos(a):
    return (a.isnull().sum() / a.shape[0] * 100).reset_index()

def borrar_duplicados(a):
    return (a).drop_duplicates()