# SNMP MIB module (SLP1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SLP1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:28 2024
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

slp1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lantronix_ObjectIdentity = ObjectIdentity
lantronix = _Lantronix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1)
)
_Slp_ObjectIdentity = ObjectIdentity
slp = _Slp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 9)
)
_Slp1SystemGroup_ObjectIdentity = ObjectIdentity
slp1SystemGroup = _Slp1SystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1)
)


class _Slp1SystemVersion_Type(DisplayString):
    """Custom type slp1SystemVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Slp1SystemVersion_Type.__name__ = "DisplayString"
_Slp1SystemVersion_Object = MibScalar
slp1SystemVersion = _Slp1SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 1),
    _Slp1SystemVersion_Type()
)
slp1SystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1SystemVersion.setStatus("current")


class _Slp1SystemNICSerialNumber_Type(DisplayString):
    """Custom type slp1SystemNICSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Slp1SystemNICSerialNumber_Type.__name__ = "DisplayString"
_Slp1SystemNICSerialNumber_Object = MibScalar
slp1SystemNICSerialNumber = _Slp1SystemNICSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 2),
    _Slp1SystemNICSerialNumber_Type()
)
slp1SystemNICSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1SystemNICSerialNumber.setStatus("current")


class _Slp1SystemLocation_Type(DisplayString):
    """Custom type slp1SystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Slp1SystemLocation_Type.__name__ = "DisplayString"
_Slp1SystemLocation_Object = MibScalar
slp1SystemLocation = _Slp1SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 3),
    _Slp1SystemLocation_Type()
)
slp1SystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1SystemLocation.setStatus("current")


class _Slp1SystemTowerCount_Type(Integer32):
    """Custom type slp1SystemTowerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Slp1SystemTowerCount_Type.__name__ = "Integer32"
_Slp1SystemTowerCount_Object = MibScalar
slp1SystemTowerCount = _Slp1SystemTowerCount_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 4),
    _Slp1SystemTowerCount_Type()
)
slp1SystemTowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1SystemTowerCount.setStatus("current")


class _Slp1SystemEnvMonCount_Type(Integer32):
    """Custom type slp1SystemEnvMonCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Slp1SystemEnvMonCount_Type.__name__ = "Integer32"
_Slp1SystemEnvMonCount_Object = MibScalar
slp1SystemEnvMonCount = _Slp1SystemEnvMonCount_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 1, 5),
    _Slp1SystemEnvMonCount_Type()
)
slp1SystemEnvMonCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1SystemEnvMonCount.setStatus("current")
_Slp1SystemTables_ObjectIdentity = ObjectIdentity
slp1SystemTables = _Slp1SystemTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2)
)
_Slp1TowerTable_Object = MibTable
slp1TowerTable = _Slp1TowerTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slp1TowerTable.setStatus("current")
_Slp1TowerEntry_Object = MibTableRow
slp1TowerEntry = _Slp1TowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1)
)
slp1TowerEntry.setIndexNames(
    (0, "SLP1-MIB", "slp1TowerIndex"),
)
if mibBuilder.loadTexts:
    slp1TowerEntry.setStatus("current")


class _Slp1TowerIndex_Type(Integer32):
    """Custom type slp1TowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Slp1TowerIndex_Type.__name__ = "Integer32"
_Slp1TowerIndex_Object = MibTableColumn
slp1TowerIndex = _Slp1TowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 1),
    _Slp1TowerIndex_Type()
)
slp1TowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slp1TowerIndex.setStatus("current")


class _Slp1TowerID_Type(DisplayString):
    """Custom type slp1TowerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Slp1TowerID_Type.__name__ = "DisplayString"
_Slp1TowerID_Object = MibTableColumn
slp1TowerID = _Slp1TowerID_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 2),
    _Slp1TowerID_Type()
)
slp1TowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TowerID.setStatus("current")


class _Slp1TowerName_Type(DisplayString):
    """Custom type slp1TowerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Slp1TowerName_Type.__name__ = "DisplayString"
_Slp1TowerName_Object = MibTableColumn
slp1TowerName = _Slp1TowerName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 3),
    _Slp1TowerName_Type()
)
slp1TowerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1TowerName.setStatus("current")


class _Slp1TowerStatus_Type(Integer32):
    """Custom type slp1TowerStatus based on Integer32"""
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


_Slp1TowerStatus_Type.__name__ = "Integer32"
_Slp1TowerStatus_Object = MibTableColumn
slp1TowerStatus = _Slp1TowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 4),
    _Slp1TowerStatus_Type()
)
slp1TowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TowerStatus.setStatus("current")


class _Slp1TowerInfeedCount_Type(Integer32):
    """Custom type slp1TowerInfeedCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Slp1TowerInfeedCount_Type.__name__ = "Integer32"
_Slp1TowerInfeedCount_Object = MibTableColumn
slp1TowerInfeedCount = _Slp1TowerInfeedCount_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 1, 1, 5),
    _Slp1TowerInfeedCount_Type()
)
slp1TowerInfeedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TowerInfeedCount.setStatus("current")
_Slp1InfeedTable_Object = MibTable
slp1InfeedTable = _Slp1InfeedTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    slp1InfeedTable.setStatus("current")
_Slp1InfeedEntry_Object = MibTableRow
slp1InfeedEntry = _Slp1InfeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1)
)
slp1InfeedEntry.setIndexNames(
    (0, "SLP1-MIB", "slp1TowerIndex"),
    (0, "SLP1-MIB", "slp1InfeedIndex"),
)
if mibBuilder.loadTexts:
    slp1InfeedEntry.setStatus("current")


class _Slp1InfeedIndex_Type(Integer32):
    """Custom type slp1InfeedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Slp1InfeedIndex_Type.__name__ = "Integer32"
