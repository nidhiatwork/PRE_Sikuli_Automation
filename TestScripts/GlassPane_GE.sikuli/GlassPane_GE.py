import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestGlassPane_GE(unittest.TestCase):

    def setUp(self):
        cleanCache_And_LaunchPRE()
        
    def test_UI_GlassPane_GE(self):

        clickElement("Button_GoalScreen_CloseGoalScreen.png")
        assertElementExists("BaselineIMG_PRE_QuickView.png")

        clickElement("Button_GuidedRoom.png")
        findElement("Button_GuidedRoom_Active.png")   
        clickElement("Button_Guided_FunEdits.png")
        
        clickElement("BaselineIMG_GlassPane_Placeholder.png")
        assertElementExists("GlassPane_Step1_GlassPane.png")
        
        clickElement("Button_GE_Next.png")
        wait(1)
        assertElementExists("BaselineIMG_AddMedia_Highlighted.png")

        assertElementExists("GlassPane_Step2_AddMedia.png")
        clickElement("Button_GE_Next.png")
        wait(1)
        assertElementExists("BaselineIMG_AddMediaOptions.png")
        assertElementExists("GlassPane_Step3_AddMedia.png")
          
        clickElement("Dropdown_AddMedia_FilesAndFolders.png")
        clickElement("GlassPane_Import_Window.png")               
        
        typeKeys(Constants.TestDataFile_path)
        type(Key.ENTER)
        clickElement("GlassPane_TestData.png")
        type(Key.ENTER)
          
        assertElementExists("GlassPane_Step5_AddMediaToTimeline.png")       
        assertElementExists("GlassPane_ProjectAssets.png")

        dragAndDropElement("GlassPane_ProjectAssets.png", "GlassPane_MonitorArea.png")

        assertElementExists("GlassPane_Step5_AddMediaToTimeline_Track2.png")
        
        wait(2)
        hoverElement("Button_Timeline_Up.png")
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(5)
        mouseUp()

        dragAndDropElement("GlassPane_ProjectAssets.png","VideoTrack2.png")
        assertElementExists("GlassPane_Step6_AddOverlay_1.png")
        
        wait(3)
        clickElement("Button_GE_Next.png")  
        assertElementExists("GlassPane_Step6_AddOverlay_2.png")
        assertElementExists("BaselineIMG_GE_MatteOverlaysHighlighted.png")
        
        wait(2)
        hoverElement("Button_Timeline_Up.png")
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(4)
        mouseUp()
       
        dragAndDropElement("MatteOverlay01.png","AudioTrack3.png")
        findElement("Button_GE_Next.png")
        wait(1)
        assertElementExists("GlassPane_Step6_AddOverlay_3.png")
        
        clickElement("Button_GE_Next.png")  
        wait(1)
        assertElementExists("GlassPane_EffectPanelHighlighted.png")
        clickElement("Button_GE_Next.png")  
        assertElementExists("GlassPane_Step7_TrackMatteEffect_1.png")
        
        assertElementExists("BaselineIMG_TrackMatteEffectHighlighted.png")
        
        wait(2)
        hoverElement("Button_Timeline_Up.png")
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(4)
        mouseUp()

        dragAndDropElement("BaselineIMG_TrackMatteEffectHighlighted.png", "GlassPane_TrackMatte_DropArea.png")
        assertElementExists("GlassPane_Step7_TrackMatteEffect_3.png")

        assertElementExists("BaselineIMG_TrackMatteKey_paramsHighlighted.png")
        clickElement("DropDown_TrackMatte_None.png")
        
        clickElement("DropDown_Matte_Video3Option.png")
        wait(1)
        clickElement("DropDown_TrackMatte_ComositeUsing.png")
        clickElement("DropDown_ComositeUsing_MatteLumaOption.png")

        assertElementExists("GlassPane_Step7_TrackMatteEffect_4.png")
        
        wait(2)
        clickElement("Button_GE_Next.png")
        assertElementExists("GlassPane_Step8_AddBlurEffect_1.png")
        assertElementExists("GlassPane_EffectPanelHighlighted.png")
        clickElement("GlassPane_EffectPanelHighlighted.png")
        wait(2)
        assertElementExists("GlassPane_Step8_AddBlurEffect_2.png")

        dragAndDropElement("BaselineIMG_FastBlurHighlighted.png", "BaselineIMG_Media_VideoTrack1.png")
        assertElementExists("GlassPane_Step8_AddBlurEffect_3.png")
        exists("BaselineIMG_FastBlur_ParamsHighlighted.png")
        
        wait(2)
        clickElement("Button_GE_Next.png")                
        assertElementExists("GlassPane_Step9_AddAdjustments_1.png")
        
        assertElementExists("BaselineIMG_AdjustmentHighlighted.png")
        clickElement("BaselineIMG_AdjustmentHighlighted.png")        
        assertElementExists("GlassPane_Step9_AddAdjustments_2.png")
        assertElementExists("BaselineIMG_Temperature-TintHighlighted.png")
       
        clickElement("BaselineIMG_Temperature-TintHighlighted.png")   

        assertElementExists("BaselineIMG_TemperatureTint_Presets.png")
        
        assertElementExists("BaselineIMG_TemperatureTint_Presets.png")
        assertElementExists("GlassPane_Step9_AddAdjustments_3.png")
        
        clickElement("Preset_TemperatureTint.png")
        
        assertElementExists("GlassPane_Step9_AddAdjustments_4.png")
        wait(2)
        clickElement("Button_GE_Next.png")         
        
        assertElementExists("GlassPane_LastStep.png")
        clickElement("Button_GlassPane_Done.png")
        

    def tearDown(self):
       closePRE()        

