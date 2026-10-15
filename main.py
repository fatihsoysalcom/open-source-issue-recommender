# This script simulates a basic AI-like system for recommending open-source issues
# based on a user's skills and experience level. It demonstrates the core concept
# of IssuePilot AI: intelligently matching contributors to suitable tasks.

# --- Mock Data: Represents various open-source issues --- 
issues = [
    {
        'id': 1,
        'title': 'Fix login page CSS bug on mobile',
        'description': 'The login page styling is broken on smaller screens. Needs responsive CSS adjustments.',
        'skills_needed': ['CSS', 'Frontend', 'Bug Fixing'],
        'difficulty': 'easy',
        'beginner_friendly': True
    },
    {
        'id': 2,
        'title': 'Add user authentication with OAuth',
        'description': 'Implement Google/GitHub OAuth for user login and registration.',
        'skills_needed': ['Python', 'Backend', 'API Development', 'Security'],
        'difficulty': 'hard',
        'beginner_friendly': False
    },
    {
        'id': 3,
        'title': 'Improve documentation for API endpoints',
        'description': 'Update README and add examples for existing REST API endpoints.',
        'skills_needed': ['Documentation', 'Technical Writing', 'API Development'],
        'difficulty': 'easy',
        'beginner_friendly': True
    },
    {
        'id': 4,
        'title': 'Write unit tests for data processing module',
        'description': 'Existing data processing logic lacks comprehensive unit tests. Increase code coverage.',
        'skills_needed': ['Python', 'Testing', 'Data Processing'],
        'difficulty': 'medium',
        'beginner_friendly': False
    },
    {
        'id': 5,
        'title': 'Implement dark mode toggle for UI',
        'description': 'Add a button to switch between light and dark themes across the application.',
        'skills_needed': ['JavaScript', 'Frontend', 'CSS', 'UI/UX'],
        'difficulty': 'medium',
        'beginner_friendly': False
    },
    {
        'id': 6,
        'title': 'Refactor database schema for performance',
        'description': 'Optimize existing PostgreSQL schema for better query performance and scalability.',
        'skills_needed': ['Database', 'SQL', 'Backend', 'Performance Optimization'],
        'difficulty': 'hard',
        'beginner_friendly': False
    },
    {
        'id': 7,
        'title': 'Translate application strings to Turkish',
        'description': 'Translate all user-facing strings in the application to Turkish.',
        'skills_needed': ['Localization', 'Turkish Language', 'Technical Writing'],
        'difficulty': 'easy',
        'beginner_friendly': True
    },
    {
        'id': 8,
        'title': 'Create a new landing page component',
        'description': 'Design and implement a new responsive landing page section using React.',
        'skills_needed': ['React', 'JavaScript', 'Frontend', 'UI/UX', 'CSS'],
        'difficulty': 'medium',
        'beginner_friendly': False
    }
]

# --- Mock User Profile: Can be changed to simulate different users --- 
user_profile_beginner = {
    'skills': ['Python', 'Bug Fixing', 'Documentation'],
    'experience_level': 'beginner' # Options: 'beginner', 'intermediate', 'advanced'
}

