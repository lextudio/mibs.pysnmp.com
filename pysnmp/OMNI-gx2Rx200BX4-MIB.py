# SNMP MIB module (OMNI-gx2Rx200BX4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2Rx200BX4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:36 2024
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

(gx2Rx200BX4,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Rx200BX4")

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

_Gx2Rx200BX4Descriptor_ObjectIdentity = ObjectIdentity
gx2Rx200BX4Descriptor = _Gx2Rx200BX4Descriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 1)
)
_Gx2Rx200BX4AnalogTable_Object = MibTable
gx2Rx200BX4AnalogTable = _Gx2Rx200BX4AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2)
)
if mibBuilder.loadTexts:
    gx2Rx200BX4AnalogTable.setStatus("mandatory")
_Gx2Rx200BX4AnalogEntry_Object = MibTableRow
gx2Rx200BX4AnalogEntry = _Gx2Rx200BX4AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1)
)
gx2Rx200BX4AnalogEntry.setIndexNames(
    (0, "OMNI-gx2Rx200BX4-MIB", "gx2Rx200BX4AnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx200BX4AnalogEntry.setStatus("mandatory")


class _Gx2Rx200BX4AnalogTableIndex_Type(Integer32):
    """Custom type gx2Rx200BX4AnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx200BX4AnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Rx200BX4AnalogTableIndex_Object = MibTableColumn
gx2Rx200BX4AnalogTableIndex = _Gx2Rx200BX4AnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 1),
    _Gx2Rx200BX4AnalogTableIndex_Type()
)
gx2Rx200BX4AnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx200BX4AnalogTableIndex.setStatus("mandatory")


class _Rx4labelOptPowerOne_Type(DisplayString):
    """Custom type rx4labelOptPowerOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelOptPowerOne_Type.__name__ = "DisplayString"
_Rx4labelOptPowerOne_Object = MibTableColumn
rx4labelOptPowerOne = _Rx4labelOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 2),
    _Rx4labelOptPowerOne_Type()
)
rx4labelOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelOptPowerOne.setStatus("optional")


class _Rx4uomOptPowerOne_Type(DisplayString):
    """Custom type rx4uomOptPowerOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4uomOptPowerOne_Type.__name__ = "DisplayString"
_Rx4uomOptPowerOne_Object = MibTableColumn
rx4uomOptPowerOne = _Rx4uomOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 3),
    _Rx4uomOptPowerOne_Type()
)
rx4uomOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4uomOptPowerOne.setStatus("optional")
_Rx4majorHighOptPowerOne_Type = Float
_Rx4majorHighOptPowerOne_Object = MibTableColumn
rx4majorHighOptPowerOne = _Rx4majorHighOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 4),
    _Rx4majorHighOptPowerOne_Type()
)
rx4majorHighOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorHighOptPowerOne.setStatus("mandatory")
_Rx4majorLowOptPowerOne_Type = Float
_Rx4majorLowOptPowerOne_Object = MibTableColumn
rx4majorLowOptPowerOne = _Rx4majorLowOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 5),
    _Rx4majorLowOptPowerOne_Type()
)
rx4majorLowOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorLowOptPowerOne.setStatus("mandatory")
_Rx4minorHighOptPowerOne_Type = Float
_Rx4minorHighOptPowerOne_Object = MibTableColumn
rx4minorHighOptPowerOne = _Rx4minorHighOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 6),
    _Rx4minorHighOptPowerOne_Type()
)
rx4minorHighOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorHighOptPowerOne.setStatus("mandatory")
_Rx4minorLowOptPowerOne_Type = Float
_Rx4minorLowOptPowerOne_Object = MibTableColumn
rx4minorLowOptPowerOne = _Rx4minorLowOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 7),
    _Rx4minorLowOptPowerOne_Type()
)
rx4minorLowOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorLowOptPowerOne.setStatus("mandatory")
_Rx4currentValueOptPowerOne_Type = Float
_Rx4currentValueOptPowerOne_Object = MibTableColumn
rx4currentValueOptPowerOne = _Rx4currentValueOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 8),
    _Rx4currentValueOptPowerOne_Type()
)
rx4currentValueOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4currentValueOptPowerOne.setStatus("mandatory")


class _Rx4stateFlagOptPowerOne_Type(Integer32):
    """Custom type rx4stateFlagOptPowerOne based on Integer32"""
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


_Rx4stateFlagOptPowerOne_Type.__name__ = "Integer32"
_Rx4stateFlagOptPowerOne_Object = MibTableColumn
rx4stateFlagOptPowerOne = _Rx4stateFlagOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 9),
    _Rx4stateFlagOptPowerOne_Type()
)
rx4stateFlagOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagOptPowerOne.setStatus("mandatory")
_Rx4minValueOptPowerOne_Type = Float
_Rx4minValueOptPowerOne_Object = MibTableColumn
rx4minValueOptPowerOne = _Rx4minValueOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 10),
    _Rx4minValueOptPowerOne_Type()
)
rx4minValueOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minValueOptPowerOne.setStatus("mandatory")
_Rx4maxValueOptPowerOne_Type = Float
_Rx4maxValueOptPowerOne_Object = MibTableColumn
rx4maxValueOptPowerOne = _Rx4maxValueOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 11),
    _Rx4maxValueOptPowerOne_Type()
)
rx4maxValueOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4maxValueOptPowerOne.setStatus("mandatory")


class _Rx4alarmStateOptPowerOne_Type(Integer32):
    """Custom type rx4alarmStateOptPowerOne based on Integer32"""
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


_Rx4alarmStateOptPowerOne_Type.__name__ = "Integer32"
_Rx4alarmStateOptPowerOne_Object = MibTableColumn
rx4alarmStateOptPowerOne = _Rx4alarmStateOptPowerOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 12),
    _Rx4alarmStateOptPowerOne_Type()
)
rx4alarmStateOptPowerOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4alarmStateOptPowerOne.setStatus("mandatory")


class _Rx4labelOptPowerTwo_Type(DisplayString):
    """Custom type rx4labelOptPowerTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelOptPowerTwo_Type.__name__ = "DisplayString"
_Rx4labelOptPowerTwo_Object = MibTableColumn
rx4labelOptPowerTwo = _Rx4labelOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 13),
    _Rx4labelOptPowerTwo_Type()
)
rx4labelOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelOptPowerTwo.setStatus("optional")


class _Rx4uomOptPowerTwo_Type(DisplayString):
    """Custom type rx4uomOptPowerTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4uomOptPowerTwo_Type.__name__ = "DisplayString"
_Rx4uomOptPowerTwo_Object = MibTableColumn
rx4uomOptPowerTwo = _Rx4uomOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 14),
    _Rx4uomOptPowerTwo_Type()
)
rx4uomOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4uomOptPowerTwo.setStatus("optional")
_Rx4majorHighOptPowerTwo_Type = Float
_Rx4majorHighOptPowerTwo_Object = MibTableColumn
rx4majorHighOptPowerTwo = _Rx4majorHighOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 15),
    _Rx4majorHighOptPowerTwo_Type()
)
rx4majorHighOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorHighOptPowerTwo.setStatus("mandatory")
_Rx4majorLowOptPowerTwo_Type = Float
_Rx4majorLowOptPowerTwo_Object = MibTableColumn
rx4majorLowOptPowerTwo = _Rx4majorLowOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 16),
    _Rx4majorLowOptPowerTwo_Type()
)
rx4majorLowOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorLowOptPowerTwo.setStatus("mandatory")
_Rx4minorHighOptPowerTwo_Type = Float
_Rx4minorHighOptPowerTwo_Object = MibTableColumn
rx4minorHighOptPowerTwo = _Rx4minorHighOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 17),
    _Rx4minorHighOptPowerTwo_Type()
)
rx4minorHighOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorHighOptPowerTwo.setStatus("mandatory")
_Rx4minorLowOptPowerTwo_Type = Float
_Rx4minorLowOptPowerTwo_Object = MibTableColumn
rx4minorLowOptPowerTwo = _Rx4minorLowOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 18),
    _Rx4minorLowOptPowerTwo_Type()
)
rx4minorLowOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorLowOptPowerTwo.setStatus("mandatory")
_Rx4currentValueOptPowerTwo_Type = Float
_Rx4currentValueOptPowerTwo_Object = MibTableColumn
rx4currentValueOptPowerTwo = _Rx4currentValueOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 19),
    _Rx4currentValueOptPowerTwo_Type()
)
rx4currentValueOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4currentValueOptPowerTwo.setStatus("mandatory")


class _Rx4stateFlagOptPowerTwo_Type(Integer32):
    """Custom type rx4stateFlagOptPowerTwo based on Integer32"""
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


_Rx4stateFlagOptPowerTwo_Type.__name__ = "Integer32"
_Rx4stateFlagOptPowerTwo_Object = MibTableColumn
rx4stateFlagOptPowerTwo = _Rx4stateFlagOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 20),
    _Rx4stateFlagOptPowerTwo_Type()
)
rx4stateFlagOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagOptPowerTwo.setStatus("mandatory")
_Rx4minValueOptPowerTwo_Type = Float
_Rx4minValueOptPowerTwo_Object = MibTableColumn
rx4minValueOptPowerTwo = _Rx4minValueOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 21),
    _Rx4minValueOptPowerTwo_Type()
)
rx4minValueOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minValueOptPowerTwo.setStatus("mandatory")
_Rx4maxValueOptPowerTwo_Type = Float
_Rx4maxValueOptPowerTwo_Object = MibTableColumn
rx4maxValueOptPowerTwo = _Rx4maxValueOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 22),
    _Rx4maxValueOptPowerTwo_Type()
)
rx4maxValueOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4maxValueOptPowerTwo.setStatus("mandatory")


class _Rx4alarmStateOptPowerTwo_Type(Integer32):
    """Custom type rx4alarmStateOptPowerTwo based on Integer32"""
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


_Rx4alarmStateOptPowerTwo_Type.__name__ = "Integer32"
_Rx4alarmStateOptPowerTwo_Object = MibTableColumn
rx4alarmStateOptPowerTwo = _Rx4alarmStateOptPowerTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 23),
    _Rx4alarmStateOptPowerTwo_Type()
)
rx4alarmStateOptPowerTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4alarmStateOptPowerTwo.setStatus("mandatory")


class _Rx4labelOptPowerThree_Type(DisplayString):
    """Custom type rx4labelOptPowerThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelOptPowerThree_Type.__name__ = "DisplayString"
_Rx4labelOptPowerThree_Object = MibTableColumn
rx4labelOptPowerThree = _Rx4labelOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 24),
    _Rx4labelOptPowerThree_Type()
)
rx4labelOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelOptPowerThree.setStatus("optional")


class _Rx4uomOptPowerThree_Type(DisplayString):
    """Custom type rx4uomOptPowerThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4uomOptPowerThree_Type.__name__ = "DisplayString"
_Rx4uomOptPowerThree_Object = MibTableColumn
rx4uomOptPowerThree = _Rx4uomOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 25),
    _Rx4uomOptPowerThree_Type()
)
rx4uomOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4uomOptPowerThree.setStatus("optional")
_Rx4majorHighOptPowerThree_Type = Float
_Rx4majorHighOptPowerThree_Object = MibTableColumn
rx4majorHighOptPowerThree = _Rx4majorHighOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 26),
    _Rx4majorHighOptPowerThree_Type()
)
rx4majorHighOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorHighOptPowerThree.setStatus("mandatory")
_Rx4majorLowOptPowerThree_Type = Float
_Rx4majorLowOptPowerThree_Object = MibTableColumn
rx4majorLowOptPowerThree = _Rx4majorLowOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 27),
    _Rx4majorLowOptPowerThree_Type()
)
rx4majorLowOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorLowOptPowerThree.setStatus("mandatory")
_Rx4minorHighOptPowerThree_Type = Float
_Rx4minorHighOptPowerThree_Object = MibTableColumn
rx4minorHighOptPowerThree = _Rx4minorHighOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 28),
    _Rx4minorHighOptPowerThree_Type()
)
rx4minorHighOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorHighOptPowerThree.setStatus("mandatory")
_Rx4minorLowOptPowerThree_Type = Float
_Rx4minorLowOptPowerThree_Object = MibTableColumn
rx4minorLowOptPowerThree = _Rx4minorLowOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 29),
    _Rx4minorLowOptPowerThree_Type()
)
rx4minorLowOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorLowOptPowerThree.setStatus("mandatory")
_Rx4currentValueOptPowerThree_Type = Float
_Rx4currentValueOptPowerThree_Object = MibTableColumn
rx4currentValueOptPowerThree = _Rx4currentValueOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 30),
    _Rx4currentValueOptPowerThree_Type()
)
rx4currentValueOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4currentValueOptPowerThree.setStatus("mandatory")


class _Rx4stateFlagOptPowerThree_Type(Integer32):
    """Custom type rx4stateFlagOptPowerThree based on Integer32"""
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


_Rx4stateFlagOptPowerThree_Type.__name__ = "Integer32"
_Rx4stateFlagOptPowerThree_Object = MibTableColumn
rx4stateFlagOptPowerThree = _Rx4stateFlagOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 31),
    _Rx4stateFlagOptPowerThree_Type()
)
rx4stateFlagOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagOptPowerThree.setStatus("mandatory")
_Rx4minValueOptPowerThree_Type = Float
_Rx4minValueOptPowerThree_Object = MibTableColumn
rx4minValueOptPowerThree = _Rx4minValueOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 32),
    _Rx4minValueOptPowerThree_Type()
)
rx4minValueOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minValueOptPowerThree.setStatus("mandatory")
_Rx4maxValueOptPowerThree_Type = Float
_Rx4maxValueOptPowerThree_Object = MibTableColumn
rx4maxValueOptPowerThree = _Rx4maxValueOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 33),
    _Rx4maxValueOptPowerThree_Type()
)
rx4maxValueOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4maxValueOptPowerThree.setStatus("mandatory")


class _Rx4alarmStateOptPowerThree_Type(Integer32):
    """Custom type rx4alarmStateOptPowerThree based on Integer32"""
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


_Rx4alarmStateOptPowerThree_Type.__name__ = "Integer32"
_Rx4alarmStateOptPowerThree_Object = MibTableColumn
rx4alarmStateOptPowerThree = _Rx4alarmStateOptPowerThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 34),
    _Rx4alarmStateOptPowerThree_Type()
)
rx4alarmStateOptPowerThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4alarmStateOptPowerThree.setStatus("mandatory")


class _Rx4labelOptPowerFour_Type(DisplayString):
    """Custom type rx4labelOptPowerFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelOptPowerFour_Type.__name__ = "DisplayString"
_Rx4labelOptPowerFour_Object = MibTableColumn
rx4labelOptPowerFour = _Rx4labelOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 35),
    _Rx4labelOptPowerFour_Type()
)
rx4labelOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelOptPowerFour.setStatus("optional")


