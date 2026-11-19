# Findings

## Defects in `messy.env`

- `APP_PORT=hello` has an invalid data type; `APP_PORT` must be a whole number.
- `DEBUG=true` violates the deployment policy; `DEBUG` must be exactly `false`.
- `DB_PASSWORD=` is present but empty.
- `dbhost=localhost` is a legacy or differently named key. It does not satisfy the required `DB_HOST=db` setting.

## Required validation rules

- `APP_PORT`: required whole number from 1024 through 65535, inclusive.
- `DEBUG`: required and exactly `false`.
- `DB_HOST`: required and nonempty.
- `DB_PASSWORD`: required and nonempty. Error output must name the key without revealing its value.
