# SNMP MIB module (CISCO-OPTICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OPTICAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:23 2024
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

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoOpticalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 828)
)
ciscoOpticalMIB.setRevisions(
        ("2016-05-24 00:00",
         "2015-12-01 00:00",
         "2015-10-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CoiOpticalPower(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 3000),
    )



class CoiOpticalWavelength(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1528770, 1604030),
    )



class CoiIntervalType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMin", 1),
          ("oneDay", 2),
          ("thirtySecond", 3))
    )



class CoiPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientPort", 1),
          ("trunkPort", 2))
    )



class CoiOptAlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmUnknown", 1),
          ("equipmentFailure", 2))
    )



class CoiOptAlarmSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("notAlarmed", 2),
          ("notReported", 1))
    )



class CoiOptAlarmStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 2),
          ("raised", 1),
          ("transient", 3))
    )



class CoiOptAlarmServiceAffecting(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonServiceAffecting", 2),
          ("serviceAffecting", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoOpticalMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoOpticalMIBNotifs = _CiscoOpticalMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 0)
)
_CiscoOpticalMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOpticalMIBObjects = _CiscoOpticalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1)
)
_CoiOpticalController_ObjectIdentity = ObjectIdentity
coiOpticalController = _CoiOpticalController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1)
)
_CoiOpticalNotifEnabled_Type = TruthValue
_CoiOpticalNotifEnabled_Object = MibScalar
coiOpticalNotifEnabled = _CoiOpticalNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 1),
    _CoiOpticalNotifEnabled_Type()
)
coiOpticalNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalNotifEnabled.setStatus("current")
_CoiOpticalControllerTable_Object = MibTable
coiOpticalControllerTable = _CoiOpticalControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2)
)
if mibBuilder.loadTexts:
    coiOpticalControllerTable.setStatus("current")
_CoiOpticalControllerEntry_Object = MibTableRow
coiOpticalControllerEntry = _CoiOpticalControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1)
)
coiOpticalControllerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coiOpticalControllerEntry.setStatus("current")


class _CoiOpticalControllerWavelength_Type(CoiOpticalWavelength):
    """Custom type coiOpticalControllerWavelength based on CoiOpticalWavelength"""
    defaultValue = 1529553


_CoiOpticalControllerWavelength_Object = MibTableColumn
coiOpticalControllerWavelength = _CoiOpticalControllerWavelength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 1),
    _CoiOpticalControllerWavelength_Type()
)
coiOpticalControllerWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerWavelength.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerWavelength.setUnits("1/100 nm")


class _CoiOpticalControllerLaserStatus_Type(Integer32):
    """Custom type coiOpticalControllerLaserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CoiOpticalControllerLaserStatus_Type.__name__ = "Integer32"
_CoiOpticalControllerLaserStatus_Object = MibTableColumn
coiOpticalControllerLaserStatus = _CoiOpticalControllerLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 2),
    _CoiOpticalControllerLaserStatus_Type()
)
coiOpticalControllerLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerLaserStatus.setStatus("current")
_CoiOpticalControllerFrequency_Type = Unsigned32
_CoiOpticalControllerFrequency_Object = MibTableColumn
coiOpticalControllerFrequency = _CoiOpticalControllerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 3),
    _CoiOpticalControllerFrequency_Type()
)
coiOpticalControllerFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerFrequency.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerFrequency.setUnits("100 MHz")
_CoiOpticalControllerChannelNumber_Type = Unsigned32
_CoiOpticalControllerChannelNumber_Object = MibTableColumn
coiOpticalControllerChannelNumber = _CoiOpticalControllerChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 4),
    _CoiOpticalControllerChannelNumber_Type()
)
coiOpticalControllerChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerChannelNumber.setStatus("current")
_CoiOpticalControllerTransmitPower_Type = CoiOpticalPower
_CoiOpticalControllerTransmitPower_Object = MibTableColumn
coiOpticalControllerTransmitPower = _CoiOpticalControllerTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 5),
    _CoiOpticalControllerTransmitPower_Type()
)
coiOpticalControllerTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerTransmitPower.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerTransmitPower.setUnits("1/100 dBm")
_CoiOpticalControllerOpticsType_Type = DisplayString
_CoiOpticalControllerOpticsType_Object = MibTableColumn
coiOpticalControllerOpticsType = _CoiOpticalControllerOpticsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 6),
    _CoiOpticalControllerOpticsType_Type()
)
coiOpticalControllerOpticsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerOpticsType.setStatus("current")
_CoiOpticalControllerRXLowThreshold_Type = CoiOpticalPower
_CoiOpticalControllerRXLowThreshold_Object = MibTableColumn
coiOpticalControllerRXLowThreshold = _CoiOpticalControllerRXLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 7),
    _CoiOpticalControllerRXLowThreshold_Type()
)
coiOpticalControllerRXLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerRXLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerRXLowThreshold.setUnits("1/100 dBm")
_CoiOpticalControllerTXLowThreshold_Type = CoiOpticalPower
_CoiOpticalControllerTXLowThreshold_Object = MibTableColumn
coiOpticalControllerTXLowThreshold = _CoiOpticalControllerTXLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 8),
    _CoiOpticalControllerTXLowThreshold_Type()
)
coiOpticalControllerTXLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerTXLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerTXLowThreshold.setUnits("1/100 dBm")
_CoiOpticalControllerRXHighThreshold_Type = CoiOpticalPower
_CoiOpticalControllerRXHighThreshold_Object = MibTableColumn
coiOpticalControllerRXHighThreshold = _CoiOpticalControllerRXHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 9),
    _CoiOpticalControllerRXHighThreshold_Type()
)
coiOpticalControllerRXHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerRXHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerRXHighThreshold.setUnits("1/100 dBm")
_CoiOpticalControllerTXHighThreshold_Type = CoiOpticalPower
_CoiOpticalControllerTXHighThreshold_Object = MibTableColumn
coiOpticalControllerTXHighThreshold = _CoiOpticalControllerTXHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 10),
    _CoiOpticalControllerTXHighThreshold_Type()
)
coiOpticalControllerTXHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerTXHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerTXHighThreshold.setUnits("1/100 dBm")


class _CoiOpticalControllerLBCHighThreshold_Type(Integer32):
    """Custom type coiOpticalControllerLBCHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CoiOpticalControllerLBCHighThreshold_Type.__name__ = "Integer32"
_CoiOpticalControllerLBCHighThreshold_Object = MibTableColumn
coiOpticalControllerLBCHighThreshold = _CoiOpticalControllerLBCHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 11),
    _CoiOpticalControllerLBCHighThreshold_Type()
)
coiOpticalControllerLBCHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerLBCHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerLBCHighThreshold.setUnits("1/10 %")


class _CoiOpticalControllerStatus_Type(Bits):
    """Custom type coiOpticalControllerStatus based on Bits"""
    namedValues = NamedValues(
        *(("highDGD", 9),
          ("highLBC", 8),
          ("highLaserTemp", 13),
          ("highRXPwr", 4),
          ("highTXPwr", 5),
          ("improprmvl", 1),
          ("lowLaserTemp", 14),
          ("lowOSNR", 11),
          ("lowRXPwr", 6),
          ("lowTXPwr", 7),
          ("mea", 2),
          ("noDefect", 0),
          ("outOfRangeCD", 10),
          ("ppmFail", 15),
          ("provMismatch", 3),
          ("wvlOutOfLock", 12))
    )

_CoiOpticalControllerStatus_Type.__name__ = "Bits"
_CoiOpticalControllerStatus_Object = MibTableColumn
coiOpticalControllerStatus = _CoiOpticalControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 12),
    _CoiOpticalControllerStatus_Type()
)
coiOpticalControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerStatus.setStatus("current")
_CoiOpticalControllerPortType_Type = CoiPortType
_CoiOpticalControllerPortType_Object = MibTableColumn
coiOpticalControllerPortType = _CoiOpticalControllerPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 13),
    _CoiOpticalControllerPortType_Type()
)
coiOpticalControllerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPortType.setStatus("current")
_CoiOpticalControllerTotalRXPower_Type = CoiOpticalPower
_CoiOpticalControllerTotalRXPower_Object = MibTableColumn
coiOpticalControllerTotalRXPower = _CoiOpticalControllerTotalRXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 14),
    _CoiOpticalControllerTotalRXPower_Type()
)
coiOpticalControllerTotalRXPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerTotalRXPower.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerTotalRXPower.setUnits("1/100 dBm")
_CoiOpticalControllerTotalTXPower_Type = CoiOpticalPower
_CoiOpticalControllerTotalTXPower_Object = MibTableColumn
coiOpticalControllerTotalTXPower = _CoiOpticalControllerTotalTXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 2, 1, 15),
    _CoiOpticalControllerTotalTXPower_Type()
)
coiOpticalControllerTotalTXPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOpticalControllerTotalTXPower.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerTotalTXPower.setUnits("1/100 dBm")
_CoiOpticalControllerPerLaneTable_Object = MibTable
coiOpticalControllerPerLaneTable = _CoiOpticalControllerPerLaneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3)
)
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneTable.setStatus("current")
_CoiOpticalControllerPerLaneEntry_Object = MibTableRow
coiOpticalControllerPerLaneEntry = _CoiOpticalControllerPerLaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1)
)
coiOpticalControllerPerLaneEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-MIB", "coiOpticalControllerLane"),
)
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneEntry.setStatus("current")


class _CoiOpticalControllerLane_Type(Integer32):
    """Custom type coiOpticalControllerLane based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CoiOpticalControllerLane_Type.__name__ = "Integer32"
_CoiOpticalControllerLane_Object = MibTableColumn
coiOpticalControllerLane = _CoiOpticalControllerLane_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 1),
    _CoiOpticalControllerLane_Type()
)
coiOpticalControllerLane.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOpticalControllerLane.setStatus("current")
_CoiOpticalControllerPerLaneRXPower_Type = CoiOpticalPower
_CoiOpticalControllerPerLaneRXPower_Object = MibTableColumn
coiOpticalControllerPerLaneRXPower = _CoiOpticalControllerPerLaneRXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 2),
    _CoiOpticalControllerPerLaneRXPower_Type()
)
coiOpticalControllerPerLaneRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneRXPower.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneRXPower.setUnits("1/100 dBm")
_CoiOpticalControllerPerLaneTXPower_Type = CoiOpticalPower
_CoiOpticalControllerPerLaneTXPower_Object = MibTableColumn
coiOpticalControllerPerLaneTXPower = _CoiOpticalControllerPerLaneTXPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 3),
    _CoiOpticalControllerPerLaneTXPower_Type()
)
coiOpticalControllerPerLaneTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneTXPower.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneTXPower.setUnits("1/100 dBm")


class _CoiOpticalControllerPerLaneLBC_Type(Integer32):
    """Custom type coiOpticalControllerPerLaneLBC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CoiOpticalControllerPerLaneLBC_Type.__name__ = "Integer32"
_CoiOpticalControllerPerLaneLBC_Object = MibTableColumn
coiOpticalControllerPerLaneLBC = _CoiOpticalControllerPerLaneLBC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 4),
    _CoiOpticalControllerPerLaneLBC_Type()
)
coiOpticalControllerPerLaneLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneLBC.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneLBC.setUnits("1/10 %")
_CoiOpticalControllerPerLaneOSNR_Type = Integer32
_CoiOpticalControllerPerLaneOSNR_Object = MibTableColumn
coiOpticalControllerPerLaneOSNR = _CoiOpticalControllerPerLaneOSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 5),
    _CoiOpticalControllerPerLaneOSNR_Type()
)
coiOpticalControllerPerLaneOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneOSNR.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneOSNR.setUnits("1/100 dB")
_CoiOpticalControllerPerLaneChromaticDispersion_Type = Integer32
_CoiOpticalControllerPerLaneChromaticDispersion_Object = MibTableColumn
coiOpticalControllerPerLaneChromaticDispersion = _CoiOpticalControllerPerLaneChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 6),
    _CoiOpticalControllerPerLaneChromaticDispersion_Type()
)
coiOpticalControllerPerLaneChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneChromaticDispersion.setUnits("ps/nm")
_CoiOpticalControllerPerLaneDifferentialGroupDelay_Type = Integer32
_CoiOpticalControllerPerLaneDifferentialGroupDelay_Object = MibTableColumn
coiOpticalControllerPerLaneDifferentialGroupDelay = _CoiOpticalControllerPerLaneDifferentialGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 7),
    _CoiOpticalControllerPerLaneDifferentialGroupDelay_Type()
)
coiOpticalControllerPerLaneDifferentialGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneDifferentialGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneDifferentialGroupDelay.setUnits("1/100 ps")
_CoiOpticalControllerPerLaneSecondOrderPMD_Type = Integer32
_CoiOpticalControllerPerLaneSecondOrderPMD_Object = MibTableColumn
coiOpticalControllerPerLaneSecondOrderPMD = _CoiOpticalControllerPerLaneSecondOrderPMD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 8),
    _CoiOpticalControllerPerLaneSecondOrderPMD_Type()
)
coiOpticalControllerPerLaneSecondOrderPMD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneSecondOrderPMD.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneSecondOrderPMD.setUnits("1/100 ps^2")
_CoiOpticalControllerPerLanePolarizationDependentLoss_Type = Integer32
_CoiOpticalControllerPerLanePolarizationDependentLoss_Object = MibTableColumn
coiOpticalControllerPerLanePolarizationDependentLoss = _CoiOpticalControllerPerLanePolarizationDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 9),
    _CoiOpticalControllerPerLanePolarizationDependentLoss_Type()
)
coiOpticalControllerPerLanePolarizationDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLanePolarizationDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLanePolarizationDependentLoss.setUnits("1/100 dB")
_CoiOpticalControllerPerLanePolarizationChangeRate_Type = Integer32
_CoiOpticalControllerPerLanePolarizationChangeRate_Object = MibTableColumn
coiOpticalControllerPerLanePolarizationChangeRate = _CoiOpticalControllerPerLanePolarizationChangeRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 10),
    _CoiOpticalControllerPerLanePolarizationChangeRate_Type()
)
coiOpticalControllerPerLanePolarizationChangeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLanePolarizationChangeRate.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLanePolarizationChangeRate.setUnits("1/100 rad/s")
_CoiOpticalControllerPerLanePhaseNoise_Type = Integer32
_CoiOpticalControllerPerLanePhaseNoise_Object = MibTableColumn
coiOpticalControllerPerLanePhaseNoise = _CoiOpticalControllerPerLanePhaseNoise_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 1, 3, 1, 11),
    _CoiOpticalControllerPerLanePhaseNoise_Type()
)
coiOpticalControllerPerLanePhaseNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLanePhaseNoise.setStatus("current")
if mibBuilder.loadTexts:
    coiOpticalControllerPerLanePhaseNoise.setUnits("1/1000 dB")
_CoiOpticalPerformanceMonitoring_ObjectIdentity = ObjectIdentity
coiOpticalPerformanceMonitoring = _CoiOpticalPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2)
)
_CoiOpticalThresholdTable_Object = MibTable
coiOpticalThresholdTable = _CoiOpticalThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coiOpticalThresholdTable.setStatus("current")
_CoiOpticalThresholdEntry_Object = MibTableRow
coiOpticalThresholdEntry = _CoiOpticalThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1)
)
coiOpticalThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-MIB", "coiOptThreshIntervalType"),
)
if mibBuilder.loadTexts:
    coiOpticalThresholdEntry.setStatus("current")
_CoiOptThreshIntervalType_Type = CoiIntervalType
_CoiOptThreshIntervalType_Object = MibTableColumn
coiOptThreshIntervalType = _CoiOptThreshIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 1),
    _CoiOptThreshIntervalType_Type()
)
coiOptThreshIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOptThreshIntervalType.setStatus("current")
_CoiOptThreshTXPowerMin_Type = CoiOpticalPower
_CoiOptThreshTXPowerMin_Object = MibTableColumn
coiOptThreshTXPowerMin = _CoiOptThreshTXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 2),
    _CoiOptThreshTXPowerMin_Type()
)
coiOptThreshTXPowerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshTXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshTXPowerMin.setUnits("1/100 dBm")
_CoiOptThreshRXPowerMin_Type = CoiOpticalPower
_CoiOptThreshRXPowerMin_Object = MibTableColumn
coiOptThreshRXPowerMin = _CoiOptThreshRXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 3),
    _CoiOptThreshRXPowerMin_Type()
)
coiOptThreshRXPowerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshRXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshRXPowerMin.setUnits("1/100 dBm")
_CoiOptThreshOSNRMin_Type = Integer32
_CoiOptThreshOSNRMin_Object = MibTableColumn
coiOptThreshOSNRMin = _CoiOptThreshOSNRMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 4),
    _CoiOptThreshOSNRMin_Type()
)
coiOptThreshOSNRMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshOSNRMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshOSNRMin.setUnits("1/100 dB")
_CoiOptThreshChromaticDispersionMin_Type = Integer32
_CoiOptThreshChromaticDispersionMin_Object = MibTableColumn
coiOptThreshChromaticDispersionMin = _CoiOptThreshChromaticDispersionMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 5),
    _CoiOptThreshChromaticDispersionMin_Type()
)
coiOptThreshChromaticDispersionMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshChromaticDispersionMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshChromaticDispersionMin.setUnits("ps/nm")
_CoiOptThreshDifferentialGroupDelayMin_Type = Integer32
_CoiOptThreshDifferentialGroupDelayMin_Object = MibTableColumn
coiOptThreshDifferentialGroupDelayMin = _CoiOptThreshDifferentialGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 6),
    _CoiOptThreshDifferentialGroupDelayMin_Type()
)
coiOptThreshDifferentialGroupDelayMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshDifferentialGroupDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshDifferentialGroupDelayMin.setUnits("1/100 ps")
_CoiOptThreshSecondOrderPMDMin_Type = Integer32
_CoiOptThreshSecondOrderPMDMin_Object = MibTableColumn
coiOptThreshSecondOrderPMDMin = _CoiOptThreshSecondOrderPMDMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 7),
    _CoiOptThreshSecondOrderPMDMin_Type()
)
coiOptThreshSecondOrderPMDMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshSecondOrderPMDMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshSecondOrderPMDMin.setUnits("1/100 ps^2")
_CoiOptThreshPolarizationDependentLossMin_Type = Integer32
_CoiOptThreshPolarizationDependentLossMin_Object = MibTableColumn
coiOptThreshPolarizationDependentLossMin = _CoiOptThreshPolarizationDependentLossMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 8),
    _CoiOptThreshPolarizationDependentLossMin_Type()
)
coiOptThreshPolarizationDependentLossMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationDependentLossMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationDependentLossMin.setUnits("1/100 dB")
_CoiOptThreshPolarizationChangeRateMin_Type = Integer32
_CoiOptThreshPolarizationChangeRateMin_Object = MibTableColumn
coiOptThreshPolarizationChangeRateMin = _CoiOptThreshPolarizationChangeRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 9),
    _CoiOptThreshPolarizationChangeRateMin_Type()
)
coiOptThreshPolarizationChangeRateMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationChangeRateMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationChangeRateMin.setUnits("1/100 rad/s")
_CoiOptThreshPhaseNoiseMin_Type = Integer32
_CoiOptThreshPhaseNoiseMin_Object = MibTableColumn
coiOptThreshPhaseNoiseMin = _CoiOptThreshPhaseNoiseMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 10),
    _CoiOptThreshPhaseNoiseMin_Type()
)
coiOptThreshPhaseNoiseMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPhaseNoiseMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshPhaseNoiseMin.setUnits("1/1000 dB")


class _CoiOptThreshLBCMin_Type(Integer32):
    """Custom type coiOptThreshLBCMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CoiOptThreshLBCMin_Type.__name__ = "Integer32"
_CoiOptThreshLBCMin_Object = MibTableColumn
coiOptThreshLBCMin = _CoiOptThreshLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 11),
    _CoiOptThreshLBCMin_Type()
)
coiOptThreshLBCMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshLBCMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshLBCMin.setUnits("1/10 %")
_CoiOptThreshTXPowerMax_Type = CoiOpticalPower
_CoiOptThreshTXPowerMax_Object = MibTableColumn
coiOptThreshTXPowerMax = _CoiOptThreshTXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 12),
    _CoiOptThreshTXPowerMax_Type()
)
coiOptThreshTXPowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshTXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshTXPowerMax.setUnits("1/100 dBm")
_CoiOptThreshRXPowerMax_Type = CoiOpticalPower
_CoiOptThreshRXPowerMax_Object = MibTableColumn
coiOptThreshRXPowerMax = _CoiOptThreshRXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 13),
    _CoiOptThreshRXPowerMax_Type()
)
coiOptThreshRXPowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshRXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshRXPowerMax.setUnits("1/100 dBm")
_CoiOptThreshOSNRMax_Type = Integer32
_CoiOptThreshOSNRMax_Object = MibTableColumn
coiOptThreshOSNRMax = _CoiOptThreshOSNRMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 14),
    _CoiOptThreshOSNRMax_Type()
)
coiOptThreshOSNRMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshOSNRMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshOSNRMax.setUnits("1/100 dB")
_CoiOptThreshChromaticDispersionMax_Type = Integer32
_CoiOptThreshChromaticDispersionMax_Object = MibTableColumn
coiOptThreshChromaticDispersionMax = _CoiOptThreshChromaticDispersionMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 15),
    _CoiOptThreshChromaticDispersionMax_Type()
)
coiOptThreshChromaticDispersionMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshChromaticDispersionMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshChromaticDispersionMax.setUnits("ps/nm")
_CoiOptThreshDifferentialGroupDelayMax_Type = Integer32
_CoiOptThreshDifferentialGroupDelayMax_Object = MibTableColumn
coiOptThreshDifferentialGroupDelayMax = _CoiOptThreshDifferentialGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 16),
    _CoiOptThreshDifferentialGroupDelayMax_Type()
)
coiOptThreshDifferentialGroupDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshDifferentialGroupDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshDifferentialGroupDelayMax.setUnits("1/100 ps")
_CoiOptThreshSecondOrderPMDMax_Type = Integer32
_CoiOptThreshSecondOrderPMDMax_Object = MibTableColumn
coiOptThreshSecondOrderPMDMax = _CoiOptThreshSecondOrderPMDMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 17),
    _CoiOptThreshSecondOrderPMDMax_Type()
)
coiOptThreshSecondOrderPMDMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshSecondOrderPMDMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshSecondOrderPMDMax.setUnits("1/100 ps^2")
_CoiOptThreshPolarizationDependentLossMax_Type = Integer32
_CoiOptThreshPolarizationDependentLossMax_Object = MibTableColumn
coiOptThreshPolarizationDependentLossMax = _CoiOptThreshPolarizationDependentLossMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 18),
    _CoiOptThreshPolarizationDependentLossMax_Type()
)
coiOptThreshPolarizationDependentLossMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationDependentLossMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationDependentLossMax.setUnits("1/100 dB")
_CoiOptThreshPolarizationChangeRateMax_Type = Integer32
_CoiOptThreshPolarizationChangeRateMax_Object = MibTableColumn
coiOptThreshPolarizationChangeRateMax = _CoiOptThreshPolarizationChangeRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 19),
    _CoiOptThreshPolarizationChangeRateMax_Type()
)
coiOptThreshPolarizationChangeRateMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationChangeRateMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationChangeRateMax.setUnits("1/100 rad/s")
_CoiOptThreshPhaseNoiseMax_Type = Integer32
_CoiOptThreshPhaseNoiseMax_Object = MibTableColumn
coiOptThreshPhaseNoiseMax = _CoiOptThreshPhaseNoiseMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 20),
    _CoiOptThreshPhaseNoiseMax_Type()
)
coiOptThreshPhaseNoiseMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPhaseNoiseMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshPhaseNoiseMax.setUnits("1/1000 dB")


class _CoiOptThreshLBCMax_Type(Integer32):
    """Custom type coiOptThreshLBCMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CoiOptThreshLBCMax_Type.__name__ = "Integer32"
_CoiOptThreshLBCMax_Object = MibTableColumn
coiOptThreshLBCMax = _CoiOptThreshLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 21),
    _CoiOptThreshLBCMax_Type()
)
coiOptThreshLBCMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshLBCMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptThreshLBCMax.setUnits("1/10 %")
_CoiOptThreshTXPowerEnableMin_Type = TruthValue
_CoiOptThreshTXPowerEnableMin_Object = MibTableColumn
coiOptThreshTXPowerEnableMin = _CoiOptThreshTXPowerEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 22),
    _CoiOptThreshTXPowerEnableMin_Type()
)
coiOptThreshTXPowerEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshTXPowerEnableMin.setStatus("current")
_CoiOptThreshRXPowerEnableMin_Type = TruthValue
_CoiOptThreshRXPowerEnableMin_Object = MibTableColumn
coiOptThreshRXPowerEnableMin = _CoiOptThreshRXPowerEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 23),
    _CoiOptThreshRXPowerEnableMin_Type()
)
coiOptThreshRXPowerEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshRXPowerEnableMin.setStatus("current")
_CoiOptThreshOSNREnableMin_Type = TruthValue
_CoiOptThreshOSNREnableMin_Object = MibTableColumn
coiOptThreshOSNREnableMin = _CoiOptThreshOSNREnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 24),
    _CoiOptThreshOSNREnableMin_Type()
)
coiOptThreshOSNREnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshOSNREnableMin.setStatus("current")
_CoiOptThreshChromaticDispersionEnableMin_Type = TruthValue
_CoiOptThreshChromaticDispersionEnableMin_Object = MibTableColumn
coiOptThreshChromaticDispersionEnableMin = _CoiOptThreshChromaticDispersionEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 25),
    _CoiOptThreshChromaticDispersionEnableMin_Type()
)
coiOptThreshChromaticDispersionEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshChromaticDispersionEnableMin.setStatus("current")
_CoiOptThreshDifferentialGroupDelayEnableMin_Type = TruthValue
_CoiOptThreshDifferentialGroupDelayEnableMin_Object = MibTableColumn
coiOptThreshDifferentialGroupDelayEnableMin = _CoiOptThreshDifferentialGroupDelayEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 26),
    _CoiOptThreshDifferentialGroupDelayEnableMin_Type()
)
coiOptThreshDifferentialGroupDelayEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshDifferentialGroupDelayEnableMin.setStatus("current")
_CoiOptThreshSecondOrderPMDEnableMin_Type = TruthValue
_CoiOptThreshSecondOrderPMDEnableMin_Object = MibTableColumn
coiOptThreshSecondOrderPMDEnableMin = _CoiOptThreshSecondOrderPMDEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 27),
    _CoiOptThreshSecondOrderPMDEnableMin_Type()
)
coiOptThreshSecondOrderPMDEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshSecondOrderPMDEnableMin.setStatus("current")
_CoiOptThreshPolarizationDependentLossEnableMin_Type = TruthValue
_CoiOptThreshPolarizationDependentLossEnableMin_Object = MibTableColumn
coiOptThreshPolarizationDependentLossEnableMin = _CoiOptThreshPolarizationDependentLossEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 28),
    _CoiOptThreshPolarizationDependentLossEnableMin_Type()
)
coiOptThreshPolarizationDependentLossEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationDependentLossEnableMin.setStatus("current")
_CoiOptThreshPolarizationChangeRateEnableMin_Type = TruthValue
_CoiOptThreshPolarizationChangeRateEnableMin_Object = MibTableColumn
coiOptThreshPolarizationChangeRateEnableMin = _CoiOptThreshPolarizationChangeRateEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 29),
    _CoiOptThreshPolarizationChangeRateEnableMin_Type()
)
coiOptThreshPolarizationChangeRateEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationChangeRateEnableMin.setStatus("current")
_CoiOptThreshPhaseNoiseEnableMin_Type = TruthValue
_CoiOptThreshPhaseNoiseEnableMin_Object = MibTableColumn
coiOptThreshPhaseNoiseEnableMin = _CoiOptThreshPhaseNoiseEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 30),
    _CoiOptThreshPhaseNoiseEnableMin_Type()
)
coiOptThreshPhaseNoiseEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPhaseNoiseEnableMin.setStatus("current")
_CoiOptThreshLBCEnableMin_Type = TruthValue
_CoiOptThreshLBCEnableMin_Object = MibTableColumn
coiOptThreshLBCEnableMin = _CoiOptThreshLBCEnableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 31),
    _CoiOptThreshLBCEnableMin_Type()
)
coiOptThreshLBCEnableMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshLBCEnableMin.setStatus("current")
_CoiOptThreshTXPowerEnableMax_Type = TruthValue
_CoiOptThreshTXPowerEnableMax_Object = MibTableColumn
coiOptThreshTXPowerEnableMax = _CoiOptThreshTXPowerEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 32),
    _CoiOptThreshTXPowerEnableMax_Type()
)
coiOptThreshTXPowerEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshTXPowerEnableMax.setStatus("current")
_CoiOptThreshRXPowerEnableMax_Type = TruthValue
_CoiOptThreshRXPowerEnableMax_Object = MibTableColumn
coiOptThreshRXPowerEnableMax = _CoiOptThreshRXPowerEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 33),
    _CoiOptThreshRXPowerEnableMax_Type()
)
coiOptThreshRXPowerEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshRXPowerEnableMax.setStatus("current")
_CoiOptThreshOSNREnableMax_Type = TruthValue
_CoiOptThreshOSNREnableMax_Object = MibTableColumn
coiOptThreshOSNREnableMax = _CoiOptThreshOSNREnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 34),
    _CoiOptThreshOSNREnableMax_Type()
)
coiOptThreshOSNREnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshOSNREnableMax.setStatus("current")
_CoiOptThreshChromaticDispersionEnableMax_Type = TruthValue
_CoiOptThreshChromaticDispersionEnableMax_Object = MibTableColumn
coiOptThreshChromaticDispersionEnableMax = _CoiOptThreshChromaticDispersionEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 35),
    _CoiOptThreshChromaticDispersionEnableMax_Type()
)
coiOptThreshChromaticDispersionEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshChromaticDispersionEnableMax.setStatus("current")
_CoiOptThreshDifferentialGroupDelayEnableMax_Type = TruthValue
_CoiOptThreshDifferentialGroupDelayEnableMax_Object = MibTableColumn
coiOptThreshDifferentialGroupDelayEnableMax = _CoiOptThreshDifferentialGroupDelayEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 36),
    _CoiOptThreshDifferentialGroupDelayEnableMax_Type()
)
coiOptThreshDifferentialGroupDelayEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshDifferentialGroupDelayEnableMax.setStatus("current")
_CoiOptThreshSecondOrderPMDEnableMax_Type = TruthValue
_CoiOptThreshSecondOrderPMDEnableMax_Object = MibTableColumn
coiOptThreshSecondOrderPMDEnableMax = _CoiOptThreshSecondOrderPMDEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 37),
    _CoiOptThreshSecondOrderPMDEnableMax_Type()
)
coiOptThreshSecondOrderPMDEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshSecondOrderPMDEnableMax.setStatus("current")
_CoiOptThreshPolarizationDependentLossEnableMax_Type = TruthValue
_CoiOptThreshPolarizationDependentLossEnableMax_Object = MibTableColumn
coiOptThreshPolarizationDependentLossEnableMax = _CoiOptThreshPolarizationDependentLossEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 38),
    _CoiOptThreshPolarizationDependentLossEnableMax_Type()
)
coiOptThreshPolarizationDependentLossEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationDependentLossEnableMax.setStatus("current")
_CoiOptThreshPolarizationChangeRateEnableMax_Type = TruthValue
_CoiOptThreshPolarizationChangeRateEnableMax_Object = MibTableColumn
coiOptThreshPolarizationChangeRateEnableMax = _CoiOptThreshPolarizationChangeRateEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 39),
    _CoiOptThreshPolarizationChangeRateEnableMax_Type()
)
coiOptThreshPolarizationChangeRateEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPolarizationChangeRateEnableMax.setStatus("current")
_CoiOptThreshPhaseNoiseEnableMax_Type = TruthValue
_CoiOptThreshPhaseNoiseEnableMax_Object = MibTableColumn
coiOptThreshPhaseNoiseEnableMax = _CoiOptThreshPhaseNoiseEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 40),
    _CoiOptThreshPhaseNoiseEnableMax_Type()
)
coiOptThreshPhaseNoiseEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshPhaseNoiseEnableMax.setStatus("current")
_CoiOptThreshLBCEnableMax_Type = TruthValue
_CoiOptThreshLBCEnableMax_Object = MibTableColumn
coiOptThreshLBCEnableMax = _CoiOptThreshLBCEnableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 1, 1, 41),
    _CoiOptThreshLBCEnableMax_Type()
)
coiOptThreshLBCEnableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOptThreshLBCEnableMax.setStatus("current")
_CoiOpticalCurrentTable_Object = MibTable
coiOpticalCurrentTable = _CoiOpticalCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2)
)
if mibBuilder.loadTexts:
    coiOpticalCurrentTable.setStatus("current")
_CoiOpticalCurrentEntry_Object = MibTableRow
coiOpticalCurrentEntry = _CoiOpticalCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1)
)
coiOpticalCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-MIB", "coiOptCurrentLane"),
    (0, "CISCO-OPTICAL-MIB", "coiOptCurrentIntervalType"),
)
if mibBuilder.loadTexts:
    coiOpticalCurrentEntry.setStatus("current")


