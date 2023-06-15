#Вычисление основных компонент
data <- read.table("C:\\Users\\User\\Desktop\\article_work\\data.txt", header=TRUE, sep="\t", as.is=TRUE, check.names=FALSE, comment.char="", row.names=1)
data.pca <- prcomp(data[,c(1:6)], center = TRUE,scale. = TRUE)

#Построение PCA
library(devtools)
library(ggbiplot)

#Интерпретация результатов
data.label <- c(rep("Гладкие 20м", 18),rep("Ребристые 4м", 18))

ggbiplot(data.pca,ellipse=TRUE, choices=c(1,2), groups=data.label) + scale_shape_manual(name="groups",values=c(15:18))  + geom_point(aes(colour=data.label, shape=data.label), size = 3) + theme(panel.background = element_rect(fill = "white",colour = "grey"), panel.grid = element_line(colour = "light grey"))
