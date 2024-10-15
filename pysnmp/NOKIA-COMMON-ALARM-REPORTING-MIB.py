# SNMP MIB module (NOKIA-COMMON-ALARM-REPORTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-COMMON-ALARM-REPORTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:35 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class AlarmSeverity(Integer32):
    """Custom type AlarmSeverity based on Integer32"""




class EnabledDisabled(Integer32):
    """Custom type EnabledDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )





class RowPointer(ObjectIdentifier):
    """Custom type RowPointer based on ObjectIdentifier"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nokia_ObjectIdentity = ObjectIdentity
nokia = _Nokia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94)
)
_NokiaProducts_ObjectIdentity = ObjectIdentity
nokiaProducts = _NokiaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1)
)
_NtcCommon_ObjectIdentity = ObjectIdentity
ntcCommon = _NtcCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16)
)
_NtcCommonAlarm_ObjectIdentity = ObjectIdentity
ntcCommonAlarm = _NtcCommonAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1)
)
_Ca_ObjectIdentity = ObjectIdentity
ca = _Ca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1)
)
_CaVars_ObjectIdentity = ObjectIdentity
caVars = _CaVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1)
)
_CaReportNokiaAlarmTraps_Type = EnabledDisabled
_CaReportNokiaAlarmTraps_Object = MibScalar
caReportNokiaAlarmTraps = _CaReportNokiaAlarmTraps_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 1),
    _CaReportNokiaAlarmTraps_Type()
)
caReportNokiaAlarmTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caReportNokiaAlarmTraps.setStatus("mandatory")
_CaReportLinkUpLinkDownTraps_Type = EnabledDisabled
_CaReportLinkUpLinkDownTraps_Object = MibScalar
caReportLinkUpLinkDownTraps = _CaReportLinkUpLinkDownTraps_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 2),
    _CaReportLinkUpLinkDownTraps_Type()
)
caReportLinkUpLinkDownTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caReportLinkUpLinkDownTraps.setStatus("mandatory")


class _CaAlarmText_Type(DisplayString):
    """Custom type caAlarmText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CaAlarmText_Type.__name__ = "DisplayString"
_CaAlarmText_Object = MibScalar
caAlarmText = _CaAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 3),
    _CaAlarmText_Type()
)
caAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caAlarmText.setStatus("mandatory")


class _CaTrapId_Type(Integer32):
    """Custom type caTrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CaTrapId_Type.__name__ = "Integer32"
_CaTrapId_Object = MibScalar
caTrapId = _CaTrapId_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 4),
    _CaTrapId_Type()
)
caTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caTrapId.setStatus("mandatory")
_CaCorrelatedAlarmId_Type = Integer32
_CaCorrelatedAlarmId_Object = MibScalar
caCorrelatedAlarmId = _CaCorrelatedAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 5),
    _CaCorrelatedAlarmId_Type()
)
caCorrelatedAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caCorrelatedAlarmId.setStatus("mandatory")
_CaColumnInTbl_Type = RowPointer
_CaColumnInTbl_Object = MibScalar
caColumnInTbl = _CaColumnInTbl_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 6),
    _CaColumnInTbl_Type()
)
caColumnInTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caColumnInTbl.setStatus("mandatory")
_CaRowIdx_Type = ObjectIdentifier
_CaRowIdx_Object = MibScalar
caRowIdx = _CaRowIdx_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 7),
    _CaRowIdx_Type()
)
caRowIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caRowIdx.setStatus("mandatory")
_CaSeverity_Type = AlarmSeverity
_CaSeverity_Object = MibScalar
caSeverity = _CaSeverity_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 8),
    _CaSeverity_Type()
)
caSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caSeverity.setStatus("mandatory")
_CaNESpecificAlarmManualPageNbr_Type = Integer32
_CaNESpecificAlarmManualPageNbr_Object = MibScalar
caNESpecificAlarmManualPageNbr = _CaNESpecificAlarmManualPageNbr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 9),
    _CaNESpecificAlarmManualPageNbr_Type()
)
caNESpecificAlarmManualPageNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caNESpecificAlarmManualPageNbr.setStatus("mandatory")


