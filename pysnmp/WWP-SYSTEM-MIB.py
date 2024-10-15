# SNMP MIB module (WWP-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:26 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2)
)
wwpSystemMIB.setRevisions(
        ("2003-03-11 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpSystemMIBObjects_ObjectIdentity = ObjectIdentity
wwpSystemMIBObjects = _WwpSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1)
)
_WwpSystemClock_ObjectIdentity = ObjectIdentity
wwpSystemClock = _WwpSystemClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 1)
)
_WwpSysClockDateTime_Type = DateAndTime
_WwpSysClockDateTime_Object = MibScalar
wwpSysClockDateTime = _WwpSysClockDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 1, 1),
    _WwpSysClockDateTime_Type()
)
wwpSysClockDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSysClockDateTime.setStatus("current")


class _WwpSysClockTimeOffset_Type(Integer32):
    """Custom type wwpSysClockTimeOffset based on Integer32"""
    defaultValue = 0


_WwpSysClockTimeOffset_Object = MibScalar
wwpSysClockTimeOffset = _WwpSysClockTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 1, 2),
    _WwpSysClockTimeOffset_Type()
)
wwpSysClockTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSysClockTimeOffset.setStatus("current")
_WwpSystemBootp_ObjectIdentity = ObjectIdentity
wwpSystemBootp = _WwpSystemBootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 2)
)


class _WwpSystemBootpMsgFreq_Type(Unsigned32):
    """Custom type wwpSystemBootpMsgFreq based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpSystemBootpMsgFreq_Type.__name__ = "Unsigned32"
_WwpSystemBootpMsgFreq_Object = MibScalar
wwpSystemBootpMsgFreq = _WwpSystemBootpMsgFreq_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 2, 1),
    _WwpSystemBootpMsgFreq_Type()
)
wwpSystemBootpMsgFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemBootpMsgFreq.setStatus("deprecated")
if mibBuilder.loadTexts:
    wwpSystemBootpMsgFreq.setUnits("in seconds")
_WwpSystemAttr_ObjectIdentity = ObjectIdentity
wwpSystemAttr = _WwpSystemAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 3)
)
_WwpSystemStartMacAddr_Type = MacAddress
_WwpSystemStartMacAddr_Object = MibScalar
wwpSystemStartMacAddr = _WwpSystemStartMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 3, 1),
    _WwpSystemStartMacAddr_Type()
)
wwpSystemStartMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpSystemStartMacAddr.setStatus("current")
_WwpSystemDefaultGateway_Type = IpAddress
_WwpSystemDefaultGateway_Object = MibScalar
wwpSystemDefaultGateway = _WwpSystemDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 3, 2),
    _WwpSystemDefaultGateway_Type()
)
wwpSystemDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemDefaultGateway.setStatus("current")
_WwpSystemTftpServer_Type = IpAddress
_WwpSystemTftpServer_Object = MibScalar
wwpSystemTftpServer = _WwpSystemTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 3, 3),
    _WwpSystemTftpServer_Type()
)
wwpSystemTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemTftpServer.setStatus("current")
_WwpSystemBootFile_Type = DisplayString
_WwpSystemBootFile_Object = MibScalar
wwpSystemBootFile = _WwpSystemBootFile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 3, 4),
    _WwpSystemBootFile_Type()
)
wwpSystemBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemBootFile.setStatus("current")
_WwpSystemInterfaceHostName_Type = DisplayString
_WwpSystemInterfaceHostName_Object = MibScalar
wwpSystemInterfaceHostName = _WwpSystemInterfaceHostName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 3, 5),
    _WwpSystemInterfaceHostName_Type()
)
wwpSystemInterfaceHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemInterfaceHostName.setStatus("current")
_WwpSystemCfg_ObjectIdentity = ObjectIdentity
wwpSystemCfg = _WwpSystemCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 4)
)


class _WwpSystemCfgControl_Type(Integer32):
    """Custom type wwpSystemCfgControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mfgDefaultCfg", 4),
          ("none", 0),
          ("save", 1),
          ("updatePasswords", 2),
          ("updateSnmpCfg", 3))
    )


