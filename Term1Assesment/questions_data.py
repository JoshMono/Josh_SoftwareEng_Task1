# Question data layout is layed out in this way for easy readability and simplicity

QUESTIONS = [
    {"question_id": 1,
     "question_text": "Which data type dosn't exist?",
     "difficulty": 1,
     "type_of_question": "multi",
     "answer": "Text",
     "choices": [
         "Text",
         "Bool",
         "Date and Time",
         "Real"
     ]
     },
     
     {"question_id": 2,
     "question_text": "What is a list?",
     "difficulty": 1,
     "type_of_question": "multi",
     "answer": "An ordered collection of items which can be indexed and changed",
     "choices": [
         "A data structure that pairs keys with values",
         "A sequence of characters used in computing",
         "An ordered collection of items which can be indexed and changed",
         "A fixed-size collection of elements of the same data type"
     ]
     },
     
     {"question_id": 3,
     "question_text": "What is the purpose of a data structure?",
     "difficulty": 1,
     "type_of_question": "multi",
     "answer": "To organize and manage data efficiently",
     "choices": [
         "To enhance the visual appeal of data in user interfaces",
         "To organize and manage data efficiently",
         "To increase the complexity of software programs",
         "To transmit data over the internet"
     ]
     },
     
     {"question_id": 4,
     "question_text": "A  _ _ _ _  table is a structure that can map keys to values.",
     "difficulty": 1,
     "type_of_question": "fill",
     "answer": "hash",
     },
     
     {"question_id": 5,
     "question_text": "What is $$$$ as an int?",
     "difficulty": 2,
     "type_of_question": "fill",
     "answer": "",
     },
     
     {"question_id": 6,
     "question_text": "Rank these fundamental software development steps",
     "difficulty": 3,
     "type_of_question": "rank",
     "answer": ["Requirements Definition", "Determining Specifications", "Design", "Development", "Integration", "Testing and Debugging", "Installation", "Maintenance"],
     "choices": [
         "Requirements Definition",
         "Determining Specifications",
         "Design",
         "Development",
         "Integration",
         "Testing and Debugging",
         "Installation",
         "Maintenance"
     ]
     },
     
     {"question_id": 7,
     "question_text": "What is $ in binary?",
     "difficulty": 2,
     "type_of_question": "multi",
     "answer": "",
     "choices": []
     },
     
     {"question_id": 8,
     "question_text": "Desk checking and  _ _ _ _  checking is an effective technique?",
     "difficulty": 1,
     "type_of_question": "fill",
     "answer": "peer"
     },
     
     {"question_id": 9,
     "question_text": "What is Waterfall technique?",
     "difficulty": 2,
     "type_of_question": "multi",
     "answer": "A project management approach used in software development",
     "choices": [
         "A method used to create intricate paper designs",
         "A project management approach used in software development",
         "A specific programming language used for web development",
         "A form of database modeling technique"
                
     ]
     },
     
     {"question_id": 10,
     "question_text": "What is Agile technique?",
     "difficulty": 2,
     "type_of_question": "multi",
     "answer": "An approach to project management that values adaptability and flexibility",
     "choices": [
         "An approach to project management that values adaptability and flexibility",
         "A programming language commonly used for mobile app development",
         "A specific method for creating software documentation",
         "A form of quality assurance testing for software products"
                
     ]
     },
     
     {"question_id": 11,
     "question_text": "_ _ _ _ _ _ _ _ _ _  is a readable description of what a program should do",
     "difficulty": 3,
     "type_of_question": "fill",
     "answer": "pseudocode"
     },
     
     {"question_id": 12,
     "question_text": "Rank these steps for the technique Agile",
     "difficulty": 2,
     "type_of_question": "rank",
     "answer": ["Plan", "Design", "Develop", "Test", "Deploy", "Review", "Launch"],
     "choices": [
         "Plan",
         "Design",
         "Develop",
         "Test",
         "Deploy",
         "Review",
         "Launch"
     ]
     },
     
     {"question_id": 13,
     "question_text": "Rank these steps for the technique Waterfall",
     "difficulty": 2,
     "type_of_question": "rank",
     "answer": ["Requirments Gathering", "Analysis", "Design", "Develop", "Testing", "Operations"],
     "choices": [
         "Requirments Gathering",
         "Analysis",
         "Design",
         "Develop",
         "Testing",
         "Operations"
     ]
     },
     
     {"question_id": 14,
     "question_text": "When is the technique Agile most efficent?",
     "difficulty": 2,
     "type_of_question": "multi",
     "answer": "When the project's end goal is always changing",
     "choices": [
         "When there's a clear end goal",
         "When the project's end goal is always changing",
         "When the project is a video game",
         "When theres more then one coding language being used"
     ]
     },
     
     {"question_id": 15,
     "question_text": "An  _ _ _ _ _ _ _ _ _  is simply a set of steps used to complete a specific task",
     "difficulty": 2,
     "type_of_question": "fill",
     "answer": "algorithm",
     },
     
     {"question_id": 16,
     "question_text": "Imperative and Declarative are programming ___?",
     "difficulty": 2,
     "type_of_question": "multi",
     "answer": "Paradigms",
     "choices": [
         "Paradigms",
         "Algorithms",
         "Pseudocode",
         "Languages"
     ]
     },

     {"question_id": 17,
     "question_text": "Rank theses binary numbers from largest to smallest (Top to bottom)",
     "difficulty": 2,
     "type_of_question": "rank",
     "answer": ["1101", "1011", "0110", "0101", "0010"],
     "choices": [
         "1101",
         "1011",
         "0110",
         "0101",
         "0010"
     ]
     },
     
     {"question_id": 18,
     "question_text": "Rank theses binary numbers from largest to smallest (Top to bottom)",
     "difficulty": 3,
     "type_of_question": "rank",
     "answer": ["1110 1101", "1011 1011", "1011 1010", "1001 1001", "1000 1000"],
     "choices": [
         "1110 1101",
         "1011 1011",
         "1011 1010",
         "1001 1001",
         "1000 1000"
     ]
     },
     
     {"question_id": 19,
     "question_text": "A ___ works on the LIFO process Last In First Out",
     "difficulty": 3,
     "type_of_question": "multi",
     "answer": "Stack",
     "choices": [
         "Stack",
         "Table",
         "String",
         "Array"
     ]
     },
     
     {"question_id": 20,
     "question_text": "What is the term 'Iteration' in programming",
     "difficulty": 3,
     "type_of_question": "multi",
     "answer": "A sequence of code being repeated until a result is achieved",
     "choices": [
         "A sequence of code being repeated until a result is achieved",
         "A statement that determines if its true or false",
         "A type of list",
         "A type of data type"
     ]
     }
]