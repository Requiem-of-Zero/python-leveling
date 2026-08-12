WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday"]


def print_review(profile):
    schedule = profile["schedule"]

    print()
    print(f"Profile: {profile["name"]}")
    print()

    for day in WEEKDAYS:
        values = schedule[day]

        print(
            f"{day.title():<10}"
            f"{values['start']}-{values['first_end']} / "
            f"{values['second_start']}-{values['end']}"
            " Lunch:"
            f"{values["lunch_start"]}-{values["lunch_end"]}"
        )
