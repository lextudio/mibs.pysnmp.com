# SNMP MIB module (CISCOSB-IpRouter) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-IpRouter
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:28 2024
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

(ipRedundancy,
 ipRipFilter,
 ipRouteLeaking,
 ipSpec,
 rip2Spec,
 rlIpRoutingProtPreference,
 rlOspf) = mibBuilder.importSymbols(
    "CISCOSB-IP",
    "ipRedundancy",
    "ipRipFilter",
    "ipRouteLeaking",
    "ipSpec",
    "rip2Spec",
    "rlIpRoutingProtPreference",
    "rlOspf")

(AreaID,
 RouterID,
 ospfIfEntry,
 ospfVirtIfEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "RouterID",
    "ospfIfEntry",
    "ospfVirtIfEntry")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlIpRouter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 18)
)
rlIpRouter.setRevisions(
        ("2004-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsRip2IfConfTable_Object = MibTable
rsRip2IfConfTable = _RsRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1)
)
if mibBuilder.loadTexts:
    rsRip2IfConfTable.setStatus("current")
_RsRip2IfConfEntry_Object = MibTableRow
rsRip2IfConfEntry = _RsRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1)
)
rsRip2IfConfEntry.setIndexNames(
    (0, "CISCOSB-IpRouter", "rsRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    rsRip2IfConfEntry.setStatus("current")
_RsRip2IfConfAddress_Type = IpAddress
_RsRip2IfConfAddress_Object = MibTableColumn
rsRip2IfConfAddress = _RsRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1, 1),
    _RsRip2IfConfAddress_Type()
)
rsRip2IfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRip2IfConfAddress.setStatus("current")


class _RsRip2IfConfVirtualDis_Type(Integer32):
    """Custom type rsRip2IfConfVirtualDis based on Integer32"""
    defaultValue = 1


_RsRip2IfConfVirtualDis_Object = MibTableColumn
rsRip2IfConfVirtualDis = _RsRip2IfConfVirtualDis_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1, 2),
    _RsRip2IfConfVirtualDis_Type()
)
rsRip2IfConfVirtualDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRip2IfConfVirtualDis.setStatus("current")
_RlRip2IfConfKeyChain_Type = DisplayString
_RlRip2IfConfKeyChain_Object = MibTableColumn
rlRip2IfConfKeyChain = _RlRip2IfConfKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1, 3),
    _RlRip2IfConfKeyChain_Type()
)
rlRip2IfConfKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2IfConfKeyChain.setStatus("current")


class _RlRip2IfConfAdminStatus_Type(Integer32):
    """Custom type rlRip2IfConfAdminStatus based on Integer32"""
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


_RlRip2IfConfAdminStatus_Type.__name__ = "Integer32"
_RlRip2IfConfAdminStatus_Object = MibTableColumn
rlRip2IfConfAdminStatus = _RlRip2IfConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1, 4),
    _RlRip2IfConfAdminStatus_Type()
)
rlRip2IfConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2IfConfAdminStatus.setStatus("current")


class _RlRip2IfConfInFilteringType_Type(Integer32):
    """Custom type rlRip2IfConfInFilteringType based on Integer32"""
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
        *(("none", 1),
          ("pefixList", 3),
          ("stdIpAcl", 2))
    )


_RlRip2IfConfInFilteringType_Type.__name__ = "Integer32"
_RlRip2IfConfInFilteringType_Object = MibTableColumn
rlRip2IfConfInFilteringType = _RlRip2IfConfInFilteringType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1, 5),
    _RlRip2IfConfInFilteringType_Type()
)
rlRip2IfConfInFilteringType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2IfConfInFilteringType.setStatus("current")


class _RlRip2IfConfOutFilteringType_Type(Integer32):
    """Custom type rlRip2IfConfOutFilteringType based on Integer32"""
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
        *(("none", 1),
          ("pefixList", 3),
          ("stdIpAcl", 2))
    )


_RlRip2IfConfOutFilteringType_Type.__name__ = "Integer32"
_RlRip2IfConfOutFilteringType_Object = MibTableColumn
rlRip2IfConfOutFilteringType = _RlRip2IfConfOutFilteringType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1, 6),
    _RlRip2IfConfOutFilteringType_Type()
)
rlRip2IfConfOutFilteringType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2IfConfOutFilteringType.setStatus("current")
_RlRip2IfConfInFilterListName_Type = DisplayString
_RlRip2IfConfInFilterListName_Object = MibTableColumn
rlRip2IfConfInFilterListName = _RlRip2IfConfInFilterListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1, 7),
    _RlRip2IfConfInFilterListName_Type()
)
rlRip2IfConfInFilterListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2IfConfInFilterListName.setStatus("current")
_RlRip2IfConfOutFilterListName_Type = DisplayString
_RlRip2IfConfOutFilterListName_Object = MibTableColumn
rlRip2IfConfOutFilterListName = _RlRip2IfConfOutFilterListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1, 8),
    _RlRip2IfConfOutFilterListName_Type()
)
rlRip2IfConfOutFilterListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2IfConfOutFilterListName.setStatus("current")


class _RlRip2IfConfDefInfOriginate_Type(Integer32):
    """Custom type rlRip2IfConfDefInfOriginate based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 2),
          ("enabled", 3),
          ("global", 1),
          ("passiveOnly", 4))
    )


_RlRip2IfConfDefInfOriginate_Type.__name__ = "Integer32"
_RlRip2IfConfDefInfOriginate_Object = MibTableColumn
rlRip2IfConfDefInfOriginate = _RlRip2IfConfDefInfOriginate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 1, 1, 9),
    _RlRip2IfConfDefInfOriginate_Type()
)
rlRip2IfConfDefInfOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2IfConfDefInfOriginate.setStatus("current")
_RlRip2MibVersion_Type = Integer32
_RlRip2MibVersion_Object = MibScalar
rlRip2MibVersion = _RlRip2MibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 2),
    _RlRip2MibVersion_Type()
)
rlRip2MibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRip2MibVersion.setStatus("current")


class _RlRip2RedistDefaultMetric_Type(Unsigned32):
    """Custom type rlRip2RedistDefaultMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlRip2RedistDefaultMetric_Type.__name__ = "Unsigned32"
_RlRip2RedistDefaultMetric_Object = MibScalar
rlRip2RedistDefaultMetric = _RlRip2RedistDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 3),
    _RlRip2RedistDefaultMetric_Type()
)
rlRip2RedistDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2RedistDefaultMetric.setStatus("current")


class _RlRip2RedistStaticTransparent_Type(TruthValue):
    """Custom type rlRip2RedistStaticTransparent based on TruthValue"""


_RlRip2RedistStaticTransparent_Object = MibScalar
rlRip2RedistStaticTransparent = _RlRip2RedistStaticTransparent_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 4),
    _RlRip2RedistStaticTransparent_Type()
)
rlRip2RedistStaticTransparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2RedistStaticTransparent.setStatus("current")


class _RlRip2ClearStatistics_Type(TruthValue):
    """Custom type rlRip2ClearStatistics based on TruthValue"""


_RlRip2ClearStatistics_Object = MibScalar
rlRip2ClearStatistics = _RlRip2ClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 5),
    _RlRip2ClearStatistics_Type()
)
rlRip2ClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2ClearStatistics.setStatus("current")


class _RlRip2IfConfGlobalPassiveInterface_Type(TruthValue):
    """Custom type rlRip2IfConfGlobalPassiveInterface based on TruthValue"""


_RlRip2IfConfGlobalPassiveInterface_Object = MibScalar
rlRip2IfConfGlobalPassiveInterface = _RlRip2IfConfGlobalPassiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 6),
    _RlRip2IfConfGlobalPassiveInterface_Type()
)
rlRip2IfConfGlobalPassiveInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2IfConfGlobalPassiveInterface.setStatus("current")


