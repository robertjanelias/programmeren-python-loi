#
# driehoek & bereken omtrek
#


class Veelhoek:
    def __init__(self, n):
        self.aantal_zijden = n
        
    def __str__(self):
        return f'{self.aantal_zijden} zijden'        
     
class Driehoek(Veelhoek):
    def __init__(self, sides):
        super().__init__(len(sides))
        self.sides = sides
    
    def bereken_omtrek(self):
        return sum(self.sides)
        
        
dh = Driehoek([3,4,5])
print(dh)
print('omtrek', dh.bereken_omtrek())


#
# rechthoek
#

class Rechthoek(Veelhoek):
    def __init__(self, l, b):
        super().__init__(4)
        self.lengte = l
        self.breedte = b
        
    def __str__(self):
        return f'lengte is {self.lengte}, breedte is {self.breedte}'
    
    def bereken_omtrek(self):
        return 2 * self.lengte + 2 * self.breedte;
    
    def bereken_oppervlakte(self):
        return self.lengte * self.breedte
    
rh = Rechthoek(100, 200)
print(rh)
print('omtrek', rh.bereken_omtrek())
print('oppervlakte', rh.bereken_oppervlakte())

#
# vierkant
#

class Vierkant(Rechthoek):
    def __init__(self, zijde):
        super().__init__(zijde, zijde)

        
vk = Vierkant(64)
print(vk)
print('omtrek', vk.bereken_omtrek())
print('oppervlakte', vk.bereken_oppervlakte())


#
# webwinkel
#

quit()		# REMOVE TO RUN!!!!

import sqlite3

conn = sqlite3.connect("Webwinkel.db")
cur = conn.cursor()

cur.execute(
    '''
select b.Besteldatum, k.Achternaam as Klantnaam, count(br.Aantal) as Aantal_artikelen, sum(br.Aantal * a.Prijs) as Totaalbedrag
from Bestellingen b
join Bestelregels br on b.Bestelnr = br.Bestelnr
join Klanten k on b.Klantnr = k.Klantnr
join Artikelen a on br.Artikelnr = a.Artikelnr
where strftime('%Y', b.Besteldatum) = '2014'
group by b.Besteldatum, k.Klantnr
    '''
)
rows = cur.fetchall()

print('{0:25} {1:25} {2:<10} {3:>10}'.format('Besteldatum', 'Klantnaam', 'Aantal art.', 'Totaalbedrag'))
for r in rows:
    print('{0:25} {1:25} {2:<10} {3:>10.2f}'.format(r[0], r[1], r[2], r[3]))
print('\n')

conn.close()

