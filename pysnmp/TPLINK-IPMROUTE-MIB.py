# SNMP MIB module (TPLINK-IPMROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-IPMROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:11 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkIpMrouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78)
)
tplinkIpMrouteMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIpMrouteMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIpMrouteMIBObjects = _TplinkIpMrouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1)
)
_TpIpMRoute_ObjectIdentity = ObjectIdentity
tpIpMRoute = _TpIpMRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1)
)


class _TpIpMRouteEnable_Type(Integer32):
    """Custom type tpIpMRouteEnable based on Integer32"""
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


_TpIpMRouteEnable_Type.__name__ = "Integer32"
_TpIpMRouteEnable_Object = MibScalar
tpIpMRouteEnable = _TpIpMRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 1),
    _TpIpMRouteEnable_Type()
)
tpIpMRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpIpMRouteEnable.setStatus("current")
_TpIpMRouteSGTable_Object = MibTable
tpIpMRouteSGTable = _TpIpMRouteSGTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tpIpMRouteSGTable.setStatus("current")
_TpIpMRouteSGEntry_Object = MibTableRow
tpIpMRouteSGEntry = _TpIpMRouteSGEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1)
)
tpIpMRouteSGEntry.setIndexNames(
    (0, "TPLINK-IPMROUTE-MIB", "tpIpMRouteSGGroup"),
    (0, "TPLINK-IPMROUTE-MIB", "tpIpMRouteSGSource"),
)
if mibBuilder.loadTexts:
    tpIpMRouteSGEntry.setStatus("current")
_TpIpMRouteSGGroup_Type = IpAddress
_TpIpMRouteSGGroup_Object = MibTableColumn
tpIpMRouteSGGroup = _TpIpMRouteSGGroup_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 1),
    _TpIpMRouteSGGroup_Type()
)
tpIpMRouteSGGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteSGGroup.setStatus("current")
_TpIpMRouteSGSource_Type = IpAddress
_TpIpMRouteSGSource_Object = MibTableColumn
tpIpMRouteSGSource = _TpIpMRouteSGSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 2),
    _TpIpMRouteSGSource_Type()
)
tpIpMRouteSGSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteSGSource.setStatus("current")


class _TpIpMRouteSGIncomingInterface_Type(OctetString):
    """Custom type tpIpMRouteSGIncomingInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TpIpMRouteSGIncomingInterface_Type.__name__ = "OctetString"
_TpIpMRouteSGIncomingInterface_Object = MibTableColumn
tpIpMRouteSGIncomingInterface = _TpIpMRouteSGIncomingInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 3),
    _TpIpMRouteSGIncomingInterface_Type()
)
tpIpMRouteSGIncomingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteSGIncomingInterface.setStatus("current")


class _TpIpMRouteSGOutgoingInterface_Type(OctetString):
    """Custom type tpIpMRouteSGOutgoingInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_TpIpMRouteSGOutgoingInterface_Type.__name__ = "OctetString"
_TpIpMRouteSGOutgoingInterface_Object = MibTableColumn
tpIpMRouteSGOutgoingInterface = _TpIpMRouteSGOutgoingInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 4),
    _TpIpMRouteSGOutgoingInterface_Type()
)
tpIpMRouteSGOutgoingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteSGOutgoingInterface.setStatus("current")
_TpIpMRouteSGRpfNeighbor_Type = IpAddress
_TpIpMRouteSGRpfNeighbor_Object = MibTableColumn
tpIpMRouteSGRpfNeighbor = _TpIpMRouteSGRpfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 5),
    _TpIpMRouteSGRpfNeighbor_Type()
)
tpIpMRouteSGRpfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteSGRpfNeighbor.setStatus("current")
_TpIpMRouteSGUpTime_Type = TimeTicks
_TpIpMRouteSGUpTime_Object = MibTableColumn
tpIpMRouteSGUpTime = _TpIpMRouteSGUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 6),
    _TpIpMRouteSGUpTime_Type()
)
tpIpMRouteSGUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteSGUpTime.setStatus("current")
_TpIpMRouteSGExpiryTime_Type = TimeTicks
_TpIpMRouteSGExpiryTime_Object = MibTableColumn
tpIpMRouteSGExpiryTime = _TpIpMRouteSGExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 7),
    _TpIpMRouteSGExpiryTime_Type()
)
tpIpMRouteSGExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteSGExpiryTime.setStatus("current")


