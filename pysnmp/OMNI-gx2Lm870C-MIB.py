# SNMP MIB module (OMNI-gx2Lm870C-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2Lm870C-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:27 2024
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

(gx2Lm870C,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Lm870C")

(gi,
 motproxies) = mibBuilder.importSymbols(
    "NLS-BBNIDENT-MIB",
    "gi",
    "motproxies")

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

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

_Gx2Lm870CDescriptor_ObjectIdentity = ObjectIdentity
gx2Lm870CDescriptor = _Gx2Lm870CDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 1)
)
_Gx2lm870CAnalogTable_Object = MibTable
gx2lm870CAnalogTable = _Gx2lm870CAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    gx2lm870CAnalogTable.setStatus("mandatory")
_Gx2lm870CAnalogEntry_Object = MibTableRow
gx2lm870CAnalogEntry = _Gx2lm870CAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1)
)
gx2lm870CAnalogEntry.setIndexNames(
    (0, "OMNI-gx2Lm870C-MIB", "gx2Lm870CAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2lm870CAnalogEntry.setStatus("mandatory")


class _Gx2Lm870CAnalogTableIndex_Type(Integer32):
    """Custom type gx2Lm870CAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Lm870CAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Lm870CAnalogTableIndex_Object = MibTableColumn
gx2Lm870CAnalogTableIndex = _Gx2Lm870CAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 1),
    _Gx2Lm870CAnalogTableIndex_Type()
)
gx2Lm870CAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm870CAnalogTableIndex.setStatus("mandatory")


class _Lm870ClabelFanCurrent_Type(DisplayString):
    """Custom type lm870ClabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelFanCurrent_Type.__name__ = "DisplayString"
_Lm870ClabelFanCurrent_Object = MibTableColumn
lm870ClabelFanCurrent = _Lm870ClabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 2),
    _Lm870ClabelFanCurrent_Type()
)
lm870ClabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelFanCurrent.setStatus("optional")


class _Lm870CuomFanCurrent_Type(DisplayString):
    """Custom type lm870CuomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CuomFanCurrent_Type.__name__ = "DisplayString"
_Lm870CuomFanCurrent_Object = MibTableColumn
lm870CuomFanCurrent = _Lm870CuomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 3),
    _Lm870CuomFanCurrent_Type()
)
lm870CuomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CuomFanCurrent.setStatus("optional")
_Lm870CmajorHighFanCurrent_Type = Float
_Lm870CmajorHighFanCurrent_Object = MibTableColumn
lm870CmajorHighFanCurrent = _Lm870CmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 4),
    _Lm870CmajorHighFanCurrent_Type()
)
lm870CmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorHighFanCurrent.setStatus("mandatory")
_Lm870CmajorLowFanCurrent_Type = Float
_Lm870CmajorLowFanCurrent_Object = MibTableColumn
lm870CmajorLowFanCurrent = _Lm870CmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 5),
    _Lm870CmajorLowFanCurrent_Type()
)
lm870CmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorLowFanCurrent.setStatus("mandatory")
_Lm870CminorHighFanCurrent_Type = Float
_Lm870CminorHighFanCurrent_Object = MibTableColumn
lm870CminorHighFanCurrent = _Lm870CminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 6),
    _Lm870CminorHighFanCurrent_Type()
)
lm870CminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorHighFanCurrent.setStatus("mandatory")
_Lm870CminorLowFanCurrent_Type = Float
_Lm870CminorLowFanCurrent_Object = MibTableColumn
lm870CminorLowFanCurrent = _Lm870CminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 7),
    _Lm870CminorLowFanCurrent_Type()
)
lm870CminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorLowFanCurrent.setStatus("mandatory")
_Lm870CcurrentValueFanCurrent_Type = Float
_Lm870CcurrentValueFanCurrent_Object = MibTableColumn
lm870CcurrentValueFanCurrent = _Lm870CcurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 8),
    _Lm870CcurrentValueFanCurrent_Type()
)
lm870CcurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CcurrentValueFanCurrent.setStatus("mandatory")


class _Lm870CstateFlagFanCurrent_Type(Integer32):
    """Custom type lm870CstateFlagFanCurrent based on Integer32"""
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


_Lm870CstateFlagFanCurrent_Type.__name__ = "Integer32"
_Lm870CstateFlagFanCurrent_Object = MibTableColumn
lm870CstateFlagFanCurrent = _Lm870CstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 9),
    _Lm870CstateFlagFanCurrent_Type()
)
lm870CstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagFanCurrent.setStatus("mandatory")
_Lm870CminValueFanCurrent_Type = Float
_Lm870CminValueFanCurrent_Object = MibTableColumn
lm870CminValueFanCurrent = _Lm870CminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 10),
    _Lm870CminValueFanCurrent_Type()
)
lm870CminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminValueFanCurrent.setStatus("mandatory")
_Lm870CmaxValueFanCurrent_Type = Float
_Lm870CmaxValueFanCurrent_Object = MibTableColumn
lm870CmaxValueFanCurrent = _Lm870CmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 11),
    _Lm870CmaxValueFanCurrent_Type()
)
lm870CmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmaxValueFanCurrent.setStatus("mandatory")


class _Lm870CalarmStateFanCurrent_Type(Integer32):
    """Custom type lm870CalarmStateFanCurrent based on Integer32"""
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


_Lm870CalarmStateFanCurrent_Type.__name__ = "Integer32"
_Lm870CalarmStateFanCurrent_Object = MibTableColumn
lm870CalarmStateFanCurrent = _Lm870CalarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 12),
    _Lm870CalarmStateFanCurrent_Type()
)
lm870CalarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CalarmStateFanCurrent.setStatus("mandatory")


class _Lm870Clabel12Volt_Type(DisplayString):
    """Custom type lm870Clabel12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870Clabel12Volt_Type.__name__ = "DisplayString"
_Lm870Clabel12Volt_Object = MibTableColumn
lm870Clabel12Volt = _Lm870Clabel12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 13),
    _Lm870Clabel12Volt_Type()
)
lm870Clabel12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870Clabel12Volt.setStatus("optional")


class _Lm870Cuom12Volt_Type(DisplayString):
    """Custom type lm870Cuom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870Cuom12Volt_Type.__name__ = "DisplayString"
_Lm870Cuom12Volt_Object = MibTableColumn
lm870Cuom12Volt = _Lm870Cuom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 14),
    _Lm870Cuom12Volt_Type()
)
lm870Cuom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870Cuom12Volt.setStatus("optional")
_Lm870CmajorHigh12Volt_Type = Float
_Lm870CmajorHigh12Volt_Object = MibTableColumn
lm870CmajorHigh12Volt = _Lm870CmajorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 15),
    _Lm870CmajorHigh12Volt_Type()
)
lm870CmajorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorHigh12Volt.setStatus("mandatory")
_Lm870CmajorLow12Volt_Type = Float
_Lm870CmajorLow12Volt_Object = MibTableColumn
lm870CmajorLow12Volt = _Lm870CmajorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 16),
    _Lm870CmajorLow12Volt_Type()
)
lm870CmajorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorLow12Volt.setStatus("mandatory")
_Lm870CminorHigh12Volt_Type = Float
_Lm870CminorHigh12Volt_Object = MibTableColumn
lm870CminorHigh12Volt = _Lm870CminorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 17),
    _Lm870CminorHigh12Volt_Type()
)
lm870CminorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorHigh12Volt.setStatus("mandatory")
_Lm870CminorLow12Volt_Type = Float
_Lm870CminorLow12Volt_Object = MibTableColumn
lm870CminorLow12Volt = _Lm870CminorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 18),
    _Lm870CminorLow12Volt_Type()
)
lm870CminorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorLow12Volt.setStatus("mandatory")
_Lm870CcurrentValue12Volt_Type = Float
_Lm870CcurrentValue12Volt_Object = MibTableColumn
lm870CcurrentValue12Volt = _Lm870CcurrentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 19),
    _Lm870CcurrentValue12Volt_Type()
)
lm870CcurrentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CcurrentValue12Volt.setStatus("mandatory")


class _Lm870CstateFlag12Volt_Type(Integer32):
    """Custom type lm870CstateFlag12Volt based on Integer32"""
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


_Lm870CstateFlag12Volt_Type.__name__ = "Integer32"
_Lm870CstateFlag12Volt_Object = MibTableColumn
lm870CstateFlag12Volt = _Lm870CstateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 20),
    _Lm870CstateFlag12Volt_Type()
)
lm870CstateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlag12Volt.setStatus("mandatory")
_Lm870CminValue12Volt_Type = Float
_Lm870CminValue12Volt_Object = MibTableColumn
lm870CminValue12Volt = _Lm870CminValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 21),
    _Lm870CminValue12Volt_Type()
)
lm870CminValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminValue12Volt.setStatus("mandatory")
_Lm870CmaxValue12Volt_Type = Float
_Lm870CmaxValue12Volt_Object = MibTableColumn
lm870CmaxValue12Volt = _Lm870CmaxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 22),
    _Lm870CmaxValue12Volt_Type()
)
lm870CmaxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmaxValue12Volt.setStatus("mandatory")


class _Lm870CalarmState12Volt_Type(Integer32):
    """Custom type lm870CalarmState12Volt based on Integer32"""
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


_Lm870CalarmState12Volt_Type.__name__ = "Integer32"
_Lm870CalarmState12Volt_Object = MibTableColumn
lm870CalarmState12Volt = _Lm870CalarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 23),
    _Lm870CalarmState12Volt_Type()
)
lm870CalarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CalarmState12Volt.setStatus("mandatory")


class _Lm870ClabelModTemp_Type(DisplayString):
    """Custom type lm870ClabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelModTemp_Type.__name__ = "DisplayString"
_Lm870ClabelModTemp_Object = MibTableColumn
lm870ClabelModTemp = _Lm870ClabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 24),
    _Lm870ClabelModTemp_Type()
)
lm870ClabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelModTemp.setStatus("optional")