class _RlRip2GlobalDefInfOriginate_Type(Integer32):
    """Custom type rlRip2GlobalDefInfOriginate based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("passiveOnly", 3))
    )


_RlRip2GlobalDefInfOriginate_Type.__name__ = "Integer32"
_RlRip2GlobalDefInfOriginate_Object = MibScalar
rlRip2GlobalDefInfOriginate = _RlRip2GlobalDefInfOriginate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 7),
    _RlRip2GlobalDefInfOriginate_Type()
)
rlRip2GlobalDefInfOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2GlobalDefInfOriginate.setStatus("current")


class _RlRip2RedistConnected_Type(TruthValue):
    """Custom type rlRip2RedistConnected based on TruthValue"""


_RlRip2RedistConnected_Object = MibScalar
rlRip2RedistConnected = _RlRip2RedistConnected_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 8),
    _RlRip2RedistConnected_Type()
)
rlRip2RedistConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2RedistConnected.setStatus("current")


class _RlRip2RedistConnectedTransparent_Type(TruthValue):
    """Custom type rlRip2RedistConnectedTransparent based on TruthValue"""


_RlRip2RedistConnectedTransparent_Object = MibScalar
rlRip2RedistConnectedTransparent = _RlRip2RedistConnectedTransparent_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 9),
    _RlRip2RedistConnectedTransparent_Type()
)
rlRip2RedistConnectedTransparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2RedistConnectedTransparent.setStatus("current")


class _RlRip2RedistConnectedMetric_Type(Unsigned32):
    """Custom type rlRip2RedistConnectedMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RlRip2RedistConnectedMetric_Type.__name__ = "Unsigned32"
_RlRip2RedistConnectedMetric_Object = MibScalar
rlRip2RedistConnectedMetric = _RlRip2RedistConnectedMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 3, 10),
    _RlRip2RedistConnectedMetric_Type()
)
rlRip2RedistConnectedMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRip2RedistConnectedMetric.setStatus("current")


class _IpRedundAdminStatus_Type(Integer32):
    """Custom type ipRedundAdminStatus based on Integer32"""
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


_IpRedundAdminStatus_Type.__name__ = "Integer32"
_IpRedundAdminStatus_Object = MibScalar
ipRedundAdminStatus = _IpRedundAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 1),
    _IpRedundAdminStatus_Type()
)
ipRedundAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundAdminStatus.setStatus("current")


class _IpRedundOperStatus_Type(Integer32):
    """Custom type ipRedundOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpRedundOperStatus_Type.__name__ = "Integer32"
_IpRedundOperStatus_Object = MibScalar
ipRedundOperStatus = _IpRedundOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 2),
    _IpRedundOperStatus_Type()
)
ipRedundOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundOperStatus.setStatus("current")
_IpRedundRoutersTable_Object = MibTable
ipRedundRoutersTable = _IpRedundRoutersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 3)
)
if mibBuilder.loadTexts:
    ipRedundRoutersTable.setStatus("current")
_IpRedundRoutersEntry_Object = MibTableRow
ipRedundRoutersEntry = _IpRedundRoutersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 3, 1)
)
ipRedundRoutersEntry.setIndexNames(
    (0, "CISCOSB-IpRouter", "ipRedundRoutersIfAddr"),
    (0, "CISCOSB-IpRouter", "ipRedundRoutersMainRouterAddr"),
)
if mibBuilder.loadTexts:
    ipRedundRoutersEntry.setStatus("current")
_IpRedundRoutersIfAddr_Type = IpAddress
_IpRedundRoutersIfAddr_Object = MibTableColumn
ipRedundRoutersIfAddr = _IpRedundRoutersIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 3, 1, 1),
    _IpRedundRoutersIfAddr_Type()
)
ipRedundRoutersIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundRoutersIfAddr.setStatus("current")
_IpRedundRoutersMainRouterAddr_Type = IpAddress
_IpRedundRoutersMainRouterAddr_Object = MibTableColumn
ipRedundRoutersMainRouterAddr = _IpRedundRoutersMainRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 3, 1, 2),
    _IpRedundRoutersMainRouterAddr_Type()
)
ipRedundRoutersMainRouterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundRoutersMainRouterAddr.setStatus("current")


class _IpRedundRoutersOperStatus_Type(Integer32):
    """Custom type ipRedundRoutersOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpRedundRoutersOperStatus_Type.__name__ = "Integer32"
_IpRedundRoutersOperStatus_Object = MibTableColumn
ipRedundRoutersOperStatus = _IpRedundRoutersOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 3, 1, 3),
    _IpRedundRoutersOperStatus_Type()
)
ipRedundRoutersOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRedundRoutersOperStatus.setStatus("current")


class _IpRedundRoutersPollInterval_Type(Integer32):
    """Custom type ipRedundRoutersPollInterval based on Integer32"""
    defaultValue = 3


_IpRedundRoutersPollInterval_Object = MibTableColumn
ipRedundRoutersPollInterval = _IpRedundRoutersPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 3, 1, 4),
    _IpRedundRoutersPollInterval_Type()
)
ipRedundRoutersPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundRoutersPollInterval.setStatus("current")


class _IpRedundRoutersTimeout_Type(Integer32):
    """Custom type ipRedundRoutersTimeout based on Integer32"""
    defaultValue = 12


_IpRedundRoutersTimeout_Object = MibTableColumn
ipRedundRoutersTimeout = _IpRedundRoutersTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 3, 1, 5),
    _IpRedundRoutersTimeout_Type()
)
ipRedundRoutersTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundRoutersTimeout.setStatus("current")


class _IpRedundRoutersStatus_Type(Integer32):
    """Custom type ipRedundRoutersStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_IpRedundRoutersStatus_Type.__name__ = "Integer32"
_IpRedundRoutersStatus_Object = MibTableColumn
ipRedundRoutersStatus = _IpRedundRoutersStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 6, 3, 1, 6),
    _IpRedundRoutersStatus_Type()
)
ipRedundRoutersStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundRoutersStatus.setStatus("current")


class _IpLeakStaticToRip_Type(Integer32):
    """Custom type ipLeakStaticToRip based on Integer32"""
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


_IpLeakStaticToRip_Type.__name__ = "Integer32"
_IpLeakStaticToRip_Object = MibScalar
ipLeakStaticToRip = _IpLeakStaticToRip_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 7, 1),
    _IpLeakStaticToRip_Type()
)
ipLeakStaticToRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakStaticToRip.setStatus("current")


class _IpLeakStaticToOspf_Type(Integer32):
    """Custom type ipLeakStaticToOspf based on Integer32"""
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


_IpLeakStaticToOspf_Type.__name__ = "Integer32"
_IpLeakStaticToOspf_Object = MibScalar
ipLeakStaticToOspf = _IpLeakStaticToOspf_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 7, 2),
    _IpLeakStaticToOspf_Type()
)
ipLeakStaticToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakStaticToOspf.setStatus("current")


class _IpLeakOspfToRip_Type(Integer32):
    """Custom type ipLeakOspfToRip based on Integer32"""
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


_IpLeakOspfToRip_Type.__name__ = "Integer32"
_IpLeakOspfToRip_Object = MibScalar
ipLeakOspfToRip = _IpLeakOspfToRip_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 7, 3),
    _IpLeakOspfToRip_Type()
)
ipLeakOspfToRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakOspfToRip.setStatus("current")


class _IpLeakRipToOspf_Type(Integer32):
    """Custom type ipLeakRipToOspf based on Integer32"""
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


_IpLeakRipToOspf_Type.__name__ = "Integer32"
_IpLeakRipToOspf_Object = MibScalar
ipLeakRipToOspf = _IpLeakRipToOspf_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 7, 4),
    _IpLeakRipToOspf_Type()
)
ipLeakRipToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakRipToOspf.setStatus("current")


class _IpLeakExtDirectToOspf_Type(Integer32):
    """Custom type ipLeakExtDirectToOspf based on Integer32"""
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


_IpLeakExtDirectToOspf_Type.__name__ = "Integer32"
_IpLeakExtDirectToOspf_Object = MibScalar
ipLeakExtDirectToOspf = _IpLeakExtDirectToOspf_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 7, 5),
    _IpLeakExtDirectToOspf_Type()
)
ipLeakExtDirectToOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLeakExtDirectToOspf.setStatus("current")
_RsIpRipFilterGlbTable_Object = MibTable
rsIpRipFilterGlbTable = _RsIpRipFilterGlbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 1)
)
if mibBuilder.loadTexts:
    rsIpRipFilterGlbTable.setStatus("current")
_RsIpRipFilterGlbEntry_Object = MibTableRow
rsIpRipFilterGlbEntry = _RsIpRipFilterGlbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 1, 1)
)
rsIpRipFilterGlbEntry.setIndexNames(
    (0, "CISCOSB-IpRouter", "rsIpRipFilterGlbType"),
    (0, "CISCOSB-IpRouter", "rsIpRipFilterGlbNumber"),
)
if mibBuilder.loadTexts:
    rsIpRipFilterGlbEntry.setStatus("current")


class _RsIpRipFilterGlbType_Type(Integer32):
    """Custom type rsIpRipFilterGlbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RsIpRipFilterGlbType_Type.__name__ = "Integer32"
