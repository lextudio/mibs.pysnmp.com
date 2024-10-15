# SNMP MIB module (IGMP-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IGMP-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:57 2024
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

(cjnProtocol,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnProtocol")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cjnIgmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnIgmpGblGroup_ObjectIdentity = ObjectIdentity
cjnIgmpGblGroup = _CjnIgmpGblGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 1)
)


class _CjnIgmpIsEnabled_Type(Integer32):
    """Custom type cjnIgmpIsEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CjnIgmpIsEnabled_Type.__name__ = "Integer32"
_CjnIgmpIsEnabled_Object = MibScalar
cjnIgmpIsEnabled = _CjnIgmpIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 1, 1),
    _CjnIgmpIsEnabled_Type()
)
cjnIgmpIsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIsEnabled.setStatus("current")


class _CjnIpIgmpGblStatsReset_Type(Integer32):
    """Custom type cjnIpIgmpGblStatsReset based on Integer32"""
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


_CjnIpIgmpGblStatsReset_Type.__name__ = "Integer32"
_CjnIpIgmpGblStatsReset_Object = MibScalar
cjnIpIgmpGblStatsReset = _CjnIpIgmpGblStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 1, 2),
    _CjnIpIgmpGblStatsReset_Type()
)
cjnIpIgmpGblStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpIgmpGblStatsReset.setStatus("current")
_CjnIgmpGblStatsGroup_ObjectIdentity = ObjectIdentity
cjnIgmpGblStatsGroup = _CjnIgmpGblStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2)
)
_CjnIgmpRxReport_Type = Integer32
_CjnIgmpRxReport_Object = MibScalar
cjnIgmpRxReport = _CjnIgmpRxReport_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2, 1),
    _CjnIgmpRxReport_Type()
)
cjnIgmpRxReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpRxReport.setStatus("current")
_CjnIgmpRxQuery_Type = Integer32
_CjnIgmpRxQuery_Object = MibScalar
cjnIgmpRxQuery = _CjnIgmpRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2, 2),
    _CjnIgmpRxQuery_Type()
)
cjnIgmpRxQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpRxQuery.setStatus("current")
_CjnIgmpTxQuery_Type = Integer32
_CjnIgmpTxQuery_Object = MibScalar
cjnIgmpTxQuery = _CjnIgmpTxQuery_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2, 3),
    _CjnIgmpTxQuery_Type()
)
cjnIgmpTxQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpTxQuery.setStatus("current")
_CjnIgmpRxUnknownCode_Type = Integer32
_CjnIgmpRxUnknownCode_Object = MibScalar
cjnIgmpRxUnknownCode = _CjnIgmpRxUnknownCode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 2, 4),
    _CjnIgmpRxUnknownCode_Type()
)
cjnIgmpRxUnknownCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpRxUnknownCode.setStatus("current")
_CjnIgmpIfGroup_ObjectIdentity = ObjectIdentity
cjnIgmpIfGroup = _CjnIgmpIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3)
)
_CjnIgmpIfTable_Object = MibTable
cjnIgmpIfTable = _CjnIgmpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1)
)
if mibBuilder.loadTexts:
    cjnIgmpIfTable.setStatus("current")
_CjnIgmpIfEntry_Object = MibTableRow
cjnIgmpIfEntry = _CjnIgmpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1)
)
cjnIgmpIfEntry.setIndexNames(
    (0, "IGMP-PRIVATE-MIB", "cjnIgmpIfIndex"),
)
if mibBuilder.loadTexts:
    cjnIgmpIfEntry.setStatus("current")
_CjnIgmpIfIndex_Type = Integer32
_CjnIgmpIfIndex_Object = MibTableColumn
cjnIgmpIfIndex = _CjnIgmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 1),
    _CjnIgmpIfIndex_Type()
)
cjnIgmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIgmpIfIndex.setStatus("current")
_CjnIgmpIfRowStatus_Type = RowStatus
_CjnIgmpIfRowStatus_Object = MibTableColumn
cjnIgmpIfRowStatus = _CjnIgmpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 2),
    _CjnIgmpIfRowStatus_Type()
)
cjnIgmpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfRowStatus.setStatus("current")


class _CjnIgmpIfIsVersion_Type(Integer32):
    """Custom type cjnIgmpIfIsVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_CjnIgmpIfIsVersion_Type.__name__ = "Integer32"
