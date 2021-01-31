"""a) Cosiderând că fiecare persoană are asociată vârsta pe același indice, afișați precum mai jos: 
Mihai are varsta de 14 ani.George are varsta de 23 de ani.... 
b) Adăugați în liste la final, corespunzător, 
datele: Andreea, 34 și Ioan, 23. Afişaţi ambele liste apoi. 
c) Ștergeți datele din ambele liste despre Ana (atenție la indici). 
d) Afișați primele trei elemente din lista prenume. 
e) Afișați lista prenume de la dreapta la stânga. 
f) Afişaţi elementele cu indicii 2 și 4, apoi de la 0 la 5 din ambele liste."""

with open ('liste.txt','r')as f:
    prenume=f.readline()
    varsta=f.readline()
prenume=prenume.split()
varsta=varsta.split()
for i in range (0,len(varsta)):
    varsta[i]=int(varsta[i])
print ('a.)')
for i in range (0,len(prenume)):    
    print(prenume[i],'are varsta de',str(varsta[i]),'ani')
print ('b.)')
prenume.extend(['Andreea' , 'Ioan'])
varsta.extend([34 , 23])
print(prenume)
print(varsta)
print ('c.)')
prenume.pop(2)
varsta.pop(2)
print ('d.)')
print(prenume[0:4])
print ('e.)')
print(prenume[::-1])
print ('f.)')
print(prenume[2],',',prenume[4])
print(prenume[0:5])
print(varsta[0:5])