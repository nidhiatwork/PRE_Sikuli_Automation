import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestTransitions(unittest.TestCase):

    def setUp(self):       
        utils.cleanCache_And_LaunchPRE()
        
    def test_UI_Transitions(self):
        utils.clickElement("Button_GoalScreen_CloseGoalScreen.png")
        utils.assertElementExists("BaselineIMG_PRE_QuickView.png")
        
        utils.clickElement("Button_ExpertRoom.png") 
        utils.assertElementExists("BaselineIMG_ExportRoomTimeline.png")
        
        utils.findElement("BaselineIMG_ExportRoomTimeline.png")
        wait(2)
        
        utils.clickElement("Button_RHSPanels_Transitions.png")
        
        
        utils.clickElement("DropDown_Panel_AllCategories.png")   
        utils.assertElementExists("BaselineIMG_Transitions_AllCategories.png")

        utils.clickElement("Transition_Category_3DMotion.png")      
        utils.assertElementExists("Transition_Category_3DMotion_items.png")
        
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")
	    
        utils.assertElementExists("Transition_Category_Dissolve_items.png")
       
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        utils.assertElementExists("Transition_Category_Iris_items.png")
        
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        utils.assertElementExists("Transition_Category_NewBlue3DExplosion_items.png")
                
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        utils.assertElementExists("Transition_Category_NewBlue3DTransformations_items.png")     
                
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        
        utils.assertElementExists("Transition_Category_NewBlue_ArtBlends_items.png")
                
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        utils.assertElementExists("Transition_Category_NewBlue_MotionBlends_items.png")
                
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        utils.assertElementExists("Transition_Category_PagePeel_items.png")        
                
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        utils.assertElementExists("Transition_Category_PictureWipes_items.png")        
                    
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        utils.assertElementExists("Transition_Category_Slide_items.png")
                                       
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        utils.assertElementExists("Transition_Category_Wipe_items.png")        
                    
        utils.clickElement("Button_Categories_Next.png")
        utils.hoverElement("NonClickable_TransitionsPanel_EffectsText.png")

        utils.assertElementExists("Transition_Category_Zoom_items.png")
        

    def tearDown(self):
       utils.closePRE()        
