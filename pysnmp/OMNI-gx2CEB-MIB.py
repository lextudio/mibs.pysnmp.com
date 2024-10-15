# SNMP MIB module (OMNI-gx2CEB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2CEB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:12 2024
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

(gx2CEB,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2CEB")

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

_Gx2CEBDescriptor_ObjectIdentity = ObjectIdentity
gx2CEBDescriptor = _Gx2CEBDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 1)
)
_Gx2CEBAnalogTable_Object = MibTable
gx2CEBAnalogTable = _Gx2CEBAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    gx2CEBAnalogTable.setStatus("mandatory")
_Gx2CEBAnalogEntry_Object = MibTableRow
gx2CEBAnalogEntry = _Gx2CEBAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1)
)
gx2CEBAnalogEntry.setIndexNames(
    (0, "OMNI-gx2CEB-MIB", "gx2CEBAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2CEBAnalogEntry.setStatus("mandatory")


class _Gx2CEBAnalogTableIndex_Type(Integer32):
    """Custom type gx2CEBAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2CEBAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2CEBAnalogTableIndex_Object = MibTableColumn
gx2CEBAnalogTableIndex = _Gx2CEBAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 1),
    _Gx2CEBAnalogTableIndex_Type()
)
gx2CEBAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2CEBAnalogTableIndex.setStatus("mandatory")


class _CeblabelModTemp_Type(DisplayString):
    """Custom type ceblabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelModTemp_Type.__name__ = "DisplayString"
_CeblabelModTemp_Object = MibTableColumn
ceblabelModTemp = _CeblabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 2),
    _CeblabelModTemp_Type()
)
ceblabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelModTemp.setStatus("optional")


class _CebuomModTemp_Type(DisplayString):
    """Custom type cebuomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CebuomModTemp_Type.__name__ = "DisplayString"
_CebuomModTemp_Object = MibTableColumn
cebuomModTemp = _CebuomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 3),
    _CebuomModTemp_Type()
)
cebuomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebuomModTemp.setStatus("optional")
_CebmajorHighModTemp_Type = Float
_CebmajorHighModTemp_Object = MibTableColumn
cebmajorHighModTemp = _CebmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 4),
    _CebmajorHighModTemp_Type()
)
cebmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorHighModTemp.setStatus("mandatory")
_CebmajorLowModTemp_Type = Float
_CebmajorLowModTemp_Object = MibTableColumn
cebmajorLowModTemp = _CebmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 5),
    _CebmajorLowModTemp_Type()
)
cebmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorLowModTemp.setStatus("mandatory")
_CebminorHighModTemp_Type = Float
_CebminorHighModTemp_Object = MibTableColumn
cebminorHighModTemp = _CebminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 6),
    _CebminorHighModTemp_Type()
)
cebminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorHighModTemp.setStatus("mandatory")
_CebminorLowModTemp_Type = Float
_CebminorLowModTemp_Object = MibTableColumn
cebminorLowModTemp = _CebminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 7),
    _CebminorLowModTemp_Type()
)
cebminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorLowModTemp.setStatus("mandatory")
_CebcurrentValueModTemp_Type = Float
_CebcurrentValueModTemp_Object = MibTableColumn
cebcurrentValueModTemp = _CebcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 8),
    _CebcurrentValueModTemp_Type()
)
cebcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebcurrentValueModTemp.setStatus("mandatory")


class _CebstateFlagModTemp_Type(Integer32):
    """Custom type cebstateFlagModTemp based on Integer32"""
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


_CebstateFlagModTemp_Type.__name__ = "Integer32"
_CebstateFlagModTemp_Object = MibTableColumn
cebstateFlagModTemp = _CebstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 9),
    _CebstateFlagModTemp_Type()
)
cebstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateFlagModTemp.setStatus("mandatory")
_CebminValueModTemp_Type = Float
_CebminValueModTemp_Object = MibTableColumn
cebminValueModTemp = _CebminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 10),
    _CebminValueModTemp_Type()
)
cebminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminValueModTemp.setStatus("mandatory")
_CebmaxValueModTemp_Type = Float
_CebmaxValueModTemp_Object = MibTableColumn
cebmaxValueModTemp = _CebmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 11),
    _CebmaxValueModTemp_Type()
)
cebmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmaxValueModTemp.setStatus("mandatory")


class _CebalarmStateModTemp_Type(Integer32):
    """Custom type cebalarmStateModTemp based on Integer32"""
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


_CebalarmStateModTemp_Type.__name__ = "Integer32"
_CebalarmStateModTemp_Object = MibTableColumn
cebalarmStateModTemp = _CebalarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 12),
    _CebalarmStateModTemp_Type()
)
cebalarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebalarmStateModTemp.setStatus("mandatory")


class _CeblabelFanCurrent_Type(DisplayString):
    """Custom type ceblabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelFanCurrent_Type.__name__ = "DisplayString"
_CeblabelFanCurrent_Object = MibTableColumn
ceblabelFanCurrent = _CeblabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 13),
    _CeblabelFanCurrent_Type()
)
ceblabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelFanCurrent.setStatus("optional")


