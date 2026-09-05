from argparse import ONE_OR_MORE
import asyncio
from tkinter import Y
from annotated_types import T
import flet as ft
import copy
import json
import os
import flet_video
import flet_camera
import random
import datetime
import calendar
from ultralytics import YOLO
from PIL import Image as PILImage
import io


async def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.scroll = ft.ScrollMode.AUTO,
    page.window.full_screen= True

    LG = "#97CE8B"
    DG = "#5ca38f"
    W = "#FFFFFF"
    P= "#e53e34"
    B= "#000000"
    DDG= "#4c9d86"
    LLG="#8FC682"
    VDG= "#295549"
    WD= "#4CAF50"
    ON= "#FFC107"
    T= "#e53e34"
   
    empty_person = {
        "username": "",
        "profile": {
            "name": None,
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
            "dailycalorietarget": 0,

            "food_group_targets": {},
        },
        "calendar": {},
        "photos":[],
    }

    empty_account = {
        "username": "",
        "password": "",
        "members": {},
    }


    

    APP_FOLDER = os.path.dirname(os.path.abspath(__file__))
    DATA_FILE = os.path.join(APP_FOLDER, "family_data.json")
    PHOTOO_FILE= os.path.join(APP_FOLDER, "photos1")
    os.makedirs(PHOTOO_FILE, exist_ok= True)

    FOOD_MODEL = YOLO(os.path.join(APP_FOLDER, "best_updt.pt"))

    NUTRITION_PER_100G = {
        "Apple": {"calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14, "sugar": 10},
        "Banana": {"calories": 89, "protein": 1.1, "fat": 0.3, "carbs": 23, "sugar": 12},
        "Cabbage": {"calories": 25, "protein": 1.3, "fat": 0.1, "carbs": 6, "sugar": 3},
        "Carrot": {"calories": 41, "protein": 0.9, "fat": 0.2, "carbs": 10, "sugar": 5},
        "ChineseCabbage": {"calories": 13, "protein": 1.2, "fat": 0.2, "carbs": 2, "sugar": 1},
        "Cucumber": {"calories": 15, "protein": 0.7, "fat": 0.1, "carbs": 4, "sugar": 2},
        "GreenOnion": {"calories": 32, "protein": 1.8, "fat": 0.2, "carbs": 7, "sugar": 2},
        "GreenPepper": {"calories": 20, "protein": 0.9, "fat": 0.2, "carbs": 5, "sugar": 2},
        "Lettuce": {"calories": 15, "protein": 1.4, "fat": 0.2, "carbs": 3, "sugar": 1},
        "MiniTomato": {"calories": 18, "protein": 0.9, "fat": 0.2, "carbs": 4, "sugar": 3},
        "Onion": {"calories": 40, "protein": 1.1, "fat": 0.1, "carbs": 9, "sugar": 4},
        "PineApple": {"calories": 50, "protein": 0.5, "fat": 0.1, "carbs": 13, "sugar": 10},
        "Potato": {"calories": 77, "protein": 2.0, "fat": 0.1, "carbs": 17, "sugar": 1},
        "Radhish": {"calories": 16, "protein": 0.7, "fat": 0.1, "carbs": 3, "sugar": 2},
        "Spinach": {"calories": 23, "protein": 2.9, "fat": 0.4, "carbs": 4, "sugar": 0.4},
        "StrawBerry": {"calories": 32, "protein": 0.7, "fat": 0.3, "carbs": 8, "sugar": 5},
        "Tomato": {"calories": 18, "protein": 0.9, "fat": 0.2, "carbs": 4, "sugar": 3},
    }

    def analyze_food_photo(photo_bytes):
        img = PILImage.open(io.BytesIO(photo_bytes))
        results = FOOD_MODEL.predict(source=img, verbose=False)
        detected = sorted({FOOD_MODEL.names[int(box.cls)] for r in results for box in r.boxes})
        total = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0, "sugar": 0}
        for food in detected:
            info = NUTRITION_PER_100G.get(food)
            if info:
                for key in total:
                    total[key] += info[key]
        return {"detected_foods": detected, "totals": total}
    page.window.full_screen = True


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
        page_11.content.controls.remove(cambutton)
        page_11.update()
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
                            page_11.content.controls.append(cambutton)
                            page_11.update()
        if nutrition.bgcolor== VDG or photo.bgcolor== VDG or addmembers.bgcolor== VDG or health.bgcolor==VDG:
            nutrition.bgcolor= "transparent" 
            nutrition.update()
            photo.bgcolor= "transparent"
            photo.update()
            addmembers.bgcolor= "transparent"
            addmembers.update()
            health.bgcolor= 'transparent'
            health.update()
            cam.bgcolor= VDG
            cam.update()
    def photoname():
        name= datetime.datetime.now()
        namestr= name.strftime("%S_%M_%d_%m_%Y")
        return namestr
            

    def savingphoto(e):
        
        saving= family[current_user[0]]["members"][current_member[0]]['photos']
        
        pn = photoname()  
        tired = os.path.join(PHOTOO_FILE, pn + ".jpg")
        
        if isinstance(photoholder[0], str) and os.path.exists(photoholder[0]):
            with open(photoholder[0], "rb") as src, open(tired, "wb") as dst:
                dst.write(src.read())
        elif isinstance(photoholder[0], bytes):
            with open(tired, "wb") as process:
                process.write(photoholder[0])
        else:
            print(f"Unexpected type: {type(photoholder[0])}")
            return
            
        saving.append(pn + ".jpg")
        orderofmp.controls.reverse()
        orderofmp.update()
        page_11.content.controls.append(cambutton)
        page_11.update() 
        current_view.content= page_13
        current_view.update()
        save_family()

    
    async def analyzephoto(e):
        current_view.content = page_loading2
        current_view.update()
        await asyncio.sleep(0.1)
        analysis = analyze_food_photo(photoholder[0])
        analysisholder[0] = analysis
        resultimage.src = photoholder[0]
        foods_text = ", ".join(analysis["detected_foods"]) if analysis["detected_foods"] else "No food detected"
        resultfoodtext.value = foods_text
        resultcaltext.value = f"Calories: {analysis['totals']['calories']} kcal"
        resultprotext.value = f"Protein: {analysis['totals']['protein']}g"
        resultfattext.value = f"Fat: {analysis['totals']['fat']}g"
        resultcarbtext.value = f"Carbs: {analysis['totals']['carbs']}g"
        resultsugartext.value = f"Sugar: {analysis['totals']['sugar']}g"
        current_view.content = page_16
        current_view.update()

    def saveresult(e):
        saving = family[current_user[0]]["members"][current_member[0]]['photos']
        pn = photoname()
        tired = os.path.join(PHOTOO_FILE, pn + ".jpg")
        if isinstance(photoholder[0], str) and os.path.exists(photoholder[0]):
            with open(photoholder[0], "rb") as src, open(tired, "wb") as dst:
                dst.write(src.read())
        elif isinstance(photoholder[0], bytes):
            with open(tired, "wb") as process:
                process.write(photoholder[0])
        saving.append(pn + ".jpg")

        analysis = analysisholder[0]
        if analysis:
            calorie['consumed'] += analysis['totals']['calories']
            protein['consumed3'] += analysis['totals']['protein']
            fat['consumed2'] += analysis['totals']['fat']
            sugar['consumed4'] += analysis['totals']['sugar']
            carbs['consumed5'] += analysis['totals']['carbs']

        orderofmp.controls.reverse()
        orderofmp.update()
        page_11.content.controls.append(cambutton)
        page_11.update()
        current_view.content = page_13
        current_view.update()
        save_family()
        asyncio.create_task(updatemanui())

    def buildgallery(photolist):
        thumbnails = []
        for filename in photolist:
            gallery1= os.path.join(PHOTOO_FILE,filename)
            with open(gallery1,"rb") as tsrc:
                imagebytes= tsrc.read()
            thumbnails.append(ft.Image(imagebytes, 
                                    width=20,
                                    height=100,
                                    fit=ft.BoxFit.COVER,
                                    border_radius= 35, ))
        
        return thumbnails
    thumbnails2= []
    def FINALGALLERY(e):
                saving= family[current_user[0]]['members'][current_member[0]]['photos']
                thumbnails2= buildgallery(saving)
                GALLERY.controls= thumbnails2
                GALLERY.update()
                print(saving)

    def savingday(e):
        today_str = datetime.date.today().strftime("%d_%m_%Y")
        info_data = family[current_user[0]]['members'][current_member[0]]
        info_data['calendar'][today_str] = {
            "calories": calorie['consumed'], "target": calorie['target'],
            "protein": protein['consumed3'], "fat": fat['consumed2'],
            "sugar": sugar['consumed4'], "carbs": carbs['consumed5'],
        }
        calorie['consumed'] = 0
        protein['consumed3'] = 0
        fat['consumed2'] = 0
        sugar['consumed4'] = 0
        carbs['consumed5'] = 0
        save_family()
        asyncio.create_task(updatemanui())

    def buildcalendarlist():
        entries = []
        info_data = family[current_user[0]]['members'][current_member[0]]
        for date_str, stats in sorted(info_data['calendar'].items(), reverse=True):
            entries.append(ft.Container(
                width=360, height=80, bgcolor=VDG, padding=10, border_radius=15,
                content=ft.Column(controls=[
                    ft.Text(date_str, size=16, weight=ft.FontWeight.BOLD, color=W),
                    ft.Text(f"Calories: {stats.get('calories',0)}  Protein: {stats.get('protein',0)}g  Fat: {stats.get('fat',0)}g", size=12, color=W),
                ])
            ))
        return entries

    def CALENDARTIME(e):
        bigcalendar.controls = [build_full_calendar()]
        nutrition.bgcolor= "transparent"
        nutrition.update()
        photo.bgcolor= "transparent"
        photo.update()
        addmembers.bgcolor= "transparent"
        addmembers.update()
        health.bgcolor= "transparent"
        health.update()
        cam.bgcolor= "transparent"
        cam.update()
        calender.bgcolor= VDG
        calender.update()
        calendarlist.controls = buildcalendarlist()
        current_view.content = page_18
        current_view.update()

    def  aisugg(profiledata):
        return {
            "dailycalorietarget":(random.randint(1500, 2500)),
            "foodgrouptargets": {
                "proteing": random.randint(40, 130),
                "fatsg": random.randint(40, 90),
                "sugarsg": random.randint(20, 50),
                "carbsg": random.randint(40, 500),
        }
    }
    def PHOTOTIME(e):
            current_view.content= page_11
            current_view.update()
            nutrition.bgcolor= "transparent"
            nutrition.update()
            photo.bgcolor= "transparent"
            photo.update()
            addmembers.bgcolor= "transparent"
            addmembers.update()
            calender.bgcolor= "transparent"
            calender.update()
            health.bgcolor= 'transparent'
            health.update()
            cam.bgcolor= VDG
            cam.update()
    def NUTRITIONNTIME(e):
                    current_view.content= page_13
                    current_view.update()
                    nutrition.bgcolor= VDG
                    nutrition.update()
                    photo.bgcolor= "transparent"
                    photo.update()
                    addmembers.bgcolor= "transparent"
                    addmembers.update()
                    health.bgcolor= 'transparent'
                    health.update()
                    calender.bgcolor= "transparent"
                    calender.update()
                    cam.bgcolor= "transparent"
                    cam.update()
    def GALLERYTIME(e):
                            current_view.content= page_14
                            current_view.update()
                            nutrition.bgcolor= "transparent"
                            nutrition.update()
                            photo.bgcolor= VDG
                            photo.update()
                            calender.bgcolor= "transparent"
                            calender.update()
                            addmembers.bgcolor= "transparent"
                            addmembers.update()
                            health.bgcolor= 'transparent'
                            health.update()
                            cam.bgcolor= "transparent"
                            cam.update()
                            FINALGALLERY(None)
    def FAMILYTIME(e):
        current_view.content= page_15
        current_view.update()
        familycards.controls = []
        familycards.update()
        familycards.controls = buildfamilycards()
        familycards.update()
        nutrition.bgcolor= "transparent"
        nutrition.update()
        photo.bgcolor= "transparent"
        photo.update()
        calender.bgcolor= "transparent"
        calender.update()
        addmembers.bgcolor= VDG
        addmembers.update()
        health.bgcolor= 'transparent'
        health.update()
        cam.bgcolor= "transparent"
        cam.update()
    def toggle_menu(e):
        
        menu_backdrop.visible = True
        menu_backdrop.update()
        menu_backdrop.opacity = 1
        menu_backdrop.update()
        menu_panel.offset = ft.Offset(0, 0)
        menu_panel.update()
        
        menu_panel.update()

    def closemenu(e):
       
        menu_panel.offset = ft.Offset(-1.5, 0)
        menu_panel.update()
        
       
        menu_backdrop.opacity = 0
        menu_backdrop.update()
        async def hide_bg():
            await asyncio.sleep(0.3)
            menu_backdrop.visible = False
            menu_backdrop.update()
        asyncio.create_task(hide_bg())
    def navigate_from_menu(target_page):
        if target_page== page_13:
            NUTRITIONNTIME(None)
        closemenu(None)
        current_view.content = target_page
        current_view.update()

    addingmember= [False]
    def createnewmember(e): 
            nm = copy.deepcopy(empty_person)
            nm["profile"]["name"] = namenew_field.value
            family[current_user[0]]['members'][namenew_field.value] = nm
            save_family()
            current_member[0]= namenew_field.value
            addingmember[0]= True
            T1.bgcolor= W
            T1.border= ft.Border.all(2, W)
            T1.content= ft.Text("1", color=DG)
            T1.update()
            T2.bgcolor= "Transparent"
            T2.content= ft.Text("2", color=W)
            T2.update()
            T3.bgcolor= "Transparent"
            T3.content= ft.Text('3',color=W)
            T3.update()
            current_view.content= page_4
            current_view.update()
    def buildfamilycards():
        cards = []
        for name, data in family[current_user[0]]['members'].items():
            card_name_text = ft.Text(data['profile'].get('name') or name, size=20, weight=ft.FontWeight.BOLD, color=W)
            card_age_text = ft.Text(f"Age: {data['profile'].get('age') or '--'}", size=13, color=W)
            card_height_text = ft.Text(f"Height: {data['profile'].get('height') or '--'}", size=13, color=W)
            card_activity_text = ft.Text(f"Activity: {data['profile'].get('activity_level') or '--'}", size=13, color=W)

            def switch_member(e, member_name=name):
                current_member[0] = member_name
                asyncio.create_task(updatemanui())
                NUTRITIONNTIME(None)

            card = ft.Container(
                width=360,
                height=130,
                bgcolor=VDG,
                padding=15,
                border_radius=20,
                ink=True,
                on_click=switch_member,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                    offset=ft.Offset(0, 4),
                ),
                content=ft.Column(
                    spacing=4,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[card_name_text, ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color=LG, size=30)],
                        ),
                        ft.Divider(color=ft.Colors.with_opacity(0.2, W), height=10),
                        ft.Row(spacing=20, controls=[card_age_text, card_height_text, card_activity_text]),
                    ],
                ),
            )
            cards.append(card)
        return cards
    def login(e):
            entered_user = info.value
            entered_pass = info2.value
            if entered_user in family and family[entered_user]['password'] == entered_pass:
                current_user[0] = entered_user
                current_member[0] = entered_user
                asyncio.create_task(updatemanui())
                current_view.content = page_13
                current_view.update()
            else:
                page_1.content.controls.append(loginwarn)
                page_1.update()         
    def get_day_color(pct):
        if pct is None:
            return VDG
        if 85 <= pct <= 115:
            return WD
        elif 60 <= pct < 85 or 115 < pct <= 140:
            return ON
        else:
            return T

    def build_month_grid(year, month):
        info_data = family[current_user[0]]['members'][current_member[0]]
        weeks = calendar.Calendar(firstweekday=6).monthdayscalendar(year, month)
        month_name = calendar.month_name[month]
        week_rows = []
        for week in weeks:
            day_cells = []
            for day in week:
                if day == 0:
                    day_cells.append(ft.Container(width=40, height=40))
                    continue
                date_str = f"{day:02d}_{month:02d}_{year}"
                entry = info_data['calendar'].get(date_str)
                if entry and entry.get("target"):
                    pct = (entry["calories"] / entry["target"]) * 100
                else:
                    pct = None
                day_cells.append(
                    ft.Container(
                        width=40, height=40, bgcolor=get_day_color(pct),
                        border_radius=8, alignment=ft.Alignment(0, 0),
                        content=ft.Text(str(day), size=12, color=W),
                )
            )
            week_rows.append(ft.Row(controls=day_cells, spacing=4, alignment=ft.MainAxisAlignment.CENTER))
        return ft.Column(
            controls=[ft.Text(f"{month_name} {year}", size=18, weight=ft.FontWeight.BOLD, color=W), *week_rows],
            spacing=6,
    )

    def build_full_calendar():
        year = datetime.date.today().year
        return ft.Column(controls=[build_month_grid(year, m) for m in range(1, 13)], spacing=25) 







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

