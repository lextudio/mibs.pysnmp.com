# SNMP MIB module (OMNI-gx2RSW1000B-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2RSW1000B-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:31 2024
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

(gx2Rsw1000b,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Rsw1000b")

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

_Gx2Rsw1000bDescriptor_ObjectIdentity = ObjectIdentity
gx2Rsw1000bDescriptor = _Gx2Rsw1000bDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 1)
)
_Gx2Rsw1000bAnalogTable_Object = MibTable
gx2Rsw1000bAnalogTable = _Gx2Rsw1000bAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2)
)
if mibBuilder.loadTexts:
    gx2Rsw1000bAnalogTable.setStatus("mandatory")
_Gx2Rsw1000bAnalogEntry_Object = MibTableRow
gx2Rsw1000bAnalogEntry = _Gx2Rsw1000bAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1)
)
gx2Rsw1000bAnalogEntry.setIndexNames(
    (0, "OMNI-gx2RSW1000B-MIB", "gx2Rsw1000bAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw1000bAnalogEntry.setStatus("mandatory")


class _Gx2Rsw1000bAnalogTableIndex_Type(Integer32):
    """Custom type gx2Rsw1000bAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Rsw1000bAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2Rsw1000bAnalogTableIndex_Object = MibTableColumn
gx2Rsw1000bAnalogTableIndex = _Gx2Rsw1000bAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 1),
    _Gx2Rsw1000bAnalogTableIndex_Type()
)
gx2Rsw1000bAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rsw1000bAnalogTableIndex.setStatus("mandatory")


class _Rsw1000blabelPriRFInputLvl_Type(DisplayString):
    """Custom type rsw1000blabelPriRFInputLvl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelPriRFInputLvl_Type.__name__ = "DisplayString"
_Rsw1000blabelPriRFInputLvl_Object = MibTableColumn
rsw1000blabelPriRFInputLvl = _Rsw1000blabelPriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 2),
    _Rsw1000blabelPriRFInputLvl_Type()
)
rsw1000blabelPriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelPriRFInputLvl.setStatus("optional")


class _Rsw1000buomPriRFInputLvl_Type(DisplayString):
    """Custom type rsw1000buomPriRFInputLvl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000buomPriRFInputLvl_Type.__name__ = "DisplayString"
_Rsw1000buomPriRFInputLvl_Object = MibTableColumn
rsw1000buomPriRFInputLvl = _Rsw1000buomPriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 3),
    _Rsw1000buomPriRFInputLvl_Type()
)
rsw1000buomPriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000buomPriRFInputLvl.setStatus("optional")
_Rsw1000bmajorHighPriRFInputLvl_Type = Float
_Rsw1000bmajorHighPriRFInputLvl_Object = MibTableColumn
rsw1000bmajorHighPriRFInputLvl = _Rsw1000bmajorHighPriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 4),
    _Rsw1000bmajorHighPriRFInputLvl_Type()
)
rsw1000bmajorHighPriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorHighPriRFInputLvl.setStatus("obsolete")
_Rsw1000bmajorLowPriRFInputLvl_Type = Float
_Rsw1000bmajorLowPriRFInputLvl_Object = MibTableColumn
rsw1000bmajorLowPriRFInputLvl = _Rsw1000bmajorLowPriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 5),
    _Rsw1000bmajorLowPriRFInputLvl_Type()
)
rsw1000bmajorLowPriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorLowPriRFInputLvl.setStatus("obsolete")
_Rsw1000bminorHighPriRFInputLvl_Type = Float
_Rsw1000bminorHighPriRFInputLvl_Object = MibTableColumn
rsw1000bminorHighPriRFInputLvl = _Rsw1000bminorHighPriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 6),
    _Rsw1000bminorHighPriRFInputLvl_Type()
)
rsw1000bminorHighPriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorHighPriRFInputLvl.setStatus("obsolete")
_Rsw1000bminorLowPriRFInputLvl_Type = Float
_Rsw1000bminorLowPriRFInputLvl_Object = MibTableColumn
rsw1000bminorLowPriRFInputLvl = _Rsw1000bminorLowPriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 7),
    _Rsw1000bminorLowPriRFInputLvl_Type()
)
rsw1000bminorLowPriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorLowPriRFInputLvl.setStatus("obsolete")
_Rsw1000bcurrentValuePriRFInputLvl_Type = Float
_Rsw1000bcurrentValuePriRFInputLvl_Object = MibTableColumn
rsw1000bcurrentValuePriRFInputLvl = _Rsw1000bcurrentValuePriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 8),
    _Rsw1000bcurrentValuePriRFInputLvl_Type()
)
rsw1000bcurrentValuePriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bcurrentValuePriRFInputLvl.setStatus("mandatory")


class _Rsw1000bstateFlagPriRFInputLvl_Type(Integer32):
    """Custom type rsw1000bstateFlagPriRFInputLvl based on Integer32"""
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


_Rsw1000bstateFlagPriRFInputLvl_Type.__name__ = "Integer32"
_Rsw1000bstateFlagPriRFInputLvl_Object = MibTableColumn
rsw1000bstateFlagPriRFInputLvl = _Rsw1000bstateFlagPriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 9),
    _Rsw1000bstateFlagPriRFInputLvl_Type()
)
rsw1000bstateFlagPriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateFlagPriRFInputLvl.setStatus("mandatory")
_Rsw1000bminValuePriRFInputLvl_Type = Float
_Rsw1000bminValuePriRFInputLvl_Object = MibTableColumn
rsw1000bminValuePriRFInputLvl = _Rsw1000bminValuePriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 10),
    _Rsw1000bminValuePriRFInputLvl_Type()
)
rsw1000bminValuePriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminValuePriRFInputLvl.setStatus("mandatory")
_Rsw1000bmaxValuePriRFInputLvl_Type = Float
_Rsw1000bmaxValuePriRFInputLvl_Object = MibTableColumn
rsw1000bmaxValuePriRFInputLvl = _Rsw1000bmaxValuePriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 11),
    _Rsw1000bmaxValuePriRFInputLvl_Type()
)
rsw1000bmaxValuePriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmaxValuePriRFInputLvl.setStatus("mandatory")


class _Rsw1000balarmStatePriRFInputLvl_Type(Integer32):
    """Custom type rsw1000balarmStatePriRFInputLvl based on Integer32"""
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


_Rsw1000balarmStatePriRFInputLvl_Type.__name__ = "Integer32"
_Rsw1000balarmStatePriRFInputLvl_Object = MibTableColumn
rsw1000balarmStatePriRFInputLvl = _Rsw1000balarmStatePriRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 12),
    _Rsw1000balarmStatePriRFInputLvl_Type()
)
rsw1000balarmStatePriRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000balarmStatePriRFInputLvl.setStatus("mandatory")


class _Rsw1000blabelSecRFInputLvl_Type(DisplayString):
    """Custom type rsw1000blabelSecRFInputLvl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelSecRFInputLvl_Type.__name__ = "DisplayString"
_Rsw1000blabelSecRFInputLvl_Object = MibTableColumn
rsw1000blabelSecRFInputLvl = _Rsw1000blabelSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 13),
    _Rsw1000blabelSecRFInputLvl_Type()
)
rsw1000blabelSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelSecRFInputLvl.setStatus("optional")


class _Rsw1000buomSecRFInputLvl_Type(DisplayString):
    """Custom type rsw1000buomSecRFInputLvl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000buomSecRFInputLvl_Type.__name__ = "DisplayString"
_Rsw1000buomSecRFInputLvl_Object = MibTableColumn
rsw1000buomSecRFInputLvl = _Rsw1000buomSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 14),
    _Rsw1000buomSecRFInputLvl_Type()
)
rsw1000buomSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000buomSecRFInputLvl.setStatus("optional")
_Rsw1000bmajorHighSecRFInputLvl_Type = Float
_Rsw1000bmajorHighSecRFInputLvl_Object = MibTableColumn
rsw1000bmajorHighSecRFInputLvl = _Rsw1000bmajorHighSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 15),
    _Rsw1000bmajorHighSecRFInputLvl_Type()
)
rsw1000bmajorHighSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorHighSecRFInputLvl.setStatus("obsolete")
_Rsw1000bmajorLowSecRFInputLvl_Type = Float
_Rsw1000bmajorLowSecRFInputLvl_Object = MibTableColumn
rsw1000bmajorLowSecRFInputLvl = _Rsw1000bmajorLowSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 16),
    _Rsw1000bmajorLowSecRFInputLvl_Type()
)
rsw1000bmajorLowSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorLowSecRFInputLvl.setStatus("obsolete")
_Rsw1000bminorHighSecRFInputLvl_Type = Float
_Rsw1000bminorHighSecRFInputLvl_Object = MibTableColumn
rsw1000bminorHighSecRFInputLvl = _Rsw1000bminorHighSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 17),
    _Rsw1000bminorHighSecRFInputLvl_Type()
)
rsw1000bminorHighSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorHighSecRFInputLvl.setStatus("obsolete")
_Rsw1000bminorLowSecRFInputLvl_Type = Float
_Rsw1000bminorLowSecRFInputLvl_Object = MibTableColumn
rsw1000bminorLowSecRFInputLvl = _Rsw1000bminorLowSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 18),
    _Rsw1000bminorLowSecRFInputLvl_Type()
)
rsw1000bminorLowSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorLowSecRFInputLvl.setStatus("obsolete")
_Rsw1000bcurrentValueSecRFInputLvl_Type = Float
_Rsw1000bcurrentValueSecRFInputLvl_Object = MibTableColumn
rsw1000bcurrentValueSecRFInputLvl = _Rsw1000bcurrentValueSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 19),
    _Rsw1000bcurrentValueSecRFInputLvl_Type()
)
rsw1000bcurrentValueSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bcurrentValueSecRFInputLvl.setStatus("mandatory")


class _Rsw1000bstateFlagSecRFInputLvl_Type(Integer32):
    """Custom type rsw1000bstateFlagSecRFInputLvl based on Integer32"""
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


_Rsw1000bstateFlagSecRFInputLvl_Type.__name__ = "Integer32"
_Rsw1000bstateFlagSecRFInputLvl_Object = MibTableColumn
rsw1000bstateFlagSecRFInputLvl = _Rsw1000bstateFlagSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 20),
    _Rsw1000bstateFlagSecRFInputLvl_Type()
)
rsw1000bstateFlagSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateFlagSecRFInputLvl.setStatus("mandatory")
_Rsw1000bminValueSecRFInputLvl_Type = Float
_Rsw1000bminValueSecRFInputLvl_Object = MibTableColumn
rsw1000bminValueSecRFInputLvl = _Rsw1000bminValueSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 21),
    _Rsw1000bminValueSecRFInputLvl_Type()
)
rsw1000bminValueSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminValueSecRFInputLvl.setStatus("mandatory")
_Rsw1000bmaxValueSecRFInputLvl_Type = Float
_Rsw1000bmaxValueSecRFInputLvl_Object = MibTableColumn
rsw1000bmaxValueSecRFInputLvl = _Rsw1000bmaxValueSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 22),
    _Rsw1000bmaxValueSecRFInputLvl_Type()
)
rsw1000bmaxValueSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmaxValueSecRFInputLvl.setStatus("mandatory")


class _Rsw1000balarmStateSecRFInputLvl_Type(Integer32):
    """Custom type rsw1000balarmStateSecRFInputLvl based on Integer32"""
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


_Rsw1000balarmStateSecRFInputLvl_Type.__name__ = "Integer32"
_Rsw1000balarmStateSecRFInputLvl_Object = MibTableColumn
rsw1000balarmStateSecRFInputLvl = _Rsw1000balarmStateSecRFInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 23),
    _Rsw1000balarmStateSecRFInputLvl_Type()
)
rsw1000balarmStateSecRFInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000balarmStateSecRFInputLvl.setStatus("mandatory")


class _Rsw1000blabelPriRFThreshold_Type(DisplayString):
    """Custom type rsw1000blabelPriRFThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelPriRFThreshold_Type.__name__ = "DisplayString"
