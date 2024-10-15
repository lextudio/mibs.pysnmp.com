# SNMP MIB module (ALCATEL-IND1-SLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-SLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:05 2024
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

(softentIND1Slb,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Slb")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1SLBMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1)
)
alcatelIND1SLBMIB.setRevisions(
        ("2010-05-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlbAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )



class SlbOperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 1))
    )



class SlbRedirectAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundRobin", 1),
          ("serverFailover", 2))
    )



class SlbHashSelector(Integer32, TextualConvention):
    status = "current"
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
        *(("dip", 2),
          ("dipL4dport", 8),
          ("dipSipL4dportL4sport", 6),
          ("sip", 3),
          ("sipAndDip", 4),
          ("sipDipL4sportL4dport", 5),
          ("sipL4sport", 7),
          ("useEcmp", 1))
    )



class SlbServerOperState(Integer32, TextualConvention):
    status = "current"
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
        *(("disabled", 4),
          ("discovery", 6),
          ("inService", 1),
          ("linkDown", 2),
          ("noAnswer", 3),
          ("retrying", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1SLBMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1SLBMIBNotifications = _AlcatelIND1SLBMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1SLBMIBNotifications.setStatus("current")
_AlcatelIND1SLBMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1SLBMIBObjects = _AlcatelIND1SLBMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SLBMIBObjects.setStatus("current")
_SlbFeature_ObjectIdentity = ObjectIdentity
slbFeature = _SlbFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 1)
)


class _SlbAdminStatus_Type(SlbAdminState):
    """Custom type slbAdminStatus based on SlbAdminState"""


_SlbAdminStatus_Object = MibScalar
slbAdminStatus = _SlbAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 1, 1),
    _SlbAdminStatus_Type()
)
slbAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbAdminStatus.setStatus("current")
_SlbOperStatus_Type = SlbOperState
_SlbOperStatus_Object = MibScalar
slbOperStatus = _SlbOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 1, 2),
    _SlbOperStatus_Type()
)
slbOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbOperStatus.setStatus("current")
_SlbClustersCount_Type = Unsigned32
_SlbClustersCount_Object = MibScalar
slbClustersCount = _SlbClustersCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 1, 3),
    _SlbClustersCount_Type()
)
slbClustersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbClustersCount.setStatus("current")


class _SlbResetStatistics_Type(Integer32):
    """Custom type slbResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSignificant", 0),
          ("resetSlbStats", 1))
    )


_SlbResetStatistics_Type.__name__ = "Integer32"
_SlbResetStatistics_Object = MibScalar
slbResetStatistics = _SlbResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 1, 4),
    _SlbResetStatistics_Type()
)
slbResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbResetStatistics.setStatus("current")
_SlbClusters_ObjectIdentity = ObjectIdentity
slbClusters = _SlbClusters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2)
)
_SlbClusterTable_Object = MibTable
slbClusterTable = _SlbClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slbClusterTable.setStatus("current")
_SlbClusterTableEntry_Object = MibTableRow
slbClusterTableEntry = _SlbClusterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1)
)
slbClusterTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-SLB-MIB", "slbClusterName"),
)
if mibBuilder.loadTexts:
    slbClusterTableEntry.setStatus("current")


class _SlbClusterName_Type(SnmpAdminString):
    """Custom type slbClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SlbClusterName_Type.__name__ = "SnmpAdminString"
_SlbClusterName_Object = MibTableColumn
slbClusterName = _SlbClusterName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 1),
    _SlbClusterName_Type()
)
slbClusterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbClusterName.setStatus("current")


class _SlbClusterAdminStatus_Type(SlbAdminState):
    """Custom type slbClusterAdminStatus based on SlbAdminState"""


_SlbClusterAdminStatus_Object = MibTableColumn
slbClusterAdminStatus = _SlbClusterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 2),
    _SlbClusterAdminStatus_Type()
)
slbClusterAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterAdminStatus.setStatus("current")
_SlbClusterOperStatus_Type = SlbOperState
_SlbClusterOperStatus_Object = MibTableColumn
slbClusterOperStatus = _SlbClusterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 3),
    _SlbClusterOperStatus_Type()
)
slbClusterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbClusterOperStatus.setStatus("current")
_SlbClusterVIP_Type = IpAddress
_SlbClusterVIP_Object = MibTableColumn
slbClusterVIP = _SlbClusterVIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 4),
    _SlbClusterVIP_Type()
)
slbClusterVIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterVIP.setStatus("current")


class _SlbClusterPingPeriod_Type(Unsigned32):
    """Custom type slbClusterPingPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SlbClusterPingPeriod_Type.__name__ = "Unsigned32"
_SlbClusterPingPeriod_Object = MibTableColumn
slbClusterPingPeriod = _SlbClusterPingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 5),
    _SlbClusterPingPeriod_Type()
)
slbClusterPingPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterPingPeriod.setStatus("current")
if mibBuilder.loadTexts:
    slbClusterPingPeriod.setUnits("seconds")


class _SlbClusterPingTimeout_Type(Unsigned32):
    """Custom type slbClusterPingTimeout based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_SlbClusterPingTimeout_Type.__name__ = "Unsigned32"
_SlbClusterPingTimeout_Object = MibTableColumn
slbClusterPingTimeout = _SlbClusterPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 6),
    _SlbClusterPingTimeout_Type()
)
slbClusterPingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slbClusterPingTimeout.setUnits("milliseconds")


