note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

#4)a)
def som(notes) :
  somme = []
  for i in notes :
    if i[0] == "eleve1" :
      somme.append(i[2])
  return sum(somme)/len(somme)

som(notes)

#4)b)
def som2(notes) :
  somme = []
  for i in notes :
    if i[0] == "eleve1" and i[1] == "math" :
      somme.append(i[2])
  return sum(somme)/len(somme)

#4)c)
def moyenne_tuple(notes, eleve, matiere) :
  somme = []
  for i in notes :
    if i[0] == eleve and i[1] == matiere :
      somme.append(i[2])
  return sum(somme)/len(somme)



print(som(notes))
print(som2(notes))
print(moyenne_tuple(notes, "eleve2", "math"))

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)




#5)

onotes = [(Note(note[0], note[1], note[2])) for note in notes]
onote = onotes[1]
print(onote)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

#6)class Note:
class Note:
  def __init__(self, eleve, matiere, valeur):
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
    self.afficher = ('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onotes = [(Note(note[0], note[1], note[2])) for note in notes]
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
print(onote.afficher)

#7)
notes_enregistrées =

#8)
def moyenne_Notes(liste)