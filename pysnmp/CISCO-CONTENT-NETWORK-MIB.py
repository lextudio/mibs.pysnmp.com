# SNMP MIB module (CISCO-CONTENT-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CONTENT-NETWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:44 2024
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

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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

ciscoContentNetworkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216)
)
ciscoContentNetworkMIB.setRevisions(
        ("2001-10-11 18:25",
         "2001-05-23 21:34")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoContentNetworkMIBObjects_ObjectIdentity = ObjectIdentity
ciscoContentNetworkMIBObjects = _CiscoContentNetworkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1)
)
_CcnReport_ObjectIdentity = ObjectIdentity
ccnReport = _CcnReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1)
)
_CcnReportDns_ObjectIdentity = ObjectIdentity
ccnReportDns = _CcnReportDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 1)
)
_CcnReportDnsRequestRate_Type = Gauge32
_CcnReportDnsRequestRate_Object = MibScalar
ccnReportDnsRequestRate = _CcnReportDnsRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 1, 1),
    _CcnReportDnsRequestRate_Type()
)
ccnReportDnsRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccnReportDnsRequestRate.setStatus("current")
if mibBuilder.loadTexts:
    ccnReportDnsRequestRate.setUnits("requests-per-second")
_CcnReportDnsClientCount_Type = ZeroBasedCounter32
_CcnReportDnsClientCount_Object = MibScalar
ccnReportDnsClientCount = _CcnReportDnsClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 1, 2),
    _CcnReportDnsClientCount_Type()
)
ccnReportDnsClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccnReportDnsClientCount.setStatus("current")
if mibBuilder.loadTexts:
    ccnReportDnsClientCount.setUnits("clients")
_CcnReportDnsRequests_Type = ZeroBasedCounter32
_CcnReportDnsRequests_Object = MibScalar
ccnReportDnsRequests = _CcnReportDnsRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 1, 3),
    _CcnReportDnsRequests_Type()
)
ccnReportDnsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccnReportDnsRequests.setStatus("current")
if mibBuilder.loadTexts:
    ccnReportDnsRequests.setUnits("requests")
_CcnReportAcct_ObjectIdentity = ObjectIdentity
ccnReportAcct = _CcnReportAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2)
)
_CcnReportAcctBytesServed_Type = ZeroBasedCounter32
_CcnReportAcctBytesServed_Object = MibScalar
ccnReportAcctBytesServed = _CcnReportAcctBytesServed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2, 1),
    _CcnReportAcctBytesServed_Type()
)
ccnReportAcctBytesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccnReportAcctBytesServed.setStatus("current")
if mibBuilder.loadTexts:
    ccnReportAcctBytesServed.setUnits("bytes")
_CcnReportAcctObjectsCached_Type = Gauge32
_CcnReportAcctObjectsCached_Object = MibScalar
ccnReportAcctObjectsCached = _CcnReportAcctObjectsCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2, 2),
    _CcnReportAcctObjectsCached_Type()
)
ccnReportAcctObjectsCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccnReportAcctObjectsCached.setStatus("current")
if mibBuilder.loadTexts:
    ccnReportAcctObjectsCached.setUnits("objects")
_CcnReportAcctCacheHitRate_Type = Gauge32
_CcnReportAcctCacheHitRate_Object = MibScalar
ccnReportAcctCacheHitRate = _CcnReportAcctCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2, 3),
    _CcnReportAcctCacheHitRate_Type()
)
ccnReportAcctCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccnReportAcctCacheHitRate.setStatus("current")
if mibBuilder.loadTexts:
    ccnReportAcctCacheHitRate.setUnits("objects-per-minute")
_CcnReportAcctCacheMissRate_Type = Gauge32
_CcnReportAcctCacheMissRate_Object = MibScalar
ccnReportAcctCacheMissRate = _CcnReportAcctCacheMissRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 1, 1, 2, 4),
    _CcnReportAcctCacheMissRate_Type()
)
ccnReportAcctCacheMissRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccnReportAcctCacheMissRate.setStatus("current")
if mibBuilder.loadTexts:
    ccnReportAcctCacheMissRate.setUnits("objects-per-minute")
_CiscoContentNetworkMIBNotif_ObjectIdentity = ObjectIdentity
ciscoContentNetworkMIBNotif = _CiscoContentNetworkMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 2)
)
_CcnNotifications_ObjectIdentity = ObjectIdentity
ccnNotifications = _CcnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0)
)
_CcnMIBConformance_ObjectIdentity = ObjectIdentity
ccnMIBConformance = _CcnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 3)
)
_CcnMIBCompliances_ObjectIdentity = ObjectIdentity
ccnMIBCompliances = _CcnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 1)
)
_CcnMIBGroups_ObjectIdentity = ObjectIdentity
ccnMIBGroups = _CcnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 2)
)