class _TpIpMRouteSGProtocol_Type(Integer32):
    """Custom type tpIpMRouteSGProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pimDenseMode", 1),
          ("pimSparseMode", 2))
    )


_TpIpMRouteSGProtocol_Type.__name__ = "Integer32"
_TpIpMRouteSGProtocol_Object = MibTableColumn
tpIpMRouteSGProtocol = _TpIpMRouteSGProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 8),
    _TpIpMRouteSGProtocol_Type()
)
tpIpMRouteSGProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteSGProtocol.setStatus("current")


class _TpIpMRouteSGFlags_Type(Integer32):
    """Custom type tpIpMRouteSGFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rpt", 2),
          ("spt", 1))
    )


_TpIpMRouteSGFlags_Type.__name__ = "Integer32"
_TpIpMRouteSGFlags_Object = MibTableColumn
tpIpMRouteSGFlags = _TpIpMRouteSGFlags_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 2, 1, 9),
    _TpIpMRouteSGFlags_Type()
)
tpIpMRouteSGFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteSGFlags.setStatus("current")
_TpIpMRouteStarGTable_Object = MibTable
tpIpMRouteStarGTable = _TpIpMRouteStarGTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tpIpMRouteStarGTable.setStatus("current")
_TpIpMRouteStarGEntry_Object = MibTableRow
tpIpMRouteStarGEntry = _TpIpMRouteStarGEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1)
)
tpIpMRouteStarGEntry.setIndexNames(
    (0, "TPLINK-IPMROUTE-MIB", "tpIpMRouteStarGGroup"),
)
if mibBuilder.loadTexts:
    tpIpMRouteStarGEntry.setStatus("current")
_TpIpMRouteStarGGroup_Type = IpAddress
_TpIpMRouteStarGGroup_Object = MibTableColumn
tpIpMRouteStarGGroup = _TpIpMRouteStarGGroup_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 1),
    _TpIpMRouteStarGGroup_Type()
)
tpIpMRouteStarGGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteStarGGroup.setStatus("current")
_TpIpMRouteStarGSource_Type = IpAddress
_TpIpMRouteStarGSource_Object = MibTableColumn
tpIpMRouteStarGSource = _TpIpMRouteStarGSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 2),
    _TpIpMRouteStarGSource_Type()
)
tpIpMRouteStarGSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteStarGSource.setStatus("current")


class _TpIpMRouteStarGIncomingInterface_Type(OctetString):
    """Custom type tpIpMRouteStarGIncomingInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TpIpMRouteStarGIncomingInterface_Type.__name__ = "OctetString"
_TpIpMRouteStarGIncomingInterface_Object = MibTableColumn
tpIpMRouteStarGIncomingInterface = _TpIpMRouteStarGIncomingInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 3),
    _TpIpMRouteStarGIncomingInterface_Type()
)
tpIpMRouteStarGIncomingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteStarGIncomingInterface.setStatus("current")


class _TpIpMRouteStarGOutgoingInterface_Type(OctetString):
    """Custom type tpIpMRouteStarGOutgoingInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_TpIpMRouteStarGOutgoingInterface_Type.__name__ = "OctetString"
_TpIpMRouteStarGOutgoingInterface_Object = MibTableColumn
tpIpMRouteStarGOutgoingInterface = _TpIpMRouteStarGOutgoingInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 4),
    _TpIpMRouteStarGOutgoingInterface_Type()
)
tpIpMRouteStarGOutgoingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteStarGOutgoingInterface.setStatus("current")
_TpIpMRouteStarGRpfNeighbor_Type = IpAddress
_TpIpMRouteStarGRpfNeighbor_Object = MibTableColumn
tpIpMRouteStarGRpfNeighbor = _TpIpMRouteStarGRpfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 5),
    _TpIpMRouteStarGRpfNeighbor_Type()
)
tpIpMRouteStarGRpfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteStarGRpfNeighbor.setStatus("current")
_TpIpMRouteStarGUpTime_Type = TimeTicks
_TpIpMRouteStarGUpTime_Object = MibTableColumn
tpIpMRouteStarGUpTime = _TpIpMRouteStarGUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 6),
    _TpIpMRouteStarGUpTime_Type()
)
tpIpMRouteStarGUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteStarGUpTime.setStatus("current")
_TpIpMRouteStarGExpiryTime_Type = TimeTicks
_TpIpMRouteStarGExpiryTime_Object = MibTableColumn
tpIpMRouteStarGExpiryTime = _TpIpMRouteStarGExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 7),
    _TpIpMRouteStarGExpiryTime_Type()
)
tpIpMRouteStarGExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteStarGExpiryTime.setStatus("current")


