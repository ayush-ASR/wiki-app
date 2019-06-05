import wikipedia
from flask import Flask, request, render_template
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET': 
        return render_template("index.html")
    else:
        query=request.form.get("query")
        #return (wikipedia.summary(query))
        try:
            return (wikipedia.summary(query))
        except wikipedia.exceptions.DisambiguationError as e:
            return str(e.options)
        except wikipedia.exceptions.PageError:
            return (query+" doesnot match any pages. Try another query")
        
if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
