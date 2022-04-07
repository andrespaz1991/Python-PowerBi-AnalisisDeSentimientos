#python -m pip install pandas #Instalación en consola de python
#python -m pip install matplotlib #Instalación en consola de python
#python -m pip install sentiment-analysis-spanish #Instalación en consola de python
#python -m pip install keras tensorflow #Instalación en consola de python
#python -m  pip install sklearn #Instalación en consola de python


############## Podemos probar en la consola la libreria
#from sentiment_analysis_spanish import sentiment_analysis
#sentiment = sentiment_analysis.SentimentAnalysisSpanish()
#print(sentiment.sentiment("me gusta la tómbola es genial"))
#print(sentiment.sentiment("me parece terrible esto que me estás diciendo"))

############## El siguiente código debe ir en la consola de python dentro de power bi en la sección de transformación, para más detalle usa la guía que se encuentra dentro del proyecto 

# 'dataset' contiene los datos de entrada para este script
nombre_columna_analizar="Comentarios" 
nombre_nueva_columna="sentimiento" 
########################################
from sentiment_analysis_spanish import sentiment_analysis
sentiment = sentiment_analysis.SentimentAnalysisSpanish() 
import pandas as pd 
coeficiente_sentimiento=list() 
for i in dataset[nombre_columna_analizar].index:   
    #valordecimal = decimal.Decimal(sentiment.sentiment(dataset[nombre_columna_analizar][i])) 
    texto_sentimiento= sentiment.sentiment(dataset[nombre_columna_analizar][i])
    valordecimal =f'{texto_sentimiento:.2f}'
    coeficiente_sentimiento.append(valordecimal)
dataset[nombre_nueva_columna] = pd.DataFrame(coeficiente_sentimiento,columns=[nombre_nueva_columna],dtype ='string') 
print(dataset)


