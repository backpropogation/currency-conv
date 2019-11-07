import React from "react";
import { TextField } from "@material-ui/core/";
import { withStyles } from "@material-ui/core/styles";

import { divideNumber } from "../../utils";

const StyledInput = withStyles({
  root: {
    width: "100%",
    padding: 20,
    boxSizing: "border-box",
    "& .MuiOutlinedInput-root": {
      "& input": {
        height: 50,
        lineHeight: 50,
        fontSize: 45,
        fontFamily: "Open Sans",
        textAlign: "center",
        border: "none"
      },
      "& fieldset": {
        border: "none"
      },
      "&:hover fieldset": {
        border: "none"
      },
      "&.Mui-focused fieldset": {
        border: "none"
      }
    }
  }
})(TextField);

function Input(props) {
  const { amount, setAmount } = props;

  function handleChange(event) {
    const newValue = event.target.value.replace(/\D/g, "");
    const dividedValue = divideNumber(newValue);
    setAmount(dividedValue);
  }

  return (
    <StyledInput
      value={amount}
      onChange={handleChange}
      inputProps={{
        maxLength: 11
      }}
      autoFocus
      variant="outlined"
    ></StyledInput>
  );
}

export default Input;
