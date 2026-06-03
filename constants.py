from dataclasses import dataclass

@dataclass(frozen=True)
class Tables:
    ROUTES: str = 'Routes'
    IDEMPOTENCY_KEYS: str = 'IdempotencyKeys'

@dataclass(frozen=True)
class CalculationMetrics:
    AVG_DISTANCE_PER_SEC_FT: float = 4.5
    DISTANCE_CAPTION_DISPLAY_DUREATION: int = 10
    TRIGGER_DISTANCE_CAPTION_ON_DURATION: int = 45
    DURATION_BEFORE_TURN_NOTICE: int = 8
