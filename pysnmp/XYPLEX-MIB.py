# SNMP MIB module (XYPLEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYPLEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:53 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xyplex_ObjectIdentity = ObjectIdentity
xyplex = _Xyplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 1)
)


class _SysIdent_Type(DisplayString):
    """Custom type sysIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysIdent_Type.__name__ = "DisplayString"
_SysIdent_Object = MibScalar
sysIdent = _SysIdent_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 1),
    _SysIdent_Type()
)
sysIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIdent.setStatus("mandatory")
_Character_ObjectIdentity = ObjectIdentity
character = _Character_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 2)
)
_CharPhysNumber_Type = Integer32
_CharPhysNumber_Object = MibScalar
charPhysNumber = _CharPhysNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 1),
    _CharPhysNumber_Type()
)
charPhysNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysNumber.setStatus("mandatory")
_CharPhysTable_Object = MibTable
charPhysTable = _CharPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2)
)
if mibBuilder.loadTexts:
    charPhysTable.setStatus("mandatory")
_CharPhysEntry_Object = MibTableRow
charPhysEntry = _CharPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1)
)
charPhysEntry.setIndexNames(
    (0, "XYPLEX-MIB", "charPhysIndex"),
)
if mibBuilder.loadTexts:
    charPhysEntry.setStatus("mandatory")
_CharPhysIndex_Type = Integer32
_CharPhysIndex_Object = MibTableColumn
charPhysIndex = _CharPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 1),
    _CharPhysIndex_Type()
)
charPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysIndex.setStatus("mandatory")


class _CharPhysPortName_Type(DisplayString):
    """Custom type charPhysPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CharPhysPortName_Type.__name__ = "DisplayString"
_CharPhysPortName_Object = MibTableColumn
charPhysPortName = _CharPhysPortName_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 2),
    _CharPhysPortName_Type()
)
charPhysPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysPortName.setStatus("mandatory")


class _CharPhysAdminAccess_Type(Integer32):
    """Custom type charPhysAdminAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("local", 3),
          ("none", 1),
          ("remote", 4))
    )


_CharPhysAdminAccess_Type.__name__ = "Integer32"
_CharPhysAdminAccess_Object = MibTableColumn
charPhysAdminAccess = _CharPhysAdminAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 3),
    _CharPhysAdminAccess_Type()
)
charPhysAdminAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysAdminAccess.setStatus("mandatory")


class _CharPhysOperAccess_Type(Integer32):
    """Custom type charPhysOperAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("none", 1),
          ("remote", 4))
    )


_CharPhysOperAccess_Type.__name__ = "Integer32"
_CharPhysOperAccess_Object = MibTableColumn
charPhysOperAccess = _CharPhysOperAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 4),
    _CharPhysOperAccess_Type()
)
charPhysOperAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysOperAccess.setStatus("mandatory")


class _CharPhysBits_Type(Integer32):
    """Custom type charPhysBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_CharPhysBits_Type.__name__ = "Integer32"
_CharPhysBits_Object = MibTableColumn
charPhysBits = _CharPhysBits_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 5),
    _CharPhysBits_Type()
)
charPhysBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysBits.setStatus("mandatory")


class _CharPhysParity_Type(Integer32):
    """Custom type charPhysParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("mark", 3),
          ("none", 1),
          ("odd", 4))
    )


_CharPhysParity_Type.__name__ = "Integer32"
_CharPhysParity_Object = MibTableColumn
charPhysParity = _CharPhysParity_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 6),
    _CharPhysParity_Type()
)
charPhysParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysParity.setStatus("mandatory")
_CharPhysSpeed_Type = Integer32
_CharPhysSpeed_Object = MibTableColumn
charPhysSpeed = _CharPhysSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 7),
    _CharPhysSpeed_Type()
)
charPhysSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysSpeed.setStatus("mandatory")


class _CharPhysModemControl_Type(Integer32):
    """Custom type charPhysModemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CharPhysModemControl_Type.__name__ = "Integer32"
_CharPhysModemControl_Object = MibTableColumn
charPhysModemControl = _CharPhysModemControl_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 8),
    _CharPhysModemControl_Type()
)
charPhysModemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysModemControl.setStatus("mandatory")


class _CharPhysSignalType_Type(Integer32):
    """Custom type charPhysSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("centronics", 2),
          ("dataproducts", 3),
          ("rs232", 1))
    )


