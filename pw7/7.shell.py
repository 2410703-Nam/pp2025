import subprocess
import shlex
import sys

def run_command(cmd):
    """
    Execute command with support for:
    - input redirection <
    - output redirection >
    - pipe |
    """

    # Split pipeline
    commands = [shlex.split(c.strip()) for c in cmd.split('|')]

    processes = []
    prev_process = None

    for i, command in enumerate(commands):
        stdin = None
        stdout = None

        # Input redirection
        if '<' in command:
            idx = command.index('<')
            stdin = open(command[idx + 1], 'r')
            command = command[:idx]

        # Output redirection
        if '>' in command:
            idx = command.index('>')
            stdout = open(command[idx + 1], 'w')
            command = command[:idx]

        # Pipe handling
        if prev_process:
            stdin = prev_process.stdout

        process = subprocess.Popen(
            command,
            stdin=stdin,
            stdout=stdout or subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        processes.append(process)
        prev_process = process

    # Get output of last command
    out, err = processes[-1].communicate()

    if out:
        print(out, end='')
    if err:
        print(err, end='', file=sys.stderr)


def main():
    while True:
        try:
            cmd = input("myshell> ").strip()

            if cmd == "":
                continue
            if cmd.lower() in ["exit", "quit"]:
                break

            run_command(cmd)

        except KeyboardInterrupt:
            print("\nExit shell")
            break
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()