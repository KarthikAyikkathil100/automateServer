from dataclasses import dataclass

@dataclass(frozen=True)
class Tables:
    ROUTES: str = 'Routes'
    DIY_ROUTES: str = 'DiyRoutes'
    DIY_SEGMENTS: str = 'DiySegments'

@dataclass(frozen=True)
class S3_PATHS:
    ROUTES: str = 'routes'
    DIY_ROUTES: str = 'diy_routes'
    
@dataclass(frozen=True)
class Media_Basics:
    MediaUrlPrefix = "https://media.rtme.us"
