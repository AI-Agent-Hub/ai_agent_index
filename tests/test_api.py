# -*- coding: utf-8 -*-
# @Time    : 2025/03/01

import ai_agent_index as aa
import json

def search_ai_agent_traffic_data():

    result = aa.search(q="Coding Agent Jetbrains")
    print ("## DEBUG: search result is|%s" % str(result))

    result2 = aa.search(q="Coding Agent", limit=20, timeout=5)
    print ("## DEBUG: search result is|%s" % str(result2))

    result3 = aa.search(q="", limit=20, timeout=5)
    print ("## DEBUG: Mock search result is|%s" % str(result3))

def publish_your_agent():
    """
        access_key can be obtained from your personal page:
        www.deepnlp.orgworkspace/my_ai_services
        once you submit, it's pending approval and you can track the data then
        get your access_key from http://www.deepnlp.org/workspace/my_ai_services
    """
    access_key = "${your_access_key}"
    name = "My First AI Agent"

    item_info = {}
    item_info["content"] = "This AI Agent can do complicated programming work for humans"
    item_info["website"] = "https://www.my_first_agent.com"
    item_info["field"] = "AI AGENT"
    item_info["subfield"] = "Coding Agent"
    item_info["content_tag_list"] = "coding,python"
    result = aa.add(access_key=access_key, name="My First Agent", item_info=item_info)
    url = result["url"] if "url" in result else ""
    msg = result["msg"] if "msg" in result else ""
    print ("## DEBUG: AI Agent Marketplace Post msg is|%s" % str(msg))
    print ("## DEBUG: AI Agent Marketplace Post url is|%s" % str(url))

def main():
    search_ai_agent_traffic_data()
    publish_your_agent()

if __name__ == '__main__':
	main()
