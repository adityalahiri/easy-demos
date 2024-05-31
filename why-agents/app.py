import streamlit as st

# Title and Introduction
st.title('Understand LLM Integration Levels')
st.write('Explore the different levels of LLM Integrations in a customer support scenario.')

details = """
### Level 1: Single Prompt and Answer
- **Overview**: At this level, the LLM answers simple queries directly based on a predefined knowledge base without any additional computation or context.
- **Example**: A user asks for the business hours of a store, and the LLM responds based on stored information.
- **Flow of Information**: Simple one-way flow from the user to the system. The system responds directly to the user's query without further interaction.

### Level 2: Prompt as a Router
- **Overview**: Here, the LLM acts as an intelligent router, directing the user's query to appropriate services or departments.
- **Example**: A customer's request to speak with a sales representative is routed to the sales department without additional input from the LLM.
- **Flow of Information**: One-way flow where the system routes or escalates the query to the right channel based on the user's input.

### Level 3: Single Agent with Tools
- **Overview**: The LLM not only understands the query but also utilizes integrated tools to fetch data or perform tasks before providing a response.
- **Example**: A customer asks about the status of an order, and the LLM checks the current status in real-time from the database to provide an update.
- **Flow of Information**: Dynamic two-way flow between the user and the system. The system may loop through different tools or databases to gather information and respond.

### Level 4: Multiple Agents with Tools
- **Overview**: Multiple LLMs coordinate among themselves, each with specialized roles, to handle complex queries.
- **Example**: A customer has a technical issue that affects billing. One LLM handles the technical troubleshooting while another interacts with the billing system to adjust the charges.
- **Flow of Information**: Multidirectional flow among various agents and tools, enabling complex interactions and comprehensive problem-solving capabilities.
"""

with st.expander("See details on LLM Integration levels"):
    st.markdown(details)

# User input
query_options = {
    "How do I reset my password?": "Level 1",
    "My phone won’t turn on": "Level 2",
    "I need a refund for my last purchase": "Level 2",
    "What’s the warranty on my device?": "Level 1",
    "My device is overheating": "Level 2",
    "Track my order status": "Level 3",
    "Issue with software update": "Level 4"
}
query = st.selectbox("Choose a sample customer support query:", list(query_options.keys()))

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
