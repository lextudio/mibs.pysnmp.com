# SNMP MIB module (OMNI-gx2RX200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2RX200-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:34 2024
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

(gx2Rx200,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Rx200")

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




class U32Data(Counter32):
    """Custom type U32Data based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gx2Rx200Descriptor_ObjectIdentity = ObjectIdentity
gx2Rx200Descriptor = _Gx2Rx200Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 1)
)
_Gx2Rx200AnalogTable_Object = MibTable
gx2Rx200AnalogTable = _Gx2Rx200AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    gx2Rx200AnalogTable.setStatus("mandatory")
_Gx2Rx200AnalogEntry_Object = MibTableRow
gx2Rx200AnalogEntry = _Gx2Rx200AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1)
)
gx2Rx200AnalogEntry.setIndexNames(
    (0, "OMNI-gx2RX200-MIB", "rxgx2Rx200AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx200AnalogEntry.setStatus("mandatory")


class _Rxgx2Rx200AnalogTableIndex_Type(Integer32):
    """Custom type rxgx2Rx200AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rx200AnalogTableIndex_Type.__name__ = "Integer32"
_Rxgx2Rx200AnalogTableIndex_Object = MibTableColumn
rxgx2Rx200AnalogTableIndex = _Rxgx2Rx200AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 1),
    _Rxgx2Rx200AnalogTableIndex_Type()
)
rxgx2Rx200AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rx200AnalogTableIndex.setStatus("mandatory")


class _RxlabelModTemp_Type(DisplayString):
    """Custom type rxlabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelModTemp_Type.__name__ = "DisplayString"
_RxlabelModTemp_Object = MibTableColumn
rxlabelModTemp = _RxlabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 2),
    _RxlabelModTemp_Type()
)
rxlabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelModTemp.setStatus("optional")


class _RxuomModTemp_Type(DisplayString):
    """Custom type rxuomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxuomModTemp_Type.__name__ = "DisplayString"
_RxuomModTemp_Object = MibTableColumn
rxuomModTemp = _RxuomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 3),
    _RxuomModTemp_Type()
)
rxuomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxuomModTemp.setStatus("optional")
_RxmajorHighModTemp_Type = Float
_RxmajorHighModTemp_Object = MibTableColumn
rxmajorHighModTemp = _RxmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 4),
    _RxmajorHighModTemp_Type()
)
rxmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmajorHighModTemp.setStatus("mandatory")
_RxmajorLowModTemp_Type = Float
_RxmajorLowModTemp_Object = MibTableColumn
rxmajorLowModTemp = _RxmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 5),
    _RxmajorLowModTemp_Type()
)
rxmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmajorLowModTemp.setStatus("mandatory")
_RxminorHighModTemp_Type = Float
_RxminorHighModTemp_Object = MibTableColumn
rxminorHighModTemp = _RxminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 6),
    _RxminorHighModTemp_Type()
)
rxminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminorHighModTemp.setStatus("mandatory")
_RxminorLowModTemp_Type = Float
_RxminorLowModTemp_Object = MibTableColumn
rxminorLowModTemp = _RxminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 7),
    _RxminorLowModTemp_Type()
)
rxminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminorLowModTemp.setStatus("mandatory")
_RxcurrentValueModTemp_Type = Float
_RxcurrentValueModTemp_Object = MibTableColumn
rxcurrentValueModTemp = _RxcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 8),
    _RxcurrentValueModTemp_Type()
)
rxcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxcurrentValueModTemp.setStatus("mandatory")


class _RxstateFlagModTemp_Type(Integer32):
    """Custom type rxstateFlagModTemp based on Integer32"""
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


_RxstateFlagModTemp_Type.__name__ = "Integer32"
_RxstateFlagModTemp_Object = MibTableColumn
rxstateFlagModTemp = _RxstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 9),
    _RxstateFlagModTemp_Type()
)
rxstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlagModTemp.setStatus("mandatory")
_RxminValueModTemp_Type = Float
_RxminValueModTemp_Object = MibTableColumn
rxminValueModTemp = _RxminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 10),
    _RxminValueModTemp_Type()
)
rxminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminValueModTemp.setStatus("mandatory")
_RxmaxValueModTemp_Type = Float
_RxmaxValueModTemp_Object = MibTableColumn
rxmaxValueModTemp = _RxmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 11),
    _RxmaxValueModTemp_Type()
)
rxmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmaxValueModTemp.setStatus("mandatory")


class _RxalarmStateModTemp_Type(Integer32):
    """Custom type rxalarmStateModTemp based on Integer32"""
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


_RxalarmStateModTemp_Type.__name__ = "Integer32"
_RxalarmStateModTemp_Object = MibTableColumn
rxalarmStateModTemp = _RxalarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 12),
    _RxalarmStateModTemp_Type()
)
rxalarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxalarmStateModTemp.setStatus("mandatory")


class _RxlabelFanCurrent_Type(DisplayString):
    """Custom type rxlabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelFanCurrent_Type.__name__ = "DisplayString"
_RxlabelFanCurrent_Object = MibTableColumn
rxlabelFanCurrent = _RxlabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 13),
    _RxlabelFanCurrent_Type()
)
rxlabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelFanCurrent.setStatus("optional")


class _RxuomFanCurrent_Type(DisplayString):
    """Custom type rxuomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxuomFanCurrent_Type.__name__ = "DisplayString"
_RxuomFanCurrent_Object = MibTableColumn
rxuomFanCurrent = _RxuomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 14),
    _RxuomFanCurrent_Type()
)
rxuomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxuomFanCurrent.setStatus("optional")
_RxmajorHighFanCurrent_Type = Float
_RxmajorHighFanCurrent_Object = MibTableColumn
rxmajorHighFanCurrent = _RxmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 15),
    _RxmajorHighFanCurrent_Type()
)
rxmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmajorHighFanCurrent.setStatus("mandatory")
_RxmajorLowFanCurrent_Type = Float
_RxmajorLowFanCurrent_Object = MibTableColumn
rxmajorLowFanCurrent = _RxmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 16),
    _RxmajorLowFanCurrent_Type()
)
rxmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmajorLowFanCurrent.setStatus("mandatory")
_RxminorHighFanCurrent_Type = Float
_RxminorHighFanCurrent_Object = MibTableColumn
rxminorHighFanCurrent = _RxminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 17),
    _RxminorHighFanCurrent_Type()
)
rxminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminorHighFanCurrent.setStatus("mandatory")
_RxminorLowFanCurrent_Type = Float
_RxminorLowFanCurrent_Object = MibTableColumn
rxminorLowFanCurrent = _RxminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 18),
    _RxminorLowFanCurrent_Type()
)
rxminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminorLowFanCurrent.setStatus("mandatory")
_RxcurrentValueFanCurrent_Type = Float
_RxcurrentValueFanCurrent_Object = MibTableColumn
rxcurrentValueFanCurrent = _RxcurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 19),
    _RxcurrentValueFanCurrent_Type()
)
rxcurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxcurrentValueFanCurrent.setStatus("mandatory")


class _RxstateFlagFanCurrent_Type(Integer32):
    """Custom type rxstateFlagFanCurrent based on Integer32"""
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


