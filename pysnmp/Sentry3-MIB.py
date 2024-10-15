# SNMP MIB module (Sentry3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Sentry3-MIB
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

sentry3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 3)
)
sentry3.setRevisions(
        ("2016-01-25 16:30",
         "2014-06-25 12:00",
         "2014-01-16 18:00",
         "2013-11-25 09:00",
         "2013-09-16 10:00",
         "2013-02-14 09:30",
         "2012-11-07 14:00",
         "2012-04-18 14:00",
         "2012-01-04 11:00",
         "2011-07-11 16:40",
         "2011-06-15 13:00",
         "2011-05-05 11:00",
         "2010-07-07 12:15",
         "2009-03-10 16:00",
         "2008-05-07 15:20",
         "2007-07-09 14:45",
         "2007-01-09 14:10",
         "2006-07-20 12:00",
         "2006-06-12 09:30",
         "2005-07-27 11:05",
         "2005-02-18 11:45",
         "2005-01-07 12:20",
         "2004-12-09 13:20",
         "2004-11-11 12:00",
         "2003-11-20 13:00",
         "2003-10-23 19:00",
         "2003-10-02 11:00",
         "2003-08-27 16:00",
         "2003-03-28 17:00",
         "2003-03-27 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ServerTech_ObjectIdentity = ObjectIdentity
serverTech = _ServerTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718)
)
_SystemGroup_ObjectIdentity = ObjectIdentity
systemGroup = _SystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1)
)


class _SystemVersion_Type(DisplayString):
    """Custom type systemVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SystemVersion_Type.__name__ = "DisplayString"
_SystemVersion_Object = MibScalar
systemVersion = _SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 1),
    _SystemVersion_Type()
)
systemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVersion.setStatus("current")


class _SystemNICSerialNumber_Type(DisplayString):
    """Custom type systemNICSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SystemNICSerialNumber_Type.__name__ = "DisplayString"
_SystemNICSerialNumber_Object = MibScalar
systemNICSerialNumber = _SystemNICSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 2),
    _SystemNICSerialNumber_Type()
)
systemNICSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNICSerialNumber.setStatus("current")


class _SystemLocation_Type(DisplayString):
    """Custom type systemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemLocation_Type.__name__ = "DisplayString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 3),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")


class _SystemTowerCount_Type(Integer32):
    """Custom type systemTowerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SystemTowerCount_Type.__name__ = "Integer32"
_SystemTowerCount_Object = MibScalar
systemTowerCount = _SystemTowerCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 4),
    _SystemTowerCount_Type()
)
systemTowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTowerCount.setStatus("current")


class _SystemEnvMonCount_Type(Integer32):
    """Custom type systemEnvMonCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SystemEnvMonCount_Type.__name__ = "Integer32"
_SystemEnvMonCount_Object = MibScalar
systemEnvMonCount = _SystemEnvMonCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 5),
    _SystemEnvMonCount_Type()
)
systemEnvMonCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEnvMonCount.setStatus("current")


class _SystemTotalPower_Type(Integer32):
    """Custom type systemTotalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_SystemTotalPower_Type.__name__ = "Integer32"
_SystemTotalPower_Object = MibScalar
systemTotalPower = _SystemTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 6),
    _SystemTotalPower_Type()
)
systemTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    systemTotalPower.setUnits("Watts")


class _SystemArea_Type(Integer32):
    """Custom type systemArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SystemArea_Type.__name__ = "Integer32"
_SystemArea_Object = MibScalar
systemArea = _SystemArea_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 7),
    _SystemArea_Type()
)
systemArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemArea.setStatus("current")
if mibBuilder.loadTexts:
    systemArea.setUnits("tenth area units")


class _SystemWattsPerAreaUnit_Type(Integer32):
    """Custom type systemWattsPerAreaUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1500000),
    )


_SystemWattsPerAreaUnit_Type.__name__ = "Integer32"
_SystemWattsPerAreaUnit_Object = MibScalar
systemWattsPerAreaUnit = _SystemWattsPerAreaUnit_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 8),
    _SystemWattsPerAreaUnit_Type()
)
systemWattsPerAreaUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemWattsPerAreaUnit.setStatus("current")
if mibBuilder.loadTexts:
    systemWattsPerAreaUnit.setUnits("Watts per area unit")


class _SystemAreaUnit_Type(Integer32):
    """Custom type systemAreaUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("squareFoot", 1),
          ("squareMeter", 0))
    )


_SystemAreaUnit_Type.__name__ = "Integer32"
_SystemAreaUnit_Object = MibScalar
systemAreaUnit = _SystemAreaUnit_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 9),
    _SystemAreaUnit_Type()
)
systemAreaUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAreaUnit.setStatus("current")


class _SystemPowerFactor_Type(Integer32):
    """Custom type systemPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100),
    )


_SystemPowerFactor_Type.__name__ = "Integer32"
_SystemPowerFactor_Object = MibScalar
systemPowerFactor = _SystemPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 10),
    _SystemPowerFactor_Type()
)
systemPowerFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    systemPowerFactor.setUnits("hundredths")


class _SystemFeatures_Type(Bits):
    """Custom type systemFeatures based on Bits"""
    namedValues = NamedValues(
        *(("outletControlInhibit", 2),
          ("smartLoadShedding", 0),
          ("snmpPOPS", 1))
    )

_SystemFeatures_Type.__name__ = "Bits"
_SystemFeatures_Object = MibScalar
systemFeatures = _SystemFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 11),
    _SystemFeatures_Type()
)
systemFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFeatures.setStatus("current")


class _SystemFeatureKey_Type(DisplayString):
    """Custom type systemFeatureKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_SystemFeatureKey_Type.__name__ = "DisplayString"
_SystemFeatureKey_Object = MibScalar
systemFeatureKey = _SystemFeatureKey_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 12),
    _SystemFeatureKey_Type()
)
systemFeatureKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemFeatureKey.setStatus("current")


class _SystemOutletSeqInterval_Type(Integer32):
    """Custom type systemOutletSeqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SystemOutletSeqInterval_Type.__name__ = "Integer32"
_SystemOutletSeqInterval_Object = MibScalar
systemOutletSeqInterval = _SystemOutletSeqInterval_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 13),
    _SystemOutletSeqInterval_Type()
)
systemOutletSeqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOutletSeqInterval.setStatus("current")
if mibBuilder.loadTexts:
    systemOutletSeqInterval.setUnits("seconds")


class _SystemOutletRebootDelay_Type(Integer32):
    """Custom type systemOutletRebootDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_SystemOutletRebootDelay_Type.__name__ = "Integer32"
_SystemOutletRebootDelay_Object = MibScalar
systemOutletRebootDelay = _SystemOutletRebootDelay_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 14),
    _SystemOutletRebootDelay_Type()
)
systemOutletRebootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOutletRebootDelay.setStatus("current")
if mibBuilder.loadTexts:
    systemOutletRebootDelay.setUnits("seconds")


class _SystemConfigModifiedCount_Type(Integer32):
    """Custom type systemConfigModifiedCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SystemConfigModifiedCount_Type.__name__ = "Integer32"
_SystemConfigModifiedCount_Object = MibScalar
systemConfigModifiedCount = _SystemConfigModifiedCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 1, 15),
    _SystemConfigModifiedCount_Type()
)
systemConfigModifiedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemConfigModifiedCount.setStatus("current")
_SystemTables_ObjectIdentity = ObjectIdentity
systemTables = _SystemTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2)
)
_TowerTable_Object = MibTable
towerTable = _TowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1)
)
if mibBuilder.loadTexts:
    towerTable.setStatus("current")
_TowerEntry_Object = MibTableRow
towerEntry = _TowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1)
)
towerEntry.setIndexNames(
    (0, "Sentry3-MIB", "towerIndex"),
)
if mibBuilder.loadTexts:
    towerEntry.setStatus("current")


class _TowerIndex_Type(Integer32):
    """Custom type towerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TowerIndex_Type.__name__ = "Integer32"
_TowerIndex_Object = MibTableColumn
towerIndex = _TowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 1),
    _TowerIndex_Type()
)
towerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    towerIndex.setStatus("current")


class _TowerID_Type(DisplayString):
    """Custom type towerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TowerID_Type.__name__ = "DisplayString"
_TowerID_Object = MibTableColumn
towerID = _TowerID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 2),
    _TowerID_Type()
)
towerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerID.setStatus("current")


