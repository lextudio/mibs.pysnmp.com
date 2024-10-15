# SNMP MIB module (OPTIX-SONET-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-SYS-MIB
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

(optixCommonSonet,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixCommonSonet")

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

optixSonetSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30)
)
optixSonetSystem.setRevisions(
        ("2006-02-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlwMsgAll_ObjectIdentity = ObjectIdentity
alwMsgAll = _AlwMsgAll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 10)
)


class _SetMsgAll_Type(Integer32):
    """Custom type setMsgAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SetMsgAll_Type.__name__ = "Integer32"
_SetMsgAll_Object = MibScalar
setMsgAll = _SetMsgAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 10, 10),
    _SetMsgAll_Type()
)
setMsgAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsgAll.setStatus("current")
_AlwPMReptAll_ObjectIdentity = ObjectIdentity
alwPMReptAll = _AlwPMReptAll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 20)
)


class _SetPMReptAll_Type(Integer32):
    """Custom type setPMReptAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SetPMReptAll_Type.__name__ = "Integer32"
_SetPMReptAll_Object = MibScalar
setPMReptAll = _SetPMReptAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 20, 10),
    _SetPMReptAll_Type()
)
setPMReptAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPMReptAll.setStatus("current")
_OptixSonetSystemConformance_ObjectIdentity = ObjectIdentity
optixSonetSystemConformance = _OptixSonetSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30)
)
_OptixSonetSystemGroups_ObjectIdentity = ObjectIdentity
optixSonetSystemGroups = _OptixSonetSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 1)
)
_OptixSonetSystemCompliances_ObjectIdentity = ObjectIdentity
optixSonetSystemCompliances = _OptixSonetSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 2)
)

# Managed Objects groups

optixSonetObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 1, 1)
)
optixSonetObjectGroup.setObjects(
      *(("OPTIX-SONET-SYS-MIB", "setMsgAll"),
        ("OPTIX-SONET-SYS-MIB", "setPMReptAll"))
)
if mibBuilder.loadTexts:
    optixSonetObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

optixSonetBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 2, 1)
)
if mibBuilder.loadTexts:
    optixSonetBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-SYS-MIB",
    **{"optixSonetSystem": optixSonetSystem,
       "alwMsgAll": alwMsgAll,
       "setMsgAll": setMsgAll,
       "alwPMReptAll": alwPMReptAll,
       "setPMReptAll": setPMReptAll,
       "optixSonetSystemConformance": optixSonetSystemConformance,
       "optixSonetSystemGroups": optixSonetSystemGroups,
       "optixSonetObjectGroup": optixSonetObjectGroup,
       "optixSonetSystemCompliances": optixSonetSystemCompliances,
       "optixSonetBasicCompliance": optixSonetBasicCompliance}
)
