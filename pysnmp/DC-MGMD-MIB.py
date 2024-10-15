# SNMP MIB module (DC-MGMD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DC-MGMD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:39 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dcMgmdMib = ModuleIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1)
)
dcMgmdMib.setRevisions(
        ("2014-11-19 00:00",
         "2011-03-09 00:00",
         "2005-08-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NonZeroUnsigned8(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class NonZeroInteger(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class AdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )



class OperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )



class PmIndex(Unsigned32, TextualConvention):
    status = "current"


class MjStatus(Integer32, TextualConvention):
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("mjFailed", 10),
          ("mjFailedToRegister", 8),
          ("mjFailingOver", 9),
          ("mjJoinActive", 4),
          ("mjJoinGone", 7),
          ("mjNotJoined", 1),
          ("mjSentAddJoin", 2),
          ("mjSentDelJoin", 5),
          ("mjSentRegister", 3),
          ("mjSentUnregister", 6))
    )



class InterfaceType(Integer32, TextualConvention):
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
        *(("ifIfInfo", 2),
          ("ifIpSockets", 1),
          ("ifRteProtInput", 3))
    )



class MgmdEntityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2))
    )



# MIB Managed Objects in the order of their OIDs

_MgmdPmEntTable_Object = MibTable
mgmdPmEntTable = _MgmdPmEntTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1)
)
if mibBuilder.loadTexts:
    mgmdPmEntTable.setStatus("current")
_MgmdPmEntEntry_Object = MibTableRow
mgmdPmEntEntry = _MgmdPmEntEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1)
)
mgmdPmEntEntry.setIndexNames(
    (0, "DC-MGMD-MIB", "mgmdPmEntIndex"),
)
if mibBuilder.loadTexts:
    mgmdPmEntEntry.setStatus("current")
_MgmdPmEntIndex_Type = PmIndex
_MgmdPmEntIndex_Object = MibTableColumn
mgmdPmEntIndex = _MgmdPmEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1, 1),
    _MgmdPmEntIndex_Type()
)
mgmdPmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmEntIndex.setStatus("current")


class _MgmdPmEntAdminStatus_Type(AdminStatus):
    """Custom type mgmdPmEntAdminStatus based on AdminStatus"""


_MgmdPmEntAdminStatus_Object = MibTableColumn
mgmdPmEntAdminStatus = _MgmdPmEntAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1, 2),
    _MgmdPmEntAdminStatus_Type()
)
mgmdPmEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmEntAdminStatus.setStatus("current")
_MgmdPmEntOperStatus_Type = OperStatus
_MgmdPmEntOperStatus_Object = MibTableColumn
mgmdPmEntOperStatus = _MgmdPmEntOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1, 3),
    _MgmdPmEntOperStatus_Type()
)
mgmdPmEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmEntOperStatus.setStatus("current")
_MgmdPmEntRowStatus_Type = RowStatus
_MgmdPmEntRowStatus_Object = MibTableColumn
mgmdPmEntRowStatus = _MgmdPmEntRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 1, 1, 4),
    _MgmdPmEntRowStatus_Type()
)
mgmdPmEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmEntRowStatus.setStatus("current")
_MgmdPmMjTable_Object = MibTable
mgmdPmMjTable = _MgmdPmMjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2)
)
if mibBuilder.loadTexts:
    mgmdPmMjTable.setStatus("current")
_MgmdPmMjEntry_Object = MibTableRow
mgmdPmMjEntry = _MgmdPmMjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1)
)
mgmdPmMjEntry.setIndexNames(
    (0, "DC-MGMD-MIB", "mgmdPmMjEntIndex"),
    (0, "DC-MGMD-MIB", "mgmdPmMjInterfaceId"),
    (0, "DC-MGMD-MIB", "mgmdPmMjPartnerIndex"),
)
if mibBuilder.loadTexts:
    mgmdPmMjEntry.setStatus("current")
