# SNMP MIB module (OPTIX-SONET-SYSTEM-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-SYSTEM-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:32 2024
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

(optixProvisionSonet,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixProvisionSonet")

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

optixsonetSysAttribute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OptixsonetNeType_ObjectIdentity = ObjectIdentity
optixsonetNeType = _OptixsonetNeType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1)
)
_OptixsonetVendId_Type = OctetString
_OptixsonetVendId_Object = MibScalar
optixsonetVendId = _OptixsonetVendId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1, 1),
    _OptixsonetVendId_Type()
)
optixsonetVendId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixsonetVendId.setStatus("current")
_OptixsonetDeviceType_Type = OctetString
_OptixsonetDeviceType_Object = MibScalar
optixsonetDeviceType = _OptixsonetDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1, 2),
    _OptixsonetDeviceType_Type()
)
optixsonetDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixsonetDeviceType.setStatus("current")
_OptixsonetEquipType_Type = OctetString
_OptixsonetEquipType_Object = MibScalar
optixsonetEquipType = _OptixsonetEquipType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1, 3),
    _OptixsonetEquipType_Type()
)
optixsonetEquipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixsonetEquipType.setStatus("current")
_OptixsonetNeVersion_Type = OctetString
_OptixsonetNeVersion_Object = MibScalar
optixsonetNeVersion = _OptixsonetNeVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1, 4),
    _OptixsonetNeVersion_Type()
)
optixsonetNeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optixsonetNeVersion.setStatus("current")
_OptixsonetSysAttributeConformance_ObjectIdentity = ObjectIdentity
optixsonetSysAttributeConformance = _OptixsonetSysAttributeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2)
)
_OptixsonetSysAttributeGroups_ObjectIdentity = ObjectIdentity
optixsonetSysAttributeGroups = _OptixsonetSysAttributeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2, 1)
)
_OptixsonetSysAttributeCompliances_ObjectIdentity = ObjectIdentity
optixsonetSysAttributeCompliances = _OptixsonetSysAttributeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2, 1, 1)
)
currentObjectGroup.setObjects(
      *(("OPTIX-SONET-SYSTEM-MIB-V2", "optixsonetVendId"),
        ("OPTIX-SONET-SYSTEM-MIB-V2", "optixsonetDeviceType"),
        ("OPTIX-SONET-SYSTEM-MIB-V2", "optixsonetEquipType"),
        ("OPTIX-SONET-SYSTEM-MIB-V2", "optixsonetNeVersion"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-SYSTEM-MIB-V2",
    **{"optixsonetSysAttribute": optixsonetSysAttribute,
       "optixsonetNeType": optixsonetNeType,
       "optixsonetVendId": optixsonetVendId,
       "optixsonetDeviceType": optixsonetDeviceType,
       "optixsonetEquipType": optixsonetEquipType,
       "optixsonetNeVersion": optixsonetNeVersion,
       "optixsonetSysAttributeConformance": optixsonetSysAttributeConformance,
       "optixsonetSysAttributeGroups": optixsonetSysAttributeGroups,
       "currentObjectGroup": currentObjectGroup,
       "optixsonetSysAttributeCompliances": optixsonetSysAttributeCompliances,
       "basicCompliance": basicCompliance}
)
