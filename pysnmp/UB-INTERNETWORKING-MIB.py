# SNMP MIB module (UB-INTERNETWORKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UB-INTERNETWORKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:13 2024
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
 iso,
 mgmt,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbNode_ObjectIdentity = ObjectIdentity
ubNode = _UbNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75)
)
_UbEquip_ObjectIdentity = ObjectIdentity
ubEquip = _UbEquip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1)
)
_UbInternetworking_ObjectIdentity = ObjectIdentity
ubInternetworking = _UbInternetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2)
)
_UbRISCFddiBrouter_ObjectIdentity = ObjectIdentity
ubRISCFddiBrouter = _UbRISCFddiBrouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1)
)
_UbInEnc_ObjectIdentity = ObjectIdentity
ubInEnc = _UbInEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 1)
)
_EncSlots_Type = Integer32
_EncSlots_Object = MibScalar
encSlots = _EncSlots_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 1, 1),
    _EncSlots_Type()
)
encSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encSlots.setStatus("mandatory")
_UbInEntity_ObjectIdentity = ObjectIdentity
ubInEntity = _UbInEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 2)
)
_UbInCard_ObjectIdentity = ObjectIdentity
ubInCard = _UbInCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 3)
)
_ControlUb1_ObjectIdentity = ObjectIdentity
controlUb1 = _ControlUb1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 3, 1)
)
_Login_Type = DisplayString
_Login_Object = MibScalar
login = _Login_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 3, 1, 1),
    _Login_Type()
)
login.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    login.setStatus("mandatory")
_ConfigurationUb1_ObjectIdentity = ObjectIdentity
configurationUb1 = _ConfigurationUb1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 3, 2)
)
_SlotNum_Type = Integer32
_SlotNum_Object = MibScalar
slotNum = _SlotNum_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 3, 2, 1),
    _SlotNum_Type()
)
slotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotNum.setStatus("mandatory")
_QeContentionOwner_Type = Integer32
_QeContentionOwner_Object = MibScalar
qeContentionOwner = _QeContentionOwner_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 3, 2, 2),
    _QeContentionOwner_Type()
)
qeContentionOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qeContentionOwner.setStatus("mandatory")
_UbInPort_ObjectIdentity = ObjectIdentity
ubInPort = _UbInPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4)
)
_Plusbus_ObjectIdentity = ObjectIdentity
plusbus = _Plusbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1)
)
_PlusbusTable_Object = MibTable
plusbusTable = _PlusbusTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    plusbusTable.setStatus("mandatory")
_PlusbusEntry_Object = MibTableRow
plusbusEntry = _PlusbusEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 1, 1)
)
plusbusEntry.setIndexNames(
    (0, "UB-INTERNETWORKING-MIB", "plusbusIndex"),
)
if mibBuilder.loadTexts:
    plusbusEntry.setStatus("mandatory")
_PlusbusIndex_Type = Integer32
_PlusbusIndex_Object = MibTableColumn
plusbusIndex = _PlusbusIndex_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 1, 1, 1),
    _PlusbusIndex_Type()
)
plusbusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plusbusIndex.setStatus("mandatory")