_MgmdPmMjEntIndex_Type = PmIndex
_MgmdPmMjEntIndex_Object = MibTableColumn
mgmdPmMjEntIndex = _MgmdPmMjEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 1),
    _MgmdPmMjEntIndex_Type()
)
mgmdPmMjEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmMjEntIndex.setStatus("current")
_MgmdPmMjInterfaceId_Type = InterfaceType
_MgmdPmMjInterfaceId_Object = MibTableColumn
mgmdPmMjInterfaceId = _MgmdPmMjInterfaceId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 2),
    _MgmdPmMjInterfaceId_Type()
)
mgmdPmMjInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmMjInterfaceId.setStatus("current")
_MgmdPmMjPartnerIndex_Type = Unsigned32
_MgmdPmMjPartnerIndex_Object = MibTableColumn
mgmdPmMjPartnerIndex = _MgmdPmMjPartnerIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 3),
    _MgmdPmMjPartnerIndex_Type()
)
mgmdPmMjPartnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmMjPartnerIndex.setStatus("current")
_MgmdPmMjRowStatus_Type = RowStatus
_MgmdPmMjRowStatus_Object = MibTableColumn
mgmdPmMjRowStatus = _MgmdPmMjRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 4),
    _MgmdPmMjRowStatus_Type()
)
mgmdPmMjRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmMjRowStatus.setStatus("current")


class _MgmdPmMjAdminStatus_Type(AdminStatus):
    """Custom type mgmdPmMjAdminStatus based on AdminStatus"""


_MgmdPmMjAdminStatus_Object = MibTableColumn
mgmdPmMjAdminStatus = _MgmdPmMjAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 5),
    _MgmdPmMjAdminStatus_Type()
)
mgmdPmMjAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmMjAdminStatus.setStatus("current")
_MgmdPmMjOperStatus_Type = OperStatus
_MgmdPmMjOperStatus_Object = MibTableColumn
mgmdPmMjOperStatus = _MgmdPmMjOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 6),
    _MgmdPmMjOperStatus_Type()
)
mgmdPmMjOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmMjOperStatus.setStatus("current")
_MgmdPmMjJoinStatus_Type = MjStatus
_MgmdPmMjJoinStatus_Object = MibTableColumn
mgmdPmMjJoinStatus = _MgmdPmMjJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 2, 1, 7),
    _MgmdPmMjJoinStatus_Type()
)
mgmdPmMjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmMjJoinStatus.setStatus("current")
_MgmdPmStaticGroupTable_Object = MibTable
mgmdPmStaticGroupTable = _MgmdPmStaticGroupTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3)
)
if mibBuilder.loadTexts:
    mgmdPmStaticGroupTable.setStatus("current")
_MgmdPmStaticGroupEntry_Object = MibTableRow
mgmdPmStaticGroupEntry = _MgmdPmStaticGroupEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1)
)
mgmdPmStaticGroupEntry.setIndexNames(
    (0, "DC-MGMD-MIB", "mgmdPmStaticGroupEntityType"),
    (0, "DC-MGMD-MIB", "mgmdPmStaticGroupIfIndex"),
    (0, "DC-MGMD-MIB", "mgmdPmStaticGroupAddressType"),
    (0, "DC-MGMD-MIB", "mgmdPmStaticGroupAddress"),
    (0, "DC-MGMD-MIB", "mgmdPmStaticGroupSourceAddress"),
)
if mibBuilder.loadTexts:
    mgmdPmStaticGroupEntry.setStatus("current")
_MgmdPmStaticGroupEntityType_Type = MgmdEntityType
_MgmdPmStaticGroupEntityType_Object = MibTableColumn
mgmdPmStaticGroupEntityType = _MgmdPmStaticGroupEntityType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 1),
    _MgmdPmStaticGroupEntityType_Type()
)
mgmdPmStaticGroupEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmStaticGroupEntityType.setStatus("current")
_MgmdPmStaticGroupIfIndex_Type = InterfaceIndex
_MgmdPmStaticGroupIfIndex_Object = MibTableColumn
mgmdPmStaticGroupIfIndex = _MgmdPmStaticGroupIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 2),
    _MgmdPmStaticGroupIfIndex_Type()
)
mgmdPmStaticGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmStaticGroupIfIndex.setStatus("current")
_MgmdPmStaticGroupAddressType_Type = InetAddressType
_MgmdPmStaticGroupAddressType_Object = MibTableColumn
mgmdPmStaticGroupAddressType = _MgmdPmStaticGroupAddressType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 3),
    _MgmdPmStaticGroupAddressType_Type()
)
mgmdPmStaticGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmStaticGroupAddressType.setStatus("current")
_MgmdPmStaticGroupAddress_Type = InetAddress
_MgmdPmStaticGroupAddress_Object = MibTableColumn
mgmdPmStaticGroupAddress = _MgmdPmStaticGroupAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 4),
    _MgmdPmStaticGroupAddress_Type()
)
mgmdPmStaticGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmStaticGroupAddress.setStatus("current")
_MgmdPmStaticGroupSourceAddress_Type = InetAddress
_MgmdPmStaticGroupSourceAddress_Object = MibTableColumn
mgmdPmStaticGroupSourceAddress = _MgmdPmStaticGroupSourceAddress_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 5),
    _MgmdPmStaticGroupSourceAddress_Type()
)
mgmdPmStaticGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmStaticGroupSourceAddress.setStatus("current")
_MgmdPmStaticGroupStatus_Type = RowStatus
_MgmdPmStaticGroupStatus_Object = MibTableColumn
mgmdPmStaticGroupStatus = _MgmdPmStaticGroupStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 6),
    _MgmdPmStaticGroupStatus_Type()
)
mgmdPmStaticGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmStaticGroupStatus.setStatus("current")


