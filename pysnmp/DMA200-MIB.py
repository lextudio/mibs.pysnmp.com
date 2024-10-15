# SNMP MIB module (DMA200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DMA200-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:40 2024
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
 NotificationType,
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
    "NotificationType",
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

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Sc_ObjectIdentity = ObjectIdentity
sc = _Sc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3)
)
_DmaSystem_ObjectIdentity = ObjectIdentity
dmaSystem = _DmaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 7)
)
_DmaMaster_ObjectIdentity = ObjectIdentity
dmaMaster = _DmaMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1)
)


class _DmaMasterFSterminate_Type(Integer32):
    """Custom type dmaMasterFSterminate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disconnect", 1)
    )


_DmaMasterFSterminate_Type.__name__ = "Integer32"
_DmaMasterFSterminate_Object = MibScalar
dmaMasterFSterminate = _DmaMasterFSterminate_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 1),
    _DmaMasterFSterminate_Type()
)
dmaMasterFSterminate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dmaMasterFSterminate.setStatus("mandatory")


class _DmaMasterSupvAccess_Type(Integer32):
    """Custom type dmaMasterSupvAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("local", 2),
          ("none", 1))
    )


_DmaMasterSupvAccess_Type.__name__ = "Integer32"
_DmaMasterSupvAccess_Object = MibScalar
dmaMasterSupvAccess = _DmaMasterSupvAccess_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 2),
    _DmaMasterSupvAccess_Type()
)
dmaMasterSupvAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmaMasterSupvAccess.setStatus("mandatory")


class _DmaMasterModemCmd_Type(DisplayString):
    """Custom type dmaMasterModemCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DmaMasterModemCmd_Type.__name__ = "DisplayString"
_DmaMasterModemCmd_Object = MibScalar
dmaMasterModemCmd = _DmaMasterModemCmd_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 3),
    _DmaMasterModemCmd_Type()
)
dmaMasterModemCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaMasterModemCmd.setStatus("mandatory")


class _DmaMasterDialPrefix_Type(DisplayString):
    """Custom type dmaMasterDialPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DmaMasterDialPrefix_Type.__name__ = "DisplayString"
_DmaMasterDialPrefix_Object = MibScalar
dmaMasterDialPrefix = _DmaMasterDialPrefix_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 4),
    _DmaMasterDialPrefix_Type()
)
dmaMasterDialPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaMasterDialPrefix.setStatus("mandatory")


class _DmaMasterDialPhoneNumber_Type(DisplayString):
    """Custom type dmaMasterDialPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DmaMasterDialPhoneNumber_Type.__name__ = "DisplayString"
_DmaMasterDialPhoneNumber_Object = MibScalar
dmaMasterDialPhoneNumber = _DmaMasterDialPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 5),
    _DmaMasterDialPhoneNumber_Type()
)
dmaMasterDialPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaMasterDialPhoneNumber.setStatus("mandatory")


class _DmaMasterDialing_Type(Integer32):
    """Custom type dmaMasterDialing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("disconnect", 2))
    )


_DmaMasterDialing_Type.__name__ = "Integer32"
_DmaMasterDialing_Object = MibScalar
dmaMasterDialing = _DmaMasterDialing_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 6),
    _DmaMasterDialing_Type()
)
dmaMasterDialing.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dmaMasterDialing.setStatus("mandatory")


class _DmaMasterDialPortStatus_Type(Integer32):
    """Custom type dmaMasterDialPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connectedOnline", 3),
          ("dialing", 2),
          ("readyOffline", 1))
    )


_DmaMasterDialPortStatus_Type.__name__ = "Integer32"
_DmaMasterDialPortStatus_Object = MibScalar
dmaMasterDialPortStatus = _DmaMasterDialPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 7),
    _DmaMasterDialPortStatus_Type()
)
dmaMasterDialPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmaMasterDialPortStatus.setStatus("mandatory")
_DmaMasterResumeScan_Type = Integer32
_DmaMasterResumeScan_Object = MibScalar
dmaMasterResumeScan = _DmaMasterResumeScan_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 8),
    _DmaMasterResumeScan_Type()
)
dmaMasterResumeScan.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dmaMasterResumeScan.setStatus("mandatory")


class _DmaMasterScanCtrl_Type(Integer32):
    """Custom type dmaMasterScanCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dmaScanOff", 1),
          ("dmaScanOn", 2))
    )


