"""
AegisGlobal AI - Maritime & Geopolitical Database
Contains high-precision coordinates for Global Ports, Chokepoints, Fleets, and Crisis Scenarios.
"""

# Global Strategic Ports (Latitude, Longitude)
GLOBAL_PORTS = {
    "Mumbai (JNPT)": {"lat": 18.9499, "lng": 72.9510, "country": "India", "code": "INBOM"},
    "Shanghai": {"lat": 31.2304, "lng": 121.4737, "country": "China", "code": "CNSHA"},
    "Singapore": {"lat": 1.3521, "lng": 103.8198, "country": "Singapore", "code": "SGSIN"},
    "Dubai (Jebel Ali)": {"lat": 25.0118, "lng": 55.0612, "country": "UAE", "code": "AEJEA"},
    "Rotterdam": {"lat": 51.9244, "lng": 4.4777, "country": "Netherlands", "code": "NLRTM"},
    "London (Gateway)": {"lat": 51.5074, "lng": 0.1278, "country": "United Kingdom", "code": "GBLON"},
    "New York": {"lat": 40.7128, "lng": -74.0060, "country": "USA", "code": "USNYC"},
    "Los Angeles": {"lat": 33.7405, "lng": -118.2713, "country": "USA", "code": "USLAX"},
    "Cape Town": {"lat": -33.9249, "lng": 18.4241, "country": "South Africa", "code": "ZACPT"},
    "Tokyo": {"lat": 35.6762, "lng": 139.6503, "country": "Japan", "code": "JPTYO"},
    "Sydney": {"lat": -33.8688, "lng": 151.2093, "country": "Australia", "code": "AUSYD"},
    "Suez Port": {"lat": 29.9668, "lng": 32.5498, "country": "Egypt", "code": "EGSUZ"},
    "Panama City": {"lat": 8.9824, "lng": -79.5199, "country": "Panama", "code": "PABAL"},
    "Colombo": {"lat": 6.9271, "lng": 79.8612, "country": "Sri Lanka", "code": "LKCMB"}
}

# Vulnerable Global Chokepoints
GLOBAL_CHOKEPOINTS = {
    "Suez Canal": {"lat": 30.5852, "lng": 32.2654, "threat_type": "Blockage / Grounding", "daily_cargo_value_usd_b": 9.6},
    "Bab-el-Mandeb Strait": {"lat": 12.5833, "lng": 43.3333, "threat_type": "Maritime Missile & Drone Attacks", "daily_cargo_value_usd_b": 6.2},
    "Strait of Hormuz": {"lat": 26.5667, "lng": 56.2500, "threat_type": "Geopolitical Oil Seizure", "daily_cargo_value_usd_b": 14.1},
    "Strait of Malacca": {"lat": 2.5000, "lng": 101.5000, "threat_type": "Congestion & Piracy", "daily_cargo_value_usd_b": 11.8},
    "Panama Canal": {"lat": 9.0800, "lng": -79.6800, "threat_type": "Drought / Low Water Capacity", "daily_cargo_value_usd_b": 4.5},
    "Taiwan Strait": {"lat": 24.5000, "lng": 119.8000, "threat_type": "Naval Blockade", "daily_cargo_value_usd_b": 8.0}
}