class _MgmdPmStaticGroupStorageType_Type(StorageType):
    """Custom type mgmdPmStaticGroupStorageType based on StorageType"""


_MgmdPmStaticGroupStorageType_Object = MibTableColumn
mgmdPmStaticGroupStorageType = _MgmdPmStaticGroupStorageType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 3, 1, 7),
    _MgmdPmStaticGroupStorageType_Type()
)
mgmdPmStaticGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmStaticGroupStorageType.setStatus("current")
_MgmdPmRouterInterfaceTable_Object = MibTable
mgmdPmRouterInterfaceTable = _MgmdPmRouterInterfaceTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4)
)
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceTable.setStatus("current")
_MgmdPmRouterInterfaceEntry_Object = MibTableRow
mgmdPmRouterInterfaceEntry = _MgmdPmRouterInterfaceEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1)
)
mgmdPmRouterInterfaceEntry.setIndexNames(
    (0, "DC-MGMD-MIB", "mgmdPmRouterInterfaceIfIndex"),
    (0, "DC-MGMD-MIB", "mgmdPmRouterInterfaceQuerierType"),
)
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceEntry.setStatus("current")
_MgmdPmRouterInterfaceIfIndex_Type = InterfaceIndex
_MgmdPmRouterInterfaceIfIndex_Object = MibTableColumn
mgmdPmRouterInterfaceIfIndex = _MgmdPmRouterInterfaceIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 1),
    _MgmdPmRouterInterfaceIfIndex_Type()
)
mgmdPmRouterInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceIfIndex.setStatus("current")
_MgmdPmRouterInterfaceQuerierType_Type = InetAddressType
_MgmdPmRouterInterfaceQuerierType_Object = MibTableColumn
mgmdPmRouterInterfaceQuerierType = _MgmdPmRouterInterfaceQuerierType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 2),
    _MgmdPmRouterInterfaceQuerierType_Type()
)
mgmdPmRouterInterfaceQuerierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceQuerierType.setStatus("current")
_MgmdPmRouterInterfaceQuerier_Type = InetAddress
_MgmdPmRouterInterfaceQuerier_Object = MibTableColumn
mgmdPmRouterInterfaceQuerier = _MgmdPmRouterInterfaceQuerier_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 3),
    _MgmdPmRouterInterfaceQuerier_Type()
)
mgmdPmRouterInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceQuerier.setStatus("current")


class _MgmdPmRouterInterfaceQueryInterval_Type(Unsigned32):
    """Custom type mgmdPmRouterInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31744),
    )


_MgmdPmRouterInterfaceQueryInterval_Type.__name__ = "Unsigned32"
_MgmdPmRouterInterfaceQueryInterval_Object = MibTableColumn
mgmdPmRouterInterfaceQueryInterval = _MgmdPmRouterInterfaceQueryInterval_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 4),
    _MgmdPmRouterInterfaceQueryInterval_Type()
)
mgmdPmRouterInterfaceQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceQueryInterval.setUnits("seconds")
_MgmdPmRouterInterfaceStatus_Type = RowStatus
_MgmdPmRouterInterfaceStatus_Object = MibTableColumn
mgmdPmRouterInterfaceStatus = _MgmdPmRouterInterfaceStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 5),
    _MgmdPmRouterInterfaceStatus_Type()
)
mgmdPmRouterInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceStatus.setStatus("current")


class _MgmdPmRouterInterfaceVersion_Type(Unsigned32):
    """Custom type mgmdPmRouterInterfaceVersion based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MgmdPmRouterInterfaceVersion_Type.__name__ = "Unsigned32"
