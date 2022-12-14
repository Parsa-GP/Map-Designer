def _DEBUGPRT(errcode):
	if errcode==-1:
		pass
	elif errcode==11:
		print('[I] The Width is too small.')
	elif errcode==12:
		print('[I] The Height is too small.')
	elif errcode==13:
		print('[I] The tiles list is empty.')
	elif errcode==14:
		print('[I] The graphical tiles list is empty.')
	elif errcode==14:
		print('[I] The default tile is lower than 0.')
	elif errcode==69:
		print('[T] Test Text')
	

class canvas:
	def __init__(self, name='Test', w=16,h=7, t=['air', 'block'], gt=[' ', '\u2588'], dti=0):
		if w<16:
			_DEBUGPRT(11)
		elif h<7:
			_DEBUGPRT(12)
		elif dti<0:
			_DEBUGPRT(15)
		elif len(t)==0:
			_DEBUGPRT(13)
		elif len(gt)==0:
			_DEBUGPRT(14)
		else:
			self.name = name.strip()
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
		bottom = '\u2550' * (self.width + 2)
		if len(self.name) < self.width-2:
			top = '\u2550\u2561' + self.name + '\u255E' + ('\u2550' * (self.width - 1 - len(self.name)))
		else:
			top = '\u2550\u2561 UnbndName \u255E' + ('\u2550' * (self.width - 12))

		pmap=str(self.map)[1:-1]
		gt_loop=self.graphictile[:]
		gt_loop.reverse()
		gtloop_len=gt_loop.__len__()
		pmap = pmap.replace(']', ', ]')
		for i in range(gtloop_len):
			#print(f'{i}: {gt_loop[i]}')
			pmap = pmap.replace(*gt_loop[i])
		pmap = pmap.replace('], ', ']\n')
		pmap = pmap.replace('[', '\u2551 ')
		pmap = pmap.replace(']', ' \u2551')
		return f'\u2554{top}\u2557\n{pmap}\n\u255A{bottom}\u255D'

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

	def addtilecustom(self, tile):
		name=str(self.graphictile.__len__()) + ', '
		if name in self.tiles:
			pass
		else:
			self.tiles.append(name)
			self.graphictile.append([name, tile])

if __name__ == '__main__':
	tiles = [
		['air','stone','water', 'box', 'thiccline', 'dagger', 'line', 'dot', 
			'left', 'up', 'right', 'down'],
		[' ', '\u2588', '\u2591', '\u25A1', '\u25AC', '\u2020', '\u2500', '\u2219',
			'\u2190', '\u2191', '\u2192', '\u2193']
	]
	map1 = canvas('  Testing a canvas   ', 33,7, tiles[0], tiles[1], 0)
	map1.settilecustom(0,1, 'a')
	for i in range(tiles[0].__len__()):
		map1.settile(i,0, i)
	map1.addtilecustom('b')
	map1.settile(1,1, 13)
	print(map1.fancymap())