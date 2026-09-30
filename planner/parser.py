def parse_module(raw_text):

    topics = []
    current_topic = None

    lines = raw_text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # If the line starts with "-", it is a task
        if line.startswith("-"):

            task = line.lstrip("-").strip()

            if current_topic and task:
                current_topic["tasks"].append(task)

        else:

            # Split a line that contains topic + tasks
            parts = line.split(" - ")

            topic_title = parts[0].strip()

            if not topic_title:
                continue

            # Create a new topic
            current_topic = {
                "title": topic_title,
                "tasks": []
            }

            topics.append(current_topic)

            # Tasks that appear on the same line as the topic
            for task in parts[1:]:

                task = task.strip()

                if task:
                    current_topic["tasks"].append(task)

    return topics