def block(lines):
	return [f"/block {line}".strip() for line in lines]
	

def ban(lines):
	return [f"/ban {line}".strip() for line in lines]


def pretty_print(l):
	return "\n".join(l)


if __name__ == "__main__":
	f = open("list.txt")
	lines = f.read().splitlines()
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
