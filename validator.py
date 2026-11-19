"""Student scaffold. Implement rules from Lab 2; never print secret values."""
import sys

def validate(values):
    errors = []
    port_text = values.get("APP_PORT", "")
    try:
        port = int(port_text)
        if not 1024 <= port <= 65535:
            errors.append("APP_PORT must be a whole number between 1024 and 65535")
    except (TypeError, ValueError):
        errors.append("APP_PORT must be a whole number between 1024 and 65535")

    if values.get("DEBUG", "") != "false":
        errors.append("DEBUG must be exactly 'false'")

    if not values.get("DB_HOST", ""):
        errors.append("DB_HOST must be present and nonempty")

    if not values.get("DB_PASSWORD", ""):
        errors.append("DB_PASSWORD must be present and nonempty")

    return errors

def load(path):
    values = {}
    for line in open(path, encoding="utf8"):
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    return values

if __name__ == "__main__":
    issues = validate(load(sys.argv[1]))
    print("\n".join(issues) if issues else "Configuration accepted")
    sys.exit(bool(issues))
