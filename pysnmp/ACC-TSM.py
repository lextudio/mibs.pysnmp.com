# SNMP MIB module (ACC-TSM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-TSM
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:06 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
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

_AccTsmGroup_ObjectIdentity = ObjectIdentity
accTsmGroup = _AccTsmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56)
)
_AccTsmTable_Object = MibTable
accTsmTable = _AccTsmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 1)
)
if mibBuilder.loadTexts:
    accTsmTable.setStatus("mandatory")
_AccTsmTableEntry_Object = MibTableRow
accTsmTableEntry = _AccTsmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 1, 1)
)
accTsmTableEntry.setIndexNames(
    (0, "ACC-TSM", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    accTsmTableEntry.setStatus("mandatory")
_AccTsmLdxIndex_Type = Integer32
_AccTsmLdxIndex_Object = MibTableColumn
accTsmLdxIndex = _AccTsmLdxIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 1, 1, 1),
    _AccTsmLdxIndex_Type()
)
accTsmLdxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmLdxIndex.setStatus("mandatory")
_AccTsmMsgLevel_Type = Integer32
_AccTsmMsgLevel_Object = MibTableColumn
accTsmMsgLevel = _AccTsmMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 1, 1, 2),
    _AccTsmMsgLevel_Type()
)
accTsmMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTsmMsgLevel.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 1, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_AccTsmSwitchTable_Object = MibTable
accTsmSwitchTable = _AccTsmSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2)
)
if mibBuilder.loadTexts:
    accTsmSwitchTable.setStatus("mandatory")
_AccTsmSwitchTableEntry_Object = MibTableRow
accTsmSwitchTableEntry = _AccTsmSwitchTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2, 1)
)
accTsmSwitchTableEntry.setIndexNames(
    (0, "ACC-TSM", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    accTsmSwitchTableEntry.setStatus("mandatory")
_AccTsmSwitchingId_Type = Integer32
_AccTsmSwitchingId_Object = MibTableColumn
accTsmSwitchingId = _AccTsmSwitchingId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2, 1, 1),
    _AccTsmSwitchingId_Type()
)
accTsmSwitchingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTsmSwitchingId.setStatus("mandatory")
_AccTsmLocStream_Type = OctetString
_AccTsmLocStream_Object = MibTableColumn
accTsmLocStream = _AccTsmLocStream_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2, 1, 2),
    _AccTsmLocStream_Type()
)
accTsmLocStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmLocStream.setStatus("mandatory")
_AccTsmLocTimeslot_Type = OctetString
_AccTsmLocTimeslot_Object = MibTableColumn
accTsmLocTimeslot = _AccTsmLocTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2, 1, 3),
    _AccTsmLocTimeslot_Type()
)
accTsmLocTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmLocTimeslot.setStatus("mandatory")
_AccTsmTdmStream_Type = OctetString
_AccTsmTdmStream_Object = MibTableColumn
accTsmTdmStream = _AccTsmTdmStream_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2, 1, 4),
    _AccTsmTdmStream_Type()
)
accTsmTdmStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmTdmStream.setStatus("mandatory")
_AccTsmTdmTimeslot_Type = OctetString
_AccTsmTdmTimeslot_Object = MibTableColumn
accTsmTdmTimeslot = _AccTsmTdmTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2, 1, 5),
    _AccTsmTdmTimeslot_Type()
)
accTsmTdmTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmTdmTimeslot.setStatus("mandatory")
_AccTsmSrcCkt_Type = Integer32
_AccTsmSrcCkt_Object = MibTableColumn
accTsmSrcCkt = _AccTsmSrcCkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2, 1, 6),
    _AccTsmSrcCkt_Type()
)
accTsmSrcCkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmSrcCkt.setStatus("mandatory")
_AccTsmDstCkt_Type = Integer32
_AccTsmDstCkt_Object = MibTableColumn
accTsmDstCkt = _AccTsmDstCkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2, 1, 7),
    _AccTsmDstCkt_Type()
)
accTsmDstCkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmDstCkt.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 2, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_AccTsmTest_Type = Integer32
_AccTsmTest_Object = MibScalar
accTsmTest = _AccTsmTest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 3),
    _AccTsmTest_Type()
)
accTsmTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTsmTest.setStatus("mandatory")
_AccSsuSrcTable_Object = MibTable
accSsuSrcTable = _AccSsuSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4)
)
if mibBuilder.loadTexts:
    accSsuSrcTable.setStatus("mandatory")
