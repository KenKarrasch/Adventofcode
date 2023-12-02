# Chat GPT input - part 1 only

# in python if I have a file, with each line remove everything before ":", then remove the ",", and ";".   
# Each line will show a number of bags of marbles
# (shown as "number color number color number color" etc), i want to know the lines where a bag does not 
# exceed it limit. red bags may have maximum 12, green 13, blue 14.  With those line numbers add them up



def calculate_total_within_limit_bags(file_path):
    total_line_numbers = 0

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Remove everything before ":" and replace "," and ";" with an empty string
            cleaned_line = line.split(":")[-1].replace(",", "").replace(";", "")

            # Split the cleaned line into pairs of "number color"
            pairs = cleaned_line.strip().split()

            # Flag to determine if any bag exceeds its limit
            exceed_limit = False

            # Iterate over pairs and check the conditions for each color
            for i in range(0, len(pairs), 2):
                num_bags = int(pairs[i])
                color = pairs[i + 1]

                # Check if the conditions are met for each color
                if (color == 'red' and num_bags > 12) or \
                   (color == 'green' and num_bags > 13) or \
                   (color == 'blue' and num_bags > 14):
                    exceed_limit = True
                    break  # Break the loop if any color exceeds its limit

            # If none of the bags exceed their limit, add the line number
            if not exceed_limit:
                print(f"Line {line_number}: Within limit")
                total_line_numbers += line_number

    return total_line_numbers

# Replace 'your_file.txt' with the actual path to your file
file_path = '23-2.txt'
total_line_numbers = calculate_total_within_limit_bags(file_path)
print(f"Total line numbers within limit: {total_line_numbers}")
