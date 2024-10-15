# SNMP MIB module (Sentry4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Sentry4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:19 2024
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

sentry4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4)
)
sentry4.setRevisions(
        ("2016-11-18 23:40",
         "2016-09-21 23:00",
         "2016-04-25 21:40",
         "2015-02-19 10:00",
         "2014-12-23 11:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DeviceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 18),
          ("breakerTripped", 12),
          ("conflict", 23),
          ("disabled", 1),
          ("fuseBlown", 13),
          ("highAlarm", 17),
          ("highWarning", 16),
          ("lost", 8),
          ("lowAlarm", 14),
          ("lowWarning", 15),
          ("noComm", 10),
          ("normal", 0),
          ("notFound", 7),
          ("nvmFail", 21),
          ("overLimit", 20),
          ("profileError", 22),
          ("purged", 2),
          ("pwrError", 11),
          ("readError", 9),
          ("reading", 5),
          ("settle", 6),
          ("underLimit", 19))
    )



class DeviceState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unknown", 0))
    )



class EventNotificationMethods(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_ServerTech_ObjectIdentity = ObjectIdentity
serverTech = _ServerTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718)
)
_St4Objects_ObjectIdentity = ObjectIdentity
st4Objects = _St4Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1)
)
_St4System_ObjectIdentity = ObjectIdentity
st4System = _St4System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1)
)
_St4SystemConfig_ObjectIdentity = ObjectIdentity
st4SystemConfig = _St4SystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1)
)


class _St4SystemProductName_Type(DisplayString):
    """Custom type st4SystemProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_St4SystemProductName_Type.__name__ = "DisplayString"
_St4SystemProductName_Object = MibScalar
st4SystemProductName = _St4SystemProductName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 1),
    _St4SystemProductName_Type()
)
st4SystemProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4SystemProductName.setStatus("current")


class _St4SystemLocation_Type(DisplayString):
    """Custom type st4SystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_St4SystemLocation_Type.__name__ = "DisplayString"
_St4SystemLocation_Object = MibScalar
st4SystemLocation = _St4SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 2),
    _St4SystemLocation_Type()
)
st4SystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4SystemLocation.setStatus("current")


class _St4SystemFirmwareVersion_Type(DisplayString):
    """Custom type st4SystemFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_St4SystemFirmwareVersion_Type.__name__ = "DisplayString"
_St4SystemFirmwareVersion_Object = MibScalar
st4SystemFirmwareVersion = _St4SystemFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 3),
    _St4SystemFirmwareVersion_Type()
)
st4SystemFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4SystemFirmwareVersion.setStatus("current")


class _St4SystemFirmwareBuildInfo_Type(DisplayString):
    """Custom type st4SystemFirmwareBuildInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_St4SystemFirmwareBuildInfo_Type.__name__ = "DisplayString"
_St4SystemFirmwareBuildInfo_Object = MibScalar
st4SystemFirmwareBuildInfo = _St4SystemFirmwareBuildInfo_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 4),
    _St4SystemFirmwareBuildInfo_Type()
)
st4SystemFirmwareBuildInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4SystemFirmwareBuildInfo.setStatus("current")


class _St4SystemNICSerialNumber_Type(DisplayString):
    """Custom type st4SystemNICSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_St4SystemNICSerialNumber_Type.__name__ = "DisplayString"
_St4SystemNICSerialNumber_Object = MibScalar
st4SystemNICSerialNumber = _St4SystemNICSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 5),
    _St4SystemNICSerialNumber_Type()
)
st4SystemNICSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4SystemNICSerialNumber.setStatus("current")


class _St4SystemNICHardwareInfo_Type(DisplayString):
    """Custom type st4SystemNICHardwareInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_St4SystemNICHardwareInfo_Type.__name__ = "DisplayString"
_St4SystemNICHardwareInfo_Object = MibScalar
st4SystemNICHardwareInfo = _St4SystemNICHardwareInfo_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 6),
    _St4SystemNICHardwareInfo_Type()
)
st4SystemNICHardwareInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4SystemNICHardwareInfo.setStatus("current")


class _St4SystemProductSeries_Type(Integer32):
    """Custom type st4SystemProductSeries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pro1", 0),
          ("pro2", 1))
    )


_St4SystemProductSeries_Type.__name__ = "Integer32"
_St4SystemProductSeries_Object = MibScalar
st4SystemProductSeries = _St4SystemProductSeries_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 7),
    _St4SystemProductSeries_Type()
)
st4SystemProductSeries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4SystemProductSeries.setStatus("current")


class _St4SystemFeatures_Type(Bits):
    """Custom type st4SystemFeatures based on Bits"""
    namedValues = NamedValues(
        *(("outletControlInhibit", 2),
          ("reserved", 1),
          ("smartLoadShedding", 0))
    )

_St4SystemFeatures_Type.__name__ = "Bits"
_St4SystemFeatures_Object = MibScalar
st4SystemFeatures = _St4SystemFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 10),
    _St4SystemFeatures_Type()
)
st4SystemFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4SystemFeatures.setStatus("current")


class _St4SystemFeatureKey_Type(DisplayString):
    """Custom type st4SystemFeatureKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_St4SystemFeatureKey_Type.__name__ = "DisplayString"
_St4SystemFeatureKey_Object = MibScalar
st4SystemFeatureKey = _St4SystemFeatureKey_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 11),
    _St4SystemFeatureKey_Type()
)
st4SystemFeatureKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4SystemFeatureKey.setStatus("current")


class _St4SystemConfigModifiedCount_Type(Integer32):
    """Custom type st4SystemConfigModifiedCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_St4SystemConfigModifiedCount_Type.__name__ = "Integer32"
_St4SystemConfigModifiedCount_Object = MibScalar
st4SystemConfigModifiedCount = _St4SystemConfigModifiedCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 20),
    _St4SystemConfigModifiedCount_Type()
)
st4SystemConfigModifiedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4SystemConfigModifiedCount.setStatus("current")


class _St4SystemUnitCount_Type(Integer32):
    """Custom type st4SystemUnitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_St4SystemUnitCount_Type.__name__ = "Integer32"
_St4SystemUnitCount_Object = MibScalar
st4SystemUnitCount = _St4SystemUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 1, 1, 21),
    _St4SystemUnitCount_Type()
)
st4SystemUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4SystemUnitCount.setStatus("current")
_St4Units_ObjectIdentity = ObjectIdentity
st4Units = _St4Units_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2)
)
_St4UnitCommonConfig_ObjectIdentity = ObjectIdentity
st4UnitCommonConfig = _St4UnitCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 1)
)
_St4UnitConfigTable_Object = MibTable
st4UnitConfigTable = _St4UnitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    st4UnitConfigTable.setStatus("current")
_St4UnitConfigEntry_Object = MibTableRow
st4UnitConfigEntry = _St4UnitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1)
)
st4UnitConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
)
if mibBuilder.loadTexts:
    st4UnitConfigEntry.setStatus("current")


class _St4UnitIndex_Type(Integer32):
    """Custom type st4UnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_St4UnitIndex_Type.__name__ = "Integer32"
_St4UnitIndex_Object = MibTableColumn
st4UnitIndex = _St4UnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 1),
    _St4UnitIndex_Type()
)
st4UnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4UnitIndex.setStatus("current")


class _St4UnitID_Type(DisplayString):
    """Custom type st4UnitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_St4UnitID_Type.__name__ = "DisplayString"
_St4UnitID_Object = MibTableColumn
st4UnitID = _St4UnitID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 2),
    _St4UnitID_Type()
)
st4UnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitID.setStatus("current")


class _St4UnitName_Type(DisplayString):
    """Custom type st4UnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4UnitName_Type.__name__ = "DisplayString"
_St4UnitName_Object = MibTableColumn
st4UnitName = _St4UnitName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 3),
    _St4UnitName_Type()
)
st4UnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4UnitName.setStatus("current")


class _St4UnitProductSN_Type(DisplayString):
    """Custom type st4UnitProductSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4UnitProductSN_Type.__name__ = "DisplayString"
_St4UnitProductSN_Object = MibTableColumn
st4UnitProductSN = _St4UnitProductSN_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 4),
    _St4UnitProductSN_Type()
)
st4UnitProductSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitProductSN.setStatus("current")


class _St4UnitModel_Type(DisplayString):
    """Custom type st4UnitModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4UnitModel_Type.__name__ = "DisplayString"
_St4UnitModel_Object = MibTableColumn
st4UnitModel = _St4UnitModel_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 5),
    _St4UnitModel_Type()
)
st4UnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitModel.setStatus("current")


class _St4UnitAssetTag_Type(DisplayString):
    """Custom type st4UnitAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4UnitAssetTag_Type.__name__ = "DisplayString"
_St4UnitAssetTag_Object = MibTableColumn
st4UnitAssetTag = _St4UnitAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 6),
    _St4UnitAssetTag_Type()
)
st4UnitAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4UnitAssetTag.setStatus("current")


class _St4UnitType_Type(Integer32):
    """Custom type st4UnitType based on Integer32"""
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
        *(("controller", 2),
          ("emcu", 3),
          ("linkPdu", 1),
          ("masterPdu", 0))
    )


_St4UnitType_Type.__name__ = "Integer32"
_St4UnitType_Object = MibTableColumn
st4UnitType = _St4UnitType_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 7),
    _St4UnitType_Type()
)
st4UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitType.setStatus("current")


class _St4UnitCapabilities_Type(Bits):
    """Custom type st4UnitCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dc", 0),
          ("delta", 3),
          ("phase3", 1),
          ("wye", 2))
    )

_St4UnitCapabilities_Type.__name__ = "Bits"
_St4UnitCapabilities_Object = MibTableColumn
st4UnitCapabilities = _St4UnitCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 8),
    _St4UnitCapabilities_Type()
)
st4UnitCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitCapabilities.setStatus("current")


class _St4UnitProductMfrDate_Type(DisplayString):
    """Custom type st4UnitProductMfrDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_St4UnitProductMfrDate_Type.__name__ = "DisplayString"
_St4UnitProductMfrDate_Object = MibTableColumn
st4UnitProductMfrDate = _St4UnitProductMfrDate_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 9),
    _St4UnitProductMfrDate_Type()
)
st4UnitProductMfrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitProductMfrDate.setStatus("current")


class _St4UnitDisplayOrientation_Type(Integer32):
    """Custom type st4UnitDisplayOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("inverted", 1),
          ("normal", 0))
    )


_St4UnitDisplayOrientation_Type.__name__ = "Integer32"
_St4UnitDisplayOrientation_Object = MibTableColumn
st4UnitDisplayOrientation = _St4UnitDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 20),
    _St4UnitDisplayOrientation_Type()
)
st4UnitDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4UnitDisplayOrientation.setStatus("current")


class _St4UnitOutletSequenceOrder_Type(Integer32):
    """Custom type st4UnitOutletSequenceOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reversed", 1))
    )


_St4UnitOutletSequenceOrder_Type.__name__ = "Integer32"
_St4UnitOutletSequenceOrder_Object = MibTableColumn
st4UnitOutletSequenceOrder = _St4UnitOutletSequenceOrder_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 21),
    _St4UnitOutletSequenceOrder_Type()
)
st4UnitOutletSequenceOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4UnitOutletSequenceOrder.setStatus("current")


class _St4UnitInputCordCount_Type(Integer32):
    """Custom type st4UnitInputCordCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_St4UnitInputCordCount_Type.__name__ = "Integer32"
_St4UnitInputCordCount_Object = MibTableColumn
st4UnitInputCordCount = _St4UnitInputCordCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 30),
    _St4UnitInputCordCount_Type()
)
st4UnitInputCordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitInputCordCount.setStatus("current")


class _St4UnitTempSensorCount_Type(Integer32):
    """Custom type st4UnitTempSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_St4UnitTempSensorCount_Type.__name__ = "Integer32"
_St4UnitTempSensorCount_Object = MibTableColumn
st4UnitTempSensorCount = _St4UnitTempSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 31),
    _St4UnitTempSensorCount_Type()
)
st4UnitTempSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitTempSensorCount.setStatus("current")


class _St4UnitHumidSensorCount_Type(Integer32):
    """Custom type st4UnitHumidSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_St4UnitHumidSensorCount_Type.__name__ = "Integer32"
_St4UnitHumidSensorCount_Object = MibTableColumn
st4UnitHumidSensorCount = _St4UnitHumidSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 32),
    _St4UnitHumidSensorCount_Type()
)
st4UnitHumidSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitHumidSensorCount.setStatus("current")


class _St4UnitWaterSensorCount_Type(Integer32):
    """Custom type st4UnitWaterSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_St4UnitWaterSensorCount_Type.__name__ = "Integer32"
_St4UnitWaterSensorCount_Object = MibTableColumn
st4UnitWaterSensorCount = _St4UnitWaterSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 33),
    _St4UnitWaterSensorCount_Type()
)
st4UnitWaterSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitWaterSensorCount.setStatus("current")


class _St4UnitCcSensorCount_Type(Integer32):
    """Custom type st4UnitCcSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_St4UnitCcSensorCount_Type.__name__ = "Integer32"
_St4UnitCcSensorCount_Object = MibTableColumn
st4UnitCcSensorCount = _St4UnitCcSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 34),
    _St4UnitCcSensorCount_Type()
)
st4UnitCcSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitCcSensorCount.setStatus("current")


class _St4UnitAdcSensorCount_Type(Integer32):
    """Custom type st4UnitAdcSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_St4UnitAdcSensorCount_Type.__name__ = "Integer32"
_St4UnitAdcSensorCount_Object = MibTableColumn
st4UnitAdcSensorCount = _St4UnitAdcSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 2, 1, 35),
    _St4UnitAdcSensorCount_Type()
)
st4UnitAdcSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitAdcSensorCount.setStatus("current")
_St4UnitMonitorTable_Object = MibTable
st4UnitMonitorTable = _St4UnitMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    st4UnitMonitorTable.setStatus("current")
_St4UnitMonitorEntry_Object = MibTableRow
st4UnitMonitorEntry = _St4UnitMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 3, 1)
)
st4UnitMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
)
if mibBuilder.loadTexts:
    st4UnitMonitorEntry.setStatus("current")
_St4UnitStatus_Type = DeviceStatus
_St4UnitStatus_Object = MibTableColumn
st4UnitStatus = _St4UnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 3, 1, 1),
    _St4UnitStatus_Type()
)
st4UnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4UnitStatus.setStatus("current")
_St4UnitEventConfigTable_Object = MibTable
st4UnitEventConfigTable = _St4UnitEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    st4UnitEventConfigTable.setStatus("current")
_St4UnitEventConfigEntry_Object = MibTableRow
st4UnitEventConfigEntry = _St4UnitEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 4, 1)
)
st4UnitEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
)
if mibBuilder.loadTexts:
    st4UnitEventConfigEntry.setStatus("current")
_St4UnitNotifications_Type = EventNotificationMethods
_St4UnitNotifications_Object = MibTableColumn
st4UnitNotifications = _St4UnitNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 2, 4, 1, 1),
    _St4UnitNotifications_Type()
)
st4UnitNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4UnitNotifications.setStatus("current")
_St4InputCords_ObjectIdentity = ObjectIdentity
st4InputCords = _St4InputCords_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3)
)
_St4InputCordCommonConfig_ObjectIdentity = ObjectIdentity
st4InputCordCommonConfig = _St4InputCordCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 1)
)


class _St4InputCordActivePowerHysteresis_Type(Integer32):
    """Custom type st4InputCordActivePowerHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_St4InputCordActivePowerHysteresis_Type.__name__ = "Integer32"
_St4InputCordActivePowerHysteresis_Object = MibScalar
st4InputCordActivePowerHysteresis = _St4InputCordActivePowerHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 1, 1),
    _St4InputCordActivePowerHysteresis_Type()
)
st4InputCordActivePowerHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordActivePowerHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordActivePowerHysteresis.setUnits("Watts")


class _St4InputCordApparentPowerHysteresis_Type(Integer32):
    """Custom type st4InputCordApparentPowerHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_St4InputCordApparentPowerHysteresis_Type.__name__ = "Integer32"
_St4InputCordApparentPowerHysteresis_Object = MibScalar
st4InputCordApparentPowerHysteresis = _St4InputCordApparentPowerHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 1, 2),
    _St4InputCordApparentPowerHysteresis_Type()
)
st4InputCordApparentPowerHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerHysteresis.setUnits("Volt-Amps")


class _St4InputCordPowerFactorHysteresis_Type(Integer32):
    """Custom type st4InputCordPowerFactorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_St4InputCordPowerFactorHysteresis_Type.__name__ = "Integer32"
_St4InputCordPowerFactorHysteresis_Object = MibScalar
st4InputCordPowerFactorHysteresis = _St4InputCordPowerFactorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 1, 3),
    _St4InputCordPowerFactorHysteresis_Type()
)
st4InputCordPowerFactorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordPowerFactorHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordPowerFactorHysteresis.setUnits("hundredths")


class _St4InputCordOutOfBalanceHysteresis_Type(Integer32):
    """Custom type st4InputCordOutOfBalanceHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_St4InputCordOutOfBalanceHysteresis_Type.__name__ = "Integer32"
_St4InputCordOutOfBalanceHysteresis_Object = MibScalar
st4InputCordOutOfBalanceHysteresis = _St4InputCordOutOfBalanceHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 1, 4),
    _St4InputCordOutOfBalanceHysteresis_Type()
)
st4InputCordOutOfBalanceHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordOutOfBalanceHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordOutOfBalanceHysteresis.setUnits("percent")
_St4InputCordConfigTable_Object = MibTable
st4InputCordConfigTable = _St4InputCordConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    st4InputCordConfigTable.setStatus("current")
_St4InputCordConfigEntry_Object = MibTableRow
st4InputCordConfigEntry = _St4InputCordConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1)
)
st4InputCordConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
)
if mibBuilder.loadTexts:
    st4InputCordConfigEntry.setStatus("current")


class _St4InputCordIndex_Type(Integer32):
    """Custom type st4InputCordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_St4InputCordIndex_Type.__name__ = "Integer32"
_St4InputCordIndex_Object = MibTableColumn
st4InputCordIndex = _St4InputCordIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 1),
    _St4InputCordIndex_Type()
)
st4InputCordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4InputCordIndex.setStatus("current")


class _St4InputCordID_Type(DisplayString):
    """Custom type st4InputCordID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_St4InputCordID_Type.__name__ = "DisplayString"
_St4InputCordID_Object = MibTableColumn
st4InputCordID = _St4InputCordID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 2),
    _St4InputCordID_Type()
)
st4InputCordID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordID.setStatus("current")


class _St4InputCordName_Type(DisplayString):
    """Custom type st4InputCordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4InputCordName_Type.__name__ = "DisplayString"
_St4InputCordName_Object = MibTableColumn
st4InputCordName = _St4InputCordName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 3),
    _St4InputCordName_Type()
)
st4InputCordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordName.setStatus("current")


class _St4InputCordInletType_Type(DisplayString):
    """Custom type st4InputCordInletType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4InputCordInletType_Type.__name__ = "DisplayString"
_St4InputCordInletType_Object = MibTableColumn
st4InputCordInletType = _St4InputCordInletType_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 6),
    _St4InputCordInletType_Type()
)
st4InputCordInletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordInletType.setStatus("current")


class _St4InputCordNominalVoltage_Type(Integer32):
    """Custom type st4InputCordNominalVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4InputCordNominalVoltage_Type.__name__ = "Integer32"
_St4InputCordNominalVoltage_Object = MibTableColumn
st4InputCordNominalVoltage = _St4InputCordNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 7),
    _St4InputCordNominalVoltage_Type()
)
st4InputCordNominalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordNominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordNominalVoltage.setUnits("tenth Volts")


class _St4InputCordNominalVoltageMin_Type(Integer32):
    """Custom type st4InputCordNominalVoltageMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_St4InputCordNominalVoltageMin_Type.__name__ = "Integer32"
_St4InputCordNominalVoltageMin_Object = MibTableColumn
st4InputCordNominalVoltageMin = _St4InputCordNominalVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 8),
    _St4InputCordNominalVoltageMin_Type()
)
st4InputCordNominalVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordNominalVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordNominalVoltageMin.setUnits("Volts")


class _St4InputCordNominalVoltageMax_Type(Integer32):
    """Custom type st4InputCordNominalVoltageMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_St4InputCordNominalVoltageMax_Type.__name__ = "Integer32"
_St4InputCordNominalVoltageMax_Object = MibTableColumn
st4InputCordNominalVoltageMax = _St4InputCordNominalVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 9),
    _St4InputCordNominalVoltageMax_Type()
)
st4InputCordNominalVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordNominalVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordNominalVoltageMax.setUnits("Volts")


class _St4InputCordCurrentCapacity_Type(Integer32):
    """Custom type st4InputCordCurrentCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_St4InputCordCurrentCapacity_Type.__name__ = "Integer32"
_St4InputCordCurrentCapacity_Object = MibTableColumn
st4InputCordCurrentCapacity = _St4InputCordCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 10),
    _St4InputCordCurrentCapacity_Type()
)
st4InputCordCurrentCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordCurrentCapacity.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordCurrentCapacity.setUnits("Amps")


class _St4InputCordCurrentCapacityMax_Type(Integer32):
    """Custom type st4InputCordCurrentCapacityMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_St4InputCordCurrentCapacityMax_Type.__name__ = "Integer32"
_St4InputCordCurrentCapacityMax_Object = MibTableColumn
st4InputCordCurrentCapacityMax = _St4InputCordCurrentCapacityMax_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 11),
    _St4InputCordCurrentCapacityMax_Type()
)
st4InputCordCurrentCapacityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordCurrentCapacityMax.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordCurrentCapacityMax.setUnits("Amps")


class _St4InputCordPowerCapacity_Type(Integer32):
    """Custom type st4InputCordPowerCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_St4InputCordPowerCapacity_Type.__name__ = "Integer32"
_St4InputCordPowerCapacity_Object = MibTableColumn
st4InputCordPowerCapacity = _St4InputCordPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 12),
    _St4InputCordPowerCapacity_Type()
)
st4InputCordPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordPowerCapacity.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordPowerCapacity.setUnits("Volt-Amps")


class _St4InputCordNominalPowerFactor_Type(Integer32):
    """Custom type st4InputCordNominalPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4InputCordNominalPowerFactor_Type.__name__ = "Integer32"
_St4InputCordNominalPowerFactor_Object = MibTableColumn
st4InputCordNominalPowerFactor = _St4InputCordNominalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 13),
    _St4InputCordNominalPowerFactor_Type()
)
st4InputCordNominalPowerFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordNominalPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordNominalPowerFactor.setUnits("hundredths")


class _St4InputCordLineCount_Type(Integer32):
    """Custom type st4InputCordLineCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_St4InputCordLineCount_Type.__name__ = "Integer32"
