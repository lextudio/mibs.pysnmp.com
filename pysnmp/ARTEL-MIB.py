# SNMP MIB module (ARTEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARTEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:42 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Artel_ObjectIdentity = ObjectIdentity
artel = _Artel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139)
)
_Node_ObjectIdentity = ObjectIdentity
node = _Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 1)
)


class _NodeName_Type(DisplayString):
    """Custom type nodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NodeName_Type.__name__ = "DisplayString"
_NodeName_Object = MibScalar
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 139, 1, 1),
    _NodeName_Type()
)
nodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeName.setStatus("mandatory")
_NodeMacSlotMap_Type = Opaque
_NodeMacSlotMap_Object = MibScalar
nodeMacSlotMap = _NodeMacSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 139, 1, 2),
    _NodeMacSlotMap_Type()
)
nodeMacSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMacSlotMap.setStatus("mandatory")
_NodeColdBoot_Type = Integer32
_NodeColdBoot_Object = MibScalar
nodeColdBoot = _NodeColdBoot_Object(
    (1, 3, 6, 1, 4, 1, 139, 1, 3),
    _NodeColdBoot_Type()
)
nodeColdBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeColdBoot.setStatus("mandatory")
_NodeResetNvRam_Type = Integer32
_NodeResetNvRam_Object = MibScalar
nodeResetNvRam = _NodeResetNvRam_Object(
    (1, 3, 6, 1, 4, 1, 139, 1, 4),
    _NodeResetNvRam_Type()
)
nodeResetNvRam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeResetNvRam.setStatus("mandatory")
_NodeIpSlotTable_Object = MibTable
nodeIpSlotTable = _NodeIpSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 1, 5)
)
if mibBuilder.loadTexts:
    nodeIpSlotTable.setStatus("mandatory")
_NodeIpSlotEntry_Object = MibTableRow
nodeIpSlotEntry = _NodeIpSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 1, 5, 1)
)
nodeIpSlotEntry.setIndexNames(
    (0, "ARTEL-MIB", "nodeIpSlotIndex"),
)
if mibBuilder.loadTexts:
    nodeIpSlotEntry.setStatus("mandatory")


class _NodeIpSlotIndex_Type(Integer32):
    """Custom type nodeIpSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_NodeIpSlotIndex_Type.__name__ = "Integer32"
_NodeIpSlotIndex_Object = MibTableColumn
nodeIpSlotIndex = _NodeIpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 1, 5, 1, 1),
    _NodeIpSlotIndex_Type()
)
nodeIpSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIpSlotIndex.setStatus("mandatory")
_NodeIpSlotAddr_Type = IpAddress
_NodeIpSlotAddr_Object = MibTableColumn
nodeIpSlotAddr = _NodeIpSlotAddr_Object(
    (1, 3, 6, 1, 4, 1, 139, 1, 5, 1, 2),
    _NodeIpSlotAddr_Type()
)
nodeIpSlotAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeIpSlotAddr.setStatus("mandatory")
_Galactica_ObjectIdentity = ObjectIdentity
galactica = _Galactica_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2)
)
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 1)
)
_BoardIpAddr_Type = IpAddress
_BoardIpAddr_Object = MibScalar
boardIpAddr = _BoardIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 1, 1),
    _BoardIpAddr_Type()
)
boardIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardIpAddr.setStatus("mandatory")
_BoardReset_Type = Integer32
_BoardReset_Object = MibScalar
boardReset = _BoardReset_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 1, 3),
    _BoardReset_Type()
)
boardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardReset.setStatus("mandatory")
_BoardResetNvRam_Type = Integer32
_BoardResetNvRam_Object = MibScalar
boardResetNvRam = _BoardResetNvRam_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 1, 4),
    _BoardResetNvRam_Type()
)
boardResetNvRam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardResetNvRam.setStatus("mandatory")
_BoardLedStatus_Type = Integer32
_BoardLedStatus_Object = MibScalar
boardLedStatus = _BoardLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 1, 5),
    _BoardLedStatus_Type()
)
boardLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardLedStatus.setStatus("mandatory")
_BoardSlotNum_Type = Integer32
_BoardSlotNum_Object = MibScalar
boardSlotNum = _BoardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 1, 6),
    _BoardSlotNum_Type()
)
boardSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSlotNum.setStatus("mandatory")


class _BoardClass_Type(Integer32):
    """Custom type boardClass based on Integer32"""
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
        *(("fddi-board", 4),
          ("starbridge-board", 2),
          ("system-management-board", 1),
          ("turbo", 3))
    )


_BoardClass_Type.__name__ = "Integer32"
_BoardClass_Object = MibScalar
boardClass = _BoardClass_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 1, 7),
    _BoardClass_Type()
)
boardClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardClass.setStatus("mandatory")
_BoardResetCounts_Type = Counter32
_BoardResetCounts_Object = MibScalar
boardResetCounts = _BoardResetCounts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 1, 8),
    _BoardResetCounts_Type()
)
boardResetCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardResetCounts.setStatus("mandatory")


class _BoardSnmpMibVersion_Type(DisplayString):
    """Custom type boardSnmpMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BoardSnmpMibVersion_Type.__name__ = "DisplayString"
_BoardSnmpMibVersion_Object = MibScalar
boardSnmpMibVersion = _BoardSnmpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 1, 9),
    _BoardSnmpMibVersion_Type()
)
boardSnmpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSnmpMibVersion.setStatus("mandatory")
_Arcnet_ObjectIdentity = ObjectIdentity
arcnet = _Arcnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 2)
)
_ArcnetBoardsPresent_Type = Integer32
_ArcnetBoardsPresent_Object = MibScalar
arcnetBoardsPresent = _ArcnetBoardsPresent_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 2, 1),
    _ArcnetBoardsPresent_Type()
)
arcnetBoardsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcnetBoardsPresent.setStatus("mandatory")
_ArcnetRxPkts_Type = Counter32
_ArcnetRxPkts_Object = MibScalar
arcnetRxPkts = _ArcnetRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 2, 2),
    _ArcnetRxPkts_Type()
)
arcnetRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcnetRxPkts.setStatus("mandatory")
_ArcnetTxPkts_Type = Counter32
_ArcnetTxPkts_Object = MibScalar
arcnetTxPkts = _ArcnetTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 2, 3),
    _ArcnetTxPkts_Type()
)
arcnetTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcnetTxPkts.setStatus("mandatory")
_ArcnetNakCnts_Type = Counter32
_ArcnetNakCnts_Object = MibScalar
arcnetNakCnts = _ArcnetNakCnts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 2, 4),
    _ArcnetNakCnts_Type()
)
arcnetNakCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcnetNakCnts.setStatus("mandatory")
_ArcnetMyReconfigCounts_Type = Counter32
_ArcnetMyReconfigCounts_Object = MibScalar
arcnetMyReconfigCounts = _ArcnetMyReconfigCounts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 2, 5),
    _ArcnetMyReconfigCounts_Type()
)
arcnetMyReconfigCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcnetMyReconfigCounts.setStatus("mandatory")
_ArcnetReconfigCounts_Type = Counter32
_ArcnetReconfigCounts_Object = MibScalar
arcnetReconfigCounts = _ArcnetReconfigCounts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 2, 6),
    _ArcnetReconfigCounts_Type()
)
arcnetReconfigCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcnetReconfigCounts.setStatus("mandatory")
_ArcnetTrashedRxMsgs_Type = Counter32
_ArcnetTrashedRxMsgs_Object = MibScalar
arcnetTrashedRxMsgs = _ArcnetTrashedRxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 2, 7),
    _ArcnetTrashedRxMsgs_Type()
)
arcnetTrashedRxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcnetTrashedRxMsgs.setStatus("mandatory")
_ArcnetTrashedTxMsgs_Type = Counter32
_ArcnetTrashedTxMsgs_Object = MibScalar
arcnetTrashedTxMsgs = _ArcnetTrashedTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 2, 8),
    _ArcnetTrashedTxMsgs_Type()
)
arcnetTrashedTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arcnetTrashedTxMsgs.setStatus("mandatory")
_Backplane_ObjectIdentity = ObjectIdentity
backplane = _Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 3)
)


class _BpStatsEnabled_Type(Integer32):
    """Custom type bpStatsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BpStatsEnabled_Type.__name__ = "Integer32"
_BpStatsEnabled_Object = MibScalar
bpStatsEnabled = _BpStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 1),
    _BpStatsEnabled_Type()
)
bpStatsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bpStatsEnabled.setStatus("mandatory")
_BpStatsRxPkts_Type = Counter32
_BpStatsRxPkts_Object = MibScalar
bpStatsRxPkts = _BpStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 2),
    _BpStatsRxPkts_Type()
)
bpStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpStatsRxPkts.setStatus("mandatory")
_BpStatsRxErrors_Type = Counter32
_BpStatsRxErrors_Object = MibScalar
bpStatsRxErrors = _BpStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 3),
    _BpStatsRxErrors_Type()
)
bpStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpStatsRxErrors.setStatus("mandatory")
_BpStatsTxPkts_Type = Counter32
_BpStatsTxPkts_Object = MibScalar
bpStatsTxPkts = _BpStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 4),
    _BpStatsTxPkts_Type()
)
bpStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpStatsTxPkts.setStatus("mandatory")
_BpStatsTxErrors_Type = Counter32
_BpStatsTxErrors_Object = MibScalar
bpStatsTxErrors = _BpStatsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 5),
    _BpStatsTxErrors_Type()
)
bpStatsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpStatsTxErrors.setStatus("mandatory")


class _BpStatsOperState_Type(Integer32):
    """Custom type bpStatsOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BpStatsOperState_Type.__name__ = "Integer32"
_BpStatsOperState_Object = MibScalar
bpStatsOperState = _BpStatsOperState_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 6),
    _BpStatsOperState_Type()
)
bpStatsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpStatsOperState.setStatus("mandatory")
_BpStatsInitialize_Type = Integer32
_BpStatsInitialize_Object = MibScalar
bpStatsInitialize = _BpStatsInitialize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 7),
    _BpStatsInitialize_Type()
)
bpStatsInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bpStatsInitialize.setStatus("mandatory")
_BpStatsTxQOverErrors_Type = Counter32
_BpStatsTxQOverErrors_Object = MibScalar
bpStatsTxQOverErrors = _BpStatsTxQOverErrors_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 8),
    _BpStatsTxQOverErrors_Type()
)
bpStatsTxQOverErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpStatsTxQOverErrors.setStatus("mandatory")
_BpStatsRxBusyTable_Object = MibTable
bpStatsRxBusyTable = _BpStatsRxBusyTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 9)
)
if mibBuilder.loadTexts:
    bpStatsRxBusyTable.setStatus("mandatory")
_BpStatsRxBusyTableEntry_Object = MibTableRow
bpStatsRxBusyTableEntry = _BpStatsRxBusyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 9, 1)
)
bpStatsRxBusyTableEntry.setIndexNames(
    (0, "ARTEL-MIB", "bpStatsRxBusyTableIndex"),
)
if mibBuilder.loadTexts:
    bpStatsRxBusyTableEntry.setStatus("mandatory")


class _BpStatsRxBusyTableIndex_Type(Integer32):
    """Custom type bpStatsRxBusyTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BpStatsRxBusyTableIndex_Type.__name__ = "Integer32"
_BpStatsRxBusyTableIndex_Object = MibTableColumn
bpStatsRxBusyTableIndex = _BpStatsRxBusyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 9, 1, 1),
    _BpStatsRxBusyTableIndex_Type()
)
bpStatsRxBusyTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpStatsRxBusyTableIndex.setStatus("mandatory")
_BpStatsRxBusyTableErrors_Type = Counter32
_BpStatsRxBusyTableErrors_Object = MibTableColumn
bpStatsRxBusyTableErrors = _BpStatsRxBusyTableErrors_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 3, 9, 1, 2),
    _BpStatsRxBusyTableErrors_Type()
)
bpStatsRxBusyTableErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bpStatsRxBusyTableErrors.setStatus("mandatory")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 4)
)
_RestrictedTable_Object = MibTable
restrictedTable = _RestrictedTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 1)
)
if mibBuilder.loadTexts:
    restrictedTable.setStatus("mandatory")
_RestrictedEntry_Object = MibTableRow
restrictedEntry = _RestrictedEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 1, 1)
)
restrictedEntry.setIndexNames(
    (0, "ARTEL-MIB", "restrictedAddr"),
)
if mibBuilder.loadTexts:
    restrictedEntry.setStatus("mandatory")
_RestrictedAddr_Type = PhysAddress
_RestrictedAddr_Object = MibTableColumn
restrictedAddr = _RestrictedAddr_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 1, 1, 1),
    _RestrictedAddr_Type()
)
restrictedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restrictedAddr.setStatus("mandatory")


