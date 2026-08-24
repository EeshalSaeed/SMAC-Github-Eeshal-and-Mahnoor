import asyncio
from tkinter import NORMAL
from turtle import done
from cv2 import FILLED, repeat
import flet as ft
import copy
import json
import os
import flet_video
import flet_camera
import random

async def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    LG = "#97CE8B"
    DG = "#5ca38f"
    W = "#FFFFFF"
    P= "#e53e34"
    B= "#000000"
    DDG= "#4c9d86"
    LLG="#8FC682"
    VDG= "#295549"

   
    empty_person = {
        "name": "",
        "profile": {
            "age": None,
            "gender": None,
            "ancestry": None,
            "height": None,
            "weight": None,
            "activity_level": None,
            "family_history": {
                "conditions": [],
                "conditions_other": "",
                "affected_members": [],
                "affected_members_other": "",
            },
        },
        "ai_recommendations": {
            "daily_calorie_target": None,
            "food_group_targets": {},
        },
        "calendar": {},
    }

    empty_account = {
        "username": "",
        "password": "",
        "members": {},
    }


    

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
    current_user = [None]
    current_member = [None]

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
    def opensurvey(e): 
        current_view.content= page_4 
        current_view.update()         
    def nextpage(e):
        timeline(e)
        if current_view.content== page_4:
            current_view.content= page_5
            current_view.update()
            
        elif current_view.content== page_5:
            current_view.content= page_6
            current_view.update()
            
        elif current_view.content== page_6:
            current_view.content= page_7
            current_view.update()
        

    def timeline(e): 
        if current_view.content== page_4:
            T1.bgcolor= "Trasparent"
            T1.border= ft.Border.all(2, ft.Colors.WHITE)
            T1.content= ft.Text("1", color=W)
            T1.update()
            T2.bgcolor= W
            T2.content= ft.Text("2", color=DG)
            T2.update()
            T3.bgcolor= "Transparent"
            T3.update()
        elif current_view.content== page_5:
            T1.bgcolor= "Trasparent"
            T1.border= ft.Border.all(2, ft.Colors.WHITE)
            T1.content= ft.Text("1", color=W)
            T1.update()
            T3.bgcolor= W
            T3.content= ft.Text("3", color=DG)
            T3.update()
            T2.bgcolor= "Transparent"
            T2.border= ft.Border.all(2, ft.Colors.WHITE)
            T2.content= ft.Text("2", color=W)
            T2.update()
    def start(e):
        current_view.content= page_1
        current_view.update()
    async def ahh():
        await asyncio.sleep(0.5)
        screen.jump_to(0)
        screen.play()
        await asyncio.sleep(7.3)
        current_view.content = page_9
        current_view.update()   
    def m(e):
        if current_view.content== page_10:
          current_view.content= page_9
          current_view.update()
        else:
            current_view.content= page_10
            current_view.update()
    def getcamera(cameras):
        cam=[]
        for i in cameras:
            if i.lens_direction==flet_camera.CameraLensDirection.FRONT:
                cam.append(i)
                return cam
    async def opencam(e):
        tp= await camera.get_available_cameras()
        camtype= getcamera(tp)
        if camtype:
           await camera.initialize(camtype[0], flet_camera.ResolutionPreset.VERY_HIGH, enable_audio=False)
        orderofmp.controls.reverse()
        orderofmp.update()
    async def takepic(e):
        photoholder[0]= await camera.take_picture()
        preview.src= photoholder[0]
        current_view.content= page_12
        current_view.update()
    async def AGAIN(e):
        orderofmp.controls.reverse()
        orderofmp.update()
        if current_view.content== page_12:
                            current_view.content= page_11
                            current_view.update()

        









#WIDGETS