class _Lm870CuomModTemp_Type(DisplayString):
    """Custom type lm870CuomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CuomModTemp_Type.__name__ = "DisplayString"
_Lm870CuomModTemp_Object = MibTableColumn
lm870CuomModTemp = _Lm870CuomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 25),
    _Lm870CuomModTemp_Type()
)
lm870CuomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CuomModTemp.setStatus("optional")
_Lm870CmajorHighModTemp_Type = Float
_Lm870CmajorHighModTemp_Object = MibTableColumn
lm870CmajorHighModTemp = _Lm870CmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 26),
    _Lm870CmajorHighModTemp_Type()
)
lm870CmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorHighModTemp.setStatus("mandatory")
_Lm870CmajorLowModTemp_Type = Float
_Lm870CmajorLowModTemp_Object = MibTableColumn
lm870CmajorLowModTemp = _Lm870CmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 27),
    _Lm870CmajorLowModTemp_Type()
)
lm870CmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorLowModTemp.setStatus("mandatory")
_Lm870CminorHighModTemp_Type = Float
_Lm870CminorHighModTemp_Object = MibTableColumn
lm870CminorHighModTemp = _Lm870CminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 28),
    _Lm870CminorHighModTemp_Type()
)
lm870CminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorHighModTemp.setStatus("mandatory")
_Lm870CminorLowModTemp_Type = Float
_Lm870CminorLowModTemp_Object = MibTableColumn
lm870CminorLowModTemp = _Lm870CminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 29),
    _Lm870CminorLowModTemp_Type()
)
lm870CminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorLowModTemp.setStatus("mandatory")
_Lm870CcurrentValueModTemp_Type = Float
_Lm870CcurrentValueModTemp_Object = MibTableColumn
lm870CcurrentValueModTemp = _Lm870CcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 30),
    _Lm870CcurrentValueModTemp_Type()
)
lm870CcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CcurrentValueModTemp.setStatus("mandatory")


class _Lm870CstateFlagModTemp_Type(Integer32):
    """Custom type lm870CstateFlagModTemp based on Integer32"""
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


_Lm870CstateFlagModTemp_Type.__name__ = "Integer32"
_Lm870CstateFlagModTemp_Object = MibTableColumn
lm870CstateFlagModTemp = _Lm870CstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 31),
    _Lm870CstateFlagModTemp_Type()
)
lm870CstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagModTemp.setStatus("mandatory")
_Lm870CminValueModTemp_Type = Float
_Lm870CminValueModTemp_Object = MibTableColumn
lm870CminValueModTemp = _Lm870CminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 32),
    _Lm870CminValueModTemp_Type()
)
lm870CminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminValueModTemp.setStatus("mandatory")
_Lm870CmaxValueModTemp_Type = Float
_Lm870CmaxValueModTemp_Object = MibTableColumn
lm870CmaxValueModTemp = _Lm870CmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 33),
    _Lm870CmaxValueModTemp_Type()
)
lm870CmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmaxValueModTemp.setStatus("mandatory")


class _Lm870CalarmStateModTemp_Type(Integer32):
    """Custom type lm870CalarmStateModTemp based on Integer32"""
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


_Lm870CalarmStateModTemp_Type.__name__ = "Integer32"
_Lm870CalarmStateModTemp_Object = MibTableColumn
lm870CalarmStateModTemp = _Lm870CalarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 34),
    _Lm870CalarmStateModTemp_Type()
)
lm870CalarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CalarmStateModTemp.setStatus("mandatory")


class _Lm870ClabelOmiOffset_Type(DisplayString):
    """Custom type lm870ClabelOmiOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelOmiOffset_Type.__name__ = "DisplayString"
_Lm870ClabelOmiOffset_Object = MibTableColumn
lm870ClabelOmiOffset = _Lm870ClabelOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 35),
    _Lm870ClabelOmiOffset_Type()
)
lm870ClabelOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelOmiOffset.setStatus("optional")


class _Lm870CuomOmiOffset_Type(DisplayString):
    """Custom type lm870CuomOmiOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CuomOmiOffset_Type.__name__ = "DisplayString"
_Lm870CuomOmiOffset_Object = MibTableColumn
lm870CuomOmiOffset = _Lm870CuomOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 36),
    _Lm870CuomOmiOffset_Type()
)
lm870CuomOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CuomOmiOffset.setStatus("optional")
_Lm870CmajorHighOmiOffset_Type = Float
_Lm870CmajorHighOmiOffset_Object = MibTableColumn
lm870CmajorHighOmiOffset = _Lm870CmajorHighOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 37),
    _Lm870CmajorHighOmiOffset_Type()
)
lm870CmajorHighOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorHighOmiOffset.setStatus("mandatory")
_Lm870CmajorLowOmiOffset_Type = Float
_Lm870CmajorLowOmiOffset_Object = MibTableColumn
lm870CmajorLowOmiOffset = _Lm870CmajorLowOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 38),
    _Lm870CmajorLowOmiOffset_Type()
)
lm870CmajorLowOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorLowOmiOffset.setStatus("mandatory")
_Lm870CminorHighOmiOffset_Type = Float
_Lm870CminorHighOmiOffset_Object = MibTableColumn
lm870CminorHighOmiOffset = _Lm870CminorHighOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 39),
    _Lm870CminorHighOmiOffset_Type()
)
lm870CminorHighOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorHighOmiOffset.setStatus("mandatory")
_Lm870CminorLowOmiOffset_Type = Float
_Lm870CminorLowOmiOffset_Object = MibTableColumn
lm870CminorLowOmiOffset = _Lm870CminorLowOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 40),
    _Lm870CminorLowOmiOffset_Type()
)
lm870CminorLowOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorLowOmiOffset.setStatus("mandatory")
_Lm870CcurrentValueOmiOffset_Type = Float
_Lm870CcurrentValueOmiOffset_Object = MibTableColumn
lm870CcurrentValueOmiOffset = _Lm870CcurrentValueOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 41),
    _Lm870CcurrentValueOmiOffset_Type()
)
lm870CcurrentValueOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CcurrentValueOmiOffset.setStatus("mandatory")


class _Lm870CstateFlagOmiOffset_Type(Integer32):
    """Custom type lm870CstateFlagOmiOffset based on Integer32"""
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


_Lm870CstateFlagOmiOffset_Type.__name__ = "Integer32"
_Lm870CstateFlagOmiOffset_Object = MibTableColumn
lm870CstateFlagOmiOffset = _Lm870CstateFlagOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 42),
    _Lm870CstateFlagOmiOffset_Type()
)
lm870CstateFlagOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagOmiOffset.setStatus("mandatory")
_Lm870CminValueOmiOffset_Type = Float
_Lm870CminValueOmiOffset_Object = MibTableColumn
lm870CminValueOmiOffset = _Lm870CminValueOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 43),
    _Lm870CminValueOmiOffset_Type()
)
lm870CminValueOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminValueOmiOffset.setStatus("mandatory")
_Lm870CmaxValueOmiOffset_Type = Float
_Lm870CmaxValueOmiOffset_Object = MibTableColumn
lm870CmaxValueOmiOffset = _Lm870CmaxValueOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 44),
    _Lm870CmaxValueOmiOffset_Type()
)
lm870CmaxValueOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmaxValueOmiOffset.setStatus("mandatory")


class _Lm870CalarmStateOmiOffset_Type(Integer32):
    """Custom type lm870CalarmStateOmiOffset based on Integer32"""
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


_Lm870CalarmStateOmiOffset_Type.__name__ = "Integer32"
_Lm870CalarmStateOmiOffset_Object = MibTableColumn
lm870CalarmStateOmiOffset = _Lm870CalarmStateOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 45),
    _Lm870CalarmStateOmiOffset_Type()
)
lm870CalarmStateOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CalarmStateOmiOffset.setStatus("mandatory")


class _Lm870ClabelOPTPower_Type(DisplayString):
    """Custom type lm870ClabelOPTPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelOPTPower_Type.__name__ = "DisplayString"
_Lm870ClabelOPTPower_Object = MibTableColumn
lm870ClabelOPTPower = _Lm870ClabelOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 46),
    _Lm870ClabelOPTPower_Type()
)
lm870ClabelOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelOPTPower.setStatus("optional")


class _Lm870CuomOPTPower_Type(DisplayString):
    """Custom type lm870CuomOPTPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CuomOPTPower_Type.__name__ = "DisplayString"
_Lm870CuomOPTPower_Object = MibTableColumn
lm870CuomOPTPower = _Lm870CuomOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 47),
    _Lm870CuomOPTPower_Type()
)
lm870CuomOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CuomOPTPower.setStatus("optional")
_Lm870CmajorHighOPTPower_Type = Float
_Lm870CmajorHighOPTPower_Object = MibTableColumn
lm870CmajorHighOPTPower = _Lm870CmajorHighOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 48),
    _Lm870CmajorHighOPTPower_Type()
)
lm870CmajorHighOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorHighOPTPower.setStatus("mandatory")
_Lm870CmajorLowOPTPower_Type = Float
_Lm870CmajorLowOPTPower_Object = MibTableColumn
lm870CmajorLowOPTPower = _Lm870CmajorLowOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 49),
    _Lm870CmajorLowOPTPower_Type()
)
lm870CmajorLowOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorLowOPTPower.setStatus("mandatory")
_Lm870CminorHighOPTPower_Type = Float
_Lm870CminorHighOPTPower_Object = MibTableColumn
lm870CminorHighOPTPower = _Lm870CminorHighOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 50),
    _Lm870CminorHighOPTPower_Type()
)
lm870CminorHighOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorHighOPTPower.setStatus("mandatory")
_Lm870CminorLowOPTPower_Type = Float
_Lm870CminorLowOPTPower_Object = MibTableColumn
lm870CminorLowOPTPower = _Lm870CminorLowOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 51),
    _Lm870CminorLowOPTPower_Type()
)
lm870CminorLowOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorLowOPTPower.setStatus("mandatory")
_Lm870CcurrentValueOPTPower_Type = Float
_Lm870CcurrentValueOPTPower_Object = MibTableColumn
lm870CcurrentValueOPTPower = _Lm870CcurrentValueOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 52),
    _Lm870CcurrentValueOPTPower_Type()
)
lm870CcurrentValueOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CcurrentValueOPTPower.setStatus("mandatory")


class _Lm870CstateFlagOPTPower_Type(Integer32):
    """Custom type lm870CstateFlagOPTPower based on Integer32"""
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


_Lm870CstateFlagOPTPower_Type.__name__ = "Integer32"
_Lm870CstateFlagOPTPower_Object = MibTableColumn
lm870CstateFlagOPTPower = _Lm870CstateFlagOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 53),
    _Lm870CstateFlagOPTPower_Type()
)
lm870CstateFlagOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagOPTPower.setStatus("mandatory")
_Lm870CminValueOPTPower_Type = Float
_Lm870CminValueOPTPower_Object = MibTableColumn
lm870CminValueOPTPower = _Lm870CminValueOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 54),
    _Lm870CminValueOPTPower_Type()
)
lm870CminValueOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminValueOPTPower.setStatus("mandatory")
_Lm870CmaxValueOPTPower_Type = Float
_Lm870CmaxValueOPTPower_Object = MibTableColumn
lm870CmaxValueOPTPower = _Lm870CmaxValueOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 55),
    _Lm870CmaxValueOPTPower_Type()
)
lm870CmaxValueOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmaxValueOPTPower.setStatus("mandatory")


class _Lm870CalarmStateOPTPower_Type(Integer32):
    """Custom type lm870CalarmStateOPTPower based on Integer32"""
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


_Lm870CalarmStateOPTPower_Type.__name__ = "Integer32"
_Lm870CalarmStateOPTPower_Object = MibTableColumn
lm870CalarmStateOPTPower = _Lm870CalarmStateOPTPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 56),
    _Lm870CalarmStateOPTPower_Type()
)
lm870CalarmStateOPTPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CalarmStateOPTPower.setStatus("mandatory")


class _Lm870ClabelLaserBias_Type(DisplayString):
    """Custom type lm870ClabelLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelLaserBias_Type.__name__ = "DisplayString"
_Lm870ClabelLaserBias_Object = MibTableColumn
lm870ClabelLaserBias = _Lm870ClabelLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 57),
    _Lm870ClabelLaserBias_Type()
)
lm870ClabelLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelLaserBias.setStatus("optional")


class _Lm870CuomLaserBias_Type(DisplayString):
    """Custom type lm870CuomLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CuomLaserBias_Type.__name__ = "DisplayString"
_Lm870CuomLaserBias_Object = MibTableColumn
lm870CuomLaserBias = _Lm870CuomLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 58),
    _Lm870CuomLaserBias_Type()
)
lm870CuomLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CuomLaserBias.setStatus("optional")
_Lm870CmajorHighLaserBias_Type = Float
_Lm870CmajorHighLaserBias_Object = MibTableColumn
lm870CmajorHighLaserBias = _Lm870CmajorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 59),
    _Lm870CmajorHighLaserBias_Type()
)
lm870CmajorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorHighLaserBias.setStatus("mandatory")
_Lm870CmajorLowLaserBias_Type = Float
_Lm870CmajorLowLaserBias_Object = MibTableColumn
lm870CmajorLowLaserBias = _Lm870CmajorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 60),
    _Lm870CmajorLowLaserBias_Type()
)
lm870CmajorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorLowLaserBias.setStatus("mandatory")
_Lm870CminorHighLaserBias_Type = Float
_Lm870CminorHighLaserBias_Object = MibTableColumn
lm870CminorHighLaserBias = _Lm870CminorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 61),
    _Lm870CminorHighLaserBias_Type()
)
lm870CminorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorHighLaserBias.setStatus("mandatory")
_Lm870CminorLowLaserBias_Type = Float
_Lm870CminorLowLaserBias_Object = MibTableColumn
lm870CminorLowLaserBias = _Lm870CminorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 62),
    _Lm870CminorLowLaserBias_Type()
)
lm870CminorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorLowLaserBias.setStatus("mandatory")
_Lm870CcurrentValueLaserBias_Type = Float
_Lm870CcurrentValueLaserBias_Object = MibTableColumn
lm870CcurrentValueLaserBias = _Lm870CcurrentValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 63),
    _Lm870CcurrentValueLaserBias_Type()
)
lm870CcurrentValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CcurrentValueLaserBias.setStatus("mandatory")


class _Lm870CstateFlagLaserBias_Type(Integer32):
    """Custom type lm870CstateFlagLaserBias based on Integer32"""
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


_Lm870CstateFlagLaserBias_Type.__name__ = "Integer32"
_Lm870CstateFlagLaserBias_Object = MibTableColumn
lm870CstateFlagLaserBias = _Lm870CstateFlagLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 64),
    _Lm870CstateFlagLaserBias_Type()
)
lm870CstateFlagLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagLaserBias.setStatus("mandatory")
_Lm870CminValueLaserBias_Type = Float
_Lm870CminValueLaserBias_Object = MibTableColumn
lm870CminValueLaserBias = _Lm870CminValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 65),
    _Lm870CminValueLaserBias_Type()
)
lm870CminValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminValueLaserBias.setStatus("mandatory")
_Lm870CmaxValueLaserBias_Type = Float
_Lm870CmaxValueLaserBias_Object = MibTableColumn
lm870CmaxValueLaserBias = _Lm870CmaxValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 66),
    _Lm870CmaxValueLaserBias_Type()
)
lm870CmaxValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmaxValueLaserBias.setStatus("mandatory")


class _Lm870CalarmStateLaserBias_Type(Integer32):
    """Custom type lm870CalarmStateLaserBias based on Integer32"""
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


_Lm870CalarmStateLaserBias_Type.__name__ = "Integer32"
_Lm870CalarmStateLaserBias_Object = MibTableColumn
lm870CalarmStateLaserBias = _Lm870CalarmStateLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 67),
    _Lm870CalarmStateLaserBias_Type()
)
lm870CalarmStateLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CalarmStateLaserBias.setStatus("mandatory")


class _Lm870ClabelTecCurrent_Type(DisplayString):
    """Custom type lm870ClabelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelTecCurrent_Type.__name__ = "DisplayString"
_Lm870ClabelTecCurrent_Object = MibTableColumn
lm870ClabelTecCurrent = _Lm870ClabelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 68),
    _Lm870ClabelTecCurrent_Type()
)
lm870ClabelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelTecCurrent.setStatus("optional")


class _Lm870CuomTecCurrent_Type(DisplayString):
    """Custom type lm870CuomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CuomTecCurrent_Type.__name__ = "DisplayString"
_Lm870CuomTecCurrent_Object = MibTableColumn
lm870CuomTecCurrent = _Lm870CuomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 69),
    _Lm870CuomTecCurrent_Type()
)
lm870CuomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CuomTecCurrent.setStatus("optional")
_Lm870CmajorHighTecCurrent_Type = Float
_Lm870CmajorHighTecCurrent_Object = MibTableColumn
lm870CmajorHighTecCurrent = _Lm870CmajorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 70),
    _Lm870CmajorHighTecCurrent_Type()
)
lm870CmajorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorHighTecCurrent.setStatus("mandatory")
_Lm870CmajorLowTecCurrent_Type = Float
_Lm870CmajorLowTecCurrent_Object = MibTableColumn
lm870CmajorLowTecCurrent = _Lm870CmajorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 71),
    _Lm870CmajorLowTecCurrent_Type()
)
lm870CmajorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorLowTecCurrent.setStatus("mandatory")
_Lm870CminorHighTecCurrent_Type = Float
_Lm870CminorHighTecCurrent_Object = MibTableColumn
lm870CminorHighTecCurrent = _Lm870CminorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 72),
    _Lm870CminorHighTecCurrent_Type()
)
lm870CminorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorHighTecCurrent.setStatus("mandatory")
_Lm870CminorLowTecCurrent_Type = Float
_Lm870CminorLowTecCurrent_Object = MibTableColumn
lm870CminorLowTecCurrent = _Lm870CminorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 73),
    _Lm870CminorLowTecCurrent_Type()
)
lm870CminorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorLowTecCurrent.setStatus("mandatory")
_Lm870CcurrentValueTecCurrent_Type = Float
_Lm870CcurrentValueTecCurrent_Object = MibTableColumn
lm870CcurrentValueTecCurrent = _Lm870CcurrentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 74),
    _Lm870CcurrentValueTecCurrent_Type()
)
lm870CcurrentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CcurrentValueTecCurrent.setStatus("mandatory")


class _Lm870CstateFlagTecCurrent_Type(Integer32):
    """Custom type lm870CstateFlagTecCurrent based on Integer32"""
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


_Lm870CstateFlagTecCurrent_Type.__name__ = "Integer32"
_Lm870CstateFlagTecCurrent_Object = MibTableColumn
lm870CstateFlagTecCurrent = _Lm870CstateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 75),
    _Lm870CstateFlagTecCurrent_Type()
)
lm870CstateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagTecCurrent.setStatus("mandatory")
_Lm870CminValueTecCurrent_Type = Float
_Lm870CminValueTecCurrent_Object = MibTableColumn
lm870CminValueTecCurrent = _Lm870CminValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 76),
    _Lm870CminValueTecCurrent_Type()
)
lm870CminValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminValueTecCurrent.setStatus("mandatory")
_Lm870CmaxValueTecCurrent_Type = Float
_Lm870CmaxValueTecCurrent_Object = MibTableColumn
lm870CmaxValueTecCurrent = _Lm870CmaxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 77),
    _Lm870CmaxValueTecCurrent_Type()
)
lm870CmaxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmaxValueTecCurrent.setStatus("mandatory")


class _Lm870CalarmStateTecCurrent_Type(Integer32):
    """Custom type lm870CalarmStateTecCurrent based on Integer32"""
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


_Lm870CalarmStateTecCurrent_Type.__name__ = "Integer32"
_Lm870CalarmStateTecCurrent_Object = MibTableColumn
lm870CalarmStateTecCurrent = _Lm870CalarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 78),
    _Lm870CalarmStateTecCurrent_Type()
)
lm870CalarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CalarmStateTecCurrent.setStatus("mandatory")


class _Lm870ClabelOmiAlarmSetpoint_Type(DisplayString):
    """Custom type lm870ClabelOmiAlarmSetpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelOmiAlarmSetpoint_Type.__name__ = "DisplayString"
