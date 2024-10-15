# SNMP MIB module (OMNI-gx2PSDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2PSDC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:29 2024
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

(gx2Psdc,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Psdc")

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

_Gx2PsdcDescriptor_ObjectIdentity = ObjectIdentity
gx2PsdcDescriptor = _Gx2PsdcDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 1)
)
_Gx2PsdcAnalogTable_Object = MibTable
gx2PsdcAnalogTable = _Gx2PsdcAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    gx2PsdcAnalogTable.setStatus("mandatory")
_Gx2PsdcAnalogEntry_Object = MibTableRow
gx2PsdcAnalogEntry = _Gx2PsdcAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1)
)
gx2PsdcAnalogEntry.setIndexNames(
    (0, "OMNI-gx2PSDC-MIB", "gx2PsdcAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2PsdcAnalogEntry.setStatus("mandatory")


class _Gx2PsdcAnalogTableIndex_Type(Integer32):
    """Custom type gx2PsdcAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2PsdcAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2PsdcAnalogTableIndex_Object = MibTableColumn
gx2PsdcAnalogTableIndex = _Gx2PsdcAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 1),
    _Gx2PsdcAnalogTableIndex_Type()
)
gx2PsdcAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2PsdcAnalogTableIndex.setStatus("mandatory")


class _PslabelFanCurrent_Type(DisplayString):
    """Custom type pslabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PslabelFanCurrent_Type.__name__ = "DisplayString"
_PslabelFanCurrent_Object = MibTableColumn
pslabelFanCurrent = _PslabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 2),
    _PslabelFanCurrent_Type()
)
pslabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabelFanCurrent.setStatus("optional")


class _PsuomFanCurrent_Type(DisplayString):
    """Custom type psuomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PsuomFanCurrent_Type.__name__ = "DisplayString"
_PsuomFanCurrent_Object = MibTableColumn
psuomFanCurrent = _PsuomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 3),
    _PsuomFanCurrent_Type()
)
psuomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuomFanCurrent.setStatus("optional")
_PsmajorHighFanCurrent_Type = Float
_PsmajorHighFanCurrent_Object = MibTableColumn
psmajorHighFanCurrent = _PsmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 4),
    _PsmajorHighFanCurrent_Type()
)
psmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorHighFanCurrent.setStatus("mandatory")
_PsmajorLowFanCurrent_Type = Float
_PsmajorLowFanCurrent_Object = MibTableColumn
psmajorLowFanCurrent = _PsmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 5),
    _PsmajorLowFanCurrent_Type()
)
psmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorLowFanCurrent.setStatus("mandatory")
_PsminorHighFanCurrent_Type = Float
_PsminorHighFanCurrent_Object = MibTableColumn
psminorHighFanCurrent = _PsminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 6),
    _PsminorHighFanCurrent_Type()
)
psminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorHighFanCurrent.setStatus("mandatory")
_PsminorLowFanCurrent_Type = Float
_PsminorLowFanCurrent_Object = MibTableColumn
psminorLowFanCurrent = _PsminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 7),
    _PsminorLowFanCurrent_Type()
)
psminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorLowFanCurrent.setStatus("mandatory")
_PscurrentValueFanCurrent_Type = Float
_PscurrentValueFanCurrent_Object = MibTableColumn
pscurrentValueFanCurrent = _PscurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 8),
    _PscurrentValueFanCurrent_Type()
)
pscurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscurrentValueFanCurrent.setStatus("mandatory")


class _PsstateFlagFanCurrent_Type(Integer32):
    """Custom type psstateFlagFanCurrent based on Integer32"""
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


_PsstateFlagFanCurrent_Type.__name__ = "Integer32"
_PsstateFlagFanCurrent_Object = MibTableColumn
psstateFlagFanCurrent = _PsstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 9),
    _PsstateFlagFanCurrent_Type()
)
psstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateFlagFanCurrent.setStatus("mandatory")
_PsminValueFanCurrent_Type = Float
_PsminValueFanCurrent_Object = MibTableColumn
psminValueFanCurrent = _PsminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 10),
    _PsminValueFanCurrent_Type()
)
psminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminValueFanCurrent.setStatus("mandatory")
_PsmaxValueFanCurrent_Type = Float
_PsmaxValueFanCurrent_Object = MibTableColumn
psmaxValueFanCurrent = _PsmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 11),
    _PsmaxValueFanCurrent_Type()
)
psmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmaxValueFanCurrent.setStatus("mandatory")


class _PsalarmStateFanCurrent_Type(Integer32):
    """Custom type psalarmStateFanCurrent based on Integer32"""
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


_PsalarmStateFanCurrent_Type.__name__ = "Integer32"
_PsalarmStateFanCurrent_Object = MibTableColumn
psalarmStateFanCurrent = _PsalarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 12),
    _PsalarmStateFanCurrent_Type()
)
psalarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psalarmStateFanCurrent.setStatus("mandatory")


class _Pslabel12Volt_Type(DisplayString):
    """Custom type pslabel12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Pslabel12Volt_Type.__name__ = "DisplayString"
_Pslabel12Volt_Object = MibTableColumn
pslabel12Volt = _Pslabel12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 13),
    _Pslabel12Volt_Type()
)
pslabel12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabel12Volt.setStatus("optional")


class _Psuom12Volt_Type(DisplayString):
    """Custom type psuom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Psuom12Volt_Type.__name__ = "DisplayString"
_Psuom12Volt_Object = MibTableColumn
psuom12Volt = _Psuom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 14),
    _Psuom12Volt_Type()
)
psuom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuom12Volt.setStatus("optional")
_PsmajorHigh12Volt_Type = Float
_PsmajorHigh12Volt_Object = MibTableColumn
psmajorHigh12Volt = _PsmajorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 15),
    _PsmajorHigh12Volt_Type()
)
psmajorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorHigh12Volt.setStatus("mandatory")
_PsmajorLow12Volt_Type = Float
_PsmajorLow12Volt_Object = MibTableColumn
psmajorLow12Volt = _PsmajorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 16),
    _PsmajorLow12Volt_Type()
)
psmajorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorLow12Volt.setStatus("mandatory")
_PsminorHigh12Volt_Type = Float
_PsminorHigh12Volt_Object = MibTableColumn
psminorHigh12Volt = _PsminorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 17),
    _PsminorHigh12Volt_Type()
)
psminorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorHigh12Volt.setStatus("mandatory")
_PsminorLow12Volt_Type = Float
_PsminorLow12Volt_Object = MibTableColumn
psminorLow12Volt = _PsminorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 18),
    _PsminorLow12Volt_Type()
)
psminorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorLow12Volt.setStatus("mandatory")
_PscurrentValue12Volt_Type = Float
_PscurrentValue12Volt_Object = MibTableColumn
pscurrentValue12Volt = _PscurrentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 19),
    _PscurrentValue12Volt_Type()
)
pscurrentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscurrentValue12Volt.setStatus("mandatory")


class _PsstateFlag12Volt_Type(Integer32):
    """Custom type psstateFlag12Volt based on Integer32"""
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


_PsstateFlag12Volt_Type.__name__ = "Integer32"
_PsstateFlag12Volt_Object = MibTableColumn
psstateFlag12Volt = _PsstateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 20),
    _PsstateFlag12Volt_Type()
)
psstateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateFlag12Volt.setStatus("mandatory")
_PsminValue12Volt_Type = Float
_PsminValue12Volt_Object = MibTableColumn
psminValue12Volt = _PsminValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 21),
    _PsminValue12Volt_Type()
)
psminValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminValue12Volt.setStatus("mandatory")
_PsmaxValue12Volt_Type = Float
_PsmaxValue12Volt_Object = MibTableColumn
psmaxValue12Volt = _PsmaxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 22),
    _PsmaxValue12Volt_Type()
)
psmaxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmaxValue12Volt.setStatus("mandatory")


class _PsalarmState12Volt_Type(Integer32):
    """Custom type psalarmState12Volt based on Integer32"""
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


_PsalarmState12Volt_Type.__name__ = "Integer32"
_PsalarmState12Volt_Object = MibTableColumn
psalarmState12Volt = _PsalarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 23),
    _PsalarmState12Volt_Type()
)
psalarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psalarmState12Volt.setStatus("mandatory")


class _Pslabel5Volt_Type(DisplayString):
    """Custom type pslabel5Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Pslabel5Volt_Type.__name__ = "DisplayString"
_Pslabel5Volt_Object = MibTableColumn
pslabel5Volt = _Pslabel5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 24),
    _Pslabel5Volt_Type()
)
pslabel5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabel5Volt.setStatus("optional")


