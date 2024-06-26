# Day of the week #

* 作者: Abdel, Noelia.

このアドオンで選択された日付の曜日がわかります。

NVDAツールメニューに、"Day of the week"というサブメニューが加わり、2つの項目を含みます:

* 1つめの名前は"日付を検索"で、3つのコントロールを含むダイアログが開きます:

    * 日付を選択または入力するリストボックス;
    * "OKボタン" 選択した日を含むメッセージボックスを表示;
    * "Cancelボタン"ダイアログを閉じる。

* 2つめの名前は"dayOfTheWeekアドオン設定"で、日付フィールドのラベルが報告された方が良いどうか記述するアドオンのパラメータを開きます。次のような要素を含みます:

    * 日付セレクタのアクセシビリティを有効にします;
    * ラベルの通知のレベル、次の3つの選択肢があります:

        * 長い (初期に選択されています);
        * 短い (短い通知);
        * オフ (ラベルの通知を無効にします)。

    * 縦に移動している時は、現在の日付フィールドの値のみの通知を有効にします;
    * 設定を保存する"OK"ボタン;
    * ダイアログをキャンセルして閉じる"Cancel"ボタン。

## 備考 ##

* Escapeキーを押すだけでダイアログを閉じることが出来ます;
* これらのダイアログを開くショートカットキーを"入力ジェスチャー"メニュー、より詳細には、"Day of the
  week"カテゴリにて、割り当てられます;
* If you use NVDA
  2018.2以降を使用している場合、日付を検索するツールメニューには一つの項目しかありません。アドオン設定は、NVDA設定パネルにあります。

## 互換性 ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240326.0.0

* Updated compatibility for nvda-2024.1.;
* Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231015.0.0 ##

* Fixed a bug detected when navigating with up arrow from the date picker in
  the latest versions of NVDA.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## 19.2の変更点 ##

* バージョンの番号をYY.MM(年2桁、ドット、月2桁)を使用するように変更しました;
* NVDA 2019.1から現れる、新しいアドオンのバージョンフォーマットとの互換性を追加しました。

## 6.0の変更点 ##

* NVDA 2018.2以降のため、アドオン設定をNVDA設定パネルに追加しました;
* ツールメニューに日付を検索する項目を移動しました;
* 設定パネルを含む2018.2より前のNVDA バージョンについて、アドオンの後方互換性を追加しました。

## 5.0の変更点 ##

* wxPython 4.0およびPython 3とのアドオンの互換性を追加しました;
* non-ASCII文字を含むアドオンパスについてのバグを修正しました。

## 4.0の変更点 ##

* アドオンは、ユーザーが選択出来る、全ての地域の日付フォーマットを認識出来るようになりました;
* gui.guiHelperを含んでいる2016.4より前のNVDA バージョンとの、アドオンの後方互換性を追加しました。

## 3.1の変更点 ##

* より多くの言語を認識可能なため、曜日を以前のフォーマットに戻しました;
* 3つのフィールド'日', '月', '年'の認識と、それらのそれぞれの値について、日付セレクタのアクセシビリティを改善しました;
* 曜日の認識のための、Georgian言語の統合の技術を追加しました;
* 日付セレクタのアクセシビリティを有効にする、または無効にする設定ダイアログボックスを追加しました;
* アドオンサブメニューを"ツール"から"設定"に移動しました;
* アドオンカテゴリを"Day of the week"に変更しました。.

## 2.0の変更点 ##

* 日付を尋ねるダイアログの正しい外見を確保するために、gui.guiHelperモジュールを使用しました;
* アドオンにGPLライセンスを追加しました;
* アドオンが異なる言語で適切に働くように、曜日が翻訳されました;
* エンコードエラーを避けるために、日付フォーマットを変更しました。

## 1.0の変更点 ##

* 最初のバージョン。

[[!tag dev stable]]
