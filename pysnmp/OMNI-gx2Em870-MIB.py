# SNMP MIB module (OMNI-gx2Em870-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2Em870-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:21 2024
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

(gx2Em870,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Em870")

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

_Gx2Em870Descriptor_ObjectIdentity = ObjectIdentity
gx2Em870Descriptor = _Gx2Em870Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 1)
)
_Gx2Em870AnalogTable_Object = MibTable
gx2Em870AnalogTable = _Gx2Em870AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    gx2Em870AnalogTable.setStatus("mandatory")
_Gx2Em870AnalogEntry_Object = MibTableRow
gx2Em870AnalogEntry = _Gx2Em870AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1)
)
gx2Em870AnalogEntry.setIndexNames(
    (0, "OMNI-gx2Em870-MIB", "gx2Em870AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Em870AnalogEntry.setStatus("mandatory")


class _Gx2Em870AnalogTableIndex_Type(Integer32):
    """Custom type gx2Em870AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Em870AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Em870AnalogTableIndex_Object = MibTableColumn
gx2Em870AnalogTableIndex = _Gx2Em870AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 1),
    _Gx2Em870AnalogTableIndex_Type()
)
gx2Em870AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Em870AnalogTableIndex.setStatus("mandatory")


class _Em870labelOpticalPower_Type(DisplayString):
    """Custom type em870labelOpticalPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelOpticalPower_Type.__name__ = "DisplayString"
_Em870labelOpticalPower_Object = MibTableColumn
em870labelOpticalPower = _Em870labelOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 2),
    _Em870labelOpticalPower_Type()
)
em870labelOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelOpticalPower.setStatus("optional")


class _Em870uomOpticalPower_Type(DisplayString):
    """Custom type em870uomOpticalPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870uomOpticalPower_Type.__name__ = "DisplayString"
_Em870uomOpticalPower_Object = MibTableColumn
em870uomOpticalPower = _Em870uomOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 3),
    _Em870uomOpticalPower_Type()
)
em870uomOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870uomOpticalPower.setStatus("optional")
_Em870majorHighOpticalPower_Type = Float
_Em870majorHighOpticalPower_Object = MibTableColumn
em870majorHighOpticalPower = _Em870majorHighOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 4),
    _Em870majorHighOpticalPower_Type()
)
em870majorHighOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorHighOpticalPower.setStatus("mandatory")
_Em870majorLowOpticalPower_Type = Float
_Em870majorLowOpticalPower_Object = MibTableColumn
em870majorLowOpticalPower = _Em870majorLowOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 5),
    _Em870majorLowOpticalPower_Type()
)
em870majorLowOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorLowOpticalPower.setStatus("mandatory")
_Em870minorHighOpticalPower_Type = Float
_Em870minorHighOpticalPower_Object = MibTableColumn
em870minorHighOpticalPower = _Em870minorHighOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 6),
    _Em870minorHighOpticalPower_Type()
)
em870minorHighOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorHighOpticalPower.setStatus("mandatory")
_Em870minorLowOpticalPower_Type = Float
_Em870minorLowOpticalPower_Object = MibTableColumn
em870minorLowOpticalPower = _Em870minorLowOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 7),
    _Em870minorLowOpticalPower_Type()
)
em870minorLowOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorLowOpticalPower.setStatus("mandatory")
_Em870currentValueOpticalPower_Type = Float
_Em870currentValueOpticalPower_Object = MibTableColumn
em870currentValueOpticalPower = _Em870currentValueOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 8),
    _Em870currentValueOpticalPower_Type()
)
em870currentValueOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870currentValueOpticalPower.setStatus("mandatory")


class _Em870stateFlagOpticalPower_Type(Integer32):
    """Custom type em870stateFlagOpticalPower based on Integer32"""
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


_Em870stateFlagOpticalPower_Type.__name__ = "Integer32"
_Em870stateFlagOpticalPower_Object = MibTableColumn
em870stateFlagOpticalPower = _Em870stateFlagOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 9),
    _Em870stateFlagOpticalPower_Type()
)
em870stateFlagOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlagOpticalPower.setStatus("mandatory")
_Em870minValueOpticalPower_Type = Float
_Em870minValueOpticalPower_Object = MibTableColumn
em870minValueOpticalPower = _Em870minValueOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 10),
    _Em870minValueOpticalPower_Type()
)
em870minValueOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minValueOpticalPower.setStatus("mandatory")
_Em870maxValueOpticalPower_Type = Float
_Em870maxValueOpticalPower_Object = MibTableColumn
em870maxValueOpticalPower = _Em870maxValueOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 11),
    _Em870maxValueOpticalPower_Type()
)
em870maxValueOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870maxValueOpticalPower.setStatus("mandatory")


class _Em870alarmStateOpticalPower_Type(Integer32):
    """Custom type em870alarmStateOpticalPower based on Integer32"""
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


_Em870alarmStateOpticalPower_Type.__name__ = "Integer32"
_Em870alarmStateOpticalPower_Object = MibTableColumn
em870alarmStateOpticalPower = _Em870alarmStateOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 12),
    _Em870alarmStateOpticalPower_Type()
)
em870alarmStateOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870alarmStateOpticalPower.setStatus("mandatory")


class _Em870labelOmiOffset_Type(DisplayString):
    """Custom type em870labelOmiOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelOmiOffset_Type.__name__ = "DisplayString"
_Em870labelOmiOffset_Object = MibTableColumn
em870labelOmiOffset = _Em870labelOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 13),
    _Em870labelOmiOffset_Type()
)
em870labelOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelOmiOffset.setStatus("optional")


class _Em870uomOmiOffset_Type(DisplayString):
    """Custom type em870uomOmiOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870uomOmiOffset_Type.__name__ = "DisplayString"
_Em870uomOmiOffset_Object = MibTableColumn
em870uomOmiOffset = _Em870uomOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 14),
    _Em870uomOmiOffset_Type()
)
em870uomOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870uomOmiOffset.setStatus("optional")
_Em870majorHighOmiOffset_Type = Float
_Em870majorHighOmiOffset_Object = MibTableColumn
em870majorHighOmiOffset = _Em870majorHighOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 15),
    _Em870majorHighOmiOffset_Type()
)
em870majorHighOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorHighOmiOffset.setStatus("mandatory")
_Em870majorLowOmiOffset_Type = Float
_Em870majorLowOmiOffset_Object = MibTableColumn
em870majorLowOmiOffset = _Em870majorLowOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 16),
    _Em870majorLowOmiOffset_Type()
)
em870majorLowOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorLowOmiOffset.setStatus("mandatory")
_Em870minorHighOmiOffset_Type = Float
_Em870minorHighOmiOffset_Object = MibTableColumn
em870minorHighOmiOffset = _Em870minorHighOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 17),
    _Em870minorHighOmiOffset_Type()
)
em870minorHighOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorHighOmiOffset.setStatus("mandatory")
_Em870minorLowOmiOffset_Type = Float
_Em870minorLowOmiOffset_Object = MibTableColumn
em870minorLowOmiOffset = _Em870minorLowOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 18),
    _Em870minorLowOmiOffset_Type()
)
em870minorLowOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorLowOmiOffset.setStatus("mandatory")
_Em870currentValueOmiOffset_Type = Float
_Em870currentValueOmiOffset_Object = MibTableColumn
em870currentValueOmiOffset = _Em870currentValueOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 19),
    _Em870currentValueOmiOffset_Type()
)
em870currentValueOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870currentValueOmiOffset.setStatus("mandatory")


class _Em870stateFlagOmiOffset_Type(Integer32):
    """Custom type em870stateFlagOmiOffset based on Integer32"""
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


_Em870stateFlagOmiOffset_Type.__name__ = "Integer32"
_Em870stateFlagOmiOffset_Object = MibTableColumn
em870stateFlagOmiOffset = _Em870stateFlagOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 20),
    _Em870stateFlagOmiOffset_Type()
)
em870stateFlagOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlagOmiOffset.setStatus("mandatory")
_Em870minValueOmiOffset_Type = Float
_Em870minValueOmiOffset_Object = MibTableColumn
em870minValueOmiOffset = _Em870minValueOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 21),
    _Em870minValueOmiOffset_Type()
)
em870minValueOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minValueOmiOffset.setStatus("mandatory")
_Em870maxValueOmiOffset_Type = Float
_Em870maxValueOmiOffset_Object = MibTableColumn
em870maxValueOmiOffset = _Em870maxValueOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 22),
    _Em870maxValueOmiOffset_Type()
)
em870maxValueOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870maxValueOmiOffset.setStatus("mandatory")


class _Em870alarmStateOmiOffset_Type(Integer32):
    """Custom type em870alarmStateOmiOffset based on Integer32"""
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


_Em870alarmStateOmiOffset_Type.__name__ = "Integer32"
_Em870alarmStateOmiOffset_Object = MibTableColumn
em870alarmStateOmiOffset = _Em870alarmStateOmiOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 23),
    _Em870alarmStateOmiOffset_Type()
)
em870alarmStateOmiOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870alarmStateOmiOffset.setStatus("mandatory")


class _Em870labelDFBPower_Type(DisplayString):
    """Custom type em870labelDFBPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelDFBPower_Type.__name__ = "DisplayString"
