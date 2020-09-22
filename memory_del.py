import torch
import os

os.system("nvidia-smi")
torch.cuda.empty_cache() 
torch.cuda.empty()
os.system("nvidia-smi")