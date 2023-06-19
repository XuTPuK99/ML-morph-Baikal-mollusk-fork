# ML-morph-Baikal-mollusk-fork
machine learning, baikal mollusk, geometric morphometry

Данный репозиторий содержит в себе fork программного обеспечения ML-morph (https://github.com/agporto/ml-morph), вместе с набором скриптов для проведения статистического анализа морфологических параметров.

Основные инструкции по работе с нейросетью и формированию своей модели описаны в файле README_neural_network.md и в статье ML-morph: A fast, accurate and general approach for automated detection and landmarking of biological structures in images.

Представленны обработанные фотографии и разметки к ним, с помощью которых можно обучить нейросеть обнаруживать 16 ключевых точек для дальнейшего анализа методом геометрической морфометрии с помощью программы Modicos или MorphJ, а также при помощи PCA (анализ главных компонент).

В репозитории содержатся вспомогательные скрипты: 
 - draw_model_mollusc.py, рисует усреднённые модели моллюсков
 - PERMANOVA_analysis.R, проводит поиск статистических зависимостей в наборе данных (PERMANOVA)
 - PCA_analysis.R, проводит PCA анализ
