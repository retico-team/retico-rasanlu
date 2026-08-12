from retico_rasanlu import RasaNLUModule
from retico_core.audio import MicrophoneModule
from retico_googleasr.googleasr import GoogleASRModule
from retico_core.debug import DebugModule

asr = GoogleASRModule()
model_dir = "C:\\Users\\dalto\\OneDrive\\Desktop\\School\\Internship\\tofix\\retico-rasanlu\\incremental-rasa-nlu\\examples\\moodbot_incremental\\models\\nlu-20260803-171453-warm-idea.tar.gz"
nlu = RasaNLUModule(model_dir=model_dir, incremental=False)
mic = MicrophoneModule()
debug = DebugModule(print_payload_only=True)

mic.subscribe(asr)
asr.subscribe(nlu)
nlu.subscribe(debug)

asr.run()
nlu.run()
mic.run()
debug.run()

input()

mic.stop()
asr.stop()
nlu.stop()
debug.stop()
