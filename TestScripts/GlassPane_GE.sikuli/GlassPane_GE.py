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
        #setBundlePath(Constants.BaselineFolder)

        # utils.clickElement("Button_GoalScreen_CloseGoalScreen.png")
        # utils.assertElementExists("BaselineIMG_PRE_QuickView.png")

        # utils.clickElement("Button_GuidedRoom.png")
        # utils.findElement("Button_GuidedRoom_Active.png")   
        #utils.clickElement("Button_Guided_FunEdits.png")
        
        # utils.clickElement("BaselineIMG_GlassPane_Placeholder.png")
        # utils.assertElementExists("GlassPane_Step1_GlassPane.png")
        
        # utils.clickElement("Button_GE_Next.png")

        # utils.assertElementExists("BaselineIMG_AddMedia_Highlighted.png")

        # utils.assertElementExists("GlassPane_Step2_AddMedia.png")
        
        # utils.clickElement("Button_GE_Next.png")
        
        # utils.assertElementExists("BaselineIMG_AddMediaOptions.png")
        # utils.assertElementExists("GlassPane_Step3_AddMedia.png")
        
        
        # utils.clickElement("Dropdown_AddMedia_FilesAndFolders.png")
        
        # click(Pattern("GlassPane_Import_Window.png").similar(0.79))
                   
        
        # type(Constants.TestDataFile_path)
        # type(Key.ENTER)
        # utils.clickElement("GlassPane_TestData.png")
        # type(Key.ENTER)
        
        
        # exists("GlassPane_Step5_AddMediaToTimeline.png")
        
        # utils.assertElementExists("GlassPane_ProjectAssets.png")
        # hover("GlassPane_ProjectAssets.png")
        # mouseDown(Button.LEFT)
        # mouseMove("GlassPane_ProjectAssets.png")
        # wait(5)
        # hover("GlassPane_MonitorArea.png")
        # wait(1)
        # mouseUp()

        exists("GlassPane_Step5_AddMediaToTimeline_Track2.png")
        
        wait(2)
        hover(Pattern("Button_Timeline_Up.png").similar(0.74))
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(5)
        mouseUp()

        hover("GlassPane_ProjectAssets.png")
        mouseDown(Button.LEFT)
        mouseMove("GlassPane_ProjectAssets.png")
        wait(5)
        hover("VideoTrack2.png")
        wait(1)
        mouseUp()

        exists("GlassPane_Step6_AddOverlay_1.png")
        

        wait(3)
        utils.clickElement("Button_GE_Next.png")  
        exists("GlassPane_Step6_AddOverlay_2.png")
        
        
        exists("BaselineIMG_GE_MatteOverlaysHighlighted.png")
        

        wait(2)
        hover(Pattern("Button_Timeline_Up.png").similar(0.74))
        mouseDown(Button.LEFT)
        mouseMove("Button_Timeline_Up.png")
        wait(2)
        mouseUp()
        

        hover("MatteOverlay01.png")
        mouseDown(Button.LEFT)
        mouseMove("MatteOverlay01.png")
        wait(5)
        hover("VideoTrack3.png")
        wait(1)
        mouseUp()


        utils.findElement("Button_GE_Next.png")
        wait(2)
        exists("GlassPane_Step6_AddOverlay_3.png")
        
        utils.clickElement("Button_GE_Next.png")  
        utils.clickElement("Button_GE_Next.png")  
        exists("GlassPane_Step7_TrackMatteEffect_1.png")
        
        exists("BaselineIMG_TrackMatteEffectHighlighted.png")
        wait(2)
        click(Pattern("Button_Timeline_Up.png").similar(0.74))
        mouseDown(Button.LEFT)
        wait(2)
        mouseUp()
        hover("BaselineIMG_TrackMatteEffectHighlighted.png")
        mouseDown(Button.LEFT)
        mouseMove("BaselineIMG_TrackMatteEffectHighlighted.png")
        wait(1)
        hover("GlassPane_TrackMatte_DropArea.png")
        
        mouseUp()

        exists("GlassPane_Step7_TrackMatteEffect_3.png")
        
        
        utils.findElement("BaselineIMG_TrackMatteKey_paramsHighlighted.png")
        utils.clickElement("DropDown_TrackMatte_None.png")
        utils.clickElement("DropDown_Matte_Video3Option.png")
        utils.findElement("GlassPane_Step7_TrackMatteEffect_3.png")        
        utils.clickElement("DropDown_TrackMatte_ComositeUsing.png")
        utils.clickElement("DropDown_ComositeUsing_MatteLumaOption.png")
        utils.findElement("GlassPane_Step7_TrackMatteEffect_4.png")
        wait(2)
        utils.clickElement("Button_GE_Next.png")
        utils.findElement("GlassPane_Step8_AddBlurEffect_1.png")
        utils.findElement("BaselineIMG_TrackMatteEffectHighlighted.png")
        utils.clickElement("BaselineIMG_TrackMatteEffectHighlighted.png")        
        wait(2)
        utils.findElement("GlassPane_Step8_AddBlurEffect_2.png")
        utils.findElement("BaselineIMG_FastBlurHighlighted.png")
        dragDrop("BaselineIMG_FastBlurHighlighted.png", "BaselineIMG_Media_VideoTrack1.png")
        utils.findElement("GlassPane_Step8_AddBlurEffect_3.png")
        utils.findElement("BaselineIMG_FastBlur_ParamsHighlighted.png")
        wait(2)
        utils.clickElement("Button_GE_Next.png")                
        utils.findElement("GlassPane_Step9_AddAdjustments_1.png")
        utils.findElement("BaselineIMG_AdjustmentHighlighted.png")
        utils.clickElement("BaselineIMG_AdjustmentHighlighted.png")        
        utils.findElement("GlassPane_Step9_AddAdjustments_2.png")
        utils.findElement("BaselineIMG_Temperature-TintHighlighted.png")
        utils.clickElement("BaselineIMG_Temperature-TintHighlighted.png")   
        utils.findElement("BaselineIMG_TemperatureTint_Presets.png")
        utils.findElement("GlassPane_Step9_AddAdjustments_3.png")
        utils.clickElement("Preset_TemperatureTint.png")
        utils.findElement("GlassPane_Step9_AddAdjustments_4.png")
        wait(2)
        utils.clickElement("Button_GE_Next.png")                        
        utils.assertElementExists("GlassPane_Step10_Done.png")
        utils.clickElement("Button_GlassPane_Done.png")
        

    def tearDown(self):
       utils.closePRE()        

