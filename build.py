#!/usr/bin/env python3
"""
Threes 지원 · 개인정보 처리방침 페이지 생성기 (GitHub Pages).
  python3 build.py   →  index.html, privacy.html (언어 자동 이동) + <lang>/index.html, <lang>/privacy.html
문구는 아래 CONTENT 에서 고친다. 앱 스토어에는 언어별 주소를 넣는다:
  지원:   https://ohtt-ios.github.io/Threes-public/<lang>/
  개인정보: https://ohtt-ios.github.io/Threes-public/<lang>/privacy.html
"""
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "https://ohtt-ios.github.io/Threes-public"
ISSUES = "https://github.com/ohtt-iOS/Threes-public/issues"
APP_STORE = "https://apps.apple.com/app/id6812920395"
EFFECTIVE = "2026-09-18"
LANG_NAMES = {"en": "English", "ko": "한국어", "ja": "日本語", "zh-Hans": "简体中文", "zh-Hant": "繁體中文",
              "vi": "Tiếng Việt", "es": "Español", "pt-BR": "Português (BR)", "th": "ไทย", "id": "Bahasa Indonesia"}

def C(support_title, tagline, faq, contact_h, contact_p, contact_link, privacy_link, support_link,
      privacy_title, effective, sections, changes_note):
    return dict(support_title=support_title, tagline=tagline, faq=faq, contact_h=contact_h, contact_p=contact_p,
                contact_link=contact_link, privacy_link=privacy_link, support_link=support_link,
                privacy_title=privacy_title, effective=effective, sections=sections, changes_note=changes_note)