_Em870labelDFBPower_Object = MibTableColumn
em870labelDFBPower = _Em870labelDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 24),
    _Em870labelDFBPower_Type()
)
em870labelDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelDFBPower.setStatus("optional")


class _Em870uomDFBPower_Type(DisplayString):
    """Custom type em870uomDFBPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870uomDFBPower_Type.__name__ = "DisplayString"
_Em870uomDFBPower_Object = MibTableColumn
em870uomDFBPower = _Em870uomDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 25),
    _Em870uomDFBPower_Type()
)
em870uomDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870uomDFBPower.setStatus("optional")
_Em870majorHighDFBPower_Type = Float
_Em870majorHighDFBPower_Object = MibTableColumn
em870majorHighDFBPower = _Em870majorHighDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 26),
    _Em870majorHighDFBPower_Type()
)
em870majorHighDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorHighDFBPower.setStatus("mandatory")
_Em870majorLowDFBPower_Type = Float
_Em870majorLowDFBPower_Object = MibTableColumn
em870majorLowDFBPower = _Em870majorLowDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 27),
    _Em870majorLowDFBPower_Type()
)
em870majorLowDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorLowDFBPower.setStatus("mandatory")
_Em870minorHighDFBPower_Type = Float
_Em870minorHighDFBPower_Object = MibTableColumn
em870minorHighDFBPower = _Em870minorHighDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 28),
    _Em870minorHighDFBPower_Type()
)
em870minorHighDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorHighDFBPower.setStatus("mandatory")
_Em870minorLowDFBPower_Type = Float
_Em870minorLowDFBPower_Object = MibTableColumn
em870minorLowDFBPower = _Em870minorLowDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 29),
    _Em870minorLowDFBPower_Type()
)
em870minorLowDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorLowDFBPower.setStatus("mandatory")
_Em870currentValueDFBPower_Type = Float
_Em870currentValueDFBPower_Object = MibTableColumn
em870currentValueDFBPower = _Em870currentValueDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 30),
    _Em870currentValueDFBPower_Type()
)
em870currentValueDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870currentValueDFBPower.setStatus("mandatory")


class _Em870stateFlagDFBPower_Type(Integer32):
    """Custom type em870stateFlagDFBPower based on Integer32"""
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


_Em870stateFlagDFBPower_Type.__name__ = "Integer32"
_Em870stateFlagDFBPower_Object = MibTableColumn
em870stateFlagDFBPower = _Em870stateFlagDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 31),
    _Em870stateFlagDFBPower_Type()
)
em870stateFlagDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlagDFBPower.setStatus("mandatory")
_Em870minValueDFBPower_Type = Float
_Em870minValueDFBPower_Object = MibTableColumn
em870minValueDFBPower = _Em870minValueDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 32),
    _Em870minValueDFBPower_Type()
)
em870minValueDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minValueDFBPower.setStatus("mandatory")
_Em870maxValueDFBPower_Type = Float
_Em870maxValueDFBPower_Object = MibTableColumn
em870maxValueDFBPower = _Em870maxValueDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 33),
    _Em870maxValueDFBPower_Type()
)
em870maxValueDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870maxValueDFBPower.setStatus("mandatory")


class _Em870alarmStateDFBPower_Type(Integer32):
    """Custom type em870alarmStateDFBPower based on Integer32"""
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


_Em870alarmStateDFBPower_Type.__name__ = "Integer32"
_Em870alarmStateDFBPower_Object = MibTableColumn
em870alarmStateDFBPower = _Em870alarmStateDFBPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 34),
    _Em870alarmStateDFBPower_Type()
)
em870alarmStateDFBPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870alarmStateDFBPower.setStatus("mandatory")


class _Em870labelLaserBias_Type(DisplayString):
    """Custom type em870labelLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelLaserBias_Type.__name__ = "DisplayString"
_Em870labelLaserBias_Object = MibTableColumn
em870labelLaserBias = _Em870labelLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 35),
    _Em870labelLaserBias_Type()
)
em870labelLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelLaserBias.setStatus("optional")


class _Em870uomLaserBias_Type(DisplayString):
    """Custom type em870uomLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870uomLaserBias_Type.__name__ = "DisplayString"
_Em870uomLaserBias_Object = MibTableColumn
em870uomLaserBias = _Em870uomLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 36),
    _Em870uomLaserBias_Type()
)
em870uomLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870uomLaserBias.setStatus("optional")
_Em870majorHighLaserBias_Type = Float
_Em870majorHighLaserBias_Object = MibTableColumn
em870majorHighLaserBias = _Em870majorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 37),
    _Em870majorHighLaserBias_Type()
)
em870majorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorHighLaserBias.setStatus("mandatory")
_Em870majorLowLaserBias_Type = Float
_Em870majorLowLaserBias_Object = MibTableColumn
em870majorLowLaserBias = _Em870majorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 38),
    _Em870majorLowLaserBias_Type()
)
em870majorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorLowLaserBias.setStatus("mandatory")
_Em870minorHighLaserBias_Type = Float
_Em870minorHighLaserBias_Object = MibTableColumn
em870minorHighLaserBias = _Em870minorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 39),
    _Em870minorHighLaserBias_Type()
)
em870minorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorHighLaserBias.setStatus("mandatory")
_Em870minorLowLaserBias_Type = Float
_Em870minorLowLaserBias_Object = MibTableColumn
em870minorLowLaserBias = _Em870minorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 40),
    _Em870minorLowLaserBias_Type()
)
em870minorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorLowLaserBias.setStatus("mandatory")
_Em870currentValueLaserBias_Type = Float
_Em870currentValueLaserBias_Object = MibTableColumn
em870currentValueLaserBias = _Em870currentValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 41),
    _Em870currentValueLaserBias_Type()
)
em870currentValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870currentValueLaserBias.setStatus("mandatory")


class _Em870stateFlagLaserBias_Type(Integer32):
    """Custom type em870stateFlagLaserBias based on Integer32"""
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


_Em870stateFlagLaserBias_Type.__name__ = "Integer32"
_Em870stateFlagLaserBias_Object = MibTableColumn
em870stateFlagLaserBias = _Em870stateFlagLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 42),
    _Em870stateFlagLaserBias_Type()
)
em870stateFlagLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlagLaserBias.setStatus("mandatory")
_Em870minValueLaserBias_Type = Float
_Em870minValueLaserBias_Object = MibTableColumn
em870minValueLaserBias = _Em870minValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 43),
    _Em870minValueLaserBias_Type()
)
em870minValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minValueLaserBias.setStatus("mandatory")
_Em870maxValueLaserBias_Type = Float
_Em870maxValueLaserBias_Object = MibTableColumn
em870maxValueLaserBias = _Em870maxValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 44),
    _Em870maxValueLaserBias_Type()
)
em870maxValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870maxValueLaserBias.setStatus("mandatory")


class _Em870alarmStateLaserBias_Type(Integer32):
    """Custom type em870alarmStateLaserBias based on Integer32"""
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


_Em870alarmStateLaserBias_Type.__name__ = "Integer32"
_Em870alarmStateLaserBias_Object = MibTableColumn
em870alarmStateLaserBias = _Em870alarmStateLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 45),
    _Em870alarmStateLaserBias_Type()
)
em870alarmStateLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870alarmStateLaserBias.setStatus("mandatory")


class _Em870labelCoolerCurrent_Type(DisplayString):
    """Custom type em870labelCoolerCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelCoolerCurrent_Type.__name__ = "DisplayString"
