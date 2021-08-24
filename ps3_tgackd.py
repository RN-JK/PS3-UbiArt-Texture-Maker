import os, glob

dir = 'input/temp'

try:
    os.makedirs(dir)

except:
    pass

try:
    for dds in os.listdir("input/"):
        os.system("dds2gtf - input/"+dds+" -o input/temp/"+dds.replace(".dds",".gtf"))
    
        with open("input/temp/"+dds.replace(".dds",".gtf"), "rb") as f:
            gtfdata=f.read()

        ckdoutput=open("output_tgackd/"+dds.replace(".dds",".tga.ckd"),"wb")
        ckdoutput.write(b'\x00\x00\x00\x09\x54\x45\x58\x00\x00\x00\x00\x2C\x00\x02\xAB\x38\x04\x00\x04\x00\x00\x01\x18\x00\x00\x02\xAB\x38\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x02\x02\xCC\xCC')

        ckdoutput.write(gtfdata)
        ckdoutput.close()
        print(ckdoutput)

except:
    pass

filelist = glob.glob(os.path.join(dir, "*"))
for f in filelist:
    os.remove(f)

os.rmdir(dir)

