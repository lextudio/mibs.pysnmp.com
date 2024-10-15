# SNMP MIB module (HP-ICF-MLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-MLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:49 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(mldInterfaceEntry,) = mibBuilder.importSymbols(
    "IPV6-MLD-MIB",
    "mldInterfaceEntry")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfMldMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48)
)
hpicfMldMIB.setRevisions(
        ("2015-09-11 00:00",
         "2013-02-10 00:00",
         "2011-03-10 00:00",
         "2011-01-11 00:00",
         "2010-09-09 00:00",
         "2007-07-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfMcastGroupTypeDefinition(Integer32, TextualConvention):
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
        *(("filtered", 2),
          ("mini", 3),
          ("standard", 1))
    )



class HpicfMldIfEntryState(Integer32, TextualConvention):
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
        *(("initialWait", 1),
          ("nonQuerier", 4),
          ("querier", 3),
          ("querierElection", 2))
    )



class HpicfMldConfigPortModeType(Integer32, TextualConvention):
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
        *(("auto", 1),
          ("blocked", 2),
          ("forward", 3))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfMldObjects_ObjectIdentity = ObjectIdentity
hpicfMldObjects = _HpicfMldObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1)
)
_HpicfMld_ObjectIdentity = ObjectIdentity
hpicfMld = _HpicfMld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1)
)


class _HpicfMldControlUnknownMulticast_Type(TruthValue):
    """Custom type hpicfMldControlUnknownMulticast based on TruthValue"""


_HpicfMldControlUnknownMulticast_Object = MibScalar
hpicfMldControlUnknownMulticast = _HpicfMldControlUnknownMulticast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 1),
    _HpicfMldControlUnknownMulticast_Type()
)
hpicfMldControlUnknownMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldControlUnknownMulticast.setStatus("current")


