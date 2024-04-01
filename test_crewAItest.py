import unittest
from crewai import Agent

class TestCrew(unittest.TestCase):
    def test_agents(self):
        researcher = Agent(
            role='Senior Researcher',
            goal='Uncover groundbreaking technologies in {topic}',
            verbose=True,
            memory=True,
            backstory=(
                "Driven by curiosity, you're at the forefront of"
                "innovation, eager to explore and share knowledge that could change"
                "the world."
            ),
            llm=None,
            tools=None,
            allow_delegation=True
        )

        writer = Agent(
            role='Writer',
            goal='Narrate compelling tech stories about {topic}',
            verbose=True,
            memory=True,
            backstory=(
                "With a flair for simplifying complex topics, you craft"
                "engaging narratives that captivate and educate, bringing new"
                "discoveries to light in an accessible manner."
            ),
            llm=None,
            tools=None,
            allow_delegation=False
        )

        self.assertEqual(researcher.role, 'Senior Researcher')
        self.assertEqual(writer.role, 'Writer')
        self.assertEqual(researcher.goal, 'Uncover groundbreaking technologies in {topic}')
        self.assertEqual(writer.goal, 'Narrate compelling tech stories about {topic}')
        self.assertTrue(researcher.verbose)
        self.assertTrue(writer.verbose)
        self.assertTrue(researcher.memory)
        self.assertTrue(writer.memory)
        self.assertEqual(researcher.backstory, (
            "Driven by curiosity, you're at the forefront of"
            "innovation, eager to explore and share knowledge that could change"
            "the world."
        ))
        self.assertEqual(writer.backstory, (
            "With a flair for simplifying complex topics, you craft"
            "engaging narratives that captivate and educate, bringing new"
            "discoveries to light in an accessible manner."
        ))
        self.assertIsNone(researcher.llm)
        self.assertIsNone(writer.llm)
        self.assertIsNone(researcher.tools)
        self.assertIsNone(writer.tools)
        self.assertTrue(researcher.allow_delegation)
        self.assertFalse(writer.allow_delegation)

if __name__ == '__main__':
    unittest.main()