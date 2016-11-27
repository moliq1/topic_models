def read_seg_data(filename):
	with open(filename, 'r') as f:
		data = [i.decode('utf-8') for i in f.readlines()]
        return data

def remove_numbers(data, target_file='data_seg3', do_write=True):
    data = [re.sub(r'[\w+]|[\.]', '', i) for i in data]
    data = [re.sub(r' . ', '', i).split() for i in data]
    #data = [list(i) for i in line if len(i) > 1 for line in data ]
    print ' '.join(data[0])
    
    if do_write == True:
    # write to disk
        with open(target_file, 'w') as outfile:
            for line in data:
                outfile.write(' '.join(line).encode('utf-8') + '\n')
    else:
        return data

