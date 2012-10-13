# My coding Dojo


## Aliases
    export DOJO_JS_TEMPLATE="var assert = require('assert');"
    export DOJO_PYTHON_TEMPLATE="if __name__ == '__main__':\n  pass"
    export DOJO_JAVA_TEMPLATE="public class Main {\n\n  public static void main(String[] args) {\n    assert true;\n  }\n}"

    alias dojoJava="javac Main.java && java -ea Main"
    alias dojoJs="node main.js"
    alias dojoPython="python main.python"

    alias initDojoJs="mkdir js && cd js && echo \"$DOJO_JS_TEMPLATE\" > main.js"
    alias initDojoPython="mkdir python && cd python && echo \"$DOJO_PYTHON_TEMPLATE\" > main.py"
    alias initDojoJava="mkdir java && cd java && echo \"$DOJO_JAVA_TEMPLATE\" > Main.java"