class _Rx4uomOptPowerFour_Type(DisplayString):
    """Custom type rx4uomOptPowerFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4uomOptPowerFour_Type.__name__ = "DisplayString"
_Rx4uomOptPowerFour_Object = MibTableColumn
rx4uomOptPowerFour = _Rx4uomOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 36),
    _Rx4uomOptPowerFour_Type()
)
rx4uomOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4uomOptPowerFour.setStatus("optional")
_Rx4majorHighOptPowerFour_Type = Float
_Rx4majorHighOptPowerFour_Object = MibTableColumn
rx4majorHighOptPowerFour = _Rx4majorHighOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 37),
    _Rx4majorHighOptPowerFour_Type()
)
rx4majorHighOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorHighOptPowerFour.setStatus("mandatory")
_Rx4majorLowOptPowerFour_Type = Float
_Rx4majorLowOptPowerFour_Object = MibTableColumn
rx4majorLowOptPowerFour = _Rx4majorLowOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 38),
    _Rx4majorLowOptPowerFour_Type()
)
rx4majorLowOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorLowOptPowerFour.setStatus("mandatory")
_Rx4minorHighOptPowerFour_Type = Float
_Rx4minorHighOptPowerFour_Object = MibTableColumn
rx4minorHighOptPowerFour = _Rx4minorHighOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 39),
    _Rx4minorHighOptPowerFour_Type()
)
rx4minorHighOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorHighOptPowerFour.setStatus("mandatory")
_Rx4minorLowOptPowerFour_Type = Float
_Rx4minorLowOptPowerFour_Object = MibTableColumn
rx4minorLowOptPowerFour = _Rx4minorLowOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 40),
    _Rx4minorLowOptPowerFour_Type()
)
rx4minorLowOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorLowOptPowerFour.setStatus("mandatory")
_Rx4currentValueOptPowerFour_Type = Float
_Rx4currentValueOptPowerFour_Object = MibTableColumn
rx4currentValueOptPowerFour = _Rx4currentValueOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 41),
    _Rx4currentValueOptPowerFour_Type()
)
rx4currentValueOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4currentValueOptPowerFour.setStatus("mandatory")


class _Rx4stateFlagOptPowerFour_Type(Integer32):
    """Custom type rx4stateFlagOptPowerFour based on Integer32"""
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


_Rx4stateFlagOptPowerFour_Type.__name__ = "Integer32"
_Rx4stateFlagOptPowerFour_Object = MibTableColumn
rx4stateFlagOptPowerFour = _Rx4stateFlagOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 42),
    _Rx4stateFlagOptPowerFour_Type()
)
rx4stateFlagOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagOptPowerFour.setStatus("mandatory")
_Rx4minValueOptPowerFour_Type = Float
_Rx4minValueOptPowerFour_Object = MibTableColumn
rx4minValueOptPowerFour = _Rx4minValueOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 43),
    _Rx4minValueOptPowerFour_Type()
)
rx4minValueOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minValueOptPowerFour.setStatus("mandatory")
_Rx4maxValueOptPowerFour_Type = Float
_Rx4maxValueOptPowerFour_Object = MibTableColumn
rx4maxValueOptPowerFour = _Rx4maxValueOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 44),
    _Rx4maxValueOptPowerFour_Type()
)
rx4maxValueOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4maxValueOptPowerFour.setStatus("mandatory")


class _Rx4alarmStateOptPowerFour_Type(Integer32):
    """Custom type rx4alarmStateOptPowerFour based on Integer32"""
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


_Rx4alarmStateOptPowerFour_Type.__name__ = "Integer32"
_Rx4alarmStateOptPowerFour_Object = MibTableColumn
rx4alarmStateOptPowerFour = _Rx4alarmStateOptPowerFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 45),
    _Rx4alarmStateOptPowerFour_Type()
)
rx4alarmStateOptPowerFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4alarmStateOptPowerFour.setStatus("mandatory")


class _Rx4labelModTemp_Type(DisplayString):
    """Custom type rx4labelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelModTemp_Type.__name__ = "DisplayString"
_Rx4labelModTemp_Object = MibTableColumn
rx4labelModTemp = _Rx4labelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 46),
    _Rx4labelModTemp_Type()
)
rx4labelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelModTemp.setStatus("optional")


class _Rx4uomModTemp_Type(DisplayString):
    """Custom type rx4uomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4uomModTemp_Type.__name__ = "DisplayString"
_Rx4uomModTemp_Object = MibTableColumn
rx4uomModTemp = _Rx4uomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 47),
    _Rx4uomModTemp_Type()
)
rx4uomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4uomModTemp.setStatus("optional")
_Rx4majorHighModTemp_Type = Float
_Rx4majorHighModTemp_Object = MibTableColumn
rx4majorHighModTemp = _Rx4majorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 48),
    _Rx4majorHighModTemp_Type()
)
rx4majorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorHighModTemp.setStatus("mandatory")
_Rx4majorLowModTemp_Type = Float
_Rx4majorLowModTemp_Object = MibTableColumn
rx4majorLowModTemp = _Rx4majorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 49),
    _Rx4majorLowModTemp_Type()
)
rx4majorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorLowModTemp.setStatus("mandatory")
_Rx4minorHighModTemp_Type = Float
_Rx4minorHighModTemp_Object = MibTableColumn
rx4minorHighModTemp = _Rx4minorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 50),
    _Rx4minorHighModTemp_Type()
)
rx4minorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorHighModTemp.setStatus("mandatory")
_Rx4minorLowModTemp_Type = Float
_Rx4minorLowModTemp_Object = MibTableColumn
rx4minorLowModTemp = _Rx4minorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 51),
    _Rx4minorLowModTemp_Type()
)
rx4minorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorLowModTemp.setStatus("mandatory")
_Rx4currentValueModTemp_Type = Float
_Rx4currentValueModTemp_Object = MibTableColumn
rx4currentValueModTemp = _Rx4currentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 52),
    _Rx4currentValueModTemp_Type()
)
rx4currentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4currentValueModTemp.setStatus("mandatory")


class _Rx4stateFlagModTemp_Type(Integer32):
    """Custom type rx4stateFlagModTemp based on Integer32"""
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


_Rx4stateFlagModTemp_Type.__name__ = "Integer32"
_Rx4stateFlagModTemp_Object = MibTableColumn
rx4stateFlagModTemp = _Rx4stateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 53),
    _Rx4stateFlagModTemp_Type()
)
rx4stateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagModTemp.setStatus("mandatory")
_Rx4minValueModTemp_Type = Float
_Rx4minValueModTemp_Object = MibTableColumn
rx4minValueModTemp = _Rx4minValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 54),
    _Rx4minValueModTemp_Type()
)
rx4minValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minValueModTemp.setStatus("mandatory")
_Rx4maxValueModTemp_Type = Float
_Rx4maxValueModTemp_Object = MibTableColumn
rx4maxValueModTemp = _Rx4maxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 55),
    _Rx4maxValueModTemp_Type()
)
rx4maxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4maxValueModTemp.setStatus("mandatory")


class _Rx4alarmStateModTemp_Type(Integer32):
    """Custom type rx4alarmStateModTemp based on Integer32"""
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


_Rx4alarmStateModTemp_Type.__name__ = "Integer32"
_Rx4alarmStateModTemp_Object = MibTableColumn
rx4alarmStateModTemp = _Rx4alarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 56),
    _Rx4alarmStateModTemp_Type()
)
rx4alarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4alarmStateModTemp.setStatus("mandatory")


class _Rx4labelFanCurrent_Type(DisplayString):
    """Custom type rx4labelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelFanCurrent_Type.__name__ = "DisplayString"
_Rx4labelFanCurrent_Object = MibTableColumn
rx4labelFanCurrent = _Rx4labelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 57),
    _Rx4labelFanCurrent_Type()
)
rx4labelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelFanCurrent.setStatus("optional")


class _Rx4uomFanCurrent_Type(DisplayString):
    """Custom type rx4uomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4uomFanCurrent_Type.__name__ = "DisplayString"
_Rx4uomFanCurrent_Object = MibTableColumn
rx4uomFanCurrent = _Rx4uomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 58),
    _Rx4uomFanCurrent_Type()
)
rx4uomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4uomFanCurrent.setStatus("optional")
_Rx4majorHighFanCurrent_Type = Float
_Rx4majorHighFanCurrent_Object = MibTableColumn
rx4majorHighFanCurrent = _Rx4majorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 59),
    _Rx4majorHighFanCurrent_Type()
)
rx4majorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorHighFanCurrent.setStatus("mandatory")
_Rx4majorLowFanCurrent_Type = Float
_Rx4majorLowFanCurrent_Object = MibTableColumn
rx4majorLowFanCurrent = _Rx4majorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 60),
    _Rx4majorLowFanCurrent_Type()
)
rx4majorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorLowFanCurrent.setStatus("mandatory")
_Rx4minorHighFanCurrent_Type = Float
_Rx4minorHighFanCurrent_Object = MibTableColumn
rx4minorHighFanCurrent = _Rx4minorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 61),
    _Rx4minorHighFanCurrent_Type()
)
rx4minorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorHighFanCurrent.setStatus("mandatory")
_Rx4minorLowFanCurrent_Type = Float
_Rx4minorLowFanCurrent_Object = MibTableColumn
rx4minorLowFanCurrent = _Rx4minorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 62),
    _Rx4minorLowFanCurrent_Type()
)
rx4minorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorLowFanCurrent.setStatus("mandatory")
_Rx4currentValueFanCurrent_Type = Float
_Rx4currentValueFanCurrent_Object = MibTableColumn
rx4currentValueFanCurrent = _Rx4currentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 63),
    _Rx4currentValueFanCurrent_Type()
)
rx4currentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4currentValueFanCurrent.setStatus("mandatory")


class _Rx4stateFlagFanCurrent_Type(Integer32):
    """Custom type rx4stateFlagFanCurrent based on Integer32"""
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


_Rx4stateFlagFanCurrent_Type.__name__ = "Integer32"
_Rx4stateFlagFanCurrent_Object = MibTableColumn
rx4stateFlagFanCurrent = _Rx4stateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 64),
    _Rx4stateFlagFanCurrent_Type()
)
rx4stateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagFanCurrent.setStatus("mandatory")
_Rx4minValueFanCurrent_Type = Float
_Rx4minValueFanCurrent_Object = MibTableColumn
rx4minValueFanCurrent = _Rx4minValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 65),
    _Rx4minValueFanCurrent_Type()
)
rx4minValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minValueFanCurrent.setStatus("mandatory")
_Rx4maxValueFanCurrent_Type = Float
_Rx4maxValueFanCurrent_Object = MibTableColumn
rx4maxValueFanCurrent = _Rx4maxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 66),
    _Rx4maxValueFanCurrent_Type()
)
rx4maxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4maxValueFanCurrent.setStatus("mandatory")


class _Rx4alarmStateFanCurrent_Type(Integer32):
    """Custom type rx4alarmStateFanCurrent based on Integer32"""
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


_Rx4alarmStateFanCurrent_Type.__name__ = "Integer32"
_Rx4alarmStateFanCurrent_Object = MibTableColumn
rx4alarmStateFanCurrent = _Rx4alarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 67),
    _Rx4alarmStateFanCurrent_Type()
)
rx4alarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4alarmStateFanCurrent.setStatus("mandatory")


class _Rx4label12Volt_Type(DisplayString):
    """Custom type rx4label12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4label12Volt_Type.__name__ = "DisplayString"
_Rx4label12Volt_Object = MibTableColumn
rx4label12Volt = _Rx4label12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 68),
    _Rx4label12Volt_Type()
)
rx4label12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4label12Volt.setStatus("optional")


class _Rx4uom12Volt_Type(DisplayString):
    """Custom type rx4uom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4uom12Volt_Type.__name__ = "DisplayString"
_Rx4uom12Volt_Object = MibTableColumn
rx4uom12Volt = _Rx4uom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 69),
    _Rx4uom12Volt_Type()
)
rx4uom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4uom12Volt.setStatus("optional")
_Rx4majorHigh12Volt_Type = Float
_Rx4majorHigh12Volt_Object = MibTableColumn
rx4majorHigh12Volt = _Rx4majorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 70),
    _Rx4majorHigh12Volt_Type()
)
rx4majorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorHigh12Volt.setStatus("mandatory")
_Rx4majorLow12Volt_Type = Float
_Rx4majorLow12Volt_Object = MibTableColumn
rx4majorLow12Volt = _Rx4majorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 71),
    _Rx4majorLow12Volt_Type()
)
rx4majorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4majorLow12Volt.setStatus("mandatory")
_Rx4minorHigh12Volt_Type = Float
_Rx4minorHigh12Volt_Object = MibTableColumn
rx4minorHigh12Volt = _Rx4minorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 72),
    _Rx4minorHigh12Volt_Type()
)
rx4minorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorHigh12Volt.setStatus("mandatory")
_Rx4minorLow12Volt_Type = Float
_Rx4minorLow12Volt_Object = MibTableColumn
rx4minorLow12Volt = _Rx4minorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 73),
    _Rx4minorLow12Volt_Type()
)
rx4minorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minorLow12Volt.setStatus("mandatory")
_Rx4currentValue12Volt_Type = Float
_Rx4currentValue12Volt_Object = MibTableColumn
rx4currentValue12Volt = _Rx4currentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 74),
    _Rx4currentValue12Volt_Type()
)
rx4currentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4currentValue12Volt.setStatus("mandatory")


class _Rx4stateFlag12Volt_Type(Integer32):
    """Custom type rx4stateFlag12Volt based on Integer32"""
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


_Rx4stateFlag12Volt_Type.__name__ = "Integer32"
_Rx4stateFlag12Volt_Object = MibTableColumn
rx4stateFlag12Volt = _Rx4stateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 75),
    _Rx4stateFlag12Volt_Type()
)
rx4stateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlag12Volt.setStatus("mandatory")
_Rx4minValue12Volt_Type = Float
_Rx4minValue12Volt_Object = MibTableColumn
rx4minValue12Volt = _Rx4minValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 76),
    _Rx4minValue12Volt_Type()
)
rx4minValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4minValue12Volt.setStatus("mandatory")
_Rx4maxValue12Volt_Type = Float
_Rx4maxValue12Volt_Object = MibTableColumn
rx4maxValue12Volt = _Rx4maxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 77),
    _Rx4maxValue12Volt_Type()
)
rx4maxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4maxValue12Volt.setStatus("mandatory")


class _Rx4alarmState12Volt_Type(Integer32):
    """Custom type rx4alarmState12Volt based on Integer32"""
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


_Rx4alarmState12Volt_Type.__name__ = "Integer32"
_Rx4alarmState12Volt_Object = MibTableColumn
rx4alarmState12Volt = _Rx4alarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 2, 1, 78),
    _Rx4alarmState12Volt_Type()
)
rx4alarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4alarmState12Volt.setStatus("mandatory")
_Gx2Rx200BX4DigitalTable_Object = MibTable
gx2Rx200BX4DigitalTable = _Gx2Rx200BX4DigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3)
)
if mibBuilder.loadTexts:
    gx2Rx200BX4DigitalTable.setStatus("mandatory")
_Gx2Rx200BX4DigitalEntry_Object = MibTableRow
gx2Rx200BX4DigitalEntry = _Gx2Rx200BX4DigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2)
)
gx2Rx200BX4DigitalEntry.setIndexNames(
    (0, "OMNI-gx2Rx200BX4-MIB", "gx2Rx200BX4DigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx200BX4DigitalEntry.setStatus("mandatory")


class _Gx2Rx200BX4DigitalTableIndex_Type(Integer32):
    """Custom type gx2Rx200BX4DigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx200BX4DigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Rx200BX4DigitalTableIndex_Object = MibTableColumn
gx2Rx200BX4DigitalTableIndex = _Gx2Rx200BX4DigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 1),
    _Gx2Rx200BX4DigitalTableIndex_Type()
)
gx2Rx200BX4DigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx200BX4DigitalTableIndex.setStatus("mandatory")


