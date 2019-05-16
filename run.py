from zeplin.api import ZeplinAPI
from zeplin.project import Project

if __name__ == "__main__":
    z = ZeplinAPI('asdf', 'asdf', True)
    

    p = Project('5c49ce9866e3b3bee966f431', z)
    s = p.get_screen('5ccaf241df6a8967aeb5174c')
    s.get_url()
    import pdb; pdb.set_trace()


    
    get_project(session, '5c49ce9866e3b3bee966f431')
    # print(get_screen_info('https://app.zeplin.io/project/5af063c9b4dc859b6bdaf897/screen/5c792cac4e848abc6c6303bf', session))
    