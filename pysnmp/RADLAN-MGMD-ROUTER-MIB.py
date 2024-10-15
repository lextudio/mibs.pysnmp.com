# SNMP MIB module (RADLAN-MGMD-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-MGMD-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:39 2024
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

(mgmdRouterInterfaceEntry,) = mibBuilder.importSymbols(
    "MGMD-STD-MIB",
    "mgmdRouterInterfaceEntry")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(NpgOperStatus,) = mibBuilder.importSymbols(
    "RADLAN-PIM-MIB",
    "NpgOperStatus")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

rlIgmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 225)
)
rlIgmp.setRevisions(
        ("2011-07-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



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



# MIB Managed Objects in the order of their OIDs

_RlMgmdInterfaceExtTable_Object = MibTable
rlMgmdInterfaceExtTable = _RlMgmdInterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1)
)
if mibBuilder.loadTexts:
    rlMgmdInterfaceExtTable.setStatus("current")
_RlMgmdInterfaceExtEntry_Object = MibTableRow
rlMgmdInterfaceExtEntry = _RlMgmdInterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1)
)
if mibBuilder.loadTexts:
    rlMgmdInterfaceExtEntry.setStatus("current")
_RlMgmdRouterInterfaceExtStatsUpTime_Type = TimeTicks
_RlMgmdRouterInterfaceExtStatsUpTime_Object = MibTableColumn
rlMgmdRouterInterfaceExtStatsUpTime = _RlMgmdRouterInterfaceExtStatsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 1),
    _RlMgmdRouterInterfaceExtStatsUpTime_Type()
)
rlMgmdRouterInterfaceExtStatsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtStatsUpTime.setStatus("current")
_RlMgmdRouterInterfaceExtEnableStats_Type = TruthValue
_RlMgmdRouterInterfaceExtEnableStats_Object = MibTableColumn
rlMgmdRouterInterfaceExtEnableStats = _RlMgmdRouterInterfaceExtEnableStats_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 2),
    _RlMgmdRouterInterfaceExtEnableStats_Type()
)
rlMgmdRouterInterfaceExtEnableStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtEnableStats.setStatus("current")
_RlMgmdRouterInterfaceExtNumFailedJoins_Type = Unsigned32
_RlMgmdRouterInterfaceExtNumFailedJoins_Object = MibTableColumn
rlMgmdRouterInterfaceExtNumFailedJoins = _RlMgmdRouterInterfaceExtNumFailedJoins_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 3),
    _RlMgmdRouterInterfaceExtNumFailedJoins_Type()
)
rlMgmdRouterInterfaceExtNumFailedJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtNumFailedJoins.setStatus("current")
_RlMgmdRouterInterfaceExtNumIgmpV1Msgs_Type = Unsigned32
_RlMgmdRouterInterfaceExtNumIgmpV1Msgs_Object = MibTableColumn
rlMgmdRouterInterfaceExtNumIgmpV1Msgs = _RlMgmdRouterInterfaceExtNumIgmpV1Msgs_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 4),
    _RlMgmdRouterInterfaceExtNumIgmpV1Msgs_Type()
)
rlMgmdRouterInterfaceExtNumIgmpV1Msgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtNumIgmpV1Msgs.setStatus("current")
_RlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs_Type = Unsigned32
_RlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs_Object = MibTableColumn
rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs = _RlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 5),
    _RlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs_Type()
)
rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs.setStatus("current")
_RlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs_Type = Unsigned32
_RlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs_Object = MibTableColumn
rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs = _RlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 6),
    _RlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs_Type()
)
rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs.setStatus("current")
_RlMgmdRouterInterfaceExtNumInvalidMsgsRcvd_Type = Unsigned32
_RlMgmdRouterInterfaceExtNumInvalidMsgsRcvd_Object = MibTableColumn
rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd = _RlMgmdRouterInterfaceExtNumInvalidMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 7),
    _RlMgmdRouterInterfaceExtNumInvalidMsgsRcvd_Type()
)
rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd.setStatus("current")
_RlMgmdRouterInterfaceExtNumGenQueriesSent_Type = Unsigned32
_RlMgmdRouterInterfaceExtNumGenQueriesSent_Object = MibTableColumn
rlMgmdRouterInterfaceExtNumGenQueriesSent = _RlMgmdRouterInterfaceExtNumGenQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 8),
    _RlMgmdRouterInterfaceExtNumGenQueriesSent_Type()
)
rlMgmdRouterInterfaceExtNumGenQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtNumGenQueriesSent.setStatus("current")
_RlMgmdRouterInterfaceExtNumSpecQueriesSent_Type = Unsigned32
_RlMgmdRouterInterfaceExtNumSpecQueriesSent_Object = MibTableColumn
rlMgmdRouterInterfaceExtNumSpecQueriesSent = _RlMgmdRouterInterfaceExtNumSpecQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 9),
    _RlMgmdRouterInterfaceExtNumSpecQueriesSent_Type()
)
rlMgmdRouterInterfaceExtNumSpecQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtNumSpecQueriesSent.setStatus("current")
_RlmgmdRouterInterfaceQrRobustness_Type = Unsigned32
_RlmgmdRouterInterfaceQrRobustness_Object = MibTableColumn
rlmgmdRouterInterfaceQrRobustness = _RlmgmdRouterInterfaceQrRobustness_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 10),
    _RlmgmdRouterInterfaceQrRobustness_Type()
)
rlmgmdRouterInterfaceQrRobustness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlmgmdRouterInterfaceQrRobustness.setStatus("current")
_RlmgmdRouterInterfaceQrQueryInterval_Type = Unsigned32
_RlmgmdRouterInterfaceQrQueryInterval_Object = MibTableColumn
rlmgmdRouterInterfaceQrQueryInterval = _RlmgmdRouterInterfaceQrQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 11),
    _RlmgmdRouterInterfaceQrQueryInterval_Type()
)
rlmgmdRouterInterfaceQrQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlmgmdRouterInterfaceQrQueryInterval.setStatus("current")
_RlmgmdRouterInterfaceQrQueryMaxResponseTime_Type = Unsigned32
_RlmgmdRouterInterfaceQrQueryMaxResponseTime_Object = MibTableColumn
rlmgmdRouterInterfaceQrQueryMaxResponseTime = _RlmgmdRouterInterfaceQrQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 12),
    _RlmgmdRouterInterfaceQrQueryMaxResponseTime_Type()
)
rlmgmdRouterInterfaceQrQueryMaxResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlmgmdRouterInterfaceQrQueryMaxResponseTime.setStatus("current")
_RlmgmdRouterInterfaceQrLastMembQueryIntvl_Type = Unsigned32
_RlmgmdRouterInterfaceQrLastMembQueryIntvl_Object = MibTableColumn
rlmgmdRouterInterfaceQrLastMembQueryIntvl = _RlmgmdRouterInterfaceQrLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 13),
    _RlmgmdRouterInterfaceQrLastMembQueryIntvl_Type()
)
rlmgmdRouterInterfaceQrLastMembQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlmgmdRouterInterfaceQrLastMembQueryIntvl.setStatus("current")
_RlmgmdRouterInterfaceExtSrcAndGrpFilter_Type = DisplayString
_RlmgmdRouterInterfaceExtSrcAndGrpFilter_Object = MibTableColumn
rlmgmdRouterInterfaceExtSrcAndGrpFilter = _RlmgmdRouterInterfaceExtSrcAndGrpFilter_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 14),
    _RlmgmdRouterInterfaceExtSrcAndGrpFilter_Type()
)
rlmgmdRouterInterfaceExtSrcAndGrpFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlmgmdRouterInterfaceExtSrcAndGrpFilter.setStatus("current")