class _HpicfMldConfigForcedLeaveInterval_Type(Integer32):
    """Custom type hpicfMldConfigForcedLeaveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfMldConfigForcedLeaveInterval_Type.__name__ = "Integer32"
_HpicfMldConfigForcedLeaveInterval_Object = MibScalar
hpicfMldConfigForcedLeaveInterval = _HpicfMldConfigForcedLeaveInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 2),
    _HpicfMldConfigForcedLeaveInterval_Type()
)
hpicfMldConfigForcedLeaveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldConfigForcedLeaveInterval.setStatus("current")
_HpicfMldEnabledCount_Type = Integer32
_HpicfMldEnabledCount_Object = MibScalar
hpicfMldEnabledCount = _HpicfMldEnabledCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 3),
    _HpicfMldEnabledCount_Type()
)
hpicfMldEnabledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldEnabledCount.setStatus("current")
_HpicfMldMcastGroupJoinsCount_Type = Integer32
_HpicfMldMcastGroupJoinsCount_Object = MibScalar
hpicfMldMcastGroupJoinsCount = _HpicfMldMcastGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 4),
    _HpicfMldMcastGroupJoinsCount_Type()
)
hpicfMldMcastGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldMcastGroupJoinsCount.setStatus("current")
_HpicfMldIfTable_Object = MibTable
hpicfMldIfTable = _HpicfMldIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfMldIfTable.setStatus("current")
_HpicfMldIfEntry_Object = MibTableRow
hpicfMldIfEntry = _HpicfMldIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfMldIfEntry.setStatus("current")


class _HpicfMldIfEntryQuerierFeature_Type(TruthValue):
    """Custom type hpicfMldIfEntryQuerierFeature based on TruthValue"""


_HpicfMldIfEntryQuerierFeature_Object = MibTableColumn
hpicfMldIfEntryQuerierFeature = _HpicfMldIfEntryQuerierFeature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 1),
    _HpicfMldIfEntryQuerierFeature_Type()
)
hpicfMldIfEntryQuerierFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldIfEntryQuerierFeature.setStatus("current")


class _HpicfMldIfEntrySnoopingFeature_Type(TruthValue):
    """Custom type hpicfMldIfEntrySnoopingFeature based on TruthValue"""


_HpicfMldIfEntrySnoopingFeature_Object = MibTableColumn
hpicfMldIfEntrySnoopingFeature = _HpicfMldIfEntrySnoopingFeature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 2),
    _HpicfMldIfEntrySnoopingFeature_Type()
)
hpicfMldIfEntrySnoopingFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldIfEntrySnoopingFeature.setStatus("current")
_HpicfMldIfEntryQuerierPort_Type = Integer32
_HpicfMldIfEntryQuerierPort_Object = MibTableColumn
hpicfMldIfEntryQuerierPort = _HpicfMldIfEntryQuerierPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 3),
    _HpicfMldIfEntryQuerierPort_Type()
)
hpicfMldIfEntryQuerierPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryQuerierPort.setStatus("current")
_HpicfMldIfEntryFilteredJoins_Type = Integer32
_HpicfMldIfEntryFilteredJoins_Object = MibTableColumn
hpicfMldIfEntryFilteredJoins = _HpicfMldIfEntryFilteredJoins_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 4),
    _HpicfMldIfEntryFilteredJoins_Type()
)
hpicfMldIfEntryFilteredJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryFilteredJoins.setStatus("current")
_HpicfMldIfEntryStandardJoins_Type = Integer32
_HpicfMldIfEntryStandardJoins_Object = MibTableColumn
hpicfMldIfEntryStandardJoins = _HpicfMldIfEntryStandardJoins_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 5),
    _HpicfMldIfEntryStandardJoins_Type()
)
hpicfMldIfEntryStandardJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStandardJoins.setStatus("current")
_HpicfMldIfEntryPortsWithMcastRouter_Type = PortList
_HpicfMldIfEntryPortsWithMcastRouter_Object = MibTableColumn
hpicfMldIfEntryPortsWithMcastRouter = _HpicfMldIfEntryPortsWithMcastRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 6),
    _HpicfMldIfEntryPortsWithMcastRouter_Type()
)
hpicfMldIfEntryPortsWithMcastRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryPortsWithMcastRouter.setStatus("current")
_HpicfMldIfEntryStatGeneralQueryRx_Type = Counter32
_HpicfMldIfEntryStatGeneralQueryRx_Object = MibTableColumn
hpicfMldIfEntryStatGeneralQueryRx = _HpicfMldIfEntryStatGeneralQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 7),
    _HpicfMldIfEntryStatGeneralQueryRx_Type()
)
hpicfMldIfEntryStatGeneralQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatGeneralQueryRx.setStatus("current")
_HpicfMldIfEntryStatQueryTx_Type = Counter32
_HpicfMldIfEntryStatQueryTx_Object = MibTableColumn
hpicfMldIfEntryStatQueryTx = _HpicfMldIfEntryStatQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 8),
    _HpicfMldIfEntryStatQueryTx_Type()
)
hpicfMldIfEntryStatQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatQueryTx.setStatus("current")
_HpicfMldIfEntryStatGSQRx_Type = Counter32
_HpicfMldIfEntryStatGSQRx_Object = MibTableColumn
hpicfMldIfEntryStatGSQRx = _HpicfMldIfEntryStatGSQRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 9),
    _HpicfMldIfEntryStatGSQRx_Type()
)
hpicfMldIfEntryStatGSQRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatGSQRx.setStatus("current")
_HpicfMldIfEntryStatGSQTx_Type = Counter32
_HpicfMldIfEntryStatGSQTx_Object = MibTableColumn
hpicfMldIfEntryStatGSQTx = _HpicfMldIfEntryStatGSQTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 10),
    _HpicfMldIfEntryStatGSQTx_Type()
)
hpicfMldIfEntryStatGSQTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatGSQTx.setStatus("current")
_HpicfMldIfEntryStatMldV1ReportRx_Type = Counter32
_HpicfMldIfEntryStatMldV1ReportRx_Object = MibTableColumn
hpicfMldIfEntryStatMldV1ReportRx = _HpicfMldIfEntryStatMldV1ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 11),
    _HpicfMldIfEntryStatMldV1ReportRx_Type()
)
hpicfMldIfEntryStatMldV1ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatMldV1ReportRx.setStatus("current")
_HpicfMldIfEntryStatMldV2ReportRx_Type = Counter32
_HpicfMldIfEntryStatMldV2ReportRx_Object = MibTableColumn
hpicfMldIfEntryStatMldV2ReportRx = _HpicfMldIfEntryStatMldV2ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 12),
    _HpicfMldIfEntryStatMldV2ReportRx_Type()
)
hpicfMldIfEntryStatMldV2ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatMldV2ReportRx.setStatus("current")
_HpicfMldIfEntryStatMldV1LeaveRx_Type = Counter32
_HpicfMldIfEntryStatMldV1LeaveRx_Object = MibTableColumn
hpicfMldIfEntryStatMldV1LeaveRx = _HpicfMldIfEntryStatMldV1LeaveRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 13),
    _HpicfMldIfEntryStatMldV1LeaveRx_Type()
)
hpicfMldIfEntryStatMldV1LeaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatMldV1LeaveRx.setStatus("current")
_HpicfMldIfEntryStatUnknownMldTypeRx_Type = Counter32
_HpicfMldIfEntryStatUnknownMldTypeRx_Object = MibTableColumn
hpicfMldIfEntryStatUnknownMldTypeRx = _HpicfMldIfEntryStatUnknownMldTypeRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 14),
    _HpicfMldIfEntryStatUnknownMldTypeRx_Type()
)
hpicfMldIfEntryStatUnknownMldTypeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatUnknownMldTypeRx.setStatus("current")
_HpicfMldIfEntryStatUnknownPktRx_Type = Counter32
_HpicfMldIfEntryStatUnknownPktRx_Object = MibTableColumn
hpicfMldIfEntryStatUnknownPktRx = _HpicfMldIfEntryStatUnknownPktRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 15),
    _HpicfMldIfEntryStatUnknownPktRx_Type()
)
hpicfMldIfEntryStatUnknownPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatUnknownPktRx.setStatus("current")
_HpicfMldIfEntryStatForwardToRoutersTx_Type = Counter32
_HpicfMldIfEntryStatForwardToRoutersTx_Object = MibTableColumn
hpicfMldIfEntryStatForwardToRoutersTx = _HpicfMldIfEntryStatForwardToRoutersTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 16),
    _HpicfMldIfEntryStatForwardToRoutersTx_Type()
)
hpicfMldIfEntryStatForwardToRoutersTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatForwardToRoutersTx.setStatus("current")
_HpicfMldIfEntryStatForwardToAllPortsTx_Type = Counter32
_HpicfMldIfEntryStatForwardToAllPortsTx_Object = MibTableColumn
hpicfMldIfEntryStatForwardToAllPortsTx = _HpicfMldIfEntryStatForwardToAllPortsTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 17),
    _HpicfMldIfEntryStatForwardToAllPortsTx_Type()
)
hpicfMldIfEntryStatForwardToAllPortsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatForwardToAllPortsTx.setStatus("current")
_HpicfMldIfEntryStatFastLeaves_Type = Counter32
_HpicfMldIfEntryStatFastLeaves_Object = MibTableColumn
hpicfMldIfEntryStatFastLeaves = _HpicfMldIfEntryStatFastLeaves_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 18),
    _HpicfMldIfEntryStatFastLeaves_Type()
)
hpicfMldIfEntryStatFastLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatFastLeaves.setStatus("current")
_HpicfMldIfEntryStatForcedFastLeaves_Type = Counter32
_HpicfMldIfEntryStatForcedFastLeaves_Object = MibTableColumn
hpicfMldIfEntryStatForcedFastLeaves = _HpicfMldIfEntryStatForcedFastLeaves_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 19),
    _HpicfMldIfEntryStatForcedFastLeaves_Type()
)
hpicfMldIfEntryStatForcedFastLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatForcedFastLeaves.setStatus("current")
_HpicfMldIfEntryStatJoinTimeouts_Type = Counter32
_HpicfMldIfEntryStatJoinTimeouts_Object = MibTableColumn
hpicfMldIfEntryStatJoinTimeouts = _HpicfMldIfEntryStatJoinTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 20),
    _HpicfMldIfEntryStatJoinTimeouts_Type()
)
hpicfMldIfEntryStatJoinTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatJoinTimeouts.setStatus("current")
_HpicfMldIfEntryStatWrongVersionQueries_Type = Counter32
_HpicfMldIfEntryStatWrongVersionQueries_Object = MibTableColumn
hpicfMldIfEntryStatWrongVersionQueries = _HpicfMldIfEntryStatWrongVersionQueries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 21),
    _HpicfMldIfEntryStatWrongVersionQueries_Type()
)
hpicfMldIfEntryStatWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatWrongVersionQueries.setStatus("current")
_HpicfMldIfEntryLastMemberQueryCount_Type = Counter32
_HpicfMldIfEntryLastMemberQueryCount_Object = MibTableColumn
hpicfMldIfEntryLastMemberQueryCount = _HpicfMldIfEntryLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 22),
    _HpicfMldIfEntryLastMemberQueryCount_Type()
)
hpicfMldIfEntryLastMemberQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryLastMemberQueryCount.setStatus("current")
_HpicfMldIfEntryStartupQueryCount_Type = Counter32
_HpicfMldIfEntryStartupQueryCount_Object = MibTableColumn
hpicfMldIfEntryStartupQueryCount = _HpicfMldIfEntryStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 23),
    _HpicfMldIfEntryStartupQueryCount_Type()
)
hpicfMldIfEntryStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStartupQueryCount.setStatus("current")
_HpicfMldIfEntryStartupQueryInterval_Type = Unsigned32
_HpicfMldIfEntryStartupQueryInterval_Object = MibTableColumn
hpicfMldIfEntryStartupQueryInterval = _HpicfMldIfEntryStartupQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 24),
    _HpicfMldIfEntryStartupQueryInterval_Type()
)
hpicfMldIfEntryStartupQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStartupQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStartupQueryInterval.setUnits("seconds")
_HpicfMldIfEntryStatExcludeGroupJoinsCount_Type = Counter32
_HpicfMldIfEntryStatExcludeGroupJoinsCount_Object = MibTableColumn
hpicfMldIfEntryStatExcludeGroupJoinsCount = _HpicfMldIfEntryStatExcludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 25),
    _HpicfMldIfEntryStatExcludeGroupJoinsCount_Type()
)
hpicfMldIfEntryStatExcludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatExcludeGroupJoinsCount.setStatus("current")
_HpicfMldIfEntryStatIncludeGroupJoinsCount_Type = Counter32
_HpicfMldIfEntryStatIncludeGroupJoinsCount_Object = MibTableColumn
hpicfMldIfEntryStatIncludeGroupJoinsCount = _HpicfMldIfEntryStatIncludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 26),
    _HpicfMldIfEntryStatIncludeGroupJoinsCount_Type()
)
hpicfMldIfEntryStatIncludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatIncludeGroupJoinsCount.setStatus("current")
_HpicfMldIfEntryStatFilteredExcludeGroupJoinsCount_Type = Counter32
_HpicfMldIfEntryStatFilteredExcludeGroupJoinsCount_Object = MibTableColumn
hpicfMldIfEntryStatFilteredExcludeGroupJoinsCount = _HpicfMldIfEntryStatFilteredExcludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 27),
    _HpicfMldIfEntryStatFilteredExcludeGroupJoinsCount_Type()
)
hpicfMldIfEntryStatFilteredExcludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatFilteredExcludeGroupJoinsCount.setStatus("current")
_HpicfMldIfEntryStatFilteredIncludeGroupJoinsCount_Type = Counter32
_HpicfMldIfEntryStatFilteredIncludeGroupJoinsCount_Object = MibTableColumn
hpicfMldIfEntryStatFilteredIncludeGroupJoinsCount = _HpicfMldIfEntryStatFilteredIncludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 28),
    _HpicfMldIfEntryStatFilteredIncludeGroupJoinsCount_Type()
)
hpicfMldIfEntryStatFilteredIncludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatFilteredIncludeGroupJoinsCount.setStatus("current")
_HpicfMldIfEntryStatStandardExcludeGroupJoinsCount_Type = Counter32
_HpicfMldIfEntryStatStandardExcludeGroupJoinsCount_Object = MibTableColumn
hpicfMldIfEntryStatStandardExcludeGroupJoinsCount = _HpicfMldIfEntryStatStandardExcludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 29),
    _HpicfMldIfEntryStatStandardExcludeGroupJoinsCount_Type()
)
hpicfMldIfEntryStatStandardExcludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatStandardExcludeGroupJoinsCount.setStatus("current")
_HpicfMldIfEntryStatStandardIncludeGroupJoinsCount_Type = Counter32
_HpicfMldIfEntryStatStandardIncludeGroupJoinsCount_Object = MibTableColumn
hpicfMldIfEntryStatStandardIncludeGroupJoinsCount = _HpicfMldIfEntryStatStandardIncludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 30),
    _HpicfMldIfEntryStatStandardIncludeGroupJoinsCount_Type()
)
hpicfMldIfEntryStatStandardIncludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatStandardIncludeGroupJoinsCount.setStatus("current")
_HpicfMldIfEntryStatV1QueryTx_Type = Counter32
_HpicfMldIfEntryStatV1QueryTx_Object = MibTableColumn
hpicfMldIfEntryStatV1QueryTx = _HpicfMldIfEntryStatV1QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 31),
    _HpicfMldIfEntryStatV1QueryTx_Type()
)
hpicfMldIfEntryStatV1QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatV1QueryTx.setStatus("current")
_HpicfMldIfEntryStatV1QueryRx_Type = Counter32
_HpicfMldIfEntryStatV1QueryRx_Object = MibTableColumn
hpicfMldIfEntryStatV1QueryRx = _HpicfMldIfEntryStatV1QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 32),
    _HpicfMldIfEntryStatV1QueryRx_Type()
)
hpicfMldIfEntryStatV1QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatV1QueryRx.setStatus("current")
_HpicfMldIfEntryStatV2QueryTx_Type = Counter32
_HpicfMldIfEntryStatV2QueryTx_Object = MibTableColumn
hpicfMldIfEntryStatV2QueryTx = _HpicfMldIfEntryStatV2QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 33),
    _HpicfMldIfEntryStatV2QueryTx_Type()
)
hpicfMldIfEntryStatV2QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatV2QueryTx.setStatus("current")
_HpicfMldIfEntryStatV2QueryRx_Type = Counter32
_HpicfMldIfEntryStatV2QueryRx_Object = MibTableColumn
hpicfMldIfEntryStatV2QueryRx = _HpicfMldIfEntryStatV2QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 34),
    _HpicfMldIfEntryStatV2QueryRx_Type()
)
hpicfMldIfEntryStatV2QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatV2QueryRx.setStatus("current")
_HpicfMldIfEntryStatGSSQTx_Type = Counter32
_HpicfMldIfEntryStatGSSQTx_Object = MibTableColumn
hpicfMldIfEntryStatGSSQTx = _HpicfMldIfEntryStatGSSQTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 35),
    _HpicfMldIfEntryStatGSSQTx_Type()
)
hpicfMldIfEntryStatGSSQTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatGSSQTx.setStatus("current")
_HpicfMldIfEntryStatGSSQRx_Type = Counter32
_HpicfMldIfEntryStatGSSQRx_Object = MibTableColumn
hpicfMldIfEntryStatGSSQRx = _HpicfMldIfEntryStatGSSQRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 36),
    _HpicfMldIfEntryStatGSSQRx_Type()
)
hpicfMldIfEntryStatGSSQRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatGSSQRx.setStatus("current")
_HpicfMldIfEntryStatMalformedPktRx_Type = Counter32
_HpicfMldIfEntryStatMalformedPktRx_Object = MibTableColumn
hpicfMldIfEntryStatMalformedPktRx = _HpicfMldIfEntryStatMalformedPktRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 37),
    _HpicfMldIfEntryStatMalformedPktRx_Type()
)
hpicfMldIfEntryStatMalformedPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatMalformedPktRx.setStatus("current")
_HpicfMldIfEntryStatBadCheckSumRx_Type = Counter32
_HpicfMldIfEntryStatBadCheckSumRx_Object = MibTableColumn
hpicfMldIfEntryStatBadCheckSumRx = _HpicfMldIfEntryStatBadCheckSumRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 38),
    _HpicfMldIfEntryStatBadCheckSumRx_Type()
)
hpicfMldIfEntryStatBadCheckSumRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatBadCheckSumRx.setStatus("current")
_HpicfMldIfEntryStatMartianSourceRx_Type = Counter32
_HpicfMldIfEntryStatMartianSourceRx_Object = MibTableColumn
hpicfMldIfEntryStatMartianSourceRx = _HpicfMldIfEntryStatMartianSourceRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 39),
    _HpicfMldIfEntryStatMartianSourceRx_Type()
)
hpicfMldIfEntryStatMartianSourceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatMartianSourceRx.setStatus("current")
_HpicfMldIfEntryStatPacketsRxOnDisabled_Type = Counter32
_HpicfMldIfEntryStatPacketsRxOnDisabled_Object = MibTableColumn
hpicfMldIfEntryStatPacketsRxOnDisabled = _HpicfMldIfEntryStatPacketsRxOnDisabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 40),
    _HpicfMldIfEntryStatPacketsRxOnDisabled_Type()
)
hpicfMldIfEntryStatPacketsRxOnDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatPacketsRxOnDisabled.setStatus("current")


class _HpicfMldIfEntryStrictVersionMode_Type(TruthValue):
    """Custom type hpicfMldIfEntryStrictVersionMode based on TruthValue"""


_HpicfMldIfEntryStrictVersionMode_Object = MibTableColumn
hpicfMldIfEntryStrictVersionMode = _HpicfMldIfEntryStrictVersionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 41),
    _HpicfMldIfEntryStrictVersionMode_Type()
)
hpicfMldIfEntryStrictVersionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStrictVersionMode.setStatus("current")
_HpicfMldIfEntryStatMldV1ReportTx_Type = Counter32
_HpicfMldIfEntryStatMldV1ReportTx_Object = MibTableColumn
hpicfMldIfEntryStatMldV1ReportTx = _HpicfMldIfEntryStatMldV1ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 42),
    _HpicfMldIfEntryStatMldV1ReportTx_Type()
)
hpicfMldIfEntryStatMldV1ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatMldV1ReportTx.setStatus("current")
_HpicfMldIfEntryStatMldV2ReportTx_Type = Counter32
_HpicfMldIfEntryStatMldV2ReportTx_Object = MibTableColumn
hpicfMldIfEntryStatMldV2ReportTx = _HpicfMldIfEntryStatMldV2ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 43),
    _HpicfMldIfEntryStatMldV2ReportTx_Type()
)
hpicfMldIfEntryStatMldV2ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatMldV2ReportTx.setStatus("current")
_HpicfMldIfEntryState_Type = HpicfMldIfEntryState
_HpicfMldIfEntryState_Object = MibTableColumn
hpicfMldIfEntryState = _HpicfMldIfEntryState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 44),
    _HpicfMldIfEntryState_Type()
)
hpicfMldIfEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryState.setStatus("current")
_HpicfMldIfEntryStatV1GSQRx_Type = Counter32
_HpicfMldIfEntryStatV1GSQRx_Object = MibTableColumn
hpicfMldIfEntryStatV1GSQRx = _HpicfMldIfEntryStatV1GSQRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 45),
    _HpicfMldIfEntryStatV1GSQRx_Type()
)
hpicfMldIfEntryStatV1GSQRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatV1GSQRx.setStatus("current")
_HpicfMldIfEntryStatV1GSQTx_Type = Counter32
_HpicfMldIfEntryStatV1GSQTx_Object = MibTableColumn
hpicfMldIfEntryStatV1GSQTx = _HpicfMldIfEntryStatV1GSQTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 46),
    _HpicfMldIfEntryStatV1GSQTx_Type()
)
hpicfMldIfEntryStatV1GSQTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatV1GSQTx.setStatus("current")
_HpicfMldIfEntryStatV2GSQRx_Type = Counter32
_HpicfMldIfEntryStatV2GSQRx_Object = MibTableColumn
hpicfMldIfEntryStatV2GSQRx = _HpicfMldIfEntryStatV2GSQRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 47),
    _HpicfMldIfEntryStatV2GSQRx_Type()
)
hpicfMldIfEntryStatV2GSQRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatV2GSQRx.setStatus("current")
_HpicfMldIfEntryStatV2GSQTx_Type = Counter32
_HpicfMldIfEntryStatV2GSQTx_Object = MibTableColumn
hpicfMldIfEntryStatV2GSQTx = _HpicfMldIfEntryStatV2GSQTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 48),
    _HpicfMldIfEntryStatV2GSQTx_Type()
)
hpicfMldIfEntryStatV2GSQTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStatV2GSQTx.setStatus("current")
_HpicfMldIfEntryStartupQueryExpiryTime_Type = TimeTicks
_HpicfMldIfEntryStartupQueryExpiryTime_Object = MibTableColumn
hpicfMldIfEntryStartupQueryExpiryTime = _HpicfMldIfEntryStartupQueryExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 49),
    _HpicfMldIfEntryStartupQueryExpiryTime_Type()
)
hpicfMldIfEntryStartupQueryExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryStartupQueryExpiryTime.setStatus("current")
_HpicfMldIfEntryOtherQuerierInterval_Type = Unsigned32
_HpicfMldIfEntryOtherQuerierInterval_Object = MibTableColumn
hpicfMldIfEntryOtherQuerierInterval = _HpicfMldIfEntryOtherQuerierInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 50),
    _HpicfMldIfEntryOtherQuerierInterval_Type()
)
hpicfMldIfEntryOtherQuerierInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryOtherQuerierInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfMldIfEntryOtherQuerierInterval.setUnits("seconds")
_HpicfMldIfEntryOtherQuerierExpiryTime_Type = TimeTicks
_HpicfMldIfEntryOtherQuerierExpiryTime_Object = MibTableColumn
hpicfMldIfEntryOtherQuerierExpiryTime = _HpicfMldIfEntryOtherQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 5, 1, 51),
    _HpicfMldIfEntryOtherQuerierExpiryTime_Type()
)
hpicfMldIfEntryOtherQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldIfEntryOtherQuerierExpiryTime.setStatus("current")
_HpicfMldCacheTable_Object = MibTable
hpicfMldCacheTable = _HpicfMldCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfMldCacheTable.setStatus("current")
_HpicfMldCacheEntry_Object = MibTableRow
hpicfMldCacheEntry = _HpicfMldCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1)
)
hpicfMldCacheEntry.setIndexNames(
    (0, "HP-ICF-MLD-MIB", "hpicfMldCacheIfIndex"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldCacheAddress"),
)
if mibBuilder.loadTexts:
    hpicfMldCacheEntry.setStatus("current")
_HpicfMldCacheIfIndex_Type = InterfaceIndex
_HpicfMldCacheIfIndex_Object = MibTableColumn
hpicfMldCacheIfIndex = _HpicfMldCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 1),
    _HpicfMldCacheIfIndex_Type()
)
hpicfMldCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldCacheIfIndex.setStatus("current")


class _HpicfMldCacheAddress_Type(InetAddressIPv6):
    """Custom type hpicfMldCacheAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpicfMldCacheAddress_Type.__name__ = "InetAddressIPv6"
