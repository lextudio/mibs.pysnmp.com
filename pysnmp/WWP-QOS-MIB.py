# SNMP MIB module (WWP-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:21 2024
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
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12)
)
wwpQosMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpQosMIBObjects_ObjectIdentity = ObjectIdentity
wwpQosMIBObjects = _WwpQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1)
)
_WwpQos_ObjectIdentity = ObjectIdentity
wwpQos = _WwpQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1)
)
_WwpQosTable_Object = MibTable
wwpQosTable = _WwpQosTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpQosTable.setStatus("current")
_WwpQosEntry_Object = MibTableRow
wwpQosEntry = _WwpQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1)
)
wwpQosEntry.setIndexNames(
    (0, "WWP-QOS-MIB", "wwpQosVlanId"),
    (0, "WWP-QOS-MIB", "wwpQosPortId"),
)
if mibBuilder.loadTexts:
    wwpQosEntry.setStatus("current")
_WwpQosVlanId_Type = VlanId
_WwpQosVlanId_Object = MibTableColumn
wwpQosVlanId = _WwpQosVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 1),
    _WwpQosVlanId_Type()
)
wwpQosVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosVlanId.setStatus("current")


class _WwpQosPortId_Type(Integer32):
    """Custom type wwpQosPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQosPortId_Type.__name__ = "Integer32"
_WwpQosPortId_Object = MibTableColumn
wwpQosPortId = _WwpQosPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 2),
    _WwpQosPortId_Type()
)
wwpQosPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosPortId.setStatus("current")


class _WwpQosRateLimit_Type(Integer32):
    """Custom type wwpQosRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_WwpQosRateLimit_Type.__name__ = "Integer32"
_WwpQosRateLimit_Object = MibTableColumn
wwpQosRateLimit = _WwpQosRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 3),
    _WwpQosRateLimit_Type()
)
wwpQosRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    wwpQosRateLimit.setUnits("kbps")


class _WwpQosPriQueue_Type(Integer32):
    """Custom type wwpQosPriQueue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpQosPriQueue_Type.__name__ = "Integer32"
_WwpQosPriQueue_Object = MibTableColumn
wwpQosPriQueue = _WwpQosPriQueue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 4),
    _WwpQosPriQueue_Type()
)
wwpQosPriQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosPriQueue.setStatus("current")
_WwpQosRowStatus_Type = RowStatus
_WwpQosRowStatus_Object = MibTableColumn
wwpQosRowStatus = _WwpQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 1, 1, 5),
    _WwpQosRowStatus_Type()
)
wwpQosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpQosRowStatus.setStatus("current")
_WwpQosStatsTable_Object = MibTable
wwpQosStatsTable = _WwpQosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpQosStatsTable.setStatus("current")
_WwpQosStatsEntry_Object = MibTableRow
wwpQosStatsEntry = _WwpQosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1)
)
wwpQosStatsEntry.setIndexNames(
    (0, "WWP-QOS-MIB", "wwpQosStatsVlanId"),
    (0, "WWP-QOS-MIB", "wwpQosStatsPortId"),
)
if mibBuilder.loadTexts:
    wwpQosStatsEntry.setStatus("current")
_WwpQosStatsVlanId_Type = VlanId
_WwpQosStatsVlanId_Object = MibTableColumn
wwpQosStatsVlanId = _WwpQosStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 1),
    _WwpQosStatsVlanId_Type()
)
wwpQosStatsVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosStatsVlanId.setStatus("current")


class _WwpQosStatsPortId_Type(Integer32):
    """Custom type wwpQosStatsPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQosStatsPortId_Type.__name__ = "Integer32"
_WwpQosStatsPortId_Object = MibTableColumn
wwpQosStatsPortId = _WwpQosStatsPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 2),
    _WwpQosStatsPortId_Type()
)
wwpQosStatsPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosStatsPortId.setStatus("current")
_WwpQosRxBytes_Type = Counter64
_WwpQosRxBytes_Object = MibTableColumn
wwpQosRxBytes = _WwpQosRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 3),
    _WwpQosRxBytes_Type()
)
wwpQosRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosRxBytes.setStatus("current")
_WwpQosRxPkts_Type = Counter64
_WwpQosRxPkts_Object = MibTableColumn
wwpQosRxPkts = _WwpQosRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 4),
    _WwpQosRxPkts_Type()
)
wwpQosRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosRxPkts.setStatus("current")