#PAGE1:
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
    circle_1o1= ft.Container(
            width=240,
            height=240,
            border= ft.Border.all(color= LG, width=2),
            border_radius=ft.BorderRadius.all(400),
            opacity=1,
            top=680,
            right=-50

        )
    circle_2o1= ft.Container(
                width=50,
                height=50,
                border= ft.Border.all(color= LG, width=2),
                border_radius=ft.BorderRadius.all(400),
                opacity=1,
                top=50,
                left=60
        
            )
    circle_3o1= ft.Container(
                    width=50,
                    height=50,
                    border= ft.Border.all(color= LG, width=2),
                    border_radius=ft.BorderRadius.all(400),
                    opacity=1,
                    top=130,
                    left=30
            
                )
    circle_4o1= ft.Container(
                width=240,
                height=240,
                border= ft.Border.all(color= LG, width=2),
                border_radius=ft.BorderRadius.all(400),
                opacity=1,
                top=680,
                left=-50)
    
    square_1= ft.Container(
        width=400,
        height=850,
        bgcolor=W,
        border_radius=ft.BorderRadius.all(0),
        opacity=1,
        top=250,
        bottom=50,
        shadow= ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                offset=ft.Offset(0, 5),),
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
        left=120
    )
    instruc= ft.Text(
        " Enter your email and password:",
        weight=ft.FontWeight.NORMAL,
        color=DG,
        top=320,
        left=105
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
            height=40,
            
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
             top=410,
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
                 top=410,
                 left=50,
                 width=300,
                 height=40
        )
    connect= ft.Container(
        width=100,
        height=80,
        content= ft.Column(
            controls=
            [
            ft.Icon(ft.Icons.FAMILY_RESTROOM,size=50,color= DDG),
            ft.Text("Connect", size= 15, color= DDG)
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment = ft.MainAxisAlignment.CENTER,
            spacing=1,

            
        )
    )

    Track= ft.Container(
            width=100,
            height=80,
            
            content= ft.Column(
                controls=
                [
                ft.Icon(ft.Icons.RESTAURANT,size=50,color= DDG),
                ft.Text("Track", size= 15, color= DDG)
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment = ft.MainAxisAlignment.CENTER,
                spacing=1,
    
                
            )
        )

    personalise= ft.Container(
                width=100,
                height=80,
                content= ft.Column(
                    controls=
                    [
                    ft.Icon(ft.Icons.BAR_CHART,size=50,color= DDG),
                    ft.Text("Tailor", size= 15, color= DDG)
                    ], 
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing=1,
        
                    
                )
            )
    ctp= ft.Container(
        width=400,
        height=100,
        top=540,
        left=35,
        content= ft.Row(
        controls=[
                connect,
                Track,
                personalise
            ],
            spacing=20
        )
    )

#this code must be here
    
    def newacc(e):
        if len(info22.value)<6:
            page_2.content.controls.append(warn1)
            page_2.update()

        else:
            new_account = copy.deepcopy(empty_account)
            new_account['username'] = info.value
            new_account['password'] = info22.value

            first_member = copy.deepcopy(empty_person)
            first_member['name'] = info.value
            new_account['members'][info.value] = first_member

            family[info.value] = new_account
            save_family()

            current_user[0] = info.value
            current_member[0] = info.value

            current_view.content= page_3
            current_view.update()
           

#page2
    squarelog= ft.Button(
                    content= ft.Text("Log In", color=W,size=20),
                    bgcolor=LG,
                    top=460,
                    left=50,
                    width=300,
                    elevation=15,
                    height=30,
                    style= ft.ButtonStyle( shape= ft.RoundedRectangleBorder(radius=5)),
                    
    )

    up=  ft.TextButton(
                    ft.Text("Don't have an account? Sign Up", color=DG, bgcolor="transparent"),
                    top=500,
                    left=90,
                    on_click= gotosignup
                )

    
    
    
   

    

    Sign= ft.Text(
                "Create An Account!",
                size=25,
                weight=ft.FontWeight.BOLD,
                color=DG,
                top=280,
                left=100,
                

    )

    squaresign= ft.Button(
            content= ft.Text("Sign Up", color=W,size=20),
            bgcolor=LG,
            top=460,
            left=50,
            width=300,
            elevation= 15,
            height=30,
            style= ft.ButtonStyle( shape= ft.RoundedRectangleBorder(radius=5)),
            on_click= newacc
    
        )
    log=  ft.TextButton(
                        ft.Text("Already have an account? Log In", color=DG, bgcolor="transparent"),
                        top=500,
                        left=90,
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
#page3
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
                " age, family health history, and activity level."
                " This helps Vale create nutrition targets that are actually personalised to you, not just a"
                " generic calorie count. It takes about 2 minutes."
                " Please don't close the app while"
                " completing this, since your answers won't"
                " be saved until you finish. Click 'Next' to continue.",
                size=13,
                weight=ft.FontWeight.NORMAL,
                color=W,
                width= 280,
                top=320,
                left=50
        
            )
    nextb= ft.Button(
        bgcolor= ft.Colors.with_opacity(0.4,B),
        top= 500,
        left= 40,
        width= 200,
        elevation=15,
        height= 50,
         on_click= opensurvey,
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
#Page_4
    Basic= ft.Text(
            "Basic Cohorts",
            size=50,
            weight=ft.FontWeight.BOLD,
            color=W,
            top=90,
            left=55
        )
    age_field = ft.TextField(
        hint_text="Enter your age",
        hint_style=ft.TextStyle(color=ft.Colors.WHITE_70),
        bgcolor="transparent",
        color=W,
        border_color="transparent",
        top=14,  
        left=0,
        width=280,
        height=45,
    )
    Age= ft.Container(
        width=330,
        height=60, 
        bgcolor= ft.Colors.with_opacity(0.4,B),
        top= 180,
        left=35,
        shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                    offset=ft.Offset(0, 5),),
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
            age_field,
        ]
    ),
)
    gender_radio = ft.RadioGroup(
        content=ft.Column(
            controls=[
                ft.Radio(value="male", label="Male"),
                ft.Radio(value="female", label="Female"),
                ft.Radio(value="other", label="Prefer not to say"),
            ],
            spacing=0.1,
        )
    )
    gender = ft.Container(
        width=330,
        height=140,
        bgcolor=ft.Colors.with_opacity(0.4, B),
        top=260,
        left=35,
        shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                offset=ft.Offset(0, 5),),
        border_radius=ft.BorderRadius.all(5),
        content= ft.Stack(
        controls=[ 
            ft.Text('2. What is your gender', color= W, size=14,left= 10, top=5 ),
        ft.Container(
            gender_radio,
        
    top=30,
    left=5,
        ),
        ]
)
    )

    ancestry_radio = ft.RadioGroup(
        content=ft.Column(
            controls=[
                ft.Radio(value="caucasian", label="Caucasian"),
                ft.Radio(value="African", label="African"),
                ft.Radio(value="South Asian", label="South Asian"),
                ft.Radio(value="East Asian", label="East Asian"),
                ft.Radio(value="Hispanic", label="Hispanic"),
                ft.Radio(value="Middle Eastern", label="Middle Eastern"),
                ft.Radio(value="Other", label="Other"),
            ],
            spacing=0.1,
        )
    )
    ancestry = ft.Container(
            width=330,
            height=260,
            bgcolor=ft.Colors.with_opacity(0.4, B),
            top=420,
            shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                        offset=ft.Offset(0, 5),),
            left=35,
            border_radius=ft.BorderRadius.all(5),
            content= ft.Stack(
            controls=[ 
                ft.Text('3. What is your ancestry?', color= W, size=14,left= 10, top=5 ),
            ft.Container(
                ancestry_radio,
            
        top=30,
        left=5,
            ),
            ]
    )
        )
    nexta= ft.Button(
            bgcolor=ft.Colors.with_opacity(0.4, B),
            top= 730,
            left= 95,
            elevation= 15,
            width= 200,
            height= 50,
            on_click= nextpage,

            content= ft.Row(
                controls= [ft.Text("Next", size= 30, color= W),
                       ft.Icon(ft.Icons.ARROW_RIGHT,size=30,color=W)
                       ], 
                       alignment = ft.MainAxisAlignment.CENTER,
                       spacing=8,
            
            ))
    weight_field = ft.TextField(
        hint_text="eg: 75kg or 165lbs",
        hint_style=ft.TextStyle(color=ft.Colors.WHITE_70),
        bgcolor="transparent",
        color=W,
        border_color="transparent",
        top=14,  
        left=0,
        width=280,
        height=45,
    )
    weight= ft.Container(
            width=330,
            height=60, 
            bgcolor= ft.Colors.with_opacity(0.4,B),
            top= 180,
            left=35,
            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                                offset=ft.Offset(0, 5),),
            border_radius=ft.BorderRadius.all(5),
            content= ft.Stack(
            controls=[
                    ft.Text(
                    "4. What is your weight?",
                    color=W,
                    weight=ft.FontWeight.NORMAL,
                    size=15,
                    top=5,
                    left=15,
                    opacity=1,
                ),
                weight_field,
            ]
        ),
    )
    height_field = ft.TextField(
        hint_text="eg: 1.75m or 5'9\"",
        hint_style=ft.TextStyle(color=ft.Colors.WHITE_70),
        bgcolor="transparent",
        color=W,
        border_color="transparent",
        top=14,  
        left=0,
        width=280,
        height=45,
    )
    height = ft.Container(
                width=330,
                height=60, 
                bgcolor= ft.Colors.with_opacity(0.4,B),
                top= 260,
                left=35,
                shadow=ft.BoxShadow(
                                                spread_radius=1,
                                                blur_radius=15,
                                                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                                                offset=ft.Offset(0, 5),),
                border_radius=ft.BorderRadius.all(5),
                content= ft.Stack(
                controls=[
                ft.Text(
                        "5. What is your height?",
                        color=W,
                        weight=ft.FontWeight.NORMAL,
                        size=15,
                        top=5,
                        left=15,
                        opacity=1,
                    ),
                height_field,
                ]
            ),
        )
    activity_radio = ft.RadioGroup(
        content=ft.Column(
            controls=[
                ft.Radio(value="sedentary", label="Sedentary"),
                ft.Radio(value="light", label="Lightly Active"),
                ft.Radio(value="moderate", label="Moderately Active"),
                ft.Radio(value="very", label="Very Active"),
                ft.Radio(value="extra", label="Extremely Active")
            ],
            spacing=0.1,
        )
    )
    activity = ft.Container(
            width=330,
            height=270,
            bgcolor=ft.Colors.with_opacity(0.4, B),
            top=340,
            left=35,
            shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                        offset=ft.Offset(0, 5),),
            border_radius=ft.BorderRadius.all(5),
            content= ft.Stack(
            controls=[ 
                ft.Text('6. What is your activity level?', color= W, size=14,left= 10, top=5 ),
            ft.Container(
                activity_radio,
        top=30,
        left=5
                           
            
        ),
            ],
            ),
    )
    cb_heart = ft.Checkbox(label="Heart disease")
    cb_cholesterol = ft.Checkbox(label="High cholesterol")
    cb_obesity = ft.Checkbox(label="Obesity")
    cb_stroke = ft.Checkbox(label="Stroke")
    cb_diabetes = ft.Checkbox(label="Diabetes")
    cb_bp = ft.Checkbox(label="High blood pressure")
    cb_cancer = ft.Checkbox(label="Cancer")
    cb_none_history = ft.Checkbox(label="None of the above")
    history_other = ft.TextField(
        hint_text=("Other (please specify)"),
        hint_style=ft.TextStyle(color=ft.Colors.WHITE_70),
        width=200,
        height= 40,
        border_color="transparent",
    )
    history = ft.Container(
        width= 340,
        height=200,
        top=180,
        padding=ft.Padding.symmetric(vertical=10, horizontal=10),
        bgcolor= ft.Colors.with_opacity(0.4, B),
        border_radius=ft.BorderRadius.all(5),
        left= 30, 
        shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                                offset=ft.Offset(0, 5),),
        content=(  
            ft.Column(
            controls=[
                ft.Text(
                    "7. Do you have a family history of any of the following conditions?",
                    width=300,
                ),
            cb_heart,
            cb_cholesterol,
            cb_obesity,
            cb_stroke,
            cb_diabetes, 
            cb_bp,
            cb_cancer,
            cb_none_history,
            history_other,
            
            ],

            scroll=ft.ScrollMode.AUTO,
        )
    ) 
    )
    cb_grandparents = ft.Checkbox(label="Grandparents")
    cb_parents = ft.Checkbox(label="Parents")
    cb_uncles_aunts = ft.Checkbox(label="Uncles/Aunts")
    cb_siblings = ft.Checkbox(label="Siblings")
    cb_na = ft.Checkbox(label="N/A")
    fami_other = ft.TextField(
        hint_text=("Other (please specify)"),
        hint_style=ft.TextStyle(color=ft.Colors.WHITE_70),
        width=200,
        height= 40,
        border_color="transparent",
    )
    fami = ft.Container(
            width= 340,
            height=200,
            top=400,
            padding=ft.Padding.symmetric(vertical=10, horizontal=10),
            bgcolor= ft.Colors.with_opacity(0.4, B),
            left= 30, 
            border_radius=ft.BorderRadius.all(5),
            shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                            offset=ft.Offset(0, 5),),
            content=(  
                ft.Column(
                controls=[
                    ft.Text(
                        "8. Which of your family members have this condition? (Check all that apply)",
                        width=300,
                    ),
                cb_grandparents,
                cb_parents,
                cb_uncles_aunts,
                cb_siblings,
                fami_other,
                cb_na, 
                
                ],
    
                scroll=ft.ScrollMode.AUTO,
            )
        ) 
        )
    end= ft.Text(

        """
    You have officially
    completed the survey!
    Click "End" so that 
    we can save your results!""",
        size=25,
        weight= ft.FontWeight.NORMAL,
        color=W,
        top=260,
        left=20
    )            
    #function:
    def filtercblabels(cblabels):
        chosen=[]              
        for i in cblabels:
           if i.value:
             chosen. append(i.label)    
        return chosen
    
    def save_results(e):
        information=family[current_user[0]]['members'][current_member[0]]

        information['profile']['age']= age_field.value
        information['profile']['gender']= gender_radio.value
        information['profile']['ancestry']= ancestry_radio.value  
        information['profile']['weight']= weight_field.value
        information['profile']['height']= height_field.value
        information['profile']['activity_level']= activity_radio.value
        information['profile']['family_history']['conditions']= filtercblabels([cb_heart, cb_cholesterol, cb_obesity, cb_stroke, cb_diabetes, cb_bp, cb_cancer, cb_none_history])
        information['profile']['family_history']['conditions_other']= history_other.value
        information['profile']['family_history']['affected_members']= filtercblabels([cb_grandparents, cb_parents, cb_siblings, cb_na, cb_uncles_aunts])
        information['profile']['family_history']['affected_members_other']= fami_other.value
        save_family()
        print(information)

                    
    End= ft.Button(
        bgcolor=ft.Colors.with_opacity(0.4, B),
        top= 500,
        left= 40,
        width= 200,
        height= 50,
        elevation= 15,
        on_click= save_results,
        content= ft.Row(
            controls= [ft.Text("End", size= 30, color= W),
                   ft.Icon(ft.Icons.ARROW_RIGHT,size=30,color=W)
                   ], 
                   alignment = ft.MainAxisAlignment.CENTER,
                   spacing=7,
    
        )
    )
    gen= ft.Text(
        "Genetic History",
        size=50,
        weight=ft.FontWeight.BOLD,
        color=W,
        top=90,
        left=45
    )
    ac= ft.Text(
        "Activity Level",
        size=50,
        weight=ft.FontWeight.BOLD,
        color=W,
        top=90,
        left=60
    )
    T1= ft.Container(
            width=40,
            height=40,
            bgcolor=W,
            top=50,
            left=100,
            border_radius=5, 
            border=ft.Border.all(2, ft.Colors.TRANSPARENT), 
            alignment= ft.Alignment.CENTER,
            content=ft.Text("1", color=DG),
    )

    
    T2= ft.Container(
                width=40,
                height=40,
                top=50,
                left=180,
                bgcolor="Transparent",
                border_radius=5,
                border=ft.Border.all(2, ft.Colors.WHITE),
                alignment=ft.Alignment.CENTER,
                content=ft.Text("2", color=W),
    )


    
    T3= ft.Container(
                width=40,
                height=40,
                bgcolor="Transparent",
                top=50,
                left=260,
                border_radius=5,
                border=ft.Border.all(2, ft.Colors.WHITE),
                alignment=ft.Alignment.CENTER,
                content=ft.Text("3", color=W),
    )

    screen= flet_video.Video(
            playlist=[flet_video.VideoMedia(resource="ValeOpeningScreen3.mp4")],
            autoplay=True,
            controls=None,
            muted=True,
            width=400,
            height=840,
            fill_color= DDG,
            on_complete=ahh
            
           
    )    
    logo2= ft.Image(
        src= ('Vale Logo (5).png'),
        width=225,
        height=225,
        left=80,
        top= 140,
    )
    signlog= ft.Button(
         content= ft.Text("Sign Up/Login", color=W,size=25, weight=ft.FontWeight.W_100),
         bgcolor=ft.Colors.with_opacity(0.4, B),
         top=383,
         left=65, 
         width=270,
         height=50,
         elevation=15,
         style= ft.ButtonStyle( shape= ft.RoundedRectangleBorder(radius=5)),
         on_click= gotologin

    )
    learn= ft.Button(
             content= ft.Text("Learn About Vale", color=W,size=25, weight=ft.FontWeight.W_100),
             bgcolor=ft.Colors.with_opacity(0.4, B),
             top=463, 
             left=65,
             width=270,
             height=50,
             elevation= 15,
             on_click= m,
             style= ft.ButtonStyle( shape= ft.RoundedRectangleBorder(radius=5)),
    
        )
    learn1= ft.Text(
        "Learn About Vale",
        weight= ft.FontWeight.BOLD,
        size=44,
        color=W,
        top=60,
        left=45
       
    )
    team= ft.Text(
        "The Team!",
        weight= ft.FontWeight.BOLD,
        size=30,
        color=W,
        top= 150,
        left=135
    )
    
    tn1= ft.Container(
        width=350,
        height=200,
        bgcolor=DG,
        top=150,
        right=15,
        content= ft.Row(
            controls=[
                    ft.Image(
                        src= 'TeamPhoto1.png',
                        width=158,
                        height=158),
                    ft.Image(
                        src= 'TeamPhoto2.png',
                        width=158,
                        height=158,
        )],
        alignment= ft.MainAxisAlignment.SPACE_BETWEEN))
    
    ES= ft.Text(
        "Eeshal Saeed",
        weight= ft.FontWeight.NORMAL,
        size=15,
        color=W,
        top=310,
        left=55
    )
    MS= ft.Text(
            "Mahnoor Saeed",
            weight= ft.FontWeight.NORMAL,
            size=15,
            color=W,
            top=310,
            left=237
        )
    wdwd= ft.Text(
        "What Do We Do?",
        weight= ft.FontWeight.BOLD,
        size=30,
        color=W,
        top= 370,
        left=95
    )
    vl= ft.Text(
        "The wave crashed and hit the sandcastle head-on. " \
        "The sandcastle began to melt under the waves force "
        "and as the wave receded, half the sandcastle was gone. " \
        "The next wave hit, not quite as strong, but still managed to " \
        "cover the remains of the sandcastle and take more of it away. Tever existed.",
        size=13,
        weight=ft.FontWeight.NORMAL,
        color=W,
        width= 280,
        top=420,
        left=55,
        text_align=ft.TextAlign.CENTER
    )
    b= ft.Button(
        bgcolor= ft.Colors.with_opacity(0.4,B),
        top= 600,
        left= 95,
        width= 200,
        height= 50,
        on_click= m,
        elevation= 15,
        content=ft.Text(
            "Back",
            color= W,
            size= 30,
        )
    )
    circle12= ft.Container(
                width= 60,
                height=60,
                bgcolor=LG,
                border_radius=ft.BorderRadius.all(200),
                opacity=1,
                top=660,
                left=100)
    camera= flet_camera.Camera(
        width=350,
        height=500,
        

                                )
    tpicture= ft.IconButton(
            icon= ft.Icon(ft.Icons.PHOTO, color= W),
            bgcolor= ft.Colors.with_opacity(0.4,VDG),
            width=50,
            height=50,
            top=500,
            animate_scale =ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            left= 180,
            on_click=takepic
        )
    camera1= ft.Container(
                    width=350,
                    height=500,
                    top=70,
                    left=25,
                    shadow= ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                            offset=ft.Offset(0, 5),),
                    content= ft.Stack(
                        controls=[
                            camera,
                        ],

                    ),
                    border_radius=ft.BorderRadius.all(10),
            )
    cambutton= ft.Button(
        elevation=35,
        content= ft.Text("Take A Photo", color= W,size=20),
        width=200,
        height=50,
        top=590,
        left=95,
        bgcolor= ft.Colors.with_opacity(0.6, B), 
        on_click= opencam,
        

    )
    food= flet_video.Video(
                playlist=[flet_video.VideoMedia(resource="food.mp4")],
                autoplay=True,
                controls=None,
                muted=True,
                width=350,
                height=500,)
    foodisplay= ft.Container(
                width=350,
                height=500,
                top=70,
                left=25,
                content=food,
                bgcolor= "#437769",
                border_radius=ft.BorderRadius.all(10),
                shadow= ft.BoxShadow(
                                            spread_radius=1,
                                            blur_radius=15,
                                            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                                            offset=ft.Offset(0, 5),),
        )              
    done= ft.Text(
            "Done!",
            size=70,
            weight=ft.FontWeight.BOLD,
            color=W,
            top=170,
            left=40
        )
    all= ft.Text(
            "All",
            size=70,
            weight=ft.FontWeight.BOLD,
            color=W,
            top=100,
            left=45
    
        )
    photoholder= [None]
    preview= ft.Image(
        src= "",
        #scale=ft.Scale(scale_x=-1, scale_y=1) ,
        width=350,
        height=500,
        fit=ft.BoxFit.COVER
    )
    previewhold= ft.Container(
                    width=350,
                    height=500,
                    top=70,
                    left=25,
                    content=preview,
                    bgcolor= "#437769",
                    border_radius=ft.BorderRadius.all(10),
                    shadow= ft.BoxShadow(
                                                spread_radius=1,
                                                blur_radius=15,
                                                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                                                offset=ft.Offset(0, 5),),
            )        
    redo= ft.IconButton(
        icon= ft.Icons.REDO,
        icon_color= W,
        icon_size= 30,
        bgcolor= DG,
        width=50, 
        height=50,
        top= 600,
        left=40,
        on_click= AGAIN,


    )
    send= ft.IconButton(
            icon= ft.Icons.SEND,
            icon_color= W,
            icon_size= 30,
            bgcolor= DG,
            width=50, 
            height=50,
            top= 600,
            left=310,
    
    
        )
    orderofmp= ft.Stack(
        controls=[
        tpicture,
        camera1,
        foodisplay
        ]
        
    )
    
    
    
               