_Em870labelCoolerCurrent_Object = MibTableColumn
em870labelCoolerCurrent = _Em870labelCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 46),
    _Em870labelCoolerCurrent_Type()
)
em870labelCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelCoolerCurrent.setStatus("optional")


class _Em870uomCoolerCurrent_Type(DisplayString):
    """Custom type em870uomCoolerCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870uomCoolerCurrent_Type.__name__ = "DisplayString"
_Em870uomCoolerCurrent_Object = MibTableColumn
em870uomCoolerCurrent = _Em870uomCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 47),
    _Em870uomCoolerCurrent_Type()
)
em870uomCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870uomCoolerCurrent.setStatus("optional")
_Em870majorHighCoolerCurrent_Type = Float
_Em870majorHighCoolerCurrent_Object = MibTableColumn
em870majorHighCoolerCurrent = _Em870majorHighCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 48),
    _Em870majorHighCoolerCurrent_Type()
)
em870majorHighCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorHighCoolerCurrent.setStatus("mandatory")
_Em870majorLowCoolerCurrent_Type = Float
_Em870majorLowCoolerCurrent_Object = MibTableColumn
em870majorLowCoolerCurrent = _Em870majorLowCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 49),
    _Em870majorLowCoolerCurrent_Type()
)
em870majorLowCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorLowCoolerCurrent.setStatus("mandatory")
_Em870minorHighCoolerCurrent_Type = Float
_Em870minorHighCoolerCurrent_Object = MibTableColumn
em870minorHighCoolerCurrent = _Em870minorHighCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 50),
    _Em870minorHighCoolerCurrent_Type()
)
em870minorHighCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorHighCoolerCurrent.setStatus("mandatory")
_Em870minorLowCoolerCurrent_Type = Float
_Em870minorLowCoolerCurrent_Object = MibTableColumn
em870minorLowCoolerCurrent = _Em870minorLowCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 51),
    _Em870minorLowCoolerCurrent_Type()
)
em870minorLowCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorLowCoolerCurrent.setStatus("mandatory")
_Em870currentValueCoolerCurrent_Type = Float
_Em870currentValueCoolerCurrent_Object = MibTableColumn
em870currentValueCoolerCurrent = _Em870currentValueCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 52),
    _Em870currentValueCoolerCurrent_Type()
)
em870currentValueCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870currentValueCoolerCurrent.setStatus("mandatory")


class _Em870stateFlagCoolerCurrent_Type(Integer32):
    """Custom type em870stateFlagCoolerCurrent based on Integer32"""
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


_Em870stateFlagCoolerCurrent_Type.__name__ = "Integer32"
_Em870stateFlagCoolerCurrent_Object = MibTableColumn
em870stateFlagCoolerCurrent = _Em870stateFlagCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 53),
    _Em870stateFlagCoolerCurrent_Type()
)
em870stateFlagCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlagCoolerCurrent.setStatus("mandatory")
_Em870minValueCoolerCurrent_Type = Float
_Em870minValueCoolerCurrent_Object = MibTableColumn
em870minValueCoolerCurrent = _Em870minValueCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 54),
    _Em870minValueCoolerCurrent_Type()
)
em870minValueCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minValueCoolerCurrent.setStatus("mandatory")
_Em870maxValueCoolerCurrent_Type = Float
_Em870maxValueCoolerCurrent_Object = MibTableColumn
em870maxValueCoolerCurrent = _Em870maxValueCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 55),
    _Em870maxValueCoolerCurrent_Type()
)
em870maxValueCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870maxValueCoolerCurrent.setStatus("mandatory")


class _Em870alarmStateCoolerCurrent_Type(Integer32):
    """Custom type em870alarmStateCoolerCurrent based on Integer32"""
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


_Em870alarmStateCoolerCurrent_Type.__name__ = "Integer32"
_Em870alarmStateCoolerCurrent_Object = MibTableColumn
em870alarmStateCoolerCurrent = _Em870alarmStateCoolerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 56),
    _Em870alarmStateCoolerCurrent_Type()
)
em870alarmStateCoolerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870alarmStateCoolerCurrent.setStatus("mandatory")


class _Em870labelLaserTemp_Type(DisplayString):
    """Custom type em870labelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelLaserTemp_Type.__name__ = "DisplayString"
_Em870labelLaserTemp_Object = MibTableColumn
em870labelLaserTemp = _Em870labelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 57),
    _Em870labelLaserTemp_Type()
)
em870labelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelLaserTemp.setStatus("optional")


class _Em870uomLaserTemp_Type(DisplayString):
    """Custom type em870uomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870uomLaserTemp_Type.__name__ = "DisplayString"
_Em870uomLaserTemp_Object = MibTableColumn
em870uomLaserTemp = _Em870uomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 58),
    _Em870uomLaserTemp_Type()
)
em870uomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870uomLaserTemp.setStatus("optional")
_Em870majorHighLaserTemp_Type = Float
_Em870majorHighLaserTemp_Object = MibTableColumn
em870majorHighLaserTemp = _Em870majorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 59),
    _Em870majorHighLaserTemp_Type()
)
em870majorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorHighLaserTemp.setStatus("mandatory")
_Em870majorLowLaserTemp_Type = Float
_Em870majorLowLaserTemp_Object = MibTableColumn
em870majorLowLaserTemp = _Em870majorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 60),
    _Em870majorLowLaserTemp_Type()
)
em870majorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorLowLaserTemp.setStatus("mandatory")
_Em870minorHighLaserTemp_Type = Float
_Em870minorHighLaserTemp_Object = MibTableColumn
em870minorHighLaserTemp = _Em870minorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 61),
    _Em870minorHighLaserTemp_Type()
)
em870minorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorHighLaserTemp.setStatus("mandatory")
_Em870minorLowLaserTemp_Type = Float
_Em870minorLowLaserTemp_Object = MibTableColumn
em870minorLowLaserTemp = _Em870minorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 62),
    _Em870minorLowLaserTemp_Type()
)
em870minorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorLowLaserTemp.setStatus("mandatory")
_Em870currentValueLaserTemp_Type = Float
_Em870currentValueLaserTemp_Object = MibTableColumn
em870currentValueLaserTemp = _Em870currentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 63),
    _Em870currentValueLaserTemp_Type()
)
em870currentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870currentValueLaserTemp.setStatus("mandatory")


class _Em870stateFlagLaserTemp_Type(Integer32):
    """Custom type em870stateFlagLaserTemp based on Integer32"""
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


_Em870stateFlagLaserTemp_Type.__name__ = "Integer32"
_Em870stateFlagLaserTemp_Object = MibTableColumn
em870stateFlagLaserTemp = _Em870stateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 64),
    _Em870stateFlagLaserTemp_Type()
)
em870stateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlagLaserTemp.setStatus("mandatory")
_Em870minValueLaserTemp_Type = Float
_Em870minValueLaserTemp_Object = MibTableColumn
em870minValueLaserTemp = _Em870minValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 65),
    _Em870minValueLaserTemp_Type()
)
em870minValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minValueLaserTemp.setStatus("mandatory")
_Em870maxValueLaserTemp_Type = Float
_Em870maxValueLaserTemp_Object = MibTableColumn
em870maxValueLaserTemp = _Em870maxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 66),
    _Em870maxValueLaserTemp_Type()
)
em870maxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870maxValueLaserTemp.setStatus("mandatory")


class _Em870alarmStateLaserTemp_Type(Integer32):
    """Custom type em870alarmStateLaserTemp based on Integer32"""
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


_Em870alarmStateLaserTemp_Type.__name__ = "Integer32"
_Em870alarmStateLaserTemp_Object = MibTableColumn
em870alarmStateLaserTemp = _Em870alarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 67),
    _Em870alarmStateLaserTemp_Type()
)
em870alarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870alarmStateLaserTemp.setStatus("mandatory")


class _Em870labelModTemp_Type(DisplayString):
    """Custom type em870labelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelModTemp_Type.__name__ = "DisplayString"
