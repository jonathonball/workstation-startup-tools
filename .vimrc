" colors
colorscheme evening

" tabs and spaces
set tabstop=4       " number of visual spaces per TAB
set softtabstop=4   " numof of spaces in tab when editing
" set smartindent   " use the tab style present in the document, which is disabled, i want all spaces all the time
set shiftwidth=4    " number of columns text is indented with reindent operations
set expandtab       " tabs are spaces, this is known

" ui config
set nonumber        " hide line numbers
set showcmd         " show last command in bottom bar
set cursorline      " highlight current line
filetype indent on  " load filetype-specific indent files
set wildmenu        " visual autocomplete for command menu
set showmatch       " highlight matching [{()}]

" searching 
set incsearch       " search as characters are entered
set hlsearch        " hightlight matches

" keybindings
let mapleader=","       " set the leader key to the comma key
"     toggle search highlighting
nnoremap <leader>h :set nohlsearch!<CR>
"     toggle line numbers
nnoremap <leader>n :set nonumber!<CR>
"     toggle paste
nnoremap <leader>p :set nopaste!<CR>

