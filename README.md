[README.md](https://github.com/user-attachments/files/23093025/README.md)
# Country Relocation AI Agent

An intelligent Python agent that helps you find the best country to move to based on your specific criteria and priorities.

## Features

- **Customizable Criteria**: Weight different factors based on your priorities
- **Minimum Requirements**: Set hard requirements that countries must meet
- **Multiple Scenarios**: Pre-built examples for digital nomads, families, and retirees
- **Detailed Explanations**: Get breakdowns of why each country was recommended
- **Extensible Database**: Easy to add more countries or update data

## Quick Start

```python
from country_relocation_agent import CountryRelocationAgent, UserCriteria

# Create the agent
agent = CountryRelocationAgent()

# Define your criteria
my_criteria = UserCriteria(
    weights={
        'cost_of_living_index': 0.20,
        'quality_of_life_index': 0.20,
        'safety_index': 0.15,
        'healthcare_index': 0.15,
        'climate_score': 0.10,
        'job_market_score': 0.10,
        'english_proficiency': 0.05,
        'visa_ease': 0.05,
        'tax_friendliness': 0.00
    },
    min_requirements={
        'safety_index': 70,
        'healthcare_index': 65
    }
)

# Get recommendations
recommendations = agent.recommend_countries(my_criteria, top_n=5)

# Display results
for i, (country, score, breakdown) in enumerate(recommendations, 1):
    print(f"\n#{i} Recommendation:")
    print(agent.explain_recommendation(country, score, breakdown))
```

## Available Criteria

### Weightable Factors
All factors are scored 0-100 (higher is better, except cost of living where lower is better):

- **cost_of_living_index**: Living expenses (lower = cheaper)
- **quality_of_life_index**: Overall quality of life
- **safety_index**: Personal safety and crime rates
- **healthcare_index**: Healthcare quality and accessibility
- **climate_score**: Weather and climate quality
- **job_market_score**: Employment opportunities
- **english_proficiency**: English language prevalence
- **visa_ease**: Ease of obtaining residence visa
- **tax_friendliness**: Tax rates and complexity (higher = lower taxes)

### Other Metrics
- **internet_speed**: Average internet speed in Mbps
- **expat_community_size**: Small, Medium, or Large

## Customization Examples

### Example 1: Digital Nomad
Priorities: Low cost, good internet, easy visa

```python
nomad_criteria = UserCriteria(
    weights={
        'cost_of_living_index': 0.25,
        'quality_of_life_index': 0.15,
        'safety_index': 0.15,
        'climate_score': 0.15,
        'visa_ease': 0.10,
        'healthcare_index': 0.10,
        'english_proficiency': 0.08,
        'job_market_score': 0.02,
        'tax_friendliness': 0.00
    },
    min_requirements={
        'internet_speed': 80,
        'safety_index': 60
    }
)
```

### Example 2: Family with Children
Priorities: Safety, healthcare, quality schools

```python
family_criteria = UserCriteria(
    weights={
        'safety_index': 0.25,
        'quality_of_life_index': 0.25,
        'healthcare_index': 0.20,
        'job_market_score': 0.10,
        'cost_of_living_index': 0.10,
        'climate_score': 0.05,
        'english_proficiency': 0.05,
        'visa_ease': 0.00,
        'tax_friendliness': 0.00
    },
    min_requirements={
        'safety_index': 75,
        'healthcare_index': 70,
        'quality_of_life_index': 70
    }
)
```

### Example 3: Early Retiree
Priorities: Low cost, good healthcare, warm climate

```python
retiree_criteria = UserCriteria(
    weights={
        'cost_of_living_index': 0.30,
        'healthcare_index': 0.20,
        'climate_score': 0.15,
        'safety_index': 0.15,
        'quality_of_life_index': 0.15,
        'english_proficiency': 0.05,
        'job_market_score': 0.00,
        'visa_ease': 0.00,
        'tax_friendliness': 0.00
    },
    min_requirements={
        'healthcare_index': 60,
        'safety_index': 65
    }
)
```

### Example 4: Tech Professional
Priorities: Job market, quality of life, tech ecosystem

```python
tech_criteria = UserCriteria(
    weights={
        'job_market_score': 0.25,
        'quality_of_life_index': 0.20,
        'safety_index': 0.15,
        'healthcare_index': 0.15,
        'english_proficiency': 0.10,
        'cost_of_living_index': 0.10,
        'tax_friendliness': 0.05,
        'visa_ease': 0.00,
        'climate_score': 0.00
    },
    min_requirements={
        'internet_speed': 100,
        'job_market_score': 70
    }
)
```

## Adding New Countries

To add a new country to the database, add a `CountryData` object to the `_initialize_country_database()` method:

```python
CountryData(
    name="Your Country",
    cost_of_living_index=50,  # 0-100
    quality_of_life_index=75,
    safety_index=80,
    healthcare_index=72,
    climate_score=85,
    job_market_score=70,
    english_proficiency=65,
    visa_ease=75,
    tax_friendliness=60,
    internet_speed=120,  # Mbps
    expat_community_size="Medium"  # Small/Medium/Large
)
```

## Understanding the Weights

Weights should add up to 1.0 (100%) and represent how important each factor is to you:

- **0.00**: Not important at all
- **0.05**: Slightly important
- **0.10**: Moderately important
- **0.15**: Important
- **0.20**: Very important
- **0.25+**: Extremely important

## Minimum Requirements

Set minimum thresholds that countries MUST meet. Any country below these thresholds will be automatically excluded:

```python
min_requirements={
    'safety_index': 70,      # Must be at least 70/100
    'internet_speed': 50,    # Must have at least 50 Mbps
    'healthcare_index': 65   # Must be at least 65/100
}
```

## Current Country Database

The agent includes data for 12 countries:
- Portugal
- Spain
- Thailand
- Germany
- Mexico
- Canada
- Australia
- Estonia
- New Zealand
- Costa Rica
- Singapore
- Czech Republic

## Extending the Agent

### Add More Criteria

To add a new criterion:

1. Add it to the `CountryData` dataclass
2. Add default weight in `UserCriteria.__post_init__`
3. Update the `criteria_names` dictionary in `explain_recommendation()`
4. Update all country entries with the new field

### Connect to Real Data Sources

You can modify the agent to pull live data from APIs:

```python
def fetch_country_data(country_name):
    """Fetch real-time data from APIs"""
    # Numbeo API for cost of living
    # World Bank API for economic data
    # etc.
    pass
```

## Tips for Best Results

1. **Be Realistic**: Don't set all weights to maximum importance
2. **Prioritize**: Focus on your top 3-4 most important factors
3. **Use Minimums Sparingly**: Too many requirements might exclude all countries
4. **Test Different Scenarios**: Try various weight combinations
5. **Update Data**: Country data changes over time - keep it current

## License

This code is provided as-is for personal and educational use.