class _PlusbusAdminstate_Type(Integer32):
    """Custom type plusbusAdminstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_PlusbusAdminstate_Type.__name__ = "Integer32"
_PlusbusAdminstate_Object = MibTableColumn
plusbusAdminstate = _PlusbusAdminstate_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 1, 1, 2),
    _PlusbusAdminstate_Type()
)
plusbusAdminstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plusbusAdminstate.setStatus("mandatory")
_PlusbusAccess_Type = OctetString
_PlusbusAccess_Object = MibScalar
plusbusAccess = _PlusbusAccess_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 1, 1, 3),
    _PlusbusAccess_Type()
)
plusbusAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plusbusAccess.setStatus("mandatory")
_PlusbusStatsTable_Object = MibTable
plusbusStatsTable = _PlusbusStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    plusbusStatsTable.setStatus("mandatory")
_PlusbusStatsEntry_Object = MibTableRow
plusbusStatsEntry = _PlusbusStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2, 1)
)
plusbusStatsEntry.setIndexNames(
    (0, "UB-INTERNETWORKING-MIB", "plusbusStatsIndex"),
)
if mibBuilder.loadTexts:
    plusbusStatsEntry.setStatus("mandatory")
_PlusbusStatsIndex_Type = Integer32
_PlusbusStatsIndex_Object = MibTableColumn
plusbusStatsIndex = _PlusbusStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2, 1, 1),
    _PlusbusStatsIndex_Type()
)
plusbusStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plusbusStatsIndex.setStatus("mandatory")
_PlusbusStatsTxErrors_Type = Counter32
_PlusbusStatsTxErrors_Object = MibTableColumn
plusbusStatsTxErrors = _PlusbusStatsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2, 1, 2),
    _PlusbusStatsTxErrors_Type()
)
plusbusStatsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plusbusStatsTxErrors.setStatus("mandatory")
_PlusbusStatsTxlostacks_Type = Counter32
_PlusbusStatsTxlostacks_Object = MibTableColumn
plusbusStatsTxlostacks = _PlusbusStatsTxlostacks_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2, 1, 3),
    _PlusbusStatsTxlostacks_Type()
)
plusbusStatsTxlostacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plusbusStatsTxlostacks.setStatus("mandatory")
_PlusbusStatsTxtimeouts_Type = Counter32
_PlusbusStatsTxtimeouts_Object = MibScalar
plusbusStatsTxtimeouts = _PlusbusStatsTxtimeouts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2, 1, 4),
    _PlusbusStatsTxtimeouts_Type()
)
plusbusStatsTxtimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plusbusStatsTxtimeouts.setStatus("mandatory")
_PlusbusStatsRxErrors_Type = Counter32
_PlusbusStatsRxErrors_Object = MibScalar
plusbusStatsRxErrors = _PlusbusStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2, 1, 5),
    _PlusbusStatsRxErrors_Type()
)
plusbusStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plusbusStatsRxErrors.setStatus("mandatory")
_PlusbusStatsRxtimeouts_Type = Counter32
_PlusbusStatsRxtimeouts_Object = MibScalar
plusbusStatsRxtimeouts = _PlusbusStatsRxtimeouts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2, 1, 6),
    _PlusbusStatsRxtimeouts_Type()
)
plusbusStatsRxtimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plusbusStatsRxtimeouts.setStatus("mandatory")
_PlusbusStatsclocklosses_Type = Counter32
_PlusbusStatsclocklosses_Object = MibScalar
plusbusStatsclocklosses = _PlusbusStatsclocklosses_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2, 1, 7),
    _PlusbusStatsclocklosses_Type()
)
plusbusStatsclocklosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plusbusStatsclocklosses.setStatus("mandatory")
_RxFifoUnderflows_Type = Counter32
_RxFifoUnderflows_Object = MibScalar
rxFifoUnderflows = _RxFifoUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 4, 1, 2, 1, 8),
    _RxFifoUnderflows_Type()
)
rxFifoUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFifoUnderflows.setStatus("mandatory")
_UbNVM_ObjectIdentity = ObjectIdentity
ubNVM = _UbNVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5)
)
_UbDownloader_ObjectIdentity = ObjectIdentity
ubDownloader = _UbDownloader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1)
)
_UbOptions_ObjectIdentity = ObjectIdentity
ubOptions = _UbOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1)
)
_UbDnloadOptions_Object = MibTableRow
ubDnloadOptions = _UbDnloadOptions_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ubDnloadOptions.setStatus("mandatory")
_DlVersionID_Type = Integer32
_DlVersionID_Object = MibTableColumn
dlVersionID = _DlVersionID_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1, 1, 1),
    _DlVersionID_Type()
)
dlVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlVersionID.setStatus("mandatory")


class _DlMaxLoadAttempts_Type(Integer32):
    """Custom type dlMaxLoadAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DlMaxLoadAttempts_Type.__name__ = "Integer32"
_DlMaxLoadAttempts_Object = MibTableColumn
dlMaxLoadAttempts = _DlMaxLoadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1, 1, 2),
    _DlMaxLoadAttempts_Type()
)
dlMaxLoadAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlMaxLoadAttempts.setStatus("mandatory")


class _DlMaxBOOTPAttempts_Type(Integer32):
    """Custom type dlMaxBOOTPAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DlMaxBOOTPAttempts_Type.__name__ = "Integer32"
_DlMaxBOOTPAttempts_Object = MibTableColumn
dlMaxBOOTPAttempts = _DlMaxBOOTPAttempts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1, 1, 3),
    _DlMaxBOOTPAttempts_Type()
)
dlMaxBOOTPAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlMaxBOOTPAttempts.setStatus("mandatory")


class _DlBOOTPRetransTime_Type(Integer32):
    """Custom type dlBOOTPRetransTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DlBOOTPRetransTime_Type.__name__ = "Integer32"
