class PlannerAgent:
    def create_plan(self, goal: str):
        """
        Breaks the study goal into simple steps.
        (Later we will make this LLM-powered)
        """
        plan = [
            "Read uploaded PDF",
            "Summarize important concepts",
            "Generate quiz questions",
            "Evaluate student understanding",
            "Provide feedback and next steps"
        ]
        return plan
