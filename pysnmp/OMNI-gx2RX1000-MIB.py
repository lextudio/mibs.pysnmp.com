# SNMP MIB module (OMNI-gx2RX1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2RX1000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:33 2024
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

(gx2Rx1000,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Rx1000")

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

_Gx2Rx1000Descriptor_ObjectIdentity = ObjectIdentity
gx2Rx1000Descriptor = _Gx2Rx1000Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 1)
)
_Gx2Rx1000AnalogTable_Object = MibTable
gx2Rx1000AnalogTable = _Gx2Rx1000AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    gx2Rx1000AnalogTable.setStatus("mandatory")
_Gx2Rx1000AnalogEntry_Object = MibTableRow
gx2Rx1000AnalogEntry = _Gx2Rx1000AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1)
)
gx2Rx1000AnalogEntry.setIndexNames(
    (0, "OMNI-gx2RX1000-MIB", "fprgx2Rx1000AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx1000AnalogEntry.setStatus("mandatory")


class _Fprgx2Rx1000AnalogTableIndex_Type(Integer32):
    """Custom type fprgx2Rx1000AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Fprgx2Rx1000AnalogTableIndex_Type.__name__ = "Integer32"
_Fprgx2Rx1000AnalogTableIndex_Object = MibTableColumn
fprgx2Rx1000AnalogTableIndex = _Fprgx2Rx1000AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 1),
    _Fprgx2Rx1000AnalogTableIndex_Type()
)
fprgx2Rx1000AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprgx2Rx1000AnalogTableIndex.setStatus("mandatory")


class _FprlabelOptPower_Type(DisplayString):
    """Custom type fprlabelOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelOptPower_Type.__name__ = "DisplayString"
_FprlabelOptPower_Object = MibTableColumn
fprlabelOptPower = _FprlabelOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 2),
    _FprlabelOptPower_Type()
)
fprlabelOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelOptPower.setStatus("optional")


class _FpruomOptPower_Type(DisplayString):
    """Custom type fpruomOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FpruomOptPower_Type.__name__ = "DisplayString"
_FpruomOptPower_Object = MibTableColumn
fpruomOptPower = _FpruomOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 3),
    _FpruomOptPower_Type()
)
fpruomOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpruomOptPower.setStatus("optional")
_FprmajorHighOptPower_Type = Float
_FprmajorHighOptPower_Object = MibTableColumn
fprmajorHighOptPower = _FprmajorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 4),
    _FprmajorHighOptPower_Type()
)
fprmajorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorHighOptPower.setStatus("mandatory")
_FprmajorLowOptPower_Type = Float
_FprmajorLowOptPower_Object = MibTableColumn
fprmajorLowOptPower = _FprmajorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 5),
    _FprmajorLowOptPower_Type()
)
fprmajorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorLowOptPower.setStatus("mandatory")
_FprminorHighOptPower_Type = Float
_FprminorHighOptPower_Object = MibTableColumn
fprminorHighOptPower = _FprminorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 6),
    _FprminorHighOptPower_Type()
)
fprminorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorHighOptPower.setStatus("mandatory")
_FprminorLowOptPower_Type = Float
_FprminorLowOptPower_Object = MibTableColumn
fprminorLowOptPower = _FprminorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 7),
    _FprminorLowOptPower_Type()
)
fprminorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorLowOptPower.setStatus("mandatory")
_FprcurrentValueOptPower_Type = Float
_FprcurrentValueOptPower_Object = MibTableColumn
fprcurrentValueOptPower = _FprcurrentValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 8),
    _FprcurrentValueOptPower_Type()
)
fprcurrentValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprcurrentValueOptPower.setStatus("mandatory")


class _FprstateFlagOptPower_Type(Integer32):
    """Custom type fprstateFlagOptPower based on Integer32"""
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


_FprstateFlagOptPower_Type.__name__ = "Integer32"
_FprstateFlagOptPower_Object = MibTableColumn
fprstateFlagOptPower = _FprstateFlagOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 9),
    _FprstateFlagOptPower_Type()
)
fprstateFlagOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagOptPower.setStatus("mandatory")
_FprminValueOptPower_Type = Float
_FprminValueOptPower_Object = MibTableColumn
fprminValueOptPower = _FprminValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 10),
    _FprminValueOptPower_Type()
)
fprminValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminValueOptPower.setStatus("mandatory")
_FprmaxValueOptPower_Type = Float
_FprmaxValueOptPower_Object = MibTableColumn
fprmaxValueOptPower = _FprmaxValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 11),
    _FprmaxValueOptPower_Type()
)
fprmaxValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmaxValueOptPower.setStatus("mandatory")


class _FpralarmStateOptPower_Type(Integer32):
    """Custom type fpralarmStateOptPower based on Integer32"""
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


_FpralarmStateOptPower_Type.__name__ = "Integer32"
_FpralarmStateOptPower_Object = MibTableColumn
fpralarmStateOptPower = _FpralarmStateOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 12),
    _FpralarmStateOptPower_Type()
)
fpralarmStateOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpralarmStateOptPower.setStatus("mandatory")


class _FprlabelModTemp_Type(DisplayString):
    """Custom type fprlabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelModTemp_Type.__name__ = "DisplayString"
_FprlabelModTemp_Object = MibTableColumn
fprlabelModTemp = _FprlabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 13),
    _FprlabelModTemp_Type()
)
fprlabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelModTemp.setStatus("optional")


class _FpruomModTemp_Type(DisplayString):
    """Custom type fpruomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FpruomModTemp_Type.__name__ = "DisplayString"
_FpruomModTemp_Object = MibTableColumn
fpruomModTemp = _FpruomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 14),
    _FpruomModTemp_Type()
)
fpruomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpruomModTemp.setStatus("optional")
_FprmajorHighModTemp_Type = Float
_FprmajorHighModTemp_Object = MibTableColumn
fprmajorHighModTemp = _FprmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 15),
    _FprmajorHighModTemp_Type()
)
fprmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorHighModTemp.setStatus("mandatory")
_FprmajorLowModTemp_Type = Float
_FprmajorLowModTemp_Object = MibTableColumn
fprmajorLowModTemp = _FprmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 16),
    _FprmajorLowModTemp_Type()
)
fprmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorLowModTemp.setStatus("mandatory")
_FprminorHighModTemp_Type = Float
_FprminorHighModTemp_Object = MibTableColumn
fprminorHighModTemp = _FprminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 17),
    _FprminorHighModTemp_Type()
)
fprminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorHighModTemp.setStatus("mandatory")
_FprminorLowModTemp_Type = Float
_FprminorLowModTemp_Object = MibTableColumn
fprminorLowModTemp = _FprminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 18),
    _FprminorLowModTemp_Type()
)
fprminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorLowModTemp.setStatus("mandatory")
_FprcurrentValueModTemp_Type = Float
_FprcurrentValueModTemp_Object = MibTableColumn
fprcurrentValueModTemp = _FprcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 19),
    _FprcurrentValueModTemp_Type()
)
fprcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprcurrentValueModTemp.setStatus("mandatory")


class _FprstateFlagModTemp_Type(Integer32):
    """Custom type fprstateFlagModTemp based on Integer32"""
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


_FprstateFlagModTemp_Type.__name__ = "Integer32"
_FprstateFlagModTemp_Object = MibTableColumn
fprstateFlagModTemp = _FprstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 20),
    _FprstateFlagModTemp_Type()
)
fprstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagModTemp.setStatus("mandatory")
_FprminValueModTemp_Type = Float
_FprminValueModTemp_Object = MibTableColumn
fprminValueModTemp = _FprminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 21),
    _FprminValueModTemp_Type()
)
fprminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminValueModTemp.setStatus("mandatory")
_FprmaxValueModTemp_Type = Float
_FprmaxValueModTemp_Object = MibTableColumn
fprmaxValueModTemp = _FprmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 22),
    _FprmaxValueModTemp_Type()
)
fprmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmaxValueModTemp.setStatus("mandatory")


class _FpralarmStateModTemp_Type(Integer32):
    """Custom type fpralarmStateModTemp based on Integer32"""
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


_FpralarmStateModTemp_Type.__name__ = "Integer32"
_FpralarmStateModTemp_Object = MibTableColumn
fpralarmStateModTemp = _FpralarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 23),
    _FpralarmStateModTemp_Type()
)
fpralarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpralarmStateModTemp.setStatus("mandatory")


class _FprlabelSinkTemp_Type(DisplayString):
    """Custom type fprlabelSinkTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelSinkTemp_Type.__name__ = "DisplayString"
