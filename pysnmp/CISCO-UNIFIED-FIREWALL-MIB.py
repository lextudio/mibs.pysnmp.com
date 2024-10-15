# SNMP MIB module (CISCO-UNIFIED-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-FIREWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:32 2024
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

(dot1dTpFdbPort,
 dot1dTpFdbStatus) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dTpFdbPort",
    "dot1dTpFdbStatus")

(CFWApplicationProtocol,
 CFWNetworkProtocol,
 CFWPolicy,
 CFWPolicyTarget,
 CFWPolicyTargetType,
 CFWUrlServerStatus,
 CFWUrlfVendorId) = mibBuilder.importSymbols(
    "CISCO-FIREWALL-TC",
    "CFWApplicationProtocol",
    "CFWNetworkProtocol",
    "CFWPolicy",
    "CFWPolicyTarget",
    "CFWPolicyTargetType",
    "CFWUrlServerStatus",
    "CFWUrlfVendorId")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoUnifiedFirewallMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491)
)
ciscoUnifiedFirewallMIB.setRevisions(
        ("2005-09-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoUnifiedFirewallMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoUnifiedFirewallMIBNotifs = _CiscoUnifiedFirewallMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 0)
)
_CiscoUnifiedFirewallMIBObjects_ObjectIdentity = ObjectIdentity
ciscoUnifiedFirewallMIBObjects = _CiscoUnifiedFirewallMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1)
)
_CuFwConnectionGrp_ObjectIdentity = ObjectIdentity
cuFwConnectionGrp = _CuFwConnectionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1)
)
_CuFwConnectionGlobals_ObjectIdentity = ObjectIdentity
cuFwConnectionGlobals = _CuFwConnectionGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1)
)
_CufwConnGlobalNumAttempted_Type = Counter64
_CufwConnGlobalNumAttempted_Object = MibScalar
cufwConnGlobalNumAttempted = _CufwConnGlobalNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 1),
    _CufwConnGlobalNumAttempted_Type()
)
cufwConnGlobalNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumAttempted.setUnits("Connections")
_CufwConnGlobalNumSetupsAborted_Type = Counter64
_CufwConnGlobalNumSetupsAborted_Object = MibScalar
cufwConnGlobalNumSetupsAborted = _CufwConnGlobalNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 2),
    _CufwConnGlobalNumSetupsAborted_Type()
)
cufwConnGlobalNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumSetupsAborted.setUnits("Connections")
_CufwConnGlobalNumPolicyDeclined_Type = Counter64
_CufwConnGlobalNumPolicyDeclined_Object = MibScalar
cufwConnGlobalNumPolicyDeclined = _CufwConnGlobalNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 3),
    _CufwConnGlobalNumPolicyDeclined_Type()
)
cufwConnGlobalNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumPolicyDeclined.setUnits("Connections")
_CufwConnGlobalNumResDeclined_Type = Counter64
_CufwConnGlobalNumResDeclined_Object = MibScalar
cufwConnGlobalNumResDeclined = _CufwConnGlobalNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 4),
    _CufwConnGlobalNumResDeclined_Type()
)
cufwConnGlobalNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumResDeclined.setUnits("Connections")
_CufwConnGlobalNumHalfOpen_Type = Gauge32
_CufwConnGlobalNumHalfOpen_Object = MibScalar
cufwConnGlobalNumHalfOpen = _CufwConnGlobalNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 5),
    _CufwConnGlobalNumHalfOpen_Type()
)
cufwConnGlobalNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumHalfOpen.setUnits("Connections")
_CufwConnGlobalNumActive_Type = Gauge32
_CufwConnGlobalNumActive_Object = MibScalar
cufwConnGlobalNumActive = _CufwConnGlobalNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 6),
    _CufwConnGlobalNumActive_Type()
)
cufwConnGlobalNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumActive.setUnits("Connections")
_CufwConnGlobalNumExpired_Type = Counter64
_CufwConnGlobalNumExpired_Object = MibScalar
cufwConnGlobalNumExpired = _CufwConnGlobalNumExpired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 7),
    _CufwConnGlobalNumExpired_Type()
)
cufwConnGlobalNumExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumExpired.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumExpired.setUnits("Connections")
_CufwConnGlobalNumAborted_Type = Counter64
_CufwConnGlobalNumAborted_Object = MibScalar
cufwConnGlobalNumAborted = _CufwConnGlobalNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 8),
    _CufwConnGlobalNumAborted_Type()
)
cufwConnGlobalNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumAborted.setUnits("Connections")
_CufwConnGlobalNumEmbryonic_Type = Gauge32
_CufwConnGlobalNumEmbryonic_Object = MibScalar
cufwConnGlobalNumEmbryonic = _CufwConnGlobalNumEmbryonic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 9),
    _CufwConnGlobalNumEmbryonic_Type()
)
cufwConnGlobalNumEmbryonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumEmbryonic.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumEmbryonic.setUnits("Connections")
_CufwConnGlobalConnSetupRate1_Type = Gauge32
_CufwConnGlobalConnSetupRate1_Object = MibScalar
cufwConnGlobalConnSetupRate1 = _CufwConnGlobalConnSetupRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 10),
    _CufwConnGlobalConnSetupRate1_Type()
)
cufwConnGlobalConnSetupRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalConnSetupRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalConnSetupRate1.setUnits("Connections per second")
_CufwConnGlobalConnSetupRate5_Type = Gauge32
_CufwConnGlobalConnSetupRate5_Object = MibScalar
cufwConnGlobalConnSetupRate5 = _CufwConnGlobalConnSetupRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 11),
    _CufwConnGlobalConnSetupRate5_Type()
)
cufwConnGlobalConnSetupRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalConnSetupRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalConnSetupRate5.setUnits("Connections per second")
_CufwConnGlobalNumRemoteAccess_Type = Gauge32
_CufwConnGlobalNumRemoteAccess_Object = MibScalar
cufwConnGlobalNumRemoteAccess = _CufwConnGlobalNumRemoteAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 1, 12),
    _CufwConnGlobalNumRemoteAccess_Type()
)
cufwConnGlobalNumRemoteAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnGlobalNumRemoteAccess.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnGlobalNumRemoteAccess.setUnits("Connections")
_CuFwConnectionResources_ObjectIdentity = ObjectIdentity
cuFwConnectionResources = _CuFwConnectionResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2)
)
_CufwConnResMemoryUsage_Type = Gauge32
_CufwConnResMemoryUsage_Object = MibScalar
cufwConnResMemoryUsage = _CufwConnResMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2, 1),
    _CufwConnResMemoryUsage_Type()
)
cufwConnResMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnResMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnResMemoryUsage.setUnits("KBytes")
_CufwConnResActiveConnMemoryUsage_Type = Gauge32
_CufwConnResActiveConnMemoryUsage_Object = MibScalar
cufwConnResActiveConnMemoryUsage = _CufwConnResActiveConnMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2, 2),
    _CufwConnResActiveConnMemoryUsage_Type()
)
cufwConnResActiveConnMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnResActiveConnMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnResActiveConnMemoryUsage.setUnits("KBytes")
_CufwConnResHOConnMemoryUsage_Type = Gauge32
_CufwConnResHOConnMemoryUsage_Object = MibScalar
cufwConnResHOConnMemoryUsage = _CufwConnResHOConnMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2, 3),
    _CufwConnResHOConnMemoryUsage_Type()
)
cufwConnResHOConnMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnResHOConnMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnResHOConnMemoryUsage.setUnits("KBytes")
_CufwConnResEmbrConnMemoryUsage_Type = Gauge32
_CufwConnResEmbrConnMemoryUsage_Object = MibScalar
cufwConnResEmbrConnMemoryUsage = _CufwConnResEmbrConnMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 2, 4),
    _CufwConnResEmbrConnMemoryUsage_Type()
)
cufwConnResEmbrConnMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnResEmbrConnMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnResEmbrConnMemoryUsage.setUnits("KBytes")
_CuFwConnectionReportSettings_ObjectIdentity = ObjectIdentity
cuFwConnectionReportSettings = _CuFwConnectionReportSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 3)
)


class _CufwConnReptAppStats_Type(TruthValue):
    """Custom type cufwConnReptAppStats based on TruthValue"""


_CufwConnReptAppStats_Object = MibScalar
cufwConnReptAppStats = _CufwConnReptAppStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 3, 1),
    _CufwConnReptAppStats_Type()
)
cufwConnReptAppStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwConnReptAppStats.setStatus("current")
_CufwConnReptAppStatsLastChanged_Type = TimeStamp
_CufwConnReptAppStatsLastChanged_Object = MibScalar
cufwConnReptAppStatsLastChanged = _CufwConnReptAppStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 3, 2),
    _CufwConnReptAppStatsLastChanged_Type()
)
cufwConnReptAppStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnReptAppStatsLastChanged.setStatus("current")
_CuFwConnectionSummaryTables_ObjectIdentity = ObjectIdentity
cuFwConnectionSummaryTables = _CuFwConnectionSummaryTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4)
)
_CufwConnSummaryTable_Object = MibTable
cufwConnSummaryTable = _CufwConnSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cufwConnSummaryTable.setStatus("current")
_CufwConnSummaryEntry_Object = MibTableRow
cufwConnSummaryEntry = _CufwConnSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1)
)
cufwConnSummaryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwConnProtocol"),
)
if mibBuilder.loadTexts:
    cufwConnSummaryEntry.setStatus("current")
