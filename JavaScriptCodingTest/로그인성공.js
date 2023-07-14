function solution(id_pw, db) {
  const id= id_pw[0]
  const pw= id_pw[1]   // const [id,pw]=id_pw
  const info_index=db.findIndex((info)=>info[0]===id)
  if( info_index===-1) return "fail"
  else{
      if(db[info_index][1]===pw) return "login"
      else return "wrong pw"
  }
}

function solution(id_pw,db){
  const [id,pw]=id_pw;
  const users= new Map(db)
  return users.has(id) ? (users.get(id) === pw ? "login" : "wrong pw") : "fail"
}