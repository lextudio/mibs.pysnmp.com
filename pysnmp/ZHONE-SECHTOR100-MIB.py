# SNMP MIB module (ZHONE-SECHTOR100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-SECHTOR100-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:44 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(sechtor100,
 zhoneModules,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "sechtor100",
    "zhoneModules",
    "zhoneShelfIndex",
    "zhoneSlotIndex")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneSechtor100 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 19)
)
zhoneSechtor100.setRevisions(
        ("2001-09-28 10:29",
         "2000-12-27 11:17",
         "2000-12-21 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sechtor100Environment_ObjectIdentity = ObjectIdentity
sechtor100Environment = _Sechtor100Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sechtor100Environment.setStatus("deprecated")


class _S100FanOperationalStatus_Type(Integer32):
    """Custom type s100FanOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fanFailure", 2),
          ("operational", 1))
    )


_S100FanOperationalStatus_Type.__name__ = "Integer32"
_S100FanOperationalStatus_Object = MibScalar
s100FanOperationalStatus = _S100FanOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1, 1),
    _S100FanOperationalStatus_Type()
)
s100FanOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s100FanOperationalStatus.setStatus("deprecated")


class _S100ThermoAUpperThreshold_Type(Integer32):
    """Custom type s100ThermoAUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 80),
    )


_S100ThermoAUpperThreshold_Type.__name__ = "Integer32"
_S100ThermoAUpperThreshold_Object = MibScalar
s100ThermoAUpperThreshold = _S100ThermoAUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1, 2),
    _S100ThermoAUpperThreshold_Type()
)
s100ThermoAUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s100ThermoAUpperThreshold.setStatus("deprecated")


class _S100ThermoBUpperThreshold_Type(Integer32):
    """Custom type s100ThermoBUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 80),
    )


_S100ThermoBUpperThreshold_Type.__name__ = "Integer32"
_S100ThermoBUpperThreshold_Object = MibScalar
s100ThermoBUpperThreshold = _S100ThermoBUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1, 3),
    _S100ThermoBUpperThreshold_Type()
)
s100ThermoBUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s100ThermoBUpperThreshold.setStatus("deprecated")


class _S10ThermoALowerThreshold_Type(Integer32):
    """Custom type s10ThermoALowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 5),
    )


_S10ThermoALowerThreshold_Type.__name__ = "Integer32"
_S10ThermoALowerThreshold_Object = MibScalar
s10ThermoALowerThreshold = _S10ThermoALowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1, 4),
    _S10ThermoALowerThreshold_Type()
)
s10ThermoALowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s10ThermoALowerThreshold.setStatus("deprecated")


class _S100ThermoBLowerThreshold_Type(Integer32):
    """Custom type s100ThermoBLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 5),
    )


_S100ThermoBLowerThreshold_Type.__name__ = "Integer32"
_S100ThermoBLowerThreshold_Object = MibScalar
s100ThermoBLowerThreshold = _S100ThermoBLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1, 5),
    _S100ThermoBLowerThreshold_Type()
)
s100ThermoBLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s100ThermoBLowerThreshold.setStatus("deprecated")


class _S100ThermoATemperature_Type(Integer32):
    """Custom type s100ThermoATemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 125),
    )


_S100ThermoATemperature_Type.__name__ = "Integer32"
_S100ThermoATemperature_Object = MibScalar
s100ThermoATemperature = _S100ThermoATemperature_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1, 6),
    _S100ThermoATemperature_Type()
)
s100ThermoATemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s100ThermoATemperature.setStatus("deprecated")


class _S100ThermoBTemperature_Type(Integer32):
    """Custom type s100ThermoBTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 125),
    )


_S100ThermoBTemperature_Type.__name__ = "Integer32"
_S100ThermoBTemperature_Object = MibScalar
s100ThermoBTemperature = _S100ThermoBTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1, 7),
    _S100ThermoBTemperature_Type()
)
s100ThermoBTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s100ThermoBTemperature.setStatus("deprecated")


class _S100ThermoAOperationalStatus_Type(Integer32):
    """Custom type s100ThermoAOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("belowLowerThreshold", 3),
          ("overUpperThreshold", 2),
          ("withinOperationalRange", 1))
    )