_RsIpRipFilterGlbType_Object = MibTableColumn
rsIpRipFilterGlbType = _RsIpRipFilterGlbType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 1, 1, 1),
    _RsIpRipFilterGlbType_Type()
)
rsIpRipFilterGlbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbType.setStatus("current")
_RsIpRipFilterGlbNumber_Type = Integer32
_RsIpRipFilterGlbNumber_Object = MibTableColumn
rsIpRipFilterGlbNumber = _RsIpRipFilterGlbNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 1, 1, 2),
    _RsIpRipFilterGlbNumber_Type()
)
rsIpRipFilterGlbNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbNumber.setStatus("current")


class _RsIpRipFilterGlbStatus_Type(Integer32):
    """Custom type rsIpRipFilterGlbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("underCreation", 3),
          ("valid", 1))
    )


_RsIpRipFilterGlbStatus_Type.__name__ = "Integer32"
_RsIpRipFilterGlbStatus_Object = MibTableColumn
rsIpRipFilterGlbStatus = _RsIpRipFilterGlbStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 1, 1, 3),
    _RsIpRipFilterGlbStatus_Type()
)
rsIpRipFilterGlbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbStatus.setStatus("current")


class _RsIpRipFilterGlbIpAddr_Type(IpAddress):
    """Custom type rsIpRipFilterGlbIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpRipFilterGlbIpAddr_Object = MibTableColumn
rsIpRipFilterGlbIpAddr = _RsIpRipFilterGlbIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 1, 1, 4),
    _RsIpRipFilterGlbIpAddr_Type()
)
rsIpRipFilterGlbIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbIpAddr.setStatus("current")


class _RsIpRipFilterGlbNetworkMaskBits_Type(Integer32):
    """Custom type rsIpRipFilterGlbNetworkMaskBits based on Integer32"""
    defaultValue = 0


_RsIpRipFilterGlbNetworkMaskBits_Object = MibTableColumn
rsIpRipFilterGlbNetworkMaskBits = _RsIpRipFilterGlbNetworkMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 1, 1, 5),
    _RsIpRipFilterGlbNetworkMaskBits_Type()
)
rsIpRipFilterGlbNetworkMaskBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbNetworkMaskBits.setStatus("current")


class _RsIpRipFilterGlbMatchBits_Type(Integer32):
    """Custom type rsIpRipFilterGlbMatchBits based on Integer32"""
    defaultValue = 32


_RsIpRipFilterGlbMatchBits_Object = MibTableColumn
rsIpRipFilterGlbMatchBits = _RsIpRipFilterGlbMatchBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 1, 1, 6),
    _RsIpRipFilterGlbMatchBits_Type()
)
rsIpRipFilterGlbMatchBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbMatchBits.setStatus("current")


class _RsIpRipFilterGlbAction_Type(Integer32):
    """Custom type rsIpRipFilterGlbAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RsIpRipFilterGlbAction_Type.__name__ = "Integer32"
_RsIpRipFilterGlbAction_Object = MibTableColumn
rsIpRipFilterGlbAction = _RsIpRipFilterGlbAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 1, 1, 7),
    _RsIpRipFilterGlbAction_Type()
)
rsIpRipFilterGlbAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterGlbAction.setStatus("current")
_RsIpRipFilterLclTable_Object = MibTable
rsIpRipFilterLclTable = _RsIpRipFilterLclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2)
)
if mibBuilder.loadTexts:
    rsIpRipFilterLclTable.setStatus("current")
_RsIpRipFilterLclEntry_Object = MibTableRow
rsIpRipFilterLclEntry = _RsIpRipFilterLclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2, 1)
)
rsIpRipFilterLclEntry.setIndexNames(
    (0, "CISCOSB-IpRouter", "rsIpRipFilterLclIpIntf"),
    (0, "CISCOSB-IpRouter", "rsIpRipFilterLclType"),
    (0, "CISCOSB-IpRouter", "rsIpRipFilterLclNumber"),
)
if mibBuilder.loadTexts:
    rsIpRipFilterLclEntry.setStatus("current")
_RsIpRipFilterLclIpIntf_Type = IpAddress
_RsIpRipFilterLclIpIntf_Object = MibTableColumn
rsIpRipFilterLclIpIntf = _RsIpRipFilterLclIpIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2, 1, 1),
    _RsIpRipFilterLclIpIntf_Type()
)
rsIpRipFilterLclIpIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterLclIpIntf.setStatus("current")


class _RsIpRipFilterLclType_Type(Integer32):
    """Custom type rsIpRipFilterLclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RsIpRipFilterLclType_Type.__name__ = "Integer32"
_RsIpRipFilterLclType_Object = MibTableColumn
rsIpRipFilterLclType = _RsIpRipFilterLclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2, 1, 2),
    _RsIpRipFilterLclType_Type()
)
rsIpRipFilterLclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterLclType.setStatus("current")
_RsIpRipFilterLclNumber_Type = Integer32
_RsIpRipFilterLclNumber_Object = MibTableColumn
rsIpRipFilterLclNumber = _RsIpRipFilterLclNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2, 1, 3),
    _RsIpRipFilterLclNumber_Type()
)
rsIpRipFilterLclNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpRipFilterLclNumber.setStatus("current")


class _RsIpRipFilterLclStatus_Type(Integer32):
    """Custom type rsIpRipFilterLclStatus based on Integer32"""
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
        *(("invalid", 2),
          ("underCreation", 3),
          ("valid", 1))
    )


_RsIpRipFilterLclStatus_Type.__name__ = "Integer32"
_RsIpRipFilterLclStatus_Object = MibTableColumn
rsIpRipFilterLclStatus = _RsIpRipFilterLclStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2, 1, 4),
    _RsIpRipFilterLclStatus_Type()
)
rsIpRipFilterLclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclStatus.setStatus("current")


class _RsIpRipFilterLclIpAddr_Type(IpAddress):
    """Custom type rsIpRipFilterLclIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_RsIpRipFilterLclIpAddr_Object = MibTableColumn
rsIpRipFilterLclIpAddr = _RsIpRipFilterLclIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2, 1, 5),
    _RsIpRipFilterLclIpAddr_Type()
)
rsIpRipFilterLclIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclIpAddr.setStatus("current")


class _RsIpRipFilterLclNetworkMaskBits_Type(Integer32):
    """Custom type rsIpRipFilterLclNetworkMaskBits based on Integer32"""
    defaultValue = 0


_RsIpRipFilterLclNetworkMaskBits_Object = MibTableColumn
rsIpRipFilterLclNetworkMaskBits = _RsIpRipFilterLclNetworkMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2, 1, 6),
    _RsIpRipFilterLclNetworkMaskBits_Type()
)
rsIpRipFilterLclNetworkMaskBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclNetworkMaskBits.setStatus("current")


class _RsIpRipFilterLclMatchBits_Type(Integer32):
    """Custom type rsIpRipFilterLclMatchBits based on Integer32"""
    defaultValue = 32


_RsIpRipFilterLclMatchBits_Object = MibTableColumn
rsIpRipFilterLclMatchBits = _RsIpRipFilterLclMatchBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2, 1, 7),
    _RsIpRipFilterLclMatchBits_Type()
)
rsIpRipFilterLclMatchBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclMatchBits.setStatus("current")


class _RsIpRipFilterLclAction_Type(Integer32):
    """Custom type rsIpRipFilterLclAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RsIpRipFilterLclAction_Type.__name__ = "Integer32"
_RsIpRipFilterLclAction_Object = MibTableColumn
rsIpRipFilterLclAction = _RsIpRipFilterLclAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 8, 2, 1, 8),
    _RsIpRipFilterLclAction_Type()
)
rsIpRipFilterLclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpRipFilterLclAction.setStatus("current")


