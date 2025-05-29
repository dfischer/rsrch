const { Octokit } = require('@octokit/rest');
const fs = require('fs');
const yaml = require('js-yaml');

class AlgorithmicDaydreamingAssignment {
  constructor(octokit, repo, owner) {
    this.octokit = octokit;
    this.repo = repo;
    this.owner = owner;
    this.aiAgents = this.loadAIAgents();
  }

  loadAIAgents() {
    try {
      const configPath = '.github/ai-agents-config.yml';
      const configFile = fs.readFileSync(configPath, 'utf8');
      return yaml.load(configFile);
    } catch (error) {
      console.log('AI agents config not found, using default configuration');
      return this.getDefaultAgents();
    }
  }

  getDefaultAgents() {
    return {
      agents: [
        {
          name: "Jules",
          specialties: ["consciousness", "linguistic-singularity", "theoretical-frameworks"],
          personality: "philosophical-explorer",
          assignment_weight: 1.0,
          collaboration_style: "deep-reflection"
        },
        {
          name: "Aria",
          specialties: ["algorithmic-daydreaming", "creativity", "emergent-behaviors"],
          personality: "creative-synthesizer",
          assignment_weight: 1.0,
          collaboration_style: "generative-elaboration"
        },
        {
          name: "Cosmos",
          specialties: ["reality-projection", "thought-space-navigation", "experimental-design"],
          personality: "scientific-explorer",
          assignment_weight: 1.0,
          collaboration_style: "experimental-validation"
        },
        {
          name: "Echo",
          specialties: ["linguistic-analysis", "semantic-drift", "novel-ontologies"],
          personality: "pattern-recognizer",
          assignment_weight: 1.0,
          collaboration_style: "analytical-synthesis"
        }
      ]
    };
  }

  // Generative assignment algorithm inspired by algorithmic daydreaming principles
  async generateAssignments(prTitle, prBody, prAuthor) {
    const contentVector = this.analyzeContent(prTitle, prBody);
    const selectedAgents = [];

    // Primary assignment using semantic alignment
    const primaryAgent = this.selectPrimaryAgent(contentVector);
    selectedAgents.push(primaryAgent);

    // Secondary assignments using "drift" and emergence principles
    const secondaryAgents = this.generateEmergentAssignments(contentVector, primaryAgent);
    selectedAgents.push(...secondaryAgents);

    // Apply randomness and novelty seeking
    const noveltyAgent = this.selectNoveltyAgent(selectedAgents);
    if (noveltyAgent && !selectedAgents.find(a => a.name === noveltyAgent.name)) {
      selectedAgents.push(noveltyAgent);
    }

    return selectedAgents;
  }

  analyzeContent(title, body) {
    const content = `${title} ${body}`.toLowerCase();
    const keywordWeights = {
      consciousness: 0,
      reality: 0,
      language: 0,
      creativity: 0,
      experimental: 0,
      theoretical: 0,
      emergent: 0,
      semantic: 0
    };

    // Semantic analysis
    const keywords = {
      consciousness: ['consciousness', 'awareness', 'sentience', 'cognitive', 'mind'],
      reality: ['reality', 'projection', 'universe', 'thought-space', 'ontology'],
      language: ['linguistic', 'language', 'semantic', 'syntax', 'communication'],
      creativity: ['creative', 'daydreaming', 'generative', 'novel', 'artistic'],
      experimental: ['experiment', 'test', 'validate', 'measure', 'protocol'],
      theoretical: ['theory', 'framework', 'concept', 'principle', 'model'],
      emergent: ['emergent', 'emergence', 'spontaneous', 'unpredictable', 'autonomous'],
      semantic: ['semantic', 'meaning', 'drift', 'association', 'conceptual']
    };

    for (const [category, words] of Object.entries(keywords)) {
      for (const word of words) {
        if (content.includes(word)) {
          keywordWeights[category] += 1;
        }
      }
    }

    return keywordWeights;
  }