_Slp1InfeedIndex_Object = MibTableColumn
slp1InfeedIndex = _Slp1InfeedIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 1),
    _Slp1InfeedIndex_Type()
)
slp1InfeedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slp1InfeedIndex.setStatus("current")


class _Slp1InfeedID_Type(DisplayString):
    """Custom type slp1InfeedID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Slp1InfeedID_Type.__name__ = "DisplayString"
_Slp1InfeedID_Object = MibTableColumn
slp1InfeedID = _Slp1InfeedID_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 2),
    _Slp1InfeedID_Type()
)
slp1InfeedID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1InfeedID.setStatus("current")


class _Slp1InfeedName_Type(DisplayString):
    """Custom type slp1InfeedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Slp1InfeedName_Type.__name__ = "DisplayString"
_Slp1InfeedName_Object = MibTableColumn
slp1InfeedName = _Slp1InfeedName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 3),
    _Slp1InfeedName_Type()
)
slp1InfeedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1InfeedName.setStatus("current")


class _Slp1InfeedCapabilities_Type(Bits):
    """Custom type slp1InfeedCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("defaultOff", 4),
          ("failSafe", 3),
          ("loadSense", 1),
          ("onSense", 0),
          ("powerControl", 2))
    )

_Slp1InfeedCapabilities_Type.__name__ = "Bits"
_Slp1InfeedCapabilities_Object = MibTableColumn
slp1InfeedCapabilities = _Slp1InfeedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 4),
    _Slp1InfeedCapabilities_Type()
)
slp1InfeedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1InfeedCapabilities.setStatus("current")


class _Slp1InfeedStatus_Type(Integer32):
    """Custom type slp1InfeedStatus based on Integer32"""
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
        *(("noComm", 6),
          ("off", 0),
          ("offError", 4),
          ("offWait", 2),
          ("on", 1),
          ("onError", 5),
          ("onWait", 3))
    )


_Slp1InfeedStatus_Type.__name__ = "Integer32"
_Slp1InfeedStatus_Object = MibTableColumn
slp1InfeedStatus = _Slp1InfeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 5),
    _Slp1InfeedStatus_Type()
)
slp1InfeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1InfeedStatus.setStatus("current")


class _Slp1InfeedLoadStatus_Type(Integer32):
    """Custom type slp1InfeedLoadStatus based on Integer32"""
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


_Slp1InfeedLoadStatus_Type.__name__ = "Integer32"
_Slp1InfeedLoadStatus_Object = MibTableColumn
slp1InfeedLoadStatus = _Slp1InfeedLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 6),
    _Slp1InfeedLoadStatus_Type()
)
slp1InfeedLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1InfeedLoadStatus.setStatus("current")


class _Slp1InfeedLoadValue_Type(Integer32):
    """Custom type slp1InfeedLoadValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25500),
    )


_Slp1InfeedLoadValue_Type.__name__ = "Integer32"
_Slp1InfeedLoadValue_Object = MibTableColumn
slp1InfeedLoadValue = _Slp1InfeedLoadValue_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 7),
    _Slp1InfeedLoadValue_Type()
)
slp1InfeedLoadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1InfeedLoadValue.setStatus("current")
if mibBuilder.loadTexts:
    slp1InfeedLoadValue.setUnits("hundredth Amps")


class _Slp1InfeedLoadHighThresh_Type(Integer32):
    """Custom type slp1InfeedLoadHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Slp1InfeedLoadHighThresh_Type.__name__ = "Integer32"
_Slp1InfeedLoadHighThresh_Object = MibTableColumn
slp1InfeedLoadHighThresh = _Slp1InfeedLoadHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 8),
    _Slp1InfeedLoadHighThresh_Type()
)
slp1InfeedLoadHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1InfeedLoadHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    slp1InfeedLoadHighThresh.setUnits("Amps")


class _Slp1InfeedOutletCount_Type(Integer32):
    """Custom type slp1InfeedOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Slp1InfeedOutletCount_Type.__name__ = "Integer32"
_Slp1InfeedOutletCount_Object = MibTableColumn
slp1InfeedOutletCount = _Slp1InfeedOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 2, 1, 9),
    _Slp1InfeedOutletCount_Type()
)
slp1InfeedOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1InfeedOutletCount.setStatus("current")
_Slp1OutletTable_Object = MibTable
slp1OutletTable = _Slp1OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    slp1OutletTable.setStatus("current")
_Slp1OutletEntry_Object = MibTableRow
slp1OutletEntry = _Slp1OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1)
)
slp1OutletEntry.setIndexNames(
    (0, "SLP1-MIB", "slp1TowerIndex"),
    (0, "SLP1-MIB", "slp1InfeedIndex"),
    (0, "SLP1-MIB", "slp1OutletIndex"),
)
if mibBuilder.loadTexts:
    slp1OutletEntry.setStatus("current")


class _Slp1OutletIndex_Type(Integer32):
    """Custom type slp1OutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Slp1OutletIndex_Type.__name__ = "Integer32"
_Slp1OutletIndex_Object = MibTableColumn
slp1OutletIndex = _Slp1OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 1),
    _Slp1OutletIndex_Type()
)
slp1OutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slp1OutletIndex.setStatus("current")


class _Slp1OutletID_Type(DisplayString):
    """Custom type slp1OutletID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Slp1OutletID_Type.__name__ = "DisplayString"
_Slp1OutletID_Object = MibTableColumn
slp1OutletID = _Slp1OutletID_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 2),
    _Slp1OutletID_Type()
)
slp1OutletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1OutletID.setStatus("current")