_Rsw1000blabelPriRFThreshold_Object = MibTableColumn
rsw1000blabelPriRFThreshold = _Rsw1000blabelPriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 24),
    _Rsw1000blabelPriRFThreshold_Type()
)
rsw1000blabelPriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelPriRFThreshold.setStatus("optional")


class _Rsw1000buomPriRFThreshold_Type(DisplayString):
    """Custom type rsw1000buomPriRFThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000buomPriRFThreshold_Type.__name__ = "DisplayString"
_Rsw1000buomPriRFThreshold_Object = MibTableColumn
rsw1000buomPriRFThreshold = _Rsw1000buomPriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 25),
    _Rsw1000buomPriRFThreshold_Type()
)
rsw1000buomPriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000buomPriRFThreshold.setStatus("optional")
_Rsw1000bmajorHighPriRFThreshold_Type = Float
_Rsw1000bmajorHighPriRFThreshold_Object = MibTableColumn
rsw1000bmajorHighPriRFThreshold = _Rsw1000bmajorHighPriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 26),
    _Rsw1000bmajorHighPriRFThreshold_Type()
)
rsw1000bmajorHighPriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorHighPriRFThreshold.setStatus("obsolete")
_Rsw1000bmajorLowPriRFThreshold_Type = Float
_Rsw1000bmajorLowPriRFThreshold_Object = MibTableColumn
rsw1000bmajorLowPriRFThreshold = _Rsw1000bmajorLowPriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 27),
    _Rsw1000bmajorLowPriRFThreshold_Type()
)
rsw1000bmajorLowPriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorLowPriRFThreshold.setStatus("obsolete")
_Rsw1000bminorHighPriRFThreshold_Type = Float
_Rsw1000bminorHighPriRFThreshold_Object = MibTableColumn
rsw1000bminorHighPriRFThreshold = _Rsw1000bminorHighPriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 28),
    _Rsw1000bminorHighPriRFThreshold_Type()
)
rsw1000bminorHighPriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorHighPriRFThreshold.setStatus("obsolete")
_Rsw1000bminorLowPriRFThreshold_Type = Float
_Rsw1000bminorLowPriRFThreshold_Object = MibTableColumn
rsw1000bminorLowPriRFThreshold = _Rsw1000bminorLowPriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 29),
    _Rsw1000bminorLowPriRFThreshold_Type()
)
rsw1000bminorLowPriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorLowPriRFThreshold.setStatus("obsolete")
_Rsw1000bcurrentValuePriRFThreshold_Type = Float
_Rsw1000bcurrentValuePriRFThreshold_Object = MibTableColumn
rsw1000bcurrentValuePriRFThreshold = _Rsw1000bcurrentValuePriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 30),
    _Rsw1000bcurrentValuePriRFThreshold_Type()
)
rsw1000bcurrentValuePriRFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw1000bcurrentValuePriRFThreshold.setStatus("mandatory")


class _Rsw1000bstateFlagPriRFThreshold_Type(Integer32):
    """Custom type rsw1000bstateFlagPriRFThreshold based on Integer32"""
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


_Rsw1000bstateFlagPriRFThreshold_Type.__name__ = "Integer32"
_Rsw1000bstateFlagPriRFThreshold_Object = MibTableColumn
rsw1000bstateFlagPriRFThreshold = _Rsw1000bstateFlagPriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 31),
    _Rsw1000bstateFlagPriRFThreshold_Type()
)
rsw1000bstateFlagPriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateFlagPriRFThreshold.setStatus("mandatory")
_Rsw1000bminValuePriRFThreshold_Type = Float
_Rsw1000bminValuePriRFThreshold_Object = MibTableColumn
rsw1000bminValuePriRFThreshold = _Rsw1000bminValuePriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 32),
    _Rsw1000bminValuePriRFThreshold_Type()
)
rsw1000bminValuePriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminValuePriRFThreshold.setStatus("mandatory")
_Rsw1000bmaxValuePriRFThreshold_Type = Float
_Rsw1000bmaxValuePriRFThreshold_Object = MibTableColumn
rsw1000bmaxValuePriRFThreshold = _Rsw1000bmaxValuePriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 33),
    _Rsw1000bmaxValuePriRFThreshold_Type()
)
rsw1000bmaxValuePriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmaxValuePriRFThreshold.setStatus("mandatory")


class _Rsw1000balarmStatePriRFThreshold_Type(Integer32):
    """Custom type rsw1000balarmStatePriRFThreshold based on Integer32"""
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


_Rsw1000balarmStatePriRFThreshold_Type.__name__ = "Integer32"
_Rsw1000balarmStatePriRFThreshold_Object = MibTableColumn
rsw1000balarmStatePriRFThreshold = _Rsw1000balarmStatePriRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 34),
    _Rsw1000balarmStatePriRFThreshold_Type()
)
rsw1000balarmStatePriRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000balarmStatePriRFThreshold.setStatus("mandatory")


class _Rsw1000blabelSecRFThreshold_Type(DisplayString):
    """Custom type rsw1000blabelSecRFThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelSecRFThreshold_Type.__name__ = "DisplayString"
_Rsw1000blabelSecRFThreshold_Object = MibTableColumn
rsw1000blabelSecRFThreshold = _Rsw1000blabelSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 35),
    _Rsw1000blabelSecRFThreshold_Type()
)
rsw1000blabelSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelSecRFThreshold.setStatus("optional")


class _Rsw1000buomSecRFThreshold_Type(DisplayString):
    """Custom type rsw1000buomSecRFThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000buomSecRFThreshold_Type.__name__ = "DisplayString"
_Rsw1000buomSecRFThreshold_Object = MibTableColumn
rsw1000buomSecRFThreshold = _Rsw1000buomSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 36),
    _Rsw1000buomSecRFThreshold_Type()
)
rsw1000buomSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000buomSecRFThreshold.setStatus("optional")
_Rsw1000bmajorHighSecRFThreshold_Type = Float
_Rsw1000bmajorHighSecRFThreshold_Object = MibTableColumn
rsw1000bmajorHighSecRFThreshold = _Rsw1000bmajorHighSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 37),
    _Rsw1000bmajorHighSecRFThreshold_Type()
)
rsw1000bmajorHighSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorHighSecRFThreshold.setStatus("obsolete")
_Rsw1000bmajorLowSecRFThreshold_Type = Float
_Rsw1000bmajorLowSecRFThreshold_Object = MibTableColumn
rsw1000bmajorLowSecRFThreshold = _Rsw1000bmajorLowSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 38),
    _Rsw1000bmajorLowSecRFThreshold_Type()
)
rsw1000bmajorLowSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorLowSecRFThreshold.setStatus("obsolete")
_Rsw1000bminorHighSecRFThreshold_Type = Float
_Rsw1000bminorHighSecRFThreshold_Object = MibTableColumn
rsw1000bminorHighSecRFThreshold = _Rsw1000bminorHighSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 39),
    _Rsw1000bminorHighSecRFThreshold_Type()
)
rsw1000bminorHighSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorHighSecRFThreshold.setStatus("obsolete")
_Rsw1000bminorLowSecRFThreshold_Type = Float
_Rsw1000bminorLowSecRFThreshold_Object = MibTableColumn
rsw1000bminorLowSecRFThreshold = _Rsw1000bminorLowSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 40),
    _Rsw1000bminorLowSecRFThreshold_Type()
)
rsw1000bminorLowSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorLowSecRFThreshold.setStatus("obsolete")
_Rsw1000bcurrentValueSecRFThreshold_Type = Float
_Rsw1000bcurrentValueSecRFThreshold_Object = MibTableColumn
rsw1000bcurrentValueSecRFThreshold = _Rsw1000bcurrentValueSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 41),
    _Rsw1000bcurrentValueSecRFThreshold_Type()
)
rsw1000bcurrentValueSecRFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw1000bcurrentValueSecRFThreshold.setStatus("mandatory")


class _Rsw1000bstateFlagSecRFThreshold_Type(Integer32):
    """Custom type rsw1000bstateFlagSecRFThreshold based on Integer32"""
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


_Rsw1000bstateFlagSecRFThreshold_Type.__name__ = "Integer32"
_Rsw1000bstateFlagSecRFThreshold_Object = MibTableColumn
rsw1000bstateFlagSecRFThreshold = _Rsw1000bstateFlagSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 42),
    _Rsw1000bstateFlagSecRFThreshold_Type()
)
rsw1000bstateFlagSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateFlagSecRFThreshold.setStatus("mandatory")
_Rsw1000bminValueSecRFThreshold_Type = Float
_Rsw1000bminValueSecRFThreshold_Object = MibTableColumn
rsw1000bminValueSecRFThreshold = _Rsw1000bminValueSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 43),
    _Rsw1000bminValueSecRFThreshold_Type()
)
rsw1000bminValueSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminValueSecRFThreshold.setStatus("mandatory")
_Rsw1000bmaxValueSecRFThreshold_Type = Float
_Rsw1000bmaxValueSecRFThreshold_Object = MibTableColumn
rsw1000bmaxValueSecRFThreshold = _Rsw1000bmaxValueSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 44),
    _Rsw1000bmaxValueSecRFThreshold_Type()
)
rsw1000bmaxValueSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmaxValueSecRFThreshold.setStatus("mandatory")


class _Rsw1000balarmStateSecRFThreshold_Type(Integer32):
    """Custom type rsw1000balarmStateSecRFThreshold based on Integer32"""
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


_Rsw1000balarmStateSecRFThreshold_Type.__name__ = "Integer32"
_Rsw1000balarmStateSecRFThreshold_Object = MibTableColumn
rsw1000balarmStateSecRFThreshold = _Rsw1000balarmStateSecRFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 45),
    _Rsw1000balarmStateSecRFThreshold_Type()
)
rsw1000balarmStateSecRFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000balarmStateSecRFThreshold.setStatus("mandatory")


class _Rsw1000blabelModTemp_Type(DisplayString):
    """Custom type rsw1000blabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelModTemp_Type.__name__ = "DisplayString"
