# Applied AI System: Agentic Music Recommender

## Base Project Summary
This project is an extension of my Module 3 Music Recommender Simulation. The original project was a CLI-based content-based filtering system that scored songs based on genre, mood, and energy, and returned a ranked list to the user.

## System Summary
This extended version transforms the basic recommender into an **Agentic Recommender with Reliability Guardrails**. Instead of just ranking songs, the system acts as an agent: it calculates scores, applies a guardrail to prevent "filter bubbles" (by ensuring no two songs by the same artist appear in the top recommendations), calculates a confidence score based on how well the songs matched the user's profile, and logs its decision-making process.

## Architecture Overview
The system flows through an agentic loop:
1. **Input:** User preferences (genre, mood, energy).
2. **Agent Loop:** The system scores all songs and ranks them.
3. **Guardrail:** Before finalizing the top 5, the agent checks the artist list. If an artist is duplicated, it skips the song and grabs the next highest.
4. **Output:** A diverse playlist with a confidence score (0-100%).

## Setup Instructions
1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python -m src.main`

## Sample Interactions

**Input 1: High-Energy Pop Fan**
```text
INFO: Agent started. Generating playlist for pop.
INFO: Agent finished. Playlist confidence: 92.5%

--- Agentic Output for pop fan ---
1. Sunrise City by Neon Echo (Score: 3.82)
2. Gym Hero by Max Pulse (Score: 3.78)
3. Rooftop Lights by Indigo Parade (Score: 3.51)

System Confidence Score: 92.5%
