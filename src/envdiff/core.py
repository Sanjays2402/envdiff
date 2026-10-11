import re

_LINE = re.compile(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_.]*)\s*=\s*(.*)$")


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    # strip trailing inline comment on unquoted values
    return re.split(r"\s+#", value, maxsplit=1)[0].strip()


def parse_env(text: str) -> dict:
    """Parse .env text into a dict. Ignores blanks and comments."""
    result = {}
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = _LINE.match(line)
        if m:
            result[m.group(1)] = _unquote(m.group(2))
    return result


def diff_envs(a: dict, b: dict) -> dict:
    """Return keys only in a, only in b, and keys whose values differ."""
    return {
        "only_a": sorted(a.keys() - b.keys()),
        "only_b": sorted(b.keys() - a.keys()),
        "changed": sorted(k for k in a.keys() & b.keys() if a[k] != b[k]),
    }
