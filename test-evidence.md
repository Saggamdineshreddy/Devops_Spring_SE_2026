# Test Evidence

Commands were run from the repository root with `python` (the `py` launcher was unavailable).

## Supplied broken configuration

```text
APP_PORT must be a whole number between 1024 and 65535
DEBUG must be exactly 'false'
DB_PASSWORD must be present and nonempty
```

Exit code: `1`

## Valid configuration

```text
Configuration accepted
```

Exit code: `0`

## Invalid port

`bad-port.env.example` uses `APP_PORT=80`.

Exit code: `1`

## Invalid debug setting

`bad-debug.env.example` uses `DEBUG=true`.

Exit code: `1`

## Missing database host

`bad-host.env.example` omits `DB_HOST`.

```text
DB_HOST must be present and nonempty
```

Exit code: `1`

No password value is printed in any error output.
