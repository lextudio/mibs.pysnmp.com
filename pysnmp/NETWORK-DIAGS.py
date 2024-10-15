# SNMP MIB module (NETWORK-DIAGS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETWORK-DIAGS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:19 2024
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

(nwDiagnostics,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "nwDiagnostics")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NwRevision_ObjectIdentity = ObjectIdentity
nwRevision = _NwRevision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 1)
)
_NwRevisionLevel_Type = Integer32
_NwRevisionLevel_Object = MibScalar
nwRevisionLevel = _NwRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 1, 1),
    _NwRevisionLevel_Type()
)
nwRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRevisionLevel.setStatus("mandatory")
_NwInternet_ObjectIdentity = ObjectIdentity
nwInternet = _NwInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2)
)
_NwIpPing_ObjectIdentity = ObjectIdentity
nwIpPing = _NwIpPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1)
)
_NwIpPingTable_Object = MibTable
nwIpPingTable = _NwIpPingTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwIpPingTable.setStatus("mandatory")
_NwIpPingEntry_Object = MibTableRow
nwIpPingEntry = _NwIpPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1)
)
nwIpPingEntry.setIndexNames(
    (0, "NETWORK-DIAGS", "nwIpPingDestination"),
    (0, "NETWORK-DIAGS", "nwIpPingOwner"),
)
if mibBuilder.loadTexts:
    nwIpPingEntry.setStatus("mandatory")
_NwIpPingDestination_Type = IpAddress
_NwIpPingDestination_Object = MibTableColumn
nwIpPingDestination = _NwIpPingDestination_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 1),
    _NwIpPingDestination_Type()
)
nwIpPingDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpPingDestination.setStatus("mandatory")
_NwIpPingOwner_Type = IpAddress
_NwIpPingOwner_Object = MibTableColumn
nwIpPingOwner = _NwIpPingOwner_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 2),
    _NwIpPingOwner_Type()
)
nwIpPingOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpPingOwner.setStatus("mandatory")


class _NwIpPingType_Type(Integer32):
    """Custom type nwIpPingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_NwIpPingType_Type.__name__ = "Integer32"
_NwIpPingType_Object = MibTableColumn
nwIpPingType = _NwIpPingType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 3),
    _NwIpPingType_Type()
)
nwIpPingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpPingType.setStatus("mandatory")


class _NwIpPingAction_Type(Integer32):
    """Custom type nwIpPingAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("other", 1),
          ("suspend", 3))
    )


_NwIpPingAction_Type.__name__ = "Integer32"
_NwIpPingAction_Object = MibTableColumn
nwIpPingAction = _NwIpPingAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 4),
    _NwIpPingAction_Type()
)
nwIpPingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpPingAction.setStatus("mandatory")


