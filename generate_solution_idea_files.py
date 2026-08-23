from pathlib import Path
import re

ROOT = Path(r"c:\Users\arpit\Desktop\SIH")
INDEX_PATH = ROOT / "index.html"
OUT_DIR = ROOT / "solution_ideas"
OUT_DIR.mkdir(exist_ok=True)

# Title-specific patterns for unique SIH-style solution ideas

COMMON_PATTERNS = {
    "disaster": {
        "summary": "Build a predictive command-and-control platform that combines sensor data, imagery, GIS intelligence, and AI to forecast hazards before they escalate into crises.",
        "approach": [
            "Collect realtime environmental signals from rainfall, terrain, soil, and satellite feeds.",
            "Use spatiotemporal models to score risk at district, block, and village level.",
            "Translate risk output into alerts, route guidance, and action plans for district teams.",
            "Enable citizen reporting with photo and geotag evidence to refine predictions and improve trust."
        ],
        "modules": [
            "Risk engine",
            "Geospatial dashboard",
            "Field reporting app",
            "Alert and escalation system",
            "Offline sync layer"
        ],
        "stack": ["Python", "PyTorch / XGBoost", "PostgreSQL/PostGIS", "Leaflet / Mapbox", "React", "Node.js", "Firebase / Redis", "AWS/GCP"]
    },
    "logistics": {
        "summary": "Create an intelligent logistics intelligence layer that makes transport decisions adaptive, resilient, and route-aware under disruption conditions.",
        "approach": [
            "Track vehicle, route, and network health in real time.",
            "Combine weather, geography, road status, and demand patterns into a route-risk model.",
            "Recommend alternate corridors, rerouting, and inventory reallocation before goods are delayed.",
            "Give field teams a mobile app for incident reporting and road-condition capture."
        ],
        "modules": [
            "Network health monitor",
            "Route optimization engine",
            "Disruption forecasting",
            "Fleet tracking portal",
            "Decision support dashboard"
        ],
        "stack": ["Python", "Scikit-learn / LightGBM", "PostgreSQL/PostGIS", "Leaflet", "React Native", "FastAPI", "Kafka", "Cloud hosting"]
    },
    "health": {
        "summary": "Develop a patient-centric digital care platform that blends assessment, personalization, behavioural engagement, and caregiver oversight into one intelligence loop.",
        "approach": [
            "Capture daily engagement, cognitive signals, symptoms, and caregiver inputs.",
            "Use adaptive difficulty algorithms and personalised exercises to improve patient outcomes.",
            "Provide medication, hydration, and appointment reminders supported by voice and multilingual UX.",
            "Summarise trends for clinicians and caregivers with risk and adherence dashboards."
        ],
        "modules": [
            "Therapy engine",
            "Caregiver dashboard",
            "Reminder scheduler",
            "Multilingual voice assistant",
            "Progress analytics"
        ],
        "stack": ["Python", "PyTorch / TensorFlow", "React Native", "MongoDB/PostgreSQL", "Speech APIs", "FastAPI", "Cloud Hosting"]
    },
    "mining": {
        "summary": "Design an operational intelligence system that connects geological, machine, and production data to predict resource availability and schedule decisions more accurately.",
        "approach": [
            "Mine historical production, blasting, and equipment uptime data to find causal bottlenecks.",
            "Map geological indicators with remote sensing and ground survey inputs to improve reserve confidence.",
            "Forecast supply shortfalls and recommend workload balancing or rerouting of machinery.",
            "Deliver prescriptive actions through a mine operations dashboard."
        ],
        "modules": [
            "Reserve analytics engine",
            "Equipment downtime predictor",
            "Production planning dashboard",
            "Action recommendation layer",
            "Geo-visualization module"
        ],
        "stack": ["Python", "XGBoost / Random Forest", "Rasterio/GDAL", "PostGIS", "QGIS", "React", "FastAPI", "Cloud storage"]
    },
    "geospatial": {
        "summary": "Create a spatial intelligence platform that unifies parcel, cadastral, utility, survey, and governance data into a single parcel-aware digital view.",
        "approach": [
            "Fuse drone, LiDAR, parcel, and administrative records into a common geospatial layer.",
            "Apply AI for feature extraction, parcel delineation, and topology validation.",
            "Resolve conflicts using confidence scoring and quality checks before publishing outputs.",
            "Expose parcel-level APIs for departments and public-facing services."
        ],
        "modules": [
            "Feature extraction engine",
            "Topology validation layer",
            "Parcel registry portal",
            "Data harmonization service",
            "Citizen information dashboard"
        ],
        "stack": ["Python", "GeoAI / OpenCV / Detectron2", "PostGIS", "QGIS", "Leaflet", "React", "Node.js", "Cloud GIS"]
    },
    "agriculture": {
        "summary": "Build a field intelligence system that links weather, crop condition, soil health, and market signal data into an actionable advisory engine for farmers and agencies.",
        "approach": [
            "Integrate satellite and field sensor data with crop calendars and market signals.",
            "Use decision models to estimate yield risk, irrigation stress, and pest emergence.",
            "Generate field-level recommendations and digital records for extension teams.",
            "Offer multilingual advisory via mobile channels and voice assistants."
        ],
        "modules": [
            "Crop risk model",
            "Soil and weather layer",
            "Advisory engine",
            "Farmer mobile interface",
            "MIS dashboard"
        ],
        "stack": ["Python", "TensorFlow / XGBoost", "PostgreSQL", "GIS tools", "React Native", "FastAPI", "Cloud services"]
    },
    "mobility": {
        "summary": "Develop a multimodal mobility intelligence platform that predicts movement risk, improves service operation, and optimizes route decisions in real time.",
        "approach": [
            "Combine historical movement, traffic, weather, and asset data to model current and future network performance.",
            "Deliver predictive ETA, station crowding, and route disruption alerts to operators and users.",
            "Support dispatch logic and passenger communication with digital dashboards.",
            "Integrate with maintenance records and safety logs for proactive interventions."
        ],
        "modules": [
            "Predictive ETA engine",
            "Operations dashboard",
            "Passenger alert system",
            "Fleet condition monitor",
            "Incident detection layer"
        ],
        "stack": ["Python", "Time-series models", "PostgreSQL", "Kafka", "React", "Mapbox", "FastAPI", "Cloud hosting"]
    },
    "smartcity": {
        "summary": "Create a city operations platform that fuses public service data, IoT feeds, and citizen input to improve service efficiency and transparency.",
        "approach": [
            "Monitor infrastructure, service queues, energy, and mobility conditions from connected systems.",
            "Use anomaly detection and predictive analytics to flag resource imbalance and service gaps.",
            "Turn operational issues into task workflows for civic teams and field workers.",
            "Create a citizen portal for requests, visibility, and two-way updates."
        ],
        "modules": [
            "IoT monitoring layer",
            "Anomaly detection engine",
            "Task assignment dashboard",
            "Citizen service portal",
            "Performance analytics"
        ],
        "stack": ["Python", "Time series / ML", "PostgreSQL", "MQTT", "React", "Node.js", "Cloud services"]
    },
    "publicservice": {
        "summary": "Build a digital public infrastructure layer that brings fragmented data, workflows, and citizen services into a single governed, interoperable experience.",
        "approach": [
            "Normalize decentralized data into common models and identity schemes.",
            "Connect departmental workflows behind secure APIs and role-based access control.",
            "Use analytics and dashboards to reduce manual checks and improve trust in public service delivery.",
            "Add citizen-facing search, request, and status-tracking features."
        ],
        "modules": [
            "Master data model",
            "Workflow orchestration",
            "APIs and identity layer",
            "Citizen dashboard",
            "Audit and analytics module"
        ],
        "stack": ["Python", "Node.js", "PostgreSQL", "OpenAPI / REST", "React", "Keycloak", "Cloud hosting"]
    },
    "cybersecurity": {
        "summary": "Develop an intelligent security analysis engine that interprets network behaviour, protocol structures, and configuration drift to identify weaknesses before exploitation.",
        "approach": [
            "Parse traffic patterns and protocol metadata to reconstruct deployment behaviour.",
            "Use rule-based and model-based inference to identify policy mismatches or vulnerable configurations.",
            "Rank risks by impact and show remediation guidance for security teams.",
            "Provide reproducible reports for audits, compliance, and incident review."
        ],
        "modules": [
            "Packet analysis engine",
            "Protocol correlation model",
            "Risk scoring dashboard",
            "Compliance report generator",
            "Remediation advisory layer"
        ],
        "stack": ["Python", "Scapy / PyShark", "PostgreSQL", "FastAPI", "React", "PyTorch / ML", "Cloud hosting"]
    },
    "education": {
        "summary": "Create a digital learning and assessment platform that personalizes learning paths, measures engagement, and improves skill outcomes for the target population.",
        "approach": [
            "Map learner aptitude, learning pace, and behaviour to adaptive content.",
            "Track completion, misconceptions, and intervention signals in real time.",
            "Use analytics to suggest revisions, mentoring, and adaptive practice plans.",
            "Support multilingual, low-bandwidth, and offline learning experiences."
        ],
        "modules": [
            "Adaptive learning engine",
            "Assessment engine",
            "Tutor dashboard",
            "Offline sync module",
            "Progress analytics"
        ],
        "stack": ["Python", "TensorFlow / XGBoost", "React", "PostgreSQL", "Node.js", "Cloud hosting"]
    },
    "industrial": {
        "summary": "Build a predictive industrial reliability system that catches mechanical faults early and keeps operations safer and more efficient.",
        "approach": [
            "Capture vibration, temperature, process, and maintenance signals from industrial equipment.",
            "Apply anomaly detection to identify early warning patterns before failure occurs.",
            "Convert outputs into maintenance scheduling and risk-priority recommendations.",
            "Give plant teams dashboards and mobile actions for rapid response."
        ],
        "modules": [
            "Sensor ingestion",
            "Anomaly detection",
            "Maintenance scheduling",
            "Operations dashboard",
            "Work-order automation"
        ],
        "stack": ["Python", "Time-series ML", "InfluxDB / PostgreSQL", "React", "Kafka", "Cloud hosting"]
    },
    "default": {
        "summary": "Build a smart, AI-assisted platform that solves the problem through connected data, multi-stakeholder workflows, and measurable decision support.",
        "approach": [
            "Digitize the current manual workflow and capture all operational signals.",
            "Create prediction and optimization engines around the real bottleneck.",
            "Add a simple but actionable dashboard and field workflow for adoption.",
            "Use analytics and pilot feedback to improve trust and market readiness."
        ],
        "modules": [
            "Data ingestion",
            "Decision engine",
            "User workflow",
            "Analytics dashboard",
            "Pilot deployment and feedback loop"
        ],
        "stack": ["Python", "PostgreSQL", "React", "FastAPI", "Cloud hosting"]
    }
}


