"""
Real-time monitoring dashboard for Project Chimera (Prometheus metrics)
"""
from prometheus_client import Counter, Histogram, Gauge

# HTTP metrics (used by app.metrics and middleware)
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

# Business metrics
agent_activity_gauge = Gauge(
    "chimera_agent_activity",
    "Active agent count",
    ["status"],
)

content_generation_counter = Counter(
    "chimera_content_generated_total",
    "Total content generated",
    ["content_type", "platform"],
)

transaction_counter = Counter(
    "chimera_transactions_total",
    "Total blockchain transactions",
    ["transaction_type", "status", "network"],
)

error_counter = Counter(
    "chimera_errors_total",
    "Total errors",
    ["error_type", "component"],
)

revenue_gauge = Gauge("chimera_revenue_usdc", "Total revenue in USDC")
engagement_gauge = Gauge("chimera_engagement_total", "Total engagement across all platforms")
cost_gauge = Gauge("chimera_operational_cost_usdc", "Total operational cost in USDC")


def record_request(method: str, endpoint: str, status: int, duration: float):
    request_counter.labels(method=method, endpoint=endpoint, status=status).inc()
    response_time_histogram.labels(method=method, endpoint=endpoint).observe(duration)


def record_agent_activity(status: str, count: int):
    agent_activity_gauge.labels(status=status).set(count)


def record_content_generation(content_type: str, platform: str):
    content_generation_counter.labels(content_type=content_type, platform=platform).inc()


def record_transaction(transaction_type: str, status: str, network: str):
    transaction_counter.labels(
        transaction_type=transaction_type, status=status, network=network
    ).inc()


def record_error(error_type: str, component: str):
    error_counter.labels(error_type=error_type, component=component).inc()


def update_business_metrics(revenue: float, engagement: int, cost: float):
    revenue_gauge.set(revenue)
    engagement_gauge.set(engagement)
    cost_gauge.set(cost)
