# SNMP MIB module (OPENBSD-RELAYD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPENBSD-RELAYD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:20 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(openBSD,) = mibBuilder.importSymbols(
    "OPENBSD-BASE-MIB",
    "openBSD")

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

relaydMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 3)
)
relaydMIBObjects.setRevisions(
        ("2015-10-15 21:16",
         "2015-10-14 00:00",
         "2014-03-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RelaydInfo_ObjectIdentity = ObjectIdentity
relaydInfo = _RelaydInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2)
)
_RelaydRedirects_Object = MibTable
relaydRedirects = _RelaydRedirects_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1)
)
if mibBuilder.loadTexts:
    relaydRedirects.setStatus("current")
_RelaydRedirectEntry_Object = MibTableRow
relaydRedirectEntry = _RelaydRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1)
)
relaydRedirectEntry.setIndexNames(
    (0, "OPENBSD-RELAYD-MIB", "relaydRedirectIndex"),
)
if mibBuilder.loadTexts:
    relaydRedirectEntry.setStatus("current")


class _RelaydRedirectIndex_Type(Integer32):
    """Custom type relaydRedirectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RelaydRedirectIndex_Type.__name__ = "Integer32"
_RelaydRedirectIndex_Object = MibTableColumn
relaydRedirectIndex = _RelaydRedirectIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 1),
    _RelaydRedirectIndex_Type()
)
relaydRedirectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectIndex.setStatus("current")


class _RelaydRedirectStatus_Type(Integer32):
    """Custom type relaydRedirectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("backup", 3),
          ("disabled", 1),
          ("down", 2))
    )


_RelaydRedirectStatus_Type.__name__ = "Integer32"
_RelaydRedirectStatus_Object = MibTableColumn
relaydRedirectStatus = _RelaydRedirectStatus_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 2),
    _RelaydRedirectStatus_Type()
)
relaydRedirectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectStatus.setStatus("current")
_RelaydRedirectName_Type = OctetString
_RelaydRedirectName_Object = MibTableColumn
relaydRedirectName = _RelaydRedirectName_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 3),
    _RelaydRedirectName_Type()
)
relaydRedirectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectName.setStatus("current")
_RelaydRedirectCnt_Type = Counter64
_RelaydRedirectCnt_Object = MibTableColumn
relaydRedirectCnt = _RelaydRedirectCnt_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 4),
    _RelaydRedirectCnt_Type()
)
relaydRedirectCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectCnt.setStatus("current")
_RelaydRedirectAvg_Type = Gauge32
_RelaydRedirectAvg_Object = MibTableColumn
relaydRedirectAvg = _RelaydRedirectAvg_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 5),
    _RelaydRedirectAvg_Type()
)
relaydRedirectAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectAvg.setStatus("current")
_RelaydRedirectLast_Type = Gauge32
_RelaydRedirectLast_Object = MibTableColumn
relaydRedirectLast = _RelaydRedirectLast_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 6),
    _RelaydRedirectLast_Type()
)
relaydRedirectLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectLast.setStatus("current")
_RelaydRedirectAvgHour_Type = Gauge32
_RelaydRedirectAvgHour_Object = MibTableColumn
relaydRedirectAvgHour = _RelaydRedirectAvgHour_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 7),
    _RelaydRedirectAvgHour_Type()
)
relaydRedirectAvgHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectAvgHour.setStatus("current")
_RelaydRedirectLastHour_Type = Gauge32
_RelaydRedirectLastHour_Object = MibTableColumn
relaydRedirectLastHour = _RelaydRedirectLastHour_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 8),
    _RelaydRedirectLastHour_Type()
)
relaydRedirectLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectLastHour.setStatus("current")
_RelaydRedirectAvgDay_Type = Gauge32
_RelaydRedirectAvgDay_Object = MibTableColumn
relaydRedirectAvgDay = _RelaydRedirectAvgDay_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 9),
    _RelaydRedirectAvgDay_Type()
)
relaydRedirectAvgDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectAvgDay.setStatus("current")
_RelaydRedirectLastDay_Type = Gauge32
_RelaydRedirectLastDay_Object = MibTableColumn
relaydRedirectLastDay = _RelaydRedirectLastDay_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 1, 1, 10),
    _RelaydRedirectLastDay_Type()
)
relaydRedirectLastDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRedirectLastDay.setStatus("current")
_RelaydRelays_Object = MibTable
relaydRelays = _RelaydRelays_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2)
)
if mibBuilder.loadTexts:
    relaydRelays.setStatus("current")