_FprlabelSinkTemp_Object = MibTableColumn
fprlabelSinkTemp = _FprlabelSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 24),
    _FprlabelSinkTemp_Type()
)
fprlabelSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelSinkTemp.setStatus("optional")


class _FpruomSinkTemp_Type(DisplayString):
    """Custom type fpruomSinkTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FpruomSinkTemp_Type.__name__ = "DisplayString"
_FpruomSinkTemp_Object = MibTableColumn
fpruomSinkTemp = _FpruomSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 25),
    _FpruomSinkTemp_Type()
)
fpruomSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpruomSinkTemp.setStatus("optional")
_FprmajorHighSinkTemp_Type = Float
_FprmajorHighSinkTemp_Object = MibTableColumn
fprmajorHighSinkTemp = _FprmajorHighSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 26),
    _FprmajorHighSinkTemp_Type()
)
fprmajorHighSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorHighSinkTemp.setStatus("mandatory")
_FprmajorLowSinkTemp_Type = Float
_FprmajorLowSinkTemp_Object = MibTableColumn
fprmajorLowSinkTemp = _FprmajorLowSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 27),
    _FprmajorLowSinkTemp_Type()
)
fprmajorLowSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorLowSinkTemp.setStatus("mandatory")
_FprminorHighSinkTemp_Type = Float
_FprminorHighSinkTemp_Object = MibTableColumn
fprminorHighSinkTemp = _FprminorHighSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 28),
    _FprminorHighSinkTemp_Type()
)
fprminorHighSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorHighSinkTemp.setStatus("mandatory")
_FprminorLowSinkTemp_Type = Float
_FprminorLowSinkTemp_Object = MibTableColumn
fprminorLowSinkTemp = _FprminorLowSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 29),
    _FprminorLowSinkTemp_Type()
)
fprminorLowSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorLowSinkTemp.setStatus("mandatory")
_FprcurrentValueSinkTemp_Type = Float
_FprcurrentValueSinkTemp_Object = MibTableColumn
fprcurrentValueSinkTemp = _FprcurrentValueSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 30),
    _FprcurrentValueSinkTemp_Type()
)
fprcurrentValueSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprcurrentValueSinkTemp.setStatus("mandatory")


class _FprstateFlagSinkTemp_Type(Integer32):
    """Custom type fprstateFlagSinkTemp based on Integer32"""
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


_FprstateFlagSinkTemp_Type.__name__ = "Integer32"
_FprstateFlagSinkTemp_Object = MibTableColumn
fprstateFlagSinkTemp = _FprstateFlagSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 31),
    _FprstateFlagSinkTemp_Type()
)
fprstateFlagSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagSinkTemp.setStatus("mandatory")
_FprminValueSinkTemp_Type = Float
_FprminValueSinkTemp_Object = MibTableColumn
fprminValueSinkTemp = _FprminValueSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 32),
    _FprminValueSinkTemp_Type()
)
fprminValueSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminValueSinkTemp.setStatus("mandatory")
_FprmaxValueSinkTemp_Type = Float
_FprmaxValueSinkTemp_Object = MibTableColumn
fprmaxValueSinkTemp = _FprmaxValueSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 33),
    _FprmaxValueSinkTemp_Type()
)
fprmaxValueSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmaxValueSinkTemp.setStatus("mandatory")


class _FpralarmStateSinkTemp_Type(Integer32):
    """Custom type fpralarmStateSinkTemp based on Integer32"""
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


_FpralarmStateSinkTemp_Type.__name__ = "Integer32"
_FpralarmStateSinkTemp_Object = MibTableColumn
fpralarmStateSinkTemp = _FpralarmStateSinkTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 34),
    _FpralarmStateSinkTemp_Type()
)
fpralarmStateSinkTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpralarmStateSinkTemp.setStatus("mandatory")


class _FprlabelFanCurrent_Type(DisplayString):
    """Custom type fprlabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelFanCurrent_Type.__name__ = "DisplayString"
_FprlabelFanCurrent_Object = MibTableColumn
fprlabelFanCurrent = _FprlabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 35),
    _FprlabelFanCurrent_Type()
)
fprlabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelFanCurrent.setStatus("optional")


class _FpruomFanCurrent_Type(DisplayString):
    """Custom type fpruomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FpruomFanCurrent_Type.__name__ = "DisplayString"
_FpruomFanCurrent_Object = MibTableColumn
fpruomFanCurrent = _FpruomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 36),
    _FpruomFanCurrent_Type()
)
fpruomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpruomFanCurrent.setStatus("optional")
_FprmajorHighFanCurrent_Type = Float
_FprmajorHighFanCurrent_Object = MibTableColumn
fprmajorHighFanCurrent = _FprmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 37),
    _FprmajorHighFanCurrent_Type()
)
fprmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorHighFanCurrent.setStatus("mandatory")
_FprmajorLowFanCurrent_Type = Float
_FprmajorLowFanCurrent_Object = MibTableColumn
fprmajorLowFanCurrent = _FprmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 38),
    _FprmajorLowFanCurrent_Type()
)
fprmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorLowFanCurrent.setStatus("mandatory")
_FprminorHighFanCurrent_Type = Float
_FprminorHighFanCurrent_Object = MibTableColumn
fprminorHighFanCurrent = _FprminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 39),
    _FprminorHighFanCurrent_Type()
)
fprminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorHighFanCurrent.setStatus("mandatory")
_FprminorLowFanCurrent_Type = Float
_FprminorLowFanCurrent_Object = MibTableColumn
fprminorLowFanCurrent = _FprminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 40),
    _FprminorLowFanCurrent_Type()
)
fprminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorLowFanCurrent.setStatus("mandatory")
_FprcurrentValueFanCurrent_Type = Float
_FprcurrentValueFanCurrent_Object = MibTableColumn
fprcurrentValueFanCurrent = _FprcurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 41),
    _FprcurrentValueFanCurrent_Type()
)
fprcurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprcurrentValueFanCurrent.setStatus("mandatory")


class _FprstateFlagFanCurrent_Type(Integer32):
    """Custom type fprstateFlagFanCurrent based on Integer32"""
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


_FprstateFlagFanCurrent_Type.__name__ = "Integer32"
_FprstateFlagFanCurrent_Object = MibTableColumn
fprstateFlagFanCurrent = _FprstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 42),
    _FprstateFlagFanCurrent_Type()
)
fprstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagFanCurrent.setStatus("mandatory")
_FprminValueFanCurrent_Type = Float
_FprminValueFanCurrent_Object = MibTableColumn
fprminValueFanCurrent = _FprminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 43),
    _FprminValueFanCurrent_Type()
)
fprminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminValueFanCurrent.setStatus("mandatory")
_FprmaxValueFanCurrent_Type = Float
_FprmaxValueFanCurrent_Object = MibTableColumn
fprmaxValueFanCurrent = _FprmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 44),
    _FprmaxValueFanCurrent_Type()
)
fprmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmaxValueFanCurrent.setStatus("mandatory")


class _FpralarmStateFanCurrent_Type(Integer32):
    """Custom type fpralarmStateFanCurrent based on Integer32"""
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


_FpralarmStateFanCurrent_Type.__name__ = "Integer32"
_FpralarmStateFanCurrent_Object = MibTableColumn
fpralarmStateFanCurrent = _FpralarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 45),
    _FpralarmStateFanCurrent_Type()
)
fpralarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpralarmStateFanCurrent.setStatus("mandatory")


class _Fprlabel12Volt_Type(DisplayString):
    """Custom type fprlabel12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Fprlabel12Volt_Type.__name__ = "DisplayString"