class _Rx4labelModeOne_Type(DisplayString):
    """Custom type rx4labelModeOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelModeOne_Type.__name__ = "DisplayString"
_Rx4labelModeOne_Object = MibTableColumn
rx4labelModeOne = _Rx4labelModeOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 2),
    _Rx4labelModeOne_Type()
)
rx4labelModeOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelModeOne.setStatus("optional")


class _Rx4enumModeOne_Type(DisplayString):
    """Custom type rx4enumModeOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumModeOne_Type.__name__ = "DisplayString"
_Rx4enumModeOne_Object = MibTableColumn
rx4enumModeOne = _Rx4enumModeOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 3),
    _Rx4enumModeOne_Type()
)
rx4enumModeOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumModeOne.setStatus("optional")


class _Rx4valueModeOne_Type(Integer32):
    """Custom type rx4valueModeOne based on Integer32"""
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


_Rx4valueModeOne_Type.__name__ = "Integer32"
_Rx4valueModeOne_Object = MibTableColumn
rx4valueModeOne = _Rx4valueModeOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 4),
    _Rx4valueModeOne_Type()
)
rx4valueModeOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueModeOne.setStatus("mandatory")


class _Rx4stateFlagModeOne_Type(Integer32):
    """Custom type rx4stateFlagModeOne based on Integer32"""
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


_Rx4stateFlagModeOne_Type.__name__ = "Integer32"
_Rx4stateFlagModeOne_Object = MibTableColumn
rx4stateFlagModeOne = _Rx4stateFlagModeOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 5),
    _Rx4stateFlagModeOne_Type()
)
rx4stateFlagModeOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagModeOne.setStatus("mandatory")


class _Rx4labelWavelengthOne_Type(DisplayString):
    """Custom type rx4labelWavelengthOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelWavelengthOne_Type.__name__ = "DisplayString"
_Rx4labelWavelengthOne_Object = MibTableColumn
rx4labelWavelengthOne = _Rx4labelWavelengthOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 6),
    _Rx4labelWavelengthOne_Type()
)
rx4labelWavelengthOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelWavelengthOne.setStatus("optional")


class _Rx4enumWavelengthOne_Type(DisplayString):
    """Custom type rx4enumWavelengthOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumWavelengthOne_Type.__name__ = "DisplayString"
_Rx4enumWavelengthOne_Object = MibTableColumn
rx4enumWavelengthOne = _Rx4enumWavelengthOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 7),
    _Rx4enumWavelengthOne_Type()
)
rx4enumWavelengthOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumWavelengthOne.setStatus("optional")


class _Rx4valueWavelengthOne_Type(Integer32):
    """Custom type rx4valueWavelengthOne based on Integer32"""
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


_Rx4valueWavelengthOne_Type.__name__ = "Integer32"
_Rx4valueWavelengthOne_Object = MibTableColumn
rx4valueWavelengthOne = _Rx4valueWavelengthOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 8),
    _Rx4valueWavelengthOne_Type()
)
rx4valueWavelengthOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueWavelengthOne.setStatus("mandatory")


class _Rx4stateFlagWavelengthOne_Type(Integer32):
    """Custom type rx4stateFlagWavelengthOne based on Integer32"""
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


_Rx4stateFlagWavelengthOne_Type.__name__ = "Integer32"
_Rx4stateFlagWavelengthOne_Object = MibTableColumn
rx4stateFlagWavelengthOne = _Rx4stateFlagWavelengthOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 9),
    _Rx4stateFlagWavelengthOne_Type()
)
rx4stateFlagWavelengthOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagWavelengthOne.setStatus("mandatory")


class _Rx4labelAttnSettingOne_Type(DisplayString):
    """Custom type rx4labelAttnSettingOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelAttnSettingOne_Type.__name__ = "DisplayString"
_Rx4labelAttnSettingOne_Object = MibTableColumn
rx4labelAttnSettingOne = _Rx4labelAttnSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 10),
    _Rx4labelAttnSettingOne_Type()
)
rx4labelAttnSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelAttnSettingOne.setStatus("optional")


class _Rx4enumAttnSettingOne_Type(DisplayString):
    """Custom type rx4enumAttnSettingOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumAttnSettingOne_Type.__name__ = "DisplayString"
_Rx4enumAttnSettingOne_Object = MibTableColumn
rx4enumAttnSettingOne = _Rx4enumAttnSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 11),
    _Rx4enumAttnSettingOne_Type()
)
rx4enumAttnSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumAttnSettingOne.setStatus("optional")
_Rx4valueAttnSettingOne_Type = Integer32
_Rx4valueAttnSettingOne_Object = MibTableColumn
rx4valueAttnSettingOne = _Rx4valueAttnSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 12),
    _Rx4valueAttnSettingOne_Type()
)
rx4valueAttnSettingOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueAttnSettingOne.setStatus("mandatory")


class _Rx4stateFlagAttnSettingOne_Type(Integer32):
    """Custom type rx4stateFlagAttnSettingOne based on Integer32"""
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


_Rx4stateFlagAttnSettingOne_Type.__name__ = "Integer32"
_Rx4stateFlagAttnSettingOne_Object = MibTableColumn
rx4stateFlagAttnSettingOne = _Rx4stateFlagAttnSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 13),
    _Rx4stateFlagAttnSettingOne_Type()
)
rx4stateFlagAttnSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagAttnSettingOne.setStatus("mandatory")


class _Rx4labelSwModeSettingOne_Type(DisplayString):
    """Custom type rx4labelSwModeSettingOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelSwModeSettingOne_Type.__name__ = "DisplayString"
_Rx4labelSwModeSettingOne_Object = MibTableColumn
rx4labelSwModeSettingOne = _Rx4labelSwModeSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 14),
    _Rx4labelSwModeSettingOne_Type()
)
rx4labelSwModeSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelSwModeSettingOne.setStatus("optional")


class _Rx4enumSwModeSettingOne_Type(DisplayString):
    """Custom type rx4enumSwModeSettingOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumSwModeSettingOne_Type.__name__ = "DisplayString"
_Rx4enumSwModeSettingOne_Object = MibTableColumn
rx4enumSwModeSettingOne = _Rx4enumSwModeSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 15),
    _Rx4enumSwModeSettingOne_Type()
)
rx4enumSwModeSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumSwModeSettingOne.setStatus("optional")


class _Rx4valueSwModeSettingOne_Type(Integer32):
    """Custom type rx4valueSwModeSettingOne based on Integer32"""
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


_Rx4valueSwModeSettingOne_Type.__name__ = "Integer32"
_Rx4valueSwModeSettingOne_Object = MibTableColumn
rx4valueSwModeSettingOne = _Rx4valueSwModeSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 16),
    _Rx4valueSwModeSettingOne_Type()
)
rx4valueSwModeSettingOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueSwModeSettingOne.setStatus("mandatory")


class _Rx4stateFlagSwModeSettingOne_Type(Integer32):
    """Custom type rx4stateFlagSwModeSettingOne based on Integer32"""
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


_Rx4stateFlagSwModeSettingOne_Type.__name__ = "Integer32"
_Rx4stateFlagSwModeSettingOne_Object = MibTableColumn
rx4stateFlagSwModeSettingOne = _Rx4stateFlagSwModeSettingOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 17),
    _Rx4stateFlagSwModeSettingOne_Type()
)
rx4stateFlagSwModeSettingOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagSwModeSettingOne.setStatus("mandatory")


class _Rx4labelSwModeThresholdOne_Type(DisplayString):
    """Custom type rx4labelSwModeThresholdOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelSwModeThresholdOne_Type.__name__ = "DisplayString"
_Rx4labelSwModeThresholdOne_Object = MibTableColumn
rx4labelSwModeThresholdOne = _Rx4labelSwModeThresholdOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 18),
    _Rx4labelSwModeThresholdOne_Type()
)
rx4labelSwModeThresholdOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelSwModeThresholdOne.setStatus("optional")


class _Rx4enumSwModeThresholdOne_Type(DisplayString):
    """Custom type rx4enumSwModeThresholdOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumSwModeThresholdOne_Type.__name__ = "DisplayString"
_Rx4enumSwModeThresholdOne_Object = MibTableColumn
rx4enumSwModeThresholdOne = _Rx4enumSwModeThresholdOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 19),
    _Rx4enumSwModeThresholdOne_Type()
)
rx4enumSwModeThresholdOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumSwModeThresholdOne.setStatus("optional")
_Rx4valueSwModeThresholdOne_Type = Integer32
_Rx4valueSwModeThresholdOne_Object = MibTableColumn
rx4valueSwModeThresholdOne = _Rx4valueSwModeThresholdOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 20),
    _Rx4valueSwModeThresholdOne_Type()
)
rx4valueSwModeThresholdOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueSwModeThresholdOne.setStatus("mandatory")


class _Rx4stateFlagSwModeThresholdOne_Type(Integer32):
    """Custom type rx4stateFlagSwModeThresholdOne based on Integer32"""
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


_Rx4stateFlagSwModeThresholdOne_Type.__name__ = "Integer32"
_Rx4stateFlagSwModeThresholdOne_Object = MibTableColumn
rx4stateFlagSwModeThresholdOne = _Rx4stateFlagSwModeThresholdOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 21),
    _Rx4stateFlagSwModeThresholdOne_Type()
)
rx4stateFlagSwModeThresholdOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagSwModeThresholdOne.setStatus("mandatory")


class _Rx4labelModeTwo_Type(DisplayString):
    """Custom type rx4labelModeTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelModeTwo_Type.__name__ = "DisplayString"
_Rx4labelModeTwo_Object = MibTableColumn
rx4labelModeTwo = _Rx4labelModeTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 22),
    _Rx4labelModeTwo_Type()
)
rx4labelModeTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelModeTwo.setStatus("optional")


class _Rx4enumModeTwo_Type(DisplayString):
    """Custom type rx4enumModeTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumModeTwo_Type.__name__ = "DisplayString"
_Rx4enumModeTwo_Object = MibTableColumn
rx4enumModeTwo = _Rx4enumModeTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 23),
    _Rx4enumModeTwo_Type()
)
rx4enumModeTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumModeTwo.setStatus("optional")


class _Rx4valueModeTwo_Type(Integer32):
    """Custom type rx4valueModeTwo based on Integer32"""
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


_Rx4valueModeTwo_Type.__name__ = "Integer32"
_Rx4valueModeTwo_Object = MibTableColumn
rx4valueModeTwo = _Rx4valueModeTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 24),
    _Rx4valueModeTwo_Type()
)
rx4valueModeTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueModeTwo.setStatus("mandatory")


class _Rx4stateFlagModeTwo_Type(Integer32):
    """Custom type rx4stateFlagModeTwo based on Integer32"""
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


_Rx4stateFlagModeTwo_Type.__name__ = "Integer32"
_Rx4stateFlagModeTwo_Object = MibTableColumn
rx4stateFlagModeTwo = _Rx4stateFlagModeTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 25),
    _Rx4stateFlagModeTwo_Type()
)
rx4stateFlagModeTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagModeTwo.setStatus("mandatory")


class _Rx4labelWavelengthTwo_Type(DisplayString):
    """Custom type rx4labelWavelengthTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelWavelengthTwo_Type.__name__ = "DisplayString"
_Rx4labelWavelengthTwo_Object = MibTableColumn
rx4labelWavelengthTwo = _Rx4labelWavelengthTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 26),
    _Rx4labelWavelengthTwo_Type()
)
rx4labelWavelengthTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelWavelengthTwo.setStatus("optional")


class _Rx4enumWavelengthTwo_Type(DisplayString):
    """Custom type rx4enumWavelengthTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumWavelengthTwo_Type.__name__ = "DisplayString"
_Rx4enumWavelengthTwo_Object = MibTableColumn
rx4enumWavelengthTwo = _Rx4enumWavelengthTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 27),
    _Rx4enumWavelengthTwo_Type()
)
rx4enumWavelengthTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumWavelengthTwo.setStatus("optional")


class _Rx4valueWavelengthTwo_Type(Integer32):
    """Custom type rx4valueWavelengthTwo based on Integer32"""
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


_Rx4valueWavelengthTwo_Type.__name__ = "Integer32"
_Rx4valueWavelengthTwo_Object = MibTableColumn
rx4valueWavelengthTwo = _Rx4valueWavelengthTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 28),
    _Rx4valueWavelengthTwo_Type()
)
rx4valueWavelengthTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueWavelengthTwo.setStatus("mandatory")


class _Rx4stateFlagWavelengthTwo_Type(Integer32):
    """Custom type rx4stateFlagWavelengthTwo based on Integer32"""
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


_Rx4stateFlagWavelengthTwo_Type.__name__ = "Integer32"
_Rx4stateFlagWavelengthTwo_Object = MibTableColumn
rx4stateFlagWavelengthTwo = _Rx4stateFlagWavelengthTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 29),
    _Rx4stateFlagWavelengthTwo_Type()
)
rx4stateFlagWavelengthTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagWavelengthTwo.setStatus("mandatory")


class _Rx4labelAttnSettingTwo_Type(DisplayString):
    """Custom type rx4labelAttnSettingTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelAttnSettingTwo_Type.__name__ = "DisplayString"
_Rx4labelAttnSettingTwo_Object = MibTableColumn
rx4labelAttnSettingTwo = _Rx4labelAttnSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 30),
    _Rx4labelAttnSettingTwo_Type()
)
rx4labelAttnSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelAttnSettingTwo.setStatus("optional")


class _Rx4enumAttnSettingTwo_Type(DisplayString):
    """Custom type rx4enumAttnSettingTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumAttnSettingTwo_Type.__name__ = "DisplayString"
_Rx4enumAttnSettingTwo_Object = MibTableColumn
rx4enumAttnSettingTwo = _Rx4enumAttnSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 31),
    _Rx4enumAttnSettingTwo_Type()
)
rx4enumAttnSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumAttnSettingTwo.setStatus("optional")
_Rx4valueAttnSettingTwo_Type = Integer32
_Rx4valueAttnSettingTwo_Object = MibTableColumn
rx4valueAttnSettingTwo = _Rx4valueAttnSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 32),
    _Rx4valueAttnSettingTwo_Type()
)
rx4valueAttnSettingTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueAttnSettingTwo.setStatus("mandatory")


class _Rx4stateFlagAttnSettingTwo_Type(Integer32):
    """Custom type rx4stateFlagAttnSettingTwo based on Integer32"""
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


_Rx4stateFlagAttnSettingTwo_Type.__name__ = "Integer32"
_Rx4stateFlagAttnSettingTwo_Object = MibTableColumn
rx4stateFlagAttnSettingTwo = _Rx4stateFlagAttnSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 33),
    _Rx4stateFlagAttnSettingTwo_Type()
)
rx4stateFlagAttnSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagAttnSettingTwo.setStatus("mandatory")


class _Rx4labelSwModeSettingTwo_Type(DisplayString):
    """Custom type rx4labelSwModeSettingTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelSwModeSettingTwo_Type.__name__ = "DisplayString"
_Rx4labelSwModeSettingTwo_Object = MibTableColumn
rx4labelSwModeSettingTwo = _Rx4labelSwModeSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 34),
    _Rx4labelSwModeSettingTwo_Type()
)
rx4labelSwModeSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelSwModeSettingTwo.setStatus("optional")


class _Rx4enumSwModeSettingTwo_Type(DisplayString):
    """Custom type rx4enumSwModeSettingTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumSwModeSettingTwo_Type.__name__ = "DisplayString"