_HpicfMldCacheAddress_Object = MibTableColumn
hpicfMldCacheAddress = _HpicfMldCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 2),
    _HpicfMldCacheAddress_Type()
)
hpicfMldCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldCacheAddress.setStatus("current")


class _HpicfMldCacheSelf_Type(TruthValue):
    """Custom type hpicfMldCacheSelf based on TruthValue"""


_HpicfMldCacheSelf_Object = MibTableColumn
hpicfMldCacheSelf = _HpicfMldCacheSelf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 3),
    _HpicfMldCacheSelf_Type()
)
hpicfMldCacheSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMldCacheSelf.setStatus("current")


class _HpicfMldCacheLastReporter_Type(InetAddressIPv6):
    """Custom type hpicfMldCacheLastReporter based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpicfMldCacheLastReporter_Type.__name__ = "InetAddressIPv6"
_HpicfMldCacheLastReporter_Object = MibTableColumn
hpicfMldCacheLastReporter = _HpicfMldCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 4),
    _HpicfMldCacheLastReporter_Type()
)
hpicfMldCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldCacheLastReporter.setStatus("current")
_HpicfMldCacheUpTime_Type = TimeTicks
_HpicfMldCacheUpTime_Object = MibTableColumn
hpicfMldCacheUpTime = _HpicfMldCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 5),
    _HpicfMldCacheUpTime_Type()
)
hpicfMldCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldCacheUpTime.setStatus("current")
_HpicfMldCacheExpiryTime_Type = TimeTicks
_HpicfMldCacheExpiryTime_Object = MibTableColumn
hpicfMldCacheExpiryTime = _HpicfMldCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 6),
    _HpicfMldCacheExpiryTime_Type()
)
hpicfMldCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldCacheExpiryTime.setStatus("current")
_HpicfMldGroupType_Type = HpicfMcastGroupTypeDefinition
_HpicfMldGroupType_Object = MibTableColumn
hpicfMldGroupType = _HpicfMldGroupType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 7),
    _HpicfMldGroupType_Type()
)
hpicfMldGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldGroupType.setStatus("current")
_HpicfJoinedPorts_Type = PortList
_HpicfJoinedPorts_Object = MibTableColumn
hpicfJoinedPorts = _HpicfJoinedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 8),
    _HpicfJoinedPorts_Type()
)
hpicfJoinedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfJoinedPorts.setStatus("current")
_HpicfMldCacheStatus_Type = RowStatus
_HpicfMldCacheStatus_Object = MibTableColumn
hpicfMldCacheStatus = _HpicfMldCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 9),
    _HpicfMldCacheStatus_Type()
)
hpicfMldCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMldCacheStatus.setStatus("current")


class _HpicfMldCacheFilterMode_Type(Integer32):
    """Custom type hpicfMldCacheFilterMode based on Integer32"""
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


_HpicfMldCacheFilterMode_Type.__name__ = "Integer32"
_HpicfMldCacheFilterMode_Object = MibTableColumn
hpicfMldCacheFilterMode = _HpicfMldCacheFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 10),
    _HpicfMldCacheFilterMode_Type()
)
hpicfMldCacheFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldCacheFilterMode.setStatus("current")
_HpicfMldCacheExcludeModeExpiryTimer_Type = TimeTicks
_HpicfMldCacheExcludeModeExpiryTimer_Object = MibTableColumn
hpicfMldCacheExcludeModeExpiryTimer = _HpicfMldCacheExcludeModeExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 11),
    _HpicfMldCacheExcludeModeExpiryTimer_Type()
)
hpicfMldCacheExcludeModeExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldCacheExcludeModeExpiryTimer.setStatus("current")
_HpicfMldCacheVersion1HostTimer_Type = TimeTicks
_HpicfMldCacheVersion1HostTimer_Object = MibTableColumn
hpicfMldCacheVersion1HostTimer = _HpicfMldCacheVersion1HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 12),
    _HpicfMldCacheVersion1HostTimer_Type()
)
hpicfMldCacheVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldCacheVersion1HostTimer.setStatus("current")
_HpicfMldCacheSrcCount_Type = Counter32
_HpicfMldCacheSrcCount_Object = MibTableColumn
hpicfMldCacheSrcCount = _HpicfMldCacheSrcCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 6, 1, 13),
    _HpicfMldCacheSrcCount_Type()
)
hpicfMldCacheSrcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldCacheSrcCount.setStatus("current")
_HpicfMldPortConfigTable_Object = MibTable
hpicfMldPortConfigTable = _HpicfMldPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfMldPortConfigTable.setStatus("current")
_HpicfMldPortConfigEntry_Object = MibTableRow
hpicfMldPortConfigEntry = _HpicfMldPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 7, 1)
)
hpicfMldPortConfigEntry.setIndexNames(
    (0, "HP-ICF-MLD-MIB", "hpicfMldPortConfigEntryInterfaceIfIndex"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldPortConfigEntryIndex"),
)
if mibBuilder.loadTexts:
    hpicfMldPortConfigEntry.setStatus("current")
_HpicfMldPortConfigEntryInterfaceIfIndex_Type = InterfaceIndex
_HpicfMldPortConfigEntryInterfaceIfIndex_Object = MibTableColumn
hpicfMldPortConfigEntryInterfaceIfIndex = _HpicfMldPortConfigEntryInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 7, 1, 1),
    _HpicfMldPortConfigEntryInterfaceIfIndex_Type()
)
hpicfMldPortConfigEntryInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldPortConfigEntryInterfaceIfIndex.setStatus("current")


class _HpicfMldPortConfigEntryIndex_Type(Integer32):
    """Custom type hpicfMldPortConfigEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfMldPortConfigEntryIndex_Type.__name__ = "Integer32"
