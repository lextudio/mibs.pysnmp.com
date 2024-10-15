# SNMP MIB module (OMNI-gx2Rx085BX4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2Rx085BX4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:35 2024
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

(gx2Rx085BX4,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Rx085BX4")

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

_Gx2Rx085BX4Descriptor_ObjectIdentity = ObjectIdentity
gx2Rx085BX4Descriptor = _Gx2Rx085BX4Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 1)
)
_Gx2Rx085BX4AnalogTable_Object = MibTable
gx2Rx085BX4AnalogTable = _Gx2Rx085BX4AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2)
)
if mibBuilder.loadTexts:
    gx2Rx085BX4AnalogTable.setStatus("mandatory")
_Gx2Rx085BX4AnalogEntry_Object = MibTableRow
gx2Rx085BX4AnalogEntry = _Gx2Rx085BX4AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1)
)
gx2Rx085BX4AnalogEntry.setIndexNames(
    (0, "OMNI-gx2Rx085BX4-MIB", "gx2Rx085BX4AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx085BX4AnalogEntry.setStatus("mandatory")


class _Gx2Rx085BX4AnalogTableIndex_Type(Integer32):
    """Custom type gx2Rx085BX4AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx085BX4AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Rx085BX4AnalogTableIndex_Object = MibTableColumn
gx2Rx085BX4AnalogTableIndex = _Gx2Rx085BX4AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 1),
    _Gx2Rx085BX4AnalogTableIndex_Type()
)
gx2Rx085BX4AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx085BX4AnalogTableIndex.setStatus("mandatory")


class _Rx085labelOptPowerOne_Type(DisplayString):
    """Custom type rx085labelOptPowerOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelOptPowerOne_Type.__name__ = "DisplayString"
_Rx085labelOptPowerOne_Object = MibTableColumn
rx085labelOptPowerOne = _Rx085labelOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 2),
    _Rx085labelOptPowerOne_Type()
)
rx085labelOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelOptPowerOne.setStatus("optional")


class _Rx085uomOptPowerOne_Type(DisplayString):
    """Custom type rx085uomOptPowerOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085uomOptPowerOne_Type.__name__ = "DisplayString"
_Rx085uomOptPowerOne_Object = MibTableColumn
rx085uomOptPowerOne = _Rx085uomOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 3),
    _Rx085uomOptPowerOne_Type()
)
rx085uomOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085uomOptPowerOne.setStatus("optional")
_Rx085majorHighOptPowerOne_Type = Float
_Rx085majorHighOptPowerOne_Object = MibTableColumn
rx085majorHighOptPowerOne = _Rx085majorHighOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 4),
    _Rx085majorHighOptPowerOne_Type()
)
rx085majorHighOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorHighOptPowerOne.setStatus("mandatory")
_Rx085majorLowOptPowerOne_Type = Float
_Rx085majorLowOptPowerOne_Object = MibTableColumn
rx085majorLowOptPowerOne = _Rx085majorLowOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 5),
    _Rx085majorLowOptPowerOne_Type()
)
rx085majorLowOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorLowOptPowerOne.setStatus("mandatory")
_Rx085minorHighOptPowerOne_Type = Float
_Rx085minorHighOptPowerOne_Object = MibTableColumn
rx085minorHighOptPowerOne = _Rx085minorHighOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 6),
    _Rx085minorHighOptPowerOne_Type()
)
rx085minorHighOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorHighOptPowerOne.setStatus("mandatory")
_Rx085minorLowOptPowerOne_Type = Float
_Rx085minorLowOptPowerOne_Object = MibTableColumn
rx085minorLowOptPowerOne = _Rx085minorLowOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 7),
    _Rx085minorLowOptPowerOne_Type()
)
rx085minorLowOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorLowOptPowerOne.setStatus("mandatory")
_Rx085currentValueOptPowerOne_Type = Float
_Rx085currentValueOptPowerOne_Object = MibTableColumn
rx085currentValueOptPowerOne = _Rx085currentValueOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 8),
    _Rx085currentValueOptPowerOne_Type()
)
rx085currentValueOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085currentValueOptPowerOne.setStatus("mandatory")


class _Rx085stateFlagOptPowerOne_Type(Integer32):
    """Custom type rx085stateFlagOptPowerOne based on Integer32"""
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


_Rx085stateFlagOptPowerOne_Type.__name__ = "Integer32"
_Rx085stateFlagOptPowerOne_Object = MibTableColumn
rx085stateFlagOptPowerOne = _Rx085stateFlagOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 9),
    _Rx085stateFlagOptPowerOne_Type()
)
rx085stateFlagOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagOptPowerOne.setStatus("mandatory")
_Rx085minValueOptPowerOne_Type = Float
_Rx085minValueOptPowerOne_Object = MibTableColumn
rx085minValueOptPowerOne = _Rx085minValueOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 10),
    _Rx085minValueOptPowerOne_Type()
)
rx085minValueOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minValueOptPowerOne.setStatus("mandatory")
_Rx085maxValueOptPowerOne_Type = Float
_Rx085maxValueOptPowerOne_Object = MibTableColumn
rx085maxValueOptPowerOne = _Rx085maxValueOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 11),
    _Rx085maxValueOptPowerOne_Type()
)
rx085maxValueOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085maxValueOptPowerOne.setStatus("mandatory")


class _Rx085alarmStateOptPowerOne_Type(Integer32):
    """Custom type rx085alarmStateOptPowerOne based on Integer32"""
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


_Rx085alarmStateOptPowerOne_Type.__name__ = "Integer32"
_Rx085alarmStateOptPowerOne_Object = MibTableColumn
rx085alarmStateOptPowerOne = _Rx085alarmStateOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 12),
    _Rx085alarmStateOptPowerOne_Type()
)
rx085alarmStateOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085alarmStateOptPowerOne.setStatus("mandatory")


class _Rx085labelOptPowerTwo_Type(DisplayString):
    """Custom type rx085labelOptPowerTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelOptPowerTwo_Type.__name__ = "DisplayString"
_Rx085labelOptPowerTwo_Object = MibTableColumn
rx085labelOptPowerTwo = _Rx085labelOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 13),
    _Rx085labelOptPowerTwo_Type()
)
rx085labelOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelOptPowerTwo.setStatus("optional")


class _Rx085uomOptPowerTwo_Type(DisplayString):
    """Custom type rx085uomOptPowerTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085uomOptPowerTwo_Type.__name__ = "DisplayString"
_Rx085uomOptPowerTwo_Object = MibTableColumn
rx085uomOptPowerTwo = _Rx085uomOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 14),
    _Rx085uomOptPowerTwo_Type()
)
rx085uomOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085uomOptPowerTwo.setStatus("optional")
_Rx085majorHighOptPowerTwo_Type = Float
_Rx085majorHighOptPowerTwo_Object = MibTableColumn
rx085majorHighOptPowerTwo = _Rx085majorHighOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 15),
    _Rx085majorHighOptPowerTwo_Type()
)
rx085majorHighOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorHighOptPowerTwo.setStatus("mandatory")
_Rx085majorLowOptPowerTwo_Type = Float
_Rx085majorLowOptPowerTwo_Object = MibTableColumn
rx085majorLowOptPowerTwo = _Rx085majorLowOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 16),
    _Rx085majorLowOptPowerTwo_Type()
)
rx085majorLowOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorLowOptPowerTwo.setStatus("mandatory")
_Rx085minorHighOptPowerTwo_Type = Float
_Rx085minorHighOptPowerTwo_Object = MibTableColumn
rx085minorHighOptPowerTwo = _Rx085minorHighOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 17),
    _Rx085minorHighOptPowerTwo_Type()
)
rx085minorHighOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorHighOptPowerTwo.setStatus("mandatory")
_Rx085minorLowOptPowerTwo_Type = Float
_Rx085minorLowOptPowerTwo_Object = MibTableColumn
rx085minorLowOptPowerTwo = _Rx085minorLowOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 18),
    _Rx085minorLowOptPowerTwo_Type()
)
rx085minorLowOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorLowOptPowerTwo.setStatus("mandatory")
_Rx085currentValueOptPowerTwo_Type = Float
_Rx085currentValueOptPowerTwo_Object = MibTableColumn
rx085currentValueOptPowerTwo = _Rx085currentValueOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 19),
    _Rx085currentValueOptPowerTwo_Type()
)
rx085currentValueOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085currentValueOptPowerTwo.setStatus("mandatory")


class _Rx085stateFlagOptPowerTwo_Type(Integer32):
    """Custom type rx085stateFlagOptPowerTwo based on Integer32"""
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


_Rx085stateFlagOptPowerTwo_Type.__name__ = "Integer32"
_Rx085stateFlagOptPowerTwo_Object = MibTableColumn
rx085stateFlagOptPowerTwo = _Rx085stateFlagOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 20),
    _Rx085stateFlagOptPowerTwo_Type()
)
rx085stateFlagOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagOptPowerTwo.setStatus("mandatory")
_Rx085minValueOptPowerTwo_Type = Float
_Rx085minValueOptPowerTwo_Object = MibTableColumn
rx085minValueOptPowerTwo = _Rx085minValueOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 21),
    _Rx085minValueOptPowerTwo_Type()
)
rx085minValueOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minValueOptPowerTwo.setStatus("mandatory")
_Rx085maxValueOptPowerTwo_Type = Float
_Rx085maxValueOptPowerTwo_Object = MibTableColumn
rx085maxValueOptPowerTwo = _Rx085maxValueOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 22),
    _Rx085maxValueOptPowerTwo_Type()
)
rx085maxValueOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085maxValueOptPowerTwo.setStatus("mandatory")


class _Rx085alarmStateOptPowerTwo_Type(Integer32):
    """Custom type rx085alarmStateOptPowerTwo based on Integer32"""
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


_Rx085alarmStateOptPowerTwo_Type.__name__ = "Integer32"
_Rx085alarmStateOptPowerTwo_Object = MibTableColumn
rx085alarmStateOptPowerTwo = _Rx085alarmStateOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 23),
    _Rx085alarmStateOptPowerTwo_Type()
)
rx085alarmStateOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085alarmStateOptPowerTwo.setStatus("mandatory")


class _Rx085labelOptPowerThree_Type(DisplayString):
    """Custom type rx085labelOptPowerThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelOptPowerThree_Type.__name__ = "DisplayString"
_Rx085labelOptPowerThree_Object = MibTableColumn
rx085labelOptPowerThree = _Rx085labelOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 24),
    _Rx085labelOptPowerThree_Type()
)
rx085labelOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelOptPowerThree.setStatus("optional")


class _Rx085uomOptPowerThree_Type(DisplayString):
    """Custom type rx085uomOptPowerThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085uomOptPowerThree_Type.__name__ = "DisplayString"
_Rx085uomOptPowerThree_Object = MibTableColumn
rx085uomOptPowerThree = _Rx085uomOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 25),
    _Rx085uomOptPowerThree_Type()
)
rx085uomOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085uomOptPowerThree.setStatus("optional")
_Rx085majorHighOptPowerThree_Type = Float
_Rx085majorHighOptPowerThree_Object = MibTableColumn
rx085majorHighOptPowerThree = _Rx085majorHighOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 26),
    _Rx085majorHighOptPowerThree_Type()
)
rx085majorHighOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorHighOptPowerThree.setStatus("mandatory")
_Rx085majorLowOptPowerThree_Type = Float
_Rx085majorLowOptPowerThree_Object = MibTableColumn
rx085majorLowOptPowerThree = _Rx085majorLowOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 27),
    _Rx085majorLowOptPowerThree_Type()
)
rx085majorLowOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorLowOptPowerThree.setStatus("mandatory")
_Rx085minorHighOptPowerThree_Type = Float
_Rx085minorHighOptPowerThree_Object = MibTableColumn
rx085minorHighOptPowerThree = _Rx085minorHighOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 28),
    _Rx085minorHighOptPowerThree_Type()
)
rx085minorHighOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorHighOptPowerThree.setStatus("mandatory")
_Rx085minorLowOptPowerThree_Type = Float
_Rx085minorLowOptPowerThree_Object = MibTableColumn
rx085minorLowOptPowerThree = _Rx085minorLowOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 29),
    _Rx085minorLowOptPowerThree_Type()
)
rx085minorLowOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorLowOptPowerThree.setStatus("mandatory")
_Rx085currentValueOptPowerThree_Type = Float
_Rx085currentValueOptPowerThree_Object = MibTableColumn
rx085currentValueOptPowerThree = _Rx085currentValueOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 30),
    _Rx085currentValueOptPowerThree_Type()
)
rx085currentValueOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085currentValueOptPowerThree.setStatus("mandatory")


class _Rx085stateFlagOptPowerThree_Type(Integer32):
    """Custom type rx085stateFlagOptPowerThree based on Integer32"""
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


_Rx085stateFlagOptPowerThree_Type.__name__ = "Integer32"
_Rx085stateFlagOptPowerThree_Object = MibTableColumn
rx085stateFlagOptPowerThree = _Rx085stateFlagOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 31),
    _Rx085stateFlagOptPowerThree_Type()
)
rx085stateFlagOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagOptPowerThree.setStatus("mandatory")
_Rx085minValueOptPowerThree_Type = Float
_Rx085minValueOptPowerThree_Object = MibTableColumn
rx085minValueOptPowerThree = _Rx085minValueOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 32),
    _Rx085minValueOptPowerThree_Type()
)
rx085minValueOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minValueOptPowerThree.setStatus("mandatory")
_Rx085maxValueOptPowerThree_Type = Float
_Rx085maxValueOptPowerThree_Object = MibTableColumn
rx085maxValueOptPowerThree = _Rx085maxValueOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 33),
    _Rx085maxValueOptPowerThree_Type()
)
rx085maxValueOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085maxValueOptPowerThree.setStatus("mandatory")


class _Rx085alarmStateOptPowerThree_Type(Integer32):
    """Custom type rx085alarmStateOptPowerThree based on Integer32"""
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


_Rx085alarmStateOptPowerThree_Type.__name__ = "Integer32"
_Rx085alarmStateOptPowerThree_Object = MibTableColumn
rx085alarmStateOptPowerThree = _Rx085alarmStateOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 34),
    _Rx085alarmStateOptPowerThree_Type()
)
rx085alarmStateOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085alarmStateOptPowerThree.setStatus("mandatory")


class _Rx085labelOptPowerFour_Type(DisplayString):
    """Custom type rx085labelOptPowerFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelOptPowerFour_Type.__name__ = "DisplayString"
_Rx085labelOptPowerFour_Object = MibTableColumn
rx085labelOptPowerFour = _Rx085labelOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 35),
    _Rx085labelOptPowerFour_Type()
)
rx085labelOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelOptPowerFour.setStatus("optional")


