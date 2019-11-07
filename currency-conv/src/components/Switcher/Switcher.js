import React from "react";
import { Grid } from "@material-ui/core/";
import { ToggleButton, ToggleButtonGroup } from "@material-ui/lab/";
import { withStyles } from "@material-ui/core/styles";

const StyledToggleButtonGroup = withStyles(theme => ({
  grouped: {
    border: "none",
    padding: theme.spacing(0, 1),
    "&:first-child": {
      borderTopLeftRadius: theme.shape.borderRadius
    },
    "&:last-child": {
      borderTopRightRadius: theme.shape.borderRadius
    }
  }
}))(ToggleButtonGroup);

const StyledButton = withStyles({
  root: {
    width: "120px",
    height: "50px",
    fontSize: "20px",
    color: "black",
    borderBottomLeftRadius: 0,
    borderBottomRightRadius: 0
  },
  selected: {
    background: "#16b67f !important",
    color: "#ffffff !important"
  }
})(ToggleButton);

function Switcher(props) {
  const { currency, setCurrency } = props;

  function handleChange(event, newCurrency) {
    if (newCurrency) {
      setCurrency(newCurrency);
    }
  }

  return (
    <Grid>
      <StyledToggleButtonGroup
        size="large"
        exclusive
        value={currency}
        onChange={handleChange}
      >
        <StyledButton key={1} value="USD">
          USD
        </StyledButton>
        <StyledButton key={2} value="EUR">
          EUR
        </StyledButton>
        <StyledButton key={3} value="CZK">
          CZK
        </StyledButton>
        <StyledButton key={4} value="PLN">
          PLN
        </StyledButton>
      </StyledToggleButtonGroup>
    </Grid>
  );
}

export default Switcher;
