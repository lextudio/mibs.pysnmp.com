# SNMP MIB module (OMNI-gx2RFA1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2RFA1000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:30 2024
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

(gx2Rfa1000,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Rfa1000")

(trapChangedObjectId,
 trapChangedValueDisplayString,
 trapChangedValueInteger,
 trapIdentifier,
 trapNETrapLastTrapTimeStamp,
 trapNetworkElemAdminState,
 trapNetworkElemAlarmStatus,
 trapNetworkElemAvailStatus,
 trapNetworkElemModelNumber,
 trapNetworkElemOperState,
 trapNetworkElemSerialNum,
 trapPerceivedSeverity,
 trapText) = mibBuilder.importSymbols(
    "NLSBBN-TRAPS-MIB",
    "trapChangedObjectId",
    "trapChangedValueDisplayString",
    "trapChangedValueInteger",
    "trapIdentifier",
    "trapNETrapLastTrapTimeStamp",
    "trapNetworkElemAdminState",
    "trapNetworkElemAlarmStatus",
    "trapNetworkElemAvailStatus",
    "trapNetworkElemModelNumber",
    "trapNetworkElemOperState",
    "trapNetworkElemSerialNum",
    "trapPerceivedSeverity",
    "trapText")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Float(Counter32):
    """Custom type Float based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gx2Rfa1000Descriptor_ObjectIdentity = ObjectIdentity
gx2Rfa1000Descriptor = _Gx2Rfa1000Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 1)
)
_Gx2Rfa1000AnalogTable_Object = MibTable
gx2Rfa1000AnalogTable = _Gx2Rfa1000AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2)
)
if mibBuilder.loadTexts:
    gx2Rfa1000AnalogTable.setStatus("mandatory")
_Gx2Rfa1000AnalogEntry_Object = MibTableRow
gx2Rfa1000AnalogEntry = _Gx2Rfa1000AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1)
)
gx2Rfa1000AnalogEntry.setIndexNames(
    (0, "OMNI-gx2RFA1000-MIB", "rfagx2Rfa1000AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rfa1000AnalogEntry.setStatus("mandatory")


class _Rfagx2Rfa1000AnalogTableIndex_Type(Integer32):
    """Custom type rfagx2Rfa1000AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Rfagx2Rfa1000AnalogTableIndex_Type.__name__ = "Integer32"
_Rfagx2Rfa1000AnalogTableIndex_Object = MibTableColumn
rfagx2Rfa1000AnalogTableIndex = _Rfagx2Rfa1000AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 1),
    _Rfagx2Rfa1000AnalogTableIndex_Type()
)
rfagx2Rfa1000AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfagx2Rfa1000AnalogTableIndex.setStatus("mandatory")


class _RfalabelModTemp_Type(DisplayString):
    """Custom type rfalabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelModTemp_Type.__name__ = "DisplayString"
_RfalabelModTemp_Object = MibTableColumn
rfalabelModTemp = _RfalabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 2),
    _RfalabelModTemp_Type()
)
rfalabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelModTemp.setStatus("optional")


class _RfauomModTemp_Type(DisplayString):
    """Custom type rfauomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfauomModTemp_Type.__name__ = "DisplayString"
_RfauomModTemp_Object = MibTableColumn
rfauomModTemp = _RfauomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 3),
    _RfauomModTemp_Type()
)
rfauomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfauomModTemp.setStatus("optional")
_RfamajorHighModTemp_Type = Float
_RfamajorHighModTemp_Object = MibTableColumn
rfamajorHighModTemp = _RfamajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 4),
    _RfamajorHighModTemp_Type()
)
rfamajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfamajorHighModTemp.setStatus("mandatory")
_RfamajorLowModTemp_Type = Float
_RfamajorLowModTemp_Object = MibTableColumn
rfamajorLowModTemp = _RfamajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 5),
    _RfamajorLowModTemp_Type()
)
rfamajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfamajorLowModTemp.setStatus("mandatory")
_RfaminorHighModTemp_Type = Float
_RfaminorHighModTemp_Object = MibTableColumn
rfaminorHighModTemp = _RfaminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 6),
    _RfaminorHighModTemp_Type()
)
rfaminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaminorHighModTemp.setStatus("mandatory")
_RfaminorLowModTemp_Type = Float
_RfaminorLowModTemp_Object = MibTableColumn
rfaminorLowModTemp = _RfaminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 7),
    _RfaminorLowModTemp_Type()
)
rfaminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaminorLowModTemp.setStatus("mandatory")
_RfacurrentValueModTemp_Type = Float
_RfacurrentValueModTemp_Object = MibTableColumn
rfacurrentValueModTemp = _RfacurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 8),
    _RfacurrentValueModTemp_Type()
)
rfacurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfacurrentValueModTemp.setStatus("mandatory")


class _RfastateFlagModTemp_Type(Integer32):
    """Custom type rfastateFlagModTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateFlagModTemp_Type.__name__ = "Integer32"
_RfastateFlagModTemp_Object = MibTableColumn
rfastateFlagModTemp = _RfastateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 9),
    _RfastateFlagModTemp_Type()
)
rfastateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateFlagModTemp.setStatus("mandatory")
_RfaminValueModTemp_Type = Float
_RfaminValueModTemp_Object = MibTableColumn
rfaminValueModTemp = _RfaminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 10),
    _RfaminValueModTemp_Type()
)
rfaminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaminValueModTemp.setStatus("mandatory")
_RfamaxValueModTemp_Type = Float
_RfamaxValueModTemp_Object = MibTableColumn
rfamaxValueModTemp = _RfamaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 11),
    _RfamaxValueModTemp_Type()
)
rfamaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfamaxValueModTemp.setStatus("mandatory")


class _RfaalarmStateModTemp_Type(Integer32):
    """Custom type rfaalarmStateModTemp based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_RfaalarmStateModTemp_Type.__name__ = "Integer32"
