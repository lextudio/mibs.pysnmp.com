# SNMP MIB module (OMNI-gx2OSW10B-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2OSW10B-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:28 2024
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

(gx2Osw10b,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Osw10b")

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

_Gx2Osw10bDescriptor_ObjectIdentity = ObjectIdentity
gx2Osw10bDescriptor = _Gx2Osw10bDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 1)
)
_Gx2Osw10bAnalogTable_Object = MibTable
gx2Osw10bAnalogTable = _Gx2Osw10bAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2)
)
if mibBuilder.loadTexts:
    gx2Osw10bAnalogTable.setStatus("mandatory")
_Gx2Osw10bAnalogEntry_Object = MibTableRow
gx2Osw10bAnalogEntry = _Gx2Osw10bAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1)
)
gx2Osw10bAnalogEntry.setIndexNames(
    (0, "OMNI-gx2OSW10B-MIB", "gx2Osw10bAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Osw10bAnalogEntry.setStatus("mandatory")


class _Gx2Osw10bAnalogTableIndex_Type(Integer32):
    """Custom type gx2Osw10bAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Osw10bAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Osw10bAnalogTableIndex_Object = MibTableColumn
gx2Osw10bAnalogTableIndex = _Gx2Osw10bAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 1),
    _Gx2Osw10bAnalogTableIndex_Type()
)
gx2Osw10bAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Osw10bAnalogTableIndex.setStatus("mandatory")


class _Osw10blabelPriOpticalInputLevel_Type(DisplayString):
    """Custom type osw10blabelPriOpticalInputLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelPriOpticalInputLevel_Type.__name__ = "DisplayString"
_Osw10blabelPriOpticalInputLevel_Object = MibTableColumn
osw10blabelPriOpticalInputLevel = _Osw10blabelPriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 2),
    _Osw10blabelPriOpticalInputLevel_Type()
)
osw10blabelPriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelPriOpticalInputLevel.setStatus("optional")


class _Osw10buomPriOpticalInputLevel_Type(DisplayString):
    """Custom type osw10buomPriOpticalInputLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10buomPriOpticalInputLevel_Type.__name__ = "DisplayString"
_Osw10buomPriOpticalInputLevel_Object = MibTableColumn
osw10buomPriOpticalInputLevel = _Osw10buomPriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 3),
    _Osw10buomPriOpticalInputLevel_Type()
)
osw10buomPriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10buomPriOpticalInputLevel.setStatus("optional")
_Osw10bmajorHighPriOpticalInputLevel_Type = Float
_Osw10bmajorHighPriOpticalInputLevel_Object = MibTableColumn
osw10bmajorHighPriOpticalInputLevel = _Osw10bmajorHighPriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 4),
    _Osw10bmajorHighPriOpticalInputLevel_Type()
)
osw10bmajorHighPriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorHighPriOpticalInputLevel.setStatus("mandatory")
_Osw10bmajorLowPriOpticalInputLevel_Type = Float
_Osw10bmajorLowPriOpticalInputLevel_Object = MibTableColumn
osw10bmajorLowPriOpticalInputLevel = _Osw10bmajorLowPriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 5),
    _Osw10bmajorLowPriOpticalInputLevel_Type()
)
osw10bmajorLowPriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorLowPriOpticalInputLevel.setStatus("mandatory")
_Osw10bminorHighPriOpticalInputLevel_Type = Float
_Osw10bminorHighPriOpticalInputLevel_Object = MibTableColumn
osw10bminorHighPriOpticalInputLevel = _Osw10bminorHighPriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 6),
    _Osw10bminorHighPriOpticalInputLevel_Type()
)
osw10bminorHighPriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorHighPriOpticalInputLevel.setStatus("mandatory")
_Osw10bminorLowPriOpticalInputLevel_Type = Float
_Osw10bminorLowPriOpticalInputLevel_Object = MibTableColumn
osw10bminorLowPriOpticalInputLevel = _Osw10bminorLowPriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 7),
    _Osw10bminorLowPriOpticalInputLevel_Type()
)
osw10bminorLowPriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorLowPriOpticalInputLevel.setStatus("mandatory")
_Osw10bcurrentValuePriOpticalInputLevel_Type = Float
_Osw10bcurrentValuePriOpticalInputLevel_Object = MibTableColumn
osw10bcurrentValuePriOpticalInputLevel = _Osw10bcurrentValuePriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 8),
    _Osw10bcurrentValuePriOpticalInputLevel_Type()
)
osw10bcurrentValuePriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bcurrentValuePriOpticalInputLevel.setStatus("mandatory")


class _Osw10bstateFlagPriOpticalInputLevel_Type(Integer32):
    """Custom type osw10bstateFlagPriOpticalInputLevel based on Integer32"""
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


_Osw10bstateFlagPriOpticalInputLevel_Type.__name__ = "Integer32"
_Osw10bstateFlagPriOpticalInputLevel_Object = MibTableColumn
osw10bstateFlagPriOpticalInputLevel = _Osw10bstateFlagPriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 9),
    _Osw10bstateFlagPriOpticalInputLevel_Type()
)
osw10bstateFlagPriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateFlagPriOpticalInputLevel.setStatus("mandatory")
_Osw10bminValuePriOpticalInputLevel_Type = Float
_Osw10bminValuePriOpticalInputLevel_Object = MibTableColumn
osw10bminValuePriOpticalInputLevel = _Osw10bminValuePriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 10),
    _Osw10bminValuePriOpticalInputLevel_Type()
)
osw10bminValuePriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminValuePriOpticalInputLevel.setStatus("mandatory")
_Osw10bmaxValuePriOpticalInputLevel_Type = Float
_Osw10bmaxValuePriOpticalInputLevel_Object = MibTableColumn
osw10bmaxValuePriOpticalInputLevel = _Osw10bmaxValuePriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 11),
    _Osw10bmaxValuePriOpticalInputLevel_Type()
)
osw10bmaxValuePriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmaxValuePriOpticalInputLevel.setStatus("mandatory")


class _Osw10balarmStatePriOpticalInputLevel_Type(Integer32):
    """Custom type osw10balarmStatePriOpticalInputLevel based on Integer32"""
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


_Osw10balarmStatePriOpticalInputLevel_Type.__name__ = "Integer32"
_Osw10balarmStatePriOpticalInputLevel_Object = MibTableColumn
osw10balarmStatePriOpticalInputLevel = _Osw10balarmStatePriOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 12),
    _Osw10balarmStatePriOpticalInputLevel_Type()
)
osw10balarmStatePriOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10balarmStatePriOpticalInputLevel.setStatus("mandatory")


class _Osw10blabelSecOpticalInputLevel_Type(DisplayString):
    """Custom type osw10blabelSecOpticalInputLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelSecOpticalInputLevel_Type.__name__ = "DisplayString"
_Osw10blabelSecOpticalInputLevel_Object = MibTableColumn
osw10blabelSecOpticalInputLevel = _Osw10blabelSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 13),
    _Osw10blabelSecOpticalInputLevel_Type()
)
osw10blabelSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelSecOpticalInputLevel.setStatus("optional")


class _Osw10buomSecOpticalInputLevel_Type(DisplayString):
    """Custom type osw10buomSecOpticalInputLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10buomSecOpticalInputLevel_Type.__name__ = "DisplayString"
_Osw10buomSecOpticalInputLevel_Object = MibTableColumn
osw10buomSecOpticalInputLevel = _Osw10buomSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 14),
    _Osw10buomSecOpticalInputLevel_Type()
)
osw10buomSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10buomSecOpticalInputLevel.setStatus("optional")
_Osw10bmajorHighSecOpticalInputLevel_Type = Float
_Osw10bmajorHighSecOpticalInputLevel_Object = MibTableColumn
osw10bmajorHighSecOpticalInputLevel = _Osw10bmajorHighSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 15),
    _Osw10bmajorHighSecOpticalInputLevel_Type()
)
osw10bmajorHighSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorHighSecOpticalInputLevel.setStatus("mandatory")
_Osw10bmajorLowSecOpticalInputLevel_Type = Float
_Osw10bmajorLowSecOpticalInputLevel_Object = MibTableColumn
osw10bmajorLowSecOpticalInputLevel = _Osw10bmajorLowSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 16),
    _Osw10bmajorLowSecOpticalInputLevel_Type()
)
osw10bmajorLowSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorLowSecOpticalInputLevel.setStatus("mandatory")
_Osw10bminorHighSecOpticalInputLevel_Type = Float
_Osw10bminorHighSecOpticalInputLevel_Object = MibTableColumn
osw10bminorHighSecOpticalInputLevel = _Osw10bminorHighSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 17),
    _Osw10bminorHighSecOpticalInputLevel_Type()
)
osw10bminorHighSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorHighSecOpticalInputLevel.setStatus("mandatory")
_Osw10bminorLowSecOpticalInputLevel_Type = Float
_Osw10bminorLowSecOpticalInputLevel_Object = MibTableColumn
osw10bminorLowSecOpticalInputLevel = _Osw10bminorLowSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 18),
    _Osw10bminorLowSecOpticalInputLevel_Type()
)
osw10bminorLowSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorLowSecOpticalInputLevel.setStatus("mandatory")
_Osw10bcurrentValueSecOpticalInputLevel_Type = Float
_Osw10bcurrentValueSecOpticalInputLevel_Object = MibTableColumn
osw10bcurrentValueSecOpticalInputLevel = _Osw10bcurrentValueSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 19),
    _Osw10bcurrentValueSecOpticalInputLevel_Type()
)
osw10bcurrentValueSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bcurrentValueSecOpticalInputLevel.setStatus("mandatory")


class _Osw10bstateFlagSecOpticalInputLevel_Type(Integer32):
    """Custom type osw10bstateFlagSecOpticalInputLevel based on Integer32"""
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


_Osw10bstateFlagSecOpticalInputLevel_Type.__name__ = "Integer32"
_Osw10bstateFlagSecOpticalInputLevel_Object = MibTableColumn
osw10bstateFlagSecOpticalInputLevel = _Osw10bstateFlagSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 20),
    _Osw10bstateFlagSecOpticalInputLevel_Type()
)
osw10bstateFlagSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateFlagSecOpticalInputLevel.setStatus("mandatory")
_Osw10bminValueSecOpticalInputLevel_Type = Float
_Osw10bminValueSecOpticalInputLevel_Object = MibTableColumn
osw10bminValueSecOpticalInputLevel = _Osw10bminValueSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 21),
    _Osw10bminValueSecOpticalInputLevel_Type()
)
osw10bminValueSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminValueSecOpticalInputLevel.setStatus("mandatory")
_Osw10bmaxValueSecOpticalInputLevel_Type = Float
_Osw10bmaxValueSecOpticalInputLevel_Object = MibTableColumn
osw10bmaxValueSecOpticalInputLevel = _Osw10bmaxValueSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 22),
    _Osw10bmaxValueSecOpticalInputLevel_Type()
)
osw10bmaxValueSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmaxValueSecOpticalInputLevel.setStatus("mandatory")


class _Osw10balarmStateSecOpticalInputLevel_Type(Integer32):
    """Custom type osw10balarmStateSecOpticalInputLevel based on Integer32"""
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


_Osw10balarmStateSecOpticalInputLevel_Type.__name__ = "Integer32"
_Osw10balarmStateSecOpticalInputLevel_Object = MibTableColumn
osw10balarmStateSecOpticalInputLevel = _Osw10balarmStateSecOpticalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 23),
    _Osw10balarmStateSecOpticalInputLevel_Type()
)
osw10balarmStateSecOpticalInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10balarmStateSecOpticalInputLevel.setStatus("mandatory")


class _Osw10blabelPriOpticalThreshold_Type(DisplayString):
    """Custom type osw10blabelPriOpticalThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelPriOpticalThreshold_Type.__name__ = "DisplayString"
_Osw10blabelPriOpticalThreshold_Object = MibTableColumn
osw10blabelPriOpticalThreshold = _Osw10blabelPriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 24),
    _Osw10blabelPriOpticalThreshold_Type()
)
osw10blabelPriOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelPriOpticalThreshold.setStatus("optional")


class _Osw10buomPriOpticalThreshold_Type(DisplayString):
    """Custom type osw10buomPriOpticalThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10buomPriOpticalThreshold_Type.__name__ = "DisplayString"
_Osw10buomPriOpticalThreshold_Object = MibTableColumn
osw10buomPriOpticalThreshold = _Osw10buomPriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 25),
    _Osw10buomPriOpticalThreshold_Type()
)
osw10buomPriOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10buomPriOpticalThreshold.setStatus("optional")
_Osw10bmajorHighPriOpticalThreshold_Type = Float
_Osw10bmajorHighPriOpticalThreshold_Object = MibTableColumn
osw10bmajorHighPriOpticalThreshold = _Osw10bmajorHighPriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 26),
    _Osw10bmajorHighPriOpticalThreshold_Type()
)
osw10bmajorHighPriOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorHighPriOpticalThreshold.setStatus("mandatory")
_Osw10bmajorLowPriOpticalThreshold_Type = Float
_Osw10bmajorLowPriOpticalThreshold_Object = MibTableColumn
osw10bmajorLowPriOpticalThreshold = _Osw10bmajorLowPriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 27),
    _Osw10bmajorLowPriOpticalThreshold_Type()
)
osw10bmajorLowPriOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorLowPriOpticalThreshold.setStatus("mandatory")
_Osw10bminorHighPriOpticalThreshold_Type = Float
_Osw10bminorHighPriOpticalThreshold_Object = MibTableColumn
osw10bminorHighPriOpticalThreshold = _Osw10bminorHighPriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 28),
    _Osw10bminorHighPriOpticalThreshold_Type()
)
osw10bminorHighPriOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorHighPriOpticalThreshold.setStatus("mandatory")
_Osw10bminorLowPriOpticalThreshold_Type = Float
_Osw10bminorLowPriOpticalThreshold_Object = MibTableColumn
osw10bminorLowPriOpticalThreshold = _Osw10bminorLowPriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 29),
    _Osw10bminorLowPriOpticalThreshold_Type()
)
osw10bminorLowPriOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorLowPriOpticalThreshold.setStatus("mandatory")
_Osw10bcurrentValuePriOpticalThreshold_Type = Float
_Osw10bcurrentValuePriOpticalThreshold_Object = MibTableColumn
osw10bcurrentValuePriOpticalThreshold = _Osw10bcurrentValuePriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 30),
    _Osw10bcurrentValuePriOpticalThreshold_Type()
)
osw10bcurrentValuePriOpticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bcurrentValuePriOpticalThreshold.setStatus("mandatory")


class _Osw10bstateFlagPriOpticalThreshold_Type(Integer32):
    """Custom type osw10bstateFlagPriOpticalThreshold based on Integer32"""
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


_Osw10bstateFlagPriOpticalThreshold_Type.__name__ = "Integer32"
_Osw10bstateFlagPriOpticalThreshold_Object = MibTableColumn
osw10bstateFlagPriOpticalThreshold = _Osw10bstateFlagPriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 31),
    _Osw10bstateFlagPriOpticalThreshold_Type()
)
osw10bstateFlagPriOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateFlagPriOpticalThreshold.setStatus("mandatory")
_Osw10bminValuePriOpticalThreshold_Type = Float
_Osw10bminValuePriOpticalThreshold_Object = MibTableColumn
osw10bminValuePriOpticalThreshold = _Osw10bminValuePriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 32),
    _Osw10bminValuePriOpticalThreshold_Type()
)
osw10bminValuePriOpticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bminValuePriOpticalThreshold.setStatus("mandatory")
_Osw10bmaxValuePriOpticalThreshold_Type = Float
_Osw10bmaxValuePriOpticalThreshold_Object = MibTableColumn
osw10bmaxValuePriOpticalThreshold = _Osw10bmaxValuePriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 33),
    _Osw10bmaxValuePriOpticalThreshold_Type()
)
osw10bmaxValuePriOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmaxValuePriOpticalThreshold.setStatus("mandatory")


class _Osw10balarmStatePriOpticalThreshold_Type(Integer32):
    """Custom type osw10balarmStatePriOpticalThreshold based on Integer32"""
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


_Osw10balarmStatePriOpticalThreshold_Type.__name__ = "Integer32"
_Osw10balarmStatePriOpticalThreshold_Object = MibTableColumn
osw10balarmStatePriOpticalThreshold = _Osw10balarmStatePriOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 34),
    _Osw10balarmStatePriOpticalThreshold_Type()
)
osw10balarmStatePriOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10balarmStatePriOpticalThreshold.setStatus("mandatory")


class _Osw10blabelSecOpticalThreshold_Type(DisplayString):
    """Custom type osw10blabelSecOpticalThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelSecOpticalThreshold_Type.__name__ = "DisplayString"
_Osw10blabelSecOpticalThreshold_Object = MibTableColumn
osw10blabelSecOpticalThreshold = _Osw10blabelSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 35),
    _Osw10blabelSecOpticalThreshold_Type()
)
osw10blabelSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelSecOpticalThreshold.setStatus("optional")


class _Osw10buomSecOpticalThreshold_Type(DisplayString):
    """Custom type osw10buomSecOpticalThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10buomSecOpticalThreshold_Type.__name__ = "DisplayString"
_Osw10buomSecOpticalThreshold_Object = MibTableColumn
osw10buomSecOpticalThreshold = _Osw10buomSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 36),
    _Osw10buomSecOpticalThreshold_Type()
)
osw10buomSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10buomSecOpticalThreshold.setStatus("optional")
_Osw10bmajorHighSecOpticalThreshold_Type = Float
_Osw10bmajorHighSecOpticalThreshold_Object = MibTableColumn
osw10bmajorHighSecOpticalThreshold = _Osw10bmajorHighSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 37),
    _Osw10bmajorHighSecOpticalThreshold_Type()
)
osw10bmajorHighSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorHighSecOpticalThreshold.setStatus("mandatory")
_Osw10bmajorLowSecOpticalThreshold_Type = Float
_Osw10bmajorLowSecOpticalThreshold_Object = MibTableColumn
osw10bmajorLowSecOpticalThreshold = _Osw10bmajorLowSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 38),
    _Osw10bmajorLowSecOpticalThreshold_Type()
)
osw10bmajorLowSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorLowSecOpticalThreshold.setStatus("mandatory")
_Osw10bminorHighSecOpticalThreshold_Type = Float
_Osw10bminorHighSecOpticalThreshold_Object = MibTableColumn
osw10bminorHighSecOpticalThreshold = _Osw10bminorHighSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 39),
    _Osw10bminorHighSecOpticalThreshold_Type()
)
osw10bminorHighSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorHighSecOpticalThreshold.setStatus("mandatory")
_Osw10bminorLowSecOpticalThreshold_Type = Float
_Osw10bminorLowSecOpticalThreshold_Object = MibTableColumn
osw10bminorLowSecOpticalThreshold = _Osw10bminorLowSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 40),
    _Osw10bminorLowSecOpticalThreshold_Type()
)
osw10bminorLowSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorLowSecOpticalThreshold.setStatus("mandatory")
_Osw10bcurrentValueSecOpticalThreshold_Type = Float
_Osw10bcurrentValueSecOpticalThreshold_Object = MibTableColumn
osw10bcurrentValueSecOpticalThreshold = _Osw10bcurrentValueSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 41),
    _Osw10bcurrentValueSecOpticalThreshold_Type()
)
osw10bcurrentValueSecOpticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bcurrentValueSecOpticalThreshold.setStatus("mandatory")


class _Osw10bstateFlagSecOpticalThreshold_Type(Integer32):
    """Custom type osw10bstateFlagSecOpticalThreshold based on Integer32"""
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


_Osw10bstateFlagSecOpticalThreshold_Type.__name__ = "Integer32"
_Osw10bstateFlagSecOpticalThreshold_Object = MibTableColumn
osw10bstateFlagSecOpticalThreshold = _Osw10bstateFlagSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 42),
    _Osw10bstateFlagSecOpticalThreshold_Type()
)
osw10bstateFlagSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateFlagSecOpticalThreshold.setStatus("mandatory")
_Osw10bminValueSecOpticalThreshold_Type = Float
_Osw10bminValueSecOpticalThreshold_Object = MibTableColumn
osw10bminValueSecOpticalThreshold = _Osw10bminValueSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 43),
    _Osw10bminValueSecOpticalThreshold_Type()
)
osw10bminValueSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminValueSecOpticalThreshold.setStatus("mandatory")
_Osw10bmaxValueSecOpticalThreshold_Type = Float
_Osw10bmaxValueSecOpticalThreshold_Object = MibTableColumn
osw10bmaxValueSecOpticalThreshold = _Osw10bmaxValueSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 44),
    _Osw10bmaxValueSecOpticalThreshold_Type()
)
osw10bmaxValueSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmaxValueSecOpticalThreshold.setStatus("mandatory")


class _Osw10balarmStateSecOpticalThreshold_Type(Integer32):
    """Custom type osw10balarmStateSecOpticalThreshold based on Integer32"""
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


_Osw10balarmStateSecOpticalThreshold_Type.__name__ = "Integer32"
_Osw10balarmStateSecOpticalThreshold_Object = MibTableColumn
osw10balarmStateSecOpticalThreshold = _Osw10balarmStateSecOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 45),
    _Osw10balarmStateSecOpticalThreshold_Type()
)
osw10balarmStateSecOpticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10balarmStateSecOpticalThreshold.setStatus("mandatory")


class _Osw10blabelModTemp_Type(DisplayString):
    """Custom type osw10blabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelModTemp_Type.__name__ = "DisplayString"
_Osw10blabelModTemp_Object = MibTableColumn
osw10blabelModTemp = _Osw10blabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 46),
    _Osw10blabelModTemp_Type()
)
osw10blabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelModTemp.setStatus("optional")


class _Osw10buomModTemp_Type(DisplayString):
    """Custom type osw10buomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10buomModTemp_Type.__name__ = "DisplayString"
_Osw10buomModTemp_Object = MibTableColumn
osw10buomModTemp = _Osw10buomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 47),
    _Osw10buomModTemp_Type()
)
osw10buomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10buomModTemp.setStatus("optional")
_Osw10bmajorHighModTemp_Type = Float
_Osw10bmajorHighModTemp_Object = MibTableColumn
osw10bmajorHighModTemp = _Osw10bmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 48),
    _Osw10bmajorHighModTemp_Type()
)
osw10bmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorHighModTemp.setStatus("mandatory")
_Osw10bmajorLowModTemp_Type = Float
_Osw10bmajorLowModTemp_Object = MibTableColumn
osw10bmajorLowModTemp = _Osw10bmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 49),
    _Osw10bmajorLowModTemp_Type()
)
osw10bmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorLowModTemp.setStatus("mandatory")
_Osw10bminorHighModTemp_Type = Float
_Osw10bminorHighModTemp_Object = MibTableColumn
osw10bminorHighModTemp = _Osw10bminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 50),
    _Osw10bminorHighModTemp_Type()
)
osw10bminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorHighModTemp.setStatus("mandatory")
_Osw10bminorLowModTemp_Type = Float
_Osw10bminorLowModTemp_Object = MibTableColumn
osw10bminorLowModTemp = _Osw10bminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 51),
    _Osw10bminorLowModTemp_Type()
)
osw10bminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorLowModTemp.setStatus("mandatory")
_Osw10bcurrentValueModTemp_Type = Float
_Osw10bcurrentValueModTemp_Object = MibTableColumn
osw10bcurrentValueModTemp = _Osw10bcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 52),
    _Osw10bcurrentValueModTemp_Type()
)
osw10bcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bcurrentValueModTemp.setStatus("mandatory")


class _Osw10bstateFlagModTemp_Type(Integer32):
    """Custom type osw10bstateFlagModTemp based on Integer32"""
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


_Osw10bstateFlagModTemp_Type.__name__ = "Integer32"
_Osw10bstateFlagModTemp_Object = MibTableColumn
osw10bstateFlagModTemp = _Osw10bstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 53),
    _Osw10bstateFlagModTemp_Type()
)
osw10bstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateFlagModTemp.setStatus("mandatory")
_Osw10bminValueModTemp_Type = Float
_Osw10bminValueModTemp_Object = MibTableColumn
osw10bminValueModTemp = _Osw10bminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 54),
    _Osw10bminValueModTemp_Type()
)
osw10bminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminValueModTemp.setStatus("mandatory")
_Osw10bmaxValueModTemp_Type = Float
_Osw10bmaxValueModTemp_Object = MibTableColumn
osw10bmaxValueModTemp = _Osw10bmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 55),
    _Osw10bmaxValueModTemp_Type()
)
osw10bmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmaxValueModTemp.setStatus("mandatory")


class _Osw10balarmStateModTemp_Type(Integer32):
    """Custom type osw10balarmStateModTemp based on Integer32"""
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


_Osw10balarmStateModTemp_Type.__name__ = "Integer32"
_Osw10balarmStateModTemp_Object = MibTableColumn
osw10balarmStateModTemp = _Osw10balarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 56),
    _Osw10balarmStateModTemp_Type()
)
osw10balarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10balarmStateModTemp.setStatus("mandatory")


class _Osw10blabelFanCurrent_Type(DisplayString):
    """Custom type osw10blabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelFanCurrent_Type.__name__ = "DisplayString"
_Osw10blabelFanCurrent_Object = MibTableColumn
osw10blabelFanCurrent = _Osw10blabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 57),
    _Osw10blabelFanCurrent_Type()
)
osw10blabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelFanCurrent.setStatus("optional")


class _Osw10buomFanCurrent_Type(DisplayString):
    """Custom type osw10buomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10buomFanCurrent_Type.__name__ = "DisplayString"
_Osw10buomFanCurrent_Object = MibTableColumn
osw10buomFanCurrent = _Osw10buomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 58),
    _Osw10buomFanCurrent_Type()
)
osw10buomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10buomFanCurrent.setStatus("optional")
_Osw10bmajorHighFanCurrent_Type = Float
_Osw10bmajorHighFanCurrent_Object = MibTableColumn
osw10bmajorHighFanCurrent = _Osw10bmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 59),
    _Osw10bmajorHighFanCurrent_Type()
)
osw10bmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorHighFanCurrent.setStatus("mandatory")
_Osw10bmajorLowFanCurrent_Type = Float
_Osw10bmajorLowFanCurrent_Object = MibTableColumn
osw10bmajorLowFanCurrent = _Osw10bmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 60),
    _Osw10bmajorLowFanCurrent_Type()
)
osw10bmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmajorLowFanCurrent.setStatus("mandatory")
_Osw10bminorHighFanCurrent_Type = Float
_Osw10bminorHighFanCurrent_Object = MibTableColumn
osw10bminorHighFanCurrent = _Osw10bminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 61),
    _Osw10bminorHighFanCurrent_Type()
)
osw10bminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorHighFanCurrent.setStatus("mandatory")
_Osw10bminorLowFanCurrent_Type = Float
_Osw10bminorLowFanCurrent_Object = MibTableColumn
osw10bminorLowFanCurrent = _Osw10bminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 62),
    _Osw10bminorLowFanCurrent_Type()
)
osw10bminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminorLowFanCurrent.setStatus("mandatory")
_Osw10bcurrentValueFanCurrent_Type = Float
_Osw10bcurrentValueFanCurrent_Object = MibTableColumn
osw10bcurrentValueFanCurrent = _Osw10bcurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 63),
    _Osw10bcurrentValueFanCurrent_Type()
)
osw10bcurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bcurrentValueFanCurrent.setStatus("mandatory")


class _Osw10bstateFlagFanCurrent_Type(Integer32):
    """Custom type osw10bstateFlagFanCurrent based on Integer32"""
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


_Osw10bstateFlagFanCurrent_Type.__name__ = "Integer32"
_Osw10bstateFlagFanCurrent_Object = MibTableColumn
osw10bstateFlagFanCurrent = _Osw10bstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 64),
    _Osw10bstateFlagFanCurrent_Type()
)
osw10bstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateFlagFanCurrent.setStatus("mandatory")
_Osw10bminValueFanCurrent_Type = Float
_Osw10bminValueFanCurrent_Object = MibTableColumn
osw10bminValueFanCurrent = _Osw10bminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 65),
    _Osw10bminValueFanCurrent_Type()
)
osw10bminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bminValueFanCurrent.setStatus("mandatory")
_Osw10bmaxValueFanCurrent_Type = Float
_Osw10bmaxValueFanCurrent_Object = MibTableColumn
osw10bmaxValueFanCurrent = _Osw10bmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 66),
    _Osw10bmaxValueFanCurrent_Type()
)
osw10bmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bmaxValueFanCurrent.setStatus("mandatory")


class _Osw10balarmStateFanCurrent_Type(Integer32):
    """Custom type osw10balarmStateFanCurrent based on Integer32"""
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


_Osw10balarmStateFanCurrent_Type.__name__ = "Integer32"
_Osw10balarmStateFanCurrent_Object = MibTableColumn
osw10balarmStateFanCurrent = _Osw10balarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 2, 1, 67),
    _Osw10balarmStateFanCurrent_Type()
)
osw10balarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10balarmStateFanCurrent.setStatus("mandatory")
_Gx2Osw10bDigitalTable_Object = MibTable
gx2Osw10bDigitalTable = _Gx2Osw10bDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3)
)
if mibBuilder.loadTexts:
    gx2Osw10bDigitalTable.setStatus("mandatory")
_Gx2Osw10bDigitalEntry_Object = MibTableRow
gx2Osw10bDigitalEntry = _Gx2Osw10bDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2)
)
gx2Osw10bDigitalEntry.setIndexNames(
    (0, "OMNI-gx2OSW10B-MIB", "gx2Osw10bDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Osw10bDigitalEntry.setStatus("mandatory")


class _Gx2Osw10bDigitalTableIndex_Type(Integer32):
    """Custom type gx2Osw10bDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Osw10bDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Osw10bDigitalTableIndex_Object = MibTableColumn
gx2Osw10bDigitalTableIndex = _Gx2Osw10bDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 1),
    _Gx2Osw10bDigitalTableIndex_Type()
)
gx2Osw10bDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Osw10bDigitalTableIndex.setStatus("mandatory")


class _Osw10blabelSwitchControl_Type(DisplayString):
    """Custom type osw10blabelSwitchControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelSwitchControl_Type.__name__ = "DisplayString"
_Osw10blabelSwitchControl_Object = MibTableColumn
osw10blabelSwitchControl = _Osw10blabelSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 2),
    _Osw10blabelSwitchControl_Type()
)
osw10blabelSwitchControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelSwitchControl.setStatus("optional")


class _Osw10benumSwitchControl_Type(DisplayString):
    """Custom type osw10benumSwitchControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10benumSwitchControl_Type.__name__ = "DisplayString"
_Osw10benumSwitchControl_Object = MibTableColumn
osw10benumSwitchControl = _Osw10benumSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 3),
    _Osw10benumSwitchControl_Type()
)
osw10benumSwitchControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10benumSwitchControl.setStatus("optional")


class _Osw10bvalueSwitchControl_Type(Integer32):
    """Custom type osw10bvalueSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossover", 2),
          ("through", 1))
    )


_Osw10bvalueSwitchControl_Type.__name__ = "Integer32"
_Osw10bvalueSwitchControl_Object = MibTableColumn
osw10bvalueSwitchControl = _Osw10bvalueSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 4),
    _Osw10bvalueSwitchControl_Type()
)
osw10bvalueSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bvalueSwitchControl.setStatus("mandatory")


class _Osw10bstateflagSwitchControl_Type(Integer32):
    """Custom type osw10bstateflagSwitchControl based on Integer32"""
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


_Osw10bstateflagSwitchControl_Type.__name__ = "Integer32"
_Osw10bstateflagSwitchControl_Object = MibTableColumn
osw10bstateflagSwitchControl = _Osw10bstateflagSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 5),
    _Osw10bstateflagSwitchControl_Type()
)
osw10bstateflagSwitchControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagSwitchControl.setStatus("mandatory")


class _Osw10blabelSwitchMode_Type(DisplayString):
    """Custom type osw10blabelSwitchMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelSwitchMode_Type.__name__ = "DisplayString"
_Osw10blabelSwitchMode_Object = MibTableColumn
osw10blabelSwitchMode = _Osw10blabelSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 6),
    _Osw10blabelSwitchMode_Type()
)
osw10blabelSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelSwitchMode.setStatus("optional")


class _Osw10benumSwitchMode_Type(DisplayString):
    """Custom type osw10benumSwitchMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10benumSwitchMode_Type.__name__ = "DisplayString"
_Osw10benumSwitchMode_Object = MibTableColumn
osw10benumSwitchMode = _Osw10benumSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 7),
    _Osw10benumSwitchMode_Type()
)
osw10benumSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10benumSwitchMode.setStatus("optional")


class _Osw10bvalueSwitchMode_Type(Integer32):
    """Custom type osw10bvalueSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_Osw10bvalueSwitchMode_Type.__name__ = "Integer32"
_Osw10bvalueSwitchMode_Object = MibTableColumn
osw10bvalueSwitchMode = _Osw10bvalueSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 8),
    _Osw10bvalueSwitchMode_Type()
)
osw10bvalueSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bvalueSwitchMode.setStatus("mandatory")


class _Osw10bstateflagSwitchMode_Type(Integer32):
    """Custom type osw10bstateflagSwitchMode based on Integer32"""
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


_Osw10bstateflagSwitchMode_Type.__name__ = "Integer32"
_Osw10bstateflagSwitchMode_Object = MibTableColumn
osw10bstateflagSwitchMode = _Osw10bstateflagSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 9),
    _Osw10bstateflagSwitchMode_Type()
)
osw10bstateflagSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagSwitchMode.setStatus("mandatory")


class _Osw10blabelRevertMode_Type(DisplayString):
    """Custom type osw10blabelRevertMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelRevertMode_Type.__name__ = "DisplayString"
_Osw10blabelRevertMode_Object = MibTableColumn
osw10blabelRevertMode = _Osw10blabelRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 10),
    _Osw10blabelRevertMode_Type()
)
osw10blabelRevertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelRevertMode.setStatus("optional")


class _Osw10benumRevertMode_Type(DisplayString):
    """Custom type osw10benumRevertMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10benumRevertMode_Type.__name__ = "DisplayString"
_Osw10benumRevertMode_Object = MibTableColumn
osw10benumRevertMode = _Osw10benumRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 11),
    _Osw10benumRevertMode_Type()
)
osw10benumRevertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10benumRevertMode.setStatus("optional")


class _Osw10bvalueRevertMode_Type(Integer32):
    """Custom type osw10bvalueRevertMode based on Integer32"""
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


_Osw10bvalueRevertMode_Type.__name__ = "Integer32"
_Osw10bvalueRevertMode_Object = MibTableColumn
osw10bvalueRevertMode = _Osw10bvalueRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 12),
    _Osw10bvalueRevertMode_Type()
)
osw10bvalueRevertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bvalueRevertMode.setStatus("mandatory")


class _Osw10bstateflagRevertMode_Type(Integer32):
    """Custom type osw10bstateflagRevertMode based on Integer32"""
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


_Osw10bstateflagRevertMode_Type.__name__ = "Integer32"
_Osw10bstateflagRevertMode_Object = MibTableColumn
osw10bstateflagRevertMode = _Osw10bstateflagRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 13),
    _Osw10bstateflagRevertMode_Type()
)
osw10bstateflagRevertMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagRevertMode.setStatus("mandatory")


class _Osw10blabelRevertTime_Type(DisplayString):
    """Custom type osw10blabelRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelRevertTime_Type.__name__ = "DisplayString"
_Osw10blabelRevertTime_Object = MibTableColumn
osw10blabelRevertTime = _Osw10blabelRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 14),
    _Osw10blabelRevertTime_Type()
)
osw10blabelRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelRevertTime.setStatus("optional")


class _Osw10benumRevertTime_Type(DisplayString):
    """Custom type osw10benumRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10benumRevertTime_Type.__name__ = "DisplayString"
_Osw10benumRevertTime_Object = MibTableColumn
osw10benumRevertTime = _Osw10benumRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 15),
    _Osw10benumRevertTime_Type()
)
osw10benumRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10benumRevertTime.setStatus("optional")


class _Osw10bvalueRevertTime_Type(Integer32):
    """Custom type osw10bvalueRevertTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sixhundredsec", 3),
          ("sixtysec", 2),
          ("tensec", 1))
    )


_Osw10bvalueRevertTime_Type.__name__ = "Integer32"
_Osw10bvalueRevertTime_Object = MibTableColumn
osw10bvalueRevertTime = _Osw10bvalueRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 16),
    _Osw10bvalueRevertTime_Type()
)
osw10bvalueRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bvalueRevertTime.setStatus("mandatory")


class _Osw10bstateflagRevertTime_Type(Integer32):
    """Custom type osw10bstateflagRevertTime based on Integer32"""
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


_Osw10bstateflagRevertTime_Type.__name__ = "Integer32"
_Osw10bstateflagRevertTime_Object = MibTableColumn
osw10bstateflagRevertTime = _Osw10bstateflagRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 17),
    _Osw10bstateflagRevertTime_Type()
)
osw10bstateflagRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagRevertTime.setStatus("mandatory")


class _Osw10blabelWavelength_Type(DisplayString):
    """Custom type osw10blabelWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelWavelength_Type.__name__ = "DisplayString"
_Osw10blabelWavelength_Object = MibTableColumn
osw10blabelWavelength = _Osw10blabelWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 18),
    _Osw10blabelWavelength_Type()
)
osw10blabelWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelWavelength.setStatus("optional")


class _Osw10benumWavelength_Type(DisplayString):
    """Custom type osw10benumWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10benumWavelength_Type.__name__ = "DisplayString"
_Osw10benumWavelength_Object = MibTableColumn
osw10benumWavelength = _Osw10benumWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 19),
    _Osw10benumWavelength_Type()
)
osw10benumWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10benumWavelength.setStatus("optional")


class _Osw10bvalueWavelength_Type(Integer32):
    """Custom type osw10bvalueWavelength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenfiftynnm", 2),
          ("thirteentennm", 1))
    )


_Osw10bvalueWavelength_Type.__name__ = "Integer32"
_Osw10bvalueWavelength_Object = MibTableColumn
osw10bvalueWavelength = _Osw10bvalueWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 20),
    _Osw10bvalueWavelength_Type()
)
osw10bvalueWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bvalueWavelength.setStatus("mandatory")


class _Osw10bstateflagWavelength_Type(Integer32):
    """Custom type osw10bstateflagWavelength based on Integer32"""
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


_Osw10bstateflagWavelength_Type.__name__ = "Integer32"
_Osw10bstateflagWavelength_Object = MibTableColumn
osw10bstateflagWavelength = _Osw10bstateflagWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 21),
    _Osw10bstateflagWavelength_Type()
)
osw10bstateflagWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagWavelength.setStatus("mandatory")


class _Osw10blabelSwitchMonitor_Type(DisplayString):
    """Custom type osw10blabelSwitchMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelSwitchMonitor_Type.__name__ = "DisplayString"
_Osw10blabelSwitchMonitor_Object = MibTableColumn
osw10blabelSwitchMonitor = _Osw10blabelSwitchMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 22),
    _Osw10blabelSwitchMonitor_Type()
)
osw10blabelSwitchMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelSwitchMonitor.setStatus("optional")


class _Osw10benumSwitchMonitor_Type(DisplayString):
    """Custom type osw10benumSwitchMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10benumSwitchMonitor_Type.__name__ = "DisplayString"
_Osw10benumSwitchMonitor_Object = MibTableColumn
osw10benumSwitchMonitor = _Osw10benumSwitchMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 23),
    _Osw10benumSwitchMonitor_Type()
)
osw10benumSwitchMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10benumSwitchMonitor.setStatus("optional")


class _Osw10bvalueSwitchMonitor_Type(Integer32):
    """Custom type osw10bvalueSwitchMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossover", 2),
          ("through", 1))
    )


_Osw10bvalueSwitchMonitor_Type.__name__ = "Integer32"
_Osw10bvalueSwitchMonitor_Object = MibTableColumn
osw10bvalueSwitchMonitor = _Osw10bvalueSwitchMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 24),
    _Osw10bvalueSwitchMonitor_Type()
)
osw10bvalueSwitchMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvalueSwitchMonitor.setStatus("mandatory")


class _Osw10bstateflagSwitchMonitor_Type(Integer32):
    """Custom type osw10bstateflagSwitchMonitor based on Integer32"""
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


_Osw10bstateflagSwitchMonitor_Type.__name__ = "Integer32"
_Osw10bstateflagSwitchMonitor_Object = MibTableColumn
osw10bstateflagSwitchMonitor = _Osw10bstateflagSwitchMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 25),
    _Osw10bstateflagSwitchMonitor_Type()
)
osw10bstateflagSwitchMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagSwitchMonitor.setStatus("mandatory")


class _Osw10blabelOperationMode_Type(DisplayString):
    """Custom type osw10blabelOperationMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelOperationMode_Type.__name__ = "DisplayString"
_Osw10blabelOperationMode_Object = MibTableColumn
osw10blabelOperationMode = _Osw10blabelOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 26),
    _Osw10blabelOperationMode_Type()
)
osw10blabelOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelOperationMode.setStatus("optional")


class _Osw10benumOperationMode_Type(DisplayString):
    """Custom type osw10benumOperationMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10benumOperationMode_Type.__name__ = "DisplayString"
_Osw10benumOperationMode_Object = MibTableColumn
osw10benumOperationMode = _Osw10benumOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 27),
    _Osw10benumOperationMode_Type()
)
osw10benumOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10benumOperationMode.setStatus("optional")


class _Osw10bvalueOperationMode_Type(Integer32):
    """Custom type osw10bvalueOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode1x2", 2),
          ("mode2x1", 1),
          ("mode2x2", 3))
    )


_Osw10bvalueOperationMode_Type.__name__ = "Integer32"
_Osw10bvalueOperationMode_Object = MibTableColumn
osw10bvalueOperationMode = _Osw10bvalueOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 28),
    _Osw10bvalueOperationMode_Type()
)
osw10bvalueOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bvalueOperationMode.setStatus("mandatory")


class _Osw10bstateflagOperationMode_Type(Integer32):
    """Custom type osw10bstateflagOperationMode based on Integer32"""
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