class _Rx085uomOptPowerFour_Type(DisplayString):
    """Custom type rx085uomOptPowerFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085uomOptPowerFour_Type.__name__ = "DisplayString"
_Rx085uomOptPowerFour_Object = MibTableColumn
rx085uomOptPowerFour = _Rx085uomOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 36),
    _Rx085uomOptPowerFour_Type()
)
rx085uomOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085uomOptPowerFour.setStatus("optional")
_Rx085majorHighOptPowerFour_Type = Float
_Rx085majorHighOptPowerFour_Object = MibTableColumn
rx085majorHighOptPowerFour = _Rx085majorHighOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 37),
    _Rx085majorHighOptPowerFour_Type()
)
rx085majorHighOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorHighOptPowerFour.setStatus("mandatory")
_Rx085majorLowOptPowerFour_Type = Float
_Rx085majorLowOptPowerFour_Object = MibTableColumn
rx085majorLowOptPowerFour = _Rx085majorLowOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 38),
    _Rx085majorLowOptPowerFour_Type()
)
rx085majorLowOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorLowOptPowerFour.setStatus("mandatory")
_Rx085minorHighOptPowerFour_Type = Float
_Rx085minorHighOptPowerFour_Object = MibTableColumn
rx085minorHighOptPowerFour = _Rx085minorHighOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 39),
    _Rx085minorHighOptPowerFour_Type()
)
rx085minorHighOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorHighOptPowerFour.setStatus("mandatory")
_Rx085minorLowOptPowerFour_Type = Float
_Rx085minorLowOptPowerFour_Object = MibTableColumn
rx085minorLowOptPowerFour = _Rx085minorLowOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 40),
    _Rx085minorLowOptPowerFour_Type()
)
rx085minorLowOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorLowOptPowerFour.setStatus("mandatory")
_Rx085currentValueOptPowerFour_Type = Float
_Rx085currentValueOptPowerFour_Object = MibTableColumn
rx085currentValueOptPowerFour = _Rx085currentValueOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 41),
    _Rx085currentValueOptPowerFour_Type()
)
rx085currentValueOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085currentValueOptPowerFour.setStatus("mandatory")


class _Rx085stateFlagOptPowerFour_Type(Integer32):
    """Custom type rx085stateFlagOptPowerFour based on Integer32"""
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


_Rx085stateFlagOptPowerFour_Type.__name__ = "Integer32"
_Rx085stateFlagOptPowerFour_Object = MibTableColumn
rx085stateFlagOptPowerFour = _Rx085stateFlagOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 42),
    _Rx085stateFlagOptPowerFour_Type()
)
rx085stateFlagOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagOptPowerFour.setStatus("mandatory")
_Rx085minValueOptPowerFour_Type = Float
_Rx085minValueOptPowerFour_Object = MibTableColumn
rx085minValueOptPowerFour = _Rx085minValueOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 43),
    _Rx085minValueOptPowerFour_Type()
)
rx085minValueOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minValueOptPowerFour.setStatus("mandatory")
_Rx085maxValueOptPowerFour_Type = Float
_Rx085maxValueOptPowerFour_Object = MibTableColumn
rx085maxValueOptPowerFour = _Rx085maxValueOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 44),
    _Rx085maxValueOptPowerFour_Type()
)
rx085maxValueOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085maxValueOptPowerFour.setStatus("mandatory")


class _Rx085alarmStateOptPowerFour_Type(Integer32):
    """Custom type rx085alarmStateOptPowerFour based on Integer32"""
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


_Rx085alarmStateOptPowerFour_Type.__name__ = "Integer32"
_Rx085alarmStateOptPowerFour_Object = MibTableColumn
rx085alarmStateOptPowerFour = _Rx085alarmStateOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 45),
    _Rx085alarmStateOptPowerFour_Type()
)
rx085alarmStateOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085alarmStateOptPowerFour.setStatus("mandatory")


class _Rx085labelModTemp_Type(DisplayString):
    """Custom type rx085labelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelModTemp_Type.__name__ = "DisplayString"
_Rx085labelModTemp_Object = MibTableColumn
rx085labelModTemp = _Rx085labelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 46),
    _Rx085labelModTemp_Type()
)
rx085labelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelModTemp.setStatus("optional")


class _Rx085uomModTemp_Type(DisplayString):
    """Custom type rx085uomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085uomModTemp_Type.__name__ = "DisplayString"
_Rx085uomModTemp_Object = MibTableColumn
rx085uomModTemp = _Rx085uomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 47),
    _Rx085uomModTemp_Type()
)
rx085uomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085uomModTemp.setStatus("optional")
_Rx085majorHighModTemp_Type = Float
_Rx085majorHighModTemp_Object = MibTableColumn
rx085majorHighModTemp = _Rx085majorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 48),
    _Rx085majorHighModTemp_Type()
)
rx085majorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorHighModTemp.setStatus("mandatory")
_Rx085majorLowModTemp_Type = Float
_Rx085majorLowModTemp_Object = MibTableColumn
rx085majorLowModTemp = _Rx085majorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 49),
    _Rx085majorLowModTemp_Type()
)
rx085majorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorLowModTemp.setStatus("mandatory")
_Rx085minorHighModTemp_Type = Float
_Rx085minorHighModTemp_Object = MibTableColumn
rx085minorHighModTemp = _Rx085minorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 50),
    _Rx085minorHighModTemp_Type()
)
rx085minorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorHighModTemp.setStatus("mandatory")
_Rx085minorLowModTemp_Type = Float
_Rx085minorLowModTemp_Object = MibTableColumn
rx085minorLowModTemp = _Rx085minorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 51),
    _Rx085minorLowModTemp_Type()
)
rx085minorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorLowModTemp.setStatus("mandatory")
_Rx085currentValueModTemp_Type = Float
_Rx085currentValueModTemp_Object = MibTableColumn
rx085currentValueModTemp = _Rx085currentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 52),
    _Rx085currentValueModTemp_Type()
)
rx085currentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085currentValueModTemp.setStatus("mandatory")


class _Rx085stateFlagModTemp_Type(Integer32):
    """Custom type rx085stateFlagModTemp based on Integer32"""
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


_Rx085stateFlagModTemp_Type.__name__ = "Integer32"
_Rx085stateFlagModTemp_Object = MibTableColumn
rx085stateFlagModTemp = _Rx085stateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 53),
    _Rx085stateFlagModTemp_Type()
)
rx085stateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagModTemp.setStatus("mandatory")
_Rx085minValueModTemp_Type = Float
_Rx085minValueModTemp_Object = MibTableColumn
rx085minValueModTemp = _Rx085minValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 54),
    _Rx085minValueModTemp_Type()
)
rx085minValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minValueModTemp.setStatus("mandatory")
_Rx085maxValueModTemp_Type = Float
_Rx085maxValueModTemp_Object = MibTableColumn
rx085maxValueModTemp = _Rx085maxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 55),
    _Rx085maxValueModTemp_Type()
)
rx085maxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085maxValueModTemp.setStatus("mandatory")


class _Rx085alarmStateModTemp_Type(Integer32):
    """Custom type rx085alarmStateModTemp based on Integer32"""
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


_Rx085alarmStateModTemp_Type.__name__ = "Integer32"
_Rx085alarmStateModTemp_Object = MibTableColumn
rx085alarmStateModTemp = _Rx085alarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 56),
    _Rx085alarmStateModTemp_Type()
)
rx085alarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085alarmStateModTemp.setStatus("mandatory")


class _Rx085labelFanCurrent_Type(DisplayString):
    """Custom type rx085labelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelFanCurrent_Type.__name__ = "DisplayString"
_Rx085labelFanCurrent_Object = MibTableColumn
rx085labelFanCurrent = _Rx085labelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 57),
    _Rx085labelFanCurrent_Type()
)
rx085labelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelFanCurrent.setStatus("optional")


class _Rx085uomFanCurrent_Type(DisplayString):
    """Custom type rx085uomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085uomFanCurrent_Type.__name__ = "DisplayString"
_Rx085uomFanCurrent_Object = MibTableColumn
rx085uomFanCurrent = _Rx085uomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 58),
    _Rx085uomFanCurrent_Type()
)
rx085uomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085uomFanCurrent.setStatus("optional")
_Rx085majorHighFanCurrent_Type = Float
_Rx085majorHighFanCurrent_Object = MibTableColumn
rx085majorHighFanCurrent = _Rx085majorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 59),
    _Rx085majorHighFanCurrent_Type()
)
rx085majorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorHighFanCurrent.setStatus("mandatory")
_Rx085majorLowFanCurrent_Type = Float
_Rx085majorLowFanCurrent_Object = MibTableColumn
rx085majorLowFanCurrent = _Rx085majorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 60),
    _Rx085majorLowFanCurrent_Type()
)
rx085majorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorLowFanCurrent.setStatus("mandatory")
_Rx085minorHighFanCurrent_Type = Float
_Rx085minorHighFanCurrent_Object = MibTableColumn
rx085minorHighFanCurrent = _Rx085minorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 61),
    _Rx085minorHighFanCurrent_Type()
)
rx085minorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorHighFanCurrent.setStatus("mandatory")
_Rx085minorLowFanCurrent_Type = Float
_Rx085minorLowFanCurrent_Object = MibTableColumn
rx085minorLowFanCurrent = _Rx085minorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 62),
    _Rx085minorLowFanCurrent_Type()
)
rx085minorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorLowFanCurrent.setStatus("mandatory")
_Rx085currentValueFanCurrent_Type = Float
_Rx085currentValueFanCurrent_Object = MibTableColumn
rx085currentValueFanCurrent = _Rx085currentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 63),
    _Rx085currentValueFanCurrent_Type()
)
rx085currentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085currentValueFanCurrent.setStatus("mandatory")


class _Rx085stateFlagFanCurrent_Type(Integer32):
    """Custom type rx085stateFlagFanCurrent based on Integer32"""
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


_Rx085stateFlagFanCurrent_Type.__name__ = "Integer32"
_Rx085stateFlagFanCurrent_Object = MibTableColumn
rx085stateFlagFanCurrent = _Rx085stateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 64),
    _Rx085stateFlagFanCurrent_Type()
)
rx085stateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagFanCurrent.setStatus("mandatory")
_Rx085minValueFanCurrent_Type = Float
_Rx085minValueFanCurrent_Object = MibTableColumn
rx085minValueFanCurrent = _Rx085minValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 65),
    _Rx085minValueFanCurrent_Type()
)
rx085minValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minValueFanCurrent.setStatus("mandatory")
_Rx085maxValueFanCurrent_Type = Float
_Rx085maxValueFanCurrent_Object = MibTableColumn
rx085maxValueFanCurrent = _Rx085maxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 66),
    _Rx085maxValueFanCurrent_Type()
)
rx085maxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085maxValueFanCurrent.setStatus("mandatory")


class _Rx085alarmStateFanCurrent_Type(Integer32):
    """Custom type rx085alarmStateFanCurrent based on Integer32"""
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


_Rx085alarmStateFanCurrent_Type.__name__ = "Integer32"
_Rx085alarmStateFanCurrent_Object = MibTableColumn
rx085alarmStateFanCurrent = _Rx085alarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 67),
    _Rx085alarmStateFanCurrent_Type()
)
rx085alarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085alarmStateFanCurrent.setStatus("mandatory")


class _Rx085label12Volt_Type(DisplayString):
    """Custom type rx085label12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085label12Volt_Type.__name__ = "DisplayString"
_Rx085label12Volt_Object = MibTableColumn
rx085label12Volt = _Rx085label12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 68),
    _Rx085label12Volt_Type()
)
rx085label12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085label12Volt.setStatus("optional")


class _Rx085uom12Volt_Type(DisplayString):
    """Custom type rx085uom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085uom12Volt_Type.__name__ = "DisplayString"
_Rx085uom12Volt_Object = MibTableColumn
rx085uom12Volt = _Rx085uom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 69),
    _Rx085uom12Volt_Type()
)
rx085uom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085uom12Volt.setStatus("optional")
_Rx085majorHigh12Volt_Type = Float
_Rx085majorHigh12Volt_Object = MibTableColumn
rx085majorHigh12Volt = _Rx085majorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 70),
    _Rx085majorHigh12Volt_Type()
)
rx085majorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorHigh12Volt.setStatus("mandatory")
_Rx085majorLow12Volt_Type = Float
_Rx085majorLow12Volt_Object = MibTableColumn
rx085majorLow12Volt = _Rx085majorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 71),
    _Rx085majorLow12Volt_Type()
)
rx085majorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085majorLow12Volt.setStatus("mandatory")
_Rx085minorHigh12Volt_Type = Float
_Rx085minorHigh12Volt_Object = MibTableColumn
rx085minorHigh12Volt = _Rx085minorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 72),
    _Rx085minorHigh12Volt_Type()
)
rx085minorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorHigh12Volt.setStatus("mandatory")
_Rx085minorLow12Volt_Type = Float
_Rx085minorLow12Volt_Object = MibTableColumn
rx085minorLow12Volt = _Rx085minorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 73),
    _Rx085minorLow12Volt_Type()
)
rx085minorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minorLow12Volt.setStatus("mandatory")
_Rx085currentValue12Volt_Type = Float
_Rx085currentValue12Volt_Object = MibTableColumn
rx085currentValue12Volt = _Rx085currentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 74),
    _Rx085currentValue12Volt_Type()
)
rx085currentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085currentValue12Volt.setStatus("mandatory")


class _Rx085stateFlag12Volt_Type(Integer32):
    """Custom type rx085stateFlag12Volt based on Integer32"""
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


_Rx085stateFlag12Volt_Type.__name__ = "Integer32"
_Rx085stateFlag12Volt_Object = MibTableColumn
rx085stateFlag12Volt = _Rx085stateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 75),
    _Rx085stateFlag12Volt_Type()
)
rx085stateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlag12Volt.setStatus("mandatory")
_Rx085minValue12Volt_Type = Float
_Rx085minValue12Volt_Object = MibTableColumn
rx085minValue12Volt = _Rx085minValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 76),
    _Rx085minValue12Volt_Type()
)
rx085minValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085minValue12Volt.setStatus("mandatory")
_Rx085maxValue12Volt_Type = Float
_Rx085maxValue12Volt_Object = MibTableColumn
rx085maxValue12Volt = _Rx085maxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 77),
    _Rx085maxValue12Volt_Type()
)
rx085maxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085maxValue12Volt.setStatus("mandatory")


class _Rx085alarmState12Volt_Type(Integer32):
    """Custom type rx085alarmState12Volt based on Integer32"""
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


_Rx085alarmState12Volt_Type.__name__ = "Integer32"
_Rx085alarmState12Volt_Object = MibTableColumn
rx085alarmState12Volt = _Rx085alarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 2, 1, 78),
    _Rx085alarmState12Volt_Type()
)
rx085alarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085alarmState12Volt.setStatus("mandatory")
_Gx2Rx085BX4DigitalTable_Object = MibTable
gx2Rx085BX4DigitalTable = _Gx2Rx085BX4DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3)
)
if mibBuilder.loadTexts:
    gx2Rx085BX4DigitalTable.setStatus("mandatory")
_Gx2Rx085BX4DigitalEntry_Object = MibTableRow
gx2Rx085BX4DigitalEntry = _Gx2Rx085BX4DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2)
)
gx2Rx085BX4DigitalEntry.setIndexNames(
    (0, "OMNI-gx2Rx085BX4-MIB", "gx2Rx085BX4DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx085BX4DigitalEntry.setStatus("mandatory")


class _Gx2Rx085BX4DigitalTableIndex_Type(Integer32):
    """Custom type gx2Rx085BX4DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx085BX4DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Rx085BX4DigitalTableIndex_Object = MibTableColumn
gx2Rx085BX4DigitalTableIndex = _Gx2Rx085BX4DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 1),
    _Gx2Rx085BX4DigitalTableIndex_Type()
)
gx2Rx085BX4DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx085BX4DigitalTableIndex.setStatus("mandatory")


class _Rx085labelModeOne_Type(DisplayString):
    """Custom type rx085labelModeOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelModeOne_Type.__name__ = "DisplayString"
_Rx085labelModeOne_Object = MibTableColumn
rx085labelModeOne = _Rx085labelModeOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 2),
    _Rx085labelModeOne_Type()
)
rx085labelModeOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelModeOne.setStatus("optional")


class _Rx085enumModeOne_Type(DisplayString):
    """Custom type rx085enumModeOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumModeOne_Type.__name__ = "DisplayString"
_Rx085enumModeOne_Object = MibTableColumn
rx085enumModeOne = _Rx085enumModeOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 3),
    _Rx085enumModeOne_Type()
)
rx085enumModeOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumModeOne.setStatus("optional")


