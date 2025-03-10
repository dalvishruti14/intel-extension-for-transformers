# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from intel_extension_for_transformers.neural_chat.pipeline.plugins.audio.asr import AudioSpeechRecognition
import unittest
import os
import torch

class TestASR(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        try:
            import habana_frameworks.torch.hpu as hthpu
            self.is_hpu_available = True
        except ImportError:
            self.is_hpu_available = False
        try:
            import intel_extension_for_pytorch as intel_ipex
            self.is_ipex_available = True
        except ImportError:
            self.is_ipex_available = False
        if self.is_hpu_available:
            self.device = "hpu"
        else:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.asr = AudioSpeechRecognition("openai/whisper-small", device=self.device)
        if self.device == "cpu" and self.is_ipex_available:
            self.asr_bf16 = AudioSpeechRecognition("openai/whisper-small", bf16=True)
        else:
            self.asr_bf16 = None

    def test_audio2text(self):
        audio_path = "/intel-extension-for-transformers/intel_extension_for_transformers/neural_chat/assets/audio/welcome.wav"
        if os.path.exists(audio_path):
            text = self.asr.audio2text(audio_path)
        else:
            text = self.asr.audio2text("../../assets/audio/welcome.wav")
        self.assertEqual(text.lower(), "Welcome to Neural Chat".lower())

    def test_audio2text_bf16(self):
        if self.asr_bf16 is None:
            return
        audio_path = "/intel-extension-for-transformers/intel_extension_for_transformers/neural_chat/assets/audio/welcome.wav"
        if os.path.exists(audio_path):
            text = self.asr_bf16.audio2text(audio_path)
        else:
            text = self.asr_bf16.audio2text("../../assets/audio/welcome.wav")
        self.assertEqual(text.lower(), "Welcome to Neural Chat".lower())

if __name__ == "__main__":
    unittest.main()
