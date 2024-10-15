# SNMP MIB module (Unisphere-Data-Registry) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-Registry
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:37 2024
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

(usAdmin,) = mibBuilder.importSymbols(
    "Unisphere-SMI",
    "usAdmin")


# MODULE-IDENTITY

usDataAdmin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2)
)
usDataAdmin.setRevisions(
        ("2001-09-25 15:25",
         "2001-06-01 21:18")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsDataRegistry_ObjectIdentity = ObjectIdentity
usDataRegistry = _UsDataRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1)
)
if mibBuilder.loadTexts:
    usDataRegistry.setStatus("current")
_UsDataEntPhysicalType_ObjectIdentity = ObjectIdentity
usDataEntPhysicalType = _UsDataEntPhysicalType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1)
)
_UsdPcmciaFlashCard_ObjectIdentity = ObjectIdentity
usdPcmciaFlashCard = _UsdPcmciaFlashCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdPcmciaFlashCard.setStatus("current")
_Usd85MegT2FlashCard_ObjectIdentity = ObjectIdentity
usd85MegT2FlashCard = _Usd85MegT2FlashCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usd85MegT2FlashCard.setStatus("current")
_Usd220MegT2FlashCard_ObjectIdentity = ObjectIdentity
usd220MegT2FlashCard = _Usd220MegT2FlashCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usd220MegT2FlashCard.setStatus("current")
_UsdTraceRouteImplementationTypes_ObjectIdentity = ObjectIdentity
usdTraceRouteImplementationTypes = _UsdTraceRouteImplementationTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 2)
)
_UsdTraceRouteUsingIcmpProbe_ObjectIdentity = ObjectIdentity
usdTraceRouteUsingIcmpProbe = _UsdTraceRouteUsingIcmpProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdTraceRouteUsingIcmpProbe.setStatus("current")
_UsdErxRegistry_ObjectIdentity = ObjectIdentity
usdErxRegistry = _UsdErxRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 2)
)
_UsdMrxRegistry_ObjectIdentity = ObjectIdentity
usdMrxRegistry = _UsdMrxRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-Registry",
    **{"usDataAdmin": usDataAdmin,
       "usDataRegistry": usDataRegistry,
       "usDataEntPhysicalType": usDataEntPhysicalType,
       "usdPcmciaFlashCard": usdPcmciaFlashCard,
       "usd85MegT2FlashCard": usd85MegT2FlashCard,
       "usd220MegT2FlashCard": usd220MegT2FlashCard,
       "usdTraceRouteImplementationTypes": usdTraceRouteImplementationTypes,
       "usdTraceRouteUsingIcmpProbe": usdTraceRouteUsingIcmpProbe,
       "usdErxRegistry": usdErxRegistry,
       "usdMrxRegistry": usdMrxRegistry}
)