_Rx4enumSwModeSettingTwo_Object = MibTableColumn
rx4enumSwModeSettingTwo = _Rx4enumSwModeSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 35),
    _Rx4enumSwModeSettingTwo_Type()
)
rx4enumSwModeSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumSwModeSettingTwo.setStatus("optional")


class _Rx4valueSwModeSettingTwo_Type(Integer32):
    """Custom type rx4valueSwModeSettingTwo based on Integer32"""
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


_Rx4valueSwModeSettingTwo_Type.__name__ = "Integer32"
_Rx4valueSwModeSettingTwo_Object = MibTableColumn
rx4valueSwModeSettingTwo = _Rx4valueSwModeSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 36),
    _Rx4valueSwModeSettingTwo_Type()
)
rx4valueSwModeSettingTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueSwModeSettingTwo.setStatus("mandatory")


class _Rx4stateFlagSwModeSettingTwo_Type(Integer32):
    """Custom type rx4stateFlagSwModeSettingTwo based on Integer32"""
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


_Rx4stateFlagSwModeSettingTwo_Type.__name__ = "Integer32"
_Rx4stateFlagSwModeSettingTwo_Object = MibTableColumn
rx4stateFlagSwModeSettingTwo = _Rx4stateFlagSwModeSettingTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 37),
    _Rx4stateFlagSwModeSettingTwo_Type()
)
rx4stateFlagSwModeSettingTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagSwModeSettingTwo.setStatus("mandatory")


class _Rx4labelSwModeThresholdTwo_Type(DisplayString):
    """Custom type rx4labelSwModeThresholdTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelSwModeThresholdTwo_Type.__name__ = "DisplayString"
_Rx4labelSwModeThresholdTwo_Object = MibTableColumn
rx4labelSwModeThresholdTwo = _Rx4labelSwModeThresholdTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 38),
    _Rx4labelSwModeThresholdTwo_Type()
)
rx4labelSwModeThresholdTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelSwModeThresholdTwo.setStatus("optional")


class _Rx4enumSwModeThresholdTwo_Type(DisplayString):
    """Custom type rx4enumSwModeThresholdTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumSwModeThresholdTwo_Type.__name__ = "DisplayString"
_Rx4enumSwModeThresholdTwo_Object = MibTableColumn
rx4enumSwModeThresholdTwo = _Rx4enumSwModeThresholdTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 39),
    _Rx4enumSwModeThresholdTwo_Type()
)
rx4enumSwModeThresholdTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumSwModeThresholdTwo.setStatus("optional")
_Rx4valueSwModeThresholdTwo_Type = Integer32
_Rx4valueSwModeThresholdTwo_Object = MibTableColumn
rx4valueSwModeThresholdTwo = _Rx4valueSwModeThresholdTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 40),
    _Rx4valueSwModeThresholdTwo_Type()
)
rx4valueSwModeThresholdTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueSwModeThresholdTwo.setStatus("mandatory")


class _Rx4stateFlagSwModeThresholdTwo_Type(Integer32):
    """Custom type rx4stateFlagSwModeThresholdTwo based on Integer32"""
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


_Rx4stateFlagSwModeThresholdTwo_Type.__name__ = "Integer32"
_Rx4stateFlagSwModeThresholdTwo_Object = MibTableColumn
rx4stateFlagSwModeThresholdTwo = _Rx4stateFlagSwModeThresholdTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 41),
    _Rx4stateFlagSwModeThresholdTwo_Type()
)
rx4stateFlagSwModeThresholdTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagSwModeThresholdTwo.setStatus("mandatory")


class _Rx4labelModeThree_Type(DisplayString):
    """Custom type rx4labelModeThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelModeThree_Type.__name__ = "DisplayString"
_Rx4labelModeThree_Object = MibTableColumn
rx4labelModeThree = _Rx4labelModeThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 42),
    _Rx4labelModeThree_Type()
)
rx4labelModeThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelModeThree.setStatus("optional")


class _Rx4enumModeThree_Type(DisplayString):
    """Custom type rx4enumModeThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumModeThree_Type.__name__ = "DisplayString"
_Rx4enumModeThree_Object = MibTableColumn
rx4enumModeThree = _Rx4enumModeThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 43),
    _Rx4enumModeThree_Type()
)
rx4enumModeThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumModeThree.setStatus("optional")


class _Rx4valueModeThree_Type(Integer32):
    """Custom type rx4valueModeThree based on Integer32"""
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


_Rx4valueModeThree_Type.__name__ = "Integer32"
_Rx4valueModeThree_Object = MibTableColumn
rx4valueModeThree = _Rx4valueModeThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 44),
    _Rx4valueModeThree_Type()
)
rx4valueModeThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueModeThree.setStatus("mandatory")


class _Rx4stateFlagModeThree_Type(Integer32):
    """Custom type rx4stateFlagModeThree based on Integer32"""
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


_Rx4stateFlagModeThree_Type.__name__ = "Integer32"
_Rx4stateFlagModeThree_Object = MibTableColumn
rx4stateFlagModeThree = _Rx4stateFlagModeThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 45),
    _Rx4stateFlagModeThree_Type()
)
rx4stateFlagModeThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagModeThree.setStatus("mandatory")


class _Rx4labelWavelengthThree_Type(DisplayString):
    """Custom type rx4labelWavelengthThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelWavelengthThree_Type.__name__ = "DisplayString"
_Rx4labelWavelengthThree_Object = MibTableColumn
rx4labelWavelengthThree = _Rx4labelWavelengthThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 46),
    _Rx4labelWavelengthThree_Type()
)
rx4labelWavelengthThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelWavelengthThree.setStatus("optional")


class _Rx4enumWavelengthThree_Type(DisplayString):
    """Custom type rx4enumWavelengthThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumWavelengthThree_Type.__name__ = "DisplayString"
_Rx4enumWavelengthThree_Object = MibTableColumn
rx4enumWavelengthThree = _Rx4enumWavelengthThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 47),
    _Rx4enumWavelengthThree_Type()
)
rx4enumWavelengthThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumWavelengthThree.setStatus("optional")


class _Rx4valueWavelengthThree_Type(Integer32):
    """Custom type rx4valueWavelengthThree based on Integer32"""
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


_Rx4valueWavelengthThree_Type.__name__ = "Integer32"
_Rx4valueWavelengthThree_Object = MibTableColumn
rx4valueWavelengthThree = _Rx4valueWavelengthThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 48),
    _Rx4valueWavelengthThree_Type()
)
rx4valueWavelengthThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueWavelengthThree.setStatus("mandatory")


class _Rx4stateFlagWavelengthThree_Type(Integer32):
    """Custom type rx4stateFlagWavelengthThree based on Integer32"""
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


_Rx4stateFlagWavelengthThree_Type.__name__ = "Integer32"
_Rx4stateFlagWavelengthThree_Object = MibTableColumn
rx4stateFlagWavelengthThree = _Rx4stateFlagWavelengthThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 49),
    _Rx4stateFlagWavelengthThree_Type()
)
rx4stateFlagWavelengthThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagWavelengthThree.setStatus("mandatory")


class _Rx4labelAttnSettingThree_Type(DisplayString):
    """Custom type rx4labelAttnSettingThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelAttnSettingThree_Type.__name__ = "DisplayString"
_Rx4labelAttnSettingThree_Object = MibTableColumn
rx4labelAttnSettingThree = _Rx4labelAttnSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 50),
    _Rx4labelAttnSettingThree_Type()
)
rx4labelAttnSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelAttnSettingThree.setStatus("optional")


class _Rx4enumAttnSettingThree_Type(DisplayString):
    """Custom type rx4enumAttnSettingThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumAttnSettingThree_Type.__name__ = "DisplayString"
_Rx4enumAttnSettingThree_Object = MibTableColumn
rx4enumAttnSettingThree = _Rx4enumAttnSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 51),
    _Rx4enumAttnSettingThree_Type()
)
rx4enumAttnSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumAttnSettingThree.setStatus("optional")
_Rx4valueAttnSettingThree_Type = Integer32
_Rx4valueAttnSettingThree_Object = MibTableColumn
rx4valueAttnSettingThree = _Rx4valueAttnSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 52),
    _Rx4valueAttnSettingThree_Type()
)
rx4valueAttnSettingThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueAttnSettingThree.setStatus("mandatory")


class _Rx4stateFlagAttnSettingThree_Type(Integer32):
    """Custom type rx4stateFlagAttnSettingThree based on Integer32"""
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


_Rx4stateFlagAttnSettingThree_Type.__name__ = "Integer32"
_Rx4stateFlagAttnSettingThree_Object = MibTableColumn
rx4stateFlagAttnSettingThree = _Rx4stateFlagAttnSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 53),
    _Rx4stateFlagAttnSettingThree_Type()
)
rx4stateFlagAttnSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagAttnSettingThree.setStatus("mandatory")


class _Rx4labelSwModeSettingThree_Type(DisplayString):
    """Custom type rx4labelSwModeSettingThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelSwModeSettingThree_Type.__name__ = "DisplayString"
_Rx4labelSwModeSettingThree_Object = MibTableColumn
rx4labelSwModeSettingThree = _Rx4labelSwModeSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 54),
    _Rx4labelSwModeSettingThree_Type()
)
rx4labelSwModeSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelSwModeSettingThree.setStatus("optional")


class _Rx4enumSwModeSettingThree_Type(DisplayString):
    """Custom type rx4enumSwModeSettingThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumSwModeSettingThree_Type.__name__ = "DisplayString"
_Rx4enumSwModeSettingThree_Object = MibTableColumn
rx4enumSwModeSettingThree = _Rx4enumSwModeSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 55),
    _Rx4enumSwModeSettingThree_Type()
)
rx4enumSwModeSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumSwModeSettingThree.setStatus("optional")


class _Rx4valueSwModeSettingThree_Type(Integer32):
    """Custom type rx4valueSwModeSettingThree based on Integer32"""
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


_Rx4valueSwModeSettingThree_Type.__name__ = "Integer32"
_Rx4valueSwModeSettingThree_Object = MibTableColumn
rx4valueSwModeSettingThree = _Rx4valueSwModeSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 56),
    _Rx4valueSwModeSettingThree_Type()
)
rx4valueSwModeSettingThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueSwModeSettingThree.setStatus("mandatory")


class _Rx4stateFlagSwModeSettingThree_Type(Integer32):
    """Custom type rx4stateFlagSwModeSettingThree based on Integer32"""
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


_Rx4stateFlagSwModeSettingThree_Type.__name__ = "Integer32"
_Rx4stateFlagSwModeSettingThree_Object = MibTableColumn
rx4stateFlagSwModeSettingThree = _Rx4stateFlagSwModeSettingThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 57),
    _Rx4stateFlagSwModeSettingThree_Type()
)
rx4stateFlagSwModeSettingThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagSwModeSettingThree.setStatus("mandatory")


class _Rx4labelSwModeThresholdThree_Type(DisplayString):
    """Custom type rx4labelSwModeThresholdThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelSwModeThresholdThree_Type.__name__ = "DisplayString"
_Rx4labelSwModeThresholdThree_Object = MibTableColumn
rx4labelSwModeThresholdThree = _Rx4labelSwModeThresholdThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 58),
    _Rx4labelSwModeThresholdThree_Type()
)
rx4labelSwModeThresholdThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelSwModeThresholdThree.setStatus("optional")


class _Rx4enumSwModeThresholdThree_Type(DisplayString):
    """Custom type rx4enumSwModeThresholdThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumSwModeThresholdThree_Type.__name__ = "DisplayString"
_Rx4enumSwModeThresholdThree_Object = MibTableColumn
rx4enumSwModeThresholdThree = _Rx4enumSwModeThresholdThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 59),
    _Rx4enumSwModeThresholdThree_Type()
)
rx4enumSwModeThresholdThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumSwModeThresholdThree.setStatus("optional")
_Rx4valueSwModeThresholdThree_Type = Integer32
_Rx4valueSwModeThresholdThree_Object = MibTableColumn
rx4valueSwModeThresholdThree = _Rx4valueSwModeThresholdThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 60),
    _Rx4valueSwModeThresholdThree_Type()
)
rx4valueSwModeThresholdThree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueSwModeThresholdThree.setStatus("mandatory")


class _Rx4stateFlagSwModeThresholdThree_Type(Integer32):
    """Custom type rx4stateFlagSwModeThresholdThree based on Integer32"""
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


_Rx4stateFlagSwModeThresholdThree_Type.__name__ = "Integer32"
_Rx4stateFlagSwModeThresholdThree_Object = MibTableColumn
rx4stateFlagSwModeThresholdThree = _Rx4stateFlagSwModeThresholdThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 61),
    _Rx4stateFlagSwModeThresholdThree_Type()
)
rx4stateFlagSwModeThresholdThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagSwModeThresholdThree.setStatus("mandatory")


class _Rx4labelModeFour_Type(DisplayString):
    """Custom type rx4labelModeFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelModeFour_Type.__name__ = "DisplayString"
_Rx4labelModeFour_Object = MibTableColumn
rx4labelModeFour = _Rx4labelModeFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 62),
    _Rx4labelModeFour_Type()
)
rx4labelModeFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelModeFour.setStatus("optional")


class _Rx4enumModeFour_Type(DisplayString):
    """Custom type rx4enumModeFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumModeFour_Type.__name__ = "DisplayString"
_Rx4enumModeFour_Object = MibTableColumn
rx4enumModeFour = _Rx4enumModeFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 63),
    _Rx4enumModeFour_Type()
)
rx4enumModeFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumModeFour.setStatus("optional")


class _Rx4valueModeFour_Type(Integer32):
    """Custom type rx4valueModeFour based on Integer32"""
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


_Rx4valueModeFour_Type.__name__ = "Integer32"
_Rx4valueModeFour_Object = MibTableColumn
rx4valueModeFour = _Rx4valueModeFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 64),
    _Rx4valueModeFour_Type()
)
rx4valueModeFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueModeFour.setStatus("mandatory")


class _Rx4stateFlagModeFour_Type(Integer32):
    """Custom type rx4stateFlagModeFour based on Integer32"""
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


_Rx4stateFlagModeFour_Type.__name__ = "Integer32"
_Rx4stateFlagModeFour_Object = MibTableColumn
rx4stateFlagModeFour = _Rx4stateFlagModeFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 65),
    _Rx4stateFlagModeFour_Type()
)
rx4stateFlagModeFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagModeFour.setStatus("mandatory")


class _Rx4labelWavelengthFour_Type(DisplayString):
    """Custom type rx4labelWavelengthFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelWavelengthFour_Type.__name__ = "DisplayString"
_Rx4labelWavelengthFour_Object = MibTableColumn
rx4labelWavelengthFour = _Rx4labelWavelengthFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 66),
    _Rx4labelWavelengthFour_Type()
)
rx4labelWavelengthFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelWavelengthFour.setStatus("optional")


class _Rx4enumWavelengthFour_Type(DisplayString):
    """Custom type rx4enumWavelengthFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumWavelengthFour_Type.__name__ = "DisplayString"
_Rx4enumWavelengthFour_Object = MibTableColumn
rx4enumWavelengthFour = _Rx4enumWavelengthFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 67),
    _Rx4enumWavelengthFour_Type()
)
rx4enumWavelengthFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumWavelengthFour.setStatus("optional")


class _Rx4valueWavelengthFour_Type(Integer32):
    """Custom type rx4valueWavelengthFour based on Integer32"""
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