class _TowerName_Type(DisplayString):
    """Custom type towerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_TowerName_Type.__name__ = "DisplayString"
_TowerName_Object = MibTableColumn
towerName = _TowerName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 3),
    _TowerName_Type()
)
towerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    towerName.setStatus("current")


class _TowerStatus_Type(Integer32):
    """Custom type towerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fanFail", 2),
          ("noComm", 1),
          ("normal", 0),
          ("nvmFail", 4),
          ("outOfBalance", 5),
          ("overTemp", 3))
    )


_TowerStatus_Type.__name__ = "Integer32"
_TowerStatus_Object = MibTableColumn
towerStatus = _TowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 4),
    _TowerStatus_Type()
)
towerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerStatus.setStatus("current")


class _TowerInfeedCount_Type(Integer32):
    """Custom type towerInfeedCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TowerInfeedCount_Type.__name__ = "Integer32"
_TowerInfeedCount_Object = MibTableColumn
towerInfeedCount = _TowerInfeedCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 5),
    _TowerInfeedCount_Type()
)
towerInfeedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerInfeedCount.setStatus("current")


class _TowerProductSN_Type(DisplayString):
    """Custom type towerProductSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TowerProductSN_Type.__name__ = "DisplayString"
_TowerProductSN_Object = MibTableColumn
towerProductSN = _TowerProductSN_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 6),
    _TowerProductSN_Type()
)
towerProductSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerProductSN.setStatus("current")


class _TowerModelNumber_Type(DisplayString):
    """Custom type towerModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_TowerModelNumber_Type.__name__ = "DisplayString"
_TowerModelNumber_Object = MibTableColumn
towerModelNumber = _TowerModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 7),
    _TowerModelNumber_Type()
)
towerModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerModelNumber.setStatus("current")


class _TowerCapabilities_Type(Bits):
    """Custom type towerCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("directCurrent", 2),
          ("failSafe", 0),
          ("fanSense", 4),
          ("fuseSense", 1),
          ("tempSense", 5),
          ("threePhase", 3))
    )

_TowerCapabilities_Type.__name__ = "Bits"
_TowerCapabilities_Object = MibTableColumn
towerCapabilities = _TowerCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 8),
    _TowerCapabilities_Type()
)
towerCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerCapabilities.setStatus("current")


class _TowerVACapacity_Type(Integer32):
    """Custom type towerVACapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 50000),
    )


_TowerVACapacity_Type.__name__ = "Integer32"
_TowerVACapacity_Object = MibTableColumn
towerVACapacity = _TowerVACapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 9),
    _TowerVACapacity_Type()
)
towerVACapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerVACapacity.setStatus("current")
if mibBuilder.loadTexts:
    towerVACapacity.setUnits("Volt-Amps")


class _TowerVACapacityUsed_Type(Integer32):
    """Custom type towerVACapacityUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1500),
    )


_TowerVACapacityUsed_Type.__name__ = "Integer32"
_TowerVACapacityUsed_Object = MibTableColumn
towerVACapacityUsed = _TowerVACapacityUsed_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 10),
    _TowerVACapacityUsed_Type()
)
towerVACapacityUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerVACapacityUsed.setStatus("current")
if mibBuilder.loadTexts:
    towerVACapacityUsed.setUnits("tenth percentage")


class _TowerActivePower_Type(Integer32):
    """Custom type towerActivePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 50000),
    )


_TowerActivePower_Type.__name__ = "Integer32"
_TowerActivePower_Object = MibTableColumn
towerActivePower = _TowerActivePower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 11),
    _TowerActivePower_Type()
)
towerActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerActivePower.setStatus("current")
if mibBuilder.loadTexts:
    towerActivePower.setUnits("Watts")


class _TowerApparentPower_Type(Integer32):
    """Custom type towerApparentPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 50000),
    )


_TowerApparentPower_Type.__name__ = "Integer32"
_TowerApparentPower_Object = MibTableColumn
towerApparentPower = _TowerApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 12),
    _TowerApparentPower_Type()
)
towerApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    towerApparentPower.setUnits("Volt-Amps")


class _TowerPowerFactor_Type(Integer32):
    """Custom type towerPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_TowerPowerFactor_Type.__name__ = "Integer32"
_TowerPowerFactor_Object = MibTableColumn
towerPowerFactor = _TowerPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 13),
    _TowerPowerFactor_Type()
)
towerPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    towerPowerFactor.setUnits("hundredths")


class _TowerEnergy_Type(Integer32):
    """Custom type towerEnergy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_TowerEnergy_Type.__name__ = "Integer32"
_TowerEnergy_Object = MibTableColumn
towerEnergy = _TowerEnergy_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 14),
    _TowerEnergy_Type()
)
towerEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerEnergy.setStatus("current")
if mibBuilder.loadTexts:
    towerEnergy.setUnits("Kilowatt-Hours")


class _TowerLineFrequency_Type(Integer32):
    """Custom type towerLineFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 60),
    )


_TowerLineFrequency_Type.__name__ = "Integer32"
_TowerLineFrequency_Object = MibTableColumn
towerLineFrequency = _TowerLineFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 1, 1, 15),
    _TowerLineFrequency_Type()
)
towerLineFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    towerLineFrequency.setStatus("current")
if mibBuilder.loadTexts:
    towerLineFrequency.setUnits("Hertz")
_InfeedTable_Object = MibTable
infeedTable = _InfeedTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2)
)
if mibBuilder.loadTexts:
    infeedTable.setStatus("current")
_InfeedEntry_Object = MibTableRow
infeedEntry = _InfeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1)
)
infeedEntry.setIndexNames(
    (0, "Sentry3-MIB", "towerIndex"),
    (0, "Sentry3-MIB", "infeedIndex"),
)
if mibBuilder.loadTexts:
    infeedEntry.setStatus("current")


class _InfeedIndex_Type(Integer32):
    """Custom type infeedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_InfeedIndex_Type.__name__ = "Integer32"
_InfeedIndex_Object = MibTableColumn
infeedIndex = _InfeedIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 1),
    _InfeedIndex_Type()
)
infeedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infeedIndex.setStatus("current")


class _InfeedID_Type(DisplayString):
    """Custom type infeedID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_InfeedID_Type.__name__ = "DisplayString"
_InfeedID_Object = MibTableColumn
infeedID = _InfeedID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 2),
    _InfeedID_Type()
)
infeedID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedID.setStatus("current")


class _InfeedName_Type(DisplayString):
    """Custom type infeedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_InfeedName_Type.__name__ = "DisplayString"
_InfeedName_Object = MibTableColumn
infeedName = _InfeedName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 3),
    _InfeedName_Type()
)
infeedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infeedName.setStatus("current")


class _InfeedCapabilities_Type(Bits):
    """Custom type infeedCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("branchLoadSense", 8),
          ("branchOnSense", 7),
          ("defaultOff", 4),
          ("failSafe", 3),
          ("loadSense", 1),
          ("onSense", 0),
          ("powerControl", 2),
          ("powerSense", 6),
          ("voltageSense", 5))
    )

_InfeedCapabilities_Type.__name__ = "Bits"
_InfeedCapabilities_Object = MibTableColumn
infeedCapabilities = _InfeedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 4),
    _InfeedCapabilities_Type()
)
infeedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedCapabilities.setStatus("current")


class _InfeedStatus_Type(Integer32):
    """Custom type infeedStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noComm", 6),
          ("off", 0),
          ("offError", 4),
          ("offFuse", 8),
          ("offWait", 2),
          ("on", 1),
          ("onError", 5),
          ("onFuse", 9),
          ("onWait", 3),
          ("reading", 7))
    )


_InfeedStatus_Type.__name__ = "Integer32"
_InfeedStatus_Object = MibTableColumn
infeedStatus = _InfeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 5),
    _InfeedStatus_Type()
)
infeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedStatus.setStatus("current")


class _InfeedLoadStatus_Type(Integer32):
    """Custom type infeedLoadStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("loadHigh", 4),
          ("loadLow", 3),
          ("noComm", 7),
          ("normal", 0),
          ("notOn", 1),
          ("overLoad", 5),
          ("readError", 6),
          ("reading", 2))
    )


_InfeedLoadStatus_Type.__name__ = "Integer32"
_InfeedLoadStatus_Object = MibTableColumn
infeedLoadStatus = _InfeedLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 6),
    _InfeedLoadStatus_Type()
)
infeedLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedLoadStatus.setStatus("current")


class _InfeedLoadValue_Type(Integer32):
    """Custom type infeedLoadValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 60000),
    )


