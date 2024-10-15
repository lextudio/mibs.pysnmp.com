# SNMP MIB module (CISCO-NAT-CGN-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NAT-CGN-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:02 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(NatBehaviorType,
 NatPoolingType,
 natCountersEntry,
 natInstanceEntry,
 natInstanceIndex) = mibBuilder.importSymbols(
    "NAT-MIB",
    "NatBehaviorType",
    "NatPoolingType",
    "natCountersEntry",
    "natInstanceEntry",
    "natInstanceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoNatCgnExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 818)
)
ciscoNatCgnExtMIB.setRevisions(
        ("2014-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NatCgnInstanceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsLite", 3),
          ("nat44", 1),
          ("nat64Stateful", 2))
    )



class NatCgnALGType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("algActiveFTP", 1),
          ("algDNS", 2),
          ("algH323", 3),
          ("algHTTP", 4),
          ("algLDAP", 5),
          ("algMSRPC", 6),
          ("algNetBIOS", 7),
          ("algPCP", 8),
          ("algPPTP", 9),
          ("algRCMD", 10),
          ("algRTSP", 11),
          ("algSCCP", 12),
          ("algSIP", 13),
          ("algSunRPC", 14))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoNatCgnExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNatCgnExtMIBNotifs = _CiscoNatCgnExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 0)
)
_CiscoNatCgnExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNatCgnExtMIBObjects = _CiscoNatCgnExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1)
)
_CNatCgnInstanceTable_Object = MibTable
cNatCgnInstanceTable = _CNatCgnInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1)
)
if mibBuilder.loadTexts:
    cNatCgnInstanceTable.setStatus("current")
_CNatCgnInstanceEntry_Object = MibTableRow
cNatCgnInstanceEntry = _CNatCgnInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cNatCgnInstanceEntry.setStatus("current")
_CNatCgnInstanceType_Type = NatCgnInstanceType
_CNatCgnInstanceType_Object = MibTableColumn
cNatCgnInstanceType = _CNatCgnInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1, 1, 1),
    _CNatCgnInstanceType_Type()
)
cNatCgnInstanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnInstanceType.setStatus("current")


class _CNatCgnInstanceServiceName_Type(SnmpAdminString):
    """Custom type cNatCgnInstanceServiceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CNatCgnInstanceServiceName_Type.__name__ = "SnmpAdminString"
_CNatCgnInstanceServiceName_Object = MibTableColumn
cNatCgnInstanceServiceName = _CNatCgnInstanceServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1, 1, 2),
    _CNatCgnInstanceServiceName_Type()
)
cNatCgnInstanceServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnInstanceServiceName.setStatus("current")


class _CNatCgnInstanceVrf_Type(SnmpAdminString):
    """Custom type cNatCgnInstanceVrf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CNatCgnInstanceVrf_Type.__name__ = "SnmpAdminString"
_CNatCgnInstanceVrf_Object = MibTableColumn
cNatCgnInstanceVrf = _CNatCgnInstanceVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1, 1, 3),
    _CNatCgnInstanceVrf_Type()
)
cNatCgnInstanceVrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnInstanceVrf.setStatus("current")


class _CNatCgnInstanceInterface_Type(SnmpAdminString):
    """Custom type cNatCgnInstanceInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CNatCgnInstanceInterface_Type.__name__ = "SnmpAdminString"
_CNatCgnInstanceInterface_Object = MibTableColumn
cNatCgnInstanceInterface = _CNatCgnInstanceInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1, 1, 4),
    _CNatCgnInstanceInterface_Type()
)
cNatCgnInstanceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnInstanceInterface.setStatus("current")
_CNatCgnInstanceBehaviorType_Type = NatBehaviorType
_CNatCgnInstanceBehaviorType_Object = MibTableColumn
cNatCgnInstanceBehaviorType = _CNatCgnInstanceBehaviorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1, 1, 5),
    _CNatCgnInstanceBehaviorType_Type()
)
cNatCgnInstanceBehaviorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnInstanceBehaviorType.setStatus("current")
_CNatCgnInstancePoolingType_Type = NatPoolingType
_CNatCgnInstancePoolingType_Object = MibTableColumn
cNatCgnInstancePoolingType = _CNatCgnInstancePoolingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1, 1, 6),
    _CNatCgnInstancePoolingType_Type()
)
cNatCgnInstancePoolingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnInstancePoolingType.setStatus("current")


class _CNatCgnInstanceProtocolPortLimit_Type(Unsigned32):
    """Custom type cNatCgnInstanceProtocolPortLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CNatCgnInstanceProtocolPortLimit_Type.__name__ = "Unsigned32"