#(note to self)this code must be here
    
    def newacc(e):
        if len(info22.value)<6:
            page_2.content.controls.append(warn1)
            page_2.update()

        else:
            new_account = copy.deepcopy(empty_account)
            new_account['username'] = info.value
            new_account['password'] = info22.value

            first_member = copy.deepcopy(empty_person)
            first_member['username'] = info.value
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
                on_click= login,
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

    menu1= ft.IconButton(
        width=50,
        height=50,
        icon= ft.Icons.MENU,
        icon_size= 35,
        icon_color= W,
        top=23,
        right=10,
        on_click= toggle_menu
        
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
        padding=ft.Padding.symmetric(horizontal=10),
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
        padding=ft.Padding.symmetric(horizontal=10),
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
    name_field= ft.TextField(
               hint_text="Enter your name",
               hint_style=ft.TextStyle(color=ft.Colors.WHITE_70),
               bgcolor="transparent",
               color=W,
               border_color="transparent",
               top=14,  
               left=0,
               width=280,
               height=45,
           )
    
    name1= ft.Container(
         width=330,
                height=60, 
                bgcolor= ft.Colors.with_opacity(0.4,B),
                top=  630,
                left=35,
                padding=ft.Padding.symmetric(horizontal=10),
                shadow=ft.BoxShadow(
                       spread_radius=1,
                       blur_radius=15,
                       color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                       offset=ft.Offset(0, 5),),
                border_radius=ft.BorderRadius.all(5),
                content= ft.Stack(
                controls=[
                        ft.Text(
                        "7. What is your name?",
                        color=W,
                        weight=ft.FontWeight.NORMAL,
                        size=15,
                        top=5,
                        left=15,
                        opacity=1,
                    ),
                    name_field,
                ]
             ),
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
            padding=ft.Padding.symmetric(horizontal=10),
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
            padding=ft.Padding.symmetric(horizontal=10),
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
                padding=ft.Padding.symmetric(horizontal=10),
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
                ft.Radio(value="Sedentary", label="Sedentary"),
                ft.Radio(value="Light", label="Lightly Active"),
                ft.Radio(value="Moderate", label="Moderately Active"),
                ft.Radio(value="Very Active", label="Very Active"),
                ft.Radio(value="Extra Active", label="Extremely Active")
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
            padding=ft.Padding.symmetric(horizontal=10),
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
                    "8. Do you have a family history of any of the following conditions?",
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
                        "9. Which of your family members have this condition? (Check all that apply)",
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
    
    async def save_results(e):
        current_view.content= page_loading
        current_view.update()

        await asyncio.sleep(1.3)

        information=family[current_user[0]]['members'][current_member[0]]

        information['profile']['name']= name_field.value
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


        
        generated_targets= aisugg(information['profile'])
        information['ai_recommendations']['dailycalorietarget'] = generated_targets["dailycalorietarget"]
        information['ai_recommendations']['foodgrouptargets'] = generated_targets["foodgrouptargets"]
        save_family()

        profile_name_text.value = name_field.value or "User Name"
        profile_age_text.value = f"Age: {age_field.value or '--'}"
        profile_height_text.value = f"Height: {height_field.value or '--'}"
        profile_activity_text.value = f"Activity: {activity_radio.value or '--'}"

 



        asyncio.create_task(updatemanui())
        if addingmember[0]== False:
            current_view.content= page_13
            current_view.update()
        elif addingmember[0]== True:
            FAMILYTIME(None)
            addingmember[0]= False 

                    
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
        "Learn About Vale!",
        weight= ft.FontWeight.BOLD,
        size=44,
        color=W,
        top=60,
        left=40
       
    )
    team= ft.Text(
        "The Team!",
        weight= ft.FontWeight.BOLD,
        size=30,
        color=W,
        top= 150,
        left=130
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
        left=65
    )
    MS= ft.Text(
            "Mahnoor Saeed",
            weight= ft.FontWeight.NORMAL,
            size=15,
            color=W,
            top=310,
            left=245
        )
    wdwd= ft.Text(
        "What Do We Do?",
        weight= ft.FontWeight.BOLD,
        size=30,
        color=W,
        top= 370,
        left=95,
    )
    vl= ft.Text(
        "The wave crashed and hit the sandcastle head-on. " \
        "The sandcastle began to melt under the waves force " \
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
            icon= ft.Icon(ft.Icons.CAMERA_ALT, color=W),
            bgcolor= ft.Colors.with_opacity(0.4,VDG),
            width=50,
            height=50,
            top=640,
            animate_scale =ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            left= 180,
            on_click=takepic
        )
    camera1= ft.Container(
                    width=350,
                    height=500,
                    top=200,
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
        top=740,
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
                top=200,
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
    analysisholder = [None]
    resultimage = ft.Image(src="", width=300, height=300, fit=ft.BoxFit.COVER)
    resultfoodtext = ft.Text("", size=20, weight=ft.FontWeight.BOLD, color=W)
    resultcaltext = ft.Text("", size=16, color=W)
    resultprotext = ft.Text("", size=14, color=W)
    resultfattext = ft.Text("", size=14, color=W)
    resultcarbtext = ft.Text("", size=14, color=W)
    resultsugartext = ft.Text("", size=14, color=W)
    preview= ft.Image(
        src= "",
        scale=ft.Scale(scale_x=-1, scale_y=1) ,
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
            on_click=analyzephoto
    
    
        )
    orderofmp= ft.Stack(
        controls=[
        tpicture, 
        camera1,
        foodisplay
        ]
        
    )
    square2= ft.Container(
        width=330,
        height=210,
        left=32,
        top=360,
        bgcolor= "#99295549",
        border_radius= 10,
        shadow= ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                    offset=ft.Offset(0, 5),)

    )
    loading_text = ft.Text("Processing your health profile...", color=W, size=16)
    loading_text2 = ft.Text("Processing your image...", color=W, size=16)
    loading_ring = ft.ProgressRing(width=40, height=40, stroke_width=4, color=W)
    menu_backdrop = ft.Container(
        width=400,
        height=850,
        bgcolor=ft.Colors.with_opacity(0.5, B),
        opacity=0,
        visible=False,
        animate_opacity=300,
        on_click= closemenu,
        border_radius= 35,
    )


    profile_name_text = ft.Text("User Name", size=20, weight=ft.FontWeight.BOLD, color=W)
    profile_age_text = ft.Text("Age: --", size=13, color=W)
    profile_height_text = ft.Text("Height: --", size=13, color=W)
    profile_activity_text = ft.Text("Activity: --", size=13, color=W)
    profilewidget = ft.Container(
        width=360,
        height=130,
        bgcolor=VDG,  
        top=180,
        left=20,
        padding=15,
        border_radius=20,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        ),

        content=ft.Column(
            spacing=4,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        profile_name_text,
                        ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color=LG, size=30)
                    ]
                ),
                ft.Divider(color=ft.Colors.with_opacity(0.2, W), height=10),
                ft.Row(
                    spacing=20,
                    controls=[
                        profile_age_text,
                        profile_height_text,
                        profile_activity_text,
                    ]
                )
            ]
        )
    )
    namenew_field=ft.TextField(
                        hint_text="Enter member name",
                        hint_style=ft.TextStyle(color=ft.Colors.WHITE_70),
                        bgcolor="transparent",
                        color=W,
                        border_color="transparent",
                        width=190,
                        height=45,
                                   )
                    
    addwidget = ft.Container(
        width=360,
        height=80,
        bgcolor=ft.Colors.with_opacity(0.3, VDG),
        border=ft.Border.all(2, LG),
        border_radius=15,
        padding= 8,
        alignment=ft.Alignment(0, 0),
        ink=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=4,
                    controls=[
                    ft.Text(
                      "Add Family Member",
                       size=16,
                       weight=ft.FontWeight.BOLD,
                       color=W
                )],
                

                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=1,
                    controls= [
                        namenew_field,
                        ft.IconButton(
                            icon= ft.Icons.PERSON_ADD_ALT_1,
                            icon_color= W,
                            on_click= createnewmember,
                               ),
                    ],
                ),
            ],
        )
    )
            
    menu_panel = ft.Container(
        width=250,
        height=850,
        bgcolor=VDG,
        padding=20,
        border_radius=35,
        offset=ft.Offset(-1.5, 0),
        animate_offset=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Text("Vale Menu", size=22, weight=ft.FontWeight.BOLD, color=W, style=ft.TextStyle(font_family="Roboto")),
                ft.Divider(color=W),
                ft.TextButton("Home / Nutrition", on_click=lambda e: navigate_from_menu(page_13),style=ft.ButtonStyle(color= W)),
                ft.TextButton("Take Photo", on_click=lambda e: navigate_from_menu(page_11), style=ft.ButtonStyle(color= W)),
                ft.TextButton("Photo Gallery", on_click=lambda e: navigate_from_menu(page_14), style=ft.ButtonStyle(color= W)),
                ft.TextButton("Log Out", on_click=lambda e: navigate_from_menu(page_1), style=ft.ButtonStyle(color= W)),
            ]
        )
    )
    
