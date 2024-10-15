# SNMP MIB module (ALCATEL-IND1-MLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-MLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:34 2024
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

(softentIND1Mld,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Mld")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

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

alcatelIND1MldMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1)
)
alcatelIND1MldMIB.setRevisions(
        ("2011-02-23 00:00",
         "2008-09-10 00:00",
         "2008-08-08 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1MldMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1MldMIBObjects = _AlcatelIND1MldMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1)
)
_AlaMld_ObjectIdentity = ObjectIdentity
alaMld = _AlaMld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1)
)


class _AlaMldStatus_Type(Integer32):
    """Custom type alaMldStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldStatus_Type.__name__ = "Integer32"
_AlaMldStatus_Object = MibScalar
alaMldStatus = _AlaMldStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 1),
    _AlaMldStatus_Type()
)
alaMldStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldStatus.setStatus("current")


class _AlaMldQuerying_Type(Integer32):
    """Custom type alaMldQuerying based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldQuerying_Type.__name__ = "Integer32"
_AlaMldQuerying_Object = MibScalar
alaMldQuerying = _AlaMldQuerying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 2),
    _AlaMldQuerying_Type()
)
alaMldQuerying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldQuerying.setStatus("current")


class _AlaMldSpoofing_Type(Integer32):
    """Custom type alaMldSpoofing based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldSpoofing_Type.__name__ = "Integer32"
_AlaMldSpoofing_Object = MibScalar
alaMldSpoofing = _AlaMldSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 3),
    _AlaMldSpoofing_Type()
)
alaMldSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldSpoofing.setStatus("current")


class _AlaMldZapping_Type(Integer32):
    """Custom type alaMldZapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldZapping_Type.__name__ = "Integer32"
_AlaMldZapping_Object = MibScalar
alaMldZapping = _AlaMldZapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 4),
    _AlaMldZapping_Type()
)
alaMldZapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldZapping.setStatus("current")


class _AlaMldVersion_Type(Unsigned32):
    """Custom type alaMldVersion based on Unsigned32"""
    defaultValue = 1


_AlaMldVersion_Object = MibScalar
alaMldVersion = _AlaMldVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 5),
    _AlaMldVersion_Type()
)
alaMldVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVersion.setStatus("current")


class _AlaMldRobustness_Type(Unsigned32):
    """Custom type alaMldRobustness based on Unsigned32"""
    defaultValue = 2


_AlaMldRobustness_Object = MibScalar
alaMldRobustness = _AlaMldRobustness_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 6),
    _AlaMldRobustness_Type()
)
alaMldRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldRobustness.setStatus("current")


class _AlaMldQueryInterval_Type(Unsigned32):
    """Custom type alaMldQueryInterval based on Unsigned32"""
    defaultValue = 125


_AlaMldQueryInterval_Object = MibScalar
alaMldQueryInterval = _AlaMldQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 7),
    _AlaMldQueryInterval_Type()
)
alaMldQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldQueryInterval.setUnits("seconds")


class _AlaMldQueryResponseInterval_Type(Unsigned32):
    """Custom type alaMldQueryResponseInterval based on Unsigned32"""
    defaultValue = 10000


_AlaMldQueryResponseInterval_Object = MibScalar
alaMldQueryResponseInterval = _AlaMldQueryResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 8),
    _AlaMldQueryResponseInterval_Type()
)
alaMldQueryResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldQueryResponseInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldQueryResponseInterval.setUnits("milliseconds")


class _AlaMldLastMemberQueryInterval_Type(Unsigned32):
    """Custom type alaMldLastMemberQueryInterval based on Unsigned32"""
    defaultValue = 1000


_AlaMldLastMemberQueryInterval_Object = MibScalar
alaMldLastMemberQueryInterval = _AlaMldLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 9),
    _AlaMldLastMemberQueryInterval_Type()
)
alaMldLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldLastMemberQueryInterval.setUnits("milliseconds")


class _AlaMldRouterTimeout_Type(Unsigned32):
    """Custom type alaMldRouterTimeout based on Unsigned32"""
    defaultValue = 90


_AlaMldRouterTimeout_Object = MibScalar
alaMldRouterTimeout = _AlaMldRouterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 10),
    _AlaMldRouterTimeout_Type()
)
alaMldRouterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldRouterTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaMldRouterTimeout.setUnits("seconds")


class _AlaMldSourceTimeout_Type(Unsigned32):
    """Custom type alaMldSourceTimeout based on Unsigned32"""
    defaultValue = 30


_AlaMldSourceTimeout_Object = MibScalar
alaMldSourceTimeout = _AlaMldSourceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 11),
    _AlaMldSourceTimeout_Type()
)
alaMldSourceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldSourceTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaMldSourceTimeout.setUnits("seconds")


class _AlaMldProxying_Type(Integer32):
    """Custom type alaMldProxying based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldProxying_Type.__name__ = "Integer32"
_AlaMldProxying_Object = MibScalar
alaMldProxying = _AlaMldProxying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 12),
    _AlaMldProxying_Type()
)
alaMldProxying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldProxying.setStatus("current")


class _AlaMldUnsolicitedReportInterval_Type(Unsigned32):
    """Custom type alaMldUnsolicitedReportInterval based on Unsigned32"""
    defaultValue = 1


_AlaMldUnsolicitedReportInterval_Object = MibScalar
alaMldUnsolicitedReportInterval = _AlaMldUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 13),
    _AlaMldUnsolicitedReportInterval_Type()
)
alaMldUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldUnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldUnsolicitedReportInterval.setUnits("seconds")


class _AlaMldQuerierForwarding_Type(Integer32):
    """Custom type alaMldQuerierForwarding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldQuerierForwarding_Type.__name__ = "Integer32"
_AlaMldQuerierForwarding_Object = MibScalar
alaMldQuerierForwarding = _AlaMldQuerierForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 14),
    _AlaMldQuerierForwarding_Type()
)
alaMldQuerierForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldQuerierForwarding.setStatus("current")


class _AlaMldMaxGroupLimit_Type(Unsigned32):
    """Custom type alaMldMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaMldMaxGroupLimit_Object = MibScalar
alaMldMaxGroupLimit = _AlaMldMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 15),
    _AlaMldMaxGroupLimit_Type()
)
alaMldMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldMaxGroupLimit.setStatus("current")


class _AlaMldMaxGroupExceedAction_Type(Integer32):
    """Custom type alaMldMaxGroupExceedAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("none", 0),
          ("replace", 2))
    )


_AlaMldMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaMldMaxGroupExceedAction_Object = MibScalar
alaMldMaxGroupExceedAction = _AlaMldMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 16),
    _AlaMldMaxGroupExceedAction_Type()
)
alaMldMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldMaxGroupExceedAction.setStatus("current")


class _AlaMldFloodUnknown_Type(Integer32):
    """Custom type alaMldFloodUnknown based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldFloodUnknown_Type.__name__ = "Integer32"
_AlaMldFloodUnknown_Object = MibScalar
alaMldFloodUnknown = _AlaMldFloodUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 17),
    _AlaMldFloodUnknown_Type()
)
alaMldFloodUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldFloodUnknown.setStatus("current")


class _AlaMldHelperAddressType_Type(InetAddressType):
    """Custom type alaMldHelperAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldHelperAddressType_Type.__name__ = "InetAddressType"
_AlaMldHelperAddressType_Object = MibScalar
alaMldHelperAddressType = _AlaMldHelperAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 18),
    _AlaMldHelperAddressType_Type()
)
alaMldHelperAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldHelperAddressType.setStatus("current")