class _NwIpPingStatus_Type(Integer32):
    """Custom type nwIpPingStatus based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("alive", 4),
          ("bad-results", 6),
          ("cant-frag", 12),
          ("failed", 7),
          ("frag-exceeded", 23),
          ("host-unknown", 15),
          ("host-unreach", 9),
          ("in-progress", 3),
          ("isolated", 16),
          ("net-unknown", 14),
          ("net-unreach", 8),
          ("no-host-comm", 18),
          ("no-host-tos", 20),
          ("no-net-comm", 17),
          ("no-net-tos", 19),
          ("not-sent", 2),
          ("other", 1),
          ("parameter", 24),
          ("port-unreach", 11),
          ("proto-unreach", 10),
          ("source-quence", 21),
          ("sr-failed", 13),
          ("timeout", 5),
          ("ttl-exceeded", 22))
    )


_NwIpPingStatus_Type.__name__ = "Integer32"
_NwIpPingStatus_Object = MibTableColumn
nwIpPingStatus = _NwIpPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 1, 1, 1, 5),
    _NwIpPingStatus_Type()
)
nwIpPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpPingStatus.setStatus("mandatory")
_NwIpTraceRoute_ObjectIdentity = ObjectIdentity
nwIpTraceRoute = _NwIpTraceRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2)
)
_NwIpTraceRouteTable_Object = MibTable
nwIpTraceRouteTable = _NwIpTraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwIpTraceRouteTable.setStatus("mandatory")
_NwIpTraceRouteEntry_Object = MibTableRow
nwIpTraceRouteEntry = _NwIpTraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1)
)
nwIpTraceRouteEntry.setIndexNames(
    (0, "NETWORK-DIAGS", "nwIpTraceRouteDestination"),
    (0, "NETWORK-DIAGS", "nwIpTraceRouteOwner"),
)
if mibBuilder.loadTexts:
    nwIpTraceRouteEntry.setStatus("mandatory")
_NwIpTraceRouteDestination_Type = IpAddress
_NwIpTraceRouteDestination_Object = MibTableColumn
nwIpTraceRouteDestination = _NwIpTraceRouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 1),
    _NwIpTraceRouteDestination_Type()
)
nwIpTraceRouteDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpTraceRouteDestination.setStatus("mandatory")
_NwIpTraceRouteOwner_Type = IpAddress
_NwIpTraceRouteOwner_Object = MibTableColumn
nwIpTraceRouteOwner = _NwIpTraceRouteOwner_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 2),
    _NwIpTraceRouteOwner_Type()
)
nwIpTraceRouteOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpTraceRouteOwner.setStatus("mandatory")


class _NwIpTraceRouteType_Type(Integer32):
    """Custom type nwIpTraceRouteType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_NwIpTraceRouteType_Type.__name__ = "Integer32"
_NwIpTraceRouteType_Object = MibTableColumn
nwIpTraceRouteType = _NwIpTraceRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 3),
    _NwIpTraceRouteType_Type()
)
nwIpTraceRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpTraceRouteType.setStatus("mandatory")


class _NwIpTraceRouteAction_Type(Integer32):
    """Custom type nwIpTraceRouteAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("other", 1),
          ("suspend", 3))
    )


_NwIpTraceRouteAction_Type.__name__ = "Integer32"
_NwIpTraceRouteAction_Object = MibTableColumn
nwIpTraceRouteAction = _NwIpTraceRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 4),
    _NwIpTraceRouteAction_Type()
)
nwIpTraceRouteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwIpTraceRouteAction.setStatus("mandatory")


class _NwIpTraceRouteStatus_Type(Integer32):
    """Custom type nwIpTraceRouteStatus based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("alive", 4),
          ("bad-results", 6),
          ("cant-frag", 12),
          ("failed", 7),
          ("frag-exceeded", 23),
          ("host-unknown", 15),
          ("host-unreach", 9),
          ("in-progress", 3),
          ("isolated", 16),
          ("net-unknown", 14),
          ("net-unreach", 8),
          ("no-host-comm", 18),
          ("no-host-tos", 20),
          ("no-net-comm", 17),
          ("no-net-tos", 19),
          ("not-sent", 2),
          ("other", 1),
          ("parameter", 24),
          ("port-unreach", 11),
          ("proto-unreach", 10),
          ("source-quence", 21),
          ("sr-failed", 13),
          ("timeout", 5),
          ("ttl-exceeded", 22))
    )


_NwIpTraceRouteStatus_Type.__name__ = "Integer32"
_NwIpTraceRouteStatus_Object = MibTableColumn
nwIpTraceRouteStatus = _NwIpTraceRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 5),
    _NwIpTraceRouteStatus_Type()
)
nwIpTraceRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpTraceRouteStatus.setStatus("mandatory")
_NwIpTraceRouteNextHops_Type = Counter32
_NwIpTraceRouteNextHops_Object = MibTableColumn
nwIpTraceRouteNextHops = _NwIpTraceRouteNextHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 1, 1, 6),
    _NwIpTraceRouteNextHops_Type()
)
nwIpTraceRouteNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpTraceRouteNextHops.setStatus("mandatory")
_NwIpTraceRouteHopTable_Object = MibTable
nwIpTraceRouteHopTable = _NwIpTraceRouteHopTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    nwIpTraceRouteHopTable.setStatus("mandatory")
_NwIpTraceRouteHopEntry_Object = MibTableRow
nwIpTraceRouteHopEntry = _NwIpTraceRouteHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1)
)
nwIpTraceRouteHopEntry.setIndexNames(
    (0, "NETWORK-DIAGS", "nwIpTraceRouteHopDestination"),
    (0, "NETWORK-DIAGS", "nwIpTraceRouteHopOwner"),
    (0, "NETWORK-DIAGS", "nwIpTraceRouteHopNumber"),
)
if mibBuilder.loadTexts:
    nwIpTraceRouteHopEntry.setStatus("mandatory")
