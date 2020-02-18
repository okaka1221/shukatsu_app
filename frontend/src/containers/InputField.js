import { connect } from 'react-redux';
import InputField from '../components/InputField';
import { getTextAnalysis } from '../api/textAnalysis';

const mapStateToProps = state => {
  return {
    isPending: state.textAnalysis.isPending,
    encodedWordcloud: state.textAnalysis.encodedWordcloud,
    keywordSimScore: state.textAnalysis.keywordSimScore,
    jikoPRScore: state.textAnalysis.jikoPRScore,
    error: state.textAnalysis.error,
  }
}

const mapDispatchToProps = dispatch => {
  return {
    getTextAnalysis(keyword, text, type) {
      dispatch(getTextAnalysis(keyword, text, type));
    }
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(InputField);