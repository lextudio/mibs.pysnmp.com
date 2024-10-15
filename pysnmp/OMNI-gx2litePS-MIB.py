# SNMP MIB module (OMNI-gx2litePS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2litePS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:40 2024
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

(gx2Liteps,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Liteps")

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

_Gx2LitepsDescriptor_ObjectIdentity = ObjectIdentity
gx2LitepsDescriptor = _Gx2LitepsDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 1)
)
_Gx2LitepsAnalogTable_Object = MibTable
gx2LitepsAnalogTable = _Gx2LitepsAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2)
)
if mibBuilder.loadTexts:
    gx2LitepsAnalogTable.setStatus("mandatory")
_Gx2LitepsAnalogEntry_Object = MibTableRow
gx2LitepsAnalogEntry = _Gx2LitepsAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1)
)
gx2LitepsAnalogEntry.setIndexNames(
    (0, "OMNI-gx2litePS-MIB", "gx2LitepsAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2LitepsAnalogEntry.setStatus("mandatory")


class _Gx2LitepsAnalogTableIndex_Type(Integer32):
    """Custom type gx2LitepsAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2LitepsAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2LitepsAnalogTableIndex_Object = MibTableColumn
gx2LitepsAnalogTableIndex = _Gx2LitepsAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 1),
    _Gx2LitepsAnalogTableIndex_Type()
)
gx2LitepsAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2LitepsAnalogTableIndex.setStatus("mandatory")


class _Litepslabel12Volt_Type(DisplayString):
    """Custom type litepslabel12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Litepslabel12Volt_Type.__name__ = "DisplayString"
_Litepslabel12Volt_Object = MibTableColumn
litepslabel12Volt = _Litepslabel12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 2),
    _Litepslabel12Volt_Type()
)
litepslabel12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepslabel12Volt.setStatus("optional")


class _Litepsuom12Volt_Type(DisplayString):
    """Custom type litepsuom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Litepsuom12Volt_Type.__name__ = "DisplayString"
_Litepsuom12Volt_Object = MibTableColumn
litepsuom12Volt = _Litepsuom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 3),
    _Litepsuom12Volt_Type()
)
litepsuom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsuom12Volt.setStatus("optional")
_LitepsmajorHigh12Volt_Type = Float
_LitepsmajorHigh12Volt_Object = MibTableColumn
litepsmajorHigh12Volt = _LitepsmajorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 4),
    _LitepsmajorHigh12Volt_Type()
)
litepsmajorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsmajorHigh12Volt.setStatus("mandatory")
_LitepsmajorLow12Volt_Type = Float
_LitepsmajorLow12Volt_Object = MibTableColumn
litepsmajorLow12Volt = _LitepsmajorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 5),
    _LitepsmajorLow12Volt_Type()
)
litepsmajorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsmajorLow12Volt.setStatus("mandatory")
_LitepsminorHigh12Volt_Type = Float
_LitepsminorHigh12Volt_Object = MibTableColumn
litepsminorHigh12Volt = _LitepsminorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 6),
    _LitepsminorHigh12Volt_Type()
)
litepsminorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsminorHigh12Volt.setStatus("mandatory")
_LitepsminorLow12Volt_Type = Float
_LitepsminorLow12Volt_Object = MibTableColumn
litepsminorLow12Volt = _LitepsminorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 7),
    _LitepsminorLow12Volt_Type()
)
litepsminorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsminorLow12Volt.setStatus("mandatory")
_LitepscurrentValue12Volt_Type = Float
_LitepscurrentValue12Volt_Object = MibTableColumn
litepscurrentValue12Volt = _LitepscurrentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 8),
    _LitepscurrentValue12Volt_Type()
)
litepscurrentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepscurrentValue12Volt.setStatus("mandatory")


class _LitepsstateFlag12Volt_Type(Integer32):
    """Custom type litepsstateFlag12Volt based on Integer32"""
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


_LitepsstateFlag12Volt_Type.__name__ = "Integer32"
_LitepsstateFlag12Volt_Object = MibTableColumn
litepsstateFlag12Volt = _LitepsstateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 9),
    _LitepsstateFlag12Volt_Type()
)
litepsstateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsstateFlag12Volt.setStatus("mandatory")
_LitepsminValue12Volt_Type = Float
_LitepsminValue12Volt_Object = MibTableColumn
litepsminValue12Volt = _LitepsminValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 10),
    _LitepsminValue12Volt_Type()
)
litepsminValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsminValue12Volt.setStatus("mandatory")
_LitepsmaxValue12Volt_Type = Float
_LitepsmaxValue12Volt_Object = MibTableColumn
litepsmaxValue12Volt = _LitepsmaxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 11),
    _LitepsmaxValue12Volt_Type()
)
litepsmaxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsmaxValue12Volt.setStatus("mandatory")


class _LitepsalarmState12Volt_Type(Integer32):
    """Custom type litepsalarmState12Volt based on Integer32"""
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


_LitepsalarmState12Volt_Type.__name__ = "Integer32"
_LitepsalarmState12Volt_Object = MibTableColumn
litepsalarmState12Volt = _LitepsalarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 12),
    _LitepsalarmState12Volt_Type()
)
litepsalarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsalarmState12Volt.setStatus("mandatory")


class _Litepslabel5Volt_Type(DisplayString):
    """Custom type litepslabel5Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Litepslabel5Volt_Type.__name__ = "DisplayString"
