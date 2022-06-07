from finvizfinance.quote import finvizfinance
from finvizfinance.screener.overview import Overview
import pandas as pd
import hvplot.pandas
from tool.calc import Calculator
import sys

sys.setrecursionlimit(20000)
screener = Calculator()

screener.convert()

