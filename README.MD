# Assessment of Travel Home to Work

This repository contains code and resources for analyzing travel patterns from home to work.
You can see states in plotted graph, analyzing the time spend travel from home to work.

### Here, you can see: 

* Analyze travel time

* Visualize the data, specifically by plotting graphs that can show information by state.

* The diference between your time spend from home to work, comparing your time with a databases (%% time).


### Resources to Compiling

* First you need donwloading of libraries in your enviroment to run the code. You can see in 'Requirements.txt'. (But before verified if have .venv in your enviroment to downloadind)

  * To see if have .venv, you need following this step:

    1) python -m venv .venv (obs: you can select other name for .venv, im using in this way, because to me as more simple)
    2) source .venv/bin/activate (you will activate this enviroment)

    3) verified if have .venv in your terminal (hes appear before your user count name); after made this, you can put the comand: **pip install -r requirements.txt** 


* In the second phase to compile, you need the archive as named with 'BR_Municipios_2024'
  * You need visit this website to donwload the archive used to plot graphs (in this context specified he write the line of the state) here: 
    * https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html.

  * You made the donwload of path named with 'Municípios | Unidades da Federação | Grandes Regiões | Regiões Geográficas Imediatas | Regiões Geográficas Intermediárias | País' click in the redirect, you will made the download of the arhive.

  * After you made the donwload, you will unzip, to put on the path './geo'

  * Obs: We only use the 'BR_Municipios_2024.shp' only it. He wil used in malhas_br.py code. 