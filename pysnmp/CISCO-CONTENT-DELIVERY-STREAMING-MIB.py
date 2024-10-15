# SNMP MIB module (CISCO-CONTENT-DELIVERY-STREAMING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CONTENT-DELIVERY-STREAMING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:42 2024
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

ciscoContentDeliveryStreamingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 708)
)
ciscoContentDeliveryStreamingMIB.setRevisions(
        ("2009-09-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoCdsBandwidthUnitType(Integer32, TextualConvention):
    status = "current"
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
        *(("bytesPerSec", 1),
          ("gigaBytesPerSec", 4),
          ("kiloBytesPerSec", 2),
          ("megaBytesPerSec", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCdsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdsMIBObjects = _CiscoCdsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1)
)
_CcdsStreamingModule_ObjectIdentity = ObjectIdentity
ccdsStreamingModule = _CcdsStreamingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1)
)
_CcdsStreamingStatsTable_Object = MibTable
ccdsStreamingStatsTable = _CcdsStreamingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccdsStreamingStatsTable.setStatus("current")
_CcdsStreamingStatsEntry_Object = MibTableRow
ccdsStreamingStatsEntry = _CcdsStreamingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1)
)
ccdsStreamingStatsEntry.setIndexNames(
    (0, "CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsIndex"),
)
if mibBuilder.loadTexts:
    ccdsStreamingStatsEntry.setStatus("current")


