import numpy as np # Tratamiento de datos
import matplotlib.pyplot as plt # Graficos
import seaborn as sns # Graficos
plt.style.use('ggplot')

def Graficas_frecuencia(df):
    rows = int(np.ceil(df.shape[1] / 3))
    height = rows * 3.5
    fig = plt.figure(figsize=(12, height))
    for n, i in enumerate(df.columns):
        if df[i].dtype in ('object', 'int64') :
            fig.add_subplot(rows, 3, n+1)
            ax = sns.countplot(x=i, data=df)
            plt.title(i)
            plt.xlabel('')
            for p in ax.patches:
                height = p.get_height()
                ax.text(p.get_x()+p.get_width()/2., height + .5,'{:1.2f}'.format(height/len(df[i])), ha="center")
        if df[i].dtype == 'float64':
            fig.add_subplot(rows, 3, n+1)
            ax = sns.distplot(df[i])
            plt.title(i)
            plt.xlabel('')    
    plt.tight_layout()
    return 0