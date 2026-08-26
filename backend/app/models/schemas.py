from typing import List, Optional, Literal
from pydantic import BaseModel, Field, EmailStr


# ==========================================
# Auth Schemas
# ==========================================

class LoginRequest(BaseModel):
    email: str
    password: str


class SignupRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    token: str


# ==========================================
# Metrics & Pod Schemas
# ==========================================

class PodMetric(BaseModel):
    pod: str
    namespace: str
    cpu_percent: float
    memory_percent: float
    restart_count: int


class MetricHistoryPoint(BaseModel):
    timestamp: int  # Unix timestamp in milliseconds
    value: float


class NodeMetric(BaseModel):
    node: str
    status: Literal["Ready", "NotReady"]
    cpu_percent: float
    memory_percent: float


# ==========================================
# Logs Schemas
# ==========================================

class LogEntry(BaseModel):
    timestamp: int  # Unix timestamp in milliseconds
    line: str


# ==========================================
# Alert Schemas
# ==========================================

AlertSeverity = Literal["warning", "critical"]
AlertStatus = Literal["active", "resolved"]


class AlertItem(BaseModel):
    id: str
    pod: str
    namespace: str
    rule: str
    severity: AlertSeverity
    message: str
    status: AlertStatus
    created_at: str  # ISO-8601 string format
    acknowledged: bool


# ==========================================
# Cluster Discovery Schemas
# ==========================================

ClusterProvider = Literal["eks", "aks", "gke", "minikube", "kind", "k3s", "unknown"]


class DiscoveredCluster(BaseModel):
    id: str
    name: str
    displayName: str
    provider: ClusterProvider
    server: str
    contextName: str
    sourceFile: str
    isReachable: bool
    statusMessage: Optional[str] = None
    latencyMs: Optional[int] = None
    defaultNamespace: Optional[str] = "default"
    isManualOverride: Optional[bool] = False


class RescanResponse(BaseModel):
    message: str
    count: int
    clusters: List[DiscoveredCluster]


class HealthResponse(BaseModel):
    status: str = "ok"