_Fprlabel12Volt_Object = MibTableColumn
fprlabel12Volt = _Fprlabel12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 46),
    _Fprlabel12Volt_Type()
)
fprlabel12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabel12Volt.setStatus("optional")


class _Fpruom12Volt_Type(DisplayString):
    """Custom type fpruom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Fpruom12Volt_Type.__name__ = "DisplayString"
_Fpruom12Volt_Object = MibTableColumn
fpruom12Volt = _Fpruom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 47),
    _Fpruom12Volt_Type()
)
fpruom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpruom12Volt.setStatus("optional")
_FprmajorHigh12Volt_Type = Float
_FprmajorHigh12Volt_Object = MibTableColumn
fprmajorHigh12Volt = _FprmajorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 48),
    _FprmajorHigh12Volt_Type()
)
fprmajorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorHigh12Volt.setStatus("mandatory")
_FprmajorLow12Volt_Type = Float
_FprmajorLow12Volt_Object = MibTableColumn
fprmajorLow12Volt = _FprmajorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 49),
    _FprmajorLow12Volt_Type()
)
fprmajorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmajorLow12Volt.setStatus("mandatory")
_FprminorHigh12Volt_Type = Float
_FprminorHigh12Volt_Object = MibTableColumn
fprminorHigh12Volt = _FprminorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 50),
    _FprminorHigh12Volt_Type()
)
fprminorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorHigh12Volt.setStatus("mandatory")
_FprminorLow12Volt_Type = Float
_FprminorLow12Volt_Object = MibTableColumn
fprminorLow12Volt = _FprminorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 51),
    _FprminorLow12Volt_Type()
)
fprminorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminorLow12Volt.setStatus("mandatory")
_FprcurrentValue12Volt_Type = Float
_FprcurrentValue12Volt_Object = MibTableColumn
fprcurrentValue12Volt = _FprcurrentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 52),
    _FprcurrentValue12Volt_Type()
)
fprcurrentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprcurrentValue12Volt.setStatus("mandatory")


class _FprstateFlag12Volt_Type(Integer32):
    """Custom type fprstateFlag12Volt based on Integer32"""
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


_FprstateFlag12Volt_Type.__name__ = "Integer32"
_FprstateFlag12Volt_Object = MibTableColumn
fprstateFlag12Volt = _FprstateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 53),
    _FprstateFlag12Volt_Type()
)
fprstateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlag12Volt.setStatus("mandatory")
_FprminValue12Volt_Type = Float
_FprminValue12Volt_Object = MibTableColumn
fprminValue12Volt = _FprminValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 54),
    _FprminValue12Volt_Type()
)
fprminValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprminValue12Volt.setStatus("mandatory")
_FprmaxValue12Volt_Type = Float
_FprmaxValue12Volt_Object = MibTableColumn
fprmaxValue12Volt = _FprmaxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 55),
    _FprmaxValue12Volt_Type()
)
fprmaxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprmaxValue12Volt.setStatus("mandatory")


class _FpralarmState12Volt_Type(Integer32):
    """Custom type fpralarmState12Volt based on Integer32"""
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


_FpralarmState12Volt_Type.__name__ = "Integer32"
_FpralarmState12Volt_Object = MibTableColumn
fpralarmState12Volt = _FpralarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 2, 1, 56),
    _FpralarmState12Volt_Type()
)
fpralarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpralarmState12Volt.setStatus("mandatory")
_Gx2Rx1000DigitalTable_Object = MibTable
gx2Rx1000DigitalTable = _Gx2Rx1000DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3)
)
if mibBuilder.loadTexts:
    gx2Rx1000DigitalTable.setStatus("mandatory")
_Gx2Rx1000DigitalEntry_Object = MibTableRow
gx2Rx1000DigitalEntry = _Gx2Rx1000DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2)
)
gx2Rx1000DigitalEntry.setIndexNames(
    (0, "OMNI-gx2RX1000-MIB", "fprgx2Rx1000DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx1000DigitalEntry.setStatus("mandatory")


class _Fprgx2Rx1000DigitalTableIndex_Type(Integer32):
    """Custom type fprgx2Rx1000DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Fprgx2Rx1000DigitalTableIndex_Type.__name__ = "Integer32"
_Fprgx2Rx1000DigitalTableIndex_Object = MibTableColumn
fprgx2Rx1000DigitalTableIndex = _Fprgx2Rx1000DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 1),
    _Fprgx2Rx1000DigitalTableIndex_Type()
)
fprgx2Rx1000DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprgx2Rx1000DigitalTableIndex.setStatus("mandatory")


class _FprlabelSlopeSetting_Type(DisplayString):
    """Custom type fprlabelSlopeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelSlopeSetting_Type.__name__ = "DisplayString"
_FprlabelSlopeSetting_Object = MibTableColumn
fprlabelSlopeSetting = _FprlabelSlopeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 2),
    _FprlabelSlopeSetting_Type()
)
fprlabelSlopeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelSlopeSetting.setStatus("optional")


class _FprenumSlopeSetting_Type(DisplayString):
    """Custom type fprenumSlopeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprenumSlopeSetting_Type.__name__ = "DisplayString"
_FprenumSlopeSetting_Object = MibTableColumn
fprenumSlopeSetting = _FprenumSlopeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 3),
    _FprenumSlopeSetting_Type()
)
fprenumSlopeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprenumSlopeSetting.setStatus("optional")
_FprvalueSlopeSetting_Type = Integer32
_FprvalueSlopeSetting_Object = MibTableColumn
fprvalueSlopeSetting = _FprvalueSlopeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 4),
    _FprvalueSlopeSetting_Type()
)
fprvalueSlopeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fprvalueSlopeSetting.setStatus("mandatory")


class _FprstateFlagSlopeSetting_Type(Integer32):
    """Custom type fprstateFlagSlopeSetting based on Integer32"""
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


_FprstateFlagSlopeSetting_Type.__name__ = "Integer32"
_FprstateFlagSlopeSetting_Object = MibTableColumn
fprstateFlagSlopeSetting = _FprstateFlagSlopeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 5),
    _FprstateFlagSlopeSetting_Type()
)
fprstateFlagSlopeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagSlopeSetting.setStatus("mandatory")


class _FprlabelAttnSetting_Type(DisplayString):
    """Custom type fprlabelAttnSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelAttnSetting_Type.__name__ = "DisplayString"
_FprlabelAttnSetting_Object = MibTableColumn
fprlabelAttnSetting = _FprlabelAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 6),
    _FprlabelAttnSetting_Type()
)
fprlabelAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelAttnSetting.setStatus("optional")


class _FprenumAttnSetting_Type(DisplayString):
    """Custom type fprenumAttnSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprenumAttnSetting_Type.__name__ = "DisplayString"
