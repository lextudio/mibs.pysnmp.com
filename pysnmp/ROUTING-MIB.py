# SNMP MIB module (ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ROUTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:20 2024
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

(routing,) = mibBuilder.importSymbols(
    "CORIOLIS-MIB",
    "routing")

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

routingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RouteAdvPrefixTable_Object = MibTable
routeAdvPrefixTable = _RouteAdvPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 7, 2)
)
if mibBuilder.loadTexts:
    routeAdvPrefixTable.setStatus("current")
_RouteAdvPrefixEntry_Object = MibTableRow
routeAdvPrefixEntry = _RouteAdvPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 7, 2, 1)
)
routeAdvPrefixEntry.setIndexNames(
    (0, "ROUTING-MIB", "routeAdvSummAddr"),
    (0, "ROUTING-MIB", "routeAdvSummMask"),
)
if mibBuilder.loadTexts:
    routeAdvPrefixEntry.setStatus("current")
_RouteAdvSummAddr_Type = IpAddress
_RouteAdvSummAddr_Object = MibTableColumn
routeAdvSummAddr = _RouteAdvSummAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 7, 2, 1, 1),
    _RouteAdvSummAddr_Type()
)
routeAdvSummAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeAdvSummAddr.setStatus("current")
_RouteAdvSummMask_Type = IpAddress
_RouteAdvSummMask_Object = MibTableColumn
routeAdvSummMask = _RouteAdvSummMask_Object(
    (1, 3, 6, 1, 4, 1, 5812, 7, 2, 1, 2),
    _RouteAdvSummMask_Type()
)
routeAdvSummMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeAdvSummMask.setStatus("current")


class _RouteAdvSummRowStatus_Type(Integer32):
    """Custom type routeAdvSummRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("invalid", 2))
    )


_RouteAdvSummRowStatus_Type.__name__ = "Integer32"
_RouteAdvSummRowStatus_Object = MibTableColumn
routeAdvSummRowStatus = _RouteAdvSummRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 7, 2, 1, 3),
    _RouteAdvSummRowStatus_Type()
)
routeAdvSummRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    routeAdvSummRowStatus.setStatus("current")
_RouteAdvSummRipAdminCost_Type = Integer32
_RouteAdvSummRipAdminCost_Object = MibTableColumn
routeAdvSummRipAdminCost = _RouteAdvSummRipAdminCost_Object(
    (1, 3, 6, 1, 4, 1, 5812, 7, 2, 1, 4),
    _RouteAdvSummRipAdminCost_Type()
)
routeAdvSummRipAdminCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeAdvSummRipAdminCost.setStatus("current")
_RouteAdvSummOspfAdminCost_Type = Integer32
_RouteAdvSummOspfAdminCost_Object = MibTableColumn
routeAdvSummOspfAdminCost = _RouteAdvSummOspfAdminCost_Object(
    (1, 3, 6, 1, 4, 1, 5812, 7, 2, 1, 5),
    _RouteAdvSummOspfAdminCost_Type()
)
routeAdvSummOspfAdminCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeAdvSummOspfAdminCost.setStatus("current")
_RouteAdvSummNumSuppressedRoutes_Type = Integer32
_RouteAdvSummNumSuppressedRoutes_Object = MibTableColumn
routeAdvSummNumSuppressedRoutes = _RouteAdvSummNumSuppressedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5812, 7, 2, 1, 6),
    _RouteAdvSummNumSuppressedRoutes_Type()
)
routeAdvSummNumSuppressedRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeAdvSummNumSuppressedRoutes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROUTING-MIB",
    **{"routingMIB": routingMIB,
       "routeAdvPrefixTable": routeAdvPrefixTable,
       "routeAdvPrefixEntry": routeAdvPrefixEntry,
       "routeAdvSummAddr": routeAdvSummAddr,
       "routeAdvSummMask": routeAdvSummMask,
       "routeAdvSummRowStatus": routeAdvSummRowStatus,
       "routeAdvSummRipAdminCost": routeAdvSummRipAdminCost,
       "routeAdvSummOspfAdminCost": routeAdvSummOspfAdminCost,
       "routeAdvSummNumSuppressedRoutes": routeAdvSummNumSuppressedRoutes}
)
