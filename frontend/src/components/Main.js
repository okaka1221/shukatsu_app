import React from "react";
import Header from "./Header";
import InputField from "../containers/InputField";
import Result from "../containers/Result";
import { Toolbar, Container } from "@material-ui/core";

class Main extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <Toolbar />
        <Container >
          <InputField />
        </Container>
        <Toolbar />
        <Container>
          <Result />
        </Container>
      </div>
    )
  }
}

export default Main;