class _RlIpRoutingProtPreferenceDirect_Type(Integer32):
    """Custom type rlIpRoutingProtPreferenceDirect based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_RlIpRoutingProtPreferenceDirect_Type.__name__ = "Integer32"
_RlIpRoutingProtPreferenceDirect_Object = MibScalar
rlIpRoutingProtPreferenceDirect = _RlIpRoutingProtPreferenceDirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 13, 1),
    _RlIpRoutingProtPreferenceDirect_Type()
)
rlIpRoutingProtPreferenceDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpRoutingProtPreferenceDirect.setStatus("current")


class _RlIpRoutingProtPreferenceStatic_Type(Integer32):
    """Custom type rlIpRoutingProtPreferenceStatic based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlIpRoutingProtPreferenceStatic_Type.__name__ = "Integer32"
_RlIpRoutingProtPreferenceStatic_Object = MibScalar
rlIpRoutingProtPreferenceStatic = _RlIpRoutingProtPreferenceStatic_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 13, 2),
    _RlIpRoutingProtPreferenceStatic_Type()
)
rlIpRoutingProtPreferenceStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpRoutingProtPreferenceStatic.setStatus("current")


class _RlIpRoutingProtPreferenceOspfInter_Type(Integer32):
    """Custom type rlIpRoutingProtPreferenceOspfInter based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlIpRoutingProtPreferenceOspfInter_Type.__name__ = "Integer32"
_RlIpRoutingProtPreferenceOspfInter_Object = MibScalar
rlIpRoutingProtPreferenceOspfInter = _RlIpRoutingProtPreferenceOspfInter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 13, 3),
    _RlIpRoutingProtPreferenceOspfInter_Type()
)
rlIpRoutingProtPreferenceOspfInter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpRoutingProtPreferenceOspfInter.setStatus("current")


class _RlIpRoutingProtPreferenceOspfExt_Type(Integer32):
    """Custom type rlIpRoutingProtPreferenceOspfExt based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlIpRoutingProtPreferenceOspfExt_Type.__name__ = "Integer32"
_RlIpRoutingProtPreferenceOspfExt_Object = MibScalar
rlIpRoutingProtPreferenceOspfExt = _RlIpRoutingProtPreferenceOspfExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 13, 4),
    _RlIpRoutingProtPreferenceOspfExt_Type()
)
rlIpRoutingProtPreferenceOspfExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpRoutingProtPreferenceOspfExt.setStatus("current")


class _RlIpRoutingProtPreferenceOspfReject_Type(Integer32):
    """Custom type rlIpRoutingProtPreferenceOspfReject based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlIpRoutingProtPreferenceOspfReject_Type.__name__ = "Integer32"
_RlIpRoutingProtPreferenceOspfReject_Object = MibScalar
rlIpRoutingProtPreferenceOspfReject = _RlIpRoutingProtPreferenceOspfReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 13, 5),
    _RlIpRoutingProtPreferenceOspfReject_Type()
)
rlIpRoutingProtPreferenceOspfReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpRoutingProtPreferenceOspfReject.setStatus("current")


class _RlIpRoutingProtPreferenceRipNormal_Type(Integer32):
    """Custom type rlIpRoutingProtPreferenceRipNormal based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlIpRoutingProtPreferenceRipNormal_Type.__name__ = "Integer32"
_RlIpRoutingProtPreferenceRipNormal_Object = MibScalar
rlIpRoutingProtPreferenceRipNormal = _RlIpRoutingProtPreferenceRipNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 13, 6),
    _RlIpRoutingProtPreferenceRipNormal_Type()
)
rlIpRoutingProtPreferenceRipNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpRoutingProtPreferenceRipNormal.setStatus("current")


class _RlIpRoutingProtPreferenceRipAggregate_Type(Integer32):
    """Custom type rlIpRoutingProtPreferenceRipAggregate based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlIpRoutingProtPreferenceRipAggregate_Type.__name__ = "Integer32"
_RlIpRoutingProtPreferenceRipAggregate_Object = MibScalar
rlIpRoutingProtPreferenceRipAggregate = _RlIpRoutingProtPreferenceRipAggregate_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 13, 7),
    _RlIpRoutingProtPreferenceRipAggregate_Type()
)
rlIpRoutingProtPreferenceRipAggregate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpRoutingProtPreferenceRipAggregate.setStatus("current")


class _RlIpRoutingProtPreferenceBgp_Type(Integer32):
    """Custom type rlIpRoutingProtPreferenceBgp based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlIpRoutingProtPreferenceBgp_Type.__name__ = "Integer32"
_RlIpRoutingProtPreferenceBgp_Object = MibScalar
rlIpRoutingProtPreferenceBgp = _RlIpRoutingProtPreferenceBgp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 13, 8),
    _RlIpRoutingProtPreferenceBgp_Type()
)
rlIpRoutingProtPreferenceBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpRoutingProtPreferenceBgp.setStatus("current")
_RlOspfMibVersion_Type = Integer32
_RlOspfMibVersion_Object = MibScalar
rlOspfMibVersion = _RlOspfMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 1),
    _RlOspfMibVersion_Type()
)
rlOspfMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfMibVersion.setStatus("current")


class _RlOspfAutoInterfaceCreation_Type(Integer32):
    """Custom type rlOspfAutoInterfaceCreation based on Integer32"""
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


_RlOspfAutoInterfaceCreation_Type.__name__ = "Integer32"
_RlOspfAutoInterfaceCreation_Object = MibScalar
rlOspfAutoInterfaceCreation = _RlOspfAutoInterfaceCreation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 2),
    _RlOspfAutoInterfaceCreation_Type()
)
rlOspfAutoInterfaceCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAutoInterfaceCreation.setStatus("current")
_RlOspfIfExtTable_Object = MibTable
rlOspfIfExtTable = _RlOspfIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 3)
)
if mibBuilder.loadTexts:
    rlOspfIfExtTable.setStatus("current")
_RlOspfIfExtEntry_Object = MibTableRow
rlOspfIfExtEntry = _RlOspfIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 3, 1)
)
if mibBuilder.loadTexts:
    rlOspfIfExtEntry.setStatus("current")
_RlOspfifKeyChain_Type = DisplayString
_RlOspfifKeyChain_Object = MibTableColumn
rlOspfifKeyChain = _RlOspfifKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 3, 1, 1),
    _RlOspfifKeyChain_Type()
)
rlOspfifKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOspfifKeyChain.setStatus("current")
_RlOspfRtrLnkTable_Object = MibTable
rlOspfRtrLnkTable = _RlOspfRtrLnkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4)
)
if mibBuilder.loadTexts:
    rlOspfRtrLnkTable.setStatus("current")
_RlOspfRtrLnkEntry_Object = MibTableRow
rlOspfRtrLnkEntry = _RlOspfRtrLnkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1)
)
rlOspfRtrLnkEntry.setIndexNames(
    (0, "CISCOSB-IpRouter", "rlOspfRtrLnkAreaId"),
    (0, "CISCOSB-IpRouter", "rlOspfRtrLnkLsid"),
    (0, "CISCOSB-IpRouter", "rlOspfRtrLnkRouterId"),
    (0, "CISCOSB-IpRouter", "rlOspfRtrLnkIdx"),
)
if mibBuilder.loadTexts:
    rlOspfRtrLnkEntry.setStatus("current")
_RlOspfRtrLnkAreaId_Type = AreaID
_RlOspfRtrLnkAreaId_Object = MibTableColumn
rlOspfRtrLnkAreaId = _RlOspfRtrLnkAreaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 1),
    _RlOspfRtrLnkAreaId_Type()
)
rlOspfRtrLnkAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkAreaId.setStatus("current")
_RlOspfRtrLnkLsid_Type = IpAddress
_RlOspfRtrLnkLsid_Object = MibTableColumn
rlOspfRtrLnkLsid = _RlOspfRtrLnkLsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 2),
    _RlOspfRtrLnkLsid_Type()
)
rlOspfRtrLnkLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkLsid.setStatus("current")
_RlOspfRtrLnkRouterId_Type = RouterID
_RlOspfRtrLnkRouterId_Object = MibTableColumn
rlOspfRtrLnkRouterId = _RlOspfRtrLnkRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 3),
    _RlOspfRtrLnkRouterId_Type()
)
rlOspfRtrLnkRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkRouterId.setStatus("current")


