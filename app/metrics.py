"""
Project Chimera: Prometheus metrics
"""
from prometheus_client import Counter, Histogram

request_counter = Counter(
    "chimera_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)

response_time_histogram = Histogram(
    "chimera_response_time_seconds",
    "HTTP response time",
    ["method", "endpoint"],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0],
)
