# SNMP MIB module (ALCATEL-IND1-IPRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-IPRM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:16 2024
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

(routingIND1Iprm,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Iprm")

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1IPRMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1)
)
alcatelIND1IPRMMIB.setRevisions(
        ("2010-02-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaIprmAdminStatus(Integer32, TextualConvention):
    status = "current"
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



class AlaIprmStaticRouteTypes(Integer32, TextualConvention):
    status = "current"
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
        *(("bfdEnabled", 3),
          ("interface", 4),
          ("recursive", 2),
          ("regular", 1))
    )



class AlaMplsL3VpnRouteType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("export", 2),
          ("import", 1))
    )



class AlaIprmRtPrefType(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bgpExternal", 5),
          ("bgpInternal", 6),
          ("import", 9),
          ("isisl1", 7),
          ("isisl2", 8),
          ("local", 1),
          ("ospf", 3),
          ("rip", 4),
          ("static", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPRMMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMMIBObjects = _AlcatelIND1IPRMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1)
)
_AlaIprmConfig_ObjectIdentity = ObjectIdentity
alaIprmConfig = _AlaIprmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1)
)
_AlaIprmRouteTable_Object = MibTable
alaIprmRouteTable = _AlaIprmRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaIprmRouteTable.setStatus("current")
_AlaIprmRouteEntry_Object = MibTableRow
alaIprmRouteEntry = _AlaIprmRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1)
)
alaIprmRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteDest"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteMask"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteTos"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaIprmRouteEntry.setStatus("current")
_AlaIprmRouteDest_Type = IpAddress
_AlaIprmRouteDest_Object = MibTableColumn
alaIprmRouteDest = _AlaIprmRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 1),
    _AlaIprmRouteDest_Type()
)
alaIprmRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRouteDest.setStatus("current")
_AlaIprmRouteMask_Type = IpAddress
_AlaIprmRouteMask_Object = MibTableColumn
alaIprmRouteMask = _AlaIprmRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 2),
    _AlaIprmRouteMask_Type()
)
alaIprmRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRouteMask.setStatus("current")