_CjnIgmpIfIsVersion_Object = MibTableColumn
cjnIgmpIfIsVersion = _CjnIgmpIfIsVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 3),
    _CjnIgmpIfIsVersion_Type()
)
cjnIgmpIfIsVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfIsVersion.setStatus("current")


class _CjnIgmpIfMaxGroups_Type(Integer32):
    """Custom type cjnIgmpIfMaxGroups based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CjnIgmpIfMaxGroups_Type.__name__ = "Integer32"
_CjnIgmpIfMaxGroups_Object = MibTableColumn
cjnIgmpIfMaxGroups = _CjnIgmpIfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 4),
    _CjnIgmpIfMaxGroups_Type()
)
cjnIgmpIfMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfMaxGroups.setStatus("current")


class _CjnIgmpIfIsQuerier_Type(Integer32):
    """Custom type cjnIgmpIfIsQuerier based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CjnIgmpIfIsQuerier_Type.__name__ = "Integer32"
_CjnIgmpIfIsQuerier_Object = MibTableColumn
cjnIgmpIfIsQuerier = _CjnIgmpIfIsQuerier_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 5),
    _CjnIgmpIfIsQuerier_Type()
)
cjnIgmpIfIsQuerier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfIsQuerier.setStatus("current")


class _CjnIgmpIfProcessLeaves_Type(Integer32):
    """Custom type cjnIgmpIfProcessLeaves based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CjnIgmpIfProcessLeaves_Type.__name__ = "Integer32"
_CjnIgmpIfProcessLeaves_Object = MibTableColumn
cjnIgmpIfProcessLeaves = _CjnIgmpIfProcessLeaves_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 6),
    _CjnIgmpIfProcessLeaves_Type()
)
cjnIgmpIfProcessLeaves.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfProcessLeaves.setStatus("current")


class _CjnIgmpIfQueryReqIntvl_Type(Integer32):
    """Custom type cjnIgmpIfQueryReqIntvl based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CjnIgmpIfQueryReqIntvl_Type.__name__ = "Integer32"
_CjnIgmpIfQueryReqIntvl_Object = MibTableColumn
cjnIgmpIfQueryReqIntvl = _CjnIgmpIfQueryReqIntvl_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 7),
    _CjnIgmpIfQueryReqIntvl_Type()
)
cjnIgmpIfQueryReqIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfQueryReqIntvl.setStatus("current")


class _CjnIgmpIfQueryRspIntvl_Type(Integer32):
    """Custom type cjnIgmpIfQueryRspIntvl based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_CjnIgmpIfQueryRspIntvl_Type.__name__ = "Integer32"
_CjnIgmpIfQueryRspIntvl_Object = MibTableColumn
cjnIgmpIfQueryRspIntvl = _CjnIgmpIfQueryRspIntvl_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 8),
    _CjnIgmpIfQueryRspIntvl_Type()
)
cjnIgmpIfQueryRspIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfQueryRspIntvl.setStatus("current")


class _CjnIgmpIfNbrQueryTimeout_Type(Integer32):
    """Custom type cjnIgmpIfNbrQueryTimeout based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_CjnIgmpIfNbrQueryTimeout_Type.__name__ = "Integer32"
_CjnIgmpIfNbrQueryTimeout_Object = MibTableColumn
cjnIgmpIfNbrQueryTimeout = _CjnIgmpIfNbrQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 9),
    _CjnIgmpIfNbrQueryTimeout_Type()
)
cjnIgmpIfNbrQueryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfNbrQueryTimeout.setStatus("current")


