# ConnexApp Timesheet Bot

Python + Playwright automation for filling ConnexApp timesheets from a local YAML profile.

The bot opens ConnexApp in a visible browser, uses your normal login session, fills the configured week, and leaves final review in the browser for submission.

## Setup

From this directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Run

Use the current ISO week:

```bash
python main.py
```

Use a specific profile:

```bash
python main.py --profile default
```

Use a specific ISO week:

```bash
python main.py --profile default --year 2026 --week-number 33
```

Show available options and the current ISO week:

```bash
python main.py --help
```

## Login

The bot does not store usernames or passwords. Log into ConnexApp normally in the browser window. Playwright can reuse the local browser session on later runs through `browser-data/`.

## Profiles

Profiles live in `profiles/` and are selected by filename:

```bash
python main.py --profile default
```

loads:

```text
profiles/default.yaml
```

Copy `profiles/example.yaml` to create a new user/profile:

```bash
cp profiles/example.yaml profiles/john.yaml
python main.py --profile john
```

## Profile Sections

`name`

Human-readable profile name printed in the review summary.

`portal_url`

ConnexApp URL. Usually:

```yaml
portal_url: "https://connexapp.dayzim.com/web/"
```

`schedule`

Work times for each weekday. Times are 24-hour strings.

Each day uses:

```yaml
start: "08:00"
first_end: "12:00"
lunch_start: "12:00"
lunch_end: "12:30"
second_start: "12:30"
end: "16:30"
```

`defaults.project`

The exact ConnexApp project code option to select from the Project Code dropdown.

Example:

```yaml
defaults:
  project: "107930~SVGOOGB~1367"
```

If a different person or assignment uses a different project code, create another profile and update only this value plus any schedule differences.

## Safety

Review the filled timesheet in ConnexApp before submitting. The automation should fill entries, but the final timesheet certification should remain a human decision.

## Future Ideas

Optional automated login mode:

The current bot uses manual login plus a saved browser session. A future version could add an optional login configuration for users who understand the risks and whose employer policies allow it.

Avoid hardcoding credentials directly in Python files or committing them to git. Safer options would be:

```text
.env
system keyring
password manager CLI
encrypted local config
```

If this is added later, keep it opt-in and local-only. The regular profile YAML should still focus on schedule and project settings, while sensitive login details should stay out of committed files.