_Rsw1000blabelModTemp_Object = MibTableColumn
rsw1000blabelModTemp = _Rsw1000blabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 46),
    _Rsw1000blabelModTemp_Type()
)
rsw1000blabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelModTemp.setStatus("optional")


class _Rsw1000buomModTemp_Type(DisplayString):
    """Custom type rsw1000buomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000buomModTemp_Type.__name__ = "DisplayString"
_Rsw1000buomModTemp_Object = MibTableColumn
rsw1000buomModTemp = _Rsw1000buomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 47),
    _Rsw1000buomModTemp_Type()
)
rsw1000buomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000buomModTemp.setStatus("optional")
_Rsw1000bmajorHighModTemp_Type = Float
_Rsw1000bmajorHighModTemp_Object = MibTableColumn
rsw1000bmajorHighModTemp = _Rsw1000bmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 48),
    _Rsw1000bmajorHighModTemp_Type()
)
rsw1000bmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorHighModTemp.setStatus("mandatory")
_Rsw1000bmajorLowModTemp_Type = Float
_Rsw1000bmajorLowModTemp_Object = MibTableColumn
rsw1000bmajorLowModTemp = _Rsw1000bmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 49),
    _Rsw1000bmajorLowModTemp_Type()
)
rsw1000bmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorLowModTemp.setStatus("mandatory")
_Rsw1000bminorHighModTemp_Type = Float
_Rsw1000bminorHighModTemp_Object = MibTableColumn
rsw1000bminorHighModTemp = _Rsw1000bminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 50),
    _Rsw1000bminorHighModTemp_Type()
)
rsw1000bminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorHighModTemp.setStatus("mandatory")
_Rsw1000bminorLowModTemp_Type = Float
_Rsw1000bminorLowModTemp_Object = MibTableColumn
rsw1000bminorLowModTemp = _Rsw1000bminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 51),
    _Rsw1000bminorLowModTemp_Type()
)
rsw1000bminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorLowModTemp.setStatus("mandatory")
_Rsw1000bcurrentValueModTemp_Type = Float
_Rsw1000bcurrentValueModTemp_Object = MibTableColumn
rsw1000bcurrentValueModTemp = _Rsw1000bcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 52),
    _Rsw1000bcurrentValueModTemp_Type()
)
rsw1000bcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bcurrentValueModTemp.setStatus("mandatory")


class _Rsw1000bstateFlagModTemp_Type(Integer32):
    """Custom type rsw1000bstateFlagModTemp based on Integer32"""
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


_Rsw1000bstateFlagModTemp_Type.__name__ = "Integer32"
_Rsw1000bstateFlagModTemp_Object = MibTableColumn
rsw1000bstateFlagModTemp = _Rsw1000bstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 53),
    _Rsw1000bstateFlagModTemp_Type()
)
rsw1000bstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateFlagModTemp.setStatus("mandatory")
_Rsw1000bminValueModTemp_Type = Float
_Rsw1000bminValueModTemp_Object = MibTableColumn
rsw1000bminValueModTemp = _Rsw1000bminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 54),
    _Rsw1000bminValueModTemp_Type()
)
rsw1000bminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminValueModTemp.setStatus("mandatory")
_Rsw1000bmaxValueModTemp_Type = Float
_Rsw1000bmaxValueModTemp_Object = MibTableColumn
rsw1000bmaxValueModTemp = _Rsw1000bmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 55),
    _Rsw1000bmaxValueModTemp_Type()
)
rsw1000bmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmaxValueModTemp.setStatus("mandatory")


class _Rsw1000balarmStateModTemp_Type(Integer32):
    """Custom type rsw1000balarmStateModTemp based on Integer32"""
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


_Rsw1000balarmStateModTemp_Type.__name__ = "Integer32"
_Rsw1000balarmStateModTemp_Object = MibTableColumn
rsw1000balarmStateModTemp = _Rsw1000balarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 56),
    _Rsw1000balarmStateModTemp_Type()
)
rsw1000balarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000balarmStateModTemp.setStatus("mandatory")


class _Rsw1000blabelFanCurrent_Type(DisplayString):
    """Custom type rsw1000blabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelFanCurrent_Type.__name__ = "DisplayString"
_Rsw1000blabelFanCurrent_Object = MibTableColumn
rsw1000blabelFanCurrent = _Rsw1000blabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 57),
    _Rsw1000blabelFanCurrent_Type()
)
rsw1000blabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelFanCurrent.setStatus("optional")


class _Rsw1000buomFanCurrent_Type(DisplayString):
    """Custom type rsw1000buomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000buomFanCurrent_Type.__name__ = "DisplayString"
_Rsw1000buomFanCurrent_Object = MibTableColumn
rsw1000buomFanCurrent = _Rsw1000buomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 58),
    _Rsw1000buomFanCurrent_Type()
)
rsw1000buomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000buomFanCurrent.setStatus("optional")
_Rsw1000bmajorHighFanCurrent_Type = Float
_Rsw1000bmajorHighFanCurrent_Object = MibTableColumn
rsw1000bmajorHighFanCurrent = _Rsw1000bmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 59),
    _Rsw1000bmajorHighFanCurrent_Type()
)
rsw1000bmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorHighFanCurrent.setStatus("mandatory")
_Rsw1000bmajorLowFanCurrent_Type = Float
_Rsw1000bmajorLowFanCurrent_Object = MibTableColumn
rsw1000bmajorLowFanCurrent = _Rsw1000bmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 60),
    _Rsw1000bmajorLowFanCurrent_Type()
)
rsw1000bmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmajorLowFanCurrent.setStatus("mandatory")
_Rsw1000bminorHighFanCurrent_Type = Float
_Rsw1000bminorHighFanCurrent_Object = MibTableColumn
rsw1000bminorHighFanCurrent = _Rsw1000bminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 61),
    _Rsw1000bminorHighFanCurrent_Type()
)
rsw1000bminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorHighFanCurrent.setStatus("obsolete")
_Rsw1000bminorLowFanCurrent_Type = Float
_Rsw1000bminorLowFanCurrent_Object = MibTableColumn
rsw1000bminorLowFanCurrent = _Rsw1000bminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 62),
    _Rsw1000bminorLowFanCurrent_Type()
)
rsw1000bminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminorLowFanCurrent.setStatus("obsolete")
_Rsw1000bcurrentValueFanCurrent_Type = Float
_Rsw1000bcurrentValueFanCurrent_Object = MibTableColumn
rsw1000bcurrentValueFanCurrent = _Rsw1000bcurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 63),
    _Rsw1000bcurrentValueFanCurrent_Type()
)
rsw1000bcurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bcurrentValueFanCurrent.setStatus("mandatory")


class _Rsw1000bstateFlagFanCurrent_Type(Integer32):
    """Custom type rsw1000bstateFlagFanCurrent based on Integer32"""
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


_Rsw1000bstateFlagFanCurrent_Type.__name__ = "Integer32"
_Rsw1000bstateFlagFanCurrent_Object = MibTableColumn
rsw1000bstateFlagFanCurrent = _Rsw1000bstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 64),
    _Rsw1000bstateFlagFanCurrent_Type()
)
rsw1000bstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateFlagFanCurrent.setStatus("mandatory")
_Rsw1000bminValueFanCurrent_Type = Float
_Rsw1000bminValueFanCurrent_Object = MibTableColumn
rsw1000bminValueFanCurrent = _Rsw1000bminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 65),
    _Rsw1000bminValueFanCurrent_Type()
)
rsw1000bminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bminValueFanCurrent.setStatus("mandatory")
_Rsw1000bmaxValueFanCurrent_Type = Float
_Rsw1000bmaxValueFanCurrent_Object = MibTableColumn
rsw1000bmaxValueFanCurrent = _Rsw1000bmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 66),
    _Rsw1000bmaxValueFanCurrent_Type()
)
rsw1000bmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bmaxValueFanCurrent.setStatus("mandatory")


class _Rsw1000balarmStateFanCurrent_Type(Integer32):
    """Custom type rsw1000balarmStateFanCurrent based on Integer32"""
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


_Rsw1000balarmStateFanCurrent_Type.__name__ = "Integer32"
_Rsw1000balarmStateFanCurrent_Object = MibTableColumn
rsw1000balarmStateFanCurrent = _Rsw1000balarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 2, 1, 67),
    _Rsw1000balarmStateFanCurrent_Type()
)
rsw1000balarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000balarmStateFanCurrent.setStatus("mandatory")
_Gx2Rsw1000bDigitalTable_Object = MibTable
gx2Rsw1000bDigitalTable = _Gx2Rsw1000bDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3)
)
if mibBuilder.loadTexts:
    gx2Rsw1000bDigitalTable.setStatus("mandatory")
_Gx2Rsw1000bDigitalEntry_Object = MibTableRow
gx2Rsw1000bDigitalEntry = _Gx2Rsw1000bDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2)
)
gx2Rsw1000bDigitalEntry.setIndexNames(
    (0, "OMNI-gx2RSW1000B-MIB", "gx2Rsw1000bDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw1000bDigitalEntry.setStatus("mandatory")


class _Gx2Rsw1000bDigitalTableIndex_Type(Integer32):
    """Custom type gx2Rsw1000bDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Rsw1000bDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2Rsw1000bDigitalTableIndex_Object = MibTableColumn
gx2Rsw1000bDigitalTableIndex = _Gx2Rsw1000bDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 1),
    _Gx2Rsw1000bDigitalTableIndex_Type()
)
gx2Rsw1000bDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rsw1000bDigitalTableIndex.setStatus("mandatory")


class _Rsw1000blabelSwitchControl_Type(DisplayString):
    """Custom type rsw1000blabelSwitchControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelSwitchControl_Type.__name__ = "DisplayString"
_Rsw1000blabelSwitchControl_Object = MibTableColumn
rsw1000blabelSwitchControl = _Rsw1000blabelSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 2),
    _Rsw1000blabelSwitchControl_Type()
)
rsw1000blabelSwitchControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelSwitchControl.setStatus("optional")


class _Rsw1000benumSwitchControl_Type(DisplayString):
    """Custom type rsw1000benumSwitchControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000benumSwitchControl_Type.__name__ = "DisplayString"
_Rsw1000benumSwitchControl_Object = MibTableColumn
rsw1000benumSwitchControl = _Rsw1000benumSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 3),
    _Rsw1000benumSwitchControl_Type()
)
rsw1000benumSwitchControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000benumSwitchControl.setStatus("optional")


class _Rsw1000bvalueSwitchControl_Type(Integer32):
    """Custom type rsw1000bvalueSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Rsw1000bvalueSwitchControl_Type.__name__ = "Integer32"
_Rsw1000bvalueSwitchControl_Object = MibTableColumn
rsw1000bvalueSwitchControl = _Rsw1000bvalueSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 4),
    _Rsw1000bvalueSwitchControl_Type()
)
rsw1000bvalueSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw1000bvalueSwitchControl.setStatus("mandatory")


class _Rsw1000bstateflagSwitchControl_Type(Integer32):
    """Custom type rsw1000bstateflagSwitchControl based on Integer32"""
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


_Rsw1000bstateflagSwitchControl_Type.__name__ = "Integer32"
_Rsw1000bstateflagSwitchControl_Object = MibTableColumn
rsw1000bstateflagSwitchControl = _Rsw1000bstateflagSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 5),
    _Rsw1000bstateflagSwitchControl_Type()
)
rsw1000bstateflagSwitchControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagSwitchControl.setStatus("mandatory")


class _Rsw1000blabelSwitchMode_Type(DisplayString):
    """Custom type rsw1000blabelSwitchMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelSwitchMode_Type.__name__ = "DisplayString"
