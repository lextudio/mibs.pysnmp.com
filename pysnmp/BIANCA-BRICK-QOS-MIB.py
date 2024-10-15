# SNMP MIB module (BIANCA-BRICK-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:43 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 27)
)
_QosIfTable_Object = MibTable
qosIfTable = _QosIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 1)
)
if mibBuilder.loadTexts:
    qosIfTable.setStatus("mandatory")
_QosIfEntry_Object = MibTableRow
qosIfEntry = _QosIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 1, 1)
)
qosIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-QOS-MIB", "qosIfIndex"),
)
if mibBuilder.loadTexts:
    qosIfEntry.setStatus("mandatory")
_QosIfIndex_Type = Integer32
_QosIfIndex_Object = MibTableColumn
qosIfIndex = _QosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 1, 1, 1),
    _QosIfIndex_Type()
)
qosIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosIfIndex.setStatus("mandatory")


class _QosIfType_Type(Integer32):
    """Custom type qosIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("delete", 9),
          ("disabled", 8),
          ("pq", 1),
          ("wfq", 3),
          ("wrr", 2))
    )


_QosIfType_Type.__name__ = "Integer32"
_QosIfType_Object = MibTableColumn
qosIfType = _QosIfType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 1, 1, 2),
    _QosIfType_Type()
)
qosIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosIfType.setStatus("mandatory")
_QosIfMaxTxRate_Type = Integer32
_QosIfMaxTxRate_Object = MibTableColumn
qosIfMaxTxRate = _QosIfMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 1, 1, 3),
    _QosIfMaxTxRate_Type()
)
qosIfMaxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosIfMaxTxRate.setStatus("mandatory")
_QosIfStatTable_Object = MibTable
qosIfStatTable = _QosIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 2)
)
if mibBuilder.loadTexts:
    qosIfStatTable.setStatus("mandatory")
_QosIfStatEntry_Object = MibTableRow
qosIfStatEntry = _QosIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 2, 1)
)
qosIfStatEntry.setIndexNames(
    (0, "BIANCA-BRICK-QOS-MIB", "qosIfStatIndex"),
)
if mibBuilder.loadTexts:
    qosIfStatEntry.setStatus("mandatory")
_QosIfStatIndex_Type = Integer32
_QosIfStatIndex_Object = MibTableColumn
qosIfStatIndex = _QosIfStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 2, 1, 1),
    _QosIfStatIndex_Type()
)
qosIfStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfStatIndex.setStatus("mandatory")
_QosIfStatOutPkts_Type = Counter32
_QosIfStatOutPkts_Object = MibTableColumn
qosIfStatOutPkts = _QosIfStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 2, 1, 2),
    _QosIfStatOutPkts_Type()
)
qosIfStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfStatOutPkts.setStatus("mandatory")
_QosIfStatOutOctets_Type = Counter32
_QosIfStatOutOctets_Object = MibTableColumn
qosIfStatOutOctets = _QosIfStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 2, 1, 3),
    _QosIfStatOutOctets_Type()
)
qosIfStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfStatOutOctets.setStatus("mandatory")
_QosIfStatPktsQueued_Type = Counter32
_QosIfStatPktsQueued_Object = MibTableColumn
qosIfStatPktsQueued = _QosIfStatPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 2, 1, 6),
    _QosIfStatPktsQueued_Type()
)
qosIfStatPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfStatPktsQueued.setStatus("mandatory")
_QosIfStatOctetsQueued_Type = Counter32
_QosIfStatOctetsQueued_Object = MibTableColumn
qosIfStatOctetsQueued = _QosIfStatOctetsQueued_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 2, 1, 7),
    _QosIfStatOctetsQueued_Type()
)
qosIfStatOctetsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfStatOctetsQueued.setStatus("mandatory")
_QosIfStatPktsDropped_Type = Counter32
_QosIfStatPktsDropped_Object = MibTableColumn
qosIfStatPktsDropped = _QosIfStatPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 2, 1, 8),
    _QosIfStatPktsDropped_Type()
)
qosIfStatPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfStatPktsDropped.setStatus("mandatory")
_QosIfStatOctetsDropped_Type = Counter32
_QosIfStatOctetsDropped_Object = MibTableColumn
qosIfStatOctetsDropped = _QosIfStatOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 2, 1, 9),
    _QosIfStatOctetsDropped_Type()
)
qosIfStatOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfStatOctetsDropped.setStatus("mandatory")
_QosPolicyTable_Object = MibTable
qosPolicyTable = _QosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3)
)
if mibBuilder.loadTexts:
    qosPolicyTable.setStatus("mandatory")
_QosPolicyEntry_Object = MibTableRow
qosPolicyEntry = _QosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1)
)
qosPolicyEntry.setIndexNames(
    (0, "BIANCA-BRICK-QOS-MIB", "qosPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    qosPolicyEntry.setStatus("mandatory")
_QosPolicyIfIndex_Type = Integer32
_QosPolicyIfIndex_Object = MibTableColumn
qosPolicyIfIndex = _QosPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 1),
    _QosPolicyIfIndex_Type()
)
qosPolicyIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyIfIndex.setStatus("mandatory")


class _QosPolicyType_Type(Integer32):
    """Custom type qosPolicyType based on Integer32"""
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
        *(("class-based", 1),
          ("default", 3),
          ("delete", 4),
          ("high-priority", 2))
    )


_QosPolicyType_Type.__name__ = "Integer32"
_QosPolicyType_Object = MibTableColumn
qosPolicyType = _QosPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 2),
    _QosPolicyType_Type()
)
qosPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyType.setStatus("mandatory")


class _QosPolicyClassId_Type(Integer32):
    """Custom type qosPolicyClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QosPolicyClassId_Type.__name__ = "Integer32"