_St4InputCordLineCount_Object = MibTableColumn
st4InputCordLineCount = _St4InputCordLineCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 20),
    _St4InputCordLineCount_Type()
)
st4InputCordLineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordLineCount.setStatus("current")


class _St4InputCordPhaseCount_Type(Integer32):
    """Custom type st4InputCordPhaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_St4InputCordPhaseCount_Type.__name__ = "Integer32"
_St4InputCordPhaseCount_Object = MibTableColumn
st4InputCordPhaseCount = _St4InputCordPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 21),
    _St4InputCordPhaseCount_Type()
)
st4InputCordPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordPhaseCount.setStatus("current")


class _St4InputCordOcpCount_Type(Integer32):
    """Custom type st4InputCordOcpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_St4InputCordOcpCount_Type.__name__ = "Integer32"
_St4InputCordOcpCount_Object = MibTableColumn
st4InputCordOcpCount = _St4InputCordOcpCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 22),
    _St4InputCordOcpCount_Type()
)
st4InputCordOcpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordOcpCount.setStatus("current")


class _St4InputCordBranchCount_Type(Integer32):
    """Custom type st4InputCordBranchCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_St4InputCordBranchCount_Type.__name__ = "Integer32"
_St4InputCordBranchCount_Object = MibTableColumn
st4InputCordBranchCount = _St4InputCordBranchCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 23),
    _St4InputCordBranchCount_Type()
)
st4InputCordBranchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordBranchCount.setStatus("current")


class _St4InputCordOutletCount_Type(Integer32):
    """Custom type st4InputCordOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_St4InputCordOutletCount_Type.__name__ = "Integer32"
_St4InputCordOutletCount_Object = MibTableColumn
st4InputCordOutletCount = _St4InputCordOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 2, 1, 24),
    _St4InputCordOutletCount_Type()
)
st4InputCordOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordOutletCount.setStatus("current")
_St4InputCordMonitorTable_Object = MibTable
st4InputCordMonitorTable = _St4InputCordMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    st4InputCordMonitorTable.setStatus("current")
_St4InputCordMonitorEntry_Object = MibTableRow
st4InputCordMonitorEntry = _St4InputCordMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1)
)
st4InputCordMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
)
if mibBuilder.loadTexts:
    st4InputCordMonitorEntry.setStatus("current")
_St4InputCordState_Type = DeviceState
_St4InputCordState_Object = MibTableColumn
st4InputCordState = _St4InputCordState_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 1),
    _St4InputCordState_Type()
)
st4InputCordState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordState.setStatus("current")
_St4InputCordStatus_Type = DeviceStatus
_St4InputCordStatus_Object = MibTableColumn
st4InputCordStatus = _St4InputCordStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 2),
    _St4InputCordStatus_Type()
)
st4InputCordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordStatus.setStatus("current")


class _St4InputCordActivePower_Type(Integer32):
    """Custom type st4InputCordActivePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 50000),
    )


_St4InputCordActivePower_Type.__name__ = "Integer32"
_St4InputCordActivePower_Object = MibTableColumn
st4InputCordActivePower = _St4InputCordActivePower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 3),
    _St4InputCordActivePower_Type()
)
st4InputCordActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordActivePower.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordActivePower.setUnits("Watts")
_St4InputCordActivePowerStatus_Type = DeviceStatus
_St4InputCordActivePowerStatus_Object = MibTableColumn
st4InputCordActivePowerStatus = _St4InputCordActivePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 4),
    _St4InputCordActivePowerStatus_Type()
)
st4InputCordActivePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordActivePowerStatus.setStatus("current")


class _St4InputCordApparentPower_Type(Integer32):
    """Custom type st4InputCordApparentPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 50000),
    )


_St4InputCordApparentPower_Type.__name__ = "Integer32"
_St4InputCordApparentPower_Object = MibTableColumn
st4InputCordApparentPower = _St4InputCordApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 5),
    _St4InputCordApparentPower_Type()
)
st4InputCordApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordApparentPower.setUnits("Volt-Amps")
_St4InputCordApparentPowerStatus_Type = DeviceStatus
_St4InputCordApparentPowerStatus_Object = MibTableColumn
st4InputCordApparentPowerStatus = _St4InputCordApparentPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 6),
    _St4InputCordApparentPowerStatus_Type()
)
st4InputCordApparentPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerStatus.setStatus("current")


class _St4InputCordPowerUtilized_Type(Integer32):
    """Custom type st4InputCordPowerUtilized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1200),
    )


_St4InputCordPowerUtilized_Type.__name__ = "Integer32"
_St4InputCordPowerUtilized_Object = MibTableColumn
st4InputCordPowerUtilized = _St4InputCordPowerUtilized_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 7),
    _St4InputCordPowerUtilized_Type()
)
st4InputCordPowerUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordPowerUtilized.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordPowerUtilized.setUnits("tenth percent")


class _St4InputCordPowerFactor_Type(Integer32):
    """Custom type st4InputCordPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_St4InputCordPowerFactor_Type.__name__ = "Integer32"
_St4InputCordPowerFactor_Object = MibTableColumn
st4InputCordPowerFactor = _St4InputCordPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 8),
    _St4InputCordPowerFactor_Type()
)
st4InputCordPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordPowerFactor.setUnits("hundredths")
_St4InputCordPowerFactorStatus_Type = DeviceStatus
_St4InputCordPowerFactorStatus_Object = MibTableColumn
st4InputCordPowerFactorStatus = _St4InputCordPowerFactorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 9),
    _St4InputCordPowerFactorStatus_Type()
)
st4InputCordPowerFactorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordPowerFactorStatus.setStatus("current")


class _St4InputCordEnergy_Type(Integer32):
    """Custom type st4InputCordEnergy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_St4InputCordEnergy_Type.__name__ = "Integer32"
_St4InputCordEnergy_Object = MibTableColumn
st4InputCordEnergy = _St4InputCordEnergy_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 10),
    _St4InputCordEnergy_Type()
)
st4InputCordEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordEnergy.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordEnergy.setUnits("tenth Kilowatt-Hours")


class _St4InputCordFrequency_Type(Integer32):
    """Custom type st4InputCordFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_St4InputCordFrequency_Type.__name__ = "Integer32"
_St4InputCordFrequency_Object = MibTableColumn
st4InputCordFrequency = _St4InputCordFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 11),
    _St4InputCordFrequency_Type()
)
st4InputCordFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordFrequency.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordFrequency.setUnits("tenth Hertz")


class _St4InputCordOutOfBalance_Type(Integer32):
    """Custom type st4InputCordOutOfBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2000),
    )


_St4InputCordOutOfBalance_Type.__name__ = "Integer32"
_St4InputCordOutOfBalance_Object = MibTableColumn
st4InputCordOutOfBalance = _St4InputCordOutOfBalance_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 12),
    _St4InputCordOutOfBalance_Type()
)
st4InputCordOutOfBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordOutOfBalance.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordOutOfBalance.setUnits("tenth percent")
_St4InputCordOutOfBalanceStatus_Type = DeviceStatus
_St4InputCordOutOfBalanceStatus_Object = MibTableColumn
st4InputCordOutOfBalanceStatus = _St4InputCordOutOfBalanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 3, 1, 13),
    _St4InputCordOutOfBalanceStatus_Type()
)
st4InputCordOutOfBalanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4InputCordOutOfBalanceStatus.setStatus("current")
_St4InputCordEventConfigTable_Object = MibTable
st4InputCordEventConfigTable = _St4InputCordEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4)
)
if mibBuilder.loadTexts:
    st4InputCordEventConfigTable.setStatus("current")
_St4InputCordEventConfigEntry_Object = MibTableRow
st4InputCordEventConfigEntry = _St4InputCordEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1)
)
st4InputCordEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
)
if mibBuilder.loadTexts:
    st4InputCordEventConfigEntry.setStatus("current")
_St4InputCordNotifications_Type = EventNotificationMethods
_St4InputCordNotifications_Object = MibTableColumn
st4InputCordNotifications = _St4InputCordNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 1),
    _St4InputCordNotifications_Type()
)
st4InputCordNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordNotifications.setStatus("current")


class _St4InputCordActivePowerLowAlarm_Type(Integer32):
    """Custom type st4InputCordActivePowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_St4InputCordActivePowerLowAlarm_Type.__name__ = "Integer32"
_St4InputCordActivePowerLowAlarm_Object = MibTableColumn
st4InputCordActivePowerLowAlarm = _St4InputCordActivePowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 2),
    _St4InputCordActivePowerLowAlarm_Type()
)
st4InputCordActivePowerLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordActivePowerLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordActivePowerLowAlarm.setUnits("Watts")


class _St4InputCordActivePowerLowWarning_Type(Integer32):
    """Custom type st4InputCordActivePowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_St4InputCordActivePowerLowWarning_Type.__name__ = "Integer32"
_St4InputCordActivePowerLowWarning_Object = MibTableColumn
st4InputCordActivePowerLowWarning = _St4InputCordActivePowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 3),
    _St4InputCordActivePowerLowWarning_Type()
)
st4InputCordActivePowerLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordActivePowerLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordActivePowerLowWarning.setUnits("Watts")


class _St4InputCordActivePowerHighWarning_Type(Integer32):
    """Custom type st4InputCordActivePowerHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_St4InputCordActivePowerHighWarning_Type.__name__ = "Integer32"
_St4InputCordActivePowerHighWarning_Object = MibTableColumn
st4InputCordActivePowerHighWarning = _St4InputCordActivePowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 4),
    _St4InputCordActivePowerHighWarning_Type()
)
st4InputCordActivePowerHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordActivePowerHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordActivePowerHighWarning.setUnits("Watts")


class _St4InputCordActivePowerHighAlarm_Type(Integer32):
    """Custom type st4InputCordActivePowerHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_St4InputCordActivePowerHighAlarm_Type.__name__ = "Integer32"
_St4InputCordActivePowerHighAlarm_Object = MibTableColumn
st4InputCordActivePowerHighAlarm = _St4InputCordActivePowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 5),
    _St4InputCordActivePowerHighAlarm_Type()
)
st4InputCordActivePowerHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordActivePowerHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordActivePowerHighAlarm.setUnits("Watts")


class _St4InputCordApparentPowerLowAlarm_Type(Integer32):
    """Custom type st4InputCordApparentPowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_St4InputCordApparentPowerLowAlarm_Type.__name__ = "Integer32"
_St4InputCordApparentPowerLowAlarm_Object = MibTableColumn
st4InputCordApparentPowerLowAlarm = _St4InputCordApparentPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 6),
    _St4InputCordApparentPowerLowAlarm_Type()
)
st4InputCordApparentPowerLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerLowAlarm.setUnits("Volt-Amps")


class _St4InputCordApparentPowerLowWarning_Type(Integer32):
    """Custom type st4InputCordApparentPowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_St4InputCordApparentPowerLowWarning_Type.__name__ = "Integer32"
_St4InputCordApparentPowerLowWarning_Object = MibTableColumn
st4InputCordApparentPowerLowWarning = _St4InputCordApparentPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 7),
    _St4InputCordApparentPowerLowWarning_Type()
)
st4InputCordApparentPowerLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerLowWarning.setUnits("Volt-Amps")


class _St4InputCordApparentPowerHighWarning_Type(Integer32):
    """Custom type st4InputCordApparentPowerHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_St4InputCordApparentPowerHighWarning_Type.__name__ = "Integer32"
_St4InputCordApparentPowerHighWarning_Object = MibTableColumn
st4InputCordApparentPowerHighWarning = _St4InputCordApparentPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 8),
    _St4InputCordApparentPowerHighWarning_Type()
)
st4InputCordApparentPowerHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerHighWarning.setUnits("Volt-Amps")


class _St4InputCordApparentPowerHighAlarm_Type(Integer32):
    """Custom type st4InputCordApparentPowerHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_St4InputCordApparentPowerHighAlarm_Type.__name__ = "Integer32"
_St4InputCordApparentPowerHighAlarm_Object = MibTableColumn
st4InputCordApparentPowerHighAlarm = _St4InputCordApparentPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 9),
    _St4InputCordApparentPowerHighAlarm_Type()
)
st4InputCordApparentPowerHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordApparentPowerHighAlarm.setUnits("Volt-Amps")


class _St4InputCordPowerFactorLowAlarm_Type(Integer32):
    """Custom type st4InputCordPowerFactorLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4InputCordPowerFactorLowAlarm_Type.__name__ = "Integer32"
_St4InputCordPowerFactorLowAlarm_Object = MibTableColumn
st4InputCordPowerFactorLowAlarm = _St4InputCordPowerFactorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 10),
    _St4InputCordPowerFactorLowAlarm_Type()
)
st4InputCordPowerFactorLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordPowerFactorLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordPowerFactorLowAlarm.setUnits("hundredths")


class _St4InputCordPowerFactorLowWarning_Type(Integer32):
    """Custom type st4InputCordPowerFactorLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4InputCordPowerFactorLowWarning_Type.__name__ = "Integer32"
_St4InputCordPowerFactorLowWarning_Object = MibTableColumn
st4InputCordPowerFactorLowWarning = _St4InputCordPowerFactorLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 11),
    _St4InputCordPowerFactorLowWarning_Type()
)
st4InputCordPowerFactorLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordPowerFactorLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordPowerFactorLowWarning.setUnits("hundredths")


class _St4InputCordOutOfBalanceHighWarning_Type(Integer32):
    """Custom type st4InputCordOutOfBalanceHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4InputCordOutOfBalanceHighWarning_Type.__name__ = "Integer32"
_St4InputCordOutOfBalanceHighWarning_Object = MibTableColumn
st4InputCordOutOfBalanceHighWarning = _St4InputCordOutOfBalanceHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 12),
    _St4InputCordOutOfBalanceHighWarning_Type()
)
st4InputCordOutOfBalanceHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordOutOfBalanceHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordOutOfBalanceHighWarning.setUnits("percent")


class _St4InputCordOutOfBalanceHighAlarm_Type(Integer32):
    """Custom type st4InputCordOutOfBalanceHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4InputCordOutOfBalanceHighAlarm_Type.__name__ = "Integer32"
_St4InputCordOutOfBalanceHighAlarm_Object = MibTableColumn
st4InputCordOutOfBalanceHighAlarm = _St4InputCordOutOfBalanceHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 3, 4, 1, 13),
    _St4InputCordOutOfBalanceHighAlarm_Type()
)
st4InputCordOutOfBalanceHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4InputCordOutOfBalanceHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4InputCordOutOfBalanceHighAlarm.setUnits("percent")
_St4Lines_ObjectIdentity = ObjectIdentity
st4Lines = _St4Lines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4)
)
_St4LineCommonConfig_ObjectIdentity = ObjectIdentity
st4LineCommonConfig = _St4LineCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 1)
)


class _St4LineCurrentHysteresis_Type(Integer32):
    """Custom type st4LineCurrentHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4LineCurrentHysteresis_Type.__name__ = "Integer32"
_St4LineCurrentHysteresis_Object = MibScalar
st4LineCurrentHysteresis = _St4LineCurrentHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 1, 1),
    _St4LineCurrentHysteresis_Type()
)
st4LineCurrentHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4LineCurrentHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4LineCurrentHysteresis.setUnits("tenth Amps")
_St4LineConfigTable_Object = MibTable
st4LineConfigTable = _St4LineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    st4LineConfigTable.setStatus("current")
_St4LineConfigEntry_Object = MibTableRow
st4LineConfigEntry = _St4LineConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 2, 1)
)
st4LineConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4LineIndex"),
)
if mibBuilder.loadTexts:
    st4LineConfigEntry.setStatus("current")


class _St4LineIndex_Type(Integer32):
    """Custom type st4LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_St4LineIndex_Type.__name__ = "Integer32"
_St4LineIndex_Object = MibTableColumn
st4LineIndex = _St4LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 2, 1, 1),
    _St4LineIndex_Type()
)
st4LineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4LineIndex.setStatus("current")


class _St4LineID_Type(DisplayString):
    """Custom type st4LineID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_St4LineID_Type.__name__ = "DisplayString"
_St4LineID_Object = MibTableColumn
st4LineID = _St4LineID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 2, 1, 2),
    _St4LineID_Type()
)
st4LineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4LineID.setStatus("current")


class _St4LineLabel_Type(DisplayString):
    """Custom type st4LineLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4LineLabel_Type.__name__ = "DisplayString"
_St4LineLabel_Object = MibTableColumn
st4LineLabel = _St4LineLabel_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 2, 1, 4),
    _St4LineLabel_Type()
)
st4LineLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4LineLabel.setStatus("current")


class _St4LineCurrentCapacity_Type(Integer32):
    """Custom type st4LineCurrentCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_St4LineCurrentCapacity_Type.__name__ = "Integer32"
_St4LineCurrentCapacity_Object = MibTableColumn
st4LineCurrentCapacity = _St4LineCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 2, 1, 6),
    _St4LineCurrentCapacity_Type()
)
st4LineCurrentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4LineCurrentCapacity.setStatus("current")
if mibBuilder.loadTexts:
    st4LineCurrentCapacity.setUnits("Amps")
_St4LineMonitorTable_Object = MibTable
st4LineMonitorTable = _St4LineMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    st4LineMonitorTable.setStatus("current")
_St4LineMonitorEntry_Object = MibTableRow
st4LineMonitorEntry = _St4LineMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 3, 1)
)
st4LineMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4LineIndex"),
)
if mibBuilder.loadTexts:
    st4LineMonitorEntry.setStatus("current")
_St4LineState_Type = DeviceState
_St4LineState_Object = MibTableColumn
st4LineState = _St4LineState_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 3, 1, 1),
    _St4LineState_Type()
)
st4LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4LineState.setStatus("current")
_St4LineStatus_Type = DeviceStatus
_St4LineStatus_Object = MibTableColumn
st4LineStatus = _St4LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 3, 1, 2),
    _St4LineStatus_Type()
)
st4LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4LineStatus.setStatus("current")


class _St4LineCurrent_Type(Integer32):
    """Custom type st4LineCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 60000),
    )


_St4LineCurrent_Type.__name__ = "Integer32"
_St4LineCurrent_Object = MibTableColumn
st4LineCurrent = _St4LineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 3, 1, 3),
    _St4LineCurrent_Type()
)
st4LineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4LineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    st4LineCurrent.setUnits("hundredth Amps")
_St4LineCurrentStatus_Type = DeviceStatus
_St4LineCurrentStatus_Object = MibTableColumn
st4LineCurrentStatus = _St4LineCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 3, 1, 4),
    _St4LineCurrentStatus_Type()
)
st4LineCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4LineCurrentStatus.setStatus("current")


class _St4LineCurrentUtilized_Type(Integer32):
    """Custom type st4LineCurrentUtilized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1200),
    )


_St4LineCurrentUtilized_Type.__name__ = "Integer32"
_St4LineCurrentUtilized_Object = MibTableColumn
st4LineCurrentUtilized = _St4LineCurrentUtilized_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 3, 1, 5),
    _St4LineCurrentUtilized_Type()
)
st4LineCurrentUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4LineCurrentUtilized.setStatus("current")
if mibBuilder.loadTexts:
    st4LineCurrentUtilized.setUnits("tenth percent")
_St4LineEventConfigTable_Object = MibTable
st4LineEventConfigTable = _St4LineEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    st4LineEventConfigTable.setStatus("current")
_St4LineEventConfigEntry_Object = MibTableRow
st4LineEventConfigEntry = _St4LineEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 4, 1)
)
st4LineEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4LineIndex"),
)
if mibBuilder.loadTexts:
    st4LineEventConfigEntry.setStatus("current")
_St4LineNotifications_Type = EventNotificationMethods
_St4LineNotifications_Object = MibTableColumn
st4LineNotifications = _St4LineNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 4, 1, 1),
    _St4LineNotifications_Type()
)
st4LineNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4LineNotifications.setStatus("current")


class _St4LineCurrentLowAlarm_Type(Integer32):
    """Custom type st4LineCurrentLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4LineCurrentLowAlarm_Type.__name__ = "Integer32"
_St4LineCurrentLowAlarm_Object = MibTableColumn
st4LineCurrentLowAlarm = _St4LineCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 4, 1, 2),
    _St4LineCurrentLowAlarm_Type()
)
st4LineCurrentLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4LineCurrentLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4LineCurrentLowAlarm.setUnits("tenth Amps")


class _St4LineCurrentLowWarning_Type(Integer32):
    """Custom type st4LineCurrentLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4LineCurrentLowWarning_Type.__name__ = "Integer32"
_St4LineCurrentLowWarning_Object = MibTableColumn
st4LineCurrentLowWarning = _St4LineCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 4, 1, 3),
    _St4LineCurrentLowWarning_Type()
)
st4LineCurrentLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4LineCurrentLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4LineCurrentLowWarning.setUnits("tenth Amps")


class _St4LineCurrentHighWarning_Type(Integer32):
    """Custom type st4LineCurrentHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4LineCurrentHighWarning_Type.__name__ = "Integer32"
_St4LineCurrentHighWarning_Object = MibTableColumn
st4LineCurrentHighWarning = _St4LineCurrentHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 4, 1, 4),
    _St4LineCurrentHighWarning_Type()
)
st4LineCurrentHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4LineCurrentHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4LineCurrentHighWarning.setUnits("tenth Amps")


class _St4LineCurrentHighAlarm_Type(Integer32):
    """Custom type st4LineCurrentHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4LineCurrentHighAlarm_Type.__name__ = "Integer32"
_St4LineCurrentHighAlarm_Object = MibTableColumn
st4LineCurrentHighAlarm = _St4LineCurrentHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 4, 4, 1, 5),
    _St4LineCurrentHighAlarm_Type()
)
st4LineCurrentHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4LineCurrentHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4LineCurrentHighAlarm.setUnits("tenth Amps")
_St4Phases_ObjectIdentity = ObjectIdentity
st4Phases = _St4Phases_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5)
)
_St4PhaseCommonConfig_ObjectIdentity = ObjectIdentity
st4PhaseCommonConfig = _St4PhaseCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 1)
)


class _St4PhaseVoltageHysteresis_Type(Integer32):
    """Custom type st4PhaseVoltageHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_St4PhaseVoltageHysteresis_Type.__name__ = "Integer32"
_St4PhaseVoltageHysteresis_Object = MibScalar
st4PhaseVoltageHysteresis = _St4PhaseVoltageHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 1, 1),
    _St4PhaseVoltageHysteresis_Type()
)
st4PhaseVoltageHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4PhaseVoltageHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseVoltageHysteresis.setUnits("tenth Volts")


class _St4PhasePowerFactorHysteresis_Type(Integer32):
    """Custom type st4PhasePowerFactorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_St4PhasePowerFactorHysteresis_Type.__name__ = "Integer32"
_St4PhasePowerFactorHysteresis_Object = MibScalar
st4PhasePowerFactorHysteresis = _St4PhasePowerFactorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 1, 2),
    _St4PhasePowerFactorHysteresis_Type()
)
st4PhasePowerFactorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4PhasePowerFactorHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4PhasePowerFactorHysteresis.setUnits("hundredths")
_St4PhaseConfigTable_Object = MibTable
st4PhaseConfigTable = _St4PhaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    st4PhaseConfigTable.setStatus("current")
_St4PhaseConfigEntry_Object = MibTableRow
st4PhaseConfigEntry = _St4PhaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 2, 1)
)
st4PhaseConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4PhaseIndex"),
)
if mibBuilder.loadTexts:
    st4PhaseConfigEntry.setStatus("current")


class _St4PhaseIndex_Type(Integer32):
    """Custom type st4PhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_St4PhaseIndex_Type.__name__ = "Integer32"
_St4PhaseIndex_Object = MibTableColumn
st4PhaseIndex = _St4PhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 2, 1, 1),
    _St4PhaseIndex_Type()
)
st4PhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4PhaseIndex.setStatus("current")


class _St4PhaseID_Type(DisplayString):
    """Custom type st4PhaseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_St4PhaseID_Type.__name__ = "DisplayString"
_St4PhaseID_Object = MibTableColumn
st4PhaseID = _St4PhaseID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 2, 1, 2),
    _St4PhaseID_Type()
)
st4PhaseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseID.setStatus("current")


class _St4PhaseLabel_Type(DisplayString):
    """Custom type st4PhaseLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4PhaseLabel_Type.__name__ = "DisplayString"
_St4PhaseLabel_Object = MibTableColumn
st4PhaseLabel = _St4PhaseLabel_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 2, 1, 4),
    _St4PhaseLabel_Type()
)
st4PhaseLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseLabel.setStatus("current")


class _St4PhaseNominalVoltage_Type(Integer32):
    """Custom type st4PhaseNominalVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4PhaseNominalVoltage_Type.__name__ = "Integer32"
_St4PhaseNominalVoltage_Object = MibTableColumn
st4PhaseNominalVoltage = _St4PhaseNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 2, 1, 6),
    _St4PhaseNominalVoltage_Type()
)
st4PhaseNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseNominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseNominalVoltage.setUnits("tenth Volts")


class _St4PhaseBranchCount_Type(Integer32):
    """Custom type st4PhaseBranchCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_St4PhaseBranchCount_Type.__name__ = "Integer32"
_St4PhaseBranchCount_Object = MibTableColumn
st4PhaseBranchCount = _St4PhaseBranchCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 2, 1, 20),
    _St4PhaseBranchCount_Type()
)
st4PhaseBranchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseBranchCount.setStatus("current")


class _St4PhaseOutletCount_Type(Integer32):
    """Custom type st4PhaseOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_St4PhaseOutletCount_Type.__name__ = "Integer32"
_St4PhaseOutletCount_Object = MibTableColumn
st4PhaseOutletCount = _St4PhaseOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 2, 1, 21),
    _St4PhaseOutletCount_Type()
)
st4PhaseOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseOutletCount.setStatus("current")
_St4PhaseMonitorTable_Object = MibTable
st4PhaseMonitorTable = _St4PhaseMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3)
)
if mibBuilder.loadTexts:
    st4PhaseMonitorTable.setStatus("current")
_St4PhaseMonitorEntry_Object = MibTableRow
st4PhaseMonitorEntry = _St4PhaseMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1)
)
st4PhaseMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4PhaseIndex"),
)
if mibBuilder.loadTexts:
    st4PhaseMonitorEntry.setStatus("current")
_St4PhaseState_Type = DeviceState
_St4PhaseState_Object = MibTableColumn
st4PhaseState = _St4PhaseState_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 1),
    _St4PhaseState_Type()
)
st4PhaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseState.setStatus("current")
_St4PhaseStatus_Type = DeviceStatus
_St4PhaseStatus_Object = MibTableColumn
st4PhaseStatus = _St4PhaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 2),
    _St4PhaseStatus_Type()
)
st4PhaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseStatus.setStatus("current")


class _St4PhaseVoltage_Type(Integer32):
    """Custom type st4PhaseVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 6000),
    )


_St4PhaseVoltage_Type.__name__ = "Integer32"
_St4PhaseVoltage_Object = MibTableColumn
st4PhaseVoltage = _St4PhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 3),
    _St4PhaseVoltage_Type()
)
st4PhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseVoltage.setUnits("tenth Volts")
_St4PhaseVoltageStatus_Type = DeviceStatus
_St4PhaseVoltageStatus_Object = MibTableColumn
st4PhaseVoltageStatus = _St4PhaseVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 4),
    _St4PhaseVoltageStatus_Type()
)
st4PhaseVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseVoltageStatus.setStatus("current")


class _St4PhaseVoltageDeviation_Type(Integer32):
    """Custom type st4PhaseVoltageDeviation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_St4PhaseVoltageDeviation_Type.__name__ = "Integer32"
_St4PhaseVoltageDeviation_Object = MibTableColumn
st4PhaseVoltageDeviation = _St4PhaseVoltageDeviation_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 5),
    _St4PhaseVoltageDeviation_Type()
)
st4PhaseVoltageDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseVoltageDeviation.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseVoltageDeviation.setUnits("tenth percent")


class _St4PhaseCurrent_Type(Integer32):
    """Custom type st4PhaseCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 30000),
    )


_St4PhaseCurrent_Type.__name__ = "Integer32"
_St4PhaseCurrent_Object = MibTableColumn
st4PhaseCurrent = _St4PhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 6),
    _St4PhaseCurrent_Type()
)
st4PhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseCurrent.setUnits("hundredth Amps")


class _St4PhaseCurrentCrestFactor_Type(Integer32):
    """Custom type st4PhaseCurrentCrestFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 250),
    )


_St4PhaseCurrentCrestFactor_Type.__name__ = "Integer32"
_St4PhaseCurrentCrestFactor_Object = MibTableColumn
st4PhaseCurrentCrestFactor = _St4PhaseCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 7),
    _St4PhaseCurrentCrestFactor_Type()
)
st4PhaseCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseCurrentCrestFactor.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseCurrentCrestFactor.setUnits("tenths")


class _St4PhaseActivePower_Type(Integer32):
    """Custom type st4PhaseActivePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25000),
    )


_St4PhaseActivePower_Type.__name__ = "Integer32"
_St4PhaseActivePower_Object = MibTableColumn
st4PhaseActivePower = _St4PhaseActivePower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 8),
    _St4PhaseActivePower_Type()
)
st4PhaseActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseActivePower.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseActivePower.setUnits("Watts")


class _St4PhaseApparentPower_Type(Integer32):
    """Custom type st4PhaseApparentPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25000),
    )


_St4PhaseApparentPower_Type.__name__ = "Integer32"
_St4PhaseApparentPower_Object = MibTableColumn
st4PhaseApparentPower = _St4PhaseApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 9),
    _St4PhaseApparentPower_Type()
)
st4PhaseApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseApparentPower.setUnits("Volt-Amps")


class _St4PhasePowerFactor_Type(Integer32):
    """Custom type st4PhasePowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_St4PhasePowerFactor_Type.__name__ = "Integer32"
_St4PhasePowerFactor_Object = MibTableColumn
st4PhasePowerFactor = _St4PhasePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 10),
    _St4PhasePowerFactor_Type()
)
st4PhasePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhasePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    st4PhasePowerFactor.setUnits("hundredths")
_St4PhasePowerFactorStatus_Type = DeviceStatus
_St4PhasePowerFactorStatus_Object = MibTableColumn
st4PhasePowerFactorStatus = _St4PhasePowerFactorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 11),
    _St4PhasePowerFactorStatus_Type()
)
st4PhasePowerFactorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhasePowerFactorStatus.setStatus("current")


class _St4PhaseReactance_Type(Integer32):
    """Custom type st4PhaseReactance based on Integer32"""
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
        *(("capacitive", 1),
          ("inductive", 2),
          ("resistive", 3),
          ("unknown", 0))
    )


_St4PhaseReactance_Type.__name__ = "Integer32"
_St4PhaseReactance_Object = MibTableColumn
st4PhaseReactance = _St4PhaseReactance_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 12),
    _St4PhaseReactance_Type()
)
st4PhaseReactance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseReactance.setStatus("current")


class _St4PhaseEnergy_Type(Integer32):
    """Custom type st4PhaseEnergy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_St4PhaseEnergy_Type.__name__ = "Integer32"
_St4PhaseEnergy_Object = MibTableColumn
st4PhaseEnergy = _St4PhaseEnergy_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 3, 1, 13),
    _St4PhaseEnergy_Type()
)
st4PhaseEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4PhaseEnergy.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseEnergy.setUnits("tenth Kilowatt-Hours")
_St4PhaseEventConfigTable_Object = MibTable
st4PhaseEventConfigTable = _St4PhaseEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 4)
)
if mibBuilder.loadTexts:
    st4PhaseEventConfigTable.setStatus("current")
_St4PhaseEventConfigEntry_Object = MibTableRow
st4PhaseEventConfigEntry = _St4PhaseEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 4, 1)
)
st4PhaseEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4PhaseIndex"),
)
if mibBuilder.loadTexts:
    st4PhaseEventConfigEntry.setStatus("current")
_St4PhaseNotifications_Type = EventNotificationMethods
_St4PhaseNotifications_Object = MibTableColumn
st4PhaseNotifications = _St4PhaseNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 4, 1, 1),
    _St4PhaseNotifications_Type()
)
st4PhaseNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4PhaseNotifications.setStatus("current")


class _St4PhaseVoltageLowAlarm_Type(Integer32):
    """Custom type st4PhaseVoltageLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4PhaseVoltageLowAlarm_Type.__name__ = "Integer32"
_St4PhaseVoltageLowAlarm_Object = MibTableColumn
st4PhaseVoltageLowAlarm = _St4PhaseVoltageLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 4, 1, 2),
    _St4PhaseVoltageLowAlarm_Type()
)
st4PhaseVoltageLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4PhaseVoltageLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseVoltageLowAlarm.setUnits("tenth Volts")


class _St4PhaseVoltageLowWarning_Type(Integer32):
    """Custom type st4PhaseVoltageLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4PhaseVoltageLowWarning_Type.__name__ = "Integer32"
_St4PhaseVoltageLowWarning_Object = MibTableColumn
st4PhaseVoltageLowWarning = _St4PhaseVoltageLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 4, 1, 3),
    _St4PhaseVoltageLowWarning_Type()
)
st4PhaseVoltageLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4PhaseVoltageLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseVoltageLowWarning.setUnits("tenth Volts")


class _St4PhaseVoltageHighWarning_Type(Integer32):
    """Custom type st4PhaseVoltageHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4PhaseVoltageHighWarning_Type.__name__ = "Integer32"
_St4PhaseVoltageHighWarning_Object = MibTableColumn
st4PhaseVoltageHighWarning = _St4PhaseVoltageHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 4, 1, 4),
    _St4PhaseVoltageHighWarning_Type()
)
st4PhaseVoltageHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4PhaseVoltageHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseVoltageHighWarning.setUnits("tenth Volts")


class _St4PhaseVoltageHighAlarm_Type(Integer32):
    """Custom type st4PhaseVoltageHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_St4PhaseVoltageHighAlarm_Type.__name__ = "Integer32"
_St4PhaseVoltageHighAlarm_Object = MibTableColumn
st4PhaseVoltageHighAlarm = _St4PhaseVoltageHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 4, 1, 5),
    _St4PhaseVoltageHighAlarm_Type()
)
st4PhaseVoltageHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4PhaseVoltageHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4PhaseVoltageHighAlarm.setUnits("tenth Volts")


class _St4PhasePowerFactorLowAlarm_Type(Integer32):
    """Custom type st4PhasePowerFactorLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4PhasePowerFactorLowAlarm_Type.__name__ = "Integer32"
_St4PhasePowerFactorLowAlarm_Object = MibTableColumn
st4PhasePowerFactorLowAlarm = _St4PhasePowerFactorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 4, 1, 6),
    _St4PhasePowerFactorLowAlarm_Type()
)
st4PhasePowerFactorLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4PhasePowerFactorLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4PhasePowerFactorLowAlarm.setUnits("hundredths")


class _St4PhasePowerFactorLowWarning_Type(Integer32):
    """Custom type st4PhasePowerFactorLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4PhasePowerFactorLowWarning_Type.__name__ = "Integer32"
_St4PhasePowerFactorLowWarning_Object = MibTableColumn
st4PhasePowerFactorLowWarning = _St4PhasePowerFactorLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 5, 4, 1, 7),
    _St4PhasePowerFactorLowWarning_Type()
)
st4PhasePowerFactorLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4PhasePowerFactorLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4PhasePowerFactorLowWarning.setUnits("hundredths")
_St4OverCurrentProtectors_ObjectIdentity = ObjectIdentity
st4OverCurrentProtectors = _St4OverCurrentProtectors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6)
)
_St4OcpCommonConfig_ObjectIdentity = ObjectIdentity
st4OcpCommonConfig = _St4OcpCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 1)
)
_St4OcpConfigTable_Object = MibTable
st4OcpConfigTable = _St4OcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2)
)
if mibBuilder.loadTexts:
    st4OcpConfigTable.setStatus("current")
_St4OcpConfigEntry_Object = MibTableRow
st4OcpConfigEntry = _St4OcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2, 1)
)
st4OcpConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4OcpIndex"),
)
if mibBuilder.loadTexts:
    st4OcpConfigEntry.setStatus("current")


class _St4OcpIndex_Type(Integer32):
    """Custom type st4OcpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_St4OcpIndex_Type.__name__ = "Integer32"
_St4OcpIndex_Object = MibTableColumn
st4OcpIndex = _St4OcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2, 1, 1),
    _St4OcpIndex_Type()
)
st4OcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4OcpIndex.setStatus("current")


class _St4OcpID_Type(DisplayString):
    """Custom type st4OcpID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_St4OcpID_Type.__name__ = "DisplayString"
_St4OcpID_Object = MibTableColumn
st4OcpID = _St4OcpID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2, 1, 2),
    _St4OcpID_Type()
)
st4OcpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OcpID.setStatus("current")


class _St4OcpLabel_Type(DisplayString):
    """Custom type st4OcpLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4OcpLabel_Type.__name__ = "DisplayString"
_St4OcpLabel_Object = MibTableColumn
st4OcpLabel = _St4OcpLabel_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2, 1, 4),
    _St4OcpLabel_Type()
)
st4OcpLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OcpLabel.setStatus("current")


class _St4OcpType_Type(Integer32):
    """Custom type st4OcpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("breaker", 1),
          ("fuse", 0))
    )


_St4OcpType_Type.__name__ = "Integer32"
_St4OcpType_Object = MibTableColumn
st4OcpType = _St4OcpType_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2, 1, 6),
    _St4OcpType_Type()
)
st4OcpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OcpType.setStatus("current")


class _St4OcpCurrentCapacity_Type(Integer32):
    """Custom type st4OcpCurrentCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 125),
    )


_St4OcpCurrentCapacity_Type.__name__ = "Integer32"
_St4OcpCurrentCapacity_Object = MibTableColumn
st4OcpCurrentCapacity = _St4OcpCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2, 1, 7),
    _St4OcpCurrentCapacity_Type()
)
st4OcpCurrentCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OcpCurrentCapacity.setStatus("current")
if mibBuilder.loadTexts:
    st4OcpCurrentCapacity.setUnits("Amps")


class _St4OcpCurrentCapacityMax_Type(Integer32):
    """Custom type st4OcpCurrentCapacityMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 125),
    )


_St4OcpCurrentCapacityMax_Type.__name__ = "Integer32"
_St4OcpCurrentCapacityMax_Object = MibTableColumn
st4OcpCurrentCapacityMax = _St4OcpCurrentCapacityMax_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2, 1, 8),
    _St4OcpCurrentCapacityMax_Type()
)
st4OcpCurrentCapacityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OcpCurrentCapacityMax.setStatus("current")
if mibBuilder.loadTexts:
    st4OcpCurrentCapacityMax.setUnits("Amps")


class _St4OcpBranchCount_Type(Integer32):
    """Custom type st4OcpBranchCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_St4OcpBranchCount_Type.__name__ = "Integer32"
_St4OcpBranchCount_Object = MibTableColumn
st4OcpBranchCount = _St4OcpBranchCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2, 1, 20),
    _St4OcpBranchCount_Type()
)
st4OcpBranchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OcpBranchCount.setStatus("current")


class _St4OcpOutletCount_Type(Integer32):
    """Custom type st4OcpOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_St4OcpOutletCount_Type.__name__ = "Integer32"
_St4OcpOutletCount_Object = MibTableColumn
st4OcpOutletCount = _St4OcpOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 2, 1, 21),
    _St4OcpOutletCount_Type()
)
st4OcpOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OcpOutletCount.setStatus("current")
_St4OcpMonitorTable_Object = MibTable
st4OcpMonitorTable = _St4OcpMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 3)
)
if mibBuilder.loadTexts:
    st4OcpMonitorTable.setStatus("current")
_St4OcpMonitorEntry_Object = MibTableRow
st4OcpMonitorEntry = _St4OcpMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 3, 1)
)
st4OcpMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4OcpIndex"),
)
if mibBuilder.loadTexts:
    st4OcpMonitorEntry.setStatus("current")
_St4OcpStatus_Type = DeviceStatus
_St4OcpStatus_Object = MibTableColumn
st4OcpStatus = _St4OcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 3, 1, 1),
    _St4OcpStatus_Type()
)
st4OcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OcpStatus.setStatus("current")
_St4OcpEventConfigTable_Object = MibTable
st4OcpEventConfigTable = _St4OcpEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 4)
)
if mibBuilder.loadTexts:
    st4OcpEventConfigTable.setStatus("current")
_St4OcpEventConfigEntry_Object = MibTableRow
st4OcpEventConfigEntry = _St4OcpEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 4, 1)
)
st4OcpEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4OcpIndex"),
)
if mibBuilder.loadTexts:
    st4OcpEventConfigEntry.setStatus("current")
_St4OcpNotifications_Type = EventNotificationMethods
_St4OcpNotifications_Object = MibTableColumn
st4OcpNotifications = _St4OcpNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 6, 4, 1, 1),
    _St4OcpNotifications_Type()
)
st4OcpNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OcpNotifications.setStatus("current")
_St4Branches_ObjectIdentity = ObjectIdentity
st4Branches = _St4Branches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7)
)
_St4BranchCommonConfig_ObjectIdentity = ObjectIdentity
st4BranchCommonConfig = _St4BranchCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 1)
)


class _St4BranchCurrentHysteresis_Type(Integer32):
    """Custom type st4BranchCurrentHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4BranchCurrentHysteresis_Type.__name__ = "Integer32"
_St4BranchCurrentHysteresis_Object = MibScalar
st4BranchCurrentHysteresis = _St4BranchCurrentHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 1, 1),
    _St4BranchCurrentHysteresis_Type()
)
st4BranchCurrentHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4BranchCurrentHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4BranchCurrentHysteresis.setUnits("tenth Amps")
_St4BranchConfigTable_Object = MibTable
st4BranchConfigTable = _St4BranchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 2)
)
if mibBuilder.loadTexts:
    st4BranchConfigTable.setStatus("current")
_St4BranchConfigEntry_Object = MibTableRow
st4BranchConfigEntry = _St4BranchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 2, 1)
)
st4BranchConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4BranchIndex"),
)
if mibBuilder.loadTexts:
    st4BranchConfigEntry.setStatus("current")


class _St4BranchIndex_Type(Integer32):
    """Custom type st4BranchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_St4BranchIndex_Type.__name__ = "Integer32"
_St4BranchIndex_Object = MibTableColumn
st4BranchIndex = _St4BranchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 2, 1, 1),
    _St4BranchIndex_Type()
)
st4BranchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4BranchIndex.setStatus("current")


class _St4BranchID_Type(DisplayString):
    """Custom type st4BranchID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_St4BranchID_Type.__name__ = "DisplayString"
_St4BranchID_Object = MibTableColumn
st4BranchID = _St4BranchID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 2, 1, 2),
    _St4BranchID_Type()
)
st4BranchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchID.setStatus("current")


class _St4BranchLabel_Type(DisplayString):
    """Custom type st4BranchLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4BranchLabel_Type.__name__ = "DisplayString"
_St4BranchLabel_Object = MibTableColumn
st4BranchLabel = _St4BranchLabel_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 2, 1, 4),
    _St4BranchLabel_Type()
)
st4BranchLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchLabel.setStatus("current")


class _St4BranchCurrentCapacity_Type(Integer32):
    """Custom type st4BranchCurrentCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 125),
    )


_St4BranchCurrentCapacity_Type.__name__ = "Integer32"
_St4BranchCurrentCapacity_Object = MibTableColumn
st4BranchCurrentCapacity = _St4BranchCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 2, 1, 6),
    _St4BranchCurrentCapacity_Type()
)
st4BranchCurrentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchCurrentCapacity.setStatus("current")
if mibBuilder.loadTexts:
    st4BranchCurrentCapacity.setUnits("Amps")


class _St4BranchPhaseID_Type(DisplayString):
    """Custom type st4BranchPhaseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_St4BranchPhaseID_Type.__name__ = "DisplayString"
_St4BranchPhaseID_Object = MibTableColumn
st4BranchPhaseID = _St4BranchPhaseID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 2, 1, 20),
    _St4BranchPhaseID_Type()
)
st4BranchPhaseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchPhaseID.setStatus("current")


class _St4BranchOcpID_Type(DisplayString):
    """Custom type st4BranchOcpID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_St4BranchOcpID_Type.__name__ = "DisplayString"
_St4BranchOcpID_Object = MibTableColumn
st4BranchOcpID = _St4BranchOcpID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 2, 1, 21),
    _St4BranchOcpID_Type()
)
st4BranchOcpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchOcpID.setStatus("current")


class _St4BranchOutletCount_Type(Integer32):
    """Custom type st4BranchOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_St4BranchOutletCount_Type.__name__ = "Integer32"
_St4BranchOutletCount_Object = MibTableColumn
st4BranchOutletCount = _St4BranchOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 2, 1, 30),
    _St4BranchOutletCount_Type()
)
st4BranchOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchOutletCount.setStatus("current")
_St4BranchMonitorTable_Object = MibTable
st4BranchMonitorTable = _St4BranchMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 3)
)
if mibBuilder.loadTexts:
    st4BranchMonitorTable.setStatus("current")
_St4BranchMonitorEntry_Object = MibTableRow
st4BranchMonitorEntry = _St4BranchMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 3, 1)
)
st4BranchMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4BranchIndex"),
)
if mibBuilder.loadTexts:
    st4BranchMonitorEntry.setStatus("current")
_St4BranchState_Type = DeviceState
_St4BranchState_Object = MibTableColumn
st4BranchState = _St4BranchState_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 3, 1, 1),
    _St4BranchState_Type()
)
st4BranchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchState.setStatus("current")
_St4BranchStatus_Type = DeviceStatus
_St4BranchStatus_Object = MibTableColumn
st4BranchStatus = _St4BranchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 3, 1, 2),
    _St4BranchStatus_Type()
)
st4BranchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchStatus.setStatus("current")


class _St4BranchCurrent_Type(Integer32):
    """Custom type st4BranchCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 12500),
    )


_St4BranchCurrent_Type.__name__ = "Integer32"
_St4BranchCurrent_Object = MibTableColumn
st4BranchCurrent = _St4BranchCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 3, 1, 3),
    _St4BranchCurrent_Type()
)
st4BranchCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchCurrent.setStatus("current")
if mibBuilder.loadTexts:
    st4BranchCurrent.setUnits("hundredth Amps")
_St4BranchCurrentStatus_Type = DeviceStatus
_St4BranchCurrentStatus_Object = MibTableColumn
st4BranchCurrentStatus = _St4BranchCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 3, 1, 4),
    _St4BranchCurrentStatus_Type()
)
st4BranchCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchCurrentStatus.setStatus("current")


class _St4BranchCurrentUtilized_Type(Integer32):
    """Custom type st4BranchCurrentUtilized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1200),
    )


_St4BranchCurrentUtilized_Type.__name__ = "Integer32"
_St4BranchCurrentUtilized_Object = MibTableColumn
st4BranchCurrentUtilized = _St4BranchCurrentUtilized_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 3, 1, 5),
    _St4BranchCurrentUtilized_Type()
)
st4BranchCurrentUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4BranchCurrentUtilized.setStatus("current")
if mibBuilder.loadTexts:
    st4BranchCurrentUtilized.setUnits("tenth percent")
_St4BranchEventConfigTable_Object = MibTable
st4BranchEventConfigTable = _St4BranchEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 4)
)
if mibBuilder.loadTexts:
    st4BranchEventConfigTable.setStatus("current")
_St4BranchEventConfigEntry_Object = MibTableRow
st4BranchEventConfigEntry = _St4BranchEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 4, 1)
)
st4BranchEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4BranchIndex"),
)
if mibBuilder.loadTexts:
    st4BranchEventConfigEntry.setStatus("current")
_St4BranchNotifications_Type = EventNotificationMethods
_St4BranchNotifications_Object = MibTableColumn
st4BranchNotifications = _St4BranchNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 4, 1, 1),
    _St4BranchNotifications_Type()
)
st4BranchNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4BranchNotifications.setStatus("current")


class _St4BranchCurrentLowAlarm_Type(Integer32):
    """Custom type st4BranchCurrentLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1250),
    )


_St4BranchCurrentLowAlarm_Type.__name__ = "Integer32"
_St4BranchCurrentLowAlarm_Object = MibTableColumn
st4BranchCurrentLowAlarm = _St4BranchCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 4, 1, 2),
    _St4BranchCurrentLowAlarm_Type()
)
st4BranchCurrentLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4BranchCurrentLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4BranchCurrentLowAlarm.setUnits("tenth Amps")


class _St4BranchCurrentLowWarning_Type(Integer32):
    """Custom type st4BranchCurrentLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1250),
    )


_St4BranchCurrentLowWarning_Type.__name__ = "Integer32"
_St4BranchCurrentLowWarning_Object = MibTableColumn
st4BranchCurrentLowWarning = _St4BranchCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 4, 1, 3),
    _St4BranchCurrentLowWarning_Type()
)
st4BranchCurrentLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4BranchCurrentLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4BranchCurrentLowWarning.setUnits("tenth Amps")


class _St4BranchCurrentHighWarning_Type(Integer32):
    """Custom type st4BranchCurrentHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1250),
    )


_St4BranchCurrentHighWarning_Type.__name__ = "Integer32"
_St4BranchCurrentHighWarning_Object = MibTableColumn
st4BranchCurrentHighWarning = _St4BranchCurrentHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 4, 1, 4),
    _St4BranchCurrentHighWarning_Type()
)
st4BranchCurrentHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4BranchCurrentHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4BranchCurrentHighWarning.setUnits("tenth Amps")


class _St4BranchCurrentHighAlarm_Type(Integer32):
    """Custom type st4BranchCurrentHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1250),
    )


_St4BranchCurrentHighAlarm_Type.__name__ = "Integer32"
_St4BranchCurrentHighAlarm_Object = MibTableColumn
st4BranchCurrentHighAlarm = _St4BranchCurrentHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 7, 4, 1, 5),
    _St4BranchCurrentHighAlarm_Type()
)
st4BranchCurrentHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4BranchCurrentHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4BranchCurrentHighAlarm.setUnits("tenth Amps")
_St4Outlets_ObjectIdentity = ObjectIdentity
st4Outlets = _St4Outlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8)
)
_St4OutletCommonConfig_ObjectIdentity = ObjectIdentity
st4OutletCommonConfig = _St4OutletCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 1)
)


class _St4OutletCurrentHysteresis_Type(Integer32):
    """Custom type st4OutletCurrentHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4OutletCurrentHysteresis_Type.__name__ = "Integer32"
_St4OutletCurrentHysteresis_Object = MibScalar
st4OutletCurrentHysteresis = _St4OutletCurrentHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 1, 1),
    _St4OutletCurrentHysteresis_Type()
)
st4OutletCurrentHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletCurrentHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletCurrentHysteresis.setUnits("tenth Amps")


class _St4OutletActivePowerHysteresis_Type(Integer32):
    """Custom type st4OutletActivePowerHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_St4OutletActivePowerHysteresis_Type.__name__ = "Integer32"
_St4OutletActivePowerHysteresis_Object = MibScalar
st4OutletActivePowerHysteresis = _St4OutletActivePowerHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 1, 2),
    _St4OutletActivePowerHysteresis_Type()
)
st4OutletActivePowerHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletActivePowerHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletActivePowerHysteresis.setUnits("Watts")


class _St4OutletPowerFactorHysteresis_Type(Integer32):
    """Custom type st4OutletPowerFactorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_St4OutletPowerFactorHysteresis_Type.__name__ = "Integer32"
_St4OutletPowerFactorHysteresis_Object = MibScalar
st4OutletPowerFactorHysteresis = _St4OutletPowerFactorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 1, 3),
    _St4OutletPowerFactorHysteresis_Type()
)
st4OutletPowerFactorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletPowerFactorHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletPowerFactorHysteresis.setUnits("hundredths")


class _St4OutletSequenceInterval_Type(Integer32):
    """Custom type st4OutletSequenceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_St4OutletSequenceInterval_Type.__name__ = "Integer32"
_St4OutletSequenceInterval_Object = MibScalar
st4OutletSequenceInterval = _St4OutletSequenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 1, 10),
    _St4OutletSequenceInterval_Type()
)
st4OutletSequenceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletSequenceInterval.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletSequenceInterval.setUnits("seconds")


class _St4OutletRebootDelay_Type(Integer32):
    """Custom type st4OutletRebootDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_St4OutletRebootDelay_Type.__name__ = "Integer32"
_St4OutletRebootDelay_Object = MibScalar
st4OutletRebootDelay = _St4OutletRebootDelay_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 1, 11),
    _St4OutletRebootDelay_Type()
)
st4OutletRebootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletRebootDelay.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletRebootDelay.setUnits("seconds")


class _St4OutletStateChangeLogging_Type(Integer32):
    """Custom type st4OutletStateChangeLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_St4OutletStateChangeLogging_Type.__name__ = "Integer32"
_St4OutletStateChangeLogging_Object = MibScalar
st4OutletStateChangeLogging = _St4OutletStateChangeLogging_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 1, 12),
    _St4OutletStateChangeLogging_Type()
)
st4OutletStateChangeLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletStateChangeLogging.setStatus("current")
_St4OutletConfigTable_Object = MibTable
st4OutletConfigTable = _St4OutletConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2)
)
if mibBuilder.loadTexts:
    st4OutletConfigTable.setStatus("current")
_St4OutletConfigEntry_Object = MibTableRow
st4OutletConfigEntry = _St4OutletConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1)
)
st4OutletConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4OutletIndex"),
)
if mibBuilder.loadTexts:
    st4OutletConfigEntry.setStatus("current")


class _St4OutletIndex_Type(Integer32):
    """Custom type st4OutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_St4OutletIndex_Type.__name__ = "Integer32"
_St4OutletIndex_Object = MibTableColumn
st4OutletIndex = _St4OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 1),
    _St4OutletIndex_Type()
)
st4OutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4OutletIndex.setStatus("current")


class _St4OutletID_Type(DisplayString):
    """Custom type st4OutletID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 5),
    )


_St4OutletID_Type.__name__ = "DisplayString"
_St4OutletID_Object = MibTableColumn
st4OutletID = _St4OutletID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 2),
    _St4OutletID_Type()
)
st4OutletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletID.setStatus("current")


class _St4OutletName_Type(DisplayString):
    """Custom type st4OutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4OutletName_Type.__name__ = "DisplayString"
_St4OutletName_Object = MibTableColumn
st4OutletName = _St4OutletName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 3),
    _St4OutletName_Type()
)
st4OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletName.setStatus("current")


class _St4OutletCapabilities_Type(Bits):
    """Custom type st4OutletCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("pops", 1),
          ("switched", 0))
    )

_St4OutletCapabilities_Type.__name__ = "Bits"
_St4OutletCapabilities_Object = MibTableColumn
st4OutletCapabilities = _St4OutletCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 5),
    _St4OutletCapabilities_Type()
)
st4OutletCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletCapabilities.setStatus("current")


class _St4OutletSocketType_Type(DisplayString):
    """Custom type st4OutletSocketType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4OutletSocketType_Type.__name__ = "DisplayString"
_St4OutletSocketType_Object = MibTableColumn
st4OutletSocketType = _St4OutletSocketType_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 6),
    _St4OutletSocketType_Type()
)
st4OutletSocketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletSocketType.setStatus("current")


class _St4OutletCurrentCapacity_Type(Integer32):
    """Custom type st4OutletCurrentCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 125),
    )


_St4OutletCurrentCapacity_Type.__name__ = "Integer32"
_St4OutletCurrentCapacity_Object = MibTableColumn
st4OutletCurrentCapacity = _St4OutletCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 7),
    _St4OutletCurrentCapacity_Type()
)
st4OutletCurrentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletCurrentCapacity.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletCurrentCapacity.setUnits("Amps")


class _St4OutletPowerCapacity_Type(Integer32):
    """Custom type st4OutletPowerCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_St4OutletPowerCapacity_Type.__name__ = "Integer32"
_St4OutletPowerCapacity_Object = MibTableColumn
st4OutletPowerCapacity = _St4OutletPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 8),
    _St4OutletPowerCapacity_Type()
)
st4OutletPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletPowerCapacity.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletPowerCapacity.setUnits("Volt-Amps")


class _St4OutletWakeupState_Type(Integer32):
    """Custom type st4OutletWakeupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("last", 2),
          ("off", 1),
          ("on", 0))
    )


_St4OutletWakeupState_Type.__name__ = "Integer32"
_St4OutletWakeupState_Object = MibTableColumn
st4OutletWakeupState = _St4OutletWakeupState_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 20),
    _St4OutletWakeupState_Type()
)
st4OutletWakeupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletWakeupState.setStatus("current")


class _St4OutletPostOnDelay_Type(Integer32):
    """Custom type st4OutletPostOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_St4OutletPostOnDelay_Type.__name__ = "Integer32"
_St4OutletPostOnDelay_Object = MibTableColumn
st4OutletPostOnDelay = _St4OutletPostOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 21),
    _St4OutletPostOnDelay_Type()
)
st4OutletPostOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletPostOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletPostOnDelay.setUnits("seconds")


class _St4OutletPhaseID_Type(DisplayString):
    """Custom type st4OutletPhaseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_St4OutletPhaseID_Type.__name__ = "DisplayString"
_St4OutletPhaseID_Object = MibTableColumn
st4OutletPhaseID = _St4OutletPhaseID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 30),
    _St4OutletPhaseID_Type()
)
st4OutletPhaseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletPhaseID.setStatus("current")


class _St4OutletOcpID_Type(DisplayString):
    """Custom type st4OutletOcpID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_St4OutletOcpID_Type.__name__ = "DisplayString"
_St4OutletOcpID_Object = MibTableColumn
st4OutletOcpID = _St4OutletOcpID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 31),
    _St4OutletOcpID_Type()
)
st4OutletOcpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletOcpID.setStatus("current")


class _St4OutletBranchID_Type(DisplayString):
    """Custom type st4OutletBranchID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_St4OutletBranchID_Type.__name__ = "DisplayString"
_St4OutletBranchID_Object = MibTableColumn
st4OutletBranchID = _St4OutletBranchID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 2, 1, 32),
    _St4OutletBranchID_Type()
)
st4OutletBranchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletBranchID.setStatus("current")
_St4OutletMonitorTable_Object = MibTable
st4OutletMonitorTable = _St4OutletMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3)
)
if mibBuilder.loadTexts:
    st4OutletMonitorTable.setStatus("current")
_St4OutletMonitorEntry_Object = MibTableRow
st4OutletMonitorEntry = _St4OutletMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1)
)
st4OutletMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4OutletIndex"),
)
if mibBuilder.loadTexts:
    st4OutletMonitorEntry.setStatus("current")
_St4OutletState_Type = DeviceState
_St4OutletState_Object = MibTableColumn
st4OutletState = _St4OutletState_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 1),
    _St4OutletState_Type()
)
st4OutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletState.setStatus("current")
_St4OutletStatus_Type = DeviceStatus
_St4OutletStatus_Object = MibTableColumn
st4OutletStatus = _St4OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 2),
    _St4OutletStatus_Type()
)
st4OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletStatus.setStatus("current")


class _St4OutletCurrent_Type(Integer32):
    """Custom type st4OutletCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 12500),
    )


_St4OutletCurrent_Type.__name__ = "Integer32"
_St4OutletCurrent_Object = MibTableColumn
st4OutletCurrent = _St4OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 3),
    _St4OutletCurrent_Type()
)
st4OutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletCurrent.setUnits("hundredth Amps")
_St4OutletCurrentStatus_Type = DeviceStatus
_St4OutletCurrentStatus_Object = MibTableColumn
st4OutletCurrentStatus = _St4OutletCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 4),
    _St4OutletCurrentStatus_Type()
)
st4OutletCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletCurrentStatus.setStatus("current")


class _St4OutletCurrentUtilized_Type(Integer32):
    """Custom type st4OutletCurrentUtilized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1200),
    )


_St4OutletCurrentUtilized_Type.__name__ = "Integer32"
_St4OutletCurrentUtilized_Object = MibTableColumn
st4OutletCurrentUtilized = _St4OutletCurrentUtilized_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 5),
    _St4OutletCurrentUtilized_Type()
)
st4OutletCurrentUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletCurrentUtilized.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletCurrentUtilized.setUnits("tenth percent")


class _St4OutletVoltage_Type(Integer32):
    """Custom type st4OutletVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 6000),
    )


_St4OutletVoltage_Type.__name__ = "Integer32"
_St4OutletVoltage_Object = MibTableColumn
st4OutletVoltage = _St4OutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 6),
    _St4OutletVoltage_Type()
)
st4OutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletVoltage.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletVoltage.setUnits("tenth Volts")


class _St4OutletActivePower_Type(Integer32):
    """Custom type st4OutletActivePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_St4OutletActivePower_Type.__name__ = "Integer32"
_St4OutletActivePower_Object = MibTableColumn
st4OutletActivePower = _St4OutletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 7),
    _St4OutletActivePower_Type()
)
st4OutletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletActivePower.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletActivePower.setUnits("Watts")
_St4OutletActivePowerStatus_Type = DeviceStatus
_St4OutletActivePowerStatus_Object = MibTableColumn
st4OutletActivePowerStatus = _St4OutletActivePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 8),
    _St4OutletActivePowerStatus_Type()
)
st4OutletActivePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletActivePowerStatus.setStatus("current")


class _St4OutletApparentPower_Type(Integer32):
    """Custom type st4OutletApparentPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_St4OutletApparentPower_Type.__name__ = "Integer32"
_St4OutletApparentPower_Object = MibTableColumn
st4OutletApparentPower = _St4OutletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 9),
    _St4OutletApparentPower_Type()
)
st4OutletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletApparentPower.setUnits("Volt-Amps")


class _St4OutletPowerFactor_Type(Integer32):
    """Custom type st4OutletPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_St4OutletPowerFactor_Type.__name__ = "Integer32"
_St4OutletPowerFactor_Object = MibTableColumn
st4OutletPowerFactor = _St4OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 10),
    _St4OutletPowerFactor_Type()
)
st4OutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletPowerFactor.setUnits("hundredths")
_St4OutletPowerFactorStatus_Type = DeviceStatus
_St4OutletPowerFactorStatus_Object = MibTableColumn
st4OutletPowerFactorStatus = _St4OutletPowerFactorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 11),
    _St4OutletPowerFactorStatus_Type()
)
st4OutletPowerFactorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletPowerFactorStatus.setStatus("current")


class _St4OutletCurrentCrestFactor_Type(Integer32):
    """Custom type st4OutletCurrentCrestFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 250),
    )


_St4OutletCurrentCrestFactor_Type.__name__ = "Integer32"
_St4OutletCurrentCrestFactor_Object = MibTableColumn
st4OutletCurrentCrestFactor = _St4OutletCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 12),
    _St4OutletCurrentCrestFactor_Type()
)
st4OutletCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletCurrentCrestFactor.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletCurrentCrestFactor.setUnits("tenths")


class _St4OutletReactance_Type(Integer32):
    """Custom type st4OutletReactance based on Integer32"""
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
        *(("capacitive", 1),
          ("inductive", 2),
          ("resistive", 3),
          ("unknown", 0))
    )


_St4OutletReactance_Type.__name__ = "Integer32"
_St4OutletReactance_Object = MibTableColumn
st4OutletReactance = _St4OutletReactance_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 13),
    _St4OutletReactance_Type()
)
st4OutletReactance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletReactance.setStatus("current")


class _St4OutletEnergy_Type(Integer32):
    """Custom type st4OutletEnergy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_St4OutletEnergy_Type.__name__ = "Integer32"
_St4OutletEnergy_Object = MibTableColumn
st4OutletEnergy = _St4OutletEnergy_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 3, 1, 14),
    _St4OutletEnergy_Type()
)
st4OutletEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletEnergy.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletEnergy.setUnits("Watt-Hours")
_St4OutletEventConfigTable_Object = MibTable
st4OutletEventConfigTable = _St4OutletEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4)
)
if mibBuilder.loadTexts:
    st4OutletEventConfigTable.setStatus("current")
_St4OutletEventConfigEntry_Object = MibTableRow
st4OutletEventConfigEntry = _St4OutletEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1)
)
st4OutletEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4OutletIndex"),
)
if mibBuilder.loadTexts:
    st4OutletEventConfigEntry.setStatus("current")
_St4OutletNotifications_Type = EventNotificationMethods
_St4OutletNotifications_Object = MibTableColumn
st4OutletNotifications = _St4OutletNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 1),
    _St4OutletNotifications_Type()
)
st4OutletNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletNotifications.setStatus("current")


class _St4OutletCurrentLowAlarm_Type(Integer32):
    """Custom type st4OutletCurrentLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1250),
    )


_St4OutletCurrentLowAlarm_Type.__name__ = "Integer32"
_St4OutletCurrentLowAlarm_Object = MibTableColumn
st4OutletCurrentLowAlarm = _St4OutletCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 2),
    _St4OutletCurrentLowAlarm_Type()
)
st4OutletCurrentLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletCurrentLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletCurrentLowAlarm.setUnits("tenth Amps")


class _St4OutletCurrentLowWarning_Type(Integer32):
    """Custom type st4OutletCurrentLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1250),
    )


_St4OutletCurrentLowWarning_Type.__name__ = "Integer32"
_St4OutletCurrentLowWarning_Object = MibTableColumn
st4OutletCurrentLowWarning = _St4OutletCurrentLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 3),
    _St4OutletCurrentLowWarning_Type()
)
st4OutletCurrentLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletCurrentLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletCurrentLowWarning.setUnits("tenth Amps")


class _St4OutletCurrentHighWarning_Type(Integer32):
    """Custom type st4OutletCurrentHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1250),
    )


_St4OutletCurrentHighWarning_Type.__name__ = "Integer32"
_St4OutletCurrentHighWarning_Object = MibTableColumn
st4OutletCurrentHighWarning = _St4OutletCurrentHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 4),
    _St4OutletCurrentHighWarning_Type()
)
st4OutletCurrentHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletCurrentHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletCurrentHighWarning.setUnits("tenth Amps")


class _St4OutletCurrentHighAlarm_Type(Integer32):
    """Custom type st4OutletCurrentHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1250),
    )


_St4OutletCurrentHighAlarm_Type.__name__ = "Integer32"
_St4OutletCurrentHighAlarm_Object = MibTableColumn
st4OutletCurrentHighAlarm = _St4OutletCurrentHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 5),
    _St4OutletCurrentHighAlarm_Type()
)
st4OutletCurrentHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletCurrentHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletCurrentHighAlarm.setUnits("tenth Amps")


class _St4OutletActivePowerLowAlarm_Type(Integer32):
    """Custom type st4OutletActivePowerLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_St4OutletActivePowerLowAlarm_Type.__name__ = "Integer32"
_St4OutletActivePowerLowAlarm_Object = MibTableColumn
st4OutletActivePowerLowAlarm = _St4OutletActivePowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 6),
    _St4OutletActivePowerLowAlarm_Type()
)
st4OutletActivePowerLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletActivePowerLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletActivePowerLowAlarm.setUnits("Watts")


class _St4OutletActivePowerLowWarning_Type(Integer32):
    """Custom type st4OutletActivePowerLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_St4OutletActivePowerLowWarning_Type.__name__ = "Integer32"
_St4OutletActivePowerLowWarning_Object = MibTableColumn
st4OutletActivePowerLowWarning = _St4OutletActivePowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 7),
    _St4OutletActivePowerLowWarning_Type()
)
st4OutletActivePowerLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletActivePowerLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletActivePowerLowWarning.setUnits("Watts")


class _St4OutletActivePowerHighWarning_Type(Integer32):
    """Custom type st4OutletActivePowerHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_St4OutletActivePowerHighWarning_Type.__name__ = "Integer32"
_St4OutletActivePowerHighWarning_Object = MibTableColumn
st4OutletActivePowerHighWarning = _St4OutletActivePowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 8),
    _St4OutletActivePowerHighWarning_Type()
)
st4OutletActivePowerHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletActivePowerHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletActivePowerHighWarning.setUnits("Watts")


class _St4OutletActivePowerHighAlarm_Type(Integer32):
    """Custom type st4OutletActivePowerHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_St4OutletActivePowerHighAlarm_Type.__name__ = "Integer32"
_St4OutletActivePowerHighAlarm_Object = MibTableColumn
st4OutletActivePowerHighAlarm = _St4OutletActivePowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 9),
    _St4OutletActivePowerHighAlarm_Type()
)
st4OutletActivePowerHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletActivePowerHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletActivePowerHighAlarm.setUnits("Watts")


class _St4OutletPowerFactorLowAlarm_Type(Integer32):
    """Custom type st4OutletPowerFactorLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4OutletPowerFactorLowAlarm_Type.__name__ = "Integer32"
_St4OutletPowerFactorLowAlarm_Object = MibTableColumn
st4OutletPowerFactorLowAlarm = _St4OutletPowerFactorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 10),
    _St4OutletPowerFactorLowAlarm_Type()
)
st4OutletPowerFactorLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletPowerFactorLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletPowerFactorLowAlarm.setUnits("hundredths")


class _St4OutletPowerFactorLowWarning_Type(Integer32):
    """Custom type st4OutletPowerFactorLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4OutletPowerFactorLowWarning_Type.__name__ = "Integer32"
_St4OutletPowerFactorLowWarning_Object = MibTableColumn
st4OutletPowerFactorLowWarning = _St4OutletPowerFactorLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 4, 1, 11),
    _St4OutletPowerFactorLowWarning_Type()
)
st4OutletPowerFactorLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletPowerFactorLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4OutletPowerFactorLowWarning.setUnits("hundredths")
_St4OutletControlTable_Object = MibTable
st4OutletControlTable = _St4OutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 5)
)
if mibBuilder.loadTexts:
    st4OutletControlTable.setStatus("current")
_St4OutletControlEntry_Object = MibTableRow
st4OutletControlEntry = _St4OutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 5, 1)
)
st4OutletControlEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4InputCordIndex"),
    (0, "Sentry4-MIB", "st4OutletIndex"),
)
if mibBuilder.loadTexts:
    st4OutletControlEntry.setStatus("current")


class _St4OutletControlState_Type(Integer32):
    """Custom type st4OutletControlState based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("eventOff", 16),
          ("eventOn", 17),
          ("eventReboot", 18),
          ("eventShutdown", 19),
          ("fixedOn", 1),
          ("idleOff", 2),
          ("idleOn", 3),
          ("lockedOff", 14),
          ("lockedOn", 15),
          ("notSet", 0),
          ("ocpOff", 6),
          ("ocpOn", 7),
          ("off", 10),
          ("on", 11),
          ("pendOff", 9),
          ("pendOn", 8),
          ("reboot", 12),
          ("shutdown", 13),
          ("wakeOff", 4),
          ("wakeOn", 5))
    )


_St4OutletControlState_Type.__name__ = "Integer32"
_St4OutletControlState_Object = MibTableColumn
st4OutletControlState = _St4OutletControlState_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 5, 1, 1),
    _St4OutletControlState_Type()
)
st4OutletControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4OutletControlState.setStatus("current")


class _St4OutletControlAction_Type(Integer32):
    """Custom type st4OutletControlAction based on Integer32"""
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
        *(("none", 0),
          ("off", 2),
          ("on", 1),
          ("queueOff", 5),
          ("queueOn", 4),
          ("queueReboot", 6),
          ("reboot", 3))
    )


_St4OutletControlAction_Type.__name__ = "Integer32"
_St4OutletControlAction_Object = MibTableColumn
st4OutletControlAction = _St4OutletControlAction_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 5, 1, 2),
    _St4OutletControlAction_Type()
)
st4OutletControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletControlAction.setStatus("current")
_St4OutletCommonControl_ObjectIdentity = ObjectIdentity
st4OutletCommonControl = _St4OutletCommonControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 6)
)


class _St4OutletQueueControl_Type(Integer32):
    """Custom type st4OutletQueueControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("commit", 1))
    )


_St4OutletQueueControl_Type.__name__ = "Integer32"
_St4OutletQueueControl_Object = MibScalar
st4OutletQueueControl = _St4OutletQueueControl_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 8, 6, 1),
    _St4OutletQueueControl_Type()
)
st4OutletQueueControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4OutletQueueControl.setStatus("current")
_St4TemperatureSensors_ObjectIdentity = ObjectIdentity
st4TemperatureSensors = _St4TemperatureSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9)
)
_St4TempSensorCommonConfig_ObjectIdentity = ObjectIdentity
st4TempSensorCommonConfig = _St4TempSensorCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 1)
)


class _St4TempSensorHysteresis_Type(Integer32):
    """Custom type st4TempSensorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_St4TempSensorHysteresis_Type.__name__ = "Integer32"
_St4TempSensorHysteresis_Object = MibScalar
st4TempSensorHysteresis = _St4TempSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 1, 1),
    _St4TempSensorHysteresis_Type()
)
st4TempSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4TempSensorHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4TempSensorHysteresis.setUnits("degrees")


class _St4TempSensorScale_Type(Integer32):
    """Custom type st4TempSensorScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 0),
          ("fahrenheit", 1))
    )


_St4TempSensorScale_Type.__name__ = "Integer32"
_St4TempSensorScale_Object = MibScalar
st4TempSensorScale = _St4TempSensorScale_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 1, 10),
    _St4TempSensorScale_Type()
)
st4TempSensorScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4TempSensorScale.setStatus("current")
_St4TempSensorConfigTable_Object = MibTable
st4TempSensorConfigTable = _St4TempSensorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 2)
)
if mibBuilder.loadTexts:
    st4TempSensorConfigTable.setStatus("current")
_St4TempSensorConfigEntry_Object = MibTableRow
st4TempSensorConfigEntry = _St4TempSensorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 2, 1)
)
st4TempSensorConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4TempSensorIndex"),
)
if mibBuilder.loadTexts:
    st4TempSensorConfigEntry.setStatus("current")


class _St4TempSensorIndex_Type(Integer32):
    """Custom type st4TempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_St4TempSensorIndex_Type.__name__ = "Integer32"
_St4TempSensorIndex_Object = MibTableColumn
st4TempSensorIndex = _St4TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 2, 1, 1),
    _St4TempSensorIndex_Type()
)
st4TempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4TempSensorIndex.setStatus("current")


class _St4TempSensorID_Type(DisplayString):
    """Custom type st4TempSensorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_St4TempSensorID_Type.__name__ = "DisplayString"
_St4TempSensorID_Object = MibTableColumn
st4TempSensorID = _St4TempSensorID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 2, 1, 2),
    _St4TempSensorID_Type()
)
st4TempSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4TempSensorID.setStatus("current")


class _St4TempSensorName_Type(DisplayString):
    """Custom type st4TempSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4TempSensorName_Type.__name__ = "DisplayString"
_St4TempSensorName_Object = MibTableColumn
st4TempSensorName = _St4TempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 2, 1, 3),
    _St4TempSensorName_Type()
)
st4TempSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4TempSensorName.setStatus("current")


class _St4TempSensorValueMin_Type(Integer32):
    """Custom type st4TempSensorValueMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 253),
    )


_St4TempSensorValueMin_Type.__name__ = "Integer32"
_St4TempSensorValueMin_Object = MibTableColumn
st4TempSensorValueMin = _St4TempSensorValueMin_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 2, 1, 4),
    _St4TempSensorValueMin_Type()
)
st4TempSensorValueMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4TempSensorValueMin.setStatus("current")
if mibBuilder.loadTexts:
    st4TempSensorValueMin.setUnits("degrees")


class _St4TempSensorValueMax_Type(Integer32):
    """Custom type st4TempSensorValueMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 253),
    )


_St4TempSensorValueMax_Type.__name__ = "Integer32"
_St4TempSensorValueMax_Object = MibTableColumn
st4TempSensorValueMax = _St4TempSensorValueMax_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 2, 1, 5),
    _St4TempSensorValueMax_Type()
)
st4TempSensorValueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4TempSensorValueMax.setStatus("current")
if mibBuilder.loadTexts:
    st4TempSensorValueMax.setUnits("degrees")
_St4TempSensorMonitorTable_Object = MibTable
st4TempSensorMonitorTable = _St4TempSensorMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 3)
)
if mibBuilder.loadTexts:
    st4TempSensorMonitorTable.setStatus("current")
_St4TempSensorMonitorEntry_Object = MibTableRow
st4TempSensorMonitorEntry = _St4TempSensorMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 3, 1)
)
st4TempSensorMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4TempSensorIndex"),
)
if mibBuilder.loadTexts:
    st4TempSensorMonitorEntry.setStatus("current")


class _St4TempSensorValue_Type(Integer32):
    """Custom type st4TempSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-410, 2540),
    )


_St4TempSensorValue_Type.__name__ = "Integer32"
_St4TempSensorValue_Object = MibTableColumn
st4TempSensorValue = _St4TempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 3, 1, 1),
    _St4TempSensorValue_Type()
)
st4TempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4TempSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    st4TempSensorValue.setUnits("tenth degrees")
_St4TempSensorStatus_Type = DeviceStatus
_St4TempSensorStatus_Object = MibTableColumn
st4TempSensorStatus = _St4TempSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 3, 1, 2),
    _St4TempSensorStatus_Type()
)
st4TempSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4TempSensorStatus.setStatus("current")
_St4TempSensorEventConfigTable_Object = MibTable
st4TempSensorEventConfigTable = _St4TempSensorEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 4)
)
if mibBuilder.loadTexts:
    st4TempSensorEventConfigTable.setStatus("current")
_St4TempSensorEventConfigEntry_Object = MibTableRow
st4TempSensorEventConfigEntry = _St4TempSensorEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 4, 1)
)
st4TempSensorEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4TempSensorIndex"),
)
if mibBuilder.loadTexts:
    st4TempSensorEventConfigEntry.setStatus("current")
_St4TempSensorNotifications_Type = EventNotificationMethods
_St4TempSensorNotifications_Object = MibTableColumn
st4TempSensorNotifications = _St4TempSensorNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 4, 1, 1),
    _St4TempSensorNotifications_Type()
)
st4TempSensorNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4TempSensorNotifications.setStatus("current")


class _St4TempSensorLowAlarm_Type(Integer32):
    """Custom type st4TempSensorLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 253),
    )


_St4TempSensorLowAlarm_Type.__name__ = "Integer32"
_St4TempSensorLowAlarm_Object = MibTableColumn
st4TempSensorLowAlarm = _St4TempSensorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 4, 1, 2),
    _St4TempSensorLowAlarm_Type()
)
st4TempSensorLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4TempSensorLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4TempSensorLowAlarm.setUnits("degrees")


class _St4TempSensorLowWarning_Type(Integer32):
    """Custom type st4TempSensorLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 253),
    )


_St4TempSensorLowWarning_Type.__name__ = "Integer32"
_St4TempSensorLowWarning_Object = MibTableColumn
st4TempSensorLowWarning = _St4TempSensorLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 4, 1, 3),
    _St4TempSensorLowWarning_Type()
)
st4TempSensorLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4TempSensorLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4TempSensorLowWarning.setUnits("degrees")


class _St4TempSensorHighWarning_Type(Integer32):
    """Custom type st4TempSensorHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 253),
    )


_St4TempSensorHighWarning_Type.__name__ = "Integer32"
_St4TempSensorHighWarning_Object = MibTableColumn
st4TempSensorHighWarning = _St4TempSensorHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 4, 1, 4),
    _St4TempSensorHighWarning_Type()
)
st4TempSensorHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4TempSensorHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4TempSensorHighWarning.setUnits("degrees")


class _St4TempSensorHighAlarm_Type(Integer32):
    """Custom type st4TempSensorHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 253),
    )


_St4TempSensorHighAlarm_Type.__name__ = "Integer32"
_St4TempSensorHighAlarm_Object = MibTableColumn
st4TempSensorHighAlarm = _St4TempSensorHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 9, 4, 1, 5),
    _St4TempSensorHighAlarm_Type()
)
st4TempSensorHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4TempSensorHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4TempSensorHighAlarm.setUnits("degrees")
_St4HumiditySensors_ObjectIdentity = ObjectIdentity
st4HumiditySensors = _St4HumiditySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10)
)
_St4HumidSensorCommonConfig_ObjectIdentity = ObjectIdentity
st4HumidSensorCommonConfig = _St4HumidSensorCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 1)
)


class _St4HumidSensorHysteresis_Type(Integer32):
    """Custom type st4HumidSensorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_St4HumidSensorHysteresis_Type.__name__ = "Integer32"
_St4HumidSensorHysteresis_Object = MibScalar
st4HumidSensorHysteresis = _St4HumidSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 1, 1),
    _St4HumidSensorHysteresis_Type()
)
st4HumidSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4HumidSensorHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    st4HumidSensorHysteresis.setUnits("percentage relative humidity")
_St4HumidSensorConfigTable_Object = MibTable
st4HumidSensorConfigTable = _St4HumidSensorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 2)
)
if mibBuilder.loadTexts:
    st4HumidSensorConfigTable.setStatus("current")
_St4HumidSensorConfigEntry_Object = MibTableRow
st4HumidSensorConfigEntry = _St4HumidSensorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 2, 1)
)
st4HumidSensorConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4HumidSensorIndex"),
)
if mibBuilder.loadTexts:
    st4HumidSensorConfigEntry.setStatus("current")


class _St4HumidSensorIndex_Type(Integer32):
    """Custom type st4HumidSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_St4HumidSensorIndex_Type.__name__ = "Integer32"
_St4HumidSensorIndex_Object = MibTableColumn
st4HumidSensorIndex = _St4HumidSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 2, 1, 1),
    _St4HumidSensorIndex_Type()
)
st4HumidSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4HumidSensorIndex.setStatus("current")


class _St4HumidSensorID_Type(DisplayString):
    """Custom type st4HumidSensorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_St4HumidSensorID_Type.__name__ = "DisplayString"
_St4HumidSensorID_Object = MibTableColumn
st4HumidSensorID = _St4HumidSensorID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 2, 1, 2),
    _St4HumidSensorID_Type()
)
st4HumidSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4HumidSensorID.setStatus("current")


class _St4HumidSensorName_Type(DisplayString):
    """Custom type st4HumidSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4HumidSensorName_Type.__name__ = "DisplayString"
_St4HumidSensorName_Object = MibTableColumn
st4HumidSensorName = _St4HumidSensorName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 2, 1, 3),
    _St4HumidSensorName_Type()
)
st4HumidSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4HumidSensorName.setStatus("current")
_St4HumidSensorMonitorTable_Object = MibTable
st4HumidSensorMonitorTable = _St4HumidSensorMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 3)
)
if mibBuilder.loadTexts:
    st4HumidSensorMonitorTable.setStatus("current")
_St4HumidSensorMonitorEntry_Object = MibTableRow
st4HumidSensorMonitorEntry = _St4HumidSensorMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 3, 1)
)
st4HumidSensorMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4HumidSensorIndex"),
)
if mibBuilder.loadTexts:
    st4HumidSensorMonitorEntry.setStatus("current")


class _St4HumidSensorValue_Type(Integer32):
    """Custom type st4HumidSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_St4HumidSensorValue_Type.__name__ = "Integer32"
_St4HumidSensorValue_Object = MibTableColumn
st4HumidSensorValue = _St4HumidSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 3, 1, 1),
    _St4HumidSensorValue_Type()
)
st4HumidSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4HumidSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    st4HumidSensorValue.setUnits("percentage relative humidity")
_St4HumidSensorStatus_Type = DeviceStatus
_St4HumidSensorStatus_Object = MibTableColumn
st4HumidSensorStatus = _St4HumidSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 3, 1, 2),
    _St4HumidSensorStatus_Type()
)
st4HumidSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4HumidSensorStatus.setStatus("current")
_St4HumidSensorEventConfigTable_Object = MibTable
st4HumidSensorEventConfigTable = _St4HumidSensorEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 4)
)
if mibBuilder.loadTexts:
    st4HumidSensorEventConfigTable.setStatus("current")
_St4HumidSensorEventConfigEntry_Object = MibTableRow
st4HumidSensorEventConfigEntry = _St4HumidSensorEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 4, 1)
)
st4HumidSensorEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4HumidSensorIndex"),
)
if mibBuilder.loadTexts:
    st4HumidSensorEventConfigEntry.setStatus("current")
_St4HumidSensorNotifications_Type = EventNotificationMethods
_St4HumidSensorNotifications_Object = MibTableColumn
st4HumidSensorNotifications = _St4HumidSensorNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 4, 1, 1),
    _St4HumidSensorNotifications_Type()
)
st4HumidSensorNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4HumidSensorNotifications.setStatus("current")


class _St4HumidSensorLowAlarm_Type(Integer32):
    """Custom type st4HumidSensorLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4HumidSensorLowAlarm_Type.__name__ = "Integer32"
_St4HumidSensorLowAlarm_Object = MibTableColumn
st4HumidSensorLowAlarm = _St4HumidSensorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 4, 1, 2),
    _St4HumidSensorLowAlarm_Type()
)
st4HumidSensorLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4HumidSensorLowAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4HumidSensorLowAlarm.setUnits("percentage relative humidity")


class _St4HumidSensorLowWarning_Type(Integer32):
    """Custom type st4HumidSensorLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4HumidSensorLowWarning_Type.__name__ = "Integer32"
_St4HumidSensorLowWarning_Object = MibTableColumn
st4HumidSensorLowWarning = _St4HumidSensorLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 4, 1, 3),
    _St4HumidSensorLowWarning_Type()
)
st4HumidSensorLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4HumidSensorLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4HumidSensorLowWarning.setUnits("percentage relative humidity")


class _St4HumidSensorHighWarning_Type(Integer32):
    """Custom type st4HumidSensorHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4HumidSensorHighWarning_Type.__name__ = "Integer32"
_St4HumidSensorHighWarning_Object = MibTableColumn
st4HumidSensorHighWarning = _St4HumidSensorHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 4, 1, 4),
    _St4HumidSensorHighWarning_Type()
)
st4HumidSensorHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4HumidSensorHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    st4HumidSensorHighWarning.setUnits("percentage relative humidity")


class _St4HumidSensorHighAlarm_Type(Integer32):
    """Custom type st4HumidSensorHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_St4HumidSensorHighAlarm_Type.__name__ = "Integer32"
_St4HumidSensorHighAlarm_Object = MibTableColumn
st4HumidSensorHighAlarm = _St4HumidSensorHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 10, 4, 1, 5),
    _St4HumidSensorHighAlarm_Type()
)
st4HumidSensorHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4HumidSensorHighAlarm.setStatus("current")
if mibBuilder.loadTexts:
    st4HumidSensorHighAlarm.setUnits("percentage relative humidity")
_St4WaterSensors_ObjectIdentity = ObjectIdentity
st4WaterSensors = _St4WaterSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11)
)
_St4WaterSensorCommonConfig_ObjectIdentity = ObjectIdentity
st4WaterSensorCommonConfig = _St4WaterSensorCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 1)
)
_St4WaterSensorConfigTable_Object = MibTable
st4WaterSensorConfigTable = _St4WaterSensorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 2)
)
if mibBuilder.loadTexts:
    st4WaterSensorConfigTable.setStatus("current")
_St4WaterSensorConfigEntry_Object = MibTableRow
st4WaterSensorConfigEntry = _St4WaterSensorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 2, 1)
)
st4WaterSensorConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4WaterSensorIndex"),
)
if mibBuilder.loadTexts:
    st4WaterSensorConfigEntry.setStatus("current")


class _St4WaterSensorIndex_Type(Integer32):
    """Custom type st4WaterSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_St4WaterSensorIndex_Type.__name__ = "Integer32"
_St4WaterSensorIndex_Object = MibTableColumn
st4WaterSensorIndex = _St4WaterSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 2, 1, 1),
    _St4WaterSensorIndex_Type()
)
st4WaterSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4WaterSensorIndex.setStatus("current")


class _St4WaterSensorID_Type(DisplayString):
    """Custom type st4WaterSensorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_St4WaterSensorID_Type.__name__ = "DisplayString"
_St4WaterSensorID_Object = MibTableColumn
st4WaterSensorID = _St4WaterSensorID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 2, 1, 2),
    _St4WaterSensorID_Type()
)
st4WaterSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4WaterSensorID.setStatus("current")


class _St4WaterSensorName_Type(DisplayString):
    """Custom type st4WaterSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4WaterSensorName_Type.__name__ = "DisplayString"
_St4WaterSensorName_Object = MibTableColumn
st4WaterSensorName = _St4WaterSensorName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 2, 1, 3),
    _St4WaterSensorName_Type()
)
st4WaterSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4WaterSensorName.setStatus("current")
_St4WaterSensorMonitorTable_Object = MibTable
st4WaterSensorMonitorTable = _St4WaterSensorMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 3)
)
if mibBuilder.loadTexts:
    st4WaterSensorMonitorTable.setStatus("current")
_St4WaterSensorMonitorEntry_Object = MibTableRow
st4WaterSensorMonitorEntry = _St4WaterSensorMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 3, 1)
)
st4WaterSensorMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4WaterSensorIndex"),
)
if mibBuilder.loadTexts:
    st4WaterSensorMonitorEntry.setStatus("current")
_St4WaterSensorStatus_Type = DeviceStatus
_St4WaterSensorStatus_Object = MibTableColumn
st4WaterSensorStatus = _St4WaterSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 3, 1, 1),
    _St4WaterSensorStatus_Type()
)
st4WaterSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4WaterSensorStatus.setStatus("current")
_St4WaterSensorEventConfigTable_Object = MibTable
st4WaterSensorEventConfigTable = _St4WaterSensorEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 4)
)
if mibBuilder.loadTexts:
    st4WaterSensorEventConfigTable.setStatus("current")
_St4WaterSensorEventConfigEntry_Object = MibTableRow
st4WaterSensorEventConfigEntry = _St4WaterSensorEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 4, 1)
)
st4WaterSensorEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4WaterSensorIndex"),
)
if mibBuilder.loadTexts:
    st4WaterSensorEventConfigEntry.setStatus("current")
_St4WaterSensorNotifications_Type = EventNotificationMethods
_St4WaterSensorNotifications_Object = MibTableColumn
st4WaterSensorNotifications = _St4WaterSensorNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 11, 4, 1, 1),
    _St4WaterSensorNotifications_Type()
)
st4WaterSensorNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4WaterSensorNotifications.setStatus("current")
_St4ContactClosureSensors_ObjectIdentity = ObjectIdentity
st4ContactClosureSensors = _St4ContactClosureSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12)
)
_St4CcSensorCommonConfig_ObjectIdentity = ObjectIdentity
st4CcSensorCommonConfig = _St4CcSensorCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 1)
)
_St4CcSensorConfigTable_Object = MibTable
st4CcSensorConfigTable = _St4CcSensorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 2)
)
if mibBuilder.loadTexts:
    st4CcSensorConfigTable.setStatus("current")
_St4CcSensorConfigEntry_Object = MibTableRow
st4CcSensorConfigEntry = _St4CcSensorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 2, 1)
)
st4CcSensorConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4CcSensorIndex"),
)
if mibBuilder.loadTexts:
    st4CcSensorConfigEntry.setStatus("current")


class _St4CcSensorIndex_Type(Integer32):
    """Custom type st4CcSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_St4CcSensorIndex_Type.__name__ = "Integer32"
_St4CcSensorIndex_Object = MibTableColumn
st4CcSensorIndex = _St4CcSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 2, 1, 1),
    _St4CcSensorIndex_Type()
)
st4CcSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4CcSensorIndex.setStatus("current")


class _St4CcSensorID_Type(DisplayString):
    """Custom type st4CcSensorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_St4CcSensorID_Type.__name__ = "DisplayString"
_St4CcSensorID_Object = MibTableColumn
st4CcSensorID = _St4CcSensorID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 2, 1, 2),
    _St4CcSensorID_Type()
)
st4CcSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4CcSensorID.setStatus("current")


class _St4CcSensorName_Type(DisplayString):
    """Custom type st4CcSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4CcSensorName_Type.__name__ = "DisplayString"
_St4CcSensorName_Object = MibTableColumn
st4CcSensorName = _St4CcSensorName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 2, 1, 3),
    _St4CcSensorName_Type()
)
st4CcSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4CcSensorName.setStatus("current")
_St4CcSensorMonitorTable_Object = MibTable
st4CcSensorMonitorTable = _St4CcSensorMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 3)
)
if mibBuilder.loadTexts:
    st4CcSensorMonitorTable.setStatus("current")
_St4CcSensorMonitorEntry_Object = MibTableRow
st4CcSensorMonitorEntry = _St4CcSensorMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 3, 1)
)
st4CcSensorMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4CcSensorIndex"),
)
if mibBuilder.loadTexts:
    st4CcSensorMonitorEntry.setStatus("current")
_St4CcSensorStatus_Type = DeviceStatus
_St4CcSensorStatus_Object = MibTableColumn
st4CcSensorStatus = _St4CcSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 3, 1, 1),
    _St4CcSensorStatus_Type()
)
st4CcSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4CcSensorStatus.setStatus("current")
_St4CcSensorEventConfigTable_Object = MibTable
st4CcSensorEventConfigTable = _St4CcSensorEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 4)
)
if mibBuilder.loadTexts:
    st4CcSensorEventConfigTable.setStatus("current")
_St4CcSensorEventConfigEntry_Object = MibTableRow
st4CcSensorEventConfigEntry = _St4CcSensorEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 4, 1)
)
st4CcSensorEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4CcSensorIndex"),
)
if mibBuilder.loadTexts:
    st4CcSensorEventConfigEntry.setStatus("current")
_St4CcSensorNotifications_Type = EventNotificationMethods
_St4CcSensorNotifications_Object = MibTableColumn
st4CcSensorNotifications = _St4CcSensorNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 12, 4, 1, 1),
    _St4CcSensorNotifications_Type()
)
st4CcSensorNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4CcSensorNotifications.setStatus("current")
_St4AnalogToDigitalConvSensors_ObjectIdentity = ObjectIdentity
st4AnalogToDigitalConvSensors = _St4AnalogToDigitalConvSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13)
)
_St4AdcSensorCommonConfig_ObjectIdentity = ObjectIdentity
st4AdcSensorCommonConfig = _St4AdcSensorCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 1)
)


class _St4AdcSensorHysteresis_Type(Integer32):
    """Custom type st4AdcSensorHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_St4AdcSensorHysteresis_Type.__name__ = "Integer32"
_St4AdcSensorHysteresis_Object = MibScalar
st4AdcSensorHysteresis = _St4AdcSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 1, 1),
    _St4AdcSensorHysteresis_Type()
)
st4AdcSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4AdcSensorHysteresis.setStatus("current")
_St4AdcSensorConfigTable_Object = MibTable
st4AdcSensorConfigTable = _St4AdcSensorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 2)
)
if mibBuilder.loadTexts:
    st4AdcSensorConfigTable.setStatus("current")
_St4AdcSensorConfigEntry_Object = MibTableRow
st4AdcSensorConfigEntry = _St4AdcSensorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 2, 1)
)
st4AdcSensorConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4AdcSensorIndex"),
)
if mibBuilder.loadTexts:
    st4AdcSensorConfigEntry.setStatus("current")


class _St4AdcSensorIndex_Type(Integer32):
    """Custom type st4AdcSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_St4AdcSensorIndex_Type.__name__ = "Integer32"
_St4AdcSensorIndex_Object = MibTableColumn
st4AdcSensorIndex = _St4AdcSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 2, 1, 1),
    _St4AdcSensorIndex_Type()
)
st4AdcSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    st4AdcSensorIndex.setStatus("current")


class _St4AdcSensorID_Type(DisplayString):
    """Custom type st4AdcSensorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_St4AdcSensorID_Type.__name__ = "DisplayString"
_St4AdcSensorID_Object = MibTableColumn
st4AdcSensorID = _St4AdcSensorID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 2, 1, 2),
    _St4AdcSensorID_Type()
)
st4AdcSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4AdcSensorID.setStatus("current")


class _St4AdcSensorName_Type(DisplayString):
    """Custom type st4AdcSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_St4AdcSensorName_Type.__name__ = "DisplayString"
_St4AdcSensorName_Object = MibTableColumn
st4AdcSensorName = _St4AdcSensorName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 2, 1, 3),
    _St4AdcSensorName_Type()
)
st4AdcSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4AdcSensorName.setStatus("current")
_St4AdcSensorMonitorTable_Object = MibTable
st4AdcSensorMonitorTable = _St4AdcSensorMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 3)
)
if mibBuilder.loadTexts:
    st4AdcSensorMonitorTable.setStatus("current")
_St4AdcSensorMonitorEntry_Object = MibTableRow
st4AdcSensorMonitorEntry = _St4AdcSensorMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 3, 1)
)
st4AdcSensorMonitorEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4AdcSensorIndex"),
)
if mibBuilder.loadTexts:
    st4AdcSensorMonitorEntry.setStatus("current")


class _St4AdcSensorValue_Type(Integer32):
    """Custom type st4AdcSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_St4AdcSensorValue_Type.__name__ = "Integer32"
_St4AdcSensorValue_Object = MibTableColumn
st4AdcSensorValue = _St4AdcSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 3, 1, 1),
    _St4AdcSensorValue_Type()
)
st4AdcSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4AdcSensorValue.setStatus("current")
_St4AdcSensorStatus_Type = DeviceStatus
_St4AdcSensorStatus_Object = MibTableColumn
st4AdcSensorStatus = _St4AdcSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 3, 1, 2),
    _St4AdcSensorStatus_Type()
)
st4AdcSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4AdcSensorStatus.setStatus("current")
_St4AdcSensorEventConfigTable_Object = MibTable
st4AdcSensorEventConfigTable = _St4AdcSensorEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 4)
)
if mibBuilder.loadTexts:
    st4AdcSensorEventConfigTable.setStatus("current")
_St4AdcSensorEventConfigEntry_Object = MibTableRow
st4AdcSensorEventConfigEntry = _St4AdcSensorEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 4, 1)
)
st4AdcSensorEventConfigEntry.setIndexNames(
    (0, "Sentry4-MIB", "st4UnitIndex"),
    (0, "Sentry4-MIB", "st4AdcSensorIndex"),
)
if mibBuilder.loadTexts:
    st4AdcSensorEventConfigEntry.setStatus("current")
_St4AdcSensorNotifications_Type = EventNotificationMethods
_St4AdcSensorNotifications_Object = MibTableColumn
st4AdcSensorNotifications = _St4AdcSensorNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 4, 1, 1),
    _St4AdcSensorNotifications_Type()
)
st4AdcSensorNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4AdcSensorNotifications.setStatus("current")


class _St4AdcSensorLowAlarm_Type(Integer32):
    """Custom type st4AdcSensorLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_St4AdcSensorLowAlarm_Type.__name__ = "Integer32"
_St4AdcSensorLowAlarm_Object = MibTableColumn
st4AdcSensorLowAlarm = _St4AdcSensorLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 4, 1, 2),
    _St4AdcSensorLowAlarm_Type()
)
st4AdcSensorLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4AdcSensorLowAlarm.setStatus("current")


class _St4AdcSensorLowWarning_Type(Integer32):
    """Custom type st4AdcSensorLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_St4AdcSensorLowWarning_Type.__name__ = "Integer32"
_St4AdcSensorLowWarning_Object = MibTableColumn
st4AdcSensorLowWarning = _St4AdcSensorLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 4, 1, 3),
    _St4AdcSensorLowWarning_Type()
)
st4AdcSensorLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4AdcSensorLowWarning.setStatus("current")


class _St4AdcSensorHighWarning_Type(Integer32):
    """Custom type st4AdcSensorHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_St4AdcSensorHighWarning_Type.__name__ = "Integer32"
_St4AdcSensorHighWarning_Object = MibTableColumn
st4AdcSensorHighWarning = _St4AdcSensorHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 4, 1, 4),
    _St4AdcSensorHighWarning_Type()
)
st4AdcSensorHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4AdcSensorHighWarning.setStatus("current")


class _St4AdcSensorHighAlarm_Type(Integer32):
    """Custom type st4AdcSensorHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_St4AdcSensorHighAlarm_Type.__name__ = "Integer32"
_St4AdcSensorHighAlarm_Object = MibTableColumn
st4AdcSensorHighAlarm = _St4AdcSensorHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 13, 4, 1, 5),
    _St4AdcSensorHighAlarm_Type()
)
st4AdcSensorHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    st4AdcSensorHighAlarm.setStatus("current")
_St4EventInformation_ObjectIdentity = ObjectIdentity
st4EventInformation = _St4EventInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 99)
)


class _St4EventStatusText_Type(DisplayString):
    """Custom type st4EventStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_St4EventStatusText_Type.__name__ = "DisplayString"
_St4EventStatusText_Object = MibScalar
st4EventStatusText = _St4EventStatusText_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 99, 1),
    _St4EventStatusText_Type()
)
st4EventStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4EventStatusText.setStatus("current")


class _St4EventStatusCondition_Type(Integer32):
    """Custom type st4EventStatusCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("nonError", 0))
    )


_St4EventStatusCondition_Type.__name__ = "Integer32"
_St4EventStatusCondition_Object = MibScalar
st4EventStatusCondition = _St4EventStatusCondition_Object(
    (1, 3, 6, 1, 4, 1, 1718, 4, 1, 99, 2),
    _St4EventStatusCondition_Type()
)
st4EventStatusCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    st4EventStatusCondition.setStatus("current")
_St4Notifications_ObjectIdentity = ObjectIdentity
st4Notifications = _St4Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100)
)
_St4Events_ObjectIdentity = ObjectIdentity
st4Events = _St4Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0)
)
_St4Conformance_ObjectIdentity = ObjectIdentity
st4Conformance = _St4Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200)
)
_St4Groups_ObjectIdentity = ObjectIdentity
st4Groups = _St4Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1)
)
_St4Compliances_ObjectIdentity = ObjectIdentity
st4Compliances = _St4Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 2)
)

# Managed Objects groups

st4SystemObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 1)
)
st4SystemObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4SystemProductName"),
        ("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4SystemFirmwareVersion"),
        ("Sentry4-MIB", "st4SystemFirmwareBuildInfo"),
        ("Sentry4-MIB", "st4SystemNICSerialNumber"),
        ("Sentry4-MIB", "st4SystemNICHardwareInfo"),
        ("Sentry4-MIB", "st4SystemProductSeries"),
        ("Sentry4-MIB", "st4SystemFeatures"),
        ("Sentry4-MIB", "st4SystemFeatureKey"),
        ("Sentry4-MIB", "st4SystemConfigModifiedCount"),
        ("Sentry4-MIB", "st4SystemUnitCount"))
)
if mibBuilder.loadTexts:
    st4SystemObjectsGroup.setStatus("current")

st4UnitObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 2)
)
st4UnitObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4UnitID"),
        ("Sentry4-MIB", "st4UnitName"),
        ("Sentry4-MIB", "st4UnitProductSN"),
        ("Sentry4-MIB", "st4UnitModel"),
        ("Sentry4-MIB", "st4UnitAssetTag"),
        ("Sentry4-MIB", "st4UnitType"),
        ("Sentry4-MIB", "st4UnitCapabilities"),
        ("Sentry4-MIB", "st4UnitProductMfrDate"),
        ("Sentry4-MIB", "st4UnitDisplayOrientation"),
        ("Sentry4-MIB", "st4UnitOutletSequenceOrder"),
        ("Sentry4-MIB", "st4UnitInputCordCount"),
        ("Sentry4-MIB", "st4UnitTempSensorCount"),
        ("Sentry4-MIB", "st4UnitHumidSensorCount"),
        ("Sentry4-MIB", "st4UnitWaterSensorCount"),
        ("Sentry4-MIB", "st4UnitCcSensorCount"),
        ("Sentry4-MIB", "st4UnitAdcSensorCount"),
        ("Sentry4-MIB", "st4UnitStatus"),
        ("Sentry4-MIB", "st4UnitNotifications"))
)
if mibBuilder.loadTexts:
    st4UnitObjectsGroup.setStatus("current")

st4InputCordObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 3)
)
st4InputCordObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4InputCordActivePowerHysteresis"),
        ("Sentry4-MIB", "st4InputCordApparentPowerHysteresis"),
        ("Sentry4-MIB", "st4InputCordPowerFactorHysteresis"),
        ("Sentry4-MIB", "st4InputCordOutOfBalanceHysteresis"),
        ("Sentry4-MIB", "st4InputCordID"),
        ("Sentry4-MIB", "st4InputCordName"),
        ("Sentry4-MIB", "st4InputCordInletType"),
        ("Sentry4-MIB", "st4InputCordNominalVoltage"),
        ("Sentry4-MIB", "st4InputCordNominalVoltageMin"),
        ("Sentry4-MIB", "st4InputCordNominalVoltageMax"),
        ("Sentry4-MIB", "st4InputCordCurrentCapacity"),
        ("Sentry4-MIB", "st4InputCordCurrentCapacityMax"),
        ("Sentry4-MIB", "st4InputCordPowerCapacity"),
        ("Sentry4-MIB", "st4InputCordNominalPowerFactor"),
        ("Sentry4-MIB", "st4InputCordLineCount"),
        ("Sentry4-MIB", "st4InputCordPhaseCount"),
        ("Sentry4-MIB", "st4InputCordOcpCount"),
        ("Sentry4-MIB", "st4InputCordBranchCount"),
        ("Sentry4-MIB", "st4InputCordOutletCount"),
        ("Sentry4-MIB", "st4InputCordState"),
        ("Sentry4-MIB", "st4InputCordStatus"),
        ("Sentry4-MIB", "st4InputCordActivePower"),
        ("Sentry4-MIB", "st4InputCordActivePowerStatus"),
        ("Sentry4-MIB", "st4InputCordApparentPower"),
        ("Sentry4-MIB", "st4InputCordApparentPowerStatus"),
        ("Sentry4-MIB", "st4InputCordPowerUtilized"),
        ("Sentry4-MIB", "st4InputCordPowerFactor"),
        ("Sentry4-MIB", "st4InputCordPowerFactorStatus"),
        ("Sentry4-MIB", "st4InputCordEnergy"),
        ("Sentry4-MIB", "st4InputCordFrequency"),
        ("Sentry4-MIB", "st4InputCordOutOfBalance"),
        ("Sentry4-MIB", "st4InputCordOutOfBalanceStatus"),
        ("Sentry4-MIB", "st4InputCordNotifications"),
        ("Sentry4-MIB", "st4InputCordActivePowerLowAlarm"),
        ("Sentry4-MIB", "st4InputCordActivePowerLowWarning"),
        ("Sentry4-MIB", "st4InputCordActivePowerHighWarning"),
        ("Sentry4-MIB", "st4InputCordActivePowerHighAlarm"),
        ("Sentry4-MIB", "st4InputCordApparentPowerLowAlarm"),
        ("Sentry4-MIB", "st4InputCordApparentPowerLowWarning"),
        ("Sentry4-MIB", "st4InputCordApparentPowerHighWarning"),
        ("Sentry4-MIB", "st4InputCordApparentPowerHighAlarm"),
        ("Sentry4-MIB", "st4InputCordPowerFactorLowAlarm"),
        ("Sentry4-MIB", "st4InputCordPowerFactorLowWarning"),
        ("Sentry4-MIB", "st4InputCordOutOfBalanceHighWarning"),
        ("Sentry4-MIB", "st4InputCordOutOfBalanceHighAlarm"))
)
if mibBuilder.loadTexts:
    st4InputCordObjectsGroup.setStatus("current")

st4LineObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 4)
)
st4LineObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4LineCurrentHysteresis"),
        ("Sentry4-MIB", "st4LineID"),
        ("Sentry4-MIB", "st4LineLabel"),
        ("Sentry4-MIB", "st4LineCurrentCapacity"),
        ("Sentry4-MIB", "st4LineState"),
        ("Sentry4-MIB", "st4LineStatus"),
        ("Sentry4-MIB", "st4LineCurrent"),
        ("Sentry4-MIB", "st4LineCurrentStatus"),
        ("Sentry4-MIB", "st4LineCurrentUtilized"),
        ("Sentry4-MIB", "st4LineNotifications"),
        ("Sentry4-MIB", "st4LineCurrentLowAlarm"),
        ("Sentry4-MIB", "st4LineCurrentLowWarning"),
        ("Sentry4-MIB", "st4LineCurrentHighWarning"),
        ("Sentry4-MIB", "st4LineCurrentHighAlarm"))
)
if mibBuilder.loadTexts:
    st4LineObjectsGroup.setStatus("current")

st4PhaseObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 5)
)
st4PhaseObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4PhaseVoltageHysteresis"),
        ("Sentry4-MIB", "st4PhasePowerFactorHysteresis"),
        ("Sentry4-MIB", "st4PhaseID"),
        ("Sentry4-MIB", "st4PhaseLabel"),
        ("Sentry4-MIB", "st4PhaseNominalVoltage"),
        ("Sentry4-MIB", "st4PhaseBranchCount"),
        ("Sentry4-MIB", "st4PhaseOutletCount"),
        ("Sentry4-MIB", "st4PhaseState"),
        ("Sentry4-MIB", "st4PhaseStatus"),
        ("Sentry4-MIB", "st4PhaseVoltage"),
        ("Sentry4-MIB", "st4PhaseVoltageStatus"),
        ("Sentry4-MIB", "st4PhaseVoltageDeviation"),
        ("Sentry4-MIB", "st4PhaseCurrent"),
        ("Sentry4-MIB", "st4PhaseCurrentCrestFactor"),
        ("Sentry4-MIB", "st4PhaseActivePower"),
        ("Sentry4-MIB", "st4PhaseApparentPower"),
        ("Sentry4-MIB", "st4PhasePowerFactor"),
        ("Sentry4-MIB", "st4PhasePowerFactorStatus"),
        ("Sentry4-MIB", "st4PhaseReactance"),
        ("Sentry4-MIB", "st4PhaseEnergy"),
        ("Sentry4-MIB", "st4PhaseNotifications"),
        ("Sentry4-MIB", "st4PhaseVoltageLowAlarm"),
        ("Sentry4-MIB", "st4PhaseVoltageLowWarning"),
        ("Sentry4-MIB", "st4PhaseVoltageHighWarning"),
        ("Sentry4-MIB", "st4PhaseVoltageHighAlarm"),
        ("Sentry4-MIB", "st4PhasePowerFactorLowAlarm"),
        ("Sentry4-MIB", "st4PhasePowerFactorLowWarning"))
)
if mibBuilder.loadTexts:
    st4PhaseObjectsGroup.setStatus("current")

st4OcpObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 6)
)
st4OcpObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4OcpID"),
        ("Sentry4-MIB", "st4OcpLabel"),
        ("Sentry4-MIB", "st4OcpType"),
        ("Sentry4-MIB", "st4OcpCurrentCapacity"),
        ("Sentry4-MIB", "st4OcpCurrentCapacityMax"),
        ("Sentry4-MIB", "st4OcpBranchCount"),
        ("Sentry4-MIB", "st4OcpOutletCount"),
        ("Sentry4-MIB", "st4OcpStatus"),
        ("Sentry4-MIB", "st4OcpNotifications"))
)
if mibBuilder.loadTexts:
    st4OcpObjectsGroup.setStatus("current")