# Live Active Fleet Simulation
ACTIVE_FLEET = [
    {
        "id": "VSL-701",
        "name": "Ever Zenith (Ultra Large Container Vessel)",
        "cargo": "Advanced Semiconductor Chips & Lithium EV Batteries",
        "cargo_value_usd_m": 480.0,
        "origin": "Shanghai",
        "destination": "Rotterdam",
        "current_route": ["Shanghai", "Singapore", "Colombo", "Suez Port", "Rotterdam"],
        "status": "In Transit",
        "speed_knots": 19.5,
        "fuel_consumption_ton_day": 85
    },
    {
        "id": "VSL-804",
        "name": "Pacific Titan (Crude Oil Supertanker)",
        "cargo": "2 Million Barrels Brent Crude Oil",
        "cargo_value_usd_m": 165.0,
        "origin": "Dubai (Jebel Ali)",
        "destination": "London (Gateway)",
        "current_route": ["Dubai (Jebel Ali)", "Bab-el-Mandeb Strait", "Suez Port", "London (Gateway)"],
        "status": "In Transit",
        "speed_knots": 14.2,
        "fuel_consumption_ton_day": 95
    },
    {
        "id": "VSL-319",
        "name": "Bharat Horizon (Specialized Freight)",
        "cargo": "Automotive Engine Units & Precision Machining",
        "cargo_value_usd_m": 210.0,
        "origin": "Mumbai (JNPT)",
        "destination": "New York",
        "current_route": ["Mumbai (JNPT)", "Bab-el-Mandeb Strait", "Suez Port", "New York"],
        "status": "In Transit",
        "speed_knots": 18.0,
        "fuel_consumption_ton_day": 78
    },
    {
        "id": "VSL-992",
        "name": "Nordic Vanguard (Bulk Carrier)",
        "cargo": "Industrial Grade Solar Panels & Rare Earth Minerals",
        "cargo_value_usd_m": 310.0,
        "origin": "Singapore",
        "destination": "Los Angeles",
        "current_route": ["Singapore", "Tokyo", "Los Angeles"],
        "status": "In Transit",
        "speed_knots": 16.8,
        "fuel_consumption_ton_day": 65
    }
]

# Crisis Preset Scenarios
CRISIS_PRESETS = [
    {
        "id": "suez_blockade",
        "title": "Suez Canal Ultra-Vessel Grounding & Blockade",
        "chokepoint": "Suez Canal",
        "severity": "CRITICAL - RED ALERT",
        "lat": 30.5852,
        "lng": 32.2654,
        "radius_km": 600,
        "description": "A 400-meter container ship has suffered catastrophic steering loss and grounded diagonally, obstructing 100% of northbound and southbound maritime traffic.",
        "affected_vessels": ["VSL-701", "VSL-804", "VSL-319"]
    },
    {
        "id": "arabian_sea_cyclone",
        "title": "Category 5 Arabian Sea Super-Cyclone 'Tej-Fury'",
        "chokepoint": "Bab-el-Mandeb Strait",
        "severity": "SEVERE - DANGER ALERT",
        "lat": 16.5000,
        "lng": 63.5000,
        "radius_km": 850,
        "description": "Extreme storm surges with 14-meter waves and sustained wind speeds of 240 km/h threaten cargo vessels navigating between Gujarat/Mumbai and the Gulf of Aden.",
        "affected_vessels": ["VSL-804", "VSL-319"]
    },
    {
        "id": "red_sea_missile_threat",
        "title": "Red Sea / Bab-el-Mandeb Asymmetric Drone Strikes",
        "chokepoint": "Bab-el-Mandeb Strait",
        "severity": "WAR ZONE - MILITARY RISK",
        "lat": 12.5833,
        "lng": 43.3333,
        "radius_km": 500,
        "description": "Active anti-ship ballistic missiles and unmanned sea vessels deployed in international shipping corridors. Marine insurance underwriters have revoked war-risk coverage.",
        "affected_vessels": ["VSL-804", "VSL-319", "VSL-701"]
    },
    {
        "id": "taiwan_strait_lockdown",
        "title": "Taiwan Strait Naval Drills & Exclusion Zone",
        "chokepoint": "Taiwan Strait",
        "severity": "HIGH - EXCLUSION ZONE",
        "lat": 24.5000,
        "lng": 119.8000,
        "radius_km": 450,
        "description": "Live-fire military exercises have closed commercial maritime lanes between East Asian semiconductor factories and Pacific trade corridors.",
        "affected_vessels": ["VSL-701", "VSL-992"]
    }
]