class _AlaMldHelperAddress_Type(InetAddress):
    """Custom type alaMldHelperAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AlaMldHelperAddress_Type.__name__ = "InetAddress"
_AlaMldHelperAddress_Object = MibScalar
alaMldHelperAddress = _AlaMldHelperAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 19),
    _AlaMldHelperAddress_Type()
)
alaMldHelperAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldHelperAddress.setStatus("current")


class _AlaMldZeroBasedQuery_Type(Integer32):
    """Custom type alaMldZeroBasedQuery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldZeroBasedQuery_Type.__name__ = "Integer32"
_AlaMldZeroBasedQuery_Object = MibScalar
alaMldZeroBasedQuery = _AlaMldZeroBasedQuery_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 1, 20),
    _AlaMldZeroBasedQuery_Type()
)
alaMldZeroBasedQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldZeroBasedQuery.setStatus("current")
_AlaMldVlan_ObjectIdentity = ObjectIdentity
alaMldVlan = _AlaMldVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2)
)
_AlaMldVlanTable_Object = MibTable
alaMldVlanTable = _AlaMldVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaMldVlanTable.setStatus("current")
_AlaMldVlanEntry_Object = MibTableRow
alaMldVlanEntry = _AlaMldVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1)
)
alaMldVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldVlanIndex"),
)
if mibBuilder.loadTexts:
    alaMldVlanEntry.setStatus("current")
_AlaMldVlanIndex_Type = Unsigned32
_AlaMldVlanIndex_Object = MibTableColumn
alaMldVlanIndex = _AlaMldVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 1),
    _AlaMldVlanIndex_Type()
)
alaMldVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldVlanIndex.setStatus("current")


class _AlaMldVlanStatus_Type(Integer32):
    """Custom type alaMldVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldVlanStatus_Type.__name__ = "Integer32"
_AlaMldVlanStatus_Object = MibTableColumn
alaMldVlanStatus = _AlaMldVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 2),
    _AlaMldVlanStatus_Type()
)
alaMldVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanStatus.setStatus("current")


class _AlaMldVlanQuerying_Type(Integer32):
    """Custom type alaMldVlanQuerying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldVlanQuerying_Type.__name__ = "Integer32"
_AlaMldVlanQuerying_Object = MibTableColumn
alaMldVlanQuerying = _AlaMldVlanQuerying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 3),
    _AlaMldVlanQuerying_Type()
)
alaMldVlanQuerying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanQuerying.setStatus("current")


class _AlaMldVlanSpoofing_Type(Integer32):
    """Custom type alaMldVlanSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldVlanSpoofing_Type.__name__ = "Integer32"
_AlaMldVlanSpoofing_Object = MibTableColumn
alaMldVlanSpoofing = _AlaMldVlanSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 4),
    _AlaMldVlanSpoofing_Type()
)
alaMldVlanSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanSpoofing.setStatus("current")


class _AlaMldVlanZapping_Type(Integer32):
    """Custom type alaMldVlanZapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldVlanZapping_Type.__name__ = "Integer32"
_AlaMldVlanZapping_Object = MibTableColumn
alaMldVlanZapping = _AlaMldVlanZapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 5),
    _AlaMldVlanZapping_Type()
)
alaMldVlanZapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanZapping.setStatus("current")
_AlaMldVlanVersion_Type = Unsigned32
_AlaMldVlanVersion_Object = MibTableColumn
alaMldVlanVersion = _AlaMldVlanVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 6),
    _AlaMldVlanVersion_Type()
)
alaMldVlanVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanVersion.setStatus("current")
_AlaMldVlanRobustness_Type = Unsigned32
_AlaMldVlanRobustness_Object = MibTableColumn
alaMldVlanRobustness = _AlaMldVlanRobustness_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 7),
    _AlaMldVlanRobustness_Type()
)
alaMldVlanRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanRobustness.setStatus("current")
_AlaMldVlanQueryInterval_Type = Unsigned32
_AlaMldVlanQueryInterval_Object = MibTableColumn
alaMldVlanQueryInterval = _AlaMldVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 8),
    _AlaMldVlanQueryInterval_Type()
)
alaMldVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldVlanQueryInterval.setUnits("seconds")
_AlaMldVlanQueryResponseInterval_Type = Unsigned32
_AlaMldVlanQueryResponseInterval_Object = MibTableColumn
alaMldVlanQueryResponseInterval = _AlaMldVlanQueryResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 9),
    _AlaMldVlanQueryResponseInterval_Type()
)
alaMldVlanQueryResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanQueryResponseInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldVlanQueryResponseInterval.setUnits("milliseconds")
_AlaMldVlanLastMemberQueryInterval_Type = Unsigned32
_AlaMldVlanLastMemberQueryInterval_Object = MibTableColumn
alaMldVlanLastMemberQueryInterval = _AlaMldVlanLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 10),
    _AlaMldVlanLastMemberQueryInterval_Type()
)
alaMldVlanLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldVlanLastMemberQueryInterval.setUnits("milliseconds")
_AlaMldVlanRouterTimeout_Type = Unsigned32
_AlaMldVlanRouterTimeout_Object = MibTableColumn
alaMldVlanRouterTimeout = _AlaMldVlanRouterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 11),
    _AlaMldVlanRouterTimeout_Type()
)
alaMldVlanRouterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanRouterTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaMldVlanRouterTimeout.setUnits("seconds")
_AlaMldVlanSourceTimeout_Type = Unsigned32
_AlaMldVlanSourceTimeout_Object = MibTableColumn
alaMldVlanSourceTimeout = _AlaMldVlanSourceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 12),
    _AlaMldVlanSourceTimeout_Type()
)
alaMldVlanSourceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanSourceTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaMldVlanSourceTimeout.setUnits("seconds")


class _AlaMldVlanProxying_Type(Integer32):
    """Custom type alaMldVlanProxying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldVlanProxying_Type.__name__ = "Integer32"
_AlaMldVlanProxying_Object = MibTableColumn
alaMldVlanProxying = _AlaMldVlanProxying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 13),
    _AlaMldVlanProxying_Type()
)
alaMldVlanProxying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanProxying.setStatus("current")
_AlaMldVlanUnsolicitedReportInterval_Type = Unsigned32
_AlaMldVlanUnsolicitedReportInterval_Object = MibTableColumn
alaMldVlanUnsolicitedReportInterval = _AlaMldVlanUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 14),
    _AlaMldVlanUnsolicitedReportInterval_Type()
)
alaMldVlanUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanUnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldVlanUnsolicitedReportInterval.setUnits("seconds")


class _AlaMldVlanQuerierForwarding_Type(Integer32):
    """Custom type alaMldVlanQuerierForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldVlanQuerierForwarding_Type.__name__ = "Integer32"
_AlaMldVlanQuerierForwarding_Object = MibTableColumn
alaMldVlanQuerierForwarding = _AlaMldVlanQuerierForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 15),
    _AlaMldVlanQuerierForwarding_Type()
)
alaMldVlanQuerierForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanQuerierForwarding.setStatus("current")


class _AlaMldVlanMaxGroupLimit_Type(Unsigned32):
    """Custom type alaMldVlanMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaMldVlanMaxGroupLimit_Object = MibTableColumn
alaMldVlanMaxGroupLimit = _AlaMldVlanMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 16),
    _AlaMldVlanMaxGroupLimit_Type()
)
alaMldVlanMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanMaxGroupLimit.setStatus("current")


class _AlaMldVlanMaxGroupExceedAction_Type(Integer32):
    """Custom type alaMldVlanMaxGroupExceedAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("none", 0),
          ("replace", 2))
    )


_AlaMldVlanMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaMldVlanMaxGroupExceedAction_Object = MibTableColumn
alaMldVlanMaxGroupExceedAction = _AlaMldVlanMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 17),
    _AlaMldVlanMaxGroupExceedAction_Type()
)
alaMldVlanMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanMaxGroupExceedAction.setStatus("current")


class _AlaMldVlanZeroBasedQuery_Type(Integer32):
    """Custom type alaMldVlanZeroBasedQuery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 0))
    )


_AlaMldVlanZeroBasedQuery_Type.__name__ = "Integer32"
_AlaMldVlanZeroBasedQuery_Object = MibTableColumn
alaMldVlanZeroBasedQuery = _AlaMldVlanZeroBasedQuery_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 2, 1, 1, 18),
    _AlaMldVlanZeroBasedQuery_Type()
)
alaMldVlanZeroBasedQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldVlanZeroBasedQuery.setStatus("current")
_AlaMldMember_ObjectIdentity = ObjectIdentity
alaMldMember = _AlaMldMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3)
)
_AlaMldMemberTable_Object = MibTable
alaMldMemberTable = _AlaMldMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaMldMemberTable.setStatus("current")
_AlaMldMemberEntry_Object = MibTableRow
alaMldMemberEntry = _AlaMldMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3, 1, 1)
)
alaMldMemberEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldMemberVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldMemberIfIndex"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldMemberGroupAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldMemberSourceAddress"),
)
if mibBuilder.loadTexts:
    alaMldMemberEntry.setStatus("current")
_AlaMldMemberVlan_Type = Unsigned32
_AlaMldMemberVlan_Object = MibTableColumn
alaMldMemberVlan = _AlaMldMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3, 1, 1, 1),
    _AlaMldMemberVlan_Type()
)
alaMldMemberVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberVlan.setStatus("current")
_AlaMldMemberIfIndex_Type = InterfaceIndex
_AlaMldMemberIfIndex_Object = MibTableColumn
alaMldMemberIfIndex = _AlaMldMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3, 1, 1, 2),
    _AlaMldMemberIfIndex_Type()
)
alaMldMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberIfIndex.setStatus("current")
_AlaMldMemberGroupAddress_Type = InetAddressIPv6
_AlaMldMemberGroupAddress_Object = MibTableColumn
alaMldMemberGroupAddress = _AlaMldMemberGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3, 1, 1, 3),
    _AlaMldMemberGroupAddress_Type()
)
alaMldMemberGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberGroupAddress.setStatus("current")
_AlaMldMemberSourceAddress_Type = InetAddressIPv6
_AlaMldMemberSourceAddress_Object = MibTableColumn
alaMldMemberSourceAddress = _AlaMldMemberSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3, 1, 1, 4),
    _AlaMldMemberSourceAddress_Type()
)
alaMldMemberSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberSourceAddress.setStatus("current")


class _AlaMldMemberMode_Type(Integer32):
    """Custom type alaMldMemberMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_AlaMldMemberMode_Type.__name__ = "Integer32"
_AlaMldMemberMode_Object = MibTableColumn
alaMldMemberMode = _AlaMldMemberMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3, 1, 1, 5),
    _AlaMldMemberMode_Type()
)
alaMldMemberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldMemberMode.setStatus("current")
_AlaMldMemberCount_Type = Counter32
_AlaMldMemberCount_Object = MibTableColumn
alaMldMemberCount = _AlaMldMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3, 1, 1, 6),
    _AlaMldMemberCount_Type()
)
alaMldMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldMemberCount.setStatus("current")
_AlaMldMemberTimeout_Type = TimeTicks
_AlaMldMemberTimeout_Object = MibTableColumn
alaMldMemberTimeout = _AlaMldMemberTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 3, 1, 1, 7),
    _AlaMldMemberTimeout_Type()
)
alaMldMemberTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldMemberTimeout.setStatus("current")
_AlaMldStaticMember_ObjectIdentity = ObjectIdentity
alaMldStaticMember = _AlaMldStaticMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 4)
)
_AlaMldStaticMemberTable_Object = MibTable
alaMldStaticMemberTable = _AlaMldStaticMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaMldStaticMemberTable.setStatus("current")
_AlaMldStaticMemberEntry_Object = MibTableRow
alaMldStaticMemberEntry = _AlaMldStaticMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 4, 1, 1)
)
alaMldStaticMemberEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldStaticMemberVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldStaticMemberIfIndex"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldStaticMemberGroupAddress"),
)
if mibBuilder.loadTexts:
    alaMldStaticMemberEntry.setStatus("current")
_AlaMldStaticMemberVlan_Type = Unsigned32
_AlaMldStaticMemberVlan_Object = MibTableColumn
alaMldStaticMemberVlan = _AlaMldStaticMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 4, 1, 1, 1),
    _AlaMldStaticMemberVlan_Type()
)
alaMldStaticMemberVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticMemberVlan.setStatus("current")
_AlaMldStaticMemberIfIndex_Type = InterfaceIndex
_AlaMldStaticMemberIfIndex_Object = MibTableColumn
alaMldStaticMemberIfIndex = _AlaMldStaticMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 4, 1, 1, 2),
    _AlaMldStaticMemberIfIndex_Type()
)
alaMldStaticMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticMemberIfIndex.setStatus("current")
_AlaMldStaticMemberGroupAddress_Type = InetAddressIPv6
_AlaMldStaticMemberGroupAddress_Object = MibTableColumn
alaMldStaticMemberGroupAddress = _AlaMldStaticMemberGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 4, 1, 1, 3),
    _AlaMldStaticMemberGroupAddress_Type()
)
alaMldStaticMemberGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticMemberGroupAddress.setStatus("current")
_AlaMldStaticMemberRowStatus_Type = RowStatus
_AlaMldStaticMemberRowStatus_Object = MibTableColumn
alaMldStaticMemberRowStatus = _AlaMldStaticMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 4, 1, 1, 4),
    _AlaMldStaticMemberRowStatus_Type()
)
alaMldStaticMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaMldStaticMemberRowStatus.setStatus("current")
_AlaMldNeighbor_ObjectIdentity = ObjectIdentity
alaMldNeighbor = _AlaMldNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 5)
)
_AlaMldNeighborTable_Object = MibTable
alaMldNeighborTable = _AlaMldNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaMldNeighborTable.setStatus("current")
_AlaMldNeighborEntry_Object = MibTableRow
alaMldNeighborEntry = _AlaMldNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 5, 1, 1)
)
alaMldNeighborEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldNeighborVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldNeighborIfIndex"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldNeighborHostAddress"),
)
if mibBuilder.loadTexts:
    alaMldNeighborEntry.setStatus("current")