_RxstateFlagFanCurrent_Type.__name__ = "Integer32"
_RxstateFlagFanCurrent_Object = MibTableColumn
rxstateFlagFanCurrent = _RxstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 20),
    _RxstateFlagFanCurrent_Type()
)
rxstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlagFanCurrent.setStatus("mandatory")
_RxminValueFanCurrent_Type = Float
_RxminValueFanCurrent_Object = MibTableColumn
rxminValueFanCurrent = _RxminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 21),
    _RxminValueFanCurrent_Type()
)
rxminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminValueFanCurrent.setStatus("mandatory")
_RxmaxValueFanCurrent_Type = Float
_RxmaxValueFanCurrent_Object = MibTableColumn
rxmaxValueFanCurrent = _RxmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 22),
    _RxmaxValueFanCurrent_Type()
)
rxmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmaxValueFanCurrent.setStatus("mandatory")


class _RxalarmStateFanCurrent_Type(Integer32):
    """Custom type rxalarmStateFanCurrent based on Integer32"""
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


_RxalarmStateFanCurrent_Type.__name__ = "Integer32"
_RxalarmStateFanCurrent_Object = MibTableColumn
rxalarmStateFanCurrent = _RxalarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 23),
    _RxalarmStateFanCurrent_Type()
)
rxalarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxalarmStateFanCurrent.setStatus("mandatory")


class _Rxlabel12Volt_Type(DisplayString):
    """Custom type rxlabel12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rxlabel12Volt_Type.__name__ = "DisplayString"
_Rxlabel12Volt_Object = MibTableColumn
rxlabel12Volt = _Rxlabel12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 24),
    _Rxlabel12Volt_Type()
)
rxlabel12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabel12Volt.setStatus("optional")


class _Rxuom12Volt_Type(DisplayString):
    """Custom type rxuom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rxuom12Volt_Type.__name__ = "DisplayString"
_Rxuom12Volt_Object = MibTableColumn
rxuom12Volt = _Rxuom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 25),
    _Rxuom12Volt_Type()
)
rxuom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxuom12Volt.setStatus("optional")
_RxmajorHigh12Volt_Type = Float
_RxmajorHigh12Volt_Object = MibTableColumn
rxmajorHigh12Volt = _RxmajorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 26),
    _RxmajorHigh12Volt_Type()
)
rxmajorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmajorHigh12Volt.setStatus("mandatory")
_RxmajorLow12Volt_Type = Float
_RxmajorLow12Volt_Object = MibTableColumn
rxmajorLow12Volt = _RxmajorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 27),
    _RxmajorLow12Volt_Type()
)
rxmajorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmajorLow12Volt.setStatus("mandatory")
_RxminorHigh12Volt_Type = Float
_RxminorHigh12Volt_Object = MibTableColumn
rxminorHigh12Volt = _RxminorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 28),
    _RxminorHigh12Volt_Type()
)
rxminorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminorHigh12Volt.setStatus("mandatory")
_RxminorLow12Volt_Type = Float
_RxminorLow12Volt_Object = MibTableColumn
rxminorLow12Volt = _RxminorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 29),
    _RxminorLow12Volt_Type()
)
rxminorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminorLow12Volt.setStatus("mandatory")
_RxcurrentValue12Volt_Type = Float
_RxcurrentValue12Volt_Object = MibTableColumn
rxcurrentValue12Volt = _RxcurrentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 30),
    _RxcurrentValue12Volt_Type()
)
rxcurrentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxcurrentValue12Volt.setStatus("mandatory")


class _RxstateFlag12Volt_Type(Integer32):
    """Custom type rxstateFlag12Volt based on Integer32"""
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


_RxstateFlag12Volt_Type.__name__ = "Integer32"
_RxstateFlag12Volt_Object = MibTableColumn
rxstateFlag12Volt = _RxstateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 31),
    _RxstateFlag12Volt_Type()
)
rxstateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlag12Volt.setStatus("mandatory")
_RxminValue12Volt_Type = Float
_RxminValue12Volt_Object = MibTableColumn
rxminValue12Volt = _RxminValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 32),
    _RxminValue12Volt_Type()
)
rxminValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminValue12Volt.setStatus("mandatory")
_RxmaxValue12Volt_Type = Float
_RxmaxValue12Volt_Object = MibTableColumn
rxmaxValue12Volt = _RxmaxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 33),
    _RxmaxValue12Volt_Type()
)
rxmaxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmaxValue12Volt.setStatus("mandatory")


class _RxalarmState12Volt_Type(Integer32):
    """Custom type rxalarmState12Volt based on Integer32"""
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


_RxalarmState12Volt_Type.__name__ = "Integer32"
_RxalarmState12Volt_Object = MibTableColumn
rxalarmState12Volt = _RxalarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 34),
    _RxalarmState12Volt_Type()
)
rxalarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxalarmState12Volt.setStatus("mandatory")


class _RxlabelOptPower_Type(DisplayString):
    """Custom type rxlabelOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelOptPower_Type.__name__ = "DisplayString"
_RxlabelOptPower_Object = MibTableColumn
rxlabelOptPower = _RxlabelOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 35),
    _RxlabelOptPower_Type()
)
rxlabelOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelOptPower.setStatus("optional")


class _RxuomOptPower_Type(DisplayString):
    """Custom type rxuomOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxuomOptPower_Type.__name__ = "DisplayString"
_RxuomOptPower_Object = MibTableColumn
rxuomOptPower = _RxuomOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 36),
    _RxuomOptPower_Type()
)
rxuomOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxuomOptPower.setStatus("optional")
_RxmajorHighOptPower_Type = Float
_RxmajorHighOptPower_Object = MibTableColumn
rxmajorHighOptPower = _RxmajorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 37),
    _RxmajorHighOptPower_Type()
)
rxmajorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmajorHighOptPower.setStatus("mandatory")
_RxmajorLowOptPower_Type = Float
_RxmajorLowOptPower_Object = MibTableColumn
rxmajorLowOptPower = _RxmajorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 38),
    _RxmajorLowOptPower_Type()
)
rxmajorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmajorLowOptPower.setStatus("mandatory")
_RxminorHighOptPower_Type = Float
_RxminorHighOptPower_Object = MibTableColumn
rxminorHighOptPower = _RxminorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 39),
    _RxminorHighOptPower_Type()
)
rxminorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminorHighOptPower.setStatus("mandatory")
_RxminorLowOptPower_Type = Float
_RxminorLowOptPower_Object = MibTableColumn
rxminorLowOptPower = _RxminorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 40),
    _RxminorLowOptPower_Type()
)
rxminorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminorLowOptPower.setStatus("mandatory")
_RxcurrentValueOptPower_Type = Float
_RxcurrentValueOptPower_Object = MibTableColumn
rxcurrentValueOptPower = _RxcurrentValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 41),
    _RxcurrentValueOptPower_Type()
)
rxcurrentValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxcurrentValueOptPower.setStatus("mandatory")


class _RxstateFlagOptPower_Type(Integer32):
    """Custom type rxstateFlagOptPower based on Integer32"""
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


