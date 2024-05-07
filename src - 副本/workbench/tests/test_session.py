import sys
from pathlib import Path

p = str(Path(__file__).parent.parent)
sys.path.append(p)

from models.session import Exploration, Job, Route, Session
from utils.id import get_uuid

session_id = "12835"
exploration_id = get_uuid()
job_id = get_uuid()


def test_session_get_empty():
    Session.load(session_id)


def test_session_save():
    route = Route(route_name="rank1", properties={"step": 3, "complete": True}, workflow={})
    job = Job(id=job_id, name="test_job", status="running", routes=[route], descriptions="")
    session = Session(session_id=session_id, creator="liupeng@dp.tech")
    exploration = Exploration(id=exploration_id, name="test exp", target_molecule="CCO", jobs=[job])
    session.explorations = [exploration]
    assert not session.save()


def test_session_get():
    test_session_save()
    s = Session.load(session_id)
    print(s.explorations[0].jobs[0].routes[0].workflow)
    assert s.explorations[0].jobs[0].routes[0].workflow == {}
    # s.delete(session_id)


# test_session_save()
# test_session_get()
test_session_get_empty()
