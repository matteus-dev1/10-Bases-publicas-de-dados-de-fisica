# Fontes públicas de dados de física

Catálogo de 10 bases públicas de dados de física, levantado para apoiar a escolha de dados dos próximos experimentos.

## Conteúdo

| Arquivo | Descrição |
|---|---|
| `fontes_fisica.csv` | Catálogo com nome, link, tema, formato e tamanho de cada base |
| `mapear_fontes.py` | Script que monta o catálogo com pandas, valida os campos e exporta o CSV |
| `explorar_magic.ipynb` | Exploração da base MAGIC (a menor do catálogo): download, estrutura, estatísticas, gráficos e resumo |
| `requirements.txt` | Dependências do projeto |

## Bases catalogadas

| Base | Área | Formato |
|---|---|---|
| The Well (PolymathicAI) | Simulações numéricas | HDF5 |
| HIGGS (UCI) | Física de partículas | CSV |
| MAGIC Gamma Telescope (UCI) | Astrofísica de altas energias | CSV |
| Stellar Classification SDSS17 (Kaggle) | Astronomia | CSV |
| NASA Exoplanet Archive | Exoplanetas | CSV / VOTable |
| CERN Open Data Portal | Física de partículas | ROOT |
| Gaia DR3 (ESA) | Astrometria | CSV / FITS / VOTable |
| GWOSC (LIGO/Virgo/KAGRA) | Ondas gravitacionais | HDF5 / GWF |
| Materials Project | Física de materiais | JSON (API) |
| NIST Atomic Spectra Database | Física atômica | CSV / texto |

## Como executar

Requer Python 3.10 ou superior.

```bash
python -m pip install -r requirements.txt
python mapear_fontes.py
```

O CSV é gerado na mesma pasta do script. Para outro destino:

```bash
python mapear_fontes.py --saida caminho/do/arquivo.csv
```

Antes de exportar, o script verifica se há exatamente 10 bases, se nenhum campo está vazio e se não há links duplicados.

## Observações

- Levantamento feito em novembro de 2026. Alguns tamanhos mudam com o tempo (por exemplo, o número de exoplanetas confirmados é atualizado semanalmente).
- Materials Project exige uma chave de API gratuita.
- Para primeiros testes de machine learning, MAGIC e SDSS17 são as opções mais leves. The Well e CERN Open Data exigem mais infraestrutura pelo volume.
