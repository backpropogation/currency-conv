export function divideNumber(num) {
  return String(num).replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, "$1 ");
}
