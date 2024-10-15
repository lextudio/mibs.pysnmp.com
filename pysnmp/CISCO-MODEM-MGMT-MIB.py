# SNMP MIB module (CISCO-MODEM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MODEM-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:50 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoModemMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47)
)
ciscoModemMgmtMIB.setRevisions(
        ("2005-12-06 00:00",
         "2001-12-01 12:00",
         "2001-10-01 12:00",
         "2000-04-01 00:00",
         "1998-12-16 00:00",
         "1998-06-18 00:00",
         "1997-12-22 00:00",
         "1997-10-13 00:00",
         "1997-07-18 00:00",
         "1998-03-09 00:00",
         "1997-12-16 00:00",
         "1997-05-01 00:00",
         "1997-04-29 00:00",
         "1997-06-11 00:00",
         "1997-03-21 00:00",
         "1997-03-17 00:00",
         "1996-01-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoModemMgmtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoModemMgmtMIBObjects = _CiscoModemMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1)
)
_CmSystemInfo_ObjectIdentity = ObjectIdentity
cmSystemInfo = _CmSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1)
)
_CmSystemInstalledModem_Type = Gauge32
_CmSystemInstalledModem_Object = MibScalar
cmSystemInstalledModem = _CmSystemInstalledModem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 1),
    _CmSystemInstalledModem_Type()
)
cmSystemInstalledModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSystemInstalledModem.setStatus("current")
if mibBuilder.loadTexts:
    cmSystemInstalledModem.setUnits("modems")
_CmSystemConfiguredGroup_Type = Gauge32
_CmSystemConfiguredGroup_Object = MibScalar
cmSystemConfiguredGroup = _CmSystemConfiguredGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 2),
    _CmSystemConfiguredGroup_Type()
)
cmSystemConfiguredGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSystemConfiguredGroup.setStatus("current")


class _CmSystemWatchdogTime_Type(Integer32):
    """Custom type cmSystemWatchdogTime based on Integer32"""
    defaultValue = 6


_CmSystemWatchdogTime_Object = MibScalar
cmSystemWatchdogTime = _CmSystemWatchdogTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 3),
    _CmSystemWatchdogTime_Type()
)
cmSystemWatchdogTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSystemWatchdogTime.setStatus("current")
if mibBuilder.loadTexts:
    cmSystemWatchdogTime.setUnits("minutes")


class _CmSystemStatusPollTime_Type(Integer32):
    """Custom type cmSystemStatusPollTime based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_CmSystemStatusPollTime_Type.__name__ = "Integer32"
_CmSystemStatusPollTime_Object = MibScalar
cmSystemStatusPollTime = _CmSystemStatusPollTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 4),
    _CmSystemStatusPollTime_Type()
)
cmSystemStatusPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSystemStatusPollTime.setStatus("current")
if mibBuilder.loadTexts:
    cmSystemStatusPollTime.setUnits("seconds")


class _CmSystemMaxRetries_Type(Integer32):
    """Custom type cmSystemMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CmSystemMaxRetries_Type.__name__ = "Integer32"
_CmSystemMaxRetries_Object = MibScalar
cmSystemMaxRetries = _CmSystemMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 5),
    _CmSystemMaxRetries_Type()
)
cmSystemMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSystemMaxRetries.setStatus("current")
_CmSystemModemsInUse_Type = Gauge32
_CmSystemModemsInUse_Object = MibScalar
cmSystemModemsInUse = _CmSystemModemsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 6),
    _CmSystemModemsInUse_Type()
)
cmSystemModemsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSystemModemsInUse.setStatus("current")
_CmSystemModemsAvailable_Type = Gauge32
_CmSystemModemsAvailable_Object = MibScalar
cmSystemModemsAvailable = _CmSystemModemsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 7),
    _CmSystemModemsAvailable_Type()
)
cmSystemModemsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSystemModemsAvailable.setStatus("current")
_CmSystemModemsUnavailable_Type = Gauge32
_CmSystemModemsUnavailable_Object = MibScalar
cmSystemModemsUnavailable = _CmSystemModemsUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 8),
    _CmSystemModemsUnavailable_Type()
)
cmSystemModemsUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSystemModemsUnavailable.setStatus("current")
_CmSystemModemsOffline_Type = Gauge32
_CmSystemModemsOffline_Object = MibScalar
cmSystemModemsOffline = _CmSystemModemsOffline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 9),
    _CmSystemModemsOffline_Type()
)
cmSystemModemsOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSystemModemsOffline.setStatus("current")
_CmSystemModemsDead_Type = Gauge32
_CmSystemModemsDead_Object = MibScalar
cmSystemModemsDead = _CmSystemModemsDead_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 1, 10),
    _CmSystemModemsDead_Type()
)
cmSystemModemsDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSystemModemsDead.setStatus("current")
_CmGroupInfo_ObjectIdentity = ObjectIdentity
cmGroupInfo = _CmGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 2)
)
_CmGroupTable_Object = MibTable
cmGroupTable = _CmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmGroupTable.setStatus("current")
_CmGroupEntry_Object = MibTableRow
cmGroupEntry = _CmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 2, 1, 1)
)
cmGroupEntry.setIndexNames(
    (0, "CISCO-MODEM-MGMT-MIB", "cmGroupIndex"),
)
if mibBuilder.loadTexts:
    cmGroupEntry.setStatus("current")
_CmGroupIndex_Type = Unsigned32
_CmGroupIndex_Object = MibTableColumn
cmGroupIndex = _CmGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 2, 1, 1, 1),
    _CmGroupIndex_Type()
)
cmGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmGroupIndex.setStatus("current")
_CmGroupTotalDevices_Type = Integer32
_CmGroupTotalDevices_Object = MibTableColumn
cmGroupTotalDevices = _CmGroupTotalDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 2, 1, 1, 2),
    _CmGroupTotalDevices_Type()
)
cmGroupTotalDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGroupTotalDevices.setStatus("current")
_CmGroupMemberTable_Object = MibTable
cmGroupMemberTable = _CmGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmGroupMemberTable.setStatus("current")
_CmGroupMemberEntry_Object = MibTableRow
cmGroupMemberEntry = _CmGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 2, 2, 1)
)
cmGroupMemberEntry.setIndexNames(
    (0, "CISCO-MODEM-MGMT-MIB", "cmGroupIndex"),
    (0, "CISCO-MODEM-MGMT-MIB", "cmSlotIndex"),
    (0, "CISCO-MODEM-MGMT-MIB", "cmPortIndex"),
)
if mibBuilder.loadTexts:
    cmGroupMemberEntry.setStatus("current")