_S100ThermoAOperationalStatus_Type.__name__ = "Integer32"
_S100ThermoAOperationalStatus_Object = MibScalar
s100ThermoAOperationalStatus = _S100ThermoAOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1, 8),
    _S100ThermoAOperationalStatus_Type()
)
s100ThermoAOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s100ThermoAOperationalStatus.setStatus("deprecated")


class _S100ThermoBOperationalStatus_Type(Integer32):
    """Custom type s100ThermoBOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("belowLowerThreshold", 3),
          ("overUpperThreshold", 2),
          ("withinOperationalRange", 1))
    )


_S100ThermoBOperationalStatus_Type.__name__ = "Integer32"
_S100ThermoBOperationalStatus_Object = MibScalar
s100ThermoBOperationalStatus = _S100ThermoBOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 1, 9),
    _S100ThermoBOperationalStatus_Type()
)
s100ThermoBOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s100ThermoBOperationalStatus.setStatus("deprecated")
_Sechtor100Traps_ObjectIdentity = ObjectIdentity
sechtor100Traps = _Sechtor100Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    sechtor100Traps.setStatus("current")
_Sechtor100TrapsPrefix_ObjectIdentity = ObjectIdentity
sechtor100TrapsPrefix = _Sechtor100TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 2, 0)
)
if mibBuilder.loadTexts:
    sechtor100TrapsPrefix.setStatus("current")
_Sechtor100ConfigTable_Object = MibTable
sechtor100ConfigTable = _Sechtor100ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    sechtor100ConfigTable.setStatus("current")
_Sechtor100ConfigEntry_Object = MibTableRow
sechtor100ConfigEntry = _Sechtor100ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1)
)
sechtor100ConfigEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    sechtor100ConfigEntry.setStatus("current")
_Sechtor100PeerMacAddress_Type = MacAddress
_Sechtor100PeerMacAddress_Object = MibTableColumn
sechtor100PeerMacAddress = _Sechtor100PeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 1),
    _Sechtor100PeerMacAddress_Type()
)
sechtor100PeerMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sechtor100PeerMacAddress.setStatus("current")
_Sechtor100RedundancyEnable_Type = TruthValue
_Sechtor100RedundancyEnable_Object = MibTableColumn
sechtor100RedundancyEnable = _Sechtor100RedundancyEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 2),
    _Sechtor100RedundancyEnable_Type()
)
sechtor100RedundancyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sechtor100RedundancyEnable.setStatus("current")


class _Sechtor100FanOperationalStatus_Type(Integer32):
    """Custom type sechtor100FanOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fanFailure", 2),
          ("operational", 1))
    )


_Sechtor100FanOperationalStatus_Type.__name__ = "Integer32"
_Sechtor100FanOperationalStatus_Object = MibTableColumn
sechtor100FanOperationalStatus = _Sechtor100FanOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 3),
    _Sechtor100FanOperationalStatus_Type()
)
sechtor100FanOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sechtor100FanOperationalStatus.setStatus("current")


class _Sechtor100ThermoAUpperThreshold_Type(Integer32):
    """Custom type sechtor100ThermoAUpperThreshold based on Integer32"""
    defaultValue = 65

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 80),
    )


_Sechtor100ThermoAUpperThreshold_Type.__name__ = "Integer32"
_Sechtor100ThermoAUpperThreshold_Object = MibTableColumn
sechtor100ThermoAUpperThreshold = _Sechtor100ThermoAUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 4),
    _Sechtor100ThermoAUpperThreshold_Type()
)
sechtor100ThermoAUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sechtor100ThermoAUpperThreshold.setStatus("current")