# Managed Objects groups

ccnReportingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 2, 1)
)
ccnReportingGroup.setObjects(
      *(("CISCO-CONTENT-NETWORK-MIB", "ccnReportDnsRequestRate"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnReportDnsClientCount"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnReportDnsRequests"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnReportAcctBytesServed"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnReportAcctObjectsCached"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnReportAcctCacheHitRate"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnReportAcctCacheMissRate"))
)
if mibBuilder.loadTexts:
    ccnReportingGroup.setStatus("current")


# Notification objects

ccnNotifServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 1)
)
if mibBuilder.loadTexts:
    ccnNotifServerStart.setStatus(
        "deprecated"
    )

ccnNotifServerStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 2)
)
if mibBuilder.loadTexts:
    ccnNotifServerStop.setStatus(
        "deprecated"
    )

ccnNotifOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 3)
)
if mibBuilder.loadTexts:
    ccnNotifOffline.setStatus(
        "current"
    )

ccnNotifNeedsAttention = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 4)
)
if mibBuilder.loadTexts:
    ccnNotifNeedsAttention.setStatus(
        "current"
    )

ccnNotifWaitingForCdm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 5)
)
if mibBuilder.loadTexts:
    ccnNotifWaitingForCdm.setStatus(
        "current"
    )

ccnNotifOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 2, 0, 6)
)
if mibBuilder.loadTexts:
    ccnNotifOnline.setStatus(
        "current"
    )


# Notifications groups

ccnNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 2, 2)
)
ccnNotifGroup.setObjects(
      *(("CISCO-CONTENT-NETWORK-MIB", "ccnNotifServerStart"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifServerStop"))
)
if mibBuilder.loadTexts:
    ccnNotifGroup.setStatus(
        "deprecated"
    )

ccnNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 2, 3)
)
ccnNotifGroupRev1.setObjects(
      *(("CISCO-CONTENT-NETWORK-MIB", "ccnNotifOffline"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifNeedsAttention"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifWaitingForCdm"),
        ("CISCO-CONTENT-NETWORK-MIB", "ccnNotifOnline"))
)
if mibBuilder.loadTexts:
    ccnNotifGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ccnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ccnMIBCompliance.setStatus(
        "deprecated"
    )

ccnMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 216, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ccnMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CONTENT-NETWORK-MIB",
    **{"ciscoContentNetworkMIB": ciscoContentNetworkMIB,
       "ciscoContentNetworkMIBObjects": ciscoContentNetworkMIBObjects,
       "ccnReport": ccnReport,
       "ccnReportDns": ccnReportDns,
       "ccnReportDnsRequestRate": ccnReportDnsRequestRate,
       "ccnReportDnsClientCount": ccnReportDnsClientCount,
       "ccnReportDnsRequests": ccnReportDnsRequests,
       "ccnReportAcct": ccnReportAcct,
       "ccnReportAcctBytesServed": ccnReportAcctBytesServed,
       "ccnReportAcctObjectsCached": ccnReportAcctObjectsCached,
       "ccnReportAcctCacheHitRate": ccnReportAcctCacheHitRate,
       "ccnReportAcctCacheMissRate": ccnReportAcctCacheMissRate,
       "ciscoContentNetworkMIBNotif": ciscoContentNetworkMIBNotif,
       "ccnNotifications": ccnNotifications,
       "ccnNotifServerStart": ccnNotifServerStart,
       "ccnNotifServerStop": ccnNotifServerStop,
       "ccnNotifOffline": ccnNotifOffline,
       "ccnNotifNeedsAttention": ccnNotifNeedsAttention,
       "ccnNotifWaitingForCdm": ccnNotifWaitingForCdm,
       "ccnNotifOnline": ccnNotifOnline,
       "ccnMIBConformance": ccnMIBConformance,
       "ccnMIBCompliances": ccnMIBCompliances,
       "ccnMIBCompliance": ccnMIBCompliance,
       "ccnMIBComplianceRev1": ccnMIBComplianceRev1,
       "ccnMIBGroups": ccnMIBGroups,
       "ccnReportingGroup": ccnReportingGroup,
       "ccnNotifGroup": ccnNotifGroup,
       "ccnNotifGroupRev1": ccnNotifGroupRev1}
)
