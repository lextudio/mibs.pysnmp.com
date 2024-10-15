# SNMP MIB module (ALCATEL-IND1-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-RIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:55 2024
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

(routingIND1Rip,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Rip")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfEntry")

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

alcatelIND1RIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1)
)
alcatelIND1RIPMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaAuthenticationEncryptKey(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1RIPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1RIPMIBObjects = _AlcatelIND1RIPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBObjects.setStatus("current")
_AlaProtocolRip_ObjectIdentity = ObjectIdentity
alaProtocolRip = _AlaProtocolRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1)
)


class _AlaRipProtoStatus_Type(Integer32):
    """Custom type alaRipProtoStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipProtoStatus_Type.__name__ = "Integer32"
_AlaRipProtoStatus_Object = MibScalar
alaRipProtoStatus = _AlaRipProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 1),
    _AlaRipProtoStatus_Type()
)
alaRipProtoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipProtoStatus.setStatus("current")


class _AlaRipHostRouteSupport_Type(Integer32):
    """Custom type alaRipHostRouteSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipHostRouteSupport_Type.__name__ = "Integer32"
_AlaRipHostRouteSupport_Object = MibScalar
alaRipHostRouteSupport = _AlaRipHostRouteSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 2),
    _AlaRipHostRouteSupport_Type()
)
alaRipHostRouteSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipHostRouteSupport.setStatus("current")


class _AlaRipRedistAdminStatus_Type(Integer32):
    """Custom type alaRipRedistAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipRedistAdminStatus_Type.__name__ = "Integer32"
_AlaRipRedistAdminStatus_Object = MibScalar
alaRipRedistAdminStatus = _AlaRipRedistAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 3),
    _AlaRipRedistAdminStatus_Type()
)
alaRipRedistAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistAdminStatus.setStatus("obsolete")


class _AlaRipRedistRouteTag_Type(Integer32):
    """Custom type alaRipRedistRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipRedistRouteTag_Type.__name__ = "Integer32"
_AlaRipRedistRouteTag_Object = MibScalar
alaRipRedistRouteTag = _AlaRipRedistRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 4),
    _AlaRipRedistRouteTag_Type()
)
alaRipRedistRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistRouteTag.setStatus("current")


class _AlaRipForceHolddownTimer_Type(Integer32):
    """Custom type alaRipForceHolddownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AlaRipForceHolddownTimer_Type.__name__ = "Integer32"
_AlaRipForceHolddownTimer_Object = MibScalar
alaRipForceHolddownTimer = _AlaRipForceHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 5),
    _AlaRipForceHolddownTimer_Type()
)
alaRipForceHolddownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipForceHolddownTimer.setStatus("current")


class _AlaRipRouteNumber_Type(Integer32):
    """Custom type alaRipRouteNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipRouteNumber_Type.__name__ = "Integer32"
_AlaRipRouteNumber_Object = MibScalar
alaRipRouteNumber = _AlaRipRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 6),
    _AlaRipRouteNumber_Type()
)
alaRipRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteNumber.setStatus("current")
_AlaRipRedistProtoTable_Object = MibTable
alaRipRedistProtoTable = _AlaRipRedistProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaRipRedistProtoTable.setStatus("obsolete")
_AlaRipRedistProtoEntry_Object = MibTableRow
alaRipRedistProtoEntry = _AlaRipRedistProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 7, 1)
)
alaRipRedistProtoEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIP-MIB", "alaRipRedistProtoId"),
)
if mibBuilder.loadTexts:
    alaRipRedistProtoEntry.setStatus("obsolete")


class _AlaRipRedistProtoId_Type(Integer32):
    """Custom type alaRipRedistProtoId based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 8),
          ("directHost", 3),
          ("isis", 7),
          ("local", 2),
          ("netmgmt", 4),
          ("ospf", 6),
          ("other", 1),
          ("rip", 5))
    )


_AlaRipRedistProtoId_Type.__name__ = "Integer32"
_AlaRipRedistProtoId_Object = MibTableColumn
alaRipRedistProtoId = _AlaRipRedistProtoId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 7, 1, 1),
    _AlaRipRedistProtoId_Type()
)
alaRipRedistProtoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRedistProtoId.setStatus("obsolete")


class _AlaRipRedistProtoMetric_Type(Integer32):
    """Custom type alaRipRedistProtoMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaRipRedistProtoMetric_Type.__name__ = "Integer32"