class _RestrictedStatus_Type(Integer32):
    """Custom type restrictedStatus based on Integer32"""
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


_RestrictedStatus_Type.__name__ = "Integer32"
_RestrictedStatus_Object = MibTableColumn
restrictedStatus = _RestrictedStatus_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 1, 1, 2),
    _RestrictedStatus_Type()
)
restrictedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restrictedStatus.setStatus("mandatory")
_BridgeAgeNow_Type = Integer32
_BridgeAgeNow_Object = MibScalar
bridgeAgeNow = _BridgeAgeNow_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 2),
    _BridgeAgeNow_Type()
)
bridgeAgeNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAgeNow.setStatus("mandatory")


class _BridgeDot1dEnable_Type(Integer32):
    """Custom type bridgeDot1dEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BridgeDot1dEnable_Type.__name__ = "Integer32"
_BridgeDot1dEnable_Object = MibScalar
bridgeDot1dEnable = _BridgeDot1dEnable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 3),
    _BridgeDot1dEnable_Type()
)
bridgeDot1dEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeDot1dEnable.setStatus("mandatory")
_BridgeDot1dResetDefaults_Type = Integer32
_BridgeDot1dResetDefaults_Object = MibScalar
bridgeDot1dResetDefaults = _BridgeDot1dResetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 4),
    _BridgeDot1dResetDefaults_Type()
)
bridgeDot1dResetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeDot1dResetDefaults.setStatus("mandatory")
_BridgeResetPktSwCount_Type = Integer32
_BridgeResetPktSwCount_Object = MibScalar
bridgeResetPktSwCount = _BridgeResetPktSwCount_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 6),
    _BridgeResetPktSwCount_Type()
)
bridgeResetPktSwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeResetPktSwCount.setStatus("mandatory")
_BridgePktSwLastReset_Type = TimeTicks
_BridgePktSwLastReset_Object = MibScalar
bridgePktSwLastReset = _BridgePktSwLastReset_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 7),
    _BridgePktSwLastReset_Type()
)
bridgePktSwLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePktSwLastReset.setStatus("mandatory")
_BridgeResetStatic_Type = Integer32
_BridgeResetStatic_Object = MibScalar
bridgeResetStatic = _BridgeResetStatic_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 8),
    _BridgeResetStatic_Type()
)
bridgeResetStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeResetStatic.setStatus("mandatory")
_BridgeRestrictedReset_Type = Integer32
_BridgeRestrictedReset_Object = MibScalar
bridgeRestrictedReset = _BridgeRestrictedReset_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 9),
    _BridgeRestrictedReset_Type()
)
bridgeRestrictedReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeRestrictedReset.setStatus("mandatory")
_BridgeUdfTable_Object = MibTable
bridgeUdfTable = _BridgeUdfTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11)
)
if mibBuilder.loadTexts:
    bridgeUdfTable.setStatus("mandatory")
_BridgeUdfEntry_Object = MibTableRow
bridgeUdfEntry = _BridgeUdfEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1)
)
bridgeUdfEntry.setIndexNames(
    (0, "ARTEL-MIB", "bridgeUdfPortIndex"),
    (0, "ARTEL-MIB", "bridgeUdfFilterIndex"),
)
if mibBuilder.loadTexts:
    bridgeUdfEntry.setStatus("mandatory")


class _BridgeUdfPortIndex_Type(Integer32):
    """Custom type bridgeUdfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BridgeUdfPortIndex_Type.__name__ = "Integer32"
_BridgeUdfPortIndex_Object = MibTableColumn
bridgeUdfPortIndex = _BridgeUdfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 1),
    _BridgeUdfPortIndex_Type()
)
bridgeUdfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeUdfPortIndex.setStatus("mandatory")


class _BridgeUdfFilterIndex_Type(Integer32):
    """Custom type bridgeUdfFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BridgeUdfFilterIndex_Type.__name__ = "Integer32"
_BridgeUdfFilterIndex_Object = MibTableColumn
bridgeUdfFilterIndex = _BridgeUdfFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 2),
    _BridgeUdfFilterIndex_Type()
)
bridgeUdfFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeUdfFilterIndex.setStatus("mandatory")


class _BridgeUdfState_Type(Integer32):
    """Custom type bridgeUdfState based on Integer32"""
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
        *(("count", 4),
          ("disabled", 1),
          ("filter", 2),
          ("forward", 3))
    )


_BridgeUdfState_Type.__name__ = "Integer32"
_BridgeUdfState_Object = MibTableColumn
bridgeUdfState = _BridgeUdfState_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 3),
    _BridgeUdfState_Type()
)
bridgeUdfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfState.setStatus("mandatory")


class _BridgeUdfComment_Type(DisplayString):
    """Custom type bridgeUdfComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BridgeUdfComment_Type.__name__ = "DisplayString"
_BridgeUdfComment_Object = MibTableColumn
bridgeUdfComment = _BridgeUdfComment_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 4),
    _BridgeUdfComment_Type()
)
bridgeUdfComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfComment.setStatus("mandatory")
_BridgeUdfMatchCounts_Type = Counter32
_BridgeUdfMatchCounts_Object = MibTableColumn
bridgeUdfMatchCounts = _BridgeUdfMatchCounts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 5),
    _BridgeUdfMatchCounts_Type()
)
bridgeUdfMatchCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeUdfMatchCounts.setStatus("mandatory")
_BridgeUdfInitMatchCount_Type = Integer32
_BridgeUdfInitMatchCount_Object = MibTableColumn
bridgeUdfInitMatchCount = _BridgeUdfInitMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 6),
    _BridgeUdfInitMatchCount_Type()
)
bridgeUdfInitMatchCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfInitMatchCount.setStatus("mandatory")


class _BridgeUdfAddressType_Type(Integer32):
    """Custom type bridgeUdfAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1))
    )


_BridgeUdfAddressType_Type.__name__ = "Integer32"
_BridgeUdfAddressType_Object = MibTableColumn
bridgeUdfAddressType = _BridgeUdfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 7),
    _BridgeUdfAddressType_Type()
)
bridgeUdfAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfAddressType.setStatus("mandatory")
_BridgeUdfAddressValue_Type = PhysAddress
_BridgeUdfAddressValue_Object = MibTableColumn
bridgeUdfAddressValue = _BridgeUdfAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 8),
    _BridgeUdfAddressValue_Type()
)
bridgeUdfAddressValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfAddressValue.setStatus("mandatory")
_BridgeUdfAddressMask_Type = PhysAddress
_BridgeUdfAddressMask_Object = MibTableColumn
bridgeUdfAddressMask = _BridgeUdfAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 9),
    _BridgeUdfAddressMask_Type()
)
bridgeUdfAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfAddressMask.setStatus("mandatory")


class _BridgeUdfAddressOperand_Type(Integer32):
    """Custom type bridgeUdfAddressOperand based on Integer32"""
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
        *(("equal", 1),
          ("greaterthan", 5),
          ("greaterthanorequal", 6),
          ("lessthan", 3),
          ("lessthanorequal", 4),
          ("notequal", 2))
    )


_BridgeUdfAddressOperand_Type.__name__ = "Integer32"
_BridgeUdfAddressOperand_Object = MibTableColumn
bridgeUdfAddressOperand = _BridgeUdfAddressOperand_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 10),
    _BridgeUdfAddressOperand_Type()
)
bridgeUdfAddressOperand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfAddressOperand.setStatus("mandatory")
_BridgeUdfTypeValue_Type = Integer32
_BridgeUdfTypeValue_Object = MibTableColumn
bridgeUdfTypeValue = _BridgeUdfTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 11),
    _BridgeUdfTypeValue_Type()
)
bridgeUdfTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfTypeValue.setStatus("mandatory")
_BridgeUdfTypeMask_Type = Integer32
_BridgeUdfTypeMask_Object = MibTableColumn
bridgeUdfTypeMask = _BridgeUdfTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 12),
    _BridgeUdfTypeMask_Type()
)
bridgeUdfTypeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfTypeMask.setStatus("mandatory")


class _BridgeUdfTypeOperand_Type(Integer32):
    """Custom type bridgeUdfTypeOperand based on Integer32"""
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
        *(("equal", 1),
          ("greaterthan", 5),
          ("greaterthanorequal", 6),
          ("lessthan", 3),
          ("lessthanorequal", 4),
          ("notequal", 2))
    )


_BridgeUdfTypeOperand_Type.__name__ = "Integer32"
_BridgeUdfTypeOperand_Object = MibTableColumn
bridgeUdfTypeOperand = _BridgeUdfTypeOperand_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 13),
    _BridgeUdfTypeOperand_Type()
)
bridgeUdfTypeOperand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfTypeOperand.setStatus("mandatory")
_BridgeUdfOffset1Offset_Type = Integer32
_BridgeUdfOffset1Offset_Object = MibTableColumn
bridgeUdfOffset1Offset = _BridgeUdfOffset1Offset_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 14),
    _BridgeUdfOffset1Offset_Type()
)
bridgeUdfOffset1Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset1Offset.setStatus("mandatory")
_BridgeUdfOffset1Value_Type = Integer32
_BridgeUdfOffset1Value_Object = MibTableColumn
bridgeUdfOffset1Value = _BridgeUdfOffset1Value_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 15),
    _BridgeUdfOffset1Value_Type()
)
bridgeUdfOffset1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset1Value.setStatus("mandatory")
_BridgeUdfOffset1Mask_Type = Integer32
_BridgeUdfOffset1Mask_Object = MibTableColumn
bridgeUdfOffset1Mask = _BridgeUdfOffset1Mask_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 16),
    _BridgeUdfOffset1Mask_Type()
)
bridgeUdfOffset1Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset1Mask.setStatus("mandatory")


class _BridgeUdfOffset1Operand_Type(Integer32):
    """Custom type bridgeUdfOffset1Operand based on Integer32"""
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
        *(("equal", 1),
          ("greaterthan", 5),
          ("greaterthanorequal", 6),
          ("lessthan", 3),
          ("lessthanorequal", 4),
          ("notequal", 2))
    )


_BridgeUdfOffset1Operand_Type.__name__ = "Integer32"
_BridgeUdfOffset1Operand_Object = MibTableColumn
bridgeUdfOffset1Operand = _BridgeUdfOffset1Operand_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 17),
    _BridgeUdfOffset1Operand_Type()
)
bridgeUdfOffset1Operand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset1Operand.setStatus("mandatory")
_BridgeUdfOffset2Offset_Type = Integer32
_BridgeUdfOffset2Offset_Object = MibTableColumn
bridgeUdfOffset2Offset = _BridgeUdfOffset2Offset_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 18),
    _BridgeUdfOffset2Offset_Type()
)
bridgeUdfOffset2Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset2Offset.setStatus("mandatory")
_BridgeUdfOffset2Value_Type = Integer32
_BridgeUdfOffset2Value_Object = MibTableColumn
bridgeUdfOffset2Value = _BridgeUdfOffset2Value_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 19),
    _BridgeUdfOffset2Value_Type()
)
bridgeUdfOffset2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset2Value.setStatus("mandatory")
_BridgeUdfOffset2Mask_Type = Integer32
_BridgeUdfOffset2Mask_Object = MibTableColumn
bridgeUdfOffset2Mask = _BridgeUdfOffset2Mask_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 20),
    _BridgeUdfOffset2Mask_Type()
)
bridgeUdfOffset2Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset2Mask.setStatus("mandatory")


class _BridgeUdfOffset2Operand_Type(Integer32):
    """Custom type bridgeUdfOffset2Operand based on Integer32"""
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
        *(("equal", 1),
          ("greaterthan", 5),
          ("greaterthanorequal", 6),
          ("lessthan", 3),
          ("lessthanorequal", 4),
          ("notequal", 2))
    )


_BridgeUdfOffset2Operand_Type.__name__ = "Integer32"
_BridgeUdfOffset2Operand_Object = MibTableColumn
bridgeUdfOffset2Operand = _BridgeUdfOffset2Operand_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 21),
    _BridgeUdfOffset2Operand_Type()
)
bridgeUdfOffset2Operand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset2Operand.setStatus("mandatory")
_BridgeUdfOffset3Offset_Type = Integer32
_BridgeUdfOffset3Offset_Object = MibTableColumn
bridgeUdfOffset3Offset = _BridgeUdfOffset3Offset_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 22),
    _BridgeUdfOffset3Offset_Type()
)
bridgeUdfOffset3Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset3Offset.setStatus("mandatory")
_BridgeUdfOffset3Value_Type = Integer32
_BridgeUdfOffset3Value_Object = MibTableColumn
bridgeUdfOffset3Value = _BridgeUdfOffset3Value_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 23),
    _BridgeUdfOffset3Value_Type()
)
bridgeUdfOffset3Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset3Value.setStatus("mandatory")
_BridgeUdfOffset3Mask_Type = Integer32
_BridgeUdfOffset3Mask_Object = MibTableColumn
bridgeUdfOffset3Mask = _BridgeUdfOffset3Mask_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 24),
    _BridgeUdfOffset3Mask_Type()
)
bridgeUdfOffset3Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset3Mask.setStatus("mandatory")


class _BridgeUdfOffset3Operand_Type(Integer32):
    """Custom type bridgeUdfOffset3Operand based on Integer32"""
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
        *(("equal", 1),
          ("greaterthan", 5),
          ("greaterthanorequal", 6),
          ("lessthan", 3),
          ("lessthanorequal", 4),
          ("notequal", 2))
    )


_BridgeUdfOffset3Operand_Type.__name__ = "Integer32"
_BridgeUdfOffset3Operand_Object = MibTableColumn
bridgeUdfOffset3Operand = _BridgeUdfOffset3Operand_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 25),
    _BridgeUdfOffset3Operand_Type()
)
bridgeUdfOffset3Operand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset3Operand.setStatus("mandatory")
_BridgeUdfOffset4Offset_Type = Integer32
_BridgeUdfOffset4Offset_Object = MibTableColumn
bridgeUdfOffset4Offset = _BridgeUdfOffset4Offset_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 26),
    _BridgeUdfOffset4Offset_Type()
)
bridgeUdfOffset4Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset4Offset.setStatus("mandatory")
_BridgeUdfOffset4Value_Type = Integer32
_BridgeUdfOffset4Value_Object = MibTableColumn
bridgeUdfOffset4Value = _BridgeUdfOffset4Value_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 27),
    _BridgeUdfOffset4Value_Type()
)
bridgeUdfOffset4Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset4Value.setStatus("mandatory")
_BridgeUdfOffset4Mask_Type = Integer32
_BridgeUdfOffset4Mask_Object = MibTableColumn
bridgeUdfOffset4Mask = _BridgeUdfOffset4Mask_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 28),
    _BridgeUdfOffset4Mask_Type()
)
bridgeUdfOffset4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset4Mask.setStatus("mandatory")


class _BridgeUdfOffset4Operand_Type(Integer32):
    """Custom type bridgeUdfOffset4Operand based on Integer32"""
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
        *(("equal", 1),
          ("greaterthan", 5),
          ("greaterthanorequal", 6),
          ("lessthan", 3),
          ("lessthanorequal", 4),
          ("notequal", 2))
    )


_BridgeUdfOffset4Operand_Type.__name__ = "Integer32"
_BridgeUdfOffset4Operand_Object = MibTableColumn
bridgeUdfOffset4Operand = _BridgeUdfOffset4Operand_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 11, 1, 29),
    _BridgeUdfOffset4Operand_Type()
)
bridgeUdfOffset4Operand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfOffset4Operand.setStatus("mandatory")
_BridgeUdfInitCountTable_Object = MibTable
bridgeUdfInitCountTable = _BridgeUdfInitCountTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 12)
)
if mibBuilder.loadTexts:
    bridgeUdfInitCountTable.setStatus("mandatory")
_BridgeUdfInitCountEntry_Object = MibTableRow
bridgeUdfInitCountEntry = _BridgeUdfInitCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 12, 1)
)
bridgeUdfInitCountEntry.setIndexNames(
    (0, "ARTEL-MIB", "bridgeUdfCountPortIndex"),
)
if mibBuilder.loadTexts:
    bridgeUdfInitCountEntry.setStatus("mandatory")


class _BridgeUdfCountPortIndex_Type(Integer32):
    """Custom type bridgeUdfCountPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BridgeUdfCountPortIndex_Type.__name__ = "Integer32"
