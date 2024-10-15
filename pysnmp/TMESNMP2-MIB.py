# SNMP MIB module (TMESNMP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TMESNMP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:23 2024
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

(tme,) = mibBuilder.importSymbols(
    "Papouch-SMI",
    "tme")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vars_ObjectIdentity = ObjectIdentity
vars = _Vars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 1, 1)
)
_Int_temperature_Type = Integer32
_Int_temperature_Object = MibScalar
int_temperature = _Int_temperature_Object(
    (1, 3, 6, 1, 4, 1, 18248, 1, 1, 1),
    _Int_temperature_Type()
)
int_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    int_temperature.setStatus("current")
_String_temperature_Type = DisplayString
_String_temperature_Object = MibScalar
string_temperature = _String_temperature_Object(
    (1, 3, 6, 1, 4, 1, 18248, 1, 1, 2),
    _String_temperature_Type()
)
string_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    string_temperature.setStatus("current")
_Device_name_Type = DisplayString
_Device_name_Object = MibScalar
device_name = _Device_name_Object(
    (1, 3, 6, 1, 4, 1, 18248, 1, 1, 3),
    _Device_name_Type()
)
device_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_name.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 1, 2)
)
_Int_temperature_t_Type = Integer32
_Int_temperature_t_Object = MibScalar
int_temperature_t = _Int_temperature_t_Object(
    (1, 3, 6, 1, 4, 1, 18248, 1, 2, 1),
    _Int_temperature_t_Type()
)
int_temperature_t.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    int_temperature_t.setStatus("current")
_String_temperature_t_Type = DisplayString
_String_temperature_t_Object = MibScalar
string_temperature_t = _String_temperature_t_Object(
    (1, 3, 6, 1, 4, 1, 18248, 1, 2, 2),
    _String_temperature_t_Type()
)
string_temperature_t.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    string_temperature_t.setStatus("current")
_Device_name_t_Type = DisplayString
_Device_name_t_Object = MibScalar
device_name_t = _Device_name_t_Object(
    (1, 3, 6, 1, 4, 1, 18248, 1, 2, 3),
    _Device_name_t_Type()
)
device_name_t.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_name_t.setStatus("current")
_Warning_t_Type = DisplayString
_Warning_t_Object = MibScalar
warning_t = _Warning_t_Object(
    (1, 3, 6, 1, 4, 1, 18248, 1, 2, 4),
    _Warning_t_Type()
)
warning_t.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warning_t.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TMESNMP2-MIB",
    **{"vars": vars,
       "int_temperature": int_temperature,
       "string_temperature": string_temperature,
       "device_name": device_name,
       "traps": traps,
       "int_temperature_t": int_temperature_t,
       "string_temperature_t": string_temperature_t,
       "device_name_t": device_name_t,
       "warning_t": warning_t}
)