class _Psuom5Volt_Type(DisplayString):
    """Custom type psuom5Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Psuom5Volt_Type.__name__ = "DisplayString"
_Psuom5Volt_Object = MibTableColumn
psuom5Volt = _Psuom5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 25),
    _Psuom5Volt_Type()
)
psuom5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuom5Volt.setStatus("optional")
_PsmajorHigh5Volt_Type = Float
_PsmajorHigh5Volt_Object = MibTableColumn
psmajorHigh5Volt = _PsmajorHigh5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 26),
    _PsmajorHigh5Volt_Type()
)
psmajorHigh5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorHigh5Volt.setStatus("mandatory")
_PsmajorLow5Volt_Type = Float
_PsmajorLow5Volt_Object = MibTableColumn
psmajorLow5Volt = _PsmajorLow5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 27),
    _PsmajorLow5Volt_Type()
)
psmajorLow5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorLow5Volt.setStatus("mandatory")
_PsminorHigh5Volt_Type = Float
_PsminorHigh5Volt_Object = MibTableColumn
psminorHigh5Volt = _PsminorHigh5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 28),
    _PsminorHigh5Volt_Type()
)
psminorHigh5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorHigh5Volt.setStatus("mandatory")
_PsminorLow5Volt_Type = Float
_PsminorLow5Volt_Object = MibTableColumn
psminorLow5Volt = _PsminorLow5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 29),
    _PsminorLow5Volt_Type()
)
psminorLow5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorLow5Volt.setStatus("mandatory")
_PscurrentValue5Volt_Type = Float
_PscurrentValue5Volt_Object = MibTableColumn
pscurrentValue5Volt = _PscurrentValue5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 30),
    _PscurrentValue5Volt_Type()
)
pscurrentValue5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscurrentValue5Volt.setStatus("mandatory")


class _PsstateFlag5Volt_Type(Integer32):
    """Custom type psstateFlag5Volt based on Integer32"""
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


_PsstateFlag5Volt_Type.__name__ = "Integer32"
_PsstateFlag5Volt_Object = MibTableColumn
psstateFlag5Volt = _PsstateFlag5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 31),
    _PsstateFlag5Volt_Type()
)
psstateFlag5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateFlag5Volt.setStatus("mandatory")
_PsminValue5Volt_Type = Float
_PsminValue5Volt_Object = MibTableColumn
psminValue5Volt = _PsminValue5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 32),
    _PsminValue5Volt_Type()
)
psminValue5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminValue5Volt.setStatus("mandatory")
_PsmaxValue5Volt_Type = Float
_PsmaxValue5Volt_Object = MibTableColumn
psmaxValue5Volt = _PsmaxValue5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 33),
    _PsmaxValue5Volt_Type()
)
psmaxValue5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmaxValue5Volt.setStatus("mandatory")


class _PsalarmState5Volt_Type(Integer32):
    """Custom type psalarmState5Volt based on Integer32"""
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


_PsalarmState5Volt_Type.__name__ = "Integer32"
_PsalarmState5Volt_Object = MibTableColumn
psalarmState5Volt = _PsalarmState5Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 34),
    _PsalarmState5Volt_Type()
)
psalarmState5Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psalarmState5Volt.setStatus("mandatory")


class _Pslabel3Volt_Type(DisplayString):
    """Custom type pslabel3Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Pslabel3Volt_Type.__name__ = "DisplayString"
_Pslabel3Volt_Object = MibTableColumn
pslabel3Volt = _Pslabel3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 35),
    _Pslabel3Volt_Type()
)
pslabel3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabel3Volt.setStatus("optional")


class _Psuom3Volt_Type(DisplayString):
    """Custom type psuom3Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Psuom3Volt_Type.__name__ = "DisplayString"
_Psuom3Volt_Object = MibTableColumn
psuom3Volt = _Psuom3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 36),
    _Psuom3Volt_Type()
)
psuom3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuom3Volt.setStatus("optional")
_PsmajorHigh3Volt_Type = Float
_PsmajorHigh3Volt_Object = MibTableColumn
psmajorHigh3Volt = _PsmajorHigh3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 37),
    _PsmajorHigh3Volt_Type()
)
psmajorHigh3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorHigh3Volt.setStatus("mandatory")
_PsmajorLow3Volt_Type = Float
_PsmajorLow3Volt_Object = MibTableColumn
psmajorLow3Volt = _PsmajorLow3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 38),
    _PsmajorLow3Volt_Type()
)
psmajorLow3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorLow3Volt.setStatus("mandatory")
_PsminorHigh3Volt_Type = Float
_PsminorHigh3Volt_Object = MibTableColumn
psminorHigh3Volt = _PsminorHigh3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 39),
    _PsminorHigh3Volt_Type()
)
psminorHigh3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorHigh3Volt.setStatus("mandatory")
_PsminorLow3Volt_Type = Float
_PsminorLow3Volt_Object = MibTableColumn
psminorLow3Volt = _PsminorLow3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 40),
    _PsminorLow3Volt_Type()
)
psminorLow3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorLow3Volt.setStatus("mandatory")
_PscurrentValue3Volt_Type = Float
_PscurrentValue3Volt_Object = MibTableColumn
pscurrentValue3Volt = _PscurrentValue3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 41),
    _PscurrentValue3Volt_Type()
)
pscurrentValue3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscurrentValue3Volt.setStatus("mandatory")


class _PsstateFlag3Volt_Type(Integer32):
    """Custom type psstateFlag3Volt based on Integer32"""
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


_PsstateFlag3Volt_Type.__name__ = "Integer32"
_PsstateFlag3Volt_Object = MibTableColumn
psstateFlag3Volt = _PsstateFlag3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 42),
    _PsstateFlag3Volt_Type()
)
psstateFlag3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateFlag3Volt.setStatus("mandatory")
_PsminValue3Volt_Type = Float
_PsminValue3Volt_Object = MibTableColumn
psminValue3Volt = _PsminValue3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 43),
    _PsminValue3Volt_Type()
)
psminValue3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminValue3Volt.setStatus("mandatory")
_PsmaxValue3Volt_Type = Float
_PsmaxValue3Volt_Object = MibTableColumn
psmaxValue3Volt = _PsmaxValue3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 44),
    _PsmaxValue3Volt_Type()
)
psmaxValue3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmaxValue3Volt.setStatus("mandatory")


class _PsalarmState3Volt_Type(Integer32):
    """Custom type psalarmState3Volt based on Integer32"""
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


_PsalarmState3Volt_Type.__name__ = "Integer32"
_PsalarmState3Volt_Object = MibTableColumn
psalarmState3Volt = _PsalarmState3Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 45),
    _PsalarmState3Volt_Type()
)
psalarmState3Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psalarmState3Volt.setStatus("mandatory")


class _PslabelAmbientTemp_Type(DisplayString):
    """Custom type pslabelAmbientTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PslabelAmbientTemp_Type.__name__ = "DisplayString"
_PslabelAmbientTemp_Object = MibTableColumn
pslabelAmbientTemp = _PslabelAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 46),
    _PslabelAmbientTemp_Type()
)
pslabelAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabelAmbientTemp.setStatus("optional")