st4BranchObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 7)
)
st4BranchObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4BranchCurrentHysteresis"),
        ("Sentry4-MIB", "st4BranchID"),
        ("Sentry4-MIB", "st4BranchLabel"),
        ("Sentry4-MIB", "st4BranchCurrentCapacity"),
        ("Sentry4-MIB", "st4BranchPhaseID"),
        ("Sentry4-MIB", "st4BranchOcpID"),
        ("Sentry4-MIB", "st4BranchOutletCount"),
        ("Sentry4-MIB", "st4BranchState"),
        ("Sentry4-MIB", "st4BranchStatus"),
        ("Sentry4-MIB", "st4BranchCurrent"),
        ("Sentry4-MIB", "st4BranchCurrentStatus"),
        ("Sentry4-MIB", "st4BranchCurrentUtilized"),
        ("Sentry4-MIB", "st4BranchNotifications"),
        ("Sentry4-MIB", "st4BranchCurrentLowAlarm"),
        ("Sentry4-MIB", "st4BranchCurrentLowWarning"),
        ("Sentry4-MIB", "st4BranchCurrentHighWarning"),
        ("Sentry4-MIB", "st4BranchCurrentHighAlarm"))
)
if mibBuilder.loadTexts:
    st4BranchObjectsGroup.setStatus("current")

st4OutletObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 8)
)
st4OutletObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4OutletCurrentHysteresis"),
        ("Sentry4-MIB", "st4OutletActivePowerHysteresis"),
        ("Sentry4-MIB", "st4OutletPowerFactorHysteresis"),
        ("Sentry4-MIB", "st4OutletSequenceInterval"),
        ("Sentry4-MIB", "st4OutletRebootDelay"),
        ("Sentry4-MIB", "st4OutletStateChangeLogging"),
        ("Sentry4-MIB", "st4OutletID"),
        ("Sentry4-MIB", "st4OutletName"),
        ("Sentry4-MIB", "st4OutletCapabilities"),
        ("Sentry4-MIB", "st4OutletSocketType"),
        ("Sentry4-MIB", "st4OutletCurrentCapacity"),
        ("Sentry4-MIB", "st4OutletPowerCapacity"),
        ("Sentry4-MIB", "st4OutletWakeupState"),
        ("Sentry4-MIB", "st4OutletPostOnDelay"),
        ("Sentry4-MIB", "st4OutletPhaseID"),
        ("Sentry4-MIB", "st4OutletOcpID"),
        ("Sentry4-MIB", "st4OutletBranchID"),
        ("Sentry4-MIB", "st4OutletState"),
        ("Sentry4-MIB", "st4OutletStatus"),
        ("Sentry4-MIB", "st4OutletCurrent"),
        ("Sentry4-MIB", "st4OutletCurrentStatus"),
        ("Sentry4-MIB", "st4OutletCurrentUtilized"),
        ("Sentry4-MIB", "st4OutletVoltage"),
        ("Sentry4-MIB", "st4OutletActivePower"),
        ("Sentry4-MIB", "st4OutletActivePowerStatus"),
        ("Sentry4-MIB", "st4OutletApparentPower"),
        ("Sentry4-MIB", "st4OutletPowerFactor"),
        ("Sentry4-MIB", "st4OutletPowerFactorStatus"),
        ("Sentry4-MIB", "st4OutletCurrentCrestFactor"),
        ("Sentry4-MIB", "st4OutletReactance"),
        ("Sentry4-MIB", "st4OutletEnergy"),
        ("Sentry4-MIB", "st4OutletNotifications"),
        ("Sentry4-MIB", "st4OutletCurrentLowAlarm"),
        ("Sentry4-MIB", "st4OutletCurrentLowWarning"),
        ("Sentry4-MIB", "st4OutletCurrentHighWarning"),
        ("Sentry4-MIB", "st4OutletCurrentHighAlarm"),
        ("Sentry4-MIB", "st4OutletActivePowerLowAlarm"),
        ("Sentry4-MIB", "st4OutletActivePowerLowWarning"),
        ("Sentry4-MIB", "st4OutletActivePowerHighWarning"),
        ("Sentry4-MIB", "st4OutletActivePowerHighAlarm"),
        ("Sentry4-MIB", "st4OutletPowerFactorLowAlarm"),
        ("Sentry4-MIB", "st4OutletPowerFactorLowWarning"),
        ("Sentry4-MIB", "st4OutletControlState"),
        ("Sentry4-MIB", "st4OutletControlAction"),
        ("Sentry4-MIB", "st4OutletQueueControl"))
)
if mibBuilder.loadTexts:
    st4OutletObjectsGroup.setStatus("current")

st4TempSensorObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 9)
)
st4TempSensorObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4TempSensorHysteresis"),
        ("Sentry4-MIB", "st4TempSensorScale"),
        ("Sentry4-MIB", "st4TempSensorID"),
        ("Sentry4-MIB", "st4TempSensorName"),
        ("Sentry4-MIB", "st4TempSensorValueMin"),
        ("Sentry4-MIB", "st4TempSensorValueMax"),
        ("Sentry4-MIB", "st4TempSensorValue"),
        ("Sentry4-MIB", "st4TempSensorStatus"),
        ("Sentry4-MIB", "st4TempSensorNotifications"),
        ("Sentry4-MIB", "st4TempSensorLowAlarm"),
        ("Sentry4-MIB", "st4TempSensorLowWarning"),
        ("Sentry4-MIB", "st4TempSensorHighWarning"),
        ("Sentry4-MIB", "st4TempSensorHighAlarm"))
)
if mibBuilder.loadTexts:
    st4TempSensorObjectsGroup.setStatus("current")

st4HumidSensorObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 10)
)
st4HumidSensorObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4HumidSensorHysteresis"),
        ("Sentry4-MIB", "st4HumidSensorID"),
        ("Sentry4-MIB", "st4HumidSensorName"),
        ("Sentry4-MIB", "st4HumidSensorValue"),
        ("Sentry4-MIB", "st4HumidSensorStatus"),
        ("Sentry4-MIB", "st4HumidSensorNotifications"),
        ("Sentry4-MIB", "st4HumidSensorLowAlarm"),
        ("Sentry4-MIB", "st4HumidSensorLowWarning"),
        ("Sentry4-MIB", "st4HumidSensorHighWarning"),
        ("Sentry4-MIB", "st4HumidSensorHighAlarm"))
)
if mibBuilder.loadTexts:
    st4HumidSensorObjectsGroup.setStatus("current")

st4WaterSensorObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 11)
)
st4WaterSensorObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4WaterSensorID"),
        ("Sentry4-MIB", "st4WaterSensorName"),
        ("Sentry4-MIB", "st4WaterSensorStatus"),
        ("Sentry4-MIB", "st4WaterSensorNotifications"))
)
if mibBuilder.loadTexts:
    st4WaterSensorObjectsGroup.setStatus("current")

st4CcSensorObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 12)
)
st4CcSensorObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4CcSensorID"),
        ("Sentry4-MIB", "st4CcSensorName"),
        ("Sentry4-MIB", "st4CcSensorStatus"),
        ("Sentry4-MIB", "st4CcSensorNotifications"))
)
if mibBuilder.loadTexts:
    st4CcSensorObjectsGroup.setStatus("current")

st4AdcSensorObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 13)
)
st4AdcSensorObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4AdcSensorHysteresis"),
        ("Sentry4-MIB", "st4AdcSensorID"),
        ("Sentry4-MIB", "st4AdcSensorName"),
        ("Sentry4-MIB", "st4AdcSensorValue"),
        ("Sentry4-MIB", "st4AdcSensorStatus"),
        ("Sentry4-MIB", "st4AdcSensorNotifications"),
        ("Sentry4-MIB", "st4AdcSensorLowAlarm"),
        ("Sentry4-MIB", "st4AdcSensorLowWarning"),
        ("Sentry4-MIB", "st4AdcSensorHighWarning"),
        ("Sentry4-MIB", "st4AdcSensorHighAlarm"))
)
if mibBuilder.loadTexts:
    st4AdcSensorObjectsGroup.setStatus("current")

st4EventInfoObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 99)
)
st4EventInfoObjectsGroup.setObjects(
      *(("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4EventInfoObjectsGroup.setStatus("current")


# Notification objects

st4UnitStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 1)
)
st4UnitStatusEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4UnitID"),
        ("Sentry4-MIB", "st4UnitName"),
        ("Sentry4-MIB", "st4UnitStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4UnitStatusEvent.setStatus(
        "current"
    )

st4InputCordStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 2)
)
st4InputCordStatusEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4InputCordID"),
        ("Sentry4-MIB", "st4InputCordName"),
        ("Sentry4-MIB", "st4InputCordState"),
        ("Sentry4-MIB", "st4InputCordStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4InputCordStatusEvent.setStatus(
        "current"
    )

st4InputCordActivePowerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 3)
)
st4InputCordActivePowerEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4InputCordID"),
        ("Sentry4-MIB", "st4InputCordName"),
        ("Sentry4-MIB", "st4InputCordActivePower"),
        ("Sentry4-MIB", "st4InputCordActivePowerStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4InputCordActivePowerEvent.setStatus(
        "current"
    )

st4InputCordApparentPowerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 4)
)
st4InputCordApparentPowerEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4InputCordID"),
        ("Sentry4-MIB", "st4InputCordName"),
        ("Sentry4-MIB", "st4InputCordApparentPower"),
        ("Sentry4-MIB", "st4InputCordApparentPowerStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4InputCordApparentPowerEvent.setStatus(
        "current"
    )

st4InputCordPowerFactorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 5)
)
st4InputCordPowerFactorEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4InputCordID"),
        ("Sentry4-MIB", "st4InputCordName"),
        ("Sentry4-MIB", "st4InputCordPowerFactor"),
        ("Sentry4-MIB", "st4InputCordPowerFactorStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4InputCordPowerFactorEvent.setStatus(
        "current"
    )

st4InputCordOutOfBalanceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 6)
)
st4InputCordOutOfBalanceEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4InputCordID"),
        ("Sentry4-MIB", "st4InputCordName"),
        ("Sentry4-MIB", "st4InputCordOutOfBalance"),
        ("Sentry4-MIB", "st4InputCordOutOfBalanceStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4InputCordOutOfBalanceEvent.setStatus(
        "current"
    )

st4LineStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 7)
)
st4LineStatusEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4LineID"),
        ("Sentry4-MIB", "st4LineLabel"),
        ("Sentry4-MIB", "st4LineState"),
        ("Sentry4-MIB", "st4LineStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4LineStatusEvent.setStatus(
        "current"
    )

st4LineCurrentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 8)
)
st4LineCurrentEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4LineID"),
        ("Sentry4-MIB", "st4LineLabel"),
        ("Sentry4-MIB", "st4LineCurrent"),
        ("Sentry4-MIB", "st4LineCurrentStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4LineCurrentEvent.setStatus(
        "current"
    )

st4PhaseStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 9)
)
st4PhaseStatusEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4PhaseID"),
        ("Sentry4-MIB", "st4PhaseLabel"),
        ("Sentry4-MIB", "st4PhaseState"),
        ("Sentry4-MIB", "st4PhaseStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4PhaseStatusEvent.setStatus(
        "current"
    )

st4PhaseVoltageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 10)
)
st4PhaseVoltageEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4PhaseID"),
        ("Sentry4-MIB", "st4PhaseLabel"),
        ("Sentry4-MIB", "st4PhaseVoltage"),
        ("Sentry4-MIB", "st4PhaseVoltageStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4PhaseVoltageEvent.setStatus(
        "current"
    )

st4PhasePowerFactorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 11)
)
st4PhasePowerFactorEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4PhaseID"),
        ("Sentry4-MIB", "st4PhaseLabel"),
        ("Sentry4-MIB", "st4PhasePowerFactor"),
        ("Sentry4-MIB", "st4PhasePowerFactorStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4PhasePowerFactorEvent.setStatus(
        "current"
    )

st4OcpStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 12)
)
st4OcpStatusEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4OcpID"),
        ("Sentry4-MIB", "st4OcpLabel"),
        ("Sentry4-MIB", "st4OcpStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4OcpStatusEvent.setStatus(
        "current"
    )

st4BranchStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 13)
)
st4BranchStatusEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4BranchID"),
        ("Sentry4-MIB", "st4BranchLabel"),
        ("Sentry4-MIB", "st4BranchState"),
        ("Sentry4-MIB", "st4BranchStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4BranchStatusEvent.setStatus(
        "current"
    )

st4BranchCurrentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 14)
)
st4BranchCurrentEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4BranchID"),
        ("Sentry4-MIB", "st4BranchLabel"),
        ("Sentry4-MIB", "st4BranchCurrent"),
        ("Sentry4-MIB", "st4BranchCurrentStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4BranchCurrentEvent.setStatus(
        "current"
    )

st4OutletStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 15)
)
st4OutletStatusEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4OutletID"),
        ("Sentry4-MIB", "st4OutletName"),
        ("Sentry4-MIB", "st4OutletState"),
        ("Sentry4-MIB", "st4OutletStatus"),
        ("Sentry4-MIB", "st4OutletControlState"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4OutletStatusEvent.setStatus(
        "current"
    )

st4OutletStateChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 16)
)
st4OutletStateChangeEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4OutletID"),
        ("Sentry4-MIB", "st4OutletName"),
        ("Sentry4-MIB", "st4OutletState"),
        ("Sentry4-MIB", "st4OutletStatus"),
        ("Sentry4-MIB", "st4OutletControlState"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4OutletStateChangeEvent.setStatus(
        "current"
    )

st4OutletCurrentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 17)
)
st4OutletCurrentEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4OutletID"),
        ("Sentry4-MIB", "st4OutletName"),
        ("Sentry4-MIB", "st4OutletCurrent"),
        ("Sentry4-MIB", "st4OutletCurrentStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4OutletCurrentEvent.setStatus(
        "current"
    )

st4OutletActivePowerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 18)
)
st4OutletActivePowerEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4OutletID"),
        ("Sentry4-MIB", "st4OutletName"),
        ("Sentry4-MIB", "st4OutletActivePower"),
        ("Sentry4-MIB", "st4OutletActivePowerStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4OutletActivePowerEvent.setStatus(
        "current"
    )

st4OutletPowerFactorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 19)
)
st4OutletPowerFactorEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4OutletID"),
        ("Sentry4-MIB", "st4OutletName"),
        ("Sentry4-MIB", "st4OutletPowerFactor"),
        ("Sentry4-MIB", "st4OutletPowerFactorStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4OutletPowerFactorEvent.setStatus(
        "current"
    )

st4TempSensorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 20)
)
st4TempSensorEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4TempSensorID"),
        ("Sentry4-MIB", "st4TempSensorName"),
        ("Sentry4-MIB", "st4TempSensorValue"),
        ("Sentry4-MIB", "st4TempSensorStatus"),
        ("Sentry4-MIB", "st4TempSensorScale"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4TempSensorEvent.setStatus(
        "current"
    )

st4HumidSensorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 21)
)
st4HumidSensorEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4HumidSensorID"),
        ("Sentry4-MIB", "st4HumidSensorName"),
        ("Sentry4-MIB", "st4HumidSensorValue"),
        ("Sentry4-MIB", "st4HumidSensorStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4HumidSensorEvent.setStatus(
        "current"
    )

st4WaterSensorStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 22)
)
st4WaterSensorStatusEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4WaterSensorID"),
        ("Sentry4-MIB", "st4WaterSensorName"),
        ("Sentry4-MIB", "st4WaterSensorStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4WaterSensorStatusEvent.setStatus(
        "current"
    )

st4CcSensorStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 23)
)
st4CcSensorStatusEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4CcSensorID"),
        ("Sentry4-MIB", "st4CcSensorName"),
        ("Sentry4-MIB", "st4CcSensorStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4CcSensorStatusEvent.setStatus(
        "current"
    )

st4AdcSensorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 4, 100, 0, 24)
)
st4AdcSensorEvent.setObjects(
      *(("Sentry4-MIB", "st4SystemLocation"),
        ("Sentry4-MIB", "st4AdcSensorID"),
        ("Sentry4-MIB", "st4AdcSensorName"),
        ("Sentry4-MIB", "st4AdcSensorValue"),
        ("Sentry4-MIB", "st4AdcSensorStatus"),
        ("Sentry4-MIB", "st4EventStatusText"),
        ("Sentry4-MIB", "st4EventStatusCondition"))
)
if mibBuilder.loadTexts:
    st4AdcSensorEvent.setStatus(
        "current"
    )


# Notifications groups

st4EventNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 1, 100)
)
st4EventNotificationsGroup.setObjects(
      *(("Sentry4-MIB", "st4UnitStatusEvent"),
        ("Sentry4-MIB", "st4InputCordStatusEvent"),
        ("Sentry4-MIB", "st4InputCordActivePowerEvent"),
        ("Sentry4-MIB", "st4InputCordApparentPowerEvent"),
        ("Sentry4-MIB", "st4InputCordPowerFactorEvent"),
        ("Sentry4-MIB", "st4InputCordOutOfBalanceEvent"),
        ("Sentry4-MIB", "st4LineStatusEvent"),
        ("Sentry4-MIB", "st4LineCurrentEvent"),
        ("Sentry4-MIB", "st4PhaseStatusEvent"),
        ("Sentry4-MIB", "st4PhaseVoltageEvent"),
        ("Sentry4-MIB", "st4PhasePowerFactorEvent"),
        ("Sentry4-MIB", "st4OcpStatusEvent"),
        ("Sentry4-MIB", "st4BranchStatusEvent"),
        ("Sentry4-MIB", "st4BranchCurrentEvent"),
        ("Sentry4-MIB", "st4OutletStatusEvent"),
        ("Sentry4-MIB", "st4OutletStateChangeEvent"),
        ("Sentry4-MIB", "st4OutletCurrentEvent"),
        ("Sentry4-MIB", "st4OutletActivePowerEvent"),
        ("Sentry4-MIB", "st4OutletPowerFactorEvent"),
        ("Sentry4-MIB", "st4TempSensorEvent"),
        ("Sentry4-MIB", "st4HumidSensorEvent"),
        ("Sentry4-MIB", "st4WaterSensorStatusEvent"),
        ("Sentry4-MIB", "st4CcSensorStatusEvent"),
        ("Sentry4-MIB", "st4AdcSensorEvent"))
)
if mibBuilder.loadTexts:
    st4EventNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