_BridgeUdfCountPortIndex_Object = MibTableColumn
bridgeUdfCountPortIndex = _BridgeUdfCountPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 12, 1, 1),
    _BridgeUdfCountPortIndex_Type()
)
bridgeUdfCountPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeUdfCountPortIndex.setStatus("mandatory")
_BridgeUdfCountInitMatchCount_Type = Integer32
_BridgeUdfCountInitMatchCount_Object = MibTableColumn
bridgeUdfCountInitMatchCount = _BridgeUdfCountInitMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 12, 1, 2),
    _BridgeUdfCountInitMatchCount_Type()
)
bridgeUdfCountInitMatchCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeUdfCountInitMatchCount.setStatus("mandatory")


class _BridgePortGroupEnable_Type(Integer32):
    """Custom type bridgePortGroupEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BridgePortGroupEnable_Type.__name__ = "Integer32"
_BridgePortGroupEnable_Object = MibScalar
bridgePortGroupEnable = _BridgePortGroupEnable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 13),
    _BridgePortGroupEnable_Type()
)
bridgePortGroupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgePortGroupEnable.setStatus("mandatory")
_BridgePortGroupTable_Object = MibTable
bridgePortGroupTable = _BridgePortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 14)
)
if mibBuilder.loadTexts:
    bridgePortGroupTable.setStatus("mandatory")
_BridgePortGroupEntry_Object = MibTableRow
bridgePortGroupEntry = _BridgePortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 14, 1)
)
bridgePortGroupEntry.setIndexNames(
    (0, "ARTEL-MIB", "bridgePortGroupTablePortIndex"),
    (0, "ARTEL-MIB", "bridgePortGroupTableGroupIndex"),
)
if mibBuilder.loadTexts:
    bridgePortGroupEntry.setStatus("mandatory")


class _BridgePortGroupTablePortIndex_Type(Integer32):
    """Custom type bridgePortGroupTablePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_BridgePortGroupTablePortIndex_Type.__name__ = "Integer32"
_BridgePortGroupTablePortIndex_Object = MibTableColumn
bridgePortGroupTablePortIndex = _BridgePortGroupTablePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 14, 1, 1),
    _BridgePortGroupTablePortIndex_Type()
)
bridgePortGroupTablePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePortGroupTablePortIndex.setStatus("mandatory")


class _BridgePortGroupTableGroupIndex_Type(Integer32):
    """Custom type bridgePortGroupTableGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BridgePortGroupTableGroupIndex_Type.__name__ = "Integer32"
_BridgePortGroupTableGroupIndex_Object = MibTableColumn
bridgePortGroupTableGroupIndex = _BridgePortGroupTableGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 14, 1, 2),
    _BridgePortGroupTableGroupIndex_Type()
)
bridgePortGroupTableGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePortGroupTableGroupIndex.setStatus("mandatory")


class _BridgePortGroupTableEnable_Type(Integer32):
    """Custom type bridgePortGroupTableEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BridgePortGroupTableEnable_Type.__name__ = "Integer32"
_BridgePortGroupTableEnable_Object = MibTableColumn
bridgePortGroupTableEnable = _BridgePortGroupTableEnable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 14, 1, 3),
    _BridgePortGroupTableEnable_Type()
)
bridgePortGroupTableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgePortGroupTableEnable.setStatus("mandatory")
_BridgePortGroupPortTable_Object = MibTable
bridgePortGroupPortTable = _BridgePortGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 15)
)
if mibBuilder.loadTexts:
    bridgePortGroupPortTable.setStatus("mandatory")
_BridgePortGroupPortEntry_Object = MibTableRow
bridgePortGroupPortEntry = _BridgePortGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 15, 1)
)
bridgePortGroupPortEntry.setIndexNames(
    (0, "ARTEL-MIB", "bridgePortGroupPortIndex"),
)
if mibBuilder.loadTexts:
    bridgePortGroupPortEntry.setStatus("mandatory")


class _BridgePortGroupPortIndex_Type(Integer32):
    """Custom type bridgePortGroupPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BridgePortGroupPortIndex_Type.__name__ = "Integer32"
_BridgePortGroupPortIndex_Object = MibTableColumn
bridgePortGroupPortIndex = _BridgePortGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 15, 1, 1),
    _BridgePortGroupPortIndex_Type()
)
bridgePortGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePortGroupPortIndex.setStatus("mandatory")


class _BridgePortGroupPortDisplayString_Type(DisplayString):
    """Custom type bridgePortGroupPortDisplayString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BridgePortGroupPortDisplayString_Type.__name__ = "DisplayString"
_BridgePortGroupPortDisplayString_Object = MibTableColumn
bridgePortGroupPortDisplayString = _BridgePortGroupPortDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 15, 1, 2),
    _BridgePortGroupPortDisplayString_Type()
)
bridgePortGroupPortDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePortGroupPortDisplayString.setStatus("mandatory")
_BridgePortGroupGroupTable_Object = MibTable
bridgePortGroupGroupTable = _BridgePortGroupGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 16)
)
if mibBuilder.loadTexts:
    bridgePortGroupGroupTable.setStatus("mandatory")
_BridgePortGroupGroupEntry_Object = MibTableRow
bridgePortGroupGroupEntry = _BridgePortGroupGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 16, 1)
)
bridgePortGroupGroupEntry.setIndexNames(
    (0, "ARTEL-MIB", "bridgePortGroupGroupIndex"),
)
if mibBuilder.loadTexts:
    bridgePortGroupGroupEntry.setStatus("mandatory")


class _BridgePortGroupGroupIndex_Type(Integer32):
    """Custom type bridgePortGroupGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BridgePortGroupGroupIndex_Type.__name__ = "Integer32"
_BridgePortGroupGroupIndex_Object = MibTableColumn
bridgePortGroupGroupIndex = _BridgePortGroupGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 16, 1, 1),
    _BridgePortGroupGroupIndex_Type()
)
bridgePortGroupGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePortGroupGroupIndex.setStatus("mandatory")
_BridgePortGroupGroupPortMap_Type = OctetString
_BridgePortGroupGroupPortMap_Object = MibTableColumn
bridgePortGroupGroupPortMap = _BridgePortGroupGroupPortMap_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 16, 1, 2),
    _BridgePortGroupGroupPortMap_Type()
)
bridgePortGroupGroupPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgePortGroupGroupPortMap.setStatus("mandatory")


class _BridgePortGroupGroupComment_Type(DisplayString):
    """Custom type bridgePortGroupGroupComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BridgePortGroupGroupComment_Type.__name__ = "DisplayString"
_BridgePortGroupGroupComment_Object = MibTableColumn
bridgePortGroupGroupComment = _BridgePortGroupGroupComment_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 16, 1, 3),
    _BridgePortGroupGroupComment_Type()
)
bridgePortGroupGroupComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePortGroupGroupComment.setStatus("mandatory")
_BridgeAddrFilterTable_Object = MibTable
bridgeAddrFilterTable = _BridgeAddrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 17)
)
if mibBuilder.loadTexts:
    bridgeAddrFilterTable.setStatus("mandatory")
_BridgeAddrFilterEntry_Object = MibTableRow
bridgeAddrFilterEntry = _BridgeAddrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 17, 1)
)
bridgeAddrFilterEntry.setIndexNames(
    (0, "ARTEL-MIB", "bridgeAddrFilterBlockIndex"),
)
if mibBuilder.loadTexts:
    bridgeAddrFilterEntry.setStatus("mandatory")


