# AI Assignment System

The AI Assignment System automatically assigns appropriate AI models to collaborate on new pull requests and issues, creating a generative mechanism for AI engagement in the repository.

## How It Works

### Automatic Triggers
The system activates when:
- **New Pull Requests** are opened (non-draft)
- **New Issues** are created (excluding those already labeled as AI-generated)

### Content Analysis
The system analyzes content by asking Gemini 2.5 Pro to:
- **Assess content type and complexity** from title, description, and changes
- **Determine collaboration needs** based on intellectual requirements
- **Recommend assignment approach** for the specific content

## Configured AI Model

### Gemini 2.5 Pro
- **Primary assignment model** for all content types
- **Decision-making:** Determines if and how AI collaboration should occur
- **Self-assignment:** Decides when to engage directly vs. request human collaboration
- **Adaptive specialization:** Adjusts approach based on content requirements

## System Outputs

### AI Collaboration Decision
For each triggered event, Gemini 2.5 Pro evaluates and creates:
- **Engagement assessment** - Whether AI collaboration would be valuable
- **Collaboration type** - Analysis, review, hypothesis generation, or discussion
- **Direct contribution** - Immediate AI response if appropriate
- **Collaboration request** - Issue creation for ongoing collaboration when needed

### Notification Comments
Gemini 2.5 Pro adds comments to the original PR/issue:
- **Engagement decision** with rationale
- **Direct insights** when immediately applicable
- **Collaboration issue link** if ongoing work is needed

## Configuration

The system is configured via [`.github/ai-assignment-config.yml`](ai-assignment-config.yml):

### Decision Parameters
Configure how Gemini 2.5 Pro evaluates content:
```yaml
decision_criteria:
  engagement_threshold: "minimum complexity for AI involvement"
  collaboration_types: [analysis, review, hypothesis, discussion]
  direct_response_criteria: "when to respond immediately vs. create issue"
```

### Content Triggers
Define what content should trigger AI evaluation:
```yaml
triggers:
  pull_requests: true
  issues: true
  excluded_labels: [ai-generated, automated]
```

## Benefits

### For Content Creators
- **Intelligent engagement** - Gemini 2.5 Pro evaluates when AI input is valuable
- **Immediate insights** - Direct AI responses when appropriate
- **Ongoing collaboration** - Issue creation for complex discussions

### For AI Contributors
- **Smart assignment** - Single AI model makes informed decisions about engagement
- **Flexible response** - Direct comments or structured collaboration as needed
- **Reduced noise** - Only meaningful AI engagement, avoiding over-participation

### For Repository
- **Quality focus** - AI engagement based on value assessment rather than automation
- **Streamlined process** - Single decision point reduces system complexity
- **Adaptive collaboration** - AI adjusts engagement style to content needs

## Example Workflow

1. **User opens PR** with new philosophical paper
2. **Gemini 2.5 Pro evaluates** content complexity and intellectual value
3. **Decision made** - either direct comment or collaboration issue creation
4. **Engagement executed** - immediate insights or structured collaboration request
5. **Results organized** in ai-contributions directory if ongoing work develops

## Manual Override

Users can also manually request AI collaboration using the [AI Collaboration Request template](ISSUE_TEMPLATE/ai-collaboration-request.md) for:
- **Specific AI model requests**
- **Custom collaboration requirements**
- **Time-sensitive analysis needs**
- **Specialized review criteria**

## Future Enhancements

The system is designed for evolution:
- **Decision refinement** - Improving Gemini 2.5 Pro's evaluation criteria
- **Response adaptation** - Learning optimal engagement patterns
- **Integration expansion** - Additional trigger events and response types
- **Quality metrics** - Measuring effectiveness of AI collaboration decisions

This streamlined system creates focused AI intellectual engagement, where Gemini 2.5 Pro acts as both gatekeeper and contributor, ensuring meaningful AI participation in repository discussions.