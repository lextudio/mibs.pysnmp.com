# SNMP MIB module (LS100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LS100-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:23 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_Atomis_mib_ObjectIdentity = ObjectIdentity
atomis_mib = _Atomis_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14)
)
_M5core_mib_ObjectIdentity = ObjectIdentity
m5core_mib = _M5core_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3)
)
_Node_ObjectIdentity = ObjectIdentity
node = _Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1)
)


class _NodeOperStatus_Type(Integer32):
    """Custom type nodeOperStatus based on Integer32"""
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
        *(("active", 2),
          ("down", 1),
          ("initializing", 5),
          ("offLine", 3),
          ("testing", 4))
    )


_NodeOperStatus_Type.__name__ = "Integer32"
_NodeOperStatus_Object = MibScalar
nodeOperStatus = _NodeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 1),
    _NodeOperStatus_Type()
)
nodeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOperStatus.setStatus("mandatory")
_NodeIfConfTable_Object = MibTable
nodeIfConfTable = _NodeIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2)
)
if mibBuilder.loadTexts:
    nodeIfConfTable.setStatus("mandatory")
_NodeIfConfEntry_Object = MibTableRow
nodeIfConfEntry = _NodeIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1)
)
nodeIfConfEntry.setIndexNames(
    (0, "LS100-MIB", "nodeIfConfIndex"),
)
if mibBuilder.loadTexts:
    nodeIfConfEntry.setStatus("mandatory")
_NodeIfConfIndex_Type = Integer32
_NodeIfConfIndex_Object = MibTableColumn
nodeIfConfIndex = _NodeIfConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1, 1),
    _NodeIfConfIndex_Type()
)
nodeIfConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIfConfIndex.setStatus("mandatory")


class _NodeIfConfPhysType_Type(Integer32):
    """Custom type nodeIfConfPhysType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ds3NoScramble", 10),
          ("ds3PlcpNoScramble", 7),
          ("ds3PlcpScramble", 6),
          ("ds3Scramble", 9),
          ("e3NoScramble", 14),
          ("e3PlcpNoScramble", 12),
          ("e3PlcpScramble", 11),
          ("e3Scramble", 13),
          ("leasedLine3M", 16),
          ("leasedLine4M", 17),
          ("leasedLine6M", 18),
          ("notInstalled", 99),
          ("oc3cMMF", 5),
          ("oc3cSMF", 4),
          ("oc3cSmfShaper", 20),
          ("other", 1),
          ("relay6Mcell", 8),
          ("sar", 2),
          ("taxi100M", 3),
          ("taxi140M", 21),
          ("utp5", 15),
          ("utp5classB", 19))
    )


_NodeIfConfPhysType_Type.__name__ = "Integer32"
_NodeIfConfPhysType_Object = MibTableColumn
nodeIfConfPhysType = _NodeIfConfPhysType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1, 2),
    _NodeIfConfPhysType_Type()
)
nodeIfConfPhysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIfConfPhysType.setStatus("mandatory")
_NodeIfConfRev_Type = DisplayString
_NodeIfConfRev_Object = MibTableColumn
nodeIfConfRev = _NodeIfConfRev_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1, 3),
    _NodeIfConfRev_Type()
)
nodeIfConfRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIfConfRev.setStatus("mandatory")


class _NodeIfConfStatus_Type(Integer32):
    """Custom type nodeIfConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("localLoopBack", 5),
          ("notInstalled", 99),
          ("other", 1),
          ("outOfService", 3),
          ("remoteLoopBack", 6),
          ("testing", 4))
    )


_NodeIfConfStatus_Type.__name__ = "Integer32"
_NodeIfConfStatus_Object = MibTableColumn
nodeIfConfStatus = _NodeIfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 2, 1, 4),
    _NodeIfConfStatus_Type()
)
nodeIfConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIfConfStatus.setStatus("mandatory")


