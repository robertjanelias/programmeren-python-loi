select b.Besteldatum, k.Achternaam as Klantnaam, count(br.Aantal) as Aantal_artikelen, sum(br.Aantal * a.Prijs) as Totaalbedrag
from Bestellingen b
join Bestelregels br on b.Bestelnr = br.Bestelnr
join Klanten k on b.Klantnr = k.Klantnr
join Artikelen a on br.Artikelnr = a.Artikelnr
where strftime('%Y', b.Besteldatum) = '2014'
group by b.Besteldatum, k.Klantnr