_CufwConnProtocol_Type = CFWNetworkProtocol
_CufwConnProtocol_Object = MibTableColumn
cufwConnProtocol = _CufwConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 1),
    _CufwConnProtocol_Type()
)
cufwConnProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwConnProtocol.setStatus("current")
_CufwConnNumAttempted_Type = Counter64
_CufwConnNumAttempted_Object = MibTableColumn
cufwConnNumAttempted = _CufwConnNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 2),
    _CufwConnNumAttempted_Type()
)
cufwConnNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumAttempted.setUnits("Connections")
_CufwConnNumSetupsAborted_Type = Counter64
_CufwConnNumSetupsAborted_Object = MibTableColumn
cufwConnNumSetupsAborted = _CufwConnNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 3),
    _CufwConnNumSetupsAborted_Type()
)
cufwConnNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumSetupsAborted.setUnits("Connections")
_CufwConnNumPolicyDeclined_Type = Counter64
_CufwConnNumPolicyDeclined_Object = MibTableColumn
cufwConnNumPolicyDeclined = _CufwConnNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 4),
    _CufwConnNumPolicyDeclined_Type()
)
cufwConnNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumPolicyDeclined.setUnits("Connections")
_CufwConnNumResDeclined_Type = Counter64
_CufwConnNumResDeclined_Object = MibTableColumn
cufwConnNumResDeclined = _CufwConnNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 5),
    _CufwConnNumResDeclined_Type()
)
cufwConnNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumResDeclined.setUnits("Connections")
_CufwConnNumHalfOpen_Type = Gauge32
_CufwConnNumHalfOpen_Object = MibTableColumn
cufwConnNumHalfOpen = _CufwConnNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 6),
    _CufwConnNumHalfOpen_Type()
)
cufwConnNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumHalfOpen.setUnits("Connections")
_CufwConnNumActive_Type = Gauge32
_CufwConnNumActive_Object = MibTableColumn
cufwConnNumActive = _CufwConnNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 7),
    _CufwConnNumActive_Type()
)
cufwConnNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumActive.setUnits("Connections")
_CufwConnNumAborted_Type = Counter64
_CufwConnNumAborted_Object = MibTableColumn
cufwConnNumAborted = _CufwConnNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 8),
    _CufwConnNumAborted_Type()
)
cufwConnNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnNumAborted.setUnits("Connections")
_CufwConnSetupRate1_Type = Gauge32
_CufwConnSetupRate1_Object = MibTableColumn
cufwConnSetupRate1 = _CufwConnSetupRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 9),
    _CufwConnSetupRate1_Type()
)
cufwConnSetupRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnSetupRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnSetupRate1.setUnits("Connections Per Second")
_CufwConnSetupRate5_Type = Gauge32
_CufwConnSetupRate5_Object = MibTableColumn
cufwConnSetupRate5 = _CufwConnSetupRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 1, 1, 10),
    _CufwConnSetupRate5_Type()
)
cufwConnSetupRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwConnSetupRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwConnSetupRate5.setUnits("Connections Per Second")
_CufwAppConnSummaryTable_Object = MibTable
cufwAppConnSummaryTable = _CufwAppConnSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cufwAppConnSummaryTable.setStatus("current")
_CufwAppConnSummaryEntry_Object = MibTableRow
cufwAppConnSummaryEntry = _CufwAppConnSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1)
)
cufwAppConnSummaryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnProtocol"),
)
if mibBuilder.loadTexts:
    cufwAppConnSummaryEntry.setStatus("current")
_CufwAppConnProtocol_Type = CFWApplicationProtocol
_CufwAppConnProtocol_Object = MibTableColumn
cufwAppConnProtocol = _CufwAppConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 1),
    _CufwAppConnProtocol_Type()
)
cufwAppConnProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwAppConnProtocol.setStatus("current")
_CufwAppConnNumAttempted_Type = Counter64
_CufwAppConnNumAttempted_Object = MibTableColumn
cufwAppConnNumAttempted = _CufwAppConnNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 2),
    _CufwAppConnNumAttempted_Type()
)
cufwAppConnNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumAttempted.setUnits("Connections")
_CufwAppConnNumSetupsAborted_Type = Counter64
_CufwAppConnNumSetupsAborted_Object = MibTableColumn
cufwAppConnNumSetupsAborted = _CufwAppConnNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 3),
    _CufwAppConnNumSetupsAborted_Type()
)
cufwAppConnNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumSetupsAborted.setUnits("Connections")
_CufwAppConnNumPolicyDeclined_Type = Counter64
_CufwAppConnNumPolicyDeclined_Object = MibTableColumn
cufwAppConnNumPolicyDeclined = _CufwAppConnNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 4),
    _CufwAppConnNumPolicyDeclined_Type()
)
cufwAppConnNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumPolicyDeclined.setUnits("Connections")
_CufwAppConnNumResDeclined_Type = Counter64
_CufwAppConnNumResDeclined_Object = MibTableColumn
cufwAppConnNumResDeclined = _CufwAppConnNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 5),
    _CufwAppConnNumResDeclined_Type()
)
cufwAppConnNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumResDeclined.setUnits("Connections")
_CufwAppConnNumHalfOpen_Type = Gauge32
_CufwAppConnNumHalfOpen_Object = MibTableColumn
cufwAppConnNumHalfOpen = _CufwAppConnNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 6),
    _CufwAppConnNumHalfOpen_Type()
)
cufwAppConnNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumHalfOpen.setUnits("Connections")
_CufwAppConnNumActive_Type = Gauge32
_CufwAppConnNumActive_Object = MibTableColumn
cufwAppConnNumActive = _CufwAppConnNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 7),
    _CufwAppConnNumActive_Type()
)
cufwAppConnNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumActive.setUnits("Connections")
_CufwAppConnNumAborted_Type = Counter64
_CufwAppConnNumAborted_Object = MibTableColumn
cufwAppConnNumAborted = _CufwAppConnNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 8),
    _CufwAppConnNumAborted_Type()
)
cufwAppConnNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnNumAborted.setUnits("Connections")
_CufwAppConnSetupRate1_Type = Gauge32
_CufwAppConnSetupRate1_Object = MibTableColumn
cufwAppConnSetupRate1 = _CufwAppConnSetupRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 9),
    _CufwAppConnSetupRate1_Type()
)
cufwAppConnSetupRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnSetupRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnSetupRate1.setUnits("Connections Per Second")
_CufwAppConnSetupRate5_Type = Gauge32
_CufwAppConnSetupRate5_Object = MibTableColumn
cufwAppConnSetupRate5 = _CufwAppConnSetupRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 2, 1, 10),
    _CufwAppConnSetupRate5_Type()
)
cufwAppConnSetupRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAppConnSetupRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwAppConnSetupRate5.setUnits("Connections Per Second")
_CufwPolicyConnSummaryTable_Object = MibTable
cufwPolicyConnSummaryTable = _CufwPolicyConnSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cufwPolicyConnSummaryTable.setStatus("current")
_CufwPolicyConnSummaryEntry_Object = MibTableRow
cufwPolicyConnSummaryEntry = _CufwPolicyConnSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1)
)
cufwPolicyConnSummaryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnPolicy"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnPolicyTargetType"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnPolicyTarget"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnProtocol"),
)
if mibBuilder.loadTexts:
    cufwPolicyConnSummaryEntry.setStatus("current")
_CufwPolConnPolicy_Type = CFWPolicy
_CufwPolConnPolicy_Object = MibTableColumn
cufwPolConnPolicy = _CufwPolConnPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 1),
    _CufwPolConnPolicy_Type()
)
cufwPolConnPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolConnPolicy.setStatus("current")
_CufwPolConnPolicyTargetType_Type = CFWPolicyTargetType
_CufwPolConnPolicyTargetType_Object = MibTableColumn
cufwPolConnPolicyTargetType = _CufwPolConnPolicyTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 2),
    _CufwPolConnPolicyTargetType_Type()
)
cufwPolConnPolicyTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolConnPolicyTargetType.setStatus("current")


class _CufwPolConnPolicyTarget_Type(CFWPolicyTarget):
    """Custom type cufwPolConnPolicyTarget based on CFWPolicyTarget"""
    subtypeSpec = CFWPolicyTarget.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CufwPolConnPolicyTarget_Type.__name__ = "CFWPolicyTarget"
