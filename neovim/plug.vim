" Plugins instalados

call plug#begin('~/.config/nvim/plugged')

Plug 'easymotion/vim-easymotion'			" es un buscador sofisticado
Plug 'scrooloose/nerdtree'						" abre un arbol de directorios
Plug 'christoomey/vim-tmux-navigator'	" me permite navegar entre paneles
Plug 'sheerun/vim-polyglot'						" sintasix
Plug 'maximbaz/lightline-ale'					" tema de la barra
Plug 'itchyny/lightline.vim'					" agrega la barra bonita
Plug 'jiangmiao/auto-pairs'						" cierra parentesis y similares
Plug 'alvan/vim-closetag'							" cierra tags como html
Plug 'mhinz/vim-signify'							" nos muestra un + y un -
Plug 'yggdroot/indentline'						" nos muestra lineas en el identado
Plug 'scrooloose/nerdcommenter'				" para comentarios
Plug 'vim-airline/vim-airline'					"	barra superior
Plug 'vim-airline/vim-airline-themes'		"	tema para airline (luna)
Plug 'ryanoasis/vim-devicons'						" iconos
Plug 'neoclide/coc.nvim', {'branch': 'release'} " coc para lenguajes

Plug 'vim-python/python-syntax'         " resalta sintasix para python

call plug#end()

" para habilitar la barra superior
let g:airline#extensions#tabline#enabled = 1

" para setear el temas de vim-airline
let g:airline_theme = 'luna'

let g:NERDSpaceDelims = 1
" para comentar <Leader>cc