_InfeedLoadValue_Type.__name__ = "Integer32"
_InfeedLoadValue_Object = MibTableColumn
infeedLoadValue = _InfeedLoadValue_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 7),
    _InfeedLoadValue_Type()
)
infeedLoadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedLoadValue.setStatus("current")
if mibBuilder.loadTexts:
    infeedLoadValue.setUnits("hundredth Amps")


class _InfeedLoadHighThresh_Type(Integer32):
    """Custom type infeedLoadHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InfeedLoadHighThresh_Type.__name__ = "Integer32"
_InfeedLoadHighThresh_Object = MibTableColumn
infeedLoadHighThresh = _InfeedLoadHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 8),
    _InfeedLoadHighThresh_Type()
)
infeedLoadHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infeedLoadHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    infeedLoadHighThresh.setUnits("Amps")


class _InfeedOutletCount_Type(Integer32):
    """Custom type infeedOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_InfeedOutletCount_Type.__name__ = "Integer32"
_InfeedOutletCount_Object = MibTableColumn
infeedOutletCount = _InfeedOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 9),
    _InfeedOutletCount_Type()
)
infeedOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedOutletCount.setStatus("current")


class _InfeedCapacity_Type(Integer32):
    """Custom type infeedCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_InfeedCapacity_Type.__name__ = "Integer32"
_InfeedCapacity_Object = MibTableColumn
infeedCapacity = _InfeedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 10),
    _InfeedCapacity_Type()
)
infeedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    infeedCapacity.setUnits("Amps")


class _InfeedVoltage_Type(Integer32):
    """Custom type infeedVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4800),
    )


_InfeedVoltage_Type.__name__ = "Integer32"
_InfeedVoltage_Object = MibTableColumn
infeedVoltage = _InfeedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 11),
    _InfeedVoltage_Type()
)
infeedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedVoltage.setStatus("current")
if mibBuilder.loadTexts:
    infeedVoltage.setUnits("tenth Volts")


class _InfeedPower_Type(Integer32):
    """Custom type infeedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25000),
    )


_InfeedPower_Type.__name__ = "Integer32"
_InfeedPower_Object = MibTableColumn
infeedPower = _InfeedPower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 12),
    _InfeedPower_Type()
)
infeedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedPower.setStatus("current")
if mibBuilder.loadTexts:
    infeedPower.setUnits("Watts")


class _InfeedApparentPower_Type(Integer32):
    """Custom type infeedApparentPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25000),
    )


_InfeedApparentPower_Type.__name__ = "Integer32"
_InfeedApparentPower_Object = MibTableColumn
infeedApparentPower = _InfeedApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 13),
    _InfeedApparentPower_Type()
)
infeedApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    infeedApparentPower.setUnits("Volt-Amps")


class _InfeedPowerFactor_Type(Integer32):
    """Custom type infeedPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_InfeedPowerFactor_Type.__name__ = "Integer32"
_InfeedPowerFactor_Object = MibTableColumn
infeedPowerFactor = _InfeedPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 14),
    _InfeedPowerFactor_Type()
)
infeedPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    infeedPowerFactor.setUnits("hundredths")


class _InfeedCrestFactor_Type(Integer32):
    """Custom type infeedCrestFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_InfeedCrestFactor_Type.__name__ = "Integer32"
_InfeedCrestFactor_Object = MibTableColumn
infeedCrestFactor = _InfeedCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 15),
    _InfeedCrestFactor_Type()
)
infeedCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedCrestFactor.setStatus("current")
if mibBuilder.loadTexts:
    infeedCrestFactor.setUnits("tenths")


class _InfeedEnergy_Type(Integer32):
    """Custom type infeedEnergy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_InfeedEnergy_Type.__name__ = "Integer32"
_InfeedEnergy_Object = MibTableColumn
infeedEnergy = _InfeedEnergy_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 16),
    _InfeedEnergy_Type()
)
infeedEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedEnergy.setStatus("current")
if mibBuilder.loadTexts:
    infeedEnergy.setUnits("tenth Kilowatt-Hours")


class _InfeedReactance_Type(Integer32):
    """Custom type infeedReactance based on Integer32"""
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


_InfeedReactance_Type.__name__ = "Integer32"
_InfeedReactance_Object = MibTableColumn
infeedReactance = _InfeedReactance_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 17),
    _InfeedReactance_Type()
)
infeedReactance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedReactance.setStatus("current")


class _InfeedPhaseVoltage_Type(Integer32):
    """Custom type infeedPhaseVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2640),
    )


_InfeedPhaseVoltage_Type.__name__ = "Integer32"
_InfeedPhaseVoltage_Object = MibTableColumn
infeedPhaseVoltage = _InfeedPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 18),
    _InfeedPhaseVoltage_Type()
)
infeedPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    infeedPhaseVoltage.setUnits("tenth Volts")


class _InfeedPhaseCurrent_Type(Integer32):
    """Custom type infeedPhaseCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25500),
    )


_InfeedPhaseCurrent_Type.__name__ = "Integer32"
_InfeedPhaseCurrent_Object = MibTableColumn
infeedPhaseCurrent = _InfeedPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 19),
    _InfeedPhaseCurrent_Type()
)
infeedPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    infeedPhaseCurrent.setUnits("hundredth Amps")


class _InfeedCapacityUsed_Type(Integer32):
    """Custom type infeedCapacityUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1500),
    )


_InfeedCapacityUsed_Type.__name__ = "Integer32"
_InfeedCapacityUsed_Object = MibTableColumn
infeedCapacityUsed = _InfeedCapacityUsed_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 20),
    _InfeedCapacityUsed_Type()
)
infeedCapacityUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedCapacityUsed.setStatus("current")
if mibBuilder.loadTexts:
    infeedCapacityUsed.setUnits("tenth percentage")


class _InfeedLineID_Type(DisplayString):
    """Custom type infeedLineID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_InfeedLineID_Type.__name__ = "DisplayString"
_InfeedLineID_Object = MibTableColumn
infeedLineID = _InfeedLineID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 21),
    _InfeedLineID_Type()
)
infeedLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedLineID.setStatus("current")


class _InfeedLineToLineID_Type(DisplayString):
    """Custom type infeedLineToLineID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_InfeedLineToLineID_Type.__name__ = "DisplayString"
_InfeedLineToLineID_Object = MibTableColumn
infeedLineToLineID = _InfeedLineToLineID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 22),
    _InfeedLineToLineID_Type()
)
infeedLineToLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedLineToLineID.setStatus("current")


class _InfeedPhaseID_Type(DisplayString):
    """Custom type infeedPhaseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_InfeedPhaseID_Type.__name__ = "DisplayString"
_InfeedPhaseID_Object = MibTableColumn
infeedPhaseID = _InfeedPhaseID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 23),
    _InfeedPhaseID_Type()
)
infeedPhaseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedPhaseID.setStatus("current")


class _InfeedVACapacity_Type(Integer32):
    """Custom type infeedVACapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25000),
    )


_InfeedVACapacity_Type.__name__ = "Integer32"
_InfeedVACapacity_Object = MibTableColumn
infeedVACapacity = _InfeedVACapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 24),
    _InfeedVACapacity_Type()
)
infeedVACapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedVACapacity.setStatus("current")
if mibBuilder.loadTexts:
    infeedVACapacity.setUnits("Volt-Amps")


class _InfeedVACapacityUsed_Type(Integer32):
    """Custom type infeedVACapacityUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1500),
    )


_InfeedVACapacityUsed_Type.__name__ = "Integer32"
_InfeedVACapacityUsed_Object = MibTableColumn
infeedVACapacityUsed = _InfeedVACapacityUsed_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 2, 1, 25),
    _InfeedVACapacityUsed_Type()
)
infeedVACapacityUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infeedVACapacityUsed.setStatus("current")
if mibBuilder.loadTexts:
    infeedVACapacityUsed.setUnits("tenth percentage")
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1)
)
outletEntry.setIndexNames(
    (0, "Sentry3-MIB", "towerIndex"),
    (0, "Sentry3-MIB", "infeedIndex"),
    (0, "Sentry3-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletEntry.setStatus("current")


class _OutletIndex_Type(Integer32):
    """Custom type outletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_OutletIndex_Type.__name__ = "Integer32"
_OutletIndex_Object = MibTableColumn
outletIndex = _OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 1),
    _OutletIndex_Type()
)
outletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletIndex.setStatus("current")


class _OutletID_Type(DisplayString):
    """Custom type outletID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_OutletID_Type.__name__ = "DisplayString"
_OutletID_Object = MibTableColumn
outletID = _OutletID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 2),
    _OutletID_Type()
)
outletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletID.setStatus("current")


class _OutletName_Type(DisplayString):
    """Custom type outletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_OutletName_Type.__name__ = "DisplayString"
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 3),
    _OutletName_Type()
)
outletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletName.setStatus("current")


