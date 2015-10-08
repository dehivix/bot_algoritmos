import urllib2

def wiki(term): # wiki <search term>
    #import ipdb; ipdb.set_trace()
    'Returns a wiki link and the first paragraph of the page'

    main_page = 'http://es.wikipedia.org/wiki/Main_Page'
    print "Going to fetch wiki of %s" % term.text
    wlink = term.text.strip('/wiki').lstrip(' ').replace(' ', '_')
    if 1 == len(wlink): # no search term given, the Main_Page is "displayed"
        response = main_page
    else:
        #search_term = wlink[1].lstrip().replace(' ', '_')
        search_term = wlink.replace(' ', '_')
        #print search_term

        if len(search_term) < 1:
            response = main_page
        else:
            response = 'http://es.wikipedia.org/wiki/' + search_term

    response = get_para(response)

    return response.encode('utf-8')

def get_para(wlink):
    msg = ''
    try:
        page_request = urllib2.Request(wlink)
        page_request.add_header('User-agent', 'Mozilla/5.0')
        page = urllib2.urlopen(page_request)
    except IOError:
        msg = 'No hay articulos en Wikipedia, tal vez quieras buscarlo en Google!'

    else:
        msg = wlink

    return msg
