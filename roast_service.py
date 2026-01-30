"""
Service for generating music taste roasts using LLM
"""
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from config.settings import settings
from models.spotify_models import UserData


class RoastService:
    """Handles generation of humorous music taste roasts"""
    
    def __init__(self):
        """Initialize the roast service with LLM model"""
        self.model = ChatOpenAI(model=settings.OPENAI_MODEL)
        self.parser = StrOutputParser()
        self.chain = self.model | self.parser
    
    @staticmethod
    def _build_prompt(user_data: UserData) -> str:
        """
        Build the prompt for the LLM to generate a roast
        
        Args:
            user_data: User's Spotify data
            
        Returns:
            str: Formatted prompt
        """
        tracks = "\n".join(
            f"- {t.track} by {', '.join(t.artists)}"
            for t in user_data.top_tracks
        )
        
        artists = "\n".join(
            f"- {a.artist} (genres: {', '.join(a.genres)})"
            for a in user_data.top_artists
        )
        
        # Extract first name if full name is provided
        first_name = user_data.user_name.split()[0] if user_data.user_name else "friend"
        
        return f"""
You are a witty, sarcastic music critic with a playful personality.

Your task is to roast {first_name}'s music taste in a humorous but good-natured way.

Top tracks:
{tracks}

Top artists:
{artists}

Rules:
- Be funny and creative, not mean-spirited or offensive
- Avoid profanity
- Make observations about their music taste (genre choices, artist popularity, etc.)
- Use a conversational, human tone
- Keep the roast between 100-150 words
- End on a slightly positive or self-aware note

Generate the roast now:
"""
    
    def generate_roast(self, user_data: UserData) -> str:
        """
        Generate a humorous roast based on user's music taste
        
        Args:
            user_data: User's Spotify data
            
        Returns:
            str: Generated roast text
        """
        prompt = self._build_prompt(user_data)
        roast = self.chain.invoke(prompt)
        return roast.strip()
