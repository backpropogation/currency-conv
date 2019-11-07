import React from "react";
import { Button } from "@material-ui/core/";
import LoopIcon from "@material-ui/icons/Loop";
import { withStyles } from "@material-ui/core/styles";

const StyledButton = withStyles({
  root: {
    height: "60px"
  }
})(Button);

function ConvertButton(props) {
  const { handleClick } = props;

  return (
    <StyledButton
      onClick={handleClick}
      size="large"
      fullWidth
      startIcon={<LoopIcon />}
    >
      Convert
    </StyledButton>
  );
}

export default ConvertButton;