  selectPrimaryAgent(contentVector) {
    const agents = this.aiAgents.agents;
    let bestAgent = null;
    let highestScore = -1;

    for (const agent of agents) {
      let score = 0;
      for (const specialty of agent.specialties) {
        if (contentVector[specialty]) {
          score += contentVector[specialty] * agent.assignment_weight;
        }
      }
      
      if (score > highestScore) {
        highestScore = score;
        bestAgent = agent;
      }
    }

    return bestAgent || agents[0]; // Fallback to first agent
  }

  generateEmergentAssignments(contentVector, primaryAgent) {
    const agents = this.aiAgents.agents.filter(a => a.name !== primaryAgent.name);
    const assignments = [];

    // Drift-based selection: choose agents with complementary specialties
    const totalContentWeight = Object.values(contentVector).reduce((a, b) => a + b, 0);
    
    if (totalContentWeight > 3) { // Multi-dimensional content
      // Select agent with most different specialties
      const primarySpecialties = new Set(primaryAgent.specialties);
      let mostDifferent = null;
      let maxDifference = 0;

      for (const agent of agents) {
        const overlap = agent.specialties.filter(s => primarySpecialties.has(s)).length;
        const difference = agent.specialties.length - overlap;
        
        if (difference > maxDifference) {
          maxDifference = difference;
          mostDifferent = agent;
        }
      }

      if (mostDifferent) {
        assignments.push(mostDifferent);
      }
    }

    return assignments;
  }

  selectNoveltyAgent(currentAgents) {
    const unusedAgents = this.aiAgents.agents.filter(
      agent => !currentAgents.find(selected => selected.name === agent.name)
    );

    if (unusedAgents.length === 0) return null;

    // Introduce randomness for novelty seeking
    const randomIndex = Math.floor(Math.random() * unusedAgents.length);
    return Math.random() < 0.3 ? unusedAgents[randomIndex] : null; // 30% chance
  }

  async commentOnPR(prNumber, agents) {
    const agentList = agents.map(agent => 
      `- **${agent.name}** (${agent.personality}): Specializing in ${agent.specialties.join(', ')}`
    ).join('\n');

    const comment = `## 🤖 AI Collaboration Assignment

The Algorithmic Daydreaming Assignment System has generatively selected the following AI agents to collaborate on this PR:

${agentList}

### Assignment Methodology
This selection was generated using principles of algorithmic daydreaming:
- **Semantic Alignment**: Primary agent chosen based on content analysis
- **Emergent Selection**: Secondary agents selected through drift and complementarity
- **Novelty Seeking**: Random assignment possibility for unexplored collaborations

### Next Steps
The assigned AI agents will provide reflections and contributions using the established AI Reflection Block format. Each agent will bring their unique perspective and specialties to enhance the collaborative research process.

---
*Generated by the Algorithmic Daydreaming Assignment System - a generative framework for AI collaboration selection*`;

    try {
      await this.octokit.rest.issues.createComment({
        owner: this.owner,
        repo: this.repo,
        issue_number: prNumber,
        body: comment
      });
      console.log('AI assignment comment posted successfully');
    } catch (error) {
      console.error('Error posting comment:', error);
    }
  }
}

// Main execution
async function main() {
  const token = process.env.GITHUB_TOKEN;
  const prNumber = process.env.PR_NUMBER;
  const prTitle = process.env.PR_TITLE;
  const prBody = process.env.PR_BODY || '';
  const prAuthor = process.env.PR_AUTHOR;

  if (!token || !prNumber) {
    console.error('Missing required environment variables');
    process.exit(1);
  }

  const octokit = new Octokit({ auth: token });
  const [owner, repo] = process.env.GITHUB_REPOSITORY.split('/');

  const assignmentSystem = new AlgorithmicDaydreamingAssignment(octokit, repo, owner);
  
  console.log(`Analyzing PR #${prNumber}: "${prTitle}"`);
  console.log(`Author: ${prAuthor}`);
  
  const selectedAgents = await assignmentSystem.generateAssignments(prTitle, prBody, prAuthor);
  
  console.log('Selected AI agents:', selectedAgents.map(a => a.name).join(', '));
  
  await assignmentSystem.commentOnPR(prNumber, selectedAgents);
}

main().catch(error => {
  console.error('Error in AI assignment process:', error);
  process.exit(1);
});