class _RlOspfRtrLnkIdx_Type(Unsigned32):
    """Custom type rlOspfRtrLnkIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfRtrLnkIdx_Type.__name__ = "Unsigned32"
_RlOspfRtrLnkIdx_Object = MibTableColumn
rlOspfRtrLnkIdx = _RlOspfRtrLnkIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 4),
    _RlOspfRtrLnkIdx_Type()
)
rlOspfRtrLnkIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkIdx.setStatus("current")
_RlOspfRtrLnkSequence_Type = Integer32
_RlOspfRtrLnkSequence_Object = MibTableColumn
rlOspfRtrLnkSequence = _RlOspfRtrLnkSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 5),
    _RlOspfRtrLnkSequence_Type()
)
rlOspfRtrLnkSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkSequence.setStatus("current")
_RlOspfRtrLnkAge_Type = Integer32
_RlOspfRtrLnkAge_Object = MibTableColumn
rlOspfRtrLnkAge = _RlOspfRtrLnkAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 6),
    _RlOspfRtrLnkAge_Type()
)
rlOspfRtrLnkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkAge.setStatus("current")
_RlOspfRtrLnkChecksum_Type = Integer32
_RlOspfRtrLnkChecksum_Object = MibTableColumn
rlOspfRtrLnkChecksum = _RlOspfRtrLnkChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 7),
    _RlOspfRtrLnkChecksum_Type()
)
rlOspfRtrLnkChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkChecksum.setStatus("current")
_RlOspfRtrLnkLength_Type = Unsigned32
_RlOspfRtrLnkLength_Object = MibTableColumn
rlOspfRtrLnkLength = _RlOspfRtrLnkLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 8),
    _RlOspfRtrLnkLength_Type()
)
rlOspfRtrLnkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkLength.setStatus("current")


class _RlOspfRtrLnkBitV_Type(Integer32):
    """Custom type rlOspfRtrLnkBitV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfRtrLnkBitV_Type.__name__ = "Integer32"
_RlOspfRtrLnkBitV_Object = MibTableColumn
rlOspfRtrLnkBitV = _RlOspfRtrLnkBitV_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 9),
    _RlOspfRtrLnkBitV_Type()
)
rlOspfRtrLnkBitV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkBitV.setStatus("current")


class _RlOspfRtrLnkBitE_Type(Integer32):
    """Custom type rlOspfRtrLnkBitE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfRtrLnkBitE_Type.__name__ = "Integer32"
_RlOspfRtrLnkBitE_Object = MibTableColumn
rlOspfRtrLnkBitE = _RlOspfRtrLnkBitE_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 10),
    _RlOspfRtrLnkBitE_Type()
)
rlOspfRtrLnkBitE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkBitE.setStatus("current")


class _RlOspfRtrLnkBitB_Type(Integer32):
    """Custom type rlOspfRtrLnkBitB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfRtrLnkBitB_Type.__name__ = "Integer32"
_RlOspfRtrLnkBitB_Object = MibTableColumn
rlOspfRtrLnkBitB = _RlOspfRtrLnkBitB_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 11),
    _RlOspfRtrLnkBitB_Type()
)
rlOspfRtrLnkBitB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkBitB.setStatus("current")
_RlOspfRtrLnkLinks_Type = Unsigned32
_RlOspfRtrLnkLinks_Object = MibTableColumn
rlOspfRtrLnkLinks = _RlOspfRtrLnkLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 12),
    _RlOspfRtrLnkLinks_Type()
)
rlOspfRtrLnkLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkLinks.setStatus("current")
_RlOspfRtrLnkLinkID_Type = IpAddress
_RlOspfRtrLnkLinkID_Object = MibTableColumn
rlOspfRtrLnkLinkID = _RlOspfRtrLnkLinkID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 13),
    _RlOspfRtrLnkLinkID_Type()
)
rlOspfRtrLnkLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkLinkID.setStatus("current")
_RlOspfRtrLnkLinkData_Type = IpAddress
_RlOspfRtrLnkLinkData_Object = MibTableColumn
rlOspfRtrLnkLinkData = _RlOspfRtrLnkLinkData_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 14),
    _RlOspfRtrLnkLinkData_Type()
)
rlOspfRtrLnkLinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkLinkData.setStatus("current")


class _RlOspfRtrLnkType_Type(Integer32):
    """Custom type rlOspfRtrLnkType based on Integer32"""
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
        *(("pointToPoint", 1),
          ("stubNetwork", 3),
          ("transitNetwork", 2),
          ("virtualLink", 4))
    )


_RlOspfRtrLnkType_Type.__name__ = "Integer32"
_RlOspfRtrLnkType_Object = MibTableColumn
rlOspfRtrLnkType = _RlOspfRtrLnkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 15),
    _RlOspfRtrLnkType_Type()
)
rlOspfRtrLnkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkType.setStatus("current")
_RlOspfRtrLnkMetric_Type = Unsigned32
_RlOspfRtrLnkMetric_Object = MibTableColumn
rlOspfRtrLnkMetric = _RlOspfRtrLnkMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 4, 1, 16),
    _RlOspfRtrLnkMetric_Type()
)
rlOspfRtrLnkMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfRtrLnkMetric.setStatus("current")
_RlOspfNetLnkTable_Object = MibTable
rlOspfNetLnkTable = _RlOspfNetLnkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5)
)
if mibBuilder.loadTexts:
    rlOspfNetLnkTable.setStatus("current")
_RlOspfNetLnkEntry_Object = MibTableRow
rlOspfNetLnkEntry = _RlOspfNetLnkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1)
)
rlOspfNetLnkEntry.setIndexNames(
    (0, "CISCOSB-IpRouter", "rlOspfNetLnkAreaId"),
    (0, "CISCOSB-IpRouter", "rlOspfNetLnkLsid"),
    (0, "CISCOSB-IpRouter", "rlOspfNetLnkRouterId"),
    (0, "CISCOSB-IpRouter", "rlOspfNetLnkIdx"),
)
if mibBuilder.loadTexts:
    rlOspfNetLnkEntry.setStatus("current")
_RlOspfNetLnkAreaId_Type = AreaID
_RlOspfNetLnkAreaId_Object = MibTableColumn
rlOspfNetLnkAreaId = _RlOspfNetLnkAreaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 1),
    _RlOspfNetLnkAreaId_Type()
)
rlOspfNetLnkAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkAreaId.setStatus("current")
_RlOspfNetLnkLsid_Type = IpAddress
_RlOspfNetLnkLsid_Object = MibTableColumn
rlOspfNetLnkLsid = _RlOspfNetLnkLsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 2),
    _RlOspfNetLnkLsid_Type()
)
rlOspfNetLnkLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkLsid.setStatus("current")
_RlOspfNetLnkRouterId_Type = RouterID
_RlOspfNetLnkRouterId_Object = MibTableColumn
rlOspfNetLnkRouterId = _RlOspfNetLnkRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 3),
    _RlOspfNetLnkRouterId_Type()
)
rlOspfNetLnkRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkRouterId.setStatus("current")


