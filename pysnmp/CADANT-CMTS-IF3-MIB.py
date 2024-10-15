# SNMP MIB module (CADANT-CMTS-IF3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-IF3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:31 2024
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

(cadIfMacDomainIfIndex,) = mibBuilder.importSymbols(
    "CADANT-CMTS-LAYER2CMTS-MIB",
    "cadIfMacDomainIfIndex")

(cadIfCmtsCmStatusMacAddress,) = mibBuilder.importSymbols(
    "CADANT-CMTS-MAC-MIB",
    "cadIfCmtsCmStatusMacAddress")

(cadCmtsIf3,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadCmtsIf3")

(DocsEqualizerData,
 DocsisQosVersion,
 DocsisUpstreamType,
 TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "DocsEqualizerData",
    "DocsisQosVersion",
    "DocsisUpstreamType",
    "TenthdB",
    "TenthdBmV")

(ChSetId,
 ChannelList,
 Dsid,
 IfDirection,
 RangingState,
 RcpId,
 docsIf3DsChSetId,
 docsIf3UsChSetId) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "ChSetId",
    "ChannelList",
    "Dsid",
    "IfDirection",
    "RangingState",
    "RcpId",
    "docsIf3DsChSetId",
    "docsIf3UsChSetId")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cadCmtsIf3Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1)
)
cadCmtsIf3Mib.setRevisions(
        ("2015-11-05 00:00",
         "2015-10-29 00:00",
         "2015-04-06 00:00",
         "2015-03-10 00:00",
         "2015-02-27 00:00",
         "2014-02-24 00:00",
         "2013-11-05 00:00",
         "2011-01-18 00:00",
         "2010-07-02 00:00",
         "2010-05-04 00:00",
         "2010-01-29 00:00",
         "2009-08-25 00:00",
         "2008-08-21 00:00",
         "2008-07-30 00:00",
         "2008-04-15 00:00",
         "2008-02-15 00:00",
         "2007-12-12 00:00",
         "2007-11-07 00:00",
         "2007-09-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HhMmSs(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d:1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class CmStatusEventTypeCode(Integer32, TextualConvention):
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
              10,
              16,
              18,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("cmAcPowerRestored", 10),
          ("cmOnBatteryBackup", 9),
          ("dpdMismatch", 18),
          ("mddRecovery", 4),
          ("ncpProfileFailure", 20),
          ("ncpProfileRecovery", 22),
          ("ofdmProfileFailure", 16),
          ("ofdmProfileRecovery", 24),
          ("plcFecLockFailure", 21),
          ("plcFecLockRecovery", 23),
          ("qamFecLockFailure", 2),
          ("qamFecLockRecovery", 5),
          ("secondaryChlMddTimeout", 1),
          ("seqOutOfRange", 3),
          ("t3RangingRecovery", 8),
          ("t3RetriesExceeded", 7),
          ("t4Timeout", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CadCmtsIf3MibObjects_ObjectIdentity = ObjectIdentity
cadCmtsIf3MibObjects = _CadCmtsIf3MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1)
)
_CadCmStatusMdCfgTable_Object = MibTable
cadCmStatusMdCfgTable = _CadCmStatusMdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cadCmStatusMdCfgTable.setStatus("current")
_CadCmStatusMdCfgEntry_Object = MibTableRow
cadCmStatusMdCfgEntry = _CadCmStatusMdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 1, 1)
)
cadCmStatusMdCfgEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex"),
    (0, "CADANT-CMTS-IF3-MIB", "cadCmStatusEventTypeCode"),
)
if mibBuilder.loadTexts:
    cadCmStatusMdCfgEntry.setStatus("current")
_CadCmStatusEventTypeCode_Type = CmStatusEventTypeCode
_CadCmStatusEventTypeCode_Object = MibTableColumn
cadCmStatusEventTypeCode = _CadCmStatusEventTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 1, 1, 1),
    _CadCmStatusEventTypeCode_Type()
)
cadCmStatusEventTypeCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCmStatusEventTypeCode.setStatus("current")


class _CadCmStatusEventDescription_Type(DisplayString):
    """Custom type cadCmStatusEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CadCmStatusEventDescription_Type.__name__ = "DisplayString"
_CadCmStatusEventDescription_Object = MibTableColumn
cadCmStatusEventDescription = _CadCmStatusEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 1, 1, 2),
    _CadCmStatusEventDescription_Type()
)
cadCmStatusEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmStatusEventDescription.setStatus("current")


class _CadCmStatusEventEnabled_Type(TruthValue):
    """Custom type cadCmStatusEventEnabled based on TruthValue"""


_CadCmStatusEventEnabled_Object = MibTableColumn
cadCmStatusEventEnabled = _CadCmStatusEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 1, 1, 3),
    _CadCmStatusEventEnabled_Type()
)
cadCmStatusEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmStatusEventEnabled.setStatus("current")


class _CadCmStatusMaxEventHoldoff_Type(Integer32):
    """Custom type cadCmStatusMaxEventHoldoff based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CadCmStatusMaxEventHoldoff_Type.__name__ = "Integer32"
_CadCmStatusMaxEventHoldoff_Object = MibTableColumn
cadCmStatusMaxEventHoldoff = _CadCmStatusMaxEventHoldoff_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 1, 1, 4),
    _CadCmStatusMaxEventHoldoff_Type()
)
cadCmStatusMaxEventHoldoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmStatusMaxEventHoldoff.setStatus("current")
if mibBuilder.loadTexts:
    cadCmStatusMaxEventHoldoff.setUnits("20 millisecond increments")


class _CadCmStatusMaxNumReports_Type(Integer32):
    """Custom type cadCmStatusMaxNumReports based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadCmStatusMaxNumReports_Type.__name__ = "Integer32"
_CadCmStatusMaxNumReports_Object = MibTableColumn
cadCmStatusMaxNumReports = _CadCmStatusMaxNumReports_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 1, 1, 5),
    _CadCmStatusMaxNumReports_Type()
)
cadCmStatusMaxNumReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmStatusMaxNumReports.setStatus("current")
_CadCmtsCmCtrlStatusOverrideCfgTable_Object = MibTable
cadCmtsCmCtrlStatusOverrideCfgTable = _CadCmtsCmCtrlStatusOverrideCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cadCmtsCmCtrlStatusOverrideCfgTable.setStatus("current")
_CadCmtsCmCtrlStatusOverrideCfgEntry_Object = MibTableRow
cadCmtsCmCtrlStatusOverrideCfgEntry = _CadCmtsCmCtrlStatusOverrideCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 2, 1)
)
cadCmtsCmCtrlStatusOverrideCfgEntry.setIndexNames(
    (0, "CADANT-CMTS-IF3-MIB", "cadCmtsCmCtrlStatusMacAddress"),
    (0, "CADANT-CMTS-IF3-MIB", "cadCmtsCmCtrlStatusEventTypeCode"),
)
if mibBuilder.loadTexts:
    cadCmtsCmCtrlStatusOverrideCfgEntry.setStatus("current")
_CadCmtsCmCtrlStatusMacAddress_Type = MacAddress
_CadCmtsCmCtrlStatusMacAddress_Object = MibTableColumn
cadCmtsCmCtrlStatusMacAddress = _CadCmtsCmCtrlStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 2, 1, 1),
    _CadCmtsCmCtrlStatusMacAddress_Type()
)
cadCmtsCmCtrlStatusMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCmtsCmCtrlStatusMacAddress.setStatus("current")
_CadCmtsCmCtrlStatusEventTypeCode_Type = CmStatusEventTypeCode
_CadCmtsCmCtrlStatusEventTypeCode_Object = MibTableColumn
cadCmtsCmCtrlStatusEventTypeCode = _CadCmtsCmCtrlStatusEventTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 2, 1, 2),
    _CadCmtsCmCtrlStatusEventTypeCode_Type()
)
cadCmtsCmCtrlStatusEventTypeCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCmtsCmCtrlStatusEventTypeCode.setStatus("current")
_CadCmtsCmCtrlStatusOverrideEnabled_Type = TruthValue
_CadCmtsCmCtrlStatusOverrideEnabled_Object = MibTableColumn
cadCmtsCmCtrlStatusOverrideEnabled = _CadCmtsCmCtrlStatusOverrideEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 2, 1, 3),
    _CadCmtsCmCtrlStatusOverrideEnabled_Type()
)
cadCmtsCmCtrlStatusOverrideEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCmtsCmCtrlStatusOverrideEnabled.setStatus("current")


class _CadCmtsCmCtrlStatusOverrideDsChList_Type(OctetString):
    """Custom type cadCmtsCmCtrlStatusOverrideDsChList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadCmtsCmCtrlStatusOverrideDsChList_Type.__name__ = "OctetString"
