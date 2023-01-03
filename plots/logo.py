import weblogo
from PIL import Image
import io
# Load a multiple sequence alignment in FASTA format
with open("./data/alig.fasta", "r") as f:
    alignment = weblogo.read_seq_data(f)

# Generate the sequence logo
logo_options = weblogo.LogoOptions()
logodata = weblogo.LogoData.from_seqs(alignment)
logo_options.title = "Multiple Sequence Alignment"
logo_format = weblogo.LogoFormat(logodata, logo_options)

eps = weblogo.eps_formatter(logodata, logo_format)

pic = io.BytesIO(eps)
img = Image.open(pic)
img.save("logo.png")