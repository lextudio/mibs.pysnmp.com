# SNMP MIB module (CISCO-VISM-CONN-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-CONN-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:49 2024
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

(vismChanGrp,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "vismChanGrp")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVismConnStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 89)
)
ciscoVismConnStatMIB.setRevisions(
        ("2005-09-26 00:00",
         "2004-04-22 00:00",
         "2003-12-12 00:00",
         "2003-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismChanCntGrp_ObjectIdentity = ObjectIdentity
vismChanCntGrp = _VismChanCntGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3)
)
_VismChanCntGrpTable_Object = MibTable
vismChanCntGrpTable = _VismChanCntGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1)
)
if mibBuilder.loadTexts:
    vismChanCntGrpTable.setStatus("current")
_VismChanCntGrpEntry_Object = MibTableRow
vismChanCntGrpEntry = _VismChanCntGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1)
)
vismChanCntGrpEntry.setIndexNames(
    (0, "CISCO-VISM-CONN-STAT-MIB", "vismCntChanNum"),
)
if mibBuilder.loadTexts:
    vismChanCntGrpEntry.setStatus("current")


class _VismCntChanNum_Type(Integer32):
    """Custom type vismCntChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismCntChanNum_Type.__name__ = "Integer32"
_VismCntChanNum_Object = MibTableColumn
vismCntChanNum = _VismCntChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 1),
    _VismCntChanNum_Type()
)
vismCntChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCntChanNum.setStatus("current")


class _VismCntClrButton_Type(Integer32):
    """Custom type vismCntClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetcounters", 2))
    )