_Litepslabel5Volt_Object = MibTableColumn
litepslabel5Volt = _Litepslabel5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 13),
    _Litepslabel5Volt_Type()
)
litepslabel5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepslabel5Volt.setStatus("optional")


class _Litepsuom5Volt_Type(DisplayString):
    """Custom type litepsuom5Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Litepsuom5Volt_Type.__name__ = "DisplayString"
_Litepsuom5Volt_Object = MibTableColumn
litepsuom5Volt = _Litepsuom5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 14),
    _Litepsuom5Volt_Type()
)
litepsuom5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsuom5Volt.setStatus("optional")
_LitepsmajorHigh5Volt_Type = Float
_LitepsmajorHigh5Volt_Object = MibTableColumn
litepsmajorHigh5Volt = _LitepsmajorHigh5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 15),
    _LitepsmajorHigh5Volt_Type()
)
litepsmajorHigh5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsmajorHigh5Volt.setStatus("mandatory")
_LitepsmajorLow5Volt_Type = Float
_LitepsmajorLow5Volt_Object = MibTableColumn
litepsmajorLow5Volt = _LitepsmajorLow5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 16),
    _LitepsmajorLow5Volt_Type()
)
litepsmajorLow5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsmajorLow5Volt.setStatus("mandatory")
_LitepsminorHigh5Volt_Type = Float
_LitepsminorHigh5Volt_Object = MibTableColumn
litepsminorHigh5Volt = _LitepsminorHigh5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 17),
    _LitepsminorHigh5Volt_Type()
)
litepsminorHigh5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsminorHigh5Volt.setStatus("mandatory")
_LitepsminorLow5Volt_Type = Float
_LitepsminorLow5Volt_Object = MibTableColumn
litepsminorLow5Volt = _LitepsminorLow5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 18),
    _LitepsminorLow5Volt_Type()
)
litepsminorLow5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsminorLow5Volt.setStatus("mandatory")
_LitepscurrentValue5Volt_Type = Float
_LitepscurrentValue5Volt_Object = MibTableColumn
litepscurrentValue5Volt = _LitepscurrentValue5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 19),
    _LitepscurrentValue5Volt_Type()
)
litepscurrentValue5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepscurrentValue5Volt.setStatus("mandatory")


class _LitepsstateFlag5Volt_Type(Integer32):
    """Custom type litepsstateFlag5Volt based on Integer32"""
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


_LitepsstateFlag5Volt_Type.__name__ = "Integer32"
_LitepsstateFlag5Volt_Object = MibTableColumn
litepsstateFlag5Volt = _LitepsstateFlag5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 20),
    _LitepsstateFlag5Volt_Type()
)
litepsstateFlag5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsstateFlag5Volt.setStatus("mandatory")
_LitepsminValue5Volt_Type = Float
_LitepsminValue5Volt_Object = MibTableColumn
litepsminValue5Volt = _LitepsminValue5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 21),
    _LitepsminValue5Volt_Type()
)
litepsminValue5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsminValue5Volt.setStatus("mandatory")
_LitepsmaxValue5Volt_Type = Float
_LitepsmaxValue5Volt_Object = MibTableColumn
litepsmaxValue5Volt = _LitepsmaxValue5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 22),
    _LitepsmaxValue5Volt_Type()
)
litepsmaxValue5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsmaxValue5Volt.setStatus("mandatory")


class _LitepsalarmState5Volt_Type(Integer32):
    """Custom type litepsalarmState5Volt based on Integer32"""
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


_LitepsalarmState5Volt_Type.__name__ = "Integer32"
_LitepsalarmState5Volt_Object = MibTableColumn
litepsalarmState5Volt = _LitepsalarmState5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 23),
    _LitepsalarmState5Volt_Type()
)
litepsalarmState5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsalarmState5Volt.setStatus("mandatory")


class _Litepslabel3Volt_Type(DisplayString):
    """Custom type litepslabel3Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Litepslabel3Volt_Type.__name__ = "DisplayString"