st4ModuleCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1718, 4, 200, 2, 1)
)
if mibBuilder.loadTexts:
    st4ModuleCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Sentry4-MIB",
    **{"DeviceStatus": DeviceStatus,
       "DeviceState": DeviceState,
       "EventNotificationMethods": EventNotificationMethods,
       "serverTech": serverTech,
       "sentry4": sentry4,
       "st4Objects": st4Objects,
       "st4System": st4System,
       "st4SystemConfig": st4SystemConfig,
       "st4SystemProductName": st4SystemProductName,
       "st4SystemLocation": st4SystemLocation,
       "st4SystemFirmwareVersion": st4SystemFirmwareVersion,
       "st4SystemFirmwareBuildInfo": st4SystemFirmwareBuildInfo,
       "st4SystemNICSerialNumber": st4SystemNICSerialNumber,
       "st4SystemNICHardwareInfo": st4SystemNICHardwareInfo,
       "st4SystemProductSeries": st4SystemProductSeries,
       "st4SystemFeatures": st4SystemFeatures,
       "st4SystemFeatureKey": st4SystemFeatureKey,
       "st4SystemConfigModifiedCount": st4SystemConfigModifiedCount,
       "st4SystemUnitCount": st4SystemUnitCount,
       "st4Units": st4Units,
       "st4UnitCommonConfig": st4UnitCommonConfig,
       "st4UnitConfigTable": st4UnitConfigTable,
       "st4UnitConfigEntry": st4UnitConfigEntry,
       "st4UnitIndex": st4UnitIndex,
       "st4UnitID": st4UnitID,
       "st4UnitName": st4UnitName,
       "st4UnitProductSN": st4UnitProductSN,
       "st4UnitModel": st4UnitModel,
       "st4UnitAssetTag": st4UnitAssetTag,
       "st4UnitType": st4UnitType,
       "st4UnitCapabilities": st4UnitCapabilities,
       "st4UnitProductMfrDate": st4UnitProductMfrDate,
       "st4UnitDisplayOrientation": st4UnitDisplayOrientation,
       "st4UnitOutletSequenceOrder": st4UnitOutletSequenceOrder,
       "st4UnitInputCordCount": st4UnitInputCordCount,
       "st4UnitTempSensorCount": st4UnitTempSensorCount,
       "st4UnitHumidSensorCount": st4UnitHumidSensorCount,
       "st4UnitWaterSensorCount": st4UnitWaterSensorCount,
       "st4UnitCcSensorCount": st4UnitCcSensorCount,
       "st4UnitAdcSensorCount": st4UnitAdcSensorCount,
       "st4UnitMonitorTable": st4UnitMonitorTable,
       "st4UnitMonitorEntry": st4UnitMonitorEntry,
       "st4UnitStatus": st4UnitStatus,
       "st4UnitEventConfigTable": st4UnitEventConfigTable,
       "st4UnitEventConfigEntry": st4UnitEventConfigEntry,
       "st4UnitNotifications": st4UnitNotifications,
       "st4InputCords": st4InputCords,
       "st4InputCordCommonConfig": st4InputCordCommonConfig,
       "st4InputCordActivePowerHysteresis": st4InputCordActivePowerHysteresis,
       "st4InputCordApparentPowerHysteresis": st4InputCordApparentPowerHysteresis,
       "st4InputCordPowerFactorHysteresis": st4InputCordPowerFactorHysteresis,
       "st4InputCordOutOfBalanceHysteresis": st4InputCordOutOfBalanceHysteresis,
       "st4InputCordConfigTable": st4InputCordConfigTable,
       "st4InputCordConfigEntry": st4InputCordConfigEntry,
       "st4InputCordIndex": st4InputCordIndex,
       "st4InputCordID": st4InputCordID,
       "st4InputCordName": st4InputCordName,
       "st4InputCordInletType": st4InputCordInletType,
       "st4InputCordNominalVoltage": st4InputCordNominalVoltage,
       "st4InputCordNominalVoltageMin": st4InputCordNominalVoltageMin,
       "st4InputCordNominalVoltageMax": st4InputCordNominalVoltageMax,
       "st4InputCordCurrentCapacity": st4InputCordCurrentCapacity,
       "st4InputCordCurrentCapacityMax": st4InputCordCurrentCapacityMax,
       "st4InputCordPowerCapacity": st4InputCordPowerCapacity,
       "st4InputCordNominalPowerFactor": st4InputCordNominalPowerFactor,
       "st4InputCordLineCount": st4InputCordLineCount,
       "st4InputCordPhaseCount": st4InputCordPhaseCount,
       "st4InputCordOcpCount": st4InputCordOcpCount,
       "st4InputCordBranchCount": st4InputCordBranchCount,
       "st4InputCordOutletCount": st4InputCordOutletCount,
       "st4InputCordMonitorTable": st4InputCordMonitorTable,
       "st4InputCordMonitorEntry": st4InputCordMonitorEntry,
       "st4InputCordState": st4InputCordState,
       "st4InputCordStatus": st4InputCordStatus,
       "st4InputCordActivePower": st4InputCordActivePower,
       "st4InputCordActivePowerStatus": st4InputCordActivePowerStatus,
       "st4InputCordApparentPower": st4InputCordApparentPower,
       "st4InputCordApparentPowerStatus": st4InputCordApparentPowerStatus,
       "st4InputCordPowerUtilized": st4InputCordPowerUtilized,
       "st4InputCordPowerFactor": st4InputCordPowerFactor,
       "st4InputCordPowerFactorStatus": st4InputCordPowerFactorStatus,
       "st4InputCordEnergy": st4InputCordEnergy,
       "st4InputCordFrequency": st4InputCordFrequency,
       "st4InputCordOutOfBalance": st4InputCordOutOfBalance,
       "st4InputCordOutOfBalanceStatus": st4InputCordOutOfBalanceStatus,
       "st4InputCordEventConfigTable": st4InputCordEventConfigTable,
       "st4InputCordEventConfigEntry": st4InputCordEventConfigEntry,
       "st4InputCordNotifications": st4InputCordNotifications,
       "st4InputCordActivePowerLowAlarm": st4InputCordActivePowerLowAlarm,
       "st4InputCordActivePowerLowWarning": st4InputCordActivePowerLowWarning,
       "st4InputCordActivePowerHighWarning": st4InputCordActivePowerHighWarning,
       "st4InputCordActivePowerHighAlarm": st4InputCordActivePowerHighAlarm,
       "st4InputCordApparentPowerLowAlarm": st4InputCordApparentPowerLowAlarm,
       "st4InputCordApparentPowerLowWarning": st4InputCordApparentPowerLowWarning,
       "st4InputCordApparentPowerHighWarning": st4InputCordApparentPowerHighWarning,
       "st4InputCordApparentPowerHighAlarm": st4InputCordApparentPowerHighAlarm,
       "st4InputCordPowerFactorLowAlarm": st4InputCordPowerFactorLowAlarm,
       "st4InputCordPowerFactorLowWarning": st4InputCordPowerFactorLowWarning,
       "st4InputCordOutOfBalanceHighWarning": st4InputCordOutOfBalanceHighWarning,
       "st4InputCordOutOfBalanceHighAlarm": st4InputCordOutOfBalanceHighAlarm,
       "st4Lines": st4Lines,
       "st4LineCommonConfig": st4LineCommonConfig,
       "st4LineCurrentHysteresis": st4LineCurrentHysteresis,
       "st4LineConfigTable": st4LineConfigTable,
       "st4LineConfigEntry": st4LineConfigEntry,
       "st4LineIndex": st4LineIndex,
       "st4LineID": st4LineID,
       "st4LineLabel": st4LineLabel,
       "st4LineCurrentCapacity": st4LineCurrentCapacity,
       "st4LineMonitorTable": st4LineMonitorTable,
       "st4LineMonitorEntry": st4LineMonitorEntry,
       "st4LineState": st4LineState,
       "st4LineStatus": st4LineStatus,
       "st4LineCurrent": st4LineCurrent,
       "st4LineCurrentStatus": st4LineCurrentStatus,
       "st4LineCurrentUtilized": st4LineCurrentUtilized,
       "st4LineEventConfigTable": st4LineEventConfigTable,
       "st4LineEventConfigEntry": st4LineEventConfigEntry,
       "st4LineNotifications": st4LineNotifications,
       "st4LineCurrentLowAlarm": st4LineCurrentLowAlarm,
       "st4LineCurrentLowWarning": st4LineCurrentLowWarning,
       "st4LineCurrentHighWarning": st4LineCurrentHighWarning,
       "st4LineCurrentHighAlarm": st4LineCurrentHighAlarm,
       "st4Phases": st4Phases,
       "st4PhaseCommonConfig": st4PhaseCommonConfig,
       "st4PhaseVoltageHysteresis": st4PhaseVoltageHysteresis,
       "st4PhasePowerFactorHysteresis": st4PhasePowerFactorHysteresis,
       "st4PhaseConfigTable": st4PhaseConfigTable,
       "st4PhaseConfigEntry": st4PhaseConfigEntry,
       "st4PhaseIndex": st4PhaseIndex,
       "st4PhaseID": st4PhaseID,
       "st4PhaseLabel": st4PhaseLabel,
       "st4PhaseNominalVoltage": st4PhaseNominalVoltage,
       "st4PhaseBranchCount": st4PhaseBranchCount,
       "st4PhaseOutletCount": st4PhaseOutletCount,
       "st4PhaseMonitorTable": st4PhaseMonitorTable,
       "st4PhaseMonitorEntry": st4PhaseMonitorEntry,
       "st4PhaseState": st4PhaseState,
       "st4PhaseStatus": st4PhaseStatus,
       "st4PhaseVoltage": st4PhaseVoltage,
       "st4PhaseVoltageStatus": st4PhaseVoltageStatus,
       "st4PhaseVoltageDeviation": st4PhaseVoltageDeviation,
       "st4PhaseCurrent": st4PhaseCurrent,
       "st4PhaseCurrentCrestFactor": st4PhaseCurrentCrestFactor,
       "st4PhaseActivePower": st4PhaseActivePower,
       "st4PhaseApparentPower": st4PhaseApparentPower,
       "st4PhasePowerFactor": st4PhasePowerFactor,
       "st4PhasePowerFactorStatus": st4PhasePowerFactorStatus,
       "st4PhaseReactance": st4PhaseReactance,
       "st4PhaseEnergy": st4PhaseEnergy,
       "st4PhaseEventConfigTable": st4PhaseEventConfigTable,
       "st4PhaseEventConfigEntry": st4PhaseEventConfigEntry,
       "st4PhaseNotifications": st4PhaseNotifications,
       "st4PhaseVoltageLowAlarm": st4PhaseVoltageLowAlarm,
       "st4PhaseVoltageLowWarning": st4PhaseVoltageLowWarning,
       "st4PhaseVoltageHighWarning": st4PhaseVoltageHighWarning,
       "st4PhaseVoltageHighAlarm": st4PhaseVoltageHighAlarm,
       "st4PhasePowerFactorLowAlarm": st4PhasePowerFactorLowAlarm,
       "st4PhasePowerFactorLowWarning": st4PhasePowerFactorLowWarning,
       "st4OverCurrentProtectors": st4OverCurrentProtectors,
       "st4OcpCommonConfig": st4OcpCommonConfig,
       "st4OcpConfigTable": st4OcpConfigTable,
       "st4OcpConfigEntry": st4OcpConfigEntry,
       "st4OcpIndex": st4OcpIndex,
       "st4OcpID": st4OcpID,
       "st4OcpLabel": st4OcpLabel,
       "st4OcpType": st4OcpType,
       "st4OcpCurrentCapacity": st4OcpCurrentCapacity,
       "st4OcpCurrentCapacityMax": st4OcpCurrentCapacityMax,
       "st4OcpBranchCount": st4OcpBranchCount,
       "st4OcpOutletCount": st4OcpOutletCount,
       "st4OcpMonitorTable": st4OcpMonitorTable,
       "st4OcpMonitorEntry": st4OcpMonitorEntry,
       "st4OcpStatus": st4OcpStatus,
       "st4OcpEventConfigTable": st4OcpEventConfigTable,
       "st4OcpEventConfigEntry": st4OcpEventConfigEntry,
       "st4OcpNotifications": st4OcpNotifications,
       "st4Branches": st4Branches,
       "st4BranchCommonConfig": st4BranchCommonConfig,
       "st4BranchCurrentHysteresis": st4BranchCurrentHysteresis,
       "st4BranchConfigTable": st4BranchConfigTable,
       "st4BranchConfigEntry": st4BranchConfigEntry,
       "st4BranchIndex": st4BranchIndex,
       "st4BranchID": st4BranchID,
       "st4BranchLabel": st4BranchLabel,
       "st4BranchCurrentCapacity": st4BranchCurrentCapacity,
       "st4BranchPhaseID": st4BranchPhaseID,
       "st4BranchOcpID": st4BranchOcpID,
       "st4BranchOutletCount": st4BranchOutletCount,
       "st4BranchMonitorTable": st4BranchMonitorTable,
       "st4BranchMonitorEntry": st4BranchMonitorEntry,
       "st4BranchState": st4BranchState,
       "st4BranchStatus": st4BranchStatus,
       "st4BranchCurrent": st4BranchCurrent,
       "st4BranchCurrentStatus": st4BranchCurrentStatus,
       "st4BranchCurrentUtilized": st4BranchCurrentUtilized,
       "st4BranchEventConfigTable": st4BranchEventConfigTable,
       "st4BranchEventConfigEntry": st4BranchEventConfigEntry,
       "st4BranchNotifications": st4BranchNotifications,
       "st4BranchCurrentLowAlarm": st4BranchCurrentLowAlarm,
       "st4BranchCurrentLowWarning": st4BranchCurrentLowWarning,
       "st4BranchCurrentHighWarning": st4BranchCurrentHighWarning,
       "st4BranchCurrentHighAlarm": st4BranchCurrentHighAlarm,
       "st4Outlets": st4Outlets,
       "st4OutletCommonConfig": st4OutletCommonConfig,
       "st4OutletCurrentHysteresis": st4OutletCurrentHysteresis,
       "st4OutletActivePowerHysteresis": st4OutletActivePowerHysteresis,
       "st4OutletPowerFactorHysteresis": st4OutletPowerFactorHysteresis,
       "st4OutletSequenceInterval": st4OutletSequenceInterval,
       "st4OutletRebootDelay": st4OutletRebootDelay,
       "st4OutletStateChangeLogging": st4OutletStateChangeLogging,
       "st4OutletConfigTable": st4OutletConfigTable,
       "st4OutletConfigEntry": st4OutletConfigEntry,
       "st4OutletIndex": st4OutletIndex,
       "st4OutletID": st4OutletID,
       "st4OutletName": st4OutletName,
       "st4OutletCapabilities": st4OutletCapabilities,
       "st4OutletSocketType": st4OutletSocketType,
       "st4OutletCurrentCapacity": st4OutletCurrentCapacity,
       "st4OutletPowerCapacity": st4OutletPowerCapacity,
       "st4OutletWakeupState": st4OutletWakeupState,
       "st4OutletPostOnDelay": st4OutletPostOnDelay,
       "st4OutletPhaseID": st4OutletPhaseID,
       "st4OutletOcpID": st4OutletOcpID,
       "st4OutletBranchID": st4OutletBranchID,
       "st4OutletMonitorTable": st4OutletMonitorTable,
       "st4OutletMonitorEntry": st4OutletMonitorEntry,
       "st4OutletState": st4OutletState,
       "st4OutletStatus": st4OutletStatus,
       "st4OutletCurrent": st4OutletCurrent,
       "st4OutletCurrentStatus": st4OutletCurrentStatus,
       "st4OutletCurrentUtilized": st4OutletCurrentUtilized,
       "st4OutletVoltage": st4OutletVoltage,
       "st4OutletActivePower": st4OutletActivePower,
       "st4OutletActivePowerStatus": st4OutletActivePowerStatus,
       "st4OutletApparentPower": st4OutletApparentPower,
       "st4OutletPowerFactor": st4OutletPowerFactor,
       "st4OutletPowerFactorStatus": st4OutletPowerFactorStatus,
       "st4OutletCurrentCrestFactor": st4OutletCurrentCrestFactor,
       "st4OutletReactance": st4OutletReactance,
       "st4OutletEnergy": st4OutletEnergy,
       "st4OutletEventConfigTable": st4OutletEventConfigTable,
       "st4OutletEventConfigEntry": st4OutletEventConfigEntry,
       "st4OutletNotifications": st4OutletNotifications,
       "st4OutletCurrentLowAlarm": st4OutletCurrentLowAlarm,
       "st4OutletCurrentLowWarning": st4OutletCurrentLowWarning,
       "st4OutletCurrentHighWarning": st4OutletCurrentHighWarning,
       "st4OutletCurrentHighAlarm": st4OutletCurrentHighAlarm,
       "st4OutletActivePowerLowAlarm": st4OutletActivePowerLowAlarm,
       "st4OutletActivePowerLowWarning": st4OutletActivePowerLowWarning,
       "st4OutletActivePowerHighWarning": st4OutletActivePowerHighWarning,
       "st4OutletActivePowerHighAlarm": st4OutletActivePowerHighAlarm,
       "st4OutletPowerFactorLowAlarm": st4OutletPowerFactorLowAlarm,
       "st4OutletPowerFactorLowWarning": st4OutletPowerFactorLowWarning,
       "st4OutletControlTable": st4OutletControlTable,
       "st4OutletControlEntry": st4OutletControlEntry,
       "st4OutletControlState": st4OutletControlState,
       "st4OutletControlAction": st4OutletControlAction,
       "st4OutletCommonControl": st4OutletCommonControl,
       "st4OutletQueueControl": st4OutletQueueControl,
       "st4TemperatureSensors": st4TemperatureSensors,
       "st4TempSensorCommonConfig": st4TempSensorCommonConfig,
       "st4TempSensorHysteresis": st4TempSensorHysteresis,
       "st4TempSensorScale": st4TempSensorScale,
       "st4TempSensorConfigTable": st4TempSensorConfigTable,
       "st4TempSensorConfigEntry": st4TempSensorConfigEntry,
       "st4TempSensorIndex": st4TempSensorIndex,
       "st4TempSensorID": st4TempSensorID,
       "st4TempSensorName": st4TempSensorName,
       "st4TempSensorValueMin": st4TempSensorValueMin,
       "st4TempSensorValueMax": st4TempSensorValueMax,
       "st4TempSensorMonitorTable": st4TempSensorMonitorTable,
       "st4TempSensorMonitorEntry": st4TempSensorMonitorEntry,
       "st4TempSensorValue": st4TempSensorValue,
       "st4TempSensorStatus": st4TempSensorStatus,
       "st4TempSensorEventConfigTable": st4TempSensorEventConfigTable,
       "st4TempSensorEventConfigEntry": st4TempSensorEventConfigEntry,
       "st4TempSensorNotifications": st4TempSensorNotifications,
       "st4TempSensorLowAlarm": st4TempSensorLowAlarm,
       "st4TempSensorLowWarning": st4TempSensorLowWarning,
       "st4TempSensorHighWarning": st4TempSensorHighWarning,
       "st4TempSensorHighAlarm": st4TempSensorHighAlarm,
       "st4HumiditySensors": st4HumiditySensors,
       "st4HumidSensorCommonConfig": st4HumidSensorCommonConfig,
       "st4HumidSensorHysteresis": st4HumidSensorHysteresis,
       "st4HumidSensorConfigTable": st4HumidSensorConfigTable,
       "st4HumidSensorConfigEntry": st4HumidSensorConfigEntry,
       "st4HumidSensorIndex": st4HumidSensorIndex,
       "st4HumidSensorID": st4HumidSensorID,
       "st4HumidSensorName": st4HumidSensorName,
       "st4HumidSensorMonitorTable": st4HumidSensorMonitorTable,
       "st4HumidSensorMonitorEntry": st4HumidSensorMonitorEntry,
       "st4HumidSensorValue": st4HumidSensorValue,
       "st4HumidSensorStatus": st4HumidSensorStatus,
       "st4HumidSensorEventConfigTable": st4HumidSensorEventConfigTable,
       "st4HumidSensorEventConfigEntry": st4HumidSensorEventConfigEntry,
       "st4HumidSensorNotifications": st4HumidSensorNotifications,
       "st4HumidSensorLowAlarm": st4HumidSensorLowAlarm,
       "st4HumidSensorLowWarning": st4HumidSensorLowWarning,
       "st4HumidSensorHighWarning": st4HumidSensorHighWarning,
       "st4HumidSensorHighAlarm": st4HumidSensorHighAlarm,
       "st4WaterSensors": st4WaterSensors,
       "st4WaterSensorCommonConfig": st4WaterSensorCommonConfig,
       "st4WaterSensorConfigTable": st4WaterSensorConfigTable,
       "st4WaterSensorConfigEntry": st4WaterSensorConfigEntry,
       "st4WaterSensorIndex": st4WaterSensorIndex,
       "st4WaterSensorID": st4WaterSensorID,
       "st4WaterSensorName": st4WaterSensorName,
       "st4WaterSensorMonitorTable": st4WaterSensorMonitorTable,
       "st4WaterSensorMonitorEntry": st4WaterSensorMonitorEntry,
       "st4WaterSensorStatus": st4WaterSensorStatus,
       "st4WaterSensorEventConfigTable": st4WaterSensorEventConfigTable,
       "st4WaterSensorEventConfigEntry": st4WaterSensorEventConfigEntry,
       "st4WaterSensorNotifications": st4WaterSensorNotifications,
       "st4ContactClosureSensors": st4ContactClosureSensors,
       "st4CcSensorCommonConfig": st4CcSensorCommonConfig,
       "st4CcSensorConfigTable": st4CcSensorConfigTable,
       "st4CcSensorConfigEntry": st4CcSensorConfigEntry,
       "st4CcSensorIndex": st4CcSensorIndex,
       "st4CcSensorID": st4CcSensorID,
       "st4CcSensorName": st4CcSensorName,
       "st4CcSensorMonitorTable": st4CcSensorMonitorTable,
       "st4CcSensorMonitorEntry": st4CcSensorMonitorEntry,
       "st4CcSensorStatus": st4CcSensorStatus,
       "st4CcSensorEventConfigTable": st4CcSensorEventConfigTable,
       "st4CcSensorEventConfigEntry": st4CcSensorEventConfigEntry,
       "st4CcSensorNotifications": st4CcSensorNotifications,
       "st4AnalogToDigitalConvSensors": st4AnalogToDigitalConvSensors,
       "st4AdcSensorCommonConfig": st4AdcSensorCommonConfig,
       "st4AdcSensorHysteresis": st4AdcSensorHysteresis,
       "st4AdcSensorConfigTable": st4AdcSensorConfigTable,
       "st4AdcSensorConfigEntry": st4AdcSensorConfigEntry,
       "st4AdcSensorIndex": st4AdcSensorIndex,
       "st4AdcSensorID": st4AdcSensorID,
       "st4AdcSensorName": st4AdcSensorName,
       "st4AdcSensorMonitorTable": st4AdcSensorMonitorTable,
       "st4AdcSensorMonitorEntry": st4AdcSensorMonitorEntry,
       "st4AdcSensorValue": st4AdcSensorValue,
       "st4AdcSensorStatus": st4AdcSensorStatus,
       "st4AdcSensorEventConfigTable": st4AdcSensorEventConfigTable,
       "st4AdcSensorEventConfigEntry": st4AdcSensorEventConfigEntry,
       "st4AdcSensorNotifications": st4AdcSensorNotifications,
       "st4AdcSensorLowAlarm": st4AdcSensorLowAlarm,
       "st4AdcSensorLowWarning": st4AdcSensorLowWarning,
       "st4AdcSensorHighWarning": st4AdcSensorHighWarning,
       "st4AdcSensorHighAlarm": st4AdcSensorHighAlarm,
       "st4EventInformation": st4EventInformation,
       "st4EventStatusText": st4EventStatusText,
       "st4EventStatusCondition": st4EventStatusCondition,
       "st4Notifications": st4Notifications,
       "st4Events": st4Events,
       "st4UnitStatusEvent": st4UnitStatusEvent,
       "st4InputCordStatusEvent": st4InputCordStatusEvent,
       "st4InputCordActivePowerEvent": st4InputCordActivePowerEvent,
       "st4InputCordApparentPowerEvent": st4InputCordApparentPowerEvent,
       "st4InputCordPowerFactorEvent": st4InputCordPowerFactorEvent,
       "st4InputCordOutOfBalanceEvent": st4InputCordOutOfBalanceEvent,
       "st4LineStatusEvent": st4LineStatusEvent,
       "st4LineCurrentEvent": st4LineCurrentEvent,
       "st4PhaseStatusEvent": st4PhaseStatusEvent,
       "st4PhaseVoltageEvent": st4PhaseVoltageEvent,
       "st4PhasePowerFactorEvent": st4PhasePowerFactorEvent,
       "st4OcpStatusEvent": st4OcpStatusEvent,
       "st4BranchStatusEvent": st4BranchStatusEvent,
       "st4BranchCurrentEvent": st4BranchCurrentEvent,
       "st4OutletStatusEvent": st4OutletStatusEvent,
       "st4OutletStateChangeEvent": st4OutletStateChangeEvent,
       "st4OutletCurrentEvent": st4OutletCurrentEvent,
       "st4OutletActivePowerEvent": st4OutletActivePowerEvent,
       "st4OutletPowerFactorEvent": st4OutletPowerFactorEvent,
       "st4TempSensorEvent": st4TempSensorEvent,
       "st4HumidSensorEvent": st4HumidSensorEvent,
       "st4WaterSensorStatusEvent": st4WaterSensorStatusEvent,
       "st4CcSensorStatusEvent": st4CcSensorStatusEvent,
       "st4AdcSensorEvent": st4AdcSensorEvent,
       "st4Conformance": st4Conformance,
       "st4Groups": st4Groups,
       "st4SystemObjectsGroup": st4SystemObjectsGroup,
       "st4UnitObjectsGroup": st4UnitObjectsGroup,
       "st4InputCordObjectsGroup": st4InputCordObjectsGroup,
       "st4LineObjectsGroup": st4LineObjectsGroup,
       "st4PhaseObjectsGroup": st4PhaseObjectsGroup,
       "st4OcpObjectsGroup": st4OcpObjectsGroup,
       "st4BranchObjectsGroup": st4BranchObjectsGroup,
       "st4OutletObjectsGroup": st4OutletObjectsGroup,
       "st4TempSensorObjectsGroup": st4TempSensorObjectsGroup,
       "st4HumidSensorObjectsGroup": st4HumidSensorObjectsGroup,
       "st4WaterSensorObjectsGroup": st4WaterSensorObjectsGroup,
       "st4CcSensorObjectsGroup": st4CcSensorObjectsGroup,
       "st4AdcSensorObjectsGroup": st4AdcSensorObjectsGroup,
       "st4EventInfoObjectsGroup": st4EventInfoObjectsGroup,
       "st4EventNotificationsGroup": st4EventNotificationsGroup,
       "st4Compliances": st4Compliances,
       "st4ModuleCompliances": st4ModuleCompliances}
)