class _Sechtor100ThermoBUpperThreshold_Type(Integer32):
    """Custom type sechtor100ThermoBUpperThreshold based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 80),
    )


_Sechtor100ThermoBUpperThreshold_Type.__name__ = "Integer32"
_Sechtor100ThermoBUpperThreshold_Object = MibTableColumn
sechtor100ThermoBUpperThreshold = _Sechtor100ThermoBUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 5),
    _Sechtor100ThermoBUpperThreshold_Type()
)
sechtor100ThermoBUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sechtor100ThermoBUpperThreshold.setStatus("current")


class _Sechtor100ThermoALowerThreshold_Type(Integer32):
    """Custom type sechtor100ThermoALowerThreshold based on Integer32"""
    defaultValue = -5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 5),
    )


_Sechtor100ThermoALowerThreshold_Type.__name__ = "Integer32"
_Sechtor100ThermoALowerThreshold_Object = MibTableColumn
sechtor100ThermoALowerThreshold = _Sechtor100ThermoALowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 6),
    _Sechtor100ThermoALowerThreshold_Type()
)
sechtor100ThermoALowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sechtor100ThermoALowerThreshold.setStatus("current")


class _Sechtor100ThermoBLowerThreshold_Type(Integer32):
    """Custom type sechtor100ThermoBLowerThreshold based on Integer32"""
    defaultValue = -5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 5),
    )


_Sechtor100ThermoBLowerThreshold_Type.__name__ = "Integer32"
_Sechtor100ThermoBLowerThreshold_Object = MibTableColumn
sechtor100ThermoBLowerThreshold = _Sechtor100ThermoBLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 7),
    _Sechtor100ThermoBLowerThreshold_Type()
)
sechtor100ThermoBLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sechtor100ThermoBLowerThreshold.setStatus("current")


class _Sechtor100ThermoATemperature_Type(Integer32):
    """Custom type sechtor100ThermoATemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 125),
    )


_Sechtor100ThermoATemperature_Type.__name__ = "Integer32"
_Sechtor100ThermoATemperature_Object = MibTableColumn
sechtor100ThermoATemperature = _Sechtor100ThermoATemperature_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 8),
    _Sechtor100ThermoATemperature_Type()
)
sechtor100ThermoATemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sechtor100ThermoATemperature.setStatus("current")


class _Sechtor100ThermoBTemperature_Type(Integer32):
    """Custom type sechtor100ThermoBTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, 125),
    )


_Sechtor100ThermoBTemperature_Type.__name__ = "Integer32"
_Sechtor100ThermoBTemperature_Object = MibTableColumn
sechtor100ThermoBTemperature = _Sechtor100ThermoBTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 9),
    _Sechtor100ThermoBTemperature_Type()
)
sechtor100ThermoBTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sechtor100ThermoBTemperature.setStatus("current")


class _Sechtor100ThermoAOperationalStatus_Type(Integer32):
    """Custom type sechtor100ThermoAOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("belowLowerThreshold", 3),
          ("overUpperThreshold", 2),
          ("withinOperationalRange", 1))
    )


_Sechtor100ThermoAOperationalStatus_Type.__name__ = "Integer32"
_Sechtor100ThermoAOperationalStatus_Object = MibTableColumn
sechtor100ThermoAOperationalStatus = _Sechtor100ThermoAOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 10),
    _Sechtor100ThermoAOperationalStatus_Type()
)
sechtor100ThermoAOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sechtor100ThermoAOperationalStatus.setStatus("current")


