""" Imports """
from sys import exit as quitprog
from ast import literal_eval

themelist = {
    'twoline':{
        'tl':'\u2554', 'tr':'\u2557', 'bl':'\u255A', 'br':'\u255D',
        'tb':'\u2550', 'lr':'\u2551', 'cl':'\u2561', 'op':'\u255E'
    },
    'oneline':{
    'tl':'\u250C', 'tr':'\u2510', 'bl':'\u2514', 'br':'\u2518',
    'tb':'\u2500', 'lr':'\u2502', 'cl':'\u2524', 'op':'\u251C'
    },
}

def _errprt(errcode):
    """ Print error with errorcode given. """
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

    quitprog(1)
    
class Canvas:
    """ A window-style canvas for graw thing on it. """
    default=[(16,7),['air', 'block'],[' ', '\u2588']]
    def __init__(self, csize=default[0], tilelist=default[1],
        graphtile=default[2], dti=0, theme='twoline', name='Test'):
        width,height = csize
        if width<16:
            _errprt(101)
        elif height<5:
            _errprt(102)
        elif dti<0:
            _errprt(105)
        elif len(tilelist)==0:
            _errprt(103)
        elif len(graphtile)==0:
            _errprt(104)
        else:
            self.theme = theme
            self.name = name.strip()
            self.width = width
            self.height = height
            self.tiles = tilelist
            self.defaulttile = dti
            width_gen=[]
            for i in range(height):
                height_gen=[]
                for i in range(width):
                    height_gen.append(dti)
                width_gen.append(height_gen)
            self.graphictile = list([str(graphtile.index(i))+', ', i[0]] for i in graphtile)
            self.map = width_gen

    def list_print(self):
        """ print canvas like a list """
        return self.map

    def fancy_print(self):
        """ Print canvas human readable """
        theme=themelist[self.theme]

        bottom = theme["tb"] * (self.width + 2)
        if len(self.name) < self.width-1:
            top = theme["tb"]+theme["cl"]+self.name+theme["op"]+(theme["tb"]*(self.width-1-len(self.name)))
        else:
            top = f'{theme["tb"]}{theme["cl"]} UnbndName {theme["op"]}'+(theme["tb"]*self.width-12)

        pmap=str(self.map)[1:-1]
        gt_loop=self.graphictile[:]
        gt_loop.reverse()
        gtloop_len=len(gt_loop)
        pmap = pmap.replace(']', ', ]')
        for i in range(gtloop_len):
            pmap = pmap.replace(*gt_loop[i])
        pmap = pmap.replace('], ', ']\n')
        pmap = pmap.replace('[', f'{theme["lr"]} ')
        pmap = pmap.replace(']', f' {theme["lr"]}')
        return f'{theme["tl"]}{top}{theme["tr"]}\n{pmap}\n{theme["bl"]}{bottom}{theme["br"]}'

    def settile(self, tile_x,tile_y, tileid):
        """ Set a specefic tile """
        if tile_x > self.width:
            _errprt(201)
        elif tile_y > self.height:
            _errprt(202)
        elif tileid > len(self.tiles):
            _errprt(203)
        else:
            self.map[tile_y][tile_x] = tileid

    def gettile(self, tile_x,tile_y):
        """ Get tile char """
        return self.map[tile_y][tile_x]

    def setcustomtile(self, tile_x,tile_y, tile):
        """ Adding a custom tile and adding it in canvas """
        name=str(len(self.graphictile)) + ', '
        if name in self.tiles:
            self.map[tile_y][tile_x] = self.tiles.index(name)
        else:
            self.tiles.append(name)
            self.graphictile.append([name, tile])
            self.map[tile_y][tile_x] = self.tiles.index(name)

    def addcustomtile(self, tile):
        """ Adding a custom tile without adding in canvas """
        name=str(len(self.graphictile)) + ', '
        if name in self.tiles:
            pass 
        else:
            self.tiles.append(name)
            self.graphictile.append([name, tile])

if __name__ == '__main__':
    with open('default.tiles', encoding='utf8') as file:
        tiledict = literal_eval(file.read())
    canvas_size=(17,5)
    WIDTH=canvas_size[0]
    map1 = Canvas(canvas_size,list(tiledict.keys()),list(tiledict.values()),name=' Testing canvas ')
    for n in range(len(list(tiledict.keys()))):
        if n%WIDTH==0:
            WID=WIDTH
        for num in range(WIDTH):
            if (n+(num+1))%WIDTH==0:
                WID=(WIDTH-1)-num
        map1.settile(WID,(n)//WIDTH, n)
    print(map1.fancy_print())
