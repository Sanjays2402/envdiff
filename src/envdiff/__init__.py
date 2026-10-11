"""envdiff: compare .env files."""
from .core import parse_env, diff_envs

__all__ = ["parse_env", "diff_envs"]
__version__ = "0.1.0"
