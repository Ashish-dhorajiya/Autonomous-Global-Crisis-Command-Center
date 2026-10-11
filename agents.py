"""
AegisGlobal AI - 4 Autonomous Swarm Agents Engine
Agent 1: Geopolitical & Weather Intelligence (SENTINEL-1)
Agent 2: Fleet Route Optimizer (NAVEX-4)
Agent 3: Financial & Carbon Auditor (QUANT-X)
Agent 4: Executive Crisis Diplomat (DIPLOMAT-PRIME)
"""

import time
import math
from typing import Dict, Any, List
from simulation_data import GLOBAL_PORTS, GLOBAL_CHOKEPOINTS, ACTIVE_FLEET, CRISIS_PRESETS

class GeopoliticalIntelligenceAgent:
    """Agent 1: Scans geopolitical friction and meteorological threats."""
    def __init__(self):
        self.name = "SENTINEL-1"
        self.role = "Geopolitical & Weather Intelligence Specialist"

    def analyze(self, crisis_info: Dict[str, Any]) -> Dict[str, Any]:
        time.sleep(0.3)  # Real-time processing simulation
        affected_vessels = []
        for vessel in ACTIVE_FLEET:
            # Check if vessel's route passes through or near the crisis chokepoint
            chokepoint_name = crisis_info.get("chokepoint", "")
            if any(chokepoint_name in stop for stop in vessel["current_route"]) or vessel["id"] in crisis_info.get("affected_vessels", []):
                affected_vessels.append(vessel)

        threat_level = crisis_info.get("severity", "HIGH ALERT")
        danger_coords = {"lat": crisis_info.get("lat", 0.0), "lng": crisis_info.get("lng", 0.0)}
        radius = crisis_info.get("radius_km", 500)

        return {
            "agent": self.name,
            "role": self.role,
            "status": "THREAT_CONFIRMED",
            "threat_level": threat_level,
            "danger_center": danger_coords,
            "exclusion_radius_km": radius,
            "description": crisis_info.get("description", "Maritime disruption detected."),
            "impacted_vessel_count": len(affected_vessels),
            "impacted_vessels": [v["name"] for v in affected_vessels],
            "action_required": "IMMEDIATE FLEET VECTOR DIVERSION"
        }

