import { CountUp } from './countUp.js';
const options = {
  separator: '.',
};
countUp = new CountUp('gifts', 0, options);
if (!countUp.error) {
  countUp.start();
} else {
  console.error(countUp.error);
}