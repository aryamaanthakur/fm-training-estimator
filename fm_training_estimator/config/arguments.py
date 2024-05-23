# Standard
from dataclasses import dataclass, field

# Third Party
from peft.tuners.lora import LoraConfig
from peft.tuners.prompt_tuning import PromptTuningConfig
from transformers import TrainingArguments


@dataclass
class PeftPromptTuningConfig(PromptTuningConfig):
    """dataclass for promptuning config

    Args:
        PromptTuningConfig (_type_): imported directly from peft library
    """


@dataclass
class PeftLoraConfig(LoraConfig):
    """dataclass for lora config

    Args:
        LoraConfig (_type_): directly imported from peft library
    """


@dataclass
class HFTrainingArguments(TrainingArguments):
    """HF trainer arguments

    Args:
        TrainingArguments (_type_): directly imported from transformers library
    """


@dataclass
class InfraArguments:
    """dataclass for infrastructure arguments"""

    numGpusPerPod: int = field(
        default=1,
        metadata={"help": ("number of gpus requested per pod")},
    )

    numPods: int = field(
        default=1,
        metadata={"help": ("number of pods requested")},
    )


@dataclass
class FMArguments:
    """dataclass to store additional args not covered by standard HF argument dataclasses"""

    base_model_path: str = field(
        default="/data/models/granite20b/",
        metadata={
            "help": (
                "Base Model location. Can be empty if output path has a checkpoint."
            )
        },
    )

    flash_attention_v2: bool = field(
        default=False,
        metadata={"help": ("It enable flash attention v2 for attention calculation.")},
    )

    lora_config: str = field(
        default=None, metadata={"help": ("LORA configuration json file path.")}
    )

    max_seq_length: int = field(
        default=2048,
        metadata={"help": ("model max sequence length.")},
    )

    data_config_file: str = field(
        default="data_config.json",
        metadata={"help": ("Input files in glob format.")},
    )

    prompt_tuning_config: str = field(
        default=None, metadata={"help": ("Prompt tuning config json file path")}
    )

    torch_dtype: str = field(
        default="float32",
        metadata={
            "help": (
                "provide torch dtype for the model precision. \
                Choose one from float16, float32, bfloat16"
            )
        },
    )
