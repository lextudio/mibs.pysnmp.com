# SNMP MIB module (AC-ANALOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-ANALOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:27 2024
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

(acBoardMibs,
 acGeneric,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acAnalog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcAnalogConfiguration_ObjectIdentity = ObjectIdentity
acAnalogConfiguration = _AcAnalogConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1)
)
_AcAnalogConfig_ObjectIdentity = ObjectIdentity
acAnalogConfig = _AcAnalogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1)
)
_AcAnalogMisc_ObjectIdentity = ObjectIdentity
acAnalogMisc = _AcAnalogMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 1)
)


class _AcAnalogMiscCurrentDisconnectDuration_Type(Unsigned32):
    """Custom type acAnalogMiscCurrentDisconnectDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1500),
    )


_AcAnalogMiscCurrentDisconnectDuration_Type.__name__ = "Unsigned32"
_AcAnalogMiscCurrentDisconnectDuration_Object = MibScalar
acAnalogMiscCurrentDisconnectDuration = _AcAnalogMiscCurrentDisconnectDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 1, 1),
    _AcAnalogMiscCurrentDisconnectDuration_Type()
)
acAnalogMiscCurrentDisconnectDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogMiscCurrentDisconnectDuration.setStatus("current")


class _AcAnalogMiscFlashHookPeriod_Type(Unsigned32):
    """Custom type acAnalogMiscFlashHookPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 3000),
    )


_AcAnalogMiscFlashHookPeriod_Type.__name__ = "Unsigned32"
_AcAnalogMiscFlashHookPeriod_Object = MibScalar
acAnalogMiscFlashHookPeriod = _AcAnalogMiscFlashHookPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 1, 2),
    _AcAnalogMiscFlashHookPeriod_Type()
)
acAnalogMiscFlashHookPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogMiscFlashHookPeriod.setStatus("current")


class _AcAnalogMiscGroundKeyDetection_Type(Integer32):
    """Custom type acAnalogMiscGroundKeyDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcAnalogMiscGroundKeyDetection_Type.__name__ = "Integer32"
_AcAnalogMiscGroundKeyDetection_Object = MibScalar
acAnalogMiscGroundKeyDetection = _AcAnalogMiscGroundKeyDetection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 1, 3),
    _AcAnalogMiscGroundKeyDetection_Type()
)
acAnalogMiscGroundKeyDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogMiscGroundKeyDetection.setStatus("current")
_AcAuxiliaryFiles_ObjectIdentity = ObjectIdentity
acAuxiliaryFiles = _AcAuxiliaryFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 2)
)


class _AcAuxiliaryFilesFxsCoefficients_Type(SnmpAdminString):
    """Custom type acAuxiliaryFilesFxsCoefficients based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcAuxiliaryFilesFxsCoefficients_Type.__name__ = "SnmpAdminString"
_AcAuxiliaryFilesFxsCoefficients_Object = MibScalar
acAuxiliaryFilesFxsCoefficients = _AcAuxiliaryFilesFxsCoefficients_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 2, 1),
    _AcAuxiliaryFilesFxsCoefficients_Type()
)
acAuxiliaryFilesFxsCoefficients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuxiliaryFilesFxsCoefficients.setStatus("current")


class _AcAuxiliaryFilesFxoCoefficients_Type(SnmpAdminString):
    """Custom type acAuxiliaryFilesFxoCoefficients based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcAuxiliaryFilesFxoCoefficients_Type.__name__ = "SnmpAdminString"
_AcAuxiliaryFilesFxoCoefficients_Object = MibScalar
acAuxiliaryFilesFxoCoefficients = _AcAuxiliaryFilesFxoCoefficients_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 1, 2, 2),
    _AcAuxiliaryFilesFxoCoefficients_Type()
)
acAuxiliaryFilesFxoCoefficients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAuxiliaryFilesFxoCoefficients.setStatus("current")
_AcAnalogFxoConfig_ObjectIdentity = ObjectIdentity
acAnalogFxoConfig = _AcAnalogFxoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2)
)
_AcAnalogFxo_ObjectIdentity = ObjectIdentity
acAnalogFxo = _AcAnalogFxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1)
)


class _AcAnalogFxoFarEndDisconnectType_Type(Unsigned32):
    """Custom type acAnalogFxoFarEndDisconnectType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcAnalogFxoFarEndDisconnectType_Type.__name__ = "Unsigned32"
_AcAnalogFxoFarEndDisconnectType_Object = MibScalar
acAnalogFxoFarEndDisconnectType = _AcAnalogFxoFarEndDisconnectType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 1),
    _AcAnalogFxoFarEndDisconnectType_Type()
)
acAnalogFxoFarEndDisconnectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxoFarEndDisconnectType.setStatus("current")


class _AcAnalogFxoCountryCoefficients_Type(Integer32):
    """Custom type acAnalogFxoCountryCoefficients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(66,
              70)
        )
    )
    namedValues = NamedValues(
        *(("europe", 66),
          ("unitedStates", 70))
    )


_AcAnalogFxoCountryCoefficients_Type.__name__ = "Integer32"
_AcAnalogFxoCountryCoefficients_Object = MibScalar
acAnalogFxoCountryCoefficients = _AcAnalogFxoCountryCoefficients_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 2),
    _AcAnalogFxoCountryCoefficients_Type()
)
acAnalogFxoCountryCoefficients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxoCountryCoefficients.setStatus("current")


class _AcAnalogFxoDCRemover_Type(Integer32):
    """Custom type acAnalogFxoDCRemover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcAnalogFxoDCRemover_Type.__name__ = "Integer32"
_AcAnalogFxoDCRemover_Object = MibScalar
acAnalogFxoDCRemover = _AcAnalogFxoDCRemover_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 3),
    _AcAnalogFxoDCRemover_Type()
)
acAnalogFxoDCRemover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxoDCRemover.setStatus("current")
_AcAnalogFxoFarEndDisconnectToneTable_Object = MibTable
acAnalogFxoFarEndDisconnectToneTable = _AcAnalogFxoFarEndDisconnectToneTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21)
)
if mibBuilder.loadTexts:
    acAnalogFxoFarEndDisconnectToneTable.setStatus("current")
_AcAnalogFxoFarEndDisconnectToneEntry_Object = MibTableRow
acAnalogFxoFarEndDisconnectToneEntry = _AcAnalogFxoFarEndDisconnectToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1)
)
acAnalogFxoFarEndDisconnectToneEntry.setIndexNames(
    (0, "AC-ANALOG-MIB", "acAnalogFxoFarEndDisconnectToneIndex"),
)
if mibBuilder.loadTexts:
    acAnalogFxoFarEndDisconnectToneEntry.setStatus("current")


class _AcAnalogFxoFarEndDisconnectToneRowStatus_Type(Unsigned32):
    """Custom type acAnalogFxoFarEndDisconnectToneRowStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AcAnalogFxoFarEndDisconnectToneRowStatus_Type.__name__ = "Unsigned32"
_AcAnalogFxoFarEndDisconnectToneRowStatus_Object = MibTableColumn
acAnalogFxoFarEndDisconnectToneRowStatus = _AcAnalogFxoFarEndDisconnectToneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 1),
    _AcAnalogFxoFarEndDisconnectToneRowStatus_Type()
)
acAnalogFxoFarEndDisconnectToneRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxoFarEndDisconnectToneRowStatus.setStatus("current")


class _AcAnalogFxoFarEndDisconnectToneAction_Type(Unsigned32):
    """Custom type acAnalogFxoFarEndDisconnectToneAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcAnalogFxoFarEndDisconnectToneAction_Type.__name__ = "Unsigned32"