_HpicfMldPortConfigEntryIndex_Object = MibTableColumn
hpicfMldPortConfigEntryIndex = _HpicfMldPortConfigEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 7, 1, 2),
    _HpicfMldPortConfigEntryIndex_Type()
)
hpicfMldPortConfigEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldPortConfigEntryIndex.setStatus("current")
_HpicfMldPortConfigEntryPortModeFeature_Type = HpicfMldConfigPortModeType
_HpicfMldPortConfigEntryPortModeFeature_Object = MibTableColumn
hpicfMldPortConfigEntryPortModeFeature = _HpicfMldPortConfigEntryPortModeFeature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 7, 1, 3),
    _HpicfMldPortConfigEntryPortModeFeature_Type()
)
hpicfMldPortConfigEntryPortModeFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldPortConfigEntryPortModeFeature.setStatus("current")
_HpicfMldPortConfigEntryForcedLeaveFeature_Type = TruthValue
_HpicfMldPortConfigEntryForcedLeaveFeature_Object = MibTableColumn
hpicfMldPortConfigEntryForcedLeaveFeature = _HpicfMldPortConfigEntryForcedLeaveFeature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 7, 1, 4),
    _HpicfMldPortConfigEntryForcedLeaveFeature_Type()
)
hpicfMldPortConfigEntryForcedLeaveFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldPortConfigEntryForcedLeaveFeature.setStatus("current")
_HpicfMldPortConfigEntryFastLeaveFeature_Type = TruthValue
_HpicfMldPortConfigEntryFastLeaveFeature_Object = MibTableColumn
hpicfMldPortConfigEntryFastLeaveFeature = _HpicfMldPortConfigEntryFastLeaveFeature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 7, 1, 5),
    _HpicfMldPortConfigEntryFastLeaveFeature_Type()
)
hpicfMldPortConfigEntryFastLeaveFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldPortConfigEntryFastLeaveFeature.setStatus("current")
_HpicfMldFilteredGroupPortCacheTable_Object = MibTable
hpicfMldFilteredGroupPortCacheTable = _HpicfMldFilteredGroupPortCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfMldFilteredGroupPortCacheTable.setStatus("current")
_HpicfMldFilteredGroupPortCacheEntry_Object = MibTableRow
hpicfMldFilteredGroupPortCacheEntry = _HpicfMldFilteredGroupPortCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 8, 1)
)
hpicfMldFilteredGroupPortCacheEntry.setIndexNames(
    (0, "HP-ICF-MLD-MIB", "hpicfMldFilteredGroupPortCacheIfIndex"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldFilteredGroupPortCacheGroupAddress"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldFilteredGroupPortCachePortIndex"),
)
if mibBuilder.loadTexts:
    hpicfMldFilteredGroupPortCacheEntry.setStatus("current")
_HpicfMldFilteredGroupPortCacheIfIndex_Type = InterfaceIndex
_HpicfMldFilteredGroupPortCacheIfIndex_Object = MibTableColumn
hpicfMldFilteredGroupPortCacheIfIndex = _HpicfMldFilteredGroupPortCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 8, 1, 1),
    _HpicfMldFilteredGroupPortCacheIfIndex_Type()
)
hpicfMldFilteredGroupPortCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldFilteredGroupPortCacheIfIndex.setStatus("current")
_HpicfMldFilteredGroupPortCacheGroupAddress_Type = InetAddressIPv6
_HpicfMldFilteredGroupPortCacheGroupAddress_Object = MibTableColumn
hpicfMldFilteredGroupPortCacheGroupAddress = _HpicfMldFilteredGroupPortCacheGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 8, 1, 2),
    _HpicfMldFilteredGroupPortCacheGroupAddress_Type()
)
hpicfMldFilteredGroupPortCacheGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldFilteredGroupPortCacheGroupAddress.setStatus("current")