_RelaydRelayEntry_Object = MibTableRow
relaydRelayEntry = _RelaydRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1)
)
relaydRelayEntry.setIndexNames(
    (0, "OPENBSD-RELAYD-MIB", "relaydRelayIndex"),
)
if mibBuilder.loadTexts:
    relaydRelayEntry.setStatus("current")


class _RelaydRelayIndex_Type(Integer32):
    """Custom type relaydRelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RelaydRelayIndex_Type.__name__ = "Integer32"
_RelaydRelayIndex_Object = MibTableColumn
relaydRelayIndex = _RelaydRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 1),
    _RelaydRelayIndex_Type()
)
relaydRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayIndex.setStatus("current")


class _RelaydRelayStatus_Type(Integer32):
    """Custom type relaydRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("disabled", 1))
    )


_RelaydRelayStatus_Type.__name__ = "Integer32"
_RelaydRelayStatus_Object = MibTableColumn
relaydRelayStatus = _RelaydRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 2),
    _RelaydRelayStatus_Type()
)
relaydRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayStatus.setStatus("current")
_RelaydRelayName_Type = OctetString
_RelaydRelayName_Object = MibTableColumn
relaydRelayName = _RelaydRelayName_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 3),
    _RelaydRelayName_Type()
)
relaydRelayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayName.setStatus("current")
_RelaydRelayCnt_Type = Counter64
_RelaydRelayCnt_Object = MibTableColumn
relaydRelayCnt = _RelaydRelayCnt_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 4),
    _RelaydRelayCnt_Type()
)
relaydRelayCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayCnt.setStatus("current")
_RelaydRelayAvg_Type = Gauge32
_RelaydRelayAvg_Object = MibTableColumn
relaydRelayAvg = _RelaydRelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 5),
    _RelaydRelayAvg_Type()
)
relaydRelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayAvg.setStatus("current")
_RelaydRelayLast_Type = Gauge32
_RelaydRelayLast_Object = MibTableColumn
relaydRelayLast = _RelaydRelayLast_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 6),
    _RelaydRelayLast_Type()
)
relaydRelayLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayLast.setStatus("current")
_RelaydRelayAvgHour_Type = Gauge32
_RelaydRelayAvgHour_Object = MibTableColumn
relaydRelayAvgHour = _RelaydRelayAvgHour_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 7),
    _RelaydRelayAvgHour_Type()
)
relaydRelayAvgHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayAvgHour.setStatus("current")
_RelaydRelayLastHour_Type = Gauge32
_RelaydRelayLastHour_Object = MibTableColumn
relaydRelayLastHour = _RelaydRelayLastHour_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 8),
    _RelaydRelayLastHour_Type()
)
relaydRelayLastHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayLastHour.setStatus("current")
_RelaydRelayAvgDay_Type = Gauge32
_RelaydRelayAvgDay_Object = MibTableColumn
relaydRelayAvgDay = _RelaydRelayAvgDay_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 9),
    _RelaydRelayAvgDay_Type()
)
relaydRelayAvgDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayAvgDay.setStatus("current")
_RelaydRelayLastDay_Type = Gauge32
_RelaydRelayLastDay_Object = MibTableColumn
relaydRelayLastDay = _RelaydRelayLastDay_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 2, 1, 10),
    _RelaydRelayLastDay_Type()
)
relaydRelayLastDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRelayLastDay.setStatus("current")
_RelaydRouters_Object = MibTable
relaydRouters = _RelaydRouters_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 3)
)
if mibBuilder.loadTexts:
    relaydRouters.setStatus("current")