_AcAnalogFxoFarEndDisconnectToneAction_Object = MibTableColumn
acAnalogFxoFarEndDisconnectToneAction = _AcAnalogFxoFarEndDisconnectToneAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 2),
    _AcAnalogFxoFarEndDisconnectToneAction_Type()
)
acAnalogFxoFarEndDisconnectToneAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxoFarEndDisconnectToneAction.setStatus("current")


class _AcAnalogFxoFarEndDisconnectToneActionResult_Type(Unsigned32):
    """Custom type acAnalogFxoFarEndDisconnectToneActionResult based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcAnalogFxoFarEndDisconnectToneActionResult_Type.__name__ = "Unsigned32"
_AcAnalogFxoFarEndDisconnectToneActionResult_Object = MibTableColumn
acAnalogFxoFarEndDisconnectToneActionResult = _AcAnalogFxoFarEndDisconnectToneActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 3),
    _AcAnalogFxoFarEndDisconnectToneActionResult_Type()
)
acAnalogFxoFarEndDisconnectToneActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoFarEndDisconnectToneActionResult.setStatus("current")


class _AcAnalogFxoFarEndDisconnectToneIndex_Type(Unsigned32):
    """Custom type acAnalogFxoFarEndDisconnectToneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcAnalogFxoFarEndDisconnectToneIndex_Type.__name__ = "Unsigned32"
_AcAnalogFxoFarEndDisconnectToneIndex_Object = MibTableColumn
acAnalogFxoFarEndDisconnectToneIndex = _AcAnalogFxoFarEndDisconnectToneIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 4),
    _AcAnalogFxoFarEndDisconnectToneIndex_Type()
)
acAnalogFxoFarEndDisconnectToneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoFarEndDisconnectToneIndex.setStatus("current")


class _AcAnalogFxoFarEndDisconnectToneType_Type(Integer32):
    """Custom type acAnalogFxoFarEndDisconnectToneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              298,
              299)
        )
    )
    namedValues = NamedValues(
        *(("acAlertingTone", 28),
          ("acBusyTone", 3),
          ("acCNGFaxTone", 40),
          ("acCallForwardTone", 25),
          ("acCallProgressCo1Tone", 10),
          ("acCallProgressCo2Tone", 11),
          ("acCallTransferDialTone", 24),
          ("acCallerWaitingTone", 39),
          ("acCarrierAnswerTone", 217),
          ("acCarrierChargingTone", 218),
          ("acCarrierDialTone", 216),
          ("acCo1Tone", 200),
          ("acCo2Tone", 201),
          ("acComfortTone", 18),
          ("acConfEnterTone", 33),
          ("acConfExitTone", 34),
          ("acConfLockTone", 35),
          ("acConfTimeLimitTone", 37),
          ("acConfUnlockTone", 36),
          ("acConfirmationTone", 8),
          ("acCongestionTone", 4),
          ("acCreditCardServiceTone", 26),
          ("acDialTone", 1),
          ("acDialTone2", 22),
          ("acFSKTrunkTestingTone", 206),
          ("acGeneralTrunkTestingTone1", 207),
          ("acGeneralTrunkTestingTone2", 208),
          ("acGeneralTrunkTestingTone3", 209),
          ("acLongDistanceIndicatorTone", 219),
          ("acMessageWaitingIndicator", 14),
          ("acNAKTone", 19),
          ("acNetworkCongestionTone", 29),
          ("acNewMilliwattTone", 13),
          ("acNullTone", 0),
          ("acOldMilliwattTone", 12),
          ("acOnHoldTone", 23),
          ("acPayphoneRecognitionTone", 38),
          ("acPlayRecordBeepTone", 202),
          ("acPrecConfNotifyType", 41),
          ("acPrecPreemptType", 43),
          ("acPrecRTType", 44),
          ("acPresConfNotifyType", 42),
          ("acR15reqOfANItone", 45),
          ("acReorderTone", 7),
          ("acRingingTone", 2),
          ("acSTUModemFirstTone", 298),
          ("acSTUModemSecondTone", 299),
          ("acSpecialConditionTone", 21),
          ("acSpecialInfoTone", 5),
          ("acSpecialInfoToneFirst", 210),
          ("acSpecialInfoToneSecond", 211),
          ("acSpecialInfoToneThird", 212),
          ("acSpecialRecallDialTone", 27),
          ("acStutterDialTone", 15),
          ("acStutterOffHookWarningTone", 16),
          ("acTT904ContinuityTone", 214),
          ("acTTMilliwattLossMeasureTone", 215),
          ("acTTYTone", 213),
          ("acTrunkTestingGuardTone", 205),
          ("acTrunkTestingTestProgressTone", 203),
          ("acTrunkTestingTestTone", 204),
          ("acVacantNumberTone", 20),
          ("acWaitingTone", 9),
          ("acWaitingTone1", 17),
          ("acWaitingTone2", 30),
          ("acWaitingTone3", 31),
          ("acWaitingTone4", 32),
          ("acWarningTone", 6))
    )


_AcAnalogFxoFarEndDisconnectToneType_Type.__name__ = "Integer32"
_AcAnalogFxoFarEndDisconnectToneType_Object = MibTableColumn
acAnalogFxoFarEndDisconnectToneType = _AcAnalogFxoFarEndDisconnectToneType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 2, 1, 21, 1, 5),
    _AcAnalogFxoFarEndDisconnectToneType_Type()
)
acAnalogFxoFarEndDisconnectToneType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxoFarEndDisconnectToneType.setStatus("current")
_AcAnalogFxsConfig_ObjectIdentity = ObjectIdentity
acAnalogFxsConfig = _AcAnalogFxsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3)
)
_AcAnalogFxs_ObjectIdentity = ObjectIdentity
acAnalogFxs = _AcAnalogFxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1)
)


class _AcAnalogFxsPolarityReversalType_Type(Integer32):
    """Custom type acAnalogFxsPolarityReversalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0))
    )


_AcAnalogFxsPolarityReversalType_Type.__name__ = "Integer32"
_AcAnalogFxsPolarityReversalType_Object = MibScalar
acAnalogFxsPolarityReversalType = _AcAnalogFxsPolarityReversalType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 1),
    _AcAnalogFxsPolarityReversalType_Type()
)
acAnalogFxsPolarityReversalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsPolarityReversalType.setStatus("current")


class _AcAnalogFxsMeteringType_Type(Integer32):
    """Custom type acAnalogFxsMeteringType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mt12kHz", 0),
          ("mt16kHz", 1),
          ("mtPolarityReversal", 2))
    )


_AcAnalogFxsMeteringType_Type.__name__ = "Integer32"
_AcAnalogFxsMeteringType_Object = MibScalar
acAnalogFxsMeteringType = _AcAnalogFxsMeteringType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 2),
    _AcAnalogFxsMeteringType_Type()
)
acAnalogFxsMeteringType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsMeteringType.setStatus("current")


class _AcAnalogFxsLifeLineType_Type(Integer32):
    """Custom type acAnalogFxsLifeLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acLifeLineType-Hardware-And-Link-And-Network-Detection", 2),
          ("acLifeLineType-Hardware-Only", 0),
          ("acLifeLineTypeHardware-And-Link-Detection", 1))
    )


_AcAnalogFxsLifeLineType_Type.__name__ = "Integer32"
_AcAnalogFxsLifeLineType_Object = MibScalar
acAnalogFxsLifeLineType = _AcAnalogFxsLifeLineType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 3),
    _AcAnalogFxsLifeLineType_Type()
)
acAnalogFxsLifeLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsLifeLineType.setStatus("current")


class _AcAnalogFxsMinFlashHookTime_Type(Unsigned32):
    """Custom type acAnalogFxsMinFlashHookTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 300),
    )


_AcAnalogFxsMinFlashHookTime_Type.__name__ = "Unsigned32"
_AcAnalogFxsMinFlashHookTime_Object = MibScalar
acAnalogFxsMinFlashHookTime = _AcAnalogFxsMinFlashHookTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 4),
    _AcAnalogFxsMinFlashHookTime_Type()
)
acAnalogFxsMinFlashHookTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsMinFlashHookTime.setStatus("current")


class _AcAnalogFxsCallerIDTimingMode_Type(Integer32):
    """Custom type acAnalogFxsCallerIDTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcAnalogFxsCallerIDTimingMode_Type.__name__ = "Integer32"
_AcAnalogFxsCallerIDTimingMode_Object = MibScalar
acAnalogFxsCallerIDTimingMode = _AcAnalogFxsCallerIDTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 5),
    _AcAnalogFxsCallerIDTimingMode_Type()
)
acAnalogFxsCallerIDTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsCallerIDTimingMode.setStatus("current")


class _AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Type(Integer32):
    """Custom type acAnalogFxsBellcoreCallerIDTypeOneSubStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bellcore-Before-Ring-RP-AS", 2),
          ("bellcore-Between-Rings", 0),
          ("bellcore-Not-Ring-Related", 1))
    )


_AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Type.__name__ = "Integer32"
_AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Object = MibScalar
acAnalogFxsBellcoreCallerIDTypeOneSubStandard = _AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 6),
    _AcAnalogFxsBellcoreCallerIDTypeOneSubStandard_Type()
)
acAnalogFxsBellcoreCallerIDTypeOneSubStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsBellcoreCallerIDTypeOneSubStandard.setStatus("current")


class _AcAnalogFxsETSICallerIDTypeOneSubStandard_Type(Integer32):
    """Custom type acAnalogFxsETSICallerIDTypeOneSubStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eTSI-Before-Ring-DT-AS", 1),
          ("eTSI-Before-Ring-LR-DT-AS", 3),
          ("eTSI-Before-Ring-RP-AS", 2),
          ("eTSI-Between-Rings", 0),
          ("eTSI-Not-Ring-Related-DT-AS", 4),
          ("eTSI-Not-Ring-Related-LR-DT-AS", 6),
          ("eTSI-Not-Ring-Related-RP-AS", 5))
    )


_AcAnalogFxsETSICallerIDTypeOneSubStandard_Type.__name__ = "Integer32"
_AcAnalogFxsETSICallerIDTypeOneSubStandard_Object = MibScalar
acAnalogFxsETSICallerIDTypeOneSubStandard = _AcAnalogFxsETSICallerIDTypeOneSubStandard_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 7),
    _AcAnalogFxsETSICallerIDTypeOneSubStandard_Type()
)
acAnalogFxsETSICallerIDTypeOneSubStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsETSICallerIDTypeOneSubStandard.setStatus("current")


class _AcAnalogFxsETSIVMWITypeOneStandard_Type(Integer32):
    """Custom type acAnalogFxsETSIVMWITypeOneStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eTSI-VMWI-Before-Ring-DT-AS", 1),
          ("eTSI-VMWI-Before-Ring-LR-DT-AS", 3),
          ("eTSI-VMWI-Before-Ring-RP-AS", 2),
          ("eTSI-VMWI-Between-Rings", 0),
          ("eTSI-VMWI-Not-Ring-Related-DT-AS", 4),
          ("eTSI-VMWI-Not-Ring-Related-LR-DT-AS", 6),
          ("eTSI-VMWI-Not-Ring-Related-RP-AS", 5))
    )


_AcAnalogFxsETSIVMWITypeOneStandard_Type.__name__ = "Integer32"
_AcAnalogFxsETSIVMWITypeOneStandard_Object = MibScalar
acAnalogFxsETSIVMWITypeOneStandard = _AcAnalogFxsETSIVMWITypeOneStandard_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 8),
    _AcAnalogFxsETSIVMWITypeOneStandard_Type()
)
acAnalogFxsETSIVMWITypeOneStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsETSIVMWITypeOneStandard.setStatus("current")


class _AcAnalogFxsBellcoreVMWITypeOneStandard_Type(Integer32):
    """Custom type acAnalogFxsBellcoreVMWITypeOneStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bellcore-VMWI-Between-Rings", 0),
          ("bellcore-VMWI-Not-Ring-Related", 1))
    )


_AcAnalogFxsBellcoreVMWITypeOneStandard_Type.__name__ = "Integer32"
_AcAnalogFxsBellcoreVMWITypeOneStandard_Object = MibScalar
acAnalogFxsBellcoreVMWITypeOneStandard = _AcAnalogFxsBellcoreVMWITypeOneStandard_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 9),
    _AcAnalogFxsBellcoreVMWITypeOneStandard_Type()
)
acAnalogFxsBellcoreVMWITypeOneStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsBellcoreVMWITypeOneStandard.setStatus("current")
_AcAnalogFxsDisableAutoCalibration_Type = Unsigned32
_AcAnalogFxsDisableAutoCalibration_Object = MibScalar
acAnalogFxsDisableAutoCalibration = _AcAnalogFxsDisableAutoCalibration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 10),
    _AcAnalogFxsDisableAutoCalibration_Type()
)
acAnalogFxsDisableAutoCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsDisableAutoCalibration.setStatus("current")


class _AcAnalogFxsExternalLifeLinePorts_Type(Unsigned32):
    """Custom type acAnalogFxsExternalLifeLinePorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AcAnalogFxsExternalLifeLinePorts_Type.__name__ = "Unsigned32"
_AcAnalogFxsExternalLifeLinePorts_Object = MibScalar
acAnalogFxsExternalLifeLinePorts = _AcAnalogFxsExternalLifeLinePorts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 11),
    _AcAnalogFxsExternalLifeLinePorts_Type()
)
acAnalogFxsExternalLifeLinePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsExternalLifeLinePorts.setStatus("current")


class _AcAnalogFxsCountryCoefficients_Type(Integer32):
    """Custom type acAnalogFxsCountryCoefficients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(66,
              70)
        )
    )
    namedValues = NamedValues(
        *(("europe", 66),
          ("unitedStates", 70))
    )


_AcAnalogFxsCountryCoefficients_Type.__name__ = "Integer32"
_AcAnalogFxsCountryCoefficients_Object = MibScalar
acAnalogFxsCountryCoefficients = _AcAnalogFxsCountryCoefficients_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 12),
    _AcAnalogFxsCountryCoefficients_Type()
)
acAnalogFxsCountryCoefficients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsCountryCoefficients.setStatus("current")


class _AcAnalogFxsTTXVoltageLevel_Type(Integer32):
    """Custom type acAnalogFxsTTXVoltageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", -1),
          ("ttxVoltageLevel05", 1),
          ("ttxVoltageLevel0V", 0),
          ("ttxVoltageLevel1V", 2))
    )


_AcAnalogFxsTTXVoltageLevel_Type.__name__ = "Integer32"
_AcAnalogFxsTTXVoltageLevel_Object = MibScalar
acAnalogFxsTTXVoltageLevel = _AcAnalogFxsTTXVoltageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 1, 3, 1, 13),
    _AcAnalogFxsTTXVoltageLevel_Type()
)
acAnalogFxsTTXVoltageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsTTXVoltageLevel.setStatus("current")
_AcAnalogStatus_ObjectIdentity = ObjectIdentity
acAnalogStatus = _AcAnalogStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2)
)
_AcAnalogStatusMisc_ObjectIdentity = ObjectIdentity
acAnalogStatusMisc = _AcAnalogStatusMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 1)
)


class _AcAnalogStatusMiscFxsOrFxo_Type(Integer32):
    """Custom type acAnalogStatusMiscFxsOrFxo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fXO", 0),
          ("fXS", 1))
    )


_AcAnalogStatusMiscFxsOrFxo_Type.__name__ = "Integer32"
_AcAnalogStatusMiscFxsOrFxo_Object = MibScalar
acAnalogStatusMiscFxsOrFxo = _AcAnalogStatusMiscFxsOrFxo_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 1, 1),
    _AcAnalogStatusMiscFxsOrFxo_Type()
)
acAnalogStatusMiscFxsOrFxo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogStatusMiscFxsOrFxo.setStatus("current")


class _AcAnalogStatusMiscBoardTemperature_Type(Unsigned32):
    """Custom type acAnalogStatusMiscBoardTemperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcAnalogStatusMiscBoardTemperature_Type.__name__ = "Unsigned32"
_AcAnalogStatusMiscBoardTemperature_Object = MibScalar
acAnalogStatusMiscBoardTemperature = _AcAnalogStatusMiscBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 1, 2),
    _AcAnalogStatusMiscBoardTemperature_Type()
)
acAnalogStatusMiscBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogStatusMiscBoardTemperature.setStatus("current")


class _AcAnalogStatusMiscAnalogChannelsCount_Type(Unsigned32):
    """Custom type acAnalogStatusMiscAnalogChannelsCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AcAnalogStatusMiscAnalogChannelsCount_Type.__name__ = "Unsigned32"
_AcAnalogStatusMiscAnalogChannelsCount_Object = MibScalar
acAnalogStatusMiscAnalogChannelsCount = _AcAnalogStatusMiscAnalogChannelsCount_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 1, 3),
    _AcAnalogStatusMiscAnalogChannelsCount_Type()
)
acAnalogStatusMiscAnalogChannelsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogStatusMiscAnalogChannelsCount.setStatus("current")
_AcAnalogFxsFxo_ObjectIdentity = ObjectIdentity
acAnalogFxsFxo = _AcAnalogFxsFxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20)
)
_AcAnalogFxsFxoTable_Object = MibTable
acAnalogFxsFxoTable = _AcAnalogFxsFxoTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1)
)
if mibBuilder.loadTexts:
    acAnalogFxsFxoTable.setStatus("current")
_AcAnalogFxsFxoEntry_Object = MibTableRow
acAnalogFxsFxoEntry = _AcAnalogFxsFxoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1)
)
acAnalogFxsFxoEntry.setIndexNames(
    (0, "AC-ANALOG-MIB", "acAnalogFxsFxoIndex"),
)
if mibBuilder.loadTexts:
    acAnalogFxsFxoEntry.setStatus("current")


class _AcAnalogFxsFxoIndex_Type(Unsigned32):
    """Custom type acAnalogFxsFxoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AcAnalogFxsFxoIndex_Type.__name__ = "Unsigned32"
_AcAnalogFxsFxoIndex_Object = MibTableColumn
acAnalogFxsFxoIndex = _AcAnalogFxsFxoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1, 1),
    _AcAnalogFxsFxoIndex_Type()
)
acAnalogFxsFxoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acAnalogFxsFxoIndex.setStatus("current")


class _AcAnalogFxsFxoType_Type(Integer32):
    """Custom type acAnalogFxsFxoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fXO", 0),
          ("fXS", 1))
    )


_AcAnalogFxsFxoType_Type.__name__ = "Integer32"
_AcAnalogFxsFxoType_Object = MibTableColumn
acAnalogFxsFxoType = _AcAnalogFxsFxoType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1, 2),
    _AcAnalogFxsFxoType_Type()
)
acAnalogFxsFxoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsFxoType.setStatus("current")


class _AcAnalogFxsFxoChipRevNum_Type(Unsigned32):
    """Custom type acAnalogFxsFxoChipRevNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcAnalogFxsFxoChipRevNum_Type.__name__ = "Unsigned32"
_AcAnalogFxsFxoChipRevNum_Object = MibTableColumn
acAnalogFxsFxoChipRevNum = _AcAnalogFxsFxoChipRevNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1, 3),
    _AcAnalogFxsFxoChipRevNum_Type()
)
acAnalogFxsFxoChipRevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsFxoChipRevNum.setStatus("current")


class _AcAnalogFxsFxoHookState_Type(Integer32):
    """Custom type acAnalogFxsFxoHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offHookState", 2),
          ("onHookState", 1))
    )


_AcAnalogFxsFxoHookState_Type.__name__ = "Integer32"
_AcAnalogFxsFxoHookState_Object = MibTableColumn
acAnalogFxsFxoHookState = _AcAnalogFxsFxoHookState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 20, 1, 1, 4),
    _AcAnalogFxsFxoHookState_Type()
)
acAnalogFxsFxoHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsFxoHookState.setStatus("current")
_AcAnalogLegs_ObjectIdentity = ObjectIdentity
acAnalogLegs = _AcAnalogLegs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21)
)
_AcAnalogLegsTable_Object = MibTable
acAnalogLegsTable = _AcAnalogLegsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1)
)
if mibBuilder.loadTexts:
    acAnalogLegsTable.setStatus("current")
_AcAnalogLegsEntry_Object = MibTableRow
acAnalogLegsEntry = _AcAnalogLegsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1)
)
acAnalogLegsEntry.setIndexNames(
    (0, "AC-ANALOG-MIB", "acAnalogLegsLegIndex"),
)
if mibBuilder.loadTexts:
    acAnalogLegsEntry.setStatus("current")


class _AcAnalogLegsLegIndex_Type(Unsigned32):
    """Custom type acAnalogLegsLegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AcAnalogLegsLegIndex_Type.__name__ = "Unsigned32"
_AcAnalogLegsLegIndex_Object = MibTableColumn
acAnalogLegsLegIndex = _AcAnalogLegsLegIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 1),
    _AcAnalogLegsLegIndex_Type()
)
acAnalogLegsLegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acAnalogLegsLegIndex.setStatus("current")


class _AcAnalogLegsCallIndex_Type(Unsigned32):
    """Custom type acAnalogLegsCallIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AcAnalogLegsCallIndex_Type.__name__ = "Unsigned32"
_AcAnalogLegsCallIndex_Object = MibTableColumn
acAnalogLegsCallIndex = _AcAnalogLegsCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 2),
    _AcAnalogLegsCallIndex_Type()
)
acAnalogLegsCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogLegsCallIndex.setStatus("current")


