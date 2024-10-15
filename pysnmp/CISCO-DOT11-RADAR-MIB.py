# SNMP MIB module (CISCO-DOT11-RADAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-RADAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:55 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDot11RadarMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 627)
)
ciscoDot11RadarMIB.setRevisions(
        ("2007-05-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDot11RadarMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDot11RadarMIBNotifs = _CiscoDot11RadarMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 0)
)
_CiscoDot11RadarMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11RadarMIBObjects = _CiscoDot11RadarMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 1)
)
_CdrDot11RadarNotifConfig_ObjectIdentity = ObjectIdentity
cdrDot11RadarNotifConfig = _CdrDot11RadarNotifConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 1)
)


class _CdrChannelSwitchNotifEnabled_Type(TruthValue):
    """Custom type cdrChannelSwitchNotifEnabled based on TruthValue"""


_CdrChannelSwitchNotifEnabled_Object = MibScalar
cdrChannelSwitchNotifEnabled = _CdrChannelSwitchNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 1, 1),
    _CdrChannelSwitchNotifEnabled_Type()
)
cdrChannelSwitchNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrChannelSwitchNotifEnabled.setStatus("current")


class _CdrChannelReturnNotifEnabled_Type(TruthValue):
    """Custom type cdrChannelReturnNotifEnabled based on TruthValue"""


_CdrChannelReturnNotifEnabled_Object = MibScalar
cdrChannelReturnNotifEnabled = _CdrChannelReturnNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 1, 2),
    _CdrChannelReturnNotifEnabled_Type()
)
cdrChannelReturnNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrChannelReturnNotifEnabled.setStatus("current")
_CdrDot11RadarDetectInfo_ObjectIdentity = ObjectIdentity
cdrDot11RadarDetectInfo = _CdrDot11RadarDetectInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2)
)


class _CdrDot11NewFrequency_Type(Unsigned32):
    """Custom type cdrDot11NewFrequency based on Unsigned32"""
    defaultHexValue = 0


_CdrDot11NewFrequency_Object = MibScalar
cdrDot11NewFrequency = _CdrDot11NewFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 1),
    _CdrDot11NewFrequency_Type()
)
cdrDot11NewFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDot11NewFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cdrDot11NewFrequency.setUnits("MHz")


class _CdrDot11PreferFrequency_Type(Unsigned32):
    """Custom type cdrDot11PreferFrequency based on Unsigned32"""
    defaultHexValue = 0


_CdrDot11PreferFrequency_Object = MibScalar
cdrDot11PreferFrequency = _CdrDot11PreferFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 2),
    _CdrDot11PreferFrequency_Type()
)
cdrDot11PreferFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrDot11PreferFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cdrDot11PreferFrequency.setUnits("MHz")
_CdrChannelSwitchLastTime_Type = TimeTicks
_CdrChannelSwitchLastTime_Object = MibScalar
cdrChannelSwitchLastTime = _CdrChannelSwitchLastTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 3),
    _CdrChannelSwitchLastTime_Type()
)
cdrChannelSwitchLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrChannelSwitchLastTime.setStatus("current")
_CdrChannelReturnLastTime_Type = TimeTicks
_CdrChannelReturnLastTime_Object = MibScalar
cdrChannelReturnLastTime = _CdrChannelReturnLastTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 4),
    _CdrChannelReturnLastTime_Type()
)
cdrChannelReturnLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrChannelReturnLastTime.setStatus("current")
_CiscoDot11RadarMIBConform_ObjectIdentity = ObjectIdentity
ciscoDot11RadarMIBConform = _CiscoDot11RadarMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 2)
)
_CiscoDot11RadarMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11RadarMIBCompliances = _CiscoDot11RadarMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 1)
)
_CiscoDot11RadarMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11RadarMIBGroups = _CiscoDot11RadarMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2)
)

# Managed Objects groups