_Rsw1000blabelSwitchMode_Object = MibTableColumn
rsw1000blabelSwitchMode = _Rsw1000blabelSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 6),
    _Rsw1000blabelSwitchMode_Type()
)
rsw1000blabelSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelSwitchMode.setStatus("optional")


class _Rsw1000benumSwitchMode_Type(DisplayString):
    """Custom type rsw1000benumSwitchMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000benumSwitchMode_Type.__name__ = "DisplayString"
_Rsw1000benumSwitchMode_Object = MibTableColumn
rsw1000benumSwitchMode = _Rsw1000benumSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 7),
    _Rsw1000benumSwitchMode_Type()
)
rsw1000benumSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000benumSwitchMode.setStatus("optional")


class _Rsw1000bvalueSwitchMode_Type(Integer32):
    """Custom type rsw1000bvalueSwitchMode based on Integer32"""
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


_Rsw1000bvalueSwitchMode_Type.__name__ = "Integer32"
_Rsw1000bvalueSwitchMode_Object = MibTableColumn
rsw1000bvalueSwitchMode = _Rsw1000bvalueSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 8),
    _Rsw1000bvalueSwitchMode_Type()
)
rsw1000bvalueSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw1000bvalueSwitchMode.setStatus("mandatory")


class _Rsw1000bstateflagSwitchMode_Type(Integer32):
    """Custom type rsw1000bstateflagSwitchMode based on Integer32"""
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


_Rsw1000bstateflagSwitchMode_Type.__name__ = "Integer32"
_Rsw1000bstateflagSwitchMode_Object = MibTableColumn
rsw1000bstateflagSwitchMode = _Rsw1000bstateflagSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 9),
    _Rsw1000bstateflagSwitchMode_Type()
)
rsw1000bstateflagSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagSwitchMode.setStatus("mandatory")


class _Rsw1000blabelRevertEnable_Type(DisplayString):
    """Custom type rsw1000blabelRevertEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelRevertEnable_Type.__name__ = "DisplayString"
_Rsw1000blabelRevertEnable_Object = MibTableColumn
rsw1000blabelRevertEnable = _Rsw1000blabelRevertEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 10),
    _Rsw1000blabelRevertEnable_Type()
)
rsw1000blabelRevertEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelRevertEnable.setStatus("optional")


class _Rsw1000benumRevertEnable_Type(DisplayString):
    """Custom type rsw1000benumRevertEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000benumRevertEnable_Type.__name__ = "DisplayString"
_Rsw1000benumRevertEnable_Object = MibTableColumn
rsw1000benumRevertEnable = _Rsw1000benumRevertEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 11),
    _Rsw1000benumRevertEnable_Type()
)
rsw1000benumRevertEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000benumRevertEnable.setStatus("optional")


class _Rsw1000bvalueRevertEnable_Type(Integer32):
    """Custom type rsw1000bvalueRevertEnable based on Integer32"""
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


_Rsw1000bvalueRevertEnable_Type.__name__ = "Integer32"
_Rsw1000bvalueRevertEnable_Object = MibTableColumn
rsw1000bvalueRevertEnable = _Rsw1000bvalueRevertEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 12),
    _Rsw1000bvalueRevertEnable_Type()
)
rsw1000bvalueRevertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw1000bvalueRevertEnable.setStatus("mandatory")


class _Rsw1000bstateflagRevertEnable_Type(Integer32):
    """Custom type rsw1000bstateflagRevertEnable based on Integer32"""
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


_Rsw1000bstateflagRevertEnable_Type.__name__ = "Integer32"
_Rsw1000bstateflagRevertEnable_Object = MibTableColumn
rsw1000bstateflagRevertEnable = _Rsw1000bstateflagRevertEnable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 13),
    _Rsw1000bstateflagRevertEnable_Type()
)
rsw1000bstateflagRevertEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagRevertEnable.setStatus("mandatory")


class _Rsw1000blabelRevertTime_Type(DisplayString):
    """Custom type rsw1000blabelRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelRevertTime_Type.__name__ = "DisplayString"
_Rsw1000blabelRevertTime_Object = MibTableColumn
rsw1000blabelRevertTime = _Rsw1000blabelRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 14),
    _Rsw1000blabelRevertTime_Type()
)
rsw1000blabelRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelRevertTime.setStatus("optional")


class _Rsw1000benumRevertTime_Type(DisplayString):
    """Custom type rsw1000benumRevertTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000benumRevertTime_Type.__name__ = "DisplayString"
_Rsw1000benumRevertTime_Object = MibTableColumn
rsw1000benumRevertTime = _Rsw1000benumRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 15),
    _Rsw1000benumRevertTime_Type()
)
rsw1000benumRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000benumRevertTime.setStatus("optional")


class _Rsw1000bvalueRevertTime_Type(Integer32):
    """Custom type rsw1000bvalueRevertTime based on Integer32"""
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


_Rsw1000bvalueRevertTime_Type.__name__ = "Integer32"
_Rsw1000bvalueRevertTime_Object = MibTableColumn
rsw1000bvalueRevertTime = _Rsw1000bvalueRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 16),
    _Rsw1000bvalueRevertTime_Type()
)
rsw1000bvalueRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw1000bvalueRevertTime.setStatus("mandatory")


class _Rsw1000bstateflagRevertTime_Type(Integer32):
    """Custom type rsw1000bstateflagRevertTime based on Integer32"""
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


_Rsw1000bstateflagRevertTime_Type.__name__ = "Integer32"
_Rsw1000bstateflagRevertTime_Object = MibTableColumn
rsw1000bstateflagRevertTime = _Rsw1000bstateflagRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 17),
    _Rsw1000bstateflagRevertTime_Type()
)
rsw1000bstateflagRevertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagRevertTime.setStatus("mandatory")


class _Rsw1000blabelSensorMode_Type(DisplayString):
    """Custom type rsw1000blabelSensorMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelSensorMode_Type.__name__ = "DisplayString"
_Rsw1000blabelSensorMode_Object = MibTableColumn
rsw1000blabelSensorMode = _Rsw1000blabelSensorMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 18),
    _Rsw1000blabelSensorMode_Type()
)
rsw1000blabelSensorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelSensorMode.setStatus("optional")


class _Rsw1000benumSensorMode_Type(DisplayString):
    """Custom type rsw1000benumSensorMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000benumSensorMode_Type.__name__ = "DisplayString"
_Rsw1000benumSensorMode_Object = MibTableColumn
rsw1000benumSensorMode = _Rsw1000benumSensorMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 19),
    _Rsw1000benumSensorMode_Type()
)
rsw1000benumSensorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000benumSensorMode.setStatus("optional")


class _Rsw1000bvalueSensorMode_Type(Integer32):
    """Custom type rsw1000bvalueSensorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_Rsw1000bvalueSensorMode_Type.__name__ = "Integer32"
_Rsw1000bvalueSensorMode_Object = MibTableColumn
rsw1000bvalueSensorMode = _Rsw1000bvalueSensorMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 20),
    _Rsw1000bvalueSensorMode_Type()
)
rsw1000bvalueSensorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw1000bvalueSensorMode.setStatus("mandatory")


class _Rsw1000bstateflagSensorMode_Type(Integer32):
    """Custom type rsw1000bstateflagSensorMode based on Integer32"""
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


_Rsw1000bstateflagSensorMode_Type.__name__ = "Integer32"
_Rsw1000bstateflagSensorMode_Object = MibTableColumn
rsw1000bstateflagSensorMode = _Rsw1000bstateflagSensorMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 21),
    _Rsw1000bstateflagSensorMode_Type()
)
rsw1000bstateflagSensorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagSensorMode.setStatus("mandatory")


class _Rsw1000blabelSwitchMonitor_Type(DisplayString):
    """Custom type rsw1000blabelSwitchMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelSwitchMonitor_Type.__name__ = "DisplayString"
_Rsw1000blabelSwitchMonitor_Object = MibTableColumn
rsw1000blabelSwitchMonitor = _Rsw1000blabelSwitchMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 22),
    _Rsw1000blabelSwitchMonitor_Type()
)
rsw1000blabelSwitchMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelSwitchMonitor.setStatus("optional")


class _Rsw1000benumSwitchMonitor_Type(DisplayString):
    """Custom type rsw1000benumSwitchMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000benumSwitchMonitor_Type.__name__ = "DisplayString"
_Rsw1000benumSwitchMonitor_Object = MibTableColumn
rsw1000benumSwitchMonitor = _Rsw1000benumSwitchMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 23),
    _Rsw1000benumSwitchMonitor_Type()
)
rsw1000benumSwitchMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000benumSwitchMonitor.setStatus("optional")


class _Rsw1000bvalueSwitchMonitor_Type(Integer32):
    """Custom type rsw1000bvalueSwitchMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Rsw1000bvalueSwitchMonitor_Type.__name__ = "Integer32"
_Rsw1000bvalueSwitchMonitor_Object = MibTableColumn
rsw1000bvalueSwitchMonitor = _Rsw1000bvalueSwitchMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 24),
    _Rsw1000bvalueSwitchMonitor_Type()
)
rsw1000bvalueSwitchMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvalueSwitchMonitor.setStatus("mandatory")


class _Rsw1000bstateflagSwitchMonitor_Type(Integer32):
    """Custom type rsw1000bstateflagSwitchMonitor based on Integer32"""
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


_Rsw1000bstateflagSwitchMonitor_Type.__name__ = "Integer32"
_Rsw1000bstateflagSwitchMonitor_Object = MibTableColumn
rsw1000bstateflagSwitchMonitor = _Rsw1000bstateflagSwitchMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 25),
    _Rsw1000bstateflagSwitchMonitor_Type()
)
rsw1000bstateflagSwitchMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagSwitchMonitor.setStatus("mandatory")


class _Rsw1000blabelPriStatusSig_Type(DisplayString):
    """Custom type rsw1000blabelPriStatusSig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelPriStatusSig_Type.__name__ = "DisplayString"
_Rsw1000blabelPriStatusSig_Object = MibTableColumn
rsw1000blabelPriStatusSig = _Rsw1000blabelPriStatusSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 26),
    _Rsw1000blabelPriStatusSig_Type()
)
rsw1000blabelPriStatusSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelPriStatusSig.setStatus("optional")


