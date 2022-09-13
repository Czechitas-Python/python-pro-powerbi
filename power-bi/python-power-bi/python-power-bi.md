## Python a Power BI

Před začátkem práce je vhodné zkontrolovat nastavení Power BI a propojení s jazykem Python.

### Nastavení

Power BI obvykle zvládne najít instalaci Pythonu. Před začátkem práce je ale dobré si nastavení zkontrolovat. Otevřeme si menu `File -> Options and Settings -> Options` a v dialogovém okně zvolíme `Python Scripting`. V menu `Detected Python home directories` je přehled instalací Pythonu, které byly Power BI detekovány.

::fig[Notebook]{src=assets/vyber_instalaci.png}

Pokud není požadovaná instalace na výběr, můžeme zvolit možnost `Other` a zadat adresář s požadovanou instalací ručně.

::fig[Notebook]{src=assets/vyber_instalaci_other.png}

### Příklady užití

Přestože má Power BI k dispozici nástroj Power Query, v řadě případů může být vhodné využít skripty v jazyce Python. Typické příklady využití jsou následující:

- Máme k dispozici již hotový program nebo skript na zpracování dat a chceme výsledky zobrazit v prostředí Power BI.
- Operace, kterou chceme provést, je v prostředí Power BI příliš komplikovaná (nebo nemožná), zatímco v modulu `pandas` jednoduchá.
- Distribuce modelů a reportů uživatelům bez hlubších technických znalostí.