class _WwpQosResetCounters_Type(Integer32):
    """Custom type wwpQosResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_WwpQosResetCounters_Type.__name__ = "Integer32"
_WwpQosResetCounters_Object = MibTableColumn
wwpQosResetCounters = _WwpQosResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 2, 1, 5),
    _WwpQosResetCounters_Type()
)
wwpQosResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosResetCounters.setStatus("deprecated")
_WwpQosPriToQMapTable_Object = MibTable
wwpQosPriToQMapTable = _WwpQosPriToQMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpQosPriToQMapTable.setStatus("current")
_WwpQosPriToQMapEntry_Object = MibTableRow
wwpQosPriToQMapEntry = _WwpQosPriToQMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 3, 1)
)
wwpQosPriToQMapEntry.setIndexNames(
    (0, "WWP-QOS-MIB", "wwpQosRxPriority"),
)
if mibBuilder.loadTexts:
    wwpQosPriToQMapEntry.setStatus("current")


class _WwpQosRxPriority_Type(Integer32):
    """Custom type wwpQosRxPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpQosRxPriority_Type.__name__ = "Integer32"
_WwpQosRxPriority_Object = MibTableColumn
wwpQosRxPriority = _WwpQosRxPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 3, 1, 1),
    _WwpQosRxPriority_Type()
)
wwpQosRxPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosRxPriority.setStatus("current")


class _WwpQosTxPriQueue_Type(Integer32):
    """Custom type wwpQosTxPriQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpQosTxPriQueue_Type.__name__ = "Integer32"
_WwpQosTxPriQueue_Object = MibTableColumn
wwpQosTxPriQueue = _WwpQosTxPriQueue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 3, 1, 2),
    _WwpQosTxPriQueue_Type()
)
wwpQosTxPriQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosTxPriQueue.setStatus("current")
_WwpQosPortTable_Object = MibTable
wwpQosPortTable = _WwpQosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpQosPortTable.setStatus("current")
_WwpQosPortEntry_Object = MibTableRow
wwpQosPortEntry = _WwpQosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1)
)
wwpQosPortEntry.setIndexNames(
    (0, "WWP-QOS-MIB", "wwpQosPortIndex"),
)
if mibBuilder.loadTexts:
    wwpQosPortEntry.setStatus("current")


class _WwpQosPortIndex_Type(Integer32):
    """Custom type wwpQosPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQosPortIndex_Type.__name__ = "Integer32"
_WwpQosPortIndex_Object = MibTableColumn
wwpQosPortIndex = _WwpQosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1, 1),
    _WwpQosPortIndex_Type()
)
wwpQosPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosPortIndex.setStatus("current")


class _WwpQosPortPriQueue_Type(Integer32):
    """Custom type wwpQosPortPriQueue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3),
    )


_WwpQosPortPriQueue_Type.__name__ = "Integer32"
_WwpQosPortPriQueue_Object = MibTableColumn
wwpQosPortPriQueue = _WwpQosPortPriQueue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1, 2),
    _WwpQosPortPriQueue_Type()
)
wwpQosPortPriQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosPortPriQueue.setStatus("current")


class _WwpQosPortQAlgo_Type(Integer32):
    """Custom type wwpQosPortQAlgo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("weighted", 0))
    )


_WwpQosPortQAlgo_Type.__name__ = "Integer32"
_WwpQosPortQAlgo_Object = MibTableColumn
wwpQosPortQAlgo = _WwpQosPortQAlgo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1, 3),
    _WwpQosPortQAlgo_Type()
)
wwpQosPortQAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosPortQAlgo.setStatus("current")


class _WwpQosPortQApplyMode_Type(Integer32):
    """Custom type wwpQosPortQApplyMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qosMgmtForAllQueues", 2),
          ("qosMgmtPerQueue", 1))
    )


_WwpQosPortQApplyMode_Type.__name__ = "Integer32"
_WwpQosPortQApplyMode_Object = MibTableColumn
wwpQosPortQApplyMode = _WwpQosPortQApplyMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 4, 1, 4),
    _WwpQosPortQApplyMode_Type()
)
wwpQosPortQApplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosPortQApplyMode.setStatus("current")
_WwpQosPortQConfTable_Object = MibTable
wwpQosPortQConfTable = _WwpQosPortQConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpQosPortQConfTable.setStatus("current")
_WwpQosPortQConfEntry_Object = MibTableRow
wwpQosPortQConfEntry = _WwpQosPortQConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1)
)
wwpQosPortQConfEntry.setIndexNames(
    (0, "WWP-QOS-MIB", "wwpQosConfPortId"),
    (0, "WWP-QOS-MIB", "wwpQosConfQueueId"),
)
if mibBuilder.loadTexts:
    wwpQosPortQConfEntry.setStatus("current")


class _WwpQosConfPortId_Type(Integer32):
    """Custom type wwpQosConfPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQosConfPortId_Type.__name__ = "Integer32"
