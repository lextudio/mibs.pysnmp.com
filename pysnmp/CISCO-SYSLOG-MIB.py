# SNMP MIB module (CISCO-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:51 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41)
)
ciscoSyslogMIB.setRevisions(
        ("2005-12-03 00:00",
         "2005-08-11 00:00",
         "2005-06-01 00:00",
         "1995-08-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogSeverity(Integer32, TextualConvention):
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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSyslogMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSyslogMIBObjects = _CiscoSyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1)
)
_ClogBasic_ObjectIdentity = ObjectIdentity
clogBasic = _ClogBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1)
)
_ClogNotificationsSent_Type = Counter32
_ClogNotificationsSent_Object = MibScalar
clogNotificationsSent = _ClogNotificationsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 1),
    _ClogNotificationsSent_Type()
)
clogNotificationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogNotificationsSent.setStatus("current")
if mibBuilder.loadTexts:
    clogNotificationsSent.setUnits("notifications")


class _ClogNotificationsEnabled_Type(TruthValue):
    """Custom type clogNotificationsEnabled based on TruthValue"""


_ClogNotificationsEnabled_Object = MibScalar
clogNotificationsEnabled = _ClogNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 2),
    _ClogNotificationsEnabled_Type()
)
clogNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clogNotificationsEnabled.setStatus("current")


class _ClogMaxSeverity_Type(SyslogSeverity):
    """Custom type clogMaxSeverity based on SyslogSeverity"""


_ClogMaxSeverity_Object = MibScalar
clogMaxSeverity = _ClogMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 3),
    _ClogMaxSeverity_Type()
)
clogMaxSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clogMaxSeverity.setStatus("current")
_ClogMsgIgnores_Type = Counter32
_ClogMsgIgnores_Object = MibScalar
clogMsgIgnores = _ClogMsgIgnores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 4),
    _ClogMsgIgnores_Type()
)
clogMsgIgnores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogMsgIgnores.setStatus("current")
if mibBuilder.loadTexts:
    clogMsgIgnores.setUnits("messages")
_ClogMsgDrops_Type = Counter32
_ClogMsgDrops_Object = MibScalar
clogMsgDrops = _ClogMsgDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 5),
    _ClogMsgDrops_Type()
)
clogMsgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogMsgDrops.setStatus("current")
if mibBuilder.loadTexts:
    clogMsgDrops.setUnits("messages")


class _ClogOriginIDType_Type(Integer32):
    """Custom type clogOriginIDType based on Integer32"""
    defaultValue = 1

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
        *(("contextName", 5),
          ("hostName", 3),
          ("ipv4Address", 4),
          ("none", 1),
          ("other", 2),
          ("userDefined", 6))
    )


_ClogOriginIDType_Type.__name__ = "Integer32"
_ClogOriginIDType_Object = MibScalar
clogOriginIDType = _ClogOriginIDType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 6),
    _ClogOriginIDType_Type()
)
clogOriginIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clogOriginIDType.setStatus("current")
_ClogOriginID_Type = SnmpAdminString
_ClogOriginID_Object = MibScalar
clogOriginID = _ClogOriginID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 1, 7),
    _ClogOriginID_Type()
)
clogOriginID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clogOriginID.setStatus("current")
_ClogHistory_ObjectIdentity = ObjectIdentity
clogHistory = _ClogHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2)
)


class _ClogHistTableMaxLength_Type(Integer32):
    """Custom type clogHistTableMaxLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ClogHistTableMaxLength_Type.__name__ = "Integer32"
_ClogHistTableMaxLength_Object = MibScalar
clogHistTableMaxLength = _ClogHistTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 1),
    _ClogHistTableMaxLength_Type()
)
clogHistTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clogHistTableMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    clogHistTableMaxLength.setUnits("entries")
_ClogHistMsgsFlushed_Type = Counter32
_ClogHistMsgsFlushed_Object = MibScalar
clogHistMsgsFlushed = _ClogHistMsgsFlushed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 2),
    _ClogHistMsgsFlushed_Type()
)
clogHistMsgsFlushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogHistMsgsFlushed.setStatus("current")
if mibBuilder.loadTexts:
    clogHistMsgsFlushed.setUnits("messages")
_ClogHistoryTable_Object = MibTable
clogHistoryTable = _ClogHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3)
)
if mibBuilder.loadTexts:
    clogHistoryTable.setStatus("current")
_ClogHistoryEntry_Object = MibTableRow
clogHistoryEntry = _ClogHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1)
)
clogHistoryEntry.setIndexNames(
    (0, "CISCO-SYSLOG-MIB", "clogHistIndex"),
)
if mibBuilder.loadTexts:
    clogHistoryEntry.setStatus("current")


class _ClogHistIndex_Type(Integer32):
    """Custom type clogHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClogHistIndex_Type.__name__ = "Integer32"
