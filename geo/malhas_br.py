import geopandas as gpd
import json
import sys

def select_uf(state_uf):
    malha_municipal = gpd.read_file("BR_Municipios_2024/BR_Municipios_2024.shp")
    gdf_state = malha_municipal[malha_municipal['SIGLA_UF'] == state_uf]
    print(gdf_state.head())
    gdf_state.to_file(f"json_states/municipios_{state_uf.lower()}.geojson", driver='GeoJSON')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        select_uf(sys.argv[1])
    else:
        print("Passe a sigla do estado como argumento. Exemplo: python malhas_br.py SP")

# usage (Example) you can create with of state interest: 
# python malhas_br.py SP