_DmaMasterScanCtrl_Type.__name__ = "Integer32"
_DmaMasterScanCtrl_Object = MibScalar
dmaMasterScanCtrl = _DmaMasterScanCtrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 9),
    _DmaMasterScanCtrl_Type()
)
dmaMasterScanCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaMasterScanCtrl.setStatus("mandatory")
_DmaNode_ObjectIdentity = ObjectIdentity
dmaNode = _DmaNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 2)
)
_DmaNodeNum_Type = Integer32
_DmaNodeNum_Object = MibScalar
dmaNodeNum = _DmaNodeNum_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 1),
    _DmaNodeNum_Type()
)
dmaNodeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmaNodeNum.setStatus("mandatory")
_DmaNodeTable_Object = MibTable
dmaNodeTable = _DmaNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2)
)
if mibBuilder.loadTexts:
    dmaNodeTable.setStatus("mandatory")
_DmaNodeEntry_Object = MibTableRow
dmaNodeEntry = _DmaNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1)
)
dmaNodeEntry.setIndexNames(
    (0, "DMA200-MIB", "dmaNodeIndex"),
)
if mibBuilder.loadTexts:
    dmaNodeEntry.setStatus("mandatory")


class _DmaNodeIndex_Type(Integer32):
    """Custom type dmaNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DmaNodeIndex_Type.__name__ = "Integer32"
_DmaNodeIndex_Object = MibTableColumn
dmaNodeIndex = _DmaNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1, 1),
    _DmaNodeIndex_Type()
)
dmaNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmaNodeIndex.setStatus("mandatory")


class _DmaNodeValid_Type(Integer32):
    """Custom type dmaNodeValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_DmaNodeValid_Type.__name__ = "Integer32"
_DmaNodeValid_Object = MibTableColumn
dmaNodeValid = _DmaNodeValid_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1, 2),
    _DmaNodeValid_Type()
)
dmaNodeValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaNodeValid.setStatus("mandatory")


class _DmaNodePhoneNumber_Type(DisplayString):
    """Custom type dmaNodePhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DmaNodePhoneNumber_Type.__name__ = "DisplayString"
_DmaNodePhoneNumber_Object = MibTableColumn
dmaNodePhoneNumber = _DmaNodePhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1, 3),
    _DmaNodePhoneNumber_Type()
)
dmaNodePhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaNodePhoneNumber.setStatus("mandatory")


class _DmaNodeName_Type(DisplayString):
    """Custom type dmaNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DmaNodeName_Type.__name__ = "DisplayString"
_DmaNodeName_Object = MibTableColumn
dmaNodeName = _DmaNodeName_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1, 4),
    _DmaNodeName_Type()
)
dmaNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaNodeName.setStatus("mandatory")
_DmaElement_ObjectIdentity = ObjectIdentity
dmaElement = _DmaElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 3)
)
_DmaElementConfigTable_Object = MibTable
dmaElementConfigTable = _DmaElementConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1)
)
if mibBuilder.loadTexts:
    dmaElementConfigTable.setStatus("mandatory")
_DmaElementEntry_Object = MibTableRow
dmaElementEntry = _DmaElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1)
)
dmaElementEntry.setIndexNames(
    (0, "DMA200-MIB", "dmaElementIndex"),
)
if mibBuilder.loadTexts:
    dmaElementEntry.setStatus("mandatory")


class _DmaElementIndex_Type(Integer32):
    """Custom type dmaElementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmaElementIndex_Type.__name__ = "Integer32"
_DmaElementIndex_Object = MibTableColumn
dmaElementIndex = _DmaElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 1),
    _DmaElementIndex_Type()
)
dmaElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmaElementIndex.setStatus("mandatory")


class _DmaElementRemoteIndex_Type(Integer32):
    """Custom type dmaElementRemoteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmaElementRemoteIndex_Type.__name__ = "Integer32"
_DmaElementRemoteIndex_Object = MibTableColumn
dmaElementRemoteIndex = _DmaElementRemoteIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 2),
    _DmaElementRemoteIndex_Type()
)
dmaElementRemoteIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaElementRemoteIndex.setStatus("mandatory")