class _CebuomFanCurrent_Type(DisplayString):
    """Custom type cebuomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CebuomFanCurrent_Type.__name__ = "DisplayString"
_CebuomFanCurrent_Object = MibTableColumn
cebuomFanCurrent = _CebuomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 14),
    _CebuomFanCurrent_Type()
)
cebuomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebuomFanCurrent.setStatus("optional")
_CebmajorHighFanCurrent_Type = Float
_CebmajorHighFanCurrent_Object = MibTableColumn
cebmajorHighFanCurrent = _CebmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 15),
    _CebmajorHighFanCurrent_Type()
)
cebmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorHighFanCurrent.setStatus("mandatory")
_CebmajorLowFanCurrent_Type = Float
_CebmajorLowFanCurrent_Object = MibTableColumn
cebmajorLowFanCurrent = _CebmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 16),
    _CebmajorLowFanCurrent_Type()
)
cebmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorLowFanCurrent.setStatus("mandatory")
_CebminorHighFanCurrent_Type = Float
_CebminorHighFanCurrent_Object = MibTableColumn
cebminorHighFanCurrent = _CebminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 17),
    _CebminorHighFanCurrent_Type()
)
cebminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorHighFanCurrent.setStatus("obsolete")
_CebminorLowFanCurrent_Type = Float
_CebminorLowFanCurrent_Object = MibTableColumn
cebminorLowFanCurrent = _CebminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 18),
    _CebminorLowFanCurrent_Type()
)
cebminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorLowFanCurrent.setStatus("obsolete")
_CebcurrentValueFanCurrent_Type = Float
_CebcurrentValueFanCurrent_Object = MibTableColumn
cebcurrentValueFanCurrent = _CebcurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 19),
    _CebcurrentValueFanCurrent_Type()
)
cebcurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebcurrentValueFanCurrent.setStatus("mandatory")


class _CebstateFlagFanCurrent_Type(Integer32):
    """Custom type cebstateFlagFanCurrent based on Integer32"""
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


_CebstateFlagFanCurrent_Type.__name__ = "Integer32"
_CebstateFlagFanCurrent_Object = MibTableColumn
cebstateFlagFanCurrent = _CebstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 20),
    _CebstateFlagFanCurrent_Type()
)
cebstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateFlagFanCurrent.setStatus("mandatory")
_CebminValueFanCurrent_Type = Float
_CebminValueFanCurrent_Object = MibTableColumn
cebminValueFanCurrent = _CebminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 21),
    _CebminValueFanCurrent_Type()
)
cebminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminValueFanCurrent.setStatus("mandatory")
_CebmaxValueFanCurrent_Type = Float
_CebmaxValueFanCurrent_Object = MibTableColumn
cebmaxValueFanCurrent = _CebmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 22),
    _CebmaxValueFanCurrent_Type()
)
cebmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmaxValueFanCurrent.setStatus("mandatory")


class _CebalarmStateFanCurrent_Type(Integer32):
    """Custom type cebalarmStateFanCurrent based on Integer32"""
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


_CebalarmStateFanCurrent_Type.__name__ = "Integer32"
_CebalarmStateFanCurrent_Object = MibTableColumn
cebalarmStateFanCurrent = _CebalarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 23),
    _CebalarmStateFanCurrent_Type()
)
cebalarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebalarmStateFanCurrent.setStatus("mandatory")


class _CeblabelAnalogVoltage01_Type(DisplayString):
    """Custom type ceblabelAnalogVoltage01 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelAnalogVoltage01_Type.__name__ = "DisplayString"
_CeblabelAnalogVoltage01_Object = MibTableColumn
ceblabelAnalogVoltage01 = _CeblabelAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 24),
    _CeblabelAnalogVoltage01_Type()
)
ceblabelAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelAnalogVoltage01.setStatus("optional")


class _CebuomAnalogVoltage01_Type(DisplayString):
    """Custom type cebuomAnalogVoltage01 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CebuomAnalogVoltage01_Type.__name__ = "DisplayString"
_CebuomAnalogVoltage01_Object = MibTableColumn
cebuomAnalogVoltage01 = _CebuomAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 25),
    _CebuomAnalogVoltage01_Type()
)
cebuomAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebuomAnalogVoltage01.setStatus("optional")
_CebmajorHighAnalogVoltage01_Type = Float
_CebmajorHighAnalogVoltage01_Object = MibTableColumn
cebmajorHighAnalogVoltage01 = _CebmajorHighAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 26),
    _CebmajorHighAnalogVoltage01_Type()
)
cebmajorHighAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorHighAnalogVoltage01.setStatus("mandatory")
_CebmajorLowAnalogVoltage01_Type = Float
_CebmajorLowAnalogVoltage01_Object = MibTableColumn
cebmajorLowAnalogVoltage01 = _CebmajorLowAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 27),
    _CebmajorLowAnalogVoltage01_Type()
)
cebmajorLowAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorLowAnalogVoltage01.setStatus("mandatory")
_CebminorHighAnalogVoltage01_Type = Float
_CebminorHighAnalogVoltage01_Object = MibTableColumn
cebminorHighAnalogVoltage01 = _CebminorHighAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 28),
    _CebminorHighAnalogVoltage01_Type()
)
cebminorHighAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorHighAnalogVoltage01.setStatus("mandatory")
_CebminorLowAnalogVoltage01_Type = Float
_CebminorLowAnalogVoltage01_Object = MibTableColumn
cebminorLowAnalogVoltage01 = _CebminorLowAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 29),
    _CebminorLowAnalogVoltage01_Type()
)
cebminorLowAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorLowAnalogVoltage01.setStatus("mandatory")
_CebcurrentValueAnalogVoltage01_Type = Float
_CebcurrentValueAnalogVoltage01_Object = MibTableColumn
cebcurrentValueAnalogVoltage01 = _CebcurrentValueAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 30),
    _CebcurrentValueAnalogVoltage01_Type()
)
cebcurrentValueAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebcurrentValueAnalogVoltage01.setStatus("mandatory")


class _CebstateFlagAnalogVoltage01_Type(Integer32):
    """Custom type cebstateFlagAnalogVoltage01 based on Integer32"""
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


_CebstateFlagAnalogVoltage01_Type.__name__ = "Integer32"
_CebstateFlagAnalogVoltage01_Object = MibTableColumn
cebstateFlagAnalogVoltage01 = _CebstateFlagAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 31),
    _CebstateFlagAnalogVoltage01_Type()
)
cebstateFlagAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateFlagAnalogVoltage01.setStatus("mandatory")
_CebminValueAnalogVoltage01_Type = Float
_CebminValueAnalogVoltage01_Object = MibTableColumn
cebminValueAnalogVoltage01 = _CebminValueAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 32),
    _CebminValueAnalogVoltage01_Type()
)
cebminValueAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminValueAnalogVoltage01.setStatus("mandatory")
_CebmaxValueAnalogVoltage01_Type = Float
_CebmaxValueAnalogVoltage01_Object = MibTableColumn
cebmaxValueAnalogVoltage01 = _CebmaxValueAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 33),
    _CebmaxValueAnalogVoltage01_Type()
)
cebmaxValueAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmaxValueAnalogVoltage01.setStatus("mandatory")


class _CebalarmStateAnalogVoltage01_Type(Integer32):
    """Custom type cebalarmStateAnalogVoltage01 based on Integer32"""
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


_CebalarmStateAnalogVoltage01_Type.__name__ = "Integer32"
_CebalarmStateAnalogVoltage01_Object = MibTableColumn
cebalarmStateAnalogVoltage01 = _CebalarmStateAnalogVoltage01_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 34),
    _CebalarmStateAnalogVoltage01_Type()
)
cebalarmStateAnalogVoltage01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebalarmStateAnalogVoltage01.setStatus("mandatory")


class _CeblabelAnalogVoltage02_Type(DisplayString):
    """Custom type ceblabelAnalogVoltage02 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelAnalogVoltage02_Type.__name__ = "DisplayString"