_FprenumAttnSetting_Object = MibTableColumn
fprenumAttnSetting = _FprenumAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 7),
    _FprenumAttnSetting_Type()
)
fprenumAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprenumAttnSetting.setStatus("optional")
_FprvalueAttnSetting_Type = Integer32
_FprvalueAttnSetting_Object = MibTableColumn
fprvalueAttnSetting = _FprvalueAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 8),
    _FprvalueAttnSetting_Type()
)
fprvalueAttnSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fprvalueAttnSetting.setStatus("mandatory")


class _FprstateFlagAttnSetting_Type(Integer32):
    """Custom type fprstateFlagAttnSetting based on Integer32"""
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


_FprstateFlagAttnSetting_Type.__name__ = "Integer32"
_FprstateFlagAttnSetting_Object = MibTableColumn
fprstateFlagAttnSetting = _FprstateFlagAttnSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 9),
    _FprstateFlagAttnSetting_Type()
)
fprstateFlagAttnSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagAttnSetting.setStatus("mandatory")


class _FprlabelWavelength_Type(DisplayString):
    """Custom type fprlabelWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelWavelength_Type.__name__ = "DisplayString"
_FprlabelWavelength_Object = MibTableColumn
fprlabelWavelength = _FprlabelWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 10),
    _FprlabelWavelength_Type()
)
fprlabelWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelWavelength.setStatus("optional")


class _FprenumWavelength_Type(DisplayString):
    """Custom type fprenumWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprenumWavelength_Type.__name__ = "DisplayString"
_FprenumWavelength_Object = MibTableColumn
fprenumWavelength = _FprenumWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 11),
    _FprenumWavelength_Type()
)
fprenumWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprenumWavelength.setStatus("optional")


class _FprvalueWavelength_Type(Integer32):
    """Custom type fprvalueWavelength based on Integer32"""
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


_FprvalueWavelength_Type.__name__ = "Integer32"
_FprvalueWavelength_Object = MibTableColumn
fprvalueWavelength = _FprvalueWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 12),
    _FprvalueWavelength_Type()
)
fprvalueWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fprvalueWavelength.setStatus("mandatory")


class _FprstateFlagWavelength_Type(Integer32):
    """Custom type fprstateFlagWavelength based on Integer32"""
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


_FprstateFlagWavelength_Type.__name__ = "Integer32"
_FprstateFlagWavelength_Object = MibTableColumn
fprstateFlagWavelength = _FprstateFlagWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 13),
    _FprstateFlagWavelength_Type()
)
fprstateFlagWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagWavelength.setStatus("mandatory")


class _FprlabelFactoryDefault_Type(DisplayString):
    """Custom type fprlabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelFactoryDefault_Type.__name__ = "DisplayString"
_FprlabelFactoryDefault_Object = MibTableColumn
fprlabelFactoryDefault = _FprlabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 14),
    _FprlabelFactoryDefault_Type()
)
fprlabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelFactoryDefault.setStatus("optional")


class _FprenumFactoryDefault_Type(DisplayString):
    """Custom type fprenumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprenumFactoryDefault_Type.__name__ = "DisplayString"
_FprenumFactoryDefault_Object = MibTableColumn
fprenumFactoryDefault = _FprenumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 15),
    _FprenumFactoryDefault_Type()
)
fprenumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprenumFactoryDefault.setStatus("optional")


class _FprvalueFactoryDefault_Type(Integer32):
    """Custom type fprvalueFactoryDefault based on Integer32"""
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


_FprvalueFactoryDefault_Type.__name__ = "Integer32"
_FprvalueFactoryDefault_Object = MibTableColumn
fprvalueFactoryDefault = _FprvalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 16),
    _FprvalueFactoryDefault_Type()
)
fprvalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fprvalueFactoryDefault.setStatus("mandatory")


class _FprstateFlagFactoryDefault_Type(Integer32):
    """Custom type fprstateFlagFactoryDefault based on Integer32"""
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


_FprstateFlagFactoryDefault_Type.__name__ = "Integer32"
_FprstateFlagFactoryDefault_Object = MibTableColumn
fprstateFlagFactoryDefault = _FprstateFlagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 17),
    _FprstateFlagFactoryDefault_Type()
)
fprstateFlagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagFactoryDefault.setStatus("mandatory")


class _FprlabelSwModeThreshold_Type(DisplayString):
    """Custom type fprlabelSwModeThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelSwModeThreshold_Type.__name__ = "DisplayString"
_FprlabelSwModeThreshold_Object = MibTableColumn
fprlabelSwModeThreshold = _FprlabelSwModeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 18),
    _FprlabelSwModeThreshold_Type()
)
fprlabelSwModeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelSwModeThreshold.setStatus("optional")


class _FprenumSwModeThreshold_Type(DisplayString):
    """Custom type fprenumSwModeThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprenumSwModeThreshold_Type.__name__ = "DisplayString"
_FprenumSwModeThreshold_Object = MibTableColumn
fprenumSwModeThreshold = _FprenumSwModeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 19),
    _FprenumSwModeThreshold_Type()
)
fprenumSwModeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprenumSwModeThreshold.setStatus("optional")
_FprvalueSwModeThreshold_Type = Integer32
_FprvalueSwModeThreshold_Object = MibTableColumn
fprvalueSwModeThreshold = _FprvalueSwModeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 20),
    _FprvalueSwModeThreshold_Type()
)
fprvalueSwModeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fprvalueSwModeThreshold.setStatus("mandatory")


class _FprstateFlagSwModeThreshold_Type(Integer32):
    """Custom type fprstateFlagSwModeThreshold based on Integer32"""
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


_FprstateFlagSwModeThreshold_Type.__name__ = "Integer32"
_FprstateFlagSwModeThreshold_Object = MibTableColumn
fprstateFlagSwModeThreshold = _FprstateFlagSwModeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 21),
    _FprstateFlagSwModeThreshold_Type()
)
fprstateFlagSwModeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagSwModeThreshold.setStatus("mandatory")


class _FprlabelSwModeSetting_Type(DisplayString):
    """Custom type fprlabelSwModeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelSwModeSetting_Type.__name__ = "DisplayString"
_FprlabelSwModeSetting_Object = MibTableColumn
fprlabelSwModeSetting = _FprlabelSwModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 22),
    _FprlabelSwModeSetting_Type()
)
fprlabelSwModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelSwModeSetting.setStatus("optional")


class _FprenumSwModeSetting_Type(DisplayString):
    """Custom type fprenumSwModeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprenumSwModeSetting_Type.__name__ = "DisplayString"
_FprenumSwModeSetting_Object = MibTableColumn
fprenumSwModeSetting = _FprenumSwModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 23),
    _FprenumSwModeSetting_Type()
)
fprenumSwModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprenumSwModeSetting.setStatus("optional")


class _FprvalueSwModeSetting_Type(Integer32):
    """Custom type fprvalueSwModeSetting based on Integer32"""
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


_FprvalueSwModeSetting_Type.__name__ = "Integer32"
_FprvalueSwModeSetting_Object = MibTableColumn
fprvalueSwModeSetting = _FprvalueSwModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 24),
    _FprvalueSwModeSetting_Type()
)
fprvalueSwModeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fprvalueSwModeSetting.setStatus("mandatory")


class _FprstateFlagSwModeSetting_Type(Integer32):
    """Custom type fprstateFlagSwModeSetting based on Integer32"""
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


_FprstateFlagSwModeSetting_Type.__name__ = "Integer32"
_FprstateFlagSwModeSetting_Object = MibTableColumn
fprstateFlagSwModeSetting = _FprstateFlagSwModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 3, 2, 25),
    _FprstateFlagSwModeSetting_Type()
)
fprstateFlagSwModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateFlagSwModeSetting.setStatus("mandatory")
_Gx2Rx1000StatusTable_Object = MibTable
gx2Rx1000StatusTable = _Gx2Rx1000StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4)
)
if mibBuilder.loadTexts:
    gx2Rx1000StatusTable.setStatus("mandatory")
