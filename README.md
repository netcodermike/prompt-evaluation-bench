# Prompt Evaluation Bench

Score model responses against reproducible contains, forbidden-text, and regular-expression checks.

**Language:** Python · **License:** MIT · **Data:** Local by default

## What it does

- Deterministic model-response assertions
- Optional real localhost Ollama inference
- Per-check outcomes and measured latency

## Requirements

Python 3.10 or newer. Uses the Python standard library unless explicitly noted.

## Install, validate, and run

```sh
python app.py --self-test
python app.py examples/cases.jsonl
```

Run `--help` where supported, or follow the examples in [docs/usage.md](docs/usage.md). Input files are never overwritten unless explicitly documented.

## Usage and examples

See [docs/usage.md](docs/usage.md) for a walkthrough and [docs/architecture.md](docs/architecture.md) for implementation details. Tests are deterministic and do not require an exchange, paid API, external model, microphone, or private data.

## Boundaries

String and regex checks assess specified criteria, not general truthfulness. Live inference needs a separately installed model.

## Privacy

No analytics or accounts are built in. Local file tools process only the paths you supply. For model-server and weather apps, the interface and usage guide identify the destination and the data sent. Do not commit personal input files, model credentials, or generated recordings.

## Development

Run the validation commands above before submitting changes. GitHub Actions runs these checks on pushes and pull requests. See the workflow for the reproducible toolchain. A successful workflow verifies the tested paths; manual audio-device behavior is documented separately.