_NwIpTraceRouteHopDestination_Type = IpAddress
_NwIpTraceRouteHopDestination_Object = MibTableColumn
nwIpTraceRouteHopDestination = _NwIpTraceRouteHopDestination_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 1),
    _NwIpTraceRouteHopDestination_Type()
)
nwIpTraceRouteHopDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpTraceRouteHopDestination.setStatus("mandatory")
_NwIpTraceRouteHopOwner_Type = IpAddress
_NwIpTraceRouteHopOwner_Object = MibTableColumn
nwIpTraceRouteHopOwner = _NwIpTraceRouteHopOwner_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 2),
    _NwIpTraceRouteHopOwner_Type()
)
nwIpTraceRouteHopOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpTraceRouteHopOwner.setStatus("mandatory")
_NwIpTraceRouteHopNumber_Type = Integer32
_NwIpTraceRouteHopNumber_Object = MibTableColumn
nwIpTraceRouteHopNumber = _NwIpTraceRouteHopNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 3),
    _NwIpTraceRouteHopNumber_Type()
)
nwIpTraceRouteHopNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpTraceRouteHopNumber.setStatus("mandatory")
_NwIpTraceRouteHopIp_Type = IpAddress
_NwIpTraceRouteHopIp_Object = MibTableColumn
nwIpTraceRouteHopIp = _NwIpTraceRouteHopIp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1, 2, 2, 2, 1, 4),
    _NwIpTraceRouteHopIp_Type()
)
nwIpTraceRouteHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwIpTraceRouteHopIp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETWORK-DIAGS",
    **{"nwRevision": nwRevision,
       "nwRevisionLevel": nwRevisionLevel,
       "nwInternet": nwInternet,
       "nwIpPing": nwIpPing,
       "nwIpPingTable": nwIpPingTable,
       "nwIpPingEntry": nwIpPingEntry,
       "nwIpPingDestination": nwIpPingDestination,
       "nwIpPingOwner": nwIpPingOwner,
       "nwIpPingType": nwIpPingType,
       "nwIpPingAction": nwIpPingAction,
       "nwIpPingStatus": nwIpPingStatus,
       "nwIpTraceRoute": nwIpTraceRoute,
       "nwIpTraceRouteTable": nwIpTraceRouteTable,
       "nwIpTraceRouteEntry": nwIpTraceRouteEntry,
       "nwIpTraceRouteDestination": nwIpTraceRouteDestination,
       "nwIpTraceRouteOwner": nwIpTraceRouteOwner,
       "nwIpTraceRouteType": nwIpTraceRouteType,
       "nwIpTraceRouteAction": nwIpTraceRouteAction,
       "nwIpTraceRouteStatus": nwIpTraceRouteStatus,
       "nwIpTraceRouteNextHops": nwIpTraceRouteNextHops,
       "nwIpTraceRouteHopTable": nwIpTraceRouteHopTable,
       "nwIpTraceRouteHopEntry": nwIpTraceRouteHopEntry,
       "nwIpTraceRouteHopDestination": nwIpTraceRouteHopDestination,
       "nwIpTraceRouteHopOwner": nwIpTraceRouteHopOwner,
       "nwIpTraceRouteHopNumber": nwIpTraceRouteHopNumber,
       "nwIpTraceRouteHopIp": nwIpTraceRouteHopIp}
)