class _RlOspfNetLnkIdx_Type(Unsigned32):
    """Custom type rlOspfNetLnkIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlOspfNetLnkIdx_Type.__name__ = "Unsigned32"
_RlOspfNetLnkIdx_Object = MibTableColumn
rlOspfNetLnkIdx = _RlOspfNetLnkIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 4),
    _RlOspfNetLnkIdx_Type()
)
rlOspfNetLnkIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkIdx.setStatus("current")
_RlOspfNetLnkSequence_Type = Integer32
_RlOspfNetLnkSequence_Object = MibTableColumn
rlOspfNetLnkSequence = _RlOspfNetLnkSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 5),
    _RlOspfNetLnkSequence_Type()
)
rlOspfNetLnkSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkSequence.setStatus("current")
_RlOspfNetLnkAge_Type = Integer32
_RlOspfNetLnkAge_Object = MibTableColumn
rlOspfNetLnkAge = _RlOspfNetLnkAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 6),
    _RlOspfNetLnkAge_Type()
)
rlOspfNetLnkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkAge.setStatus("current")
_RlOspfNetLnkChecksum_Type = Integer32
_RlOspfNetLnkChecksum_Object = MibTableColumn
rlOspfNetLnkChecksum = _RlOspfNetLnkChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 7),
    _RlOspfNetLnkChecksum_Type()
)
rlOspfNetLnkChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkChecksum.setStatus("current")
_RlOspfNetLnkLength_Type = Unsigned32
_RlOspfNetLnkLength_Object = MibTableColumn
rlOspfNetLnkLength = _RlOspfNetLnkLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 8),
    _RlOspfNetLnkLength_Type()
)
rlOspfNetLnkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkLength.setStatus("current")
_RlOspfNetLnkMask_Type = IpAddress
_RlOspfNetLnkMask_Object = MibTableColumn
rlOspfNetLnkMask = _RlOspfNetLnkMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 9),
    _RlOspfNetLnkMask_Type()
)
rlOspfNetLnkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkMask.setStatus("current")
_RlOspfNetLnkAttRouter_Type = IpAddress
_RlOspfNetLnkAttRouter_Object = MibTableColumn
rlOspfNetLnkAttRouter = _RlOspfNetLnkAttRouter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 5, 1, 10),
    _RlOspfNetLnkAttRouter_Type()
)
rlOspfNetLnkAttRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfNetLnkAttRouter.setStatus("current")
_RlOspfSumLnkTable_Object = MibTable
rlOspfSumLnkTable = _RlOspfSumLnkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6)
)
if mibBuilder.loadTexts:
    rlOspfSumLnkTable.setStatus("current")
_RlOspfSumLnkEntry_Object = MibTableRow
rlOspfSumLnkEntry = _RlOspfSumLnkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1)
)
rlOspfSumLnkEntry.setIndexNames(
    (0, "CISCOSB-IpRouter", "rlOspfSumLnkAreaId"),
    (0, "CISCOSB-IpRouter", "rlOspfSumLnkLsid"),
    (0, "CISCOSB-IpRouter", "rlOspfSumLnkRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfSumLnkEntry.setStatus("current")
_RlOspfSumLnkAreaId_Type = AreaID
_RlOspfSumLnkAreaId_Object = MibTableColumn
rlOspfSumLnkAreaId = _RlOspfSumLnkAreaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1, 1),
    _RlOspfSumLnkAreaId_Type()
)
rlOspfSumLnkAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSumLnkAreaId.setStatus("current")
_RlOspfSumLnkLsid_Type = IpAddress
_RlOspfSumLnkLsid_Object = MibTableColumn
rlOspfSumLnkLsid = _RlOspfSumLnkLsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1, 2),
    _RlOspfSumLnkLsid_Type()
)
rlOspfSumLnkLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSumLnkLsid.setStatus("current")
_RlOspfSumLnkRouterId_Type = RouterID
_RlOspfSumLnkRouterId_Object = MibTableColumn
rlOspfSumLnkRouterId = _RlOspfSumLnkRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1, 3),
    _RlOspfSumLnkRouterId_Type()
)
rlOspfSumLnkRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSumLnkRouterId.setStatus("current")
_RlOspfSumLnkSequence_Type = Integer32
_RlOspfSumLnkSequence_Object = MibTableColumn
rlOspfSumLnkSequence = _RlOspfSumLnkSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1, 4),
    _RlOspfSumLnkSequence_Type()
)
rlOspfSumLnkSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSumLnkSequence.setStatus("current")
_RlOspfSumLnkAge_Type = Integer32
_RlOspfSumLnkAge_Object = MibTableColumn
rlOspfSumLnkAge = _RlOspfSumLnkAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1, 5),
    _RlOspfSumLnkAge_Type()
)
rlOspfSumLnkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSumLnkAge.setStatus("current")
_RlOspfSumLnkChecksum_Type = Integer32
_RlOspfSumLnkChecksum_Object = MibTableColumn
rlOspfSumLnkChecksum = _RlOspfSumLnkChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1, 6),
    _RlOspfSumLnkChecksum_Type()
)
rlOspfSumLnkChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSumLnkChecksum.setStatus("current")
_RlOspfSumLnkLength_Type = Unsigned32
_RlOspfSumLnkLength_Object = MibTableColumn
rlOspfSumLnkLength = _RlOspfSumLnkLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1, 7),
    _RlOspfSumLnkLength_Type()
)
rlOspfSumLnkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSumLnkLength.setStatus("current")
_RlOspfSumLnkMask_Type = IpAddress
_RlOspfSumLnkMask_Object = MibTableColumn
rlOspfSumLnkMask = _RlOspfSumLnkMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1, 8),
    _RlOspfSumLnkMask_Type()
)
rlOspfSumLnkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSumLnkMask.setStatus("current")
_RlOspfSumLnkMetric_Type = Unsigned32
_RlOspfSumLnkMetric_Object = MibTableColumn
rlOspfSumLnkMetric = _RlOspfSumLnkMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 6, 1, 9),
    _RlOspfSumLnkMetric_Type()
)
rlOspfSumLnkMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfSumLnkMetric.setStatus("current")
_RlOspfAsbLnkTable_Object = MibTable
rlOspfAsbLnkTable = _RlOspfAsbLnkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7)
)
if mibBuilder.loadTexts:
    rlOspfAsbLnkTable.setStatus("current")
_RlOspfAsbLnkEntry_Object = MibTableRow
rlOspfAsbLnkEntry = _RlOspfAsbLnkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7, 1)
)
rlOspfAsbLnkEntry.setIndexNames(
    (0, "CISCOSB-IpRouter", "rlOspfAsbLnkAreaId"),
    (0, "CISCOSB-IpRouter", "rlOspfAsbLnkLsid"),
    (0, "CISCOSB-IpRouter", "rlOspfAsbLnkRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfAsbLnkEntry.setStatus("current")
_RlOspfAsbLnkAreaId_Type = AreaID
_RlOspfAsbLnkAreaId_Object = MibTableColumn
rlOspfAsbLnkAreaId = _RlOspfAsbLnkAreaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7, 1, 1),
    _RlOspfAsbLnkAreaId_Type()
)
rlOspfAsbLnkAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsbLnkAreaId.setStatus("current")
_RlOspfAsbLnkLsid_Type = IpAddress
_RlOspfAsbLnkLsid_Object = MibTableColumn
rlOspfAsbLnkLsid = _RlOspfAsbLnkLsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7, 1, 2),
    _RlOspfAsbLnkLsid_Type()
)
rlOspfAsbLnkLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsbLnkLsid.setStatus("current")
_RlOspfAsbLnkRouterId_Type = RouterID
_RlOspfAsbLnkRouterId_Object = MibTableColumn
rlOspfAsbLnkRouterId = _RlOspfAsbLnkRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7, 1, 3),
    _RlOspfAsbLnkRouterId_Type()
)
rlOspfAsbLnkRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsbLnkRouterId.setStatus("current")
_RlOspfAsbLnkSequence_Type = Integer32
_RlOspfAsbLnkSequence_Object = MibTableColumn
rlOspfAsbLnkSequence = _RlOspfAsbLnkSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7, 1, 4),
    _RlOspfAsbLnkSequence_Type()
)
rlOspfAsbLnkSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsbLnkSequence.setStatus("current")
_RlOspfAsbLnkAge_Type = Integer32
_RlOspfAsbLnkAge_Object = MibTableColumn
rlOspfAsbLnkAge = _RlOspfAsbLnkAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7, 1, 5),
    _RlOspfAsbLnkAge_Type()
)
rlOspfAsbLnkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsbLnkAge.setStatus("current")
_RlOspfAsbLnkChecksum_Type = Integer32
_RlOspfAsbLnkChecksum_Object = MibTableColumn
rlOspfAsbLnkChecksum = _RlOspfAsbLnkChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7, 1, 6),
    _RlOspfAsbLnkChecksum_Type()
)
rlOspfAsbLnkChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsbLnkChecksum.setStatus("current")
_RlOspfAsbLnkLength_Type = Unsigned32
_RlOspfAsbLnkLength_Object = MibTableColumn
rlOspfAsbLnkLength = _RlOspfAsbLnkLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7, 1, 7),
    _RlOspfAsbLnkLength_Type()
)
rlOspfAsbLnkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsbLnkLength.setStatus("current")
_RlOspfAsbLnkMetric_Type = Unsigned32
_RlOspfAsbLnkMetric_Object = MibTableColumn
rlOspfAsbLnkMetric = _RlOspfAsbLnkMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 7, 1, 8),
    _RlOspfAsbLnkMetric_Type()
)
rlOspfAsbLnkMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAsbLnkMetric.setStatus("current")
_RlOspfAseLnkTable_Object = MibTable
rlOspfAseLnkTable = _RlOspfAseLnkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8)
)
if mibBuilder.loadTexts:
    rlOspfAseLnkTable.setStatus("current")
_RlOspfAseLnkEntry_Object = MibTableRow
rlOspfAseLnkEntry = _RlOspfAseLnkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1)
)
rlOspfAseLnkEntry.setIndexNames(
    (0, "CISCOSB-IpRouter", "rlOspfAseLnkLsid"),
    (0, "CISCOSB-IpRouter", "rlOspfAseLnkRouterId"),
)
if mibBuilder.loadTexts:
    rlOspfAseLnkEntry.setStatus("current")
_RlOspfAseLnkLsid_Type = IpAddress
_RlOspfAseLnkLsid_Object = MibTableColumn
rlOspfAseLnkLsid = _RlOspfAseLnkLsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 1),
    _RlOspfAseLnkLsid_Type()
)
rlOspfAseLnkLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkLsid.setStatus("current")
_RlOspfAseLnkRouterId_Type = RouterID
_RlOspfAseLnkRouterId_Object = MibTableColumn
rlOspfAseLnkRouterId = _RlOspfAseLnkRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 2),
    _RlOspfAseLnkRouterId_Type()
)
rlOspfAseLnkRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkRouterId.setStatus("current")
_RlOspfAseLnkSequence_Type = Integer32
_RlOspfAseLnkSequence_Object = MibTableColumn
rlOspfAseLnkSequence = _RlOspfAseLnkSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 3),
    _RlOspfAseLnkSequence_Type()
)
rlOspfAseLnkSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkSequence.setStatus("current")
_RlOspfAseLnkAge_Type = Integer32
_RlOspfAseLnkAge_Object = MibTableColumn
rlOspfAseLnkAge = _RlOspfAseLnkAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 4),
    _RlOspfAseLnkAge_Type()
)
rlOspfAseLnkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkAge.setStatus("current")
_RlOspfAseLnkChecksum_Type = Integer32
_RlOspfAseLnkChecksum_Object = MibTableColumn
rlOspfAseLnkChecksum = _RlOspfAseLnkChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 5),
    _RlOspfAseLnkChecksum_Type()
)
rlOspfAseLnkChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkChecksum.setStatus("current")
_RlOspfAseLnkLength_Type = Unsigned32
_RlOspfAseLnkLength_Object = MibTableColumn
rlOspfAseLnkLength = _RlOspfAseLnkLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 6),
    _RlOspfAseLnkLength_Type()
)
rlOspfAseLnkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkLength.setStatus("current")
_RlOspfAseLnkMask_Type = IpAddress
_RlOspfAseLnkMask_Object = MibTableColumn
rlOspfAseLnkMask = _RlOspfAseLnkMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 7),
    _RlOspfAseLnkMask_Type()
)
rlOspfAseLnkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkMask.setStatus("current")
_RlOspfAseLnkFrwAddress_Type = IpAddress
_RlOspfAseLnkFrwAddress_Object = MibTableColumn
rlOspfAseLnkFrwAddress = _RlOspfAseLnkFrwAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 8),
    _RlOspfAseLnkFrwAddress_Type()
)
rlOspfAseLnkFrwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkFrwAddress.setStatus("current")


class _RlOspfAseLnkBitE_Type(Integer32):
    """Custom type rlOspfAseLnkBitE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RlOspfAseLnkBitE_Type.__name__ = "Integer32"
