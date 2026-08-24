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

@dataclass(frozen=True)
class DirectionDetectionConfig:
    """Speed tunables for Farneback direction detection (stride + downscale + lighter params)."""
    FRAME_STRIDE: int = 2
    FLOW_MAX_WIDTH: int = 640
    FARNEBACK_PYR_SCALE: float = 0.5
    FARNEBACK_LEVELS: int = 3
    FARNEBACK_WINSIZE: int = 11
    FARNEBACK_ITERATIONS: int = 2
    FARNEBACK_POLY_N: int = 5
    FARNEBACK_POLY_SIGMA: float = 1.2
    # Calibrated for stride=1 at native resolution; scaled at runtime for resize only
    BASE_SENSITIVITY: float = 1.6
    BASE_SLIGHT_THRESHOLD: float = 0.8
