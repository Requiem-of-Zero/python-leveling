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


def split_time_for_dropdown(time_text):
    parsed = datetime.strptime(time_text, "%H:%M")

    hour = parsed.strftime("%I").lstrip("0")
    minute = parsed.strftime("%M")
    am_pm = parsed.strftime("%p")

    return hour, minute, am_pm


def get_week_start(year, week_number):
    return date.fromisocalendar(year, week_number, 1)


def get_current_week_selection():
    today = date.today()
    iso_year, iso_week, _ = today.isocalendar()
    return iso_year, iso_week


def format_week_summary(year, week_number, week_start):
    week_end = week_start + timedelta(days=6)
    return (
        f"Selected ISO week {week_number} of {year}: "
        f"{week_start.isoformat()} to {week_end.isoformat()}"
    )


def click_day(page, date_text):
    page.locator(f"td.fc-day-top[data-date='{date_text}']").click()


def choose_option(page, dropdown, option_name):
    dropdown.locator(".ui-dropdown-trigger").click()
    page.get_by_role("option", name=option_name, exact=True).click()


def fill_time_picker(page, picker, time_text):
    hour, minute, am_pm = split_time_for_dropdown(time_text)

    choose_option(page, picker.locator("p-dropdown[formcontrolname='hourPart']"), hour)
    choose_option(
        page, picker.locator("p-dropdown[formcontrolname='minutePart']"), minute
    )
    choose_option(page, picker.locator("p-dropdown[formcontrolname='amPmPart']"), am_pm)


def fill_day(page, values, defaults):
    entry = page.locator("app-time-entry")
    entry.wait_for(timeout=10000)

    project_dropdown = entry.locator("p-dropdown[formcontrolname='projectcode']")
    choose_option(page, project_dropdown, defaults["project"])

    first_attendance = page.locator("app-attendance-entry").nth(0)

    start_picker = first_attendance.locator(
        "app-time-picker[formcontrolname='startTime']"
    )
    end_picker = first_attendance.locator("app-time-picker[formcontrolname='endTime']")

    fill_time_picker(page, start_picker, values["start"])
    fill_time_picker(page, end_picker, values["first_end"])

    rest_break_dropdown = page.locator("p-dropdown[inputid='restBreak']").nth(0)

    choose_option(page, rest_break_dropdown, "Yes")
    entry = page.locator("app-time-entry")
    entry.get_by_role("button", name="Add").click()

    second_attendance = page.locator("app-attendance-entry").nth(1)
    second_attendance.wait_for(timeout=10000)

    attendance_type_dropdown = second_attendance.locator(
        "p-dropdown[formcontrolname='attendanceType']"
    )
    choose_option(page, attendance_type_dropdown, "Unpaid Meal Period")

    lunch_start_picker = second_attendance.locator(
        "app-time-picker[formcontrolname='startTime']"
    )
    lunch_end_picker = second_attendance.locator(
        "app-time-picker[formcontrolname='endTime']"
    )

    fill_time_picker(page, lunch_start_picker, values["lunch_start"])
    fill_time_picker(page, lunch_end_picker, values["lunch_end"])

    page.wait_for_timeout(500)
    entry.get_by_role("button", name="Add").click()

    third_attendance = page.locator("app-attendance-entry").nth(2)
    third_attendance.wait_for(timeout=10000)

    second_start_picker = third_attendance.locator(
        "app-time-picker[formcontrolname='startTime']"
    )
    end_picker = third_attendance.locator("app-time-picker[formcontrolname='endTime']")

    fill_time_picker(page, second_start_picker, values["second_start"])
    fill_time_picker(page, end_picker, values["end"])

    rest_break_dropdown = page.locator("p-dropdown[inputid='restBreak']").nth(1)
    choose_option(page, rest_break_dropdown, "Yes")

    entry.get_by_role("button", name="Save").click()
    page.locator(".ui-sidebar-active").wait_for(state="hidden", timeout=10000)
    page.locator(".ui-sidebar-mask").wait_for(state="hidden", timeout=10000)
    page.locator(".splash-screen").wait_for(state="hidden", timeout=10000)


def fill_week(page, profile, week_start):
    schedule = profile["schedule"]
    defaults = profile["defaults"]

    for index, day in enumerate(WEEKDAYS):
        day_date = week_start + timedelta(days=index)

        print(f"Filling {day.title()}: {day_date.isoformat()}")
        click_day(page, day_date.isoformat())
        fill_day(page, schedule[day], defaults)
        print(f"{day.title()} has been filled and saved.")


def open_timesheet(page):
    page.get_by_role("link", name="access_time TIME SHEET").click()
    page.locator(".fc-view-container").wait_for()
    page.locator(".splash-screen").wait_for(state="hidden")


def submit_timesheet(page):
    print("Submitting timesheet...")
    page.locator(".fc-submitButton-button").click()
    page.get_by_role("button", name="Yes").click()
    page.locator(".splash-screen").wait_for(state="hidden", timeout=10000)
    print("Submit action completed.")


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
