"""Catálogo de bases públicas de dados de física.

Gera um CSV com nome, link, tema, formato e tamanho de cada fonte,
para apoiar a seleção de dados dos próximos experimentos.

Uso:
    python mapear_fontes.py [--saida caminho/do/arquivo.csv]

Por padrão, o CSV é salvo na mesma pasta do script.
"""

import argparse
from pathlib import Path

import pandas as pd

COLUNAS = ["nome", "link", "tema", "formato", "tamanho"]
SAIDA_PADRAO = Path(__file__).resolve().parent / "fontes_fisica.csv"

FONTES = [
    {
        "nome": "The Well (PolymathicAI)",
        "link": "https://github.com/PolymathicAI/the_well",
        "tema": "Simulações numéricas: fluidos, turbulência, MHD, acústica, sistemas biológicos",
        "formato": "HDF5 (interface PyTorch; streaming pelo Hugging Face)",
        "tamanho": "15 TB em 16 datasets",
    },
    {
        "nome": "HIGGS (UCI)",
        "link": "https://archive.ics.uci.edu/dataset/280/higgs",
        "tema": "Física de partículas: sinal de bóson de Higgs vs. ruído (classificação)",
        "formato": "CSV compactado (.csv.gz)",
        "tamanho": "11 milhões de linhas, 28 features, 2,6 GB",
    },
    {
        "nome": "MAGIC Gamma Telescope (UCI)",
        "link": "https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope",
        "tema": "Astrofísica de altas energias: raios gama vs. hádrons (classificação)",
        "formato": "CSV (magic04.data)",
        "tamanho": "19.020 linhas, 10 features, 1,4 MB",
    },
    {
        "nome": "Stellar Classification SDSS17 (Kaggle)",
        "link": "https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17",
        "tema": "Astronomia: classificação de estrelas, galáxias e quasares",
        "formato": "CSV",
        "tamanho": "100.000 linhas, 17 features + classe",
    },
    {
        "nome": "NASA Exoplanet Archive",
        "link": "https://exoplanetarchive.ipac.caltech.edu",
        "tema": "Exoplanetas: massa, raio, órbita e estrela hospedeira",
        "formato": "CSV / VOTable (download e API TAP)",
        "tamanho": "~6.150 planetas confirmados (atualização semanal)",
    },
    {
        "nome": "CERN Open Data Portal",
        "link": "https://opendata.cern.ch",
        "tema": "Física de partículas: colisões do LHC (CMS, ATLAS, ALICE, LHCb)",
        "formato": "ROOT (amostras educacionais em CSV)",
        "tamanho": "Mais de 5 PB no total",
    },
    {
        "nome": "Gaia DR3 (ESA)",
        "link": "https://gea.esac.esa.int/archive/",
        "tema": "Astrometria: posição, paralaxe e movimento próprio de estrelas",
        "formato": "Consultas ADQL/TAP -> CSV, FITS, VOTable",
        "tamanho": "~1,8 bilhão de fontes",
    },
    {
        "nome": "GWOSC (LIGO/Virgo/KAGRA)",
        "link": "https://gwosc.org",
        "tema": "Ondas gravitacionais: séries de strain e catálogos de eventos",
        "formato": "HDF5 e GWF (biblioteca gwpy)",
        "tamanho": "Séries a 4096 ou 16384 Hz, arquivos de 4096 s por corrida",
    },
    {
        "nome": "Materials Project",
        "link": "https://next-gen.materialsproject.org",
        "tema": "Física de materiais: estrutura cristalina, band gap e energia (DFT)",
        "formato": "JSON via API (pacote mp-api; chave gratuita)",
        "tamanho": "Mais de 140 mil materiais",
    },
    {
        "nome": "NIST Atomic Spectra Database (ASD)",
        "link": "https://physics.nist.gov/asd",
        "tema": "Física atômica: linhas espectrais e níveis de energia",
        "formato": "Tabelas web exportáveis (CSV / texto)",
        "tamanho": "~300 mil linhas espectrais (versão 5.12)",
    },
]


def montar_catalogo(fontes: list[dict]) -> pd.DataFrame:
    """Converte a lista de fontes em DataFrame com colunas na ordem padrão."""
    return pd.DataFrame(fontes, columns=COLUNAS)


def validar_catalogo(df: pd.DataFrame, total_esperado: int = 10) -> None:
    """Garante a quantidade de fontes e que nenhum campo esteja vazio."""
    if len(df) != total_esperado:
        raise ValueError(f"Esperadas {total_esperado} fontes, encontradas {len(df)}.")

    vazios = df.isna() | df.astype(str).apply(lambda col: col.str.strip().eq(""))
    if vazios.any().any():
        linhas = df.loc[vazios.any(axis=1), "nome"].tolist()
        raise ValueError(f"Campos vazios nas fontes: {linhas}")

    if df["link"].duplicated().any():
        raise ValueError("Há links duplicados no catálogo.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Exporta o catálogo de bases de física para CSV.")
    parser.add_argument("--saida", type=Path, default=SAIDA_PADRAO, help="Caminho do CSV de saída.")
    args = parser.parse_args()

    catalogo = montar_catalogo(FONTES)
    validar_catalogo(catalogo)

    # utf-8-sig preserva a acentuação ao abrir o arquivo no Excel.
    catalogo.to_csv(args.saida, index=False, encoding="utf-8-sig")
    print(f"{len(catalogo)} fontes exportadas para {args.saida}")


if __name__ == "__main__":
    main()