class _RlMgmdRouterInterfaceExtAdminStatus_Type(AdminStatus):
    """Custom type rlMgmdRouterInterfaceExtAdminStatus based on AdminStatus"""


_RlMgmdRouterInterfaceExtAdminStatus_Object = MibTableColumn
rlMgmdRouterInterfaceExtAdminStatus = _RlMgmdRouterInterfaceExtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 15),
    _RlMgmdRouterInterfaceExtAdminStatus_Type()
)
rlMgmdRouterInterfaceExtAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtAdminStatus.setStatus("current")
_RlMgmdRouterInterfaceExtOperStatus_Type = NpgOperStatus
_RlMgmdRouterInterfaceExtOperStatus_Object = MibTableColumn
rlMgmdRouterInterfaceExtOperStatus = _RlMgmdRouterInterfaceExtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 16),
    _RlMgmdRouterInterfaceExtOperStatus_Type()
)
rlMgmdRouterInterfaceExtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtOperStatus.setStatus("current")
_RlMgmdRouterInterfaceExtIsQuerier_Type = TruthValue
_RlMgmdRouterInterfaceExtIsQuerier_Object = MibTableColumn
rlMgmdRouterInterfaceExtIsQuerier = _RlMgmdRouterInterfaceExtIsQuerier_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 17),
    _RlMgmdRouterInterfaceExtIsQuerier_Type()
)
rlMgmdRouterInterfaceExtIsQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtIsQuerier.setStatus("current")


