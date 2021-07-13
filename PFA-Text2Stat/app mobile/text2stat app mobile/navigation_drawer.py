navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                
                
                BoxLayout:
                    orientation: 'vertical'
                    spacing:10
                    MDToolbar:
                       
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:5
                        Image:
                            id: avatar
                            size_hint: (0.75,0.75)
                            source: "ump.png"
                    
                    FloatLayout:
                        Label:
                            id: login_message
                            text: "Connectez-vous sur Facebook"
                            color: (0, 0, 1)
                            size_hint: .8, .1
                            pos_hint: {"top": 0.9, "right": 0.9}
                        TextInput:
                            id: login_email
                            hint_text: "email"
                            size_hint: .8, .2
                            pos_hint: {"top": 0.6, "right": 0.9}
                        TextInput:
                            id: login_password
                            password: True
                            hint_text: "password"
                            size_hint: .8, .2
                            pos_hint: {"top": 0.3, "right": 0.9}
                        
                        
                        
                      
                    Widget:
                    
        MDNavigationDrawer:
            id: nav_drawer
            
                  
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "img.png"
                
                ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Acceuil"

                                IconLeftWidget:
                                    icon: "home"



                            OneLineIconListItem:
                                text: "Dashboards"

                                IconLeftWidget:
                                    icon: "animation"


                            OneLineIconListItem:
                                text: "Mois"

                                IconLeftWidget:
                                    icon: "calendar-month-outline"





"""