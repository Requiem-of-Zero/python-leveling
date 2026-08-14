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

Run headless with a profile that has login credentials:

```bash
python main.py --profile local --headless
```

Show available options and the current ISO week:

```bash
python main.py --help
```

## Login

By default, leave login fields empty and log into ConnexApp normally in the browser window. Playwright can reuse the local browser session on later runs through `browser-data/`.

Optional automated login can be enabled locally by filling both values in a profile:

```yaml
defaults:
  login:
    email: "person@example.com"
    password: "local-password"
```

If either value is blank or missing, the bot uses manual login. If automated login does not complete, the bot falls back to manual login.

Do not commit real credentials to git.

Headless mode:

```bash
python main.py --profile local --headless
```

`--headless` only takes effect when the selected profile has both `defaults.login.email` and `defaults.login.password`. Without credentials, the bot opens a visible browser so manual login can work.

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

For profiles that contain real login credentials, prefer an ignored local filename:

```bash
cp profiles/example.yaml profiles/local.yaml
python main.py --profile local
```

`profiles/local*.yaml` and `profiles/private*.yaml` are ignored by git.

## Profile Sections

`name`

Human-readable profile name printed in the review summary.

`portal_url`

ConnexApp URL. Usually:

```yaml
portal_url: "https://connexapp.dayzim.com/web/"
```

`defaults.login`

Optional local login configuration.

Manual/session login:

```yaml
defaults:
  login:
    email: ""
    password: ""
```

Automated login:

```yaml
defaults:
  login:
    email: "person@example.com"
    password: "local-password"
```

Keep this local to the machine using the bot.

Recommended for real credentials:

```text
profiles/local.yaml
profiles/private-your-name.yaml
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

Safer credential storage:

The current optional automated login mode reads credentials from the local YAML profile. Future versions could support safer storage options:

```text
.env
system keyring
password manager CLI
encrypted local config
```
