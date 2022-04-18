document.addEventListener('DOMContentLoaded', () => {
    const STEPPER = 'stepper'
    const MAXIMUM_NUMBER_COLUMNS = 10

    const gridView = document.getElementById('gridView')

    const form = document.getElementById("form")
    const form_pallet = document.getElementById("form_pallet")
    const form_door = document.getElementById("form_door")


    const container = document.getElementById("grid_container")
    const undoButton = document.getElementById('undo')

    let arrayOfClickedRows = []


    //hide the gridView

    gridView.style.display = 'none'

    for (let indexRow = 0; indexRow < MAXIMUM_NUMBER_COLUMNS; indexRow++) {
        const row = document.createElement('div')
        row.classList = 'row'
        for (let index = 0; index < MAXIMUM_NUMBER_COLUMNS; index++) {
            //colums here
            const column = document.createElement('div')
            column.classList = 'col-1 p-2 border border-2 '
            column.style.cursor = 'pointer'
            column.innerText = `R${indexRow}C${index}`
            column.onclick = () => {
                const columnIndex = arrayOfClickedRows.indexOf(`R${indexRow}C${index}`)
                console.log(columnIndex)

                if (columnIndex > -1) {
                    arrayOfClickedRows = arrayOfClickedRows.filter(item => item !== `R${indexRow}C${index}`)
                    column.style.background = 'transparent'
                    console.log({ removed: arrayOfClickedRows })
                    return
                }

                column.style.background = 'red'
                arrayOfClickedRows.push(`R${indexRow}C${index}`)
                console.log({ added: arrayOfClickedRows })
            }
            row.appendChild(column)

        }

        container.appendChild(row);

        //rows here
    }


    form.onsubmit = (event) => {
        console.log(event)
        event.preventDefault()

        const formData = new FormData(event.target);
        const formProps = Object.fromEntries(formData);

        // form.style.display = 'none'
        gridView.style.display = 'grid'
    }


}, false);