# --- AI-like Recommendation Logic --- 
def recommend_issues(user_profile, all_issues):
    """
    Recommends open-source issues based on user's skills and experience level.
    This function simulates the "AI" aspect of matching contributors to tasks.
    """
    recommendations = []
    user_skills = set(user_profile['skills'])
    user_experience = user_profile['experience_level']

    for issue in all_issues:
        issue_skills = set(issue['skills_needed'])
        
        # Calculate skill match score: More common skills mean a better match
        common_skills = user_skills.intersection(issue_skills)
        skill_match_score = len(common_skills)
        
        # Adjust score based on difficulty and user experience
        # This part simulates intelligent filtering/prioritization by IssuePilot AI
        difficulty_score_adjustment = 0
        if user_experience == 'beginner':
            if issue.get('beginner_friendly', False):
                difficulty_score_adjustment += 3 # Strong preference for beginner-friendly
            elif issue['difficulty'] == 'easy':
                difficulty_score_adjustment += 1
            elif issue['difficulty'] in ['medium', 'hard']:
                difficulty_score_adjustment -= 2 # Discourage harder issues for beginners
        elif user_experience == 'intermediate':
            if issue['difficulty'] == 'medium':
                difficulty_score_adjustment += 2 # Prefer medium difficulty
            elif issue['difficulty'] in ['easy', 'hard']:
                difficulty_score_adjustment += 1 # Can handle, but not primary focus
        elif user_experience == 'advanced':
            if issue['difficulty'] == 'hard':
                difficulty_score_adjustment += 3 # Strong preference for challenging issues
            elif issue['difficulty'] == 'medium':
                difficulty_score_adjustment += 1
            elif issue['difficulty'] == 'easy':
                difficulty_score_adjustment += 0.5 # Can still contribute, but less challenging

        # Combine scores: Skill match is primary, difficulty adjustment fine-tunes
        total_score = skill_match_score * 10 + difficulty_score_adjustment 

        # Only recommend if there's a positive match score
        if total_score > 0: 
            recommendations.append({
                'issue': issue,
                'score': total_score,
                'common_skills': list(common_skills)
            })

    # Sort recommendations by score in descending order
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    return recommendations

# --- Main Execution --- 
if __name__ == "__main__":
    print("--- IssuePilot AI - Simple Open Source Issue Recommender ---\n")

    current_user_profile = user_profile_beginner # Start with the beginner profile

    print("Your current profile:")
    print(f"  Skills: {', '.join(current_user_profile['skills'])}")
    print(f"  Experience Level: {current_user_profile['experience_level'].capitalize()}\n")

    recommended = recommend_issues(current_user_profile, issues)

    if recommended:
        print("Top Recommended Open Source Issues for you:")
        for i, rec in enumerate(recommended[:5]): # Show top 5 recommendations
            issue = rec['issue']
            print(f"\n{i+1}. {issue['title']} (Recommendation Score: {rec['score']:.1f})")
            print(f"   Description: {issue['description']}")
            print(f"   Skills Needed: {', '.join(issue['skills_needed'])}")
            print(f"   Difficulty: {issue['difficulty'].capitalize()}")
            print(f"   Common Skills matched: {', '.join(rec['common_skills'])}")
            if issue.get('beginner_friendly'):
                print("   *This issue is marked as beginner-friendly!*")
    else:
        print("No suitable issues found based on your profile. Try updating your skills!")

    # --- Demonstrate with a different user profile --- 
    print("\n" + "="*60 + "\n")
    print("--- Simulating an 'Advanced' Python/Backend Developer Profile ---\n")
    
    user_profile_advanced = {
        'skills': ['Python', 'Backend', 'Database', 'API Development', 'Security', 'Performance Optimization'],
        'experience_level': 'advanced'
    }
    print("New profile:")
    print(f"  Skills: {', '.join(user_profile_advanced['skills'])}")
    print(f"  Experience Level: {user_profile_advanced['experience_level'].capitalize()}\n")

    recommended_advanced = recommend_issues(user_profile_advanced, issues)
    if recommended_advanced:
        print("Top Recommended Open Source Issues for the advanced profile:")
        for i, rec in enumerate(recommended_advanced[:5]):
            issue = rec['issue']
            print(f"\n{i+1}. {issue['title']} (Recommendation Score: {rec['score']:.1f})")
            print(f"   Description: {issue['description']}")
            print(f"   Skills Needed: {', '.join(issue['skills_needed'])}")
            print(f"   Difficulty: {issue['difficulty'].capitalize()}")
            print(f"   Common Skills matched: {', '.join(rec['common_skills'])}")
    else:
        print("No suitable issues found for the advanced profile.")