_Gx2Rx1000StatusEntry_Object = MibTableRow
gx2Rx1000StatusEntry = _Gx2Rx1000StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3)
)
gx2Rx1000StatusEntry.setIndexNames(
    (0, "OMNI-gx2RX1000-MIB", "fprgx2Rx1000StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx1000StatusEntry.setStatus("mandatory")


class _Fprgx2Rx1000StatusTableIndex_Type(Integer32):
    """Custom type fprgx2Rx1000StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Fprgx2Rx1000StatusTableIndex_Type.__name__ = "Integer32"
_Fprgx2Rx1000StatusTableIndex_Object = MibTableColumn
fprgx2Rx1000StatusTableIndex = _Fprgx2Rx1000StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 1),
    _Fprgx2Rx1000StatusTableIndex_Type()
)
fprgx2Rx1000StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprgx2Rx1000StatusTableIndex.setStatus("mandatory")


class _FprlabelBoot_Type(DisplayString):
    """Custom type fprlabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelBoot_Type.__name__ = "DisplayString"
_FprlabelBoot_Object = MibTableColumn
fprlabelBoot = _FprlabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 2),
    _FprlabelBoot_Type()
)
fprlabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelBoot.setStatus("optional")


class _FprvalueBoot_Type(Integer32):
    """Custom type fprvalueBoot based on Integer32"""
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


_FprvalueBoot_Type.__name__ = "Integer32"
_FprvalueBoot_Object = MibTableColumn
fprvalueBoot = _FprvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 3),
    _FprvalueBoot_Type()
)
fprvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprvalueBoot.setStatus("mandatory")


class _FprstateflagBoot_Type(Integer32):
    """Custom type fprstateflagBoot based on Integer32"""
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


_FprstateflagBoot_Type.__name__ = "Integer32"
_FprstateflagBoot_Object = MibTableColumn
fprstateflagBoot = _FprstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 4),
    _FprstateflagBoot_Type()
)
fprstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateflagBoot.setStatus("mandatory")


class _FprlabelFlash_Type(DisplayString):
    """Custom type fprlabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelFlash_Type.__name__ = "DisplayString"
_FprlabelFlash_Object = MibTableColumn
fprlabelFlash = _FprlabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 5),
    _FprlabelFlash_Type()
)
fprlabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelFlash.setStatus("optional")


class _FprvalueFlash_Type(Integer32):
    """Custom type fprvalueFlash based on Integer32"""
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


_FprvalueFlash_Type.__name__ = "Integer32"
_FprvalueFlash_Object = MibTableColumn
fprvalueFlash = _FprvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 6),
    _FprvalueFlash_Type()
)
fprvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprvalueFlash.setStatus("mandatory")


class _FprstateflagFlash_Type(Integer32):
    """Custom type fprstateflagFlash based on Integer32"""
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


_FprstateflagFlash_Type.__name__ = "Integer32"
_FprstateflagFlash_Object = MibTableColumn
fprstateflagFlash = _FprstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 7),
    _FprstateflagFlash_Type()
)
fprstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateflagFlash.setStatus("mandatory")


class _FprlabelFactoryDataCRC_Type(DisplayString):
    """Custom type fprlabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelFactoryDataCRC_Type.__name__ = "DisplayString"
_FprlabelFactoryDataCRC_Object = MibTableColumn
fprlabelFactoryDataCRC = _FprlabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 8),
    _FprlabelFactoryDataCRC_Type()
)
fprlabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelFactoryDataCRC.setStatus("optional")


class _FprvalueFactoryDataCRC_Type(Integer32):
    """Custom type fprvalueFactoryDataCRC based on Integer32"""
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


_FprvalueFactoryDataCRC_Type.__name__ = "Integer32"
_FprvalueFactoryDataCRC_Object = MibTableColumn
fprvalueFactoryDataCRC = _FprvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 9),
    _FprvalueFactoryDataCRC_Type()
)
fprvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprvalueFactoryDataCRC.setStatus("mandatory")


class _FprstateflagFactoryDataCRC_Type(Integer32):
    """Custom type fprstateflagFactoryDataCRC based on Integer32"""
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


_FprstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_FprstateflagFactoryDataCRC_Object = MibTableColumn
fprstateflagFactoryDataCRC = _FprstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 10),
    _FprstateflagFactoryDataCRC_Type()
)
fprstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateflagFactoryDataCRC.setStatus("mandatory")


class _FprlabelAlarmDataCRC_Type(DisplayString):
    """Custom type fprlabelAlarmDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelAlarmDataCRC_Type.__name__ = "DisplayString"
_FprlabelAlarmDataCRC_Object = MibTableColumn
fprlabelAlarmDataCRC = _FprlabelAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 11),
    _FprlabelAlarmDataCRC_Type()
)
fprlabelAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelAlarmDataCRC.setStatus("optional")


class _FprvalueAlarmDataCRC_Type(Integer32):
    """Custom type fprvalueAlarmDataCRC based on Integer32"""
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


_FprvalueAlarmDataCRC_Type.__name__ = "Integer32"
_FprvalueAlarmDataCRC_Object = MibTableColumn
fprvalueAlarmDataCRC = _FprvalueAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 12),
    _FprvalueAlarmDataCRC_Type()
)
fprvalueAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprvalueAlarmDataCRC.setStatus("mandatory")


class _FprstateflagAlarmDataCRC_Type(Integer32):
    """Custom type fprstateflagAlarmDataCRC based on Integer32"""
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


_FprstateflagAlarmDataCRC_Type.__name__ = "Integer32"
_FprstateflagAlarmDataCRC_Object = MibTableColumn
fprstateflagAlarmDataCRC = _FprstateflagAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 13),
    _FprstateflagAlarmDataCRC_Type()
)
fprstateflagAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateflagAlarmDataCRC.setStatus("mandatory")


class _FprlabelCalibrationDataCRC_Type(DisplayString):
    """Custom type fprlabelCalibrationDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelCalibrationDataCRC_Type.__name__ = "DisplayString"
_FprlabelCalibrationDataCRC_Object = MibTableColumn
fprlabelCalibrationDataCRC = _FprlabelCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 14),
    _FprlabelCalibrationDataCRC_Type()
)
fprlabelCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelCalibrationDataCRC.setStatus("optional")


class _FprvalueCalibrationDataCRC_Type(Integer32):
    """Custom type fprvalueCalibrationDataCRC based on Integer32"""
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


_FprvalueCalibrationDataCRC_Type.__name__ = "Integer32"
_FprvalueCalibrationDataCRC_Object = MibTableColumn
fprvalueCalibrationDataCRC = _FprvalueCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 15),
    _FprvalueCalibrationDataCRC_Type()
)
fprvalueCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprvalueCalibrationDataCRC.setStatus("mandatory")


class _FprstateflagCalibrationDataCRC_Type(Integer32):
    """Custom type fprstateflagCalibrationDataCRC based on Integer32"""
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


_FprstateflagCalibrationDataCRC_Type.__name__ = "Integer32"
_FprstateflagCalibrationDataCRC_Object = MibTableColumn
fprstateflagCalibrationDataCRC = _FprstateflagCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 16),
    _FprstateflagCalibrationDataCRC_Type()
)
fprstateflagCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateflagCalibrationDataCRC.setStatus("mandatory")


