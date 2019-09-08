

install:
	- virtualenv ../mestrado_cefet
	- ( \
       . bin/activate; \
       pip3 install -r requirements.txt; \
    )
start:
	- ( \
       . bin/activate; \
      python main.py \
    )