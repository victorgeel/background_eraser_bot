from environs import Env

# environs kitapxanasınan paydalanıw
env = Env()
env.read_env()

# .env fayl ishinen tómendegilerdi oqıymız
BOT_TOKEN = env.str("1991353536:AAHZ-YIQfg5g87O9jC4XfrgUag68zDKwclw")  # bot token
ADMINS = env.list("ADMINS")  # adminler listi
IP = env.str("80")  # xosting ip adress
