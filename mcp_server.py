# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Glymphatic Clearance Aquaporin-4 Sleep Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentGlymphaticClearanceAquaporin4Sleep

mcp = FastMCP("PersonalAgentGlymphaticClearanceAquaporin4Sleep")
client = PersonalAgentGlymphaticClearanceAquaporin4Sleep()

@mcp.tool()
def model_nocturnal_glymphatic_flux(
    slow_wave_sleep_minutes: float = 85.0,
    rem_sleep_minutes: float = 95.0,
    total_sleep_hours: float = 7.5,
    sleep_position: str = "lateral_right",
    alcohol_consumed_evening: bool = False
) -> str:
    """Calculates nocturnal Neuro-Metabolic Solute Clearance Score (NMSCS), SWS interstitial expansion, and washout."""
    import json
    return json.dumps(client.model_nocturnal_glymphatic_flux(
        slow_wave_sleep_minutes, rem_sleep_minutes, total_sleep_hours, sleep_position, alcohol_consumed_evening
    ), indent=2)

@mcp.tool()
def prescribe_glymphatic_optimization_routine(
    baseline_sws_minutes: float = 60.0,
    habitual_position: str = "supine"
) -> str:
    """Prescribes biomechanical posture and chronobiological routine to maximize convective brain waste clearance."""
    import json
    return json.dumps(client.prescribe_glymphatic_optimization_routine(
        baseline_sws_minutes, habitual_position
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
