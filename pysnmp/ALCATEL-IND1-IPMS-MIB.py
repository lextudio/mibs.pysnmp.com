# SNMP MIB module (ALCATEL-IND1-IPMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-IPMS-MIB
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

(softentIND1Ipms,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Ipms")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1IPMSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1)
)
alcatelIND1IPMSMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPMSMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPMSMIBObjects = _AlcatelIND1IPMSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1)
)
_AlaIpmsConfig_ObjectIdentity = ObjectIdentity
alaIpmsConfig = _AlaIpmsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1)
)


class _AlaIpmsStatus_Type(Integer32):
    """Custom type alaIpmsStatus based on Integer32"""
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


_AlaIpmsStatus_Type.__name__ = "Integer32"
_AlaIpmsStatus_Object = MibScalar
alaIpmsStatus = _AlaIpmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 1),
    _AlaIpmsStatus_Type()
)
alaIpmsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsStatus.setStatus("current")


class _AlaIpmsLeaveTimeout_Type(Unsigned32):
    """Custom type alaIpmsLeaveTimeout based on Unsigned32"""
    defaultValue = 1


_AlaIpmsLeaveTimeout_Object = MibScalar
alaIpmsLeaveTimeout = _AlaIpmsLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 2),
    _AlaIpmsLeaveTimeout_Type()
)
alaIpmsLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsLeaveTimeout.setStatus("current")


class _AlaIpmsQueryInterval_Type(Unsigned32):
    """Custom type alaIpmsQueryInterval based on Unsigned32"""
    defaultValue = 125


_AlaIpmsQueryInterval_Object = MibScalar
alaIpmsQueryInterval = _AlaIpmsQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 3),
    _AlaIpmsQueryInterval_Type()
)
alaIpmsQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsQueryInterval.setStatus("current")


class _AlaIpmsNeighborTimer_Type(Unsigned32):
    """Custom type alaIpmsNeighborTimer based on Unsigned32"""
    defaultValue = 90


_AlaIpmsNeighborTimer_Object = MibScalar
alaIpmsNeighborTimer = _AlaIpmsNeighborTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 4),
    _AlaIpmsNeighborTimer_Type()
)
alaIpmsNeighborTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsNeighborTimer.setStatus("current")


class _AlaIpmsQuerierTimer_Type(Unsigned32):
    """Custom type alaIpmsQuerierTimer based on Unsigned32"""
    defaultValue = 260


_AlaIpmsQuerierTimer_Object = MibScalar
alaIpmsQuerierTimer = _AlaIpmsQuerierTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 5),
    _AlaIpmsQuerierTimer_Type()
)
alaIpmsQuerierTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsQuerierTimer.setStatus("current")


class _AlaIpmsMembershipTimer_Type(Unsigned32):
    """Custom type alaIpmsMembershipTimer based on Unsigned32"""
    defaultValue = 260


_AlaIpmsMembershipTimer_Object = MibScalar
alaIpmsMembershipTimer = _AlaIpmsMembershipTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 6),
    _AlaIpmsMembershipTimer_Type()
)
alaIpmsMembershipTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsMembershipTimer.setStatus("current")


class _AlaIpmsPriority_Type(Integer32):
    """Custom type alaIpmsPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 0),
          ("medium", 1),
          ("unsupported", 4),
          ("urgent", 3))
    )


_AlaIpmsPriority_Type.__name__ = "Integer32"
_AlaIpmsPriority_Object = MibScalar
alaIpmsPriority = _AlaIpmsPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 7),
    _AlaIpmsPriority_Type()
)
alaIpmsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsPriority.setStatus("current")


class _AlaIpmsMaxBandwidth_Type(Unsigned32):
    """Custom type alaIpmsMaxBandwidth based on Unsigned32"""
    defaultValue = 10


_AlaIpmsMaxBandwidth_Object = MibScalar
alaIpmsMaxBandwidth = _AlaIpmsMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 8),
    _AlaIpmsMaxBandwidth_Type()
)
alaIpmsMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsMaxBandwidth.setStatus("current")


class _AlaIpmsHardwareRoute_Type(Integer32):
    """Custom type alaIpmsHardwareRoute based on Integer32"""
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
          ("unsupported", 0))
    )


_AlaIpmsHardwareRoute_Type.__name__ = "Integer32"
_AlaIpmsHardwareRoute_Object = MibScalar
alaIpmsHardwareRoute = _AlaIpmsHardwareRoute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 9),
    _AlaIpmsHardwareRoute_Type()
)
alaIpmsHardwareRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsHardwareRoute.setStatus("current")


class _AlaIpmsIGMPMembershipProxyVersion_Type(Integer32):
    """Custom type alaIpmsIGMPMembershipProxyVersion based on Integer32"""
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
        *(("igmpv1", 1),
          ("igmpv2", 2),
          ("igmpv3", 3))
    )


_AlaIpmsIGMPMembershipProxyVersion_Type.__name__ = "Integer32"
_AlaIpmsIGMPMembershipProxyVersion_Object = MibScalar
alaIpmsIGMPMembershipProxyVersion = _AlaIpmsIGMPMembershipProxyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 10),
    _AlaIpmsIGMPMembershipProxyVersion_Type()
)
alaIpmsIGMPMembershipProxyVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsIGMPMembershipProxyVersion.setStatus("current")


class _AlaIpmsOtherQuerierTimer_Type(Unsigned32):
    """Custom type alaIpmsOtherQuerierTimer based on Unsigned32"""
    defaultValue = 255


_AlaIpmsOtherQuerierTimer_Object = MibScalar
alaIpmsOtherQuerierTimer = _AlaIpmsOtherQuerierTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 1, 11),
    _AlaIpmsOtherQuerierTimer_Type()
)
alaIpmsOtherQuerierTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsOtherQuerierTimer.setStatus("current")
_AlaIpmsGroup_ObjectIdentity = ObjectIdentity
alaIpmsGroup = _AlaIpmsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2)
)
_AlaIpmsGroupTable_Object = MibTable
alaIpmsGroupTable = _AlaIpmsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIpmsGroupTable.setStatus("current")
_AlaIpmsGroupEntry_Object = MibTableRow
alaIpmsGroupEntry = _AlaIpmsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1)
)
alaIpmsGroupEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupDestIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupClientIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupClientVlan"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupClientIfIndex"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupClientVci"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupIGMPVersion"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupIGMPv3SrcIP"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupIGMPv3SrcType"),
)
if mibBuilder.loadTexts:
    alaIpmsGroupEntry.setStatus("current")
_AlaIpmsGroupDestIpAddr_Type = IpAddress
_AlaIpmsGroupDestIpAddr_Object = MibTableColumn
alaIpmsGroupDestIpAddr = _AlaIpmsGroupDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 1),
    _AlaIpmsGroupDestIpAddr_Type()
)
alaIpmsGroupDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsGroupDestIpAddr.setStatus("current")
_AlaIpmsGroupClientIpAddr_Type = IpAddress
_AlaIpmsGroupClientIpAddr_Object = MibTableColumn
alaIpmsGroupClientIpAddr = _AlaIpmsGroupClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 2),
    _AlaIpmsGroupClientIpAddr_Type()
)
alaIpmsGroupClientIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsGroupClientIpAddr.setStatus("current")
_AlaIpmsGroupClientMacAddr_Type = MacAddress
_AlaIpmsGroupClientMacAddr_Object = MibTableColumn
alaIpmsGroupClientMacAddr = _AlaIpmsGroupClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 3),
    _AlaIpmsGroupClientMacAddr_Type()
)
alaIpmsGroupClientMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsGroupClientMacAddr.setStatus("current")


class _AlaIpmsGroupClientVlan_Type(Integer32):
    """Custom type alaIpmsGroupClientVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsGroupClientVlan_Type.__name__ = "Integer32"
