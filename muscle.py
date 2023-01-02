import subprocess

def muscle(fasta_file):
    # Function to run muscle on a fasta file
    # Returns the output of the muscle command  
    output = subprocess.check_output(
        ["./muscle5.1.win64.exe",
         "-align", fasta_file,
         "-output", r"./aligned.fasta"], text=True)
    return output