_AccSsuSrcEntry_Object = MibTableRow
accSsuSrcEntry = _AccSsuSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4, 1)
)
accSsuSrcEntry.setIndexNames(
    (0, "ACC-TSM", "accSsuSrcType"),
    (0, "ACC-TSM", "accSsuSrcIfIndex"),
)
if mibBuilder.loadTexts:
    accSsuSrcEntry.setStatus("mandatory")


class _AccSsuSrcType_Type(Integer32):
    """Custom type accSsuSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("derived", 2),
          ("external", 1),
          ("internal", 3))
    )


_AccSsuSrcType_Type.__name__ = "Integer32"
_AccSsuSrcType_Object = MibTableColumn
accSsuSrcType = _AccSsuSrcType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4, 1, 1),
    _AccSsuSrcType_Type()
)
accSsuSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSsuSrcType.setStatus("mandatory")
_AccSsuSrcIfIndex_Type = Integer32
_AccSsuSrcIfIndex_Object = MibTableColumn
accSsuSrcIfIndex = _AccSsuSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4, 1, 2),
    _AccSsuSrcIfIndex_Type()
)
accSsuSrcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSsuSrcIfIndex.setStatus("mandatory")


class _AccSsuSrcPriority_Type(Integer32):
    """Custom type accSsuSrcPriority based on Integer32"""
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
        *(("disabled", 4),
          ("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_AccSsuSrcPriority_Type.__name__ = "Integer32"
_AccSsuSrcPriority_Object = MibTableColumn
accSsuSrcPriority = _AccSsuSrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4, 1, 3),
    _AccSsuSrcPriority_Type()
)
accSsuSrcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSsuSrcPriority.setStatus("mandatory")
_AccSsuSrcFrequency_Type = Integer32
_AccSsuSrcFrequency_Object = MibTableColumn
accSsuSrcFrequency = _AccSsuSrcFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4, 1, 4),
    _AccSsuSrcFrequency_Type()
)
accSsuSrcFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSsuSrcFrequency.setStatus("mandatory")


class _AccSsuSrcRecovery_Type(Integer32):
    """Custom type accSsuSrcRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_AccSsuSrcRecovery_Type.__name__ = "Integer32"
_AccSsuSrcRecovery_Object = MibTableColumn
accSsuSrcRecovery = _AccSsuSrcRecovery_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4, 1, 5),
    _AccSsuSrcRecovery_Type()
)
accSsuSrcRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSsuSrcRecovery.setStatus("mandatory")
_AccSsuSrcThreshold_Type = Integer32
_AccSsuSrcThreshold_Object = MibTableColumn
accSsuSrcThreshold = _AccSsuSrcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4, 1, 6),
    _AccSsuSrcThreshold_Type()
)
accSsuSrcThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSsuSrcThreshold.setStatus("mandatory")