class _HpicfMldFilteredGroupPortCachePortIndex_Type(Integer32):
    """Custom type hpicfMldFilteredGroupPortCachePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfMldFilteredGroupPortCachePortIndex_Type.__name__ = "Integer32"
_HpicfMldFilteredGroupPortCachePortIndex_Object = MibTableColumn
hpicfMldFilteredGroupPortCachePortIndex = _HpicfMldFilteredGroupPortCachePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 8, 1, 3),
    _HpicfMldFilteredGroupPortCachePortIndex_Type()
)
hpicfMldFilteredGroupPortCachePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldFilteredGroupPortCachePortIndex.setStatus("current")
_HpicfMldFilteredGroupPortCacheExpiryTime_Type = TimeTicks
_HpicfMldFilteredGroupPortCacheExpiryTime_Object = MibTableColumn
hpicfMldFilteredGroupPortCacheExpiryTime = _HpicfMldFilteredGroupPortCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 8, 1, 4),
    _HpicfMldFilteredGroupPortCacheExpiryTime_Type()
)
hpicfMldFilteredGroupPortCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldFilteredGroupPortCacheExpiryTime.setStatus("current")
_HpicfMldSrcListTable_Object = MibTable
hpicfMldSrcListTable = _HpicfMldSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfMldSrcListTable.setStatus("current")
_HpicfMldSrcListEntry_Object = MibTableRow
hpicfMldSrcListEntry = _HpicfMldSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 9, 1)
)
hpicfMldSrcListEntry.setIndexNames(
    (0, "HP-ICF-MLD-MIB", "hpicfMldSrcListIfIndex"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldSrcListAddress"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    hpicfMldSrcListEntry.setStatus("current")
_HpicfMldSrcListIfIndex_Type = InterfaceIndex
_HpicfMldSrcListIfIndex_Object = MibTableColumn
hpicfMldSrcListIfIndex = _HpicfMldSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 9, 1, 1),
    _HpicfMldSrcListIfIndex_Type()
)
hpicfMldSrcListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldSrcListIfIndex.setStatus("current")


class _HpicfMldSrcListAddress_Type(InetAddressIPv6):
    """Custom type hpicfMldSrcListAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpicfMldSrcListAddress_Type.__name__ = "InetAddressIPv6"
_HpicfMldSrcListAddress_Object = MibTableColumn
hpicfMldSrcListAddress = _HpicfMldSrcListAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 9, 1, 2),
    _HpicfMldSrcListAddress_Type()
)
hpicfMldSrcListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldSrcListAddress.setStatus("current")


class _HpicfMldSrcListHostAddress_Type(InetAddressIPv6):
    """Custom type hpicfMldSrcListHostAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpicfMldSrcListHostAddress_Type.__name__ = "InetAddressIPv6"
_HpicfMldSrcListHostAddress_Object = MibTableColumn
hpicfMldSrcListHostAddress = _HpicfMldSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 9, 1, 3),
    _HpicfMldSrcListHostAddress_Type()
)
hpicfMldSrcListHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldSrcListHostAddress.setStatus("current")
_HpicfMldSrcListPorts_Type = PortList
_HpicfMldSrcListPorts_Object = MibTableColumn
hpicfMldSrcListPorts = _HpicfMldSrcListPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 9, 1, 4),
    _HpicfMldSrcListPorts_Type()
)
hpicfMldSrcListPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldSrcListPorts.setStatus("current")
_HpicfMldSrcListExpiry_Type = TimeTicks
_HpicfMldSrcListExpiry_Object = MibTableColumn
hpicfMldSrcListExpiry = _HpicfMldSrcListExpiry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 9, 1, 5),
    _HpicfMldSrcListExpiry_Type()
)
hpicfMldSrcListExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldSrcListExpiry.setStatus("current")
_HpicfMldSrcListUpTime_Type = TimeTicks
_HpicfMldSrcListUpTime_Object = MibTableColumn
hpicfMldSrcListUpTime = _HpicfMldSrcListUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 9, 1, 6),
    _HpicfMldSrcListUpTime_Type()
)
hpicfMldSrcListUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldSrcListUpTime.setStatus("current")
_HpicfMldSrcListType_Type = HpicfMcastGroupTypeDefinition
_HpicfMldSrcListType_Object = MibTableColumn
hpicfMldSrcListType = _HpicfMldSrcListType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 9, 1, 7),
    _HpicfMldSrcListType_Type()
)
hpicfMldSrcListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldSrcListType.setStatus("current")
_HpicfMldPortSrcTable_Object = MibTable
hpicfMldPortSrcTable = _HpicfMldPortSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hpicfMldPortSrcTable.setStatus("current")
_HpicfMldPortSrcEntry_Object = MibTableRow
hpicfMldPortSrcEntry = _HpicfMldPortSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 10, 1)
)
hpicfMldPortSrcEntry.setIndexNames(
    (0, "HP-ICF-MLD-MIB", "hpicfMldPortSrcIfIndex"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldPortSrcAddress"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldPortSrcHostAddress"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldPortSrcPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfMldPortSrcEntry.setStatus("current")
_HpicfMldPortSrcIfIndex_Type = InterfaceIndex
_HpicfMldPortSrcIfIndex_Object = MibTableColumn
hpicfMldPortSrcIfIndex = _HpicfMldPortSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 10, 1, 1),
    _HpicfMldPortSrcIfIndex_Type()
)
hpicfMldPortSrcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldPortSrcIfIndex.setStatus("current")


class _HpicfMldPortSrcAddress_Type(InetAddressIPv6):
    """Custom type hpicfMldPortSrcAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpicfMldPortSrcAddress_Type.__name__ = "InetAddressIPv6"
_HpicfMldPortSrcAddress_Object = MibTableColumn
hpicfMldPortSrcAddress = _HpicfMldPortSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 10, 1, 2),
    _HpicfMldPortSrcAddress_Type()
)
hpicfMldPortSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldPortSrcAddress.setStatus("current")


class _HpicfMldPortSrcHostAddress_Type(InetAddressIPv6):
    """Custom type hpicfMldPortSrcHostAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HpicfMldPortSrcHostAddress_Type.__name__ = "InetAddressIPv6"
_HpicfMldPortSrcHostAddress_Object = MibTableColumn
hpicfMldPortSrcHostAddress = _HpicfMldPortSrcHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 10, 1, 3),
    _HpicfMldPortSrcHostAddress_Type()
)
hpicfMldPortSrcHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldPortSrcHostAddress.setStatus("current")


class _HpicfMldPortSrcPortIndex_Type(Integer32):
    """Custom type hpicfMldPortSrcPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfMldPortSrcPortIndex_Type.__name__ = "Integer32"
_HpicfMldPortSrcPortIndex_Object = MibTableColumn
hpicfMldPortSrcPortIndex = _HpicfMldPortSrcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 10, 1, 4),
    _HpicfMldPortSrcPortIndex_Type()
)
hpicfMldPortSrcPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldPortSrcPortIndex.setStatus("current")
_HpicfMldPortSrcExpiry_Type = TimeTicks
_HpicfMldPortSrcExpiry_Object = MibTableColumn
hpicfMldPortSrcExpiry = _HpicfMldPortSrcExpiry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 10, 1, 5),
    _HpicfMldPortSrcExpiry_Type()
)
hpicfMldPortSrcExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldPortSrcExpiry.setStatus("current")
_HpicfMldPortSrcUpTime_Type = TimeTicks
_HpicfMldPortSrcUpTime_Object = MibTableColumn
hpicfMldPortSrcUpTime = _HpicfMldPortSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 10, 1, 6),
    _HpicfMldPortSrcUpTime_Type()
)
hpicfMldPortSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldPortSrcUpTime.setStatus("current")


class _HpicfMldPortSrcFilterMode_Type(Integer32):
    """Custom type hpicfMldPortSrcFilterMode based on Integer32"""
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


_HpicfMldPortSrcFilterMode_Type.__name__ = "Integer32"
_HpicfMldPortSrcFilterMode_Object = MibTableColumn
hpicfMldPortSrcFilterMode = _HpicfMldPortSrcFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 10, 1, 7),
    _HpicfMldPortSrcFilterMode_Type()
)
hpicfMldPortSrcFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldPortSrcFilterMode.setStatus("current")
_HpicfMldMcastExcludeGroupJoinsCount_Type = Integer32
_HpicfMldMcastExcludeGroupJoinsCount_Object = MibScalar
hpicfMldMcastExcludeGroupJoinsCount = _HpicfMldMcastExcludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 11),
    _HpicfMldMcastExcludeGroupJoinsCount_Type()
)
hpicfMldMcastExcludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldMcastExcludeGroupJoinsCount.setStatus("current")
_HpicfMldMcastIncludeGroupJoinsCount_Type = Integer32
_HpicfMldMcastIncludeGroupJoinsCount_Object = MibScalar
hpicfMldMcastIncludeGroupJoinsCount = _HpicfMldMcastIncludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 12),
    _HpicfMldMcastIncludeGroupJoinsCount_Type()
)
hpicfMldMcastIncludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldMcastIncludeGroupJoinsCount.setStatus("current")
_HpicfMldMcastPortFastLearn_Type = PortList
_HpicfMldMcastPortFastLearn_Object = MibScalar
hpicfMldMcastPortFastLearn = _HpicfMldMcastPortFastLearn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 13),
    _HpicfMldMcastPortFastLearn_Type()
)
hpicfMldMcastPortFastLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldMcastPortFastLearn.setStatus("current")
_HpicfMldGroupPortCacheTable_Object = MibTable
hpicfMldGroupPortCacheTable = _HpicfMldGroupPortCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheTable.setStatus("current")
_HpicfMldGroupPortCacheEntry_Object = MibTableRow
hpicfMldGroupPortCacheEntry = _HpicfMldGroupPortCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1)
)
hpicfMldGroupPortCacheEntry.setIndexNames(
    (0, "HP-ICF-MLD-MIB", "hpicfMldGroupPortCacheIfIndex"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldGroupPortCacheGroupAddress"),
    (0, "HP-ICF-MLD-MIB", "hpicfMldGroupPortCachePortIndex"),
)
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheEntry.setStatus("current")
_HpicfMldGroupPortCacheIfIndex_Type = InterfaceIndex
_HpicfMldGroupPortCacheIfIndex_Object = MibTableColumn
hpicfMldGroupPortCacheIfIndex = _HpicfMldGroupPortCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 1),
    _HpicfMldGroupPortCacheIfIndex_Type()
)
hpicfMldGroupPortCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheIfIndex.setStatus("current")
_HpicfMldGroupPortCacheGroupAddress_Type = InetAddressIPv6
_HpicfMldGroupPortCacheGroupAddress_Object = MibTableColumn
hpicfMldGroupPortCacheGroupAddress = _HpicfMldGroupPortCacheGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 2),
    _HpicfMldGroupPortCacheGroupAddress_Type()
)
hpicfMldGroupPortCacheGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheGroupAddress.setStatus("current")


