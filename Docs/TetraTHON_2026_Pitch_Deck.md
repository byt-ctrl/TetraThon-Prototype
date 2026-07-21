# AgriTech — TetraTHON 2026 Pitch Deck

> **Precision Crop Advisory & Post-Harvest Decision Intelligence**

---

## Slide 1: Title & Project Overview

### **AgriTech**
*Empowering Smallholder Farmers with Data-Driven Crop Advisory & Post-Harvest Optimization*

* **Event:** TetraTHON 2026 Hackathon
* **Track:** Precision Agriculture & AgriTech Innovation
* **Phase:** Phase 0 Pre-Screening Prototype
* **Team:** Om B Patel, Mithil Desai, Dhruvin Patel, Saumya Thakur

---

## Slide 2: The Problem

### **India's Smallholder Farmers Face Two Critical Challenges**

**1. In-Season Yield Loss (20–30% penalty)**
* 85% of Indian farmers operate on less than 2 hectares
* Generic farming advice ignores local crop growth stages and 7-day weather forecasts
* Results in over-watering, misplaced fertilizer applications, and missed pest alerts

**2. Post-Harvest Produce Waste (15–20% loss)**
* Farmers lack data-driven tools for timing sales
* No visibility into spoilage decay across storage types
* No comparison of transport costs vs. market prices across regions

**3. Market Price Asymmetry**
* Farmers sell at the nearest APMC without knowing price differences in neighboring markets
* Leaves money on the table every harvest season

---

## Slide 3: Our Solution — Dual Intelligence Engine

### **One Platform, Two Powerful Modules**

```
                     ┌────────────────────────────────┐
                     │        AgriTech Engine         │
                     └───────────────┬────────────────┘
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
┌─────────────────────────────────┐             ┌─────────────────────────────────┐
│   Module A: Crop Advisory      │             │   Module B: Post-Harvest       │
│   - Stage-Specific Advice      │             │   - Spoilage Forecasting       │
│   - Weather-Aware Rules        │             │   - Transport Cost Analysis    │
│   - Ranked Action Items        │             │   - Market Price Comparison    │
└─────────────────────────────────┘             └─────────────────────────────────┘
```

**Module A — Precision Crop Advisory:**
* Identifies current growth stage from sowing date
* Generates 3 ranked advisories: irrigation, fertiliser, pest/disease alerts
* Each advisory includes confidence level (High/Medium/Low) and plain-language explanation

**Module B — Post-Harvest Loss Planner:**
* Calculates expected returns for Sell Now, Store 14 Days, or Transport to Best Market
* Uses spoilage decay curves and Haversine distance-based transport costs
* Visualizes 30-day value retention and 90-day price trends

---

## Slide 4: How It Works — User Flow

### **Simple Inputs, Powerful Outputs**

**Step 1: Farmer Enters Basic Information**
* Location (pin/GPS), Crop type, Sowing date, Recent weather, Quantity, Storage condition

**Step 2: System Processes Data**
* Fetches 7-day weather forecast (live or mocked)
* Runs crop-stage rules against current conditions
* Pulls mandi prices and computes spoilage/transport costs

**Step 3: Farmer Receives Actionable Advice**
* **Advisory:** "Water your crop today — soil moisture is low and no rain expected for 3 days"
* **Decision:** "Sell now at Ahmedabad APMC for ₹62,000 or transport to Surat for ₹63,862"

---

## Slide 5: Live Product Demo

### **Unified Intelligence Dashboard**

* **Single-Intake Form:** Select location, crop, sowing date, weather, quantity, and storage
* **4 Quick Demo Presets:** One-click scenarios for Cotton, Wheat, Groundnut, and Tomato
* **Side-by-Side Results:** Both advisory and post-harvest recommendations on one screen

**Interactive Visualizations:**
* Spoilage Decay Chart: 30-day value curves for Open Field, Warehouse, and Cold Storage
* Price Trend Chart: 90-day APMC mandi prices showing market arbitrage opportunities