_CeblabelAnalogVoltage02_Object = MibTableColumn
ceblabelAnalogVoltage02 = _CeblabelAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 35),
    _CeblabelAnalogVoltage02_Type()
)
ceblabelAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelAnalogVoltage02.setStatus("optional")


class _CebuomAnalogVoltage02_Type(DisplayString):
    """Custom type cebuomAnalogVoltage02 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CebuomAnalogVoltage02_Type.__name__ = "DisplayString"
_CebuomAnalogVoltage02_Object = MibTableColumn
cebuomAnalogVoltage02 = _CebuomAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 36),
    _CebuomAnalogVoltage02_Type()
)
cebuomAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebuomAnalogVoltage02.setStatus("optional")
_CebmajorHighAnalogVoltage02_Type = Float
_CebmajorHighAnalogVoltage02_Object = MibTableColumn
cebmajorHighAnalogVoltage02 = _CebmajorHighAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 37),
    _CebmajorHighAnalogVoltage02_Type()
)
cebmajorHighAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorHighAnalogVoltage02.setStatus("mandatory")
_CebmajorLowAnalogVoltage02_Type = Float
_CebmajorLowAnalogVoltage02_Object = MibTableColumn
cebmajorLowAnalogVoltage02 = _CebmajorLowAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 38),
    _CebmajorLowAnalogVoltage02_Type()
)
cebmajorLowAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorLowAnalogVoltage02.setStatus("mandatory")
_CebminorHighAnalogVoltage02_Type = Float
_CebminorHighAnalogVoltage02_Object = MibTableColumn
cebminorHighAnalogVoltage02 = _CebminorHighAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 39),
    _CebminorHighAnalogVoltage02_Type()
)
cebminorHighAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorHighAnalogVoltage02.setStatus("mandatory")
_CebminorLowAnalogVoltage02_Type = Float
_CebminorLowAnalogVoltage02_Object = MibTableColumn
cebminorLowAnalogVoltage02 = _CebminorLowAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 40),
    _CebminorLowAnalogVoltage02_Type()
)
cebminorLowAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorLowAnalogVoltage02.setStatus("mandatory")
_CebcurrentValueAnalogVoltage02_Type = Float
_CebcurrentValueAnalogVoltage02_Object = MibTableColumn
cebcurrentValueAnalogVoltage02 = _CebcurrentValueAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 41),
    _CebcurrentValueAnalogVoltage02_Type()
)
cebcurrentValueAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebcurrentValueAnalogVoltage02.setStatus("mandatory")


class _CebstateFlagAnalogVoltage02_Type(Integer32):
    """Custom type cebstateFlagAnalogVoltage02 based on Integer32"""
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


_CebstateFlagAnalogVoltage02_Type.__name__ = "Integer32"
_CebstateFlagAnalogVoltage02_Object = MibTableColumn
cebstateFlagAnalogVoltage02 = _CebstateFlagAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 42),
    _CebstateFlagAnalogVoltage02_Type()
)
cebstateFlagAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateFlagAnalogVoltage02.setStatus("mandatory")
_CebminValueAnalogVoltage02_Type = Float
_CebminValueAnalogVoltage02_Object = MibTableColumn
cebminValueAnalogVoltage02 = _CebminValueAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 43),
    _CebminValueAnalogVoltage02_Type()
)
cebminValueAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminValueAnalogVoltage02.setStatus("mandatory")
_CebmaxValueAnalogVoltage02_Type = Float
_CebmaxValueAnalogVoltage02_Object = MibTableColumn
cebmaxValueAnalogVoltage02 = _CebmaxValueAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 44),
    _CebmaxValueAnalogVoltage02_Type()
)
cebmaxValueAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmaxValueAnalogVoltage02.setStatus("mandatory")


class _CebalarmStateAnalogVoltage02_Type(Integer32):
    """Custom type cebalarmStateAnalogVoltage02 based on Integer32"""
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


_CebalarmStateAnalogVoltage02_Type.__name__ = "Integer32"
_CebalarmStateAnalogVoltage02_Object = MibTableColumn
cebalarmStateAnalogVoltage02 = _CebalarmStateAnalogVoltage02_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 45),
    _CebalarmStateAnalogVoltage02_Type()
)
cebalarmStateAnalogVoltage02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebalarmStateAnalogVoltage02.setStatus("mandatory")


class _CeblabelAnalogVoltage03_Type(DisplayString):
    """Custom type ceblabelAnalogVoltage03 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelAnalogVoltage03_Type.__name__ = "DisplayString"
_CeblabelAnalogVoltage03_Object = MibTableColumn
ceblabelAnalogVoltage03 = _CeblabelAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 46),
    _CeblabelAnalogVoltage03_Type()
)
ceblabelAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelAnalogVoltage03.setStatus("optional")


