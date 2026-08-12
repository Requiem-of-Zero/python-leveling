from profiles import load_profile
from timesheet import print_review, get_week_start, open_timesheet, click_day, fill_day
from portal import open_portal, is_logged_in, wait_for_manual_login
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Fill ConnexApp timesheets from a profile."
    )
    parser.add_argument("--profile", default="default")
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--week-number", type=int, required=True)

    args = parser.parse_args()

    print("Timesheet bot starting...")

    profile = load_profile(args.profile)

    print_review(profile)

    week_start = get_week_start(args.year, args.week_number)
    print(f"Selected week starts on: {week_start}")

    playwright, context, page = open_portal(profile["portal_url"])

    print(page.url)
    print(is_logged_in(page))

    if not is_logged_in(page):
        wait_for_manual_login(page)

    print(page.url)
    print(is_logged_in(page))

    open_timesheet(page)
    click_day(page, week_start.isoformat())
    fill_day(page, profile["schedule"]["monday"], profile["defaults"])

    input("Press Enter to close browser...")

    context.close()
    playwright.stop()


if __name__ == "__main__":
    main()
