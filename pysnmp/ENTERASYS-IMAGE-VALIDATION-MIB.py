# SNMP MIB module (ENTERASYS-IMAGE-VALIDATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-IMAGE-VALIDATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:00 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysImageValidationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47)
)
etsysImageValidationMIB.setRevisions(
        ("2004-04-02 21:34",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysImageValidationObjects_ObjectIdentity = ObjectIdentity
etsysImageValidationObjects = _EtsysImageValidationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1)
)
_EtsysImageValidationConfig_ObjectIdentity = ObjectIdentity
etsysImageValidationConfig = _EtsysImageValidationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1)
)


class _EtsysImageValidationEnable_Type(EnabledStatus):
    """Custom type etsysImageValidationEnable based on EnabledStatus"""


_EtsysImageValidationEnable_Object = MibScalar
etsysImageValidationEnable = _EtsysImageValidationEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 1),
    _EtsysImageValidationEnable_Type()
)
etsysImageValidationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysImageValidationEnable.setStatus("current")


class _EtsysImageValidationPeriod_Type(Unsigned32):
    """Custom type etsysImageValidationPeriod based on Unsigned32"""
    defaultValue = 600


_EtsysImageValidationPeriod_Object = MibScalar
etsysImageValidationPeriod = _EtsysImageValidationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 2),
    _EtsysImageValidationPeriod_Type()
)
etsysImageValidationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysImageValidationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    etsysImageValidationPeriod.setUnits("seconds")


class _EtsysImageValidationOperations_Type(Bits):
    """Custom type etsysImageValidationOperations based on Bits"""
    namedValues = NamedValues(
        *(("etsysImageValidationConfig", 0),
          ("etsysImageValidationIcmp", 1),
          ("etsysImageValidationSnmp", 2))
    )

_EtsysImageValidationOperations_Type.__name__ = "Bits"
_EtsysImageValidationOperations_Object = MibScalar
etsysImageValidationOperations = _EtsysImageValidationOperations_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 3),
    _EtsysImageValidationOperations_Type()
)
etsysImageValidationOperations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysImageValidationOperations.setStatus("current")


class _EtsysImageValidationIcmpAddressType_Type(InetAddressType):
    """Custom type etsysImageValidationIcmpAddressType based on InetAddressType"""


_EtsysImageValidationIcmpAddressType_Object = MibScalar
etsysImageValidationIcmpAddressType = _EtsysImageValidationIcmpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 4),
    _EtsysImageValidationIcmpAddressType_Type()
)
etsysImageValidationIcmpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysImageValidationIcmpAddressType.setStatus("current")


class _EtsysImageValidationIcmpAddress_Type(InetAddress):
    """Custom type etsysImageValidationIcmpAddress based on InetAddress"""
    defaultHexValue = "00000000"


_EtsysImageValidationIcmpAddress_Object = MibScalar
etsysImageValidationIcmpAddress = _EtsysImageValidationIcmpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 5),
    _EtsysImageValidationIcmpAddress_Type()
)
etsysImageValidationIcmpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysImageValidationIcmpAddress.setStatus("current")


class _EtsysImageValidationSnmpAddressType_Type(InetAddressType):
    """Custom type etsysImageValidationSnmpAddressType based on InetAddressType"""


_EtsysImageValidationSnmpAddressType_Object = MibScalar
etsysImageValidationSnmpAddressType = _EtsysImageValidationSnmpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 6),
    _EtsysImageValidationSnmpAddressType_Type()
)
etsysImageValidationSnmpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysImageValidationSnmpAddressType.setStatus("current")


class _EtsysImageValidationSnmpAddress_Type(InetAddress):
    """Custom type etsysImageValidationSnmpAddress based on InetAddress"""
    defaultHexValue = "00000000"


_EtsysImageValidationSnmpAddress_Object = MibScalar
etsysImageValidationSnmpAddress = _EtsysImageValidationSnmpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 1, 1, 7),
    _EtsysImageValidationSnmpAddress_Type()
)
etsysImageValidationSnmpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysImageValidationSnmpAddress.setStatus("current")
_EtsysImageValidationConformance_ObjectIdentity = ObjectIdentity
etsysImageValidationConformance = _EtsysImageValidationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2)
)
_EtsysImageValidationGroups_ObjectIdentity = ObjectIdentity
etsysImageValidationGroups = _EtsysImageValidationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 1)
)
_EtsysImageValidationCompliances_ObjectIdentity = ObjectIdentity
etsysImageValidationCompliances = _EtsysImageValidationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 2)
)

# Managed Objects groups

etsysImageValidationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 1, 1)
)
etsysImageValidationConfigGroup.setObjects(
      *(("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationEnable"),
        ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationPeriod"),
        ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationOperations"),
        ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationIcmpAddressType"),
        ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationIcmpAddress"),
        ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationSnmpAddressType"),
        ("ENTERASYS-IMAGE-VALIDATION-MIB", "etsysImageValidationSnmpAddress"))
)
if mibBuilder.loadTexts:
    etsysImageValidationConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysImageValidationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 47, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysImageValidationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IMAGE-VALIDATION-MIB",
    **{"etsysImageValidationMIB": etsysImageValidationMIB,
       "etsysImageValidationObjects": etsysImageValidationObjects,
       "etsysImageValidationConfig": etsysImageValidationConfig,
       "etsysImageValidationEnable": etsysImageValidationEnable,
       "etsysImageValidationPeriod": etsysImageValidationPeriod,
       "etsysImageValidationOperations": etsysImageValidationOperations,
       "etsysImageValidationIcmpAddressType": etsysImageValidationIcmpAddressType,
       "etsysImageValidationIcmpAddress": etsysImageValidationIcmpAddress,
       "etsysImageValidationSnmpAddressType": etsysImageValidationSnmpAddressType,
       "etsysImageValidationSnmpAddress": etsysImageValidationSnmpAddress,
       "etsysImageValidationConformance": etsysImageValidationConformance,
       "etsysImageValidationGroups": etsysImageValidationGroups,
       "etsysImageValidationConfigGroup": etsysImageValidationConfigGroup,
       "etsysImageValidationCompliances": etsysImageValidationCompliances,
       "etsysImageValidationCompliance": etsysImageValidationCompliance}
)
