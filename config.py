import os
import ast

BOT_TOKEN = os.environ.get("BOT_TOKEN")
GROUP_ID = int(os.environ.get("GROUP_ID"))
MANAGER_IDS = ast.literal_eval(os.environ.get("MANAGER_IDS"))