_CmSlotIndex_Type = Unsigned32
_CmSlotIndex_Object = MibTableColumn
cmSlotIndex = _CmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 2, 2, 1, 1),
    _CmSlotIndex_Type()
)
cmSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmSlotIndex.setStatus("current")
_CmPortIndex_Type = Unsigned32
_CmPortIndex_Object = MibTableColumn
cmPortIndex = _CmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 2, 2, 1, 2),
    _CmPortIndex_Type()
)
cmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPortIndex.setStatus("current")
_CmLineInfo_ObjectIdentity = ObjectIdentity
cmLineInfo = _CmLineInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3)
)
_CmLineStatusTable_Object = MibTable
cmLineStatusTable = _CmLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmLineStatusTable.setStatus("current")
_CmLineStatusEntry_Object = MibTableRow
cmLineStatusEntry = _CmLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1)
)
cmLineStatusEntry.setIndexNames(
    (0, "CISCO-MODEM-MGMT-MIB", "cmSlotIndex"),
    (0, "CISCO-MODEM-MGMT-MIB", "cmPortIndex"),
)
if mibBuilder.loadTexts:
    cmLineStatusEntry.setStatus("current")
_CmInterface_Type = InterfaceIndex
_CmInterface_Object = MibTableColumn
cmInterface = _CmInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 1),
    _CmInterface_Type()
)
cmInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmInterface.setStatus("current")
_CmGroup_Type = Integer32
_CmGroup_Object = MibTableColumn
cmGroup = _CmGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 2),
    _CmGroup_Type()
)
cmGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGroup.setStatus("current")


class _CmManufacturerID_Type(DisplayString):
    """Custom type cmManufacturerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CmManufacturerID_Type.__name__ = "DisplayString"
_CmManufacturerID_Object = MibTableColumn
cmManufacturerID = _CmManufacturerID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 3),
    _CmManufacturerID_Type()
)
cmManufacturerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmManufacturerID.setStatus("current")


class _CmProductDetails_Type(DisplayString):
    """Custom type cmProductDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_CmProductDetails_Type.__name__ = "DisplayString"
_CmProductDetails_Object = MibTableColumn
cmProductDetails = _CmProductDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 4),
    _CmProductDetails_Type()
)
cmProductDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmProductDetails.setStatus("current")
_CmManageable_Type = TruthValue
_CmManageable_Object = MibTableColumn
cmManageable = _CmManageable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 5),
    _CmManageable_Type()
)
cmManageable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmManageable.setStatus("current")


class _CmState_Type(Integer32):
    """Custom type cmState based on Integer32"""
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
        *(("bad", 7),
          ("busiedOut", 5),
          ("connected", 4),
          ("disabled", 6),
          ("downloadFirmware", 9),
          ("downloadFirmwareFailed", 10),
          ("loopback", 8),
          ("offHook", 3),
          ("onHook", 2),
          ("unknown", 1))
    )


_CmState_Type.__name__ = "Integer32"
_CmState_Object = MibTableColumn
cmState = _CmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 6),
    _CmState_Type()
)
cmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmState.setStatus("current")


class _CmCallDirection_Type(Integer32):
    """Custom type cmCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("none", 3),
          ("outgoing", 2))
    )


_CmCallDirection_Type.__name__ = "Integer32"
_CmCallDirection_Object = MibTableColumn
cmCallDirection = _CmCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 7),
    _CmCallDirection_Type()
)
cmCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCallDirection.setStatus("current")


class _CmDisconnectReason_Type(Integer32):
    """Custom type cmDisconnectReason based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("abort", 12),
          ("autoLogonError", 27),
          ("blacklist", 30),
          ("busy", 5),
          ("callbackFailed", 29),
          ("ccpNotSeen", 28),
          ("cdOffTimeout", 34),
          ("codewordSizeMismatch", 35),
          ("compressionProblem", 9),
          ("dialStringError", 14),
          ("dialTimeout", 17),
          ("dspAccessFailure", 33),
          ("dspDownloadFailure", 36),
          ("dtrDrop", 7),
          ("excessiveEC", 24),
          ("fallbackTerminate", 23),
          ("faxClass2Error", 21),
          ("hostDrop", 25),
          ("inactivityTimeout", 13),
          ("lapmProtocolError", 20),
          ("lapmTimeout", 31),
          ("linkFailure", 15),
          ("lostCarrier", 2),
          ("mnp10ProtocolError", 19),
          ("modemDrAborted", 44),
          ("modemDrAbtEndFailure", 51),
          ("modemDrAth", 43),
          ("modemDrBadCmnd", 67),
          ("modemDrBadCopState", 42),
          ("modemDrBadMnp5Rxdata", 40),
          ("modemDrBadNr", 63),
          ("modemDrBadV42bisRxdata", 41),
          ("modemDrConnectTimeout", 45),
          ("modemDrCotAck", 89),
          ("modemDrCotNak1", 90),
          ("modemDrCotNak2", 91),
          ("modemDrCotOff", 92),
          ("modemDrCotTimeout", 93),
          ("modemDrDcCompressionError", 103),
          ("modemDrDcIllegalCharacterSizeStepup", 98),
          ("modemDrDcIllegalCodewordStepup", 94),
          ("modemDrDcIllegalTokenEmptyNode", 95),
          ("modemDrDcIllegalTokenTooLarge", 96),
          ("modemDrDcNegotiationError", 102),
          ("modemDrDcReservedCommand", 97),
          ("modemDrDcRxDictionaryFull", 99),
          ("modemDrDcRxHistoryFull", 100),
          ("modemDrDcRxStringSizeExceeded", 101),
          ("modemDrDisc", 61),
          ("modemDrDm", 62),
          ("modemDrEcTerminated", 39),
          ("modemDrFallbackTerminate", 58),
          ("modemDrFrmrBadCmnd", 68),
          ("modemDrFrmrBadNr", 71),
          ("modemDrFrmrData", 69),
          ("modemDrFrmrLength", 70),
          ("modemDrHostAck", 86),
          ("modemDrHostAth", 83),
          ("modemDrHostBusy", 80),
          ("modemDrHostDtr", 82),
          ("modemDrHostNoAnswer", 81),
          ("modemDrHostNoCarrier", 85),
          ("modemDrHostNoDialtone", 84),
          ("modemDrHostNonspecific", 79),
          ("modemDrInactivity", 56),
          ("modemDrLdInactivity", 76),
          ("modemDrLdLrIncompat", 74),
          ("modemDrLdLrParam1", 73),
          ("modemDrLdNoLr", 72),
          ("modemDrLdProtocol", 77),
          ("modemDrLdRetransLimit", 75),
          ("modemDrLdUser", 78),
          ("modemDrLrIncompat", 54),
          ("modemDrLrOnline", 66),
          ("modemDrLrParam1", 53),
          ("modemDrMohClrd", 87),
          ("modemDrMohTimeout", 88),
          ("modemDrNoAbtDetected", 48),
          ("modemDrNoCarrier", 47),
          ("modemDrNoLr", 52),
          ("modemDrNoXid", 59),
          ("modemDrNone", 37),
          ("modemDrProtocolError", 57),
          ("modemDrResetDsp", 46),
          ("modemDrRetrainLimit", 50),
          ("modemDrRetransmitLimit", 55),
          ("modemDrSabmeOnline", 64),
          ("modemDrSoftwareReset", 38),
          ("modemDrTrainupFailure", 49),
          ("modemDrXidIncompat", 60),
          ("modemDrXidOnline", 65),
          ("modemWatchdogTimeout", 6),
          ("modulationError", 16),
          ("noCarrier", 3),
          ("noDialTone", 4),
          ("reliableLinkTxTimeout", 32),
          ("remoteHangup", 18),
          ("remoteLinkDisconnect", 11),
          ("retrainFailure", 10),
          ("terminate", 26),
          ("trainupFailure", 22),
          ("unknown", 1),
          ("userHangup", 8))
    )