class _CaSupplementaryInfo_Type(OctetString):
    """Custom type caSupplementaryInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CaSupplementaryInfo_Type.__name__ = "OctetString"
_CaSupplementaryInfo_Object = MibScalar
caSupplementaryInfo = _CaSupplementaryInfo_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 1, 1, 10),
    _CaSupplementaryInfo_Type()
)
caSupplementaryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caSupplementaryInfo.setStatus("mandatory")
_Cal_ObjectIdentity = ObjectIdentity
cal = _Cal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2)
)
_CalVars_ObjectIdentity = ObjectIdentity
calVars = _CalVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 1)
)
_CalActiveAlarmCount_Type = Integer32
_CalActiveAlarmCount_Object = MibScalar
calActiveAlarmCount = _CalActiveAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 1, 1),
    _CalActiveAlarmCount_Type()
)
calActiveAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calActiveAlarmCount.setStatus("mandatory")
_CalContentsChangeTime_Type = TimeTicks
_CalContentsChangeTime_Object = MibScalar
calContentsChangeTime = _CalContentsChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 1, 2),
    _CalContentsChangeTime_Type()
)
calContentsChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calContentsChangeTime.setStatus("mandatory")
_CalTables_ObjectIdentity = ObjectIdentity
calTables = _CalTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2)
)
_CalCurrentAlarmListTable_Object = MibTable
calCurrentAlarmListTable = _CalCurrentAlarmListTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    calCurrentAlarmListTable.setStatus("mandatory")
_CalCurrentAlarmListEntry_Object = MibTableRow
calCurrentAlarmListEntry = _CalCurrentAlarmListEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1)
)
calCurrentAlarmListEntry.setIndexNames(
    (0, "NOKIA-COMMON-ALARM-REPORTING-MIB", "calAlarmIndex"),
)
if mibBuilder.loadTexts:
    calCurrentAlarmListEntry.setStatus("mandatory")


class _CalAlarmIndex_Type(Integer32):
    """Custom type calAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CalAlarmIndex_Type.__name__ = "Integer32"
_CalAlarmIndex_Object = MibTableColumn
calAlarmIndex = _CalAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1, 1),
    _CalAlarmIndex_Type()
)
calAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calAlarmIndex.setStatus("mandatory")


class _CalSpecificTrap_Type(Integer32):
    """Custom type calSpecificTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CalSpecificTrap_Type.__name__ = "Integer32"
_CalSpecificTrap_Object = MibTableColumn
calSpecificTrap = _CalSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1, 2),
    _CalSpecificTrap_Type()
)
calSpecificTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calSpecificTrap.setStatus("mandatory")
_CalTimeStamp_Type = TimeTicks
_CalTimeStamp_Object = MibTableColumn
calTimeStamp = _CalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1, 3),
    _CalTimeStamp_Type()
)
calTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calTimeStamp.setStatus("mandatory")


class _CalAlarmText_Type(DisplayString):
    """Custom type calAlarmText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CalAlarmText_Type.__name__ = "DisplayString"
_CalAlarmText_Object = MibTableColumn
calAlarmText = _CalAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1, 4),
    _CalAlarmText_Type()
)
calAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calAlarmText.setStatus("mandatory")
_CalFirstColumnInTbl_Type = RowPointer
_CalFirstColumnInTbl_Object = MibTableColumn
calFirstColumnInTbl = _CalFirstColumnInTbl_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1, 5),
    _CalFirstColumnInTbl_Type()
)
calFirstColumnInTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calFirstColumnInTbl.setStatus("mandatory")
_CalRowIdx_Type = ObjectIdentifier
_CalRowIdx_Object = MibTableColumn
calRowIdx = _CalRowIdx_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1, 6),
    _CalRowIdx_Type()
)
calRowIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calRowIdx.setStatus("mandatory")
_CalSeverity_Type = AlarmSeverity
_CalSeverity_Object = MibTableColumn
calSeverity = _CalSeverity_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1, 7),
    _CalSeverity_Type()
)
calSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calSeverity.setStatus("mandatory")
_CalNESpecificAMPNbr_Type = Integer32
_CalNESpecificAMPNbr_Object = MibTableColumn
calNESpecificAMPNbr = _CalNESpecificAMPNbr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1, 8),
    _CalNESpecificAMPNbr_Type()
)
calNESpecificAMPNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calNESpecificAMPNbr.setStatus("mandatory")


