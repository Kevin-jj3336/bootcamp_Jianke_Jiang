# NYC Citi Bike Forecast
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
A common problem New York City residents face is that the public Citi Bike system frequently experiences shortages at popular docking stations during commuting hours. Riders often find that stations either have no available bikes or no open docks to return their bikes. This problem not only hurts the user experience but also discourages more citizens from adopting Citi Bike as a regular transportation option.

Citi Bike offers a more sustainable alternative to other forms of transportation and can help to ease heavy traffic in New York City during peak commuting hours. Therefore, reliable bike availability is crucial. Addressing this issue would support reduced traffic congestion, improve public health, encourage broader adoption of bike sharing, and lower carbon emissions. Predicting bike availability and determining the best strategy for rebalancing docks and bikes in real time could ensure the system operates more efficiently and is able to provide more bikes to users when and where they are needed.


## Stakeholder & User
Stakeholder: NYC Department of Transportation and Lyft (company behind the Citi Bike Program). They decide on bike redistribution strategies and infrastructure investment/allocation.

User 1: Citi Bike operations team — they will use the forecast results from the model to execute real-time rebalancing among all docks.
User 2: Citi Bike riders — they benefit from better bike and dock availability.

Timing & Workflow Context: Predictions and recommendations should be updated at most every 10 minutes for the rebalancing team to react to peak demand periods. The rebalancing strategy should also consider the approximate travel time for the team to carry bikes from one station to the next.

## Useful Answer & Decision
- **Type:** Predictive — we want to forecast bikes and dock availability at each station up to 45 minutes in advance.  
- **Decision Supported:** Where and when to move bikes to prevent shortages and full stations.  
- **Metrics:**  
  1. Prediction accuracy (e.g., Standard Error).  
  2. Operational utility (measured by reduction in frequency of shortage events compared to past).  
- **Artifact:** An API showing station-level forecasts refreshing at least every 10 minutes, with redistribution recommendations for the Citi Bike team.  

## Assumptions & Constraints

- Historical and real-time Citi Bike station status is accessible through some API with low latency and high accuracy.  
- Weather and event data are available for modeling seasonality effects.  
- Riding patterns remain reasonably consistent on days with similar conditions.  
- Limited resources such as number of bikes and staff may prevent perfect rebalancing.  
- Predictions must be generated and refreshed at high speed.  
- A powerful synchronous system is necessary to coordinate between stations, servers, and teams.  

## Known Unknowns / Risks

### Known Unknowns
- Factors like weather, events, and transit disruptions may impact bike demand across different areas.  
- Rider behavior may shift over time.  

### Risks & Mitigation
1. **Risk:** Real-time data feed may experience downtime or delays.  
   **Mitigation:** Implement data caching and fallback to recent historical patterns when live data is unavailable.  

2. **Risk:** Data overfitting to past events that have lost predictive power.  
   **Mitigation:** Consistently monitor and regularly validate the model with the latest data.  

3. **Risk:** Resource limitations (bikes and staff) may prevent acting on predictions.  
   **Mitigation:** Incorporate resource constraints and likelihood of action failure into optimization planning.  



## Lifecycle Mapping
Goal → Stage → Deliverable
- 1: Identify shortage patterns and key demand drivers → Problem Framing & Scoping (Stage 01) → Problem statement, stakeholder memo, and initial exploratory analysis.
- 2: Gather and clean historical and real-time Citi Bike data → Data Collection & Cleaning (Stage 02) → Cleaned datasets with integrated weather and event data.
- 3: Forecast bike and dock availability at each station → Modeling & Evaluation (Stage 03) → Predictive model, performance metrics, and validation results.
- 4: Report real-time bike redistribution strategy → Deployment & Monitoring (Stage 04) → Operational dashboard or API with live predictions and suggested actions.


## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates