# SNMP MIB module (DEVTRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVTRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:13 2024
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

(device,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "device")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aniDevTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniDevTraps_ObjectIdentity = ObjectIdentity
aniDevTraps = _AniDevTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0)
)
_AniDevTrapControl_ObjectIdentity = ObjectIdentity
aniDevTrapControl = _AniDevTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 1)
)


class _AniDevControlTrapGeneration_Type(Integer32):
    """Custom type aniDevControlTrapGeneration based on Integer32"""
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


_AniDevControlTrapGeneration_Type.__name__ = "Integer32"
_AniDevControlTrapGeneration_Object = MibScalar
aniDevControlTrapGeneration = _AniDevControlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 1, 1),
    _AniDevControlTrapGeneration_Type()
)
aniDevControlTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevControlTrapGeneration.setStatus("current")

# Managed Objects groups


# Notification objects

aniDevTrapSuSyncAcquired = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 1)
)
if mibBuilder.loadTexts:
    aniDevTrapSuSyncAcquired.setStatus(
        "current"
    )

aniDevTrapBsuSuUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 2)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuSuUp.setStatus(
        "current"
    )

aniDevTrapBsuSuDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 3)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuSuDown.setStatus(
        "current"
    )

aniDevTrapSuBsuUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 4)
)
if mibBuilder.loadTexts:
    aniDevTrapSuBsuUp.setStatus(
        "current"
    )

aniDevTrapSuBsuDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 5)
)
if mibBuilder.loadTexts:
    aniDevTrapSuBsuDown.setStatus(
        "current"
    )

aniDevTrapDhcpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 6)
)
if mibBuilder.loadTexts:
    aniDevTrapDhcpFailure.setStatus(
        "current"
    )

aniDevTrapConfigDownloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 7)
)
if mibBuilder.loadTexts:
    aniDevTrapConfigDownloadFailure.setStatus(
        "current"
    )

aniDevTrapRamTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 8)
)
if mibBuilder.loadTexts:
    aniDevTrapRamTooLow.setStatus(
        "current"
    )

aniDevTrapRamNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 9)
)
if mibBuilder.loadTexts:
    aniDevTrapRamNormal.setStatus(
        "current"
    )

aniDevTrapModemPllNotLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 10)
)
if mibBuilder.loadTexts:
    aniDevTrapModemPllNotLocked.setStatus(
        "current"
    )

aniDevTrapModemPllNotLockedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 11)
)
if mibBuilder.loadTexts:
    aniDevTrapModemPllNotLockedClear.setStatus(
        "current"
    )

aniDevTrapRadioVoltReg = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 12)
)
if mibBuilder.loadTexts:
    aniDevTrapRadioVoltReg.setStatus(
        "current"
    )

aniDevTrapRadioVoltRegClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 13)
)
if mibBuilder.loadTexts:
    aniDevTrapRadioVoltRegClear.setStatus(
        "current"
    )

aniDevTrapRadioSynthNotLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 14)
)
if mibBuilder.loadTexts:
    aniDevTrapRadioSynthNotLocked.setStatus(
        "current"
    )

aniDevTrapRadioSynthNotLockedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 15)
)
if mibBuilder.loadTexts:
    aniDevTrapRadioSynthNotLockedClear.setStatus(
        "current"
    )

aniDevTrapBsuFanStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 16)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuFanStatus.setStatus(
        "current"
    )

aniDevTrapBsuFanStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 17)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuFanStatusClear.setStatus(
        "current"
    )

aniDevTrapBsuDc12vStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 18)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuDc12vStatus.setStatus(
        "current"
    )

aniDevTrapBsuDc12vStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 19)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuDc12vStatusClear.setStatus(
        "current"
    )

aniDevTrapMssPllNotLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 20)
)
if mibBuilder.loadTexts:
    aniDevTrapMssPllNotLocked.setStatus(
        "current"
    )

aniDevTrapMssPllNotLockedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 21)
)
if mibBuilder.loadTexts:
    aniDevTrapMssPllNotLockedClear.setStatus(
        "current"
    )

aniDevTrapBsuTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 22)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuTempTooLow.setStatus(
        "current"
    )

aniDevTrapBsuTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 23)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuTempTooHigh.setStatus(
        "current"
    )

aniDevTrapBsuTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 24)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuTempNormal.setStatus(
        "current"
    )

aniDevTrapFlashSpaceTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 25)
)
if mibBuilder.loadTexts:
    aniDevTrapFlashSpaceTooLow.setStatus(
        "current"
    )

aniDevTrapFlashSpaceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 26)
)
if mibBuilder.loadTexts:
    aniDevTrapFlashSpaceNormal.setStatus(
        "current"
    )

aniDevTrapNvramCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 27)
)
if mibBuilder.loadTexts:
    aniDevTrapNvramCorrupted.setStatus(
        "current"
    )

aniDevTrapNvramCorruptionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 28)
)
if mibBuilder.loadTexts:
    aniDevTrapNvramCorruptionClear.setStatus(
        "current"
    )

aniDevTrapFileSysCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 29)
)
if mibBuilder.loadTexts:
    aniDevTrapFileSysCorrupted.setStatus(
        "current"
    )

aniDevTrapFileSysCorruptionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 30)
)
if mibBuilder.loadTexts:
    aniDevTrapFileSysCorruptionClear.setStatus(
        "current"
    )

aniDevTrapSmtpConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 31)
)
if mibBuilder.loadTexts:
    aniDevTrapSmtpConnectFailure.setStatus(
        "current"
    )

aniDevTrapSmtpDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 32)
)
if mibBuilder.loadTexts:
    aniDevTrapSmtpDisabled.setStatus(
        "current"
    )

aniDevTrapSwWatchdogReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 33)
)
if mibBuilder.loadTexts:
    aniDevTrapSwWatchdogReset.setStatus(
        "current"
    )

aniDevTrapNatFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 34)
)
if mibBuilder.loadTexts:
    aniDevTrapNatFailure.setStatus(
        "current"
    )

aniDevTrapCurrentImageCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 35)
)
if mibBuilder.loadTexts:
    aniDevTrapCurrentImageCorrupted.setStatus(
        "current"
    )

aniDevTrapBsuSuFailedReg = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 36)
)
if mibBuilder.loadTexts:
    aniDevTrapBsuSuFailedReg.setStatus(
        "current"
    )

aniDevTrapDefaultConfigFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 37)
)
if mibBuilder.loadTexts:
    aniDevTrapDefaultConfigFileNotFound.setStatus(
        "current"
    )

aniDevTrapCurrentBsuState = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 38)
)
if mibBuilder.loadTexts:
    aniDevTrapCurrentBsuState.setStatus(
        "current"
    )

aniDevTrapCurrentSuState = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 39)
)
if mibBuilder.loadTexts:
    aniDevTrapCurrentSuState.setStatus(
        "current"
    )

aniDevTrapMemBufferTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 40)
)
if mibBuilder.loadTexts:
    aniDevTrapMemBufferTooLow.setStatus(
        "current"
    )

aniDevTrapMemBufferNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 41)
)
if mibBuilder.loadTexts:
    aniDevTrapMemBufferNormal.setStatus(
        "current"
    )

aniDevTrapConfigFileVersionCheckFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 42)
)
if mibBuilder.loadTexts:
    aniDevTrapConfigFileVersionCheckFailure.setStatus(
        "current"
    )

aniDevTrapDefaultFileVersionCheckFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 43)
)
if mibBuilder.loadTexts:
    aniDevTrapDefaultFileVersionCheckFailure.setStatus(
        "current"
    )

aniDevTrapConfigFileUploadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 44)
)
if mibBuilder.loadTexts:
    aniDevTrapConfigFileUploadFailure.setStatus(
        "current"
    )

aniDevTrapConfigFileUploadChecksumFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 45)
)
if mibBuilder.loadTexts:
    aniDevTrapConfigFileUploadChecksumFailure.setStatus(
        "current"
    )

aniDevTrapRunningBaselineImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 46)
)
if mibBuilder.loadTexts:
    aniDevTrapRunningBaselineImage.setStatus(
        "current"
    )

aniDevTrapPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 48)
)
if mibBuilder.loadTexts:
    aniDevTrapPowerSupplyFailure.setStatus(
        "current"
    )

aniDevTrapPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 49)
)
if mibBuilder.loadTexts:
    aniDevTrapPowerSupplyNormal.setStatus(
        "current"
    )

aniDevTrapRealtimeClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 50)
)
if mibBuilder.loadTexts:
    aniDevTrapRealtimeClockFailure.setStatus(
        "current"
    )

aniDevTrapRealtimeClockNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 51)
)
if mibBuilder.loadTexts:
    aniDevTrapRealtimeClockNormal.setStatus(
        "current"
    )

aniDevTrapModelNumFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 53)
)
if mibBuilder.loadTexts:
    aniDevTrapModelNumFailure.setStatus(
        "current"
    )

aniDevTrapConfigParseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 55)
)
if mibBuilder.loadTexts:
    aniDevTrapConfigParseFailure.setStatus(
        "current"
    )

aniDevUpdateInventory = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 56)
)
if mibBuilder.loadTexts:
    aniDevUpdateInventory.setStatus(
        "current"
    )

aniDevTrapPppFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 57)
)
if mibBuilder.loadTexts:
    aniDevTrapPppFailure.setStatus(
        "current"
    )

aniDevTrapPppStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 58)
)
if mibBuilder.loadTexts:
    aniDevTrapPppStatus.setStatus(
        "current"
    )

aniDevTrapFrequencyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 59)
)
if mibBuilder.loadTexts:
    aniDevTrapFrequencyChange.setStatus(
        "current"
    )

aniDevTrapPPPoeSessionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 62)
)
if mibBuilder.loadTexts:
    aniDevTrapPPPoeSessionUp.setStatus(
        "current"
    )

aniDevTrapPPPoeOfferError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 63)
)
if mibBuilder.loadTexts:
    aniDevTrapPPPoeOfferError.setStatus(
        "current"
    )

aniDevTrapPPPoeSessionTerminate = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 64)
)
if mibBuilder.loadTexts:
    aniDevTrapPPPoeSessionTerminate.setStatus(
        "current"
    )

aniDevTrapEtherAutoNegotiate = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 65)
)
if mibBuilder.loadTexts:
    aniDevTrapEtherAutoNegotiate.setStatus(
        "current"
    )

aniDevTrapRadioInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 66)
)
if mibBuilder.loadTexts:
    aniDevTrapRadioInitError.setStatus(
        "current"
    )

aniDevTrapMaxPowerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 67)
)
if mibBuilder.loadTexts:
    aniDevTrapMaxPowerError.setStatus(
        "current"
    )

aniDevTrapMaxPowerErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 68)
)
if mibBuilder.loadTexts:
    aniDevTrapMaxPowerErrorClear.setStatus(
        "current"
    )

aniDevTrapAgcTableNotCalibrated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 69)
)
if mibBuilder.loadTexts:
    aniDevTrapAgcTableNotCalibrated.setStatus(
        "current"
    )

aniDevTrapFreqTableInvalidEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 70)
)
if mibBuilder.loadTexts:
    aniDevTrapFreqTableInvalidEntry.setStatus(
        "current"
    )

aniDevTrapHtmlUnzippedError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 71)
)
if mibBuilder.loadTexts:
    aniDevTrapHtmlUnzippedError.setStatus(
        "current"
    )

aniDevTrapBootLineBackupUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 72)
)
if mibBuilder.loadTexts:
    aniDevTrapBootLineBackupUpdated.setStatus(
        "current"
    )

aniDevTrapBootLineRestoredFromBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 73)
)
if mibBuilder.loadTexts:
    aniDevTrapBootLineRestoredFromBackup.setStatus(
        "current"
    )

aniDevTrapNvramBackupUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 74)
)
if mibBuilder.loadTexts:
    aniDevTrapNvramBackupUpdated.setStatus(
        "current"
    )

aniDevTrapNvramRestoredFromBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 4325, 2, 10, 0, 75)
)
if mibBuilder.loadTexts:
    aniDevTrapNvramRestoredFromBackup.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVTRAPS-MIB",
    **{"aniDevTrap": aniDevTrap,
       "aniDevTraps": aniDevTraps,
       "aniDevTrapSuSyncAcquired": aniDevTrapSuSyncAcquired,
       "aniDevTrapBsuSuUp": aniDevTrapBsuSuUp,
       "aniDevTrapBsuSuDown": aniDevTrapBsuSuDown,
       "aniDevTrapSuBsuUp": aniDevTrapSuBsuUp,
       "aniDevTrapSuBsuDown": aniDevTrapSuBsuDown,
       "aniDevTrapDhcpFailure": aniDevTrapDhcpFailure,
       "aniDevTrapConfigDownloadFailure": aniDevTrapConfigDownloadFailure,
       "aniDevTrapRamTooLow": aniDevTrapRamTooLow,
       "aniDevTrapRamNormal": aniDevTrapRamNormal,
       "aniDevTrapModemPllNotLocked": aniDevTrapModemPllNotLocked,
       "aniDevTrapModemPllNotLockedClear": aniDevTrapModemPllNotLockedClear,
       "aniDevTrapRadioVoltReg": aniDevTrapRadioVoltReg,
       "aniDevTrapRadioVoltRegClear": aniDevTrapRadioVoltRegClear,
       "aniDevTrapRadioSynthNotLocked": aniDevTrapRadioSynthNotLocked,
       "aniDevTrapRadioSynthNotLockedClear": aniDevTrapRadioSynthNotLockedClear,
       "aniDevTrapBsuFanStatus": aniDevTrapBsuFanStatus,
       "aniDevTrapBsuFanStatusClear": aniDevTrapBsuFanStatusClear,
       "aniDevTrapBsuDc12vStatus": aniDevTrapBsuDc12vStatus,
       "aniDevTrapBsuDc12vStatusClear": aniDevTrapBsuDc12vStatusClear,
       "aniDevTrapMssPllNotLocked": aniDevTrapMssPllNotLocked,
       "aniDevTrapMssPllNotLockedClear": aniDevTrapMssPllNotLockedClear,
       "aniDevTrapBsuTempTooLow": aniDevTrapBsuTempTooLow,
       "aniDevTrapBsuTempTooHigh": aniDevTrapBsuTempTooHigh,
       "aniDevTrapBsuTempNormal": aniDevTrapBsuTempNormal,
       "aniDevTrapFlashSpaceTooLow": aniDevTrapFlashSpaceTooLow,
       "aniDevTrapFlashSpaceNormal": aniDevTrapFlashSpaceNormal,
       "aniDevTrapNvramCorrupted": aniDevTrapNvramCorrupted,
       "aniDevTrapNvramCorruptionClear": aniDevTrapNvramCorruptionClear,
       "aniDevTrapFileSysCorrupted": aniDevTrapFileSysCorrupted,
       "aniDevTrapFileSysCorruptionClear": aniDevTrapFileSysCorruptionClear,
       "aniDevTrapSmtpConnectFailure": aniDevTrapSmtpConnectFailure,
       "aniDevTrapSmtpDisabled": aniDevTrapSmtpDisabled,
       "aniDevTrapSwWatchdogReset": aniDevTrapSwWatchdogReset,
       "aniDevTrapNatFailure": aniDevTrapNatFailure,
       "aniDevTrapCurrentImageCorrupted": aniDevTrapCurrentImageCorrupted,
       "aniDevTrapBsuSuFailedReg": aniDevTrapBsuSuFailedReg,
       "aniDevTrapDefaultConfigFileNotFound": aniDevTrapDefaultConfigFileNotFound,
       "aniDevTrapCurrentBsuState": aniDevTrapCurrentBsuState,
       "aniDevTrapCurrentSuState": aniDevTrapCurrentSuState,
       "aniDevTrapMemBufferTooLow": aniDevTrapMemBufferTooLow,
       "aniDevTrapMemBufferNormal": aniDevTrapMemBufferNormal,
       "aniDevTrapConfigFileVersionCheckFailure": aniDevTrapConfigFileVersionCheckFailure,
       "aniDevTrapDefaultFileVersionCheckFailure": aniDevTrapDefaultFileVersionCheckFailure,
       "aniDevTrapConfigFileUploadFailure": aniDevTrapConfigFileUploadFailure,
       "aniDevTrapConfigFileUploadChecksumFailure": aniDevTrapConfigFileUploadChecksumFailure,
       "aniDevTrapRunningBaselineImage": aniDevTrapRunningBaselineImage,
       "aniDevTrapPowerSupplyFailure": aniDevTrapPowerSupplyFailure,
       "aniDevTrapPowerSupplyNormal": aniDevTrapPowerSupplyNormal,
       "aniDevTrapRealtimeClockFailure": aniDevTrapRealtimeClockFailure,
       "aniDevTrapRealtimeClockNormal": aniDevTrapRealtimeClockNormal,
       "aniDevTrapModelNumFailure": aniDevTrapModelNumFailure,
       "aniDevTrapConfigParseFailure": aniDevTrapConfigParseFailure,
       "aniDevUpdateInventory": aniDevUpdateInventory,
       "aniDevTrapPppFailure": aniDevTrapPppFailure,
       "aniDevTrapPppStatus": aniDevTrapPppStatus,
       "aniDevTrapFrequencyChange": aniDevTrapFrequencyChange,
       "aniDevTrapPPPoeSessionUp": aniDevTrapPPPoeSessionUp,
       "aniDevTrapPPPoeOfferError": aniDevTrapPPPoeOfferError,
       "aniDevTrapPPPoeSessionTerminate": aniDevTrapPPPoeSessionTerminate,
       "aniDevTrapEtherAutoNegotiate": aniDevTrapEtherAutoNegotiate,
       "aniDevTrapRadioInitError": aniDevTrapRadioInitError,
       "aniDevTrapMaxPowerError": aniDevTrapMaxPowerError,
       "aniDevTrapMaxPowerErrorClear": aniDevTrapMaxPowerErrorClear,
       "aniDevTrapAgcTableNotCalibrated": aniDevTrapAgcTableNotCalibrated,
       "aniDevTrapFreqTableInvalidEntry": aniDevTrapFreqTableInvalidEntry,
       "aniDevTrapHtmlUnzippedError": aniDevTrapHtmlUnzippedError,
       "aniDevTrapBootLineBackupUpdated": aniDevTrapBootLineBackupUpdated,
       "aniDevTrapBootLineRestoredFromBackup": aniDevTrapBootLineRestoredFromBackup,
       "aniDevTrapNvramBackupUpdated": aniDevTrapNvramBackupUpdated,
       "aniDevTrapNvramRestoredFromBackup": aniDevTrapNvramRestoredFromBackup,
       "aniDevTrapControl": aniDevTrapControl,
       "aniDevControlTrapGeneration": aniDevControlTrapGeneration}
)
