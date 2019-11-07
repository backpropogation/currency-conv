import React from "react";

import "./OutputString.scss";

function OutputString(props) {
  const { title, amount } = props;

  return (
    <div className="output_string">
      <p className="output_string__title">{title}</p>
      <p className="output_string__amount">{amount || "-"}</p>
    </div>
  );
}

export default OutputString;
