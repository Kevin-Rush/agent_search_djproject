# Information flow:

## User Input:

Ask for all API keys required:
- OpenAI
- Scarper (or FireCrawl)

n fields to build the user prompt:
- Document type
- Audience
- Purpose
- Additional information
- File name

Display the user prompt to the user for validation
- If the user is satisfied with the prompt, proceed to subsections
- If not, ask for the user to edit prompt directly

1. User prompt comes in that gives information about the type of file to be generated.

Breaking down the prompt:
- Is the document type iden
- Is it vague and requires more information?

Need to extract:
1. Document type (e.g. business development, marketing, business analysis, etc.)
2. Additional information about the document (e.g. target audience, purpose, etc.)

Need to generate (i.e., decide):
1. File name (e.g. business_dev_context.ppptx)
2. What the sub sections for this document will be (e.g. Introduction, Market Analysis, Competitor Analysis, Conclusion etc.)