class _AlaIprmRouteTos_Type(Integer32):
    """Custom type alaIprmRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaIprmRouteTos_Type.__name__ = "Integer32"
_AlaIprmRouteTos_Object = MibTableColumn
alaIprmRouteTos = _AlaIprmRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 3),
    _AlaIprmRouteTos_Type()
)
alaIprmRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRouteTos.setStatus("current")
_AlaIprmRouteNextHop_Type = IpAddress
_AlaIprmRouteNextHop_Object = MibTableColumn
alaIprmRouteNextHop = _AlaIprmRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 4),
    _AlaIprmRouteNextHop_Type()
)
alaIprmRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRouteNextHop.setStatus("current")
_AlaIprmRouteProto_Type = IANAipRouteProtocol
_AlaIprmRouteProto_Object = MibTableColumn
alaIprmRouteProto = _AlaIprmRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 5),
    _AlaIprmRouteProto_Type()
)
alaIprmRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIprmRouteProto.setStatus("current")
_AlaIprmRouteMetric_Type = Integer32
_AlaIprmRouteMetric_Object = MibTableColumn
alaIprmRouteMetric = _AlaIprmRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 6),
    _AlaIprmRouteMetric_Type()
)
alaIprmRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIprmRouteMetric.setStatus("current")
_AlaIprmRoutePriority_Type = Integer32
_AlaIprmRoutePriority_Object = MibTableColumn
alaIprmRoutePriority = _AlaIprmRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 1, 1, 7),
    _AlaIprmRoutePriority_Type()
)
alaIprmRoutePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIprmRoutePriority.setStatus("current")
_AlaIprmStaticRouteTable_Object = MibTable
alaIprmStaticRouteTable = _AlaIprmStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIprmStaticRouteTable.setStatus("current")
_AlaIprmStaticRouteEntry_Object = MibTableRow
alaIprmStaticRouteEntry = _AlaIprmStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1)
)
alaIprmStaticRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteDest"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteMask"),
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaIprmStaticRouteEntry.setStatus("current")
_AlaIprmStaticRouteDest_Type = IpAddress
_AlaIprmStaticRouteDest_Object = MibTableColumn
alaIprmStaticRouteDest = _AlaIprmStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 1),
    _AlaIprmStaticRouteDest_Type()
)
alaIprmStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmStaticRouteDest.setStatus("current")
_AlaIprmStaticRouteMask_Type = IpAddress
_AlaIprmStaticRouteMask_Object = MibTableColumn
alaIprmStaticRouteMask = _AlaIprmStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 2),
    _AlaIprmStaticRouteMask_Type()
)
alaIprmStaticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmStaticRouteMask.setStatus("current")
_AlaIprmStaticRouteNextHop_Type = IpAddress
_AlaIprmStaticRouteNextHop_Object = MibTableColumn
alaIprmStaticRouteNextHop = _AlaIprmStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 3),
    _AlaIprmStaticRouteNextHop_Type()
)
alaIprmStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmStaticRouteNextHop.setStatus("current")
_AlaIprmStaticRouteMetric_Type = Integer32
_AlaIprmStaticRouteMetric_Object = MibTableColumn
alaIprmStaticRouteMetric = _AlaIprmStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 4),
    _AlaIprmStaticRouteMetric_Type()
)
alaIprmStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmStaticRouteMetric.setStatus("current")
_AlaIprmStaticRouteStatus_Type = RowStatus
_AlaIprmStaticRouteStatus_Object = MibTableColumn
alaIprmStaticRouteStatus = _AlaIprmStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 5),
    _AlaIprmStaticRouteStatus_Type()
)
alaIprmStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmStaticRouteStatus.setStatus("current")
_AlaIprmStaticRouteBfdStatus_Type = AlaIprmAdminStatus
_AlaIprmStaticRouteBfdStatus_Object = MibTableColumn
alaIprmStaticRouteBfdStatus = _AlaIprmStaticRouteBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 6),
    _AlaIprmStaticRouteBfdStatus_Type()
)
alaIprmStaticRouteBfdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmStaticRouteBfdStatus.setStatus("current")
_AlaIprmStaticRouteType_Type = AlaIprmStaticRouteTypes
_AlaIprmStaticRouteType_Object = MibTableColumn
alaIprmStaticRouteType = _AlaIprmStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 7),
    _AlaIprmStaticRouteType_Type()
)
alaIprmStaticRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmStaticRouteType.setStatus("current")
_AlaIprmStaticRouteTag_Type = Unsigned32
_AlaIprmStaticRouteTag_Object = MibTableColumn
alaIprmStaticRouteTag = _AlaIprmStaticRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 8),
    _AlaIprmStaticRouteTag_Type()
)
alaIprmStaticRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmStaticRouteTag.setStatus("current")


class _AlaIprmStaticRouteName_Type(SnmpAdminString):
    """Custom type alaIprmStaticRouteName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaIprmStaticRouteName_Type.__name__ = "SnmpAdminString"
_AlaIprmStaticRouteName_Object = MibTableColumn
alaIprmStaticRouteName = _AlaIprmStaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 2, 1, 9),
    _AlaIprmStaticRouteName_Type()
)
alaIprmStaticRouteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmStaticRouteName.setStatus("current")


class _AlaIprmStaticAllBfd_Type(AlaIprmAdminStatus):
    """Custom type alaIprmStaticAllBfd based on AlaIprmAdminStatus"""


_AlaIprmStaticAllBfd_Object = MibScalar
alaIprmStaticAllBfd = _AlaIprmStaticAllBfd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 3),
    _AlaIprmStaticAllBfd_Type()
)
alaIprmStaticAllBfd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmStaticAllBfd.setStatus("current")
_AlaIprmPrimaryAddress_Type = IpAddress
_AlaIprmPrimaryAddress_Object = MibScalar
alaIprmPrimaryAddress = _AlaIprmPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 4),
    _AlaIprmPrimaryAddress_Type()
)
alaIprmPrimaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmPrimaryAddress.setStatus("current")
_AlaIprmRouterId_Type = IpAddress
_AlaIprmRouterId_Object = MibScalar
alaIprmRouterId = _AlaIprmRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 5),
    _AlaIprmRouterId_Type()
)
alaIprmRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRouterId.setStatus("current")


