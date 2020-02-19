import { connect } from 'react-redux';
import Result from '../components/Result';

const mapStateToProps = state => {
  return {
    isPending: state.entrySheet.isPending,
    encodedWordcloud: state.entrySheet.encodedWordcloud,
    keywordSimScore: state.entrySheet.keywordSimScore,
    jikoPRScore: state.entrySheet.jikoPRScore,
    error: state.entrySheet.error,
  }
}

export default connect(mapStateToProps, null)(Result);