class _NodeFanStatus_Type(Integer32):
    """Custom type nodeFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_NodeFanStatus_Type.__name__ = "Integer32"
_NodeFanStatus_Object = MibScalar
nodeFanStatus = _NodeFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 3),
    _NodeFanStatus_Type()
)
nodeFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFanStatus.setStatus("mandatory")


class _NodeUpcWindowSize_Type(Integer32):
    """Custom type nodeUpcWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_NodeUpcWindowSize_Type.__name__ = "Integer32"
_NodeUpcWindowSize_Object = MibScalar
nodeUpcWindowSize = _NodeUpcWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 4),
    _NodeUpcWindowSize_Type()
)
nodeUpcWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeUpcWindowSize.setStatus("mandatory")


class _NodeBestEffortBufferSize_Type(Integer32):
    """Custom type nodeBestEffortBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NodeBestEffortBufferSize_Type.__name__ = "Integer32"
_NodeBestEffortBufferSize_Object = MibScalar
nodeBestEffortBufferSize = _NodeBestEffortBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 5),
    _NodeBestEffortBufferSize_Type()
)
nodeBestEffortBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBestEffortBufferSize.setStatus("mandatory")


class _NodeGuaranteedBufferSize_Type(Integer32):
    """Custom type nodeGuaranteedBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NodeGuaranteedBufferSize_Type.__name__ = "Integer32"
_NodeGuaranteedBufferSize_Object = MibScalar
nodeGuaranteedBufferSize = _NodeGuaranteedBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 6),
    _NodeGuaranteedBufferSize_Type()
)
nodeGuaranteedBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeGuaranteedBufferSize.setStatus("mandatory")


class _NodeBestEffortBufferThreshold_Type(Integer32):
    """Custom type nodeBestEffortBufferThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NodeBestEffortBufferThreshold_Type.__name__ = "Integer32"
_NodeBestEffortBufferThreshold_Object = MibScalar
nodeBestEffortBufferThreshold = _NodeBestEffortBufferThreshold_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 7),
    _NodeBestEffortBufferThreshold_Type()
)
nodeBestEffortBufferThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeBestEffortBufferThreshold.setStatus("mandatory")


class _NodeGuaranteedBufferThreshold_Type(Integer32):
    """Custom type nodeGuaranteedBufferThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NodeGuaranteedBufferThreshold_Type.__name__ = "Integer32"
_NodeGuaranteedBufferThreshold_Object = MibScalar
nodeGuaranteedBufferThreshold = _NodeGuaranteedBufferThreshold_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 8),
    _NodeGuaranteedBufferThreshold_Type()
)
nodeGuaranteedBufferThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeGuaranteedBufferThreshold.setStatus("mandatory")


class _NodeSaveConf_Type(Integer32):
    """Custom type nodeSaveConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 2),
          ("save", 1))
    )


_NodeSaveConf_Type.__name__ = "Integer32"
_NodeSaveConf_Object = MibScalar
nodeSaveConf = _NodeSaveConf_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 9),
    _NodeSaveConf_Type()
)
nodeSaveConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSaveConf.setStatus("mandatory")


class _NodeSaveResult_Type(Integer32):
    """Custom type nodeSaveResult based on Integer32"""
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
        *(("nearend", 5),
          ("notReady", 2),
          ("ready", 3),
          ("success", 4),
          ("temporaryFailure", 1))
    )


_NodeSaveResult_Type.__name__ = "Integer32"
_NodeSaveResult_Object = MibScalar
nodeSaveResult = _NodeSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 10),
    _NodeSaveResult_Type()
)
nodeSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSaveResult.setStatus("mandatory")


class _NodeReset_Type(Integer32):
    """Custom type nodeReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 2),
          ("reset", 1))
    )


