# SNMP MIB module (CISCO-AAA-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AAA-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:26 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoAAASessionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 150)
)
ciscoAAASessionMIB.setRevisions(
        ("2006-03-21 00:00",
         "2002-04-11 00:00",
         "1999-11-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CctCallId(Unsigned32, TextualConvention):
    status = "current"


class CasnSessionId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_CasnMIBObjects_ObjectIdentity = ObjectIdentity
casnMIBObjects = _CasnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1)
)
_CasnActive_ObjectIdentity = ObjectIdentity
casnActive = _CasnActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1)
)
_CasnActiveTableEntries_Type = Gauge32
_CasnActiveTableEntries_Object = MibScalar
casnActiveTableEntries = _CasnActiveTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 1),
    _CasnActiveTableEntries_Type()
)
casnActiveTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnActiveTableEntries.setStatus("current")
_CasnActiveTableHighWaterMark_Type = Gauge32
_CasnActiveTableHighWaterMark_Object = MibScalar
casnActiveTableHighWaterMark = _CasnActiveTableHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 2),
    _CasnActiveTableHighWaterMark_Type()
)
casnActiveTableHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnActiveTableHighWaterMark.setStatus("current")
_CasnActiveTable_Object = MibTable
casnActiveTable = _CasnActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3)
)
if mibBuilder.loadTexts:
    casnActiveTable.setStatus("current")
_CasnActiveEntry_Object = MibTableRow
casnActiveEntry = _CasnActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1)
)
casnActiveEntry.setIndexNames(
    (0, "CISCO-AAA-SESSION-MIB", "casnSessionId"),
)
if mibBuilder.loadTexts:
    casnActiveEntry.setStatus("current")
_CasnSessionId_Type = CasnSessionId
_CasnSessionId_Object = MibTableColumn
casnSessionId = _CasnSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 1),
    _CasnSessionId_Type()
)
casnSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casnSessionId.setStatus("current")