_RxstateFlagOptPower_Type.__name__ = "Integer32"
_RxstateFlagOptPower_Object = MibTableColumn
rxstateFlagOptPower = _RxstateFlagOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 42),
    _RxstateFlagOptPower_Type()
)
rxstateFlagOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlagOptPower.setStatus("mandatory")
_RxminValueOptPower_Type = Float
_RxminValueOptPower_Object = MibTableColumn
rxminValueOptPower = _RxminValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 43),
    _RxminValueOptPower_Type()
)
rxminValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxminValueOptPower.setStatus("mandatory")
_RxmaxValueOptPower_Type = Float
_RxmaxValueOptPower_Object = MibTableColumn
rxmaxValueOptPower = _RxmaxValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 44),
    _RxmaxValueOptPower_Type()
)
rxmaxValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxmaxValueOptPower.setStatus("mandatory")


class _RxalarmStateOptPower_Type(Integer32):
    """Custom type rxalarmStateOptPower based on Integer32"""
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


_RxalarmStateOptPower_Type.__name__ = "Integer32"
_RxalarmStateOptPower_Object = MibTableColumn
rxalarmStateOptPower = _RxalarmStateOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 2, 1, 45),
    _RxalarmStateOptPower_Type()
)
rxalarmStateOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxalarmStateOptPower.setStatus("mandatory")
_Gx2Rx200DigitalTable_Object = MibTable
gx2Rx200DigitalTable = _Gx2Rx200DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    gx2Rx200DigitalTable.setStatus("mandatory")
_Gx2Rx200DigitalEntry_Object = MibTableRow
gx2Rx200DigitalEntry = _Gx2Rx200DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2)
)
gx2Rx200DigitalEntry.setIndexNames(
    (0, "OMNI-gx2RX200-MIB", "rxgx2Rx200DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx200DigitalEntry.setStatus("mandatory")


class _Rxgx2Rx200DigitalTableIndex_Type(Integer32):
    """Custom type rxgx2Rx200DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rx200DigitalTableIndex_Type.__name__ = "Integer32"
_Rxgx2Rx200DigitalTableIndex_Object = MibTableColumn
rxgx2Rx200DigitalTableIndex = _Rxgx2Rx200DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 1),
    _Rxgx2Rx200DigitalTableIndex_Type()
)
rxgx2Rx200DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rx200DigitalTableIndex.setStatus("mandatory")


class _RxlabelMode_Type(DisplayString):
    """Custom type rxlabelMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelMode_Type.__name__ = "DisplayString"
_RxlabelMode_Object = MibTableColumn
rxlabelMode = _RxlabelMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 2),
    _RxlabelMode_Type()
)
rxlabelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelMode.setStatus("optional")


class _RxenumMode_Type(DisplayString):
    """Custom type rxenumMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxenumMode_Type.__name__ = "DisplayString"
_RxenumMode_Object = MibTableColumn
rxenumMode = _RxenumMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 3),
    _RxenumMode_Type()
)
rxenumMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxenumMode.setStatus("optional")


class _RxvalueMode_Type(Integer32):
    """Custom type rxvalueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("burst", 3),
          ("normal", 2),
          ("off", 1))
    )


_RxvalueMode_Type.__name__ = "Integer32"
_RxvalueMode_Object = MibTableColumn
rxvalueMode = _RxvalueMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 4),
    _RxvalueMode_Type()
)
rxvalueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxvalueMode.setStatus("mandatory")


class _RxstateFlagMode_Type(Integer32):
    """Custom type rxstateFlagMode based on Integer32"""
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


_RxstateFlagMode_Type.__name__ = "Integer32"
_RxstateFlagMode_Object = MibTableColumn
rxstateFlagMode = _RxstateFlagMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 5),
    _RxstateFlagMode_Type()
)
rxstateFlagMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlagMode.setStatus("mandatory")


class _RxlabelWavelength_Type(DisplayString):
    """Custom type rxlabelWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelWavelength_Type.__name__ = "DisplayString"
_RxlabelWavelength_Object = MibTableColumn
rxlabelWavelength = _RxlabelWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 6),
    _RxlabelWavelength_Type()
)
rxlabelWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelWavelength.setStatus("optional")


class _RxenumWavelength_Type(DisplayString):
    """Custom type rxenumWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxenumWavelength_Type.__name__ = "DisplayString"
_RxenumWavelength_Object = MibTableColumn
rxenumWavelength = _RxenumWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 7),
    _RxenumWavelength_Type()
)
rxenumWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxenumWavelength.setStatus("optional")


class _RxvalueWavelength_Type(Integer32):
    """Custom type rxvalueWavelength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nM1310", 1),
          ("nM1550", 2))
    )


_RxvalueWavelength_Type.__name__ = "Integer32"
_RxvalueWavelength_Object = MibTableColumn
rxvalueWavelength = _RxvalueWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 8),
    _RxvalueWavelength_Type()
)
rxvalueWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxvalueWavelength.setStatus("mandatory")


class _RxstateFlagWavelength_Type(Integer32):
    """Custom type rxstateFlagWavelength based on Integer32"""
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


_RxstateFlagWavelength_Type.__name__ = "Integer32"
_RxstateFlagWavelength_Object = MibTableColumn
rxstateFlagWavelength = _RxstateFlagWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 9),
    _RxstateFlagWavelength_Type()
)
rxstateFlagWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlagWavelength.setStatus("mandatory")


class _RxlabelAttnSetting_Type(DisplayString):
    """Custom type rxlabelAttnSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelAttnSetting_Type.__name__ = "DisplayString"
_RxlabelAttnSetting_Object = MibTableColumn
rxlabelAttnSetting = _RxlabelAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 10),
    _RxlabelAttnSetting_Type()
)
rxlabelAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelAttnSetting.setStatus("optional")


class _RxenumAttnSetting_Type(DisplayString):
    """Custom type rxenumAttnSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxenumAttnSetting_Type.__name__ = "DisplayString"
_RxenumAttnSetting_Object = MibTableColumn
rxenumAttnSetting = _RxenumAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 11),
    _RxenumAttnSetting_Type()
)
rxenumAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxenumAttnSetting.setStatus("optional")
_RxvalueAttnSetting_Type = Integer32
_RxvalueAttnSetting_Object = MibTableColumn
rxvalueAttnSetting = _RxvalueAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 12),
    _RxvalueAttnSetting_Type()
)
rxvalueAttnSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxvalueAttnSetting.setStatus("mandatory")


class _RxstateFlagAttnSetting_Type(Integer32):
    """Custom type rxstateFlagAttnSetting based on Integer32"""
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


_RxstateFlagAttnSetting_Type.__name__ = "Integer32"
_RxstateFlagAttnSetting_Object = MibTableColumn
rxstateFlagAttnSetting = _RxstateFlagAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 13),
    _RxstateFlagAttnSetting_Type()
)
rxstateFlagAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlagAttnSetting.setStatus("mandatory")


class _RxlabelSwModeSetting_Type(DisplayString):
    """Custom type rxlabelSwModeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelSwModeSetting_Type.__name__ = "DisplayString"
