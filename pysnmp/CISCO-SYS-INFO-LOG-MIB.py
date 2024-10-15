# SNMP MIB module (CISCO-SYS-INFO-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SYS-INFO-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:21 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSysInfoLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 330)
)
ciscoSysInfoLogMIB.setRevisions(
        ("2005-08-12 10:00",
         "2003-01-24 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSysInfoLogMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSysInfoLogMIBNotifs = _CiscoSysInfoLogMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 0)
)
_CiscoSysInfoLogMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSysInfoLogMIBObjects = _CiscoSysInfoLogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1)
)
_CsilGlobalConfig_ObjectIdentity = ObjectIdentity
csilGlobalConfig = _CsilGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 1)
)
_CsilSysInfoLogEnabled_Type = TruthValue
_CsilSysInfoLogEnabled_Object = MibScalar
csilSysInfoLogEnabled = _CsilSysInfoLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 1, 1),
    _CsilSysInfoLogEnabled_Type()
)
csilSysInfoLogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csilSysInfoLogEnabled.setStatus("current")
_CsilSysInfoLogNotifEnabled_Type = TruthValue
_CsilSysInfoLogNotifEnabled_Object = MibScalar
csilSysInfoLogNotifEnabled = _CsilSysInfoLogNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 1, 2),
    _CsilSysInfoLogNotifEnabled_Type()
)
csilSysInfoLogNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csilSysInfoLogNotifEnabled.setStatus("current")
_CsilServerConfig_ObjectIdentity = ObjectIdentity
csilServerConfig = _CsilServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2)
)


class _CsilMaxServerAllowed_Type(Unsigned32):
    """Custom type csilMaxServerAllowed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CsilMaxServerAllowed_Type.__name__ = "Unsigned32"
_CsilMaxServerAllowed_Object = MibScalar
csilMaxServerAllowed = _CsilMaxServerAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 1),
    _CsilMaxServerAllowed_Type()
)
csilMaxServerAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csilMaxServerAllowed.setStatus("current")
if mibBuilder.loadTexts:
    csilMaxServerAllowed.setUnits("servers")
_CsilMaxProfilePerServerAllowed_Type = Unsigned32
_CsilMaxProfilePerServerAllowed_Object = MibScalar
csilMaxProfilePerServerAllowed = _CsilMaxProfilePerServerAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 2),
    _CsilMaxProfilePerServerAllowed_Type()
)
csilMaxProfilePerServerAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csilMaxProfilePerServerAllowed.setStatus("current")
if mibBuilder.loadTexts:
    csilMaxProfilePerServerAllowed.setUnits("profiles")
_CsilServerTable_Object = MibTable
csilServerTable = _CsilServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3)
)
if mibBuilder.loadTexts:
    csilServerTable.setStatus("current")
_CsilServerEntry_Object = MibTableRow
csilServerEntry = _CsilServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1)
)
csilServerEntry.setIndexNames(
    (0, "CISCO-SYS-INFO-LOG-MIB", "csilServerIndex"),
)
if mibBuilder.loadTexts:
    csilServerEntry.setStatus("current")
_CsilServerIndex_Type = Unsigned32
_CsilServerIndex_Object = MibTableColumn
csilServerIndex = _CsilServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 1),
    _CsilServerIndex_Type()
)
csilServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csilServerIndex.setStatus("current")
_CsilServerAddressType_Type = InetAddressType
_CsilServerAddressType_Object = MibTableColumn
csilServerAddressType = _CsilServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 2),
    _CsilServerAddressType_Type()
)
csilServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilServerAddressType.setStatus("current")
_CsilServerAddress_Type = InetAddress
_CsilServerAddress_Object = MibTableColumn
csilServerAddress = _CsilServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 3),
    _CsilServerAddress_Type()
)
csilServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilServerAddress.setStatus("current")
_CsilServerProfileIndex_Type = Unsigned32
_CsilServerProfileIndex_Object = MibTableColumn
csilServerProfileIndex = _CsilServerProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 4),
    _CsilServerProfileIndex_Type()
)
csilServerProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilServerProfileIndex.setStatus("current")


class _CsilServerProtocol_Type(Integer32):
    """Custom type csilServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 3),
          ("rcp", 2),
          ("tftp", 1))
    )


_CsilServerProtocol_Type.__name__ = "Integer32"
_CsilServerProtocol_Object = MibTableColumn
csilServerProtocol = _CsilServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 5),
    _CsilServerProtocol_Type()
)
csilServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilServerProtocol.setStatus("current")
_CsilServerRcpUserName_Type = SnmpAdminString
_CsilServerRcpUserName_Object = MibTableColumn
csilServerRcpUserName = _CsilServerRcpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 6),
    _CsilServerRcpUserName_Type()
)
csilServerRcpUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilServerRcpUserName.setStatus("current")