_CadCmtsCmCtrlStatusOverrideDsChList_Object = MibTableColumn
cadCmtsCmCtrlStatusOverrideDsChList = _CadCmtsCmCtrlStatusOverrideDsChList_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 2, 1, 4),
    _CadCmtsCmCtrlStatusOverrideDsChList_Type()
)
cadCmtsCmCtrlStatusOverrideDsChList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCmtsCmCtrlStatusOverrideDsChList.setStatus("current")


class _CadCmtsCmCtrlStatusOverrideUsChList_Type(OctetString):
    """Custom type cadCmtsCmCtrlStatusOverrideUsChList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CadCmtsCmCtrlStatusOverrideUsChList_Type.__name__ = "OctetString"
_CadCmtsCmCtrlStatusOverrideUsChList_Object = MibTableColumn
cadCmtsCmCtrlStatusOverrideUsChList = _CadCmtsCmCtrlStatusOverrideUsChList_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 2, 1, 5),
    _CadCmtsCmCtrlStatusOverrideUsChList_Type()
)
cadCmtsCmCtrlStatusOverrideUsChList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCmtsCmCtrlStatusOverrideUsChList.setStatus("current")
_CadCmtsCmCtrlStatusRowStatus_Type = RowStatus
_CadCmtsCmCtrlStatusRowStatus_Object = MibTableColumn
cadCmtsCmCtrlStatusRowStatus = _CadCmtsCmCtrlStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 2, 1, 6),
    _CadCmtsCmCtrlStatusRowStatus_Type()
)
cadCmtsCmCtrlStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadCmtsCmCtrlStatusRowStatus.setStatus("current")
_CadCmStatusCountsTable_Object = MibTable
cadCmStatusCountsTable = _CadCmStatusCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cadCmStatusCountsTable.setStatus("current")
_CadCmStatusCountsEntry_Object = MibTableRow
cadCmStatusCountsEntry = _CadCmStatusCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3, 1)
)
cadCmStatusCountsEntry.setIndexNames(
    (0, "CADANT-CMTS-IF3-MIB", "cadCmStatusCountsCmMacAddress"),
    (0, "CADANT-CMTS-IF3-MIB", "cadCmStatusEventTypeCode"),
)
if mibBuilder.loadTexts:
    cadCmStatusCountsEntry.setStatus("current")
_CadCmStatusCountsCmMacAddress_Type = MacAddress
_CadCmStatusCountsCmMacAddress_Object = MibTableColumn
cadCmStatusCountsCmMacAddress = _CadCmStatusCountsCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3, 1, 1),
    _CadCmStatusCountsCmMacAddress_Type()
)
cadCmStatusCountsCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCmStatusCountsCmMacAddress.setStatus("current")
_CadCmStatusCountsEventTypeCode_Type = CmStatusEventTypeCode
_CadCmStatusCountsEventTypeCode_Object = MibTableColumn
cadCmStatusCountsEventTypeCode = _CadCmStatusCountsEventTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3, 1, 2),
    _CadCmStatusCountsEventTypeCode_Type()
)
cadCmStatusCountsEventTypeCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadCmStatusCountsEventTypeCode.setStatus("current")


class _CadCmStatusCountsEventDescription_Type(DisplayString):
    """Custom type cadCmStatusCountsEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CadCmStatusCountsEventDescription_Type.__name__ = "DisplayString"
_CadCmStatusCountsEventDescription_Object = MibTableColumn
cadCmStatusCountsEventDescription = _CadCmStatusCountsEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3, 1, 3),
    _CadCmStatusCountsEventDescription_Type()
)
cadCmStatusCountsEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmStatusCountsEventDescription.setStatus("current")
_CadCmStatusCountsEventCount_Type = Counter64
_CadCmStatusCountsEventCount_Object = MibTableColumn
cadCmStatusCountsEventCount = _CadCmStatusCountsEventCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3, 1, 4),
    _CadCmStatusCountsEventCount_Type()
)
cadCmStatusCountsEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmStatusCountsEventCount.setStatus("current")
_CadCmStatusCountsReportedDsChIfIndex_Type = InterfaceIndexOrZero
_CadCmStatusCountsReportedDsChIfIndex_Object = MibTableColumn
cadCmStatusCountsReportedDsChIfIndex = _CadCmStatusCountsReportedDsChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3, 1, 5),
    _CadCmStatusCountsReportedDsChIfIndex_Type()
)
cadCmStatusCountsReportedDsChIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmStatusCountsReportedDsChIfIndex.setStatus("current")
_CadCmStatusCountsReportedUsChIfIndex_Type = InterfaceIndexOrZero
_CadCmStatusCountsReportedUsChIfIndex_Object = MibTableColumn
cadCmStatusCountsReportedUsChIfIndex = _CadCmStatusCountsReportedUsChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3, 1, 6),
    _CadCmStatusCountsReportedUsChIfIndex_Type()
)
cadCmStatusCountsReportedUsChIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmStatusCountsReportedUsChIfIndex.setStatus("current")
_CadCmStatusCountsReportedDsid_Type = Dsid
_CadCmStatusCountsReportedDsid_Object = MibTableColumn
cadCmStatusCountsReportedDsid = _CadCmStatusCountsReportedDsid_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3, 1, 7),
    _CadCmStatusCountsReportedDsid_Type()
)
cadCmStatusCountsReportedDsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmStatusCountsReportedDsid.setStatus("current")
_CadCmStatusCountsTimeStamp_Type = TimeStamp
_CadCmStatusCountsTimeStamp_Object = MibTableColumn
cadCmStatusCountsTimeStamp = _CadCmStatusCountsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 3, 1, 8),
    _CadCmStatusCountsTimeStamp_Type()
)
cadCmStatusCountsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmStatusCountsTimeStamp.setStatus("current")
_CadCmtsCmRepairParamTable_Object = MibTable
cadCmtsCmRepairParamTable = _CadCmtsCmRepairParamTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cadCmtsCmRepairParamTable.setStatus("current")
_CadCmtsCmRepairParamEntry_Object = MibTableRow
cadCmtsCmRepairParamEntry = _CadCmtsCmRepairParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 4, 1)
)
cadCmtsCmRepairParamEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex"),
)
if mibBuilder.loadTexts:
    cadCmtsCmRepairParamEntry.setStatus("current")