_Em870labelModTemp_Object = MibTableColumn
em870labelModTemp = _Em870labelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 68),
    _Em870labelModTemp_Type()
)
em870labelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelModTemp.setStatus("optional")


class _Em870uomModTemp_Type(DisplayString):
    """Custom type em870uomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870uomModTemp_Type.__name__ = "DisplayString"
_Em870uomModTemp_Object = MibTableColumn
em870uomModTemp = _Em870uomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 69),
    _Em870uomModTemp_Type()
)
em870uomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870uomModTemp.setStatus("optional")
_Em870majorHighModTemp_Type = Float
_Em870majorHighModTemp_Object = MibTableColumn
em870majorHighModTemp = _Em870majorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 70),
    _Em870majorHighModTemp_Type()
)
em870majorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorHighModTemp.setStatus("mandatory")
_Em870majorLowModTemp_Type = Float
_Em870majorLowModTemp_Object = MibTableColumn
em870majorLowModTemp = _Em870majorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 71),
    _Em870majorLowModTemp_Type()
)
em870majorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorLowModTemp.setStatus("mandatory")
_Em870minorHighModTemp_Type = Float
_Em870minorHighModTemp_Object = MibTableColumn
em870minorHighModTemp = _Em870minorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 72),
    _Em870minorHighModTemp_Type()
)
em870minorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorHighModTemp.setStatus("mandatory")
_Em870minorLowModTemp_Type = Float
_Em870minorLowModTemp_Object = MibTableColumn
em870minorLowModTemp = _Em870minorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 73),
    _Em870minorLowModTemp_Type()
)
em870minorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorLowModTemp.setStatus("mandatory")
_Em870currentValueModTemp_Type = Float
_Em870currentValueModTemp_Object = MibTableColumn
em870currentValueModTemp = _Em870currentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 74),
    _Em870currentValueModTemp_Type()
)
em870currentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870currentValueModTemp.setStatus("mandatory")


class _Em870stateFlagModTemp_Type(Integer32):
    """Custom type em870stateFlagModTemp based on Integer32"""
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


_Em870stateFlagModTemp_Type.__name__ = "Integer32"
_Em870stateFlagModTemp_Object = MibTableColumn
em870stateFlagModTemp = _Em870stateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 75),
    _Em870stateFlagModTemp_Type()
)
em870stateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlagModTemp.setStatus("mandatory")
_Em870minValueModTemp_Type = Float
_Em870minValueModTemp_Object = MibTableColumn
em870minValueModTemp = _Em870minValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 76),
    _Em870minValueModTemp_Type()
)
em870minValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minValueModTemp.setStatus("mandatory")
_Em870maxValueModTemp_Type = Float
_Em870maxValueModTemp_Object = MibTableColumn
em870maxValueModTemp = _Em870maxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 77),
    _Em870maxValueModTemp_Type()
)
em870maxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870maxValueModTemp.setStatus("mandatory")


class _Em870alarmStateModTemp_Type(Integer32):
    """Custom type em870alarmStateModTemp based on Integer32"""
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


_Em870alarmStateModTemp_Type.__name__ = "Integer32"
_Em870alarmStateModTemp_Object = MibTableColumn
em870alarmStateModTemp = _Em870alarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 78),
    _Em870alarmStateModTemp_Type()
)
em870alarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870alarmStateModTemp.setStatus("mandatory")


class _Em870labelFanCurrent_Type(DisplayString):
    """Custom type em870labelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelFanCurrent_Type.__name__ = "DisplayString"
_Em870labelFanCurrent_Object = MibTableColumn
em870labelFanCurrent = _Em870labelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 79),
    _Em870labelFanCurrent_Type()
)
em870labelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelFanCurrent.setStatus("optional")


class _Em870uomFanCurrent_Type(DisplayString):
    """Custom type em870uomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870uomFanCurrent_Type.__name__ = "DisplayString"
_Em870uomFanCurrent_Object = MibTableColumn
em870uomFanCurrent = _Em870uomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 80),
    _Em870uomFanCurrent_Type()
)
em870uomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870uomFanCurrent.setStatus("optional")
_Em870majorHighFanCurrent_Type = Float
_Em870majorHighFanCurrent_Object = MibTableColumn
em870majorHighFanCurrent = _Em870majorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 81),
    _Em870majorHighFanCurrent_Type()
)
em870majorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorHighFanCurrent.setStatus("mandatory")
_Em870majorLowFanCurrent_Type = Float
_Em870majorLowFanCurrent_Object = MibTableColumn
em870majorLowFanCurrent = _Em870majorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 82),
    _Em870majorLowFanCurrent_Type()
)
em870majorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorLowFanCurrent.setStatus("mandatory")
_Em870minorHighFanCurrent_Type = Float
_Em870minorHighFanCurrent_Object = MibTableColumn
em870minorHighFanCurrent = _Em870minorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 83),
    _Em870minorHighFanCurrent_Type()
)
em870minorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorHighFanCurrent.setStatus("mandatory")
_Em870minorLowFanCurrent_Type = Float
_Em870minorLowFanCurrent_Object = MibTableColumn
em870minorLowFanCurrent = _Em870minorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 84),
    _Em870minorLowFanCurrent_Type()
)
em870minorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorLowFanCurrent.setStatus("mandatory")
_Em870currentValueFanCurrent_Type = Float
_Em870currentValueFanCurrent_Object = MibTableColumn
em870currentValueFanCurrent = _Em870currentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 85),
    _Em870currentValueFanCurrent_Type()
)
em870currentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870currentValueFanCurrent.setStatus("mandatory")


class _Em870stateFlagFanCurrent_Type(Integer32):
    """Custom type em870stateFlagFanCurrent based on Integer32"""
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


_Em870stateFlagFanCurrent_Type.__name__ = "Integer32"
_Em870stateFlagFanCurrent_Object = MibTableColumn
em870stateFlagFanCurrent = _Em870stateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 86),
    _Em870stateFlagFanCurrent_Type()
)
em870stateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlagFanCurrent.setStatus("mandatory")
_Em870minValueFanCurrent_Type = Float
_Em870minValueFanCurrent_Object = MibTableColumn
em870minValueFanCurrent = _Em870minValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 87),
    _Em870minValueFanCurrent_Type()
)
em870minValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minValueFanCurrent.setStatus("mandatory")
_Em870maxValueFanCurrent_Type = Float
_Em870maxValueFanCurrent_Object = MibTableColumn
em870maxValueFanCurrent = _Em870maxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 88),
    _Em870maxValueFanCurrent_Type()
)
em870maxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870maxValueFanCurrent.setStatus("mandatory")


class _Em870alarmStateFanCurrent_Type(Integer32):
    """Custom type em870alarmStateFanCurrent based on Integer32"""
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


_Em870alarmStateFanCurrent_Type.__name__ = "Integer32"
_Em870alarmStateFanCurrent_Object = MibTableColumn
em870alarmStateFanCurrent = _Em870alarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 89),
    _Em870alarmStateFanCurrent_Type()
)
em870alarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870alarmStateFanCurrent.setStatus("mandatory")


class _Em870label12Volt_Type(DisplayString):
    """Custom type em870label12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870label12Volt_Type.__name__ = "DisplayString"
_Em870label12Volt_Object = MibTableColumn
em870label12Volt = _Em870label12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 90),
    _Em870label12Volt_Type()
)
em870label12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870label12Volt.setStatus("optional")


