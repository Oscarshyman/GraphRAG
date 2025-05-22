# Experiment
5 iterations  of Auto-Prompt-tuning with same parameters



mkdir `input` and add txt files
## In `settings.yaml`

    `model: gpt-4o-mini`
    for cache --> `base_dir: "cache_grag-<1>"`
    for output storage --> `base_dir: "output_grag-<1>"`

Then run,

`python -m graphrag prompt-tune --root ./grag-1 --config ./grag-1/settings.yaml  --domain "Senescence" --min-examples-required 5`