_CadCmtsCmRepairEnabled_Type = TruthValue
_CadCmtsCmRepairEnabled_Object = MibTableColumn
cadCmtsCmRepairEnabled = _CadCmtsCmRepairEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 4, 1, 1),
    _CadCmtsCmRepairEnabled_Type()
)
cadCmtsCmRepairEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsCmRepairEnabled.setStatus("current")
_CadCmtsCmRepairWindowStartTime_Type = HhMmSs
_CadCmtsCmRepairWindowStartTime_Object = MibTableColumn
cadCmtsCmRepairWindowStartTime = _CadCmtsCmRepairWindowStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 4, 1, 2),
    _CadCmtsCmRepairWindowStartTime_Type()
)
cadCmtsCmRepairWindowStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsCmRepairWindowStartTime.setStatus("current")
_CadCmtsCmRepairWindowEndTime_Type = HhMmSs
_CadCmtsCmRepairWindowEndTime_Object = MibTableColumn
cadCmtsCmRepairWindowEndTime = _CadCmtsCmRepairWindowEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 4, 1, 3),
    _CadCmtsCmRepairWindowEndTime_Type()
)
cadCmtsCmRepairWindowEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsCmRepairWindowEndTime.setStatus("current")
_CadCmtsCmRepairInterval_Type = HhMmSs
_CadCmtsCmRepairInterval_Object = MibTableColumn
cadCmtsCmRepairInterval = _CadCmtsCmRepairInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 4, 1, 4),
    _CadCmtsCmRepairInterval_Type()
)
cadCmtsCmRepairInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadCmtsCmRepairInterval.setStatus("current")
_CadCmtsCmRegImpairedStatusTable_Object = MibTable
cadCmtsCmRegImpairedStatusTable = _CadCmtsCmRegImpairedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cadCmtsCmRegImpairedStatusTable.setStatus("current")
_CadCmtsCmRegImpairedStatusEntry_Object = MibTableRow
cadCmtsCmRegImpairedStatusEntry = _CadCmtsCmRegImpairedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 5, 1)
)
cadCmtsCmRegImpairedStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusMacAddress"),
    (0, "CADANT-CMTS-IF3-MIB", "cadCmtsCmRegImpairedIfIndex"),
    (0, "CADANT-CMTS-IF3-MIB", "cadCmtsCmRegImpairedReason"),
)
if mibBuilder.loadTexts:
    cadCmtsCmRegImpairedStatusEntry.setStatus("current")


class _CadCmtsCmRegImpairedReason_Type(Integer32):
    """Custom type cadCmtsCmRegImpairedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              130,
              150,
              170,
              200,
              300,
              400,
              500,
              600,
              700,
              900)
        )
    )
    namedValues = NamedValues(
        *(("badRcs", 400),
          ("badTcs", 500),
          ("ncpFecLockFailure", 150),
          ("plcFecLockFailure", 130),
          ("prof0FecLockFailure", 170),
          ("qamFecLockFailure", 100),
          ("t3Timeout", 700),
          ("t4Timeout", 600),
          ("unknownMdDsSgId", 200),
          ("unknownMdUsSgId", 300),
          ("usStationMaintFailure", 900))
    )


_CadCmtsCmRegImpairedReason_Type.__name__ = "Integer32"
_CadCmtsCmRegImpairedReason_Object = MibTableColumn
cadCmtsCmRegImpairedReason = _CadCmtsCmRegImpairedReason_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 5, 1, 1),
    _CadCmtsCmRegImpairedReason_Type()
)
cadCmtsCmRegImpairedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmRegImpairedReason.setStatus("current")
_CadCmtsCmRegImpairedFaultDetected_Type = DateAndTime
_CadCmtsCmRegImpairedFaultDetected_Object = MibTableColumn
cadCmtsCmRegImpairedFaultDetected = _CadCmtsCmRegImpairedFaultDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 5, 1, 2),
    _CadCmtsCmRegImpairedFaultDetected_Type()
)
cadCmtsCmRegImpairedFaultDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmRegImpairedFaultDetected.setStatus("current")
_CadCmtsCmRegImpairedLastRepairAttempt_Type = DateAndTime
_CadCmtsCmRegImpairedLastRepairAttempt_Object = MibTableColumn
cadCmtsCmRegImpairedLastRepairAttempt = _CadCmtsCmRegImpairedLastRepairAttempt_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 5, 1, 3),
    _CadCmtsCmRegImpairedLastRepairAttempt_Type()
)
cadCmtsCmRegImpairedLastRepairAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmRegImpairedLastRepairAttempt.setStatus("current")


class _CadCmtsCmRegImpairedLastRepairAction_Type(Integer32):
    """Custom type cadCmtsCmRegImpairedLastRepairAction based on Integer32"""
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
        *(("cmReset", 1),
          ("dbcMessage", 2),
          ("dccMessage", 3),
          ("noAction", 0))
    )


_CadCmtsCmRegImpairedLastRepairAction_Type.__name__ = "Integer32"
_CadCmtsCmRegImpairedLastRepairAction_Object = MibTableColumn
cadCmtsCmRegImpairedLastRepairAction = _CadCmtsCmRegImpairedLastRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 5, 1, 4),
    _CadCmtsCmRegImpairedLastRepairAction_Type()
)
cadCmtsCmRegImpairedLastRepairAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmRegImpairedLastRepairAction.setStatus("current")
_CadCmtsCmRegImpairedIfIndex_Type = InterfaceIndex
_CadCmtsCmRegImpairedIfIndex_Object = MibTableColumn
cadCmtsCmRegImpairedIfIndex = _CadCmtsCmRegImpairedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 5, 1, 5),
    _CadCmtsCmRegImpairedIfIndex_Type()
)
cadCmtsCmRegImpairedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadCmtsCmRegImpairedIfIndex.setStatus("current")
_CadIf3CmtsCmUsStatusTable_Object = MibTable
cadIf3CmtsCmUsStatusTable = _CadIf3CmtsCmUsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cadIf3CmtsCmUsStatusTable.setStatus("current")
_CadIf3CmtsCmUsStatusEntry_Object = MibTableRow
cadIf3CmtsCmUsStatusEntry = _CadIf3CmtsCmUsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 6, 1)
)
cadIf3CmtsCmUsStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-MAC-MIB", "cadIfCmtsCmStatusMacAddress"),
    (0, "CADANT-CMTS-IF3-MIB", "cadIf3CmtsCmUsStatusChIfIndex"),
)
if mibBuilder.loadTexts:
    cadIf3CmtsCmUsStatusEntry.setStatus("current")
_CadIf3CmtsCmUsStatusChIfIndex_Type = InterfaceIndex
_CadIf3CmtsCmUsStatusChIfIndex_Object = MibTableColumn
cadIf3CmtsCmUsStatusChIfIndex = _CadIf3CmtsCmUsStatusChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 6, 1, 1),
    _CadIf3CmtsCmUsStatusChIfIndex_Type()
)
cadIf3CmtsCmUsStatusChIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIf3CmtsCmUsStatusChIfIndex.setStatus("current")
_CadIf3CmtsCmUsStatusModulationType_Type = DocsisUpstreamType
_CadIf3CmtsCmUsStatusModulationType_Object = MibTableColumn
cadIf3CmtsCmUsStatusModulationType = _CadIf3CmtsCmUsStatusModulationType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 6, 1, 2),
    _CadIf3CmtsCmUsStatusModulationType_Type()
)
cadIf3CmtsCmUsStatusModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmUsStatusModulationType.setStatus("current")
_CadIf3CmtsCmUsStatusIsMuted_Type = TruthValue
_CadIf3CmtsCmUsStatusIsMuted_Object = MibTableColumn
cadIf3CmtsCmUsStatusIsMuted = _CadIf3CmtsCmUsStatusIsMuted_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 6, 1, 11),
    _CadIf3CmtsCmUsStatusIsMuted_Type()
)
cadIf3CmtsCmUsStatusIsMuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmUsStatusIsMuted.setStatus("current")
_CadIf3CmtsCmUsStatusRangingStatus_Type = RangingState
_CadIf3CmtsCmUsStatusRangingStatus_Object = MibTableColumn
cadIf3CmtsCmUsStatusRangingStatus = _CadIf3CmtsCmUsStatusRangingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 6, 1, 12),
    _CadIf3CmtsCmUsStatusRangingStatus_Type()
)
cadIf3CmtsCmUsStatusRangingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CmtsCmUsStatusRangingStatus.setStatus("current")
_CadRccStatusTable_Object = MibTable
cadRccStatusTable = _CadRccStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cadRccStatusTable.setStatus("current")
_CadRccStatusEntry_Object = MibTableRow
cadRccStatusEntry = _CadRccStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 7, 1)
)
cadRccStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex"),
    (0, "CADANT-CMTS-IF3-MIB", "cadRccStatusRcpId"),
    (0, "CADANT-CMTS-IF3-MIB", "cadRccStatusId"),
)
if mibBuilder.loadTexts:
    cadRccStatusEntry.setStatus("current")
_CadRccStatusRcpId_Type = RcpId
_CadRccStatusRcpId_Object = MibTableColumn
cadRccStatusRcpId = _CadRccStatusRcpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 7, 1, 1),
    _CadRccStatusRcpId_Type()
)
cadRccStatusRcpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadRccStatusRcpId.setStatus("current")


class _CadRccStatusId_Type(Unsigned32):
    """Custom type cadRccStatusId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CadRccStatusId_Type.__name__ = "Unsigned32"
