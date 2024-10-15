# SNMP MIB module (CISCO-CALL-TRACKER-TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CALL-TRACKER-TCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:50 2024
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

(cctActiveCallId,
 cctHistoryIndex) = mibBuilder.importSymbols(
    "CISCO-CALL-TRACKER-MIB",
    "cctActiveCallId",
    "cctHistoryIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

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

ciscoCallTrackerTCPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 164)
)
ciscoCallTrackerTCPMIB.setRevisions(
        ("2005-12-06 00:00",
         "2000-06-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CcttMIBObjects_ObjectIdentity = ObjectIdentity
ccttMIBObjects = _CcttMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1)
)
_CcttActive_ObjectIdentity = ObjectIdentity
ccttActive = _CcttActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1)
)
_CcttActiveTable_Object = MibTable
ccttActiveTable = _CcttActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccttActiveTable.setStatus("current")
_CcttActiveEntry_Object = MibTableRow
ccttActiveEntry = _CcttActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1)
)
ccttActiveEntry.setIndexNames(
    (0, "CISCO-CALL-TRACKER-MIB", "cctActiveCallId"),
)
if mibBuilder.loadTexts:
    ccttActiveEntry.setStatus("current")
_CcttActiveLocalIpAddress_Type = IpAddress
_CcttActiveLocalIpAddress_Object = MibTableColumn
ccttActiveLocalIpAddress = _CcttActiveLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 1),
    _CcttActiveLocalIpAddress_Type()
)
ccttActiveLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttActiveLocalIpAddress.setStatus("current")
_CcttActiveLocalTcpPort_Type = CiscoPort
_CcttActiveLocalTcpPort_Object = MibTableColumn
ccttActiveLocalTcpPort = _CcttActiveLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 2),
    _CcttActiveLocalTcpPort_Type()
)
ccttActiveLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttActiveLocalTcpPort.setStatus("current")
_CcttActiveRemoteIpAddress_Type = IpAddress
_CcttActiveRemoteIpAddress_Object = MibTableColumn
ccttActiveRemoteIpAddress = _CcttActiveRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 3),
    _CcttActiveRemoteIpAddress_Type()
)
ccttActiveRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttActiveRemoteIpAddress.setStatus("current")
_CcttActiveRemoteTcpPort_Type = CiscoPort
_CcttActiveRemoteTcpPort_Object = MibTableColumn
ccttActiveRemoteTcpPort = _CcttActiveRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 4),
    _CcttActiveRemoteTcpPort_Type()
)
ccttActiveRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttActiveRemoteTcpPort.setStatus("current")
_CcttActiveDestinationFailures_Type = Counter32
_CcttActiveDestinationFailures_Object = MibTableColumn
ccttActiveDestinationFailures = _CcttActiveDestinationFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 1, 1, 1, 5),
    _CcttActiveDestinationFailures_Type()
)
ccttActiveDestinationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttActiveDestinationFailures.setStatus("current")
_CcttHistory_ObjectIdentity = ObjectIdentity
ccttHistory = _CcttHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2)
)
_CcttHistoryTable_Object = MibTable
ccttHistoryTable = _CcttHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccttHistoryTable.setStatus("current")
_CcttHistoryEntry_Object = MibTableRow
ccttHistoryEntry = _CcttHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1)
)
ccttHistoryEntry.setIndexNames(
    (0, "CISCO-CALL-TRACKER-MIB", "cctHistoryIndex"),
)
if mibBuilder.loadTexts:
    ccttHistoryEntry.setStatus("current")