_RelaydRouterEntry_Object = MibTableRow
relaydRouterEntry = _RelaydRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 3, 1)
)
relaydRouterEntry.setIndexNames(
    (0, "OPENBSD-RELAYD-MIB", "relaydRouterIndex"),
)
if mibBuilder.loadTexts:
    relaydRouterEntry.setStatus("current")


class _RelaydRouterIndex_Type(Integer32):
    """Custom type relaydRouterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RelaydRouterIndex_Type.__name__ = "Integer32"
_RelaydRouterIndex_Object = MibTableColumn
relaydRouterIndex = _RelaydRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 3, 1, 1),
    _RelaydRouterIndex_Type()
)
relaydRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRouterIndex.setStatus("current")
_RelaydRouterTableIndex_Type = Integer32
_RelaydRouterTableIndex_Object = MibTableColumn
relaydRouterTableIndex = _RelaydRouterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 3, 1, 2),
    _RelaydRouterTableIndex_Type()
)
relaydRouterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRouterTableIndex.setStatus("current")


class _RelaydRouterStatus_Type(Integer32):
    """Custom type relaydRouterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("disabled", 1))
    )


_RelaydRouterStatus_Type.__name__ = "Integer32"
_RelaydRouterStatus_Object = MibTableColumn
relaydRouterStatus = _RelaydRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 3, 1, 3),
    _RelaydRouterStatus_Type()
)
relaydRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRouterStatus.setStatus("current")
_RelaydRouterName_Type = OctetString
_RelaydRouterName_Object = MibTableColumn
relaydRouterName = _RelaydRouterName_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 3, 1, 4),
    _RelaydRouterName_Type()
)
relaydRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRouterName.setStatus("current")
_RelaydRouterLabel_Type = OctetString
_RelaydRouterLabel_Object = MibTableColumn
relaydRouterLabel = _RelaydRouterLabel_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 3, 1, 5),
    _RelaydRouterLabel_Type()
)
relaydRouterLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRouterLabel.setStatus("current")
_RelaydRouterRtable_Type = Integer32
_RelaydRouterRtable_Object = MibTableColumn
relaydRouterRtable = _RelaydRouterRtable_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 3, 1, 6),
    _RelaydRouterRtable_Type()
)
relaydRouterRtable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydRouterRtable.setStatus("current")
_RelaydNetRoutes_Object = MibTable
relaydNetRoutes = _RelaydNetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 4)
)
if mibBuilder.loadTexts:
    relaydNetRoutes.setStatus("current")
_RelaydNetRouteEntry_Object = MibTableRow
relaydNetRouteEntry = _RelaydNetRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 4, 1)
)
relaydNetRouteEntry.setIndexNames(
    (0, "OPENBSD-RELAYD-MIB", "relaydNetRouteIndex"),
)
if mibBuilder.loadTexts:
    relaydNetRouteEntry.setStatus("current")


