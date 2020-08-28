""" Project for Week 4 of "Python Data Representations". Find
differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    current_index = 0
    if min(len(line1), len(line2)) == 0 and max(len(line1), len(line2)) != 0:
        return 0
    elif max(len(line1), len(line2)) == 0:
        return IDENTICAL
    for current_index in range(min(len(line1), len(line2))):
        if line1[current_index] != line2[current_index]:
            break
    else:
        if len(line1) != len(line2):
            return current_index+1
        else:
            return IDENTICAL
    return current_index


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if idx > min(len(line1), len(line2)) or idx < 0:
        return ""
    for char in line1+line2:
        if char in ('\n','\r'):
            return ""
    
    output = line1+'\n'
    output += '='*idx + '^\n'
    output += line2+"\n"
    return output



def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    
    for line_num in range(min(len(lines1), len(lines2))):
        line_diff_idx = singleline_diff(lines1[line_num], lines2[line_num])
        if line_diff_idx is not IDENTICAL:
            return (line_num, line_diff_idx)

    if len(lines1) != len(lines2):
        return (min(len(lines1), len(lines2)), 0)
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    try:
        file_ptr = open(filename, 'r')
        output = [line.replace('\n', '') for line in file_ptr.readlines()]
        file_ptr.close()
        return output
    except FileNotFoundError:
        return []


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    line_diff = multiline_diff(lines1, lines2)
    if line_diff == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    if line_diff[0] >= min(len(lines1), len(lines2)):
        output = "Line 0:\n"
        if len(lines1) >= len(lines2):
            output += singleline_diff_format(lines1[line_diff[0]], "", line_diff[1])
        else:
            output += singleline_diff_format("", lines2[line_diff[0]], line_diff[1])
    else:
        output = "Line {}:\n".format(line_diff[0])
        output += singleline_diff_format(lines1[line_diff[0]], lines2[line_diff[0]], line_diff[1])
    return output

file_diff_format('file8.txt', 'file9.txt')
