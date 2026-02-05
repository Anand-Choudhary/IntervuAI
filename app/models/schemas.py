from pydantic import BaseModel, Field
from typing import Literal, Optional, List, Dict
from datetime import datetime
from uuid import UUID


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


class StartInterviewResponse(BaseModel):
    """Response after starting interview."""
    session_id: UUID
    topic: InterviewTopic
    current_section: InterviewSection
    message: str


class QuestionResponse(BaseModel):
    """Response containing next question."""
    question: str
    section: InterviewSection
    question_number: int
    difficulty: Optional[Difficulty] = None


class AnswerSubmissionResponse(BaseModel):
    """Response after submitting answer."""
    status: Literal["answer_recorded"]
    message: str


class EvaluationScores(BaseModel):
    """Detailed scores for an answer."""
    correctness: int = Field(..., ge=0, le=10)
    depth: int = Field(..., ge=0, le=10)
    trade_off_awareness: int = Field(..., ge=0, le=10)
    communication_clarity: int = Field(..., ge=0, le=10)


class EvaluationResponse(BaseModel):
    """Response from evaluation."""
    scores: EvaluationScores
    average_score: float = Field(..., ge=0, le=10)
    feedback: str
    strengths: List[str]
    improvements: List[str]


class NextSectionResponse(BaseModel):
    """Response after moving to next section."""
    current_section: InterviewSection
    difficulty: Difficulty
    message: str


class SectionReport(BaseModel):
    """Report for a single section."""
    section: InterviewSection
    score: float
    feedback: str
    difficulty: Difficulty
    questions_asked: int
    strengths: List[str]
    improvements: List[str]


class FinalReportResponse(BaseModel):
    """Complete interview report."""
    session_id: UUID
    topic: InterviewTopic
    candidate_name: str
    started_at: datetime
    completed_at: Optional[datetime]
    sections: List[SectionReport]
    overall_score: float
    recommendation: Recommendation
    summary: str
    key_strengths: List[str]
    key_improvements: List[str]


# Internal Models (for LLM communication)
class InterviewerContext(BaseModel):
    """Context passed to interviewer LLM."""
    topic: InterviewTopic
    section: InterviewSection
    difficulty: Difficulty
    question_number: int
    conversation_history: List[Dict[str, str]]


class EvaluatorContext(BaseModel):
    """Context passed to evaluator LLM."""
    topic: InterviewTopic
    section: InterviewSection
    question: str
    answer: str
    difficulty: Difficulty


class LLMEvaluationOutput(BaseModel):
    """Structured output from evaluator LLM."""
    correctness: int
    depth: int
    trade_off_awareness: int
    communication_clarity: int
    feedback: str
    strengths: List[str]
    improvements: List[str]