_CcttHistoryLocalIpAddress_Type = IpAddress
_CcttHistoryLocalIpAddress_Object = MibTableColumn
ccttHistoryLocalIpAddress = _CcttHistoryLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 1),
    _CcttHistoryLocalIpAddress_Type()
)
ccttHistoryLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttHistoryLocalIpAddress.setStatus("current")
_CcttHistoryLocalTcpPort_Type = CiscoPort
_CcttHistoryLocalTcpPort_Object = MibTableColumn
ccttHistoryLocalTcpPort = _CcttHistoryLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 2),
    _CcttHistoryLocalTcpPort_Type()
)
ccttHistoryLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttHistoryLocalTcpPort.setStatus("current")
_CcttHistoryRemoteIpAddress_Type = IpAddress
_CcttHistoryRemoteIpAddress_Object = MibTableColumn
ccttHistoryRemoteIpAddress = _CcttHistoryRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 3),
    _CcttHistoryRemoteIpAddress_Type()
)
ccttHistoryRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttHistoryRemoteIpAddress.setStatus("current")
_CcttHistoryRemoteTcpPort_Type = CiscoPort
_CcttHistoryRemoteTcpPort_Object = MibTableColumn
ccttHistoryRemoteTcpPort = _CcttHistoryRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 4),
    _CcttHistoryRemoteTcpPort_Type()
)
ccttHistoryRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttHistoryRemoteTcpPort.setStatus("current")
_CcttHistoryDestinationFailures_Type = Counter32
_CcttHistoryDestinationFailures_Object = MibTableColumn
ccttHistoryDestinationFailures = _CcttHistoryDestinationFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 1, 2, 1, 1, 5),
    _CcttHistoryDestinationFailures_Type()
)
ccttHistoryDestinationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccttHistoryDestinationFailures.setStatus("current")
_CcttMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ccttMIBNotificationPrefix = _CcttMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 2)
)
_CcttMIBNotifications_ObjectIdentity = ObjectIdentity
ccttMIBNotifications = _CcttMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 2, 0)
)
_CcttMIBConformance_ObjectIdentity = ObjectIdentity
ccttMIBConformance = _CcttMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 3)
)
_CcttMIBCompliances_ObjectIdentity = ObjectIdentity
ccttMIBCompliances = _CcttMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 1)
)
_CcttMIBGroups_ObjectIdentity = ObjectIdentity
ccttMIBGroups = _CcttMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 2)
)

# Managed Objects groups

ccttActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 2, 2)
)
ccttActiveGroup.setObjects(
      *(("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveLocalIpAddress"),
        ("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveLocalTcpPort"),
        ("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveRemoteIpAddress"),
        ("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveRemoteTcpPort"),
        ("CISCO-CALL-TRACKER-TCP-MIB", "ccttActiveDestinationFailures"))
)
if mibBuilder.loadTexts:
    ccttActiveGroup.setStatus("current")

ccttHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 2, 3)
)
ccttHistoryGroup.setObjects(
      *(("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryLocalIpAddress"),
        ("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryLocalTcpPort"),
        ("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryRemoteIpAddress"),
        ("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryRemoteTcpPort"),
        ("CISCO-CALL-TRACKER-TCP-MIB", "ccttHistoryDestinationFailures"))
)
if mibBuilder.loadTexts:
    ccttHistoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccttMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 164, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ccttMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CALL-TRACKER-TCP-MIB",
    **{"ciscoCallTrackerTCPMIB": ciscoCallTrackerTCPMIB,
       "ccttMIBObjects": ccttMIBObjects,
       "ccttActive": ccttActive,
       "ccttActiveTable": ccttActiveTable,
       "ccttActiveEntry": ccttActiveEntry,
       "ccttActiveLocalIpAddress": ccttActiveLocalIpAddress,
       "ccttActiveLocalTcpPort": ccttActiveLocalTcpPort,
       "ccttActiveRemoteIpAddress": ccttActiveRemoteIpAddress,
       "ccttActiveRemoteTcpPort": ccttActiveRemoteTcpPort,
       "ccttActiveDestinationFailures": ccttActiveDestinationFailures,
       "ccttHistory": ccttHistory,
       "ccttHistoryTable": ccttHistoryTable,
       "ccttHistoryEntry": ccttHistoryEntry,
       "ccttHistoryLocalIpAddress": ccttHistoryLocalIpAddress,
       "ccttHistoryLocalTcpPort": ccttHistoryLocalTcpPort,
       "ccttHistoryRemoteIpAddress": ccttHistoryRemoteIpAddress,
       "ccttHistoryRemoteTcpPort": ccttHistoryRemoteTcpPort,
       "ccttHistoryDestinationFailures": ccttHistoryDestinationFailures,
       "ccttMIBNotificationPrefix": ccttMIBNotificationPrefix,
       "ccttMIBNotifications": ccttMIBNotifications,
       "ccttMIBConformance": ccttMIBConformance,
       "ccttMIBCompliances": ccttMIBCompliances,
       "ccttMIBCompliance": ccttMIBCompliance,
       "ccttMIBGroups": ccttMIBGroups,
       "ccttActiveGroup": ccttActiveGroup,
       "ccttHistoryGroup": ccttHistoryGroup}
)
