import { connect } from 'react-redux';
import InputField from '../components/InputField';
import { getTextAnalysis } from '../api/textAnalysis';

const mapDispatchToProps = dispatch => {
  return {
    getTextAnalysis(keyword, text, type) {
      dispatch(getTextAnalysis(keyword, text, type));
    }
  };
}

export default connect(null, mapDispatchToProps)(InputField);