# Lintubongaussovellus

Lintubongaussovellus on sivusto, johon käyttäjät voivat rekisteröityä ja lisätä lintubongauksiaan. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä. 

DONE:
- Sivua ja muiden lisäämiä bongauksia voi tarkastella kirjautumatta sisään.
- Käyttäjä voi rekisteröityä / kirjautua sisään tililleen.
- Kirjautunut käyttäjä voi lisätä bongauksia.
- Bongaukset voi järjestää ajan, paikan ja lajin perusteella.
- Etusivulta näkee yleisimmin bongatun lajin ja ahkerimman lintubongarin.
- Ylläpitäjät voivat ylentää peruskäyttäjiä ylläpitäjiksi.
- Peruskäyttäjä voi poistaa bongauksiaan profiilissaan.
- Ylläpitäjä voi poistaa kaikkien bongauksia (profiili -> hallitse käyttäjätunnuksia).

LOPPUPALAUTUKSEEN:
- Sivujen ulkoasu -> ulkonäkö, selkeys, lisää tekstiä.
- Lisää tietokantoja -> uusia tietokantoja ja niiden järkevä hyödyntäminen, nykyisten tietokantojen parantelu.

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