_MgmdPmRouterInterfaceVersion_Object = MibTableColumn
mgmdPmRouterInterfaceVersion = _MgmdPmRouterInterfaceVersion_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 6),
    _MgmdPmRouterInterfaceVersion_Type()
)
mgmdPmRouterInterfaceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceVersion.setStatus("current")


class _MgmdPmRouterInterfaceQueryMaxResponseTime_Type(Unsigned32):
    """Custom type mgmdPmRouterInterfaceQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_MgmdPmRouterInterfaceQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_MgmdPmRouterInterfaceQueryMaxResponseTime_Object = MibTableColumn
mgmdPmRouterInterfaceQueryMaxResponseTime = _MgmdPmRouterInterfaceQueryMaxResponseTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 7),
    _MgmdPmRouterInterfaceQueryMaxResponseTime_Type()
)
mgmdPmRouterInterfaceQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceQueryMaxResponseTime.setUnits("tenths of seconds")
_MgmdPmRouterInterfaceQuerierUpTime_Type = TimeTicks
_MgmdPmRouterInterfaceQuerierUpTime_Object = MibTableColumn
mgmdPmRouterInterfaceQuerierUpTime = _MgmdPmRouterInterfaceQuerierUpTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 8),
    _MgmdPmRouterInterfaceQuerierUpTime_Type()
)
mgmdPmRouterInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceQuerierUpTime.setStatus("current")
_MgmdPmRouterInterfaceQuerierExpiryTime_Type = TimeTicks
_MgmdPmRouterInterfaceQuerierExpiryTime_Object = MibTableColumn
mgmdPmRouterInterfaceQuerierExpiryTime = _MgmdPmRouterInterfaceQuerierExpiryTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 9),
    _MgmdPmRouterInterfaceQuerierExpiryTime_Type()
)
mgmdPmRouterInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceQuerierExpiryTime.setStatus("current")
_MgmdPmRouterInterfaceWrongVersionQueries_Type = Counter32
_MgmdPmRouterInterfaceWrongVersionQueries_Object = MibTableColumn
mgmdPmRouterInterfaceWrongVersionQueries = _MgmdPmRouterInterfaceWrongVersionQueries_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 10),
    _MgmdPmRouterInterfaceWrongVersionQueries_Type()
)
mgmdPmRouterInterfaceWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceWrongVersionQueries.setStatus("current")
_MgmdPmRouterInterfaceJoins_Type = Counter32
_MgmdPmRouterInterfaceJoins_Object = MibTableColumn
mgmdPmRouterInterfaceJoins = _MgmdPmRouterInterfaceJoins_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 11),
    _MgmdPmRouterInterfaceJoins_Type()
)
mgmdPmRouterInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceJoins.setStatus("current")


class _MgmdPmRouterInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mgmdPmRouterInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MgmdPmRouterInterfaceProxyIfIndex_Object = MibTableColumn
mgmdPmRouterInterfaceProxyIfIndex = _MgmdPmRouterInterfaceProxyIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 12),
    _MgmdPmRouterInterfaceProxyIfIndex_Type()
)
mgmdPmRouterInterfaceProxyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceProxyIfIndex.setStatus("current")
_MgmdPmRouterInterfaceGroups_Type = Gauge32
_MgmdPmRouterInterfaceGroups_Object = MibTableColumn
mgmdPmRouterInterfaceGroups = _MgmdPmRouterInterfaceGroups_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 13),
    _MgmdPmRouterInterfaceGroups_Type()
)
mgmdPmRouterInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceGroups.setStatus("current")


class _MgmdPmRouterInterfaceRobustness_Type(Unsigned32):
    """Custom type mgmdPmRouterInterfaceRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MgmdPmRouterInterfaceRobustness_Type.__name__ = "Unsigned32"
_MgmdPmRouterInterfaceRobustness_Object = MibTableColumn
mgmdPmRouterInterfaceRobustness = _MgmdPmRouterInterfaceRobustness_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 14),
    _MgmdPmRouterInterfaceRobustness_Type()
)
mgmdPmRouterInterfaceRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceRobustness.setStatus("current")


