import flet as ft
import copy
import json
import os

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    LG = "#97CE8B"
    DG = "#5ca38f"
    W = "#FFFFFF"
    P= "#e53e34"
    B= "#000000"

    #edit this to add more features ltr 
    empty_person = {
        "username": "",
        "password": "",
        "profile": {
            "age": None,
            "gender": None,
            "race": None,
            "family_history": [],
        },
        "ai_recommendations": {
            "daily_calorie_target": None,
            "food_group_targets": {},
        },
        "calendar": {},
        "family_links": [],
    }

    family = {}


    

    APP_FOLDER = os.path.dirname(os.path.abspath(__file__))
    DATA_FILE = os.path.join(APP_FOLDER, "family_data.json")

    def save_family():
        with open(DATA_FILE, "w") as thef:
            json.dump(family, thef, indent=4)

    def load_family():
        try:
            with open(DATA_FILE, "r") as thef:
                family = json.load(thef)
        except FileNotFoundError:
            family = {}
        return family
    family = load_family()  


#CODEWITHDEFINED VARIABLES
    
    def gotosignup(e):
         current_view.content= page_2
         current_view.update()

    def gotologin(e):
         
         current_view.content= page_1
         current_view.update()
    vis= [False]

    def visibility(e):
         if not vis[0]:
           eye1.content= ft.Icon(ft.Icons.VISIBILITY_OFF, color= W)
           info2.password= False 
           vis[0]= True
         else:
             eye1.content= ft.Icon(ft.Icons.VISIBILITY, color= W)
             info2.password= True
             vis[0]= False
         eye1.update(
        )
         info2.update()
         page_1.update()

    fiz= [False]
    
    def visibility2(e):
             if not fiz[0]:
               eye2.content= ft.Icon(ft.Icons.VISIBILITY_OFF, color= W)
               info22.password= False 
               fiz[0]= True
             else:
                 eye2.content= ft.Icon(ft.Icons.VISIBILITY, color= W)
                 info22.password= True
                 fiz[0]= False
             eye2.update(
            )
             info22.update()
             page_2.update()
                      
    

    



         










#WIDGETS

    circle = ft.Container(
        width=100,
        height=100,
        bgcolor=LG,
        border_radius=ft.BorderRadius.all(200),
        opacity=1,
        top=-20,
        left=40
    )
    circle_1= ft.Container(
        width=180,
        height=180,
        bgcolor=LG,
        border_radius=ft.BorderRadius.all(400),
        opacity=1,
        top=120,
        right=-80

    )
    square_1= ft.Container(
        width=400,
        height=850,
        bgcolor=W,
        border_radius=ft.BorderRadius.all(0),
        opacity=1,
        top=250,
        bottom=50
    )
    logo= ft.Image(
        src="Vale Logo (4).png",
        width=250,
        height=250,
        border_radius=ft.BorderRadius.all(0),
        top=35,
        left=75,
        opacity=1

    )

    circle_3= ft.Container(
        width=180,
        height=180,
        bgcolor=LG,
        border_radius=ft.BorderRadius.all(200),
        opacity=1,
        top=700,
        left=-20
    
    )

    Welcome= ft.Text(
        "Welcome Back!",
        size=25,
        weight=ft.FontWeight.BOLD,
        color=DG,
        top=280,
        left=105
    )
    instruc= ft.Text(
        " Enter your email and password:",
        weight=ft.FontWeight.BOLD,
        color=DG,
        top=320,
        left=93
    )

    eye1= ft.Container(
            content= ft.Icon(ft.Icons.VISIBILITY,color=W),
            on_click=visibility)
    
    eye2= ft.Container(
                content= ft.Icon(ft.Icons.VISIBILITY,color=W),
                on_click=visibility2)
    warn1= ft.Text(
            "Password must include atleast 6 characters.",
            color= P,
            size= 12,
            top= 610,
            left=75
        )
    
    
    info = ft.TextField(
            hint_text="Email",
            prefix_icon=ft.Icon(ft.Icons.PERSON, color=W, size=25
                                ),
            color=W,
            bgcolor=DG,
            hint_style=ft.TextStyle(color=W),
            border_radius=ft.BorderRadius.all(30),
            border_color="transparent",
            content_padding= ft.Padding.symmetric(horizontal=20, vertical=0),
            top=360,
            left=50,
            width=300,
            height=40
        )
          
   
    info2 = ft.TextField(
             hint_text="Password",
             prefix_icon=ft.Icon(ft.Icons.LOCK, color=W), 
             bgcolor=DG,
             suffix_icon= eye1,
             color=W,
             hint_style=ft.TextStyle(color=W),
             border_radius=ft.BorderRadius.all(30),
             border_color="transparent",
             content_padding= ft.Padding.symmetric(horizontal=20, vertical=0),
             top=405,
             left=50,
             width=300,
             height=40
    )
    info22 = ft.TextField(
                 hint_text="Password",
                 prefix_icon=ft.Icon(ft.Icons.LOCK, color=W), 
                 bgcolor=DG,
                 suffix_icon= eye2,
                 color=W,
                 hint_style=ft.TextStyle(color=W),
                 border_radius=ft.BorderRadius.all(30),
                 border_color="transparent",
                 content_padding= ft.Padding.symmetric(horizontal=20, vertical=0),
                 top=405,
                 left=50,
                 width=300,
                 height=40
        )
    