class _PsuomAmbientTemp_Type(DisplayString):
    """Custom type psuomAmbientTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PsuomAmbientTemp_Type.__name__ = "DisplayString"
_PsuomAmbientTemp_Object = MibTableColumn
psuomAmbientTemp = _PsuomAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 47),
    _PsuomAmbientTemp_Type()
)
psuomAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuomAmbientTemp.setStatus("optional")
_PsmajorHighAmbientTemp_Type = Float
_PsmajorHighAmbientTemp_Object = MibTableColumn
psmajorHighAmbientTemp = _PsmajorHighAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 48),
    _PsmajorHighAmbientTemp_Type()
)
psmajorHighAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorHighAmbientTemp.setStatus("mandatory")
_PsmajorLowAmbientTemp_Type = Float
_PsmajorLowAmbientTemp_Object = MibTableColumn
psmajorLowAmbientTemp = _PsmajorLowAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 49),
    _PsmajorLowAmbientTemp_Type()
)
psmajorLowAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorLowAmbientTemp.setStatus("mandatory")
_PsminorHighAmbientTemp_Type = Float
_PsminorHighAmbientTemp_Object = MibTableColumn
psminorHighAmbientTemp = _PsminorHighAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 50),
    _PsminorHighAmbientTemp_Type()
)
psminorHighAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorHighAmbientTemp.setStatus("mandatory")
_PsminorLowAmbientTemp_Type = Float
_PsminorLowAmbientTemp_Object = MibTableColumn
psminorLowAmbientTemp = _PsminorLowAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 51),
    _PsminorLowAmbientTemp_Type()
)
psminorLowAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorLowAmbientTemp.setStatus("mandatory")
_PscurrentValueAmbientTemp_Type = Float
_PscurrentValueAmbientTemp_Object = MibTableColumn
pscurrentValueAmbientTemp = _PscurrentValueAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 52),
    _PscurrentValueAmbientTemp_Type()
)
pscurrentValueAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscurrentValueAmbientTemp.setStatus("mandatory")


class _PsstateFlagAmbientTemp_Type(Integer32):
    """Custom type psstateFlagAmbientTemp based on Integer32"""
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


_PsstateFlagAmbientTemp_Type.__name__ = "Integer32"
_PsstateFlagAmbientTemp_Object = MibTableColumn
psstateFlagAmbientTemp = _PsstateFlagAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 53),
    _PsstateFlagAmbientTemp_Type()
)
psstateFlagAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateFlagAmbientTemp.setStatus("mandatory")
_PsminValueAmbientTemp_Type = Float
_PsminValueAmbientTemp_Object = MibTableColumn
psminValueAmbientTemp = _PsminValueAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 54),
    _PsminValueAmbientTemp_Type()
)
psminValueAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminValueAmbientTemp.setStatus("mandatory")
_PsmaxValueAmbientTemp_Type = Float
_PsmaxValueAmbientTemp_Object = MibTableColumn
psmaxValueAmbientTemp = _PsmaxValueAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 55),
    _PsmaxValueAmbientTemp_Type()
)
psmaxValueAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmaxValueAmbientTemp.setStatus("mandatory")


class _PsalarmStateAmbientTemp_Type(Integer32):
    """Custom type psalarmStateAmbientTemp based on Integer32"""
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


_PsalarmStateAmbientTemp_Type.__name__ = "Integer32"
_PsalarmStateAmbientTemp_Object = MibTableColumn
psalarmStateAmbientTemp = _PsalarmStateAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 56),
    _PsalarmStateAmbientTemp_Type()
)
psalarmStateAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psalarmStateAmbientTemp.setStatus("mandatory")


class _PslabelMainTemp_Type(DisplayString):
    """Custom type pslabelMainTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PslabelMainTemp_Type.__name__ = "DisplayString"
_PslabelMainTemp_Object = MibTableColumn
pslabelMainTemp = _PslabelMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 57),
    _PslabelMainTemp_Type()
)
pslabelMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabelMainTemp.setStatus("optional")


class _PsuomMainTemp_Type(DisplayString):
    """Custom type psuomMainTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PsuomMainTemp_Type.__name__ = "DisplayString"
_PsuomMainTemp_Object = MibTableColumn
psuomMainTemp = _PsuomMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 58),
    _PsuomMainTemp_Type()
)
psuomMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuomMainTemp.setStatus("optional")
_PsmajorHighMainTemp_Type = Float
_PsmajorHighMainTemp_Object = MibTableColumn
psmajorHighMainTemp = _PsmajorHighMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 59),
    _PsmajorHighMainTemp_Type()
)
psmajorHighMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorHighMainTemp.setStatus("mandatory")
_PsmajorLowMainTemp_Type = Float
_PsmajorLowMainTemp_Object = MibTableColumn
psmajorLowMainTemp = _PsmajorLowMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 60),
    _PsmajorLowMainTemp_Type()
)
psmajorLowMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorLowMainTemp.setStatus("mandatory")
_PsminorHighMainTemp_Type = Float
_PsminorHighMainTemp_Object = MibTableColumn
psminorHighMainTemp = _PsminorHighMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 61),
    _PsminorHighMainTemp_Type()
)
psminorHighMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorHighMainTemp.setStatus("mandatory")
_PsminorLowMainTemp_Type = Float
_PsminorLowMainTemp_Object = MibTableColumn
psminorLowMainTemp = _PsminorLowMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 62),
    _PsminorLowMainTemp_Type()
)
psminorLowMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorLowMainTemp.setStatus("mandatory")
_PscurrentValueMainTemp_Type = Float
_PscurrentValueMainTemp_Object = MibTableColumn
pscurrentValueMainTemp = _PscurrentValueMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 63),
    _PscurrentValueMainTemp_Type()
)
pscurrentValueMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscurrentValueMainTemp.setStatus("mandatory")


class _PsstateFlagMainTemp_Type(Integer32):
    """Custom type psstateFlagMainTemp based on Integer32"""
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


_PsstateFlagMainTemp_Type.__name__ = "Integer32"
_PsstateFlagMainTemp_Object = MibTableColumn
psstateFlagMainTemp = _PsstateFlagMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 64),
    _PsstateFlagMainTemp_Type()
)
psstateFlagMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateFlagMainTemp.setStatus("mandatory")
_PsminValueMainTemp_Type = Float
_PsminValueMainTemp_Object = MibTableColumn
psminValueMainTemp = _PsminValueMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 65),
    _PsminValueMainTemp_Type()
)
psminValueMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminValueMainTemp.setStatus("mandatory")
_PsmaxValueMainTemp_Type = Float
_PsmaxValueMainTemp_Object = MibTableColumn
psmaxValueMainTemp = _PsmaxValueMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 66),
    _PsmaxValueMainTemp_Type()
)
psmaxValueMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmaxValueMainTemp.setStatus("mandatory")


class _PsalarmStateMainTemp_Type(Integer32):
    """Custom type psalarmStateMainTemp based on Integer32"""
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


_PsalarmStateMainTemp_Type.__name__ = "Integer32"
_PsalarmStateMainTemp_Object = MibTableColumn
psalarmStateMainTemp = _PsalarmStateMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 67),
    _PsalarmStateMainTemp_Type()
)
psalarmStateMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psalarmStateMainTemp.setStatus("mandatory")


class _Pslabel12AnodeVolt_Type(DisplayString):
    """Custom type pslabel12AnodeVolt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Pslabel12AnodeVolt_Type.__name__ = "DisplayString"
_Pslabel12AnodeVolt_Object = MibTableColumn
pslabel12AnodeVolt = _Pslabel12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 68),
    _Pslabel12AnodeVolt_Type()
)
pslabel12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabel12AnodeVolt.setStatus("optional")


class _Psuom12AnodeVolt_Type(DisplayString):
    """Custom type psuom12AnodeVolt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Psuom12AnodeVolt_Type.__name__ = "DisplayString"
_Psuom12AnodeVolt_Object = MibTableColumn
psuom12AnodeVolt = _Psuom12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 69),
    _Psuom12AnodeVolt_Type()
)
psuom12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuom12AnodeVolt.setStatus("optional")
_PsmajorHigh12AnodeVolt_Type = Float
_PsmajorHigh12AnodeVolt_Object = MibTableColumn
psmajorHigh12AnodeVolt = _PsmajorHigh12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 70),
    _PsmajorHigh12AnodeVolt_Type()
)
psmajorHigh12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorHigh12AnodeVolt.setStatus("mandatory")
_PsmajorLow12AnodeVolt_Type = Float
_PsmajorLow12AnodeVolt_Object = MibTableColumn
psmajorLow12AnodeVolt = _PsmajorLow12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 71),
    _PsmajorLow12AnodeVolt_Type()
)
psmajorLow12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorLow12AnodeVolt.setStatus("mandatory")
_PsminorHigh12AnodeVolt_Type = Float
_PsminorHigh12AnodeVolt_Object = MibTableColumn
psminorHigh12AnodeVolt = _PsminorHigh12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 72),
    _PsminorHigh12AnodeVolt_Type()
)
psminorHigh12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorHigh12AnodeVolt.setStatus("mandatory")
_PsminorLow12AnodeVolt_Type = Float
_PsminorLow12AnodeVolt_Object = MibTableColumn
psminorLow12AnodeVolt = _PsminorLow12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 73),
    _PsminorLow12AnodeVolt_Type()
)
psminorLow12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorLow12AnodeVolt.setStatus("mandatory")
_PscurrentValue12AnodeVolt_Type = Float
_PscurrentValue12AnodeVolt_Object = MibTableColumn
pscurrentValue12AnodeVolt = _PscurrentValue12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 74),
    _PscurrentValue12AnodeVolt_Type()
)
pscurrentValue12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscurrentValue12AnodeVolt.setStatus("mandatory")


class _PsstateFlag12AnodeVolt_Type(Integer32):
    """Custom type psstateFlag12AnodeVolt based on Integer32"""
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


_PsstateFlag12AnodeVolt_Type.__name__ = "Integer32"
_PsstateFlag12AnodeVolt_Object = MibTableColumn
psstateFlag12AnodeVolt = _PsstateFlag12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 75),
    _PsstateFlag12AnodeVolt_Type()
)
psstateFlag12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateFlag12AnodeVolt.setStatus("mandatory")
_PsminValue12AnodeVolt_Type = Float
_PsminValue12AnodeVolt_Object = MibTableColumn
psminValue12AnodeVolt = _PsminValue12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 76),
    _PsminValue12AnodeVolt_Type()
)
psminValue12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminValue12AnodeVolt.setStatus("mandatory")
_PsmaxValue12AnodeVolt_Type = Float
_PsmaxValue12AnodeVolt_Object = MibTableColumn
psmaxValue12AnodeVolt = _PsmaxValue12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 77),
    _PsmaxValue12AnodeVolt_Type()
)
psmaxValue12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmaxValue12AnodeVolt.setStatus("mandatory")


class _PsalarmState12AnodeVolt_Type(Integer32):
    """Custom type psalarmState12AnodeVolt based on Integer32"""
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


_PsalarmState12AnodeVolt_Type.__name__ = "Integer32"
_PsalarmState12AnodeVolt_Object = MibTableColumn
psalarmState12AnodeVolt = _PsalarmState12AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 78),
    _PsalarmState12AnodeVolt_Type()
)
psalarmState12AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psalarmState12AnodeVolt.setStatus("mandatory")


class _Pslabel5AnodeVolt_Type(DisplayString):
    """Custom type pslabel5AnodeVolt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Pslabel5AnodeVolt_Type.__name__ = "DisplayString"
