import requests

class MessagingSender():
    """
    LINE NOTIFYでメッセージを送る
    """
    url = 'https://notify-api.line.me/api/notify'

    def __init__(self, token):
        """
        Parameters
        ----------
        token: String
            アクセストークン
        """

        self.token = token
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def send_message(self, message, image=None, sticker_package_id=None, sticker_id=None):
        """
        メッセージを送る

        Parameters
        ----------
        message: String
            送るメッセージ
        image: String, default None
            画像のパス（送る場合のみ）
        sticker_package_id: int, default None
            スタンプID
        sticker_id: int, default None
            スタンプID 上のやつもhttps://devdocs.line.me/files/sticker_list.pdfから探す
        """

        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id
        }

        # 画像送信
        files = {}
        if image != None:
            files['imageFile'] = open(image, 'rb')

        r = requests.post(
            MessagingSender.url,
            headers=self.headers,
            data=payload,
            files=files
        )