_DlBOOTPRetransTime_Object = MibTableColumn
dlBOOTPRetransTime = _DlBOOTPRetransTime_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1, 1, 4),
    _DlBOOTPRetransTime_Type()
)
dlBOOTPRetransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlBOOTPRetransTime.setStatus("mandatory")


class _DlMaxRARPAttempts_Type(Integer32):
    """Custom type dlMaxRARPAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlMaxRARPAttempts_Type.__name__ = "Integer32"
_DlMaxRARPAttempts_Object = MibTableColumn
dlMaxRARPAttempts = _DlMaxRARPAttempts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1, 1, 5),
    _DlMaxRARPAttempts_Type()
)
dlMaxRARPAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlMaxRARPAttempts.setStatus("mandatory")


class _DlRARPRetransTime_Type(Integer32):
    """Custom type dlRARPRetransTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlRARPRetransTime_Type.__name__ = "Integer32"
_DlRARPRetransTime_Object = MibTableColumn
dlRARPRetransTime = _DlRARPRetransTime_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1, 1, 6),
    _DlRARPRetransTime_Type()
)
dlRARPRetransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlRARPRetransTime.setStatus("mandatory")


class _DlMaxTFTPAttempts_Type(Integer32):
    """Custom type dlMaxTFTPAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlMaxTFTPAttempts_Type.__name__ = "Integer32"
_DlMaxTFTPAttempts_Object = MibTableColumn
dlMaxTFTPAttempts = _DlMaxTFTPAttempts_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1, 1, 7),
    _DlMaxTFTPAttempts_Type()
)
dlMaxTFTPAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlMaxTFTPAttempts.setStatus("mandatory")


class _DlTFTPRetransTime_Type(Integer32):
    """Custom type dlTFTPRetransTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DlTFTPRetransTime_Type.__name__ = "Integer32"
_DlTFTPRetransTime_Object = MibTableColumn
dlTFTPRetransTime = _DlTFTPRetransTime_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 1, 1, 8),
    _DlTFTPRetransTime_Type()
)
dlTFTPRetransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTFTPRetransTime.setStatus("mandatory")
_UbBOOTP_ObjectIdentity = ObjectIdentity
ubBOOTP = _UbBOOTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 2)
)
_DlBOOTPOptionsTbl_Object = MibTable
dlBOOTPOptionsTbl = _DlBOOTPOptionsTbl_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dlBOOTPOptionsTbl.setStatus("mandatory")
_DlBOOTPOptionsEntry_Object = MibTableRow
dlBOOTPOptionsEntry = _DlBOOTPOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 2, 1, 1)
)
dlBOOTPOptionsEntry.setIndexNames(
    (0, "UB-INTERNETWORKING-MIB", "dlBOOTPOptionTblEntry"),
)
if mibBuilder.loadTexts:
    dlBOOTPOptionsEntry.setStatus("mandatory")


class _DlBOOTPOptionTblEntry_Type(Integer32):
    """Custom type dlBOOTPOptionTblEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DlBOOTPOptionTblEntry_Type.__name__ = "Integer32"
_DlBOOTPOptionTblEntry_Object = MibTableColumn
dlBOOTPOptionTblEntry = _DlBOOTPOptionTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 2, 1, 1, 1),
    _DlBOOTPOptionTblEntry_Type()
)
dlBOOTPOptionTblEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlBOOTPOptionTblEntry.setStatus("mandatory")
_DlBOOTPHostName_Type = DisplayString
_DlBOOTPHostName_Object = MibTableColumn
dlBOOTPHostName = _DlBOOTPHostName_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 2, 1, 1, 2),
    _DlBOOTPHostName_Type()
)
dlBOOTPHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlBOOTPHostName.setStatus("mandatory")
_DlBOOTPPortAssignTbl_Object = MibTable
dlBOOTPPortAssignTbl = _DlBOOTPPortAssignTbl_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dlBOOTPPortAssignTbl.setStatus("mandatory")
_DlBOOTPPortAssignEntry_Object = MibTableRow
dlBOOTPPortAssignEntry = _DlBOOTPPortAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 2, 2, 1)
)
dlBOOTPPortAssignEntry.setIndexNames(
    (0, "UB-INTERNETWORKING-MIB", "dlBOOTPPortId"),
)
if mibBuilder.loadTexts:
    dlBOOTPPortAssignEntry.setStatus("mandatory")


class _DlBOOTPPortId_Type(Integer32):
    """Custom type dlBOOTPPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fddi", 3),
          ("plusbus", 1),
          ("qe", 2))
    )


