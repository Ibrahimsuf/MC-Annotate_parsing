class Annotations:
    def __init__(self, annotations_list) -> None:
        self.annotations_list = annotations_list


    def write_base_pair_info_to_file(self, output_file):
        base_pair_lines = self.extract_information("Base-pairs")
        with open(output_file, "w") as file:
            for line in base_pair_lines:
                file.write(line)

    def extract_information(self, heading_keyword):
        lines_after_heading = []
        heading_found = False

        for line in self.annotations_list:
            # Check if the heading_keyword is in the line
            if heading_keyword in line:
                heading_found = True
                continue
            # If the heading has been found, add the line to the result
            if heading_found:
                lines_after_heading.append(line)

        return lines_after_heading