_NodeReset_Type.__name__ = "Integer32"
_NodeReset_Object = MibScalar
nodeReset = _NodeReset_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 11),
    _NodeReset_Type()
)
nodeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeReset.setStatus("mandatory")
_Linf_ObjectIdentity = ObjectIdentity
linf = _Linf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2)
)
_LinfStatusTable_Object = MibTable
linfStatusTable = _LinfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1)
)
if mibBuilder.loadTexts:
    linfStatusTable.setStatus("mandatory")
_LinfStatusEntry_Object = MibTableRow
linfStatusEntry = _LinfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1)
)
linfStatusEntry.setIndexNames(
    (0, "LS100-MIB", "linfIndex"),
)
if mibBuilder.loadTexts:
    linfStatusEntry.setStatus("mandatory")


class _LinfIndex_Type(Integer32):
    """Custom type linfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_LinfIndex_Type.__name__ = "Integer32"
_LinfIndex_Object = MibTableColumn
linfIndex = _LinfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1, 1),
    _LinfIndex_Type()
)
linfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfIndex.setStatus("mandatory")


class _LinfStatus_Type(Integer32):
    """Custom type linfStatus based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ais", 5),
          ("idle", 9),
          ("loc", 4),
          ("lof", 3),
          ("lop", 8),
          ("los", 2),
          ("maFERF", 13),
          ("normal", 1),
          ("notInstalled", 99),
          ("payloadAllOnes", 15),
          ("plcpLOF", 11),
          ("plcpYellow", 12),
          ("rai", 14),
          ("yellowAlarm", 10),
          ("yellowLine", 6),
          ("yellowPath", 7))
    )


_LinfStatus_Type.__name__ = "Integer32"
_LinfStatus_Object = MibTableColumn
linfStatus = _LinfStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1, 2),
    _LinfStatus_Type()
)
linfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfStatus.setStatus("mandatory")


class _LinfConf_Type(Integer32):
    """Custom type linfConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("others", 99),
          ("privateNNI", 3),
          ("privateUNI", 2),
          ("publicUNI", 1))
    )


_LinfConf_Type.__name__ = "Integer32"
_LinfConf_Object = MibTableColumn
linfConf = _LinfConf_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1, 3),
    _LinfConf_Type()
)
linfConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linfConf.setStatus("mandatory")
_LinfFwdAvailableBandWidth_Type = Integer32
_LinfFwdAvailableBandWidth_Object = MibTableColumn
linfFwdAvailableBandWidth = _LinfFwdAvailableBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1, 4),
    _LinfFwdAvailableBandWidth_Type()
)
linfFwdAvailableBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfFwdAvailableBandWidth.setStatus("mandatory")
_LinfBkwdAvailableBandWidth_Type = Integer32
_LinfBkwdAvailableBandWidth_Object = MibTableColumn
linfBkwdAvailableBandWidth = _LinfBkwdAvailableBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 2, 1, 1, 5),
    _LinfBkwdAvailableBandWidth_Type()
)
linfBkwdAvailableBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linfBkwdAvailableBandWidth.setStatus("mandatory")
_Conn_ObjectIdentity = ObjectIdentity
conn = _Conn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3)
)


class _ConnPvcIndexNext_Type(Integer32):
    """Custom type connPvcIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ConnPvcIndexNext_Type.__name__ = "Integer32"
_ConnPvcIndexNext_Object = MibScalar
connPvcIndexNext = _ConnPvcIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 1),
    _ConnPvcIndexNext_Type()
)
connPvcIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcIndexNext.setStatus("mandatory")


class _ConnPvcIndexEnable_Type(Integer32):
    """Custom type connPvcIndexEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ConnPvcIndexEnable_Type.__name__ = "Integer32"
_ConnPvcIndexEnable_Object = MibScalar
connPvcIndexEnable = _ConnPvcIndexEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 2),
    _ConnPvcIndexEnable_Type()
)
connPvcIndexEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcIndexEnable.setStatus("deprecated")
_ConnPvcTable_Object = MibTable
connPvcTable = _ConnPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3)
)
if mibBuilder.loadTexts:
    connPvcTable.setStatus("mandatory")
_ConnPvcEntry_Object = MibTableRow
connPvcEntry = _ConnPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1)
)
connPvcEntry.setIndexNames(
    (0, "LS100-MIB", "connPvcIndex"),
    (0, "LS100-MIB", "connPvcHighIfIndex"),
)
if mibBuilder.loadTexts:
    connPvcEntry.setStatus("mandatory")


class _ConnPvcIndex_Type(Integer32):
    """Custom type connPvcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ConnPvcIndex_Type.__name__ = "Integer32"
