# SNMP MIB module (MITEL-ROUTERGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-ROUTERGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:28 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mitelRouterIpRouterGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5)
)
mitelRouterIpRouterGroup.setRevisions(
        ("2003-03-24 10:45",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelIpRouteTable_Object = MibTable
mitelIpRouteTable = _MitelIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mitelIpRouteTable.setStatus("current")
_MitelIpRouteEntry_Object = MibTableRow
mitelIpRouteEntry = _MitelIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1)
)
mitelIpRouteEntry.setIndexNames(
    (0, "MITEL-ROUTERGROUP-MIB", "mitelIpRouteTblDestAddress"),
    (0, "MITEL-ROUTERGROUP-MIB", "mitelIpRouteTblGateAddress"),
)
if mibBuilder.loadTexts:
    mitelIpRouteEntry.setStatus("current")
_MitelIpRouteTblDestAddress_Type = IpAddress
_MitelIpRouteTblDestAddress_Object = MibTableColumn
mitelIpRouteTblDestAddress = _MitelIpRouteTblDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 1),
    _MitelIpRouteTblDestAddress_Type()
)
mitelIpRouteTblDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblDestAddress.setStatus("current")
_MitelIpRouteTblGateAddress_Type = IpAddress
_MitelIpRouteTblGateAddress_Object = MibTableColumn
mitelIpRouteTblGateAddress = _MitelIpRouteTblGateAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 2),
    _MitelIpRouteTblGateAddress_Type()
)
mitelIpRouteTblGateAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblGateAddress.setStatus("current")
_MitelIpRouteTblNetmaskAddress_Type = IpAddress
_MitelIpRouteTblNetmaskAddress_Object = MibTableColumn
mitelIpRouteTblNetmaskAddress = _MitelIpRouteTblNetmaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 3),
    _MitelIpRouteTblNetmaskAddress_Type()
)
mitelIpRouteTblNetmaskAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblNetmaskAddress.setStatus("current")


class _MitelIpRouteTblIfIndex_Type(Integer32):
    """Custom type mitelIpRouteTblIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 13),
    )


_MitelIpRouteTblIfIndex_Type.__name__ = "Integer32"
_MitelIpRouteTblIfIndex_Object = MibTableColumn
mitelIpRouteTblIfIndex = _MitelIpRouteTblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 4),
    _MitelIpRouteTblIfIndex_Type()
)
mitelIpRouteTblIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblIfIndex.setStatus("current")
_MitelIpRouteTblMetric1_Type = Integer32
_MitelIpRouteTblMetric1_Object = MibTableColumn
mitelIpRouteTblMetric1 = _MitelIpRouteTblMetric1_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 5),
    _MitelIpRouteTblMetric1_Type()
)
mitelIpRouteTblMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblMetric1.setStatus("current")
_MitelIpRouteTblMetric2_Type = Integer32
_MitelIpRouteTblMetric2_Object = MibTableColumn
mitelIpRouteTblMetric2 = _MitelIpRouteTblMetric2_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 6),
    _MitelIpRouteTblMetric2_Type()
)
mitelIpRouteTblMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblMetric2.setStatus("current")
_MitelIpRouteTblMetric3_Type = Integer32
_MitelIpRouteTblMetric3_Object = MibTableColumn
mitelIpRouteTblMetric3 = _MitelIpRouteTblMetric3_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 7),
    _MitelIpRouteTblMetric3_Type()
)
mitelIpRouteTblMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblMetric3.setStatus("current")
_MitelIpRouteTblMetric4_Type = Integer32
_MitelIpRouteTblMetric4_Object = MibTableColumn
mitelIpRouteTblMetric4 = _MitelIpRouteTblMetric4_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 8),
    _MitelIpRouteTblMetric4_Type()
)
mitelIpRouteTblMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblMetric4.setStatus("current")
_MitelIpRouteTblMetric5_Type = Integer32
_MitelIpRouteTblMetric5_Object = MibTableColumn
mitelIpRouteTblMetric5 = _MitelIpRouteTblMetric5_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 9),
    _MitelIpRouteTblMetric5_Type()
)
mitelIpRouteTblMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblMetric5.setStatus("current")
_MitelIpRouteTblRouteType_Type = Integer32
_MitelIpRouteTblRouteType_Object = MibTableColumn
mitelIpRouteTblRouteType = _MitelIpRouteTblRouteType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 10),
    _MitelIpRouteTblRouteType_Type()
)
mitelIpRouteTblRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblRouteType.setStatus("current")
_MitelIpRouteTblRouteProto_Type = Integer32
_MitelIpRouteTblRouteProto_Object = MibTableColumn
mitelIpRouteTblRouteProto = _MitelIpRouteTblRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 11),
    _MitelIpRouteTblRouteProto_Type()
)
mitelIpRouteTblRouteProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblRouteProto.setStatus("current")


class _MitelIpRouteTblRouteAge_Type(Integer32):
    """Custom type mitelIpRouteTblRouteAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MitelIpRouteTblRouteAge_Type.__name__ = "Integer32"