class _SlbClusterPingRetries_Type(Unsigned32):
    """Custom type slbClusterPingRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbClusterPingRetries_Type.__name__ = "Unsigned32"
_SlbClusterPingRetries_Object = MibTableColumn
slbClusterPingRetries = _SlbClusterPingRetries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 7),
    _SlbClusterPingRetries_Type()
)
slbClusterPingRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterPingRetries.setStatus("current")


class _SlbClusterRedirectAlgorithm_Type(SlbRedirectAlgorithm):
    """Custom type slbClusterRedirectAlgorithm based on SlbRedirectAlgorithm"""


_SlbClusterRedirectAlgorithm_Object = MibTableColumn
slbClusterRedirectAlgorithm = _SlbClusterRedirectAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 8),
    _SlbClusterRedirectAlgorithm_Type()
)
slbClusterRedirectAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterRedirectAlgorithm.setStatus("current")


class _SlbClusterIdleTimer_Type(Unsigned32):
    """Custom type slbClusterIdleTimer based on Unsigned32"""
    defaultValue = 1200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SlbClusterIdleTimer_Type.__name__ = "Unsigned32"
_SlbClusterIdleTimer_Object = MibTableColumn
slbClusterIdleTimer = _SlbClusterIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 9),
    _SlbClusterIdleTimer_Type()
)
slbClusterIdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterIdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    slbClusterIdleTimer.setUnits("seconds")


class _SlbClusterNumberOfServers_Type(Unsigned32):
    """Custom type slbClusterNumberOfServers based on Unsigned32"""
    defaultValue = 0


_SlbClusterNumberOfServers_Object = MibTableColumn
slbClusterNumberOfServers = _SlbClusterNumberOfServers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 10),
    _SlbClusterNumberOfServers_Type()
)
slbClusterNumberOfServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbClusterNumberOfServers.setStatus("current")
_SlbClusterNewFlows_Type = Counter32
_SlbClusterNewFlows_Object = MibTableColumn
slbClusterNewFlows = _SlbClusterNewFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 11),
    _SlbClusterNewFlows_Type()
)
slbClusterNewFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbClusterNewFlows.setStatus("current")
_SlbClusterRowStatus_Type = RowStatus
_SlbClusterRowStatus_Object = MibTableColumn
slbClusterRowStatus = _SlbClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 12),
    _SlbClusterRowStatus_Type()
)
slbClusterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterRowStatus.setStatus("current")


class _SlbClusterProbeName_Type(SnmpAdminString):
    """Custom type slbClusterProbeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SlbClusterProbeName_Type.__name__ = "SnmpAdminString"
_SlbClusterProbeName_Object = MibTableColumn
slbClusterProbeName = _SlbClusterProbeName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 13),
    _SlbClusterProbeName_Type()
)
slbClusterProbeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterProbeName.setStatus("current")
_SlbClusterPackets_Type = Counter64
_SlbClusterPackets_Object = MibTableColumn
slbClusterPackets = _SlbClusterPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 14),
    _SlbClusterPackets_Type()
)
slbClusterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbClusterPackets.setStatus("current")


class _SlbClusterCondition_Type(SnmpAdminString):
    """Custom type slbClusterCondition based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SlbClusterCondition_Type.__name__ = "SnmpAdminString"
_SlbClusterCondition_Object = MibTableColumn
slbClusterCondition = _SlbClusterCondition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 15),
    _SlbClusterCondition_Type()
)
slbClusterCondition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterCondition.setStatus("current")


class _SlbClusterType_Type(Integer32):
    """Custom type slbClusterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2", 2),
          ("l3", 1))
    )


_SlbClusterType_Type.__name__ = "Integer32"
_SlbClusterType_Object = MibTableColumn
slbClusterType = _SlbClusterType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 16),
    _SlbClusterType_Type()
)
slbClusterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterType.setStatus("current")


class _SlbClusterHashType_Type(SlbHashSelector):
    """Custom type slbClusterHashType based on SlbHashSelector"""


_SlbClusterHashType_Object = MibTableColumn
slbClusterHashType = _SlbClusterHashType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 2, 1, 1, 17),
    _SlbClusterHashType_Type()
)
slbClusterHashType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbClusterHashType.setStatus("current")
_SlbServers_ObjectIdentity = ObjectIdentity
slbServers = _SlbServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3)
)
_SlbServerTable_Object = MibTable
slbServerTable = _SlbServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    slbServerTable.setStatus("current")
_SlbServerTableEntry_Object = MibTableRow
slbServerTableEntry = _SlbServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1)
)
slbServerTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-SLB-MIB", "slbServerClusterName"),
    (0, "ALCATEL-IND1-SLB-MIB", "slbServerIpAddress"),
)
if mibBuilder.loadTexts:
    slbServerTableEntry.setStatus("current")


class _SlbServerClusterName_Type(SnmpAdminString):
    """Custom type slbServerClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SlbServerClusterName_Type.__name__ = "SnmpAdminString"
_SlbServerClusterName_Object = MibTableColumn
slbServerClusterName = _SlbServerClusterName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 1),
    _SlbServerClusterName_Type()
)
slbServerClusterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbServerClusterName.setStatus("current")
_SlbServerIpAddress_Type = IpAddress
_SlbServerIpAddress_Object = MibTableColumn
slbServerIpAddress = _SlbServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 2),
    _SlbServerIpAddress_Type()
)
slbServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbServerIpAddress.setStatus("current")


class _SlbServerAdminStatus_Type(SlbAdminState):
    """Custom type slbServerAdminStatus based on SlbAdminState"""


_SlbServerAdminStatus_Object = MibTableColumn
slbServerAdminStatus = _SlbServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 3),
    _SlbServerAdminStatus_Type()
)
slbServerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbServerAdminStatus.setStatus("current")
_SlbServerOperStatus_Type = SlbServerOperState
_SlbServerOperStatus_Object = MibTableColumn
slbServerOperStatus = _SlbServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 4),
    _SlbServerOperStatus_Type()
)
slbServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbServerOperStatus.setStatus("current")


class _SlbServerAdminWeight_Type(Unsigned32):
    """Custom type slbServerAdminWeight based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SlbServerAdminWeight_Type.__name__ = "Unsigned32"