class _RelaydNetRouteIndex_Type(Integer32):
    """Custom type relaydNetRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RelaydNetRouteIndex_Type.__name__ = "Integer32"
_RelaydNetRouteIndex_Object = MibTableColumn
relaydNetRouteIndex = _RelaydNetRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 4, 1, 1),
    _RelaydNetRouteIndex_Type()
)
relaydNetRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydNetRouteIndex.setStatus("current")
_RelaydNetRouteAddr_Type = InetAddress
_RelaydNetRouteAddr_Object = MibTableColumn
relaydNetRouteAddr = _RelaydNetRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 4, 1, 2),
    _RelaydNetRouteAddr_Type()
)
relaydNetRouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydNetRouteAddr.setStatus("current")
_RelaydNetRouteAddrType_Type = InetAddressType
_RelaydNetRouteAddrType_Object = MibTableColumn
relaydNetRouteAddrType = _RelaydNetRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 4, 1, 3),
    _RelaydNetRouteAddrType_Type()
)
relaydNetRouteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydNetRouteAddrType.setStatus("current")
_RelaydNetRoutePrefixLen_Type = Integer32
_RelaydNetRoutePrefixLen_Object = MibTableColumn
relaydNetRoutePrefixLen = _RelaydNetRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 4, 1, 4),
    _RelaydNetRoutePrefixLen_Type()
)
relaydNetRoutePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydNetRoutePrefixLen.setStatus("current")
_RelaydNetRouteRouterIndex_Type = Integer32
_RelaydNetRouteRouterIndex_Object = MibTableColumn
relaydNetRouteRouterIndex = _RelaydNetRouteRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 4, 1, 5),
    _RelaydNetRouteRouterIndex_Type()
)
relaydNetRouteRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydNetRouteRouterIndex.setStatus("current")
_RelaydHosts_Object = MibTable
relaydHosts = _RelaydHosts_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5)
)
if mibBuilder.loadTexts:
    relaydHosts.setStatus("current")
_RelaydHostEntry_Object = MibTableRow
relaydHostEntry = _RelaydHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1)
)
relaydHostEntry.setIndexNames(
    (0, "OPENBSD-RELAYD-MIB", "relaydHostIndex"),
)
if mibBuilder.loadTexts:
    relaydHostEntry.setStatus("current")


class _RelaydHostIndex_Type(Integer32):
    """Custom type relaydHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RelaydHostIndex_Type.__name__ = "Integer32"
_RelaydHostIndex_Object = MibTableColumn
relaydHostIndex = _RelaydHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 1),
    _RelaydHostIndex_Type()
)
relaydHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostIndex.setStatus("current")
_RelaydHostParentIndex_Type = Integer32
_RelaydHostParentIndex_Object = MibTableColumn
relaydHostParentIndex = _RelaydHostParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 2),
    _RelaydHostParentIndex_Type()
)
relaydHostParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostParentIndex.setStatus("current")
_RelaydHostTableIndex_Type = Integer32
_RelaydHostTableIndex_Object = MibTableColumn
relaydHostTableIndex = _RelaydHostTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 3),
    _RelaydHostTableIndex_Type()
)
relaydHostTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostTableIndex.setStatus("current")
_RelaydHostName_Type = OctetString
_RelaydHostName_Object = MibTableColumn
relaydHostName = _RelaydHostName_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 4),
    _RelaydHostName_Type()
)
relaydHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostName.setStatus("current")
_RelaydHostAddress_Type = InetAddress
_RelaydHostAddress_Object = MibTableColumn
relaydHostAddress = _RelaydHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 5),
    _RelaydHostAddress_Type()
)
relaydHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostAddress.setStatus("current")
_RelaydHostAddressType_Type = InetAddressType
_RelaydHostAddressType_Object = MibTableColumn
relaydHostAddressType = _RelaydHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 6),
    _RelaydHostAddressType_Type()
)
relaydHostAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostAddressType.setStatus("current")