_AlaIpmsGroupClientVlan_Object = MibTableColumn
alaIpmsGroupClientVlan = _AlaIpmsGroupClientVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 4),
    _AlaIpmsGroupClientVlan_Type()
)
alaIpmsGroupClientVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsGroupClientVlan.setStatus("current")
_AlaIpmsGroupClientIfIndex_Type = InterfaceIndex
_AlaIpmsGroupClientIfIndex_Object = MibTableColumn
alaIpmsGroupClientIfIndex = _AlaIpmsGroupClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 5),
    _AlaIpmsGroupClientIfIndex_Type()
)
alaIpmsGroupClientIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsGroupClientIfIndex.setStatus("current")
_AlaIpmsGroupClientVci_Type = Unsigned32
_AlaIpmsGroupClientVci_Object = MibTableColumn
alaIpmsGroupClientVci = _AlaIpmsGroupClientVci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 6),
    _AlaIpmsGroupClientVci_Type()
)
alaIpmsGroupClientVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsGroupClientVci.setStatus("current")


class _AlaIpmsGroupIGMPVersion_Type(Integer32):
    """Custom type alaIpmsGroupIGMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1", 1),
          ("igmpv2", 2),
          ("igmpv3", 3))
    )


_AlaIpmsGroupIGMPVersion_Type.__name__ = "Integer32"
_AlaIpmsGroupIGMPVersion_Object = MibTableColumn
alaIpmsGroupIGMPVersion = _AlaIpmsGroupIGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 7),
    _AlaIpmsGroupIGMPVersion_Type()
)
alaIpmsGroupIGMPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsGroupIGMPVersion.setStatus("current")
_AlaIpmsGroupIGMPv3SrcIP_Type = IpAddress
_AlaIpmsGroupIGMPv3SrcIP_Object = MibTableColumn
alaIpmsGroupIGMPv3SrcIP = _AlaIpmsGroupIGMPv3SrcIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 8),
    _AlaIpmsGroupIGMPv3SrcIP_Type()
)
alaIpmsGroupIGMPv3SrcIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsGroupIGMPv3SrcIP.setStatus("current")


class _AlaIpmsGroupIGMPv3SrcType_Type(Integer32):
    """Custom type alaIpmsGroupIGMPv3SrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1),
          ("na", 0))
    )


_AlaIpmsGroupIGMPv3SrcType_Type.__name__ = "Integer32"
_AlaIpmsGroupIGMPv3SrcType_Object = MibTableColumn
alaIpmsGroupIGMPv3SrcType = _AlaIpmsGroupIGMPv3SrcType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 9),
    _AlaIpmsGroupIGMPv3SrcType_Type()
)
alaIpmsGroupIGMPv3SrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsGroupIGMPv3SrcType.setStatus("current")
_AlaIpmsGroupIGMPv3SrcTimeout_Type = Unsigned32
_AlaIpmsGroupIGMPv3SrcTimeout_Object = MibTableColumn
alaIpmsGroupIGMPv3SrcTimeout = _AlaIpmsGroupIGMPv3SrcTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 10),
    _AlaIpmsGroupIGMPv3SrcTimeout_Type()
)
alaIpmsGroupIGMPv3SrcTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsGroupIGMPv3SrcTimeout.setStatus("current")


class _AlaIpmsGroupIGMPv3GroupType_Type(Integer32):
    """Custom type alaIpmsGroupIGMPv3GroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1),
          ("na", 0))
    )


_AlaIpmsGroupIGMPv3GroupType_Type.__name__ = "Integer32"
_AlaIpmsGroupIGMPv3GroupType_Object = MibTableColumn
alaIpmsGroupIGMPv3GroupType = _AlaIpmsGroupIGMPv3GroupType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 11),
    _AlaIpmsGroupIGMPv3GroupType_Type()
)
alaIpmsGroupIGMPv3GroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsGroupIGMPv3GroupType.setStatus("current")
_AlaIpmsGroupTimeout_Type = Unsigned32
_AlaIpmsGroupTimeout_Object = MibTableColumn
alaIpmsGroupTimeout = _AlaIpmsGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 2, 1, 1, 12),
    _AlaIpmsGroupTimeout_Type()
)
alaIpmsGroupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsGroupTimeout.setStatus("current")
_AlaIpmsNeighbor_ObjectIdentity = ObjectIdentity
alaIpmsNeighbor = _AlaIpmsNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 3)
)
_AlaIpmsNeighborTable_Object = MibTable
alaIpmsNeighborTable = _AlaIpmsNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaIpmsNeighborTable.setStatus("current")
_AlaIpmsNeighborEntry_Object = MibTableRow
alaIpmsNeighborEntry = _AlaIpmsNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 3, 1, 1)
)
alaIpmsNeighborEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsNeighborIpAddr"),
)
if mibBuilder.loadTexts:
    alaIpmsNeighborEntry.setStatus("current")
_AlaIpmsNeighborIpAddr_Type = IpAddress
_AlaIpmsNeighborIpAddr_Object = MibTableColumn
alaIpmsNeighborIpAddr = _AlaIpmsNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 3, 1, 1, 1),
    _AlaIpmsNeighborIpAddr_Type()
)
alaIpmsNeighborIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsNeighborIpAddr.setStatus("current")


class _AlaIpmsNeighborVlan_Type(Integer32):
    """Custom type alaIpmsNeighborVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsNeighborVlan_Type.__name__ = "Integer32"
_AlaIpmsNeighborVlan_Object = MibTableColumn
alaIpmsNeighborVlan = _AlaIpmsNeighborVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 3, 1, 1, 2),
    _AlaIpmsNeighborVlan_Type()
)
alaIpmsNeighborVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsNeighborVlan.setStatus("current")
_AlaIpmsNeighborIfIndex_Type = InterfaceIndex
_AlaIpmsNeighborIfIndex_Object = MibTableColumn
alaIpmsNeighborIfIndex = _AlaIpmsNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 3, 1, 1, 3),
    _AlaIpmsNeighborIfIndex_Type()
)
alaIpmsNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsNeighborIfIndex.setStatus("current")
_AlaIpmsNeighborVci_Type = Unsigned32
_AlaIpmsNeighborVci_Object = MibTableColumn
alaIpmsNeighborVci = _AlaIpmsNeighborVci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 3, 1, 1, 4),
    _AlaIpmsNeighborVci_Type()
)
alaIpmsNeighborVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsNeighborVci.setStatus("current")


class _AlaIpmsNeighborType_Type(Integer32):
    """Custom type alaIpmsNeighborType based on Integer32"""
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
        *(("cmm", 3),
          ("ipip", 1),
          ("native", 0),
          ("pim", 2))
    )


