import os
import shutil

from glob import glob


class TextToMd:

    def __init__(self):
        self.input_dir = os.path.abspath('../input')
        self.output_dir = os.path.abspath('../output')

    def convert_all(self) -> None:
        """inputディレクトリ内の全txtファイルを変換する
        """
        self.clear_output_dir()
        target_paths = self.get_target_list()

        for path in target_paths:
            self.convert_to_md(path)

    def convert_to_md(self, path: str) -> None:
        """txtファイルをmdファイルへ変換する
            Args:
                path (str): 対象txtファイルの絶対パス
        """
        # 変換対象の中身を取得
        txt_filename = os.path.basename(path)
        with open(path, 'r', encoding='UTF-8') as txt_org:

            # 改行を{ 半角スペース2つ + 改行 }に変換
            txt_converted = txt_org.read().replace('\n', '  \n')

            # mdファイルを生成
            md_filename = txt_filename.replace('.txt', '.md')
            md = open(f'{self.output_dir}/{md_filename}', 'w', encoding='UTF-8')
            md.write(txt_converted)

            print(f'[INFO]converted ===> output/{md_filename}')
            md.close()

    def get_target_list(self) -> list:
        """対象ファイルの一覧を取得する
            Returns:
                (list): 対象ファイルの一覧
        """
        return glob(f'{self.input_dir}/*.txt')

    def clear_output_dir(self) -> None:
        """フォルダの中身を空にする
        """
        shutil.rmtree(self.output_dir)
        os.mkdir(self.output_dir)


if __name__ == '__main__':
    ttm = TextToMd()
    ttm.convert_all()