_CmDisconnectReason_Type.__name__ = "Integer32"
_CmDisconnectReason_Object = MibTableColumn
cmDisconnectReason = _CmDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 8),
    _CmDisconnectReason_Type()
)
cmDisconnectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDisconnectReason.setStatus("current")
_CmCallDuration_Type = TimeTicks
_CmCallDuration_Object = MibTableColumn
cmCallDuration = _CmCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 9),
    _CmCallDuration_Type()
)
cmCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCallDuration.setStatus("current")


class _CmCallPhoneNumber_Type(DisplayString):
    """Custom type cmCallPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmCallPhoneNumber_Type.__name__ = "DisplayString"
_CmCallPhoneNumber_Object = MibTableColumn
cmCallPhoneNumber = _CmCallPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 10),
    _CmCallPhoneNumber_Type()
)
cmCallPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCallPhoneNumber.setStatus("current")


class _CmCallerID_Type(DisplayString):
    """Custom type cmCallerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmCallerID_Type.__name__ = "DisplayString"
_CmCallerID_Object = MibTableColumn
cmCallerID = _CmCallerID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 11),
    _CmCallerID_Type()
)
cmCallerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCallerID.setStatus("current")


class _CmModulationSchemeUsed_Type(Integer32):
    """Custom type cmModulationSchemeUsed based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("bell103a", 2),
          ("bell212a", 3),
          ("k56flex", 14),
          ("piafs", 21),
          ("unknown", 1),
          ("v110", 20),
          ("v17", 11),
          ("v21", 4),
          ("v22", 5),
          ("v22bis", 6),
          ("v23", 15),
          ("v27ter", 19),
          ("v29", 12),
          ("v32", 7),
          ("v32bis", 8),
          ("v32terbo", 16),
          ("v33", 13),
          ("v34", 10),
          ("v34plus", 17),
          ("v90", 18),
          ("vfc", 9))
    )


_CmModulationSchemeUsed_Type.__name__ = "Integer32"
_CmModulationSchemeUsed_Object = MibTableColumn
cmModulationSchemeUsed = _CmModulationSchemeUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 12),
    _CmModulationSchemeUsed_Type()
)
cmModulationSchemeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmModulationSchemeUsed.setStatus("current")


class _CmProtocolUsed_Type(Integer32):
    """Custom type cmProtocolUsed based on Integer32"""
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
        *(("ara10", 7),
          ("ara20", 8),
          ("asyncMode", 6),
          ("direct", 2),
          ("normal", 1),
          ("reliableLAPM", 4),
          ("reliableMNP", 3),
          ("syncMode", 5),
          ("unknown", 9))
    )


_CmProtocolUsed_Type.__name__ = "Integer32"
_CmProtocolUsed_Object = MibTableColumn
cmProtocolUsed = _CmProtocolUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 13),
    _CmProtocolUsed_Type()
)
cmProtocolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmProtocolUsed.setStatus("current")
_CmTXRate_Type = Gauge32
_CmTXRate_Object = MibTableColumn
cmTXRate = _CmTXRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 14),
    _CmTXRate_Type()
)
cmTXRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTXRate.setStatus("current")
if mibBuilder.loadTexts:
    cmTXRate.setUnits("bits/second")
_CmRXRate_Type = Gauge32
_CmRXRate_Object = MibTableColumn
cmRXRate = _CmRXRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 15),
    _CmRXRate_Type()
)
cmRXRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRXRate.setStatus("current")
if mibBuilder.loadTexts:
    cmRXRate.setUnits("bits/second")


class _CmTXAnalogSignalLevel_Type(Integer32):
    """Custom type cmTXAnalogSignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-43, -9),
        ValueRangeConstraint(0, 0),
    )


_CmTXAnalogSignalLevel_Type.__name__ = "Integer32"
_CmTXAnalogSignalLevel_Object = MibTableColumn
cmTXAnalogSignalLevel = _CmTXAnalogSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 16),
    _CmTXAnalogSignalLevel_Type()
)
cmTXAnalogSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTXAnalogSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    cmTXAnalogSignalLevel.setUnits("dBm")


