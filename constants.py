from dataclasses import dataclass

@dataclass(frozen=True)
class Tables:
    ROUTES: str = 'Routes'
    DIY_ROUTES: str = 'DiyRoutes'
    DIY_SEGMENTS: str = 'DiySegments'
    IDEMPOTENCY_KEYS: str = 'IdempotencyKeys'

@dataclass(frozen=True)
class CalculationMetrics:
    AVG_DISTANCE_PER_SEC_FT: float = 4.5
    DISTANCE_CAPTION_DISPLAY_DUREATION: int = 10
    TRIGGER_DISTANCE_CAPTION_ON_DURATION: int = 45
    DURATION_BEFORE_TURN_NOTICE: int = 8 # This is derived from "AVG_DISTANCE_PER_SEC_FT"

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

@dataclass(frozen=True)
class S3_PATHS:
    ROUTES: str = 'routes'
    SECURE_ROUTES: str = 'secure_routes'
    DIY_ROUTES: str = 'diy_routes'
    DIY_SEGMENTS: str = 'diy_segments'

@dataclass(frozen=True)
class PROCESS_STATUS:
    FACE_BLUR_START: str = 'FACE_BLUR_START'
    FACE_BLUR_ERROR: str = 'FACE_BLUR_ERROR'
    FACE_BLUR_SUCCESS: str = 'FACE_BLUR_SUCCESS'
    TEXT_BLUR_START: str = 'TEXT_BLUR_START'
    TEXT_BLUR_ERROR: str = 'TEXT_BLUR_ERROR'
    TEXT_BLUR_SUCCESS: str = 'TEXT_BLUR_SUCCESS'
    DIRECTION_DETECTION_ERROR: str = 'DIRECTION_DETECTION_ERROR'
    DIRECTION_DETECTION_SUCCESS: str = 'DIRECTION_DETECTION_SUCCESS'
    DIRECTION_DETECTION_START: str = 'DIRECTION_DETECTION_START'
    ARROW_ATTACHMENT_START: str = 'ARROW_ATTACHMENT_START'
    ARROW_ATTACHMENT_ERROR: str = 'ARROW_ATTACHMENT_ERROR'
    ARROW_ATTACHMENT_SUCCESS: str = 'ARROW_ATTACHMENT_SUCCESS'
    ROUTE_CREATION_START: str = 'ROUTE_CREATION_START'
    ROUTE_CREATION_ERROR: str = 'ROUTE_CREATION_ERROR'
    ROUTE_CREATION_SUCCESS: str = 'ROUTE_CREATION_SUCCESS'
    TRIM_VIDEO_START: str = 'SEGMENT_VIDEO_TRIM_START'
    TRIM_VIDEO_ERROR: str = 'SEGMENT_VIDEO_TRIM_ERROR'
    TRIM_VIDEO_SUCCESS: str = 'SEGMENT_VIDEO_TRIM_SUCCESS'
    LITE_ROUTE_VIDEO_TRIM_START: str = 'LITE_ROUTE_VIDEO_TRIM_START'
    LITE_ROUTE_VIDEO_TRIM_ERROR: str = 'LITE_ROUTE_VIDEO_TRIM_ERROR'
    LITE_ROUTE_VIDEO_TRIM_SUCCESS: str = 'LITE_ROUTE_VIDEO_TRIM_SUCCESS'


class ROUTE_ACTION_STATUS:
    CREATING: str = 'Creating'
    UPDATING: str = 'Updating'
    DELETING: str = 'Deleting'
    CREATED: str = 'Created'
    UPDATED: str = 'Updated'
    UPDATE_FAILED: str = 'Update failed'

@dataclass(frozen=True)
class Media_Basics:
    MediaUrlPrefix = "https://media.rtme.us"