class _CalSupplementaryInfo_Type(OctetString):
    """Custom type calSupplementaryInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CalSupplementaryInfo_Type.__name__ = "OctetString"
_CalSupplementaryInfo_Object = MibTableColumn
calSupplementaryInfo = _CalSupplementaryInfo_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 2, 2, 1, 1, 9),
    _CalSupplementaryInfo_Type()
)
calSupplementaryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calSupplementaryInfo.setStatus("mandatory")
_Al_ObjectIdentity = ObjectIdentity
al = _Al_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3)
)
_AlVars_ObjectIdentity = ObjectIdentity
alVars = _AlVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 1)
)
_AlAlarmLogEntryCount_Type = Integer32
_AlAlarmLogEntryCount_Object = MibScalar
alAlarmLogEntryCount = _AlAlarmLogEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 1, 1),
    _AlAlarmLogEntryCount_Type()
)
alAlarmLogEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlarmLogEntryCount.setStatus("mandatory")
_AlAlarmLogMaxSize_Type = Integer32
_AlAlarmLogMaxSize_Object = MibScalar
alAlarmLogMaxSize = _AlAlarmLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 1, 2),
    _AlAlarmLogMaxSize_Type()
)
alAlarmLogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAlarmLogMaxSize.setStatus("mandatory")
_AlLogFullAction_Type = Integer32
_AlLogFullAction_Object = MibScalar
alLogFullAction = _AlLogFullAction_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 1, 3),
    _AlLogFullAction_Type()
)
alLogFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alLogFullAction.setStatus("mandatory")
_AlResendTrapDestinationAddr_Type = IpAddress
_AlResendTrapDestinationAddr_Object = MibScalar
alResendTrapDestinationAddr = _AlResendTrapDestinationAddr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 1, 4),
    _AlResendTrapDestinationAddr_Type()
)
alResendTrapDestinationAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alResendTrapDestinationAddr.setStatus("mandatory")


class _AlResendTrapDestinationPort_Type(Integer32):
    """Custom type alResendTrapDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlResendTrapDestinationPort_Type.__name__ = "Integer32"
_AlResendTrapDestinationPort_Object = MibScalar
alResendTrapDestinationPort = _AlResendTrapDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 1, 5),
    _AlResendTrapDestinationPort_Type()
)
alResendTrapDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alResendTrapDestinationPort.setStatus("mandatory")
_AlResendTrapId_Type = Integer32
_AlResendTrapId_Object = MibScalar
alResendTrapId = _AlResendTrapId_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 1, 6),
    _AlResendTrapId_Type()
)
alResendTrapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alResendTrapId.setStatus("mandatory")
_AlTables_ObjectIdentity = ObjectIdentity
alTables = _AlTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2)
)
_AlAlarmLogTable_Object = MibTable
alAlarmLogTable = _AlAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    alAlarmLogTable.setStatus("mandatory")
_AlAlarmLogEntry_Object = MibTableRow
alAlarmLogEntry = _AlAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1)
)
alAlarmLogEntry.setIndexNames(
    (0, "NOKIA-COMMON-ALARM-REPORTING-MIB", "alTrapIndex"),
)
if mibBuilder.loadTexts:
    alAlarmLogEntry.setStatus("mandatory")


class _AlTrapIndex_Type(Integer32):
    """Custom type alTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlTrapIndex_Type.__name__ = "Integer32"
_AlTrapIndex_Object = MibTableColumn
alTrapIndex = _AlTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 1),
    _AlTrapIndex_Type()
)
alTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTrapIndex.setStatus("mandatory")


class _AlSpecificTrap_Type(Integer32):
    """Custom type alSpecificTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlSpecificTrap_Type.__name__ = "Integer32"
_AlSpecificTrap_Object = MibTableColumn
alSpecificTrap = _AlSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 2),
    _AlSpecificTrap_Type()
)
alSpecificTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSpecificTrap.setStatus("mandatory")
_AlTimeStamp_Type = TimeTicks
_AlTimeStamp_Object = MibTableColumn
alTimeStamp = _AlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 3),
    _AlTimeStamp_Type()
)
alTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTimeStamp.setStatus("mandatory")