class _BridgeAddrFilterBlockIndex_Type(Integer32):
    """Custom type bridgeAddrFilterBlockIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 205),
    )


_BridgeAddrFilterBlockIndex_Type.__name__ = "Integer32"
_BridgeAddrFilterBlockIndex_Object = MibTableColumn
bridgeAddrFilterBlockIndex = _BridgeAddrFilterBlockIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 17, 1, 1),
    _BridgeAddrFilterBlockIndex_Type()
)
bridgeAddrFilterBlockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeAddrFilterBlockIndex.setStatus("mandatory")
_BridgeAddrFilterBlockData_Type = Opaque
_BridgeAddrFilterBlockData_Object = MibTableColumn
bridgeAddrFilterBlockData = _BridgeAddrFilterBlockData_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 17, 1, 2),
    _BridgeAddrFilterBlockData_Type()
)
bridgeAddrFilterBlockData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeAddrFilterBlockData.setStatus("mandatory")
_Bridgedot1dTpFdbTable_Object = MibTable
bridgedot1dTpFdbTable = _Bridgedot1dTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 18)
)
if mibBuilder.loadTexts:
    bridgedot1dTpFdbTable.setStatus("mandatory")
_Bridgedot1dTpFdbEntry_Object = MibTableRow
bridgedot1dTpFdbEntry = _Bridgedot1dTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 18, 1)
)
bridgedot1dTpFdbEntry.setIndexNames(
    (0, "ARTEL-MIB", "bridgedot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    bridgedot1dTpFdbEntry.setStatus("mandatory")
_Bridgedot1dTpFdbAddress_Type = PhysAddress
_Bridgedot1dTpFdbAddress_Object = MibTableColumn
bridgedot1dTpFdbAddress = _Bridgedot1dTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 18, 1, 1),
    _Bridgedot1dTpFdbAddress_Type()
)
bridgedot1dTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgedot1dTpFdbAddress.setStatus("mandatory")
_Bridgedot1dTpFdbSlot_Type = Integer32
_Bridgedot1dTpFdbSlot_Object = MibTableColumn
bridgedot1dTpFdbSlot = _Bridgedot1dTpFdbSlot_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 18, 1, 2),
    _Bridgedot1dTpFdbSlot_Type()
)
bridgedot1dTpFdbSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgedot1dTpFdbSlot.setStatus("mandatory")
_Bridgedot1dTpFdbPort_Type = Integer32
_Bridgedot1dTpFdbPort_Object = MibTableColumn
bridgedot1dTpFdbPort = _Bridgedot1dTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 18, 1, 3),
    _Bridgedot1dTpFdbPort_Type()
)
bridgedot1dTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgedot1dTpFdbPort.setStatus("mandatory")


class _Bridgedot1dTpFdbStatus_Type(Integer32):
    """Custom type bridgedot1dTpFdbStatus based on Integer32"""
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
        *(("invalid", 1),
          ("learned", 2),
          ("restrict", 4),
          ("self", 6),
          ("spantree", 5),
          ("static", 3))
    )


_Bridgedot1dTpFdbStatus_Type.__name__ = "Integer32"
_Bridgedot1dTpFdbStatus_Object = MibTableColumn
bridgedot1dTpFdbStatus = _Bridgedot1dTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 18, 1, 4),
    _Bridgedot1dTpFdbStatus_Type()
)
bridgedot1dTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgedot1dTpFdbStatus.setStatus("mandatory")


class _Bridgedot1dTpFdbAge_Type(Integer32):
    """Custom type bridgedot1dTpFdbAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("notaged", 2),
          ("onceaged", 3))
    )


_Bridgedot1dTpFdbAge_Type.__name__ = "Integer32"
_Bridgedot1dTpFdbAge_Object = MibTableColumn
bridgedot1dTpFdbAge = _Bridgedot1dTpFdbAge_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 4, 18, 1, 5),
    _Bridgedot1dTpFdbAge_Type()
)
bridgedot1dTpFdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgedot1dTpFdbAge.setStatus("mandatory")
_SystemManagement_ObjectIdentity = ObjectIdentity
systemManagement = _SystemManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 5)
)
_SmConfiguration_ObjectIdentity = ObjectIdentity
smConfiguration = _SmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1)
)


class _SmCfgManufactureDate_Type(DisplayString):
    """Custom type smCfgManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmCfgManufactureDate_Type.__name__ = "DisplayString"
_SmCfgManufactureDate_Object = MibScalar
smCfgManufactureDate = _SmCfgManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 1),
    _SmCfgManufactureDate_Type()
)
smCfgManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgManufactureDate.setStatus("mandatory")


class _SmCfgType_Type(Integer32):
    """Custom type smCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("system-management-board", 1)
    )


_SmCfgType_Type.__name__ = "Integer32"
_SmCfgType_Object = MibScalar
smCfgType = _SmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 2),
    _SmCfgType_Type()
)
smCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgType.setStatus("mandatory")


class _SmCfgHardwareRev_Type(DisplayString):
    """Custom type smCfgHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmCfgHardwareRev_Type.__name__ = "DisplayString"
_SmCfgHardwareRev_Object = MibScalar
smCfgHardwareRev = _SmCfgHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 3),
    _SmCfgHardwareRev_Type()
)
smCfgHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgHardwareRev.setStatus("mandatory")


class _SmCfgSerialNumber_Type(DisplayString):
    """Custom type smCfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmCfgSerialNumber_Type.__name__ = "DisplayString"
_SmCfgSerialNumber_Object = MibScalar
smCfgSerialNumber = _SmCfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 4),
    _SmCfgSerialNumber_Type()
)
smCfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgSerialNumber.setStatus("mandatory")
_SmCfgMacAddr_Type = PhysAddress
_SmCfgMacAddr_Object = MibScalar
smCfgMacAddr = _SmCfgMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 5),
    _SmCfgMacAddr_Type()
)
smCfgMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgMacAddr.setStatus("mandatory")
_SmCfgFlashMemSize_Type = Integer32
_SmCfgFlashMemSize_Object = MibScalar
smCfgFlashMemSize = _SmCfgFlashMemSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 6),
    _SmCfgFlashMemSize_Type()
)
smCfgFlashMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgFlashMemSize.setStatus("mandatory")
_SmCfg68kRamSize_Type = Integer32
_SmCfg68kRamSize_Object = MibScalar
smCfg68kRamSize = _SmCfg68kRamSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 7),
    _SmCfg68kRamSize_Type()
)
smCfg68kRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfg68kRamSize.setStatus("mandatory")


class _SmCfgBootRev_Type(DisplayString):
    """Custom type smCfgBootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmCfgBootRev_Type.__name__ = "DisplayString"
_SmCfgBootRev_Object = MibScalar
smCfgBootRev = _SmCfgBootRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 8),
    _SmCfgBootRev_Type()
)
smCfgBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgBootRev.setStatus("mandatory")


class _SmCfg68kRev_Type(DisplayString):
    """Custom type smCfg68kRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmCfg68kRev_Type.__name__ = "DisplayString"
_SmCfg68kRev_Object = MibScalar
smCfg68kRev = _SmCfg68kRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 9),
    _SmCfg68kRev_Type()
)
smCfg68kRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfg68kRev.setStatus("mandatory")


class _SmCfgModulePartNumber_Type(DisplayString):
    """Custom type smCfgModulePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmCfgModulePartNumber_Type.__name__ = "DisplayString"
_SmCfgModulePartNumber_Object = MibScalar
smCfgModulePartNumber = _SmCfgModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 10),
    _SmCfgModulePartNumber_Type()
)
smCfgModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgModulePartNumber.setStatus("mandatory")


class _SmCfgModuleSerialNumber_Type(DisplayString):
    """Custom type smCfgModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmCfgModuleSerialNumber_Type.__name__ = "DisplayString"
_SmCfgModuleSerialNumber_Object = MibScalar
smCfgModuleSerialNumber = _SmCfgModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 11),
    _SmCfgModuleSerialNumber_Type()
)
smCfgModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgModuleSerialNumber.setStatus("mandatory")


class _SmCfgStoreFlashRev_Type(DisplayString):
    """Custom type smCfgStoreFlashRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmCfgStoreFlashRev_Type.__name__ = "DisplayString"
_SmCfgStoreFlashRev_Object = MibScalar
smCfgStoreFlashRev = _SmCfgStoreFlashRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 12),
    _SmCfgStoreFlashRev_Type()
)
smCfgStoreFlashRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgStoreFlashRev.setStatus("mandatory")


class _SmCfgExecFlashRev_Type(DisplayString):
    """Custom type smCfgExecFlashRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmCfgExecFlashRev_Type.__name__ = "DisplayString"
_SmCfgExecFlashRev_Object = MibScalar
smCfgExecFlashRev = _SmCfgExecFlashRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 1, 13),
    _SmCfgExecFlashRev_Type()
)
smCfgExecFlashRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smCfgExecFlashRev.setStatus("mandatory")
_SmBackplane_ObjectIdentity = ObjectIdentity
smBackplane = _SmBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2)
)


class _SmBpType_Type(Integer32):
    """Custom type smBpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("five-Slot", 5)
    )


_SmBpType_Type.__name__ = "Integer32"
_SmBpType_Object = MibScalar
smBpType = _SmBpType_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 1),
    _SmBpType_Type()
)
smBpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBpType.setStatus("mandatory")
_SmBpArbTimer_Type = Integer32
_SmBpArbTimer_Object = MibScalar
smBpArbTimer = _SmBpArbTimer_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 2),
    _SmBpArbTimer_Type()
)
smBpArbTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBpArbTimer.setStatus("mandatory")
_SmBpMaxPktSize_Type = Integer32
_SmBpMaxPktSize_Object = MibScalar
smBpMaxPktSize = _SmBpMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 3),
    _SmBpMaxPktSize_Type()
)
smBpMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBpMaxPktSize.setStatus("mandatory")
_SmBpAsyncSlotsEnb_Type = Integer32
_SmBpAsyncSlotsEnb_Object = MibScalar
smBpAsyncSlotsEnb = _SmBpAsyncSlotsEnb_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 4),
    _SmBpAsyncSlotsEnb_Type()
)
smBpAsyncSlotsEnb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBpAsyncSlotsEnb.setStatus("mandatory")
_SmBpSyncSlotsEnb_Type = Integer32
_SmBpSyncSlotsEnb_Object = MibScalar
smBpSyncSlotsEnb = _SmBpSyncSlotsEnb_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 5),
    _SmBpSyncSlotsEnb_Type()
)
smBpSyncSlotsEnb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBpSyncSlotsEnb.setStatus("mandatory")
_SmBpUtilization_Type = Integer32
_SmBpUtilization_Object = MibScalar
smBpUtilization = _SmBpUtilization_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 6),
    _SmBpUtilization_Type()
)
smBpUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBpUtilization.setStatus("mandatory")
_SmBpTable_Object = MibTable
smBpTable = _SmBpTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 7)
)
if mibBuilder.loadTexts:
    smBpTable.setStatus("mandatory")
_SmBpEntry_Object = MibTableRow
smBpEntry = _SmBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 7, 1)
)
smBpEntry.setIndexNames(
    (0, "ARTEL-MIB", "smBpIndex"),
)
if mibBuilder.loadTexts:
    smBpEntry.setStatus("mandatory")


class _SmBpIndex_Type(Integer32):
    """Custom type smBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SmBpIndex_Type.__name__ = "Integer32"
_SmBpIndex_Object = MibTableColumn
smBpIndex = _SmBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 7, 1, 1),
    _SmBpIndex_Type()
)
smBpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBpIndex.setStatus("mandatory")


class _SmBpTableEnable_Type(Integer32):
    """Custom type smBpTableEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SmBpTableEnable_Type.__name__ = "Integer32"
_SmBpTableEnable_Object = MibTableColumn
smBpTableEnable = _SmBpTableEnable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 7, 1, 2),
    _SmBpTableEnable_Type()
)
smBpTableEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBpTableEnable.setStatus("mandatory")


class _SmBpTableJabber_Type(Integer32):
    """Custom type smBpTableJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SmBpTableJabber_Type.__name__ = "Integer32"
_SmBpTableJabber_Object = MibTableColumn
smBpTableJabber = _SmBpTableJabber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 7, 1, 3),
    _SmBpTableJabber_Type()
)
smBpTableJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smBpTableJabber.setStatus("mandatory")
_SmBpTableClearJabber_Type = Integer32
_SmBpTableClearJabber_Object = MibTableColumn
smBpTableClearJabber = _SmBpTableClearJabber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 2, 7, 1, 4),
    _SmBpTableClearJabber_Type()
)
smBpTableClearJabber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smBpTableClearJabber.setStatus("mandatory")
_SmPowerSupply_ObjectIdentity = ObjectIdentity
smPowerSupply = _SmPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 4)
)
_SmSupplyPresent_Type = Integer32
_SmSupplyPresent_Object = MibScalar
smSupplyPresent = _SmSupplyPresent_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 4, 1),
    _SmSupplyPresent_Type()
)
smSupplyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSupplyPresent.setStatus("mandatory")
_SmSupplyType_Type = Integer32
_SmSupplyType_Object = MibScalar
smSupplyType = _SmSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 4, 2),
    _SmSupplyType_Type()
)
smSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSupplyType.setStatus("mandatory")
_SmSupplyAcOk_Type = Integer32
_SmSupplyAcOk_Object = MibScalar
smSupplyAcOk = _SmSupplyAcOk_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 4, 3),
    _SmSupplyAcOk_Type()
)
smSupplyAcOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSupplyAcOk.setStatus("mandatory")
_SmSupplyDcOk_Type = Integer32
_SmSupplyDcOk_Object = MibScalar
smSupplyDcOk = _SmSupplyDcOk_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 4, 4),
    _SmSupplyDcOk_Type()
)
smSupplyDcOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSupplyDcOk.setStatus("mandatory")
_SmSupplyTable_Object = MibTable
smSupplyTable = _SmSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 4, 5)
)
if mibBuilder.loadTexts:
    smSupplyTable.setStatus("mandatory")
_SmSupplyTableEntry_Object = MibTableRow
smSupplyTableEntry = _SmSupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 4, 5, 1)
)
smSupplyTableEntry.setIndexNames(
    (0, "ARTEL-MIB", "smSupplyTableIndex"),
)
if mibBuilder.loadTexts:
    smSupplyTableEntry.setStatus("mandatory")