_Osw10bstateflagOperationMode_Type.__name__ = "Integer32"
_Osw10bstateflagOperationMode_Object = MibTableColumn
osw10bstateflagOperationMode = _Osw10bstateflagOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 29),
    _Osw10bstateflagOperationMode_Type()
)
osw10bstateflagOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagOperationMode.setStatus("mandatory")


class _Osw10blabelFactoryDefault_Type(DisplayString):
    """Custom type osw10blabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelFactoryDefault_Type.__name__ = "DisplayString"
_Osw10blabelFactoryDefault_Object = MibTableColumn
osw10blabelFactoryDefault = _Osw10blabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 30),
    _Osw10blabelFactoryDefault_Type()
)
osw10blabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelFactoryDefault.setStatus("optional")


class _Osw10benumFactoryDefault_Type(DisplayString):
    """Custom type osw10benumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10benumFactoryDefault_Type.__name__ = "DisplayString"
_Osw10benumFactoryDefault_Object = MibTableColumn
osw10benumFactoryDefault = _Osw10benumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 31),
    _Osw10benumFactoryDefault_Type()
)
osw10benumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10benumFactoryDefault.setStatus("optional")


class _Osw10bvalueFactoryDefault_Type(Integer32):
    """Custom type osw10bvalueFactoryDefault based on Integer32"""
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


_Osw10bvalueFactoryDefault_Type.__name__ = "Integer32"
_Osw10bvalueFactoryDefault_Object = MibTableColumn
osw10bvalueFactoryDefault = _Osw10bvalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 32),
    _Osw10bvalueFactoryDefault_Type()
)
osw10bvalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osw10bvalueFactoryDefault.setStatus("mandatory")


class _Osw10bstateflagFactoryDefault_Type(Integer32):
    """Custom type osw10bstateflagFactoryDefault based on Integer32"""
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


_Osw10bstateflagFactoryDefault_Type.__name__ = "Integer32"
_Osw10bstateflagFactoryDefault_Object = MibTableColumn
osw10bstateflagFactoryDefault = _Osw10bstateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 3, 2, 33),
    _Osw10bstateflagFactoryDefault_Type()
)
osw10bstateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagFactoryDefault.setStatus("mandatory")
_Gx2Osw10bStatusTable_Object = MibTable
gx2Osw10bStatusTable = _Gx2Osw10bStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4)
)
if mibBuilder.loadTexts:
    gx2Osw10bStatusTable.setStatus("mandatory")
_Gx2Osw10bStatusEntry_Object = MibTableRow
gx2Osw10bStatusEntry = _Gx2Osw10bStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3)
)
gx2Osw10bStatusEntry.setIndexNames(
    (0, "OMNI-gx2OSW10B-MIB", "gx2Osw10bStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Osw10bStatusEntry.setStatus("mandatory")


class _Gx2Osw10bStatusTableIndex_Type(Integer32):
    """Custom type gx2Osw10bStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Osw10bStatusTableIndex_Type.__name__ = "Integer32"
_Gx2Osw10bStatusTableIndex_Object = MibTableColumn
gx2Osw10bStatusTableIndex = _Gx2Osw10bStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 1),
    _Gx2Osw10bStatusTableIndex_Type()
)
gx2Osw10bStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Osw10bStatusTableIndex.setStatus("mandatory")


class _Osw10blabelBoot_Type(DisplayString):
    """Custom type osw10blabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelBoot_Type.__name__ = "DisplayString"
_Osw10blabelBoot_Object = MibTableColumn
osw10blabelBoot = _Osw10blabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 2),
    _Osw10blabelBoot_Type()
)
osw10blabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelBoot.setStatus("optional")


class _Osw10bvalueBoot_Type(Integer32):
    """Custom type osw10bvalueBoot based on Integer32"""
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


_Osw10bvalueBoot_Type.__name__ = "Integer32"
_Osw10bvalueBoot_Object = MibTableColumn
osw10bvalueBoot = _Osw10bvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 3),
    _Osw10bvalueBoot_Type()
)
osw10bvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvalueBoot.setStatus("mandatory")


class _Osw10bstateflagBoot_Type(Integer32):
    """Custom type osw10bstateflagBoot based on Integer32"""
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


_Osw10bstateflagBoot_Type.__name__ = "Integer32"
_Osw10bstateflagBoot_Object = MibTableColumn
osw10bstateflagBoot = _Osw10bstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 4),
    _Osw10bstateflagBoot_Type()
)
osw10bstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagBoot.setStatus("mandatory")


class _Osw10blabelFlash_Type(DisplayString):
    """Custom type osw10blabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelFlash_Type.__name__ = "DisplayString"
_Osw10blabelFlash_Object = MibTableColumn
osw10blabelFlash = _Osw10blabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 5),
    _Osw10blabelFlash_Type()
)
osw10blabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelFlash.setStatus("optional")


class _Osw10bvalueFlash_Type(Integer32):
    """Custom type osw10bvalueFlash based on Integer32"""
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


_Osw10bvalueFlash_Type.__name__ = "Integer32"
_Osw10bvalueFlash_Object = MibTableColumn
osw10bvalueFlash = _Osw10bvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 6),
    _Osw10bvalueFlash_Type()
)
osw10bvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvalueFlash.setStatus("mandatory")


class _Osw10bstateflagFlash_Type(Integer32):
    """Custom type osw10bstateflagFlash based on Integer32"""
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


_Osw10bstateflagFlash_Type.__name__ = "Integer32"
_Osw10bstateflagFlash_Object = MibTableColumn
osw10bstateflagFlash = _Osw10bstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 7),
    _Osw10bstateflagFlash_Type()
)
osw10bstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagFlash.setStatus("mandatory")


class _Osw10blabelFactoryDataCRC_Type(DisplayString):
    """Custom type osw10blabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelFactoryDataCRC_Type.__name__ = "DisplayString"
_Osw10blabelFactoryDataCRC_Object = MibTableColumn
osw10blabelFactoryDataCRC = _Osw10blabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 8),
    _Osw10blabelFactoryDataCRC_Type()
)
osw10blabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelFactoryDataCRC.setStatus("optional")


class _Osw10bvalueFactoryDataCRC_Type(Integer32):
    """Custom type osw10bvalueFactoryDataCRC based on Integer32"""
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


_Osw10bvalueFactoryDataCRC_Type.__name__ = "Integer32"
_Osw10bvalueFactoryDataCRC_Object = MibTableColumn
osw10bvalueFactoryDataCRC = _Osw10bvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 9),
    _Osw10bvalueFactoryDataCRC_Type()
)
osw10bvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvalueFactoryDataCRC.setStatus("mandatory")


class _Osw10bstateflagFactoryDataCRC_Type(Integer32):
    """Custom type osw10bstateflagFactoryDataCRC based on Integer32"""
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


_Osw10bstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Osw10bstateflagFactoryDataCRC_Object = MibTableColumn
osw10bstateflagFactoryDataCRC = _Osw10bstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 10),
    _Osw10bstateflagFactoryDataCRC_Type()
)
osw10bstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagFactoryDataCRC.setStatus("mandatory")


class _Osw10blabelCalibrateTableStatus_Type(DisplayString):
    """Custom type osw10blabelCalibrateTableStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelCalibrateTableStatus_Type.__name__ = "DisplayString"
_Osw10blabelCalibrateTableStatus_Object = MibTableColumn
osw10blabelCalibrateTableStatus = _Osw10blabelCalibrateTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 11),
    _Osw10blabelCalibrateTableStatus_Type()
)
osw10blabelCalibrateTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelCalibrateTableStatus.setStatus("optional")


class _Osw10bvalueCalibrateTableStatus_Type(Integer32):
    """Custom type osw10bvalueCalibrateTableStatus based on Integer32"""
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


_Osw10bvalueCalibrateTableStatus_Type.__name__ = "Integer32"
_Osw10bvalueCalibrateTableStatus_Object = MibTableColumn
osw10bvalueCalibrateTableStatus = _Osw10bvalueCalibrateTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 12),
    _Osw10bvalueCalibrateTableStatus_Type()
)
osw10bvalueCalibrateTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvalueCalibrateTableStatus.setStatus("mandatory")


class _Osw10bstateflagCalibrateTableStatus_Type(Integer32):
    """Custom type osw10bstateflagCalibrateTableStatus based on Integer32"""
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


_Osw10bstateflagCalibrateTableStatus_Type.__name__ = "Integer32"
_Osw10bstateflagCalibrateTableStatus_Object = MibTableColumn
osw10bstateflagCalibrateTableStatus = _Osw10bstateflagCalibrateTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 13),
    _Osw10bstateflagCalibrateTableStatus_Type()
)
osw10bstateflagCalibrateTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagCalibrateTableStatus.setStatus("mandatory")


class _Osw10blabelAlarmDataCrc_Type(DisplayString):
    """Custom type osw10blabelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelAlarmDataCrc_Type.__name__ = "DisplayString"
_Osw10blabelAlarmDataCrc_Object = MibTableColumn
osw10blabelAlarmDataCrc = _Osw10blabelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 14),
    _Osw10blabelAlarmDataCrc_Type()
)
osw10blabelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelAlarmDataCrc.setStatus("optional")


class _Osw10bvalueAlarmDataCrc_Type(Integer32):
    """Custom type osw10bvalueAlarmDataCrc based on Integer32"""
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


_Osw10bvalueAlarmDataCrc_Type.__name__ = "Integer32"
_Osw10bvalueAlarmDataCrc_Object = MibTableColumn
osw10bvalueAlarmDataCrc = _Osw10bvalueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 15),
    _Osw10bvalueAlarmDataCrc_Type()
)
osw10bvalueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvalueAlarmDataCrc.setStatus("mandatory")


class _Osw10bstateflagAlarmDataCrc_Type(Integer32):
    """Custom type osw10bstateflagAlarmDataCrc based on Integer32"""
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


_Osw10bstateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Osw10bstateflagAlarmDataCrc_Object = MibTableColumn
osw10bstateflagAlarmDataCrc = _Osw10bstateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 16),
    _Osw10bstateflagAlarmDataCrc_Type()
)
osw10bstateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagAlarmDataCrc.setStatus("mandatory")


class _Osw10blabelInputStatus_Type(DisplayString):
    """Custom type osw10blabelInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelInputStatus_Type.__name__ = "DisplayString"
_Osw10blabelInputStatus_Object = MibTableColumn
osw10blabelInputStatus = _Osw10blabelInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 17),
    _Osw10blabelInputStatus_Type()
)
osw10blabelInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelInputStatus.setStatus("obsolete")


class _Osw10bvalueInputStatus_Type(Integer32):
    """Custom type osw10bvalueInputStatus based on Integer32"""
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


_Osw10bvalueInputStatus_Type.__name__ = "Integer32"
_Osw10bvalueInputStatus_Object = MibTableColumn
osw10bvalueInputStatus = _Osw10bvalueInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 18),
    _Osw10bvalueInputStatus_Type()
)
osw10bvalueInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvalueInputStatus.setStatus("obsolete")


class _Osw10bstateflagInputStatus_Type(Integer32):
    """Custom type osw10bstateflagInputStatus based on Integer32"""
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


_Osw10bstateflagInputStatus_Type.__name__ = "Integer32"
_Osw10bstateflagInputStatus_Object = MibTableColumn
osw10bstateflagInputStatus = _Osw10bstateflagInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 19),
    _Osw10bstateflagInputStatus_Type()
)
osw10bstateflagInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagInputStatus.setStatus("obsolete")


class _Osw10blabelPriActiveStatus_Type(DisplayString):
    """Custom type osw10blabelPriActiveStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelPriActiveStatus_Type.__name__ = "DisplayString"