_CufwPolConnPolicyTarget_Object = MibTableColumn
cufwPolConnPolicyTarget = _CufwPolConnPolicyTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 3),
    _CufwPolConnPolicyTarget_Type()
)
cufwPolConnPolicyTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolConnPolicyTarget.setStatus("current")
_CufwPolConnProtocol_Type = CFWNetworkProtocol
_CufwPolConnProtocol_Object = MibTableColumn
cufwPolConnProtocol = _CufwPolConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 4),
    _CufwPolConnProtocol_Type()
)
cufwPolConnProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolConnProtocol.setStatus("current")
_CufwPolConnNumAttempted_Type = Counter64
_CufwPolConnNumAttempted_Object = MibTableColumn
cufwPolConnNumAttempted = _CufwPolConnNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 5),
    _CufwPolConnNumAttempted_Type()
)
cufwPolConnNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumAttempted.setUnits("Connections")
_CufwPolConnNumSetupsAborted_Type = Counter64
_CufwPolConnNumSetupsAborted_Object = MibTableColumn
cufwPolConnNumSetupsAborted = _CufwPolConnNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 6),
    _CufwPolConnNumSetupsAborted_Type()
)
cufwPolConnNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumSetupsAborted.setUnits("Connections")
_CufwPolConnNumPolicyDeclined_Type = Counter64
_CufwPolConnNumPolicyDeclined_Object = MibTableColumn
cufwPolConnNumPolicyDeclined = _CufwPolConnNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 7),
    _CufwPolConnNumPolicyDeclined_Type()
)
cufwPolConnNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumPolicyDeclined.setUnits("Connections")
_CufwPolConnNumResDeclined_Type = Counter64
_CufwPolConnNumResDeclined_Object = MibTableColumn
cufwPolConnNumResDeclined = _CufwPolConnNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 8),
    _CufwPolConnNumResDeclined_Type()
)
cufwPolConnNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumResDeclined.setUnits("Connections")
_CufwPolConnNumHalfOpen_Type = Gauge32
_CufwPolConnNumHalfOpen_Object = MibTableColumn
cufwPolConnNumHalfOpen = _CufwPolConnNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 9),
    _CufwPolConnNumHalfOpen_Type()
)
cufwPolConnNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumHalfOpen.setUnits("Connections")
_CufwPolConnNumActive_Type = Gauge32
_CufwPolConnNumActive_Object = MibTableColumn
cufwPolConnNumActive = _CufwPolConnNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 10),
    _CufwPolConnNumActive_Type()
)
cufwPolConnNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumActive.setUnits("Connections")
_CufwPolConnNumAborted_Type = Counter64
_CufwPolConnNumAborted_Object = MibTableColumn
cufwPolConnNumAborted = _CufwPolConnNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 3, 1, 11),
    _CufwPolConnNumAborted_Type()
)
cufwPolConnNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolConnNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolConnNumAborted.setUnits("Connections")
_CufwPolicyAppConnSummaryTable_Object = MibTable
cufwPolicyAppConnSummaryTable = _CufwPolicyAppConnSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cufwPolicyAppConnSummaryTable.setStatus("current")
_CufwPolicyAppConnSummaryEntry_Object = MibTableRow
cufwPolicyAppConnSummaryEntry = _CufwPolicyAppConnSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1)
)
cufwPolicyAppConnSummaryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnPolicy"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnPolicyTargetType"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnPolicyTarget"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnProtocol"),
)
if mibBuilder.loadTexts:
    cufwPolicyAppConnSummaryEntry.setStatus("current")
_CufwPolAppConnPolicy_Type = CFWPolicy
_CufwPolAppConnPolicy_Object = MibTableColumn
cufwPolAppConnPolicy = _CufwPolAppConnPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 1),
    _CufwPolAppConnPolicy_Type()
)
cufwPolAppConnPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolAppConnPolicy.setStatus("current")
_CufwPolAppConnPolicyTargetType_Type = CFWPolicyTargetType
_CufwPolAppConnPolicyTargetType_Object = MibTableColumn
cufwPolAppConnPolicyTargetType = _CufwPolAppConnPolicyTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 2),
    _CufwPolAppConnPolicyTargetType_Type()
)
cufwPolAppConnPolicyTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolAppConnPolicyTargetType.setStatus("current")


class _CufwPolAppConnPolicyTarget_Type(CFWPolicyTarget):
    """Custom type cufwPolAppConnPolicyTarget based on CFWPolicyTarget"""
    subtypeSpec = CFWPolicyTarget.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CufwPolAppConnPolicyTarget_Type.__name__ = "CFWPolicyTarget"
_CufwPolAppConnPolicyTarget_Object = MibTableColumn
cufwPolAppConnPolicyTarget = _CufwPolAppConnPolicyTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 3),
    _CufwPolAppConnPolicyTarget_Type()
)
cufwPolAppConnPolicyTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolAppConnPolicyTarget.setStatus("current")
_CufwPolAppConnProtocol_Type = CFWApplicationProtocol
_CufwPolAppConnProtocol_Object = MibTableColumn
cufwPolAppConnProtocol = _CufwPolAppConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 4),
    _CufwPolAppConnProtocol_Type()
)
cufwPolAppConnProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwPolAppConnProtocol.setStatus("current")
_CufwPolAppConnNumAttempted_Type = Counter64
_CufwPolAppConnNumAttempted_Object = MibTableColumn
cufwPolAppConnNumAttempted = _CufwPolAppConnNumAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 5),
    _CufwPolAppConnNumAttempted_Type()
)
cufwPolAppConnNumAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumAttempted.setUnits("Connections")
_CufwPolAppConnNumSetupsAborted_Type = Counter64
_CufwPolAppConnNumSetupsAborted_Object = MibTableColumn
cufwPolAppConnNumSetupsAborted = _CufwPolAppConnNumSetupsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 6),
    _CufwPolAppConnNumSetupsAborted_Type()
)
cufwPolAppConnNumSetupsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumSetupsAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumSetupsAborted.setUnits("Connections")
_CufwPolAppConnNumPolicyDeclined_Type = Counter64
_CufwPolAppConnNumPolicyDeclined_Object = MibTableColumn
cufwPolAppConnNumPolicyDeclined = _CufwPolAppConnNumPolicyDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 7),
    _CufwPolAppConnNumPolicyDeclined_Type()
)
cufwPolAppConnNumPolicyDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumPolicyDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumPolicyDeclined.setUnits("Connections")
_CufwPolAppConnNumResDeclined_Type = Counter64
_CufwPolAppConnNumResDeclined_Object = MibTableColumn
cufwPolAppConnNumResDeclined = _CufwPolAppConnNumResDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 8),
    _CufwPolAppConnNumResDeclined_Type()
)
cufwPolAppConnNumResDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumResDeclined.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumResDeclined.setUnits("Connections")
_CufwPolAppConnNumHalfOpen_Type = Gauge32
_CufwPolAppConnNumHalfOpen_Object = MibTableColumn
cufwPolAppConnNumHalfOpen = _CufwPolAppConnNumHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 9),
    _CufwPolAppConnNumHalfOpen_Type()
)
cufwPolAppConnNumHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumHalfOpen.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumHalfOpen.setUnits("Connections")
_CufwPolAppConnNumActive_Type = Gauge32
_CufwPolAppConnNumActive_Object = MibTableColumn
cufwPolAppConnNumActive = _CufwPolAppConnNumActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 10),
    _CufwPolAppConnNumActive_Type()
)
cufwPolAppConnNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumActive.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumActive.setUnits("Connections")
_CufwPolAppConnNumAborted_Type = Counter64
_CufwPolAppConnNumAborted_Object = MibTableColumn
cufwPolAppConnNumAborted = _CufwPolAppConnNumAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 1, 4, 4, 1, 11),
    _CufwPolAppConnNumAborted_Type()
)
cufwPolAppConnNumAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwPolAppConnNumAborted.setStatus("current")
if mibBuilder.loadTexts:
    cufwPolAppConnNumAborted.setUnits("Connections")
_CuFwApplInspectionGrp_ObjectIdentity = ObjectIdentity
cuFwApplInspectionGrp = _CuFwApplInspectionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2)
)
_CufwAIAuditTrailEnabled_Type = TruthValue
_CufwAIAuditTrailEnabled_Object = MibScalar
cufwAIAuditTrailEnabled = _CufwAIAuditTrailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 1),
    _CufwAIAuditTrailEnabled_Type()
)
cufwAIAuditTrailEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwAIAuditTrailEnabled.setStatus("current")
_CufwAIAlertEnabled_Type = TruthValue
_CufwAIAlertEnabled_Object = MibScalar
cufwAIAlertEnabled = _CufwAIAlertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 2),
    _CufwAIAlertEnabled_Type()
)
cufwAIAlertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwAIAlertEnabled.setStatus("current")
_CufwInspectionTable_Object = MibTable
cufwInspectionTable = _CufwInspectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cufwInspectionTable.setStatus("current")
_CufwInspectionEntry_Object = MibTableRow
cufwInspectionEntry = _CufwInspectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3, 1)
)
cufwInspectionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwInspectionPolicyName"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwInspectionProtocol"),
)
if mibBuilder.loadTexts:
    cufwInspectionEntry.setStatus("current")


class _CufwInspectionPolicyName_Type(CFWPolicy):
    """Custom type cufwInspectionPolicyName based on CFWPolicy"""
    subtypeSpec = CFWPolicy.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CufwInspectionPolicyName_Type.__name__ = "CFWPolicy"
