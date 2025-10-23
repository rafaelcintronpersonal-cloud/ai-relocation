"""
AI Agent for Country Relocation Recommendation
This agent helps users find the best country to move to based on their specific criteria.
"""

import json
from typing import Dict, List, Tuple
from dataclasses import dataclass, field


@dataclass
class CountryData:
    """Stores comprehensive data about a country"""
    name: str
    cost_of_living_index: float  # 0-100, lower is cheaper
    quality_of_life_index: float  # 0-100, higher is better
    safety_index: float  # 0-100, higher is safer
    healthcare_index: float  # 0-100, higher is better
    climate_score: float  # 0-100, higher is better weather
    job_market_score: float  # 0-100, higher is better opportunities
    english_proficiency: float  # 0-100, higher means better English
    visa_ease: float  # 0-100, higher means easier to get visa
    tax_friendliness: float  # 0-100, higher means lower taxes
    internet_speed: float  # Mbps average
    expat_community_size: str  # Small, Medium, Large
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'cost_of_living_index': self.cost_of_living_index,
            'quality_of_life_index': self.quality_of_life_index,
            'safety_index': self.safety_index,
            'healthcare_index': self.healthcare_index,
            'climate_score': self.climate_score,
            'job_market_score': self.job_market_score,
            'english_proficiency': self.english_proficiency,
            'visa_ease': self.visa_ease,
            'tax_friendliness': self.tax_friendliness,
            'internet_speed': self.internet_speed,
            'expat_community_size': self.expat_community_size
        }


@dataclass
class UserCriteria:
    """User's preferences and priorities for relocation"""
    weights: Dict[str, float] = field(default_factory=dict)
    min_requirements: Dict[str, float] = field(default_factory=dict)
    preferred_regions: List[str] = field(default_factory=list)
    deal_breakers: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        # Default weights if none provided
        if not self.weights:
            self.weights = {
                'cost_of_living_index': 0.15,
                'quality_of_life_index': 0.20,
                'safety_index': 0.15,
                'healthcare_index': 0.10,
                'climate_score': 0.10,
                'job_market_score': 0.10,
                'english_proficiency': 0.05,
                'visa_ease': 0.10,
                'tax_friendliness': 0.05
            }


