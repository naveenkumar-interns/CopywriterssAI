import os
from crewai import Agent, Task, Crew, LLM
from crewai.tools import tool

# Set API Key for LLM
os.environ["GEMINI_API_KEY"] = "AIzaSyBPuJyHX0rcQV7DneUbAvgJT0BUobRwCS4"

# Define LLM
my_llm = LLM(
    model='gemini/gemini-1.5-flash',
    api_key=os.environ["GEMINI_API_KEY"]
)

# Define the Agents
researcher = Agent(
    role="Market Researcher",
    goal="Analyze the product and audience to extract key selling points.",
    backstory="An expert in market trends and consumer behavior analysis.",
    verbose=True,
    llm=my_llm
)

copywriter = Agent(
    role="Creative Copywriter",
    goal="Craft compelling AIDA copy using the given inputs and insights from the researcher.",
    backstory="An experienced copywriter specializing in persuasive marketing techniques.",
    verbose=True,
    llm=my_llm
)
editor = Agent(
    role="Senior Editor",
    goal="Refine and enhance the copy for maximum impact and readability.",
    backstory="A skilled editor with a keen eye for detail and engaging language.",
    verbose=True,
    llm=my_llm
)

# Define the function to generate QUEST marketing copy

def generate_aida(Creativity, Product_Name, Audience, Product_Description, Tone_of_Voice):
    # Define the Tasks
    research_task = Task(
        description=f"Analyze the product description and audience to extract key selling points. \n"
                    f"Product Name: {Product_Name}, Audience: {Audience}, \n"
                    f"Product Description: {Product_Description}",
        expected_output="A list of compelling product benefits and market insights.",
        agent=researcher
    )

    aida_task = Task(
        description=f"Generate a persuasive marketing copy using the AIDA (Attention, Interest, Desire, Action) framework. \n"
                    f"Use the following product insights: {Product_Description}, creativity level: {Creativity}, and tone of voice: {Tone_of_Voice}",
        expected_output="A well-structured marketing copy using the AIDA framework.",
        agent=copywriter,
        depends_on=[research_task]
    )

    edit_task = Task(
        description="Refine and enhance the AIDA (Attention, Interest, Desire, Action) copy for clarity, persuasion, and brand alignment.",
        expected_output="A polished and engaging AIDA marketing copy.",
        agent=editor,
        depends_on=[aida_task]
    )

    parse_task = Task(
        description="Parse and correct the final AIDA(Attention, Interest, Desire, Action) marketing copy for any errors or inconsistencies.",
        expected_output="A final, error-free AIDA (Attention, Interest, Desire, Action) marketing copy.",
        agent=editor,
        depends_on=[edit_task]
    )
    
    # Define the Crew
    crew = Crew(
        agents=[researcher, copywriter, editor],
        tasks=[research_task, aida_task, edit_task, parse_task],
        verbose=True
    )
    
    # Running the Crew
    result = crew.kickoff({})

    return result.raw