class _SmSupplyTableIndex_Type(Integer32):
    """Custom type smSupplyTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SmSupplyTableIndex_Type.__name__ = "Integer32"
_SmSupplyTableIndex_Object = MibTableColumn
smSupplyTableIndex = _SmSupplyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 4, 5, 1, 1),
    _SmSupplyTableIndex_Type()
)
smSupplyTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSupplyTableIndex.setStatus("mandatory")


class _SmSupplyTableStatus_Type(DisplayString):
    """Custom type smSupplyTableStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmSupplyTableStatus_Type.__name__ = "DisplayString"
_SmSupplyTableStatus_Object = MibTableColumn
smSupplyTableStatus = _SmSupplyTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 4, 5, 1, 2),
    _SmSupplyTableStatus_Type()
)
smSupplyTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSupplyTableStatus.setStatus("mandatory")
_SmModem_ObjectIdentity = ObjectIdentity
smModem = _SmModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 5)
)


class _SmModemType_Type(Integer32):
    """Custom type smModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal-japan-2400-baud", 1),
          ("internal-usa-2400-baud", 2))
    )


_SmModemType_Type.__name__ = "Integer32"
_SmModemType_Object = MibScalar
smModemType = _SmModemType_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 5, 1),
    _SmModemType_Type()
)
smModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smModemType.setStatus("mandatory")


class _SmModemCallBackEnable_Type(Integer32):
    """Custom type smModemCallBackEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SmModemCallBackEnable_Type.__name__ = "Integer32"
_SmModemCallBackEnable_Object = MibScalar
smModemCallBackEnable = _SmModemCallBackEnable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 5, 2),
    _SmModemCallBackEnable_Type()
)
smModemCallBackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smModemCallBackEnable.setStatus("mandatory")


class _SmModemCallBackNumber_Type(DisplayString):
    """Custom type smModemCallBackNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmModemCallBackNumber_Type.__name__ = "DisplayString"
_SmModemCallBackNumber_Object = MibScalar
smModemCallBackNumber = _SmModemCallBackNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 5, 5, 3),
    _SmModemCallBackNumber_Type()
)
smModemCallBackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smModemCallBackNumber.setStatus("mandatory")
_Starbridge_ObjectIdentity = ObjectIdentity
starbridge = _Starbridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 6)
)
_SbConfiguration_ObjectIdentity = ObjectIdentity
sbConfiguration = _SbConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1)
)


class _SbCfgManufactureDate_Type(DisplayString):
    """Custom type sbCfgManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgManufactureDate_Type.__name__ = "DisplayString"
_SbCfgManufactureDate_Object = MibScalar
sbCfgManufactureDate = _SbCfgManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 1),
    _SbCfgManufactureDate_Type()
)
sbCfgManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgManufactureDate.setStatus("mandatory")


class _SbCfgType_Type(Integer32):
    """Custom type sbCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("starbridge-board", 2)
    )


_SbCfgType_Type.__name__ = "Integer32"
_SbCfgType_Object = MibScalar
sbCfgType = _SbCfgType_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 2),
    _SbCfgType_Type()
)
sbCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgType.setStatus("mandatory")


class _SbCfgHardwareRev_Type(DisplayString):
    """Custom type sbCfgHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgHardwareRev_Type.__name__ = "DisplayString"
_SbCfgHardwareRev_Object = MibScalar
sbCfgHardwareRev = _SbCfgHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 3),
    _SbCfgHardwareRev_Type()
)
sbCfgHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgHardwareRev.setStatus("mandatory")


class _SbCfgSerialNumber_Type(DisplayString):
    """Custom type sbCfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgSerialNumber_Type.__name__ = "DisplayString"
_SbCfgSerialNumber_Object = MibScalar
sbCfgSerialNumber = _SbCfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 4),
    _SbCfgSerialNumber_Type()
)
sbCfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgSerialNumber.setStatus("mandatory")
_SbCfgNumberIfBoards_Type = Integer32
_SbCfgNumberIfBoards_Object = MibScalar
sbCfgNumberIfBoards = _SbCfgNumberIfBoards_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 5),
    _SbCfgNumberIfBoards_Type()
)
sbCfgNumberIfBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgNumberIfBoards.setStatus("mandatory")


class _SbCfgIfBd1Type_Type(Integer32):
    """Custom type sbCfgIfBd1Type based on Integer32"""
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
        *(("foirl", 5),
          ("ten-base-f", 6),
          ("thicknet-dce", 2),
          ("thicknet-dte", 1),
          ("thinnet", 3),
          ("twisted-pair", 4))
    )


_SbCfgIfBd1Type_Type.__name__ = "Integer32"
_SbCfgIfBd1Type_Object = MibScalar
sbCfgIfBd1Type = _SbCfgIfBd1Type_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 6),
    _SbCfgIfBd1Type_Type()
)
sbCfgIfBd1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgIfBd1Type.setStatus("mandatory")


class _SbCfgIfBd1Rev_Type(DisplayString):
    """Custom type sbCfgIfBd1Rev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgIfBd1Rev_Type.__name__ = "DisplayString"
_SbCfgIfBd1Rev_Object = MibScalar
sbCfgIfBd1Rev = _SbCfgIfBd1Rev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 7),
    _SbCfgIfBd1Rev_Type()
)
sbCfgIfBd1Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgIfBd1Rev.setStatus("mandatory")


class _SbCfgIfBd1SerialNum_Type(DisplayString):
    """Custom type sbCfgIfBd1SerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgIfBd1SerialNum_Type.__name__ = "DisplayString"
_SbCfgIfBd1SerialNum_Object = MibScalar
sbCfgIfBd1SerialNum = _SbCfgIfBd1SerialNum_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 8),
    _SbCfgIfBd1SerialNum_Type()
)
sbCfgIfBd1SerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgIfBd1SerialNum.setStatus("mandatory")
_SbCfgIfBd1NumPorts_Type = Integer32
_SbCfgIfBd1NumPorts_Object = MibScalar
sbCfgIfBd1NumPorts = _SbCfgIfBd1NumPorts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 9),
    _SbCfgIfBd1NumPorts_Type()
)
sbCfgIfBd1NumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgIfBd1NumPorts.setStatus("mandatory")


class _SbCfgIfBd2Type_Type(Integer32):
    """Custom type sbCfgIfBd2Type based on Integer32"""
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
        *(("foirl", 5),
          ("ten-base-f", 6),
          ("thicknet-dce", 2),
          ("thicknet-dte", 1),
          ("thinnet", 3),
          ("twisted-pair", 4))
    )


_SbCfgIfBd2Type_Type.__name__ = "Integer32"
_SbCfgIfBd2Type_Object = MibScalar
sbCfgIfBd2Type = _SbCfgIfBd2Type_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 10),
    _SbCfgIfBd2Type_Type()
)
sbCfgIfBd2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgIfBd2Type.setStatus("mandatory")


class _SbCfgIfBd2Rev_Type(DisplayString):
    """Custom type sbCfgIfBd2Rev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgIfBd2Rev_Type.__name__ = "DisplayString"
_SbCfgIfBd2Rev_Object = MibScalar
sbCfgIfBd2Rev = _SbCfgIfBd2Rev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 11),
    _SbCfgIfBd2Rev_Type()
)
sbCfgIfBd2Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgIfBd2Rev.setStatus("mandatory")


class _SbCfgIfBd2SerialNum_Type(DisplayString):
    """Custom type sbCfgIfBd2SerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgIfBd2SerialNum_Type.__name__ = "DisplayString"
_SbCfgIfBd2SerialNum_Object = MibScalar
sbCfgIfBd2SerialNum = _SbCfgIfBd2SerialNum_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 12),
    _SbCfgIfBd2SerialNum_Type()
)
sbCfgIfBd2SerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgIfBd2SerialNum.setStatus("mandatory")
_SbCfgIfBd2NumPorts_Type = Integer32
_SbCfgIfBd2NumPorts_Object = MibScalar
sbCfgIfBd2NumPorts = _SbCfgIfBd2NumPorts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 13),
    _SbCfgIfBd2NumPorts_Type()
)
sbCfgIfBd2NumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgIfBd2NumPorts.setStatus("mandatory")
_SbCfgFlashMemorySize_Type = Integer32
_SbCfgFlashMemorySize_Object = MibScalar
sbCfgFlashMemorySize = _SbCfgFlashMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 14),
    _SbCfgFlashMemorySize_Type()
)
sbCfgFlashMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgFlashMemorySize.setStatus("mandatory")
_SbCfg68kRamSize_Type = Integer32
_SbCfg68kRamSize_Object = MibScalar
sbCfg68kRamSize = _SbCfg68kRamSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 15),
    _SbCfg68kRamSize_Type()
)
sbCfg68kRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfg68kRamSize.setStatus("mandatory")
_SbCfg960RamSize_Type = Integer32
_SbCfg960RamSize_Object = MibScalar
sbCfg960RamSize = _SbCfg960RamSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 16),
    _SbCfg960RamSize_Type()
)
sbCfg960RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfg960RamSize.setStatus("mandatory")
_SbCfgSonicRamSize_Type = Integer32
_SbCfgSonicRamSize_Object = MibScalar
sbCfgSonicRamSize = _SbCfgSonicRamSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 17),
    _SbCfgSonicRamSize_Type()
)
sbCfgSonicRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgSonicRamSize.setStatus("mandatory")
_SbCfgHasherCacheTagSize_Type = Integer32
_SbCfgHasherCacheTagSize_Object = MibScalar
sbCfgHasherCacheTagSize = _SbCfgHasherCacheTagSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 18),
    _SbCfgHasherCacheTagSize_Type()
)
sbCfgHasherCacheTagSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgHasherCacheTagSize.setStatus("mandatory")
_SbCfgDualPortRamSize_Type = Integer32
_SbCfgDualPortRamSize_Object = MibScalar
sbCfgDualPortRamSize = _SbCfgDualPortRamSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 19),
    _SbCfgDualPortRamSize_Type()
)
sbCfgDualPortRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgDualPortRamSize.setStatus("mandatory")


class _SbCfgBootRev_Type(DisplayString):
    """Custom type sbCfgBootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgBootRev_Type.__name__ = "DisplayString"
_SbCfgBootRev_Object = MibScalar
sbCfgBootRev = _SbCfgBootRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 20),
    _SbCfgBootRev_Type()
)
sbCfgBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgBootRev.setStatus("mandatory")


class _SbCfg68kRev_Type(DisplayString):
    """Custom type sbCfg68kRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfg68kRev_Type.__name__ = "DisplayString"
_SbCfg68kRev_Object = MibScalar
sbCfg68kRev = _SbCfg68kRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 21),
    _SbCfg68kRev_Type()
)
sbCfg68kRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfg68kRev.setStatus("mandatory")


class _SbCfg960Rev_Type(DisplayString):
    """Custom type sbCfg960Rev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfg960Rev_Type.__name__ = "DisplayString"
_SbCfg960Rev_Object = MibScalar
sbCfg960Rev = _SbCfg960Rev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 22),
    _SbCfg960Rev_Type()
)
sbCfg960Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfg960Rev.setStatus("mandatory")


class _SbCfgModulePartNumber_Type(DisplayString):
    """Custom type sbCfgModulePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgModulePartNumber_Type.__name__ = "DisplayString"
_SbCfgModulePartNumber_Object = MibScalar
sbCfgModulePartNumber = _SbCfgModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 23),
    _SbCfgModulePartNumber_Type()
)
sbCfgModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgModulePartNumber.setStatus("mandatory")


class _SbCfgModuleSerialNumber_Type(DisplayString):
    """Custom type sbCfgModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgModuleSerialNumber_Type.__name__ = "DisplayString"
_SbCfgModuleSerialNumber_Object = MibScalar
sbCfgModuleSerialNumber = _SbCfgModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 24),
    _SbCfgModuleSerialNumber_Type()
)
sbCfgModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgModuleSerialNumber.setStatus("mandatory")


class _SbCfgStoreFlashRev_Type(DisplayString):
    """Custom type sbCfgStoreFlashRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgStoreFlashRev_Type.__name__ = "DisplayString"
_SbCfgStoreFlashRev_Object = MibScalar
sbCfgStoreFlashRev = _SbCfgStoreFlashRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 25),
    _SbCfgStoreFlashRev_Type()
)
sbCfgStoreFlashRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgStoreFlashRev.setStatus("mandatory")


class _SbCfgExecFlashRev_Type(DisplayString):
    """Custom type sbCfgExecFlashRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbCfgExecFlashRev_Type.__name__ = "DisplayString"