cdrDot11RadarNotifObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2, 1)
)
cdrDot11RadarNotifObjectGroup.setObjects(
      *(("CISCO-DOT11-RADAR-MIB", "cdrChannelSwitchNotifEnabled"),
        ("CISCO-DOT11-RADAR-MIB", "cdrChannelReturnNotifEnabled"))
)
if mibBuilder.loadTexts:
    cdrDot11RadarNotifObjectGroup.setStatus("current")

ciscoDot11RadarDetectInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2, 2)
)
ciscoDot11RadarDetectInfoGroup.setObjects(
      *(("CISCO-DOT11-RADAR-MIB", "cdrDot11NewFrequency"),
        ("CISCO-DOT11-RADAR-MIB", "cdrDot11PreferFrequency"),
        ("CISCO-DOT11-RADAR-MIB", "cdrChannelSwitchLastTime"),
        ("CISCO-DOT11-RADAR-MIB", "cdrChannelReturnLastTime"))
)
if mibBuilder.loadTexts:
    ciscoDot11RadarDetectInfoGroup.setStatus("current")


# Notification objects

ciscoDot11RadarChannelSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 0, 1)
)
ciscoDot11RadarChannelSwitch.setObjects(
      *(("CISCO-DOT11-RADAR-MIB", "cdrDot11NewFrequency"),
        ("CISCO-DOT11-RADAR-MIB", "cdrChannelSwitchLastTime"))
)
if mibBuilder.loadTexts:
    ciscoDot11RadarChannelSwitch.setStatus(
        "current"
    )

ciscoDot11RadarChannelReturn = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 0, 2)
)
ciscoDot11RadarChannelReturn.setObjects(
      *(("CISCO-DOT11-RADAR-MIB", "cdrDot11PreferFrequency"),
        ("CISCO-DOT11-RADAR-MIB", "cdrChannelReturnLastTime"))
)
if mibBuilder.loadTexts:
    ciscoDot11RadarChannelReturn.setStatus(
        "current"
    )


# Notifications groups

ciscoDot11RadarNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2, 3)
)
ciscoDot11RadarNotificationGroup.setObjects(
      *(("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarChannelSwitch"),
        ("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarChannelReturn"))
)
if mibBuilder.loadTexts:
    ciscoDot11RadarNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDot11RadarCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11RadarCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-RADAR-MIB",
    **{"ciscoDot11RadarMIB": ciscoDot11RadarMIB,
       "ciscoDot11RadarMIBNotifs": ciscoDot11RadarMIBNotifs,
       "ciscoDot11RadarChannelSwitch": ciscoDot11RadarChannelSwitch,
       "ciscoDot11RadarChannelReturn": ciscoDot11RadarChannelReturn,
       "ciscoDot11RadarMIBObjects": ciscoDot11RadarMIBObjects,
       "cdrDot11RadarNotifConfig": cdrDot11RadarNotifConfig,
       "cdrChannelSwitchNotifEnabled": cdrChannelSwitchNotifEnabled,
       "cdrChannelReturnNotifEnabled": cdrChannelReturnNotifEnabled,
       "cdrDot11RadarDetectInfo": cdrDot11RadarDetectInfo,
       "cdrDot11NewFrequency": cdrDot11NewFrequency,
       "cdrDot11PreferFrequency": cdrDot11PreferFrequency,
       "cdrChannelSwitchLastTime": cdrChannelSwitchLastTime,
       "cdrChannelReturnLastTime": cdrChannelReturnLastTime,
       "ciscoDot11RadarMIBConform": ciscoDot11RadarMIBConform,
       "ciscoDot11RadarMIBCompliances": ciscoDot11RadarMIBCompliances,
       "ciscoDot11RadarCompliance": ciscoDot11RadarCompliance,
       "ciscoDot11RadarMIBGroups": ciscoDot11RadarMIBGroups,
       "cdrDot11RadarNotifObjectGroup": cdrDot11RadarNotifObjectGroup,
       "ciscoDot11RadarDetectInfoGroup": ciscoDot11RadarDetectInfoGroup,
       "ciscoDot11RadarNotificationGroup": ciscoDot11RadarNotificationGroup}
)