_DlBOOTPPortId_Type.__name__ = "Integer32"
_DlBOOTPPortId_Object = MibTableColumn
dlBOOTPPortId = _DlBOOTPPortId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 2, 2, 1, 1),
    _DlBOOTPPortId_Type()
)
dlBOOTPPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlBOOTPPortId.setStatus("mandatory")


class _DlBOOTPOptionsRunning_Type(Integer32):
    """Custom type dlBOOTPOptionsRunning based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("opt-1", 2),
          ("opt-2", 3),
          ("opt-3", 5),
          ("opts-1-2", 4),
          ("opts-1-2-3", 8),
          ("opts-1-3", 6),
          ("opts-2-3", 7))
    )


_DlBOOTPOptionsRunning_Type.__name__ = "Integer32"
_DlBOOTPOptionsRunning_Object = MibTableColumn
dlBOOTPOptionsRunning = _DlBOOTPOptionsRunning_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 2, 2, 1, 2),
    _DlBOOTPOptionsRunning_Type()
)
dlBOOTPOptionsRunning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlBOOTPOptionsRunning.setStatus("mandatory")
_UbTFTP_ObjectIdentity = ObjectIdentity
ubTFTP = _UbTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3)
)
_DlTFTPOptionsTbl_Object = MibTable
dlTFTPOptionsTbl = _DlTFTPOptionsTbl_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dlTFTPOptionsTbl.setStatus("mandatory")
_DlTFTPOptionsEntry_Object = MibTableRow
dlTFTPOptionsEntry = _DlTFTPOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3, 1, 1)
)
dlTFTPOptionsEntry.setIndexNames(
    (0, "UB-INTERNETWORKING-MIB", "dlTFTPOptionTblEntry"),
)
if mibBuilder.loadTexts:
    dlTFTPOptionsEntry.setStatus("mandatory")


class _DlTFTPOptionTblEntry_Type(Integer32):
    """Custom type dlTFTPOptionTblEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DlTFTPOptionTblEntry_Type.__name__ = "Integer32"
_DlTFTPOptionTblEntry_Object = MibTableColumn
dlTFTPOptionTblEntry = _DlTFTPOptionTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3, 1, 1, 1),
    _DlTFTPOptionTblEntry_Type()
)
dlTFTPOptionTblEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlTFTPOptionTblEntry.setStatus("mandatory")
_DlTFTPServerIpAddr_Type = IpAddress
_DlTFTPServerIpAddr_Object = MibTableColumn
dlTFTPServerIpAddr = _DlTFTPServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3, 1, 1, 2),
    _DlTFTPServerIpAddr_Type()
)
dlTFTPServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTFTPServerIpAddr.setStatus("mandatory")
_DlTFTPServerFileName_Type = DisplayString
_DlTFTPServerFileName_Object = MibTableColumn
dlTFTPServerFileName = _DlTFTPServerFileName_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3, 1, 1, 3),
    _DlTFTPServerFileName_Type()
)
dlTFTPServerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTFTPServerFileName.setStatus("mandatory")
_DlTFTPPortAssignTbl_Object = MibTable
dlTFTPPortAssignTbl = _DlTFTPPortAssignTbl_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dlTFTPPortAssignTbl.setStatus("mandatory")
_DlTFTPPortAssignEntry_Object = MibTableRow
dlTFTPPortAssignEntry = _DlTFTPPortAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3, 2, 1)
)
dlTFTPPortAssignEntry.setIndexNames(
    (0, "UB-INTERNETWORKING-MIB", "dlTFTPPortId"),
)
if mibBuilder.loadTexts:
    dlTFTPPortAssignEntry.setStatus("mandatory")


class _DlTFTPPortId_Type(Integer32):
    """Custom type dlTFTPPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fddi", 3),
          ("plusbus", 1),
          ("qe", 2))
    )


_DlTFTPPortId_Type.__name__ = "Integer32"
_DlTFTPPortId_Object = MibTableColumn
dlTFTPPortId = _DlTFTPPortId_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3, 2, 1, 1),
    _DlTFTPPortId_Type()
)
dlTFTPPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlTFTPPortId.setStatus("mandatory")


class _DlTFTPOptionsRunning_Type(Integer32):
    """Custom type dlTFTPOptionsRunning based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("opt-1", 2),
          ("opt-2", 3),
          ("opt-3", 5),
          ("opts-1-2", 4),
          ("opts-1-2-3", 8),
          ("opts-1-3", 6),
          ("opts-2-3", 7))
    )