class _Slp1OutletName_Type(DisplayString):
    """Custom type slp1OutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Slp1OutletName_Type.__name__ = "DisplayString"
_Slp1OutletName_Object = MibTableColumn
slp1OutletName = _Slp1OutletName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 3),
    _Slp1OutletName_Type()
)
slp1OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1OutletName.setStatus("current")


class _Slp1OutletCapabilities_Type(Bits):
    """Custom type slp1OutletCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("defaultOn", 4),
          ("loadSense", 1),
          ("onSense", 0),
          ("ownInfeed", 5),
          ("powerControl", 2),
          ("shutdown", 3))
    )

_Slp1OutletCapabilities_Type.__name__ = "Bits"
_Slp1OutletCapabilities_Object = MibTableColumn
slp1OutletCapabilities = _Slp1OutletCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 4),
    _Slp1OutletCapabilities_Type()
)
slp1OutletCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1OutletCapabilities.setStatus("current")


class _Slp1OutletStatus_Type(Integer32):
    """Custom type slp1OutletStatus based on Integer32"""
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
        *(("noComm", 6),
          ("off", 0),
          ("offError", 4),
          ("offWait", 2),
          ("on", 1),
          ("onError", 5),
          ("onWait", 3),
          ("reading", 7))
    )


_Slp1OutletStatus_Type.__name__ = "Integer32"
_Slp1OutletStatus_Object = MibTableColumn
slp1OutletStatus = _Slp1OutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 5),
    _Slp1OutletStatus_Type()
)
slp1OutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1OutletStatus.setStatus("current")


class _Slp1OutletLoadStatus_Type(Integer32):
    """Custom type slp1OutletLoadStatus based on Integer32"""
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


_Slp1OutletLoadStatus_Type.__name__ = "Integer32"
_Slp1OutletLoadStatus_Object = MibTableColumn
slp1OutletLoadStatus = _Slp1OutletLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 6),
    _Slp1OutletLoadStatus_Type()
)
slp1OutletLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1OutletLoadStatus.setStatus("current")


class _Slp1OutletLoadValue_Type(Integer32):
    """Custom type slp1OutletLoadValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 25500),
    )


_Slp1OutletLoadValue_Type.__name__ = "Integer32"
_Slp1OutletLoadValue_Object = MibTableColumn
slp1OutletLoadValue = _Slp1OutletLoadValue_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 7),
    _Slp1OutletLoadValue_Type()
)
slp1OutletLoadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1OutletLoadValue.setStatus("current")
if mibBuilder.loadTexts:
    slp1OutletLoadValue.setUnits("hundredth Amps")


class _Slp1OutletLoadLowThresh_Type(Integer32):
    """Custom type slp1OutletLoadLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Slp1OutletLoadLowThresh_Type.__name__ = "Integer32"
_Slp1OutletLoadLowThresh_Object = MibTableColumn
slp1OutletLoadLowThresh = _Slp1OutletLoadLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 8),
    _Slp1OutletLoadLowThresh_Type()
)
slp1OutletLoadLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1OutletLoadLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    slp1OutletLoadLowThresh.setUnits("Amps")


class _Slp1OutletLoadHighThresh_Type(Integer32):
    """Custom type slp1OutletLoadHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Slp1OutletLoadHighThresh_Type.__name__ = "Integer32"
_Slp1OutletLoadHighThresh_Object = MibTableColumn
slp1OutletLoadHighThresh = _Slp1OutletLoadHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 9),
    _Slp1OutletLoadHighThresh_Type()
)
slp1OutletLoadHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1OutletLoadHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    slp1OutletLoadHighThresh.setUnits("Amps")


class _Slp1OutletControlState_Type(Integer32):
    """Custom type slp1OutletControlState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("idleOff", 0),
          ("idleOn", 1),
          ("lockedOff", 6),
          ("lockedOn", 7),
          ("off", 4),
          ("on", 5),
          ("pendOff", 11),
          ("pendOn", 10),
          ("reboot", 8),
          ("shutdown", 9),
          ("wakeOff", 2),
          ("wakeOn", 3))
    )


_Slp1OutletControlState_Type.__name__ = "Integer32"
_Slp1OutletControlState_Object = MibTableColumn
slp1OutletControlState = _Slp1OutletControlState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 10),
    _Slp1OutletControlState_Type()
)
slp1OutletControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1OutletControlState.setStatus("current")


class _Slp1OutletControlAction_Type(Integer32):
    """Custom type slp1OutletControlAction based on Integer32"""
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


_Slp1OutletControlAction_Type.__name__ = "Integer32"
_Slp1OutletControlAction_Object = MibTableColumn
slp1OutletControlAction = _Slp1OutletControlAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 3, 1, 11),
    _Slp1OutletControlAction_Type()
)
slp1OutletControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1OutletControlAction.setStatus("current")
_Slp1EnvMonTable_Object = MibTable
slp1EnvMonTable = _Slp1EnvMonTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4)
)
if mibBuilder.loadTexts:
    slp1EnvMonTable.setStatus("current")
_Slp1EnvMonEntry_Object = MibTableRow
slp1EnvMonEntry = _Slp1EnvMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1)
)
slp1EnvMonEntry.setIndexNames(
    (0, "SLP1-MIB", "slp1EnvMonIndex"),
)
if mibBuilder.loadTexts:
    slp1EnvMonEntry.setStatus("current")


class _Slp1EnvMonIndex_Type(Integer32):
    """Custom type slp1EnvMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Slp1EnvMonIndex_Type.__name__ = "Integer32"
_Slp1EnvMonIndex_Object = MibTableColumn
slp1EnvMonIndex = _Slp1EnvMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 1),
    _Slp1EnvMonIndex_Type()
)
slp1EnvMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slp1EnvMonIndex.setStatus("current")


class _Slp1EnvMonID_Type(DisplayString):
    """Custom type slp1EnvMonID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Slp1EnvMonID_Type.__name__ = "DisplayString"
