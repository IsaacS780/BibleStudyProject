"""
fakeStudyData.py

Purpose:
    Creates reusable fake AI study data for unit tests.

Functions:
    - createFakeStudyData()
"""

from models.studyData import StudyData


def createFakeStudyData():
    """
    Creates fake study data for testing.

    Parameters: None

    Returns:
        StudyData: Fake AI study data.
    """

    return StudyData(
        summary="God delivers Israel through Moses.",
        people=[
            "Moses",
            "Aaron",
            "Pharaoh"
        ],
        places=[
            "Egypt"
        ],
        themes=[
            "Deliverance",
            "Faith"
        ],
        crossReferences=[
            "Hebrews 11",
            "Acts 7"
        ],
        applications=[
            "Trust God's timing."
        ]
    )