class _OutletCapabilities_Type(Bits):
    """Custom type outletCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("defaultOn", 4),
          ("fusedBranch", 6),
          ("loadSense", 1),
          ("onSense", 0),
          ("ownInfeed", 5),
          ("powerControl", 2),
          ("powerSense", 8),
          ("shutdown", 3),
          ("voltageSense", 7))
    )

_OutletCapabilities_Type.__name__ = "Bits"
_OutletCapabilities_Object = MibTableColumn
outletCapabilities = _OutletCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 4),
    _OutletCapabilities_Type()
)
outletCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCapabilities.setStatus("current")


class _OutletStatus_Type(Integer32):
    """Custom type outletStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noComm", 6),
          ("off", 0),
          ("offError", 4),
          ("offFuse", 8),
          ("offWait", 2),
          ("on", 1),
          ("onError", 5),
          ("onFuse", 9),
          ("onWait", 3),
          ("reading", 7))
    )


_OutletStatus_Type.__name__ = "Integer32"
_OutletStatus_Object = MibTableColumn
outletStatus = _OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 5),
    _OutletStatus_Type()
)
outletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletStatus.setStatus("current")


class _OutletLoadStatus_Type(Integer32):
    """Custom type outletLoadStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("loadHigh", 4),
          ("loadLow", 3),
          ("noComm", 7),
          ("normal", 0),
          ("notOn", 1),
          ("overLoad", 5),
          ("readError", 6),
          ("reading", 2))
    )


_OutletLoadStatus_Type.__name__ = "Integer32"
_OutletLoadStatus_Object = MibTableColumn
outletLoadStatus = _OutletLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 6),
    _OutletLoadStatus_Type()
)
outletLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletLoadStatus.setStatus("current")


class _OutletLoadValue_Type(Integer32):
    """Custom type outletLoadValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25500),
    )


_OutletLoadValue_Type.__name__ = "Integer32"
_OutletLoadValue_Object = MibTableColumn
outletLoadValue = _OutletLoadValue_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 7),
    _OutletLoadValue_Type()
)
outletLoadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletLoadValue.setStatus("current")
if mibBuilder.loadTexts:
    outletLoadValue.setUnits("hundredth Amps")


class _OutletLoadLowThresh_Type(Integer32):
    """Custom type outletLoadLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OutletLoadLowThresh_Type.__name__ = "Integer32"
_OutletLoadLowThresh_Object = MibTableColumn
outletLoadLowThresh = _OutletLoadLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 8),
    _OutletLoadLowThresh_Type()
)
outletLoadLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletLoadLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    outletLoadLowThresh.setUnits("Amps")


class _OutletLoadHighThresh_Type(Integer32):
    """Custom type outletLoadHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OutletLoadHighThresh_Type.__name__ = "Integer32"
_OutletLoadHighThresh_Object = MibTableColumn
outletLoadHighThresh = _OutletLoadHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 9),
    _OutletLoadHighThresh_Type()
)
outletLoadHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletLoadHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    outletLoadHighThresh.setUnits("Amps")


class _OutletControlState_Type(Integer32):
    """Custom type outletControlState based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("eventOff", 14),
          ("eventOn", 15),
          ("eventReboot", 16),
          ("eventShutdown", 17),
          ("idleOff", 0),
          ("idleOn", 1),
          ("lockedOff", 6),
          ("lockedOn", 7),
          ("minimumOff", 12),
          ("minimumOn", 13),
          ("off", 4),
          ("on", 5),
          ("pendOff", 11),
          ("pendOn", 10),
          ("reboot", 8),
          ("shutdown", 9),
          ("wakeOff", 2),
          ("wakeOn", 3))
    )


_OutletControlState_Type.__name__ = "Integer32"
_OutletControlState_Object = MibTableColumn
outletControlState = _OutletControlState_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 10),
    _OutletControlState_Type()
)
outletControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletControlState.setStatus("current")


class _OutletControlAction_Type(Integer32):
    """Custom type outletControlAction based on Integer32"""
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
        *(("none", 0),
          ("off", 2),
          ("on", 1),
          ("reboot", 3))
    )


_OutletControlAction_Type.__name__ = "Integer32"
_OutletControlAction_Object = MibTableColumn
outletControlAction = _OutletControlAction_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 11),
    _OutletControlAction_Type()
)
outletControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlAction.setStatus("current")


class _OutletCapacity_Type(Integer32):
    """Custom type outletCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_OutletCapacity_Type.__name__ = "Integer32"
_OutletCapacity_Object = MibTableColumn
outletCapacity = _OutletCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 12),
    _OutletCapacity_Type()
)
outletCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCapacity.setStatus("current")
if mibBuilder.loadTexts:
    outletCapacity.setUnits("Amps")


class _OutletVoltage_Type(Integer32):
    """Custom type outletVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2640),
    )


_OutletVoltage_Type.__name__ = "Integer32"
_OutletVoltage_Object = MibTableColumn
outletVoltage = _OutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 13),
    _OutletVoltage_Type()
)
outletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletVoltage.setStatus("current")
if mibBuilder.loadTexts:
    outletVoltage.setUnits("tenth Volts")


class _OutletPower_Type(Integer32):
    """Custom type outletPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_OutletPower_Type.__name__ = "Integer32"
_OutletPower_Object = MibTableColumn
outletPower = _OutletPower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 14),
    _OutletPower_Type()
)
outletPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPower.setStatus("current")
if mibBuilder.loadTexts:
    outletPower.setUnits("Watts")


class _OutletApparentPower_Type(Integer32):
    """Custom type outletApparentPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_OutletApparentPower_Type.__name__ = "Integer32"
_OutletApparentPower_Object = MibTableColumn
outletApparentPower = _OutletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 15),
    _OutletApparentPower_Type()
)
outletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    outletApparentPower.setUnits("Volt-Amps")


class _OutletPowerFactor_Type(Integer32):
    """Custom type outletPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_OutletPowerFactor_Type.__name__ = "Integer32"
_OutletPowerFactor_Object = MibTableColumn
outletPowerFactor = _OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 16),
    _OutletPowerFactor_Type()
)
outletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    outletPowerFactor.setUnits("hundredths")


class _OutletCrestFactor_Type(Integer32):
    """Custom type outletCrestFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_OutletCrestFactor_Type.__name__ = "Integer32"
_OutletCrestFactor_Object = MibTableColumn
outletCrestFactor = _OutletCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 17),
    _OutletCrestFactor_Type()
)
outletCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCrestFactor.setStatus("current")
if mibBuilder.loadTexts:
    outletCrestFactor.setUnits("tenths")


class _OutletEnergy_Type(Integer32):
    """Custom type outletEnergy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_OutletEnergy_Type.__name__ = "Integer32"
_OutletEnergy_Object = MibTableColumn
outletEnergy = _OutletEnergy_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 18),
    _OutletEnergy_Type()
)
outletEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletEnergy.setStatus("current")
if mibBuilder.loadTexts:
    outletEnergy.setUnits("Watt-Hours")


class _OutletWakeupState_Type(Integer32):
    """Custom type outletWakeupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("last", 1),
          ("off", 2),
          ("on", 3))
    )


_OutletWakeupState_Type.__name__ = "Integer32"
_OutletWakeupState_Object = MibTableColumn
outletWakeupState = _OutletWakeupState_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 19),
    _OutletWakeupState_Type()
)
outletWakeupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletWakeupState.setStatus("current")


class _OutletPostOnDelay_Type(Integer32):
    """Custom type outletPostOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_OutletPostOnDelay_Type.__name__ = "Integer32"
_OutletPostOnDelay_Object = MibTableColumn
outletPostOnDelay = _OutletPostOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 3, 1, 20),
    _OutletPostOnDelay_Type()
)
outletPostOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPostOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    outletPostOnDelay.setUnits("seconds")
_EnvMonTable_Object = MibTable
envMonTable = _EnvMonTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4)
)
if mibBuilder.loadTexts:
    envMonTable.setStatus("current")
_EnvMonEntry_Object = MibTableRow
envMonEntry = _EnvMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1)
)
envMonEntry.setIndexNames(
    (0, "Sentry3-MIB", "envMonIndex"),
)
if mibBuilder.loadTexts:
    envMonEntry.setStatus("current")


