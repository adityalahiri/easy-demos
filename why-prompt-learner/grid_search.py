from prompt_learner.tasks.classification import ClassificationTask
from prompt_learner.examples.example import Example
from prompt_learner.selectors.random_sampler import RandomSampler
from prompt_learner.selectors.diverse_sampler import DiverseSampler
from prompt_learner.prompts.cot import CoT
from prompt_learner.templates.markdown import MarkdownTemplate
from prompt_learner.templates.xml import XmlTemplate
from prompt_learner.adapters.ollama_local import OllamaLocal
from prompt_learner.adapters.anthropic import Anthropic
from prompt_learner.adapters.openai import OpenAI
from prompt_learner.evals.metrics.accuracy import Accuracy
from prompt_learner.optimizers.grid_search import GridSearch
import pandas as pd

# Task description and allowed labels
TASK_DESCRIPTION = "You have to classify intent for customer messages sent to chatbot."
ALLOWED_LABELS = ["INFO_ADD_REMOVE_VEHICLE",
    "INFO_SPEAK_TO_REP",
    "INFO_LIFE_BENEFICIARY_CHANGE",
    "INFO_ADD_REMOVE_INSURED",
    "INFO_CANCEL_INS_POLICY"]

classification_task = ClassificationTask(description=TASK_DESCRIPTION,
                                         allowed_labels=ALLOWED_LABELS)

# Template for the task
template = MarkdownTemplate(task=classification_task)

# Load training data
with open("train.csv") as f:
    for line in f:
        text, label = line.split(",")
        classification_task.add_example(Example(text=text.strip(), label=label.strip()))

# Sample examples from the training data
sampler = RandomSampler(num_samples=2, task=classification_task)
sampler.select_examples()

# Assemble the prompt using the Chain of Thought (CoT) template
base_prompt = CoT(template=template)
base_prompt.assemble_prompt()
print(base_prompt.prompt)

# Initialize a grid search on the current prompt
grid_search = GridSearch(prompt=base_prompt)
random_2_shot = RandomSampler(num_samples=2, task=classification_task)
diverse_2_shot = DiverseSampler(num_samples=2, task=classification_task)
random_4_shot = RandomSampler(num_samples=4, task=classification_task)
diverse_4_shot = DiverseSampler(num_samples=4, task=classification_task)

# Define parameter grid for grid search
param_grid = {
    'sampler': [random_2_shot, diverse_2_shot, random_4_shot, diverse_4_shot],
    'template': [MarkdownTemplate, XmlTemplate],
    'adapter': [OllamaLocal(model_name="llama3"), Anthropic(model_name="claude-3-haiku-20240307"), OpenAI(model_name='gpt-4o')]
}

# Perform grid search to find the best parameters
best_params, all_results = grid_search.search(param_grid)
print(pd.DataFrame(all_results))

# Evaluate the best model
template = MarkdownTemplate(task=classification_task)
sampler = RandomSampler(num_samples=2, task=classification_task)
sampler.select_examples()

best_prompt = CoT(template=template)
best_prompt.assemble_prompt()

# Compute accuracy on test data
# Load test data
with open("test.csv") as f:
    for line in f:
        text, label = line.split(",")
        classification_task.add_example(Example(text=text.strip(),
                                                label=label.strip()),
                                                test=True)

acc, results = Accuracy(classification_task).compute(best_prompt,
                                                     OllamaLocal(),
                                                     test=True)
print(acc)
print(pd.DataFrame(results))