class _Em870uom12Volt_Type(DisplayString):
    """Custom type em870uom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870uom12Volt_Type.__name__ = "DisplayString"
_Em870uom12Volt_Object = MibTableColumn
em870uom12Volt = _Em870uom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 91),
    _Em870uom12Volt_Type()
)
em870uom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870uom12Volt.setStatus("optional")
_Em870majorHigh12Volt_Type = Float
_Em870majorHigh12Volt_Object = MibTableColumn
em870majorHigh12Volt = _Em870majorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 92),
    _Em870majorHigh12Volt_Type()
)
em870majorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorHigh12Volt.setStatus("mandatory")
_Em870majorLow12Volt_Type = Float
_Em870majorLow12Volt_Object = MibTableColumn
em870majorLow12Volt = _Em870majorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 93),
    _Em870majorLow12Volt_Type()
)
em870majorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870majorLow12Volt.setStatus("mandatory")
_Em870minorHigh12Volt_Type = Float
_Em870minorHigh12Volt_Object = MibTableColumn
em870minorHigh12Volt = _Em870minorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 94),
    _Em870minorHigh12Volt_Type()
)
em870minorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorHigh12Volt.setStatus("mandatory")
_Em870minorLow12Volt_Type = Float
_Em870minorLow12Volt_Object = MibTableColumn
em870minorLow12Volt = _Em870minorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 95),
    _Em870minorLow12Volt_Type()
)
em870minorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minorLow12Volt.setStatus("mandatory")
_Em870currentValue12Volt_Type = Float
_Em870currentValue12Volt_Object = MibTableColumn
em870currentValue12Volt = _Em870currentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 96),
    _Em870currentValue12Volt_Type()
)
em870currentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870currentValue12Volt.setStatus("mandatory")


class _Em870stateFlag12Volt_Type(Integer32):
    """Custom type em870stateFlag12Volt based on Integer32"""
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


_Em870stateFlag12Volt_Type.__name__ = "Integer32"
_Em870stateFlag12Volt_Object = MibTableColumn
em870stateFlag12Volt = _Em870stateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 97),
    _Em870stateFlag12Volt_Type()
)
em870stateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlag12Volt.setStatus("mandatory")
_Em870minValue12Volt_Type = Float
_Em870minValue12Volt_Object = MibTableColumn
em870minValue12Volt = _Em870minValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 98),
    _Em870minValue12Volt_Type()
)
em870minValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870minValue12Volt.setStatus("mandatory")
_Em870maxValue12Volt_Type = Float
_Em870maxValue12Volt_Object = MibTableColumn
em870maxValue12Volt = _Em870maxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 99),
    _Em870maxValue12Volt_Type()
)
em870maxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870maxValue12Volt.setStatus("mandatory")


class _Em870alarmState12Volt_Type(Integer32):
    """Custom type em870alarmState12Volt based on Integer32"""
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


_Em870alarmState12Volt_Type.__name__ = "Integer32"
_Em870alarmState12Volt_Object = MibTableColumn
em870alarmState12Volt = _Em870alarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 2, 1, 100),
    _Em870alarmState12Volt_Type()
)
em870alarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870alarmState12Volt.setStatus("mandatory")
_Gx2Em870DigitalTable_Object = MibTable
gx2Em870DigitalTable = _Gx2Em870DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 3)
)
if mibBuilder.loadTexts:
    gx2Em870DigitalTable.setStatus("mandatory")
_Gx2Em870DigitalEntry_Object = MibTableRow
gx2Em870DigitalEntry = _Gx2Em870DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 3, 4)
)
gx2Em870DigitalEntry.setIndexNames(
    (0, "OMNI-gx2Em870-MIB", "gx2Em870DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Em870DigitalEntry.setStatus("mandatory")


class _Gx2Em870DigitalTableIndex_Type(Integer32):
    """Custom type gx2Em870DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Em870DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Em870DigitalTableIndex_Object = MibTableColumn
gx2Em870DigitalTableIndex = _Gx2Em870DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 3, 4, 1),
    _Gx2Em870DigitalTableIndex_Type()
)
gx2Em870DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Em870DigitalTableIndex.setStatus("mandatory")


class _Em870labelOpticalAlarmSetpoint_Type(DisplayString):
    """Custom type em870labelOpticalAlarmSetpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelOpticalAlarmSetpoint_Type.__name__ = "DisplayString"
_Em870labelOpticalAlarmSetpoint_Object = MibTableColumn
em870labelOpticalAlarmSetpoint = _Em870labelOpticalAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 3, 4, 2),
    _Em870labelOpticalAlarmSetpoint_Type()
)
em870labelOpticalAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelOpticalAlarmSetpoint.setStatus("optional")


class _Em870enumOpticalAlarmSetpoint_Type(DisplayString):
    """Custom type em870enumOpticalAlarmSetpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870enumOpticalAlarmSetpoint_Type.__name__ = "DisplayString"
_Em870enumOpticalAlarmSetpoint_Object = MibTableColumn
em870enumOpticalAlarmSetpoint = _Em870enumOpticalAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 3, 4, 3),
    _Em870enumOpticalAlarmSetpoint_Type()
)
em870enumOpticalAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870enumOpticalAlarmSetpoint.setStatus("optional")


class _Em870valueOpticalAlarmSetpoint_Type(Integer32):
    """Custom type em870valueOpticalAlarmSetpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Em870valueOpticalAlarmSetpoint_Type.__name__ = "Integer32"
_Em870valueOpticalAlarmSetpoint_Object = MibTableColumn
em870valueOpticalAlarmSetpoint = _Em870valueOpticalAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 3, 4, 4),
    _Em870valueOpticalAlarmSetpoint_Type()
)
em870valueOpticalAlarmSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    em870valueOpticalAlarmSetpoint.setStatus("mandatory")


class _Em870stateFlagOpticalAlarmSetpoint_Type(Integer32):
    """Custom type em870stateFlagOpticalAlarmSetpoint based on Integer32"""
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


_Em870stateFlagOpticalAlarmSetpoint_Type.__name__ = "Integer32"
_Em870stateFlagOpticalAlarmSetpoint_Object = MibTableColumn
em870stateFlagOpticalAlarmSetpoint = _Em870stateFlagOpticalAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 3, 4, 5),
    _Em870stateFlagOpticalAlarmSetpoint_Type()
)
em870stateFlagOpticalAlarmSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateFlagOpticalAlarmSetpoint.setStatus("mandatory")
_Gx2Em870StatusTable_Object = MibTable
gx2Em870StatusTable = _Gx2Em870StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4)
)
if mibBuilder.loadTexts:
    gx2Em870StatusTable.setStatus("mandatory")
_Gx2Em870StatusEntry_Object = MibTableRow
gx2Em870StatusEntry = _Gx2Em870StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2)
)
gx2Em870StatusEntry.setIndexNames(
    (0, "OMNI-gx2Em870-MIB", "gx2Em870StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Em870StatusEntry.setStatus("mandatory")


class _Gx2Em870StatusTableIndex_Type(Integer32):
    """Custom type gx2Em870StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Em870StatusTableIndex_Type.__name__ = "Integer32"
_Gx2Em870StatusTableIndex_Object = MibTableColumn
gx2Em870StatusTableIndex = _Gx2Em870StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 1),
    _Gx2Em870StatusTableIndex_Type()
)
gx2Em870StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Em870StatusTableIndex.setStatus("mandatory")


class _Em870labelBoot_Type(DisplayString):
    """Custom type em870labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelBoot_Type.__name__ = "DisplayString"
_Em870labelBoot_Object = MibTableColumn
em870labelBoot = _Em870labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 2),
    _Em870labelBoot_Type()
)
em870labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelBoot.setStatus("optional")


class _Em870valueBoot_Type(Integer32):
    """Custom type em870valueBoot based on Integer32"""
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


_Em870valueBoot_Type.__name__ = "Integer32"
_Em870valueBoot_Object = MibTableColumn
em870valueBoot = _Em870valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 3),
    _Em870valueBoot_Type()
)
em870valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870valueBoot.setStatus("mandatory")


class _Em870stateflagBoot_Type(Integer32):
    """Custom type em870stateflagBoot based on Integer32"""
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


_Em870stateflagBoot_Type.__name__ = "Integer32"
_Em870stateflagBoot_Object = MibTableColumn
em870stateflagBoot = _Em870stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 4),
    _Em870stateflagBoot_Type()
)
em870stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateflagBoot.setStatus("mandatory")


class _Em870labelFlash_Type(DisplayString):
    """Custom type em870labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelFlash_Type.__name__ = "DisplayString"
_Em870labelFlash_Object = MibTableColumn
em870labelFlash = _Em870labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 5),
    _Em870labelFlash_Type()
)
em870labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelFlash.setStatus("optional")