_AlaRipRedistProtoMetric_Object = MibTableColumn
alaRipRedistProtoMetric = _AlaRipRedistProtoMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 7, 1, 2),
    _AlaRipRedistProtoMetric_Type()
)
alaRipRedistProtoMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistProtoMetric.setStatus("obsolete")


class _AlaRipRedistProtoStatus_Type(RowStatus):
    """Custom type alaRipRedistProtoStatus based on RowStatus"""


_AlaRipRedistProtoStatus_Object = MibTableColumn
alaRipRedistProtoStatus = _AlaRipRedistProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 7, 1, 3),
    _AlaRipRedistProtoStatus_Type()
)
alaRipRedistProtoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistProtoStatus.setStatus("obsolete")
_AlaRipRouteTable_Object = MibTable
alaRipRouteTable = _AlaRipRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaRipRouteTable.setStatus("deprecated")
_AlaRipRouteEntry_Object = MibTableRow
alaRipRouteEntry = _AlaRipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9, 1)
)
alaRipRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIP-MIB", "alaRipRouteDest"),
    (0, "ALCATEL-IND1-RIP-MIB", "alaRipRouteMask"),
)
if mibBuilder.loadTexts:
    alaRipRouteEntry.setStatus("deprecated")
_AlaRipRouteDest_Type = IpAddress
_AlaRipRouteDest_Object = MibTableColumn
alaRipRouteDest = _AlaRipRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9, 1, 1),
    _AlaRipRouteDest_Type()
)
alaRipRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteDest.setStatus("deprecated")
_AlaRipRouteMask_Type = IpAddress
_AlaRipRouteMask_Object = MibTableColumn
alaRipRouteMask = _AlaRipRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9, 1, 2),
    _AlaRipRouteMask_Type()
)
alaRipRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteMask.setStatus("deprecated")
_AlaRipRouteNextHop_Type = IpAddress
_AlaRipRouteNextHop_Object = MibTableColumn
alaRipRouteNextHop = _AlaRipRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9, 1, 3),
    _AlaRipRouteNextHop_Type()
)
alaRipRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteNextHop.setStatus("deprecated")


class _AlaRipRouteType_Type(Integer32):
    """Custom type alaRipRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("redistribute", 3),
          ("remote", 2))
    )


_AlaRipRouteType_Type.__name__ = "Integer32"
_AlaRipRouteType_Object = MibTableColumn
alaRipRouteType = _AlaRipRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9, 1, 4),
    _AlaRipRouteType_Type()
)
alaRipRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteType.setStatus("deprecated")
_AlaRipRouteAge_Type = TimeTicks
_AlaRipRouteAge_Object = MibTableColumn
alaRipRouteAge = _AlaRipRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9, 1, 5),
    _AlaRipRouteAge_Type()
)
alaRipRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteAge.setStatus("deprecated")


class _AlaRipRouteTag_Type(Integer32):
    """Custom type alaRipRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipRouteTag_Type.__name__ = "Integer32"
_AlaRipRouteTag_Object = MibTableColumn
alaRipRouteTag = _AlaRipRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9, 1, 6),
    _AlaRipRouteTag_Type()
)
alaRipRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteTag.setStatus("deprecated")


class _AlaRipRouteMetric_Type(Integer32):
    """Custom type alaRipRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaRipRouteMetric_Type.__name__ = "Integer32"
_AlaRipRouteMetric_Object = MibTableColumn
alaRipRouteMetric = _AlaRipRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9, 1, 7),
    _AlaRipRouteMetric_Type()
)
alaRipRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteMetric.setStatus("deprecated")
_AlaRipRouteStatus_Type = RowStatus
_AlaRipRouteStatus_Object = MibTableColumn
alaRipRouteStatus = _AlaRipRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 9, 1, 8),
    _AlaRipRouteStatus_Type()
)
alaRipRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteStatus.setStatus("deprecated")
_AlaRipRedistRouteTable_Object = MibTable
alaRipRedistRouteTable = _AlaRipRedistRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaRipRedistRouteTable.setStatus("obsolete")
_AlaRipRedistRouteEntry_Object = MibTableRow
alaRipRedistRouteEntry = _AlaRipRedistRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10, 1)
)
alaRipRedistRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteProto"),
    (0, "ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteDest"),
    (0, "ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteMask"),
)
if mibBuilder.loadTexts:
    alaRipRedistRouteEntry.setStatus("obsolete")


class _AlaRipRedistRouteProto_Type(Integer32):
    """Custom type alaRipRedistRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 8),
          ("directHost", 3),
          ("isis", 7),
          ("local", 2),
          ("netmgmt", 4),
          ("ospf", 6),
          ("other", 1))
    )


