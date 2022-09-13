## Čtení na doma

### Bodový graf a korelace

U různých dat nás často zajímá *korelace*. Odborně, řečeno korelace *vyjadřuje lineární vztah mezi dvěma veličinami*. Uvažujme například **cenu dvou akcií** na akciovém trhu. Pokud jsou ze stejném odvětví (např. technologického sektoru), jsou často *korelované*, tj. pokud vzroste cena akcie jedné firmy, vzroste cena akcie i té druhé. Naopak, pokud jedna cena akcie jedné firmy poklesne, poklesne i druhé. Ceny dvou akcií z různých odvětví (např. technologií a potravinářství) takto provázané být nemusí. Technologické firmy jsou totiž více závislé na tom, v jaké kondici je ekonomika. Nákup nového telefonu nebo televize odložit můžeme, pokud máme problém vyjít s penězi, jídlo si ale musíme kupovat pořád.

Uvažujme data v souboru [stock_data.csv](stock_data.csv), ve kterém jsou ceny akcií společností Apple (AAPL), Microsoft (MSFT), Meta (META), Phillip Morris (PM) a Tyson Foods (TSN). V souboru jsou kromě cen v absolutní hodnotě i procentuální změny cen, a to ve sloupcích s koncovkou `_change`. 

Pro dvě ceny akcií si můžeme provázanost zobrazit formou bodového grafu, tj. volíme typ vizualizace `Scatter chart`.

::fig[Notebook]{src=assets/bodovy_graf_nastaveni.png}

U typu agregace musíme nastavit `Don't summarize`, jinak bychom v grafu měli pouze jeden bod.

::fig[Notebook]{src=assets/bodovy_graf_agregace.png}

Výsledný graf vypadá přibližně takto.

::fig[Notebook]{src=assets/bodovy_graf.png}

Pokud bychom chtěli vidět, jak jsou závislé ceny většího množství akcií, bodový graf není úplně praktický, protože bychom potřebovali příliš velké množství grafů (pro *n* akcií potřebujeme *n(n - 1)* grafů), můžeme použít tvz. korelační matici. Do korelační matice vkládáme velikosti korelací, které mohou být v rozsahu - 1 až + 1. Korelace blízko + 1 znamenají, že jsou hodnoty silně provázané a při růstu jedné hodnoty má tendenci růst i druhá. Korelace blízko - 1 znamenají, že hodnoty jsou též vzájemně provázané a při poklesu jedné hodnoty druhá roste. Korelace blízko 0 znamenají, že hodnoty jsou (lineárně) nezávislé.

Hodnoty korelací všech dvojic můžeme zobrazit jako teplotní mapu. Nejprve vytvoříme korelační matici, a to pomocí metody `corr()`. Korelační matice je čtvercová matice, kde řádky i sloupce složí názvy jednotlivých datových řad a hodnoty v matici jsou korelace mezi v popisku řádku a hodnotou v popisku sloupce.

Protože korelační matice je vždy zrcadlová, často se pro přehlednost vykresluje pouze levá dolní polovina. Abychom toho dosáhli, použijeme funkci triu z modulu numpy, která vygeneruje matici, která bude mít hodnoty 0 v levé dolní polovině. Takovou matici označíme jako masku a následně ji využijeme jako parametr `mask`.

```py
import matplotlib.pyplot as plt
import seaborn
import numpy

cmap = seaborn.diverging_palette(230, 20, as_cmap=True)

corr = dataset.corr()
mask = numpy.triu(numpy.ones_like(corr, dtype=bool))
seaborn.heatmap(corr, center=0, square=True, cmap=cmap, mask=mask)
plt.show()
```

Výsledný graf vypadá takto.

::fig[Notebook]{src=assets/korelaceni_matice.png}


### Přidání popisů v modulu matplotlib

Popisky můžeme doplnit i do grafu vytvořeného v modulu `matplotlib`, je však potřeba to udělat ručně. Můžeme k tomu využít kód s vnořeným cyklem, který do každého pole vloží hodnotu, která odpovídá hodnota v tabulce `df_actual_pivot`.

```py
import matplotlib.pyplot as plt

df_actual_pivot = pandas.pivot_table(dataset, values="ip_address", index="marketing_channel", columns="age_group", aggfunc=len)
fig, ax = plt.subplots()

plt.xticks(range(df_actual_pivot.shape[1]), df_actual_pivot.columns)
plt.yticks(range(df_actual_pivot.shape[0]), df_actual_pivot.index)

plt.imshow(df_actual_pivot, cmap ="viridis")
for i in range(df_actual_pivot.shape[0]):
    for j in range(df_actual_pivot.shape[1]):
        text = ax.text(j, i, df_actual_pivot.iloc[i, j],
                       ha="center", va="center", color="w")
plt.show()
```
