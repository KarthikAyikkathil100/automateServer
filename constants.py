from dataclasses import dataclass

@dataclass(frozen=True)
class Tables:
    ROUTES: str = 'Routes'
    IDEMPOTENCY_KEYS: str = 'IdempotencyKeys'