CONTENT = {
"en": C("Threes Support", "Three 3-second clips, stacked into one vertical video diary.",
    [("How do I record?", "Tap the record button. It records for 3 seconds and stops by itself. Do that three times and your three is done. You can also pull a video or photo in from your album."),
     ("Where are my videos?", "Tap Save video on the finished screen and it goes to the Photos app as a 9:16 mp4 with no watermark. Clips are stored only on your phone."),
     ("How long are drafts kept?", "Free keeps up to 3 drafts for 14 days. Pro keeps unlimited drafts for 90 days. A finished three can be re-edited for 7 days."),
     ("What does Pro include, and how do I restore it?", "Threes Pro is a one-time purchase through Apple: every template, custom labels, every filter with strength control, unlimited drafts. To restore on another device, sign in with the same Apple ID and tap Settings → Restore purchases."),
     ("Can I use my own font?", "Yes. Add a ttf or otf file in Settings → My fonts, or with the + card at the end of the Font tab while editing."),
     ("How do I delete my data?", "Delete a three from Home, or delete the app. Everything lives on your device, so nothing remains anywhere else.")],
    "Contact", "Found a bug or have a question? Open an issue and we'll reply there.", "Open an issue on GitHub",
    "Privacy Policy", "Support",
    "Privacy Policy", f"Effective {EFFECTIVE}",
    [("In short", "Threes has no account and no server of its own. Everything you record stays on your device. We do not collect personal data."),
     ("Camera and Photos", "Threes asks for the camera to record your clips and for permission to add to Photos so it can save your finished video. Nothing is uploaded anywhere."),
     ("Data on your device", "Clips, thumbnails, drafts, fonts you add and your settings are stored only on your device. They are removed when you delete them in the app or delete the app."),
     ("Purchases", "Threes Pro is sold through Apple's In-App Purchase. Apple handles payment; we never see your payment details or Apple ID. Restoring a purchase also goes through Apple."),
     ("Network use", "The app connects to the internet only to check whether a newer version exists, by asking Apple's App Store about the app's own identifier and your store region, and possibly by fetching a small update-notice file from our hosting. No device identifiers are sent. There is no analytics SDK, no advertising and no tracking."),
     ("Sharing", "When you share a video, it is handed to the app you choose, and that app's privacy policy applies."),
     ("Children", "Threes is not directed at children under 13 and, as described above, collects no personal data from anyone."),
     ("Changes", "If this policy changes, the new version will be posted on this page with a new effective date."),
     ("Contact", f"Questions about privacy: open an issue at {ISSUES}.")],
    ""),
"ko": C("Threes 지원", "3초씩 세 컷, 세로로 이어 붙인 영상 일기.",
    [("어떻게 찍나요?", "촬영 버튼을 누르면 3초 뒤에 알아서 멈춰요. 세 번 찍으면 3컷이 완성됩니다. 앨범에 있는 영상·사진을 가져와도 돼요."),
     ("완성한 영상은 어디에 있나요?", "완성 화면에서 '영상 저장'을 누르면 워터마크 없는 9:16 mp4로 사진 앱에 들어가요. 클립은 휴대폰 안에만 저장됩니다."),
     ("작업 중인 3컷은 얼마나 보관되나요?", "무료는 3개까지 14일, Pro는 개수 제한 없이 90일이에요. 완성한 3컷은 7일 동안 다시 편집할 수 있어요."),
     ("Pro에는 뭐가 들어 있고, 복원은 어떻게 하나요?", "Threes Pro는 Apple을 통한 한 번 결제예요. 모든 템플릿, 나만의 라벨, 모든 필터와 강도 조절, 작업 중 3컷 무제한이 열립니다. 다른 기기에서는 같은 Apple ID로 로그인한 뒤 설정 → 구매 복원을 누르세요."),
     ("내 폰트를 쓸 수 있나요?", "네. 설정 → 내 폰트에서, 또는 편집 화면 폰트 탭 맨 끝의 + 카드에서 ttf·otf 파일을 넣으면 돼요."),
     ("내 데이터는 어떻게 지우나요?", "홈에서 3컷을 지우거나 앱을 삭제하면 끝이에요. 모든 데이터가 기기 안에만 있어서 다른 곳에 남는 게 없습니다.")],
    "문의", "버그나 궁금한 점은 이슈로 남겨 주세요. 거기서 답합니다.", "GitHub에 이슈 남기기",
    "개인정보 처리방침", "지원",
    "개인정보 처리방침", f"시행일 {EFFECTIVE}",
    [("요약", "Threes에는 계정도, 자체 서버도 없어요. 찍은 것은 전부 기기 안에 남고, 개인정보를 수집하지 않습니다."),
     ("카메라와 사진", "클립을 찍기 위해 카메라 권한을, 완성한 영상을 저장하기 위해 사진 추가 권한을 요청합니다. 어디에도 업로드하지 않아요."),
     ("기기 안의 데이터", "클립, 썸네일, 작업 중인 3컷, 추가한 폰트, 설정은 기기에만 저장됩니다. 앱에서 지우거나 앱을 삭제하면 함께 사라져요."),
     ("결제", "Threes Pro는 Apple 인앱 결제로 판매합니다. 결제는 Apple이 처리하고, 결제 정보나 Apple ID는 저희에게 전달되지 않아요. 구매 복원도 Apple을 통해 이뤄집니다."),
     ("네트워크 사용", "앱은 새 버전이 있는지 확인할 때만 인터넷에 연결해요. Apple App Store에 앱 식별자와 스토어 지역으로 최신 버전을 묻고, 저희 호스팅에서 작은 업데이트 안내 파일을 받아올 수 있습니다. 기기 식별자는 보내지 않고, 분석 SDK·광고·추적이 없습니다."),
     ("공유", "영상을 공유하면 선택한 앱으로 넘어가며, 그 앱의 개인정보 처리방침이 적용됩니다."),
     ("아동", "Threes는 만 13세 미만 아동을 대상으로 하지 않으며, 위와 같이 누구의 개인정보도 수집하지 않습니다."),
     ("변경", "이 방침이 바뀌면 새 시행일과 함께 이 페이지에 게시합니다."),
     ("문의", f"개인정보 관련 문의는 {ISSUES} 에 이슈로 남겨 주세요.")],
    ""),
"ja": C("Threes サポート", "3秒のクリップを3つ、縦につないだ動画日記。",
    [("どうやって撮りますか？", "録画ボタンを押すと3秒で自動的に止まります。3回撮れば3カットの完成。アルバムの動画や写真を読み込むこともできます。"),
     ("完成した動画はどこにありますか？", "完成画面で「動画を保存」を押すと、透かしのない9:16のmp4として写真アプリに保存されます。クリップはお使いの端末の中にだけ保存されます。"),
     ("作業中の3カットはどのくらい残りますか？", "無料版は3件まで14日間、Proは件数無制限で90日間です。完成した3カットは7日間、再編集できます。"),
     ("Proの内容と復元方法は？", "Threes ProはAppleを通じた買い切りです。すべてのテンプレート、自分だけのラベル、すべてのフィルターと強さ調整、作業中3カット無制限が使えます。別の端末では同じApple IDでサインインし、設定 → 購入を復元を押してください。"),
     ("自分のフォントは使えますか？", "はい。設定 → マイフォント、または編集画面のフォントタブ末尾の「+」カードから ttf・otf ファイルを追加できます。"),
     ("データを削除するには？", "ホームで3カットを削除するか、アプリを削除してください。データはすべて端末内にあるので、他の場所には何も残りません。")],
    "お問い合わせ", "不具合や質問は Issue にお書きください。そこでお返事します。", "GitHubでIssueを作成",
    "プライバシーポリシー", "サポート",
    "プライバシーポリシー", f"施行日 {EFFECTIVE}",
    [("要約", "Threesにはアカウントも独自サーバーもありません。撮影したものはすべて端末内に残り、個人情報は収集しません。"),
     ("カメラと写真", "クリップの撮影にカメラの許可を、完成した動画の保存に写真への追加の許可を求めます。どこにもアップロードしません。"),
     ("端末内のデータ", "クリップ、サムネイル、作業中の3カット、追加したフォント、設定は端末内にのみ保存されます。アプリ内で削除するか、アプリを削除すると消えます。"),
     ("購入", "Threes ProはAppleのアプリ内課金で販売しています。決済はAppleが処理し、決済情報やApple IDは当方に渡りません。購入の復元もAppleを通じて行われます。"),
     ("ネットワークの利用", "アプリがインターネットに接続するのは、新しいバージョンの確認時だけです。AppleのApp Storeにアプリの識別子とストアの地域で最新バージョンを問い合わせ、当方のホスティングから小さな更新案内ファイルを取得することがあります。端末識別子は送信しません。分析SDK・広告・トラッキングはありません。"),
     ("共有", "動画を共有すると、選択したアプリに渡され、そのアプリのプライバシーポリシーが適用されます。"),
     ("子ども", "Threesは13歳未満の子どもを対象としておらず、上記のとおり誰の個人情報も収集しません。"),
     ("変更", "本ポリシーを変更する場合は、新しい施行日とともにこのページに掲載します。"),
     ("お問い合わせ", f"プライバシーに関するご質問は {ISSUES} にIssueをお書きください。")],
    ""),
"zh-Hans": C("Threes 支持", "三段 3 秒短片，竖向拼成一支视频日记。",
    [("怎么拍？", "按下录制按钮，3 秒后自动停止。拍三次，三格就完成了。也可以从相册导入视频或照片。"),
     ("完成的视频在哪里？", "在完成页面点“保存视频”，会以无水印的 9:16 mp4 保存到照片 App。片段只保存在你的手机里。"),
     ("草稿能保留多久？", "免费版最多 3 个草稿、保留 14 天；Pro 不限数量、保留 90 天。完成的三格 7 天内可以重新编辑。"),
     ("Pro 包含什么？怎么恢复购买？", "Threes Pro 通过 Apple 一次性购买：全部模板、自定义标签、全部滤镜和强度调节、草稿不限量。换设备时，用同一个 Apple ID 登录，然后在设置 → 恢复购买。"),
     ("能用自己的字体吗？", "可以。在设置 → 我的字体，或编辑页字体标签末尾的“+”卡片添加 ttf/otf 文件。"),
     ("怎么删除我的数据？", "在首页删除三格，或直接删除 App。所有数据都只在你的设备上，别处不会留下任何东西。")],
    "联系我们", "有问题或发现 bug，请提交 issue，我们会在那里回复。", "在 GitHub 提交 issue",
    "隐私政策", "支持",
    "隐私政策", f"生效日期 {EFFECTIVE}",
    [("简要说明", "Threes 没有账号，也没有自己的服务器。你拍的一切都留在设备上，我们不收集个人数据。"),
     ("相机与照片", "拍摄片段需要相机权限，保存成片需要“添加到照片”权限。任何内容都不会被上传。"),
     ("设备上的数据", "片段、缩略图、草稿、你添加的字体和设置只保存在你的设备上。你在 App 内删除或卸载 App 后即被移除。"),
     ("购买", "Threes Pro 通过 Apple 的 App 内购买销售。付款由 Apple 处理，我们不会看到你的付款信息或 Apple ID。恢复购买同样通过 Apple 完成。"),
     ("网络使用", "App 只在检查新版本时联网：向 Apple App Store 查询本 App 的标识符和你所在的商店地区，并可能从我们的托管服务获取一个小的更新提示文件。不会发送设备标识符。没有分析 SDK、没有广告、没有跟踪。"),
     ("分享", "分享视频时，视频会交给你选择的 App，并适用该 App 的隐私政策。"),
     ("儿童", "Threes 不面向 13 岁以下儿童，且如上所述不收集任何人的个人数据。"),
     ("变更", "如本政策有变更，将在本页面发布新版本并更新生效日期。"),
     ("联系", f"隐私相关问题请在 {ISSUES} 提交 issue。")],
    ""),
"zh-Hant": C("Threes 支援", "三段 3 秒短片，直向接成一支影片日記。",
    [("怎麼拍？", "按下錄製按鈕，3 秒後自動停止。拍三次，三格就完成了。也可以從相簿匯入影片或照片。"),
     ("完成的影片在哪裡？", "在完成頁面點「儲存影片」，會以無浮水印的 9:16 mp4 儲存到照片 App。片段只保存在你的手機裡。"),
     ("草稿能保留多久？", "免費版最多 3 個草稿、保留 14 天；Pro 不限數量、保留 90 天。完成的三格 7 天內可以重新編輯。"),
     ("Pro 包含什麼？怎麼回復購買？", "Threes Pro 透過 Apple 一次性購買：全部範本、自訂標籤、全部濾鏡和強度調整、草稿不限量。換裝置時，用同一個 Apple ID 登入，然後在設定 → 回復購買。"),
     ("能用自己的字體嗎？", "可以。在設定 → 我的字體，或編輯頁字體標籤末尾的「+」卡片加入 ttf/otf 檔案。"),
     ("怎麼刪除我的資料？", "在首頁刪除三格，或直接刪除 App。所有資料都只在你的裝置上，別處不會留下任何東西。")],
    "聯絡我們", "有問題或發現 bug，請建立 issue，我們會在那裡回覆。", "在 GitHub 建立 issue",
    "隱私權政策", "支援",
    "隱私權政策", f"生效日期 {EFFECTIVE}",
    [("簡要說明", "Threes 沒有帳號，也沒有自己的伺服器。你拍的一切都留在裝置上，我們不蒐集個人資料。"),
     ("相機與照片", "拍攝片段需要相機權限，儲存成品需要「加入照片」權限。任何內容都不會被上傳。"),
     ("裝置上的資料", "片段、縮圖、草稿、你加入的字體和設定只保存在你的裝置上。你在 App 內刪除或移除 App 後即被清除。"),
     ("購買", "Threes Pro 透過 Apple 的 App 內購買販售。付款由 Apple 處理，我們不會看到你的付款資訊或 Apple ID。回復購買同樣透過 Apple 完成。"),
     ("網路使用", "App 只在檢查新版本時連網：向 Apple App Store 查詢本 App 的識別碼和你所在的商店地區，並可能從我們的主機取得一個小的更新提示檔案。不會傳送裝置識別碼。沒有分析 SDK、沒有廣告、沒有追蹤。"),
     ("分享", "分享影片時，影片會交給你選擇的 App，並適用該 App 的隱私權政策。"),
     ("兒童", "Threes 不以 13 歲以下兒童為對象，且如上所述不蒐集任何人的個人資料。"),
     ("變更", "如本政策有變更，將在本頁面發布新版本並更新生效日期。"),
     ("聯絡", f"隱私相關問題請在 {ISSUES} 建立 issue。")],
    ""),
"vi": C("Hỗ trợ Threes", "Ba clip 3 giây, xếp dọc thành một video nhật ký.",
    [("Quay như thế nào?", "Chạm nút quay, máy tự dừng sau 3 giây. Quay ba lần là xong bộ 3 cảnh. Bạn cũng có thể lấy video hoặc ảnh từ album."),
     ("Video của tôi ở đâu?", "Ở màn hình hoàn thành, chạm Lưu video: video 9:16 mp4 không watermark sẽ vào ứng dụng Ảnh. Clip chỉ được lưu trên điện thoại của bạn."),
     ("Bản nháp giữ được bao lâu?", "Bản miễn phí giữ tối đa 3 bản nháp trong 14 ngày. Pro không giới hạn, giữ 90 ngày. Bộ 3 cảnh đã hoàn thành có thể sửa lại trong 7 ngày."),
     ("Pro gồm những gì và khôi phục ra sao?", "Threes Pro là mua một lần qua Apple: mọi mẫu, nhãn tùy chỉnh, mọi bộ lọc kèm chỉnh độ mạnh, bản nháp không giới hạn. Trên thiết bị khác, đăng nhập cùng Apple ID rồi vào Cài đặt → Khôi phục mua hàng."),
     ("Dùng phông chữ riêng được không?", "Được. Thêm tệp ttf hoặc otf trong Cài đặt → Phông chữ của tôi, hoặc thẻ + ở cuối tab Phông chữ khi chỉnh sửa."),
     ("Xóa dữ liệu của tôi thế nào?", "Xóa bộ 3 cảnh ở trang chủ, hoặc xóa ứng dụng. Mọi thứ nằm trên thiết bị của bạn nên không còn gì ở nơi khác.")],
    "Liên hệ", "Gặp lỗi hoặc có câu hỏi? Hãy mở một issue, chúng tôi sẽ trả lời ở đó.", "Mở issue trên GitHub",
    "Chính sách quyền riêng tư", "Hỗ trợ",
    "Chính sách quyền riêng tư", f"Có hiệu lực từ {EFFECTIVE}",
    [("Tóm tắt", "Threes không có tài khoản và không có máy chủ riêng. Mọi thứ bạn quay đều ở trên thiết bị. Chúng tôi không thu thập dữ liệu cá nhân."),
     ("Camera và Ảnh", "Threes xin quyền camera để quay clip và quyền thêm vào Ảnh để lưu video hoàn thành. Không có gì được tải lên đâu cả."),
     ("Dữ liệu trên thiết bị", "Clip, ảnh thu nhỏ, bản nháp, phông chữ bạn thêm và cài đặt chỉ được lưu trên thiết bị. Chúng bị xóa khi bạn xóa trong ứng dụng hoặc gỡ ứng dụng."),
     ("Mua hàng", "Threes Pro được bán qua Mua trong ứng dụng của Apple. Apple xử lý thanh toán; chúng tôi không thấy thông tin thanh toán hay Apple ID của bạn. Khôi phục mua hàng cũng qua Apple."),
     ("Sử dụng mạng", "Ứng dụng chỉ kết nối internet để kiểm tra phiên bản mới: hỏi App Store của Apple bằng mã định danh của ứng dụng và khu vực cửa hàng của bạn, và có thể tải một tệp thông báo cập nhật nhỏ từ máy chủ lưu trữ của chúng tôi. Không gửi mã định danh thiết bị. Không có SDK phân tích, không quảng cáo, không theo dõi."),
     ("Chia sẻ", "Khi bạn chia sẻ video, video được chuyển cho ứng dụng bạn chọn và chính sách của ứng dụng đó sẽ áp dụng."),
     ("Trẻ em", "Threes không hướng đến trẻ em dưới 13 tuổi và, như đã nêu, không thu thập dữ liệu cá nhân của bất kỳ ai."),
     ("Thay đổi", "Nếu chính sách này thay đổi, phiên bản mới sẽ được đăng tại trang này với ngày hiệu lực mới."),
     ("Liên hệ", f"Câu hỏi về quyền riêng tư: mở issue tại {ISSUES}.")],
    ""),
"es": C("Soporte de Threes", "Tres clips de 3 segundos, apilados en un diario en video vertical.",
    [("¿Cómo grabo?", "Toca el botón de grabar. Graba 3 segundos y se detiene solo. Hazlo tres veces y tus 3 tomas están listas. También puedes traer un video o una foto de tu álbum."),
     ("¿Dónde están mis videos?", "En la pantalla final toca Guardar video y se guarda en Fotos como mp4 9:16 sin marca de agua. Los clips solo se guardan en tu teléfono."),
     ("¿Cuánto tiempo se guardan los borradores?", "La versión gratis guarda hasta 3 borradores durante 14 días. Pro guarda borradores ilimitados durante 90 días. Unas 3 tomas terminadas se pueden volver a editar durante 7 días."),
     ("¿Qué incluye Pro y cómo lo restauro?", "Threes Pro es una compra única a través de Apple: todas las plantillas, etiquetas propias, todos los filtros con intensidad y borradores ilimitados. En otro dispositivo, inicia sesión con el mismo Apple ID y toca Ajustes → Restaurar compras."),
     ("¿Puedo usar mi propia fuente?", "Sí. Añade un archivo ttf u otf en Ajustes → Mis fuentes, o con la tarjeta + al final de la pestaña Fuente al editar."),
     ("¿Cómo borro mis datos?", "Elimina unas 3 tomas desde Inicio o elimina la app. Todo vive en tu dispositivo, así que no queda nada en ningún otro sitio.")],
    "Contacto", "¿Un error o una duda? Abre un issue y te respondemos ahí.", "Abrir un issue en GitHub",
    "Política de privacidad", "Soporte",
    "Política de privacidad", f"Vigente desde el {EFFECTIVE}",
    [("En resumen", "Threes no tiene cuenta ni servidor propio. Todo lo que grabas se queda en tu dispositivo. No recopilamos datos personales."),
     ("Cámara y Fotos", "Threes pide la cámara para grabar tus clips y permiso para añadir a Fotos para guardar el video terminado. No se sube nada a ningún sitio."),
     ("Datos en tu dispositivo", "Los clips, miniaturas, borradores, fuentes que añades y ajustes se guardan solo en tu dispositivo. Se eliminan cuando los borras en la app o eliminas la app."),
     ("Compras", "Threes Pro se vende mediante la compra dentro de la app de Apple. Apple gestiona el pago; nunca vemos tus datos de pago ni tu Apple ID. Restaurar una compra también pasa por Apple."),
     ("Uso de red", "La app se conecta a internet solo para comprobar si hay una versión nueva: consulta al App Store de Apple con el identificador de la app y tu región de tienda, y puede descargar un pequeño archivo de aviso de actualización desde nuestro alojamiento. No se envían identificadores del dispositivo. No hay SDK de analítica, ni publicidad, ni rastreo."),
     ("Compartir", "Cuando compartes un video, se entrega a la app que elijas y se aplica la política de privacidad de esa app."),
     ("Menores", "Threes no está dirigida a menores de 13 años y, como se indica arriba, no recopila datos personales de nadie."),
     ("Cambios", "Si esta política cambia, la nueva versión se publicará en esta página con una nueva fecha de vigencia."),
     ("Contacto", f"Preguntas sobre privacidad: abre un issue en {ISSUES}.")],
    ""),
"pt-BR": C("Suporte do Threes", "Três clipes de 3 segundos, empilhados em um diário em vídeo vertical.",
    [("Como eu gravo?", "Toque no botão de gravar. Ele grava 3 segundos e para sozinho. Faça isso três vezes e suas 3 cenas estão prontas. Você também pode puxar um vídeo ou foto do seu álbum."),
     ("Onde estão meus vídeos?", "Na tela final, toque em Salvar vídeo e ele vai para o app Fotos como mp4 9:16 sem marca d'água. Os clipes ficam só no seu celular."),
     ("Por quanto tempo os rascunhos ficam guardados?", "A versão grátis guarda até 3 rascunhos por 14 dias. O Pro guarda rascunhos ilimitados por 90 dias. Uma cena tripla concluída pode ser reeditada por 7 dias."),
     ("O que o Pro inclui e como restauro?", "O Threes Pro é uma compra única pela Apple: todos os modelos, textos personalizados, todos os filtros com intensidade e rascunhos ilimitados. Em outro aparelho, entre com o mesmo Apple ID e toque em Ajustes → Restaurar compras."),
     ("Posso usar minha própria fonte?", "Sim. Adicione um arquivo ttf ou otf em Ajustes → Minhas fontes, ou pelo cartão + no fim da aba Fonte ao editar."),
     ("Como apago meus dados?", "Exclua as 3 cenas no Início ou exclua o app. Tudo fica no seu aparelho, então não sobra nada em outro lugar.")],
    "Contato", "Achou um bug ou tem uma dúvida? Abra um issue e respondemos por lá.", "Abrir um issue no GitHub",
    "Política de privacidade", "Suporte",
    "Política de privacidade", f"Em vigor desde {EFFECTIVE}",
    [("Resumo", "O Threes não tem conta nem servidor próprio. Tudo o que você grava fica no seu aparelho. Não coletamos dados pessoais."),
     ("Câmera e Fotos", "O Threes pede a câmera para gravar seus clipes e permissão para adicionar a Fotos para salvar o vídeo pronto. Nada é enviado para lugar nenhum."),
     ("Dados no seu aparelho", "Clipes, miniaturas, rascunhos, fontes que você adiciona e ajustes ficam só no seu aparelho. São removidos quando você os exclui no app ou exclui o app."),
     ("Compras", "O Threes Pro é vendido pela compra no app da Apple. A Apple processa o pagamento; nunca vemos seus dados de pagamento nem seu Apple ID. Restaurar uma compra também passa pela Apple."),
     ("Uso de rede", "O app se conecta à internet só para verificar se há uma versão nova: consulta a App Store da Apple com o identificador do app e sua região de loja, e pode baixar um pequeno arquivo de aviso de atualização da nossa hospedagem. Nenhum identificador do aparelho é enviado. Não há SDK de análise, publicidade nem rastreamento."),
     ("Compartilhamento", "Quando você compartilha um vídeo, ele é entregue ao app que você escolher, e a política de privacidade desse app se aplica."),
     ("Crianças", "O Threes não é dirigido a menores de 13 anos e, como descrito acima, não coleta dados pessoais de ninguém."),
     ("Alterações", "Se esta política mudar, a nova versão será publicada nesta página com uma nova data de vigência."),
     ("Contato", f"Dúvidas sobre privacidade: abra um issue em {ISSUES}.")],
    ""),
"th": C("ฝ่ายสนับสนุน Threes", "3 คลิป คลิปละ 3 วินาที ต่อกันแนวตั้งเป็นวิดีโอไดอารี่",
    [("ถ่ายอย่างไร?", "แตะปุ่มถ่าย เครื่องจะถ่าย 3 วินาทีแล้วหยุดเอง ถ่าย 3 ครั้งก็ครบชุด หรือจะนำเข้าวิดีโอและรูปจากอัลบั้มก็ได้"),
     ("วิดีโอของฉันอยู่ที่ไหน?", "ที่หน้าเสร็จสิ้น แตะ “บันทึกวิดีโอ” ไฟล์ mp4 9:16 ไม่มีลายน้ำจะเข้าไปในแอปรูปภาพ คลิปถูกเก็บไว้ในเครื่องของคุณเท่านั้น"),
     ("ฉบับร่างเก็บได้นานแค่ไหน?", "แบบฟรีเก็บได้ 3 ชุด นาน 14 วัน Pro เก็บได้ไม่จำกัด นาน 90 วัน ชุดที่เสร็จแล้วแก้ไขซ้ำได้ภายใน 7 วัน"),
     ("Pro มีอะไรบ้าง และกู้คืนอย่างไร?", "Threes Pro เป็นการซื้อครั้งเดียวผ่าน Apple: ทุกเทมเพลต ป้ายกำหนดเอง ทุกฟิลเตอร์พร้อมปรับความแรง และฉบับร่างไม่จำกัด บนเครื่องอื่น ให้ลงชื่อเข้าใช้ Apple ID เดิมแล้วไปที่ การตั้งค่า → กู้คืนการซื้อ"),
     ("ใช้ฟอนต์ของตัวเองได้ไหม?", "ได้ เพิ่มไฟล์ ttf หรือ otf ที่ การตั้งค่า → ฟอนต์ของฉัน หรือการ์ด + ท้ายแท็บฟอนต์ตอนแก้ไข"),
     ("ลบข้อมูลของฉันอย่างไร?", "ลบชุดคลิปที่หน้าแรก หรือลบแอป ข้อมูลทั้งหมดอยู่ในเครื่องของคุณ จึงไม่มีอะไรเหลืออยู่ที่อื่น")],
    "ติดต่อ", "พบบั๊กหรือมีคำถาม? เปิด issue ไว้ได้เลย เราจะตอบที่นั่น", "เปิด issue บน GitHub",
    "นโยบายความเป็นส่วนตัว", "ฝ่ายสนับสนุน",
    "นโยบายความเป็นส่วนตัว", f"มีผลตั้งแต่ {EFFECTIVE}",
    [("สรุป", "Threes ไม่มีบัญชีผู้ใช้และไม่มีเซิร์ฟเวอร์ของตัวเอง ทุกอย่างที่คุณถ่ายอยู่ในเครื่องของคุณ เราไม่เก็บข้อมูลส่วนบุคคล"),
     ("กล้องและรูปภาพ", "Threes ขอสิทธิ์กล้องเพื่อถ่ายคลิป และสิทธิ์เพิ่มลงรูปภาพเพื่อบันทึกวิดีโอที่เสร็จแล้ว ไม่มีการอัปโหลดไปที่ใด"),
     ("ข้อมูลในเครื่อง", "คลิป ภาพย่อ ฉบับร่าง ฟอนต์ที่คุณเพิ่ม และการตั้งค่า ถูกเก็บไว้ในเครื่องเท่านั้น และจะหายไปเมื่อคุณลบในแอปหรือลบแอป"),
     ("การซื้อ", "Threes Pro ขายผ่านการซื้อภายในแอปของ Apple โดย Apple เป็นผู้จัดการการชำระเงิน เราไม่เห็นข้อมูลการชำระเงินหรือ Apple ID ของคุณ การกู้คืนการซื้อก็ผ่าน Apple เช่นกัน"),
     ("การใช้เครือข่าย", "แอปเชื่อมต่ออินเทอร์เน็ตเฉพาะตอนตรวจสอบเวอร์ชันใหม่ โดยสอบถาม App Store ของ Apple ด้วยตัวระบุของแอปและภูมิภาคของสโตร์ และอาจดึงไฟล์แจ้งเตือนอัปเดตขนาดเล็กจากโฮสติ้งของเรา ไม่มีการส่งตัวระบุอุปกรณ์ ไม่มี SDK วิเคราะห์ ไม่มีโฆษณา ไม่มีการติดตาม"),
     ("การแชร์", "เมื่อคุณแชร์วิดีโอ วิดีโอจะถูกส่งให้แอปที่คุณเลือก และนโยบายความเป็นส่วนตัวของแอปนั้นจะมีผล"),
     ("เด็ก", "Threes ไม่ได้มุ่งเป้าไปที่เด็กอายุต่ำกว่า 13 ปี และดังที่กล่าวข้างต้น ไม่เก็บข้อมูลส่วนบุคคลของใครทั้งสิ้น"),
     ("การเปลี่ยนแปลง", "หากนโยบายนี้เปลี่ยน เวอร์ชันใหม่จะถูกโพสต์ในหน้านี้พร้อมวันที่มีผลใหม่"),
     ("ติดต่อ", f"คำถามเรื่องความเป็นส่วนตัว: เปิด issue ได้ที่ {ISSUES}")],
    ""),
"id": C("Dukungan Threes", "Tiga klip 3 detik, ditumpuk jadi satu diary video vertikal.",
    [("Bagaimana cara merekam?", "Ketuk tombol rekam. Aplikasi merekam 3 detik lalu berhenti sendiri. Lakukan tiga kali dan 3 klipmu selesai. Kamu juga bisa mengambil video atau foto dari album."),
     ("Di mana video saya?", "Di layar selesai, ketuk Simpan video dan video masuk ke aplikasi Foto sebagai mp4 9:16 tanpa watermark. Klip hanya tersimpan di ponselmu."),
     ("Berapa lama draf disimpan?", "Versi gratis menyimpan maksimal 3 draf selama 14 hari. Pro menyimpan draf tanpa batas selama 90 hari. 3 klip yang selesai bisa diedit ulang selama 7 hari."),
     ("Apa isi Pro dan cara memulihkannya?", "Threes Pro adalah pembelian sekali lewat Apple: semua templat, label kustom, semua filter dengan pengaturan kekuatan, dan draf tanpa batas. Di perangkat lain, masuk dengan Apple ID yang sama lalu ketuk Pengaturan → Pulihkan pembelian."),
     ("Bisa pakai font sendiri?", "Bisa. Tambahkan file ttf atau otf di Pengaturan → Font saya, atau lewat kartu + di ujung tab Font saat mengedit."),
     ("Bagaimana cara menghapus data saya?", "Hapus 3 klip dari Beranda, atau hapus aplikasinya. Semua ada di perangkatmu, jadi tidak ada yang tersisa di tempat lain.")],
    "Kontak", "Menemukan bug atau punya pertanyaan? Buka issue, kami balas di sana.", "Buka issue di GitHub",
    "Kebijakan Privasi", "Dukungan",
    "Kebijakan Privasi", f"Berlaku sejak {EFFECTIVE}",
    [("Singkatnya", "Threes tidak punya akun dan tidak punya server sendiri. Semua yang kamu rekam tetap di perangkatmu. Kami tidak mengumpulkan data pribadi."),
     ("Kamera dan Foto", "Threes meminta akses kamera untuk merekam klip dan izin menambahkan ke Foto untuk menyimpan video yang selesai. Tidak ada yang diunggah ke mana pun."),
     ("Data di perangkatmu", "Klip, thumbnail, draf, font yang kamu tambahkan, dan pengaturan hanya tersimpan di perangkatmu. Semuanya terhapus saat kamu menghapusnya di aplikasi atau menghapus aplikasi."),
     ("Pembelian", "Threes Pro dijual lewat Pembelian Dalam Aplikasi Apple. Apple yang memproses pembayaran; kami tidak pernah melihat data pembayaran atau Apple ID-mu. Pemulihan pembelian juga lewat Apple."),
     ("Penggunaan jaringan", "Aplikasi terhubung ke internet hanya untuk memeriksa versi baru: menanyakan App Store Apple dengan pengenal aplikasi dan wilayah toko-mu, dan mungkin mengambil file pemberitahuan pembaruan kecil dari hosting kami. Tidak ada pengenal perangkat yang dikirim. Tidak ada SDK analitik, iklan, maupun pelacakan."),
     ("Berbagi", "Saat kamu membagikan video, video diserahkan ke aplikasi yang kamu pilih, dan kebijakan privasi aplikasi itu yang berlaku."),
     ("Anak-anak", "Threes tidak ditujukan untuk anak di bawah 13 tahun dan, seperti dijelaskan di atas, tidak mengumpulkan data pribadi siapa pun."),
     ("Perubahan", "Jika kebijakan ini berubah, versi baru akan dipasang di halaman ini dengan tanggal berlaku baru."),
     ("Kontak", f"Pertanyaan tentang privasi: buka issue di {ISSUES}.")],
    ""),
}