_RlOspfAseLnkBitE_Object = MibTableColumn
rlOspfAseLnkBitE = _RlOspfAseLnkBitE_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 9),
    _RlOspfAseLnkBitE_Type()
)
rlOspfAseLnkBitE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkBitE.setStatus("current")
_RlOspfAseLnkMetric_Type = Unsigned32
_RlOspfAseLnkMetric_Object = MibTableColumn
rlOspfAseLnkMetric = _RlOspfAseLnkMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 10),
    _RlOspfAseLnkMetric_Type()
)
rlOspfAseLnkMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkMetric.setStatus("current")
_RlOspfAseLnkTag_Type = Unsigned32
_RlOspfAseLnkTag_Object = MibTableColumn
rlOspfAseLnkTag = _RlOspfAseLnkTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 8, 1, 11),
    _RlOspfAseLnkTag_Type()
)
rlOspfAseLnkTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOspfAseLnkTag.setStatus("current")
_RlospfVirtIfExtTable_Object = MibTable
rlospfVirtIfExtTable = _RlospfVirtIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 9)
)
if mibBuilder.loadTexts:
    rlospfVirtIfExtTable.setStatus("current")
_RlospfVirtIfExtEntry_Object = MibTableRow
rlospfVirtIfExtEntry = _RlospfVirtIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 9, 1)
)
if mibBuilder.loadTexts:
    rlospfVirtIfExtEntry.setStatus("current")
