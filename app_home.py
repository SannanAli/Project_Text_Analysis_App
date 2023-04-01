import streamlit  as st
import neattext.functions as nfx
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pylab as plt
import matplotlib
matplotlib.use('Agg')
import streamlit.components.v1 as stc
from collections import Counter
from textblob import TextBlob


def plot_wordcloud(my_text):
    my_wordcloud = WordCloud().generate(my_text)
    fig = plt.figure()
    plt.imshow(my_wordcloud,interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)

def get_most_common_words(my_text,num = 7):
    word_tokens = Counter(my_text.split())
    most_common = dict(word_tokens.most_common(num))
    return most_common

#plotting stylometry curve also called mendelhal curve

def plot_mendelhal_curve(my_text):
    word_length = [len(token) for token in my_text.split()] #getting the length of token in list
    word_length_count = Counter(word_length) #frequency of words
    sorted_word_length_count = sorted(dict(word_length_count).items())
    x,y = zip(*sorted_word_length_count)
    mendelhal_curve = pd.DataFrame({'tokens':x,'counts':y})
    st.line_chart(mendelhal_curve['counts'])

def get_POS_tag(my_text):
    blob = TextBlob(my_text)
    pos_tags = blob.tags
    pos_tags_df = pd.DataFrame(pos_tags,columns=['Token','Tags'])
    return pos_tags_df

TAGS = {
            'NN'   : 'green',
            'NNS'  : 'green',
            'NNP'  : 'green',
            'NNPS' : 'green',
            'VB'   : 'blue',
            'VBD'  : 'blue',
            'VBG'  : 'blue',
            'VBN'  : 'blue',
            'VBP'  : 'blue',
            'VBZ'  : 'blue',
            'JJ'   : 'red',
            'JJR'  : 'red',
            'JJS'  : 'red',
            'RB'   : 'cyan',
            'RBR'  : 'cyan',
            'RBS'  : 'cyan',
            'IN'   : 'darkwhite',
            'POS'  : 'darkyellow',
            'PRP$' : 'magenta',
            'PRP$' : 'magenta',
            'DET'   : 'black',
            'CC'   : 'black',
            'CD'   : 'black',
            'WDT'  : 'black',
            'WP'   : 'black',
            'WP$'  : 'black',
            'WRB'  : 'black',
            'EX'   : 'yellow',
            'FW'   : 'yellow',
            'LS'   : 'yellow',
            'MD'   : 'yellow',
            'PDT'  : 'yellow',
            'RP'   : 'yellow',
            'SYM'  : 'yellow',
            'TO'   : 'yellow',
            'None' : 'off'
        }

def mytag_visualizer(my_text):
    color_text = []
    for i in my_text:
        if i[1] in TAGS.keys():
            token = i[0]
            color_for_tag = TAGS.get(i[1])
            result = '<span style = "color:{}">{}</span>'.format(color_for_tag,token)
            color_text.append(result)
    result = ' '.join(color_text)
    return result


def home():
    raw_text = st.text_area(':blue[Paste Your Text Below]')

    if raw_text is not None:

        if st.button('ANALYSE'):

            c1,c2 = st.columns(2)

            with c1:
                with st.expander('Original Text'):
                    st.write(raw_text)


                with st.expander('POS Tagged Text'):
                    tag_docx = get_POS_tag(raw_text)
                    st.dataframe(tag_docx)

                    taged_docx = TextBlob(raw_text).tags
                    color_tags  = mytag_visualizer(taged_docx)
                    stc.html(color_tags,scrolling=True)


                with st.expander('Word Frequency Plot'):
                    stop_words_removed = nfx.remove_stopwords(raw_text)
                    most_common = get_most_common_words(stop_words_removed)
                    fig = plt.figure()
                    top_most_common = get_most_common_words(
                        stop_words_removed
                    )
                    plt.bar(most_common.keys(),top_most_common.values())
                    plt.xticks(rotation = 45)
                    st.pyplot(fig)


            with c2:
                with st.expander('Processed Text'):
                    st.info("Stopword are removed")
                    stop_words_removed = nfx.remove_stopwords(raw_text)
                    st.write(stop_words_removed)


                with st.expander('Stylometry Curve plot'):
                    st.info("plot_mendelhal_curve")
                    plot_mendelhal_curve(raw_text)


                with st.expander('Wordcloud Plot'):
                    plot_wordcloud(raw_text)
