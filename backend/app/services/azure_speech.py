"""Azure Text-to-Speech Service"""
import azure.cognitiveservices.speech as speechsdk
from app.config import settings
import os
import logging

logger = logging.getLogger(__name__)

class AzureSpeechService:
    def __init__(self):
        self.speech_config = speechsdk.SpeechConfig(
            subscription=settings.AZURE_SPEECH_KEY,
            region=settings.AZURE_SPEECH_REGION
        )
        
        # Configure voice
        self.speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"
    
    async def text_to_speech(
        self, 
        text: str, 
        output_path: str,
        voice_name: str = "en-US-JennyNeural"
    ) -> str:
        """Convert text to speech and save to file"""
        try:
            # Set voice
            self.speech_config.speech_synthesis_voice_name = voice_name
            
            # Configure audio output
            audio_config = speechsdk.audio.AudioOutputConfig(filename=output_path)
            
            # Create synthesizer
            synthesizer = speechsdk.SpeechSynthesizer(
                speech_config=self.speech_config,
                audio_config=audio_config
            )
            
            # Generate speech
            result = synthesizer.speak_text_async(text).get()
            
            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                logger.info(f"Speech synthesized successfully: {output_path}")
                return output_path
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation = result.cancellation_details
                logger.error(f"Speech synthesis canceled: {cancellation.reason}")
                if cancellation.reason == speechsdk.CancellationReason.Error:
                    logger.error(f"Error details: {cancellation.error_details}")
                raise Exception(f"Speech synthesis failed: {cancellation.error_details}")
            
        except Exception as e:
            logger.error(f"Azure Speech error: {e}")
            raise
    
    async def synthesize_ssml(self, ssml: str, output_path: str) -> str:
        """Synthesize speech using SSML"""
        try:
            audio_config = speechsdk.audio.AudioOutputConfig(filename=output_path)
            synthesizer = speechsdk.SpeechSynthesizer(
                speech_config=self.speech_config,
                audio_config=audio_config
            )
            
            result = synthesizer.speak_ssml_async(ssml).get()
            
            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                return output_path
            else:
                raise Exception("SSML synthesis failed")
                
        except Exception as e:
            logger.error(f"SSML synthesis error: {e}")
            raise