class _Sechtor100ThermoBOperationalStatus_Type(Integer32):
    """Custom type sechtor100ThermoBOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("belowLowerThreshold", 3),
          ("overUpperThreshold", 2),
          ("withinOperationalRange", 1))
    )


_Sechtor100ThermoBOperationalStatus_Type.__name__ = "Integer32"
_Sechtor100ThermoBOperationalStatus_Object = MibTableColumn
sechtor100ThermoBOperationalStatus = _Sechtor100ThermoBOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 11),
    _Sechtor100ThermoBOperationalStatus_Type()
)
sechtor100ThermoBOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sechtor100ThermoBOperationalStatus.setStatus("current")
_Sechtor100RowStatus_Type = ZhoneRowStatus
_Sechtor100RowStatus_Object = MibTableColumn
sechtor100RowStatus = _Sechtor100RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 3, 1, 12),
    _Sechtor100RowStatus_Type()
)
sechtor100RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sechtor100RowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

s100FanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 2, 0, 1)
)
s100FanStatusChange.setObjects(
    ("ZHONE-SECHTOR100-MIB", "s100FanOperationalStatus")
)
if mibBuilder.loadTexts:
    s100FanStatusChange.setStatus(
        "deprecated"
    )

s100ThermoStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 2, 0, 2)
)
s100ThermoStatusChange.setObjects(
      *(("ZHONE-SECHTOR100-MIB", "s100ThermoATemperature"),
        ("ZHONE-SECHTOR100-MIB", "s100ThermoBTemperature"),
        ("ZHONE-SECHTOR100-MIB", "s100ThermoAOperationalStatus"),
        ("ZHONE-SECHTOR100-MIB", "s100ThermoBOperationalStatus"))
)
if mibBuilder.loadTexts:
    s100ThermoStatusChange.setStatus(
        "deprecated"
    )

sechtor100FanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 2, 0, 3)
)
sechtor100FanStatusChange.setObjects(
    ("ZHONE-SECHTOR100-MIB", "sechtor100FanOperationalStatus")
)
if mibBuilder.loadTexts:
    sechtor100FanStatusChange.setStatus(
        "current"
    )

sechtor100ThermoStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 1, 2, 0, 4)
)
sechtor100ThermoStatusChange.setObjects(
      *(("ZHONE-SECHTOR100-MIB", "sechtor100ThermoATemperature"),
        ("ZHONE-SECHTOR100-MIB", "sechtor100ThermoBTemperature"),
        ("ZHONE-SECHTOR100-MIB", "sechtor100ThermoAOperationalStatus"),
        ("ZHONE-SECHTOR100-MIB", "sechtor100ThermoBOperationalStatus"))
)
if mibBuilder.loadTexts:
    sechtor100ThermoStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-SECHTOR100-MIB",
    **{"sechtor100Environment": sechtor100Environment,
       "s100FanOperationalStatus": s100FanOperationalStatus,
       "s100ThermoAUpperThreshold": s100ThermoAUpperThreshold,
       "s100ThermoBUpperThreshold": s100ThermoBUpperThreshold,
       "s10ThermoALowerThreshold": s10ThermoALowerThreshold,
       "s100ThermoBLowerThreshold": s100ThermoBLowerThreshold,
       "s100ThermoATemperature": s100ThermoATemperature,
       "s100ThermoBTemperature": s100ThermoBTemperature,
       "s100ThermoAOperationalStatus": s100ThermoAOperationalStatus,
       "s100ThermoBOperationalStatus": s100ThermoBOperationalStatus,
       "sechtor100Traps": sechtor100Traps,
       "sechtor100TrapsPrefix": sechtor100TrapsPrefix,
       "s100FanStatusChange": s100FanStatusChange,
       "s100ThermoStatusChange": s100ThermoStatusChange,
       "sechtor100FanStatusChange": sechtor100FanStatusChange,
       "sechtor100ThermoStatusChange": sechtor100ThermoStatusChange,
       "sechtor100ConfigTable": sechtor100ConfigTable,
       "sechtor100ConfigEntry": sechtor100ConfigEntry,
       "sechtor100PeerMacAddress": sechtor100PeerMacAddress,
       "sechtor100RedundancyEnable": sechtor100RedundancyEnable,
       "sechtor100FanOperationalStatus": sechtor100FanOperationalStatus,
       "sechtor100ThermoAUpperThreshold": sechtor100ThermoAUpperThreshold,
       "sechtor100ThermoBUpperThreshold": sechtor100ThermoBUpperThreshold,
       "sechtor100ThermoALowerThreshold": sechtor100ThermoALowerThreshold,
       "sechtor100ThermoBLowerThreshold": sechtor100ThermoBLowerThreshold,
       "sechtor100ThermoATemperature": sechtor100ThermoATemperature,
       "sechtor100ThermoBTemperature": sechtor100ThermoBTemperature,
       "sechtor100ThermoAOperationalStatus": sechtor100ThermoAOperationalStatus,
       "sechtor100ThermoBOperationalStatus": sechtor100ThermoBOperationalStatus,
       "sechtor100RowStatus": sechtor100RowStatus,
       "zhoneSechtor100": zhoneSechtor100}
)