_Rx4valueWavelengthFour_Type.__name__ = "Integer32"
_Rx4valueWavelengthFour_Object = MibTableColumn
rx4valueWavelengthFour = _Rx4valueWavelengthFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 68),
    _Rx4valueWavelengthFour_Type()
)
rx4valueWavelengthFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueWavelengthFour.setStatus("mandatory")


class _Rx4stateFlagWavelengthFour_Type(Integer32):
    """Custom type rx4stateFlagWavelengthFour based on Integer32"""
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


_Rx4stateFlagWavelengthFour_Type.__name__ = "Integer32"
_Rx4stateFlagWavelengthFour_Object = MibTableColumn
rx4stateFlagWavelengthFour = _Rx4stateFlagWavelengthFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 69),
    _Rx4stateFlagWavelengthFour_Type()
)
rx4stateFlagWavelengthFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagWavelengthFour.setStatus("mandatory")


class _Rx4labelAttnSettingFour_Type(DisplayString):
    """Custom type rx4labelAttnSettingFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelAttnSettingFour_Type.__name__ = "DisplayString"
_Rx4labelAttnSettingFour_Object = MibTableColumn
rx4labelAttnSettingFour = _Rx4labelAttnSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 70),
    _Rx4labelAttnSettingFour_Type()
)
rx4labelAttnSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelAttnSettingFour.setStatus("optional")


class _Rx4enumAttnSettingFour_Type(DisplayString):
    """Custom type rx4enumAttnSettingFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumAttnSettingFour_Type.__name__ = "DisplayString"
_Rx4enumAttnSettingFour_Object = MibTableColumn
rx4enumAttnSettingFour = _Rx4enumAttnSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 71),
    _Rx4enumAttnSettingFour_Type()
)
rx4enumAttnSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumAttnSettingFour.setStatus("optional")
_Rx4valueAttnSettingFour_Type = Integer32
_Rx4valueAttnSettingFour_Object = MibTableColumn
rx4valueAttnSettingFour = _Rx4valueAttnSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 72),
    _Rx4valueAttnSettingFour_Type()
)
rx4valueAttnSettingFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueAttnSettingFour.setStatus("mandatory")


class _Rx4stateFlagAttnSettingFour_Type(Integer32):
    """Custom type rx4stateFlagAttnSettingFour based on Integer32"""
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


_Rx4stateFlagAttnSettingFour_Type.__name__ = "Integer32"
_Rx4stateFlagAttnSettingFour_Object = MibTableColumn
rx4stateFlagAttnSettingFour = _Rx4stateFlagAttnSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 73),
    _Rx4stateFlagAttnSettingFour_Type()
)
rx4stateFlagAttnSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagAttnSettingFour.setStatus("mandatory")


class _Rx4labelSwModeSettingFour_Type(DisplayString):
    """Custom type rx4labelSwModeSettingFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelSwModeSettingFour_Type.__name__ = "DisplayString"
_Rx4labelSwModeSettingFour_Object = MibTableColumn
rx4labelSwModeSettingFour = _Rx4labelSwModeSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 74),
    _Rx4labelSwModeSettingFour_Type()
)
rx4labelSwModeSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelSwModeSettingFour.setStatus("optional")


class _Rx4enumSwModeSettingFour_Type(DisplayString):
    """Custom type rx4enumSwModeSettingFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumSwModeSettingFour_Type.__name__ = "DisplayString"
_Rx4enumSwModeSettingFour_Object = MibTableColumn
rx4enumSwModeSettingFour = _Rx4enumSwModeSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 75),
    _Rx4enumSwModeSettingFour_Type()
)
rx4enumSwModeSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumSwModeSettingFour.setStatus("optional")


class _Rx4valueSwModeSettingFour_Type(Integer32):
    """Custom type rx4valueSwModeSettingFour based on Integer32"""
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


_Rx4valueSwModeSettingFour_Type.__name__ = "Integer32"
_Rx4valueSwModeSettingFour_Object = MibTableColumn
rx4valueSwModeSettingFour = _Rx4valueSwModeSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 76),
    _Rx4valueSwModeSettingFour_Type()
)
rx4valueSwModeSettingFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueSwModeSettingFour.setStatus("mandatory")


class _Rx4stateFlagSwModeSettingFour_Type(Integer32):
    """Custom type rx4stateFlagSwModeSettingFour based on Integer32"""
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


_Rx4stateFlagSwModeSettingFour_Type.__name__ = "Integer32"
_Rx4stateFlagSwModeSettingFour_Object = MibTableColumn
rx4stateFlagSwModeSettingFour = _Rx4stateFlagSwModeSettingFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 77),
    _Rx4stateFlagSwModeSettingFour_Type()
)
rx4stateFlagSwModeSettingFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagSwModeSettingFour.setStatus("mandatory")


class _Rx4labelSwModeThresholdFour_Type(DisplayString):
    """Custom type rx4labelSwModeThresholdFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelSwModeThresholdFour_Type.__name__ = "DisplayString"
_Rx4labelSwModeThresholdFour_Object = MibTableColumn
rx4labelSwModeThresholdFour = _Rx4labelSwModeThresholdFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 78),
    _Rx4labelSwModeThresholdFour_Type()
)
rx4labelSwModeThresholdFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelSwModeThresholdFour.setStatus("optional")


class _Rx4enumSwModeThresholdFour_Type(DisplayString):
    """Custom type rx4enumSwModeThresholdFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumSwModeThresholdFour_Type.__name__ = "DisplayString"
_Rx4enumSwModeThresholdFour_Object = MibTableColumn
rx4enumSwModeThresholdFour = _Rx4enumSwModeThresholdFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 79),
    _Rx4enumSwModeThresholdFour_Type()
)
rx4enumSwModeThresholdFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumSwModeThresholdFour.setStatus("optional")
_Rx4valueSwModeThresholdFour_Type = Integer32
_Rx4valueSwModeThresholdFour_Object = MibTableColumn
rx4valueSwModeThresholdFour = _Rx4valueSwModeThresholdFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 80),
    _Rx4valueSwModeThresholdFour_Type()
)
rx4valueSwModeThresholdFour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueSwModeThresholdFour.setStatus("mandatory")


class _Rx4stateFlagSwModeThresholdFour_Type(Integer32):
    """Custom type rx4stateFlagSwModeThresholdFour based on Integer32"""
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


_Rx4stateFlagSwModeThresholdFour_Type.__name__ = "Integer32"
_Rx4stateFlagSwModeThresholdFour_Object = MibTableColumn
rx4stateFlagSwModeThresholdFour = _Rx4stateFlagSwModeThresholdFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 81),
    _Rx4stateFlagSwModeThresholdFour_Type()
)
rx4stateFlagSwModeThresholdFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagSwModeThresholdFour.setStatus("mandatory")


class _Rx4labelModuleConfig_Type(DisplayString):
    """Custom type rx4labelModuleConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelModuleConfig_Type.__name__ = "DisplayString"
_Rx4labelModuleConfig_Object = MibTableColumn
rx4labelModuleConfig = _Rx4labelModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 82),
    _Rx4labelModuleConfig_Type()
)
rx4labelModuleConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelModuleConfig.setStatus("optional")


class _Rx4enumModuleConfig_Type(DisplayString):
    """Custom type rx4enumModuleConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumModuleConfig_Type.__name__ = "DisplayString"
_Rx4enumModuleConfig_Object = MibTableColumn
rx4enumModuleConfig = _Rx4enumModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 83),
    _Rx4enumModuleConfig_Type()
)
rx4enumModuleConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumModuleConfig.setStatus("optional")


class _Rx4valueModuleConfig_Type(Integer32):
    """Custom type rx4valueModuleConfig based on Integer32"""
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


_Rx4valueModuleConfig_Type.__name__ = "Integer32"
_Rx4valueModuleConfig_Object = MibTableColumn
rx4valueModuleConfig = _Rx4valueModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 84),
    _Rx4valueModuleConfig_Type()
)
rx4valueModuleConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueModuleConfig.setStatus("mandatory")


class _Rx4stateFlagModuleConfig_Type(Integer32):
    """Custom type rx4stateFlagModuleConfig based on Integer32"""
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


_Rx4stateFlagModuleConfig_Type.__name__ = "Integer32"
_Rx4stateFlagModuleConfig_Object = MibTableColumn
rx4stateFlagModuleConfig = _Rx4stateFlagModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 85),
    _Rx4stateFlagModuleConfig_Type()
)
rx4stateFlagModuleConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagModuleConfig.setStatus("mandatory")


class _Rx4labelRevertTime_Type(DisplayString):
    """Custom type rx4labelRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelRevertTime_Type.__name__ = "DisplayString"
_Rx4labelRevertTime_Object = MibTableColumn
rx4labelRevertTime = _Rx4labelRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 86),
    _Rx4labelRevertTime_Type()
)
rx4labelRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelRevertTime.setStatus("optional")


class _Rx4enumRevertTime_Type(DisplayString):
    """Custom type rx4enumRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumRevertTime_Type.__name__ = "DisplayString"
_Rx4enumRevertTime_Object = MibTableColumn
rx4enumRevertTime = _Rx4enumRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 87),
    _Rx4enumRevertTime_Type()
)
rx4enumRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumRevertTime.setStatus("optional")


class _Rx4valueRevertTime_Type(Integer32):
    """Custom type rx4valueRevertTime based on Integer32"""
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


_Rx4valueRevertTime_Type.__name__ = "Integer32"
_Rx4valueRevertTime_Object = MibTableColumn
rx4valueRevertTime = _Rx4valueRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 88),
    _Rx4valueRevertTime_Type()
)
rx4valueRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueRevertTime.setStatus("mandatory")


class _Rx4stateFlagRevertTime_Type(Integer32):
    """Custom type rx4stateFlagRevertTime based on Integer32"""
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


_Rx4stateFlagRevertTime_Type.__name__ = "Integer32"
_Rx4stateFlagRevertTime_Object = MibTableColumn
rx4stateFlagRevertTime = _Rx4stateFlagRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 89),
    _Rx4stateFlagRevertTime_Type()
)
rx4stateFlagRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagRevertTime.setStatus("mandatory")


class _Rx4labelTestPointSelect_Type(DisplayString):
    """Custom type rx4labelTestPointSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelTestPointSelect_Type.__name__ = "DisplayString"
_Rx4labelTestPointSelect_Object = MibTableColumn
rx4labelTestPointSelect = _Rx4labelTestPointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 90),
    _Rx4labelTestPointSelect_Type()
)
rx4labelTestPointSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelTestPointSelect.setStatus("optional")


class _Rx4enumTestPointSelect_Type(DisplayString):
    """Custom type rx4enumTestPointSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumTestPointSelect_Type.__name__ = "DisplayString"
_Rx4enumTestPointSelect_Object = MibTableColumn
rx4enumTestPointSelect = _Rx4enumTestPointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 91),
    _Rx4enumTestPointSelect_Type()
)
rx4enumTestPointSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumTestPointSelect.setStatus("optional")


class _Rx4valueTestPointSelect_Type(Integer32):
    """Custom type rx4valueTestPointSelect based on Integer32"""
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


_Rx4valueTestPointSelect_Type.__name__ = "Integer32"
_Rx4valueTestPointSelect_Object = MibTableColumn
rx4valueTestPointSelect = _Rx4valueTestPointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 92),
    _Rx4valueTestPointSelect_Type()
)
rx4valueTestPointSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueTestPointSelect.setStatus("mandatory")


class _Rx4stateFlagTestPointSelect_Type(Integer32):
    """Custom type rx4stateFlagTestPointSelect based on Integer32"""
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


_Rx4stateFlagTestPointSelect_Type.__name__ = "Integer32"
_Rx4stateFlagTestPointSelect_Object = MibTableColumn
rx4stateFlagTestPointSelect = _Rx4stateFlagTestPointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 93),
    _Rx4stateFlagTestPointSelect_Type()
)
rx4stateFlagTestPointSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagTestPointSelect.setStatus("mandatory")


class _Rx4labelFactoryDefault_Type(DisplayString):
    """Custom type rx4labelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelFactoryDefault_Type.__name__ = "DisplayString"
_Rx4labelFactoryDefault_Object = MibTableColumn
rx4labelFactoryDefault = _Rx4labelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 94),
    _Rx4labelFactoryDefault_Type()
)
rx4labelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelFactoryDefault.setStatus("optional")


class _Rx4enumFactoryDefault_Type(DisplayString):
    """Custom type rx4enumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4enumFactoryDefault_Type.__name__ = "DisplayString"
_Rx4enumFactoryDefault_Object = MibTableColumn
rx4enumFactoryDefault = _Rx4enumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 95),
    _Rx4enumFactoryDefault_Type()
)
rx4enumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4enumFactoryDefault.setStatus("optional")


class _Rx4valueFactoryDefault_Type(Integer32):
    """Custom type rx4valueFactoryDefault based on Integer32"""
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


_Rx4valueFactoryDefault_Type.__name__ = "Integer32"
_Rx4valueFactoryDefault_Object = MibTableColumn
rx4valueFactoryDefault = _Rx4valueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 96),
    _Rx4valueFactoryDefault_Type()
)
rx4valueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rx4valueFactoryDefault.setStatus("mandatory")


class _Rx4stateFlagFactoryDefault_Type(Integer32):
    """Custom type rx4stateFlagFactoryDefault based on Integer32"""
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


_Rx4stateFlagFactoryDefault_Type.__name__ = "Integer32"
_Rx4stateFlagFactoryDefault_Object = MibTableColumn
rx4stateFlagFactoryDefault = _Rx4stateFlagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 3, 2, 97),
    _Rx4stateFlagFactoryDefault_Type()
)
rx4stateFlagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateFlagFactoryDefault.setStatus("mandatory")
_Gx2Rx200BX4StatusTable_Object = MibTable
gx2Rx200BX4StatusTable = _Gx2Rx200BX4StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4)
)
if mibBuilder.loadTexts:
    gx2Rx200BX4StatusTable.setStatus("mandatory")
_Gx2Rx200BX4StatusEntry_Object = MibTableRow
gx2Rx200BX4StatusEntry = _Gx2Rx200BX4StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3)
)
gx2Rx200BX4StatusEntry.setIndexNames(
    (0, "OMNI-gx2Rx200BX4-MIB", "gx2Rx200BX4StatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx200BX4StatusEntry.setStatus("mandatory")


class _Gx2Rx200BX4StatusTableIndex_Type(Integer32):
    """Custom type gx2Rx200BX4StatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx200BX4StatusTableIndex_Type.__name__ = "Integer32"
_Gx2Rx200BX4StatusTableIndex_Object = MibTableColumn
gx2Rx200BX4StatusTableIndex = _Gx2Rx200BX4StatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 1),
    _Gx2Rx200BX4StatusTableIndex_Type()
)
gx2Rx200BX4StatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx200BX4StatusTableIndex.setStatus("mandatory")


class _Rx4labelBoot_Type(DisplayString):
    """Custom type rx4labelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelBoot_Type.__name__ = "DisplayString"
_Rx4labelBoot_Object = MibTableColumn
rx4labelBoot = _Rx4labelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 2),
    _Rx4labelBoot_Type()
)
rx4labelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelBoot.setStatus("optional")


class _Rx4valueBoot_Type(Integer32):
    """Custom type rx4valueBoot based on Integer32"""
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


