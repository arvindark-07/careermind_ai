from groq import AsyncGroq

from .config import GROQ_API_KEY, GROQ_MODEL


async def generate_answer(
    message: str,
    profile: str,
    memories: list,
    history: list,
):
    if not GROQ_API_KEY:
        return (
            "Groq API key is not configured. "
            "Please add GROQ_API_KEY to your .env file."
        )

    memory_text = "\n".join(
        f"- {item}" for item in memories
    ) if memories else "No long-term memories found."

    history_text = "\n".join(
        f"{item.get('role', 'user')}: {item.get('content', '')}"
        for item in history[-10:]
    ) if history else "No previous conversation."

    prompt = f"""
You are CareerMind AI, a personalized career assistant.

Your job is to give useful career guidance based on the user's
resume, long-term memories, and previous conversations.

USER RESUME / PROFILE:
{profile}

LONG-TERM MEMORY:
{memory_text}

PREVIOUS CONVERSATION:
{history_text}

CURRENT USER MESSAGE:
{message}

Instructions:
- Give personalized career advice.
- Use the user's actual skills, projects, education, and goals when available.
- Do not invent qualifications or experience.
- Clearly identify skill gaps when relevant.
- Give practical next steps.
- Keep the answer easy to understand.
- If the user asks about internships, connect the advice to their current profile.
"""

    client = AsyncGroq(api_key=GROQ_API_KEY)

    response = await client.chat.completions.create(
        model=GROQ_MODEL,
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are CareerMind AI, "
                    "a personalized long-term career assistant."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.choices[0].message.content