_AlaMldNeighborVlan_Type = Unsigned32
_AlaMldNeighborVlan_Object = MibTableColumn
alaMldNeighborVlan = _AlaMldNeighborVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 5, 1, 1, 1),
    _AlaMldNeighborVlan_Type()
)
alaMldNeighborVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldNeighborVlan.setStatus("current")
_AlaMldNeighborIfIndex_Type = InterfaceIndex
_AlaMldNeighborIfIndex_Object = MibTableColumn
alaMldNeighborIfIndex = _AlaMldNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 5, 1, 1, 2),
    _AlaMldNeighborIfIndex_Type()
)
alaMldNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldNeighborIfIndex.setStatus("current")
_AlaMldNeighborHostAddress_Type = InetAddressIPv6
_AlaMldNeighborHostAddress_Object = MibTableColumn
alaMldNeighborHostAddress = _AlaMldNeighborHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 5, 1, 1, 3),
    _AlaMldNeighborHostAddress_Type()
)
alaMldNeighborHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldNeighborHostAddress.setStatus("current")
_AlaMldNeighborCount_Type = Counter32
_AlaMldNeighborCount_Object = MibTableColumn
alaMldNeighborCount = _AlaMldNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 5, 1, 1, 4),
    _AlaMldNeighborCount_Type()
)
alaMldNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldNeighborCount.setStatus("current")
_AlaMldNeighborTimeout_Type = TimeTicks
_AlaMldNeighborTimeout_Object = MibTableColumn
alaMldNeighborTimeout = _AlaMldNeighborTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 5, 1, 1, 5),
    _AlaMldNeighborTimeout_Type()
)
alaMldNeighborTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldNeighborTimeout.setStatus("current")
_AlaMldStaticNeighbor_ObjectIdentity = ObjectIdentity
alaMldStaticNeighbor = _AlaMldStaticNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 6)
)
_AlaMldStaticNeighborTable_Object = MibTable
alaMldStaticNeighborTable = _AlaMldStaticNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alaMldStaticNeighborTable.setStatus("current")
_AlaMldStaticNeighborEntry_Object = MibTableRow
alaMldStaticNeighborEntry = _AlaMldStaticNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 6, 1, 1)
)
alaMldStaticNeighborEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldStaticNeighborVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldStaticNeighborIfIndex"),
)
if mibBuilder.loadTexts:
    alaMldStaticNeighborEntry.setStatus("current")
_AlaMldStaticNeighborVlan_Type = Unsigned32
_AlaMldStaticNeighborVlan_Object = MibTableColumn
alaMldStaticNeighborVlan = _AlaMldStaticNeighborVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 6, 1, 1, 1),
    _AlaMldStaticNeighborVlan_Type()
)
alaMldStaticNeighborVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticNeighborVlan.setStatus("current")
_AlaMldStaticNeighborIfIndex_Type = InterfaceIndex
_AlaMldStaticNeighborIfIndex_Object = MibTableColumn
alaMldStaticNeighborIfIndex = _AlaMldStaticNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 6, 1, 1, 2),
    _AlaMldStaticNeighborIfIndex_Type()
)
alaMldStaticNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticNeighborIfIndex.setStatus("current")
_AlaMldStaticNeighborRowStatus_Type = RowStatus
_AlaMldStaticNeighborRowStatus_Object = MibTableColumn
alaMldStaticNeighborRowStatus = _AlaMldStaticNeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 6, 1, 1, 3),
    _AlaMldStaticNeighborRowStatus_Type()
)
alaMldStaticNeighborRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaMldStaticNeighborRowStatus.setStatus("current")
_AlaMldQuerier_ObjectIdentity = ObjectIdentity
alaMldQuerier = _AlaMldQuerier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 7)
)
_AlaMldQuerierTable_Object = MibTable
alaMldQuerierTable = _AlaMldQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaMldQuerierTable.setStatus("current")
_AlaMldQuerierEntry_Object = MibTableRow
alaMldQuerierEntry = _AlaMldQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 7, 1, 1)
)
alaMldQuerierEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldQuerierVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldQuerierIfIndex"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldQuerierHostAddress"),
)
if mibBuilder.loadTexts:
    alaMldQuerierEntry.setStatus("current")
_AlaMldQuerierVlan_Type = Unsigned32
_AlaMldQuerierVlan_Object = MibTableColumn
alaMldQuerierVlan = _AlaMldQuerierVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 7, 1, 1, 1),
    _AlaMldQuerierVlan_Type()
)
alaMldQuerierVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldQuerierVlan.setStatus("current")
_AlaMldQuerierIfIndex_Type = InterfaceIndex
_AlaMldQuerierIfIndex_Object = MibTableColumn
alaMldQuerierIfIndex = _AlaMldQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 7, 1, 1, 2),
    _AlaMldQuerierIfIndex_Type()
)
alaMldQuerierIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldQuerierIfIndex.setStatus("current")
_AlaMldQuerierHostAddress_Type = InetAddressIPv6
_AlaMldQuerierHostAddress_Object = MibTableColumn
alaMldQuerierHostAddress = _AlaMldQuerierHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 7, 1, 1, 3),
    _AlaMldQuerierHostAddress_Type()
)
alaMldQuerierHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldQuerierHostAddress.setStatus("current")
_AlaMldQuerierCount_Type = Counter32
_AlaMldQuerierCount_Object = MibTableColumn
alaMldQuerierCount = _AlaMldQuerierCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 7, 1, 1, 4),
    _AlaMldQuerierCount_Type()
)
alaMldQuerierCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldQuerierCount.setStatus("current")
_AlaMldQuerierTimeout_Type = TimeTicks
_AlaMldQuerierTimeout_Object = MibTableColumn
alaMldQuerierTimeout = _AlaMldQuerierTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 7, 1, 1, 5),
    _AlaMldQuerierTimeout_Type()
)
alaMldQuerierTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldQuerierTimeout.setStatus("current")
_AlaMldStaticQuerier_ObjectIdentity = ObjectIdentity
alaMldStaticQuerier = _AlaMldStaticQuerier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 8)
)
_AlaMldStaticQuerierTable_Object = MibTable
alaMldStaticQuerierTable = _AlaMldStaticQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaMldStaticQuerierTable.setStatus("current")
_AlaMldStaticQuerierEntry_Object = MibTableRow
alaMldStaticQuerierEntry = _AlaMldStaticQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 8, 1, 1)
)
alaMldStaticQuerierEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldStaticQuerierVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldStaticQuerierIfIndex"),
)
if mibBuilder.loadTexts:
    alaMldStaticQuerierEntry.setStatus("current")
_AlaMldStaticQuerierVlan_Type = Unsigned32
_AlaMldStaticQuerierVlan_Object = MibTableColumn
alaMldStaticQuerierVlan = _AlaMldStaticQuerierVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 8, 1, 1, 1),
    _AlaMldStaticQuerierVlan_Type()
)
alaMldStaticQuerierVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticQuerierVlan.setStatus("current")
_AlaMldStaticQuerierIfIndex_Type = InterfaceIndex
_AlaMldStaticQuerierIfIndex_Object = MibTableColumn
alaMldStaticQuerierIfIndex = _AlaMldStaticQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 8, 1, 1, 2),
    _AlaMldStaticQuerierIfIndex_Type()
)
alaMldStaticQuerierIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticQuerierIfIndex.setStatus("current")
_AlaMldStaticQuerierRowStatus_Type = RowStatus
_AlaMldStaticQuerierRowStatus_Object = MibTableColumn
alaMldStaticQuerierRowStatus = _AlaMldStaticQuerierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 8, 1, 1, 3),
    _AlaMldStaticQuerierRowStatus_Type()
)
alaMldStaticQuerierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaMldStaticQuerierRowStatus.setStatus("current")
_AlaMldSource_ObjectIdentity = ObjectIdentity
alaMldSource = _AlaMldSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9)
)
_AlaMldSourceTable_Object = MibTable
alaMldSourceTable = _AlaMldSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alaMldSourceTable.setStatus("current")
_AlaMldSourceEntry_Object = MibTableRow
alaMldSourceEntry = _AlaMldSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9, 1, 1)
)
alaMldSourceEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldSourceVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldSourceGroupAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldSourceHostAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldSourceDestAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldSourceOrigAddress"),
)
if mibBuilder.loadTexts:
    alaMldSourceEntry.setStatus("current")
