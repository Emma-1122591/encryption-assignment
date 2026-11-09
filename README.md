# Encryption-assignment
Opdracht voor Security & Cyberwarfare

## Opzet project
Dit project is een Flask app met één index.html pagina als gebruikersinterface.

### App.py
In app.py draait de Flask app met een route voor '/' en een render_template voor 'index.html'.

### Templates/index.html
De index.html pagina die wordt ingeladen.

### Static/copy_clipboard.js
Heeft een functie om de 'encrypted_text' te kopieëren naar het clipboard.

### Static/styles.css
Hier staat alle styling in voor de elementen in de index.html

### Utils/key_generator
Heeft een functie om een (Fernet) key aan te maken en slaat deze vervolgens op in een secret.key bestand met beperkte toegang. Genereert een key op het moment dat het bestand wordt uitgevoerd. 

### Utils/Key_loader
Heeft een functie die het bestand secret.key kan openen en de (Fernet) key kan 'lezen'/ophalen.

### .gitignore
Zorgt ervoor dat de secret.key niet wordt meegegeven met de Pull Requests naar GitHub.

## Werking project
### Om het project te gebruiken in een eigen IDE:
Stap 1: Clone de repository naar je eigen IDE.
Stap 2: Maak een virtual environment aan.
Stap 3: Installeer cryptography (van Python) en Flask (e.g. pip install cryptography en pip install flask)
Stap 4: Change directories naar de utils (e.g. cd utils)
Stap 5: Maak een Fernet key aan (e.g. python key_generator.py)
Stap 6: Change directories naar encryption-assignment (e.g. cd encryption-assignment)
Stap 7: Activeer de Flask app (e.g. python app.py)

### Het project gebruiken via de gebruikersinterface
Als je het project hebt opgestart met app.py kan je naar de gegeven URL navigeren.
(Waarschijnlijk: http://127.0.0.1:5000/)

- Je kan in de enctyptie textarea een tekst schrijven en deze vervolgens versleutelen.
- Het resultaat hiervan wordt onderaan het scherm weergegeven met een knop om de tekst te kopieëren voor gemak. 
- Mocht je een versleuteld bericht (die je via deze site hebt versleuteld) willen ontsleutelen, kan je deze in de decryptie textarea typen/plakken en vervolgens ontsleutelen.
- Ook hier wordt het resultaat onderaan het scherm weergegeven. 
- Mocht er een ongeldige token (versleuteld bericht) worden ingevoerd bij de decryptie, dan komt er een foutmelding onder te staan.

## Encryptiemethoden
Voor dit project heb ik gebruik gemaakt van de Cryptography - Fernet methode. 
Deze staat aangeraden voor mensen die nog nieuw zijn in de cryptografie en heeft handige standaarden en functies om te gebruiken.

Cryptography.Fernet instellingen:
- Algoritme: AES-128
- Mode: CBC
- Padding: PKCS7
- Authentication: HMAC - SHA256
- Encryption: "base64url"
(Cryptography, z.d.)

## Sleutelbeheer (symmetrisch)
Omdat deze applicatie draait om symmetrische encryptie wordt er dus 1 sleutel gebruikt om een tekst te versleutelen en een token te ontsleutelen. 
Deze key staat in een secret.key bestand waar alleen de 'owner' de rechten heeft met de chmod 0o600 (CHMOD Command Calculator, z.d.).
De sleutel wordt alleen aangemaakt als de functie wordt aangeroepen in de terminal.

## Reflectie


## Bronnen
- Cryptography. (z.d.). Fernet - symmetric encryption. Cryptography.io. 
    https://cryptography.io/en/latest/fernet/#cryptography.fernet.Fernet

- @kr, @tmaher (Tom Maher), @kennyp (Kenny Parnell), @chendave (Dave (Wei) Chen). 
(last updated: 2021, 9 december). Fernet Spec (spec.md). Github.com.
    https://github.com/fernet/spec/blob/master/Spec.md

- W3schools. (z.d.). How TO - Copy Test to Clipboard. W3schools.
    https://www.w3schools.com/howto/howto_js_copy_clipboard.asp

- CHMOD Command Calculator. (z.d.). CHMOD Calculator.
    https://chmodcommand.com/chmod-0600/