class _CcdsStreamingStatsIndex_Type(Unsigned32):
    """Custom type ccdsStreamingStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcdsStreamingStatsIndex_Type.__name__ = "Unsigned32"
_CcdsStreamingStatsIndex_Object = MibTableColumn
ccdsStreamingStatsIndex = _CcdsStreamingStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 1),
    _CcdsStreamingStatsIndex_Type()
)
ccdsStreamingStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccdsStreamingStatsIndex.setStatus("current")
_CcdsStreamingStatsDescr_Type = SnmpAdminString
_CcdsStreamingStatsDescr_Object = MibTableColumn
ccdsStreamingStatsDescr = _CcdsStreamingStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 2),
    _CcdsStreamingStatsDescr_Type()
)
ccdsStreamingStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsDescr.setStatus("current")


class _CcdsStreamingStatsModuleType_Type(Integer32):
    """Custom type ccdsStreamingStatsModuleType based on Integer32"""
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
        *(("fms", 5),
          ("http", 2),
          ("ms", 4),
          ("unknown", 1),
          ("wmt", 3))
    )


_CcdsStreamingStatsModuleType_Type.__name__ = "Integer32"
_CcdsStreamingStatsModuleType_Object = MibTableColumn
ccdsStreamingStatsModuleType = _CcdsStreamingStatsModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 3),
    _CcdsStreamingStatsModuleType_Type()
)
ccdsStreamingStatsModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsModuleType.setStatus("current")
_CcdsStreamingStatsRequests_Type = Counter32
_CcdsStreamingStatsRequests_Object = MibTableColumn
ccdsStreamingStatsRequests = _CcdsStreamingStatsRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 4),
    _CcdsStreamingStatsRequests_Type()
)
ccdsStreamingStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsRequests.setStatus("current")
_CcdsStreamingStatsLiveRequests_Type = Counter32
_CcdsStreamingStatsLiveRequests_Object = MibTableColumn
ccdsStreamingStatsLiveRequests = _CcdsStreamingStatsLiveRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 5),
    _CcdsStreamingStatsLiveRequests_Type()
)
ccdsStreamingStatsLiveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsLiveRequests.setStatus("current")
_CcdsStreamingStatsVODRequests_Type = Counter32
_CcdsStreamingStatsVODRequests_Object = MibTableColumn
ccdsStreamingStatsVODRequests = _CcdsStreamingStatsVODRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 6),
    _CcdsStreamingStatsVODRequests_Type()
)
ccdsStreamingStatsVODRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsVODRequests.setStatus("current")
_CcdsStreamingStatsPrepHitRequests_Type = Counter32
_CcdsStreamingStatsPrepHitRequests_Object = MibTableColumn
ccdsStreamingStatsPrepHitRequests = _CcdsStreamingStatsPrepHitRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 7),
    _CcdsStreamingStatsPrepHitRequests_Type()
)
ccdsStreamingStatsPrepHitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsPrepHitRequests.setStatus("current")
_CcdsStreamingStatsCacheHitRequests_Type = Counter32
_CcdsStreamingStatsCacheHitRequests_Object = MibTableColumn
ccdsStreamingStatsCacheHitRequests = _CcdsStreamingStatsCacheHitRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 8),
    _CcdsStreamingStatsCacheHitRequests_Type()
)
ccdsStreamingStatsCacheHitRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsCacheHitRequests.setStatus("current")
_CcdsStreamingStatsMissRequests_Type = Counter32
_CcdsStreamingStatsMissRequests_Object = MibTableColumn
ccdsStreamingStatsMissRequests = _CcdsStreamingStatsMissRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 9),
    _CcdsStreamingStatsMissRequests_Type()
)
ccdsStreamingStatsMissRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsMissRequests.setStatus("current")
_CcdsStreamingStatsClientErrors_Type = Counter32
_CcdsStreamingStatsClientErrors_Object = MibTableColumn
ccdsStreamingStatsClientErrors = _CcdsStreamingStatsClientErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 10),
    _CcdsStreamingStatsClientErrors_Type()
)
ccdsStreamingStatsClientErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsClientErrors.setStatus("current")
_CcdsStreamingStatsServerErrors_Type = Counter32
_CcdsStreamingStatsServerErrors_Object = MibTableColumn
ccdsStreamingStatsServerErrors = _CcdsStreamingStatsServerErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 11),
    _CcdsStreamingStatsServerErrors_Type()
)
ccdsStreamingStatsServerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsServerErrors.setStatus("current")
_CcdsStreamingStatsBlockedRequests_Type = Counter32
_CcdsStreamingStatsBlockedRequests_Object = MibTableColumn
ccdsStreamingStatsBlockedRequests = _CcdsStreamingStatsBlockedRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 12),
    _CcdsStreamingStatsBlockedRequests_Type()
)
ccdsStreamingStatsBlockedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsBlockedRequests.setStatus("current")
_CcdsStreamingStatsServedBytes_Type = Counter32
_CcdsStreamingStatsServedBytes_Object = MibTableColumn
ccdsStreamingStatsServedBytes = _CcdsStreamingStatsServedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 13),
    _CcdsStreamingStatsServedBytes_Type()
)
ccdsStreamingStatsServedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsServedBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccdsStreamingStatsServedBytes.setUnits("Bytes")
_CcdsStreamingStatsHCServedBytes_Type = Counter64
_CcdsStreamingStatsHCServedBytes_Object = MibTableColumn
ccdsStreamingStatsHCServedBytes = _CcdsStreamingStatsHCServedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 14),
    _CcdsStreamingStatsHCServedBytes_Type()
)
ccdsStreamingStatsHCServedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsHCServedBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccdsStreamingStatsHCServedBytes.setUnits("Bytes")
_CcdsStreamingStatsLiveBytes_Type = Counter32
_CcdsStreamingStatsLiveBytes_Object = MibTableColumn
ccdsStreamingStatsLiveBytes = _CcdsStreamingStatsLiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 15),
    _CcdsStreamingStatsLiveBytes_Type()
)
ccdsStreamingStatsLiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsLiveBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccdsStreamingStatsLiveBytes.setUnits("Bytes")
_CcdsStreamingStatsHCLiveBytes_Type = Counter64
_CcdsStreamingStatsHCLiveBytes_Object = MibTableColumn
ccdsStreamingStatsHCLiveBytes = _CcdsStreamingStatsHCLiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 16),
    _CcdsStreamingStatsHCLiveBytes_Type()
)
ccdsStreamingStatsHCLiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsHCLiveBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccdsStreamingStatsHCLiveBytes.setUnits("Bytes")
_CcdsStreamingStatsVODBytes_Type = Counter32
_CcdsStreamingStatsVODBytes_Object = MibTableColumn
ccdsStreamingStatsVODBytes = _CcdsStreamingStatsVODBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 17),
    _CcdsStreamingStatsVODBytes_Type()
)
ccdsStreamingStatsVODBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsVODBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccdsStreamingStatsVODBytes.setUnits("Bytes")
_CcdsStreamingStatsHCVODBytes_Type = Counter64
_CcdsStreamingStatsHCVODBytes_Object = MibTableColumn
ccdsStreamingStatsHCVODBytes = _CcdsStreamingStatsHCVODBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 18),
    _CcdsStreamingStatsHCVODBytes_Type()
)
ccdsStreamingStatsHCVODBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsHCVODBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccdsStreamingStatsHCVODBytes.setUnits("Bytes")
_CcdsStreamingStatsBandwidthUnit_Type = CiscoCdsBandwidthUnitType
_CcdsStreamingStatsBandwidthUnit_Object = MibTableColumn
ccdsStreamingStatsBandwidthUnit = _CcdsStreamingStatsBandwidthUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 19),
    _CcdsStreamingStatsBandwidthUnit_Type()
)
ccdsStreamingStatsBandwidthUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsBandwidthUnit.setStatus("current")


class _CcdsStreamingStatsBandwidthRate_Type(Gauge32):
    """Custom type ccdsStreamingStatsBandwidthRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcdsStreamingStatsBandwidthRate_Type.__name__ = "Gauge32"