_VismCntClrButton_Type.__name__ = "Integer32"
_VismCntClrButton_Object = MibTableColumn
vismCntClrButton = _VismCntClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 10),
    _VismCntClrButton_Type()
)
vismCntClrButton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCntClrButton.setStatus("current")
_VismChanAal2HecErrors_Type = Counter32
_VismChanAal2HecErrors_Object = MibTableColumn
vismChanAal2HecErrors = _VismChanAal2HecErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 11),
    _VismChanAal2HecErrors_Type()
)
vismChanAal2HecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2HecErrors.setStatus("current")
_VismChanAal2CrcErrors_Type = Counter32
_VismChanAal2CrcErrors_Object = MibTableColumn
vismChanAal2CrcErrors = _VismChanAal2CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 12),
    _VismChanAal2CrcErrors_Type()
)
vismChanAal2CrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2CrcErrors.setStatus("current")
_VismChanAal2OamLpbLostCells_Type = Counter32
_VismChanAal2OamLpbLostCells_Object = MibTableColumn
vismChanAal2OamLpbLostCells = _VismChanAal2OamLpbLostCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 13),
    _VismChanAal2OamLpbLostCells_Type()
)
vismChanAal2OamLpbLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2OamLpbLostCells.setStatus("current")
_VismChanAal2InvOsfCells_Type = Counter32
_VismChanAal2InvOsfCells_Object = MibTableColumn
vismChanAal2InvOsfCells = _VismChanAal2InvOsfCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 14),
    _VismChanAal2InvOsfCells_Type()
)
vismChanAal2InvOsfCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2InvOsfCells.setStatus("current")
_VismChanAal2InvParCells_Type = Counter32
_VismChanAal2InvParCells_Object = MibTableColumn
vismChanAal2InvParCells = _VismChanAal2InvParCells_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 15),
    _VismChanAal2InvParCells_Type()
)
vismChanAal2InvParCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2InvParCells.setStatus("current")
_VismChanAal2CpsSentPkts_Type = Counter32
_VismChanAal2CpsSentPkts_Object = MibTableColumn
vismChanAal2CpsSentPkts = _VismChanAal2CpsSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 16),
    _VismChanAal2CpsSentPkts_Type()
)
vismChanAal2CpsSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2CpsSentPkts.setStatus("current")
_VismChanAal2CpsRcvdPkts_Type = Counter32
_VismChanAal2CpsRcvdPkts_Object = MibTableColumn
vismChanAal2CpsRcvdPkts = _VismChanAal2CpsRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 17),
    _VismChanAal2CpsRcvdPkts_Type()
)
vismChanAal2CpsRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2CpsRcvdPkts.setStatus("current")
_VismChanAal2CpsInvCidPkts_Type = Counter32
_VismChanAal2CpsInvCidPkts_Object = MibTableColumn
vismChanAal2CpsInvCidPkts = _VismChanAal2CpsInvCidPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 18),
    _VismChanAal2CpsInvCidPkts_Type()
)
vismChanAal2CpsInvCidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2CpsInvCidPkts.setStatus("current")
_VismChanAal2CpsInvUuiPkts_Type = Counter32
_VismChanAal2CpsInvUuiPkts_Object = MibTableColumn
vismChanAal2CpsInvUuiPkts = _VismChanAal2CpsInvUuiPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 19),
    _VismChanAal2CpsInvUuiPkts_Type()
)
vismChanAal2CpsInvUuiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2CpsInvUuiPkts.setStatus("current")
_VismChanAal2CpsInvLenPkts_Type = Counter32
_VismChanAal2CpsInvLenPkts_Object = MibTableColumn
vismChanAal2CpsInvLenPkts = _VismChanAal2CpsInvLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 20),
    _VismChanAal2CpsInvLenPkts_Type()
)
vismChanAal2CpsInvLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal2CpsInvLenPkts.setStatus("current")
_VismChanAal5InvCpiPdus_Type = Counter32
_VismChanAal5InvCpiPdus_Object = MibTableColumn
vismChanAal5InvCpiPdus = _VismChanAal5InvCpiPdus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 21),
    _VismChanAal5InvCpiPdus_Type()
)
vismChanAal5InvCpiPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal5InvCpiPdus.setStatus("current")
_VismChanAal5OversizedSdusRcvdPdus_Type = Counter32
_VismChanAal5OversizedSdusRcvdPdus_Object = MibTableColumn
vismChanAal5OversizedSdusRcvdPdus = _VismChanAal5OversizedSdusRcvdPdus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 22),
    _VismChanAal5OversizedSdusRcvdPdus_Type()
)
vismChanAal5OversizedSdusRcvdPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal5OversizedSdusRcvdPdus.setStatus("current")
_VismChanAal5InvLenPdus_Type = Counter32
_VismChanAal5InvLenPdus_Object = MibTableColumn
vismChanAal5InvLenPdus = _VismChanAal5InvLenPdus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 23),
    _VismChanAal5InvLenPdus_Type()
)
vismChanAal5InvLenPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal5InvLenPdus.setStatus("current")
_VismChanAal5Crc32ErrorPdus_Type = Counter32
_VismChanAal5Crc32ErrorPdus_Object = MibTableColumn
vismChanAal5Crc32ErrorPdus = _VismChanAal5Crc32ErrorPdus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 24),
    _VismChanAal5Crc32ErrorPdus_Type()
)
vismChanAal5Crc32ErrorPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal5Crc32ErrorPdus.setStatus("current")
_VismChanAal5ReassemTimerExpiryPdus_Type = Counter32
_VismChanAal5ReassemTimerExpiryPdus_Object = MibTableColumn
vismChanAal5ReassemTimerExpiryPdus = _VismChanAal5ReassemTimerExpiryPdus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 25),
    _VismChanAal5ReassemTimerExpiryPdus_Type()
)
vismChanAal5ReassemTimerExpiryPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal5ReassemTimerExpiryPdus.setStatus("current")
_VismChan24HrPeakXmtCellRate_Type = Counter32
_VismChan24HrPeakXmtCellRate_Object = MibTableColumn
vismChan24HrPeakXmtCellRate = _VismChan24HrPeakXmtCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 26),
    _VismChan24HrPeakXmtCellRate_Type()
)
vismChan24HrPeakXmtCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChan24HrPeakXmtCellRate.setStatus("current")
_VismChanCurrentXmtCellRate_Type = Counter32
_VismChanCurrentXmtCellRate_Object = MibTableColumn
vismChanCurrentXmtCellRate = _VismChanCurrentXmtCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 27),
    _VismChanCurrentXmtCellRate_Type()
)
vismChanCurrentXmtCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanCurrentXmtCellRate.setStatus("current")
_VismChan24HrPeakRcvCellRate_Type = Counter32
_VismChan24HrPeakRcvCellRate_Object = MibTableColumn
vismChan24HrPeakRcvCellRate = _VismChan24HrPeakRcvCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 28),
    _VismChan24HrPeakRcvCellRate_Type()
)
vismChan24HrPeakRcvCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChan24HrPeakRcvCellRate.setStatus("current")
_VismChanCurrentRcvCellRate_Type = Counter32
_VismChanCurrentRcvCellRate_Object = MibTableColumn
vismChanCurrentRcvCellRate = _VismChanCurrentRcvCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 29),
    _VismChanCurrentRcvCellRate_Type()
)
vismChanCurrentRcvCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanCurrentRcvCellRate.setStatus("current")
_VismChanAisSuppressCount_Type = Counter32
_VismChanAisSuppressCount_Object = MibTableColumn
vismChanAisSuppressCount = _VismChanAisSuppressCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 30),
    _VismChanAisSuppressCount_Type()
)
vismChanAisSuppressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAisSuppressCount.setStatus("current")
_VismChanXmtAisCnts_Type = Counter32
_VismChanXmtAisCnts_Object = MibTableColumn
vismChanXmtAisCnts = _VismChanXmtAisCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 31),
    _VismChanXmtAisCnts_Type()
)
vismChanXmtAisCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanXmtAisCnts.setStatus("current")
_VismChanRcvAisCnts_Type = Counter32
_VismChanRcvAisCnts_Object = MibTableColumn
vismChanRcvAisCnts = _VismChanRcvAisCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 32),
    _VismChanRcvAisCnts_Type()
)
vismChanRcvAisCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanRcvAisCnts.setStatus("current")
_VismChanXmtFerfCnts_Type = Counter32
_VismChanXmtFerfCnts_Object = MibTableColumn
vismChanXmtFerfCnts = _VismChanXmtFerfCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 33),
    _VismChanXmtFerfCnts_Type()
)
vismChanXmtFerfCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanXmtFerfCnts.setStatus("current")
_VismChanRcvFerfCnts_Type = Counter32
_VismChanRcvFerfCnts_Object = MibTableColumn
vismChanRcvFerfCnts = _VismChanRcvFerfCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 34),
    _VismChanRcvFerfCnts_Type()
)
vismChanRcvFerfCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanRcvFerfCnts.setStatus("current")
_VismChanAal5PduSentPkts_Type = Counter32
_VismChanAal5PduSentPkts_Object = MibTableColumn
vismChanAal5PduSentPkts = _VismChanAal5PduSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 35),
    _VismChanAal5PduSentPkts_Type()
)
vismChanAal5PduSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal5PduSentPkts.setStatus("current")
_VismChanAal5PduRcvdPkts_Type = Counter32
_VismChanAal5PduRcvdPkts_Object = MibTableColumn
vismChanAal5PduRcvdPkts = _VismChanAal5PduRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 36),
    _VismChanAal5PduRcvdPkts_Type()
)
vismChanAal5PduRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAal5PduRcvdPkts.setStatus("current")
_VismChanAisDelayLeft_Type = Unsigned32
_VismChanAisDelayLeft_Object = MibTableColumn
vismChanAisDelayLeft = _VismChanAisDelayLeft_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 37),
    _VismChanAisDelayLeft_Type()
)
vismChanAisDelayLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanAisDelayLeft.setStatus("current")
_VismChanOamLpbkTimeoutCnts_Type = Counter32
_VismChanOamLpbkTimeoutCnts_Object = MibTableColumn
vismChanOamLpbkTimeoutCnts = _VismChanOamLpbkTimeoutCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 38),
    _VismChanOamLpbkTimeoutCnts_Type()
)
vismChanOamLpbkTimeoutCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanOamLpbkTimeoutCnts.setStatus("current")
_VismChanOamLpbkTimeoutDuration_Type = Unsigned32
_VismChanOamLpbkTimeoutDuration_Object = MibTableColumn
vismChanOamLpbkTimeoutDuration = _VismChanOamLpbkTimeoutDuration_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 3, 1, 1, 39),
    _VismChanOamLpbkTimeoutDuration_Type()
)
vismChanOamLpbkTimeoutDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanOamLpbkTimeoutDuration.setStatus("current")
if mibBuilder.loadTexts:
    vismChanOamLpbkTimeoutDuration.setUnits("seconds")
_CiscoVismConnStatMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismConnStatMIBConformance = _CiscoVismConnStatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2)
)
_CiscoVismConnStatMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismConnStatMIBGroups = _CiscoVismConnStatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 1)
)
_CiscoVismConnStatMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismConnStatMIBCompliances = _CiscoVismConnStatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 2)
)

# Managed Objects groups

ciscoVismConnStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 1, 1)
)
ciscoVismConnStatGroup.setObjects(
      *(("CISCO-VISM-CONN-STAT-MIB", "vismCntChanNum"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismCntClrButton"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2HecErrors"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CrcErrors"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2OamLpbLostCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2InvOsfCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2InvParCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsSentPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsRcvdPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvCidPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvUuiPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvLenPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5InvCpiPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5OversizedSdusRcvdPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5InvLenPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5Crc32ErrorPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5ReassemTimerExpiryPdus"))
)
if mibBuilder.loadTexts:
    ciscoVismConnStatGroup.setStatus("deprecated")

ciscoVismConnStatGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 1, 2)
)
ciscoVismConnStatGroup1.setObjects(
      *(("CISCO-VISM-CONN-STAT-MIB", "vismCntChanNum"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismCntClrButton"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2HecErrors"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CrcErrors"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2OamLpbLostCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2InvOsfCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2InvParCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsSentPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsRcvdPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvCidPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvUuiPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvLenPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5InvCpiPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5OversizedSdusRcvdPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5InvLenPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5Crc32ErrorPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5ReassemTimerExpiryPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChan24HrPeakXmtCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanCurrentXmtCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChan24HrPeakRcvCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanCurrentRcvCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAisSuppressCount"))
)
if mibBuilder.loadTexts:
    ciscoVismConnStatGroup1.setStatus("deprecated")

ciscoVismConnStatGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 1, 3)
)
ciscoVismConnStatGroup2.setObjects(
      *(("CISCO-VISM-CONN-STAT-MIB", "vismCntChanNum"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismCntClrButton"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2HecErrors"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CrcErrors"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2OamLpbLostCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2InvOsfCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2InvParCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsSentPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsRcvdPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvCidPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvUuiPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvLenPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5InvCpiPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5OversizedSdusRcvdPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5InvLenPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5Crc32ErrorPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5ReassemTimerExpiryPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChan24HrPeakXmtCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanCurrentXmtCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChan24HrPeakRcvCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanCurrentRcvCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAisSuppressCount"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanXmtAisCnts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanRcvAisCnts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanXmtFerfCnts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanRcvFerfCnts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5PduSentPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5PduRcvdPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAisDelayLeft"))
)
if mibBuilder.loadTexts:
    ciscoVismConnStatGroup2.setStatus("deprecated")

ciscoVismConnStatGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 1, 4)
)
ciscoVismConnStatGroup3.setObjects(
      *(("CISCO-VISM-CONN-STAT-MIB", "vismCntChanNum"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismCntClrButton"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2HecErrors"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CrcErrors"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2OamLpbLostCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2InvOsfCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2InvParCells"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsSentPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsRcvdPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvCidPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvUuiPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal2CpsInvLenPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5InvCpiPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5OversizedSdusRcvdPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5InvLenPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5Crc32ErrorPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5ReassemTimerExpiryPdus"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChan24HrPeakXmtCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanCurrentXmtCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChan24HrPeakRcvCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanCurrentRcvCellRate"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAisSuppressCount"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanXmtAisCnts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanRcvAisCnts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanXmtFerfCnts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanRcvFerfCnts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5PduSentPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAal5PduRcvdPkts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanAisDelayLeft"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanOamLpbkTimeoutCnts"),
        ("CISCO-VISM-CONN-STAT-MIB", "vismChanOamLpbkTimeoutDuration"))
)
if mibBuilder.loadTexts:
    ciscoVismConnStatGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismConnStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismConnStatCompliance.setStatus(
        "deprecated"
    )

ciscoVismConnStatCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoVismConnStatCompliance1.setStatus(
        "deprecated"
    )

ciscoVismConnStatCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 2, 3)
)
if mibBuilder.loadTexts:
    ciscoVismConnStatCompliance2.setStatus(
        "deprecated"
    )

ciscoVismConnStatCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 89, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ciscoVismConnStatCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-CONN-STAT-MIB",
    **{"vismChanCntGrp": vismChanCntGrp,
       "vismChanCntGrpTable": vismChanCntGrpTable,
       "vismChanCntGrpEntry": vismChanCntGrpEntry,
       "vismCntChanNum": vismCntChanNum,
       "vismCntClrButton": vismCntClrButton,
       "vismChanAal2HecErrors": vismChanAal2HecErrors,
       "vismChanAal2CrcErrors": vismChanAal2CrcErrors,
       "vismChanAal2OamLpbLostCells": vismChanAal2OamLpbLostCells,
       "vismChanAal2InvOsfCells": vismChanAal2InvOsfCells,
       "vismChanAal2InvParCells": vismChanAal2InvParCells,
       "vismChanAal2CpsSentPkts": vismChanAal2CpsSentPkts,
       "vismChanAal2CpsRcvdPkts": vismChanAal2CpsRcvdPkts,
       "vismChanAal2CpsInvCidPkts": vismChanAal2CpsInvCidPkts,
       "vismChanAal2CpsInvUuiPkts": vismChanAal2CpsInvUuiPkts,
       "vismChanAal2CpsInvLenPkts": vismChanAal2CpsInvLenPkts,
       "vismChanAal5InvCpiPdus": vismChanAal5InvCpiPdus,
       "vismChanAal5OversizedSdusRcvdPdus": vismChanAal5OversizedSdusRcvdPdus,
       "vismChanAal5InvLenPdus": vismChanAal5InvLenPdus,
       "vismChanAal5Crc32ErrorPdus": vismChanAal5Crc32ErrorPdus,
       "vismChanAal5ReassemTimerExpiryPdus": vismChanAal5ReassemTimerExpiryPdus,
       "vismChan24HrPeakXmtCellRate": vismChan24HrPeakXmtCellRate,
       "vismChanCurrentXmtCellRate": vismChanCurrentXmtCellRate,
       "vismChan24HrPeakRcvCellRate": vismChan24HrPeakRcvCellRate,
       "vismChanCurrentRcvCellRate": vismChanCurrentRcvCellRate,
       "vismChanAisSuppressCount": vismChanAisSuppressCount,
       "vismChanXmtAisCnts": vismChanXmtAisCnts,
       "vismChanRcvAisCnts": vismChanRcvAisCnts,
       "vismChanXmtFerfCnts": vismChanXmtFerfCnts,
       "vismChanRcvFerfCnts": vismChanRcvFerfCnts,
       "vismChanAal5PduSentPkts": vismChanAal5PduSentPkts,
       "vismChanAal5PduRcvdPkts": vismChanAal5PduRcvdPkts,
       "vismChanAisDelayLeft": vismChanAisDelayLeft,
       "vismChanOamLpbkTimeoutCnts": vismChanOamLpbkTimeoutCnts,
       "vismChanOamLpbkTimeoutDuration": vismChanOamLpbkTimeoutDuration,
       "ciscoVismConnStatMIB": ciscoVismConnStatMIB,
       "ciscoVismConnStatMIBConformance": ciscoVismConnStatMIBConformance,
       "ciscoVismConnStatMIBGroups": ciscoVismConnStatMIBGroups,
       "ciscoVismConnStatGroup": ciscoVismConnStatGroup,
       "ciscoVismConnStatGroup1": ciscoVismConnStatGroup1,
       "ciscoVismConnStatGroup2": ciscoVismConnStatGroup2,
       "ciscoVismConnStatGroup3": ciscoVismConnStatGroup3,
       "ciscoVismConnStatMIBCompliances": ciscoVismConnStatMIBCompliances,
       "ciscoVismConnStatCompliance": ciscoVismConnStatCompliance,
       "ciscoVismConnStatCompliance1": ciscoVismConnStatCompliance1,
       "ciscoVismConnStatCompliance2": ciscoVismConnStatCompliance2,
       "ciscoVismConnStatCompliance3": ciscoVismConnStatCompliance3}
)