_Rx4valueBoot_Type.__name__ = "Integer32"
_Rx4valueBoot_Object = MibTableColumn
rx4valueBoot = _Rx4valueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 3),
    _Rx4valueBoot_Type()
)
rx4valueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueBoot.setStatus("mandatory")


class _Rx4stateflagBoot_Type(Integer32):
    """Custom type rx4stateflagBoot based on Integer32"""
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


_Rx4stateflagBoot_Type.__name__ = "Integer32"
_Rx4stateflagBoot_Object = MibTableColumn
rx4stateflagBoot = _Rx4stateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 4),
    _Rx4stateflagBoot_Type()
)
rx4stateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagBoot.setStatus("mandatory")


class _Rx4labelFlash_Type(DisplayString):
    """Custom type rx4labelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelFlash_Type.__name__ = "DisplayString"
_Rx4labelFlash_Object = MibTableColumn
rx4labelFlash = _Rx4labelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 5),
    _Rx4labelFlash_Type()
)
rx4labelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelFlash.setStatus("optional")


class _Rx4valueFlash_Type(Integer32):
    """Custom type rx4valueFlash based on Integer32"""
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


_Rx4valueFlash_Type.__name__ = "Integer32"
_Rx4valueFlash_Object = MibTableColumn
rx4valueFlash = _Rx4valueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 6),
    _Rx4valueFlash_Type()
)
rx4valueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueFlash.setStatus("mandatory")


class _Rx4stateflagFlash_Type(Integer32):
    """Custom type rx4stateflagFlash based on Integer32"""
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


_Rx4stateflagFlash_Type.__name__ = "Integer32"
_Rx4stateflagFlash_Object = MibTableColumn
rx4stateflagFlash = _Rx4stateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 7),
    _Rx4stateflagFlash_Type()
)
rx4stateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagFlash.setStatus("mandatory")


class _Rx4labelFactoryDataCRC_Type(DisplayString):
    """Custom type rx4labelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelFactoryDataCRC_Type.__name__ = "DisplayString"
_Rx4labelFactoryDataCRC_Object = MibTableColumn
rx4labelFactoryDataCRC = _Rx4labelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 8),
    _Rx4labelFactoryDataCRC_Type()
)
rx4labelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelFactoryDataCRC.setStatus("optional")


class _Rx4valueFactoryDataCRC_Type(Integer32):
    """Custom type rx4valueFactoryDataCRC based on Integer32"""
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


_Rx4valueFactoryDataCRC_Type.__name__ = "Integer32"
_Rx4valueFactoryDataCRC_Object = MibTableColumn
rx4valueFactoryDataCRC = _Rx4valueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 9),
    _Rx4valueFactoryDataCRC_Type()
)
rx4valueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueFactoryDataCRC.setStatus("mandatory")


class _Rx4stateflagFactoryDataCRC_Type(Integer32):
    """Custom type rx4stateflagFactoryDataCRC based on Integer32"""
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


_Rx4stateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Rx4stateflagFactoryDataCRC_Object = MibTableColumn
rx4stateflagFactoryDataCRC = _Rx4stateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 10),
    _Rx4stateflagFactoryDataCRC_Type()
)
rx4stateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagFactoryDataCRC.setStatus("mandatory")


class _Rx4labelAlarmDataCRC_Type(DisplayString):
    """Custom type rx4labelAlarmDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelAlarmDataCRC_Type.__name__ = "DisplayString"
_Rx4labelAlarmDataCRC_Object = MibTableColumn
rx4labelAlarmDataCRC = _Rx4labelAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 11),
    _Rx4labelAlarmDataCRC_Type()
)
rx4labelAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelAlarmDataCRC.setStatus("optional")


class _Rx4valueAlarmDataCRC_Type(Integer32):
    """Custom type rx4valueAlarmDataCRC based on Integer32"""
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


_Rx4valueAlarmDataCRC_Type.__name__ = "Integer32"
_Rx4valueAlarmDataCRC_Object = MibTableColumn
rx4valueAlarmDataCRC = _Rx4valueAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 12),
    _Rx4valueAlarmDataCRC_Type()
)
rx4valueAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueAlarmDataCRC.setStatus("mandatory")


class _Rx4stateflagAlarmDataCRC_Type(Integer32):
    """Custom type rx4stateflagAlarmDataCRC based on Integer32"""
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


_Rx4stateflagAlarmDataCRC_Type.__name__ = "Integer32"
_Rx4stateflagAlarmDataCRC_Object = MibTableColumn
rx4stateflagAlarmDataCRC = _Rx4stateflagAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 13),
    _Rx4stateflagAlarmDataCRC_Type()
)
rx4stateflagAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagAlarmDataCRC.setStatus("mandatory")


class _Rx4labelCalibrationDataCRC_Type(DisplayString):
    """Custom type rx4labelCalibrationDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelCalibrationDataCRC_Type.__name__ = "DisplayString"
_Rx4labelCalibrationDataCRC_Object = MibTableColumn
rx4labelCalibrationDataCRC = _Rx4labelCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 14),
    _Rx4labelCalibrationDataCRC_Type()
)
rx4labelCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelCalibrationDataCRC.setStatus("optional")


class _Rx4valueCalibrationDataCRC_Type(Integer32):
    """Custom type rx4valueCalibrationDataCRC based on Integer32"""
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


_Rx4valueCalibrationDataCRC_Type.__name__ = "Integer32"
_Rx4valueCalibrationDataCRC_Object = MibTableColumn
rx4valueCalibrationDataCRC = _Rx4valueCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 15),
    _Rx4valueCalibrationDataCRC_Type()
)
rx4valueCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueCalibrationDataCRC.setStatus("mandatory")


class _Rx4stateflagCalibrationDataCRC_Type(Integer32):
    """Custom type rx4stateflagCalibrationDataCRC based on Integer32"""
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


_Rx4stateflagCalibrationDataCRC_Type.__name__ = "Integer32"
_Rx4stateflagCalibrationDataCRC_Object = MibTableColumn
rx4stateflagCalibrationDataCRC = _Rx4stateflagCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 16),
    _Rx4stateflagCalibrationDataCRC_Type()
)
rx4stateflagCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagCalibrationDataCRC.setStatus("mandatory")


class _Rx4labelHW_Type(DisplayString):
    """Custom type rx4labelHW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelHW_Type.__name__ = "DisplayString"
_Rx4labelHW_Object = MibTableColumn
rx4labelHW = _Rx4labelHW_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 17),
    _Rx4labelHW_Type()
)
rx4labelHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelHW.setStatus("optional")


class _Rx4valueHW_Type(Integer32):
    """Custom type rx4valueHW based on Integer32"""
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


_Rx4valueHW_Type.__name__ = "Integer32"
_Rx4valueHW_Object = MibTableColumn
rx4valueHW = _Rx4valueHW_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 18),
    _Rx4valueHW_Type()
)
rx4valueHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueHW.setStatus("mandatory")


class _Rx4stateflagHW_Type(Integer32):
    """Custom type rx4stateflagHW based on Integer32"""
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


_Rx4stateflagHW_Type.__name__ = "Integer32"
_Rx4stateflagHW_Object = MibTableColumn
rx4stateflagHW = _Rx4stateflagHW_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 19),
    _Rx4stateflagHW_Type()
)
rx4stateflagHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagHW.setStatus("mandatory")


class _Rx4labelOptSigOne_Type(DisplayString):
    """Custom type rx4labelOptSigOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelOptSigOne_Type.__name__ = "DisplayString"
_Rx4labelOptSigOne_Object = MibTableColumn
rx4labelOptSigOne = _Rx4labelOptSigOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 20),
    _Rx4labelOptSigOne_Type()
)
rx4labelOptSigOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelOptSigOne.setStatus("optional")


class _Rx4valueOptSigOne_Type(Integer32):
    """Custom type rx4valueOptSigOne based on Integer32"""
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


_Rx4valueOptSigOne_Type.__name__ = "Integer32"
_Rx4valueOptSigOne_Object = MibTableColumn
rx4valueOptSigOne = _Rx4valueOptSigOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 21),
    _Rx4valueOptSigOne_Type()
)
rx4valueOptSigOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueOptSigOne.setStatus("mandatory")


class _Rx4stateflagOptSigOne_Type(Integer32):
    """Custom type rx4stateflagOptSigOne based on Integer32"""
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


_Rx4stateflagOptSigOne_Type.__name__ = "Integer32"
_Rx4stateflagOptSigOne_Object = MibTableColumn
rx4stateflagOptSigOne = _Rx4stateflagOptSigOne_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 22),
    _Rx4stateflagOptSigOne_Type()
)
rx4stateflagOptSigOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagOptSigOne.setStatus("mandatory")


class _Rx4labelOptSigTwo_Type(DisplayString):
    """Custom type rx4labelOptSigTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelOptSigTwo_Type.__name__ = "DisplayString"
_Rx4labelOptSigTwo_Object = MibTableColumn
rx4labelOptSigTwo = _Rx4labelOptSigTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 23),
    _Rx4labelOptSigTwo_Type()
)
rx4labelOptSigTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelOptSigTwo.setStatus("optional")


class _Rx4valueOptSigTwo_Type(Integer32):
    """Custom type rx4valueOptSigTwo based on Integer32"""
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


_Rx4valueOptSigTwo_Type.__name__ = "Integer32"
_Rx4valueOptSigTwo_Object = MibTableColumn
rx4valueOptSigTwo = _Rx4valueOptSigTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 24),
    _Rx4valueOptSigTwo_Type()
)
rx4valueOptSigTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueOptSigTwo.setStatus("mandatory")


class _Rx4stateflagOptSigTwo_Type(Integer32):
    """Custom type rx4stateflagOptSigTwo based on Integer32"""
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


_Rx4stateflagOptSigTwo_Type.__name__ = "Integer32"
_Rx4stateflagOptSigTwo_Object = MibTableColumn
rx4stateflagOptSigTwo = _Rx4stateflagOptSigTwo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 25),
    _Rx4stateflagOptSigTwo_Type()
)
rx4stateflagOptSigTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagOptSigTwo.setStatus("mandatory")


class _Rx4labelOptSigThree_Type(DisplayString):
    """Custom type rx4labelOptSigThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelOptSigThree_Type.__name__ = "DisplayString"
_Rx4labelOptSigThree_Object = MibTableColumn
rx4labelOptSigThree = _Rx4labelOptSigThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 26),
    _Rx4labelOptSigThree_Type()
)
rx4labelOptSigThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelOptSigThree.setStatus("optional")


class _Rx4valueOptSigThree_Type(Integer32):
    """Custom type rx4valueOptSigThree based on Integer32"""
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


_Rx4valueOptSigThree_Type.__name__ = "Integer32"
_Rx4valueOptSigThree_Object = MibTableColumn
rx4valueOptSigThree = _Rx4valueOptSigThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 27),
    _Rx4valueOptSigThree_Type()
)
rx4valueOptSigThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueOptSigThree.setStatus("mandatory")


class _Rx4stateflagOptSigThree_Type(Integer32):
    """Custom type rx4stateflagOptSigThree based on Integer32"""
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


_Rx4stateflagOptSigThree_Type.__name__ = "Integer32"
_Rx4stateflagOptSigThree_Object = MibTableColumn
rx4stateflagOptSigThree = _Rx4stateflagOptSigThree_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 28),
    _Rx4stateflagOptSigThree_Type()
)
rx4stateflagOptSigThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagOptSigThree.setStatus("mandatory")


class _Rx4labelOptSigFour_Type(DisplayString):
    """Custom type rx4labelOptSigFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelOptSigFour_Type.__name__ = "DisplayString"
_Rx4labelOptSigFour_Object = MibTableColumn
rx4labelOptSigFour = _Rx4labelOptSigFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 29),
    _Rx4labelOptSigFour_Type()
)
rx4labelOptSigFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelOptSigFour.setStatus("optional")


class _Rx4valueOptSigFour_Type(Integer32):
    """Custom type rx4valueOptSigFour based on Integer32"""
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


_Rx4valueOptSigFour_Type.__name__ = "Integer32"
_Rx4valueOptSigFour_Object = MibTableColumn
rx4valueOptSigFour = _Rx4valueOptSigFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 30),
    _Rx4valueOptSigFour_Type()
)
rx4valueOptSigFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueOptSigFour.setStatus("mandatory")


class _Rx4stateflagOptSigFour_Type(Integer32):
    """Custom type rx4stateflagOptSigFour based on Integer32"""
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


_Rx4stateflagOptSigFour_Type.__name__ = "Integer32"
_Rx4stateflagOptSigFour_Object = MibTableColumn
rx4stateflagOptSigFour = _Rx4stateflagOptSigFour_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 31),
    _Rx4stateflagOptSigFour_Type()
)
rx4stateflagOptSigFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagOptSigFour.setStatus("mandatory")


class _Rx4labelBackupCable_Type(DisplayString):
    """Custom type rx4labelBackupCable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4labelBackupCable_Type.__name__ = "DisplayString"
_Rx4labelBackupCable_Object = MibTableColumn
rx4labelBackupCable = _Rx4labelBackupCable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 32),
    _Rx4labelBackupCable_Type()
)
rx4labelBackupCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4labelBackupCable.setStatus("optional")


class _Rx4valueBackupCable_Type(Integer32):
    """Custom type rx4valueBackupCable based on Integer32"""
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


_Rx4valueBackupCable_Type.__name__ = "Integer32"
_Rx4valueBackupCable_Object = MibTableColumn
rx4valueBackupCable = _Rx4valueBackupCable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 33),
    _Rx4valueBackupCable_Type()
)
rx4valueBackupCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4valueBackupCable.setStatus("mandatory")


class _Rx4stateflagBackupCable_Type(Integer32):
    """Custom type rx4stateflagBackupCable based on Integer32"""
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


_Rx4stateflagBackupCable_Type.__name__ = "Integer32"
_Rx4stateflagBackupCable_Object = MibTableColumn
rx4stateflagBackupCable = _Rx4stateflagBackupCable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 4, 3, 34),
    _Rx4stateflagBackupCable_Type()
)
rx4stateflagBackupCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4stateflagBackupCable.setStatus("mandatory")
_Gx2Rx200BX4FactoryTable_Object = MibTable
gx2Rx200BX4FactoryTable = _Gx2Rx200BX4FactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5)
)
if mibBuilder.loadTexts:
    gx2Rx200BX4FactoryTable.setStatus("mandatory")
