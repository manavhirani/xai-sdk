import httpx

class Completions:
    
    def __init__(self, url, headers):
        self.headers = headers
        self.url = url
    
    def create(self, **data):
        print(self.headers)
        print(self.url)
        response = httpx.post(url=self.url, headers=self.headers, json=data)
        return response
        
class Chat:
    def __init__(self, url, headers):
        self.url = url
        self.endpoints = {
            'completions': [self.url, 'completions']
        }
        self.completions = Completions(url='/'.join(self.endpoints['completions']), headers=headers)

class xAI:
    def __init__(self, base_url: httpx.URL | str | None = None, api_key: str = None) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        self.endpoints = {
            'chat':[base_url, 'chat']
        }
        self.chat = Chat(url='/'.join(self.endpoints['chat']), headers=self.headers)


if __name__ == "__main__":
    import os
    base = "https://api.x.ai/v1"
    api_key = os.getenv("XAI_API_KEY")
    client = xAI(base_url=base, api_key=api_key)
    print(client.base_url)
    print(client.api_key)
    print(client.chat.url)
    print(client.chat.completions.url)
    response = client.chat.completions.create(
        model = 'grok-beta',
        messages = [
            {
                "role": "system",
                "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
                },
            {
                "role": "user",
                "content": "What is the meaning of life, the universe, and everything?"
                }
            ]
        )
    print(response.text)