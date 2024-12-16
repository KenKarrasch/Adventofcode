Imports System.Net.Mime.MediaTypeNames
Imports System.Drawing
Imports System.Windows.Forms.VisualStyles.VisualStyleElement.Rebar
Imports System.IO

Public Class Form1
    ' Variables to control the grid and the position of the little man
    Inherits Form
    Private shouldDrawGrid As Boolean = False
    Private manRow As Integer = 2
    Private manCol As Integer = 2
    Private squareSize As Integer = 10
    Private rows As Integer = 50
    Private columns As Integer = 50
    Private gridBitmap As Bitmap
    Private grass As System.Drawing.Image
    Private haybale As System.Drawing.Image
    Private fire As System.Drawing.Image
    Private wall As System.Drawing.Image

    'Public Structure Point
    ' Public X As Integer
    'Public Y As Integer

    ' Constructor to initialize the point
    '    Public Sub New(x As Integer, y As Integer)
    '    Me.X = x
    '    Me.Y = y
    '   End Sub

    ' Override ToString method for easy display
    '   Public Overrides Function ToString() As String
    '   Return $"({X}, {Y})"
    '   End Function
    '   End Structure


    Dim walls(columns, rows) As Integer

    Dim directions() As Char

    ' Dim walls(,) As Integer = {
    '         {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    '         {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1},
    '         {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}}

    Dim fires As New List(Of Point)()


    ' Constructor to initialize the form
    Public Sub New()
        ' This call is required by the designer.
        InitializeComponent()

        grass = System.Drawing.Image.FromFile("grass.png")
        haybale = System.Drawing.Image.FromFile("haybale.png")
        fire = System.Drawing.Image.FromFile("fire.png")
        wall = System.Drawing.Image.FromFile("wall.png")


        Dim filePath As String = "24-15.txt"
        Dim fileContent As String = File.ReadAllText(filePath)
        Dim sections() As String = fileContent.Split(New String() {Environment.NewLine & Environment.NewLine}, StringSplitOptions.RemoveEmptyEntries)

        Dim mapLines() As String = sections(0).Split(Environment.NewLine)
        Dim rows As Integer = mapLines.Length
        Dim cols As Integer = mapLines(0).Length


        'MsgBox(rows, cols)

        'Dim walls(rows - 1, cols - 1) As Integer

        For i As Integer = 0 To rows - 1
            For j As Integer = 0 To cols - 1
                Select Case mapLines(i)(j)
                    Case "#"c
                        walls(i, j) = 2
                    Case "O"c
                        walls(i, j) = 1
                    Case "."c
                        walls(i, j) = 0
                    Case "@"c
                        manRow = i
                        manCol = j
                End Select
            Next
        Next

        directions = sections(1).Replace(Environment.NewLine, "").ToCharArray()

        'Dim rand As New Random()

        'For row As Integer = 0 To 600
        'walls(rand.Next(0, 20), rand.Next(0, 30)) = 1
        'Next

        'For row As Integer = 0 To 5
        'fires.Add(New Point(rand.Next(0, 20), rand.Next(0, 30)))
        'Next


        ' Set double buffering to reduce flicker
        Me.DoubleBuffered = True
    End Sub

    ' Event handler for the button click event
    Private Sub btnDrawGrid_Click(sender As Object, e As EventArgs) Handles Button1.Click
        shouldDrawGrid = True
        CreateGridBitmap()
        Invalidate() ' This will trigger the Paint event
    End Sub

    ' Event handler for the Paint event of the form
    Private Sub Form1_Paint(sender As Object, e As PaintEventArgs) Handles MyBase.Paint
        If shouldDrawGrid Then
            If gridBitmap IsNot Nothing Then
                e.Graphics.DrawImage(gridBitmap, 0, 0)
            End If
            DrawLittleMan(e.Graphics)
        End If

    End Sub

    ' Method to create the grid bitmap
    Private Sub CreateGridBitmap()
        ' Initialize the bitmap
        gridBitmap = New Bitmap(columns * squareSize, rows * squareSize)
        Using g As Graphics = Graphics.FromImage(gridBitmap)
            DrawGrid(g)
        End Using
    End Sub

    ' Method to draw the grid
    Private Sub DrawGrid(g As Graphics)
        ' Create a pen to draw the squares
        Dim pen As New Pen(Color.Black)
        Dim wallpen As New Pen(Color.Red)

        Dim brush As New SolidBrush(Color.Blue)

        ' Loop through the number of rows and columns to draw the grid
        For row As Integer = 0 To rows - 1
            For col As Integer = 0 To columns - 1
                ' Calculate the position of each square
                Dim x As Integer = col * squareSize
                Dim y As Integer = row * squareSize

                ' Draw the square
                If walls(row, col) = 1 Then
                    g.DrawRectangle(wallpen, x, y, squareSize, squareSize)
                    g.DrawImage(haybale, x, y, squareSize, squareSize)
                    If fires.Contains(New Point(row, col)) Then
                        g.DrawImage(fire, x, y, squareSize, squareSize)
                    End If
                ElseIf walls(row, col) = 2 Then
                    g.DrawRectangle(pen, x, y, squareSize, squareSize)
                    g.DrawImage(wall, x, y, squareSize, squareSize)
                Else
                    g.DrawRectangle(pen, x, y, squareSize, squareSize)
                    g.DrawImage(grass, x, y, squareSize, squareSize)
                    ' g.FillRectangle(brush, x, y, squareSize, squareSize)
                End If
            Next
        Next
    End Sub

    ' Method to draw the little man
    Private Sub DrawLittleMan(g As Graphics)
        ' Calculate the position of the little man
        Dim x As Integer = manCol * squareSize
        Dim y As Integer = manRow * squareSize

        ' Draw the little man (simple representation: head, body, arms, legs)
        Dim headSize As Integer = squareSize \ 2
        Dim bodyHeight As Integer = squareSize \ 2
        Dim bodyWidth As Integer = squareSize \ 4

        ' Draw head
        g.FillEllipse(Brushes.Blue, x + (squareSize - headSize) \ 2, y, headSize, headSize)

        ' Draw body
        g.FillRectangle(Brushes.Blue, x + (squareSize - bodyWidth) \ 2, y + headSize, bodyWidth, bodyHeight)

        ' Draw arms
        g.DrawLine(Pens.Blue, x + (squareSize - bodyWidth) \ 2, y + headSize + bodyHeight \ 2, x, y + headSize + bodyHeight \ 2)
        g.DrawLine(Pens.Blue, x + (squareSize + bodyWidth) \ 2, y + headSize + bodyHeight \ 2, x + squareSize, y + headSize + bodyHeight \ 2)

        ' Draw legs
        g.DrawLine(Pens.Blue, x + (squareSize - bodyWidth) \ 2, y + headSize + bodyHeight, x, y + squareSize)
        g.DrawLine(Pens.Blue, x + (squareSize + bodyWidth) \ 2, y + headSize + bodyHeight, x + squareSize, y + squareSize)
    End Sub

    ' Override the ProcessCmdKey method to handle arrow key presses
    Protected Overrides Function ProcessCmdKey(ByRef msg As Message, keyData As Keys) As Boolean
        Dim results = (0, 0)
        Dim shiftPressed As Boolean = (keyData And Keys.Shift) = Keys.Shift

        Select Case keyData And Not Keys.Shift
            Case Keys.Up
                results = MoveMan(manRow, manCol, -1, 0, shiftPressed)
            Case Keys.Down
                results = MoveMan(manRow, manCol, 1, 0, shiftPressed)
            Case Keys.Left
                results = MoveMan(manRow, manCol, 0, -1, shiftPressed)
            Case Keys.Right
                results = MoveMan(manRow, manCol, 0, 1, shiftPressed)
            Case Else
                Return MyBase.ProcessCmdKey(msg, keyData)
        End Select
        manRow = results.Item1
        manCol = results.Item2

        Me.Invalidate() ' Trigger the Paint event to redraw the grid and the little man
        Return True
    End Function

    Function MoveMan(manRow As Integer, manCol As Integer, dr As Integer, dc As Integer, shiftPressed As Boolean) As (Integer, Integer)
        Dim results = (0, 0)
        results = MoveManAuto(manRow, manCol, dr, dc, shiftPressed)
        manRow = results.Item1
        manCol = results.Item2
        Return (manRow, manCol)
    End Function

    Function MoveManAuto(manRow As Integer, manCol As Integer, dr As Integer, dc As Integer, shiftPressed As Boolean) As (Integer, Integer)
        If manRow + dr < 1 Then
            Return (manRow, manCol)
        End If
        If manCol + dc < 1 Then
            Return (manRow, manCol)
        End If
        If manRow + dr > rows - 2 Then
            Return (manRow, manCol)
        End If
        If manCol + dc > columns - 2 Then
            Return (manRow, manCol)
        End If
        Dim oktoPull = False
        Dim oktoPush = False

        Dim pullObject = (0, 0)

        If walls(manRow + dr, manCol + dc) = 0 Then
            If Not shiftPressed Then
                Return (manRow + dr, manCol + dc)
            End If
        End If

        If walls(manRow - dr, manCol - dc) = 1 Then
            If walls(manRow + dr, manCol + dc) = 0 Then
                If shiftPressed Then
                    pullObject = (manRow - dr, manCol - dc)
                    If walls(pullObject.Item1 + dr, pullObject.Item2 + dc) = 0 Then
                        If pullObject.Item1 > 0 Then
                            If pullObject.Item2 > 0 Then
                                If pullObject.Item1 < rows - 1 Then
                                    If pullObject.Item2 < columns - 1 Then
                                        oktoPull = True
                                    End If
                                End If
                            End If
                        End If
                    End If
                End If
            End If
        End If

        Dim srch = 1
        Dim foundEdge = False
        Dim foundClear = False

        While Not (foundEdge Or foundClear)
            If manRow + srch * dr < 1 Then
                foundEdge = True
            End If
            If manCol + srch * dc < 1 Then
                foundEdge = True
            End If
            If manRow + srch * dr > rows - 2 Then
                foundEdge = True
            End If
            If manCol + srch * dc > columns - 2 Then
                foundEdge = True
            End If
            If walls(manRow + (srch * dr), manCol + (srch * dc)) = 2 Then
                foundEdge = True
            End If
            If walls(manRow + (srch * dr), manCol + (srch * dc)) = 0 Then
                foundClear = True
            End If
            srch = srch + 1
        End While

        If Not foundEdge Then
            If srch > 1 Then
                If shiftPressed Then
                    If (walls(manRow - dr, manCol - dc) = 0) Then
                        oktoPush = True
                    End If
                Else
                    oktoPush = True
                End If
            End If
        End If

        If oktoPull Then
            walls(pullObject.Item1, pullObject.Item2) = 0
            walls(pullObject.Item1 + dr, pullObject.Item2 + dc) = 1
            'CreateGridBitmap()
            Return (manRow + dr, manCol + dc)
        End If

        If oktoPush Then
            walls(manRow + dr, manCol + dc) = 0
            For ctr As Integer = 2 To srch - 1
                If fires.Contains(New Point(manRow + ((ctr - 1) * dr), manCol + ((ctr - 1) * dc))) Then
                    fires.Add(New Point(manRow + (ctr * dr), manCol + (ctr * dc)))
                End If
                walls(manRow + (ctr * dr), manCol + (ctr * dc)) = 1
            Next
            'CreateGridBitmap()
            Return (manRow + dr, manCol + dc)
        End If

        Return (manRow, manCol)
    End Function

    ' Event handler to initialize the form
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        ' Ensure the form is large enough to display the grid
        Me.ClientSize = New Size(columns * squareSize, rows * squareSize)
        Me.KeyPreview = True
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click

        Dim results = (0, 0)

        For Each movedir As Char In directions
            ' Process the movedir character here
            Select Case movedir
                Case "^"c
                    results = MoveMan(manRow, manCol, -1, 0, False)
                Case "v"c
                    results = MoveMan(manRow, manCol, 1, 0, False)
                Case "<"c
                    results = MoveMan(manRow, manCol, 0, -1, False)
                Case ">"c
                    results = MoveMan(manRow, manCol, 0, 1, False)

            End Select
            manRow = results.Item1
            manCol = results.Item2

        Next
        Me.Invalidate() ' Trigger the Paint event to redraw the grid and the little man

        Dim tally = 0


        For i As Integer = 0 To rows
            For j As Integer = 0 To columns
                If walls(i, j) = 1 Then
                    tally = tally + i * 100 + j
                End If
            Next
        Next
        MsgBox(tally)

        shouldDrawGrid = True
        CreateGridBitmap()
        Invalidate() ' This will trigger the Paint event
    End Sub
End Class
