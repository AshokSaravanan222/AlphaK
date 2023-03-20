mkdir python
for file in *ui; do
    python3 -m PyQt6.uic.pyuic "$file" -o python/"${file%%.*}"_ui.py
done