_WwpSystemCfgControl_Type.__name__ = "Integer32"
_WwpSystemCfgControl_Object = MibScalar
wwpSystemCfgControl = _WwpSystemCfgControl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 4, 1),
    _WwpSystemCfgControl_Type()
)
wwpSystemCfgControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemCfgControl.setStatus("current")
_WwpSystemCfgFilepath_Type = DisplayString
_WwpSystemCfgFilepath_Object = MibScalar
wwpSystemCfgFilepath = _WwpSystemCfgFilepath_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 4, 2),
    _WwpSystemCfgFilepath_Type()
)
wwpSystemCfgFilepath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpSystemCfgFilepath.setStatus("current")
_WwpSystemDebug_ObjectIdentity = ObjectIdentity
wwpSystemDebug = _WwpSystemDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 5)
)


class _WwpSystemConsolePortEnable_Type(TruthValue):
    """Custom type wwpSystemConsolePortEnable based on TruthValue"""


_WwpSystemConsolePortEnable_Object = MibScalar
wwpSystemConsolePortEnable = _WwpSystemConsolePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 1, 5, 1),
    _WwpSystemConsolePortEnable_Type()
)
wwpSystemConsolePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSystemConsolePortEnable.setStatus("current")
_WwpSystemMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpSystemMIBNotificationPrefix = _WwpSystemMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 2)
)
_WwpSystemMIBNotifications_ObjectIdentity = ObjectIdentity
wwpSystemMIBNotifications = _WwpSystemMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 2, 0)
)
_WwpSystemMIBConformance_ObjectIdentity = ObjectIdentity
wwpSystemMIBConformance = _WwpSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 3)
)
_WwpSystemMIBCompliances_ObjectIdentity = ObjectIdentity
wwpSystemMIBCompliances = _WwpSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 3, 1)
)
_WwpSystemMIBGroups_ObjectIdentity = ObjectIdentity
wwpSystemMIBGroups = _WwpSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 2, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-SYSTEM-MIB",
    **{"wwpSystemMIB": wwpSystemMIB,
       "wwpSystemMIBObjects": wwpSystemMIBObjects,
       "wwpSystemClock": wwpSystemClock,
       "wwpSysClockDateTime": wwpSysClockDateTime,
       "wwpSysClockTimeOffset": wwpSysClockTimeOffset,
       "wwpSystemBootp": wwpSystemBootp,
       "wwpSystemBootpMsgFreq": wwpSystemBootpMsgFreq,
       "wwpSystemAttr": wwpSystemAttr,
       "wwpSystemStartMacAddr": wwpSystemStartMacAddr,
       "wwpSystemDefaultGateway": wwpSystemDefaultGateway,
       "wwpSystemTftpServer": wwpSystemTftpServer,
       "wwpSystemBootFile": wwpSystemBootFile,
       "wwpSystemInterfaceHostName": wwpSystemInterfaceHostName,
       "wwpSystemCfg": wwpSystemCfg,
       "wwpSystemCfgControl": wwpSystemCfgControl,
       "wwpSystemCfgFilepath": wwpSystemCfgFilepath,
       "wwpSystemDebug": wwpSystemDebug,
       "wwpSystemConsolePortEnable": wwpSystemConsolePortEnable,
       "wwpSystemMIBNotificationPrefix": wwpSystemMIBNotificationPrefix,
       "wwpSystemMIBNotifications": wwpSystemMIBNotifications,
       "wwpSystemMIBConformance": wwpSystemMIBConformance,
       "wwpSystemMIBCompliances": wwpSystemMIBCompliances,
       "wwpSystemMIBGroups": wwpSystemMIBGroups}
)
