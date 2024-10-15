# SNMP MIB module (OPTIX-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-OID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:27 2024
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
 enterprises,
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
    "enterprises",
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

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25)
)
_OptixCommon_ObjectIdentity = ObjectIdentity
optixCommon = _OptixCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3)
)
_OptixCommonSdh_ObjectIdentity = ObjectIdentity
optixCommonSdh = _OptixCommonSdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 10)
)
_OptixCommonSonet_ObjectIdentity = ObjectIdentity
optixCommonSonet = _OptixCommonSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20)
)
_OptixProvision_ObjectIdentity = ObjectIdentity
optixProvision = _OptixProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4)
)
_OptixProvisionSdh_ObjectIdentity = ObjectIdentity
optixProvisionSdh = _OptixProvisionSdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 10)
)
_OptixProvisionSonet_ObjectIdentity = ObjectIdentity
optixProvisionSonet = _OptixProvisionSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-OID-MIB",
    **{"huawei": huawei,
       "products": products,
       "transmission": transmission,
       "optixCommon": optixCommon,
       "optixCommonSdh": optixCommonSdh,
       "optixCommonSonet": optixCommonSonet,
       "optixProvision": optixProvision,
       "optixProvisionSdh": optixProvisionSdh,
       "optixProvisionSonet": optixProvisionSonet}
)