_DlTFTPOptionsRunning_Type.__name__ = "Integer32"
_DlTFTPOptionsRunning_Object = MibTableColumn
dlTFTPOptionsRunning = _DlTFTPOptionsRunning_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 3, 2, 1, 2),
    _DlTFTPOptionsRunning_Type()
)
dlTFTPOptionsRunning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTFTPOptionsRunning.setStatus("mandatory")
_UbDefaults_ObjectIdentity = ObjectIdentity
ubDefaults = _UbDefaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 4)
)
_DlDefaultTFTPParams_Object = MibTableRow
dlDefaultTFTPParams = _DlDefaultTFTPParams_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dlDefaultTFTPParams.setStatus("mandatory")
_DlTFTPDefaultNodeIpAddr_Type = IpAddress
_DlTFTPDefaultNodeIpAddr_Object = MibTableColumn
dlTFTPDefaultNodeIpAddr = _DlTFTPDefaultNodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 4, 1, 1),
    _DlTFTPDefaultNodeIpAddr_Type()
)
dlTFTPDefaultNodeIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTFTPDefaultNodeIpAddr.setStatus("mandatory")
_DlTFTPDefaultSubnetMask_Type = IpAddress
_DlTFTPDefaultSubnetMask_Object = MibTableColumn
dlTFTPDefaultSubnetMask = _DlTFTPDefaultSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 4, 1, 2),
    _DlTFTPDefaultSubnetMask_Type()
)
dlTFTPDefaultSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTFTPDefaultSubnetMask.setStatus("mandatory")
_DlTFTPDefaultGatewayIpAddr_Type = IpAddress
_DlTFTPDefaultGatewayIpAddr_Object = MibTableColumn
dlTFTPDefaultGatewayIpAddr = _DlTFTPDefaultGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 1, 4, 1, 3),
    _DlTFTPDefaultGatewayIpAddr_Type()
)
dlTFTPDefaultGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTFTPDefaultGatewayIpAddr.setStatus("mandatory")
_UbBridgeParams_Object = MibTableRow
ubBridgeParams = _UbBridgeParams_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ubBridgeParams.setStatus("mandatory")
_UbAgingTime_Type = Integer32
_UbAgingTime_Object = MibTableColumn
ubAgingTime = _UbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 2, 1),
    _UbAgingTime_Type()
)
ubAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubAgingTime.setStatus("mandatory")


class _UbPreForwardingTime_Type(Integer32):
    """Custom type ubPreForwardingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_UbPreForwardingTime_Type.__name__ = "Integer32"
_UbPreForwardingTime_Object = MibTableColumn
ubPreForwardingTime = _UbPreForwardingTime_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 2, 2),
    _UbPreForwardingTime_Type()
)
ubPreForwardingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubPreForwardingTime.setStatus("mandatory")


class _UbAppleTalkSupport_Type(Integer32):
    """Custom type ubAppleTalkSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 2),
          ("phase2", 1))
    )


_UbAppleTalkSupport_Type.__name__ = "Integer32"
_UbAppleTalkSupport_Object = MibTableColumn
ubAppleTalkSupport = _UbAppleTalkSupport_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 2, 3),
    _UbAppleTalkSupport_Type()
)
ubAppleTalkSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubAppleTalkSupport.setStatus("mandatory")
_UbSystemParams_Object = MibTableRow
ubSystemParams = _UbSystemParams_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ubSystemParams.setStatus("mandatory")
_UbBroadcastPktLmt_Type = Counter32
_UbBroadcastPktLmt_Object = MibTableColumn
ubBroadcastPktLmt = _UbBroadcastPktLmt_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 3, 1),
    _UbBroadcastPktLmt_Type()
)
ubBroadcastPktLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubBroadcastPktLmt.setStatus("mandatory")
_UbUnicastPktLmt_Type = Counter32
_UbUnicastPktLmt_Object = MibTableColumn
ubUnicastPktLmt = _UbUnicastPktLmt_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 3, 2),
    _UbUnicastPktLmt_Type()
)
ubUnicastPktLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubUnicastPktLmt.setStatus("mandatory")