_WwpQosConfPortId_Object = MibTableColumn
wwpQosConfPortId = _WwpQosConfPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 1),
    _WwpQosConfPortId_Type()
)
wwpQosConfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosConfPortId.setStatus("current")


class _WwpQosConfQueueId_Type(Integer32):
    """Custom type wwpQosConfQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpQosConfQueueId_Type.__name__ = "Integer32"
_WwpQosConfQueueId_Object = MibTableColumn
wwpQosConfQueueId = _WwpQosConfQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 2),
    _WwpQosConfQueueId_Type()
)
wwpQosConfQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosConfQueueId.setStatus("current")


class _WwpQosPortQConfWeight_Type(Integer32):
    """Custom type wwpQosPortQConfWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WwpQosPortQConfWeight_Type.__name__ = "Integer32"
_WwpQosPortQConfWeight_Object = MibTableColumn
wwpQosPortQConfWeight = _WwpQosPortQConfWeight_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 3),
    _WwpQosPortQConfWeight_Type()
)
wwpQosPortQConfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosPortQConfWeight.setStatus("current")


class _WwpQosPortQConfDepth_Type(Integer32):
    """Custom type wwpQosPortQConfDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpQosPortQConfDepth_Type.__name__ = "Integer32"
_WwpQosPortQConfDepth_Object = MibTableColumn
wwpQosPortQConfDepth = _WwpQosPortQConfDepth_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 4),
    _WwpQosPortQConfDepth_Type()
)
wwpQosPortQConfDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosPortQConfDepth.setStatus("current")
_WwpQosPortQConfStatus_Type = RowStatus
_WwpQosPortQConfStatus_Object = MibTableColumn
wwpQosPortQConfStatus = _WwpQosPortQConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 5, 1, 5),
    _WwpQosPortQConfStatus_Type()
)
wwpQosPortQConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpQosPortQConfStatus.setStatus("current")
_WwpQosPortQStatusTable_Object = MibTable
wwpQosPortQStatusTable = _WwpQosPortQStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpQosPortQStatusTable.setStatus("current")
_WwpQosPortQStatusEntry_Object = MibTableRow
wwpQosPortQStatusEntry = _WwpQosPortQStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1)
)
wwpQosPortQStatusEntry.setIndexNames(
    (0, "WWP-QOS-MIB", "wwpQosQPortId"),
    (0, "WWP-QOS-MIB", "wwpQosQueueId"),
)
if mibBuilder.loadTexts:
    wwpQosPortQStatusEntry.setStatus("current")


class _WwpQosQPortId_Type(Integer32):
    """Custom type wwpQosQPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpQosQPortId_Type.__name__ = "Integer32"
_WwpQosQPortId_Object = MibTableColumn
wwpQosQPortId = _WwpQosQPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1, 1),
    _WwpQosQPortId_Type()
)
wwpQosQPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosQPortId.setStatus("current")


class _WwpQosQueueId_Type(Integer32):
    """Custom type wwpQosQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpQosQueueId_Type.__name__ = "Integer32"
_WwpQosQueueId_Object = MibTableColumn
wwpQosQueueId = _WwpQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1, 2),
    _WwpQosQueueId_Type()
)
wwpQosQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosQueueId.setStatus("current")


class _WwpQosPortQWeight_Type(Integer32):
    """Custom type wwpQosPortQWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WwpQosPortQWeight_Type.__name__ = "Integer32"
_WwpQosPortQWeight_Object = MibTableColumn
wwpQosPortQWeight = _WwpQosPortQWeight_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1, 3),
    _WwpQosPortQWeight_Type()
)
wwpQosPortQWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosPortQWeight.setStatus("current")


class _WwpQosPortQDepth_Type(Integer32):
    """Custom type wwpQosPortQDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpQosPortQDepth_Type.__name__ = "Integer32"
_WwpQosPortQDepth_Object = MibTableColumn
wwpQosPortQDepth = _WwpQosPortQDepth_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 6, 1, 4),
    _WwpQosPortQDepth_Type()
)
wwpQosPortQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpQosPortQDepth.setStatus("current")


class _WwpQosTxAssignmentMode_Type(Integer32):
    """Custom type wwpQosTxAssignmentMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useGreater", 1),
          ("useQos", 0))
    )


_WwpQosTxAssignmentMode_Type.__name__ = "Integer32"
_WwpQosTxAssignmentMode_Object = MibScalar
wwpQosTxAssignmentMode = _WwpQosTxAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 7),
    _WwpQosTxAssignmentMode_Type()
)
wwpQosTxAssignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosTxAssignmentMode.setStatus("current")