class _CebuomAnalogVoltage03_Type(DisplayString):
    """Custom type cebuomAnalogVoltage03 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CebuomAnalogVoltage03_Type.__name__ = "DisplayString"
_CebuomAnalogVoltage03_Object = MibTableColumn
cebuomAnalogVoltage03 = _CebuomAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 47),
    _CebuomAnalogVoltage03_Type()
)
cebuomAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebuomAnalogVoltage03.setStatus("optional")
_CebmajorHighAnalogVoltage03_Type = Float
_CebmajorHighAnalogVoltage03_Object = MibTableColumn
cebmajorHighAnalogVoltage03 = _CebmajorHighAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 48),
    _CebmajorHighAnalogVoltage03_Type()
)
cebmajorHighAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorHighAnalogVoltage03.setStatus("mandatory")
_CebmajorLowAnalogVoltage03_Type = Float
_CebmajorLowAnalogVoltage03_Object = MibTableColumn
cebmajorLowAnalogVoltage03 = _CebmajorLowAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 49),
    _CebmajorLowAnalogVoltage03_Type()
)
cebmajorLowAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorLowAnalogVoltage03.setStatus("mandatory")
_CebminorHighAnalogVoltage03_Type = Float
_CebminorHighAnalogVoltage03_Object = MibTableColumn
cebminorHighAnalogVoltage03 = _CebminorHighAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 50),
    _CebminorHighAnalogVoltage03_Type()
)
cebminorHighAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorHighAnalogVoltage03.setStatus("mandatory")
_CebminorLowAnalogVoltage03_Type = Float
_CebminorLowAnalogVoltage03_Object = MibTableColumn
cebminorLowAnalogVoltage03 = _CebminorLowAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 51),
    _CebminorLowAnalogVoltage03_Type()
)
cebminorLowAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorLowAnalogVoltage03.setStatus("mandatory")
_CebcurrentValueAnalogVoltage03_Type = Float
_CebcurrentValueAnalogVoltage03_Object = MibTableColumn
cebcurrentValueAnalogVoltage03 = _CebcurrentValueAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 52),
    _CebcurrentValueAnalogVoltage03_Type()
)
cebcurrentValueAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebcurrentValueAnalogVoltage03.setStatus("mandatory")


class _CebstateFlagAnalogVoltage03_Type(Integer32):
    """Custom type cebstateFlagAnalogVoltage03 based on Integer32"""
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


_CebstateFlagAnalogVoltage03_Type.__name__ = "Integer32"
_CebstateFlagAnalogVoltage03_Object = MibTableColumn
cebstateFlagAnalogVoltage03 = _CebstateFlagAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 53),
    _CebstateFlagAnalogVoltage03_Type()
)
cebstateFlagAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateFlagAnalogVoltage03.setStatus("mandatory")
_CebminValueAnalogVoltage03_Type = Float
_CebminValueAnalogVoltage03_Object = MibTableColumn
cebminValueAnalogVoltage03 = _CebminValueAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 54),
    _CebminValueAnalogVoltage03_Type()
)
cebminValueAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminValueAnalogVoltage03.setStatus("mandatory")
_CebmaxValueAnalogVoltage03_Type = Float
_CebmaxValueAnalogVoltage03_Object = MibTableColumn
cebmaxValueAnalogVoltage03 = _CebmaxValueAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 55),
    _CebmaxValueAnalogVoltage03_Type()
)
cebmaxValueAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmaxValueAnalogVoltage03.setStatus("mandatory")


class _CebalarmStateAnalogVoltage03_Type(Integer32):
    """Custom type cebalarmStateAnalogVoltage03 based on Integer32"""
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


_CebalarmStateAnalogVoltage03_Type.__name__ = "Integer32"
_CebalarmStateAnalogVoltage03_Object = MibTableColumn
cebalarmStateAnalogVoltage03 = _CebalarmStateAnalogVoltage03_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 56),
    _CebalarmStateAnalogVoltage03_Type()
)
cebalarmStateAnalogVoltage03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebalarmStateAnalogVoltage03.setStatus("mandatory")


class _CeblabelAnalogVoltage04_Type(DisplayString):
    """Custom type ceblabelAnalogVoltage04 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelAnalogVoltage04_Type.__name__ = "DisplayString"
_CeblabelAnalogVoltage04_Object = MibTableColumn
ceblabelAnalogVoltage04 = _CeblabelAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 57),
    _CeblabelAnalogVoltage04_Type()
)
ceblabelAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelAnalogVoltage04.setStatus("optional")


class _CebuomAnalogVoltage04_Type(DisplayString):
    """Custom type cebuomAnalogVoltage04 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CebuomAnalogVoltage04_Type.__name__ = "DisplayString"
_CebuomAnalogVoltage04_Object = MibTableColumn
cebuomAnalogVoltage04 = _CebuomAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 58),
    _CebuomAnalogVoltage04_Type()
)
cebuomAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebuomAnalogVoltage04.setStatus("optional")
_CebmajorHighAnalogVoltage04_Type = Float
_CebmajorHighAnalogVoltage04_Object = MibTableColumn
cebmajorHighAnalogVoltage04 = _CebmajorHighAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 59),
    _CebmajorHighAnalogVoltage04_Type()
)
cebmajorHighAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorHighAnalogVoltage04.setStatus("mandatory")
_CebmajorLowAnalogVoltage04_Type = Float
_CebmajorLowAnalogVoltage04_Object = MibTableColumn
cebmajorLowAnalogVoltage04 = _CebmajorLowAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 60),
    _CebmajorLowAnalogVoltage04_Type()
)
cebmajorLowAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorLowAnalogVoltage04.setStatus("mandatory")
_CebminorHighAnalogVoltage04_Type = Float
_CebminorHighAnalogVoltage04_Object = MibTableColumn
cebminorHighAnalogVoltage04 = _CebminorHighAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 61),
    _CebminorHighAnalogVoltage04_Type()
)
cebminorHighAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorHighAnalogVoltage04.setStatus("mandatory")
_CebminorLowAnalogVoltage04_Type = Float
_CebminorLowAnalogVoltage04_Object = MibTableColumn
cebminorLowAnalogVoltage04 = _CebminorLowAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 62),
    _CebminorLowAnalogVoltage04_Type()
)
cebminorLowAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorLowAnalogVoltage04.setStatus("mandatory")
_CebcurrentValueAnalogVoltage04_Type = Float
_CebcurrentValueAnalogVoltage04_Object = MibTableColumn
cebcurrentValueAnalogVoltage04 = _CebcurrentValueAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 63),
    _CebcurrentValueAnalogVoltage04_Type()
)
cebcurrentValueAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebcurrentValueAnalogVoltage04.setStatus("mandatory")


class _CebstateFlagAnalogVoltage04_Type(Integer32):
    """Custom type cebstateFlagAnalogVoltage04 based on Integer32"""
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


_CebstateFlagAnalogVoltage04_Type.__name__ = "Integer32"
_CebstateFlagAnalogVoltage04_Object = MibTableColumn
cebstateFlagAnalogVoltage04 = _CebstateFlagAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 64),
    _CebstateFlagAnalogVoltage04_Type()
)
cebstateFlagAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateFlagAnalogVoltage04.setStatus("mandatory")
_CebminValueAnalogVoltage04_Type = Float
_CebminValueAnalogVoltage04_Object = MibTableColumn
cebminValueAnalogVoltage04 = _CebminValueAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 65),
    _CebminValueAnalogVoltage04_Type()
)
cebminValueAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminValueAnalogVoltage04.setStatus("mandatory")
_CebmaxValueAnalogVoltage04_Type = Float
_CebmaxValueAnalogVoltage04_Object = MibTableColumn
cebmaxValueAnalogVoltage04 = _CebmaxValueAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 66),
    _CebmaxValueAnalogVoltage04_Type()
)
cebmaxValueAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmaxValueAnalogVoltage04.setStatus("mandatory")


class _CebalarmStateAnalogVoltage04_Type(Integer32):
    """Custom type cebalarmStateAnalogVoltage04 based on Integer32"""
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


_CebalarmStateAnalogVoltage04_Type.__name__ = "Integer32"
_CebalarmStateAnalogVoltage04_Object = MibTableColumn
cebalarmStateAnalogVoltage04 = _CebalarmStateAnalogVoltage04_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 67),
    _CebalarmStateAnalogVoltage04_Type()
)
cebalarmStateAnalogVoltage04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebalarmStateAnalogVoltage04.setStatus("mandatory")


class _CeblabelAnalogVoltage05_Type(DisplayString):
    """Custom type ceblabelAnalogVoltage05 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelAnalogVoltage05_Type.__name__ = "DisplayString"
