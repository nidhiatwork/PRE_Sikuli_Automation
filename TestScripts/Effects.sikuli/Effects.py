import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestEffects(unittest.TestCase):

    def setUp(self):       
        utils.cleanCache_And_LaunchPRE()
                  
    def test_UI_Effects(self):
        utils.clickElement("Button_GoalScreen_CloseGoalScreen.png")
        utils.assertElementExists("BaselineIMG_PRE_QuickView.png")
        
        utils.clickElement("Button_ExpertRoom.png") 
        utils.assertElementExists("BaselineIMG_ExportRoomTimeline.png")
        
        utils.findElement("BaselineIMG_ExportRoomTimeline.png")
        wait(2)
        utils.clickElement("Button_RHSPanels_Effects.png")
        
        utils.clickElement("DropDown_EffectsPanel_AllCategories.png")
        utils.assertElementExists("BaselineIMG_Effects_AllCategories.png")
        
        utils.clickElement("Effects_Category_AdvancedAdjustments.png")
        utils.assertElementExists("Effects_Category_AdvancedAdjustments_items.png")     
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Category_BlurSharpen_items.png")
 
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Category_Channel_items.png")
 
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_ColorCorrection_items.png")

        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_Distort_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_Generate_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_ImageControl_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_Keying_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_NewBlueArtEffects_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_NewBlueCartoonrPlus_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_NewBlueFilmLooks_items.png")
              
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_Perspective_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_Render_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_Stylize_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_Time_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_Transform_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")
        utils.assertElementExists("Effects_Categories_VideoMerge_items.png")
        
        utils.clickElement("Button_EffectCategories_Next.png")   
        wait(2)
        
        utils.clickElement("Button_EffectCategories_Next.png")   
        utils.assertElementExists("Effects_Categories_HollywoodLooks_items.png")              

    
        
    def tearDown(self):
       utils.closePRE()        

