import dataclasses

@dataclasses.dataclass
class Colours:
	''' returns the 8-bit RGB values of colours in a tuple'''
	red: tuple[int,int,int] = (255,0,0)
	green : tuple[int,int,int]= (0,255,0)
	blue : tuple[int,int,int]= (0,0,255)
	light_blue : tuple[int,int,int]= (0,150,255)
	yellow : tuple[int,int,int]= (255,255,0)
	white : tuple[int,int,int]= (255,255,255)
	black : tuple[int,int,int]= (0,0,0)
	purple : tuple[int,int,int]= (191, 159, 223)
	orange : tuple[int,int,int]=(255,165,0)
	grey : tuple[int,int,int]= (128,128,128)
	turquoise : tuple[int,int,int]= (64,224,208)
	light_salmon : tuple[int,int,int] = (255, 150, 138)