def classify_domain(title):
    t = title.lower()
    if any(k in t for k in ["landslide", "flood", "disaster", "earthquake", "storm", "climate", "fire", "forest"]):
        return "disaster"
    if any(k in t for k in ["logistics", "route", "transport", "vehicle", "freight", "cargo", "vessel", "port", "supply chain", "shipment", "delivery"]):
        return "logistics"
    if any(k in t for k in ["dementia", "elderly", "health", "medical", "diagnosis", "patient", "caregiver", "hospital", "therapy", "disease"]):
        return "health"
    if any(k in t for k in ["mine", "mining", "ore", "coal", "manganese", "reserve", "production shortfall", "quarry", "drill"]):
        return "mining"
    if any(k in t for k in ["land", "parcel", "cadastral", "ulpin", "gis", "geospatial", "property", "survey", "urban", "mapping", "record"]):
        return "geospatial"
    if any(k in t for k in ["farmer", "agriculture", "crop", "soil", "irrigation", "fertilizer", "harvest", "market", "farm"]):
        return "agriculture"
    if any(k in t for k in ["train", "rail", "eta", "station", "mobility", "traffic", "transportation", "road", "airport", "bus"]):
        return "mobility"
    if any(k in t for k in ["smart city", "municipal", "waste", "water", "energy", "public service", "infrastructure", "citizen", "service"]):
        return "smartcity"
    if any(k in t for k in ["security", "cyber", "vpn", "network", "protocol", "threat", "firewall", "anomaly"]):
        return "cybersecurity"
    if any(k in t for k in ["education", "exam", "student", "learning", "school", "scholarship", "teaching", "skill"]):
        return "education"
    if any(k in t for k in ["industrial", "machine", "factory", "predictive maintenance", "belt", "conveyor", "equipment", "reliability"]):
        return "industrial"
    if any(k in t for k in ["governance", "digital public", "land stack", "platform", "registry", "public infrastructure", "digital infrastructure"]):
        return "publicservice"
    return "default"