class _RlMgmdRouterInterfaceExtProxyDownProtected_Type(Integer32):
    """Custom type rlMgmdRouterInterfaceExtProxyDownProtected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unspecified", -1))
    )


_RlMgmdRouterInterfaceExtProxyDownProtected_Type.__name__ = "Integer32"
_RlMgmdRouterInterfaceExtProxyDownProtected_Object = MibTableColumn
rlMgmdRouterInterfaceExtProxyDownProtected = _RlMgmdRouterInterfaceExtProxyDownProtected_Object(
    (1, 3, 6, 1, 4, 1, 89, 225, 1, 1, 18),
    _RlMgmdRouterInterfaceExtProxyDownProtected_Type()
)
rlMgmdRouterInterfaceExtProxyDownProtected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMgmdRouterInterfaceExtProxyDownProtected.setStatus("current")
mgmdRouterInterfaceEntry.registerAugmentions(
    ("RADLAN-MGMD-ROUTER-MIB",
     "rlMgmdInterfaceExtEntry")
)
rlMgmdInterfaceExtEntry.setIndexNames(*mgmdRouterInterfaceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-MGMD-ROUTER-MIB",
    **{"AdminStatus": AdminStatus,
       "rlIgmp": rlIgmp,
       "rlMgmdInterfaceExtTable": rlMgmdInterfaceExtTable,
       "rlMgmdInterfaceExtEntry": rlMgmdInterfaceExtEntry,
       "rlMgmdRouterInterfaceExtStatsUpTime": rlMgmdRouterInterfaceExtStatsUpTime,
       "rlMgmdRouterInterfaceExtEnableStats": rlMgmdRouterInterfaceExtEnableStats,
       "rlMgmdRouterInterfaceExtNumFailedJoins": rlMgmdRouterInterfaceExtNumFailedJoins,
       "rlMgmdRouterInterfaceExtNumIgmpV1Msgs": rlMgmdRouterInterfaceExtNumIgmpV1Msgs,
       "rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs": rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs,
       "rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs": rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs,
       "rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd": rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd,
       "rlMgmdRouterInterfaceExtNumGenQueriesSent": rlMgmdRouterInterfaceExtNumGenQueriesSent,
       "rlMgmdRouterInterfaceExtNumSpecQueriesSent": rlMgmdRouterInterfaceExtNumSpecQueriesSent,
       "rlmgmdRouterInterfaceQrRobustness": rlmgmdRouterInterfaceQrRobustness,
       "rlmgmdRouterInterfaceQrQueryInterval": rlmgmdRouterInterfaceQrQueryInterval,
       "rlmgmdRouterInterfaceQrQueryMaxResponseTime": rlmgmdRouterInterfaceQrQueryMaxResponseTime,
       "rlmgmdRouterInterfaceQrLastMembQueryIntvl": rlmgmdRouterInterfaceQrLastMembQueryIntvl,
       "rlmgmdRouterInterfaceExtSrcAndGrpFilter": rlmgmdRouterInterfaceExtSrcAndGrpFilter,
       "rlMgmdRouterInterfaceExtAdminStatus": rlMgmdRouterInterfaceExtAdminStatus,
       "rlMgmdRouterInterfaceExtOperStatus": rlMgmdRouterInterfaceExtOperStatus,
       "rlMgmdRouterInterfaceExtIsQuerier": rlMgmdRouterInterfaceExtIsQuerier,
       "rlMgmdRouterInterfaceExtProxyDownProtected": rlMgmdRouterInterfaceExtProxyDownProtected}
)