class _RelaydHostStatus_Type(Integer32):
    """Custom type relaydHostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("down", 2),
          ("unknown", 3),
          ("up", 0))
    )


_RelaydHostStatus_Type.__name__ = "Integer32"
_RelaydHostStatus_Object = MibTableColumn
relaydHostStatus = _RelaydHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 7),
    _RelaydHostStatus_Type()
)
relaydHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostStatus.setStatus("current")
_RelaydHostCheckCnt_Type = Counter64
_RelaydHostCheckCnt_Object = MibTableColumn
relaydHostCheckCnt = _RelaydHostCheckCnt_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 8),
    _RelaydHostCheckCnt_Type()
)
relaydHostCheckCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostCheckCnt.setStatus("current")
_RelaydHostUpCnt_Type = Counter64
_RelaydHostUpCnt_Object = MibTableColumn
relaydHostUpCnt = _RelaydHostUpCnt_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 9),
    _RelaydHostUpCnt_Type()
)
relaydHostUpCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostUpCnt.setStatus("current")


class _RelaydHostErrno_Type(Integer32):
    """Custom type relaydHostErrno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("abort", 1),
          ("httpCodeError", 28),
          ("httpCodeFail", 29),
          ("httpCodeOk", 30),
          ("httpDigestError", 31),
          ("httpDigestFail", 32),
          ("httpDigestOk", 33),
          ("icmpOk", 3),
          ("icmpReadTimeout", 4),
          ("icmpWriteTimeout", 5),
          ("intervalTimeout", 2),
          ("none", 0),
          ("scriptFail", 17),
          ("scriptOk", 16),
          ("sendExpectFail", 26),
          ("sendExpectOk", 27),
          ("sslConnectError", 18),
          ("sslConnectFail", 19),
          ("sslConnectOk", 20),
          ("sslConnectTimeout", 21),
          ("sslReadError", 24),
          ("sslReadTimeout", 22),
          ("sslWriteError", 25),
          ("sslWriteTimeout", 23),
          ("tcpConnectFail", 9),
          ("tcpConnectOk", 11),
          ("tcpConnectTimeout", 10),
          ("tcpReadFail", 15),
          ("tcpReadTimeout", 14),
          ("tcpSocketError", 6),
          ("tcpSocketLimit", 7),
          ("tcpSocketOption", 8),
          ("tcpWriteFail", 13),
          ("tcpWriteTimeout", 12))
    )


_RelaydHostErrno_Type.__name__ = "Integer32"
_RelaydHostErrno_Object = MibTableColumn
relaydHostErrno = _RelaydHostErrno_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 5, 1, 10),
    _RelaydHostErrno_Type()
)
relaydHostErrno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydHostErrno.setStatus("current")
_RelaydSessions_Object = MibTable
relaydSessions = _RelaydSessions_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6)
)
if mibBuilder.loadTexts:
    relaydSessions.setStatus("current")
_RelaydSessionEntry_Object = MibTableRow
relaydSessionEntry = _RelaydSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1)
)
relaydSessionEntry.setIndexNames(
    (0, "OPENBSD-RELAYD-MIB", "relaydSessionRelayIndex"),
    (0, "OPENBSD-RELAYD-MIB", "relaydSessionIndex"),
)
if mibBuilder.loadTexts:
    relaydSessionEntry.setStatus("current")


class _RelaydSessionIndex_Type(Integer32):
    """Custom type relaydSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RelaydSessionIndex_Type.__name__ = "Integer32"
_RelaydSessionIndex_Object = MibTableColumn
relaydSessionIndex = _RelaydSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 1),
    _RelaydSessionIndex_Type()
)
relaydSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionIndex.setStatus("current")


class _RelaydSessionRelayIndex_Type(Integer32):
    """Custom type relaydSessionRelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RelaydSessionRelayIndex_Type.__name__ = "Integer32"
