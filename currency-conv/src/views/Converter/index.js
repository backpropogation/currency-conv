import React, { useState, useEffect } from "react";
import { Paper } from "@material-ui/core/";
import { makeStyles } from "@material-ui/core/styles";

import { convert, update } from "../../actions";

import {
  Container,
  Switcher,
  Input,
  Output,
  RefreshButton,
  ConvertButton
} from "../../components";

const useStyles = makeStyles(theme => ({
  paper: {
    marginTop: 32
  }
}));

function Converter() {
  const [amount, setAmount] = useState("1");
  const [currency, setCurrency] = useState("USD");
  const [convertedCurrency, setConvertedCurrency] = useState(null);

  const classes = useStyles();

  useEffect(() => {
    handleConvert();
  }, []);

  async function handleConvert() {
    const response = await convert(amount, currency);
    const data = response.data.converted_currencies;
    setConvertedCurrency(data);
  }

  async function handleUpdate() {
    await update();
    handleConvert();
  }

  return (
    convertedCurrency && (
      <Container>
        <Paper>
          <Switcher currency={currency} setCurrency={setCurrency} />
          <Input amount={amount} setAmount={setAmount} />
        </Paper>

        <Paper className={classes.paper}>
          <ConvertButton handleClick={handleConvert} />
          <RefreshButton handleClick={handleUpdate} />
        </Paper>

        <Output data={convertedCurrency} />
      </Container>
    )
  );
}

export default Converter;