class _AcAnalogLegsAnalogType_Type(Integer32):
    """Custom type acAnalogLegsAnalogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fxo", 2),
          ("fxs", 1))
    )


_AcAnalogLegsAnalogType_Type.__name__ = "Integer32"
_AcAnalogLegsAnalogType_Object = MibTableColumn
acAnalogLegsAnalogType = _AcAnalogLegsAnalogType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 3),
    _AcAnalogLegsAnalogType_Type()
)
acAnalogLegsAnalogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogLegsAnalogType.setStatus("current")


class _AcAnalogLegsEchoCanceller_Type(Integer32):
    """Custom type acAnalogLegsEchoCanceller based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcAnalogLegsEchoCanceller_Type.__name__ = "Integer32"
_AcAnalogLegsEchoCanceller_Object = MibTableColumn
acAnalogLegsEchoCanceller = _AcAnalogLegsEchoCanceller_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 4),
    _AcAnalogLegsEchoCanceller_Type()
)
acAnalogLegsEchoCanceller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogLegsEchoCanceller.setStatus("current")


class _AcAnalogLegsHighPassFilter_Type(Integer32):
    """Custom type acAnalogLegsHighPassFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcAnalogLegsHighPassFilter_Type.__name__ = "Integer32"
_AcAnalogLegsHighPassFilter_Object = MibTableColumn
acAnalogLegsHighPassFilter = _AcAnalogLegsHighPassFilter_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 5),
    _AcAnalogLegsHighPassFilter_Type()
)
acAnalogLegsHighPassFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogLegsHighPassFilter.setStatus("current")


class _AcAnalogLegsDTMFDetection_Type(Integer32):
    """Custom type acAnalogLegsDTMFDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcAnalogLegsDTMFDetection_Type.__name__ = "Integer32"
_AcAnalogLegsDTMFDetection_Object = MibTableColumn
acAnalogLegsDTMFDetection = _AcAnalogLegsDTMFDetection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 6),
    _AcAnalogLegsDTMFDetection_Type()
)
acAnalogLegsDTMFDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogLegsDTMFDetection.setStatus("current")


class _AcAnalogLegsVoiceVolume_Type(Unsigned32):
    """Custom type acAnalogLegsVoiceVolume based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_AcAnalogLegsVoiceVolume_Type.__name__ = "Unsigned32"
_AcAnalogLegsVoiceVolume_Object = MibTableColumn
acAnalogLegsVoiceVolume = _AcAnalogLegsVoiceVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 7),
    _AcAnalogLegsVoiceVolume_Type()
)
acAnalogLegsVoiceVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogLegsVoiceVolume.setStatus("current")


class _AcAnalogLegsInputGain_Type(Unsigned32):
    """Custom type acAnalogLegsInputGain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_AcAnalogLegsInputGain_Type.__name__ = "Unsigned32"
_AcAnalogLegsInputGain_Object = MibTableColumn
acAnalogLegsInputGain = _AcAnalogLegsInputGain_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 8),
    _AcAnalogLegsInputGain_Type()
)
acAnalogLegsInputGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogLegsInputGain.setStatus("current")


class _AcAnalogLegsLegName_Type(SnmpAdminString):
    """Custom type acAnalogLegsLegName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcAnalogLegsLegName_Type.__name__ = "SnmpAdminString"
_AcAnalogLegsLegName_Object = MibTableColumn
acAnalogLegsLegName = _AcAnalogLegsLegName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 2, 21, 1, 1, 9),
    _AcAnalogLegsLegName_Type()
)
acAnalogLegsLegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogLegsLegName.setStatus("current")
_AcAnalogAction_ObjectIdentity = ObjectIdentity
acAnalogAction = _AcAnalogAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3)
)
_AcAnalogFxoAction_ObjectIdentity = ObjectIdentity
acAnalogFxoAction = _AcAnalogFxoAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1)
)
_AcAnalogFxoLineTestTable_Object = MibTable
acAnalogFxoLineTestTable = _AcAnalogFxoLineTestTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    acAnalogFxoLineTestTable.setStatus("current")
_AcAnalogFxoLineTestEntry_Object = MibTableRow
acAnalogFxoLineTestEntry = _AcAnalogFxoLineTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1)
)
acAnalogFxoLineTestEntry.setIndexNames(
    (0, "AC-ANALOG-MIB", "acAnalogFxoLineTestIndex"),
)
if mibBuilder.loadTexts:
    acAnalogFxoLineTestEntry.setStatus("current")


class _AcAnalogFxoLineTestIndex_Type(Unsigned32):
    """Custom type acAnalogFxoLineTestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AcAnalogFxoLineTestIndex_Type.__name__ = "Unsigned32"
_AcAnalogFxoLineTestIndex_Object = MibTableColumn
acAnalogFxoLineTestIndex = _AcAnalogFxoLineTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 1),
    _AcAnalogFxoLineTestIndex_Type()
)
acAnalogFxoLineTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestIndex.setStatus("current")


class _AcAnalogFxoLineTestActivate_Type(Integer32):
    """Custom type acAnalogFxoLineTestActivate based on Integer32"""
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
        *(("lineTestDone", 2),
          ("noTestActivated", 0),
          ("runLineTest", 1),
          ("testFailed", 3))
    )


_AcAnalogFxoLineTestActivate_Type.__name__ = "Integer32"
_AcAnalogFxoLineTestActivate_Object = MibTableColumn
acAnalogFxoLineTestActivate = _AcAnalogFxoLineTestActivate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 2),
    _AcAnalogFxoLineTestActivate_Type()
)
acAnalogFxoLineTestActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestActivate.setStatus("current")


class _AcAnalogFxoLineTestHookState_Type(Integer32):
    """Custom type acAnalogFxoLineTestHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offHookState", 2),
          ("onHookState", 1))
    )


_AcAnalogFxoLineTestHookState_Type.__name__ = "Integer32"
_AcAnalogFxoLineTestHookState_Object = MibTableColumn
acAnalogFxoLineTestHookState = _AcAnalogFxoLineTestHookState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 3),
    _AcAnalogFxoLineTestHookState_Type()
)
acAnalogFxoLineTestHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestHookState.setStatus("current")


class _AcAnalogFxoLineTestPolarityStatus_Type(Integer32):
    """Custom type acAnalogFxoLineTestPolarityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normalPolarity", 1),
          ("notAvailable", 3),
          ("reversePolarity", 2))
    )


_AcAnalogFxoLineTestPolarityStatus_Type.__name__ = "Integer32"
_AcAnalogFxoLineTestPolarityStatus_Object = MibTableColumn
acAnalogFxoLineTestPolarityStatus = _AcAnalogFxoLineTestPolarityStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 4),
    _AcAnalogFxoLineTestPolarityStatus_Type()
)
acAnalogFxoLineTestPolarityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestPolarityStatus.setStatus("current")


class _AcAnalogFxoLineTestLineConnectionStatus_Type(Integer32):
    """Custom type acAnalogFxoLineTestLineConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineConnected", 2),
          ("lineDisconnected", 1))
    )


_AcAnalogFxoLineTestLineConnectionStatus_Type.__name__ = "Integer32"
_AcAnalogFxoLineTestLineConnectionStatus_Object = MibTableColumn
acAnalogFxoLineTestLineConnectionStatus = _AcAnalogFxoLineTestLineConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 5),
    _AcAnalogFxoLineTestLineConnectionStatus_Type()
)
acAnalogFxoLineTestLineConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestLineConnectionStatus.setStatus("current")


class _AcAnalogFxoLineTestLineCurrent_Type(Integer32):
    """Custom type acAnalogFxoLineTestLineCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 24),
    )


_AcAnalogFxoLineTestLineCurrent_Type.__name__ = "Integer32"
_AcAnalogFxoLineTestLineCurrent_Object = MibTableColumn
acAnalogFxoLineTestLineCurrent = _AcAnalogFxoLineTestLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 6),
    _AcAnalogFxoLineTestLineCurrent_Type()
)
acAnalogFxoLineTestLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestLineCurrent.setStatus("current")


class _AcAnalogFxoLineTestLineVoltage_Type(Integer32):
    """Custom type acAnalogFxoLineTestLineVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_AcAnalogFxoLineTestLineVoltage_Type.__name__ = "Integer32"
_AcAnalogFxoLineTestLineVoltage_Object = MibTableColumn
acAnalogFxoLineTestLineVoltage = _AcAnalogFxoLineTestLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 7),
    _AcAnalogFxoLineTestLineVoltage_Type()
)
acAnalogFxoLineTestLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestLineVoltage.setStatus("current")


class _AcAnalogFxoLineTestRingState_Type(Integer32):
    """Custom type acAnalogFxoLineTestRingState based on Integer32"""
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


_AcAnalogFxoLineTestRingState_Type.__name__ = "Integer32"
_AcAnalogFxoLineTestRingState_Object = MibTableColumn
acAnalogFxoLineTestRingState = _AcAnalogFxoLineTestRingState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 8),
    _AcAnalogFxoLineTestRingState_Type()
)
acAnalogFxoLineTestRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestRingState.setStatus("current")


class _AcAnalogFxoLineTestLinePolarity_Type(Integer32):
    """Custom type acAnalogFxoLineTestLinePolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1))
    )


_AcAnalogFxoLineTestLinePolarity_Type.__name__ = "Integer32"
_AcAnalogFxoLineTestLinePolarity_Object = MibTableColumn
acAnalogFxoLineTestLinePolarity = _AcAnalogFxoLineTestLinePolarity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 9),
    _AcAnalogFxoLineTestLinePolarity_Type()
)
acAnalogFxoLineTestLinePolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestLinePolarity.setStatus("current")


class _AcAnalogFxoLineTestMwiState_Type(Integer32):
    """Custom type acAnalogFxoLineTestMwiState based on Integer32"""
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


_AcAnalogFxoLineTestMwiState_Type.__name__ = "Integer32"
_AcAnalogFxoLineTestMwiState_Object = MibTableColumn
acAnalogFxoLineTestMwiState = _AcAnalogFxoLineTestMwiState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 10),
    _AcAnalogFxoLineTestMwiState_Type()
)
acAnalogFxoLineTestMwiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestMwiState.setStatus("current")


class _AcAnalogFxoLineTestLastCurrentDisconnectDuration_Type(Unsigned32):
    """Custom type acAnalogFxoLineTestLastCurrentDisconnectDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcAnalogFxoLineTestLastCurrentDisconnectDuration_Type.__name__ = "Unsigned32"
_AcAnalogFxoLineTestLastCurrentDisconnectDuration_Object = MibTableColumn
acAnalogFxoLineTestLastCurrentDisconnectDuration = _AcAnalogFxoLineTestLastCurrentDisconnectDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 1, 1, 1, 11),
    _AcAnalogFxoLineTestLastCurrentDisconnectDuration_Type()
)
acAnalogFxoLineTestLastCurrentDisconnectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxoLineTestLastCurrentDisconnectDuration.setStatus("current")
_AcAnalogFxsAction_ObjectIdentity = ObjectIdentity
acAnalogFxsAction = _AcAnalogFxsAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2)
)
_AcAnalogFxsLineTestTable_Object = MibTable
acAnalogFxsLineTestTable = _AcAnalogFxsLineTestTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    acAnalogFxsLineTestTable.setStatus("current")
_AcAnalogFxsLineTestEntry_Object = MibTableRow
acAnalogFxsLineTestEntry = _AcAnalogFxsLineTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1)
)
acAnalogFxsLineTestEntry.setIndexNames(
    (0, "AC-ANALOG-MIB", "acAnalogFxsLineTestIndex"),
)
if mibBuilder.loadTexts:
    acAnalogFxsLineTestEntry.setStatus("current")


class _AcAnalogFxsLineTestIndex_Type(Unsigned32):
    """Custom type acAnalogFxsLineTestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AcAnalogFxsLineTestIndex_Type.__name__ = "Unsigned32"
_AcAnalogFxsLineTestIndex_Object = MibTableColumn
acAnalogFxsLineTestIndex = _AcAnalogFxsLineTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 1),
    _AcAnalogFxsLineTestIndex_Type()
)
acAnalogFxsLineTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestIndex.setStatus("current")


class _AcAnalogFxsLineTestActivate_Type(Integer32):
    """Custom type acAnalogFxsLineTestActivate based on Integer32"""
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
        *(("lineTestDone", 2),
          ("noTestActivated", 0),
          ("runLineTest", 1),
          ("testFailed", 3))
    )


_AcAnalogFxsLineTestActivate_Type.__name__ = "Integer32"
_AcAnalogFxsLineTestActivate_Object = MibTableColumn
acAnalogFxsLineTestActivate = _AcAnalogFxsLineTestActivate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 2),
    _AcAnalogFxsLineTestActivate_Type()
)
acAnalogFxsLineTestActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestActivate.setStatus("current")


class _AcAnalogFxsLineTestHookState_Type(Integer32):
    """Custom type acAnalogFxsLineTestHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offHookState", 2),
          ("onHookState", 1))
    )


_AcAnalogFxsLineTestHookState_Type.__name__ = "Integer32"
_AcAnalogFxsLineTestHookState_Object = MibTableColumn
acAnalogFxsLineTestHookState = _AcAnalogFxsLineTestHookState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 3),
    _AcAnalogFxsLineTestHookState_Type()
)
acAnalogFxsLineTestHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestHookState.setStatus("current")


class _AcAnalogFxsLineTestRingState_Type(Integer32):
    """Custom type acAnalogFxsLineTestRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offRingState", 1),
          ("onRingState", 2))
    )


_AcAnalogFxsLineTestRingState_Type.__name__ = "Integer32"
_AcAnalogFxsLineTestRingState_Object = MibTableColumn
acAnalogFxsLineTestRingState = _AcAnalogFxsLineTestRingState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 4),
    _AcAnalogFxsLineTestRingState_Type()
)
acAnalogFxsLineTestRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestRingState.setStatus("current")


class _AcAnalogFxsLineTestPolarityStatus_Type(Integer32):
    """Custom type acAnalogFxsLineTestPolarityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalPolarity", 1),
          ("reversePolarity", 2))
    )


_AcAnalogFxsLineTestPolarityStatus_Type.__name__ = "Integer32"
_AcAnalogFxsLineTestPolarityStatus_Object = MibTableColumn
acAnalogFxsLineTestPolarityStatus = _AcAnalogFxsLineTestPolarityStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 5),
    _AcAnalogFxsLineTestPolarityStatus_Type()
)
acAnalogFxsLineTestPolarityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestPolarityStatus.setStatus("current")


class _AcAnalogFxsLineTestMessageWaitingIndication_Type(Integer32):
    """Custom type acAnalogFxsLineTestMessageWaitingIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWaitingMessage", 1),
          ("waitingMessage", 2))
    )


