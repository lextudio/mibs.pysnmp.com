# SNMP MIB module (DEVROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:11 2024
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

(device,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "device")

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

aniDevRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniDevRouteTable_Object = MibTable
aniDevRouteTable = _AniDevRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1)
)
if mibBuilder.loadTexts:
    aniDevRouteTable.setStatus("current")
_AniDevRouteEntry_Object = MibTableRow
aniDevRouteEntry = _AniDevRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1)
)
aniDevRouteEntry.setIndexNames(
    (0, "DEVROUTE-MIB", "aniDevRouteDest"),
    (0, "DEVROUTE-MIB", "aniDevRouteNextHop"),
    (0, "DEVROUTE-MIB", "aniDevRouteMask"),
)
if mibBuilder.loadTexts:
    aniDevRouteEntry.setStatus("current")
_AniDevRouteDest_Type = IpAddress
_AniDevRouteDest_Object = MibTableColumn
aniDevRouteDest = _AniDevRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 1),
    _AniDevRouteDest_Type()
)
aniDevRouteDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aniDevRouteDest.setStatus("current")
_AniDevRouteIfIndex_Type = Integer32
_AniDevRouteIfIndex_Object = MibTableColumn
aniDevRouteIfIndex = _AniDevRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 2),
    _AniDevRouteIfIndex_Type()
)
aniDevRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevRouteIfIndex.setStatus("current")
_AniDevRouteMetric1_Type = Integer32
_AniDevRouteMetric1_Object = MibTableColumn
aniDevRouteMetric1 = _AniDevRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 3),
    _AniDevRouteMetric1_Type()
)
aniDevRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevRouteMetric1.setStatus("current")
_AniDevRouteMetric2_Type = Integer32
_AniDevRouteMetric2_Object = MibTableColumn
aniDevRouteMetric2 = _AniDevRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 4),
    _AniDevRouteMetric2_Type()
)
aniDevRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevRouteMetric2.setStatus("current")
_AniDevRouteMetric3_Type = Integer32
_AniDevRouteMetric3_Object = MibTableColumn
aniDevRouteMetric3 = _AniDevRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 5),
    _AniDevRouteMetric3_Type()
)
aniDevRouteMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevRouteMetric3.setStatus("current")
_AniDevRouteMetric4_Type = Integer32
_AniDevRouteMetric4_Object = MibTableColumn
aniDevRouteMetric4 = _AniDevRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 6),
    _AniDevRouteMetric4_Type()
)
aniDevRouteMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevRouteMetric4.setStatus("current")
_AniDevRouteNextHop_Type = IpAddress
_AniDevRouteNextHop_Object = MibTableColumn
aniDevRouteNextHop = _AniDevRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 7),
    _AniDevRouteNextHop_Type()
)
aniDevRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aniDevRouteNextHop.setStatus("current")


class _AniDevRouteType_Type(Integer32):
    """Custom type aniDevRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_AniDevRouteType_Type.__name__ = "Integer32"
_AniDevRouteType_Object = MibTableColumn
aniDevRouteType = _AniDevRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 8),
    _AniDevRouteType_Type()
)
aniDevRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aniDevRouteType.setStatus("current")


class _AniDevRouteProto_Type(Integer32):
    """Custom type aniDevRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_AniDevRouteProto_Type.__name__ = "Integer32"
_AniDevRouteProto_Object = MibTableColumn
aniDevRouteProto = _AniDevRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 9),
    _AniDevRouteProto_Type()
)
aniDevRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevRouteProto.setStatus("current")
_AniDevRouteAge_Type = Integer32
_AniDevRouteAge_Object = MibTableColumn
aniDevRouteAge = _AniDevRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 10),
    _AniDevRouteAge_Type()
)
aniDevRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevRouteAge.setStatus("current")
_AniDevRouteMask_Type = IpAddress
_AniDevRouteMask_Object = MibTableColumn
aniDevRouteMask = _AniDevRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 11),
    _AniDevRouteMask_Type()
)
aniDevRouteMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aniDevRouteMask.setStatus("current")
_AniDevRouteMetric5_Type = Integer32
_AniDevRouteMetric5_Object = MibTableColumn
aniDevRouteMetric5 = _AniDevRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 12),
    _AniDevRouteMetric5_Type()
)
aniDevRouteMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevRouteMetric5.setStatus("current")
_AniDevRouteInfo_Type = ObjectIdentifier
_AniDevRouteInfo_Object = MibTableColumn
aniDevRouteInfo = _AniDevRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 13),
    _AniDevRouteInfo_Type()
)
aniDevRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevRouteInfo.setStatus("current")


class _AniDevRouteFlag_Type(Integer32):
    """Custom type aniDevRouteFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("network", 1))
    )


_AniDevRouteFlag_Type.__name__ = "Integer32"
_AniDevRouteFlag_Object = MibTableColumn
aniDevRouteFlag = _AniDevRouteFlag_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 9, 1, 1, 14),
    _AniDevRouteFlag_Type()
)
aniDevRouteFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aniDevRouteFlag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVROUTE-MIB",
    **{"aniDevRoute": aniDevRoute,
       "aniDevRouteTable": aniDevRouteTable,
       "aniDevRouteEntry": aniDevRouteEntry,
       "aniDevRouteDest": aniDevRouteDest,
       "aniDevRouteIfIndex": aniDevRouteIfIndex,
       "aniDevRouteMetric1": aniDevRouteMetric1,
       "aniDevRouteMetric2": aniDevRouteMetric2,
       "aniDevRouteMetric3": aniDevRouteMetric3,
       "aniDevRouteMetric4": aniDevRouteMetric4,
       "aniDevRouteNextHop": aniDevRouteNextHop,
       "aniDevRouteType": aniDevRouteType,
       "aniDevRouteProto": aniDevRouteProto,
       "aniDevRouteAge": aniDevRouteAge,
       "aniDevRouteMask": aniDevRouteMask,
       "aniDevRouteMetric5": aniDevRouteMetric5,
       "aniDevRouteInfo": aniDevRouteInfo,
       "aniDevRouteFlag": aniDevRouteFlag}
)