_AlaMldSourceVlan_Type = Unsigned32
_AlaMldSourceVlan_Object = MibTableColumn
alaMldSourceVlan = _AlaMldSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9, 1, 1, 1),
    _AlaMldSourceVlan_Type()
)
alaMldSourceVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldSourceVlan.setStatus("current")
_AlaMldSourceIfIndex_Type = InterfaceIndex
_AlaMldSourceIfIndex_Object = MibTableColumn
alaMldSourceIfIndex = _AlaMldSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9, 1, 1, 2),
    _AlaMldSourceIfIndex_Type()
)
alaMldSourceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldSourceIfIndex.setStatus("current")
_AlaMldSourceGroupAddress_Type = InetAddressIPv6
_AlaMldSourceGroupAddress_Object = MibTableColumn
alaMldSourceGroupAddress = _AlaMldSourceGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9, 1, 1, 3),
    _AlaMldSourceGroupAddress_Type()
)
alaMldSourceGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldSourceGroupAddress.setStatus("current")
_AlaMldSourceHostAddress_Type = InetAddressIPv6
_AlaMldSourceHostAddress_Object = MibTableColumn
alaMldSourceHostAddress = _AlaMldSourceHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9, 1, 1, 4),
    _AlaMldSourceHostAddress_Type()
)
alaMldSourceHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldSourceHostAddress.setStatus("current")
_AlaMldSourceDestAddress_Type = InetAddressIPv6
_AlaMldSourceDestAddress_Object = MibTableColumn
alaMldSourceDestAddress = _AlaMldSourceDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9, 1, 1, 5),
    _AlaMldSourceDestAddress_Type()
)
alaMldSourceDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldSourceDestAddress.setStatus("current")
_AlaMldSourceOrigAddress_Type = InetAddressIPv6
_AlaMldSourceOrigAddress_Object = MibTableColumn
alaMldSourceOrigAddress = _AlaMldSourceOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9, 1, 1, 6),
    _AlaMldSourceOrigAddress_Type()
)
alaMldSourceOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldSourceOrigAddress.setStatus("current")


class _AlaMldSourceType_Type(Integer32):
    """Custom type alaMldSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2))
    )


_AlaMldSourceType_Type.__name__ = "Integer32"
_AlaMldSourceType_Object = MibTableColumn
alaMldSourceType = _AlaMldSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 9, 1, 1, 7),
    _AlaMldSourceType_Type()
)
alaMldSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldSourceType.setStatus("current")
_AlaMldForward_ObjectIdentity = ObjectIdentity
alaMldForward = _AlaMldForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10)
)
_AlaMldForwardTable_Object = MibTable
alaMldForwardTable = _AlaMldForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    alaMldForwardTable.setStatus("current")
_AlaMldForwardEntry_Object = MibTableRow
alaMldForwardEntry = _AlaMldForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1)
)
alaMldForwardEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldForwardVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldForwardGroupAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldForwardHostAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldForwardDestAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldForwardOrigAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldForwardNextVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldForwardNextIfIndex"),
)
if mibBuilder.loadTexts:
    alaMldForwardEntry.setStatus("current")
_AlaMldForwardVlan_Type = Unsigned32
_AlaMldForwardVlan_Object = MibTableColumn
alaMldForwardVlan = _AlaMldForwardVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 1),
    _AlaMldForwardVlan_Type()
)
alaMldForwardVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldForwardVlan.setStatus("current")
_AlaMldForwardIfIndex_Type = InterfaceIndex
_AlaMldForwardIfIndex_Object = MibTableColumn
alaMldForwardIfIndex = _AlaMldForwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 2),
    _AlaMldForwardIfIndex_Type()
)
alaMldForwardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldForwardIfIndex.setStatus("current")
_AlaMldForwardGroupAddress_Type = InetAddressIPv6
_AlaMldForwardGroupAddress_Object = MibTableColumn
alaMldForwardGroupAddress = _AlaMldForwardGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 3),
    _AlaMldForwardGroupAddress_Type()
)
alaMldForwardGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldForwardGroupAddress.setStatus("current")
_AlaMldForwardHostAddress_Type = InetAddressIPv6
_AlaMldForwardHostAddress_Object = MibTableColumn
alaMldForwardHostAddress = _AlaMldForwardHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 4),
    _AlaMldForwardHostAddress_Type()
)
alaMldForwardHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldForwardHostAddress.setStatus("current")
_AlaMldForwardDestAddress_Type = InetAddressIPv6
_AlaMldForwardDestAddress_Object = MibTableColumn
alaMldForwardDestAddress = _AlaMldForwardDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 5),
    _AlaMldForwardDestAddress_Type()
)
alaMldForwardDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldForwardDestAddress.setStatus("current")
_AlaMldForwardOrigAddress_Type = InetAddressIPv6
_AlaMldForwardOrigAddress_Object = MibTableColumn
alaMldForwardOrigAddress = _AlaMldForwardOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 6),
    _AlaMldForwardOrigAddress_Type()
)
alaMldForwardOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldForwardOrigAddress.setStatus("current")


class _AlaMldForwardType_Type(Integer32):
    """Custom type alaMldForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2))
    )


_AlaMldForwardType_Type.__name__ = "Integer32"
_AlaMldForwardType_Object = MibTableColumn
alaMldForwardType = _AlaMldForwardType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 7),
    _AlaMldForwardType_Type()
)
alaMldForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldForwardType.setStatus("current")
_AlaMldForwardNextVlan_Type = Unsigned32
_AlaMldForwardNextVlan_Object = MibTableColumn
alaMldForwardNextVlan = _AlaMldForwardNextVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 8),
    _AlaMldForwardNextVlan_Type()
)
alaMldForwardNextVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldForwardNextVlan.setStatus("current")
_AlaMldForwardNextIfIndex_Type = InterfaceIndex
_AlaMldForwardNextIfIndex_Object = MibTableColumn
alaMldForwardNextIfIndex = _AlaMldForwardNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 9),
    _AlaMldForwardNextIfIndex_Type()
)
alaMldForwardNextIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldForwardNextIfIndex.setStatus("current")