_ClogHistIndex_Object = MibTableColumn
clogHistIndex = _ClogHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 1),
    _ClogHistIndex_Type()
)
clogHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clogHistIndex.setStatus("current")


class _ClogHistFacility_Type(DisplayString):
    """Custom type clogHistFacility based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ClogHistFacility_Type.__name__ = "DisplayString"
_ClogHistFacility_Object = MibTableColumn
clogHistFacility = _ClogHistFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 2),
    _ClogHistFacility_Type()
)
clogHistFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogHistFacility.setStatus("current")
_ClogHistSeverity_Type = SyslogSeverity
_ClogHistSeverity_Object = MibTableColumn
clogHistSeverity = _ClogHistSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 3),
    _ClogHistSeverity_Type()
)
clogHistSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogHistSeverity.setStatus("current")


class _ClogHistMsgName_Type(DisplayString):
    """Custom type clogHistMsgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ClogHistMsgName_Type.__name__ = "DisplayString"
_ClogHistMsgName_Object = MibTableColumn
clogHistMsgName = _ClogHistMsgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 4),
    _ClogHistMsgName_Type()
)
clogHistMsgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogHistMsgName.setStatus("current")


class _ClogHistMsgText_Type(DisplayString):
    """Custom type clogHistMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClogHistMsgText_Type.__name__ = "DisplayString"
_ClogHistMsgText_Object = MibTableColumn
clogHistMsgText = _ClogHistMsgText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 5),
    _ClogHistMsgText_Type()
)
clogHistMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogHistMsgText.setStatus("current")
_ClogHistTimestamp_Type = TimeStamp
_ClogHistTimestamp_Object = MibTableColumn
clogHistTimestamp = _ClogHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 2, 3, 1, 6),
    _ClogHistTimestamp_Type()
)
clogHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogHistTimestamp.setStatus("current")
_ClogServer_ObjectIdentity = ObjectIdentity
clogServer = _ClogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3)
)
_ClogMaxServers_Type = Unsigned32
_ClogMaxServers_Object = MibScalar
clogMaxServers = _ClogMaxServers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 1),
    _ClogMaxServers_Type()
)
clogMaxServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clogMaxServers.setStatus("current")
_ClogServerConfigTable_Object = MibTable
clogServerConfigTable = _ClogServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2)
)
if mibBuilder.loadTexts:
    clogServerConfigTable.setStatus("current")
_ClogServerConfigEntry_Object = MibTableRow
clogServerConfigEntry = _ClogServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2, 1)
)
clogServerConfigEntry.setIndexNames(
    (0, "CISCO-SYSLOG-MIB", "clogServerAddrType"),
    (0, "CISCO-SYSLOG-MIB", "clogServerAddr"),
)
if mibBuilder.loadTexts:
    clogServerConfigEntry.setStatus("current")
_ClogServerAddrType_Type = InetAddressType
_ClogServerAddrType_Object = MibTableColumn
clogServerAddrType = _ClogServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2, 1, 1),
    _ClogServerAddrType_Type()
)
clogServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clogServerAddrType.setStatus("current")


class _ClogServerAddr_Type(InetAddress):
    """Custom type clogServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClogServerAddr_Type.__name__ = "InetAddress"
_ClogServerAddr_Object = MibTableColumn
clogServerAddr = _ClogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2, 1, 2),
    _ClogServerAddr_Type()
)
clogServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clogServerAddr.setStatus("current")
_ClogServerStatus_Type = RowStatus
_ClogServerStatus_Object = MibTableColumn
clogServerStatus = _ClogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 1, 3, 2, 1, 3),
    _ClogServerStatus_Type()
)
clogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clogServerStatus.setStatus("current")
_CiscoSyslogMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoSyslogMIBNotificationPrefix = _CiscoSyslogMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 2)
)
_CiscoSyslogMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSyslogMIBNotifications = _CiscoSyslogMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 2, 0)
)
_CiscoSyslogMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSyslogMIBConformance = _CiscoSyslogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 3)
)
_CiscoSyslogMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSyslogMIBCompliances = _CiscoSyslogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 1)
)
_CiscoSyslogMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSyslogMIBGroups = _CiscoSyslogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2)
)

# Managed Objects groups

ciscoSyslogMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2, 1)
)
ciscoSyslogMIBGroup.setObjects(
      *(("CISCO-SYSLOG-MIB", "clogNotificationsSent"),
        ("CISCO-SYSLOG-MIB", "clogNotificationsEnabled"),
        ("CISCO-SYSLOG-MIB", "clogMaxSeverity"),
        ("CISCO-SYSLOG-MIB", "clogMsgIgnores"),
        ("CISCO-SYSLOG-MIB", "clogMsgDrops"),
        ("CISCO-SYSLOG-MIB", "clogHistTableMaxLength"),
        ("CISCO-SYSLOG-MIB", "clogHistMsgsFlushed"),
        ("CISCO-SYSLOG-MIB", "clogHistFacility"),
        ("CISCO-SYSLOG-MIB", "clogHistSeverity"),
        ("CISCO-SYSLOG-MIB", "clogHistMsgName"),
        ("CISCO-SYSLOG-MIB", "clogHistMsgText"),
        ("CISCO-SYSLOG-MIB", "clogHistTimestamp"))
)
if mibBuilder.loadTexts:
    ciscoSyslogMIBGroup.setStatus("current")

clogServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2, 3)
)
clogServerGroup.setObjects(
      *(("CISCO-SYSLOG-MIB", "clogMaxServers"),
        ("CISCO-SYSLOG-MIB", "clogServerStatus"))
)
if mibBuilder.loadTexts:
    clogServerGroup.setStatus("current")

clogOriginIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2, 4)
)
clogOriginIDGroup.setObjects(
      *(("CISCO-SYSLOG-MIB", "clogOriginIDType"),
        ("CISCO-SYSLOG-MIB", "clogOriginID"))
)
if mibBuilder.loadTexts:
    clogOriginIDGroup.setStatus("current")


# Notification objects

clogMessageGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 2, 0, 1)
)
clogMessageGenerated.setObjects(
      *(("CISCO-SYSLOG-MIB", "clogHistFacility"),
        ("CISCO-SYSLOG-MIB", "clogHistSeverity"),
        ("CISCO-SYSLOG-MIB", "clogHistMsgName"),
        ("CISCO-SYSLOG-MIB", "clogHistMsgText"),
        ("CISCO-SYSLOG-MIB", "clogHistTimestamp"))
)
if mibBuilder.loadTexts:
    clogMessageGenerated.setStatus(
        "current"
    )


# Notifications groups

clogNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 2, 2)
)
clogNotificationsGroup.setObjects(
    ("CISCO-SYSLOG-MIB", "clogMessageGenerated")
)
if mibBuilder.loadTexts:
    clogNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSyslogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSyslogMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSyslogMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 41, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSyslogMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SYSLOG-MIB",
    **{"SyslogSeverity": SyslogSeverity,
       "ciscoSyslogMIB": ciscoSyslogMIB,
       "ciscoSyslogMIBObjects": ciscoSyslogMIBObjects,
       "clogBasic": clogBasic,
       "clogNotificationsSent": clogNotificationsSent,
       "clogNotificationsEnabled": clogNotificationsEnabled,
       "clogMaxSeverity": clogMaxSeverity,
       "clogMsgIgnores": clogMsgIgnores,
       "clogMsgDrops": clogMsgDrops,
       "clogOriginIDType": clogOriginIDType,
       "clogOriginID": clogOriginID,
       "clogHistory": clogHistory,
       "clogHistTableMaxLength": clogHistTableMaxLength,
       "clogHistMsgsFlushed": clogHistMsgsFlushed,
       "clogHistoryTable": clogHistoryTable,
       "clogHistoryEntry": clogHistoryEntry,
       "clogHistIndex": clogHistIndex,
       "clogHistFacility": clogHistFacility,
       "clogHistSeverity": clogHistSeverity,
       "clogHistMsgName": clogHistMsgName,
       "clogHistMsgText": clogHistMsgText,
       "clogHistTimestamp": clogHistTimestamp,
       "clogServer": clogServer,
       "clogMaxServers": clogMaxServers,
       "clogServerConfigTable": clogServerConfigTable,
       "clogServerConfigEntry": clogServerConfigEntry,
       "clogServerAddrType": clogServerAddrType,
       "clogServerAddr": clogServerAddr,
       "clogServerStatus": clogServerStatus,
       "ciscoSyslogMIBNotificationPrefix": ciscoSyslogMIBNotificationPrefix,
       "ciscoSyslogMIBNotifications": ciscoSyslogMIBNotifications,
       "clogMessageGenerated": clogMessageGenerated,
       "ciscoSyslogMIBConformance": ciscoSyslogMIBConformance,
       "ciscoSyslogMIBCompliances": ciscoSyslogMIBCompliances,
       "ciscoSyslogMIBCompliance": ciscoSyslogMIBCompliance,
       "ciscoSyslogMIBComplianceRev1": ciscoSyslogMIBComplianceRev1,
       "ciscoSyslogMIBGroups": ciscoSyslogMIBGroups,
       "ciscoSyslogMIBGroup": ciscoSyslogMIBGroup,
       "clogNotificationsGroup": clogNotificationsGroup,
       "clogServerGroup": clogServerGroup,
       "clogOriginIDGroup": clogOriginIDGroup}
)
