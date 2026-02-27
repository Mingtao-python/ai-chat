import os, sys
import requests, time

times = input('type the maximum dialog of chat\nbetween 5-15\ngive me money if you want more: ').strip()

if times.isdigit():
    times = int(times)
    if not (5 <= times <= 15):
        print('out of range\nturns set to 12')
        times = 12
else:
    print('wrong input\nturns set to 12')
    times = 12

URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = input('API key please>').strip()
if not API_KEY:
    print('API key cannot be empty')
    time.sleep(5)
    sys.exit()

messages = []

form = input("Style for the assistant (Eg: smart/professional). Press Enter for default: ").strip()
if form != '':
    messages.append({"role": "system", "content": f"You must ALWAYS respond in a {form} style."})

def trim_history(max_turns):
    global messages
    if len(messages) > max_turns:
        print("max turns reached. Refreshing...")
        os.system('cls')
        system_prompts = [m for m in messages if m["role"] == "system"]
        if len(system_prompts) > 0:
            messages = [system_prompts[0]]
        else:
            messages = []
        
def ask(q):
    global messages
    global times
    q = q.strip()
    if not q:
        return "(empty input, not sent)"
    messages.append({"role": "user", "content": q})
    trim_history(times)
    try:
        r = requests.post(URL, json={"model": "llama-3.1-8b-instant", "messages": messages}, headers={"Authorization": f"Bearer {API_KEY}"}, timeout = 10)
        if not int(r.status_code) == 200:
            return f"❌ Unable to access HTTP.The code is: {r.status_code}"  
        data = r.json()
        if "choices" not in data or not data["choices"]:
            return "❌ Bad responce by the AI model."
        reply = data["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply
    except requests.exceptions.Timeout:
        return "❌ Timeout. Please try again."
    except requests.exceptions.RequestException as e:
        return f"❌ Network error: {e}"
    except ValueError:
        return "❌ Response not valid."
print(r'''
Chat started. Type e/exit/quit to exit.
''')

while True:
    user_text = input("you> ").strip()
    if user_text.lower() in ("e", "exit", "quit"):
        break
    print("AI>", ask(user_text))
print('-----GOODBYE------')
time.sleep(0.5)
print('         --                --         ')
time.sleep(0.5)
print('     --     --       --       --  ')
time.sleep(0.5)
print()
time.sleep(0.5)
print('   ----                      ----')
time.sleep(0.5)
print('         ---------------      ')
time.sleep(0.5)
print(':)')
time.sleep(5)
sys.exit()
