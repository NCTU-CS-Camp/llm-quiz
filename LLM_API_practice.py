import requests

GEMINI_API_KEY = "-----申請 Gemini API key 後填入-----"        

def call_gemini(prompt: str) -> str:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/____1____:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.____2____(url, headers=headers, json=data)
    response.raise_for_status()
    res_json = response.json()
    return res_json["candidates"][0]["content"]["parts"][0]["text"]

if __name__ == "__main__":
    user_prompt = input("請輸入要送給 Gemini 的訊息：")
    reply = call_gemini(user_prompt.strip())
    print("Gemini 回覆：")
    print(reply)