_MitelIpRouteTblRouteAge_Object = MibTableColumn
mitelIpRouteTblRouteAge = _MitelIpRouteTblRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 12),
    _MitelIpRouteTblRouteAge_Type()
)
mitelIpRouteTblRouteAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblRouteAge.setStatus("current")


class _MitelIpRouteTblBlockLearning_Type(Integer32):
    """Custom type mitelIpRouteTblBlockLearning based on Integer32"""
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


_MitelIpRouteTblBlockLearning_Type.__name__ = "Integer32"
_MitelIpRouteTblBlockLearning_Object = MibTableColumn
mitelIpRouteTblBlockLearning = _MitelIpRouteTblBlockLearning_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 13),
    _MitelIpRouteTblBlockLearning_Type()
)
mitelIpRouteTblBlockLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblBlockLearning.setStatus("current")


class _MitelIpRouteTblInUse_Type(Integer32):
    """Custom type mitelIpRouteTblInUse based on Integer32"""
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


_MitelIpRouteTblInUse_Type.__name__ = "Integer32"
_MitelIpRouteTblInUse_Object = MibTableColumn
mitelIpRouteTblInUse = _MitelIpRouteTblInUse_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 14),
    _MitelIpRouteTblInUse_Type()
)
mitelIpRouteTblInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblInUse.setStatus("current")


class _MitelIpRouteTblDisableLearned_Type(Integer32):
    """Custom type mitelIpRouteTblDisableLearned based on Integer32"""
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


_MitelIpRouteTblDisableLearned_Type.__name__ = "Integer32"
_MitelIpRouteTblDisableLearned_Object = MibTableColumn
mitelIpRouteTblDisableLearned = _MitelIpRouteTblDisableLearned_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 15),
    _MitelIpRouteTblDisableLearned_Type()
)
mitelIpRouteTblDisableLearned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblDisableLearned.setStatus("current")


class _MitelIpRouteTblConvertStatic_Type(Integer32):
    """Custom type mitelIpRouteTblConvertStatic based on Integer32"""
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


_MitelIpRouteTblConvertStatic_Type.__name__ = "Integer32"
_MitelIpRouteTblConvertStatic_Object = MibTableColumn
mitelIpRouteTblConvertStatic = _MitelIpRouteTblConvertStatic_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 16),
    _MitelIpRouteTblConvertStatic_Type()
)
mitelIpRouteTblConvertStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelIpRouteTblConvertStatic.setStatus("current")
_MitelIpRouteTblRowStatus_Type = RowStatus
_MitelIpRouteTblRowStatus_Object = MibTableColumn
mitelIpRouteTblRowStatus = _MitelIpRouteTblRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 17),
    _MitelIpRouteTblRowStatus_Type()
)
mitelIpRouteTblRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelIpRouteTblRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-ROUTERGROUP-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterIpRouterGroup": mitelRouterIpRouterGroup,
       "mitelIpRouteTable": mitelIpRouteTable,
       "mitelIpRouteEntry": mitelIpRouteEntry,
       "mitelIpRouteTblDestAddress": mitelIpRouteTblDestAddress,
       "mitelIpRouteTblGateAddress": mitelIpRouteTblGateAddress,
       "mitelIpRouteTblNetmaskAddress": mitelIpRouteTblNetmaskAddress,
       "mitelIpRouteTblIfIndex": mitelIpRouteTblIfIndex,
       "mitelIpRouteTblMetric1": mitelIpRouteTblMetric1,
       "mitelIpRouteTblMetric2": mitelIpRouteTblMetric2,
       "mitelIpRouteTblMetric3": mitelIpRouteTblMetric3,
       "mitelIpRouteTblMetric4": mitelIpRouteTblMetric4,
       "mitelIpRouteTblMetric5": mitelIpRouteTblMetric5,
       "mitelIpRouteTblRouteType": mitelIpRouteTblRouteType,
       "mitelIpRouteTblRouteProto": mitelIpRouteTblRouteProto,
       "mitelIpRouteTblRouteAge": mitelIpRouteTblRouteAge,
       "mitelIpRouteTblBlockLearning": mitelIpRouteTblBlockLearning,
       "mitelIpRouteTblInUse": mitelIpRouteTblInUse,
       "mitelIpRouteTblDisableLearned": mitelIpRouteTblDisableLearned,
       "mitelIpRouteTblConvertStatic": mitelIpRouteTblConvertStatic,
       "mitelIpRouteTblRowStatus": mitelIpRouteTblRowStatus}
)
