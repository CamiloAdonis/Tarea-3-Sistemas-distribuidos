import matplotlib.pyplot as plt
import pandas as pd
import os
from wordcloud import WordCloud
import numpy as np


yahoo_path = 'output/yahoo_wordcount/part-r-00000'
llm_path = 'output/llm_wordcount/part-r-00000'


yahoo_data = pd.read_csv(yahoo_path, sep='\t', names=['palabra', 'frecuencia'])
llm_data = pd.read_csv(llm_path, sep='\t', names=['palabra', 'frecuencia'])


yahoo_data = yahoo_data.sort_values('frecuencia', ascending=False)
llm_data = llm_data.sort_values('frecuencia', ascending=False)


top_yahoo = yahoo_data.head(50)
top_llm = llm_data.head(50)

print("=== TOP 10 YAHOO ===")
print(top_yahoo.head(10))
print("\n=== TOP 10 LLM ===")
print(top_llm.head(10))


# GRÁFICO 1: BARRAS VERTICALES (Top 50)

plt.figure(figsize=(20, 10))

#  Yahoo
plt.subplot(1, 2, 1)
plt.bar(top_yahoo['palabra'], top_yahoo['frecuencia'], color='skyblue', alpha=0.7)
plt.title('Top 50 Palabras - Yahoo Answers', fontsize=16, fontweight='bold')
plt.ylabel('Frecuencia', fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)

# LLM
plt.subplot(1, 2, 2)
plt.bar(top_llm['palabra'], top_llm['frecuencia'], color='lightcoral', alpha=0.7)
plt.title('Top 50 Palabras - LLM', fontsize=16, fontweight='bold')
plt.ylabel('Frecuencia', fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('barras_verticales_top50.png', dpi=300, bbox_inches='tight')
plt.show()


# NUBES DE PALABRAS

plt.figure(figsize=(20, 8))

# Yahoo
plt.subplot(1, 2, 1)
wordcloud_yahoo = WordCloud(
    width=800, 
    height=400, 
    background_color='white',
    colormap='Blues',
    max_words=100
).generate_from_frequencies(dict(zip(top_yahoo['palabra'], top_yahoo['frecuencia'])))

plt.imshow(wordcloud_yahoo, interpolation='bilinear')
plt.title('Nube de Palabras - Yahoo Answers', fontsize=16, fontweight='bold')
plt.axis('off')

#  LLM
plt.subplot(1, 2, 2)
wordcloud_llm = WordCloud(
    width=800, 
    height=400, 
    background_color='white',
    colormap='Reds',
    max_words=100
).generate_from_frequencies(dict(zip(top_llm['palabra'], top_llm['frecuencia'])))

plt.imshow(wordcloud_llm, interpolation='bilinear')
plt.title('Nube de Palabras - LLM', fontsize=16, fontweight='bold')
plt.axis('off')

plt.tight_layout()
plt.savefig('nubes_palabras.png', dpi=300, bbox_inches='tight')
plt.show()


#  COMPARACIÓN DIRECTA (Top 20)

plt.figure(figsize=(15, 8))

top_20_yahoo = top_yahoo.head(20)
top_20_llm = top_llm.head(20)

x = np.arange(len(top_20_yahoo))
width = 0.35

plt.bar(x - width/2, top_20_yahoo['frecuencia'], width, label='Yahoo', color='skyblue', alpha=0.7)
plt.bar(x + width/2, top_20_llm['frecuencia'], width, label='LLM', color='lightcoral', alpha=0.7)

plt.xlabel('Palabras')
plt.ylabel('Frecuencia')
plt.title('Comparación Directa - Top 20 Palabras (Yahoo vs LLM)', fontsize=16, fontweight='bold')
plt.xticks(x, top_20_yahoo['palabra'], rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('comparacion_directa.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Gráficos guardados:")
print("   - barras_verticales_top50.png")
print("   - nubes_palabras.png") 
print("   - comparacion_directa.png")