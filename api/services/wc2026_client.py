import requests
from typing import Optional
from datetime import datetime

BASE_URL = "https://wheniskickoff.com/data/v1"


def _fetch(endpoint: str) -> Optional[dict]:
    try:
        r = requests.get(f"{BASE_URL}/{endpoint}", timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        print(f"WC2026 API error: {e}")
        return None


def get_matches() -> list:
    data = _fetch("matches.json")
    return data.get("data", []) if data else []


def get_teams() -> list:
    data = _fetch("teams.json")
    return data.get("data", []) if data else []


def get_groups() -> list:
    data = _fetch("groups.json")
    return data.get("data", []) if data else []


def build_standings() -> list:
    matches = get_matches()
    teams = get_teams()
    team_lookup = {t["code"]: t for t in teams}
    group_matches: dict[str, list] = {}

    for m in matches:
        g = m.get("group")
        if g and m.get("phase") == "group":
            group_matches.setdefault(g, []).append(m)

    result = []
    group_names = sorted(group_matches.keys())

    for gn in group_names:
        group_teams_map: dict[str, dict] = {}
        for code, t in team_lookup.items():
            if t.get("group") == gn:
                group_teams_map[code] = {
                    "team_code": code,
                    "team_name": t.get("name", code),
                    "team_flag": t.get("flag", ""),
                    "played": 0,
                    "win": 0,
                    "draw": 0,
                    "lose": 0,
                    "goals_for": 0,
                    "goals_against": 0,
                    "points": 0,
                }

        for m in group_matches[gn]:
            home = m.get("home")
            away = m.get("away")
            sh = m.get("score_home")
            sa = m.get("score_away")
            status = m.get("status")

            if status not in ("FINISHED",):
                continue
            if sh is None or sa is None:
                continue

            if home in group_teams_map:
                ht = group_teams_map[home]
                ht["played"] += 1
                ht["goals_for"] += sh
                ht["goals_against"] += sa
                if sh > sa:
                    ht["win"] += 1
                    ht["points"] += 3
                elif sh == sa:
                    ht["draw"] += 1
                    ht["points"] += 1
                else:
                    ht["lose"] += 1

            if away in group_teams_map:
                at = group_teams_map[away]
                at["played"] += 1
                at["goals_for"] += sa
                at["goals_against"] += sh
                if sa > sh:
                    at["win"] += 1
                    at["points"] += 3
                elif sa == sh:
                    at["draw"] += 1
                    at["points"] += 1
                else:
                    at["lose"] += 1

        sorted_teams = sorted(
            group_teams_map.values(),
            key=lambda t: (-t["points"], -(t["goals_for"] - t["goals_against"]), -t["goals_for"]),
        )

        label = f"Grupo {gn}"
        result.append({
            "name": label,
            "teams": [
                {
                    "position": i + 1,
                    "team_id": t["team_code"],
                    "team_name": t["team_name"],
                    "team_logo": t["team_flag"],
                    "points": t["points"],
                    "played": t["played"],
                    "win": t["win"],
                    "draw": t["draw"],
                    "lose": t["lose"],
                    "goals_for": t["goals_for"],
                    "goals_against": t["goals_against"],
                    "goal_difference": t["goals_for"] - t["goals_against"],
                }
                for i, t in enumerate(sorted_teams)
            ],
        })

    return result


def build_fixtures() -> list:
    matches = get_matches()
    result = []
    for i, m in enumerate(matches):
        status = m.get("status", "")
        short_status = "FT" if status == "FINISHED" else "LIVE" if status == "LIVE" else "SCHEDULED"
        result.append({
            "id": m.get("num", i),
            "date": m.get("datetime_utc", ""),
            "status": short_status,
            "elapsed": None,
            "round": m.get("phase", "group"),
            "group": m.get("group", ""),
            "home": {
                "id": m.get("home"),
                "name": m.get("home_name", m.get("home")),
                "logo": "",
            },
            "away": {
                "id": m.get("away"),
                "name": m.get("away_name", m.get("away")),
                "logo": "",
            },
            "goals": {
                "home": m.get("score_home"),
                "away": m.get("score_away"),
            },
        })
    return result


def build_topscorers() -> list:
    return []