class RouteOptimizerAgent:
    """Agent 2: Calculates alternative global oceanic bypass routes in 3D coordinates."""
    def __init__(self):
        self.name = "NAVEX-4"
        self.role = "Autonomous Fleet & Deep-Sea Route Optimizer"

    def optimize_routes(self, crisis_info: Dict[str, Any], affected_vessels: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        time.sleep(0.4)
        rerouted_plans = []

        for vessel in affected_vessels:
            original_route = vessel["current_route"]
            # Alternative route: If through Suez / Red Sea, reroute via Cape of Good Hope
            chokepoint = crisis_info.get("chokepoint", "")
            
            if "Suez" in chokepoint or "Bab-el-Mandeb" in chokepoint:
                new_route_waypoints = [
                    vessel["origin"],
                    "Colombo",
                    "Cape Town",
                    "Rotterdam" if "Rotterdam" in vessel["destination"] else vessel["destination"]
                ]
                additional_nautical_miles = 3650
                additional_days = 9.8
                bypass_strategy = "Cape of Good Hope Oceanic Deep-Water Detour (South Africa)"
            elif "Taiwan" in chokepoint:
                new_route_waypoints = [
                    vessel["origin"],
                    "Tokyo",
                    "Sydney",
                    vessel["destination"]
                ]
                additional_nautical_miles = 2100
                additional_days = 5.4
                bypass_strategy = "East Pacific Mariana Trench Deep-Water Corridor"
            else:
                new_route_waypoints = [
                    vessel["origin"],
                    "Cape Town",
                    vessel["destination"]
                ]
                additional_nautical_miles = 2800
                additional_days = 7.2
                bypass_strategy = "Strategic International Waters Circumvention"

            # Generate 3D latitude & longitude coordinates for the new route
            route_coords = []
            for point_name in new_route_waypoints:
                if point_name in GLOBAL_PORTS:
                    route_coords.append({
                        "name": point_name,
                        "lat": GLOBAL_PORTS[point_name]["lat"],
                        "lng": GLOBAL_PORTS[point_name]["lng"]
                    })
                elif point_name in GLOBAL_CHOKEPOINTS:
                    route_coords.append({
                        "name": point_name,
                        "lat": GLOBAL_CHOKEPOINTS[point_name]["lat"],
                        "lng": GLOBAL_CHOKEPOINTS[point_name]["lng"]
                    })

            rerouted_plans.append({
                "vessel_id": vessel["id"],
                "vessel_name": vessel["name"],
                "cargo": vessel["cargo"],
                "cargo_value_m": vessel["cargo_value_usd_m"],
                "original_route": original_route,
                "optimized_route": new_route_waypoints,
                "route_coordinates": route_coords,
                "strategy": bypass_strategy,
                "additional_nautical_miles": additional_nautical_miles,
                "delay_days": additional_days,
                "safety_score_percentage": 99.4
            })

        return rerouted_plans

class FinancialAuditorAgent:
    """Agent 3: Computes fuel burn, charter party penalties, and cargo value preservation."""
    def __init__(self):
        self.name = "QUANT-X"
        self.role = "Maritime Financial & Carbon Impact Auditor"

    def audit(self, reroute_plans: List[Dict[str, Any]]) -> Dict[str, Any]:
        time.sleep(0.3)
        bunker_fuel_price_per_ton = 680.0  # USD / metric ton VLSFO
        daily_charter_rate_usd = 42000.0  # Daily vessel operating cost
        co2_emissions_factor_ton = 3.114  # Tons of CO2 per ton of VLSFO burned

        total_cargo_preserved_m = sum(plan["cargo_value_m"] for plan in reroute_plans)
        total_additional_days = sum(plan["delay_days"] for plan in reroute_plans)
        
        # Operational expenses calculation
        total_additional_fuel_tons = sum(plan["delay_days"] * 75.0 for plan in reroute_plans)
        total_fuel_cost_usd = total_additional_fuel_tons * bunker_fuel_price_per_ton
        total_charter_cost_usd = total_additional_days * daily_charter_rate_usd
        total_net_cost_increase_usd = total_fuel_cost_usd + total_charter_cost_usd
        total_co2_increase_tons = total_additional_fuel_tons * co2_emissions_factor_ton

        return {
            "agent": self.name,
            "role": self.role,
            "total_cargo_value_saved_usd_m": round(total_cargo_preserved_m, 1),
            "net_logistics_cost_delta_usd": round(total_net_cost_increase_usd, 2),
            "fuel_cost_increase_usd": round(total_fuel_cost_usd, 2),
            "charter_cost_increase_usd": round(total_charter_cost_usd, 2),
            "average_transit_delay_days": round(total_additional_days / max(len(reroute_plans), 1), 1),
            "carbon_emission_delta_co2_tons": round(total_co2_increase_tons, 1),
            "roi_loss_prevention_ratio": f"{round((total_cargo_preserved_m * 1000000) / max(total_net_cost_increase_usd, 1), 1)}:1"
        }

class ExecutiveDiplomatAgent:
    """Agent 4: Synthesizes executive briefings, port authority communications, and marine insurance filings."""
    def __init__(self):
        self.name = "DIPLOMAT-PRIME"
        self.role = "Executive Crisis Diplomat & Incident Controller"

    def draft_executive_brief(self, crisis_info: Dict[str, Any], sentinel_data: Dict[str, Any], nav_plans: List[Dict[str, Any]], quant_data: Dict[str, Any]) -> Dict[str, Any]:
        time.sleep(0.3)
        incident_id = f"AEGIS-INC-{int(time.time())}"
        
        executive_summary = (
            f"EXECUTIVE ACTION DIRECTIVE: {crisis_info.get('title', 'Global Maritime Event')}. "
            f"Immediate circumvention protocol activated across {sentinel_data['impacted_vessel_count']} commercial vessels. "
            f"Total cargo valued at ${quant_data['total_cargo_value_saved_usd_m']}M successfully insulated from threat perimeter. "
            f"Operational cost variance accepted at ${quant_data['net_logistics_cost_delta_usd']:,.2f} with average arrival delta of +{quant_data['average_transit_delay_days']} days."
        )

        insurance_notice = (
            f"NOTICE TO LLOYD'S UNDERWRITERS & P&I CLUBS: Vessels diverted prior to entering exclusion zone radius {sentinel_data['exclusion_radius_km']} km. "
            f"War-Risk and Gross Negligence exemptions nullified. Hull & Machinery (H&M) integrity verified."
        )

        supplier_notice = (
            f"SUPPLY CHAIN CONTINUITY ADVISORY: Tier-1 manufacturing plants (EV & Semiconductors) notified of adjusted estimated time of arrival (ETA). "
            f"Critical inventory buffer stocks engaged."
        )

        return {
            "agent": self.name,
            "role": self.role,
            "incident_id": incident_id,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
            "executive_summary": executive_summary,
            "insurance_underwriter_filing": insurance_notice,
            "supplier_continuity_bulletin": supplier_notice,
            "status": "DIRECTIVE_DISPATCHED_TO_BRIDGE_OFFICERS"
        }

class MultiAgentCrisisCoordinator:
    """Master Orchestrator coordinating all 4 AI agents."""
    def __init__(self):
        self.sentinel = GeopoliticalIntelligenceAgent()
        self.navex = RouteOptimizerAgent()
        self.quant = FinancialAuditorAgent()
        self.diplomat = ExecutiveDiplomatAgent()

    def execute_crisis_swarm(self, crisis_data: Dict[str, Any]) -> Dict[str, Any]:
        # Step 1: Agent 1 Intelligence Scan
        sentinel_output = self.sentinel.analyze(crisis_data)
        
        # Filter affected vessels
        affected_vessels = [v for v in ACTIVE_FLEET if v["name"] in sentinel_output["impacted_vessels"]]
        if not affected_vessels:
            affected_vessels = ACTIVE_FLEET[:2]  # Default to top 2 if general crisis

        # Step 2: Agent 2 Route Optimization
        route_plans = self.navex.optimize_routes(crisis_data, affected_vessels)

        # Step 3: Agent 3 Financial & Carbon Audit
        financial_audit = self.quant.audit(route_plans)

        # Step 4: Agent 4 Executive Briefing & Directives
        executive_brief = self.diplomat.draft_executive_brief(crisis_data, sentinel_output, route_plans, financial_audit)

        return {
            "success": True,
            "crisis": crisis_data,
            "agent_1_intelligence": sentinel_output,
            "agent_2_route_optimizer": route_plans,
            "agent_3_financial_auditor": financial_audit,
            "agent_4_executive_diplomat": executive_brief
        }
