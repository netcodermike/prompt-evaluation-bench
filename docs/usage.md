# Using Prompt Evaluation Bench

## Quick start

Cases require unique `id`, `prompt`, and at least one `contains`, `forbidden`, or `regex` assertion. Offline mode uses `response`; `--model NAME` calls local Ollama. Treat regex configurations as trusted input.

## Supported workflow

1. Deterministic model-response assertions.
2. Optional real localhost Ollama inference.
3. Per-check outcomes and measured latency.

## Validation and troubleshooting

Run the commands in the README. Invalid inputs produce explicit errors rather than silently changing the requested operation. Browser audio requires a user gesture; microphone apps require HTTPS or localhost and permission. For file tools, supply supported input formats and writable output directories.

## Limitations

String and regex checks assess specified criteria, not general truthfulness. Live inference needs a separately installed model.

Tests use synthetic fixtures. These tests do not certify hardware compatibility, real-world forecast quality, trained-model accuracy, or production suitability for every input.
