// Generated from d:/GitHub/CSC615M-Abstract-Machine-Interpreter/automata/AbstractMachineLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class AbstractMachineLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DATA=1, STACK=2, QUEUE=3, TAPE=4, TAPE_2D=5, LOGIC=6, SCAN=7, PRINT=8, 
		SCAN_RIGHT=9, SCAN_LEFT=10, READ=11, WRITE=12, RIGHT=13, LEFT=14, UP=15, 
		DOWN=16, COMMA=17, CLOSE_BRACKET=18, OPEN_PAR=19, CLOSE_PAR=20, SLASH=21, 
		SYMBOL=22, IDENTIFIER=23, COMMENT=24, WS=25;
	public static final int
		ERRORS=2;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN", "ERRORS"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DATA", "STACK", "QUEUE", "TAPE", "TAPE_2D", "LOGIC", "SCAN", "PRINT", 
			"SCAN_RIGHT", "SCAN_LEFT", "READ", "WRITE", "RIGHT", "LEFT", "UP", "DOWN", 
			"COMMA", "CLOSE_BRACKET", "OPEN_PAR", "CLOSE_PAR", "SLASH", "SYMBOL", 
			"IDENTIFIER", "COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.DATA'", "'STACK'", "'QUEUE'", "'TAPE'", "'2D_TAPE'", "'.LOGIC'", 
			"'SCAN'", "'PRINT'", "'SCAN RIGHT'", "'SCAN LEFT'", "'READ'", "'WRITE'", 
			"'RIGHT'", "'LEFT'", "'UP'", "'DOWN'", "','", "']'", "'('", "')'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "DATA", "STACK", "QUEUE", "TAPE", "TAPE_2D", "LOGIC", "SCAN", "PRINT", 
			"SCAN_RIGHT", "SCAN_LEFT", "READ", "WRITE", "RIGHT", "LEFT", "UP", "DOWN", 
			"COMMA", "CLOSE_BRACKET", "OPEN_PAR", "CLOSE_PAR", "SLASH", "SYMBOL", 
			"IDENTIFIER", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public AbstractMachineLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "AbstractMachineLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0019\u00be\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0016\u0001\u0016\u0005\u0016\u00a6\b\u0016\n\u0016\f\u0016\u00a9\t\u0016"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u00af\b\u0017"+
		"\n\u0017\f\u0017\u00b2\t\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0018\u0004\u0018\u00b9\b\u0018\u000b\u0018\f\u0018\u00ba"+
		"\u0001\u0018\u0001\u0018\u0001\u00b0\u0000\u0019\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013"+
		"\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/\u00181\u0019\u0001\u0000"+
		"\u0004\u0004\u0000#$09AZaz\u0002\u0000AZaz\u0004\u000009AZ__az\u0003\u0000"+
		"\t\n\r\r  \u00c0\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000"+
		"\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000"+
		"%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0001"+
		"3\u0001\u0000\u0000\u0000\u00039\u0001\u0000\u0000\u0000\u0005?\u0001"+
		"\u0000\u0000\u0000\u0007E\u0001\u0000\u0000\u0000\tJ\u0001\u0000\u0000"+
		"\u0000\u000bR\u0001\u0000\u0000\u0000\rY\u0001\u0000\u0000\u0000\u000f"+
		"^\u0001\u0000\u0000\u0000\u0011d\u0001\u0000\u0000\u0000\u0013o\u0001"+
		"\u0000\u0000\u0000\u0015y\u0001\u0000\u0000\u0000\u0017~\u0001\u0000\u0000"+
		"\u0000\u0019\u0084\u0001\u0000\u0000\u0000\u001b\u008a\u0001\u0000\u0000"+
		"\u0000\u001d\u008f\u0001\u0000\u0000\u0000\u001f\u0092\u0001\u0000\u0000"+
		"\u0000!\u0097\u0001\u0000\u0000\u0000#\u0099\u0001\u0000\u0000\u0000%"+
		"\u009b\u0001\u0000\u0000\u0000\'\u009d\u0001\u0000\u0000\u0000)\u009f"+
		"\u0001\u0000\u0000\u0000+\u00a1\u0001\u0000\u0000\u0000-\u00a3\u0001\u0000"+
		"\u0000\u0000/\u00aa\u0001\u0000\u0000\u00001\u00b8\u0001\u0000\u0000\u0000"+
		"34\u0005.\u0000\u000045\u0005D\u0000\u000056\u0005A\u0000\u000067\u0005"+
		"T\u0000\u000078\u0005A\u0000\u00008\u0002\u0001\u0000\u0000\u00009:\u0005"+
		"S\u0000\u0000:;\u0005T\u0000\u0000;<\u0005A\u0000\u0000<=\u0005C\u0000"+
		"\u0000=>\u0005K\u0000\u0000>\u0004\u0001\u0000\u0000\u0000?@\u0005Q\u0000"+
		"\u0000@A\u0005U\u0000\u0000AB\u0005E\u0000\u0000BC\u0005U\u0000\u0000"+
		"CD\u0005E\u0000\u0000D\u0006\u0001\u0000\u0000\u0000EF\u0005T\u0000\u0000"+
		"FG\u0005A\u0000\u0000GH\u0005P\u0000\u0000HI\u0005E\u0000\u0000I\b\u0001"+
		"\u0000\u0000\u0000JK\u00052\u0000\u0000KL\u0005D\u0000\u0000LM\u0005_"+
		"\u0000\u0000MN\u0005T\u0000\u0000NO\u0005A\u0000\u0000OP\u0005P\u0000"+
		"\u0000PQ\u0005E\u0000\u0000Q\n\u0001\u0000\u0000\u0000RS\u0005.\u0000"+
		"\u0000ST\u0005L\u0000\u0000TU\u0005O\u0000\u0000UV\u0005G\u0000\u0000"+
		"VW\u0005I\u0000\u0000WX\u0005C\u0000\u0000X\f\u0001\u0000\u0000\u0000"+
		"YZ\u0005S\u0000\u0000Z[\u0005C\u0000\u0000[\\\u0005A\u0000\u0000\\]\u0005"+
		"N\u0000\u0000]\u000e\u0001\u0000\u0000\u0000^_\u0005P\u0000\u0000_`\u0005"+
		"R\u0000\u0000`a\u0005I\u0000\u0000ab\u0005N\u0000\u0000bc\u0005T\u0000"+
		"\u0000c\u0010\u0001\u0000\u0000\u0000de\u0005S\u0000\u0000ef\u0005C\u0000"+
		"\u0000fg\u0005A\u0000\u0000gh\u0005N\u0000\u0000hi\u0005 \u0000\u0000"+
		"ij\u0005R\u0000\u0000jk\u0005I\u0000\u0000kl\u0005G\u0000\u0000lm\u0005"+
		"H\u0000\u0000mn\u0005T\u0000\u0000n\u0012\u0001\u0000\u0000\u0000op\u0005"+
		"S\u0000\u0000pq\u0005C\u0000\u0000qr\u0005A\u0000\u0000rs\u0005N\u0000"+
		"\u0000st\u0005 \u0000\u0000tu\u0005L\u0000\u0000uv\u0005E\u0000\u0000"+
		"vw\u0005F\u0000\u0000wx\u0005T\u0000\u0000x\u0014\u0001\u0000\u0000\u0000"+
		"yz\u0005R\u0000\u0000z{\u0005E\u0000\u0000{|\u0005A\u0000\u0000|}\u0005"+
		"D\u0000\u0000}\u0016\u0001\u0000\u0000\u0000~\u007f\u0005W\u0000\u0000"+
		"\u007f\u0080\u0005R\u0000\u0000\u0080\u0081\u0005I\u0000\u0000\u0081\u0082"+
		"\u0005T\u0000\u0000\u0082\u0083\u0005E\u0000\u0000\u0083\u0018\u0001\u0000"+
		"\u0000\u0000\u0084\u0085\u0005R\u0000\u0000\u0085\u0086\u0005I\u0000\u0000"+
		"\u0086\u0087\u0005G\u0000\u0000\u0087\u0088\u0005H\u0000\u0000\u0088\u0089"+
		"\u0005T\u0000\u0000\u0089\u001a\u0001\u0000\u0000\u0000\u008a\u008b\u0005"+
		"L\u0000\u0000\u008b\u008c\u0005E\u0000\u0000\u008c\u008d\u0005F\u0000"+
		"\u0000\u008d\u008e\u0005T\u0000\u0000\u008e\u001c\u0001\u0000\u0000\u0000"+
		"\u008f\u0090\u0005U\u0000\u0000\u0090\u0091\u0005P\u0000\u0000\u0091\u001e"+
		"\u0001\u0000\u0000\u0000\u0092\u0093\u0005D\u0000\u0000\u0093\u0094\u0005"+
		"O\u0000\u0000\u0094\u0095\u0005W\u0000\u0000\u0095\u0096\u0005N\u0000"+
		"\u0000\u0096 \u0001\u0000\u0000\u0000\u0097\u0098\u0005,\u0000\u0000\u0098"+
		"\"\u0001\u0000\u0000\u0000\u0099\u009a\u0005]\u0000\u0000\u009a$\u0001"+
		"\u0000\u0000\u0000\u009b\u009c\u0005(\u0000\u0000\u009c&\u0001\u0000\u0000"+
		"\u0000\u009d\u009e\u0005)\u0000\u0000\u009e(\u0001\u0000\u0000\u0000\u009f"+
		"\u00a0\u0005/\u0000\u0000\u00a0*\u0001\u0000\u0000\u0000\u00a1\u00a2\u0007"+
		"\u0000\u0000\u0000\u00a2,\u0001\u0000\u0000\u0000\u00a3\u00a7\u0007\u0001"+
		"\u0000\u0000\u00a4\u00a6\u0007\u0002\u0000\u0000\u00a5\u00a4\u0001\u0000"+
		"\u0000\u0000\u00a6\u00a9\u0001\u0000\u0000\u0000\u00a7\u00a5\u0001\u0000"+
		"\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8.\u0001\u0000\u0000"+
		"\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00aa\u00ab\u0005/\u0000\u0000"+
		"\u00ab\u00ac\u0005/\u0000\u0000\u00ac\u00b0\u0001\u0000\u0000\u0000\u00ad"+
		"\u00af\t\u0000\u0000\u0000\u00ae\u00ad\u0001\u0000\u0000\u0000\u00af\u00b2"+
		"\u0001\u0000\u0000\u0000\u00b0\u00b1\u0001\u0000\u0000\u0000\u00b0\u00ae"+
		"\u0001\u0000\u0000\u0000\u00b1\u00b3\u0001\u0000\u0000\u0000\u00b2\u00b0"+
		"\u0001\u0000\u0000\u0000\u00b3\u00b4\u0005\n\u0000\u0000\u00b4\u00b5\u0001"+
		"\u0000\u0000\u0000\u00b5\u00b6\u0006\u0017\u0000\u0000\u00b60\u0001\u0000"+
		"\u0000\u0000\u00b7\u00b9\u0007\u0003\u0000\u0000\u00b8\u00b7\u0001\u0000"+
		"\u0000\u0000\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba\u00b8\u0001\u0000"+
		"\u0000\u0000\u00ba\u00bb\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000"+
		"\u0000\u0000\u00bc\u00bd\u0006\u0018\u0000\u0000\u00bd2\u0001\u0000\u0000"+
		"\u0000\u0004\u0000\u00a7\u00b0\u00ba\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}