_CeblabelAnalogVoltage05_Object = MibTableColumn
ceblabelAnalogVoltage05 = _CeblabelAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 68),
    _CeblabelAnalogVoltage05_Type()
)
ceblabelAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelAnalogVoltage05.setStatus("optional")


class _CebuomAnalogVoltage05_Type(DisplayString):
    """Custom type cebuomAnalogVoltage05 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CebuomAnalogVoltage05_Type.__name__ = "DisplayString"
_CebuomAnalogVoltage05_Object = MibTableColumn
cebuomAnalogVoltage05 = _CebuomAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 69),
    _CebuomAnalogVoltage05_Type()
)
cebuomAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebuomAnalogVoltage05.setStatus("optional")
_CebmajorHighAnalogVoltage05_Type = Float
_CebmajorHighAnalogVoltage05_Object = MibTableColumn
cebmajorHighAnalogVoltage05 = _CebmajorHighAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 70),
    _CebmajorHighAnalogVoltage05_Type()
)
cebmajorHighAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorHighAnalogVoltage05.setStatus("mandatory")
_CebmajorLowAnalogVoltage05_Type = Float
_CebmajorLowAnalogVoltage05_Object = MibTableColumn
cebmajorLowAnalogVoltage05 = _CebmajorLowAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 71),
    _CebmajorLowAnalogVoltage05_Type()
)
cebmajorLowAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmajorLowAnalogVoltage05.setStatus("mandatory")
_CebminorHighAnalogVoltage05_Type = Float
_CebminorHighAnalogVoltage05_Object = MibTableColumn
cebminorHighAnalogVoltage05 = _CebminorHighAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 72),
    _CebminorHighAnalogVoltage05_Type()
)
cebminorHighAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorHighAnalogVoltage05.setStatus("mandatory")
_CebminorLowAnalogVoltage05_Type = Float
_CebminorLowAnalogVoltage05_Object = MibTableColumn
cebminorLowAnalogVoltage05 = _CebminorLowAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 73),
    _CebminorLowAnalogVoltage05_Type()
)
cebminorLowAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminorLowAnalogVoltage05.setStatus("mandatory")
_CebcurrentValueAnalogVoltage05_Type = Float
_CebcurrentValueAnalogVoltage05_Object = MibTableColumn
cebcurrentValueAnalogVoltage05 = _CebcurrentValueAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 74),
    _CebcurrentValueAnalogVoltage05_Type()
)
cebcurrentValueAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebcurrentValueAnalogVoltage05.setStatus("mandatory")


class _CebstateFlagAnalogVoltage05_Type(Integer32):
    """Custom type cebstateFlagAnalogVoltage05 based on Integer32"""
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


_CebstateFlagAnalogVoltage05_Type.__name__ = "Integer32"
_CebstateFlagAnalogVoltage05_Object = MibTableColumn
cebstateFlagAnalogVoltage05 = _CebstateFlagAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 75),
    _CebstateFlagAnalogVoltage05_Type()
)
cebstateFlagAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateFlagAnalogVoltage05.setStatus("mandatory")
_CebminValueAnalogVoltage05_Type = Float
_CebminValueAnalogVoltage05_Object = MibTableColumn
cebminValueAnalogVoltage05 = _CebminValueAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 76),
    _CebminValueAnalogVoltage05_Type()
)
cebminValueAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebminValueAnalogVoltage05.setStatus("mandatory")
_CebmaxValueAnalogVoltage05_Type = Float
_CebmaxValueAnalogVoltage05_Object = MibTableColumn
cebmaxValueAnalogVoltage05 = _CebmaxValueAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 77),
    _CebmaxValueAnalogVoltage05_Type()
)
cebmaxValueAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebmaxValueAnalogVoltage05.setStatus("mandatory")


class _CebalarmStateAnalogVoltage05_Type(Integer32):
    """Custom type cebalarmStateAnalogVoltage05 based on Integer32"""
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


_CebalarmStateAnalogVoltage05_Type.__name__ = "Integer32"
_CebalarmStateAnalogVoltage05_Object = MibTableColumn
cebalarmStateAnalogVoltage05 = _CebalarmStateAnalogVoltage05_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 2, 1, 78),
    _CebalarmStateAnalogVoltage05_Type()
)
cebalarmStateAnalogVoltage05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebalarmStateAnalogVoltage05.setStatus("mandatory")
_Gx2CEBStatusTable_Object = MibTable
gx2CEBStatusTable = _Gx2CEBStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3)
)
if mibBuilder.loadTexts:
    gx2CEBStatusTable.setStatus("mandatory")
_Gx2CEBStatusEntry_Object = MibTableRow
gx2CEBStatusEntry = _Gx2CEBStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2)
)
gx2CEBStatusEntry.setIndexNames(
    (0, "OMNI-gx2CEB-MIB", "gx2CEBStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2CEBStatusEntry.setStatus("mandatory")


class _Gx2CEBStatusTableIndex_Type(Integer32):
    """Custom type gx2CEBStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2CEBStatusTableIndex_Type.__name__ = "Integer32"
_Gx2CEBStatusTableIndex_Object = MibTableColumn
gx2CEBStatusTableIndex = _Gx2CEBStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 1),
    _Gx2CEBStatusTableIndex_Type()
)
gx2CEBStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2CEBStatusTableIndex.setStatus("mandatory")


class _CeblabelBoot_Type(DisplayString):
    """Custom type ceblabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelBoot_Type.__name__ = "DisplayString"
_CeblabelBoot_Object = MibTableColumn
ceblabelBoot = _CeblabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 2),
    _CeblabelBoot_Type()
)
ceblabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelBoot.setStatus("optional")


class _CebvalueBoot_Type(Integer32):
    """Custom type cebvalueBoot based on Integer32"""
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


_CebvalueBoot_Type.__name__ = "Integer32"
_CebvalueBoot_Object = MibTableColumn
cebvalueBoot = _CebvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 3),
    _CebvalueBoot_Type()
)
cebvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebvalueBoot.setStatus("mandatory")


class _CebstateflagBoot_Type(Integer32):
    """Custom type cebstateflagBoot based on Integer32"""
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


_CebstateflagBoot_Type.__name__ = "Integer32"
_CebstateflagBoot_Object = MibTableColumn
cebstateflagBoot = _CebstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 4),
    _CebstateflagBoot_Type()
)
cebstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateflagBoot.setStatus("mandatory")


class _CeblabelFlash_Type(DisplayString):
    """Custom type ceblabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelFlash_Type.__name__ = "DisplayString"