_RxlabelSwModeSetting_Object = MibTableColumn
rxlabelSwModeSetting = _RxlabelSwModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 14),
    _RxlabelSwModeSetting_Type()
)
rxlabelSwModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelSwModeSetting.setStatus("optional")


class _RxenumSwModeSetting_Type(DisplayString):
    """Custom type rxenumSwModeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxenumSwModeSetting_Type.__name__ = "DisplayString"
_RxenumSwModeSetting_Object = MibTableColumn
rxenumSwModeSetting = _RxenumSwModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 15),
    _RxenumSwModeSetting_Type()
)
rxenumSwModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxenumSwModeSetting.setStatus("optional")


class _RxvalueSwModeSetting_Type(Integer32):
    """Custom type rxvalueSwModeSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-and-switch", 3),
          ("alarm-only", 2),
          ("off", 1))
    )


_RxvalueSwModeSetting_Type.__name__ = "Integer32"
_RxvalueSwModeSetting_Object = MibTableColumn
rxvalueSwModeSetting = _RxvalueSwModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 16),
    _RxvalueSwModeSetting_Type()
)
rxvalueSwModeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxvalueSwModeSetting.setStatus("mandatory")


class _RxstateFlagSwModeSetting_Type(Integer32):
    """Custom type rxstateFlagSwModeSetting based on Integer32"""
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


_RxstateFlagSwModeSetting_Type.__name__ = "Integer32"
_RxstateFlagSwModeSetting_Object = MibTableColumn
rxstateFlagSwModeSetting = _RxstateFlagSwModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 17),
    _RxstateFlagSwModeSetting_Type()
)
rxstateFlagSwModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlagSwModeSetting.setStatus("mandatory")


class _RxlabelSwModeThreshold_Type(DisplayString):
    """Custom type rxlabelSwModeThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelSwModeThreshold_Type.__name__ = "DisplayString"
_RxlabelSwModeThreshold_Object = MibTableColumn
rxlabelSwModeThreshold = _RxlabelSwModeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 18),
    _RxlabelSwModeThreshold_Type()
)
rxlabelSwModeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelSwModeThreshold.setStatus("optional")


class _RxenumSwModeThreshold_Type(DisplayString):
    """Custom type rxenumSwModeThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxenumSwModeThreshold_Type.__name__ = "DisplayString"
_RxenumSwModeThreshold_Object = MibTableColumn
rxenumSwModeThreshold = _RxenumSwModeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 19),
    _RxenumSwModeThreshold_Type()
)
rxenumSwModeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxenumSwModeThreshold.setStatus("optional")
_RxvalueSwModeThreshold_Type = Integer32
_RxvalueSwModeThreshold_Object = MibTableColumn
rxvalueSwModeThreshold = _RxvalueSwModeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 20),
    _RxvalueSwModeThreshold_Type()
)
rxvalueSwModeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxvalueSwModeThreshold.setStatus("mandatory")


class _RxstateFlagSwModeThreshold_Type(Integer32):
    """Custom type rxstateFlagSwModeThreshold based on Integer32"""
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


_RxstateFlagSwModeThreshold_Type.__name__ = "Integer32"
_RxstateFlagSwModeThreshold_Object = MibTableColumn
rxstateFlagSwModeThreshold = _RxstateFlagSwModeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 21),
    _RxstateFlagSwModeThreshold_Type()
)
rxstateFlagSwModeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlagSwModeThreshold.setStatus("mandatory")


class _RxlabelFactoryDefault_Type(DisplayString):
    """Custom type rxlabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelFactoryDefault_Type.__name__ = "DisplayString"
_RxlabelFactoryDefault_Object = MibTableColumn
rxlabelFactoryDefault = _RxlabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 22),
    _RxlabelFactoryDefault_Type()
)
rxlabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelFactoryDefault.setStatus("optional")


class _RxenumFactoryDefault_Type(DisplayString):
    """Custom type rxenumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxenumFactoryDefault_Type.__name__ = "DisplayString"
_RxenumFactoryDefault_Object = MibTableColumn
rxenumFactoryDefault = _RxenumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 23),
    _RxenumFactoryDefault_Type()
)
rxenumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxenumFactoryDefault.setStatus("optional")


class _RxvalueFactoryDefault_Type(Integer32):
    """Custom type rxvalueFactoryDefault based on Integer32"""
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


_RxvalueFactoryDefault_Type.__name__ = "Integer32"
_RxvalueFactoryDefault_Object = MibTableColumn
rxvalueFactoryDefault = _RxvalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 24),
    _RxvalueFactoryDefault_Type()
)
rxvalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxvalueFactoryDefault.setStatus("mandatory")


class _RxstateFlagFactoryDefault_Type(Integer32):
    """Custom type rxstateFlagFactoryDefault based on Integer32"""
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


_RxstateFlagFactoryDefault_Type.__name__ = "Integer32"
_RxstateFlagFactoryDefault_Object = MibTableColumn
rxstateFlagFactoryDefault = _RxstateFlagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 3, 2, 25),
    _RxstateFlagFactoryDefault_Type()
)
rxstateFlagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateFlagFactoryDefault.setStatus("mandatory")
_Gx2Rx200StatusTable_Object = MibTable
gx2Rx200StatusTable = _Gx2Rx200StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    gx2Rx200StatusTable.setStatus("mandatory")
_Gx2Rx200StatusEntry_Object = MibTableRow
gx2Rx200StatusEntry = _Gx2Rx200StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3)
)
gx2Rx200StatusEntry.setIndexNames(
    (0, "OMNI-gx2RX200-MIB", "rxgx2Rx200StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx200StatusEntry.setStatus("mandatory")


class _Rxgx2Rx200StatusTableIndex_Type(Integer32):
    """Custom type rxgx2Rx200StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rx200StatusTableIndex_Type.__name__ = "Integer32"
_Rxgx2Rx200StatusTableIndex_Object = MibTableColumn
rxgx2Rx200StatusTableIndex = _Rxgx2Rx200StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 1),
    _Rxgx2Rx200StatusTableIndex_Type()
)
rxgx2Rx200StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rx200StatusTableIndex.setStatus("mandatory")


class _RxlabelBoot_Type(DisplayString):
    """Custom type rxlabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelBoot_Type.__name__ = "DisplayString"
_RxlabelBoot_Object = MibTableColumn
rxlabelBoot = _RxlabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 2),
    _RxlabelBoot_Type()
)
rxlabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelBoot.setStatus("optional")


class _RxvalueBoot_Type(Integer32):
    """Custom type rxvalueBoot based on Integer32"""
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


_RxvalueBoot_Type.__name__ = "Integer32"
_RxvalueBoot_Object = MibTableColumn
rxvalueBoot = _RxvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 3),
    _RxvalueBoot_Type()
)
rxvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxvalueBoot.setStatus("mandatory")


class _RxstateflagBoot_Type(Integer32):
    """Custom type rxstateflagBoot based on Integer32"""
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


_RxstateflagBoot_Type.__name__ = "Integer32"
_RxstateflagBoot_Object = MibTableColumn
rxstateflagBoot = _RxstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 4),
    _RxstateflagBoot_Type()
)
rxstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateflagBoot.setStatus("mandatory")


