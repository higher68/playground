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