_RfaalarmStateModTemp_Object = MibTableColumn
rfaalarmStateModTemp = _RfaalarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 12),
    _RfaalarmStateModTemp_Type()
)
rfaalarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaalarmStateModTemp.setStatus("mandatory")


class _RfalabelFanCurrent_Type(DisplayString):
    """Custom type rfalabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelFanCurrent_Type.__name__ = "DisplayString"
_RfalabelFanCurrent_Object = MibTableColumn
rfalabelFanCurrent = _RfalabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 13),
    _RfalabelFanCurrent_Type()
)
rfalabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelFanCurrent.setStatus("optional")


class _RfauomFanCurrent_Type(DisplayString):
    """Custom type rfauomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfauomFanCurrent_Type.__name__ = "DisplayString"
_RfauomFanCurrent_Object = MibTableColumn
rfauomFanCurrent = _RfauomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 14),
    _RfauomFanCurrent_Type()
)
rfauomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfauomFanCurrent.setStatus("optional")
_RfamajorHighFanCurrent_Type = Float
_RfamajorHighFanCurrent_Object = MibTableColumn
rfamajorHighFanCurrent = _RfamajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 15),
    _RfamajorHighFanCurrent_Type()
)
rfamajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfamajorHighFanCurrent.setStatus("mandatory")
_RfamajorLowFanCurrent_Type = Float
_RfamajorLowFanCurrent_Object = MibTableColumn
rfamajorLowFanCurrent = _RfamajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 16),
    _RfamajorLowFanCurrent_Type()
)
rfamajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfamajorLowFanCurrent.setStatus("mandatory")
_RfaminorHighFanCurrent_Type = Float
_RfaminorHighFanCurrent_Object = MibTableColumn
rfaminorHighFanCurrent = _RfaminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 17),
    _RfaminorHighFanCurrent_Type()
)
rfaminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaminorHighFanCurrent.setStatus("obsolete")
_RfaminorLowFanCurrent_Type = Float
_RfaminorLowFanCurrent_Object = MibTableColumn
rfaminorLowFanCurrent = _RfaminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 18),
    _RfaminorLowFanCurrent_Type()
)
rfaminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaminorLowFanCurrent.setStatus("obsolete")
_RfacurrentValueFanCurrent_Type = Float
_RfacurrentValueFanCurrent_Object = MibTableColumn
rfacurrentValueFanCurrent = _RfacurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 19),
    _RfacurrentValueFanCurrent_Type()
)
rfacurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfacurrentValueFanCurrent.setStatus("mandatory")


class _RfastateFlagFanCurrent_Type(Integer32):
    """Custom type rfastateFlagFanCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateFlagFanCurrent_Type.__name__ = "Integer32"
_RfastateFlagFanCurrent_Object = MibTableColumn
rfastateFlagFanCurrent = _RfastateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 20),
    _RfastateFlagFanCurrent_Type()
)
rfastateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateFlagFanCurrent.setStatus("mandatory")
_RfaminValueFanCurrent_Type = Float
_RfaminValueFanCurrent_Object = MibTableColumn
rfaminValueFanCurrent = _RfaminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 21),
    _RfaminValueFanCurrent_Type()
)
rfaminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaminValueFanCurrent.setStatus("mandatory")
_RfamaxValueFanCurrent_Type = Float
_RfamaxValueFanCurrent_Object = MibTableColumn
rfamaxValueFanCurrent = _RfamaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 22),
    _RfamaxValueFanCurrent_Type()
)
rfamaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfamaxValueFanCurrent.setStatus("mandatory")


class _RfaalarmStateFanCurrent_Type(Integer32):
    """Custom type rfaalarmStateFanCurrent based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_RfaalarmStateFanCurrent_Type.__name__ = "Integer32"
_RfaalarmStateFanCurrent_Object = MibTableColumn
rfaalarmStateFanCurrent = _RfaalarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 23),
    _RfaalarmStateFanCurrent_Type()
)
rfaalarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaalarmStateFanCurrent.setStatus("mandatory")


class _Rfalabel12Volt_Type(DisplayString):
    """Custom type rfalabel12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rfalabel12Volt_Type.__name__ = "DisplayString"
_Rfalabel12Volt_Object = MibTableColumn
rfalabel12Volt = _Rfalabel12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 24),
    _Rfalabel12Volt_Type()
)
rfalabel12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabel12Volt.setStatus("optional")


class _Rfauom12Volt_Type(DisplayString):
    """Custom type rfauom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rfauom12Volt_Type.__name__ = "DisplayString"
_Rfauom12Volt_Object = MibTableColumn
rfauom12Volt = _Rfauom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 25),
    _Rfauom12Volt_Type()
)
rfauom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfauom12Volt.setStatus("optional")
_RfamajorHigh12Volt_Type = Float
_RfamajorHigh12Volt_Object = MibTableColumn
rfamajorHigh12Volt = _RfamajorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 26),
    _RfamajorHigh12Volt_Type()
)
rfamajorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfamajorHigh12Volt.setStatus("mandatory")
_RfamajorLow12Volt_Type = Float
_RfamajorLow12Volt_Object = MibTableColumn
rfamajorLow12Volt = _RfamajorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 27),
    _RfamajorLow12Volt_Type()
)
rfamajorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfamajorLow12Volt.setStatus("mandatory")
_RfaminorHigh12Volt_Type = Float
_RfaminorHigh12Volt_Object = MibTableColumn
rfaminorHigh12Volt = _RfaminorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 28),
    _RfaminorHigh12Volt_Type()
)
rfaminorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaminorHigh12Volt.setStatus("mandatory")
_RfaminorLow12Volt_Type = Float
_RfaminorLow12Volt_Object = MibTableColumn
rfaminorLow12Volt = _RfaminorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 29),
    _RfaminorLow12Volt_Type()
)
rfaminorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaminorLow12Volt.setStatus("mandatory")
_RfacurrentValue12Volt_Type = Float
_RfacurrentValue12Volt_Object = MibTableColumn
rfacurrentValue12Volt = _RfacurrentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 30),
    _RfacurrentValue12Volt_Type()
)
rfacurrentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfacurrentValue12Volt.setStatus("mandatory")