_AlaIpmsNeighborType_Type.__name__ = "Integer32"
_AlaIpmsNeighborType_Object = MibTableColumn
alaIpmsNeighborType = _AlaIpmsNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 3, 1, 1, 5),
    _AlaIpmsNeighborType_Type()
)
alaIpmsNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsNeighborType.setStatus("current")
_AlaIpmsNeighborTimeout_Type = Unsigned32
_AlaIpmsNeighborTimeout_Object = MibTableColumn
alaIpmsNeighborTimeout = _AlaIpmsNeighborTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 3, 1, 1, 6),
    _AlaIpmsNeighborTimeout_Type()
)
alaIpmsNeighborTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsNeighborTimeout.setStatus("current")
_AlaIpmsStaticNeighbor_ObjectIdentity = ObjectIdentity
alaIpmsStaticNeighbor = _AlaIpmsStaticNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 4)
)
_AlaIpmsStaticNeighborTable_Object = MibTable
alaIpmsStaticNeighborTable = _AlaIpmsStaticNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaIpmsStaticNeighborTable.setStatus("current")
_AlaIpmsStaticNeighborEntry_Object = MibTableRow
alaIpmsStaticNeighborEntry = _AlaIpmsStaticNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 4, 1, 1)
)
alaIpmsStaticNeighborEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticNeighborVlan"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticNeighborIfIndex"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticNeighborVci"),
)
if mibBuilder.loadTexts:
    alaIpmsStaticNeighborEntry.setStatus("current")


class _AlaIpmsStaticNeighborVlan_Type(Integer32):
    """Custom type alaIpmsStaticNeighborVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsStaticNeighborVlan_Type.__name__ = "Integer32"
_AlaIpmsStaticNeighborVlan_Object = MibTableColumn
alaIpmsStaticNeighborVlan = _AlaIpmsStaticNeighborVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 4, 1, 1, 1),
    _AlaIpmsStaticNeighborVlan_Type()
)
alaIpmsStaticNeighborVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticNeighborVlan.setStatus("current")
_AlaIpmsStaticNeighborIfIndex_Type = InterfaceIndex
_AlaIpmsStaticNeighborIfIndex_Object = MibTableColumn
alaIpmsStaticNeighborIfIndex = _AlaIpmsStaticNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 4, 1, 1, 2),
    _AlaIpmsStaticNeighborIfIndex_Type()
)
alaIpmsStaticNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticNeighborIfIndex.setStatus("current")
_AlaIpmsStaticNeighborVci_Type = Unsigned32
_AlaIpmsStaticNeighborVci_Object = MibTableColumn
alaIpmsStaticNeighborVci = _AlaIpmsStaticNeighborVci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 4, 1, 1, 3),
    _AlaIpmsStaticNeighborVci_Type()
)
alaIpmsStaticNeighborVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticNeighborVci.setStatus("current")


class _AlaIpmsStaticNeighborIGMPVersion_Type(Integer32):
    """Custom type alaIpmsStaticNeighborIGMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv2", 2),
          ("igmpv3", 3))
    )


_AlaIpmsStaticNeighborIGMPVersion_Type.__name__ = "Integer32"
_AlaIpmsStaticNeighborIGMPVersion_Object = MibTableColumn
alaIpmsStaticNeighborIGMPVersion = _AlaIpmsStaticNeighborIGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 4, 1, 1, 4),
    _AlaIpmsStaticNeighborIGMPVersion_Type()
)
alaIpmsStaticNeighborIGMPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsStaticNeighborIGMPVersion.setStatus("current")
_AlaIpmsStaticNeighborRowStatus_Type = RowStatus
_AlaIpmsStaticNeighborRowStatus_Object = MibTableColumn
alaIpmsStaticNeighborRowStatus = _AlaIpmsStaticNeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 4, 1, 1, 5),
    _AlaIpmsStaticNeighborRowStatus_Type()
)
alaIpmsStaticNeighborRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsStaticNeighborRowStatus.setStatus("current")
_AlaIpmsQuerier_ObjectIdentity = ObjectIdentity
alaIpmsQuerier = _AlaIpmsQuerier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 5)
)
_AlaIpmsQuerierTable_Object = MibTable
alaIpmsQuerierTable = _AlaIpmsQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaIpmsQuerierTable.setStatus("current")
_AlaIpmsQuerierEntry_Object = MibTableRow
alaIpmsQuerierEntry = _AlaIpmsQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 5, 1, 1)
)
alaIpmsQuerierEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsQuerierIpAddr"),
)
if mibBuilder.loadTexts:
    alaIpmsQuerierEntry.setStatus("current")
_AlaIpmsQuerierIpAddr_Type = IpAddress
_AlaIpmsQuerierIpAddr_Object = MibTableColumn
alaIpmsQuerierIpAddr = _AlaIpmsQuerierIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 5, 1, 1, 1),
    _AlaIpmsQuerierIpAddr_Type()
)
alaIpmsQuerierIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsQuerierIpAddr.setStatus("current")


class _AlaIpmsQuerierVlan_Type(Integer32):
    """Custom type alaIpmsQuerierVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsQuerierVlan_Type.__name__ = "Integer32"
_AlaIpmsQuerierVlan_Object = MibTableColumn
alaIpmsQuerierVlan = _AlaIpmsQuerierVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 5, 1, 1, 2),
    _AlaIpmsQuerierVlan_Type()
)
alaIpmsQuerierVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsQuerierVlan.setStatus("current")
_AlaIpmsQuerierIfIndex_Type = InterfaceIndex
_AlaIpmsQuerierIfIndex_Object = MibTableColumn
alaIpmsQuerierIfIndex = _AlaIpmsQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 5, 1, 1, 3),
    _AlaIpmsQuerierIfIndex_Type()
)
alaIpmsQuerierIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsQuerierIfIndex.setStatus("current")
_AlaIpmsQuerierVci_Type = Unsigned32
_AlaIpmsQuerierVci_Object = MibTableColumn
alaIpmsQuerierVci = _AlaIpmsQuerierVci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 5, 1, 1, 4),
    _AlaIpmsQuerierVci_Type()
)
alaIpmsQuerierVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsQuerierVci.setStatus("current")


class _AlaIpmsQuerierType_Type(Integer32):
    """Custom type alaIpmsQuerierType based on Integer32"""
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
        *(("cmm", 3),
          ("ipip", 1),
          ("native", 0),
          ("pim", 2))
    )


_AlaIpmsQuerierType_Type.__name__ = "Integer32"
_AlaIpmsQuerierType_Object = MibTableColumn
alaIpmsQuerierType = _AlaIpmsQuerierType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 5, 1, 1, 5),
    _AlaIpmsQuerierType_Type()
)
alaIpmsQuerierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsQuerierType.setStatus("current")
_AlaIpmsQuerierTimeout_Type = Unsigned32
_AlaIpmsQuerierTimeout_Object = MibTableColumn
alaIpmsQuerierTimeout = _AlaIpmsQuerierTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 5, 1, 1, 6),
    _AlaIpmsQuerierTimeout_Type()
)
alaIpmsQuerierTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsQuerierTimeout.setStatus("current")
_AlaIpmsStaticQuerier_ObjectIdentity = ObjectIdentity
alaIpmsStaticQuerier = _AlaIpmsStaticQuerier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 6)
)
_AlaIpmsStaticQuerierTable_Object = MibTable
alaIpmsStaticQuerierTable = _AlaIpmsStaticQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alaIpmsStaticQuerierTable.setStatus("current")
_AlaIpmsStaticQuerierEntry_Object = MibTableRow
alaIpmsStaticQuerierEntry = _AlaIpmsStaticQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 6, 1, 1)
)
alaIpmsStaticQuerierEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticQuerierVlan"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticQuerierIfIndex"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticQuerierVci"),
)
if mibBuilder.loadTexts:
    alaIpmsStaticQuerierEntry.setStatus("current")


class _AlaIpmsStaticQuerierVlan_Type(Integer32):
    """Custom type alaIpmsStaticQuerierVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsStaticQuerierVlan_Type.__name__ = "Integer32"