_AcAnalogFxsLineTestMessageWaitingIndication_Type.__name__ = "Integer32"
_AcAnalogFxsLineTestMessageWaitingIndication_Object = MibTableColumn
acAnalogFxsLineTestMessageWaitingIndication = _AcAnalogFxsLineTestMessageWaitingIndication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 6),
    _AcAnalogFxsLineTestMessageWaitingIndication_Type()
)
acAnalogFxsLineTestMessageWaitingIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestMessageWaitingIndication.setStatus("current")


class _AcAnalogFxsLineTestLineCurrentReading_Type(Unsigned32):
    """Custom type acAnalogFxsLineTestLineCurrentReading based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_AcAnalogFxsLineTestLineCurrentReading_Type.__name__ = "Unsigned32"
_AcAnalogFxsLineTestLineCurrentReading_Object = MibTableColumn
acAnalogFxsLineTestLineCurrentReading = _AcAnalogFxsLineTestLineCurrentReading_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 7),
    _AcAnalogFxsLineTestLineCurrentReading_Type()
)
acAnalogFxsLineTestLineCurrentReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestLineCurrentReading.setStatus("current")


class _AcAnalogFxsLineTestLineVoltageReading_Type(Integer32):
    """Custom type acAnalogFxsLineTestLineVoltageReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6000, 6000),
    )


_AcAnalogFxsLineTestLineVoltageReading_Type.__name__ = "Integer32"
_AcAnalogFxsLineTestLineVoltageReading_Object = MibTableColumn
acAnalogFxsLineTestLineVoltageReading = _AcAnalogFxsLineTestLineVoltageReading_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 8),
    _AcAnalogFxsLineTestLineVoltageReading_Type()
)
acAnalogFxsLineTestLineVoltageReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestLineVoltageReading.setStatus("current")


class _AcAnalogFxsLineTestAnalogVoltageReading_Type(Unsigned32):
    """Custom type acAnalogFxsLineTestAnalogVoltageReading based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 340),
    )


_AcAnalogFxsLineTestAnalogVoltageReading_Type.__name__ = "Unsigned32"
_AcAnalogFxsLineTestAnalogVoltageReading_Object = MibTableColumn
acAnalogFxsLineTestAnalogVoltageReading = _AcAnalogFxsLineTestAnalogVoltageReading_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 9),
    _AcAnalogFxsLineTestAnalogVoltageReading_Type()
)
acAnalogFxsLineTestAnalogVoltageReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestAnalogVoltageReading.setStatus("current")


class _AcAnalogFxsLineTestRingVoltageReading_Type(Integer32):
    """Custom type acAnalogFxsLineTestRingVoltageReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-13000, 13000),
    )


_AcAnalogFxsLineTestRingVoltageReading_Type.__name__ = "Integer32"
_AcAnalogFxsLineTestRingVoltageReading_Object = MibTableColumn
acAnalogFxsLineTestRingVoltageReading = _AcAnalogFxsLineTestRingVoltageReading_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 10),
    _AcAnalogFxsLineTestRingVoltageReading_Type()
)
acAnalogFxsLineTestRingVoltageReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestRingVoltageReading.setStatus("current")


class _AcAnalogFxsLineTestLongLineCurrentReading_Type(Unsigned32):
    """Custom type acAnalogFxsLineTestLongLineCurrentReading based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_AcAnalogFxsLineTestLongLineCurrentReading_Type.__name__ = "Unsigned32"
_AcAnalogFxsLineTestLongLineCurrentReading_Object = MibTableColumn
acAnalogFxsLineTestLongLineCurrentReading = _AcAnalogFxsLineTestLongLineCurrentReading_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 2, 1, 1, 11),
    _AcAnalogFxsLineTestLongLineCurrentReading_Type()
)
acAnalogFxsLineTestLongLineCurrentReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acAnalogFxsLineTestLongLineCurrentReading.setStatus("current")
_AcAnalogCommonAction_ObjectIdentity = ObjectIdentity
acAnalogCommonAction = _AcAnalogCommonAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3)
)
_AcAnalogCommonChannelTable_Object = MibTable
acAnalogCommonChannelTable = _AcAnalogCommonChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3, 1)
)
if mibBuilder.loadTexts:
    acAnalogCommonChannelTable.setStatus("current")
_AcAnalogCommonChannelEntry_Object = MibTableRow
acAnalogCommonChannelEntry = _AcAnalogCommonChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3, 1, 1)
)
acAnalogCommonChannelEntry.setIndexNames(
    (0, "AC-ANALOG-MIB", "acAnalogCommonChannelIndex"),
)
if mibBuilder.loadTexts:
    acAnalogCommonChannelEntry.setStatus("current")


class _AcAnalogCommonChannelIndex_Type(Unsigned32):
    """Custom type acAnalogCommonChannelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AcAnalogCommonChannelIndex_Type.__name__ = "Unsigned32"
_AcAnalogCommonChannelIndex_Object = MibTableColumn
acAnalogCommonChannelIndex = _AcAnalogCommonChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3, 1, 1, 1),
    _AcAnalogCommonChannelIndex_Type()
)
acAnalogCommonChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acAnalogCommonChannelIndex.setStatus("current")


