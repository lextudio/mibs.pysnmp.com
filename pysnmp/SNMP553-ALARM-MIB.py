# SNMP MIB module (SNMP553-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP553-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:13 2024
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

(snmp553s,) = mibBuilder.importSymbols(
    "SNMP553S-MGMT-MIB",
    "snmp553s")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Snmp553sTextAlarm_ObjectIdentity = ObjectIdentity
snmp553sTextAlarm = _Snmp553sTextAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 9)
)


class _Snmp553sTextAlarmMIBversion_Type(DisplayString):
    """Custom type snmp553sTextAlarmMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Snmp553sTextAlarmMIBversion_Type.__name__ = "DisplayString"
_Snmp553sTextAlarmMIBversion_Object = MibScalar
snmp553sTextAlarmMIBversion = _Snmp553sTextAlarmMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 9, 1),
    _Snmp553sTextAlarmMIBversion_Type()
)
snmp553sTextAlarmMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmp553sTextAlarmMIBversion.setStatus("mandatory")


class _Snmp553sTextAlarmGlobal_Type(Integer32):
    """Custom type snmp553sTextAlarmGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Snmp553sTextAlarmGlobal_Type.__name__ = "Integer32"
_Snmp553sTextAlarmGlobal_Object = MibScalar
snmp553sTextAlarmGlobal = _Snmp553sTextAlarmGlobal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 9, 2),
    _Snmp553sTextAlarmGlobal_Type()
)
snmp553sTextAlarmGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp553sTextAlarmGlobal.setStatus("mandatory")
_Snmp553sTextAlarmTable_Object = MibTable
snmp553sTextAlarmTable = _Snmp553sTextAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 9, 3)
)
if mibBuilder.loadTexts:
    snmp553sTextAlarmTable.setStatus("mandatory")
_Snmp553sTextAlarmEntry_Object = MibTableRow
snmp553sTextAlarmEntry = _Snmp553sTextAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 9, 3, 1)
)
snmp553sTextAlarmEntry.setIndexNames(
    (0, "SNMP553-ALARM-MIB", "alarmNumber"),
)
if mibBuilder.loadTexts:
    snmp553sTextAlarmEntry.setStatus("mandatory")
_AlarmNumber_Type = Integer32
_AlarmNumber_Object = MibTableColumn
alarmNumber = _AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 9, 3, 1, 1),
    _AlarmNumber_Type()
)
alarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNumber.setStatus("mandatory")


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibTableColumn
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 9, 3, 1, 2),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("mandatory")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 9, 3, 1, 3),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")

# Managed Objects groups


# Notification objects

snmp553sTextAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 6, 3, 0, 1)
)
snmp553sTextAlarmTrap.setObjects(
      *(("SNMP553-ALARM-MIB", "description"),
        ("SNMP553-ALARM-MIB", "status"))
)
if mibBuilder.loadTexts:
    snmp553sTextAlarmTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP553-ALARM-MIB",
    **{"snmp553sTextAlarmTrap": snmp553sTextAlarmTrap,
       "snmp553sTextAlarm": snmp553sTextAlarm,
       "snmp553sTextAlarmMIBversion": snmp553sTextAlarmMIBversion,
       "snmp553sTextAlarmGlobal": snmp553sTextAlarmGlobal,
       "snmp553sTextAlarmTable": snmp553sTextAlarmTable,
       "snmp553sTextAlarmEntry": snmp553sTextAlarmEntry,
       "alarmNumber": alarmNumber,
       "description": description,
       "status": status}
)
