from base64 import b64encode
from io import BytesIO
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem.rdChemReactions import ReactionFromSmarts


def validate_smiles(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None and mol.GetNumAtoms() > 0:
            return True  # SMILES is valid
        else:
            return False  # SMILES is invalid
    except:
        return False  # Exception occurred, SMILES is invalid


def validate_reaction(smiles):
    try:
        mol = ReactionFromSmarts(smiles, useSmiles=True)
        if mol is not None:
            return True  # SMILES is valid
        else:
            return False  # SMILES is invalid
    except:
        return False  # Exception occurred, SMILES is invalid


def smi2png(smi, height=300, width=300, opacity=0.0, full_screen=False):
    buffered = BytesIO()
    d2d = rdMolDraw2D.MolDraw2DCairo(width, height)
    opts = d2d.drawOptions()
    opts.clearBackground = True
    opts.setBackgroundColour((1, 1, 1, opacity))  # 设置背景颜色为透明
    d2d.SetColour((1, 1, 1, opacity))  # 设置背景颜色为透明
    d2d.DrawReaction(ReactionFromSmarts(smi, useSmiles=True))
    d2d.FinishDrawing()
    img = d2d.GetDrawingText()
    # d2d.WriteDrawingText(buffered)
    buffered.write(img)

    img_str = "data:image/png;base64," + b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def smi2svg(smi, height=300, width=300, reaction=False, opacity=0.0, full_screen=False):
    buffered = BytesIO()

    d2d = rdMolDraw2D.MolDraw2DSVG(width, height)
    opts = d2d.drawOptions()
    opts.clearBackground = True
    if not reaction:
        d2d.DrawMolecule(Chem.MolFromSmiles(smi))
    else:
        d2d.DrawReaction(ReactionFromSmarts(smi, useSmiles=True))
    d2d.FinishDrawing()
    img_str = d2d.GetDrawingText()
    img_str = img_str.replace(
        "<rect style='opacity:1.0", f"<rect style='opacity: {opacity}"
    )
    if not full_screen:
        img_str = img_str.replace("stroke-width:2.0px;", "stroke-width:0.5px;")
    buffered.write(str.encode(img_str))
    img_str = b64encode(buffered.getvalue())
    img_str = f"data:image/svg+xml;base64,{repr(img_str)[2:-1]}"
    return img_str