class _HpicfMldGroupPortCachePortIndex_Type(Integer32):
    """Custom type hpicfMldGroupPortCachePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfMldGroupPortCachePortIndex_Type.__name__ = "Integer32"
_HpicfMldGroupPortCachePortIndex_Object = MibTableColumn
hpicfMldGroupPortCachePortIndex = _HpicfMldGroupPortCachePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 3),
    _HpicfMldGroupPortCachePortIndex_Type()
)
hpicfMldGroupPortCachePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCachePortIndex.setStatus("current")
_HpicfMldGroupPortCacheExpiryTime_Type = TimeTicks
_HpicfMldGroupPortCacheExpiryTime_Object = MibTableColumn
hpicfMldGroupPortCacheExpiryTime = _HpicfMldGroupPortCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 4),
    _HpicfMldGroupPortCacheExpiryTime_Type()
)
hpicfMldGroupPortCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheExpiryTime.setStatus("current")
_HpicfMldGroupPortCacheUpTime_Type = TimeTicks
_HpicfMldGroupPortCacheUpTime_Object = MibTableColumn
hpicfMldGroupPortCacheUpTime = _HpicfMldGroupPortCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 5),
    _HpicfMldGroupPortCacheUpTime_Type()
)
hpicfMldGroupPortCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheUpTime.setStatus("current")
_HpicfMldGroupPortCacheVersion1Timer_Type = TimeTicks
_HpicfMldGroupPortCacheVersion1Timer_Object = MibTableColumn
hpicfMldGroupPortCacheVersion1Timer = _HpicfMldGroupPortCacheVersion1Timer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 6),
    _HpicfMldGroupPortCacheVersion1Timer_Type()
)
hpicfMldGroupPortCacheVersion1Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheVersion1Timer.setStatus("current")
_HpicfMldGroupPortCacheFilterTimer_Type = TimeTicks
_HpicfMldGroupPortCacheFilterTimer_Object = MibTableColumn
hpicfMldGroupPortCacheFilterTimer = _HpicfMldGroupPortCacheFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 7),
    _HpicfMldGroupPortCacheFilterTimer_Type()
)
hpicfMldGroupPortCacheFilterTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheFilterTimer.setStatus("current")


class _HpicfMldGroupPortCacheFilterMode_Type(Integer32):
    """Custom type hpicfMldGroupPortCacheFilterMode based on Integer32"""
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


_HpicfMldGroupPortCacheFilterMode_Type.__name__ = "Integer32"
_HpicfMldGroupPortCacheFilterMode_Object = MibTableColumn
hpicfMldGroupPortCacheFilterMode = _HpicfMldGroupPortCacheFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 8),
    _HpicfMldGroupPortCacheFilterMode_Type()
)
hpicfMldGroupPortCacheFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheFilterMode.setStatus("current")
_HpicfMldGroupPortCacheExcludeSrcCount_Type = Counter32
_HpicfMldGroupPortCacheExcludeSrcCount_Object = MibTableColumn
hpicfMldGroupPortCacheExcludeSrcCount = _HpicfMldGroupPortCacheExcludeSrcCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 9),
    _HpicfMldGroupPortCacheExcludeSrcCount_Type()
)
hpicfMldGroupPortCacheExcludeSrcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheExcludeSrcCount.setStatus("current")
_HpicfMldGroupPortCacheRequestedSrcCount_Type = Counter32
_HpicfMldGroupPortCacheRequestedSrcCount_Object = MibTableColumn
hpicfMldGroupPortCacheRequestedSrcCount = _HpicfMldGroupPortCacheRequestedSrcCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 14, 1, 10),
    _HpicfMldGroupPortCacheRequestedSrcCount_Type()
)
hpicfMldGroupPortCacheRequestedSrcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheRequestedSrcCount.setStatus("current")


class _HpicfMldReload_Type(TruthValue):
    """Custom type hpicfMldReload based on TruthValue"""


_HpicfMldReload_Object = MibScalar
hpicfMldReload = _HpicfMldReload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 1, 1, 15),
    _HpicfMldReload_Type()
)
hpicfMldReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMldReload.setStatus("current")
_HpicfMldConformance_ObjectIdentity = ObjectIdentity
hpicfMldConformance = _HpicfMldConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2)
)
_HpicfMldGroups_ObjectIdentity = ObjectIdentity
hpicfMldGroups = _HpicfMldGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1)
)
_HpicfMldCompliances_ObjectIdentity = ObjectIdentity
hpicfMldCompliances = _HpicfMldCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 2)
)
mldInterfaceEntry.registerAugmentions(
    ("HP-ICF-MLD-MIB",
     "hpicfMldIfEntry")
)
hpicfMldIfEntry.setIndexNames(*mldInterfaceEntry.getIndexNames())

# Managed Objects groups

hpicfMldBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 1)
)
hpicfMldBaseGroup.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldControlUnknownMulticast"),
        ("HP-ICF-MLD-MIB", "hpicfMldConfigForcedLeaveInterval"),
        ("HP-ICF-MLD-MIB", "hpicfMldEnabledCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldMcastGroupJoinsCount"))
)
if mibBuilder.loadTexts:
    hpicfMldBaseGroup.setStatus("current")

hpicfMldIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 2)
)
hpicfMldIfGroup.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldIfEntryQuerierFeature"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntrySnoopingFeature"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryQuerierPort"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryFilteredJoins"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStandardJoins"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryPortsWithMcastRouter"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGeneralQueryRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatQueryTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSQRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSQTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV1ReportRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV2ReportRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV1LeaveRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatUnknownMldTypeRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatUnknownPktRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatForwardToRoutersTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatForwardToAllPortsTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatFastLeaves"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatForcedFastLeaves"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatJoinTimeouts"))
)
if mibBuilder.loadTexts:
    hpicfMldIfGroup.setStatus("current")

hpicfMldCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 3)
)
hpicfMldCacheGroup.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldCacheSelf"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheLastReporter"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheUpTime"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheExpiryTime"),
        ("HP-ICF-MLD-MIB", "hpicfMldGroupType"),
        ("HP-ICF-MLD-MIB", "hpicfJoinedPorts"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheStatus"))
)
if mibBuilder.loadTexts:
    hpicfMldCacheGroup.setStatus("current")

hpicfMldPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 4)
)
hpicfMldPortGroup.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldPortConfigEntryPortModeFeature"),
        ("HP-ICF-MLD-MIB", "hpicfMldPortConfigEntryForcedLeaveFeature"),
        ("HP-ICF-MLD-MIB", "hpicfMldPortConfigEntryFastLeaveFeature"))
)
if mibBuilder.loadTexts:
    hpicfMldPortGroup.setStatus("current")

hpicfMldFilteredGroupPortCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 5)
)
hpicfMldFilteredGroupPortCacheGroup.setObjects(
    ("HP-ICF-MLD-MIB", "hpicfMldFilteredGroupPortCacheExpiryTime")
)
if mibBuilder.loadTexts:
    hpicfMldFilteredGroupPortCacheGroup.setStatus("current")

hpicfMldBaseGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 6)
)
hpicfMldBaseGroupV2.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldControlUnknownMulticast"),
        ("HP-ICF-MLD-MIB", "hpicfMldConfigForcedLeaveInterval"),
        ("HP-ICF-MLD-MIB", "hpicfMldEnabledCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldMcastGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldMcastExcludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldMcastIncludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldMcastPortFastLearn"))
)
if mibBuilder.loadTexts:
    hpicfMldBaseGroupV2.setStatus("current")

hpicfMldIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 7)
)
hpicfMldIfGroupV2.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldIfEntryQuerierFeature"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntrySnoopingFeature"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryQuerierPort"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryFilteredJoins"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStandardJoins"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryPortsWithMcastRouter"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGeneralQueryRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatQueryTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSQRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSQTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV1ReportRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV2ReportRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV1LeaveRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatUnknownMldTypeRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatUnknownPktRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatForwardToRoutersTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatForwardToAllPortsTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatFastLeaves"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatForcedFastLeaves"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatJoinTimeouts"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatWrongVersionQueries"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryLastMemberQueryCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStartupQueryCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStartupQueryInterval"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatExcludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatIncludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatFilteredExcludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatFilteredIncludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatStandardExcludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatStandardIncludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV1QueryTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV1QueryRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV2QueryTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV2QueryRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSSQTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSSQRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMalformedPktRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatBadCheckSumRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMartianSourceRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatPacketsRxOnDisabled"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStrictVersionMode"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV1ReportTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV2ReportTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryState"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV1GSQRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV1GSQTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV2GSQRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV2GSQTx"))
)
if mibBuilder.loadTexts:
    hpicfMldIfGroupV2.setStatus("current")

hpicfMldCacheGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 8)
)
hpicfMldCacheGroupV2.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldCacheSelf"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheLastReporter"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheUpTime"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheExpiryTime"),
        ("HP-ICF-MLD-MIB", "hpicfMldGroupType"),
        ("HP-ICF-MLD-MIB", "hpicfJoinedPorts"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheStatus"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheFilterMode"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheExcludeModeExpiryTimer"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheVersion1HostTimer"),
        ("HP-ICF-MLD-MIB", "hpicfMldCacheSrcCount"))
)
if mibBuilder.loadTexts:
    hpicfMldCacheGroupV2.setStatus("current")

hpicfMldSrcListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 9)
)
hpicfMldSrcListGroup.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldSrcListPorts"),
        ("HP-ICF-MLD-MIB", "hpicfMldSrcListExpiry"),
        ("HP-ICF-MLD-MIB", "hpicfMldSrcListUpTime"),
        ("HP-ICF-MLD-MIB", "hpicfMldSrcListType"))
)
if mibBuilder.loadTexts:
    hpicfMldSrcListGroup.setStatus("current")

hpicfMldPortSrcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 10)
)
hpicfMldPortSrcGroup.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldPortSrcExpiry"),
        ("HP-ICF-MLD-MIB", "hpicfMldPortSrcUpTime"),
        ("HP-ICF-MLD-MIB", "hpicfMldPortSrcFilterMode"))
)
if mibBuilder.loadTexts:
    hpicfMldPortSrcGroup.setStatus("current")

hpicfMldGroupPortCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 11)
)
hpicfMldGroupPortCacheGroup.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldGroupPortCacheExpiryTime"),
        ("HP-ICF-MLD-MIB", "hpicfMldGroupPortCacheUpTime"),
        ("HP-ICF-MLD-MIB", "hpicfMldGroupPortCacheVersion1Timer"),
        ("HP-ICF-MLD-MIB", "hpicfMldGroupPortCacheFilterTimer"),
        ("HP-ICF-MLD-MIB", "hpicfMldGroupPortCacheFilterMode"),
        ("HP-ICF-MLD-MIB", "hpicfMldGroupPortCacheExcludeSrcCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldGroupPortCacheRequestedSrcCount"))
)
if mibBuilder.loadTexts:
    hpicfMldGroupPortCacheGroup.setStatus("current")

hpicfMldIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 12)
)
hpicfMldIfGroupV3.setObjects(
      *(("HP-ICF-MLD-MIB", "hpicfMldIfEntryQuerierFeature"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntrySnoopingFeature"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryQuerierPort"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryFilteredJoins"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStandardJoins"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryPortsWithMcastRouter"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGeneralQueryRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatQueryTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSQRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSQTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV1ReportRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV2ReportRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV1LeaveRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatUnknownMldTypeRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatUnknownPktRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatForwardToRoutersTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatForwardToAllPortsTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatFastLeaves"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatForcedFastLeaves"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatJoinTimeouts"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatWrongVersionQueries"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryLastMemberQueryCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStartupQueryCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStartupQueryInterval"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatExcludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatIncludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatFilteredExcludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatFilteredIncludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatStandardExcludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatStandardIncludeGroupJoinsCount"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV1QueryTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV1QueryRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV2QueryTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV2QueryRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSSQTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatGSSQRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMalformedPktRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatBadCheckSumRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMartianSourceRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatPacketsRxOnDisabled"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStrictVersionMode"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV1ReportTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatMldV2ReportTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryState"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV1GSQRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV1GSQTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV2GSQRx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStatV2GSQTx"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryStartupQueryExpiryTime"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryOtherQuerierInterval"),
        ("HP-ICF-MLD-MIB", "hpicfMldIfEntryOtherQuerierExpiryTime"))
)
if mibBuilder.loadTexts:
    hpicfMldIfGroupV3.setStatus("current")

hpicfMldReloadModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 1, 13)
)
hpicfMldReloadModeGroup.setObjects(
    ("HP-ICF-MLD-MIB", "hpicfMldReload")
)
if mibBuilder.loadTexts:
    hpicfMldReloadModeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfMldMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfMldMIBCompliance.setStatus(
        "current"
    )

hpicfMldMIBComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfMldMIBComplianceV2.setStatus(
        "current"
    )

hpicfMldMIBComplianceV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfMldMIBComplianceV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-MLD-MIB",
    **{"HpicfMcastGroupTypeDefinition": HpicfMcastGroupTypeDefinition,
       "HpicfMldIfEntryState": HpicfMldIfEntryState,
       "HpicfMldConfigPortModeType": HpicfMldConfigPortModeType,
       "hpicfMldMIB": hpicfMldMIB,
       "hpicfMldObjects": hpicfMldObjects,
       "hpicfMld": hpicfMld,
       "hpicfMldControlUnknownMulticast": hpicfMldControlUnknownMulticast,
       "hpicfMldConfigForcedLeaveInterval": hpicfMldConfigForcedLeaveInterval,
       "hpicfMldEnabledCount": hpicfMldEnabledCount,
       "hpicfMldMcastGroupJoinsCount": hpicfMldMcastGroupJoinsCount,
       "hpicfMldIfTable": hpicfMldIfTable,
       "hpicfMldIfEntry": hpicfMldIfEntry,
       "hpicfMldIfEntryQuerierFeature": hpicfMldIfEntryQuerierFeature,
       "hpicfMldIfEntrySnoopingFeature": hpicfMldIfEntrySnoopingFeature,
       "hpicfMldIfEntryQuerierPort": hpicfMldIfEntryQuerierPort,
       "hpicfMldIfEntryFilteredJoins": hpicfMldIfEntryFilteredJoins,
       "hpicfMldIfEntryStandardJoins": hpicfMldIfEntryStandardJoins,
       "hpicfMldIfEntryPortsWithMcastRouter": hpicfMldIfEntryPortsWithMcastRouter,
       "hpicfMldIfEntryStatGeneralQueryRx": hpicfMldIfEntryStatGeneralQueryRx,
       "hpicfMldIfEntryStatQueryTx": hpicfMldIfEntryStatQueryTx,
       "hpicfMldIfEntryStatGSQRx": hpicfMldIfEntryStatGSQRx,
       "hpicfMldIfEntryStatGSQTx": hpicfMldIfEntryStatGSQTx,
       "hpicfMldIfEntryStatMldV1ReportRx": hpicfMldIfEntryStatMldV1ReportRx,
       "hpicfMldIfEntryStatMldV2ReportRx": hpicfMldIfEntryStatMldV2ReportRx,
       "hpicfMldIfEntryStatMldV1LeaveRx": hpicfMldIfEntryStatMldV1LeaveRx,
       "hpicfMldIfEntryStatUnknownMldTypeRx": hpicfMldIfEntryStatUnknownMldTypeRx,
       "hpicfMldIfEntryStatUnknownPktRx": hpicfMldIfEntryStatUnknownPktRx,
       "hpicfMldIfEntryStatForwardToRoutersTx": hpicfMldIfEntryStatForwardToRoutersTx,
       "hpicfMldIfEntryStatForwardToAllPortsTx": hpicfMldIfEntryStatForwardToAllPortsTx,
       "hpicfMldIfEntryStatFastLeaves": hpicfMldIfEntryStatFastLeaves,
       "hpicfMldIfEntryStatForcedFastLeaves": hpicfMldIfEntryStatForcedFastLeaves,
       "hpicfMldIfEntryStatJoinTimeouts": hpicfMldIfEntryStatJoinTimeouts,
       "hpicfMldIfEntryStatWrongVersionQueries": hpicfMldIfEntryStatWrongVersionQueries,
       "hpicfMldIfEntryLastMemberQueryCount": hpicfMldIfEntryLastMemberQueryCount,
       "hpicfMldIfEntryStartupQueryCount": hpicfMldIfEntryStartupQueryCount,
       "hpicfMldIfEntryStartupQueryInterval": hpicfMldIfEntryStartupQueryInterval,
       "hpicfMldIfEntryStatExcludeGroupJoinsCount": hpicfMldIfEntryStatExcludeGroupJoinsCount,
       "hpicfMldIfEntryStatIncludeGroupJoinsCount": hpicfMldIfEntryStatIncludeGroupJoinsCount,
       "hpicfMldIfEntryStatFilteredExcludeGroupJoinsCount": hpicfMldIfEntryStatFilteredExcludeGroupJoinsCount,
       "hpicfMldIfEntryStatFilteredIncludeGroupJoinsCount": hpicfMldIfEntryStatFilteredIncludeGroupJoinsCount,
       "hpicfMldIfEntryStatStandardExcludeGroupJoinsCount": hpicfMldIfEntryStatStandardExcludeGroupJoinsCount,
       "hpicfMldIfEntryStatStandardIncludeGroupJoinsCount": hpicfMldIfEntryStatStandardIncludeGroupJoinsCount,
       "hpicfMldIfEntryStatV1QueryTx": hpicfMldIfEntryStatV1QueryTx,
       "hpicfMldIfEntryStatV1QueryRx": hpicfMldIfEntryStatV1QueryRx,
       "hpicfMldIfEntryStatV2QueryTx": hpicfMldIfEntryStatV2QueryTx,
       "hpicfMldIfEntryStatV2QueryRx": hpicfMldIfEntryStatV2QueryRx,
       "hpicfMldIfEntryStatGSSQTx": hpicfMldIfEntryStatGSSQTx,
       "hpicfMldIfEntryStatGSSQRx": hpicfMldIfEntryStatGSSQRx,
       "hpicfMldIfEntryStatMalformedPktRx": hpicfMldIfEntryStatMalformedPktRx,
       "hpicfMldIfEntryStatBadCheckSumRx": hpicfMldIfEntryStatBadCheckSumRx,
       "hpicfMldIfEntryStatMartianSourceRx": hpicfMldIfEntryStatMartianSourceRx,
       "hpicfMldIfEntryStatPacketsRxOnDisabled": hpicfMldIfEntryStatPacketsRxOnDisabled,
       "hpicfMldIfEntryStrictVersionMode": hpicfMldIfEntryStrictVersionMode,
       "hpicfMldIfEntryStatMldV1ReportTx": hpicfMldIfEntryStatMldV1ReportTx,
       "hpicfMldIfEntryStatMldV2ReportTx": hpicfMldIfEntryStatMldV2ReportTx,
       "hpicfMldIfEntryState": hpicfMldIfEntryState,
       "hpicfMldIfEntryStatV1GSQRx": hpicfMldIfEntryStatV1GSQRx,
       "hpicfMldIfEntryStatV1GSQTx": hpicfMldIfEntryStatV1GSQTx,
       "hpicfMldIfEntryStatV2GSQRx": hpicfMldIfEntryStatV2GSQRx,
       "hpicfMldIfEntryStatV2GSQTx": hpicfMldIfEntryStatV2GSQTx,
       "hpicfMldIfEntryStartupQueryExpiryTime": hpicfMldIfEntryStartupQueryExpiryTime,
       "hpicfMldIfEntryOtherQuerierInterval": hpicfMldIfEntryOtherQuerierInterval,
       "hpicfMldIfEntryOtherQuerierExpiryTime": hpicfMldIfEntryOtherQuerierExpiryTime,
       "hpicfMldCacheTable": hpicfMldCacheTable,
       "hpicfMldCacheEntry": hpicfMldCacheEntry,
       "hpicfMldCacheIfIndex": hpicfMldCacheIfIndex,
       "hpicfMldCacheAddress": hpicfMldCacheAddress,
       "hpicfMldCacheSelf": hpicfMldCacheSelf,
       "hpicfMldCacheLastReporter": hpicfMldCacheLastReporter,
       "hpicfMldCacheUpTime": hpicfMldCacheUpTime,
       "hpicfMldCacheExpiryTime": hpicfMldCacheExpiryTime,
       "hpicfMldGroupType": hpicfMldGroupType,
       "hpicfJoinedPorts": hpicfJoinedPorts,
       "hpicfMldCacheStatus": hpicfMldCacheStatus,
       "hpicfMldCacheFilterMode": hpicfMldCacheFilterMode,
       "hpicfMldCacheExcludeModeExpiryTimer": hpicfMldCacheExcludeModeExpiryTimer,
       "hpicfMldCacheVersion1HostTimer": hpicfMldCacheVersion1HostTimer,
       "hpicfMldCacheSrcCount": hpicfMldCacheSrcCount,
       "hpicfMldPortConfigTable": hpicfMldPortConfigTable,
       "hpicfMldPortConfigEntry": hpicfMldPortConfigEntry,
       "hpicfMldPortConfigEntryInterfaceIfIndex": hpicfMldPortConfigEntryInterfaceIfIndex,
       "hpicfMldPortConfigEntryIndex": hpicfMldPortConfigEntryIndex,
       "hpicfMldPortConfigEntryPortModeFeature": hpicfMldPortConfigEntryPortModeFeature,
       "hpicfMldPortConfigEntryForcedLeaveFeature": hpicfMldPortConfigEntryForcedLeaveFeature,
       "hpicfMldPortConfigEntryFastLeaveFeature": hpicfMldPortConfigEntryFastLeaveFeature,
       "hpicfMldFilteredGroupPortCacheTable": hpicfMldFilteredGroupPortCacheTable,
       "hpicfMldFilteredGroupPortCacheEntry": hpicfMldFilteredGroupPortCacheEntry,
       "hpicfMldFilteredGroupPortCacheIfIndex": hpicfMldFilteredGroupPortCacheIfIndex,
       "hpicfMldFilteredGroupPortCacheGroupAddress": hpicfMldFilteredGroupPortCacheGroupAddress,
       "hpicfMldFilteredGroupPortCachePortIndex": hpicfMldFilteredGroupPortCachePortIndex,
       "hpicfMldFilteredGroupPortCacheExpiryTime": hpicfMldFilteredGroupPortCacheExpiryTime,
       "hpicfMldSrcListTable": hpicfMldSrcListTable,
       "hpicfMldSrcListEntry": hpicfMldSrcListEntry,
       "hpicfMldSrcListIfIndex": hpicfMldSrcListIfIndex,
       "hpicfMldSrcListAddress": hpicfMldSrcListAddress,
       "hpicfMldSrcListHostAddress": hpicfMldSrcListHostAddress,
       "hpicfMldSrcListPorts": hpicfMldSrcListPorts,
       "hpicfMldSrcListExpiry": hpicfMldSrcListExpiry,
       "hpicfMldSrcListUpTime": hpicfMldSrcListUpTime,
       "hpicfMldSrcListType": hpicfMldSrcListType,
       "hpicfMldPortSrcTable": hpicfMldPortSrcTable,
       "hpicfMldPortSrcEntry": hpicfMldPortSrcEntry,
       "hpicfMldPortSrcIfIndex": hpicfMldPortSrcIfIndex,
       "hpicfMldPortSrcAddress": hpicfMldPortSrcAddress,
       "hpicfMldPortSrcHostAddress": hpicfMldPortSrcHostAddress,
       "hpicfMldPortSrcPortIndex": hpicfMldPortSrcPortIndex,
       "hpicfMldPortSrcExpiry": hpicfMldPortSrcExpiry,
       "hpicfMldPortSrcUpTime": hpicfMldPortSrcUpTime,
       "hpicfMldPortSrcFilterMode": hpicfMldPortSrcFilterMode,
       "hpicfMldMcastExcludeGroupJoinsCount": hpicfMldMcastExcludeGroupJoinsCount,
       "hpicfMldMcastIncludeGroupJoinsCount": hpicfMldMcastIncludeGroupJoinsCount,
       "hpicfMldMcastPortFastLearn": hpicfMldMcastPortFastLearn,
       "hpicfMldGroupPortCacheTable": hpicfMldGroupPortCacheTable,
       "hpicfMldGroupPortCacheEntry": hpicfMldGroupPortCacheEntry,
       "hpicfMldGroupPortCacheIfIndex": hpicfMldGroupPortCacheIfIndex,
       "hpicfMldGroupPortCacheGroupAddress": hpicfMldGroupPortCacheGroupAddress,
       "hpicfMldGroupPortCachePortIndex": hpicfMldGroupPortCachePortIndex,
       "hpicfMldGroupPortCacheExpiryTime": hpicfMldGroupPortCacheExpiryTime,
       "hpicfMldGroupPortCacheUpTime": hpicfMldGroupPortCacheUpTime,
       "hpicfMldGroupPortCacheVersion1Timer": hpicfMldGroupPortCacheVersion1Timer,
       "hpicfMldGroupPortCacheFilterTimer": hpicfMldGroupPortCacheFilterTimer,
       "hpicfMldGroupPortCacheFilterMode": hpicfMldGroupPortCacheFilterMode,
       "hpicfMldGroupPortCacheExcludeSrcCount": hpicfMldGroupPortCacheExcludeSrcCount,
       "hpicfMldGroupPortCacheRequestedSrcCount": hpicfMldGroupPortCacheRequestedSrcCount,
       "hpicfMldReload": hpicfMldReload,
       "hpicfMldConformance": hpicfMldConformance,
       "hpicfMldGroups": hpicfMldGroups,
       "hpicfMldBaseGroup": hpicfMldBaseGroup,
       "hpicfMldIfGroup": hpicfMldIfGroup,
       "hpicfMldCacheGroup": hpicfMldCacheGroup,
       "hpicfMldPortGroup": hpicfMldPortGroup,
       "hpicfMldFilteredGroupPortCacheGroup": hpicfMldFilteredGroupPortCacheGroup,
       "hpicfMldBaseGroupV2": hpicfMldBaseGroupV2,
       "hpicfMldIfGroupV2": hpicfMldIfGroupV2,
       "hpicfMldCacheGroupV2": hpicfMldCacheGroupV2,
       "hpicfMldSrcListGroup": hpicfMldSrcListGroup,
       "hpicfMldPortSrcGroup": hpicfMldPortSrcGroup,
       "hpicfMldGroupPortCacheGroup": hpicfMldGroupPortCacheGroup,
       "hpicfMldIfGroupV3": hpicfMldIfGroupV3,
       "hpicfMldReloadModeGroup": hpicfMldReloadModeGroup,
       "hpicfMldCompliances": hpicfMldCompliances,
       "hpicfMldMIBCompliance": hpicfMldMIBCompliance,
       "hpicfMldMIBComplianceV2": hpicfMldMIBComplianceV2,
       "hpicfMldMIBComplianceV3": hpicfMldMIBComplianceV3}
)