class _Rsw1000benumPriStatusSig_Type(DisplayString):
    """Custom type rsw1000benumPriStatusSig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000benumPriStatusSig_Type.__name__ = "DisplayString"
_Rsw1000benumPriStatusSig_Object = MibTableColumn
rsw1000benumPriStatusSig = _Rsw1000benumPriStatusSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 27),
    _Rsw1000benumPriStatusSig_Type()
)
rsw1000benumPriStatusSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000benumPriStatusSig.setStatus("optional")


class _Rsw1000bvaluePriStatusSig_Type(Integer32):
    """Custom type rsw1000bvaluePriStatusSig based on Integer32"""
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
        *(("invalid", 3),
          ("open", 4),
          ("short", 1),
          ("valid", 2))
    )


_Rsw1000bvaluePriStatusSig_Type.__name__ = "Integer32"
_Rsw1000bvaluePriStatusSig_Object = MibTableColumn
rsw1000bvaluePriStatusSig = _Rsw1000bvaluePriStatusSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 28),
    _Rsw1000bvaluePriStatusSig_Type()
)
rsw1000bvaluePriStatusSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvaluePriStatusSig.setStatus("mandatory")


class _Rsw1000bstateflagPriStatusSig_Type(Integer32):
    """Custom type rsw1000bstateflagPriStatusSig based on Integer32"""
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


_Rsw1000bstateflagPriStatusSig_Type.__name__ = "Integer32"
_Rsw1000bstateflagPriStatusSig_Object = MibTableColumn
rsw1000bstateflagPriStatusSig = _Rsw1000bstateflagPriStatusSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 29),
    _Rsw1000bstateflagPriStatusSig_Type()
)
rsw1000bstateflagPriStatusSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagPriStatusSig.setStatus("mandatory")


class _Rsw1000blabelSecStatusSig_Type(DisplayString):
    """Custom type rsw1000blabelSecStatusSig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelSecStatusSig_Type.__name__ = "DisplayString"
_Rsw1000blabelSecStatusSig_Object = MibTableColumn
rsw1000blabelSecStatusSig = _Rsw1000blabelSecStatusSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 30),
    _Rsw1000blabelSecStatusSig_Type()
)
rsw1000blabelSecStatusSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelSecStatusSig.setStatus("optional")


class _Rsw1000benumSecStatusSig_Type(DisplayString):
    """Custom type rsw1000benumSecStatusSig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000benumSecStatusSig_Type.__name__ = "DisplayString"
_Rsw1000benumSecStatusSig_Object = MibTableColumn
rsw1000benumSecStatusSig = _Rsw1000benumSecStatusSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 31),
    _Rsw1000benumSecStatusSig_Type()
)
rsw1000benumSecStatusSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000benumSecStatusSig.setStatus("optional")


class _Rsw1000bvalueSecStatusSig_Type(Integer32):
    """Custom type rsw1000bvalueSecStatusSig based on Integer32"""
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
        *(("invalid", 3),
          ("open", 4),
          ("short", 1),
          ("valid", 2))
    )


_Rsw1000bvalueSecStatusSig_Type.__name__ = "Integer32"
_Rsw1000bvalueSecStatusSig_Object = MibTableColumn
rsw1000bvalueSecStatusSig = _Rsw1000bvalueSecStatusSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 32),
    _Rsw1000bvalueSecStatusSig_Type()
)
rsw1000bvalueSecStatusSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvalueSecStatusSig.setStatus("mandatory")


class _Rsw1000bstateflagSecStatusSig_Type(Integer32):
    """Custom type rsw1000bstateflagSecStatusSig based on Integer32"""
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


_Rsw1000bstateflagSecStatusSig_Type.__name__ = "Integer32"
_Rsw1000bstateflagSecStatusSig_Object = MibTableColumn
rsw1000bstateflagSecStatusSig = _Rsw1000bstateflagSecStatusSig_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 33),
    _Rsw1000bstateflagSecStatusSig_Type()
)
rsw1000bstateflagSecStatusSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagSecStatusSig.setStatus("mandatory")


class _Rsw1000blabelFactoryDefault_Type(DisplayString):
    """Custom type rsw1000blabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelFactoryDefault_Type.__name__ = "DisplayString"
_Rsw1000blabelFactoryDefault_Object = MibTableColumn
rsw1000blabelFactoryDefault = _Rsw1000blabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 34),
    _Rsw1000blabelFactoryDefault_Type()
)
rsw1000blabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelFactoryDefault.setStatus("optional")


class _Rsw1000benumFactoryDefault_Type(DisplayString):
    """Custom type rsw1000benumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000benumFactoryDefault_Type.__name__ = "DisplayString"
_Rsw1000benumFactoryDefault_Object = MibTableColumn
rsw1000benumFactoryDefault = _Rsw1000benumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 35),
    _Rsw1000benumFactoryDefault_Type()
)
rsw1000benumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000benumFactoryDefault.setStatus("optional")


class _Rsw1000bvalueFactoryDefault_Type(Integer32):
    """Custom type rsw1000bvalueFactoryDefault based on Integer32"""
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


_Rsw1000bvalueFactoryDefault_Type.__name__ = "Integer32"
_Rsw1000bvalueFactoryDefault_Object = MibTableColumn
rsw1000bvalueFactoryDefault = _Rsw1000bvalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 36),
    _Rsw1000bvalueFactoryDefault_Type()
)
rsw1000bvalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsw1000bvalueFactoryDefault.setStatus("mandatory")


class _Rsw1000bstateflagFactoryDefault_Type(Integer32):
    """Custom type rsw1000bstateflagFactoryDefault based on Integer32"""
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


_Rsw1000bstateflagFactoryDefault_Type.__name__ = "Integer32"
_Rsw1000bstateflagFactoryDefault_Object = MibTableColumn
rsw1000bstateflagFactoryDefault = _Rsw1000bstateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 3, 2, 37),
    _Rsw1000bstateflagFactoryDefault_Type()
)
rsw1000bstateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagFactoryDefault.setStatus("mandatory")
_Gx2Rsw1000bStatusTable_Object = MibTable
gx2Rsw1000bStatusTable = _Gx2Rsw1000bStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4)
)
if mibBuilder.loadTexts:
    gx2Rsw1000bStatusTable.setStatus("mandatory")
_Gx2Rsw1000bStatusEntry_Object = MibTableRow
gx2Rsw1000bStatusEntry = _Gx2Rsw1000bStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3)
)
gx2Rsw1000bStatusEntry.setIndexNames(
    (0, "OMNI-gx2RSW1000B-MIB", "gx2Rsw1000bStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw1000bStatusEntry.setStatus("mandatory")


class _Gx2Rsw1000bStatusTableIndex_Type(Integer32):
    """Custom type gx2Rsw1000bStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Rsw1000bStatusTableIndex_Type.__name__ = "Integer32"
_Gx2Rsw1000bStatusTableIndex_Object = MibTableColumn
gx2Rsw1000bStatusTableIndex = _Gx2Rsw1000bStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 1),
    _Gx2Rsw1000bStatusTableIndex_Type()
)
gx2Rsw1000bStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rsw1000bStatusTableIndex.setStatus("mandatory")


class _Rsw1000blabelBoot_Type(DisplayString):
    """Custom type rsw1000blabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelBoot_Type.__name__ = "DisplayString"
_Rsw1000blabelBoot_Object = MibTableColumn
rsw1000blabelBoot = _Rsw1000blabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 2),
    _Rsw1000blabelBoot_Type()
)
rsw1000blabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelBoot.setStatus("optional")


class _Rsw1000bvalueBoot_Type(Integer32):
    """Custom type rsw1000bvalueBoot based on Integer32"""
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


_Rsw1000bvalueBoot_Type.__name__ = "Integer32"
_Rsw1000bvalueBoot_Object = MibTableColumn
rsw1000bvalueBoot = _Rsw1000bvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 3),
    _Rsw1000bvalueBoot_Type()
)
rsw1000bvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvalueBoot.setStatus("mandatory")


class _Rsw1000bstateflagBoot_Type(Integer32):
    """Custom type rsw1000bstateflagBoot based on Integer32"""
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


_Rsw1000bstateflagBoot_Type.__name__ = "Integer32"
_Rsw1000bstateflagBoot_Object = MibTableColumn
rsw1000bstateflagBoot = _Rsw1000bstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 4),
    _Rsw1000bstateflagBoot_Type()
)
rsw1000bstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagBoot.setStatus("mandatory")


class _Rsw1000blabelFlash_Type(DisplayString):
    """Custom type rsw1000blabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelFlash_Type.__name__ = "DisplayString"
_Rsw1000blabelFlash_Object = MibTableColumn
rsw1000blabelFlash = _Rsw1000blabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 5),
    _Rsw1000blabelFlash_Type()
)
rsw1000blabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelFlash.setStatus("optional")


class _Rsw1000bvalueFlash_Type(Integer32):
    """Custom type rsw1000bvalueFlash based on Integer32"""
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


_Rsw1000bvalueFlash_Type.__name__ = "Integer32"
_Rsw1000bvalueFlash_Object = MibTableColumn
rsw1000bvalueFlash = _Rsw1000bvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 6),
    _Rsw1000bvalueFlash_Type()
)
rsw1000bvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvalueFlash.setStatus("mandatory")


class _Rsw1000bstateflagFlash_Type(Integer32):
    """Custom type rsw1000bstateflagFlash based on Integer32"""
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


_Rsw1000bstateflagFlash_Type.__name__ = "Integer32"
_Rsw1000bstateflagFlash_Object = MibTableColumn
rsw1000bstateflagFlash = _Rsw1000bstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 7),
    _Rsw1000bstateflagFlash_Type()
)
rsw1000bstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagFlash.setStatus("mandatory")


class _Rsw1000blabelFactoryDataCRC_Type(DisplayString):
    """Custom type rsw1000blabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelFactoryDataCRC_Type.__name__ = "DisplayString"
_Rsw1000blabelFactoryDataCRC_Object = MibTableColumn
rsw1000blabelFactoryDataCRC = _Rsw1000blabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 8),
    _Rsw1000blabelFactoryDataCRC_Type()
)
rsw1000blabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelFactoryDataCRC.setStatus("optional")


class _Rsw1000bvalueFactoryDataCRC_Type(Integer32):
    """Custom type rsw1000bvalueFactoryDataCRC based on Integer32"""
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


_Rsw1000bvalueFactoryDataCRC_Type.__name__ = "Integer32"
_Rsw1000bvalueFactoryDataCRC_Object = MibTableColumn
rsw1000bvalueFactoryDataCRC = _Rsw1000bvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 9),
    _Rsw1000bvalueFactoryDataCRC_Type()
)
rsw1000bvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvalueFactoryDataCRC.setStatus("mandatory")


class _Rsw1000bstateflagFactoryDataCRC_Type(Integer32):
    """Custom type rsw1000bstateflagFactoryDataCRC based on Integer32"""
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


_Rsw1000bstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Rsw1000bstateflagFactoryDataCRC_Object = MibTableColumn
rsw1000bstateflagFactoryDataCRC = _Rsw1000bstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 10),
    _Rsw1000bstateflagFactoryDataCRC_Type()
)
rsw1000bstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagFactoryDataCRC.setStatus("mandatory")


class _Rsw1000blabelRFDataCRC_Type(DisplayString):
    """Custom type rsw1000blabelRFDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelRFDataCRC_Type.__name__ = "DisplayString"