class _RfastateFlag12Volt_Type(Integer32):
    """Custom type rfastateFlag12Volt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateFlag12Volt_Type.__name__ = "Integer32"
_RfastateFlag12Volt_Object = MibTableColumn
rfastateFlag12Volt = _RfastateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 31),
    _RfastateFlag12Volt_Type()
)
rfastateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateFlag12Volt.setStatus("mandatory")
_RfaminValue12Volt_Type = Float
_RfaminValue12Volt_Object = MibTableColumn
rfaminValue12Volt = _RfaminValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 32),
    _RfaminValue12Volt_Type()
)
rfaminValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaminValue12Volt.setStatus("mandatory")
_RfamaxValue12Volt_Type = Float
_RfamaxValue12Volt_Object = MibTableColumn
rfamaxValue12Volt = _RfamaxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 33),
    _RfamaxValue12Volt_Type()
)
rfamaxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfamaxValue12Volt.setStatus("mandatory")


class _RfaalarmState12Volt_Type(Integer32):
    """Custom type rfaalarmState12Volt based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_RfaalarmState12Volt_Type.__name__ = "Integer32"
_RfaalarmState12Volt_Object = MibTableColumn
rfaalarmState12Volt = _RfaalarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 2, 1, 34),
    _RfaalarmState12Volt_Type()
)
rfaalarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaalarmState12Volt.setStatus("mandatory")
_Gx2Rfa1000DigitalTable_Object = MibTable
gx2Rfa1000DigitalTable = _Gx2Rfa1000DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3)
)
if mibBuilder.loadTexts:
    gx2Rfa1000DigitalTable.setStatus("mandatory")
_Gx2Rfa1000DigitalEntry_Object = MibTableRow
gx2Rfa1000DigitalEntry = _Gx2Rfa1000DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2)
)
gx2Rfa1000DigitalEntry.setIndexNames(
    (0, "OMNI-gx2RFA1000-MIB", "rfagx2Rfa1000DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rfa1000DigitalEntry.setStatus("mandatory")


class _Rfagx2Rfa1000DigitalTableIndex_Type(Integer32):
    """Custom type rfagx2Rfa1000DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Rfagx2Rfa1000DigitalTableIndex_Type.__name__ = "Integer32"
_Rfagx2Rfa1000DigitalTableIndex_Object = MibTableColumn
rfagx2Rfa1000DigitalTableIndex = _Rfagx2Rfa1000DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 1),
    _Rfagx2Rfa1000DigitalTableIndex_Type()
)
rfagx2Rfa1000DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfagx2Rfa1000DigitalTableIndex.setStatus("mandatory")


class _RfalabelSlopeSetting_Type(DisplayString):
    """Custom type rfalabelSlopeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelSlopeSetting_Type.__name__ = "DisplayString"
_RfalabelSlopeSetting_Object = MibTableColumn
rfalabelSlopeSetting = _RfalabelSlopeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 2),
    _RfalabelSlopeSetting_Type()
)
rfalabelSlopeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelSlopeSetting.setStatus("optional")


class _RfaenumSlopeSetting_Type(DisplayString):
    """Custom type rfaenumSlopeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfaenumSlopeSetting_Type.__name__ = "DisplayString"
_RfaenumSlopeSetting_Object = MibTableColumn
rfaenumSlopeSetting = _RfaenumSlopeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 3),
    _RfaenumSlopeSetting_Type()
)
rfaenumSlopeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaenumSlopeSetting.setStatus("optional")


class _RfavalueSlopeSetting_Type(Integer32):
    """Custom type rfavalueSlopeSetting based on Integer32"""
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
        *(("db1point0", 1),
          ("db1point5", 2),
          ("db2point0", 3),
          ("db2point5", 4),
          ("db3point0", 5),
          ("db3point5", 6),
          ("db4point0", 7))
    )


_RfavalueSlopeSetting_Type.__name__ = "Integer32"
_RfavalueSlopeSetting_Object = MibTableColumn
rfavalueSlopeSetting = _RfavalueSlopeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 4),
    _RfavalueSlopeSetting_Type()
)
rfavalueSlopeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfavalueSlopeSetting.setStatus("mandatory")


class _RfastateFlagSlopeSetting_Type(Integer32):
    """Custom type rfastateFlagSlopeSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateFlagSlopeSetting_Type.__name__ = "Integer32"
_RfastateFlagSlopeSetting_Object = MibTableColumn
rfastateFlagSlopeSetting = _RfastateFlagSlopeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 5),
    _RfastateFlagSlopeSetting_Type()
)
rfastateFlagSlopeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateFlagSlopeSetting.setStatus("mandatory")


class _RfalabelAttnSetting_Type(DisplayString):
    """Custom type rfalabelAttnSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelAttnSetting_Type.__name__ = "DisplayString"
_RfalabelAttnSetting_Object = MibTableColumn
rfalabelAttnSetting = _RfalabelAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 6),
    _RfalabelAttnSetting_Type()
)
rfalabelAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelAttnSetting.setStatus("optional")


class _RfaenumAttnSetting_Type(DisplayString):
    """Custom type rfaenumAttnSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfaenumAttnSetting_Type.__name__ = "DisplayString"
_RfaenumAttnSetting_Object = MibTableColumn
rfaenumAttnSetting = _RfaenumAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 7),
    _RfaenumAttnSetting_Type()
)
rfaenumAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaenumAttnSetting.setStatus("optional")