_Lm870ClabelOmiAlarmSetpoint_Object = MibTableColumn
lm870ClabelOmiAlarmSetpoint = _Lm870ClabelOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 79),
    _Lm870ClabelOmiAlarmSetpoint_Type()
)
lm870ClabelOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelOmiAlarmSetpoint.setStatus("optional")


class _Lm870CuomOmiAlarmSetpoint_Type(DisplayString):
    """Custom type lm870CuomOmiAlarmSetpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CuomOmiAlarmSetpoint_Type.__name__ = "DisplayString"
_Lm870CuomOmiAlarmSetpoint_Object = MibTableColumn
lm870CuomOmiAlarmSetpoint = _Lm870CuomOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 80),
    _Lm870CuomOmiAlarmSetpoint_Type()
)
lm870CuomOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CuomOmiAlarmSetpoint.setStatus("optional")
_Lm870CmajorHighOmiAlarmSetpoint_Type = Float
_Lm870CmajorHighOmiAlarmSetpoint_Object = MibTableColumn
lm870CmajorHighOmiAlarmSetpoint = _Lm870CmajorHighOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 81),
    _Lm870CmajorHighOmiAlarmSetpoint_Type()
)
lm870CmajorHighOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorHighOmiAlarmSetpoint.setStatus("mandatory")
_Lm870CmajorLowOmiAlarmSetpoint_Type = Float
_Lm870CmajorLowOmiAlarmSetpoint_Object = MibTableColumn
lm870CmajorLowOmiAlarmSetpoint = _Lm870CmajorLowOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 82),
    _Lm870CmajorLowOmiAlarmSetpoint_Type()
)
lm870CmajorLowOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmajorLowOmiAlarmSetpoint.setStatus("mandatory")
_Lm870CminorHighOmiAlarmSetpoint_Type = Float
_Lm870CminorHighOmiAlarmSetpoint_Object = MibTableColumn
lm870CminorHighOmiAlarmSetpoint = _Lm870CminorHighOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 83),
    _Lm870CminorHighOmiAlarmSetpoint_Type()
)
lm870CminorHighOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorHighOmiAlarmSetpoint.setStatus("mandatory")
_Lm870CminorLowOmiAlarmSetpoint_Type = Float
_Lm870CminorLowOmiAlarmSetpoint_Object = MibTableColumn
lm870CminorLowOmiAlarmSetpoint = _Lm870CminorLowOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 84),
    _Lm870CminorLowOmiAlarmSetpoint_Type()
)
lm870CminorLowOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminorLowOmiAlarmSetpoint.setStatus("mandatory")
_Lm870CcurrentValueOmiAlarmSetpoint_Type = Float
_Lm870CcurrentValueOmiAlarmSetpoint_Object = MibTableColumn
lm870CcurrentValueOmiAlarmSetpoint = _Lm870CcurrentValueOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 85),
    _Lm870CcurrentValueOmiAlarmSetpoint_Type()
)
lm870CcurrentValueOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CcurrentValueOmiAlarmSetpoint.setStatus("mandatory")


class _Lm870CstateFlagOmiAlarmSetpoint_Type(Integer32):
    """Custom type lm870CstateFlagOmiAlarmSetpoint based on Integer32"""
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


_Lm870CstateFlagOmiAlarmSetpoint_Type.__name__ = "Integer32"
_Lm870CstateFlagOmiAlarmSetpoint_Object = MibTableColumn
lm870CstateFlagOmiAlarmSetpoint = _Lm870CstateFlagOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 86),
    _Lm870CstateFlagOmiAlarmSetpoint_Type()
)
lm870CstateFlagOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagOmiAlarmSetpoint.setStatus("mandatory")
_Lm870CminValueOmiAlarmSetpoint_Type = Float
_Lm870CminValueOmiAlarmSetpoint_Object = MibTableColumn
lm870CminValueOmiAlarmSetpoint = _Lm870CminValueOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 87),
    _Lm870CminValueOmiAlarmSetpoint_Type()
)
lm870CminValueOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CminValueOmiAlarmSetpoint.setStatus("mandatory")
_Lm870CmaxValueOmiAlarmSetpoint_Type = Float
_Lm870CmaxValueOmiAlarmSetpoint_Object = MibTableColumn
lm870CmaxValueOmiAlarmSetpoint = _Lm870CmaxValueOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 88),
    _Lm870CmaxValueOmiAlarmSetpoint_Type()
)
lm870CmaxValueOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CmaxValueOmiAlarmSetpoint.setStatus("mandatory")


class _Lm870CalarmStateOmiAlarmSetpoint_Type(Integer32):
    """Custom type lm870CalarmStateOmiAlarmSetpoint based on Integer32"""
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


_Lm870CalarmStateOmiAlarmSetpoint_Type.__name__ = "Integer32"
_Lm870CalarmStateOmiAlarmSetpoint_Object = MibTableColumn
lm870CalarmStateOmiAlarmSetpoint = _Lm870CalarmStateOmiAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 2, 1, 89),
    _Lm870CalarmStateOmiAlarmSetpoint_Type()
)
lm870CalarmStateOmiAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CalarmStateOmiAlarmSetpoint.setStatus("mandatory")
_Gx2lm870CDigitalTable_Object = MibTable
gx2lm870CDigitalTable = _Gx2lm870CDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3)
)
if mibBuilder.loadTexts:
    gx2lm870CDigitalTable.setStatus("mandatory")
_Gx2lm870CDigitalEntry_Object = MibTableRow
gx2lm870CDigitalEntry = _Gx2lm870CDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2)
)
gx2lm870CDigitalEntry.setIndexNames(
    (0, "OMNI-gx2Lm870C-MIB", "gx2Lm870CDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2lm870CDigitalEntry.setStatus("mandatory")


class _Gx2Lm870CDigitalTableIndex_Type(Integer32):
    """Custom type gx2Lm870CDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Lm870CDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Lm870CDigitalTableIndex_Object = MibTableColumn
gx2Lm870CDigitalTableIndex = _Gx2Lm870CDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 1),
    _Gx2Lm870CDigitalTableIndex_Type()
)
gx2Lm870CDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm870CDigitalTableIndex.setStatus("mandatory")


class _Lm870ClabelOMIOffsetAlarms_Type(DisplayString):
    """Custom type lm870ClabelOMIOffsetAlarms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelOMIOffsetAlarms_Type.__name__ = "DisplayString"
_Lm870ClabelOMIOffsetAlarms_Object = MibTableColumn
lm870ClabelOMIOffsetAlarms = _Lm870ClabelOMIOffsetAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 2),
    _Lm870ClabelOMIOffsetAlarms_Type()
)
lm870ClabelOMIOffsetAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelOMIOffsetAlarms.setStatus("optional")


class _Lm870CenumOMIOffsetAlarms_Type(DisplayString):
    """Custom type lm870CenumOMIOffsetAlarms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CenumOMIOffsetAlarms_Type.__name__ = "DisplayString"
_Lm870CenumOMIOffsetAlarms_Object = MibTableColumn
lm870CenumOMIOffsetAlarms = _Lm870CenumOMIOffsetAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 3),
    _Lm870CenumOMIOffsetAlarms_Type()
)
lm870CenumOMIOffsetAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CenumOMIOffsetAlarms.setStatus("optional")


class _Lm870CvalueOMIOffsetAlarms_Type(Integer32):
    """Custom type lm870CvalueOMIOffsetAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("set", 3))
    )


_Lm870CvalueOMIOffsetAlarms_Type.__name__ = "Integer32"
_Lm870CvalueOMIOffsetAlarms_Object = MibTableColumn
lm870CvalueOMIOffsetAlarms = _Lm870CvalueOMIOffsetAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 4),
    _Lm870CvalueOMIOffsetAlarms_Type()
)
lm870CvalueOMIOffsetAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lm870CvalueOMIOffsetAlarms.setStatus("mandatory")


class _Lm870CstateFlagOMIOffsetAlarms_Type(Integer32):
    """Custom type lm870CstateFlagOMIOffsetAlarms based on Integer32"""
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


_Lm870CstateFlagOMIOffsetAlarms_Type.__name__ = "Integer32"
_Lm870CstateFlagOMIOffsetAlarms_Object = MibTableColumn
lm870CstateFlagOMIOffsetAlarms = _Lm870CstateFlagOMIOffsetAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 5),
    _Lm870CstateFlagOMIOffsetAlarms_Type()
)
lm870CstateFlagOMIOffsetAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagOMIOffsetAlarms.setStatus("mandatory")


class _Lm870ClabelFactoryDefault_Type(DisplayString):
    """Custom type lm870ClabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelFactoryDefault_Type.__name__ = "DisplayString"
_Lm870ClabelFactoryDefault_Object = MibTableColumn
lm870ClabelFactoryDefault = _Lm870ClabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 6),
    _Lm870ClabelFactoryDefault_Type()
)
lm870ClabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelFactoryDefault.setStatus("optional")