_SlbServerAdminWeight_Object = MibTableColumn
slbServerAdminWeight = _SlbServerAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 5),
    _SlbServerAdminWeight_Type()
)
slbServerAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbServerAdminWeight.setStatus("current")
_SlbServerUpTime_Type = Integer32
_SlbServerUpTime_Object = MibTableColumn
slbServerUpTime = _SlbServerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 6),
    _SlbServerUpTime_Type()
)
slbServerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbServerUpTime.setStatus("current")
_SlbServerLastRTT_Type = Integer32
_SlbServerLastRTT_Object = MibTableColumn
slbServerLastRTT = _SlbServerLastRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 7),
    _SlbServerLastRTT_Type()
)
slbServerLastRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbServerLastRTT.setStatus("current")
if mibBuilder.loadTexts:
    slbServerLastRTT.setUnits("milliseconds")
_SlbServerPingFails_Type = Counter32
_SlbServerPingFails_Object = MibTableColumn
slbServerPingFails = _SlbServerPingFails_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 8),
    _SlbServerPingFails_Type()
)
slbServerPingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbServerPingFails.setStatus("current")
_SlbServerPortDown_Type = Counter32
_SlbServerPortDown_Object = MibTableColumn
slbServerPortDown = _SlbServerPortDown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 9),
    _SlbServerPortDown_Type()
)
slbServerPortDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbServerPortDown.setStatus("current")
_SlbServerFlows_Type = Counter32
_SlbServerFlows_Object = MibTableColumn
slbServerFlows = _SlbServerFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 10),
    _SlbServerFlows_Type()
)
slbServerFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbServerFlows.setStatus("current")
_SlbServerRowStatus_Type = RowStatus
_SlbServerRowStatus_Object = MibTableColumn
slbServerRowStatus = _SlbServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 11),
    _SlbServerRowStatus_Type()
)
slbServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbServerRowStatus.setStatus("current")


class _SlbServerProbeName_Type(SnmpAdminString):
    """Custom type slbServerProbeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SlbServerProbeName_Type.__name__ = "SnmpAdminString"
_SlbServerProbeName_Object = MibTableColumn
slbServerProbeName = _SlbServerProbeName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 12),
    _SlbServerProbeName_Type()
)
slbServerProbeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbServerProbeName.setStatus("current")


class _SlbServerProbeStatus_Type(SnmpAdminString):
    """Custom type slbServerProbeStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbServerProbeStatus_Type.__name__ = "SnmpAdminString"
_SlbServerProbeStatus_Object = MibTableColumn
slbServerProbeStatus = _SlbServerProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 3, 1, 1, 13),
    _SlbServerProbeStatus_Type()
)
slbServerProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbServerProbeStatus.setStatus("current")
_SlbProbes_ObjectIdentity = ObjectIdentity
slbProbes = _SlbProbes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4)
)
_SlbProbeTable_Object = MibTable
slbProbeTable = _SlbProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    slbProbeTable.setStatus("current")
_SlbProbeTableEntry_Object = MibTableRow
slbProbeTableEntry = _SlbProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1)
)
slbProbeTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-SLB-MIB", "slbProbeName"),
)
if mibBuilder.loadTexts:
    slbProbeTableEntry.setStatus("current")


class _SlbProbeName_Type(SnmpAdminString):
    """Custom type slbProbeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SlbProbeName_Type.__name__ = "SnmpAdminString"
_SlbProbeName_Object = MibTableColumn
slbProbeName = _SlbProbeName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 1),
    _SlbProbeName_Type()
)
slbProbeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbProbeName.setStatus("current")


class _SlbProbeMethod_Type(Integer32):
    """Custom type slbProbeMethod based on Integer32"""
    defaultValue = 1

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 6),
          ("http", 2),
          ("https", 3),
          ("imap", 10),
          ("imaps", 11),
          ("nntp", 12),
          ("ping", 1),
          ("pop", 8),
          ("pops", 9),
          ("smtp", 7),
          ("tcp", 5),
          ("udp", 4))
    )


_SlbProbeMethod_Type.__name__ = "Integer32"
_SlbProbeMethod_Object = MibTableColumn
slbProbeMethod = _SlbProbeMethod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 2),
    _SlbProbeMethod_Type()
)
slbProbeMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeMethod.setStatus("current")


class _SlbProbePeriod_Type(Unsigned32):
    """Custom type slbProbePeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SlbProbePeriod_Type.__name__ = "Unsigned32"
_SlbProbePeriod_Object = MibTableColumn
slbProbePeriod = _SlbProbePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 3),
    _SlbProbePeriod_Type()
)
slbProbePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbePeriod.setStatus("current")
if mibBuilder.loadTexts:
    slbProbePeriod.setUnits("seconds")


