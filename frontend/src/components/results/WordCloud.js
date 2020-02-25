import React from "react";
import { Typography, Grid, Button, Dialog, DialogTitle, DialogContent, DialogContentText } from "@material-ui/core";

class WordCloud extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      open: false,
    }

    this.handleOpen = this.handleOpen.bind(this);
    this.handleClose = this.handleClose.bind(this);
  };

  handleOpen() {
    this.setState({ open: true });
  }

  handleClose() {
    this.setState({ open: false });
  }

  render() {
    return (
      <div>
        {
          this.props.encodedWordcloud !== null ?
            <div>
              <Grid container>
                <Grid item xs={12} md={5} lg={4}>
                  <Typography variant='h5'>ワードクラウド</Typography>
                </Grid>
                <Grid item xs={12} md={5} lg={4}>
                  <Button 
                    size='large'
                    onClick={this.handleOpen}
                  >
                    ワードクラウドとは？
                  </Button>
                </Grid>
                <Grid item xs={0} md={2} lg={4}>
                </Grid>
              </Grid>
              <img 
                src={"data:image/png;base64," + this.props.encodedWordcloud}
                alt="wordcloud"
                width="450" height="450"
                style={{ marginTop: 20 }}
              />
            </div>
          : null
        }
        <Dialog
          aria-labelledby="modal-title"
          aria-describedby="modal-description"
          open={this.state.open}
          onClose={this.handleClose}
        >
          <DialogTitle>
            ワードクラウドとは？
          </DialogTitle>
          <DialogContent>
            <DialogContentText>
              文章内の単語の頻度を視覚的に捉えやすくしたものです。              
            </DialogContentText>
            <DialogContentText>            
              頻度の高い単語ほど大きく表示されます。
            </DialogContentText>
          </DialogContent>
        </Dialog>
      </div>
    )
  }
}

export default WordCloud;