class _MgmdPmRouterInterfaceLastMembQueryIntvl_Type(Unsigned32):
    """Custom type mgmdPmRouterInterfaceLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_MgmdPmRouterInterfaceLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_MgmdPmRouterInterfaceLastMembQueryIntvl_Object = MibTableColumn
mgmdPmRouterInterfaceLastMembQueryIntvl = _MgmdPmRouterInterfaceLastMembQueryIntvl_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 15),
    _MgmdPmRouterInterfaceLastMembQueryIntvl_Type()
)
mgmdPmRouterInterfaceLastMembQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceLastMembQueryIntvl.setUnits("tenths of seconds")


class _MgmdPmRouterInterfaceLastMembQueryCount_Type(Unsigned32):
    """Custom type mgmdPmRouterInterfaceLastMembQueryCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MgmdPmRouterInterfaceLastMembQueryCount_Type.__name__ = "Unsigned32"
_MgmdPmRouterInterfaceLastMembQueryCount_Object = MibTableColumn
mgmdPmRouterInterfaceLastMembQueryCount = _MgmdPmRouterInterfaceLastMembQueryCount_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 16),
    _MgmdPmRouterInterfaceLastMembQueryCount_Type()
)
mgmdPmRouterInterfaceLastMembQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceLastMembQueryCount.setStatus("current")


class _MgmdPmRouterInterfaceStartupQueryCount_Type(Unsigned32):
    """Custom type mgmdPmRouterInterfaceStartupQueryCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MgmdPmRouterInterfaceStartupQueryCount_Type.__name__ = "Unsigned32"
_MgmdPmRouterInterfaceStartupQueryCount_Object = MibTableColumn
mgmdPmRouterInterfaceStartupQueryCount = _MgmdPmRouterInterfaceStartupQueryCount_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 17),
    _MgmdPmRouterInterfaceStartupQueryCount_Type()
)
mgmdPmRouterInterfaceStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceStartupQueryCount.setStatus("current")


class _MgmdPmRouterInterfaceStartupQueryInterval_Type(Unsigned32):
    """Custom type mgmdPmRouterInterfaceStartupQueryInterval based on Unsigned32"""
    defaultValue = 31

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31744),
    )


_MgmdPmRouterInterfaceStartupQueryInterval_Type.__name__ = "Unsigned32"
_MgmdPmRouterInterfaceStartupQueryInterval_Object = MibTableColumn
mgmdPmRouterInterfaceStartupQueryInterval = _MgmdPmRouterInterfaceStartupQueryInterval_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 18),
    _MgmdPmRouterInterfaceStartupQueryInterval_Type()
)
mgmdPmRouterInterfaceStartupQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceStartupQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceStartupQueryInterval.setUnits("seconds")


class _MgmdPmRouterInterfaceStaticMulticastMode_Type(TruthValue):
    """Custom type mgmdPmRouterInterfaceStaticMulticastMode based on TruthValue"""


_MgmdPmRouterInterfaceStaticMulticastMode_Object = MibTableColumn
mgmdPmRouterInterfaceStaticMulticastMode = _MgmdPmRouterInterfaceStaticMulticastMode_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 19),
    _MgmdPmRouterInterfaceStaticMulticastMode_Type()
)
mgmdPmRouterInterfaceStaticMulticastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceStaticMulticastMode.setStatus("current")


class _MgmdPmRouterInterfaceBackupProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mgmdPmRouterInterfaceBackupProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MgmdPmRouterInterfaceBackupProxyIfIndex_Object = MibTableColumn
mgmdPmRouterInterfaceBackupProxyIfIndex = _MgmdPmRouterInterfaceBackupProxyIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 20),
    _MgmdPmRouterInterfaceBackupProxyIfIndex_Type()
)
mgmdPmRouterInterfaceBackupProxyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceBackupProxyIfIndex.setStatus("current")


class _MgmdPmRouterInterfaceActiveProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mgmdPmRouterInterfaceActiveProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MgmdPmRouterInterfaceActiveProxyIfIndex_Object = MibTableColumn
mgmdPmRouterInterfaceActiveProxyIfIndex = _MgmdPmRouterInterfaceActiveProxyIfIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 21),
    _MgmdPmRouterInterfaceActiveProxyIfIndex_Type()
)
mgmdPmRouterInterfaceActiveProxyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceActiveProxyIfIndex.setStatus("current")


class _MgmdPmRouterInterfaceAccessList_Type(Unsigned32):
    """Custom type mgmdPmRouterInterfaceAccessList based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_MgmdPmRouterInterfaceAccessList_Type.__name__ = "Unsigned32"