_ConnPvcIndex_Object = MibTableColumn
connPvcIndex = _ConnPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 1),
    _ConnPvcIndex_Type()
)
connPvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcIndex.setStatus("mandatory")


class _ConnPvcTopology_Type(Integer32):
    """Custom type connPvcTopology based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("biDirectionalVCC", 2),
          ("biDirectionalVPC", 4),
          ("broadcastVCC", 6),
          ("broadcastVPC", 5),
          ("gateway", 7),
          ("uniDirectionalVCC", 1),
          ("uniDirectionalVPC", 3),
          ("vpterm", 8))
    )


_ConnPvcTopology_Type.__name__ = "Integer32"
_ConnPvcTopology_Object = MibTableColumn
connPvcTopology = _ConnPvcTopology_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 2),
    _ConnPvcTopology_Type()
)
connPvcTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcTopology.setStatus("mandatory")


class _ConnPvcTrafficType_Type(Integer32):
    """Custom type connPvcTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("trafficCBR", 1),
          ("trafficUBR", 4),
          ("trafficVBR", 2))
    )


_ConnPvcTrafficType_Type.__name__ = "Integer32"
_ConnPvcTrafficType_Object = MibTableColumn
connPvcTrafficType = _ConnPvcTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 3),
    _ConnPvcTrafficType_Type()
)
connPvcTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcTrafficType.setStatus("mandatory")


class _ConnPvcLowIfIndex_Type(Integer32):
    """Custom type connPvcLowIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ConnPvcLowIfIndex_Type.__name__ = "Integer32"
_ConnPvcLowIfIndex_Object = MibTableColumn
connPvcLowIfIndex = _ConnPvcLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 4),
    _ConnPvcLowIfIndex_Type()
)
connPvcLowIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcLowIfIndex.setStatus("mandatory")
_ConnPvcLowVPI_Type = Integer32
_ConnPvcLowVPI_Object = MibTableColumn
connPvcLowVPI = _ConnPvcLowVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 5),
    _ConnPvcLowVPI_Type()
)
connPvcLowVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcLowVPI.setStatus("mandatory")
_ConnPvcLowVCI_Type = Integer32
_ConnPvcLowVCI_Object = MibTableColumn
connPvcLowVCI = _ConnPvcLowVCI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 6),
    _ConnPvcLowVCI_Type()
)
connPvcLowVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcLowVCI.setStatus("mandatory")


class _ConnPvcLowUpcParam_Type(Integer32):
    """Custom type connPvcLowUpcParam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ConnPvcLowUpcParam_Type.__name__ = "Integer32"
_ConnPvcLowUpcParam_Object = MibTableColumn
connPvcLowUpcParam = _ConnPvcLowUpcParam_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 7),
    _ConnPvcLowUpcParam_Type()
)
connPvcLowUpcParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcLowUpcParam.setStatus("mandatory")


class _ConnPvcLowUpc_Type(Integer32):
    """Custom type connPvcLowUpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("pass", 1),
          ("tagging", 3))
    )


_ConnPvcLowUpc_Type.__name__ = "Integer32"
_ConnPvcLowUpc_Object = MibTableColumn
connPvcLowUpc = _ConnPvcLowUpc_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 8),
    _ConnPvcLowUpc_Type()
)
connPvcLowUpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcLowUpc.setStatus("mandatory")


class _ConnPvcLowThroughput_Type(Integer32):
    """Custom type connPvcLowThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 622),
    )