_Litepslabel3Volt_Object = MibTableColumn
litepslabel3Volt = _Litepslabel3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 24),
    _Litepslabel3Volt_Type()
)
litepslabel3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepslabel3Volt.setStatus("optional")


class _Litepsuom3Volt_Type(DisplayString):
    """Custom type litepsuom3Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Litepsuom3Volt_Type.__name__ = "DisplayString"
_Litepsuom3Volt_Object = MibTableColumn
litepsuom3Volt = _Litepsuom3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 25),
    _Litepsuom3Volt_Type()
)
litepsuom3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsuom3Volt.setStatus("optional")
_LitepsmajorHigh3Volt_Type = Float
_LitepsmajorHigh3Volt_Object = MibTableColumn
litepsmajorHigh3Volt = _LitepsmajorHigh3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 26),
    _LitepsmajorHigh3Volt_Type()
)
litepsmajorHigh3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsmajorHigh3Volt.setStatus("mandatory")
_LitepsmajorLow3Volt_Type = Float
_LitepsmajorLow3Volt_Object = MibTableColumn
litepsmajorLow3Volt = _LitepsmajorLow3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 27),
    _LitepsmajorLow3Volt_Type()
)
litepsmajorLow3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsmajorLow3Volt.setStatus("mandatory")
_LitepsminorHigh3Volt_Type = Float
_LitepsminorHigh3Volt_Object = MibTableColumn
litepsminorHigh3Volt = _LitepsminorHigh3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 28),
    _LitepsminorHigh3Volt_Type()
)
litepsminorHigh3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsminorHigh3Volt.setStatus("mandatory")
_LitepsminorLow3Volt_Type = Float
_LitepsminorLow3Volt_Object = MibTableColumn
litepsminorLow3Volt = _LitepsminorLow3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 29),
    _LitepsminorLow3Volt_Type()
)
litepsminorLow3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsminorLow3Volt.setStatus("mandatory")
_LitepscurrentValue3Volt_Type = Float
_LitepscurrentValue3Volt_Object = MibTableColumn
litepscurrentValue3Volt = _LitepscurrentValue3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 30),
    _LitepscurrentValue3Volt_Type()
)
litepscurrentValue3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepscurrentValue3Volt.setStatus("mandatory")


class _LitepsstateFlag3Volt_Type(Integer32):
    """Custom type litepsstateFlag3Volt based on Integer32"""
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


_LitepsstateFlag3Volt_Type.__name__ = "Integer32"
_LitepsstateFlag3Volt_Object = MibTableColumn
litepsstateFlag3Volt = _LitepsstateFlag3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 31),
    _LitepsstateFlag3Volt_Type()
)
litepsstateFlag3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsstateFlag3Volt.setStatus("mandatory")
_LitepsminValue3Volt_Type = Float
_LitepsminValue3Volt_Object = MibTableColumn
litepsminValue3Volt = _LitepsminValue3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 32),
    _LitepsminValue3Volt_Type()
)
litepsminValue3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsminValue3Volt.setStatus("mandatory")
_LitepsmaxValue3Volt_Type = Float
_LitepsmaxValue3Volt_Object = MibTableColumn
litepsmaxValue3Volt = _LitepsmaxValue3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 33),
    _LitepsmaxValue3Volt_Type()
)
litepsmaxValue3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsmaxValue3Volt.setStatus("mandatory")


class _LitepsalarmState3Volt_Type(Integer32):
    """Custom type litepsalarmState3Volt based on Integer32"""
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


_LitepsalarmState3Volt_Type.__name__ = "Integer32"
_LitepsalarmState3Volt_Object = MibTableColumn
litepsalarmState3Volt = _LitepsalarmState3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 2, 1, 34),
    _LitepsalarmState3Volt_Type()
)
litepsalarmState3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsalarmState3Volt.setStatus("mandatory")
_Gx2LitepsStatusTable_Object = MibTable
gx2LitepsStatusTable = _Gx2LitepsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 3)
)
if mibBuilder.loadTexts:
    gx2LitepsStatusTable.setStatus("mandatory")
_Gx2LitepsStatusEntry_Object = MibTableRow
gx2LitepsStatusEntry = _Gx2LitepsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 3, 2)
)
gx2LitepsStatusEntry.setIndexNames(
    (0, "OMNI-gx2litePS-MIB", "gx2LitepsStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2LitepsStatusEntry.setStatus("mandatory")


class _Gx2LitepsStatusTableIndex_Type(Integer32):
    """Custom type gx2LitepsStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2LitepsStatusTableIndex_Type.__name__ = "Integer32"
