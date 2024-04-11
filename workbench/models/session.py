import re
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import field
from pydantic.dataclasses import dataclass
from pydantic import parse_obj_as, root_validator
from enum import Enum
from loguru import logger
from pydantic import field_validator
from models.store import get_store
from utils.enhanced_dataclasses import asdict
from utils.tracer import trace_time

store = get_store()
UUID4_RE = re.compile("^[a-f0-9]{32}$")


@dataclass
class Route:
    route_name: str = ""
    properties: Dict[str, Any] = field(default_factory=dict)
    workflow: Dict[str, Any] = field(default_factory=dict)
    download_smiles: Optional[Dict[str, Any]] = field(default_factory=dict)
    # backup_reactions: Dict[str, Any] = field(default_factory=dict)


class JobStatus(str, Enum):
    init = "init"
    start = "start"
    preprocessed = "preprocessed"
    running = "running"
    success = "success"
    downloading = "downloading"
    stopping = "stopping"
    stopped = "stopped"
    finished = "finished"
    failed = "failed"
    unknown = "unknown"
    pending = "pending"
    submitted = "submitted"


RUNNING_JOB_STATUS = (
    JobStatus.init,
    JobStatus.start,
    JobStatus.preprocessed,
    JobStatus.running,
    JobStatus.downloading,
    JobStatus.stopping,
    JobStatus.pending,
    JobStatus.submitted,
    JobStatus.unknown,
)


@dataclass
class Job:
    id: str
    name: str
    routes: Optional[List[Route]] = field(default_factory=list)
    status: JobStatus = JobStatus.init
    descriptions: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def set_routes(self, routes):
        if not routes:
            return
        for route in routes:
            r: Route = parse_obj_as(Route, route)
            self.routes.append(r)


@dataclass
class Options:
    reaction_type: str = "ai+database"
    fast_fail: bool = False
    max_iteration: int = 10
    backup_reactions: Optional[Dict[str, Any]] = field(default_factory=dict)


class ExplorationStatus(str, Enum):
    running = "running"
    success = "success"
    failed = "failed"


@dataclass
class Exploration:
    id: str
    name: str
    jobs: Optional[List[Job]] = field(default_factory=list)
    target_molecule: str = ""
    bohrium_payment_project_id: Optional[int] = 0
    options: Optional[Options] = field(default_factory=dict)
    summary: Dict[str, Any] = field(default_factory=dict)
    status: ExplorationStatus = ExplorationStatus.running

    def get_job_index(self, job_id):
        # return -1 if not found.
        if not self.jobs:
            return -1
        for i in range(0, len(self.jobs)):
            job = self.jobs[i]
            if job.id == job_id:
                return i
        return -1


# TODO 用独立 key 分别存储 explorations 和 jobs 来支持 patch 操作提升性能，减少竞争写
@dataclass
class Session:
    # current use userId as session_id
    session_id: str
    description: str = ""
    creator: str = ""
    # current 类信息暂时只存在 state 中
    # current_exploration_name: str = ""
    # current_job_id: str = ""
    # current_route_id: str = ""
    tour_shown: bool = False
    explorations: List[Exploration] = field(default_factory=list)
    options: Dict[str, Any] = field(default_factory=dict)
    properties: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

    @classmethod
    def get_session_key(cls, session_id):
        return f"{session_id}"

    def get_exploration_index(self, name):
        # return -1 if not found.
        if not self.explorations:
            return -1
        for i in range(0, len(self.explorations)):
            exp = self.explorations[i]
            if exp.name == name:
                return i
        return -1

    def save(self) -> None:
        content = json.dumps(asdict(self), indent=4)
        key = self.get_session_key(self.session_id)
        store.put(key, content)

    @classmethod
    @trace_time
    def load(cls, session_id: str) -> "Session":
        key = cls.get_session_key(session_id)
        content = store.get(key)
        if not content:
            session = Session(session_id=session_id)
            session.save()
            content = store.get(key)
        return parse_obj_as(cls, json.loads(content))

    @classmethod
    @trace_time
    def delete(cls, session_id: str) -> None:
        key = cls.get_session_key(session_id)
        return store.delete(key)
