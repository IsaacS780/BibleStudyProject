from models.chapter import Chapter
from tests.fakeStudyData import createFakeStudyData


class TestStudyService:
    """
    Purpose:
        Tests Chapter creation using fake AI data.

    Methods:
        - testChapterCreation()
    """

    def testChapterCreation(self):
        """
        Verifies a Chapter stores the StudyData object correctly.

        Parameters:
            None

        Returns:
            None
        """

        studyData = createFakeStudyData()

        chapter = Chapter(
            "Exodus",
            2,
            studyData
        )

        assert chapter.book == "Exodus"
        assert chapter.chapterNumber == 2

        assert chapter.studyData.summary == "God delivers Israel through Moses."

        assert "Moses" in chapter.studyData.people

        assert "Deliverance" in chapter.studyData.themes

        assert "Egypt" in chapter.studyData.places