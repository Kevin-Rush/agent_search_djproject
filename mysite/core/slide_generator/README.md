# Business Document Generation

## User Input:

Ask for all config information required:
- OpenAI API Key
- Model Type (Note can give cost expectations per model)
- Serper (or FireCrawl ... TBD) API Key

n fields to build the user prompt:
- Document type (business development, business analysis, marketing, etc.)
-- Note the actual document will be ppxt by default, other file types will be added in the future
- Audience
- Purpose
- Additional information
- File name

Display the user prompt to the user for validation
- If the user is satisfied with the prompt, proceed to sections
- If not, ask for the user to edit prompt directly

## Section Generation

**Gen 1:** Based on the user prompt, propose sections to be generated

### Processing 
Display all sections in an editable text field for the user to remove, add, or edit the sections as necessary

Create a JSON file with the following structure:

{
    "document": {
        "metadata": {
            "type": "",
            "audience": "",
            "purpose": "",
            "file_name": ""
        },
        "user_prompt": "",
        "sections": [
            "section1",
            "section2",
            "section3",
        ]
    }
}

Once the sections are approved, the next phase is content generation. My strategy for this will be to generate an entire body of text filling in the information needed per section. It will be saved in the following JSON.

{
    "content": {
        "section1": {
            "title": "",
            "content": "",
        },
        "section2": {
            "title": "",
            "content": "",
            "notes": "",
        },
        "section3": {
            "title": "",
            "content": "",
        }
    }
}