class _Rx085valueModeOne_Type(Integer32):
    """Custom type rx085valueModeOne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("agc", 3),
          ("manual", 2),
          ("off", 1))
    )


_Rx085valueModeOne_Type.__name__ = "Integer32"
_Rx085valueModeOne_Object = MibTableColumn
rx085valueModeOne = _Rx085valueModeOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 4),
    _Rx085valueModeOne_Type()
)
rx085valueModeOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueModeOne.setStatus("mandatory")


class _Rx085stateFlagModeOne_Type(Integer32):
    """Custom type rx085stateFlagModeOne based on Integer32"""
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


_Rx085stateFlagModeOne_Type.__name__ = "Integer32"
_Rx085stateFlagModeOne_Object = MibTableColumn
rx085stateFlagModeOne = _Rx085stateFlagModeOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 5),
    _Rx085stateFlagModeOne_Type()
)
rx085stateFlagModeOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagModeOne.setStatus("mandatory")


class _Rx085labelWavelengthOne_Type(DisplayString):
    """Custom type rx085labelWavelengthOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelWavelengthOne_Type.__name__ = "DisplayString"
_Rx085labelWavelengthOne_Object = MibTableColumn
rx085labelWavelengthOne = _Rx085labelWavelengthOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 6),
    _Rx085labelWavelengthOne_Type()
)
rx085labelWavelengthOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelWavelengthOne.setStatus("optional")


class _Rx085enumWavelengthOne_Type(DisplayString):
    """Custom type rx085enumWavelengthOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumWavelengthOne_Type.__name__ = "DisplayString"
_Rx085enumWavelengthOne_Object = MibTableColumn
rx085enumWavelengthOne = _Rx085enumWavelengthOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 7),
    _Rx085enumWavelengthOne_Type()
)
rx085enumWavelengthOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumWavelengthOne.setStatus("optional")


class _Rx085valueWavelengthOne_Type(Integer32):
    """Custom type rx085valueWavelengthOne based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("nM1270", 1),
          ("nM1290", 2),
          ("nM1310", 3),
          ("nM1330", 4),
          ("nM1350", 5),
          ("nM1370", 6),
          ("nM1390", 7),
          ("nM1410", 8),
          ("nM1430", 9),
          ("nM1450", 10),
          ("nM1470", 11),
          ("nM1490", 12),
          ("nM1510", 13),
          ("nM1530", 14),
          ("nM1550", 15),
          ("nM1570", 16),
          ("nM1590", 17),
          ("nM1610", 18))
    )


_Rx085valueWavelengthOne_Type.__name__ = "Integer32"
_Rx085valueWavelengthOne_Object = MibTableColumn
rx085valueWavelengthOne = _Rx085valueWavelengthOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 8),
    _Rx085valueWavelengthOne_Type()
)
rx085valueWavelengthOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueWavelengthOne.setStatus("mandatory")


class _Rx085stateFlagWavelengthOne_Type(Integer32):
    """Custom type rx085stateFlagWavelengthOne based on Integer32"""
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


_Rx085stateFlagWavelengthOne_Type.__name__ = "Integer32"
_Rx085stateFlagWavelengthOne_Object = MibTableColumn
rx085stateFlagWavelengthOne = _Rx085stateFlagWavelengthOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 9),
    _Rx085stateFlagWavelengthOne_Type()
)
rx085stateFlagWavelengthOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagWavelengthOne.setStatus("mandatory")


class _Rx085labelAttnSettingOne_Type(DisplayString):
    """Custom type rx085labelAttnSettingOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelAttnSettingOne_Type.__name__ = "DisplayString"
_Rx085labelAttnSettingOne_Object = MibTableColumn
rx085labelAttnSettingOne = _Rx085labelAttnSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 10),
    _Rx085labelAttnSettingOne_Type()
)
rx085labelAttnSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelAttnSettingOne.setStatus("optional")


class _Rx085enumAttnSettingOne_Type(DisplayString):
    """Custom type rx085enumAttnSettingOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumAttnSettingOne_Type.__name__ = "DisplayString"
_Rx085enumAttnSettingOne_Object = MibTableColumn
rx085enumAttnSettingOne = _Rx085enumAttnSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 11),
    _Rx085enumAttnSettingOne_Type()
)
rx085enumAttnSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumAttnSettingOne.setStatus("optional")
_Rx085valueAttnSettingOne_Type = Integer32
_Rx085valueAttnSettingOne_Object = MibTableColumn
rx085valueAttnSettingOne = _Rx085valueAttnSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 12),
    _Rx085valueAttnSettingOne_Type()
)
rx085valueAttnSettingOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueAttnSettingOne.setStatus("mandatory")


class _Rx085stateFlagAttnSettingOne_Type(Integer32):
    """Custom type rx085stateFlagAttnSettingOne based on Integer32"""
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


_Rx085stateFlagAttnSettingOne_Type.__name__ = "Integer32"
_Rx085stateFlagAttnSettingOne_Object = MibTableColumn
rx085stateFlagAttnSettingOne = _Rx085stateFlagAttnSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 13),
    _Rx085stateFlagAttnSettingOne_Type()
)
rx085stateFlagAttnSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagAttnSettingOne.setStatus("mandatory")


class _Rx085labelSwModeSettingOne_Type(DisplayString):
    """Custom type rx085labelSwModeSettingOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelSwModeSettingOne_Type.__name__ = "DisplayString"
_Rx085labelSwModeSettingOne_Object = MibTableColumn
rx085labelSwModeSettingOne = _Rx085labelSwModeSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 14),
    _Rx085labelSwModeSettingOne_Type()
)
rx085labelSwModeSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelSwModeSettingOne.setStatus("optional")


class _Rx085enumSwModeSettingOne_Type(DisplayString):
    """Custom type rx085enumSwModeSettingOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumSwModeSettingOne_Type.__name__ = "DisplayString"
_Rx085enumSwModeSettingOne_Object = MibTableColumn
rx085enumSwModeSettingOne = _Rx085enumSwModeSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 15),
    _Rx085enumSwModeSettingOne_Type()
)
rx085enumSwModeSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumSwModeSettingOne.setStatus("optional")


class _Rx085valueSwModeSettingOne_Type(Integer32):
    """Custom type rx085valueSwModeSettingOne based on Integer32"""
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


_Rx085valueSwModeSettingOne_Type.__name__ = "Integer32"
_Rx085valueSwModeSettingOne_Object = MibTableColumn
rx085valueSwModeSettingOne = _Rx085valueSwModeSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 16),
    _Rx085valueSwModeSettingOne_Type()
)
rx085valueSwModeSettingOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueSwModeSettingOne.setStatus("mandatory")


class _Rx085stateFlagSwModeSettingOne_Type(Integer32):
    """Custom type rx085stateFlagSwModeSettingOne based on Integer32"""
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


_Rx085stateFlagSwModeSettingOne_Type.__name__ = "Integer32"
_Rx085stateFlagSwModeSettingOne_Object = MibTableColumn
rx085stateFlagSwModeSettingOne = _Rx085stateFlagSwModeSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 17),
    _Rx085stateFlagSwModeSettingOne_Type()
)
rx085stateFlagSwModeSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagSwModeSettingOne.setStatus("mandatory")


class _Rx085labelSwModeThresholdOne_Type(DisplayString):
    """Custom type rx085labelSwModeThresholdOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelSwModeThresholdOne_Type.__name__ = "DisplayString"
_Rx085labelSwModeThresholdOne_Object = MibTableColumn
rx085labelSwModeThresholdOne = _Rx085labelSwModeThresholdOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 18),
    _Rx085labelSwModeThresholdOne_Type()
)
rx085labelSwModeThresholdOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelSwModeThresholdOne.setStatus("optional")


class _Rx085enumSwModeThresholdOne_Type(DisplayString):
    """Custom type rx085enumSwModeThresholdOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumSwModeThresholdOne_Type.__name__ = "DisplayString"
_Rx085enumSwModeThresholdOne_Object = MibTableColumn
rx085enumSwModeThresholdOne = _Rx085enumSwModeThresholdOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 19),
    _Rx085enumSwModeThresholdOne_Type()
)
rx085enumSwModeThresholdOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumSwModeThresholdOne.setStatus("optional")
_Rx085valueSwModeThresholdOne_Type = Integer32
_Rx085valueSwModeThresholdOne_Object = MibTableColumn
rx085valueSwModeThresholdOne = _Rx085valueSwModeThresholdOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 20),
    _Rx085valueSwModeThresholdOne_Type()
)
rx085valueSwModeThresholdOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueSwModeThresholdOne.setStatus("mandatory")


class _Rx085stateFlagSwModeThresholdOne_Type(Integer32):
    """Custom type rx085stateFlagSwModeThresholdOne based on Integer32"""
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


_Rx085stateFlagSwModeThresholdOne_Type.__name__ = "Integer32"
_Rx085stateFlagSwModeThresholdOne_Object = MibTableColumn
rx085stateFlagSwModeThresholdOne = _Rx085stateFlagSwModeThresholdOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 21),
    _Rx085stateFlagSwModeThresholdOne_Type()
)
rx085stateFlagSwModeThresholdOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagSwModeThresholdOne.setStatus("mandatory")


class _Rx085labelModeTwo_Type(DisplayString):
    """Custom type rx085labelModeTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelModeTwo_Type.__name__ = "DisplayString"
_Rx085labelModeTwo_Object = MibTableColumn
rx085labelModeTwo = _Rx085labelModeTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 22),
    _Rx085labelModeTwo_Type()
)
rx085labelModeTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelModeTwo.setStatus("optional")


class _Rx085enumModeTwo_Type(DisplayString):
    """Custom type rx085enumModeTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumModeTwo_Type.__name__ = "DisplayString"
_Rx085enumModeTwo_Object = MibTableColumn
rx085enumModeTwo = _Rx085enumModeTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 23),
    _Rx085enumModeTwo_Type()
)
rx085enumModeTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumModeTwo.setStatus("optional")


class _Rx085valueModeTwo_Type(Integer32):
    """Custom type rx085valueModeTwo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("agc", 3),
          ("manual", 2),
          ("off", 1))
    )


_Rx085valueModeTwo_Type.__name__ = "Integer32"
_Rx085valueModeTwo_Object = MibTableColumn
rx085valueModeTwo = _Rx085valueModeTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 24),
    _Rx085valueModeTwo_Type()
)
rx085valueModeTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueModeTwo.setStatus("mandatory")


class _Rx085stateFlagModeTwo_Type(Integer32):
    """Custom type rx085stateFlagModeTwo based on Integer32"""
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


_Rx085stateFlagModeTwo_Type.__name__ = "Integer32"
_Rx085stateFlagModeTwo_Object = MibTableColumn
rx085stateFlagModeTwo = _Rx085stateFlagModeTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 25),
    _Rx085stateFlagModeTwo_Type()
)
rx085stateFlagModeTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagModeTwo.setStatus("mandatory")


class _Rx085labelWavelengthTwo_Type(DisplayString):
    """Custom type rx085labelWavelengthTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelWavelengthTwo_Type.__name__ = "DisplayString"
_Rx085labelWavelengthTwo_Object = MibTableColumn
rx085labelWavelengthTwo = _Rx085labelWavelengthTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 26),
    _Rx085labelWavelengthTwo_Type()
)
rx085labelWavelengthTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelWavelengthTwo.setStatus("optional")


class _Rx085enumWavelengthTwo_Type(DisplayString):
    """Custom type rx085enumWavelengthTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumWavelengthTwo_Type.__name__ = "DisplayString"
_Rx085enumWavelengthTwo_Object = MibTableColumn
rx085enumWavelengthTwo = _Rx085enumWavelengthTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 27),
    _Rx085enumWavelengthTwo_Type()
)
rx085enumWavelengthTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumWavelengthTwo.setStatus("optional")


class _Rx085valueWavelengthTwo_Type(Integer32):
    """Custom type rx085valueWavelengthTwo based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("nM1270", 1),
          ("nM1290", 2),
          ("nM1310", 3),
          ("nM1330", 4),
          ("nM1350", 5),
          ("nM1370", 6),
          ("nM1390", 7),
          ("nM1410", 8),
          ("nM1430", 9),
          ("nM1450", 10),
          ("nM1470", 11),
          ("nM1490", 12),
          ("nM1510", 13),
          ("nM1530", 14),
          ("nM1550", 15),
          ("nM1570", 16),
          ("nM1590", 17),
          ("nM1610", 18))
    )


_Rx085valueWavelengthTwo_Type.__name__ = "Integer32"
_Rx085valueWavelengthTwo_Object = MibTableColumn
rx085valueWavelengthTwo = _Rx085valueWavelengthTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 28),
    _Rx085valueWavelengthTwo_Type()
)
rx085valueWavelengthTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueWavelengthTwo.setStatus("mandatory")


class _Rx085stateFlagWavelengthTwo_Type(Integer32):
    """Custom type rx085stateFlagWavelengthTwo based on Integer32"""
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


_Rx085stateFlagWavelengthTwo_Type.__name__ = "Integer32"
_Rx085stateFlagWavelengthTwo_Object = MibTableColumn
rx085stateFlagWavelengthTwo = _Rx085stateFlagWavelengthTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 29),
    _Rx085stateFlagWavelengthTwo_Type()
)
rx085stateFlagWavelengthTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagWavelengthTwo.setStatus("mandatory")


class _Rx085labelAttnSettingTwo_Type(DisplayString):
    """Custom type rx085labelAttnSettingTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelAttnSettingTwo_Type.__name__ = "DisplayString"
_Rx085labelAttnSettingTwo_Object = MibTableColumn
rx085labelAttnSettingTwo = _Rx085labelAttnSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 30),
    _Rx085labelAttnSettingTwo_Type()
)
rx085labelAttnSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelAttnSettingTwo.setStatus("optional")


class _Rx085enumAttnSettingTwo_Type(DisplayString):
    """Custom type rx085enumAttnSettingTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumAttnSettingTwo_Type.__name__ = "DisplayString"
_Rx085enumAttnSettingTwo_Object = MibTableColumn
rx085enumAttnSettingTwo = _Rx085enumAttnSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 31),
    _Rx085enumAttnSettingTwo_Type()
)
rx085enumAttnSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumAttnSettingTwo.setStatus("optional")
_Rx085valueAttnSettingTwo_Type = Integer32
_Rx085valueAttnSettingTwo_Object = MibTableColumn
rx085valueAttnSettingTwo = _Rx085valueAttnSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 32),
    _Rx085valueAttnSettingTwo_Type()
)
rx085valueAttnSettingTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueAttnSettingTwo.setStatus("mandatory")


class _Rx085stateFlagAttnSettingTwo_Type(Integer32):
    """Custom type rx085stateFlagAttnSettingTwo based on Integer32"""
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


_Rx085stateFlagAttnSettingTwo_Type.__name__ = "Integer32"
_Rx085stateFlagAttnSettingTwo_Object = MibTableColumn
rx085stateFlagAttnSettingTwo = _Rx085stateFlagAttnSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 33),
    _Rx085stateFlagAttnSettingTwo_Type()
)
rx085stateFlagAttnSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagAttnSettingTwo.setStatus("mandatory")


class _Rx085labelSwModeSettingTwo_Type(DisplayString):
    """Custom type rx085labelSwModeSettingTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelSwModeSettingTwo_Type.__name__ = "DisplayString"
_Rx085labelSwModeSettingTwo_Object = MibTableColumn
rx085labelSwModeSettingTwo = _Rx085labelSwModeSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 34),
    _Rx085labelSwModeSettingTwo_Type()
)
rx085labelSwModeSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelSwModeSettingTwo.setStatus("optional")


class _Rx085enumSwModeSettingTwo_Type(DisplayString):
    """Custom type rx085enumSwModeSettingTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumSwModeSettingTwo_Type.__name__ = "DisplayString"