_CadRccStatusId_Object = MibTableColumn
cadRccStatusId = _CadRccStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 7, 1, 2),
    _CadRccStatusId_Type()
)
cadRccStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadRccStatusId.setStatus("current")


class _CadRccStatusRccCfgId_Type(Unsigned32):
    """Custom type cadRccStatusRccCfgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadRccStatusRccCfgId_Type.__name__ = "Unsigned32"
_CadRccStatusRccCfgId_Object = MibTableColumn
cadRccStatusRccCfgId = _CadRccStatusRccCfgId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 7, 1, 3),
    _CadRccStatusRccCfgId_Type()
)
cadRccStatusRccCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRccStatusRccCfgId.setStatus("current")


class _CadRccStatusValidityCode_Type(Integer32):
    """Custom type cadRccStatusValidityCode based on Integer32"""
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
        *(("duplicateDs", 7),
          ("invalid", 3),
          ("missingPrimaryDs", 5),
          ("multiplePrimaryDs", 6),
          ("other", 1),
          ("valid", 2),
          ("wrongConnectivity", 9),
          ("wrongFrequencyRange", 8),
          ("wrongPrimaryDs", 4))
    )


_CadRccStatusValidityCode_Type.__name__ = "Integer32"
_CadRccStatusValidityCode_Object = MibTableColumn
cadRccStatusValidityCode = _CadRccStatusValidityCode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 7, 1, 4),
    _CadRccStatusValidityCode_Type()
)
cadRccStatusValidityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRccStatusValidityCode.setStatus("current")
_CadRccStatusValidityCodeText_Type = SnmpAdminString
_CadRccStatusValidityCodeText_Object = MibTableColumn
cadRccStatusValidityCodeText = _CadRccStatusValidityCodeText_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 7, 1, 5),
    _CadRccStatusValidityCodeText_Type()
)
cadRccStatusValidityCodeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRccStatusValidityCodeText.setStatus("current")
_CadRccStatusDsChSetId_Type = ChSetId
_CadRccStatusDsChSetId_Object = MibTableColumn
cadRccStatusDsChSetId = _CadRccStatusDsChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 7, 1, 6),
    _CadRccStatusDsChSetId_Type()
)
cadRccStatusDsChSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRccStatusDsChSetId.setStatus("current")
_CadRccStatusChannelCount_Type = Unsigned32
_CadRccStatusChannelCount_Object = MibTableColumn
cadRccStatusChannelCount = _CadRccStatusChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 7, 1, 7),
    _CadRccStatusChannelCount_Type()
)
cadRccStatusChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadRccStatusChannelCount.setStatus("current")
_CadIf3UsChSetTable_Object = MibTable
cadIf3UsChSetTable = _CadIf3UsChSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cadIf3UsChSetTable.setStatus("current")
_CadIf3UsChSetEntry_Object = MibTableRow
cadIf3UsChSetEntry = _CadIf3UsChSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 8, 1)
)
cadIf3UsChSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3UsChSetId"),
    (0, "CADANT-CMTS-IF3-MIB", "cadIf3UsChIfIndex"),
)
if mibBuilder.loadTexts:
    cadIf3UsChSetEntry.setStatus("current")
_CadIf3UsChIfIndex_Type = InterfaceIndex
_CadIf3UsChIfIndex_Object = MibTableColumn
cadIf3UsChIfIndex = _CadIf3UsChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 8, 1, 1),
    _CadIf3UsChIfIndex_Type()
)
cadIf3UsChIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3UsChIfIndex.setStatus("current")
_CadIf3DsChSetTable_Object = MibTable
cadIf3DsChSetTable = _CadIf3DsChSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cadIf3DsChSetTable.setStatus("current")
_CadIf3DsChSetEntry_Object = MibTableRow
cadIf3DsChSetEntry = _CadIf3DsChSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 9, 1)
)
cadIf3DsChSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IF3-MIB", "docsIf3DsChSetId"),
    (0, "CADANT-CMTS-IF3-MIB", "cadIf3DsChIfIndex"),
)
if mibBuilder.loadTexts:
    cadIf3DsChSetEntry.setStatus("current")
_CadIf3DsChIfIndex_Type = InterfaceIndex
_CadIf3DsChIfIndex_Object = MibTableColumn
cadIf3DsChIfIndex = _CadIf3DsChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 9, 1, 1),
    _CadIf3DsChIfIndex_Type()
)
cadIf3DsChIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3DsChIfIndex.setStatus("current")
_CadIf3CsSummaryTable_Object = MibTable
cadIf3CsSummaryTable = _CadIf3CsSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cadIf3CsSummaryTable.setStatus("current")
_CadIf3CsSummaryEntry_Object = MibTableRow
cadIf3CsSummaryEntry = _CadIf3CsSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1)
)
cadIf3CsSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-CMTS-IF3-MIB", "cadIf3CsDir"),
    (0, "CADANT-CMTS-IF3-MIB", "cadIf3CsId"),
)
if mibBuilder.loadTexts:
    cadIf3CsSummaryEntry.setStatus("deprecated")
_CadIf3CsDir_Type = IfDirection
_CadIf3CsDir_Object = MibTableColumn
cadIf3CsDir = _CadIf3CsDir_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 1),
    _CadIf3CsDir_Type()
)
cadIf3CsDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIf3CsDir.setStatus("deprecated")
_CadIf3CsId_Type = ChSetId
_CadIf3CsId_Object = MibTableColumn
cadIf3CsId = _CadIf3CsId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 2),
    _CadIf3CsId_Type()
)
cadIf3CsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIf3CsId.setStatus("deprecated")
_CadIf3CsNumOther_Type = Integer32
_CadIf3CsNumOther_Object = MibTableColumn
cadIf3CsNumOther = _CadIf3CsNumOther_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 3),
    _CadIf3CsNumOther_Type()
)
cadIf3CsNumOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumOther.setStatus("deprecated")
_CadIf3CsNumInitRanging_Type = Integer32
_CadIf3CsNumInitRanging_Object = MibTableColumn
cadIf3CsNumInitRanging = _CadIf3CsNumInitRanging_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 4),
    _CadIf3CsNumInitRanging_Type()
)
cadIf3CsNumInitRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumInitRanging.setStatus("deprecated")
_CadIf3CsNumRangingComplete_Type = Integer32
_CadIf3CsNumRangingComplete_Object = MibTableColumn
cadIf3CsNumRangingComplete = _CadIf3CsNumRangingComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 5),
    _CadIf3CsNumRangingComplete_Type()
)
cadIf3CsNumRangingComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumRangingComplete.setStatus("deprecated")
_CadIf3CsNumStartEae_Type = Integer32
_CadIf3CsNumStartEae_Object = MibTableColumn
cadIf3CsNumStartEae = _CadIf3CsNumStartEae_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 6),
    _CadIf3CsNumStartEae_Type()
)
cadIf3CsNumStartEae.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumStartEae.setStatus("deprecated")
_CadIf3CsNumStartDhcpv4_Type = Integer32
_CadIf3CsNumStartDhcpv4_Object = MibTableColumn
cadIf3CsNumStartDhcpv4 = _CadIf3CsNumStartDhcpv4_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 7),
    _CadIf3CsNumStartDhcpv4_Type()
)
cadIf3CsNumStartDhcpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumStartDhcpv4.setStatus("deprecated")
_CadIf3CsNumStartDhcpv6_Type = Integer32
_CadIf3CsNumStartDhcpv6_Object = MibTableColumn
cadIf3CsNumStartDhcpv6 = _CadIf3CsNumStartDhcpv6_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 8),
    _CadIf3CsNumStartDhcpv6_Type()
)
cadIf3CsNumStartDhcpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumStartDhcpv6.setStatus("deprecated")
_CadIf3CsNumDhcpv4Complete_Type = Integer32
_CadIf3CsNumDhcpv4Complete_Object = MibTableColumn
cadIf3CsNumDhcpv4Complete = _CadIf3CsNumDhcpv4Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 9),
    _CadIf3CsNumDhcpv4Complete_Type()
)
cadIf3CsNumDhcpv4Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumDhcpv4Complete.setStatus("deprecated")
_CadIf3CsNumDhcpv6Complete_Type = Integer32
_CadIf3CsNumDhcpv6Complete_Object = MibTableColumn
cadIf3CsNumDhcpv6Complete = _CadIf3CsNumDhcpv6Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 10),
    _CadIf3CsNumDhcpv6Complete_Type()
)
cadIf3CsNumDhcpv6Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumDhcpv6Complete.setStatus("deprecated")
_CadIf3CsNumStartCfgFileDownload_Type = Integer32
_CadIf3CsNumStartCfgFileDownload_Object = MibTableColumn
cadIf3CsNumStartCfgFileDownload = _CadIf3CsNumStartCfgFileDownload_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 11),
    _CadIf3CsNumStartCfgFileDownload_Type()
)
cadIf3CsNumStartCfgFileDownload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumStartCfgFileDownload.setStatus("deprecated")
_CadIf3CsNumCfgFileDownloadComplete_Type = Integer32
_CadIf3CsNumCfgFileDownloadComplete_Object = MibTableColumn
cadIf3CsNumCfgFileDownloadComplete = _CadIf3CsNumCfgFileDownloadComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 12),
    _CadIf3CsNumCfgFileDownloadComplete_Type()
)
cadIf3CsNumCfgFileDownloadComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumCfgFileDownloadComplete.setStatus("deprecated")
_CadIf3CsNumStartRegistration_Type = Integer32
_CadIf3CsNumStartRegistration_Object = MibTableColumn
cadIf3CsNumStartRegistration = _CadIf3CsNumStartRegistration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 13),
    _CadIf3CsNumStartRegistration_Type()
)
cadIf3CsNumStartRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumStartRegistration.setStatus("deprecated")
_CadIf3CsNumRegistrationComplete_Type = Integer32
_CadIf3CsNumRegistrationComplete_Object = MibTableColumn
cadIf3CsNumRegistrationComplete = _CadIf3CsNumRegistrationComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 14),
    _CadIf3CsNumRegistrationComplete_Type()
)
cadIf3CsNumRegistrationComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumRegistrationComplete.setStatus("deprecated")
_CadIf3CsNumOperational_Type = Integer32
_CadIf3CsNumOperational_Object = MibTableColumn
cadIf3CsNumOperational = _CadIf3CsNumOperational_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 15),
    _CadIf3CsNumOperational_Type()
)
cadIf3CsNumOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumOperational.setStatus("deprecated")
_CadIf3CsNumBpiInit_Type = Integer32
_CadIf3CsNumBpiInit_Object = MibTableColumn
cadIf3CsNumBpiInit = _CadIf3CsNumBpiInit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 16),
    _CadIf3CsNumBpiInit_Type()
)
cadIf3CsNumBpiInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumBpiInit.setStatus("deprecated")
_CadIf3CsNumForwardingDisabled_Type = Integer32
_CadIf3CsNumForwardingDisabled_Object = MibTableColumn
cadIf3CsNumForwardingDisabled = _CadIf3CsNumForwardingDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 17),
    _CadIf3CsNumForwardingDisabled_Type()
)
cadIf3CsNumForwardingDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumForwardingDisabled.setStatus("deprecated")
_CadIf3CsNumRfMuteAll_Type = Integer32
_CadIf3CsNumRfMuteAll_Object = MibTableColumn
cadIf3CsNumRfMuteAll = _CadIf3CsNumRfMuteAll_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 18),
    _CadIf3CsNumRfMuteAll_Type()
)
cadIf3CsNumRfMuteAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumRfMuteAll.setStatus("deprecated")
_CadIf3CsNumTotal_Type = Integer32
_CadIf3CsNumTotal_Object = MibTableColumn
cadIf3CsNumTotal = _CadIf3CsNumTotal_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 19),
    _CadIf3CsNumTotal_Type()
)
cadIf3CsNumTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumTotal.setStatus("deprecated")
_CadIf3CsNumRangingAborted_Type = Integer32
_CadIf3CsNumRangingAborted_Object = MibTableColumn
cadIf3CsNumRangingAborted = _CadIf3CsNumRangingAborted_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 20),
    _CadIf3CsNumRangingAborted_Type()
)
cadIf3CsNumRangingAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumRangingAborted.setStatus("deprecated")
_CadIf3CsNumRangFlaps_Type = Integer32
_CadIf3CsNumRangFlaps_Object = MibTableColumn
cadIf3CsNumRangFlaps = _CadIf3CsNumRangFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 21),
    _CadIf3CsNumRangFlaps_Type()
)
cadIf3CsNumRangFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumRangFlaps.setStatus("deprecated")
_CadIf3CsNumProvFlaps_Type = Integer32
_CadIf3CsNumProvFlaps_Object = MibTableColumn
cadIf3CsNumProvFlaps = _CadIf3CsNumProvFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 22),
    _CadIf3CsNumProvFlaps_Type()
)
cadIf3CsNumProvFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumProvFlaps.setStatus("deprecated")
_CadIf3CsNumRegFlaps_Type = Integer32
_CadIf3CsNumRegFlaps_Object = MibTableColumn
cadIf3CsNumRegFlaps = _CadIf3CsNumRegFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 10, 1, 23),
    _CadIf3CsNumRegFlaps_Type()
)
cadIf3CsNumRegFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3CsNumRegFlaps.setStatus("deprecated")
_CadIf3ChsSummary_ObjectIdentity = ObjectIdentity
cadIf3ChsSummary = _CadIf3ChsSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11)
)
_CadIf3ChsNumOther_Type = Integer32
_CadIf3ChsNumOther_Object = MibScalar
cadIf3ChsNumOther = _CadIf3ChsNumOther_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 3),
    _CadIf3ChsNumOther_Type()
)
cadIf3ChsNumOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumOther.setStatus("deprecated")
_CadIf3ChsNumInitRanging_Type = Integer32
_CadIf3ChsNumInitRanging_Object = MibScalar
cadIf3ChsNumInitRanging = _CadIf3ChsNumInitRanging_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 4),
    _CadIf3ChsNumInitRanging_Type()
)
cadIf3ChsNumInitRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumInitRanging.setStatus("deprecated")
_CadIf3ChsNumRangingComplete_Type = Integer32
_CadIf3ChsNumRangingComplete_Object = MibScalar
cadIf3ChsNumRangingComplete = _CadIf3ChsNumRangingComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 5),
    _CadIf3ChsNumRangingComplete_Type()
)
cadIf3ChsNumRangingComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumRangingComplete.setStatus("deprecated")
_CadIf3ChsNumStartEae_Type = Integer32
_CadIf3ChsNumStartEae_Object = MibScalar
cadIf3ChsNumStartEae = _CadIf3ChsNumStartEae_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 6),
    _CadIf3ChsNumStartEae_Type()
)
cadIf3ChsNumStartEae.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumStartEae.setStatus("deprecated")
_CadIf3ChsNumStartDhcpv4_Type = Integer32
_CadIf3ChsNumStartDhcpv4_Object = MibScalar
cadIf3ChsNumStartDhcpv4 = _CadIf3ChsNumStartDhcpv4_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 7),
    _CadIf3ChsNumStartDhcpv4_Type()
)
cadIf3ChsNumStartDhcpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumStartDhcpv4.setStatus("deprecated")
_CadIf3ChsNumStartDhcpv6_Type = Integer32
_CadIf3ChsNumStartDhcpv6_Object = MibScalar
cadIf3ChsNumStartDhcpv6 = _CadIf3ChsNumStartDhcpv6_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 8),
    _CadIf3ChsNumStartDhcpv6_Type()
)
cadIf3ChsNumStartDhcpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumStartDhcpv6.setStatus("deprecated")
_CadIf3ChsNumDhcpv4Complete_Type = Integer32
_CadIf3ChsNumDhcpv4Complete_Object = MibScalar
cadIf3ChsNumDhcpv4Complete = _CadIf3ChsNumDhcpv4Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 9),
    _CadIf3ChsNumDhcpv4Complete_Type()
)
cadIf3ChsNumDhcpv4Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumDhcpv4Complete.setStatus("deprecated")
_CadIf3ChsNumDhcpv6Complete_Type = Integer32
_CadIf3ChsNumDhcpv6Complete_Object = MibScalar
cadIf3ChsNumDhcpv6Complete = _CadIf3ChsNumDhcpv6Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 10),
    _CadIf3ChsNumDhcpv6Complete_Type()
)
cadIf3ChsNumDhcpv6Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumDhcpv6Complete.setStatus("deprecated")
_CadIf3ChsNumStartCfgFileDownload_Type = Integer32
_CadIf3ChsNumStartCfgFileDownload_Object = MibScalar
cadIf3ChsNumStartCfgFileDownload = _CadIf3ChsNumStartCfgFileDownload_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 11),
    _CadIf3ChsNumStartCfgFileDownload_Type()
)
cadIf3ChsNumStartCfgFileDownload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumStartCfgFileDownload.setStatus("deprecated")
_CadIf3ChsNumCfgFileDownloadComplete_Type = Integer32
_CadIf3ChsNumCfgFileDownloadComplete_Object = MibScalar
cadIf3ChsNumCfgFileDownloadComplete = _CadIf3ChsNumCfgFileDownloadComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 12),
    _CadIf3ChsNumCfgFileDownloadComplete_Type()
)
cadIf3ChsNumCfgFileDownloadComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumCfgFileDownloadComplete.setStatus("deprecated")
_CadIf3ChsNumStartRegistration_Type = Integer32
_CadIf3ChsNumStartRegistration_Object = MibScalar
cadIf3ChsNumStartRegistration = _CadIf3ChsNumStartRegistration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 13),
    _CadIf3ChsNumStartRegistration_Type()
)
cadIf3ChsNumStartRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumStartRegistration.setStatus("deprecated")
_CadIf3ChsNumRegistrationComplete_Type = Integer32
_CadIf3ChsNumRegistrationComplete_Object = MibScalar
cadIf3ChsNumRegistrationComplete = _CadIf3ChsNumRegistrationComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 14),
    _CadIf3ChsNumRegistrationComplete_Type()
)
cadIf3ChsNumRegistrationComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumRegistrationComplete.setStatus("deprecated")
_CadIf3ChsNumOperational_Type = Integer32
_CadIf3ChsNumOperational_Object = MibScalar
cadIf3ChsNumOperational = _CadIf3ChsNumOperational_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 15),
    _CadIf3ChsNumOperational_Type()
)
cadIf3ChsNumOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumOperational.setStatus("deprecated")
_CadIf3ChsNumBpiInit_Type = Integer32
_CadIf3ChsNumBpiInit_Object = MibScalar
cadIf3ChsNumBpiInit = _CadIf3ChsNumBpiInit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 16),
    _CadIf3ChsNumBpiInit_Type()
)
cadIf3ChsNumBpiInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumBpiInit.setStatus("deprecated")
_CadIf3ChsNumForwardingDisabled_Type = Integer32
_CadIf3ChsNumForwardingDisabled_Object = MibScalar
cadIf3ChsNumForwardingDisabled = _CadIf3ChsNumForwardingDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 17),
    _CadIf3ChsNumForwardingDisabled_Type()
)
cadIf3ChsNumForwardingDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumForwardingDisabled.setStatus("deprecated")
_CadIf3ChsNumRfMuteAll_Type = Integer32
_CadIf3ChsNumRfMuteAll_Object = MibScalar
cadIf3ChsNumRfMuteAll = _CadIf3ChsNumRfMuteAll_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 18),
    _CadIf3ChsNumRfMuteAll_Type()
)
cadIf3ChsNumRfMuteAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumRfMuteAll.setStatus("deprecated")
_CadIf3ChsNumTotal_Type = Integer32
_CadIf3ChsNumTotal_Object = MibScalar
cadIf3ChsNumTotal = _CadIf3ChsNumTotal_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 19),
    _CadIf3ChsNumTotal_Type()
)
cadIf3ChsNumTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumTotal.setStatus("deprecated")
_CadIf3ChsNumRangingAborted_Type = Integer32
_CadIf3ChsNumRangingAborted_Object = MibScalar
cadIf3ChsNumRangingAborted = _CadIf3ChsNumRangingAborted_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 20),
    _CadIf3ChsNumRangingAborted_Type()
)
cadIf3ChsNumRangingAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumRangingAborted.setStatus("deprecated")
_CadIf3ChsNumRangFlaps_Type = Integer32
_CadIf3ChsNumRangFlaps_Object = MibScalar
cadIf3ChsNumRangFlaps = _CadIf3ChsNumRangFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 21),
    _CadIf3ChsNumRangFlaps_Type()
)
cadIf3ChsNumRangFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumRangFlaps.setStatus("deprecated")
_CadIf3ChsNumProvFlaps_Type = Integer32
_CadIf3ChsNumProvFlaps_Object = MibScalar
cadIf3ChsNumProvFlaps = _CadIf3ChsNumProvFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 22),
    _CadIf3ChsNumProvFlaps_Type()
)
cadIf3ChsNumProvFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumProvFlaps.setStatus("deprecated")
_CadIf3ChsNumRegFlaps_Type = Integer32
_CadIf3ChsNumRegFlaps_Object = MibScalar
cadIf3ChsNumRegFlaps = _CadIf3ChsNumRegFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 11, 23),
    _CadIf3ChsNumRegFlaps_Type()
)
cadIf3ChsNumRegFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIf3ChsNumRegFlaps.setStatus("deprecated")
_CadIfCmtsCmFailedProfStatusTable_Object = MibTable
cadIfCmtsCmFailedProfStatusTable = _CadIfCmtsCmFailedProfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cadIfCmtsCmFailedProfStatusTable.setStatus("current")
_CadIfCmtsCmFailedProfStatusEntry_Object = MibTableRow
cadIfCmtsCmFailedProfStatusEntry = _CadIfCmtsCmFailedProfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 12, 1)
)
cadIfCmtsCmFailedProfStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-IF3-MIB", "cadIfCmtsCmFailedProfMacAddress"),
    (0, "CADANT-CMTS-IF3-MIB", "cadIfCmtsCmFailedProfIfIndex"),
    (0, "CADANT-CMTS-IF3-MIB", "cadIfCmtsCmFailedProfId"),
    (0, "CADANT-CMTS-IF3-MIB", "cadIfCmtsCmFailedProfReason"),
)
if mibBuilder.loadTexts:
    cadIfCmtsCmFailedProfStatusEntry.setStatus("current")
_CadIfCmtsCmFailedProfMacAddress_Type = MacAddress
_CadIfCmtsCmFailedProfMacAddress_Object = MibTableColumn
cadIfCmtsCmFailedProfMacAddress = _CadIfCmtsCmFailedProfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 12, 1, 1),
    _CadIfCmtsCmFailedProfMacAddress_Type()
)
cadIfCmtsCmFailedProfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmFailedProfMacAddress.setStatus("current")
_CadIfCmtsCmFailedProfIfIndex_Type = InterfaceIndex
_CadIfCmtsCmFailedProfIfIndex_Object = MibTableColumn
cadIfCmtsCmFailedProfIfIndex = _CadIfCmtsCmFailedProfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 12, 1, 2),
    _CadIfCmtsCmFailedProfIfIndex_Type()
)
cadIfCmtsCmFailedProfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmFailedProfIfIndex.setStatus("current")


class _CadIfCmtsCmFailedProfId_Type(Integer32):
    """Custom type cadIfCmtsCmFailedProfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_CadIfCmtsCmFailedProfId_Type.__name__ = "Integer32"