_CharPhysSignalType_Type.__name__ = "Integer32"
_CharPhysSignalType_Object = MibTableColumn
charPhysSignalType = _CharPhysSignalType_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 9),
    _CharPhysSignalType_Type()
)
charPhysSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysSignalType.setStatus("mandatory")
_CharPhysInSignalNumber_Type = Integer32
_CharPhysInSignalNumber_Object = MibTableColumn
charPhysInSignalNumber = _CharPhysInSignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 10),
    _CharPhysInSignalNumber_Type()
)
charPhysInSignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysInSignalNumber.setStatus("mandatory")
_CharPhysOutSignalNumber_Type = Integer32
_CharPhysOutSignalNumber_Object = MibTableColumn
charPhysOutSignalNumber = _CharPhysOutSignalNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 11),
    _CharPhysOutSignalNumber_Type()
)
charPhysOutSignalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysOutSignalNumber.setStatus("mandatory")


class _CharPhysFlowControl_Type(Integer32):
    """Custom type charPhysFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cts", 2),
          ("dsr", 3),
          ("none", 1),
          ("xon", 4))
    )


_CharPhysFlowControl_Type.__name__ = "Integer32"
_CharPhysFlowControl_Object = MibTableColumn
charPhysFlowControl = _CharPhysFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 12),
    _CharPhysFlowControl_Type()
)
charPhysFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysFlowControl.setStatus("mandatory")


class _CharPhysInFlow_Type(Integer32):
    """Custom type charPhysInFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CharPhysInFlow_Type.__name__ = "Integer32"
_CharPhysInFlow_Object = MibTableColumn
charPhysInFlow = _CharPhysInFlow_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 13),
    _CharPhysInFlow_Type()
)
charPhysInFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysInFlow.setStatus("mandatory")


class _CharPhysOutFlow_Type(Integer32):
    """Custom type charPhysOutFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CharPhysOutFlow_Type.__name__ = "Integer32"
_CharPhysOutFlow_Object = MibTableColumn
charPhysOutFlow = _CharPhysOutFlow_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 14),
    _CharPhysOutFlow_Type()
)
charPhysOutFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysOutFlow.setStatus("mandatory")


class _CharPhysInFlowState_Type(Integer32):
    """Custom type charPhysInFlowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("go", 1),
          ("stop", 2))
    )


_CharPhysInFlowState_Type.__name__ = "Integer32"
_CharPhysInFlowState_Object = MibTableColumn
charPhysInFlowState = _CharPhysInFlowState_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 15),
    _CharPhysInFlowState_Type()
)
charPhysInFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysInFlowState.setStatus("mandatory")


class _CharPhysOutFlowState_Type(Integer32):
    """Custom type charPhysOutFlowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("go", 1),
          ("stop", 2))
    )


_CharPhysOutFlowState_Type.__name__ = "Integer32"
_CharPhysOutFlowState_Object = MibTableColumn
charPhysOutFlowState = _CharPhysOutFlowState_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 16),
    _CharPhysOutFlowState_Type()
)
charPhysOutFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysOutFlowState.setStatus("mandatory")


class _CharPhysAutobaud_Type(Integer32):
    """Custom type charPhysAutobaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CharPhysAutobaud_Type.__name__ = "Integer32"
_CharPhysAutobaud_Object = MibTableColumn
charPhysAutobaud = _CharPhysAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 17),
    _CharPhysAutobaud_Type()
)
charPhysAutobaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPhysAutobaud.setStatus("mandatory")
_CharPhysInCharacters_Type = Counter32
_CharPhysInCharacters_Object = MibTableColumn
charPhysInCharacters = _CharPhysInCharacters_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 18),
    _CharPhysInCharacters_Type()
)
charPhysInCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysInCharacters.setStatus("mandatory")
_CharPhysOutCharacters_Type = Counter32
_CharPhysOutCharacters_Object = MibTableColumn
charPhysOutCharacters = _CharPhysOutCharacters_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 19),
    _CharPhysOutCharacters_Type()
)
charPhysOutCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysOutCharacters.setStatus("mandatory")
_CharPhysFramingErrors_Type = Counter32
_CharPhysFramingErrors_Object = MibTableColumn
charPhysFramingErrors = _CharPhysFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 20),
    _CharPhysFramingErrors_Type()
)
charPhysFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysFramingErrors.setStatus("mandatory")
_CharPhysParityErrors_Type = Counter32
_CharPhysParityErrors_Object = MibTableColumn
charPhysParityErrors = _CharPhysParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 21),
    _CharPhysParityErrors_Type()
)
charPhysParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysParityErrors.setStatus("mandatory")
_CharPhysOverrunErrors_Type = Counter32
_CharPhysOverrunErrors_Object = MibTableColumn
charPhysOverrunErrors = _CharPhysOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 22),
    _CharPhysOverrunErrors_Type()
)
charPhysOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysOverrunErrors.setStatus("mandatory")