_Rx085enumSwModeSettingTwo_Object = MibTableColumn
rx085enumSwModeSettingTwo = _Rx085enumSwModeSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 35),
    _Rx085enumSwModeSettingTwo_Type()
)
rx085enumSwModeSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumSwModeSettingTwo.setStatus("optional")


class _Rx085valueSwModeSettingTwo_Type(Integer32):
    """Custom type rx085valueSwModeSettingTwo based on Integer32"""
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


_Rx085valueSwModeSettingTwo_Type.__name__ = "Integer32"
_Rx085valueSwModeSettingTwo_Object = MibTableColumn
rx085valueSwModeSettingTwo = _Rx085valueSwModeSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 36),
    _Rx085valueSwModeSettingTwo_Type()
)
rx085valueSwModeSettingTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueSwModeSettingTwo.setStatus("mandatory")


class _Rx085stateFlagSwModeSettingTwo_Type(Integer32):
    """Custom type rx085stateFlagSwModeSettingTwo based on Integer32"""
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


_Rx085stateFlagSwModeSettingTwo_Type.__name__ = "Integer32"
_Rx085stateFlagSwModeSettingTwo_Object = MibTableColumn
rx085stateFlagSwModeSettingTwo = _Rx085stateFlagSwModeSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 37),
    _Rx085stateFlagSwModeSettingTwo_Type()
)
rx085stateFlagSwModeSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagSwModeSettingTwo.setStatus("mandatory")


class _Rx085labelSwModeThresholdTwo_Type(DisplayString):
    """Custom type rx085labelSwModeThresholdTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelSwModeThresholdTwo_Type.__name__ = "DisplayString"
_Rx085labelSwModeThresholdTwo_Object = MibTableColumn
rx085labelSwModeThresholdTwo = _Rx085labelSwModeThresholdTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 38),
    _Rx085labelSwModeThresholdTwo_Type()
)
rx085labelSwModeThresholdTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelSwModeThresholdTwo.setStatus("optional")


class _Rx085enumSwModeThresholdTwo_Type(DisplayString):
    """Custom type rx085enumSwModeThresholdTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumSwModeThresholdTwo_Type.__name__ = "DisplayString"
_Rx085enumSwModeThresholdTwo_Object = MibTableColumn
rx085enumSwModeThresholdTwo = _Rx085enumSwModeThresholdTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 39),
    _Rx085enumSwModeThresholdTwo_Type()
)
rx085enumSwModeThresholdTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumSwModeThresholdTwo.setStatus("optional")
_Rx085valueSwModeThresholdTwo_Type = Integer32
_Rx085valueSwModeThresholdTwo_Object = MibTableColumn
rx085valueSwModeThresholdTwo = _Rx085valueSwModeThresholdTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 40),
    _Rx085valueSwModeThresholdTwo_Type()
)
rx085valueSwModeThresholdTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueSwModeThresholdTwo.setStatus("mandatory")


class _Rx085stateFlagSwModeThresholdTwo_Type(Integer32):
    """Custom type rx085stateFlagSwModeThresholdTwo based on Integer32"""
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


_Rx085stateFlagSwModeThresholdTwo_Type.__name__ = "Integer32"
_Rx085stateFlagSwModeThresholdTwo_Object = MibTableColumn
rx085stateFlagSwModeThresholdTwo = _Rx085stateFlagSwModeThresholdTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 41),
    _Rx085stateFlagSwModeThresholdTwo_Type()
)
rx085stateFlagSwModeThresholdTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagSwModeThresholdTwo.setStatus("mandatory")


class _Rx085labelModeThree_Type(DisplayString):
    """Custom type rx085labelModeThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelModeThree_Type.__name__ = "DisplayString"
_Rx085labelModeThree_Object = MibTableColumn
rx085labelModeThree = _Rx085labelModeThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 42),
    _Rx085labelModeThree_Type()
)
rx085labelModeThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelModeThree.setStatus("optional")


class _Rx085enumModeThree_Type(DisplayString):
    """Custom type rx085enumModeThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumModeThree_Type.__name__ = "DisplayString"
_Rx085enumModeThree_Object = MibTableColumn
rx085enumModeThree = _Rx085enumModeThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 43),
    _Rx085enumModeThree_Type()
)
rx085enumModeThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumModeThree.setStatus("optional")


class _Rx085valueModeThree_Type(Integer32):
    """Custom type rx085valueModeThree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("agc", 3),
          ("manual", 2),
          ("off", 1))
    )


_Rx085valueModeThree_Type.__name__ = "Integer32"
_Rx085valueModeThree_Object = MibTableColumn
rx085valueModeThree = _Rx085valueModeThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 44),
    _Rx085valueModeThree_Type()
)
rx085valueModeThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueModeThree.setStatus("mandatory")


class _Rx085stateFlagModeThree_Type(Integer32):
    """Custom type rx085stateFlagModeThree based on Integer32"""
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


_Rx085stateFlagModeThree_Type.__name__ = "Integer32"
_Rx085stateFlagModeThree_Object = MibTableColumn
rx085stateFlagModeThree = _Rx085stateFlagModeThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 45),
    _Rx085stateFlagModeThree_Type()
)
rx085stateFlagModeThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagModeThree.setStatus("mandatory")


class _Rx085labelWavelengthThree_Type(DisplayString):
    """Custom type rx085labelWavelengthThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelWavelengthThree_Type.__name__ = "DisplayString"
_Rx085labelWavelengthThree_Object = MibTableColumn
rx085labelWavelengthThree = _Rx085labelWavelengthThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 46),
    _Rx085labelWavelengthThree_Type()
)
rx085labelWavelengthThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelWavelengthThree.setStatus("optional")


class _Rx085enumWavelengthThree_Type(DisplayString):
    """Custom type rx085enumWavelengthThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumWavelengthThree_Type.__name__ = "DisplayString"
_Rx085enumWavelengthThree_Object = MibTableColumn
rx085enumWavelengthThree = _Rx085enumWavelengthThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 47),
    _Rx085enumWavelengthThree_Type()
)
rx085enumWavelengthThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumWavelengthThree.setStatus("optional")


class _Rx085valueWavelengthThree_Type(Integer32):
    """Custom type rx085valueWavelengthThree based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("nM1270", 1),
          ("nM1290", 2),
          ("nM1310", 3),
          ("nM1330", 4),
          ("nM1350", 5),
          ("nM1370", 6),
          ("nM1390", 7),
          ("nM1410", 8),
          ("nM1430", 9),
          ("nM1450", 10),
          ("nM1470", 11),
          ("nM1490", 12),
          ("nM1510", 13),
          ("nM1530", 14),
          ("nM1550", 15),
          ("nM1570", 16),
          ("nM1590", 17),
          ("nM1610", 18))
    )


_Rx085valueWavelengthThree_Type.__name__ = "Integer32"
_Rx085valueWavelengthThree_Object = MibTableColumn
rx085valueWavelengthThree = _Rx085valueWavelengthThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 48),
    _Rx085valueWavelengthThree_Type()
)
rx085valueWavelengthThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueWavelengthThree.setStatus("mandatory")


class _Rx085stateFlagWavelengthThree_Type(Integer32):
    """Custom type rx085stateFlagWavelengthThree based on Integer32"""
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


_Rx085stateFlagWavelengthThree_Type.__name__ = "Integer32"
_Rx085stateFlagWavelengthThree_Object = MibTableColumn
rx085stateFlagWavelengthThree = _Rx085stateFlagWavelengthThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 49),
    _Rx085stateFlagWavelengthThree_Type()
)
rx085stateFlagWavelengthThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagWavelengthThree.setStatus("mandatory")


class _Rx085labelAttnSettingThree_Type(DisplayString):
    """Custom type rx085labelAttnSettingThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelAttnSettingThree_Type.__name__ = "DisplayString"
_Rx085labelAttnSettingThree_Object = MibTableColumn
rx085labelAttnSettingThree = _Rx085labelAttnSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 50),
    _Rx085labelAttnSettingThree_Type()
)
rx085labelAttnSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelAttnSettingThree.setStatus("optional")


class _Rx085enumAttnSettingThree_Type(DisplayString):
    """Custom type rx085enumAttnSettingThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumAttnSettingThree_Type.__name__ = "DisplayString"
_Rx085enumAttnSettingThree_Object = MibTableColumn
rx085enumAttnSettingThree = _Rx085enumAttnSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 51),
    _Rx085enumAttnSettingThree_Type()
)
rx085enumAttnSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumAttnSettingThree.setStatus("optional")
_Rx085valueAttnSettingThree_Type = Integer32
_Rx085valueAttnSettingThree_Object = MibTableColumn
rx085valueAttnSettingThree = _Rx085valueAttnSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 52),
    _Rx085valueAttnSettingThree_Type()
)
rx085valueAttnSettingThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueAttnSettingThree.setStatus("mandatory")


class _Rx085stateFlagAttnSettingThree_Type(Integer32):
    """Custom type rx085stateFlagAttnSettingThree based on Integer32"""
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


_Rx085stateFlagAttnSettingThree_Type.__name__ = "Integer32"
_Rx085stateFlagAttnSettingThree_Object = MibTableColumn
rx085stateFlagAttnSettingThree = _Rx085stateFlagAttnSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 53),
    _Rx085stateFlagAttnSettingThree_Type()
)
rx085stateFlagAttnSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagAttnSettingThree.setStatus("mandatory")


class _Rx085labelSwModeSettingThree_Type(DisplayString):
    """Custom type rx085labelSwModeSettingThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelSwModeSettingThree_Type.__name__ = "DisplayString"
_Rx085labelSwModeSettingThree_Object = MibTableColumn
rx085labelSwModeSettingThree = _Rx085labelSwModeSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 54),
    _Rx085labelSwModeSettingThree_Type()
)
rx085labelSwModeSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelSwModeSettingThree.setStatus("optional")


class _Rx085enumSwModeSettingThree_Type(DisplayString):
    """Custom type rx085enumSwModeSettingThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumSwModeSettingThree_Type.__name__ = "DisplayString"
_Rx085enumSwModeSettingThree_Object = MibTableColumn
rx085enumSwModeSettingThree = _Rx085enumSwModeSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 55),
    _Rx085enumSwModeSettingThree_Type()
)
rx085enumSwModeSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumSwModeSettingThree.setStatus("optional")


class _Rx085valueSwModeSettingThree_Type(Integer32):
    """Custom type rx085valueSwModeSettingThree based on Integer32"""
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


_Rx085valueSwModeSettingThree_Type.__name__ = "Integer32"
_Rx085valueSwModeSettingThree_Object = MibTableColumn
rx085valueSwModeSettingThree = _Rx085valueSwModeSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 56),
    _Rx085valueSwModeSettingThree_Type()
)
rx085valueSwModeSettingThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueSwModeSettingThree.setStatus("mandatory")


class _Rx085stateFlagSwModeSettingThree_Type(Integer32):
    """Custom type rx085stateFlagSwModeSettingThree based on Integer32"""
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


_Rx085stateFlagSwModeSettingThree_Type.__name__ = "Integer32"
_Rx085stateFlagSwModeSettingThree_Object = MibTableColumn
rx085stateFlagSwModeSettingThree = _Rx085stateFlagSwModeSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 57),
    _Rx085stateFlagSwModeSettingThree_Type()
)
rx085stateFlagSwModeSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagSwModeSettingThree.setStatus("mandatory")


class _Rx085labelSwModeThresholdThree_Type(DisplayString):
    """Custom type rx085labelSwModeThresholdThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelSwModeThresholdThree_Type.__name__ = "DisplayString"
_Rx085labelSwModeThresholdThree_Object = MibTableColumn
rx085labelSwModeThresholdThree = _Rx085labelSwModeThresholdThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 58),
    _Rx085labelSwModeThresholdThree_Type()
)
rx085labelSwModeThresholdThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelSwModeThresholdThree.setStatus("optional")


class _Rx085enumSwModeThresholdThree_Type(DisplayString):
    """Custom type rx085enumSwModeThresholdThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumSwModeThresholdThree_Type.__name__ = "DisplayString"
_Rx085enumSwModeThresholdThree_Object = MibTableColumn
rx085enumSwModeThresholdThree = _Rx085enumSwModeThresholdThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 59),
    _Rx085enumSwModeThresholdThree_Type()
)
rx085enumSwModeThresholdThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumSwModeThresholdThree.setStatus("optional")
_Rx085valueSwModeThresholdThree_Type = Integer32
_Rx085valueSwModeThresholdThree_Object = MibTableColumn
rx085valueSwModeThresholdThree = _Rx085valueSwModeThresholdThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 60),
    _Rx085valueSwModeThresholdThree_Type()
)
rx085valueSwModeThresholdThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueSwModeThresholdThree.setStatus("mandatory")


class _Rx085stateFlagSwModeThresholdThree_Type(Integer32):
    """Custom type rx085stateFlagSwModeThresholdThree based on Integer32"""
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


_Rx085stateFlagSwModeThresholdThree_Type.__name__ = "Integer32"
_Rx085stateFlagSwModeThresholdThree_Object = MibTableColumn
rx085stateFlagSwModeThresholdThree = _Rx085stateFlagSwModeThresholdThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 61),
    _Rx085stateFlagSwModeThresholdThree_Type()
)
rx085stateFlagSwModeThresholdThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagSwModeThresholdThree.setStatus("mandatory")


class _Rx085labelModeFour_Type(DisplayString):
    """Custom type rx085labelModeFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelModeFour_Type.__name__ = "DisplayString"
_Rx085labelModeFour_Object = MibTableColumn
rx085labelModeFour = _Rx085labelModeFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 62),
    _Rx085labelModeFour_Type()
)
rx085labelModeFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelModeFour.setStatus("optional")


class _Rx085enumModeFour_Type(DisplayString):
    """Custom type rx085enumModeFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumModeFour_Type.__name__ = "DisplayString"
_Rx085enumModeFour_Object = MibTableColumn
rx085enumModeFour = _Rx085enumModeFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 63),
    _Rx085enumModeFour_Type()
)
rx085enumModeFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumModeFour.setStatus("optional")


class _Rx085valueModeFour_Type(Integer32):
    """Custom type rx085valueModeFour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("agc", 3),
          ("manual", 2),
          ("off", 1))
    )


_Rx085valueModeFour_Type.__name__ = "Integer32"
_Rx085valueModeFour_Object = MibTableColumn
rx085valueModeFour = _Rx085valueModeFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 64),
    _Rx085valueModeFour_Type()
)
rx085valueModeFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueModeFour.setStatus("mandatory")


class _Rx085stateFlagModeFour_Type(Integer32):
    """Custom type rx085stateFlagModeFour based on Integer32"""
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


_Rx085stateFlagModeFour_Type.__name__ = "Integer32"
_Rx085stateFlagModeFour_Object = MibTableColumn
rx085stateFlagModeFour = _Rx085stateFlagModeFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 65),
    _Rx085stateFlagModeFour_Type()
)
rx085stateFlagModeFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagModeFour.setStatus("mandatory")


class _Rx085labelWavelengthFour_Type(DisplayString):
    """Custom type rx085labelWavelengthFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelWavelengthFour_Type.__name__ = "DisplayString"
_Rx085labelWavelengthFour_Object = MibTableColumn
rx085labelWavelengthFour = _Rx085labelWavelengthFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 66),
    _Rx085labelWavelengthFour_Type()
)
rx085labelWavelengthFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelWavelengthFour.setStatus("optional")


