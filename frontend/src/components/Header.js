import React from "react";
import { AppBar, Toolbar, Typography } from "@material-ui/core";

class Header extends React.Component {
  render() {
    return (
      <header>
        <AppBar>
          <Toolbar>
            <Typography variant="h6">
              エントリーシート自己PR分析　〜 あなたの自己PRをAIが分析します 〜
            </Typography>
          </Toolbar>
        </AppBar>
      </header>
    )
  }
}

export default Header
