class QuizAgent:
    def __init__(self, model):
        self.model = model

    def generate_quiz(self, summary: str):
        """
        Generates quiz questions from summary.
        """
        prompt = f"""
        Create 5 quiz questions (with answers) from the following summary:

        {summary}
        """

        response = self.model.generate_content(prompt)
        return response.text
