
## SAO Releases Stalk

Personal project that allows people to get notified whenever kadokawa uploads the cover/Bookwalker uploads the preview of a newly SAO release.

In addition, the script automatically downloads the cover or rips the preview images.

tested with Python 3.9.5 on Windows 10.



## Usage
### Main usage
- Download the repository
- Do `pip install -r requirements.txt`
- Launch the `sao-releases-stalk.py` file with your Command Prompt
- Follow the instructions
- Wait until you get a notification

The "ID" of the release can be found in its URL. (Example: kadokawa.co.jp/product/**322102000017**/ or bookwalker.jp/**ded6f8074d-9a1d-4f57-bcdc-c011aaed6fc5**/).



### To enable the option that rips the images of the Bookwalker preview:
- Install [this](https://github.com/Atemu/bookwalker-dl) (and its dependencies)
- Rename `bw-dl.bash` to `bw-dl.sh`, and stick the file next to `sao-releases-stalk.py`
- Uncomment the [94th line](https://github.com/CeIest/SAO-Releases-Stalk/blob/main/sao-releases-stalk.py#L94) of the main script


## To-do list
- Add e-mail support
- Automatically upload the ripped bw files on Imgur or on a Drive
- Write the repo's own ripper