_ConnPvcLowThroughput_Type.__name__ = "Integer32"
_ConnPvcLowThroughput_Object = MibTableColumn
connPvcLowThroughput = _ConnPvcLowThroughput_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 9),
    _ConnPvcLowThroughput_Type()
)
connPvcLowThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcLowThroughput.setStatus("mandatory")


class _ConnPvcHighIfIndex_Type(Integer32):
    """Custom type connPvcHighIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_ConnPvcHighIfIndex_Type.__name__ = "Integer32"
_ConnPvcHighIfIndex_Object = MibTableColumn
connPvcHighIfIndex = _ConnPvcHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 10),
    _ConnPvcHighIfIndex_Type()
)
connPvcHighIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcHighIfIndex.setStatus("mandatory")
_ConnPvcHighVPI_Type = Integer32
_ConnPvcHighVPI_Object = MibTableColumn
connPvcHighVPI = _ConnPvcHighVPI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 11),
    _ConnPvcHighVPI_Type()
)
connPvcHighVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcHighVPI.setStatus("mandatory")
_ConnPvcHighVCI_Type = Integer32
_ConnPvcHighVCI_Object = MibTableColumn
connPvcHighVCI = _ConnPvcHighVCI_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 12),
    _ConnPvcHighVCI_Type()
)
connPvcHighVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcHighVCI.setStatus("mandatory")


class _ConnPvcHighUpcParam_Type(Integer32):
    """Custom type connPvcHighUpcParam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ConnPvcHighUpcParam_Type.__name__ = "Integer32"
_ConnPvcHighUpcParam_Object = MibTableColumn
connPvcHighUpcParam = _ConnPvcHighUpcParam_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 13),
    _ConnPvcHighUpcParam_Type()
)
connPvcHighUpcParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcHighUpcParam.setStatus("mandatory")


class _ConnPvcHighUpc_Type(Integer32):
    """Custom type connPvcHighUpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("pass", 1),
          ("tagging", 3))
    )


_ConnPvcHighUpc_Type.__name__ = "Integer32"
_ConnPvcHighUpc_Object = MibTableColumn
connPvcHighUpc = _ConnPvcHighUpc_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 14),
    _ConnPvcHighUpc_Type()
)
connPvcHighUpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcHighUpc.setStatus("mandatory")


class _ConnPvcHighThroughput_Type(Integer32):
    """Custom type connPvcHighThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 622),
    )


_ConnPvcHighThroughput_Type.__name__ = "Integer32"
_ConnPvcHighThroughput_Object = MibTableColumn
connPvcHighThroughput = _ConnPvcHighThroughput_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 15),
    _ConnPvcHighThroughput_Type()
)
connPvcHighThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcHighThroughput.setStatus("mandatory")
_ConnPvcLowInCells_Type = Counter32
_ConnPvcLowInCells_Object = MibTableColumn
connPvcLowInCells = _ConnPvcLowInCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 16),
    _ConnPvcLowInCells_Type()
)
connPvcLowInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcLowInCells.setStatus("mandatory")
_ConnPvcHighOutCells_Type = Counter32
_ConnPvcHighOutCells_Object = MibTableColumn
connPvcHighOutCells = _ConnPvcHighOutCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 17),
    _ConnPvcHighOutCells_Type()
)
connPvcHighOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcHighOutCells.setStatus("mandatory")
_ConnPvcHighInCells_Type = Counter32
_ConnPvcHighInCells_Object = MibTableColumn
connPvcHighInCells = _ConnPvcHighInCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 18),
    _ConnPvcHighInCells_Type()
)
connPvcHighInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcHighInCells.setStatus("mandatory")
_ConnPvcLowOutCells_Type = Counter32
_ConnPvcLowOutCells_Object = MibTableColumn
connPvcLowOutCells = _ConnPvcLowOutCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 19),
    _ConnPvcLowOutCells_Type()
)
connPvcLowOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcLowOutCells.setStatus("mandatory")
_ConnPvcLowUpcViolatedCells_Type = Counter32
_ConnPvcLowUpcViolatedCells_Object = MibTableColumn
connPvcLowUpcViolatedCells = _ConnPvcLowUpcViolatedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 20),
    _ConnPvcLowUpcViolatedCells_Type()
)
connPvcLowUpcViolatedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcLowUpcViolatedCells.setStatus("mandatory")
_ConnPvcHighUpcViolatedCells_Type = Counter32
_ConnPvcHighUpcViolatedCells_Object = MibTableColumn
connPvcHighUpcViolatedCells = _ConnPvcHighUpcViolatedCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 21),
    _ConnPvcHighUpcViolatedCells_Type()
)
connPvcHighUpcViolatedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcHighUpcViolatedCells.setStatus("mandatory")


