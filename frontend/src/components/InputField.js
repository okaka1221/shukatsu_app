import React from "react";
import { 
  Typography, 
  TextField, 
  Button, 
  FormControl,
  FormHelperText,
  Select,
  MenuItem
} from "@material-ui/core";

class InputField extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      keywords: "",
      text: "",
      label: "",
      labelError: false,
      textError: false,
    }

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e) {
    e.preventDefault();
    const { name, value } = e.target;
    this.setState({ [name]: value });
  }

  handleSubmit(e) {
    e.preventDefault();
    const { keywords, text, label } = this.state;

    if (label === "") {
      this.setState({ labelError: true })
    } else {
      this.setState({ labelError: false })
    }

    if (text === "") {
      this.setState({ textError: true })
    } else {
      this.setState({ textError: false })
    }
    
    if (text !== "" && label !== "") {
      this.props.getTextAnalysis(keywords, text, label);
    }
  }

  render() {
    const { error } = this.props;
    let { textError } = this.state;
    let textErrorDetail;


    
    if (textError) {
      textErrorDetail = "自己PRを入力してください"
    } else if (error === 400) {
      textError = true;
      textErrorDetail = "自己PRを適切に入力してください"
    }

    return (
      <div>
        <form name="form" onSubmit={this.handleSubmit}>
          <Typography variant='h5' style={{ marginTop: 30 }}>自己PRであなたを表すキーワード（日本語のみで、複数の場合は間にスペースを入れて下さい。）</Typography>
          <TextField
            margin="normal"
            name="keywords"
            fullWidth
            placeholder="e.g. サークル　テニス　幹部"
            variant="outlined"
            value={this.state.keywords}
            onChange={this.handleChange}
          />
          <Typography variant='h5' style={{ marginTop: 30 }}>この自己PRを用いてES選考を通過しましたか？</Typography>
          <FormControl 
            variant="outlined" 
            style={{minWidth: 300, marginTop: 15}}
            error={this.state.labelError}
          >
            <Select
              name="label"
              value={this.state.label}
              onChange={this.handleChange}
              displayEmpty
             >
              <MenuItem value={""} disabled>
                選択して下さい
              </MenuItem>
              <MenuItem value={true}>はい</MenuItem>
              <MenuItem value={false}>いいえ</MenuItem>
              <MenuItem value={"unk"}>未使用</MenuItem>
            </Select>
            <FormHelperText>{this.state.labelError ? "選択して下さい" : ""}</FormHelperText>
          </FormControl>
          <Typography variant='h5' style={{ marginTop: 30 }}>自己PR</Typography>
          <TextField
            margin="normal"
            name="text"
            multiline
            fullWidth
            rows="8"
            variant="outlined"
            value={this.state.text}
            onChange={this.handleChange}
            error={textError}
            helperText={textError ? textErrorDetail : ""}
          />
          <Button
            margin="normal"
            type="submit"
            variant="contained"
            size="large"
            style={{ marginTop: 30 }}
          >
            分析
          </Button>
        </form>
      </div>
    )
  }
}

export default InputField;