_Osw10blabelPriActiveStatus_Object = MibTableColumn
osw10blabelPriActiveStatus = _Osw10blabelPriActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 20),
    _Osw10blabelPriActiveStatus_Type()
)
osw10blabelPriActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelPriActiveStatus.setStatus("optional")


class _Osw10bvaluePriActiveStatus_Type(Integer32):
    """Custom type osw10bvaluePriActiveStatus based on Integer32"""
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


_Osw10bvaluePriActiveStatus_Type.__name__ = "Integer32"
_Osw10bvaluePriActiveStatus_Object = MibTableColumn
osw10bvaluePriActiveStatus = _Osw10bvaluePriActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 21),
    _Osw10bvaluePriActiveStatus_Type()
)
osw10bvaluePriActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvaluePriActiveStatus.setStatus("mandatory")


class _Osw10bstateflagPriActiveStatus_Type(Integer32):
    """Custom type osw10bstateflagPriActiveStatus based on Integer32"""
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


_Osw10bstateflagPriActiveStatus_Type.__name__ = "Integer32"
_Osw10bstateflagPriActiveStatus_Object = MibTableColumn
osw10bstateflagPriActiveStatus = _Osw10bstateflagPriActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 22),
    _Osw10bstateflagPriActiveStatus_Type()
)
osw10bstateflagPriActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagPriActiveStatus.setStatus("mandatory")


class _Osw10blabelHardwareErr_Type(DisplayString):
    """Custom type osw10blabelHardwareErr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelHardwareErr_Type.__name__ = "DisplayString"
_Osw10blabelHardwareErr_Object = MibTableColumn
osw10blabelHardwareErr = _Osw10blabelHardwareErr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 23),
    _Osw10blabelHardwareErr_Type()
)
osw10blabelHardwareErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelHardwareErr.setStatus("optional")


class _Osw10bvalueHardwareErr_Type(Integer32):
    """Custom type osw10bvalueHardwareErr based on Integer32"""
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


_Osw10bvalueHardwareErr_Type.__name__ = "Integer32"
_Osw10bvalueHardwareErr_Object = MibTableColumn
osw10bvalueHardwareErr = _Osw10bvalueHardwareErr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 24),
    _Osw10bvalueHardwareErr_Type()
)
osw10bvalueHardwareErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvalueHardwareErr.setStatus("mandatory")


class _Osw10bstateflagHardwareErr_Type(Integer32):
    """Custom type osw10bstateflagHardwareErr based on Integer32"""
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


_Osw10bstateflagHardwareErr_Type.__name__ = "Integer32"
_Osw10bstateflagHardwareErr_Object = MibTableColumn
osw10bstateflagHardwareErr = _Osw10bstateflagHardwareErr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 25),
    _Osw10bstateflagHardwareErr_Type()
)
osw10bstateflagHardwareErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagHardwareErr.setStatus("mandatory")


class _Osw10blabelPriThresholdStatus_Type(DisplayString):
    """Custom type osw10blabelPriThresholdStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelPriThresholdStatus_Type.__name__ = "DisplayString"
_Osw10blabelPriThresholdStatus_Object = MibTableColumn
osw10blabelPriThresholdStatus = _Osw10blabelPriThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 26),
    _Osw10blabelPriThresholdStatus_Type()
)
osw10blabelPriThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelPriThresholdStatus.setStatus("optional")


class _Osw10bvaluePriThresholdStatus_Type(Integer32):
    """Custom type osw10bvaluePriThresholdStatus based on Integer32"""
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


_Osw10bvaluePriThresholdStatus_Type.__name__ = "Integer32"
_Osw10bvaluePriThresholdStatus_Object = MibTableColumn
osw10bvaluePriThresholdStatus = _Osw10bvaluePriThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 27),
    _Osw10bvaluePriThresholdStatus_Type()
)
osw10bvaluePriThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvaluePriThresholdStatus.setStatus("mandatory")


class _Osw10bstateflagPriThresholdStatus_Type(Integer32):
    """Custom type osw10bstateflagPriThresholdStatus based on Integer32"""
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


_Osw10bstateflagPriThresholdStatus_Type.__name__ = "Integer32"
_Osw10bstateflagPriThresholdStatus_Object = MibTableColumn
osw10bstateflagPriThresholdStatus = _Osw10bstateflagPriThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 28),
    _Osw10bstateflagPriThresholdStatus_Type()
)
osw10bstateflagPriThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagPriThresholdStatus.setStatus("mandatory")


class _Osw10blabelSecThresholdStatus_Type(DisplayString):
    """Custom type osw10blabelSecThresholdStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10blabelSecThresholdStatus_Type.__name__ = "DisplayString"
_Osw10blabelSecThresholdStatus_Object = MibTableColumn
osw10blabelSecThresholdStatus = _Osw10blabelSecThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 29),
    _Osw10blabelSecThresholdStatus_Type()
)
osw10blabelSecThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10blabelSecThresholdStatus.setStatus("optional")


class _Osw10bvalueSecThresholdStatus_Type(Integer32):
    """Custom type osw10bvalueSecThresholdStatus based on Integer32"""
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


_Osw10bvalueSecThresholdStatus_Type.__name__ = "Integer32"
_Osw10bvalueSecThresholdStatus_Object = MibTableColumn
osw10bvalueSecThresholdStatus = _Osw10bvalueSecThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 30),
    _Osw10bvalueSecThresholdStatus_Type()
)
osw10bvalueSecThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bvalueSecThresholdStatus.setStatus("mandatory")


class _Osw10bstateflagSecThresholdStatus_Type(Integer32):
    """Custom type osw10bstateflagSecThresholdStatus based on Integer32"""
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


_Osw10bstateflagSecThresholdStatus_Type.__name__ = "Integer32"
_Osw10bstateflagSecThresholdStatus_Object = MibTableColumn
osw10bstateflagSecThresholdStatus = _Osw10bstateflagSecThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 4, 3, 31),
    _Osw10bstateflagSecThresholdStatus_Type()
)
osw10bstateflagSecThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bstateflagSecThresholdStatus.setStatus("mandatory")
_Gx2Osw10bFactoryTable_Object = MibTable
gx2Osw10bFactoryTable = _Gx2Osw10bFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5)
)
if mibBuilder.loadTexts:
    gx2Osw10bFactoryTable.setStatus("mandatory")
_Gx2Osw10bFactoryEntry_Object = MibTableRow
gx2Osw10bFactoryEntry = _Gx2Osw10bFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4)
)
gx2Osw10bFactoryEntry.setIndexNames(
    (0, "OMNI-gx2OSW10B-MIB", "gx2Osw10bFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Osw10bFactoryEntry.setStatus("mandatory")


class _Gx2Osw10bFactoryTableIndex_Type(Integer32):
    """Custom type gx2Osw10bFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Osw10bFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Osw10bFactoryTableIndex_Object = MibTableColumn
gx2Osw10bFactoryTableIndex = _Gx2Osw10bFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 1),
    _Gx2Osw10bFactoryTableIndex_Type()
)
gx2Osw10bFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Osw10bFactoryTableIndex.setStatus("mandatory")
_Osw10bbootControlByte_Type = Integer32
_Osw10bbootControlByte_Object = MibTableColumn
osw10bbootControlByte = _Osw10bbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 2),
    _Osw10bbootControlByte_Type()
)
osw10bbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bbootControlByte.setStatus("mandatory")
_Osw10bbootStatusByte_Type = Integer32
_Osw10bbootStatusByte_Object = MibTableColumn
osw10bbootStatusByte = _Osw10bbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 3),
    _Osw10bbootStatusByte_Type()
)
osw10bbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bbootStatusByte.setStatus("mandatory")
_Osw10bbank1CRC_Type = Integer32
_Osw10bbank1CRC_Object = MibTableColumn
osw10bbank1CRC = _Osw10bbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 4),
    _Osw10bbank1CRC_Type()
)
osw10bbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bbank1CRC.setStatus("mandatory")
_Osw10bbank2CRC_Type = Integer32
_Osw10bbank2CRC_Object = MibTableColumn
osw10bbank2CRC = _Osw10bbank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 5),
    _Osw10bbank2CRC_Type()
)
osw10bbank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bbank2CRC.setStatus("mandatory")
_Osw10bprgEEPROMByte_Type = Integer32
_Osw10bprgEEPROMByte_Object = MibTableColumn
osw10bprgEEPROMByte = _Osw10bprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 6),
    _Osw10bprgEEPROMByte_Type()
)
osw10bprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bprgEEPROMByte.setStatus("mandatory")
_Osw10bfactoryCRC_Type = Integer32
_Osw10bfactoryCRC_Object = MibTableColumn
osw10bfactoryCRC = _Osw10bfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 7),
    _Osw10bfactoryCRC_Type()
)
osw10bfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bfactoryCRC.setStatus("mandatory")


class _Osw10bcalculateCRC_Type(Integer32):
    """Custom type osw10bcalculateCRC based on Integer32"""
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
          ("calTable", 2),
          ("factory", 1),
          ("na", 4))
    )


_Osw10bcalculateCRC_Type.__name__ = "Integer32"
_Osw10bcalculateCRC_Object = MibTableColumn
osw10bcalculateCRC = _Osw10bcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 8),
    _Osw10bcalculateCRC_Type()
)
osw10bcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bcalculateCRC.setStatus("mandatory")
_Osw10bhourMeter_Type = Integer32
_Osw10bhourMeter_Object = MibTableColumn
osw10bhourMeter = _Osw10bhourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 9),
    _Osw10bhourMeter_Type()
)
osw10bhourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bhourMeter.setStatus("mandatory")
_Osw10bflashPrgCntA_Type = Integer32
_Osw10bflashPrgCntA_Object = MibTableColumn
osw10bflashPrgCntA = _Osw10bflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 10),
    _Osw10bflashPrgCntA_Type()
)
osw10bflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bflashPrgCntA.setStatus("mandatory")
_Osw10bflashPrgCntB_Type = Integer32
_Osw10bflashPrgCntB_Object = MibTableColumn
osw10bflashPrgCntB = _Osw10bflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 11),
    _Osw10bflashPrgCntB_Type()
)
osw10bflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bflashPrgCntB.setStatus("mandatory")