_Gx2Rx200BX4FactoryEntry_Object = MibTableRow
gx2Rx200BX4FactoryEntry = _Gx2Rx200BX4FactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4)
)
gx2Rx200BX4FactoryEntry.setIndexNames(
    (0, "OMNI-gx2Rx200BX4-MIB", "gx2Rx200BX4FactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rx200BX4FactoryEntry.setStatus("mandatory")


class _Gx2Rx200BX4FactoryTableIndex_Type(Integer32):
    """Custom type gx2Rx200BX4FactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Rx200BX4FactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Rx200BX4FactoryTableIndex_Object = MibTableColumn
gx2Rx200BX4FactoryTableIndex = _Gx2Rx200BX4FactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 1),
    _Gx2Rx200BX4FactoryTableIndex_Type()
)
gx2Rx200BX4FactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rx200BX4FactoryTableIndex.setStatus("mandatory")
_Rx4bootControlByte_Type = Integer32
_Rx4bootControlByte_Object = MibTableColumn
rx4bootControlByte = _Rx4bootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 2),
    _Rx4bootControlByte_Type()
)
rx4bootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4bootControlByte.setStatus("mandatory")
_Rx4bootStatusByte_Type = Integer32
_Rx4bootStatusByte_Object = MibTableColumn
rx4bootStatusByte = _Rx4bootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 3),
    _Rx4bootStatusByte_Type()
)
rx4bootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4bootStatusByte.setStatus("mandatory")
_Rx4bank0CRC_Type = Integer32
_Rx4bank0CRC_Object = MibTableColumn
rx4bank0CRC = _Rx4bank0CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 4),
    _Rx4bank0CRC_Type()
)
rx4bank0CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4bank0CRC.setStatus("mandatory")
_Rx4bank1CRC_Type = Integer32
_Rx4bank1CRC_Object = MibTableColumn
rx4bank1CRC = _Rx4bank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 5),
    _Rx4bank1CRC_Type()
)
rx4bank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4bank1CRC.setStatus("mandatory")
_Rx4prgEEPROMByte_Type = Integer32
_Rx4prgEEPROMByte_Object = MibTableColumn
rx4prgEEPROMByte = _Rx4prgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 6),
    _Rx4prgEEPROMByte_Type()
)
rx4prgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4prgEEPROMByte.setStatus("mandatory")
_Rx4factoryCRC_Type = Integer32
_Rx4factoryCRC_Object = MibTableColumn
rx4factoryCRC = _Rx4factoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 7),
    _Rx4factoryCRC_Type()
)
rx4factoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4factoryCRC.setStatus("mandatory")


class _Rx4calculateCRC_Type(Integer32):
    """Custom type rx4calculateCRC based on Integer32"""
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


_Rx4calculateCRC_Type.__name__ = "Integer32"
_Rx4calculateCRC_Object = MibTableColumn
rx4calculateCRC = _Rx4calculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 8),
    _Rx4calculateCRC_Type()
)
rx4calculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4calculateCRC.setStatus("mandatory")
_Rx4hourMeter_Type = Integer32
_Rx4hourMeter_Object = MibTableColumn
rx4hourMeter = _Rx4hourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 9),
    _Rx4hourMeter_Type()
)
rx4hourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4hourMeter.setStatus("mandatory")
_Rx4flashPrgCntA_Type = Integer32
_Rx4flashPrgCntA_Object = MibTableColumn
rx4flashPrgCntA = _Rx4flashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 10),
    _Rx4flashPrgCntA_Type()
)
rx4flashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4flashPrgCntA.setStatus("mandatory")
_Rx4flashPrgCntB_Type = Integer32
_Rx4flashPrgCntB_Object = MibTableColumn
rx4flashPrgCntB = _Rx4flashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 11),
    _Rx4flashPrgCntB_Type()
)
rx4flashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4flashPrgCntB.setStatus("mandatory")


class _Rx4fwRev0_Type(DisplayString):
    """Custom type rx4fwRev0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4fwRev0_Type.__name__ = "DisplayString"
_Rx4fwRev0_Object = MibTableColumn
rx4fwRev0 = _Rx4fwRev0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 12),
    _Rx4fwRev0_Type()
)
rx4fwRev0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4fwRev0.setStatus("mandatory")


