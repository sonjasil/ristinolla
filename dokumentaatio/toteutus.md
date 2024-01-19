# Toteutusdokumentti

## Ohjelman rakenne
Ohjelma on perinteinen ristinolla, joka toimii tekstikäyttöliittymällä komentorivin kautta. Tietokone, jota vastaan pelataan, etsii itselleen parhaan siirron alpha-beta-karsinnalla varustetun minimax-algoritmin avulla. Pelilaudan luonti ja tulostus tapahtuu luokan Ruudukko avulla. Kaikki muu pelin toiminnallisuus on luokassa Peli.

## Puutteet ja parannusehdotukset
Ohjelman olisi voinut jakaa paremmin eri luokkiin ja tiedostoihin, nyt suurin osa ohjelmasta on samassa luokassa yhdessä tiedostossa. En saanut heuristiikkafunktiota toimimaan, tämänhetkinen heuristiikka toimii virheellisesti (tarkastelee vääränlaista aluetta pelilaudalla).

## Laajojen kielimallien käyttö
Käytin ChatGPT:tä luomaan pohjan 3x3-ristinollalle ja 20x20-heuristiikkafunktiolle. Koska 3x3 eroaa 20x20-ristinollasta jonkin verran ja luotu heuristiikkafunktio ei ollut toimiva, en lopulta käyttänyt kumpaakaan työssä.

