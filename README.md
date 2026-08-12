# retico-rasa-nlu
ReTiCo Module for Rasa NLU. Uses incremental version of Rasa to provide intent classification using ReTiCo's incremental dialogue pipeline.

## Installation and Requirements

As specified on pyproject a specific version of Python (3.7 || 3.8) will be required.

* Install the retico-rasanlu: ```pip install git+https://github.com/retico-team/retico-rasanlu```

You will need to install a spaCy language model. A good option can be found below.
* SpaCy language model download: ```python -m spacy download en_core_web_md```

A Google cloud account may be required if running the example code. Please refer to [retico-googleasr](https://github.com/retico-team/retico-googleasr) to be able to run it properly.
* Install the retico-rasanlu and include googleasr: ```pip install retico-rasanlu[asr] @ git+https://github.com/retico-team/retico-rasanlu```

### Training an NLU model

You need a trained RasaNLU model before you can use the module.

- An example config.yml and domain for training can be found [here](https://bitbucket.org/bsu-slim/incremental-rasa-nlu/src/master/examples/moodbot_incremental/).
- [This video](https://drive.google.com/file/d/1A-W1itqtMQoI_Igl94moaje0ATT2GWte/view?usp=drive_link) explains how to setup the environment, domain, and training.

You may also follow these steps:

1. Find where pip installed the fork's source (or, if you cloned it manually for reference, navigate there):

   ```bash
   cd examples/moodbot_incremental
   ```

2. Train the model:

   ```bash
   rasa train nlu
   ```

   This produces a trained model file under `models/`, e.g. `models/nlu-20260803-171453-warm-idea.tar.gz`. If replicating the runner example, you'll pass this path to `RasaNLUModule` as `model_dir`.

## Modules

### `RasaNLUModule`

Incrementally classify intent and extract entities from text using a trained, incremental Rasa NLU model.

Arguments:

* `model_dir` (str): Path to a trained model `.tar.gz` file, or a directory containing one
* `preprocessor` (callable, optional): Custom function to preprocess incoming text before it's passed to the interpreter. Defaults to `None`

## Example

```python
from retico_core.audio import MicrophoneModule
from retico_googleasr.googleasr import GoogleASRModule
from retico_rasanlu import RasaNLUModule
from retico_core.debug import DebugModule

mic = MicrophoneModule()
asr = GoogleASRModule()
model_dir = "path/to/rasa/model/directory"
nlu = RasaNLUModule(model_dir=model_dir, incremental=False)
debug = DebugModule(print_payload_only=True)

mic.subscribe(asr)
asr.subscribe(nlu)
nlu.subscribe(debug)

mic.run()
asr.run()
nlu.run()
debug.run()

input()

mic.stop()
asr.stop()
nlu.stop()
debug.stop()
```

Citation
```

@ARTICLE{Bocklisch2017-ez,
  title    = "Rasa: Open Source Language Understanding and Dialogue Management",
  author   = "Bocklisch, Tom and Faulkner, Joey and Pawlowski, Nick and Nichol,
              Alan",
  abstract = "We introduce a pair of tools, Rasa NLU and Rasa Core, which are
              open source python libraries for building conversational
              software. Their purpose is to make machine-learning based
              dialogue management and language understanding accessible to
              non-specialist software developers. In terms of design
              philosophy, we aim for ease of use, and bootstrapping from
              minimal (or no) initial training data. Both packages are
              extensively documented and ship with a comprehensive suite of
              tests. The code is available at https://github.com/RasaHQ/",
  journal  = "Proceedings of the 31st Conference on Neural Information
              Processing Systems",
  year     =  2017,
  address  = "Long Beach, CA"
}
```