class _Lm870CenumFactoryDefault_Type(DisplayString):
    """Custom type lm870CenumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CenumFactoryDefault_Type.__name__ = "DisplayString"
_Lm870CenumFactoryDefault_Object = MibTableColumn
lm870CenumFactoryDefault = _Lm870CenumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 7),
    _Lm870CenumFactoryDefault_Type()
)
lm870CenumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CenumFactoryDefault.setStatus("optional")


class _Lm870CvalueFactoryDefault_Type(Integer32):
    """Custom type lm870CvalueFactoryDefault based on Integer32"""
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


_Lm870CvalueFactoryDefault_Type.__name__ = "Integer32"
_Lm870CvalueFactoryDefault_Object = MibTableColumn
lm870CvalueFactoryDefault = _Lm870CvalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 8),
    _Lm870CvalueFactoryDefault_Type()
)
lm870CvalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lm870CvalueFactoryDefault.setStatus("mandatory")


class _Lm870CstateFlagFactoryDefault_Type(Integer32):
    """Custom type lm870CstateFlagFactoryDefault based on Integer32"""
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


_Lm870CstateFlagFactoryDefault_Type.__name__ = "Integer32"
_Lm870CstateFlagFactoryDefault_Object = MibTableColumn
lm870CstateFlagFactoryDefault = _Lm870CstateFlagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 9),
    _Lm870CstateFlagFactoryDefault_Type()
)
lm870CstateFlagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagFactoryDefault.setStatus("mandatory")


class _Lm870ClabelOMISetpoint_Type(DisplayString):
    """Custom type lm870ClabelOMISetpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelOMISetpoint_Type.__name__ = "DisplayString"
_Lm870ClabelOMISetpoint_Object = MibTableColumn
lm870ClabelOMISetpoint = _Lm870ClabelOMISetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 10),
    _Lm870ClabelOMISetpoint_Type()
)
lm870ClabelOMISetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelOMISetpoint.setStatus("obsolete")


class _Lm870CenumOMISetpoint_Type(DisplayString):
    """Custom type lm870CenumOMISetpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CenumOMISetpoint_Type.__name__ = "DisplayString"
_Lm870CenumOMISetpoint_Object = MibTableColumn
lm870CenumOMISetpoint = _Lm870CenumOMISetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 11),
    _Lm870CenumOMISetpoint_Type()
)
lm870CenumOMISetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CenumOMISetpoint.setStatus("obsolete")
_Lm870CvalueOMISetpoint_Type = Integer32
_Lm870CvalueOMISetpoint_Object = MibTableColumn
lm870CvalueOMISetpoint = _Lm870CvalueOMISetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 12),
    _Lm870CvalueOMISetpoint_Type()
)
lm870CvalueOMISetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueOMISetpoint.setStatus("obsolete")


class _Lm870CstateFlagOMISetpoint_Type(Integer32):
    """Custom type lm870CstateFlagOMISetpoint based on Integer32"""
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


_Lm870CstateFlagOMISetpoint_Type.__name__ = "Integer32"
_Lm870CstateFlagOMISetpoint_Object = MibTableColumn
lm870CstateFlagOMISetpoint = _Lm870CstateFlagOMISetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 3, 2, 13),
    _Lm870CstateFlagOMISetpoint_Type()
)
lm870CstateFlagOMISetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateFlagOMISetpoint.setStatus("obsolete")
_Gx2lm870CStatusTable_Object = MibTable
gx2lm870CStatusTable = _Gx2lm870CStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4)
)
if mibBuilder.loadTexts:
    gx2lm870CStatusTable.setStatus("mandatory")
_Gx2lm870CStatusEntry_Object = MibTableRow
gx2lm870CStatusEntry = _Gx2lm870CStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3)
)
gx2lm870CStatusEntry.setIndexNames(
    (0, "OMNI-gx2Lm870C-MIB", "gx2Lm870CStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2lm870CStatusEntry.setStatus("mandatory")


class _Gx2Lm870CStatusTableIndex_Type(Integer32):
    """Custom type gx2Lm870CStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Lm870CStatusTableIndex_Type.__name__ = "Integer32"
_Gx2Lm870CStatusTableIndex_Object = MibTableColumn
gx2Lm870CStatusTableIndex = _Gx2Lm870CStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 1),
    _Gx2Lm870CStatusTableIndex_Type()
)
gx2Lm870CStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm870CStatusTableIndex.setStatus("mandatory")


class _Lm870ClabelBoot_Type(DisplayString):
    """Custom type lm870ClabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelBoot_Type.__name__ = "DisplayString"
_Lm870ClabelBoot_Object = MibTableColumn
lm870ClabelBoot = _Lm870ClabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 2),
    _Lm870ClabelBoot_Type()
)
lm870ClabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelBoot.setStatus("optional")


class _Lm870CvalueBoot_Type(Integer32):
    """Custom type lm870CvalueBoot based on Integer32"""
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


_Lm870CvalueBoot_Type.__name__ = "Integer32"
_Lm870CvalueBoot_Object = MibTableColumn
lm870CvalueBoot = _Lm870CvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 3),
    _Lm870CvalueBoot_Type()
)
lm870CvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueBoot.setStatus("mandatory")


class _Lm870CstateflagBoot_Type(Integer32):
    """Custom type lm870CstateflagBoot based on Integer32"""
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


_Lm870CstateflagBoot_Type.__name__ = "Integer32"
_Lm870CstateflagBoot_Object = MibTableColumn
lm870CstateflagBoot = _Lm870CstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 4),
    _Lm870CstateflagBoot_Type()
)
lm870CstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateflagBoot.setStatus("mandatory")


class _Lm870ClabelFlash_Type(DisplayString):
    """Custom type lm870ClabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelFlash_Type.__name__ = "DisplayString"
_Lm870ClabelFlash_Object = MibTableColumn
lm870ClabelFlash = _Lm870ClabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 5),
    _Lm870ClabelFlash_Type()
)
lm870ClabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelFlash.setStatus("optional")


class _Lm870CvalueFlash_Type(Integer32):
    """Custom type lm870CvalueFlash based on Integer32"""
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


_Lm870CvalueFlash_Type.__name__ = "Integer32"
_Lm870CvalueFlash_Object = MibTableColumn
lm870CvalueFlash = _Lm870CvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 6),
    _Lm870CvalueFlash_Type()
)
lm870CvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueFlash.setStatus("mandatory")


class _Lm870CstateflagFlash_Type(Integer32):
    """Custom type lm870CstateflagFlash based on Integer32"""
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


_Lm870CstateflagFlash_Type.__name__ = "Integer32"
_Lm870CstateflagFlash_Object = MibTableColumn
lm870CstateflagFlash = _Lm870CstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 7),
    _Lm870CstateflagFlash_Type()
)
lm870CstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateflagFlash.setStatus("mandatory")


class _Lm870ClabelRFOverload_Type(DisplayString):
    """Custom type lm870ClabelRFOverload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelRFOverload_Type.__name__ = "DisplayString"
_Lm870ClabelRFOverload_Object = MibTableColumn
lm870ClabelRFOverload = _Lm870ClabelRFOverload_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 8),
    _Lm870ClabelRFOverload_Type()
)
lm870ClabelRFOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelRFOverload.setStatus("optional")


class _Lm870CvalueRFOverload_Type(Integer32):
    """Custom type lm870CvalueRFOverload based on Integer32"""
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


_Lm870CvalueRFOverload_Type.__name__ = "Integer32"
_Lm870CvalueRFOverload_Object = MibTableColumn
lm870CvalueRFOverload = _Lm870CvalueRFOverload_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 9),
    _Lm870CvalueRFOverload_Type()
)
lm870CvalueRFOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueRFOverload.setStatus("mandatory")


class _Lm870CstateflagRFOverload_Type(Integer32):
    """Custom type lm870CstateflagRFOverload based on Integer32"""
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


_Lm870CstateflagRFOverload_Type.__name__ = "Integer32"
_Lm870CstateflagRFOverload_Object = MibTableColumn
lm870CstateflagRFOverload = _Lm870CstateflagRFOverload_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 10),
    _Lm870CstateflagRFOverload_Type()
)
lm870CstateflagRFOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateflagRFOverload.setStatus("mandatory")


class _Lm870ClabelRFPower_Type(DisplayString):
    """Custom type lm870ClabelRFPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelRFPower_Type.__name__ = "DisplayString"
_Lm870ClabelRFPower_Object = MibTableColumn
lm870ClabelRFPower = _Lm870ClabelRFPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 11),
    _Lm870ClabelRFPower_Type()
)
lm870ClabelRFPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelRFPower.setStatus("optional")


class _Lm870CvalueRFPower_Type(Integer32):
    """Custom type lm870CvalueRFPower based on Integer32"""
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


_Lm870CvalueRFPower_Type.__name__ = "Integer32"
_Lm870CvalueRFPower_Object = MibTableColumn
lm870CvalueRFPower = _Lm870CvalueRFPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 12),
    _Lm870CvalueRFPower_Type()
)
lm870CvalueRFPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueRFPower.setStatus("mandatory")


class _Lm870CstateflagRFPower_Type(Integer32):
    """Custom type lm870CstateflagRFPower based on Integer32"""
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


_Lm870CstateflagRFPower_Type.__name__ = "Integer32"
_Lm870CstateflagRFPower_Object = MibTableColumn
lm870CstateflagRFPower = _Lm870CstateflagRFPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 13),
    _Lm870CstateflagRFPower_Type()
)
lm870CstateflagRFPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateflagRFPower.setStatus("mandatory")