class _Em870valueFlash_Type(Integer32):
    """Custom type em870valueFlash based on Integer32"""
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


_Em870valueFlash_Type.__name__ = "Integer32"
_Em870valueFlash_Object = MibTableColumn
em870valueFlash = _Em870valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 6),
    _Em870valueFlash_Type()
)
em870valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870valueFlash.setStatus("mandatory")


class _Em870stateflagFlash_Type(Integer32):
    """Custom type em870stateflagFlash based on Integer32"""
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


_Em870stateflagFlash_Type.__name__ = "Integer32"
_Em870stateflagFlash_Object = MibTableColumn
em870stateflagFlash = _Em870stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 7),
    _Em870stateflagFlash_Type()
)
em870stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateflagFlash.setStatus("mandatory")


class _Em870labelFactoryDataCRC_Type(DisplayString):
    """Custom type em870labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Em870labelFactoryDataCRC_Object = MibTableColumn
em870labelFactoryDataCRC = _Em870labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 8),
    _Em870labelFactoryDataCRC_Type()
)
em870labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelFactoryDataCRC.setStatus("optional")


class _Em870valueFactoryDataCRC_Type(Integer32):
    """Custom type em870valueFactoryDataCRC based on Integer32"""
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


_Em870valueFactoryDataCRC_Type.__name__ = "Integer32"
_Em870valueFactoryDataCRC_Object = MibTableColumn
em870valueFactoryDataCRC = _Em870valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 9),
    _Em870valueFactoryDataCRC_Type()
)
em870valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870valueFactoryDataCRC.setStatus("mandatory")


class _Em870stateflagFactoryDataCRC_Type(Integer32):
    """Custom type em870stateflagFactoryDataCRC based on Integer32"""
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


_Em870stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Em870stateflagFactoryDataCRC_Object = MibTableColumn
em870stateflagFactoryDataCRC = _Em870stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 10),
    _Em870stateflagFactoryDataCRC_Type()
)
em870stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateflagFactoryDataCRC.setStatus("mandatory")


class _Em870labelAlarmDataCrc_Type(DisplayString):
    """Custom type em870labelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelAlarmDataCrc_Type.__name__ = "DisplayString"
_Em870labelAlarmDataCrc_Object = MibTableColumn
em870labelAlarmDataCrc = _Em870labelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 11),
    _Em870labelAlarmDataCrc_Type()
)
em870labelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelAlarmDataCrc.setStatus("optional")


class _Em870valueAlarmDataCrc_Type(Integer32):
    """Custom type em870valueAlarmDataCrc based on Integer32"""
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


_Em870valueAlarmDataCrc_Type.__name__ = "Integer32"
_Em870valueAlarmDataCrc_Object = MibTableColumn
em870valueAlarmDataCrc = _Em870valueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 12),
    _Em870valueAlarmDataCrc_Type()
)
em870valueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870valueAlarmDataCrc.setStatus("mandatory")


class _Em870stateflagAlarmDataCrc_Type(Integer32):
    """Custom type em870stateflagAlarmDataCrc based on Integer32"""
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


_Em870stateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Em870stateflagAlarmDataCrc_Object = MibTableColumn
em870stateflagAlarmDataCrc = _Em870stateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 13),
    _Em870stateflagAlarmDataCrc_Type()
)
em870stateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateflagAlarmDataCrc.setStatus("mandatory")


class _Em870labelCsoStatus_Type(DisplayString):
    """Custom type em870labelCsoStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870labelCsoStatus_Type.__name__ = "DisplayString"
_Em870labelCsoStatus_Object = MibTableColumn
em870labelCsoStatus = _Em870labelCsoStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 14),
    _Em870labelCsoStatus_Type()
)
em870labelCsoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870labelCsoStatus.setStatus("optional")


class _Em870valueCsoStatus_Type(Integer32):
    """Custom type em870valueCsoStatus based on Integer32"""
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


_Em870valueCsoStatus_Type.__name__ = "Integer32"
_Em870valueCsoStatus_Object = MibTableColumn
em870valueCsoStatus = _Em870valueCsoStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 15),
    _Em870valueCsoStatus_Type()
)
em870valueCsoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870valueCsoStatus.setStatus("mandatory")


class _Em870stateflagCsoStatus_Type(Integer32):
    """Custom type em870stateflagCsoStatus based on Integer32"""
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


_Em870stateflagCsoStatus_Type.__name__ = "Integer32"
_Em870stateflagCsoStatus_Object = MibTableColumn
em870stateflagCsoStatus = _Em870stateflagCsoStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 4, 2, 16),
    _Em870stateflagCsoStatus_Type()
)
em870stateflagCsoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870stateflagCsoStatus.setStatus("mandatory")
_Gx2Em870FactoryTable_Object = MibTable
gx2Em870FactoryTable = _Gx2Em870FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5)
)
if mibBuilder.loadTexts:
    gx2Em870FactoryTable.setStatus("mandatory")
_Gx2Em870FactoryEntry_Object = MibTableRow
gx2Em870FactoryEntry = _Gx2Em870FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3)
)
gx2Em870FactoryEntry.setIndexNames(
    (0, "OMNI-gx2Em870-MIB", "gx2Em870FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Em870FactoryEntry.setStatus("mandatory")


class _Gx2Em870FactoryTableIndex_Type(Integer32):
    """Custom type gx2Em870FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Em870FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Em870FactoryTableIndex_Object = MibTableColumn
gx2Em870FactoryTableIndex = _Gx2Em870FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 1),
    _Gx2Em870FactoryTableIndex_Type()
)
gx2Em870FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Em870FactoryTableIndex.setStatus("mandatory")
_Em870bootControlByte_Type = Integer32
_Em870bootControlByte_Object = MibTableColumn
em870bootControlByte = _Em870bootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 2),
    _Em870bootControlByte_Type()
)
em870bootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870bootControlByte.setStatus("mandatory")
_Em870bootStatusByte_Type = Integer32
_Em870bootStatusByte_Object = MibTableColumn
em870bootStatusByte = _Em870bootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 3),
    _Em870bootStatusByte_Type()
)
em870bootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870bootStatusByte.setStatus("mandatory")
_Em870bank1CRC_Type = Integer32
_Em870bank1CRC_Object = MibTableColumn
em870bank1CRC = _Em870bank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 4),
    _Em870bank1CRC_Type()
)
em870bank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870bank1CRC.setStatus("mandatory")
_Em870bank2CRC_Type = Integer32
_Em870bank2CRC_Object = MibTableColumn
em870bank2CRC = _Em870bank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 5),
    _Em870bank2CRC_Type()
)
em870bank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870bank2CRC.setStatus("mandatory")
_Em870prgEEPROMByte_Type = Integer32
_Em870prgEEPROMByte_Object = MibTableColumn
em870prgEEPROMByte = _Em870prgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 6),
    _Em870prgEEPROMByte_Type()
)
em870prgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870prgEEPROMByte.setStatus("mandatory")
_Em870factoryCRC_Type = Integer32
_Em870factoryCRC_Object = MibTableColumn
em870factoryCRC = _Em870factoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 7),
    _Em870factoryCRC_Type()
)
em870factoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870factoryCRC.setStatus("mandatory")


class _Em870calculateCRC_Type(Integer32):
    """Custom type em870calculateCRC based on Integer32"""
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


_Em870calculateCRC_Type.__name__ = "Integer32"
_Em870calculateCRC_Object = MibTableColumn
em870calculateCRC = _Em870calculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 8),
    _Em870calculateCRC_Type()
)
em870calculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870calculateCRC.setStatus("mandatory")
_Em870hourMeter_Type = Integer32
_Em870hourMeter_Object = MibTableColumn
em870hourMeter = _Em870hourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 9),
    _Em870hourMeter_Type()
)
em870hourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870hourMeter.setStatus("mandatory")
_Em870flashPrgCntA_Type = Integer32
_Em870flashPrgCntA_Object = MibTableColumn
em870flashPrgCntA = _Em870flashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 10),
    _Em870flashPrgCntA_Type()
)
em870flashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870flashPrgCntA.setStatus("mandatory")
_Em870flashPrgCntB_Type = Integer32
_Em870flashPrgCntB_Object = MibTableColumn
em870flashPrgCntB = _Em870flashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 11),
    _Em870flashPrgCntB_Type()
)
em870flashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870flashPrgCntB.setStatus("mandatory")