_CeblabelFlash_Object = MibTableColumn
ceblabelFlash = _CeblabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 5),
    _CeblabelFlash_Type()
)
ceblabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelFlash.setStatus("optional")


class _CebvalueFlash_Type(Integer32):
    """Custom type cebvalueFlash based on Integer32"""
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


_CebvalueFlash_Type.__name__ = "Integer32"
_CebvalueFlash_Object = MibTableColumn
cebvalueFlash = _CebvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 6),
    _CebvalueFlash_Type()
)
cebvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebvalueFlash.setStatus("mandatory")


class _CebstateflagFlash_Type(Integer32):
    """Custom type cebstateflagFlash based on Integer32"""
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


_CebstateflagFlash_Type.__name__ = "Integer32"
_CebstateflagFlash_Object = MibTableColumn
cebstateflagFlash = _CebstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 7),
    _CebstateflagFlash_Type()
)
cebstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateflagFlash.setStatus("mandatory")


class _CeblabelFactoryDataCRC_Type(DisplayString):
    """Custom type ceblabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelFactoryDataCRC_Type.__name__ = "DisplayString"
_CeblabelFactoryDataCRC_Object = MibTableColumn
ceblabelFactoryDataCRC = _CeblabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 8),
    _CeblabelFactoryDataCRC_Type()
)
ceblabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelFactoryDataCRC.setStatus("optional")


class _CebvalueFactoryDataCRC_Type(Integer32):
    """Custom type cebvalueFactoryDataCRC based on Integer32"""
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


_CebvalueFactoryDataCRC_Type.__name__ = "Integer32"
_CebvalueFactoryDataCRC_Object = MibTableColumn
cebvalueFactoryDataCRC = _CebvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 9),
    _CebvalueFactoryDataCRC_Type()
)
cebvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebvalueFactoryDataCRC.setStatus("mandatory")


class _CebstateflagFactoryDataCRC_Type(Integer32):
    """Custom type cebstateflagFactoryDataCRC based on Integer32"""
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


_CebstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_CebstateflagFactoryDataCRC_Object = MibTableColumn
cebstateflagFactoryDataCRC = _CebstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 10),
    _CebstateflagFactoryDataCRC_Type()
)
cebstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateflagFactoryDataCRC.setStatus("mandatory")


class _CeblabelAlarmDataCrc_Type(DisplayString):
    """Custom type ceblabelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CeblabelAlarmDataCrc_Type.__name__ = "DisplayString"
_CeblabelAlarmDataCrc_Object = MibTableColumn
ceblabelAlarmDataCrc = _CeblabelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 11),
    _CeblabelAlarmDataCrc_Type()
)
ceblabelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceblabelAlarmDataCrc.setStatus("optional")


class _CebvalueAlarmDataCrc_Type(Integer32):
    """Custom type cebvalueAlarmDataCrc based on Integer32"""
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


_CebvalueAlarmDataCrc_Type.__name__ = "Integer32"
_CebvalueAlarmDataCrc_Object = MibTableColumn
cebvalueAlarmDataCrc = _CebvalueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 12),
    _CebvalueAlarmDataCrc_Type()
)
cebvalueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebvalueAlarmDataCrc.setStatus("mandatory")


class _CebstateflagAlarmDataCrc_Type(Integer32):
    """Custom type cebstateflagAlarmDataCrc based on Integer32"""
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


_CebstateflagAlarmDataCrc_Type.__name__ = "Integer32"
_CebstateflagAlarmDataCrc_Object = MibTableColumn
cebstateflagAlarmDataCrc = _CebstateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 3, 2, 13),
    _CebstateflagAlarmDataCrc_Type()
)
cebstateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebstateflagAlarmDataCrc.setStatus("mandatory")
_Gx2CEBFactoryTable_Object = MibTable
gx2CEBFactoryTable = _Gx2CEBFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4)
)
if mibBuilder.loadTexts:
    gx2CEBFactoryTable.setStatus("mandatory")
_Gx2CEBFactoryEntry_Object = MibTableRow
gx2CEBFactoryEntry = _Gx2CEBFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3)
)
gx2CEBFactoryEntry.setIndexNames(
    (0, "OMNI-gx2CEB-MIB", "gx2CEBFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2CEBFactoryEntry.setStatus("mandatory")


class _Gx2CEBFactoryTableIndex_Type(Integer32):
    """Custom type gx2CEBFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2CEBFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2CEBFactoryTableIndex_Object = MibTableColumn
gx2CEBFactoryTableIndex = _Gx2CEBFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 1),
    _Gx2CEBFactoryTableIndex_Type()
)
gx2CEBFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2CEBFactoryTableIndex.setStatus("mandatory")
_CebbootControlByte_Type = Integer32
_CebbootControlByte_Object = MibTableColumn
cebbootControlByte = _CebbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 2),
    _CebbootControlByte_Type()
)
cebbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebbootControlByte.setStatus("mandatory")
_CebbootStatusByte_Type = Integer32
_CebbootStatusByte_Object = MibTableColumn
cebbootStatusByte = _CebbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 3),
    _CebbootStatusByte_Type()
)
cebbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebbootStatusByte.setStatus("mandatory")
_Cebbank1CRC_Type = Integer32
_Cebbank1CRC_Object = MibTableColumn
cebbank1CRC = _Cebbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 4),
    _Cebbank1CRC_Type()
)
cebbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebbank1CRC.setStatus("mandatory")
_Cebbank2CRC_Type = Integer32
_Cebbank2CRC_Object = MibTableColumn
cebbank2CRC = _Cebbank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 5),
    _Cebbank2CRC_Type()
)
cebbank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebbank2CRC.setStatus("mandatory")
_CebprgEEPROMByte_Type = Integer32
_CebprgEEPROMByte_Object = MibTableColumn
cebprgEEPROMByte = _CebprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 6),
    _CebprgEEPROMByte_Type()
)
cebprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebprgEEPROMByte.setStatus("mandatory")
_CebfactoryCRC_Type = Integer32
_CebfactoryCRC_Object = MibTableColumn
cebfactoryCRC = _CebfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 7),
    _CebfactoryCRC_Type()
)
cebfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebfactoryCRC.setStatus("mandatory")


class _CebcalculateCRC_Type(Integer32):
    """Custom type cebcalculateCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("factory", 1),
          ("na", 2))
    )


