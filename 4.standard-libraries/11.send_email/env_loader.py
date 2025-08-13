
def load_env():
    env_dict = {}
    try:
        with open('.env', 'r', encoding='utf-8') as env_file:
            for line in env_file:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', maxsplit=1)
                    env_dict[key.strip()] = value.strip()
    except FileNotFoundError:
        print("Warning: .env file not found")
    return env_dict
