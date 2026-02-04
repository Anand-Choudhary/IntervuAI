from typing import Literal
InterviewTopic = Literal["url_shortener", "whatsapp", "uber"]
InterviewSection = Literal[
    "requirements",
    "capacity_estimation", 
    "high_level_architecture",
    "api_design",
    "database_schema",
    "scaling_strategy",
    "trade_offs"
]
Difficulty = Literal["easy", "medium", "hard"]
Recommendation = Literal["STRONG_HIRE", "HIRE", "NO_HIRE", "STRONG_NO_HIRE"]