_SbCfgExecFlashRev_Object = MibScalar
sbCfgExecFlashRev = _SbCfgExecFlashRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 1, 26),
    _SbCfgExecFlashRev_Type()
)
sbCfgExecFlashRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbCfgExecFlashRev.setStatus("mandatory")
_SbPort_ObjectIdentity = ObjectIdentity
sbPort = _SbPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3)
)
_SbPortTable_Object = MibTable
sbPortTable = _SbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    sbPortTable.setStatus("mandatory")
_SbPortEntry_Object = MibTableRow
sbPortEntry = _SbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1)
)
sbPortEntry.setIndexNames(
    (0, "ARTEL-MIB", "sbPortIndex"),
)
if mibBuilder.loadTexts:
    sbPortEntry.setStatus("mandatory")


class _SbPortIndex_Type(Integer32):
    """Custom type sbPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SbPortIndex_Type.__name__ = "Integer32"
_SbPortIndex_Object = MibTableColumn
sbPortIndex = _SbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 1),
    _SbPortIndex_Type()
)
sbPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortIndex.setStatus("mandatory")
_SbPortRxMulticastFrames_Type = Counter32
_SbPortRxMulticastFrames_Object = MibTableColumn
sbPortRxMulticastFrames = _SbPortRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 2),
    _SbPortRxMulticastFrames_Type()
)
sbPortRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortRxMulticastFrames.setStatus("mandatory")
_SbPortRxBroadcastFrames_Type = Counter32
_SbPortRxBroadcastFrames_Object = MibTableColumn
sbPortRxBroadcastFrames = _SbPortRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 3),
    _SbPortRxBroadcastFrames_Type()
)
sbPortRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortRxBroadcastFrames.setStatus("mandatory")
_SbPortRxRuntErrors_Type = Counter32
_SbPortRxRuntErrors_Object = MibTableColumn
sbPortRxRuntErrors = _SbPortRxRuntErrors_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 5),
    _SbPortRxRuntErrors_Type()
)
sbPortRxRuntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortRxRuntErrors.setStatus("mandatory")
_SbPortRxBytes_Type = Counter32
_SbPortRxBytes_Object = MibTableColumn
sbPortRxBytes = _SbPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 6),
    _SbPortRxBytes_Type()
)
sbPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortRxBytes.setStatus("mandatory")
_SbPortTxBytes_Type = Counter32
_SbPortTxBytes_Object = MibTableColumn
sbPortTxBytes = _SbPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 7),
    _SbPortTxBytes_Type()
)
sbPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortTxBytes.setStatus("mandatory")


class _SbPortRxBroadcastStatus_Type(Integer32):
    """Custom type sbPortRxBroadcastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SbPortRxBroadcastStatus_Type.__name__ = "Integer32"
_SbPortRxBroadcastStatus_Object = MibTableColumn
sbPortRxBroadcastStatus = _SbPortRxBroadcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 8),
    _SbPortRxBroadcastStatus_Type()
)
sbPortRxBroadcastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPortRxBroadcastStatus.setStatus("mandatory")


class _SbPortName_Type(DisplayString):
    """Custom type sbPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbPortName_Type.__name__ = "DisplayString"
_SbPortName_Object = MibTableColumn
sbPortName = _SbPortName_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 9),
    _SbPortName_Type()
)
sbPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPortName.setStatus("mandatory")
_SbPortUtilization_Type = Gauge32
_SbPortUtilization_Object = MibTableColumn
sbPortUtilization = _SbPortUtilization_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 10),
    _SbPortUtilization_Type()
)
sbPortUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortUtilization.setStatus("mandatory")
_SbPortFramesPerSecond_Type = Gauge32
_SbPortFramesPerSecond_Object = MibTableColumn
sbPortFramesPerSecond = _SbPortFramesPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 11),
    _SbPortFramesPerSecond_Type()
)
sbPortFramesPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortFramesPerSecond.setStatus("mandatory")
_SbPortErrorRate_Type = Gauge32
_SbPortErrorRate_Object = MibTableColumn
sbPortErrorRate = _SbPortErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 12),
    _SbPortErrorRate_Type()
)
sbPortErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortErrorRate.setStatus("mandatory")
_SbPortInitStats_Type = Integer32
_SbPortInitStats_Object = MibTableColumn
sbPortInitStats = _SbPortInitStats_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 1, 1, 13),
    _SbPortInitStats_Type()
)
sbPortInitStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPortInitStats.setStatus("mandatory")
_SbPortUnidirectTable_Object = MibTable
sbPortUnidirectTable = _SbPortUnidirectTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 2)
)
if mibBuilder.loadTexts:
    sbPortUnidirectTable.setStatus("mandatory")
_SbPortUnidirectEntry_Object = MibTableRow
sbPortUnidirectEntry = _SbPortUnidirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 2, 1)
)
sbPortUnidirectEntry.setIndexNames(
    (0, "ARTEL-MIB", "sbPortUnidirectIndex"),
)
if mibBuilder.loadTexts:
    sbPortUnidirectEntry.setStatus("mandatory")


class _SbPortUnidirectIndex_Type(Integer32):
    """Custom type sbPortUnidirectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SbPortUnidirectIndex_Type.__name__ = "Integer32"
_SbPortUnidirectIndex_Object = MibTableColumn
sbPortUnidirectIndex = _SbPortUnidirectIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 2, 1, 1),
    _SbPortUnidirectIndex_Type()
)
sbPortUnidirectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPortUnidirectIndex.setStatus("mandatory")


class _SbPortUnidirectEnable_Type(Integer32):
    """Custom type sbPortUnidirectEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SbPortUnidirectEnable_Type.__name__ = "Integer32"
_SbPortUnidirectEnable_Object = MibTableColumn
sbPortUnidirectEnable = _SbPortUnidirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 6, 3, 2, 1, 2),
    _SbPortUnidirectEnable_Type()
)
sbPortUnidirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPortUnidirectEnable.setStatus("mandatory")
_Fddi_ObjectIdentity = ObjectIdentity
fddi = _Fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 7)
)
_FddiConfiguration_ObjectIdentity = ObjectIdentity
fddiConfiguration = _FddiConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1)
)


class _FddiCfgManufactureDate_Type(DisplayString):
    """Custom type fddiCfgManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgManufactureDate_Type.__name__ = "DisplayString"
_FddiCfgManufactureDate_Object = MibScalar
fddiCfgManufactureDate = _FddiCfgManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 1),
    _FddiCfgManufactureDate_Type()
)
fddiCfgManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgManufactureDate.setStatus("mandatory")


class _FddiCfgType_Type(Integer32):
    """Custom type fddiCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("fddi-board", 4)
    )


_FddiCfgType_Type.__name__ = "Integer32"
_FddiCfgType_Object = MibScalar
fddiCfgType = _FddiCfgType_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 2),
    _FddiCfgType_Type()
)
fddiCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgType.setStatus("mandatory")


class _FddiCfgHardwareRev_Type(DisplayString):
    """Custom type fddiCfgHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgHardwareRev_Type.__name__ = "DisplayString"
_FddiCfgHardwareRev_Object = MibScalar
fddiCfgHardwareRev = _FddiCfgHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 3),
    _FddiCfgHardwareRev_Type()
)
fddiCfgHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgHardwareRev.setStatus("mandatory")


class _FddiCfgSerialNumber_Type(DisplayString):
    """Custom type fddiCfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgSerialNumber_Type.__name__ = "DisplayString"
_FddiCfgSerialNumber_Object = MibScalar
fddiCfgSerialNumber = _FddiCfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 4),
    _FddiCfgSerialNumber_Type()
)
fddiCfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgSerialNumber.setStatus("mandatory")
_FddiCfgNumberFddiPorts_Type = Integer32
_FddiCfgNumberFddiPorts_Object = MibScalar
fddiCfgNumberFddiPorts = _FddiCfgNumberFddiPorts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 5),
    _FddiCfgNumberFddiPorts_Type()
)
fddiCfgNumberFddiPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgNumberFddiPorts.setStatus("mandatory")


class _FddiCfgPPFType_Type(DisplayString):
    """Custom type fddiCfgPPFType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgPPFType_Type.__name__ = "DisplayString"
_FddiCfgPPFType_Object = MibScalar
fddiCfgPPFType = _FddiCfgPPFType_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 6),
    _FddiCfgPPFType_Type()
)
fddiCfgPPFType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgPPFType.setStatus("mandatory")


class _FddiCfgPPFRev_Type(DisplayString):
    """Custom type fddiCfgPPFRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgPPFRev_Type.__name__ = "DisplayString"
_FddiCfgPPFRev_Object = MibScalar
fddiCfgPPFRev = _FddiCfgPPFRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 7),
    _FddiCfgPPFRev_Type()
)
fddiCfgPPFRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgPPFRev.setStatus("mandatory")


class _FddiCfgPPFSerialNumber_Type(DisplayString):
    """Custom type fddiCfgPPFSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgPPFSerialNumber_Type.__name__ = "DisplayString"
_FddiCfgPPFSerialNumber_Object = MibScalar
fddiCfgPPFSerialNumber = _FddiCfgPPFSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 8),
    _FddiCfgPPFSerialNumber_Type()
)
fddiCfgPPFSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgPPFSerialNumber.setStatus("mandatory")


class _FddiCfgMediaType_Type(DisplayString):
    """Custom type fddiCfgMediaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgMediaType_Type.__name__ = "DisplayString"
_FddiCfgMediaType_Object = MibScalar
fddiCfgMediaType = _FddiCfgMediaType_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 9),
    _FddiCfgMediaType_Type()
)
fddiCfgMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgMediaType.setStatus("mandatory")
_FddiCfgFlashMemorySize_Type = Integer32
_FddiCfgFlashMemorySize_Object = MibScalar
fddiCfgFlashMemorySize = _FddiCfgFlashMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 10),
    _FddiCfgFlashMemorySize_Type()
)
fddiCfgFlashMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgFlashMemorySize.setStatus("mandatory")
_FddiCfg68kRamSize_Type = Integer32
_FddiCfg68kRamSize_Object = MibScalar
fddiCfg68kRamSize = _FddiCfg68kRamSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 11),
    _FddiCfg68kRamSize_Type()
)
fddiCfg68kRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfg68kRamSize.setStatus("mandatory")
_FddiCfg960RamSize_Type = Integer32
_FddiCfg960RamSize_Object = MibScalar
fddiCfg960RamSize = _FddiCfg960RamSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 12),
    _FddiCfg960RamSize_Type()
)
fddiCfg960RamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfg960RamSize.setStatus("mandatory")
_FddiCfgSonicRamSize_Type = Integer32
_FddiCfgSonicRamSize_Object = MibScalar
fddiCfgSonicRamSize = _FddiCfgSonicRamSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 13),
    _FddiCfgSonicRamSize_Type()
)
fddiCfgSonicRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgSonicRamSize.setStatus("mandatory")
_FddiCfgHasherCacheTagSize_Type = Integer32
_FddiCfgHasherCacheTagSize_Object = MibScalar
fddiCfgHasherCacheTagSize = _FddiCfgHasherCacheTagSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 14),
    _FddiCfgHasherCacheTagSize_Type()
)
fddiCfgHasherCacheTagSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgHasherCacheTagSize.setStatus("mandatory")
_FddiCfgDualPortRamSize_Type = Integer32
_FddiCfgDualPortRamSize_Object = MibScalar
fddiCfgDualPortRamSize = _FddiCfgDualPortRamSize_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 15),
    _FddiCfgDualPortRamSize_Type()
)
fddiCfgDualPortRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgDualPortRamSize.setStatus("mandatory")


class _FddiCfgBootRev_Type(DisplayString):
    """Custom type fddiCfgBootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgBootRev_Type.__name__ = "DisplayString"
_FddiCfgBootRev_Object = MibScalar
fddiCfgBootRev = _FddiCfgBootRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 16),
    _FddiCfgBootRev_Type()
)
fddiCfgBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgBootRev.setStatus("mandatory")


class _FddiCfg68kRev_Type(DisplayString):
    """Custom type fddiCfg68kRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfg68kRev_Type.__name__ = "DisplayString"
_FddiCfg68kRev_Object = MibScalar
fddiCfg68kRev = _FddiCfg68kRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 17),
    _FddiCfg68kRev_Type()
)
fddiCfg68kRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfg68kRev.setStatus("mandatory")


class _FddiCfg960Rev_Type(DisplayString):
    """Custom type fddiCfg960Rev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfg960Rev_Type.__name__ = "DisplayString"
_FddiCfg960Rev_Object = MibScalar
fddiCfg960Rev = _FddiCfg960Rev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 18),
    _FddiCfg960Rev_Type()
)
fddiCfg960Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfg960Rev.setStatus("mandatory")


