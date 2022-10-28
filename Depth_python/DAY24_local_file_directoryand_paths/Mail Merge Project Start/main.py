#Get data
the_names=[]
letter_path = r"Depth_python\DAY24_local_file_directoryand_paths\Mail Merge Project Start\Input\Letters\starting_letter.txt"
invited_names_path =r"Depth_python\DAY24_local_file_directoryand_paths\Mail Merge Project Start\Input\Names\invited_names.txt" 

with open(invited_names_path,mode='r') as invited_names:
        lines = invited_names.read()
        list_of_names = lines.splitlines()
        for name in list_of_names:
            the_names.append(name)

with open(letter_path,mode='r') as letter_read:
    content_read = letter_read.read()
    for i, name in enumerate(the_names):
        x = content_read.replace('[name]',f'{name}')
        output = open(f"Depth_python\DAY24_local_file_directoryand_paths\Mail Merge Project Start\Output\ReadyToSend\sendletter_to_{name}","w")
        output.write(x)