_CufwInspectionPolicyName_Object = MibTableColumn
cufwInspectionPolicyName = _CufwInspectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3, 1, 1),
    _CufwInspectionPolicyName_Type()
)
cufwInspectionPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwInspectionPolicyName.setStatus("current")
_CufwInspectionProtocol_Type = CFWApplicationProtocol
_CufwInspectionProtocol_Object = MibTableColumn
cufwInspectionProtocol = _CufwInspectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3, 1, 2),
    _CufwInspectionProtocol_Type()
)
cufwInspectionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwInspectionProtocol.setStatus("current")
_CufwInspectionStatus_Type = TruthValue
_CufwInspectionStatus_Object = MibTableColumn
cufwInspectionStatus = _CufwInspectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 2, 3, 1, 3),
    _CufwInspectionStatus_Type()
)
cufwInspectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwInspectionStatus.setStatus("current")
_CuFwUrlFilterGrp_ObjectIdentity = ObjectIdentity
cuFwUrlFilterGrp = _CuFwUrlFilterGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3)
)
_CufwUrlFilterGlobals_ObjectIdentity = ObjectIdentity
cufwUrlFilterGlobals = _CufwUrlFilterGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1)
)
_CufwUrlfFunctionEnabled_Type = TruthValue
_CufwUrlfFunctionEnabled_Object = MibScalar
cufwUrlfFunctionEnabled = _CufwUrlfFunctionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 1),
    _CufwUrlfFunctionEnabled_Type()
)
cufwUrlfFunctionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwUrlfFunctionEnabled.setStatus("current")
_CufwUrlfRequestsNumProcessed_Type = Counter64
_CufwUrlfRequestsNumProcessed_Object = MibScalar
cufwUrlfRequestsNumProcessed = _CufwUrlfRequestsNumProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 2),
    _CufwUrlfRequestsNumProcessed_Type()
)
cufwUrlfRequestsNumProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumProcessed.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumProcessed.setUnits("Requests")
_CufwUrlfRequestsProcRate1_Type = Gauge32
_CufwUrlfRequestsProcRate1_Object = MibScalar
cufwUrlfRequestsProcRate1 = _CufwUrlfRequestsProcRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 3),
    _CufwUrlfRequestsProcRate1_Type()
)
cufwUrlfRequestsProcRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsProcRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsProcRate1.setUnits("Requests per second")
_CufwUrlfRequestsProcRate5_Type = Gauge32
_CufwUrlfRequestsProcRate5_Object = MibScalar
cufwUrlfRequestsProcRate5 = _CufwUrlfRequestsProcRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 4),
    _CufwUrlfRequestsProcRate5_Type()
)
cufwUrlfRequestsProcRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsProcRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsProcRate5.setUnits("Requests per second")
_CufwUrlfRequestsNumAllowed_Type = Counter64
_CufwUrlfRequestsNumAllowed_Object = MibScalar
cufwUrlfRequestsNumAllowed = _CufwUrlfRequestsNumAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 5),
    _CufwUrlfRequestsNumAllowed_Type()
)
cufwUrlfRequestsNumAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumAllowed.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumAllowed.setUnits("Requests")
_CufwUrlfRequestsNumDenied_Type = Counter64
_CufwUrlfRequestsNumDenied_Object = MibScalar
cufwUrlfRequestsNumDenied = _CufwUrlfRequestsNumDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 6),
    _CufwUrlfRequestsNumDenied_Type()
)
cufwUrlfRequestsNumDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumDenied.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumDenied.setUnits("Requests")
_CufwUrlfRequestsDeniedRate1_Type = Gauge32
_CufwUrlfRequestsDeniedRate1_Object = MibScalar
cufwUrlfRequestsDeniedRate1 = _CufwUrlfRequestsDeniedRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 7),
    _CufwUrlfRequestsDeniedRate1_Type()
)
cufwUrlfRequestsDeniedRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsDeniedRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsDeniedRate1.setUnits("Requests per second")
_CufwUrlfRequestsDeniedRate5_Type = Gauge32
_CufwUrlfRequestsDeniedRate5_Object = MibScalar
cufwUrlfRequestsDeniedRate5 = _CufwUrlfRequestsDeniedRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 8),
    _CufwUrlfRequestsDeniedRate5_Type()
)
cufwUrlfRequestsDeniedRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsDeniedRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsDeniedRate5.setUnits("Requests Per Second")
_CufwUrlfRequestsNumCacheAllowed_Type = Counter64
_CufwUrlfRequestsNumCacheAllowed_Object = MibScalar
cufwUrlfRequestsNumCacheAllowed = _CufwUrlfRequestsNumCacheAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 9),
    _CufwUrlfRequestsNumCacheAllowed_Type()
)
cufwUrlfRequestsNumCacheAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumCacheAllowed.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumCacheAllowed.setUnits("Requests")
_CufwUrlfRequestsNumCacheDenied_Type = Counter64
_CufwUrlfRequestsNumCacheDenied_Object = MibScalar
cufwUrlfRequestsNumCacheDenied = _CufwUrlfRequestsNumCacheDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 10),
    _CufwUrlfRequestsNumCacheDenied_Type()
)
cufwUrlfRequestsNumCacheDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumCacheDenied.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumCacheDenied.setUnits("Requests")
_CufwUrlfAllowModeReqNumAllowed_Type = Counter64
_CufwUrlfAllowModeReqNumAllowed_Object = MibScalar
cufwUrlfAllowModeReqNumAllowed = _CufwUrlfAllowModeReqNumAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 11),
    _CufwUrlfAllowModeReqNumAllowed_Type()
)
cufwUrlfAllowModeReqNumAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfAllowModeReqNumAllowed.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfAllowModeReqNumAllowed.setUnits("Requests")
_CufwUrlfAllowModeReqNumDenied_Type = Counter64
_CufwUrlfAllowModeReqNumDenied_Object = MibScalar
cufwUrlfAllowModeReqNumDenied = _CufwUrlfAllowModeReqNumDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 12),
    _CufwUrlfAllowModeReqNumDenied_Type()
)
cufwUrlfAllowModeReqNumDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfAllowModeReqNumDenied.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfAllowModeReqNumDenied.setUnits("Requests")
_CufwUrlfRequestsNumResDropped_Type = Counter64
_CufwUrlfRequestsNumResDropped_Object = MibScalar
cufwUrlfRequestsNumResDropped = _CufwUrlfRequestsNumResDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 13),
    _CufwUrlfRequestsNumResDropped_Type()
)
cufwUrlfRequestsNumResDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumResDropped.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsNumResDropped.setUnits("Requests")
_CufwUrlfRequestsResDropRate1_Type = Gauge32
_CufwUrlfRequestsResDropRate1_Object = MibScalar
cufwUrlfRequestsResDropRate1 = _CufwUrlfRequestsResDropRate1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 14),
    _CufwUrlfRequestsResDropRate1_Type()
)
cufwUrlfRequestsResDropRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsResDropRate1.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsResDropRate1.setUnits("Requests Per Second")
_CufwUrlfRequestsResDropRate5_Type = Gauge32
_CufwUrlfRequestsResDropRate5_Object = MibScalar
cufwUrlfRequestsResDropRate5 = _CufwUrlfRequestsResDropRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 15),
    _CufwUrlfRequestsResDropRate5_Type()
)
cufwUrlfRequestsResDropRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfRequestsResDropRate5.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfRequestsResDropRate5.setUnits("Requests Per Second")
_CufwUrlfNumServerTimeouts_Type = Counter64
_CufwUrlfNumServerTimeouts_Object = MibScalar
cufwUrlfNumServerTimeouts = _CufwUrlfNumServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 16),
    _CufwUrlfNumServerTimeouts_Type()
)
cufwUrlfNumServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfNumServerTimeouts.setStatus("current")
_CufwUrlfNumServerRetries_Type = Counter64
_CufwUrlfNumServerRetries_Object = MibScalar
cufwUrlfNumServerRetries = _CufwUrlfNumServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 17),
    _CufwUrlfNumServerRetries_Type()
)
cufwUrlfNumServerRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfNumServerRetries.setStatus("current")
_CufwUrlfResponsesNumLate_Type = Counter64
_CufwUrlfResponsesNumLate_Object = MibScalar
cufwUrlfResponsesNumLate = _CufwUrlfResponsesNumLate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 18),
    _CufwUrlfResponsesNumLate_Type()
)
cufwUrlfResponsesNumLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfResponsesNumLate.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfResponsesNumLate.setUnits("Responses")
_CufwUrlfUrlAccRespsNumResDropped_Type = Counter64
_CufwUrlfUrlAccRespsNumResDropped_Object = MibScalar
cufwUrlfUrlAccRespsNumResDropped = _CufwUrlfUrlAccRespsNumResDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 1, 19),
    _CufwUrlfUrlAccRespsNumResDropped_Type()
)
cufwUrlfUrlAccRespsNumResDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfUrlAccRespsNumResDropped.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfUrlAccRespsNumResDropped.setUnits("Responses")
_CufwUrlFilterResourceUsage_ObjectIdentity = ObjectIdentity
cufwUrlFilterResourceUsage = _CufwUrlFilterResourceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 2)
)
_CufwUrlfResTotalRequestCacheSize_Type = Gauge32
_CufwUrlfResTotalRequestCacheSize_Object = MibScalar
cufwUrlfResTotalRequestCacheSize = _CufwUrlfResTotalRequestCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 2, 1),
    _CufwUrlfResTotalRequestCacheSize_Type()
)
cufwUrlfResTotalRequestCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfResTotalRequestCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfResTotalRequestCacheSize.setUnits("KBytes")
_CufwUrlfResTotalRespCacheSize_Type = Gauge32
_CufwUrlfResTotalRespCacheSize_Object = MibScalar
cufwUrlfResTotalRespCacheSize = _CufwUrlfResTotalRespCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 2, 2),
    _CufwUrlfResTotalRespCacheSize_Type()
)
cufwUrlfResTotalRespCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfResTotalRespCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfResTotalRespCacheSize.setUnits("KBytes")
_CufwUrlFilterServers_ObjectIdentity = ObjectIdentity
cufwUrlFilterServers = _CufwUrlFilterServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3)
)
_CufwUrlfServerTable_Object = MibTable
cufwUrlfServerTable = _CufwUrlfServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cufwUrlfServerTable.setStatus("current")
_CufwUrlfServerEntry_Object = MibTableRow
cufwUrlfServerEntry = _CufwUrlfServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1)
)
cufwUrlfServerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerAddrType"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerAddress"),
    (0, "CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerPort"),
)
if mibBuilder.loadTexts:
    cufwUrlfServerEntry.setStatus("current")