class _AlaIprmRouteDistinguisher_Type(SnmpAdminString):
    """Custom type alaIprmRouteDistinguisher based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_AlaIprmRouteDistinguisher_Type.__name__ = "SnmpAdminString"
_AlaIprmRouteDistinguisher_Object = MibScalar
alaIprmRouteDistinguisher = _AlaIprmRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 6),
    _AlaIprmRouteDistinguisher_Type()
)
alaIprmRouteDistinguisher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRouteDistinguisher.setStatus("current")
_AlaIprmRouteTargetTable_Object = MibTable
alaIprmRouteTargetTable = _AlaIprmRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaIprmRouteTargetTable.setStatus("current")
_AlaIprmRouteTargetEntry_Object = MibTableRow
alaIprmRouteTargetEntry = _AlaIprmRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7, 1)
)
alaIprmRouteTargetEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRouteTarget"),
)
if mibBuilder.loadTexts:
    alaIprmRouteTargetEntry.setStatus("current")


class _AlaIprmRouteTarget_Type(SnmpAdminString):
    """Custom type alaIprmRouteTarget based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_AlaIprmRouteTarget_Type.__name__ = "SnmpAdminString"
_AlaIprmRouteTarget_Object = MibTableColumn
alaIprmRouteTarget = _AlaIprmRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7, 1, 1),
    _AlaIprmRouteTarget_Type()
)
alaIprmRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRouteTarget.setStatus("current")
_AlaIprmRouteTargetType_Type = AlaMplsL3VpnRouteType
_AlaIprmRouteTargetType_Object = MibTableColumn
alaIprmRouteTargetType = _AlaIprmRouteTargetType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7, 1, 2),
    _AlaIprmRouteTargetType_Type()
)
alaIprmRouteTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmRouteTargetType.setStatus("current")
_AlaIprmRouteTargetRowStatus_Type = RowStatus
_AlaIprmRouteTargetRowStatus_Object = MibTableColumn
alaIprmRouteTargetRowStatus = _AlaIprmRouteTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 7, 1, 3),
    _AlaIprmRouteTargetRowStatus_Type()
)
alaIprmRouteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmRouteTargetRowStatus.setStatus("current")
_AlaIprmRtPrefTable_Object = MibTable
alaIprmRtPrefTable = _AlaIprmRtPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaIprmRtPrefTable.setStatus("current")
_AlaIprmRtPrefTableEntry_Object = MibTableRow
alaIprmRtPrefTableEntry = _AlaIprmRtPrefTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 8, 1)
)
alaIprmRtPrefTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefEntryType"),
)
if mibBuilder.loadTexts:
    alaIprmRtPrefTableEntry.setStatus("current")
_AlaIprmRtPrefEntryType_Type = AlaIprmRtPrefType
_AlaIprmRtPrefEntryType_Object = MibTableColumn
alaIprmRtPrefEntryType = _AlaIprmRtPrefEntryType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 8, 1, 1),
    _AlaIprmRtPrefEntryType_Type()
)
alaIprmRtPrefEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmRtPrefEntryType.setStatus("current")


class _AlaIprmRtPrefEntryValue_Type(Integer32):
    """Custom type alaIprmRtPrefEntryValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmRtPrefEntryValue_Type.__name__ = "Integer32"
_AlaIprmRtPrefEntryValue_Object = MibTableColumn
alaIprmRtPrefEntryValue = _AlaIprmRtPrefEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 8, 1, 2),
    _AlaIprmRtPrefEntryValue_Type()
)
alaIprmRtPrefEntryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmRtPrefEntryValue.setStatus("current")
_AlaIprmExportRouteMap_Type = Integer32
_AlaIprmExportRouteMap_Object = MibScalar
alaIprmExportRouteMap = _AlaIprmExportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 9),
    _AlaIprmExportRouteMap_Type()
)
alaIprmExportRouteMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmExportRouteMap.setStatus("current")
_AlaIprmImportVrfTable_Object = MibTable
alaIprmImportVrfTable = _AlaIprmImportVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaIprmImportVrfTable.setStatus("current")
_AlaIprmImportVrfEntry_Object = MibTableRow
alaIprmImportVrfEntry = _AlaIprmImportVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10, 1)
)
alaIprmImportVrfEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmImportVrfName"),
)
if mibBuilder.loadTexts:
    alaIprmImportVrfEntry.setStatus("current")


class _AlaIprmImportVrfName_Type(SnmpAdminString):
    """Custom type alaIprmImportVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlaIprmImportVrfName_Type.__name__ = "SnmpAdminString"
