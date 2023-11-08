import polling
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def simple_assistant():
    assistant = client.beta.assistants.create(
        name="Leetcode Tutor",
        instructions="You are a personal leetcode tutor. Write and run code to answer leetcode questions.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-1106-preview",
    )

    thread = client.beta.threads.create()

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address the user as Jane Doe. The user has a premium account.",
    )

    return run, thread


def poll_assistant(run, thread):
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    return run.completed_at is not None


def run_loop():
    run, thread = simple_assistant()

    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    polling.poll(lambda: (poll_assistant(run, thread) is True), step=5, poll_forever=True)

    res = []
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    for message in messages.data:
        for content in message.content:
            res.append(content.text.value)
            print(content.text.value)
    return res