#this code must be here
    
    def newacc(e):
        if len(info22.value)<6:
            page_2.content.controls.append(warn1)
            page_2.update()

        else:
            new_person = copy.deepcopy(empty_person)
            new_person['username'] = info.value
            new_person['password'] = info22.value
            family[info.value] = new_person
            save_family()
            current_view.content= page_3
            current_view.update()

        

    squarelog= ft.Button(
        content= ft.Text("Log In", color=W,size=20),
        bgcolor=LG,
        top=460,
        left=50,
        width=300,
        height=30,
        style= ft.ButtonStyle( shape= ft.RoundedRectangleBorder(radius=5)),

    )

    up=  ft.TextButton(
                    ft.Text("Don't have an account? Sign Up", color=DG, bgcolor="transparent"),
                    top=485,
                    left=87,
                    on_click= gotosignup
                )

    
    
    
   

    

    Sign= ft.Text(
                "Sign Up",
                size=25,
                weight=ft.FontWeight.BOLD,
                color=DG,
                top=280,
                left=148,
                

    )

    squaresign= ft.Button(
            content= ft.Text("Sign Up", color=W,size=20),
            bgcolor=LG,
            top=460,
            left=50,
            width=300,
            height=30,
            style= ft.ButtonStyle( shape= ft.RoundedRectangleBorder(radius=5)),
            on_click= newacc
    
        )
    log=  ft.TextButton(
                        ft.Text("Already have an account? Log In", color=DG, bgcolor="transparent"),
                        top=485,
                        left=87,
                        on_click=gotologin)
    
    OrS= ft.Text(
        "Or sign up with",
        color= DG,
        top=530,
        left=155)
    
    circle4=ft.Container(
        width=100,
        height=100,
        bgcolor=LG,
        border_radius=ft.BorderRadius.all(200),
        opacity=1,
        top=20,
        right=-20
    )

    circle5= ft.Container(
        width=180,
        height=180,
        bgcolor=LG,
        border_radius=ft.BorderRadius.all(400),
        opacity=1,
        top=120,
        left=-80)

    circle6= ft.Container(
        width=180,
        height=180,
        bgcolor=LG,
        border_radius=ft.BorderRadius.all(200),
        opacity=1,
        top=700,
        right=-20
    
    )

    menu1= ft.Container(
         content= ft.Icon(ft.Icons.MENU, color=  W,),
         top=20,
         left=20,
        
    )
    circle7 = ft.Container(
            width= 80,
            height=80,
            bgcolor=LG,
            border_radius=ft.BorderRadius.all(200),
            opacity=1,
            top=630,
            left=100
        )
    circle8=ft.Container(
            width= 150,
            height= 150,
            bgcolor=LG,
            border_radius=ft.BorderRadius.all(200),
            top= 670,
            left=-60
            )

    circle9=ft.Container(
                width= 190,
                height= 190,
                bgcolor=LG,
                border_radius=ft.BorderRadius.all(200),
                bottom= -60,
                left= 100
                )
    surv= ft.Text(
        "Survey:",
        size=70,
        weight=ft.FontWeight.BOLD,
        color=W,
        top=170,
        left=40
    )
    v= ft.Text(
        "Vale",
        size=70,
        weight=ft.FontWeight.BOLD,
        color=W,
        top=100,
        left=40

    )
    w= ft.Text(
            "Welcome to Vale!",
            size=20,
            weight=ft.FontWeight.NORMAL,
            color=W,
            top=280,
            left=50
    
        )
    intro= ft.Text(
                "We'll ask a few quick questions about your"
                "age, family health history, and activity level."
                "This helps Vale create nutrition targets that are actually personalised to you, not just a"
                "generic calorie count. It takes about 2 minutes."
                "Please don't close the app while"
                " completing this, since your answers won't"
                "be saved until you finish. Click “Next” to continue.",
                size=13,
                weight=ft.FontWeight.NORMAL,
                color=W,
                width= 280,
                top=320,
                left=50
        
            )
    nextb= ft.Button(
        bgcolor="Transparent",
        top= 500,
        left= 40,
        width= 200,
        height= 60,
        content= ft.Row(
            controls= [ft.Text("Next", size= 30, color= W),
                   ft.Icon(ft.Icons.ARROW_RIGHT,size=30,color=W)
                   ], 
                   alignment = ft.MainAxisAlignment.CENTER,
                   spacing=8,
        
        ))
    circle10= ft.Container(
                width= 150,
                height= 150,
                bgcolor=LG,
                border_radius=ft.BorderRadius.all(200),
                bottom= 600,
                right=-30
                )
    circle11= ft.Container(
                    width= 90,
                    height= 90,
                    bgcolor=LG,
                    border_radius=ft.BorderRadius.all(200),
                    top=-10,
                    right=80
                    )
    Basic= ft.Text(
            "Basic Cohorts",
            size=50,
            weight=ft.FontWeight.BOLD,
            color=W,
            top=90,
            left=38
        )
    Age= ft.Container(
        width=330,
        height=60, 
        bgcolor= ft.Colors.with_opacity(0.4,B),
        top= 180,
        left=36,
        border_radius=ft.BorderRadius.all(5),
        content= ft.Stack(
        controls=[
                ft.Text(
                "1. What is your age?",
                color=W,
                weight=ft.FontWeight.NORMAL,
                size=15,
                top=5,
                left=15,
                opacity=1,
            ),
            ft.TextField(
                bgcolor="transparent",
                color=W,
                border_color="transparent",
                top=14,  
                left=0,
                width=280,
                height=45,

            ),
        ]
    ),
)
    gender = ft.Container(
        width=300,
        height=100,
        bgcolor=ft.Colors.with_opacity(0.4, B),
        top=300,
        left=36,
        border_radius=ft.BorderRadius.all(5),
        content= ft.Stack(
        controls=[ 
            ft.Text('2. What is your gender', color= W, size=14,left= 10, top=5 ),
            ft.RadioGroup(
        content=ft.Stack(
            controls=[
                ft.Radio(value="male", label="Male",scale=0.8,top=20, left= 5),
                ft.Radio(value="female", label="Female",scale=0.8,top=40, left=5),
                ft.Radio(value="other", label="Other", scale=0.8,top=60, left=5),
            ]
        )
    ),
        ]
)
    )


                      
                
                
                
    
                  









    
    
    
               


