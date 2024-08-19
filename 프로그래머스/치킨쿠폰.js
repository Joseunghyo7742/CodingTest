function solution(chicken) {
  let total_chicks= Math.floor(chicken/10);
  let coupon= chicken%10+total_chicks;
  while(coupon>=10){
      const chicks= Math.floor(coupon/10);
      coupon-=(chicks*10-chicks);
      total_chicks+=chicks;
      console.log(coupon);
  }
  return total_chicks;
}