_RelaydSessionRelayIndex_Object = MibTableColumn
relaydSessionRelayIndex = _RelaydSessionRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 2),
    _RelaydSessionRelayIndex_Type()
)
relaydSessionRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionRelayIndex.setStatus("current")
_RelaydSessionInAddr_Type = InetAddress
_RelaydSessionInAddr_Object = MibTableColumn
relaydSessionInAddr = _RelaydSessionInAddr_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 3),
    _RelaydSessionInAddr_Type()
)
relaydSessionInAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionInAddr.setStatus("current")
_RelaydSessionInAddrType_Type = InetAddressType
_RelaydSessionInAddrType_Object = MibTableColumn
relaydSessionInAddrType = _RelaydSessionInAddrType_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 4),
    _RelaydSessionInAddrType_Type()
)
relaydSessionInAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionInAddrType.setStatus("current")
_RelaydSessionOutAddr_Type = InetAddress
_RelaydSessionOutAddr_Object = MibTableColumn
relaydSessionOutAddr = _RelaydSessionOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 5),
    _RelaydSessionOutAddr_Type()
)
relaydSessionOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionOutAddr.setStatus("current")
_RelaydSessionOutAddrType_Type = InetAddressType
_RelaydSessionOutAddrType_Object = MibTableColumn
relaydSessionOutAddrType = _RelaydSessionOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 6),
    _RelaydSessionOutAddrType_Type()
)
relaydSessionOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionOutAddrType.setStatus("current")
_RelaydSessionPortIn_Type = Integer32
_RelaydSessionPortIn_Object = MibTableColumn
relaydSessionPortIn = _RelaydSessionPortIn_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 7),
    _RelaydSessionPortIn_Type()
)
relaydSessionPortIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionPortIn.setStatus("current")
_RelaydSessionPortOut_Type = Integer32
_RelaydSessionPortOut_Object = MibTableColumn
relaydSessionPortOut = _RelaydSessionPortOut_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 8),
    _RelaydSessionPortOut_Type()
)
relaydSessionPortOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionPortOut.setStatus("current")
_RelaydSessionAge_Type = TimeTicks
_RelaydSessionAge_Object = MibTableColumn
relaydSessionAge = _RelaydSessionAge_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 9),
    _RelaydSessionAge_Type()
)
relaydSessionAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionAge.setStatus("current")
_RelaydSessionIdle_Type = TimeTicks
_RelaydSessionIdle_Object = MibTableColumn
relaydSessionIdle = _RelaydSessionIdle_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 10),
    _RelaydSessionIdle_Type()
)
relaydSessionIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionIdle.setStatus("current")


class _RelaydSessionStatus_Type(Integer32):
    """Custom type relaydSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("running", 0))
    )


_RelaydSessionStatus_Type.__name__ = "Integer32"
_RelaydSessionStatus_Object = MibTableColumn
relaydSessionStatus = _RelaydSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 11),
    _RelaydSessionStatus_Type()
)
relaydSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionStatus.setStatus("current")
_RelaydSessionPid_Type = Integer32
_RelaydSessionPid_Object = MibTableColumn
relaydSessionPid = _RelaydSessionPid_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 6, 1, 12),
    _RelaydSessionPid_Type()
)
relaydSessionPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydSessionPid.setStatus("current")
_RelaydTables_Object = MibTable
relaydTables = _RelaydTables_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 7)
)
if mibBuilder.loadTexts:
    relaydTables.setStatus("current")
_RelaydTableEntry_Object = MibTableRow
relaydTableEntry = _RelaydTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 7, 1)
)
relaydTableEntry.setIndexNames(
    (0, "OPENBSD-RELAYD-MIB", "relaydTableIndex"),
)
if mibBuilder.loadTexts:
    relaydTableEntry.setStatus("current")


class _RelaydTableIndex_Type(Integer32):
    """Custom type relaydTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RelaydTableIndex_Type.__name__ = "Integer32"
_RelaydTableIndex_Object = MibTableColumn
relaydTableIndex = _RelaydTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 7, 1, 1),
    _RelaydTableIndex_Type()
)
relaydTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydTableIndex.setStatus("current")
_RelaydTableName_Type = OctetString
_RelaydTableName_Object = MibTableColumn
relaydTableName = _RelaydTableName_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 7, 1, 2),
    _RelaydTableName_Type()
)
relaydTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydTableName.setStatus("current")