class _AccSsuSrcState_Type(Integer32):
    """Custom type accSsuSrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("disabled-not-ready", 5),
          ("disabled-ready", 4),
          ("not-ready", 3),
          ("ready", 2))
    )


_AccSsuSrcState_Type.__name__ = "Integer32"
_AccSsuSrcState_Object = MibTableColumn
accSsuSrcState = _AccSsuSrcState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4, 1, 7),
    _AccSsuSrcState_Type()
)
accSsuSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSsuSrcState.setStatus("mandatory")
_AccSsuSrcFailures_Type = Counter32
_AccSsuSrcFailures_Object = MibTableColumn
accSsuSrcFailures = _AccSsuSrcFailures_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 4, 1, 8),
    _AccSsuSrcFailures_Type()
)
accSsuSrcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSsuSrcFailures.setStatus("mandatory")
_AccTsmDITable_Object = MibTable
accTsmDITable = _AccTsmDITable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 5)
)
if mibBuilder.loadTexts:
    accTsmDITable.setStatus("mandatory")
_AccTsmDIEntry_Object = MibTableRow
accTsmDIEntry = _AccTsmDIEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 5, 1)
)
accTsmDIEntry.setIndexNames(
    (0, "ACC-TSM", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    accTsmDIEntry.setStatus("mandatory")
_AccTsmDIId_Type = Integer32
_AccTsmDIId_Object = MibTableColumn
accTsmDIId = _AccTsmDIId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 5, 1, 1),
    _AccTsmDIId_Type()
)
accTsmDIId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmDIId.setStatus("mandatory")
_AccTsmDIFromDS0_Type = Integer32
_AccTsmDIFromDS0_Object = MibTableColumn
accTsmDIFromDS0 = _AccTsmDIFromDS0_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 5, 1, 2),
    _AccTsmDIFromDS0_Type()
)
accTsmDIFromDS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmDIFromDS0.setStatus("mandatory")
_AccTsmDIFromDS1_Type = Integer32
_AccTsmDIFromDS1_Object = MibTableColumn
accTsmDIFromDS1 = _AccTsmDIFromDS1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 5, 1, 3),
    _AccTsmDIFromDS1_Type()
)
accTsmDIFromDS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmDIFromDS1.setStatus("mandatory")
_AccTsmDIToDS0_Type = Integer32
_AccTsmDIToDS0_Object = MibTableColumn
accTsmDIToDS0 = _AccTsmDIToDS0_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 5, 1, 4),
    _AccTsmDIToDS0_Type()
)
accTsmDIToDS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmDIToDS0.setStatus("mandatory")
_AccTsmDIToDS1_Type = Integer32
_AccTsmDIToDS1_Object = MibTableColumn
accTsmDIToDS1 = _AccTsmDIToDS1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 5, 1, 5),
    _AccTsmDIToDS1_Type()
)
accTsmDIToDS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmDIToDS1.setStatus("mandatory")


class _AccTsmDIRowStatus_Type(Integer32):
    """Custom type accTsmDIRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccTsmDIRowStatus_Type.__name__ = "Integer32"
_AccTsmDIRowStatus_Object = MibTableColumn
accTsmDIRowStatus = _AccTsmDIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 5, 1, 6),
    _AccTsmDIRowStatus_Type()
)
accTsmDIRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTsmDIRowStatus.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 56, 5, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-TSM",
    **{"accTsmGroup": accTsmGroup,
       "accTsmTable": accTsmTable,
       "accTsmTableEntry": accTsmTableEntry,
       "accTsmLdxIndex": accTsmLdxIndex,
       "accTsmMsgLevel": accTsmMsgLevel,
       "pysmiFakeCol1": pysmiFakeCol1,
       "accTsmSwitchTable": accTsmSwitchTable,
       "accTsmSwitchTableEntry": accTsmSwitchTableEntry,
       "accTsmSwitchingId": accTsmSwitchingId,
       "accTsmLocStream": accTsmLocStream,
       "accTsmLocTimeslot": accTsmLocTimeslot,
       "accTsmTdmStream": accTsmTdmStream,
       "accTsmTdmTimeslot": accTsmTdmTimeslot,
       "accTsmSrcCkt": accTsmSrcCkt,
       "accTsmDstCkt": accTsmDstCkt,
       "pysmiFakeCol2": pysmiFakeCol2,
       "accTsmTest": accTsmTest,
       "accSsuSrcTable": accSsuSrcTable,
       "accSsuSrcEntry": accSsuSrcEntry,
       "accSsuSrcType": accSsuSrcType,
       "accSsuSrcIfIndex": accSsuSrcIfIndex,
       "accSsuSrcPriority": accSsuSrcPriority,
       "accSsuSrcFrequency": accSsuSrcFrequency,
       "accSsuSrcRecovery": accSsuSrcRecovery,
       "accSsuSrcThreshold": accSsuSrcThreshold,
       "accSsuSrcState": accSsuSrcState,
       "accSsuSrcFailures": accSsuSrcFailures,
       "accTsmDITable": accTsmDITable,
       "accTsmDIEntry": accTsmDIEntry,
       "accTsmDIId": accTsmDIId,
       "accTsmDIFromDS0": accTsmDIFromDS0,
       "accTsmDIFromDS1": accTsmDIFromDS1,
       "accTsmDIToDS0": accTsmDIToDS0,
       "accTsmDIToDS1": accTsmDIToDS1,
       "accTsmDIRowStatus": accTsmDIRowStatus,
       "pysmiFakeCol3": pysmiFakeCol3}
)
