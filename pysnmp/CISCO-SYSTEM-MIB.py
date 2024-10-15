# SNMP MIB module (CISCO-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:28 2024
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

(CountryCode,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CountryCode")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131)
)
ciscoSystemMIB.setRevisions(
        ("2007-09-16 00:00",
         "2007-05-29 00:00",
         "2001-06-22 00:00",
         "2000-01-25 17:00",
         "1999-02-02 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSystemMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSystemMIBObjects = _CiscoSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1)
)
_CsyClock_ObjectIdentity = ObjectIdentity
csyClock = _CsyClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 1)
)
_CsyClockDateAndTime_Type = DateAndTime
_CsyClockDateAndTime_Object = MibScalar
csyClockDateAndTime = _CsyClockDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 1, 1),
    _CsyClockDateAndTime_Type()
)
csyClockDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csyClockDateAndTime.setStatus("current")
_CsyClockLostOnReboot_Type = TruthValue
_CsyClockLostOnReboot_Object = MibScalar
csyClockLostOnReboot = _CsyClockLostOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 1, 2),
    _CsyClockLostOnReboot_Type()
)
csyClockLostOnReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csyClockLostOnReboot.setStatus("current")
_CsyLocation_ObjectIdentity = ObjectIdentity
csyLocation = _CsyLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 2)
)
_CsyLocationCountry_Type = CountryCode
_CsyLocationCountry_Object = MibScalar
csyLocationCountry = _CsyLocationCountry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 2, 1),
    _CsyLocationCountry_Type()
)
csyLocationCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csyLocationCountry.setStatus("current")
_CsySummerTime_ObjectIdentity = ObjectIdentity
csySummerTime = _CsySummerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3)
)
_CsySummerTimeStatus_Type = TruthValue
_CsySummerTimeStatus_Object = MibScalar
csySummerTimeStatus = _CsySummerTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 1),
    _CsySummerTimeStatus_Type()
)
csySummerTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csySummerTimeStatus.setStatus("current")


class _CsySummerTimeOffset_Type(Integer32):
    """Custom type csySummerTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_CsySummerTimeOffset_Type.__name__ = "Integer32"
_CsySummerTimeOffset_Object = MibScalar
csySummerTimeOffset = _CsySummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 2),
    _CsySummerTimeOffset_Type()
)
csySummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csySummerTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    csySummerTimeOffset.setUnits("Minutes")


class _CsySummerTimeRecurringStart_Type(OctetString):
    """Custom type csySummerTimeRecurringStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CsySummerTimeRecurringStart_Type.__name__ = "OctetString"
_CsySummerTimeRecurringStart_Object = MibScalar
csySummerTimeRecurringStart = _CsySummerTimeRecurringStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 3),
    _CsySummerTimeRecurringStart_Type()
)
csySummerTimeRecurringStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csySummerTimeRecurringStart.setStatus("current")


class _CsySummerTimeRecurringEnd_Type(OctetString):
    """Custom type csySummerTimeRecurringEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CsySummerTimeRecurringEnd_Type.__name__ = "OctetString"
_CsySummerTimeRecurringEnd_Object = MibScalar
csySummerTimeRecurringEnd = _CsySummerTimeRecurringEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 4),
    _CsySummerTimeRecurringEnd_Type()
)
csySummerTimeRecurringEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csySummerTimeRecurringEnd.setStatus("current")


class _CsyStandardTmZnGMTOffset_Type(Integer32):
    """Custom type csyStandardTmZnGMTOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 720),
    )


_CsyStandardTmZnGMTOffset_Type.__name__ = "Integer32"
_CsyStandardTmZnGMTOffset_Object = MibScalar
csyStandardTmZnGMTOffset = _CsyStandardTmZnGMTOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 5),
    _CsyStandardTmZnGMTOffset_Type()
)
csyStandardTmZnGMTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csyStandardTmZnGMTOffset.setStatus("current")
if mibBuilder.loadTexts:
    csyStandardTmZnGMTOffset.setUnits("minutes")


class _CsySummerTmZnGMTOffset_Type(Integer32):
    """Custom type csySummerTmZnGMTOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 720),
    )


_CsySummerTmZnGMTOffset_Type.__name__ = "Integer32"
_CsySummerTmZnGMTOffset_Object = MibScalar
csySummerTmZnGMTOffset = _CsySummerTmZnGMTOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 3, 6),
    _CsySummerTmZnGMTOffset_Type()
)
csySummerTmZnGMTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csySummerTmZnGMTOffset.setStatus("current")
if mibBuilder.loadTexts:
    csySummerTmZnGMTOffset.setUnits("minutes")
_CsyScheduledReset_ObjectIdentity = ObjectIdentity
csyScheduledReset = _CsyScheduledReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 4)
)
_CsyScheduledResetTime_Type = DateAndTime
_CsyScheduledResetTime_Object = MibScalar
csyScheduledResetTime = _CsyScheduledResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 4, 1),
    _CsyScheduledResetTime_Type()
)
csyScheduledResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csyScheduledResetTime.setStatus("current")


class _CsyScheduledResetAction_Type(Integer32):
    """Custom type csyScheduledResetAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("resetMinDown", 2))
    )