class _SlbProbeTimeout_Type(Unsigned32):
    """Custom type slbProbeTimeout based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3600000),
    )


_SlbProbeTimeout_Type.__name__ = "Unsigned32"
_SlbProbeTimeout_Object = MibTableColumn
slbProbeTimeout = _SlbProbeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 4),
    _SlbProbeTimeout_Type()
)
slbProbeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slbProbeTimeout.setUnits("milliseconds")


class _SlbProbeRetries_Type(Unsigned32):
    """Custom type slbProbeRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbProbeRetries_Type.__name__ = "Unsigned32"
_SlbProbeRetries_Object = MibTableColumn
slbProbeRetries = _SlbProbeRetries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 5),
    _SlbProbeRetries_Type()
)
slbProbeRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeRetries.setStatus("current")


class _SlbProbePort_Type(Integer32):
    """Custom type slbProbePort based on Integer32"""
    defaultValue = 0


_SlbProbePort_Object = MibTableColumn
slbProbePort = _SlbProbePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 6),
    _SlbProbePort_Type()
)
slbProbePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbePort.setStatus("current")


class _SlbProbeExpect_Type(SnmpAdminString):
    """Custom type slbProbeExpect based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbProbeExpect_Type.__name__ = "SnmpAdminString"
_SlbProbeExpect_Object = MibTableColumn
slbProbeExpect = _SlbProbeExpect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 7),
    _SlbProbeExpect_Type()
)
slbProbeExpect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeExpect.setStatus("current")


class _SlbProbeSSL_Type(Integer32):
    """Custom type slbProbeSSL based on Integer32"""
    defaultValue = 2

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


_SlbProbeSSL_Type.__name__ = "Integer32"
_SlbProbeSSL_Object = MibTableColumn
slbProbeSSL = _SlbProbeSSL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 8),
    _SlbProbeSSL_Type()
)
slbProbeSSL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeSSL.setStatus("current")


class _SlbProbeSend_Type(SnmpAdminString):
    """Custom type slbProbeSend based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbProbeSend_Type.__name__ = "SnmpAdminString"
_SlbProbeSend_Object = MibTableColumn
slbProbeSend = _SlbProbeSend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 9),
    _SlbProbeSend_Type()
)
slbProbeSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeSend.setStatus("current")


class _SlbProbeHttpStatus_Type(Integer32):
    """Custom type slbProbeHttpStatus based on Integer32"""
    defaultValue = 200


_SlbProbeHttpStatus_Object = MibTableColumn
slbProbeHttpStatus = _SlbProbeHttpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 10),
    _SlbProbeHttpStatus_Type()
)
slbProbeHttpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeHttpStatus.setStatus("current")


class _SlbProbeHttpUrl_Type(SnmpAdminString):
    """Custom type slbProbeHttpUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SlbProbeHttpUrl_Type.__name__ = "SnmpAdminString"
_SlbProbeHttpUrl_Object = MibTableColumn
slbProbeHttpUrl = _SlbProbeHttpUrl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 11),
    _SlbProbeHttpUrl_Type()
)
slbProbeHttpUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeHttpUrl.setStatus("current")


class _SlbProbeHttpUsername_Type(SnmpAdminString):
    """Custom type slbProbeHttpUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbProbeHttpUsername_Type.__name__ = "SnmpAdminString"
_SlbProbeHttpUsername_Object = MibTableColumn
slbProbeHttpUsername = _SlbProbeHttpUsername_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 12),
    _SlbProbeHttpUsername_Type()
)
slbProbeHttpUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeHttpUsername.setStatus("current")


class _SlbProbeHttpPassword_Type(SnmpAdminString):
    """Custom type slbProbeHttpPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbProbeHttpPassword_Type.__name__ = "SnmpAdminString"
_SlbProbeHttpPassword_Object = MibTableColumn
slbProbeHttpPassword = _SlbProbeHttpPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 13),
    _SlbProbeHttpPassword_Type()
)
slbProbeHttpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeHttpPassword.setStatus("current")
_SlbProbeRowStatus_Type = RowStatus
_SlbProbeRowStatus_Object = MibTableColumn
slbProbeRowStatus = _SlbProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 4, 1, 1, 14),
    _SlbProbeRowStatus_Type()
)
slbProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbProbeRowStatus.setStatus("current")
_SlbStats_ObjectIdentity = ObjectIdentity
slbStats = _SlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5)
)
_SlbStatsTable_Object = MibTable
slbStatsTable = _SlbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    slbStatsTable.setStatus("current")
_SlbStatsTableEntry_Object = MibTableRow
slbStatsTableEntry = _SlbStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 1, 1)
)
slbStatsTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-SLB-MIB", "slbStatsClusterName"),
    (0, "ALCATEL-IND1-SLB-MIB", "slbStatsIndex"),
)
if mibBuilder.loadTexts:
    slbStatsTableEntry.setStatus("current")


class _SlbStatsClusterName_Type(SnmpAdminString):
    """Custom type slbStatsClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SlbStatsClusterName_Type.__name__ = "SnmpAdminString"
_SlbStatsClusterName_Object = MibTableColumn
slbStatsClusterName = _SlbStatsClusterName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 1, 1, 1),
    _SlbStatsClusterName_Type()
)
slbStatsClusterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbStatsClusterName.setStatus("current")