#PAGES
    page_4= ft.Container(width=400,
                        height=850,
                        bgcolor=DG,
                        border_radius=ft.BorderRadius.all(35),

    
                        content=ft.Stack(
                                controls=[
                                ft.Container(
                                width=400,
                        height=850,
                        bgcolor=DG,
                        border_radius=ft.BorderRadius.all(35),
                        ),
                        circle7,
                        circle8,
                        circle9,
                        circle10,
                        circle11,
                        Basic,
                        Age,
                        gender
                        ]))


    page_3= ft.Container(width=400,
                        height=850,
                        bgcolor=DG,
                        border_radius=ft.BorderRadius.all(35),

    
                        content=ft.Stack(
                                controls=[
                                ft.Container(
                                width=400,
                        height=850,
                        bgcolor=DG,
                        border_radius=ft.BorderRadius.all(35),
                        ),
                        circle7,
                        circle8,
                        circle9,
                        surv,
                        v,
                        w,
                        intro,
                        nextb,
                        circle10,
                        circle11,
                        

                        ]))
                        
                                                       

    

    page_2 = ft.Container(
                    width=410,
                    height=870,
                    bgcolor=DG,
                    border_radius=ft.BorderRadius.all(35),

                        
                    content=ft.Stack(
                            controls=[
                            ft.Container(
                            width=400,
                            height=850,
                            bgcolor=DG,
                            border_radius=ft.BorderRadius.all(35),
                                    ),
                                    logo,
                                    square_1,
                                    circle4,
                                    circle6,
                                    circle5,
                                    Sign,
                                    instruc,
                                    info,
                                    info22,
                                    squaresign,
                                    log,
                                    
                                    
                    
                                    ]
                                
                                )
                    
                        
                        )
                                

    page_1 = ft.Container(
            width=410,
            height=870,
            bgcolor=DG,
            border_radius=ft.BorderRadius.all(35),
    
            content=ft.Stack(
                controls=[
                ft.Container(
                    width=400,
                    height=850,
                    bgcolor=DG,
                    border_radius=ft.BorderRadius.all(35),
                ),
                  logo,
                  circle,
                  square_1,
                  circle_1,
                  circle_3,
                  Welcome,
                  instruc,
                  info,
                  info2,
                  squarelog,
                  up,
                  
                  
                  
                

                ]
            
            )

    
    )
                  
            
    
    

    

    

#CODE


























    current_view = ft.Container(
           width=400, height=850, bgcolor=LG,
           border_radius=ft.BorderRadius.all(35),
           content=page_4,
           animate= ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
           animate_offset= ft.Animation(300, ft.AnimationCurve.EASE_IN),
           offset=ft.Offset(0,0)
    )

    outer_stack = ft.Stack(
        controls=[
            page_3,
            current_view
        ]
    )
    page.add(outer_stack)



ft.app(target=main, view=ft.AppView.WEB_BROWSER)
#python -c "import sys; from flet.cli import main; sys.argv = ['flet', 'run', 'Untitled-1.py', '--web']; main()"
#Remove-Item family_data.json        
#To do list :
# Create survey










