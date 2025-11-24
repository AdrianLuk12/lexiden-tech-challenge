"""
Conversation management service.
Handles conversation history and document state.
"""
from typing import Dict, List, Optional
import uuid


class ConversationService:
    """Service for managing conversations and document state."""

    def __init__(self):
        """Initialize conversation storage."""
        # In-memory storage for conversations and documents
        self._conversations: Dict[str, List[Dict]] = {}
        # Store both PDF bytes and document data
        self._documents: Dict[str, Dict] = {}  # {conversation_id: {pdf: bytes, data: dict}}

    def create_conversation(self) -> str:
        """
        Create a new conversation.

        Returns:
            Conversation ID
        """
        conversation_id = str(uuid.uuid4())
        self._conversations[conversation_id] = []
        return conversation_id

    def add_message(
        self,
        conversation_id: str,
        role: str,
        content: str
    ) -> None:
        """
        Add a message to conversation history.

        Args:
            conversation_id: Conversation ID
            role: Message role ('user' or 'model')
            content: Message content
        """
        if conversation_id not in self._conversations:
            self._conversations[conversation_id] = []

        self._conversations[conversation_id].append({
            'role': role,
            'parts': [content]
        })

    def get_history(self, conversation_id: str) -> List[Dict]:
        """
        Get conversation history.

        Args:
            conversation_id: Conversation ID

        Returns:
            List of messages in conversation
        """
        return self._conversations.get(conversation_id, [])

    def set_document(self, conversation_id: str, pdf_bytes: bytes, doc_data: Dict) -> None:
        """
        Store document for a conversation.

        Args:
            conversation_id: Conversation ID
            pdf_bytes: PDF document as bytes
            doc_data: Document data dictionary for editing
        """
        self._documents[conversation_id] = {
            'pdf': pdf_bytes,
            'data': doc_data
        }

    def get_document(self, conversation_id: str) -> Optional[Dict]:
        """
        Get document for a conversation.

        Args:
            conversation_id: Conversation ID

        Returns:
            Dictionary with 'pdf' (bytes) and 'data' (dict) if exists, None otherwise
        """
        return self._documents.get(conversation_id)

    def get_document_data(self, conversation_id: str) -> Optional[Dict]:
        """
        Get just the document data (not PDF bytes) for a conversation.

        Args:
            conversation_id: Conversation ID

        Returns:
            Document data dictionary if exists, None otherwise
        """
        doc = self._documents.get(conversation_id)
        return doc['data'] if doc else None

    def conversation_exists(self, conversation_id: str) -> bool:
        """
        Check if conversation exists.

        Args:
            conversation_id: Conversation ID

        Returns:
            True if conversation exists, False otherwise
        """
        return conversation_id in self._conversations

    def delete_conversation(self, conversation_id: str) -> bool:
        """
        Delete a conversation and its associated data.

        Args:
            conversation_id: Conversation ID

        Returns:
            True if deleted, False if not found
        """
        if conversation_id in self._conversations:
            del self._conversations[conversation_id]
            if conversation_id in self._documents:
                del self._documents[conversation_id]
            return True
        return False

    def get_conversation_data(self, conversation_id: str) -> Optional[Dict]:
        """
        Get full conversation data including messages and document.

        Args:
            conversation_id: Conversation ID

        Returns:
            Dictionary with conversation data or None if not found
        """
        if not self.conversation_exists(conversation_id):
            return None

        return {
            'conversation_id': conversation_id,
            'messages': self.get_history(conversation_id),
            'document': self.get_document(conversation_id)
        }


# Global conversation service instance
conversation_service = ConversationService()
