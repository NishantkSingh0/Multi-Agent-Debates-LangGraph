from GenerateResponse import Generate
from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda

def run_debate(topic, rounds=4):
    print(f"\n\nEnter topic for debate: {topic}")
    print("Starting debate between Scientist and Philosopher...\n")

    history=[]
    last_msg=f"The debate topic is: {topic}"

    scientist_node=RunnableLambda(lambda x: Generate("scientist", x).split('\n')[0])
    philosopher_node=RunnableLambda(lambda x: Generate("philosopher", x).split('\n')[0])
    judge_node=RunnableLambda(lambda x: Generate("judge", x, max_tokens=200))

    graph=StateGraph(dict)

    graph.add_node("Scientist", scientist_node)
    graph.add_node("Philosopher", philosopher_node)

    graph.set_entry_point("Scientist")
    graph.add_edge("Scientist", "Philosopher")
    graph.add_edge("Philosopher", "Scientist")

    debate_graph=graph.compile()

    for i in range(rounds):
        print('---' * 40)
        print(f"[Round {i+1}]\n")

        scientist_msg=scientist_node.invoke(last_msg)
        print(f"-> Scientist: {scientist_msg}\n")
        history.append(("Scientist", scientist_msg))

        philosopher_msg=philosopher_node.invoke(scientist_msg)
        print(f"-> Philosopher: {philosopher_msg}\n")
        history.append(("Philosopher", philosopher_msg))

        last_msg=philosopher_msg

    print('---' * 40 + "\n")
    debate_transcript="\n".join([f"{role}: {msg}" for role, msg in history])
    judge_msg=judge_node.invoke(f"Summarize and decide the winner of the following debate:\n{debate_transcript}")
    print(f"[Judge] Summary of debate:\n\n{judge_msg}")