class _RfavalueAttnSetting_Type(Integer32):
    """Custom type rfavalueAttnSetting based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("db0point00", 1),
          ("db0point25", 2),
          ("db0point50", 3),
          ("db0point75", 4),
          ("db1point00", 5),
          ("db1point25", 6),
          ("db1point50", 7),
          ("db1point75", 8),
          ("db2point00", 9),
          ("db2point25", 10),
          ("db2point50", 11),
          ("db2point75", 12),
          ("db3point00", 13),
          ("db3point25", 14),
          ("db3point50", 15),
          ("db3point75", 16),
          ("db4point00", 17),
          ("db4point25", 18),
          ("db4point50", 19),
          ("db4point75", 20),
          ("db5point00", 21))
    )


_RfavalueAttnSetting_Type.__name__ = "Integer32"
_RfavalueAttnSetting_Object = MibTableColumn
rfavalueAttnSetting = _RfavalueAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 8),
    _RfavalueAttnSetting_Type()
)
rfavalueAttnSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfavalueAttnSetting.setStatus("mandatory")


class _RfastateFlagAttnSetting_Type(Integer32):
    """Custom type rfastateFlagAttnSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateFlagAttnSetting_Type.__name__ = "Integer32"
_RfastateFlagAttnSetting_Object = MibTableColumn
rfastateFlagAttnSetting = _RfastateFlagAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 9),
    _RfastateFlagAttnSetting_Type()
)
rfastateFlagAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateFlagAttnSetting.setStatus("mandatory")


class _RfalabelFactoryDefault_Type(DisplayString):
    """Custom type rfalabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelFactoryDefault_Type.__name__ = "DisplayString"
_RfalabelFactoryDefault_Object = MibTableColumn
rfalabelFactoryDefault = _RfalabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 10),
    _RfalabelFactoryDefault_Type()
)
rfalabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelFactoryDefault.setStatus("optional")


class _RfaenumFactoryDefault_Type(DisplayString):
    """Custom type rfaenumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfaenumFactoryDefault_Type.__name__ = "DisplayString"
_RfaenumFactoryDefault_Object = MibTableColumn
rfaenumFactoryDefault = _RfaenumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 11),
    _RfaenumFactoryDefault_Type()
)
rfaenumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaenumFactoryDefault.setStatus("optional")


class _RfavalueFactoryDefault_Type(Integer32):
    """Custom type rfavalueFactoryDefault based on Integer32"""
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


_RfavalueFactoryDefault_Type.__name__ = "Integer32"
_RfavalueFactoryDefault_Object = MibTableColumn
rfavalueFactoryDefault = _RfavalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 12),
    _RfavalueFactoryDefault_Type()
)
rfavalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfavalueFactoryDefault.setStatus("mandatory")


class _RfastateFlagFactoryDefault_Type(Integer32):
    """Custom type rfastateFlagFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateFlagFactoryDefault_Type.__name__ = "Integer32"
_RfastateFlagFactoryDefault_Object = MibTableColumn
rfastateFlagFactoryDefault = _RfastateFlagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 3, 2, 13),
    _RfastateFlagFactoryDefault_Type()
)
rfastateFlagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateFlagFactoryDefault.setStatus("mandatory")
_Gx2Rfa1000StatusTable_Object = MibTable
gx2Rfa1000StatusTable = _Gx2Rfa1000StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4)
)
if mibBuilder.loadTexts:
    gx2Rfa1000StatusTable.setStatus("mandatory")
_Gx2Rfa1000StatusEntry_Object = MibTableRow
gx2Rfa1000StatusEntry = _Gx2Rfa1000StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3)
)
gx2Rfa1000StatusEntry.setIndexNames(
    (0, "OMNI-gx2RFA1000-MIB", "rfagx2Rfa1000StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rfa1000StatusEntry.setStatus("mandatory")


class _Rfagx2Rfa1000StatusTableIndex_Type(Integer32):
    """Custom type rfagx2Rfa1000StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Rfagx2Rfa1000StatusTableIndex_Type.__name__ = "Integer32"
_Rfagx2Rfa1000StatusTableIndex_Object = MibTableColumn
rfagx2Rfa1000StatusTableIndex = _Rfagx2Rfa1000StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 1),
    _Rfagx2Rfa1000StatusTableIndex_Type()
)
rfagx2Rfa1000StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfagx2Rfa1000StatusTableIndex.setStatus("mandatory")


class _RfalabelBoot_Type(DisplayString):
    """Custom type rfalabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelBoot_Type.__name__ = "DisplayString"
_RfalabelBoot_Object = MibTableColumn
rfalabelBoot = _RfalabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 2),
    _RfalabelBoot_Type()
)
rfalabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelBoot.setStatus("optional")


class _RfavalueBoot_Type(Integer32):
    """Custom type rfavalueBoot based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_RfavalueBoot_Type.__name__ = "Integer32"
_RfavalueBoot_Object = MibTableColumn
rfavalueBoot = _RfavalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 3),
    _RfavalueBoot_Type()
)
rfavalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfavalueBoot.setStatus("mandatory")


class _RfastateflagBoot_Type(Integer32):
    """Custom type rfastateflagBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateflagBoot_Type.__name__ = "Integer32"
_RfastateflagBoot_Object = MibTableColumn
rfastateflagBoot = _RfastateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 4),
    _RfastateflagBoot_Type()
)
rfastateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateflagBoot.setStatus("mandatory")


class _RfalabelFlash_Type(DisplayString):
    """Custom type rfalabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelFlash_Type.__name__ = "DisplayString"
_RfalabelFlash_Object = MibTableColumn
rfalabelFlash = _RfalabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 5),
    _RfalabelFlash_Type()
)
rfalabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelFlash.setStatus("optional")


class _RfavalueFlash_Type(Integer32):
    """Custom type rfavalueFlash based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_RfavalueFlash_Type.__name__ = "Integer32"
_RfavalueFlash_Object = MibTableColumn
rfavalueFlash = _RfavalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 6),
    _RfavalueFlash_Type()
)
rfavalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfavalueFlash.setStatus("mandatory")


class _RfastateflagFlash_Type(Integer32):
    """Custom type rfastateflagFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateflagFlash_Type.__name__ = "Integer32"
