Each class has exactly one responsibility.

Application – Runs the application.
StudyService – Creates a Bible study.
AIClient – Coordinates AI requests.
PromptBuilder – Builds prompts.
AIProviderFactory – Chooses the configured provider.
GeminiProvider/OpenAIProvider/etc. – Talks to one AI service.

ReferenceParser → understands syntax and formatting.
BookManager → understands Bible books.
Book → understands properties of a single book.

Current pipeline:
Application
    ↓
StudyService
    ↓
AIService
    ├── PromptBuilder
    └── AIProviderFactory
             ↓
       GeminiProvider


AI pipeline:

Load a prompt template.
Fill in the Bible reference.
Send it to Gemini.
Return the generated study.
Keep everything provider-independent.


StudyService
      |
      +--> AIService
             |
             +--> ProviderFactory
                    |
                    +--> GeminiProvider

General application outline
User
 │
 ▼
ReferenceParser
    ✓ Tested
 │
 ▼
BookManager
    ✓ Tested
 │
 ▼
BibleReference
 │
 ▼
StudyService
 │
 ▼
AIService
 │
 ▼
Provider

AI PIPELINE:
Gemini
   │
   ▼
Raw AI Response
   │
   ▼
AIService
   │
   ▼
StudyData
   │
   ▼
StudyService