_QosPolicyClassId_Object = MibTableColumn
qosPolicyClassId = _QosPolicyClassId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 3),
    _QosPolicyClassId_Type()
)
qosPolicyClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyClassId.setStatus("mandatory")


class _QosPolicyPriority_Type(Integer32):
    """Custom type qosPolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QosPolicyPriority_Type.__name__ = "Integer32"
_QosPolicyPriority_Object = MibTableColumn
qosPolicyPriority = _QosPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 4),
    _QosPolicyPriority_Type()
)
qosPolicyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyPriority.setStatus("mandatory")


class _QosPolicyWeight_Type(Integer32):
    """Custom type qosPolicyWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QosPolicyWeight_Type.__name__ = "Integer32"
_QosPolicyWeight_Object = MibTableColumn
qosPolicyWeight = _QosPolicyWeight_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 5),
    _QosPolicyWeight_Type()
)
qosPolicyWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyWeight.setStatus("mandatory")


class _QosPolicyShaper_Type(Integer32):
    """Custom type qosPolicyShaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("token-bucket", 2))
    )


_QosPolicyShaper_Type.__name__ = "Integer32"
_QosPolicyShaper_Object = MibTableColumn
qosPolicyShaper = _QosPolicyShaper_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 6),
    _QosPolicyShaper_Type()
)
qosPolicyShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyShaper.setStatus("mandatory")


class _QosPolicyCongestionAvoidance_Type(Integer32):
    """Custom type qosPolicyCongestionAvoidance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("weighted-random", 2))
    )


_QosPolicyCongestionAvoidance_Type.__name__ = "Integer32"
_QosPolicyCongestionAvoidance_Object = MibTableColumn
qosPolicyCongestionAvoidance = _QosPolicyCongestionAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 7),
    _QosPolicyCongestionAvoidance_Type()
)
qosPolicyCongestionAvoidance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyCongestionAvoidance.setStatus("mandatory")


class _QosPolicyDropAlgorithm_Type(Integer32):
    """Custom type qosPolicyDropAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("head-drop", 2),
          ("random-drop", 3),
          ("tail-drop", 1))
    )


_QosPolicyDropAlgorithm_Type.__name__ = "Integer32"
_QosPolicyDropAlgorithm_Object = MibTableColumn
qosPolicyDropAlgorithm = _QosPolicyDropAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 9),
    _QosPolicyDropAlgorithm_Type()
)
qosPolicyDropAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyDropAlgorithm.setStatus("mandatory")
_QosPolicyTxRate_Type = Integer32
_QosPolicyTxRate_Object = MibTableColumn
qosPolicyTxRate = _QosPolicyTxRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 17),
    _QosPolicyTxRate_Type()
)
qosPolicyTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyTxRate.setStatus("mandatory")


class _QosPolicyTxRateLimitation_Type(Integer32):
    """Custom type qosPolicyTxRateLimitation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bounded", 2),
          ("not-bounded", 1))
    )


