import xbmc,xbmcgui,os,re,urllib,time
import adultresolver
import linkfinder
adultresolver = adultresolver.streamer()
dialog = xbmcgui.Dialog()
def Blacklistcheck(url):

	if 'hclips.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'chaturbate.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'watchxxxfreeinhd.com' in url:
		linkfinder.find(url)
		quit()
	elif 'youngpornvideos.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'adult-channels.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'javhihi.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'txxx.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'vrsumo.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'anysex.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'pandamovie.info' in url:
		adultresolver.resolve(url)
		quit()
	elif 'http://streamingporn.xyz' in url:
		adultresolver.resolve(url)
		quit()
	elif '3movs.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'watchmygf.me' in url:
		adultresolver.resolve(url)
		quit()
	elif 'vrsmash.com' in url:
		adultresolver.resolve(url)
		quit()
	elif '4tube.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'justporno.tv' in url:
		adultresolver.resolve(url)
		quit()
	elif 'spankbang.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'teenpornsite.net' in url:
		adultresolver.resolve(url)
		quit()
	elif 'watchpornfree.info' in url:
		adultresolver.resolve(url)
		quit()
	else:
		return url
		