_AlaIpmsStaticQuerierVlan_Object = MibTableColumn
alaIpmsStaticQuerierVlan = _AlaIpmsStaticQuerierVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 6, 1, 1, 1),
    _AlaIpmsStaticQuerierVlan_Type()
)
alaIpmsStaticQuerierVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticQuerierVlan.setStatus("current")
_AlaIpmsStaticQuerierIfIndex_Type = InterfaceIndex
_AlaIpmsStaticQuerierIfIndex_Object = MibTableColumn
alaIpmsStaticQuerierIfIndex = _AlaIpmsStaticQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 6, 1, 1, 2),
    _AlaIpmsStaticQuerierIfIndex_Type()
)
alaIpmsStaticQuerierIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticQuerierIfIndex.setStatus("current")
_AlaIpmsStaticQuerierVci_Type = Unsigned32
_AlaIpmsStaticQuerierVci_Object = MibTableColumn
alaIpmsStaticQuerierVci = _AlaIpmsStaticQuerierVci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 6, 1, 1, 3),
    _AlaIpmsStaticQuerierVci_Type()
)
alaIpmsStaticQuerierVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticQuerierVci.setStatus("current")


class _AlaIpmsStaticQuerierIGMPVersion_Type(Integer32):
    """Custom type alaIpmsStaticQuerierIGMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv2", 2),
          ("igmpv3", 3))
    )


_AlaIpmsStaticQuerierIGMPVersion_Type.__name__ = "Integer32"
_AlaIpmsStaticQuerierIGMPVersion_Object = MibTableColumn
alaIpmsStaticQuerierIGMPVersion = _AlaIpmsStaticQuerierIGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 6, 1, 1, 4),
    _AlaIpmsStaticQuerierIGMPVersion_Type()
)
alaIpmsStaticQuerierIGMPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsStaticQuerierIGMPVersion.setStatus("current")
_AlaIpmsStaticQuerierRowStatus_Type = RowStatus
_AlaIpmsStaticQuerierRowStatus_Object = MibTableColumn
alaIpmsStaticQuerierRowStatus = _AlaIpmsStaticQuerierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 6, 1, 1, 5),
    _AlaIpmsStaticQuerierRowStatus_Type()
)
alaIpmsStaticQuerierRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpmsStaticQuerierRowStatus.setStatus("current")
_AlaIpmsSource_ObjectIdentity = ObjectIdentity
alaIpmsSource = _AlaIpmsSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7)
)
_AlaIpmsSourceTable_Object = MibTable
alaIpmsSourceTable = _AlaIpmsSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaIpmsSourceTable.setStatus("current")
_AlaIpmsSourceEntry_Object = MibTableRow
alaIpmsSourceEntry = _AlaIpmsSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1)
)
alaIpmsSourceEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsSourceDestIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsSourceSrcIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsSourceSrcVlan"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsSourceSrcIfIndex"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsSourceUniIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsSourceSrcVci"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsSourceSrcType"),
)
if mibBuilder.loadTexts:
    alaIpmsSourceEntry.setStatus("current")
_AlaIpmsSourceDestIpAddr_Type = IpAddress
_AlaIpmsSourceDestIpAddr_Object = MibTableColumn
alaIpmsSourceDestIpAddr = _AlaIpmsSourceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1, 1),
    _AlaIpmsSourceDestIpAddr_Type()
)
alaIpmsSourceDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsSourceDestIpAddr.setStatus("current")
_AlaIpmsSourceSrcIpAddr_Type = IpAddress
_AlaIpmsSourceSrcIpAddr_Object = MibTableColumn
alaIpmsSourceSrcIpAddr = _AlaIpmsSourceSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1, 2),
    _AlaIpmsSourceSrcIpAddr_Type()
)
alaIpmsSourceSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsSourceSrcIpAddr.setStatus("current")
_AlaIpmsSourceSrcMacAddr_Type = MacAddress
_AlaIpmsSourceSrcMacAddr_Object = MibTableColumn
alaIpmsSourceSrcMacAddr = _AlaIpmsSourceSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1, 3),
    _AlaIpmsSourceSrcMacAddr_Type()
)
alaIpmsSourceSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsSourceSrcMacAddr.setStatus("current")


class _AlaIpmsSourceSrcVlan_Type(Integer32):
    """Custom type alaIpmsSourceSrcVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsSourceSrcVlan_Type.__name__ = "Integer32"
_AlaIpmsSourceSrcVlan_Object = MibTableColumn
alaIpmsSourceSrcVlan = _AlaIpmsSourceSrcVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1, 4),
    _AlaIpmsSourceSrcVlan_Type()
)
alaIpmsSourceSrcVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsSourceSrcVlan.setStatus("current")
_AlaIpmsSourceSrcIfIndex_Type = InterfaceIndex
_AlaIpmsSourceSrcIfIndex_Object = MibTableColumn
alaIpmsSourceSrcIfIndex = _AlaIpmsSourceSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1, 5),
    _AlaIpmsSourceSrcIfIndex_Type()
)
alaIpmsSourceSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsSourceSrcIfIndex.setStatus("current")
_AlaIpmsSourceUniIpAddr_Type = IpAddress
_AlaIpmsSourceUniIpAddr_Object = MibTableColumn
alaIpmsSourceUniIpAddr = _AlaIpmsSourceUniIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1, 6),
    _AlaIpmsSourceUniIpAddr_Type()
)
alaIpmsSourceUniIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsSourceUniIpAddr.setStatus("current")
_AlaIpmsSourceSrcVci_Type = Unsigned32
_AlaIpmsSourceSrcVci_Object = MibTableColumn
alaIpmsSourceSrcVci = _AlaIpmsSourceSrcVci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1, 7),
    _AlaIpmsSourceSrcVci_Type()
)
alaIpmsSourceSrcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsSourceSrcVci.setStatus("current")


class _AlaIpmsSourceSrcType_Type(Integer32):
    """Custom type alaIpmsSourceSrcType based on Integer32"""
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
        *(("cmm", 3),
          ("ipip", 1),
          ("native", 0),
          ("pim", 2))
    )


_AlaIpmsSourceSrcType_Type.__name__ = "Integer32"
_AlaIpmsSourceSrcType_Object = MibTableColumn
alaIpmsSourceSrcType = _AlaIpmsSourceSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1, 8),
    _AlaIpmsSourceSrcType_Type()
)
alaIpmsSourceSrcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsSourceSrcType.setStatus("current")
_AlaIpmsSourceTimeout_Type = Unsigned32
_AlaIpmsSourceTimeout_Object = MibTableColumn
alaIpmsSourceTimeout = _AlaIpmsSourceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 7, 1, 1, 9),
    _AlaIpmsSourceTimeout_Type()
)
alaIpmsSourceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsSourceTimeout.setStatus("current")
_AlaIpmsForward_ObjectIdentity = ObjectIdentity
alaIpmsForward = _AlaIpmsForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8)
)
_AlaIpmsForwardTable_Object = MibTable
alaIpmsForwardTable = _AlaIpmsForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaIpmsForwardTable.setStatus("current")
_AlaIpmsForwardEntry_Object = MibTableRow
alaIpmsForwardEntry = _AlaIpmsForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1)
)
alaIpmsForwardEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardDestIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardSrcIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardDestVlan"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardSrcVlan"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardSrcIfIndex"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardUniIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardSrcVci"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardDestType"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardSrcType"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardDestIfIndex"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardDestTunIpAddr"),
)
if mibBuilder.loadTexts:
    alaIpmsForwardEntry.setStatus("current")
