"""
E2E: Full agent workflow (Planner → Worker → Judge).
Ref: specs/functional.md, FastRender Swarm
"""
import pytest

pytestmark = pytest.mark.asyncio


async def test_agent_workflow_plan_execute_validate():
    """
    FR 6.0: E2E Planner → Worker → Judge. Plan a goal, execute tasks, validate outputs.
    TDD: Defines goal posts for full swarm workflow; may be minimal until implemented.
    """
    # Stub: full workflow to be implemented with real Planner/Worker/Judge
    from app.services import PlannerService, WorkerService, JudgeService

    planner = PlannerService()
    worker = WorkerService()
    judge = JudgeService()

    tasks = planner.plan("Create one fashion trend post for Alex Crypto")
    assert isinstance(tasks, list)
    # With no implementation, tasks may be empty
    if tasks:
        task_id = tasks[0].get("id") or tasks[0].get("task_id") or "stub"
        result = await worker.execute_task(task_id, tasks[0])
        assert "status" in result
        if result.get("output_data"):
            validation = judge.validate(result.get("task_id", task_id), result["output_data"])
            assert "confidence_score" in validation