_RfastateflagFlash_Object = MibTableColumn
rfastateflagFlash = _RfastateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 7),
    _RfastateflagFlash_Type()
)
rfastateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateflagFlash.setStatus("mandatory")


class _RfalabelFactoryDataCRC_Type(DisplayString):
    """Custom type rfalabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelFactoryDataCRC_Type.__name__ = "DisplayString"
_RfalabelFactoryDataCRC_Object = MibTableColumn
rfalabelFactoryDataCRC = _RfalabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 8),
    _RfalabelFactoryDataCRC_Type()
)
rfalabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelFactoryDataCRC.setStatus("optional")


class _RfavalueFactoryDataCRC_Type(Integer32):
    """Custom type rfavalueFactoryDataCRC based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_RfavalueFactoryDataCRC_Type.__name__ = "Integer32"
_RfavalueFactoryDataCRC_Object = MibTableColumn
rfavalueFactoryDataCRC = _RfavalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 9),
    _RfavalueFactoryDataCRC_Type()
)
rfavalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfavalueFactoryDataCRC.setStatus("mandatory")


class _RfastateflagFactoryDataCRC_Type(Integer32):
    """Custom type rfastateflagFactoryDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateflagFactoryDataCRC_Type.__name__ = "Integer32"
_RfastateflagFactoryDataCRC_Object = MibTableColumn
rfastateflagFactoryDataCRC = _RfastateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 10),
    _RfastateflagFactoryDataCRC_Type()
)
rfastateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateflagFactoryDataCRC.setStatus("mandatory")


class _RfalabelAlarmDataCRC_Type(DisplayString):
    """Custom type rfalabelAlarmDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelAlarmDataCRC_Type.__name__ = "DisplayString"
_RfalabelAlarmDataCRC_Object = MibTableColumn
rfalabelAlarmDataCRC = _RfalabelAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 11),
    _RfalabelAlarmDataCRC_Type()
)
rfalabelAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelAlarmDataCRC.setStatus("optional")


class _RfavalueAlarmDataCRC_Type(Integer32):
    """Custom type rfavalueAlarmDataCRC based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_RfavalueAlarmDataCRC_Type.__name__ = "Integer32"
_RfavalueAlarmDataCRC_Object = MibTableColumn
rfavalueAlarmDataCRC = _RfavalueAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 12),
    _RfavalueAlarmDataCRC_Type()
)
rfavalueAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfavalueAlarmDataCRC.setStatus("mandatory")


class _RfastateflagAlarmDataCRC_Type(Integer32):
    """Custom type rfastateflagAlarmDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateflagAlarmDataCRC_Type.__name__ = "Integer32"
_RfastateflagAlarmDataCRC_Object = MibTableColumn
rfastateflagAlarmDataCRC = _RfastateflagAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 13),
    _RfastateflagAlarmDataCRC_Type()
)
rfastateflagAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateflagAlarmDataCRC.setStatus("mandatory")


class _RfalabelSlopeCalDataCRC_Type(DisplayString):
    """Custom type rfalabelSlopeCalDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelSlopeCalDataCRC_Type.__name__ = "DisplayString"
_RfalabelSlopeCalDataCRC_Object = MibTableColumn
rfalabelSlopeCalDataCRC = _RfalabelSlopeCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 14),
    _RfalabelSlopeCalDataCRC_Type()
)
rfalabelSlopeCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelSlopeCalDataCRC.setStatus("optional")


class _RfavalueSlopeCalDataCRC_Type(Integer32):
    """Custom type rfavalueSlopeCalDataCRC based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_RfavalueSlopeCalDataCRC_Type.__name__ = "Integer32"
_RfavalueSlopeCalDataCRC_Object = MibTableColumn
rfavalueSlopeCalDataCRC = _RfavalueSlopeCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 15),
    _RfavalueSlopeCalDataCRC_Type()
)
rfavalueSlopeCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfavalueSlopeCalDataCRC.setStatus("mandatory")


class _RfastateflagSlopeCalDataCRC_Type(Integer32):
    """Custom type rfastateflagSlopeCalDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateflagSlopeCalDataCRC_Type.__name__ = "Integer32"
_RfastateflagSlopeCalDataCRC_Object = MibTableColumn
rfastateflagSlopeCalDataCRC = _RfastateflagSlopeCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 16),
    _RfastateflagSlopeCalDataCRC_Type()
)
rfastateflagSlopeCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateflagSlopeCalDataCRC.setStatus("mandatory")


class _RfalabelAttnCalDataCRC_Type(DisplayString):
    """Custom type rfalabelAttnCalDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfalabelAttnCalDataCRC_Type.__name__ = "DisplayString"
_RfalabelAttnCalDataCRC_Object = MibTableColumn
rfalabelAttnCalDataCRC = _RfalabelAttnCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 17),
    _RfalabelAttnCalDataCRC_Type()
)
rfalabelAttnCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfalabelAttnCalDataCRC.setStatus("optional")


class _RfavalueAttnCalDataCRC_Type(Integer32):
    """Custom type rfavalueAttnCalDataCRC based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_RfavalueAttnCalDataCRC_Type.__name__ = "Integer32"
_RfavalueAttnCalDataCRC_Object = MibTableColumn
rfavalueAttnCalDataCRC = _RfavalueAttnCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 18),
    _RfavalueAttnCalDataCRC_Type()
)
rfavalueAttnCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfavalueAttnCalDataCRC.setStatus("mandatory")


class _RfastateflagAttnCalDataCRC_Type(Integer32):
    """Custom type rfastateflagAttnCalDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_RfastateflagAttnCalDataCRC_Type.__name__ = "Integer32"
