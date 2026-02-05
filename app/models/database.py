from sqlalchemy import Column, String, Float, Integer, DateTime, JSON, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid


Base = declarative_base()


class InterviewSession(Base):
    
    __tablename__ = "interview_sessions"
    
    session_id = Column(String(36), primary_key=True)
    
    topic = Column(String(50), nullable=False)
    candidate_name = Column(String(100), nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    
    current_section = Column(String(50), nullable=False)
    current_difficulty = Column(String(20), default="medium")
    
    section_scores = Column(JSON, default=dict)

    overall_score = Column(Float, nullable=True)
    recommendation = Column(String(50), nullable=True)
    final_summary = Column(Text, nullable=True)
    
    def __repr__(self):
        return f"<InterviewSession(id={self.session_id}, topic={self.topic})>"


class SectionEvaluation(Base):
    """Individual section evaluation."""
    __tablename__ = "section_evaluations"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    session_id = Column(String(36), nullable=False, index=True)
    
    section = Column(String(50), nullable=False)
    difficulty = Column(String(20), nullable=False)
    question_number = Column(Integer, nullable=False)
    
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    
    correctness = Column(Integer, nullable=False)
    depth = Column(Integer, nullable=False)
    trade_off_awareness = Column(Integer, nullable=False)
    communication_clarity = Column(Integer, nullable=False)
    average_score = Column(Float, nullable=False)
    
    feedback = Column(Text, nullable=False)
    strengths = Column(JSON, default=list)
    improvements = Column(JSON, default=list)
    
    evaluated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"<SectionEvaluation(session={self.session_id}, section={self.section})>"