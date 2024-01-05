#!/usr/bin/env python
# coding: utf-8

# In[9]:


# linkcreator.py


def create_link(link_text, url):
    
    """
    Create a clickable link in Jupyter Notebook.

    Parameters:
    - link_text (str): The text to be displayed for the link.
    - url (str): The URL to link to.

    Example:
    create_link("Visit Example Website", "https://www.example.com")
    
    By Omkar Jagtap (omkarjagtap9773@gmail.com)
    """
    from IPython.display import HTML
    html_link = f'<a href="{url}" target="_blank">{link_text}</a>'
    display(HTML(html_link))


# In[ ]:




