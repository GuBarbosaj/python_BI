import pandas as pd

dados = [['João',10],['Maria',15],['Joana',20],['Pedro',25]]
df = pd.DataFrame(dados,columns=['Nome','Idade'],dtype=float)
print (df)