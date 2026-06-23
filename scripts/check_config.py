from pathlib import Path
import sys
import yaml


REQUIRED_KEYS = ["katago_path", "model_path", "config_path"]


def load_config(config_path: Path) -> dict:
    if not config_path.exists():
        raise FileNotFoundError(
            f"Missing {config_path}. Create local_config.yaml from "
            f"configs/local_config.example.yaml and fill in your local paths."
        )

    with config_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if config is None:
        raise ValueError(f"{config_path} is empty.")

    return config


def check_paths(config: dict) -> bool:
    all_ok = True

    for key in REQUIRED_KEYS:
        if key not in config:
            print(f"[MISSING KEY] {key}")
            all_ok = False
            continue

        path = Path(config[key])
        if path.exists():
            print(f"[OK]      {key}: {path}")
        else:
            print(f"[MISSING] {key}: {path}")
            all_ok = False

    return all_ok


def main() -> int:
    config_path = Path("local_config.yaml")

    try:
        config = load_config(config_path)
    except Exception as e:
        print(f"[ERROR] {e}")
        return 1

    all_ok = check_paths(config)

    if all_ok:
        print("\nConfig check passed.")
        return 0
    else:
        print("\nConfig check failed. Fix local_config.yaml paths.")
        return 1


if __name__ == "__main__":
    sys.exit(main())