class _UbQuickReset_Type(Integer32):
    """Custom type ubQuickReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_UbQuickReset_Type.__name__ = "Integer32"
_UbQuickReset_Object = MibTableColumn
ubQuickReset = _UbQuickReset_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 3, 3),
    _UbQuickReset_Type()
)
ubQuickReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubQuickReset.setStatus("mandatory")


class _UbBasePromCode_Type(DisplayString):
    """Custom type ubBasePromCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbBasePromCode_Type.__name__ = "DisplayString"
_UbBasePromCode_Object = MibTableColumn
ubBasePromCode = _UbBasePromCode_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 3, 4),
    _UbBasePromCode_Type()
)
ubBasePromCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubBasePromCode.setStatus("mandatory")


class _UbOpswPromCode_Type(DisplayString):
    """Custom type ubOpswPromCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbOpswPromCode_Type.__name__ = "DisplayString"
_UbOpswPromCode_Object = MibTableColumn
ubOpswPromCode = _UbOpswPromCode_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 3, 5),
    _UbOpswPromCode_Type()
)
ubOpswPromCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubOpswPromCode.setStatus("mandatory")


class _UbDownloadedCode_Type(DisplayString):
    """Custom type ubDownloadedCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UbDownloadedCode_Type.__name__ = "DisplayString"
_UbDownloadedCode_Object = MibTableColumn
ubDownloadedCode = _UbDownloadedCode_Object(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 1, 5, 3, 6),
    _UbDownloadedCode_Type()
)
ubDownloadedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubDownloadedCode.setStatus("mandatory")
_UbRISCMPET_ObjectIdentity = ObjectIdentity
ubRISCMPET = _UbRISCMPET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 2)
)
_UbRISCTokenRing_ObjectIdentity = ObjectIdentity
ubRISCTokenRing = _UbRISCTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 1, 2, 3)
)
_UbExtInternetworking_ObjectIdentity = ObjectIdentity
ubExtInternetworking = _UbExtInternetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 2)
)
_UbInExt1_ObjectIdentity = ObjectIdentity
ubInExt1 = _UbInExt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 2, 1)
)
_Ubdot1dExt_ObjectIdentity = ObjectIdentity
ubdot1dExt = _Ubdot1dExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1)
)
_Ubdot1dBaseExt_ObjectIdentity = ObjectIdentity
ubdot1dBaseExt = _Ubdot1dBaseExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 1)
)


class _Ubdot1dAdminState_Type(Integer32):
    """Custom type ubdot1dAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_Ubdot1dAdminState_Type.__name__ = "Integer32"
_Ubdot1dAdminState_Object = MibScalar
ubdot1dAdminState = _Ubdot1dAdminState_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 1, 1),
    _Ubdot1dAdminState_Type()
)
ubdot1dAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubdot1dAdminState.setStatus("mandatory")
_Ubdot1dBasePortTable_Object = MibTable
ubdot1dBasePortTable = _Ubdot1dBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ubdot1dBasePortTable.setStatus("mandatory")
_Ubdot1dBasePortEntry_Object = MibTableRow
ubdot1dBasePortEntry = _Ubdot1dBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 1, 2, 1)
)
ubdot1dBasePortEntry.setIndexNames(
    (0, "UB-INTERNETWORKING-MIB", "ubdot1dBasePort"),
)
if mibBuilder.loadTexts:
    ubdot1dBasePortEntry.setStatus("mandatory")
_Ubdot1dBasePort_Type = Integer32
_Ubdot1dBasePort_Object = MibTableColumn
ubdot1dBasePort = _Ubdot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 1, 2, 1, 1),
    _Ubdot1dBasePort_Type()
)
ubdot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubdot1dBasePort.setStatus("mandatory")
_Ubdot1dBasePortBlockedFrames_Type = Counter32
_Ubdot1dBasePortBlockedFrames_Object = MibTableColumn
ubdot1dBasePortBlockedFrames = _Ubdot1dBasePortBlockedFrames_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 1, 2, 1, 2),
    _Ubdot1dBasePortBlockedFrames_Type()
)
ubdot1dBasePortBlockedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubdot1dBasePortBlockedFrames.setStatus("mandatory")
_Ubdot1dProtocolFilterTable_Object = MibTable
ubdot1dProtocolFilterTable = _Ubdot1dProtocolFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ubdot1dProtocolFilterTable.setStatus("mandatory")
_Ubdot1dProtFiltEntry_Object = MibTableRow
ubdot1dProtFiltEntry = _Ubdot1dProtFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 2, 1)
)
ubdot1dProtFiltEntry.setIndexNames(
    (0, "UB-INTERNETWORKING-MIB", "ubdot1dProtFiltType"),
    (0, "UB-INTERNETWORKING-MIB", "ubdot1dProtFiltReceivePort"),
)
if mibBuilder.loadTexts:
    ubdot1dProtFiltEntry.setStatus("mandatory")


class _Ubdot1dProtFiltType_Type(Integer32):
    """Custom type ubdot1dProtFiltType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("unknown", 2)
    )