_CNatCgnInstanceProtocolPortLimit_Object = MibTableColumn
cNatCgnInstanceProtocolPortLimit = _CNatCgnInstanceProtocolPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1, 1, 7),
    _CNatCgnInstanceProtocolPortLimit_Type()
)
cNatCgnInstanceProtocolPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnInstanceProtocolPortLimit.setStatus("current")


class _CNatCgnInstanceProtocolPortBulkAllocControl_Type(Unsigned32):
    """Custom type cNatCgnInstanceProtocolPortBulkAllocControl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CNatCgnInstanceProtocolPortBulkAllocControl_Type.__name__ = "Unsigned32"
_CNatCgnInstanceProtocolPortBulkAllocControl_Object = MibTableColumn
cNatCgnInstanceProtocolPortBulkAllocControl = _CNatCgnInstanceProtocolPortBulkAllocControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 1, 1, 8),
    _CNatCgnInstanceProtocolPortBulkAllocControl_Type()
)
cNatCgnInstanceProtocolPortBulkAllocControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnInstanceProtocolPortBulkAllocControl.setStatus("current")
_CNatCgnCounters_ObjectIdentity = ObjectIdentity
cNatCgnCounters = _CNatCgnCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2)
)
_CNatCgnCounterTable_Object = MibTable
cNatCgnCounterTable = _CNatCgnCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cNatCgnCounterTable.setStatus("current")
_CNatCgnCounterEntry_Object = MibTableRow
cNatCgnCounterEntry = _CNatCgnCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cNatCgnCounterEntry.setStatus("current")
_CNatCgnCounterSessionCreations_Type = Counter64
_CNatCgnCounterSessionCreations_Object = MibTableColumn
cNatCgnCounterSessionCreations = _CNatCgnCounterSessionCreations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 1),
    _CNatCgnCounterSessionCreations_Type()
)
cNatCgnCounterSessionCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterSessionCreations.setStatus("current")
_CNatCgnCounterSessionRemovals_Type = Counter64
_CNatCgnCounterSessionRemovals_Object = MibTableColumn
cNatCgnCounterSessionRemovals = _CNatCgnCounterSessionRemovals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 2),
    _CNatCgnCounterSessionRemovals_Type()
)
cNatCgnCounterSessionRemovals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterSessionRemovals.setStatus("current")
_CNatCgnCounterOutOfSessionDrops_Type = Counter64
_CNatCgnCounterOutOfSessionDrops_Object = MibTableColumn
cNatCgnCounterOutOfSessionDrops = _CNatCgnCounterOutOfSessionDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 3),
    _CNatCgnCounterOutOfSessionDrops_Type()
)
cNatCgnCounterOutOfSessionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterOutOfSessionDrops.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterOutOfSessionDrops.setUnits("packets")
_CNatCgnCounterSessionLimitDrops_Type = Counter64
_CNatCgnCounterSessionLimitDrops_Object = MibTableColumn
cNatCgnCounterSessionLimitDrops = _CNatCgnCounterSessionLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 4),
    _CNatCgnCounterSessionLimitDrops_Type()
)
cNatCgnCounterSessionLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterSessionLimitDrops.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterSessionLimitDrops.setUnits("packets")
_CNatCgnCounterNoMappingEntryDrops_Type = Counter64
_CNatCgnCounterNoMappingEntryDrops_Object = MibTableColumn
cNatCgnCounterNoMappingEntryDrops = _CNatCgnCounterNoMappingEntryDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 5),
    _CNatCgnCounterNoMappingEntryDrops_Type()
)
cNatCgnCounterNoMappingEntryDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterNoMappingEntryDrops.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterNoMappingEntryDrops.setUnits("packets")
_CNatCgnCounterSourceIPOutOfRangeDrops_Type = Counter64
_CNatCgnCounterSourceIPOutOfRangeDrops_Object = MibTableColumn
cNatCgnCounterSourceIPOutOfRangeDrops = _CNatCgnCounterSourceIPOutOfRangeDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 6),
    _CNatCgnCounterSourceIPOutOfRangeDrops_Type()
)
cNatCgnCounterSourceIPOutOfRangeDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterSourceIPOutOfRangeDrops.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterSourceIPOutOfRangeDrops.setUnits("packets")
_CNatCgnCounterEndPointFilteringDrops_Type = Counter64
_CNatCgnCounterEndPointFilteringDrops_Object = MibTableColumn
cNatCgnCounterEndPointFilteringDrops = _CNatCgnCounterEndPointFilteringDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 7),
    _CNatCgnCounterEndPointFilteringDrops_Type()
)
cNatCgnCounterEndPointFilteringDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterEndPointFilteringDrops.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterEndPointFilteringDrops.setUnits("packets")
_CNatCgnCounterTCPSequenceDrops_Type = Counter64
_CNatCgnCounterTCPSequenceDrops_Object = MibTableColumn
cNatCgnCounterTCPSequenceDrops = _CNatCgnCounterTCPSequenceDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 8),
    _CNatCgnCounterTCPSequenceDrops_Type()
)
cNatCgnCounterTCPSequenceDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterTCPSequenceDrops.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterTCPSequenceDrops.setUnits("packets")
_CNatCgnCounterTCPMappingDrops_Type = Counter64
_CNatCgnCounterTCPMappingDrops_Object = MibTableColumn
cNatCgnCounterTCPMappingDrops = _CNatCgnCounterTCPMappingDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 9),
    _CNatCgnCounterTCPMappingDrops_Type()
)
cNatCgnCounterTCPMappingDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterTCPMappingDrops.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterTCPMappingDrops.setUnits("packets")
_CNatCgnCounterFragmentPktsInToOutDrops_Type = Counter64
_CNatCgnCounterFragmentPktsInToOutDrops_Object = MibTableColumn
cNatCgnCounterFragmentPktsInToOutDrops = _CNatCgnCounterFragmentPktsInToOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 10),
    _CNatCgnCounterFragmentPktsInToOutDrops_Type()
)
cNatCgnCounterFragmentPktsInToOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterFragmentPktsInToOutDrops.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterFragmentPktsInToOutDrops.setUnits("packets")
_CNatCgnCounterFragmentPktsOutToInDrops_Type = Counter64
_CNatCgnCounterFragmentPktsOutToInDrops_Object = MibTableColumn
cNatCgnCounterFragmentPktsOutToInDrops = _CNatCgnCounterFragmentPktsOutToInDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 11),
    _CNatCgnCounterFragmentPktsOutToInDrops_Type()
)
cNatCgnCounterFragmentPktsOutToInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterFragmentPktsOutToInDrops.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterFragmentPktsOutToInDrops.setUnits("packets")


class _CNatCgnCounterCurrentPortAllocation_Type(Integer32):
    """Custom type cNatCgnCounterCurrentPortAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CNatCgnCounterCurrentPortAllocation_Type.__name__ = "Integer32"
