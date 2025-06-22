from crewai import Agent, Task, Crew
from tools.mongodb_tool import MongoDBTool
from tools.external_api_tool import ExternalAPITool

support_agent = Agent(
    role="Support Agent",
    goal="Respond to service queries using tools and memory",
    backstory="You are a friendly and knowledgeable assistant for a course booking platform. You handle client queries about orders, classes, and payments with clarity and efficiency.",
    tools=[MongoDBTool(), ExternalAPITool()],

    verbose=True
)

def run_support_task(prompt: str):
    task = Task(
        description=prompt,
        agent=support_agent,
        expected_output="A string or JSON with the answer to the support query."
    )
    crew = Crew(tasks=[task], agents=[support_agent])
    return crew.kickoff()  