class _FddiCfgPPFSoftwareRev_Type(DisplayString):
    """Custom type fddiCfgPPFSoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgPPFSoftwareRev_Type.__name__ = "DisplayString"
_FddiCfgPPFSoftwareRev_Object = MibScalar
fddiCfgPPFSoftwareRev = _FddiCfgPPFSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 19),
    _FddiCfgPPFSoftwareRev_Type()
)
fddiCfgPPFSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgPPFSoftwareRev.setStatus("mandatory")


class _FddiCfgModulePartNumber_Type(DisplayString):
    """Custom type fddiCfgModulePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgModulePartNumber_Type.__name__ = "DisplayString"
_FddiCfgModulePartNumber_Object = MibScalar
fddiCfgModulePartNumber = _FddiCfgModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 20),
    _FddiCfgModulePartNumber_Type()
)
fddiCfgModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgModulePartNumber.setStatus("mandatory")


class _FddiCfgModuleSerialNumber_Type(DisplayString):
    """Custom type fddiCfgModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgModuleSerialNumber_Type.__name__ = "DisplayString"
_FddiCfgModuleSerialNumber_Object = MibScalar
fddiCfgModuleSerialNumber = _FddiCfgModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 21),
    _FddiCfgModuleSerialNumber_Type()
)
fddiCfgModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgModuleSerialNumber.setStatus("mandatory")


class _FddiCfgStoreFlashRev_Type(DisplayString):
    """Custom type fddiCfgStoreFlashRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgStoreFlashRev_Type.__name__ = "DisplayString"
_FddiCfgStoreFlashRev_Object = MibScalar
fddiCfgStoreFlashRev = _FddiCfgStoreFlashRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 22),
    _FddiCfgStoreFlashRev_Type()
)
fddiCfgStoreFlashRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgStoreFlashRev.setStatus("mandatory")


class _FddiCfgExecFlashRev_Type(DisplayString):
    """Custom type fddiCfgExecFlashRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FddiCfgExecFlashRev_Type.__name__ = "DisplayString"
_FddiCfgExecFlashRev_Object = MibScalar
fddiCfgExecFlashRev = _FddiCfgExecFlashRev_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 1, 23),
    _FddiCfgExecFlashRev_Type()
)
fddiCfgExecFlashRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiCfgExecFlashRev.setStatus("mandatory")
_FddiIpFragmentation_ObjectIdentity = ObjectIdentity
fddiIpFragmentation = _FddiIpFragmentation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 2)
)


class _FddiIpFragEnabled_Type(Integer32):
    """Custom type fddiIpFragEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FddiIpFragEnabled_Type.__name__ = "Integer32"
_FddiIpFragEnabled_Object = MibScalar
fddiIpFragEnabled = _FddiIpFragEnabled_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 2, 1),
    _FddiIpFragEnabled_Type()
)
fddiIpFragEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddiIpFragEnabled.setStatus("mandatory")
_FddiPort_ObjectIdentity = ObjectIdentity
fddiPort = _FddiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 3)
)
_FddiPortTable_Object = MibTable
fddiPortTable = _FddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    fddiPortTable.setStatus("mandatory")
_FddiPortEntry_Object = MibTableRow
fddiPortEntry = _FddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 3, 1, 1)
)
fddiPortEntry.setIndexNames(
    (0, "ARTEL-MIB", "fddiPortIndex"),
)
if mibBuilder.loadTexts:
    fddiPortEntry.setStatus("mandatory")


class _FddiPortIndex_Type(Integer32):
    """Custom type fddiPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_FddiPortIndex_Type.__name__ = "Integer32"
_FddiPortIndex_Object = MibTableColumn
fddiPortIndex = _FddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 3, 1, 1, 1),
    _FddiPortIndex_Type()
)
fddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiPortIndex.setStatus("mandatory")


class _FddiPortRxMcastEnabled_Type(Integer32):
    """Custom type fddiPortRxMcastEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FddiPortRxMcastEnabled_Type.__name__ = "Integer32"
_FddiPortRxMcastEnabled_Object = MibTableColumn
fddiPortRxMcastEnabled = _FddiPortRxMcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 3, 1, 1, 2),
    _FddiPortRxMcastEnabled_Type()
)
fddiPortRxMcastEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiPortRxMcastEnabled.setStatus("mandatory")
_FddiPortNotCopiedOffRingErrs_Type = Counter32
_FddiPortNotCopiedOffRingErrs_Object = MibTableColumn
fddiPortNotCopiedOffRingErrs = _FddiPortNotCopiedOffRingErrs_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 3, 1, 1, 3),
    _FddiPortNotCopiedOffRingErrs_Type()
)
fddiPortNotCopiedOffRingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiPortNotCopiedOffRingErrs.setStatus("mandatory")
_FddiPortRingOpCounts_Type = Counter32
_FddiPortRingOpCounts_Object = MibTableColumn
fddiPortRingOpCounts = _FddiPortRingOpCounts_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 3, 1, 1, 4),
    _FddiPortRingOpCounts_Type()
)
fddiPortRingOpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiPortRingOpCounts.setStatus("mandatory")
_FddiPortFrameCheckErrs_Type = Counter32
_FddiPortFrameCheckErrs_Object = MibTableColumn
fddiPortFrameCheckErrs = _FddiPortFrameCheckErrs_Object(
    (1, 3, 6, 1, 4, 1, 139, 2, 7, 3, 1, 1, 5),
    _FddiPortFrameCheckErrs_Type()
)
fddiPortFrameCheckErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiPortFrameCheckErrs.setStatus("mandatory")
_ArtelTrap_ObjectIdentity = ObjectIdentity
artelTrap = _ArtelTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 139, 64)
)
_ArtelTrapAddrTable_Object = MibTable
artelTrapAddrTable = _ArtelTrapAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 139, 64, 1)
)
if mibBuilder.loadTexts:
    artelTrapAddrTable.setStatus("mandatory")
_ArtelTrapAddrEntry_Object = MibTableRow
artelTrapAddrEntry = _ArtelTrapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 139, 64, 1, 1)
)
artelTrapAddrEntry.setIndexNames(
    (0, "ARTEL-MIB", "artelTrapAddrIpDest"),
    (0, "ARTEL-MIB", "artelTrapAddrXPortIndex"),
)
if mibBuilder.loadTexts:
    artelTrapAddrEntry.setStatus("mandatory")
_ArtelTrapAddrIpDest_Type = IpAddress
_ArtelTrapAddrIpDest_Object = MibTableColumn
artelTrapAddrIpDest = _ArtelTrapAddrIpDest_Object(
    (1, 3, 6, 1, 4, 1, 139, 64, 1, 1, 1),
    _ArtelTrapAddrIpDest_Type()
)
artelTrapAddrIpDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artelTrapAddrIpDest.setStatus("mandatory")


class _ArtelTrapAddrXPortIndex_Type(OctetString):
    """Custom type artelTrapAddrXPortIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ArtelTrapAddrXPortIndex_Type.__name__ = "OctetString"
_ArtelTrapAddrXPortIndex_Object = MibTableColumn
artelTrapAddrXPortIndex = _ArtelTrapAddrXPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 139, 64, 1, 1, 2),
    _ArtelTrapAddrXPortIndex_Type()
)
artelTrapAddrXPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artelTrapAddrXPortIndex.setStatus("mandatory")
_ArtelTrapAddrUdpDest_Type = Integer32
_ArtelTrapAddrUdpDest_Object = MibTableColumn
artelTrapAddrUdpDest = _ArtelTrapAddrUdpDest_Object(
    (1, 3, 6, 1, 4, 1, 139, 64, 1, 1, 3),
    _ArtelTrapAddrUdpDest_Type()
)
artelTrapAddrUdpDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artelTrapAddrUdpDest.setStatus("mandatory")


class _ArtelTrapAddrCommunity_Type(OctetString):
    """Custom type artelTrapAddrCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArtelTrapAddrCommunity_Type.__name__ = "OctetString"
_ArtelTrapAddrCommunity_Object = MibTableColumn
artelTrapAddrCommunity = _ArtelTrapAddrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 139, 64, 1, 1, 4),
    _ArtelTrapAddrCommunity_Type()
)
artelTrapAddrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artelTrapAddrCommunity.setStatus("mandatory")


class _ArtelTrapAddrStatus_Type(Integer32):
    """Custom type artelTrapAddrStatus based on Integer32"""
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
        *(("invalid", 2),
          ("other", 1),
          ("permanent", 3),
          ("temporary", 4))
    )


_ArtelTrapAddrStatus_Type.__name__ = "Integer32"
_ArtelTrapAddrStatus_Object = MibTableColumn
artelTrapAddrStatus = _ArtelTrapAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 139, 64, 1, 1, 5),
    _ArtelTrapAddrStatus_Type()
)
artelTrapAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artelTrapAddrStatus.setStatus("mandatory")