_Ubdot1dProtFiltType_Type.__name__ = "Integer32"
_Ubdot1dProtFiltType_Object = MibTableColumn
ubdot1dProtFiltType = _Ubdot1dProtFiltType_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 2, 1, 1),
    _Ubdot1dProtFiltType_Type()
)
ubdot1dProtFiltType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubdot1dProtFiltType.setStatus("mandatory")
_Ubdot1dProtFiltReceivePort_Type = Integer32
_Ubdot1dProtFiltReceivePort_Object = MibTableColumn
ubdot1dProtFiltReceivePort = _Ubdot1dProtFiltReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 2, 1, 2),
    _Ubdot1dProtFiltReceivePort_Type()
)
ubdot1dProtFiltReceivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubdot1dProtFiltReceivePort.setStatus("mandatory")
_Ubdot1dProtFiltAllowedToGoTo_Type = OctetString
_Ubdot1dProtFiltAllowedToGoTo_Object = MibScalar
ubdot1dProtFiltAllowedToGoTo = _Ubdot1dProtFiltAllowedToGoTo_Object(
    (1, 3, 6, 1, 4, 1, 75, 2, 1, 1, 2, 1, 3),
    _Ubdot1dProtFiltAllowedToGoTo_Type()
)
ubdot1dProtFiltAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubdot1dProtFiltAllowedToGoTo.setStatus("mandatory")
_UbTrapAttrs_ObjectIdentity = ObjectIdentity
ubTrapAttrs = _UbTrapAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 3)
)
_UbSystem_ObjectIdentity = ObjectIdentity
ubSystem = _UbSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 4)
)
_UbProduct_ObjectIdentity = ObjectIdentity
ubProduct = _UbProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 5)
)
_UbExperimental_ObjectIdentity = ObjectIdentity
ubExperimental = _UbExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 6)
)
_UbExpInternetworking_ObjectIdentity = ObjectIdentity
ubExpInternetworking = _UbExpInternetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 6, 2)
)
_UbInExp1_ObjectIdentity = ObjectIdentity
ubInExp1 = _UbInExp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 6, 2, 1)
)
_UbExtensions_ObjectIdentity = ObjectIdentity
ubExtensions = _UbExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 75, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UB-INTERNETWORKING-MIB",
    **{"ubNode": ubNode,
       "ubEquip": ubEquip,
       "ubInternetworking": ubInternetworking,
       "ubRISCFddiBrouter": ubRISCFddiBrouter,
       "ubInEnc": ubInEnc,
       "encSlots": encSlots,
       "ubInEntity": ubInEntity,
       "ubInCard": ubInCard,
       "controlUb1": controlUb1,
       "login": login,
       "configurationUb1": configurationUb1,
       "slotNum": slotNum,
       "qeContentionOwner": qeContentionOwner,
       "ubInPort": ubInPort,
       "plusbus": plusbus,
       "plusbusTable": plusbusTable,
       "plusbusEntry": plusbusEntry,
       "plusbusIndex": plusbusIndex,
       "plusbusAdminstate": plusbusAdminstate,
       "plusbusAccess": plusbusAccess,
       "plusbusStatsTable": plusbusStatsTable,
       "plusbusStatsEntry": plusbusStatsEntry,
       "plusbusStatsIndex": plusbusStatsIndex,
       "plusbusStatsTxErrors": plusbusStatsTxErrors,
       "plusbusStatsTxlostacks": plusbusStatsTxlostacks,
       "plusbusStatsTxtimeouts": plusbusStatsTxtimeouts,
       "plusbusStatsRxErrors": plusbusStatsRxErrors,
       "plusbusStatsRxtimeouts": plusbusStatsRxtimeouts,
       "plusbusStatsclocklosses": plusbusStatsclocklosses,
       "rxFifoUnderflows": rxFifoUnderflows,
       "ubNVM": ubNVM,
       "ubDownloader": ubDownloader,
       "ubOptions": ubOptions,
       "ubDnloadOptions": ubDnloadOptions,
       "dlVersionID": dlVersionID,
       "dlMaxLoadAttempts": dlMaxLoadAttempts,
       "dlMaxBOOTPAttempts": dlMaxBOOTPAttempts,
       "dlBOOTPRetransTime": dlBOOTPRetransTime,
       "dlMaxRARPAttempts": dlMaxRARPAttempts,
       "dlRARPRetransTime": dlRARPRetransTime,
       "dlMaxTFTPAttempts": dlMaxTFTPAttempts,
       "dlTFTPRetransTime": dlTFTPRetransTime,
       "ubBOOTP": ubBOOTP,
       "dlBOOTPOptionsTbl": dlBOOTPOptionsTbl,
       "dlBOOTPOptionsEntry": dlBOOTPOptionsEntry,
       "dlBOOTPOptionTblEntry": dlBOOTPOptionTblEntry,
       "dlBOOTPHostName": dlBOOTPHostName,
       "dlBOOTPPortAssignTbl": dlBOOTPPortAssignTbl,
       "dlBOOTPPortAssignEntry": dlBOOTPPortAssignEntry,
       "dlBOOTPPortId": dlBOOTPPortId,
       "dlBOOTPOptionsRunning": dlBOOTPOptionsRunning,
       "ubTFTP": ubTFTP,
       "dlTFTPOptionsTbl": dlTFTPOptionsTbl,
       "dlTFTPOptionsEntry": dlTFTPOptionsEntry,
       "dlTFTPOptionTblEntry": dlTFTPOptionTblEntry,
       "dlTFTPServerIpAddr": dlTFTPServerIpAddr,
       "dlTFTPServerFileName": dlTFTPServerFileName,
       "dlTFTPPortAssignTbl": dlTFTPPortAssignTbl,
       "dlTFTPPortAssignEntry": dlTFTPPortAssignEntry,
       "dlTFTPPortId": dlTFTPPortId,
       "dlTFTPOptionsRunning": dlTFTPOptionsRunning,
       "ubDefaults": ubDefaults,
       "dlDefaultTFTPParams": dlDefaultTFTPParams,
       "dlTFTPDefaultNodeIpAddr": dlTFTPDefaultNodeIpAddr,
       "dlTFTPDefaultSubnetMask": dlTFTPDefaultSubnetMask,
       "dlTFTPDefaultGatewayIpAddr": dlTFTPDefaultGatewayIpAddr,
       "ubBridgeParams": ubBridgeParams,
       "ubAgingTime": ubAgingTime,
       "ubPreForwardingTime": ubPreForwardingTime,
       "ubAppleTalkSupport": ubAppleTalkSupport,
       "ubSystemParams": ubSystemParams,
       "ubBroadcastPktLmt": ubBroadcastPktLmt,
       "ubUnicastPktLmt": ubUnicastPktLmt,
       "ubQuickReset": ubQuickReset,
       "ubBasePromCode": ubBasePromCode,
       "ubOpswPromCode": ubOpswPromCode,
       "ubDownloadedCode": ubDownloadedCode,
       "ubRISCMPET": ubRISCMPET,
       "ubRISCTokenRing": ubRISCTokenRing,
       "ubExtInternetworking": ubExtInternetworking,
       "ubInExt1": ubInExt1,
       "ubdot1dExt": ubdot1dExt,
       "ubdot1dBaseExt": ubdot1dBaseExt,
       "ubdot1dAdminState": ubdot1dAdminState,
       "ubdot1dBasePortTable": ubdot1dBasePortTable,
       "ubdot1dBasePortEntry": ubdot1dBasePortEntry,
       "ubdot1dBasePort": ubdot1dBasePort,
       "ubdot1dBasePortBlockedFrames": ubdot1dBasePortBlockedFrames,
       "ubdot1dProtocolFilterTable": ubdot1dProtocolFilterTable,
       "ubdot1dProtFiltEntry": ubdot1dProtFiltEntry,
       "ubdot1dProtFiltType": ubdot1dProtFiltType,
       "ubdot1dProtFiltReceivePort": ubdot1dProtFiltReceivePort,
       "ubdot1dProtFiltAllowedToGoTo": ubdot1dProtFiltAllowedToGoTo,
       "ubTrapAttrs": ubTrapAttrs,
       "ubSystem": ubSystem,
       "ubProduct": ubProduct,
       "ubExperimental": ubExperimental,
       "ubExpInternetworking": ubExpInternetworking,
       "ubInExp1": ubInExp1,
       "ubExtensions": ubExtensions}
)
