import pytest
import tasks
from tasks import Task

@pytest.fixture()
def _create_players(players_count=2):
    
