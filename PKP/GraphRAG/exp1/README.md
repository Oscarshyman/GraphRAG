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