class _CjnIgmpIfRobustVariable_Type(Integer32):
    """Custom type cjnIgmpIfRobustVariable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CjnIgmpIfRobustVariable_Type.__name__ = "Integer32"
_CjnIgmpIfRobustVariable_Object = MibTableColumn
cjnIgmpIfRobustVariable = _CjnIgmpIfRobustVariable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 10),
    _CjnIgmpIfRobustVariable_Type()
)
cjnIgmpIfRobustVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfRobustVariable.setStatus("current")


class _CjnIgmpIfState_Type(Integer32):
    """Custom type cjnIgmpIfState based on Integer32"""
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
        *(("down", 0),
          ("init", 1),
          ("nonQuerier", 3),
          ("querier", 2))
    )


_CjnIgmpIfState_Type.__name__ = "Integer32"
_CjnIgmpIfState_Object = MibTableColumn
cjnIgmpIfState = _CjnIgmpIfState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 3, 1, 1, 11),
    _CjnIgmpIfState_Type()
)
cjnIgmpIfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIgmpIfState.setStatus("current")
_CjnIgmpIfStatGroup_ObjectIdentity = ObjectIdentity
cjnIgmpIfStatGroup = _CjnIgmpIfStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4)
)
_CjnIgmpIfStatTable_Object = MibTable
cjnIgmpIfStatTable = _CjnIgmpIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1)
)
if mibBuilder.loadTexts:
    cjnIgmpIfStatTable.setStatus("current")
_CjnIgmpIfStatEntry_Object = MibTableRow
cjnIgmpIfStatEntry = _CjnIgmpIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1)
)
cjnIgmpIfStatEntry.setIndexNames(
    (0, "IGMP-PRIVATE-MIB", "cjnIgmpIfIndex"),
)
if mibBuilder.loadTexts:
    cjnIgmpIfStatEntry.setStatus("current")
_CjnIgmpIfQval_Type = Integer32
_CjnIgmpIfQval_Object = MibTableColumn
cjnIgmpIfQval = _CjnIgmpIfQval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 1),
    _CjnIgmpIfQval_Type()
)
cjnIgmpIfQval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIfQval.setStatus("current")
_CjnIgmpIfQpval_Type = Integer32
_CjnIgmpIfQpval_Object = MibTableColumn
cjnIgmpIfQpval = _CjnIgmpIfQpval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 2),
    _CjnIgmpIfQpval_Type()
)
cjnIgmpIfQpval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIfQpval.setStatus("current")
_CjnIgmpIfJoins_Type = Integer32
_CjnIgmpIfJoins_Object = MibTableColumn
cjnIgmpIfJoins = _CjnIgmpIfJoins_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 3),
    _CjnIgmpIfJoins_Type()
)
cjnIgmpIfJoins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIfJoins.setStatus("current")
_CjnIgmpIfLeaves_Type = Integer32
_CjnIgmpIfLeaves_Object = MibTableColumn
cjnIgmpIfLeaves = _CjnIgmpIfLeaves_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 4),
    _CjnIgmpIfLeaves_Type()
)
cjnIgmpIfLeaves.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIfLeaves.setStatus("current")
_CjnIgmpIfRptRcvd_Type = Integer32
_CjnIgmpIfRptRcvd_Object = MibTableColumn
cjnIgmpIfRptRcvd = _CjnIgmpIfRptRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 5),
    _CjnIgmpIfRptRcvd_Type()
)
cjnIgmpIfRptRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIfRptRcvd.setStatus("current")
_CjnIgmpIfQueryRcvd_Type = Integer32
_CjnIgmpIfQueryRcvd_Object = MibTableColumn
cjnIgmpIfQueryRcvd = _CjnIgmpIfQueryRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 6),
    _CjnIgmpIfQueryRcvd_Type()
)
cjnIgmpIfQueryRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIfQueryRcvd.setStatus("current")
_CjnIgmpIfQueryXmit_Type = Integer32
_CjnIgmpIfQueryXmit_Object = MibTableColumn
cjnIgmpIfQueryXmit = _CjnIgmpIfQueryXmit_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 7),
    _CjnIgmpIfQueryXmit_Type()
)
cjnIgmpIfQueryXmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIfQueryXmit.setStatus("current")
_CjnIgmpIfWrongVer_Type = Integer32
_CjnIgmpIfWrongVer_Object = MibTableColumn
cjnIgmpIfWrongVer = _CjnIgmpIfWrongVer_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 8),
    _CjnIgmpIfWrongVer_Type()
)
cjnIgmpIfWrongVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIfWrongVer.setStatus("current")
_CjnIgmpIfCurGrps_Type = Integer32
_CjnIgmpIfCurGrps_Object = MibTableColumn
cjnIgmpIfCurGrps = _CjnIgmpIfCurGrps_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 11, 4, 1, 1, 9),
    _CjnIgmpIfCurGrps_Type()
)
cjnIgmpIfCurGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIgmpIfCurGrps.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IGMP-PRIVATE-MIB",
    **{"cjnIgmp": cjnIgmp,
       "cjnIgmpGblGroup": cjnIgmpGblGroup,
       "cjnIgmpIsEnabled": cjnIgmpIsEnabled,
       "cjnIpIgmpGblStatsReset": cjnIpIgmpGblStatsReset,
       "cjnIgmpGblStatsGroup": cjnIgmpGblStatsGroup,
       "cjnIgmpRxReport": cjnIgmpRxReport,
       "cjnIgmpRxQuery": cjnIgmpRxQuery,
       "cjnIgmpTxQuery": cjnIgmpTxQuery,
       "cjnIgmpRxUnknownCode": cjnIgmpRxUnknownCode,
       "cjnIgmpIfGroup": cjnIgmpIfGroup,
       "cjnIgmpIfTable": cjnIgmpIfTable,
       "cjnIgmpIfEntry": cjnIgmpIfEntry,
       "cjnIgmpIfIndex": cjnIgmpIfIndex,
       "cjnIgmpIfRowStatus": cjnIgmpIfRowStatus,
       "cjnIgmpIfIsVersion": cjnIgmpIfIsVersion,
       "cjnIgmpIfMaxGroups": cjnIgmpIfMaxGroups,
       "cjnIgmpIfIsQuerier": cjnIgmpIfIsQuerier,
       "cjnIgmpIfProcessLeaves": cjnIgmpIfProcessLeaves,
       "cjnIgmpIfQueryReqIntvl": cjnIgmpIfQueryReqIntvl,
       "cjnIgmpIfQueryRspIntvl": cjnIgmpIfQueryRspIntvl,
       "cjnIgmpIfNbrQueryTimeout": cjnIgmpIfNbrQueryTimeout,
       "cjnIgmpIfRobustVariable": cjnIgmpIfRobustVariable,
       "cjnIgmpIfState": cjnIgmpIfState,
       "cjnIgmpIfStatGroup": cjnIgmpIfStatGroup,
       "cjnIgmpIfStatTable": cjnIgmpIfStatTable,
       "cjnIgmpIfStatEntry": cjnIgmpIfStatEntry,
       "cjnIgmpIfQval": cjnIgmpIfQval,
       "cjnIgmpIfQpval": cjnIgmpIfQpval,
       "cjnIgmpIfJoins": cjnIgmpIfJoins,
       "cjnIgmpIfLeaves": cjnIgmpIfLeaves,
       "cjnIgmpIfRptRcvd": cjnIgmpIfRptRcvd,
       "cjnIgmpIfQueryRcvd": cjnIgmpIfQueryRcvd,
       "cjnIgmpIfQueryXmit": cjnIgmpIfQueryXmit,
       "cjnIgmpIfWrongVer": cjnIgmpIfWrongVer,
       "cjnIgmpIfCurGrps": cjnIgmpIfCurGrps}
)
