class Map:
	def __init__(self, w,h, t, gt, dti):
		self.width = w
		self.height = h
		self.tiles = t
		self.defaulttile = dti
		m=[]
		for i in range(h):
			l=[]
			for i in range(w):
				l.append(dti)
			m.append(l)
		self.graphictile = list([str(gt.index(i))+', ', i[0]] for i in gt)
		self.map = m

	def prmap(self):
		return self.map

	def fancymap(self):
		tb = '\u2550' * (self.width + 2)
		pmap=str(self.map)[1:-1]
		gt_loop=self.graphictile[:]
		gt_loop.reverse()
		gtloop_len=gt_loop.__len__()
		for i in range(gtloop_len):
			#print(f'{i}: {gt_loop[i]}')
			pmap = pmap.replace(*gt_loop[i])
		pmap = pmap.replace('], ', ']\n')
		pmap = pmap.replace('[', '\u2551 ')
		pmap = pmap.replace(']', ' \u2551')
		return f'\u2554{tb}\u2557\n{pmap}\n\u255A{tb}\u255D'

	def settile(self, x,y, tileid):
		self.map[y][x] = tileid

	def gettile(self, x,y):
		return self.map[y][x]

	def setdragtile(self, x1,y1, x2,y2):
		pass

	def settilecustom(self, x,y, tile):
		name=str(self.graphictile.__len__()) + ', '
		if name in self.tiles:
			self.map[y][x] = self.tiles.index(name)
		else:
			self.tiles.append(name)
			self.graphictile.append([name, tile])
			self.map[y][x] = self.tiles.index(name)

if __name__ == '__main__':
	tiles = [
		['air','stone','water', 'box', 'thiccline', 'dagger', 'line', 'dot', 
			'left', 'up', 'right', 'down'],
		[' ', '\u2588', '\u2591', '\u25A1', '\u25AC', '\u2020', '\u2500', '\u2219',
			'\u2190', '\u2191', '\u2192', '\u2193']
	]
	map1 = Map(33,7, tiles[0], tiles[1], 0)
	for i in range(tiles[0].__len__()):
		map1.settile(i,0, i)
	map1.settilecustom(0,2, 'a')
	#print(map1.prmap())
	print(map1.fancymap())