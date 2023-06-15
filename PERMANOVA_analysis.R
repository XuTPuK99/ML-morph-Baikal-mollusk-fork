Sys.setlocale("LC_CTYPE", "russian")

library(vegan)

setwd("C:\\Users\\User\\Desktop\\article_work\\")

data<-read.table("data.txt",header=TRUE,sep="\t")

morfotip<-data[, 8, drop=F]

data<-data[,-8]

data<-data[,-1]

data<-decostand(data, method="range", MARGIN=2)

data.div <- adonis2(data ~ Morfotip, data=morfotip, permutations = 10000, method="euclidean")

data.div