_Slp1EnvMonID_Object = MibTableColumn
slp1EnvMonID = _Slp1EnvMonID_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 2),
    _Slp1EnvMonID_Type()
)
slp1EnvMonID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1EnvMonID.setStatus("current")


class _Slp1EnvMonName_Type(DisplayString):
    """Custom type slp1EnvMonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Slp1EnvMonName_Type.__name__ = "DisplayString"
_Slp1EnvMonName_Object = MibTableColumn
slp1EnvMonName = _Slp1EnvMonName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 3),
    _Slp1EnvMonName_Type()
)
slp1EnvMonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1EnvMonName.setStatus("current")


class _Slp1EnvMonStatus_Type(Integer32):
    """Custom type slp1EnvMonStatus based on Integer32"""
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


_Slp1EnvMonStatus_Type.__name__ = "Integer32"
_Slp1EnvMonStatus_Object = MibTableColumn
slp1EnvMonStatus = _Slp1EnvMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 4),
    _Slp1EnvMonStatus_Type()
)
slp1EnvMonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1EnvMonStatus.setStatus("current")


class _Slp1EnvMonWaterSensorName_Type(DisplayString):
    """Custom type slp1EnvMonWaterSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Slp1EnvMonWaterSensorName_Type.__name__ = "DisplayString"
_Slp1EnvMonWaterSensorName_Object = MibTableColumn
slp1EnvMonWaterSensorName = _Slp1EnvMonWaterSensorName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 5),
    _Slp1EnvMonWaterSensorName_Type()
)
slp1EnvMonWaterSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1EnvMonWaterSensorName.setStatus("current")


class _Slp1EnvMonWaterSensorStatus_Type(Integer32):
    """Custom type slp1EnvMonWaterSensorStatus based on Integer32"""
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


_Slp1EnvMonWaterSensorStatus_Type.__name__ = "Integer32"
_Slp1EnvMonWaterSensorStatus_Object = MibTableColumn
slp1EnvMonWaterSensorStatus = _Slp1EnvMonWaterSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 6),
    _Slp1EnvMonWaterSensorStatus_Type()
)
slp1EnvMonWaterSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1EnvMonWaterSensorStatus.setStatus("current")


class _Slp1EnvMonADCName_Type(DisplayString):
    """Custom type slp1EnvMonADCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Slp1EnvMonADCName_Type.__name__ = "DisplayString"
_Slp1EnvMonADCName_Object = MibTableColumn
slp1EnvMonADCName = _Slp1EnvMonADCName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 7),
    _Slp1EnvMonADCName_Type()
)
slp1EnvMonADCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1EnvMonADCName.setStatus("current")


class _Slp1EnvMonADCStatus_Type(Integer32):
    """Custom type slp1EnvMonADCStatus based on Integer32"""
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


_Slp1EnvMonADCStatus_Type.__name__ = "Integer32"
_Slp1EnvMonADCStatus_Object = MibTableColumn
slp1EnvMonADCStatus = _Slp1EnvMonADCStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 8),
    _Slp1EnvMonADCStatus_Type()
)
slp1EnvMonADCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1EnvMonADCStatus.setStatus("current")


class _Slp1EnvMonADCCount_Type(Integer32):
    """Custom type slp1EnvMonADCCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_Slp1EnvMonADCCount_Type.__name__ = "Integer32"
_Slp1EnvMonADCCount_Object = MibTableColumn
slp1EnvMonADCCount = _Slp1EnvMonADCCount_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 9),
    _Slp1EnvMonADCCount_Type()
)
slp1EnvMonADCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1EnvMonADCCount.setStatus("current")


class _Slp1EnvMonADCLowThresh_Type(Integer32):
    """Custom type slp1EnvMonADCLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Slp1EnvMonADCLowThresh_Type.__name__ = "Integer32"
_Slp1EnvMonADCLowThresh_Object = MibTableColumn
slp1EnvMonADCLowThresh = _Slp1EnvMonADCLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 10),
    _Slp1EnvMonADCLowThresh_Type()
)
slp1EnvMonADCLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1EnvMonADCLowThresh.setStatus("current")


class _Slp1EnvMonADCHighThresh_Type(Integer32):
    """Custom type slp1EnvMonADCHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Slp1EnvMonADCHighThresh_Type.__name__ = "Integer32"
_Slp1EnvMonADCHighThresh_Object = MibTableColumn
slp1EnvMonADCHighThresh = _Slp1EnvMonADCHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 11),
    _Slp1EnvMonADCHighThresh_Type()
)
slp1EnvMonADCHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1EnvMonADCHighThresh.setStatus("current")


class _Slp1EnvMonTempHumidSensorCount_Type(Integer32):
    """Custom type slp1EnvMonTempHumidSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Slp1EnvMonTempHumidSensorCount_Type.__name__ = "Integer32"
_Slp1EnvMonTempHumidSensorCount_Object = MibTableColumn
slp1EnvMonTempHumidSensorCount = _Slp1EnvMonTempHumidSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 12),
    _Slp1EnvMonTempHumidSensorCount_Type()
)
slp1EnvMonTempHumidSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1EnvMonTempHumidSensorCount.setStatus("current")


class _Slp1EnvMonContactClosureCount_Type(Integer32):
    """Custom type slp1EnvMonContactClosureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Slp1EnvMonContactClosureCount_Type.__name__ = "Integer32"
