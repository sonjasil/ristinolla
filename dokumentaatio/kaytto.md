# Käyttöohje

## Käynnistysohje

Asenna ensin sovelluksen riippuvuudet komennolla:

```bash
poetry install
```

Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```

## Käyttöohje
Peli on perinteinen ristinolla 20x20-ruudukolla. Viiden rivi vaaka-, pysty- tai vinosuuntaan voittaa. Pelaaja pelaa merkillä X.

Sovellus pyytää pelaajan syöttämään rivin ja sarakkeen erikseen. Molempien tulee olla numero välillä 1-20. Jos syöte on vääränlainen, pyydetään se uudestaan. Jos syötetty kohta ei ole tyhjä, vuoro jää välistä.