# Relational-Interval-Geometry
Simple demos to show users how to use the PhD code components, and what is neat about them.  
Also to help me formulate better presentations.  We will see how it goes!


### How do I get set up? ###

* First, you will need my big PhD code dump.  Sorry!  Don't focus on the mess, just install it this way:
    *  Pull the code here:
    git clone https://github.com/LukeMcCulloch/feasible-form-parameter-design
    *  Assuming dependencies are met (see below), go to the top level directory (where setup.py is found)
    and run
    > pip install .

    to install.
    *  Or
    > pip install . --upgrade
    
    to update after making changes.
    *  import relational_lsplines to access the code.
    
* Second, pull this repo.  It will contain demos and samples using pieces of my code installed above.
    *  The idea is to break out your interpreter and have fun!
    *  Isn't that always the idea??
  

## Building slides and hosting on github pages
[From here](https://medium.com/learning-machine-learning/present-your-data-science-projects-with-jupyter-slides-75f20735eb0f)

### How to build slides of a jupyter notebook
 * convert the jupyter notebook to slides:
  
   jupyter nbconvert ADdemo.ipynb --to slides --post serve

 * jupyter nbconvert ADdemo.ipynb --to slides --post serve 
--SlidesExporter.reveal_theme=serif 
--SlidesExporter.reveal_scroll=True 
--SlidesExporter.reveal_transition=none


### How to host on github pages
