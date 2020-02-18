import { connect } from 'react-redux';
import Result from '../components/Result';

const mapStateToProps = state => {
  return {
    isPending: state.textAnalysis.isPending,
    encodedWordcloud: state.textAnalysis.encodedWordcloud,
    keywordSimScore: state.textAnalysis.keywordSimScore,
    jikoPRScore: state.textAnalysis.jikoPRScore,
    error: state.textAnalysis.error,
  }
}

export default connect(mapStateToProps, null)(Result);