class _Rx085enumWavelengthFour_Type(DisplayString):
    """Custom type rx085enumWavelengthFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumWavelengthFour_Type.__name__ = "DisplayString"
_Rx085enumWavelengthFour_Object = MibTableColumn
rx085enumWavelengthFour = _Rx085enumWavelengthFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 67),
    _Rx085enumWavelengthFour_Type()
)
rx085enumWavelengthFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumWavelengthFour.setStatus("optional")


class _Rx085valueWavelengthFour_Type(Integer32):
    """Custom type rx085valueWavelengthFour based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("nM1270", 1),
          ("nM1290", 2),
          ("nM1310", 3),
          ("nM1330", 4),
          ("nM1350", 5),
          ("nM1370", 6),
          ("nM1390", 7),
          ("nM1410", 8),
          ("nM1430", 9),
          ("nM1450", 10),
          ("nM1470", 11),
          ("nM1490", 12),
          ("nM1510", 13),
          ("nM1530", 14),
          ("nM1550", 15),
          ("nM1570", 16),
          ("nM1590", 17),
          ("nM1610", 18))
    )


_Rx085valueWavelengthFour_Type.__name__ = "Integer32"
_Rx085valueWavelengthFour_Object = MibTableColumn
rx085valueWavelengthFour = _Rx085valueWavelengthFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 68),
    _Rx085valueWavelengthFour_Type()
)
rx085valueWavelengthFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueWavelengthFour.setStatus("mandatory")


class _Rx085stateFlagWavelengthFour_Type(Integer32):
    """Custom type rx085stateFlagWavelengthFour based on Integer32"""
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


_Rx085stateFlagWavelengthFour_Type.__name__ = "Integer32"
_Rx085stateFlagWavelengthFour_Object = MibTableColumn
rx085stateFlagWavelengthFour = _Rx085stateFlagWavelengthFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 69),
    _Rx085stateFlagWavelengthFour_Type()
)
rx085stateFlagWavelengthFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagWavelengthFour.setStatus("mandatory")


class _Rx085labelAttnSettingFour_Type(DisplayString):
    """Custom type rx085labelAttnSettingFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelAttnSettingFour_Type.__name__ = "DisplayString"
_Rx085labelAttnSettingFour_Object = MibTableColumn
rx085labelAttnSettingFour = _Rx085labelAttnSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 70),
    _Rx085labelAttnSettingFour_Type()
)
rx085labelAttnSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelAttnSettingFour.setStatus("optional")


class _Rx085enumAttnSettingFour_Type(DisplayString):
    """Custom type rx085enumAttnSettingFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumAttnSettingFour_Type.__name__ = "DisplayString"
_Rx085enumAttnSettingFour_Object = MibTableColumn
rx085enumAttnSettingFour = _Rx085enumAttnSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 71),
    _Rx085enumAttnSettingFour_Type()
)
rx085enumAttnSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumAttnSettingFour.setStatus("optional")
_Rx085valueAttnSettingFour_Type = Integer32
_Rx085valueAttnSettingFour_Object = MibTableColumn
rx085valueAttnSettingFour = _Rx085valueAttnSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 72),
    _Rx085valueAttnSettingFour_Type()
)
rx085valueAttnSettingFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueAttnSettingFour.setStatus("mandatory")


class _Rx085stateFlagAttnSettingFour_Type(Integer32):
    """Custom type rx085stateFlagAttnSettingFour based on Integer32"""
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


_Rx085stateFlagAttnSettingFour_Type.__name__ = "Integer32"
_Rx085stateFlagAttnSettingFour_Object = MibTableColumn
rx085stateFlagAttnSettingFour = _Rx085stateFlagAttnSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 73),
    _Rx085stateFlagAttnSettingFour_Type()
)
rx085stateFlagAttnSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagAttnSettingFour.setStatus("mandatory")


class _Rx085labelSwModeSettingFour_Type(DisplayString):
    """Custom type rx085labelSwModeSettingFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelSwModeSettingFour_Type.__name__ = "DisplayString"
_Rx085labelSwModeSettingFour_Object = MibTableColumn
rx085labelSwModeSettingFour = _Rx085labelSwModeSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 74),
    _Rx085labelSwModeSettingFour_Type()
)
rx085labelSwModeSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelSwModeSettingFour.setStatus("optional")


class _Rx085enumSwModeSettingFour_Type(DisplayString):
    """Custom type rx085enumSwModeSettingFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumSwModeSettingFour_Type.__name__ = "DisplayString"
_Rx085enumSwModeSettingFour_Object = MibTableColumn
rx085enumSwModeSettingFour = _Rx085enumSwModeSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 75),
    _Rx085enumSwModeSettingFour_Type()
)
rx085enumSwModeSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumSwModeSettingFour.setStatus("optional")


class _Rx085valueSwModeSettingFour_Type(Integer32):
    """Custom type rx085valueSwModeSettingFour based on Integer32"""
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


_Rx085valueSwModeSettingFour_Type.__name__ = "Integer32"
_Rx085valueSwModeSettingFour_Object = MibTableColumn
rx085valueSwModeSettingFour = _Rx085valueSwModeSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 76),
    _Rx085valueSwModeSettingFour_Type()
)
rx085valueSwModeSettingFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueSwModeSettingFour.setStatus("mandatory")


class _Rx085stateFlagSwModeSettingFour_Type(Integer32):
    """Custom type rx085stateFlagSwModeSettingFour based on Integer32"""
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


_Rx085stateFlagSwModeSettingFour_Type.__name__ = "Integer32"
_Rx085stateFlagSwModeSettingFour_Object = MibTableColumn
rx085stateFlagSwModeSettingFour = _Rx085stateFlagSwModeSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 77),
    _Rx085stateFlagSwModeSettingFour_Type()
)
rx085stateFlagSwModeSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagSwModeSettingFour.setStatus("mandatory")


class _Rx085labelSwModeThresholdFour_Type(DisplayString):
    """Custom type rx085labelSwModeThresholdFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelSwModeThresholdFour_Type.__name__ = "DisplayString"
_Rx085labelSwModeThresholdFour_Object = MibTableColumn
rx085labelSwModeThresholdFour = _Rx085labelSwModeThresholdFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 78),
    _Rx085labelSwModeThresholdFour_Type()
)
rx085labelSwModeThresholdFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelSwModeThresholdFour.setStatus("optional")


class _Rx085enumSwModeThresholdFour_Type(DisplayString):
    """Custom type rx085enumSwModeThresholdFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumSwModeThresholdFour_Type.__name__ = "DisplayString"
_Rx085enumSwModeThresholdFour_Object = MibTableColumn
rx085enumSwModeThresholdFour = _Rx085enumSwModeThresholdFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 79),
    _Rx085enumSwModeThresholdFour_Type()
)
rx085enumSwModeThresholdFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumSwModeThresholdFour.setStatus("optional")
_Rx085valueSwModeThresholdFour_Type = Integer32
_Rx085valueSwModeThresholdFour_Object = MibTableColumn
rx085valueSwModeThresholdFour = _Rx085valueSwModeThresholdFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 80),
    _Rx085valueSwModeThresholdFour_Type()
)
rx085valueSwModeThresholdFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueSwModeThresholdFour.setStatus("mandatory")


class _Rx085stateFlagSwModeThresholdFour_Type(Integer32):
    """Custom type rx085stateFlagSwModeThresholdFour based on Integer32"""
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


_Rx085stateFlagSwModeThresholdFour_Type.__name__ = "Integer32"
_Rx085stateFlagSwModeThresholdFour_Object = MibTableColumn
rx085stateFlagSwModeThresholdFour = _Rx085stateFlagSwModeThresholdFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 81),
    _Rx085stateFlagSwModeThresholdFour_Type()
)
rx085stateFlagSwModeThresholdFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagSwModeThresholdFour.setStatus("mandatory")


class _Rx085labelModuleConfig_Type(DisplayString):
    """Custom type rx085labelModuleConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelModuleConfig_Type.__name__ = "DisplayString"
_Rx085labelModuleConfig_Object = MibTableColumn
rx085labelModuleConfig = _Rx085labelModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 82),
    _Rx085labelModuleConfig_Type()
)
rx085labelModuleConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelModuleConfig.setStatus("optional")


class _Rx085enumModuleConfig_Type(DisplayString):
    """Custom type rx085enumModuleConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumModuleConfig_Type.__name__ = "DisplayString"
_Rx085enumModuleConfig_Object = MibTableColumn
rx085enumModuleConfig = _Rx085enumModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 83),
    _Rx085enumModuleConfig_Type()
)
rx085enumModuleConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumModuleConfig.setStatus("optional")


class _Rx085valueModuleConfig_Type(Integer32):
    """Custom type rx085valueModuleConfig based on Integer32"""
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
          ("master", 2),
          ("slave", 1))
    )


_Rx085valueModuleConfig_Type.__name__ = "Integer32"
_Rx085valueModuleConfig_Object = MibTableColumn
rx085valueModuleConfig = _Rx085valueModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 84),
    _Rx085valueModuleConfig_Type()
)
rx085valueModuleConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueModuleConfig.setStatus("mandatory")


class _Rx085stateFlagModuleConfig_Type(Integer32):
    """Custom type rx085stateFlagModuleConfig based on Integer32"""
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


_Rx085stateFlagModuleConfig_Type.__name__ = "Integer32"
_Rx085stateFlagModuleConfig_Object = MibTableColumn
rx085stateFlagModuleConfig = _Rx085stateFlagModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 85),
    _Rx085stateFlagModuleConfig_Type()
)
rx085stateFlagModuleConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagModuleConfig.setStatus("mandatory")


class _Rx085labelRevertTime_Type(DisplayString):
    """Custom type rx085labelRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelRevertTime_Type.__name__ = "DisplayString"
_Rx085labelRevertTime_Object = MibTableColumn
rx085labelRevertTime = _Rx085labelRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 86),
    _Rx085labelRevertTime_Type()
)
rx085labelRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelRevertTime.setStatus("optional")


class _Rx085enumRevertTime_Type(DisplayString):
    """Custom type rx085enumRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumRevertTime_Type.__name__ = "DisplayString"
_Rx085enumRevertTime_Object = MibTableColumn
rx085enumRevertTime = _Rx085enumRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 87),
    _Rx085enumRevertTime_Type()
)
rx085enumRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumRevertTime.setStatus("optional")


class _Rx085valueRevertTime_Type(Integer32):
    """Custom type rx085valueRevertTime based on Integer32"""
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
        *(("one-sec", 1),
          ("six-hundred-sec", 4),
          ("sixty-sec", 3),
          ("ten-sec", 2))
    )


_Rx085valueRevertTime_Type.__name__ = "Integer32"
_Rx085valueRevertTime_Object = MibTableColumn
rx085valueRevertTime = _Rx085valueRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 88),
    _Rx085valueRevertTime_Type()
)
rx085valueRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueRevertTime.setStatus("mandatory")


class _Rx085stateFlagRevertTime_Type(Integer32):
    """Custom type rx085stateFlagRevertTime based on Integer32"""
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


_Rx085stateFlagRevertTime_Type.__name__ = "Integer32"
_Rx085stateFlagRevertTime_Object = MibTableColumn
rx085stateFlagRevertTime = _Rx085stateFlagRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 89),
    _Rx085stateFlagRevertTime_Type()
)
rx085stateFlagRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagRevertTime.setStatus("mandatory")


class _Rx085labelTestPointSelect_Type(DisplayString):
    """Custom type rx085labelTestPointSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelTestPointSelect_Type.__name__ = "DisplayString"
_Rx085labelTestPointSelect_Object = MibTableColumn
rx085labelTestPointSelect = _Rx085labelTestPointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 90),
    _Rx085labelTestPointSelect_Type()
)
rx085labelTestPointSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelTestPointSelect.setStatus("optional")


class _Rx085enumTestPointSelect_Type(DisplayString):
    """Custom type rx085enumTestPointSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumTestPointSelect_Type.__name__ = "DisplayString"
_Rx085enumTestPointSelect_Object = MibTableColumn
rx085enumTestPointSelect = _Rx085enumTestPointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 91),
    _Rx085enumTestPointSelect_Type()
)
rx085enumTestPointSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumTestPointSelect.setStatus("optional")


class _Rx085valueTestPointSelect_Type(Integer32):
    """Custom type rx085valueTestPointSelect based on Integer32"""
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
        *(("four", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_Rx085valueTestPointSelect_Type.__name__ = "Integer32"
_Rx085valueTestPointSelect_Object = MibTableColumn
rx085valueTestPointSelect = _Rx085valueTestPointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 92),
    _Rx085valueTestPointSelect_Type()
)
rx085valueTestPointSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueTestPointSelect.setStatus("mandatory")


class _Rx085stateFlagTestPointSelect_Type(Integer32):
    """Custom type rx085stateFlagTestPointSelect based on Integer32"""
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


_Rx085stateFlagTestPointSelect_Type.__name__ = "Integer32"
_Rx085stateFlagTestPointSelect_Object = MibTableColumn
rx085stateFlagTestPointSelect = _Rx085stateFlagTestPointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 93),
    _Rx085stateFlagTestPointSelect_Type()
)
rx085stateFlagTestPointSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagTestPointSelect.setStatus("mandatory")


class _Rx085labelFactoryDefault_Type(DisplayString):
    """Custom type rx085labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelFactoryDefault_Type.__name__ = "DisplayString"
_Rx085labelFactoryDefault_Object = MibTableColumn
rx085labelFactoryDefault = _Rx085labelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 94),
    _Rx085labelFactoryDefault_Type()
)
rx085labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelFactoryDefault.setStatus("optional")


class _Rx085enumFactoryDefault_Type(DisplayString):
    """Custom type rx085enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085enumFactoryDefault_Type.__name__ = "DisplayString"
_Rx085enumFactoryDefault_Object = MibTableColumn
rx085enumFactoryDefault = _Rx085enumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 95),
    _Rx085enumFactoryDefault_Type()
)
rx085enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085enumFactoryDefault.setStatus("optional")


class _Rx085valueFactoryDefault_Type(Integer32):
    """Custom type rx085valueFactoryDefault based on Integer32"""
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


_Rx085valueFactoryDefault_Type.__name__ = "Integer32"
_Rx085valueFactoryDefault_Object = MibTableColumn
rx085valueFactoryDefault = _Rx085valueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 96),
    _Rx085valueFactoryDefault_Type()
)
rx085valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx085valueFactoryDefault.setStatus("mandatory")


class _Rx085stateFlagFactoryDefault_Type(Integer32):
    """Custom type rx085stateFlagFactoryDefault based on Integer32"""
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


_Rx085stateFlagFactoryDefault_Type.__name__ = "Integer32"
_Rx085stateFlagFactoryDefault_Object = MibTableColumn
rx085stateFlagFactoryDefault = _Rx085stateFlagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 3, 2, 97),
    _Rx085stateFlagFactoryDefault_Type()
)
rx085stateFlagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateFlagFactoryDefault.setStatus("mandatory")
_Gx2Rx085BX4StatusTable_Object = MibTable
gx2Rx085BX4StatusTable = _Gx2Rx085BX4StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4)
)
if mibBuilder.loadTexts:
    gx2Rx085BX4StatusTable.setStatus("mandatory")