class _SlbStatsIndex_Type(Integer32):
    """Custom type slbStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_SlbStatsIndex_Type.__name__ = "Integer32"
_SlbStatsIndex_Object = MibTableColumn
slbStatsIndex = _SlbStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 1, 1, 2),
    _SlbStatsIndex_Type()
)
slbStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbStatsIndex.setStatus("current")
_SlbStatsCounter_Type = Counter64
_SlbStatsCounter_Object = MibTableColumn
slbStatsCounter = _SlbStatsCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 1, 1, 3),
    _SlbStatsCounter_Type()
)
slbStatsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsCounter.setStatus("current")
_SlbStatsQualTable_Object = MibTable
slbStatsQualTable = _SlbStatsQualTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    slbStatsQualTable.setStatus("current")
_SlbStatsQualTableEntry_Object = MibTableRow
slbStatsQualTableEntry = _SlbStatsQualTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1)
)
slbStatsQualTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-SLB-MIB", "slbStatsClusterName"),
    (0, "ALCATEL-IND1-SLB-MIB", "slbStatsIndex"),
    (0, "ALCATEL-IND1-SLB-MIB", "slbStatsQualType"),
)
if mibBuilder.loadTexts:
    slbStatsQualTableEntry.setStatus("current")


class _SlbStatsQualType_Type(Integer32):
    """Custom type slbStatsQualType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("d8021p", 15),
          ("dstIp", 1),
          ("dstIpPort", 7),
          ("dstIpTcpPort", 9),
          ("dstIpUdpPort", 11),
          ("dstMac", 14),
          ("dstPort", 21),
          ("dstPortGroup", 22),
          ("ethertype", 16),
          ("icmpCode", 18),
          ("icmpType", 17),
          ("ipProtocol", 6),
          ("srcIp", 2),
          ("srcIpPort", 8),
          ("srcIpTcpPort", 10),
          ("srcIpUdpPort", 12),
          ("srcMac", 13),
          ("srcPort", 3),
          ("srcPortGroup", 4),
          ("srcVlan", 5),
          ("tcpFlags", 19),
          ("tos", 20))
    )


_SlbStatsQualType_Type.__name__ = "Integer32"
_SlbStatsQualType_Object = MibTableColumn
slbStatsQualType = _SlbStatsQualType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 1),
    _SlbStatsQualType_Type()
)
slbStatsQualType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slbStatsQualType.setStatus("current")
_SlbStatsQualDataIp_Type = IpAddress
_SlbStatsQualDataIp_Object = MibTableColumn
slbStatsQualDataIp = _SlbStatsQualDataIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 2),
    _SlbStatsQualDataIp_Type()
)
slbStatsQualDataIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataIp.setStatus("current")
_SlbStatsQualDataIpMask_Type = IpAddress
_SlbStatsQualDataIpMask_Object = MibTableColumn
slbStatsQualDataIpMask = _SlbStatsQualDataIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 3),
    _SlbStatsQualDataIpMask_Type()
)
slbStatsQualDataIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataIpMask.setStatus("current")


class _SlbStatsQualDataSlot_Type(Integer32):
    """Custom type slbStatsQualDataSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbStatsQualDataSlot_Type.__name__ = "Integer32"
_SlbStatsQualDataSlot_Object = MibTableColumn
slbStatsQualDataSlot = _SlbStatsQualDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 4),
    _SlbStatsQualDataSlot_Type()
)
slbStatsQualDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataSlot.setStatus("current")


class _SlbStatsQualDataStartPort_Type(Integer32):
    """Custom type slbStatsQualDataStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbStatsQualDataStartPort_Type.__name__ = "Integer32"
_SlbStatsQualDataStartPort_Object = MibTableColumn
slbStatsQualDataStartPort = _SlbStatsQualDataStartPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 5),
    _SlbStatsQualDataStartPort_Type()
)
slbStatsQualDataStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataStartPort.setStatus("current")


class _SlbStatsQualDataEndPort_Type(Integer32):
    """Custom type slbStatsQualDataEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbStatsQualDataEndPort_Type.__name__ = "Integer32"
_SlbStatsQualDataEndPort_Object = MibTableColumn
slbStatsQualDataEndPort = _SlbStatsQualDataEndPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 6),
    _SlbStatsQualDataEndPort_Type()
)
slbStatsQualDataEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataEndPort.setStatus("current")


class _SlbStatsQualDataIpProtocol_Type(Integer32):
    """Custom type slbStatsQualDataIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbStatsQualDataIpProtocol_Type.__name__ = "Integer32"
_SlbStatsQualDataIpProtocol_Object = MibTableColumn
slbStatsQualDataIpProtocol = _SlbStatsQualDataIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 7),
    _SlbStatsQualDataIpProtocol_Type()
)
slbStatsQualDataIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataIpProtocol.setStatus("current")


class _SlbStatsQualDataVlan_Type(Integer32):
    """Custom type slbStatsQualDataVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SlbStatsQualDataVlan_Type.__name__ = "Integer32"
_SlbStatsQualDataVlan_Object = MibTableColumn
slbStatsQualDataVlan = _SlbStatsQualDataVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 8),
    _SlbStatsQualDataVlan_Type()
)
slbStatsQualDataVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataVlan.setStatus("current")


class _SlbStatsQualDataL4Port_Type(Integer32):
    """Custom type slbStatsQualDataL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbStatsQualDataL4Port_Type.__name__ = "Integer32"
_SlbStatsQualDataL4Port_Object = MibTableColumn
slbStatsQualDataL4Port = _SlbStatsQualDataL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 9),
    _SlbStatsQualDataL4Port_Type()
)
slbStatsQualDataL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataL4Port.setStatus("current")
_SlbStatsQualDataMac_Type = MacAddress
_SlbStatsQualDataMac_Object = MibTableColumn
slbStatsQualDataMac = _SlbStatsQualDataMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 10),
    _SlbStatsQualDataMac_Type()
)
slbStatsQualDataMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataMac.setStatus("current")
_SlbStatsQualDataMacMask_Type = MacAddress
_SlbStatsQualDataMacMask_Object = MibTableColumn
slbStatsQualDataMacMask = _SlbStatsQualDataMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 11),
    _SlbStatsQualDataMacMask_Type()
)
slbStatsQualDataMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataMacMask.setStatus("current")