class _Osw10bflashBankARev_Type(DisplayString):
    """Custom type osw10bflashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10bflashBankARev_Type.__name__ = "DisplayString"
_Osw10bflashBankARev_Object = MibTableColumn
osw10bflashBankARev = _Osw10bflashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 12),
    _Osw10bflashBankARev_Type()
)
osw10bflashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bflashBankARev.setStatus("mandatory")


class _Osw10bflashBankBRev_Type(DisplayString):
    """Custom type osw10bflashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Osw10bflashBankBRev_Type.__name__ = "DisplayString"
_Osw10bflashBankBRev_Object = MibTableColumn
osw10bflashBankBRev = _Osw10bflashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 5, 4, 13),
    _Osw10bflashBankBRev_Type()
)
osw10bflashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osw10bflashBankBRev.setStatus("mandatory")
_Gx2Osw10bHoldTimeTable_Object = MibTable
gx2Osw10bHoldTimeTable = _Gx2Osw10bHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 6)
)
if mibBuilder.loadTexts:
    gx2Osw10bHoldTimeTable.setStatus("mandatory")
_Gx2Osw10bHoldTimeEntry_Object = MibTableRow
gx2Osw10bHoldTimeEntry = _Gx2Osw10bHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 6, 5)
)
gx2Osw10bHoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2OSW10B-MIB", "rxgx2Osw10bHoldTimeTableIndex"),
    (0, "OMNI-gx2OSW10B-MIB", "rxgx2Osw10bHoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Osw10bHoldTimeEntry.setStatus("mandatory")


class _Rxgx2Osw10bHoldTimeTableIndex_Type(Integer32):
    """Custom type rxgx2Osw10bHoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Osw10bHoldTimeTableIndex_Type.__name__ = "Integer32"
_Rxgx2Osw10bHoldTimeTableIndex_Object = MibTableColumn
rxgx2Osw10bHoldTimeTableIndex = _Rxgx2Osw10bHoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 6, 5, 1),
    _Rxgx2Osw10bHoldTimeTableIndex_Type()
)
rxgx2Osw10bHoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Osw10bHoldTimeTableIndex.setStatus("mandatory")


class _Rxgx2Osw10bHoldTimeSpecIndex_Type(Integer32):
    """Custom type rxgx2Osw10bHoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Osw10bHoldTimeSpecIndex_Type.__name__ = "Integer32"
_Rxgx2Osw10bHoldTimeSpecIndex_Object = MibTableColumn
rxgx2Osw10bHoldTimeSpecIndex = _Rxgx2Osw10bHoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 6, 5, 2),
    _Rxgx2Osw10bHoldTimeSpecIndex_Type()
)
rxgx2Osw10bHoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Osw10bHoldTimeSpecIndex.setStatus("mandatory")
_Rxgx2Osw10bHoldTimeData_Type = Integer32
_Rxgx2Osw10bHoldTimeData_Object = MibTableColumn
rxgx2Osw10bHoldTimeData = _Rxgx2Osw10bHoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 6, 5, 3),
    _Rxgx2Osw10bHoldTimeData_Type()
)
rxgx2Osw10bHoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxgx2Osw10bHoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapOSW10BConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 1)
)
trapOSW10BConfigChangeInteger.setObjects(
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
    trapOSW10BConfigChangeInteger.setStatus(
        ""
    )

trapOSW10BConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 2)
)
trapOSW10BConfigChangeDisplayString.setObjects(
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
    trapOSW10BConfigChangeDisplayString.setStatus(
        ""
    )

trapOSW10BOpticalInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 3)
)
trapOSW10BOpticalInputAlarm.setObjects(
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
    trapOSW10BOpticalInputAlarm.setStatus(
        ""
    )

trapOSW10BFanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 4)
)
trapOSW10BFanCurrentAlarm.setObjects(
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
    trapOSW10BFanCurrentAlarm.setStatus(
        ""
    )

trapOSW10BModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 5)
)
trapOSW10BModuleTempAlarm.setObjects(
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
    trapOSW10BModuleTempAlarm.setStatus(
        ""
    )

trapOSW10BFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 6)
)
trapOSW10BFlashAlarm.setObjects(
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
    trapOSW10BFlashAlarm.setStatus(
        ""
    )

trapOSW10BBankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 7)
)
trapOSW10BBankBootAlarm.setObjects(
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
    trapOSW10BBankBootAlarm.setStatus(
        ""
    )

trapOSW10BCaliDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 8)
)
trapOSW10BCaliDataCRCAlarm.setObjects(
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
    trapOSW10BCaliDataCRCAlarm.setStatus(
        ""
    )

trapOSW10BFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 9)
)
trapOSW10BFactoryDataCRCAlarm.setObjects(
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
    trapOSW10BFactoryDataCRCAlarm.setStatus(
        ""
    )

trapOSW10BAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 10)
)
trapOSW10BAlarmDataCRCAlarm.setObjects(
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
    trapOSW10BAlarmDataCRCAlarm.setStatus(
        ""
    )

trapOSW10BInputSwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 11)
)
trapOSW10BInputSwitchedAlarm.setObjects(
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
    trapOSW10BInputSwitchedAlarm.setStatus(
        ""
    )

trapOSW10BResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 12)
)
trapOSW10BResetFactoryDefaultAlarm.setObjects(
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
    trapOSW10BResetFactoryDefaultAlarm.setStatus(
        ""
    )

trapOSW10BSecondaryInputActiveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 13)
)
trapOSW10BSecondaryInputActiveAlarm.setObjects(
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
    trapOSW10BSecondaryInputActiveAlarm.setStatus(
        ""
    )

trapOSW10BPriOpticInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 14)
)
trapOSW10BPriOpticInputAlarm.setObjects(
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
    trapOSW10BPriOpticInputAlarm.setStatus(
        ""
    )

trapOSW10BSecOpticInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 15)
)
trapOSW10BSecOpticInputAlarm.setObjects(
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
    trapOSW10BSecOpticInputAlarm.setStatus(
        ""
    )

trapOSW10BHardwareErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15, 0, 16)
)
trapOSW10BHardwareErrorAlarm.setObjects(
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
    trapOSW10BHardwareErrorAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2OSW10B-MIB",
    **{"Float": Float,
       "trapOSW10BConfigChangeInteger": trapOSW10BConfigChangeInteger,
       "trapOSW10BConfigChangeDisplayString": trapOSW10BConfigChangeDisplayString,
       "trapOSW10BOpticalInputAlarm": trapOSW10BOpticalInputAlarm,
       "trapOSW10BFanCurrentAlarm": trapOSW10BFanCurrentAlarm,
       "trapOSW10BModuleTempAlarm": trapOSW10BModuleTempAlarm,
       "trapOSW10BFlashAlarm": trapOSW10BFlashAlarm,
       "trapOSW10BBankBootAlarm": trapOSW10BBankBootAlarm,
       "trapOSW10BCaliDataCRCAlarm": trapOSW10BCaliDataCRCAlarm,
       "trapOSW10BFactoryDataCRCAlarm": trapOSW10BFactoryDataCRCAlarm,
       "trapOSW10BAlarmDataCRCAlarm": trapOSW10BAlarmDataCRCAlarm,
       "trapOSW10BInputSwitchedAlarm": trapOSW10BInputSwitchedAlarm,
       "trapOSW10BResetFactoryDefaultAlarm": trapOSW10BResetFactoryDefaultAlarm,
       "trapOSW10BSecondaryInputActiveAlarm": trapOSW10BSecondaryInputActiveAlarm,
       "trapOSW10BPriOpticInputAlarm": trapOSW10BPriOpticInputAlarm,
       "trapOSW10BSecOpticInputAlarm": trapOSW10BSecOpticInputAlarm,
       "trapOSW10BHardwareErrorAlarm": trapOSW10BHardwareErrorAlarm,
       "gx2Osw10bDescriptor": gx2Osw10bDescriptor,
       "gx2Osw10bAnalogTable": gx2Osw10bAnalogTable,
       "gx2Osw10bAnalogEntry": gx2Osw10bAnalogEntry,
       "gx2Osw10bAnalogTableIndex": gx2Osw10bAnalogTableIndex,
       "osw10blabelPriOpticalInputLevel": osw10blabelPriOpticalInputLevel,
       "osw10buomPriOpticalInputLevel": osw10buomPriOpticalInputLevel,
       "osw10bmajorHighPriOpticalInputLevel": osw10bmajorHighPriOpticalInputLevel,
       "osw10bmajorLowPriOpticalInputLevel": osw10bmajorLowPriOpticalInputLevel,
       "osw10bminorHighPriOpticalInputLevel": osw10bminorHighPriOpticalInputLevel,
       "osw10bminorLowPriOpticalInputLevel": osw10bminorLowPriOpticalInputLevel,
       "osw10bcurrentValuePriOpticalInputLevel": osw10bcurrentValuePriOpticalInputLevel,
       "osw10bstateFlagPriOpticalInputLevel": osw10bstateFlagPriOpticalInputLevel,
       "osw10bminValuePriOpticalInputLevel": osw10bminValuePriOpticalInputLevel,
       "osw10bmaxValuePriOpticalInputLevel": osw10bmaxValuePriOpticalInputLevel,
       "osw10balarmStatePriOpticalInputLevel": osw10balarmStatePriOpticalInputLevel,
       "osw10blabelSecOpticalInputLevel": osw10blabelSecOpticalInputLevel,
       "osw10buomSecOpticalInputLevel": osw10buomSecOpticalInputLevel,
       "osw10bmajorHighSecOpticalInputLevel": osw10bmajorHighSecOpticalInputLevel,
       "osw10bmajorLowSecOpticalInputLevel": osw10bmajorLowSecOpticalInputLevel,
       "osw10bminorHighSecOpticalInputLevel": osw10bminorHighSecOpticalInputLevel,
       "osw10bminorLowSecOpticalInputLevel": osw10bminorLowSecOpticalInputLevel,
       "osw10bcurrentValueSecOpticalInputLevel": osw10bcurrentValueSecOpticalInputLevel,
       "osw10bstateFlagSecOpticalInputLevel": osw10bstateFlagSecOpticalInputLevel,
       "osw10bminValueSecOpticalInputLevel": osw10bminValueSecOpticalInputLevel,
       "osw10bmaxValueSecOpticalInputLevel": osw10bmaxValueSecOpticalInputLevel,
       "osw10balarmStateSecOpticalInputLevel": osw10balarmStateSecOpticalInputLevel,
       "osw10blabelPriOpticalThreshold": osw10blabelPriOpticalThreshold,
       "osw10buomPriOpticalThreshold": osw10buomPriOpticalThreshold,
       "osw10bmajorHighPriOpticalThreshold": osw10bmajorHighPriOpticalThreshold,
       "osw10bmajorLowPriOpticalThreshold": osw10bmajorLowPriOpticalThreshold,
       "osw10bminorHighPriOpticalThreshold": osw10bminorHighPriOpticalThreshold,
       "osw10bminorLowPriOpticalThreshold": osw10bminorLowPriOpticalThreshold,
       "osw10bcurrentValuePriOpticalThreshold": osw10bcurrentValuePriOpticalThreshold,
       "osw10bstateFlagPriOpticalThreshold": osw10bstateFlagPriOpticalThreshold,
       "osw10bminValuePriOpticalThreshold": osw10bminValuePriOpticalThreshold,
       "osw10bmaxValuePriOpticalThreshold": osw10bmaxValuePriOpticalThreshold,
       "osw10balarmStatePriOpticalThreshold": osw10balarmStatePriOpticalThreshold,
       "osw10blabelSecOpticalThreshold": osw10blabelSecOpticalThreshold,
       "osw10buomSecOpticalThreshold": osw10buomSecOpticalThreshold,
       "osw10bmajorHighSecOpticalThreshold": osw10bmajorHighSecOpticalThreshold,
       "osw10bmajorLowSecOpticalThreshold": osw10bmajorLowSecOpticalThreshold,
       "osw10bminorHighSecOpticalThreshold": osw10bminorHighSecOpticalThreshold,
       "osw10bminorLowSecOpticalThreshold": osw10bminorLowSecOpticalThreshold,
       "osw10bcurrentValueSecOpticalThreshold": osw10bcurrentValueSecOpticalThreshold,
       "osw10bstateFlagSecOpticalThreshold": osw10bstateFlagSecOpticalThreshold,
       "osw10bminValueSecOpticalThreshold": osw10bminValueSecOpticalThreshold,
       "osw10bmaxValueSecOpticalThreshold": osw10bmaxValueSecOpticalThreshold,
       "osw10balarmStateSecOpticalThreshold": osw10balarmStateSecOpticalThreshold,
       "osw10blabelModTemp": osw10blabelModTemp,
       "osw10buomModTemp": osw10buomModTemp,
       "osw10bmajorHighModTemp": osw10bmajorHighModTemp,
       "osw10bmajorLowModTemp": osw10bmajorLowModTemp,
       "osw10bminorHighModTemp": osw10bminorHighModTemp,
       "osw10bminorLowModTemp": osw10bminorLowModTemp,
       "osw10bcurrentValueModTemp": osw10bcurrentValueModTemp,
       "osw10bstateFlagModTemp": osw10bstateFlagModTemp,
       "osw10bminValueModTemp": osw10bminValueModTemp,
       "osw10bmaxValueModTemp": osw10bmaxValueModTemp,
       "osw10balarmStateModTemp": osw10balarmStateModTemp,
       "osw10blabelFanCurrent": osw10blabelFanCurrent,
       "osw10buomFanCurrent": osw10buomFanCurrent,
       "osw10bmajorHighFanCurrent": osw10bmajorHighFanCurrent,
       "osw10bmajorLowFanCurrent": osw10bmajorLowFanCurrent,
       "osw10bminorHighFanCurrent": osw10bminorHighFanCurrent,
       "osw10bminorLowFanCurrent": osw10bminorLowFanCurrent,
       "osw10bcurrentValueFanCurrent": osw10bcurrentValueFanCurrent,
       "osw10bstateFlagFanCurrent": osw10bstateFlagFanCurrent,
       "osw10bminValueFanCurrent": osw10bminValueFanCurrent,
       "osw10bmaxValueFanCurrent": osw10bmaxValueFanCurrent,
       "osw10balarmStateFanCurrent": osw10balarmStateFanCurrent,
       "gx2Osw10bDigitalTable": gx2Osw10bDigitalTable,
       "gx2Osw10bDigitalEntry": gx2Osw10bDigitalEntry,
       "gx2Osw10bDigitalTableIndex": gx2Osw10bDigitalTableIndex,
       "osw10blabelSwitchControl": osw10blabelSwitchControl,
       "osw10benumSwitchControl": osw10benumSwitchControl,
       "osw10bvalueSwitchControl": osw10bvalueSwitchControl,
       "osw10bstateflagSwitchControl": osw10bstateflagSwitchControl,
       "osw10blabelSwitchMode": osw10blabelSwitchMode,
       "osw10benumSwitchMode": osw10benumSwitchMode,
       "osw10bvalueSwitchMode": osw10bvalueSwitchMode,
       "osw10bstateflagSwitchMode": osw10bstateflagSwitchMode,
       "osw10blabelRevertMode": osw10blabelRevertMode,
       "osw10benumRevertMode": osw10benumRevertMode,
       "osw10bvalueRevertMode": osw10bvalueRevertMode,
       "osw10bstateflagRevertMode": osw10bstateflagRevertMode,
       "osw10blabelRevertTime": osw10blabelRevertTime,
       "osw10benumRevertTime": osw10benumRevertTime,
       "osw10bvalueRevertTime": osw10bvalueRevertTime,
       "osw10bstateflagRevertTime": osw10bstateflagRevertTime,
       "osw10blabelWavelength": osw10blabelWavelength,
       "osw10benumWavelength": osw10benumWavelength,
       "osw10bvalueWavelength": osw10bvalueWavelength,
       "osw10bstateflagWavelength": osw10bstateflagWavelength,
       "osw10blabelSwitchMonitor": osw10blabelSwitchMonitor,
       "osw10benumSwitchMonitor": osw10benumSwitchMonitor,
       "osw10bvalueSwitchMonitor": osw10bvalueSwitchMonitor,
       "osw10bstateflagSwitchMonitor": osw10bstateflagSwitchMonitor,
       "osw10blabelOperationMode": osw10blabelOperationMode,
       "osw10benumOperationMode": osw10benumOperationMode,
       "osw10bvalueOperationMode": osw10bvalueOperationMode,
       "osw10bstateflagOperationMode": osw10bstateflagOperationMode,
       "osw10blabelFactoryDefault": osw10blabelFactoryDefault,
       "osw10benumFactoryDefault": osw10benumFactoryDefault,
       "osw10bvalueFactoryDefault": osw10bvalueFactoryDefault,
       "osw10bstateflagFactoryDefault": osw10bstateflagFactoryDefault,
       "gx2Osw10bStatusTable": gx2Osw10bStatusTable,
       "gx2Osw10bStatusEntry": gx2Osw10bStatusEntry,
       "gx2Osw10bStatusTableIndex": gx2Osw10bStatusTableIndex,
       "osw10blabelBoot": osw10blabelBoot,
       "osw10bvalueBoot": osw10bvalueBoot,
       "osw10bstateflagBoot": osw10bstateflagBoot,
       "osw10blabelFlash": osw10blabelFlash,
       "osw10bvalueFlash": osw10bvalueFlash,
       "osw10bstateflagFlash": osw10bstateflagFlash,
       "osw10blabelFactoryDataCRC": osw10blabelFactoryDataCRC,
       "osw10bvalueFactoryDataCRC": osw10bvalueFactoryDataCRC,
       "osw10bstateflagFactoryDataCRC": osw10bstateflagFactoryDataCRC,
       "osw10blabelCalibrateTableStatus": osw10blabelCalibrateTableStatus,
       "osw10bvalueCalibrateTableStatus": osw10bvalueCalibrateTableStatus,
       "osw10bstateflagCalibrateTableStatus": osw10bstateflagCalibrateTableStatus,
       "osw10blabelAlarmDataCrc": osw10blabelAlarmDataCrc,
       "osw10bvalueAlarmDataCrc": osw10bvalueAlarmDataCrc,
       "osw10bstateflagAlarmDataCrc": osw10bstateflagAlarmDataCrc,
       "osw10blabelInputStatus": osw10blabelInputStatus,
       "osw10bvalueInputStatus": osw10bvalueInputStatus,
       "osw10bstateflagInputStatus": osw10bstateflagInputStatus,
       "osw10blabelPriActiveStatus": osw10blabelPriActiveStatus,
       "osw10bvaluePriActiveStatus": osw10bvaluePriActiveStatus,
       "osw10bstateflagPriActiveStatus": osw10bstateflagPriActiveStatus,
       "osw10blabelHardwareErr": osw10blabelHardwareErr,
       "osw10bvalueHardwareErr": osw10bvalueHardwareErr,
       "osw10bstateflagHardwareErr": osw10bstateflagHardwareErr,
       "osw10blabelPriThresholdStatus": osw10blabelPriThresholdStatus,
       "osw10bvaluePriThresholdStatus": osw10bvaluePriThresholdStatus,
       "osw10bstateflagPriThresholdStatus": osw10bstateflagPriThresholdStatus,
       "osw10blabelSecThresholdStatus": osw10blabelSecThresholdStatus,
       "osw10bvalueSecThresholdStatus": osw10bvalueSecThresholdStatus,
       "osw10bstateflagSecThresholdStatus": osw10bstateflagSecThresholdStatus,
       "gx2Osw10bFactoryTable": gx2Osw10bFactoryTable,
       "gx2Osw10bFactoryEntry": gx2Osw10bFactoryEntry,
       "gx2Osw10bFactoryTableIndex": gx2Osw10bFactoryTableIndex,
       "osw10bbootControlByte": osw10bbootControlByte,
       "osw10bbootStatusByte": osw10bbootStatusByte,
       "osw10bbank1CRC": osw10bbank1CRC,
       "osw10bbank2CRC": osw10bbank2CRC,
       "osw10bprgEEPROMByte": osw10bprgEEPROMByte,
       "osw10bfactoryCRC": osw10bfactoryCRC,
       "osw10bcalculateCRC": osw10bcalculateCRC,
       "osw10bhourMeter": osw10bhourMeter,
       "osw10bflashPrgCntA": osw10bflashPrgCntA,
       "osw10bflashPrgCntB": osw10bflashPrgCntB,
       "osw10bflashBankARev": osw10bflashBankARev,
       "osw10bflashBankBRev": osw10bflashBankBRev,
       "gx2Osw10bHoldTimeTable": gx2Osw10bHoldTimeTable,
       "gx2Osw10bHoldTimeEntry": gx2Osw10bHoldTimeEntry,
       "rxgx2Osw10bHoldTimeTableIndex": rxgx2Osw10bHoldTimeTableIndex,
       "rxgx2Osw10bHoldTimeSpecIndex": rxgx2Osw10bHoldTimeSpecIndex,
       "rxgx2Osw10bHoldTimeData": rxgx2Osw10bHoldTimeData}
)