_RfastateflagAttnCalDataCRC_Object = MibTableColumn
rfastateflagAttnCalDataCRC = _RfastateflagAttnCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 4, 3, 19),
    _RfastateflagAttnCalDataCRC_Type()
)
rfastateflagAttnCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfastateflagAttnCalDataCRC.setStatus("mandatory")
_Gx2Rfa1000FactoryTable_Object = MibTable
gx2Rfa1000FactoryTable = _Gx2Rfa1000FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5)
)
if mibBuilder.loadTexts:
    gx2Rfa1000FactoryTable.setStatus("mandatory")
_Gx2Rfa1000FactoryEntry_Object = MibTableRow
gx2Rfa1000FactoryEntry = _Gx2Rfa1000FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4)
)
gx2Rfa1000FactoryEntry.setIndexNames(
    (0, "OMNI-gx2RFA1000-MIB", "rfagx2Rfa1000FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rfa1000FactoryEntry.setStatus("mandatory")


class _Rfagx2Rfa1000FactoryTableIndex_Type(Integer32):
    """Custom type rfagx2Rfa1000FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Rfagx2Rfa1000FactoryTableIndex_Type.__name__ = "Integer32"
_Rfagx2Rfa1000FactoryTableIndex_Object = MibTableColumn
rfagx2Rfa1000FactoryTableIndex = _Rfagx2Rfa1000FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 1),
    _Rfagx2Rfa1000FactoryTableIndex_Type()
)
rfagx2Rfa1000FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfagx2Rfa1000FactoryTableIndex.setStatus("mandatory")
_RfabootControlByte_Type = Integer32
_RfabootControlByte_Object = MibTableColumn
rfabootControlByte = _RfabootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 2),
    _RfabootControlByte_Type()
)
rfabootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfabootControlByte.setStatus("mandatory")
_RfabootStatusByte_Type = Integer32
_RfabootStatusByte_Object = MibTableColumn
rfabootStatusByte = _RfabootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 3),
    _RfabootStatusByte_Type()
)
rfabootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfabootStatusByte.setStatus("mandatory")
_Rfabank0CRC_Type = Integer32
_Rfabank0CRC_Object = MibTableColumn
rfabank0CRC = _Rfabank0CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 4),
    _Rfabank0CRC_Type()
)
rfabank0CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfabank0CRC.setStatus("mandatory")
_Rfabank1CRC_Type = Integer32
_Rfabank1CRC_Object = MibTableColumn
rfabank1CRC = _Rfabank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 5),
    _Rfabank1CRC_Type()
)
rfabank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfabank1CRC.setStatus("mandatory")
_RfaprgEEPROMByte_Type = Integer32
_RfaprgEEPROMByte_Object = MibTableColumn
rfaprgEEPROMByte = _RfaprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 6),
    _RfaprgEEPROMByte_Type()
)
rfaprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaprgEEPROMByte.setStatus("mandatory")
_RfafactoryCRC_Type = Integer32
_RfafactoryCRC_Object = MibTableColumn
rfafactoryCRC = _RfafactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 7),
    _RfafactoryCRC_Type()
)
rfafactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfafactoryCRC.setStatus("mandatory")


class _RfacalculateCRC_Type(Integer32):
    """Custom type rfacalculateCRC based on Integer32"""
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
        *(("alarmdata", 3),
          ("calSetting", 4),
          ("calibration", 2),
          ("factory", 1))
    )


_RfacalculateCRC_Type.__name__ = "Integer32"
_RfacalculateCRC_Object = MibTableColumn
rfacalculateCRC = _RfacalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 8),
    _RfacalculateCRC_Type()
)
rfacalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfacalculateCRC.setStatus("obsolete")
_RfahourMeter_Type = Integer32
_RfahourMeter_Object = MibTableColumn
rfahourMeter = _RfahourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 9),
    _RfahourMeter_Type()
)
rfahourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfahourMeter.setStatus("mandatory")
_RfaflashPrgCntA_Type = Integer32
_RfaflashPrgCntA_Object = MibTableColumn
rfaflashPrgCntA = _RfaflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 10),
    _RfaflashPrgCntA_Type()
)
rfaflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaflashPrgCntA.setStatus("mandatory")
_RfaflashPrgCntB_Type = Integer32
_RfaflashPrgCntB_Object = MibTableColumn
rfaflashPrgCntB = _RfaflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 11),
    _RfaflashPrgCntB_Type()
)
rfaflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfaflashPrgCntB.setStatus("mandatory")


class _RfafwRev0_Type(DisplayString):
    """Custom type rfafwRev0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfafwRev0_Type.__name__ = "DisplayString"
_RfafwRev0_Object = MibTableColumn
rfafwRev0 = _RfafwRev0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 12),
    _RfafwRev0_Type()
)
rfafwRev0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfafwRev0.setStatus("mandatory")


class _RfafwRev1_Type(DisplayString):
    """Custom type rfafwRev1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RfafwRev1_Type.__name__ = "DisplayString"
_RfafwRev1_Object = MibTableColumn
rfafwRev1 = _RfafwRev1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 5, 4, 13),
    _RfafwRev1_Type()
)
rfafwRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfafwRev1.setStatus("mandatory")
_Gx2Rfa1000HoldTimeTable_Object = MibTable
gx2Rfa1000HoldTimeTable = _Gx2Rfa1000HoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 6)
)
if mibBuilder.loadTexts:
    gx2Rfa1000HoldTimeTable.setStatus("mandatory")
_Gx2Rfa1000HoldTimeEntry_Object = MibTableRow
gx2Rfa1000HoldTimeEntry = _Gx2Rfa1000HoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 6, 5)
)
gx2Rfa1000HoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2RFA1000-MIB", "gx2Rfa1000HoldTimeTableIndex"),
    (0, "OMNI-gx2RFA1000-MIB", "gx2Rfa1000HoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Rfa1000HoldTimeEntry.setStatus("mandatory")


class _Gx2Rfa1000HoldTimeTableIndex_Type(Integer32):
    """Custom type gx2Rfa1000HoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rfa1000HoldTimeTableIndex_Type.__name__ = "Integer32"