_AlaRipRedistRouteProto_Type.__name__ = "Integer32"
_AlaRipRedistRouteProto_Object = MibTableColumn
alaRipRedistRouteProto = _AlaRipRedistRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10, 1, 1),
    _AlaRipRedistRouteProto_Type()
)
alaRipRedistRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRedistRouteProto.setStatus("obsolete")
_AlaRipRedistRouteDest_Type = IpAddress
_AlaRipRedistRouteDest_Object = MibTableColumn
alaRipRedistRouteDest = _AlaRipRedistRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10, 1, 2),
    _AlaRipRedistRouteDest_Type()
)
alaRipRedistRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRedistRouteDest.setStatus("obsolete")
_AlaRipRedistRouteMask_Type = IpAddress
_AlaRipRedistRouteMask_Object = MibTableColumn
alaRipRedistRouteMask = _AlaRipRedistRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10, 1, 3),
    _AlaRipRedistRouteMask_Type()
)
alaRipRedistRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRedistRouteMask.setStatus("obsolete")


class _AlaRipRedistRouteMetric_Type(Integer32):
    """Custom type alaRipRedistRouteMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaRipRedistRouteMetric_Type.__name__ = "Integer32"
_AlaRipRedistRouteMetric_Object = MibTableColumn
alaRipRedistRouteMetric = _AlaRipRedistRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10, 1, 4),
    _AlaRipRedistRouteMetric_Type()
)
alaRipRedistRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistRouteMetric.setStatus("obsolete")


class _AlaRipRedistRouteControl_Type(Integer32):
    """Custom type alaRipRedistRouteControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("redistributeAllSubnets", 1),
          ("redistributeAsAggregate", 2),
          ("redistributeExactMatch", 3))
    )


_AlaRipRedistRouteControl_Type.__name__ = "Integer32"
_AlaRipRedistRouteControl_Object = MibTableColumn
alaRipRedistRouteControl = _AlaRipRedistRouteControl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10, 1, 5),
    _AlaRipRedistRouteControl_Type()
)
alaRipRedistRouteControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistRouteControl.setStatus("obsolete")


class _AlaRipRedistRouteTagMatch_Type(Integer32):
    """Custom type alaRipRedistRouteTagMatch based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AlaRipRedistRouteTagMatch_Type.__name__ = "Integer32"
_AlaRipRedistRouteTagMatch_Object = MibTableColumn
alaRipRedistRouteTagMatch = _AlaRipRedistRouteTagMatch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10, 1, 6),
    _AlaRipRedistRouteTagMatch_Type()
)
alaRipRedistRouteTagMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistRouteTagMatch.setStatus("obsolete")


class _AlaRipRedistRouteEffect_Type(Integer32):
    """Custom type alaRipRedistRouteEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotRedistribute", 2),
          ("redistribute", 1))
    )


_AlaRipRedistRouteEffect_Type.__name__ = "Integer32"
_AlaRipRedistRouteEffect_Object = MibTableColumn
alaRipRedistRouteEffect = _AlaRipRedistRouteEffect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10, 1, 7),
    _AlaRipRedistRouteEffect_Type()
)
alaRipRedistRouteEffect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistRouteEffect.setStatus("obsolete")
_AlaRipRedistRouteStatus_Type = RowStatus
_AlaRipRedistRouteStatus_Object = MibTableColumn
alaRipRedistRouteStatus = _AlaRipRedistRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 10, 1, 8),
    _AlaRipRedistRouteStatus_Type()
)
alaRipRedistRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistRouteStatus.setStatus("obsolete")
_AlaRip2IfConfAugTable_Object = MibTable
alaRip2IfConfAugTable = _AlaRip2IfConfAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaRip2IfConfAugTable.setStatus("current")
_AlaRip2IfConfAugEntry_Object = MibTableRow
alaRip2IfConfAugEntry = _AlaRip2IfConfAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alaRip2IfConfAugEntry.setStatus("current")
_AlaRip2IfConfEncryptKey_Type = AlaAuthenticationEncryptKey
_AlaRip2IfConfEncryptKey_Object = MibTableColumn
alaRip2IfConfEncryptKey = _AlaRip2IfConfEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 1),
    _AlaRip2IfConfEncryptKey_Type()
)
alaRip2IfConfEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRip2IfConfEncryptKey.setStatus("current")