_AlaIpmsForwardDestIpAddr_Type = IpAddress
_AlaIpmsForwardDestIpAddr_Object = MibTableColumn
alaIpmsForwardDestIpAddr = _AlaIpmsForwardDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 1),
    _AlaIpmsForwardDestIpAddr_Type()
)
alaIpmsForwardDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardDestIpAddr.setStatus("current")
_AlaIpmsForwardSrcIpAddr_Type = IpAddress
_AlaIpmsForwardSrcIpAddr_Object = MibTableColumn
alaIpmsForwardSrcIpAddr = _AlaIpmsForwardSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 2),
    _AlaIpmsForwardSrcIpAddr_Type()
)
alaIpmsForwardSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardSrcIpAddr.setStatus("current")


class _AlaIpmsForwardDestVlan_Type(Integer32):
    """Custom type alaIpmsForwardDestVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsForwardDestVlan_Type.__name__ = "Integer32"
_AlaIpmsForwardDestVlan_Object = MibTableColumn
alaIpmsForwardDestVlan = _AlaIpmsForwardDestVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 3),
    _AlaIpmsForwardDestVlan_Type()
)
alaIpmsForwardDestVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardDestVlan.setStatus("current")


class _AlaIpmsForwardSrcVlan_Type(Integer32):
    """Custom type alaIpmsForwardSrcVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsForwardSrcVlan_Type.__name__ = "Integer32"
_AlaIpmsForwardSrcVlan_Object = MibTableColumn
alaIpmsForwardSrcVlan = _AlaIpmsForwardSrcVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 4),
    _AlaIpmsForwardSrcVlan_Type()
)
alaIpmsForwardSrcVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardSrcVlan.setStatus("current")
_AlaIpmsForwardSrcIfIndex_Type = InterfaceIndex
_AlaIpmsForwardSrcIfIndex_Object = MibTableColumn
alaIpmsForwardSrcIfIndex = _AlaIpmsForwardSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 5),
    _AlaIpmsForwardSrcIfIndex_Type()
)
alaIpmsForwardSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardSrcIfIndex.setStatus("current")
_AlaIpmsForwardUniIpAddr_Type = IpAddress
_AlaIpmsForwardUniIpAddr_Object = MibTableColumn
alaIpmsForwardUniIpAddr = _AlaIpmsForwardUniIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 6),
    _AlaIpmsForwardUniIpAddr_Type()
)
alaIpmsForwardUniIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardUniIpAddr.setStatus("current")
_AlaIpmsForwardSrcVci_Type = Unsigned32
_AlaIpmsForwardSrcVci_Object = MibTableColumn
alaIpmsForwardSrcVci = _AlaIpmsForwardSrcVci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 7),
    _AlaIpmsForwardSrcVci_Type()
)
alaIpmsForwardSrcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardSrcVci.setStatus("current")


class _AlaIpmsForwardDestType_Type(Integer32):
    """Custom type alaIpmsForwardDestType based on Integer32"""
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
        *(("cmm", 3),
          ("ipip", 1),
          ("native", 0),
          ("pim", 2))
    )


_AlaIpmsForwardDestType_Type.__name__ = "Integer32"
_AlaIpmsForwardDestType_Object = MibTableColumn
alaIpmsForwardDestType = _AlaIpmsForwardDestType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 8),
    _AlaIpmsForwardDestType_Type()
)
alaIpmsForwardDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardDestType.setStatus("current")


class _AlaIpmsForwardSrcType_Type(Integer32):
    """Custom type alaIpmsForwardSrcType based on Integer32"""
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
        *(("cmm", 3),
          ("ipip", 1),
          ("native", 0),
          ("pim", 2))
    )


_AlaIpmsForwardSrcType_Type.__name__ = "Integer32"
_AlaIpmsForwardSrcType_Object = MibTableColumn
alaIpmsForwardSrcType = _AlaIpmsForwardSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 9),
    _AlaIpmsForwardSrcType_Type()
)
alaIpmsForwardSrcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardSrcType.setStatus("current")
_AlaIpmsForwardDestTunIpAddr_Type = IpAddress
_AlaIpmsForwardDestTunIpAddr_Object = MibTableColumn
alaIpmsForwardDestTunIpAddr = _AlaIpmsForwardDestTunIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 10),
    _AlaIpmsForwardDestTunIpAddr_Type()
)
alaIpmsForwardDestTunIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardDestTunIpAddr.setStatus("current")
_AlaIpmsForwardSrcTunIpAddr_Type = IpAddress
_AlaIpmsForwardSrcTunIpAddr_Object = MibTableColumn
alaIpmsForwardSrcTunIpAddr = _AlaIpmsForwardSrcTunIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 11),
    _AlaIpmsForwardSrcTunIpAddr_Type()
)
alaIpmsForwardSrcTunIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsForwardSrcTunIpAddr.setStatus("current")
_AlaIpmsForwardRtrMacAddr_Type = MacAddress
_AlaIpmsForwardRtrMacAddr_Object = MibTableColumn
alaIpmsForwardRtrMacAddr = _AlaIpmsForwardRtrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 12),
    _AlaIpmsForwardRtrMacAddr_Type()
)
alaIpmsForwardRtrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsForwardRtrMacAddr.setStatus("current")


class _AlaIpmsForwardRtrTtl_Type(Integer32):
    """Custom type alaIpmsForwardRtrTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIpmsForwardRtrTtl_Type.__name__ = "Integer32"
_AlaIpmsForwardRtrTtl_Object = MibTableColumn
alaIpmsForwardRtrTtl = _AlaIpmsForwardRtrTtl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 13),
    _AlaIpmsForwardRtrTtl_Type()
)
alaIpmsForwardRtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsForwardRtrTtl.setStatus("current")
_AlaIpmsForwardDestIfIndex_Type = InterfaceIndex
_AlaIpmsForwardDestIfIndex_Object = MibTableColumn
alaIpmsForwardDestIfIndex = _AlaIpmsForwardDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 8, 1, 1, 14),
    _AlaIpmsForwardDestIfIndex_Type()
)
alaIpmsForwardDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsForwardDestIfIndex.setStatus("current")
_AlaIpmsPolicy_ObjectIdentity = ObjectIdentity
alaIpmsPolicy = _AlaIpmsPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9)
)
_AlaIpmsPolicyTable_Object = MibTable
alaIpmsPolicyTable = _AlaIpmsPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alaIpmsPolicyTable.setStatus("current")
_AlaIpmsPolicyEntry_Object = MibTableRow
alaIpmsPolicyEntry = _AlaIpmsPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1)
)
alaIpmsPolicyEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicyDestIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicySrcIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicySrcVlan"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicySrcIfIndex"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicyUniIpAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicySrcVci"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicySrcType"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicyPolicy"),
)
if mibBuilder.loadTexts:
    alaIpmsPolicyEntry.setStatus("current")
_AlaIpmsPolicyDestIpAddr_Type = IpAddress
_AlaIpmsPolicyDestIpAddr_Object = MibTableColumn
alaIpmsPolicyDestIpAddr = _AlaIpmsPolicyDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 1),
    _AlaIpmsPolicyDestIpAddr_Type()
)
alaIpmsPolicyDestIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsPolicyDestIpAddr.setStatus("current")
_AlaIpmsPolicySrcIpAddr_Type = IpAddress
_AlaIpmsPolicySrcIpAddr_Object = MibTableColumn
alaIpmsPolicySrcIpAddr = _AlaIpmsPolicySrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 2),
    _AlaIpmsPolicySrcIpAddr_Type()
)
alaIpmsPolicySrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsPolicySrcIpAddr.setStatus("current")
_AlaIpmsPolicySrcMacAddr_Type = MacAddress
_AlaIpmsPolicySrcMacAddr_Object = MibTableColumn
alaIpmsPolicySrcMacAddr = _AlaIpmsPolicySrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 3),
    _AlaIpmsPolicySrcMacAddr_Type()
)
alaIpmsPolicySrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsPolicySrcMacAddr.setStatus("current")


class _AlaIpmsPolicySrcVlan_Type(Integer32):
    """Custom type alaIpmsPolicySrcVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsPolicySrcVlan_Type.__name__ = "Integer32"