class _Em870flashBankARev_Type(DisplayString):
    """Custom type em870flashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870flashBankARev_Type.__name__ = "DisplayString"
_Em870flashBankARev_Object = MibTableColumn
em870flashBankARev = _Em870flashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 12),
    _Em870flashBankARev_Type()
)
em870flashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870flashBankARev.setStatus("mandatory")


class _Em870flashBankBRev_Type(DisplayString):
    """Custom type em870flashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Em870flashBankBRev_Type.__name__ = "DisplayString"
_Em870flashBankBRev_Object = MibTableColumn
em870flashBankBRev = _Em870flashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 5, 3, 13),
    _Em870flashBankBRev_Type()
)
em870flashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    em870flashBankBRev.setStatus("mandatory")
_Gx2Em870HoldTimeTable_Object = MibTable
gx2Em870HoldTimeTable = _Gx2Em870HoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 6)
)
if mibBuilder.loadTexts:
    gx2Em870HoldTimeTable.setStatus("mandatory")
_Gx2Em870HoldTimeEntry_Object = MibTableRow
gx2Em870HoldTimeEntry = _Gx2Em870HoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 6, 5)
)
gx2Em870HoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2Em870-MIB", "gx2Em870HoldTimeTableIndex"),
    (0, "OMNI-gx2Em870-MIB", "gx2Em870HoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Em870HoldTimeEntry.setStatus("mandatory")


class _Gx2Em870HoldTimeTableIndex_Type(Integer32):
    """Custom type gx2Em870HoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Em870HoldTimeTableIndex_Type.__name__ = "Integer32"
_Gx2Em870HoldTimeTableIndex_Object = MibTableColumn
gx2Em870HoldTimeTableIndex = _Gx2Em870HoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 6, 5, 1),
    _Gx2Em870HoldTimeTableIndex_Type()
)
gx2Em870HoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Em870HoldTimeTableIndex.setStatus("mandatory")


class _Gx2Em870HoldTimeSpecIndex_Type(Integer32):
    """Custom type gx2Em870HoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Em870HoldTimeSpecIndex_Type.__name__ = "Integer32"
_Gx2Em870HoldTimeSpecIndex_Object = MibTableColumn
gx2Em870HoldTimeSpecIndex = _Gx2Em870HoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 6, 5, 2),
    _Gx2Em870HoldTimeSpecIndex_Type()
)
gx2Em870HoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Em870HoldTimeSpecIndex.setStatus("mandatory")
_Gx2Em870HoldTimeData_Type = Integer32
_Gx2Em870HoldTimeData_Object = MibTableColumn
gx2Em870HoldTimeData = _Gx2Em870HoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 6, 5, 3),
    _Gx2Em870HoldTimeData_Type()
)
gx2Em870HoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gx2Em870HoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapEM870ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 1)
)
trapEM870ConfigChangeInteger.setObjects(
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
    trapEM870ConfigChangeInteger.setStatus(
        ""
    )

trapEM870ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 2)
)
trapEM870ConfigChangeDisplayString.setObjects(
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
    trapEM870ConfigChangeDisplayString.setStatus(
        ""
    )

trapEM870FanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 3)
)
trapEM870FanCurrentAlarm.setObjects(
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
    trapEM870FanCurrentAlarm.setStatus(
        ""
    )

trapEM87012vAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 4)
)
trapEM87012vAlarm.setObjects(
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
    trapEM87012vAlarm.setStatus(
        ""
    )

trapEM870ModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 5)
)
trapEM870ModuleTempAlarm.setObjects(
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
    trapEM870ModuleTempAlarm.setStatus(
        ""
    )

trapEM870OmiOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 6)
)
trapEM870OmiOffsetAlarm.setObjects(
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
    trapEM870OmiOffsetAlarm.setStatus(
        ""
    )

trapEM870OpticalOutputPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 7)
)
trapEM870OpticalOutputPowerAlarm.setObjects(
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
    trapEM870OpticalOutputPowerAlarm.setStatus(
        ""
    )

trapEM870FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 8)
)
trapEM870FlashAlarm.setObjects(
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
    trapEM870FlashAlarm.setStatus(
        ""
    )

trapEM870BankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 9)
)
trapEM870BankBootAlarm.setObjects(
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
    trapEM870BankBootAlarm.setStatus(
        ""
    )

trapEM870AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 10)
)
trapEM870AlarmDataCRCAlarm.setObjects(
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
    trapEM870AlarmDataCRCAlarm.setStatus(
        ""
    )

trapEM870FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12, 0, 11)
)
trapEM870FactoryDataCRCAlarm.setObjects(
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
    trapEM870FactoryDataCRCAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2Em870-MIB",
    **{"Float": Float,
       "trapEM870ConfigChangeInteger": trapEM870ConfigChangeInteger,
       "trapEM870ConfigChangeDisplayString": trapEM870ConfigChangeDisplayString,
       "trapEM870FanCurrentAlarm": trapEM870FanCurrentAlarm,
       "trapEM87012vAlarm": trapEM87012vAlarm,
       "trapEM870ModuleTempAlarm": trapEM870ModuleTempAlarm,
       "trapEM870OmiOffsetAlarm": trapEM870OmiOffsetAlarm,
       "trapEM870OpticalOutputPowerAlarm": trapEM870OpticalOutputPowerAlarm,
       "trapEM870FlashAlarm": trapEM870FlashAlarm,
       "trapEM870BankBootAlarm": trapEM870BankBootAlarm,
       "trapEM870AlarmDataCRCAlarm": trapEM870AlarmDataCRCAlarm,
       "trapEM870FactoryDataCRCAlarm": trapEM870FactoryDataCRCAlarm,
       "gx2Em870Descriptor": gx2Em870Descriptor,
       "gx2Em870AnalogTable": gx2Em870AnalogTable,
       "gx2Em870AnalogEntry": gx2Em870AnalogEntry,
       "gx2Em870AnalogTableIndex": gx2Em870AnalogTableIndex,
       "em870labelOpticalPower": em870labelOpticalPower,
       "em870uomOpticalPower": em870uomOpticalPower,
       "em870majorHighOpticalPower": em870majorHighOpticalPower,
       "em870majorLowOpticalPower": em870majorLowOpticalPower,
       "em870minorHighOpticalPower": em870minorHighOpticalPower,
       "em870minorLowOpticalPower": em870minorLowOpticalPower,
       "em870currentValueOpticalPower": em870currentValueOpticalPower,
       "em870stateFlagOpticalPower": em870stateFlagOpticalPower,
       "em870minValueOpticalPower": em870minValueOpticalPower,
       "em870maxValueOpticalPower": em870maxValueOpticalPower,
       "em870alarmStateOpticalPower": em870alarmStateOpticalPower,
       "em870labelOmiOffset": em870labelOmiOffset,
       "em870uomOmiOffset": em870uomOmiOffset,
       "em870majorHighOmiOffset": em870majorHighOmiOffset,
       "em870majorLowOmiOffset": em870majorLowOmiOffset,
       "em870minorHighOmiOffset": em870minorHighOmiOffset,
       "em870minorLowOmiOffset": em870minorLowOmiOffset,
       "em870currentValueOmiOffset": em870currentValueOmiOffset,
       "em870stateFlagOmiOffset": em870stateFlagOmiOffset,
       "em870minValueOmiOffset": em870minValueOmiOffset,
       "em870maxValueOmiOffset": em870maxValueOmiOffset,
       "em870alarmStateOmiOffset": em870alarmStateOmiOffset,
       "em870labelDFBPower": em870labelDFBPower,
       "em870uomDFBPower": em870uomDFBPower,
       "em870majorHighDFBPower": em870majorHighDFBPower,
       "em870majorLowDFBPower": em870majorLowDFBPower,
       "em870minorHighDFBPower": em870minorHighDFBPower,
       "em870minorLowDFBPower": em870minorLowDFBPower,
       "em870currentValueDFBPower": em870currentValueDFBPower,
       "em870stateFlagDFBPower": em870stateFlagDFBPower,
       "em870minValueDFBPower": em870minValueDFBPower,
       "em870maxValueDFBPower": em870maxValueDFBPower,
       "em870alarmStateDFBPower": em870alarmStateDFBPower,
       "em870labelLaserBias": em870labelLaserBias,
       "em870uomLaserBias": em870uomLaserBias,
       "em870majorHighLaserBias": em870majorHighLaserBias,
       "em870majorLowLaserBias": em870majorLowLaserBias,
       "em870minorHighLaserBias": em870minorHighLaserBias,
       "em870minorLowLaserBias": em870minorLowLaserBias,
       "em870currentValueLaserBias": em870currentValueLaserBias,
       "em870stateFlagLaserBias": em870stateFlagLaserBias,
       "em870minValueLaserBias": em870minValueLaserBias,
       "em870maxValueLaserBias": em870maxValueLaserBias,
       "em870alarmStateLaserBias": em870alarmStateLaserBias,
       "em870labelCoolerCurrent": em870labelCoolerCurrent,
       "em870uomCoolerCurrent": em870uomCoolerCurrent,
       "em870majorHighCoolerCurrent": em870majorHighCoolerCurrent,
       "em870majorLowCoolerCurrent": em870majorLowCoolerCurrent,
       "em870minorHighCoolerCurrent": em870minorHighCoolerCurrent,
       "em870minorLowCoolerCurrent": em870minorLowCoolerCurrent,
       "em870currentValueCoolerCurrent": em870currentValueCoolerCurrent,
       "em870stateFlagCoolerCurrent": em870stateFlagCoolerCurrent,
       "em870minValueCoolerCurrent": em870minValueCoolerCurrent,
       "em870maxValueCoolerCurrent": em870maxValueCoolerCurrent,
       "em870alarmStateCoolerCurrent": em870alarmStateCoolerCurrent,
       "em870labelLaserTemp": em870labelLaserTemp,
       "em870uomLaserTemp": em870uomLaserTemp,
       "em870majorHighLaserTemp": em870majorHighLaserTemp,
       "em870majorLowLaserTemp": em870majorLowLaserTemp,
       "em870minorHighLaserTemp": em870minorHighLaserTemp,
       "em870minorLowLaserTemp": em870minorLowLaserTemp,
       "em870currentValueLaserTemp": em870currentValueLaserTemp,
       "em870stateFlagLaserTemp": em870stateFlagLaserTemp,
       "em870minValueLaserTemp": em870minValueLaserTemp,
       "em870maxValueLaserTemp": em870maxValueLaserTemp,
       "em870alarmStateLaserTemp": em870alarmStateLaserTemp,
       "em870labelModTemp": em870labelModTemp,
       "em870uomModTemp": em870uomModTemp,
       "em870majorHighModTemp": em870majorHighModTemp,
       "em870majorLowModTemp": em870majorLowModTemp,
       "em870minorHighModTemp": em870minorHighModTemp,
       "em870minorLowModTemp": em870minorLowModTemp,
       "em870currentValueModTemp": em870currentValueModTemp,
       "em870stateFlagModTemp": em870stateFlagModTemp,
       "em870minValueModTemp": em870minValueModTemp,
       "em870maxValueModTemp": em870maxValueModTemp,
       "em870alarmStateModTemp": em870alarmStateModTemp,
       "em870labelFanCurrent": em870labelFanCurrent,
       "em870uomFanCurrent": em870uomFanCurrent,
       "em870majorHighFanCurrent": em870majorHighFanCurrent,
       "em870majorLowFanCurrent": em870majorLowFanCurrent,
       "em870minorHighFanCurrent": em870minorHighFanCurrent,
       "em870minorLowFanCurrent": em870minorLowFanCurrent,
       "em870currentValueFanCurrent": em870currentValueFanCurrent,
       "em870stateFlagFanCurrent": em870stateFlagFanCurrent,
       "em870minValueFanCurrent": em870minValueFanCurrent,
       "em870maxValueFanCurrent": em870maxValueFanCurrent,
       "em870alarmStateFanCurrent": em870alarmStateFanCurrent,
       "em870label12Volt": em870label12Volt,
       "em870uom12Volt": em870uom12Volt,
       "em870majorHigh12Volt": em870majorHigh12Volt,
       "em870majorLow12Volt": em870majorLow12Volt,
       "em870minorHigh12Volt": em870minorHigh12Volt,
       "em870minorLow12Volt": em870minorLow12Volt,
       "em870currentValue12Volt": em870currentValue12Volt,
       "em870stateFlag12Volt": em870stateFlag12Volt,
       "em870minValue12Volt": em870minValue12Volt,
       "em870maxValue12Volt": em870maxValue12Volt,
       "em870alarmState12Volt": em870alarmState12Volt,
       "gx2Em870DigitalTable": gx2Em870DigitalTable,
       "gx2Em870DigitalEntry": gx2Em870DigitalEntry,
       "gx2Em870DigitalTableIndex": gx2Em870DigitalTableIndex,
       "em870labelOpticalAlarmSetpoint": em870labelOpticalAlarmSetpoint,
       "em870enumOpticalAlarmSetpoint": em870enumOpticalAlarmSetpoint,
       "em870valueOpticalAlarmSetpoint": em870valueOpticalAlarmSetpoint,
       "em870stateFlagOpticalAlarmSetpoint": em870stateFlagOpticalAlarmSetpoint,
       "gx2Em870StatusTable": gx2Em870StatusTable,
       "gx2Em870StatusEntry": gx2Em870StatusEntry,
       "gx2Em870StatusTableIndex": gx2Em870StatusTableIndex,
       "em870labelBoot": em870labelBoot,
       "em870valueBoot": em870valueBoot,
       "em870stateflagBoot": em870stateflagBoot,
       "em870labelFlash": em870labelFlash,
       "em870valueFlash": em870valueFlash,
       "em870stateflagFlash": em870stateflagFlash,
       "em870labelFactoryDataCRC": em870labelFactoryDataCRC,
       "em870valueFactoryDataCRC": em870valueFactoryDataCRC,
       "em870stateflagFactoryDataCRC": em870stateflagFactoryDataCRC,
       "em870labelAlarmDataCrc": em870labelAlarmDataCrc,
       "em870valueAlarmDataCrc": em870valueAlarmDataCrc,
       "em870stateflagAlarmDataCrc": em870stateflagAlarmDataCrc,
       "em870labelCsoStatus": em870labelCsoStatus,
       "em870valueCsoStatus": em870valueCsoStatus,
       "em870stateflagCsoStatus": em870stateflagCsoStatus,
       "gx2Em870FactoryTable": gx2Em870FactoryTable,
       "gx2Em870FactoryEntry": gx2Em870FactoryEntry,
       "gx2Em870FactoryTableIndex": gx2Em870FactoryTableIndex,
       "em870bootControlByte": em870bootControlByte,
       "em870bootStatusByte": em870bootStatusByte,
       "em870bank1CRC": em870bank1CRC,
       "em870bank2CRC": em870bank2CRC,
       "em870prgEEPROMByte": em870prgEEPROMByte,
       "em870factoryCRC": em870factoryCRC,
       "em870calculateCRC": em870calculateCRC,
       "em870hourMeter": em870hourMeter,
       "em870flashPrgCntA": em870flashPrgCntA,
       "em870flashPrgCntB": em870flashPrgCntB,
       "em870flashBankARev": em870flashBankARev,
       "em870flashBankBRev": em870flashBankBRev,
       "gx2Em870HoldTimeTable": gx2Em870HoldTimeTable,
       "gx2Em870HoldTimeEntry": gx2Em870HoldTimeEntry,
       "gx2Em870HoldTimeTableIndex": gx2Em870HoldTimeTableIndex,
       "gx2Em870HoldTimeSpecIndex": gx2Em870HoldTimeSpecIndex,
       "gx2Em870HoldTimeData": gx2Em870HoldTimeData}
)