class _Lm870ClabelFactoryDataCRC_Type(DisplayString):
    """Custom type lm870ClabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelFactoryDataCRC_Type.__name__ = "DisplayString"
_Lm870ClabelFactoryDataCRC_Object = MibTableColumn
lm870ClabelFactoryDataCRC = _Lm870ClabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 14),
    _Lm870ClabelFactoryDataCRC_Type()
)
lm870ClabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelFactoryDataCRC.setStatus("optional")


class _Lm870CvalueFactoryDataCRC_Type(Integer32):
    """Custom type lm870CvalueFactoryDataCRC based on Integer32"""
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


_Lm870CvalueFactoryDataCRC_Type.__name__ = "Integer32"
_Lm870CvalueFactoryDataCRC_Object = MibTableColumn
lm870CvalueFactoryDataCRC = _Lm870CvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 15),
    _Lm870CvalueFactoryDataCRC_Type()
)
lm870CvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueFactoryDataCRC.setStatus("mandatory")


class _Lm870CstateflagFactoryDataCRC_Type(Integer32):
    """Custom type lm870CstateflagFactoryDataCRC based on Integer32"""
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


_Lm870CstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Lm870CstateflagFactoryDataCRC_Object = MibTableColumn
lm870CstateflagFactoryDataCRC = _Lm870CstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 16),
    _Lm870CstateflagFactoryDataCRC_Type()
)
lm870CstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateflagFactoryDataCRC.setStatus("mandatory")


class _Lm870ClabelAlarmDataCrc_Type(DisplayString):
    """Custom type lm870ClabelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelAlarmDataCrc_Type.__name__ = "DisplayString"
_Lm870ClabelAlarmDataCrc_Object = MibTableColumn
lm870ClabelAlarmDataCrc = _Lm870ClabelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 17),
    _Lm870ClabelAlarmDataCrc_Type()
)
lm870ClabelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelAlarmDataCrc.setStatus("optional")


class _Lm870CvalueAlarmDataCrc_Type(Integer32):
    """Custom type lm870CvalueAlarmDataCrc based on Integer32"""
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


_Lm870CvalueAlarmDataCrc_Type.__name__ = "Integer32"
_Lm870CvalueAlarmDataCrc_Object = MibTableColumn
lm870CvalueAlarmDataCrc = _Lm870CvalueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 18),
    _Lm870CvalueAlarmDataCrc_Type()
)
lm870CvalueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueAlarmDataCrc.setStatus("mandatory")


class _Lm870CstateflagAlarmDataCrc_Type(Integer32):
    """Custom type lm870CstateflagAlarmDataCrc based on Integer32"""
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


_Lm870CstateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Lm870CstateflagAlarmDataCrc_Object = MibTableColumn
lm870CstateflagAlarmDataCrc = _Lm870CstateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 19),
    _Lm870CstateflagAlarmDataCrc_Type()
)
lm870CstateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateflagAlarmDataCrc.setStatus("mandatory")


class _Lm870ClabelModSetDataCRC_Type(DisplayString):
    """Custom type lm870ClabelModSetDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelModSetDataCRC_Type.__name__ = "DisplayString"
_Lm870ClabelModSetDataCRC_Object = MibTableColumn
lm870ClabelModSetDataCRC = _Lm870ClabelModSetDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 20),
    _Lm870ClabelModSetDataCRC_Type()
)
lm870ClabelModSetDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelModSetDataCRC.setStatus("optional")


class _Lm870CvalueModSetDataCRC_Type(Integer32):
    """Custom type lm870CvalueModSetDataCRC based on Integer32"""
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


_Lm870CvalueModSetDataCRC_Type.__name__ = "Integer32"
_Lm870CvalueModSetDataCRC_Object = MibTableColumn
lm870CvalueModSetDataCRC = _Lm870CvalueModSetDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 21),
    _Lm870CvalueModSetDataCRC_Type()
)
lm870CvalueModSetDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueModSetDataCRC.setStatus("mandatory")


class _Lm870CstateflagModSetDataCRC_Type(Integer32):
    """Custom type lm870CstateflagModSetDataCRC based on Integer32"""
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


_Lm870CstateflagModSetDataCRC_Type.__name__ = "Integer32"
_Lm870CstateflagModSetDataCRC_Object = MibTableColumn
lm870CstateflagModSetDataCRC = _Lm870CstateflagModSetDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 22),
    _Lm870CstateflagModSetDataCRC_Type()
)
lm870CstateflagModSetDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateflagModSetDataCRC.setStatus("mandatory")


class _Lm870ClabelOptCalDataCRC_Type(DisplayString):
    """Custom type lm870ClabelOptCalDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelOptCalDataCRC_Type.__name__ = "DisplayString"
_Lm870ClabelOptCalDataCRC_Object = MibTableColumn
lm870ClabelOptCalDataCRC = _Lm870ClabelOptCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 23),
    _Lm870ClabelOptCalDataCRC_Type()
)
lm870ClabelOptCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelOptCalDataCRC.setStatus("optional")


class _Lm870CvalueOptCalDataCRC_Type(Integer32):
    """Custom type lm870CvalueOptCalDataCRC based on Integer32"""
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


_Lm870CvalueOptCalDataCRC_Type.__name__ = "Integer32"
_Lm870CvalueOptCalDataCRC_Object = MibTableColumn
lm870CvalueOptCalDataCRC = _Lm870CvalueOptCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 24),
    _Lm870CvalueOptCalDataCRC_Type()
)
lm870CvalueOptCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueOptCalDataCRC.setStatus("mandatory")


class _Lm870CstateflagOptCalDataCRC_Type(Integer32):
    """Custom type lm870CstateflagOptCalDataCRC based on Integer32"""
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


_Lm870CstateflagOptCalDataCRC_Type.__name__ = "Integer32"
_Lm870CstateflagOptCalDataCRC_Object = MibTableColumn
lm870CstateflagOptCalDataCRC = _Lm870CstateflagOptCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 25),
    _Lm870CstateflagOptCalDataCRC_Type()
)
lm870CstateflagOptCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateflagOptCalDataCRC.setStatus("mandatory")


class _Lm870ClabelRFCalDataCRC_Type(DisplayString):
    """Custom type lm870ClabelRFCalDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870ClabelRFCalDataCRC_Type.__name__ = "DisplayString"
_Lm870ClabelRFCalDataCRC_Object = MibTableColumn
lm870ClabelRFCalDataCRC = _Lm870ClabelRFCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 26),
    _Lm870ClabelRFCalDataCRC_Type()
)
lm870ClabelRFCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ClabelRFCalDataCRC.setStatus("optional")


class _Lm870CvalueRFCalDataCRC_Type(Integer32):
    """Custom type lm870CvalueRFCalDataCRC based on Integer32"""
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


_Lm870CvalueRFCalDataCRC_Type.__name__ = "Integer32"
_Lm870CvalueRFCalDataCRC_Object = MibTableColumn
lm870CvalueRFCalDataCRC = _Lm870CvalueRFCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 27),
    _Lm870CvalueRFCalDataCRC_Type()
)
lm870CvalueRFCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CvalueRFCalDataCRC.setStatus("mandatory")


class _Lm870CstateflagRFCalDataCRC_Type(Integer32):
    """Custom type lm870CstateflagRFCalDataCRC based on Integer32"""
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


_Lm870CstateflagRFCalDataCRC_Type.__name__ = "Integer32"
_Lm870CstateflagRFCalDataCRC_Object = MibTableColumn
lm870CstateflagRFCalDataCRC = _Lm870CstateflagRFCalDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 4, 3, 28),
    _Lm870CstateflagRFCalDataCRC_Type()
)
lm870CstateflagRFCalDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CstateflagRFCalDataCRC.setStatus("mandatory")
_Gx2lm870CFactoryTable_Object = MibTable
gx2lm870CFactoryTable = _Gx2lm870CFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5)
)
if mibBuilder.loadTexts:
    gx2lm870CFactoryTable.setStatus("mandatory")
_Gx2lm870CFactoryEntry_Object = MibTableRow
gx2lm870CFactoryEntry = _Gx2lm870CFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4)
)
gx2lm870CFactoryEntry.setIndexNames(
    (0, "OMNI-gx2Lm870C-MIB", "gx2Lm870CFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2lm870CFactoryEntry.setStatus("mandatory")


class _Gx2Lm870CFactoryTableIndex_Type(Integer32):
    """Custom type gx2Lm870CFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Lm870CFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Lm870CFactoryTableIndex_Object = MibTableColumn
gx2Lm870CFactoryTableIndex = _Gx2Lm870CFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 1),
    _Gx2Lm870CFactoryTableIndex_Type()
)
gx2Lm870CFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm870CFactoryTableIndex.setStatus("mandatory")
_Lm870CbootControlByte_Type = Integer32
_Lm870CbootControlByte_Object = MibTableColumn
lm870CbootControlByte = _Lm870CbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 2),
    _Lm870CbootControlByte_Type()
)
lm870CbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CbootControlByte.setStatus("mandatory")
_Lm870CbootStatusByte_Type = Integer32
_Lm870CbootStatusByte_Object = MibTableColumn
lm870CbootStatusByte = _Lm870CbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 3),
    _Lm870CbootStatusByte_Type()
)
lm870CbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CbootStatusByte.setStatus("mandatory")
_Lm870Cbank1CRC_Type = Integer32
_Lm870Cbank1CRC_Object = MibTableColumn
lm870Cbank1CRC = _Lm870Cbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 4),
    _Lm870Cbank1CRC_Type()
)
lm870Cbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870Cbank1CRC.setStatus("mandatory")
_Lm870Cbank2CRC_Type = Integer32
_Lm870Cbank2CRC_Object = MibTableColumn
lm870Cbank2CRC = _Lm870Cbank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 5),
    _Lm870Cbank2CRC_Type()
)
lm870Cbank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870Cbank2CRC.setStatus("mandatory")
_Lm870CprgEEPROMByte_Type = Integer32
_Lm870CprgEEPROMByte_Object = MibTableColumn
lm870CprgEEPROMByte = _Lm870CprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 6),
    _Lm870CprgEEPROMByte_Type()
)
lm870CprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CprgEEPROMByte.setStatus("mandatory")
_Lm870CfactoryCRC_Type = Integer32
_Lm870CfactoryCRC_Object = MibTableColumn
lm870CfactoryCRC = _Lm870CfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 7),
    _Lm870CfactoryCRC_Type()
)
lm870CfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CfactoryCRC.setStatus("mandatory")