_CcdsStreamingStatsBandwidthRate_Object = MibTableColumn
ccdsStreamingStatsBandwidthRate = _CcdsStreamingStatsBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 20),
    _CcdsStreamingStatsBandwidthRate_Type()
)
ccdsStreamingStatsBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsBandwidthRate.setStatus("current")
_CcdsStreamingStatsConcurrentRequests_Type = Gauge32
_CcdsStreamingStatsConcurrentRequests_Object = MibTableColumn
ccdsStreamingStatsConcurrentRequests = _CcdsStreamingStatsConcurrentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 1, 1, 1, 1, 21),
    _CcdsStreamingStatsConcurrentRequests_Type()
)
ccdsStreamingStatsConcurrentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccdsStreamingStatsConcurrentRequests.setStatus("current")
_CiscoCdsMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCdsMIBConformance = _CiscoCdsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 2)
)
_CiscoCdsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdsMIBCompliances = _CiscoCdsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 2, 1)
)
_CiscoCdsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdsMIBGroups = _CiscoCdsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 2, 2)
)

# Managed Objects groups

ccdsStreamingStatsGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 2, 2, 1)
)
ccdsStreamingStatsGeneralGroup.setObjects(
      *(("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsDescr"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsModuleType"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsRequests"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsClientErrors"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsServerErrors"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsBlockedRequests"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsPrepHitRequests"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsCacheHitRequests"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsMissRequests"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsLiveRequests"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsLiveBytes"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsHCLiveBytes"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsVODRequests"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsVODBytes"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsHCVODBytes"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsServedBytes"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsHCServedBytes"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsBandwidthUnit"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsBandwidthRate"),
        ("CISCO-CONTENT-DELIVERY-STREAMING-MIB", "ccdsStreamingStatsConcurrentRequests"))
)
if mibBuilder.loadTexts:
    ccdsStreamingStatsGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 708, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CONTENT-DELIVERY-STREAMING-MIB",
    **{"CiscoCdsBandwidthUnitType": CiscoCdsBandwidthUnitType,
       "ciscoContentDeliveryStreamingMIB": ciscoContentDeliveryStreamingMIB,
       "ciscoCdsMIBObjects": ciscoCdsMIBObjects,
       "ccdsStreamingModule": ccdsStreamingModule,
       "ccdsStreamingStatsTable": ccdsStreamingStatsTable,
       "ccdsStreamingStatsEntry": ccdsStreamingStatsEntry,
       "ccdsStreamingStatsIndex": ccdsStreamingStatsIndex,
       "ccdsStreamingStatsDescr": ccdsStreamingStatsDescr,
       "ccdsStreamingStatsModuleType": ccdsStreamingStatsModuleType,
       "ccdsStreamingStatsRequests": ccdsStreamingStatsRequests,
       "ccdsStreamingStatsLiveRequests": ccdsStreamingStatsLiveRequests,
       "ccdsStreamingStatsVODRequests": ccdsStreamingStatsVODRequests,
       "ccdsStreamingStatsPrepHitRequests": ccdsStreamingStatsPrepHitRequests,
       "ccdsStreamingStatsCacheHitRequests": ccdsStreamingStatsCacheHitRequests,
       "ccdsStreamingStatsMissRequests": ccdsStreamingStatsMissRequests,
       "ccdsStreamingStatsClientErrors": ccdsStreamingStatsClientErrors,
       "ccdsStreamingStatsServerErrors": ccdsStreamingStatsServerErrors,
       "ccdsStreamingStatsBlockedRequests": ccdsStreamingStatsBlockedRequests,
       "ccdsStreamingStatsServedBytes": ccdsStreamingStatsServedBytes,
       "ccdsStreamingStatsHCServedBytes": ccdsStreamingStatsHCServedBytes,
       "ccdsStreamingStatsLiveBytes": ccdsStreamingStatsLiveBytes,
       "ccdsStreamingStatsHCLiveBytes": ccdsStreamingStatsHCLiveBytes,
       "ccdsStreamingStatsVODBytes": ccdsStreamingStatsVODBytes,
       "ccdsStreamingStatsHCVODBytes": ccdsStreamingStatsHCVODBytes,
       "ccdsStreamingStatsBandwidthUnit": ccdsStreamingStatsBandwidthUnit,
       "ccdsStreamingStatsBandwidthRate": ccdsStreamingStatsBandwidthRate,
       "ccdsStreamingStatsConcurrentRequests": ccdsStreamingStatsConcurrentRequests,
       "ciscoCdsMIBConformance": ciscoCdsMIBConformance,
       "ciscoCdsMIBCompliances": ciscoCdsMIBCompliances,
       "ciscoCdsMIBCompliance": ciscoCdsMIBCompliance,
       "ciscoCdsMIBGroups": ciscoCdsMIBGroups,
       "ccdsStreamingStatsGeneralGroup": ccdsStreamingStatsGeneralGroup}
)