class _CharPhysLastInCharacter_Type(Integer32):
    """Custom type charPhysLastInCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CharPhysLastInCharacter_Type.__name__ = "Integer32"
_CharPhysLastInCharacter_Object = MibTableColumn
charPhysLastInCharacter = _CharPhysLastInCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 23),
    _CharPhysLastInCharacter_Type()
)
charPhysLastInCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysLastInCharacter.setStatus("mandatory")


class _CharPhysLastOutCharacter_Type(Integer32):
    """Custom type charPhysLastOutCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CharPhysLastOutCharacter_Type.__name__ = "Integer32"
_CharPhysLastOutCharacter_Object = MibTableColumn
charPhysLastOutCharacter = _CharPhysLastOutCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 24),
    _CharPhysLastOutCharacter_Type()
)
charPhysLastOutCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysLastOutCharacter.setStatus("mandatory")


class _CharPhysNode_Type(DisplayString):
    """Custom type charPhysNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CharPhysNode_Type.__name__ = "DisplayString"
_CharPhysNode_Object = MibTableColumn
charPhysNode = _CharPhysNode_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 25),
    _CharPhysNode_Type()
)
charPhysNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysNode.setStatus("mandatory")


class _CharPhysUserName_Type(DisplayString):
    """Custom type charPhysUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CharPhysUserName_Type.__name__ = "DisplayString"
_CharPhysUserName_Object = MibTableColumn
charPhysUserName = _CharPhysUserName_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 2, 1, 26),
    _CharPhysUserName_Type()
)
charPhysUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPhysUserName.setStatus("mandatory")
_CharPhysInSignalTable_Object = MibTable
charPhysInSignalTable = _CharPhysInSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 3)
)
if mibBuilder.loadTexts:
    charPhysInSignalTable.setStatus("mandatory")
_CharPhysInSignalEntry_Object = MibTableRow
charPhysInSignalEntry = _CharPhysInSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 3, 1)
)
charPhysInSignalEntry.setIndexNames(
    (0, "XYPLEX-MIB", "charInPhysIndex"),
    (0, "XYPLEX-MIB", "charInSignalName"),
)
if mibBuilder.loadTexts:
    charPhysInSignalEntry.setStatus("mandatory")
_CharInPhysIndex_Type = Integer32
_CharInPhysIndex_Object = MibTableColumn
charInPhysIndex = _CharInPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 3, 1, 1),
    _CharInPhysIndex_Type()
)
charInPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charInPhysIndex.setStatus("mandatory")


class _CharInSignalName_Type(DisplayString):
    """Custom type charInSignalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CharInSignalName_Type.__name__ = "DisplayString"
_CharInSignalName_Object = MibTableColumn
charInSignalName = _CharInSignalName_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 3, 1, 2),
    _CharInSignalName_Type()
)
charInSignalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charInSignalName.setStatus("mandatory")


class _CharInSignalState_Type(Integer32):
    """Custom type charInSignalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CharInSignalState_Type.__name__ = "Integer32"
_CharInSignalState_Object = MibTableColumn
charInSignalState = _CharInSignalState_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 3, 1, 3),
    _CharInSignalState_Type()
)
charInSignalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charInSignalState.setStatus("mandatory")
_CharPhysOutSignalTable_Object = MibTable
charPhysOutSignalTable = _CharPhysOutSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 4)
)
if mibBuilder.loadTexts:
    charPhysOutSignalTable.setStatus("mandatory")
_CharPhysOutSignalEntry_Object = MibTableRow
charPhysOutSignalEntry = _CharPhysOutSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 4, 1)
)
charPhysOutSignalEntry.setIndexNames(
    (0, "XYPLEX-MIB", "charOutPhysIndex"),
    (0, "XYPLEX-MIB", "charOutSignalName"),
)
if mibBuilder.loadTexts:
    charPhysOutSignalEntry.setStatus("mandatory")
_CharOutPhysIndex_Type = Integer32
_CharOutPhysIndex_Object = MibTableColumn
charOutPhysIndex = _CharOutPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 4, 1, 1),
    _CharOutPhysIndex_Type()
)
charOutPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charOutPhysIndex.setStatus("mandatory")


class _CharOutSignalName_Type(DisplayString):
    """Custom type charOutSignalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CharOutSignalName_Type.__name__ = "DisplayString"
_CharOutSignalName_Object = MibTableColumn
charOutSignalName = _CharOutSignalName_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 4, 1, 2),
    _CharOutSignalName_Type()
)
charOutSignalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charOutSignalName.setStatus("mandatory")


class _CharOutSignalState_Type(Integer32):
    """Custom type charOutSignalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CharOutSignalState_Type.__name__ = "Integer32"
