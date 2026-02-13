#!/usr/bin/env python3
"""
Claude Interface to OpenClaw Skills
Simple functions Claude can call to manage skills and agents
"""
import json
import requests
import subprocess

API_BASE = "http://127.0.0.1:8081"

def find_skills(query):
    """Find skills by searching name, description, or category"""
    try:
        response = requests.get(f"{API_BASE}/api/skills/search", params={"q": query})
        return response.json()
    except:
        return {"error": "API not available"}

def get_category_skills(category):
    """Get all skills in a specific category"""
    try:
        response = requests.get(f"{API_BASE}/api/skills/category", params={"cat": category})
        return response.json()
    except:
        return {"error": "API not available"}

def list_categories():
    """Get all available skill categories"""
    try:
        response = requests.get(f"{API_BASE}/api/skills/categories")
        return response.json()
    except:
        return {"error": "API not available"}

def install_skill(skill_id):
    """Install a skill by ID"""
    try:
        response = requests.post(f"{API_BASE}/api/skills/install", 
                               json={"skill_id": skill_id})
        return response.json()
    except:
        return {"error": "API not available"}

def create_agent(name, skills, description=""):
    """Create a new agent with specified skills"""
    try:
        response = requests.post(f"{API_BASE}/api/agents/create",
                               json={
                                   "name": name,
                                   "skills": skills,
                                   "description": description
                               })
        return response.json()
    except:
        return {"error": "API not available"}

def chat_with_agent(message, agent="deep-researcher"):
    """Send message to an agent"""
    try:
        result = subprocess.run(
            ["openclaw", "agent", message, "--agent", agent],
            capture_output=True, text=True, timeout=60
        )
        return {
            "success": result.returncode == 0,
            "response": result.stdout if result.returncode == 0 else result.stderr
        }
    except:
        return {"error": "Failed to chat with agent"}

# Example usage for Claude:
"""
# To find Twitter-related skills:
twitter_skills = find_skills("twitter")

# To get all AI skills:
ai_skills = get_category_skills("AI & LLMs")

# To install a skill:
install_result = install_skill("aisa-twitter-api")

# To create a specialist agent:
agent_result = create_agent(
    name="Twitter Bot",
    skills=["aisa-twitter-api", "social-media-manager"],
    description="Specialized agent for Twitter automation"
)

# To chat with the new agent:
response = chat_with_agent("Post a tweet about AI", "twitter-bot")
"""

if __name__ == "__main__":
    # Test the API
    print("Testing Claude Skills API...")
    
    # List categories
    cats = list_categories()
    print(f"Found {len(cats.get('categories', []))} categories")
    
    # Search for something
    results = find_skills("twitter")
    print(f"Found {len(results.get('results', []))} Twitter-related skills")