_Gx2Rx085BX4StatusEntry_Object = MibTableRow
gx2Rx085BX4StatusEntry = _Gx2Rx085BX4StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3)
)
gx2Rx085BX4StatusEntry.setIndexNames(
    (0, "OMNI-gx2Rx085BX4-MIB", "gx2Rx085BX4StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx085BX4StatusEntry.setStatus("mandatory")


class _Gx2Rx085BX4StatusTableIndex_Type(Integer32):
    """Custom type gx2Rx085BX4StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx085BX4StatusTableIndex_Type.__name__ = "Integer32"
_Gx2Rx085BX4StatusTableIndex_Object = MibTableColumn
gx2Rx085BX4StatusTableIndex = _Gx2Rx085BX4StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 1),
    _Gx2Rx085BX4StatusTableIndex_Type()
)
gx2Rx085BX4StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx085BX4StatusTableIndex.setStatus("mandatory")


class _Rx085labelBoot_Type(DisplayString):
    """Custom type rx085labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelBoot_Type.__name__ = "DisplayString"
_Rx085labelBoot_Object = MibTableColumn
rx085labelBoot = _Rx085labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 2),
    _Rx085labelBoot_Type()
)
rx085labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelBoot.setStatus("optional")


class _Rx085valueBoot_Type(Integer32):
    """Custom type rx085valueBoot based on Integer32"""
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


_Rx085valueBoot_Type.__name__ = "Integer32"
_Rx085valueBoot_Object = MibTableColumn
rx085valueBoot = _Rx085valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 3),
    _Rx085valueBoot_Type()
)
rx085valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueBoot.setStatus("mandatory")


class _Rx085stateflagBoot_Type(Integer32):
    """Custom type rx085stateflagBoot based on Integer32"""
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


_Rx085stateflagBoot_Type.__name__ = "Integer32"
_Rx085stateflagBoot_Object = MibTableColumn
rx085stateflagBoot = _Rx085stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 4),
    _Rx085stateflagBoot_Type()
)
rx085stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagBoot.setStatus("mandatory")


class _Rx085labelFlash_Type(DisplayString):
    """Custom type rx085labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelFlash_Type.__name__ = "DisplayString"
_Rx085labelFlash_Object = MibTableColumn
rx085labelFlash = _Rx085labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 5),
    _Rx085labelFlash_Type()
)
rx085labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelFlash.setStatus("optional")


class _Rx085valueFlash_Type(Integer32):
    """Custom type rx085valueFlash based on Integer32"""
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


_Rx085valueFlash_Type.__name__ = "Integer32"
_Rx085valueFlash_Object = MibTableColumn
rx085valueFlash = _Rx085valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 6),
    _Rx085valueFlash_Type()
)
rx085valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueFlash.setStatus("mandatory")


class _Rx085stateflagFlash_Type(Integer32):
    """Custom type rx085stateflagFlash based on Integer32"""
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


_Rx085stateflagFlash_Type.__name__ = "Integer32"
_Rx085stateflagFlash_Object = MibTableColumn
rx085stateflagFlash = _Rx085stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 7),
    _Rx085stateflagFlash_Type()
)
rx085stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagFlash.setStatus("mandatory")


class _Rx085labelFactoryDataCRC_Type(DisplayString):
    """Custom type rx085labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Rx085labelFactoryDataCRC_Object = MibTableColumn
rx085labelFactoryDataCRC = _Rx085labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 8),
    _Rx085labelFactoryDataCRC_Type()
)
rx085labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelFactoryDataCRC.setStatus("optional")


class _Rx085valueFactoryDataCRC_Type(Integer32):
    """Custom type rx085valueFactoryDataCRC based on Integer32"""
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


_Rx085valueFactoryDataCRC_Type.__name__ = "Integer32"
_Rx085valueFactoryDataCRC_Object = MibTableColumn
rx085valueFactoryDataCRC = _Rx085valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 9),
    _Rx085valueFactoryDataCRC_Type()
)
rx085valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueFactoryDataCRC.setStatus("mandatory")


class _Rx085stateflagFactoryDataCRC_Type(Integer32):
    """Custom type rx085stateflagFactoryDataCRC based on Integer32"""
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


_Rx085stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Rx085stateflagFactoryDataCRC_Object = MibTableColumn
rx085stateflagFactoryDataCRC = _Rx085stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 10),
    _Rx085stateflagFactoryDataCRC_Type()
)
rx085stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagFactoryDataCRC.setStatus("mandatory")


class _Rx085labelAlarmDataCRC_Type(DisplayString):
    """Custom type rx085labelAlarmDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelAlarmDataCRC_Type.__name__ = "DisplayString"
_Rx085labelAlarmDataCRC_Object = MibTableColumn
rx085labelAlarmDataCRC = _Rx085labelAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 11),
    _Rx085labelAlarmDataCRC_Type()
)
rx085labelAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelAlarmDataCRC.setStatus("optional")


class _Rx085valueAlarmDataCRC_Type(Integer32):
    """Custom type rx085valueAlarmDataCRC based on Integer32"""
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


_Rx085valueAlarmDataCRC_Type.__name__ = "Integer32"
_Rx085valueAlarmDataCRC_Object = MibTableColumn
rx085valueAlarmDataCRC = _Rx085valueAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 12),
    _Rx085valueAlarmDataCRC_Type()
)
rx085valueAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueAlarmDataCRC.setStatus("mandatory")


class _Rx085stateflagAlarmDataCRC_Type(Integer32):
    """Custom type rx085stateflagAlarmDataCRC based on Integer32"""
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


_Rx085stateflagAlarmDataCRC_Type.__name__ = "Integer32"
_Rx085stateflagAlarmDataCRC_Object = MibTableColumn
rx085stateflagAlarmDataCRC = _Rx085stateflagAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 13),
    _Rx085stateflagAlarmDataCRC_Type()
)
rx085stateflagAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagAlarmDataCRC.setStatus("mandatory")


class _Rx085labelCalibrationDataCRC_Type(DisplayString):
    """Custom type rx085labelCalibrationDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelCalibrationDataCRC_Type.__name__ = "DisplayString"
_Rx085labelCalibrationDataCRC_Object = MibTableColumn
rx085labelCalibrationDataCRC = _Rx085labelCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 14),
    _Rx085labelCalibrationDataCRC_Type()
)
rx085labelCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelCalibrationDataCRC.setStatus("optional")


class _Rx085valueCalibrationDataCRC_Type(Integer32):
    """Custom type rx085valueCalibrationDataCRC based on Integer32"""
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


_Rx085valueCalibrationDataCRC_Type.__name__ = "Integer32"
_Rx085valueCalibrationDataCRC_Object = MibTableColumn
rx085valueCalibrationDataCRC = _Rx085valueCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 15),
    _Rx085valueCalibrationDataCRC_Type()
)
rx085valueCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueCalibrationDataCRC.setStatus("mandatory")


class _Rx085stateflagCalibrationDataCRC_Type(Integer32):
    """Custom type rx085stateflagCalibrationDataCRC based on Integer32"""
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


_Rx085stateflagCalibrationDataCRC_Type.__name__ = "Integer32"
_Rx085stateflagCalibrationDataCRC_Object = MibTableColumn
rx085stateflagCalibrationDataCRC = _Rx085stateflagCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 16),
    _Rx085stateflagCalibrationDataCRC_Type()
)
rx085stateflagCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagCalibrationDataCRC.setStatus("mandatory")


class _Rx085labelHW_Type(DisplayString):
    """Custom type rx085labelHW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelHW_Type.__name__ = "DisplayString"
_Rx085labelHW_Object = MibTableColumn
rx085labelHW = _Rx085labelHW_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 17),
    _Rx085labelHW_Type()
)
rx085labelHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelHW.setStatus("optional")


class _Rx085valueHW_Type(Integer32):
    """Custom type rx085valueHW based on Integer32"""
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


_Rx085valueHW_Type.__name__ = "Integer32"
_Rx085valueHW_Object = MibTableColumn
rx085valueHW = _Rx085valueHW_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 18),
    _Rx085valueHW_Type()
)
rx085valueHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueHW.setStatus("mandatory")


class _Rx085stateflagHW_Type(Integer32):
    """Custom type rx085stateflagHW based on Integer32"""
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


_Rx085stateflagHW_Type.__name__ = "Integer32"
_Rx085stateflagHW_Object = MibTableColumn
rx085stateflagHW = _Rx085stateflagHW_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 19),
    _Rx085stateflagHW_Type()
)
rx085stateflagHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagHW.setStatus("mandatory")


class _Rx085labelOptSigOne_Type(DisplayString):
    """Custom type rx085labelOptSigOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelOptSigOne_Type.__name__ = "DisplayString"
_Rx085labelOptSigOne_Object = MibTableColumn
rx085labelOptSigOne = _Rx085labelOptSigOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 20),
    _Rx085labelOptSigOne_Type()
)
rx085labelOptSigOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelOptSigOne.setStatus("optional")


class _Rx085valueOptSigOne_Type(Integer32):
    """Custom type rx085valueOptSigOne based on Integer32"""
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


_Rx085valueOptSigOne_Type.__name__ = "Integer32"
_Rx085valueOptSigOne_Object = MibTableColumn
rx085valueOptSigOne = _Rx085valueOptSigOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 21),
    _Rx085valueOptSigOne_Type()
)
rx085valueOptSigOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueOptSigOne.setStatus("mandatory")


class _Rx085stateflagOptSigOne_Type(Integer32):
    """Custom type rx085stateflagOptSigOne based on Integer32"""
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


_Rx085stateflagOptSigOne_Type.__name__ = "Integer32"
_Rx085stateflagOptSigOne_Object = MibTableColumn
rx085stateflagOptSigOne = _Rx085stateflagOptSigOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 22),
    _Rx085stateflagOptSigOne_Type()
)
rx085stateflagOptSigOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagOptSigOne.setStatus("mandatory")


class _Rx085labelOptSigTwo_Type(DisplayString):
    """Custom type rx085labelOptSigTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelOptSigTwo_Type.__name__ = "DisplayString"
_Rx085labelOptSigTwo_Object = MibTableColumn
rx085labelOptSigTwo = _Rx085labelOptSigTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 23),
    _Rx085labelOptSigTwo_Type()
)
rx085labelOptSigTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelOptSigTwo.setStatus("optional")


class _Rx085valueOptSigTwo_Type(Integer32):
    """Custom type rx085valueOptSigTwo based on Integer32"""
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


_Rx085valueOptSigTwo_Type.__name__ = "Integer32"
_Rx085valueOptSigTwo_Object = MibTableColumn
rx085valueOptSigTwo = _Rx085valueOptSigTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 24),
    _Rx085valueOptSigTwo_Type()
)
rx085valueOptSigTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueOptSigTwo.setStatus("mandatory")


class _Rx085stateflagOptSigTwo_Type(Integer32):
    """Custom type rx085stateflagOptSigTwo based on Integer32"""
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


_Rx085stateflagOptSigTwo_Type.__name__ = "Integer32"
_Rx085stateflagOptSigTwo_Object = MibTableColumn
rx085stateflagOptSigTwo = _Rx085stateflagOptSigTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 25),
    _Rx085stateflagOptSigTwo_Type()
)
rx085stateflagOptSigTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagOptSigTwo.setStatus("mandatory")


class _Rx085labelOptSigThree_Type(DisplayString):
    """Custom type rx085labelOptSigThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelOptSigThree_Type.__name__ = "DisplayString"
_Rx085labelOptSigThree_Object = MibTableColumn
rx085labelOptSigThree = _Rx085labelOptSigThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 26),
    _Rx085labelOptSigThree_Type()
)
rx085labelOptSigThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelOptSigThree.setStatus("optional")


class _Rx085valueOptSigThree_Type(Integer32):
    """Custom type rx085valueOptSigThree based on Integer32"""
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


_Rx085valueOptSigThree_Type.__name__ = "Integer32"
_Rx085valueOptSigThree_Object = MibTableColumn
rx085valueOptSigThree = _Rx085valueOptSigThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 27),
    _Rx085valueOptSigThree_Type()
)
rx085valueOptSigThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueOptSigThree.setStatus("mandatory")


class _Rx085stateflagOptSigThree_Type(Integer32):
    """Custom type rx085stateflagOptSigThree based on Integer32"""
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


_Rx085stateflagOptSigThree_Type.__name__ = "Integer32"
_Rx085stateflagOptSigThree_Object = MibTableColumn
rx085stateflagOptSigThree = _Rx085stateflagOptSigThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 28),
    _Rx085stateflagOptSigThree_Type()
)
rx085stateflagOptSigThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagOptSigThree.setStatus("mandatory")


class _Rx085labelOptSigFour_Type(DisplayString):
    """Custom type rx085labelOptSigFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelOptSigFour_Type.__name__ = "DisplayString"
_Rx085labelOptSigFour_Object = MibTableColumn
rx085labelOptSigFour = _Rx085labelOptSigFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 29),
    _Rx085labelOptSigFour_Type()
)
rx085labelOptSigFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelOptSigFour.setStatus("optional")


class _Rx085valueOptSigFour_Type(Integer32):
    """Custom type rx085valueOptSigFour based on Integer32"""
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


_Rx085valueOptSigFour_Type.__name__ = "Integer32"
_Rx085valueOptSigFour_Object = MibTableColumn
rx085valueOptSigFour = _Rx085valueOptSigFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 30),
    _Rx085valueOptSigFour_Type()
)
rx085valueOptSigFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueOptSigFour.setStatus("mandatory")


class _Rx085stateflagOptSigFour_Type(Integer32):
    """Custom type rx085stateflagOptSigFour based on Integer32"""
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


_Rx085stateflagOptSigFour_Type.__name__ = "Integer32"
_Rx085stateflagOptSigFour_Object = MibTableColumn
rx085stateflagOptSigFour = _Rx085stateflagOptSigFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 31),
    _Rx085stateflagOptSigFour_Type()
)
rx085stateflagOptSigFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagOptSigFour.setStatus("mandatory")


class _Rx085labelBackupCable_Type(DisplayString):
    """Custom type rx085labelBackupCable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085labelBackupCable_Type.__name__ = "DisplayString"
_Rx085labelBackupCable_Object = MibTableColumn
rx085labelBackupCable = _Rx085labelBackupCable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 32),
    _Rx085labelBackupCable_Type()
)
rx085labelBackupCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085labelBackupCable.setStatus("optional")


class _Rx085valueBackupCable_Type(Integer32):
    """Custom type rx085valueBackupCable based on Integer32"""
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


_Rx085valueBackupCable_Type.__name__ = "Integer32"
_Rx085valueBackupCable_Object = MibTableColumn
rx085valueBackupCable = _Rx085valueBackupCable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 33),
    _Rx085valueBackupCable_Type()
)
rx085valueBackupCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085valueBackupCable.setStatus("mandatory")


class _Rx085stateflagBackupCable_Type(Integer32):
    """Custom type rx085stateflagBackupCable based on Integer32"""
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


_Rx085stateflagBackupCable_Type.__name__ = "Integer32"
_Rx085stateflagBackupCable_Object = MibTableColumn
rx085stateflagBackupCable = _Rx085stateflagBackupCable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 4, 3, 34),
    _Rx085stateflagBackupCable_Type()
)
rx085stateflagBackupCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085stateflagBackupCable.setStatus("mandatory")
_Gx2Rx085BX4FactoryTable_Object = MibTable
gx2Rx085BX4FactoryTable = _Gx2Rx085BX4FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5)
)
if mibBuilder.loadTexts:
    gx2Rx085BX4FactoryTable.setStatus("mandatory")