_CNatCgnCounterCurrentPortAllocation_Object = MibTableColumn
cNatCgnCounterCurrentPortAllocation = _CNatCgnCounterCurrentPortAllocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 12),
    _CNatCgnCounterCurrentPortAllocation_Type()
)
cNatCgnCounterCurrentPortAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterCurrentPortAllocation.setStatus("current")


class _CNatCgnCounterPortUsageLowThreshold_Type(Integer32):
    """Custom type cNatCgnCounterPortUsageLowThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CNatCgnCounterPortUsageLowThreshold_Type.__name__ = "Integer32"
_CNatCgnCounterPortUsageLowThreshold_Object = MibTableColumn
cNatCgnCounterPortUsageLowThreshold = _CNatCgnCounterPortUsageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 13),
    _CNatCgnCounterPortUsageLowThreshold_Type()
)
cNatCgnCounterPortUsageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnCounterPortUsageLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterPortUsageLowThreshold.setUnits("percent")


class _CNatCgnCounterPortUsageClearLowThreshold_Type(Integer32):
    """Custom type cNatCgnCounterPortUsageClearLowThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CNatCgnCounterPortUsageClearLowThreshold_Type.__name__ = "Integer32"
_CNatCgnCounterPortUsageClearLowThreshold_Object = MibTableColumn
cNatCgnCounterPortUsageClearLowThreshold = _CNatCgnCounterPortUsageClearLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 14),
    _CNatCgnCounterPortUsageClearLowThreshold_Type()
)
cNatCgnCounterPortUsageClearLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnCounterPortUsageClearLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterPortUsageClearLowThreshold.setUnits("percent")