class _EnvMonIndex_Type(Integer32):
    """Custom type envMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_EnvMonIndex_Type.__name__ = "Integer32"
_EnvMonIndex_Object = MibTableColumn
envMonIndex = _EnvMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 1),
    _EnvMonIndex_Type()
)
envMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    envMonIndex.setStatus("current")


class _EnvMonID_Type(DisplayString):
    """Custom type envMonID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_EnvMonID_Type.__name__ = "DisplayString"
_EnvMonID_Object = MibTableColumn
envMonID = _EnvMonID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 2),
    _EnvMonID_Type()
)
envMonID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonID.setStatus("current")


class _EnvMonName_Type(DisplayString):
    """Custom type envMonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_EnvMonName_Type.__name__ = "DisplayString"
_EnvMonName_Object = MibTableColumn
envMonName = _EnvMonName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 3),
    _EnvMonName_Type()
)
envMonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envMonName.setStatus("current")


class _EnvMonStatus_Type(Integer32):
    """Custom type envMonStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noComm", 1),
          ("normal", 0))
    )


_EnvMonStatus_Type.__name__ = "Integer32"
_EnvMonStatus_Object = MibTableColumn
envMonStatus = _EnvMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 4),
    _EnvMonStatus_Type()
)
envMonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonStatus.setStatus("current")


class _EnvMonWaterSensorName_Type(DisplayString):
    """Custom type envMonWaterSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_EnvMonWaterSensorName_Type.__name__ = "DisplayString"
_EnvMonWaterSensorName_Object = MibTableColumn
envMonWaterSensorName = _EnvMonWaterSensorName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 5),
    _EnvMonWaterSensorName_Type()
)
envMonWaterSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envMonWaterSensorName.setStatus("current")


class _EnvMonWaterSensorStatus_Type(Integer32):
    """Custom type envMonWaterSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("noComm", 2),
          ("normal", 0))
    )


_EnvMonWaterSensorStatus_Type.__name__ = "Integer32"
_EnvMonWaterSensorStatus_Object = MibTableColumn
envMonWaterSensorStatus = _EnvMonWaterSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 6),
    _EnvMonWaterSensorStatus_Type()
)
envMonWaterSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonWaterSensorStatus.setStatus("current")


class _EnvMonADCName_Type(DisplayString):
    """Custom type envMonADCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_EnvMonADCName_Type.__name__ = "DisplayString"
_EnvMonADCName_Object = MibTableColumn
envMonADCName = _EnvMonADCName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 7),
    _EnvMonADCName_Type()
)
envMonADCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envMonADCName.setStatus("current")


class _EnvMonADCStatus_Type(Integer32):
    """Custom type envMonADCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("countHigh", 3),
          ("countLow", 2),
          ("noComm", 5),
          ("normal", 0),
          ("readError", 4),
          ("reading", 1))
    )


_EnvMonADCStatus_Type.__name__ = "Integer32"
_EnvMonADCStatus_Object = MibTableColumn
envMonADCStatus = _EnvMonADCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 8),
    _EnvMonADCStatus_Type()
)
envMonADCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonADCStatus.setStatus("current")


class _EnvMonADCCount_Type(Integer32):
    """Custom type envMonADCCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_EnvMonADCCount_Type.__name__ = "Integer32"
_EnvMonADCCount_Object = MibTableColumn
envMonADCCount = _EnvMonADCCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 9),
    _EnvMonADCCount_Type()
)
envMonADCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonADCCount.setStatus("current")


class _EnvMonADCLowThresh_Type(Integer32):
    """Custom type envMonADCLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnvMonADCLowThresh_Type.__name__ = "Integer32"
_EnvMonADCLowThresh_Object = MibTableColumn
envMonADCLowThresh = _EnvMonADCLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 10),
    _EnvMonADCLowThresh_Type()
)
envMonADCLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envMonADCLowThresh.setStatus("current")


class _EnvMonADCHighThresh_Type(Integer32):
    """Custom type envMonADCHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnvMonADCHighThresh_Type.__name__ = "Integer32"
_EnvMonADCHighThresh_Object = MibTableColumn
envMonADCHighThresh = _EnvMonADCHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 11),
    _EnvMonADCHighThresh_Type()
)
envMonADCHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envMonADCHighThresh.setStatus("current")


class _EnvMonTempHumidSensorCount_Type(Integer32):
    """Custom type envMonTempHumidSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_EnvMonTempHumidSensorCount_Type.__name__ = "Integer32"
_EnvMonTempHumidSensorCount_Object = MibTableColumn
envMonTempHumidSensorCount = _EnvMonTempHumidSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 12),
    _EnvMonTempHumidSensorCount_Type()
)
envMonTempHumidSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonTempHumidSensorCount.setStatus("current")


class _EnvMonContactClosureCount_Type(Integer32):
    """Custom type envMonContactClosureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_EnvMonContactClosureCount_Type.__name__ = "Integer32"
_EnvMonContactClosureCount_Object = MibTableColumn
envMonContactClosureCount = _EnvMonContactClosureCount_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 4, 1, 13),
    _EnvMonContactClosureCount_Type()
)
envMonContactClosureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonContactClosureCount.setStatus("current")
_TempHumidSensorTable_Object = MibTable
tempHumidSensorTable = _TempHumidSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5)
)
if mibBuilder.loadTexts:
    tempHumidSensorTable.setStatus("current")
_TempHumidSensorEntry_Object = MibTableRow
tempHumidSensorEntry = _TempHumidSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1)
)
tempHumidSensorEntry.setIndexNames(
    (0, "Sentry3-MIB", "envMonIndex"),
    (0, "Sentry3-MIB", "tempHumidSensorIndex"),
)
if mibBuilder.loadTexts:
    tempHumidSensorEntry.setStatus("current")


class _TempHumidSensorIndex_Type(Integer32):
    """Custom type tempHumidSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TempHumidSensorIndex_Type.__name__ = "Integer32"
_TempHumidSensorIndex_Object = MibTableColumn
tempHumidSensorIndex = _TempHumidSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 1),
    _TempHumidSensorIndex_Type()
)
tempHumidSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempHumidSensorIndex.setStatus("current")


class _TempHumidSensorID_Type(DisplayString):
    """Custom type tempHumidSensorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TempHumidSensorID_Type.__name__ = "DisplayString"
_TempHumidSensorID_Object = MibTableColumn
tempHumidSensorID = _TempHumidSensorID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 2),
    _TempHumidSensorID_Type()
)
tempHumidSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHumidSensorID.setStatus("current")


class _TempHumidSensorName_Type(DisplayString):
    """Custom type tempHumidSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_TempHumidSensorName_Type.__name__ = "DisplayString"
_TempHumidSensorName_Object = MibTableColumn
tempHumidSensorName = _TempHumidSensorName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 3),
    _TempHumidSensorName_Type()
)
tempHumidSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHumidSensorName.setStatus("current")


class _TempHumidSensorStatus_Type(Integer32):
    """Custom type tempHumidSensorStatus based on Integer32"""
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
        *(("found", 0),
          ("lost", 2),
          ("noComm", 3),
          ("notFound", 1))
    )


_TempHumidSensorStatus_Type.__name__ = "Integer32"
_TempHumidSensorStatus_Object = MibTableColumn
tempHumidSensorStatus = _TempHumidSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 4),
    _TempHumidSensorStatus_Type()
)
tempHumidSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHumidSensorStatus.setStatus("current")


class _TempHumidSensorTempStatus_Type(Integer32):
    """Custom type tempHumidSensorTempStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("lost", 6),
          ("noComm", 7),
          ("normal", 0),
          ("notFound", 1),
          ("readError", 5),
          ("reading", 2),
          ("tempHigh", 4),
          ("tempLow", 3))
    )


_TempHumidSensorTempStatus_Type.__name__ = "Integer32"
_TempHumidSensorTempStatus_Object = MibTableColumn
tempHumidSensorTempStatus = _TempHumidSensorTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 5),
    _TempHumidSensorTempStatus_Type()
)
tempHumidSensorTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHumidSensorTempStatus.setStatus("current")


class _TempHumidSensorTempValue_Type(Integer32):
    """Custom type tempHumidSensorTempValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2540),
    )


_TempHumidSensorTempValue_Type.__name__ = "Integer32"
_TempHumidSensorTempValue_Object = MibTableColumn
tempHumidSensorTempValue = _TempHumidSensorTempValue_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 6),
    _TempHumidSensorTempValue_Type()
)
tempHumidSensorTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHumidSensorTempValue.setStatus("current")
if mibBuilder.loadTexts:
    tempHumidSensorTempValue.setUnits("tenth degrees")


