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
(Cryptography, z.d. a)

## Sleutelbeheer (symmetrisch)
Omdat deze applicatie draait om symmetrische encryptie wordt er dus 1 sleutel gebruikt om een tekst te versleutelen en een token te ontsleutelen. 
Deze key staat in een secret.key bestand waar alleen de 'owner' de rechten heeft met de chmod 0o600 (CHMOD Command Calculator, z.d.).
De sleutel wordt alleen aangemaakt als de functie wordt aangeroepen in de terminal.

## Reflectie
### Keuze Python Cryptography Fernet
Ik ben erg blij met mijn keuze voor de python.cryptography.Fernet methode/library.
Ik kon hierdoor namelijk op een makkelijke manier functies maken voor het genereren van een sleutel (en deze opslaan), het gebruiken van de sleutel voor encryptie en het gebruiken van de sleutel voor decryptie. 
De keuze om er een Flask app van te maken ben ik ook erg tevreden over. Hierdoor kon ik op een gemakkelijke manier de variabelen en functies gebruiken in combinatie met de index.html template.

### Keuze sleutelbeheer
De keuze voor het sleutelbeheer vind ik lastig. Ik denk dat het voor zo'n project een prima keuze is geweest om op deze manier de sleutel op te slaan, maar bij veel artikelen en persoonlijke aanbevelingen lees ik dat de andere opties (waar waarschijnlijk beter gebruik van gemaakt kan worden) gaan over het gebruiken van environment variables of een online vault service (zoals AWS secrets manager).
Ik kon alleen niet op een snelle of gemakkelijke manier achterhalen hoe ik precies gebruik moest maken van de environment variables zonder direct de key in een file te moeten schrijven. (En de secret managers kosten vaak geld.) Daarom heb ik ervoor gekozen om toch door te gaan met het idee voor het wegschrijven naar een secret.key bestand. Mocht ik hier ooit nog een keer gebruik van maken lijkt het me een goede volgende stap om gebruik te maken van een andere manier, aangezien het sleutelbeheer (en dus het geheimhouden van de sleutel) als belangrijkste wordt gezien bij de Kerckhoffs principes.

## Onderzoek
Hieronder het onderzoek wat ik vooraf heb gedaan aan het project. Het gaat over symmetrische en asymmetrische enctyptie, Kerckhoffs principles en mijn keuze voor cryptography.Fernet.

### Symmetrisch en Asymmetrisch
Symmetrische encryptie is het gebruiken van één gedeelde geheime sleutel voor de encryptie en decryptie van data/gegevens. Het proces volgt het volgende model: De zender voert een platte tekst en de sleutel door een symmetrisch algoritme om een versleutelde tekst te produceren die onleesbaar is tijdens de verzending of opslag. De ontvanger kan de versleutelde tekst met dezelfde sleutel door het algoritme halen om de oorspronkelijke platte tekst te herstellen. De veiligheid komt neer op het geheimhouden van de sleutel en de sterkte van het algoritme (EC-team, 2026 a).
Bij asymmetrische encryptie worden er verschillende sleutels gebruikt. De data wordt versleuteld met een publieke key van de ontvanger, maar kan alleen ontsleuteld worden met een privé key, ook van de ontvanger. Hierdoor kan de publieke key (voor encryptie) wel gedeeld worden en moet alleen de decryptie key geheim blijven (EC-team, 2026 b). 

### Kerckhoffs Principle
Kerckhoffs principle is een concept in cryptografie. Het gaat dan om de veiligheid van een cryptografiesysteem dat niet moet vertrouwen op het geheimhouden van het algoritme, maar op de geheimhouding van de cryptografische sleutel. Het systeem moet veilig blijven, ook al is het gebruikte algoritme bekend (NordVPN, z.d.). 

### Cryptografische library
Cryptography - Fernet
Ik ga voor het project gebruik maken van een library van Python genaamd cryptography. Binnen deze library is er een module Fernet. Fernet maakt gebruik van het algoritme: AES-128 (Cryptography, z.d. b). 
Alle sleutellengtes van het AES-algoritme werden in 2000 door NIST (National Institute of Standards and Technology) aangekondigd als ‘voldoende’ om geclassificeerde informatie te beschermen. (Proton, z.d.).

## Bronnen
- Cryptography. (z.d. a). Fernet - symmetric encryption. Cryptography.io. 
    https://cryptography.io/en/latest/fernet/#cryptography.fernet.Fernet

- Cryptography. (z.d. b). Welcome to pyca/cryptography. Cryptography.io. 
    https://cryptography.io/en/latest/

- @kr, @tmaher (Tom Maher), @kennyp (Kenny Parnell), @chendave (Dave (Wei) Chen). 
(last updated: 2021, 9 december). Fernet Spec (spec.md). Github.com.
    https://github.com/fernet/spec/blob/master/Spec.md

- W3schools. (z.d.). How TO - Copy Test to Clipboard. W3schools.
    https://www.w3schools.com/howto/howto_js_copy_clipboard.asp

- CHMOD Command Calculator. (z.d.). CHMOD Calculator.
    https://chmodcommand.com/chmod-0600/

- EC-team. (2026, 22 mei a). Wat is symmetrische codering? Encryption Consulting. 
    https://www.encryptionconsulting.com/nl/education-center/what-is-symmetric-encryption/

- EC-team. (2026, 20 juli b). Symmetrische versus assymetrische encryptie: welke is beter? 
    https://www.encryptionconsulting.com/nl/education-center/symmetric-vs-asymmetric-encryption/

- NordVPN. (z.d.). Kerckhoffs’ principle. NordVPN. 
    https://nordvpn.com/nl/cybersecurity/glossary/kerckhoffs-principle/?srsltid=AYCX9vLA5vCh6BYQArIoDxZFqbMyqWDb_Ey2keYdkjALNSlA1fQ29dpe