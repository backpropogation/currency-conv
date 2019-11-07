import React from "react";
import { Button } from "@material-ui/core/";
import RefreshIcon from "@material-ui/icons/Refresh";
import { withStyles } from "@material-ui/core/styles";

const StyledButton = withStyles({
  root: {
    height: "60px"
  }
})(Button);

function RefreshButton(props) {
  const { handleClick } = props;

  return (
    <StyledButton
      onClick={handleClick}
      size="large"
      fullWidth
      startIcon={<RefreshIcon />}
    >
      Update rates
    </StyledButton>
  );
}

export default RefreshButton;