_MgmdPmRouterInterfaceAccessList_Object = MibTableColumn
mgmdPmRouterInterfaceAccessList = _MgmdPmRouterInterfaceAccessList_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 22),
    _MgmdPmRouterInterfaceAccessList_Type()
)
mgmdPmRouterInterfaceAccessList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceAccessList.setStatus("current")
_MgmdPmRouterInterfaceIgmpResetCounts_Type = Unsigned32
_MgmdPmRouterInterfaceIgmpResetCounts_Object = MibTableColumn
mgmdPmRouterInterfaceIgmpResetCounts = _MgmdPmRouterInterfaceIgmpResetCounts_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 23),
    _MgmdPmRouterInterfaceIgmpResetCounts_Type()
)
mgmdPmRouterInterfaceIgmpResetCounts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceIgmpResetCounts.setStatus("current")
_MgmdPmRouterInterfaceIgmpCountIntvl_Type = Unsigned32
_MgmdPmRouterInterfaceIgmpCountIntvl_Object = MibTableColumn
mgmdPmRouterInterfaceIgmpCountIntvl = _MgmdPmRouterInterfaceIgmpCountIntvl_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 24),
    _MgmdPmRouterInterfaceIgmpCountIntvl_Type()
)
mgmdPmRouterInterfaceIgmpCountIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceIgmpCountIntvl.setStatus("current")
_MgmdPmRouterInterfaceIgmpRcvCount_Type = Unsigned32
_MgmdPmRouterInterfaceIgmpRcvCount_Object = MibTableColumn
mgmdPmRouterInterfaceIgmpRcvCount = _MgmdPmRouterInterfaceIgmpRcvCount_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 25),
    _MgmdPmRouterInterfaceIgmpRcvCount_Type()
)
mgmdPmRouterInterfaceIgmpRcvCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceIgmpRcvCount.setStatus("current")
_MgmdPmRouterInterfaceIgmpSendCount_Type = Unsigned32
_MgmdPmRouterInterfaceIgmpSendCount_Object = MibTableColumn
mgmdPmRouterInterfaceIgmpSendCount = _MgmdPmRouterInterfaceIgmpSendCount_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 26),
    _MgmdPmRouterInterfaceIgmpSendCount_Type()
)
mgmdPmRouterInterfaceIgmpSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceIgmpSendCount.setStatus("current")


class _MgmdPmRouterInterfaceProxyAutoSwitchback_Type(TruthValue):
    """Custom type mgmdPmRouterInterfaceProxyAutoSwitchback based on TruthValue"""


