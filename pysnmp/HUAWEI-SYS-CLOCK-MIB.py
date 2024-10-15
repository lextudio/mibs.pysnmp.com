# SNMP MIB module (HUAWEI-SYS-CLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SYS-CLOCK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:05 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hwSysClockMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205)
)
hwSysClockMIB.setRevisions(
        ("2009-07-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HuaweiClockObjects_ObjectIdentity = ObjectIdentity
huaweiClockObjects = _HuaweiClockObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 1)
)
_HwLocalClock_Type = OctetString
_HwLocalClock_Object = MibScalar
hwLocalClock = _HwLocalClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 1, 1),
    _HwLocalClock_Type()
)
hwLocalClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalClock.setStatus("current")
_HwUTCClock_Type = OctetString
_HwUTCClock_Object = MibScalar
hwUTCClock = _HwUTCClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 1, 2),
    _HwUTCClock_Type()
)
hwUTCClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUTCClock.setStatus("current")
_HuaweiClockNotifications_ObjectIdentity = ObjectIdentity
huaweiClockNotifications = _HuaweiClockNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 2)
)
_HuaweiClockMIBConformance_ObjectIdentity = ObjectIdentity
huaweiClockMIBConformance = _HuaweiClockMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3)
)
_HwClockMIBCompliances_ObjectIdentity = ObjectIdentity
hwClockMIBCompliances = _HwClockMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 1)
)
_HuaweiClockMIBGroups_ObjectIdentity = ObjectIdentity
huaweiClockMIBGroups = _HuaweiClockMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 2)
)

# Managed Objects groups

hwClockSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 2, 1)
)
hwClockSetGroup.setObjects(
      *(("HUAWEI-SYS-CLOCK-MIB", "hwLocalClock"),
        ("HUAWEI-SYS-CLOCK-MIB", "hwUTCClock"))
)
if mibBuilder.loadTexts:
    hwClockSetGroup.setStatus("current")


# Notification objects

hwClockChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 2, 1)
)
hwClockChanged.setObjects(
    ("HUAWEI-SYS-CLOCK-MIB", "hwUTCClock")
)
if mibBuilder.loadTexts:
    hwClockChanged.setStatus(
        "current"
    )


# Notifications groups

hwClockNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 2, 2)
)
hwClockNotificationGroup.setObjects(
    ("HUAWEI-SYS-CLOCK-MIB", "hwClockChanged")
)
if mibBuilder.loadTexts:
    hwClockNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwClockMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 205, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwClockMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SYS-CLOCK-MIB",
    **{"hwSysClockMIB": hwSysClockMIB,
       "huaweiClockObjects": huaweiClockObjects,
       "hwLocalClock": hwLocalClock,
       "hwUTCClock": hwUTCClock,
       "huaweiClockNotifications": huaweiClockNotifications,
       "hwClockChanged": hwClockChanged,
       "huaweiClockMIBConformance": huaweiClockMIBConformance,
       "hwClockMIBCompliances": hwClockMIBCompliances,
       "hwClockMIBCompliance": hwClockMIBCompliance,
       "huaweiClockMIBGroups": huaweiClockMIBGroups,
       "hwClockSetGroup": hwClockSetGroup,
       "hwClockNotificationGroup": hwClockNotificationGroup}
)
