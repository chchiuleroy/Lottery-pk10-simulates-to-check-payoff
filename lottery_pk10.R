x = 1:10

u = {}

for(j in 1:30) {
  
  sim = t(replicate(1000000, sample(x, 2, replace = F)))
  s = apply(sim, 1, sum)
  pay = c(0, 0, 44.145, 44.145, 22.070, 22.070, 14.695, 14.695, 11.025, 11.025, 8.820, 11.025, 11.025, 14.695, 14.695, 22.070, 22.070, 44.145, 44.145)
  money = c(0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1)
  temp = sapply(1:length(s), function(x) {pay[[s[x]]]*money[s[x]]}) 
  u[j] = sum(temp)/length(s)/sum(money)
  
}

boxplot(u)