class _AlaRip2IfIpConfStatus_Type(Integer32):
    """Custom type alaRip2IfIpConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 3))
    )


_AlaRip2IfIpConfStatus_Type.__name__ = "Integer32"
_AlaRip2IfIpConfStatus_Object = MibTableColumn
alaRip2IfIpConfStatus = _AlaRip2IfIpConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 2),
    _AlaRip2IfIpConfStatus_Type()
)
alaRip2IfIpConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRip2IfIpConfStatus.setStatus("current")
_AlaRip2IfRecvPkts_Type = Integer32
_AlaRip2IfRecvPkts_Object = MibTableColumn
alaRip2IfRecvPkts = _AlaRip2IfRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 3),
    _AlaRip2IfRecvPkts_Type()
)
alaRip2IfRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRip2IfRecvPkts.setStatus("current")
_AlaRip2IfConfName_Type = DisplayString
_AlaRip2IfConfName_Object = MibTableColumn
alaRip2IfConfName = _AlaRip2IfConfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 4),
    _AlaRip2IfConfName_Type()
)
alaRip2IfConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRip2IfConfName.setStatus("current")


class _AlaRip2IfConfType_Type(Integer32):
    """Custom type alaRip2IfConfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("point2point", 2))
    )


_AlaRip2IfConfType_Type.__name__ = "Integer32"
_AlaRip2IfConfType_Object = MibTableColumn
alaRip2IfConfType = _AlaRip2IfConfType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 5),
    _AlaRip2IfConfType_Type()
)
alaRip2IfConfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRip2IfConfType.setStatus("current")
_AlaRip2IfConfPtoPPeer_Type = IpAddress
_AlaRip2IfConfPtoPPeer_Object = MibTableColumn
alaRip2IfConfPtoPPeer = _AlaRip2IfConfPtoPPeer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 6),
    _AlaRip2IfConfPtoPPeer_Type()
)
alaRip2IfConfPtoPPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRip2IfConfPtoPPeer.setStatus("current")
_AlaRipEcmpRouteTable_Object = MibTable
alaRipEcmpRouteTable = _AlaRipEcmpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaRipEcmpRouteTable.setStatus("current")
_AlaRipEcmpRouteEntry_Object = MibTableRow
alaRipEcmpRouteEntry = _AlaRipEcmpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1)
)
alaRipEcmpRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-RIP-MIB", "alaRipEcmpRouteDest"),
    (0, "ALCATEL-IND1-RIP-MIB", "alaRipEcmpRouteMask"),
    (0, "ALCATEL-IND1-RIP-MIB", "alaRipEcmpRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaRipEcmpRouteEntry.setStatus("current")
_AlaRipEcmpRouteDest_Type = IpAddress
_AlaRipEcmpRouteDest_Object = MibTableColumn
alaRipEcmpRouteDest = _AlaRipEcmpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 1),
    _AlaRipEcmpRouteDest_Type()
)
alaRipEcmpRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipEcmpRouteDest.setStatus("current")
_AlaRipEcmpRouteMask_Type = IpAddress
_AlaRipEcmpRouteMask_Object = MibTableColumn
alaRipEcmpRouteMask = _AlaRipEcmpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 2),
    _AlaRipEcmpRouteMask_Type()
)
alaRipEcmpRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipEcmpRouteMask.setStatus("current")
_AlaRipEcmpRouteNextHop_Type = IpAddress
_AlaRipEcmpRouteNextHop_Object = MibTableColumn
alaRipEcmpRouteNextHop = _AlaRipEcmpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 3),
    _AlaRipEcmpRouteNextHop_Type()
)
alaRipEcmpRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipEcmpRouteNextHop.setStatus("current")


class _AlaRipEcmpRouteType_Type(Integer32):
    """Custom type alaRipEcmpRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("redistribute", 3),
          ("remote", 2))
    )


_AlaRipEcmpRouteType_Type.__name__ = "Integer32"
_AlaRipEcmpRouteType_Object = MibTableColumn
alaRipEcmpRouteType = _AlaRipEcmpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 4),
    _AlaRipEcmpRouteType_Type()
)
alaRipEcmpRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteType.setStatus("current")
_AlaRipEcmpRouteAge_Type = TimeTicks
_AlaRipEcmpRouteAge_Object = MibTableColumn
alaRipEcmpRouteAge = _AlaRipEcmpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 5),
    _AlaRipEcmpRouteAge_Type()
)
alaRipEcmpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteAge.setStatus("current")


class _AlaRipEcmpRouteTag_Type(Integer32):
    """Custom type alaRipEcmpRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipEcmpRouteTag_Type.__name__ = "Integer32"
