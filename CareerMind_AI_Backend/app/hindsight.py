import httpx

from .config import (
    HINDSIGHT_API_KEY,
    HINDSIGHT_BASE_URL,
    HINDSIGHT_BANK_ID,
)


class HindsightMemory:

    def __init__(self):
        self.enabled = bool(HINDSIGHT_API_KEY)

        self.base_url = (
            HINDSIGHT_BASE_URL.rstrip("/")
        )

        self.bank_id = HINDSIGHT_BANK_ID

        self.headers = {
            "Authorization": f"Bearer {HINDSIGHT_API_KEY}",
            "Content-Type": "application/json",
        }

    async def retain(
        self,
        user_id: int,
        content: str,
        context: str = "CareerMind user memory",
    ):

        if not self.enabled:
            return {
                "stored": False,
                "provider": "sqlite_fallback",
            }

        url = (
            f"{self.base_url}"
            f"/v1/default/banks/"
            f"{self.bank_id}/memories"
        )

        payload = {
            "items": [
                {
                    "content": content,
                    "context": context,
                    "metadata": {
                        "user_id": str(user_id),
                        "application": "CareerMind AI",
                    },
                }
            ]
        }

        try:

            async with httpx.AsyncClient(
                timeout=30
            ) as client:

                response = await client.post(
                    url,
                    json=payload,
                    headers=self.headers,
                )

                response.raise_for_status()

                return {
                    "stored": True,
                    "provider": "hindsight",
                    "data": response.json(),
                }

        except Exception as exc:

            return {
                "stored": False,
                "provider": "sqlite_fallback",
                "error": str(exc),
            }

    async def recall(
        self,
        user_id: int,
        query: str,
    ):

        if not self.enabled:
            return []

        url = (
            f"{self.base_url}"
            f"/v1/default/banks/"
            f"{self.bank_id}/memories/recall"
        )

        payload = {
            "query": query,
            "budget": "mid",
            "max_tokens": 4096,
        }

        try:

            async with httpx.AsyncClient(
                timeout=30
            ) as client:

                response = await client.post(
                    url,
                    json=payload,
                    headers=self.headers,
                )

                response.raise_for_status()

                data = response.json()

                results = data.get(
                    "results",
                    []
                )

                memories = []

                for item in results:

                    if isinstance(item, dict):

                        text = (
                            item.get("text")
                            or item.get("content")
                            or item.get("memory")
                        )

                        if text:
                            memories.append(text)

                    elif isinstance(item, str):

                        memories.append(item)

                return memories

        except Exception:
            return []