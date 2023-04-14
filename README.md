# Lintubongaussovellus

Lintubongaussovellus on sivusto, johon käyttäjät voivat rekisteröityä ja lisätä lintubongauksiaan. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä. 

DONE:
- Sivua ja muiden lisäämiä bongauksia voi tarkastella kirjautumatta sisään.
- Käyttäjä voi rekisteröityä / kirjautua sisään tililleen.
- Kirjautunut käyttäjä voi lisätä bongauksia.

TO DO:
- Peruskäyttäjä voi muokata ja poistaa aiempia bongauksiaan.
- Ylläpitäjä voi muokata ja poistaa kaikkien lisäämiä bongauksia, sekä ylentää peruskäyttäjiä ylläpitäjiksi.
- Bongauksia voi suodattaa ja järjestää ajan, paikan ja lajin perusteella.
- Sivulta voi selvittää yleisimmin bongatut lajit ja ahkerimman lintubongarin.

# Sovelluksen testaaminen paikallisesti

1. Kloonaa repositorio koneellesi.
2. Luo juurikansioon .env -tiedosto seuraavalla sisällöllä:
  ```bash
  DATABASE_URL=<tietokannan-paikallinen-osoite>
  SECRET_KEY=<salainen-avain>
  ``` 
3. Käynnistä virtuaaliympäristö ja asenna tarvittavat kirjastot ajamalla seuraavat komennot:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r ./requirements.txt
  ``` 
4. Määritä tietokannan skeema komennolla:
  ```bash
  psql < schema.sql
  ```
5. Käynnistä sovellus komennolla:
  ```bash
  flask run
  ``` 
