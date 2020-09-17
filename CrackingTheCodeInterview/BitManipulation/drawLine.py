def drawLine(screen: 'list[byte]', width: 'int', x1: 'int', x2: 'int', y: 'int') -> 'None':
	start_offset = x1 % 8	#si es divisible entre 8 entonces el primer byte esta totalmente prendido
	first_full_byte = x1 / 8
	if start_offset != 0: first_full_byte += 1
	end_offset = x2 % 8
	last_full_byte = x2 / 8
	if end_offset != 7: last_full_byte -=1 		#debe acabar en 7 para encender desde el bit 0 hasta el 1
	for bte in range(first_full_byte, last_full_byte + 1): screen[((width // 8) * y) + bte] = 0xFF
	start_mask = 0xFF >> start_offset
	end_mask = 0xFF << end_offset
	if x1 // 8 == x2 // 8: screen[(width // 8) * y + (x1 // 8)] |= end_mask & start_mask
	else:
		if start_offset != 0: screen[(width // 8) * y + first_full_byte - 1] |= start_mask
		if end_offset != 7: screen[(width // 8) * y + last_full_byte + 1] |= end_mask