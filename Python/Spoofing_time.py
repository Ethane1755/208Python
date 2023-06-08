from datetime import datetime

time_now = 1400#int(datetime.now().strftime('%H%M'))
time_zone= 8
time_start = int(input('Input the time the activity starts.'))
time_end = int(input('Input the time the activity ends.'))
time = int(time_end)-int(time_start)

i=0
time_list = []
location = {
    'Zaragoza, Spain' : '41.661130,-0.893750',
    'Dubai, United Arab Emirates ' : '25.076303,55.132383',
    'Budapest, Hungary' : '47.529972,19.051153',
    'Gran Canaria, Canary Islands' : '28.12976,-15.45106',
    'Saõ Paulo, Brazil' : '-23.550572,-46.657470',
    'Oeiras, Portugal' : '38.699629,-9.300969',
    'Guayas, Ecuador' : '-2.102919,-79.907980',
    'Lima, Peru' : '-11.562937,-77.270209',
    'Minnesota Landscape Arboretum' : '44.859873,-93.618821'
}

cities = {
    'Pier 39 - San Francisco, CA' : '37.808864,-122.409786',
    'Santa Monica Pier - Santa Monica, CA' : '34.008976,-118.497452',
    'Busan, South Korea' : '35.153662,129.060283',
    'Tottori Dunes - Tottori, Japan' : '35.542978,134.223962',
    'Olympic Park - Seoul, South Korea' : '37.518103,127.124086',
    'San Diego Zoo - San Diego, CA' : '32.735302,-117.155184',
    'Mexico City, Mexico' : '19.427393,-99.193284',
    'Bucharest, Romania' : '44.456930,26.082360',
    'Paris, France' : '48.855218,2.346307',
    'Barcelona, Spain' : '41.391129,2.164906',
    'London, England' : '51.512369,-0.119003',
    'Vienna, Austria' : '48.209445,16.372196',
    'Sydney, Australia' : '-33.861898,151.210024',
    'Boston, MA' : '42.358814,-71.056500',
    'New York City, NY' : '40.755931,-73.984606',
    'Melbourne, Australia' : '-37.815114,144.966514',
    'Florence, Italy' : '43.776737,11.257311',
    'Amsterdam, Netherlands' : '52.373166,4.890620',
    'Philadelphia, PA' : '39.954647,-75.164452',
    'San Francisco, CA ' : '37.785583,-122.415337',
    'Madrid, Spain' : '40.423504,-3.700581',
    'Tokyo, Japan' : '35.691619,139.696914',
    'Prague, Czechia' : '50.088015,14.422866',
    'Buenos Aires, Argentina' : '-34.599085,-58.398801',
    'Brussels, Belgium' : '50.845710,4.355076',
    'Berlin, Germany' : '52.516991,13.407505',
    'Munich, Germany' : '48.136378,11.578512',
    'Dublin, Ireland' : '53.343987,-6.266908',
    'Los Angeles, CA' : '34.053331,-118.242341',
    'Chicago, IL' : '41.876136,-87.629140',
    'Osaka, Japan' : '34.693759,135.501064',
    'Taipei City, Taiwan' : '25.033612,121.553963',
    'Seoul, South Korea' : '37.551167,126.939058',
    'Rio de Janeiro, Brazil' : '-22.912900,-43.177271',
    'Rome, Italy' : '41.914208,12.484971',
    'Atlanta, GA' : '33.756025,-84.388758',
    'Moscow, Russia' : '55.761583,37.609466',
    'Pune, India' : '18.5138342, 73.85366767',
    'St. Louis, Mo' : '38.635791,-90.288158',
    'Honululu, Hi' : '21.2736111,-157.8202778'
}

if time_now < time_start:
    k = time_zone - abs(2400+time_now - time_start)/100
else:
    k = time_zone - abs(time_now - time_start)/100
while time*i + 200*i < 2400 and 12 >= k >= -12:
    time_list.append(round(k))
    k = k-time/100-2
    i+=1

list = []
for i in time_list:
    print('GMT',str(i))
    long = 15*i
    for j in location:
        if long - 15 < float((location[j].split(',',1))[1]) < long +15:
            print (j,'\n'+str(location[j]),'\n')
            break
    for k in cities:
        if long - 15 < float((cities[k].split(',',1))[1]) < long +15:
            list.append(k)
            print (list[0]+'\n'+str(cities[list[0]]),'\n')
            list.remove(list[0])
    print('===')
