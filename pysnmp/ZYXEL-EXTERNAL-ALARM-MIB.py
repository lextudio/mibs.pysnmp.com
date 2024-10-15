# SNMP MIB module (ZYXEL-EXTERNAL-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-EXTERNAL-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:50 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelExternalAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelExternalAlarmTrapInfoObjects_ObjectIdentity = ObjectIdentity
zyxelExternalAlarmTrapInfoObjects = _ZyxelExternalAlarmTrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1)
)
_ZyExternalAlarmTrapAlarmId_Type = Integer32
_ZyExternalAlarmTrapAlarmId_Object = MibScalar
zyExternalAlarmTrapAlarmId = _ZyExternalAlarmTrapAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1, 1),
    _ZyExternalAlarmTrapAlarmId_Type()
)
zyExternalAlarmTrapAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyExternalAlarmTrapAlarmId.setStatus("current")
_ZyxelExternalAlarmNotifications_ObjectIdentity = ObjectIdentity
zyxelExternalAlarmNotifications = _ZyxelExternalAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2)
)

# Managed Objects groups


# Notification objects

zyExternalAlarmDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2, 1)
)
zyExternalAlarmDetect.setObjects(
    ("ZYXEL-EXTERNAL-ALARM-MIB", "zyExternalAlarmTrapAlarmId")
)
if mibBuilder.loadTexts:
    zyExternalAlarmDetect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-EXTERNAL-ALARM-MIB",
    **{"zyxelExternalAlarm": zyxelExternalAlarm,
       "zyxelExternalAlarmTrapInfoObjects": zyxelExternalAlarmTrapInfoObjects,
       "zyExternalAlarmTrapAlarmId": zyExternalAlarmTrapAlarmId,
       "zyxelExternalAlarmNotifications": zyxelExternalAlarmNotifications,
       "zyExternalAlarmDetect": zyExternalAlarmDetect}
)
