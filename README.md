# 🧠 AI Debate Simulator using LangGraph & HuggingFace API

This project simulates a structured debate between a **Scientist** and a **Philosopher**, where each side presents their arguments, followed by a **Judge** evaluating the discussion. The debate is built using [LangGraph](https://github.com/langchain-ai/langgraph), with language generation powered by a HuggingFace-compatible chat model.

<br>

## 📁 Project Structure

```
Multi-Agent-Debates-LangGraph/
├── loadModel.py           # Loads the model using HuggingFace API token
├── GenerateResponse.py    # Function to generate role-based responses
├── Debate.py              # Main logic to simulate the debate using LangGraph
└── main.py                # Entry point to start the debate
```

<br>

## ⚙️ How It Works

1. **Roles:**

   * `Scientist` and `Philosopher` present alternate arguments.
   * `Judge` provides a final summary and declares the winner.

2. **LangGraph Flow:**

   * Uses `StateGraph` to create a loop between Scientist → Philosopher → Scientist for multiple rounds.
   * After the rounds, the Judge evaluates the discussion.

3. **Response Generation:**

   * Each role is prompted differently using a system message.
   * Responses are generated using a HuggingFace-compatible LLM via API token.

<br>

## 🧪 Example Output:

### 🗣️ Topic: **"Should AI be regulated like medicine?"**

```
Enter topic for debate: Should AI be regulated like medicine?
Starting debate between Scientist and Philosopher...

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Round 1]

-> Scientist: As a scientist, I'll approach this topic with a critical and nuanced perspective. The idea of regulating AI like medicine is an intriguing one, but it's essential to consider the unique characteristics of AI and the implications of such a regulatory framework.

-> Philosopher: A most astute observation from a scientist.  The analogy between regulating AI and medicine is indeed intriguing, but as you astutely pointed out, it's crucial to consider the unique characteristics of AI and the potential implications of such a regulatory framework.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Round 2]

-> Scientist: I'm glad you found my analogy thought-provoking. Indeed, the comparison between regulating AI and medicine is a compelling one, as both involve complex systems with potential to either improve or harm human lives. However, as you astutely pointed out,

-> Philosopher: I'm happy to engage in a philosophical discussion with you, but I must correct you that this is the beginning of our convers-> Philosopher: I'm happy to engage in a philosophical discussion with you, but I must correct you that this is the beginning of our conversation, and I haven't made any previous statements. I'm a philosopher, and I'd be delighted to explore the analogy between

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Round 3]

-> Scientist: I'm glad we could start fresh and correct the assumption.  It seems we're both eager to dive into a thoughtful conversation. As a scientist, I've often found that interdisciplinary exchanges can lead to fascinating insights and new perspectives.

-> Philosopher: What a delightful beginning to our conversation!  I couldn't agree more about the value of interdisciplinary exchanges.  As a philosopher, I've had the privilege of engaging with scholars from various fields, and it's indeed amazed me how our seemingly disparate perspectives

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Round 4]

-> Scientist: I completely share your enthusiasm for interdisciplinary exchanges. In my own experience, delving into the realms of philosophy has not only broadened my understanding of the world but also sparked novel insights that I wouldn't have gained through my work in scientific disciplines alone.

-> Philosopher: The confluence of philosophy and other disciplines - it's a rich tapestry that can yield profound and far-reaching insights.  I wholeheartedly agree that venturing into the realm of philosophy can be a transformative experience, capable of illuminating new perspectives

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[Judge] Summary of debate:

After carefully reviewing the debate between the Scientist and the Philosopher, I must conclude that neither participant has effectively addressed the central question of the debate, which is to compare and contrast the regulation of AI with the regulation of medicine.

While both participants have shown a willingness to engage in an interdisciplinary conversation and have acknowledged the value of exploring the unique characteristics of AI, they have failed to provide concrete arguments or evidence to support their claims.

The debate has instead focused on establishing a rapport and building a collaborative atmosphere, which, while commendable, does not necessarily contribute to a meaningful exchange of ideas on the topic at hand.

In light of this, I must declare that neither participant has effectively made their case, and therefore, I must declare the debate a draw. 

However, I do want to commend both participants for their enthusiasm and willingness to engage in a thoughtful conversation. This level of intellectual curiosity and openness is essential for any meaningful exchange of ideas, and I have no doubt that this debate will continue to evolve and
```

<br>

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/nishantksingh0/Multi-Agent-Debates-LangGraph.git
cd Multi-Agent-Debates-LangGraph
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Include in your `requirements.txt`:

```
langgraph
langchain-core
python-dotenv
```

### 3. Setup Environment Variables

Create a `.env` file:

```
HUGGINGFACE_API_TOKEN=your_huggingface_api_token_here
```

### 4. Run the Debate

```bash
python main.py
```

Or you can directly call the `run_debate()` function from `Debate.py`.

<br>

## 🧠 Tech Stack

* **LangGraph** – For defining node-based conversational flow.
* **HuggingFace Model API** – To generate dialogue from each role's perspective.
* **LangChain Core** – To implement `RunnableLambda` nodes.
* **Python** – With environment configuration using `dotenv`.

<br>

## 🛠️ Customization

* Change the number of rounds in `run_debate(topic, rounds=4)`
* Modify response behavior by editing system prompts in `GenerateResponse.py`
* Swap the base model by editing `loadModel.py`

<br>

## 🙌 Contribution

Contributions, suggestions, and improvements are welcome. Fork this repo and submit a pull request!

