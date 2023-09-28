from django.core.management import utils


key = utils.get_random_secret_key()

with open(".env", "w") as env_file:
    env_file.write(f"SECRET_KEY={key}\nDEBUG=True")