_RlospfVirtifKeyChain_Type = DisplayString
_RlospfVirtifKeyChain_Object = MibTableColumn
rlospfVirtifKeyChain = _RlospfVirtifKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 14, 9, 1, 1),
    _RlospfVirtifKeyChain_Type()
)
rlospfVirtifKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlospfVirtifKeyChain.setStatus("current")
ospfIfEntry.registerAugmentions(
    ("CISCOSB-IpRouter",
     "rlOspfIfExtEntry")
)
rlOspfIfExtEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("CISCOSB-IpRouter",
     "rlospfVirtIfExtEntry")
)
rlospfVirtIfExtEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-IpRouter",
    **{"rsRip2IfConfTable": rsRip2IfConfTable,
       "rsRip2IfConfEntry": rsRip2IfConfEntry,
       "rsRip2IfConfAddress": rsRip2IfConfAddress,
       "rsRip2IfConfVirtualDis": rsRip2IfConfVirtualDis,
       "rlRip2IfConfKeyChain": rlRip2IfConfKeyChain,
       "rlRip2IfConfAdminStatus": rlRip2IfConfAdminStatus,
       "rlRip2IfConfInFilteringType": rlRip2IfConfInFilteringType,
       "rlRip2IfConfOutFilteringType": rlRip2IfConfOutFilteringType,
       "rlRip2IfConfInFilterListName": rlRip2IfConfInFilterListName,
       "rlRip2IfConfOutFilterListName": rlRip2IfConfOutFilterListName,
       "rlRip2IfConfDefInfOriginate": rlRip2IfConfDefInfOriginate,
       "rlRip2MibVersion": rlRip2MibVersion,
       "rlRip2RedistDefaultMetric": rlRip2RedistDefaultMetric,
       "rlRip2RedistStaticTransparent": rlRip2RedistStaticTransparent,
       "rlRip2ClearStatistics": rlRip2ClearStatistics,
       "rlRip2IfConfGlobalPassiveInterface": rlRip2IfConfGlobalPassiveInterface,
       "rlRip2GlobalDefInfOriginate": rlRip2GlobalDefInfOriginate,
       "rlRip2RedistConnected": rlRip2RedistConnected,
       "rlRip2RedistConnectedTransparent": rlRip2RedistConnectedTransparent,
       "rlRip2RedistConnectedMetric": rlRip2RedistConnectedMetric,
       "ipRedundAdminStatus": ipRedundAdminStatus,
       "ipRedundOperStatus": ipRedundOperStatus,
       "ipRedundRoutersTable": ipRedundRoutersTable,
       "ipRedundRoutersEntry": ipRedundRoutersEntry,
       "ipRedundRoutersIfAddr": ipRedundRoutersIfAddr,
       "ipRedundRoutersMainRouterAddr": ipRedundRoutersMainRouterAddr,
       "ipRedundRoutersOperStatus": ipRedundRoutersOperStatus,
       "ipRedundRoutersPollInterval": ipRedundRoutersPollInterval,
       "ipRedundRoutersTimeout": ipRedundRoutersTimeout,
       "ipRedundRoutersStatus": ipRedundRoutersStatus,
       "ipLeakStaticToRip": ipLeakStaticToRip,
       "ipLeakStaticToOspf": ipLeakStaticToOspf,
       "ipLeakOspfToRip": ipLeakOspfToRip,
       "ipLeakRipToOspf": ipLeakRipToOspf,
       "ipLeakExtDirectToOspf": ipLeakExtDirectToOspf,
       "rsIpRipFilterGlbTable": rsIpRipFilterGlbTable,
       "rsIpRipFilterGlbEntry": rsIpRipFilterGlbEntry,
       "rsIpRipFilterGlbType": rsIpRipFilterGlbType,
       "rsIpRipFilterGlbNumber": rsIpRipFilterGlbNumber,
       "rsIpRipFilterGlbStatus": rsIpRipFilterGlbStatus,
       "rsIpRipFilterGlbIpAddr": rsIpRipFilterGlbIpAddr,
       "rsIpRipFilterGlbNetworkMaskBits": rsIpRipFilterGlbNetworkMaskBits,
       "rsIpRipFilterGlbMatchBits": rsIpRipFilterGlbMatchBits,
       "rsIpRipFilterGlbAction": rsIpRipFilterGlbAction,
       "rsIpRipFilterLclTable": rsIpRipFilterLclTable,
       "rsIpRipFilterLclEntry": rsIpRipFilterLclEntry,
       "rsIpRipFilterLclIpIntf": rsIpRipFilterLclIpIntf,
       "rsIpRipFilterLclType": rsIpRipFilterLclType,
       "rsIpRipFilterLclNumber": rsIpRipFilterLclNumber,
       "rsIpRipFilterLclStatus": rsIpRipFilterLclStatus,
       "rsIpRipFilterLclIpAddr": rsIpRipFilterLclIpAddr,
       "rsIpRipFilterLclNetworkMaskBits": rsIpRipFilterLclNetworkMaskBits,
       "rsIpRipFilterLclMatchBits": rsIpRipFilterLclMatchBits,
       "rsIpRipFilterLclAction": rsIpRipFilterLclAction,
       "rlIpRoutingProtPreferenceDirect": rlIpRoutingProtPreferenceDirect,
       "rlIpRoutingProtPreferenceStatic": rlIpRoutingProtPreferenceStatic,
       "rlIpRoutingProtPreferenceOspfInter": rlIpRoutingProtPreferenceOspfInter,
       "rlIpRoutingProtPreferenceOspfExt": rlIpRoutingProtPreferenceOspfExt,
       "rlIpRoutingProtPreferenceOspfReject": rlIpRoutingProtPreferenceOspfReject,
       "rlIpRoutingProtPreferenceRipNormal": rlIpRoutingProtPreferenceRipNormal,
       "rlIpRoutingProtPreferenceRipAggregate": rlIpRoutingProtPreferenceRipAggregate,
       "rlIpRoutingProtPreferenceBgp": rlIpRoutingProtPreferenceBgp,
       "rlOspfMibVersion": rlOspfMibVersion,
       "rlOspfAutoInterfaceCreation": rlOspfAutoInterfaceCreation,
       "rlOspfIfExtTable": rlOspfIfExtTable,
       "rlOspfIfExtEntry": rlOspfIfExtEntry,
       "rlOspfifKeyChain": rlOspfifKeyChain,
       "rlOspfRtrLnkTable": rlOspfRtrLnkTable,
       "rlOspfRtrLnkEntry": rlOspfRtrLnkEntry,
       "rlOspfRtrLnkAreaId": rlOspfRtrLnkAreaId,
       "rlOspfRtrLnkLsid": rlOspfRtrLnkLsid,
       "rlOspfRtrLnkRouterId": rlOspfRtrLnkRouterId,
       "rlOspfRtrLnkIdx": rlOspfRtrLnkIdx,
       "rlOspfRtrLnkSequence": rlOspfRtrLnkSequence,
       "rlOspfRtrLnkAge": rlOspfRtrLnkAge,
       "rlOspfRtrLnkChecksum": rlOspfRtrLnkChecksum,
       "rlOspfRtrLnkLength": rlOspfRtrLnkLength,
       "rlOspfRtrLnkBitV": rlOspfRtrLnkBitV,
       "rlOspfRtrLnkBitE": rlOspfRtrLnkBitE,
       "rlOspfRtrLnkBitB": rlOspfRtrLnkBitB,
       "rlOspfRtrLnkLinks": rlOspfRtrLnkLinks,
       "rlOspfRtrLnkLinkID": rlOspfRtrLnkLinkID,
       "rlOspfRtrLnkLinkData": rlOspfRtrLnkLinkData,
       "rlOspfRtrLnkType": rlOspfRtrLnkType,
       "rlOspfRtrLnkMetric": rlOspfRtrLnkMetric,
       "rlOspfNetLnkTable": rlOspfNetLnkTable,
       "rlOspfNetLnkEntry": rlOspfNetLnkEntry,
       "rlOspfNetLnkAreaId": rlOspfNetLnkAreaId,
       "rlOspfNetLnkLsid": rlOspfNetLnkLsid,
       "rlOspfNetLnkRouterId": rlOspfNetLnkRouterId,
       "rlOspfNetLnkIdx": rlOspfNetLnkIdx,
       "rlOspfNetLnkSequence": rlOspfNetLnkSequence,
       "rlOspfNetLnkAge": rlOspfNetLnkAge,
       "rlOspfNetLnkChecksum": rlOspfNetLnkChecksum,
       "rlOspfNetLnkLength": rlOspfNetLnkLength,
       "rlOspfNetLnkMask": rlOspfNetLnkMask,
       "rlOspfNetLnkAttRouter": rlOspfNetLnkAttRouter,
       "rlOspfSumLnkTable": rlOspfSumLnkTable,
       "rlOspfSumLnkEntry": rlOspfSumLnkEntry,
       "rlOspfSumLnkAreaId": rlOspfSumLnkAreaId,
       "rlOspfSumLnkLsid": rlOspfSumLnkLsid,
       "rlOspfSumLnkRouterId": rlOspfSumLnkRouterId,
       "rlOspfSumLnkSequence": rlOspfSumLnkSequence,
       "rlOspfSumLnkAge": rlOspfSumLnkAge,
       "rlOspfSumLnkChecksum": rlOspfSumLnkChecksum,
       "rlOspfSumLnkLength": rlOspfSumLnkLength,
       "rlOspfSumLnkMask": rlOspfSumLnkMask,
       "rlOspfSumLnkMetric": rlOspfSumLnkMetric,
       "rlOspfAsbLnkTable": rlOspfAsbLnkTable,
       "rlOspfAsbLnkEntry": rlOspfAsbLnkEntry,
       "rlOspfAsbLnkAreaId": rlOspfAsbLnkAreaId,
       "rlOspfAsbLnkLsid": rlOspfAsbLnkLsid,
       "rlOspfAsbLnkRouterId": rlOspfAsbLnkRouterId,
       "rlOspfAsbLnkSequence": rlOspfAsbLnkSequence,
       "rlOspfAsbLnkAge": rlOspfAsbLnkAge,
       "rlOspfAsbLnkChecksum": rlOspfAsbLnkChecksum,
       "rlOspfAsbLnkLength": rlOspfAsbLnkLength,
       "rlOspfAsbLnkMetric": rlOspfAsbLnkMetric,
       "rlOspfAseLnkTable": rlOspfAseLnkTable,
       "rlOspfAseLnkEntry": rlOspfAseLnkEntry,
       "rlOspfAseLnkLsid": rlOspfAseLnkLsid,
       "rlOspfAseLnkRouterId": rlOspfAseLnkRouterId,
       "rlOspfAseLnkSequence": rlOspfAseLnkSequence,
       "rlOspfAseLnkAge": rlOspfAseLnkAge,
       "rlOspfAseLnkChecksum": rlOspfAseLnkChecksum,
       "rlOspfAseLnkLength": rlOspfAseLnkLength,
       "rlOspfAseLnkMask": rlOspfAseLnkMask,
       "rlOspfAseLnkFrwAddress": rlOspfAseLnkFrwAddress,
       "rlOspfAseLnkBitE": rlOspfAseLnkBitE,
       "rlOspfAseLnkMetric": rlOspfAseLnkMetric,
       "rlOspfAseLnkTag": rlOspfAseLnkTag,
       "rlospfVirtIfExtTable": rlospfVirtIfExtTable,
       "rlospfVirtIfExtEntry": rlospfVirtIfExtEntry,
       "rlospfVirtifKeyChain": rlospfVirtifKeyChain,
       "rlIpRouter": rlIpRouter}
)