_Slp1EnvMonContactClosureCount_Object = MibTableColumn
slp1EnvMonContactClosureCount = _Slp1EnvMonContactClosureCount_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 4, 1, 13),
    _Slp1EnvMonContactClosureCount_Type()
)
slp1EnvMonContactClosureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1EnvMonContactClosureCount.setStatus("current")
_Slp1TempHumidSensorTable_Object = MibTable
slp1TempHumidSensorTable = _Slp1TempHumidSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5)
)
if mibBuilder.loadTexts:
    slp1TempHumidSensorTable.setStatus("current")
_Slp1TempHumidSensorEntry_Object = MibTableRow
slp1TempHumidSensorEntry = _Slp1TempHumidSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1)
)
slp1TempHumidSensorEntry.setIndexNames(
    (0, "SLP1-MIB", "slp1EnvMonIndex"),
    (0, "SLP1-MIB", "slp1TempHumidSensorIndex"),
)
if mibBuilder.loadTexts:
    slp1TempHumidSensorEntry.setStatus("current")


class _Slp1TempHumidSensorIndex_Type(Integer32):
    """Custom type slp1TempHumidSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Slp1TempHumidSensorIndex_Type.__name__ = "Integer32"
_Slp1TempHumidSensorIndex_Object = MibTableColumn
slp1TempHumidSensorIndex = _Slp1TempHumidSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 1),
    _Slp1TempHumidSensorIndex_Type()
)
slp1TempHumidSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slp1TempHumidSensorIndex.setStatus("current")


class _Slp1TempHumidSensorID_Type(DisplayString):
    """Custom type slp1TempHumidSensorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Slp1TempHumidSensorID_Type.__name__ = "DisplayString"
_Slp1TempHumidSensorID_Object = MibTableColumn
slp1TempHumidSensorID = _Slp1TempHumidSensorID_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 2),
    _Slp1TempHumidSensorID_Type()
)
slp1TempHumidSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TempHumidSensorID.setStatus("current")


class _Slp1TempHumidSensorName_Type(DisplayString):
    """Custom type slp1TempHumidSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Slp1TempHumidSensorName_Type.__name__ = "DisplayString"
_Slp1TempHumidSensorName_Object = MibTableColumn
slp1TempHumidSensorName = _Slp1TempHumidSensorName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 3),
    _Slp1TempHumidSensorName_Type()
)
slp1TempHumidSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1TempHumidSensorName.setStatus("current")


class _Slp1TempHumidSensorStatus_Type(Integer32):
    """Custom type slp1TempHumidSensorStatus based on Integer32"""
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


_Slp1TempHumidSensorStatus_Type.__name__ = "Integer32"
_Slp1TempHumidSensorStatus_Object = MibTableColumn
slp1TempHumidSensorStatus = _Slp1TempHumidSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 4),
    _Slp1TempHumidSensorStatus_Type()
)
slp1TempHumidSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TempHumidSensorStatus.setStatus("current")


class _Slp1TempHumidSensorTempStatus_Type(Integer32):
    """Custom type slp1TempHumidSensorTempStatus based on Integer32"""
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


_Slp1TempHumidSensorTempStatus_Type.__name__ = "Integer32"
_Slp1TempHumidSensorTempStatus_Object = MibTableColumn
slp1TempHumidSensorTempStatus = _Slp1TempHumidSensorTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 5),
    _Slp1TempHumidSensorTempStatus_Type()
)
slp1TempHumidSensorTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TempHumidSensorTempStatus.setStatus("current")


class _Slp1TempHumidSensorTempValue_Type(Integer32):
    """Custom type slp1TempHumidSensorTempValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1235),
    )


_Slp1TempHumidSensorTempValue_Type.__name__ = "Integer32"
_Slp1TempHumidSensorTempValue_Object = MibTableColumn
slp1TempHumidSensorTempValue = _Slp1TempHumidSensorTempValue_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 6),
    _Slp1TempHumidSensorTempValue_Type()
)
slp1TempHumidSensorTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TempHumidSensorTempValue.setStatus("current")
if mibBuilder.loadTexts:
    slp1TempHumidSensorTempValue.setUnits("tenth degrees Celsius")


class _Slp1TempHumidSensorTempLowThresh_Type(Integer32):
    """Custom type slp1TempHumidSensorTempLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 123),
    )


_Slp1TempHumidSensorTempLowThresh_Type.__name__ = "Integer32"
_Slp1TempHumidSensorTempLowThresh_Object = MibTableColumn
slp1TempHumidSensorTempLowThresh = _Slp1TempHumidSensorTempLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 7),
    _Slp1TempHumidSensorTempLowThresh_Type()
)
slp1TempHumidSensorTempLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1TempHumidSensorTempLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    slp1TempHumidSensorTempLowThresh.setUnits("degrees Celsius")


class _Slp1TempHumidSensorTempHighThresh_Type(Integer32):
    """Custom type slp1TempHumidSensorTempHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 123),
    )


_Slp1TempHumidSensorTempHighThresh_Type.__name__ = "Integer32"
_Slp1TempHumidSensorTempHighThresh_Object = MibTableColumn
slp1TempHumidSensorTempHighThresh = _Slp1TempHumidSensorTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 8),
    _Slp1TempHumidSensorTempHighThresh_Type()
)
slp1TempHumidSensorTempHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1TempHumidSensorTempHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    slp1TempHumidSensorTempHighThresh.setUnits("degrees Celsius")


class _Slp1TempHumidSensorHumidStatus_Type(Integer32):
    """Custom type slp1TempHumidSensorHumidStatus based on Integer32"""
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


_Slp1TempHumidSensorHumidStatus_Type.__name__ = "Integer32"
_Slp1TempHumidSensorHumidStatus_Object = MibTableColumn
slp1TempHumidSensorHumidStatus = _Slp1TempHumidSensorHumidStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 9),
    _Slp1TempHumidSensorHumidStatus_Type()
)
slp1TempHumidSensorHumidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TempHumidSensorHumidStatus.setStatus("current")