class _CasnUserId_Type(DisplayString):
    """Custom type casnUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CasnUserId_Type.__name__ = "DisplayString"
_CasnUserId_Object = MibTableColumn
casnUserId = _CasnUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 2),
    _CasnUserId_Type()
)
casnUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnUserId.setStatus("current")
_CasnIpAddr_Type = IpAddress
_CasnIpAddr_Object = MibTableColumn
casnIpAddr = _CasnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 3),
    _CasnIpAddr_Type()
)
casnIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnIpAddr.setStatus("current")
_CasnIdleTime_Type = Gauge32
_CasnIdleTime_Object = MibTableColumn
casnIdleTime = _CasnIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 4),
    _CasnIdleTime_Type()
)
casnIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    casnIdleTime.setUnits("seconds")
_CasnDisconnect_Type = TruthValue
_CasnDisconnect_Object = MibTableColumn
casnDisconnect = _CasnDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 5),
    _CasnDisconnect_Type()
)
casnDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    casnDisconnect.setStatus("current")
_CasnCallTrackerId_Type = CctCallId
_CasnCallTrackerId_Object = MibTableColumn
casnCallTrackerId = _CasnCallTrackerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 6),
    _CasnCallTrackerId_Type()
)
casnCallTrackerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnCallTrackerId.setStatus("current")
_CasnNasPort_Type = RowPointer
_CasnNasPort_Object = MibTableColumn
casnNasPort = _CasnNasPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 7),
    _CasnNasPort_Type()
)
casnNasPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnNasPort.setStatus("current")
_CasnVaiIfIndex_Type = InterfaceIndexOrZero
_CasnVaiIfIndex_Object = MibTableColumn
casnVaiIfIndex = _CasnVaiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 8),
    _CasnVaiIfIndex_Type()
)
casnVaiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnVaiIfIndex.setStatus("current")
_CasnGeneral_ObjectIdentity = ObjectIdentity
casnGeneral = _CasnGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2)
)
_CasnTotalSessions_Type = Counter32
_CasnTotalSessions_Object = MibScalar
casnTotalSessions = _CasnTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 1),
    _CasnTotalSessions_Type()
)
casnTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnTotalSessions.setStatus("current")
_CasnDisconnectedSessions_Type = Counter32
_CasnDisconnectedSessions_Object = MibScalar
casnDisconnectedSessions = _CasnDisconnectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 2),
    _CasnDisconnectedSessions_Type()
)
casnDisconnectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casnDisconnectedSessions.setStatus("current")
_CasnMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
casnMIBNotificationPrefix = _CasnMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 2)
)
_CasnMIBNotifications_ObjectIdentity = ObjectIdentity
casnMIBNotifications = _CasnMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 2, 1)
)
_CasnMIBConformance_ObjectIdentity = ObjectIdentity
casnMIBConformance = _CasnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 3)
)
_CasnMIBCompliances_ObjectIdentity = ObjectIdentity
casnMIBCompliances = _CasnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1)
)
_CasnMIBGroups_ObjectIdentity = ObjectIdentity
casnMIBGroups = _CasnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2)
)

# Managed Objects groups

casnActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 1)
)
casnActiveGroup.setObjects(
      *(("CISCO-AAA-SESSION-MIB", "casnActiveTableEntries"),
        ("CISCO-AAA-SESSION-MIB", "casnActiveTableHighWaterMark"),
        ("CISCO-AAA-SESSION-MIB", "casnUserId"),
        ("CISCO-AAA-SESSION-MIB", "casnIpAddr"),
        ("CISCO-AAA-SESSION-MIB", "casnIdleTime"),
        ("CISCO-AAA-SESSION-MIB", "casnDisconnect"),
        ("CISCO-AAA-SESSION-MIB", "casnCallTrackerId"))
)
if mibBuilder.loadTexts:
    casnActiveGroup.setStatus("current")

casnGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 2)
)
casnGeneralGroup.setObjects(
      *(("CISCO-AAA-SESSION-MIB", "casnTotalSessions"),
        ("CISCO-AAA-SESSION-MIB", "casnDisconnectedSessions"))
)
if mibBuilder.loadTexts:
    casnGeneralGroup.setStatus("current")

casnActiveGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 3)
)
casnActiveGroupSup1.setObjects(
      *(("CISCO-AAA-SESSION-MIB", "casnNasPort"),
        ("CISCO-AAA-SESSION-MIB", "casnVaiIfIndex"))
)
if mibBuilder.loadTexts:
    casnActiveGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

casnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 1)
)
if mibBuilder.loadTexts:
    casnMIBCompliance.setStatus(
        "deprecated"
    )

casnMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 2)
)
if mibBuilder.loadTexts:
    casnMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AAA-SESSION-MIB",
    **{"CctCallId": CctCallId,
       "CasnSessionId": CasnSessionId,
       "ciscoAAASessionMIB": ciscoAAASessionMIB,
       "casnMIBObjects": casnMIBObjects,
       "casnActive": casnActive,
       "casnActiveTableEntries": casnActiveTableEntries,
       "casnActiveTableHighWaterMark": casnActiveTableHighWaterMark,
       "casnActiveTable": casnActiveTable,
       "casnActiveEntry": casnActiveEntry,
       "casnSessionId": casnSessionId,
       "casnUserId": casnUserId,
       "casnIpAddr": casnIpAddr,
       "casnIdleTime": casnIdleTime,
       "casnDisconnect": casnDisconnect,
       "casnCallTrackerId": casnCallTrackerId,
       "casnNasPort": casnNasPort,
       "casnVaiIfIndex": casnVaiIfIndex,
       "casnGeneral": casnGeneral,
       "casnTotalSessions": casnTotalSessions,
       "casnDisconnectedSessions": casnDisconnectedSessions,
       "casnMIBNotificationPrefix": casnMIBNotificationPrefix,
       "casnMIBNotifications": casnMIBNotifications,
       "casnMIBConformance": casnMIBConformance,
       "casnMIBCompliances": casnMIBCompliances,
       "casnMIBCompliance": casnMIBCompliance,
       "casnMIBComplianceRev1": casnMIBComplianceRev1,
       "casnMIBGroups": casnMIBGroups,
       "casnActiveGroup": casnActiveGroup,
       "casnGeneralGroup": casnGeneralGroup,
       "casnActiveGroupSup1": casnActiveGroupSup1}
)