class _TpIpMRouteStarGProtocol_Type(Integer32):
    """Custom type tpIpMRouteStarGProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pimDenseMode", 1),
          ("pimSparseMode", 2))
    )


_TpIpMRouteStarGProtocol_Type.__name__ = "Integer32"
_TpIpMRouteStarGProtocol_Object = MibTableColumn
tpIpMRouteStarGProtocol = _TpIpMRouteStarGProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 8),
    _TpIpMRouteStarGProtocol_Type()
)
tpIpMRouteStarGProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteStarGProtocol.setStatus("current")


class _TpIpMRouteStarGFlags_Type(Integer32):
    """Custom type tpIpMRouteStarGFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rpt", 2),
          ("spt", 1))
    )


_TpIpMRouteStarGFlags_Type.__name__ = "Integer32"
_TpIpMRouteStarGFlags_Object = MibTableColumn
tpIpMRouteStarGFlags = _TpIpMRouteStarGFlags_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 1, 1, 3, 1, 9),
    _TpIpMRouteStarGFlags_Type()
)
tpIpMRouteStarGFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIpMRouteStarGFlags.setStatus("current")
_TplinkIpMrouteNotifications_ObjectIdentity = ObjectIdentity
tplinkIpMrouteNotifications = _TplinkIpMrouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 78, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IPMROUTE-MIB",
    **{"tplinkIpMrouteMIB": tplinkIpMrouteMIB,
       "tplinkIpMrouteMIBObjects": tplinkIpMrouteMIBObjects,
       "tpIpMRoute": tpIpMRoute,
       "tpIpMRouteEnable": tpIpMRouteEnable,
       "tpIpMRouteSGTable": tpIpMRouteSGTable,
       "tpIpMRouteSGEntry": tpIpMRouteSGEntry,
       "tpIpMRouteSGGroup": tpIpMRouteSGGroup,
       "tpIpMRouteSGSource": tpIpMRouteSGSource,
       "tpIpMRouteSGIncomingInterface": tpIpMRouteSGIncomingInterface,
       "tpIpMRouteSGOutgoingInterface": tpIpMRouteSGOutgoingInterface,
       "tpIpMRouteSGRpfNeighbor": tpIpMRouteSGRpfNeighbor,
       "tpIpMRouteSGUpTime": tpIpMRouteSGUpTime,
       "tpIpMRouteSGExpiryTime": tpIpMRouteSGExpiryTime,
       "tpIpMRouteSGProtocol": tpIpMRouteSGProtocol,
       "tpIpMRouteSGFlags": tpIpMRouteSGFlags,
       "tpIpMRouteStarGTable": tpIpMRouteStarGTable,
       "tpIpMRouteStarGEntry": tpIpMRouteStarGEntry,
       "tpIpMRouteStarGGroup": tpIpMRouteStarGGroup,
       "tpIpMRouteStarGSource": tpIpMRouteStarGSource,
       "tpIpMRouteStarGIncomingInterface": tpIpMRouteStarGIncomingInterface,
       "tpIpMRouteStarGOutgoingInterface": tpIpMRouteStarGOutgoingInterface,
       "tpIpMRouteStarGRpfNeighbor": tpIpMRouteStarGRpfNeighbor,
       "tpIpMRouteStarGUpTime": tpIpMRouteStarGUpTime,
       "tpIpMRouteStarGExpiryTime": tpIpMRouteStarGExpiryTime,
       "tpIpMRouteStarGProtocol": tpIpMRouteStarGProtocol,
       "tpIpMRouteStarGFlags": tpIpMRouteStarGFlags,
       "tplinkIpMrouteNotifications": tplinkIpMrouteNotifications}
)
