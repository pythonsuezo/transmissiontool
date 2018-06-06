# transmissiontool
telnetとserial(RS232c)通信が出来るツールです。

transmissiontool.py と teraframe.py を同じフォルダに置いてください。
transmissiontool.pyを起動すると通信アプリが起動します。

ローカルでtelnet通信テストを行う用にechoserver.pyを用意しました。
HOST: localhost , port: 50007
で繋がります。
サーバーへ送信した文字列をそのまま返してくれます。

起動に必要な外部ライブラリ
・wxpython
・pyserial

制作者
suezo

HP
http://blog.livedoor.jp/pythonsuezo/
