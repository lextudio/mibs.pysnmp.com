# SNMP MIB module (SYMMGNSS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMGNSS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:50 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

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

(GNSSHealthStatus,
 GNSSPositionMode,
 GNSSReceiverMode,
 YESVALUETYPE,
 symmPhysicalSignal) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "GNSSHealthStatus",
    "GNSSPositionMode",
    "GNSSReceiverMode",
    "YESVALUETYPE",
    "symmPhysicalSignal")


# MODULE-IDENTITY

symmGNSS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1)
)


# Types definitions



class GNSSCURPOSITIONMODE(Integer32):
    """Custom type GNSSCURPOSITIONMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 3),
          ("positionHold", 2),
          ("surveying", 1))
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_GnssStatus_ObjectIdentity = ObjectIdentity
gnssStatus = _GnssStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1)
)
_GnssPortStatusTable_Object = MibTable
gnssPortStatusTable = _GnssPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    gnssPortStatusTable.setStatus("current")
_GnssPortStatusEntry_Object = MibTableRow
gnssPortStatusEntry = _GnssPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1)
)
gnssPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMGNSS", "gnssPortStatusIndex"),
)
if mibBuilder.loadTexts:
    gnssPortStatusEntry.setStatus("current")


class _GnssPortStatusIndex_Type(Integer32):
    """Custom type gnssPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_GnssPortStatusIndex_Type.__name__ = "Integer32"
_GnssPortStatusIndex_Object = MibTableColumn
gnssPortStatusIndex = _GnssPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 1),
    _GnssPortStatusIndex_Type()
)
gnssPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gnssPortStatusIndex.setStatus("current")
_GnssPortStatusPortName_Type = DisplayString
_GnssPortStatusPortName_Object = MibTableColumn
gnssPortStatusPortName = _GnssPortStatusPortName_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 2),
    _GnssPortStatusPortName_Type()
)
gnssPortStatusPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssPortStatusPortName.setStatus("current")
_GnssPortCurrentGNSS_Type = YESVALUETYPE
_GnssPortCurrentGNSS_Object = MibTableColumn
gnssPortCurrentGNSS = _GnssPortCurrentGNSS_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 3),
    _GnssPortCurrentGNSS_Type()
)
gnssPortCurrentGNSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssPortCurrentGNSS.setStatus("current")
_GnssPortCurrentPosMode_Type = GNSSCURPOSITIONMODE
_GnssPortCurrentPosMode_Object = MibTableColumn
gnssPortCurrentPosMode = _GnssPortCurrentPosMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 1, 1, 4),
    _GnssPortCurrentPosMode_Type()
)
gnssPortCurrentPosMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssPortCurrentPosMode.setStatus("current")
_GnssSatTable_Object = MibTable
gnssSatTable = _GnssSatTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    gnssSatTable.setStatus("current")
_GnssSatEntry_Object = MibTableRow
gnssSatEntry = _GnssSatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1)
)
gnssSatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMGNSS", "gnssSatIndex"),
)
if mibBuilder.loadTexts:
    gnssSatEntry.setStatus("current")


class _GnssSatIndex_Type(Integer32):
    """Custom type gnssSatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 125),
    )


_GnssSatIndex_Type.__name__ = "Integer32"
_GnssSatIndex_Object = MibTableColumn
gnssSatIndex = _GnssSatIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 1),
    _GnssSatIndex_Type()
)
gnssSatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatIndex.setStatus("current")


class _GnssSatNum_Type(Integer32):
    """Custom type gnssSatNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_GnssSatNum_Type.__name__ = "Integer32"
_GnssSatNum_Object = MibTableColumn
gnssSatNum = _GnssSatNum_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 2),
    _GnssSatNum_Type()
)
gnssSatNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatNum.setStatus("current")


class _GnssSatSNR_Type(Integer32):
    """Custom type gnssSatSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_GnssSatSNR_Type.__name__ = "Integer32"
_GnssSatSNR_Object = MibTableColumn
gnssSatSNR = _GnssSatSNR_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 3),
    _GnssSatSNR_Type()
)
gnssSatSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatSNR.setStatus("current")
_GnssSatHealth_Type = GNSSHealthStatus
_GnssSatHealth_Object = MibTableColumn
gnssSatHealth = _GnssSatHealth_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 4),
    _GnssSatHealth_Type()
)
gnssSatHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatHealth.setStatus("current")


class _GnssSatAzimuth_Type(Integer32):
    """Custom type gnssSatAzimuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360),
    )


_GnssSatAzimuth_Type.__name__ = "Integer32"
_GnssSatAzimuth_Object = MibTableColumn
gnssSatAzimuth = _GnssSatAzimuth_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 5),
    _GnssSatAzimuth_Type()
)
gnssSatAzimuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatAzimuth.setStatus("current")
if mibBuilder.loadTexts:
    gnssSatAzimuth.setUnits("degrees")


class _GnssSatElevation_Type(Integer32):
    """Custom type gnssSatElevation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360),
    )


_GnssSatElevation_Type.__name__ = "Integer32"
_GnssSatElevation_Object = MibTableColumn
gnssSatElevation = _GnssSatElevation_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 6),
    _GnssSatElevation_Type()
)
gnssSatElevation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatElevation.setStatus("current")
if mibBuilder.loadTexts:
    gnssSatElevation.setUnits("degrees")
_GnssSatPortName_Type = DisplayString
_GnssSatPortName_Object = MibTableColumn
gnssSatPortName = _GnssSatPortName_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 2, 1, 7),
    _GnssSatPortName_Type()
)
gnssSatPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssSatPortName.setStatus("current")
_GnssPresentPosTable_Object = MibTable
gnssPresentPosTable = _GnssPresentPosTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    gnssPresentPosTable.setStatus("current")
_GnssPresentPosEntry_Object = MibTableRow
gnssPresentPosEntry = _GnssPresentPosEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1)
)
gnssPresentPosEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMGNSS", "gnssPresentPosIndex"),
)
if mibBuilder.loadTexts:
    gnssPresentPosEntry.setStatus("current")


class _GnssPresentPosIndex_Type(Integer32):
    """Custom type gnssPresentPosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GnssPresentPosIndex_Type.__name__ = "Integer32"
_GnssPresentPosIndex_Object = MibTableColumn
gnssPresentPosIndex = _GnssPresentPosIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 1),
    _GnssPresentPosIndex_Type()
)
gnssPresentPosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gnssPresentPosIndex.setStatus("current")
_GnssPresentPosLat_Type = DisplayString
_GnssPresentPosLat_Object = MibTableColumn
gnssPresentPosLat = _GnssPresentPosLat_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 2),
    _GnssPresentPosLat_Type()
)
gnssPresentPosLat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssPresentPosLat.setStatus("current")
_GnssPresentPosLong_Type = DisplayString
_GnssPresentPosLong_Object = MibTableColumn
gnssPresentPosLong = _GnssPresentPosLong_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 3),
    _GnssPresentPosLong_Type()
)
gnssPresentPosLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssPresentPosLong.setStatus("current")
_GnssPresentPosHeight_Type = DisplayString
_GnssPresentPosHeight_Object = MibTableColumn
gnssPresentPosHeight = _GnssPresentPosHeight_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 1, 3, 1, 4),
    _GnssPresentPosHeight_Type()
)
gnssPresentPosHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssPresentPosHeight.setStatus("current")
_GnssConfig_ObjectIdentity = ObjectIdentity
gnssConfig = _GnssConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2)
)
_GnssConfigurationTable_Object = MibTable
gnssConfigurationTable = _GnssConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gnssConfigurationTable.setStatus("current")
_GnssConfigurationEntry_Object = MibTableRow
gnssConfigurationEntry = _GnssConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1)
)
gnssConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMGNSS", "gnssConfigurationIndex"),
)
if mibBuilder.loadTexts:
    gnssConfigurationEntry.setStatus("current")


class _GnssConfigurationIndex_Type(Integer32):
    """Custom type gnssConfigurationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_GnssConfigurationIndex_Type.__name__ = "Integer32"
_GnssConfigurationIndex_Object = MibTableColumn
gnssConfigurationIndex = _GnssConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 1),
    _GnssConfigurationIndex_Type()
)
gnssConfigurationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gnssConfigurationIndex.setStatus("current")
_GnssConfigurationPortName_Type = DisplayString
_GnssConfigurationPortName_Object = MibTableColumn
gnssConfigurationPortName = _GnssConfigurationPortName_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 2),
    _GnssConfigurationPortName_Type()
)
gnssConfigurationPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssConfigurationPortName.setStatus("current")
_GnssConfigurationTrackMode_Type = GNSSReceiverMode
_GnssConfigurationTrackMode_Object = MibTableColumn
gnssConfigurationTrackMode = _GnssConfigurationTrackMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 3),
    _GnssConfigurationTrackMode_Type()
)
gnssConfigurationTrackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnssConfigurationTrackMode.setStatus("current")
_GnssConfigurationPosMode_Type = GNSSPositionMode
_GnssConfigurationPosMode_Object = MibTableColumn
gnssConfigurationPosMode = _GnssConfigurationPosMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 4),
    _GnssConfigurationPosMode_Type()
)
gnssConfigurationPosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnssConfigurationPosMode.setStatus("current")


class _GnssConfigurationElevMask_Type(Integer32):
    """Custom type gnssConfigurationElevMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 45),
    )


_GnssConfigurationElevMask_Type.__name__ = "Integer32"
_GnssConfigurationElevMask_Object = MibTableColumn
gnssConfigurationElevMask = _GnssConfigurationElevMask_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 5),
    _GnssConfigurationElevMask_Type()
)
gnssConfigurationElevMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnssConfigurationElevMask.setStatus("current")
_GnssConfigurationCableDelay_Type = Integer32
_GnssConfigurationCableDelay_Object = MibTableColumn
gnssConfigurationCableDelay = _GnssConfigurationCableDelay_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 6),
    _GnssConfigurationCableDelay_Type()
)
gnssConfigurationCableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnssConfigurationCableDelay.setStatus("current")


class _GnssConfigurationLeapSeconds_Type(Integer32):
    """Custom type gnssConfigurationLeapSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_GnssConfigurationLeapSeconds_Type.__name__ = "Integer32"
_GnssConfigurationLeapSeconds_Object = MibTableColumn
gnssConfigurationLeapSeconds = _GnssConfigurationLeapSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 1, 1, 7),
    _GnssConfigurationLeapSeconds_Type()
)
gnssConfigurationLeapSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnssConfigurationLeapSeconds.setStatus("current")
_GnssPosSettingTable_Object = MibTable
gnssPosSettingTable = _GnssPosSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gnssPosSettingTable.setStatus("current")
_GnssPosSettingEntry_Object = MibTableRow
gnssPosSettingEntry = _GnssPosSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1)
)
gnssPosSettingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SYMMGNSS", "gnssPosSettingIndex"),
)
if mibBuilder.loadTexts:
    gnssPosSettingEntry.setStatus("current")


class _GnssPosSettingIndex_Type(Integer32):
    """Custom type gnssPosSettingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GnssPosSettingIndex_Type.__name__ = "Integer32"
_GnssPosSettingIndex_Object = MibTableColumn
gnssPosSettingIndex = _GnssPosSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 1),
    _GnssPosSettingIndex_Type()
)
gnssPosSettingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gnssPosSettingIndex.setStatus("current")
_GnssPosSettingLat_Type = DisplayString
_GnssPosSettingLat_Object = MibTableColumn
gnssPosSettingLat = _GnssPosSettingLat_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 2),
    _GnssPosSettingLat_Type()
)
gnssPosSettingLat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnssPosSettingLat.setStatus("current")
_GnssPosSettingLong_Type = DisplayString
_GnssPosSettingLong_Object = MibTableColumn
gnssPosSettingLong = _GnssPosSettingLong_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 3),
    _GnssPosSettingLong_Type()
)
gnssPosSettingLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnssPosSettingLong.setStatus("current")
_GnssPosSettingHeight_Type = DisplayString
_GnssPosSettingHeight_Object = MibTableColumn
gnssPosSettingHeight = _GnssPosSettingHeight_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 2, 2, 1, 4),
    _GnssPosSettingHeight_Type()
)
gnssPosSettingHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnssPosSettingHeight.setStatus("current")
_GnssConformance_ObjectIdentity = ObjectIdentity
gnssConformance = _GnssConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    gnssConformance.setStatus("current")
_GnssCompliances_ObjectIdentity = ObjectIdentity
gnssCompliances = _GnssCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 1)
)
_GnssUocGroups_ObjectIdentity = ObjectIdentity
gnssUocGroups = _GnssUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2)
)

# Managed Objects groups

gnssStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 1)
)
gnssStatusGroup.setObjects(
      *(("SYMMGNSS", "gnssPortStatusPortName"),
        ("SYMMGNSS", "gnssPortCurrentGNSS"),
        ("SYMMGNSS", "gnssPortCurrentPosMode"))
)
if mibBuilder.loadTexts:
    gnssStatusGroup.setStatus("current")

gnssConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 2)
)
gnssConfigGroup.setObjects(
      *(("SYMMGNSS", "gnssConfigurationPortName"),
        ("SYMMGNSS", "gnssConfigurationTrackMode"),
        ("SYMMGNSS", "gnssConfigurationPosMode"),
        ("SYMMGNSS", "gnssConfigurationElevMask"),
        ("SYMMGNSS", "gnssConfigurationCableDelay"),
        ("SYMMGNSS", "gnssConfigurationLeapSeconds"))
)
if mibBuilder.loadTexts:
    gnssConfigGroup.setStatus("current")

gnssSVGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 3)
)
gnssSVGroup.setObjects(
      *(("SYMMGNSS", "gnssSatIndex"),
        ("SYMMGNSS", "gnssSatNum"),
        ("SYMMGNSS", "gnssSatSNR"),
        ("SYMMGNSS", "gnssSatHealth"),
        ("SYMMGNSS", "gnssSatAzimuth"),
        ("SYMMGNSS", "gnssSatElevation"),
        ("SYMMGNSS", "gnssSatPortName"))
)
if mibBuilder.loadTexts:
    gnssSVGroup.setStatus("current")

gnssConfigPosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 4)
)
gnssConfigPosGroup.setObjects(
      *(("SYMMGNSS", "gnssPosSettingLat"),
        ("SYMMGNSS", "gnssPosSettingLong"),
        ("SYMMGNSS", "gnssPosSettingHeight"))
)
if mibBuilder.loadTexts:
    gnssConfigPosGroup.setStatus("current")

gnssCurrentPosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 2, 5)
)
gnssCurrentPosGroup.setObjects(
      *(("SYMMGNSS", "gnssPresentPosLat"),
        ("SYMMGNSS", "gnssPresentPosLong"),
        ("SYMMGNSS", "gnssPresentPosHeight"))
)
if mibBuilder.loadTexts:
    gnssCurrentPosGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gnssBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    gnssBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMGNSS",
    **{"GNSSCURPOSITIONMODE": GNSSCURPOSITIONMODE,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmGNSS": symmGNSS,
       "gnssStatus": gnssStatus,
       "gnssPortStatusTable": gnssPortStatusTable,
       "gnssPortStatusEntry": gnssPortStatusEntry,
       "gnssPortStatusIndex": gnssPortStatusIndex,
       "gnssPortStatusPortName": gnssPortStatusPortName,
       "gnssPortCurrentGNSS": gnssPortCurrentGNSS,
       "gnssPortCurrentPosMode": gnssPortCurrentPosMode,
       "gnssSatTable": gnssSatTable,
       "gnssSatEntry": gnssSatEntry,
       "gnssSatIndex": gnssSatIndex,
       "gnssSatNum": gnssSatNum,
       "gnssSatSNR": gnssSatSNR,
       "gnssSatHealth": gnssSatHealth,
       "gnssSatAzimuth": gnssSatAzimuth,
       "gnssSatElevation": gnssSatElevation,
       "gnssSatPortName": gnssSatPortName,
       "gnssPresentPosTable": gnssPresentPosTable,
       "gnssPresentPosEntry": gnssPresentPosEntry,
       "gnssPresentPosIndex": gnssPresentPosIndex,
       "gnssPresentPosLat": gnssPresentPosLat,
       "gnssPresentPosLong": gnssPresentPosLong,
       "gnssPresentPosHeight": gnssPresentPosHeight,
       "gnssConfig": gnssConfig,
       "gnssConfigurationTable": gnssConfigurationTable,
       "gnssConfigurationEntry": gnssConfigurationEntry,
       "gnssConfigurationIndex": gnssConfigurationIndex,
       "gnssConfigurationPortName": gnssConfigurationPortName,
       "gnssConfigurationTrackMode": gnssConfigurationTrackMode,
       "gnssConfigurationPosMode": gnssConfigurationPosMode,
       "gnssConfigurationElevMask": gnssConfigurationElevMask,
       "gnssConfigurationCableDelay": gnssConfigurationCableDelay,
       "gnssConfigurationLeapSeconds": gnssConfigurationLeapSeconds,
       "gnssPosSettingTable": gnssPosSettingTable,
       "gnssPosSettingEntry": gnssPosSettingEntry,
       "gnssPosSettingIndex": gnssPosSettingIndex,
       "gnssPosSettingLat": gnssPosSettingLat,
       "gnssPosSettingLong": gnssPosSettingLong,
       "gnssPosSettingHeight": gnssPosSettingHeight,
       "gnssConformance": gnssConformance,
       "gnssCompliances": gnssCompliances,
       "gnssBasicCompliance": gnssBasicCompliance,
       "gnssUocGroups": gnssUocGroups,
       "gnssStatusGroup": gnssStatusGroup,
       "gnssConfigGroup": gnssConfigGroup,
       "gnssSVGroup": gnssSVGroup,
       "gnssConfigPosGroup": gnssConfigPosGroup,
       "gnssCurrentPosGroup": gnssCurrentPosGroup}
)
