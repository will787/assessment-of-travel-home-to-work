import geopandas as gpd
import json
import sys
from pathlib import Path


def select_uf(state_uf: str) -> Path:
    """
    Selects municipalities for a given state (UF), saves them as a GeoJSON file,
    and returns the path to the generated file. If the file already exists,
    it skips the generation.
    """
    script_dir = Path(__file__).parent
    shapefile_path = script_dir / "BR_Municipios_2024/BR_Municipios_2024.shp"
    output_dir = script_dir / "json_states"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"municipios_{state_uf.lower()}.geojson"

    if output_path.exists():
        print(f"GeoJSON for {state_uf.upper()} already exists. Skipping generation.")
        return output_path

    print(f"Generating GeoJSON for {state_uf.upper()}...")
    malha_municipal = gpd.read_file(shapefile_path)
    gdf_state = malha_municipal[malha_municipal['SIGLA_UF'] == state_uf.upper()]
    print(gdf_state.head())
    gdf_state.to_file(output_path, driver='GeoJSON')
    print(f"Successfully created {output_path}")
    return output_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        select_uf(sys.argv[1])
    else:
        print("Passe a sigla do estado como argumento. Exemplo: python malhas_br.py SP")

# usage (Example) you can create with of state interest: 
# python malhas_br.py SP