#MAIN PAGEINTERFACE
    #CALORIES:
    cl= ft.Text("""Calories: \n  0/--kcal""", size=34,color= W, weight= ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    caloriering= ft.ProgressRing(
        value= 0.0,
        width=93,
        height= 93,
        stroke_width= 10,
        color=W,
        bgcolor= LG,
    ) 
    bgring1= ft.Container(
        width=93,
        border_radius= 200,
        height= 93,
        bgcolor= LG,
    ) 
    calnum = ft.Text("0.0%", size=18, weight=ft.FontWeight.BOLD, color=W)
    callabel = ft.Text("kcal eaten", size=12, color=W)
    ringdisplay = ft.Container(
        border=ft.Border.all(width=6, color=W),
        border_radius=200,
        width=100,
        height=100,
        alignment= ft.Alignment(0,0),
        content= ft.Stack(
            controls=[
                        bgring1,
                        caloriering,
                        ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                            controls=[ calnum, callabel]
                        ),
                        
                    ],
                    alignment= ft.Alignment(0,0)
        )

        
    )

    #PROTEIN:
    proteinring= ft.ProgressRing(
            value= 0.0,
            width=93,
            height= 93,
            stroke_width= 10,
            color=W,
            bgcolor=DG,
        ) 
    bgring2= ft.Container(
            width=93,
            border_radius= 200,
            height= 93,
            bgcolor= DG,
        ) 
    
    pl= ft.Text("""Protein: \n 0/--g""", size=34,color= W, weight= ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER)
    pronum= ft.Text("0.0%", size=18,color=W, weight= ft.FontWeight.BOLD)
    protein= {
            "target3":0,
            "consumed3":0,
        }        
    ringdisplay2 = ft.Container(

            border=ft.Border.all(width=6, color=W),
            border_radius=200,
            width=100,
            height=100,
            alignment= ft.Alignment(0,0),
            content= ft.Stack(
                controls=[
                            bgring2,
                            proteinring,
                            pronum,
                            
                            
                        ],
                        alignment= ft.Alignment(0,0)
            )
    
            
        )



    
    #FATS:
    fatring= ft.ProgressRing(
                value= 0.0,
                width=93,
                height= 93,
                stroke_width= 10,
                color=LG,
                bgcolor= LG,
            ) 
    bgring3= ft.Container(
                width=93,
                border_radius= 200,
                height= 93,
                bgcolor= LG,
            ) 
    fat= {
            "target2":0,
            "consumed2":0,
        }
    fatnum= ft.Text("0.0%", size=18,color=W, weight= ft.FontWeight.BOLD)
        
    fl= ft.Text("Fats: \n 0/--g", size=34,color=W, weight= ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    ringdisplay3 = ft.Container( border=ft.Border.all(width=6, color=W),
                border_radius=200,
                width=100,
                height=100,
                alignment= ft.Alignment(0,0),
                content= ft.Stack(
                    controls=[
                                bgring3,
                                fatring,
                                fatnum,
                                
                                
                            ],
                            alignment= ft.Alignment(0,0)
                )
        
                
            )

    
    #SUGAR:
    sugring= ft.ProgressRing(
                    value= 0.0,
                    width=93,
                    height= 93,
                    stroke_width= 10,
                    color=W,
                    bgcolor=DG,
                ) 
    bgring4= ft.Container(
                    width=93,
                    border_radius= 200,
                    height= 93,
                    bgcolor= DG,
                ) 
    sl= ft.Text("Sugar: \n 0/--g", size=34,color= W, weight= ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER)
    sugnum= ft.Text("0.0%", size=18,color= W, weight= ft.FontWeight.BOLD)
    ringdisplay4 = ft.Container( border=ft.Border.all(width=6, color=W),
                    border_radius=200,
                    width=100,
                    height=100,
                    alignment= ft.Alignment(0,0),
                    content= ft.Stack(
                        controls=[
                                    bgring4,
                                    sugring,
                                    sugnum,
                                    
                                    
                                ],
                                alignment= ft.Alignment(0,0)
                    )
            
                    
                )
    
    sugar= {
            "target4":0,
            "consumed4":0,
        }




    #CARBOHYDRATES
    carring= ft.ProgressRing(
                        value= 0.0,
                        width=93,
                        height= 93,
                        stroke_width= 10,
                        color=W,
                        bgcolor= LG,
                    ) 
    bgring5= ft.Container(
                        width=93,
                        border_radius= 200,
                        height= 93,
                        bgcolor= LG,
                    ) 
    c= ft.Text("""Carbs: \n 0/--g""", size=34,color= W, weight= ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER)
    carnum= ft.Text("0.0%", size=18,color= W, weight= ft.FontWeight.BOLD)
    ringdisplay5 = ft.Container( border=ft.Border.all(width=6, color=W),
                                
                        border_radius=200,
                        width=100,
                        height=100,
                        alignment= ft.Alignment(0,0),
                        content= ft.Stack(
                            controls=[
                                        bgring5,
                                        carring,
                                        carnum,
                                        
                                        
                                    ],
                                    alignment= ft.Alignment(0,0)
                        )
                
                        
                    )
    carbs= {
            "target5":0,
            "consumed5":0,
        }
    #OTHER ELEMENTS
    decor = ft.Container(
        width=450,
        height=450,
        border_radius=200, 
        right= -20,
        top=200,
        gradient=ft.RadialGradient(
            center=ft.Alignment(0, 0),
            radius=0.5,
            colors=[
                LG,
                DG, 
            ],
        )
    )
    maintext= ft.Text(
        "Vale - Stay Healthy",
        color= W,
        size=25,
        top=30,
        left=20,
        weight= ft.FontWeight.BOLD,
    )
    tinylogo = ft.Container(
        width=40,
        height=40,
        top=29,
        left=300,
        content=ft.Image(
            src="Vale Logo (5).png",
            width=50,
            height=50,
            fit="contain"
        ),
        on_click=lambda e: print("Logo clicked"),
        ink=True 
    )

    nutrition= ft.IconButton(
            bgcolor= VDG,
            icon_size=40,
            icon_color= W,
            icon= ft.Icons.RESTAURANT,
            on_click= NUTRITIONNTIME,
    
        )
    addmembers= ft.IconButton(
                bgcolor= "transparent",
                icon_size=40,
                icon_color= W,
                icon= ft.Icons.FAMILY_RESTROOM,
                on_click= FAMILYTIME
        
            )
    health= ft.IconButton(
                    bgcolor= "transparent",
                    icon_size=40,
                    icon_color= W,
                    icon= ft.Icons.MONITOR_HEART,
            
                )
    cam= ft.IconButton(                        
                        bgcolor= "transparent",
                        icon_size=40,
                        icon_color= W,
                        icon= ft.Icons.CAMERA_ALT,
                        on_click= PHOTOTIME,
                
                    )
    photo= ft.IconButton(
                            bgcolor= "transparent",
                            icon_size=40,
                            icon_color= W,
                            icon= ft.Icons.PHOTO,
                            on_click= GALLERYTIME
                    
                        )
    calender= ft.IconButton(
            icon= ft.Icons.CALENDAR_MONTH, 
            icon_size=40,
            icon_color= W,
            bgcolor= "transparent",
            on_click= CALENDARTIME
        )
    travel= ft.Container(
        height= 60,
        width=360,
        top=100,
        left=20,
        bgcolor= "transparent",
        border_radius= 10,
        border=ft.Border.all(width=2, color=W),
        content= 
            ft.Row(
            controls=[
            
            nutrition,
            addmembers,
            health,
            cam,
            photo,
            calender
            ],
            spacing=20,
            alignment = ft.Alignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),

        
    )
    nutritiontitle= ft.Text(
        "Nutrition",
        size=18,
        color= W,
        top=180,
        left=20

    )
    nutritioninfo= ft.Text(
        " This part of Vale shows how much of each food group you \n should be consuming daily based on your age requirements, \n activity levels and family history. This information has been \n tailored for you based on recent research.",
        size= 12,
        color=W,
        top=210,
        left=18
    )
    display= ft.Container(
        width= 360,
        height=120,
        bgcolor= "#99295549",
        top=300,
        left=20,
        padding=ft.Padding.only(left=20, right=70),
        border_radius= 20,
        content=
            ft.Row(
                controls=[
                    ringdisplay,
                    cl,
                    
                ],
                spacing= 40,
                alignment = ft.Alignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )

    )
    display2= ft.Container(
            width= 360,
            height=120,
            bgcolor= "#99295549",
            top=440,
            left=20,
            padding=ft.Padding.only(left=70, right=20),
            border_radius= 20,
            content=
                ft.Row(
                    controls=[
                        pl,
                        ringdisplay2,
                        
                    ],
                    spacing=50,
                    alignment = ft.Alignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
    
        )
    display3= ft.Container(
                width= 360,
                height=120,
                bgcolor= "#99295549",
                top=580,
                left=20,
                padding=ft.Padding.only(left=20, right=70),
                border_radius= 20,
                content=
                    ft.Row(
                        controls=[
                            ringdisplay3,
                            fl,
                            
                        ],
                        spacing=70,
                        alignment = ft.Alignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
        
            )
    display4= ft.Container(
                    width= 360,
                    height=120,
                    bgcolor= "#99295549",
                    top=720,
                    left=20,
                    padding=ft.Padding.only(left=70, right=20),
                    border_radius= 20,
                    content=
                        ft.Row(
                            controls=[
                                sl,
                                ringdisplay4,
                                
                            ],
                            spacing=70,
                            alignment = ft.Alignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        )
        
                )
    display5= ft.Container(
                        width= 360,
                        height=120,
                        bgcolor= "#99295549",
                        top=860,
                        left=20,
                        padding=ft.Padding.only(left=20, right=70),
                        border_radius= 20,
                        content=
                            ft.Row(
                                controls=[
                                    ringdisplay5,
                                    c,
                                    
                                ],
                                spacing=70,
                                alignment = ft.Alignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER
                            )
        
                    )
    GALLERY= ft.GridView(
         runs_count= 2,
         controls= thumbnails2,
         expand=True,
         top= 200,
         left=20,
         width=350,
         height=700,
    )
    familycards= ft.Column(
                                            controls=[],
                                            spacing=15)
    calendarlist = ft.Column(controls=[], spacing=15)
    savedaybutton = ft.Button(bgcolor=ft.Colors.with_opacity(0.4, B),
                              content=ft.Text("Save Day", color=W, size=20), 
                              width=200, 
                              height=50, 
                              elevation=15, 
                              on_click=savingday, 
                              left=100, 
                              top=1000)
    resultbutton = ft.Button(
        bgcolor=ft.Colors.with_opacity(0.4, B),
        content=ft.Text("Save Result", color=W, size=20),
        width=200, height=50, elevation=15,
        top=700, left=95,
        on_click=saveresult,
    )
    loginwarn = ft.Text(
           "Incorrect email or password.",
           color=P,
           size=12,
           top=640,
           left=125
       )
    calorie= {
        "target":0,
        "consumed":0,
    }
    async def updatemanui():
        if current_user[0] and current_member[0]:
            udata = family[current_user[0]]['members'][current_member[0]]
            
            airecs = udata.get("ai_recommendations", {})
            groups = airecs.get('foodgrouptargets', {})
            
            target = airecs.get("dailycalorietarget")
            target3 = groups.get("proteing", 0)
            target4 = groups.get("sugarg", 0)
            target2 = groups.get("fatsg", 0)
            target5 = groups.get("carbsg", 0)
            
            if not target:
                target = 2000

            calorie['target'] = target  
            fat["target2"] = target2
            protein["target3"] = target3
            sugar["target4"] = target4
            carbs["target5"] = target5
            
            pl.value = f"Protein:\n{protein['consumed3']}/{target3}g"
            fl.value = f"Fats:\n{fat['consumed2']}/{target2}g"
            sl.value = f"Sugars:\n{sugar['consumed4']}/{target4}g"
            c.value = f"Carbs:\n{carbs['consumed5']}/{target5}g"
            cl.value = f"Calories:\n{calorie['consumed']}/{target}kcal"

            try:
                pl.update()
                fl.update()
                sl.update()
                c.update()
                cl.update()
            except Exception:
                pass

        target = calorie["target"]
        consumed = calorie["consumed"]
        target2 = fat["target2"]
        consumed2 = fat['consumed2']
        target3 = protein['target3']
        consumed3 = protein['consumed3']
        target4 = sugar['target4']
        consumed4 = sugar['consumed4']
        target5 = carbs['target5']
        consumed5 = carbs['consumed5']

        finalprogress = min(1.0, consumed / target) if target > 0 else 0.0
        calpercentage = ((consumed / target) * 100) if target > 0 else 0.0
        fatpercentage = ((consumed2 / target2) * 100) if target2 and target2 > 0 else 0.0
        propercentage = ((consumed3 / target3) * 100) if target3 and target3 > 0 else 0.0
        sugpercentage = ((consumed4 / target4) * 100) if target4 and target4 > 0 else 0.0

        await asyncio.sleep(0.1)
        
        caloriering.value = finalprogress
        calnum.value = f"{calpercentage:.1f}%"
        fatnum.value = f'{fatpercentage:.1f}%'
        pronum.value = f'{propercentage:.1f}%'
        sugnum.value = f'{sugpercentage:.1f}%'
                
        try:
            caloriering.update()
            calnum.update()
            fatnum.update()
            pronum.update()
            sugnum.update()
        except Exception:
            pass
    bigcalendar = ft.Column(controls=[], spacing=25)

#PAGES
    page_loading2 = ft.Container(
                width=400,
                height=850,
                bgcolor=VDG,
                border_radius=ft.BorderRadius.all(35),
                alignment=ft.Alignment(0, 0),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        loading_ring,
                        loading_text2,
                    ]
                )
            )
    page_loading = ft.Container(
            width=400,
            height=850,
            bgcolor=VDG,
            border_radius=ft.BorderRadius.all(35),
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    loading_ring,
                    loading_text
                ]
            )
        )
    page_15 = ft.Container(          
        width=400,
        height=850,
        bgcolor=DG,
        padding=ft.Padding(0),
        border_radius=ft.BorderRadius.all(35),
        content=ft.ListView(
            expand=True,
            controls=[
                ft.Container(
                    width=400,
                    height=1200, 
                    bgcolor=DG,
                    border_radius=ft.BorderRadius.all(35),
                    content=ft.Stack(
                        controls=[
                            decor,
                            maintext,
                            tinylogo,
                            menu1,
                            travel,
                            ft.Container(
                                top=180,
                                left=20,
                                width=360,
                                content=ft.Column(
                                    spacing=20,
                                    controls=[
                                        familycards,  
                                        addwidget        
                                    ]
                                )
                            )
                        ],
                    ),
                )
            ]
        )
    )
    page_18 = ft.Container(          
                width=400,
                height=850,
                bgcolor=DG,
                padding= ft.Padding(0),
                border_radius=ft.BorderRadius.all(35),
                content=ft.ListView(
                    expand=True,
                    controls=[
                        ft.Container(width=400,height=3600,bgcolor=DG, border_radius=ft.BorderRadius.all(35),content=
                                   ft.Stack(
                                              controls=[
                        decor,
                        maintext,
                        tinylogo,
                        menu1,
                        travel,
                        ft.Container(top=180, left=20, width=360, content=bigcalendar)
                                              ],
                                   ),
            
                        )
                    ]
                )
            )        
        
    
    page_16 = ft.Container(
        width=400, height=850, bgcolor=VDG, border_radius=ft.BorderRadius.all(35),
        content=ft.Stack(controls=[
            ft.Container(width=400, height=850, bgcolor=VDG, border_radius=ft.BorderRadius.all(35)),
            ft.Container(top=60, left=50, content=resultimage),
            ft.Container(top=380, left=30, content=resultfoodtext),
            ft.Container(top=420, left=30, content=resultcaltext),
            ft.Container(top=450, left=30, content=resultprotext),
            ft.Container(top=480, left=30, content=resultfattext),
            ft.Container(top=510, left=30, content=resultcarbtext),
            ft.Container(top=540, left=30, content=resultsugartext),
            resultbutton,
            menu1,
        ])
    )
    page_14 = ft.Container(          
            width=400,
            height=850,
            bgcolor=DG,
            padding= ft.Padding(0),
            border_radius=ft.BorderRadius.all(35),
            content=ft.ListView(
                expand=True,
                controls=[
                    ft.Container(width=400,height=1000,bgcolor=DG, border_radius=ft.BorderRadius.all(35),content=
                               ft.Stack(
                                          controls=[
                    decor,
                    maintext,
                    tinylogo,
                    menu1,
                    travel,
                    GALLERY,
                                          ],
                               ),
        
                    )
                ]
            )
        )
    page_13 = ft.Container(          
        width=400,
        height=850,
        bgcolor=DG,
        padding= ft.Padding(0),
        border_radius=ft.BorderRadius.all(35),
        content=ft.ListView(
            expand=True,
            controls=[
                ft.Container(width=400,height=1100,bgcolor=DG, border_radius=ft.BorderRadius.all(35),content=
                           ft.Stack(
                                     controls=[
                decor,
                maintext,
                tinylogo,
                menu1,
                travel,
                nutritiontitle,
                nutritioninfo,
                display,
                display2,
                display3,
                display4,
                display5,
                savedaybutton,
                                     ],
                           ),

                )
            ]
        )
    )
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
                                            menu1,
                                            
                                            
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
                                            decor,
                                            maintext,
                                            tinylogo,
                                            menu1,
                                            travel,
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
                                            square2,
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
                        bgcolor=DDG,
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
                            T3,
                            name1,
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
                 circle_3o1,

                ]
            
            )

    
    )
                 
   
    

#CODE


























    current_view = ft.Container(
           width=400, height=850, bgcolor=LG,
           border_radius=ft.BorderRadius.all(35),
           content=page_1,
           offset=ft.Offset(0,0)
    )



    outer_stack = ft.Stack(
        controls=[
            current_view,
            menu_backdrop,
            menu_panel,

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