class _SlbStatsQualDataEthertype_Type(Integer32):
    """Custom type slbStatsQualDataEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbStatsQualDataEthertype_Type.__name__ = "Integer32"
_SlbStatsQualDataEthertype_Object = MibTableColumn
slbStatsQualDataEthertype = _SlbStatsQualDataEthertype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 12),
    _SlbStatsQualDataEthertype_Type()
)
slbStatsQualDataEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataEthertype.setStatus("current")


class _SlbStatsQualDataIcmpData_Type(Integer32):
    """Custom type slbStatsQualDataIcmpData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbStatsQualDataIcmpData_Type.__name__ = "Integer32"
_SlbStatsQualDataIcmpData_Object = MibTableColumn
slbStatsQualDataIcmpData = _SlbStatsQualDataIcmpData_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 13),
    _SlbStatsQualDataIcmpData_Type()
)
slbStatsQualDataIcmpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataIcmpData.setStatus("current")


class _SlbStatsQualDataTcpFlags_Type(OctetString):
    """Custom type slbStatsQualDataTcpFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SlbStatsQualDataTcpFlags_Type.__name__ = "OctetString"
_SlbStatsQualDataTcpFlags_Object = MibTableColumn
slbStatsQualDataTcpFlags = _SlbStatsQualDataTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 14),
    _SlbStatsQualDataTcpFlags_Type()
)
slbStatsQualDataTcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataTcpFlags.setStatus("current")


class _SlbStatsQualDataTos_Type(OctetString):
    """Custom type slbStatsQualDataTos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SlbStatsQualDataTos_Type.__name__ = "OctetString"
_SlbStatsQualDataTos_Object = MibTableColumn
slbStatsQualDataTos = _SlbStatsQualDataTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 15),
    _SlbStatsQualDataTos_Type()
)
slbStatsQualDataTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualDataTos.setStatus("current")


class _SlbStatsQualData8021p_Type(Integer32):
    """Custom type slbStatsQualData8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbStatsQualData8021p_Type.__name__ = "Integer32"
_SlbStatsQualData8021p_Object = MibTableColumn
slbStatsQualData8021p = _SlbStatsQualData8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 5, 2, 1, 16),
    _SlbStatsQualData8021p_Type()
)
slbStatsQualData8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatsQualData8021p.setStatus("current")
_SlbStatsQual_ObjectIdentity = ObjectIdentity
slbStatsQual = _SlbStatsQual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 6)
)
_SlbTrapsObj_ObjectIdentity = ObjectIdentity
slbTrapsObj = _SlbTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 7)
)


class _SlbTrapInfoClusterName_Type(SnmpAdminString):
    """Custom type slbTrapInfoClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SlbTrapInfoClusterName_Type.__name__ = "SnmpAdminString"
_SlbTrapInfoClusterName_Object = MibScalar
slbTrapInfoClusterName = _SlbTrapInfoClusterName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 7, 1),
    _SlbTrapInfoClusterName_Type()
)
slbTrapInfoClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbTrapInfoClusterName.setStatus("current")
_SlbTrapInfoOperStatus_Type = SlbOperState
_SlbTrapInfoOperStatus_Object = MibScalar
slbTrapInfoOperStatus = _SlbTrapInfoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 7, 2),
    _SlbTrapInfoOperStatus_Type()
)
slbTrapInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbTrapInfoOperStatus.setStatus("current")
_SlbTrapInfoServerIpAddr_Type = IpAddress
_SlbTrapInfoServerIpAddr_Object = MibScalar
slbTrapInfoServerIpAddr = _SlbTrapInfoServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 7, 3),
    _SlbTrapInfoServerIpAddr_Type()
)
slbTrapInfoServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbTrapInfoServerIpAddr.setStatus("current")


