# Ticapsoriginal_tags_google_trends_analisys
Ticapsoriginal analisys tags on google trends

# make python environment:
* Install pip first:
<pre><code>sudo apt-get install python3-pip
</code></pre>
* Then install virtualenv using pip3
<pre><code>sudo pip3 install virtualenv 
</code></pre>
* Now create a virtual environment
<pre><code>virtualenv venv
</code></pre>
* Active your virtual environment:
<pre><code>source venv/bin/activate
</code></pre>
* Enter on environment:
<pre><code>cd venv
</code></pre>

## Install tqdm to see progress bar: 
<pre><code>pip install tqdm
</code></pre>

## Install pytrends to make request of trends data: 
<pre><code>pip install pytrends
</code></pre>

## Install plotly to see trends ploted: 
<pre><code>pip install plotly
</code></pre>

## Clone Ticapsoriginal google trends tag ploted trends:
<pre><code> git clone https://github.com/Tinoco/Ticapsoriginal_site_wide_full_text_extract.git
</code></pre>

* Change the trendtopic.py multiply_args_list variable with your tags

## Start plot:
<pre><code>python trendtopic.py
</code></pre>

![](https://desembo.la/assets/ticapstrendsanal.png)

## quality:
* [`100% pycodestyle coverage`](https://pypi.org/project/pycodestyle/)

* [`0% code plagiarism detected`](https://github.com/blingenf/copydetect)

## about:
* code and resource used in [`Ticapsoriginal`](https://ticapsoriginal.com)