class _Lm870CcalculateCRC_Type(Integer32):
    """Custom type lm870CcalculateCRC based on Integer32"""
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
        *(("alarm", 3),
          ("factory", 1),
          ("opticalCal", 4),
          ("rfCal", 5),
          ("settings", 2))
    )


_Lm870CcalculateCRC_Type.__name__ = "Integer32"
_Lm870CcalculateCRC_Object = MibTableColumn
lm870CcalculateCRC = _Lm870CcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 8),
    _Lm870CcalculateCRC_Type()
)
lm870CcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CcalculateCRC.setStatus("mandatory")
_Lm870ChourMeter_Type = Integer32
_Lm870ChourMeter_Object = MibTableColumn
lm870ChourMeter = _Lm870ChourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 9),
    _Lm870ChourMeter_Type()
)
lm870ChourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870ChourMeter.setStatus("mandatory")
_Lm870CflashPrgCntA_Type = Integer32
_Lm870CflashPrgCntA_Object = MibTableColumn
lm870CflashPrgCntA = _Lm870CflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 10),
    _Lm870CflashPrgCntA_Type()
)
lm870CflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CflashPrgCntA.setStatus("mandatory")
_Lm870CflashPrgCntB_Type = Integer32
_Lm870CflashPrgCntB_Object = MibTableColumn
lm870CflashPrgCntB = _Lm870CflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 11),
    _Lm870CflashPrgCntB_Type()
)
lm870CflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CflashPrgCntB.setStatus("mandatory")


class _Lm870CflashBankARev_Type(DisplayString):
    """Custom type lm870CflashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CflashBankARev_Type.__name__ = "DisplayString"
_Lm870CflashBankARev_Object = MibTableColumn
lm870CflashBankARev = _Lm870CflashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 12),
    _Lm870CflashBankARev_Type()
)
lm870CflashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CflashBankARev.setStatus("mandatory")


class _Lm870CflashBankBRev_Type(DisplayString):
    """Custom type lm870CflashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lm870CflashBankBRev_Type.__name__ = "DisplayString"
