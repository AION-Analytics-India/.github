# „AION Sargas“ veikimo ir privatumo schemos

**Schemos yra aiškinamosios.** Jos neįrodo, kad visos galimybės jau veikia vartotojų įrenginiuose.

## 1. Asmeninio naudotojo patikra

~~~mermaid
flowchart TD
 A[Naudotojui kyla įtarimas] --> B{Ką tikrinti?}
 B -->|Galinga prieiga| C[Pritaikymo neįgaliesiems ir administratorių sąrašas]
 B -->|Blokuotas domenas| D[Vietinis DNS atmetimų žurnalas]
 B -->|Galima infekcija| E[Žinomų požymių diagnostika]
 C --> F[Radinių ir apribojimų paaiškinimas]
 D --> F
 E --> F
 F --> G[Naudotojas pasirenka veiksmą Android nustatymuose]
~~~

## 2. Naudotojo ir organizacijos duomenų riba

~~~mermaid
flowchart TB
 subgraph Telefonas[Asmeninis ar darbo telefonas]
 A[Vietiniai išsamūs radiniai] --> B[Juos mato įrenginio naudotojas]
 B --> C[Naudotojo pasirenkami veiksmai]
 end
 subgraph Ateitis[Siūloma ateities funkcija - DAR NEĮDIEGTA]
 D[Minimalūs rizikos duomenys] --> E[Įgaliotas organizacijos vertintojas]
 end
 B -.->|Reikia teisėto pagrindo ir patikrintų kontrolės priemonių| D
 P[Asmeninės žinutės, kontaktai, nuotraukos] -.->|Automatiškai neperduodami| E
~~~

## 3. Diagnostikos interpretavimas

~~~mermaid
flowchart TD
 A[Patikra] --> B{Rezultatas}
 B -->|Rastas požymis| C[Reikia išsiaiškinti; ne galutinė išvada]
 B -->|Požymio nerasta| D[Neįrodo, kad saugu]
 B -->|Duomenų nepakako| E[Nežinoma; nelaikyti saugiu]
 C --> F[Žmogaus atliekama peržiūra]
 D --> F
 E --> F
~~~

[English diagrams](../DIAGRAMS.md) · [Palyginimas](COMPARISON.lt.md). Joks rezultatas nėra garantija, kad įrenginyje nėra šnipinėjimo programų. Šios sistemos institucinis duomenų perdavimo kelias **dar neįdiegtas**.