class _RelaydTableStatus_Type(Integer32):
    """Custom type relaydTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("disabled", 2),
          ("empty", 1))
    )


_RelaydTableStatus_Type.__name__ = "Integer32"
_RelaydTableStatus_Object = MibTableColumn
relaydTableStatus = _RelaydTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 30155, 3, 2, 7, 1, 3),
    _RelaydTableStatus_Type()
)
relaydTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaydTableStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPENBSD-RELAYD-MIB",
    **{"relaydMIBObjects": relaydMIBObjects,
       "relaydInfo": relaydInfo,
       "relaydRedirects": relaydRedirects,
       "relaydRedirectEntry": relaydRedirectEntry,
       "relaydRedirectIndex": relaydRedirectIndex,
       "relaydRedirectStatus": relaydRedirectStatus,
       "relaydRedirectName": relaydRedirectName,
       "relaydRedirectCnt": relaydRedirectCnt,
       "relaydRedirectAvg": relaydRedirectAvg,
       "relaydRedirectLast": relaydRedirectLast,
       "relaydRedirectAvgHour": relaydRedirectAvgHour,
       "relaydRedirectLastHour": relaydRedirectLastHour,
       "relaydRedirectAvgDay": relaydRedirectAvgDay,
       "relaydRedirectLastDay": relaydRedirectLastDay,
       "relaydRelays": relaydRelays,
       "relaydRelayEntry": relaydRelayEntry,
       "relaydRelayIndex": relaydRelayIndex,
       "relaydRelayStatus": relaydRelayStatus,
       "relaydRelayName": relaydRelayName,
       "relaydRelayCnt": relaydRelayCnt,
       "relaydRelayAvg": relaydRelayAvg,
       "relaydRelayLast": relaydRelayLast,
       "relaydRelayAvgHour": relaydRelayAvgHour,
       "relaydRelayLastHour": relaydRelayLastHour,
       "relaydRelayAvgDay": relaydRelayAvgDay,
       "relaydRelayLastDay": relaydRelayLastDay,
       "relaydRouters": relaydRouters,
       "relaydRouterEntry": relaydRouterEntry,
       "relaydRouterIndex": relaydRouterIndex,
       "relaydRouterTableIndex": relaydRouterTableIndex,
       "relaydRouterStatus": relaydRouterStatus,
       "relaydRouterName": relaydRouterName,
       "relaydRouterLabel": relaydRouterLabel,
       "relaydRouterRtable": relaydRouterRtable,
       "relaydNetRoutes": relaydNetRoutes,
       "relaydNetRouteEntry": relaydNetRouteEntry,
       "relaydNetRouteIndex": relaydNetRouteIndex,
       "relaydNetRouteAddr": relaydNetRouteAddr,
       "relaydNetRouteAddrType": relaydNetRouteAddrType,
       "relaydNetRoutePrefixLen": relaydNetRoutePrefixLen,
       "relaydNetRouteRouterIndex": relaydNetRouteRouterIndex,
       "relaydHosts": relaydHosts,
       "relaydHostEntry": relaydHostEntry,
       "relaydHostIndex": relaydHostIndex,
       "relaydHostParentIndex": relaydHostParentIndex,
       "relaydHostTableIndex": relaydHostTableIndex,
       "relaydHostName": relaydHostName,
       "relaydHostAddress": relaydHostAddress,
       "relaydHostAddressType": relaydHostAddressType,
       "relaydHostStatus": relaydHostStatus,
       "relaydHostCheckCnt": relaydHostCheckCnt,
       "relaydHostUpCnt": relaydHostUpCnt,
       "relaydHostErrno": relaydHostErrno,
       "relaydSessions": relaydSessions,
       "relaydSessionEntry": relaydSessionEntry,
       "relaydSessionIndex": relaydSessionIndex,
       "relaydSessionRelayIndex": relaydSessionRelayIndex,
       "relaydSessionInAddr": relaydSessionInAddr,
       "relaydSessionInAddrType": relaydSessionInAddrType,
       "relaydSessionOutAddr": relaydSessionOutAddr,
       "relaydSessionOutAddrType": relaydSessionOutAddrType,
       "relaydSessionPortIn": relaydSessionPortIn,
       "relaydSessionPortOut": relaydSessionPortOut,
       "relaydSessionAge": relaydSessionAge,
       "relaydSessionIdle": relaydSessionIdle,
       "relaydSessionStatus": relaydSessionStatus,
       "relaydSessionPid": relaydSessionPid,
       "relaydTables": relaydTables,
       "relaydTableEntry": relaydTableEntry,
       "relaydTableIndex": relaydTableIndex,
       "relaydTableName": relaydTableName,
       "relaydTableStatus": relaydTableStatus}
)
