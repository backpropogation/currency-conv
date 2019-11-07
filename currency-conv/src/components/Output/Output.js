import React from "react";
import { Paper } from "@material-ui/core/";
import { makeStyles } from "@material-ui/core/styles";

import OutputString from "../OutputString";

const useStyles = makeStyles(theme => ({
  root: {
    marginTop: 32
  }
}));

function Output(props) {
  const { data } = props;
  const classes = useStyles();

  return (
    <Paper className={classes.root}>
      <OutputString title="USD" amount={data.USD} />
      <OutputString title="EUR" amount={data.EUR} />
      <OutputString title="CZK" amount={data.CZK} />
      <OutputString title="PLN" amount={data.PLN} />
    </Paper>
  );
}

export default Output;
