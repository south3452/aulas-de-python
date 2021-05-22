'''
Atividade machine-learning, Checkpoint 3 
Nome: Lucas Venancio Coutinho 
'''

from sklearn import tree #                                                                                                                                      ||||                                                                                                                                                       ||||

features = [[54, 64, 199], [90, 94, 178], [69, 123, 119], [78, 109, 138], [99, 88, 121], [93, 113, 179], [92, 49, 132], [63, 96, 127], [57, 79, 149], [96, 60, 107], [107, 164, 93],[117, 163, 83],[126, 153, 125],[119, 193, 188],[106, 160, 130],[113, 169, 66],[122, 197, 23],[115, 178, 168],[114, 155, 68],[100, 198, 47],[136, 313, 345],[211, 285, 376],[250, 339, 325],[287, 230, 264],[158, 258, 295],[129, 255, 352],[181, 366, 294],[137, 202, 246],[241, 307, 244],[212, 218, 222]]
#Uma pessoa normal será representada por 0,  Uma pessoa alterada será representada por 1 e uma pessoa diabética será representada por 2
labels = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
classif = tree.DecisionTreeClassifier() #Classificador
classif.fit(features, labels)
print("*"*60)
print("Programa para fazer um pré-diagnóstico de diabetes")
print("*"*60)
i = 0
while i == 0:
    try:
        jejum = float(input("Digite a sua glicose em jejum: "))
        apos = float(input("Digite a sua glicose após 2h de injerir 75g de glicose: "))
        casual = float(input("Digite sua Glicose Casual: "))
        i = 1
    except:
        print("coloque apenas numeros")
x = classif.predict([[jejum, apos, casual]])
print("-"*40)
if x == 0:
    print("Sua Glicose está Normal")
elif x == 1:
    print("Sua Glicose está Diminuída")
elif x == 2:
    print("Sua Glicose está acima do normal, provavelmete está com diabetes")
print("Lembre-se isto é um pré-diagnóstico, nunca se auto diagnostique sempre procre um médico")
