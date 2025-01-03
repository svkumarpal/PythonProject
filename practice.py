def merge_logs(log_files, output_file):
    with open(output_file, 'w') as output:
        for log_file in log_files:
            with open(log_file, 'r') as input_file:
                output.write(input_file.read())
            # Optionally, you can add a separator between log files
            output.write('\n' + '='*20 + '\n')

def clear_logs(log_files):
    for log_file in log_files:
        with open(log_file, 'w'):
            pass  # This opens the file in write mode and clears its content

# Example usage
log_files = ['messages', 'secure', 'cron']  # List of log files to merge
output_file = 'merged_logs.log'
pip
merge_logs(log_files, output_file)
clear_logs(log_files)