_MgmdPmRouterInterfaceProxyAutoSwitchback_Object = MibTableColumn
mgmdPmRouterInterfaceProxyAutoSwitchback = _MgmdPmRouterInterfaceProxyAutoSwitchback_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 99, 1, 4, 1, 27),
    _MgmdPmRouterInterfaceProxyAutoSwitchback_Type()
)
mgmdPmRouterInterfaceProxyAutoSwitchback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mgmdPmRouterInterfaceProxyAutoSwitchback.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-MGMD-MIB",
    **{"NonZeroUnsigned8": NonZeroUnsigned8,
       "NonZeroInteger": NonZeroInteger,
       "AdminStatus": AdminStatus,
       "OperStatus": OperStatus,
       "PmIndex": PmIndex,
       "MjStatus": MjStatus,
       "InterfaceType": InterfaceType,
       "MgmdEntityType": MgmdEntityType,
       "dcMgmdMib": dcMgmdMib,
       "mgmdPmEntTable": mgmdPmEntTable,
       "mgmdPmEntEntry": mgmdPmEntEntry,
       "mgmdPmEntIndex": mgmdPmEntIndex,
       "mgmdPmEntAdminStatus": mgmdPmEntAdminStatus,
       "mgmdPmEntOperStatus": mgmdPmEntOperStatus,
       "mgmdPmEntRowStatus": mgmdPmEntRowStatus,
       "mgmdPmMjTable": mgmdPmMjTable,
       "mgmdPmMjEntry": mgmdPmMjEntry,
       "mgmdPmMjEntIndex": mgmdPmMjEntIndex,
       "mgmdPmMjInterfaceId": mgmdPmMjInterfaceId,
       "mgmdPmMjPartnerIndex": mgmdPmMjPartnerIndex,
       "mgmdPmMjRowStatus": mgmdPmMjRowStatus,
       "mgmdPmMjAdminStatus": mgmdPmMjAdminStatus,
       "mgmdPmMjOperStatus": mgmdPmMjOperStatus,
       "mgmdPmMjJoinStatus": mgmdPmMjJoinStatus,
       "mgmdPmStaticGroupTable": mgmdPmStaticGroupTable,
       "mgmdPmStaticGroupEntry": mgmdPmStaticGroupEntry,
       "mgmdPmStaticGroupEntityType": mgmdPmStaticGroupEntityType,
       "mgmdPmStaticGroupIfIndex": mgmdPmStaticGroupIfIndex,
       "mgmdPmStaticGroupAddressType": mgmdPmStaticGroupAddressType,
       "mgmdPmStaticGroupAddress": mgmdPmStaticGroupAddress,
       "mgmdPmStaticGroupSourceAddress": mgmdPmStaticGroupSourceAddress,
       "mgmdPmStaticGroupStatus": mgmdPmStaticGroupStatus,
       "mgmdPmStaticGroupStorageType": mgmdPmStaticGroupStorageType,
       "mgmdPmRouterInterfaceTable": mgmdPmRouterInterfaceTable,
       "mgmdPmRouterInterfaceEntry": mgmdPmRouterInterfaceEntry,
       "mgmdPmRouterInterfaceIfIndex": mgmdPmRouterInterfaceIfIndex,
       "mgmdPmRouterInterfaceQuerierType": mgmdPmRouterInterfaceQuerierType,
       "mgmdPmRouterInterfaceQuerier": mgmdPmRouterInterfaceQuerier,
       "mgmdPmRouterInterfaceQueryInterval": mgmdPmRouterInterfaceQueryInterval,
       "mgmdPmRouterInterfaceStatus": mgmdPmRouterInterfaceStatus,
       "mgmdPmRouterInterfaceVersion": mgmdPmRouterInterfaceVersion,
       "mgmdPmRouterInterfaceQueryMaxResponseTime": mgmdPmRouterInterfaceQueryMaxResponseTime,
       "mgmdPmRouterInterfaceQuerierUpTime": mgmdPmRouterInterfaceQuerierUpTime,
       "mgmdPmRouterInterfaceQuerierExpiryTime": mgmdPmRouterInterfaceQuerierExpiryTime,
       "mgmdPmRouterInterfaceWrongVersionQueries": mgmdPmRouterInterfaceWrongVersionQueries,
       "mgmdPmRouterInterfaceJoins": mgmdPmRouterInterfaceJoins,
       "mgmdPmRouterInterfaceProxyIfIndex": mgmdPmRouterInterfaceProxyIfIndex,
       "mgmdPmRouterInterfaceGroups": mgmdPmRouterInterfaceGroups,
       "mgmdPmRouterInterfaceRobustness": mgmdPmRouterInterfaceRobustness,
       "mgmdPmRouterInterfaceLastMembQueryIntvl": mgmdPmRouterInterfaceLastMembQueryIntvl,
       "mgmdPmRouterInterfaceLastMembQueryCount": mgmdPmRouterInterfaceLastMembQueryCount,
       "mgmdPmRouterInterfaceStartupQueryCount": mgmdPmRouterInterfaceStartupQueryCount,
       "mgmdPmRouterInterfaceStartupQueryInterval": mgmdPmRouterInterfaceStartupQueryInterval,
       "mgmdPmRouterInterfaceStaticMulticastMode": mgmdPmRouterInterfaceStaticMulticastMode,
       "mgmdPmRouterInterfaceBackupProxyIfIndex": mgmdPmRouterInterfaceBackupProxyIfIndex,
       "mgmdPmRouterInterfaceActiveProxyIfIndex": mgmdPmRouterInterfaceActiveProxyIfIndex,
       "mgmdPmRouterInterfaceAccessList": mgmdPmRouterInterfaceAccessList,
       "mgmdPmRouterInterfaceIgmpResetCounts": mgmdPmRouterInterfaceIgmpResetCounts,
       "mgmdPmRouterInterfaceIgmpCountIntvl": mgmdPmRouterInterfaceIgmpCountIntvl,
       "mgmdPmRouterInterfaceIgmpRcvCount": mgmdPmRouterInterfaceIgmpRcvCount,
       "mgmdPmRouterInterfaceIgmpSendCount": mgmdPmRouterInterfaceIgmpSendCount,
       "mgmdPmRouterInterfaceProxyAutoSwitchback": mgmdPmRouterInterfaceProxyAutoSwitchback}
)