_CharOutSignalState_Object = MibTableColumn
charOutSignalState = _CharOutSignalState_Object(
    (1, 3, 6, 1, 4, 1, 33, 2, 4, 1, 3),
    _CharOutSignalState_Type()
)
charOutSignalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charOutSignalState.setStatus("mandatory")
_XInternet_ObjectIdentity = ObjectIdentity
xInternet = _XInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 4)
)


class _IntDomainSuffix_Type(DisplayString):
    """Custom type intDomainSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 115),
    )


_IntDomainSuffix_Type.__name__ = "DisplayString"
_IntDomainSuffix_Object = MibScalar
intDomainSuffix = _IntDomainSuffix_Object(
    (1, 3, 6, 1, 4, 1, 33, 4, 1),
    _IntDomainSuffix_Type()
)
intDomainSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intDomainSuffix.setStatus("mandatory")
_IntDomainAddress1_Type = IpAddress
_IntDomainAddress1_Object = MibScalar
intDomainAddress1 = _IntDomainAddress1_Object(
    (1, 3, 6, 1, 4, 1, 33, 4, 2),
    _IntDomainAddress1_Type()
)
intDomainAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intDomainAddress1.setStatus("mandatory")
_IntDomainAddress2_Type = IpAddress
_IntDomainAddress2_Object = MibScalar
intDomainAddress2 = _IntDomainAddress2_Object(
    (1, 3, 6, 1, 4, 1, 33, 4, 3),
    _IntDomainAddress2_Type()
)
intDomainAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intDomainAddress2.setStatus("mandatory")
_IntGatewayAddress1_Type = IpAddress
_IntGatewayAddress1_Object = MibScalar
intGatewayAddress1 = _IntGatewayAddress1_Object(
    (1, 3, 6, 1, 4, 1, 33, 4, 4),
    _IntGatewayAddress1_Type()
)
intGatewayAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intGatewayAddress1.setStatus("mandatory")
_IntGatewayAddress2_Type = IpAddress
_IntGatewayAddress2_Object = MibScalar
intGatewayAddress2 = _IntGatewayAddress2_Object(
    (1, 3, 6, 1, 4, 1, 33, 4, 5),
    _IntGatewayAddress2_Type()
)
intGatewayAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intGatewayAddress2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYPLEX-MIB",
    **{"xyplex": xyplex,
       "system": system,
       "sysIdent": sysIdent,
       "character": character,
       "charPhysNumber": charPhysNumber,
       "charPhysTable": charPhysTable,
       "charPhysEntry": charPhysEntry,
       "charPhysIndex": charPhysIndex,
       "charPhysPortName": charPhysPortName,
       "charPhysAdminAccess": charPhysAdminAccess,
       "charPhysOperAccess": charPhysOperAccess,
       "charPhysBits": charPhysBits,
       "charPhysParity": charPhysParity,
       "charPhysSpeed": charPhysSpeed,
       "charPhysModemControl": charPhysModemControl,
       "charPhysSignalType": charPhysSignalType,
       "charPhysInSignalNumber": charPhysInSignalNumber,
       "charPhysOutSignalNumber": charPhysOutSignalNumber,
       "charPhysFlowControl": charPhysFlowControl,
       "charPhysInFlow": charPhysInFlow,
       "charPhysOutFlow": charPhysOutFlow,
       "charPhysInFlowState": charPhysInFlowState,
       "charPhysOutFlowState": charPhysOutFlowState,
       "charPhysAutobaud": charPhysAutobaud,
       "charPhysInCharacters": charPhysInCharacters,
       "charPhysOutCharacters": charPhysOutCharacters,
       "charPhysFramingErrors": charPhysFramingErrors,
       "charPhysParityErrors": charPhysParityErrors,
       "charPhysOverrunErrors": charPhysOverrunErrors,
       "charPhysLastInCharacter": charPhysLastInCharacter,
       "charPhysLastOutCharacter": charPhysLastOutCharacter,
       "charPhysNode": charPhysNode,
       "charPhysUserName": charPhysUserName,
       "charPhysInSignalTable": charPhysInSignalTable,
       "charPhysInSignalEntry": charPhysInSignalEntry,
       "charInPhysIndex": charInPhysIndex,
       "charInSignalName": charInSignalName,
       "charInSignalState": charInSignalState,
       "charPhysOutSignalTable": charPhysOutSignalTable,
       "charPhysOutSignalEntry": charPhysOutSignalEntry,
       "charOutPhysIndex": charOutPhysIndex,
       "charOutSignalName": charOutSignalName,
       "charOutSignalState": charOutSignalState,
       "xInternet": xInternet,
       "intDomainSuffix": intDomainSuffix,
       "intDomainAddress1": intDomainAddress1,
       "intDomainAddress2": intDomainAddress2,
       "intGatewayAddress1": intGatewayAddress1,
       "intGatewayAddress2": intGatewayAddress2}
)
