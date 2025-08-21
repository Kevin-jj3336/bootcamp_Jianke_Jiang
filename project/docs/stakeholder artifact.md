# Stakeholder Memo — Citi Bike Availability Forecasting

**To:** NYC Department of Transportation & Lyft (Citi Bike Operations)  
**From:** Jianke Jiang
**Date:** August 2025  
**Subject:** Improving Citi Bike Availability through Predictive Modeling

---

## 1. Background
Citi Bike is a key part of New York City’s sustainable transportation network.  
However, during peak commuting hours, popular stations often have:
- **No bikes available** for riders to take, or
- **No empty docks** for returning bikes.

These shortages and overflows reduce rider satisfaction and discourage adoption of bike-sharing as a daily commuting option.

---

## 2. Problem
Unbalanced bike and dock availability:
- Causes delays for commuters.
- Reduces system reliability.
- Limits the environmental and congestion-reduction benefits of bike sharing.

---

## 3. Proposed Solution
We propose building a **Forecasting model** to predict number of bike and dock availability at each station **up to 45 minutes in advance**.  
Key features:
- **Live data integration** from Citi Bike APIs.
- Inclusion of **weather and event data** for demand forecasting.
- **Automated recommendations** for redistribution crews.

---

## 4. Benefits to Stakeholders
- **Improved rider satisfaction** → more consistent availability.
- **Optimized operations** → better use of limited staff and bike resources.
- **Environmental impact** → higher adoption rates lead to fewer car trips.
- **Data-driven planning** → insights for future station expansions.

---

## 5. Deliverables
- **Operational Dashboard/API**: Station-level forecasts, updated every 10 minutes.
- **Redistribution Recommendations**: Priority list of stations needing bikes/docks.
- **Performance Metrics**: Prediction accuracy (e.g., Standard Error) and operational utility (reduction in shortage events).

---

## 6. Next Steps
1. Gather and clean historical + real-time data.
2. Develop and validate the predictive model.
3. Deploy dashboard/API for live operational use.
4. Monitor and iterate based on field performance.

---

**Contact:** jj3336@nyu.edu