from pathlib import Path
import yaml

PROFILE_DIR = Path(__file__).parent / "profiles"


def load_profile(profile_name):
    profile_path = PROFILE_DIR / f"{profile_name}.yaml"

    with profile_path.open("r", encoding="utf-8") as file:
        profile = yaml.safe_load(file)

    return profile