class _RxlabelFlash_Type(DisplayString):
    """Custom type rxlabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelFlash_Type.__name__ = "DisplayString"
_RxlabelFlash_Object = MibTableColumn
rxlabelFlash = _RxlabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 5),
    _RxlabelFlash_Type()
)
rxlabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelFlash.setStatus("optional")


class _RxvalueFlash_Type(Integer32):
    """Custom type rxvalueFlash based on Integer32"""
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


_RxvalueFlash_Type.__name__ = "Integer32"
_RxvalueFlash_Object = MibTableColumn
rxvalueFlash = _RxvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 6),
    _RxvalueFlash_Type()
)
rxvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxvalueFlash.setStatus("mandatory")


class _RxstateflagFlash_Type(Integer32):
    """Custom type rxstateflagFlash based on Integer32"""
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


_RxstateflagFlash_Type.__name__ = "Integer32"
_RxstateflagFlash_Object = MibTableColumn
rxstateflagFlash = _RxstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 7),
    _RxstateflagFlash_Type()
)
rxstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateflagFlash.setStatus("mandatory")


class _RxlabelFactoryDataCRC_Type(DisplayString):
    """Custom type rxlabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelFactoryDataCRC_Type.__name__ = "DisplayString"
_RxlabelFactoryDataCRC_Object = MibTableColumn
rxlabelFactoryDataCRC = _RxlabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 8),
    _RxlabelFactoryDataCRC_Type()
)
rxlabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelFactoryDataCRC.setStatus("optional")


class _RxvalueFactoryDataCRC_Type(Integer32):
    """Custom type rxvalueFactoryDataCRC based on Integer32"""
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


_RxvalueFactoryDataCRC_Type.__name__ = "Integer32"
_RxvalueFactoryDataCRC_Object = MibTableColumn
rxvalueFactoryDataCRC = _RxvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 9),
    _RxvalueFactoryDataCRC_Type()
)
rxvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxvalueFactoryDataCRC.setStatus("mandatory")


class _RxstateflagFactoryDataCRC_Type(Integer32):
    """Custom type rxstateflagFactoryDataCRC based on Integer32"""
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


_RxstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_RxstateflagFactoryDataCRC_Object = MibTableColumn
rxstateflagFactoryDataCRC = _RxstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 10),
    _RxstateflagFactoryDataCRC_Type()
)
rxstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateflagFactoryDataCRC.setStatus("mandatory")


class _RxlabelAlarmDataCRC_Type(DisplayString):
    """Custom type rxlabelAlarmDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelAlarmDataCRC_Type.__name__ = "DisplayString"
_RxlabelAlarmDataCRC_Object = MibTableColumn
rxlabelAlarmDataCRC = _RxlabelAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 11),
    _RxlabelAlarmDataCRC_Type()
)
rxlabelAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelAlarmDataCRC.setStatus("optional")


class _RxvalueAlarmDataCRC_Type(Integer32):
    """Custom type rxvalueAlarmDataCRC based on Integer32"""
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


_RxvalueAlarmDataCRC_Type.__name__ = "Integer32"
_RxvalueAlarmDataCRC_Object = MibTableColumn
rxvalueAlarmDataCRC = _RxvalueAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 12),
    _RxvalueAlarmDataCRC_Type()
)
rxvalueAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxvalueAlarmDataCRC.setStatus("mandatory")


class _RxstateflagAlarmDataCRC_Type(Integer32):
    """Custom type rxstateflagAlarmDataCRC based on Integer32"""
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


_RxstateflagAlarmDataCRC_Type.__name__ = "Integer32"
_RxstateflagAlarmDataCRC_Object = MibTableColumn
rxstateflagAlarmDataCRC = _RxstateflagAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 13),
    _RxstateflagAlarmDataCRC_Type()
)
rxstateflagAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateflagAlarmDataCRC.setStatus("mandatory")


class _RxlabelCalibrationDataCRC_Type(DisplayString):
    """Custom type rxlabelCalibrationDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelCalibrationDataCRC_Type.__name__ = "DisplayString"
_RxlabelCalibrationDataCRC_Object = MibTableColumn
rxlabelCalibrationDataCRC = _RxlabelCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 14),
    _RxlabelCalibrationDataCRC_Type()
)
rxlabelCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelCalibrationDataCRC.setStatus("optional")


class _RxvalueCalibrationDataCRC_Type(Integer32):
    """Custom type rxvalueCalibrationDataCRC based on Integer32"""
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


_RxvalueCalibrationDataCRC_Type.__name__ = "Integer32"
_RxvalueCalibrationDataCRC_Object = MibTableColumn
rxvalueCalibrationDataCRC = _RxvalueCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 15),
    _RxvalueCalibrationDataCRC_Type()
)
rxvalueCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxvalueCalibrationDataCRC.setStatus("mandatory")


class _RxstateflagCalibrationDataCRC_Type(Integer32):
    """Custom type rxstateflagCalibrationDataCRC based on Integer32"""
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


_RxstateflagCalibrationDataCRC_Type.__name__ = "Integer32"
_RxstateflagCalibrationDataCRC_Object = MibTableColumn
rxstateflagCalibrationDataCRC = _RxstateflagCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 16),
    _RxstateflagCalibrationDataCRC_Type()
)
rxstateflagCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateflagCalibrationDataCRC.setStatus("mandatory")


class _RxlabelThermalCompCRC_Type(DisplayString):
    """Custom type rxlabelThermalCompCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelThermalCompCRC_Type.__name__ = "DisplayString"
_RxlabelThermalCompCRC_Object = MibTableColumn
rxlabelThermalCompCRC = _RxlabelThermalCompCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 17),
    _RxlabelThermalCompCRC_Type()
)
rxlabelThermalCompCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelThermalCompCRC.setStatus("optional")


class _RxvalueThermalCompCRC_Type(Integer32):
    """Custom type rxvalueThermalCompCRC based on Integer32"""
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


_RxvalueThermalCompCRC_Type.__name__ = "Integer32"
_RxvalueThermalCompCRC_Object = MibTableColumn
rxvalueThermalCompCRC = _RxvalueThermalCompCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 18),
    _RxvalueThermalCompCRC_Type()
)
rxvalueThermalCompCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxvalueThermalCompCRC.setStatus("mandatory")


class _RxstateflagThermalCompCRC_Type(Integer32):
    """Custom type rxstateflagThermalCompCRC based on Integer32"""
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


_RxstateflagThermalCompCRC_Type.__name__ = "Integer32"
_RxstateflagThermalCompCRC_Object = MibTableColumn
rxstateflagThermalCompCRC = _RxstateflagThermalCompCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 19),
    _RxstateflagThermalCompCRC_Type()
)
rxstateflagThermalCompCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateflagThermalCompCRC.setStatus("mandatory")


class _RxlabelHW_Type(DisplayString):
    """Custom type rxlabelHW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelHW_Type.__name__ = "DisplayString"
_RxlabelHW_Object = MibTableColumn
rxlabelHW = _RxlabelHW_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 20),
    _RxlabelHW_Type()
)
rxlabelHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelHW.setStatus("optional")


