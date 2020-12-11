from extract_post import get_content
import re

content = get_content()
title = content[0]
body = content[1]



pattern_1 = '</pre>'
pattern_2 = '\xa0|\u200a'
pattern_3 = '(?s)<figure>.*?</figure>|(?s)<a href.*?>|(?s)<img src.*?>|</a>'
pattern_4 = "<strong>|</strong>|<ul>|</ul>|<li>|</li>|</h3>|<hr>"
pattern_5 = '\d\D\s'
pattern_6 = '\s(.yml)'
pattern_7 = '(— all)'

body_beginning = '<speak><prosody volume="loud">'
title_end = '</prosody> '
body_end = '</speak>'


patterns = [pattern_1,pattern_2, pattern_3,pattern_4,pattern_5]
replacement_1 = ['.</pre>',' ','','','' ]
substitutions_1 = dict(zip(patterns,replacement_1))


tags = ['<p>', '</p>', '<pre>', '</pre>', '<em>', '</em>','<br>','<h3>', '<blockquote>', '</blockquote>']
replacement_2 = ['<p>', '</p>', '<amazon:effect name="drc">','</amazon:effect>',
              '<amazon:domain name="news">', '</amazon:domain>','<break strength="strong"/>' ,
              '<break time="1s"/><break strength="strong"/>','<amazon:domain name="news">', '</amazon:domain>' ]
substitutions_2 = dict(zip(tags,replacement_2))

def substitute_tags(body, substitutions_1):
    new_body = body
    for i, v in substitutions_1.items():
        new_body = re.sub(i,v,new_body)
    return new_body


def add_paragraph_tags(body):
    new = body.split('\n')
    new_list = []
    for i in new:
        if len(i)!=0 and not i.startswith('<'):
            i = '<p>'+ i +'</p>'
        new_list.append(i)

    return new_list

def remove_commentary(body):
    new_list = add_paragraph_tags(body)
    new = []

    for i in new_list:
        if 'Fritz' not in i and 'Heartbeat' not in i and not i.startswith('</'):
            new.append(i)
    new_string = ''.join(new)
    new_string = new_string.strip()
    return new_string

def replace(string, substitutions):

    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)

def add_ssml_to_keywords(output):
    output = re.sub(pattern_6, '<say-as interpret-as="ordinal">.yml</say-as>', output)
    output = re.sub(pattern_7, '<say-as interpret-as="ordinal">—</say-as>all', output)
    return output

def get_title_and_body_content(output):
    total_content = body_beginning +  title + title_end + output + body_end
    total_content = total_content.strip()
    return total_content

def return_total_clean_content():
        body_new = substitute_tags(body, substitutions_1)
        body_clean = remove_commentary(body_new)
        output = replace(body_clean, substitutions_2)
        output_new = add_ssml_to_keywords(output)
        total_content = get_title_and_body_content(output_new)
        return total_content


if __name__ == "__main__":
    return_total_clean_content()
    










