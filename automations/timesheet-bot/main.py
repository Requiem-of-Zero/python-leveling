from profiles import load_profile
from timesheet import (
    fill_week,
    format_week_summary,
    get_current_week_selection,
    get_week_start,
    open_timesheet,
    print_review,
)
from portal import has_login_credentials, open_portal, login_if_needed
import argparse


def build_parser():
    current_year, current_week = get_current_week_selection()

    parser = argparse.ArgumentParser(
        description="Fill ConnexApp timesheets from a saved profile.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            f"Current ISO week: {current_week} of {current_year}\n\n"
            "Examples:\n"
            "  python main.py\n"
            "  python main.py --profile default\n"
            f"  python main.py --year {current_year} --week-number {current_week}\n"
            "  python main.py --profile local --headless\n"
            "  python main.py --profile john --year 2026 --week-number 33"
        ),
    )
    parser.add_argument(
        "--profile",
        default="default",
        help="Profile name from profiles/<name>.yaml. Default: default",
    )
    parser.add_argument(
        "--year",
        type=int,
        help=f"ISO week-numbering year. Default: current year ({current_year})",
    )
    parser.add_argument(
        "--week-number",
        type=int,
        help=f"ISO week number to fill. Default: current week ({current_week})",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run without showing the browser. Only used when profile login credentials are configured.",
    )
    return parser


def main():
    parser = build_parser()

    args = parser.parse_args()

    print("Timesheet bot starting...")

    profile = load_profile(args.profile)

    print_review(profile)

    if args.year is None and args.week_number is None:
        year, week_number = get_current_week_selection()
        print(f"No week specified. Using current ISO week: {week_number} of {year}")
    elif args.year is None or args.week_number is None:
        parser.error("--year and --week-number must be used together.")
    else:
        year = args.year
        week_number = args.week_number

    week_start = get_week_start(year, week_number)
    print(format_week_summary(year, week_number, week_start))

    defaults = profile.get("defaults", {})
    login_config = defaults.get("login", profile.get("login"))
    can_login_automatically = has_login_credentials(login_config)
    use_headless = args.headless and can_login_automatically

    if args.headless and not can_login_automatically:
        print("Headless requested, but no login credentials are configured.")
        print("Opening a visible browser so manual login can work.")

    playwright, context, page = open_portal(profile["portal_url"], headless=use_headless)

    login_if_needed(page, login_config)

    open_timesheet(page)
    fill_week(page, profile, week_start)

    if not use_headless:
        input("Press Enter to close browser...")

    context.close()
    playwright.stop()


if __name__ == "__main__":
    main()
