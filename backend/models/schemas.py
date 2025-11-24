"""
Function schemas and data models for Gemini function calling.
"""

# Define function declarations for Gemini
FUNCTION_TOOLS = [
    {
        "function_declarations": [
            {
                "name": "extract_information",
                "description": "Extract structured information from the conversation for legal document generation. Use this when you need to gather specific details like names, dates, positions, or other document parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "document_type": {
                            "type": "string",
                            "description": "Type of legal document (e.g., 'director_appointment', 'nda', 'employment_agreement')"
                        },
                        "extracted_data": {
                            "type": "object",
                            "description": "Key-value pairs of extracted information",
                            "properties": {}
                        },
                        "missing_fields": {
                            "type": "array",
                            "description": "List of required fields that are still missing",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["document_type", "extracted_data"]
                }
            },
            {
                "name": "generate_document",
                "description": "Generate a complete legal document based on extracted information. Use this only when you have all required information to create a comprehensive document.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "document_type": {
                            "type": "string",
                            "description": "Type of legal document to generate"
                        },
                        "document_data": {
                            "type": "object",
                            "description": "All data needed to generate the document"
                        }
                    },
                    "required": ["document_type", "document_data"]
                }
            },
            {
                "name": "apply_edits",
                "description": "Apply specific edits to an existing document based on user requests. Use this when the user wants to modify, update, or change part of an already generated document.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "edit_type": {
                            "type": "string",
                            "description": "Type of edit (e.g., 'update_field', 'replace_section', 'add_clause')"
                        },
                        "field_name": {
                            "type": "string",
                            "description": "Name of the field or section to edit"
                        },
                        "new_value": {
                            "type": "string",
                            "description": "New value or content to apply"
                        },
                        "reason": {
                            "type": "string",
                            "description": "Brief explanation of the edit"
                        }
                    },
                    "required": ["edit_type", "field_name", "new_value"]
                }
            }
        ]
    }
]