_Rsw1000blabelRFDataCRC_Object = MibTableColumn
rsw1000blabelRFDataCRC = _Rsw1000blabelRFDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 11),
    _Rsw1000blabelRFDataCRC_Type()
)
rsw1000blabelRFDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelRFDataCRC.setStatus("optional")


class _Rsw1000bvalueRFDataCRC_Type(Integer32):
    """Custom type rsw1000bvalueRFDataCRC based on Integer32"""
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


_Rsw1000bvalueRFDataCRC_Type.__name__ = "Integer32"
_Rsw1000bvalueRFDataCRC_Object = MibTableColumn
rsw1000bvalueRFDataCRC = _Rsw1000bvalueRFDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 12),
    _Rsw1000bvalueRFDataCRC_Type()
)
rsw1000bvalueRFDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvalueRFDataCRC.setStatus("mandatory")


class _Rsw1000bstateflagRFDataCRC_Type(Integer32):
    """Custom type rsw1000bstateflagRFDataCRC based on Integer32"""
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


_Rsw1000bstateflagRFDataCRC_Type.__name__ = "Integer32"
_Rsw1000bstateflagRFDataCRC_Object = MibTableColumn
rsw1000bstateflagRFDataCRC = _Rsw1000bstateflagRFDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 13),
    _Rsw1000bstateflagRFDataCRC_Type()
)
rsw1000bstateflagRFDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagRFDataCRC.setStatus("mandatory")


class _Rsw1000blabelAlarmDataCRC_Type(DisplayString):
    """Custom type rsw1000blabelAlarmDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelAlarmDataCRC_Type.__name__ = "DisplayString"
_Rsw1000blabelAlarmDataCRC_Object = MibTableColumn
rsw1000blabelAlarmDataCRC = _Rsw1000blabelAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 14),
    _Rsw1000blabelAlarmDataCRC_Type()
)
rsw1000blabelAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelAlarmDataCRC.setStatus("optional")


class _Rsw1000bvalueAlarmDataCRC_Type(Integer32):
    """Custom type rsw1000bvalueAlarmDataCRC based on Integer32"""
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


_Rsw1000bvalueAlarmDataCRC_Type.__name__ = "Integer32"
_Rsw1000bvalueAlarmDataCRC_Object = MibTableColumn
rsw1000bvalueAlarmDataCRC = _Rsw1000bvalueAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 15),
    _Rsw1000bvalueAlarmDataCRC_Type()
)
rsw1000bvalueAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvalueAlarmDataCRC.setStatus("mandatory")


class _Rsw1000bstateflagAlarmDataCRC_Type(Integer32):
    """Custom type rsw1000bstateflagAlarmDataCRC based on Integer32"""
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


_Rsw1000bstateflagAlarmDataCRC_Type.__name__ = "Integer32"
_Rsw1000bstateflagAlarmDataCRC_Object = MibTableColumn
rsw1000bstateflagAlarmDataCRC = _Rsw1000bstateflagAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 16),
    _Rsw1000bstateflagAlarmDataCRC_Type()
)
rsw1000bstateflagAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagAlarmDataCRC.setStatus("mandatory")


class _Rsw1000blabelRFSignalStatus_Type(DisplayString):
    """Custom type rsw1000blabelRFSignalStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelRFSignalStatus_Type.__name__ = "DisplayString"
_Rsw1000blabelRFSignalStatus_Object = MibTableColumn
rsw1000blabelRFSignalStatus = _Rsw1000blabelRFSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 17),
    _Rsw1000blabelRFSignalStatus_Type()
)
rsw1000blabelRFSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelRFSignalStatus.setStatus("optional")


class _Rsw1000bvalueRFSignalStatus_Type(Integer32):
    """Custom type rsw1000bvalueRFSignalStatus based on Integer32"""
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


_Rsw1000bvalueRFSignalStatus_Type.__name__ = "Integer32"
_Rsw1000bvalueRFSignalStatus_Object = MibTableColumn
rsw1000bvalueRFSignalStatus = _Rsw1000bvalueRFSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 18),
    _Rsw1000bvalueRFSignalStatus_Type()
)
rsw1000bvalueRFSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvalueRFSignalStatus.setStatus("mandatory")


class _Rsw1000bstateflagRFSignalStatus_Type(Integer32):
    """Custom type rsw1000bstateflagRFSignalStatus based on Integer32"""
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


_Rsw1000bstateflagRFSignalStatus_Type.__name__ = "Integer32"
_Rsw1000bstateflagRFSignalStatus_Object = MibTableColumn
rsw1000bstateflagRFSignalStatus = _Rsw1000bstateflagRFSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 19),
    _Rsw1000bstateflagRFSignalStatus_Type()
)
rsw1000bstateflagRFSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagRFSignalStatus.setStatus("mandatory")


class _Rsw1000blabelPriActiveStatus_Type(DisplayString):
    """Custom type rsw1000blabelPriActiveStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000blabelPriActiveStatus_Type.__name__ = "DisplayString"
_Rsw1000blabelPriActiveStatus_Object = MibTableColumn
rsw1000blabelPriActiveStatus = _Rsw1000blabelPriActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 20),
    _Rsw1000blabelPriActiveStatus_Type()
)
rsw1000blabelPriActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000blabelPriActiveStatus.setStatus("optional")


class _Rsw1000bvaluePriActiveStatus_Type(Integer32):
    """Custom type rsw1000bvaluePriActiveStatus based on Integer32"""
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


_Rsw1000bvaluePriActiveStatus_Type.__name__ = "Integer32"
_Rsw1000bvaluePriActiveStatus_Object = MibTableColumn
rsw1000bvaluePriActiveStatus = _Rsw1000bvaluePriActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 21),
    _Rsw1000bvaluePriActiveStatus_Type()
)
rsw1000bvaluePriActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bvaluePriActiveStatus.setStatus("mandatory")


class _Rsw1000bstateflagPriActiveStatus_Type(Integer32):
    """Custom type rsw1000bstateflagPriActiveStatus based on Integer32"""
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


_Rsw1000bstateflagPriActiveStatus_Type.__name__ = "Integer32"
_Rsw1000bstateflagPriActiveStatus_Object = MibTableColumn
rsw1000bstateflagPriActiveStatus = _Rsw1000bstateflagPriActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 4, 3, 22),
    _Rsw1000bstateflagPriActiveStatus_Type()
)
rsw1000bstateflagPriActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bstateflagPriActiveStatus.setStatus("mandatory")
_Gx2Rsw1000bFactoryTable_Object = MibTable
gx2Rsw1000bFactoryTable = _Gx2Rsw1000bFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5)
)
if mibBuilder.loadTexts:
    gx2Rsw1000bFactoryTable.setStatus("mandatory")
_Gx2Rsw1000bFactoryEntry_Object = MibTableRow
gx2Rsw1000bFactoryEntry = _Gx2Rsw1000bFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4)
)
gx2Rsw1000bFactoryEntry.setIndexNames(
    (0, "OMNI-gx2RSW1000B-MIB", "gx2Rsw1000bFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw1000bFactoryEntry.setStatus("mandatory")


class _Gx2Rsw1000bFactoryTableIndex_Type(Integer32):
    """Custom type gx2Rsw1000bFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2Rsw1000bFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2Rsw1000bFactoryTableIndex_Object = MibTableColumn
gx2Rsw1000bFactoryTableIndex = _Gx2Rsw1000bFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 1),
    _Gx2Rsw1000bFactoryTableIndex_Type()
)
gx2Rsw1000bFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Rsw1000bFactoryTableIndex.setStatus("mandatory")
_Rsw1000bbootControlByte_Type = Integer32
_Rsw1000bbootControlByte_Object = MibTableColumn
rsw1000bbootControlByte = _Rsw1000bbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 2),
    _Rsw1000bbootControlByte_Type()
)
rsw1000bbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bbootControlByte.setStatus("mandatory")
_Rsw1000bbootStatusByte_Type = Integer32
_Rsw1000bbootStatusByte_Object = MibTableColumn
rsw1000bbootStatusByte = _Rsw1000bbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 3),
    _Rsw1000bbootStatusByte_Type()
)
rsw1000bbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bbootStatusByte.setStatus("mandatory")
_Rsw1000bbank0CRC_Type = Integer32
_Rsw1000bbank0CRC_Object = MibTableColumn
rsw1000bbank0CRC = _Rsw1000bbank0CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 4),
    _Rsw1000bbank0CRC_Type()
)
rsw1000bbank0CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bbank0CRC.setStatus("mandatory")
_Rsw1000bbank1CRC_Type = Integer32
_Rsw1000bbank1CRC_Object = MibTableColumn
rsw1000bbank1CRC = _Rsw1000bbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 5),
    _Rsw1000bbank1CRC_Type()
)
rsw1000bbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bbank1CRC.setStatus("mandatory")
_Rsw1000bprgEEPROMByte_Type = Integer32
_Rsw1000bprgEEPROMByte_Object = MibTableColumn
rsw1000bprgEEPROMByte = _Rsw1000bprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 6),
    _Rsw1000bprgEEPROMByte_Type()
)
rsw1000bprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bprgEEPROMByte.setStatus("mandatory")
_Rsw1000bfactoryCRC_Type = Integer32
_Rsw1000bfactoryCRC_Object = MibTableColumn
rsw1000bfactoryCRC = _Rsw1000bfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 7),
    _Rsw1000bfactoryCRC_Type()
)
rsw1000bfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bfactoryCRC.setStatus("mandatory")


class _Rsw1000bcalculateCRC_Type(Integer32):
    """Custom type rsw1000bcalculateCRC based on Integer32"""
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
          ("rf", 2))
    )


_Rsw1000bcalculateCRC_Type.__name__ = "Integer32"
_Rsw1000bcalculateCRC_Object = MibTableColumn
rsw1000bcalculateCRC = _Rsw1000bcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 8),
    _Rsw1000bcalculateCRC_Type()
)
rsw1000bcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bcalculateCRC.setStatus("mandatory")
_Rsw1000bhourMeter_Type = Integer32
_Rsw1000bhourMeter_Object = MibTableColumn
rsw1000bhourMeter = _Rsw1000bhourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 9),
    _Rsw1000bhourMeter_Type()
)
rsw1000bhourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bhourMeter.setStatus("mandatory")
_Rsw1000bflashPrgCnt0_Type = Integer32
_Rsw1000bflashPrgCnt0_Object = MibTableColumn
rsw1000bflashPrgCnt0 = _Rsw1000bflashPrgCnt0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 10),
    _Rsw1000bflashPrgCnt0_Type()
)
rsw1000bflashPrgCnt0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bflashPrgCnt0.setStatus("mandatory")
_Rsw1000bflashPrgCnt1_Type = Integer32
_Rsw1000bflashPrgCnt1_Object = MibTableColumn
rsw1000bflashPrgCnt1 = _Rsw1000bflashPrgCnt1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 11),
    _Rsw1000bflashPrgCnt1_Type()
)
rsw1000bflashPrgCnt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bflashPrgCnt1.setStatus("mandatory")