_QosPolicyTxRateLimitation_Type.__name__ = "Integer32"
_QosPolicyTxRateLimitation_Object = MibTableColumn
qosPolicyTxRateLimitation = _QosPolicyTxRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 18),
    _QosPolicyTxRateLimitation_Type()
)
qosPolicyTxRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyTxRateLimitation.setStatus("mandatory")
_QosPolicyTxBurstSize_Type = Integer32
_QosPolicyTxBurstSize_Object = MibTableColumn
qosPolicyTxBurstSize = _QosPolicyTxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 19),
    _QosPolicyTxBurstSize_Type()
)
qosPolicyTxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyTxBurstSize.setStatus("mandatory")


class _QosPolicyLowerThreshold_Type(Integer32):
    """Custom type qosPolicyLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_QosPolicyLowerThreshold_Type.__name__ = "Integer32"
_QosPolicyLowerThreshold_Object = MibTableColumn
qosPolicyLowerThreshold = _QosPolicyLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 20),
    _QosPolicyLowerThreshold_Type()
)
qosPolicyLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyLowerThreshold.setStatus("mandatory")


class _QosPolicyUpperThreshold_Type(Integer32):
    """Custom type qosPolicyUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_QosPolicyUpperThreshold_Type.__name__ = "Integer32"
_QosPolicyUpperThreshold_Object = MibTableColumn
qosPolicyUpperThreshold = _QosPolicyUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 3, 1, 21),
    _QosPolicyUpperThreshold_Type()
)
qosPolicyUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicyUpperThreshold.setStatus("mandatory")
_QosPolicyStatTable_Object = MibTable
qosPolicyStatTable = _QosPolicyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4)
)
if mibBuilder.loadTexts:
    qosPolicyStatTable.setStatus("mandatory")
_QosPolicyStatEntry_Object = MibTableRow
qosPolicyStatEntry = _QosPolicyStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1)
)
qosPolicyStatEntry.setIndexNames(
    (0, "BIANCA-BRICK-QOS-MIB", "qosPolicyStatIfIndex"),
)
if mibBuilder.loadTexts:
    qosPolicyStatEntry.setStatus("mandatory")
_QosPolicyStatIfIndex_Type = Integer32
_QosPolicyStatIfIndex_Object = MibTableColumn
qosPolicyStatIfIndex = _QosPolicyStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1, 1),
    _QosPolicyStatIfIndex_Type()
)
qosPolicyStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyStatIfIndex.setStatus("mandatory")