class _CmRXAnalogSignalLevel_Type(Integer32):
    """Custom type cmRXAnalogSignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -1),
        ValueRangeConstraint(0, 0),
    )


_CmRXAnalogSignalLevel_Type.__name__ = "Integer32"
_CmRXAnalogSignalLevel_Object = MibTableColumn
cmRXAnalogSignalLevel = _CmRXAnalogSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 1, 1, 17),
    _CmRXAnalogSignalLevel_Type()
)
cmRXAnalogSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRXAnalogSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    cmRXAnalogSignalLevel.setUnits("dBm")
_CmLineConfigTable_Object = MibTable
cmLineConfigTable = _CmLineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cmLineConfigTable.setStatus("current")
_CmLineConfigEntry_Object = MibTableRow
cmLineConfigEntry = _CmLineConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cmLineConfigEntry.setStatus("current")


class _CmATModePermit_Type(TruthValue):
    """Custom type cmATModePermit based on TruthValue"""


_CmATModePermit_Object = MibTableColumn
cmATModePermit = _CmATModePermit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 2, 1, 1),
    _CmATModePermit_Type()
)
cmATModePermit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmATModePermit.setStatus("current")


class _CmStatusPolling_Type(TruthValue):
    """Custom type cmStatusPolling based on TruthValue"""


_CmStatusPolling_Object = MibTableColumn
cmStatusPolling = _CmStatusPolling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 2, 1, 2),
    _CmStatusPolling_Type()
)
cmStatusPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmStatusPolling.setStatus("current")


class _CmBusyOutRequest_Type(TruthValue):
    """Custom type cmBusyOutRequest based on TruthValue"""


_CmBusyOutRequest_Object = MibTableColumn
cmBusyOutRequest = _CmBusyOutRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 2, 1, 3),
    _CmBusyOutRequest_Type()
)
cmBusyOutRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBusyOutRequest.setStatus("current")


class _CmShutdown_Type(TruthValue):
    """Custom type cmShutdown based on TruthValue"""


_CmShutdown_Object = MibTableColumn
cmShutdown = _CmShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 2, 1, 4),
    _CmShutdown_Type()
)
cmShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmShutdown.setStatus("current")


class _CmHoldReset_Type(TruthValue):
    """Custom type cmHoldReset based on TruthValue"""


_CmHoldReset_Object = MibTableColumn
cmHoldReset = _CmHoldReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 2, 1, 5),
    _CmHoldReset_Type()
)
cmHoldReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHoldReset.setStatus("current")


class _CmBad_Type(TruthValue):
    """Custom type cmBad based on TruthValue"""


_CmBad_Object = MibTableColumn
cmBad = _CmBad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 2, 1, 6),
    _CmBad_Type()
)
cmBad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBad.setStatus("current")
_CmLineStatisticsTable_Object = MibTable
cmLineStatisticsTable = _CmLineStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cmLineStatisticsTable.setStatus("current")
_CmLineStatisticsEntry_Object = MibTableRow
cmLineStatisticsEntry = _CmLineStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cmLineStatisticsEntry.setStatus("current")
_CmRingNoAnswers_Type = Counter32
_CmRingNoAnswers_Object = MibTableColumn
cmRingNoAnswers = _CmRingNoAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 1),
    _CmRingNoAnswers_Type()
)
cmRingNoAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRingNoAnswers.setStatus("current")
if mibBuilder.loadTexts:
    cmRingNoAnswers.setUnits("calls")
_CmIncomingConnectionFailures_Type = Counter32
_CmIncomingConnectionFailures_Object = MibTableColumn
cmIncomingConnectionFailures = _CmIncomingConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 2),
    _CmIncomingConnectionFailures_Type()
)
cmIncomingConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIncomingConnectionFailures.setStatus("current")
if mibBuilder.loadTexts:
    cmIncomingConnectionFailures.setUnits("calls")
_CmIncomingConnectionCompletions_Type = Counter32
_CmIncomingConnectionCompletions_Object = MibTableColumn
cmIncomingConnectionCompletions = _CmIncomingConnectionCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 3),
    _CmIncomingConnectionCompletions_Type()
)
cmIncomingConnectionCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIncomingConnectionCompletions.setStatus("current")
if mibBuilder.loadTexts:
    cmIncomingConnectionCompletions.setUnits("calls")
_CmOutgoingConnectionFailures_Type = Counter32
_CmOutgoingConnectionFailures_Object = MibTableColumn
cmOutgoingConnectionFailures = _CmOutgoingConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 4),
    _CmOutgoingConnectionFailures_Type()
)
cmOutgoingConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOutgoingConnectionFailures.setStatus("current")
if mibBuilder.loadTexts:
    cmOutgoingConnectionFailures.setUnits("calls")
_CmOutgoingConnectionCompletions_Type = Counter32
_CmOutgoingConnectionCompletions_Object = MibTableColumn
cmOutgoingConnectionCompletions = _CmOutgoingConnectionCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 5),
    _CmOutgoingConnectionCompletions_Type()
)
cmOutgoingConnectionCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOutgoingConnectionCompletions.setStatus("current")
if mibBuilder.loadTexts:
    cmOutgoingConnectionCompletions.setUnits("calls")
_CmFailedDialAttempts_Type = Counter32
_CmFailedDialAttempts_Object = MibTableColumn
cmFailedDialAttempts = _CmFailedDialAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 6),
    _CmFailedDialAttempts_Type()
)
cmFailedDialAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFailedDialAttempts.setStatus("current")
if mibBuilder.loadTexts:
    cmFailedDialAttempts.setUnits("calls")
_CmNoDialTones_Type = Counter32
_CmNoDialTones_Object = MibTableColumn
cmNoDialTones = _CmNoDialTones_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 7),
    _CmNoDialTones_Type()
)
cmNoDialTones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNoDialTones.setStatus("current")
if mibBuilder.loadTexts:
    cmNoDialTones.setUnits("calls")
_CmDialTimeouts_Type = Counter32
_CmDialTimeouts_Object = MibTableColumn
cmDialTimeouts = _CmDialTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 8),
    _CmDialTimeouts_Type()
)
cmDialTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDialTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    cmDialTimeouts.setUnits("calls")
_CmWatchdogTimeouts_Type = Counter32
_CmWatchdogTimeouts_Object = MibTableColumn
cmWatchdogTimeouts = _CmWatchdogTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 9),
    _CmWatchdogTimeouts_Type()
)
cmWatchdogTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmWatchdogTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    cmWatchdogTimeouts.setUnits("calls")
_Cm2400OrLessConnections_Type = Counter32
_Cm2400OrLessConnections_Object = MibTableColumn
cm2400OrLessConnections = _Cm2400OrLessConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 10),
    _Cm2400OrLessConnections_Type()
)
cm2400OrLessConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cm2400OrLessConnections.setStatus("deprecated")
if mibBuilder.loadTexts:
    cm2400OrLessConnections.setUnits("calls")
_Cm2400To14400Connections_Type = Counter32
_Cm2400To14400Connections_Object = MibTableColumn
cm2400To14400Connections = _Cm2400To14400Connections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 11),
    _Cm2400To14400Connections_Type()
)
cm2400To14400Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cm2400To14400Connections.setStatus("deprecated")
if mibBuilder.loadTexts:
    cm2400To14400Connections.setUnits("calls")
_CmGreaterThan14400Connections_Type = Counter32
_CmGreaterThan14400Connections_Object = MibTableColumn
cmGreaterThan14400Connections = _CmGreaterThan14400Connections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 12),
    _CmGreaterThan14400Connections_Type()
)
cmGreaterThan14400Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGreaterThan14400Connections.setStatus("deprecated")
if mibBuilder.loadTexts:
    cmGreaterThan14400Connections.setUnits("calls")
_CmNoCarriers_Type = Counter32
_CmNoCarriers_Object = MibTableColumn
cmNoCarriers = _CmNoCarriers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 13),
    _CmNoCarriers_Type()
)
cmNoCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNoCarriers.setStatus("current")
if mibBuilder.loadTexts:
    cmNoCarriers.setUnits("calls")
_CmLinkFailures_Type = Counter32
_CmLinkFailures_Object = MibTableColumn
cmLinkFailures = _CmLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 14),
    _CmLinkFailures_Type()
)
cmLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLinkFailures.setStatus("current")
if mibBuilder.loadTexts:
    cmLinkFailures.setUnits("calls")
_CmProtocolErrors_Type = Counter32
_CmProtocolErrors_Object = MibTableColumn
cmProtocolErrors = _CmProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 15),
    _CmProtocolErrors_Type()
)
cmProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmProtocolErrors.setStatus("current")
if mibBuilder.loadTexts:
    cmProtocolErrors.setUnits("errors")
_CmPollingTimeouts_Type = Counter32
_CmPollingTimeouts_Object = MibTableColumn
cmPollingTimeouts = _CmPollingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 16),
    _CmPollingTimeouts_Type()
)
cmPollingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPollingTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    cmPollingTimeouts.setUnits("errors")
_CmTotalCallDuration_Type = Counter32
_CmTotalCallDuration_Object = MibTableColumn
cmTotalCallDuration = _CmTotalCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 3, 1, 17),
    _CmTotalCallDuration_Type()
)
cmTotalCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTotalCallDuration.setStatus("current")
if mibBuilder.loadTexts:
    cmTotalCallDuration.setUnits("seconds")
_CmLineSpeedStatisticsTable_Object = MibTable
cmLineSpeedStatisticsTable = _CmLineSpeedStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cmLineSpeedStatisticsTable.setStatus("current")
_CmLineSpeedStatisticsEntry_Object = MibTableRow
cmLineSpeedStatisticsEntry = _CmLineSpeedStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 4, 1)
)
cmLineSpeedStatisticsEntry.setIndexNames(
    (0, "CISCO-MODEM-MGMT-MIB", "cmSlotIndex"),
    (0, "CISCO-MODEM-MGMT-MIB", "cmPortIndex"),
    (0, "CISCO-MODEM-MGMT-MIB", "cmInitialLineSpeed"),
)
if mibBuilder.loadTexts:
    cmLineSpeedStatisticsEntry.setStatus("current")
_CmInitialLineSpeed_Type = Unsigned32
_CmInitialLineSpeed_Object = MibTableColumn
cmInitialLineSpeed = _CmInitialLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 4, 1, 1),
    _CmInitialLineSpeed_Type()
)
cmInitialLineSpeed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmInitialLineSpeed.setStatus("current")
_CmInitialLineConnections_Type = Counter32
_CmInitialLineConnections_Object = MibTableColumn
cmInitialLineConnections = _CmInitialLineConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 4, 1, 2),
    _CmInitialLineConnections_Type()
)
cmInitialLineConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmInitialLineConnections.setStatus("deprecated")
if mibBuilder.loadTexts:
    cmInitialLineConnections.setUnits("calls")
_CmInitialTxLineConnections_Type = Counter32
_CmInitialTxLineConnections_Object = MibTableColumn
cmInitialTxLineConnections = _CmInitialTxLineConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 4, 1, 3),
    _CmInitialTxLineConnections_Type()
)
cmInitialTxLineConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmInitialTxLineConnections.setStatus("current")
if mibBuilder.loadTexts:
    cmInitialTxLineConnections.setUnits("calls")
_CmInitialRxLineConnections_Type = Counter32
_CmInitialRxLineConnections_Object = MibTableColumn
cmInitialRxLineConnections = _CmInitialRxLineConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 3, 4, 1, 4),
    _CmInitialRxLineConnections_Type()
)
cmInitialRxLineConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmInitialRxLineConnections.setStatus("current")
if mibBuilder.loadTexts:
    cmInitialRxLineConnections.setUnits("calls")
_CmNotificationConfig_ObjectIdentity = ObjectIdentity
cmNotificationConfig = _CmNotificationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 4)
)
_CmStateNotifyEnable_Type = TruthValue
_CmStateNotifyEnable_Object = MibScalar
cmStateNotifyEnable = _CmStateNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 1, 4, 1),
    _CmStateNotifyEnable_Type()
)
cmStateNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmStateNotifyEnable.setStatus("current")
_CmMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cmMIBNotificationPrefix = _CmMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 2)
)
_CmMIBNotifications_ObjectIdentity = ObjectIdentity
cmMIBNotifications = _CmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 2, 0)
)
_CiscoModemMgmtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoModemMgmtMIBConformance = _CiscoModemMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3)
)
_CiscoModemMgmtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoModemMgmtMIBCompliances = _CiscoModemMgmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 1)
)
_CiscoModemMgmtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoModemMgmtMIBGroups = _CiscoModemMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2)
)
cmLineStatusEntry.registerAugmentions(
    ("CISCO-MODEM-MGMT-MIB",
     "cmLineConfigEntry")
)
cmLineConfigEntry.setIndexNames(*cmLineStatusEntry.getIndexNames())
cmLineStatusEntry.registerAugmentions(
    ("CISCO-MODEM-MGMT-MIB",
     "cmLineStatisticsEntry")
)
cmLineStatisticsEntry.setIndexNames(*cmLineStatusEntry.getIndexNames())

# Managed Objects groups

cmSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 1)
)
cmSystemInfoGroup.setObjects(
      *(("CISCO-MODEM-MGMT-MIB", "cmSystemInstalledModem"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemConfiguredGroup"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemWatchdogTime"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemStatusPollTime"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemMaxRetries"))
)
if mibBuilder.loadTexts:
    cmSystemInfoGroup.setStatus("obsolete")

cmGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 2)
)
cmGroupInfoGroup.setObjects(
      *(("CISCO-MODEM-MGMT-MIB", "cmGroupTotalDevices"),
        ("CISCO-MODEM-MGMT-MIB", "cmPortIndex"))
)
if mibBuilder.loadTexts:
    cmGroupInfoGroup.setStatus("current")

cmLineInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 3)
)
cmLineInfoGroup.setObjects(
      *(("CISCO-MODEM-MGMT-MIB", "cmInterface"),
        ("CISCO-MODEM-MGMT-MIB", "cmGroup"),
        ("CISCO-MODEM-MGMT-MIB", "cmManufacturerID"),
        ("CISCO-MODEM-MGMT-MIB", "cmProductDetails"),
        ("CISCO-MODEM-MGMT-MIB", "cmManageable"),
        ("CISCO-MODEM-MGMT-MIB", "cmState"),
        ("CISCO-MODEM-MGMT-MIB", "cmDisconnectReason"),
        ("CISCO-MODEM-MGMT-MIB", "cmCallDirection"),
        ("CISCO-MODEM-MGMT-MIB", "cmCallDuration"),
        ("CISCO-MODEM-MGMT-MIB", "cmCallPhoneNumber"),
        ("CISCO-MODEM-MGMT-MIB", "cmCallerID"),
        ("CISCO-MODEM-MGMT-MIB", "cmATModePermit"),
        ("CISCO-MODEM-MGMT-MIB", "cmStatusPolling"),
        ("CISCO-MODEM-MGMT-MIB", "cmBusyOutRequest"),
        ("CISCO-MODEM-MGMT-MIB", "cmShutdown"),
        ("CISCO-MODEM-MGMT-MIB", "cmHoldReset"),
        ("CISCO-MODEM-MGMT-MIB", "cmBad"),
        ("CISCO-MODEM-MGMT-MIB", "cmRingNoAnswers"),
        ("CISCO-MODEM-MGMT-MIB", "cmFailedDialAttempts"),
        ("CISCO-MODEM-MGMT-MIB", "cmWatchdogTimeouts"))
)
if mibBuilder.loadTexts:
    cmLineInfoGroup.setStatus("current")

cmManagedLineInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 4)
)
cmManagedLineInfoGroup.setObjects(
      *(("CISCO-MODEM-MGMT-MIB", "cmModulationSchemeUsed"),
        ("CISCO-MODEM-MGMT-MIB", "cmProtocolUsed"),
        ("CISCO-MODEM-MGMT-MIB", "cmTXRate"),
        ("CISCO-MODEM-MGMT-MIB", "cmRXRate"),
        ("CISCO-MODEM-MGMT-MIB", "cmTXAnalogSignalLevel"),
        ("CISCO-MODEM-MGMT-MIB", "cmRXAnalogSignalLevel"),
        ("CISCO-MODEM-MGMT-MIB", "cmIncomingConnectionFailures"),
        ("CISCO-MODEM-MGMT-MIB", "cmIncomingConnectionCompletions"),
        ("CISCO-MODEM-MGMT-MIB", "cmOutgoingConnectionFailures"),
        ("CISCO-MODEM-MGMT-MIB", "cmOutgoingConnectionCompletions"),
        ("CISCO-MODEM-MGMT-MIB", "cmNoDialTones"),
        ("CISCO-MODEM-MGMT-MIB", "cmDialTimeouts"),
        ("CISCO-MODEM-MGMT-MIB", "cm2400OrLessConnections"),
        ("CISCO-MODEM-MGMT-MIB", "cm2400To14400Connections"),
        ("CISCO-MODEM-MGMT-MIB", "cmGreaterThan14400Connections"),
        ("CISCO-MODEM-MGMT-MIB", "cmNoCarriers"),
        ("CISCO-MODEM-MGMT-MIB", "cmLinkFailures"),
        ("CISCO-MODEM-MGMT-MIB", "cmProtocolErrors"),
        ("CISCO-MODEM-MGMT-MIB", "cmPollingTimeouts"),
        ("CISCO-MODEM-MGMT-MIB", "cmTotalCallDuration"))
)
if mibBuilder.loadTexts:
    cmManagedLineInfoGroup.setStatus("deprecated")

cmLineSpeedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 5)
)
cmLineSpeedInfoGroup.setObjects(
    ("CISCO-MODEM-MGMT-MIB", "cmInitialLineConnections")
)
if mibBuilder.loadTexts:
    cmLineSpeedInfoGroup.setStatus("obsolete")

cmSystemInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 6)
)
cmSystemInfoGroupRev1.setObjects(
      *(("CISCO-MODEM-MGMT-MIB", "cmSystemInstalledModem"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemConfiguredGroup"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemWatchdogTime"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemStatusPollTime"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemMaxRetries"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemModemsInUse"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemModemsAvailable"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemModemsUnavailable"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemModemsOffline"),
        ("CISCO-MODEM-MGMT-MIB", "cmSystemModemsDead"))
)
if mibBuilder.loadTexts:
    cmSystemInfoGroupRev1.setStatus("current")

cmLineSpeedInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 7)
)
cmLineSpeedInfoGroupRev1.setObjects(
      *(("CISCO-MODEM-MGMT-MIB", "cmInitialLineConnections"),
        ("CISCO-MODEM-MGMT-MIB", "cmInitialTxLineConnections"),
        ("CISCO-MODEM-MGMT-MIB", "cmInitialRxLineConnections"))
)
if mibBuilder.loadTexts:
    cmLineSpeedInfoGroupRev1.setStatus("deprecated")

cmManagedLineInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 8)
)
cmManagedLineInfoGroupRev1.setObjects(
      *(("CISCO-MODEM-MGMT-MIB", "cmModulationSchemeUsed"),
        ("CISCO-MODEM-MGMT-MIB", "cmProtocolUsed"),
        ("CISCO-MODEM-MGMT-MIB", "cmTXRate"),
        ("CISCO-MODEM-MGMT-MIB", "cmRXRate"),
        ("CISCO-MODEM-MGMT-MIB", "cmTXAnalogSignalLevel"),
        ("CISCO-MODEM-MGMT-MIB", "cmRXAnalogSignalLevel"),
        ("CISCO-MODEM-MGMT-MIB", "cmIncomingConnectionFailures"),
        ("CISCO-MODEM-MGMT-MIB", "cmIncomingConnectionCompletions"),
        ("CISCO-MODEM-MGMT-MIB", "cmOutgoingConnectionFailures"),
        ("CISCO-MODEM-MGMT-MIB", "cmOutgoingConnectionCompletions"),
        ("CISCO-MODEM-MGMT-MIB", "cmNoDialTones"),
        ("CISCO-MODEM-MGMT-MIB", "cmDialTimeouts"),
        ("CISCO-MODEM-MGMT-MIB", "cm2400OrLessConnections"),
        ("CISCO-MODEM-MGMT-MIB", "cm2400To14400Connections"),
        ("CISCO-MODEM-MGMT-MIB", "cmGreaterThan14400Connections"),
        ("CISCO-MODEM-MGMT-MIB", "cmNoCarriers"),
        ("CISCO-MODEM-MGMT-MIB", "cmLinkFailures"),
        ("CISCO-MODEM-MGMT-MIB", "cmProtocolErrors"),
        ("CISCO-MODEM-MGMT-MIB", "cmPollingTimeouts"),
        ("CISCO-MODEM-MGMT-MIB", "cmTotalCallDuration"))
)
if mibBuilder.loadTexts:
    cmManagedLineInfoGroupRev1.setStatus("deprecated")

cmNotificationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 9)
)
cmNotificationConfigGroup.setObjects(
    ("CISCO-MODEM-MGMT-MIB", "cmStateNotifyEnable")
)
if mibBuilder.loadTexts:
    cmNotificationConfigGroup.setStatus("current")

cmLineSpeedInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 11)
)
cmLineSpeedInfoGroupRev2.setObjects(
      *(("CISCO-MODEM-MGMT-MIB", "cmInitialTxLineConnections"),
        ("CISCO-MODEM-MGMT-MIB", "cmInitialRxLineConnections"))
)
if mibBuilder.loadTexts:
    cmLineSpeedInfoGroupRev2.setStatus("current")

cmManagedLineInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 12)
)
cmManagedLineInfoGroupRev2.setObjects(
      *(("CISCO-MODEM-MGMT-MIB", "cmModulationSchemeUsed"),
        ("CISCO-MODEM-MGMT-MIB", "cmProtocolUsed"),
        ("CISCO-MODEM-MGMT-MIB", "cmTXRate"),
        ("CISCO-MODEM-MGMT-MIB", "cmRXRate"),
        ("CISCO-MODEM-MGMT-MIB", "cmTXAnalogSignalLevel"),
        ("CISCO-MODEM-MGMT-MIB", "cmRXAnalogSignalLevel"),
        ("CISCO-MODEM-MGMT-MIB", "cmIncomingConnectionFailures"),
        ("CISCO-MODEM-MGMT-MIB", "cmIncomingConnectionCompletions"),
        ("CISCO-MODEM-MGMT-MIB", "cmOutgoingConnectionFailures"),
        ("CISCO-MODEM-MGMT-MIB", "cmOutgoingConnectionCompletions"),
        ("CISCO-MODEM-MGMT-MIB", "cmNoDialTones"),
        ("CISCO-MODEM-MGMT-MIB", "cmDialTimeouts"),
        ("CISCO-MODEM-MGMT-MIB", "cmNoCarriers"),
        ("CISCO-MODEM-MGMT-MIB", "cmLinkFailures"),
        ("CISCO-MODEM-MGMT-MIB", "cmProtocolErrors"),
        ("CISCO-MODEM-MGMT-MIB", "cmPollingTimeouts"),
        ("CISCO-MODEM-MGMT-MIB", "cmTotalCallDuration"))
)
if mibBuilder.loadTexts:
    cmManagedLineInfoGroupRev2.setStatus("current")


# Notification objects

cmStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 2, 0, 1)
)
cmStateNotification.setObjects(
    ("CISCO-MODEM-MGMT-MIB", "cmState")
)
if mibBuilder.loadTexts:
    cmStateNotification.setStatus(
        "current"
    )


# Notifications groups

cmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 2, 10)
)
cmNotificationGroup.setObjects(
    ("CISCO-MODEM-MGMT-MIB", "cmStateNotification")
)
if mibBuilder.loadTexts:
    cmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoModemMgmtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoModemMgmtMIBCompliance.setStatus(
        "obsolete"
    )

ciscoModemMgmtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoModemMgmtMIBComplianceRev1.setStatus(
        "obsolete"
    )

ciscoModemMgmtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoModemMgmtMIBComplianceRev2.setStatus(
        "obsolete"
    )

ciscoModemMgmtMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoModemMgmtMIBComplianceRev3.setStatus(
        "obsolete"
    )

ciscoModemMgmtMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoModemMgmtMIBComplianceRev4.setStatus(
        "obsolete"
    )

ciscoModemMgmtMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoModemMgmtMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoModemMgmtMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 47, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoModemMgmtMIBComplianceRev6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MODEM-MGMT-MIB",
    **{"ciscoModemMgmtMIB": ciscoModemMgmtMIB,
       "ciscoModemMgmtMIBObjects": ciscoModemMgmtMIBObjects,
       "cmSystemInfo": cmSystemInfo,
       "cmSystemInstalledModem": cmSystemInstalledModem,
       "cmSystemConfiguredGroup": cmSystemConfiguredGroup,
       "cmSystemWatchdogTime": cmSystemWatchdogTime,
       "cmSystemStatusPollTime": cmSystemStatusPollTime,
       "cmSystemMaxRetries": cmSystemMaxRetries,
       "cmSystemModemsInUse": cmSystemModemsInUse,
       "cmSystemModemsAvailable": cmSystemModemsAvailable,
       "cmSystemModemsUnavailable": cmSystemModemsUnavailable,
       "cmSystemModemsOffline": cmSystemModemsOffline,
       "cmSystemModemsDead": cmSystemModemsDead,
       "cmGroupInfo": cmGroupInfo,
       "cmGroupTable": cmGroupTable,
       "cmGroupEntry": cmGroupEntry,
       "cmGroupIndex": cmGroupIndex,
       "cmGroupTotalDevices": cmGroupTotalDevices,
       "cmGroupMemberTable": cmGroupMemberTable,
       "cmGroupMemberEntry": cmGroupMemberEntry,
       "cmSlotIndex": cmSlotIndex,
       "cmPortIndex": cmPortIndex,
       "cmLineInfo": cmLineInfo,
       "cmLineStatusTable": cmLineStatusTable,
       "cmLineStatusEntry": cmLineStatusEntry,
       "cmInterface": cmInterface,
       "cmGroup": cmGroup,
       "cmManufacturerID": cmManufacturerID,
       "cmProductDetails": cmProductDetails,
       "cmManageable": cmManageable,
       "cmState": cmState,
       "cmCallDirection": cmCallDirection,
       "cmDisconnectReason": cmDisconnectReason,
       "cmCallDuration": cmCallDuration,
       "cmCallPhoneNumber": cmCallPhoneNumber,
       "cmCallerID": cmCallerID,
       "cmModulationSchemeUsed": cmModulationSchemeUsed,
       "cmProtocolUsed": cmProtocolUsed,
       "cmTXRate": cmTXRate,
       "cmRXRate": cmRXRate,
       "cmTXAnalogSignalLevel": cmTXAnalogSignalLevel,
       "cmRXAnalogSignalLevel": cmRXAnalogSignalLevel,
       "cmLineConfigTable": cmLineConfigTable,
       "cmLineConfigEntry": cmLineConfigEntry,
       "cmATModePermit": cmATModePermit,
       "cmStatusPolling": cmStatusPolling,
       "cmBusyOutRequest": cmBusyOutRequest,
       "cmShutdown": cmShutdown,
       "cmHoldReset": cmHoldReset,
       "cmBad": cmBad,
       "cmLineStatisticsTable": cmLineStatisticsTable,
       "cmLineStatisticsEntry": cmLineStatisticsEntry,
       "cmRingNoAnswers": cmRingNoAnswers,
       "cmIncomingConnectionFailures": cmIncomingConnectionFailures,
       "cmIncomingConnectionCompletions": cmIncomingConnectionCompletions,
       "cmOutgoingConnectionFailures": cmOutgoingConnectionFailures,
       "cmOutgoingConnectionCompletions": cmOutgoingConnectionCompletions,
       "cmFailedDialAttempts": cmFailedDialAttempts,
       "cmNoDialTones": cmNoDialTones,
       "cmDialTimeouts": cmDialTimeouts,
       "cmWatchdogTimeouts": cmWatchdogTimeouts,
       "cm2400OrLessConnections": cm2400OrLessConnections,
       "cm2400To14400Connections": cm2400To14400Connections,
       "cmGreaterThan14400Connections": cmGreaterThan14400Connections,
       "cmNoCarriers": cmNoCarriers,
       "cmLinkFailures": cmLinkFailures,
       "cmProtocolErrors": cmProtocolErrors,
       "cmPollingTimeouts": cmPollingTimeouts,
       "cmTotalCallDuration": cmTotalCallDuration,
       "cmLineSpeedStatisticsTable": cmLineSpeedStatisticsTable,
       "cmLineSpeedStatisticsEntry": cmLineSpeedStatisticsEntry,
       "cmInitialLineSpeed": cmInitialLineSpeed,
       "cmInitialLineConnections": cmInitialLineConnections,
       "cmInitialTxLineConnections": cmInitialTxLineConnections,
       "cmInitialRxLineConnections": cmInitialRxLineConnections,
       "cmNotificationConfig": cmNotificationConfig,
       "cmStateNotifyEnable": cmStateNotifyEnable,
       "cmMIBNotificationPrefix": cmMIBNotificationPrefix,
       "cmMIBNotifications": cmMIBNotifications,
       "cmStateNotification": cmStateNotification,
       "ciscoModemMgmtMIBConformance": ciscoModemMgmtMIBConformance,
       "ciscoModemMgmtMIBCompliances": ciscoModemMgmtMIBCompliances,
       "ciscoModemMgmtMIBCompliance": ciscoModemMgmtMIBCompliance,
       "ciscoModemMgmtMIBComplianceRev1": ciscoModemMgmtMIBComplianceRev1,
       "ciscoModemMgmtMIBComplianceRev2": ciscoModemMgmtMIBComplianceRev2,
       "ciscoModemMgmtMIBComplianceRev3": ciscoModemMgmtMIBComplianceRev3,
       "ciscoModemMgmtMIBComplianceRev4": ciscoModemMgmtMIBComplianceRev4,
       "ciscoModemMgmtMIBComplianceRev5": ciscoModemMgmtMIBComplianceRev5,
       "ciscoModemMgmtMIBComplianceRev6": ciscoModemMgmtMIBComplianceRev6,
       "ciscoModemMgmtMIBGroups": ciscoModemMgmtMIBGroups,
       "cmSystemInfoGroup": cmSystemInfoGroup,
       "cmGroupInfoGroup": cmGroupInfoGroup,
       "cmLineInfoGroup": cmLineInfoGroup,
       "cmManagedLineInfoGroup": cmManagedLineInfoGroup,
       "cmLineSpeedInfoGroup": cmLineSpeedInfoGroup,
       "cmSystemInfoGroupRev1": cmSystemInfoGroupRev1,
       "cmLineSpeedInfoGroupRev1": cmLineSpeedInfoGroupRev1,
       "cmManagedLineInfoGroupRev1": cmManagedLineInfoGroupRev1,
       "cmNotificationConfigGroup": cmNotificationConfigGroup,
       "cmNotificationGroup": cmNotificationGroup,
       "cmLineSpeedInfoGroupRev2": cmLineSpeedInfoGroupRev2,
       "cmManagedLineInfoGroupRev2": cmManagedLineInfoGroupRev2}
)
