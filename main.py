import os
import pathlib

PROJECT_PATH = pathlib.Path(__file__).parent
INPUT_PATH = os.path.join(PROJECT_PATH, 'input')
OUTPUT_PATH = os.path.join(PROJECT_PATH, 'output')

# Key list
# https://www.autohotkey.com/docs/v1/KeyList.htm
CONTROLS = {
    "l": "a",
    "r": "d",
    "u": "w",
    "d": "s",
    "block": "Space",
    "fp": "Numpad8",
    "bp": "Numpad9",
    "fk": "Numpad5",
    "bk": "Numpad6",
}


def create_left_side(cmd, dest):
    sides = cmd.split('+')

    if len(sides) > 2:
        raise Exception(f"""
        Invalid Syntax on line:
        {cmd}

        Expected left side with 0 or 1 '+' sign
        """)

    if len(sides) == 1:
        dest.write(sides[0])
    elif len(sides) == 2 and sides[0] == 'shift':
        dest.write('+' + sides[1])
    elif len(sides) == 2 and sides[0] == 'ctrl':
        dest.write('^' + sides[1])
    elif len(sides) == 2 and sides[0] == 'alt':
        dest.write('!' + sides[1])
    else:
        raise Exception(f"""
        Invalid Modifier on left side:
        {cmd}
        """)

    dest.write('::')


def create_right_side(cmd, dest):
    dest.write("""
        if GetKeyState(%l%)
          Send, {%l% up}
          b := r
          f := l
        else
          Send, {%r% up}
          b := l
          f := r
    """)

    steps = cmd.split(',')
    for step in steps:
        substeps = step.split('+')
        substeps = [sub.lower() for sub in substeps]
        if len(substeps) == 1:
            dest.write(f"    Send, %{substeps[0]}%\n")
        else:
            # we press multiple keys simultaneously here
            dest.write(f"    Send, ")
            for sub in substeps:
                dest.write(f"{{%{sub}% down}}")
            substeps.reverse()
            for sub in substeps:
                dest.write(f"{{%{sub}% up}}")
            dest.write("\n")

    dest.write('    return\n')


def create_initialization_block(dest):
    for key in CONTROLS:
        dest.write(f'{key} := "{CONTROLS[key]}"\n')
    dest.write("SetKeyDelay, 30, 30\n")


def create_command(cmd, dest):
    sides = cmd.split('=')

    if len(sides) != 2:
        raise Exception(f"""
        Invalid Syntax on line:
        {cmd}

        Expected command with single '=' sign
        """)

    create_initialization_block(dest)
    create_left_side(sides[0], dest)
    create_right_side(sides[1], dest)


def create_output_file(input_file):
    path_to_file = os.path.join(INPUT_PATH, input_file)
    output_file_name = pathlib.Path(path_to_file).stem + ".ahk"
    output_file_path = os.path.join(OUTPUT_PATH, output_file_name)

    with open(path_to_file, "r") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    with open(output_file_path, "w") as dest:
        for line in lines:
            if not line:
                dest.write(line)
                dest.write('\n')
            elif line.startswith('#') or line.startswith(';'):
                dest.write("; " + line)
                dest.write('\n')
            elif '=' in line:
                create_command(line, dest)
            else:
                raise Exception(f"""
                Invalid Syntax on line:
                {line}
                
                Expected comment, empty line or command
                """)


def main():
    for input_file in os.listdir(INPUT_PATH):
        if input_file.endswith('.txt'):
            create_output_file(input_file)


main()
