# SNMP MIB module (HP-ICF-AUTORUN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-AUTORUN
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:05 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfAutorun = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfAutorunConfig_ObjectIdentity = ObjectIdentity
hpicfAutorunConfig = _HpicfAutorunConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1)
)
_HpicfUsbAutorunEnable_Type = TruthValue
_HpicfUsbAutorunEnable_Object = MibScalar
hpicfUsbAutorunEnable = _HpicfUsbAutorunEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1, 1),
    _HpicfUsbAutorunEnable_Type()
)
hpicfUsbAutorunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsbAutorunEnable.setStatus("current")
_HpicfUsbAutorunSecureMode_Type = TruthValue
_HpicfUsbAutorunSecureMode_Object = MibScalar
hpicfUsbAutorunSecureMode = _HpicfUsbAutorunSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1, 2),
    _HpicfUsbAutorunSecureMode_Type()
)
hpicfUsbAutorunSecureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsbAutorunSecureMode.setStatus("current")


class _HpicfUsbAutorunEncryptionKey_Type(SnmpAdminString):
    """Custom type hpicfUsbAutorunEncryptionKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpicfUsbAutorunEncryptionKey_Type.__name__ = "SnmpAdminString"
_HpicfUsbAutorunEncryptionKey_Object = MibScalar
hpicfUsbAutorunEncryptionKey = _HpicfUsbAutorunEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 1, 3),
    _HpicfUsbAutorunEncryptionKey_Type()
)
hpicfUsbAutorunEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUsbAutorunEncryptionKey.setStatus("current")
_HpicfAutorunConformance_ObjectIdentity = ObjectIdentity
hpicfAutorunConformance = _HpicfAutorunConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2)
)
_HpicfAutorunCompliances_ObjectIdentity = ObjectIdentity
hpicfAutorunCompliances = _HpicfAutorunCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 1)
)
_HpicfAutorunGroups_ObjectIdentity = ObjectIdentity
hpicfAutorunGroups = _HpicfAutorunGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 2)
)

# Managed Objects groups

hpicfAutorunConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 2, 1)
)
hpicfAutorunConfigGroup.setObjects(
      *(("HP-ICF-AUTORUN", "hpicfUsbAutorunEnable"),
        ("HP-ICF-AUTORUN", "hpicfUsbAutorunSecureMode"),
        ("HP-ICF-AUTORUN", "hpicfUsbAutorunEncryptionKey"))
)
if mibBuilder.loadTexts:
    hpicfAutorunConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfAutorunCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfAutorunCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-AUTORUN",
    **{"hpicfAutorun": hpicfAutorun,
       "hpicfAutorunConfig": hpicfAutorunConfig,
       "hpicfUsbAutorunEnable": hpicfUsbAutorunEnable,
       "hpicfUsbAutorunSecureMode": hpicfUsbAutorunSecureMode,
       "hpicfUsbAutorunEncryptionKey": hpicfUsbAutorunEncryptionKey,
       "hpicfAutorunConformance": hpicfAutorunConformance,
       "hpicfAutorunCompliances": hpicfAutorunCompliances,
       "hpicfAutorunCompliance": hpicfAutorunCompliance,
       "hpicfAutorunGroups": hpicfAutorunGroups,
       "hpicfAutorunConfigGroup": hpicfAutorunConfigGroup}
)