class _TempHumidSensorTempLowThresh_Type(Integer32):
    """Custom type tempHumidSensorTempLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TempHumidSensorTempLowThresh_Type.__name__ = "Integer32"
_TempHumidSensorTempLowThresh_Object = MibTableColumn
tempHumidSensorTempLowThresh = _TempHumidSensorTempLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 7),
    _TempHumidSensorTempLowThresh_Type()
)
tempHumidSensorTempLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHumidSensorTempLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    tempHumidSensorTempLowThresh.setUnits("degrees")


class _TempHumidSensorTempHighThresh_Type(Integer32):
    """Custom type tempHumidSensorTempHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_TempHumidSensorTempHighThresh_Type.__name__ = "Integer32"
_TempHumidSensorTempHighThresh_Object = MibTableColumn
tempHumidSensorTempHighThresh = _TempHumidSensorTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 8),
    _TempHumidSensorTempHighThresh_Type()
)
tempHumidSensorTempHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHumidSensorTempHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    tempHumidSensorTempHighThresh.setUnits("degrees")


class _TempHumidSensorHumidStatus_Type(Integer32):
    """Custom type tempHumidSensorHumidStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("humidHigh", 4),
          ("humidLow", 3),
          ("lost", 6),
          ("noComm", 7),
          ("normal", 0),
          ("notFound", 1),
          ("readError", 5),
          ("reading", 2))
    )


_TempHumidSensorHumidStatus_Type.__name__ = "Integer32"
_TempHumidSensorHumidStatus_Object = MibTableColumn
tempHumidSensorHumidStatus = _TempHumidSensorHumidStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 9),
    _TempHumidSensorHumidStatus_Type()
)
tempHumidSensorHumidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHumidSensorHumidStatus.setStatus("current")


class _TempHumidSensorHumidValue_Type(Integer32):
    """Custom type tempHumidSensorHumidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_TempHumidSensorHumidValue_Type.__name__ = "Integer32"
_TempHumidSensorHumidValue_Object = MibTableColumn
tempHumidSensorHumidValue = _TempHumidSensorHumidValue_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 10),
    _TempHumidSensorHumidValue_Type()
)
tempHumidSensorHumidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHumidSensorHumidValue.setStatus("current")
if mibBuilder.loadTexts:
    tempHumidSensorHumidValue.setUnits("percentage relative humidity")


class _TempHumidSensorHumidLowThresh_Type(Integer32):
    """Custom type tempHumidSensorHumidLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TempHumidSensorHumidLowThresh_Type.__name__ = "Integer32"
_TempHumidSensorHumidLowThresh_Object = MibTableColumn
tempHumidSensorHumidLowThresh = _TempHumidSensorHumidLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 11),
    _TempHumidSensorHumidLowThresh_Type()
)
tempHumidSensorHumidLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHumidSensorHumidLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    tempHumidSensorHumidLowThresh.setUnits("percentage relative humidity")


class _TempHumidSensorHumidHighThresh_Type(Integer32):
    """Custom type tempHumidSensorHumidHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TempHumidSensorHumidHighThresh_Type.__name__ = "Integer32"
_TempHumidSensorHumidHighThresh_Object = MibTableColumn
tempHumidSensorHumidHighThresh = _TempHumidSensorHumidHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 12),
    _TempHumidSensorHumidHighThresh_Type()
)
tempHumidSensorHumidHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHumidSensorHumidHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    tempHumidSensorHumidHighThresh.setUnits("percentage relative humidity")


class _TempHumidSensorTempScale_Type(Integer32):
    """Custom type tempHumidSensorTempScale based on Integer32"""
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


_TempHumidSensorTempScale_Type.__name__ = "Integer32"
_TempHumidSensorTempScale_Object = MibTableColumn
tempHumidSensorTempScale = _TempHumidSensorTempScale_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 13),
    _TempHumidSensorTempScale_Type()
)
tempHumidSensorTempScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHumidSensorTempScale.setStatus("current")


class _TempHumidSensorTempRecDelta_Type(Integer32):
    """Custom type tempHumidSensorTempRecDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_TempHumidSensorTempRecDelta_Type.__name__ = "Integer32"
_TempHumidSensorTempRecDelta_Object = MibTableColumn
tempHumidSensorTempRecDelta = _TempHumidSensorTempRecDelta_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 14),
    _TempHumidSensorTempRecDelta_Type()
)
tempHumidSensorTempRecDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHumidSensorTempRecDelta.setStatus("current")
if mibBuilder.loadTexts:
    tempHumidSensorTempRecDelta.setUnits("degrees")


class _TempHumidSensorHumidRecDelta_Type(Integer32):
    """Custom type tempHumidSensorHumidRecDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_TempHumidSensorHumidRecDelta_Type.__name__ = "Integer32"
_TempHumidSensorHumidRecDelta_Object = MibTableColumn
tempHumidSensorHumidRecDelta = _TempHumidSensorHumidRecDelta_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 5, 1, 15),
    _TempHumidSensorHumidRecDelta_Type()
)
tempHumidSensorHumidRecDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHumidSensorHumidRecDelta.setStatus("current")
if mibBuilder.loadTexts:
    tempHumidSensorHumidRecDelta.setUnits("percentage relative humidity")
_ContactClosureTable_Object = MibTable
contactClosureTable = _ContactClosureTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 6)
)
if mibBuilder.loadTexts:
    contactClosureTable.setStatus("current")
_ContactClosureEntry_Object = MibTableRow
contactClosureEntry = _ContactClosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 6, 1)
)
contactClosureEntry.setIndexNames(
    (0, "Sentry3-MIB", "envMonIndex"),
    (0, "Sentry3-MIB", "contactClosureIndex"),
)
if mibBuilder.loadTexts:
    contactClosureEntry.setStatus("current")


class _ContactClosureIndex_Type(Integer32):
    """Custom type contactClosureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ContactClosureIndex_Type.__name__ = "Integer32"
_ContactClosureIndex_Object = MibTableColumn
contactClosureIndex = _ContactClosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 6, 1, 1),
    _ContactClosureIndex_Type()
)
contactClosureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    contactClosureIndex.setStatus("current")


class _ContactClosureID_Type(DisplayString):
    """Custom type contactClosureID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ContactClosureID_Type.__name__ = "DisplayString"
_ContactClosureID_Object = MibTableColumn
contactClosureID = _ContactClosureID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 6, 1, 2),
    _ContactClosureID_Type()
)
contactClosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactClosureID.setStatus("current")


class _ContactClosureName_Type(DisplayString):
    """Custom type contactClosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ContactClosureName_Type.__name__ = "DisplayString"
_ContactClosureName_Object = MibTableColumn
contactClosureName = _ContactClosureName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 6, 1, 3),
    _ContactClosureName_Type()
)
contactClosureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactClosureName.setStatus("current")


class _ContactClosureStatus_Type(Integer32):
    """Custom type contactClosureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("noComm", 2),
          ("normal", 0))
    )


_ContactClosureStatus_Type.__name__ = "Integer32"
_ContactClosureStatus_Object = MibTableColumn
contactClosureStatus = _ContactClosureStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 6, 1, 4),
    _ContactClosureStatus_Type()
)
contactClosureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactClosureStatus.setStatus("current")
_BranchTable_Object = MibTable
branchTable = _BranchTable_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7)
)
if mibBuilder.loadTexts:
    branchTable.setStatus("current")
_BranchEntry_Object = MibTableRow
branchEntry = _BranchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1)
)
branchEntry.setIndexNames(
    (0, "Sentry3-MIB", "towerIndex"),
    (0, "Sentry3-MIB", "infeedIndex"),
    (0, "Sentry3-MIB", "branchIndex"),
)
if mibBuilder.loadTexts:
    branchEntry.setStatus("current")


class _BranchIndex_Type(Integer32):
    """Custom type branchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BranchIndex_Type.__name__ = "Integer32"
_BranchIndex_Object = MibTableColumn
branchIndex = _BranchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1, 1),
    _BranchIndex_Type()
)
branchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    branchIndex.setStatus("current")


class _BranchID_Type(DisplayString):
    """Custom type branchID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_BranchID_Type.__name__ = "DisplayString"
_BranchID_Object = MibTableColumn
branchID = _BranchID_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1, 2),
    _BranchID_Type()
)
branchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branchID.setStatus("current")


class _BranchName_Type(DisplayString):
    """Custom type branchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_BranchName_Type.__name__ = "DisplayString"
_BranchName_Object = MibTableColumn
branchName = _BranchName_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1, 3),
    _BranchName_Type()
)
branchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    branchName.setStatus("current")


class _BranchCapabilities_Type(Bits):
    """Custom type branchCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("loadSense", 1),
          ("onSense", 0))
    )