_CufwUrlfServerAddrType_Type = InetAddressType
_CufwUrlfServerAddrType_Object = MibTableColumn
cufwUrlfServerAddrType = _CufwUrlfServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 1),
    _CufwUrlfServerAddrType_Type()
)
cufwUrlfServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwUrlfServerAddrType.setStatus("current")
_CufwUrlfServerAddress_Type = InetAddress
_CufwUrlfServerAddress_Object = MibTableColumn
cufwUrlfServerAddress = _CufwUrlfServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 2),
    _CufwUrlfServerAddress_Type()
)
cufwUrlfServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwUrlfServerAddress.setStatus("current")
_CufwUrlfServerPort_Type = InetPortNumber
_CufwUrlfServerPort_Object = MibTableColumn
cufwUrlfServerPort = _CufwUrlfServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 3),
    _CufwUrlfServerPort_Type()
)
cufwUrlfServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cufwUrlfServerPort.setStatus("current")
_CufwUrlfServerVendor_Type = CFWUrlfVendorId
_CufwUrlfServerVendor_Object = MibTableColumn
cufwUrlfServerVendor = _CufwUrlfServerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 4),
    _CufwUrlfServerVendor_Type()
)
cufwUrlfServerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerVendor.setStatus("current")
_CufwUrlfServerStatus_Type = CFWUrlServerStatus
_CufwUrlfServerStatus_Object = MibTableColumn
cufwUrlfServerStatus = _CufwUrlfServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 5),
    _CufwUrlfServerStatus_Type()
)
cufwUrlfServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerStatus.setStatus("current")
_CufwUrlfServerReqsNumProcessed_Type = Counter64
_CufwUrlfServerReqsNumProcessed_Object = MibTableColumn
cufwUrlfServerReqsNumProcessed = _CufwUrlfServerReqsNumProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 6),
    _CufwUrlfServerReqsNumProcessed_Type()
)
cufwUrlfServerReqsNumProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerReqsNumProcessed.setStatus("current")
_CufwUrlfServerReqsNumAllowed_Type = Counter64
_CufwUrlfServerReqsNumAllowed_Object = MibTableColumn
cufwUrlfServerReqsNumAllowed = _CufwUrlfServerReqsNumAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 7),
    _CufwUrlfServerReqsNumAllowed_Type()
)
cufwUrlfServerReqsNumAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerReqsNumAllowed.setStatus("current")
_CufwUrlfServerReqsNumDenied_Type = Counter64
_CufwUrlfServerReqsNumDenied_Object = MibTableColumn
cufwUrlfServerReqsNumDenied = _CufwUrlfServerReqsNumDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 8),
    _CufwUrlfServerReqsNumDenied_Type()
)
cufwUrlfServerReqsNumDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerReqsNumDenied.setStatus("current")
_CufwUrlfServerNumTimeouts_Type = Counter64
_CufwUrlfServerNumTimeouts_Object = MibTableColumn
cufwUrlfServerNumTimeouts = _CufwUrlfServerNumTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 9),
    _CufwUrlfServerNumTimeouts_Type()
)
cufwUrlfServerNumTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerNumTimeouts.setStatus("current")
_CufwUrlfServerNumRetries_Type = Counter64
_CufwUrlfServerNumRetries_Object = MibTableColumn
cufwUrlfServerNumRetries = _CufwUrlfServerNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 10),
    _CufwUrlfServerNumRetries_Type()
)
cufwUrlfServerNumRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerNumRetries.setStatus("current")
_CufwUrlfServerRespsNumReceived_Type = Counter64
_CufwUrlfServerRespsNumReceived_Object = MibTableColumn
cufwUrlfServerRespsNumReceived = _CufwUrlfServerRespsNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 11),
    _CufwUrlfServerRespsNumReceived_Type()
)
cufwUrlfServerRespsNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerRespsNumReceived.setStatus("current")
_CufwUrlfServerRespsNumLate_Type = Counter64
_CufwUrlfServerRespsNumLate_Object = MibTableColumn
cufwUrlfServerRespsNumLate = _CufwUrlfServerRespsNumLate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 12),
    _CufwUrlfServerRespsNumLate_Type()
)
cufwUrlfServerRespsNumLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerRespsNumLate.setStatus("current")
_CufwUrlfServerAvgRespTime1_Type = Gauge32
_CufwUrlfServerAvgRespTime1_Object = MibTableColumn
cufwUrlfServerAvgRespTime1 = _CufwUrlfServerAvgRespTime1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 13),
    _CufwUrlfServerAvgRespTime1_Type()
)
cufwUrlfServerAvgRespTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerAvgRespTime1.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfServerAvgRespTime1.setUnits("seconds")
_CufwUrlfServerAvgRespTime5_Type = Gauge32
_CufwUrlfServerAvgRespTime5_Object = MibTableColumn
cufwUrlfServerAvgRespTime5 = _CufwUrlfServerAvgRespTime5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 3, 3, 1, 1, 14),
    _CufwUrlfServerAvgRespTime5_Type()
)
cufwUrlfServerAvgRespTime5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwUrlfServerAvgRespTime5.setStatus("current")
if mibBuilder.loadTexts:
    cufwUrlfServerAvgRespTime5.setUnits("seconds")
_CuFwFailoverGrp_ObjectIdentity = ObjectIdentity
cuFwFailoverGrp = _CuFwFailoverGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 4)
)
_CuFwAaicGrp_ObjectIdentity = ObjectIdentity
cuFwAaicGrp = _CuFwAaicGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5)
)
_CufwAaicGlobals_ObjectIdentity = ObjectIdentity
cufwAaicGlobals = _CufwAaicGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 1)
)
_CufwAaicGlobalNumBadProtocolOps_Type = Counter64
_CufwAaicGlobalNumBadProtocolOps_Object = MibScalar
cufwAaicGlobalNumBadProtocolOps = _CufwAaicGlobalNumBadProtocolOps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 1, 1),
    _CufwAaicGlobalNumBadProtocolOps_Type()
)
cufwAaicGlobalNumBadProtocolOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadProtocolOps.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadProtocolOps.setUnits("Protocol Data Units")
_CufwAaicGlobalNumBadPDUSize_Type = Counter64
_CufwAaicGlobalNumBadPDUSize_Object = MibScalar
cufwAaicGlobalNumBadPDUSize = _CufwAaicGlobalNumBadPDUSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 1, 2),
    _CufwAaicGlobalNumBadPDUSize_Type()
)
cufwAaicGlobalNumBadPDUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadPDUSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadPDUSize.setUnits("Protocol Data Units")
_CufwAaicGlobalNumBadPortRange_Type = Counter64
_CufwAaicGlobalNumBadPortRange_Object = MibScalar
cufwAaicGlobalNumBadPortRange = _CufwAaicGlobalNumBadPortRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 1, 3),
    _CufwAaicGlobalNumBadPortRange_Type()
)
cufwAaicGlobalNumBadPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadPortRange.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicGlobalNumBadPortRange.setUnits("Protocol Data Units")
_CufwAaicProtocolStats_ObjectIdentity = ObjectIdentity
cufwAaicProtocolStats = _CufwAaicProtocolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2)
)
_CufwAaicHttpProtocolStats_ObjectIdentity = ObjectIdentity
cufwAaicHttpProtocolStats = _CufwAaicHttpProtocolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1)
)
_CufwAaicHttpNumBadProtocolOps_Type = Counter64
_CufwAaicHttpNumBadProtocolOps_Object = MibScalar
cufwAaicHttpNumBadProtocolOps = _CufwAaicHttpNumBadProtocolOps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 1),
    _CufwAaicHttpNumBadProtocolOps_Type()
)
cufwAaicHttpNumBadProtocolOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadProtocolOps.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadProtocolOps.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumBadPDUSize_Type = Counter64
_CufwAaicHttpNumBadPDUSize_Object = MibScalar
cufwAaicHttpNumBadPDUSize = _CufwAaicHttpNumBadPDUSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 2),
    _CufwAaicHttpNumBadPDUSize_Type()
)
cufwAaicHttpNumBadPDUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadPDUSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadPDUSize.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumTunneledConns_Type = Counter64
_CufwAaicHttpNumTunneledConns_Object = MibScalar
cufwAaicHttpNumTunneledConns = _CufwAaicHttpNumTunneledConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 3),
    _CufwAaicHttpNumTunneledConns_Type()
)
cufwAaicHttpNumTunneledConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumTunneledConns.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumTunneledConns.setUnits("Connections")
_CufwAaicHttpNumLargeURIs_Type = Counter64
_CufwAaicHttpNumLargeURIs_Object = MibScalar
cufwAaicHttpNumLargeURIs = _CufwAaicHttpNumLargeURIs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 4),
    _CufwAaicHttpNumLargeURIs_Type()
)
cufwAaicHttpNumLargeURIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumLargeURIs.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumLargeURIs.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumBadContent_Type = Counter64
_CufwAaicHttpNumBadContent_Object = MibScalar
cufwAaicHttpNumBadContent = _CufwAaicHttpNumBadContent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 5),
    _CufwAaicHttpNumBadContent_Type()
)
cufwAaicHttpNumBadContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadContent.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumBadContent.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumMismatchContent_Type = Counter64
_CufwAaicHttpNumMismatchContent_Object = MibScalar
cufwAaicHttpNumMismatchContent = _CufwAaicHttpNumMismatchContent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 6),
    _CufwAaicHttpNumMismatchContent_Type()
)
cufwAaicHttpNumMismatchContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumMismatchContent.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumMismatchContent.setUnits("HTTP Protocol Data Units")
_CufwAaicHttpNumDoubleEncodedPkts_Type = Counter64
_CufwAaicHttpNumDoubleEncodedPkts_Object = MibScalar
cufwAaicHttpNumDoubleEncodedPkts = _CufwAaicHttpNumDoubleEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 5, 2, 1, 7),
    _CufwAaicHttpNumDoubleEncodedPkts_Type()
)
cufwAaicHttpNumDoubleEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwAaicHttpNumDoubleEncodedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cufwAaicHttpNumDoubleEncodedPkts.setUnits("HTTP Protocol Data Units")
_CuFwL2FwGrp_ObjectIdentity = ObjectIdentity
cuFwL2FwGrp = _CuFwL2FwGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6)
)
_CufwL2FwGlobals_ObjectIdentity = ObjectIdentity
cufwL2FwGlobals = _CufwL2FwGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1)
)
_CufwL2GlobalEnableStealthMode_Type = TruthValue
_CufwL2GlobalEnableStealthMode_Object = MibScalar
cufwL2GlobalEnableStealthMode = _CufwL2GlobalEnableStealthMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 1),
    _CufwL2GlobalEnableStealthMode_Type()
)
cufwL2GlobalEnableStealthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalEnableStealthMode.setStatus("current")


