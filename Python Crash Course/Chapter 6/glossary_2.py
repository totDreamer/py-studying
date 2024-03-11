glossary = {"IDE": "a software application that provides comprehensive facilities for software development. An IDE\n"
                   "normally consists of at least a source-code editor, build automation tools, and a debugger. Some\n"
                   "IDEs, such as IntelliJ IDEA, Eclipse and Lazarus contain the necessary compiler, interpreter or\n" 
                   "both; others, such as SharpDevelop and NetBeans, do not.",
            "Python": "a high-level general-purpose programming language.",
            "List": "an abstract data type that represents a finite number of ordered values, where the same value\n"
                    "may occur more than once."
            }
for definition, value in glossary.items():
    print(f"{definition} is {value}", end = "\n\n")