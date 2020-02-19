import { connect } from 'react-redux';
import InputField from '../components/InputField';
import { postEntrySheet } from '../api/entrySheet';

const mapStateToProps = state => {
  return {
    isPending: state.entrySheet.isPending,
    encodedWordcloud: state.entrySheet.encodedWordcloud,
    keywordSimScore: state.entrySheet.keywordSimScore,
    jikoPRScore: state.entrySheet.jikoPRScore,
    error: state.entrySheet.error,
  }
}

const mapDispatchToProps = dispatch => {
  return {
    postEntrySheet(keyword, text, type) {
      dispatch(postEntrySheet(keyword, text, type));
    }
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(InputField);