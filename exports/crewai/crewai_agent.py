from crewai import Agent
def create_agent():
    return Agent(role='GitAMLWatch', goal='Autonomous Anti-Money Laundering (AML), Transaction Velocity & SAR Filing Risk Agent', backstory='Autonomous agent', verbose=True)