class _QosPolicyStatType_Type(Integer32):
    """Custom type qosPolicyStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("class-based", 1),
          ("default", 3),
          ("high-priority", 2))
    )


_QosPolicyStatType_Type.__name__ = "Integer32"
_QosPolicyStatType_Object = MibTableColumn
qosPolicyStatType = _QosPolicyStatType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1, 2),
    _QosPolicyStatType_Type()
)
qosPolicyStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyStatType.setStatus("mandatory")
_QosPolicyStatClassId_Type = Integer32
_QosPolicyStatClassId_Object = MibTableColumn
qosPolicyStatClassId = _QosPolicyStatClassId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1, 3),
    _QosPolicyStatClassId_Type()
)
qosPolicyStatClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyStatClassId.setStatus("mandatory")
_QosPolicyStatOutPkts_Type = Counter32
_QosPolicyStatOutPkts_Object = MibTableColumn
qosPolicyStatOutPkts = _QosPolicyStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1, 4),
    _QosPolicyStatOutPkts_Type()
)
qosPolicyStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyStatOutPkts.setStatus("mandatory")
_QosPolicyStatOutOctets_Type = Counter32
_QosPolicyStatOutOctets_Object = MibTableColumn
qosPolicyStatOutOctets = _QosPolicyStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1, 5),
    _QosPolicyStatOutOctets_Type()
)
qosPolicyStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyStatOutOctets.setStatus("mandatory")
_QosPolicyStatPktsQueued_Type = Counter32
_QosPolicyStatPktsQueued_Object = MibTableColumn
qosPolicyStatPktsQueued = _QosPolicyStatPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1, 8),
    _QosPolicyStatPktsQueued_Type()
)
qosPolicyStatPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyStatPktsQueued.setStatus("mandatory")
_QosPolicyStatOctetsQueued_Type = Counter32
_QosPolicyStatOctetsQueued_Object = MibTableColumn
qosPolicyStatOctetsQueued = _QosPolicyStatOctetsQueued_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1, 9),
    _QosPolicyStatOctetsQueued_Type()
)
qosPolicyStatOctetsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyStatOctetsQueued.setStatus("mandatory")
_QosPolicyStatPktsDropped_Type = Counter32
_QosPolicyStatPktsDropped_Object = MibTableColumn
qosPolicyStatPktsDropped = _QosPolicyStatPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1, 10),
    _QosPolicyStatPktsDropped_Type()
)
qosPolicyStatPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyStatPktsDropped.setStatus("mandatory")
_QosPolicyStatOctetsDropped_Type = Counter32
_QosPolicyStatOctetsDropped_Object = MibTableColumn
qosPolicyStatOctetsDropped = _QosPolicyStatOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 27, 4, 1, 11),
    _QosPolicyStatOctetsDropped_Type()
)
qosPolicyStatOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyStatOctetsDropped.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-QOS-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "qos": qos,
       "qosIfTable": qosIfTable,
       "qosIfEntry": qosIfEntry,
       "qosIfIndex": qosIfIndex,
       "qosIfType": qosIfType,
       "qosIfMaxTxRate": qosIfMaxTxRate,
       "qosIfStatTable": qosIfStatTable,
       "qosIfStatEntry": qosIfStatEntry,
       "qosIfStatIndex": qosIfStatIndex,
       "qosIfStatOutPkts": qosIfStatOutPkts,
       "qosIfStatOutOctets": qosIfStatOutOctets,
       "qosIfStatPktsQueued": qosIfStatPktsQueued,
       "qosIfStatOctetsQueued": qosIfStatOctetsQueued,
       "qosIfStatPktsDropped": qosIfStatPktsDropped,
       "qosIfStatOctetsDropped": qosIfStatOctetsDropped,
       "qosPolicyTable": qosPolicyTable,
       "qosPolicyEntry": qosPolicyEntry,
       "qosPolicyIfIndex": qosPolicyIfIndex,
       "qosPolicyType": qosPolicyType,
       "qosPolicyClassId": qosPolicyClassId,
       "qosPolicyPriority": qosPolicyPriority,
       "qosPolicyWeight": qosPolicyWeight,
       "qosPolicyShaper": qosPolicyShaper,
       "qosPolicyCongestionAvoidance": qosPolicyCongestionAvoidance,
       "qosPolicyDropAlgorithm": qosPolicyDropAlgorithm,
       "qosPolicyTxRate": qosPolicyTxRate,
       "qosPolicyTxRateLimitation": qosPolicyTxRateLimitation,
       "qosPolicyTxBurstSize": qosPolicyTxBurstSize,
       "qosPolicyLowerThreshold": qosPolicyLowerThreshold,
       "qosPolicyUpperThreshold": qosPolicyUpperThreshold,
       "qosPolicyStatTable": qosPolicyStatTable,
       "qosPolicyStatEntry": qosPolicyStatEntry,
       "qosPolicyStatIfIndex": qosPolicyStatIfIndex,
       "qosPolicyStatType": qosPolicyStatType,
       "qosPolicyStatClassId": qosPolicyStatClassId,
       "qosPolicyStatOutPkts": qosPolicyStatOutPkts,
       "qosPolicyStatOutOctets": qosPolicyStatOutOctets,
       "qosPolicyStatPktsQueued": qosPolicyStatPktsQueued,
       "qosPolicyStatOctetsQueued": qosPolicyStatOctetsQueued,
       "qosPolicyStatPktsDropped": qosPolicyStatPktsDropped,
       "qosPolicyStatOctetsDropped": qosPolicyStatOctetsDropped}
)