_AlaRipEcmpRouteTag_Object = MibTableColumn
alaRipEcmpRouteTag = _AlaRipEcmpRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 6),
    _AlaRipEcmpRouteTag_Type()
)
alaRipEcmpRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteTag.setStatus("current")


class _AlaRipEcmpRouteMetric_Type(Integer32):
    """Custom type alaRipEcmpRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaRipEcmpRouteMetric_Type.__name__ = "Integer32"
_AlaRipEcmpRouteMetric_Object = MibTableColumn
alaRipEcmpRouteMetric = _AlaRipEcmpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 7),
    _AlaRipEcmpRouteMetric_Type()
)
alaRipEcmpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteMetric.setStatus("current")
_AlaRipEcmpRouteStatus_Type = RowStatus
_AlaRipEcmpRouteStatus_Object = MibTableColumn
alaRipEcmpRouteStatus = _AlaRipEcmpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 8),
    _AlaRipEcmpRouteStatus_Type()
)
alaRipEcmpRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteStatus.setStatus("current")


class _AlaRipEcmpRouteState_Type(Integer32):
    """Custom type alaRipEcmpRouteState based on Integer32"""
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
        *(("active", 1),
          ("garbage", 2),
          ("holddown", 3),
          ("unknown", 4))
    )


_AlaRipEcmpRouteState_Type.__name__ = "Integer32"
_AlaRipEcmpRouteState_Object = MibTableColumn
alaRipEcmpRouteState = _AlaRipEcmpRouteState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 9),
    _AlaRipEcmpRouteState_Type()
)
alaRipEcmpRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteState.setStatus("current")


class _AlaRipUpdateInterval_Type(Integer32):
    """Custom type alaRipUpdateInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AlaRipUpdateInterval_Type.__name__ = "Integer32"
_AlaRipUpdateInterval_Object = MibScalar
alaRipUpdateInterval = _AlaRipUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 13),
    _AlaRipUpdateInterval_Type()
)
alaRipUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaRipUpdateInterval.setUnits("seconds")


class _AlaRipInvalidTimer_Type(Integer32):
    """Custom type alaRipInvalidTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 360),
    )


_AlaRipInvalidTimer_Type.__name__ = "Integer32"
_AlaRipInvalidTimer_Object = MibScalar
alaRipInvalidTimer = _AlaRipInvalidTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 14),
    _AlaRipInvalidTimer_Type()
)
alaRipInvalidTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipInvalidTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaRipInvalidTimer.setUnits("seconds")


class _AlaRipHolddownTimer_Type(Integer32):
    """Custom type alaRipHolddownTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AlaRipHolddownTimer_Type.__name__ = "Integer32"
_AlaRipHolddownTimer_Object = MibScalar
alaRipHolddownTimer = _AlaRipHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 15),
    _AlaRipHolddownTimer_Type()
)
alaRipHolddownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipHolddownTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaRipHolddownTimer.setUnits("seconds")


class _AlaRipGarbageTimer_Type(Integer32):
    """Custom type alaRipGarbageTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_AlaRipGarbageTimer_Type.__name__ = "Integer32"
_AlaRipGarbageTimer_Object = MibScalar
alaRipGarbageTimer = _AlaRipGarbageTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 16),
    _AlaRipGarbageTimer_Type()
)
alaRipGarbageTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipGarbageTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaRipGarbageTimer.setUnits("seconds")
_AlaRipDebug_ObjectIdentity = ObjectIdentity
alaRipDebug = _AlaRipDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2)
)


class _AlaRipDebugLevel_Type(Integer32):
    """Custom type alaRipDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaRipDebugLevel_Type.__name__ = "Integer32"
_AlaRipDebugLevel_Object = MibScalar
alaRipDebugLevel = _AlaRipDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 1),
    _AlaRipDebugLevel_Type()
)
alaRipDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugLevel.setStatus("deprecated")


class _AlaRipDebugError_Type(Integer32):
    """Custom type alaRipDebugError based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugError_Type.__name__ = "Integer32"
_AlaRipDebugError_Object = MibScalar
alaRipDebugError = _AlaRipDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 2),
    _AlaRipDebugError_Type()
)
alaRipDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugError.setStatus("deprecated")


class _AlaRipDebugWarn_Type(Integer32):
    """Custom type alaRipDebugWarn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugWarn_Type.__name__ = "Integer32"
_AlaRipDebugWarn_Object = MibScalar
alaRipDebugWarn = _AlaRipDebugWarn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 3),
    _AlaRipDebugWarn_Type()
)
alaRipDebugWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugWarn.setStatus("deprecated")