_Pslabel5AnodeVolt_Object = MibTableColumn
pslabel5AnodeVolt = _Pslabel5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 79),
    _Pslabel5AnodeVolt_Type()
)
pslabel5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabel5AnodeVolt.setStatus("optional")


class _Psuom5AnodeVolt_Type(DisplayString):
    """Custom type psuom5AnodeVolt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Psuom5AnodeVolt_Type.__name__ = "DisplayString"
_Psuom5AnodeVolt_Object = MibTableColumn
psuom5AnodeVolt = _Psuom5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 80),
    _Psuom5AnodeVolt_Type()
)
psuom5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuom5AnodeVolt.setStatus("optional")
_PsmajorHigh5AnodeVolt_Type = Float
_PsmajorHigh5AnodeVolt_Object = MibTableColumn
psmajorHigh5AnodeVolt = _PsmajorHigh5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 81),
    _PsmajorHigh5AnodeVolt_Type()
)
psmajorHigh5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorHigh5AnodeVolt.setStatus("mandatory")
_PsmajorLow5AnodeVolt_Type = Float
_PsmajorLow5AnodeVolt_Object = MibTableColumn
psmajorLow5AnodeVolt = _PsmajorLow5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 82),
    _PsmajorLow5AnodeVolt_Type()
)
psmajorLow5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorLow5AnodeVolt.setStatus("mandatory")
_PsminorHigh5AnodeVolt_Type = Float
_PsminorHigh5AnodeVolt_Object = MibTableColumn
psminorHigh5AnodeVolt = _PsminorHigh5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 83),
    _PsminorHigh5AnodeVolt_Type()
)
psminorHigh5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorHigh5AnodeVolt.setStatus("mandatory")
_PsminorLow5AnodeVolt_Type = Float
_PsminorLow5AnodeVolt_Object = MibTableColumn
psminorLow5AnodeVolt = _PsminorLow5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 84),
    _PsminorLow5AnodeVolt_Type()
)
psminorLow5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorLow5AnodeVolt.setStatus("mandatory")
_PscurrentValue5AnodeVolt_Type = Float
_PscurrentValue5AnodeVolt_Object = MibTableColumn
pscurrentValue5AnodeVolt = _PscurrentValue5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 85),
    _PscurrentValue5AnodeVolt_Type()
)
pscurrentValue5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscurrentValue5AnodeVolt.setStatus("mandatory")


class _PsstateFlag5AnodeVolt_Type(Integer32):
    """Custom type psstateFlag5AnodeVolt based on Integer32"""
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


_PsstateFlag5AnodeVolt_Type.__name__ = "Integer32"
_PsstateFlag5AnodeVolt_Object = MibTableColumn
psstateFlag5AnodeVolt = _PsstateFlag5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 86),
    _PsstateFlag5AnodeVolt_Type()
)
psstateFlag5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateFlag5AnodeVolt.setStatus("mandatory")
_PsminValue5AnodeVolt_Type = Float
_PsminValue5AnodeVolt_Object = MibTableColumn
psminValue5AnodeVolt = _PsminValue5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 87),
    _PsminValue5AnodeVolt_Type()
)
psminValue5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminValue5AnodeVolt.setStatus("mandatory")
_PsmaxValue5AnodeVolt_Type = Float
_PsmaxValue5AnodeVolt_Object = MibTableColumn
psmaxValue5AnodeVolt = _PsmaxValue5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 88),
    _PsmaxValue5AnodeVolt_Type()
)
psmaxValue5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmaxValue5AnodeVolt.setStatus("mandatory")


class _PsalarmState5AnodeVolt_Type(Integer32):
    """Custom type psalarmState5AnodeVolt based on Integer32"""
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


_PsalarmState5AnodeVolt_Type.__name__ = "Integer32"
_PsalarmState5AnodeVolt_Object = MibTableColumn
psalarmState5AnodeVolt = _PsalarmState5AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 89),
    _PsalarmState5AnodeVolt_Type()
)
psalarmState5AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psalarmState5AnodeVolt.setStatus("mandatory")


class _Pslabel3AnodeVolt_Type(DisplayString):
    """Custom type pslabel3AnodeVolt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Pslabel3AnodeVolt_Type.__name__ = "DisplayString"
_Pslabel3AnodeVolt_Object = MibTableColumn
pslabel3AnodeVolt = _Pslabel3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 90),
    _Pslabel3AnodeVolt_Type()
)
pslabel3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabel3AnodeVolt.setStatus("optional")


class _Psuom3AnodeVolt_Type(DisplayString):
    """Custom type psuom3AnodeVolt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Psuom3AnodeVolt_Type.__name__ = "DisplayString"
_Psuom3AnodeVolt_Object = MibTableColumn
psuom3AnodeVolt = _Psuom3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 91),
    _Psuom3AnodeVolt_Type()
)
psuom3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuom3AnodeVolt.setStatus("optional")
_PsmajorHigh3AnodeVolt_Type = Float
_PsmajorHigh3AnodeVolt_Object = MibTableColumn
psmajorHigh3AnodeVolt = _PsmajorHigh3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 92),
    _PsmajorHigh3AnodeVolt_Type()
)
psmajorHigh3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorHigh3AnodeVolt.setStatus("mandatory")
_PsmajorLow3AnodeVolt_Type = Float
_PsmajorLow3AnodeVolt_Object = MibTableColumn
psmajorLow3AnodeVolt = _PsmajorLow3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 93),
    _PsmajorLow3AnodeVolt_Type()
)
psmajorLow3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmajorLow3AnodeVolt.setStatus("mandatory")
_PsminorHigh3AnodeVolt_Type = Float
_PsminorHigh3AnodeVolt_Object = MibTableColumn
psminorHigh3AnodeVolt = _PsminorHigh3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 94),
    _PsminorHigh3AnodeVolt_Type()
)
psminorHigh3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorHigh3AnodeVolt.setStatus("mandatory")
_PsminorLow3AnodeVolt_Type = Float
_PsminorLow3AnodeVolt_Object = MibTableColumn
psminorLow3AnodeVolt = _PsminorLow3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 95),
    _PsminorLow3AnodeVolt_Type()
)
psminorLow3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminorLow3AnodeVolt.setStatus("mandatory")
_PscurrentValue3AnodeVolt_Type = Float
_PscurrentValue3AnodeVolt_Object = MibTableColumn
pscurrentValue3AnodeVolt = _PscurrentValue3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 96),
    _PscurrentValue3AnodeVolt_Type()
)
pscurrentValue3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscurrentValue3AnodeVolt.setStatus("mandatory")


class _PsstateFlag3AnodeVolt_Type(Integer32):
    """Custom type psstateFlag3AnodeVolt based on Integer32"""
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


_PsstateFlag3AnodeVolt_Type.__name__ = "Integer32"
_PsstateFlag3AnodeVolt_Object = MibTableColumn
psstateFlag3AnodeVolt = _PsstateFlag3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 97),
    _PsstateFlag3AnodeVolt_Type()
)
psstateFlag3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateFlag3AnodeVolt.setStatus("mandatory")
_PsminValue3AnodeVolt_Type = Float
_PsminValue3AnodeVolt_Object = MibTableColumn
psminValue3AnodeVolt = _PsminValue3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 98),
    _PsminValue3AnodeVolt_Type()
)
psminValue3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psminValue3AnodeVolt.setStatus("mandatory")
_PsmaxValue3AnodeVolt_Type = Float
_PsmaxValue3AnodeVolt_Object = MibTableColumn
psmaxValue3AnodeVolt = _PsmaxValue3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 99),
    _PsmaxValue3AnodeVolt_Type()
)
psmaxValue3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmaxValue3AnodeVolt.setStatus("mandatory")


class _PsalarmState3AnodeVolt_Type(Integer32):
    """Custom type psalarmState3AnodeVolt based on Integer32"""
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


_PsalarmState3AnodeVolt_Type.__name__ = "Integer32"
_PsalarmState3AnodeVolt_Object = MibTableColumn
psalarmState3AnodeVolt = _PsalarmState3AnodeVolt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 2, 1, 100),
    _PsalarmState3AnodeVolt_Type()
)
psalarmState3AnodeVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psalarmState3AnodeVolt.setStatus("mandatory")
_Gx2PsdcStatusTable_Object = MibTable
gx2PsdcStatusTable = _Gx2PsdcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    gx2PsdcStatusTable.setStatus("mandatory")
_Gx2PsdcStatusEntry_Object = MibTableRow
gx2PsdcStatusEntry = _Gx2PsdcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2)
)
gx2PsdcStatusEntry.setIndexNames(
    (0, "OMNI-gx2PSDC-MIB", "gx2PsdcStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2PsdcStatusEntry.setStatus("mandatory")


class _Gx2PsdcStatusTableIndex_Type(Integer32):
    """Custom type gx2PsdcStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2PsdcStatusTableIndex_Type.__name__ = "Integer32"