_Gx2LitepsStatusTableIndex_Object = MibTableColumn
gx2LitepsStatusTableIndex = _Gx2LitepsStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 3, 2, 1),
    _Gx2LitepsStatusTableIndex_Type()
)
gx2LitepsStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2LitepsStatusTableIndex.setStatus("mandatory")


class _LitepslabelFan1Status_Type(DisplayString):
    """Custom type litepslabelFan1Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LitepslabelFan1Status_Type.__name__ = "DisplayString"
_LitepslabelFan1Status_Object = MibTableColumn
litepslabelFan1Status = _LitepslabelFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 3, 2, 2),
    _LitepslabelFan1Status_Type()
)
litepslabelFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepslabelFan1Status.setStatus("optional")


class _LitepsvalueFan1Status_Type(Integer32):
    """Custom type litepsvalueFan1Status based on Integer32"""
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


_LitepsvalueFan1Status_Type.__name__ = "Integer32"
_LitepsvalueFan1Status_Object = MibTableColumn
litepsvalueFan1Status = _LitepsvalueFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 3, 2, 3),
    _LitepsvalueFan1Status_Type()
)
litepsvalueFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsvalueFan1Status.setStatus("mandatory")


class _LitepsstateflagFan1Status_Type(Integer32):
    """Custom type litepsstateflagFan1Status based on Integer32"""
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


_LitepsstateflagFan1Status_Type.__name__ = "Integer32"
_LitepsstateflagFan1Status_Object = MibTableColumn
litepsstateflagFan1Status = _LitepsstateflagFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 3, 2, 4),
    _LitepsstateflagFan1Status_Type()
)
litepsstateflagFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsstateflagFan1Status.setStatus("mandatory")


class _LitepslabelFan2Status_Type(DisplayString):
    """Custom type litepslabelFan2Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LitepslabelFan2Status_Type.__name__ = "DisplayString"
_LitepslabelFan2Status_Object = MibTableColumn
litepslabelFan2Status = _LitepslabelFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 3, 2, 5),
    _LitepslabelFan2Status_Type()
)
litepslabelFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepslabelFan2Status.setStatus("optional")


class _LitepsvalueFan2Status_Type(Integer32):
    """Custom type litepsvalueFan2Status based on Integer32"""
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


_LitepsvalueFan2Status_Type.__name__ = "Integer32"
_LitepsvalueFan2Status_Object = MibTableColumn
litepsvalueFan2Status = _LitepsvalueFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 3, 2, 6),
    _LitepsvalueFan2Status_Type()
)
litepsvalueFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsvalueFan2Status.setStatus("mandatory")


class _LitepsstateflagFan2Status_Type(Integer32):
    """Custom type litepsstateflagFan2Status based on Integer32"""
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


