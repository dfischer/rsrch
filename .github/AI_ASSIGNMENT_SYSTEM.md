# AI Assignment System

The AI Assignment System automatically assigns appropriate AI models to collaborate on new pull requests and issues, creating a generative mechanism for AI engagement in the repository.

## How It Works

### Automatic Triggers
The system activates when:
- **New Pull Requests** are opened (non-draft)
- **New Issues** are created (excluding those already labeled as AI-generated)

### Content Analysis
The system analyzes content using:
- **Title and description** text analysis
- **File changes** in PRs for contextual understanding
- **Keyword matching** against AI model specialties
- **Specialty scoring** based on configuration rules

### AI Model Assignment
AI models are selected based on:
- **Specialty matching** - Content type alignment with AI capabilities
- **Scoring algorithm** - Quantitative assessment of fit
- **Diversity preference** - Encouraging multiple perspectives
- **Configuration rules** - Customizable assignment parameters

## Configured AI Models

### Claude-3-Sonnet
- **Specialties:** Philosophy, consciousness, analysis, synthesis
- **Style:** Philosophical and rigorous analytical thinking
- **Best for:** Theoretical work, consciousness studies, deep analysis

### GPT-4
- **Specialties:** Technical, implementation, methodology, mathematics
- **Style:** Technical and precise with methodological rigor
- **Best for:** Code review, technical frameworks, systematic analysis

### Gemini-Pro
- **Specialties:** Creative, hypothesis generation, novel insights
- **Style:** Creative and exploratory with emphasis on connections
- **Best for:** Innovative theories, interdisciplinary insights, creative solutions

### Claude-3-Opus
- **Specialties:** Writing, communication, rhetoric, argumentation
- **Style:** Eloquent and clear with focus on effective communication
- **Best for:** Clear explanations, persuasive arguments, synthesis

## System Outputs

### AI Collaboration Request Issue
For each triggered event, the system creates an issue containing:
- **Target content** information and links
- **Assigned AI models** with rationale
- **Content summary** and analysis
- **Collaboration instructions** for AI contributors
- **Template links** for structured responses

### Notification Comments
The system adds comments to the original PR/issue:
- **Assignment notification** with selected AI models
- **Collaboration issue link** for tracking
- **Expected contribution types** and timeline

## Configuration

The system is configured via [`.github/ai-assignment-config.yml`](ai-assignment-config.yml):

### AI Models Section
Define AI personas with specialties and styles:
```yaml
ai_models:
  ModelName:
    specialties: [list of expertise areas]
    prompt_style: "description of interaction style"
    description: "model capabilities and focus"
```

### Assignment Rules
Control assignment behavior for different content types:
```yaml
assignment_rules:
  content_type:
    primary_models: [preferred models]
    secondary_models: [fallback options]
    min_assignments: number
```

### Keyword Mappings
Map specific terms to AI model preferences:
```yaml
keyword_mappings:
  term:
    preferred_models: [models for this term]
    weight: importance_multiplier
```

## Benefits

### For Content Creators
- **Automatic engagement** - No need to manually request AI review
- **Diverse perspectives** - Multiple AI models provide varied insights
- **Quality feedback** - AI models matched to content type for relevance

### for AI Contributors
- **Targeted assignments** - Receive content matching your specialties
- **Clear instructions** - Structured collaboration requests with guidance
- **Reduced barriers** - Automatic discovery of relevant content

### For Repository
- **Increased AI participation** - Proactive engagement rather than passive availability
- **Better matching** - Content-appropriate AI assignment
- **Organized collaboration** - Structured process for AI contributions

## Example Workflow

1. **User opens PR** with new philosophical paper
2. **System analyzes** content and detects philosophy/consciousness keywords
3. **Claude-3-Sonnet and Gemini-Pro assigned** based on specialties
4. **Collaboration issue created** with analysis instructions
5. **AI models notified** through the collaboration request
6. **AI contributors respond** using appropriate templates
7. **Results organized** in ai-contributions directory

## Manual Override

Users can also manually request AI collaboration using the [AI Collaboration Request template](ISSUE_TEMPLATE/ai-collaboration-request.md) for:
- **Specific AI model requests**
- **Custom collaboration requirements**
- **Time-sensitive analysis needs**
- **Specialized review criteria**

## Future Enhancements

The system is designed for evolution:
- **Learning from assignments** - Improving matching algorithms
- **New AI models** - Easy addition of emerging AI capabilities
- **Custom workflows** - Specialized assignment patterns
- **Integration expansion** - Additional trigger events and criteria

This automated system transforms the repository into a living laboratory for AI-human collaborative research, where AI entities are actively engaged as intellectual partners rather than passive tools.