_Gx2Rfa1000HoldTimeTableIndex_Object = MibTableColumn
gx2Rfa1000HoldTimeTableIndex = _Gx2Rfa1000HoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 6, 5, 1),
    _Gx2Rfa1000HoldTimeTableIndex_Type()
)
gx2Rfa1000HoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rfa1000HoldTimeTableIndex.setStatus("mandatory")


class _Gx2Rfa1000HoldTimeSpecIndex_Type(Integer32):
    """Custom type gx2Rfa1000HoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rfa1000HoldTimeSpecIndex_Type.__name__ = "Integer32"
_Gx2Rfa1000HoldTimeSpecIndex_Object = MibTableColumn
gx2Rfa1000HoldTimeSpecIndex = _Gx2Rfa1000HoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 6, 5, 2),
    _Gx2Rfa1000HoldTimeSpecIndex_Type()
)
gx2Rfa1000HoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rfa1000HoldTimeSpecIndex.setStatus("mandatory")
_Gx2Rfa1000HoldTimeData_Type = Integer32
_Gx2Rfa1000HoldTimeData_Object = MibTableColumn
gx2Rfa1000HoldTimeData = _Gx2Rfa1000HoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 6, 5, 3),
    _Gx2Rfa1000HoldTimeData_Type()
)
gx2Rfa1000HoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gx2Rfa1000HoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapRFA1000ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 1)
)
trapRFA1000ConfigChangeInteger.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000ConfigChangeInteger.setStatus(
        ""
    )

trapRFA1000ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 2)
)
trapRFA1000ConfigChangeDisplayString.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueDisplayString"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000ConfigChangeDisplayString.setStatus(
        ""
    )

trapRFA1000ModuleTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 3)
)
trapRFA1000ModuleTemperatureAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000ModuleTemperatureAlarm.setStatus(
        ""
    )

trapRFA1000FanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 4)
)
trapRFA1000FanCurrentAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000FanCurrentAlarm.setStatus(
        ""
    )

trapRFA1000Plus12CurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 5)
)
trapRFA1000Plus12CurrentAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000Plus12CurrentAlarm.setStatus(
        ""
    )

trapRFA1000Boot0Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 6)
)
trapRFA1000Boot0Alarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000Boot0Alarm.setStatus(
        ""
    )

trapRFA1000Boot1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 7)
)
trapRFA1000Boot1Alarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000Boot1Alarm.setStatus(
        ""
    )

trapRFA1000FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 8)
)
trapRFA1000FlashAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000FlashAlarm.setStatus(
        ""
    )

trapRFA1000AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 9)
)
trapRFA1000AlarmDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000AlarmDataCRCAlarm.setStatus(
        ""
    )

trapRFA1000FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 10)
)
trapRFA1000FactoryDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000FactoryDataCRCAlarm.setStatus(
        ""
    )

trapRFA1000SlopeCalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 11)
)
trapRFA1000SlopeCalDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000SlopeCalDataCRCAlarm.setStatus(
        ""
    )

trapRFA1000AttnCalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 12)
)
trapRFA1000AttnCalDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000AttnCalDataCRCAlarm.setStatus(
        ""
    )

trapRFA1000ResetFacDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22, 0, 13)
)
trapRFA1000ResetFacDefault.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapRFA1000ResetFacDefault.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2RFA1000-MIB",
    **{"Float": Float,
       "trapRFA1000ConfigChangeInteger": trapRFA1000ConfigChangeInteger,
       "trapRFA1000ConfigChangeDisplayString": trapRFA1000ConfigChangeDisplayString,
       "trapRFA1000ModuleTemperatureAlarm": trapRFA1000ModuleTemperatureAlarm,
       "trapRFA1000FanCurrentAlarm": trapRFA1000FanCurrentAlarm,
       "trapRFA1000Plus12CurrentAlarm": trapRFA1000Plus12CurrentAlarm,
       "trapRFA1000Boot0Alarm": trapRFA1000Boot0Alarm,
       "trapRFA1000Boot1Alarm": trapRFA1000Boot1Alarm,
       "trapRFA1000FlashAlarm": trapRFA1000FlashAlarm,
       "trapRFA1000AlarmDataCRCAlarm": trapRFA1000AlarmDataCRCAlarm,
       "trapRFA1000FactoryDataCRCAlarm": trapRFA1000FactoryDataCRCAlarm,
       "trapRFA1000SlopeCalDataCRCAlarm": trapRFA1000SlopeCalDataCRCAlarm,
       "trapRFA1000AttnCalDataCRCAlarm": trapRFA1000AttnCalDataCRCAlarm,
       "trapRFA1000ResetFacDefault": trapRFA1000ResetFacDefault,
       "gx2Rfa1000Descriptor": gx2Rfa1000Descriptor,
       "gx2Rfa1000AnalogTable": gx2Rfa1000AnalogTable,
       "gx2Rfa1000AnalogEntry": gx2Rfa1000AnalogEntry,
       "rfagx2Rfa1000AnalogTableIndex": rfagx2Rfa1000AnalogTableIndex,
       "rfalabelModTemp": rfalabelModTemp,
       "rfauomModTemp": rfauomModTemp,
       "rfamajorHighModTemp": rfamajorHighModTemp,
       "rfamajorLowModTemp": rfamajorLowModTemp,
       "rfaminorHighModTemp": rfaminorHighModTemp,
       "rfaminorLowModTemp": rfaminorLowModTemp,
       "rfacurrentValueModTemp": rfacurrentValueModTemp,
       "rfastateFlagModTemp": rfastateFlagModTemp,
       "rfaminValueModTemp": rfaminValueModTemp,
       "rfamaxValueModTemp": rfamaxValueModTemp,
       "rfaalarmStateModTemp": rfaalarmStateModTemp,
       "rfalabelFanCurrent": rfalabelFanCurrent,
       "rfauomFanCurrent": rfauomFanCurrent,
       "rfamajorHighFanCurrent": rfamajorHighFanCurrent,
       "rfamajorLowFanCurrent": rfamajorLowFanCurrent,
       "rfaminorHighFanCurrent": rfaminorHighFanCurrent,
       "rfaminorLowFanCurrent": rfaminorLowFanCurrent,
       "rfacurrentValueFanCurrent": rfacurrentValueFanCurrent,
       "rfastateFlagFanCurrent": rfastateFlagFanCurrent,
       "rfaminValueFanCurrent": rfaminValueFanCurrent,
       "rfamaxValueFanCurrent": rfamaxValueFanCurrent,
       "rfaalarmStateFanCurrent": rfaalarmStateFanCurrent,
       "rfalabel12Volt": rfalabel12Volt,
       "rfauom12Volt": rfauom12Volt,
       "rfamajorHigh12Volt": rfamajorHigh12Volt,
       "rfamajorLow12Volt": rfamajorLow12Volt,
       "rfaminorHigh12Volt": rfaminorHigh12Volt,
       "rfaminorLow12Volt": rfaminorLow12Volt,
       "rfacurrentValue12Volt": rfacurrentValue12Volt,
       "rfastateFlag12Volt": rfastateFlag12Volt,
       "rfaminValue12Volt": rfaminValue12Volt,
       "rfamaxValue12Volt": rfamaxValue12Volt,
       "rfaalarmState12Volt": rfaalarmState12Volt,
       "gx2Rfa1000DigitalTable": gx2Rfa1000DigitalTable,
       "gx2Rfa1000DigitalEntry": gx2Rfa1000DigitalEntry,
       "rfagx2Rfa1000DigitalTableIndex": rfagx2Rfa1000DigitalTableIndex,
       "rfalabelSlopeSetting": rfalabelSlopeSetting,
       "rfaenumSlopeSetting": rfaenumSlopeSetting,
       "rfavalueSlopeSetting": rfavalueSlopeSetting,
       "rfastateFlagSlopeSetting": rfastateFlagSlopeSetting,
       "rfalabelAttnSetting": rfalabelAttnSetting,
       "rfaenumAttnSetting": rfaenumAttnSetting,
       "rfavalueAttnSetting": rfavalueAttnSetting,
       "rfastateFlagAttnSetting": rfastateFlagAttnSetting,
       "rfalabelFactoryDefault": rfalabelFactoryDefault,
       "rfaenumFactoryDefault": rfaenumFactoryDefault,
       "rfavalueFactoryDefault": rfavalueFactoryDefault,
       "rfastateFlagFactoryDefault": rfastateFlagFactoryDefault,
       "gx2Rfa1000StatusTable": gx2Rfa1000StatusTable,
       "gx2Rfa1000StatusEntry": gx2Rfa1000StatusEntry,
       "rfagx2Rfa1000StatusTableIndex": rfagx2Rfa1000StatusTableIndex,
       "rfalabelBoot": rfalabelBoot,
       "rfavalueBoot": rfavalueBoot,
       "rfastateflagBoot": rfastateflagBoot,
       "rfalabelFlash": rfalabelFlash,
       "rfavalueFlash": rfavalueFlash,
       "rfastateflagFlash": rfastateflagFlash,
       "rfalabelFactoryDataCRC": rfalabelFactoryDataCRC,
       "rfavalueFactoryDataCRC": rfavalueFactoryDataCRC,
       "rfastateflagFactoryDataCRC": rfastateflagFactoryDataCRC,
       "rfalabelAlarmDataCRC": rfalabelAlarmDataCRC,
       "rfavalueAlarmDataCRC": rfavalueAlarmDataCRC,
       "rfastateflagAlarmDataCRC": rfastateflagAlarmDataCRC,
       "rfalabelSlopeCalDataCRC": rfalabelSlopeCalDataCRC,
       "rfavalueSlopeCalDataCRC": rfavalueSlopeCalDataCRC,
       "rfastateflagSlopeCalDataCRC": rfastateflagSlopeCalDataCRC,
       "rfalabelAttnCalDataCRC": rfalabelAttnCalDataCRC,
       "rfavalueAttnCalDataCRC": rfavalueAttnCalDataCRC,
       "rfastateflagAttnCalDataCRC": rfastateflagAttnCalDataCRC,
       "gx2Rfa1000FactoryTable": gx2Rfa1000FactoryTable,
       "gx2Rfa1000FactoryEntry": gx2Rfa1000FactoryEntry,
       "rfagx2Rfa1000FactoryTableIndex": rfagx2Rfa1000FactoryTableIndex,
       "rfabootControlByte": rfabootControlByte,
       "rfabootStatusByte": rfabootStatusByte,
       "rfabank0CRC": rfabank0CRC,
       "rfabank1CRC": rfabank1CRC,
       "rfaprgEEPROMByte": rfaprgEEPROMByte,
       "rfafactoryCRC": rfafactoryCRC,
       "rfacalculateCRC": rfacalculateCRC,
       "rfahourMeter": rfahourMeter,
       "rfaflashPrgCntA": rfaflashPrgCntA,
       "rfaflashPrgCntB": rfaflashPrgCntB,
       "rfafwRev0": rfafwRev0,
       "rfafwRev1": rfafwRev1,
       "gx2Rfa1000HoldTimeTable": gx2Rfa1000HoldTimeTable,
       "gx2Rfa1000HoldTimeEntry": gx2Rfa1000HoldTimeEntry,
       "gx2Rfa1000HoldTimeTableIndex": gx2Rfa1000HoldTimeTableIndex,
       "gx2Rfa1000HoldTimeSpecIndex": gx2Rfa1000HoldTimeSpecIndex,
       "gx2Rfa1000HoldTimeData": gx2Rfa1000HoldTimeData}
)