class _CufwL2GlobalArpCacheSize_Type(Integer32):
    """Custom type cufwL2GlobalArpCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CufwL2GlobalArpCacheSize_Type.__name__ = "Integer32"
_CufwL2GlobalArpCacheSize_Object = MibScalar
cufwL2GlobalArpCacheSize = _CufwL2GlobalArpCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 2),
    _CufwL2GlobalArpCacheSize_Type()
)
cufwL2GlobalArpCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalArpCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalArpCacheSize.setUnits("ARP entries")
_CufwL2GlobalEnableArpInspection_Type = TruthValue
_CufwL2GlobalEnableArpInspection_Object = MibScalar
cufwL2GlobalEnableArpInspection = _CufwL2GlobalEnableArpInspection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 3),
    _CufwL2GlobalEnableArpInspection_Type()
)
cufwL2GlobalEnableArpInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwL2GlobalEnableArpInspection.setStatus("current")
_CufwL2GlobalNumArpRequests_Type = Counter64
_CufwL2GlobalNumArpRequests_Object = MibScalar
cufwL2GlobalNumArpRequests = _CufwL2GlobalNumArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 5),
    _CufwL2GlobalNumArpRequests_Type()
)
cufwL2GlobalNumArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumArpRequests.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalNumArpRequests.setUnits("ARP Requests")
_CufwL2GlobalNumIcmpRequests_Type = Counter64
_CufwL2GlobalNumIcmpRequests_Object = MibScalar
cufwL2GlobalNumIcmpRequests = _CufwL2GlobalNumIcmpRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 6),
    _CufwL2GlobalNumIcmpRequests_Type()
)
cufwL2GlobalNumIcmpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumIcmpRequests.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalNumIcmpRequests.setUnits("ICMP Traceroute Requests")
_CufwL2GlobalNumFloods_Type = Counter64
_CufwL2GlobalNumFloods_Object = MibScalar
cufwL2GlobalNumFloods = _CufwL2GlobalNumFloods_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 7),
    _CufwL2GlobalNumFloods_Type()
)
cufwL2GlobalNumFloods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumFloods.setStatus("current")
_CufwL2GlobalNumDrops_Type = Counter64
_CufwL2GlobalNumDrops_Object = MibScalar
cufwL2GlobalNumDrops = _CufwL2GlobalNumDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 8),
    _CufwL2GlobalNumDrops_Type()
)
cufwL2GlobalNumDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumDrops.setStatus("current")
_CufwL2GlobalArpOverflowRate5_Type = Gauge32
_CufwL2GlobalArpOverflowRate5_Object = MibScalar
cufwL2GlobalArpOverflowRate5 = _CufwL2GlobalArpOverflowRate5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 9),
    _CufwL2GlobalArpOverflowRate5_Type()
)
cufwL2GlobalArpOverflowRate5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalArpOverflowRate5.setStatus("current")
_CufwL2GlobalNumBadArpResponses_Type = Counter64
_CufwL2GlobalNumBadArpResponses_Object = MibScalar
cufwL2GlobalNumBadArpResponses = _CufwL2GlobalNumBadArpResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 10),
    _CufwL2GlobalNumBadArpResponses_Type()
)
cufwL2GlobalNumBadArpResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumBadArpResponses.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalNumBadArpResponses.setUnits("ARP Responses")
_CufwL2GlobalNumSpoofedArpResps_Type = Counter64
_CufwL2GlobalNumSpoofedArpResps_Object = MibScalar
cufwL2GlobalNumSpoofedArpResps = _CufwL2GlobalNumSpoofedArpResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 6, 1, 11),
    _CufwL2GlobalNumSpoofedArpResps_Type()
)
cufwL2GlobalNumSpoofedArpResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cufwL2GlobalNumSpoofedArpResps.setStatus("current")
if mibBuilder.loadTexts:
    cufwL2GlobalNumSpoofedArpResps.setUnits("ARP Responses")
_CuFwNotifCntlGrp_ObjectIdentity = ObjectIdentity
cuFwNotifCntlGrp = _CuFwNotifCntlGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 7)
)


class _CufwCntlUrlfServerStatusChange_Type(TruthValue):
    """Custom type cufwCntlUrlfServerStatusChange based on TruthValue"""


_CufwCntlUrlfServerStatusChange_Object = MibScalar
cufwCntlUrlfServerStatusChange = _CufwCntlUrlfServerStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 7, 1),
    _CufwCntlUrlfServerStatusChange_Type()
)
cufwCntlUrlfServerStatusChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwCntlUrlfServerStatusChange.setStatus("current")


class _CufwCntlL2StaticMacAddressMoved_Type(TruthValue):
    """Custom type cufwCntlL2StaticMacAddressMoved based on TruthValue"""


_CufwCntlL2StaticMacAddressMoved_Object = MibScalar
cufwCntlL2StaticMacAddressMoved = _CufwCntlL2StaticMacAddressMoved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 1, 7, 2),
    _CufwCntlL2StaticMacAddressMoved_Type()
)
cufwCntlL2StaticMacAddressMoved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cufwCntlL2StaticMacAddressMoved.setStatus("current")
_CiscoUnifiedFirewallMIBConform_ObjectIdentity = ObjectIdentity
ciscoUnifiedFirewallMIBConform = _CiscoUnifiedFirewallMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2)
)
_CiscoUniFirewallMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoUniFirewallMIBCompliances = _CiscoUniFirewallMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 1)
)
_CiscoUniFirewallMIBGroups_ObjectIdentity = ObjectIdentity
ciscoUniFirewallMIBGroups = _CiscoUniFirewallMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2)
)

# Managed Objects groups

ciscoFwConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 1)
)
ciscoFwConnectionGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumExpired"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumEmbryonic"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalConnSetupRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalConnSetupRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnGlobalNumRemoteAccess"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnNumAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnSetupRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnSetupRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnNumAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnSetupRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAppConnSetupRate5"))
)
if mibBuilder.loadTexts:
    ciscoFwConnectionGroup.setStatus("current")

ciscoFwConnResourceUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 2)
)
ciscoFwConnResourceUsageGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnResMemoryUsage"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnResActiveConnMemoryUsage"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnResHOConnMemoryUsage"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnResEmbrConnMemoryUsage"))
)
if mibBuilder.loadTexts:
    ciscoFwConnResourceUsageGroup.setStatus("current")

ciscoFwPolicyConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 3)
)
ciscoFwPolicyConnectionGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolConnNumAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumAttempted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumSetupsAborted"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumPolicyDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumResDeclined"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumHalfOpen"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumActive"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwPolAppConnNumAborted"))
)
if mibBuilder.loadTexts:
    ciscoFwPolicyConnectionGroup.setStatus("current")

ciscoFwApplInspectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 4)
)
ciscoFwApplInspectionGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwAIAuditTrailEnabled"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAIAlertEnabled"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwInspectionStatus"))
)
if mibBuilder.loadTexts:
    ciscoFwApplInspectionGroup.setStatus("current")

ciscoFwUrlFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 5)
)
ciscoFwUrlFilterGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfFunctionEnabled"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumProcessed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsProcRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsProcRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumAllowed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumDenied"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsDeniedRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsDeniedRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumCacheAllowed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumCacheDenied"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfAllowModeReqNumAllowed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfAllowModeReqNumDenied"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsNumResDropped"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsResDropRate1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfRequestsResDropRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfNumServerTimeouts"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfNumServerRetries"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfResponsesNumLate"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfUrlAccRespsNumResDropped"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerVendor"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerStatus"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerReqsNumProcessed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerReqsNumAllowed"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerReqsNumDenied"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerNumTimeouts"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerNumRetries"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerRespsNumReceived"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerRespsNumLate"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerAvgRespTime1"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerAvgRespTime5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwCntlUrlfServerStatusChange"))
)
if mibBuilder.loadTexts:
    ciscoFwUrlFilterGroup.setStatus("current")

ciscoFwUrlFilterResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 6)
)
ciscoFwUrlFilterResourceGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfResTotalRequestCacheSize"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfResTotalRespCacheSize"))
)
if mibBuilder.loadTexts:
    ciscoFwUrlFilterResourceGroup.setStatus("current")

ciscoFwTransparentFwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 7)
)
ciscoFwTransparentFwGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalEnableStealthMode"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalArpCacheSize"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalEnableArpInspection"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumArpRequests"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumIcmpRequests"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumFloods"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumDrops"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalArpOverflowRate5"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumBadArpResponses"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwL2GlobalNumSpoofedArpResps"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwCntlL2StaticMacAddressMoved"))
)
if mibBuilder.loadTexts:
    ciscoFwTransparentFwGroup.setStatus("current")

ciscoFwBasicAaicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 10)
)
ciscoFwBasicAaicGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicGlobalNumBadProtocolOps"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicGlobalNumBadPDUSize"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicGlobalNumBadPortRange"))
)
if mibBuilder.loadTexts:
    ciscoFwBasicAaicGroup.setStatus("current")

ciscoFwAaicHttpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 11)
)
ciscoFwAaicHttpGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumBadProtocolOps"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumBadPDUSize"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumTunneledConns"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumLargeURIs"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumBadContent"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumMismatchContent"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwAaicHttpNumDoubleEncodedPkts"))
)
if mibBuilder.loadTexts:
    ciscoFwAaicHttpGroup.setStatus("current")

ciscoFwMibReportingControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 12)
)
ciscoFwMibReportingControlGroup.setObjects(
      *(("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnReptAppStats"),
        ("CISCO-UNIFIED-FIREWALL-MIB", "cufwConnReptAppStatsLastChanged"))
)
if mibBuilder.loadTexts:
    ciscoFwMibReportingControlGroup.setStatus("current")


# Notification objects

ciscoUFwUrlfServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 0, 1)
)
ciscoUFwUrlfServerStateChange.setObjects(
    ("CISCO-UNIFIED-FIREWALL-MIB", "cufwUrlfServerStatus")
)
if mibBuilder.loadTexts:
    ciscoUFwUrlfServerStateChange.setStatus(
        "current"
    )

ciscoUFwL2StaticMacAddressMoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 0, 2)
)
ciscoUFwL2StaticMacAddressMoved.setObjects(
      *(("BRIDGE-MIB", "dot1dTpFdbPort"),
        ("BRIDGE-MIB", "dot1dTpFdbStatus"))
)
if mibBuilder.loadTexts:
    ciscoUFwL2StaticMacAddressMoved.setStatus(
        "current"
    )


# Notifications groups

ciscoFwNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 8)
)
ciscoFwNotificationsGroup.setObjects(
    ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoUFwUrlfServerStateChange")
)
if mibBuilder.loadTexts:
    ciscoFwNotificationsGroup.setStatus(
        "current"
    )

ciscoFwTransparentNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 2, 9)
)
ciscoFwTransparentNotifGroup.setObjects(
    ("CISCO-UNIFIED-FIREWALL-MIB", "ciscoUFwL2StaticMacAddressMoved")
)
if mibBuilder.loadTexts:
    ciscoFwTransparentNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoUniFirewallMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 491, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoUniFirewallMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-FIREWALL-MIB",
    **{"ciscoUnifiedFirewallMIB": ciscoUnifiedFirewallMIB,
       "ciscoUnifiedFirewallMIBNotifs": ciscoUnifiedFirewallMIBNotifs,
       "ciscoUFwUrlfServerStateChange": ciscoUFwUrlfServerStateChange,
       "ciscoUFwL2StaticMacAddressMoved": ciscoUFwL2StaticMacAddressMoved,
       "ciscoUnifiedFirewallMIBObjects": ciscoUnifiedFirewallMIBObjects,
       "cuFwConnectionGrp": cuFwConnectionGrp,
       "cuFwConnectionGlobals": cuFwConnectionGlobals,
       "cufwConnGlobalNumAttempted": cufwConnGlobalNumAttempted,
       "cufwConnGlobalNumSetupsAborted": cufwConnGlobalNumSetupsAborted,
       "cufwConnGlobalNumPolicyDeclined": cufwConnGlobalNumPolicyDeclined,
       "cufwConnGlobalNumResDeclined": cufwConnGlobalNumResDeclined,
       "cufwConnGlobalNumHalfOpen": cufwConnGlobalNumHalfOpen,
       "cufwConnGlobalNumActive": cufwConnGlobalNumActive,
       "cufwConnGlobalNumExpired": cufwConnGlobalNumExpired,
       "cufwConnGlobalNumAborted": cufwConnGlobalNumAborted,
       "cufwConnGlobalNumEmbryonic": cufwConnGlobalNumEmbryonic,
       "cufwConnGlobalConnSetupRate1": cufwConnGlobalConnSetupRate1,
       "cufwConnGlobalConnSetupRate5": cufwConnGlobalConnSetupRate5,
       "cufwConnGlobalNumRemoteAccess": cufwConnGlobalNumRemoteAccess,
       "cuFwConnectionResources": cuFwConnectionResources,
       "cufwConnResMemoryUsage": cufwConnResMemoryUsage,
       "cufwConnResActiveConnMemoryUsage": cufwConnResActiveConnMemoryUsage,
       "cufwConnResHOConnMemoryUsage": cufwConnResHOConnMemoryUsage,
       "cufwConnResEmbrConnMemoryUsage": cufwConnResEmbrConnMemoryUsage,
       "cuFwConnectionReportSettings": cuFwConnectionReportSettings,
       "cufwConnReptAppStats": cufwConnReptAppStats,
       "cufwConnReptAppStatsLastChanged": cufwConnReptAppStatsLastChanged,
       "cuFwConnectionSummaryTables": cuFwConnectionSummaryTables,
       "cufwConnSummaryTable": cufwConnSummaryTable,
       "cufwConnSummaryEntry": cufwConnSummaryEntry,
       "cufwConnProtocol": cufwConnProtocol,
       "cufwConnNumAttempted": cufwConnNumAttempted,
       "cufwConnNumSetupsAborted": cufwConnNumSetupsAborted,
       "cufwConnNumPolicyDeclined": cufwConnNumPolicyDeclined,
       "cufwConnNumResDeclined": cufwConnNumResDeclined,
       "cufwConnNumHalfOpen": cufwConnNumHalfOpen,
       "cufwConnNumActive": cufwConnNumActive,
       "cufwConnNumAborted": cufwConnNumAborted,
       "cufwConnSetupRate1": cufwConnSetupRate1,
       "cufwConnSetupRate5": cufwConnSetupRate5,
       "cufwAppConnSummaryTable": cufwAppConnSummaryTable,
       "cufwAppConnSummaryEntry": cufwAppConnSummaryEntry,
       "cufwAppConnProtocol": cufwAppConnProtocol,
       "cufwAppConnNumAttempted": cufwAppConnNumAttempted,
       "cufwAppConnNumSetupsAborted": cufwAppConnNumSetupsAborted,
       "cufwAppConnNumPolicyDeclined": cufwAppConnNumPolicyDeclined,
       "cufwAppConnNumResDeclined": cufwAppConnNumResDeclined,
       "cufwAppConnNumHalfOpen": cufwAppConnNumHalfOpen,
       "cufwAppConnNumActive": cufwAppConnNumActive,
       "cufwAppConnNumAborted": cufwAppConnNumAborted,
       "cufwAppConnSetupRate1": cufwAppConnSetupRate1,
       "cufwAppConnSetupRate5": cufwAppConnSetupRate5,
       "cufwPolicyConnSummaryTable": cufwPolicyConnSummaryTable,
       "cufwPolicyConnSummaryEntry": cufwPolicyConnSummaryEntry,
       "cufwPolConnPolicy": cufwPolConnPolicy,
       "cufwPolConnPolicyTargetType": cufwPolConnPolicyTargetType,
       "cufwPolConnPolicyTarget": cufwPolConnPolicyTarget,
       "cufwPolConnProtocol": cufwPolConnProtocol,
       "cufwPolConnNumAttempted": cufwPolConnNumAttempted,
       "cufwPolConnNumSetupsAborted": cufwPolConnNumSetupsAborted,
       "cufwPolConnNumPolicyDeclined": cufwPolConnNumPolicyDeclined,
       "cufwPolConnNumResDeclined": cufwPolConnNumResDeclined,
       "cufwPolConnNumHalfOpen": cufwPolConnNumHalfOpen,
       "cufwPolConnNumActive": cufwPolConnNumActive,
       "cufwPolConnNumAborted": cufwPolConnNumAborted,
       "cufwPolicyAppConnSummaryTable": cufwPolicyAppConnSummaryTable,
       "cufwPolicyAppConnSummaryEntry": cufwPolicyAppConnSummaryEntry,
       "cufwPolAppConnPolicy": cufwPolAppConnPolicy,
       "cufwPolAppConnPolicyTargetType": cufwPolAppConnPolicyTargetType,
       "cufwPolAppConnPolicyTarget": cufwPolAppConnPolicyTarget,
       "cufwPolAppConnProtocol": cufwPolAppConnProtocol,
       "cufwPolAppConnNumAttempted": cufwPolAppConnNumAttempted,
       "cufwPolAppConnNumSetupsAborted": cufwPolAppConnNumSetupsAborted,
       "cufwPolAppConnNumPolicyDeclined": cufwPolAppConnNumPolicyDeclined,
       "cufwPolAppConnNumResDeclined": cufwPolAppConnNumResDeclined,
       "cufwPolAppConnNumHalfOpen": cufwPolAppConnNumHalfOpen,
       "cufwPolAppConnNumActive": cufwPolAppConnNumActive,
       "cufwPolAppConnNumAborted": cufwPolAppConnNumAborted,
       "cuFwApplInspectionGrp": cuFwApplInspectionGrp,
       "cufwAIAuditTrailEnabled": cufwAIAuditTrailEnabled,
       "cufwAIAlertEnabled": cufwAIAlertEnabled,
       "cufwInspectionTable": cufwInspectionTable,
       "cufwInspectionEntry": cufwInspectionEntry,
       "cufwInspectionPolicyName": cufwInspectionPolicyName,
       "cufwInspectionProtocol": cufwInspectionProtocol,
       "cufwInspectionStatus": cufwInspectionStatus,
       "cuFwUrlFilterGrp": cuFwUrlFilterGrp,
       "cufwUrlFilterGlobals": cufwUrlFilterGlobals,
       "cufwUrlfFunctionEnabled": cufwUrlfFunctionEnabled,
       "cufwUrlfRequestsNumProcessed": cufwUrlfRequestsNumProcessed,
       "cufwUrlfRequestsProcRate1": cufwUrlfRequestsProcRate1,
       "cufwUrlfRequestsProcRate5": cufwUrlfRequestsProcRate5,
       "cufwUrlfRequestsNumAllowed": cufwUrlfRequestsNumAllowed,
       "cufwUrlfRequestsNumDenied": cufwUrlfRequestsNumDenied,
       "cufwUrlfRequestsDeniedRate1": cufwUrlfRequestsDeniedRate1,
       "cufwUrlfRequestsDeniedRate5": cufwUrlfRequestsDeniedRate5,
       "cufwUrlfRequestsNumCacheAllowed": cufwUrlfRequestsNumCacheAllowed,
       "cufwUrlfRequestsNumCacheDenied": cufwUrlfRequestsNumCacheDenied,
       "cufwUrlfAllowModeReqNumAllowed": cufwUrlfAllowModeReqNumAllowed,
       "cufwUrlfAllowModeReqNumDenied": cufwUrlfAllowModeReqNumDenied,
       "cufwUrlfRequestsNumResDropped": cufwUrlfRequestsNumResDropped,
       "cufwUrlfRequestsResDropRate1": cufwUrlfRequestsResDropRate1,
       "cufwUrlfRequestsResDropRate5": cufwUrlfRequestsResDropRate5,
       "cufwUrlfNumServerTimeouts": cufwUrlfNumServerTimeouts,
       "cufwUrlfNumServerRetries": cufwUrlfNumServerRetries,
       "cufwUrlfResponsesNumLate": cufwUrlfResponsesNumLate,
       "cufwUrlfUrlAccRespsNumResDropped": cufwUrlfUrlAccRespsNumResDropped,
       "cufwUrlFilterResourceUsage": cufwUrlFilterResourceUsage,
       "cufwUrlfResTotalRequestCacheSize": cufwUrlfResTotalRequestCacheSize,
       "cufwUrlfResTotalRespCacheSize": cufwUrlfResTotalRespCacheSize,
       "cufwUrlFilterServers": cufwUrlFilterServers,
       "cufwUrlfServerTable": cufwUrlfServerTable,
       "cufwUrlfServerEntry": cufwUrlfServerEntry,
       "cufwUrlfServerAddrType": cufwUrlfServerAddrType,
       "cufwUrlfServerAddress": cufwUrlfServerAddress,
       "cufwUrlfServerPort": cufwUrlfServerPort,
       "cufwUrlfServerVendor": cufwUrlfServerVendor,
       "cufwUrlfServerStatus": cufwUrlfServerStatus,
       "cufwUrlfServerReqsNumProcessed": cufwUrlfServerReqsNumProcessed,
       "cufwUrlfServerReqsNumAllowed": cufwUrlfServerReqsNumAllowed,
       "cufwUrlfServerReqsNumDenied": cufwUrlfServerReqsNumDenied,
       "cufwUrlfServerNumTimeouts": cufwUrlfServerNumTimeouts,
       "cufwUrlfServerNumRetries": cufwUrlfServerNumRetries,
       "cufwUrlfServerRespsNumReceived": cufwUrlfServerRespsNumReceived,
       "cufwUrlfServerRespsNumLate": cufwUrlfServerRespsNumLate,
       "cufwUrlfServerAvgRespTime1": cufwUrlfServerAvgRespTime1,
       "cufwUrlfServerAvgRespTime5": cufwUrlfServerAvgRespTime5,
       "cuFwFailoverGrp": cuFwFailoverGrp,
       "cuFwAaicGrp": cuFwAaicGrp,
       "cufwAaicGlobals": cufwAaicGlobals,
       "cufwAaicGlobalNumBadProtocolOps": cufwAaicGlobalNumBadProtocolOps,
       "cufwAaicGlobalNumBadPDUSize": cufwAaicGlobalNumBadPDUSize,
       "cufwAaicGlobalNumBadPortRange": cufwAaicGlobalNumBadPortRange,
       "cufwAaicProtocolStats": cufwAaicProtocolStats,
       "cufwAaicHttpProtocolStats": cufwAaicHttpProtocolStats,
       "cufwAaicHttpNumBadProtocolOps": cufwAaicHttpNumBadProtocolOps,
       "cufwAaicHttpNumBadPDUSize": cufwAaicHttpNumBadPDUSize,
       "cufwAaicHttpNumTunneledConns": cufwAaicHttpNumTunneledConns,
       "cufwAaicHttpNumLargeURIs": cufwAaicHttpNumLargeURIs,
       "cufwAaicHttpNumBadContent": cufwAaicHttpNumBadContent,
       "cufwAaicHttpNumMismatchContent": cufwAaicHttpNumMismatchContent,
       "cufwAaicHttpNumDoubleEncodedPkts": cufwAaicHttpNumDoubleEncodedPkts,
       "cuFwL2FwGrp": cuFwL2FwGrp,
       "cufwL2FwGlobals": cufwL2FwGlobals,
       "cufwL2GlobalEnableStealthMode": cufwL2GlobalEnableStealthMode,
       "cufwL2GlobalArpCacheSize": cufwL2GlobalArpCacheSize,
       "cufwL2GlobalEnableArpInspection": cufwL2GlobalEnableArpInspection,
       "cufwL2GlobalNumArpRequests": cufwL2GlobalNumArpRequests,
       "cufwL2GlobalNumIcmpRequests": cufwL2GlobalNumIcmpRequests,
       "cufwL2GlobalNumFloods": cufwL2GlobalNumFloods,
       "cufwL2GlobalNumDrops": cufwL2GlobalNumDrops,
       "cufwL2GlobalArpOverflowRate5": cufwL2GlobalArpOverflowRate5,
       "cufwL2GlobalNumBadArpResponses": cufwL2GlobalNumBadArpResponses,
       "cufwL2GlobalNumSpoofedArpResps": cufwL2GlobalNumSpoofedArpResps,
       "cuFwNotifCntlGrp": cuFwNotifCntlGrp,
       "cufwCntlUrlfServerStatusChange": cufwCntlUrlfServerStatusChange,
       "cufwCntlL2StaticMacAddressMoved": cufwCntlL2StaticMacAddressMoved,
       "ciscoUnifiedFirewallMIBConform": ciscoUnifiedFirewallMIBConform,
       "ciscoUniFirewallMIBCompliances": ciscoUniFirewallMIBCompliances,
       "ciscoUniFirewallMIBCompliance": ciscoUniFirewallMIBCompliance,
       "ciscoUniFirewallMIBGroups": ciscoUniFirewallMIBGroups,
       "ciscoFwConnectionGroup": ciscoFwConnectionGroup,
       "ciscoFwConnResourceUsageGroup": ciscoFwConnResourceUsageGroup,
       "ciscoFwPolicyConnectionGroup": ciscoFwPolicyConnectionGroup,
       "ciscoFwApplInspectionGroup": ciscoFwApplInspectionGroup,
       "ciscoFwUrlFilterGroup": ciscoFwUrlFilterGroup,
       "ciscoFwUrlFilterResourceGroup": ciscoFwUrlFilterResourceGroup,
       "ciscoFwTransparentFwGroup": ciscoFwTransparentFwGroup,
       "ciscoFwNotificationsGroup": ciscoFwNotificationsGroup,
       "ciscoFwTransparentNotifGroup": ciscoFwTransparentNotifGroup,
       "ciscoFwBasicAaicGroup": ciscoFwBasicAaicGroup,
       "ciscoFwAaicHttpGroup": ciscoFwAaicHttpGroup,
       "ciscoFwMibReportingControlGroup": ciscoFwMibReportingControlGroup}
)
