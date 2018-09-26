import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestTransitions(unittest.TestCase):

    def setUp(self):       
        cleanCache_And_LaunchPRE()
        
    def test_UI_Transitions(self):
        doubleClickElement("Button_GoalScreen_CloseGoalScreen.png")
        wait(2)
        assertElementExists("BaselineIMG_PRE_QuickView.png")
        
        clickElement("Button_ExpertRoom.png") 
        assertElementExists("BaselineIMG_ExportRoomTimeline.png")
        
        findElement("BaselineIMG_ExportRoomTimeline.png")
        wait(2)
        
        clickElement("Button_RHSPanels_Transitions.png")
        
        
        clickElement("DropDown_Panel_AllCategories.png")   
        assertElementExists("BaselineIMG_Transitions_AllCategories.png")

        clickElement("Transition_Category_3DMotion.png")      
        assertElementExists("Transition_Category_3DMotion_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")
	    
        assertElementExists("Transition_Category_Dissolve_items.png")
       
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        assertElementExists("Transition_Category_Iris_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        assertElementExists("Transition_Category_NewBlue3DExplosion_items.png")
                
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        assertElementExists("Transition_Category_NewBlue3DTransformations_items.png")     
                
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        
        assertElementExists("Transition_Category_NewBlue_ArtBlends_items.png")
                
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        assertElementExists("Transition_Category_NewBlue_MotionBlends_items.png")
                
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        assertElementExists("Transition_Category_PagePeel_items.png")        
                
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        assertElementExists("Transition_Category_PictureWipes_items.png")        
                    
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        assertElementExists("Transition_Category_Slide_items.png")
                                       
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        assertElementExists("Transition_Category_Wipe_items.png")        
                    
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        assertElementExists("Transition_Category_Zoom_items.png")
        

    def tearDown(self):
       closePRE()        
