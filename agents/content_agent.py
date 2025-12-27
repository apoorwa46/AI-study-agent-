class ContentAgent:
    def __init__(self, model):
        self.model = model

    def summarize(self, text: str):
        """
        Summarizes extracted PDF text for a student.
        """
        prompt = f"""
        You are a study assistant.
        Summarize the following content clearly for a beginner student:

        {text}
        """

        response = self.model.generate_content(prompt)
        return response.text