class _RxvalueHW_Type(Integer32):
    """Custom type rxvalueHW based on Integer32"""
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


_RxvalueHW_Type.__name__ = "Integer32"
_RxvalueHW_Object = MibTableColumn
rxvalueHW = _RxvalueHW_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 21),
    _RxvalueHW_Type()
)
rxvalueHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxvalueHW.setStatus("mandatory")


class _RxstateflagHW_Type(Integer32):
    """Custom type rxstateflagHW based on Integer32"""
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


_RxstateflagHW_Type.__name__ = "Integer32"
_RxstateflagHW_Object = MibTableColumn
rxstateflagHW = _RxstateflagHW_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 22),
    _RxstateflagHW_Type()
)
rxstateflagHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateflagHW.setStatus("mandatory")


class _RxlabelOptSig_Type(DisplayString):
    """Custom type rxlabelOptSig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxlabelOptSig_Type.__name__ = "DisplayString"
_RxlabelOptSig_Object = MibTableColumn
rxlabelOptSig = _RxlabelOptSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 23),
    _RxlabelOptSig_Type()
)
rxlabelOptSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxlabelOptSig.setStatus("optional")


class _RxvalueOptSig_Type(Integer32):
    """Custom type rxvalueOptSig based on Integer32"""
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


_RxvalueOptSig_Type.__name__ = "Integer32"
_RxvalueOptSig_Object = MibTableColumn
rxvalueOptSig = _RxvalueOptSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 24),
    _RxvalueOptSig_Type()
)
rxvalueOptSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxvalueOptSig.setStatus("mandatory")


class _RxstateflagOptSig_Type(Integer32):
    """Custom type rxstateflagOptSig based on Integer32"""
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


_RxstateflagOptSig_Type.__name__ = "Integer32"
_RxstateflagOptSig_Object = MibTableColumn
rxstateflagOptSig = _RxstateflagOptSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 4, 3, 25),
    _RxstateflagOptSig_Type()
)
rxstateflagOptSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstateflagOptSig.setStatus("mandatory")
_Gx2Rx200FactoryTable_Object = MibTable
gx2Rx200FactoryTable = _Gx2Rx200FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    gx2Rx200FactoryTable.setStatus("mandatory")
_Gx2Rx200FactoryEntry_Object = MibTableRow
gx2Rx200FactoryEntry = _Gx2Rx200FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4)
)
gx2Rx200FactoryEntry.setIndexNames(
    (0, "OMNI-gx2RX200-MIB", "rxgx2Rx200FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx200FactoryEntry.setStatus("mandatory")


class _Rxgx2Rx200FactoryTableIndex_Type(Integer32):
    """Custom type rxgx2Rx200FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rx200FactoryTableIndex_Type.__name__ = "Integer32"
_Rxgx2Rx200FactoryTableIndex_Object = MibTableColumn
rxgx2Rx200FactoryTableIndex = _Rxgx2Rx200FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 1),
    _Rxgx2Rx200FactoryTableIndex_Type()
)
rxgx2Rx200FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rx200FactoryTableIndex.setStatus("mandatory")
_RxbootControlByte_Type = Integer32
_RxbootControlByte_Object = MibTableColumn
rxbootControlByte = _RxbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 2),
    _RxbootControlByte_Type()
)
rxbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxbootControlByte.setStatus("mandatory")
_RxbootStatusByte_Type = Integer32
_RxbootStatusByte_Object = MibTableColumn
rxbootStatusByte = _RxbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 3),
    _RxbootStatusByte_Type()
)
rxbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxbootStatusByte.setStatus("mandatory")
_Rxbank0CRC_Type = Integer32
_Rxbank0CRC_Object = MibTableColumn
rxbank0CRC = _Rxbank0CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 4),
    _Rxbank0CRC_Type()
)
rxbank0CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxbank0CRC.setStatus("mandatory")
_Rxbank1CRC_Type = Integer32
_Rxbank1CRC_Object = MibTableColumn
rxbank1CRC = _Rxbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 5),
    _Rxbank1CRC_Type()
)
rxbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxbank1CRC.setStatus("mandatory")
_RxprgEEPROMByte_Type = Integer32
_RxprgEEPROMByte_Object = MibTableColumn
rxprgEEPROMByte = _RxprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 6),
    _RxprgEEPROMByte_Type()
)
rxprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxprgEEPROMByte.setStatus("mandatory")
_RxfactoryCRC_Type = Integer32
_RxfactoryCRC_Object = MibTableColumn
rxfactoryCRC = _RxfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 7),
    _RxfactoryCRC_Type()
)
rxfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxfactoryCRC.setStatus("mandatory")


class _RxcalculateCRC_Type(Integer32):
    """Custom type rxcalculateCRC based on Integer32"""
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
        *(("alarm", 3),
          ("calibration", 2),
          ("factory", 1),
          ("tempComp", 4))
    )


_RxcalculateCRC_Type.__name__ = "Integer32"
_RxcalculateCRC_Object = MibTableColumn
rxcalculateCRC = _RxcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 8),
    _RxcalculateCRC_Type()
)
rxcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxcalculateCRC.setStatus("mandatory")
_RxhourMeter_Type = Integer32
_RxhourMeter_Object = MibTableColumn
rxhourMeter = _RxhourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 9),
    _RxhourMeter_Type()
)
rxhourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxhourMeter.setStatus("mandatory")
_RxflashPrgCntA_Type = Integer32
_RxflashPrgCntA_Object = MibTableColumn
rxflashPrgCntA = _RxflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 10),
    _RxflashPrgCntA_Type()
)
rxflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxflashPrgCntA.setStatus("mandatory")
_RxflashPrgCntB_Type = Integer32
_RxflashPrgCntB_Object = MibTableColumn
rxflashPrgCntB = _RxflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 11),
    _RxflashPrgCntB_Type()
)
rxflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxflashPrgCntB.setStatus("mandatory")


class _RxfwRev0_Type(DisplayString):
    """Custom type rxfwRev0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxfwRev0_Type.__name__ = "DisplayString"
_RxfwRev0_Object = MibTableColumn
rxfwRev0 = _RxfwRev0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 12),
    _RxfwRev0_Type()
)
rxfwRev0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxfwRev0.setStatus("mandatory")


class _RxfwRev1_Type(DisplayString):
    """Custom type rxfwRev1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RxfwRev1_Type.__name__ = "DisplayString"