_Gx2PsdcStatusTableIndex_Object = MibTableColumn
gx2PsdcStatusTableIndex = _Gx2PsdcStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 1),
    _Gx2PsdcStatusTableIndex_Type()
)
gx2PsdcStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2PsdcStatusTableIndex.setStatus("mandatory")


class _PslabelBoot_Type(DisplayString):
    """Custom type pslabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PslabelBoot_Type.__name__ = "DisplayString"
_PslabelBoot_Object = MibTableColumn
pslabelBoot = _PslabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 2),
    _PslabelBoot_Type()
)
pslabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabelBoot.setStatus("optional")


class _PsvalueBoot_Type(Integer32):
    """Custom type psvalueBoot based on Integer32"""
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


_PsvalueBoot_Type.__name__ = "Integer32"
_PsvalueBoot_Object = MibTableColumn
psvalueBoot = _PsvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 3),
    _PsvalueBoot_Type()
)
psvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psvalueBoot.setStatus("mandatory")


class _PsstateflagBoot_Type(Integer32):
    """Custom type psstateflagBoot based on Integer32"""
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


_PsstateflagBoot_Type.__name__ = "Integer32"
_PsstateflagBoot_Object = MibTableColumn
psstateflagBoot = _PsstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 4),
    _PsstateflagBoot_Type()
)
psstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateflagBoot.setStatus("mandatory")


class _PslabelFlash_Type(DisplayString):
    """Custom type pslabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PslabelFlash_Type.__name__ = "DisplayString"
_PslabelFlash_Object = MibTableColumn
pslabelFlash = _PslabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 5),
    _PslabelFlash_Type()
)
pslabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabelFlash.setStatus("optional")


class _PsvalueFlash_Type(Integer32):
    """Custom type psvalueFlash based on Integer32"""
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


_PsvalueFlash_Type.__name__ = "Integer32"
_PsvalueFlash_Object = MibTableColumn
psvalueFlash = _PsvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 6),
    _PsvalueFlash_Type()
)
psvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psvalueFlash.setStatus("mandatory")


class _PsstateflagFlash_Type(Integer32):
    """Custom type psstateflagFlash based on Integer32"""
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


_PsstateflagFlash_Type.__name__ = "Integer32"
_PsstateflagFlash_Object = MibTableColumn
psstateflagFlash = _PsstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 7),
    _PsstateflagFlash_Type()
)
psstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateflagFlash.setStatus("mandatory")


class _PslabelFactoryDataCRC_Type(DisplayString):
    """Custom type pslabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PslabelFactoryDataCRC_Type.__name__ = "DisplayString"
_PslabelFactoryDataCRC_Object = MibTableColumn
pslabelFactoryDataCRC = _PslabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 8),
    _PslabelFactoryDataCRC_Type()
)
pslabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabelFactoryDataCRC.setStatus("optional")


class _PsvalueFactoryDataCRC_Type(Integer32):
    """Custom type psvalueFactoryDataCRC based on Integer32"""
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


_PsvalueFactoryDataCRC_Type.__name__ = "Integer32"
_PsvalueFactoryDataCRC_Object = MibTableColumn
psvalueFactoryDataCRC = _PsvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 9),
    _PsvalueFactoryDataCRC_Type()
)
psvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psvalueFactoryDataCRC.setStatus("mandatory")


class _PsstateflagFactoryDataCRC_Type(Integer32):
    """Custom type psstateflagFactoryDataCRC based on Integer32"""
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


_PsstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_PsstateflagFactoryDataCRC_Object = MibTableColumn
psstateflagFactoryDataCRC = _PsstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 10),
    _PsstateflagFactoryDataCRC_Type()
)
psstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateflagFactoryDataCRC.setStatus("mandatory")


class _PslabelPsdcDataCRC_Type(DisplayString):
    """Custom type pslabelPsdcDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PslabelPsdcDataCRC_Type.__name__ = "DisplayString"
_PslabelPsdcDataCRC_Object = MibTableColumn
pslabelPsdcDataCRC = _PslabelPsdcDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 11),
    _PslabelPsdcDataCRC_Type()
)
pslabelPsdcDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabelPsdcDataCRC.setStatus("optional")


class _PsvaluePsdcDataCRC_Type(Integer32):
    """Custom type psvaluePsdcDataCRC based on Integer32"""
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


_PsvaluePsdcDataCRC_Type.__name__ = "Integer32"
_PsvaluePsdcDataCRC_Object = MibTableColumn
psvaluePsdcDataCRC = _PsvaluePsdcDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 12),
    _PsvaluePsdcDataCRC_Type()
)
psvaluePsdcDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psvaluePsdcDataCRC.setStatus("mandatory")


class _PsstateflagPsdcDataCRC_Type(Integer32):
    """Custom type psstateflagPsdcDataCRC based on Integer32"""
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


_PsstateflagPsdcDataCRC_Type.__name__ = "Integer32"
_PsstateflagPsdcDataCRC_Object = MibTableColumn
psstateflagPsdcDataCRC = _PsstateflagPsdcDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 13),
    _PsstateflagPsdcDataCRC_Type()
)
psstateflagPsdcDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateflagPsdcDataCRC.setStatus("mandatory")


class _PslabelPsdcHwStatus_Type(DisplayString):
    """Custom type pslabelPsdcHwStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PslabelPsdcHwStatus_Type.__name__ = "DisplayString"
_PslabelPsdcHwStatus_Object = MibTableColumn
pslabelPsdcHwStatus = _PslabelPsdcHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 14),
    _PslabelPsdcHwStatus_Type()
)
pslabelPsdcHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pslabelPsdcHwStatus.setStatus("optional")


class _PsvaluePsdcHwStatus_Type(Integer32):
    """Custom type psvaluePsdcHwStatus based on Integer32"""
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


_PsvaluePsdcHwStatus_Type.__name__ = "Integer32"
_PsvaluePsdcHwStatus_Object = MibTableColumn
psvaluePsdcHwStatus = _PsvaluePsdcHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 15),
    _PsvaluePsdcHwStatus_Type()
)
psvaluePsdcHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psvaluePsdcHwStatus.setStatus("mandatory")


class _PsstateflagPsdcHwStatus_Type(Integer32):
    """Custom type psstateflagPsdcHwStatus based on Integer32"""
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


_PsstateflagPsdcHwStatus_Type.__name__ = "Integer32"
_PsstateflagPsdcHwStatus_Object = MibTableColumn
psstateflagPsdcHwStatus = _PsstateflagPsdcHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 3, 2, 16),
    _PsstateflagPsdcHwStatus_Type()
)
psstateflagPsdcHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psstateflagPsdcHwStatus.setStatus("mandatory")
_Gx2PsdcFactoryTable_Object = MibTable
gx2PsdcFactoryTable = _Gx2PsdcFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4)
)
if mibBuilder.loadTexts:
    gx2PsdcFactoryTable.setStatus("mandatory")
_Gx2PsdcFactoryEntry_Object = MibTableRow
gx2PsdcFactoryEntry = _Gx2PsdcFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3)
)
gx2PsdcFactoryEntry.setIndexNames(
    (0, "OMNI-gx2PSDC-MIB", "gx2PsdcFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2PsdcFactoryEntry.setStatus("mandatory")


class _Gx2PsdcFactoryTableIndex_Type(Integer32):
    """Custom type gx2PsdcFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2PsdcFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2PsdcFactoryTableIndex_Object = MibTableColumn
