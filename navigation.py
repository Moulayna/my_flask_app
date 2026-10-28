def navigation():
    navbar=["Home", "Projects", "CV", "Publications"]
    nav= "<nav>" 
    for i in navbar:
        nav += '<a style ="border:solid" href="/'+ i.lower() +'">'+ i +'</a>'
    nav += "</nav>"
    return nav
def projects_bar():
    navbar=["Health", "HAII", "Responsible Design"]
    nav= "<nav>" 
    for i in navbar:
        nav += '<a style ="border:solid" href="/'+ i.lower() +'">'+ i +'</a>'
    nav += "</nav>"
    return nav