class _Slp1TempHumidSensorHumidValue_Type(Integer32):
    """Custom type slp1TempHumidSensorHumidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_Slp1TempHumidSensorHumidValue_Type.__name__ = "Integer32"
_Slp1TempHumidSensorHumidValue_Object = MibTableColumn
slp1TempHumidSensorHumidValue = _Slp1TempHumidSensorHumidValue_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 10),
    _Slp1TempHumidSensorHumidValue_Type()
)
slp1TempHumidSensorHumidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1TempHumidSensorHumidValue.setStatus("current")
if mibBuilder.loadTexts:
    slp1TempHumidSensorHumidValue.setUnits("percentage relative humidity")


class _Slp1TempHumidSensorHumidLowThresh_Type(Integer32):
    """Custom type slp1TempHumidSensorHumidLowThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Slp1TempHumidSensorHumidLowThresh_Type.__name__ = "Integer32"
_Slp1TempHumidSensorHumidLowThresh_Object = MibTableColumn
slp1TempHumidSensorHumidLowThresh = _Slp1TempHumidSensorHumidLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 11),
    _Slp1TempHumidSensorHumidLowThresh_Type()
)
slp1TempHumidSensorHumidLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1TempHumidSensorHumidLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    slp1TempHumidSensorHumidLowThresh.setUnits("percentage relative humidity")


class _Slp1TempHumidSensorHumidHighThresh_Type(Integer32):
    """Custom type slp1TempHumidSensorHumidHighThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Slp1TempHumidSensorHumidHighThresh_Type.__name__ = "Integer32"
_Slp1TempHumidSensorHumidHighThresh_Object = MibTableColumn
slp1TempHumidSensorHumidHighThresh = _Slp1TempHumidSensorHumidHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 5, 1, 12),
    _Slp1TempHumidSensorHumidHighThresh_Type()
)
slp1TempHumidSensorHumidHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1TempHumidSensorHumidHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    slp1TempHumidSensorHumidHighThresh.setUnits("percentage relative humidity")
_Slp1ContactClosureTable_Object = MibTable
slp1ContactClosureTable = _Slp1ContactClosureTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6)
)
if mibBuilder.loadTexts:
    slp1ContactClosureTable.setStatus("current")
_Slp1ContactClosureEntry_Object = MibTableRow
slp1ContactClosureEntry = _Slp1ContactClosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1)
)
slp1ContactClosureEntry.setIndexNames(
    (0, "SLP1-MIB", "slp1EnvMonIndex"),
    (0, "SLP1-MIB", "slp1ContactClosureIndex"),
)
if mibBuilder.loadTexts:
    slp1ContactClosureEntry.setStatus("current")


class _Slp1ContactClosureIndex_Type(Integer32):
    """Custom type slp1ContactClosureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Slp1ContactClosureIndex_Type.__name__ = "Integer32"
_Slp1ContactClosureIndex_Object = MibTableColumn
slp1ContactClosureIndex = _Slp1ContactClosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1, 1),
    _Slp1ContactClosureIndex_Type()
)
slp1ContactClosureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slp1ContactClosureIndex.setStatus("current")


class _Slp1ContactClosureID_Type(DisplayString):
    """Custom type slp1ContactClosureID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Slp1ContactClosureID_Type.__name__ = "DisplayString"
_Slp1ContactClosureID_Object = MibTableColumn
slp1ContactClosureID = _Slp1ContactClosureID_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1, 2),
    _Slp1ContactClosureID_Type()
)
slp1ContactClosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1ContactClosureID.setStatus("current")


class _Slp1ContactClosureName_Type(DisplayString):
    """Custom type slp1ContactClosureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Slp1ContactClosureName_Type.__name__ = "DisplayString"
_Slp1ContactClosureName_Object = MibTableColumn
slp1ContactClosureName = _Slp1ContactClosureName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1, 3),
    _Slp1ContactClosureName_Type()
)
slp1ContactClosureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slp1ContactClosureName.setStatus("current")


class _Slp1ContactClosureStatus_Type(Integer32):
    """Custom type slp1ContactClosureStatus based on Integer32"""
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


_Slp1ContactClosureStatus_Type.__name__ = "Integer32"
_Slp1ContactClosureStatus_Object = MibTableColumn
slp1ContactClosureStatus = _Slp1ContactClosureStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 2, 6, 1, 4),
    _Slp1ContactClosureStatus_Type()
)
slp1ContactClosureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slp1ContactClosureStatus.setStatus("current")
_Slp1Traps_ObjectIdentity = ObjectIdentity
slp1Traps = _Slp1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100)
)
_Slp1Events_ObjectIdentity = ObjectIdentity
slp1Events = _Slp1Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0)
)

# Managed Objects groups


# Notification objects

slp1TowerStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 1)
)
slp1TowerStatusEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1TowerID"),
        ("SLP1-MIB", "slp1TowerName"),
        ("SLP1-MIB", "slp1TowerStatus"))
)
if mibBuilder.loadTexts:
    slp1TowerStatusEvent.setStatus(
        "current"
    )

slp1InfeedStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 2)
)
slp1InfeedStatusEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1InfeedID"),
        ("SLP1-MIB", "slp1InfeedName"),
        ("SLP1-MIB", "slp1InfeedStatus"))
)
if mibBuilder.loadTexts:
    slp1InfeedStatusEvent.setStatus(
        "current"
    )

slp1InfeedLoadEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 3)
)
slp1InfeedLoadEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1InfeedID"),
        ("SLP1-MIB", "slp1InfeedName"),
        ("SLP1-MIB", "slp1InfeedLoadStatus"),
        ("SLP1-MIB", "slp1InfeedLoadValue"),
        ("SLP1-MIB", "slp1InfeedLoadHighThresh"))
)
if mibBuilder.loadTexts:
    slp1InfeedLoadEvent.setStatus(
        "current"
    )

