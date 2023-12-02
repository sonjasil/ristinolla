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

Sovellus pyytää pelaajan syöttämään rivin ja sarakkeen erikseen. Molempien tulee olla numero välillä 1-20. Tällä hetkellä ohjelmassa on bugi, jonka takia vuoron menettää, jos koordinaatin antaa väärässä muodossa. Tämä on tarkoitus korjata.