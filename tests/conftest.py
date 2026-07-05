"""Test configuration for Disaster Recovery Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "disaster-recovery-agent", "category": "Cloud Engineering"}
