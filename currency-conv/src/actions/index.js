import axios from "axios";

import { PATH } from "../constants";

export function convert(amount, currency) {
  const data = {
    from_currency: currency,
    amount: Number(amount.replace(/\s/g, ""))
  };

  return axios
    .post(`${PATH}/api/currency/`, data)
    .catch(error => alert(error.message));
}

export function update() {
  return axios
    .post(`${PATH}/rate/update`)
    .catch(error => alert(error.message));
}