_Gx2Rx085BX4FactoryEntry_Object = MibTableRow
gx2Rx085BX4FactoryEntry = _Gx2Rx085BX4FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4)
)
gx2Rx085BX4FactoryEntry.setIndexNames(
    (0, "OMNI-gx2Rx085BX4-MIB", "gx2Rx085BX4FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx085BX4FactoryEntry.setStatus("mandatory")


class _Gx2Rx085BX4FactoryTableIndex_Type(Integer32):
    """Custom type gx2Rx085BX4FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx085BX4FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Rx085BX4FactoryTableIndex_Object = MibTableColumn
gx2Rx085BX4FactoryTableIndex = _Gx2Rx085BX4FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 1),
    _Gx2Rx085BX4FactoryTableIndex_Type()
)
gx2Rx085BX4FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx085BX4FactoryTableIndex.setStatus("mandatory")
_Rx085bootControlByte_Type = Integer32
_Rx085bootControlByte_Object = MibTableColumn
rx085bootControlByte = _Rx085bootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 2),
    _Rx085bootControlByte_Type()
)
rx085bootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085bootControlByte.setStatus("mandatory")
_Rx085bootStatusByte_Type = Integer32
_Rx085bootStatusByte_Object = MibTableColumn
rx085bootStatusByte = _Rx085bootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 3),
    _Rx085bootStatusByte_Type()
)
rx085bootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085bootStatusByte.setStatus("mandatory")
_Rx085bank0CRC_Type = Integer32
_Rx085bank0CRC_Object = MibTableColumn
rx085bank0CRC = _Rx085bank0CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 4),
    _Rx085bank0CRC_Type()
)
rx085bank0CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085bank0CRC.setStatus("mandatory")
_Rx085bank1CRC_Type = Integer32
_Rx085bank1CRC_Object = MibTableColumn
rx085bank1CRC = _Rx085bank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 5),
    _Rx085bank1CRC_Type()
)
rx085bank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085bank1CRC.setStatus("mandatory")
_Rx085prgEEPROMByte_Type = Integer32
_Rx085prgEEPROMByte_Object = MibTableColumn
rx085prgEEPROMByte = _Rx085prgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 6),
    _Rx085prgEEPROMByte_Type()
)
rx085prgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085prgEEPROMByte.setStatus("mandatory")
_Rx085factoryCRC_Type = Integer32
_Rx085factoryCRC_Object = MibTableColumn
rx085factoryCRC = _Rx085factoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 7),
    _Rx085factoryCRC_Type()
)
rx085factoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085factoryCRC.setStatus("mandatory")


class _Rx085calculateCRC_Type(Integer32):
    """Custom type rx085calculateCRC based on Integer32"""
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


_Rx085calculateCRC_Type.__name__ = "Integer32"
_Rx085calculateCRC_Object = MibTableColumn
rx085calculateCRC = _Rx085calculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 8),
    _Rx085calculateCRC_Type()
)
rx085calculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085calculateCRC.setStatus("mandatory")
_Rx085hourMeter_Type = Integer32
_Rx085hourMeter_Object = MibTableColumn
rx085hourMeter = _Rx085hourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 9),
    _Rx085hourMeter_Type()
)
rx085hourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085hourMeter.setStatus("mandatory")
_Rx085flashPrgCntA_Type = Integer32
_Rx085flashPrgCntA_Object = MibTableColumn
rx085flashPrgCntA = _Rx085flashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 10),
    _Rx085flashPrgCntA_Type()
)
rx085flashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085flashPrgCntA.setStatus("mandatory")
_Rx085flashPrgCntB_Type = Integer32
_Rx085flashPrgCntB_Object = MibTableColumn
rx085flashPrgCntB = _Rx085flashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 11),
    _Rx085flashPrgCntB_Type()
)
rx085flashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085flashPrgCntB.setStatus("mandatory")


class _Rx085fwRev0_Type(DisplayString):
    """Custom type rx085fwRev0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085fwRev0_Type.__name__ = "DisplayString"
_Rx085fwRev0_Object = MibTableColumn
rx085fwRev0 = _Rx085fwRev0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 12),
    _Rx085fwRev0_Type()
)
rx085fwRev0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085fwRev0.setStatus("mandatory")