class _SlbTrapInfoEntityGroup_Type(Integer32):
    """Custom type slbTrapInfoEntityGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cluster", 2),
          ("server", 3),
          ("slb", 1))
    )


_SlbTrapInfoEntityGroup_Type.__name__ = "Integer32"
_SlbTrapInfoEntityGroup_Object = MibScalar
slbTrapInfoEntityGroup = _SlbTrapInfoEntityGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 7, 4),
    _SlbTrapInfoEntityGroup_Type()
)
slbTrapInfoEntityGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbTrapInfoEntityGroup.setStatus("current")
_SlbTrapInfoException_Type = Integer32
_SlbTrapInfoException_Object = MibScalar
slbTrapInfoException = _SlbTrapInfoException_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 1, 7, 5),
    _SlbTrapInfoException_Type()
)
slbTrapInfoException.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbTrapInfoException.setStatus("current")
_AlcatelIND1SLBMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1SLBMIBConformance = _AlcatelIND1SLBMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SLBMIBConformance.setStatus("current")
_AlcatelIND1SLBMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1SLBMIBGroups = _AlcatelIND1SLBMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SLBMIBGroups.setStatus("current")
_AlcatelIND1SLBMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1SLBMIBCompliances = _AlcatelIND1SLBMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SLBMIBCompliances.setStatus("current")

# Managed Objects groups

slbFeatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 1, 1)
)
slbFeatureGroup.setObjects(
      *(("ALCATEL-IND1-SLB-MIB", "slbAdminStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbOperStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbClustersCount"),
        ("ALCATEL-IND1-SLB-MIB", "slbResetStatistics"))
)
if mibBuilder.loadTexts:
    slbFeatureGroup.setStatus("current")

slbClustersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 1, 2)
)
slbClustersGroup.setObjects(
      *(("ALCATEL-IND1-SLB-MIB", "slbClusterAdminStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterOperStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterVIP"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterPingPeriod"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterPingTimeout"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterPingRetries"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterRedirectAlgorithm"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterIdleTimer"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterNumberOfServers"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterNewFlows"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterRowStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterProbeName"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterPackets"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterCondition"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterType"),
        ("ALCATEL-IND1-SLB-MIB", "slbClusterHashType"))
)
if mibBuilder.loadTexts:
    slbClustersGroup.setStatus("current")

slbServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 1, 3)
)
slbServersGroup.setObjects(
      *(("ALCATEL-IND1-SLB-MIB", "slbServerAdminStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerOperStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerAdminWeight"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerUpTime"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerLastRTT"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerPingFails"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerFlows"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerRowStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerProbeName"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerProbeStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbServerPortDown"))
)
if mibBuilder.loadTexts:
    slbServersGroup.setStatus("current")

slbProbesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 1, 5)
)
slbProbesGroup.setObjects(
      *(("ALCATEL-IND1-SLB-MIB", "slbProbeMethod"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbePeriod"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeTimeout"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeRetries"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbePort"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeExpect"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeSend"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeSSL"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeHttpStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeHttpUrl"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeHttpUsername"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeHttpPassword"),
        ("ALCATEL-IND1-SLB-MIB", "slbProbeRowStatus"))
)
if mibBuilder.loadTexts:
    slbProbesGroup.setStatus("current")

slbStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 1, 6)
)
slbStatsGroup.setObjects(
      *(("ALCATEL-IND1-SLB-MIB", "slbStatsCounter"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataIp"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataIpMask"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataSlot"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataStartPort"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataEndPort"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataVlan"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataL4Port"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataMac"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataEthertype"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataIcmpData"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataTcpFlags"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataTos"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualData8021p"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataIpProtocol"),
        ("ALCATEL-IND1-SLB-MIB", "slbStatsQualDataMacMask"))
)
if mibBuilder.loadTexts:
    slbStatsGroup.setStatus("current")

slbTrapsObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 1, 7)
)
slbTrapsObjGroup.setObjects(
      *(("ALCATEL-IND1-SLB-MIB", "slbTrapInfoClusterName"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoEntityGroup"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoException"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoOperStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoServerIpAddr"))
)
if mibBuilder.loadTexts:
    slbTrapsObjGroup.setStatus("current")


# Notification objects

slbTrapException = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 0, 1)
)
slbTrapException.setObjects(
    ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoException")
)
if mibBuilder.loadTexts:
    slbTrapException.setStatus(
        "current"
    )

slbTrapConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 0, 2)
)
slbTrapConfigChanged.setObjects(
      *(("ALCATEL-IND1-SLB-MIB", "slbTrapInfoEntityGroup"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoClusterName"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoServerIpAddr"))
)
if mibBuilder.loadTexts:
    slbTrapConfigChanged.setStatus(
        "current"
    )

slbTrapOperStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 0, 3)
)
slbTrapOperStatus.setObjects(
      *(("ALCATEL-IND1-SLB-MIB", "slbTrapInfoEntityGroup"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoOperStatus"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoClusterName"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapInfoServerIpAddr"))
)
if mibBuilder.loadTexts:
    slbTrapOperStatus.setStatus(
        "current"
    )


# Notifications groups

slbTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 1, 4)
)
slbTrapsGroup.setObjects(
      *(("ALCATEL-IND1-SLB-MIB", "slbTrapException"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapConfigChanged"),
        ("ALCATEL-IND1-SLB-MIB", "slbTrapOperStatus"))
)
if mibBuilder.loadTexts:
    slbTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1SLBMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 20, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SLBMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-SLB-MIB",
    **{"SlbAdminState": SlbAdminState,
       "SlbOperState": SlbOperState,
       "SlbRedirectAlgorithm": SlbRedirectAlgorithm,
       "SlbHashSelector": SlbHashSelector,
       "SlbServerOperState": SlbServerOperState,
       "alcatelIND1SLBMIB": alcatelIND1SLBMIB,
       "alcatelIND1SLBMIBNotifications": alcatelIND1SLBMIBNotifications,
       "slbTrapException": slbTrapException,
       "slbTrapConfigChanged": slbTrapConfigChanged,
       "slbTrapOperStatus": slbTrapOperStatus,
       "alcatelIND1SLBMIBObjects": alcatelIND1SLBMIBObjects,
       "slbFeature": slbFeature,
       "slbAdminStatus": slbAdminStatus,
       "slbOperStatus": slbOperStatus,
       "slbClustersCount": slbClustersCount,
       "slbResetStatistics": slbResetStatistics,
       "slbClusters": slbClusters,
       "slbClusterTable": slbClusterTable,
       "slbClusterTableEntry": slbClusterTableEntry,
       "slbClusterName": slbClusterName,
       "slbClusterAdminStatus": slbClusterAdminStatus,
       "slbClusterOperStatus": slbClusterOperStatus,
       "slbClusterVIP": slbClusterVIP,
       "slbClusterPingPeriod": slbClusterPingPeriod,
       "slbClusterPingTimeout": slbClusterPingTimeout,
       "slbClusterPingRetries": slbClusterPingRetries,
       "slbClusterRedirectAlgorithm": slbClusterRedirectAlgorithm,
       "slbClusterIdleTimer": slbClusterIdleTimer,
       "slbClusterNumberOfServers": slbClusterNumberOfServers,
       "slbClusterNewFlows": slbClusterNewFlows,
       "slbClusterRowStatus": slbClusterRowStatus,
       "slbClusterProbeName": slbClusterProbeName,
       "slbClusterPackets": slbClusterPackets,
       "slbClusterCondition": slbClusterCondition,
       "slbClusterType": slbClusterType,
       "slbClusterHashType": slbClusterHashType,
       "slbServers": slbServers,
       "slbServerTable": slbServerTable,
       "slbServerTableEntry": slbServerTableEntry,
       "slbServerClusterName": slbServerClusterName,
       "slbServerIpAddress": slbServerIpAddress,
       "slbServerAdminStatus": slbServerAdminStatus,
       "slbServerOperStatus": slbServerOperStatus,
       "slbServerAdminWeight": slbServerAdminWeight,
       "slbServerUpTime": slbServerUpTime,
       "slbServerLastRTT": slbServerLastRTT,
       "slbServerPingFails": slbServerPingFails,
       "slbServerPortDown": slbServerPortDown,
       "slbServerFlows": slbServerFlows,
       "slbServerRowStatus": slbServerRowStatus,
       "slbServerProbeName": slbServerProbeName,
       "slbServerProbeStatus": slbServerProbeStatus,
       "slbProbes": slbProbes,
       "slbProbeTable": slbProbeTable,
       "slbProbeTableEntry": slbProbeTableEntry,
       "slbProbeName": slbProbeName,
       "slbProbeMethod": slbProbeMethod,
       "slbProbePeriod": slbProbePeriod,
       "slbProbeTimeout": slbProbeTimeout,
       "slbProbeRetries": slbProbeRetries,
       "slbProbePort": slbProbePort,
       "slbProbeExpect": slbProbeExpect,
       "slbProbeSSL": slbProbeSSL,
       "slbProbeSend": slbProbeSend,
       "slbProbeHttpStatus": slbProbeHttpStatus,
       "slbProbeHttpUrl": slbProbeHttpUrl,
       "slbProbeHttpUsername": slbProbeHttpUsername,
       "slbProbeHttpPassword": slbProbeHttpPassword,
       "slbProbeRowStatus": slbProbeRowStatus,
       "slbStats": slbStats,
       "slbStatsTable": slbStatsTable,
       "slbStatsTableEntry": slbStatsTableEntry,
       "slbStatsClusterName": slbStatsClusterName,
       "slbStatsIndex": slbStatsIndex,
       "slbStatsCounter": slbStatsCounter,
       "slbStatsQualTable": slbStatsQualTable,
       "slbStatsQualTableEntry": slbStatsQualTableEntry,
       "slbStatsQualType": slbStatsQualType,
       "slbStatsQualDataIp": slbStatsQualDataIp,
       "slbStatsQualDataIpMask": slbStatsQualDataIpMask,
       "slbStatsQualDataSlot": slbStatsQualDataSlot,
       "slbStatsQualDataStartPort": slbStatsQualDataStartPort,
       "slbStatsQualDataEndPort": slbStatsQualDataEndPort,
       "slbStatsQualDataIpProtocol": slbStatsQualDataIpProtocol,
       "slbStatsQualDataVlan": slbStatsQualDataVlan,
       "slbStatsQualDataL4Port": slbStatsQualDataL4Port,
       "slbStatsQualDataMac": slbStatsQualDataMac,
       "slbStatsQualDataMacMask": slbStatsQualDataMacMask,
       "slbStatsQualDataEthertype": slbStatsQualDataEthertype,
       "slbStatsQualDataIcmpData": slbStatsQualDataIcmpData,
       "slbStatsQualDataTcpFlags": slbStatsQualDataTcpFlags,
       "slbStatsQualDataTos": slbStatsQualDataTos,
       "slbStatsQualData8021p": slbStatsQualData8021p,
       "slbStatsQual": slbStatsQual,
       "slbTrapsObj": slbTrapsObj,
       "slbTrapInfoClusterName": slbTrapInfoClusterName,
       "slbTrapInfoOperStatus": slbTrapInfoOperStatus,
       "slbTrapInfoServerIpAddr": slbTrapInfoServerIpAddr,
       "slbTrapInfoEntityGroup": slbTrapInfoEntityGroup,
       "slbTrapInfoException": slbTrapInfoException,
       "alcatelIND1SLBMIBConformance": alcatelIND1SLBMIBConformance,
       "alcatelIND1SLBMIBGroups": alcatelIND1SLBMIBGroups,
       "slbFeatureGroup": slbFeatureGroup,
       "slbClustersGroup": slbClustersGroup,
       "slbServersGroup": slbServersGroup,
       "slbTrapsGroup": slbTrapsGroup,
       "slbProbesGroup": slbProbesGroup,
       "slbStatsGroup": slbStatsGroup,
       "slbTrapsObjGroup": slbTrapsObjGroup,
       "alcatelIND1SLBMIBCompliances": alcatelIND1SLBMIBCompliances,
       "alcatelIND1SLBMIBCompliance": alcatelIND1SLBMIBCompliance}
)