#PAGES
    page_12= ft.Container(          
                                    width=400,
                                    height=850,
                                    bgcolor=VDG,
                                    border_radius=ft.BorderRadius.all(35),
            
                
                                    content=ft.Stack(
                                            controls=[
                                            ft.Container(
                                            width=400,
                                    height=850,
                                    bgcolor=VDG,
                                    border_radius=ft.BorderRadius.all(35),
                                    ),
                                    previewhold,
                                    redo,
                                    send,
                                    menu1
                                    
                                    ]))
    page_11= ft.Container(          
                                    width=400,
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
                                    orderofmp,
                                    menu1,
                                    cambutton,
                                    
                                    ]))
    page_10= ft.Container(width=400,
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
                                    circle6,
                                    circle,
                                    circle8,
                                    circle12,
                                    learn1,
                                    tn1,
                                    team,
                                    ES,
                                    MS,
                                    wdwd,
                                    vl,
                                    b,
                                    circle_1o1,
                                   
                                    
                                    ]))
    
    page_0= ft.Container(
                        content= screen,
                        width=400,
                        height=850,
                        bgcolor=DG,
                        border_radius=ft.BorderRadius.all(35),
                                    )

    page_7= ft.Container(width=400,
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
                                    done,
                                    all,
                                    end,
                                    circle10,
                                    circle11,
                                    End,
                                     ]))
    page_6= ft.Container(width=400,
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
                                history,
                                nexta,
                                fami,
                                gen,
                                T1,
                                T2,
                                T3
                                        ]
                                )
    )
    
    page_9=ft.Container(width=400,
                                    height=850,
                                    bgcolor=DDG,
                                    border_radius=ft.BorderRadius.all(35),
            
                
                                    content=ft.Stack(
                                            controls=[
                                            ft.Container(
                                            width=400,
                                    height=850,
                                    bgcolor=DDG,
                                    border_radius=ft.BorderRadius.all(35),
                                    ),
                                    logo2,
                                    signlog,
                                    learn,
                                    ]))


                            
    page_5= ft.Container(width=400,
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
                            weight,
                            height,
                            nexta,
                            activity,
                            ac,
                            T1,
                            T2,
                            T3
                            ]))
                         
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
                        gender,
                        ancestry,
                        nexta,
                        T1,
                        T2,
                        T3
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
                                    ctp,
                                    circle_1o1,
                                    circle_2o1
                    
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
                  ctp,
                  circle_4o1,
                  circle_3o1
                  

                  
                  
                  
                

                ]
            
            )

    
    )
                  
            
    
    

    

    

#CODE


























    current_view = ft.Container(
           width=400, height=850, bgcolor=LG,
           border_radius=ft.BorderRadius.all(35),
           content=page_11,
           offset=ft.Offset(0,0)
    )



    outer_stack = ft.Stack(
        controls=[
            current_view
        ]
    )
    page.add(outer_stack)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
#python -c "import sys; from flet.cli import main; sys.argv = ['flet', 'run', 'Untitled-1.py', '--web']; main()"
#this is for a phone:
#python -c "import sys; from flet.cli import main; sys.argv = ['flet', 'run', 'Untitled-1.py', '--android']; main()"
#Remove-Item family_data.json        
#To do list :
# Fix page_10 because when I checked it on an actual phone a lot of the key widgets are not aligned/ not aesthetic
# Scratch that, all of the pages have widgets that are not aligned, only noticed this when testing the app on a phone