_RxfwRev1_Object = MibTableColumn
rxfwRev1 = _RxfwRev1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 5, 4, 13),
    _RxfwRev1_Type()
)
rxfwRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxfwRev1.setStatus("mandatory")
_Gx2Rx200HoldTimeTable_Object = MibTable
gx2Rx200HoldTimeTable = _Gx2Rx200HoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    gx2Rx200HoldTimeTable.setStatus("mandatory")
_Gx2Rx200HoldTimeEntry_Object = MibTableRow
gx2Rx200HoldTimeEntry = _Gx2Rx200HoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 6, 5)
)
gx2Rx200HoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2RX200-MIB", "rxgx2Rx200HoldTimeTableIndex"),
    (0, "OMNI-gx2RX200-MIB", "rxgx2Rx200HoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx200HoldTimeEntry.setStatus("mandatory")


class _Rxgx2Rx200HoldTimeTableIndex_Type(Integer32):
    """Custom type rxgx2Rx200HoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rx200HoldTimeTableIndex_Type.__name__ = "Integer32"
_Rxgx2Rx200HoldTimeTableIndex_Object = MibTableColumn
rxgx2Rx200HoldTimeTableIndex = _Rxgx2Rx200HoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 6, 5, 1),
    _Rxgx2Rx200HoldTimeTableIndex_Type()
)
rxgx2Rx200HoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rx200HoldTimeTableIndex.setStatus("mandatory")


class _Rxgx2Rx200HoldTimeSpecIndex_Type(Integer32):
    """Custom type rxgx2Rx200HoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rx200HoldTimeSpecIndex_Type.__name__ = "Integer32"
_Rxgx2Rx200HoldTimeSpecIndex_Object = MibTableColumn
rxgx2Rx200HoldTimeSpecIndex = _Rxgx2Rx200HoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 6, 5, 2),
    _Rxgx2Rx200HoldTimeSpecIndex_Type()
)
rxgx2Rx200HoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rx200HoldTimeSpecIndex.setStatus("mandatory")
_Rxgx2Rx200HoldTimeData_Type = Integer32
_Rxgx2Rx200HoldTimeData_Object = MibTableColumn
rxgx2Rx200HoldTimeData = _Rxgx2Rx200HoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 6, 5, 3),
    _Rxgx2Rx200HoldTimeData_Type()
)
rxgx2Rx200HoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxgx2Rx200HoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapRX200ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 1)
)
trapRX200ConfigChangeInteger.setObjects(
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
    trapRX200ConfigChangeInteger.setStatus(
        ""
    )

trapRX200ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 2)
)
trapRX200ConfigChangeDisplayString.setObjects(
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
    trapRX200ConfigChangeDisplayString.setStatus(
        ""
    )

trapRX200OpticalPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 3)
)
trapRX200OpticalPowerAlarm.setObjects(
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
    trapRX200OpticalPowerAlarm.setStatus(
        ""
    )

trapRX200ModuleTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 4)
)
trapRX200ModuleTemperatureAlarm.setObjects(
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
    trapRX200ModuleTemperatureAlarm.setStatus(
        ""
    )

trapRX200FanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 5)
)
trapRX200FanCurrentAlarm.setObjects(
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
    trapRX200FanCurrentAlarm.setStatus(
        ""
    )

trapRX200Plus12CurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 6)
)
trapRX200Plus12CurrentAlarm.setObjects(
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
    trapRX200Plus12CurrentAlarm.setStatus(
        ""
    )

trapRX200Boot0Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 7)
)
trapRX200Boot0Alarm.setObjects(
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
    trapRX200Boot0Alarm.setStatus(
        ""
    )

trapRX200Boot1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 8)
)
trapRX200Boot1Alarm.setObjects(
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
    trapRX200Boot1Alarm.setStatus(
        ""
    )

trapRX200FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 9)
)
trapRX200FlashAlarm.setObjects(
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
    trapRX200FlashAlarm.setStatus(
        ""
    )

trapRX200AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 10)
)
trapRX200AlarmDataCRCAlarm.setObjects(
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
    trapRX200AlarmDataCRCAlarm.setStatus(
        ""
    )

trapRX200FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 11)
)
trapRX200FactoryDataCRCAlarm.setObjects(
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
    trapRX200FactoryDataCRCAlarm.setStatus(
        ""
    )

trapRX200CalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 12)
)
trapRX200CalDataCRCAlarm.setObjects(
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
    trapRX200CalDataCRCAlarm.setStatus(
        ""
    )

trapRX200DefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 13)
)
trapRX200DefaultAlarm.setObjects(
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
    trapRX200DefaultAlarm.setStatus(
        ""
    )

trapRX200ModeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 14)
)
trapRX200ModeAlarm.setObjects(
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
    trapRX200ModeAlarm.setStatus(
        ""
    )

trapRX200OutputSwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 15)
)
trapRX200OutputSwitchedAlarm.setObjects(
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
    trapRX200OutputSwitchedAlarm.setStatus(
        ""
    )

trapRX200SideStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6, 0, 16)
)
trapRX200SideStatusAlarm.setObjects(
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
    trapRX200SideStatusAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2RX200-MIB",
    **{"Float": Float,
       "U32Data": U32Data,
       "trapRX200ConfigChangeInteger": trapRX200ConfigChangeInteger,
       "trapRX200ConfigChangeDisplayString": trapRX200ConfigChangeDisplayString,
       "trapRX200OpticalPowerAlarm": trapRX200OpticalPowerAlarm,
       "trapRX200ModuleTemperatureAlarm": trapRX200ModuleTemperatureAlarm,
       "trapRX200FanCurrentAlarm": trapRX200FanCurrentAlarm,
       "trapRX200Plus12CurrentAlarm": trapRX200Plus12CurrentAlarm,
       "trapRX200Boot0Alarm": trapRX200Boot0Alarm,
       "trapRX200Boot1Alarm": trapRX200Boot1Alarm,
       "trapRX200FlashAlarm": trapRX200FlashAlarm,
       "trapRX200AlarmDataCRCAlarm": trapRX200AlarmDataCRCAlarm,
       "trapRX200FactoryDataCRCAlarm": trapRX200FactoryDataCRCAlarm,
       "trapRX200CalDataCRCAlarm": trapRX200CalDataCRCAlarm,
       "trapRX200DefaultAlarm": trapRX200DefaultAlarm,
       "trapRX200ModeAlarm": trapRX200ModeAlarm,
       "trapRX200OutputSwitchedAlarm": trapRX200OutputSwitchedAlarm,
       "trapRX200SideStatusAlarm": trapRX200SideStatusAlarm,
       "gx2Rx200Descriptor": gx2Rx200Descriptor,
       "gx2Rx200AnalogTable": gx2Rx200AnalogTable,
       "gx2Rx200AnalogEntry": gx2Rx200AnalogEntry,
       "rxgx2Rx200AnalogTableIndex": rxgx2Rx200AnalogTableIndex,
       "rxlabelModTemp": rxlabelModTemp,
       "rxuomModTemp": rxuomModTemp,
       "rxmajorHighModTemp": rxmajorHighModTemp,
       "rxmajorLowModTemp": rxmajorLowModTemp,
       "rxminorHighModTemp": rxminorHighModTemp,
       "rxminorLowModTemp": rxminorLowModTemp,
       "rxcurrentValueModTemp": rxcurrentValueModTemp,
       "rxstateFlagModTemp": rxstateFlagModTemp,
       "rxminValueModTemp": rxminValueModTemp,
       "rxmaxValueModTemp": rxmaxValueModTemp,
       "rxalarmStateModTemp": rxalarmStateModTemp,
       "rxlabelFanCurrent": rxlabelFanCurrent,
       "rxuomFanCurrent": rxuomFanCurrent,
       "rxmajorHighFanCurrent": rxmajorHighFanCurrent,
       "rxmajorLowFanCurrent": rxmajorLowFanCurrent,
       "rxminorHighFanCurrent": rxminorHighFanCurrent,
       "rxminorLowFanCurrent": rxminorLowFanCurrent,
       "rxcurrentValueFanCurrent": rxcurrentValueFanCurrent,
       "rxstateFlagFanCurrent": rxstateFlagFanCurrent,
       "rxminValueFanCurrent": rxminValueFanCurrent,
       "rxmaxValueFanCurrent": rxmaxValueFanCurrent,
       "rxalarmStateFanCurrent": rxalarmStateFanCurrent,
       "rxlabel12Volt": rxlabel12Volt,
       "rxuom12Volt": rxuom12Volt,
       "rxmajorHigh12Volt": rxmajorHigh12Volt,
       "rxmajorLow12Volt": rxmajorLow12Volt,
       "rxminorHigh12Volt": rxminorHigh12Volt,
       "rxminorLow12Volt": rxminorLow12Volt,
       "rxcurrentValue12Volt": rxcurrentValue12Volt,
       "rxstateFlag12Volt": rxstateFlag12Volt,
       "rxminValue12Volt": rxminValue12Volt,
       "rxmaxValue12Volt": rxmaxValue12Volt,
       "rxalarmState12Volt": rxalarmState12Volt,
       "rxlabelOptPower": rxlabelOptPower,
       "rxuomOptPower": rxuomOptPower,
       "rxmajorHighOptPower": rxmajorHighOptPower,
       "rxmajorLowOptPower": rxmajorLowOptPower,
       "rxminorHighOptPower": rxminorHighOptPower,
       "rxminorLowOptPower": rxminorLowOptPower,
       "rxcurrentValueOptPower": rxcurrentValueOptPower,
       "rxstateFlagOptPower": rxstateFlagOptPower,
       "rxminValueOptPower": rxminValueOptPower,
       "rxmaxValueOptPower": rxmaxValueOptPower,
       "rxalarmStateOptPower": rxalarmStateOptPower,
       "gx2Rx200DigitalTable": gx2Rx200DigitalTable,
       "gx2Rx200DigitalEntry": gx2Rx200DigitalEntry,
       "rxgx2Rx200DigitalTableIndex": rxgx2Rx200DigitalTableIndex,
       "rxlabelMode": rxlabelMode,
       "rxenumMode": rxenumMode,
       "rxvalueMode": rxvalueMode,
       "rxstateFlagMode": rxstateFlagMode,
       "rxlabelWavelength": rxlabelWavelength,
       "rxenumWavelength": rxenumWavelength,
       "rxvalueWavelength": rxvalueWavelength,
       "rxstateFlagWavelength": rxstateFlagWavelength,
       "rxlabelAttnSetting": rxlabelAttnSetting,
       "rxenumAttnSetting": rxenumAttnSetting,
       "rxvalueAttnSetting": rxvalueAttnSetting,
       "rxstateFlagAttnSetting": rxstateFlagAttnSetting,
       "rxlabelSwModeSetting": rxlabelSwModeSetting,
       "rxenumSwModeSetting": rxenumSwModeSetting,
       "rxvalueSwModeSetting": rxvalueSwModeSetting,
       "rxstateFlagSwModeSetting": rxstateFlagSwModeSetting,
       "rxlabelSwModeThreshold": rxlabelSwModeThreshold,
       "rxenumSwModeThreshold": rxenumSwModeThreshold,
       "rxvalueSwModeThreshold": rxvalueSwModeThreshold,
       "rxstateFlagSwModeThreshold": rxstateFlagSwModeThreshold,
       "rxlabelFactoryDefault": rxlabelFactoryDefault,
       "rxenumFactoryDefault": rxenumFactoryDefault,
       "rxvalueFactoryDefault": rxvalueFactoryDefault,
       "rxstateFlagFactoryDefault": rxstateFlagFactoryDefault,
       "gx2Rx200StatusTable": gx2Rx200StatusTable,
       "gx2Rx200StatusEntry": gx2Rx200StatusEntry,
       "rxgx2Rx200StatusTableIndex": rxgx2Rx200StatusTableIndex,
       "rxlabelBoot": rxlabelBoot,
       "rxvalueBoot": rxvalueBoot,
       "rxstateflagBoot": rxstateflagBoot,
       "rxlabelFlash": rxlabelFlash,
       "rxvalueFlash": rxvalueFlash,
       "rxstateflagFlash": rxstateflagFlash,
       "rxlabelFactoryDataCRC": rxlabelFactoryDataCRC,
       "rxvalueFactoryDataCRC": rxvalueFactoryDataCRC,
       "rxstateflagFactoryDataCRC": rxstateflagFactoryDataCRC,
       "rxlabelAlarmDataCRC": rxlabelAlarmDataCRC,
       "rxvalueAlarmDataCRC": rxvalueAlarmDataCRC,
       "rxstateflagAlarmDataCRC": rxstateflagAlarmDataCRC,
       "rxlabelCalibrationDataCRC": rxlabelCalibrationDataCRC,
       "rxvalueCalibrationDataCRC": rxvalueCalibrationDataCRC,
       "rxstateflagCalibrationDataCRC": rxstateflagCalibrationDataCRC,
       "rxlabelThermalCompCRC": rxlabelThermalCompCRC,
       "rxvalueThermalCompCRC": rxvalueThermalCompCRC,
       "rxstateflagThermalCompCRC": rxstateflagThermalCompCRC,
       "rxlabelHW": rxlabelHW,
       "rxvalueHW": rxvalueHW,
       "rxstateflagHW": rxstateflagHW,
       "rxlabelOptSig": rxlabelOptSig,
       "rxvalueOptSig": rxvalueOptSig,
       "rxstateflagOptSig": rxstateflagOptSig,
       "gx2Rx200FactoryTable": gx2Rx200FactoryTable,
       "gx2Rx200FactoryEntry": gx2Rx200FactoryEntry,
       "rxgx2Rx200FactoryTableIndex": rxgx2Rx200FactoryTableIndex,
       "rxbootControlByte": rxbootControlByte,
       "rxbootStatusByte": rxbootStatusByte,
       "rxbank0CRC": rxbank0CRC,
       "rxbank1CRC": rxbank1CRC,
       "rxprgEEPROMByte": rxprgEEPROMByte,
       "rxfactoryCRC": rxfactoryCRC,
       "rxcalculateCRC": rxcalculateCRC,
       "rxhourMeter": rxhourMeter,
       "rxflashPrgCntA": rxflashPrgCntA,
       "rxflashPrgCntB": rxflashPrgCntB,
       "rxfwRev0": rxfwRev0,
       "rxfwRev1": rxfwRev1,
       "gx2Rx200HoldTimeTable": gx2Rx200HoldTimeTable,
       "gx2Rx200HoldTimeEntry": gx2Rx200HoldTimeEntry,
       "rxgx2Rx200HoldTimeTableIndex": rxgx2Rx200HoldTimeTableIndex,
       "rxgx2Rx200HoldTimeSpecIndex": rxgx2Rx200HoldTimeSpecIndex,
       "rxgx2Rx200HoldTimeData": rxgx2Rx200HoldTimeData}
)