class _ConnPvcRowStatus_Type(Integer32):
    """Custom type connPvcRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_ConnPvcRowStatus_Type.__name__ = "Integer32"
_ConnPvcRowStatus_Object = MibTableColumn
connPvcRowStatus = _ConnPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 22),
    _ConnPvcRowStatus_Type()
)
connPvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connPvcRowStatus.setStatus("mandatory")


class _ConnPvcCause_Type(Integer32):
    """Custom type connPvcCause based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("broadcastTableFull", 6),
          ("existing", 1),
          ("inconsistentVPVC", 7),
          ("lineDiagnosis", 8),
          ("rateOverFlow", 4),
          ("upvpOutOfRange", 5),
          ("vpivciBusy", 2),
          ("vpivciOutOfRange", 3))
    )


_ConnPvcCause_Type.__name__ = "Integer32"
_ConnPvcCause_Object = MibTableColumn
connPvcCause = _ConnPvcCause_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 23),
    _ConnPvcCause_Type()
)
connPvcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcCause.setStatus("mandatory")


class _ConnPvcKind_Type(Integer32):
    """Custom type connPvcKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_ConnPvcKind_Type.__name__ = "Integer32"
_ConnPvcKind_Object = MibTableColumn
connPvcKind = _ConnPvcKind_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3, 3, 1, 24),
    _ConnPvcKind_Type()
)
connPvcKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPvcKind.setStatus("mandatory")
_Perf_ObjectIdentity = ObjectIdentity
perf = _Perf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4)
)


class _PerfTrapEnable_Type(Integer32):
    """Custom type perfTrapEnable based on Integer32"""
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


_PerfTrapEnable_Type.__name__ = "Integer32"
_PerfTrapEnable_Object = MibScalar
perfTrapEnable = _PerfTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 1),
    _PerfTrapEnable_Type()
)
perfTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfTrapEnable.setStatus("mandatory")
_PerfIfTable_Object = MibTable
perfIfTable = _PerfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2)
)
if mibBuilder.loadTexts:
    perfIfTable.setStatus("mandatory")
_PerfIfEntry_Object = MibTableRow
perfIfEntry = _PerfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1)
)
perfIfEntry.setIndexNames(
    (0, "LS100-MIB", "perfIfIndex"),
)
if mibBuilder.loadTexts:
    perfIfEntry.setStatus("mandatory")
_PerfIfIndex_Type = Integer32
_PerfIfIndex_Object = MibTableColumn
perfIfIndex = _PerfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 1),
    _PerfIfIndex_Type()
)
perfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfIndex.setStatus("mandatory")
_PerfIfLcvs_Type = Counter32
_PerfIfLcvs_Object = MibTableColumn
perfIfLcvs = _PerfIfLcvs_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 2),
    _PerfIfLcvs_Type()
)
perfIfLcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfLcvs.setStatus("mandatory")
_PerfIfParitySections_Type = Counter32
_PerfIfParitySections_Object = MibTableColumn
perfIfParitySections = _PerfIfParitySections_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 3),
    _PerfIfParitySections_Type()
)
perfIfParitySections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfParitySections.setStatus("mandatory")
_PerfIfParityLines_Type = Counter32
_PerfIfParityLines_Object = MibTableColumn
perfIfParityLines = _PerfIfParityLines_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 4),
    _PerfIfParityLines_Type()
)
perfIfParityLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfParityLines.setStatus("mandatory")
_PerfIfParityPaths_Type = Counter32
_PerfIfParityPaths_Object = MibTableColumn
perfIfParityPaths = _PerfIfParityPaths_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 5),
    _PerfIfParityPaths_Type()
)
perfIfParityPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfParityPaths.setStatus("mandatory")
_PerfIfHecErrors_Type = Counter32
_PerfIfHecErrors_Object = MibTableColumn
perfIfHecErrors = _PerfIfHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 6),
    _PerfIfHecErrors_Type()
)
perfIfHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfHecErrors.setStatus("mandatory")
_PerfIfMisDelivdCells_Type = Counter32
_PerfIfMisDelivdCells_Object = MibTableColumn
perfIfMisDelivdCells = _PerfIfMisDelivdCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 7),
    _PerfIfMisDelivdCells_Type()
)
perfIfMisDelivdCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfMisDelivdCells.setStatus("mandatory")
_PerfIfOverFlowCells_Type = Counter32
_PerfIfOverFlowCells_Object = MibTableColumn
perfIfOverFlowCells = _PerfIfOverFlowCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 8),
    _PerfIfOverFlowCells_Type()
)
perfIfOverFlowCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfOverFlowCells.setStatus("mandatory")
_PerfIfInCBRCells_Type = Counter32
_PerfIfInCBRCells_Object = MibTableColumn
perfIfInCBRCells = _PerfIfInCBRCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 9),
    _PerfIfInCBRCells_Type()
)
perfIfInCBRCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfInCBRCells.setStatus("mandatory")
_PerfIfOutCBRCells_Type = Counter32
_PerfIfOutCBRCells_Object = MibTableColumn
perfIfOutCBRCells = _PerfIfOutCBRCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 10),
    _PerfIfOutCBRCells_Type()
)
perfIfOutCBRCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfOutCBRCells.setStatus("mandatory")
_PerfIfInVBRCells_Type = Counter32
_PerfIfInVBRCells_Object = MibTableColumn
perfIfInVBRCells = _PerfIfInVBRCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 11),
    _PerfIfInVBRCells_Type()
)
perfIfInVBRCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfInVBRCells.setStatus("mandatory")
_PerfIfOutVBRCells_Type = Counter32
_PerfIfOutVBRCells_Object = MibTableColumn
perfIfOutVBRCells = _PerfIfOutVBRCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 12),
    _PerfIfOutVBRCells_Type()
)
perfIfOutVBRCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfOutVBRCells.setStatus("mandatory")
_PerfIfInUBRCells_Type = Counter32
_PerfIfInUBRCells_Object = MibTableColumn
perfIfInUBRCells = _PerfIfInUBRCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 15),
    _PerfIfInUBRCells_Type()
)
perfIfInUBRCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfInUBRCells.setStatus("mandatory")
_PerfIfOutUBRCells_Type = Counter32
_PerfIfOutUBRCells_Object = MibTableColumn
perfIfOutUBRCells = _PerfIfOutUBRCells_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4, 2, 1, 16),
    _PerfIfOutUBRCells_Type()
)
perfIfOutUBRCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perfIfOutUBRCells.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LS100-MIB",
    **{"DisplayString": DisplayString,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "atomis-mib": atomis_mib,
       "m5core-mib": m5core_mib,
       "node": node,
       "nodeOperStatus": nodeOperStatus,
       "nodeIfConfTable": nodeIfConfTable,
       "nodeIfConfEntry": nodeIfConfEntry,
       "nodeIfConfIndex": nodeIfConfIndex,
       "nodeIfConfPhysType": nodeIfConfPhysType,
       "nodeIfConfRev": nodeIfConfRev,
       "nodeIfConfStatus": nodeIfConfStatus,
       "nodeFanStatus": nodeFanStatus,
       "nodeUpcWindowSize": nodeUpcWindowSize,
       "nodeBestEffortBufferSize": nodeBestEffortBufferSize,
       "nodeGuaranteedBufferSize": nodeGuaranteedBufferSize,
       "nodeBestEffortBufferThreshold": nodeBestEffortBufferThreshold,
       "nodeGuaranteedBufferThreshold": nodeGuaranteedBufferThreshold,
       "nodeSaveConf": nodeSaveConf,
       "nodeSaveResult": nodeSaveResult,
       "nodeReset": nodeReset,
       "linf": linf,
       "linfStatusTable": linfStatusTable,
       "linfStatusEntry": linfStatusEntry,
       "linfIndex": linfIndex,
       "linfStatus": linfStatus,
       "linfConf": linfConf,
       "linfFwdAvailableBandWidth": linfFwdAvailableBandWidth,
       "linfBkwdAvailableBandWidth": linfBkwdAvailableBandWidth,
       "conn": conn,
       "connPvcIndexNext": connPvcIndexNext,
       "connPvcIndexEnable": connPvcIndexEnable,
       "connPvcTable": connPvcTable,
       "connPvcEntry": connPvcEntry,
       "connPvcIndex": connPvcIndex,
       "connPvcTopology": connPvcTopology,
       "connPvcTrafficType": connPvcTrafficType,
       "connPvcLowIfIndex": connPvcLowIfIndex,
       "connPvcLowVPI": connPvcLowVPI,
       "connPvcLowVCI": connPvcLowVCI,
       "connPvcLowUpcParam": connPvcLowUpcParam,
       "connPvcLowUpc": connPvcLowUpc,
       "connPvcLowThroughput": connPvcLowThroughput,
       "connPvcHighIfIndex": connPvcHighIfIndex,
       "connPvcHighVPI": connPvcHighVPI,
       "connPvcHighVCI": connPvcHighVCI,
       "connPvcHighUpcParam": connPvcHighUpcParam,
       "connPvcHighUpc": connPvcHighUpc,
       "connPvcHighThroughput": connPvcHighThroughput,
       "connPvcLowInCells": connPvcLowInCells,
       "connPvcHighOutCells": connPvcHighOutCells,
       "connPvcHighInCells": connPvcHighInCells,
       "connPvcLowOutCells": connPvcLowOutCells,
       "connPvcLowUpcViolatedCells": connPvcLowUpcViolatedCells,
       "connPvcHighUpcViolatedCells": connPvcHighUpcViolatedCells,
       "connPvcRowStatus": connPvcRowStatus,
       "connPvcCause": connPvcCause,
       "connPvcKind": connPvcKind,
       "perf": perf,
       "perfTrapEnable": perfTrapEnable,
       "perfIfTable": perfIfTable,
       "perfIfEntry": perfIfEntry,
       "perfIfIndex": perfIfIndex,
       "perfIfLcvs": perfIfLcvs,
       "perfIfParitySections": perfIfParitySections,
       "perfIfParityLines": perfIfParityLines,
       "perfIfParityPaths": perfIfParityPaths,
       "perfIfHecErrors": perfIfHecErrors,
       "perfIfMisDelivdCells": perfIfMisDelivdCells,
       "perfIfOverFlowCells": perfIfOverFlowCells,
       "perfIfInCBRCells": perfIfInCBRCells,
       "perfIfOutCBRCells": perfIfOutCBRCells,
       "perfIfInVBRCells": perfIfInVBRCells,
       "perfIfOutVBRCells": perfIfOutVBRCells,
       "perfIfInUBRCells": perfIfInUBRCells,
       "perfIfOutUBRCells": perfIfOutUBRCells}
)
