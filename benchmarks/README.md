# Benchmark protocol

CI checks the application test suite and benchmark-record format. The benchmark framework is a reporting scaffold only; it does not claim field-tested harvest performance.

## Record format

Store one JSON object per line in a versioned JSONL file (for example, `benchmarks/results.jsonl`). Each record must include:

- `scenario`: named scenario or test condition
- `metric`: metric name
- `value`: finite numeric value
- `unit`: unit or scale
- `split`: evaluation split, such as `test`, `simulation`, or `synthetic`
- `seed`: integer random seed
- `source`: dataset, simulator, or measurement source
- `notes`: concise protocol notes, limitations, and relevant configuration

Validate a file with:

```bash
python benchmarks/validate_results.py benchmarks/results.jsonl
```

CI checks the validator itself with:

```bash
python benchmarks/validate_results.py --self-test
```

## Metrics to prioritize

Suggested metrics to report separately by crop/lighting/occlusion condition:
- detection precision/recall or AP, with dataset and annotation protocol
- localization error (cm) and ripe-fruit classification precision/recall
- safe-reach proposal rate and human-review rate
- end-to-end latency (ms), missed detections, and false picks
- test episodes, hardware/simulator version, random seeds, and failure cases

## Research integrity

- Do not put fabricated or illustrative numbers in results files.
- Keep training/validation/test splits separate and document dataset licenses and provenance.
- Report sample counts, confidence intervals where appropriate, baselines, hardware, software versions, and failed runs.
- Label simulation, synthetic data, and real-world trials distinctly; never present one as another.
- Preserve raw predictions/logs and the evaluation script so results can be reproduced.
- A passing schema check only confirms record format. It does not establish model quality, safety, or deployment readiness.
