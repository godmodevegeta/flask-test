import os
from dotenv import load_dotenv
from supabase import create_client, Client

# load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
test: str = "just checking"
# supabase: Client = create_client(url, key)

print("SUPABASE-URL: ", url)
print("SUPABASE-KEY: ", key)
print("TEST: ", test)