CSS = """
:root{--paper:#FAFAF8;--card:#F0EFEC;--line:#D9D6CF;--ink:#2B2926;--soft:#6F6B64;--faint:#A9A49B;--pink:#F58BB4;--butter:#F7E08A}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.65 -apple-system,BlinkMacSystemFont,"Pretendard","Apple SD Gothic Neo","Hiragino Sans","PingFang SC","PingFang TC","Thonburi","Segoe UI",Roboto,sans-serif}
main{max-width:680px;margin:0 auto;padding:40px 20px 80px}
.brand{font-weight:800;font-size:28px;letter-spacing:-.02em;text-decoration:none;color:var(--ink)}
.brand span{display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--pink);margin-left:6px;vertical-align:middle}
nav{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:36px}
nav a{color:var(--soft);text-decoration:none;font-size:15px}nav a:hover{color:var(--ink)}
select{font:inherit;font-size:14px;color:var(--soft);background:var(--card);border:1px solid var(--line);border-radius:10px;padding:6px 10px}
h1{font-size:34px;line-height:1.2;letter-spacing:-.02em;margin:0 0 8px}
.tag{color:var(--soft);margin:0 0 32px}.eff{color:var(--faint);font-size:14px;margin:0 0 32px}
h2{font-size:19px;margin:32px 0 6px}p{margin:0 0 12px}
details{background:var(--card);border-radius:14px;padding:14px 18px;margin:10px 0}summary{font-weight:600;cursor:pointer}details p{margin:10px 0 2px;color:var(--soft)}
.btn{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;padding:12px 18px;border-radius:999px;font-weight:600;margin-top:6px}
footer{margin-top:56px;color:var(--faint);font-size:14px}footer a{color:var(--soft)}
mark{background:var(--butter);padding:0 4px;border-radius:4px}
"""