_BranchCapabilities_Type.__name__ = "Bits"
_BranchCapabilities_Object = MibTableColumn
branchCapabilities = _BranchCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1, 4),
    _BranchCapabilities_Type()
)
branchCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branchCapabilities.setStatus("current")


class _BranchStatus_Type(Integer32):
    """Custom type branchStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noComm", 6),
          ("off", 0),
          ("offError", 4),
          ("offFuse", 8),
          ("offWait", 2),
          ("on", 1),
          ("onError", 5),
          ("onFuse", 9),
          ("onWait", 3),
          ("reading", 7))
    )


_BranchStatus_Type.__name__ = "Integer32"
_BranchStatus_Object = MibTableColumn
branchStatus = _BranchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1, 5),
    _BranchStatus_Type()
)
branchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branchStatus.setStatus("current")


class _BranchLoadStatus_Type(Integer32):
    """Custom type branchLoadStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("loadHigh", 4),
          ("loadLow", 3),
          ("noComm", 7),
          ("normal", 0),
          ("notOn", 1),
          ("overLoad", 5),
          ("readError", 6),
          ("reading", 2))
    )


_BranchLoadStatus_Type.__name__ = "Integer32"
_BranchLoadStatus_Object = MibTableColumn
branchLoadStatus = _BranchLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1, 6),
    _BranchLoadStatus_Type()
)
branchLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branchLoadStatus.setStatus("current")


class _BranchLoadValue_Type(Integer32):
    """Custom type branchLoadValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4000),
    )


_BranchLoadValue_Type.__name__ = "Integer32"
_BranchLoadValue_Object = MibTableColumn
branchLoadValue = _BranchLoadValue_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1, 7),
    _BranchLoadValue_Type()
)
branchLoadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branchLoadValue.setStatus("current")
if mibBuilder.loadTexts:
    branchLoadValue.setUnits("hundredth Amps")


class _BranchLoadHighThresh_Type(Integer32):
    """Custom type branchLoadHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_BranchLoadHighThresh_Type.__name__ = "Integer32"
_BranchLoadHighThresh_Object = MibTableColumn
branchLoadHighThresh = _BranchLoadHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1, 8),
    _BranchLoadHighThresh_Type()
)
branchLoadHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    branchLoadHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    branchLoadHighThresh.setUnits("Amps")


class _BranchCapacity_Type(Integer32):
    """Custom type branchCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 40),
    )


_BranchCapacity_Type.__name__ = "Integer32"
_BranchCapacity_Object = MibTableColumn
branchCapacity = _BranchCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 2, 7, 1, 9),
    _BranchCapacity_Type()
)
branchCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    branchCapacity.setStatus("current")
if mibBuilder.loadTexts:
    branchCapacity.setUnits("Amps")
_EventInformationGroup_ObjectIdentity = ObjectIdentity
eventInformationGroup = _EventInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 3, 99)
)


class _EventStatusText_Type(DisplayString):
    """Custom type eventStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EventStatusText_Type.__name__ = "DisplayString"
_EventStatusText_Object = MibScalar
eventStatusText = _EventStatusText_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 99, 1),
    _EventStatusText_Type()
)
eventStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventStatusText.setStatus("current")


class _EventStatusCondition_Type(Integer32):
    """Custom type eventStatusCondition based on Integer32"""
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


_EventStatusCondition_Type.__name__ = "Integer32"
_EventStatusCondition_Object = MibScalar
eventStatusCondition = _EventStatusCondition_Object(
    (1, 3, 6, 1, 4, 1, 1718, 3, 99, 2),
    _EventStatusCondition_Type()
)
eventStatusCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventStatusCondition.setStatus("current")
_Sentry3Traps_ObjectIdentity = ObjectIdentity
sentry3Traps = _Sentry3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0)
)

# Managed Objects groups


# Notification objects

towerStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 1)
)
towerStatusEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "towerID"),
        ("Sentry3-MIB", "towerName"),
        ("Sentry3-MIB", "towerStatus"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    towerStatusEvent.setStatus(
        "current"
    )

infeedStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 2)
)
infeedStatusEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "infeedID"),
        ("Sentry3-MIB", "infeedName"),
        ("Sentry3-MIB", "infeedStatus"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    infeedStatusEvent.setStatus(
        "current"
    )

infeedLoadEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 3)
)
infeedLoadEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "infeedID"),
        ("Sentry3-MIB", "infeedName"),
        ("Sentry3-MIB", "infeedLoadStatus"),
        ("Sentry3-MIB", "infeedLoadValue"),
        ("Sentry3-MIB", "infeedLoadHighThresh"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    infeedLoadEvent.setStatus(
        "current"
    )

outletStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 4)
)
outletStatusEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "outletID"),
        ("Sentry3-MIB", "outletName"),
        ("Sentry3-MIB", "outletStatus"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    outletStatusEvent.setStatus(
        "current"
    )

outletLoadEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 5)
)
outletLoadEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "outletID"),
        ("Sentry3-MIB", "outletName"),
        ("Sentry3-MIB", "outletLoadStatus"),
        ("Sentry3-MIB", "outletLoadValue"),
        ("Sentry3-MIB", "outletLoadLowThresh"),
        ("Sentry3-MIB", "outletLoadHighThresh"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    outletLoadEvent.setStatus(
        "current"
    )

outletChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 6)
)
outletChangeEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "outletID"),
        ("Sentry3-MIB", "outletName"),
        ("Sentry3-MIB", "outletStatus"),
        ("Sentry3-MIB", "outletControlState"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    outletChangeEvent.setStatus(
        "current"
    )

envMonStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 7)
)
envMonStatusEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "envMonID"),
        ("Sentry3-MIB", "envMonName"),
        ("Sentry3-MIB", "envMonStatus"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    envMonStatusEvent.setStatus(
        "current"
    )

envMonWaterSensorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 8)
)
envMonWaterSensorEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "envMonID"),
        ("Sentry3-MIB", "envMonWaterSensorName"),
        ("Sentry3-MIB", "envMonWaterSensorStatus"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    envMonWaterSensorEvent.setStatus(
        "current"
    )

envMonADCEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 9)
)
envMonADCEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "envMonID"),
        ("Sentry3-MIB", "envMonADCName"),
        ("Sentry3-MIB", "envMonADCStatus"),
        ("Sentry3-MIB", "envMonADCCount"),
        ("Sentry3-MIB", "envMonADCLowThresh"),
        ("Sentry3-MIB", "envMonADCHighThresh"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    envMonADCEvent.setStatus(
        "current"
    )

tempHumidSensorStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 10)
)
tempHumidSensorStatusEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "tempHumidSensorID"),
        ("Sentry3-MIB", "tempHumidSensorName"),
        ("Sentry3-MIB", "tempHumidSensorStatus"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    tempHumidSensorStatusEvent.setStatus(
        "current"
    )

tempHumidSensorTempEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 11)
)
tempHumidSensorTempEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "tempHumidSensorID"),
        ("Sentry3-MIB", "tempHumidSensorName"),
        ("Sentry3-MIB", "tempHumidSensorTempStatus"),
        ("Sentry3-MIB", "tempHumidSensorTempValue"),
        ("Sentry3-MIB", "tempHumidSensorTempLowThresh"),
        ("Sentry3-MIB", "tempHumidSensorTempHighThresh"),
        ("Sentry3-MIB", "tempHumidSensorTempScale"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    tempHumidSensorTempEvent.setStatus(
        "current"
    )

tempHumidSensorHumidEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 12)
)
tempHumidSensorHumidEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "tempHumidSensorID"),
        ("Sentry3-MIB", "tempHumidSensorName"),
        ("Sentry3-MIB", "tempHumidSensorHumidStatus"),
        ("Sentry3-MIB", "tempHumidSensorHumidValue"),
        ("Sentry3-MIB", "tempHumidSensorHumidLowThresh"),
        ("Sentry3-MIB", "tempHumidSensorHumidHighThresh"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    tempHumidSensorHumidEvent.setStatus(
        "current"
    )

contactClosureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 13)
)
contactClosureEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "contactClosureID"),
        ("Sentry3-MIB", "contactClosureName"),
        ("Sentry3-MIB", "contactClosureStatus"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    contactClosureEvent.setStatus(
        "current"
    )

branchStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 14)
)
branchStatusEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "branchID"),
        ("Sentry3-MIB", "branchName"),
        ("Sentry3-MIB", "branchStatus"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    branchStatusEvent.setStatus(
        "current"
    )

branchLoadEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1718, 3, 100, 0, 15)
)
branchLoadEvent.setObjects(
      *(("Sentry3-MIB", "systemLocation"),
        ("Sentry3-MIB", "branchID"),
        ("Sentry3-MIB", "branchName"),
        ("Sentry3-MIB", "branchLoadStatus"),
        ("Sentry3-MIB", "branchLoadValue"),
        ("Sentry3-MIB", "branchLoadHighThresh"),
        ("Sentry3-MIB", "eventStatusText"),
        ("Sentry3-MIB", "eventStatusCondition"))
)
if mibBuilder.loadTexts:
    branchLoadEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Sentry3-MIB",
    **{"serverTech": serverTech,
       "sentry3": sentry3,
       "systemGroup": systemGroup,
       "systemVersion": systemVersion,
       "systemNICSerialNumber": systemNICSerialNumber,
       "systemLocation": systemLocation,
       "systemTowerCount": systemTowerCount,
       "systemEnvMonCount": systemEnvMonCount,
       "systemTotalPower": systemTotalPower,
       "systemArea": systemArea,
       "systemWattsPerAreaUnit": systemWattsPerAreaUnit,
       "systemAreaUnit": systemAreaUnit,
       "systemPowerFactor": systemPowerFactor,
       "systemFeatures": systemFeatures,
       "systemFeatureKey": systemFeatureKey,
       "systemOutletSeqInterval": systemOutletSeqInterval,
       "systemOutletRebootDelay": systemOutletRebootDelay,
       "systemConfigModifiedCount": systemConfigModifiedCount,
       "systemTables": systemTables,
       "towerTable": towerTable,
       "towerEntry": towerEntry,
       "towerIndex": towerIndex,
       "towerID": towerID,
       "towerName": towerName,
       "towerStatus": towerStatus,
       "towerInfeedCount": towerInfeedCount,
       "towerProductSN": towerProductSN,
       "towerModelNumber": towerModelNumber,
       "towerCapabilities": towerCapabilities,
       "towerVACapacity": towerVACapacity,
       "towerVACapacityUsed": towerVACapacityUsed,
       "towerActivePower": towerActivePower,
       "towerApparentPower": towerApparentPower,
       "towerPowerFactor": towerPowerFactor,
       "towerEnergy": towerEnergy,
       "towerLineFrequency": towerLineFrequency,
       "infeedTable": infeedTable,
       "infeedEntry": infeedEntry,
       "infeedIndex": infeedIndex,
       "infeedID": infeedID,
       "infeedName": infeedName,
       "infeedCapabilities": infeedCapabilities,
       "infeedStatus": infeedStatus,
       "infeedLoadStatus": infeedLoadStatus,
       "infeedLoadValue": infeedLoadValue,
       "infeedLoadHighThresh": infeedLoadHighThresh,
       "infeedOutletCount": infeedOutletCount,
       "infeedCapacity": infeedCapacity,
       "infeedVoltage": infeedVoltage,
       "infeedPower": infeedPower,
       "infeedApparentPower": infeedApparentPower,
       "infeedPowerFactor": infeedPowerFactor,
       "infeedCrestFactor": infeedCrestFactor,
       "infeedEnergy": infeedEnergy,
       "infeedReactance": infeedReactance,
       "infeedPhaseVoltage": infeedPhaseVoltage,
       "infeedPhaseCurrent": infeedPhaseCurrent,
       "infeedCapacityUsed": infeedCapacityUsed,
       "infeedLineID": infeedLineID,
       "infeedLineToLineID": infeedLineToLineID,
       "infeedPhaseID": infeedPhaseID,
       "infeedVACapacity": infeedVACapacity,
       "infeedVACapacityUsed": infeedVACapacityUsed,
       "outletTable": outletTable,
       "outletEntry": outletEntry,
       "outletIndex": outletIndex,
       "outletID": outletID,
       "outletName": outletName,
       "outletCapabilities": outletCapabilities,
       "outletStatus": outletStatus,
       "outletLoadStatus": outletLoadStatus,
       "outletLoadValue": outletLoadValue,
       "outletLoadLowThresh": outletLoadLowThresh,
       "outletLoadHighThresh": outletLoadHighThresh,
       "outletControlState": outletControlState,
       "outletControlAction": outletControlAction,
       "outletCapacity": outletCapacity,
       "outletVoltage": outletVoltage,
       "outletPower": outletPower,
       "outletApparentPower": outletApparentPower,
       "outletPowerFactor": outletPowerFactor,
       "outletCrestFactor": outletCrestFactor,
       "outletEnergy": outletEnergy,
       "outletWakeupState": outletWakeupState,
       "outletPostOnDelay": outletPostOnDelay,
       "envMonTable": envMonTable,
       "envMonEntry": envMonEntry,
       "envMonIndex": envMonIndex,
       "envMonID": envMonID,
       "envMonName": envMonName,
       "envMonStatus": envMonStatus,
       "envMonWaterSensorName": envMonWaterSensorName,
       "envMonWaterSensorStatus": envMonWaterSensorStatus,
       "envMonADCName": envMonADCName,
       "envMonADCStatus": envMonADCStatus,
       "envMonADCCount": envMonADCCount,
       "envMonADCLowThresh": envMonADCLowThresh,
       "envMonADCHighThresh": envMonADCHighThresh,
       "envMonTempHumidSensorCount": envMonTempHumidSensorCount,
       "envMonContactClosureCount": envMonContactClosureCount,
       "tempHumidSensorTable": tempHumidSensorTable,
       "tempHumidSensorEntry": tempHumidSensorEntry,
       "tempHumidSensorIndex": tempHumidSensorIndex,
       "tempHumidSensorID": tempHumidSensorID,
       "tempHumidSensorName": tempHumidSensorName,
       "tempHumidSensorStatus": tempHumidSensorStatus,
       "tempHumidSensorTempStatus": tempHumidSensorTempStatus,
       "tempHumidSensorTempValue": tempHumidSensorTempValue,
       "tempHumidSensorTempLowThresh": tempHumidSensorTempLowThresh,
       "tempHumidSensorTempHighThresh": tempHumidSensorTempHighThresh,
       "tempHumidSensorHumidStatus": tempHumidSensorHumidStatus,
       "tempHumidSensorHumidValue": tempHumidSensorHumidValue,
       "tempHumidSensorHumidLowThresh": tempHumidSensorHumidLowThresh,
       "tempHumidSensorHumidHighThresh": tempHumidSensorHumidHighThresh,
       "tempHumidSensorTempScale": tempHumidSensorTempScale,
       "tempHumidSensorTempRecDelta": tempHumidSensorTempRecDelta,
       "tempHumidSensorHumidRecDelta": tempHumidSensorHumidRecDelta,
       "contactClosureTable": contactClosureTable,
       "contactClosureEntry": contactClosureEntry,
       "contactClosureIndex": contactClosureIndex,
       "contactClosureID": contactClosureID,
       "contactClosureName": contactClosureName,
       "contactClosureStatus": contactClosureStatus,
       "branchTable": branchTable,
       "branchEntry": branchEntry,
       "branchIndex": branchIndex,
       "branchID": branchID,
       "branchName": branchName,
       "branchCapabilities": branchCapabilities,
       "branchStatus": branchStatus,
       "branchLoadStatus": branchLoadStatus,
       "branchLoadValue": branchLoadValue,
       "branchLoadHighThresh": branchLoadHighThresh,
       "branchCapacity": branchCapacity,
       "eventInformationGroup": eventInformationGroup,
       "eventStatusText": eventStatusText,
       "eventStatusCondition": eventStatusCondition,
       "sentry3Traps": sentry3Traps,
       "events": events,
       "towerStatusEvent": towerStatusEvent,
       "infeedStatusEvent": infeedStatusEvent,
       "infeedLoadEvent": infeedLoadEvent,
       "outletStatusEvent": outletStatusEvent,
       "outletLoadEvent": outletLoadEvent,
       "outletChangeEvent": outletChangeEvent,
       "envMonStatusEvent": envMonStatusEvent,
       "envMonWaterSensorEvent": envMonWaterSensorEvent,
       "envMonADCEvent": envMonADCEvent,
       "tempHumidSensorStatusEvent": tempHumidSensorStatusEvent,
       "tempHumidSensorTempEvent": tempHumidSensorTempEvent,
       "tempHumidSensorHumidEvent": tempHumidSensorHumidEvent,
       "contactClosureEvent": contactClosureEvent,
       "branchStatusEvent": branchStatusEvent,
       "branchLoadEvent": branchLoadEvent}
)