class _CNatCgnCounterPortUsageHighThreshold_Type(Integer32):
    """Custom type cNatCgnCounterPortUsageHighThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CNatCgnCounterPortUsageHighThreshold_Type.__name__ = "Integer32"
_CNatCgnCounterPortUsageHighThreshold_Object = MibTableColumn
cNatCgnCounterPortUsageHighThreshold = _CNatCgnCounterPortUsageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 15),
    _CNatCgnCounterPortUsageHighThreshold_Type()
)
cNatCgnCounterPortUsageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnCounterPortUsageHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterPortUsageHighThreshold.setUnits("percent")


class _CNatCgnCounterPortUsageClearHighThreshold_Type(Integer32):
    """Custom type cNatCgnCounterPortUsageClearHighThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CNatCgnCounterPortUsageClearHighThreshold_Type.__name__ = "Integer32"
_CNatCgnCounterPortUsageClearHighThreshold_Object = MibTableColumn
cNatCgnCounterPortUsageClearHighThreshold = _CNatCgnCounterPortUsageClearHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 16),
    _CNatCgnCounterPortUsageClearHighThreshold_Type()
)
cNatCgnCounterPortUsageClearHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cNatCgnCounterPortUsageClearHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cNatCgnCounterPortUsageClearHighThreshold.setUnits("percent")


