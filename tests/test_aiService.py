import json

from models.studyData import StudyData


class FakeProvider:
    """
    Purpose:
        Simulates an AI provider by returning valid JSON.

    Methods:
        - generate()
    """

    def generate(self, prompt):
        """
        Returns fake AI JSON.

        Parameters:
            prompt (str): Ignored.

        Returns:
            str: JSON string.
        """

        return json.dumps({
            "summary": "God delivers Israel through Moses.",
            "people": [
                "Moses",
                "Aaron",
                "Pharaoh"
            ],
            "places": [
                "Egypt",
                "Midian"
            ],
            "themes": [
                "Deliverance",
                "Providence"
            ],
            "crossReferences": [
                "Acts 7",
                "Hebrews 11"
            ],
            "applications": [
                "Trust God's timing."
            ]
        })


class TestAIService:
    """
    Purpose:
        Tests AI JSON conversion.

    Methods:
        - testStudyDataFromJson()
    """

    def testStudyDataFromJson(self):
        """
        Verifies JSON is correctly converted into a StudyData object.

        Parameters:
            None

        Returns:
            None
        """

        provider = FakeProvider()

        response = provider.generate("ignored")

        data = json.loads(response)

        study = StudyData(
            summary=data["summary"],
            people=data["people"],
            places=data["places"],
            themes=data["themes"],
            crossReferences=data["crossReferences"],
            applications=data["applications"]
        )

        assert study.summary == "God delivers Israel through Moses."

        assert study.people == [
            "Moses",
            "Aaron",
            "Pharaoh"
        ]

        assert study.places == [
            "Egypt",
            "Midian"
        ]

        assert study.themes == [
            "Deliverance",
            "Providence"
        ]

        assert study.crossReferences == [
            "Acts 7",
            "Hebrews 11"
        ]

        assert study.applications == [
            "Trust God's timing."
        ]