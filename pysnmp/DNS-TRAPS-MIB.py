# SNMP MIB module (DNS-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNS-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:24 2024
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

(bcs,) = mibBuilder.importSymbols(
    "BCS-IDENT-MIB",
    "bcs")

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


# MODULE-IDENTITY

dns = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DnsTraps_ObjectIdentity = ObjectIdentity
dnsTraps = _DnsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 1)
)
_DnsAlarms_ObjectIdentity = ObjectIdentity
dnsAlarms = _DnsAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 2)
)
_AlarmConditionNotInList_Type = Integer32
_AlarmConditionNotInList_Object = MibScalar
alarmConditionNotInList = _AlarmConditionNotInList_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 2, 20),
    _AlarmConditionNotInList_Type()
)
alarmConditionNotInList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmConditionNotInList.setStatus("current")
_AlarmConditionAlreadyInList_Type = Integer32
_AlarmConditionAlreadyInList_Object = MibScalar
alarmConditionAlreadyInList = _AlarmConditionAlreadyInList_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 2, 21),
    _AlarmConditionAlreadyInList_Type()
)
alarmConditionAlreadyInList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmConditionAlreadyInList.setStatus("current")
_AlarmConditionListFull_Type = Integer32
_AlarmConditionListFull_Object = MibScalar
alarmConditionListFull = _AlarmConditionListFull_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 2, 22),
    _AlarmConditionListFull_Type()
)
alarmConditionListFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmConditionListFull.setStatus("current")
_AlarmInvalidCaseInSwitch_Type = Integer32
_AlarmInvalidCaseInSwitch_Object = MibScalar
alarmInvalidCaseInSwitch = _AlarmInvalidCaseInSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 2, 23),
    _AlarmInvalidCaseInSwitch_Type()
)
alarmInvalidCaseInSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInvalidCaseInSwitch.setStatus("current")
_AlarmCannotCreateSemaphore_Type = Integer32
_AlarmCannotCreateSemaphore_Object = MibScalar
alarmCannotCreateSemaphore = _AlarmCannotCreateSemaphore_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 2, 24),
    _AlarmCannotCreateSemaphore_Type()
)
alarmCannotCreateSemaphore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCannotCreateSemaphore.setStatus("current")
_AlarmCannotOpenSocket_Type = Integer32
_AlarmCannotOpenSocket_Object = MibScalar
alarmCannotOpenSocket = _AlarmCannotOpenSocket_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 2, 25),
    _AlarmCannotOpenSocket_Type()
)
alarmCannotOpenSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCannotOpenSocket.setStatus("current")
_AlarmUnknownMessageReceived_Type = Integer32
_AlarmUnknownMessageReceived_Object = MibScalar
alarmUnknownMessageReceived = _AlarmUnknownMessageReceived_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 2, 26),
    _AlarmUnknownMessageReceived_Type()
)
alarmUnknownMessageReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnknownMessageReceived.setStatus("current")
_AlarmInvalidMessageReceived_Type = Integer32
_AlarmInvalidMessageReceived_Object = MibScalar
alarmInvalidMessageReceived = _AlarmInvalidMessageReceived_Object(
    (1, 3, 6, 1, 4, 1, 1166, 7, 5, 2, 27),
    _AlarmInvalidMessageReceived_Type()
)
alarmInvalidMessageReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInvalidMessageReceived.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNS-TRAPS-MIB",
    **{"dns": dns,
       "dnsTraps": dnsTraps,
       "dnsAlarms": dnsAlarms,
       "alarmConditionNotInList": alarmConditionNotInList,
       "alarmConditionAlreadyInList": alarmConditionAlreadyInList,
       "alarmConditionListFull": alarmConditionListFull,
       "alarmInvalidCaseInSwitch": alarmInvalidCaseInSwitch,
       "alarmCannotCreateSemaphore": alarmCannotCreateSemaphore,
       "alarmCannotOpenSocket": alarmCannotOpenSocket,
       "alarmUnknownMessageReceived": alarmUnknownMessageReceived,
       "alarmInvalidMessageReceived": alarmInvalidMessageReceived}
)