class _WwpQosPortTxAssignmentMode_Type(Integer32):
    """Custom type wwpQosPortTxAssignmentMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useGreater", 1),
          ("usePort", 0))
    )


_WwpQosPortTxAssignmentMode_Type.__name__ = "Integer32"
_WwpQosPortTxAssignmentMode_Object = MibScalar
wwpQosPortTxAssignmentMode = _WwpQosPortTxAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 1, 1, 8),
    _WwpQosPortTxAssignmentMode_Type()
)
wwpQosPortTxAssignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpQosPortTxAssignmentMode.setStatus("current")
_WwpQosNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpQosNotificationPrefix = _WwpQosNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 2)
)
_WwpQosNotifications_ObjectIdentity = ObjectIdentity
wwpQosNotifications = _WwpQosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 2, 0)
)
_WwpQosMIBConformance_ObjectIdentity = ObjectIdentity
wwpQosMIBConformance = _WwpQosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 3)
)
_WwpQosMIBCompliances_ObjectIdentity = ObjectIdentity
wwpQosMIBCompliances = _WwpQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 3, 1)
)
_WwpQosMIBGroups_ObjectIdentity = ObjectIdentity
wwpQosMIBGroups = _WwpQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 12, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-QOS-MIB",
    **{"VlanId": VlanId,
       "wwpQosMIB": wwpQosMIB,
       "wwpQosMIBObjects": wwpQosMIBObjects,
       "wwpQos": wwpQos,
       "wwpQosTable": wwpQosTable,
       "wwpQosEntry": wwpQosEntry,
       "wwpQosVlanId": wwpQosVlanId,
       "wwpQosPortId": wwpQosPortId,
       "wwpQosRateLimit": wwpQosRateLimit,
       "wwpQosPriQueue": wwpQosPriQueue,
       "wwpQosRowStatus": wwpQosRowStatus,
       "wwpQosStatsTable": wwpQosStatsTable,
       "wwpQosStatsEntry": wwpQosStatsEntry,
       "wwpQosStatsVlanId": wwpQosStatsVlanId,
       "wwpQosStatsPortId": wwpQosStatsPortId,
       "wwpQosRxBytes": wwpQosRxBytes,
       "wwpQosRxPkts": wwpQosRxPkts,
       "wwpQosResetCounters": wwpQosResetCounters,
       "wwpQosPriToQMapTable": wwpQosPriToQMapTable,
       "wwpQosPriToQMapEntry": wwpQosPriToQMapEntry,
       "wwpQosRxPriority": wwpQosRxPriority,
       "wwpQosTxPriQueue": wwpQosTxPriQueue,
       "wwpQosPortTable": wwpQosPortTable,
       "wwpQosPortEntry": wwpQosPortEntry,
       "wwpQosPortIndex": wwpQosPortIndex,
       "wwpQosPortPriQueue": wwpQosPortPriQueue,
       "wwpQosPortQAlgo": wwpQosPortQAlgo,
       "wwpQosPortQApplyMode": wwpQosPortQApplyMode,
       "wwpQosPortQConfTable": wwpQosPortQConfTable,
       "wwpQosPortQConfEntry": wwpQosPortQConfEntry,
       "wwpQosConfPortId": wwpQosConfPortId,
       "wwpQosConfQueueId": wwpQosConfQueueId,
       "wwpQosPortQConfWeight": wwpQosPortQConfWeight,
       "wwpQosPortQConfDepth": wwpQosPortQConfDepth,
       "wwpQosPortQConfStatus": wwpQosPortQConfStatus,
       "wwpQosPortQStatusTable": wwpQosPortQStatusTable,
       "wwpQosPortQStatusEntry": wwpQosPortQStatusEntry,
       "wwpQosQPortId": wwpQosQPortId,
       "wwpQosQueueId": wwpQosQueueId,
       "wwpQosPortQWeight": wwpQosPortQWeight,
       "wwpQosPortQDepth": wwpQosPortQDepth,
       "wwpQosTxAssignmentMode": wwpQosTxAssignmentMode,
       "wwpQosPortTxAssignmentMode": wwpQosPortTxAssignmentMode,
       "wwpQosNotificationPrefix": wwpQosNotificationPrefix,
       "wwpQosNotifications": wwpQosNotifications,
       "wwpQosMIBConformance": wwpQosMIBConformance,
       "wwpQosMIBCompliances": wwpQosMIBCompliances,
       "wwpQosMIBGroups": wwpQosMIBGroups}
)