_CadIfCmtsCmFailedProfId_Object = MibTableColumn
cadIfCmtsCmFailedProfId = _CadIfCmtsCmFailedProfId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 12, 1, 3),
    _CadIfCmtsCmFailedProfId_Type()
)
cadIfCmtsCmFailedProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmFailedProfId.setStatus("current")


class _CadIfCmtsCmFailedProfReason_Type(Integer32):
    """Custom type cadIfCmtsCmFailedProfReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            300
        )
    )
    namedValues = NamedValues(
        ("lostFecLock", 300)
    )


_CadIfCmtsCmFailedProfReason_Type.__name__ = "Integer32"
_CadIfCmtsCmFailedProfReason_Object = MibTableColumn
cadIfCmtsCmFailedProfReason = _CadIfCmtsCmFailedProfReason_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 12, 1, 4),
    _CadIfCmtsCmFailedProfReason_Type()
)
cadIfCmtsCmFailedProfReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsCmFailedProfReason.setStatus("current")
_CadIfCmtsCmFailedProfFaultDetected_Type = DateAndTime
_CadIfCmtsCmFailedProfFaultDetected_Object = MibTableColumn
cadIfCmtsCmFailedProfFaultDetected = _CadIfCmtsCmFailedProfFaultDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 110, 1, 1, 12, 1, 5),
    _CadIfCmtsCmFailedProfFaultDetected_Type()
)
cadIfCmtsCmFailedProfFaultDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsCmFailedProfFaultDetected.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-IF3-MIB",
    **{"HhMmSs": HhMmSs,
       "CmStatusEventTypeCode": CmStatusEventTypeCode,
       "cadCmtsIf3Mib": cadCmtsIf3Mib,
       "cadCmtsIf3MibObjects": cadCmtsIf3MibObjects,
       "cadCmStatusMdCfgTable": cadCmStatusMdCfgTable,
       "cadCmStatusMdCfgEntry": cadCmStatusMdCfgEntry,
       "cadCmStatusEventTypeCode": cadCmStatusEventTypeCode,
       "cadCmStatusEventDescription": cadCmStatusEventDescription,
       "cadCmStatusEventEnabled": cadCmStatusEventEnabled,
       "cadCmStatusMaxEventHoldoff": cadCmStatusMaxEventHoldoff,
       "cadCmStatusMaxNumReports": cadCmStatusMaxNumReports,
       "cadCmtsCmCtrlStatusOverrideCfgTable": cadCmtsCmCtrlStatusOverrideCfgTable,
       "cadCmtsCmCtrlStatusOverrideCfgEntry": cadCmtsCmCtrlStatusOverrideCfgEntry,
       "cadCmtsCmCtrlStatusMacAddress": cadCmtsCmCtrlStatusMacAddress,
       "cadCmtsCmCtrlStatusEventTypeCode": cadCmtsCmCtrlStatusEventTypeCode,
       "cadCmtsCmCtrlStatusOverrideEnabled": cadCmtsCmCtrlStatusOverrideEnabled,
       "cadCmtsCmCtrlStatusOverrideDsChList": cadCmtsCmCtrlStatusOverrideDsChList,
       "cadCmtsCmCtrlStatusOverrideUsChList": cadCmtsCmCtrlStatusOverrideUsChList,
       "cadCmtsCmCtrlStatusRowStatus": cadCmtsCmCtrlStatusRowStatus,
       "cadCmStatusCountsTable": cadCmStatusCountsTable,
       "cadCmStatusCountsEntry": cadCmStatusCountsEntry,
       "cadCmStatusCountsCmMacAddress": cadCmStatusCountsCmMacAddress,
       "cadCmStatusCountsEventTypeCode": cadCmStatusCountsEventTypeCode,
       "cadCmStatusCountsEventDescription": cadCmStatusCountsEventDescription,
       "cadCmStatusCountsEventCount": cadCmStatusCountsEventCount,
       "cadCmStatusCountsReportedDsChIfIndex": cadCmStatusCountsReportedDsChIfIndex,
       "cadCmStatusCountsReportedUsChIfIndex": cadCmStatusCountsReportedUsChIfIndex,
       "cadCmStatusCountsReportedDsid": cadCmStatusCountsReportedDsid,
       "cadCmStatusCountsTimeStamp": cadCmStatusCountsTimeStamp,
       "cadCmtsCmRepairParamTable": cadCmtsCmRepairParamTable,
       "cadCmtsCmRepairParamEntry": cadCmtsCmRepairParamEntry,
       "cadCmtsCmRepairEnabled": cadCmtsCmRepairEnabled,
       "cadCmtsCmRepairWindowStartTime": cadCmtsCmRepairWindowStartTime,
       "cadCmtsCmRepairWindowEndTime": cadCmtsCmRepairWindowEndTime,
       "cadCmtsCmRepairInterval": cadCmtsCmRepairInterval,
       "cadCmtsCmRegImpairedStatusTable": cadCmtsCmRegImpairedStatusTable,
       "cadCmtsCmRegImpairedStatusEntry": cadCmtsCmRegImpairedStatusEntry,
       "cadCmtsCmRegImpairedReason": cadCmtsCmRegImpairedReason,
       "cadCmtsCmRegImpairedFaultDetected": cadCmtsCmRegImpairedFaultDetected,
       "cadCmtsCmRegImpairedLastRepairAttempt": cadCmtsCmRegImpairedLastRepairAttempt,
       "cadCmtsCmRegImpairedLastRepairAction": cadCmtsCmRegImpairedLastRepairAction,
       "cadCmtsCmRegImpairedIfIndex": cadCmtsCmRegImpairedIfIndex,
       "cadIf3CmtsCmUsStatusTable": cadIf3CmtsCmUsStatusTable,
       "cadIf3CmtsCmUsStatusEntry": cadIf3CmtsCmUsStatusEntry,
       "cadIf3CmtsCmUsStatusChIfIndex": cadIf3CmtsCmUsStatusChIfIndex,
       "cadIf3CmtsCmUsStatusModulationType": cadIf3CmtsCmUsStatusModulationType,
       "cadIf3CmtsCmUsStatusIsMuted": cadIf3CmtsCmUsStatusIsMuted,
       "cadIf3CmtsCmUsStatusRangingStatus": cadIf3CmtsCmUsStatusRangingStatus,
       "cadRccStatusTable": cadRccStatusTable,
       "cadRccStatusEntry": cadRccStatusEntry,
       "cadRccStatusRcpId": cadRccStatusRcpId,
       "cadRccStatusId": cadRccStatusId,
       "cadRccStatusRccCfgId": cadRccStatusRccCfgId,
       "cadRccStatusValidityCode": cadRccStatusValidityCode,
       "cadRccStatusValidityCodeText": cadRccStatusValidityCodeText,
       "cadRccStatusDsChSetId": cadRccStatusDsChSetId,
       "cadRccStatusChannelCount": cadRccStatusChannelCount,
       "cadIf3UsChSetTable": cadIf3UsChSetTable,
       "cadIf3UsChSetEntry": cadIf3UsChSetEntry,
       "cadIf3UsChIfIndex": cadIf3UsChIfIndex,
       "cadIf3DsChSetTable": cadIf3DsChSetTable,
       "cadIf3DsChSetEntry": cadIf3DsChSetEntry,
       "cadIf3DsChIfIndex": cadIf3DsChIfIndex,
       "cadIf3CsSummaryTable": cadIf3CsSummaryTable,
       "cadIf3CsSummaryEntry": cadIf3CsSummaryEntry,
       "cadIf3CsDir": cadIf3CsDir,
       "cadIf3CsId": cadIf3CsId,
       "cadIf3CsNumOther": cadIf3CsNumOther,
       "cadIf3CsNumInitRanging": cadIf3CsNumInitRanging,
       "cadIf3CsNumRangingComplete": cadIf3CsNumRangingComplete,
       "cadIf3CsNumStartEae": cadIf3CsNumStartEae,
       "cadIf3CsNumStartDhcpv4": cadIf3CsNumStartDhcpv4,
       "cadIf3CsNumStartDhcpv6": cadIf3CsNumStartDhcpv6,
       "cadIf3CsNumDhcpv4Complete": cadIf3CsNumDhcpv4Complete,
       "cadIf3CsNumDhcpv6Complete": cadIf3CsNumDhcpv6Complete,
       "cadIf3CsNumStartCfgFileDownload": cadIf3CsNumStartCfgFileDownload,
       "cadIf3CsNumCfgFileDownloadComplete": cadIf3CsNumCfgFileDownloadComplete,
       "cadIf3CsNumStartRegistration": cadIf3CsNumStartRegistration,
       "cadIf3CsNumRegistrationComplete": cadIf3CsNumRegistrationComplete,
       "cadIf3CsNumOperational": cadIf3CsNumOperational,
       "cadIf3CsNumBpiInit": cadIf3CsNumBpiInit,
       "cadIf3CsNumForwardingDisabled": cadIf3CsNumForwardingDisabled,
       "cadIf3CsNumRfMuteAll": cadIf3CsNumRfMuteAll,
       "cadIf3CsNumTotal": cadIf3CsNumTotal,
       "cadIf3CsNumRangingAborted": cadIf3CsNumRangingAborted,
       "cadIf3CsNumRangFlaps": cadIf3CsNumRangFlaps,
       "cadIf3CsNumProvFlaps": cadIf3CsNumProvFlaps,
       "cadIf3CsNumRegFlaps": cadIf3CsNumRegFlaps,
       "cadIf3ChsSummary": cadIf3ChsSummary,
       "cadIf3ChsNumOther": cadIf3ChsNumOther,
       "cadIf3ChsNumInitRanging": cadIf3ChsNumInitRanging,
       "cadIf3ChsNumRangingComplete": cadIf3ChsNumRangingComplete,
       "cadIf3ChsNumStartEae": cadIf3ChsNumStartEae,
       "cadIf3ChsNumStartDhcpv4": cadIf3ChsNumStartDhcpv4,
       "cadIf3ChsNumStartDhcpv6": cadIf3ChsNumStartDhcpv6,
       "cadIf3ChsNumDhcpv4Complete": cadIf3ChsNumDhcpv4Complete,
       "cadIf3ChsNumDhcpv6Complete": cadIf3ChsNumDhcpv6Complete,
       "cadIf3ChsNumStartCfgFileDownload": cadIf3ChsNumStartCfgFileDownload,
       "cadIf3ChsNumCfgFileDownloadComplete": cadIf3ChsNumCfgFileDownloadComplete,
       "cadIf3ChsNumStartRegistration": cadIf3ChsNumStartRegistration,
       "cadIf3ChsNumRegistrationComplete": cadIf3ChsNumRegistrationComplete,
       "cadIf3ChsNumOperational": cadIf3ChsNumOperational,
       "cadIf3ChsNumBpiInit": cadIf3ChsNumBpiInit,
       "cadIf3ChsNumForwardingDisabled": cadIf3ChsNumForwardingDisabled,
       "cadIf3ChsNumRfMuteAll": cadIf3ChsNumRfMuteAll,
       "cadIf3ChsNumTotal": cadIf3ChsNumTotal,
       "cadIf3ChsNumRangingAborted": cadIf3ChsNumRangingAborted,
       "cadIf3ChsNumRangFlaps": cadIf3ChsNumRangFlaps,
       "cadIf3ChsNumProvFlaps": cadIf3ChsNumProvFlaps,
       "cadIf3ChsNumRegFlaps": cadIf3ChsNumRegFlaps,
       "cadIfCmtsCmFailedProfStatusTable": cadIfCmtsCmFailedProfStatusTable,
       "cadIfCmtsCmFailedProfStatusEntry": cadIfCmtsCmFailedProfStatusEntry,
       "cadIfCmtsCmFailedProfMacAddress": cadIfCmtsCmFailedProfMacAddress,
       "cadIfCmtsCmFailedProfIfIndex": cadIfCmtsCmFailedProfIfIndex,
       "cadIfCmtsCmFailedProfId": cadIfCmtsCmFailedProfId,
       "cadIfCmtsCmFailedProfReason": cadIfCmtsCmFailedProfReason,
       "cadIfCmtsCmFailedProfFaultDetected": cadIfCmtsCmFailedProfFaultDetected}
)