class _AlaMldForwardNextType_Type(Integer32):
    """Custom type alaMldForwardNextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2))
    )


_AlaMldForwardNextType_Type.__name__ = "Integer32"
_AlaMldForwardNextType_Object = MibTableColumn
alaMldForwardNextType = _AlaMldForwardNextType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 10, 1, 1, 10),
    _AlaMldForwardNextType_Type()
)
alaMldForwardNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldForwardNextType.setStatus("current")
_AlaMldTunnel_ObjectIdentity = ObjectIdentity
alaMldTunnel = _AlaMldTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11)
)
_AlaMldTunnelTable_Object = MibTable
alaMldTunnelTable = _AlaMldTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alaMldTunnelTable.setStatus("current")
_AlaMldTunnelEntry_Object = MibTableRow
alaMldTunnelEntry = _AlaMldTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1)
)
alaMldTunnelEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldTunnelVlan"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldTunnelGroupAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldTunnelHostAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldTunnelDestAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldTunnelOrigAddress"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldTunnelNextDestAddress"),
)
if mibBuilder.loadTexts:
    alaMldTunnelEntry.setStatus("current")
_AlaMldTunnelVlan_Type = Unsigned32
_AlaMldTunnelVlan_Object = MibTableColumn
alaMldTunnelVlan = _AlaMldTunnelVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1, 1),
    _AlaMldTunnelVlan_Type()
)
alaMldTunnelVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldTunnelVlan.setStatus("current")
_AlaMldTunnelIfIndex_Type = InterfaceIndex
_AlaMldTunnelIfIndex_Object = MibTableColumn
alaMldTunnelIfIndex = _AlaMldTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1, 2),
    _AlaMldTunnelIfIndex_Type()
)
alaMldTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldTunnelIfIndex.setStatus("current")
_AlaMldTunnelGroupAddress_Type = InetAddressIPv6
_AlaMldTunnelGroupAddress_Object = MibTableColumn
alaMldTunnelGroupAddress = _AlaMldTunnelGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1, 3),
    _AlaMldTunnelGroupAddress_Type()
)
alaMldTunnelGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldTunnelGroupAddress.setStatus("current")
_AlaMldTunnelHostAddress_Type = InetAddressIPv6
_AlaMldTunnelHostAddress_Object = MibTableColumn
alaMldTunnelHostAddress = _AlaMldTunnelHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1, 4),
    _AlaMldTunnelHostAddress_Type()
)
alaMldTunnelHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldTunnelHostAddress.setStatus("current")
_AlaMldTunnelDestAddress_Type = InetAddressIPv6
_AlaMldTunnelDestAddress_Object = MibTableColumn
alaMldTunnelDestAddress = _AlaMldTunnelDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1, 5),
    _AlaMldTunnelDestAddress_Type()
)
alaMldTunnelDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldTunnelDestAddress.setStatus("current")
_AlaMldTunnelOrigAddress_Type = InetAddressIPv6
_AlaMldTunnelOrigAddress_Object = MibTableColumn
alaMldTunnelOrigAddress = _AlaMldTunnelOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1, 6),
    _AlaMldTunnelOrigAddress_Type()
)
alaMldTunnelOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldTunnelOrigAddress.setStatus("current")


class _AlaMldTunnelType_Type(Integer32):
    """Custom type alaMldTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2))
    )


_AlaMldTunnelType_Type.__name__ = "Integer32"
_AlaMldTunnelType_Object = MibTableColumn
alaMldTunnelType = _AlaMldTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1, 7),
    _AlaMldTunnelType_Type()
)
alaMldTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldTunnelType.setStatus("current")
_AlaMldTunnelNextDestAddress_Type = InetAddressIPv6
_AlaMldTunnelNextDestAddress_Object = MibTableColumn
alaMldTunnelNextDestAddress = _AlaMldTunnelNextDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1, 8),
    _AlaMldTunnelNextDestAddress_Type()
)
alaMldTunnelNextDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldTunnelNextDestAddress.setStatus("current")


class _AlaMldTunnelNextType_Type(Integer32):
    """Custom type alaMldTunnelNextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2))
    )


_AlaMldTunnelNextType_Type.__name__ = "Integer32"
_AlaMldTunnelNextType_Object = MibTableColumn
alaMldTunnelNextType = _AlaMldTunnelNextType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 11, 1, 1, 9),
    _AlaMldTunnelNextType_Type()
)
alaMldTunnelNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldTunnelNextType.setStatus("current")
_AlaMldPort_ObjectIdentity = ObjectIdentity
alaMldPort = _AlaMldPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 12)
)
_AlaMldPortTable_Object = MibTable
alaMldPortTable = _AlaMldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    alaMldPortTable.setStatus("current")
_AlaMldPortEntry_Object = MibTableRow
alaMldPortEntry = _AlaMldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 12, 1, 1)
)
alaMldPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldPortIfIndex"),
)
if mibBuilder.loadTexts:
    alaMldPortEntry.setStatus("current")
_AlaMldPortIfIndex_Type = InterfaceIndex
_AlaMldPortIfIndex_Object = MibTableColumn
alaMldPortIfIndex = _AlaMldPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 12, 1, 1, 1),
    _AlaMldPortIfIndex_Type()
)
alaMldPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldPortIfIndex.setStatus("current")


class _AlaMldPortMaxGroupLimit_Type(Unsigned32):
    """Custom type alaMldPortMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaMldPortMaxGroupLimit_Object = MibTableColumn
alaMldPortMaxGroupLimit = _AlaMldPortMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 12, 1, 1, 2),
    _AlaMldPortMaxGroupLimit_Type()
)
alaMldPortMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldPortMaxGroupLimit.setStatus("current")


class _AlaMldPortMaxGroupExceedAction_Type(Integer32):
    """Custom type alaMldPortMaxGroupExceedAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("none", 0),
          ("replace", 2))
    )


_AlaMldPortMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaMldPortMaxGroupExceedAction_Object = MibTableColumn
alaMldPortMaxGroupExceedAction = _AlaMldPortMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 12, 1, 1, 3),
    _AlaMldPortMaxGroupExceedAction_Type()
)
alaMldPortMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldPortMaxGroupExceedAction.setStatus("current")
_AlaMldPortVlan_ObjectIdentity = ObjectIdentity
alaMldPortVlan = _AlaMldPortVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 13)
)
_AlaMldPortVlanTable_Object = MibTable
alaMldPortVlanTable = _AlaMldPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    alaMldPortVlanTable.setStatus("current")
_AlaMldPortVlanEntry_Object = MibTableRow
alaMldPortVlanEntry = _AlaMldPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 13, 1, 1)
)
alaMldPortVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldPortIfIndex"),
    (0, "ALCATEL-IND1-MLD-MIB", "alaMldVlanId"),
)
if mibBuilder.loadTexts:
    alaMldPortVlanEntry.setStatus("current")
_AlaMldVlanId_Type = Unsigned32
_AlaMldVlanId_Object = MibTableColumn
alaMldVlanId = _AlaMldVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 13, 1, 1, 1),
    _AlaMldVlanId_Type()
)
alaMldVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldVlanId.setStatus("current")
_AlaMldPortVlanCurrentGroupCount_Type = Unsigned32
_AlaMldPortVlanCurrentGroupCount_Object = MibTableColumn
alaMldPortVlanCurrentGroupCount = _AlaMldPortVlanCurrentGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 13, 1, 1, 2),
    _AlaMldPortVlanCurrentGroupCount_Type()
)
alaMldPortVlanCurrentGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldPortVlanCurrentGroupCount.setStatus("current")
_AlaMldPortVlanMaxGroupLimit_Type = Unsigned32
_AlaMldPortVlanMaxGroupLimit_Object = MibTableColumn
alaMldPortVlanMaxGroupLimit = _AlaMldPortVlanMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 13, 1, 1, 3),
    _AlaMldPortVlanMaxGroupLimit_Type()
)
alaMldPortVlanMaxGroupLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldPortVlanMaxGroupLimit.setStatus("current")


class _AlaMldPortVlanMaxGroupExceedAction_Type(Integer32):
    """Custom type alaMldPortVlanMaxGroupExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("none", 0),
          ("replace", 2))
    )


_AlaMldPortVlanMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaMldPortVlanMaxGroupExceedAction_Object = MibTableColumn
alaMldPortVlanMaxGroupExceedAction = _AlaMldPortVlanMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 1, 13, 1, 1, 4),
    _AlaMldPortVlanMaxGroupExceedAction_Type()
)
alaMldPortVlanMaxGroupExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldPortVlanMaxGroupExceedAction.setStatus("current")
_AlcatelIND1MldMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1MldMIBConformance = _AlcatelIND1MldMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2)
)
_AlcatelIND1MldMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1MldMIBCompliances = _AlcatelIND1MldMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 1)
)
_AlcatelIND1MldMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1MldMIBGroups = _AlcatelIND1MldMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2)
)

