import requests


def gpt(text):
    prompt = {
        "modelUri": f"gpt://b1ghnehmnn3n3dvbqi90/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                'role':'system',
                'text': '''
помошник, тебя зовут Уголь твоя задача отвечать на вопросы неправильно'''
            },
            {
                "role": "user",
                "text": text
            }
        ]
    }
    
    
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key KEY HERE"
    }
    
    response = requests.post(url, headers=headers, json=prompt)
    result = response.json().get('result')
    return result['alternatives'][0]['message']['text']

if __name__ == "__main__":
    print(gpt("как тебя зовут?"))