class CountryRelocationAgent:
    """AI Agent for recommending countries based on user criteria"""
    
    def __init__(self):
        self.countries = self._initialize_country_database()
        
    def _initialize_country_database(self) -> List[CountryData]:
        """Initialize database with sample country data"""
        return [
            CountryData(
                name="Portugal",
                cost_of_living_index=45,
                quality_of_life_index=75,
                safety_index=82,
                healthcare_index=72,
                climate_score=85,
                job_market_score=60,
                english_proficiency=65,
                visa_ease=75,
                tax_friendliness=60,
                internet_speed=95,
                expat_community_size="Large"
            ),
            CountryData(
                name="Spain",
                cost_of_living_index=50,
                quality_of_life_index=78,
                safety_index=80,
                healthcare_index=78,
                climate_score=88,
                job_market_score=58,
                english_proficiency=60,
                visa_ease=72,
                tax_friendliness=55,
                internet_speed=110,
                expat_community_size="Large"
            ),
            CountryData(
                name="Thailand",
                cost_of_living_index=30,
                quality_of_life_index=68,
                safety_index=70,
                healthcare_index=65,
                climate_score=75,
                job_market_score=55,
                english_proficiency=50,
                visa_ease=85,
                tax_friendliness=70,
                internet_speed=85,
                expat_community_size="Large"
            ),
            CountryData(
                name="Germany",
                cost_of_living_index=65,
                quality_of_life_index=85,
                safety_index=85,
                healthcare_index=88,
                climate_score=65,
                job_market_score=82,
                english_proficiency=70,
                visa_ease=60,
                tax_friendliness=45,
                internet_speed=120,
                expat_community_size="Large"
            ),
            CountryData(
                name="Mexico",
                cost_of_living_index=35,
                quality_of_life_index=65,
                safety_index=55,
                healthcare_index=60,
                climate_score=80,
                job_market_score=60,
                english_proficiency=45,
                visa_ease=90,
                tax_friendliness=65,
                internet_speed=70,
                expat_community_size="Large"
            ),
            CountryData(
                name="Canada",
                cost_of_living_index=70,
                quality_of_life_index=88,
                safety_index=88,
                healthcare_index=85,
                climate_score=60,
                job_market_score=80,
                english_proficiency=95,
                visa_ease=55,
                tax_friendliness=50,
                internet_speed=130,
                expat_community_size="Large"
            ),
            CountryData(
                name="Australia",
                cost_of_living_index=75,
                quality_of_life_index=90,
                safety_index=87,
                healthcare_index=87,
                climate_score=85,
                job_market_score=78,
                english_proficiency=100,
                visa_ease=50,
                tax_friendliness=55,
                internet_speed=110,
                expat_community_size="Large"
            ),
            CountryData(
                name="Estonia",
                cost_of_living_index=48,
                quality_of_life_index=72,
                safety_index=82,
                healthcare_index=70,
                climate_score=55,
                job_market_score=72,
                english_proficiency=75,
                visa_ease=80,
                tax_friendliness=75,
                internet_speed=150,
                expat_community_size="Medium"
            ),
            CountryData(
                name="New Zealand",
                cost_of_living_index=72,
                quality_of_life_index=87,
                safety_index=90,
                healthcare_index=82,
                climate_score=82,
                job_market_score=70,
                english_proficiency=100,
                visa_ease=52,
                tax_friendliness=58,
                internet_speed=105,
                expat_community_size="Medium"
            ),
            CountryData(
                name="Costa Rica",
                cost_of_living_index=40,
                quality_of_life_index=70,
                safety_index=68,
                healthcare_index=72,
                climate_score=88,
                job_market_score=58,
                english_proficiency=52,
                visa_ease=88,
                tax_friendliness=68,
                internet_speed=75,
                expat_community_size="Large"
            ),
            CountryData(
                name="Singapore",
                cost_of_living_index=85,
                quality_of_life_index=92,
                safety_index=95,
                healthcare_index=92,
                climate_score=70,
                job_market_score=88,
                english_proficiency=85,
                visa_ease=65,
                tax_friendliness=80,
                internet_speed=200,
                expat_community_size="Large"
            ),
            CountryData(
                name="Czech Republic",
                cost_of_living_index=42,
                quality_of_life_index=74,
                safety_index=80,
                healthcare_index=75,
                climate_score=68,
                job_market_score=70,
                english_proficiency=65,
                visa_ease=70,
                tax_friendliness=65,
                internet_speed=115,
                expat_community_size="Medium"
            ),
        ]
    
    def calculate_score(self, country: CountryData, criteria: UserCriteria) -> Tuple[float, Dict[str, float]]:
        """
        Calculate weighted score for a country based on user criteria
        Returns total score and breakdown by category
        """
        scores = {}
        total_score = 0
        
        for criterion, weight in criteria.weights.items():
            if hasattr(country, criterion):
                raw_value = getattr(country, criterion)
                
                # Invert cost of living (lower is better)
                if criterion == 'cost_of_living_index':
                    normalized_value = 100 - raw_value
                else:
                    normalized_value = raw_value
                
                # Check minimum requirements
                if criterion in criteria.min_requirements:
                    if raw_value < criteria.min_requirements[criterion]:
                        return 0, {}  # Fails minimum requirement
                
                weighted_score = normalized_value * weight
                scores[criterion] = weighted_score
                total_score += weighted_score
        
        return total_score, scores
    
    def filter_countries(self, criteria: UserCriteria) -> List[CountryData]:
        """Filter countries based on deal-breakers and minimum requirements"""
        filtered = []
        
        for country in self.countries:
            # Check minimum requirements
            meets_requirements = True
            for criterion, min_value in criteria.min_requirements.items():
                if hasattr(country, criterion):
                    if getattr(country, criterion) < min_value:
                        meets_requirements = False
                        break
            
            if meets_requirements:
                filtered.append(country)
        
        return filtered
    
    def recommend_countries(self, criteria: UserCriteria, top_n: int = 5) -> List[Tuple[CountryData, float, Dict]]:
        """
        Main method: Recommend top countries based on criteria
        Returns list of (country, score, breakdown) tuples
        """
        # Filter countries
        eligible_countries = self.filter_countries(criteria)
        
        # Calculate scores
        scored_countries = []
        for country in eligible_countries:
            score, breakdown = self.calculate_score(country, criteria)
            if score > 0:  # Only include countries that passed all checks
                scored_countries.append((country, score, breakdown))
        
        # Sort by score
        scored_countries.sort(key=lambda x: x[1], reverse=True)
        
        return scored_countries[:top_n]
    
    def explain_recommendation(self, country: CountryData, score: float, breakdown: Dict) -> str:
        """Generate human-readable explanation for recommendation"""
        explanation = f"\n{'='*60}\n"
        explanation += f"Country: {country.name}\n"
        explanation += f"Overall Score: {score:.2f}/100\n"
        explanation += f"{'='*60}\n\n"
        
        explanation += "Score Breakdown:\n"
        explanation += "-" * 60 + "\n"
        
        criteria_names = {
            'cost_of_living_index': 'Cost of Living (inverted)',
            'quality_of_life_index': 'Quality of Life',
            'safety_index': 'Safety',
            'healthcare_index': 'Healthcare',
            'climate_score': 'Climate',
            'job_market_score': 'Job Market',
            'english_proficiency': 'English Proficiency',
            'visa_ease': 'Visa Accessibility',
            'tax_friendliness': 'Tax Friendliness'
        }
        
        for criterion, weighted_score in sorted(breakdown.items(), key=lambda x: x[1], reverse=True):
            display_name = criteria_names.get(criterion, criterion)
            explanation += f"  {display_name:.<40} {weighted_score:>6.2f}\n"
        
        explanation += "\nKey Statistics:\n"
        explanation += "-" * 60 + "\n"
        explanation += f"  Cost of Living Index: {country.cost_of_living_index}/100 (lower is cheaper)\n"
        explanation += f"  Safety Index: {country.safety_index}/100\n"
        explanation += f"  Healthcare Index: {country.healthcare_index}/100\n"
        explanation += f"  Average Internet Speed: {country.internet_speed} Mbps\n"
        explanation += f"  Expat Community: {country.expat_community_size}\n"
        
        return explanation