class _AcAnalogCommonChannelAction_Type(Integer32):
    """Custom type acAnalogCommonChannelAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_AcAnalogCommonChannelAction_Type.__name__ = "Integer32"
_AcAnalogCommonChannelAction_Object = MibTableColumn
acAnalogCommonChannelAction = _AcAnalogCommonChannelAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 8, 3, 3, 1, 1, 2),
    _AcAnalogCommonChannelAction_Type()
)
acAnalogCommonChannelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acAnalogCommonChannelAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-ANALOG-MIB",
    **{"acAnalog": acAnalog,
       "acAnalogConfiguration": acAnalogConfiguration,
       "acAnalogConfig": acAnalogConfig,
       "acAnalogMisc": acAnalogMisc,
       "acAnalogMiscCurrentDisconnectDuration": acAnalogMiscCurrentDisconnectDuration,
       "acAnalogMiscFlashHookPeriod": acAnalogMiscFlashHookPeriod,
       "acAnalogMiscGroundKeyDetection": acAnalogMiscGroundKeyDetection,
       "acAuxiliaryFiles": acAuxiliaryFiles,
       "acAuxiliaryFilesFxsCoefficients": acAuxiliaryFilesFxsCoefficients,
       "acAuxiliaryFilesFxoCoefficients": acAuxiliaryFilesFxoCoefficients,
       "acAnalogFxoConfig": acAnalogFxoConfig,
       "acAnalogFxo": acAnalogFxo,
       "acAnalogFxoFarEndDisconnectType": acAnalogFxoFarEndDisconnectType,
       "acAnalogFxoCountryCoefficients": acAnalogFxoCountryCoefficients,
       "acAnalogFxoDCRemover": acAnalogFxoDCRemover,
       "acAnalogFxoFarEndDisconnectToneTable": acAnalogFxoFarEndDisconnectToneTable,
       "acAnalogFxoFarEndDisconnectToneEntry": acAnalogFxoFarEndDisconnectToneEntry,
       "acAnalogFxoFarEndDisconnectToneRowStatus": acAnalogFxoFarEndDisconnectToneRowStatus,
       "acAnalogFxoFarEndDisconnectToneAction": acAnalogFxoFarEndDisconnectToneAction,
       "acAnalogFxoFarEndDisconnectToneActionResult": acAnalogFxoFarEndDisconnectToneActionResult,
       "acAnalogFxoFarEndDisconnectToneIndex": acAnalogFxoFarEndDisconnectToneIndex,
       "acAnalogFxoFarEndDisconnectToneType": acAnalogFxoFarEndDisconnectToneType,
       "acAnalogFxsConfig": acAnalogFxsConfig,
       "acAnalogFxs": acAnalogFxs,
       "acAnalogFxsPolarityReversalType": acAnalogFxsPolarityReversalType,
       "acAnalogFxsMeteringType": acAnalogFxsMeteringType,
       "acAnalogFxsLifeLineType": acAnalogFxsLifeLineType,
       "acAnalogFxsMinFlashHookTime": acAnalogFxsMinFlashHookTime,
       "acAnalogFxsCallerIDTimingMode": acAnalogFxsCallerIDTimingMode,
       "acAnalogFxsBellcoreCallerIDTypeOneSubStandard": acAnalogFxsBellcoreCallerIDTypeOneSubStandard,
       "acAnalogFxsETSICallerIDTypeOneSubStandard": acAnalogFxsETSICallerIDTypeOneSubStandard,
       "acAnalogFxsETSIVMWITypeOneStandard": acAnalogFxsETSIVMWITypeOneStandard,
       "acAnalogFxsBellcoreVMWITypeOneStandard": acAnalogFxsBellcoreVMWITypeOneStandard,
       "acAnalogFxsDisableAutoCalibration": acAnalogFxsDisableAutoCalibration,
       "acAnalogFxsExternalLifeLinePorts": acAnalogFxsExternalLifeLinePorts,
       "acAnalogFxsCountryCoefficients": acAnalogFxsCountryCoefficients,
       "acAnalogFxsTTXVoltageLevel": acAnalogFxsTTXVoltageLevel,
       "acAnalogStatus": acAnalogStatus,
       "acAnalogStatusMisc": acAnalogStatusMisc,
       "acAnalogStatusMiscFxsOrFxo": acAnalogStatusMiscFxsOrFxo,
       "acAnalogStatusMiscBoardTemperature": acAnalogStatusMiscBoardTemperature,
       "acAnalogStatusMiscAnalogChannelsCount": acAnalogStatusMiscAnalogChannelsCount,
       "acAnalogFxsFxo": acAnalogFxsFxo,
       "acAnalogFxsFxoTable": acAnalogFxsFxoTable,
       "acAnalogFxsFxoEntry": acAnalogFxsFxoEntry,
       "acAnalogFxsFxoIndex": acAnalogFxsFxoIndex,
       "acAnalogFxsFxoType": acAnalogFxsFxoType,
       "acAnalogFxsFxoChipRevNum": acAnalogFxsFxoChipRevNum,
       "acAnalogFxsFxoHookState": acAnalogFxsFxoHookState,
       "acAnalogLegs": acAnalogLegs,
       "acAnalogLegsTable": acAnalogLegsTable,
       "acAnalogLegsEntry": acAnalogLegsEntry,
       "acAnalogLegsLegIndex": acAnalogLegsLegIndex,
       "acAnalogLegsCallIndex": acAnalogLegsCallIndex,
       "acAnalogLegsAnalogType": acAnalogLegsAnalogType,
       "acAnalogLegsEchoCanceller": acAnalogLegsEchoCanceller,
       "acAnalogLegsHighPassFilter": acAnalogLegsHighPassFilter,
       "acAnalogLegsDTMFDetection": acAnalogLegsDTMFDetection,
       "acAnalogLegsVoiceVolume": acAnalogLegsVoiceVolume,
       "acAnalogLegsInputGain": acAnalogLegsInputGain,
       "acAnalogLegsLegName": acAnalogLegsLegName,
       "acAnalogAction": acAnalogAction,
       "acAnalogFxoAction": acAnalogFxoAction,
       "acAnalogFxoLineTestTable": acAnalogFxoLineTestTable,
       "acAnalogFxoLineTestEntry": acAnalogFxoLineTestEntry,
       "acAnalogFxoLineTestIndex": acAnalogFxoLineTestIndex,
       "acAnalogFxoLineTestActivate": acAnalogFxoLineTestActivate,
       "acAnalogFxoLineTestHookState": acAnalogFxoLineTestHookState,
       "acAnalogFxoLineTestPolarityStatus": acAnalogFxoLineTestPolarityStatus,
       "acAnalogFxoLineTestLineConnectionStatus": acAnalogFxoLineTestLineConnectionStatus,
       "acAnalogFxoLineTestLineCurrent": acAnalogFxoLineTestLineCurrent,
       "acAnalogFxoLineTestLineVoltage": acAnalogFxoLineTestLineVoltage,
       "acAnalogFxoLineTestRingState": acAnalogFxoLineTestRingState,
       "acAnalogFxoLineTestLinePolarity": acAnalogFxoLineTestLinePolarity,
       "acAnalogFxoLineTestMwiState": acAnalogFxoLineTestMwiState,
       "acAnalogFxoLineTestLastCurrentDisconnectDuration": acAnalogFxoLineTestLastCurrentDisconnectDuration,
       "acAnalogFxsAction": acAnalogFxsAction,
       "acAnalogFxsLineTestTable": acAnalogFxsLineTestTable,
       "acAnalogFxsLineTestEntry": acAnalogFxsLineTestEntry,
       "acAnalogFxsLineTestIndex": acAnalogFxsLineTestIndex,
       "acAnalogFxsLineTestActivate": acAnalogFxsLineTestActivate,
       "acAnalogFxsLineTestHookState": acAnalogFxsLineTestHookState,
       "acAnalogFxsLineTestRingState": acAnalogFxsLineTestRingState,
       "acAnalogFxsLineTestPolarityStatus": acAnalogFxsLineTestPolarityStatus,
       "acAnalogFxsLineTestMessageWaitingIndication": acAnalogFxsLineTestMessageWaitingIndication,
       "acAnalogFxsLineTestLineCurrentReading": acAnalogFxsLineTestLineCurrentReading,
       "acAnalogFxsLineTestLineVoltageReading": acAnalogFxsLineTestLineVoltageReading,
       "acAnalogFxsLineTestAnalogVoltageReading": acAnalogFxsLineTestAnalogVoltageReading,
       "acAnalogFxsLineTestRingVoltageReading": acAnalogFxsLineTestRingVoltageReading,
       "acAnalogFxsLineTestLongLineCurrentReading": acAnalogFxsLineTestLongLineCurrentReading,
       "acAnalogCommonAction": acAnalogCommonAction,
       "acAnalogCommonChannelTable": acAnalogCommonChannelTable,
       "acAnalogCommonChannelEntry": acAnalogCommonChannelEntry,
       "acAnalogCommonChannelIndex": acAnalogCommonChannelIndex,
       "acAnalogCommonChannelAction": acAnalogCommonChannelAction}
)
