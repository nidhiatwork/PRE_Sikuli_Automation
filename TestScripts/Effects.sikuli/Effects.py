import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestEffects(unittest.TestCase):

    def setUp(self):       
        cleanCache_And_LaunchPRE()
                  
    def test_UI_Effects(self):
        clickElement("Button_GoalScreen_CloseGoalScreen.png")
        assertElementExists("BaselineIMG_PRE_QuickView.png")
        
        clickElement("Button_ExpertRoom.png") 
        assertElementExists("BaselineIMG_ExportRoomTimeline.png")
        
        findElement("BaselineIMG_ExportRoomTimeline.png")
        wait(2)
        clickElement("Button_RHSPanels_Effects.png")
        
        clickElement("DropDown_Panel_AllCategories.png")
        assertElementExists("BaselineIMG_Effects_AllCategories.png")
        
        clickElement("Effects_Category_AdvancedAdjustments.png")
        assertElementExists("Effects_Category_AdvancedAdjustments_items.png")     
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        
        assertElementExists("Effects_Category_BlurSharpen_items.png")
 
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Category_Channel_items.png")
 
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_ColorCorrection_items.png")

        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_Distort_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_Generate_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_ImageControl_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_Keying_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_NewBlueArtEffects_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_NewBlueCartoonrPlus_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_NewBlueFilmLooks_items.png")
              
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_Perspective_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_Render_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_Stylize_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_Time_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_Transform_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_VideoMerge_items.png")
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        wait(2)
        
        clickElement("Button_Categories_Next.png")
        hoverElement("NonClickable_EffectsPanelText.png")
        assertElementExists("Effects_Categories_HollywoodLooks_items.png")              

    
        
    def tearDown(self):
       closePRE()        

