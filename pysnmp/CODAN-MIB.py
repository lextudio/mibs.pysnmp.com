# SNMP MIB module (CODAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CODAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:05 2024
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

(codanMibs,) = mibBuilder.importSymbols(
    "CODAN-SMI",
    "codanMibs")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TestAndIncr,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval")


# MODULE-IDENTITY

minetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1)
)
minetMIB.setRevisions(
        ("1997-08-26 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WvAlarmsList(Bits, TextualConvention):
    status = "current"


class ComponentRevision(OctetString, TextualConvention):
    status = "current"
    displayHint = "Vxx.yy"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class FrontPanelPassword(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class FloatingPoint(OctetString, TextualConvention):
    status = "current"
    displayHint = "a.bcdE-n"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class WvLoopbacksList(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_WvConfiguration_ObjectIdentity = ObjectIdentity
wvConfiguration = _WvConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1)
)
_WvLinkSettings_ObjectIdentity = ObjectIdentity
wvLinkSettings = _WvLinkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1)
)


class _WvLinkId_Type(Integer32):
    """Custom type wvLinkId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_WvLinkId_Type.__name__ = "Integer32"
_WvLinkId_Object = MibScalar
wvLinkId = _WvLinkId_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 1),
    _WvLinkId_Type()
)
wvLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkId.setStatus("current")


class _WvLinkName_Type(DisplayString):
    """Custom type wvLinkName based on DisplayString"""
    defaultValue = OctetString("Codan")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WvLinkName_Type.__name__ = "DisplayString"
_WvLinkName_Object = MibScalar
wvLinkName = _WvLinkName_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 2),
    _WvLinkName_Type()
)
wvLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkName.setStatus("current")


class _WvLinkRouteDescription_Type(DisplayString):
    """Custom type wvLinkRouteDescription based on DisplayString"""
    defaultValue = OctetString("siteA-siteB")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WvLinkRouteDescription_Type.__name__ = "DisplayString"
_WvLinkRouteDescription_Object = MibScalar
wvLinkRouteDescription = _WvLinkRouteDescription_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 3),
    _WvLinkRouteDescription_Type()
)
wvLinkRouteDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkRouteDescription.setStatus("current")


class _WvTxPowerSetting_Type(Integer32):
    """Custom type wvTxPowerSetting based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 29),
    )


_WvTxPowerSetting_Type.__name__ = "Integer32"
_WvTxPowerSetting_Object = MibScalar
wvTxPowerSetting = _WvTxPowerSetting_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 4),
    _WvTxPowerSetting_Type()
)
wvTxPowerSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTxPowerSetting.setStatus("current")
if mibBuilder.loadTexts:
    wvTxPowerSetting.setUnits("dBm")


class _WvChannelNo_Type(Integer32):
    """Custom type wvChannelNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2400),
    )


_WvChannelNo_Type.__name__ = "Integer32"
_WvChannelNo_Object = MibScalar
wvChannelNo = _WvChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 5),
    _WvChannelNo_Type()
)
wvChannelNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvChannelNo.setStatus("current")


class _WvLinkCapacity_Type(Integer32):
    """Custom type wvLinkCapacity based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("e3", 6),
          ("e3PlusOneE1", 7),
          ("e3PlusTwoE1", 8),
          ("eightE1", 4),
          ("eightT1", 12),
          ("eth10-100Only", 18),
          ("eth10-100PlusFourE1", 21),
          ("eth10-100PlusFourT1", 24),
          ("eth10-100PlusOneE1", 19),
          ("eth10-100PlusOneT1", 22),
          ("eth10-100PlusTwoE1", 20),
          ("eth10-100PlusTwoT1", 23),
          ("fourE1", 3),
          ("fourT1", 11),
          ("oneE1", 1),
          ("oneT1", 9),
          ("sixteenE1", 5),
          ("sixteenT1", 13),
          ("sts1", 17),
          ("t3", 14),
          ("t3PlusFourT1", 16),
          ("t3PlusTwoT1", 15),
          ("twoE1", 2),
          ("twoT1", 10))
    )


_WvLinkCapacity_Type.__name__ = "Integer32"
_WvLinkCapacity_Object = MibScalar
wvLinkCapacity = _WvLinkCapacity_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 6),
    _WvLinkCapacity_Type()
)
wvLinkCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkCapacity.setStatus("current")


class _WvTransmitterMute_Type(Integer32):
    """Custom type wvTransmitterMute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WvTransmitterMute_Type.__name__ = "Integer32"
_WvTransmitterMute_Object = MibScalar
wvTransmitterMute = _WvTransmitterMute_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 7),
    _WvTransmitterMute_Type()
)
wvTransmitterMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTransmitterMute.setStatus("current")


class _WvReceiverMute_Type(Integer32):
    """Custom type wvReceiverMute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WvReceiverMute_Type.__name__ = "Integer32"
_WvReceiverMute_Object = MibScalar
wvReceiverMute = _WvReceiverMute_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 8),
    _WvReceiverMute_Type()
)
wvReceiverMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvReceiverMute.setStatus("current")


class _WvModulation_Type(Integer32):
    """Custom type wvModulation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cp4fsk", 2),
          ("qam128", 8),
          ("qam16", 5),
          ("qam32", 6),
          ("qam4", 3),
          ("qam64", 7),
          ("qam8", 4))
    )


_WvModulation_Type.__name__ = "Integer32"
_WvModulation_Object = MibScalar
wvModulation = _WvModulation_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 9),
    _WvModulation_Type()
)
wvModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvModulation.setStatus("current")


class _WvForceAis_Type(Integer32):
    """Custom type wvForceAis based on Integer32"""
    defaultValue = 1

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
        *(("always", 4),
          ("never", 1),
          ("onBerError", 3),
          ("onBerWarning", 2))
    )


_WvForceAis_Type.__name__ = "Integer32"
_WvForceAis_Object = MibScalar
wvForceAis = _WvForceAis_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 10),
    _WvForceAis_Type()
)
wvForceAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvForceAis.setStatus("current")


class _WvFecEnabled_Type(Integer32):
    """Custom type wvFecEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WvFecEnabled_Type.__name__ = "Integer32"
_WvFecEnabled_Object = MibScalar
wvFecEnabled = _WvFecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 11),
    _WvFecEnabled_Type()
)
wvFecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvFecEnabled.setStatus("deprecated")


class _WvFecReceiveCorrection_Type(Integer32):
    """Custom type wvFecReceiveCorrection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WvFecReceiveCorrection_Type.__name__ = "Integer32"
_WvFecReceiveCorrection_Object = MibScalar
wvFecReceiveCorrection = _WvFecReceiveCorrection_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 12),
    _WvFecReceiveCorrection_Type()
)
wvFecReceiveCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvFecReceiveCorrection.setStatus("current")


class _WvFecNoOfCorrectableBytes_Type(Integer32):
    """Custom type wvFecNoOfCorrectableBytes based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WvFecNoOfCorrectableBytes_Type.__name__ = "Integer32"
_WvFecNoOfCorrectableBytes_Object = MibScalar
wvFecNoOfCorrectableBytes = _WvFecNoOfCorrectableBytes_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 13),
    _WvFecNoOfCorrectableBytes_Type()
)
wvFecNoOfCorrectableBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvFecNoOfCorrectableBytes.setStatus("current")


class _WvEth10_100ChannelSpacing_Type(Integer32):
    """Custom type wvEth10_100ChannelSpacing based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("fifty", 6),
          ("fiftySix", 11),
          ("five", 2),
          ("fourteen", 9),
          ("seven", 8),
          ("sevenAndAHalf", 3),
          ("threeAndAHalf", 7),
          ("twelveAndAHalf", 4),
          ("twentyEight", 10),
          ("twentyFive", 5),
          ("twoAndAHalf", 1))
    )


_WvEth10_100ChannelSpacing_Type.__name__ = "Integer32"
_WvEth10_100ChannelSpacing_Object = MibScalar
wvEth10_100ChannelSpacing = _WvEth10_100ChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 14),
    _WvEth10_100ChannelSpacing_Type()
)
wvEth10_100ChannelSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100ChannelSpacing.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100ChannelSpacing.setUnits("MHz")


class _WvAtpcControl_Type(Integer32):
    """Custom type wvAtpcControl based on Integer32"""
    defaultValue = 2

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


_WvAtpcControl_Type.__name__ = "Integer32"
_WvAtpcControl_Object = MibScalar
wvAtpcControl = _WvAtpcControl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 30),
    _WvAtpcControl_Type()
)
wvAtpcControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAtpcControl.setStatus("current")


class _WvAtpcRslOptimalValue_Type(Integer32):
    """Custom type wvAtpcRslOptimalValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -15),
    )


_WvAtpcRslOptimalValue_Type.__name__ = "Integer32"
_WvAtpcRslOptimalValue_Object = MibScalar
wvAtpcRslOptimalValue = _WvAtpcRslOptimalValue_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 31),
    _WvAtpcRslOptimalValue_Type()
)
wvAtpcRslOptimalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAtpcRslOptimalValue.setStatus("current")
if mibBuilder.loadTexts:
    wvAtpcRslOptimalValue.setUnits("dBm")


class _WvAtpcRslUpperThreshold_Type(Integer32):
    """Custom type wvAtpcRslUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -15),
    )


_WvAtpcRslUpperThreshold_Type.__name__ = "Integer32"
_WvAtpcRslUpperThreshold_Object = MibScalar
wvAtpcRslUpperThreshold = _WvAtpcRslUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 32),
    _WvAtpcRslUpperThreshold_Type()
)
wvAtpcRslUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAtpcRslUpperThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wvAtpcRslUpperThreshold.setUnits("dBm")


class _WvAtpcRslLowerThreshold_Type(Integer32):
    """Custom type wvAtpcRslLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -15),
    )


_WvAtpcRslLowerThreshold_Type.__name__ = "Integer32"
_WvAtpcRslLowerThreshold_Object = MibScalar
wvAtpcRslLowerThreshold = _WvAtpcRslLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 33),
    _WvAtpcRslLowerThreshold_Type()
)
wvAtpcRslLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAtpcRslLowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wvAtpcRslLowerThreshold.setUnits("dBm")


class _WvPauseTransmitterControl_Type(Integer32):
    """Custom type wvPauseTransmitterControl based on Integer32"""
    defaultValue = 2

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


_WvPauseTransmitterControl_Type.__name__ = "Integer32"
_WvPauseTransmitterControl_Object = MibScalar
wvPauseTransmitterControl = _WvPauseTransmitterControl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 34),
    _WvPauseTransmitterControl_Type()
)
wvPauseTransmitterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvPauseTransmitterControl.setStatus("current")


class _WvPauseTransmitterTime_Type(Integer32):
    """Custom type wvPauseTransmitterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 36000),
    )


_WvPauseTransmitterTime_Type.__name__ = "Integer32"
_WvPauseTransmitterTime_Object = MibScalar
wvPauseTransmitterTime = _WvPauseTransmitterTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 35),
    _WvPauseTransmitterTime_Type()
)
wvPauseTransmitterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvPauseTransmitterTime.setStatus("current")
if mibBuilder.loadTexts:
    wvPauseTransmitterTime.setUnits("seconds")


class _WvE1BNC75ohm_Type(Integer32):
    """Custom type wvE1BNC75ohm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WvE1BNC75ohm_Type.__name__ = "Integer32"
_WvE1BNC75ohm_Object = MibScalar
wvE1BNC75ohm = _WvE1BNC75ohm_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 36),
    _WvE1BNC75ohm_Type()
)
wvE1BNC75ohm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvE1BNC75ohm.setStatus("current")


class _WvAtpcTimeOutControl_Type(Integer32):
    """Custom type wvAtpcTimeOutControl based on Integer32"""
    defaultValue = 2

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


_WvAtpcTimeOutControl_Type.__name__ = "Integer32"
_WvAtpcTimeOutControl_Object = MibScalar
wvAtpcTimeOutControl = _WvAtpcTimeOutControl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 37),
    _WvAtpcTimeOutControl_Type()
)
wvAtpcTimeOutControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAtpcTimeOutControl.setStatus("current")


class _WvAtpcTimeOutTimer_Type(Integer32):
    """Custom type wvAtpcTimeOutTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WvAtpcTimeOutTimer_Type.__name__ = "Integer32"
_WvAtpcTimeOutTimer_Object = MibScalar
wvAtpcTimeOutTimer = _WvAtpcTimeOutTimer_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 38),
    _WvAtpcTimeOutTimer_Type()
)
wvAtpcTimeOutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAtpcTimeOutTimer.setStatus("current")
if mibBuilder.loadTexts:
    wvAtpcTimeOutTimer.setUnits("minutes")


class _WvAtpcTimeOutAlarm_Type(Integer32):
    """Custom type wvAtpcTimeOutAlarm based on Integer32"""
    defaultValue = 2

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


_WvAtpcTimeOutAlarm_Type.__name__ = "Integer32"
_WvAtpcTimeOutAlarm_Object = MibScalar
wvAtpcTimeOutAlarm = _WvAtpcTimeOutAlarm_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 39),
    _WvAtpcTimeOutAlarm_Type()
)
wvAtpcTimeOutAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAtpcTimeOutAlarm.setStatus("current")


class _WvAtpcTimeOutAlarmLevel_Type(Integer32):
    """Custom type wvAtpcTimeOutAlarmLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("fatal", 3),
          ("message", 1))
    )


_WvAtpcTimeOutAlarmLevel_Type.__name__ = "Integer32"
_WvAtpcTimeOutAlarmLevel_Object = MibScalar
wvAtpcTimeOutAlarmLevel = _WvAtpcTimeOutAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 40),
    _WvAtpcTimeOutAlarmLevel_Type()
)
wvAtpcTimeOutAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAtpcTimeOutAlarmLevel.setStatus("current")


class _WvDisableAtpcInTimeOutAlarm_Type(Integer32):
    """Custom type wvDisableAtpcInTimeOutAlarm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WvDisableAtpcInTimeOutAlarm_Type.__name__ = "Integer32"
_WvDisableAtpcInTimeOutAlarm_Object = MibScalar
wvDisableAtpcInTimeOutAlarm = _WvDisableAtpcInTimeOutAlarm_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 41),
    _WvDisableAtpcInTimeOutAlarm_Type()
)
wvDisableAtpcInTimeOutAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvDisableAtpcInTimeOutAlarm.setStatus("current")


class _WvEnableSpaceDiversity_Type(Integer32):
    """Custom type wvEnableSpaceDiversity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WvEnableSpaceDiversity_Type.__name__ = "Integer32"
_WvEnableSpaceDiversity_Object = MibScalar
wvEnableSpaceDiversity = _WvEnableSpaceDiversity_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 1, 42),
    _WvEnableSpaceDiversity_Type()
)
wvEnableSpaceDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEnableSpaceDiversity.setStatus("current")
_WvInterfaces_ObjectIdentity = ObjectIdentity
wvInterfaces = _WvInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2)
)


class _WvTributaryPortConnectionsMode_Type(Integer32):
    """Custom type wvTributaryPortConnectionsMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoSensing", 2),
          ("manual", 1))
    )


_WvTributaryPortConnectionsMode_Type.__name__ = "Integer32"
_WvTributaryPortConnectionsMode_Object = MibScalar
wvTributaryPortConnectionsMode = _WvTributaryPortConnectionsMode_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 1),
    _WvTributaryPortConnectionsMode_Type()
)
wvTributaryPortConnectionsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTributaryPortConnectionsMode.setStatus("current")
_WvTributaryPortTable_Object = MibTable
wvTributaryPortTable = _WvTributaryPortTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wvTributaryPortTable.setStatus("current")
_WvTributaryPortEntry_Object = MibTableRow
wvTributaryPortEntry = _WvTributaryPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 2, 1)
)
wvTributaryPortEntry.setIndexNames(
    (0, "CODAN-MIB", "wvTributaryPortIfIndex"),
)
if mibBuilder.loadTexts:
    wvTributaryPortEntry.setStatus("current")
_WvTributaryPortIfIndex_Type = Integer32
_WvTributaryPortIfIndex_Object = MibTableColumn
wvTributaryPortIfIndex = _WvTributaryPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 2, 1, 1),
    _WvTributaryPortIfIndex_Type()
)
wvTributaryPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvTributaryPortIfIndex.setStatus("current")


class _WvTributaryPortConnection_Type(Integer32):
    """Custom type wvTributaryPortConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_WvTributaryPortConnection_Type.__name__ = "Integer32"
_WvTributaryPortConnection_Object = MibTableColumn
wvTributaryPortConnection = _WvTributaryPortConnection_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 2, 1, 2),
    _WvTributaryPortConnection_Type()
)
wvTributaryPortConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTributaryPortConnection.setStatus("current")


class _WvTributaryPortInvertedAlarm_Type(Integer32):
    """Custom type wvTributaryPortInvertedAlarm based on Integer32"""
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


_WvTributaryPortInvertedAlarm_Type.__name__ = "Integer32"
_WvTributaryPortInvertedAlarm_Object = MibTableColumn
wvTributaryPortInvertedAlarm = _WvTributaryPortInvertedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 2, 1, 3),
    _WvTributaryPortInvertedAlarm_Type()
)
wvTributaryPortInvertedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTributaryPortInvertedAlarm.setStatus("current")


class _WvTributaryPortName_Type(DisplayString):
    """Custom type wvTributaryPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WvTributaryPortName_Type.__name__ = "DisplayString"
_WvTributaryPortName_Object = MibTableColumn
wvTributaryPortName = _WvTributaryPortName_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 2, 1, 4),
    _WvTributaryPortName_Type()
)
wvTributaryPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTributaryPortName.setStatus("current")


class _WvDsx3CableLengthRange_Type(Integer32):
    """Custom type wvDsx3CableLengthRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moreThan225Feet", 2),
          ("upTo225Feet", 1))
    )


_WvDsx3CableLengthRange_Type.__name__ = "Integer32"
_WvDsx3CableLengthRange_Object = MibScalar
wvDsx3CableLengthRange = _WvDsx3CableLengthRange_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 3),
    _WvDsx3CableLengthRange_Type()
)
wvDsx3CableLengthRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvDsx3CableLengthRange.setStatus("current")


class _WvSlipConnection_Type(Integer32):
    """Custom type wvSlipConnection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("modem", 2))
    )


_WvSlipConnection_Type.__name__ = "Integer32"
_WvSlipConnection_Object = MibScalar
wvSlipConnection = _WvSlipConnection_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 4),
    _WvSlipConnection_Type()
)
wvSlipConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSlipConnection.setStatus("current")


class _WvTelephoneNumber_Type(DisplayString):
    """Custom type wvTelephoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_WvTelephoneNumber_Type.__name__ = "DisplayString"
_WvTelephoneNumber_Object = MibScalar
wvTelephoneNumber = _WvTelephoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 5),
    _WvTelephoneNumber_Type()
)
wvTelephoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTelephoneNumber.setStatus("current")


class _WvDialPrefixString_Type(DisplayString):
    """Custom type wvDialPrefixString based on DisplayString"""
    defaultValue = OctetString("ATDT")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WvDialPrefixString_Type.__name__ = "DisplayString"
_WvDialPrefixString_Object = MibScalar
wvDialPrefixString = _WvDialPrefixString_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 6),
    _WvDialPrefixString_Type()
)
wvDialPrefixString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvDialPrefixString.setStatus("current")


class _WvInitString_Type(DisplayString):
    """Custom type wvInitString based on DisplayString"""
    defaultValue = OctetString("ATZ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WvInitString_Type.__name__ = "DisplayString"
_WvInitString_Object = MibScalar
wvInitString = _WvInitString_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 7),
    _WvInitString_Type()
)
wvInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvInitString.setStatus("current")


class _WvEth10_100SysCtrl_Type(Bits):
    """Custom type wvEth10_100SysCtrl based on Bits"""
    namedValues = NamedValues(
        *(("aging", 0),
          ("crcCheck", 1),
          ("flowCtrl", 2))
    )

_WvEth10_100SysCtrl_Type.__name__ = "Bits"
_WvEth10_100SysCtrl_Object = MibScalar
wvEth10_100SysCtrl = _WvEth10_100SysCtrl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 20),
    _WvEth10_100SysCtrl_Type()
)
wvEth10_100SysCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100SysCtrl.setStatus("current")


class _WvEth10_100SysAgingTime_Type(Integer32):
    """Custom type wvEth10_100SysAgingTime based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524280),
    )


_WvEth10_100SysAgingTime_Type.__name__ = "Integer32"
_WvEth10_100SysAgingTime_Object = MibScalar
wvEth10_100SysAgingTime = _WvEth10_100SysAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 21),
    _WvEth10_100SysAgingTime_Type()
)
wvEth10_100SysAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100SysAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100SysAgingTime.setUnits("seconds")
_WvEth10_100PortTable_Object = MibTable
wvEth10_100PortTable = _WvEth10_100PortTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 22)
)
if mibBuilder.loadTexts:
    wvEth10_100PortTable.setStatus("current")
_WvEth10_100PortEntry_Object = MibTableRow
wvEth10_100PortEntry = _WvEth10_100PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 22, 1)
)
wvEth10_100PortEntry.setIndexNames(
    (0, "CODAN-MIB", "wvEth10-100PortIfIndex"),
)
if mibBuilder.loadTexts:
    wvEth10_100PortEntry.setStatus("current")
_WvEth10_100PortIfIndex_Type = Integer32
_WvEth10_100PortIfIndex_Object = MibScalar
wvEth10_100PortIfIndex = _WvEth10_100PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 22, 1, 1),
    _WvEth10_100PortIfIndex_Type()
)
wvEth10_100PortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvEth10_100PortIfIndex.setStatus("current")


class _WvEth10_100PortCtrl_Type(Bits):
    """Custom type wvEth10_100PortCtrl based on Bits"""
    namedValues = NamedValues(
        *(("autoNegotiation", 2),
          ("fastSpeed", 0),
          ("forceDisconnectOnLinkDown", 3),
          ("fullDuplex", 1))
    )

_WvEth10_100PortCtrl_Type.__name__ = "Bits"
_WvEth10_100PortCtrl_Object = MibScalar
wvEth10_100PortCtrl = _WvEth10_100PortCtrl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 22, 1, 2),
    _WvEth10_100PortCtrl_Type()
)
wvEth10_100PortCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100PortCtrl.setStatus("current")


class _WvEth10_100PortStatus_Type(Bits):
    """Custom type wvEth10_100PortStatus based on Bits"""
    namedValues = NamedValues(
        *(("cslAlarm", 2),
          ("ecAlarm", 3),
          ("fastSpeedOn", 0),
          ("fullDuplexOn", 1),
          ("imreAlarm", 5),
          ("imteAlarm", 4))
    )

_WvEth10_100PortStatus_Type.__name__ = "Bits"
_WvEth10_100PortStatus_Object = MibScalar
wvEth10_100PortStatus = _WvEth10_100PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 22, 1, 3),
    _WvEth10_100PortStatus_Type()
)
wvEth10_100PortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvEth10_100PortStatus.setStatus("current")
_WvEth10_100PortClearStats_Type = Integer32
_WvEth10_100PortClearStats_Object = MibScalar
wvEth10_100PortClearStats = _WvEth10_100PortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 22, 1, 4),
    _WvEth10_100PortClearStats_Type()
)
wvEth10_100PortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100PortClearStats.setStatus("current")


class _WvEth10_100PortThroughputCtrl_Type(Integer32):
    """Custom type wvEth10_100PortThroughputCtrl based on Integer32"""
    defaultValue = 1

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
        *(("limit128K", 2),
          ("limit1M", 5),
          ("limit256K", 3),
          ("limit2M", 6),
          ("limit4M", 7),
          ("limit512K", 4),
          ("limit8M", 8),
          ("unlimited", 1))
    )


_WvEth10_100PortThroughputCtrl_Type.__name__ = "Integer32"
_WvEth10_100PortThroughputCtrl_Object = MibScalar
wvEth10_100PortThroughputCtrl = _WvEth10_100PortThroughputCtrl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 22, 1, 5),
    _WvEth10_100PortThroughputCtrl_Type()
)
wvEth10_100PortThroughputCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100PortThroughputCtrl.setStatus("current")
_WvEth10_100AvailCapacity_Type = Integer32
_WvEth10_100AvailCapacity_Object = MibScalar
wvEth10_100AvailCapacity = _WvEth10_100AvailCapacity_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 23),
    _WvEth10_100AvailCapacity_Type()
)
wvEth10_100AvailCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvEth10_100AvailCapacity.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100AvailCapacity.setUnits("Bits/sec")
_WvRs232PortTable_Object = MibTable
wvRs232PortTable = _WvRs232PortTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 30)
)
if mibBuilder.loadTexts:
    wvRs232PortTable.setStatus("current")
_WvRs232PortEntry_Object = MibTableRow
wvRs232PortEntry = _WvRs232PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 30, 1)
)
wvRs232PortEntry.setIndexNames(
    (0, "CODAN-MIB", "wvRs232PortIndex"),
)
if mibBuilder.loadTexts:
    wvRs232PortEntry.setStatus("current")
_WvRs232PortIndex_Type = Integer32
_WvRs232PortIndex_Object = MibTableColumn
wvRs232PortIndex = _WvRs232PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 30, 1, 1),
    _WvRs232PortIndex_Type()
)
wvRs232PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvRs232PortIndex.setStatus("current")


class _WvRs232PortType_Type(Integer32):
    """Custom type wvRs232PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 2),
          ("rs422", 3))
    )


_WvRs232PortType_Type.__name__ = "Integer32"
_WvRs232PortType_Object = MibTableColumn
wvRs232PortType = _WvRs232PortType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 30, 1, 2),
    _WvRs232PortType_Type()
)
wvRs232PortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRs232PortType.setStatus("current")
_WvRs232PortSpeed_Type = Integer32
_WvRs232PortSpeed_Object = MibTableColumn
wvRs232PortSpeed = _WvRs232PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 30, 1, 3),
    _WvRs232PortSpeed_Type()
)
wvRs232PortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRs232PortSpeed.setStatus("current")


class _WvRs232PortFlowType_Type(Integer32):
    """Custom type wvRs232PortFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xonXoff", 2))
    )


_WvRs232PortFlowType_Type.__name__ = "Integer32"
_WvRs232PortFlowType_Object = MibTableColumn
wvRs232PortFlowType = _WvRs232PortFlowType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 30, 1, 4),
    _WvRs232PortFlowType_Type()
)
wvRs232PortFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRs232PortFlowType.setStatus("current")


class _WvRs232AsyncPortBits_Type(Integer32):
    """Custom type wvRs232AsyncPortBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_WvRs232AsyncPortBits_Type.__name__ = "Integer32"
_WvRs232AsyncPortBits_Object = MibTableColumn
wvRs232AsyncPortBits = _WvRs232AsyncPortBits_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 30, 1, 5),
    _WvRs232AsyncPortBits_Type()
)
wvRs232AsyncPortBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRs232AsyncPortBits.setStatus("current")


class _WvRs232AsyncPortStopBits_Type(Integer32):
    """Custom type wvRs232AsyncPortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WvRs232AsyncPortStopBits_Type.__name__ = "Integer32"
_WvRs232AsyncPortStopBits_Object = MibTableColumn
wvRs232AsyncPortStopBits = _WvRs232AsyncPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 30, 1, 6),
    _WvRs232AsyncPortStopBits_Type()
)
wvRs232AsyncPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRs232AsyncPortStopBits.setStatus("current")


class _WvRs232AsyncPortParity_Type(Integer32):
    """Custom type wvRs232AsyncPortParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_WvRs232AsyncPortParity_Type.__name__ = "Integer32"
_WvRs232AsyncPortParity_Object = MibTableColumn
wvRs232AsyncPortParity = _WvRs232AsyncPortParity_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 2, 30, 1, 7),
    _WvRs232AsyncPortParity_Type()
)
wvRs232AsyncPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRs232AsyncPortParity.setStatus("current")
_WvManagement_ObjectIdentity = ObjectIdentity
wvManagement = _WvManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3)
)
_WvUpdateTerminalConfiguration_Type = Integer32
_WvUpdateTerminalConfiguration_Object = MibScalar
wvUpdateTerminalConfiguration = _WvUpdateTerminalConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 2),
    _WvUpdateTerminalConfiguration_Type()
)
wvUpdateTerminalConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvUpdateTerminalConfiguration.setStatus("current")
_WvActivateTerminalConfiguration_Type = Integer32
_WvActivateTerminalConfiguration_Object = MibScalar
wvActivateTerminalConfiguration = _WvActivateTerminalConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 3),
    _WvActivateTerminalConfiguration_Type()
)
wvActivateTerminalConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvActivateTerminalConfiguration.setStatus("current")


class _WvResetTerminal_Type(Integer32):
    """Custom type wvResetTerminal based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("coldSwitchOver", 3),
          ("oduSwitchOver", 6),
          ("running", 5),
          ("terminalSwitchOver", 4),
          ("warm", 2))
    )


_WvResetTerminal_Type.__name__ = "Integer32"
_WvResetTerminal_Object = MibScalar
wvResetTerminal = _WvResetTerminal_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 4),
    _WvResetTerminal_Type()
)
wvResetTerminal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvResetTerminal.setStatus("current")
_WvActivateTerminalConfigurationTime_Type = TimeTicks
_WvActivateTerminalConfigurationTime_Object = MibScalar
wvActivateTerminalConfigurationTime = _WvActivateTerminalConfigurationTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 5),
    _WvActivateTerminalConfigurationTime_Type()
)
wvActivateTerminalConfigurationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvActivateTerminalConfigurationTime.setStatus("current")


class _WvSavedActiveConfiguration_Type(Integer32):
    """Custom type wvSavedActiveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefault", 4),
          ("none", 5),
          ("savedConfiguration1", 1),
          ("savedConfiguration2", 2),
          ("savedConfiguration3", 3))
    )


_WvSavedActiveConfiguration_Type.__name__ = "Integer32"
_WvSavedActiveConfiguration_Object = MibScalar
wvSavedActiveConfiguration = _WvSavedActiveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 6),
    _WvSavedActiveConfiguration_Type()
)
wvSavedActiveConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSavedActiveConfiguration.setStatus("deprecated")
_WvOnePlusOneRequestSwitchOut_Type = Integer32
_WvOnePlusOneRequestSwitchOut_Object = MibScalar
wvOnePlusOneRequestSwitchOut = _WvOnePlusOneRequestSwitchOut_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 7),
    _WvOnePlusOneRequestSwitchOut_Type()
)
wvOnePlusOneRequestSwitchOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvOnePlusOneRequestSwitchOut.setStatus("current")


class _WvFrontPanelUserPassword_Type(FrontPanelPassword):
    """Custom type wvFrontPanelUserPassword based on FrontPanelPassword"""
    defaultHexValue = "0101010101"


_WvFrontPanelUserPassword_Object = MibScalar
wvFrontPanelUserPassword = _WvFrontPanelUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 10),
    _WvFrontPanelUserPassword_Type()
)
wvFrontPanelUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvFrontPanelUserPassword.setStatus("current")


class _WvFrontPanelAdminPassword_Type(FrontPanelPassword):
    """Custom type wvFrontPanelAdminPassword based on FrontPanelPassword"""
    defaultHexValue = "0101020202"


_WvFrontPanelAdminPassword_Object = MibScalar
wvFrontPanelAdminPassword = _WvFrontPanelAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 11),
    _WvFrontPanelAdminPassword_Type()
)
wvFrontPanelAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvFrontPanelAdminPassword.setStatus("current")


class _WvFrontPanelSupervisorPassword_Type(FrontPanelPassword):
    """Custom type wvFrontPanelSupervisorPassword based on FrontPanelPassword"""
    defaultHexValue = "0101030304"


_WvFrontPanelSupervisorPassword_Object = MibScalar
wvFrontPanelSupervisorPassword = _WvFrontPanelSupervisorPassword_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 12),
    _WvFrontPanelSupervisorPassword_Type()
)
wvFrontPanelSupervisorPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvFrontPanelSupervisorPassword.setStatus("current")


class _WvResetOdu_Type(Integer32):
    """Custom type wvResetOdu based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("coldSwitchOver", 2),
          ("running", 3))
    )


_WvResetOdu_Type.__name__ = "Integer32"
_WvResetOdu_Object = MibScalar
wvResetOdu = _WvResetOdu_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 15),
    _WvResetOdu_Type()
)
wvResetOdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvResetOdu.setStatus("current")
_WvSlipInIPAddress_Type = IpAddress
_WvSlipInIPAddress_Object = MibScalar
wvSlipInIPAddress = _WvSlipInIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 20),
    _WvSlipInIPAddress_Type()
)
wvSlipInIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSlipInIPAddress.setStatus("current")
_WvSlipInIPSubnetMask_Type = IpAddress
_WvSlipInIPSubnetMask_Object = MibScalar
wvSlipInIPSubnetMask = _WvSlipInIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 21),
    _WvSlipInIPSubnetMask_Type()
)
wvSlipInIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSlipInIPSubnetMask.setStatus("current")
_WvSlipOutIPAddress_Type = IpAddress
_WvSlipOutIPAddress_Object = MibScalar
wvSlipOutIPAddress = _WvSlipOutIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 22),
    _WvSlipOutIPAddress_Type()
)
wvSlipOutIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSlipOutIPAddress.setStatus("current")
_WvSlipOutIPSubnetMask_Type = IpAddress
_WvSlipOutIPSubnetMask_Object = MibScalar
wvSlipOutIPSubnetMask = _WvSlipOutIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 23),
    _WvSlipOutIPSubnetMask_Type()
)
wvSlipOutIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSlipOutIPSubnetMask.setStatus("current")
_WvLanIPAddress_Type = IpAddress
_WvLanIPAddress_Object = MibScalar
wvLanIPAddress = _WvLanIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 24),
    _WvLanIPAddress_Type()
)
wvLanIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLanIPAddress.setStatus("current")
_WvLanIPSubnetMask_Type = IpAddress
_WvLanIPSubnetMask_Object = MibScalar
wvLanIPSubnetMask = _WvLanIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 25),
    _WvLanIPSubnetMask_Type()
)
wvLanIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLanIPSubnetMask.setStatus("current")
_WvLinkIPAddress_Type = IpAddress
_WvLinkIPAddress_Object = MibScalar
wvLinkIPAddress = _WvLinkIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 26),
    _WvLinkIPAddress_Type()
)
wvLinkIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkIPAddress.setStatus("current")
_WvLinkIPSubnetMask_Type = IpAddress
_WvLinkIPSubnetMask_Object = MibScalar
wvLinkIPSubnetMask = _WvLinkIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 27),
    _WvLinkIPSubnetMask_Type()
)
wvLinkIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkIPSubnetMask.setStatus("current")
_WvEth10_100ManIPAddress_Type = IpAddress
_WvEth10_100ManIPAddress_Object = MibScalar
wvEth10_100ManIPAddress = _WvEth10_100ManIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 28),
    _WvEth10_100ManIPAddress_Type()
)
wvEth10_100ManIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100ManIPAddress.setStatus("current")
_WvEth10_100ManIPSubnetMask_Type = IpAddress
_WvEth10_100ManIPSubnetMask_Object = MibScalar
wvEth10_100ManIPSubnetMask = _WvEth10_100ManIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 29),
    _WvEth10_100ManIPSubnetMask_Type()
)
wvEth10_100ManIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100ManIPSubnetMask.setStatus("current")
_WvPeerSlipInIPAddress_Type = IpAddress
_WvPeerSlipInIPAddress_Object = MibScalar
wvPeerSlipInIPAddress = _WvPeerSlipInIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 30),
    _WvPeerSlipInIPAddress_Type()
)
wvPeerSlipInIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerSlipInIPAddress.setStatus("current")
_WvPeerSlipInIPSubnetMask_Type = IpAddress
_WvPeerSlipInIPSubnetMask_Object = MibScalar
wvPeerSlipInIPSubnetMask = _WvPeerSlipInIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 31),
    _WvPeerSlipInIPSubnetMask_Type()
)
wvPeerSlipInIPSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerSlipInIPSubnetMask.setStatus("current")
_WvPeerSlipOutIPAddress_Type = IpAddress
_WvPeerSlipOutIPAddress_Object = MibScalar
wvPeerSlipOutIPAddress = _WvPeerSlipOutIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 32),
    _WvPeerSlipOutIPAddress_Type()
)
wvPeerSlipOutIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerSlipOutIPAddress.setStatus("current")
_WvPeerSlipOutIPSubnetMask_Type = IpAddress
_WvPeerSlipOutIPSubnetMask_Object = MibScalar
wvPeerSlipOutIPSubnetMask = _WvPeerSlipOutIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 33),
    _WvPeerSlipOutIPSubnetMask_Type()
)
wvPeerSlipOutIPSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerSlipOutIPSubnetMask.setStatus("current")
_WvPeerLanIPAddress_Type = IpAddress
_WvPeerLanIPAddress_Object = MibScalar
wvPeerLanIPAddress = _WvPeerLanIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 34),
    _WvPeerLanIPAddress_Type()
)
wvPeerLanIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerLanIPAddress.setStatus("current")
_WvPeerLanIPSubnetMask_Type = IpAddress
_WvPeerLanIPSubnetMask_Object = MibScalar
wvPeerLanIPSubnetMask = _WvPeerLanIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 35),
    _WvPeerLanIPSubnetMask_Type()
)
wvPeerLanIPSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerLanIPSubnetMask.setStatus("current")
_WvPeerLinkIPAddress_Type = IpAddress
_WvPeerLinkIPAddress_Object = MibScalar
wvPeerLinkIPAddress = _WvPeerLinkIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 36),
    _WvPeerLinkIPAddress_Type()
)
wvPeerLinkIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerLinkIPAddress.setStatus("current")
_WvPeerLinkIPSubnetMask_Type = IpAddress
_WvPeerLinkIPSubnetMask_Object = MibScalar
wvPeerLinkIPSubnetMask = _WvPeerLinkIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 37),
    _WvPeerLinkIPSubnetMask_Type()
)
wvPeerLinkIPSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerLinkIPSubnetMask.setStatus("current")
_WvPeerEth10_100ManIPAddress_Type = IpAddress
_WvPeerEth10_100ManIPAddress_Object = MibScalar
wvPeerEth10_100ManIPAddress = _WvPeerEth10_100ManIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 38),
    _WvPeerEth10_100ManIPAddress_Type()
)
wvPeerEth10_100ManIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerEth10_100ManIPAddress.setStatus("current")
_WvPeerEth10_100ManIPSubnetMask_Type = IpAddress
_WvPeerEth10_100ManIPSubnetMask_Object = MibScalar
wvPeerEth10_100ManIPSubnetMask = _WvPeerEth10_100ManIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 39),
    _WvPeerEth10_100ManIPSubnetMask_Type()
)
wvPeerEth10_100ManIPSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvPeerEth10_100ManIPSubnetMask.setStatus("current")
_WvSlipInDestIPAddress_Type = IpAddress
_WvSlipInDestIPAddress_Object = MibScalar
wvSlipInDestIPAddress = _WvSlipInDestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 40),
    _WvSlipInDestIPAddress_Type()
)
wvSlipInDestIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSlipInDestIPAddress.setStatus("current")
_WvSlipInDestIPSubnetMask_Type = IpAddress
_WvSlipInDestIPSubnetMask_Object = MibScalar
wvSlipInDestIPSubnetMask = _WvSlipInDestIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 41),
    _WvSlipInDestIPSubnetMask_Type()
)
wvSlipInDestIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSlipInDestIPSubnetMask.setStatus("deprecated")
_WvSlipOutDestIPAddress_Type = IpAddress
_WvSlipOutDestIPAddress_Object = MibScalar
wvSlipOutDestIPAddress = _WvSlipOutDestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 42),
    _WvSlipOutDestIPAddress_Type()
)
wvSlipOutDestIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSlipOutDestIPAddress.setStatus("current")
_WvSlipOutDestIPSubnetMask_Type = IpAddress
_WvSlipOutDestIPSubnetMask_Object = MibScalar
wvSlipOutDestIPSubnetMask = _WvSlipOutDestIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 43),
    _WvSlipOutDestIPSubnetMask_Type()
)
wvSlipOutDestIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSlipOutDestIPSubnetMask.setStatus("deprecated")
_WvOnePlusOneCompanionLinkIPAddress_Type = IpAddress
_WvOnePlusOneCompanionLinkIPAddress_Object = MibScalar
wvOnePlusOneCompanionLinkIPAddress = _WvOnePlusOneCompanionLinkIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 44),
    _WvOnePlusOneCompanionLinkIPAddress_Type()
)
wvOnePlusOneCompanionLinkIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOnePlusOneCompanionLinkIPAddress.setStatus("current")
_WvOnePlusOneCompanionEthIPAddress_Type = IpAddress
_WvOnePlusOneCompanionEthIPAddress_Object = MibScalar
wvOnePlusOneCompanionEthIPAddress = _WvOnePlusOneCompanionEthIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 45),
    _WvOnePlusOneCompanionEthIPAddress_Type()
)
wvOnePlusOneCompanionEthIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvOnePlusOneCompanionEthIPAddress.setStatus("current")
_WvUserRoutesManagement_ObjectIdentity = ObjectIdentity
wvUserRoutesManagement = _WvUserRoutesManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50)
)
_WvUserRoutesTable_Object = MibTable
wvUserRoutesTable = _WvUserRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50, 1)
)
if mibBuilder.loadTexts:
    wvUserRoutesTable.setStatus("current")
_WvUserRoutesEntry_Object = MibTableRow
wvUserRoutesEntry = _WvUserRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50, 1, 1)
)
wvUserRoutesEntry.setIndexNames(
    (0, "CODAN-MIB", "wvUserRoutesIndex"),
)
if mibBuilder.loadTexts:
    wvUserRoutesEntry.setStatus("current")


class _WvUserRoutesIndex_Type(Integer32):
    """Custom type wvUserRoutesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WvUserRoutesIndex_Type.__name__ = "Integer32"
_WvUserRoutesIndex_Object = MibTableColumn
wvUserRoutesIndex = _WvUserRoutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50, 1, 1, 1),
    _WvUserRoutesIndex_Type()
)
wvUserRoutesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvUserRoutesIndex.setStatus("current")
_WvUserRoutesDest_Type = IpAddress
_WvUserRoutesDest_Object = MibTableColumn
wvUserRoutesDest = _WvUserRoutesDest_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50, 1, 1, 2),
    _WvUserRoutesDest_Type()
)
wvUserRoutesDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvUserRoutesDest.setStatus("current")
_WvUserRoutesHop_Type = IpAddress
_WvUserRoutesHop_Object = MibTableColumn
wvUserRoutesHop = _WvUserRoutesHop_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50, 1, 1, 3),
    _WvUserRoutesHop_Type()
)
wvUserRoutesHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvUserRoutesHop.setStatus("current")
_WvUserRoutesMask_Type = IpAddress
_WvUserRoutesMask_Object = MibTableColumn
wvUserRoutesMask = _WvUserRoutesMask_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50, 1, 1, 4),
    _WvUserRoutesMask_Type()
)
wvUserRoutesMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvUserRoutesMask.setStatus("current")


class _WvUserRoutesIf_Type(Integer32):
    """Custom type wvUserRoutesIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eth", 1),
          ("eth10-100", 2),
          ("link", 3),
          ("nms-in", 4),
          ("nms-out", 5),
          ("sys-choice", 6))
    )


_WvUserRoutesIf_Type.__name__ = "Integer32"
_WvUserRoutesIf_Object = MibTableColumn
wvUserRoutesIf = _WvUserRoutesIf_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50, 1, 1, 5),
    _WvUserRoutesIf_Type()
)
wvUserRoutesIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvUserRoutesIf.setStatus("current")


class _WvUserRoutesType_Type(Integer32):
    """Custom type wvUserRoutesType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WvUserRoutesType_Type.__name__ = "Integer32"
_WvUserRoutesType_Object = MibTableColumn
wvUserRoutesType = _WvUserRoutesType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50, 1, 1, 6),
    _WvUserRoutesType_Type()
)
wvUserRoutesType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvUserRoutesType.setStatus("current")


class _WvUserRoutesCount_Type(Integer32):
    """Custom type wvUserRoutesCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WvUserRoutesCount_Type.__name__ = "Integer32"
_WvUserRoutesCount_Object = MibScalar
wvUserRoutesCount = _WvUserRoutesCount_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 50, 2),
    _WvUserRoutesCount_Type()
)
wvUserRoutesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvUserRoutesCount.setStatus("current")
_WvSetOperationId_Type = TestAndIncr
_WvSetOperationId_Object = MibScalar
wvSetOperationId = _WvSetOperationId_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 100),
    _WvSetOperationId_Type()
)
wvSetOperationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSetOperationId.setStatus("current")


class _WvSetOperationCtrl_Type(Integer32):
    """Custom type wvSetOperationCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setDisabled", 2),
          ("setEnabled", 1))
    )


_WvSetOperationCtrl_Type.__name__ = "Integer32"
_WvSetOperationCtrl_Object = MibScalar
wvSetOperationCtrl = _WvSetOperationCtrl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 101),
    _WvSetOperationCtrl_Type()
)
wvSetOperationCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSetOperationCtrl.setStatus("current")


class _WvSetOperationOwner_Type(DisplayString):
    """Custom type wvSetOperationOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_WvSetOperationOwner_Type.__name__ = "DisplayString"
_WvSetOperationOwner_Object = MibScalar
wvSetOperationOwner = _WvSetOperationOwner_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 102),
    _WvSetOperationOwner_Type()
)
wvSetOperationOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSetOperationOwner.setStatus("current")


class _WvConfigurationChangedStatus_Type(Bits):
    """Custom type wvConfigurationChangedStatus based on Bits"""
    namedValues = NamedValues(
        *(("dsx1ConfigTable", 6),
          ("dsx3ConfigTable", 7),
          ("filler", 0),
          ("ifTestTable", 4),
          ("interfaces", 3),
          ("ipAddrTable", 5),
          ("rs232", 8),
          ("system", 10),
          ("wvAlarmControl", 13),
          ("wvExternalInputTable", 12),
          ("wvInterfaces", 2),
          ("wvLinkSettings", 1),
          ("wvManagement", 9),
          ("wvRelayTable", 11),
          ("wvTests", 14))
    )

_WvConfigurationChangedStatus_Type.__name__ = "Bits"
_WvConfigurationChangedStatus_Object = MibScalar
wvConfigurationChangedStatus = _WvConfigurationChangedStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 103),
    _WvConfigurationChangedStatus_Type()
)
wvConfigurationChangedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvConfigurationChangedStatus.setStatus("deprecated")
_WvCommunityTable_Object = MibTable
wvCommunityTable = _WvCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 110)
)
if mibBuilder.loadTexts:
    wvCommunityTable.setStatus("current")
_WvCommunityEntry_Object = MibTableRow
wvCommunityEntry = _WvCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 110, 1)
)
wvCommunityEntry.setIndexNames(
    (0, "CODAN-MIB", "wvCommunityId"),
)
if mibBuilder.loadTexts:
    wvCommunityEntry.setStatus("current")


class _WvCommunityId_Type(Integer32):
    """Custom type wvCommunityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WvCommunityId_Type.__name__ = "Integer32"
_WvCommunityId_Object = MibTableColumn
wvCommunityId = _WvCommunityId_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 110, 1, 1),
    _WvCommunityId_Type()
)
wvCommunityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvCommunityId.setStatus("current")


class _WvCommunityName_Type(DisplayString):
    """Custom type wvCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WvCommunityName_Type.__name__ = "DisplayString"
_WvCommunityName_Object = MibTableColumn
wvCommunityName = _WvCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 110, 1, 2),
    _WvCommunityName_Type()
)
wvCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvCommunityName.setStatus("current")


class _WvCommunityPrivilege_Type(Integer32):
    """Custom type wvCommunityPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_WvCommunityPrivilege_Type.__name__ = "Integer32"
_WvCommunityPrivilege_Object = MibTableColumn
wvCommunityPrivilege = _WvCommunityPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 110, 1, 3),
    _WvCommunityPrivilege_Type()
)
wvCommunityPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvCommunityPrivilege.setStatus("current")
_WvTrapRecipientsTable_Object = MibTable
wvTrapRecipientsTable = _WvTrapRecipientsTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 111)
)
if mibBuilder.loadTexts:
    wvTrapRecipientsTable.setStatus("current")
_WvTrapRecipientsEntry_Object = MibTableRow
wvTrapRecipientsEntry = _WvTrapRecipientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 111, 1)
)
wvTrapRecipientsEntry.setIndexNames(
    (0, "CODAN-MIB", "wvTrapRecipientsId"),
)
if mibBuilder.loadTexts:
    wvTrapRecipientsEntry.setStatus("current")


class _WvTrapRecipientsId_Type(Integer32):
    """Custom type wvTrapRecipientsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WvTrapRecipientsId_Type.__name__ = "Integer32"
_WvTrapRecipientsId_Object = MibTableColumn
wvTrapRecipientsId = _WvTrapRecipientsId_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 111, 1, 1),
    _WvTrapRecipientsId_Type()
)
wvTrapRecipientsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvTrapRecipientsId.setStatus("current")
_WvTrapRecipientsIp_Type = IpAddress
_WvTrapRecipientsIp_Object = MibTableColumn
wvTrapRecipientsIp = _WvTrapRecipientsIp_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 111, 1, 2),
    _WvTrapRecipientsIp_Type()
)
wvTrapRecipientsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTrapRecipientsIp.setStatus("current")
_WvTftpServerIpAddress_Type = IpAddress
_WvTftpServerIpAddress_Object = MibScalar
wvTftpServerIpAddress = _WvTftpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 200),
    _WvTftpServerIpAddress_Type()
)
wvTftpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTftpServerIpAddress.setStatus("current")


class _WvTftpOperationCtrl_Type(Integer32):
    """Custom type wvTftpOperationCtrl based on Integer32"""
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


_WvTftpOperationCtrl_Type.__name__ = "Integer32"
_WvTftpOperationCtrl_Object = MibScalar
wvTftpOperationCtrl = _WvTftpOperationCtrl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 201),
    _WvTftpOperationCtrl_Type()
)
wvTftpOperationCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTftpOperationCtrl.setStatus("current")


class _WvTftpNoOfRetries_Type(Integer32):
    """Custom type wvTftpNoOfRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_WvTftpNoOfRetries_Type.__name__ = "Integer32"
_WvTftpNoOfRetries_Object = MibScalar
wvTftpNoOfRetries = _WvTftpNoOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 202),
    _WvTftpNoOfRetries_Type()
)
wvTftpNoOfRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTftpNoOfRetries.setStatus("current")


class _WvTftpFileName_Type(DisplayString):
    """Custom type wvTftpFileName based on DisplayString"""
    defaultValue = OctetString("\\codan.lst")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WvTftpFileName_Type.__name__ = "DisplayString"
_WvTftpFileName_Object = MibScalar
wvTftpFileName = _WvTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 203),
    _WvTftpFileName_Type()
)
wvTftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTftpFileName.setStatus("current")
_WvTftpStartTime_Type = TimeTicks
_WvTftpStartTime_Object = MibScalar
wvTftpStartTime = _WvTftpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 204),
    _WvTftpStartTime_Type()
)
wvTftpStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTftpStartTime.setStatus("current")
_WvTftpRemainingStartTime_Type = TimeTicks
_WvTftpRemainingStartTime_Object = MibScalar
wvTftpRemainingStartTime = _WvTftpRemainingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 205),
    _WvTftpRemainingStartTime_Type()
)
wvTftpRemainingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvTftpRemainingStartTime.setStatus("current")
_WvSwModuleTable_Object = MibTable
wvSwModuleTable = _WvSwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 210)
)
if mibBuilder.loadTexts:
    wvSwModuleTable.setStatus("current")
_WvSwModuleEntry_Object = MibTableRow
wvSwModuleEntry = _WvSwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 210, 1)
)
wvSwModuleEntry.setIndexNames(
    (0, "CODAN-MIB", "wvSwModuleIndex"),
)
if mibBuilder.loadTexts:
    wvSwModuleEntry.setStatus("current")


class _WvSwModuleIndex_Type(Integer32):
    """Custom type wvSwModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WvSwModuleIndex_Type.__name__ = "Integer32"
_WvSwModuleIndex_Object = MibTableColumn
wvSwModuleIndex = _WvSwModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 210, 1, 1),
    _WvSwModuleIndex_Type()
)
wvSwModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSwModuleIndex.setStatus("current")


class _WvSwModuleName_Type(DisplayString):
    """Custom type wvSwModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WvSwModuleName_Type.__name__ = "DisplayString"
_WvSwModuleName_Object = MibTableColumn
wvSwModuleName = _WvSwModuleName_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 210, 1, 2),
    _WvSwModuleName_Type()
)
wvSwModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSwModuleName.setStatus("current")
_WvSwModuleActiveRev_Type = ComponentRevision
_WvSwModuleActiveRev_Object = MibTableColumn
wvSwModuleActiveRev = _WvSwModuleActiveRev_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 210, 1, 3),
    _WvSwModuleActiveRev_Type()
)
wvSwModuleActiveRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSwModuleActiveRev.setStatus("current")


class _WvSwModuleActiveCS_Type(Integer32):
    """Custom type wvSwModuleActiveCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WvSwModuleActiveCS_Type.__name__ = "Integer32"
_WvSwModuleActiveCS_Object = MibTableColumn
wvSwModuleActiveCS = _WvSwModuleActiveCS_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 210, 1, 4),
    _WvSwModuleActiveCS_Type()
)
wvSwModuleActiveCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSwModuleActiveCS.setStatus("current")
_WvSwModuleStandByRev_Type = ComponentRevision
_WvSwModuleStandByRev_Object = MibTableColumn
wvSwModuleStandByRev = _WvSwModuleStandByRev_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 210, 1, 5),
    _WvSwModuleStandByRev_Type()
)
wvSwModuleStandByRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSwModuleStandByRev.setStatus("current")


class _WvSwModuleStandByCS_Type(Integer32):
    """Custom type wvSwModuleStandByCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WvSwModuleStandByCS_Type.__name__ = "Integer32"
_WvSwModuleStandByCS_Object = MibTableColumn
wvSwModuleStandByCS = _WvSwModuleStandByCS_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 210, 1, 6),
    _WvSwModuleStandByCS_Type()
)
wvSwModuleStandByCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSwModuleStandByCS.setStatus("current")


class _WvResetPerformance_Type(Integer32):
    """Custom type wvResetPerformance based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WvResetPerformance_Type.__name__ = "Integer32"
_WvResetPerformance_Object = MibScalar
wvResetPerformance = _WvResetPerformance_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 3, 215),
    _WvResetPerformance_Type()
)
wvResetPerformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvResetPerformance.setStatus("current")
_WvRelays_ObjectIdentity = ObjectIdentity
wvRelays = _WvRelays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4)
)
_WvRelayTable_Object = MibTable
wvRelayTable = _WvRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wvRelayTable.setStatus("current")
_WvRelayEntry_Object = MibTableRow
wvRelayEntry = _WvRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4, 1, 1)
)
wvRelayEntry.setIndexNames(
    (0, "CODAN-MIB", "wvRelayId"),
)
if mibBuilder.loadTexts:
    wvRelayEntry.setStatus("current")


class _WvRelayId_Type(Integer32):
    """Custom type wvRelayId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_WvRelayId_Type.__name__ = "Integer32"
_WvRelayId_Object = MibTableColumn
wvRelayId = _WvRelayId_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4, 1, 1, 1),
    _WvRelayId_Type()
)
wvRelayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvRelayId.setStatus("current")


class _WvRelayOperation_Type(Integer32):
    """Custom type wvRelayOperation based on Integer32"""
    defaultValue = 1

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


_WvRelayOperation_Type.__name__ = "Integer32"
_WvRelayOperation_Object = MibTableColumn
wvRelayOperation = _WvRelayOperation_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4, 1, 1, 2),
    _WvRelayOperation_Type()
)
wvRelayOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRelayOperation.setStatus("current")


class _WvRelayNormalState_Type(Integer32):
    """Custom type wvRelayNormalState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_WvRelayNormalState_Type.__name__ = "Integer32"
_WvRelayNormalState_Object = MibTableColumn
wvRelayNormalState = _WvRelayNormalState_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4, 1, 1, 3),
    _WvRelayNormalState_Type()
)
wvRelayNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRelayNormalState.setStatus("current")


class _WvRelayActivate_Type(Integer32):
    """Custom type wvRelayActivate based on Integer32"""
    defaultValue = 1

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


_WvRelayActivate_Type.__name__ = "Integer32"
_WvRelayActivate_Object = MibTableColumn
wvRelayActivate = _WvRelayActivate_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4, 1, 1, 4),
    _WvRelayActivate_Type()
)
wvRelayActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRelayActivate.setStatus("current")
_WvRelayToLocalAlarmMapping_Type = WvAlarmsList
_WvRelayToLocalAlarmMapping_Object = MibTableColumn
wvRelayToLocalAlarmMapping = _WvRelayToLocalAlarmMapping_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4, 1, 1, 5),
    _WvRelayToLocalAlarmMapping_Type()
)
wvRelayToLocalAlarmMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRelayToLocalAlarmMapping.setStatus("current")
_WvRelayToRemoteAlarmMapping_Type = WvAlarmsList
_WvRelayToRemoteAlarmMapping_Object = MibTableColumn
wvRelayToRemoteAlarmMapping = _WvRelayToRemoteAlarmMapping_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4, 1, 1, 6),
    _WvRelayToRemoteAlarmMapping_Type()
)
wvRelayToRemoteAlarmMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvRelayToRemoteAlarmMapping.setStatus("current")


class _WvRelayStatus_Type(Integer32):
    """Custom type wvRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_WvRelayStatus_Type.__name__ = "Integer32"
_WvRelayStatus_Object = MibTableColumn
wvRelayStatus = _WvRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 4, 1, 1, 7),
    _WvRelayStatus_Type()
)
wvRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvRelayStatus.setStatus("current")
_WvExternalInputs_ObjectIdentity = ObjectIdentity
wvExternalInputs = _WvExternalInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 5)
)
_WvExternalInputTable_Object = MibTable
wvExternalInputTable = _WvExternalInputTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wvExternalInputTable.setStatus("current")
_WvExternalInputEntry_Object = MibTableRow
wvExternalInputEntry = _WvExternalInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 5, 1, 1)
)
wvExternalInputEntry.setIndexNames(
    (0, "CODAN-MIB", "wvExternalInputId"),
)
if mibBuilder.loadTexts:
    wvExternalInputEntry.setStatus("current")


class _WvExternalInputId_Type(Integer32):
    """Custom type wvExternalInputId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WvExternalInputId_Type.__name__ = "Integer32"
_WvExternalInputId_Object = MibTableColumn
wvExternalInputId = _WvExternalInputId_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 5, 1, 1, 1),
    _WvExternalInputId_Type()
)
wvExternalInputId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvExternalInputId.setStatus("current")


class _WvExternalInputSetting_Type(Integer32):
    """Custom type wvExternalInputSetting based on Integer32"""
    defaultValue = 1

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


_WvExternalInputSetting_Type.__name__ = "Integer32"
_WvExternalInputSetting_Object = MibTableColumn
wvExternalInputSetting = _WvExternalInputSetting_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 5, 1, 1, 2),
    _WvExternalInputSetting_Type()
)
wvExternalInputSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvExternalInputSetting.setStatus("current")


class _WvExternalInputSense_Type(Integer32):
    """Custom type wvExternalInputSense based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anyChange", 3),
          ("high", 2),
          ("low", 1))
    )


_WvExternalInputSense_Type.__name__ = "Integer32"
_WvExternalInputSense_Object = MibTableColumn
wvExternalInputSense = _WvExternalInputSense_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 5, 1, 1, 3),
    _WvExternalInputSense_Type()
)
wvExternalInputSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvExternalInputSense.setStatus("current")


class _WvExternalInputAlarmSeverity_Type(Integer32):
    """Custom type wvExternalInputAlarmSeverity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("fatal", 3),
          ("warning", 1))
    )


_WvExternalInputAlarmSeverity_Type.__name__ = "Integer32"
_WvExternalInputAlarmSeverity_Object = MibTableColumn
wvExternalInputAlarmSeverity = _WvExternalInputAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 5, 1, 1, 4),
    _WvExternalInputAlarmSeverity_Type()
)
wvExternalInputAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvExternalInputAlarmSeverity.setStatus("current")


class _WvExternalInputStatus_Type(Integer32):
    """Custom type wvExternalInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_WvExternalInputStatus_Type.__name__ = "Integer32"
_WvExternalInputStatus_Object = MibTableColumn
wvExternalInputStatus = _WvExternalInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 5, 1, 1, 5),
    _WvExternalInputStatus_Type()
)
wvExternalInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvExternalInputStatus.setStatus("current")
_WvAlarmControl_ObjectIdentity = ObjectIdentity
wvAlarmControl = _WvAlarmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6)
)


class _WvAlarmsReportToNMSCtrl_Type(Integer32):
    """Custom type wvAlarmsReportToNMSCtrl based on Integer32"""
    defaultValue = 2

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
        *(("all", 1),
          ("errorAndFatal", 2),
          ("fatalOnly", 3),
          ("none", 4))
    )


_WvAlarmsReportToNMSCtrl_Type.__name__ = "Integer32"
_WvAlarmsReportToNMSCtrl_Object = MibScalar
wvAlarmsReportToNMSCtrl = _WvAlarmsReportToNMSCtrl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 1),
    _WvAlarmsReportToNMSCtrl_Type()
)
wvAlarmsReportToNMSCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAlarmsReportToNMSCtrl.setStatus("current")


class _WvAlarmsReportToLCDCtrl_Type(Integer32):
    """Custom type wvAlarmsReportToLCDCtrl based on Integer32"""
    defaultValue = 3

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
        *(("all", 1),
          ("errorAndFatal", 2),
          ("fatalOnly", 3),
          ("none", 4))
    )


_WvAlarmsReportToLCDCtrl_Type.__name__ = "Integer32"
_WvAlarmsReportToLCDCtrl_Object = MibScalar
wvAlarmsReportToLCDCtrl = _WvAlarmsReportToLCDCtrl_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 2),
    _WvAlarmsReportToLCDCtrl_Type()
)
wvAlarmsReportToLCDCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvAlarmsReportToLCDCtrl.setStatus("current")


class _WvNoOfAlertsOnLCD_Type(Integer32):
    """Custom type wvNoOfAlertsOnLCD based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_WvNoOfAlertsOnLCD_Type.__name__ = "Integer32"
_WvNoOfAlertsOnLCD_Object = MibScalar
wvNoOfAlertsOnLCD = _WvNoOfAlertsOnLCD_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 3),
    _WvNoOfAlertsOnLCD_Type()
)
wvNoOfAlertsOnLCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvNoOfAlertsOnLCD.setStatus("current")


class _WvLinkBERWarningThresholdHigh_Type(FloatingPoint):
    """Custom type wvLinkBERWarningThresholdHigh based on FloatingPoint"""
    defaultHexValue = "03e805"


_WvLinkBERWarningThresholdHigh_Object = MibScalar
wvLinkBERWarningThresholdHigh = _WvLinkBERWarningThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 4),
    _WvLinkBERWarningThresholdHigh_Type()
)
wvLinkBERWarningThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkBERWarningThresholdHigh.setStatus("current")


class _WvLinkBERWarningThresholdLow_Type(FloatingPoint):
    """Custom type wvLinkBERWarningThresholdLow based on FloatingPoint"""
    defaultHexValue = "03e806"


_WvLinkBERWarningThresholdLow_Object = MibScalar
wvLinkBERWarningThresholdLow = _WvLinkBERWarningThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 5),
    _WvLinkBERWarningThresholdLow_Type()
)
wvLinkBERWarningThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkBERWarningThresholdLow.setStatus("current")


class _WvLinkBERErrorThresholdHigh_Type(FloatingPoint):
    """Custom type wvLinkBERErrorThresholdHigh based on FloatingPoint"""
    defaultHexValue = "03e802"


_WvLinkBERErrorThresholdHigh_Object = MibScalar
wvLinkBERErrorThresholdHigh = _WvLinkBERErrorThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 6),
    _WvLinkBERErrorThresholdHigh_Type()
)
wvLinkBERErrorThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkBERErrorThresholdHigh.setStatus("current")


class _WvLinkBERErrorThresholdLow_Type(FloatingPoint):
    """Custom type wvLinkBERErrorThresholdLow based on FloatingPoint"""
    defaultHexValue = "03e803"


_WvLinkBERErrorThresholdLow_Object = MibScalar
wvLinkBERErrorThresholdLow = _WvLinkBERErrorThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 7),
    _WvLinkBERErrorThresholdLow_Type()
)
wvLinkBERErrorThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkBERErrorThresholdLow.setStatus("current")


class _WvLinkBLERAlarmThresholdHigh_Type(FloatingPoint):
    """Custom type wvLinkBLERAlarmThresholdHigh based on FloatingPoint"""
    defaultHexValue = "03e802"


_WvLinkBLERAlarmThresholdHigh_Object = MibScalar
wvLinkBLERAlarmThresholdHigh = _WvLinkBLERAlarmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 8),
    _WvLinkBLERAlarmThresholdHigh_Type()
)
wvLinkBLERAlarmThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkBLERAlarmThresholdHigh.setStatus("current")


class _WvLinkBLERAlarmThresholdLow_Type(FloatingPoint):
    """Custom type wvLinkBLERAlarmThresholdLow based on FloatingPoint"""
    defaultHexValue = "03e803"


_WvLinkBLERAlarmThresholdLow_Object = MibScalar
wvLinkBLERAlarmThresholdLow = _WvLinkBLERAlarmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 9),
    _WvLinkBLERAlarmThresholdLow_Type()
)
wvLinkBLERAlarmThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkBLERAlarmThresholdLow.setStatus("current")


class _WvLinkBBERAlarmThresholdHigh_Type(FloatingPoint):
    """Custom type wvLinkBBERAlarmThresholdHigh based on FloatingPoint"""
    defaultHexValue = "03e802"


_WvLinkBBERAlarmThresholdHigh_Object = MibScalar
wvLinkBBERAlarmThresholdHigh = _WvLinkBBERAlarmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 10),
    _WvLinkBBERAlarmThresholdHigh_Type()
)
wvLinkBBERAlarmThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkBBERAlarmThresholdHigh.setStatus("current")


class _WvLinkBBERAlarmThresholdLow_Type(FloatingPoint):
    """Custom type wvLinkBBERAlarmThresholdLow based on FloatingPoint"""
    defaultHexValue = "03e803"


_WvLinkBBERAlarmThresholdLow_Object = MibScalar
wvLinkBBERAlarmThresholdLow = _WvLinkBBERAlarmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 11),
    _WvLinkBBERAlarmThresholdLow_Type()
)
wvLinkBBERAlarmThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkBBERAlarmThresholdLow.setStatus("current")


class _WvLinkNCBLERAlarmThresholdHigh_Type(FloatingPoint):
    """Custom type wvLinkNCBLERAlarmThresholdHigh based on FloatingPoint"""
    defaultHexValue = "03e802"


_WvLinkNCBLERAlarmThresholdHigh_Object = MibScalar
wvLinkNCBLERAlarmThresholdHigh = _WvLinkNCBLERAlarmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 12),
    _WvLinkNCBLERAlarmThresholdHigh_Type()
)
wvLinkNCBLERAlarmThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkNCBLERAlarmThresholdHigh.setStatus("current")


class _WvLinkNCBLERAlarmThresholdLow_Type(FloatingPoint):
    """Custom type wvLinkNCBLERAlarmThresholdLow based on FloatingPoint"""
    defaultHexValue = "03e803"


_WvLinkNCBLERAlarmThresholdLow_Object = MibScalar
wvLinkNCBLERAlarmThresholdLow = _WvLinkNCBLERAlarmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 13),
    _WvLinkNCBLERAlarmThresholdLow_Type()
)
wvLinkNCBLERAlarmThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkNCBLERAlarmThresholdLow.setStatus("current")


class _WvLinkESAlarmThresholdHigh_Type(Integer32):
    """Custom type wvLinkESAlarmThresholdHigh based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WvLinkESAlarmThresholdHigh_Type.__name__ = "Integer32"
_WvLinkESAlarmThresholdHigh_Object = MibScalar
wvLinkESAlarmThresholdHigh = _WvLinkESAlarmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 14),
    _WvLinkESAlarmThresholdHigh_Type()
)
wvLinkESAlarmThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkESAlarmThresholdHigh.setStatus("current")


class _WvLinkESAlarmThresholdLow_Type(Integer32):
    """Custom type wvLinkESAlarmThresholdLow based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WvLinkESAlarmThresholdLow_Type.__name__ = "Integer32"
_WvLinkESAlarmThresholdLow_Object = MibScalar
wvLinkESAlarmThresholdLow = _WvLinkESAlarmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 15),
    _WvLinkESAlarmThresholdLow_Type()
)
wvLinkESAlarmThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkESAlarmThresholdLow.setStatus("current")


class _WvLinkSESAlarmThresholdHigh_Type(Integer32):
    """Custom type wvLinkSESAlarmThresholdHigh based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WvLinkSESAlarmThresholdHigh_Type.__name__ = "Integer32"
_WvLinkSESAlarmThresholdHigh_Object = MibScalar
wvLinkSESAlarmThresholdHigh = _WvLinkSESAlarmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 16),
    _WvLinkSESAlarmThresholdHigh_Type()
)
wvLinkSESAlarmThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkSESAlarmThresholdHigh.setStatus("current")


class _WvLinkSESAlarmThresholdLow_Type(Integer32):
    """Custom type wvLinkSESAlarmThresholdLow based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WvLinkSESAlarmThresholdLow_Type.__name__ = "Integer32"
_WvLinkSESAlarmThresholdLow_Object = MibScalar
wvLinkSESAlarmThresholdLow = _WvLinkSESAlarmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 17),
    _WvLinkSESAlarmThresholdLow_Type()
)
wvLinkSESAlarmThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkSESAlarmThresholdLow.setStatus("current")


class _WvLinkDMAlarmThresholdHigh_Type(Integer32):
    """Custom type wvLinkDMAlarmThresholdHigh based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WvLinkDMAlarmThresholdHigh_Type.__name__ = "Integer32"
_WvLinkDMAlarmThresholdHigh_Object = MibScalar
wvLinkDMAlarmThresholdHigh = _WvLinkDMAlarmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 18),
    _WvLinkDMAlarmThresholdHigh_Type()
)
wvLinkDMAlarmThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkDMAlarmThresholdHigh.setStatus("current")


class _WvLinkDMAlarmThresholdLow_Type(Integer32):
    """Custom type wvLinkDMAlarmThresholdLow based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WvLinkDMAlarmThresholdLow_Type.__name__ = "Integer32"
_WvLinkDMAlarmThresholdLow_Object = MibScalar
wvLinkDMAlarmThresholdLow = _WvLinkDMAlarmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 19),
    _WvLinkDMAlarmThresholdLow_Type()
)
wvLinkDMAlarmThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkDMAlarmThresholdLow.setStatus("current")


class _WvLinkUASAlarmThresholdHigh_Type(Integer32):
    """Custom type wvLinkUASAlarmThresholdHigh based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WvLinkUASAlarmThresholdHigh_Type.__name__ = "Integer32"
_WvLinkUASAlarmThresholdHigh_Object = MibScalar
wvLinkUASAlarmThresholdHigh = _WvLinkUASAlarmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 20),
    _WvLinkUASAlarmThresholdHigh_Type()
)
wvLinkUASAlarmThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkUASAlarmThresholdHigh.setStatus("current")


class _WvLinkUASAlarmThresholdLow_Type(Integer32):
    """Custom type wvLinkUASAlarmThresholdLow based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WvLinkUASAlarmThresholdLow_Type.__name__ = "Integer32"
_WvLinkUASAlarmThresholdLow_Object = MibScalar
wvLinkUASAlarmThresholdLow = _WvLinkUASAlarmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 21),
    _WvLinkUASAlarmThresholdLow_Type()
)
wvLinkUASAlarmThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkUASAlarmThresholdLow.setStatus("current")


class _WvlinkRSLLowAlarmThresholdhHigh_Type(Integer32):
    """Custom type wvlinkRSLLowAlarmThresholdhHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -10),
    )


_WvlinkRSLLowAlarmThresholdhHigh_Type.__name__ = "Integer32"
_WvlinkRSLLowAlarmThresholdhHigh_Object = MibScalar
wvlinkRSLLowAlarmThresholdhHigh = _WvlinkRSLLowAlarmThresholdhHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 22),
    _WvlinkRSLLowAlarmThresholdhHigh_Type()
)
wvlinkRSLLowAlarmThresholdhHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvlinkRSLLowAlarmThresholdhHigh.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkRSLLowAlarmThresholdhHigh.setUnits("dBm")


class _WvlinkRSLLowAlarmThresholdhLow_Type(Integer32):
    """Custom type wvlinkRSLLowAlarmThresholdhLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -10),
    )


_WvlinkRSLLowAlarmThresholdhLow_Type.__name__ = "Integer32"
_WvlinkRSLLowAlarmThresholdhLow_Object = MibScalar
wvlinkRSLLowAlarmThresholdhLow = _WvlinkRSLLowAlarmThresholdhLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 23),
    _WvlinkRSLLowAlarmThresholdhLow_Type()
)
wvlinkRSLLowAlarmThresholdhLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvlinkRSLLowAlarmThresholdhLow.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkRSLLowAlarmThresholdhLow.setUnits("dBm")


class _WvlinkAverageRSLLowAlarmThresholdhHigh_Type(Integer32):
    """Custom type wvlinkAverageRSLLowAlarmThresholdhHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -10),
    )


_WvlinkAverageRSLLowAlarmThresholdhHigh_Type.__name__ = "Integer32"
_WvlinkAverageRSLLowAlarmThresholdhHigh_Object = MibScalar
wvlinkAverageRSLLowAlarmThresholdhHigh = _WvlinkAverageRSLLowAlarmThresholdhHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 24),
    _WvlinkAverageRSLLowAlarmThresholdhHigh_Type()
)
wvlinkAverageRSLLowAlarmThresholdhHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvlinkAverageRSLLowAlarmThresholdhHigh.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkAverageRSLLowAlarmThresholdhHigh.setUnits("dBm")


class _WvlinkAverageRSLLowAlarmThresholdhLow_Type(Integer32):
    """Custom type wvlinkAverageRSLLowAlarmThresholdhLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -10),
    )


_WvlinkAverageRSLLowAlarmThresholdhLow_Type.__name__ = "Integer32"
_WvlinkAverageRSLLowAlarmThresholdhLow_Object = MibScalar
wvlinkAverageRSLLowAlarmThresholdhLow = _WvlinkAverageRSLLowAlarmThresholdhLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 25),
    _WvlinkAverageRSLLowAlarmThresholdhLow_Type()
)
wvlinkAverageRSLLowAlarmThresholdhLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvlinkAverageRSLLowAlarmThresholdhLow.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkAverageRSLLowAlarmThresholdhLow.setUnits("dBm")


class _WvLinkThresholdMeasurementInterval_Type(Integer32):
    """Custom type wvLinkThresholdMeasurementInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_WvLinkThresholdMeasurementInterval_Type.__name__ = "Integer32"
_WvLinkThresholdMeasurementInterval_Object = MibScalar
wvLinkThresholdMeasurementInterval = _WvLinkThresholdMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 26),
    _WvLinkThresholdMeasurementInterval_Type()
)
wvLinkThresholdMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLinkThresholdMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    wvLinkThresholdMeasurementInterval.setUnits("seconds")


class _WvEth10_100CSLAlarmThresholdhHigh_Type(Integer32):
    """Custom type wvEth10_100CSLAlarmThresholdhHigh based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100CSLAlarmThresholdhHigh_Type.__name__ = "Integer32"
_WvEth10_100CSLAlarmThresholdhHigh_Object = MibScalar
wvEth10_100CSLAlarmThresholdhHigh = _WvEth10_100CSLAlarmThresholdhHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 50),
    _WvEth10_100CSLAlarmThresholdhHigh_Type()
)
wvEth10_100CSLAlarmThresholdhHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100CSLAlarmThresholdhHigh.setStatus("current")


class _WvEth10_100CSLAlarmThresholdhLow_Type(Integer32):
    """Custom type wvEth10_100CSLAlarmThresholdhLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100CSLAlarmThresholdhLow_Type.__name__ = "Integer32"
_WvEth10_100CSLAlarmThresholdhLow_Object = MibScalar
wvEth10_100CSLAlarmThresholdhLow = _WvEth10_100CSLAlarmThresholdhLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 51),
    _WvEth10_100CSLAlarmThresholdhLow_Type()
)
wvEth10_100CSLAlarmThresholdhLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100CSLAlarmThresholdhLow.setStatus("current")


class _WvEth10_100ECAlarmThresholdhHigh_Type(Integer32):
    """Custom type wvEth10_100ECAlarmThresholdhHigh based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100ECAlarmThresholdhHigh_Type.__name__ = "Integer32"
_WvEth10_100ECAlarmThresholdhHigh_Object = MibScalar
wvEth10_100ECAlarmThresholdhHigh = _WvEth10_100ECAlarmThresholdhHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 52),
    _WvEth10_100ECAlarmThresholdhHigh_Type()
)
wvEth10_100ECAlarmThresholdhHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100ECAlarmThresholdhHigh.setStatus("current")


class _WvEth10_100ECAlarmThresholdhLow_Type(Integer32):
    """Custom type wvEth10_100ECAlarmThresholdhLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100ECAlarmThresholdhLow_Type.__name__ = "Integer32"
_WvEth10_100ECAlarmThresholdhLow_Object = MibScalar
wvEth10_100ECAlarmThresholdhLow = _WvEth10_100ECAlarmThresholdhLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 53),
    _WvEth10_100ECAlarmThresholdhLow_Type()
)
wvEth10_100ECAlarmThresholdhLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100ECAlarmThresholdhLow.setStatus("current")


class _WvEth10_100IMTEAlarmThresholdhHigh_Type(Integer32):
    """Custom type wvEth10_100IMTEAlarmThresholdhHigh based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100IMTEAlarmThresholdhHigh_Type.__name__ = "Integer32"
_WvEth10_100IMTEAlarmThresholdhHigh_Object = MibScalar
wvEth10_100IMTEAlarmThresholdhHigh = _WvEth10_100IMTEAlarmThresholdhHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 54),
    _WvEth10_100IMTEAlarmThresholdhHigh_Type()
)
wvEth10_100IMTEAlarmThresholdhHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100IMTEAlarmThresholdhHigh.setStatus("current")


class _WvEth10_100IMTEAlarmThresholdhLow_Type(Integer32):
    """Custom type wvEth10_100IMTEAlarmThresholdhLow based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100IMTEAlarmThresholdhLow_Type.__name__ = "Integer32"
_WvEth10_100IMTEAlarmThresholdhLow_Object = MibScalar
wvEth10_100IMTEAlarmThresholdhLow = _WvEth10_100IMTEAlarmThresholdhLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 55),
    _WvEth10_100IMTEAlarmThresholdhLow_Type()
)
wvEth10_100IMTEAlarmThresholdhLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100IMTEAlarmThresholdhLow.setStatus("current")


class _WvEth10_100IMREAlarmThresholdhHigh_Type(Integer32):
    """Custom type wvEth10_100IMREAlarmThresholdhHigh based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100IMREAlarmThresholdhHigh_Type.__name__ = "Integer32"
_WvEth10_100IMREAlarmThresholdhHigh_Object = MibScalar
wvEth10_100IMREAlarmThresholdhHigh = _WvEth10_100IMREAlarmThresholdhHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 56),
    _WvEth10_100IMREAlarmThresholdhHigh_Type()
)
wvEth10_100IMREAlarmThresholdhHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100IMREAlarmThresholdhHigh.setStatus("current")


class _WvEth10_100IMREAlarmThresholdhLow_Type(Integer32):
    """Custom type wvEth10_100IMREAlarmThresholdhLow based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100IMREAlarmThresholdhLow_Type.__name__ = "Integer32"
_WvEth10_100IMREAlarmThresholdhLow_Object = MibScalar
wvEth10_100IMREAlarmThresholdhLow = _WvEth10_100IMREAlarmThresholdhLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 57),
    _WvEth10_100IMREAlarmThresholdhLow_Type()
)
wvEth10_100IMREAlarmThresholdhLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100IMREAlarmThresholdhLow.setStatus("current")


class _WvEth10_100TxLinkUsageAlarmThresholdLow_Type(Integer32):
    """Custom type wvEth10_100TxLinkUsageAlarmThresholdLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100TxLinkUsageAlarmThresholdLow_Type.__name__ = "Integer32"
_WvEth10_100TxLinkUsageAlarmThresholdLow_Object = MibScalar
wvEth10_100TxLinkUsageAlarmThresholdLow = _WvEth10_100TxLinkUsageAlarmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 58),
    _WvEth10_100TxLinkUsageAlarmThresholdLow_Type()
)
wvEth10_100TxLinkUsageAlarmThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100TxLinkUsageAlarmThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100TxLinkUsageAlarmThresholdLow.setUnits("MBits/sec")


class _WvEth10_100TxLinkUsageAlarmThresholdHigh_Type(Integer32):
    """Custom type wvEth10_100TxLinkUsageAlarmThresholdHigh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100TxLinkUsageAlarmThresholdHigh_Type.__name__ = "Integer32"
_WvEth10_100TxLinkUsageAlarmThresholdHigh_Object = MibScalar
wvEth10_100TxLinkUsageAlarmThresholdHigh = _WvEth10_100TxLinkUsageAlarmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 59),
    _WvEth10_100TxLinkUsageAlarmThresholdHigh_Type()
)
wvEth10_100TxLinkUsageAlarmThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100TxLinkUsageAlarmThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100TxLinkUsageAlarmThresholdHigh.setUnits("MBits/sec")


class _WvEth10_100RxLinkUsageAlarmThresholdLow_Type(Integer32):
    """Custom type wvEth10_100RxLinkUsageAlarmThresholdLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100RxLinkUsageAlarmThresholdLow_Type.__name__ = "Integer32"
_WvEth10_100RxLinkUsageAlarmThresholdLow_Object = MibScalar
wvEth10_100RxLinkUsageAlarmThresholdLow = _WvEth10_100RxLinkUsageAlarmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 60),
    _WvEth10_100RxLinkUsageAlarmThresholdLow_Type()
)
wvEth10_100RxLinkUsageAlarmThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100RxLinkUsageAlarmThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100RxLinkUsageAlarmThresholdLow.setUnits("MBits/sec")


class _WvEth10_100RxLinkUsageAlarmThresholdHigh_Type(Integer32):
    """Custom type wvEth10_100RxLinkUsageAlarmThresholdHigh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_WvEth10_100RxLinkUsageAlarmThresholdHigh_Type.__name__ = "Integer32"
_WvEth10_100RxLinkUsageAlarmThresholdHigh_Object = MibScalar
wvEth10_100RxLinkUsageAlarmThresholdHigh = _WvEth10_100RxLinkUsageAlarmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 61),
    _WvEth10_100RxLinkUsageAlarmThresholdHigh_Type()
)
wvEth10_100RxLinkUsageAlarmThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100RxLinkUsageAlarmThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100RxLinkUsageAlarmThresholdHigh.setUnits("MBits/sec")


class _WvEth10_100ThresholdMeasurementInterval_Type(Integer32):
    """Custom type wvEth10_100ThresholdMeasurementInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_WvEth10_100ThresholdMeasurementInterval_Type.__name__ = "Integer32"
_WvEth10_100ThresholdMeasurementInterval_Object = MibScalar
wvEth10_100ThresholdMeasurementInterval = _WvEth10_100ThresholdMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 70),
    _WvEth10_100ThresholdMeasurementInterval_Type()
)
wvEth10_100ThresholdMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvEth10_100ThresholdMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100ThresholdMeasurementInterval.setUnits("seconds")
_WvClearAlarmLog_Type = Integer32
_WvClearAlarmLog_Object = MibScalar
wvClearAlarmLog = _WvClearAlarmLog_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 6, 71),
    _WvClearAlarmLog_Type()
)
wvClearAlarmLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvClearAlarmLog.setStatus("current")
_WvComponentsRevisions_ObjectIdentity = ObjectIdentity
wvComponentsRevisions = _WvComponentsRevisions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7)
)


class _WvInstalledPlugInPartNo_Type(DisplayString):
    """Custom type wvInstalledPlugInPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WvInstalledPlugInPartNo_Type.__name__ = "DisplayString"
_WvInstalledPlugInPartNo_Object = MibScalar
wvInstalledPlugInPartNo = _WvInstalledPlugInPartNo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 1),
    _WvInstalledPlugInPartNo_Type()
)
wvInstalledPlugInPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvInstalledPlugInPartNo.setStatus("current")
_WvInstalledPlugInHwRevision_Type = ComponentRevision
_WvInstalledPlugInHwRevision_Object = MibScalar
wvInstalledPlugInHwRevision = _WvInstalledPlugInHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 2),
    _WvInstalledPlugInHwRevision_Type()
)
wvInstalledPlugInHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvInstalledPlugInHwRevision.setStatus("current")


class _WvIduPartNo_Type(DisplayString):
    """Custom type wvIduPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WvIduPartNo_Type.__name__ = "DisplayString"
_WvIduPartNo_Object = MibScalar
wvIduPartNo = _WvIduPartNo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 3),
    _WvIduPartNo_Type()
)
wvIduPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvIduPartNo.setStatus("current")
_WvIduHwRevision_Type = ComponentRevision
_WvIduHwRevision_Object = MibScalar
wvIduHwRevision = _WvIduHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 4),
    _WvIduHwRevision_Type()
)
wvIduHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvIduHwRevision.setStatus("current")
_WvIduSwRevision_Type = ComponentRevision
_WvIduSwRevision_Object = MibScalar
wvIduSwRevision = _WvIduSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 5),
    _WvIduSwRevision_Type()
)
wvIduSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvIduSwRevision.setStatus("current")
_WvIduLastSwUpdateTime_Type = DateAndTime
_WvIduLastSwUpdateTime_Object = MibScalar
wvIduLastSwUpdateTime = _WvIduLastSwUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 6),
    _WvIduLastSwUpdateTime_Type()
)
wvIduLastSwUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvIduLastSwUpdateTime.setStatus("current")


class _WvOduPartNo_Type(DisplayString):
    """Custom type wvOduPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_WvOduPartNo_Type.__name__ = "DisplayString"
_WvOduPartNo_Object = MibScalar
wvOduPartNo = _WvOduPartNo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 7),
    _WvOduPartNo_Type()
)
wvOduPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOduPartNo.setStatus("current")
_WvOduHwRevision_Type = ComponentRevision
_WvOduHwRevision_Object = MibScalar
wvOduHwRevision = _WvOduHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 8),
    _WvOduHwRevision_Type()
)
wvOduHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOduHwRevision.setStatus("current")
_WvOduSwRevision_Type = ComponentRevision
_WvOduSwRevision_Object = MibScalar
wvOduSwRevision = _WvOduSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 9),
    _WvOduSwRevision_Type()
)
wvOduSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOduSwRevision.setStatus("current")
_WvOduLastSwUpdateTime_Type = DateAndTime
_WvOduLastSwUpdateTime_Object = MibScalar
wvOduLastSwUpdateTime = _WvOduLastSwUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 10),
    _WvOduLastSwUpdateTime_Type()
)
wvOduLastSwUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOduLastSwUpdateTime.setStatus("current")
_WvIpbHwRevision_Type = ComponentRevision
_WvIpbHwRevision_Object = MibScalar
wvIpbHwRevision = _WvIpbHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 11),
    _WvIpbHwRevision_Type()
)
wvIpbHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvIpbHwRevision.setStatus("current")
_WvBootSwRevision_Type = ComponentRevision
_WvBootSwRevision_Object = MibScalar
wvBootSwRevision = _WvBootSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 12),
    _WvBootSwRevision_Type()
)
wvBootSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvBootSwRevision.setStatus("current")
_WvIduAlternetSwRevision_Type = ComponentRevision
_WvIduAlternetSwRevision_Object = MibScalar
wvIduAlternetSwRevision = _WvIduAlternetSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 13),
    _WvIduAlternetSwRevision_Type()
)
wvIduAlternetSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvIduAlternetSwRevision.setStatus("current")


class _WvOemId_Type(Integer32):
    """Custom type wvOemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WvOemId_Type.__name__ = "Integer32"
_WvOemId_Object = MibScalar
wvOemId = _WvOemId_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 14),
    _WvOemId_Type()
)
wvOemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOemId.setStatus("current")


class _WvOemIduPartNo_Type(DisplayString):
    """Custom type wvOemIduPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_WvOemIduPartNo_Type.__name__ = "DisplayString"
_WvOemIduPartNo_Object = MibScalar
wvOemIduPartNo = _WvOemIduPartNo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 15),
    _WvOemIduPartNo_Type()
)
wvOemIduPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOemIduPartNo.setStatus("current")


class _WvOemOduPartNo_Type(DisplayString):
    """Custom type wvOemOduPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_WvOemOduPartNo_Type.__name__ = "DisplayString"
_WvOemOduPartNo_Object = MibScalar
wvOemOduPartNo = _WvOemOduPartNo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 16),
    _WvOemOduPartNo_Type()
)
wvOemOduPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOemOduPartNo.setStatus("current")


class _WvInstalledOemPlugInPartNo_Type(DisplayString):
    """Custom type wvInstalledOemPlugInPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_WvInstalledOemPlugInPartNo_Type.__name__ = "DisplayString"
_WvInstalledOemPlugInPartNo_Object = MibScalar
wvInstalledOemPlugInPartNo = _WvInstalledOemPlugInPartNo_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 1, 7, 17),
    _WvInstalledOemPlugInPartNo_Type()
)
wvInstalledOemPlugInPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvInstalledOemPlugInPartNo.setStatus("current")
_WvStatusAndGauges_ObjectIdentity = ObjectIdentity
wvStatusAndGauges = _WvStatusAndGauges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2)
)


class _WvTelemetryStatus_Type(Integer32):
    """Custom type wvTelemetryStatus based on Integer32"""
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
        *(("fault", 3),
          ("notOperational", 4),
          ("ok", 1),
          ("warning", 2))
    )


_WvTelemetryStatus_Type.__name__ = "Integer32"
_WvTelemetryStatus_Object = MibScalar
wvTelemetryStatus = _WvTelemetryStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 1),
    _WvTelemetryStatus_Type()
)
wvTelemetryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvTelemetryStatus.setStatus("current")


class _WvOperatingSystemStatus_Type(Integer32):
    """Custom type wvOperatingSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("systemFailure", 2))
    )


_WvOperatingSystemStatus_Type.__name__ = "Integer32"
_WvOperatingSystemStatus_Object = MibScalar
wvOperatingSystemStatus = _WvOperatingSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 2),
    _WvOperatingSystemStatus_Type()
)
wvOperatingSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOperatingSystemStatus.setStatus("current")


class _WvIduOduCableStatus_Type(Integer32):
    """Custom type wvIduOduCableStatus based on Integer32"""
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
        *(("ok", 1),
          ("open", 4),
          ("short", 3),
          ("warning", 2))
    )


_WvIduOduCableStatus_Type.__name__ = "Integer32"
_WvIduOduCableStatus_Object = MibScalar
wvIduOduCableStatus = _WvIduOduCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 3),
    _WvIduOduCableStatus_Type()
)
wvIduOduCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvIduOduCableStatus.setStatus("current")


class _WvIduStatus_Type(Bits):
    """Custom type wvIduStatus based on Bits"""
    namedValues = NamedValues(
        *(("externalInputsActive", 4),
          ("filler0", 0),
          ("iduNotOperational", 6),
          ("iduPowerSupplyLowValue", 1),
          ("iduRxSynthesizerOutOfLock", 3),
          ("iduTxSynthesizerOutOfLock", 2),
          ("selfTestFault", 5))
    )

_WvIduStatus_Type.__name__ = "Bits"
_WvIduStatus_Object = MibScalar
wvIduStatus = _WvIduStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 4),
    _WvIduStatus_Type()
)
wvIduStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvIduStatus.setStatus("current")


class _WvOduStatus_Type(Bits):
    """Custom type wvOduStatus based on Bits"""
    namedValues = NamedValues(
        *(("anyOtherOduFault", 12),
          ("averageRSLLow", 7),
          ("filler0", 0),
          ("oduNotResponding", 13),
          ("oduPowerSupplyOutOfRange", 1),
          ("oduRfSynthesizerOutOfLock", 10),
          ("oduRxSynthesizerOutOfLock", 9),
          ("oduTemperatureViolation", 11),
          ("oduTxSynthesizerOutOfLock", 8),
          ("rslLow", 6),
          ("rxFailure", 5),
          ("rxOnMuteState", 3),
          ("txFailure", 4),
          ("txOnMuteState", 2))
    )

_WvOduStatus_Type.__name__ = "Bits"
_WvOduStatus_Object = MibScalar
wvOduStatus = _WvOduStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 5),
    _WvOduStatus_Type()
)
wvOduStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOduStatus.setStatus("current")


class _WvRemoteTerminalStatus_Type(Bits):
    """Custom type wvRemoteTerminalStatus based on Bits"""
    namedValues = NamedValues(
        *(("remoteTerminalFailure", 1),
          ("remoteTerminalNotResponding", 2),
          ("remoteTerminalWarning", 0))
    )

_WvRemoteTerminalStatus_Type.__name__ = "Bits"
_WvRemoteTerminalStatus_Object = MibScalar
wvRemoteTerminalStatus = _WvRemoteTerminalStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 6),
    _WvRemoteTerminalStatus_Type()
)
wvRemoteTerminalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvRemoteTerminalStatus.setStatus("current")


class _WvSlipModemStatus_Type(Integer32):
    """Custom type wvSlipModemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("anyOtherFault", 6),
          ("connected", 5),
          ("lineBusy", 4),
          ("noAnswer", 7),
          ("noDialTone", 3),
          ("notResponding", 2),
          ("ok", 1))
    )


_WvSlipModemStatus_Type.__name__ = "Integer32"
_WvSlipModemStatus_Object = MibScalar
wvSlipModemStatus = _WvSlipModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 7),
    _WvSlipModemStatus_Type()
)
wvSlipModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSlipModemStatus.setStatus("current")


class _WvSecurityStatus_Type(Bits):
    """Custom type wvSecurityStatus based on Bits"""
    namedValues = NamedValues(
        *(("filler0", 0),
          ("linkIdViolation", 1),
          ("passwordBypass", 2))
    )

_WvSecurityStatus_Type.__name__ = "Bits"
_WvSecurityStatus_Object = MibScalar
wvSecurityStatus = _WvSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 8),
    _WvSecurityStatus_Type()
)
wvSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSecurityStatus.setStatus("current")


class _WvTftpDwnlStatus_Type(Integer32):
    """Custom type wvTftpDwnlStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("dwnlCancelByUser", 11),
          ("dwnlChecksumError", 6),
          ("dwnlConfigIncompatibleImage", 8),
          ("dwnlGeneralError", 4),
          ("dwnlInProcess", 2),
          ("dwnlNoResponseFromServer", 5),
          ("dwnlStatusUnknown", 1),
          ("dwnlSuccess", 3),
          ("dwnlSwIncompatibleImage", 7),
          ("dwnlTftpFilePasswordError", 10),
          ("dwnlTftpProtocolError", 9))
    )


_WvTftpDwnlStatus_Type.__name__ = "Integer32"
_WvTftpDwnlStatus_Object = MibScalar
wvTftpDwnlStatus = _WvTftpDwnlStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 9),
    _WvTftpDwnlStatus_Type()
)
wvTftpDwnlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvTftpDwnlStatus.setStatus("current")


class _WvLinkPerformanceAlarmsStatus_Type(Bits):
    """Custom type wvLinkPerformanceAlarmsStatus based on Bits"""
    namedValues = NamedValues(
        *(("eth10-100RxLinkUsageHigh", 11),
          ("eth10-100RxLinkUsageLow", 10),
          ("eth10-100TxLinkUsageHigh", 13),
          ("eth10-100TxLinkUsageLow", 12),
          ("filler0", 0),
          ("wvLinkBBERAlarm", 8),
          ("wvLinkBERFailureAlarm", 6),
          ("wvLinkBERWarningAlarm", 5),
          ("wvLinkBLERAlarm", 7),
          ("wvLinkDMAlarm", 4),
          ("wvLinkESAlarm", 1),
          ("wvLinkNCBLERAlarm", 9),
          ("wvLinkSESAlarm", 2),
          ("wvLinkUASAlarm", 3))
    )

_WvLinkPerformanceAlarmsStatus_Type.__name__ = "Bits"
_WvLinkPerformanceAlarmsStatus_Object = MibScalar
wvLinkPerformanceAlarmsStatus = _WvLinkPerformanceAlarmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 10),
    _WvLinkPerformanceAlarmsStatus_Type()
)
wvLinkPerformanceAlarmsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkPerformanceAlarmsStatus.setStatus("current")
_WvOperatingFrequency_Type = Integer32
_WvOperatingFrequency_Object = MibScalar
wvOperatingFrequency = _WvOperatingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 11),
    _WvOperatingFrequency_Type()
)
wvOperatingFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOperatingFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wvOperatingFrequency.setUnits("MHz*100")


class _WvFrequencyBand_Type(Integer32):
    """Custom type wvFrequencyBand based on Integer32"""
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
        *(("bandFour", 4),
          ("bandOne", 1),
          ("bandThree", 3),
          ("bandTwo", 2))
    )


_WvFrequencyBand_Type.__name__ = "Integer32"
_WvFrequencyBand_Object = MibScalar
wvFrequencyBand = _WvFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 12),
    _WvFrequencyBand_Type()
)
wvFrequencyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvFrequencyBand.setStatus("current")


class _WvChannelSpacing_Type(Integer32):
    """Custom type wvChannelSpacing based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("fifty", 6),
          ("fiftySix", 11),
          ("five", 2),
          ("fourteen", 9),
          ("seven", 8),
          ("sevenAndAHalf", 3),
          ("threeAndAHalf", 7),
          ("twelveAndAHalf", 4),
          ("twentyEight", 10),
          ("twentyFive", 5),
          ("twoAndAHalf", 1))
    )


_WvChannelSpacing_Type.__name__ = "Integer32"
_WvChannelSpacing_Object = MibScalar
wvChannelSpacing = _WvChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 13),
    _WvChannelSpacing_Type()
)
wvChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvChannelSpacing.setStatus("current")
if mibBuilder.loadTexts:
    wvChannelSpacing.setUnits("MHz")


class _WvTxPowerLevel_Type(Integer32):
    """Custom type wvTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, 30),
    )


_WvTxPowerLevel_Type.__name__ = "Integer32"
_WvTxPowerLevel_Object = MibScalar
wvTxPowerLevel = _WvTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 14),
    _WvTxPowerLevel_Type()
)
wvTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    wvTxPowerLevel.setUnits("dBm")


class _WvRxSignalLevel_Type(Integer32):
    """Custom type wvRxSignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -10),
    )


_WvRxSignalLevel_Type.__name__ = "Integer32"
_WvRxSignalLevel_Object = MibScalar
wvRxSignalLevel = _WvRxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 15),
    _WvRxSignalLevel_Type()
)
wvRxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvRxSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    wvRxSignalLevel.setUnits("dBm")


class _WvFadeMargin_Type(Integer32):
    """Custom type wvFadeMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_WvFadeMargin_Type.__name__ = "Integer32"
_WvFadeMargin_Object = MibScalar
wvFadeMargin = _WvFadeMargin_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 16),
    _WvFadeMargin_Type()
)
wvFadeMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvFadeMargin.setStatus("current")
if mibBuilder.loadTexts:
    wvFadeMargin.setUnits("dB")


class _WvOduTemperature_Type(Integer32):
    """Custom type wvOduTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_WvOduTemperature_Type.__name__ = "Integer32"
_WvOduTemperature_Object = MibScalar
wvOduTemperature = _WvOduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 17),
    _WvOduTemperature_Type()
)
wvOduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOduTemperature.setStatus("current")


class _WvLedState_Type(Bits):
    """Custom type wvLedState based on Bits"""
    namedValues = NamedValues(
        *(("filler0", 0),
          ("linkOperational", 2),
          ("localCableFault", 8),
          ("localFrontPanelDisplay", 14),
          ("localIduFault", 10),
          ("localOduFault", 12),
          ("powerOn", 1),
          ("relay1On", 3),
          ("relay2On", 4),
          ("relay3On", 5),
          ("relay4On", 6),
          ("relay5On", 7),
          ("remoteCableFault", 9),
          ("remoteFrontPanelDisplay", 15),
          ("remoteIduFault", 11),
          ("remoteOduFault", 13))
    )

_WvLedState_Type.__name__ = "Bits"
_WvLedState_Object = MibScalar
wvLedState = _WvLedState_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 18),
    _WvLedState_Type()
)
wvLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLedState.setStatus("current")


class _WvModemAfc_Type(Integer32):
    """Custom type wvModemAfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_WvModemAfc_Type.__name__ = "Integer32"
_WvModemAfc_Object = MibScalar
wvModemAfc = _WvModemAfc_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 19),
    _WvModemAfc_Type()
)
wvModemAfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvModemAfc.setStatus("current")
_WvRxPllFrequency_Type = Integer32
_WvRxPllFrequency_Object = MibScalar
wvRxPllFrequency = _WvRxPllFrequency_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 20),
    _WvRxPllFrequency_Type()
)
wvRxPllFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvRxPllFrequency.setStatus("current")
_WvWorkingFrequency_Type = Integer32
_WvWorkingFrequency_Object = MibScalar
wvWorkingFrequency = _WvWorkingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 21),
    _WvWorkingFrequency_Type()
)
wvWorkingFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvWorkingFrequency.setStatus("current")
if mibBuilder.loadTexts:
    wvWorkingFrequency.setUnits("MHz*100")


class _WvMaxTxPowerSetting_Type(Integer32):
    """Custom type wvMaxTxPowerSetting based on Integer32"""
    defaultValue = 29

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 29),
    )


_WvMaxTxPowerSetting_Type.__name__ = "Integer32"
_WvMaxTxPowerSetting_Object = MibScalar
wvMaxTxPowerSetting = _WvMaxTxPowerSetting_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 22),
    _WvMaxTxPowerSetting_Type()
)
wvMaxTxPowerSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvMaxTxPowerSetting.setStatus("current")
if mibBuilder.loadTexts:
    wvMaxTxPowerSetting.setUnits("dBm")


class _WvMinTxPowerSetting_Type(Integer32):
    """Custom type wvMinTxPowerSetting based on Integer32"""
    defaultValue = -10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 29),
    )


_WvMinTxPowerSetting_Type.__name__ = "Integer32"
_WvMinTxPowerSetting_Object = MibScalar
wvMinTxPowerSetting = _WvMinTxPowerSetting_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 23),
    _WvMinTxPowerSetting_Type()
)
wvMinTxPowerSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvMinTxPowerSetting.setStatus("current")
if mibBuilder.loadTexts:
    wvMinTxPowerSetting.setUnits("dBm")
_WvOduSerialNumber_Type = Integer32
_WvOduSerialNumber_Object = MibScalar
wvOduSerialNumber = _WvOduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 24),
    _WvOduSerialNumber_Type()
)
wvOduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOduSerialNumber.setStatus("current")
_WvIduSerialNumber_Type = Integer32
_WvIduSerialNumber_Object = MibScalar
wvIduSerialNumber = _WvIduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 25),
    _WvIduSerialNumber_Type()
)
wvIduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvIduSerialNumber.setStatus("current")


class _WvOnePlusOneStatus_Type(Bits):
    """Custom type wvOnePlusOneStatus based on Bits"""
    namedValues = NamedValues(
        *(("alternateIduOk", 4),
          ("filler0", 0),
          ("frequencyDiversityOn", 6),
          ("manualModeOn", 3),
          ("onePlusOneOn", 1),
          ("primaryUnit", 2),
          ("swIduFail", 7),
          ("unitActive", 5),
          ("upperUnit", 8))
    )

_WvOnePlusOneStatus_Type.__name__ = "Bits"
_WvOnePlusOneStatus_Object = MibScalar
wvOnePlusOneStatus = _WvOnePlusOneStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 30),
    _WvOnePlusOneStatus_Type()
)
wvOnePlusOneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOnePlusOneStatus.setStatus("current")


class _WvSupport2T1and2E1Status_Type(Integer32):
    """Custom type wvSupport2T1and2E1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("support2T1and2E1Disable", 1),
          ("support2T1and2E1Enable", 0))
    )


_WvSupport2T1and2E1Status_Type.__name__ = "Integer32"
_WvSupport2T1and2E1Status_Object = MibScalar
wvSupport2T1and2E1Status = _WvSupport2T1and2E1Status_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 31),
    _WvSupport2T1and2E1Status_Type()
)
wvSupport2T1and2E1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSupport2T1and2E1Status.setStatus("current")
_WvLastUpdateConfigurationTimestamp_Type = Integer32
_WvLastUpdateConfigurationTimestamp_Object = MibScalar
wvLastUpdateConfigurationTimestamp = _WvLastUpdateConfigurationTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 32),
    _WvLastUpdateConfigurationTimestamp_Type()
)
wvLastUpdateConfigurationTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLastUpdateConfigurationTimestamp.setStatus("current")


class _WvOemIduSerialNumber_Type(DisplayString):
    """Custom type wvOemIduSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_WvOemIduSerialNumber_Type.__name__ = "DisplayString"
_WvOemIduSerialNumber_Object = MibScalar
wvOemIduSerialNumber = _WvOemIduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 33),
    _WvOemIduSerialNumber_Type()
)
wvOemIduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOemIduSerialNumber.setStatus("current")


class _WvOemOduSerialNumber_Type(DisplayString):
    """Custom type wvOemOduSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_WvOemOduSerialNumber_Type.__name__ = "DisplayString"
_WvOemOduSerialNumber_Object = MibScalar
wvOemOduSerialNumber = _WvOemOduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 34),
    _WvOemOduSerialNumber_Type()
)
wvOemOduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOemOduSerialNumber.setStatus("current")


class _WvOnePlusOneConnectorType_Type(Integer32):
    """Custom type wvOnePlusOneConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iau75", 2),
          ("iauDb25", 1),
          ("yCable", 0))
    )


_WvOnePlusOneConnectorType_Type.__name__ = "Integer32"
_WvOnePlusOneConnectorType_Object = MibScalar
wvOnePlusOneConnectorType = _WvOnePlusOneConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 35),
    _WvOnePlusOneConnectorType_Type()
)
wvOnePlusOneConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvOnePlusOneConnectorType.setStatus("current")
_WvLog_ObjectIdentity = ObjectIdentity
wvLog = _WvLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 40)
)
_WvLogEventsElapsed_Type = Gauge32
_WvLogEventsElapsed_Object = MibScalar
wvLogEventsElapsed = _WvLogEventsElapsed_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 40, 1),
    _WvLogEventsElapsed_Type()
)
wvLogEventsElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLogEventsElapsed.setStatus("current")
_WvLogEventTable_Object = MibTable
wvLogEventTable = _WvLogEventTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 40, 2)
)
if mibBuilder.loadTexts:
    wvLogEventTable.setStatus("current")
_WvLogEventEntry_Object = MibTableRow
wvLogEventEntry = _WvLogEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 40, 2, 1)
)
wvLogEventEntry.setIndexNames(
    (0, "CODAN-MIB", "wvLogEventLock"),
)
if mibBuilder.loadTexts:
    wvLogEventEntry.setStatus("current")


class _WvLogEventLock_Type(Integer32):
    """Custom type wvLogEventLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WvLogEventLock_Type.__name__ = "Integer32"
_WvLogEventLock_Object = MibTableColumn
wvLogEventLock = _WvLogEventLock_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 40, 2, 1, 1),
    _WvLogEventLock_Type()
)
wvLogEventLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLogEventLock.setStatus("current")
_WvLogEventTime_Type = TimeTicks
_WvLogEventTime_Object = MibTableColumn
wvLogEventTime = _WvLogEventTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 40, 2, 1, 2),
    _WvLogEventTime_Type()
)
wvLogEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLogEventTime.setStatus("current")


class _WvLogEventStatus_Type(Integer32):
    """Custom type wvLogEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fatalEnd", 6),
          ("fatalStart", 3),
          ("messageEnd", 4),
          ("messageStart", 1),
          ("warningEnd", 5),
          ("warningStart", 2))
    )


_WvLogEventStatus_Type.__name__ = "Integer32"
_WvLogEventStatus_Object = MibTableColumn
wvLogEventStatus = _WvLogEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 40, 2, 1, 3),
    _WvLogEventStatus_Type()
)
wvLogEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLogEventStatus.setStatus("current")


class _WvLogEventDescription_Type(DisplayString):
    """Custom type wvLogEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WvLogEventDescription_Type.__name__ = "DisplayString"
_WvLogEventDescription_Object = MibTableColumn
wvLogEventDescription = _WvLogEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 2, 40, 2, 1, 4),
    _WvLogEventDescription_Type()
)
wvLogEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLogEventDescription.setStatus("current")
_WvPerformance_ObjectIdentity = ObjectIdentity
wvPerformance = _WvPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3)
)
_WvlinkBER_Type = FloatingPoint
_WvlinkBER_Object = MibScalar
wvlinkBER = _WvlinkBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 1),
    _WvlinkBER_Type()
)
wvlinkBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkBER.setStatus("current")
_WvlinkBLER_Type = FloatingPoint
_WvlinkBLER_Object = MibScalar
wvlinkBLER = _WvlinkBLER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 2),
    _WvlinkBLER_Type()
)
wvlinkBLER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkBLER.setStatus("current")
_WvlinkBBER_Type = FloatingPoint
_WvlinkBBER_Object = MibScalar
wvlinkBBER = _WvlinkBBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 3),
    _WvlinkBBER_Type()
)
wvlinkBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkBBER.setStatus("current")
_WvlinkNCBLER_Type = FloatingPoint
_WvlinkNCBLER_Object = MibScalar
wvlinkNCBLER = _WvlinkNCBLER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 4),
    _WvlinkNCBLER_Type()
)
wvlinkNCBLER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkNCBLER.setStatus("current")
_WvLinkESs_Type = Gauge32
_WvLinkESs_Object = MibScalar
wvLinkESs = _WvLinkESs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 5),
    _WvLinkESs_Type()
)
wvLinkESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkESs.setStatus("current")
if mibBuilder.loadTexts:
    wvLinkESs.setUnits("seconds")
_WvLinkSESs_Type = Gauge32
_WvLinkSESs_Object = MibScalar
wvLinkSESs = _WvLinkSESs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 6),
    _WvLinkSESs_Type()
)
wvLinkSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkSESs.setStatus("current")
if mibBuilder.loadTexts:
    wvLinkSESs.setUnits("seconds")
_WvLinkUAs_Type = Gauge32
_WvLinkUAs_Object = MibScalar
wvLinkUAs = _WvLinkUAs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 7),
    _WvLinkUAs_Type()
)
wvLinkUAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkUAs.setStatus("current")
if mibBuilder.loadTexts:
    wvLinkUAs.setUnits("seconds")
_WvLinkDMs_Type = Gauge32
_WvLinkDMs_Object = MibScalar
wvLinkDMs = _WvLinkDMs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 8),
    _WvLinkDMs_Type()
)
wvLinkDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkDMs.setStatus("current")
if mibBuilder.loadTexts:
    wvLinkDMs.setUnits("minutes")
_WvlinkAverageRSL_Type = Integer32
_WvlinkAverageRSL_Object = MibScalar
wvlinkAverageRSL = _WvlinkAverageRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 9),
    _WvlinkAverageRSL_Type()
)
wvlinkAverageRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkAverageRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkAverageRSL.setUnits("dBm")
_WvlinkMaximumRSL_Type = Integer32
_WvlinkMaximumRSL_Object = MibScalar
wvlinkMaximumRSL = _WvlinkMaximumRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 10),
    _WvlinkMaximumRSL_Type()
)
wvlinkMaximumRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkMaximumRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkMaximumRSL.setUnits("dBm")
_WvlinkMinimumRSL_Type = Integer32
_WvlinkMinimumRSL_Object = MibScalar
wvlinkMinimumRSL = _WvlinkMinimumRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 11),
    _WvlinkMinimumRSL_Type()
)
wvlinkMinimumRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkMinimumRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkMinimumRSL.setUnits("dBm")


class _WvLinkValidIntervals_Type(Integer32):
    """Custom type wvLinkValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_WvLinkValidIntervals_Type.__name__ = "Integer32"
_WvLinkValidIntervals_Object = MibScalar
wvLinkValidIntervals = _WvLinkValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 12),
    _WvLinkValidIntervals_Type()
)
wvLinkValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkValidIntervals.setStatus("current")
_WvLinkCurrentESs_Type = Gauge32
_WvLinkCurrentESs_Object = MibScalar
wvLinkCurrentESs = _WvLinkCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 13),
    _WvLinkCurrentESs_Type()
)
wvLinkCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkCurrentESs.setStatus("current")
if mibBuilder.loadTexts:
    wvLinkCurrentESs.setUnits("seconds")
_WvLinkCurrentSESs_Type = Gauge32
_WvLinkCurrentSESs_Object = MibScalar
wvLinkCurrentSESs = _WvLinkCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 14),
    _WvLinkCurrentSESs_Type()
)
wvLinkCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkCurrentSESs.setStatus("current")
if mibBuilder.loadTexts:
    wvLinkCurrentSESs.setUnits("seconds")
_WvLinkCurrentUASs_Type = Gauge32
_WvLinkCurrentUASs_Object = MibScalar
wvLinkCurrentUASs = _WvLinkCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 15),
    _WvLinkCurrentUASs_Type()
)
wvLinkCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkCurrentUASs.setStatus("current")
if mibBuilder.loadTexts:
    wvLinkCurrentUASs.setUnits("seconds")
_WvLinkCurrentDMs_Type = Gauge32
_WvLinkCurrentDMs_Object = MibScalar
wvLinkCurrentDMs = _WvLinkCurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 16),
    _WvLinkCurrentDMs_Type()
)
wvLinkCurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkCurrentDMs.setStatus("current")
if mibBuilder.loadTexts:
    wvLinkCurrentDMs.setUnits("seconds")
_WvLinkCurrentBER_Type = FloatingPoint
_WvLinkCurrentBER_Object = MibScalar
wvLinkCurrentBER = _WvLinkCurrentBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 17),
    _WvLinkCurrentBER_Type()
)
wvLinkCurrentBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkCurrentBER.setStatus("current")
_WvLinkCurrentBLER_Type = FloatingPoint
_WvLinkCurrentBLER_Object = MibScalar
wvLinkCurrentBLER = _WvLinkCurrentBLER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 18),
    _WvLinkCurrentBLER_Type()
)
wvLinkCurrentBLER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkCurrentBLER.setStatus("current")
_WvLinkCurrentBBER_Type = FloatingPoint
_WvLinkCurrentBBER_Object = MibScalar
wvLinkCurrentBBER = _WvLinkCurrentBBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 19),
    _WvLinkCurrentBBER_Type()
)
wvLinkCurrentBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkCurrentBBER.setStatus("current")
_WvLinkCurrentNCBLER_Type = FloatingPoint
_WvLinkCurrentNCBLER_Object = MibScalar
wvLinkCurrentNCBLER = _WvLinkCurrentNCBLER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 20),
    _WvLinkCurrentNCBLER_Type()
)
wvLinkCurrentNCBLER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkCurrentNCBLER.setStatus("current")
_WvlinkCurrentAverageRSL_Type = Integer32
_WvlinkCurrentAverageRSL_Object = MibScalar
wvlinkCurrentAverageRSL = _WvlinkCurrentAverageRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 21),
    _WvlinkCurrentAverageRSL_Type()
)
wvlinkCurrentAverageRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkCurrentAverageRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkCurrentAverageRSL.setUnits("dBm")
_WvlinkCurrentMaximumRSL_Type = Integer32
_WvlinkCurrentMaximumRSL_Object = MibScalar
wvlinkCurrentMaximumRSL = _WvlinkCurrentMaximumRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 22),
    _WvlinkCurrentMaximumRSL_Type()
)
wvlinkCurrentMaximumRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkCurrentMaximumRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkCurrentMaximumRSL.setUnits("dBm")
_WvlinkCurrentMinimumRSL_Type = Integer32
_WvlinkCurrentMinimumRSL_Object = MibScalar
wvlinkCurrentMinimumRSL = _WvlinkCurrentMinimumRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 23),
    _WvlinkCurrentMinimumRSL_Type()
)
wvlinkCurrentMinimumRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkCurrentMinimumRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkCurrentMinimumRSL.setUnits("dBm")


class _WvlinkCurrentTimeElapsed_Type(Integer32):
    """Custom type wvlinkCurrentTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_WvlinkCurrentTimeElapsed_Type.__name__ = "Integer32"
_WvlinkCurrentTimeElapsed_Object = MibScalar
wvlinkCurrentTimeElapsed = _WvlinkCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 24),
    _WvlinkCurrentTimeElapsed_Type()
)
wvlinkCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkCurrentTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkCurrentTimeElapsed.setUnits("seconds")
_WvLinkIntervalTable_Object = MibTable
wvLinkIntervalTable = _WvLinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25)
)
if mibBuilder.loadTexts:
    wvLinkIntervalTable.setStatus("current")
_WvLinkIntervalEntry_Object = MibTableRow
wvLinkIntervalEntry = _WvLinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1)
)
wvLinkIntervalEntry.setIndexNames(
    (0, "CODAN-MIB", "wvLinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    wvLinkIntervalEntry.setStatus("current")


class _WvLinkIntervalNumber_Type(Integer32):
    """Custom type wvLinkIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WvLinkIntervalNumber_Type.__name__ = "Integer32"
_WvLinkIntervalNumber_Object = MibTableColumn
wvLinkIntervalNumber = _WvLinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 1),
    _WvLinkIntervalNumber_Type()
)
wvLinkIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkIntervalNumber.setStatus("current")
_WvLinkIntervalESs_Type = Gauge32
_WvLinkIntervalESs_Object = MibTableColumn
wvLinkIntervalESs = _WvLinkIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 2),
    _WvLinkIntervalESs_Type()
)
wvLinkIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkIntervalESs.setStatus("current")
_WvLinkIntervalSESs_Type = Gauge32
_WvLinkIntervalSESs_Object = MibTableColumn
wvLinkIntervalSESs = _WvLinkIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 3),
    _WvLinkIntervalSESs_Type()
)
wvLinkIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkIntervalSESs.setStatus("current")
_WvLinkIntervalUASs_Type = Gauge32
_WvLinkIntervalUASs_Object = MibTableColumn
wvLinkIntervalUASs = _WvLinkIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 4),
    _WvLinkIntervalUASs_Type()
)
wvLinkIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkIntervalUASs.setStatus("current")
_WvLinkIntervalDMs_Type = Gauge32
_WvLinkIntervalDMs_Object = MibTableColumn
wvLinkIntervalDMs = _WvLinkIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 5),
    _WvLinkIntervalDMs_Type()
)
wvLinkIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkIntervalDMs.setStatus("current")
_WvLinkIntervalBER_Type = FloatingPoint
_WvLinkIntervalBER_Object = MibTableColumn
wvLinkIntervalBER = _WvLinkIntervalBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 6),
    _WvLinkIntervalBER_Type()
)
wvLinkIntervalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkIntervalBER.setStatus("current")
_WvLinkIntervalBLER_Type = FloatingPoint
_WvLinkIntervalBLER_Object = MibTableColumn
wvLinkIntervalBLER = _WvLinkIntervalBLER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 7),
    _WvLinkIntervalBLER_Type()
)
wvLinkIntervalBLER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkIntervalBLER.setStatus("current")
_WvLinkIntervalBBER_Type = FloatingPoint
_WvLinkIntervalBBER_Object = MibTableColumn
wvLinkIntervalBBER = _WvLinkIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 8),
    _WvLinkIntervalBBER_Type()
)
wvLinkIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkIntervalBBER.setStatus("current")
_WvLinkIntervalNCBLER_Type = FloatingPoint
_WvLinkIntervalNCBLER_Object = MibTableColumn
wvLinkIntervalNCBLER = _WvLinkIntervalNCBLER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 9),
    _WvLinkIntervalNCBLER_Type()
)
wvLinkIntervalNCBLER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkIntervalNCBLER.setStatus("current")
_WvlinkIntervalAverageRSL_Type = Integer32
_WvlinkIntervalAverageRSL_Object = MibTableColumn
wvlinkIntervalAverageRSL = _WvlinkIntervalAverageRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 10),
    _WvlinkIntervalAverageRSL_Type()
)
wvlinkIntervalAverageRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkIntervalAverageRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkIntervalAverageRSL.setUnits("dBm")
_WvlinkIntervalMaximumRSL_Type = Integer32
_WvlinkIntervalMaximumRSL_Object = MibTableColumn
wvlinkIntervalMaximumRSL = _WvlinkIntervalMaximumRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 11),
    _WvlinkIntervalMaximumRSL_Type()
)
wvlinkIntervalMaximumRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkIntervalMaximumRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkIntervalMaximumRSL.setUnits("dBm")
_WvlinkIntervalMinimumRSL_Type = Integer32
_WvlinkIntervalMinimumRSL_Object = MibTableColumn
wvlinkIntervalMinimumRSL = _WvlinkIntervalMinimumRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 25, 1, 12),
    _WvlinkIntervalMinimumRSL_Type()
)
wvlinkIntervalMinimumRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkIntervalMinimumRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkIntervalMinimumRSL.setUnits("dBm")
_WvLinkTotalESs_Type = Gauge32
_WvLinkTotalESs_Object = MibScalar
wvLinkTotalESs = _WvLinkTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 26),
    _WvLinkTotalESs_Type()
)
wvLinkTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkTotalESs.setStatus("current")
_WvLinkTotalSESs_Type = Gauge32
_WvLinkTotalSESs_Object = MibScalar
wvLinkTotalSESs = _WvLinkTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 27),
    _WvLinkTotalSESs_Type()
)
wvLinkTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkTotalSESs.setStatus("current")
_WvLinkTotalUASs_Type = Gauge32
_WvLinkTotalUASs_Object = MibScalar
wvLinkTotalUASs = _WvLinkTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 28),
    _WvLinkTotalUASs_Type()
)
wvLinkTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkTotalUASs.setStatus("current")
_WvLinkTotalDMs_Type = Gauge32
_WvLinkTotalDMs_Object = MibScalar
wvLinkTotalDMs = _WvLinkTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 29),
    _WvLinkTotalDMs_Type()
)
wvLinkTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkTotalDMs.setStatus("current")
_WvLinkTotalBER_Type = FloatingPoint
_WvLinkTotalBER_Object = MibScalar
wvLinkTotalBER = _WvLinkTotalBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 30),
    _WvLinkTotalBER_Type()
)
wvLinkTotalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkTotalBER.setStatus("current")
_WvLinkTotalBLER_Type = FloatingPoint
_WvLinkTotalBLER_Object = MibScalar
wvLinkTotalBLER = _WvLinkTotalBLER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 31),
    _WvLinkTotalBLER_Type()
)
wvLinkTotalBLER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkTotalBLER.setStatus("current")
_WvLinkTotalBBER_Type = FloatingPoint
_WvLinkTotalBBER_Object = MibScalar
wvLinkTotalBBER = _WvLinkTotalBBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 32),
    _WvLinkTotalBBER_Type()
)
wvLinkTotalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkTotalBBER.setStatus("current")
_WvLinkTotalNCBLER_Type = FloatingPoint
_WvLinkTotalNCBLER_Object = MibScalar
wvLinkTotalNCBLER = _WvLinkTotalNCBLER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 33),
    _WvLinkTotalNCBLER_Type()
)
wvLinkTotalNCBLER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkTotalNCBLER.setStatus("current")
_WvlinkTotalAverageRSL_Type = Integer32
_WvlinkTotalAverageRSL_Object = MibScalar
wvlinkTotalAverageRSL = _WvlinkTotalAverageRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 34),
    _WvlinkTotalAverageRSL_Type()
)
wvlinkTotalAverageRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkTotalAverageRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkTotalAverageRSL.setUnits("dBm")
_WvlinkTotalMaximumRSL_Type = Integer32
_WvlinkTotalMaximumRSL_Object = MibScalar
wvlinkTotalMaximumRSL = _WvlinkTotalMaximumRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 35),
    _WvlinkTotalMaximumRSL_Type()
)
wvlinkTotalMaximumRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkTotalMaximumRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkTotalMaximumRSL.setUnits("dBm")
_WvlinkTotalMinimumRSL_Type = Integer32
_WvlinkTotalMinimumRSL_Object = MibScalar
wvlinkTotalMinimumRSL = _WvlinkTotalMinimumRSL_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 36),
    _WvlinkTotalMinimumRSL_Type()
)
wvlinkTotalMinimumRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkTotalMinimumRSL.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkTotalMinimumRSL.setUnits("dBm")
_WvlinkNoOfReceivedKBits_Type = Counter32
_WvlinkNoOfReceivedKBits_Object = MibScalar
wvlinkNoOfReceivedKBits = _WvlinkNoOfReceivedKBits_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 40),
    _WvlinkNoOfReceivedKBits_Type()
)
wvlinkNoOfReceivedKBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkNoOfReceivedKBits.setStatus("current")
if mibBuilder.loadTexts:
    wvlinkNoOfReceivedKBits.setUnits("Kilobits")
_WvlinkNoOfErrors_Type = Counter32
_WvlinkNoOfErrors_Object = MibScalar
wvlinkNoOfErrors = _WvlinkNoOfErrors_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 41),
    _WvlinkNoOfErrors_Type()
)
wvlinkNoOfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkNoOfErrors.setStatus("current")
_WvlinkErroredBlocks_Type = Counter32
_WvlinkErroredBlocks_Object = MibScalar
wvlinkErroredBlocks = _WvlinkErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 42),
    _WvlinkErroredBlocks_Type()
)
wvlinkErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkErroredBlocks.setStatus("current")
_WvlinkNotCorrectedErroredBlocks_Type = Counter32
_WvlinkNotCorrectedErroredBlocks_Object = MibScalar
wvlinkNotCorrectedErroredBlocks = _WvlinkNotCorrectedErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 43),
    _WvlinkNotCorrectedErroredBlocks_Type()
)
wvlinkNotCorrectedErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkNotCorrectedErroredBlocks.setStatus("current")
_WvLinkPerformanceCountTime_Type = TimeTicks
_WvLinkPerformanceCountTime_Object = MibScalar
wvLinkPerformanceCountTime = _WvLinkPerformanceCountTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 50),
    _WvLinkPerformanceCountTime_Type()
)
wvLinkPerformanceCountTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLinkPerformanceCountTime.setStatus("current")
_WvlinkInstantaneousBER_Type = FloatingPoint
_WvlinkInstantaneousBER_Object = MibScalar
wvlinkInstantaneousBER = _WvlinkInstantaneousBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 60),
    _WvlinkInstantaneousBER_Type()
)
wvlinkInstantaneousBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvlinkInstantaneousBER.setStatus("current")
_WvEth10_100TxLinkUsage_Type = Integer32
_WvEth10_100TxLinkUsage_Object = MibScalar
wvEth10_100TxLinkUsage = _WvEth10_100TxLinkUsage_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 100),
    _WvEth10_100TxLinkUsage_Type()
)
wvEth10_100TxLinkUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvEth10_100TxLinkUsage.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100TxLinkUsage.setUnits("Bits/sec")
_WvEth10_100RxLinkUsage_Type = Integer32
_WvEth10_100RxLinkUsage_Object = MibScalar
wvEth10_100RxLinkUsage = _WvEth10_100RxLinkUsage_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 101),
    _WvEth10_100RxLinkUsage_Type()
)
wvEth10_100RxLinkUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvEth10_100RxLinkUsage.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100RxLinkUsage.setUnits("Bits/sec")
_WvEth10_100TxLinkUtilization_Type = Integer32
_WvEth10_100TxLinkUtilization_Object = MibScalar
wvEth10_100TxLinkUtilization = _WvEth10_100TxLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 102),
    _WvEth10_100TxLinkUtilization_Type()
)
wvEth10_100TxLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvEth10_100TxLinkUtilization.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100TxLinkUtilization.setUnits("%")
_WvEth10_100RxLinkUtilization_Type = Integer32
_WvEth10_100RxLinkUtilization_Object = MibScalar
wvEth10_100RxLinkUtilization = _WvEth10_100RxLinkUtilization_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 3, 103),
    _WvEth10_100RxLinkUtilization_Type()
)
wvEth10_100RxLinkUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvEth10_100RxLinkUtilization.setStatus("current")
if mibBuilder.loadTexts:
    wvEth10_100RxLinkUtilization.setUnits("%")
_WvTests_ObjectIdentity = ObjectIdentity
wvTests = _WvTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4)
)
_WvLoopbackType_Type = WvLoopbacksList
_WvLoopbackType_Object = MibScalar
wvLoopbackType = _WvLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 1),
    _WvLoopbackType_Type()
)
wvLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLoopbackType.setStatus("current")
_WvLoopbackStartTime_Type = TimeTicks
_WvLoopbackStartTime_Object = MibScalar
wvLoopbackStartTime = _WvLoopbackStartTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 2),
    _WvLoopbackStartTime_Type()
)
wvLoopbackStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLoopbackStartTime.setStatus("current")


class _WvLoopbackTimePeriod_Type(TimeInterval):
    """Custom type wvLoopbackTimePeriod based on TimeInterval"""
    defaultValue = 60000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_WvLoopbackTimePeriod_Type.__name__ = "TimeInterval"
_WvLoopbackTimePeriod_Object = MibScalar
wvLoopbackTimePeriod = _WvLoopbackTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 3),
    _WvLoopbackTimePeriod_Type()
)
wvLoopbackTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvLoopbackTimePeriod.setStatus("current")
_WvLoopbackRemainingStartTime_Type = TimeTicks
_WvLoopbackRemainingStartTime_Object = MibScalar
wvLoopbackRemainingStartTime = _WvLoopbackRemainingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 4),
    _WvLoopbackRemainingStartTime_Type()
)
wvLoopbackRemainingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLoopbackRemainingStartTime.setStatus("current")
_WvLoopbackRemainingTimePeriod_Type = TimeInterval
_WvLoopbackRemainingTimePeriod_Object = MibScalar
wvLoopbackRemainingTimePeriod = _WvLoopbackRemainingTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 5),
    _WvLoopbackRemainingTimePeriod_Type()
)
wvLoopbackRemainingTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLoopbackRemainingTimePeriod.setStatus("current")


class _WvSelfTestType_Type(Bits):
    """Custom type wvSelfTestType based on Bits"""
    namedValues = NamedValues(
        *(("bertTest", 9),
          ("epromTest", 3),
          ("fecTest", 6),
          ("flashTest", 2),
          ("fpTest", 4),
          ("ibTest", 8),
          ("modemTest", 5),
          ("muxTest", 7),
          ("noTest", 0),
          ("ramTest", 1),
          ("sccTest", 10))
    )

_WvSelfTestType_Type.__name__ = "Bits"
_WvSelfTestType_Object = MibScalar
wvSelfTestType = _WvSelfTestType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 100),
    _WvSelfTestType_Type()
)
wvSelfTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSelfTestType.setStatus("deprecated")
_WvSelfTestStartTime_Type = TimeTicks
_WvSelfTestStartTime_Object = MibScalar
wvSelfTestStartTime = _WvSelfTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 101),
    _WvSelfTestStartTime_Type()
)
wvSelfTestStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSelfTestStartTime.setStatus("deprecated")
_WvLastSelfTestStartTime_Type = TimeTicks
_WvLastSelfTestStartTime_Object = MibScalar
wvLastSelfTestStartTime = _WvLastSelfTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 102),
    _WvLastSelfTestStartTime_Type()
)
wvLastSelfTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLastSelfTestStartTime.setStatus("current")
_WvLastSelfTestTable_Object = MibTable
wvLastSelfTestTable = _WvLastSelfTestTable_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 103)
)
if mibBuilder.loadTexts:
    wvLastSelfTestTable.setStatus("current")
_WvLastSelfTestEntry_Object = MibTableRow
wvLastSelfTestEntry = _WvLastSelfTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 103, 1)
)
wvLastSelfTestEntry.setIndexNames(
    (0, "CODAN-MIB", "wvLastSelfTestType"),
)
if mibBuilder.loadTexts:
    wvLastSelfTestEntry.setStatus("current")


class _WvLastSelfTestType_Type(Integer32):
    """Custom type wvLastSelfTestType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("bertTest", 9),
          ("epromTest", 3),
          ("fecTest", 6),
          ("flashTest", 2),
          ("fpTest", 4),
          ("ibTest", 8),
          ("modemTest", 5),
          ("muxTest", 7),
          ("noTest", 0),
          ("ramTest", 1),
          ("sccTest", 10))
    )


_WvLastSelfTestType_Type.__name__ = "Integer32"
_WvLastSelfTestType_Object = MibTableColumn
wvLastSelfTestType = _WvLastSelfTestType_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 103, 1, 1),
    _WvLastSelfTestType_Type()
)
wvLastSelfTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLastSelfTestType.setStatus("current")


class _WvLastSelfTestStatus_Type(Integer32):
    """Custom type wvLastSelfTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_WvLastSelfTestStatus_Type.__name__ = "Integer32"
_WvLastSelfTestStatus_Object = MibTableColumn
wvLastSelfTestStatus = _WvLastSelfTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 103, 1, 2),
    _WvLastSelfTestStatus_Type()
)
wvLastSelfTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLastSelfTestStatus.setStatus("current")
_WvSelfTestRemainingStartTime_Type = TimeTicks
_WvSelfTestRemainingStartTime_Object = MibScalar
wvSelfTestRemainingStartTime = _WvSelfTestRemainingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 104),
    _WvSelfTestRemainingStartTime_Type()
)
wvSelfTestRemainingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvSelfTestRemainingStartTime.setStatus("deprecated")


class _WvInsertTestSignalLine_Type(Bits):
    """Custom type wvInsertTestSignalLine based on Bits"""
    namedValues = NamedValues(
        *(("dsx1-1", 1),
          ("dsx1-10", 10),
          ("dsx1-11", 11),
          ("dsx1-12", 12),
          ("dsx1-13", 13),
          ("dsx1-14", 14),
          ("dsx1-15", 15),
          ("dsx1-16", 16),
          ("dsx1-2", 2),
          ("dsx1-3", 3),
          ("dsx1-4", 4),
          ("dsx1-5", 5),
          ("dsx1-6", 6),
          ("dsx1-7", 7),
          ("dsx1-8", 8),
          ("dsx1-9", 9),
          ("dsx3", 17),
          ("eth10-100", 18),
          ("filler0", 0))
    )

_WvInsertTestSignalLine_Type.__name__ = "Bits"
_WvInsertTestSignalLine_Object = MibScalar
wvInsertTestSignalLine = _WvInsertTestSignalLine_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 200),
    _WvInsertTestSignalLine_Type()
)
wvInsertTestSignalLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvInsertTestSignalLine.setStatus("current")
_WvInsertTestSignalStartTime_Type = TimeTicks
_WvInsertTestSignalStartTime_Object = MibScalar
wvInsertTestSignalStartTime = _WvInsertTestSignalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 201),
    _WvInsertTestSignalStartTime_Type()
)
wvInsertTestSignalStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvInsertTestSignalStartTime.setStatus("current")


class _WvInsertTestSignalTimePeriod_Type(TimeInterval):
    """Custom type wvInsertTestSignalTimePeriod based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_WvInsertTestSignalTimePeriod_Type.__name__ = "TimeInterval"
_WvInsertTestSignalTimePeriod_Object = MibScalar
wvInsertTestSignalTimePeriod = _WvInsertTestSignalTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 202),
    _WvInsertTestSignalTimePeriod_Type()
)
wvInsertTestSignalTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvInsertTestSignalTimePeriod.setStatus("current")
_WvLastTestSignalTime_Type = TimeTicks
_WvLastTestSignalTime_Object = MibScalar
wvLastTestSignalTime = _WvLastTestSignalTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 203),
    _WvLastTestSignalTime_Type()
)
wvLastTestSignalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLastTestSignalTime.setStatus("current")
_WvLastTestSignalBER_Type = FloatingPoint
_WvLastTestSignalBER_Object = MibScalar
wvLastTestSignalBER = _WvLastTestSignalBER_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 204),
    _WvLastTestSignalBER_Type()
)
wvLastTestSignalBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLastTestSignalBER.setStatus("current")
_WvInsertTestSignalRemainingStartTime_Type = TimeTicks
_WvInsertTestSignalRemainingStartTime_Object = MibScalar
wvInsertTestSignalRemainingStartTime = _WvInsertTestSignalRemainingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 205),
    _WvInsertTestSignalRemainingStartTime_Type()
)
wvInsertTestSignalRemainingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvInsertTestSignalRemainingStartTime.setStatus("current")
_WvInsertTestSignalRemainingTimePeriod_Type = TimeInterval
_WvInsertTestSignalRemainingTimePeriod_Object = MibScalar
wvInsertTestSignalRemainingTimePeriod = _WvInsertTestSignalRemainingTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 206),
    _WvInsertTestSignalRemainingTimePeriod_Type()
)
wvInsertTestSignalRemainingTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvInsertTestSignalRemainingTimePeriod.setStatus("current")
_WvGenericDiagnosticsParameterAddress_Type = Integer32
_WvGenericDiagnosticsParameterAddress_Object = MibScalar
wvGenericDiagnosticsParameterAddress = _WvGenericDiagnosticsParameterAddress_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 300),
    _WvGenericDiagnosticsParameterAddress_Type()
)
wvGenericDiagnosticsParameterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvGenericDiagnosticsParameterAddress.setStatus("current")
_WvGenericDiagnosticsParameterValue_Type = Integer32
_WvGenericDiagnosticsParameterValue_Object = MibScalar
wvGenericDiagnosticsParameterValue = _WvGenericDiagnosticsParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 4, 301),
    _WvGenericDiagnosticsParameterValue_Type()
)
wvGenericDiagnosticsParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvGenericDiagnosticsParameterValue.setStatus("current")
_WvTraps_ObjectIdentity = ObjectIdentity
wvTraps = _WvTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10)
)
_WvTraps0_ObjectIdentity = ObjectIdentity
wvTraps0 = _WvTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0)
)
_WvTrapVars_ObjectIdentity = ObjectIdentity
wvTrapVars = _WvTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 1)
)
_WvTrapKeepAlivePeriod_Type = Integer32
_WvTrapKeepAlivePeriod_Object = MibScalar
wvTrapKeepAlivePeriod = _WvTrapKeepAlivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 1, 1),
    _WvTrapKeepAlivePeriod_Type()
)
wvTrapKeepAlivePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTrapKeepAlivePeriod.setStatus("current")
_WvAisPortTrap_Type = Integer32
_WvAisPortTrap_Object = MibScalar
wvAisPortTrap = _WvAisPortTrap_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 1, 2),
    _WvAisPortTrap_Type()
)
wvAisPortTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvAisPortTrap.setStatus("current")
_WvLosPortTrap_Type = Integer32
_WvLosPortTrap_Object = MibScalar
wvLosPortTrap = _WvLosPortTrap_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 1, 3),
    _WvLosPortTrap_Type()
)
wvLosPortTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvLosPortTrap.setStatus("current")


class _WvExternalInputTrap_Type(Integer32):
    """Custom type wvExternalInputTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_WvExternalInputTrap_Type.__name__ = "Integer32"
_WvExternalInputTrap_Object = MibScalar
wvExternalInputTrap = _WvExternalInputTrap_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 1, 4),
    _WvExternalInputTrap_Type()
)
wvExternalInputTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvExternalInputTrap.setStatus("current")
_WvRelayIdTrap_Type = Integer32
_WvRelayIdTrap_Object = MibScalar
wvRelayIdTrap = _WvRelayIdTrap_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 1, 5),
    _WvRelayIdTrap_Type()
)
wvRelayIdTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvRelayIdTrap.setStatus("current")


class _WvSelectTrapVector_Type(Bits):
    """Custom type wvSelectTrapVector based on Bits"""
    namedValues = NamedValues(
        *(("wlAisReceiveStart", 45),
          ("wlAisReceiveStop", 46),
          ("wlAisStart", 18),
          ("wlAisStop", 19),
          ("wlBankSw", 39),
          ("wlBerErrStart", 24),
          ("wlBerErrStop", 25),
          ("wlBerWarnStart", 22),
          ("wlBerWarnStop", 23),
          ("wlCfgMismatch", 38),
          ("wlEnd", 55),
          ("wlEth10x100RxLinkUsageHighStart", 49),
          ("wlEth10x100RxLinkUsageHighStop", 50),
          ("wlEth10x100RxLinkUsageLowStart", 47),
          ("wlEth10x100RxLinkUsageLowStop", 48),
          ("wlEth10x100TxLinkUsageHighStart", 53),
          ("wlEth10x100TxLinkUsageHighStop", 54),
          ("wlEth10x100TxLinkUsageLowStart", 51),
          ("wlEth10x100TxLinkUsageLowStop", 52),
          ("wlExtInputsStart", 26),
          ("wlExtInputsStop", 27),
          ("wlHeartBit", 44),
          ("wlIdViolationStop", 9),
          ("wlIdViolationtStart", 8),
          ("wlIduIntnlFaultStart", 2),
          ("wlIduIntnlFaultStop", 3),
          ("wlLinkDownStart", 6),
          ("wlLinkDownStop", 7),
          ("wlLoclOduAccsStart", 12),
          ("wlLoclOduAccsStop", 13),
          ("wlLosStart", 20),
          ("wlLosStop", 21),
          ("wlOduCableFaultStart", 0),
          ("wlOduCableFaultStop", 1),
          ("wlOduIntnlFaultStart", 4),
          ("wlOduIntnlFaultStop", 5),
          ("wlOduTempStart", 32),
          ("wlOduTempStop", 33),
          ("wlPortBertStart", 42),
          ("wlPortBertStop", 43),
          ("wlPortLoopBckStart", 40),
          ("wlPortLoopBckStop", 41),
          ("wlPwrSupplyStart", 36),
          ("wlPwrSupplyStop", 37),
          ("wlRcvSignLowLevlStart", 14),
          ("wlRcvSignLowLevlStop", 15),
          ("wlRelayStart", 16),
          ("wlRelayStop", 17),
          ("wlRmtTermAccsStart", 10),
          ("wlRmtTermAccsStop", 11),
          ("wlTftpFail", 30),
          ("wlTftpSuss", 31),
          ("wlTxMuteStart", 34),
          ("wlTxMuteStop", 35),
          ("wlUasStart", 28),
          ("wlUasStop", 29))
    )

_WvSelectTrapVector_Type.__name__ = "Bits"
_WvSelectTrapVector_Object = MibScalar
wvSelectTrapVector = _WvSelectTrapVector_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 1, 6),
    _WvSelectTrapVector_Type()
)
wvSelectTrapVector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvSelectTrapVector.setStatus("current")


class _WvTrapKeepAliveVarsSelect_Type(Bits):
    """Custom type wvTrapKeepAliveVarsSelect based on Bits"""
    namedValues = NamedValues(
        *(("vBER", 1),
          ("vEnd", 3),
          ("vRSL", 0),
          ("vUAS", 2))
    )

_WvTrapKeepAliveVarsSelect_Type.__name__ = "Bits"
_WvTrapKeepAliveVarsSelect_Object = MibScalar
wvTrapKeepAliveVarsSelect = _WvTrapKeepAliveVarsSelect_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 1, 7),
    _WvTrapKeepAliveVarsSelect_Type()
)
wvTrapKeepAliveVarsSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wvTrapKeepAliveVarsSelect.setStatus("current")


class _WvTrapKeepAliveString_Type(DisplayString):
    """Custom type wvTrapKeepAliveString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WvTrapKeepAliveString_Type.__name__ = "DisplayString"
_WvTrapKeepAliveString_Object = MibScalar
wvTrapKeepAliveString = _WvTrapKeepAliveString_Object(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 1, 8),
    _WvTrapKeepAliveString_Type()
)
wvTrapKeepAliveString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wvTrapKeepAliveString.setStatus("current")

# Managed Objects groups


# Notification objects

wvIduOduCableFaultStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 1)
)
wvIduOduCableFaultStart.setObjects(
    ("CODAN-MIB", "wvIduOduCableStatus")
)
if mibBuilder.loadTexts:
    wvIduOduCableFaultStart.setStatus(
        "current"
    )

wvIduOduCableFaultStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 2)
)
wvIduOduCableFaultStop.setObjects(
    ("CODAN-MIB", "wvIduOduCableStatus")
)
if mibBuilder.loadTexts:
    wvIduOduCableFaultStop.setStatus(
        "current"
    )

wvIduInternalFaultStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 3)
)
wvIduInternalFaultStart.setObjects(
    ("CODAN-MIB", "wvIduStatus")
)
if mibBuilder.loadTexts:
    wvIduInternalFaultStart.setStatus(
        "current"
    )

wvIduInternalFaultStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 4)
)
wvIduInternalFaultStop.setObjects(
    ("CODAN-MIB", "wvIduStatus")
)
if mibBuilder.loadTexts:
    wvIduInternalFaultStop.setStatus(
        "current"
    )

wvOduInternalFaultStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 5)
)
wvOduInternalFaultStart.setObjects(
    ("CODAN-MIB", "wvOduStatus")
)
if mibBuilder.loadTexts:
    wvOduInternalFaultStart.setStatus(
        "current"
    )

wvOduInternalFaultStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 6)
)
wvOduInternalFaultStop.setObjects(
    ("CODAN-MIB", "wvOduStatus")
)
if mibBuilder.loadTexts:
    wvOduInternalFaultStop.setStatus(
        "current"
    )

wvLinkDownStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 7)
)
wvLinkDownStart.setObjects(
    ("CODAN-MIB", "wvLinkPerformanceAlarmsStatus")
)
if mibBuilder.loadTexts:
    wvLinkDownStart.setStatus(
        "current"
    )

wvLinkDownStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 8)
)
wvLinkDownStop.setObjects(
    ("CODAN-MIB", "wvLinkPerformanceAlarmsStatus")
)
if mibBuilder.loadTexts:
    wvLinkDownStop.setStatus(
        "current"
    )

wvIdViolationStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 9)
)
wvIdViolationStart.setObjects(
    ("CODAN-MIB", "wvSecurityStatus")
)
if mibBuilder.loadTexts:
    wvIdViolationStart.setStatus(
        "current"
    )

wvIdViolationStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 10)
)
wvIdViolationStop.setObjects(
    ("CODAN-MIB", "wvSecurityStatus")
)
if mibBuilder.loadTexts:
    wvIdViolationStop.setStatus(
        "current"
    )

wvRemoteAccessStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 11)
)
wvRemoteAccessStart.setObjects(
    ("CODAN-MIB", "wvRemoteTerminalStatus")
)
if mibBuilder.loadTexts:
    wvRemoteAccessStart.setStatus(
        "current"
    )

wvRemoteAccessStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 12)
)
wvRemoteAccessStop.setObjects(
    ("CODAN-MIB", "wvRemoteTerminalStatus")
)
if mibBuilder.loadTexts:
    wvRemoteAccessStop.setStatus(
        "current"
    )

wvLocalOduAccessStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 13)
)
wvLocalOduAccessStart.setObjects(
    ("CODAN-MIB", "wvOduStatus")
)
if mibBuilder.loadTexts:
    wvLocalOduAccessStart.setStatus(
        "current"
    )

wvLocalOduAccessStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 14)
)
wvLocalOduAccessStop.setObjects(
    ("CODAN-MIB", "wvOduStatus")
)
if mibBuilder.loadTexts:
    wvLocalOduAccessStop.setStatus(
        "current"
    )

wvReceiveSignalLowerLevelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 15)
)
wvReceiveSignalLowerLevelStart.setObjects(
      *(("CODAN-MIB", "wvRxSignalLevel"),
        ("CODAN-MIB", "wvAtpcRslLowerThreshold"))
)
if mibBuilder.loadTexts:
    wvReceiveSignalLowerLevelStart.setStatus(
        "current"
    )

wvReceiveSignalLowerLevelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 16)
)
wvReceiveSignalLowerLevelStop.setObjects(
      *(("CODAN-MIB", "wvRxSignalLevel"),
        ("CODAN-MIB", "wvAtpcRslLowerThreshold"))
)
if mibBuilder.loadTexts:
    wvReceiveSignalLowerLevelStop.setStatus(
        "current"
    )

wvRelayStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 17)
)
wvRelayStart.setObjects(
    ("CODAN-MIB", "wvRelayIdTrap")
)
if mibBuilder.loadTexts:
    wvRelayStart.setStatus(
        "current"
    )

wvRelayStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 18)
)
wvRelayStop.setObjects(
    ("CODAN-MIB", "wvRelayIdTrap")
)
if mibBuilder.loadTexts:
    wvRelayStop.setStatus(
        "current"
    )

wvLineAisStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 19)
)
wvLineAisStart.setObjects(
    ("CODAN-MIB", "wvAisPortTrap")
)
if mibBuilder.loadTexts:
    wvLineAisStart.setStatus(
        "current"
    )

wvLineAisStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 20)
)
wvLineAisStop.setObjects(
    ("CODAN-MIB", "wvAisPortTrap")
)
if mibBuilder.loadTexts:
    wvLineAisStop.setStatus(
        "current"
    )

wvLineLosStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 21)
)
wvLineLosStart.setObjects(
    ("CODAN-MIB", "wvLosPortTrap")
)
if mibBuilder.loadTexts:
    wvLineLosStart.setStatus(
        "current"
    )

wvLineLosStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 22)
)
wvLineLosStop.setObjects(
    ("CODAN-MIB", "wvLosPortTrap")
)
if mibBuilder.loadTexts:
    wvLineLosStop.setStatus(
        "current"
    )

wvBerWarningStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 23)
)
wvBerWarningStart.setObjects(
      *(("CODAN-MIB", "wvlinkBER"),
        ("CODAN-MIB", "wvLinkBERWarningThresholdLow"),
        ("CODAN-MIB", "wvLinkBERWarningThresholdHigh"))
)
if mibBuilder.loadTexts:
    wvBerWarningStart.setStatus(
        "current"
    )

wvBerWarningStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 24)
)
wvBerWarningStop.setObjects(
      *(("CODAN-MIB", "wvlinkBER"),
        ("CODAN-MIB", "wvLinkBERWarningThresholdLow"),
        ("CODAN-MIB", "wvLinkBERWarningThresholdHigh"))
)
if mibBuilder.loadTexts:
    wvBerWarningStop.setStatus(
        "current"
    )

wvBerFatalStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 25)
)
wvBerFatalStart.setObjects(
      *(("CODAN-MIB", "wvlinkBER"),
        ("CODAN-MIB", "wvLinkBERErrorThresholdLow"),
        ("CODAN-MIB", "wvLinkBERErrorThresholdHigh"))
)
if mibBuilder.loadTexts:
    wvBerFatalStart.setStatus(
        "current"
    )

wvBerFatalStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 26)
)
wvBerFatalStop.setObjects(
      *(("CODAN-MIB", "wvlinkBER"),
        ("CODAN-MIB", "wvLinkBERErrorThresholdLow"),
        ("CODAN-MIB", "wvLinkBERErrorThresholdHigh"))
)
if mibBuilder.loadTexts:
    wvBerFatalStop.setStatus(
        "current"
    )

wvExternalInputsStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 27)
)
wvExternalInputsStart.setObjects(
    ("CODAN-MIB", "wvExternalInputTrap")
)
if mibBuilder.loadTexts:
    wvExternalInputsStart.setStatus(
        "current"
    )

wvExternalInputsStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 28)
)
wvExternalInputsStop.setObjects(
    ("CODAN-MIB", "wvExternalInputTrap")
)
if mibBuilder.loadTexts:
    wvExternalInputsStop.setStatus(
        "current"
    )

wvLinkUasStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 29)
)
wvLinkUasStart.setObjects(
      *(("CODAN-MIB", "wvLinkUAs"),
        ("CODAN-MIB", "wvLinkUASAlarmThresholdLow"),
        ("CODAN-MIB", "wvLinkUASAlarmThresholdHigh"))
)
if mibBuilder.loadTexts:
    wvLinkUasStart.setStatus(
        "current"
    )

wvLinkUasStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 30)
)
wvLinkUasStop.setObjects(
      *(("CODAN-MIB", "wvLinkUAs"),
        ("CODAN-MIB", "wvLinkUASAlarmThresholdLow"),
        ("CODAN-MIB", "wvLinkUASAlarmThresholdHigh"))
)
if mibBuilder.loadTexts:
    wvLinkUasStop.setStatus(
        "current"
    )

wvTftpFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 31)
)
wvTftpFail.setObjects(
      *(("CODAN-MIB", "wvTftpServerIpAddress"),
        ("CODAN-MIB", "wvTftpOperationCtrl"),
        ("CODAN-MIB", "wvTftpFileName"),
        ("CODAN-MIB", "wvTftpDwnlStatus"))
)
if mibBuilder.loadTexts:
    wvTftpFail.setStatus(
        "current"
    )

wvTftpSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 32)
)
wvTftpSuccess.setObjects(
      *(("CODAN-MIB", "wvTftpServerIpAddress"),
        ("CODAN-MIB", "wvTftpOperationCtrl"),
        ("CODAN-MIB", "wvTftpFileName"),
        ("CODAN-MIB", "wvTftpDwnlStatus"))
)
if mibBuilder.loadTexts:
    wvTftpSuccess.setStatus(
        "current"
    )

wvOduTempViolationStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 33)
)
wvOduTempViolationStart.setObjects(
    ("CODAN-MIB", "wvOduTemperature")
)
if mibBuilder.loadTexts:
    wvOduTempViolationStart.setStatus(
        "current"
    )

wvOduTempViolationStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 34)
)
wvOduTempViolationStop.setObjects(
    ("CODAN-MIB", "wvOduTemperature")
)
if mibBuilder.loadTexts:
    wvOduTempViolationStop.setStatus(
        "current"
    )

wvOduTxMuteStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 35)
)
wvOduTxMuteStart.setObjects(
    ("CODAN-MIB", "wvOduStatus")
)
if mibBuilder.loadTexts:
    wvOduTxMuteStart.setStatus(
        "current"
    )

wvOduTxMuteStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 36)
)
wvOduTxMuteStop.setObjects(
    ("CODAN-MIB", "wvOduStatus")
)
if mibBuilder.loadTexts:
    wvOduTxMuteStop.setStatus(
        "current"
    )

wvIduPowerSupplyStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 37)
)
wvIduPowerSupplyStart.setObjects(
    ("CODAN-MIB", "wvIduStatus")
)
if mibBuilder.loadTexts:
    wvIduPowerSupplyStart.setStatus(
        "current"
    )

wvIduPowerSupplyStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 38)
)
wvIduPowerSupplyStop.setObjects(
    ("CODAN-MIB", "wvIduStatus")
)
if mibBuilder.loadTexts:
    wvIduPowerSupplyStop.setStatus(
        "current"
    )

wvIduConfigurationMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 39)
)
if mibBuilder.loadTexts:
    wvIduConfigurationMismatch.setStatus(
        "current"
    )

wvIduBankSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 40)
)
if mibBuilder.loadTexts:
    wvIduBankSwitchover.setStatus(
        "current"
    )

wvIduPortLoopbackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 41)
)
wvIduPortLoopbackStart.setObjects(
    ("CODAN-MIB", "wvIduStatus")
)
if mibBuilder.loadTexts:
    wvIduPortLoopbackStart.setStatus(
        "current"
    )

wvIduPortLoopbackStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 42)
)
wvIduPortLoopbackStop.setObjects(
    ("CODAN-MIB", "wvIduStatus")
)
if mibBuilder.loadTexts:
    wvIduPortLoopbackStop.setStatus(
        "current"
    )

wvIduPortBertStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 43)
)
wvIduPortBertStart.setObjects(
    ("CODAN-MIB", "wvIduStatus")
)
if mibBuilder.loadTexts:
    wvIduPortBertStart.setStatus(
        "current"
    )

wvIduPortBertStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 44)
)
wvIduPortBertStop.setObjects(
    ("CODAN-MIB", "wvIduStatus")
)
if mibBuilder.loadTexts:
    wvIduPortBertStop.setStatus(
        "current"
    )

wvIduHeartBit = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 45)
)
wvIduHeartBit.setObjects(
    ("CODAN-MIB", "wvTrapKeepAliveString")
)
if mibBuilder.loadTexts:
    wvIduHeartBit.setStatus(
        "current"
    )

wvAisReceiveStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 46)
)
wvAisReceiveStart.setObjects(
    ("CODAN-MIB", "wvAisPortTrap")
)
if mibBuilder.loadTexts:
    wvAisReceiveStart.setStatus(
        "current"
    )

wvAisReceiveStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 47)
)
wvAisReceiveStop.setObjects(
    ("CODAN-MIB", "wvAisPortTrap")
)
if mibBuilder.loadTexts:
    wvAisReceiveStop.setStatus(
        "current"
    )

wlEth10x100RxLinkUsageLowStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 48)
)
wlEth10x100RxLinkUsageLowStart.setObjects(
      *(("CODAN-MIB", "wvEth10_100RxLinkUsage"),
        ("CODAN-MIB", "wvEth10_100RxLinkUsageAlarmThresholdLow"))
)
if mibBuilder.loadTexts:
    wlEth10x100RxLinkUsageLowStart.setStatus(
        "current"
    )

wlEth10x100RxLinkUsageLowStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 49)
)
wlEth10x100RxLinkUsageLowStop.setObjects(
      *(("CODAN-MIB", "wvEth10_100RxLinkUsage"),
        ("CODAN-MIB", "wvEth10_100RxLinkUsageAlarmThresholdLow"))
)
if mibBuilder.loadTexts:
    wlEth10x100RxLinkUsageLowStop.setStatus(
        "current"
    )

wlEth10x100RxLinkUsageHighStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 50)
)
wlEth10x100RxLinkUsageHighStart.setObjects(
      *(("CODAN-MIB", "wvEth10_100RxLinkUsage"),
        ("CODAN-MIB", "wvEth10_100RxLinkUsageAlarmThresholdHigh"))
)
if mibBuilder.loadTexts:
    wlEth10x100RxLinkUsageHighStart.setStatus(
        "current"
    )

wlEth10x100RxLinkUsageHighStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 51)
)
wlEth10x100RxLinkUsageHighStop.setObjects(
      *(("CODAN-MIB", "wvEth10_100RxLinkUsage"),
        ("CODAN-MIB", "wvEth10_100RxLinkUsageAlarmThresholdHigh"))
)
if mibBuilder.loadTexts:
    wlEth10x100RxLinkUsageHighStop.setStatus(
        "current"
    )

wlEth10x100TxLinkUsageLowStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 52)
)
wlEth10x100TxLinkUsageLowStart.setObjects(
      *(("CODAN-MIB", "wvEth10_100TxLinkUsage"),
        ("CODAN-MIB", "wvEth10_100TxLinkUsageAlarmThresholdLow"))
)
if mibBuilder.loadTexts:
    wlEth10x100TxLinkUsageLowStart.setStatus(
        "current"
    )

wlEth10x100TxLinkUsageLowStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 53)
)
wlEth10x100TxLinkUsageLowStop.setObjects(
      *(("CODAN-MIB", "wvEth10_100TxLinkUsage"),
        ("CODAN-MIB", "wvEth10_100TxLinkUsageAlarmThresholdLow"))
)
if mibBuilder.loadTexts:
    wlEth10x100TxLinkUsageLowStop.setStatus(
        "current"
    )

wlEth10x100TxLinkUsageHighStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 54)
)
wlEth10x100TxLinkUsageHighStart.setObjects(
      *(("CODAN-MIB", "wvEth10_100TxLinkUsage"),
        ("CODAN-MIB", "wvEth10_100TxLinkUsageAlarmThresholdHigh"))
)
if mibBuilder.loadTexts:
    wlEth10x100TxLinkUsageHighStart.setStatus(
        "current"
    )

wlEth10x100TxLinkUsageHighStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 23304, 1, 1, 10, 0, 55)
)
wlEth10x100TxLinkUsageHighStop.setObjects(
      *(("CODAN-MIB", "wvEth10_100TxLinkUsage"),
        ("CODAN-MIB", "wvEth10_100TxLinkUsageAlarmThresholdHigh"))
)
if mibBuilder.loadTexts:
    wlEth10x100TxLinkUsageHighStop.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CODAN-MIB",
    **{"WvAlarmsList": WvAlarmsList,
       "ComponentRevision": ComponentRevision,
       "FrontPanelPassword": FrontPanelPassword,
       "FloatingPoint": FloatingPoint,
       "WvLoopbacksList": WvLoopbacksList,
       "minetMIB": minetMIB,
       "wvConfiguration": wvConfiguration,
       "wvLinkSettings": wvLinkSettings,
       "wvLinkId": wvLinkId,
       "wvLinkName": wvLinkName,
       "wvLinkRouteDescription": wvLinkRouteDescription,
       "wvTxPowerSetting": wvTxPowerSetting,
       "wvChannelNo": wvChannelNo,
       "wvLinkCapacity": wvLinkCapacity,
       "wvTransmitterMute": wvTransmitterMute,
       "wvReceiverMute": wvReceiverMute,
       "wvModulation": wvModulation,
       "wvForceAis": wvForceAis,
       "wvFecEnabled": wvFecEnabled,
       "wvFecReceiveCorrection": wvFecReceiveCorrection,
       "wvFecNoOfCorrectableBytes": wvFecNoOfCorrectableBytes,
       "wvEth10-100ChannelSpacing": wvEth10_100ChannelSpacing,
       "wvAtpcControl": wvAtpcControl,
       "wvAtpcRslOptimalValue": wvAtpcRslOptimalValue,
       "wvAtpcRslUpperThreshold": wvAtpcRslUpperThreshold,
       "wvAtpcRslLowerThreshold": wvAtpcRslLowerThreshold,
       "wvPauseTransmitterControl": wvPauseTransmitterControl,
       "wvPauseTransmitterTime": wvPauseTransmitterTime,
       "wvE1BNC75ohm": wvE1BNC75ohm,
       "wvAtpcTimeOutControl": wvAtpcTimeOutControl,
       "wvAtpcTimeOutTimer": wvAtpcTimeOutTimer,
       "wvAtpcTimeOutAlarm": wvAtpcTimeOutAlarm,
       "wvAtpcTimeOutAlarmLevel": wvAtpcTimeOutAlarmLevel,
       "wvDisableAtpcInTimeOutAlarm": wvDisableAtpcInTimeOutAlarm,
       "wvEnableSpaceDiversity": wvEnableSpaceDiversity,
       "wvInterfaces": wvInterfaces,
       "wvTributaryPortConnectionsMode": wvTributaryPortConnectionsMode,
       "wvTributaryPortTable": wvTributaryPortTable,
       "wvTributaryPortEntry": wvTributaryPortEntry,
       "wvTributaryPortIfIndex": wvTributaryPortIfIndex,
       "wvTributaryPortConnection": wvTributaryPortConnection,
       "wvTributaryPortInvertedAlarm": wvTributaryPortInvertedAlarm,
       "wvTributaryPortName": wvTributaryPortName,
       "wvDsx3CableLengthRange": wvDsx3CableLengthRange,
       "wvSlipConnection": wvSlipConnection,
       "wvTelephoneNumber": wvTelephoneNumber,
       "wvDialPrefixString": wvDialPrefixString,
       "wvInitString": wvInitString,
       "wvEth10-100SysCtrl": wvEth10_100SysCtrl,
       "wvEth10-100SysAgingTime": wvEth10_100SysAgingTime,
       "wvEth10-100PortTable": wvEth10_100PortTable,
       "wvEth10-100PortEntry": wvEth10_100PortEntry,
       "wvEth10-100PortIfIndex": wvEth10_100PortIfIndex,
       "wvEth10-100PortCtrl": wvEth10_100PortCtrl,
       "wvEth10-100PortStatus": wvEth10_100PortStatus,
       "wvEth10-100PortClearStats": wvEth10_100PortClearStats,
       "wvEth10-100PortThroughputCtrl": wvEth10_100PortThroughputCtrl,
       "wvEth10-100AvailCapacity": wvEth10_100AvailCapacity,
       "wvRs232PortTable": wvRs232PortTable,
       "wvRs232PortEntry": wvRs232PortEntry,
       "wvRs232PortIndex": wvRs232PortIndex,
       "wvRs232PortType": wvRs232PortType,
       "wvRs232PortSpeed": wvRs232PortSpeed,
       "wvRs232PortFlowType": wvRs232PortFlowType,
       "wvRs232AsyncPortBits": wvRs232AsyncPortBits,
       "wvRs232AsyncPortStopBits": wvRs232AsyncPortStopBits,
       "wvRs232AsyncPortParity": wvRs232AsyncPortParity,
       "wvManagement": wvManagement,
       "wvUpdateTerminalConfiguration": wvUpdateTerminalConfiguration,
       "wvActivateTerminalConfiguration": wvActivateTerminalConfiguration,
       "wvResetTerminal": wvResetTerminal,
       "wvActivateTerminalConfigurationTime": wvActivateTerminalConfigurationTime,
       "wvSavedActiveConfiguration": wvSavedActiveConfiguration,
       "wvOnePlusOneRequestSwitchOut": wvOnePlusOneRequestSwitchOut,
       "wvFrontPanelUserPassword": wvFrontPanelUserPassword,
       "wvFrontPanelAdminPassword": wvFrontPanelAdminPassword,
       "wvFrontPanelSupervisorPassword": wvFrontPanelSupervisorPassword,
       "wvResetOdu": wvResetOdu,
       "wvSlipInIPAddress": wvSlipInIPAddress,
       "wvSlipInIPSubnetMask": wvSlipInIPSubnetMask,
       "wvSlipOutIPAddress": wvSlipOutIPAddress,
       "wvSlipOutIPSubnetMask": wvSlipOutIPSubnetMask,
       "wvLanIPAddress": wvLanIPAddress,
       "wvLanIPSubnetMask": wvLanIPSubnetMask,
       "wvLinkIPAddress": wvLinkIPAddress,
       "wvLinkIPSubnetMask": wvLinkIPSubnetMask,
       "wvEth10-100ManIPAddress": wvEth10_100ManIPAddress,
       "wvEth10-100ManIPSubnetMask": wvEth10_100ManIPSubnetMask,
       "wvPeerSlipInIPAddress": wvPeerSlipInIPAddress,
       "wvPeerSlipInIPSubnetMask": wvPeerSlipInIPSubnetMask,
       "wvPeerSlipOutIPAddress": wvPeerSlipOutIPAddress,
       "wvPeerSlipOutIPSubnetMask": wvPeerSlipOutIPSubnetMask,
       "wvPeerLanIPAddress": wvPeerLanIPAddress,
       "wvPeerLanIPSubnetMask": wvPeerLanIPSubnetMask,
       "wvPeerLinkIPAddress": wvPeerLinkIPAddress,
       "wvPeerLinkIPSubnetMask": wvPeerLinkIPSubnetMask,
       "wvPeerEth10-100ManIPAddress": wvPeerEth10_100ManIPAddress,
       "wvPeerEth10-100ManIPSubnetMask": wvPeerEth10_100ManIPSubnetMask,
       "wvSlipInDestIPAddress": wvSlipInDestIPAddress,
       "wvSlipInDestIPSubnetMask": wvSlipInDestIPSubnetMask,
       "wvSlipOutDestIPAddress": wvSlipOutDestIPAddress,
       "wvSlipOutDestIPSubnetMask": wvSlipOutDestIPSubnetMask,
       "wvOnePlusOneCompanionLinkIPAddress": wvOnePlusOneCompanionLinkIPAddress,
       "wvOnePlusOneCompanionEthIPAddress": wvOnePlusOneCompanionEthIPAddress,
       "wvUserRoutesManagement": wvUserRoutesManagement,
       "wvUserRoutesTable": wvUserRoutesTable,
       "wvUserRoutesEntry": wvUserRoutesEntry,
       "wvUserRoutesIndex": wvUserRoutesIndex,
       "wvUserRoutesDest": wvUserRoutesDest,
       "wvUserRoutesHop": wvUserRoutesHop,
       "wvUserRoutesMask": wvUserRoutesMask,
       "wvUserRoutesIf": wvUserRoutesIf,
       "wvUserRoutesType": wvUserRoutesType,
       "wvUserRoutesCount": wvUserRoutesCount,
       "wvSetOperationId": wvSetOperationId,
       "wvSetOperationCtrl": wvSetOperationCtrl,
       "wvSetOperationOwner": wvSetOperationOwner,
       "wvConfigurationChangedStatus": wvConfigurationChangedStatus,
       "wvCommunityTable": wvCommunityTable,
       "wvCommunityEntry": wvCommunityEntry,
       "wvCommunityId": wvCommunityId,
       "wvCommunityName": wvCommunityName,
       "wvCommunityPrivilege": wvCommunityPrivilege,
       "wvTrapRecipientsTable": wvTrapRecipientsTable,
       "wvTrapRecipientsEntry": wvTrapRecipientsEntry,
       "wvTrapRecipientsId": wvTrapRecipientsId,
       "wvTrapRecipientsIp": wvTrapRecipientsIp,
       "wvTftpServerIpAddress": wvTftpServerIpAddress,
       "wvTftpOperationCtrl": wvTftpOperationCtrl,
       "wvTftpNoOfRetries": wvTftpNoOfRetries,
       "wvTftpFileName": wvTftpFileName,
       "wvTftpStartTime": wvTftpStartTime,
       "wvTftpRemainingStartTime": wvTftpRemainingStartTime,
       "wvSwModuleTable": wvSwModuleTable,
       "wvSwModuleEntry": wvSwModuleEntry,
       "wvSwModuleIndex": wvSwModuleIndex,
       "wvSwModuleName": wvSwModuleName,
       "wvSwModuleActiveRev": wvSwModuleActiveRev,
       "wvSwModuleActiveCS": wvSwModuleActiveCS,
       "wvSwModuleStandByRev": wvSwModuleStandByRev,
       "wvSwModuleStandByCS": wvSwModuleStandByCS,
       "wvResetPerformance": wvResetPerformance,
       "wvRelays": wvRelays,
       "wvRelayTable": wvRelayTable,
       "wvRelayEntry": wvRelayEntry,
       "wvRelayId": wvRelayId,
       "wvRelayOperation": wvRelayOperation,
       "wvRelayNormalState": wvRelayNormalState,
       "wvRelayActivate": wvRelayActivate,
       "wvRelayToLocalAlarmMapping": wvRelayToLocalAlarmMapping,
       "wvRelayToRemoteAlarmMapping": wvRelayToRemoteAlarmMapping,
       "wvRelayStatus": wvRelayStatus,
       "wvExternalInputs": wvExternalInputs,
       "wvExternalInputTable": wvExternalInputTable,
       "wvExternalInputEntry": wvExternalInputEntry,
       "wvExternalInputId": wvExternalInputId,
       "wvExternalInputSetting": wvExternalInputSetting,
       "wvExternalInputSense": wvExternalInputSense,
       "wvExternalInputAlarmSeverity": wvExternalInputAlarmSeverity,
       "wvExternalInputStatus": wvExternalInputStatus,
       "wvAlarmControl": wvAlarmControl,
       "wvAlarmsReportToNMSCtrl": wvAlarmsReportToNMSCtrl,
       "wvAlarmsReportToLCDCtrl": wvAlarmsReportToLCDCtrl,
       "wvNoOfAlertsOnLCD": wvNoOfAlertsOnLCD,
       "wvLinkBERWarningThresholdHigh": wvLinkBERWarningThresholdHigh,
       "wvLinkBERWarningThresholdLow": wvLinkBERWarningThresholdLow,
       "wvLinkBERErrorThresholdHigh": wvLinkBERErrorThresholdHigh,
       "wvLinkBERErrorThresholdLow": wvLinkBERErrorThresholdLow,
       "wvLinkBLERAlarmThresholdHigh": wvLinkBLERAlarmThresholdHigh,
       "wvLinkBLERAlarmThresholdLow": wvLinkBLERAlarmThresholdLow,
       "wvLinkBBERAlarmThresholdHigh": wvLinkBBERAlarmThresholdHigh,
       "wvLinkBBERAlarmThresholdLow": wvLinkBBERAlarmThresholdLow,
       "wvLinkNCBLERAlarmThresholdHigh": wvLinkNCBLERAlarmThresholdHigh,
       "wvLinkNCBLERAlarmThresholdLow": wvLinkNCBLERAlarmThresholdLow,
       "wvLinkESAlarmThresholdHigh": wvLinkESAlarmThresholdHigh,
       "wvLinkESAlarmThresholdLow": wvLinkESAlarmThresholdLow,
       "wvLinkSESAlarmThresholdHigh": wvLinkSESAlarmThresholdHigh,
       "wvLinkSESAlarmThresholdLow": wvLinkSESAlarmThresholdLow,
       "wvLinkDMAlarmThresholdHigh": wvLinkDMAlarmThresholdHigh,
       "wvLinkDMAlarmThresholdLow": wvLinkDMAlarmThresholdLow,
       "wvLinkUASAlarmThresholdHigh": wvLinkUASAlarmThresholdHigh,
       "wvLinkUASAlarmThresholdLow": wvLinkUASAlarmThresholdLow,
       "wvlinkRSLLowAlarmThresholdhHigh": wvlinkRSLLowAlarmThresholdhHigh,
       "wvlinkRSLLowAlarmThresholdhLow": wvlinkRSLLowAlarmThresholdhLow,
       "wvlinkAverageRSLLowAlarmThresholdhHigh": wvlinkAverageRSLLowAlarmThresholdhHigh,
       "wvlinkAverageRSLLowAlarmThresholdhLow": wvlinkAverageRSLLowAlarmThresholdhLow,
       "wvLinkThresholdMeasurementInterval": wvLinkThresholdMeasurementInterval,
       "wvEth10-100CSLAlarmThresholdhHigh": wvEth10_100CSLAlarmThresholdhHigh,
       "wvEth10-100CSLAlarmThresholdhLow": wvEth10_100CSLAlarmThresholdhLow,
       "wvEth10-100ECAlarmThresholdhHigh": wvEth10_100ECAlarmThresholdhHigh,
       "wvEth10-100ECAlarmThresholdhLow": wvEth10_100ECAlarmThresholdhLow,
       "wvEth10-100IMTEAlarmThresholdhHigh": wvEth10_100IMTEAlarmThresholdhHigh,
       "wvEth10-100IMTEAlarmThresholdhLow": wvEth10_100IMTEAlarmThresholdhLow,
       "wvEth10-100IMREAlarmThresholdhHigh": wvEth10_100IMREAlarmThresholdhHigh,
       "wvEth10-100IMREAlarmThresholdhLow": wvEth10_100IMREAlarmThresholdhLow,
       "wvEth10-100TxLinkUsageAlarmThresholdLow": wvEth10_100TxLinkUsageAlarmThresholdLow,
       "wvEth10-100TxLinkUsageAlarmThresholdHigh": wvEth10_100TxLinkUsageAlarmThresholdHigh,
       "wvEth10-100RxLinkUsageAlarmThresholdLow": wvEth10_100RxLinkUsageAlarmThresholdLow,
       "wvEth10-100RxLinkUsageAlarmThresholdHigh": wvEth10_100RxLinkUsageAlarmThresholdHigh,
       "wvEth10-100ThresholdMeasurementInterval": wvEth10_100ThresholdMeasurementInterval,
       "wvClearAlarmLog": wvClearAlarmLog,
       "wvComponentsRevisions": wvComponentsRevisions,
       "wvInstalledPlugInPartNo": wvInstalledPlugInPartNo,
       "wvInstalledPlugInHwRevision": wvInstalledPlugInHwRevision,
       "wvIduPartNo": wvIduPartNo,
       "wvIduHwRevision": wvIduHwRevision,
       "wvIduSwRevision": wvIduSwRevision,
       "wvIduLastSwUpdateTime": wvIduLastSwUpdateTime,
       "wvOduPartNo": wvOduPartNo,
       "wvOduHwRevision": wvOduHwRevision,
       "wvOduSwRevision": wvOduSwRevision,
       "wvOduLastSwUpdateTime": wvOduLastSwUpdateTime,
       "wvIpbHwRevision": wvIpbHwRevision,
       "wvBootSwRevision": wvBootSwRevision,
       "wvIduAlternetSwRevision": wvIduAlternetSwRevision,
       "wvOemId": wvOemId,
       "wvOemIduPartNo": wvOemIduPartNo,
       "wvOemOduPartNo": wvOemOduPartNo,
       "wvInstalledOemPlugInPartNo": wvInstalledOemPlugInPartNo,
       "wvStatusAndGauges": wvStatusAndGauges,
       "wvTelemetryStatus": wvTelemetryStatus,
       "wvOperatingSystemStatus": wvOperatingSystemStatus,
       "wvIduOduCableStatus": wvIduOduCableStatus,
       "wvIduStatus": wvIduStatus,
       "wvOduStatus": wvOduStatus,
       "wvRemoteTerminalStatus": wvRemoteTerminalStatus,
       "wvSlipModemStatus": wvSlipModemStatus,
       "wvSecurityStatus": wvSecurityStatus,
       "wvTftpDwnlStatus": wvTftpDwnlStatus,
       "wvLinkPerformanceAlarmsStatus": wvLinkPerformanceAlarmsStatus,
       "wvOperatingFrequency": wvOperatingFrequency,
       "wvFrequencyBand": wvFrequencyBand,
       "wvChannelSpacing": wvChannelSpacing,
       "wvTxPowerLevel": wvTxPowerLevel,
       "wvRxSignalLevel": wvRxSignalLevel,
       "wvFadeMargin": wvFadeMargin,
       "wvOduTemperature": wvOduTemperature,
       "wvLedState": wvLedState,
       "wvModemAfc": wvModemAfc,
       "wvRxPllFrequency": wvRxPllFrequency,
       "wvWorkingFrequency": wvWorkingFrequency,
       "wvMaxTxPowerSetting": wvMaxTxPowerSetting,
       "wvMinTxPowerSetting": wvMinTxPowerSetting,
       "wvOduSerialNumber": wvOduSerialNumber,
       "wvIduSerialNumber": wvIduSerialNumber,
       "wvOnePlusOneStatus": wvOnePlusOneStatus,
       "wvSupport2T1and2E1Status": wvSupport2T1and2E1Status,
       "wvLastUpdateConfigurationTimestamp": wvLastUpdateConfigurationTimestamp,
       "wvOemIduSerialNumber": wvOemIduSerialNumber,
       "wvOemOduSerialNumber": wvOemOduSerialNumber,
       "wvOnePlusOneConnectorType": wvOnePlusOneConnectorType,
       "wvLog": wvLog,
       "wvLogEventsElapsed": wvLogEventsElapsed,
       "wvLogEventTable": wvLogEventTable,
       "wvLogEventEntry": wvLogEventEntry,
       "wvLogEventLock": wvLogEventLock,
       "wvLogEventTime": wvLogEventTime,
       "wvLogEventStatus": wvLogEventStatus,
       "wvLogEventDescription": wvLogEventDescription,
       "wvPerformance": wvPerformance,
       "wvlinkBER": wvlinkBER,
       "wvlinkBLER": wvlinkBLER,
       "wvlinkBBER": wvlinkBBER,
       "wvlinkNCBLER": wvlinkNCBLER,
       "wvLinkESs": wvLinkESs,
       "wvLinkSESs": wvLinkSESs,
       "wvLinkUAs": wvLinkUAs,
       "wvLinkDMs": wvLinkDMs,
       "wvlinkAverageRSL": wvlinkAverageRSL,
       "wvlinkMaximumRSL": wvlinkMaximumRSL,
       "wvlinkMinimumRSL": wvlinkMinimumRSL,
       "wvLinkValidIntervals": wvLinkValidIntervals,
       "wvLinkCurrentESs": wvLinkCurrentESs,
       "wvLinkCurrentSESs": wvLinkCurrentSESs,
       "wvLinkCurrentUASs": wvLinkCurrentUASs,
       "wvLinkCurrentDMs": wvLinkCurrentDMs,
       "wvLinkCurrentBER": wvLinkCurrentBER,
       "wvLinkCurrentBLER": wvLinkCurrentBLER,
       "wvLinkCurrentBBER": wvLinkCurrentBBER,
       "wvLinkCurrentNCBLER": wvLinkCurrentNCBLER,
       "wvlinkCurrentAverageRSL": wvlinkCurrentAverageRSL,
       "wvlinkCurrentMaximumRSL": wvlinkCurrentMaximumRSL,
       "wvlinkCurrentMinimumRSL": wvlinkCurrentMinimumRSL,
       "wvlinkCurrentTimeElapsed": wvlinkCurrentTimeElapsed,
       "wvLinkIntervalTable": wvLinkIntervalTable,
       "wvLinkIntervalEntry": wvLinkIntervalEntry,
       "wvLinkIntervalNumber": wvLinkIntervalNumber,
       "wvLinkIntervalESs": wvLinkIntervalESs,
       "wvLinkIntervalSESs": wvLinkIntervalSESs,
       "wvLinkIntervalUASs": wvLinkIntervalUASs,
       "wvLinkIntervalDMs": wvLinkIntervalDMs,
       "wvLinkIntervalBER": wvLinkIntervalBER,
       "wvLinkIntervalBLER": wvLinkIntervalBLER,
       "wvLinkIntervalBBER": wvLinkIntervalBBER,
       "wvLinkIntervalNCBLER": wvLinkIntervalNCBLER,
       "wvlinkIntervalAverageRSL": wvlinkIntervalAverageRSL,
       "wvlinkIntervalMaximumRSL": wvlinkIntervalMaximumRSL,
       "wvlinkIntervalMinimumRSL": wvlinkIntervalMinimumRSL,
       "wvLinkTotalESs": wvLinkTotalESs,
       "wvLinkTotalSESs": wvLinkTotalSESs,
       "wvLinkTotalUASs": wvLinkTotalUASs,
       "wvLinkTotalDMs": wvLinkTotalDMs,
       "wvLinkTotalBER": wvLinkTotalBER,
       "wvLinkTotalBLER": wvLinkTotalBLER,
       "wvLinkTotalBBER": wvLinkTotalBBER,
       "wvLinkTotalNCBLER": wvLinkTotalNCBLER,
       "wvlinkTotalAverageRSL": wvlinkTotalAverageRSL,
       "wvlinkTotalMaximumRSL": wvlinkTotalMaximumRSL,
       "wvlinkTotalMinimumRSL": wvlinkTotalMinimumRSL,
       "wvlinkNoOfReceivedKBits": wvlinkNoOfReceivedKBits,
       "wvlinkNoOfErrors": wvlinkNoOfErrors,
       "wvlinkErroredBlocks": wvlinkErroredBlocks,
       "wvlinkNotCorrectedErroredBlocks": wvlinkNotCorrectedErroredBlocks,
       "wvLinkPerformanceCountTime": wvLinkPerformanceCountTime,
       "wvlinkInstantaneousBER": wvlinkInstantaneousBER,
       "wvEth10-100TxLinkUsage": wvEth10_100TxLinkUsage,
       "wvEth10-100RxLinkUsage": wvEth10_100RxLinkUsage,
       "wvEth10-100TxLinkUtilization": wvEth10_100TxLinkUtilization,
       "wvEth10-100RxLinkUtilization": wvEth10_100RxLinkUtilization,
       "wvTests": wvTests,
       "wvLoopbackType": wvLoopbackType,
       "wvLoopbackStartTime": wvLoopbackStartTime,
       "wvLoopbackTimePeriod": wvLoopbackTimePeriod,
       "wvLoopbackRemainingStartTime": wvLoopbackRemainingStartTime,
       "wvLoopbackRemainingTimePeriod": wvLoopbackRemainingTimePeriod,
       "wvSelfTestType": wvSelfTestType,
       "wvSelfTestStartTime": wvSelfTestStartTime,
       "wvLastSelfTestStartTime": wvLastSelfTestStartTime,
       "wvLastSelfTestTable": wvLastSelfTestTable,
       "wvLastSelfTestEntry": wvLastSelfTestEntry,
       "wvLastSelfTestType": wvLastSelfTestType,
       "wvLastSelfTestStatus": wvLastSelfTestStatus,
       "wvSelfTestRemainingStartTime": wvSelfTestRemainingStartTime,
       "wvInsertTestSignalLine": wvInsertTestSignalLine,
       "wvInsertTestSignalStartTime": wvInsertTestSignalStartTime,
       "wvInsertTestSignalTimePeriod": wvInsertTestSignalTimePeriod,
       "wvLastTestSignalTime": wvLastTestSignalTime,
       "wvLastTestSignalBER": wvLastTestSignalBER,
       "wvInsertTestSignalRemainingStartTime": wvInsertTestSignalRemainingStartTime,
       "wvInsertTestSignalRemainingTimePeriod": wvInsertTestSignalRemainingTimePeriod,
       "wvGenericDiagnosticsParameterAddress": wvGenericDiagnosticsParameterAddress,
       "wvGenericDiagnosticsParameterValue": wvGenericDiagnosticsParameterValue,
       "wvTraps": wvTraps,
       "wvTraps0": wvTraps0,
       "wvIduOduCableFaultStart": wvIduOduCableFaultStart,
       "wvIduOduCableFaultStop": wvIduOduCableFaultStop,
       "wvIduInternalFaultStart": wvIduInternalFaultStart,
       "wvIduInternalFaultStop": wvIduInternalFaultStop,
       "wvOduInternalFaultStart": wvOduInternalFaultStart,
       "wvOduInternalFaultStop": wvOduInternalFaultStop,
       "wvLinkDownStart": wvLinkDownStart,
       "wvLinkDownStop": wvLinkDownStop,
       "wvIdViolationStart": wvIdViolationStart,
       "wvIdViolationStop": wvIdViolationStop,
       "wvRemoteAccessStart": wvRemoteAccessStart,
       "wvRemoteAccessStop": wvRemoteAccessStop,
       "wvLocalOduAccessStart": wvLocalOduAccessStart,
       "wvLocalOduAccessStop": wvLocalOduAccessStop,
       "wvReceiveSignalLowerLevelStart": wvReceiveSignalLowerLevelStart,
       "wvReceiveSignalLowerLevelStop": wvReceiveSignalLowerLevelStop,
       "wvRelayStart": wvRelayStart,
       "wvRelayStop": wvRelayStop,
       "wvLineAisStart": wvLineAisStart,
       "wvLineAisStop": wvLineAisStop,
       "wvLineLosStart": wvLineLosStart,
       "wvLineLosStop": wvLineLosStop,
       "wvBerWarningStart": wvBerWarningStart,
       "wvBerWarningStop": wvBerWarningStop,
       "wvBerFatalStart": wvBerFatalStart,
       "wvBerFatalStop": wvBerFatalStop,
       "wvExternalInputsStart": wvExternalInputsStart,
       "wvExternalInputsStop": wvExternalInputsStop,
       "wvLinkUasStart": wvLinkUasStart,
       "wvLinkUasStop": wvLinkUasStop,
       "wvTftpFail": wvTftpFail,
       "wvTftpSuccess": wvTftpSuccess,
       "wvOduTempViolationStart": wvOduTempViolationStart,
       "wvOduTempViolationStop": wvOduTempViolationStop,
       "wvOduTxMuteStart": wvOduTxMuteStart,
       "wvOduTxMuteStop": wvOduTxMuteStop,
       "wvIduPowerSupplyStart": wvIduPowerSupplyStart,
       "wvIduPowerSupplyStop": wvIduPowerSupplyStop,
       "wvIduConfigurationMismatch": wvIduConfigurationMismatch,
       "wvIduBankSwitchover": wvIduBankSwitchover,
       "wvIduPortLoopbackStart": wvIduPortLoopbackStart,
       "wvIduPortLoopbackStop": wvIduPortLoopbackStop,
       "wvIduPortBertStart": wvIduPortBertStart,
       "wvIduPortBertStop": wvIduPortBertStop,
       "wvIduHeartBit": wvIduHeartBit,
       "wvAisReceiveStart": wvAisReceiveStart,
       "wvAisReceiveStop": wvAisReceiveStop,
       "wlEth10x100RxLinkUsageLowStart": wlEth10x100RxLinkUsageLowStart,
       "wlEth10x100RxLinkUsageLowStop": wlEth10x100RxLinkUsageLowStop,
       "wlEth10x100RxLinkUsageHighStart": wlEth10x100RxLinkUsageHighStart,
       "wlEth10x100RxLinkUsageHighStop": wlEth10x100RxLinkUsageHighStop,
       "wlEth10x100TxLinkUsageLowStart": wlEth10x100TxLinkUsageLowStart,
       "wlEth10x100TxLinkUsageLowStop": wlEth10x100TxLinkUsageLowStop,
       "wlEth10x100TxLinkUsageHighStart": wlEth10x100TxLinkUsageHighStart,
       "wlEth10x100TxLinkUsageHighStop": wlEth10x100TxLinkUsageHighStop,
       "wvTrapVars": wvTrapVars,
       "wvTrapKeepAlivePeriod": wvTrapKeepAlivePeriod,
       "wvAisPortTrap": wvAisPortTrap,
       "wvLosPortTrap": wvLosPortTrap,
       "wvExternalInputTrap": wvExternalInputTrap,
       "wvRelayIdTrap": wvRelayIdTrap,
       "wvSelectTrapVector": wvSelectTrapVector,
       "wvTrapKeepAliveVarsSelect": wvTrapKeepAliveVarsSelect,
       "wvTrapKeepAliveString": wvTrapKeepAliveString}
)
