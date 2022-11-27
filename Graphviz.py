#En-tête
import  graphviz

#Définition de quelques caractéristiques du graphique, on a notamment le format de fichier (png supportera des itérations sans changement de nom, ça écrasera juste le fichier, en pdf il faudra changer de nom à chaque itération)
#on a aussi le nom et le type de moteur de rendu, des informations sur ce dernier sont dispo dans la documentation du thread (https://graphviz.org/)
g = graphviz.Digraph(format='png', filename='V3', engine='dot') #File informations
#Même chose ici, on a des attributs du graph et des liens (edges)
g.attr('graph',splines='polyline',constraint='false',labelfontsize='90',outputorder='nodesfirst',mode='KK',labeljust='r',shape='rect', margin='0,0,0,0')
g.attr('edge', decorate='false',remincross='true',labelfontsize='90', len='8', arrowsize='0.5', labelfloat='false', minlen='2.5')

g.attr('node', shape='box',weight='50') #Node attribute

#à partir de là on va pouvoir copier les données issues de Excel 


#Ce bout de code est en exemple, il peut être supprimé
g.edge('Node 2','Node 1',label='Caractéristique',color='Red',dir='forward',arrowhead='dot')
g.edge('Node 3','Node 2',label='Lien',dir='both',arrowhead='dot')
g.edge('Node 3','Node 1',label='Permet',color='Green',dir='forward',arrowhead='dot')





#Enfin on a la dernière ligne du code, à ne pas supprimer 
g.view() 
