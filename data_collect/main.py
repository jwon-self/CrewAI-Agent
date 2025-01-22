"""
나중에 클래스로 할게요
"""

# import Agent form crewai library
from crewai import Agent

# import Tasks from crewai library
from crewai import Task

# import API_KEY from config
from config import API_KEY


# Agent 제작
finder = Agent(
    role='data finder', # 역할
    goal="""
    여러 인터넷 자료 중 요청한 내용의 자료를 찾습니다.
    """, # 목적
    backstory="""
    당신은 상황에 맞는 데이터를 판단할 수 있습니다.
    여러 자료를 수집하여 다른 AI들과 협업할 수 있도록 노력해보세요.
    주제에 관련된 어떤 자료든지 가능하니 **최대한 있어보이는 자료**를 가져오세요.
    """, # 뒷배경 이야기
c
)

filter = Agent(
    role='data filter', # 도구(서폿어ㅣㅁ)
    goal="""
    수집된 데이터를 필터링합니다.
    가장 완벽하고 좋은 데이터만 분류하여 최적의 데이터를 수집할 수 있도록 합시다.
    필요하다면 추가적인 자료 검색도 가능합니다.
    """,
    backstory="""
    당신은 상황에 맞는 데이터를 꼼꼼히 확인하여 정확한 데이터를 분류할 수 있습니다.
    당신은 매우 꼼꼼하게 자료를 확인하는 최종 분석가 역할을 합니다.
    """,  # 뒷배경 이야기
    verbose=True
)

research_data = Task(
    description="""
    du
    """,
    agent='',
    expected_output=
)
filter_data = Task()