_LitepsstateflagFan2Status_Type.__name__ = "Integer32"
_LitepsstateflagFan2Status_Object = MibTableColumn
litepsstateflagFan2Status = _LitepsstateflagFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 3, 2, 7),
    _LitepsstateflagFan2Status_Type()
)
litepsstateflagFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    litepsstateflagFan2Status.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapLitepsConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 0, 1)
)
trapLitepsConfigChangeInteger.setObjects(
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
    trapLitepsConfigChangeInteger.setStatus(
        ""
    )

trapLitepsConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 0, 2)
)
trapLitepsConfigChangeDisplayString.setObjects(
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
    trapLitepsConfigChangeDisplayString.setStatus(
        ""
    )

trapLitepsFanCurrent1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 0, 3)
)
trapLitepsFanCurrent1.setObjects(
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
    trapLitepsFanCurrent1.setStatus(
        ""
    )

trapLitepsFanCurrent2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 0, 4)
)
trapLitepsFanCurrent2.setObjects(
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
    trapLitepsFanCurrent2.setStatus(
        ""
    )

trapLiteps12Volt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 0, 5)
)
trapLiteps12Volt.setObjects(
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
    trapLiteps12Volt.setStatus(
        ""
    )

trapLiteps5Volt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 0, 6)
)
trapLiteps5Volt.setObjects(
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
    trapLiteps5Volt.setStatus(
        ""
    )

trapLiteps3Volt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23, 0, 7)
)
trapLiteps3Volt.setObjects(
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
    trapLiteps3Volt.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2litePS-MIB",
    **{"Float": Float,
       "trapLitepsConfigChangeInteger": trapLitepsConfigChangeInteger,
       "trapLitepsConfigChangeDisplayString": trapLitepsConfigChangeDisplayString,
       "trapLitepsFanCurrent1": trapLitepsFanCurrent1,
       "trapLitepsFanCurrent2": trapLitepsFanCurrent2,
       "trapLiteps12Volt": trapLiteps12Volt,
       "trapLiteps5Volt": trapLiteps5Volt,
       "trapLiteps3Volt": trapLiteps3Volt,
       "gx2LitepsDescriptor": gx2LitepsDescriptor,
       "gx2LitepsAnalogTable": gx2LitepsAnalogTable,
       "gx2LitepsAnalogEntry": gx2LitepsAnalogEntry,
       "gx2LitepsAnalogTableIndex": gx2LitepsAnalogTableIndex,
       "litepslabel12Volt": litepslabel12Volt,
       "litepsuom12Volt": litepsuom12Volt,
       "litepsmajorHigh12Volt": litepsmajorHigh12Volt,
       "litepsmajorLow12Volt": litepsmajorLow12Volt,
       "litepsminorHigh12Volt": litepsminorHigh12Volt,
       "litepsminorLow12Volt": litepsminorLow12Volt,
       "litepscurrentValue12Volt": litepscurrentValue12Volt,
       "litepsstateFlag12Volt": litepsstateFlag12Volt,
       "litepsminValue12Volt": litepsminValue12Volt,
       "litepsmaxValue12Volt": litepsmaxValue12Volt,
       "litepsalarmState12Volt": litepsalarmState12Volt,
       "litepslabel5Volt": litepslabel5Volt,
       "litepsuom5Volt": litepsuom5Volt,
       "litepsmajorHigh5Volt": litepsmajorHigh5Volt,
       "litepsmajorLow5Volt": litepsmajorLow5Volt,
       "litepsminorHigh5Volt": litepsminorHigh5Volt,
       "litepsminorLow5Volt": litepsminorLow5Volt,
       "litepscurrentValue5Volt": litepscurrentValue5Volt,
       "litepsstateFlag5Volt": litepsstateFlag5Volt,
       "litepsminValue5Volt": litepsminValue5Volt,
       "litepsmaxValue5Volt": litepsmaxValue5Volt,
       "litepsalarmState5Volt": litepsalarmState5Volt,
       "litepslabel3Volt": litepslabel3Volt,
       "litepsuom3Volt": litepsuom3Volt,
       "litepsmajorHigh3Volt": litepsmajorHigh3Volt,
       "litepsmajorLow3Volt": litepsmajorLow3Volt,
       "litepsminorHigh3Volt": litepsminorHigh3Volt,
       "litepsminorLow3Volt": litepsminorLow3Volt,
       "litepscurrentValue3Volt": litepscurrentValue3Volt,
       "litepsstateFlag3Volt": litepsstateFlag3Volt,
       "litepsminValue3Volt": litepsminValue3Volt,
       "litepsmaxValue3Volt": litepsmaxValue3Volt,
       "litepsalarmState3Volt": litepsalarmState3Volt,
       "gx2LitepsStatusTable": gx2LitepsStatusTable,
       "gx2LitepsStatusEntry": gx2LitepsStatusEntry,
       "gx2LitepsStatusTableIndex": gx2LitepsStatusTableIndex,
       "litepslabelFan1Status": litepslabelFan1Status,
       "litepsvalueFan1Status": litepsvalueFan1Status,
       "litepsstateflagFan1Status": litepsstateflagFan1Status,
       "litepslabelFan2Status": litepslabelFan2Status,
       "litepsvalueFan2Status": litepsvalueFan2Status,
       "litepsstateflagFan2Status": litepsstateflagFan2Status}
)
