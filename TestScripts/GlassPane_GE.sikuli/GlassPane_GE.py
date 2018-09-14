import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestGlassPane_GE(unittest.TestCase):

    def setUp(self):
        utils.cleanCache_And_LaunchPRE()
        
    def test_UI_GlassPane_GE(self):

        utils.clickElement("Button_GoalScreen_CloseGoalScreen.png")
        utils.assertElementExists("BaselineIMG_PRE_QuickView.png")

        utils.clickElement("Button_GuidedRoom.png")
        utils.findElement("Button_GuidedRoom_Active.png")   
        utils.clickElement("Button_Guided_FunEdits.png")
        
        utils.clickElement("BaselineIMG_GlassPane_Placeholder.png")
        utils.assertElementExists("GlassPane_Step1_GlassPane.png")
        
        utils.clickElement("Button_GE_Next.png")
        wait(1)
        utils.assertElementExists("BaselineIMG_AddMedia_Highlighted.png")

        utils.assertElementExists("GlassPane_Step2_AddMedia.png")
        utils.clickElement("Button_GE_Next.png")
        wait(1)
        utils.assertElementExists("BaselineIMG_AddMediaOptions.png")
        utils.assertElementExists("GlassPane_Step3_AddMedia.png")
        
        
        utils.clickElement("Dropdown_AddMedia_FilesAndFolders.png")
        
        utils.clickElement("GlassPane_Import_Window.png")
                   
        
        type(Constants.TestDataFile_path)
        type(Key.ENTER)
        utils.clickElement("GlassPane_TestData.png")
        type(Key.ENTER)
        
        
        utils.assertElementExists("GlassPane_Step5_AddMediaToTimeline.png")
        
        utils.assertElementExists("GlassPane_ProjectAssets.png")
        utils.clickElement("GlassPane_ProjectAssets.png")
        mouseDown(Button.LEFT)
        mouseMove(4,4)
        wait(1)
        mouseMove("GlassPane_ProjectAssets.png")
        wait(1)
        mouseMove("GlassPane_MonitorArea.png")
        wait(1)
        mouseUp()

        utils.assertElementExists("GlassPane_Step5_AddMediaToTimeline_Track2.png")
        
        wait(2)
        hover(Pattern("Button_Timeline_Up.png").similar(0.74))
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(5)
        mouseUp()

        utils.clickElement("GlassPane_ProjectAssets.png")
        mouseDown(Button.LEFT)
        mouseMove(4,4)
        wait(1)
        mouseMove("GlassPane_ProjectAssets.png")
        wait(1)
        mouseMove("VideoTrack2.png")
        wait(1)
        mouseUp()

        utils.assertElementExists("GlassPane_Step6_AddOverlay_1.png")
        
        wait(3)
        utils.clickElement("Button_GE_Next.png")  
        utils.assertElementExists("GlassPane_Step6_AddOverlay_2.png")
        utils.assertElementExists("BaselineIMG_GE_MatteOverlaysHighlighted.png")
        
        wait(2)
        hover(Pattern("Button_Timeline_Up.png").similar(0.74))
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(4)
        mouseUp()
       
        utils.clickElement("MatteOverlay01.png")
        mouseDown(Button.LEFT)
        mouseMove(4,4)
        wait(1)
        mouseMove("MatteOverlay01.png")
        wait(2)
        mouseMove("AudioTrack3.png")
        wait(1)
        mouseUp()

        utils.findElement("Button_GE_Next.png")
        wait(1)
        
        utils.assertElementExists("GlassPane_Step6_AddOverlay_3.png")
        
        utils.clickElement("Button_GE_Next.png")  
        wait(1)
        utils.assertElementExists("GlassPane_EffectPanelHighlighted.png")
        utils.clickElement("Button_GE_Next.png")  
        utils.assertElementExists("GlassPane_Step7_TrackMatteEffect_1.png")
        
        utils.assertElementExists("BaselineIMG_TrackMatteEffectHighlighted.png")
        
        wait(2)
        hover(Pattern("Button_Timeline_Up.png").similar(0.74))
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(4)
        mouseUp()

        utils.clickElement("BaselineIMG_TrackMatteEffectHighlighted.png")
        mouseDown(Button.LEFT)
        mouseMove(4,4)
        wait(1)
        mouseMove("BaselineIMG_TrackMatteEffectHighlighted.png")
        wait(1)
        mouseMove(Pattern("GlassPane_TrackMatte_DropArea.png").similar(0.80))
        wait(1)
        mouseUp()

        utils.assertElementExists("GlassPane_Step7_TrackMatteEffect_3.png")

        utils.assertElementExists("BaselineIMG_TrackMatteKey_paramsHighlighted.png")
        utils.clickElement("DropDown_TrackMatte_None.png")
        
        utils.clickElement("DropDown_Matte_Video3Option.png")
        wait(1)
        utils.clickElement("DropDown_TrackMatte_ComositeUsing.png")
        utils.clickElement("DropDown_ComositeUsing_MatteLumaOption.png")

        utils.assertElementExists("GlassPane_Step7_TrackMatteEffect_4.png")
        
        wait(2)
        utils.clickElement("Button_GE_Next.png")
        utils.assertElementExists("GlassPane_Step8_AddBlurEffect_1.png")
        utils.assertElementExists("GlassPane_EffectPanelHighlighted.png")
        utils.clickElement("GlassPane_EffectPanelHighlighted.png")
        wait(2)
        utils.assertElementExists("GlassPane_Step8_AddBlurEffect_2.png")

        utils.clickElement("BaselineIMG_FastBlurHighlighted.png")
        mouseDown(Button.LEFT)
        mouseMove(4,4)
        wait(1)
        mouseMove("BaselineIMG_FastBlurHighlighted.png")
        wait(1)
        mouseMove("BaselineIMG_Media_VideoTrack1.png")
        wait(1)
        mouseUp()

        utils.assertElementExists("GlassPane_Step8_AddBlurEffect_3.png")
        exists("BaselineIMG_FastBlur_ParamsHighlighted.png")
        
        wait(2)
        utils.clickElement("Button_GE_Next.png")                
        utils.assertElementExists("GlassPane_Step9_AddAdjustments_1.png")
        
        utils.assertElementExists("BaselineIMG_AdjustmentHighlighted.png")
        utils.clickElement("BaselineIMG_AdjustmentHighlighted.png")        
        utils.assertElementExists("GlassPane_Step9_AddAdjustments_2.png")
        utils.assertElementExists("BaselineIMG_Temperature-TintHighlighted.png")
       
        utils.clickElement("BaselineIMG_Temperature-TintHighlighted.png")   

        utils.assertElementExists("BaselineIMG_TemperatureTint_Presets.png")
        
        utils.assertElementExists("BaselineIMG_TemperatureTint_Presets.png")
        utils.assertElementExists("GlassPane_Step9_AddAdjustments_3.png")
        
        utils.clickElement("Preset_TemperatureTint.png")
        
        utils.assertElementExists("GlassPane_Step9_AddAdjustments_4.png")
        wait(2)
        utils.clickElement("Button_GE_Next.png")         
        
        utils.assertElementExists("GlassPane_LastStep.png")
        utils.clickElement("Button_GlassPane_Done.png")
        

    def tearDown(self):
       utils.closePRE()        