_AlaIpmsPolicySrcVlan_Object = MibTableColumn
alaIpmsPolicySrcVlan = _AlaIpmsPolicySrcVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 4),
    _AlaIpmsPolicySrcVlan_Type()
)
alaIpmsPolicySrcVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsPolicySrcVlan.setStatus("current")
_AlaIpmsPolicySrcIfIndex_Type = InterfaceIndex
_AlaIpmsPolicySrcIfIndex_Object = MibTableColumn
alaIpmsPolicySrcIfIndex = _AlaIpmsPolicySrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 5),
    _AlaIpmsPolicySrcIfIndex_Type()
)
alaIpmsPolicySrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsPolicySrcIfIndex.setStatus("current")
_AlaIpmsPolicyUniIpAddr_Type = IpAddress
_AlaIpmsPolicyUniIpAddr_Object = MibTableColumn
alaIpmsPolicyUniIpAddr = _AlaIpmsPolicyUniIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 6),
    _AlaIpmsPolicyUniIpAddr_Type()
)
alaIpmsPolicyUniIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsPolicyUniIpAddr.setStatus("current")
_AlaIpmsPolicySrcVci_Type = Unsigned32
_AlaIpmsPolicySrcVci_Object = MibTableColumn
alaIpmsPolicySrcVci = _AlaIpmsPolicySrcVci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 7),
    _AlaIpmsPolicySrcVci_Type()
)
alaIpmsPolicySrcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsPolicySrcVci.setStatus("current")


class _AlaIpmsPolicySrcType_Type(Integer32):
    """Custom type alaIpmsPolicySrcType based on Integer32"""
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
        *(("cmm", 3),
          ("ipip", 1),
          ("native", 0),
          ("pim", 2))
    )


_AlaIpmsPolicySrcType_Type.__name__ = "Integer32"
_AlaIpmsPolicySrcType_Object = MibTableColumn
alaIpmsPolicySrcType = _AlaIpmsPolicySrcType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 8),
    _AlaIpmsPolicySrcType_Type()
)
alaIpmsPolicySrcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsPolicySrcType.setStatus("current")


class _AlaIpmsPolicyPolicy_Type(Integer32):
    """Custom type alaIpmsPolicyPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("membership", 1)
    )


_AlaIpmsPolicyPolicy_Type.__name__ = "Integer32"
_AlaIpmsPolicyPolicy_Object = MibTableColumn
alaIpmsPolicyPolicy = _AlaIpmsPolicyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 9),
    _AlaIpmsPolicyPolicy_Type()
)
alaIpmsPolicyPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsPolicyPolicy.setStatus("current")


class _AlaIpmsPolicyDisposition_Type(Integer32):
    """Custom type alaIpmsPolicyDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 0))
    )


_AlaIpmsPolicyDisposition_Type.__name__ = "Integer32"
_AlaIpmsPolicyDisposition_Object = MibTableColumn
alaIpmsPolicyDisposition = _AlaIpmsPolicyDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 10),
    _AlaIpmsPolicyDisposition_Type()
)
alaIpmsPolicyDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsPolicyDisposition.setStatus("current")
_AlaIpmsPolicyTimeout_Type = Unsigned32
_AlaIpmsPolicyTimeout_Object = MibTableColumn
alaIpmsPolicyTimeout = _AlaIpmsPolicyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 9, 1, 1, 11),
    _AlaIpmsPolicyTimeout_Type()
)
alaIpmsPolicyTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpmsPolicyTimeout.setStatus("current")
_AlaIpmsStaticMember_ObjectIdentity = ObjectIdentity
alaIpmsStaticMember = _AlaIpmsStaticMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 10)
)
_AlaIpmsStaticMemberTable_Object = MibTable
alaIpmsStaticMemberTable = _AlaIpmsStaticMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    alaIpmsStaticMemberTable.setStatus("current")
_AlaIpmsStaticMemberEntry_Object = MibTableRow
alaIpmsStaticMemberEntry = _AlaIpmsStaticMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 10, 1, 1)
)
alaIpmsStaticMemberEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticMemberGroupAddr"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticMemberVlan"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticMemberIfIndex"),
    (0, "ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticMemberVci"),
)
if mibBuilder.loadTexts:
    alaIpmsStaticMemberEntry.setStatus("current")
_AlaIpmsStaticMemberGroupAddr_Type = IpAddress
_AlaIpmsStaticMemberGroupAddr_Object = MibTableColumn
alaIpmsStaticMemberGroupAddr = _AlaIpmsStaticMemberGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 10, 1, 1, 1),
    _AlaIpmsStaticMemberGroupAddr_Type()
)
alaIpmsStaticMemberGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticMemberGroupAddr.setStatus("current")


class _AlaIpmsStaticMemberIGMPVersion_Type(Integer32):
    """Custom type alaIpmsStaticMemberIGMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv2", 2),
          ("igmpv3", 3))
    )


_AlaIpmsStaticMemberIGMPVersion_Type.__name__ = "Integer32"
_AlaIpmsStaticMemberIGMPVersion_Object = MibTableColumn
alaIpmsStaticMemberIGMPVersion = _AlaIpmsStaticMemberIGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 10, 1, 1, 2),
    _AlaIpmsStaticMemberIGMPVersion_Type()
)
alaIpmsStaticMemberIGMPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticMemberIGMPVersion.setStatus("current")


class _AlaIpmsStaticMemberVlan_Type(Integer32):
    """Custom type alaIpmsStaticMemberVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaIpmsStaticMemberVlan_Type.__name__ = "Integer32"