class _Rx085fwRev1_Type(DisplayString):
    """Custom type rx085fwRev1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx085fwRev1_Type.__name__ = "DisplayString"
_Rx085fwRev1_Object = MibTableColumn
rx085fwRev1 = _Rx085fwRev1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 5, 4, 13),
    _Rx085fwRev1_Type()
)
rx085fwRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx085fwRev1.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapRx085BX4ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 1)
)
trapRx085BX4ConfigChangeInteger.setObjects(
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
    trapRx085BX4ConfigChangeInteger.setStatus(
        ""
    )

trapRx085BX4ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 2)
)
trapRx085BX4ConfigChangeDisplayString.setObjects(
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
    trapRx085BX4ConfigChangeDisplayString.setStatus(
        ""
    )

trapRx085BX4OpticalPower1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 3)
)
trapRx085BX4OpticalPower1Alarm.setObjects(
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
    trapRx085BX4OpticalPower1Alarm.setStatus(
        ""
    )

trapRx085BX4OpticalPower2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 4)
)
trapRx085BX4OpticalPower2Alarm.setObjects(
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
    trapRx085BX4OpticalPower2Alarm.setStatus(
        ""
    )

trapRx085BX4OpticalPower3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 5)
)
trapRx085BX4OpticalPower3Alarm.setObjects(
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
    trapRx085BX4OpticalPower3Alarm.setStatus(
        ""
    )

trapRx085BX4OpticalPower4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 6)
)
trapRx085BX4OpticalPower4Alarm.setObjects(
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
    trapRx085BX4OpticalPower4Alarm.setStatus(
        ""
    )

trapRx085BX4ModuleTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 7)
)
trapRx085BX4ModuleTemperatureAlarm.setObjects(
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
    trapRx085BX4ModuleTemperatureAlarm.setStatus(
        ""
    )

trapRx085BX4FanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 8)
)
trapRx085BX4FanCurrentAlarm.setObjects(
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
    trapRx085BX4FanCurrentAlarm.setStatus(
        ""
    )

trapRx085BX4Plus12CurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 9)
)
trapRx085BX4Plus12CurrentAlarm.setObjects(
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
    trapRx085BX4Plus12CurrentAlarm.setStatus(
        ""
    )

trapRx085BX4Boot0Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 10)
)
trapRx085BX4Boot0Alarm.setObjects(
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
    trapRx085BX4Boot0Alarm.setStatus(
        ""
    )

trapRx085BX4Boot1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 11)
)
trapRx085BX4Boot1Alarm.setObjects(
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
    trapRx085BX4Boot1Alarm.setStatus(
        ""
    )

trapRx085BX4FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 12)
)
trapRx085BX4FlashAlarm.setObjects(
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
    trapRx085BX4FlashAlarm.setStatus(
        ""
    )

trapRx085BX4AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 13)
)
trapRx085BX4AlarmDataCRCAlarm.setObjects(
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
    trapRx085BX4AlarmDataCRCAlarm.setStatus(
        ""
    )

trapRx085BX4FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 14)
)
trapRx085BX4FactoryDataCRCAlarm.setObjects(
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
    trapRx085BX4FactoryDataCRCAlarm.setStatus(
        ""
    )

trapRx085BX4CalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 15)
)
trapRx085BX4CalDataCRCAlarm.setObjects(
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
    trapRx085BX4CalDataCRCAlarm.setStatus(
        ""
    )

trapRx085BX4DefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 16)
)
trapRx085BX4DefaultAlarm.setObjects(
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
    trapRx085BX4DefaultAlarm.setStatus(
        ""
    )

trapRx085BX4Mode1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 17)
)
trapRx085BX4Mode1Alarm.setObjects(
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
    trapRx085BX4Mode1Alarm.setStatus(
        ""
    )

trapRx085BX4Mode2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 18)
)
trapRx085BX4Mode2Alarm.setObjects(
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
    trapRx085BX4Mode2Alarm.setStatus(
        ""
    )

trapRx085BX4Mode3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 19)
)
trapRx085BX4Mode3Alarm.setObjects(
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
    trapRx085BX4Mode3Alarm.setStatus(
        ""
    )

trapRx085BX4Mode4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 20)
)
trapRx085BX4Mode4Alarm.setObjects(
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
    trapRx085BX4Mode4Alarm.setStatus(
        ""
    )

trapRx085BX4Output1SwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 21)
)
trapRx085BX4Output1SwitchedAlarm.setObjects(
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
    trapRx085BX4Output1SwitchedAlarm.setStatus(
        ""
    )

trapRx085BX4Output2SwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 22)
)
trapRx085BX4Output2SwitchedAlarm.setObjects(
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
    trapRx085BX4Output2SwitchedAlarm.setStatus(
        ""
    )

trapRx085BX4Output3SwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 23)
)
trapRx085BX4Output3SwitchedAlarm.setObjects(
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
    trapRx085BX4Output3SwitchedAlarm.setStatus(
        ""
    )

trapRx085BX4Output4SwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 24)
)
trapRx085BX4Output4SwitchedAlarm.setObjects(
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
    trapRx085BX4Output4SwitchedAlarm.setStatus(
        ""
    )

trapRx085BX4RX1StatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 25)
)
trapRx085BX4RX1StatusAlarm.setObjects(
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
    trapRx085BX4RX1StatusAlarm.setStatus(
        ""
    )

trapRx085BX4RX2StatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 26)
)
trapRx085BX4RX2StatusAlarm.setObjects(
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
    trapRx085BX4RX2StatusAlarm.setStatus(
        ""
    )

trapRx085BX4RX3StatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 27)
)
trapRx085BX4RX3StatusAlarm.setObjects(
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
    trapRx085BX4RX3StatusAlarm.setStatus(
        ""
    )

trapRx085BX4RX4StatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 28)
)
trapRx085BX4RX4StatusAlarm.setObjects(
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
    trapRx085BX4RX4StatusAlarm.setStatus(
        ""
    )

trapRx085BX4BackupCableAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 29)
)
trapRx085BX4BackupCableAlarm.setObjects(
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
    trapRx085BX4BackupCableAlarm.setStatus(
        ""
    )

trapRx085BX4OptPwr1BadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 30)
)
trapRx085BX4OptPwr1BadAlarm.setObjects(
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
    trapRx085BX4OptPwr1BadAlarm.setStatus(
        ""
    )

trapRx085BX4OptPwr2BadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 31)
)
trapRx085BX4OptPwr2BadAlarm.setObjects(
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
    trapRx085BX4OptPwr2BadAlarm.setStatus(
        ""
    )

trapRx085BX4OptPwr3BadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 32)
)
trapRx085BX4OptPwr3BadAlarm.setObjects(
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
    trapRx085BX4OptPwr3BadAlarm.setStatus(
        ""
    )

trapRx085BX4OptPwr4BadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32, 0, 33)
)
trapRx085BX4OptPwr4BadAlarm.setObjects(
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
    trapRx085BX4OptPwr4BadAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2Rx085BX4-MIB",
    **{"Float": Float,
       "U32Data": U32Data,
       "trapRx085BX4ConfigChangeInteger": trapRx085BX4ConfigChangeInteger,
       "trapRx085BX4ConfigChangeDisplayString": trapRx085BX4ConfigChangeDisplayString,
       "trapRx085BX4OpticalPower1Alarm": trapRx085BX4OpticalPower1Alarm,
       "trapRx085BX4OpticalPower2Alarm": trapRx085BX4OpticalPower2Alarm,
       "trapRx085BX4OpticalPower3Alarm": trapRx085BX4OpticalPower3Alarm,
       "trapRx085BX4OpticalPower4Alarm": trapRx085BX4OpticalPower4Alarm,
       "trapRx085BX4ModuleTemperatureAlarm": trapRx085BX4ModuleTemperatureAlarm,
       "trapRx085BX4FanCurrentAlarm": trapRx085BX4FanCurrentAlarm,
       "trapRx085BX4Plus12CurrentAlarm": trapRx085BX4Plus12CurrentAlarm,
       "trapRx085BX4Boot0Alarm": trapRx085BX4Boot0Alarm,
       "trapRx085BX4Boot1Alarm": trapRx085BX4Boot1Alarm,
       "trapRx085BX4FlashAlarm": trapRx085BX4FlashAlarm,
       "trapRx085BX4AlarmDataCRCAlarm": trapRx085BX4AlarmDataCRCAlarm,
       "trapRx085BX4FactoryDataCRCAlarm": trapRx085BX4FactoryDataCRCAlarm,
       "trapRx085BX4CalDataCRCAlarm": trapRx085BX4CalDataCRCAlarm,
       "trapRx085BX4DefaultAlarm": trapRx085BX4DefaultAlarm,
       "trapRx085BX4Mode1Alarm": trapRx085BX4Mode1Alarm,
       "trapRx085BX4Mode2Alarm": trapRx085BX4Mode2Alarm,
       "trapRx085BX4Mode3Alarm": trapRx085BX4Mode3Alarm,
       "trapRx085BX4Mode4Alarm": trapRx085BX4Mode4Alarm,
       "trapRx085BX4Output1SwitchedAlarm": trapRx085BX4Output1SwitchedAlarm,
       "trapRx085BX4Output2SwitchedAlarm": trapRx085BX4Output2SwitchedAlarm,
       "trapRx085BX4Output3SwitchedAlarm": trapRx085BX4Output3SwitchedAlarm,
       "trapRx085BX4Output4SwitchedAlarm": trapRx085BX4Output4SwitchedAlarm,
       "trapRx085BX4RX1StatusAlarm": trapRx085BX4RX1StatusAlarm,
       "trapRx085BX4RX2StatusAlarm": trapRx085BX4RX2StatusAlarm,
       "trapRx085BX4RX3StatusAlarm": trapRx085BX4RX3StatusAlarm,
       "trapRx085BX4RX4StatusAlarm": trapRx085BX4RX4StatusAlarm,
       "trapRx085BX4BackupCableAlarm": trapRx085BX4BackupCableAlarm,
       "trapRx085BX4OptPwr1BadAlarm": trapRx085BX4OptPwr1BadAlarm,
       "trapRx085BX4OptPwr2BadAlarm": trapRx085BX4OptPwr2BadAlarm,
       "trapRx085BX4OptPwr3BadAlarm": trapRx085BX4OptPwr3BadAlarm,
       "trapRx085BX4OptPwr4BadAlarm": trapRx085BX4OptPwr4BadAlarm,
       "gx2Rx085BX4Descriptor": gx2Rx085BX4Descriptor,
       "gx2Rx085BX4AnalogTable": gx2Rx085BX4AnalogTable,
       "gx2Rx085BX4AnalogEntry": gx2Rx085BX4AnalogEntry,
       "gx2Rx085BX4AnalogTableIndex": gx2Rx085BX4AnalogTableIndex,
       "rx085labelOptPowerOne": rx085labelOptPowerOne,
       "rx085uomOptPowerOne": rx085uomOptPowerOne,
       "rx085majorHighOptPowerOne": rx085majorHighOptPowerOne,
       "rx085majorLowOptPowerOne": rx085majorLowOptPowerOne,
       "rx085minorHighOptPowerOne": rx085minorHighOptPowerOne,
       "rx085minorLowOptPowerOne": rx085minorLowOptPowerOne,
       "rx085currentValueOptPowerOne": rx085currentValueOptPowerOne,
       "rx085stateFlagOptPowerOne": rx085stateFlagOptPowerOne,
       "rx085minValueOptPowerOne": rx085minValueOptPowerOne,
       "rx085maxValueOptPowerOne": rx085maxValueOptPowerOne,
       "rx085alarmStateOptPowerOne": rx085alarmStateOptPowerOne,
       "rx085labelOptPowerTwo": rx085labelOptPowerTwo,
       "rx085uomOptPowerTwo": rx085uomOptPowerTwo,
       "rx085majorHighOptPowerTwo": rx085majorHighOptPowerTwo,
       "rx085majorLowOptPowerTwo": rx085majorLowOptPowerTwo,
       "rx085minorHighOptPowerTwo": rx085minorHighOptPowerTwo,
       "rx085minorLowOptPowerTwo": rx085minorLowOptPowerTwo,
       "rx085currentValueOptPowerTwo": rx085currentValueOptPowerTwo,
       "rx085stateFlagOptPowerTwo": rx085stateFlagOptPowerTwo,
       "rx085minValueOptPowerTwo": rx085minValueOptPowerTwo,
       "rx085maxValueOptPowerTwo": rx085maxValueOptPowerTwo,
       "rx085alarmStateOptPowerTwo": rx085alarmStateOptPowerTwo,
       "rx085labelOptPowerThree": rx085labelOptPowerThree,
       "rx085uomOptPowerThree": rx085uomOptPowerThree,
       "rx085majorHighOptPowerThree": rx085majorHighOptPowerThree,
       "rx085majorLowOptPowerThree": rx085majorLowOptPowerThree,
       "rx085minorHighOptPowerThree": rx085minorHighOptPowerThree,
       "rx085minorLowOptPowerThree": rx085minorLowOptPowerThree,
       "rx085currentValueOptPowerThree": rx085currentValueOptPowerThree,
       "rx085stateFlagOptPowerThree": rx085stateFlagOptPowerThree,
       "rx085minValueOptPowerThree": rx085minValueOptPowerThree,
       "rx085maxValueOptPowerThree": rx085maxValueOptPowerThree,
       "rx085alarmStateOptPowerThree": rx085alarmStateOptPowerThree,
       "rx085labelOptPowerFour": rx085labelOptPowerFour,
       "rx085uomOptPowerFour": rx085uomOptPowerFour,
       "rx085majorHighOptPowerFour": rx085majorHighOptPowerFour,
       "rx085majorLowOptPowerFour": rx085majorLowOptPowerFour,
       "rx085minorHighOptPowerFour": rx085minorHighOptPowerFour,
       "rx085minorLowOptPowerFour": rx085minorLowOptPowerFour,
       "rx085currentValueOptPowerFour": rx085currentValueOptPowerFour,
       "rx085stateFlagOptPowerFour": rx085stateFlagOptPowerFour,
       "rx085minValueOptPowerFour": rx085minValueOptPowerFour,
       "rx085maxValueOptPowerFour": rx085maxValueOptPowerFour,
       "rx085alarmStateOptPowerFour": rx085alarmStateOptPowerFour,
       "rx085labelModTemp": rx085labelModTemp,
       "rx085uomModTemp": rx085uomModTemp,
       "rx085majorHighModTemp": rx085majorHighModTemp,
       "rx085majorLowModTemp": rx085majorLowModTemp,
       "rx085minorHighModTemp": rx085minorHighModTemp,
       "rx085minorLowModTemp": rx085minorLowModTemp,
       "rx085currentValueModTemp": rx085currentValueModTemp,
       "rx085stateFlagModTemp": rx085stateFlagModTemp,
       "rx085minValueModTemp": rx085minValueModTemp,
       "rx085maxValueModTemp": rx085maxValueModTemp,
       "rx085alarmStateModTemp": rx085alarmStateModTemp,
       "rx085labelFanCurrent": rx085labelFanCurrent,
       "rx085uomFanCurrent": rx085uomFanCurrent,
       "rx085majorHighFanCurrent": rx085majorHighFanCurrent,
       "rx085majorLowFanCurrent": rx085majorLowFanCurrent,
       "rx085minorHighFanCurrent": rx085minorHighFanCurrent,
       "rx085minorLowFanCurrent": rx085minorLowFanCurrent,
       "rx085currentValueFanCurrent": rx085currentValueFanCurrent,
       "rx085stateFlagFanCurrent": rx085stateFlagFanCurrent,
       "rx085minValueFanCurrent": rx085minValueFanCurrent,
       "rx085maxValueFanCurrent": rx085maxValueFanCurrent,
       "rx085alarmStateFanCurrent": rx085alarmStateFanCurrent,
       "rx085label12Volt": rx085label12Volt,
       "rx085uom12Volt": rx085uom12Volt,
       "rx085majorHigh12Volt": rx085majorHigh12Volt,
       "rx085majorLow12Volt": rx085majorLow12Volt,
       "rx085minorHigh12Volt": rx085minorHigh12Volt,
       "rx085minorLow12Volt": rx085minorLow12Volt,
       "rx085currentValue12Volt": rx085currentValue12Volt,
       "rx085stateFlag12Volt": rx085stateFlag12Volt,
       "rx085minValue12Volt": rx085minValue12Volt,
       "rx085maxValue12Volt": rx085maxValue12Volt,
       "rx085alarmState12Volt": rx085alarmState12Volt,
       "gx2Rx085BX4DigitalTable": gx2Rx085BX4DigitalTable,
       "gx2Rx085BX4DigitalEntry": gx2Rx085BX4DigitalEntry,
       "gx2Rx085BX4DigitalTableIndex": gx2Rx085BX4DigitalTableIndex,
       "rx085labelModeOne": rx085labelModeOne,
       "rx085enumModeOne": rx085enumModeOne,
       "rx085valueModeOne": rx085valueModeOne,
       "rx085stateFlagModeOne": rx085stateFlagModeOne,
       "rx085labelWavelengthOne": rx085labelWavelengthOne,
       "rx085enumWavelengthOne": rx085enumWavelengthOne,
       "rx085valueWavelengthOne": rx085valueWavelengthOne,
       "rx085stateFlagWavelengthOne": rx085stateFlagWavelengthOne,
       "rx085labelAttnSettingOne": rx085labelAttnSettingOne,
       "rx085enumAttnSettingOne": rx085enumAttnSettingOne,
       "rx085valueAttnSettingOne": rx085valueAttnSettingOne,
       "rx085stateFlagAttnSettingOne": rx085stateFlagAttnSettingOne,
       "rx085labelSwModeSettingOne": rx085labelSwModeSettingOne,
       "rx085enumSwModeSettingOne": rx085enumSwModeSettingOne,
       "rx085valueSwModeSettingOne": rx085valueSwModeSettingOne,
       "rx085stateFlagSwModeSettingOne": rx085stateFlagSwModeSettingOne,
       "rx085labelSwModeThresholdOne": rx085labelSwModeThresholdOne,
       "rx085enumSwModeThresholdOne": rx085enumSwModeThresholdOne,
       "rx085valueSwModeThresholdOne": rx085valueSwModeThresholdOne,
       "rx085stateFlagSwModeThresholdOne": rx085stateFlagSwModeThresholdOne,
       "rx085labelModeTwo": rx085labelModeTwo,
       "rx085enumModeTwo": rx085enumModeTwo,
       "rx085valueModeTwo": rx085valueModeTwo,
       "rx085stateFlagModeTwo": rx085stateFlagModeTwo,
       "rx085labelWavelengthTwo": rx085labelWavelengthTwo,
       "rx085enumWavelengthTwo": rx085enumWavelengthTwo,
       "rx085valueWavelengthTwo": rx085valueWavelengthTwo,
       "rx085stateFlagWavelengthTwo": rx085stateFlagWavelengthTwo,
       "rx085labelAttnSettingTwo": rx085labelAttnSettingTwo,
       "rx085enumAttnSettingTwo": rx085enumAttnSettingTwo,
       "rx085valueAttnSettingTwo": rx085valueAttnSettingTwo,
       "rx085stateFlagAttnSettingTwo": rx085stateFlagAttnSettingTwo,
       "rx085labelSwModeSettingTwo": rx085labelSwModeSettingTwo,
       "rx085enumSwModeSettingTwo": rx085enumSwModeSettingTwo,
       "rx085valueSwModeSettingTwo": rx085valueSwModeSettingTwo,
       "rx085stateFlagSwModeSettingTwo": rx085stateFlagSwModeSettingTwo,
       "rx085labelSwModeThresholdTwo": rx085labelSwModeThresholdTwo,
       "rx085enumSwModeThresholdTwo": rx085enumSwModeThresholdTwo,
       "rx085valueSwModeThresholdTwo": rx085valueSwModeThresholdTwo,
       "rx085stateFlagSwModeThresholdTwo": rx085stateFlagSwModeThresholdTwo,
       "rx085labelModeThree": rx085labelModeThree,
       "rx085enumModeThree": rx085enumModeThree,
       "rx085valueModeThree": rx085valueModeThree,
       "rx085stateFlagModeThree": rx085stateFlagModeThree,
       "rx085labelWavelengthThree": rx085labelWavelengthThree,
       "rx085enumWavelengthThree": rx085enumWavelengthThree,
       "rx085valueWavelengthThree": rx085valueWavelengthThree,
       "rx085stateFlagWavelengthThree": rx085stateFlagWavelengthThree,
       "rx085labelAttnSettingThree": rx085labelAttnSettingThree,
       "rx085enumAttnSettingThree": rx085enumAttnSettingThree,
       "rx085valueAttnSettingThree": rx085valueAttnSettingThree,
       "rx085stateFlagAttnSettingThree": rx085stateFlagAttnSettingThree,
       "rx085labelSwModeSettingThree": rx085labelSwModeSettingThree,
       "rx085enumSwModeSettingThree": rx085enumSwModeSettingThree,
       "rx085valueSwModeSettingThree": rx085valueSwModeSettingThree,
       "rx085stateFlagSwModeSettingThree": rx085stateFlagSwModeSettingThree,
       "rx085labelSwModeThresholdThree": rx085labelSwModeThresholdThree,
       "rx085enumSwModeThresholdThree": rx085enumSwModeThresholdThree,
       "rx085valueSwModeThresholdThree": rx085valueSwModeThresholdThree,
       "rx085stateFlagSwModeThresholdThree": rx085stateFlagSwModeThresholdThree,
       "rx085labelModeFour": rx085labelModeFour,
       "rx085enumModeFour": rx085enumModeFour,
       "rx085valueModeFour": rx085valueModeFour,
       "rx085stateFlagModeFour": rx085stateFlagModeFour,
       "rx085labelWavelengthFour": rx085labelWavelengthFour,
       "rx085enumWavelengthFour": rx085enumWavelengthFour,
       "rx085valueWavelengthFour": rx085valueWavelengthFour,
       "rx085stateFlagWavelengthFour": rx085stateFlagWavelengthFour,
       "rx085labelAttnSettingFour": rx085labelAttnSettingFour,
       "rx085enumAttnSettingFour": rx085enumAttnSettingFour,
       "rx085valueAttnSettingFour": rx085valueAttnSettingFour,
       "rx085stateFlagAttnSettingFour": rx085stateFlagAttnSettingFour,
       "rx085labelSwModeSettingFour": rx085labelSwModeSettingFour,
       "rx085enumSwModeSettingFour": rx085enumSwModeSettingFour,
       "rx085valueSwModeSettingFour": rx085valueSwModeSettingFour,
       "rx085stateFlagSwModeSettingFour": rx085stateFlagSwModeSettingFour,
       "rx085labelSwModeThresholdFour": rx085labelSwModeThresholdFour,
       "rx085enumSwModeThresholdFour": rx085enumSwModeThresholdFour,
       "rx085valueSwModeThresholdFour": rx085valueSwModeThresholdFour,
       "rx085stateFlagSwModeThresholdFour": rx085stateFlagSwModeThresholdFour,
       "rx085labelModuleConfig": rx085labelModuleConfig,
       "rx085enumModuleConfig": rx085enumModuleConfig,
       "rx085valueModuleConfig": rx085valueModuleConfig,
       "rx085stateFlagModuleConfig": rx085stateFlagModuleConfig,
       "rx085labelRevertTime": rx085labelRevertTime,
       "rx085enumRevertTime": rx085enumRevertTime,
       "rx085valueRevertTime": rx085valueRevertTime,
       "rx085stateFlagRevertTime": rx085stateFlagRevertTime,
       "rx085labelTestPointSelect": rx085labelTestPointSelect,
       "rx085enumTestPointSelect": rx085enumTestPointSelect,
       "rx085valueTestPointSelect": rx085valueTestPointSelect,
       "rx085stateFlagTestPointSelect": rx085stateFlagTestPointSelect,
       "rx085labelFactoryDefault": rx085labelFactoryDefault,
       "rx085enumFactoryDefault": rx085enumFactoryDefault,
       "rx085valueFactoryDefault": rx085valueFactoryDefault,
       "rx085stateFlagFactoryDefault": rx085stateFlagFactoryDefault,
       "gx2Rx085BX4StatusTable": gx2Rx085BX4StatusTable,
       "gx2Rx085BX4StatusEntry": gx2Rx085BX4StatusEntry,
       "gx2Rx085BX4StatusTableIndex": gx2Rx085BX4StatusTableIndex,
       "rx085labelBoot": rx085labelBoot,
       "rx085valueBoot": rx085valueBoot,
       "rx085stateflagBoot": rx085stateflagBoot,
       "rx085labelFlash": rx085labelFlash,
       "rx085valueFlash": rx085valueFlash,
       "rx085stateflagFlash": rx085stateflagFlash,
       "rx085labelFactoryDataCRC": rx085labelFactoryDataCRC,
       "rx085valueFactoryDataCRC": rx085valueFactoryDataCRC,
       "rx085stateflagFactoryDataCRC": rx085stateflagFactoryDataCRC,
       "rx085labelAlarmDataCRC": rx085labelAlarmDataCRC,
       "rx085valueAlarmDataCRC": rx085valueAlarmDataCRC,
       "rx085stateflagAlarmDataCRC": rx085stateflagAlarmDataCRC,
       "rx085labelCalibrationDataCRC": rx085labelCalibrationDataCRC,
       "rx085valueCalibrationDataCRC": rx085valueCalibrationDataCRC,
       "rx085stateflagCalibrationDataCRC": rx085stateflagCalibrationDataCRC,
       "rx085labelHW": rx085labelHW,
       "rx085valueHW": rx085valueHW,
       "rx085stateflagHW": rx085stateflagHW,
       "rx085labelOptSigOne": rx085labelOptSigOne,
       "rx085valueOptSigOne": rx085valueOptSigOne,
       "rx085stateflagOptSigOne": rx085stateflagOptSigOne,
       "rx085labelOptSigTwo": rx085labelOptSigTwo,
       "rx085valueOptSigTwo": rx085valueOptSigTwo,
       "rx085stateflagOptSigTwo": rx085stateflagOptSigTwo,
       "rx085labelOptSigThree": rx085labelOptSigThree,
       "rx085valueOptSigThree": rx085valueOptSigThree,
       "rx085stateflagOptSigThree": rx085stateflagOptSigThree,
       "rx085labelOptSigFour": rx085labelOptSigFour,
       "rx085valueOptSigFour": rx085valueOptSigFour,
       "rx085stateflagOptSigFour": rx085stateflagOptSigFour,
       "rx085labelBackupCable": rx085labelBackupCable,
       "rx085valueBackupCable": rx085valueBackupCable,
       "rx085stateflagBackupCable": rx085stateflagBackupCable,
       "gx2Rx085BX4FactoryTable": gx2Rx085BX4FactoryTable,
       "gx2Rx085BX4FactoryEntry": gx2Rx085BX4FactoryEntry,
       "gx2Rx085BX4FactoryTableIndex": gx2Rx085BX4FactoryTableIndex,
       "rx085bootControlByte": rx085bootControlByte,
       "rx085bootStatusByte": rx085bootStatusByte,
       "rx085bank0CRC": rx085bank0CRC,
       "rx085bank1CRC": rx085bank1CRC,
       "rx085prgEEPROMByte": rx085prgEEPROMByte,
       "rx085factoryCRC": rx085factoryCRC,
       "rx085calculateCRC": rx085calculateCRC,
       "rx085hourMeter": rx085hourMeter,
       "rx085flashPrgCntA": rx085flashPrgCntA,
       "rx085flashPrgCntB": rx085flashPrgCntB,
       "rx085fwRev0": rx085fwRev0,
       "rx085fwRev1": rx085fwRev1}
)
