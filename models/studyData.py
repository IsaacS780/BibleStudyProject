"""
studyData.py

Purpose:
    Represents AI-generated Bible study content.

Primary Class:
    StudyData
"""


class StudyData:
    """
    Purpose:
        Stores AI-generated study information for a Bible chapter.

    Current Responsibilities:
        - Store chapter summary.
        - Store people.
        - Store places.
        - Store themes.
        - Store cross references.
        - Store applications.

    Future Responsibilities:
        - Store timelines.
        - Store maps.
        - Store word studies.

    Methods:
        - fromDictionary()
        - toDictionary()
    """

    REQUIRED_FIELDS = [
    "summary",
    "people",
    "places",
    "themes",
    "crossReferences",
    "applications"
    ]
    
    def __init__(
        self,
        summary,
        people=None,
        places=None,
        themes=None,
        crossReferences=None,
        applications=None
    ):
        """
        Creates a StudyData object.

        Parameters:
            summary (str): Chapter summary.
            people (list): People mentioned.
            places (list): Places mentioned.
            themes (list): Major themes.
            crossReferences (list): Related passages.
            applications (list): Practical applications.

        Returns:
            None
        """

        self.summary = summary
        self.people = people or []
        self.places = places or []
        self.themes = themes or []
        self.crossReferences = crossReferences or []
        self.applications = applications or []

    @classmethod
    def validateDictionary(cls, data):
        """
        Validates AI-generated study data.

        Parameters:
            data (dict): Parsed AI response.

        Returns: None

        Raises: ValueError: If required fields are missing.
        """

        for field in cls.REQUIRED_FIELDS:
            if field not in data:
                raise ValueError(f"AI response missing required field '{field}'.")

    @classmethod
    def fromDictionary(cls, data):
        """
        Creates a StudyData object from AI JSON.
        """

        return cls(
            summary=data.get("summary", ""),
            people=data.get("people", []),
            places=data.get("places", []),
            themes=data.get("themes", []),
            crossReferences=data.get("crossReferences", []),
            applications=data.get("applications", [])
        )
    
    def toDictionary(self):
        """
        Converts the StudyData object into a dictionary.

        Parameters: None

        Returns:
            dict: Serializable study data.
        """

        return {
            "summary": self.summary,
            "people": self.people,
            "places": self.places,
            "themes": self.themes,
            "crossReferences": self.crossReferences,
            "applications": self.applications
        }