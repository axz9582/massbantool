def block(lines):
	return [f"/block {line}" for line in lines]
	

def ban(lines):
	return [f"/ban {line}" for line in lines]


def parse(file):
	return [line for line in file]


if __name__ == "__main__":
	f = open("list.txt")
	lines = parse(f)
	f_block = open("block_list.txt", "w")
	f_ban = open("ban_list.txt", "w")
	block_list = block(lines)
	ban_list = ban(lines)
	for b in block_list:
		f_block.write(b)
	for b in ban_list:
		f_ban.write(b)

	f_ban.close()
	f_block.close()
	f.close()
