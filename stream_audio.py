'''Generar y enviar audio
'''
import sqlite3
import json
import vlc
import time
p_audio = 0
slaveID = 0
inicio = 0
fin = 0

def main():
	global inicio,fin,slaveID,p_audio
	while True:
		try:
			conn = sqlite3.connect('/home/pi/Resiliente_CD/resiliente.db')
			cur = conn.cursor()
			cur.execute('''SELECT slave,fecha_inicio,fecha_fin FROM activacion WHERE ID=(SELECT MAX(ID) FROM activacion)''')
			tiempos = cur.fetchall()
			for t in tiempos:
				slaveID = t[0]
				inicio = t[1]
				fin = t[2]
			print("Inicio:	"+str(inicio))
			print("Final:	"+str(fin))
		except sqlite3.Error as e:
			print("[!] Sqlite3 error, ID: ",e.args[0])
		conn.close()
		now = int(time.time()) - 18000
		print("Now:	"+str(now))
		if (int(time.time()) - 18000) >= int(inicio) and (int(time.time()) - 18000) <= int(fin):
			with open('/home/pi/Resiliente_CD/audio_param.json') as file:
				p_audio = json.load(file)
			p_audio['evento'] = p_audio['evento'].lower()
			p_audio['estado'] = p_audio['estado'].lower()
			p_audio['urgencia'] = p_audio['urgencia'].lower()
			p_audio['respuesta'] = p_audio['respuesta'].lower()
			p_audio['severidad'] = p_audio['severidad'].lower()
			p_audio['mensaje'] = p_audio['mensaje'].lower()
			if p_audio['mensaje'] != 'cancela':
				audio_gen(True)
		#else:
		#	audio_gen(False)
		time.sleep(1)

def audio_gen(estado):
	global p_audio, slaveID
	print(p_audio)
	x = ['/home/pi/Resiliente_CD/audios/'+p_audio['estado']+'.wav',
		 '/home/pi/Resiliente_CD/audios/'+p_audio['evento']+'.wav',
		 '/home/pi/Resiliente_CD/audios/'+p_audio['severidad']+'.wav',
		 '/home/pi/Resiliente_CD/audios/'+p_audio['respuesta']+'.wav',
		 '/home/pi/Resiliente_CD/audios/'+p_audio['urgencia']+'.wav']
	fixed_audios = ["/home/pi/Resiliente_CD/audios/alerta_crecidario_evacuar_inmediata.wav",
			"/home/pi/Resiliente_CD/audios/alerta_crecidario_extremo_evacuar_inmediata.wav",
			"/home/pi/Resiliente_CD/audios/alerta_sismo_extremo_evacuar_inmediata.wav",
			"/home/pi/Resiliente_CD/audios/alerta_tsunami_extremo_evacuar_inmediata.wav",
			"/home/pi/Resiliente_CD/audios/simulacro_crecidario_extremo_evacuar_inmediata.wav",
			"/home/pi/Resiliente_CD/audios/simulacro_inundacion_extremo_evacuar_inmediata.wav",
			"/home/pi/Resiliente_CD/audios/simulacro_sismo_extremo_evacuar_inmediata.wav",
			"/home/pi/Resiliente_CD/audios/simulacro_tsunami_extremo_evacuar_inmediata.wav"]
	instance = vlc.Instance()
	player = instance.media_player_new()
	player.audio_set_volume(250)
	if estado == True:
		if p_audio['estado'] == 'actual' and p_audio['evento'] == 'crecidario' and p_audio['respuesta'] == 'evacuar' and p_audio['severidad'] != 'extremo' and p_audio['urgencia'] == 'inmediato':
			media = instance.media_new(fixed_audios[0])
			player.set_media(media)
			player.play()
			while player.get_state() != vlc.State.Ended:
				time.sleep(1)
		elif p_audio['estado'] == 'actual' and p_audio['evento'] == 'crecidario' and p_audio['respuesta'] == 'evacuar' and p_audio['severidad'] == 'extremo' and p_audio['urgencia'] == 'inmediato':
			media = instance.media_new(fixed_audios[1])
			player.set_media(media)
			player.play()
			while player.get_state() != vlc.State.Ended:
				time.sleep(1)
		elif p_audio['estado'] == 'actual' and p_audio['evento'] == 'sismo' and p_audio['respuesta'] == 'evacuar' and p_audio['severidad'] == 'extremo' and p_audio['urgencia'] == 'inmediato':
			media = instance.media.new(fixed_audios[2])
			player.set_media(media)
			player.play()
			while player.get_state() != vlc.State.Ended:
				time.sleep(1)
		elif p_audio['estado'] == 'actual' and p_audio['evento'] == 'tsunami' and p_audio['respuesta'] == 'evacuar' and p_audio['severidad'] == 'extremo' and p_audio['urgencia'] == 'inmediato':
			media = instance.media_new(fixed_audios[3])
			player.set_media(media)
			player.play()
			while player.get_state() != vlc.State.Ended:
				time.sleep(1)
		elif p_audio['estado'] == 'simulacro' and p_audio['evento'] == 'crecidario' and p_audio['respuesta'] == 'evacuar' and p_audio['severidad'] == 'extremo' and p_audio['urgencia'] == 'inmediato':
			media = instance.media_new(fixed_audios[4])
			player.set_media(media)
			player.play()
			while player.get_state() != vlc.State.Ended:
				time.sleep(1)
		elif p_audio['estado'] == 'simulacro' and p_audio['evento'] == 'inundacion' and p_audio['respuesta'] == 'evacuar' and p_audio['severidad'] == 'extremo' and p_audio['urgencia'] == 'inmediato':
			media = instance.media_new(fixed_audios[5])
			player.set_media(media)
			player.play()
			while player.get_state() != vlc.State.Ended:
				time.sleep(1)
		elif p_audio['estado'] == 'simulacro' and p_audio['evento'] == 'sismo' and p_audio['respuesta'] == 'evacuar' and p_audio['severidad'] == 'extremo' and p_audio['urgencia'] == 'inmediato':
			media = instance.media_new(fixed_audios[6])
			player.set_media(media)
			player.play()
			while player.get_state() != vlc.State.Ended:
				time.sleep(1)
		elif p_audio['estado'] == 'simulacro' and p_audio['evento'] == 'tsunami' and p_audio['respuesta'] == 'evacuar' and p_audio['severidad'] == 'extremo' and p_audio['urgencia'] == 'inmediato':
			media = instance.media_new(fixed_audios[7])
			player.set_media(media)
			player.play()
			while player.get_state() != vlc.State.Ended:
				time.sleep(1)
		else:
			for a in x:
				print(a)
				media = instance.media_new(a)
				player.set_media(media)
				player.play()
				while player.get_state() != vlc.State.Ended:
					time.sleep(1)
	else:
		player.stop()

if __name__ == '__main__':
	print("Generador y Output de audio")
	main()
