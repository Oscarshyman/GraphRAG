# Experiment
5 iterations  of Auto-Prompt-tuning with same parameters

## initialise graphrag
graphrag init --root ./grag-1

mkdir `input` and add txt files

(assing OPEN-AI key in .env)
## In `settings.yaml`

    `model: gpt-4o-mini`
    for cache --> `base_dir: "cache_grag-<1>"`
    for output storage --> `base_dir: "output_grag-<1>"`

    `graphml:true`


## Auto-tuning

cd into the specific grag folder ( `cd grag-1`)

`graphrag prompt-tune --root . --config ./settings.yaml  --domain "Senescence" --min-examples-required 5`

## Run Graphrag Pipeline

cd ..  
graphrag index --root ./grag-1


# Miscellaneous
## Dependencies
(local PC conda VM grag3)

| # packages in environment at C:\Users\Partha\anaconda3\envs\grag3: |              |                 |         |
|--------------------------------------------------------------------|--------------|-----------------|---------|
| #                                                                  |              |                 |         |
| # Name                                                             | Version      | Build           | Channel |
| aiofiles                                                           | 24.1.0       | pypi_0          | pypi    |
| aiolimiter                                                         | 1.2.1        | pypi_0          | pypi    |
| annotated-types                                                    | 0.7.0        | pypi_0          | pypi    |
| anyio                                                              | 4.9.0        | pypi_0          | pypi    |
| anytree                                                            | 2.13.0       | pypi_0          | pypi    |
| asttokens                                                          | 2.4.1        | pypi_0          | pypi    |
| autograd                                                           | 1.8.0        | pypi_0          | pypi    |
| azure-common                                                       | 1.1.28       | pypi_0          | pypi    |
| azure-core                                                         | 1.34.0       | pypi_0          | pypi    |
| azure-cosmos                                                       | 4.9.0        | pypi_0          | pypi    |
| azure-identity                                                     | 1.23.0       | pypi_0          | pypi    |
| azure-search-documents                                             | 11.5.2       | pypi_0          | pypi    |
| azure-storage-blob                                                 | 12.25.1      | pypi_0          | pypi    |
| beartype                                                           | 0.18.5       | pypi_0          | pypi    |
| blis                                                               | 1.2.1        | pypi_0          | pypi    |
| bzip2                                                              | 1.0.8        | h2bbff1b_6      |         |
| ca-certificates                                                    | 2025.2.25    | haa95532_0      |         |
| catalogue                                                          | 2.0.10       | pypi_0          | pypi    |
| certifi                                                            | 2025.4.26    | pypi_0          | pypi    |
| cffi                                                               | 1.17.1       | pypi_0          | pypi    |
| charset-normalizer                                                 | 3.4.2        | pypi_0          | pypi    |
| click                                                              | 8.1.8        | pypi_0          | pypi    |
| cloudpathlib                                                       | 0.21.1       | pypi_0          | pypi    |
| colorama                                                           | 0.4.6        | pypi_0          | pypi    |
| confection                                                         | 0.1.5        | pypi_0          | pypi    |
| contourpy                                                          | 1.3.2        | pypi_0          | pypi    |
| cryptography                                                       | 45.0.3       | pypi_0          | pypi    |
| cycler                                                             | 0.12.1       | pypi_0          | pypi    |
| cymem                                                              | 2.0.11       | pypi_0          | pypi    |
| deprecation                                                        | 2.1.0        | pypi_0          | pypi    |
| devtools                                                           | 0.12.2       | pypi_0          | pypi    |
| distro                                                             | 1.9.0        | pypi_0          | pypi    |
| environs                                                           | 11.2.1       | pypi_0          | pypi    |
| executing                                                          | 2.2.0        | pypi_0          | pypi    |
| fnllm                                                              | 0.3.0        | pypi_0          | pypi    |
| fonttools                                                          | 4.58.1       | pypi_0          | pypi    |
| future                                                             | 1.0.0        | pypi_0          | pypi    |
| gensim                                                             | 4.3.3        | pypi_0          | pypi    |
| graphrag                                                           | 2.3.0        | pypi_0          | pypi    |
| graspologic                                                        | 3.4.1        | pypi_0          | pypi    |
| graspologic-native                                                 | 1.2.5        | pypi_0          | pypi    |
| h11                                                                | 0.16.0       | pypi_0          | pypi    |
| httpcore                                                           | 1.0.9        | pypi_0          | pypi    |
| httpx                                                              | 0.28.1       | pypi_0          | pypi    |
| hyppo                                                              | 0.4.0        | pypi_0          | pypi    |
| idna                                                               | 3.10         | pypi_0          | pypi    |
| isodate                                                            | 0.7.2        | pypi_0          | pypi    |
| jinja2                                                             | 3.1.6        | pypi_0          | pypi    |
| jiter                                                              | 0.10.0       | pypi_0          | pypi    |
| joblib                                                             | 1.5.1        | pypi_0          | pypi    |
| json-repair                                                        | 0.30.3       | pypi_0          | pypi    |
| kiwisolver                                                         | 1.4.8        | pypi_0          | pypi    |
| lancedb                                                            | 0.17.0       | pypi_0          | pypi    |
| langcodes                                                          | 3.5.0        | pypi_0          | pypi    |
| language-data                                                      | 1.3.0        | pypi_0          | pypi    |
| libffi                                                             | 3.4.4        | hd77b12b_1      |         |
| llvmlite                                                           | 0.44.0       | pypi_0          | pypi    |
| marisa-trie                                                        | 1.2.1        | pypi_0          | pypi    |
| markdown-it-py                                                     | 3.0.0        | pypi_0          | pypi    |
| markupsafe                                                         | 3.0.2        | pypi_0          | pypi    |
| marshmallow                                                        | 4.0.0        | pypi_0          | pypi    |
| matplotlib                                                         | 3.10.3       | pypi_0          | pypi    |
| mdurl                                                              | 0.1.2        | pypi_0          | pypi    |
| msal                                                               | 1.32.3       | pypi_0          | pypi    |
| msal-extensions                                                    | 1.3.1        | pypi_0          | pypi    |
| murmurhash                                                         | 1.0.13       | pypi_0          | pypi    |
| networkx                                                           | 3.5          | pypi_0          | pypi    |
| nltk                                                               | 3.9.1        | pypi_0          | pypi    |
| numba                                                              | 0.61.2       | pypi_0          | pypi    |
| numpy                                                              | 1.26.4       | pypi_0          | pypi    |
| openai                                                             | 1.84.0       | pypi_0          | pypi    |
| openssl                                                            | 3.0.16       | h3f729d1_0      |         |
| overrides                                                          | 7.7.0        | pypi_0          | pypi    |
| packaging                                                          | 25.0         | pypi_0          | pypi    |
| pandas                                                             | 2.3.0        | pypi_0          | pypi    |
| patsy                                                              | 1.0.1        | pypi_0          | pypi    |
| pillow                                                             | 11.2.1       | pypi_0          | pypi    |
| pip                                                                | 25.1         | pyhc872135_2    |         |
| pot                                                                | 0.9.5        | pypi_0          | pypi    |
| preshed                                                            | 3.0.10       | pypi_0          | pypi    |
| pyarrow                                                            | 20.0.0       | pypi_0          | pypi    |
| pycparser                                                          | 2.22         | pypi_0          | pypi    |
| pydantic                                                           | 2.11.5       | pypi_0          | pypi    |
| pydantic-core                                                      | 2.33.2       | pypi_0          | pypi    |
| pygments                                                           | 2.19.1       | pypi_0          | pypi    |
| pyjwt                                                              | 2.10.1       | pypi_0          | pypi    |
| pylance                                                            | 0.20.0       | pypi_0          | pypi    |
| pynndescent                                                        | 0.5.13       | pypi_0          | pypi    |
| pyparsing                                                          | 3.2.3        | pypi_0          | pypi    |
| python                                                             | 3.11.11      | h4607a30_0      |         |
| python-dateutil                                                    | 2.9.0.post0  | pypi_0          | pypi    |
| python-dotenv                                                      | 1.1.0        | pypi_0          | pypi    |
| pytz                                                               | 2025.2       | pypi_0          | pypi    |
| pyyaml                                                             | 6.0.2        | pypi_0          | pypi    |
| regex                                                              | 2024.11.6    | pypi_0          | pypi    |
| requests                                                           | 2.32.3       | pypi_0          | pypi    |
| rich                                                               | 13.9.4       | pypi_0          | pypi    |
| scikit-learn                                                       | 1.6.1        | pypi_0          | pypi    |
| scipy                                                              | 1.12.0       | pypi_0          | pypi    |
| seaborn                                                            | 0.13.2       | pypi_0          | pypi    |
| setuptools                                                         | 78.1.1       | py311haa95532_0 |         |
| shellingham                                                        | 1.5.4        | pypi_0          | pypi    |
| six                                                                | 1.17.0       | pypi_0          | pypi    |
| smart-open                                                         | 7.1.0        | pypi_0          | pypi    |
| sniffio                                                            | 1.3.1        | pypi_0          | pypi    |
| spacy                                                              | 3.8.7        | pypi_0          | pypi    |
| spacy-legacy                                                       | 3.0.12       | pypi_0          | pypi    |
| spacy-loggers                                                      | 1.0.5        | pypi_0          | pypi    |
| sqlite                                                             | 3.45.3       | h2bbff1b_0      |         |
| srsly                                                              | 2.5.1        | pypi_0          | pypi    |
| statsmodels                                                        | 0.14.4       | pypi_0          | pypi    |
| tenacity                                                           | 9.1.2        | pypi_0          | pypi    |
| textblob                                                           | 0.18.0.post0 | pypi_0          | pypi    |
| thinc                                                              | 8.3.4        | pypi_0          | pypi    |
| threadpoolctl                                                      | 3.6.0        | pypi_0          | pypi    |
| tiktoken                                                           | 0.9.0        | pypi_0          | pypi    |
| tk                                                                 | 8.6.14       | h5e9d12e_1      |         |
| tqdm                                                               | 4.67.1       | pypi_0          | pypi    |
| typer                                                              | 0.15.4       | pypi_0          | pypi    |
| typing-extensions                                                  | 4.14.0       | pypi_0          | pypi    |
| typing-inspection                                                  | 0.4.1        | pypi_0          | pypi    |
| tzdata                                                             | 2025.2       | pypi_0          | pypi    |
| umap-learn                                                         | 0.5.7        | pypi_0          | pypi    |
| urllib3                                                            | 2.4.0        | pypi_0          | pypi    |
| vc                                                                 | 14.42        | haa95532_5      |         |
| vs2015_runtime                                                     | 14.42.34433  | hbfb602d_5      |         |
| wasabi                                                             | 1.1.3        | pypi_0          | pypi    |
| weasel                                                             | 0.4.1        | pypi_0          | pypi    |
| wheel                                                              | 0.45.1       | py311haa95532_0 |         |
| wrapt                                                              | 1.17.2       | pypi_0          | pypi    |
| xz                                                                 | 5.6.4        | h4754444_1      |         |
| zlib                                                               | 1.2.13       | h8cc25b3_1      |         |