class _AlAlarmText_Type(DisplayString):
    """Custom type alAlarmText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlAlarmText_Type.__name__ = "DisplayString"
_AlAlarmText_Object = MibTableColumn
alAlarmText = _AlAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 4),
    _AlAlarmText_Type()
)
alAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAlarmText.setStatus("mandatory")
_AlCorrelatedAlarmId_Type = Integer32
_AlCorrelatedAlarmId_Object = MibTableColumn
alCorrelatedAlarmId = _AlCorrelatedAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 5),
    _AlCorrelatedAlarmId_Type()
)
alCorrelatedAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCorrelatedAlarmId.setStatus("mandatory")
_AlFirstColumnInTbl_Type = RowPointer
_AlFirstColumnInTbl_Object = MibTableColumn
alFirstColumnInTbl = _AlFirstColumnInTbl_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 6),
    _AlFirstColumnInTbl_Type()
)
alFirstColumnInTbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFirstColumnInTbl.setStatus("mandatory")
_AlRowIdx_Type = ObjectIdentifier
_AlRowIdx_Object = MibTableColumn
alRowIdx = _AlRowIdx_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 7),
    _AlRowIdx_Type()
)
alRowIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRowIdx.setStatus("mandatory")
_AlSeverity_Type = AlarmSeverity
_AlSeverity_Object = MibTableColumn
alSeverity = _AlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 8),
    _AlSeverity_Type()
)
alSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSeverity.setStatus("mandatory")
_AlNESpecificAMPNbr_Type = Integer32
_AlNESpecificAMPNbr_Object = MibTableColumn
alNESpecificAMPNbr = _AlNESpecificAMPNbr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 9),
    _AlNESpecificAMPNbr_Type()
)
alNESpecificAMPNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alNESpecificAMPNbr.setStatus("mandatory")


class _AlSupplementaryInfo_Type(OctetString):
    """Custom type alSupplementaryInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlSupplementaryInfo_Type.__name__ = "OctetString"
_AlSupplementaryInfo_Object = MibTableColumn
alSupplementaryInfo = _AlSupplementaryInfo_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 16, 1, 3, 2, 1, 1, 10),
    _AlSupplementaryInfo_Type()
)
alSupplementaryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSupplementaryInfo.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-COMMON-ALARM-REPORTING-MIB",
    **{"AlarmSeverity": AlarmSeverity,
       "EnabledDisabled": EnabledDisabled,
       "RowPointer": RowPointer,
       "nokia": nokia,
       "nokiaProducts": nokiaProducts,
       "ntcCommon": ntcCommon,
       "ntcCommonAlarm": ntcCommonAlarm,
       "ca": ca,
       "caVars": caVars,
       "caReportNokiaAlarmTraps": caReportNokiaAlarmTraps,
       "caReportLinkUpLinkDownTraps": caReportLinkUpLinkDownTraps,
       "caAlarmText": caAlarmText,
       "caTrapId": caTrapId,
       "caCorrelatedAlarmId": caCorrelatedAlarmId,
       "caColumnInTbl": caColumnInTbl,
       "caRowIdx": caRowIdx,
       "caSeverity": caSeverity,
       "caNESpecificAlarmManualPageNbr": caNESpecificAlarmManualPageNbr,
       "caSupplementaryInfo": caSupplementaryInfo,
       "cal": cal,
       "calVars": calVars,
       "calActiveAlarmCount": calActiveAlarmCount,
       "calContentsChangeTime": calContentsChangeTime,
       "calTables": calTables,
       "calCurrentAlarmListTable": calCurrentAlarmListTable,
       "calCurrentAlarmListEntry": calCurrentAlarmListEntry,
       "calAlarmIndex": calAlarmIndex,
       "calSpecificTrap": calSpecificTrap,
       "calTimeStamp": calTimeStamp,
       "calAlarmText": calAlarmText,
       "calFirstColumnInTbl": calFirstColumnInTbl,
       "calRowIdx": calRowIdx,
       "calSeverity": calSeverity,
       "calNESpecificAMPNbr": calNESpecificAMPNbr,
       "calSupplementaryInfo": calSupplementaryInfo,
       "al": al,
       "alVars": alVars,
       "alAlarmLogEntryCount": alAlarmLogEntryCount,
       "alAlarmLogMaxSize": alAlarmLogMaxSize,
       "alLogFullAction": alLogFullAction,
       "alResendTrapDestinationAddr": alResendTrapDestinationAddr,
       "alResendTrapDestinationPort": alResendTrapDestinationPort,
       "alResendTrapId": alResendTrapId,
       "alTables": alTables,
       "alAlarmLogTable": alAlarmLogTable,
       "alAlarmLogEntry": alAlarmLogEntry,
       "alTrapIndex": alTrapIndex,
       "alSpecificTrap": alSpecificTrap,
       "alTimeStamp": alTimeStamp,
       "alAlarmText": alAlarmText,
       "alCorrelatedAlarmId": alCorrelatedAlarmId,
       "alFirstColumnInTbl": alFirstColumnInTbl,
       "alRowIdx": alRowIdx,
       "alSeverity": alSeverity,
       "alNESpecificAMPNbr": alNESpecificAMPNbr,
       "alSupplementaryInfo": alSupplementaryInfo}
)