class _DmaElementValid_Type(Integer32):
    """Custom type dmaElementValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_DmaElementValid_Type.__name__ = "Integer32"
_DmaElementValid_Object = MibTableColumn
dmaElementValid = _DmaElementValid_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 3),
    _DmaElementValid_Type()
)
dmaElementValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaElementValid.setStatus("mandatory")


class _DmaElementType_Type(Integer32):
    """Custom type dmaElementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dc551", 2),
          ("dc552A", 3),
          ("dc552A-1", 4),
          ("dc552A-1-V11", 6),
          ("dc552A-V11", 5),
          ("other", 1))
    )


_DmaElementType_Type.__name__ = "Integer32"
_DmaElementType_Object = MibTableColumn
dmaElementType = _DmaElementType_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 4),
    _DmaElementType_Type()
)
dmaElementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaElementType.setStatus("mandatory")


class _DmaElementStatus_Type(Integer32):
    """Custom type dmaElementStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("statusCommErr", 5),
          ("statusMajor", 2),
          ("statusMinor", 3),
          ("statusMismatchDC551", 6),
          ("statusMismatchDC552A", 7),
          ("statusMismatchDC552A-1", 8),
          ("statusMismatchDC552A-1-V11", 10),
          ("statusMismatchDC552A-V11", 9),
          ("statusNotResponding", 4),
          ("statusOK", 1))
    )


_DmaElementStatus_Type.__name__ = "Integer32"
_DmaElementStatus_Object = MibTableColumn
dmaElementStatus = _DmaElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 5),
    _DmaElementStatus_Type()
)
dmaElementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmaElementStatus.setStatus("mandatory")
_DmaElementNode_Type = Integer32
_DmaElementNode_Object = MibTableColumn
dmaElementNode = _DmaElementNode_Object(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 6),
    _DmaElementNode_Type()
)
dmaElementNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmaElementNode.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dmaAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 0, 1)
)
dmaAccess.setObjects(
    ("DMA200-MIB", "dmaMasterSupvAccess")
)
if mibBuilder.loadTexts:
    dmaAccess.setStatus(
        ""
    )

dmaElementAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 3, 7, 0, 2)
)
dmaElementAlarm.setObjects(
      *(("DMA200-MIB", "dmaElementIndex"),
        ("DMA200-MIB", "dmaElementType"),
        ("DMA200-MIB", "dmaElementStatus"),
        ("DMA200-MIB", "dmaNodeName"))
)
if mibBuilder.loadTexts:
    dmaElementAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMA200-MIB",
    **{"gdc": gdc,
       "sc": sc,
       "dmaSystem": dmaSystem,
       "dmaAccess": dmaAccess,
       "dmaElementAlarm": dmaElementAlarm,
       "dmaMaster": dmaMaster,
       "dmaMasterFSterminate": dmaMasterFSterminate,
       "dmaMasterSupvAccess": dmaMasterSupvAccess,
       "dmaMasterModemCmd": dmaMasterModemCmd,
       "dmaMasterDialPrefix": dmaMasterDialPrefix,
       "dmaMasterDialPhoneNumber": dmaMasterDialPhoneNumber,
       "dmaMasterDialing": dmaMasterDialing,
       "dmaMasterDialPortStatus": dmaMasterDialPortStatus,
       "dmaMasterResumeScan": dmaMasterResumeScan,
       "dmaMasterScanCtrl": dmaMasterScanCtrl,
       "dmaNode": dmaNode,
       "dmaNodeNum": dmaNodeNum,
       "dmaNodeTable": dmaNodeTable,
       "dmaNodeEntry": dmaNodeEntry,
       "dmaNodeIndex": dmaNodeIndex,
       "dmaNodeValid": dmaNodeValid,
       "dmaNodePhoneNumber": dmaNodePhoneNumber,
       "dmaNodeName": dmaNodeName,
       "dmaElement": dmaElement,
       "dmaElementConfigTable": dmaElementConfigTable,
       "dmaElementEntry": dmaElementEntry,
       "dmaElementIndex": dmaElementIndex,
       "dmaElementRemoteIndex": dmaElementRemoteIndex,
       "dmaElementValid": dmaElementValid,
       "dmaElementType": dmaElementType,
       "dmaElementStatus": dmaElementStatus,
       "dmaElementNode": dmaElementNode}
)
