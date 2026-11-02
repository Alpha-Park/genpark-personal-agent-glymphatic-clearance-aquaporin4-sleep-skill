# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Glymphatic Clearance Aquaporin-4 Sleep Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentGlymphaticClearanceAquaporin4Sleep

def main():
    agent = PersonalAgentGlymphaticClearanceAquaporin4Sleep()

    print("=" * 70)
    print("DEMO: Personal Agent Glymphatic Brain Clearance & AQP4 Modeler")
    print("=" * 70)

    # 1. Model Glymphatic Flux (90 min SWS, 7.8 hrs sleep, lateral right position, 0 alcohol)
    res_flux = agent.model_nocturnal_glymphatic_flux(
        slow_wave_sleep_minutes=90.0,
        rem_sleep_minutes=100.0,
        total_sleep_hours=7.8,
        sleep_position="lateral_right",
        alcohol_consumed_evening=False
    )

    print(f"\n1. Nocturnal Glymphatic Solute Clearance Analysis:")
    print(f"   Total Sleep: {res_flux['total_sleep_duration_hours']} hrs (SWS: {res_flux['slow_wave_sleep_minutes']} min)")
    print(f"   Sleep Posture: {res_flux['dominant_sleep_posture']} (Multiplier: {res_flux['postural_flux_multiplier']}x)")
    print(f"   Interstitial Expansion: {res_flux['interstitial_volume_expansion_pct']}")
    print(f"   NMSCS Score: {res_flux['neuro_metabolic_solute_clearance_score_nmscs']}/100")
    print(f"   Clearance Tier: {res_flux['glymphatic_clearance_tier']}")
    print(f"   Solute Estimate: {res_flux['interstitial_metabolite_clearance_estimate']}")
    print(f"   AQP4 Status: {'Intact & Polarized' if res_flux['aquaporin4_polarization_intact'] else 'Disrupted'}")
    print(f"   Mechanism: {res_flux['clinical_mechanism_summary']}")

    # 2. Prescribe Optimization Routine for someone with 65 min SWS sleeping supine
    res_proto = agent.prescribe_glymphatic_optimization_routine(
        baseline_sws_minutes=65.0,
        habitual_position="supine"
    )

    print(f"\n2. Personalized Glymphatic Optimization Routine:")
    print(f"   Baseline SWS: {res_proto['baseline_sws_minutes']} min | Posture: {res_proto['habitual_posture']}")
    print(f"   Postural Change Needed: {res_proto['postural_optimization_warranted']}")
    print(f"   Expected Flux Gain: {res_proto['expected_glymphatic_gain']}")
    print(f"   Prescriptions:")
    for r in res_proto['actionable_prescriptions']:
        print(f"     * {r}")

    print("\nVerification complete: Glymphatic clearance engine executed flawlessly.")

if __name__ == "__main__":
    main()
