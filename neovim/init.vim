" Archivo de configuración de neovim

source $HOME/.config/nvim/conf.vim
source $HOME/.config/nvim/plug.vim
source $HOME/.config/nvim/coc.vim

let mapleader = " "
nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>
nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
nmap <Leader>a gg0vG$

nnoremap <Leader>> 10<C-w>>
nnoremap <Leader>< 10<C-w><

" Primero se selecciona la linea con V
vnoremap <A-k> :move '<-2<CR>-gv
vnoremap <A-j> :move '>+1<CR>-gv

" PD: si separas la configuración en varios archivos
" Te va mas rapido, de lo contrario si tienes todo en uno
" solo se relentiza.
