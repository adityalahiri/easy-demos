import streamlit as st

# Title and Introduction
st.title('Understand LLM Integration Levels')
st.write('Explore the different levels of LLM Integrations in a customer support scenario.')
details="""
### Level 1: Single Prompt and Answer

- **Overview**: At this most basic level, the system provides direct answers to user queries without any further action.
- **Functionality**: Users input a question and receive an immediate answer based purely on the input provided.
- **Flow of Information**: One-way flow of information from the user to the system, with no further interaction required.

### Level 2: Prompt as a Router

- **Overview**: This level introduces a router that directs prompts to initiate specific actions or tools without providing a direct response.
- **Functionality**: A user input triggers specific actions or tool activations, guiding the process flow in one direction without back-and-forth interaction.
- **Flow of Information**: One-way flow of information from the user to the system, with the system directing the user to the appropriate tools or actions.

### Level 3: Single Agent with Tools

- **Overview**: An intelligent agent at this level has the capability to decide which tools to use, execute them, and then choose to either loop within the tools for further processing or return a response.
- **Functionality**: The agent dynamically handles the interaction, deciding the flow of data and tools, which allows for a two-way information exchange.
- **Flow of Information**: Two-way flow of information between the user and the system, with the agent deciding the flow of tools and data.

### Level 4: Multiple Agents with Tools

- **Overview**: The most complex level involves multiple agents, each equipped with one or more specialized tools. These agents can communicate and coordinate with each other, managing different tasks.
- **Functionality**: Information flows in all directions among multiple agents, each handling specific tasks and collaborating to resolve more complex scenarios effectively.
- **Flow of Information**: Multi-directional flow of information among multiple agents and tools, allowing for comprehensive handling of complex user queries.

"""
with st.expander("See details on LLM Integration levels"):
    st.markdown(details)
# User input

import streamlit as st

# Dropdown menu for selecting queries
query_options = {
    "How do I reset my password?": "Level 1",
    "My phone won’t turn on": "Level 2",
    "I need a refund for my last purchase": "Level 2",
    "What’s the warranty on my device?": "Level 1",
    "My device is overheating": "Level 2",
    "Track my order status": "Level 3",
    "Issue with software update": "Level 4"
}
query = st.selectbox("Choose a customer support query:", list(query_options.keys()))

# Define responses and explanations for each level
responses = {
    "Level 1": ("This query requires a straightforward, direct response based on static information.",
                "To reset your password, go to settings and click 'Reset Password.'",
                "The warranty on your device lasts for 12 months from the purchase date."),
    "Level 2": ("This query needs routing to specific departments or follow-up actions without an immediate solution.",
                "Routing to technical support for troubleshooting your power issue.",
                "Please contact our refund department through your account dashboard."),
    "Level 3": ("An intelligent agent will fetch real-time data and provide personalized responses.",
                "Your order #12345 shipped on 03/15 and will arrive by 03/20."),
    "Level 4": ("Complex issues requiring multiple agents to diagnose problems, check service history, and provide comprehensive solutions.",
                "Diagnosing... It appears there's a compatibility issue with the software update. Our tech support will contact you shortly.")
}

# Show selected level and response
selected_level = query_options[query]
st.write(f"### Required Interaction: {selected_level}")
explanation, *possible_responses = responses[selected_level]

# Determine the response based on the query
if query in ["How do I reset my password?", "What’s the warranty on my device?"]:
    response = possible_responses[0] if query == "How do I reset my password?" else possible_responses[1]
else:
    response = possible_responses[0]

st.write(explanation)
st.write("### Response:")
st.write(response)