class _FprlabelFacCalSettingCRC_Type(DisplayString):
    """Custom type fprlabelFacCalSettingCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelFacCalSettingCRC_Type.__name__ = "DisplayString"
_FprlabelFacCalSettingCRC_Object = MibTableColumn
fprlabelFacCalSettingCRC = _FprlabelFacCalSettingCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 17),
    _FprlabelFacCalSettingCRC_Type()
)
fprlabelFacCalSettingCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelFacCalSettingCRC.setStatus("optional")


class _FprvalueFacCalSettingCRC_Type(Integer32):
    """Custom type fprvalueFacCalSettingCRC based on Integer32"""
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


_FprvalueFacCalSettingCRC_Type.__name__ = "Integer32"
_FprvalueFacCalSettingCRC_Object = MibTableColumn
fprvalueFacCalSettingCRC = _FprvalueFacCalSettingCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 18),
    _FprvalueFacCalSettingCRC_Type()
)
fprvalueFacCalSettingCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprvalueFacCalSettingCRC.setStatus("mandatory")


class _FprstateflagFacCalSettingCRC_Type(Integer32):
    """Custom type fprstateflagFacCalSettingCRC based on Integer32"""
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


_FprstateflagFacCalSettingCRC_Type.__name__ = "Integer32"
_FprstateflagFacCalSettingCRC_Object = MibTableColumn
fprstateflagFacCalSettingCRC = _FprstateflagFacCalSettingCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 19),
    _FprstateflagFacCalSettingCRC_Type()
)
fprstateflagFacCalSettingCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateflagFacCalSettingCRC.setStatus("mandatory")


class _FprlabelInputSig_Type(DisplayString):
    """Custom type fprlabelInputSig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprlabelInputSig_Type.__name__ = "DisplayString"
_FprlabelInputSig_Object = MibTableColumn
fprlabelInputSig = _FprlabelInputSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 20),
    _FprlabelInputSig_Type()
)
fprlabelInputSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprlabelInputSig.setStatus("optional")


class _FprvalueInputSig_Type(Integer32):
    """Custom type fprvalueInputSig based on Integer32"""
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


_FprvalueInputSig_Type.__name__ = "Integer32"
_FprvalueInputSig_Object = MibTableColumn
fprvalueInputSig = _FprvalueInputSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 21),
    _FprvalueInputSig_Type()
)
fprvalueInputSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprvalueInputSig.setStatus("mandatory")


class _FprstateflagInputSig_Type(Integer32):
    """Custom type fprstateflagInputSig based on Integer32"""
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


_FprstateflagInputSig_Type.__name__ = "Integer32"
_FprstateflagInputSig_Object = MibTableColumn
fprstateflagInputSig = _FprstateflagInputSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 4, 3, 22),
    _FprstateflagInputSig_Type()
)
fprstateflagInputSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprstateflagInputSig.setStatus("mandatory")
_Gx2Rx1000FactoryTable_Object = MibTable
gx2Rx1000FactoryTable = _Gx2Rx1000FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5)
)
if mibBuilder.loadTexts:
    gx2Rx1000FactoryTable.setStatus("mandatory")
_Gx2Rx1000FactoryEntry_Object = MibTableRow
gx2Rx1000FactoryEntry = _Gx2Rx1000FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4)
)
gx2Rx1000FactoryEntry.setIndexNames(
    (0, "OMNI-gx2RX1000-MIB", "fprgx2Rx1000FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx1000FactoryEntry.setStatus("mandatory")


class _Fprgx2Rx1000FactoryTableIndex_Type(Integer32):
    """Custom type fprgx2Rx1000FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Fprgx2Rx1000FactoryTableIndex_Type.__name__ = "Integer32"
_Fprgx2Rx1000FactoryTableIndex_Object = MibTableColumn
fprgx2Rx1000FactoryTableIndex = _Fprgx2Rx1000FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 1),
    _Fprgx2Rx1000FactoryTableIndex_Type()
)
fprgx2Rx1000FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprgx2Rx1000FactoryTableIndex.setStatus("mandatory")
_FprbootControlByte_Type = Integer32
_FprbootControlByte_Object = MibTableColumn
fprbootControlByte = _FprbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 2),
    _FprbootControlByte_Type()
)
fprbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprbootControlByte.setStatus("mandatory")
_FprbootStatusByte_Type = Integer32
_FprbootStatusByte_Object = MibTableColumn
fprbootStatusByte = _FprbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 3),
    _FprbootStatusByte_Type()
)
fprbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprbootStatusByte.setStatus("mandatory")
_Fprbank0CRC_Type = Integer32
_Fprbank0CRC_Object = MibTableColumn
fprbank0CRC = _Fprbank0CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 4),
    _Fprbank0CRC_Type()
)
fprbank0CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprbank0CRC.setStatus("mandatory")
_Fprbank1CRC_Type = Integer32
_Fprbank1CRC_Object = MibTableColumn
fprbank1CRC = _Fprbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 5),
    _Fprbank1CRC_Type()
)
fprbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprbank1CRC.setStatus("mandatory")
_FprprgEEPROMByte_Type = Integer32
_FprprgEEPROMByte_Object = MibTableColumn
fprprgEEPROMByte = _FprprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 6),
    _FprprgEEPROMByte_Type()
)
fprprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprprgEEPROMByte.setStatus("mandatory")
_FprfactoryCRC_Type = Integer32
_FprfactoryCRC_Object = MibTableColumn
fprfactoryCRC = _FprfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 7),
    _FprfactoryCRC_Type()
)
fprfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprfactoryCRC.setStatus("mandatory")


class _FprcalculateCRC_Type(Integer32):
    """Custom type fprcalculateCRC based on Integer32"""
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


_FprcalculateCRC_Type.__name__ = "Integer32"
_FprcalculateCRC_Object = MibTableColumn
fprcalculateCRC = _FprcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 8),
    _FprcalculateCRC_Type()
)
fprcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprcalculateCRC.setStatus("mandatory")
_FprhourMeter_Type = Integer32
_FprhourMeter_Object = MibTableColumn
fprhourMeter = _FprhourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 9),
    _FprhourMeter_Type()
)
fprhourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprhourMeter.setStatus("mandatory")
_FprflashPrgCntA_Type = Integer32
_FprflashPrgCntA_Object = MibTableColumn
fprflashPrgCntA = _FprflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 10),
    _FprflashPrgCntA_Type()
)
fprflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprflashPrgCntA.setStatus("mandatory")
_FprflashPrgCntB_Type = Integer32
_FprflashPrgCntB_Object = MibTableColumn
fprflashPrgCntB = _FprflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 11),
    _FprflashPrgCntB_Type()
)
fprflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprflashPrgCntB.setStatus("mandatory")


class _FprfwRev0_Type(DisplayString):
    """Custom type fprfwRev0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprfwRev0_Type.__name__ = "DisplayString"
_FprfwRev0_Object = MibTableColumn
fprfwRev0 = _FprfwRev0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 12),
    _FprfwRev0_Type()
)
fprfwRev0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprfwRev0.setStatus("mandatory")


class _FprfwRev1_Type(DisplayString):
    """Custom type fprfwRev1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FprfwRev1_Type.__name__ = "DisplayString"
_FprfwRev1_Object = MibTableColumn
fprfwRev1 = _FprfwRev1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 5, 4, 13),
    _FprfwRev1_Type()
)
fprfwRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fprfwRev1.setStatus("mandatory")
_Gx2Rx1000HoldTimeTable_Object = MibTable
gx2Rx1000HoldTimeTable = _Gx2Rx1000HoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 6)
)
if mibBuilder.loadTexts:
    gx2Rx1000HoldTimeTable.setStatus("mandatory")
_Gx2Rx1000HoldTimeEntry_Object = MibTableRow
gx2Rx1000HoldTimeEntry = _Gx2Rx1000HoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 6, 5)
)
gx2Rx1000HoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2RX1000-MIB", "gx2Rx1000HoldTimeTableIndex"),
    (0, "OMNI-gx2RX1000-MIB", "gx2Rx1000HoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx1000HoldTimeEntry.setStatus("mandatory")


class _Gx2Rx1000HoldTimeTableIndex_Type(Integer32):
    """Custom type gx2Rx1000HoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx1000HoldTimeTableIndex_Type.__name__ = "Integer32"