class _CNatCgnCounterAverageBulkPortUsage_Type(Gauge32):
    """Custom type cNatCgnCounterAverageBulkPortUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CNatCgnCounterAverageBulkPortUsage_Type.__name__ = "Gauge32"
_CNatCgnCounterAverageBulkPortUsage_Object = MibTableColumn
cNatCgnCounterAverageBulkPortUsage = _CNatCgnCounterAverageBulkPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 1, 1, 17),
    _CNatCgnCounterAverageBulkPortUsage_Type()
)
cNatCgnCounterAverageBulkPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnCounterAverageBulkPortUsage.setStatus("current")
_CNatCgnLogStatTable_Object = MibTable
cNatCgnLogStatTable = _CNatCgnLogStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cNatCgnLogStatTable.setStatus("current")
_CNatCgnLogStatEntry_Object = MibTableRow
cNatCgnLogStatEntry = _CNatCgnLogStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2, 1)
)
cNatCgnLogStatEntry.setIndexNames(
    (0, "NAT-MIB", "natInstanceIndex"),
)
if mibBuilder.loadTexts:
    cNatCgnLogStatEntry.setStatus("current")
_CNatCgnLogStatMappingCreateRecords_Type = Counter64
_CNatCgnLogStatMappingCreateRecords_Object = MibTableColumn
cNatCgnLogStatMappingCreateRecords = _CNatCgnLogStatMappingCreateRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2, 1, 1),
    _CNatCgnLogStatMappingCreateRecords_Type()
)
cNatCgnLogStatMappingCreateRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnLogStatMappingCreateRecords.setStatus("current")
_CNatCgnLogStatMappingDeleteRecords_Type = Counter64
_CNatCgnLogStatMappingDeleteRecords_Object = MibTableColumn
cNatCgnLogStatMappingDeleteRecords = _CNatCgnLogStatMappingDeleteRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2, 1, 2),
    _CNatCgnLogStatMappingDeleteRecords_Type()
)
cNatCgnLogStatMappingDeleteRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnLogStatMappingDeleteRecords.setStatus("current")
_CNatCgnLogStatSessionCreateRecords_Type = Counter64
_CNatCgnLogStatSessionCreateRecords_Object = MibTableColumn
cNatCgnLogStatSessionCreateRecords = _CNatCgnLogStatSessionCreateRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2, 1, 3),
    _CNatCgnLogStatSessionCreateRecords_Type()
)
cNatCgnLogStatSessionCreateRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnLogStatSessionCreateRecords.setStatus("current")
_CNatCgnLogStatSessionDeleteRecords_Type = Counter64
_CNatCgnLogStatSessionDeleteRecords_Object = MibTableColumn
cNatCgnLogStatSessionDeleteRecords = _CNatCgnLogStatSessionDeleteRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2, 1, 4),
    _CNatCgnLogStatSessionDeleteRecords_Type()
)
cNatCgnLogStatSessionDeleteRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnLogStatSessionDeleteRecords.setStatus("current")
_CNatCgnLogStatNetflowPackets_Type = Counter64
_CNatCgnLogStatNetflowPackets_Object = MibTableColumn
cNatCgnLogStatNetflowPackets = _CNatCgnLogStatNetflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2, 1, 5),
    _CNatCgnLogStatNetflowPackets_Type()
)
cNatCgnLogStatNetflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnLogStatNetflowPackets.setStatus("current")
_CNatCgnLogStatNetflowPacketDrops_Type = Counter64
_CNatCgnLogStatNetflowPacketDrops_Object = MibTableColumn
cNatCgnLogStatNetflowPacketDrops = _CNatCgnLogStatNetflowPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2, 1, 6),
    _CNatCgnLogStatNetflowPacketDrops_Type()
)
cNatCgnLogStatNetflowPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnLogStatNetflowPacketDrops.setStatus("current")
_CNatCgnLogStatSyslogPackets_Type = Counter64
_CNatCgnLogStatSyslogPackets_Object = MibTableColumn
cNatCgnLogStatSyslogPackets = _CNatCgnLogStatSyslogPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2, 1, 7),
    _CNatCgnLogStatSyslogPackets_Type()
)
cNatCgnLogStatSyslogPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnLogStatSyslogPackets.setStatus("current")
_CNatCgnLogStatSyslogPacketDrops_Type = Counter64
_CNatCgnLogStatSyslogPacketDrops_Object = MibTableColumn
cNatCgnLogStatSyslogPacketDrops = _CNatCgnLogStatSyslogPacketDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 2, 1, 8),
    _CNatCgnLogStatSyslogPacketDrops_Type()
)
cNatCgnLogStatSyslogPacketDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnLogStatSyslogPacketDrops.setStatus("current")
_CNatCgnALGCountersTable_Object = MibTable
cNatCgnALGCountersTable = _CNatCgnALGCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cNatCgnALGCountersTable.setStatus("current")
_CNatCgnALGCountersEntry_Object = MibTableRow
cNatCgnALGCountersEntry = _CNatCgnALGCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 3, 1)
)
cNatCgnALGCountersEntry.setIndexNames(
    (0, "NAT-MIB", "natInstanceIndex"),
    (0, "CISCO-NAT-CGN-EXT-MIB", "cNatCgnALGType"),
)
if mibBuilder.loadTexts:
    cNatCgnALGCountersEntry.setStatus("current")
_CNatCgnALGType_Type = NatCgnALGType
_CNatCgnALGType_Object = MibTableColumn
cNatCgnALGType = _CNatCgnALGType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 3, 1, 1),
    _CNatCgnALGType_Type()
)
cNatCgnALGType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cNatCgnALGType.setStatus("current")


class _CNatCgnALGStatus_Type(Integer32):
    """Custom type cNatCgnALGStatus based on Integer32"""
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
        *(("enabled", 4),
          ("notApplicable", 1),
          ("notEnabled", 3),
          ("unSupported", 2))
    )


_CNatCgnALGStatus_Type.__name__ = "Integer32"
_CNatCgnALGStatus_Object = MibTableColumn
cNatCgnALGStatus = _CNatCgnALGStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 3, 1, 2),
    _CNatCgnALGStatus_Type()
)
cNatCgnALGStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnALGStatus.setStatus("current")
_CNatCgnALGMappingCreations_Type = Counter64
_CNatCgnALGMappingCreations_Object = MibTableColumn
cNatCgnALGMappingCreations = _CNatCgnALGMappingCreations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 3, 1, 3),
    _CNatCgnALGMappingCreations_Type()
)
cNatCgnALGMappingCreations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnALGMappingCreations.setStatus("current")
_CNatCgnALGMappingRemovals_Type = Counter64
_CNatCgnALGMappingRemovals_Object = MibTableColumn
cNatCgnALGMappingRemovals = _CNatCgnALGMappingRemovals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 3, 1, 4),
    _CNatCgnALGMappingRemovals_Type()
)
cNatCgnALGMappingRemovals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnALGMappingRemovals.setStatus("current")
_CNatCgnALGUnsupportedErrors_Type = Counter64
_CNatCgnALGUnsupportedErrors_Object = MibTableColumn
cNatCgnALGUnsupportedErrors = _CNatCgnALGUnsupportedErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 3, 1, 5),
    _CNatCgnALGUnsupportedErrors_Type()
)
cNatCgnALGUnsupportedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnALGUnsupportedErrors.setStatus("current")
_CNatCgnALGProtocolErrors_Type = Counter64
_CNatCgnALGProtocolErrors_Object = MibTableColumn
cNatCgnALGProtocolErrors = _CNatCgnALGProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 1, 2, 3, 1, 6),
    _CNatCgnALGProtocolErrors_Type()
)
cNatCgnALGProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNatCgnALGProtocolErrors.setStatus("current")
_CiscoNatCgnExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoNatCgnExtMIBConform = _CiscoNatCgnExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2)
)
_CNatCgnMIBCompliances_ObjectIdentity = ObjectIdentity
cNatCgnMIBCompliances = _CNatCgnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 1)
)
_CNatCgnMIBGroups_ObjectIdentity = ObjectIdentity
cNatCgnMIBGroups = _CNatCgnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2)
)
natInstanceEntry.registerAugmentions(
    ("CISCO-NAT-CGN-EXT-MIB",
     "cNatCgnInstanceEntry")
)
cNatCgnInstanceEntry.setIndexNames(*natInstanceEntry.getIndexNames())
natCountersEntry.registerAugmentions(
    ("CISCO-NAT-CGN-EXT-MIB",
     "cNatCgnCounterEntry")
)
cNatCgnCounterEntry.setIndexNames(*natCountersEntry.getIndexNames())

# Managed Objects groups

cNatCgnConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 1)
)
cNatCgnConfigGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnInstanceType"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnInstanceInterface"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnInstanceVrf"))
)
if mibBuilder.loadTexts:
    cNatCgnConfigGroup.setStatus("current")

cNatCgnOptionConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 2)
)
cNatCgnOptionConfigGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnInstanceBehaviorType"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnInstancePoolingType"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnInstanceProtocolPortLimit"))
)
if mibBuilder.loadTexts:
    cNatCgnOptionConfigGroup.setStatus("current")

cNatCgnCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 3)
)
cNatCgnCountersGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterNoMappingEntryDrops"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterSourceIPOutOfRangeDrops"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterEndPointFilteringDrops"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterTCPSequenceDrops"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterTCPMappingDrops"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterCurrentPortAllocation"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterPortUsageLowThreshold"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterPortUsageClearLowThreshold"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterPortUsageHighThreshold"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterPortUsageClearHighThreshold"))
)
if mibBuilder.loadTexts:
    cNatCgnCountersGroup.setStatus("current")

cNatCgnSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 4)
)
cNatCgnSessionGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterSessionCreations"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterSessionRemovals"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterOutOfSessionDrops"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterEndPointFilteringDrops"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterSessionLimitDrops"))
)
if mibBuilder.loadTexts:
    cNatCgnSessionGroup.setStatus("current")

cNatCgnBulkAllocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 5)
)
cNatCgnBulkAllocGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnInstanceProtocolPortBulkAllocControl"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterAverageBulkPortUsage"))
)
if mibBuilder.loadTexts:
    cNatCgnBulkAllocGroup.setStatus("current")

cNatCgnNetflowLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 6)
)
cNatCgnNetflowLoggingGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatMappingCreateRecords"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatMappingDeleteRecords"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatSessionCreateRecords"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatSessionDeleteRecords"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatNetflowPackets"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatNetflowPacketDrops"))
)
if mibBuilder.loadTexts:
    cNatCgnNetflowLoggingGroup.setStatus("current")

cNatCgnSyslogLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 7)
)
cNatCgnSyslogLoggingGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatMappingCreateRecords"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatMappingDeleteRecords"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatSessionCreateRecords"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatSessionDeleteRecords"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatSyslogPackets"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnLogStatSyslogPacketDrops"))
)
if mibBuilder.loadTexts:
    cNatCgnSyslogLoggingGroup.setStatus("current")

cNatCgnFragmentsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 8)
)
cNatCgnFragmentsGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterFragmentPktsInToOutDrops"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterFragmentPktsOutToInDrops"))
)
if mibBuilder.loadTexts:
    cNatCgnFragmentsGroup.setStatus("current")

cNatCgnALGCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 9)
)
cNatCgnALGCountersGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnALGStatus"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnALGMappingCreations"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnALGMappingRemovals"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnALGUnsupportedErrors"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnALGProtocolErrors"))
)
if mibBuilder.loadTexts:
    cNatCgnALGCountersGroup.setStatus("current")

cNatCgnServiceNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 11)
)
cNatCgnServiceNameGroup.setObjects(
    ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnInstanceServiceName")
)
if mibBuilder.loadTexts:
    cNatCgnServiceNameGroup.setStatus("current")


# Notification objects

cNatCgnNotifPortUsageWatermarkLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 0, 1)
)
cNatCgnNotifPortUsageWatermarkLow.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterCurrentPortAllocation"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterPortUsageLowThreshold"))
)
if mibBuilder.loadTexts:
    cNatCgnNotifPortUsageWatermarkLow.setStatus(
        "current"
    )

cNatCgnNotifPortUsageWatermarkLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 0, 2)
)
cNatCgnNotifPortUsageWatermarkLowClear.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterCurrentPortAllocation"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterPortUsageClearLowThreshold"))
)
if mibBuilder.loadTexts:
    cNatCgnNotifPortUsageWatermarkLowClear.setStatus(
        "current"
    )

cNatCgnNotifPortUsageWatermarkHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 0, 3)
)
cNatCgnNotifPortUsageWatermarkHigh.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterCurrentPortAllocation"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterPortUsageHighThreshold"))
)
if mibBuilder.loadTexts:
    cNatCgnNotifPortUsageWatermarkHigh.setStatus(
        "current"
    )

cNatCgnNotifPortUsageWatermarkHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 0, 4)
)
cNatCgnNotifPortUsageWatermarkHighClear.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterCurrentPortAllocation"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnCounterPortUsageClearHighThreshold"))
)
if mibBuilder.loadTexts:
    cNatCgnNotifPortUsageWatermarkHighClear.setStatus(
        "current"
    )


# Notifications groups

cNatCgnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 2, 15)
)
cNatCgnNotificationsGroup.setObjects(
      *(("CISCO-NAT-CGN-EXT-MIB", "cNatCgnNotifPortUsageWatermarkLow"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnNotifPortUsageWatermarkLowClear"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnNotifPortUsageWatermarkHigh"),
        ("CISCO-NAT-CGN-EXT-MIB", "cNatCgnNotifPortUsageWatermarkHighClear"))
)
if mibBuilder.loadTexts:
    cNatCgnNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cNatCgnModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 818, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cNatCgnModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NAT-CGN-EXT-MIB",
    **{"NatCgnInstanceType": NatCgnInstanceType,
       "NatCgnALGType": NatCgnALGType,
       "ciscoNatCgnExtMIB": ciscoNatCgnExtMIB,
       "ciscoNatCgnExtMIBNotifs": ciscoNatCgnExtMIBNotifs,
       "cNatCgnNotifPortUsageWatermarkLow": cNatCgnNotifPortUsageWatermarkLow,
       "cNatCgnNotifPortUsageWatermarkLowClear": cNatCgnNotifPortUsageWatermarkLowClear,
       "cNatCgnNotifPortUsageWatermarkHigh": cNatCgnNotifPortUsageWatermarkHigh,
       "cNatCgnNotifPortUsageWatermarkHighClear": cNatCgnNotifPortUsageWatermarkHighClear,
       "ciscoNatCgnExtMIBObjects": ciscoNatCgnExtMIBObjects,
       "cNatCgnInstanceTable": cNatCgnInstanceTable,
       "cNatCgnInstanceEntry": cNatCgnInstanceEntry,
       "cNatCgnInstanceType": cNatCgnInstanceType,
       "cNatCgnInstanceServiceName": cNatCgnInstanceServiceName,
       "cNatCgnInstanceVrf": cNatCgnInstanceVrf,
       "cNatCgnInstanceInterface": cNatCgnInstanceInterface,
       "cNatCgnInstanceBehaviorType": cNatCgnInstanceBehaviorType,
       "cNatCgnInstancePoolingType": cNatCgnInstancePoolingType,
       "cNatCgnInstanceProtocolPortLimit": cNatCgnInstanceProtocolPortLimit,
       "cNatCgnInstanceProtocolPortBulkAllocControl": cNatCgnInstanceProtocolPortBulkAllocControl,
       "cNatCgnCounters": cNatCgnCounters,
       "cNatCgnCounterTable": cNatCgnCounterTable,
       "cNatCgnCounterEntry": cNatCgnCounterEntry,
       "cNatCgnCounterSessionCreations": cNatCgnCounterSessionCreations,
       "cNatCgnCounterSessionRemovals": cNatCgnCounterSessionRemovals,
       "cNatCgnCounterOutOfSessionDrops": cNatCgnCounterOutOfSessionDrops,
       "cNatCgnCounterSessionLimitDrops": cNatCgnCounterSessionLimitDrops,
       "cNatCgnCounterNoMappingEntryDrops": cNatCgnCounterNoMappingEntryDrops,
       "cNatCgnCounterSourceIPOutOfRangeDrops": cNatCgnCounterSourceIPOutOfRangeDrops,
       "cNatCgnCounterEndPointFilteringDrops": cNatCgnCounterEndPointFilteringDrops,
       "cNatCgnCounterTCPSequenceDrops": cNatCgnCounterTCPSequenceDrops,
       "cNatCgnCounterTCPMappingDrops": cNatCgnCounterTCPMappingDrops,
       "cNatCgnCounterFragmentPktsInToOutDrops": cNatCgnCounterFragmentPktsInToOutDrops,
       "cNatCgnCounterFragmentPktsOutToInDrops": cNatCgnCounterFragmentPktsOutToInDrops,
       "cNatCgnCounterCurrentPortAllocation": cNatCgnCounterCurrentPortAllocation,
       "cNatCgnCounterPortUsageLowThreshold": cNatCgnCounterPortUsageLowThreshold,
       "cNatCgnCounterPortUsageClearLowThreshold": cNatCgnCounterPortUsageClearLowThreshold,
       "cNatCgnCounterPortUsageHighThreshold": cNatCgnCounterPortUsageHighThreshold,
       "cNatCgnCounterPortUsageClearHighThreshold": cNatCgnCounterPortUsageClearHighThreshold,
       "cNatCgnCounterAverageBulkPortUsage": cNatCgnCounterAverageBulkPortUsage,
       "cNatCgnLogStatTable": cNatCgnLogStatTable,
       "cNatCgnLogStatEntry": cNatCgnLogStatEntry,
       "cNatCgnLogStatMappingCreateRecords": cNatCgnLogStatMappingCreateRecords,
       "cNatCgnLogStatMappingDeleteRecords": cNatCgnLogStatMappingDeleteRecords,
       "cNatCgnLogStatSessionCreateRecords": cNatCgnLogStatSessionCreateRecords,
       "cNatCgnLogStatSessionDeleteRecords": cNatCgnLogStatSessionDeleteRecords,
       "cNatCgnLogStatNetflowPackets": cNatCgnLogStatNetflowPackets,
       "cNatCgnLogStatNetflowPacketDrops": cNatCgnLogStatNetflowPacketDrops,
       "cNatCgnLogStatSyslogPackets": cNatCgnLogStatSyslogPackets,
       "cNatCgnLogStatSyslogPacketDrops": cNatCgnLogStatSyslogPacketDrops,
       "cNatCgnALGCountersTable": cNatCgnALGCountersTable,
       "cNatCgnALGCountersEntry": cNatCgnALGCountersEntry,
       "cNatCgnALGType": cNatCgnALGType,
       "cNatCgnALGStatus": cNatCgnALGStatus,
       "cNatCgnALGMappingCreations": cNatCgnALGMappingCreations,
       "cNatCgnALGMappingRemovals": cNatCgnALGMappingRemovals,
       "cNatCgnALGUnsupportedErrors": cNatCgnALGUnsupportedErrors,
       "cNatCgnALGProtocolErrors": cNatCgnALGProtocolErrors,
       "ciscoNatCgnExtMIBConform": ciscoNatCgnExtMIBConform,
       "cNatCgnMIBCompliances": cNatCgnMIBCompliances,
       "cNatCgnModuleCompliance": cNatCgnModuleCompliance,
       "cNatCgnMIBGroups": cNatCgnMIBGroups,
       "cNatCgnConfigGroup": cNatCgnConfigGroup,
       "cNatCgnOptionConfigGroup": cNatCgnOptionConfigGroup,
       "cNatCgnCountersGroup": cNatCgnCountersGroup,
       "cNatCgnSessionGroup": cNatCgnSessionGroup,
       "cNatCgnBulkAllocGroup": cNatCgnBulkAllocGroup,
       "cNatCgnNetflowLoggingGroup": cNatCgnNetflowLoggingGroup,
       "cNatCgnSyslogLoggingGroup": cNatCgnSyslogLoggingGroup,
       "cNatCgnFragmentsGroup": cNatCgnFragmentsGroup,
       "cNatCgnALGCountersGroup": cNatCgnALGCountersGroup,
       "cNatCgnServiceNameGroup": cNatCgnServiceNameGroup,
       "cNatCgnNotificationsGroup": cNatCgnNotificationsGroup}
)