class _AlaRipDebugRecv_Type(Integer32):
    """Custom type alaRipDebugRecv based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugRecv_Type.__name__ = "Integer32"
_AlaRipDebugRecv_Object = MibScalar
alaRipDebugRecv = _AlaRipDebugRecv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 4),
    _AlaRipDebugRecv_Type()
)
alaRipDebugRecv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugRecv.setStatus("deprecated")


class _AlaRipDebugSend_Type(Integer32):
    """Custom type alaRipDebugSend based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugSend_Type.__name__ = "Integer32"
_AlaRipDebugSend_Object = MibScalar
alaRipDebugSend = _AlaRipDebugSend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 5),
    _AlaRipDebugSend_Type()
)
alaRipDebugSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugSend.setStatus("deprecated")


class _AlaRipDebugRdb_Type(Integer32):
    """Custom type alaRipDebugRdb based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugRdb_Type.__name__ = "Integer32"
_AlaRipDebugRdb_Object = MibScalar
alaRipDebugRdb = _AlaRipDebugRdb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 6),
    _AlaRipDebugRdb_Type()
)
alaRipDebugRdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugRdb.setStatus("deprecated")


class _AlaRipDebugAge_Type(Integer32):
    """Custom type alaRipDebugAge based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugAge_Type.__name__ = "Integer32"
_AlaRipDebugAge_Object = MibScalar
alaRipDebugAge = _AlaRipDebugAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 7),
    _AlaRipDebugAge_Type()
)
alaRipDebugAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugAge.setStatus("deprecated")


class _AlaRipDebugConfig_Type(Integer32):
    """Custom type alaRipDebugConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugConfig_Type.__name__ = "Integer32"
_AlaRipDebugConfig_Object = MibScalar
alaRipDebugConfig = _AlaRipDebugConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 8),
    _AlaRipDebugConfig_Type()
)
alaRipDebugConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugConfig.setStatus("deprecated")


class _AlaRipDebugRedist_Type(Integer32):
    """Custom type alaRipDebugRedist based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugRedist_Type.__name__ = "Integer32"
_AlaRipDebugRedist_Object = MibScalar
alaRipDebugRedist = _AlaRipDebugRedist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 9),
    _AlaRipDebugRedist_Type()
)
alaRipDebugRedist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugRedist.setStatus("deprecated")


class _AlaRipDebugInfo_Type(Integer32):
    """Custom type alaRipDebugInfo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugInfo_Type.__name__ = "Integer32"
_AlaRipDebugInfo_Object = MibScalar
alaRipDebugInfo = _AlaRipDebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 10),
    _AlaRipDebugInfo_Type()
)
alaRipDebugInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugInfo.setStatus("deprecated")


class _AlaRipDebugSetup_Type(Integer32):
    """Custom type alaRipDebugSetup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugSetup_Type.__name__ = "Integer32"
_AlaRipDebugSetup_Object = MibScalar
alaRipDebugSetup = _AlaRipDebugSetup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 11),
    _AlaRipDebugSetup_Type()
)
alaRipDebugSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugSetup.setStatus("deprecated")


class _AlaRipDebugTime_Type(Integer32):
    """Custom type alaRipDebugTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugTime_Type.__name__ = "Integer32"
_AlaRipDebugTime_Object = MibScalar
alaRipDebugTime = _AlaRipDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 12),
    _AlaRipDebugTime_Type()
)
alaRipDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugTime.setStatus("deprecated")


class _AlaRipDebugAll_Type(Integer32):
    """Custom type alaRipDebugAll based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaRipDebugAll_Type.__name__ = "Integer32"
_AlaRipDebugAll_Object = MibScalar
alaRipDebugAll = _AlaRipDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 2, 13),
    _AlaRipDebugAll_Type()
)
alaRipDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipDebugAll.setStatus("deprecated")
_AlcatelIND1RIPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1RIPMIBConformance = _AlcatelIND1RIPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBConformance.setStatus("current")
_AlcatelIND1RIPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1RIPMIBGroups = _AlcatelIND1RIPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBGroups.setStatus("current")
_AlcatelIND1RIPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1RIPMIBCompliances = _AlcatelIND1RIPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBCompliances.setStatus("current")
_AlcatelIND1RIPTraps_ObjectIdentity = ObjectIdentity
alcatelIND1RIPTraps = _AlcatelIND1RIPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 3)
)
_AlcatelIND1RIPTrapsRoot_ObjectIdentity = ObjectIdentity
alcatelIND1RIPTrapsRoot = _AlcatelIND1RIPTrapsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 3, 0)
)
rip2IfConfEntry.registerAugmentions(
    ("ALCATEL-IND1-RIP-MIB",
     "alaRip2IfConfAugEntry")
)
alaRip2IfConfAugEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())