_Gx2Rx1000HoldTimeTableIndex_Object = MibTableColumn
gx2Rx1000HoldTimeTableIndex = _Gx2Rx1000HoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 6, 5, 1),
    _Gx2Rx1000HoldTimeTableIndex_Type()
)
gx2Rx1000HoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx1000HoldTimeTableIndex.setStatus("mandatory")


class _Gx2Rx1000HoldTimeSpecIndex_Type(Integer32):
    """Custom type gx2Rx1000HoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx1000HoldTimeSpecIndex_Type.__name__ = "Integer32"
_Gx2Rx1000HoldTimeSpecIndex_Object = MibTableColumn
gx2Rx1000HoldTimeSpecIndex = _Gx2Rx1000HoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 6, 5, 2),
    _Gx2Rx1000HoldTimeSpecIndex_Type()
)
gx2Rx1000HoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx1000HoldTimeSpecIndex.setStatus("mandatory")
_Gx2Rx1000HoldTimeData_Type = Integer32
_Gx2Rx1000HoldTimeData_Object = MibTableColumn
gx2Rx1000HoldTimeData = _Gx2Rx1000HoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 6, 5, 3),
    _Gx2Rx1000HoldTimeData_Type()
)
gx2Rx1000HoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gx2Rx1000HoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapRX1000ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 1)
)
trapRX1000ConfigChangeInteger.setObjects(
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
    trapRX1000ConfigChangeInteger.setStatus(
        ""
    )

trapRX1000ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 2)
)
trapRX1000ConfigChangeDisplayString.setObjects(
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
    trapRX1000ConfigChangeDisplayString.setStatus(
        ""
    )

trapRX1000OpticalPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 3)
)
trapRX1000OpticalPowerAlarm.setObjects(
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
    trapRX1000OpticalPowerAlarm.setStatus(
        ""
    )

trapRX1000ModuleTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 4)
)
trapRX1000ModuleTemperatureAlarm.setObjects(
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
    trapRX1000ModuleTemperatureAlarm.setStatus(
        ""
    )

trapRX1000HeatSinkTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 5)
)
trapRX1000HeatSinkTemperatureAlarm.setObjects(
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
    trapRX1000HeatSinkTemperatureAlarm.setStatus(
        ""
    )

trapRX1000FanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 6)
)
trapRX1000FanCurrentAlarm.setObjects(
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
    trapRX1000FanCurrentAlarm.setStatus(
        ""
    )

trapRX1000Plus12CurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 7)
)
trapRX1000Plus12CurrentAlarm.setObjects(
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
    trapRX1000Plus12CurrentAlarm.setStatus(
        ""
    )

trapRX1000OpticalSwitchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 8)
)
trapRX1000OpticalSwitchAlarm.setObjects(
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
    trapRX1000OpticalSwitchAlarm.setStatus(
        ""
    )

trapRX1000Boot0Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 9)
)
trapRX1000Boot0Alarm.setObjects(
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
    trapRX1000Boot0Alarm.setStatus(
        ""
    )

trapRX1000Boot1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 10)
)
trapRX1000Boot1Alarm.setObjects(
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
    trapRX1000Boot1Alarm.setStatus(
        ""
    )

trapRX1000FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 11)
)
trapRX1000FlashAlarm.setObjects(
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
    trapRX1000FlashAlarm.setStatus(
        ""
    )

trapRX1000AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 12)
)
trapRX1000AlarmDataCRCAlarm.setObjects(
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
    trapRX1000AlarmDataCRCAlarm.setStatus(
        ""
    )

trapRX1000FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 13)
)
trapRX1000FactoryDataCRCAlarm.setObjects(
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
    trapRX1000FactoryDataCRCAlarm.setStatus(
        ""
    )

trapRX1000CalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 14)
)
trapRX1000CalDataCRCAlarm.setObjects(
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
    trapRX1000CalDataCRCAlarm.setStatus(
        ""
    )

trapRX1000ResetFacDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 15)
)
trapRX1000ResetFacDefault.setObjects(
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
    trapRX1000ResetFacDefault.setStatus(
        ""
    )

trapRX1000FacCalSettingCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9, 0, 16)
)
trapRX1000FacCalSettingCRCAlarm.setObjects(
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
    trapRX1000FacCalSettingCRCAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2RX1000-MIB",
    **{"Float": Float,
       "trapRX1000ConfigChangeInteger": trapRX1000ConfigChangeInteger,
       "trapRX1000ConfigChangeDisplayString": trapRX1000ConfigChangeDisplayString,
       "trapRX1000OpticalPowerAlarm": trapRX1000OpticalPowerAlarm,
       "trapRX1000ModuleTemperatureAlarm": trapRX1000ModuleTemperatureAlarm,
       "trapRX1000HeatSinkTemperatureAlarm": trapRX1000HeatSinkTemperatureAlarm,
       "trapRX1000FanCurrentAlarm": trapRX1000FanCurrentAlarm,
       "trapRX1000Plus12CurrentAlarm": trapRX1000Plus12CurrentAlarm,
       "trapRX1000OpticalSwitchAlarm": trapRX1000OpticalSwitchAlarm,
       "trapRX1000Boot0Alarm": trapRX1000Boot0Alarm,
       "trapRX1000Boot1Alarm": trapRX1000Boot1Alarm,
       "trapRX1000FlashAlarm": trapRX1000FlashAlarm,
       "trapRX1000AlarmDataCRCAlarm": trapRX1000AlarmDataCRCAlarm,
       "trapRX1000FactoryDataCRCAlarm": trapRX1000FactoryDataCRCAlarm,
       "trapRX1000CalDataCRCAlarm": trapRX1000CalDataCRCAlarm,
       "trapRX1000ResetFacDefault": trapRX1000ResetFacDefault,
       "trapRX1000FacCalSettingCRCAlarm": trapRX1000FacCalSettingCRCAlarm,
       "gx2Rx1000Descriptor": gx2Rx1000Descriptor,
       "gx2Rx1000AnalogTable": gx2Rx1000AnalogTable,
       "gx2Rx1000AnalogEntry": gx2Rx1000AnalogEntry,
       "fprgx2Rx1000AnalogTableIndex": fprgx2Rx1000AnalogTableIndex,
       "fprlabelOptPower": fprlabelOptPower,
       "fpruomOptPower": fpruomOptPower,
       "fprmajorHighOptPower": fprmajorHighOptPower,
       "fprmajorLowOptPower": fprmajorLowOptPower,
       "fprminorHighOptPower": fprminorHighOptPower,
       "fprminorLowOptPower": fprminorLowOptPower,
       "fprcurrentValueOptPower": fprcurrentValueOptPower,
       "fprstateFlagOptPower": fprstateFlagOptPower,
       "fprminValueOptPower": fprminValueOptPower,
       "fprmaxValueOptPower": fprmaxValueOptPower,
       "fpralarmStateOptPower": fpralarmStateOptPower,
       "fprlabelModTemp": fprlabelModTemp,
       "fpruomModTemp": fpruomModTemp,
       "fprmajorHighModTemp": fprmajorHighModTemp,
       "fprmajorLowModTemp": fprmajorLowModTemp,
       "fprminorHighModTemp": fprminorHighModTemp,
       "fprminorLowModTemp": fprminorLowModTemp,
       "fprcurrentValueModTemp": fprcurrentValueModTemp,
       "fprstateFlagModTemp": fprstateFlagModTemp,
       "fprminValueModTemp": fprminValueModTemp,
       "fprmaxValueModTemp": fprmaxValueModTemp,
       "fpralarmStateModTemp": fpralarmStateModTemp,
       "fprlabelSinkTemp": fprlabelSinkTemp,
       "fpruomSinkTemp": fpruomSinkTemp,
       "fprmajorHighSinkTemp": fprmajorHighSinkTemp,
       "fprmajorLowSinkTemp": fprmajorLowSinkTemp,
       "fprminorHighSinkTemp": fprminorHighSinkTemp,
       "fprminorLowSinkTemp": fprminorLowSinkTemp,
       "fprcurrentValueSinkTemp": fprcurrentValueSinkTemp,
       "fprstateFlagSinkTemp": fprstateFlagSinkTemp,
       "fprminValueSinkTemp": fprminValueSinkTemp,
       "fprmaxValueSinkTemp": fprmaxValueSinkTemp,
       "fpralarmStateSinkTemp": fpralarmStateSinkTemp,
       "fprlabelFanCurrent": fprlabelFanCurrent,
       "fpruomFanCurrent": fpruomFanCurrent,
       "fprmajorHighFanCurrent": fprmajorHighFanCurrent,
       "fprmajorLowFanCurrent": fprmajorLowFanCurrent,
       "fprminorHighFanCurrent": fprminorHighFanCurrent,
       "fprminorLowFanCurrent": fprminorLowFanCurrent,
       "fprcurrentValueFanCurrent": fprcurrentValueFanCurrent,
       "fprstateFlagFanCurrent": fprstateFlagFanCurrent,
       "fprminValueFanCurrent": fprminValueFanCurrent,
       "fprmaxValueFanCurrent": fprmaxValueFanCurrent,
       "fpralarmStateFanCurrent": fpralarmStateFanCurrent,
       "fprlabel12Volt": fprlabel12Volt,
       "fpruom12Volt": fpruom12Volt,
       "fprmajorHigh12Volt": fprmajorHigh12Volt,
       "fprmajorLow12Volt": fprmajorLow12Volt,
       "fprminorHigh12Volt": fprminorHigh12Volt,
       "fprminorLow12Volt": fprminorLow12Volt,
       "fprcurrentValue12Volt": fprcurrentValue12Volt,
       "fprstateFlag12Volt": fprstateFlag12Volt,
       "fprminValue12Volt": fprminValue12Volt,
       "fprmaxValue12Volt": fprmaxValue12Volt,
       "fpralarmState12Volt": fpralarmState12Volt,
       "gx2Rx1000DigitalTable": gx2Rx1000DigitalTable,
       "gx2Rx1000DigitalEntry": gx2Rx1000DigitalEntry,
       "fprgx2Rx1000DigitalTableIndex": fprgx2Rx1000DigitalTableIndex,
       "fprlabelSlopeSetting": fprlabelSlopeSetting,
       "fprenumSlopeSetting": fprenumSlopeSetting,
       "fprvalueSlopeSetting": fprvalueSlopeSetting,
       "fprstateFlagSlopeSetting": fprstateFlagSlopeSetting,
       "fprlabelAttnSetting": fprlabelAttnSetting,
       "fprenumAttnSetting": fprenumAttnSetting,
       "fprvalueAttnSetting": fprvalueAttnSetting,
       "fprstateFlagAttnSetting": fprstateFlagAttnSetting,
       "fprlabelWavelength": fprlabelWavelength,
       "fprenumWavelength": fprenumWavelength,
       "fprvalueWavelength": fprvalueWavelength,
       "fprstateFlagWavelength": fprstateFlagWavelength,
       "fprlabelFactoryDefault": fprlabelFactoryDefault,
       "fprenumFactoryDefault": fprenumFactoryDefault,
       "fprvalueFactoryDefault": fprvalueFactoryDefault,
       "fprstateFlagFactoryDefault": fprstateFlagFactoryDefault,
       "fprlabelSwModeThreshold": fprlabelSwModeThreshold,
       "fprenumSwModeThreshold": fprenumSwModeThreshold,
       "fprvalueSwModeThreshold": fprvalueSwModeThreshold,
       "fprstateFlagSwModeThreshold": fprstateFlagSwModeThreshold,
       "fprlabelSwModeSetting": fprlabelSwModeSetting,
       "fprenumSwModeSetting": fprenumSwModeSetting,
       "fprvalueSwModeSetting": fprvalueSwModeSetting,
       "fprstateFlagSwModeSetting": fprstateFlagSwModeSetting,
       "gx2Rx1000StatusTable": gx2Rx1000StatusTable,
       "gx2Rx1000StatusEntry": gx2Rx1000StatusEntry,
       "fprgx2Rx1000StatusTableIndex": fprgx2Rx1000StatusTableIndex,
       "fprlabelBoot": fprlabelBoot,
       "fprvalueBoot": fprvalueBoot,
       "fprstateflagBoot": fprstateflagBoot,
       "fprlabelFlash": fprlabelFlash,
       "fprvalueFlash": fprvalueFlash,
       "fprstateflagFlash": fprstateflagFlash,
       "fprlabelFactoryDataCRC": fprlabelFactoryDataCRC,
       "fprvalueFactoryDataCRC": fprvalueFactoryDataCRC,
       "fprstateflagFactoryDataCRC": fprstateflagFactoryDataCRC,
       "fprlabelAlarmDataCRC": fprlabelAlarmDataCRC,
       "fprvalueAlarmDataCRC": fprvalueAlarmDataCRC,
       "fprstateflagAlarmDataCRC": fprstateflagAlarmDataCRC,
       "fprlabelCalibrationDataCRC": fprlabelCalibrationDataCRC,
       "fprvalueCalibrationDataCRC": fprvalueCalibrationDataCRC,
       "fprstateflagCalibrationDataCRC": fprstateflagCalibrationDataCRC,
       "fprlabelFacCalSettingCRC": fprlabelFacCalSettingCRC,
       "fprvalueFacCalSettingCRC": fprvalueFacCalSettingCRC,
       "fprstateflagFacCalSettingCRC": fprstateflagFacCalSettingCRC,
       "fprlabelInputSig": fprlabelInputSig,
       "fprvalueInputSig": fprvalueInputSig,
       "fprstateflagInputSig": fprstateflagInputSig,
       "gx2Rx1000FactoryTable": gx2Rx1000FactoryTable,
       "gx2Rx1000FactoryEntry": gx2Rx1000FactoryEntry,
       "fprgx2Rx1000FactoryTableIndex": fprgx2Rx1000FactoryTableIndex,
       "fprbootControlByte": fprbootControlByte,
       "fprbootStatusByte": fprbootStatusByte,
       "fprbank0CRC": fprbank0CRC,
       "fprbank1CRC": fprbank1CRC,
       "fprprgEEPROMByte": fprprgEEPROMByte,
       "fprfactoryCRC": fprfactoryCRC,
       "fprcalculateCRC": fprcalculateCRC,
       "fprhourMeter": fprhourMeter,
       "fprflashPrgCntA": fprflashPrgCntA,
       "fprflashPrgCntB": fprflashPrgCntB,
       "fprfwRev0": fprfwRev0,
       "fprfwRev1": fprfwRev1,
       "gx2Rx1000HoldTimeTable": gx2Rx1000HoldTimeTable,
       "gx2Rx1000HoldTimeEntry": gx2Rx1000HoldTimeEntry,
       "gx2Rx1000HoldTimeTableIndex": gx2Rx1000HoldTimeTableIndex,
       "gx2Rx1000HoldTimeSpecIndex": gx2Rx1000HoldTimeSpecIndex,
       "gx2Rx1000HoldTimeData": gx2Rx1000HoldTimeData}
)
