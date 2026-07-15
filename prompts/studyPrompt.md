Generate a Bible study for ${book} chapter ${chapter}.

Return ONLY a valid JSON object.

Do not include:

- Markdown
- ```json

  ```
- Explanations
- Introductory text
- Closing text

Use this exact schema:

{
    "summary": "One or more paragraphs.",
    "people": [],
    "places": [],
    "themes": [],
    "crossReferences": [],
    "applications": []
}
