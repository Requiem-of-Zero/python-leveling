from profiles import load_profile
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Fill ConnexApp timesheets from a profile."
    )
    parser.add_argument("--profile", default="default")

    args = parser.parse_args()

    print("Timesheet bot starting...")

    profile = load_profile(args.profile)

    print(profile)


if __name__ == "__main__":
    main()
