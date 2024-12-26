# 音声生成
GCP(Google Cloud Platform)が提供する、text to speech APiを用いて音声生成を行う

## text to speechについて
- DL(DeepLearning)を用いて、テキストから自然な音声生成ができる
- speech to text（音声→テキスト）もある


## 音声生成スクリプト
### インポート
以下のようにして、Google cloudのtexttospeechをインポートする
```
from google.cloud import texttospeech
```

### 音声生成設定
音声生成において、テキスト、話者の性別、言語、出力形式等を設定する。

#### テキスト
以下のように、インポートしたtexttospeechにテキストを渡す
```
synthesis_input = texttospeech.SynthesisInput(text=text)
```

#### 性別と言語
話者の性別と言語を以下のように設定できる

```
# 言語を日本語に
lang='日本語'
# 性別をdefalutに
gender='defalut'

gender_type = {
    # defalutの場合、不特定の性別となる
    'defalut': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
    'male': texttospeech.SsmlVoiceGender.MALE,
    'female': texttospeech.SsmlVoiceGender.FEMALE,
    'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
}
lang_code = {
    '英語': 'en-US',
    '日本語': 'ja-JP'
}

voice = texttospeech.VoiceSelectionParams(
    # lang, genderそれぞれに対応した情報を渡す
    language_code=lang_code[lang], ssml_gender=gender_type[gender]
)
```

### 音声の生成
以下のように、texttospeech clientのsynthesize_speechに設定情報を渡すことで、生成された音声を得られる。
```
client = texttospeech.TextToSpeechClient()
# 上記で設定した情報をtexttospeechに渡す
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)
```