gx2PsdcFactoryTableIndex = _Gx2PsdcFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 1),
    _Gx2PsdcFactoryTableIndex_Type()
)
gx2PsdcFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2PsdcFactoryTableIndex.setStatus("mandatory")
_PsbootControlByteValue_Type = Integer32
_PsbootControlByteValue_Object = MibTableColumn
psbootControlByteValue = _PsbootControlByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 2),
    _PsbootControlByteValue_Type()
)
psbootControlByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbootControlByteValue.setStatus("mandatory")
_PsbootStatusByteValue_Type = Integer32
_PsbootStatusByteValue_Object = MibTableColumn
psbootStatusByteValue = _PsbootStatusByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 3),
    _PsbootStatusByteValue_Type()
)
psbootStatusByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbootStatusByteValue.setStatus("mandatory")
_Psbank1CRCValue_Type = Integer32
_Psbank1CRCValue_Object = MibTableColumn
psbank1CRCValue = _Psbank1CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 4),
    _Psbank1CRCValue_Type()
)
psbank1CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbank1CRCValue.setStatus("mandatory")
_Psbank2CRCValue_Type = Integer32
_Psbank2CRCValue_Object = MibTableColumn
psbank2CRCValue = _Psbank2CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 5),
    _Psbank2CRCValue_Type()
)
psbank2CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psbank2CRCValue.setStatus("mandatory")
_PsprgEEPROMByteValue_Type = Integer32
_PsprgEEPROMByteValue_Object = MibTableColumn
psprgEEPROMByteValue = _PsprgEEPROMByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 6),
    _PsprgEEPROMByteValue_Type()
)
psprgEEPROMByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psprgEEPROMByteValue.setStatus("mandatory")
_PsfactoryCRCValue_Type = Integer32
_PsfactoryCRCValue_Object = MibTableColumn
psfactoryCRCValue = _PsfactoryCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 7),
    _PsfactoryCRCValue_Type()
)
psfactoryCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psfactoryCRCValue.setStatus("mandatory")


class _PscalculateCRCValue_Type(Integer32):
    """Custom type pscalculateCRCValue based on Integer32"""
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


_PscalculateCRCValue_Type.__name__ = "Integer32"
_PscalculateCRCValue_Object = MibTableColumn
pscalculateCRCValue = _PscalculateCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 8),
    _PscalculateCRCValue_Type()
)
pscalculateCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscalculateCRCValue.setStatus("mandatory")
_PshourMeterValue_Type = Integer32
_PshourMeterValue_Object = MibTableColumn
pshourMeterValue = _PshourMeterValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 9),
    _PshourMeterValue_Type()
)
pshourMeterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pshourMeterValue.setStatus("mandatory")
_PsflashPrgCntAValue_Type = Integer32
_PsflashPrgCntAValue_Object = MibTableColumn
psflashPrgCntAValue = _PsflashPrgCntAValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 10),
    _PsflashPrgCntAValue_Type()
)
psflashPrgCntAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psflashPrgCntAValue.setStatus("mandatory")
_PsflashPrgCntBValue_Type = Integer32
_PsflashPrgCntBValue_Object = MibTableColumn
psflashPrgCntBValue = _PsflashPrgCntBValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 11),
    _PsflashPrgCntBValue_Type()
)
psflashPrgCntBValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psflashPrgCntBValue.setStatus("mandatory")


class _PsflashBankARevValue_Type(DisplayString):
    """Custom type psflashBankARevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PsflashBankARevValue_Type.__name__ = "DisplayString"
_PsflashBankARevValue_Object = MibTableColumn
psflashBankARevValue = _PsflashBankARevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 12),
    _PsflashBankARevValue_Type()
)
psflashBankARevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psflashBankARevValue.setStatus("mandatory")


class _PsflashBankBRevValue_Type(DisplayString):
    """Custom type psflashBankBRevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PsflashBankBRevValue_Type.__name__ = "DisplayString"
_PsflashBankBRevValue_Object = MibTableColumn
psflashBankBRevValue = _PsflashBankBRevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 4, 3, 13),
    _PsflashBankBRevValue_Type()
)
psflashBankBRevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psflashBankBRevValue.setStatus("mandatory")
_Gx2PsdcHoldTimeTable_Object = MibTable
gx2PsdcHoldTimeTable = _Gx2PsdcHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 5)
)
if mibBuilder.loadTexts:
    gx2PsdcHoldTimeTable.setStatus("mandatory")
_Gx2PsdcHoldTimeEntry_Object = MibTableRow
gx2PsdcHoldTimeEntry = _Gx2PsdcHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 5, 4)
)
gx2PsdcHoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2PSDC-MIB", "rxgx2PsdcHoldTimeTableIndex"),
    (0, "OMNI-gx2PSDC-MIB", "rxgx2PsdcHoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2PsdcHoldTimeEntry.setStatus("mandatory")


class _Rxgx2PsdcHoldTimeTableIndex_Type(Integer32):
    """Custom type rxgx2PsdcHoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2PsdcHoldTimeTableIndex_Type.__name__ = "Integer32"
_Rxgx2PsdcHoldTimeTableIndex_Object = MibTableColumn
rxgx2PsdcHoldTimeTableIndex = _Rxgx2PsdcHoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 5, 4, 1),
    _Rxgx2PsdcHoldTimeTableIndex_Type()
)
rxgx2PsdcHoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2PsdcHoldTimeTableIndex.setStatus("mandatory")


class _Rxgx2PsdcHoldTimeSpecIndex_Type(Integer32):
    """Custom type rxgx2PsdcHoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2PsdcHoldTimeSpecIndex_Type.__name__ = "Integer32"
_Rxgx2PsdcHoldTimeSpecIndex_Object = MibTableColumn
rxgx2PsdcHoldTimeSpecIndex = _Rxgx2PsdcHoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 5, 4, 2),
    _Rxgx2PsdcHoldTimeSpecIndex_Type()
)
rxgx2PsdcHoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2PsdcHoldTimeSpecIndex.setStatus("mandatory")
_Rxgx2PsdcHoldTimeData_Type = Integer32
_Rxgx2PsdcHoldTimeData_Object = MibTableColumn
rxgx2PsdcHoldTimeData = _Rxgx2PsdcHoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 5, 4, 3),
    _Rxgx2PsdcHoldTimeData_Type()
)
rxgx2PsdcHoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxgx2PsdcHoldTimeData.setStatus("mandatory")
_Gx2PsdcDigitalTable_Object = MibTable
gx2PsdcDigitalTable = _Gx2PsdcDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 6)
)
if mibBuilder.loadTexts:
    gx2PsdcDigitalTable.setStatus("mandatory")
_Gx2PsdcDigitalEntry_Object = MibTableRow
gx2PsdcDigitalEntry = _Gx2PsdcDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 6, 5)
)
gx2PsdcDigitalEntry.setIndexNames(
    (0, "OMNI-gx2PSDC-MIB", "gx2PsdcDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2PsdcDigitalEntry.setStatus("mandatory")


class _Gx2PsdcDigitalTableIndex_Type(Integer32):
    """Custom type gx2PsdcDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2PsdcDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2PsdcDigitalTableIndex_Object = MibTableColumn
gx2PsdcDigitalTableIndex = _Gx2PsdcDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 6, 5, 1),
    _Gx2PsdcDigitalTableIndex_Type()
)
gx2PsdcDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2PsdcDigitalTableIndex.setStatus("mandatory")


class _PsdclabelNVfanAlrm_Type(DisplayString):
    """Custom type psdclabelNVfanAlrm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PsdclabelNVfanAlrm_Type.__name__ = "DisplayString"
_PsdclabelNVfanAlrm_Object = MibTableColumn
psdclabelNVfanAlrm = _PsdclabelNVfanAlrm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 6, 5, 2),
    _PsdclabelNVfanAlrm_Type()
)
psdclabelNVfanAlrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdclabelNVfanAlrm.setStatus("optional")


