from dataclasses import dataclass

@dataclass(frozen=True)
class Tables:
    ROUTES: str = 'Routes'
    DIY_ROUTES: str = 'DiyRoutes'
    DIY_SEGMENTS: str = 'DiySegments'
    IDEMPOTENCY_KEYS: str = 'IdempotencyKeys'

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
