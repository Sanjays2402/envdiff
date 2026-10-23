import argparse
import sys

from .core import diff_envs, parse_env


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="envdiff", description="Compare two .env files.")
    p.add_argument("a", help="first .env file (e.g. .env.example)")
    p.add_argument("b", help="second .env file (e.g. .env)")
    p.add_argument("--values", action="store_true", help="show values of changed keys")
    args = p.parse_args(argv)

    with open(args.a, encoding="utf-8") as f:
        ea = parse_env(f.read())
    with open(args.b, encoding="utf-8") as f:
        eb = parse_env(f.read())
    d = diff_envs(ea, eb)

    for k in d["only_a"]:
        print(f"- {k}  (only in {args.a})")
    for k in d["only_b"]:
        print(f"+ {k}  (only in {args.b})")
    for k in d["changed"]:
        suffix = f"  {ea[k]!r} -> {eb[k]!r}" if args.values else ""
        print(f"~ {k}{suffix}")
    return 1 if any(d.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
