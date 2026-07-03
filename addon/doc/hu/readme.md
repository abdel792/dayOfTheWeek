# A hét napja #

* Fejlesztők: Abdel, Noelia.

Ez a kiegészítő lehetővé teszi, hogy megtalálja a kiválasztott dátumnak megfelelő napot a héten.

Egy "A hét napja" nevű almenüt ad hozzá az NVDA Eszközök menüjéhez, amely 2 elemet tartalmaz:

* Az első, "Nap keresése" nevű elem egy 3 vezérlőből álló párbeszédpanelt nyit meg:

    * Egy listamezőt a dátum kiválasztásához vagy beírásához;
    * Egy "OK" gombot a napot tartalmazó üzenetablak megjelenítéséhez;
    * Egy "Mégse" gombot a párbeszédpanel bezárásához.

* A második, "A hét napja kiegészítő beállításai" nevű elem megnyitja a kiegészítő paramétereit, ahol megadhatja, hogy szeretné-e bemondatni a dátummezők címkéit vagy sem. Ez a következő elemekből áll:

    * A dátumválasztó akadálymentesítésének engedélyezése;
    * A címkék bemondási szintje, amelynél 3 lehetőség közül választhat:

        * Hosszú (ez az alapértelmezett választás);
        * Rövid (rövid bemondásokhoz);
        * Kikapcsolva (a címkék bemondásának letiltásához).

    * Csak az aktuális dátummező értékének bemondása függőleges mozgás közben;
    * Egy "OK" gomb a konfiguráció mentéséhez;
    * Egy "Mégse" gomb a megszakításhoz és a párbeszédpanel bezárásához.

## Megjegyzések ##

* Ezeket a párbeszédpaneleket az Escape billentyű megnyomásával is bezárhatja;
* Hozzárendelhet egy billentyűparancsot ezeknek a párbeszédpaneleknek a megnyitásához a "Billentyűkombinációk" menüben, pontosabban "A hét napja" kategóriában;
* Ha az NVDA 2018.2 vagy újabb verzióját használja, csak egy elemet talál az eszközök menüben a nap kereséséhez, a kiegészítő beállításai pedig az NVDA beállítási paneljén lesznek.

## Kompatibilitás ##

* Ez a kiegészítő az NVDA 2019.3 és újabb verzióival kompatibilis.

## Változások a 20240326.0.0 verzióban

* Frissítve a kompatibilitás az nvda-2024.1 verzióhoz.;
* A letöltési link törölve lett a readme fájlból, a jövőbeni frissítések letöltési linkje mostantól csak a kiegészítő-áruházból lesz elérhető.

## Változások a 20231229.0.0 verzióban ##

* Visszafelé kompatibilis implementáció hozzáadása a beszéd igény szerint mód támogatásához, amely hamarosan elérhető lesz az nvda-2024.1 verzióval.

## Változások a 20231015.0.0 verzióban ##

* Javítva egy hiba, amely az NVDA legújabb verzióiban a dátumválasztóból a felfelé nyíllal történő navigáláskor jelentkezett.

## Változások a 20230728.0.0 verzióban ##

* A flake8 és a mypy szabályok alkalmazása a kódon;
* A minimálisan támogatott NVDA verzió módosítva 2019.3-ra a Python 3-ban bevezetett annotációk támogatásához.

## Változások a 20230607.0.0 verzióban ##

* A következő munkafolyamatok hozzáadása:
 * auto-update-translations - a fordítások automatikus frissítéséhez az NVDA fordítási rendszeréből.
 * release-on-tag..yaml: a kiegészítő fordításához és közzétételéhez, amint egy új tag elküldésre kerül;
 * manual-release.yaml: a kiegészítő új verzióinak manuális fordításához és kiadásához.
* Frissített fordítások.

## Változások a 20230508.0.0 és újabb verziókban ##

* • A verziószám, a minimális NVDA verzió és a letöltési link módosítva az áruház konvencióinak/követelményeinek megfelelően.

## Változások a 19.02 verzióban ##

* A verziószámozás módosítása ÉÉ.HH formátumra (Az év 2 számjeggyel, ponttal elválasztva, majd a hónap 2 számjeggyel);
* Kompatibilitás hozzáadása az új kiegészítő-verzióformátummal, amely az nvda 2019.1 verzió óta jelent meg.

## Változások a 6.0 verzióban ##

* A kiegészítő beállításainak hozzáadása az NVDA beállítási paneljéhez az NVDA 2018.2 és újabb verziókhoz;
* A nap keresése elem áthelyezése az eszközök menübe;
* A kiegészítő visszafelé kompatibilitásának hozzáadása a 2018.2-es verzió előtti NVDA verziókkal, amelyek tartalmazták a beállítási panelt.

## Változások a 5.0 verzióban ##

* A kiegészítő kompatibilitásának hozzáadása a wxPython 4.0 és Python3 verziókkal;
* Javítva egy hiba a nem ASCII karaktereket tartalmazó kiegészítő-útvonalakkal kapcsolatban.

## Változások a 4.0 verzióban ##

* A kiegészítő mostantól képes felismerni az összes olyan regionális dátumformátumot, amelyet a felhasználó választhat;
* A kiegészítő visszafelé kompatibilitásának hozzáadása a 2016.4-es verzió előtti NVDA verziókkal, amelyek tartalmazták a gui.guiHelper modult.

## Változások a 3.1 verzióban ##

* Visszatérés a hét napjának előző formátumához, mivel ez nagyobb számú nyelv felismerését teszi lehetővé;
* A dátumválasztó akadálymentesítésének javítása a 'Nap', 'Hónap' és 'Év' mezők, valamint a hozzájuk tartozó értékek felismerésével;
* Technika hozzáadása a grúz nyelv integrálásához a hét napjainak felismeréséhez;
* Konfigurációs párbeszédpanel hozzáadása a dátumválasztó akadálymentesítésének engedélyezéséhez vagy letiltásához;
* A kiegészítő almenüjének áthelyezése az "Eszközök" menüből a "Beállítások" menübe;
* A kiegészítő kategóriájának módosítása "A hét napja" értékre.

## Változások a 2.0 verzióban ##

* A gui.guiHelper modul használata a dátumot kérő párbeszédpanel megfelelő megjelenésének biztosítására;
* A GPL licenc hozzáadása a kiegészítőhöz;
* A hét napjai le lettek fordítva, hogy a kiegészítő megfelelően működjön a különböző nyelveken;
* A nap formátumának módosítása a kódolási hibák elkerülése érdekében.

## Változások a 1.0 verzióban ##

* Kezdeti verzió.