_Lm870CflashBankBRev_Object = MibTableColumn
lm870CflashBankBRev = _Lm870CflashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 5, 4, 13),
    _Lm870CflashBankBRev_Type()
)
lm870CflashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lm870CflashBankBRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapLM870CConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 1)
)
trapLM870CConfigChangeInteger.setObjects(
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
    trapLM870CConfigChangeInteger.setStatus(
        ""
    )

trapLMCConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 2)
)
trapLMCConfigChangeDisplayString.setObjects(
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
    trapLMCConfigChangeDisplayString.setStatus(
        ""
    )

trapLMCFanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 3)
)
trapLMCFanCurrentAlarm.setObjects(
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
    trapLMCFanCurrentAlarm.setStatus(
        ""
    )

trapLMC12vAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 4)
)
trapLMC12vAlarm.setObjects(
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
    trapLMC12vAlarm.setStatus(
        ""
    )

trapLMCModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 5)
)
trapLMCModuleTempAlarm.setObjects(
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
    trapLMCModuleTempAlarm.setStatus(
        ""
    )

trapLMCRFPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 6)
)
trapLMCRFPowerAlarm.setObjects(
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
    trapLMCRFPowerAlarm.setStatus(
        ""
    )

trapLMCOPTPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 7)
)
trapLMCOPTPowerAlarm.setObjects(
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
    trapLMCOPTPowerAlarm.setStatus(
        ""
    )

trapLMCLaserBiasAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 8)
)
trapLMCLaserBiasAlarm.setObjects(
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
    trapLMCLaserBiasAlarm.setStatus(
        ""
    )

trapLMCTECCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 9)
)
trapLMCTECCurrentAlarm.setObjects(
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
    trapLMCTECCurrentAlarm.setStatus(
        ""
    )

trapLMCFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 10)
)
trapLMCFlashAlarm.setObjects(
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
    trapLMCFlashAlarm.setStatus(
        ""
    )

trapLMCBankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 11)
)
trapLMCBankBootAlarm.setObjects(
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
    trapLMCBankBootAlarm.setStatus(
        ""
    )

trapLMCAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 12)
)
trapLMCAlarmDataCRCAlarm.setObjects(
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
    trapLMCAlarmDataCRCAlarm.setStatus(
        ""
    )

trapLMCModSetDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 13)
)
trapLMCModSetDataCRCAlarm.setObjects(
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
    trapLMCModSetDataCRCAlarm.setStatus(
        ""
    )

trapLMCFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 14)
)
trapLMCFactoryDataCRCAlarm.setObjects(
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
    trapLMCFactoryDataCRCAlarm.setStatus(
        ""
    )

trapLMCResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 15)
)
trapLMCResetFactoryDefaultAlarm.setObjects(
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
    trapLMCResetFactoryDefaultAlarm.setStatus(
        ""
    )

trapLMCOPCalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 16)
)
trapLMCOPCalDataCRCAlarm.setObjects(
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
    trapLMCOPCalDataCRCAlarm.setStatus(
        ""
    )

trapLMCRFCalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 17)
)
trapLMCRFCalDataCRCAlarm.setObjects(
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
    trapLMCRFCalDataCRCAlarm.setStatus(
        ""
    )

trapLMCRFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 18)
)
trapLMCRFOverloadAlarm.setObjects(
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
    trapLMCRFOverloadAlarm.setStatus(
        ""
    )

trapLMCOMIoffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10, 0, 19)
)
trapLMCOMIoffsetAlarm.setObjects(
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
    trapLMCOMIoffsetAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2Lm870C-MIB",
    **{"Float": Float,
       "trapLM870CConfigChangeInteger": trapLM870CConfigChangeInteger,
       "trapLMCConfigChangeDisplayString": trapLMCConfigChangeDisplayString,
       "trapLMCFanCurrentAlarm": trapLMCFanCurrentAlarm,
       "trapLMC12vAlarm": trapLMC12vAlarm,
       "trapLMCModuleTempAlarm": trapLMCModuleTempAlarm,
       "trapLMCRFPowerAlarm": trapLMCRFPowerAlarm,
       "trapLMCOPTPowerAlarm": trapLMCOPTPowerAlarm,
       "trapLMCLaserBiasAlarm": trapLMCLaserBiasAlarm,
       "trapLMCTECCurrentAlarm": trapLMCTECCurrentAlarm,
       "trapLMCFlashAlarm": trapLMCFlashAlarm,
       "trapLMCBankBootAlarm": trapLMCBankBootAlarm,
       "trapLMCAlarmDataCRCAlarm": trapLMCAlarmDataCRCAlarm,
       "trapLMCModSetDataCRCAlarm": trapLMCModSetDataCRCAlarm,
       "trapLMCFactoryDataCRCAlarm": trapLMCFactoryDataCRCAlarm,
       "trapLMCResetFactoryDefaultAlarm": trapLMCResetFactoryDefaultAlarm,
       "trapLMCOPCalDataCRCAlarm": trapLMCOPCalDataCRCAlarm,
       "trapLMCRFCalDataCRCAlarm": trapLMCRFCalDataCRCAlarm,
       "trapLMCRFOverloadAlarm": trapLMCRFOverloadAlarm,
       "trapLMCOMIoffsetAlarm": trapLMCOMIoffsetAlarm,
       "gx2Lm870CDescriptor": gx2Lm870CDescriptor,
       "gx2lm870CAnalogTable": gx2lm870CAnalogTable,
       "gx2lm870CAnalogEntry": gx2lm870CAnalogEntry,
       "gx2Lm870CAnalogTableIndex": gx2Lm870CAnalogTableIndex,
       "lm870ClabelFanCurrent": lm870ClabelFanCurrent,
       "lm870CuomFanCurrent": lm870CuomFanCurrent,
       "lm870CmajorHighFanCurrent": lm870CmajorHighFanCurrent,
       "lm870CmajorLowFanCurrent": lm870CmajorLowFanCurrent,
       "lm870CminorHighFanCurrent": lm870CminorHighFanCurrent,
       "lm870CminorLowFanCurrent": lm870CminorLowFanCurrent,
       "lm870CcurrentValueFanCurrent": lm870CcurrentValueFanCurrent,
       "lm870CstateFlagFanCurrent": lm870CstateFlagFanCurrent,
       "lm870CminValueFanCurrent": lm870CminValueFanCurrent,
       "lm870CmaxValueFanCurrent": lm870CmaxValueFanCurrent,
       "lm870CalarmStateFanCurrent": lm870CalarmStateFanCurrent,
       "lm870Clabel12Volt": lm870Clabel12Volt,
       "lm870Cuom12Volt": lm870Cuom12Volt,
       "lm870CmajorHigh12Volt": lm870CmajorHigh12Volt,
       "lm870CmajorLow12Volt": lm870CmajorLow12Volt,
       "lm870CminorHigh12Volt": lm870CminorHigh12Volt,
       "lm870CminorLow12Volt": lm870CminorLow12Volt,
       "lm870CcurrentValue12Volt": lm870CcurrentValue12Volt,
       "lm870CstateFlag12Volt": lm870CstateFlag12Volt,
       "lm870CminValue12Volt": lm870CminValue12Volt,
       "lm870CmaxValue12Volt": lm870CmaxValue12Volt,
       "lm870CalarmState12Volt": lm870CalarmState12Volt,
       "lm870ClabelModTemp": lm870ClabelModTemp,
       "lm870CuomModTemp": lm870CuomModTemp,
       "lm870CmajorHighModTemp": lm870CmajorHighModTemp,
       "lm870CmajorLowModTemp": lm870CmajorLowModTemp,
       "lm870CminorHighModTemp": lm870CminorHighModTemp,
       "lm870CminorLowModTemp": lm870CminorLowModTemp,
       "lm870CcurrentValueModTemp": lm870CcurrentValueModTemp,
       "lm870CstateFlagModTemp": lm870CstateFlagModTemp,
       "lm870CminValueModTemp": lm870CminValueModTemp,
       "lm870CmaxValueModTemp": lm870CmaxValueModTemp,
       "lm870CalarmStateModTemp": lm870CalarmStateModTemp,
       "lm870ClabelOmiOffset": lm870ClabelOmiOffset,
       "lm870CuomOmiOffset": lm870CuomOmiOffset,
       "lm870CmajorHighOmiOffset": lm870CmajorHighOmiOffset,
       "lm870CmajorLowOmiOffset": lm870CmajorLowOmiOffset,
       "lm870CminorHighOmiOffset": lm870CminorHighOmiOffset,
       "lm870CminorLowOmiOffset": lm870CminorLowOmiOffset,
       "lm870CcurrentValueOmiOffset": lm870CcurrentValueOmiOffset,
       "lm870CstateFlagOmiOffset": lm870CstateFlagOmiOffset,
       "lm870CminValueOmiOffset": lm870CminValueOmiOffset,
       "lm870CmaxValueOmiOffset": lm870CmaxValueOmiOffset,
       "lm870CalarmStateOmiOffset": lm870CalarmStateOmiOffset,
       "lm870ClabelOPTPower": lm870ClabelOPTPower,
       "lm870CuomOPTPower": lm870CuomOPTPower,
       "lm870CmajorHighOPTPower": lm870CmajorHighOPTPower,
       "lm870CmajorLowOPTPower": lm870CmajorLowOPTPower,
       "lm870CminorHighOPTPower": lm870CminorHighOPTPower,
       "lm870CminorLowOPTPower": lm870CminorLowOPTPower,
       "lm870CcurrentValueOPTPower": lm870CcurrentValueOPTPower,
       "lm870CstateFlagOPTPower": lm870CstateFlagOPTPower,
       "lm870CminValueOPTPower": lm870CminValueOPTPower,
       "lm870CmaxValueOPTPower": lm870CmaxValueOPTPower,
       "lm870CalarmStateOPTPower": lm870CalarmStateOPTPower,
       "lm870ClabelLaserBias": lm870ClabelLaserBias,
       "lm870CuomLaserBias": lm870CuomLaserBias,
       "lm870CmajorHighLaserBias": lm870CmajorHighLaserBias,
       "lm870CmajorLowLaserBias": lm870CmajorLowLaserBias,
       "lm870CminorHighLaserBias": lm870CminorHighLaserBias,
       "lm870CminorLowLaserBias": lm870CminorLowLaserBias,
       "lm870CcurrentValueLaserBias": lm870CcurrentValueLaserBias,
       "lm870CstateFlagLaserBias": lm870CstateFlagLaserBias,
       "lm870CminValueLaserBias": lm870CminValueLaserBias,
       "lm870CmaxValueLaserBias": lm870CmaxValueLaserBias,
       "lm870CalarmStateLaserBias": lm870CalarmStateLaserBias,
       "lm870ClabelTecCurrent": lm870ClabelTecCurrent,
       "lm870CuomTecCurrent": lm870CuomTecCurrent,
       "lm870CmajorHighTecCurrent": lm870CmajorHighTecCurrent,
       "lm870CmajorLowTecCurrent": lm870CmajorLowTecCurrent,
       "lm870CminorHighTecCurrent": lm870CminorHighTecCurrent,
       "lm870CminorLowTecCurrent": lm870CminorLowTecCurrent,
       "lm870CcurrentValueTecCurrent": lm870CcurrentValueTecCurrent,
       "lm870CstateFlagTecCurrent": lm870CstateFlagTecCurrent,
       "lm870CminValueTecCurrent": lm870CminValueTecCurrent,
       "lm870CmaxValueTecCurrent": lm870CmaxValueTecCurrent,
       "lm870CalarmStateTecCurrent": lm870CalarmStateTecCurrent,
       "lm870ClabelOmiAlarmSetpoint": lm870ClabelOmiAlarmSetpoint,
       "lm870CuomOmiAlarmSetpoint": lm870CuomOmiAlarmSetpoint,
       "lm870CmajorHighOmiAlarmSetpoint": lm870CmajorHighOmiAlarmSetpoint,
       "lm870CmajorLowOmiAlarmSetpoint": lm870CmajorLowOmiAlarmSetpoint,
       "lm870CminorHighOmiAlarmSetpoint": lm870CminorHighOmiAlarmSetpoint,
       "lm870CminorLowOmiAlarmSetpoint": lm870CminorLowOmiAlarmSetpoint,
       "lm870CcurrentValueOmiAlarmSetpoint": lm870CcurrentValueOmiAlarmSetpoint,
       "lm870CstateFlagOmiAlarmSetpoint": lm870CstateFlagOmiAlarmSetpoint,
       "lm870CminValueOmiAlarmSetpoint": lm870CminValueOmiAlarmSetpoint,
       "lm870CmaxValueOmiAlarmSetpoint": lm870CmaxValueOmiAlarmSetpoint,
       "lm870CalarmStateOmiAlarmSetpoint": lm870CalarmStateOmiAlarmSetpoint,
       "gx2lm870CDigitalTable": gx2lm870CDigitalTable,
       "gx2lm870CDigitalEntry": gx2lm870CDigitalEntry,
       "gx2Lm870CDigitalTableIndex": gx2Lm870CDigitalTableIndex,
       "lm870ClabelOMIOffsetAlarms": lm870ClabelOMIOffsetAlarms,
       "lm870CenumOMIOffsetAlarms": lm870CenumOMIOffsetAlarms,
       "lm870CvalueOMIOffsetAlarms": lm870CvalueOMIOffsetAlarms,
       "lm870CstateFlagOMIOffsetAlarms": lm870CstateFlagOMIOffsetAlarms,
       "lm870ClabelFactoryDefault": lm870ClabelFactoryDefault,
       "lm870CenumFactoryDefault": lm870CenumFactoryDefault,
       "lm870CvalueFactoryDefault": lm870CvalueFactoryDefault,
       "lm870CstateFlagFactoryDefault": lm870CstateFlagFactoryDefault,
       "lm870ClabelOMISetpoint": lm870ClabelOMISetpoint,
       "lm870CenumOMISetpoint": lm870CenumOMISetpoint,
       "lm870CvalueOMISetpoint": lm870CvalueOMISetpoint,
       "lm870CstateFlagOMISetpoint": lm870CstateFlagOMISetpoint,
       "gx2lm870CStatusTable": gx2lm870CStatusTable,
       "gx2lm870CStatusEntry": gx2lm870CStatusEntry,
       "gx2Lm870CStatusTableIndex": gx2Lm870CStatusTableIndex,
       "lm870ClabelBoot": lm870ClabelBoot,
       "lm870CvalueBoot": lm870CvalueBoot,
       "lm870CstateflagBoot": lm870CstateflagBoot,
       "lm870ClabelFlash": lm870ClabelFlash,
       "lm870CvalueFlash": lm870CvalueFlash,
       "lm870CstateflagFlash": lm870CstateflagFlash,
       "lm870ClabelRFOverload": lm870ClabelRFOverload,
       "lm870CvalueRFOverload": lm870CvalueRFOverload,
       "lm870CstateflagRFOverload": lm870CstateflagRFOverload,
       "lm870ClabelRFPower": lm870ClabelRFPower,
       "lm870CvalueRFPower": lm870CvalueRFPower,
       "lm870CstateflagRFPower": lm870CstateflagRFPower,
       "lm870ClabelFactoryDataCRC": lm870ClabelFactoryDataCRC,
       "lm870CvalueFactoryDataCRC": lm870CvalueFactoryDataCRC,
       "lm870CstateflagFactoryDataCRC": lm870CstateflagFactoryDataCRC,
       "lm870ClabelAlarmDataCrc": lm870ClabelAlarmDataCrc,
       "lm870CvalueAlarmDataCrc": lm870CvalueAlarmDataCrc,
       "lm870CstateflagAlarmDataCrc": lm870CstateflagAlarmDataCrc,
       "lm870ClabelModSetDataCRC": lm870ClabelModSetDataCRC,
       "lm870CvalueModSetDataCRC": lm870CvalueModSetDataCRC,
       "lm870CstateflagModSetDataCRC": lm870CstateflagModSetDataCRC,
       "lm870ClabelOptCalDataCRC": lm870ClabelOptCalDataCRC,
       "lm870CvalueOptCalDataCRC": lm870CvalueOptCalDataCRC,
       "lm870CstateflagOptCalDataCRC": lm870CstateflagOptCalDataCRC,
       "lm870ClabelRFCalDataCRC": lm870ClabelRFCalDataCRC,
       "lm870CvalueRFCalDataCRC": lm870CvalueRFCalDataCRC,
       "lm870CstateflagRFCalDataCRC": lm870CstateflagRFCalDataCRC,
       "gx2lm870CFactoryTable": gx2lm870CFactoryTable,
       "gx2lm870CFactoryEntry": gx2lm870CFactoryEntry,
       "gx2Lm870CFactoryTableIndex": gx2Lm870CFactoryTableIndex,
       "lm870CbootControlByte": lm870CbootControlByte,
       "lm870CbootStatusByte": lm870CbootStatusByte,
       "lm870Cbank1CRC": lm870Cbank1CRC,
       "lm870Cbank2CRC": lm870Cbank2CRC,
       "lm870CprgEEPROMByte": lm870CprgEEPROMByte,
       "lm870CfactoryCRC": lm870CfactoryCRC,
       "lm870CcalculateCRC": lm870CcalculateCRC,
       "lm870ChourMeter": lm870ChourMeter,
       "lm870CflashPrgCntA": lm870CflashPrgCntA,
       "lm870CflashPrgCntB": lm870CflashPrgCntB,
       "lm870CflashBankARev": lm870CflashBankARev,
       "lm870CflashBankBRev": lm870CflashBankBRev}
)
