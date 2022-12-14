themelist = {
	'twoline':{'topleft':'\u2554', 'topright':'\u2557', 'btmleft':'\u255A', 'btmright':'\u255D', 'topbtm':'\u2550', 'leftright':'\u2551', 'close':'\u2561', 'open':'\u255E'},
	'oneline':{'topleft':'\u250C', 'topright':'\u2510', 'btmleft':'\u2514', 'btmright':'\u2518', 'topbtm':'\u2500', 'leftright':'\u2502', 'close':'\u2524', 'open':'\u251C'},
}

def _DEBUGPRT(errcode):
	# ?
	if errcode==0:
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

	exit(1)
	

class canvas:
	def __init__(self, w=16,h=7, t=['air', 'block'], gt=[' ', '\u2588'], dti=0, th='twoline', n='Test'):
		if w<16:
			_DEBUGPRT(101)
		elif h<5:
			_DEBUGPRT(102)
		elif dti<0:
			_DEBUGPRT(105)
		elif len(t)==0:
			_DEBUGPRT(103)
		elif len(gt)==0:
			_DEBUGPRT(104)
		else:
			self.theme = th
			self.name = n.strip()
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
		theme=themelist[self.theme]

		bottom = theme["topbtm"] * (self.width + 2)
		if len(self.name) < self.width-1:
			top = theme["topbtm"] + theme["close"] + self.name + theme["open"] + (theme["topbtm"] * (self.width - 1 - len(self.name)))
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
		pmap = pmap.replace('[', f'{theme["leftright"]} ')
		pmap = pmap.replace(']', f' {theme["leftright"]}')
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
	tiledict = {'air':' ','stone':'\u2588', 'water':'\u2591', 'box':'\u25A1', 'box_filled ':'\u25A0', 'dagger':'\u2020', 'line':'\u2500', 'bullet':'\u2219', 'empty_bullet':'\u25E6', 'pointer_left':'\u2190', 'pointer_up':'\u2191', 'pointer_right':'\u2192', 'pointer_down':'\u2193', 'pointer_leftright':'\u2194', 'pointer_topbtm':'\u2195', 'w_face':'\u263A', 'b_face':'\u263B', 'note':'\u266A', 'note_beam':'\u266B', 'thiccline':'\u25AC', 'wave':'\u2248', 'sun':'\u263C', 'heart':'\u2665', 'triangle_top':'\u25b2', 'triangle_right':'\u25ba', 'triangle_btm':'\u25bc', 'triangle_left':'\u25c4', 'lozenge':'\u25CA', 'diamond_filled':'\u2666', 'bitcoin':'\u20BF', 'circle':'\u20DD', 'star':'\u2736'}
	w,h=17,5
	map1 = canvas(w,h, list(tiledict.keys()),list(tiledict.values()), n=' Testing canvas ')
	for n in range(len(list(tiledict.keys()))):
		if n%w==0: o=w;
		for i in range(w):
			if (n+(i+1))%w==0: o=(w-1)-i;
		map1.settile(o,(n)//w, n)
	print(map1.fancymap())