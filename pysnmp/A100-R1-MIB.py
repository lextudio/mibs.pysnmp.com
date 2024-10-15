# SNMP MIB module (A100-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A100-R1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:09 2024
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
          ("off-line", 3),
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
    (0, "A100-R1-MIB", "nodeIfConfIndex"),
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("ds3-PLCP-SCRAMBLE", 6),
          ("ds3-PLCP-noScramble", 7),
          ("notInstalled", 99),
          ("oc-3cMMF", 5),
          ("oc3cSMF", 4),
          ("other", 1),
          ("relay-6Mcel", 8),
          ("sar", 2),
          ("taxi100M", 3))
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
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_NodeSaveConf_Type.__name__ = "Integer32"
_NodeSaveConf_Object = MibScalar
nodeSaveConf = _NodeSaveConf_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 1, 9),
    _NodeSaveConf_Type()
)
nodeSaveConf.setMaxAccess("write-only")
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
          ("succeed", 4),
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
    (0, "A100-R1-MIB", "linfIndex"),
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("ais", 5),
          ("loc", 4),
          ("lof", 3),
          ("lop", 8),
          ("los", 2),
          ("normal", 1),
          ("notInstalled", 99),
          ("yellow-line", 6),
          ("yellow-path", 7))
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
          ("private-NNI", 3),
          ("private-UNI", 2),
          ("public-UNI", 1))
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
_Conn_ObjectIdentity = ObjectIdentity
conn = _Conn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 3)
)
_Perf_ObjectIdentity = ObjectIdentity
perf = _Perf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 14, 3, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A100-R1-MIB",
    **{"nec": nec,
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
       "linf": linf,
       "linfStatusTable": linfStatusTable,
       "linfStatusEntry": linfStatusEntry,
       "linfIndex": linfIndex,
       "linfStatus": linfStatus,
       "linfConf": linfConf,
       "conn": conn,
       "perf": perf}
)
