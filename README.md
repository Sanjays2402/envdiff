# envdiff

Compare two `.env` files and see which keys are missing, extra, or changed. Zero dependencies.

```
pip install .
envdiff .env.example .env
```

Output: `-` key only in the first file, `+` only in the second, `~` value differs (add `--values` to show them).
Exit code is `1` when differences exist, so it works in CI.

## Develop
```
pip install -e . pytest && pytest
```

MIT licensed. Contributions welcome.
