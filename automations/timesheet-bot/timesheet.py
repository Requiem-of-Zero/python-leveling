from datetime import datetime, date, timedelta

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday"]


def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")


def calculate_day_hours(values):
    start = parse_time(values["start"])
    first_end = parse_time(values["first_end"])
    second_start = parse_time(values["second_start"])
    end = parse_time(values["end"])

    morning = first_end - start
    afternoon = end - second_start

    total = morning + afternoon

    return total.seconds / 3600


def get_week_start(year, week_number):
    return date.fromisocalendar(year, week_number, 1)


def click_day(page, date_text):
    page.locator(f"td.fc-day-top[data-date='{date_text}']").click()


def choose_option(page, select, option_name):
    select.click()
    page.get_by_role("option", name=option_name).click()


def fill_day(page, values, defaults):
    entry = page.locator("app-time-entry")
    entry.wait_for(timeout=10000)

    project_dropdown = entry.locator("p-dropdown[formcontrolname='projectcode']")
    project_dropdown.click()

    page.get_by_role("option", name=defaults["project"], exact=True).click()
    page.pause()


def open_timesheet(page):
    page.get_by_role("link", name="access_time TIME SHEET").click()
    page.locator(".fc-view-container").wait_for()
    page.locator(".splash-screen").wait_for(state="hidden")


def print_review(profile):
    schedule = profile["schedule"]
    total_hours = 0

    print()
    print(f"Profile: {profile["name"]}")
    print()

    for day in WEEKDAYS:
        values = schedule[day]

        hours = calculate_day_hours(values)

        total_hours += hours

        print(
            f"{day.title():<10}"
            f"{values['start']}-{values['first_end']} / "
            f"{values['second_start']}-{values['end']}"
            " Lunch:"
            f"{values["lunch_start"]}-{values["lunch_end"]}"
        )

    print()
    print(f"Total: {total_hours:.1f} hours")