# Managed Objects groups

alaMldGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 1)
)
alaMldGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldStatus"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldQuerying"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldSpoofing"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldZapping"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVersion"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldRobustness"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldQueryInterval"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldQueryResponseInterval"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldLastMemberQueryInterval"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldRouterTimeout"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldSourceTimeout"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldProxying"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldUnsolicitedReportInterval"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldQuerierForwarding"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldMaxGroupLimit"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldMaxGroupExceedAction"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldFloodUnknown"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldHelperAddressType"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldHelperAddress"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldZeroBasedQuery"))
)
if mibBuilder.loadTexts:
    alaMldGroup.setStatus("current")

alaMldVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 2)
)
alaMldVlanGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldVlanStatus"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanQuerying"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanSpoofing"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanZapping"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanVersion"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanRobustness"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanQueryInterval"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanQueryResponseInterval"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanLastMemberQueryInterval"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanRouterTimeout"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanSourceTimeout"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanProxying"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanUnsolicitedReportInterval"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanQuerierForwarding"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanMaxGroupLimit"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanMaxGroupExceedAction"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldVlanZeroBasedQuery"))
)
if mibBuilder.loadTexts:
    alaMldVlanGroup.setStatus("current")

alaMldMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 3)
)
alaMldMemberGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldMemberMode"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldMemberCount"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldMemberTimeout"))
)
if mibBuilder.loadTexts:
    alaMldMemberGroup.setStatus("current")

alaMldStaticMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 4)
)
alaMldStaticMemberGroup.setObjects(
    ("ALCATEL-IND1-MLD-MIB", "alaMldStaticMemberRowStatus")
)
if mibBuilder.loadTexts:
    alaMldStaticMemberGroup.setStatus("current")

alaMldNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 5)
)
alaMldNeighborGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldNeighborCount"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldNeighborTimeout"))
)
if mibBuilder.loadTexts:
    alaMldNeighborGroup.setStatus("current")

alaMldStaticNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 6)
)
alaMldStaticNeighborGroup.setObjects(
    ("ALCATEL-IND1-MLD-MIB", "alaMldStaticNeighborRowStatus")
)
if mibBuilder.loadTexts:
    alaMldStaticNeighborGroup.setStatus("current")

alaMldQuerierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 7)
)
alaMldQuerierGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldQuerierCount"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldQuerierTimeout"))
)
if mibBuilder.loadTexts:
    alaMldQuerierGroup.setStatus("current")

alaMldStaticQuerierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 8)
)
alaMldStaticQuerierGroup.setObjects(
    ("ALCATEL-IND1-MLD-MIB", "alaMldStaticQuerierRowStatus")
)
if mibBuilder.loadTexts:
    alaMldStaticQuerierGroup.setStatus("current")

alaMldSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 9)
)
alaMldSourceGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldSourceIfIndex"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldSourceType"))
)
if mibBuilder.loadTexts:
    alaMldSourceGroup.setStatus("current")

alaMldForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 10)
)
alaMldForwardGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldForwardIfIndex"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldForwardType"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldForwardNextType"))
)
if mibBuilder.loadTexts:
    alaMldForwardGroup.setStatus("current")

alaMldTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 11)
)
alaMldTunnelGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldTunnelIfIndex"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldTunnelType"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldTunnelNextType"))
)
if mibBuilder.loadTexts:
    alaMldTunnelGroup.setStatus("current")

alaMldPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 12)
)
alaMldPortGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldPortMaxGroupLimit"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldPortMaxGroupExceedAction"))
)
if mibBuilder.loadTexts:
    alaMldPortGroup.setStatus("current")

alaMldPortVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 2, 13)
)
alaMldPortVlanGroup.setObjects(
      *(("ALCATEL-IND1-MLD-MIB", "alaMldPortVlanCurrentGroupCount"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldPortVlanMaxGroupLimit"),
        ("ALCATEL-IND1-MLD-MIB", "alaMldPortVlanMaxGroupExceedAction"))
)
if mibBuilder.loadTexts:
    alaMldPortVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaMldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 35, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaMldCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-MLD-MIB",
    **{"alcatelIND1MldMIB": alcatelIND1MldMIB,
       "alcatelIND1MldMIBObjects": alcatelIND1MldMIBObjects,
       "alaMld": alaMld,
       "alaMldStatus": alaMldStatus,
       "alaMldQuerying": alaMldQuerying,
       "alaMldSpoofing": alaMldSpoofing,
       "alaMldZapping": alaMldZapping,
       "alaMldVersion": alaMldVersion,
       "alaMldRobustness": alaMldRobustness,
       "alaMldQueryInterval": alaMldQueryInterval,
       "alaMldQueryResponseInterval": alaMldQueryResponseInterval,
       "alaMldLastMemberQueryInterval": alaMldLastMemberQueryInterval,
       "alaMldRouterTimeout": alaMldRouterTimeout,
       "alaMldSourceTimeout": alaMldSourceTimeout,
       "alaMldProxying": alaMldProxying,
       "alaMldUnsolicitedReportInterval": alaMldUnsolicitedReportInterval,
       "alaMldQuerierForwarding": alaMldQuerierForwarding,
       "alaMldMaxGroupLimit": alaMldMaxGroupLimit,
       "alaMldMaxGroupExceedAction": alaMldMaxGroupExceedAction,
       "alaMldFloodUnknown": alaMldFloodUnknown,
       "alaMldHelperAddressType": alaMldHelperAddressType,
       "alaMldHelperAddress": alaMldHelperAddress,
       "alaMldZeroBasedQuery": alaMldZeroBasedQuery,
       "alaMldVlan": alaMldVlan,
       "alaMldVlanTable": alaMldVlanTable,
       "alaMldVlanEntry": alaMldVlanEntry,
       "alaMldVlanIndex": alaMldVlanIndex,
       "alaMldVlanStatus": alaMldVlanStatus,
       "alaMldVlanQuerying": alaMldVlanQuerying,
       "alaMldVlanSpoofing": alaMldVlanSpoofing,
       "alaMldVlanZapping": alaMldVlanZapping,
       "alaMldVlanVersion": alaMldVlanVersion,
       "alaMldVlanRobustness": alaMldVlanRobustness,
       "alaMldVlanQueryInterval": alaMldVlanQueryInterval,
       "alaMldVlanQueryResponseInterval": alaMldVlanQueryResponseInterval,
       "alaMldVlanLastMemberQueryInterval": alaMldVlanLastMemberQueryInterval,
       "alaMldVlanRouterTimeout": alaMldVlanRouterTimeout,
       "alaMldVlanSourceTimeout": alaMldVlanSourceTimeout,
       "alaMldVlanProxying": alaMldVlanProxying,
       "alaMldVlanUnsolicitedReportInterval": alaMldVlanUnsolicitedReportInterval,
       "alaMldVlanQuerierForwarding": alaMldVlanQuerierForwarding,
       "alaMldVlanMaxGroupLimit": alaMldVlanMaxGroupLimit,
       "alaMldVlanMaxGroupExceedAction": alaMldVlanMaxGroupExceedAction,
       "alaMldVlanZeroBasedQuery": alaMldVlanZeroBasedQuery,
       "alaMldMember": alaMldMember,
       "alaMldMemberTable": alaMldMemberTable,
       "alaMldMemberEntry": alaMldMemberEntry,
       "alaMldMemberVlan": alaMldMemberVlan,
       "alaMldMemberIfIndex": alaMldMemberIfIndex,
       "alaMldMemberGroupAddress": alaMldMemberGroupAddress,
       "alaMldMemberSourceAddress": alaMldMemberSourceAddress,
       "alaMldMemberMode": alaMldMemberMode,
       "alaMldMemberCount": alaMldMemberCount,
       "alaMldMemberTimeout": alaMldMemberTimeout,
       "alaMldStaticMember": alaMldStaticMember,
       "alaMldStaticMemberTable": alaMldStaticMemberTable,
       "alaMldStaticMemberEntry": alaMldStaticMemberEntry,
       "alaMldStaticMemberVlan": alaMldStaticMemberVlan,
       "alaMldStaticMemberIfIndex": alaMldStaticMemberIfIndex,
       "alaMldStaticMemberGroupAddress": alaMldStaticMemberGroupAddress,
       "alaMldStaticMemberRowStatus": alaMldStaticMemberRowStatus,
       "alaMldNeighbor": alaMldNeighbor,
       "alaMldNeighborTable": alaMldNeighborTable,
       "alaMldNeighborEntry": alaMldNeighborEntry,
       "alaMldNeighborVlan": alaMldNeighborVlan,
       "alaMldNeighborIfIndex": alaMldNeighborIfIndex,
       "alaMldNeighborHostAddress": alaMldNeighborHostAddress,
       "alaMldNeighborCount": alaMldNeighborCount,
       "alaMldNeighborTimeout": alaMldNeighborTimeout,
       "alaMldStaticNeighbor": alaMldStaticNeighbor,
       "alaMldStaticNeighborTable": alaMldStaticNeighborTable,
       "alaMldStaticNeighborEntry": alaMldStaticNeighborEntry,
       "alaMldStaticNeighborVlan": alaMldStaticNeighborVlan,
       "alaMldStaticNeighborIfIndex": alaMldStaticNeighborIfIndex,
       "alaMldStaticNeighborRowStatus": alaMldStaticNeighborRowStatus,
       "alaMldQuerier": alaMldQuerier,
       "alaMldQuerierTable": alaMldQuerierTable,
       "alaMldQuerierEntry": alaMldQuerierEntry,
       "alaMldQuerierVlan": alaMldQuerierVlan,
       "alaMldQuerierIfIndex": alaMldQuerierIfIndex,
       "alaMldQuerierHostAddress": alaMldQuerierHostAddress,
       "alaMldQuerierCount": alaMldQuerierCount,
       "alaMldQuerierTimeout": alaMldQuerierTimeout,
       "alaMldStaticQuerier": alaMldStaticQuerier,
       "alaMldStaticQuerierTable": alaMldStaticQuerierTable,
       "alaMldStaticQuerierEntry": alaMldStaticQuerierEntry,
       "alaMldStaticQuerierVlan": alaMldStaticQuerierVlan,
       "alaMldStaticQuerierIfIndex": alaMldStaticQuerierIfIndex,
       "alaMldStaticQuerierRowStatus": alaMldStaticQuerierRowStatus,
       "alaMldSource": alaMldSource,
       "alaMldSourceTable": alaMldSourceTable,
       "alaMldSourceEntry": alaMldSourceEntry,
       "alaMldSourceVlan": alaMldSourceVlan,
       "alaMldSourceIfIndex": alaMldSourceIfIndex,
       "alaMldSourceGroupAddress": alaMldSourceGroupAddress,
       "alaMldSourceHostAddress": alaMldSourceHostAddress,
       "alaMldSourceDestAddress": alaMldSourceDestAddress,
       "alaMldSourceOrigAddress": alaMldSourceOrigAddress,
       "alaMldSourceType": alaMldSourceType,
       "alaMldForward": alaMldForward,
       "alaMldForwardTable": alaMldForwardTable,
       "alaMldForwardEntry": alaMldForwardEntry,
       "alaMldForwardVlan": alaMldForwardVlan,
       "alaMldForwardIfIndex": alaMldForwardIfIndex,
       "alaMldForwardGroupAddress": alaMldForwardGroupAddress,
       "alaMldForwardHostAddress": alaMldForwardHostAddress,
       "alaMldForwardDestAddress": alaMldForwardDestAddress,
       "alaMldForwardOrigAddress": alaMldForwardOrigAddress,
       "alaMldForwardType": alaMldForwardType,
       "alaMldForwardNextVlan": alaMldForwardNextVlan,
       "alaMldForwardNextIfIndex": alaMldForwardNextIfIndex,
       "alaMldForwardNextType": alaMldForwardNextType,
       "alaMldTunnel": alaMldTunnel,
       "alaMldTunnelTable": alaMldTunnelTable,
       "alaMldTunnelEntry": alaMldTunnelEntry,
       "alaMldTunnelVlan": alaMldTunnelVlan,
       "alaMldTunnelIfIndex": alaMldTunnelIfIndex,
       "alaMldTunnelGroupAddress": alaMldTunnelGroupAddress,
       "alaMldTunnelHostAddress": alaMldTunnelHostAddress,
       "alaMldTunnelDestAddress": alaMldTunnelDestAddress,
       "alaMldTunnelOrigAddress": alaMldTunnelOrigAddress,
       "alaMldTunnelType": alaMldTunnelType,
       "alaMldTunnelNextDestAddress": alaMldTunnelNextDestAddress,
       "alaMldTunnelNextType": alaMldTunnelNextType,
       "alaMldPort": alaMldPort,
       "alaMldPortTable": alaMldPortTable,
       "alaMldPortEntry": alaMldPortEntry,
       "alaMldPortIfIndex": alaMldPortIfIndex,
       "alaMldPortMaxGroupLimit": alaMldPortMaxGroupLimit,
       "alaMldPortMaxGroupExceedAction": alaMldPortMaxGroupExceedAction,
       "alaMldPortVlan": alaMldPortVlan,
       "alaMldPortVlanTable": alaMldPortVlanTable,
       "alaMldPortVlanEntry": alaMldPortVlanEntry,
       "alaMldVlanId": alaMldVlanId,
       "alaMldPortVlanCurrentGroupCount": alaMldPortVlanCurrentGroupCount,
       "alaMldPortVlanMaxGroupLimit": alaMldPortVlanMaxGroupLimit,
       "alaMldPortVlanMaxGroupExceedAction": alaMldPortVlanMaxGroupExceedAction,
       "alcatelIND1MldMIBConformance": alcatelIND1MldMIBConformance,
       "alcatelIND1MldMIBCompliances": alcatelIND1MldMIBCompliances,
       "alaMldCompliance": alaMldCompliance,
       "alcatelIND1MldMIBGroups": alcatelIND1MldMIBGroups,
       "alaMldGroup": alaMldGroup,
       "alaMldVlanGroup": alaMldVlanGroup,
       "alaMldMemberGroup": alaMldMemberGroup,
       "alaMldStaticMemberGroup": alaMldStaticMemberGroup,
       "alaMldNeighborGroup": alaMldNeighborGroup,
       "alaMldStaticNeighborGroup": alaMldStaticNeighborGroup,
       "alaMldQuerierGroup": alaMldQuerierGroup,
       "alaMldStaticQuerierGroup": alaMldStaticQuerierGroup,
       "alaMldSourceGroup": alaMldSourceGroup,
       "alaMldForwardGroup": alaMldForwardGroup,
       "alaMldTunnelGroup": alaMldTunnelGroup,
       "alaMldPortGroup": alaMldPortGroup,
       "alaMldPortVlanGroup": alaMldPortVlanGroup}
)