class _Rx4fwRev1_Type(DisplayString):
    """Custom type rx4fwRev1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rx4fwRev1_Type.__name__ = "DisplayString"
_Rx4fwRev1_Object = MibTableColumn
rx4fwRev1 = _Rx4fwRev1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 5, 4, 13),
    _Rx4fwRev1_Type()
)
rx4fwRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx4fwRev1.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapRx200BX4ConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 1)
)
trapRx200BX4ConfigChangeInteger.setObjects(
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
    trapRx200BX4ConfigChangeInteger.setStatus(
        ""
    )

trapRx200BX4ConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 2)
)
trapRx200BX4ConfigChangeDisplayString.setObjects(
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
    trapRx200BX4ConfigChangeDisplayString.setStatus(
        ""
    )

trapRx200BX4OpticalPower1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 3)
)
trapRx200BX4OpticalPower1Alarm.setObjects(
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
    trapRx200BX4OpticalPower1Alarm.setStatus(
        ""
    )

trapRx200BX4OpticalPower2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 4)
)
trapRx200BX4OpticalPower2Alarm.setObjects(
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
    trapRx200BX4OpticalPower2Alarm.setStatus(
        ""
    )

trapRx200BX4OpticalPower3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 5)
)
trapRx200BX4OpticalPower3Alarm.setObjects(
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
    trapRx200BX4OpticalPower3Alarm.setStatus(
        ""
    )

trapRx200BX4OpticalPower4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 6)
)
trapRx200BX4OpticalPower4Alarm.setObjects(
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
    trapRx200BX4OpticalPower4Alarm.setStatus(
        ""
    )

trapRx200BX4ModuleTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 7)
)
trapRx200BX4ModuleTemperatureAlarm.setObjects(
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
    trapRx200BX4ModuleTemperatureAlarm.setStatus(
        ""
    )

trapRx200BX4FanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 8)
)
trapRx200BX4FanCurrentAlarm.setObjects(
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
    trapRx200BX4FanCurrentAlarm.setStatus(
        ""
    )

trapRx200BX4Plus12CurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 9)
)
trapRx200BX4Plus12CurrentAlarm.setObjects(
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
    trapRx200BX4Plus12CurrentAlarm.setStatus(
        ""
    )

trapRx200BX4Boot0Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 10)
)
trapRx200BX4Boot0Alarm.setObjects(
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
    trapRx200BX4Boot0Alarm.setStatus(
        ""
    )

trapRx200BX4Boot1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 11)
)
trapRx200BX4Boot1Alarm.setObjects(
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
    trapRx200BX4Boot1Alarm.setStatus(
        ""
    )

trapRx200BX4FlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 12)
)
trapRx200BX4FlashAlarm.setObjects(
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
    trapRx200BX4FlashAlarm.setStatus(
        ""
    )

trapRx200BX4AlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 13)
)
trapRx200BX4AlarmDataCRCAlarm.setObjects(
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
    trapRx200BX4AlarmDataCRCAlarm.setStatus(
        ""
    )

trapRx200BX4FactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 14)
)
trapRx200BX4FactoryDataCRCAlarm.setObjects(
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
    trapRx200BX4FactoryDataCRCAlarm.setStatus(
        ""
    )

trapRx200BX4CalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 15)
)
trapRx200BX4CalDataCRCAlarm.setObjects(
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
    trapRx200BX4CalDataCRCAlarm.setStatus(
        ""
    )

trapRx200BX4DefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 16)
)
trapRx200BX4DefaultAlarm.setObjects(
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
    trapRx200BX4DefaultAlarm.setStatus(
        ""
    )

trapRx200BX4Mode1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 17)
)
trapRx200BX4Mode1Alarm.setObjects(
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
    trapRx200BX4Mode1Alarm.setStatus(
        ""
    )

trapRx200BX4Mode2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 18)
)
trapRx200BX4Mode2Alarm.setObjects(
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
    trapRx200BX4Mode2Alarm.setStatus(
        ""
    )

trapRx200BX4Mode3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 19)
)
trapRx200BX4Mode3Alarm.setObjects(
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
    trapRx200BX4Mode3Alarm.setStatus(
        ""
    )

trapRx200BX4Mode4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 20)
)
trapRx200BX4Mode4Alarm.setObjects(
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
    trapRx200BX4Mode4Alarm.setStatus(
        ""
    )

trapRx200BX4Output1SwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 21)
)
trapRx200BX4Output1SwitchedAlarm.setObjects(
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
    trapRx200BX4Output1SwitchedAlarm.setStatus(
        ""
    )

trapRx200BX4Output2SwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 22)
)
trapRx200BX4Output2SwitchedAlarm.setObjects(
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
    trapRx200BX4Output2SwitchedAlarm.setStatus(
        ""
    )

trapRx200BX4Output3SwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 23)
)
trapRx200BX4Output3SwitchedAlarm.setObjects(
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
    trapRx200BX4Output3SwitchedAlarm.setStatus(
        ""
    )

trapRx200BX4Output4SwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 24)
)
trapRx200BX4Output4SwitchedAlarm.setObjects(
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
    trapRx200BX4Output4SwitchedAlarm.setStatus(
        ""
    )

trapRx200BX4RX1StatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 25)
)
trapRx200BX4RX1StatusAlarm.setObjects(
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
    trapRx200BX4RX1StatusAlarm.setStatus(
        ""
    )

trapRx200BX4RX2StatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 26)
)
trapRx200BX4RX2StatusAlarm.setObjects(
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
    trapRx200BX4RX2StatusAlarm.setStatus(
        ""
    )

trapRx200BX4RX3StatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 27)
)
trapRx200BX4RX3StatusAlarm.setObjects(
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
    trapRx200BX4RX3StatusAlarm.setStatus(
        ""
    )

trapRx200BX4RX4StatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 28)
)
trapRx200BX4RX4StatusAlarm.setObjects(
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
    trapRx200BX4RX4StatusAlarm.setStatus(
        ""
    )

trapRx200BX4BackupCableAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 29)
)
trapRx200BX4BackupCableAlarm.setObjects(
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
    trapRx200BX4BackupCableAlarm.setStatus(
        ""
    )

trapRx200BX4OptPwr1BadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 30)
)
trapRx200BX4OptPwr1BadAlarm.setObjects(
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
    trapRx200BX4OptPwr1BadAlarm.setStatus(
        ""
    )

trapRx200BX4OptPwr2BadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 31)
)
trapRx200BX4OptPwr2BadAlarm.setObjects(
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
    trapRx200BX4OptPwr2BadAlarm.setStatus(
        ""
    )

trapRx200BX4OptPwr3BadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 32)
)
trapRx200BX4OptPwr3BadAlarm.setObjects(
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
    trapRx200BX4OptPwr3BadAlarm.setStatus(
        ""
    )

trapRx200BX4OptPwr4BadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29, 0, 33)
)
trapRx200BX4OptPwr4BadAlarm.setObjects(
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
    trapRx200BX4OptPwr4BadAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2Rx200BX4-MIB",
    **{"Float": Float,
       "U32Data": U32Data,
       "trapRx200BX4ConfigChangeInteger": trapRx200BX4ConfigChangeInteger,
       "trapRx200BX4ConfigChangeDisplayString": trapRx200BX4ConfigChangeDisplayString,
       "trapRx200BX4OpticalPower1Alarm": trapRx200BX4OpticalPower1Alarm,
       "trapRx200BX4OpticalPower2Alarm": trapRx200BX4OpticalPower2Alarm,
       "trapRx200BX4OpticalPower3Alarm": trapRx200BX4OpticalPower3Alarm,
       "trapRx200BX4OpticalPower4Alarm": trapRx200BX4OpticalPower4Alarm,
       "trapRx200BX4ModuleTemperatureAlarm": trapRx200BX4ModuleTemperatureAlarm,
       "trapRx200BX4FanCurrentAlarm": trapRx200BX4FanCurrentAlarm,
       "trapRx200BX4Plus12CurrentAlarm": trapRx200BX4Plus12CurrentAlarm,
       "trapRx200BX4Boot0Alarm": trapRx200BX4Boot0Alarm,
       "trapRx200BX4Boot1Alarm": trapRx200BX4Boot1Alarm,
       "trapRx200BX4FlashAlarm": trapRx200BX4FlashAlarm,
       "trapRx200BX4AlarmDataCRCAlarm": trapRx200BX4AlarmDataCRCAlarm,
       "trapRx200BX4FactoryDataCRCAlarm": trapRx200BX4FactoryDataCRCAlarm,
       "trapRx200BX4CalDataCRCAlarm": trapRx200BX4CalDataCRCAlarm,
       "trapRx200BX4DefaultAlarm": trapRx200BX4DefaultAlarm,
       "trapRx200BX4Mode1Alarm": trapRx200BX4Mode1Alarm,
       "trapRx200BX4Mode2Alarm": trapRx200BX4Mode2Alarm,
       "trapRx200BX4Mode3Alarm": trapRx200BX4Mode3Alarm,
       "trapRx200BX4Mode4Alarm": trapRx200BX4Mode4Alarm,
       "trapRx200BX4Output1SwitchedAlarm": trapRx200BX4Output1SwitchedAlarm,
       "trapRx200BX4Output2SwitchedAlarm": trapRx200BX4Output2SwitchedAlarm,
       "trapRx200BX4Output3SwitchedAlarm": trapRx200BX4Output3SwitchedAlarm,
       "trapRx200BX4Output4SwitchedAlarm": trapRx200BX4Output4SwitchedAlarm,
       "trapRx200BX4RX1StatusAlarm": trapRx200BX4RX1StatusAlarm,
       "trapRx200BX4RX2StatusAlarm": trapRx200BX4RX2StatusAlarm,
       "trapRx200BX4RX3StatusAlarm": trapRx200BX4RX3StatusAlarm,
       "trapRx200BX4RX4StatusAlarm": trapRx200BX4RX4StatusAlarm,
       "trapRx200BX4BackupCableAlarm": trapRx200BX4BackupCableAlarm,
       "trapRx200BX4OptPwr1BadAlarm": trapRx200BX4OptPwr1BadAlarm,
       "trapRx200BX4OptPwr2BadAlarm": trapRx200BX4OptPwr2BadAlarm,
       "trapRx200BX4OptPwr3BadAlarm": trapRx200BX4OptPwr3BadAlarm,
       "trapRx200BX4OptPwr4BadAlarm": trapRx200BX4OptPwr4BadAlarm,
       "gx2Rx200BX4Descriptor": gx2Rx200BX4Descriptor,
       "gx2Rx200BX4AnalogTable": gx2Rx200BX4AnalogTable,
       "gx2Rx200BX4AnalogEntry": gx2Rx200BX4AnalogEntry,
       "gx2Rx200BX4AnalogTableIndex": gx2Rx200BX4AnalogTableIndex,
       "rx4labelOptPowerOne": rx4labelOptPowerOne,
       "rx4uomOptPowerOne": rx4uomOptPowerOne,
       "rx4majorHighOptPowerOne": rx4majorHighOptPowerOne,
       "rx4majorLowOptPowerOne": rx4majorLowOptPowerOne,
       "rx4minorHighOptPowerOne": rx4minorHighOptPowerOne,
       "rx4minorLowOptPowerOne": rx4minorLowOptPowerOne,
       "rx4currentValueOptPowerOne": rx4currentValueOptPowerOne,
       "rx4stateFlagOptPowerOne": rx4stateFlagOptPowerOne,
       "rx4minValueOptPowerOne": rx4minValueOptPowerOne,
       "rx4maxValueOptPowerOne": rx4maxValueOptPowerOne,
       "rx4alarmStateOptPowerOne": rx4alarmStateOptPowerOne,
       "rx4labelOptPowerTwo": rx4labelOptPowerTwo,
       "rx4uomOptPowerTwo": rx4uomOptPowerTwo,
       "rx4majorHighOptPowerTwo": rx4majorHighOptPowerTwo,
       "rx4majorLowOptPowerTwo": rx4majorLowOptPowerTwo,
       "rx4minorHighOptPowerTwo": rx4minorHighOptPowerTwo,
       "rx4minorLowOptPowerTwo": rx4minorLowOptPowerTwo,
       "rx4currentValueOptPowerTwo": rx4currentValueOptPowerTwo,
       "rx4stateFlagOptPowerTwo": rx4stateFlagOptPowerTwo,
       "rx4minValueOptPowerTwo": rx4minValueOptPowerTwo,
       "rx4maxValueOptPowerTwo": rx4maxValueOptPowerTwo,
       "rx4alarmStateOptPowerTwo": rx4alarmStateOptPowerTwo,
       "rx4labelOptPowerThree": rx4labelOptPowerThree,
       "rx4uomOptPowerThree": rx4uomOptPowerThree,
       "rx4majorHighOptPowerThree": rx4majorHighOptPowerThree,
       "rx4majorLowOptPowerThree": rx4majorLowOptPowerThree,
       "rx4minorHighOptPowerThree": rx4minorHighOptPowerThree,
       "rx4minorLowOptPowerThree": rx4minorLowOptPowerThree,
       "rx4currentValueOptPowerThree": rx4currentValueOptPowerThree,
       "rx4stateFlagOptPowerThree": rx4stateFlagOptPowerThree,
       "rx4minValueOptPowerThree": rx4minValueOptPowerThree,
       "rx4maxValueOptPowerThree": rx4maxValueOptPowerThree,
       "rx4alarmStateOptPowerThree": rx4alarmStateOptPowerThree,
       "rx4labelOptPowerFour": rx4labelOptPowerFour,
       "rx4uomOptPowerFour": rx4uomOptPowerFour,
       "rx4majorHighOptPowerFour": rx4majorHighOptPowerFour,
       "rx4majorLowOptPowerFour": rx4majorLowOptPowerFour,
       "rx4minorHighOptPowerFour": rx4minorHighOptPowerFour,
       "rx4minorLowOptPowerFour": rx4minorLowOptPowerFour,
       "rx4currentValueOptPowerFour": rx4currentValueOptPowerFour,
       "rx4stateFlagOptPowerFour": rx4stateFlagOptPowerFour,
       "rx4minValueOptPowerFour": rx4minValueOptPowerFour,
       "rx4maxValueOptPowerFour": rx4maxValueOptPowerFour,
       "rx4alarmStateOptPowerFour": rx4alarmStateOptPowerFour,
       "rx4labelModTemp": rx4labelModTemp,
       "rx4uomModTemp": rx4uomModTemp,
       "rx4majorHighModTemp": rx4majorHighModTemp,
       "rx4majorLowModTemp": rx4majorLowModTemp,
       "rx4minorHighModTemp": rx4minorHighModTemp,
       "rx4minorLowModTemp": rx4minorLowModTemp,
       "rx4currentValueModTemp": rx4currentValueModTemp,
       "rx4stateFlagModTemp": rx4stateFlagModTemp,
       "rx4minValueModTemp": rx4minValueModTemp,
       "rx4maxValueModTemp": rx4maxValueModTemp,
       "rx4alarmStateModTemp": rx4alarmStateModTemp,
       "rx4labelFanCurrent": rx4labelFanCurrent,
       "rx4uomFanCurrent": rx4uomFanCurrent,
       "rx4majorHighFanCurrent": rx4majorHighFanCurrent,
       "rx4majorLowFanCurrent": rx4majorLowFanCurrent,
       "rx4minorHighFanCurrent": rx4minorHighFanCurrent,
       "rx4minorLowFanCurrent": rx4minorLowFanCurrent,
       "rx4currentValueFanCurrent": rx4currentValueFanCurrent,
       "rx4stateFlagFanCurrent": rx4stateFlagFanCurrent,
       "rx4minValueFanCurrent": rx4minValueFanCurrent,
       "rx4maxValueFanCurrent": rx4maxValueFanCurrent,
       "rx4alarmStateFanCurrent": rx4alarmStateFanCurrent,
       "rx4label12Volt": rx4label12Volt,
       "rx4uom12Volt": rx4uom12Volt,
       "rx4majorHigh12Volt": rx4majorHigh12Volt,
       "rx4majorLow12Volt": rx4majorLow12Volt,
       "rx4minorHigh12Volt": rx4minorHigh12Volt,
       "rx4minorLow12Volt": rx4minorLow12Volt,
       "rx4currentValue12Volt": rx4currentValue12Volt,
       "rx4stateFlag12Volt": rx4stateFlag12Volt,
       "rx4minValue12Volt": rx4minValue12Volt,
       "rx4maxValue12Volt": rx4maxValue12Volt,
       "rx4alarmState12Volt": rx4alarmState12Volt,
       "gx2Rx200BX4DigitalTable": gx2Rx200BX4DigitalTable,
       "gx2Rx200BX4DigitalEntry": gx2Rx200BX4DigitalEntry,
       "gx2Rx200BX4DigitalTableIndex": gx2Rx200BX4DigitalTableIndex,
       "rx4labelModeOne": rx4labelModeOne,
       "rx4enumModeOne": rx4enumModeOne,
       "rx4valueModeOne": rx4valueModeOne,
       "rx4stateFlagModeOne": rx4stateFlagModeOne,
       "rx4labelWavelengthOne": rx4labelWavelengthOne,
       "rx4enumWavelengthOne": rx4enumWavelengthOne,
       "rx4valueWavelengthOne": rx4valueWavelengthOne,
       "rx4stateFlagWavelengthOne": rx4stateFlagWavelengthOne,
       "rx4labelAttnSettingOne": rx4labelAttnSettingOne,
       "rx4enumAttnSettingOne": rx4enumAttnSettingOne,
       "rx4valueAttnSettingOne": rx4valueAttnSettingOne,
       "rx4stateFlagAttnSettingOne": rx4stateFlagAttnSettingOne,
       "rx4labelSwModeSettingOne": rx4labelSwModeSettingOne,
       "rx4enumSwModeSettingOne": rx4enumSwModeSettingOne,
       "rx4valueSwModeSettingOne": rx4valueSwModeSettingOne,
       "rx4stateFlagSwModeSettingOne": rx4stateFlagSwModeSettingOne,
       "rx4labelSwModeThresholdOne": rx4labelSwModeThresholdOne,
       "rx4enumSwModeThresholdOne": rx4enumSwModeThresholdOne,
       "rx4valueSwModeThresholdOne": rx4valueSwModeThresholdOne,
       "rx4stateFlagSwModeThresholdOne": rx4stateFlagSwModeThresholdOne,
       "rx4labelModeTwo": rx4labelModeTwo,
       "rx4enumModeTwo": rx4enumModeTwo,
       "rx4valueModeTwo": rx4valueModeTwo,
       "rx4stateFlagModeTwo": rx4stateFlagModeTwo,
       "rx4labelWavelengthTwo": rx4labelWavelengthTwo,
       "rx4enumWavelengthTwo": rx4enumWavelengthTwo,
       "rx4valueWavelengthTwo": rx4valueWavelengthTwo,
       "rx4stateFlagWavelengthTwo": rx4stateFlagWavelengthTwo,
       "rx4labelAttnSettingTwo": rx4labelAttnSettingTwo,
       "rx4enumAttnSettingTwo": rx4enumAttnSettingTwo,
       "rx4valueAttnSettingTwo": rx4valueAttnSettingTwo,
       "rx4stateFlagAttnSettingTwo": rx4stateFlagAttnSettingTwo,
       "rx4labelSwModeSettingTwo": rx4labelSwModeSettingTwo,
       "rx4enumSwModeSettingTwo": rx4enumSwModeSettingTwo,
       "rx4valueSwModeSettingTwo": rx4valueSwModeSettingTwo,
       "rx4stateFlagSwModeSettingTwo": rx4stateFlagSwModeSettingTwo,
       "rx4labelSwModeThresholdTwo": rx4labelSwModeThresholdTwo,
       "rx4enumSwModeThresholdTwo": rx4enumSwModeThresholdTwo,
       "rx4valueSwModeThresholdTwo": rx4valueSwModeThresholdTwo,
       "rx4stateFlagSwModeThresholdTwo": rx4stateFlagSwModeThresholdTwo,
       "rx4labelModeThree": rx4labelModeThree,
       "rx4enumModeThree": rx4enumModeThree,
       "rx4valueModeThree": rx4valueModeThree,
       "rx4stateFlagModeThree": rx4stateFlagModeThree,
       "rx4labelWavelengthThree": rx4labelWavelengthThree,
       "rx4enumWavelengthThree": rx4enumWavelengthThree,
       "rx4valueWavelengthThree": rx4valueWavelengthThree,
       "rx4stateFlagWavelengthThree": rx4stateFlagWavelengthThree,
       "rx4labelAttnSettingThree": rx4labelAttnSettingThree,
       "rx4enumAttnSettingThree": rx4enumAttnSettingThree,
       "rx4valueAttnSettingThree": rx4valueAttnSettingThree,
       "rx4stateFlagAttnSettingThree": rx4stateFlagAttnSettingThree,
       "rx4labelSwModeSettingThree": rx4labelSwModeSettingThree,
       "rx4enumSwModeSettingThree": rx4enumSwModeSettingThree,
       "rx4valueSwModeSettingThree": rx4valueSwModeSettingThree,
       "rx4stateFlagSwModeSettingThree": rx4stateFlagSwModeSettingThree,
       "rx4labelSwModeThresholdThree": rx4labelSwModeThresholdThree,
       "rx4enumSwModeThresholdThree": rx4enumSwModeThresholdThree,
       "rx4valueSwModeThresholdThree": rx4valueSwModeThresholdThree,
       "rx4stateFlagSwModeThresholdThree": rx4stateFlagSwModeThresholdThree,
       "rx4labelModeFour": rx4labelModeFour,
       "rx4enumModeFour": rx4enumModeFour,
       "rx4valueModeFour": rx4valueModeFour,
       "rx4stateFlagModeFour": rx4stateFlagModeFour,
       "rx4labelWavelengthFour": rx4labelWavelengthFour,
       "rx4enumWavelengthFour": rx4enumWavelengthFour,
       "rx4valueWavelengthFour": rx4valueWavelengthFour,
       "rx4stateFlagWavelengthFour": rx4stateFlagWavelengthFour,
       "rx4labelAttnSettingFour": rx4labelAttnSettingFour,
       "rx4enumAttnSettingFour": rx4enumAttnSettingFour,
       "rx4valueAttnSettingFour": rx4valueAttnSettingFour,
       "rx4stateFlagAttnSettingFour": rx4stateFlagAttnSettingFour,
       "rx4labelSwModeSettingFour": rx4labelSwModeSettingFour,
       "rx4enumSwModeSettingFour": rx4enumSwModeSettingFour,
       "rx4valueSwModeSettingFour": rx4valueSwModeSettingFour,
       "rx4stateFlagSwModeSettingFour": rx4stateFlagSwModeSettingFour,
       "rx4labelSwModeThresholdFour": rx4labelSwModeThresholdFour,
       "rx4enumSwModeThresholdFour": rx4enumSwModeThresholdFour,
       "rx4valueSwModeThresholdFour": rx4valueSwModeThresholdFour,
       "rx4stateFlagSwModeThresholdFour": rx4stateFlagSwModeThresholdFour,
       "rx4labelModuleConfig": rx4labelModuleConfig,
       "rx4enumModuleConfig": rx4enumModuleConfig,
       "rx4valueModuleConfig": rx4valueModuleConfig,
       "rx4stateFlagModuleConfig": rx4stateFlagModuleConfig,
       "rx4labelRevertTime": rx4labelRevertTime,
       "rx4enumRevertTime": rx4enumRevertTime,
       "rx4valueRevertTime": rx4valueRevertTime,
       "rx4stateFlagRevertTime": rx4stateFlagRevertTime,
       "rx4labelTestPointSelect": rx4labelTestPointSelect,
       "rx4enumTestPointSelect": rx4enumTestPointSelect,
       "rx4valueTestPointSelect": rx4valueTestPointSelect,
       "rx4stateFlagTestPointSelect": rx4stateFlagTestPointSelect,
       "rx4labelFactoryDefault": rx4labelFactoryDefault,
       "rx4enumFactoryDefault": rx4enumFactoryDefault,
       "rx4valueFactoryDefault": rx4valueFactoryDefault,
       "rx4stateFlagFactoryDefault": rx4stateFlagFactoryDefault,
       "gx2Rx200BX4StatusTable": gx2Rx200BX4StatusTable,
       "gx2Rx200BX4StatusEntry": gx2Rx200BX4StatusEntry,
       "gx2Rx200BX4StatusTableIndex": gx2Rx200BX4StatusTableIndex,
       "rx4labelBoot": rx4labelBoot,
       "rx4valueBoot": rx4valueBoot,
       "rx4stateflagBoot": rx4stateflagBoot,
       "rx4labelFlash": rx4labelFlash,
       "rx4valueFlash": rx4valueFlash,
       "rx4stateflagFlash": rx4stateflagFlash,
       "rx4labelFactoryDataCRC": rx4labelFactoryDataCRC,
       "rx4valueFactoryDataCRC": rx4valueFactoryDataCRC,
       "rx4stateflagFactoryDataCRC": rx4stateflagFactoryDataCRC,
       "rx4labelAlarmDataCRC": rx4labelAlarmDataCRC,
       "rx4valueAlarmDataCRC": rx4valueAlarmDataCRC,
       "rx4stateflagAlarmDataCRC": rx4stateflagAlarmDataCRC,
       "rx4labelCalibrationDataCRC": rx4labelCalibrationDataCRC,
       "rx4valueCalibrationDataCRC": rx4valueCalibrationDataCRC,
       "rx4stateflagCalibrationDataCRC": rx4stateflagCalibrationDataCRC,
       "rx4labelHW": rx4labelHW,
       "rx4valueHW": rx4valueHW,
       "rx4stateflagHW": rx4stateflagHW,
       "rx4labelOptSigOne": rx4labelOptSigOne,
       "rx4valueOptSigOne": rx4valueOptSigOne,
       "rx4stateflagOptSigOne": rx4stateflagOptSigOne,
       "rx4labelOptSigTwo": rx4labelOptSigTwo,
       "rx4valueOptSigTwo": rx4valueOptSigTwo,
       "rx4stateflagOptSigTwo": rx4stateflagOptSigTwo,
       "rx4labelOptSigThree": rx4labelOptSigThree,
       "rx4valueOptSigThree": rx4valueOptSigThree,
       "rx4stateflagOptSigThree": rx4stateflagOptSigThree,
       "rx4labelOptSigFour": rx4labelOptSigFour,
       "rx4valueOptSigFour": rx4valueOptSigFour,
       "rx4stateflagOptSigFour": rx4stateflagOptSigFour,
       "rx4labelBackupCable": rx4labelBackupCable,
       "rx4valueBackupCable": rx4valueBackupCable,
       "rx4stateflagBackupCable": rx4stateflagBackupCable,
       "gx2Rx200BX4FactoryTable": gx2Rx200BX4FactoryTable,
       "gx2Rx200BX4FactoryEntry": gx2Rx200BX4FactoryEntry,
       "gx2Rx200BX4FactoryTableIndex": gx2Rx200BX4FactoryTableIndex,
       "rx4bootControlByte": rx4bootControlByte,
       "rx4bootStatusByte": rx4bootStatusByte,
       "rx4bank0CRC": rx4bank0CRC,
       "rx4bank1CRC": rx4bank1CRC,
       "rx4prgEEPROMByte": rx4prgEEPROMByte,
       "rx4factoryCRC": rx4factoryCRC,
       "rx4calculateCRC": rx4calculateCRC,
       "rx4hourMeter": rx4hourMeter,
       "rx4flashPrgCntA": rx4flashPrgCntA,
       "rx4flashPrgCntB": rx4flashPrgCntB,
       "rx4fwRev0": rx4fwRev0,
       "rx4fwRev1": rx4fwRev1}
)