class _PsdcenumNVfanAlrm_Type(DisplayString):
    """Custom type psdcenumNVfanAlrm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PsdcenumNVfanAlrm_Type.__name__ = "DisplayString"
_PsdcenumNVfanAlrm_Object = MibTableColumn
psdcenumNVfanAlrm = _PsdcenumNVfanAlrm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 6, 5, 3),
    _PsdcenumNVfanAlrm_Type()
)
psdcenumNVfanAlrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdcenumNVfanAlrm.setStatus("optional")


class _PsdcvalueNVfanAlrm_Type(Integer32):
    """Custom type psdcvalueNVfanAlrm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 3),
          ("none", 1),
          ("unacknowledged", 2))
    )


_PsdcvalueNVfanAlrm_Type.__name__ = "Integer32"
_PsdcvalueNVfanAlrm_Object = MibTableColumn
psdcvalueNVfanAlrm = _PsdcvalueNVfanAlrm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 6, 5, 4),
    _PsdcvalueNVfanAlrm_Type()
)
psdcvalueNVfanAlrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psdcvalueNVfanAlrm.setStatus("mandatory")


class _PsdcstateflagNVfanAlrm_Type(Integer32):
    """Custom type psdcstateflagNVfanAlrm based on Integer32"""
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


_PsdcstateflagNVfanAlrm_Type.__name__ = "Integer32"
_PsdcstateflagNVfanAlrm_Object = MibTableColumn
psdcstateflagNVfanAlrm = _PsdcstateflagNVfanAlrm_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 6, 5, 5),
    _PsdcstateflagNVfanAlrm_Type()
)
psdcstateflagNVfanAlrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psdcstateflagNVfanAlrm.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapPSDCConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 1)
)
trapPSDCConfigChangeInteger.setObjects(
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
    trapPSDCConfigChangeInteger.setStatus(
        ""
    )

trapPSDCConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 2)
)
trapPSDCConfigChangeDisplayString.setObjects(
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
    trapPSDCConfigChangeDisplayString.setStatus(
        ""
    )

trapPSDCFanCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 3)
)
trapPSDCFanCurrent.setObjects(
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
    trapPSDCFanCurrent.setStatus(
        ""
    )

trapPSDC12Volt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 4)
)
trapPSDC12Volt.setObjects(
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
    trapPSDC12Volt.setStatus(
        ""
    )

trapPSDC5Volt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 5)
)
trapPSDC5Volt.setObjects(
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
    trapPSDC5Volt.setStatus(
        ""
    )

trapPSDC3Volt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 6)
)
trapPSDC3Volt.setObjects(
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
    trapPSDC3Volt.setStatus(
        ""
    )

trapPSDCAmbientTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 7)
)
trapPSDCAmbientTemp.setObjects(
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
    trapPSDCAmbientTemp.setStatus(
        ""
    )

trapPSDCMainTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 8)
)
trapPSDCMainTemp.setObjects(
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
    trapPSDCMainTemp.setStatus(
        ""
    )

trapPSDC12AnodeVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 9)
)
trapPSDC12AnodeVolt.setObjects(
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
    trapPSDC12AnodeVolt.setStatus(
        ""
    )

trapPSDC5AnodeVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 10)
)
trapPSDC5AnodeVolt.setObjects(
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
    trapPSDC5AnodeVolt.setStatus(
        ""
    )

trapPSDC3AnodeVolt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 11)
)
trapPSDC3AnodeVolt.setObjects(
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
    trapPSDC3AnodeVolt.setStatus(
        ""
    )

trapPSDCEEChksmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 12)
)
trapPSDCEEChksmAlarm.setObjects(
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
    trapPSDCEEChksmAlarm.setStatus(
        ""
    )

trapPSDCFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 13)
)
trapPSDCFlashAlarm.setObjects(
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
    trapPSDCFlashAlarm.setStatus(
        ""
    )

trapPSDCBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 14)
)
trapPSDCBootAlarm.setObjects(
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
    trapPSDCBootAlarm.setStatus(
        ""
    )

trapPSDCAlarmReportingStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 15)
)
trapPSDCAlarmReportingStatus.setObjects(
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
    trapPSDCAlarmReportingStatus.setStatus(
        ""
    )

trapPSbrickType = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 16)
)
trapPSbrickType.setObjects(
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
    trapPSbrickType.setStatus(
        ""
    )

trapPSsupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 17)
)
trapPSsupplyFailure.setObjects(
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
    trapPSsupplyFailure.setStatus(
        ""
    )

trapPSDCALARMChksmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7, 0, 18)
)
trapPSDCALARMChksmAlarm.setObjects(
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
    trapPSDCALARMChksmAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2PSDC-MIB",
    **{"Float": Float,
       "trapPSDCConfigChangeInteger": trapPSDCConfigChangeInteger,
       "trapPSDCConfigChangeDisplayString": trapPSDCConfigChangeDisplayString,
       "trapPSDCFanCurrent": trapPSDCFanCurrent,
       "trapPSDC12Volt": trapPSDC12Volt,
       "trapPSDC5Volt": trapPSDC5Volt,
       "trapPSDC3Volt": trapPSDC3Volt,
       "trapPSDCAmbientTemp": trapPSDCAmbientTemp,
       "trapPSDCMainTemp": trapPSDCMainTemp,
       "trapPSDC12AnodeVolt": trapPSDC12AnodeVolt,
       "trapPSDC5AnodeVolt": trapPSDC5AnodeVolt,
       "trapPSDC3AnodeVolt": trapPSDC3AnodeVolt,
       "trapPSDCEEChksmAlarm": trapPSDCEEChksmAlarm,
       "trapPSDCFlashAlarm": trapPSDCFlashAlarm,
       "trapPSDCBootAlarm": trapPSDCBootAlarm,
       "trapPSDCAlarmReportingStatus": trapPSDCAlarmReportingStatus,
       "trapPSbrickType": trapPSbrickType,
       "trapPSsupplyFailure": trapPSsupplyFailure,
       "trapPSDCALARMChksmAlarm": trapPSDCALARMChksmAlarm,
       "gx2PsdcDescriptor": gx2PsdcDescriptor,
       "gx2PsdcAnalogTable": gx2PsdcAnalogTable,
       "gx2PsdcAnalogEntry": gx2PsdcAnalogEntry,
       "gx2PsdcAnalogTableIndex": gx2PsdcAnalogTableIndex,
       "pslabelFanCurrent": pslabelFanCurrent,
       "psuomFanCurrent": psuomFanCurrent,
       "psmajorHighFanCurrent": psmajorHighFanCurrent,
       "psmajorLowFanCurrent": psmajorLowFanCurrent,
       "psminorHighFanCurrent": psminorHighFanCurrent,
       "psminorLowFanCurrent": psminorLowFanCurrent,
       "pscurrentValueFanCurrent": pscurrentValueFanCurrent,
       "psstateFlagFanCurrent": psstateFlagFanCurrent,
       "psminValueFanCurrent": psminValueFanCurrent,
       "psmaxValueFanCurrent": psmaxValueFanCurrent,
       "psalarmStateFanCurrent": psalarmStateFanCurrent,
       "pslabel12Volt": pslabel12Volt,
       "psuom12Volt": psuom12Volt,
       "psmajorHigh12Volt": psmajorHigh12Volt,
       "psmajorLow12Volt": psmajorLow12Volt,
       "psminorHigh12Volt": psminorHigh12Volt,
       "psminorLow12Volt": psminorLow12Volt,
       "pscurrentValue12Volt": pscurrentValue12Volt,
       "psstateFlag12Volt": psstateFlag12Volt,
       "psminValue12Volt": psminValue12Volt,
       "psmaxValue12Volt": psmaxValue12Volt,
       "psalarmState12Volt": psalarmState12Volt,
       "pslabel5Volt": pslabel5Volt,
       "psuom5Volt": psuom5Volt,
       "psmajorHigh5Volt": psmajorHigh5Volt,
       "psmajorLow5Volt": psmajorLow5Volt,
       "psminorHigh5Volt": psminorHigh5Volt,
       "psminorLow5Volt": psminorLow5Volt,
       "pscurrentValue5Volt": pscurrentValue5Volt,
       "psstateFlag5Volt": psstateFlag5Volt,
       "psminValue5Volt": psminValue5Volt,
       "psmaxValue5Volt": psmaxValue5Volt,
       "psalarmState5Volt": psalarmState5Volt,
       "pslabel3Volt": pslabel3Volt,
       "psuom3Volt": psuom3Volt,
       "psmajorHigh3Volt": psmajorHigh3Volt,
       "psmajorLow3Volt": psmajorLow3Volt,
       "psminorHigh3Volt": psminorHigh3Volt,
       "psminorLow3Volt": psminorLow3Volt,
       "pscurrentValue3Volt": pscurrentValue3Volt,
       "psstateFlag3Volt": psstateFlag3Volt,
       "psminValue3Volt": psminValue3Volt,
       "psmaxValue3Volt": psmaxValue3Volt,
       "psalarmState3Volt": psalarmState3Volt,
       "pslabelAmbientTemp": pslabelAmbientTemp,
       "psuomAmbientTemp": psuomAmbientTemp,
       "psmajorHighAmbientTemp": psmajorHighAmbientTemp,
       "psmajorLowAmbientTemp": psmajorLowAmbientTemp,
       "psminorHighAmbientTemp": psminorHighAmbientTemp,
       "psminorLowAmbientTemp": psminorLowAmbientTemp,
       "pscurrentValueAmbientTemp": pscurrentValueAmbientTemp,
       "psstateFlagAmbientTemp": psstateFlagAmbientTemp,
       "psminValueAmbientTemp": psminValueAmbientTemp,
       "psmaxValueAmbientTemp": psmaxValueAmbientTemp,
       "psalarmStateAmbientTemp": psalarmStateAmbientTemp,
       "pslabelMainTemp": pslabelMainTemp,
       "psuomMainTemp": psuomMainTemp,
       "psmajorHighMainTemp": psmajorHighMainTemp,
       "psmajorLowMainTemp": psmajorLowMainTemp,
       "psminorHighMainTemp": psminorHighMainTemp,
       "psminorLowMainTemp": psminorLowMainTemp,
       "pscurrentValueMainTemp": pscurrentValueMainTemp,
       "psstateFlagMainTemp": psstateFlagMainTemp,
       "psminValueMainTemp": psminValueMainTemp,
       "psmaxValueMainTemp": psmaxValueMainTemp,
       "psalarmStateMainTemp": psalarmStateMainTemp,
       "pslabel12AnodeVolt": pslabel12AnodeVolt,
       "psuom12AnodeVolt": psuom12AnodeVolt,
       "psmajorHigh12AnodeVolt": psmajorHigh12AnodeVolt,
       "psmajorLow12AnodeVolt": psmajorLow12AnodeVolt,
       "psminorHigh12AnodeVolt": psminorHigh12AnodeVolt,
       "psminorLow12AnodeVolt": psminorLow12AnodeVolt,
       "pscurrentValue12AnodeVolt": pscurrentValue12AnodeVolt,
       "psstateFlag12AnodeVolt": psstateFlag12AnodeVolt,
       "psminValue12AnodeVolt": psminValue12AnodeVolt,
       "psmaxValue12AnodeVolt": psmaxValue12AnodeVolt,
       "psalarmState12AnodeVolt": psalarmState12AnodeVolt,
       "pslabel5AnodeVolt": pslabel5AnodeVolt,
       "psuom5AnodeVolt": psuom5AnodeVolt,
       "psmajorHigh5AnodeVolt": psmajorHigh5AnodeVolt,
       "psmajorLow5AnodeVolt": psmajorLow5AnodeVolt,
       "psminorHigh5AnodeVolt": psminorHigh5AnodeVolt,
       "psminorLow5AnodeVolt": psminorLow5AnodeVolt,
       "pscurrentValue5AnodeVolt": pscurrentValue5AnodeVolt,
       "psstateFlag5AnodeVolt": psstateFlag5AnodeVolt,
       "psminValue5AnodeVolt": psminValue5AnodeVolt,
       "psmaxValue5AnodeVolt": psmaxValue5AnodeVolt,
       "psalarmState5AnodeVolt": psalarmState5AnodeVolt,
       "pslabel3AnodeVolt": pslabel3AnodeVolt,
       "psuom3AnodeVolt": psuom3AnodeVolt,
       "psmajorHigh3AnodeVolt": psmajorHigh3AnodeVolt,
       "psmajorLow3AnodeVolt": psmajorLow3AnodeVolt,
       "psminorHigh3AnodeVolt": psminorHigh3AnodeVolt,
       "psminorLow3AnodeVolt": psminorLow3AnodeVolt,
       "pscurrentValue3AnodeVolt": pscurrentValue3AnodeVolt,
       "psstateFlag3AnodeVolt": psstateFlag3AnodeVolt,
       "psminValue3AnodeVolt": psminValue3AnodeVolt,
       "psmaxValue3AnodeVolt": psmaxValue3AnodeVolt,
       "psalarmState3AnodeVolt": psalarmState3AnodeVolt,
       "gx2PsdcStatusTable": gx2PsdcStatusTable,
       "gx2PsdcStatusEntry": gx2PsdcStatusEntry,
       "gx2PsdcStatusTableIndex": gx2PsdcStatusTableIndex,
       "pslabelBoot": pslabelBoot,
       "psvalueBoot": psvalueBoot,
       "psstateflagBoot": psstateflagBoot,
       "pslabelFlash": pslabelFlash,
       "psvalueFlash": psvalueFlash,
       "psstateflagFlash": psstateflagFlash,
       "pslabelFactoryDataCRC": pslabelFactoryDataCRC,
       "psvalueFactoryDataCRC": psvalueFactoryDataCRC,
       "psstateflagFactoryDataCRC": psstateflagFactoryDataCRC,
       "pslabelPsdcDataCRC": pslabelPsdcDataCRC,
       "psvaluePsdcDataCRC": psvaluePsdcDataCRC,
       "psstateflagPsdcDataCRC": psstateflagPsdcDataCRC,
       "pslabelPsdcHwStatus": pslabelPsdcHwStatus,
       "psvaluePsdcHwStatus": psvaluePsdcHwStatus,
       "psstateflagPsdcHwStatus": psstateflagPsdcHwStatus,
       "gx2PsdcFactoryTable": gx2PsdcFactoryTable,
       "gx2PsdcFactoryEntry": gx2PsdcFactoryEntry,
       "gx2PsdcFactoryTableIndex": gx2PsdcFactoryTableIndex,
       "psbootControlByteValue": psbootControlByteValue,
       "psbootStatusByteValue": psbootStatusByteValue,
       "psbank1CRCValue": psbank1CRCValue,
       "psbank2CRCValue": psbank2CRCValue,
       "psprgEEPROMByteValue": psprgEEPROMByteValue,
       "psfactoryCRCValue": psfactoryCRCValue,
       "pscalculateCRCValue": pscalculateCRCValue,
       "pshourMeterValue": pshourMeterValue,
       "psflashPrgCntAValue": psflashPrgCntAValue,
       "psflashPrgCntBValue": psflashPrgCntBValue,
       "psflashBankARevValue": psflashBankARevValue,
       "psflashBankBRevValue": psflashBankBRevValue,
       "gx2PsdcHoldTimeTable": gx2PsdcHoldTimeTable,
       "gx2PsdcHoldTimeEntry": gx2PsdcHoldTimeEntry,
       "rxgx2PsdcHoldTimeTableIndex": rxgx2PsdcHoldTimeTableIndex,
       "rxgx2PsdcHoldTimeSpecIndex": rxgx2PsdcHoldTimeSpecIndex,
       "rxgx2PsdcHoldTimeData": rxgx2PsdcHoldTimeData,
       "gx2PsdcDigitalTable": gx2PsdcDigitalTable,
       "gx2PsdcDigitalEntry": gx2PsdcDigitalEntry,
       "gx2PsdcDigitalTableIndex": gx2PsdcDigitalTableIndex,
       "psdclabelNVfanAlrm": psdclabelNVfanAlrm,
       "psdcenumNVfanAlrm": psdcenumNVfanAlrm,
       "psdcvalueNVfanAlrm": psdcvalueNVfanAlrm,
       "psdcstateflagNVfanAlrm": psdcstateflagNVfanAlrm}
)
