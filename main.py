def _DEBUGPRT(errcode):
	# ?
	if errcode==-1:
		pass

	# Create canvas errors
	elif errcode==101:
		print('[INP] The Width is too small.')
	elif errcode==102:
		print('[INP] The Height is too small.')
	elif errcode==103:
		print('[INP] The tiles list is empty.')
	elif errcode==104:
		print('[INP] The graphical tiles list is empty.')
	elif errcode==105:
		print('[INP] The default tile is lower than 0.')

	# settile errors
	elif errcode==201:
		print('[SET] The x is out of canvas.')
	elif errcode==202:
		print('[SET] The y is out of canvas.')
	elif errcode==203:
		print('[SET] The tile id is not exist.')
		
	elif errcode==69:
		print('[TST] Test Text')
	

class canvas:
	def __init__(self, name='Test', w=16,h=7, t=['air', 'block'], gt=[' ', '\u2588'], dti=0, test=True):
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
		theme={'topleft':'\u2554', 'topright':'\u2557', 'btmleft':'\u255A', 'btmright':'\u255D',
		'topbtm':'\u2550', 'leftright':'\u2551', 'close':'\u2561', 'open':'\u255E'}

		bottom = theme["topbtm"] * (self.width + 2)
		if len(self.name) < self.width-1:
			top = theme["topbtm"] + theme["close"] + self.name + '\u255E' + ('\u2550' * (self.width - 1 - len(self.name)))
		else:
			top = f'{theme["topbtm"]}{theme["close"]} UnbndName {theme["open"]}' + (theme["topbtm"] * (self.width - 12))

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
		return f'{theme["topleft"]}{top}{theme["topright"]}\n{pmap}\n{theme["btmleft"]}{bottom}{theme["btmright"]}'

	def settile(self, x,y, tileid):
		if x > self.width:
			_DEBUGPRT(201)
		elif y > self.height:
			_DEBUGPRT(202)
		elif tileid > len(self.tiles):
			_DEBUGPRT(203)
		else:
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
	tiledict = {'air':' ','stone':'\u2588', 'water':'\u2591', 'box':'\u25A1',
		'thiccline':'\u25AC', 'dagger':'\u2020', 'line':'\u2500', 'dot':'\u2219',
		'left':'\u2190', 'up':'\u2191', 'right':'\u2192', 'down':'\u2193',
		'w face':'\u263A', 'b face':'\u263B', 'note':'\u266A', 'notebeam':'\u266B',
		'boxfilled ':'\u25A0'}
	map1 = canvas('  Testing a canvas ', 19,7, list(tiledict.keys()), list(tiledict.values()), 0)
	#map1.settilecustom(0,1, 'a')
	for i in range(len(list(tiledict.keys()))):
		map1.settile(i,0, i)
	print(map1.fancymap())