# Managed Objects groups

alaRipMiscellaneousGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 1)
)
alaRipMiscellaneousGroup.setObjects(
      *(("ALCATEL-IND1-RIP-MIB", "alaRipRedistAdminStatus"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteTag"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipForceHolddownTimer"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRouteNumber"))
)
if mibBuilder.loadTexts:
    alaRipMiscellaneousGroup.setStatus("current")

alaRipRedistProtoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 2)
)
alaRipRedistProtoGroup.setObjects(
      *(("ALCATEL-IND1-RIP-MIB", "alaRipRedistProtoId"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistProtoMetric"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistProtoStatus"))
)
if mibBuilder.loadTexts:
    alaRipRedistProtoGroup.setStatus("obsolete")

alaRipDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 3)
)
alaRipDebugGroup.setObjects(
      *(("ALCATEL-IND1-RIP-MIB", "alaRipDebugLevel"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugError"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugWarn"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugRecv"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugSend"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugRdb"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugAge"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugConfig"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugRedist"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugInfo"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugSetup"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugTime"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipDebugAll"))
)
if mibBuilder.loadTexts:
    alaRipDebugGroup.setStatus("deprecated")

alaRipRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 4)
)
alaRipRouteGroup.setObjects(
      *(("ALCATEL-IND1-RIP-MIB", "alaRipRouteNumber"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRouteDest"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRouteMask"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRouteNextHop"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRouteType"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRouteAge"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRouteTag"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRouteMetric"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRouteStatus"))
)
if mibBuilder.loadTexts:
    alaRipRouteGroup.setStatus("deprecated")

alaRipRedistRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 5)
)
alaRipRedistRouteGroup.setObjects(
      *(("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteTag"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteProto"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteDest"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteMask"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteMetric"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteControl"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteTagMatch"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteEffect"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipRedistRouteStatus"))
)
if mibBuilder.loadTexts:
    alaRipRedistRouteGroup.setStatus("obsolete")

alaRipEcmpRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 6)
)
alaRipEcmpRouteGroup.setObjects(
      *(("ALCATEL-IND1-RIP-MIB", "alaRipRouteNumber"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipEcmpRouteType"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipEcmpRouteAge"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipEcmpRouteTag"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipEcmpRouteMetric"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipEcmpRouteStatus"),
        ("ALCATEL-IND1-RIP-MIB", "alaRipEcmpRouteState"))
)
if mibBuilder.loadTexts:
    alaRipEcmpRouteGroup.setStatus("current")


# Notification objects

ripRouteMaxLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    ripRouteMaxLimitReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1RIPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-RIP-MIB",
    **{"AlaAuthenticationEncryptKey": AlaAuthenticationEncryptKey,
       "alcatelIND1RIPMIB": alcatelIND1RIPMIB,
       "alcatelIND1RIPMIBObjects": alcatelIND1RIPMIBObjects,
       "alaProtocolRip": alaProtocolRip,
       "alaRipProtoStatus": alaRipProtoStatus,
       "alaRipHostRouteSupport": alaRipHostRouteSupport,
       "alaRipRedistAdminStatus": alaRipRedistAdminStatus,
       "alaRipRedistRouteTag": alaRipRedistRouteTag,
       "alaRipForceHolddownTimer": alaRipForceHolddownTimer,
       "alaRipRouteNumber": alaRipRouteNumber,
       "alaRipRedistProtoTable": alaRipRedistProtoTable,
       "alaRipRedistProtoEntry": alaRipRedistProtoEntry,
       "alaRipRedistProtoId": alaRipRedistProtoId,
       "alaRipRedistProtoMetric": alaRipRedistProtoMetric,
       "alaRipRedistProtoStatus": alaRipRedistProtoStatus,
       "alaRipRouteTable": alaRipRouteTable,
       "alaRipRouteEntry": alaRipRouteEntry,
       "alaRipRouteDest": alaRipRouteDest,
       "alaRipRouteMask": alaRipRouteMask,
       "alaRipRouteNextHop": alaRipRouteNextHop,
       "alaRipRouteType": alaRipRouteType,
       "alaRipRouteAge": alaRipRouteAge,
       "alaRipRouteTag": alaRipRouteTag,
       "alaRipRouteMetric": alaRipRouteMetric,
       "alaRipRouteStatus": alaRipRouteStatus,
       "alaRipRedistRouteTable": alaRipRedistRouteTable,
       "alaRipRedistRouteEntry": alaRipRedistRouteEntry,
       "alaRipRedistRouteProto": alaRipRedistRouteProto,
       "alaRipRedistRouteDest": alaRipRedistRouteDest,
       "alaRipRedistRouteMask": alaRipRedistRouteMask,
       "alaRipRedistRouteMetric": alaRipRedistRouteMetric,
       "alaRipRedistRouteControl": alaRipRedistRouteControl,
       "alaRipRedistRouteTagMatch": alaRipRedistRouteTagMatch,
       "alaRipRedistRouteEffect": alaRipRedistRouteEffect,
       "alaRipRedistRouteStatus": alaRipRedistRouteStatus,
       "alaRip2IfConfAugTable": alaRip2IfConfAugTable,
       "alaRip2IfConfAugEntry": alaRip2IfConfAugEntry,
       "alaRip2IfConfEncryptKey": alaRip2IfConfEncryptKey,
       "alaRip2IfIpConfStatus": alaRip2IfIpConfStatus,
       "alaRip2IfRecvPkts": alaRip2IfRecvPkts,
       "alaRip2IfConfName": alaRip2IfConfName,
       "alaRip2IfConfType": alaRip2IfConfType,
       "alaRip2IfConfPtoPPeer": alaRip2IfConfPtoPPeer,
       "alaRipEcmpRouteTable": alaRipEcmpRouteTable,
       "alaRipEcmpRouteEntry": alaRipEcmpRouteEntry,
       "alaRipEcmpRouteDest": alaRipEcmpRouteDest,
       "alaRipEcmpRouteMask": alaRipEcmpRouteMask,
       "alaRipEcmpRouteNextHop": alaRipEcmpRouteNextHop,
       "alaRipEcmpRouteType": alaRipEcmpRouteType,
       "alaRipEcmpRouteAge": alaRipEcmpRouteAge,
       "alaRipEcmpRouteTag": alaRipEcmpRouteTag,
       "alaRipEcmpRouteMetric": alaRipEcmpRouteMetric,
       "alaRipEcmpRouteStatus": alaRipEcmpRouteStatus,
       "alaRipEcmpRouteState": alaRipEcmpRouteState,
       "alaRipUpdateInterval": alaRipUpdateInterval,
       "alaRipInvalidTimer": alaRipInvalidTimer,
       "alaRipHolddownTimer": alaRipHolddownTimer,
       "alaRipGarbageTimer": alaRipGarbageTimer,
       "alaRipDebug": alaRipDebug,
       "alaRipDebugLevel": alaRipDebugLevel,
       "alaRipDebugError": alaRipDebugError,
       "alaRipDebugWarn": alaRipDebugWarn,
       "alaRipDebugRecv": alaRipDebugRecv,
       "alaRipDebugSend": alaRipDebugSend,
       "alaRipDebugRdb": alaRipDebugRdb,
       "alaRipDebugAge": alaRipDebugAge,
       "alaRipDebugConfig": alaRipDebugConfig,
       "alaRipDebugRedist": alaRipDebugRedist,
       "alaRipDebugInfo": alaRipDebugInfo,
       "alaRipDebugSetup": alaRipDebugSetup,
       "alaRipDebugTime": alaRipDebugTime,
       "alaRipDebugAll": alaRipDebugAll,
       "alcatelIND1RIPMIBConformance": alcatelIND1RIPMIBConformance,
       "alcatelIND1RIPMIBGroups": alcatelIND1RIPMIBGroups,
       "alaRipMiscellaneousGroup": alaRipMiscellaneousGroup,
       "alaRipRedistProtoGroup": alaRipRedistProtoGroup,
       "alaRipDebugGroup": alaRipDebugGroup,
       "alaRipRouteGroup": alaRipRouteGroup,
       "alaRipRedistRouteGroup": alaRipRedistRouteGroup,
       "alaRipEcmpRouteGroup": alaRipEcmpRouteGroup,
       "alcatelIND1RIPMIBCompliances": alcatelIND1RIPMIBCompliances,
       "alcatelIND1RIPMIBCompliance": alcatelIND1RIPMIBCompliance,
       "alcatelIND1RIPTraps": alcatelIND1RIPTraps,
       "alcatelIND1RIPTrapsRoot": alcatelIND1RIPTrapsRoot,
       "ripRouteMaxLimitReached": ripRouteMaxLimitReached}
)