class _Rsw1000bflashBank0Rev_Type(DisplayString):
    """Custom type rsw1000bflashBank0Rev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000bflashBank0Rev_Type.__name__ = "DisplayString"
_Rsw1000bflashBank0Rev_Object = MibTableColumn
rsw1000bflashBank0Rev = _Rsw1000bflashBank0Rev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 12),
    _Rsw1000bflashBank0Rev_Type()
)
rsw1000bflashBank0Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bflashBank0Rev.setStatus("mandatory")


class _Rsw1000bflashBank1Rev_Type(DisplayString):
    """Custom type rsw1000bflashBank1Rev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000bflashBank1Rev_Type.__name__ = "DisplayString"
_Rsw1000bflashBank1Rev_Object = MibTableColumn
rsw1000bflashBank1Rev = _Rsw1000bflashBank1Rev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 13),
    _Rsw1000bflashBank1Rev_Type()
)
rsw1000bflashBank1Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bflashBank1Rev.setStatus("mandatory")


class _Rsw1000bSubagentRev_Type(DisplayString):
    """Custom type rsw1000bSubagentRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Rsw1000bSubagentRev_Type.__name__ = "DisplayString"
_Rsw1000bSubagentRev_Object = MibTableColumn
rsw1000bSubagentRev = _Rsw1000bSubagentRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 5, 4, 14),
    _Rsw1000bSubagentRev_Type()
)
rsw1000bSubagentRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsw1000bSubagentRev.setStatus("mandatory")
_Gx2Rsw1000bHoldTimeTable_Object = MibTable
gx2Rsw1000bHoldTimeTable = _Gx2Rsw1000bHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 6)
)
if mibBuilder.loadTexts:
    gx2Rsw1000bHoldTimeTable.setStatus("mandatory")
_Gx2Rsw1000bHoldTimeEntry_Object = MibTableRow
gx2Rsw1000bHoldTimeEntry = _Gx2Rsw1000bHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 6, 5)
)
gx2Rsw1000bHoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2RSW1000B-MIB", "rxgx2Rsw1000bHoldTimeTableIndex"),
    (0, "OMNI-gx2RSW1000B-MIB", "rxgx2Rsw1000bHoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Rsw1000bHoldTimeEntry.setStatus("mandatory")


class _Rxgx2Rsw1000bHoldTimeTableIndex_Type(Integer32):
    """Custom type rxgx2Rsw1000bHoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rsw1000bHoldTimeTableIndex_Type.__name__ = "Integer32"
_Rxgx2Rsw1000bHoldTimeTableIndex_Object = MibTableColumn
rxgx2Rsw1000bHoldTimeTableIndex = _Rxgx2Rsw1000bHoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 6, 5, 1),
    _Rxgx2Rsw1000bHoldTimeTableIndex_Type()
)
rxgx2Rsw1000bHoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rsw1000bHoldTimeTableIndex.setStatus("mandatory")