class _CoiOptCurrentLane_Type(Integer32):
    """Custom type coiOptCurrentLane based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CoiOptCurrentLane_Type.__name__ = "Integer32"
_CoiOptCurrentLane_Object = MibTableColumn
coiOptCurrentLane = _CoiOptCurrentLane_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 1),
    _CoiOptCurrentLane_Type()
)
coiOptCurrentLane.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOptCurrentLane.setStatus("current")
_CoiOptCurrentIntervalType_Type = CoiIntervalType
_CoiOptCurrentIntervalType_Object = MibTableColumn
coiOptCurrentIntervalType = _CoiOptCurrentIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 2),
    _CoiOptCurrentIntervalType_Type()
)
coiOptCurrentIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOptCurrentIntervalType.setStatus("current")
_CoiOptCurrentTXPowerMax_Type = CoiOpticalPower
_CoiOptCurrentTXPowerMax_Object = MibTableColumn
coiOptCurrentTXPowerMax = _CoiOptCurrentTXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 3),
    _CoiOptCurrentTXPowerMax_Type()
)
coiOptCurrentTXPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentTXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentTXPowerMax.setUnits("1/100 dBm")
_CoiOptCurrentRXPowerMax_Type = CoiOpticalPower
_CoiOptCurrentRXPowerMax_Object = MibTableColumn
coiOptCurrentRXPowerMax = _CoiOptCurrentRXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 4),
    _CoiOptCurrentRXPowerMax_Type()
)
coiOptCurrentRXPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentRXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentRXPowerMax.setUnits("1/100 dBm")
_CoiOptCurrentOSNRMax_Type = Integer32
_CoiOptCurrentOSNRMax_Object = MibTableColumn
coiOptCurrentOSNRMax = _CoiOptCurrentOSNRMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 5),
    _CoiOptCurrentOSNRMax_Type()
)
coiOptCurrentOSNRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentOSNRMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentOSNRMax.setUnits("1/100 dB")
_CoiOptCurrentChromaticDispersionMax_Type = Integer32
_CoiOptCurrentChromaticDispersionMax_Object = MibTableColumn
coiOptCurrentChromaticDispersionMax = _CoiOptCurrentChromaticDispersionMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 6),
    _CoiOptCurrentChromaticDispersionMax_Type()
)
coiOptCurrentChromaticDispersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentChromaticDispersionMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentChromaticDispersionMax.setUnits("ps/nm")
_CoiOptCurrentDifferentialGroupDelayMax_Type = Integer32
_CoiOptCurrentDifferentialGroupDelayMax_Object = MibTableColumn
coiOptCurrentDifferentialGroupDelayMax = _CoiOptCurrentDifferentialGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 7),
    _CoiOptCurrentDifferentialGroupDelayMax_Type()
)
coiOptCurrentDifferentialGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentDifferentialGroupDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentDifferentialGroupDelayMax.setUnits("1/100 ps")
_CoiOptCurrentSecondOrderPMDMax_Type = Integer32
_CoiOptCurrentSecondOrderPMDMax_Object = MibTableColumn
coiOptCurrentSecondOrderPMDMax = _CoiOptCurrentSecondOrderPMDMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 8),
    _CoiOptCurrentSecondOrderPMDMax_Type()
)
coiOptCurrentSecondOrderPMDMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentSecondOrderPMDMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentSecondOrderPMDMax.setUnits("1/100 ps^2")
_CoiOptCurrentPolarizationDependentLossMax_Type = Integer32
_CoiOptCurrentPolarizationDependentLossMax_Object = MibTableColumn
coiOptCurrentPolarizationDependentLossMax = _CoiOptCurrentPolarizationDependentLossMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 9),
    _CoiOptCurrentPolarizationDependentLossMax_Type()
)
coiOptCurrentPolarizationDependentLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationDependentLossMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationDependentLossMax.setUnits("1/100 dB")
_CoiOptCurrentPolarizationChangeRateMax_Type = Integer32
_CoiOptCurrentPolarizationChangeRateMax_Object = MibTableColumn
coiOptCurrentPolarizationChangeRateMax = _CoiOptCurrentPolarizationChangeRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 10),
    _CoiOptCurrentPolarizationChangeRateMax_Type()
)
coiOptCurrentPolarizationChangeRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationChangeRateMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationChangeRateMax.setUnits("1/100 rad/s")
_CoiOptCurrentPhaseNoiseMax_Type = Integer32
_CoiOptCurrentPhaseNoiseMax_Object = MibTableColumn
coiOptCurrentPhaseNoiseMax = _CoiOptCurrentPhaseNoiseMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 11),
    _CoiOptCurrentPhaseNoiseMax_Type()
)
coiOptCurrentPhaseNoiseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentPhaseNoiseMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentPhaseNoiseMax.setUnits("1/1000 dB")


class _CoiOptCurrentLBCMax_Type(Integer32):
    """Custom type coiOptCurrentLBCMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CoiOptCurrentLBCMax_Type.__name__ = "Integer32"
_CoiOptCurrentLBCMax_Object = MibTableColumn
coiOptCurrentLBCMax = _CoiOptCurrentLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 12),
    _CoiOptCurrentLBCMax_Type()
)
coiOptCurrentLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentLBCMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentLBCMax.setUnits("1/10 %")
_CoiOptCurrentTXPowerMin_Type = CoiOpticalPower
_CoiOptCurrentTXPowerMin_Object = MibTableColumn
coiOptCurrentTXPowerMin = _CoiOptCurrentTXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 13),
    _CoiOptCurrentTXPowerMin_Type()
)
coiOptCurrentTXPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentTXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentTXPowerMin.setUnits("1/100 dBm")
_CoiOptCurrentRXPowerMin_Type = CoiOpticalPower
_CoiOptCurrentRXPowerMin_Object = MibTableColumn
coiOptCurrentRXPowerMin = _CoiOptCurrentRXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 14),
    _CoiOptCurrentRXPowerMin_Type()
)
coiOptCurrentRXPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentRXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentRXPowerMin.setUnits("1/100 dBm")
_CoiOptCurrentOSNRMin_Type = Integer32
_CoiOptCurrentOSNRMin_Object = MibTableColumn
coiOptCurrentOSNRMin = _CoiOptCurrentOSNRMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 15),
    _CoiOptCurrentOSNRMin_Type()
)
coiOptCurrentOSNRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentOSNRMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentOSNRMin.setUnits("1/100 dB")
_CoiOptCurrentChromaticDispersionMin_Type = Integer32
_CoiOptCurrentChromaticDispersionMin_Object = MibTableColumn
coiOptCurrentChromaticDispersionMin = _CoiOptCurrentChromaticDispersionMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 16),
    _CoiOptCurrentChromaticDispersionMin_Type()
)
coiOptCurrentChromaticDispersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentChromaticDispersionMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentChromaticDispersionMin.setUnits("ps/nm")
_CoiOptCurrentDifferentialGroupDelayMin_Type = Integer32
_CoiOptCurrentDifferentialGroupDelayMin_Object = MibTableColumn
coiOptCurrentDifferentialGroupDelayMin = _CoiOptCurrentDifferentialGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 17),
    _CoiOptCurrentDifferentialGroupDelayMin_Type()
)
coiOptCurrentDifferentialGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentDifferentialGroupDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentDifferentialGroupDelayMin.setUnits("1/100 ps")
_CoiOptCurrentSecondOrderPMDMin_Type = Integer32
_CoiOptCurrentSecondOrderPMDMin_Object = MibTableColumn
coiOptCurrentSecondOrderPMDMin = _CoiOptCurrentSecondOrderPMDMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 18),
    _CoiOptCurrentSecondOrderPMDMin_Type()
)
coiOptCurrentSecondOrderPMDMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentSecondOrderPMDMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentSecondOrderPMDMin.setUnits("1/100 ps^2")
_CoiOptCurrentPolarizationDependentLossMin_Type = Integer32
_CoiOptCurrentPolarizationDependentLossMin_Object = MibTableColumn
coiOptCurrentPolarizationDependentLossMin = _CoiOptCurrentPolarizationDependentLossMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 19),
    _CoiOptCurrentPolarizationDependentLossMin_Type()
)
coiOptCurrentPolarizationDependentLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationDependentLossMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationDependentLossMin.setUnits("1/100 dB")
_CoiOptCurrentPolarizationChangeRateMin_Type = Integer32
_CoiOptCurrentPolarizationChangeRateMin_Object = MibTableColumn
coiOptCurrentPolarizationChangeRateMin = _CoiOptCurrentPolarizationChangeRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 20),
    _CoiOptCurrentPolarizationChangeRateMin_Type()
)
coiOptCurrentPolarizationChangeRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationChangeRateMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationChangeRateMin.setUnits("1/100 rad/s")
_CoiOptCurrentPhaseNoiseMin_Type = Integer32
_CoiOptCurrentPhaseNoiseMin_Object = MibTableColumn
coiOptCurrentPhaseNoiseMin = _CoiOptCurrentPhaseNoiseMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 21),
    _CoiOptCurrentPhaseNoiseMin_Type()
)
coiOptCurrentPhaseNoiseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentPhaseNoiseMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentPhaseNoiseMin.setUnits("1/1000 dB")


class _CoiOptCurrentLBCMin_Type(Integer32):
    """Custom type coiOptCurrentLBCMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CoiOptCurrentLBCMin_Type.__name__ = "Integer32"
_CoiOptCurrentLBCMin_Object = MibTableColumn
coiOptCurrentLBCMin = _CoiOptCurrentLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 22),
    _CoiOptCurrentLBCMin_Type()
)
coiOptCurrentLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentLBCMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentLBCMin.setUnits("1/10 %")
_CoiOptCurrentTXPowerAvg_Type = CoiOpticalPower
_CoiOptCurrentTXPowerAvg_Object = MibTableColumn
coiOptCurrentTXPowerAvg = _CoiOptCurrentTXPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 23),
    _CoiOptCurrentTXPowerAvg_Type()
)
coiOptCurrentTXPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentTXPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentTXPowerAvg.setUnits("1/100 dBm")
_CoiOptCurrentRXPowerAvg_Type = CoiOpticalPower
_CoiOptCurrentRXPowerAvg_Object = MibTableColumn
coiOptCurrentRXPowerAvg = _CoiOptCurrentRXPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 24),
    _CoiOptCurrentRXPowerAvg_Type()
)
coiOptCurrentRXPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentRXPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentRXPowerAvg.setUnits("1/100 dBm")
_CoiOptCurrentOSNRAvg_Type = Integer32
_CoiOptCurrentOSNRAvg_Object = MibTableColumn
coiOptCurrentOSNRAvg = _CoiOptCurrentOSNRAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 25),
    _CoiOptCurrentOSNRAvg_Type()
)
coiOptCurrentOSNRAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentOSNRAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentOSNRAvg.setUnits("1/100 dB")
_CoiOptCurrentChromaticDispersionAvg_Type = Integer32
_CoiOptCurrentChromaticDispersionAvg_Object = MibTableColumn
coiOptCurrentChromaticDispersionAvg = _CoiOptCurrentChromaticDispersionAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 26),
    _CoiOptCurrentChromaticDispersionAvg_Type()
)
coiOptCurrentChromaticDispersionAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentChromaticDispersionAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentChromaticDispersionAvg.setUnits("ps/nm")
_CoiOptCurrentDifferentialGroupDelayAvg_Type = Integer32
_CoiOptCurrentDifferentialGroupDelayAvg_Object = MibTableColumn
coiOptCurrentDifferentialGroupDelayAvg = _CoiOptCurrentDifferentialGroupDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 27),
    _CoiOptCurrentDifferentialGroupDelayAvg_Type()
)
coiOptCurrentDifferentialGroupDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentDifferentialGroupDelayAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentDifferentialGroupDelayAvg.setUnits("1/100 ps")
_CoiOptCurrentSecondOrderPMDAvg_Type = Integer32
_CoiOptCurrentSecondOrderPMDAvg_Object = MibTableColumn
coiOptCurrentSecondOrderPMDAvg = _CoiOptCurrentSecondOrderPMDAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 28),
    _CoiOptCurrentSecondOrderPMDAvg_Type()
)
coiOptCurrentSecondOrderPMDAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentSecondOrderPMDAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentSecondOrderPMDAvg.setUnits("1/100 ps^2")
_CoiOptCurrentPolarizationDependentLossAvg_Type = Integer32
_CoiOptCurrentPolarizationDependentLossAvg_Object = MibTableColumn
coiOptCurrentPolarizationDependentLossAvg = _CoiOptCurrentPolarizationDependentLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 29),
    _CoiOptCurrentPolarizationDependentLossAvg_Type()
)
coiOptCurrentPolarizationDependentLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationDependentLossAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationDependentLossAvg.setUnits("1/100 dB")
_CoiOptCurrentPolarizationChangeRateAvg_Type = Integer32
_CoiOptCurrentPolarizationChangeRateAvg_Object = MibTableColumn
coiOptCurrentPolarizationChangeRateAvg = _CoiOptCurrentPolarizationChangeRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 30),
    _CoiOptCurrentPolarizationChangeRateAvg_Type()
)
coiOptCurrentPolarizationChangeRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationChangeRateAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentPolarizationChangeRateAvg.setUnits("1/100 rad/s")
_CoiOptCurrentPhaseNoiseAvg_Type = Integer32
_CoiOptCurrentPhaseNoiseAvg_Object = MibTableColumn
coiOptCurrentPhaseNoiseAvg = _CoiOptCurrentPhaseNoiseAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 31),
    _CoiOptCurrentPhaseNoiseAvg_Type()
)
coiOptCurrentPhaseNoiseAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentPhaseNoiseAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentPhaseNoiseAvg.setUnits("1/1000 dB")


class _CoiOptCurrentLBCAvg_Type(Integer32):
    """Custom type coiOptCurrentLBCAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CoiOptCurrentLBCAvg_Type.__name__ = "Integer32"
_CoiOptCurrentLBCAvg_Object = MibTableColumn
coiOptCurrentLBCAvg = _CoiOptCurrentLBCAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 32),
    _CoiOptCurrentLBCAvg_Type()
)
coiOptCurrentLBCAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentLBCAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptCurrentLBCAvg.setUnits("1/10 %")
_CoiOptCurrentTimestamp_Type = OctetString
_CoiOptCurrentTimestamp_Object = MibTableColumn
coiOptCurrentTimestamp = _CoiOptCurrentTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 2, 1, 33),
    _CoiOptCurrentTimestamp_Type()
)
coiOptCurrentTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptCurrentTimestamp.setStatus("current")
_CoiOpticalIntervalTable_Object = MibTable
coiOpticalIntervalTable = _CoiOpticalIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3)
)
if mibBuilder.loadTexts:
    coiOpticalIntervalTable.setStatus("current")
_CoiOpticalIntervalEntry_Object = MibTableRow
coiOpticalIntervalEntry = _CoiOpticalIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1)
)
coiOpticalIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-MIB", "coiOptIntervalLane"),
    (0, "CISCO-OPTICAL-MIB", "coiOptIntervalIntervalType"),
    (0, "CISCO-OPTICAL-MIB", "coiOptIntervalNum"),
)
if mibBuilder.loadTexts:
    coiOpticalIntervalEntry.setStatus("current")


class _CoiOptIntervalLane_Type(Integer32):
    """Custom type coiOptIntervalLane based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CoiOptIntervalLane_Type.__name__ = "Integer32"
_CoiOptIntervalLane_Object = MibTableColumn
coiOptIntervalLane = _CoiOptIntervalLane_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 1),
    _CoiOptIntervalLane_Type()
)
coiOptIntervalLane.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOptIntervalLane.setStatus("current")
_CoiOptIntervalIntervalType_Type = CoiIntervalType
_CoiOptIntervalIntervalType_Object = MibTableColumn
coiOptIntervalIntervalType = _CoiOptIntervalIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 2),
    _CoiOptIntervalIntervalType_Type()
)
coiOptIntervalIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOptIntervalIntervalType.setStatus("current")


class _CoiOptIntervalNum_Type(Integer32):
    """Custom type coiOptIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CoiOptIntervalNum_Type.__name__ = "Integer32"
_CoiOptIntervalNum_Object = MibTableColumn
coiOptIntervalNum = _CoiOptIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 3),
    _CoiOptIntervalNum_Type()
)
coiOptIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOptIntervalNum.setStatus("current")
_CoiOptIntervalTXPowerMax_Type = CoiOpticalPower
_CoiOptIntervalTXPowerMax_Object = MibTableColumn
coiOptIntervalTXPowerMax = _CoiOptIntervalTXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 4),
    _CoiOptIntervalTXPowerMax_Type()
)
coiOptIntervalTXPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalTXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalTXPowerMax.setUnits("1/100 dBm")
_CoiOptIntervalRXPowerMax_Type = CoiOpticalPower
_CoiOptIntervalRXPowerMax_Object = MibTableColumn
coiOptIntervalRXPowerMax = _CoiOptIntervalRXPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 5),
    _CoiOptIntervalRXPowerMax_Type()
)
coiOptIntervalRXPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalRXPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalRXPowerMax.setUnits("1/100 dBm")
_CoiOptIntervalOSNRMax_Type = Integer32
_CoiOptIntervalOSNRMax_Object = MibTableColumn
coiOptIntervalOSNRMax = _CoiOptIntervalOSNRMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 6),
    _CoiOptIntervalOSNRMax_Type()
)
coiOptIntervalOSNRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalOSNRMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalOSNRMax.setUnits("1/100 dB")
_CoiOptIntervalChromaticDispersionMax_Type = Integer32
_CoiOptIntervalChromaticDispersionMax_Object = MibTableColumn
coiOptIntervalChromaticDispersionMax = _CoiOptIntervalChromaticDispersionMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 7),
    _CoiOptIntervalChromaticDispersionMax_Type()
)
coiOptIntervalChromaticDispersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalChromaticDispersionMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalChromaticDispersionMax.setUnits("ps/nm")
_CoiOptIntervalDifferentialGroupDelayMax_Type = Integer32
_CoiOptIntervalDifferentialGroupDelayMax_Object = MibTableColumn
coiOptIntervalDifferentialGroupDelayMax = _CoiOptIntervalDifferentialGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 8),
    _CoiOptIntervalDifferentialGroupDelayMax_Type()
)
coiOptIntervalDifferentialGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalDifferentialGroupDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalDifferentialGroupDelayMax.setUnits("1/100 ps")
_CoiOptIntervalSecondOrderPMDMax_Type = Integer32
_CoiOptIntervalSecondOrderPMDMax_Object = MibTableColumn
coiOptIntervalSecondOrderPMDMax = _CoiOptIntervalSecondOrderPMDMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 9),
    _CoiOptIntervalSecondOrderPMDMax_Type()
)
coiOptIntervalSecondOrderPMDMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalSecondOrderPMDMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalSecondOrderPMDMax.setUnits("1/100 ps^2")
_CoiOptIntervalPolarizationDependentLossMax_Type = Integer32
_CoiOptIntervalPolarizationDependentLossMax_Object = MibTableColumn
coiOptIntervalPolarizationDependentLossMax = _CoiOptIntervalPolarizationDependentLossMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 10),
    _CoiOptIntervalPolarizationDependentLossMax_Type()
)
coiOptIntervalPolarizationDependentLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationDependentLossMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationDependentLossMax.setUnits("1/100 dB")
_CoiOptIntervalPolarizationChangeRateMax_Type = Integer32
_CoiOptIntervalPolarizationChangeRateMax_Object = MibTableColumn
coiOptIntervalPolarizationChangeRateMax = _CoiOptIntervalPolarizationChangeRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 11),
    _CoiOptIntervalPolarizationChangeRateMax_Type()
)
coiOptIntervalPolarizationChangeRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationChangeRateMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationChangeRateMax.setUnits("1/100 rad/s")
_CoiOptIntervalPhaseNoiseMax_Type = Integer32
_CoiOptIntervalPhaseNoiseMax_Object = MibTableColumn
coiOptIntervalPhaseNoiseMax = _CoiOptIntervalPhaseNoiseMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 12),
    _CoiOptIntervalPhaseNoiseMax_Type()
)
coiOptIntervalPhaseNoiseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalPhaseNoiseMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalPhaseNoiseMax.setUnits("1/1000 dB")
_CoiOptIntervalLBCMax_Type = Integer32
_CoiOptIntervalLBCMax_Object = MibTableColumn
coiOptIntervalLBCMax = _CoiOptIntervalLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 13),
    _CoiOptIntervalLBCMax_Type()
)
coiOptIntervalLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalLBCMax.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalLBCMax.setUnits("1/10 %")
_CoiOptIntervalTXPowerMin_Type = CoiOpticalPower
_CoiOptIntervalTXPowerMin_Object = MibTableColumn
coiOptIntervalTXPowerMin = _CoiOptIntervalTXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 14),
    _CoiOptIntervalTXPowerMin_Type()
)
coiOptIntervalTXPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalTXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalTXPowerMin.setUnits("1/100 dBm")
_CoiOptIntervalRXPowerMin_Type = CoiOpticalPower
_CoiOptIntervalRXPowerMin_Object = MibTableColumn
coiOptIntervalRXPowerMin = _CoiOptIntervalRXPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 15),
    _CoiOptIntervalRXPowerMin_Type()
)
coiOptIntervalRXPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalRXPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalRXPowerMin.setUnits("1/100 dBm")
_CoiOptIntervalOSNRMin_Type = Integer32
_CoiOptIntervalOSNRMin_Object = MibTableColumn
coiOptIntervalOSNRMin = _CoiOptIntervalOSNRMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 16),
    _CoiOptIntervalOSNRMin_Type()
)
coiOptIntervalOSNRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalOSNRMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalOSNRMin.setUnits("1/100 dB")
_CoiOptIntervalChromaticDispersionMin_Type = Integer32
_CoiOptIntervalChromaticDispersionMin_Object = MibTableColumn
coiOptIntervalChromaticDispersionMin = _CoiOptIntervalChromaticDispersionMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 17),
    _CoiOptIntervalChromaticDispersionMin_Type()
)
coiOptIntervalChromaticDispersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalChromaticDispersionMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalChromaticDispersionMin.setUnits("ps/nm")
_CoiOptIntervalDifferentialGroupDelayMin_Type = Integer32
_CoiOptIntervalDifferentialGroupDelayMin_Object = MibTableColumn
coiOptIntervalDifferentialGroupDelayMin = _CoiOptIntervalDifferentialGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 18),
    _CoiOptIntervalDifferentialGroupDelayMin_Type()
)
coiOptIntervalDifferentialGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalDifferentialGroupDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalDifferentialGroupDelayMin.setUnits("1/100 ps")
_CoiOptIntervalSecondOrderPMDMin_Type = Integer32
_CoiOptIntervalSecondOrderPMDMin_Object = MibTableColumn
coiOptIntervalSecondOrderPMDMin = _CoiOptIntervalSecondOrderPMDMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 19),
    _CoiOptIntervalSecondOrderPMDMin_Type()
)
coiOptIntervalSecondOrderPMDMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalSecondOrderPMDMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalSecondOrderPMDMin.setUnits("1/100 ps^2")
_CoiOptIntervalPolarizationDependentLossMin_Type = Integer32
_CoiOptIntervalPolarizationDependentLossMin_Object = MibTableColumn
coiOptIntervalPolarizationDependentLossMin = _CoiOptIntervalPolarizationDependentLossMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 20),
    _CoiOptIntervalPolarizationDependentLossMin_Type()
)
coiOptIntervalPolarizationDependentLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationDependentLossMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationDependentLossMin.setUnits("1/100 dB")
_CoiOptIntervalPolarizationChangeRateMin_Type = Integer32
_CoiOptIntervalPolarizationChangeRateMin_Object = MibTableColumn
coiOptIntervalPolarizationChangeRateMin = _CoiOptIntervalPolarizationChangeRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 21),
    _CoiOptIntervalPolarizationChangeRateMin_Type()
)
coiOptIntervalPolarizationChangeRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationChangeRateMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationChangeRateMin.setUnits("1/100 rad/s")
_CoiOptIntervalPhaseNoiseMin_Type = Integer32
_CoiOptIntervalPhaseNoiseMin_Object = MibTableColumn
coiOptIntervalPhaseNoiseMin = _CoiOptIntervalPhaseNoiseMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 22),
    _CoiOptIntervalPhaseNoiseMin_Type()
)
coiOptIntervalPhaseNoiseMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalPhaseNoiseMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalPhaseNoiseMin.setUnits("1/1000 dB")
_CoiOptIntervalLBCMin_Type = Integer32
_CoiOptIntervalLBCMin_Object = MibTableColumn
coiOptIntervalLBCMin = _CoiOptIntervalLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 23),
    _CoiOptIntervalLBCMin_Type()
)
coiOptIntervalLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalLBCMin.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalLBCMin.setUnits("1/10 %")
_CoiOptIntervalTXPowerAvg_Type = CoiOpticalPower
_CoiOptIntervalTXPowerAvg_Object = MibTableColumn
coiOptIntervalTXPowerAvg = _CoiOptIntervalTXPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 24),
    _CoiOptIntervalTXPowerAvg_Type()
)
coiOptIntervalTXPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalTXPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalTXPowerAvg.setUnits("1/100 dBm")
_CoiOptIntervalRXPowerAvg_Type = CoiOpticalPower
_CoiOptIntervalRXPowerAvg_Object = MibTableColumn
coiOptIntervalRXPowerAvg = _CoiOptIntervalRXPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 25),
    _CoiOptIntervalRXPowerAvg_Type()
)
coiOptIntervalRXPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalRXPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalRXPowerAvg.setUnits("1/100 dBm")
_CoiOptIntervalOSNRAvg_Type = Integer32
_CoiOptIntervalOSNRAvg_Object = MibTableColumn
coiOptIntervalOSNRAvg = _CoiOptIntervalOSNRAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 26),
    _CoiOptIntervalOSNRAvg_Type()
)
coiOptIntervalOSNRAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalOSNRAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalOSNRAvg.setUnits("1/100 dB")
_CoiOptIntervalChromaticDispersionAvg_Type = Integer32
_CoiOptIntervalChromaticDispersionAvg_Object = MibTableColumn
coiOptIntervalChromaticDispersionAvg = _CoiOptIntervalChromaticDispersionAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 27),
    _CoiOptIntervalChromaticDispersionAvg_Type()
)
coiOptIntervalChromaticDispersionAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalChromaticDispersionAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalChromaticDispersionAvg.setUnits("ps/nm")
_CoiOptIntervalDifferentialGroupDelayAvg_Type = Integer32
_CoiOptIntervalDifferentialGroupDelayAvg_Object = MibTableColumn
coiOptIntervalDifferentialGroupDelayAvg = _CoiOptIntervalDifferentialGroupDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 28),
    _CoiOptIntervalDifferentialGroupDelayAvg_Type()
)
coiOptIntervalDifferentialGroupDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalDifferentialGroupDelayAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalDifferentialGroupDelayAvg.setUnits("1/100 ps")
_CoiOptIntervalSecondOrderPMDAvg_Type = Integer32
_CoiOptIntervalSecondOrderPMDAvg_Object = MibTableColumn
coiOptIntervalSecondOrderPMDAvg = _CoiOptIntervalSecondOrderPMDAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 29),
    _CoiOptIntervalSecondOrderPMDAvg_Type()
)
coiOptIntervalSecondOrderPMDAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalSecondOrderPMDAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalSecondOrderPMDAvg.setUnits("1/100 ps^2")
_CoiOptIntervalPolarizationDependentLossAvg_Type = Integer32
_CoiOptIntervalPolarizationDependentLossAvg_Object = MibTableColumn
coiOptIntervalPolarizationDependentLossAvg = _CoiOptIntervalPolarizationDependentLossAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 30),
    _CoiOptIntervalPolarizationDependentLossAvg_Type()
)
coiOptIntervalPolarizationDependentLossAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationDependentLossAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationDependentLossAvg.setUnits("1/100 dB")
_CoiOptIntervalPolarizationChangeRateAvg_Type = Integer32
_CoiOptIntervalPolarizationChangeRateAvg_Object = MibTableColumn
coiOptIntervalPolarizationChangeRateAvg = _CoiOptIntervalPolarizationChangeRateAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 31),
    _CoiOptIntervalPolarizationChangeRateAvg_Type()
)
coiOptIntervalPolarizationChangeRateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationChangeRateAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalPolarizationChangeRateAvg.setUnits("1/100 rad/s")
_CoiOptIntervalPhaseNoiseAvg_Type = Integer32
_CoiOptIntervalPhaseNoiseAvg_Object = MibTableColumn
coiOptIntervalPhaseNoiseAvg = _CoiOptIntervalPhaseNoiseAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 32),
    _CoiOptIntervalPhaseNoiseAvg_Type()
)
coiOptIntervalPhaseNoiseAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalPhaseNoiseAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalPhaseNoiseAvg.setUnits("1/1000 dB")
_CoiOptIntervalLBCAvg_Type = Integer32
_CoiOptIntervalLBCAvg_Object = MibTableColumn
coiOptIntervalLBCAvg = _CoiOptIntervalLBCAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 33),
    _CoiOptIntervalLBCAvg_Type()
)
coiOptIntervalLBCAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalLBCAvg.setStatus("current")
if mibBuilder.loadTexts:
    coiOptIntervalLBCAvg.setUnits("1/10 %")
_CoiOptIntervalTimestamp_Type = OctetString
_CoiOptIntervalTimestamp_Object = MibTableColumn
coiOptIntervalTimestamp = _CoiOptIntervalTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 2, 3, 1, 34),
    _CoiOptIntervalTimestamp_Type()
)
coiOptIntervalTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOptIntervalTimestamp.setStatus("current")
_CoiOpticalClientInfoTable_Object = MibTable
coiOpticalClientInfoTable = _CoiOpticalClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 3)
)
if mibBuilder.loadTexts:
    coiOpticalClientInfoTable.setStatus("current")
_CoiOpticalClientInfoEntry_Object = MibTableRow
coiOpticalClientInfoEntry = _CoiOpticalClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 3, 1)
)
coiOpticalClientInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coiOpticalClientInfoEntry.setStatus("current")
_CoiOpticalClientEthernetNeighbourMAC_Type = MacAddress
_CoiOpticalClientEthernetNeighbourMAC_Object = MibTableColumn
coiOpticalClientEthernetNeighbourMAC = _CoiOpticalClientEthernetNeighbourMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 3, 1, 1),
    _CoiOpticalClientEthernetNeighbourMAC_Type()
)
coiOpticalClientEthernetNeighbourMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOpticalClientEthernetNeighbourMAC.setStatus("current")
_CoiOpticalEquipmentAlarmGroup_ObjectIdentity = ObjectIdentity
coiOpticalEquipmentAlarmGroup = _CoiOpticalEquipmentAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 4)
)
_CoiOpticalAlarmLocation_Type = DisplayString
_CoiOpticalAlarmLocation_Object = MibScalar
coiOpticalAlarmLocation = _CoiOpticalAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 4, 1),
    _CoiOpticalAlarmLocation_Type()
)
coiOpticalAlarmLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    coiOpticalAlarmLocation.setStatus("current")
_CoiOpticalAlarmType_Type = CoiOptAlarmType
_CoiOpticalAlarmType_Object = MibScalar
coiOpticalAlarmType = _CoiOpticalAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 4, 2),
    _CoiOpticalAlarmType_Type()
)
coiOpticalAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    coiOpticalAlarmType.setStatus("current")
_CoiOpticalAlarmTimeStamp_Type = TimeStamp
_CoiOpticalAlarmTimeStamp_Object = MibScalar
coiOpticalAlarmTimeStamp = _CoiOpticalAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 4, 3),
    _CoiOpticalAlarmTimeStamp_Type()
)
coiOpticalAlarmTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    coiOpticalAlarmTimeStamp.setStatus("current")
_CoiOpticalAlarmName_Type = DisplayString
_CoiOpticalAlarmName_Object = MibScalar
coiOpticalAlarmName = _CoiOpticalAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 4, 4),
    _CoiOpticalAlarmName_Type()
)
coiOpticalAlarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    coiOpticalAlarmName.setStatus("current")
_CoiOpticalAlarmAdditionalInfo_Type = DisplayString
_CoiOpticalAlarmAdditionalInfo_Object = MibScalar
coiOpticalAlarmAdditionalInfo = _CoiOpticalAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 4, 5),
    _CoiOpticalAlarmAdditionalInfo_Type()
)
coiOpticalAlarmAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    coiOpticalAlarmAdditionalInfo.setStatus("current")
_CoiOpticalAlarmSeverity_Type = CoiOptAlarmSeverity
_CoiOpticalAlarmSeverity_Object = MibScalar
coiOpticalAlarmSeverity = _CoiOpticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 4, 6),
    _CoiOpticalAlarmSeverity_Type()
)
coiOpticalAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    coiOpticalAlarmSeverity.setStatus("current")
_CoiOpticalAlarmStatus_Type = CoiOptAlarmStatus
_CoiOpticalAlarmStatus_Object = MibScalar
coiOpticalAlarmStatus = _CoiOpticalAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 4, 7),
    _CoiOpticalAlarmStatus_Type()
)
coiOpticalAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    coiOpticalAlarmStatus.setStatus("current")
_CoiOpticalAlarmServiceAffecting_Type = CoiOptAlarmServiceAffecting
_CoiOpticalAlarmServiceAffecting_Object = MibScalar
coiOpticalAlarmServiceAffecting = _CoiOpticalAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 1, 4, 8),
    _CoiOpticalAlarmServiceAffecting_Type()
)
coiOpticalAlarmServiceAffecting.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    coiOpticalAlarmServiceAffecting.setStatus("current")
_CiscoOpticalMIBConformance_ObjectIdentity = ObjectIdentity
ciscoOpticalMIBConformance = _CiscoOpticalMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2)
)
_CiscoOpticalMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoOpticalMIBCompliances = _CiscoOpticalMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 1)
)
_CiscoOpticalMIBGroups_ObjectIdentity = ObjectIdentity
ciscoOpticalMIBGroups = _CiscoOpticalMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2)
)

# Managed Objects groups

coiOpticalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 1)
)
coiOpticalGroup.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOpticalControllerLaserStatus"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerTransmitPower"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerOpticsType"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerRXLowThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerTXLowThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerRXHighThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerTXHighThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerLBCHighThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneRXPower"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneTXPower"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneLBC"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerStatus"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshTXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshRXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshLBCMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshTXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshRXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshLBCMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentTXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentRXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentLBCMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentTXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentRXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentLBCMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentTXPowerAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentRXPowerAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentLBCAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalTXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalRXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalLBCMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalTXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalRXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalLBCMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalTXPowerAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalRXPowerAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalLBCAvg"))
)
if mibBuilder.loadTexts:
    coiOpticalGroup.setStatus("current")

coiOpticalControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 2)
)
coiOpticalControllerGroup.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOpticalControllerWavelength"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerLaserStatus"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerFrequency"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerChannelNumber"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerTransmitPower"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerOpticsType"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerRXLowThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerTXLowThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerRXHighThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerTXHighThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerLBCHighThreshold"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerStatus"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPortType"))
)
if mibBuilder.loadTexts:
    coiOpticalControllerGroup.setStatus("current")

coiOpticalControllerPerLaneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 3)
)
coiOpticalControllerPerLaneGroup.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneRXPower"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneTXPower"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneLBC"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneOSNR"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneChromaticDispersion"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneDifferentialGroupDelay"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLaneSecondOrderPMD"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLanePolarizationDependentLoss"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLanePolarizationChangeRate"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPerLanePhaseNoise"))
)
if mibBuilder.loadTexts:
    coiOpticalControllerPerLaneGroup.setStatus("current")

coiOpticalClientInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 4)
)
coiOpticalClientInfoGroup.setObjects(
    ("CISCO-OPTICAL-MIB", "coiOpticalClientEthernetNeighbourMAC")
)
if mibBuilder.loadTexts:
    coiOpticalClientInfoGroup.setStatus("current")

coiOpticalThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 5)
)
coiOpticalThresholdGroup.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOptThreshTXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshRXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshOSNRMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshChromaticDispersionMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshDifferentialGroupDelayMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshSecondOrderPMDMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPolarizationDependentLossMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPolarizationChangeRateMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPhaseNoiseMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshLBCMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshTXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshRXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshOSNRMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshChromaticDispersionMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshDifferentialGroupDelayMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshSecondOrderPMDMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPolarizationDependentLossMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPolarizationChangeRateMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPhaseNoiseMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshLBCMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshTXPowerEnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshRXPowerEnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshOSNREnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshChromaticDispersionEnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshDifferentialGroupDelayEnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshSecondOrderPMDEnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPolarizationDependentLossEnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPolarizationChangeRateEnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPhaseNoiseEnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshLBCEnableMin"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshTXPowerEnableMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshRXPowerEnableMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshOSNREnableMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshChromaticDispersionEnableMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshDifferentialGroupDelayEnableMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshSecondOrderPMDEnableMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPolarizationDependentLossEnableMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPolarizationChangeRateEnableMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshPhaseNoiseEnableMax"),
        ("CISCO-OPTICAL-MIB", "coiOptThreshLBCEnableMax"))
)
if mibBuilder.loadTexts:
    coiOpticalThresholdGroup.setStatus("current")

coiOpticalCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 6)
)
coiOpticalCurrentGroup.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOptCurrentTXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentRXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentOSNRMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentChromaticDispersionMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentDifferentialGroupDelayMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentSecondOrderPMDMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentPolarizationDependentLossMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentPolarizationChangeRateMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentPhaseNoiseMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentLBCMax"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentTXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentRXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentOSNRMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentChromaticDispersionMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentDifferentialGroupDelayMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentSecondOrderPMDMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentPolarizationDependentLossMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentPolarizationChangeRateMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentPhaseNoiseMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentLBCMin"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentTXPowerAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentRXPowerAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentOSNRAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentChromaticDispersionAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentDifferentialGroupDelayAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentSecondOrderPMDAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentPolarizationDependentLossAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentPolarizationChangeRateAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentPhaseNoiseAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentLBCAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptCurrentTimestamp"))
)
if mibBuilder.loadTexts:
    coiOpticalCurrentGroup.setStatus("current")

coiOpticalIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 7)
)
coiOpticalIntervalGroup.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOptIntervalTXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalRXPowerMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalOSNRMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalChromaticDispersionMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalDifferentialGroupDelayMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalSecondOrderPMDMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalPolarizationDependentLossMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalPolarizationChangeRateMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalPhaseNoiseMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalLBCMax"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalTXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalRXPowerMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalOSNRMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalChromaticDispersionMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalDifferentialGroupDelayMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalSecondOrderPMDMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalPolarizationDependentLossMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalPolarizationChangeRateMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalPhaseNoiseMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalLBCMin"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalTXPowerAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalRXPowerAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalOSNRAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalChromaticDispersionAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalDifferentialGroupDelayAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalSecondOrderPMDAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalPolarizationDependentLossAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalPolarizationChangeRateAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalPhaseNoiseAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalLBCAvg"),
        ("CISCO-OPTICAL-MIB", "coiOptIntervalTimestamp"))
)
if mibBuilder.loadTexts:
    coiOpticalIntervalGroup.setStatus("current")

coiOpticalNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 8)
)
coiOpticalNotifEnableGroup.setObjects(
    ("CISCO-OPTICAL-MIB", "coiOpticalNotifEnabled")
)
if mibBuilder.loadTexts:
    coiOpticalNotifEnableGroup.setStatus("current")

coiOpticalNotifStatusObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 9)
)
coiOpticalNotifStatusObjectGroup.setObjects(
    ("CISCO-OPTICAL-MIB", "coiOpticalControllerStatus")
)
if mibBuilder.loadTexts:
    coiOpticalNotifStatusObjectGroup.setStatus("current")

coiOpticalEquipmentAlarmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 11)
)
coiOpticalEquipmentAlarmInfoGroup.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOpticalAlarmLocation"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmType"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmTimeStamp"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmName"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmAdditionalInfo"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmSeverity"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmStatus"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    coiOpticalEquipmentAlarmInfoGroup.setStatus("current")

coiOpticalPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 12)
)
coiOpticalPowerGroup.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOpticalControllerTotalRXPower"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerTotalTXPower"))
)
if mibBuilder.loadTexts:
    coiOpticalPowerGroup.setStatus("current")


# Notification objects

coiOpticsStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 0, 1)
)
coiOpticsStatusChange.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerPortType"),
        ("CISCO-OPTICAL-MIB", "coiOpticalControllerStatus"))
)
if mibBuilder.loadTexts:
    coiOpticsStatusChange.setStatus(
        "current"
    )

coiOpticalEquipmentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 0, 2)
)
coiOpticalEquipmentAlarm.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOpticalAlarmLocation"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmType"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmTimeStamp"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmName"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmAdditionalInfo"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmSeverity"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmStatus"),
        ("CISCO-OPTICAL-MIB", "coiOpticalAlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    coiOpticalEquipmentAlarm.setStatus(
        "current"
    )


# Notifications groups

coiOpticalNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 2, 10)
)
coiOpticalNotifGroup.setObjects(
      *(("CISCO-OPTICAL-MIB", "coiOpticsStatusChange"),
        ("CISCO-OPTICAL-MIB", "coiOpticalEquipmentAlarm"))
)
if mibBuilder.loadTexts:
    coiOpticalNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoOpticalMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoOpticalMIBCompliance.setStatus(
        "deprecated"
    )

ciscoOpticalMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 828, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoOpticalMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OPTICAL-MIB",
    **{"CoiOpticalPower": CoiOpticalPower,
       "CoiOpticalWavelength": CoiOpticalWavelength,
       "CoiIntervalType": CoiIntervalType,
       "CoiPortType": CoiPortType,
       "CoiOptAlarmType": CoiOptAlarmType,
       "CoiOptAlarmSeverity": CoiOptAlarmSeverity,
       "CoiOptAlarmStatus": CoiOptAlarmStatus,
       "CoiOptAlarmServiceAffecting": CoiOptAlarmServiceAffecting,
       "ciscoOpticalMIB": ciscoOpticalMIB,
       "ciscoOpticalMIBNotifs": ciscoOpticalMIBNotifs,
       "coiOpticsStatusChange": coiOpticsStatusChange,
       "coiOpticalEquipmentAlarm": coiOpticalEquipmentAlarm,
       "ciscoOpticalMIBObjects": ciscoOpticalMIBObjects,
       "coiOpticalController": coiOpticalController,
       "coiOpticalNotifEnabled": coiOpticalNotifEnabled,
       "coiOpticalControllerTable": coiOpticalControllerTable,
       "coiOpticalControllerEntry": coiOpticalControllerEntry,
       "coiOpticalControllerWavelength": coiOpticalControllerWavelength,
       "coiOpticalControllerLaserStatus": coiOpticalControllerLaserStatus,
       "coiOpticalControllerFrequency": coiOpticalControllerFrequency,
       "coiOpticalControllerChannelNumber": coiOpticalControllerChannelNumber,
       "coiOpticalControllerTransmitPower": coiOpticalControllerTransmitPower,
       "coiOpticalControllerOpticsType": coiOpticalControllerOpticsType,
       "coiOpticalControllerRXLowThreshold": coiOpticalControllerRXLowThreshold,
       "coiOpticalControllerTXLowThreshold": coiOpticalControllerTXLowThreshold,
       "coiOpticalControllerRXHighThreshold": coiOpticalControllerRXHighThreshold,
       "coiOpticalControllerTXHighThreshold": coiOpticalControllerTXHighThreshold,
       "coiOpticalControllerLBCHighThreshold": coiOpticalControllerLBCHighThreshold,
       "coiOpticalControllerStatus": coiOpticalControllerStatus,
       "coiOpticalControllerPortType": coiOpticalControllerPortType,
       "coiOpticalControllerTotalRXPower": coiOpticalControllerTotalRXPower,
       "coiOpticalControllerTotalTXPower": coiOpticalControllerTotalTXPower,
       "coiOpticalControllerPerLaneTable": coiOpticalControllerPerLaneTable,
       "coiOpticalControllerPerLaneEntry": coiOpticalControllerPerLaneEntry,
       "coiOpticalControllerLane": coiOpticalControllerLane,
       "coiOpticalControllerPerLaneRXPower": coiOpticalControllerPerLaneRXPower,
       "coiOpticalControllerPerLaneTXPower": coiOpticalControllerPerLaneTXPower,
       "coiOpticalControllerPerLaneLBC": coiOpticalControllerPerLaneLBC,
       "coiOpticalControllerPerLaneOSNR": coiOpticalControllerPerLaneOSNR,
       "coiOpticalControllerPerLaneChromaticDispersion": coiOpticalControllerPerLaneChromaticDispersion,
       "coiOpticalControllerPerLaneDifferentialGroupDelay": coiOpticalControllerPerLaneDifferentialGroupDelay,
       "coiOpticalControllerPerLaneSecondOrderPMD": coiOpticalControllerPerLaneSecondOrderPMD,
       "coiOpticalControllerPerLanePolarizationDependentLoss": coiOpticalControllerPerLanePolarizationDependentLoss,
       "coiOpticalControllerPerLanePolarizationChangeRate": coiOpticalControllerPerLanePolarizationChangeRate,
       "coiOpticalControllerPerLanePhaseNoise": coiOpticalControllerPerLanePhaseNoise,
       "coiOpticalPerformanceMonitoring": coiOpticalPerformanceMonitoring,
       "coiOpticalThresholdTable": coiOpticalThresholdTable,
       "coiOpticalThresholdEntry": coiOpticalThresholdEntry,
       "coiOptThreshIntervalType": coiOptThreshIntervalType,
       "coiOptThreshTXPowerMin": coiOptThreshTXPowerMin,
       "coiOptThreshRXPowerMin": coiOptThreshRXPowerMin,
       "coiOptThreshOSNRMin": coiOptThreshOSNRMin,
       "coiOptThreshChromaticDispersionMin": coiOptThreshChromaticDispersionMin,
       "coiOptThreshDifferentialGroupDelayMin": coiOptThreshDifferentialGroupDelayMin,
       "coiOptThreshSecondOrderPMDMin": coiOptThreshSecondOrderPMDMin,
       "coiOptThreshPolarizationDependentLossMin": coiOptThreshPolarizationDependentLossMin,
       "coiOptThreshPolarizationChangeRateMin": coiOptThreshPolarizationChangeRateMin,
       "coiOptThreshPhaseNoiseMin": coiOptThreshPhaseNoiseMin,
       "coiOptThreshLBCMin": coiOptThreshLBCMin,
       "coiOptThreshTXPowerMax": coiOptThreshTXPowerMax,
       "coiOptThreshRXPowerMax": coiOptThreshRXPowerMax,
       "coiOptThreshOSNRMax": coiOptThreshOSNRMax,
       "coiOptThreshChromaticDispersionMax": coiOptThreshChromaticDispersionMax,
       "coiOptThreshDifferentialGroupDelayMax": coiOptThreshDifferentialGroupDelayMax,
       "coiOptThreshSecondOrderPMDMax": coiOptThreshSecondOrderPMDMax,
       "coiOptThreshPolarizationDependentLossMax": coiOptThreshPolarizationDependentLossMax,
       "coiOptThreshPolarizationChangeRateMax": coiOptThreshPolarizationChangeRateMax,
       "coiOptThreshPhaseNoiseMax": coiOptThreshPhaseNoiseMax,
       "coiOptThreshLBCMax": coiOptThreshLBCMax,
       "coiOptThreshTXPowerEnableMin": coiOptThreshTXPowerEnableMin,
       "coiOptThreshRXPowerEnableMin": coiOptThreshRXPowerEnableMin,
       "coiOptThreshOSNREnableMin": coiOptThreshOSNREnableMin,
       "coiOptThreshChromaticDispersionEnableMin": coiOptThreshChromaticDispersionEnableMin,
       "coiOptThreshDifferentialGroupDelayEnableMin": coiOptThreshDifferentialGroupDelayEnableMin,
       "coiOptThreshSecondOrderPMDEnableMin": coiOptThreshSecondOrderPMDEnableMin,
       "coiOptThreshPolarizationDependentLossEnableMin": coiOptThreshPolarizationDependentLossEnableMin,
       "coiOptThreshPolarizationChangeRateEnableMin": coiOptThreshPolarizationChangeRateEnableMin,
       "coiOptThreshPhaseNoiseEnableMin": coiOptThreshPhaseNoiseEnableMin,
       "coiOptThreshLBCEnableMin": coiOptThreshLBCEnableMin,
       "coiOptThreshTXPowerEnableMax": coiOptThreshTXPowerEnableMax,
       "coiOptThreshRXPowerEnableMax": coiOptThreshRXPowerEnableMax,
       "coiOptThreshOSNREnableMax": coiOptThreshOSNREnableMax,
       "coiOptThreshChromaticDispersionEnableMax": coiOptThreshChromaticDispersionEnableMax,
       "coiOptThreshDifferentialGroupDelayEnableMax": coiOptThreshDifferentialGroupDelayEnableMax,
       "coiOptThreshSecondOrderPMDEnableMax": coiOptThreshSecondOrderPMDEnableMax,
       "coiOptThreshPolarizationDependentLossEnableMax": coiOptThreshPolarizationDependentLossEnableMax,
       "coiOptThreshPolarizationChangeRateEnableMax": coiOptThreshPolarizationChangeRateEnableMax,
       "coiOptThreshPhaseNoiseEnableMax": coiOptThreshPhaseNoiseEnableMax,
       "coiOptThreshLBCEnableMax": coiOptThreshLBCEnableMax,
       "coiOpticalCurrentTable": coiOpticalCurrentTable,
       "coiOpticalCurrentEntry": coiOpticalCurrentEntry,
       "coiOptCurrentLane": coiOptCurrentLane,
       "coiOptCurrentIntervalType": coiOptCurrentIntervalType,
       "coiOptCurrentTXPowerMax": coiOptCurrentTXPowerMax,
       "coiOptCurrentRXPowerMax": coiOptCurrentRXPowerMax,
       "coiOptCurrentOSNRMax": coiOptCurrentOSNRMax,
       "coiOptCurrentChromaticDispersionMax": coiOptCurrentChromaticDispersionMax,
       "coiOptCurrentDifferentialGroupDelayMax": coiOptCurrentDifferentialGroupDelayMax,
       "coiOptCurrentSecondOrderPMDMax": coiOptCurrentSecondOrderPMDMax,
       "coiOptCurrentPolarizationDependentLossMax": coiOptCurrentPolarizationDependentLossMax,
       "coiOptCurrentPolarizationChangeRateMax": coiOptCurrentPolarizationChangeRateMax,
       "coiOptCurrentPhaseNoiseMax": coiOptCurrentPhaseNoiseMax,
       "coiOptCurrentLBCMax": coiOptCurrentLBCMax,
       "coiOptCurrentTXPowerMin": coiOptCurrentTXPowerMin,
       "coiOptCurrentRXPowerMin": coiOptCurrentRXPowerMin,
       "coiOptCurrentOSNRMin": coiOptCurrentOSNRMin,
       "coiOptCurrentChromaticDispersionMin": coiOptCurrentChromaticDispersionMin,
       "coiOptCurrentDifferentialGroupDelayMin": coiOptCurrentDifferentialGroupDelayMin,
       "coiOptCurrentSecondOrderPMDMin": coiOptCurrentSecondOrderPMDMin,
       "coiOptCurrentPolarizationDependentLossMin": coiOptCurrentPolarizationDependentLossMin,
       "coiOptCurrentPolarizationChangeRateMin": coiOptCurrentPolarizationChangeRateMin,
       "coiOptCurrentPhaseNoiseMin": coiOptCurrentPhaseNoiseMin,
       "coiOptCurrentLBCMin": coiOptCurrentLBCMin,
       "coiOptCurrentTXPowerAvg": coiOptCurrentTXPowerAvg,
       "coiOptCurrentRXPowerAvg": coiOptCurrentRXPowerAvg,
       "coiOptCurrentOSNRAvg": coiOptCurrentOSNRAvg,
       "coiOptCurrentChromaticDispersionAvg": coiOptCurrentChromaticDispersionAvg,
       "coiOptCurrentDifferentialGroupDelayAvg": coiOptCurrentDifferentialGroupDelayAvg,
       "coiOptCurrentSecondOrderPMDAvg": coiOptCurrentSecondOrderPMDAvg,
       "coiOptCurrentPolarizationDependentLossAvg": coiOptCurrentPolarizationDependentLossAvg,
       "coiOptCurrentPolarizationChangeRateAvg": coiOptCurrentPolarizationChangeRateAvg,
       "coiOptCurrentPhaseNoiseAvg": coiOptCurrentPhaseNoiseAvg,
       "coiOptCurrentLBCAvg": coiOptCurrentLBCAvg,
       "coiOptCurrentTimestamp": coiOptCurrentTimestamp,
       "coiOpticalIntervalTable": coiOpticalIntervalTable,
       "coiOpticalIntervalEntry": coiOpticalIntervalEntry,
       "coiOptIntervalLane": coiOptIntervalLane,
       "coiOptIntervalIntervalType": coiOptIntervalIntervalType,
       "coiOptIntervalNum": coiOptIntervalNum,
       "coiOptIntervalTXPowerMax": coiOptIntervalTXPowerMax,
       "coiOptIntervalRXPowerMax": coiOptIntervalRXPowerMax,
       "coiOptIntervalOSNRMax": coiOptIntervalOSNRMax,
       "coiOptIntervalChromaticDispersionMax": coiOptIntervalChromaticDispersionMax,
       "coiOptIntervalDifferentialGroupDelayMax": coiOptIntervalDifferentialGroupDelayMax,
       "coiOptIntervalSecondOrderPMDMax": coiOptIntervalSecondOrderPMDMax,
       "coiOptIntervalPolarizationDependentLossMax": coiOptIntervalPolarizationDependentLossMax,
       "coiOptIntervalPolarizationChangeRateMax": coiOptIntervalPolarizationChangeRateMax,
       "coiOptIntervalPhaseNoiseMax": coiOptIntervalPhaseNoiseMax,
       "coiOptIntervalLBCMax": coiOptIntervalLBCMax,
       "coiOptIntervalTXPowerMin": coiOptIntervalTXPowerMin,
       "coiOptIntervalRXPowerMin": coiOptIntervalRXPowerMin,
       "coiOptIntervalOSNRMin": coiOptIntervalOSNRMin,
       "coiOptIntervalChromaticDispersionMin": coiOptIntervalChromaticDispersionMin,
       "coiOptIntervalDifferentialGroupDelayMin": coiOptIntervalDifferentialGroupDelayMin,
       "coiOptIntervalSecondOrderPMDMin": coiOptIntervalSecondOrderPMDMin,
       "coiOptIntervalPolarizationDependentLossMin": coiOptIntervalPolarizationDependentLossMin,
       "coiOptIntervalPolarizationChangeRateMin": coiOptIntervalPolarizationChangeRateMin,
       "coiOptIntervalPhaseNoiseMin": coiOptIntervalPhaseNoiseMin,
       "coiOptIntervalLBCMin": coiOptIntervalLBCMin,
       "coiOptIntervalTXPowerAvg": coiOptIntervalTXPowerAvg,
       "coiOptIntervalRXPowerAvg": coiOptIntervalRXPowerAvg,
       "coiOptIntervalOSNRAvg": coiOptIntervalOSNRAvg,
       "coiOptIntervalChromaticDispersionAvg": coiOptIntervalChromaticDispersionAvg,
       "coiOptIntervalDifferentialGroupDelayAvg": coiOptIntervalDifferentialGroupDelayAvg,
       "coiOptIntervalSecondOrderPMDAvg": coiOptIntervalSecondOrderPMDAvg,
       "coiOptIntervalPolarizationDependentLossAvg": coiOptIntervalPolarizationDependentLossAvg,
       "coiOptIntervalPolarizationChangeRateAvg": coiOptIntervalPolarizationChangeRateAvg,
       "coiOptIntervalPhaseNoiseAvg": coiOptIntervalPhaseNoiseAvg,
       "coiOptIntervalLBCAvg": coiOptIntervalLBCAvg,
       "coiOptIntervalTimestamp": coiOptIntervalTimestamp,
       "coiOpticalClientInfoTable": coiOpticalClientInfoTable,
       "coiOpticalClientInfoEntry": coiOpticalClientInfoEntry,
       "coiOpticalClientEthernetNeighbourMAC": coiOpticalClientEthernetNeighbourMAC,
       "coiOpticalEquipmentAlarmGroup": coiOpticalEquipmentAlarmGroup,
       "coiOpticalAlarmLocation": coiOpticalAlarmLocation,
       "coiOpticalAlarmType": coiOpticalAlarmType,
       "coiOpticalAlarmTimeStamp": coiOpticalAlarmTimeStamp,
       "coiOpticalAlarmName": coiOpticalAlarmName,
       "coiOpticalAlarmAdditionalInfo": coiOpticalAlarmAdditionalInfo,
       "coiOpticalAlarmSeverity": coiOpticalAlarmSeverity,
       "coiOpticalAlarmStatus": coiOpticalAlarmStatus,
       "coiOpticalAlarmServiceAffecting": coiOpticalAlarmServiceAffecting,
       "ciscoOpticalMIBConformance": ciscoOpticalMIBConformance,
       "ciscoOpticalMIBCompliances": ciscoOpticalMIBCompliances,
       "ciscoOpticalMIBCompliance": ciscoOpticalMIBCompliance,
       "ciscoOpticalMIBComplianceRev1": ciscoOpticalMIBComplianceRev1,
       "ciscoOpticalMIBGroups": ciscoOpticalMIBGroups,
       "coiOpticalGroup": coiOpticalGroup,
       "coiOpticalControllerGroup": coiOpticalControllerGroup,
       "coiOpticalControllerPerLaneGroup": coiOpticalControllerPerLaneGroup,
       "coiOpticalClientInfoGroup": coiOpticalClientInfoGroup,
       "coiOpticalThresholdGroup": coiOpticalThresholdGroup,
       "coiOpticalCurrentGroup": coiOpticalCurrentGroup,
       "coiOpticalIntervalGroup": coiOpticalIntervalGroup,
       "coiOpticalNotifEnableGroup": coiOpticalNotifEnableGroup,
       "coiOpticalNotifStatusObjectGroup": coiOpticalNotifStatusObjectGroup,
       "coiOpticalNotifGroup": coiOpticalNotifGroup,
       "coiOpticalEquipmentAlarmInfoGroup": coiOpticalEquipmentAlarmInfoGroup,
       "coiOpticalPowerGroup": coiOpticalPowerGroup}
)
