# SNMP MIB module (ARUBA-VENDORTYPE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARUBA-VENDORTYPE
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:46 2024
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

(arubaMIBModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "arubaMIBModules")

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

arubaVendorTypeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1)
)
arubaVendorTypeMIB.setRevisions(
        ("2012-08-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaVendorTypeMIBObjects_ObjectIdentity = ObjectIdentity
arubaVendorTypeMIBObjects = _ArubaVendorTypeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1)
)
_ArubaSystem_ObjectIdentity = ObjectIdentity
arubaSystem = _ArubaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1)
)
_ASystemUnknown_ObjectIdentity = ObjectIdentity
aSystemUnknown = _ASystemUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 1)
)
_ASystemChassis_ObjectIdentity = ObjectIdentity
aSystemChassis = _ASystemChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 2)
)
_ASystemBackplane_ObjectIdentity = ObjectIdentity
aSystemBackplane = _ASystemBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 3)
)
_ASystemModule_ObjectIdentity = ObjectIdentity
aSystemModule = _ASystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 4)
)
_ASystemPSU_ObjectIdentity = ObjectIdentity
aSystemPSU = _ASystemPSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 5)
)
_ASystemFAN_ObjectIdentity = ObjectIdentity
aSystemFAN = _ASystemFAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 6)
)
_ASystemContainer_ObjectIdentity = ObjectIdentity
aSystemContainer = _ASystemContainer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 7)
)
_ASystemPort_ObjectIdentity = ObjectIdentity
aSystemPort = _ASystemPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 8)
)
_ASystemSensor_ObjectIdentity = ObjectIdentity
aSystemSensor = _ASystemSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBA-VENDORTYPE",
    **{"arubaVendorTypeMIB": arubaVendorTypeMIB,
       "arubaVendorTypeMIBObjects": arubaVendorTypeMIBObjects,
       "arubaSystem": arubaSystem,
       "aSystemUnknown": aSystemUnknown,
       "aSystemChassis": aSystemChassis,
       "aSystemBackplane": aSystemBackplane,
       "aSystemModule": aSystemModule,
       "aSystemPSU": aSystemPSU,
       "aSystemFAN": aSystemFAN,
       "aSystemContainer": aSystemContainer,
       "aSystemPort": aSystemPort,
       "aSystemSensor": aSystemSensor}
)