def switcher(lang, page):
    opts = "".join(f'<option value="{code}"{" selected" if code == lang else ""}>{name}</option>' for code, name in LANG_NAMES.items())
    return f'<select onchange="location.href=\'../\'+this.value+\'/{page}\'" aria-label="Language">{opts}</select>'

def shell(lang, title, page, body, other_link):
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · Threes</title><style>{CSS}</style></head>
<body><main>
<nav><a class="brand" href="./">Threes<span></span></a><div>{other_link} &nbsp; {switcher(lang, page)}</div></nav>
{body}
<footer>Threes · <a href="{APP_STORE}">App Store</a> · <a href="https://github.com/ohtt-iOS/Threes-public">GitHub</a></footer>
</main></body></html>
"""

def support_page(lang, c):
    faq = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in c["faq"])
    body = f"""<h1>{html.escape(c['support_title'])}</h1><p class="tag">{html.escape(c['tagline'])}</p>
{faq}
<h2>{html.escape(c['contact_h'])}</h2><p>{html.escape(c['contact_p'])}</p>
<a class="btn" href="{ISSUES}">{html.escape(c['contact_link'])}</a>"""
    return shell(lang, c["support_title"], "index.html", body, f'<a href="privacy.html">{html.escape(c["privacy_link"])}</a>')

def privacy_page(lang, c):
    secs = "".join(f"<h2>{html.escape(h)}</h2><p>{html.escape(p).replace(html.escape(ISSUES), f'<a href={chr(34)}{ISSUES}{chr(34)}>{ISSUES}</a>')}</p>" for h, p in c["sections"])
    body = f"""<h1>{html.escape(c['privacy_title'])}</h1><p class="eff">{html.escape(c['effective'])}</p>{secs}"""
    return shell(lang, c["privacy_title"], "privacy.html", body, f'<a href="./">{html.escape(c["support_link"])}</a>')

def redirect_page(page):
    codes = list(LANG_NAMES)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Threes</title><meta http-equiv="refresh" content="1;url=en/{page}">
<script>
var langs={codes!r};var want=(navigator.languages||[navigator.language||'en']).map(function(l){{return l.toLowerCase()}});
var pick='en';outer:for(var i=0;i<want.length;i++){{var w=want[i];
 if(w.indexOf('zh')===0){{pick=(w.indexOf('hant')>-1||w.indexOf('tw')>-1||w.indexOf('hk')>-1||w.indexOf('mo')>-1)?'zh-Hant':'zh-Hans';break}}
 if(w.indexOf('pt')===0){{pick='pt-BR';break}}
 for(var j=0;j<langs.length;j++){{if(w===langs[j].toLowerCase()||w.split('-')[0]===langs[j].toLowerCase()){{pick=langs[j];break outer}}}}}}
location.replace(pick+'/{page}');
</script></head><body><a href="en/{page}">Threes</a></body></html>
"""

if __name__ == "__main__":
    for lang, c in CONTENT.items():
        d = ROOT / lang; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(support_page(lang, c), encoding="utf-8")
        (d / "privacy.html").write_text(privacy_page(lang, c), encoding="utf-8")
    (ROOT / "index.html").write_text(redirect_page("index.html"), encoding="utf-8")
    (ROOT / "privacy.html").write_text(redirect_page("privacy.html"), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("")
    print("built:", ", ".join(CONTENT))
