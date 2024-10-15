# SNMP MIB module (MY-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:29 2024
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

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

mySystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1)
)
mySystemMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MySystemMIBObjects_ObjectIdentity = ObjectIdentity
mySystemMIBObjects = _MySystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1)
)


class _MySystemHwVersion_Type(DisplayString):
    """Custom type mySystemHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MySystemHwVersion_Type.__name__ = "DisplayString"
_MySystemHwVersion_Object = MibScalar
mySystemHwVersion = _MySystemHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 1),
    _MySystemHwVersion_Type()
)
mySystemHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemHwVersion.setStatus("current")


class _MySystemSwVersion_Type(DisplayString):
    """Custom type mySystemSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MySystemSwVersion_Type.__name__ = "DisplayString"
_MySystemSwVersion_Object = MibScalar
mySystemSwVersion = _MySystemSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 2),
    _MySystemSwVersion_Type()
)
mySystemSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemSwVersion.setStatus("current")


class _MySystemBootVersion_Type(DisplayString):
    """Custom type mySystemBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MySystemBootVersion_Type.__name__ = "DisplayString"
_MySystemBootVersion_Object = MibScalar
mySystemBootVersion = _MySystemBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 3),
    _MySystemBootVersion_Type()
)
mySystemBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemBootVersion.setStatus("current")


class _MySystemSysCtrlVersion_Type(DisplayString):
    """Custom type mySystemSysCtrlVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MySystemSysCtrlVersion_Type.__name__ = "DisplayString"
_MySystemSysCtrlVersion_Object = MibScalar
mySystemSysCtrlVersion = _MySystemSysCtrlVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 4),
    _MySystemSysCtrlVersion_Type()
)
mySystemSysCtrlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemSysCtrlVersion.setStatus("current")
_MySystemParametersSave_Type = Integer32
_MySystemParametersSave_Object = MibScalar
mySystemParametersSave = _MySystemParametersSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 5),
    _MySystemParametersSave_Type()
)
mySystemParametersSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySystemParametersSave.setStatus("current")


class _MySystemOutBandRate_Type(Integer32):
    """Custom type mySystemOutBandRate based on Integer32"""
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
        *(("baud115200", 5),
          ("baud19200", 2),
          ("baud38400", 3),
          ("baud57600", 4),
          ("baud9600", 1))
    )


_MySystemOutBandRate_Type.__name__ = "Integer32"
_MySystemOutBandRate_Object = MibScalar
mySystemOutBandRate = _MySystemOutBandRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 6),
    _MySystemOutBandRate_Type()
)
mySystemOutBandRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySystemOutBandRate.setStatus("current")
_MySystemReset_Type = Integer32
_MySystemReset_Object = MibScalar
mySystemReset = _MySystemReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 7),
    _MySystemReset_Type()
)
mySystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySystemReset.setStatus("current")


class _MySwitchLayer_Type(Integer32):
    """Custom type mySwitchLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2),
          ("router", 3))
    )


_MySwitchLayer_Type.__name__ = "Integer32"
_MySwitchLayer_Object = MibScalar
mySwitchLayer = _MySwitchLayer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 8),
    _MySwitchLayer_Type()
)
mySwitchLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySwitchLayer.setStatus("current")


class _MySystemHwPower_Type(Integer32):
    """Custom type mySystemHwPower based on Integer32"""
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
        *(("rpsLinkAndNoPower", 2),
          ("rpsLinkAndPower", 4),
          ("rpsLinkAndReadyForPower", 3),
          ("rpsNoLink", 1))
    )


_MySystemHwPower_Type.__name__ = "Integer32"
_MySystemHwPower_Object = MibScalar
mySystemHwPower = _MySystemHwPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 9),
    _MySystemHwPower_Type()
)
mySystemHwPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemHwPower.setStatus("current")


class _MySystemHwFan_Type(Integer32):
    """Custom type mySystemHwFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 2),
          ("work", 1))
    )


_MySystemHwFan_Type.__name__ = "Integer32"
_MySystemHwFan_Object = MibScalar
mySystemHwFan = _MySystemHwFan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 10),
    _MySystemHwFan_Type()
)
mySystemHwFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemHwFan.setStatus("current")


class _MySystemOutBandTimeout_Type(Integer32):
    """Custom type mySystemOutBandTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MySystemOutBandTimeout_Type.__name__ = "Integer32"
_MySystemOutBandTimeout_Object = MibScalar
mySystemOutBandTimeout = _MySystemOutBandTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 11),
    _MySystemOutBandTimeout_Type()
)
mySystemOutBandTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySystemOutBandTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    mySystemOutBandTimeout.setUnits("seconds")


class _MySystemTelnetTimeout_Type(Integer32):
    """Custom type mySystemTelnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MySystemTelnetTimeout_Type.__name__ = "Integer32"
_MySystemTelnetTimeout_Object = MibScalar
mySystemTelnetTimeout = _MySystemTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 12),
    _MySystemTelnetTimeout_Type()
)
mySystemTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySystemTelnetTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    mySystemTelnetTimeout.setUnits("seconds")


class _MySystemMainFile_Type(DisplayString):
    """Custom type mySystemMainFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MySystemMainFile_Type.__name__ = "DisplayString"
_MySystemMainFile_Object = MibScalar
mySystemMainFile = _MySystemMainFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 13),
    _MySystemMainFile_Type()
)
mySystemMainFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemMainFile.setStatus("current")
_MySystemCurrentPower_Type = Integer32
_MySystemCurrentPower_Object = MibScalar
mySystemCurrentPower = _MySystemCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 14),
    _MySystemCurrentPower_Type()
)
mySystemCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemCurrentPower.setStatus("current")
_MySystemRemainPower_Type = Integer32
_MySystemRemainPower_Object = MibScalar
mySystemRemainPower = _MySystemRemainPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 15),
    _MySystemRemainPower_Type()
)
mySystemRemainPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemRemainPower.setStatus("current")
_MySystemTemperature_Type = Integer32
_MySystemTemperature_Object = MibScalar
mySystemTemperature = _MySystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 16),
    _MySystemTemperature_Type()
)
mySystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemTemperature.setStatus("current")
_MySystemElectricalSourceNum_Type = Integer32
_MySystemElectricalSourceNum_Object = MibScalar
mySystemElectricalSourceNum = _MySystemElectricalSourceNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 17),
    _MySystemElectricalSourceNum_Type()
)
mySystemElectricalSourceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemElectricalSourceNum.setStatus("current")
_MySystemElectricalSourceIsNormalTable_Object = MibTable
mySystemElectricalSourceIsNormalTable = _MySystemElectricalSourceIsNormalTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 18)
)
if mibBuilder.loadTexts:
    mySystemElectricalSourceIsNormalTable.setStatus("current")
_MySystemElectricalSourceIsNormalEntry_Object = MibTableRow
mySystemElectricalSourceIsNormalEntry = _MySystemElectricalSourceIsNormalEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 18, 1)
)
mySystemElectricalSourceIsNormalEntry.setIndexNames(
    (0, "MY-SYSTEM-MIB", "mySystemElectricalSourceIsNormalIndex"),
)
if mibBuilder.loadTexts:
    mySystemElectricalSourceIsNormalEntry.setStatus("current")
_MySystemElectricalSourceIsNormalIndex_Type = Integer32
_MySystemElectricalSourceIsNormalIndex_Object = MibTableColumn
mySystemElectricalSourceIsNormalIndex = _MySystemElectricalSourceIsNormalIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 18, 1, 1),
    _MySystemElectricalSourceIsNormalIndex_Type()
)
mySystemElectricalSourceIsNormalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemElectricalSourceIsNormalIndex.setStatus("current")


class _MySystemElectricalSourceIsNormal_Type(Integer32):
    """Custom type mySystemElectricalSourceIsNormal based on Integer32"""
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
        *(("existnopower", 2),
          ("existreadypower", 3),
          ("noexist", 1),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6))
    )


_MySystemElectricalSourceIsNormal_Type.__name__ = "Integer32"
_MySystemElectricalSourceIsNormal_Object = MibTableColumn
mySystemElectricalSourceIsNormal = _MySystemElectricalSourceIsNormal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 18, 1, 2),
    _MySystemElectricalSourceIsNormal_Type()
)
mySystemElectricalSourceIsNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemElectricalSourceIsNormal.setStatus("current")
_MySystemElectricalSourceName_Type = DisplayString
_MySystemElectricalSourceName_Object = MibTableColumn
mySystemElectricalSourceName = _MySystemElectricalSourceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 18, 1, 3),
    _MySystemElectricalSourceName_Type()
)
mySystemElectricalSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemElectricalSourceName.setStatus("current")
_MySystemCurrentVoltage_Type = Integer32
_MySystemCurrentVoltage_Object = MibScalar
mySystemCurrentVoltage = _MySystemCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 19),
    _MySystemCurrentVoltage_Type()
)
mySystemCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemCurrentVoltage.setStatus("current")
_MySystemFanNUM_Type = Integer32
_MySystemFanNUM_Object = MibScalar
mySystemFanNUM = _MySystemFanNUM_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 20),
    _MySystemFanNUM_Type()
)
mySystemFanNUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemFanNUM.setStatus("current")
_MySystemFanIsNormalTable_Object = MibTable
mySystemFanIsNormalTable = _MySystemFanIsNormalTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 21)
)
if mibBuilder.loadTexts:
    mySystemFanIsNormalTable.setStatus("current")
_MySystemFanIsNormalEntry_Object = MibTableRow
mySystemFanIsNormalEntry = _MySystemFanIsNormalEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 21, 1)
)
mySystemFanIsNormalEntry.setIndexNames(
    (0, "MY-SYSTEM-MIB", "mySystemFanIsNormalIndex"),
)
if mibBuilder.loadTexts:
    mySystemFanIsNormalEntry.setStatus("current")
_MySystemFanIsNormalIndex_Type = Integer32
_MySystemFanIsNormalIndex_Object = MibTableColumn
mySystemFanIsNormalIndex = _MySystemFanIsNormalIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 21, 1, 1),
    _MySystemFanIsNormalIndex_Type()
)
mySystemFanIsNormalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemFanIsNormalIndex.setStatus("current")


class _MySystemFanIsNormal_Type(Integer32):
    """Custom type mySystemFanIsNormal based on Integer32"""
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
        *(("existnopower", 2),
          ("existreadypower", 3),
          ("noexist", 1),
          ("normal", 4),
          ("powerbutabnormal", 5),
          ("unknow", 6))
    )


_MySystemFanIsNormal_Type.__name__ = "Integer32"
_MySystemFanIsNormal_Object = MibTableColumn
mySystemFanIsNormal = _MySystemFanIsNormal_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 21, 1, 2),
    _MySystemFanIsNormal_Type()
)
mySystemFanIsNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemFanIsNormal.setStatus("current")
_MySystemFanName_Type = DisplayString
_MySystemFanName_Object = MibTableColumn
mySystemFanName = _MySystemFanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 21, 1, 3),
    _MySystemFanName_Type()
)
mySystemFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemFanName.setStatus("current")
_MySystemReloadTimeRemain_Type = Integer32
_MySystemReloadTimeRemain_Object = MibScalar
mySystemReloadTimeRemain = _MySystemReloadTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 22),
    _MySystemReloadTimeRemain_Type()
)
mySystemReloadTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemReloadTimeRemain.setStatus("current")
_MySystemTemperatureTable_Object = MibTable
mySystemTemperatureTable = _MySystemTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 23)
)
if mibBuilder.loadTexts:
    mySystemTemperatureTable.setStatus("current")
_MySystemTemperatureEntry_Object = MibTableRow
mySystemTemperatureEntry = _MySystemTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 23, 1)
)
mySystemTemperatureEntry.setIndexNames(
    (0, "MY-SYSTEM-MIB", "mySystemTemperatureIndex"),
)
if mibBuilder.loadTexts:
    mySystemTemperatureEntry.setStatus("current")
_MySystemTemperatureIndex_Type = Integer32
_MySystemTemperatureIndex_Object = MibTableColumn
mySystemTemperatureIndex = _MySystemTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 23, 1, 1),
    _MySystemTemperatureIndex_Type()
)
mySystemTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemTemperatureIndex.setStatus("current")
_MySystemTemperatureName_Type = DisplayString
_MySystemTemperatureName_Object = MibTableColumn
mySystemTemperatureName = _MySystemTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 23, 1, 2),
    _MySystemTemperatureName_Type()
)
mySystemTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemTemperatureName.setStatus("current")
_MySystemTemperatureCurrent_Type = Integer32
_MySystemTemperatureCurrent_Object = MibTableColumn
mySystemTemperatureCurrent = _MySystemTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 23, 1, 3),
    _MySystemTemperatureCurrent_Type()
)
mySystemTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemTemperatureCurrent.setStatus("current")
_MySystemTemperatureWarningVaule_Type = Integer32
_MySystemTemperatureWarningVaule_Object = MibTableColumn
mySystemTemperatureWarningVaule = _MySystemTemperatureWarningVaule_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 23, 1, 4),
    _MySystemTemperatureWarningVaule_Type()
)
mySystemTemperatureWarningVaule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySystemTemperatureWarningVaule.setStatus("current")
_MySystemTemperatureCritialVaule_Type = Integer32
_MySystemTemperatureCritialVaule_Object = MibTableColumn
mySystemTemperatureCritialVaule = _MySystemTemperatureCritialVaule_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 23, 1, 5),
    _MySystemTemperatureCritialVaule_Type()
)
mySystemTemperatureCritialVaule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySystemTemperatureCritialVaule.setStatus("current")
_MySystemSerialno_Type = DisplayString
_MySystemSerialno_Object = MibScalar
mySystemSerialno = _MySystemSerialno_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 24),
    _MySystemSerialno_Type()
)
mySystemSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemSerialno.setStatus("current")
_MySystemVersionTable_Object = MibTable
mySystemVersionTable = _MySystemVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 25)
)
if mibBuilder.loadTexts:
    mySystemVersionTable.setStatus("current")
_MySystemVersionEntry_Object = MibTableRow
mySystemVersionEntry = _MySystemVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 25, 1)
)
mySystemVersionEntry.setIndexNames(
    (0, "MY-SYSTEM-MIB", "mySystemVersionIndex"),
)
if mibBuilder.loadTexts:
    mySystemVersionEntry.setStatus("current")
_MySystemVersionIndex_Type = Unsigned32
_MySystemVersionIndex_Object = MibTableColumn
mySystemVersionIndex = _MySystemVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 25, 1, 1),
    _MySystemVersionIndex_Type()
)
mySystemVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemVersionIndex.setStatus("current")
_MySystemVersionName_Type = DisplayString
_MySystemVersionName_Object = MibTableColumn
mySystemVersionName = _MySystemVersionName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 25, 1, 2),
    _MySystemVersionName_Type()
)
mySystemVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemVersionName.setStatus("current")
_MySystemVersionSwBoot_Type = DisplayString
_MySystemVersionSwBoot_Object = MibTableColumn
mySystemVersionSwBoot = _MySystemVersionSwBoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 25, 1, 3),
    _MySystemVersionSwBoot_Type()
)
mySystemVersionSwBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemVersionSwBoot.setStatus("current")
_MySystemVersionSwCtrl_Type = DisplayString
_MySystemVersionSwCtrl_Object = MibTableColumn
mySystemVersionSwCtrl = _MySystemVersionSwCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 25, 1, 4),
    _MySystemVersionSwCtrl_Type()
)
mySystemVersionSwCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemVersionSwCtrl.setStatus("current")
_MySystemVersionSwMain_Type = DisplayString
_MySystemVersionSwMain_Object = MibTableColumn
mySystemVersionSwMain = _MySystemVersionSwMain_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 25, 1, 5),
    _MySystemVersionSwMain_Type()
)
mySystemVersionSwMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemVersionSwMain.setStatus("current")
_MySystemVersionHw_Type = DisplayString
_MySystemVersionHw_Object = MibTableColumn
mySystemVersionHw = _MySystemVersionHw_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 25, 1, 6),
    _MySystemVersionHw_Type()
)
mySystemVersionHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemVersionHw.setStatus("current")
_MySystemVersionSerialno_Type = DisplayString
_MySystemVersionSerialno_Object = MibTableColumn
mySystemVersionSerialno = _MySystemVersionSerialno_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 1, 25, 1, 7),
    _MySystemVersionSerialno_Type()
)
mySystemVersionSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemVersionSerialno.setStatus("current")
_MySystemMIBTraps_ObjectIdentity = ObjectIdentity
mySystemMIBTraps = _MySystemMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 2)
)
_MySystemHardChangeDesc_Type = DisplayString
_MySystemHardChangeDesc_Object = MibScalar
mySystemHardChangeDesc = _MySystemHardChangeDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 2, 1),
    _MySystemHardChangeDesc_Type()
)
mySystemHardChangeDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySystemHardChangeDesc.setStatus("current")
_MySystemMIBConformance_ObjectIdentity = ObjectIdentity
mySystemMIBConformance = _MySystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 3)
)
_MySystemMIBCompliances_ObjectIdentity = ObjectIdentity
mySystemMIBCompliances = _MySystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 3, 1)
)
_MySystemMIBGroups_ObjectIdentity = ObjectIdentity
mySystemMIBGroups = _MySystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 3, 2)
)

# Managed Objects groups

mySystemMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 3, 2, 1)
)
mySystemMIBGroup.setObjects(
      *(("MY-SYSTEM-MIB", "mySystemHwVersion"),
        ("MY-SYSTEM-MIB", "mySystemSwVersion"),
        ("MY-SYSTEM-MIB", "mySystemBootVersion"),
        ("MY-SYSTEM-MIB", "mySystemSysCtrlVersion"),
        ("MY-SYSTEM-MIB", "mySystemParametersSave"),
        ("MY-SYSTEM-MIB", "mySystemReset"),
        ("MY-SYSTEM-MIB", "mySystemOutBandRate"),
        ("MY-SYSTEM-MIB", "mySwitchLayer"))
)
if mibBuilder.loadTexts:
    mySystemMIBGroup.setStatus("current")


# Notification objects

mySystemHardChangeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 2, 2)
)
mySystemHardChangeDetected.setObjects(
    ("MY-SYSTEM-MIB", "mySystemHardChangeDesc")
)
if mibBuilder.loadTexts:
    mySystemHardChangeDetected.setStatus(
        "current"
    )

mySystemPowerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 2, 3)
)
mySystemPowerStateChange.setObjects(
    ("MY-SYSTEM-MIB", "mySystemHwPower")
)
if mibBuilder.loadTexts:
    mySystemPowerStateChange.setStatus(
        "current"
    )

mySystemFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 2, 4)
)
mySystemFanStateChange.setObjects(
    ("MY-SYSTEM-MIB", "mySystemHwFan")
)
if mibBuilder.loadTexts:
    mySystemFanStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

mySystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mySystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-SYSTEM-MIB",
    **{"mySystemMIB": mySystemMIB,
       "mySystemMIBObjects": mySystemMIBObjects,
       "mySystemHwVersion": mySystemHwVersion,
       "mySystemSwVersion": mySystemSwVersion,
       "mySystemBootVersion": mySystemBootVersion,
       "mySystemSysCtrlVersion": mySystemSysCtrlVersion,
       "mySystemParametersSave": mySystemParametersSave,
       "mySystemOutBandRate": mySystemOutBandRate,
       "mySystemReset": mySystemReset,
       "mySwitchLayer": mySwitchLayer,
       "mySystemHwPower": mySystemHwPower,
       "mySystemHwFan": mySystemHwFan,
       "mySystemOutBandTimeout": mySystemOutBandTimeout,
       "mySystemTelnetTimeout": mySystemTelnetTimeout,
       "mySystemMainFile": mySystemMainFile,
       "mySystemCurrentPower": mySystemCurrentPower,
       "mySystemRemainPower": mySystemRemainPower,
       "mySystemTemperature": mySystemTemperature,
       "mySystemElectricalSourceNum": mySystemElectricalSourceNum,
       "mySystemElectricalSourceIsNormalTable": mySystemElectricalSourceIsNormalTable,
       "mySystemElectricalSourceIsNormalEntry": mySystemElectricalSourceIsNormalEntry,
       "mySystemElectricalSourceIsNormalIndex": mySystemElectricalSourceIsNormalIndex,
       "mySystemElectricalSourceIsNormal": mySystemElectricalSourceIsNormal,
       "mySystemElectricalSourceName": mySystemElectricalSourceName,
       "mySystemCurrentVoltage": mySystemCurrentVoltage,
       "mySystemFanNUM": mySystemFanNUM,
       "mySystemFanIsNormalTable": mySystemFanIsNormalTable,
       "mySystemFanIsNormalEntry": mySystemFanIsNormalEntry,
       "mySystemFanIsNormalIndex": mySystemFanIsNormalIndex,
       "mySystemFanIsNormal": mySystemFanIsNormal,
       "mySystemFanName": mySystemFanName,
       "mySystemReloadTimeRemain": mySystemReloadTimeRemain,
       "mySystemTemperatureTable": mySystemTemperatureTable,
       "mySystemTemperatureEntry": mySystemTemperatureEntry,
       "mySystemTemperatureIndex": mySystemTemperatureIndex,
       "mySystemTemperatureName": mySystemTemperatureName,
       "mySystemTemperatureCurrent": mySystemTemperatureCurrent,
       "mySystemTemperatureWarningVaule": mySystemTemperatureWarningVaule,
       "mySystemTemperatureCritialVaule": mySystemTemperatureCritialVaule,
       "mySystemSerialno": mySystemSerialno,
       "mySystemVersionTable": mySystemVersionTable,
       "mySystemVersionEntry": mySystemVersionEntry,
       "mySystemVersionIndex": mySystemVersionIndex,
       "mySystemVersionName": mySystemVersionName,
       "mySystemVersionSwBoot": mySystemVersionSwBoot,
       "mySystemVersionSwCtrl": mySystemVersionSwCtrl,
       "mySystemVersionSwMain": mySystemVersionSwMain,
       "mySystemVersionHw": mySystemVersionHw,
       "mySystemVersionSerialno": mySystemVersionSerialno,
       "mySystemMIBTraps": mySystemMIBTraps,
       "mySystemHardChangeDesc": mySystemHardChangeDesc,
       "mySystemHardChangeDetected": mySystemHardChangeDetected,
       "mySystemPowerStateChange": mySystemPowerStateChange,
       "mySystemFanStateChange": mySystemFanStateChange,
       "mySystemMIBConformance": mySystemMIBConformance,
       "mySystemMIBCompliances": mySystemMIBCompliances,
       "mySystemMIBCompliance": mySystemMIBCompliance,
       "mySystemMIBGroups": mySystemMIBGroups,
       "mySystemMIBGroup": mySystemMIBGroup}
)
