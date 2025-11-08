# Indicate questions to be analyzed
QUESTIONS: dict[str, list[str]] = {
    'A': [
        'Why do you want to take this skill track?',
        'What are your expectations before starting this skill track?',
        'Do you have prior knowledge and experience related to this skill track? If yes, please feel free to share.',
    ],
    'B': [
        'Why do you want to take this skill track?',
        'What are your expectations before starting this skill track?',
        'Do you have prior knowledge and experience related to this skill track? If yes, please feel free to share.',
    ]
}

# Get semesters
semesters = [key for key in QUESTIONS]

print(semesters)