def build_unique_idea(title, code):
    domain = classify_domain(title)
    pattern = COMMON_PATTERNS.get(domain, COMMON_PATTERNS["default"])
    title_clean = re.sub(r'\s+', ' ', title).strip()
    strong_value = "".join(
        [
            "- Business value: reduce response time, improve trust, and create operational visibility for decision-makers.\n",
            "- Government value: improve citizen service delivery, reduce manual workload, and create auditable digital workflows.\n",
            "- Technical value: combine AI, geospatial intelligence, automation, and user workflows into one deployable system.\n"
        ]
    )

    bullet_list = "\n".join([f"- {item}" for item in pattern["approach"]])
    modules = "\n".join([f"- {m}" for m in pattern["modules"]])
    stack = ", ".join(pattern["stack"])
    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>{title_clean} | SIH Solution Idea</title>
  <style>
    body {{ font-family: Arial, sans-serif; line-height: 1.7; margin: 0 auto; max-width: 1100px; padding: 32px 20px 80px; color: #111827; background: #f8fafc; }}
    h1, h2, h3 {{ color: #0f172a; }}
    h1 {{ border-bottom: 3px solid #2563eb; padding-bottom: 10px; margin-bottom: 18px; }}
    h2 {{ margin-top: 30px; }}
    .meta {{ background: #fff; border: 1px solid #dbeafe; border-radius: 10px; padding: 18px 20px; margin-bottom: 20px; }}
    .badge {{ display: inline-block; background: #dbeafe; color: #1d4ed8; padding: 5px 10px; border-radius: 999px; font-size: 12px; font-weight: bold; margin-right: 8px; margin-bottom: 8px; }}
    ul {{ padding-left: 22px; }}
    li {{ margin-bottom: 8px; }}
    code {{ background: #eef2ff; padding: 3px 6px; border-radius: 5px; }}
    .back-link {{ margin-top: 30px; display: inline-block; text-decoration: none; color: #1d4ed8; font-weight: bold; }}
  </style>
</head>
<body>
  <h1>{title_clean}</h1>
  <div class=\"meta\">
    <div><span class=\"badge\">PS ID</span> {code}</div>
    <div><span class=\"badge\">Domain</span> {domain.title()}</div>
    <div><span class=\"badge\">Core strategy</span> {pattern['summary']}</div>
  </div>

  <h2>1. Problem framing</h2>
  <p>
    This problem is not just about digitizing a manual process; the real challenge is creating a system that is intelligent, transparent, and usable in the actual operating environment. In SIH, the winning idea usually solves two things at the same time: it reduces effort for the institutions and it creates measurable public or operational value for the end user.
  </p>
  <p>
    For this statement, the best approach is to combine data capture, AI-based prediction, workflow automation, and citizen/field reporting into a single story. The platform should be built around a clear failure point: delayed decisions, poor visibility, fragmented data, unsafe operations, or weak service delivery.
  </p>

  <h2>2. What makes this unique</h2>
  <ul>
    <li>Use real operational signals instead of only static forms or dashboard mockups.</li>
    <li>Make the system decision-supportive rather than just report-generating.</li>
    <li>Provide a field-to-dashboard workflow so administrators, field teams, and users stay connected.</li>
    <li>Use AI as a decision assistant, not as a black-box model with no operational meaning.</li>
    <li>Design for usability in low-connectivity, multilingual, or rapidly changing field settings.</li>
  </ul>

  <h2>3. Recommended solution approach</h2>
  <ul>
    {bullet_list}
  </ul>

  <h2>4. High-impact architecture</h2>
  <ul>
    <li><strong>Data Ingestion Layer:</strong> ingest government data, sensor feeds, satellite imagery, public reports, field updates, and historical records.</li>
    <li><strong>Data Standardization Layer:</strong> clean, map, normalize, and validate data across formats, geographies, and departments.</li>
    <li><strong>AI & Decision Engine:</strong> build predictive models, anomaly detection, optimization algorithms, and prioritization layers.</li>
    <li><strong>Workflow Layer:</strong> convert predictions into tasks, alerts, service requests, or operational actions.</li>
    <li><strong>Dashboards and Interfaces:</strong> administrator console, field app, citizen portal, or mobile app depending on the use case.</li>
    <li><strong>Feedback Loop:</strong> collect outcomes, corrections, and user feedback to continuously improve predictions and trust.</li>
  </ul>

  <h2>5. Core modules to build</h2>
  <ul>
    {modules}
  </ul>

  <h2>6. Minimum viable product (MVP)</h2>
  <ul>
    <li>Gather 2-3 sources of real data and build a pilot dataset for one geography or one use case.</li>
    <li>Implement one reliable prediction or optimization model with visible output such as risk score, route score, anomaly alert, or recommendation.</li>
    <li>Build one user-facing dashboard or mobile flow for decision-making.</li>
    <li>Add role-based access, alerting, and a feedback form for administrators or field teams.</li>
    <li>Show measurable performance improvement: faster decisions, lower cost, fewer errors, or less delay.</li>
  </ul>

  <h2>7. Suggested tech stack</h2>
  <ul>
    <li>{stack}</li>
  </ul>

  <h2>8. What to measure as success</h2>
  <ul>
    <li>Accuracy or prediction improvement against a baseline.</li>
    <li>Reduction in manual effort or turnaround time.</li>
    <li>Improvement in decision quality, service coverage, or operational safety.</li>
    <li>Higher user adoption, trust, and response rate from field teams or citizens.</li>
    <li>Ability to scale from a pilot region to a larger district, state, or national deployment.</li>
  </ul>

  <h2>9. Practical SIH pitch</h2>
  <p>
    The strongest SIH pitch is not “we built an AI solution” but “we built a deployable decision-support system that improves outcomes in a real public or industrial problem and can scale with government or enterprise adoption.”
  </p>
  <p>
    Make the demo feel tangible: show live data, one risk event or route change, and a clear result from the system. If a live dataset is not available, simulate realistic data and show how the model behaves under edge conditions.
  </p>

  <h2>10. Extra innovation ideas</h2>
  <ul>
    <li>Add multilingual alerts and support for low-network environments.</li>
    <li>Include explainable AI so users understand why a recommendation was made.</li>
    <li>Connect to digital public infrastructure, government APIs, or operational workflows.</li>
    <li>Use a human-in-the-loop model so domain experts can verify and improve outputs.</li>
    <li>Include cost-benefit estimate for deployment at district or state scale.</li>
  </ul>

  <h2>11. Impact</h2>
  {strong_value}

  <a class=\"back-link\" href=\"../index.html\">← Back to problem list</a>
</body>
</html>
"""


# For each problem title, generate a specific file
html = INDEX_PATH.read_text(encoding='utf-8')
pattern = re.compile(r'<h2>(.*?)</h2>', re.DOTALL)

# Keep as a working pass to avoid duplicate insertion if script is re-run
if not (OUT_DIR / 'README.md').exists():
    (OUT_DIR / 'README.md').write_text('Generated solution idea files for SIH 2026 problem statements.\n', encoding='utf-8')


def get_code_from_title(header_text):
    m = re.search(r'(SIH\d+)', header_text, re.I)
    return m.group(1) if m else None


def add_links_to_index(index_html):
    def repl(match):
        header = match.group(0)
        title_text = match.group(1)
        code = get_code_from_title(title_text)
        if not code:
            return header
        file_name = f"{code}.html"
        link = f"<p class=\"ps-idea-link\"><a href=\"solution_ideas/{file_name}\" target=\"_blank\" rel=\"noopener\">Open detailed solution idea</a></p>"
        return f"{header}\n{link}"
    return pattern.sub(repl, index_html)


# Build files first
seen = set()
for m in pattern.finditer(html):
    title_text = m.group(1)
    code = get_code_from_title(title_text)
    if not code or code in seen:
        continue
    seen.add(code)
    content = build_unique_idea(title_text, code)
    (OUT_DIR / f"{code}.html").write_text(content, encoding='utf-8')

# Update index with links after all h2 headings
new_html = add_links_to_index(html)
INDEX_PATH.write_text(new_html, encoding='utf-8')

print(f"Generated {len(seen)} solution idea files in {OUT_DIR}")
print("Index updated with links after each problem statement.")