_CebcalculateCRC_Type.__name__ = "Integer32"
_CebcalculateCRC_Object = MibTableColumn
cebcalculateCRC = _CebcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 8),
    _CebcalculateCRC_Type()
)
cebcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebcalculateCRC.setStatus("obsolete")
_CebhourMeter_Type = Integer32
_CebhourMeter_Object = MibTableColumn
cebhourMeter = _CebhourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 9),
    _CebhourMeter_Type()
)
cebhourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebhourMeter.setStatus("mandatory")
_CebflashPrgCntA_Type = Integer32
_CebflashPrgCntA_Object = MibTableColumn
cebflashPrgCntA = _CebflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 10),
    _CebflashPrgCntA_Type()
)
cebflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebflashPrgCntA.setStatus("mandatory")
_CebflashPrgCntB_Type = Integer32
_CebflashPrgCntB_Object = MibTableColumn
cebflashPrgCntB = _CebflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 11),
    _CebflashPrgCntB_Type()
)
cebflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebflashPrgCntB.setStatus("mandatory")


class _CebflashBankARev_Type(DisplayString):
    """Custom type cebflashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CebflashBankARev_Type.__name__ = "DisplayString"
_CebflashBankARev_Object = MibTableColumn
cebflashBankARev = _CebflashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 12),
    _CebflashBankARev_Type()
)
cebflashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebflashBankARev.setStatus("mandatory")


class _CebflashBankBRev_Type(DisplayString):
    """Custom type cebflashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CebflashBankBRev_Type.__name__ = "DisplayString"