class _ArtelTrapReportString_Type(DisplayString):
    """Custom type artelTrapReportString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArtelTrapReportString_Type.__name__ = "DisplayString"
_ArtelTrapReportString_Object = MibScalar
artelTrapReportString = _ArtelTrapReportString_Object(
    (1, 3, 6, 1, 4, 1, 139, 64, 2),
    _ArtelTrapReportString_Type()
)
artelTrapReportString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artelTrapReportString.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARTEL-MIB",
    **{"artel": artel,
       "node": node,
       "nodeName": nodeName,
       "nodeMacSlotMap": nodeMacSlotMap,
       "nodeColdBoot": nodeColdBoot,
       "nodeResetNvRam": nodeResetNvRam,
       "nodeIpSlotTable": nodeIpSlotTable,
       "nodeIpSlotEntry": nodeIpSlotEntry,
       "nodeIpSlotIndex": nodeIpSlotIndex,
       "nodeIpSlotAddr": nodeIpSlotAddr,
       "galactica": galactica,
       "board": board,
       "boardIpAddr": boardIpAddr,
       "boardReset": boardReset,
       "boardResetNvRam": boardResetNvRam,
       "boardLedStatus": boardLedStatus,
       "boardSlotNum": boardSlotNum,
       "boardClass": boardClass,
       "boardResetCounts": boardResetCounts,
       "boardSnmpMibVersion": boardSnmpMibVersion,
       "arcnet": arcnet,
       "arcnetBoardsPresent": arcnetBoardsPresent,
       "arcnetRxPkts": arcnetRxPkts,
       "arcnetTxPkts": arcnetTxPkts,
       "arcnetNakCnts": arcnetNakCnts,
       "arcnetMyReconfigCounts": arcnetMyReconfigCounts,
       "arcnetReconfigCounts": arcnetReconfigCounts,
       "arcnetTrashedRxMsgs": arcnetTrashedRxMsgs,
       "arcnetTrashedTxMsgs": arcnetTrashedTxMsgs,
       "backplane": backplane,
       "bpStatsEnabled": bpStatsEnabled,
       "bpStatsRxPkts": bpStatsRxPkts,
       "bpStatsRxErrors": bpStatsRxErrors,
       "bpStatsTxPkts": bpStatsTxPkts,
       "bpStatsTxErrors": bpStatsTxErrors,
       "bpStatsOperState": bpStatsOperState,
       "bpStatsInitialize": bpStatsInitialize,
       "bpStatsTxQOverErrors": bpStatsTxQOverErrors,
       "bpStatsRxBusyTable": bpStatsRxBusyTable,
       "bpStatsRxBusyTableEntry": bpStatsRxBusyTableEntry,
       "bpStatsRxBusyTableIndex": bpStatsRxBusyTableIndex,
       "bpStatsRxBusyTableErrors": bpStatsRxBusyTableErrors,
       "bridge": bridge,
       "restrictedTable": restrictedTable,
       "restrictedEntry": restrictedEntry,
       "restrictedAddr": restrictedAddr,
       "restrictedStatus": restrictedStatus,
       "bridgeAgeNow": bridgeAgeNow,
       "bridgeDot1dEnable": bridgeDot1dEnable,
       "bridgeDot1dResetDefaults": bridgeDot1dResetDefaults,
       "bridgeResetPktSwCount": bridgeResetPktSwCount,
       "bridgePktSwLastReset": bridgePktSwLastReset,
       "bridgeResetStatic": bridgeResetStatic,
       "bridgeRestrictedReset": bridgeRestrictedReset,
       "bridgeUdfTable": bridgeUdfTable,
       "bridgeUdfEntry": bridgeUdfEntry,
       "bridgeUdfPortIndex": bridgeUdfPortIndex,
       "bridgeUdfFilterIndex": bridgeUdfFilterIndex,
       "bridgeUdfState": bridgeUdfState,
       "bridgeUdfComment": bridgeUdfComment,
       "bridgeUdfMatchCounts": bridgeUdfMatchCounts,
       "bridgeUdfInitMatchCount": bridgeUdfInitMatchCount,
       "bridgeUdfAddressType": bridgeUdfAddressType,
       "bridgeUdfAddressValue": bridgeUdfAddressValue,
       "bridgeUdfAddressMask": bridgeUdfAddressMask,
       "bridgeUdfAddressOperand": bridgeUdfAddressOperand,
       "bridgeUdfTypeValue": bridgeUdfTypeValue,
       "bridgeUdfTypeMask": bridgeUdfTypeMask,
       "bridgeUdfTypeOperand": bridgeUdfTypeOperand,
       "bridgeUdfOffset1Offset": bridgeUdfOffset1Offset,
       "bridgeUdfOffset1Value": bridgeUdfOffset1Value,
       "bridgeUdfOffset1Mask": bridgeUdfOffset1Mask,
       "bridgeUdfOffset1Operand": bridgeUdfOffset1Operand,
       "bridgeUdfOffset2Offset": bridgeUdfOffset2Offset,
       "bridgeUdfOffset2Value": bridgeUdfOffset2Value,
       "bridgeUdfOffset2Mask": bridgeUdfOffset2Mask,
       "bridgeUdfOffset2Operand": bridgeUdfOffset2Operand,
       "bridgeUdfOffset3Offset": bridgeUdfOffset3Offset,
       "bridgeUdfOffset3Value": bridgeUdfOffset3Value,
       "bridgeUdfOffset3Mask": bridgeUdfOffset3Mask,
       "bridgeUdfOffset3Operand": bridgeUdfOffset3Operand,
       "bridgeUdfOffset4Offset": bridgeUdfOffset4Offset,
       "bridgeUdfOffset4Value": bridgeUdfOffset4Value,
       "bridgeUdfOffset4Mask": bridgeUdfOffset4Mask,
       "bridgeUdfOffset4Operand": bridgeUdfOffset4Operand,
       "bridgeUdfInitCountTable": bridgeUdfInitCountTable,
       "bridgeUdfInitCountEntry": bridgeUdfInitCountEntry,
       "bridgeUdfCountPortIndex": bridgeUdfCountPortIndex,
       "bridgeUdfCountInitMatchCount": bridgeUdfCountInitMatchCount,
       "bridgePortGroupEnable": bridgePortGroupEnable,
       "bridgePortGroupTable": bridgePortGroupTable,
       "bridgePortGroupEntry": bridgePortGroupEntry,
       "bridgePortGroupTablePortIndex": bridgePortGroupTablePortIndex,
       "bridgePortGroupTableGroupIndex": bridgePortGroupTableGroupIndex,
       "bridgePortGroupTableEnable": bridgePortGroupTableEnable,
       "bridgePortGroupPortTable": bridgePortGroupPortTable,
       "bridgePortGroupPortEntry": bridgePortGroupPortEntry,
       "bridgePortGroupPortIndex": bridgePortGroupPortIndex,
       "bridgePortGroupPortDisplayString": bridgePortGroupPortDisplayString,
       "bridgePortGroupGroupTable": bridgePortGroupGroupTable,
       "bridgePortGroupGroupEntry": bridgePortGroupGroupEntry,
       "bridgePortGroupGroupIndex": bridgePortGroupGroupIndex,
       "bridgePortGroupGroupPortMap": bridgePortGroupGroupPortMap,
       "bridgePortGroupGroupComment": bridgePortGroupGroupComment,
       "bridgeAddrFilterTable": bridgeAddrFilterTable,
       "bridgeAddrFilterEntry": bridgeAddrFilterEntry,
       "bridgeAddrFilterBlockIndex": bridgeAddrFilterBlockIndex,
       "bridgeAddrFilterBlockData": bridgeAddrFilterBlockData,
       "bridgedot1dTpFdbTable": bridgedot1dTpFdbTable,
       "bridgedot1dTpFdbEntry": bridgedot1dTpFdbEntry,
       "bridgedot1dTpFdbAddress": bridgedot1dTpFdbAddress,
       "bridgedot1dTpFdbSlot": bridgedot1dTpFdbSlot,
       "bridgedot1dTpFdbPort": bridgedot1dTpFdbPort,
       "bridgedot1dTpFdbStatus": bridgedot1dTpFdbStatus,
       "bridgedot1dTpFdbAge": bridgedot1dTpFdbAge,
       "systemManagement": systemManagement,
       "smConfiguration": smConfiguration,
       "smCfgManufactureDate": smCfgManufactureDate,
       "smCfgType": smCfgType,
       "smCfgHardwareRev": smCfgHardwareRev,
       "smCfgSerialNumber": smCfgSerialNumber,
       "smCfgMacAddr": smCfgMacAddr,
       "smCfgFlashMemSize": smCfgFlashMemSize,
       "smCfg68kRamSize": smCfg68kRamSize,
       "smCfgBootRev": smCfgBootRev,
       "smCfg68kRev": smCfg68kRev,
       "smCfgModulePartNumber": smCfgModulePartNumber,
       "smCfgModuleSerialNumber": smCfgModuleSerialNumber,
       "smCfgStoreFlashRev": smCfgStoreFlashRev,
       "smCfgExecFlashRev": smCfgExecFlashRev,
       "smBackplane": smBackplane,
       "smBpType": smBpType,
       "smBpArbTimer": smBpArbTimer,
       "smBpMaxPktSize": smBpMaxPktSize,
       "smBpAsyncSlotsEnb": smBpAsyncSlotsEnb,
       "smBpSyncSlotsEnb": smBpSyncSlotsEnb,
       "smBpUtilization": smBpUtilization,
       "smBpTable": smBpTable,
       "smBpEntry": smBpEntry,
       "smBpIndex": smBpIndex,
       "smBpTableEnable": smBpTableEnable,
       "smBpTableJabber": smBpTableJabber,
       "smBpTableClearJabber": smBpTableClearJabber,
       "smPowerSupply": smPowerSupply,
       "smSupplyPresent": smSupplyPresent,
       "smSupplyType": smSupplyType,
       "smSupplyAcOk": smSupplyAcOk,
       "smSupplyDcOk": smSupplyDcOk,
       "smSupplyTable": smSupplyTable,
       "smSupplyTableEntry": smSupplyTableEntry,
       "smSupplyTableIndex": smSupplyTableIndex,
       "smSupplyTableStatus": smSupplyTableStatus,
       "smModem": smModem,
       "smModemType": smModemType,
       "smModemCallBackEnable": smModemCallBackEnable,
       "smModemCallBackNumber": smModemCallBackNumber,
       "starbridge": starbridge,
       "sbConfiguration": sbConfiguration,
       "sbCfgManufactureDate": sbCfgManufactureDate,
       "sbCfgType": sbCfgType,
       "sbCfgHardwareRev": sbCfgHardwareRev,
       "sbCfgSerialNumber": sbCfgSerialNumber,
       "sbCfgNumberIfBoards": sbCfgNumberIfBoards,
       "sbCfgIfBd1Type": sbCfgIfBd1Type,
       "sbCfgIfBd1Rev": sbCfgIfBd1Rev,
       "sbCfgIfBd1SerialNum": sbCfgIfBd1SerialNum,
       "sbCfgIfBd1NumPorts": sbCfgIfBd1NumPorts,
       "sbCfgIfBd2Type": sbCfgIfBd2Type,
       "sbCfgIfBd2Rev": sbCfgIfBd2Rev,
       "sbCfgIfBd2SerialNum": sbCfgIfBd2SerialNum,
       "sbCfgIfBd2NumPorts": sbCfgIfBd2NumPorts,
       "sbCfgFlashMemorySize": sbCfgFlashMemorySize,
       "sbCfg68kRamSize": sbCfg68kRamSize,
       "sbCfg960RamSize": sbCfg960RamSize,
       "sbCfgSonicRamSize": sbCfgSonicRamSize,
       "sbCfgHasherCacheTagSize": sbCfgHasherCacheTagSize,
       "sbCfgDualPortRamSize": sbCfgDualPortRamSize,
       "sbCfgBootRev": sbCfgBootRev,
       "sbCfg68kRev": sbCfg68kRev,
       "sbCfg960Rev": sbCfg960Rev,
       "sbCfgModulePartNumber": sbCfgModulePartNumber,
       "sbCfgModuleSerialNumber": sbCfgModuleSerialNumber,
       "sbCfgStoreFlashRev": sbCfgStoreFlashRev,
       "sbCfgExecFlashRev": sbCfgExecFlashRev,
       "sbPort": sbPort,
       "sbPortTable": sbPortTable,
       "sbPortEntry": sbPortEntry,
       "sbPortIndex": sbPortIndex,
       "sbPortRxMulticastFrames": sbPortRxMulticastFrames,
       "sbPortRxBroadcastFrames": sbPortRxBroadcastFrames,
       "sbPortRxRuntErrors": sbPortRxRuntErrors,
       "sbPortRxBytes": sbPortRxBytes,
       "sbPortTxBytes": sbPortTxBytes,
       "sbPortRxBroadcastStatus": sbPortRxBroadcastStatus,
       "sbPortName": sbPortName,
       "sbPortUtilization": sbPortUtilization,
       "sbPortFramesPerSecond": sbPortFramesPerSecond,
       "sbPortErrorRate": sbPortErrorRate,
       "sbPortInitStats": sbPortInitStats,
       "sbPortUnidirectTable": sbPortUnidirectTable,
       "sbPortUnidirectEntry": sbPortUnidirectEntry,
       "sbPortUnidirectIndex": sbPortUnidirectIndex,
       "sbPortUnidirectEnable": sbPortUnidirectEnable,
       "fddi": fddi,
       "fddiConfiguration": fddiConfiguration,
       "fddiCfgManufactureDate": fddiCfgManufactureDate,
       "fddiCfgType": fddiCfgType,
       "fddiCfgHardwareRev": fddiCfgHardwareRev,
       "fddiCfgSerialNumber": fddiCfgSerialNumber,
       "fddiCfgNumberFddiPorts": fddiCfgNumberFddiPorts,
       "fddiCfgPPFType": fddiCfgPPFType,
       "fddiCfgPPFRev": fddiCfgPPFRev,
       "fddiCfgPPFSerialNumber": fddiCfgPPFSerialNumber,
       "fddiCfgMediaType": fddiCfgMediaType,
       "fddiCfgFlashMemorySize": fddiCfgFlashMemorySize,
       "fddiCfg68kRamSize": fddiCfg68kRamSize,
       "fddiCfg960RamSize": fddiCfg960RamSize,
       "fddiCfgSonicRamSize": fddiCfgSonicRamSize,
       "fddiCfgHasherCacheTagSize": fddiCfgHasherCacheTagSize,
       "fddiCfgDualPortRamSize": fddiCfgDualPortRamSize,
       "fddiCfgBootRev": fddiCfgBootRev,
       "fddiCfg68kRev": fddiCfg68kRev,
       "fddiCfg960Rev": fddiCfg960Rev,
       "fddiCfgPPFSoftwareRev": fddiCfgPPFSoftwareRev,
       "fddiCfgModulePartNumber": fddiCfgModulePartNumber,
       "fddiCfgModuleSerialNumber": fddiCfgModuleSerialNumber,
       "fddiCfgStoreFlashRev": fddiCfgStoreFlashRev,
       "fddiCfgExecFlashRev": fddiCfgExecFlashRev,
       "fddiIpFragmentation": fddiIpFragmentation,
       "fddiIpFragEnabled": fddiIpFragEnabled,
       "fddiPort": fddiPort,
       "fddiPortTable": fddiPortTable,
       "fddiPortEntry": fddiPortEntry,
       "fddiPortIndex": fddiPortIndex,
       "fddiPortRxMcastEnabled": fddiPortRxMcastEnabled,
       "fddiPortNotCopiedOffRingErrs": fddiPortNotCopiedOffRingErrs,
       "fddiPortRingOpCounts": fddiPortRingOpCounts,
       "fddiPortFrameCheckErrs": fddiPortFrameCheckErrs,
       "artelTrap": artelTrap,
       "artelTrapAddrTable": artelTrapAddrTable,
       "artelTrapAddrEntry": artelTrapAddrEntry,
       "artelTrapAddrIpDest": artelTrapAddrIpDest,
       "artelTrapAddrXPortIndex": artelTrapAddrXPortIndex,
       "artelTrapAddrUdpDest": artelTrapAddrUdpDest,
       "artelTrapAddrCommunity": artelTrapAddrCommunity,
       "artelTrapAddrStatus": artelTrapAddrStatus,
       "artelTrapReportString": artelTrapReportString}
)
