# AI Agent Index | AI Agent Directory | AI Agent Marketplace to Host All AI Agent Directory related AI Agents Web Traffic Data, Search Ranking, Community, Reviews and More.

This is the official github repo for pypi package "ai_agent_directory" https://pypi.org/project/ai_agent_index. You can use this package to download and get statistics (Google/Bing Search Ranking/Github Stars/Website Traffic) of AI agents on website from AI Agent Marketplace AI Agent Directory and AI Agent Search Portal by Deepnlp AI Agent Marketplace, is the directory for more than 5000+ AI Agents and Apps covering various types of AI agents, such as autonomous agent, chatbots, Computer and Mobile phone use agents, robotic agents, and various industries such as business, finance, law, medical or healthcare, etc. The directory are updated to websites from both public repo (github/huggingface) as well as AI Agent services in cloud service provider (Microsoft Azure AWS, Copilot, GPT Store, Google Cloud, etc). 

### AI Agent Search Engine

Website : http://www.deepnlp.org/search/agent

Find the AI Agent in any category and get the realtime search/app store/github ranking data

![AI Agent Marketplace Directory Search](https://raw.githubusercontent.com/AI-Agent-Hub/AI-Agent-Marketplace/refs/heads/main/AI%20Agent%20Marketplace%20Search.jpg)

Register and list your AI agent For Free through (http://www.deepnlp.org/workspace/my_ai_services)


### AI Agent Index

Website: http://www.deepnlp.org/store/ai-agent

![AI Agent Marketplace AI Agent Directory](https://raw.githubusercontent.com/AI-Agent-Hub/AI-Agent-Marketplace/refs/heads/main/docs/ai_agents_navigation.jpg)

#### Track Google/Bing Search Ranking Data

For example, if you want to know the AI coding agent traffic data, you can visit (http://www.deepnlp.org/store/ai-agent#section_Coding%20Agent)

You can track vanna.ai, Cody and Cline bot, etc.

- cline bot (http://www.deepnlp.org/store/ai-agent/coding-agent/pub-cline-bot/cline-bot) has google search ranking 37.0 and bing search ranking 15.0, and under search keywords such as "AI Coding Agent, AI Coding, etc.", it got 22.8k Github stars 
- vanna.ai (http://www.deepnlp.org/store/ai-agent/ai-agent/pub-vanna-ai/vanna-ai)
- Cody Sourcegraph (http://www.deepnlp.org/store/ai-agent/ai-agent/pub-cody-by-sourcegraph/cody-by-sourcegraph)
- Taskade.com (http://www.deepnlp.org/store/ai-agent/finance/pub-taskade/taskade)

![AI Coding Agent](https://raw.githubusercontent.com/AI-Agent-Hub/AI-Agent-Marketplace/refs/heads/main/docs/image_coding_agent_v2.jpg)


## API to Search OpenDomain AI Agent Traffic Data

### Install

```
pip install ai_agent_index

```

### API Seach Agent Web Data Usage
python 

```

import ai_agent_index as aa
import json

def search_ai_agent_traffic_data():

    result = aa.search(q="AI Agents Frameworks LLamaIndex")
    print ("## DEBUG: search result is|%s" % str(result))

    result2 = aa.search(q="AI Agents Frameworks", limit=20, timeout=5)
    print ("## DEBUG: search result is|%s" % str(result2))

    result3 = aa.search(q="", limit=20, timeout=5)
    print ("## DEBUG: Mock search result is|%s" % str(result3))


search_ai_agent_traffic_data()


```

### API to Add New AI Agent to AI Agent Marketplace | AI Agent Directory | AI Agent Index for Free
You can call the API to register the meta information of your AI Agents. Alternatively, you can also use the web page (http://www.deepnlp.org/workspace/my_ai_services) to list your 
AI Agent.

```

import ai_agent_index as aa
import json

def publish_your_agent():
    """
        Get your access_key from http://www.deepnlp.org/workspace/my_ai_services
        access_key can be generated from your personal page at: www.deepnlp.orgworkspace/my_ai_services
        Once you submit, it's pending approval and you can track the data then
    """
    access_key = "${your_access_key}"
    name = "My First AI Agent"

    item_info = {}
    item_info["content"] = "This AI Agent can help users develop complicated AI Agent Workflow..."
    item_info["website"] = "https://www.my_first_agent.com"
    item_info["field"] = "AI AGENT"
    item_info["subfield"] = "Coding Agent"
    item_info["content_tag_list"] = "coding,python"
    result = aa.add(access_key=access_key, name="My First Agent", item_info=item_info)
    url = result["url"] if "url" in result else ""
    msg = result["msg"] if "msg" in result else ""
    print ("## DEBUG: AI Agent Marketplace Post msg is|%s" % str(msg))
    print ("## DEBUG: AI Agent Marketplace Post url is|%s" % str(url))


publish_your_agent()

```



### AI Agent List


### Related
#### AI Agent Marketplace and Search
[AI Agent Marketplace and Search](http://www.deepnlp.org/search/agent) <br>
[AI Robot Search](http://www.deepnlp.org/search/robot) <br>
[Equation and Academic search](http://www.deepnlp.org/search/equation) <br>
[AI & Robot Comprehensive Search](http://www.deepnlp.org/search) <br>
[AI & Robot Question](http://www.deepnlp.org/question) <br>
[AI & Robot Community](http://www.deepnlp.org/community) <br>
##### AI Agent
[AI Agent Marketplace Reviews](http://www.deepnlp.org/store/ai-agent) <br>
[AI Agent Marketplace and Search Portal Reviews 2025](http://www.deepnlp.org/blog/ai-agent-marketplace-and-search-portal-reviews-2025) <br>
[AI Agent Publisher](http://www.deepnlp.org/store/pub?category=ai-agent) <br>
[Microsoft AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-microsoft-ai-agent) <br>
[Claude AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-claude-ai-agent) <br>
[OpenAI AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-openai-ai-agent) <br>
[AgentGPT AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-agentgpt) <br>
[Saleforce AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-salesforce-ai-agent) <br>
[AI Agent Builder Reviews](http://www.deepnlp.org/store/ai-agent/ai-agent-builder) <br>
##### Robotics
[Tesla Cybercab Robotaxi](http://www.deepnlp.org/store/pub/pub-tesla-cybercab) <br>
[Tesla Optimus](http://www.deepnlp.org/store/pub/pub-tesla-optimus) <br>
[Figure AI](http://www.deepnlp.org/store/pub/pub-figure-ai) <br>
#### Equation
[DeepNLP Equation Database](http://www.deepnlp.org/equation) <br>
