

install:
	- virtualenv ../mestrado_cefet
	- ( \
       . bin/activate; \
       pip3 install -U -r requirements.txt; \
    )
run:
	- ( \
       . bin/activate; \
      python3 main.py \
    )