class _CsilServerInterval_Type(Unsigned32):
    """Custom type csilServerInterval based on Unsigned32"""
    defaultValue = 1440


_CsilServerInterval_Object = MibTableColumn
csilServerInterval = _CsilServerInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 7),
    _CsilServerInterval_Type()
)
csilServerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilServerInterval.setStatus("current")
if mibBuilder.loadTexts:
    csilServerInterval.setUnits("minutes")
_CsilServerLoggingFileName_Type = SnmpAdminString
_CsilServerLoggingFileName_Object = MibTableColumn
csilServerLoggingFileName = _CsilServerLoggingFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 8),
    _CsilServerLoggingFileName_Type()
)
csilServerLoggingFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilServerLoggingFileName.setStatus("current")


class _CsilServerLastStatus_Type(Integer32):
    """Custom type csilServerLastStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("addrError", 6),
          ("authError", 5),
          ("copying", 7),
          ("ftpError", 10),
          ("linkBlock", 4),
          ("noCommand", 3),
          ("noLogFile", 2),
          ("none", 1),
          ("success", 9),
          ("writeError", 8))
    )


_CsilServerLastStatus_Type.__name__ = "Integer32"
_CsilServerLastStatus_Object = MibTableColumn
csilServerLastStatus = _CsilServerLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 9),
    _CsilServerLastStatus_Type()
)
csilServerLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csilServerLastStatus.setStatus("current")
_CsilServerRowStatus_Type = RowStatus
_CsilServerRowStatus_Object = MibTableColumn
csilServerRowStatus = _CsilServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 2, 3, 1, 10),
    _CsilServerRowStatus_Type()
)
csilServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilServerRowStatus.setStatus("current")
_CsilCommandConfig_ObjectIdentity = ObjectIdentity
csilCommandConfig = _CsilCommandConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3)
)
_CsilMaxCommandPerProfile_Type = Unsigned32
_CsilMaxCommandPerProfile_Object = MibScalar
csilMaxCommandPerProfile = _CsilMaxCommandPerProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 1),
    _CsilMaxCommandPerProfile_Type()
)
csilMaxCommandPerProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csilMaxCommandPerProfile.setStatus("current")
_CsilCommandsTable_Object = MibTable
csilCommandsTable = _CsilCommandsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2)
)
if mibBuilder.loadTexts:
    csilCommandsTable.setStatus("current")
_CsilCommandsEntry_Object = MibTableRow
csilCommandsEntry = _CsilCommandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1)
)
csilCommandsEntry.setIndexNames(
    (0, "CISCO-SYS-INFO-LOG-MIB", "csilCommandProfileIndex"),
    (0, "CISCO-SYS-INFO-LOG-MIB", "csilCommandIndex"),
)
if mibBuilder.loadTexts:
    csilCommandsEntry.setStatus("current")
_CsilCommandProfileIndex_Type = Unsigned32
_CsilCommandProfileIndex_Object = MibTableColumn
csilCommandProfileIndex = _CsilCommandProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 1),
    _CsilCommandProfileIndex_Type()
)
csilCommandProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csilCommandProfileIndex.setStatus("current")
_CsilCommandIndex_Type = Unsigned32
_CsilCommandIndex_Object = MibTableColumn
csilCommandIndex = _CsilCommandIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 2),
    _CsilCommandIndex_Type()
)
csilCommandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csilCommandIndex.setStatus("current")


class _CsilCommandString_Type(SnmpAdminString):
    """Custom type csilCommandString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CsilCommandString_Type.__name__ = "SnmpAdminString"
_CsilCommandString_Object = MibTableColumn
csilCommandString = _CsilCommandString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 3),
    _CsilCommandString_Type()
)
csilCommandString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilCommandString.setStatus("current")
_CsilCommandExecOrder_Type = Unsigned32
_CsilCommandExecOrder_Object = MibTableColumn
csilCommandExecOrder = _CsilCommandExecOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 4),
    _CsilCommandExecOrder_Type()
)
csilCommandExecOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilCommandExecOrder.setStatus("current")
_CsilCommandStatus_Type = RowStatus
_CsilCommandStatus_Object = MibTableColumn
csilCommandStatus = _CsilCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 1, 3, 2, 1, 5),
    _CsilCommandStatus_Type()
)
csilCommandStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csilCommandStatus.setStatus("current")
_CiscoSysInfoLogMIBConform_ObjectIdentity = ObjectIdentity
ciscoSysInfoLogMIBConform = _CiscoSysInfoLogMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 2)
)
_CiscoSysInfoLogMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSysInfoLogMIBCompliances = _CiscoSysInfoLogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 1)
)
_CiscoSysInfoLogMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSysInfoLogMIBGroups = _CiscoSysInfoLogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2)
)

# Managed Objects groups

csilGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 1)
)
csilGlobalConfigGroup.setObjects(
    ("CISCO-SYS-INFO-LOG-MIB", "csilSysInfoLogEnabled")
)
if mibBuilder.loadTexts:
    csilGlobalConfigGroup.setStatus("current")

csilServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 2)
)
csilServerConfigGroup.setObjects(
      *(("CISCO-SYS-INFO-LOG-MIB", "csilMaxServerAllowed"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilMaxProfilePerServerAllowed"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilServerAddress"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilServerAddressType"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilServerProfileIndex"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilServerProtocol"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilServerInterval"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilServerLoggingFileName"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilServerRcpUserName"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilServerLastStatus"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilServerRowStatus"))
)
if mibBuilder.loadTexts:
    csilServerConfigGroup.setStatus("current")

csilCommandConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 3)
)
csilCommandConfigGroup.setObjects(
      *(("CISCO-SYS-INFO-LOG-MIB", "csilMaxCommandPerProfile"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilCommandString"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilCommandExecOrder"),
        ("CISCO-SYS-INFO-LOG-MIB", "csilCommandStatus"))
)
if mibBuilder.loadTexts:
    csilCommandConfigGroup.setStatus("current")

csilNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 4)
)
csilNotifControlGroup.setObjects(
    ("CISCO-SYS-INFO-LOG-MIB", "csilSysInfoLogNotifEnabled")
)
if mibBuilder.loadTexts:
    csilNotifControlGroup.setStatus("current")


# Notification objects

csilLoggingFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 0, 1)
)
csilLoggingFailNotif.setObjects(
    ("CISCO-SYS-INFO-LOG-MIB", "csilServerLastStatus")
)
if mibBuilder.loadTexts:
    csilLoggingFailNotif.setStatus(
        "current"
    )


# Notifications groups

csilLoggingFailNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 2, 5)
)
csilLoggingFailNotifGroup.setObjects(
    ("CISCO-SYS-INFO-LOG-MIB", "csilLoggingFailNotif")
)
if mibBuilder.loadTexts:
    csilLoggingFailNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSysInfoLogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 330, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSysInfoLogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SYS-INFO-LOG-MIB",
    **{"ciscoSysInfoLogMIB": ciscoSysInfoLogMIB,
       "ciscoSysInfoLogMIBNotifs": ciscoSysInfoLogMIBNotifs,
       "csilLoggingFailNotif": csilLoggingFailNotif,
       "ciscoSysInfoLogMIBObjects": ciscoSysInfoLogMIBObjects,
       "csilGlobalConfig": csilGlobalConfig,
       "csilSysInfoLogEnabled": csilSysInfoLogEnabled,
       "csilSysInfoLogNotifEnabled": csilSysInfoLogNotifEnabled,
       "csilServerConfig": csilServerConfig,
       "csilMaxServerAllowed": csilMaxServerAllowed,
       "csilMaxProfilePerServerAllowed": csilMaxProfilePerServerAllowed,
       "csilServerTable": csilServerTable,
       "csilServerEntry": csilServerEntry,
       "csilServerIndex": csilServerIndex,
       "csilServerAddressType": csilServerAddressType,
       "csilServerAddress": csilServerAddress,
       "csilServerProfileIndex": csilServerProfileIndex,
       "csilServerProtocol": csilServerProtocol,
       "csilServerRcpUserName": csilServerRcpUserName,
       "csilServerInterval": csilServerInterval,
       "csilServerLoggingFileName": csilServerLoggingFileName,
       "csilServerLastStatus": csilServerLastStatus,
       "csilServerRowStatus": csilServerRowStatus,
       "csilCommandConfig": csilCommandConfig,
       "csilMaxCommandPerProfile": csilMaxCommandPerProfile,
       "csilCommandsTable": csilCommandsTable,
       "csilCommandsEntry": csilCommandsEntry,
       "csilCommandProfileIndex": csilCommandProfileIndex,
       "csilCommandIndex": csilCommandIndex,
       "csilCommandString": csilCommandString,
       "csilCommandExecOrder": csilCommandExecOrder,
       "csilCommandStatus": csilCommandStatus,
       "ciscoSysInfoLogMIBConform": ciscoSysInfoLogMIBConform,
       "ciscoSysInfoLogMIBCompliances": ciscoSysInfoLogMIBCompliances,
       "ciscoSysInfoLogMIBCompliance": ciscoSysInfoLogMIBCompliance,
       "ciscoSysInfoLogMIBGroups": ciscoSysInfoLogMIBGroups,
       "csilGlobalConfigGroup": csilGlobalConfigGroup,
       "csilServerConfigGroup": csilServerConfigGroup,
       "csilCommandConfigGroup": csilCommandConfigGroup,
       "csilNotifControlGroup": csilNotifControlGroup,
       "csilLoggingFailNotifGroup": csilLoggingFailNotifGroup}
)
