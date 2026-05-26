from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import Config

def get_transcript_and_split(video_id: str):
    """Fetches YouTube transcript and splits it into chunks."""
    try:
        # NEW SYNTAX for the updated youtube-transcript-api
        api = YouTubeTranscriptApi()
        fetched_transcript = api.fetch(video_id, languages=["hi", "en"])
        
        # Extract text (using a try/except to handle the new snippet object format)
        try:
            transcript = " ".join(snippet.text for snippet in fetched_transcript)
        except AttributeError:
            # Fallback just in case it returns the raw dictionary format
            transcript = " ".join(chunk["text"] for chunk in fetched_transcript)
        
        # Split text
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE, 
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        chunks = splitter.create_documents([transcript])
        return chunks
        
    except TranscriptsDisabled:
        raise ValueError("No captions available for this video.")
    except Exception as e:
        raise ValueError(f"Error fetching transcript: {e}")