# 🎧 Model Card: Applied AI System

## 1. Model Name  
Agentic Music Curator 2.0

## 2. Intended Use  
This system is designed to demonstrate how guardrails and agentic reasoning can improve a basic recommendation engine by preventing filter bubbles and providing confidence scores. It is for educational purposes.

## 3. How the Model Works  
The model scores songs based on genre (+2.0), mood (+1.0), and energy similarity (+1.0). It then acts as an agent by filtering out duplicate artists (the guardrail) before presenting the final playlist and a calculated confidence percentage.

## 4. Limitations and Bias
The dataset is still limited to 16 songs, so the diversity guardrail sometimes results in playlists with fewer than 5 songs. Additionally, the confidence score is simply a normalized average of the math scores, not a deep semantic understanding of whether the user actually likes the music.

## 5. Evaluation
I evaluated the system by writing a pytest that intentionally forced the agent to evaluate two songs by the same artist. The test proved the guardrail works by dropping the duplicate and falling back to a different artist.

## 6. AI Collaboration
- **Accepted Suggestion:** The AI suggested using a `set()` to track `seen_artists` in the guardrail loop. This was highly efficient (O(1) lookup time) and clean to implement.
- **Rejected Suggestion:** The AI initially suggested calling the OpenAI API to get the confidence score. I rejected this because it would make the script reliant on an internet connection and API keys, violating the requirement for reproducible execution without external dependencies.
