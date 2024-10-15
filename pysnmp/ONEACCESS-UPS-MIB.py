# SNMP MIB module (ONEACCESS-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-UPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:06 2024
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

(oacExpIMManagement,) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMManagement")

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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

oacUpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacUpsMIBObjects_ObjectIdentity = ObjectIdentity
oacUpsMIBObjects = _OacUpsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1)
)
_OacUpsBattery_ObjectIdentity = ObjectIdentity
oacUpsBattery = _OacUpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 1)
)


class _OacUpsBatteryStatus_Type(Integer32):
    """Custom type oacUpsBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("batteryDepleted", 4),
          ("batteryLow", 3),
          ("batteryNormal", 2),
          ("unknown", 1))
    )


_OacUpsBatteryStatus_Type.__name__ = "Integer32"
_OacUpsBatteryStatus_Object = MibScalar
oacUpsBatteryStatus = _OacUpsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 1, 1),
    _OacUpsBatteryStatus_Type()
)
oacUpsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacUpsBatteryStatus.setStatus("current")
_OacUpsAlarm_ObjectIdentity = ObjectIdentity
oacUpsAlarm = _OacUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2)
)
_OacUpsAlarmsPresent_Type = Gauge32
_OacUpsAlarmsPresent_Object = MibScalar
oacUpsAlarmsPresent = _OacUpsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2, 1),
    _OacUpsAlarmsPresent_Type()
)
oacUpsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacUpsAlarmsPresent.setStatus("current")
_OacUpsAlarmDescr_Type = AutonomousType
_OacUpsAlarmDescr_Object = MibScalar
oacUpsAlarmDescr = _OacUpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2, 2),
    _OacUpsAlarmDescr_Type()
)
oacUpsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacUpsAlarmDescr.setStatus("current")
_OacUpsAlarmTime_Type = TimeStamp
_OacUpsAlarmTime_Object = MibScalar
oacUpsAlarmTime = _OacUpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 1, 2, 3),
    _OacUpsAlarmTime_Type()
)
oacUpsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacUpsAlarmTime.setStatus("current")
_OacUpsTraps_ObjectIdentity = ObjectIdentity
oacUpsTraps = _OacUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 2)
)

# Managed Objects groups


# Notification objects

oacUpsTrapAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 2, 0)
)
oacUpsTrapAlarmEntryAdded.setObjects(
    ("ONEACCESS-UPS-MIB", "oacUpsAlarmDescr")
)
if mibBuilder.loadTexts:
    oacUpsTrapAlarmEntryAdded.setStatus(
        "current"
    )

oacUpsTrapAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1225, 2, 1)
)
oacUpsTrapAlarmEntryRemoved.setObjects(
    ("ONEACCESS-UPS-MIB", "oacUpsAlarmDescr")
)
if mibBuilder.loadTexts:
    oacUpsTrapAlarmEntryRemoved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-UPS-MIB",
    **{"oacUpsMIB": oacUpsMIB,
       "oacUpsMIBObjects": oacUpsMIBObjects,
       "oacUpsBattery": oacUpsBattery,
       "oacUpsBatteryStatus": oacUpsBatteryStatus,
       "oacUpsAlarm": oacUpsAlarm,
       "oacUpsAlarmsPresent": oacUpsAlarmsPresent,
       "oacUpsAlarmDescr": oacUpsAlarmDescr,
       "oacUpsAlarmTime": oacUpsAlarmTime,
       "oacUpsTraps": oacUpsTraps,
       "oacUpsTrapAlarmEntryAdded": oacUpsTrapAlarmEntryAdded,
       "oacUpsTrapAlarmEntryRemoved": oacUpsTrapAlarmEntryRemoved}
)
