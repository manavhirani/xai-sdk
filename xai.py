"""Copyright (c) 2023, Your Company Name.

All rights reserved.
"""

import httpx


class Completions:
    """I am a DocString."""

    def __init__(self, url: str, headers: dict) -> None:
        """Initialize the Completions instance."""
        self.headers = headers
        self.url = url

    def create(self, **data: dict) -> httpx.Response:
        """Create stuff.

        Returns:
            httpx.Response: The response from the HTTP POST request.

        """
        return httpx.post(url=self.url, headers=self.headers, json=data, timeout=10)


class Chat:
    """Chat class docstring."""

    def __init__(self, url: str, headers: dict) -> None:
        """Initialize the Chat instance."""
        self.url = url
        self.endpoints = {
            "completions": [self.url, "completions"],
        }
        self.completions = Completions(
            url="/".join(self.endpoints["completions"]), headers=headers,
        )


class XAI:
    """Create an xAI client."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
    ) -> None:
        """Initialize the xAI client."""
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        self.endpoints = {
            "chat": [base_url, "chat"],
        }
        self.chat = Chat(url="/".join(self.endpoints["chat"]), headers=self.headers)

    def get_chat(self) -> None:
        """Chat docstring."""


if __name__ == "__main__":
    import os

    base = "https://api.x.ai/v1"
    api_key = os.getenv("XAI_API_KEY")
    client = XAI(base_url=base, api_key=api_key)
    response = client.chat.completions.create(
        model="grok-beta",
        messages=[
            {
                "role": "system",
                "content": "You are Grok, a news reporter getting live feed through X",
            },
            {
                "role": "user",
                "content": "What's the headlines for today?",
            },
        ],
    )
