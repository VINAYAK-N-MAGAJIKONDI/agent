from crewai import Agent, Task, Crew, LLM
from tools.analytics_tool import DashboardAnalyticsTool



llm = LLM(
              model='gemini/gemini-2.0-flash-lite',
              api_key="AIzaSyBU3bBx1G1We7JUgaKJ_yoQZxbuVBJGMOY"
            )

dashboard_agent = Agent(
    role="Dashboard Agent",
    goal="Provide business analytics on revenue, clients, courses, and attendance.",
    backstory=(
        "You're an expert analytics assistant that helps business owners understand trends in "
        "client activity, revenue generation, course popularity, and attendance stats."
    ),
    tools=[DashboardAnalyticsTool()],
    verbose=True,
    llm= llm,

)


def run_dashboard_task(prompt: str):
    task = Task(
        description=prompt,
        agent=dashboard_agent,
        expected_output= "value of the result"
        
    )
    crew = Crew(
        agents=[dashboard_agent],
        tasks=[task]
    )
    return crew.kickoff().raw  