---

## Slide 6: Real-World Impact

### **Quantifiable Benefits for Farmers**

| Crop Scenario | Baseline (Sell Now) | Recommended Strategy | Net Gain |
|---------------|---------------------|----------------------|----------|
| **Cotton (Anand, 10q)** | ₹62,000 | Transport to Surat APMC | **+₹1,862** |
| **Wheat (Ahmedabad, 25q)** | ₹60,000 | Store 14 Days (Cold Storage) | **+₹3,250** |
| **Tomato (Surat, 15q)** | ₹29,250 | Sell Now (Prevent Spoilage) | **Avoids ₹8,500 loss** |

**Distribution Model:**
* Low-bandwidth web app deployable via Farmer Producer Organizations (FPOs) & Krishi Vigyan Kendras (KVKs)
* No app installation required — works on any smartphone browser

---

## Slide 7: Technical Approach

### **Lightweight, Fast, and Scalable**

**Built for Speed and Reliability:**
* Rule-based engine — fast to build, easy to explain, no training data needed
* Mocked data with seamless live API upgrade path (no UI changes required)
* SQLite database for quick prototyping, PostgreSQL for production

**Coverage:**
* 4 crop types: Cotton, Wheat, Groundnut, Tomato
* 5 Gujarat APMC markets: Ahmedabad, Surat, Vadodara, Rajkot, Anand
* 20 crop-location combinations tested end-to-end

**Graceful Degradation:**
* If live API fails, system automatically uses cached/mocked data
* No error screens — farmer always gets a recommendation

---

## Slide 8: Scalability Roadmap

### **From Prototype to National Impact**

**Phase 0 — Prototype (Current):**
* Working demo with mocked weather and price data
* Rule-based advisory and decision engine
* Deployed and live for evaluation

**Phase 1 — Hackathon MVP (Week 2):**
* Live OpenWeatherMap & Agmarknet API integration
* Leaf-disease photo classifier using lightweight AI
* SMS/WhatsApp price threshold alerts

**Phase 2 — Pilot Rollout (Month 1–3):**
* WhatsApp Bot integration for low-literacy farmers
* Multi-tenant FPO agent portals
* Real farmer feedback loop

**Phase 3 — Enterprise Scale (Month 3–12):**
* Cloud microservices architecture
* Mobile app for offline-first access
* Multi-partner FPO/KVK onboarding

---

## Slide 9: Market Fit & Viability

### **Built for India's 150M+ Smallholder Farmers**

**Target Users:**
* Primary: Smallholder farmers (under 2 hectares)
* Secondary: FPO/KVK field agents managing multiple farmers
* Distribution: Through existing agricultural extension networks

**Why This Works:**
* **Low barrier:** Web app works on any smartphone, no installation
* **Low cost:** Uses free/open data sources with paid API upgrade path
* **High trust:** Plain-language output in regional languages
* **Proven need:** 15–20% post-harvest loss is a documented, quantifiable problem

**Scalability:**
* Modular architecture — swap mock data for live APIs without rebuilding
* FPO/KVK distribution channel reaches millions of farmers
* Phase 3 multi-partner support enables rapid expansion

---

## Slide 10: Call to Action

### **Join Us in Empowering India's Farmers**

**What We've Built:**
* Working prototype with both advisory and post-harvest modules
* Live demo at [INSERT LINK]
* GitHub repository with complete codebase

**What We Need:**
* Selection into TetraTHON 2026 hackathon
* Access to live weather and market price APIs
* Partnership with FPOs/KVKs for pilot testing

**Expected Impact:**
* Reduce post-harvest losses by 10–15% for pilot farmers
* Increase farmer income by ₹2,000–5,000 per season per hectare
* Create a replicable model for agricultural extension nationwide

---

*— Thank You —*
*Team AgriTech | TetraTHON 2026*