_AlaIprmImportVrfName_Object = MibTableColumn
alaIprmImportVrfName = _AlaIprmImportVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10, 1, 1),
    _AlaIprmImportVrfName_Type()
)
alaIprmImportVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmImportVrfName.setStatus("current")
_AlaIprmImportVrfRouteMap_Type = Integer32
_AlaIprmImportVrfRouteMap_Object = MibTableColumn
alaIprmImportVrfRouteMap = _AlaIprmImportVrfRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10, 1, 2),
    _AlaIprmImportVrfRouteMap_Type()
)
alaIprmImportVrfRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmImportVrfRouteMap.setStatus("current")
_AlaIprmImportVrfRowStatus_Type = RowStatus
_AlaIprmImportVrfRowStatus_Object = MibTableColumn
alaIprmImportVrfRowStatus = _AlaIprmImportVrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 10, 1, 3),
    _AlaIprmImportVrfRowStatus_Type()
)
alaIprmImportVrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmImportVrfRowStatus.setStatus("current")
_AlaIprmImportIsidTable_Object = MibTable
alaIprmImportIsidTable = _AlaIprmImportIsidTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaIprmImportIsidTable.setStatus("current")
_AlaIprmImportIsidEntry_Object = MibTableRow
alaIprmImportIsidEntry = _AlaIprmImportIsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11, 1)
)
alaIprmImportIsidEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRM-MIB", "alaIprmImportIsid"),
)
if mibBuilder.loadTexts:
    alaIprmImportIsidEntry.setStatus("current")
_AlaIprmImportIsid_Type = Unsigned32
_AlaIprmImportIsid_Object = MibTableColumn
alaIprmImportIsid = _AlaIprmImportIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11, 1, 1),
    _AlaIprmImportIsid_Type()
)
alaIprmImportIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmImportIsid.setStatus("current")
_AlaIprmImportIsidRouteMap_Type = Integer32
_AlaIprmImportIsidRouteMap_Object = MibTableColumn
alaIprmImportIsidRouteMap = _AlaIprmImportIsidRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11, 1, 2),
    _AlaIprmImportIsidRouteMap_Type()
)
alaIprmImportIsidRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmImportIsidRouteMap.setStatus("current")
_AlaIprmImportIsidRowStatus_Type = RowStatus
_AlaIprmImportIsidRowStatus_Object = MibTableColumn
alaIprmImportIsidRowStatus = _AlaIprmImportIsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 11, 1, 3),
    _AlaIprmImportIsidRowStatus_Type()
)
alaIprmImportIsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmImportIsidRowStatus.setStatus("current")
_AlaIprmExportToAllVrfsRouteMap_Type = Integer32
_AlaIprmExportToAllVrfsRouteMap_Object = MibScalar
alaIprmExportToAllVrfsRouteMap = _AlaIprmExportToAllVrfsRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 1, 1, 12),
    _AlaIprmExportToAllVrfsRouteMap_Type()
)
alaIprmExportToAllVrfsRouteMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmExportToAllVrfsRouteMap.setStatus("current")
_AlcatelIND1IPRMMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMMIBConformance = _AlcatelIND1IPRMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2)
)
_AlcatelIND1IPRMMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMMIBCompliances = _AlcatelIND1IPRMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2, 1)
)
_AlcatelIND1IPRMMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMMIBGroups = _AlcatelIND1IPRMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2, 2)
)

# Managed Objects groups

alaIprmConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2, 2, 1)
)
alaIprmConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteProto"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteMetric"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRoutePriority"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteMetric"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteStatus"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteBfdStatus"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteType"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteTag"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticRouteName"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmStaticAllBfd"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmPrimaryAddress"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouterId"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteDistinguisher"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteTargetType"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRouteTargetRowStatus"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmRtPrefEntryValue"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmExportRouteMap"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmImportVrfRouteMap"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmImportVrfRowStatus"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmImportIsidRouteMap"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmImportIsidRowStatus"),
        ("ALCATEL-IND1-IPRM-MIB", "alaIprmExportToAllVrfsRouteMap"))
)
if mibBuilder.loadTexts:
    alaIprmConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIprmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaIprmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPRM-MIB",
    **{"AlaIprmAdminStatus": AlaIprmAdminStatus,
       "AlaIprmStaticRouteTypes": AlaIprmStaticRouteTypes,
       "AlaMplsL3VpnRouteType": AlaMplsL3VpnRouteType,
       "AlaIprmRtPrefType": AlaIprmRtPrefType,
       "alcatelIND1IPRMMIB": alcatelIND1IPRMMIB,
       "alcatelIND1IPRMMIBObjects": alcatelIND1IPRMMIBObjects,
       "alaIprmConfig": alaIprmConfig,
       "alaIprmRouteTable": alaIprmRouteTable,
       "alaIprmRouteEntry": alaIprmRouteEntry,
       "alaIprmRouteDest": alaIprmRouteDest,
       "alaIprmRouteMask": alaIprmRouteMask,
       "alaIprmRouteTos": alaIprmRouteTos,
       "alaIprmRouteNextHop": alaIprmRouteNextHop,
       "alaIprmRouteProto": alaIprmRouteProto,
       "alaIprmRouteMetric": alaIprmRouteMetric,
       "alaIprmRoutePriority": alaIprmRoutePriority,
       "alaIprmStaticRouteTable": alaIprmStaticRouteTable,
       "alaIprmStaticRouteEntry": alaIprmStaticRouteEntry,
       "alaIprmStaticRouteDest": alaIprmStaticRouteDest,
       "alaIprmStaticRouteMask": alaIprmStaticRouteMask,
       "alaIprmStaticRouteNextHop": alaIprmStaticRouteNextHop,
       "alaIprmStaticRouteMetric": alaIprmStaticRouteMetric,
       "alaIprmStaticRouteStatus": alaIprmStaticRouteStatus,
       "alaIprmStaticRouteBfdStatus": alaIprmStaticRouteBfdStatus,
       "alaIprmStaticRouteType": alaIprmStaticRouteType,
       "alaIprmStaticRouteTag": alaIprmStaticRouteTag,
       "alaIprmStaticRouteName": alaIprmStaticRouteName,
       "alaIprmStaticAllBfd": alaIprmStaticAllBfd,
       "alaIprmPrimaryAddress": alaIprmPrimaryAddress,
       "alaIprmRouterId": alaIprmRouterId,
       "alaIprmRouteDistinguisher": alaIprmRouteDistinguisher,
       "alaIprmRouteTargetTable": alaIprmRouteTargetTable,
       "alaIprmRouteTargetEntry": alaIprmRouteTargetEntry,
       "alaIprmRouteTarget": alaIprmRouteTarget,
       "alaIprmRouteTargetType": alaIprmRouteTargetType,
       "alaIprmRouteTargetRowStatus": alaIprmRouteTargetRowStatus,
       "alaIprmRtPrefTable": alaIprmRtPrefTable,
       "alaIprmRtPrefTableEntry": alaIprmRtPrefTableEntry,
       "alaIprmRtPrefEntryType": alaIprmRtPrefEntryType,
       "alaIprmRtPrefEntryValue": alaIprmRtPrefEntryValue,
       "alaIprmExportRouteMap": alaIprmExportRouteMap,
       "alaIprmImportVrfTable": alaIprmImportVrfTable,
       "alaIprmImportVrfEntry": alaIprmImportVrfEntry,
       "alaIprmImportVrfName": alaIprmImportVrfName,
       "alaIprmImportVrfRouteMap": alaIprmImportVrfRouteMap,
       "alaIprmImportVrfRowStatus": alaIprmImportVrfRowStatus,
       "alaIprmImportIsidTable": alaIprmImportIsidTable,
       "alaIprmImportIsidEntry": alaIprmImportIsidEntry,
       "alaIprmImportIsid": alaIprmImportIsid,
       "alaIprmImportIsidRouteMap": alaIprmImportIsidRouteMap,
       "alaIprmImportIsidRowStatus": alaIprmImportIsidRowStatus,
       "alaIprmExportToAllVrfsRouteMap": alaIprmExportToAllVrfsRouteMap,
       "alcatelIND1IPRMMIBConformance": alcatelIND1IPRMMIBConformance,
       "alcatelIND1IPRMMIBCompliances": alcatelIND1IPRMMIBCompliances,
       "alaIprmCompliance": alaIprmCompliance,
       "alcatelIND1IPRMMIBGroups": alcatelIND1IPRMMIBGroups,
       "alaIprmConfigMIBGroup": alaIprmConfigMIBGroup}
)
