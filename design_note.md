# デザインパターン

## 3章

### 概要 
- スーパークラスで処理する内容の大枠だけ決めておくパターン
### 具体例
スーパークラスで
AbstractDisplayの持つメソッドをopen, print, close, displayとして
displayはopen, print, closeを使うものとして実装しておく
そのほかは抽象メソッドとして定義しておいて、サブクラスで実装
例えばCharDisplayの場合には、
- openに<<表示、
- printにコンストラクタで与えた1文字を与える実装
- closeに>>を表示
とするみたいな実装で
StringDisplayだったら
- openで+---+表示
- printでコンストラクタで与えた文字を|と|で挟んで表示
- closeで+---+表示
みたいにするって感じ

### その他情報
#### メリット
- ロジックの共通化してるので、バグが見つかった際に一個のスーパークラスだけ直せばいい。逆にコピペだといっぱい直す
- 上は逆に、サブクラスがメソッドを実装する責任が生じているとも言えるので、責任をsuper classから分離できる
    - subclass responsibility
#### 適用できる場合
- スーパークラスのソースがわかる場合
- AbstractDisplay型の変数に代入して使えるように実装する・・・・LSP
- 呼び出し元は抽象クラスとして扱えるように


## 5章

### 概要
- singletonパターンはインスタンスが絶対に1個しか存在しないことを保証したいパターン
### 具体例
- Singletonクラス
    - newして新しく作れないようにする → コンストラクタはプライベート・・・コンストラクタが呼び出せないので、クラスの外でnewをしたら失敗する
    - 上の代わりに、クラス変数としてsingletonインスタンスを作成する
    - getterでインスタンスは手に入れる

### その他情報
#### メリット
- 複数のインスタンスが影響して複雑な挙動をするのを排除し、その条件下でプログラミングできる
    - 制限を与えるが、同時に条件を増やしているとも言える
#### etc
- インスタンスの生成は、getInstanceを呼び出した時に行われている。
    - より正確には、getInstance呼ぶ、Singletonクラスが初期化される
    - staticフィールドが初期化される唯一のインスタンスが作られる



# abstructfactory
## abstructfactoryパターン
- 抽象的・・・具体的な実装には着目せずにインターフェースのみに注目する
- apiだけを使って部品を組み立て製品にまとめる
- 具体的な実装はサブクラスのレベルで
- まとめ
    - 抽象的な部品(インターフェース)を組み合わせて抽象的な製品を作る

## 仕様
- factory package：抽象
- 無名：main
- listfa：具象

## 実装
### item
- linkとtrayのスーパークラス
### link
- itemのサブクラスの一つ
- ハイパーリンクを表現
### tray
- link、trayを集めるクラス
- itemのサブクラスの一つ
### page
- pageと同階層のクラス
- itemを部品とすると製品を表す

### factory
- 工場
- 工場のインスタンスを作るメソッド
- 部品と製品を作るメソッドを持つ
- getFactoryは具象クラスを動的に読み込み、インスタンスを作成する

### main
- 具体的な名前を一切使っていない。これが利点


具象クラス
### listfactory
- 部品、製品はnewするよう実装
- prototypeでcloneしてもよい
### listlink
- makeHtmlを実装しただけ
### listtray
- superに定義したlistのtrayを、使ってそれぞれのitemでループ
- itemクラスとして扱ってmakehtmlするのが大事

listpage
- contentイテレータを使ってループ
- htmlを作ってる

具象をもう一個（再利用性を強調したいのだろう）
tablefactory
- 

## その他
- 抽象的・・・具体的な実装には着目せずにインターフェースのみに注目している
- 
#### メリット
- 具体的な工場の追加は簡単
- つまり、何を実装すればいいか明確なので、仕様が把握しやすい
- 
#### デメリット
- 部品の追加は困難
- 存在する工場全てに修正が入るのでめんどい：継承の層が深くて種類の幅が広いからだろうなあ

