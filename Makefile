

install:
	- virtualenv ../mestrado_cefet
	- ( \
       . bin/activate; \
       pip install -r requirements.txt; \
    )
start:
	- ( \
       . bin/activate; \
      python main.py \
    )