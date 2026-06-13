from fastapi import APIRouter

router = APIRouter(prefix="/api/mundial", tags=["mundial"])


@router.get("/standings")
def get_mundial_standings():
    from api.services import wc2026_client
    groups = wc2026_client.build_standings()
    return {"groups": groups}


@router.get("/fixtures")
def get_mundial_fixtures():
    from api.services import wc2026_client
    fixtures = wc2026_client.build_fixtures()
    return {"fixtures": fixtures}


@router.get("/topscorers")
def get_mundial_topscorers():
    from api.services import wc2026_client
    scorers = wc2026_client.build_topscorers()
    return {"scorers": scorers}