class _Rxgx2Rsw1000bHoldTimeSpecIndex_Type(Integer32):
    """Custom type rxgx2Rsw1000bHoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Rxgx2Rsw1000bHoldTimeSpecIndex_Type.__name__ = "Integer32"
_Rxgx2Rsw1000bHoldTimeSpecIndex_Object = MibTableColumn
rxgx2Rsw1000bHoldTimeSpecIndex = _Rxgx2Rsw1000bHoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 6, 5, 2),
    _Rxgx2Rsw1000bHoldTimeSpecIndex_Type()
)
rxgx2Rsw1000bHoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxgx2Rsw1000bHoldTimeSpecIndex.setStatus("mandatory")
_Rxgx2Rsw1000bHoldTimeData_Type = Integer32
_Rxgx2Rsw1000bHoldTimeData_Object = MibTableColumn
rxgx2Rsw1000bHoldTimeData = _Rxgx2Rsw1000bHoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 6, 5, 3),
    _Rxgx2Rsw1000bHoldTimeData_Type()
)
rxgx2Rsw1000bHoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxgx2Rsw1000bHoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapRSW1000bConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 1)
)
trapRSW1000bConfigChangeInteger.setObjects(
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
    trapRSW1000bConfigChangeInteger.setStatus(
        ""
    )

trapRSW1000bConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 2)
)
trapRSW1000bConfigChangeDisplayString.setObjects(
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
    trapRSW1000bConfigChangeDisplayString.setStatus(
        ""
    )

trapRSW1000bRFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 3)
)
trapRSW1000bRFInputAlarm.setObjects(
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
    trapRSW1000bRFInputAlarm.setStatus(
        ""
    )

trapRSW1000bFanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 4)
)
trapRSW1000bFanCurrentAlarm.setObjects(
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
    trapRSW1000bFanCurrentAlarm.setStatus(
        ""
    )

trapRSW1000bModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 5)
)
trapRSW1000bModuleTempAlarm.setObjects(
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
    trapRSW1000bModuleTempAlarm.setStatus(
        ""
    )

trapRSW1000bFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 6)
)
trapRSW1000bFlashAlarm.setObjects(
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
    trapRSW1000bFlashAlarm.setStatus(
        ""
    )

trapRSW1000bBankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 7)
)
trapRSW1000bBankBootAlarm.setObjects(
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
    trapRSW1000bBankBootAlarm.setStatus(
        ""
    )

trapRSW1000bAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 8)
)
trapRSW1000bAlarmDataCRCAlarm.setObjects(
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
    trapRSW1000bAlarmDataCRCAlarm.setStatus(
        ""
    )

trapRSW1000bFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 9)
)
trapRSW1000bFactoryDataCRCAlarm.setObjects(
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
    trapRSW1000bFactoryDataCRCAlarm.setStatus(
        ""
    )

trapRSW1000bInputSwitchedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 10)
)
trapRSW1000bInputSwitchedAlarm.setObjects(
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
    trapRSW1000bInputSwitchedAlarm.setStatus(
        ""
    )

trapRSW1000bResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 11)
)
trapRSW1000bResetFactoryDefaultAlarm.setObjects(
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
    trapRSW1000bResetFactoryDefaultAlarm.setStatus(
        ""
    )

trapRSW1000bSecondaryInputActiveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 12)
)
trapRSW1000bSecondaryInputActiveAlarm.setObjects(
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
    trapRSW1000bSecondaryInputActiveAlarm.setStatus(
        ""
    )

trapRSW1000bCalibrationDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18, 0, 13)
)
trapRSW1000bCalibrationDataCRCAlarm.setObjects(
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
    trapRSW1000bCalibrationDataCRCAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2RSW1000B-MIB",
    **{"Float": Float,
       "trapRSW1000bConfigChangeInteger": trapRSW1000bConfigChangeInteger,
       "trapRSW1000bConfigChangeDisplayString": trapRSW1000bConfigChangeDisplayString,
       "trapRSW1000bRFInputAlarm": trapRSW1000bRFInputAlarm,
       "trapRSW1000bFanCurrentAlarm": trapRSW1000bFanCurrentAlarm,
       "trapRSW1000bModuleTempAlarm": trapRSW1000bModuleTempAlarm,
       "trapRSW1000bFlashAlarm": trapRSW1000bFlashAlarm,
       "trapRSW1000bBankBootAlarm": trapRSW1000bBankBootAlarm,
       "trapRSW1000bAlarmDataCRCAlarm": trapRSW1000bAlarmDataCRCAlarm,
       "trapRSW1000bFactoryDataCRCAlarm": trapRSW1000bFactoryDataCRCAlarm,
       "trapRSW1000bInputSwitchedAlarm": trapRSW1000bInputSwitchedAlarm,
       "trapRSW1000bResetFactoryDefaultAlarm": trapRSW1000bResetFactoryDefaultAlarm,
       "trapRSW1000bSecondaryInputActiveAlarm": trapRSW1000bSecondaryInputActiveAlarm,
       "trapRSW1000bCalibrationDataCRCAlarm": trapRSW1000bCalibrationDataCRCAlarm,
       "gx2Rsw1000bDescriptor": gx2Rsw1000bDescriptor,
       "gx2Rsw1000bAnalogTable": gx2Rsw1000bAnalogTable,
       "gx2Rsw1000bAnalogEntry": gx2Rsw1000bAnalogEntry,
       "gx2Rsw1000bAnalogTableIndex": gx2Rsw1000bAnalogTableIndex,
       "rsw1000blabelPriRFInputLvl": rsw1000blabelPriRFInputLvl,
       "rsw1000buomPriRFInputLvl": rsw1000buomPriRFInputLvl,
       "rsw1000bmajorHighPriRFInputLvl": rsw1000bmajorHighPriRFInputLvl,
       "rsw1000bmajorLowPriRFInputLvl": rsw1000bmajorLowPriRFInputLvl,
       "rsw1000bminorHighPriRFInputLvl": rsw1000bminorHighPriRFInputLvl,
       "rsw1000bminorLowPriRFInputLvl": rsw1000bminorLowPriRFInputLvl,
       "rsw1000bcurrentValuePriRFInputLvl": rsw1000bcurrentValuePriRFInputLvl,
       "rsw1000bstateFlagPriRFInputLvl": rsw1000bstateFlagPriRFInputLvl,
       "rsw1000bminValuePriRFInputLvl": rsw1000bminValuePriRFInputLvl,
       "rsw1000bmaxValuePriRFInputLvl": rsw1000bmaxValuePriRFInputLvl,
       "rsw1000balarmStatePriRFInputLvl": rsw1000balarmStatePriRFInputLvl,
       "rsw1000blabelSecRFInputLvl": rsw1000blabelSecRFInputLvl,
       "rsw1000buomSecRFInputLvl": rsw1000buomSecRFInputLvl,
       "rsw1000bmajorHighSecRFInputLvl": rsw1000bmajorHighSecRFInputLvl,
       "rsw1000bmajorLowSecRFInputLvl": rsw1000bmajorLowSecRFInputLvl,
       "rsw1000bminorHighSecRFInputLvl": rsw1000bminorHighSecRFInputLvl,
       "rsw1000bminorLowSecRFInputLvl": rsw1000bminorLowSecRFInputLvl,
       "rsw1000bcurrentValueSecRFInputLvl": rsw1000bcurrentValueSecRFInputLvl,
       "rsw1000bstateFlagSecRFInputLvl": rsw1000bstateFlagSecRFInputLvl,
       "rsw1000bminValueSecRFInputLvl": rsw1000bminValueSecRFInputLvl,
       "rsw1000bmaxValueSecRFInputLvl": rsw1000bmaxValueSecRFInputLvl,
       "rsw1000balarmStateSecRFInputLvl": rsw1000balarmStateSecRFInputLvl,
       "rsw1000blabelPriRFThreshold": rsw1000blabelPriRFThreshold,
       "rsw1000buomPriRFThreshold": rsw1000buomPriRFThreshold,
       "rsw1000bmajorHighPriRFThreshold": rsw1000bmajorHighPriRFThreshold,
       "rsw1000bmajorLowPriRFThreshold": rsw1000bmajorLowPriRFThreshold,
       "rsw1000bminorHighPriRFThreshold": rsw1000bminorHighPriRFThreshold,
       "rsw1000bminorLowPriRFThreshold": rsw1000bminorLowPriRFThreshold,
       "rsw1000bcurrentValuePriRFThreshold": rsw1000bcurrentValuePriRFThreshold,
       "rsw1000bstateFlagPriRFThreshold": rsw1000bstateFlagPriRFThreshold,
       "rsw1000bminValuePriRFThreshold": rsw1000bminValuePriRFThreshold,
       "rsw1000bmaxValuePriRFThreshold": rsw1000bmaxValuePriRFThreshold,
       "rsw1000balarmStatePriRFThreshold": rsw1000balarmStatePriRFThreshold,
       "rsw1000blabelSecRFThreshold": rsw1000blabelSecRFThreshold,
       "rsw1000buomSecRFThreshold": rsw1000buomSecRFThreshold,
       "rsw1000bmajorHighSecRFThreshold": rsw1000bmajorHighSecRFThreshold,
       "rsw1000bmajorLowSecRFThreshold": rsw1000bmajorLowSecRFThreshold,
       "rsw1000bminorHighSecRFThreshold": rsw1000bminorHighSecRFThreshold,
       "rsw1000bminorLowSecRFThreshold": rsw1000bminorLowSecRFThreshold,
       "rsw1000bcurrentValueSecRFThreshold": rsw1000bcurrentValueSecRFThreshold,
       "rsw1000bstateFlagSecRFThreshold": rsw1000bstateFlagSecRFThreshold,
       "rsw1000bminValueSecRFThreshold": rsw1000bminValueSecRFThreshold,
       "rsw1000bmaxValueSecRFThreshold": rsw1000bmaxValueSecRFThreshold,
       "rsw1000balarmStateSecRFThreshold": rsw1000balarmStateSecRFThreshold,
       "rsw1000blabelModTemp": rsw1000blabelModTemp,
       "rsw1000buomModTemp": rsw1000buomModTemp,
       "rsw1000bmajorHighModTemp": rsw1000bmajorHighModTemp,
       "rsw1000bmajorLowModTemp": rsw1000bmajorLowModTemp,
       "rsw1000bminorHighModTemp": rsw1000bminorHighModTemp,
       "rsw1000bminorLowModTemp": rsw1000bminorLowModTemp,
       "rsw1000bcurrentValueModTemp": rsw1000bcurrentValueModTemp,
       "rsw1000bstateFlagModTemp": rsw1000bstateFlagModTemp,
       "rsw1000bminValueModTemp": rsw1000bminValueModTemp,
       "rsw1000bmaxValueModTemp": rsw1000bmaxValueModTemp,
       "rsw1000balarmStateModTemp": rsw1000balarmStateModTemp,
       "rsw1000blabelFanCurrent": rsw1000blabelFanCurrent,
       "rsw1000buomFanCurrent": rsw1000buomFanCurrent,
       "rsw1000bmajorHighFanCurrent": rsw1000bmajorHighFanCurrent,
       "rsw1000bmajorLowFanCurrent": rsw1000bmajorLowFanCurrent,
       "rsw1000bminorHighFanCurrent": rsw1000bminorHighFanCurrent,
       "rsw1000bminorLowFanCurrent": rsw1000bminorLowFanCurrent,
       "rsw1000bcurrentValueFanCurrent": rsw1000bcurrentValueFanCurrent,
       "rsw1000bstateFlagFanCurrent": rsw1000bstateFlagFanCurrent,
       "rsw1000bminValueFanCurrent": rsw1000bminValueFanCurrent,
       "rsw1000bmaxValueFanCurrent": rsw1000bmaxValueFanCurrent,
       "rsw1000balarmStateFanCurrent": rsw1000balarmStateFanCurrent,
       "gx2Rsw1000bDigitalTable": gx2Rsw1000bDigitalTable,
       "gx2Rsw1000bDigitalEntry": gx2Rsw1000bDigitalEntry,
       "gx2Rsw1000bDigitalTableIndex": gx2Rsw1000bDigitalTableIndex,
       "rsw1000blabelSwitchControl": rsw1000blabelSwitchControl,
       "rsw1000benumSwitchControl": rsw1000benumSwitchControl,
       "rsw1000bvalueSwitchControl": rsw1000bvalueSwitchControl,
       "rsw1000bstateflagSwitchControl": rsw1000bstateflagSwitchControl,
       "rsw1000blabelSwitchMode": rsw1000blabelSwitchMode,
       "rsw1000benumSwitchMode": rsw1000benumSwitchMode,
       "rsw1000bvalueSwitchMode": rsw1000bvalueSwitchMode,
       "rsw1000bstateflagSwitchMode": rsw1000bstateflagSwitchMode,
       "rsw1000blabelRevertEnable": rsw1000blabelRevertEnable,
       "rsw1000benumRevertEnable": rsw1000benumRevertEnable,
       "rsw1000bvalueRevertEnable": rsw1000bvalueRevertEnable,
       "rsw1000bstateflagRevertEnable": rsw1000bstateflagRevertEnable,
       "rsw1000blabelRevertTime": rsw1000blabelRevertTime,
       "rsw1000benumRevertTime": rsw1000benumRevertTime,
       "rsw1000bvalueRevertTime": rsw1000bvalueRevertTime,
       "rsw1000bstateflagRevertTime": rsw1000bstateflagRevertTime,
       "rsw1000blabelSensorMode": rsw1000blabelSensorMode,
       "rsw1000benumSensorMode": rsw1000benumSensorMode,
       "rsw1000bvalueSensorMode": rsw1000bvalueSensorMode,
       "rsw1000bstateflagSensorMode": rsw1000bstateflagSensorMode,
       "rsw1000blabelSwitchMonitor": rsw1000blabelSwitchMonitor,
       "rsw1000benumSwitchMonitor": rsw1000benumSwitchMonitor,
       "rsw1000bvalueSwitchMonitor": rsw1000bvalueSwitchMonitor,
       "rsw1000bstateflagSwitchMonitor": rsw1000bstateflagSwitchMonitor,
       "rsw1000blabelPriStatusSig": rsw1000blabelPriStatusSig,
       "rsw1000benumPriStatusSig": rsw1000benumPriStatusSig,
       "rsw1000bvaluePriStatusSig": rsw1000bvaluePriStatusSig,
       "rsw1000bstateflagPriStatusSig": rsw1000bstateflagPriStatusSig,
       "rsw1000blabelSecStatusSig": rsw1000blabelSecStatusSig,
       "rsw1000benumSecStatusSig": rsw1000benumSecStatusSig,
       "rsw1000bvalueSecStatusSig": rsw1000bvalueSecStatusSig,
       "rsw1000bstateflagSecStatusSig": rsw1000bstateflagSecStatusSig,
       "rsw1000blabelFactoryDefault": rsw1000blabelFactoryDefault,
       "rsw1000benumFactoryDefault": rsw1000benumFactoryDefault,
       "rsw1000bvalueFactoryDefault": rsw1000bvalueFactoryDefault,
       "rsw1000bstateflagFactoryDefault": rsw1000bstateflagFactoryDefault,
       "gx2Rsw1000bStatusTable": gx2Rsw1000bStatusTable,
       "gx2Rsw1000bStatusEntry": gx2Rsw1000bStatusEntry,
       "gx2Rsw1000bStatusTableIndex": gx2Rsw1000bStatusTableIndex,
       "rsw1000blabelBoot": rsw1000blabelBoot,
       "rsw1000bvalueBoot": rsw1000bvalueBoot,
       "rsw1000bstateflagBoot": rsw1000bstateflagBoot,
       "rsw1000blabelFlash": rsw1000blabelFlash,
       "rsw1000bvalueFlash": rsw1000bvalueFlash,
       "rsw1000bstateflagFlash": rsw1000bstateflagFlash,
       "rsw1000blabelFactoryDataCRC": rsw1000blabelFactoryDataCRC,
       "rsw1000bvalueFactoryDataCRC": rsw1000bvalueFactoryDataCRC,
       "rsw1000bstateflagFactoryDataCRC": rsw1000bstateflagFactoryDataCRC,
       "rsw1000blabelRFDataCRC": rsw1000blabelRFDataCRC,
       "rsw1000bvalueRFDataCRC": rsw1000bvalueRFDataCRC,
       "rsw1000bstateflagRFDataCRC": rsw1000bstateflagRFDataCRC,
       "rsw1000blabelAlarmDataCRC": rsw1000blabelAlarmDataCRC,
       "rsw1000bvalueAlarmDataCRC": rsw1000bvalueAlarmDataCRC,
       "rsw1000bstateflagAlarmDataCRC": rsw1000bstateflagAlarmDataCRC,
       "rsw1000blabelRFSignalStatus": rsw1000blabelRFSignalStatus,
       "rsw1000bvalueRFSignalStatus": rsw1000bvalueRFSignalStatus,
       "rsw1000bstateflagRFSignalStatus": rsw1000bstateflagRFSignalStatus,
       "rsw1000blabelPriActiveStatus": rsw1000blabelPriActiveStatus,
       "rsw1000bvaluePriActiveStatus": rsw1000bvaluePriActiveStatus,
       "rsw1000bstateflagPriActiveStatus": rsw1000bstateflagPriActiveStatus,
       "gx2Rsw1000bFactoryTable": gx2Rsw1000bFactoryTable,
       "gx2Rsw1000bFactoryEntry": gx2Rsw1000bFactoryEntry,
       "gx2Rsw1000bFactoryTableIndex": gx2Rsw1000bFactoryTableIndex,
       "rsw1000bbootControlByte": rsw1000bbootControlByte,
       "rsw1000bbootStatusByte": rsw1000bbootStatusByte,
       "rsw1000bbank0CRC": rsw1000bbank0CRC,
       "rsw1000bbank1CRC": rsw1000bbank1CRC,
       "rsw1000bprgEEPROMByte": rsw1000bprgEEPROMByte,
       "rsw1000bfactoryCRC": rsw1000bfactoryCRC,
       "rsw1000bcalculateCRC": rsw1000bcalculateCRC,
       "rsw1000bhourMeter": rsw1000bhourMeter,
       "rsw1000bflashPrgCnt0": rsw1000bflashPrgCnt0,
       "rsw1000bflashPrgCnt1": rsw1000bflashPrgCnt1,
       "rsw1000bflashBank0Rev": rsw1000bflashBank0Rev,
       "rsw1000bflashBank1Rev": rsw1000bflashBank1Rev,
       "rsw1000bSubagentRev": rsw1000bSubagentRev,
       "gx2Rsw1000bHoldTimeTable": gx2Rsw1000bHoldTimeTable,
       "gx2Rsw1000bHoldTimeEntry": gx2Rsw1000bHoldTimeEntry,
       "rxgx2Rsw1000bHoldTimeTableIndex": rxgx2Rsw1000bHoldTimeTableIndex,
       "rxgx2Rsw1000bHoldTimeSpecIndex": rxgx2Rsw1000bHoldTimeSpecIndex,
       "rxgx2Rsw1000bHoldTimeData": rxgx2Rsw1000bHoldTimeData}
)