slp1OutletStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 4)
)
slp1OutletStatusEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1OutletID"),
        ("SLP1-MIB", "slp1OutletName"),
        ("SLP1-MIB", "slp1OutletStatus"))
)
if mibBuilder.loadTexts:
    slp1OutletStatusEvent.setStatus(
        "current"
    )

slp1OutletLoadEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 5)
)
slp1OutletLoadEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1OutletID"),
        ("SLP1-MIB", "slp1OutletName"),
        ("SLP1-MIB", "slp1OutletLoadStatus"),
        ("SLP1-MIB", "slp1OutletLoadValue"),
        ("SLP1-MIB", "slp1OutletLoadLowThresh"),
        ("SLP1-MIB", "slp1OutletLoadHighThresh"))
)
if mibBuilder.loadTexts:
    slp1OutletLoadEvent.setStatus(
        "current"
    )

slp1OutletChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 6)
)
slp1OutletChangeEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1OutletID"),
        ("SLP1-MIB", "slp1OutletName"),
        ("SLP1-MIB", "slp1OutletStatus"),
        ("SLP1-MIB", "slp1OutletControlState"))
)
if mibBuilder.loadTexts:
    slp1OutletChangeEvent.setStatus(
        "current"
    )

slp1EnvMonStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 7)
)
slp1EnvMonStatusEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1EnvMonID"),
        ("SLP1-MIB", "slp1EnvMonName"),
        ("SLP1-MIB", "slp1EnvMonStatus"))
)
if mibBuilder.loadTexts:
    slp1EnvMonStatusEvent.setStatus(
        "current"
    )

slp1EnvMonWaterSensorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 8)
)
slp1EnvMonWaterSensorEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1EnvMonID"),
        ("SLP1-MIB", "slp1EnvMonWaterSensorName"),
        ("SLP1-MIB", "slp1EnvMonWaterSensorStatus"))
)
if mibBuilder.loadTexts:
    slp1EnvMonWaterSensorEvent.setStatus(
        "current"
    )

slp1EnvMonADCEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 9)
)
slp1EnvMonADCEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1EnvMonID"),
        ("SLP1-MIB", "slp1EnvMonADCName"),
        ("SLP1-MIB", "slp1EnvMonADCStatus"),
        ("SLP1-MIB", "slp1EnvMonADCCount"),
        ("SLP1-MIB", "slp1EnvMonADCLowThresh"),
        ("SLP1-MIB", "slp1EnvMonADCHighThresh"))
)
if mibBuilder.loadTexts:
    slp1EnvMonADCEvent.setStatus(
        "current"
    )

slp1TempHumidSensorStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 10)
)
slp1TempHumidSensorStatusEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1TempHumidSensorID"),
        ("SLP1-MIB", "slp1TempHumidSensorName"),
        ("SLP1-MIB", "slp1TempHumidSensorStatus"))
)
if mibBuilder.loadTexts:
    slp1TempHumidSensorStatusEvent.setStatus(
        "current"
    )

slp1TempHumidSensorTempEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 11)
)
slp1TempHumidSensorTempEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1TempHumidSensorID"),
        ("SLP1-MIB", "slp1TempHumidSensorName"),
        ("SLP1-MIB", "slp1TempHumidSensorTempStatus"),
        ("SLP1-MIB", "slp1TempHumidSensorTempValue"),
        ("SLP1-MIB", "slp1TempHumidSensorTempLowThresh"),
        ("SLP1-MIB", "slp1TempHumidSensorTempHighThresh"))
)
if mibBuilder.loadTexts:
    slp1TempHumidSensorTempEvent.setStatus(
        "current"
    )

slp1TempHumidSensorHumidEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 12)
)
slp1TempHumidSensorHumidEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1TempHumidSensorID"),
        ("SLP1-MIB", "slp1TempHumidSensorName"),
        ("SLP1-MIB", "slp1TempHumidSensorHumidStatus"),
        ("SLP1-MIB", "slp1TempHumidSensorHumidValue"),
        ("SLP1-MIB", "slp1TempHumidSensorHumidLowThresh"),
        ("SLP1-MIB", "slp1TempHumidSensorHumidHighThresh"))
)
if mibBuilder.loadTexts:
    slp1TempHumidSensorHumidEvent.setStatus(
        "current"
    )