_CebflashBankBRev_Object = MibTableColumn
cebflashBankBRev = _CebflashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 4, 3, 13),
    _CebflashBankBRev_Type()
)
cebflashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cebflashBankBRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapCEBConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 0, 1)
)
trapCEBConfigChangeInteger.setObjects(
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
    trapCEBConfigChangeInteger.setStatus(
        ""
    )

trapCEBConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 0, 2)
)
trapCEBConfigChangeDisplayString.setObjects(
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
    trapCEBConfigChangeDisplayString.setStatus(
        ""
    )

trapCEBfanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 0, 3)
)
trapCEBfanCurrentAlarm.setObjects(
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
    trapCEBfanCurrentAlarm.setStatus(
        ""
    )

trapCEBModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 0, 4)
)
trapCEBModuleTempAlarm.setObjects(
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
    trapCEBModuleTempAlarm.setStatus(
        ""
    )

trapCEBFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 0, 5)
)
trapCEBFlashAlarm.setObjects(
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
    trapCEBFlashAlarm.setStatus(
        ""
    )

trapCEBBankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 0, 6)
)
trapCEBBankBootAlarm.setObjects(
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
    trapCEBBankBootAlarm.setStatus(
        ""
    )

trapCEBAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 0, 7)
)
trapCEBAlarmDataCRCAlarm.setObjects(
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
    trapCEBAlarmDataCRCAlarm.setStatus(
        ""
    )

trapCEBFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20, 0, 8)
)
trapCEBFactoryDataCRCAlarm.setObjects(
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
    trapCEBFactoryDataCRCAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2CEB-MIB",
    **{"Float": Float,
       "trapCEBConfigChangeInteger": trapCEBConfigChangeInteger,
       "trapCEBConfigChangeDisplayString": trapCEBConfigChangeDisplayString,
       "trapCEBfanCurrentAlarm": trapCEBfanCurrentAlarm,
       "trapCEBModuleTempAlarm": trapCEBModuleTempAlarm,
       "trapCEBFlashAlarm": trapCEBFlashAlarm,
       "trapCEBBankBootAlarm": trapCEBBankBootAlarm,
       "trapCEBAlarmDataCRCAlarm": trapCEBAlarmDataCRCAlarm,
       "trapCEBFactoryDataCRCAlarm": trapCEBFactoryDataCRCAlarm,
       "gx2CEBDescriptor": gx2CEBDescriptor,
       "gx2CEBAnalogTable": gx2CEBAnalogTable,
       "gx2CEBAnalogEntry": gx2CEBAnalogEntry,
       "gx2CEBAnalogTableIndex": gx2CEBAnalogTableIndex,
       "ceblabelModTemp": ceblabelModTemp,
       "cebuomModTemp": cebuomModTemp,
       "cebmajorHighModTemp": cebmajorHighModTemp,
       "cebmajorLowModTemp": cebmajorLowModTemp,
       "cebminorHighModTemp": cebminorHighModTemp,
       "cebminorLowModTemp": cebminorLowModTemp,
       "cebcurrentValueModTemp": cebcurrentValueModTemp,
       "cebstateFlagModTemp": cebstateFlagModTemp,
       "cebminValueModTemp": cebminValueModTemp,
       "cebmaxValueModTemp": cebmaxValueModTemp,
       "cebalarmStateModTemp": cebalarmStateModTemp,
       "ceblabelFanCurrent": ceblabelFanCurrent,
       "cebuomFanCurrent": cebuomFanCurrent,
       "cebmajorHighFanCurrent": cebmajorHighFanCurrent,
       "cebmajorLowFanCurrent": cebmajorLowFanCurrent,
       "cebminorHighFanCurrent": cebminorHighFanCurrent,
       "cebminorLowFanCurrent": cebminorLowFanCurrent,
       "cebcurrentValueFanCurrent": cebcurrentValueFanCurrent,
       "cebstateFlagFanCurrent": cebstateFlagFanCurrent,
       "cebminValueFanCurrent": cebminValueFanCurrent,
       "cebmaxValueFanCurrent": cebmaxValueFanCurrent,
       "cebalarmStateFanCurrent": cebalarmStateFanCurrent,
       "ceblabelAnalogVoltage01": ceblabelAnalogVoltage01,
       "cebuomAnalogVoltage01": cebuomAnalogVoltage01,
       "cebmajorHighAnalogVoltage01": cebmajorHighAnalogVoltage01,
       "cebmajorLowAnalogVoltage01": cebmajorLowAnalogVoltage01,
       "cebminorHighAnalogVoltage01": cebminorHighAnalogVoltage01,
       "cebminorLowAnalogVoltage01": cebminorLowAnalogVoltage01,
       "cebcurrentValueAnalogVoltage01": cebcurrentValueAnalogVoltage01,
       "cebstateFlagAnalogVoltage01": cebstateFlagAnalogVoltage01,
       "cebminValueAnalogVoltage01": cebminValueAnalogVoltage01,
       "cebmaxValueAnalogVoltage01": cebmaxValueAnalogVoltage01,
       "cebalarmStateAnalogVoltage01": cebalarmStateAnalogVoltage01,
       "ceblabelAnalogVoltage02": ceblabelAnalogVoltage02,
       "cebuomAnalogVoltage02": cebuomAnalogVoltage02,
       "cebmajorHighAnalogVoltage02": cebmajorHighAnalogVoltage02,
       "cebmajorLowAnalogVoltage02": cebmajorLowAnalogVoltage02,
       "cebminorHighAnalogVoltage02": cebminorHighAnalogVoltage02,
       "cebminorLowAnalogVoltage02": cebminorLowAnalogVoltage02,
       "cebcurrentValueAnalogVoltage02": cebcurrentValueAnalogVoltage02,
       "cebstateFlagAnalogVoltage02": cebstateFlagAnalogVoltage02,
       "cebminValueAnalogVoltage02": cebminValueAnalogVoltage02,
       "cebmaxValueAnalogVoltage02": cebmaxValueAnalogVoltage02,
       "cebalarmStateAnalogVoltage02": cebalarmStateAnalogVoltage02,
       "ceblabelAnalogVoltage03": ceblabelAnalogVoltage03,
       "cebuomAnalogVoltage03": cebuomAnalogVoltage03,
       "cebmajorHighAnalogVoltage03": cebmajorHighAnalogVoltage03,
       "cebmajorLowAnalogVoltage03": cebmajorLowAnalogVoltage03,
       "cebminorHighAnalogVoltage03": cebminorHighAnalogVoltage03,
       "cebminorLowAnalogVoltage03": cebminorLowAnalogVoltage03,
       "cebcurrentValueAnalogVoltage03": cebcurrentValueAnalogVoltage03,
       "cebstateFlagAnalogVoltage03": cebstateFlagAnalogVoltage03,
       "cebminValueAnalogVoltage03": cebminValueAnalogVoltage03,
       "cebmaxValueAnalogVoltage03": cebmaxValueAnalogVoltage03,
       "cebalarmStateAnalogVoltage03": cebalarmStateAnalogVoltage03,
       "ceblabelAnalogVoltage04": ceblabelAnalogVoltage04,
       "cebuomAnalogVoltage04": cebuomAnalogVoltage04,
       "cebmajorHighAnalogVoltage04": cebmajorHighAnalogVoltage04,
       "cebmajorLowAnalogVoltage04": cebmajorLowAnalogVoltage04,
       "cebminorHighAnalogVoltage04": cebminorHighAnalogVoltage04,
       "cebminorLowAnalogVoltage04": cebminorLowAnalogVoltage04,
       "cebcurrentValueAnalogVoltage04": cebcurrentValueAnalogVoltage04,
       "cebstateFlagAnalogVoltage04": cebstateFlagAnalogVoltage04,
       "cebminValueAnalogVoltage04": cebminValueAnalogVoltage04,
       "cebmaxValueAnalogVoltage04": cebmaxValueAnalogVoltage04,
       "cebalarmStateAnalogVoltage04": cebalarmStateAnalogVoltage04,
       "ceblabelAnalogVoltage05": ceblabelAnalogVoltage05,
       "cebuomAnalogVoltage05": cebuomAnalogVoltage05,
       "cebmajorHighAnalogVoltage05": cebmajorHighAnalogVoltage05,
       "cebmajorLowAnalogVoltage05": cebmajorLowAnalogVoltage05,
       "cebminorHighAnalogVoltage05": cebminorHighAnalogVoltage05,
       "cebminorLowAnalogVoltage05": cebminorLowAnalogVoltage05,
       "cebcurrentValueAnalogVoltage05": cebcurrentValueAnalogVoltage05,
       "cebstateFlagAnalogVoltage05": cebstateFlagAnalogVoltage05,
       "cebminValueAnalogVoltage05": cebminValueAnalogVoltage05,
       "cebmaxValueAnalogVoltage05": cebmaxValueAnalogVoltage05,
       "cebalarmStateAnalogVoltage05": cebalarmStateAnalogVoltage05,
       "gx2CEBStatusTable": gx2CEBStatusTable,
       "gx2CEBStatusEntry": gx2CEBStatusEntry,
       "gx2CEBStatusTableIndex": gx2CEBStatusTableIndex,
       "ceblabelBoot": ceblabelBoot,
       "cebvalueBoot": cebvalueBoot,
       "cebstateflagBoot": cebstateflagBoot,
       "ceblabelFlash": ceblabelFlash,
       "cebvalueFlash": cebvalueFlash,
       "cebstateflagFlash": cebstateflagFlash,
       "ceblabelFactoryDataCRC": ceblabelFactoryDataCRC,
       "cebvalueFactoryDataCRC": cebvalueFactoryDataCRC,
       "cebstateflagFactoryDataCRC": cebstateflagFactoryDataCRC,
       "ceblabelAlarmDataCrc": ceblabelAlarmDataCrc,
       "cebvalueAlarmDataCrc": cebvalueAlarmDataCrc,
       "cebstateflagAlarmDataCrc": cebstateflagAlarmDataCrc,
       "gx2CEBFactoryTable": gx2CEBFactoryTable,
       "gx2CEBFactoryEntry": gx2CEBFactoryEntry,
       "gx2CEBFactoryTableIndex": gx2CEBFactoryTableIndex,
       "cebbootControlByte": cebbootControlByte,
       "cebbootStatusByte": cebbootStatusByte,
       "cebbank1CRC": cebbank1CRC,
       "cebbank2CRC": cebbank2CRC,
       "cebprgEEPROMByte": cebprgEEPROMByte,
       "cebfactoryCRC": cebfactoryCRC,
       "cebcalculateCRC": cebcalculateCRC,
       "cebhourMeter": cebhourMeter,
       "cebflashPrgCntA": cebflashPrgCntA,
       "cebflashPrgCntB": cebflashPrgCntB,
       "cebflashBankARev": cebflashBankARev,
       "cebflashBankBRev": cebflashBankBRev}
)