_CsyScheduledResetAction_Type.__name__ = "Integer32"
_CsyScheduledResetAction_Object = MibScalar
csyScheduledResetAction = _CsyScheduledResetAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 4, 2),
    _CsyScheduledResetAction_Type()
)
csyScheduledResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csyScheduledResetAction.setStatus("current")
_CsyScheduledResetReason_Type = DisplayString
_CsyScheduledResetReason_Object = MibScalar
csyScheduledResetReason = _CsyScheduledResetReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 4, 3),
    _CsyScheduledResetReason_Type()
)
csyScheduledResetReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csyScheduledResetReason.setStatus("current")
_CsySnmpAuthentication_ObjectIdentity = ObjectIdentity
csySnmpAuthentication = _CsySnmpAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 5)
)
_CsySnmpAuthFail_Type = Counter32
_CsySnmpAuthFail_Object = MibScalar
csySnmpAuthFail = _CsySnmpAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 5, 1),
    _CsySnmpAuthFail_Type()
)
csySnmpAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csySnmpAuthFail.setStatus("current")
_CsySnmpAuthFailAddressType_Type = InetAddressType
_CsySnmpAuthFailAddressType_Object = MibScalar
csySnmpAuthFailAddressType = _CsySnmpAuthFailAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 5, 2),
    _CsySnmpAuthFailAddressType_Type()
)
csySnmpAuthFailAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csySnmpAuthFailAddressType.setStatus("current")
_CsySnmpAuthFailAddress_Type = InetAddress
_CsySnmpAuthFailAddress_Object = MibScalar
csySnmpAuthFailAddress = _CsySnmpAuthFailAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 5, 3),
    _CsySnmpAuthFailAddress_Type()
)
csySnmpAuthFailAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csySnmpAuthFailAddress.setStatus("current")
_CsyGeneral_ObjectIdentity = ObjectIdentity
csyGeneral = _CsyGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 6)
)


class _CsyNotificationsEnable_Type(TruthValue):
    """Custom type csyNotificationsEnable based on TruthValue"""


_CsyNotificationsEnable_Object = MibScalar
csyNotificationsEnable = _CsyNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 1, 6, 1),
    _CsyNotificationsEnable_Type()
)
csyNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csyNotificationsEnable.setStatus("current")
_CiscoSystemMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoSystemMIBNotificationPrefix = _CiscoSystemMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 2)
)
_CiscoSystemMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSystemMIBNotifications = _CiscoSystemMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 2, 0)
)
_CiscoSystemMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSystemMIBConformance = _CiscoSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3)
)
_CiscoSystemMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSystemMIBCompliances = _CiscoSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1)
)
_CiscoSystemMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSystemMIBGroups = _CiscoSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2)
)

# Managed Objects groups

ciscoSystemClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 1)
)
ciscoSystemClockGroup.setObjects(
      *(("CISCO-SYSTEM-MIB", "csyClockDateAndTime"),
        ("CISCO-SYSTEM-MIB", "csyClockLostOnReboot"))
)
if mibBuilder.loadTexts:
    ciscoSystemClockGroup.setStatus("current")

ciscoSystemLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 2)
)
ciscoSystemLocationGroup.setObjects(
    ("CISCO-SYSTEM-MIB", "csyLocationCountry")
)
if mibBuilder.loadTexts:
    ciscoSystemLocationGroup.setStatus("current")

ciscoSystemSummerTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 3)
)
ciscoSystemSummerTimeGroup.setObjects(
      *(("CISCO-SYSTEM-MIB", "csySummerTimeStatus"),
        ("CISCO-SYSTEM-MIB", "csySummerTimeOffset"),
        ("CISCO-SYSTEM-MIB", "csySummerTimeRecurringStart"),
        ("CISCO-SYSTEM-MIB", "csySummerTimeRecurringEnd"))
)
if mibBuilder.loadTexts:
    ciscoSystemSummerTimeGroup.setStatus("deprecated")

ciscoSystemScheduledResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 4)
)
ciscoSystemScheduledResetGroup.setObjects(
      *(("CISCO-SYSTEM-MIB", "csyScheduledResetTime"),
        ("CISCO-SYSTEM-MIB", "csyScheduledResetAction"),
        ("CISCO-SYSTEM-MIB", "csyScheduledResetReason"))
)
if mibBuilder.loadTexts:
    ciscoSystemScheduledResetGroup.setStatus("current")

ciscoSystemSnmpAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 5)
)
ciscoSystemSnmpAuthGroup.setObjects(
      *(("CISCO-SYSTEM-MIB", "csySnmpAuthFail"),
        ("CISCO-SYSTEM-MIB", "csySnmpAuthFailAddressType"),
        ("CISCO-SYSTEM-MIB", "csySnmpAuthFailAddress"))
)
if mibBuilder.loadTexts:
    ciscoSystemSnmpAuthGroup.setStatus("current")

ciscoSystemGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 6)
)
ciscoSystemGeneralGroup.setObjects(
    ("CISCO-SYSTEM-MIB", "csyNotificationsEnable")
)
if mibBuilder.loadTexts:
    ciscoSystemGeneralGroup.setStatus("current")

ciscoSystemSummerTimeGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 8)
)
ciscoSystemSummerTimeGroupRev1.setObjects(
      *(("CISCO-SYSTEM-MIB", "csySummerTimeStatus"),
        ("CISCO-SYSTEM-MIB", "csySummerTimeOffset"),
        ("CISCO-SYSTEM-MIB", "csySummerTimeRecurringStart"),
        ("CISCO-SYSTEM-MIB", "csySummerTimeRecurringEnd"),
        ("CISCO-SYSTEM-MIB", "csyStandardTmZnGMTOffset"),
        ("CISCO-SYSTEM-MIB", "csySummerTmZnGMTOffset"))
)
if mibBuilder.loadTexts:
    ciscoSystemSummerTimeGroupRev1.setStatus("current")


# Notification objects

ciscoSystemClockChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 2, 0, 1)
)
ciscoSystemClockChanged.setObjects(
    ("CISCO-SYSTEM-MIB", "csyClockDateAndTime")
)
if mibBuilder.loadTexts:
    ciscoSystemClockChanged.setStatus(
        "current"
    )


# Notifications groups

ciscoSystemNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 2, 7)
)
ciscoSystemNotificationsGroup.setObjects(
    ("CISCO-SYSTEM-MIB", "ciscoSystemClockChanged")
)
if mibBuilder.loadTexts:
    ciscoSystemNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSystemMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSystemMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSystemMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoSystemMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSystemMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoSystemMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 131, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSystemMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SYSTEM-MIB",
    **{"ciscoSystemMIB": ciscoSystemMIB,
       "ciscoSystemMIBObjects": ciscoSystemMIBObjects,
       "csyClock": csyClock,
       "csyClockDateAndTime": csyClockDateAndTime,
       "csyClockLostOnReboot": csyClockLostOnReboot,
       "csyLocation": csyLocation,
       "csyLocationCountry": csyLocationCountry,
       "csySummerTime": csySummerTime,
       "csySummerTimeStatus": csySummerTimeStatus,
       "csySummerTimeOffset": csySummerTimeOffset,
       "csySummerTimeRecurringStart": csySummerTimeRecurringStart,
       "csySummerTimeRecurringEnd": csySummerTimeRecurringEnd,
       "csyStandardTmZnGMTOffset": csyStandardTmZnGMTOffset,
       "csySummerTmZnGMTOffset": csySummerTmZnGMTOffset,
       "csyScheduledReset": csyScheduledReset,
       "csyScheduledResetTime": csyScheduledResetTime,
       "csyScheduledResetAction": csyScheduledResetAction,
       "csyScheduledResetReason": csyScheduledResetReason,
       "csySnmpAuthentication": csySnmpAuthentication,
       "csySnmpAuthFail": csySnmpAuthFail,
       "csySnmpAuthFailAddressType": csySnmpAuthFailAddressType,
       "csySnmpAuthFailAddress": csySnmpAuthFailAddress,
       "csyGeneral": csyGeneral,
       "csyNotificationsEnable": csyNotificationsEnable,
       "ciscoSystemMIBNotificationPrefix": ciscoSystemMIBNotificationPrefix,
       "ciscoSystemMIBNotifications": ciscoSystemMIBNotifications,
       "ciscoSystemClockChanged": ciscoSystemClockChanged,
       "ciscoSystemMIBConformance": ciscoSystemMIBConformance,
       "ciscoSystemMIBCompliances": ciscoSystemMIBCompliances,
       "ciscoSystemMIBCompliance": ciscoSystemMIBCompliance,
       "ciscoSystemMIBCompliance2": ciscoSystemMIBCompliance2,
       "ciscoSystemMIBCompliance3": ciscoSystemMIBCompliance3,
       "ciscoSystemMIBCompliance4": ciscoSystemMIBCompliance4,
       "ciscoSystemMIBGroups": ciscoSystemMIBGroups,
       "ciscoSystemClockGroup": ciscoSystemClockGroup,
       "ciscoSystemLocationGroup": ciscoSystemLocationGroup,
       "ciscoSystemSummerTimeGroup": ciscoSystemSummerTimeGroup,
       "ciscoSystemScheduledResetGroup": ciscoSystemScheduledResetGroup,
       "ciscoSystemSnmpAuthGroup": ciscoSystemSnmpAuthGroup,
       "ciscoSystemGeneralGroup": ciscoSystemGeneralGroup,
       "ciscoSystemNotificationsGroup": ciscoSystemNotificationsGroup,
       "ciscoSystemSummerTimeGroupRev1": ciscoSystemSummerTimeGroupRev1}
)