slp1ContactClosureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 9, 1, 100, 0, 13)
)
slp1ContactClosureEvent.setObjects(
      *(("SLP1-MIB", "slp1SystemLocation"),
        ("SLP1-MIB", "slp1ContactClosureID"),
        ("SLP1-MIB", "slp1ContactClosureName"),
        ("SLP1-MIB", "slp1ContactClosureStatus"))
)
if mibBuilder.loadTexts:
    slp1ContactClosureEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLP1-MIB",
    **{"lantronix": lantronix,
       "products": products,
       "slp": slp,
       "slp1": slp1,
       "slp1SystemGroup": slp1SystemGroup,
       "slp1SystemVersion": slp1SystemVersion,
       "slp1SystemNICSerialNumber": slp1SystemNICSerialNumber,
       "slp1SystemLocation": slp1SystemLocation,
       "slp1SystemTowerCount": slp1SystemTowerCount,
       "slp1SystemEnvMonCount": slp1SystemEnvMonCount,
       "slp1SystemTables": slp1SystemTables,
       "slp1TowerTable": slp1TowerTable,
       "slp1TowerEntry": slp1TowerEntry,
       "slp1TowerIndex": slp1TowerIndex,
       "slp1TowerID": slp1TowerID,
       "slp1TowerName": slp1TowerName,
       "slp1TowerStatus": slp1TowerStatus,
       "slp1TowerInfeedCount": slp1TowerInfeedCount,
       "slp1InfeedTable": slp1InfeedTable,
       "slp1InfeedEntry": slp1InfeedEntry,
       "slp1InfeedIndex": slp1InfeedIndex,
       "slp1InfeedID": slp1InfeedID,
       "slp1InfeedName": slp1InfeedName,
       "slp1InfeedCapabilities": slp1InfeedCapabilities,
       "slp1InfeedStatus": slp1InfeedStatus,
       "slp1InfeedLoadStatus": slp1InfeedLoadStatus,
       "slp1InfeedLoadValue": slp1InfeedLoadValue,
       "slp1InfeedLoadHighThresh": slp1InfeedLoadHighThresh,
       "slp1InfeedOutletCount": slp1InfeedOutletCount,
       "slp1OutletTable": slp1OutletTable,
       "slp1OutletEntry": slp1OutletEntry,
       "slp1OutletIndex": slp1OutletIndex,
       "slp1OutletID": slp1OutletID,
       "slp1OutletName": slp1OutletName,
       "slp1OutletCapabilities": slp1OutletCapabilities,
       "slp1OutletStatus": slp1OutletStatus,
       "slp1OutletLoadStatus": slp1OutletLoadStatus,
       "slp1OutletLoadValue": slp1OutletLoadValue,
       "slp1OutletLoadLowThresh": slp1OutletLoadLowThresh,
       "slp1OutletLoadHighThresh": slp1OutletLoadHighThresh,
       "slp1OutletControlState": slp1OutletControlState,
       "slp1OutletControlAction": slp1OutletControlAction,
       "slp1EnvMonTable": slp1EnvMonTable,
       "slp1EnvMonEntry": slp1EnvMonEntry,
       "slp1EnvMonIndex": slp1EnvMonIndex,
       "slp1EnvMonID": slp1EnvMonID,
       "slp1EnvMonName": slp1EnvMonName,
       "slp1EnvMonStatus": slp1EnvMonStatus,
       "slp1EnvMonWaterSensorName": slp1EnvMonWaterSensorName,
       "slp1EnvMonWaterSensorStatus": slp1EnvMonWaterSensorStatus,
       "slp1EnvMonADCName": slp1EnvMonADCName,
       "slp1EnvMonADCStatus": slp1EnvMonADCStatus,
       "slp1EnvMonADCCount": slp1EnvMonADCCount,
       "slp1EnvMonADCLowThresh": slp1EnvMonADCLowThresh,
       "slp1EnvMonADCHighThresh": slp1EnvMonADCHighThresh,
       "slp1EnvMonTempHumidSensorCount": slp1EnvMonTempHumidSensorCount,
       "slp1EnvMonContactClosureCount": slp1EnvMonContactClosureCount,
       "slp1TempHumidSensorTable": slp1TempHumidSensorTable,
       "slp1TempHumidSensorEntry": slp1TempHumidSensorEntry,
       "slp1TempHumidSensorIndex": slp1TempHumidSensorIndex,
       "slp1TempHumidSensorID": slp1TempHumidSensorID,
       "slp1TempHumidSensorName": slp1TempHumidSensorName,
       "slp1TempHumidSensorStatus": slp1TempHumidSensorStatus,
       "slp1TempHumidSensorTempStatus": slp1TempHumidSensorTempStatus,
       "slp1TempHumidSensorTempValue": slp1TempHumidSensorTempValue,
       "slp1TempHumidSensorTempLowThresh": slp1TempHumidSensorTempLowThresh,
       "slp1TempHumidSensorTempHighThresh": slp1TempHumidSensorTempHighThresh,
       "slp1TempHumidSensorHumidStatus": slp1TempHumidSensorHumidStatus,
       "slp1TempHumidSensorHumidValue": slp1TempHumidSensorHumidValue,
       "slp1TempHumidSensorHumidLowThresh": slp1TempHumidSensorHumidLowThresh,
       "slp1TempHumidSensorHumidHighThresh": slp1TempHumidSensorHumidHighThresh,
       "slp1ContactClosureTable": slp1ContactClosureTable,
       "slp1ContactClosureEntry": slp1ContactClosureEntry,
       "slp1ContactClosureIndex": slp1ContactClosureIndex,
       "slp1ContactClosureID": slp1ContactClosureID,
       "slp1ContactClosureName": slp1ContactClosureName,
       "slp1ContactClosureStatus": slp1ContactClosureStatus,
       "slp1Traps": slp1Traps,
       "slp1Events": slp1Events,
       "slp1TowerStatusEvent": slp1TowerStatusEvent,
       "slp1InfeedStatusEvent": slp1InfeedStatusEvent,
       "slp1InfeedLoadEvent": slp1InfeedLoadEvent,
       "slp1OutletStatusEvent": slp1OutletStatusEvent,
       "slp1OutletLoadEvent": slp1OutletLoadEvent,
       "slp1OutletChangeEvent": slp1OutletChangeEvent,
       "slp1EnvMonStatusEvent": slp1EnvMonStatusEvent,
       "slp1EnvMonWaterSensorEvent": slp1EnvMonWaterSensorEvent,
       "slp1EnvMonADCEvent": slp1EnvMonADCEvent,
       "slp1TempHumidSensorStatusEvent": slp1TempHumidSensorStatusEvent,
       "slp1TempHumidSensorTempEvent": slp1TempHumidSensorTempEvent,
       "slp1TempHumidSensorHumidEvent": slp1TempHumidSensorHumidEvent,
       "slp1ContactClosureEvent": slp1ContactClosureEvent}
)
