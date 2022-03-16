set number
set title
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd
set cursorline
set encoding=utf-8
set showmatch
set sw=2

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

call plug#end()

let mapleader = " "
nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>
nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
nmap <Leader>a gg0vG$

nnoremap <Leader>> 10<C-w>>
nnoremap <Leader>< 10<C-w><

let g:NERDSpaceDelims = 1
" para comentar <Leader>cc
