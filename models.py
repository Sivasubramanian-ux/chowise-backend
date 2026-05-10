from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Promise(BaseModel):
    id: Optional[str] = None
    title: str
    category: str
    status: str
    year: int

class MLAProfile(BaseModel):
    id: Optional[str] = None
    name: str
    constituency: str
    party: str
    photo_url: str
    activity_rate: float = Field(default=0.75, ge=0.0, le=1.0)
    promises: List[Promise] = Field(default_factory=list)
    accuracy_score: float = Field(default=0.75, ge=0.0, le=1.0)
    tenure_start: Optional[int] = 2021
    tenure_end: Optional[int] = 2026
    education: Optional[str] = None
    years_in_politics: Optional[int] = None
    portfolio: Optional[str] = "MLA"
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "1",
                "name": "Udhayanidhi Stalin",
                "constituency": "Chepauk-Thiruvallikeni",
                "party": "DMK",
                "photo_url": "https://via.placeholder.com/150",
                "activity_rate": 0.85,
                "promises": [],
                "accuracy_score": 0.85,
                "tenure_start": 2021,
                "tenure_end": 2026
            }
        }

class MLACreate(BaseModel):
    name: str
    constituency: str
    party: str
    photo_url: Optional[str] = "https://via.placeholder.com/150"
    activity_rate: Optional[float] = 0.75
    accuracy_score: Optional[float] = 0.75
    promises: Optional[List[Promise]] = None

class MLAUpdate(BaseModel):
    name: Optional[str] = None
    constituency: Optional[str] = None
    party: Optional[str] = None
    photo_url: Optional[str] = None
    activity_rate: Optional[float] = None
    accuracy_score: Optional[float] = None

class CMCandidate(BaseModel):
    id: str
    name: str
    party: str
    position: str
    status: str  # 'Current CM', 'Potential Successor', 'Opposition Candidate'
    cm_probability: float = Field(ge=0.0, le=1.0)
    is_current_cm: bool = False
    term_start: Optional[int] = None
    term_end: Optional[int] = None
    past_performance: Optional[Dict[str, Any]] = None
    photo_url: Optional[str] = None
    biography: Optional[str] = None
    education: Optional[str] = None
    years_in_politics: Optional[int] = None
    party_symbol: Optional[str] = None

class OppositionLeader(BaseModel):
    id: str
    name: str
    party: str
    position: str
    party_symbol: Optional[str] = None
    cm_probability: float = Field(ge=0.0, le=1.0)
    past_performance: Optional[Dict[str, Any]] = None
    photo_url: Optional[str] = None
    biography: Optional[str] = None
    education: Optional[str] = None

class Feedback(BaseModel):
    id: Optional[str] = None
    constituency: str
    issue_description: str
    submitted_at: datetime = Field(default_factory=datetime.utcnow)

class PredictionResponse(BaseModel):
    constituency: str
    recommended_candidate: str
    party: str
    confidence_score: float
    reasoning: str

class CMPredictionResponse(BaseModel):
    cm_candidate: str
    party: str
    probability: float
    reasoning: str
    alternative_candidates: List[Dict[str, Any]] = Field(default_factory=list)
