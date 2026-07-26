from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class ComponentScores(BaseModel):
    formatting: float
    keywords: float
    content: float
    skill_validation: float
    ats_compatibility: float


class JDComparison(BaseModel):
    match_percentage: float
    semantic_similarity: float
    matched_keywords: List[str]
    missing_keywords: List[str]
    skills_gap: List[str]          # was: skills_gap=List[str]


class SkillValidationDetails(BaseModel):
    validated: List[Dict[str, Any]] = []
    unvalidated: List[str] = []
    total: int = 0
    validation_count: int = 0
    validation_pct: float = 0.0


class IssueDetail(BaseModel):
    issue_title: str
    severity_level: str            # was: severity_level=str
    ats_impact: str                # was: ats_impact=str
    explanation: str               # was: explanation=str
    where_it_appears: str
    how_to_fix: str
    action_items: List[str] = []
    example_improvement: str


class AnalysisResponse(BaseModel):
    ATS_score: float
    component_scores: ComponentScores
    issues_summary: List[str]
    detailed_feedback: List[IssueDetail]
    jd_match_analysis: Optional[JDComparison] = None
    skill_validation_details: Optional[SkillValidationDetails] = None   # was: broken syntax
    keyword_match: float = 0.0