_AlaIpmsStaticMemberVlan_Object = MibTableColumn
alaIpmsStaticMemberVlan = _AlaIpmsStaticMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 10, 1, 1, 3),
    _AlaIpmsStaticMemberVlan_Type()
)
alaIpmsStaticMemberVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticMemberVlan.setStatus("current")
_AlaIpmsStaticMemberIfIndex_Type = InterfaceIndex
_AlaIpmsStaticMemberIfIndex_Object = MibTableColumn
alaIpmsStaticMemberIfIndex = _AlaIpmsStaticMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 10, 1, 1, 4),
    _AlaIpmsStaticMemberIfIndex_Type()
)
alaIpmsStaticMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticMemberIfIndex.setStatus("current")
_AlaIpmsStaticMemberVci_Type = Unsigned32
_AlaIpmsStaticMemberVci_Object = MibTableColumn
alaIpmsStaticMemberVci = _AlaIpmsStaticMemberVci_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 10, 1, 1, 5),
    _AlaIpmsStaticMemberVci_Type()
)
alaIpmsStaticMemberVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpmsStaticMemberVci.setStatus("current")
_AlaIpmsStaticMemberRowStatus_Type = RowStatus
_AlaIpmsStaticMemberRowStatus_Object = MibTableColumn
alaIpmsStaticMemberRowStatus = _AlaIpmsStaticMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 1, 10, 1, 1, 6),
    _AlaIpmsStaticMemberRowStatus_Type()
)
alaIpmsStaticMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpmsStaticMemberRowStatus.setStatus("current")
_AlcatelIND1IPMSMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPMSMIBConformance = _AlcatelIND1IPMSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2)
)
_AlcatelIND1IPMSMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPMSMIBCompliances = _AlcatelIND1IPMSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 1)
)
_AlcatelIND1IPMSMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPMSMIBGroups = _AlcatelIND1IPMSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2)
)

# Managed Objects groups

alaIpmsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2, 1)
)
alaIpmsConfigGroup.setObjects(
      *(("ALCATEL-IND1-IPMS-MIB", "alaIpmsStatus"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsLeaveTimeout"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsQueryInterval"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsNeighborTimer"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsQuerierTimer"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsMembershipTimer"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsOtherQuerierTimer"))
)
if mibBuilder.loadTexts:
    alaIpmsConfigGroup.setStatus("current")

alaIpmsGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2, 2)
)
alaIpmsGroupGroup.setObjects(
      *(("ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupClientMacAddr"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupTimeout"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupIGMPv3GroupType"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsGroupIGMPv3SrcTimeout"))
)
if mibBuilder.loadTexts:
    alaIpmsGroupGroup.setStatus("current")

alaIpmsNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2, 3)
)
alaIpmsNeighborGroup.setObjects(
      *(("ALCATEL-IND1-IPMS-MIB", "alaIpmsNeighborVlan"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsNeighborIfIndex"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsNeighborVci"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsNeighborType"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsNeighborTimeout"))
)
if mibBuilder.loadTexts:
    alaIpmsNeighborGroup.setStatus("current")

alaIpmsStaticNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2, 4)
)
alaIpmsStaticNeighborGroup.setObjects(
    ("ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticNeighborRowStatus")
)
if mibBuilder.loadTexts:
    alaIpmsStaticNeighborGroup.setStatus("current")

alaIpmsQuerierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2, 5)
)
alaIpmsQuerierGroup.setObjects(
      *(("ALCATEL-IND1-IPMS-MIB", "alaIpmsQuerierVlan"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsQuerierIfIndex"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsQuerierVci"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsQuerierType"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsQuerierTimeout"))
)
if mibBuilder.loadTexts:
    alaIpmsQuerierGroup.setStatus("current")

alaIpmsStaticQuerierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2, 6)
)
alaIpmsStaticQuerierGroup.setObjects(
    ("ALCATEL-IND1-IPMS-MIB", "alaIpmsStaticQuerierRowStatus")
)
if mibBuilder.loadTexts:
    alaIpmsStaticQuerierGroup.setStatus("current")

alaIpmsSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2, 7)
)
alaIpmsSourceGroup.setObjects(
      *(("ALCATEL-IND1-IPMS-MIB", "alaIpmsSourceSrcMacAddr"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsSourceTimeout"))
)
if mibBuilder.loadTexts:
    alaIpmsSourceGroup.setStatus("current")

alaIpmsForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2, 8)
)
alaIpmsForwardGroup.setObjects(
      *(("ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardSrcTunIpAddr"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardRtrMacAddr"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsForwardRtrTtl"))
)
if mibBuilder.loadTexts:
    alaIpmsForwardGroup.setStatus("current")

alaIpmsPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 2, 9)
)
alaIpmsPolicyGroup.setObjects(
      *(("ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicySrcMacAddr"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicyDisposition"),
        ("ALCATEL-IND1-IPMS-MIB", "alaIpmsPolicyTimeout"))
)
if mibBuilder.loadTexts:
    alaIpmsPolicyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIpmsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 18, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaIpmsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPMS-MIB",
    **{"alcatelIND1IPMSMIB": alcatelIND1IPMSMIB,
       "alcatelIND1IPMSMIBObjects": alcatelIND1IPMSMIBObjects,
       "alaIpmsConfig": alaIpmsConfig,
       "alaIpmsStatus": alaIpmsStatus,
       "alaIpmsLeaveTimeout": alaIpmsLeaveTimeout,
       "alaIpmsQueryInterval": alaIpmsQueryInterval,
       "alaIpmsNeighborTimer": alaIpmsNeighborTimer,
       "alaIpmsQuerierTimer": alaIpmsQuerierTimer,
       "alaIpmsMembershipTimer": alaIpmsMembershipTimer,
       "alaIpmsPriority": alaIpmsPriority,
       "alaIpmsMaxBandwidth": alaIpmsMaxBandwidth,
       "alaIpmsHardwareRoute": alaIpmsHardwareRoute,
       "alaIpmsIGMPMembershipProxyVersion": alaIpmsIGMPMembershipProxyVersion,
       "alaIpmsOtherQuerierTimer": alaIpmsOtherQuerierTimer,
       "alaIpmsGroup": alaIpmsGroup,
       "alaIpmsGroupTable": alaIpmsGroupTable,
       "alaIpmsGroupEntry": alaIpmsGroupEntry,
       "alaIpmsGroupDestIpAddr": alaIpmsGroupDestIpAddr,
       "alaIpmsGroupClientIpAddr": alaIpmsGroupClientIpAddr,
       "alaIpmsGroupClientMacAddr": alaIpmsGroupClientMacAddr,
       "alaIpmsGroupClientVlan": alaIpmsGroupClientVlan,
       "alaIpmsGroupClientIfIndex": alaIpmsGroupClientIfIndex,
       "alaIpmsGroupClientVci": alaIpmsGroupClientVci,
       "alaIpmsGroupIGMPVersion": alaIpmsGroupIGMPVersion,
       "alaIpmsGroupIGMPv3SrcIP": alaIpmsGroupIGMPv3SrcIP,
       "alaIpmsGroupIGMPv3SrcType": alaIpmsGroupIGMPv3SrcType,
       "alaIpmsGroupIGMPv3SrcTimeout": alaIpmsGroupIGMPv3SrcTimeout,
       "alaIpmsGroupIGMPv3GroupType": alaIpmsGroupIGMPv3GroupType,
       "alaIpmsGroupTimeout": alaIpmsGroupTimeout,
       "alaIpmsNeighbor": alaIpmsNeighbor,
       "alaIpmsNeighborTable": alaIpmsNeighborTable,
       "alaIpmsNeighborEntry": alaIpmsNeighborEntry,
       "alaIpmsNeighborIpAddr": alaIpmsNeighborIpAddr,
       "alaIpmsNeighborVlan": alaIpmsNeighborVlan,
       "alaIpmsNeighborIfIndex": alaIpmsNeighborIfIndex,
       "alaIpmsNeighborVci": alaIpmsNeighborVci,
       "alaIpmsNeighborType": alaIpmsNeighborType,
       "alaIpmsNeighborTimeout": alaIpmsNeighborTimeout,
       "alaIpmsStaticNeighbor": alaIpmsStaticNeighbor,
       "alaIpmsStaticNeighborTable": alaIpmsStaticNeighborTable,
       "alaIpmsStaticNeighborEntry": alaIpmsStaticNeighborEntry,
       "alaIpmsStaticNeighborVlan": alaIpmsStaticNeighborVlan,
       "alaIpmsStaticNeighborIfIndex": alaIpmsStaticNeighborIfIndex,
       "alaIpmsStaticNeighborVci": alaIpmsStaticNeighborVci,
       "alaIpmsStaticNeighborIGMPVersion": alaIpmsStaticNeighborIGMPVersion,
       "alaIpmsStaticNeighborRowStatus": alaIpmsStaticNeighborRowStatus,
       "alaIpmsQuerier": alaIpmsQuerier,
       "alaIpmsQuerierTable": alaIpmsQuerierTable,
       "alaIpmsQuerierEntry": alaIpmsQuerierEntry,
       "alaIpmsQuerierIpAddr": alaIpmsQuerierIpAddr,
       "alaIpmsQuerierVlan": alaIpmsQuerierVlan,
       "alaIpmsQuerierIfIndex": alaIpmsQuerierIfIndex,
       "alaIpmsQuerierVci": alaIpmsQuerierVci,
       "alaIpmsQuerierType": alaIpmsQuerierType,
       "alaIpmsQuerierTimeout": alaIpmsQuerierTimeout,
       "alaIpmsStaticQuerier": alaIpmsStaticQuerier,
       "alaIpmsStaticQuerierTable": alaIpmsStaticQuerierTable,
       "alaIpmsStaticQuerierEntry": alaIpmsStaticQuerierEntry,
       "alaIpmsStaticQuerierVlan": alaIpmsStaticQuerierVlan,
       "alaIpmsStaticQuerierIfIndex": alaIpmsStaticQuerierIfIndex,
       "alaIpmsStaticQuerierVci": alaIpmsStaticQuerierVci,
       "alaIpmsStaticQuerierIGMPVersion": alaIpmsStaticQuerierIGMPVersion,
       "alaIpmsStaticQuerierRowStatus": alaIpmsStaticQuerierRowStatus,
       "alaIpmsSource": alaIpmsSource,
       "alaIpmsSourceTable": alaIpmsSourceTable,
       "alaIpmsSourceEntry": alaIpmsSourceEntry,
       "alaIpmsSourceDestIpAddr": alaIpmsSourceDestIpAddr,
       "alaIpmsSourceSrcIpAddr": alaIpmsSourceSrcIpAddr,
       "alaIpmsSourceSrcMacAddr": alaIpmsSourceSrcMacAddr,
       "alaIpmsSourceSrcVlan": alaIpmsSourceSrcVlan,
       "alaIpmsSourceSrcIfIndex": alaIpmsSourceSrcIfIndex,
       "alaIpmsSourceUniIpAddr": alaIpmsSourceUniIpAddr,
       "alaIpmsSourceSrcVci": alaIpmsSourceSrcVci,
       "alaIpmsSourceSrcType": alaIpmsSourceSrcType,
       "alaIpmsSourceTimeout": alaIpmsSourceTimeout,
       "alaIpmsForward": alaIpmsForward,
       "alaIpmsForwardTable": alaIpmsForwardTable,
       "alaIpmsForwardEntry": alaIpmsForwardEntry,
       "alaIpmsForwardDestIpAddr": alaIpmsForwardDestIpAddr,
       "alaIpmsForwardSrcIpAddr": alaIpmsForwardSrcIpAddr,
       "alaIpmsForwardDestVlan": alaIpmsForwardDestVlan,
       "alaIpmsForwardSrcVlan": alaIpmsForwardSrcVlan,
       "alaIpmsForwardSrcIfIndex": alaIpmsForwardSrcIfIndex,
       "alaIpmsForwardUniIpAddr": alaIpmsForwardUniIpAddr,
       "alaIpmsForwardSrcVci": alaIpmsForwardSrcVci,
       "alaIpmsForwardDestType": alaIpmsForwardDestType,
       "alaIpmsForwardSrcType": alaIpmsForwardSrcType,
       "alaIpmsForwardDestTunIpAddr": alaIpmsForwardDestTunIpAddr,
       "alaIpmsForwardSrcTunIpAddr": alaIpmsForwardSrcTunIpAddr,
       "alaIpmsForwardRtrMacAddr": alaIpmsForwardRtrMacAddr,
       "alaIpmsForwardRtrTtl": alaIpmsForwardRtrTtl,
       "alaIpmsForwardDestIfIndex": alaIpmsForwardDestIfIndex,
       "alaIpmsPolicy": alaIpmsPolicy,
       "alaIpmsPolicyTable": alaIpmsPolicyTable,
       "alaIpmsPolicyEntry": alaIpmsPolicyEntry,
       "alaIpmsPolicyDestIpAddr": alaIpmsPolicyDestIpAddr,
       "alaIpmsPolicySrcIpAddr": alaIpmsPolicySrcIpAddr,
       "alaIpmsPolicySrcMacAddr": alaIpmsPolicySrcMacAddr,
       "alaIpmsPolicySrcVlan": alaIpmsPolicySrcVlan,
       "alaIpmsPolicySrcIfIndex": alaIpmsPolicySrcIfIndex,
       "alaIpmsPolicyUniIpAddr": alaIpmsPolicyUniIpAddr,
       "alaIpmsPolicySrcVci": alaIpmsPolicySrcVci,
       "alaIpmsPolicySrcType": alaIpmsPolicySrcType,
       "alaIpmsPolicyPolicy": alaIpmsPolicyPolicy,
       "alaIpmsPolicyDisposition": alaIpmsPolicyDisposition,
       "alaIpmsPolicyTimeout": alaIpmsPolicyTimeout,
       "alaIpmsStaticMember": alaIpmsStaticMember,
       "alaIpmsStaticMemberTable": alaIpmsStaticMemberTable,
       "alaIpmsStaticMemberEntry": alaIpmsStaticMemberEntry,
       "alaIpmsStaticMemberGroupAddr": alaIpmsStaticMemberGroupAddr,
       "alaIpmsStaticMemberIGMPVersion": alaIpmsStaticMemberIGMPVersion,
       "alaIpmsStaticMemberVlan": alaIpmsStaticMemberVlan,
       "alaIpmsStaticMemberIfIndex": alaIpmsStaticMemberIfIndex,
       "alaIpmsStaticMemberVci": alaIpmsStaticMemberVci,
       "alaIpmsStaticMemberRowStatus": alaIpmsStaticMemberRowStatus,
       "alcatelIND1IPMSMIBConformance": alcatelIND1IPMSMIBConformance,
       "alcatelIND1IPMSMIBCompliances": alcatelIND1IPMSMIBCompliances,
       "alaIpmsCompliance": alaIpmsCompliance,
       "alcatelIND1IPMSMIBGroups": alcatelIND1IPMSMIBGroups,
       "alaIpmsConfigGroup": alaIpmsConfigGroup,
       "alaIpmsGroupGroup": alaIpmsGroupGroup,
       "alaIpmsNeighborGroup": alaIpmsNeighborGroup,
       "alaIpmsStaticNeighborGroup": alaIpmsStaticNeighborGroup,
       "alaIpmsQuerierGroup": alaIpmsQuerierGroup,
       "alaIpmsStaticQuerierGroup": alaIpmsStaticQuerierGroup,
       "alaIpmsSourceGroup": alaIpmsSourceGroup,
       "alaIpmsForwardGroup": alaIpmsForwardGroup,
       "alaIpmsPolicyGroup": alaIpmsPolicyGroup}
)