def main():
    """Example usage of the Country Relocation Agent"""
    
    print("🌍 Country Relocation AI Agent")
    print("=" * 60)
    
    # Create agent
    agent = CountryRelocationAgent()
    
    # Example 1: Digital Nomad
    print("\n\n📱 SCENARIO 1: Digital Nomad")
    print("-" * 60)
    nomad_criteria = UserCriteria(
        weights={
            'cost_of_living_index': 0.25,  # Very important
            'quality_of_life_index': 0.15,
            'safety_index': 0.15,
            'healthcare_index': 0.10,
            'climate_score': 0.15,
            'job_market_score': 0.02,  # Not important for remote work
            'english_proficiency': 0.08,
            'visa_ease': 0.10,
            'tax_friendliness': 0.00
        },
        min_requirements={
            'internet_speed': 80,  # Must have good internet
            'safety_index': 60
        }
    )
    
    recommendations = agent.recommend_countries(nomad_criteria, top_n=3)
    
    for i, (country, score, breakdown) in enumerate(recommendations, 1):
        print(f"\n#{i} Recommendation:")
        print(agent.explain_recommendation(country, score, breakdown))
    
    # Example 2: Family Relocation
    print("\n\n👨‍👩‍👧‍👦 SCENARIO 2: Family Relocation")
    print("-" * 60)
    family_criteria = UserCriteria(
        weights={
            'cost_of_living_index': 0.10,
            'quality_of_life_index': 0.25,  # Very important
            'safety_index': 0.25,  # Very important
            'healthcare_index': 0.20,  # Very important
            'climate_score': 0.05,
            'job_market_score': 0.10,
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
    
    recommendations = agent.recommend_countries(family_criteria, top_n=3)
    
    for i, (country, score, breakdown) in enumerate(recommendations, 1):
        print(f"\n#{i} Recommendation:")
        print(agent.explain_recommendation(country, score, breakdown))
    
    # Example 3: Budget Retiree
    print("\n\n🏖️ SCENARIO 3: Budget-Conscious Retiree")
    print("-" * 60)
    retiree_criteria = UserCriteria(
        weights={
            'cost_of_living_index': 0.30,  # Very important
            'quality_of_life_index': 0.15,
            'safety_index': 0.15,
            'healthcare_index': 0.20,  # Important for retirees
            'climate_score': 0.15,  # Want good weather
            'job_market_score': 0.00,  # Not relevant
            'english_proficiency': 0.05,
            'visa_ease': 0.00,
            'tax_friendliness': 0.00
        },
        min_requirements={
            'healthcare_index': 60,
            'safety_index': 65
        }
    )
    
    recommendations = agent.recommend_countries(retiree_criteria, top_n=3)
    
    for i, (country, score, breakdown) in enumerate(recommendations, 1):
        print(f"\n#{i} Recommendation:")
        print(agent.explain_recommendation(country, score, breakdown))


if __name__ == "__main__":
    main()
