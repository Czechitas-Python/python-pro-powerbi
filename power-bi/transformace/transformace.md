## Transformace

Uzavřené smlouvy jsou často porovnávány s plánem, aby bylo jasné, zda hodnoty uzavřených kontraktů dosahují požadové úrovně. Tabulka s plánem tržeb je ke stažení [zde](https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/power-bi/assets/sales_plan.csv). Tabulku importujeme do Power BI jako nový zdroj.

Tabulka má data zadaná jako čísla - číslo roku a číslo měsíce. Abychom mohli zobrazit obě hodnoty v jednom grafu, potřebujeme k tabulce s plánem přidat datum. Kliknutím na tlačítko `Transform data` otevřeme nástroj Power Query, kde můžeme provádět různé transformace dat.

Nejprve přidáme sloupec s datem. Klikneme na tlačítko `Custom column`, které nám umožní přidat sloupec s hodnotou spočítanou na základě ostatních funkcí. V počítaných sloupcích můžeme využít balík více než 700 funkcí, které jsou popsány [v dokumentaci](https://docs.microsoft.com/en-us/powerquery-m/power-query-m-function-reference). V našem případě využijeme funkci [#datetime](https://docs.microsoft.com/en-us/powerquery-m/sharpdatetime).

::fig[Notebook]{src=assets/custom_column.png size=60}

Po zavolání funkce bychom měli zkontrolovat typ hodnoty ve sloupci. Pokud není nastaven jako `Date`, provedeme převod pomocí menu `Change Type`.

::fig[Notebook]{src=assets/change_type.png}

Jako poslední krok spojíme obě tabulky dohromady. Nejjednodušší je použití tlačítka `Append Queries`, což je obdoba operace UNION v jazyce SQL nebo funkce `concat()` v modulu `pandas`. 

Nyní můžeme přidat vizualizaci `Lined and Stacked column chart` a porovnat, nakolik se obchodníkům daří plnit obchodní plán.

::fig[Notebook]{src=assets/sales_plan_vs_actual.png size=70}

### Využití Pythonu jako zdroje

Python můžeme využít jako zdroj dat a do Power BI můžeme například přenést již hotové skripty. Zkusme tedy nejprve přenést do Power BI výsledky maturity, se kterými jsme již pracovali. 

Ve skupině `Other` vybereme jako zdroj `Python script`. Budeme opět využívat modul `pandas`. Data načteme pomocí metody `read_csv`, do které vložíme URL jednotlivých datových souborů.

Po stisknutí tlačítka OK se zobrazí dialogové okno, ve kterém vybereme, které datové zdroje chceme využít. Jednotlivé "zdroje" se v terminologii Power BI označují jako `query` (dotazy).

::fig[Notebook]{src=assets/vyber_zdroju.png size=70}

Pokud vybereme všechny, uvidíme v levé části okna každý ze zdrojů jako samostatnou položku v menu, kterou si můžeme zobrazit.

::fig[Notebook]{src=assets/zobrazeni_zdroju.png size=70}

Nyní bychom mohli pomocí nástrojů Power Query mohli provést stejné transformace (propojení zdrojů, filtrování, případně agregace), abychom se dostali k obdobným výsledkům jako v předchozí části. Níže je například vidět dialog na pro spojení jednotlivých datových souborů.

::fig[Notebook]{src=assets/spojeni_dat.png size=90}

Efektivnější ale bude využít již připravený kód v jazyce Python a v Power BI pracovat až s připravenými výsledky. Smažme tedy všechny vytvořené dotazy a přidejme nový skript, ze kterého vybereme pouze dotaz `maturita`.

```
import pandas

u202 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u202.csv")
u203 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u203.csv")
u302 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u302.csv")
u202['mistnost'] = 'u202'
u203['mistnost'] = 'u203'
u302['mistnost'] = 'u302'
maturita = pandas.concat([u202, u203, u302], ignore_index=True)
```

Po vyhodnocení výsledků maturity stačí, abychom tabulky propojili dohromady, 
agregace budou vypočteny automaticky při tvorbě vizualizací. Proto klikneme na tlačítko `Close & Apply`.

*Poznámka:* Pokud bychom se k editaci skriptu chtěli vrátit, klikneme na ikonku ozubeného kola v řádku `Source` v panelu napravo.

::fig[Notebook]{src=assets/editace_skriptu.png}

