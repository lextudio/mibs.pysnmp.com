# SNMP MIB module (CISCO-UBE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UBE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:56 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoUbeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764)
)
ciscoUbeMIB.setRevisions(
        ("2010-11-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoUbeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoUbeMIBObjects = _CiscoUbeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 0)
)
_CubeEnabled_Type = TruthValue
_CubeEnabled_Object = MibScalar
cubeEnabled = _CubeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 1),
    _CubeEnabled_Type()
)
cubeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubeEnabled.setStatus("current")
_CubeVersion_Type = SnmpAdminString
_CubeVersion_Object = MibScalar
cubeVersion = _CubeVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 2),
    _CubeVersion_Type()
)
cubeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubeVersion.setStatus("current")


class _CubeTotalSessionAllowed_Type(Unsigned32):
    """Custom type cubeTotalSessionAllowed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_CubeTotalSessionAllowed_Type.__name__ = "Unsigned32"
_CubeTotalSessionAllowed_Object = MibScalar
cubeTotalSessionAllowed = _CubeTotalSessionAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 3),
    _CubeTotalSessionAllowed_Type()
)
cubeTotalSessionAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubeTotalSessionAllowed.setStatus("current")
if mibBuilder.loadTexts:
    cubeTotalSessionAllowed.setUnits("session")
_CiscoUbeMIBConform_ObjectIdentity = ObjectIdentity
ciscoUbeMIBConform = _CiscoUbeMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1)
)
_CiscoUbeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoUbeMIBCompliances = _CiscoUbeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1)
)
_CiscoUbeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoUbeMIBGroups = _CiscoUbeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2)
)

# Managed Objects groups

ciscoUbeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2, 1)
)
ciscoUbeMIBGroup.setObjects(
      *(("CISCO-UBE-MIB", "cubeEnabled"),
        ("CISCO-UBE-MIB", "cubeVersion"),
        ("CISCO-UBE-MIB", "cubeTotalSessionAllowed"))
)
if mibBuilder.loadTexts:
    ciscoUbeMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCubeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCubeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UBE-MIB",
    **{"ciscoUbeMIB": ciscoUbeMIB,
       "ciscoUbeMIBObjects": ciscoUbeMIBObjects,
       "cubeEnabled": cubeEnabled,
       "cubeVersion": cubeVersion,
       "cubeTotalSessionAllowed": cubeTotalSessionAllowed,
       "ciscoUbeMIBConform": ciscoUbeMIBConform,
       "ciscoUbeMIBCompliances": ciscoUbeMIBCompliances,
       "ciscoCubeMIBCompliance": ciscoCubeMIBCompliance,
       "ciscoUbeMIBGroups": ciscoUbeMIBGroups,
       "ciscoUbeMIBGroup": ciscoUbeMIBGroup}
)
