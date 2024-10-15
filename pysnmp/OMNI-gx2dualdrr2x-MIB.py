# SNMP MIB module (OMNI-gx2dualdrr2x-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2dualdrr2x-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:39 2024
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

(gx2DualDrr2x,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2DualDrr2x")

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

_Gx2dualdrr2xDescriptor_ObjectIdentity = ObjectIdentity
gx2dualdrr2xDescriptor = _Gx2dualdrr2xDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 1)
)
_Gx2dualdrr2xAnalogTable_Object = MibTable
gx2dualdrr2xAnalogTable = _Gx2dualdrr2xAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2)
)
if mibBuilder.loadTexts:
    gx2dualdrr2xAnalogTable.setStatus("mandatory")
_Gx2dualdrr2xAnalogEntry_Object = MibTableRow
gx2dualdrr2xAnalogEntry = _Gx2dualdrr2xAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1)
)
gx2dualdrr2xAnalogEntry.setIndexNames(
    (0, "OMNI-gx2dualdrr2x-MIB", "gx2dualdrr2xAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2dualdrr2xAnalogEntry.setStatus("mandatory")


class _Gx2dualdrr2xAnalogTableIndex_Type(Integer32):
    """Custom type gx2dualdrr2xAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2dualdrr2xAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2dualdrr2xAnalogTableIndex_Object = MibTableColumn
gx2dualdrr2xAnalogTableIndex = _Gx2dualdrr2xAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 1),
    _Gx2dualdrr2xAnalogTableIndex_Type()
)
gx2dualdrr2xAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2dualdrr2xAnalogTableIndex.setStatus("mandatory")


class _Dualdrr2xlabelRecdOptPwr1_Type(DisplayString):
    """Custom type dualdrr2xlabelRecdOptPwr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelRecdOptPwr1_Type.__name__ = "DisplayString"
_Dualdrr2xlabelRecdOptPwr1_Object = MibTableColumn
dualdrr2xlabelRecdOptPwr1 = _Dualdrr2xlabelRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 2),
    _Dualdrr2xlabelRecdOptPwr1_Type()
)
dualdrr2xlabelRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelRecdOptPwr1.setStatus("optional")


class _Dualdrr2xuomRecdOptPwr1_Type(DisplayString):
    """Custom type dualdrr2xuomRecdOptPwr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomRecdOptPwr1_Type.__name__ = "DisplayString"
_Dualdrr2xuomRecdOptPwr1_Object = MibTableColumn
dualdrr2xuomRecdOptPwr1 = _Dualdrr2xuomRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 3),
    _Dualdrr2xuomRecdOptPwr1_Type()
)
dualdrr2xuomRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomRecdOptPwr1.setStatus("optional")
_Dualdrr2xmajorHighRecdOptPwr1_Type = Float
_Dualdrr2xmajorHighRecdOptPwr1_Object = MibTableColumn
dualdrr2xmajorHighRecdOptPwr1 = _Dualdrr2xmajorHighRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 4),
    _Dualdrr2xmajorHighRecdOptPwr1_Type()
)
dualdrr2xmajorHighRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighRecdOptPwr1.setStatus("obsolete")
_Dualdrr2xmajorLowRecdOptPwr1_Type = Float
_Dualdrr2xmajorLowRecdOptPwr1_Object = MibTableColumn
dualdrr2xmajorLowRecdOptPwr1 = _Dualdrr2xmajorLowRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 5),
    _Dualdrr2xmajorLowRecdOptPwr1_Type()
)
dualdrr2xmajorLowRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowRecdOptPwr1.setStatus("obsolete")
_Dualdrr2xminorHighRecdOptPwr1_Type = Float
_Dualdrr2xminorHighRecdOptPwr1_Object = MibTableColumn
dualdrr2xminorHighRecdOptPwr1 = _Dualdrr2xminorHighRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 6),
    _Dualdrr2xminorHighRecdOptPwr1_Type()
)
dualdrr2xminorHighRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighRecdOptPwr1.setStatus("obsolete")
_Dualdrr2xminorLowRecdOptPwr1_Type = Float
_Dualdrr2xminorLowRecdOptPwr1_Object = MibTableColumn
dualdrr2xminorLowRecdOptPwr1 = _Dualdrr2xminorLowRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 7),
    _Dualdrr2xminorLowRecdOptPwr1_Type()
)
dualdrr2xminorLowRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowRecdOptPwr1.setStatus("obsolete")
_Dualdrr2xcurrentValueRecdOptPwr1_Type = Float
_Dualdrr2xcurrentValueRecdOptPwr1_Object = MibTableColumn
dualdrr2xcurrentValueRecdOptPwr1 = _Dualdrr2xcurrentValueRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 8),
    _Dualdrr2xcurrentValueRecdOptPwr1_Type()
)
dualdrr2xcurrentValueRecdOptPwr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueRecdOptPwr1.setStatus("mandatory")


class _Dualdrr2xstateFlagRecdOptPwr1_Type(Integer32):
    """Custom type dualdrr2xstateFlagRecdOptPwr1 based on Integer32"""
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


_Dualdrr2xstateFlagRecdOptPwr1_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagRecdOptPwr1_Object = MibTableColumn
dualdrr2xstateFlagRecdOptPwr1 = _Dualdrr2xstateFlagRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 9),
    _Dualdrr2xstateFlagRecdOptPwr1_Type()
)
dualdrr2xstateFlagRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagRecdOptPwr1.setStatus("mandatory")
_Dualdrr2xminValueRecdOptPwr1_Type = Float
_Dualdrr2xminValueRecdOptPwr1_Object = MibTableColumn
dualdrr2xminValueRecdOptPwr1 = _Dualdrr2xminValueRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 10),
    _Dualdrr2xminValueRecdOptPwr1_Type()
)
dualdrr2xminValueRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueRecdOptPwr1.setStatus("mandatory")
_Dualdrr2xmaxValueRecdOptPwr1_Type = Float
_Dualdrr2xmaxValueRecdOptPwr1_Object = MibTableColumn
dualdrr2xmaxValueRecdOptPwr1 = _Dualdrr2xmaxValueRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 11),
    _Dualdrr2xmaxValueRecdOptPwr1_Type()
)
dualdrr2xmaxValueRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueRecdOptPwr1.setStatus("mandatory")


class _Dualdrr2xalarmStateRecdOptPwr1_Type(Integer32):
    """Custom type dualdrr2xalarmStateRecdOptPwr1 based on Integer32"""
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


_Dualdrr2xalarmStateRecdOptPwr1_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateRecdOptPwr1_Object = MibTableColumn
dualdrr2xalarmStateRecdOptPwr1 = _Dualdrr2xalarmStateRecdOptPwr1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 12),
    _Dualdrr2xalarmStateRecdOptPwr1_Type()
)
dualdrr2xalarmStateRecdOptPwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateRecdOptPwr1.setStatus("mandatory")


class _Dualdrr2xlabelRecdOptPwr2_Type(DisplayString):
    """Custom type dualdrr2xlabelRecdOptPwr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelRecdOptPwr2_Type.__name__ = "DisplayString"
_Dualdrr2xlabelRecdOptPwr2_Object = MibTableColumn
dualdrr2xlabelRecdOptPwr2 = _Dualdrr2xlabelRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 13),
    _Dualdrr2xlabelRecdOptPwr2_Type()
)
dualdrr2xlabelRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelRecdOptPwr2.setStatus("optional")


class _Dualdrr2xuomRecdOptPwr2_Type(DisplayString):
    """Custom type dualdrr2xuomRecdOptPwr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomRecdOptPwr2_Type.__name__ = "DisplayString"
_Dualdrr2xuomRecdOptPwr2_Object = MibTableColumn
dualdrr2xuomRecdOptPwr2 = _Dualdrr2xuomRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 14),
    _Dualdrr2xuomRecdOptPwr2_Type()
)
dualdrr2xuomRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomRecdOptPwr2.setStatus("optional")
_Dualdrr2xmajorHighRecdOptPwr2_Type = Float
_Dualdrr2xmajorHighRecdOptPwr2_Object = MibTableColumn
dualdrr2xmajorHighRecdOptPwr2 = _Dualdrr2xmajorHighRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 15),
    _Dualdrr2xmajorHighRecdOptPwr2_Type()
)
dualdrr2xmajorHighRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighRecdOptPwr2.setStatus("obsolete")
_Dualdrr2xmajorLowRecdOptPwr2_Type = Float
_Dualdrr2xmajorLowRecdOptPwr2_Object = MibTableColumn
dualdrr2xmajorLowRecdOptPwr2 = _Dualdrr2xmajorLowRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 16),
    _Dualdrr2xmajorLowRecdOptPwr2_Type()
)
dualdrr2xmajorLowRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowRecdOptPwr2.setStatus("obsolete")
_Dualdrr2xminorHighRecdOptPwr2_Type = Float
_Dualdrr2xminorHighRecdOptPwr2_Object = MibTableColumn
dualdrr2xminorHighRecdOptPwr2 = _Dualdrr2xminorHighRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 17),
    _Dualdrr2xminorHighRecdOptPwr2_Type()
)
dualdrr2xminorHighRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighRecdOptPwr2.setStatus("obsolete")
_Dualdrr2xminorLowRecdOptPwr2_Type = Float
_Dualdrr2xminorLowRecdOptPwr2_Object = MibTableColumn
dualdrr2xminorLowRecdOptPwr2 = _Dualdrr2xminorLowRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 18),
    _Dualdrr2xminorLowRecdOptPwr2_Type()
)
dualdrr2xminorLowRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowRecdOptPwr2.setStatus("obsolete")
_Dualdrr2xcurrentValueRecdOptPwr2_Type = Float
_Dualdrr2xcurrentValueRecdOptPwr2_Object = MibTableColumn
dualdrr2xcurrentValueRecdOptPwr2 = _Dualdrr2xcurrentValueRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 19),
    _Dualdrr2xcurrentValueRecdOptPwr2_Type()
)
dualdrr2xcurrentValueRecdOptPwr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueRecdOptPwr2.setStatus("mandatory")


class _Dualdrr2xstateFlagRecdOptPwr2_Type(Integer32):
    """Custom type dualdrr2xstateFlagRecdOptPwr2 based on Integer32"""
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


_Dualdrr2xstateFlagRecdOptPwr2_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagRecdOptPwr2_Object = MibTableColumn
dualdrr2xstateFlagRecdOptPwr2 = _Dualdrr2xstateFlagRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 20),
    _Dualdrr2xstateFlagRecdOptPwr2_Type()
)
dualdrr2xstateFlagRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagRecdOptPwr2.setStatus("mandatory")
_Dualdrr2xminValueRecdOptPwr2_Type = Float
_Dualdrr2xminValueRecdOptPwr2_Object = MibTableColumn
dualdrr2xminValueRecdOptPwr2 = _Dualdrr2xminValueRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 21),
    _Dualdrr2xminValueRecdOptPwr2_Type()
)
dualdrr2xminValueRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueRecdOptPwr2.setStatus("mandatory")
_Dualdrr2xmaxValueRecdOptPwr2_Type = Float
_Dualdrr2xmaxValueRecdOptPwr2_Object = MibTableColumn
dualdrr2xmaxValueRecdOptPwr2 = _Dualdrr2xmaxValueRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 22),
    _Dualdrr2xmaxValueRecdOptPwr2_Type()
)
dualdrr2xmaxValueRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueRecdOptPwr2.setStatus("mandatory")


class _Dualdrr2xalarmStateRecdOptPwr2_Type(Integer32):
    """Custom type dualdrr2xalarmStateRecdOptPwr2 based on Integer32"""
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


_Dualdrr2xalarmStateRecdOptPwr2_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateRecdOptPwr2_Object = MibTableColumn
dualdrr2xalarmStateRecdOptPwr2 = _Dualdrr2xalarmStateRecdOptPwr2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 23),
    _Dualdrr2xalarmStateRecdOptPwr2_Type()
)
dualdrr2xalarmStateRecdOptPwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateRecdOptPwr2.setStatus("mandatory")


class _Dualdrr2xlabelModTemp_Type(DisplayString):
    """Custom type dualdrr2xlabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelModTemp_Type.__name__ = "DisplayString"
_Dualdrr2xlabelModTemp_Object = MibTableColumn
dualdrr2xlabelModTemp = _Dualdrr2xlabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 24),
    _Dualdrr2xlabelModTemp_Type()
)
dualdrr2xlabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelModTemp.setStatus("optional")


class _Dualdrr2xuomModTemp_Type(DisplayString):
    """Custom type dualdrr2xuomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomModTemp_Type.__name__ = "DisplayString"
_Dualdrr2xuomModTemp_Object = MibTableColumn
dualdrr2xuomModTemp = _Dualdrr2xuomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 25),
    _Dualdrr2xuomModTemp_Type()
)
dualdrr2xuomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomModTemp.setStatus("optional")
_Dualdrr2xmajorHighModTemp_Type = Float
_Dualdrr2xmajorHighModTemp_Object = MibTableColumn
dualdrr2xmajorHighModTemp = _Dualdrr2xmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 26),
    _Dualdrr2xmajorHighModTemp_Type()
)
dualdrr2xmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighModTemp.setStatus("mandatory")
_Dualdrr2xmajorLowModTemp_Type = Float
_Dualdrr2xmajorLowModTemp_Object = MibTableColumn
dualdrr2xmajorLowModTemp = _Dualdrr2xmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 27),
    _Dualdrr2xmajorLowModTemp_Type()
)
dualdrr2xmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowModTemp.setStatus("mandatory")
_Dualdrr2xminorHighModTemp_Type = Float
_Dualdrr2xminorHighModTemp_Object = MibTableColumn
dualdrr2xminorHighModTemp = _Dualdrr2xminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 28),
    _Dualdrr2xminorHighModTemp_Type()
)
dualdrr2xminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighModTemp.setStatus("mandatory")
_Dualdrr2xminorLowModTemp_Type = Float
_Dualdrr2xminorLowModTemp_Object = MibTableColumn
dualdrr2xminorLowModTemp = _Dualdrr2xminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 29),
    _Dualdrr2xminorLowModTemp_Type()
)
dualdrr2xminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowModTemp.setStatus("mandatory")
_Dualdrr2xcurrentValueModTemp_Type = Float
_Dualdrr2xcurrentValueModTemp_Object = MibTableColumn
dualdrr2xcurrentValueModTemp = _Dualdrr2xcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 30),
    _Dualdrr2xcurrentValueModTemp_Type()
)
dualdrr2xcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueModTemp.setStatus("mandatory")


class _Dualdrr2xstateFlagModTemp_Type(Integer32):
    """Custom type dualdrr2xstateFlagModTemp based on Integer32"""
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


_Dualdrr2xstateFlagModTemp_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagModTemp_Object = MibTableColumn
dualdrr2xstateFlagModTemp = _Dualdrr2xstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 31),
    _Dualdrr2xstateFlagModTemp_Type()
)
dualdrr2xstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagModTemp.setStatus("mandatory")
_Dualdrr2xminValueModTemp_Type = Float
_Dualdrr2xminValueModTemp_Object = MibTableColumn
dualdrr2xminValueModTemp = _Dualdrr2xminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 32),
    _Dualdrr2xminValueModTemp_Type()
)
dualdrr2xminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueModTemp.setStatus("mandatory")
_Dualdrr2xmaxValueModTemp_Type = Float
_Dualdrr2xmaxValueModTemp_Object = MibTableColumn
dualdrr2xmaxValueModTemp = _Dualdrr2xmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 33),
    _Dualdrr2xmaxValueModTemp_Type()
)
dualdrr2xmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueModTemp.setStatus("mandatory")


class _Dualdrr2xalarmStateModTemp_Type(Integer32):
    """Custom type dualdrr2xalarmStateModTemp based on Integer32"""
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


_Dualdrr2xalarmStateModTemp_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateModTemp_Object = MibTableColumn
dualdrr2xalarmStateModTemp = _Dualdrr2xalarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 34),
    _Dualdrr2xalarmStateModTemp_Type()
)
dualdrr2xalarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateModTemp.setStatus("mandatory")


class _Dualdrr2xlabel12VCurrent_Type(DisplayString):
    """Custom type dualdrr2xlabel12VCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabel12VCurrent_Type.__name__ = "DisplayString"
_Dualdrr2xlabel12VCurrent_Object = MibTableColumn
dualdrr2xlabel12VCurrent = _Dualdrr2xlabel12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 35),
    _Dualdrr2xlabel12VCurrent_Type()
)
dualdrr2xlabel12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabel12VCurrent.setStatus("optional")


class _Dualdrr2xuom12VCurrent_Type(DisplayString):
    """Custom type dualdrr2xuom12VCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuom12VCurrent_Type.__name__ = "DisplayString"
_Dualdrr2xuom12VCurrent_Object = MibTableColumn
dualdrr2xuom12VCurrent = _Dualdrr2xuom12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 36),
    _Dualdrr2xuom12VCurrent_Type()
)
dualdrr2xuom12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuom12VCurrent.setStatus("optional")
_Dualdrr2xmajorHigh12VCurrent_Type = Float
_Dualdrr2xmajorHigh12VCurrent_Object = MibTableColumn
dualdrr2xmajorHigh12VCurrent = _Dualdrr2xmajorHigh12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 37),
    _Dualdrr2xmajorHigh12VCurrent_Type()
)
dualdrr2xmajorHigh12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHigh12VCurrent.setStatus("mandatory")
_Dualdrr2xmajorLow12VCurrent_Type = Float
_Dualdrr2xmajorLow12VCurrent_Object = MibTableColumn
dualdrr2xmajorLow12VCurrent = _Dualdrr2xmajorLow12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 38),
    _Dualdrr2xmajorLow12VCurrent_Type()
)
dualdrr2xmajorLow12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLow12VCurrent.setStatus("mandatory")
_Dualdrr2xminorHigh12VCurrent_Type = Float
_Dualdrr2xminorHigh12VCurrent_Object = MibTableColumn
dualdrr2xminorHigh12VCurrent = _Dualdrr2xminorHigh12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 39),
    _Dualdrr2xminorHigh12VCurrent_Type()
)
dualdrr2xminorHigh12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHigh12VCurrent.setStatus("mandatory")
_Dualdrr2xminorLow12VCurrent_Type = Float
_Dualdrr2xminorLow12VCurrent_Object = MibTableColumn
dualdrr2xminorLow12VCurrent = _Dualdrr2xminorLow12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 40),
    _Dualdrr2xminorLow12VCurrent_Type()
)
dualdrr2xminorLow12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLow12VCurrent.setStatus("mandatory")
_Dualdrr2xcurrentValue12VCurrent_Type = Float
_Dualdrr2xcurrentValue12VCurrent_Object = MibTableColumn
dualdrr2xcurrentValue12VCurrent = _Dualdrr2xcurrentValue12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 41),
    _Dualdrr2xcurrentValue12VCurrent_Type()
)
dualdrr2xcurrentValue12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValue12VCurrent.setStatus("mandatory")


class _Dualdrr2xstateFlag12VCurrent_Type(Integer32):
    """Custom type dualdrr2xstateFlag12VCurrent based on Integer32"""
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


_Dualdrr2xstateFlag12VCurrent_Type.__name__ = "Integer32"
_Dualdrr2xstateFlag12VCurrent_Object = MibTableColumn
dualdrr2xstateFlag12VCurrent = _Dualdrr2xstateFlag12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 42),
    _Dualdrr2xstateFlag12VCurrent_Type()
)
dualdrr2xstateFlag12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlag12VCurrent.setStatus("mandatory")
_Dualdrr2xminValue12VCurrent_Type = Float
_Dualdrr2xminValue12VCurrent_Object = MibTableColumn
dualdrr2xminValue12VCurrent = _Dualdrr2xminValue12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 43),
    _Dualdrr2xminValue12VCurrent_Type()
)
dualdrr2xminValue12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValue12VCurrent.setStatus("mandatory")
_Dualdrr2xmaxValue12VCurrent_Type = Float
_Dualdrr2xmaxValue12VCurrent_Object = MibTableColumn
dualdrr2xmaxValue12VCurrent = _Dualdrr2xmaxValue12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 44),
    _Dualdrr2xmaxValue12VCurrent_Type()
)
dualdrr2xmaxValue12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValue12VCurrent.setStatus("mandatory")


class _Dualdrr2xalarmState12VCurrent_Type(Integer32):
    """Custom type dualdrr2xalarmState12VCurrent based on Integer32"""
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


_Dualdrr2xalarmState12VCurrent_Type.__name__ = "Integer32"
_Dualdrr2xalarmState12VCurrent_Object = MibTableColumn
dualdrr2xalarmState12VCurrent = _Dualdrr2xalarmState12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 45),
    _Dualdrr2xalarmState12VCurrent_Type()
)
dualdrr2xalarmState12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmState12VCurrent.setStatus("mandatory")


class _Dualdrr2xlabelFanSpeed_Type(DisplayString):
    """Custom type dualdrr2xlabelFanSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelFanSpeed_Type.__name__ = "DisplayString"
_Dualdrr2xlabelFanSpeed_Object = MibTableColumn
dualdrr2xlabelFanSpeed = _Dualdrr2xlabelFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 46),
    _Dualdrr2xlabelFanSpeed_Type()
)
dualdrr2xlabelFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelFanSpeed.setStatus("optional")


class _Dualdrr2xuomFanSpeed_Type(DisplayString):
    """Custom type dualdrr2xuomFanSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomFanSpeed_Type.__name__ = "DisplayString"
_Dualdrr2xuomFanSpeed_Object = MibTableColumn
dualdrr2xuomFanSpeed = _Dualdrr2xuomFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 47),
    _Dualdrr2xuomFanSpeed_Type()
)
dualdrr2xuomFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomFanSpeed.setStatus("optional")
_Dualdrr2xmajorHighFanSpeed_Type = Float
_Dualdrr2xmajorHighFanSpeed_Object = MibTableColumn
dualdrr2xmajorHighFanSpeed = _Dualdrr2xmajorHighFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 48),
    _Dualdrr2xmajorHighFanSpeed_Type()
)
dualdrr2xmajorHighFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighFanSpeed.setStatus("mandatory")
_Dualdrr2xmajorLowFanSpeed_Type = Float
_Dualdrr2xmajorLowFanSpeed_Object = MibTableColumn
dualdrr2xmajorLowFanSpeed = _Dualdrr2xmajorLowFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 49),
    _Dualdrr2xmajorLowFanSpeed_Type()
)
dualdrr2xmajorLowFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowFanSpeed.setStatus("mandatory")
_Dualdrr2xminorHighFanSpeed_Type = Float
_Dualdrr2xminorHighFanSpeed_Object = MibTableColumn
dualdrr2xminorHighFanSpeed = _Dualdrr2xminorHighFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 50),
    _Dualdrr2xminorHighFanSpeed_Type()
)
dualdrr2xminorHighFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighFanSpeed.setStatus("obsolete")
_Dualdrr2xminorLowFanSpeed_Type = Float
_Dualdrr2xminorLowFanSpeed_Object = MibTableColumn
dualdrr2xminorLowFanSpeed = _Dualdrr2xminorLowFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 51),
    _Dualdrr2xminorLowFanSpeed_Type()
)
dualdrr2xminorLowFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowFanSpeed.setStatus("obsolete")
_Dualdrr2xcurrentValueFanSpeed_Type = Float
_Dualdrr2xcurrentValueFanSpeed_Object = MibTableColumn
dualdrr2xcurrentValueFanSpeed = _Dualdrr2xcurrentValueFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 52),
    _Dualdrr2xcurrentValueFanSpeed_Type()
)
dualdrr2xcurrentValueFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueFanSpeed.setStatus("mandatory")


class _Dualdrr2xstateFlagFanSpeed_Type(Integer32):
    """Custom type dualdrr2xstateFlagFanSpeed based on Integer32"""
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


_Dualdrr2xstateFlagFanSpeed_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagFanSpeed_Object = MibTableColumn
dualdrr2xstateFlagFanSpeed = _Dualdrr2xstateFlagFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 53),
    _Dualdrr2xstateFlagFanSpeed_Type()
)
dualdrr2xstateFlagFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagFanSpeed.setStatus("mandatory")
_Dualdrr2xminValueFanSpeed_Type = Float
_Dualdrr2xminValueFanSpeed_Object = MibTableColumn
dualdrr2xminValueFanSpeed = _Dualdrr2xminValueFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 54),
    _Dualdrr2xminValueFanSpeed_Type()
)
dualdrr2xminValueFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueFanSpeed.setStatus("mandatory")
_Dualdrr2xmaxValueFanSpeed_Type = Float
_Dualdrr2xmaxValueFanSpeed_Object = MibTableColumn
dualdrr2xmaxValueFanSpeed = _Dualdrr2xmaxValueFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 55),
    _Dualdrr2xmaxValueFanSpeed_Type()
)
dualdrr2xmaxValueFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueFanSpeed.setStatus("mandatory")


class _Dualdrr2xalarmStateFanSpeed_Type(Integer32):
    """Custom type dualdrr2xalarmStateFanSpeed based on Integer32"""
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


_Dualdrr2xalarmStateFanSpeed_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateFanSpeed_Object = MibTableColumn
dualdrr2xalarmStateFanSpeed = _Dualdrr2xalarmStateFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 56),
    _Dualdrr2xalarmStateFanSpeed_Type()
)
dualdrr2xalarmStateFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateFanSpeed.setStatus("mandatory")


class _Dualdrr2xlabelTx0SFPWave_Type(DisplayString):
    """Custom type dualdrr2xlabelTx0SFPWave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx0SFPWave_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx0SFPWave_Object = MibTableColumn
dualdrr2xlabelTx0SFPWave = _Dualdrr2xlabelTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 57),
    _Dualdrr2xlabelTx0SFPWave_Type()
)
dualdrr2xlabelTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx0SFPWave.setStatus("optional")


class _Dualdrr2xuomTx0SFPWave_Type(DisplayString):
    """Custom type dualdrr2xuomTx0SFPWave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx0SFPWave_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx0SFPWave_Object = MibTableColumn
dualdrr2xuomTx0SFPWave = _Dualdrr2xuomTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 58),
    _Dualdrr2xuomTx0SFPWave_Type()
)
dualdrr2xuomTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx0SFPWave.setStatus("optional")
_Dualdrr2xmajorHighTx0SFPWave_Type = Float
_Dualdrr2xmajorHighTx0SFPWave_Object = MibTableColumn
dualdrr2xmajorHighTx0SFPWave = _Dualdrr2xmajorHighTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 59),
    _Dualdrr2xmajorHighTx0SFPWave_Type()
)
dualdrr2xmajorHighTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx0SFPWave.setStatus("mandatory")
_Dualdrr2xmajorLowTx0SFPWave_Type = Float
_Dualdrr2xmajorLowTx0SFPWave_Object = MibTableColumn
dualdrr2xmajorLowTx0SFPWave = _Dualdrr2xmajorLowTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 60),
    _Dualdrr2xmajorLowTx0SFPWave_Type()
)
dualdrr2xmajorLowTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx0SFPWave.setStatus("mandatory")
_Dualdrr2xminorHighTx0SFPWave_Type = Float
_Dualdrr2xminorHighTx0SFPWave_Object = MibTableColumn
dualdrr2xminorHighTx0SFPWave = _Dualdrr2xminorHighTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 61),
    _Dualdrr2xminorHighTx0SFPWave_Type()
)
dualdrr2xminorHighTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx0SFPWave.setStatus("obsolete")
_Dualdrr2xminorLowTx0SFPWave_Type = Float
_Dualdrr2xminorLowTx0SFPWave_Object = MibTableColumn
dualdrr2xminorLowTx0SFPWave = _Dualdrr2xminorLowTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 62),
    _Dualdrr2xminorLowTx0SFPWave_Type()
)
dualdrr2xminorLowTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx0SFPWave.setStatus("obsolete")
_Dualdrr2xcurrentValueTx0SFPWave_Type = Float
_Dualdrr2xcurrentValueTx0SFPWave_Object = MibTableColumn
dualdrr2xcurrentValueTx0SFPWave = _Dualdrr2xcurrentValueTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 63),
    _Dualdrr2xcurrentValueTx0SFPWave_Type()
)
dualdrr2xcurrentValueTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx0SFPWave.setStatus("mandatory")


class _Dualdrr2xstateFlagTx0SFPWave_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx0SFPWave based on Integer32"""
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


_Dualdrr2xstateFlagTx0SFPWave_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx0SFPWave_Object = MibTableColumn
dualdrr2xstateFlagTx0SFPWave = _Dualdrr2xstateFlagTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 64),
    _Dualdrr2xstateFlagTx0SFPWave_Type()
)
dualdrr2xstateFlagTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx0SFPWave.setStatus("mandatory")
_Dualdrr2xminValueTx0SFPWave_Type = Float
_Dualdrr2xminValueTx0SFPWave_Object = MibTableColumn
dualdrr2xminValueTx0SFPWave = _Dualdrr2xminValueTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 65),
    _Dualdrr2xminValueTx0SFPWave_Type()
)
dualdrr2xminValueTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx0SFPWave.setStatus("mandatory")
_Dualdrr2xmaxValueTx0SFPWave_Type = Float
_Dualdrr2xmaxValueTx0SFPWave_Object = MibTableColumn
dualdrr2xmaxValueTx0SFPWave = _Dualdrr2xmaxValueTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 66),
    _Dualdrr2xmaxValueTx0SFPWave_Type()
)
dualdrr2xmaxValueTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx0SFPWave.setStatus("mandatory")


class _Dualdrr2xalarmStateTx0SFPWave_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx0SFPWave based on Integer32"""
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


_Dualdrr2xalarmStateTx0SFPWave_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx0SFPWave_Object = MibTableColumn
dualdrr2xalarmStateTx0SFPWave = _Dualdrr2xalarmStateTx0SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 67),
    _Dualdrr2xalarmStateTx0SFPWave_Type()
)
dualdrr2xalarmStateTx0SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx0SFPWave.setStatus("mandatory")


class _Dualdrr2xlabelTx0OptPwr_Type(DisplayString):
    """Custom type dualdrr2xlabelTx0OptPwr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx0OptPwr_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx0OptPwr_Object = MibTableColumn
dualdrr2xlabelTx0OptPwr = _Dualdrr2xlabelTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 68),
    _Dualdrr2xlabelTx0OptPwr_Type()
)
dualdrr2xlabelTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx0OptPwr.setStatus("optional")


class _Dualdrr2xuomTx0OptPwr_Type(DisplayString):
    """Custom type dualdrr2xuomTx0OptPwr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx0OptPwr_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx0OptPwr_Object = MibTableColumn
dualdrr2xuomTx0OptPwr = _Dualdrr2xuomTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 69),
    _Dualdrr2xuomTx0OptPwr_Type()
)
dualdrr2xuomTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx0OptPwr.setStatus("optional")
_Dualdrr2xmajorHighTx0OptPwr_Type = Float
_Dualdrr2xmajorHighTx0OptPwr_Object = MibTableColumn
dualdrr2xmajorHighTx0OptPwr = _Dualdrr2xmajorHighTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 70),
    _Dualdrr2xmajorHighTx0OptPwr_Type()
)
dualdrr2xmajorHighTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx0OptPwr.setStatus("mandatory")
_Dualdrr2xmajorLowTx0OptPwr_Type = Float
_Dualdrr2xmajorLowTx0OptPwr_Object = MibTableColumn
dualdrr2xmajorLowTx0OptPwr = _Dualdrr2xmajorLowTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 71),
    _Dualdrr2xmajorLowTx0OptPwr_Type()
)
dualdrr2xmajorLowTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx0OptPwr.setStatus("mandatory")
_Dualdrr2xminorHighTx0OptPwr_Type = Float
_Dualdrr2xminorHighTx0OptPwr_Object = MibTableColumn
dualdrr2xminorHighTx0OptPwr = _Dualdrr2xminorHighTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 72),
    _Dualdrr2xminorHighTx0OptPwr_Type()
)
dualdrr2xminorHighTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx0OptPwr.setStatus("obsolete")
_Dualdrr2xminorLowTx0OptPwr_Type = Float
_Dualdrr2xminorLowTx0OptPwr_Object = MibTableColumn
dualdrr2xminorLowTx0OptPwr = _Dualdrr2xminorLowTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 73),
    _Dualdrr2xminorLowTx0OptPwr_Type()
)
dualdrr2xminorLowTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx0OptPwr.setStatus("obsolete")
_Dualdrr2xcurrentValueTx0OptPwr_Type = Float
_Dualdrr2xcurrentValueTx0OptPwr_Object = MibTableColumn
dualdrr2xcurrentValueTx0OptPwr = _Dualdrr2xcurrentValueTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 74),
    _Dualdrr2xcurrentValueTx0OptPwr_Type()
)
dualdrr2xcurrentValueTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx0OptPwr.setStatus("mandatory")


class _Dualdrr2xstateFlagTx0OptPwr_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx0OptPwr based on Integer32"""
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


_Dualdrr2xstateFlagTx0OptPwr_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx0OptPwr_Object = MibTableColumn
dualdrr2xstateFlagTx0OptPwr = _Dualdrr2xstateFlagTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 75),
    _Dualdrr2xstateFlagTx0OptPwr_Type()
)
dualdrr2xstateFlagTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx0OptPwr.setStatus("mandatory")
_Dualdrr2xminValueTx0OptPwr_Type = Float
_Dualdrr2xminValueTx0OptPwr_Object = MibTableColumn
dualdrr2xminValueTx0OptPwr = _Dualdrr2xminValueTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 76),
    _Dualdrr2xminValueTx0OptPwr_Type()
)
dualdrr2xminValueTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx0OptPwr.setStatus("mandatory")
_Dualdrr2xmaxValueTx0OptPwr_Type = Float
_Dualdrr2xmaxValueTx0OptPwr_Object = MibTableColumn
dualdrr2xmaxValueTx0OptPwr = _Dualdrr2xmaxValueTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 77),
    _Dualdrr2xmaxValueTx0OptPwr_Type()
)
dualdrr2xmaxValueTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx0OptPwr.setStatus("mandatory")


class _Dualdrr2xalarmStateTx0OptPwr_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx0OptPwr based on Integer32"""
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


_Dualdrr2xalarmStateTx0OptPwr_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx0OptPwr_Object = MibTableColumn
dualdrr2xalarmStateTx0OptPwr = _Dualdrr2xalarmStateTx0OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 78),
    _Dualdrr2xalarmStateTx0OptPwr_Type()
)
dualdrr2xalarmStateTx0OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx0OptPwr.setStatus("mandatory")


class _Dualdrr2xlabelTx024vCurr_Type(DisplayString):
    """Custom type dualdrr2xlabelTx024vCurr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx024vCurr_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx024vCurr_Object = MibTableColumn
dualdrr2xlabelTx024vCurr = _Dualdrr2xlabelTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 79),
    _Dualdrr2xlabelTx024vCurr_Type()
)
dualdrr2xlabelTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx024vCurr.setStatus("optional")


class _Dualdrr2xuomTx024vCurr_Type(DisplayString):
    """Custom type dualdrr2xuomTx024vCurr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx024vCurr_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx024vCurr_Object = MibTableColumn
dualdrr2xuomTx024vCurr = _Dualdrr2xuomTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 80),
    _Dualdrr2xuomTx024vCurr_Type()
)
dualdrr2xuomTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx024vCurr.setStatus("optional")
_Dualdrr2xmajorHighTx024vCurr_Type = Float
_Dualdrr2xmajorHighTx024vCurr_Object = MibTableColumn
dualdrr2xmajorHighTx024vCurr = _Dualdrr2xmajorHighTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 81),
    _Dualdrr2xmajorHighTx024vCurr_Type()
)
dualdrr2xmajorHighTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx024vCurr.setStatus("mandatory")
_Dualdrr2xmajorLowTx024vCurr_Type = Float
_Dualdrr2xmajorLowTx024vCurr_Object = MibTableColumn
dualdrr2xmajorLowTx024vCurr = _Dualdrr2xmajorLowTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 82),
    _Dualdrr2xmajorLowTx024vCurr_Type()
)
dualdrr2xmajorLowTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx024vCurr.setStatus("mandatory")
_Dualdrr2xminorHighTx024vCurr_Type = Float
_Dualdrr2xminorHighTx024vCurr_Object = MibTableColumn
dualdrr2xminorHighTx024vCurr = _Dualdrr2xminorHighTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 83),
    _Dualdrr2xminorHighTx024vCurr_Type()
)
dualdrr2xminorHighTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx024vCurr.setStatus("obsolete")
_Dualdrr2xminorLowTx024vCurr_Type = Float
_Dualdrr2xminorLowTx024vCurr_Object = MibTableColumn
dualdrr2xminorLowTx024vCurr = _Dualdrr2xminorLowTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 84),
    _Dualdrr2xminorLowTx024vCurr_Type()
)
dualdrr2xminorLowTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx024vCurr.setStatus("obsolete")
_Dualdrr2xcurrentValueTx024vCurr_Type = Float
_Dualdrr2xcurrentValueTx024vCurr_Object = MibTableColumn
dualdrr2xcurrentValueTx024vCurr = _Dualdrr2xcurrentValueTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 85),
    _Dualdrr2xcurrentValueTx024vCurr_Type()
)
dualdrr2xcurrentValueTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx024vCurr.setStatus("mandatory")


class _Dualdrr2xstateFlagTx024vCurr_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx024vCurr based on Integer32"""
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


_Dualdrr2xstateFlagTx024vCurr_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx024vCurr_Object = MibTableColumn
dualdrr2xstateFlagTx024vCurr = _Dualdrr2xstateFlagTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 86),
    _Dualdrr2xstateFlagTx024vCurr_Type()
)
dualdrr2xstateFlagTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx024vCurr.setStatus("mandatory")
_Dualdrr2xminValueTx024vCurr_Type = Float
_Dualdrr2xminValueTx024vCurr_Object = MibTableColumn
dualdrr2xminValueTx024vCurr = _Dualdrr2xminValueTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 87),
    _Dualdrr2xminValueTx024vCurr_Type()
)
dualdrr2xminValueTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx024vCurr.setStatus("mandatory")
_Dualdrr2xmaxValueTx024vCurr_Type = Float
_Dualdrr2xmaxValueTx024vCurr_Object = MibTableColumn
dualdrr2xmaxValueTx024vCurr = _Dualdrr2xmaxValueTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 88),
    _Dualdrr2xmaxValueTx024vCurr_Type()
)
dualdrr2xmaxValueTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx024vCurr.setStatus("mandatory")


class _Dualdrr2xalarmStateTx024vCurr_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx024vCurr based on Integer32"""
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


_Dualdrr2xalarmStateTx024vCurr_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx024vCurr_Object = MibTableColumn
dualdrr2xalarmStateTx024vCurr = _Dualdrr2xalarmStateTx024vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 89),
    _Dualdrr2xalarmStateTx024vCurr_Type()
)
dualdrr2xalarmStateTx024vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx024vCurr.setStatus("mandatory")


class _Dualdrr2xlabelTx024Volt_Type(DisplayString):
    """Custom type dualdrr2xlabelTx024Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx024Volt_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx024Volt_Object = MibTableColumn
dualdrr2xlabelTx024Volt = _Dualdrr2xlabelTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 90),
    _Dualdrr2xlabelTx024Volt_Type()
)
dualdrr2xlabelTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx024Volt.setStatus("optional")


class _Dualdrr2xuomTx024Volt_Type(DisplayString):
    """Custom type dualdrr2xuomTx024Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx024Volt_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx024Volt_Object = MibTableColumn
dualdrr2xuomTx024Volt = _Dualdrr2xuomTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 91),
    _Dualdrr2xuomTx024Volt_Type()
)
dualdrr2xuomTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx024Volt.setStatus("optional")
_Dualdrr2xmajorHighTx024Volt_Type = Float
_Dualdrr2xmajorHighTx024Volt_Object = MibTableColumn
dualdrr2xmajorHighTx024Volt = _Dualdrr2xmajorHighTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 92),
    _Dualdrr2xmajorHighTx024Volt_Type()
)
dualdrr2xmajorHighTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx024Volt.setStatus("mandatory")
_Dualdrr2xmajorLowTx024Volt_Type = Float
_Dualdrr2xmajorLowTx024Volt_Object = MibTableColumn
dualdrr2xmajorLowTx024Volt = _Dualdrr2xmajorLowTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 93),
    _Dualdrr2xmajorLowTx024Volt_Type()
)
dualdrr2xmajorLowTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx024Volt.setStatus("mandatory")
_Dualdrr2xminorHighTx024Volt_Type = Float
_Dualdrr2xminorHighTx024Volt_Object = MibTableColumn
dualdrr2xminorHighTx024Volt = _Dualdrr2xminorHighTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 94),
    _Dualdrr2xminorHighTx024Volt_Type()
)
dualdrr2xminorHighTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx024Volt.setStatus("obsolete")
_Dualdrr2xminorLowTx024Volt_Type = Float
_Dualdrr2xminorLowTx024Volt_Object = MibTableColumn
dualdrr2xminorLowTx024Volt = _Dualdrr2xminorLowTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 95),
    _Dualdrr2xminorLowTx024Volt_Type()
)
dualdrr2xminorLowTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx024Volt.setStatus("obsolete")
_Dualdrr2xcurrentValueTx024Volt_Type = Float
_Dualdrr2xcurrentValueTx024Volt_Object = MibTableColumn
dualdrr2xcurrentValueTx024Volt = _Dualdrr2xcurrentValueTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 96),
    _Dualdrr2xcurrentValueTx024Volt_Type()
)
dualdrr2xcurrentValueTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx024Volt.setStatus("mandatory")


class _Dualdrr2xstateFlagTx024Volt_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx024Volt based on Integer32"""
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


_Dualdrr2xstateFlagTx024Volt_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx024Volt_Object = MibTableColumn
dualdrr2xstateFlagTx024Volt = _Dualdrr2xstateFlagTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 97),
    _Dualdrr2xstateFlagTx024Volt_Type()
)
dualdrr2xstateFlagTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx024Volt.setStatus("mandatory")
_Dualdrr2xminValueTx024Volt_Type = Float
_Dualdrr2xminValueTx024Volt_Object = MibTableColumn
dualdrr2xminValueTx024Volt = _Dualdrr2xminValueTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 98),
    _Dualdrr2xminValueTx024Volt_Type()
)
dualdrr2xminValueTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx024Volt.setStatus("mandatory")
_Dualdrr2xmaxValueTx024Volt_Type = Float
_Dualdrr2xmaxValueTx024Volt_Object = MibTableColumn
dualdrr2xmaxValueTx024Volt = _Dualdrr2xmaxValueTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 99),
    _Dualdrr2xmaxValueTx024Volt_Type()
)
dualdrr2xmaxValueTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx024Volt.setStatus("mandatory")


class _Dualdrr2xalarmStateTx024Volt_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx024Volt based on Integer32"""
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


_Dualdrr2xalarmStateTx024Volt_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx024Volt_Object = MibTableColumn
dualdrr2xalarmStateTx024Volt = _Dualdrr2xalarmStateTx024Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 100),
    _Dualdrr2xalarmStateTx024Volt_Type()
)
dualdrr2xalarmStateTx024Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx024Volt.setStatus("mandatory")


class _Dualdrr2xlabelTx0ModTemp_Type(DisplayString):
    """Custom type dualdrr2xlabelTx0ModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx0ModTemp_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx0ModTemp_Object = MibTableColumn
dualdrr2xlabelTx0ModTemp = _Dualdrr2xlabelTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 101),
    _Dualdrr2xlabelTx0ModTemp_Type()
)
dualdrr2xlabelTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx0ModTemp.setStatus("optional")


class _Dualdrr2xuomTx0ModTemp_Type(DisplayString):
    """Custom type dualdrr2xuomTx0ModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx0ModTemp_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx0ModTemp_Object = MibTableColumn
dualdrr2xuomTx0ModTemp = _Dualdrr2xuomTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 102),
    _Dualdrr2xuomTx0ModTemp_Type()
)
dualdrr2xuomTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx0ModTemp.setStatus("optional")
_Dualdrr2xmajorHighTx0ModTemp_Type = Float
_Dualdrr2xmajorHighTx0ModTemp_Object = MibTableColumn
dualdrr2xmajorHighTx0ModTemp = _Dualdrr2xmajorHighTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 103),
    _Dualdrr2xmajorHighTx0ModTemp_Type()
)
dualdrr2xmajorHighTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx0ModTemp.setStatus("mandatory")
_Dualdrr2xmajorLowTx0ModTemp_Type = Float
_Dualdrr2xmajorLowTx0ModTemp_Object = MibTableColumn
dualdrr2xmajorLowTx0ModTemp = _Dualdrr2xmajorLowTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 104),
    _Dualdrr2xmajorLowTx0ModTemp_Type()
)
dualdrr2xmajorLowTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx0ModTemp.setStatus("mandatory")
_Dualdrr2xminorHighTx0ModTemp_Type = Float
_Dualdrr2xminorHighTx0ModTemp_Object = MibTableColumn
dualdrr2xminorHighTx0ModTemp = _Dualdrr2xminorHighTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 105),
    _Dualdrr2xminorHighTx0ModTemp_Type()
)
dualdrr2xminorHighTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx0ModTemp.setStatus("obsolete")
_Dualdrr2xminorLowTx0ModTemp_Type = Float
_Dualdrr2xminorLowTx0ModTemp_Object = MibTableColumn
dualdrr2xminorLowTx0ModTemp = _Dualdrr2xminorLowTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 106),
    _Dualdrr2xminorLowTx0ModTemp_Type()
)
dualdrr2xminorLowTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx0ModTemp.setStatus("obsolete")
_Dualdrr2xcurrentValueTx0ModTemp_Type = Float
_Dualdrr2xcurrentValueTx0ModTemp_Object = MibTableColumn
dualdrr2xcurrentValueTx0ModTemp = _Dualdrr2xcurrentValueTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 107),
    _Dualdrr2xcurrentValueTx0ModTemp_Type()
)
dualdrr2xcurrentValueTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx0ModTemp.setStatus("mandatory")


class _Dualdrr2xstateFlagTx0ModTemp_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx0ModTemp based on Integer32"""
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


_Dualdrr2xstateFlagTx0ModTemp_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx0ModTemp_Object = MibTableColumn
dualdrr2xstateFlagTx0ModTemp = _Dualdrr2xstateFlagTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 108),
    _Dualdrr2xstateFlagTx0ModTemp_Type()
)
dualdrr2xstateFlagTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx0ModTemp.setStatus("mandatory")
_Dualdrr2xminValueTx0ModTemp_Type = Float
_Dualdrr2xminValueTx0ModTemp_Object = MibTableColumn
dualdrr2xminValueTx0ModTemp = _Dualdrr2xminValueTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 109),
    _Dualdrr2xminValueTx0ModTemp_Type()
)
dualdrr2xminValueTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx0ModTemp.setStatus("mandatory")
_Dualdrr2xmaxValueTx0ModTemp_Type = Float
_Dualdrr2xmaxValueTx0ModTemp_Object = MibTableColumn
dualdrr2xmaxValueTx0ModTemp = _Dualdrr2xmaxValueTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 110),
    _Dualdrr2xmaxValueTx0ModTemp_Type()
)
dualdrr2xmaxValueTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx0ModTemp.setStatus("mandatory")


class _Dualdrr2xalarmStateTx0ModTemp_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx0ModTemp based on Integer32"""
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


_Dualdrr2xalarmStateTx0ModTemp_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx0ModTemp_Object = MibTableColumn
dualdrr2xalarmStateTx0ModTemp = _Dualdrr2xalarmStateTx0ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 111),
    _Dualdrr2xalarmStateTx0ModTemp_Type()
)
dualdrr2xalarmStateTx0ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx0ModTemp.setStatus("mandatory")


class _Dualdrr2xlabelTx1SFPWave_Type(DisplayString):
    """Custom type dualdrr2xlabelTx1SFPWave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx1SFPWave_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx1SFPWave_Object = MibTableColumn
dualdrr2xlabelTx1SFPWave = _Dualdrr2xlabelTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 112),
    _Dualdrr2xlabelTx1SFPWave_Type()
)
dualdrr2xlabelTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx1SFPWave.setStatus("optional")


class _Dualdrr2xuomTx1SFPWave_Type(DisplayString):
    """Custom type dualdrr2xuomTx1SFPWave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx1SFPWave_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx1SFPWave_Object = MibTableColumn
dualdrr2xuomTx1SFPWave = _Dualdrr2xuomTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 113),
    _Dualdrr2xuomTx1SFPWave_Type()
)
dualdrr2xuomTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx1SFPWave.setStatus("optional")
_Dualdrr2xmajorHighTx1SFPWave_Type = Float
_Dualdrr2xmajorHighTx1SFPWave_Object = MibTableColumn
dualdrr2xmajorHighTx1SFPWave = _Dualdrr2xmajorHighTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 114),
    _Dualdrr2xmajorHighTx1SFPWave_Type()
)
dualdrr2xmajorHighTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx1SFPWave.setStatus("mandatory")
_Dualdrr2xmajorLowTx1SFPWave_Type = Float
_Dualdrr2xmajorLowTx1SFPWave_Object = MibTableColumn
dualdrr2xmajorLowTx1SFPWave = _Dualdrr2xmajorLowTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 115),
    _Dualdrr2xmajorLowTx1SFPWave_Type()
)
dualdrr2xmajorLowTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx1SFPWave.setStatus("mandatory")
_Dualdrr2xminorHighTx1SFPWave_Type = Float
_Dualdrr2xminorHighTx1SFPWave_Object = MibTableColumn
dualdrr2xminorHighTx1SFPWave = _Dualdrr2xminorHighTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 116),
    _Dualdrr2xminorHighTx1SFPWave_Type()
)
dualdrr2xminorHighTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx1SFPWave.setStatus("obsolete")
_Dualdrr2xminorLowTx1SFPWave_Type = Float
_Dualdrr2xminorLowTx1SFPWave_Object = MibTableColumn
dualdrr2xminorLowTx1SFPWave = _Dualdrr2xminorLowTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 117),
    _Dualdrr2xminorLowTx1SFPWave_Type()
)
dualdrr2xminorLowTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx1SFPWave.setStatus("obsolete")
_Dualdrr2xcurrentValueTx1SFPWave_Type = Float
_Dualdrr2xcurrentValueTx1SFPWave_Object = MibTableColumn
dualdrr2xcurrentValueTx1SFPWave = _Dualdrr2xcurrentValueTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 118),
    _Dualdrr2xcurrentValueTx1SFPWave_Type()
)
dualdrr2xcurrentValueTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx1SFPWave.setStatus("mandatory")


class _Dualdrr2xstateFlagTx1SFPWave_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx1SFPWave based on Integer32"""
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


_Dualdrr2xstateFlagTx1SFPWave_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx1SFPWave_Object = MibTableColumn
dualdrr2xstateFlagTx1SFPWave = _Dualdrr2xstateFlagTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 119),
    _Dualdrr2xstateFlagTx1SFPWave_Type()
)
dualdrr2xstateFlagTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx1SFPWave.setStatus("mandatory")
_Dualdrr2xminValueTx1SFPWave_Type = Float
_Dualdrr2xminValueTx1SFPWave_Object = MibTableColumn
dualdrr2xminValueTx1SFPWave = _Dualdrr2xminValueTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 120),
    _Dualdrr2xminValueTx1SFPWave_Type()
)
dualdrr2xminValueTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx1SFPWave.setStatus("mandatory")
_Dualdrr2xmaxValueTx1SFPWave_Type = Float
_Dualdrr2xmaxValueTx1SFPWave_Object = MibTableColumn
dualdrr2xmaxValueTx1SFPWave = _Dualdrr2xmaxValueTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 121),
    _Dualdrr2xmaxValueTx1SFPWave_Type()
)
dualdrr2xmaxValueTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx1SFPWave.setStatus("mandatory")


class _Dualdrr2xalarmStateTx1SFPWave_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx1SFPWave based on Integer32"""
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


_Dualdrr2xalarmStateTx1SFPWave_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx1SFPWave_Object = MibTableColumn
dualdrr2xalarmStateTx1SFPWave = _Dualdrr2xalarmStateTx1SFPWave_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 122),
    _Dualdrr2xalarmStateTx1SFPWave_Type()
)
dualdrr2xalarmStateTx1SFPWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx1SFPWave.setStatus("mandatory")


class _Dualdrr2xlabelTx1OptPwr_Type(DisplayString):
    """Custom type dualdrr2xlabelTx1OptPwr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx1OptPwr_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx1OptPwr_Object = MibTableColumn
dualdrr2xlabelTx1OptPwr = _Dualdrr2xlabelTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 123),
    _Dualdrr2xlabelTx1OptPwr_Type()
)
dualdrr2xlabelTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx1OptPwr.setStatus("optional")


class _Dualdrr2xuomTx1OptPwr_Type(DisplayString):
    """Custom type dualdrr2xuomTx1OptPwr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx1OptPwr_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx1OptPwr_Object = MibTableColumn
dualdrr2xuomTx1OptPwr = _Dualdrr2xuomTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 124),
    _Dualdrr2xuomTx1OptPwr_Type()
)
dualdrr2xuomTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx1OptPwr.setStatus("optional")
_Dualdrr2xmajorHighTx1OptPwr_Type = Float
_Dualdrr2xmajorHighTx1OptPwr_Object = MibTableColumn
dualdrr2xmajorHighTx1OptPwr = _Dualdrr2xmajorHighTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 125),
    _Dualdrr2xmajorHighTx1OptPwr_Type()
)
dualdrr2xmajorHighTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx1OptPwr.setStatus("mandatory")
_Dualdrr2xmajorLowTx1OptPwr_Type = Float
_Dualdrr2xmajorLowTx1OptPwr_Object = MibTableColumn
dualdrr2xmajorLowTx1OptPwr = _Dualdrr2xmajorLowTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 126),
    _Dualdrr2xmajorLowTx1OptPwr_Type()
)
dualdrr2xmajorLowTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx1OptPwr.setStatus("mandatory")
_Dualdrr2xminorHighTx1OptPwr_Type = Float
_Dualdrr2xminorHighTx1OptPwr_Object = MibTableColumn
dualdrr2xminorHighTx1OptPwr = _Dualdrr2xminorHighTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 127),
    _Dualdrr2xminorHighTx1OptPwr_Type()
)
dualdrr2xminorHighTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx1OptPwr.setStatus("obsolete")
_Dualdrr2xminorLowTx1OptPwr_Type = Float
_Dualdrr2xminorLowTx1OptPwr_Object = MibTableColumn
dualdrr2xminorLowTx1OptPwr = _Dualdrr2xminorLowTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 128),
    _Dualdrr2xminorLowTx1OptPwr_Type()
)
dualdrr2xminorLowTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx1OptPwr.setStatus("obsolete")
_Dualdrr2xcurrentValueTx1OptPwr_Type = Float
_Dualdrr2xcurrentValueTx1OptPwr_Object = MibTableColumn
dualdrr2xcurrentValueTx1OptPwr = _Dualdrr2xcurrentValueTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 129),
    _Dualdrr2xcurrentValueTx1OptPwr_Type()
)
dualdrr2xcurrentValueTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx1OptPwr.setStatus("mandatory")


class _Dualdrr2xstateFlagTx1OptPwr_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx1OptPwr based on Integer32"""
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


_Dualdrr2xstateFlagTx1OptPwr_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx1OptPwr_Object = MibTableColumn
dualdrr2xstateFlagTx1OptPwr = _Dualdrr2xstateFlagTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 130),
    _Dualdrr2xstateFlagTx1OptPwr_Type()
)
dualdrr2xstateFlagTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx1OptPwr.setStatus("mandatory")
_Dualdrr2xminValueTx1OptPwr_Type = Float
_Dualdrr2xminValueTx1OptPwr_Object = MibTableColumn
dualdrr2xminValueTx1OptPwr = _Dualdrr2xminValueTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 131),
    _Dualdrr2xminValueTx1OptPwr_Type()
)
dualdrr2xminValueTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx1OptPwr.setStatus("mandatory")
_Dualdrr2xmaxValueTx1OptPwr_Type = Float
_Dualdrr2xmaxValueTx1OptPwr_Object = MibTableColumn
dualdrr2xmaxValueTx1OptPwr = _Dualdrr2xmaxValueTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 132),
    _Dualdrr2xmaxValueTx1OptPwr_Type()
)
dualdrr2xmaxValueTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx1OptPwr.setStatus("mandatory")


class _Dualdrr2xalarmStateTx1OptPwr_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx1OptPwr based on Integer32"""
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


_Dualdrr2xalarmStateTx1OptPwr_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx1OptPwr_Object = MibTableColumn
dualdrr2xalarmStateTx1OptPwr = _Dualdrr2xalarmStateTx1OptPwr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 133),
    _Dualdrr2xalarmStateTx1OptPwr_Type()
)
dualdrr2xalarmStateTx1OptPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx1OptPwr.setStatus("mandatory")


class _Dualdrr2xlabelTx124vCurr_Type(DisplayString):
    """Custom type dualdrr2xlabelTx124vCurr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx124vCurr_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx124vCurr_Object = MibTableColumn
dualdrr2xlabelTx124vCurr = _Dualdrr2xlabelTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 134),
    _Dualdrr2xlabelTx124vCurr_Type()
)
dualdrr2xlabelTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx124vCurr.setStatus("optional")


class _Dualdrr2xuomTx124vCurr_Type(DisplayString):
    """Custom type dualdrr2xuomTx124vCurr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx124vCurr_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx124vCurr_Object = MibTableColumn
dualdrr2xuomTx124vCurr = _Dualdrr2xuomTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 135),
    _Dualdrr2xuomTx124vCurr_Type()
)
dualdrr2xuomTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx124vCurr.setStatus("optional")
_Dualdrr2xmajorHighTx124vCurr_Type = Float
_Dualdrr2xmajorHighTx124vCurr_Object = MibTableColumn
dualdrr2xmajorHighTx124vCurr = _Dualdrr2xmajorHighTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 136),
    _Dualdrr2xmajorHighTx124vCurr_Type()
)
dualdrr2xmajorHighTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx124vCurr.setStatus("mandatory")
_Dualdrr2xmajorLowTx124vCurr_Type = Float
_Dualdrr2xmajorLowTx124vCurr_Object = MibTableColumn
dualdrr2xmajorLowTx124vCurr = _Dualdrr2xmajorLowTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 137),
    _Dualdrr2xmajorLowTx124vCurr_Type()
)
dualdrr2xmajorLowTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx124vCurr.setStatus("mandatory")
_Dualdrr2xminorHighTx124vCurr_Type = Float
_Dualdrr2xminorHighTx124vCurr_Object = MibTableColumn
dualdrr2xminorHighTx124vCurr = _Dualdrr2xminorHighTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 138),
    _Dualdrr2xminorHighTx124vCurr_Type()
)
dualdrr2xminorHighTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx124vCurr.setStatus("obsolete")
_Dualdrr2xminorLowTx124vCurr_Type = Float
_Dualdrr2xminorLowTx124vCurr_Object = MibTableColumn
dualdrr2xminorLowTx124vCurr = _Dualdrr2xminorLowTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 139),
    _Dualdrr2xminorLowTx124vCurr_Type()
)
dualdrr2xminorLowTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx124vCurr.setStatus("obsolete")
_Dualdrr2xcurrentValueTx124vCurr_Type = Float
_Dualdrr2xcurrentValueTx124vCurr_Object = MibTableColumn
dualdrr2xcurrentValueTx124vCurr = _Dualdrr2xcurrentValueTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 140),
    _Dualdrr2xcurrentValueTx124vCurr_Type()
)
dualdrr2xcurrentValueTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx124vCurr.setStatus("mandatory")


class _Dualdrr2xstateFlagTx124vCurr_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx124vCurr based on Integer32"""
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


_Dualdrr2xstateFlagTx124vCurr_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx124vCurr_Object = MibTableColumn
dualdrr2xstateFlagTx124vCurr = _Dualdrr2xstateFlagTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 141),
    _Dualdrr2xstateFlagTx124vCurr_Type()
)
dualdrr2xstateFlagTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx124vCurr.setStatus("mandatory")
_Dualdrr2xminValueTx124vCurr_Type = Float
_Dualdrr2xminValueTx124vCurr_Object = MibTableColumn
dualdrr2xminValueTx124vCurr = _Dualdrr2xminValueTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 142),
    _Dualdrr2xminValueTx124vCurr_Type()
)
dualdrr2xminValueTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx124vCurr.setStatus("mandatory")
_Dualdrr2xmaxValueTx124vCurr_Type = Float
_Dualdrr2xmaxValueTx124vCurr_Object = MibTableColumn
dualdrr2xmaxValueTx124vCurr = _Dualdrr2xmaxValueTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 143),
    _Dualdrr2xmaxValueTx124vCurr_Type()
)
dualdrr2xmaxValueTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx124vCurr.setStatus("mandatory")


class _Dualdrr2xalarmStateTx124vCurr_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx124vCurr based on Integer32"""
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


_Dualdrr2xalarmStateTx124vCurr_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx124vCurr_Object = MibTableColumn
dualdrr2xalarmStateTx124vCurr = _Dualdrr2xalarmStateTx124vCurr_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 144),
    _Dualdrr2xalarmStateTx124vCurr_Type()
)
dualdrr2xalarmStateTx124vCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx124vCurr.setStatus("mandatory")


class _Dualdrr2xlabelTx124Volt_Type(DisplayString):
    """Custom type dualdrr2xlabelTx124Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx124Volt_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx124Volt_Object = MibTableColumn
dualdrr2xlabelTx124Volt = _Dualdrr2xlabelTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 145),
    _Dualdrr2xlabelTx124Volt_Type()
)
dualdrr2xlabelTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx124Volt.setStatus("optional")


class _Dualdrr2xuomTx124Volt_Type(DisplayString):
    """Custom type dualdrr2xuomTx124Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx124Volt_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx124Volt_Object = MibTableColumn
dualdrr2xuomTx124Volt = _Dualdrr2xuomTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 146),
    _Dualdrr2xuomTx124Volt_Type()
)
dualdrr2xuomTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx124Volt.setStatus("optional")
_Dualdrr2xmajorHighTx124Volt_Type = Float
_Dualdrr2xmajorHighTx124Volt_Object = MibTableColumn
dualdrr2xmajorHighTx124Volt = _Dualdrr2xmajorHighTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 147),
    _Dualdrr2xmajorHighTx124Volt_Type()
)
dualdrr2xmajorHighTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx124Volt.setStatus("mandatory")
_Dualdrr2xmajorLowTx124Volt_Type = Float
_Dualdrr2xmajorLowTx124Volt_Object = MibTableColumn
dualdrr2xmajorLowTx124Volt = _Dualdrr2xmajorLowTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 148),
    _Dualdrr2xmajorLowTx124Volt_Type()
)
dualdrr2xmajorLowTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx124Volt.setStatus("mandatory")
_Dualdrr2xminorHighTx124Volt_Type = Float
_Dualdrr2xminorHighTx124Volt_Object = MibTableColumn
dualdrr2xminorHighTx124Volt = _Dualdrr2xminorHighTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 149),
    _Dualdrr2xminorHighTx124Volt_Type()
)
dualdrr2xminorHighTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx124Volt.setStatus("obsolete")
_Dualdrr2xminorLowTx124Volt_Type = Float
_Dualdrr2xminorLowTx124Volt_Object = MibTableColumn
dualdrr2xminorLowTx124Volt = _Dualdrr2xminorLowTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 150),
    _Dualdrr2xminorLowTx124Volt_Type()
)
dualdrr2xminorLowTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx124Volt.setStatus("obsolete")
_Dualdrr2xcurrentValueTx124Volt_Type = Float
_Dualdrr2xcurrentValueTx124Volt_Object = MibTableColumn
dualdrr2xcurrentValueTx124Volt = _Dualdrr2xcurrentValueTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 151),
    _Dualdrr2xcurrentValueTx124Volt_Type()
)
dualdrr2xcurrentValueTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx124Volt.setStatus("mandatory")


class _Dualdrr2xstateFlagTx124Volt_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx124Volt based on Integer32"""
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


_Dualdrr2xstateFlagTx124Volt_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx124Volt_Object = MibTableColumn
dualdrr2xstateFlagTx124Volt = _Dualdrr2xstateFlagTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 152),
    _Dualdrr2xstateFlagTx124Volt_Type()
)
dualdrr2xstateFlagTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx124Volt.setStatus("mandatory")
_Dualdrr2xminValueTx124Volt_Type = Float
_Dualdrr2xminValueTx124Volt_Object = MibTableColumn
dualdrr2xminValueTx124Volt = _Dualdrr2xminValueTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 153),
    _Dualdrr2xminValueTx124Volt_Type()
)
dualdrr2xminValueTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx124Volt.setStatus("mandatory")
_Dualdrr2xmaxValueTx124Volt_Type = Float
_Dualdrr2xmaxValueTx124Volt_Object = MibTableColumn
dualdrr2xmaxValueTx124Volt = _Dualdrr2xmaxValueTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 154),
    _Dualdrr2xmaxValueTx124Volt_Type()
)
dualdrr2xmaxValueTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx124Volt.setStatus("mandatory")


class _Dualdrr2xalarmStateTx124Volt_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx124Volt based on Integer32"""
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


_Dualdrr2xalarmStateTx124Volt_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx124Volt_Object = MibTableColumn
dualdrr2xalarmStateTx124Volt = _Dualdrr2xalarmStateTx124Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 155),
    _Dualdrr2xalarmStateTx124Volt_Type()
)
dualdrr2xalarmStateTx124Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx124Volt.setStatus("mandatory")


class _Dualdrr2xlabelTx1ModTemp_Type(DisplayString):
    """Custom type dualdrr2xlabelTx1ModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTx1ModTemp_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTx1ModTemp_Object = MibTableColumn
dualdrr2xlabelTx1ModTemp = _Dualdrr2xlabelTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 156),
    _Dualdrr2xlabelTx1ModTemp_Type()
)
dualdrr2xlabelTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTx1ModTemp.setStatus("optional")


class _Dualdrr2xuomTx1ModTemp_Type(DisplayString):
    """Custom type dualdrr2xuomTx1ModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xuomTx1ModTemp_Type.__name__ = "DisplayString"
_Dualdrr2xuomTx1ModTemp_Object = MibTableColumn
dualdrr2xuomTx1ModTemp = _Dualdrr2xuomTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 157),
    _Dualdrr2xuomTx1ModTemp_Type()
)
dualdrr2xuomTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xuomTx1ModTemp.setStatus("optional")
_Dualdrr2xmajorHighTx1ModTemp_Type = Float
_Dualdrr2xmajorHighTx1ModTemp_Object = MibTableColumn
dualdrr2xmajorHighTx1ModTemp = _Dualdrr2xmajorHighTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 158),
    _Dualdrr2xmajorHighTx1ModTemp_Type()
)
dualdrr2xmajorHighTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorHighTx1ModTemp.setStatus("mandatory")
_Dualdrr2xmajorLowTx1ModTemp_Type = Float
_Dualdrr2xmajorLowTx1ModTemp_Object = MibTableColumn
dualdrr2xmajorLowTx1ModTemp = _Dualdrr2xmajorLowTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 159),
    _Dualdrr2xmajorLowTx1ModTemp_Type()
)
dualdrr2xmajorLowTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmajorLowTx1ModTemp.setStatus("mandatory")
_Dualdrr2xminorHighTx1ModTemp_Type = Float
_Dualdrr2xminorHighTx1ModTemp_Object = MibTableColumn
dualdrr2xminorHighTx1ModTemp = _Dualdrr2xminorHighTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 160),
    _Dualdrr2xminorHighTx1ModTemp_Type()
)
dualdrr2xminorHighTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorHighTx1ModTemp.setStatus("obsolete")
_Dualdrr2xminorLowTx1ModTemp_Type = Float
_Dualdrr2xminorLowTx1ModTemp_Object = MibTableColumn
dualdrr2xminorLowTx1ModTemp = _Dualdrr2xminorLowTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 161),
    _Dualdrr2xminorLowTx1ModTemp_Type()
)
dualdrr2xminorLowTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminorLowTx1ModTemp.setStatus("obsolete")
_Dualdrr2xcurrentValueTx1ModTemp_Type = Float
_Dualdrr2xcurrentValueTx1ModTemp_Object = MibTableColumn
dualdrr2xcurrentValueTx1ModTemp = _Dualdrr2xcurrentValueTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 162),
    _Dualdrr2xcurrentValueTx1ModTemp_Type()
)
dualdrr2xcurrentValueTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcurrentValueTx1ModTemp.setStatus("mandatory")


class _Dualdrr2xstateFlagTx1ModTemp_Type(Integer32):
    """Custom type dualdrr2xstateFlagTx1ModTemp based on Integer32"""
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


_Dualdrr2xstateFlagTx1ModTemp_Type.__name__ = "Integer32"
_Dualdrr2xstateFlagTx1ModTemp_Object = MibTableColumn
dualdrr2xstateFlagTx1ModTemp = _Dualdrr2xstateFlagTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 163),
    _Dualdrr2xstateFlagTx1ModTemp_Type()
)
dualdrr2xstateFlagTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateFlagTx1ModTemp.setStatus("mandatory")
_Dualdrr2xminValueTx1ModTemp_Type = Float
_Dualdrr2xminValueTx1ModTemp_Object = MibTableColumn
dualdrr2xminValueTx1ModTemp = _Dualdrr2xminValueTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 164),
    _Dualdrr2xminValueTx1ModTemp_Type()
)
dualdrr2xminValueTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xminValueTx1ModTemp.setStatus("mandatory")
_Dualdrr2xmaxValueTx1ModTemp_Type = Float
_Dualdrr2xmaxValueTx1ModTemp_Object = MibTableColumn
dualdrr2xmaxValueTx1ModTemp = _Dualdrr2xmaxValueTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 165),
    _Dualdrr2xmaxValueTx1ModTemp_Type()
)
dualdrr2xmaxValueTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xmaxValueTx1ModTemp.setStatus("mandatory")


class _Dualdrr2xalarmStateTx1ModTemp_Type(Integer32):
    """Custom type dualdrr2xalarmStateTx1ModTemp based on Integer32"""
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


_Dualdrr2xalarmStateTx1ModTemp_Type.__name__ = "Integer32"
_Dualdrr2xalarmStateTx1ModTemp_Object = MibTableColumn
dualdrr2xalarmStateTx1ModTemp = _Dualdrr2xalarmStateTx1ModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 2, 1, 166),
    _Dualdrr2xalarmStateTx1ModTemp_Type()
)
dualdrr2xalarmStateTx1ModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xalarmStateTx1ModTemp.setStatus("mandatory")
_Gx2dualdrr2xDigitalTable_Object = MibTable
gx2dualdrr2xDigitalTable = _Gx2dualdrr2xDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3)
)
if mibBuilder.loadTexts:
    gx2dualdrr2xDigitalTable.setStatus("mandatory")
_Gx2dualdrr2xDigitalEntry_Object = MibTableRow
gx2dualdrr2xDigitalEntry = _Gx2dualdrr2xDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2)
)
gx2dualdrr2xDigitalEntry.setIndexNames(
    (0, "OMNI-gx2dualdrr2x-MIB", "gx2dualdrr2xDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2dualdrr2xDigitalEntry.setStatus("mandatory")


class _Gx2dualdrr2xDigitalTableIndex_Type(Integer32):
    """Custom type gx2dualdrr2xDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2dualdrr2xDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2dualdrr2xDigitalTableIndex_Object = MibTableColumn
gx2dualdrr2xDigitalTableIndex = _Gx2dualdrr2xDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 1),
    _Gx2dualdrr2xDigitalTableIndex_Type()
)
gx2dualdrr2xDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2dualdrr2xDigitalTableIndex.setStatus("mandatory")


class _Dualdrr2xlabelTrippoint1Value_Type(DisplayString):
    """Custom type dualdrr2xlabelTrippoint1Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTrippoint1Value_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTrippoint1Value_Object = MibTableColumn
dualdrr2xlabelTrippoint1Value = _Dualdrr2xlabelTrippoint1Value_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 2),
    _Dualdrr2xlabelTrippoint1Value_Type()
)
dualdrr2xlabelTrippoint1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTrippoint1Value.setStatus("optional")


class _Dualdrr2xenumTrippoint1Value_Type(DisplayString):
    """Custom type dualdrr2xenumTrippoint1Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumTrippoint1Value_Type.__name__ = "DisplayString"
_Dualdrr2xenumTrippoint1Value_Object = MibTableColumn
dualdrr2xenumTrippoint1Value = _Dualdrr2xenumTrippoint1Value_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 3),
    _Dualdrr2xenumTrippoint1Value_Type()
)
dualdrr2xenumTrippoint1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumTrippoint1Value.setStatus("optional")
_Dualdrr2xvalueTrippoint1Value_Type = Integer32
_Dualdrr2xvalueTrippoint1Value_Object = MibTableColumn
dualdrr2xvalueTrippoint1Value = _Dualdrr2xvalueTrippoint1Value_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 4),
    _Dualdrr2xvalueTrippoint1Value_Type()
)
dualdrr2xvalueTrippoint1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueTrippoint1Value.setStatus("mandatory")


class _Dualdrr2xstateflagTrippoint1Value_Type(Integer32):
    """Custom type dualdrr2xstateflagTrippoint1Value based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagTrippoint1Value_Type.__name__ = "Integer32"
_Dualdrr2xstateflagTrippoint1Value_Object = MibTableColumn
dualdrr2xstateflagTrippoint1Value = _Dualdrr2xstateflagTrippoint1Value_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 5),
    _Dualdrr2xstateflagTrippoint1Value_Type()
)
dualdrr2xstateflagTrippoint1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagTrippoint1Value.setStatus("mandatory")


class _Dualdrr2xlabelTrippoint1Mode_Type(DisplayString):
    """Custom type dualdrr2xlabelTrippoint1Mode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTrippoint1Mode_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTrippoint1Mode_Object = MibTableColumn
dualdrr2xlabelTrippoint1Mode = _Dualdrr2xlabelTrippoint1Mode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 6),
    _Dualdrr2xlabelTrippoint1Mode_Type()
)
dualdrr2xlabelTrippoint1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTrippoint1Mode.setStatus("optional")


class _Dualdrr2xenumTrippoint1Mode_Type(DisplayString):
    """Custom type dualdrr2xenumTrippoint1Mode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumTrippoint1Mode_Type.__name__ = "DisplayString"
_Dualdrr2xenumTrippoint1Mode_Object = MibTableColumn
dualdrr2xenumTrippoint1Mode = _Dualdrr2xenumTrippoint1Mode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 7),
    _Dualdrr2xenumTrippoint1Mode_Type()
)
dualdrr2xenumTrippoint1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumTrippoint1Mode.setStatus("optional")


class _Dualdrr2xvalueTrippoint1Mode_Type(Integer32):
    """Custom type dualdrr2xvalueTrippoint1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-and-Switch", 3),
          ("alarmOnly", 2),
          ("off", 1))
    )


_Dualdrr2xvalueTrippoint1Mode_Type.__name__ = "Integer32"
_Dualdrr2xvalueTrippoint1Mode_Object = MibTableColumn
dualdrr2xvalueTrippoint1Mode = _Dualdrr2xvalueTrippoint1Mode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 8),
    _Dualdrr2xvalueTrippoint1Mode_Type()
)
dualdrr2xvalueTrippoint1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueTrippoint1Mode.setStatus("mandatory")


class _Dualdrr2xstateflagTrippoint1Mode_Type(Integer32):
    """Custom type dualdrr2xstateflagTrippoint1Mode based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagTrippoint1Mode_Type.__name__ = "Integer32"
_Dualdrr2xstateflagTrippoint1Mode_Object = MibTableColumn
dualdrr2xstateflagTrippoint1Mode = _Dualdrr2xstateflagTrippoint1Mode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 9),
    _Dualdrr2xstateflagTrippoint1Mode_Type()
)
dualdrr2xstateflagTrippoint1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagTrippoint1Mode.setStatus("mandatory")


class _Dualdrr2xlabelTrippoint2Value_Type(DisplayString):
    """Custom type dualdrr2xlabelTrippoint2Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTrippoint2Value_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTrippoint2Value_Object = MibTableColumn
dualdrr2xlabelTrippoint2Value = _Dualdrr2xlabelTrippoint2Value_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 10),
    _Dualdrr2xlabelTrippoint2Value_Type()
)
dualdrr2xlabelTrippoint2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTrippoint2Value.setStatus("optional")


class _Dualdrr2xenumTrippoint2Value_Type(DisplayString):
    """Custom type dualdrr2xenumTrippoint2Value based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumTrippoint2Value_Type.__name__ = "DisplayString"
_Dualdrr2xenumTrippoint2Value_Object = MibTableColumn
dualdrr2xenumTrippoint2Value = _Dualdrr2xenumTrippoint2Value_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 11),
    _Dualdrr2xenumTrippoint2Value_Type()
)
dualdrr2xenumTrippoint2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumTrippoint2Value.setStatus("optional")
_Dualdrr2xvalueTrippoint2Value_Type = Integer32
_Dualdrr2xvalueTrippoint2Value_Object = MibTableColumn
dualdrr2xvalueTrippoint2Value = _Dualdrr2xvalueTrippoint2Value_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 12),
    _Dualdrr2xvalueTrippoint2Value_Type()
)
dualdrr2xvalueTrippoint2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueTrippoint2Value.setStatus("mandatory")


class _Dualdrr2xstateflagTrippoint2Value_Type(Integer32):
    """Custom type dualdrr2xstateflagTrippoint2Value based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagTrippoint2Value_Type.__name__ = "Integer32"
_Dualdrr2xstateflagTrippoint2Value_Object = MibTableColumn
dualdrr2xstateflagTrippoint2Value = _Dualdrr2xstateflagTrippoint2Value_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 13),
    _Dualdrr2xstateflagTrippoint2Value_Type()
)
dualdrr2xstateflagTrippoint2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagTrippoint2Value.setStatus("mandatory")


class _Dualdrr2xlabelTrippoint2Mode_Type(DisplayString):
    """Custom type dualdrr2xlabelTrippoint2Mode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTrippoint2Mode_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTrippoint2Mode_Object = MibTableColumn
dualdrr2xlabelTrippoint2Mode = _Dualdrr2xlabelTrippoint2Mode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 14),
    _Dualdrr2xlabelTrippoint2Mode_Type()
)
dualdrr2xlabelTrippoint2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTrippoint2Mode.setStatus("optional")


class _Dualdrr2xenumTrippoint2Mode_Type(DisplayString):
    """Custom type dualdrr2xenumTrippoint2Mode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumTrippoint2Mode_Type.__name__ = "DisplayString"
_Dualdrr2xenumTrippoint2Mode_Object = MibTableColumn
dualdrr2xenumTrippoint2Mode = _Dualdrr2xenumTrippoint2Mode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 15),
    _Dualdrr2xenumTrippoint2Mode_Type()
)
dualdrr2xenumTrippoint2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumTrippoint2Mode.setStatus("optional")


class _Dualdrr2xvalueTrippoint2Mode_Type(Integer32):
    """Custom type dualdrr2xvalueTrippoint2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm-and-Switch", 3),
          ("alarmOnly", 2),
          ("off", 1))
    )


_Dualdrr2xvalueTrippoint2Mode_Type.__name__ = "Integer32"
_Dualdrr2xvalueTrippoint2Mode_Object = MibTableColumn
dualdrr2xvalueTrippoint2Mode = _Dualdrr2xvalueTrippoint2Mode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 16),
    _Dualdrr2xvalueTrippoint2Mode_Type()
)
dualdrr2xvalueTrippoint2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueTrippoint2Mode.setStatus("mandatory")


class _Dualdrr2xstateflagTrippoint2Mode_Type(Integer32):
    """Custom type dualdrr2xstateflagTrippoint2Mode based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagTrippoint2Mode_Type.__name__ = "Integer32"
_Dualdrr2xstateflagTrippoint2Mode_Object = MibTableColumn
dualdrr2xstateflagTrippoint2Mode = _Dualdrr2xstateflagTrippoint2Mode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 17),
    _Dualdrr2xstateflagTrippoint2Mode_Type()
)
dualdrr2xstateflagTrippoint2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagTrippoint2Mode.setStatus("mandatory")


class _Dualdrr2xlabelGainChannel1A_Type(DisplayString):
    """Custom type dualdrr2xlabelGainChannel1A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelGainChannel1A_Type.__name__ = "DisplayString"
_Dualdrr2xlabelGainChannel1A_Object = MibTableColumn
dualdrr2xlabelGainChannel1A = _Dualdrr2xlabelGainChannel1A_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 18),
    _Dualdrr2xlabelGainChannel1A_Type()
)
dualdrr2xlabelGainChannel1A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelGainChannel1A.setStatus("optional")


class _Dualdrr2xenumGainChannel1A_Type(DisplayString):
    """Custom type dualdrr2xenumGainChannel1A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumGainChannel1A_Type.__name__ = "DisplayString"
_Dualdrr2xenumGainChannel1A_Object = MibTableColumn
dualdrr2xenumGainChannel1A = _Dualdrr2xenumGainChannel1A_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 19),
    _Dualdrr2xenumGainChannel1A_Type()
)
dualdrr2xenumGainChannel1A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumGainChannel1A.setStatus("optional")
_Dualdrr2xvalueGainChannel1A_Type = Integer32
_Dualdrr2xvalueGainChannel1A_Object = MibTableColumn
dualdrr2xvalueGainChannel1A = _Dualdrr2xvalueGainChannel1A_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 20),
    _Dualdrr2xvalueGainChannel1A_Type()
)
dualdrr2xvalueGainChannel1A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueGainChannel1A.setStatus("mandatory")


class _Dualdrr2xstateflagGainChannel1A_Type(Integer32):
    """Custom type dualdrr2xstateflagGainChannel1A based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagGainChannel1A_Type.__name__ = "Integer32"
_Dualdrr2xstateflagGainChannel1A_Object = MibTableColumn
dualdrr2xstateflagGainChannel1A = _Dualdrr2xstateflagGainChannel1A_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 21),
    _Dualdrr2xstateflagGainChannel1A_Type()
)
dualdrr2xstateflagGainChannel1A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagGainChannel1A.setStatus("mandatory")


class _Dualdrr2xlabelGainChannel1B_Type(DisplayString):
    """Custom type dualdrr2xlabelGainChannel1B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelGainChannel1B_Type.__name__ = "DisplayString"
_Dualdrr2xlabelGainChannel1B_Object = MibTableColumn
dualdrr2xlabelGainChannel1B = _Dualdrr2xlabelGainChannel1B_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 22),
    _Dualdrr2xlabelGainChannel1B_Type()
)
dualdrr2xlabelGainChannel1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelGainChannel1B.setStatus("optional")


class _Dualdrr2xenumGainChannel1B_Type(DisplayString):
    """Custom type dualdrr2xenumGainChannel1B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumGainChannel1B_Type.__name__ = "DisplayString"
_Dualdrr2xenumGainChannel1B_Object = MibTableColumn
dualdrr2xenumGainChannel1B = _Dualdrr2xenumGainChannel1B_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 23),
    _Dualdrr2xenumGainChannel1B_Type()
)
dualdrr2xenumGainChannel1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumGainChannel1B.setStatus("optional")
_Dualdrr2xvalueGainChannel1B_Type = Integer32
_Dualdrr2xvalueGainChannel1B_Object = MibTableColumn
dualdrr2xvalueGainChannel1B = _Dualdrr2xvalueGainChannel1B_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 24),
    _Dualdrr2xvalueGainChannel1B_Type()
)
dualdrr2xvalueGainChannel1B.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueGainChannel1B.setStatus("mandatory")


class _Dualdrr2xstateflagGainChannel1B_Type(Integer32):
    """Custom type dualdrr2xstateflagGainChannel1B based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagGainChannel1B_Type.__name__ = "Integer32"
_Dualdrr2xstateflagGainChannel1B_Object = MibTableColumn
dualdrr2xstateflagGainChannel1B = _Dualdrr2xstateflagGainChannel1B_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 25),
    _Dualdrr2xstateflagGainChannel1B_Type()
)
dualdrr2xstateflagGainChannel1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagGainChannel1B.setStatus("mandatory")


class _Dualdrr2xlabelGainChannel2A_Type(DisplayString):
    """Custom type dualdrr2xlabelGainChannel2A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelGainChannel2A_Type.__name__ = "DisplayString"
_Dualdrr2xlabelGainChannel2A_Object = MibTableColumn
dualdrr2xlabelGainChannel2A = _Dualdrr2xlabelGainChannel2A_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 26),
    _Dualdrr2xlabelGainChannel2A_Type()
)
dualdrr2xlabelGainChannel2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelGainChannel2A.setStatus("optional")


class _Dualdrr2xenumGainChannel2A_Type(DisplayString):
    """Custom type dualdrr2xenumGainChannel2A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumGainChannel2A_Type.__name__ = "DisplayString"
_Dualdrr2xenumGainChannel2A_Object = MibTableColumn
dualdrr2xenumGainChannel2A = _Dualdrr2xenumGainChannel2A_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 27),
    _Dualdrr2xenumGainChannel2A_Type()
)
dualdrr2xenumGainChannel2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumGainChannel2A.setStatus("optional")
_Dualdrr2xvalueGainChannel2A_Type = Integer32
_Dualdrr2xvalueGainChannel2A_Object = MibTableColumn
dualdrr2xvalueGainChannel2A = _Dualdrr2xvalueGainChannel2A_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 28),
    _Dualdrr2xvalueGainChannel2A_Type()
)
dualdrr2xvalueGainChannel2A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueGainChannel2A.setStatus("mandatory")


class _Dualdrr2xstateflagGainChannel2A_Type(Integer32):
    """Custom type dualdrr2xstateflagGainChannel2A based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagGainChannel2A_Type.__name__ = "Integer32"
_Dualdrr2xstateflagGainChannel2A_Object = MibTableColumn
dualdrr2xstateflagGainChannel2A = _Dualdrr2xstateflagGainChannel2A_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 29),
    _Dualdrr2xstateflagGainChannel2A_Type()
)
dualdrr2xstateflagGainChannel2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagGainChannel2A.setStatus("mandatory")


class _Dualdrr2xlabelGainChannel2B_Type(DisplayString):
    """Custom type dualdrr2xlabelGainChannel2B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelGainChannel2B_Type.__name__ = "DisplayString"
_Dualdrr2xlabelGainChannel2B_Object = MibTableColumn
dualdrr2xlabelGainChannel2B = _Dualdrr2xlabelGainChannel2B_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 30),
    _Dualdrr2xlabelGainChannel2B_Type()
)
dualdrr2xlabelGainChannel2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelGainChannel2B.setStatus("optional")


class _Dualdrr2xenumGainChannel2B_Type(DisplayString):
    """Custom type dualdrr2xenumGainChannel2B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumGainChannel2B_Type.__name__ = "DisplayString"
_Dualdrr2xenumGainChannel2B_Object = MibTableColumn
dualdrr2xenumGainChannel2B = _Dualdrr2xenumGainChannel2B_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 31),
    _Dualdrr2xenumGainChannel2B_Type()
)
dualdrr2xenumGainChannel2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumGainChannel2B.setStatus("optional")
_Dualdrr2xvalueGainChannel2B_Type = Integer32
_Dualdrr2xvalueGainChannel2B_Object = MibTableColumn
dualdrr2xvalueGainChannel2B = _Dualdrr2xvalueGainChannel2B_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 32),
    _Dualdrr2xvalueGainChannel2B_Type()
)
dualdrr2xvalueGainChannel2B.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueGainChannel2B.setStatus("mandatory")


class _Dualdrr2xstateflagGainChannel2B_Type(Integer32):
    """Custom type dualdrr2xstateflagGainChannel2B based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagGainChannel2B_Type.__name__ = "Integer32"
_Dualdrr2xstateflagGainChannel2B_Object = MibTableColumn
dualdrr2xstateflagGainChannel2B = _Dualdrr2xstateflagGainChannel2B_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 33),
    _Dualdrr2xstateflagGainChannel2B_Type()
)
dualdrr2xstateflagGainChannel2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagGainChannel2B.setStatus("mandatory")


class _Dualdrr2xlabelTestpointSelect_Type(DisplayString):
    """Custom type dualdrr2xlabelTestpointSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelTestpointSelect_Type.__name__ = "DisplayString"
_Dualdrr2xlabelTestpointSelect_Object = MibTableColumn
dualdrr2xlabelTestpointSelect = _Dualdrr2xlabelTestpointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 34),
    _Dualdrr2xlabelTestpointSelect_Type()
)
dualdrr2xlabelTestpointSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelTestpointSelect.setStatus("optional")


class _Dualdrr2xenumTestpointSelect_Type(DisplayString):
    """Custom type dualdrr2xenumTestpointSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumTestpointSelect_Type.__name__ = "DisplayString"
_Dualdrr2xenumTestpointSelect_Object = MibTableColumn
dualdrr2xenumTestpointSelect = _Dualdrr2xenumTestpointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 35),
    _Dualdrr2xenumTestpointSelect_Type()
)
dualdrr2xenumTestpointSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumTestpointSelect.setStatus("optional")


class _Dualdrr2xvalueTestpointSelect_Type(Integer32):
    """Custom type dualdrr2xvalueTestpointSelect based on Integer32"""
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


_Dualdrr2xvalueTestpointSelect_Type.__name__ = "Integer32"
_Dualdrr2xvalueTestpointSelect_Object = MibTableColumn
dualdrr2xvalueTestpointSelect = _Dualdrr2xvalueTestpointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 36),
    _Dualdrr2xvalueTestpointSelect_Type()
)
dualdrr2xvalueTestpointSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueTestpointSelect.setStatus("mandatory")


class _Dualdrr2xstateflagTestpointSelect_Type(Integer32):
    """Custom type dualdrr2xstateflagTestpointSelect based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagTestpointSelect_Type.__name__ = "Integer32"
_Dualdrr2xstateflagTestpointSelect_Object = MibTableColumn
dualdrr2xstateflagTestpointSelect = _Dualdrr2xstateflagTestpointSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 37),
    _Dualdrr2xstateflagTestpointSelect_Type()
)
dualdrr2xstateflagTestpointSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagTestpointSelect.setStatus("mandatory")


class _Dualdrr2xlabelOpFrequency_Type(DisplayString):
    """Custom type dualdrr2xlabelOpFrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelOpFrequency_Type.__name__ = "DisplayString"
_Dualdrr2xlabelOpFrequency_Object = MibTableColumn
dualdrr2xlabelOpFrequency = _Dualdrr2xlabelOpFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 38),
    _Dualdrr2xlabelOpFrequency_Type()
)
dualdrr2xlabelOpFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelOpFrequency.setStatus("optional")


class _Dualdrr2xenumOpFrequency_Type(DisplayString):
    """Custom type dualdrr2xenumOpFrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumOpFrequency_Type.__name__ = "DisplayString"
_Dualdrr2xenumOpFrequency_Object = MibTableColumn
dualdrr2xenumOpFrequency = _Dualdrr2xenumOpFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 39),
    _Dualdrr2xenumOpFrequency_Type()
)
dualdrr2xenumOpFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumOpFrequency.setStatus("optional")


class _Dualdrr2xvalueOpFrequency_Type(Integer32):
    """Custom type dualdrr2xvalueOpFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eightyfive", 1),
          ("sixtyfive", 2))
    )


_Dualdrr2xvalueOpFrequency_Type.__name__ = "Integer32"
_Dualdrr2xvalueOpFrequency_Object = MibTableColumn
dualdrr2xvalueOpFrequency = _Dualdrr2xvalueOpFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 40),
    _Dualdrr2xvalueOpFrequency_Type()
)
dualdrr2xvalueOpFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueOpFrequency.setStatus("mandatory")


class _Dualdrr2xstateflagOpFrequency_Type(Integer32):
    """Custom type dualdrr2xstateflagOpFrequency based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagOpFrequency_Type.__name__ = "Integer32"
_Dualdrr2xstateflagOpFrequency_Object = MibTableColumn
dualdrr2xstateflagOpFrequency = _Dualdrr2xstateflagOpFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 41),
    _Dualdrr2xstateflagOpFrequency_Type()
)
dualdrr2xstateflagOpFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagOpFrequency.setStatus("mandatory")


class _Dualdrr2xlabelActChanSelect_Type(DisplayString):
    """Custom type dualdrr2xlabelActChanSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelActChanSelect_Type.__name__ = "DisplayString"
_Dualdrr2xlabelActChanSelect_Object = MibTableColumn
dualdrr2xlabelActChanSelect = _Dualdrr2xlabelActChanSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 42),
    _Dualdrr2xlabelActChanSelect_Type()
)
dualdrr2xlabelActChanSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelActChanSelect.setStatus("optional")


class _Dualdrr2xenumActChanSelect_Type(DisplayString):
    """Custom type dualdrr2xenumActChanSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumActChanSelect_Type.__name__ = "DisplayString"
_Dualdrr2xenumActChanSelect_Object = MibTableColumn
dualdrr2xenumActChanSelect = _Dualdrr2xenumActChanSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 43),
    _Dualdrr2xenumActChanSelect_Type()
)
dualdrr2xenumActChanSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumActChanSelect.setStatus("optional")


class _Dualdrr2xvalueActChanSelect_Type(Integer32):
    """Custom type dualdrr2xvalueActChanSelect based on Integer32"""
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
        *(("both", 4),
          ("channel1", 2),
          ("channel2", 3),
          ("none", 1))
    )


_Dualdrr2xvalueActChanSelect_Type.__name__ = "Integer32"
_Dualdrr2xvalueActChanSelect_Object = MibTableColumn
dualdrr2xvalueActChanSelect = _Dualdrr2xvalueActChanSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 44),
    _Dualdrr2xvalueActChanSelect_Type()
)
dualdrr2xvalueActChanSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueActChanSelect.setStatus("mandatory")


class _Dualdrr2xstateflagActChanSelect_Type(Integer32):
    """Custom type dualdrr2xstateflagActChanSelect based on Integer32"""
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
          ("readOnly", 2),
          ("updateable", 3))
    )


_Dualdrr2xstateflagActChanSelect_Type.__name__ = "Integer32"
_Dualdrr2xstateflagActChanSelect_Object = MibTableColumn
dualdrr2xstateflagActChanSelect = _Dualdrr2xstateflagActChanSelect_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 45),
    _Dualdrr2xstateflagActChanSelect_Type()
)
dualdrr2xstateflagActChanSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagActChanSelect.setStatus("mandatory")


class _Dualdrr2xlabelFactoryDefaultReset_Type(DisplayString):
    """Custom type dualdrr2xlabelFactoryDefaultReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelFactoryDefaultReset_Type.__name__ = "DisplayString"
_Dualdrr2xlabelFactoryDefaultReset_Object = MibTableColumn
dualdrr2xlabelFactoryDefaultReset = _Dualdrr2xlabelFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 46),
    _Dualdrr2xlabelFactoryDefaultReset_Type()
)
dualdrr2xlabelFactoryDefaultReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelFactoryDefaultReset.setStatus("optional")


class _Dualdrr2xenumFactoryDefaultReset_Type(DisplayString):
    """Custom type dualdrr2xenumFactoryDefaultReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xenumFactoryDefaultReset_Type.__name__ = "DisplayString"
_Dualdrr2xenumFactoryDefaultReset_Object = MibTableColumn
dualdrr2xenumFactoryDefaultReset = _Dualdrr2xenumFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 47),
    _Dualdrr2xenumFactoryDefaultReset_Type()
)
dualdrr2xenumFactoryDefaultReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xenumFactoryDefaultReset.setStatus("optional")


class _Dualdrr2xvalueFactoryDefaultReset_Type(Integer32):
    """Custom type dualdrr2xvalueFactoryDefaultReset based on Integer32"""
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


_Dualdrr2xvalueFactoryDefaultReset_Type.__name__ = "Integer32"
_Dualdrr2xvalueFactoryDefaultReset_Object = MibTableColumn
dualdrr2xvalueFactoryDefaultReset = _Dualdrr2xvalueFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 48),
    _Dualdrr2xvalueFactoryDefaultReset_Type()
)
dualdrr2xvalueFactoryDefaultReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dualdrr2xvalueFactoryDefaultReset.setStatus("mandatory")


class _Dualdrr2xstateflagFactoryDefaultReset_Type(Integer32):
    """Custom type dualdrr2xstateflagFactoryDefaultReset based on Integer32"""
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


_Dualdrr2xstateflagFactoryDefaultReset_Type.__name__ = "Integer32"
_Dualdrr2xstateflagFactoryDefaultReset_Object = MibTableColumn
dualdrr2xstateflagFactoryDefaultReset = _Dualdrr2xstateflagFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 3, 2, 49),
    _Dualdrr2xstateflagFactoryDefaultReset_Type()
)
dualdrr2xstateflagFactoryDefaultReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagFactoryDefaultReset.setStatus("mandatory")
_Gx2dualdrr2xStatusTable_Object = MibTable
gx2dualdrr2xStatusTable = _Gx2dualdrr2xStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4)
)
if mibBuilder.loadTexts:
    gx2dualdrr2xStatusTable.setStatus("mandatory")
_Gx2dualdrr2xStatusEntry_Object = MibTableRow
gx2dualdrr2xStatusEntry = _Gx2dualdrr2xStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3)
)
gx2dualdrr2xStatusEntry.setIndexNames(
    (0, "OMNI-gx2dualdrr2x-MIB", "gx2dualdrr2xStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2dualdrr2xStatusEntry.setStatus("mandatory")


class _Gx2dualdrr2xStatusTableIndex_Type(Integer32):
    """Custom type gx2dualdrr2xStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2dualdrr2xStatusTableIndex_Type.__name__ = "Integer32"
_Gx2dualdrr2xStatusTableIndex_Object = MibTableColumn
gx2dualdrr2xStatusTableIndex = _Gx2dualdrr2xStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 1),
    _Gx2dualdrr2xStatusTableIndex_Type()
)
gx2dualdrr2xStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2dualdrr2xStatusTableIndex.setStatus("mandatory")


class _Dualdrr2xlabelBoot_Type(DisplayString):
    """Custom type dualdrr2xlabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelBoot_Type.__name__ = "DisplayString"
_Dualdrr2xlabelBoot_Object = MibTableColumn
dualdrr2xlabelBoot = _Dualdrr2xlabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 2),
    _Dualdrr2xlabelBoot_Type()
)
dualdrr2xlabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelBoot.setStatus("optional")


class _Dualdrr2xvalueBoot_Type(Integer32):
    """Custom type dualdrr2xvalueBoot based on Integer32"""
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


_Dualdrr2xvalueBoot_Type.__name__ = "Integer32"
_Dualdrr2xvalueBoot_Object = MibTableColumn
dualdrr2xvalueBoot = _Dualdrr2xvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 3),
    _Dualdrr2xvalueBoot_Type()
)
dualdrr2xvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueBoot.setStatus("mandatory")


class _Dualdrr2xstateflagBoot_Type(Integer32):
    """Custom type dualdrr2xstateflagBoot based on Integer32"""
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


_Dualdrr2xstateflagBoot_Type.__name__ = "Integer32"
_Dualdrr2xstateflagBoot_Object = MibTableColumn
dualdrr2xstateflagBoot = _Dualdrr2xstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 4),
    _Dualdrr2xstateflagBoot_Type()
)
dualdrr2xstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagBoot.setStatus("mandatory")


class _Dualdrr2xlabelFlash_Type(DisplayString):
    """Custom type dualdrr2xlabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelFlash_Type.__name__ = "DisplayString"
_Dualdrr2xlabelFlash_Object = MibTableColumn
dualdrr2xlabelFlash = _Dualdrr2xlabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 5),
    _Dualdrr2xlabelFlash_Type()
)
dualdrr2xlabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelFlash.setStatus("optional")


class _Dualdrr2xvalueFlash_Type(Integer32):
    """Custom type dualdrr2xvalueFlash based on Integer32"""
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


_Dualdrr2xvalueFlash_Type.__name__ = "Integer32"
_Dualdrr2xvalueFlash_Object = MibTableColumn
dualdrr2xvalueFlash = _Dualdrr2xvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 6),
    _Dualdrr2xvalueFlash_Type()
)
dualdrr2xvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueFlash.setStatus("mandatory")


class _Dualdrr2xstateflagFlash_Type(Integer32):
    """Custom type dualdrr2xstateflagFlash based on Integer32"""
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


_Dualdrr2xstateflagFlash_Type.__name__ = "Integer32"
_Dualdrr2xstateflagFlash_Object = MibTableColumn
dualdrr2xstateflagFlash = _Dualdrr2xstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 7),
    _Dualdrr2xstateflagFlash_Type()
)
dualdrr2xstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagFlash.setStatus("mandatory")


class _Dualdrr2xlabelFactoryDataCRC_Type(DisplayString):
    """Custom type dualdrr2xlabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelFactoryDataCRC_Type.__name__ = "DisplayString"
_Dualdrr2xlabelFactoryDataCRC_Object = MibTableColumn
dualdrr2xlabelFactoryDataCRC = _Dualdrr2xlabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 8),
    _Dualdrr2xlabelFactoryDataCRC_Type()
)
dualdrr2xlabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelFactoryDataCRC.setStatus("optional")


class _Dualdrr2xvalueFactoryDataCRC_Type(Integer32):
    """Custom type dualdrr2xvalueFactoryDataCRC based on Integer32"""
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


_Dualdrr2xvalueFactoryDataCRC_Type.__name__ = "Integer32"
_Dualdrr2xvalueFactoryDataCRC_Object = MibTableColumn
dualdrr2xvalueFactoryDataCRC = _Dualdrr2xvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 9),
    _Dualdrr2xvalueFactoryDataCRC_Type()
)
dualdrr2xvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueFactoryDataCRC.setStatus("mandatory")


class _Dualdrr2xstateflagFactoryDataCRC_Type(Integer32):
    """Custom type dualdrr2xstateflagFactoryDataCRC based on Integer32"""
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


_Dualdrr2xstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Dualdrr2xstateflagFactoryDataCRC_Object = MibTableColumn
dualdrr2xstateflagFactoryDataCRC = _Dualdrr2xstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 10),
    _Dualdrr2xstateflagFactoryDataCRC_Type()
)
dualdrr2xstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagFactoryDataCRC.setStatus("mandatory")


class _Dualdrr2xlabelAlarmDataCrc_Type(DisplayString):
    """Custom type dualdrr2xlabelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelAlarmDataCrc_Type.__name__ = "DisplayString"
_Dualdrr2xlabelAlarmDataCrc_Object = MibTableColumn
dualdrr2xlabelAlarmDataCrc = _Dualdrr2xlabelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 11),
    _Dualdrr2xlabelAlarmDataCrc_Type()
)
dualdrr2xlabelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelAlarmDataCrc.setStatus("optional")


class _Dualdrr2xvalueAlarmDataCrc_Type(Integer32):
    """Custom type dualdrr2xvalueAlarmDataCrc based on Integer32"""
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


_Dualdrr2xvalueAlarmDataCrc_Type.__name__ = "Integer32"
_Dualdrr2xvalueAlarmDataCrc_Object = MibTableColumn
dualdrr2xvalueAlarmDataCrc = _Dualdrr2xvalueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 12),
    _Dualdrr2xvalueAlarmDataCrc_Type()
)
dualdrr2xvalueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueAlarmDataCrc.setStatus("mandatory")


class _Dualdrr2xstateflagAlarmDataCrc_Type(Integer32):
    """Custom type dualdrr2xstateflagAlarmDataCrc based on Integer32"""
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


_Dualdrr2xstateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Dualdrr2xstateflagAlarmDataCrc_Object = MibTableColumn
dualdrr2xstateflagAlarmDataCrc = _Dualdrr2xstateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 13),
    _Dualdrr2xstateflagAlarmDataCrc_Type()
)
dualdrr2xstateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagAlarmDataCrc.setStatus("mandatory")


class _Dualdrr2xlabelCalibrationDataCrc_Type(DisplayString):
    """Custom type dualdrr2xlabelCalibrationDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelCalibrationDataCrc_Type.__name__ = "DisplayString"
_Dualdrr2xlabelCalibrationDataCrc_Object = MibTableColumn
dualdrr2xlabelCalibrationDataCrc = _Dualdrr2xlabelCalibrationDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 14),
    _Dualdrr2xlabelCalibrationDataCrc_Type()
)
dualdrr2xlabelCalibrationDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelCalibrationDataCrc.setStatus("optional")


class _Dualdrr2xvalueCalibrationDataCrc_Type(Integer32):
    """Custom type dualdrr2xvalueCalibrationDataCrc based on Integer32"""
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


_Dualdrr2xvalueCalibrationDataCrc_Type.__name__ = "Integer32"
_Dualdrr2xvalueCalibrationDataCrc_Object = MibTableColumn
dualdrr2xvalueCalibrationDataCrc = _Dualdrr2xvalueCalibrationDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 15),
    _Dualdrr2xvalueCalibrationDataCrc_Type()
)
dualdrr2xvalueCalibrationDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueCalibrationDataCrc.setStatus("mandatory")


class _Dualdrr2xstateflagCalibrationDataCrc_Type(Integer32):
    """Custom type dualdrr2xstateflagCalibrationDataCrc based on Integer32"""
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


_Dualdrr2xstateflagCalibrationDataCrc_Type.__name__ = "Integer32"
_Dualdrr2xstateflagCalibrationDataCrc_Object = MibTableColumn
dualdrr2xstateflagCalibrationDataCrc = _Dualdrr2xstateflagCalibrationDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 16),
    _Dualdrr2xstateflagCalibrationDataCrc_Type()
)
dualdrr2xstateflagCalibrationDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagCalibrationDataCrc.setStatus("mandatory")


class _Dualdrr2xlabelHardwareStatus_Type(DisplayString):
    """Custom type dualdrr2xlabelHardwareStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelHardwareStatus_Type.__name__ = "DisplayString"
_Dualdrr2xlabelHardwareStatus_Object = MibTableColumn
dualdrr2xlabelHardwareStatus = _Dualdrr2xlabelHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 17),
    _Dualdrr2xlabelHardwareStatus_Type()
)
dualdrr2xlabelHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelHardwareStatus.setStatus("optional")


class _Dualdrr2xvalueHardwareStatus_Type(Integer32):
    """Custom type dualdrr2xvalueHardwareStatus based on Integer32"""
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


_Dualdrr2xvalueHardwareStatus_Type.__name__ = "Integer32"
_Dualdrr2xvalueHardwareStatus_Object = MibTableColumn
dualdrr2xvalueHardwareStatus = _Dualdrr2xvalueHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 18),
    _Dualdrr2xvalueHardwareStatus_Type()
)
dualdrr2xvalueHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueHardwareStatus.setStatus("mandatory")


class _Dualdrr2xstateflagHardwareStatus_Type(Integer32):
    """Custom type dualdrr2xstateflagHardwareStatus based on Integer32"""
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


_Dualdrr2xstateflagHardwareStatus_Type.__name__ = "Integer32"
_Dualdrr2xstateflagHardwareStatus_Object = MibTableColumn
dualdrr2xstateflagHardwareStatus = _Dualdrr2xstateflagHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 19),
    _Dualdrr2xstateflagHardwareStatus_Type()
)
dualdrr2xstateflagHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagHardwareStatus.setStatus("mandatory")


class _Dualdrr2xlabelCh1TripPointStatus_Type(DisplayString):
    """Custom type dualdrr2xlabelCh1TripPointStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelCh1TripPointStatus_Type.__name__ = "DisplayString"
_Dualdrr2xlabelCh1TripPointStatus_Object = MibTableColumn
dualdrr2xlabelCh1TripPointStatus = _Dualdrr2xlabelCh1TripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 20),
    _Dualdrr2xlabelCh1TripPointStatus_Type()
)
dualdrr2xlabelCh1TripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelCh1TripPointStatus.setStatus("optional")


class _Dualdrr2xvalueCh1TripPointStatus_Type(Integer32):
    """Custom type dualdrr2xvalueCh1TripPointStatus based on Integer32"""
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


_Dualdrr2xvalueCh1TripPointStatus_Type.__name__ = "Integer32"
_Dualdrr2xvalueCh1TripPointStatus_Object = MibTableColumn
dualdrr2xvalueCh1TripPointStatus = _Dualdrr2xvalueCh1TripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 21),
    _Dualdrr2xvalueCh1TripPointStatus_Type()
)
dualdrr2xvalueCh1TripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueCh1TripPointStatus.setStatus("mandatory")


class _Dualdrr2xstateflagCh1TripPointStatus_Type(Integer32):
    """Custom type dualdrr2xstateflagCh1TripPointStatus based on Integer32"""
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


_Dualdrr2xstateflagCh1TripPointStatus_Type.__name__ = "Integer32"
_Dualdrr2xstateflagCh1TripPointStatus_Object = MibTableColumn
dualdrr2xstateflagCh1TripPointStatus = _Dualdrr2xstateflagCh1TripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 22),
    _Dualdrr2xstateflagCh1TripPointStatus_Type()
)
dualdrr2xstateflagCh1TripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagCh1TripPointStatus.setStatus("mandatory")


class _Dualdrr2xlabelLink1Status_Type(DisplayString):
    """Custom type dualdrr2xlabelLink1Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelLink1Status_Type.__name__ = "DisplayString"
_Dualdrr2xlabelLink1Status_Object = MibTableColumn
dualdrr2xlabelLink1Status = _Dualdrr2xlabelLink1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 23),
    _Dualdrr2xlabelLink1Status_Type()
)
dualdrr2xlabelLink1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelLink1Status.setStatus("optional")


class _Dualdrr2xvalueLink1Status_Type(Integer32):
    """Custom type dualdrr2xvalueLink1Status based on Integer32"""
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


_Dualdrr2xvalueLink1Status_Type.__name__ = "Integer32"
_Dualdrr2xvalueLink1Status_Object = MibTableColumn
dualdrr2xvalueLink1Status = _Dualdrr2xvalueLink1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 24),
    _Dualdrr2xvalueLink1Status_Type()
)
dualdrr2xvalueLink1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueLink1Status.setStatus("mandatory")


class _Dualdrr2xstateflagLink1Status_Type(Integer32):
    """Custom type dualdrr2xstateflagLink1Status based on Integer32"""
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


_Dualdrr2xstateflagLink1Status_Type.__name__ = "Integer32"
_Dualdrr2xstateflagLink1Status_Object = MibTableColumn
dualdrr2xstateflagLink1Status = _Dualdrr2xstateflagLink1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 25),
    _Dualdrr2xstateflagLink1Status_Type()
)
dualdrr2xstateflagLink1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagLink1Status.setStatus("mandatory")


class _Dualdrr2xlabelCh2TripPointStatus_Type(DisplayString):
    """Custom type dualdrr2xlabelCh2TripPointStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelCh2TripPointStatus_Type.__name__ = "DisplayString"
_Dualdrr2xlabelCh2TripPointStatus_Object = MibTableColumn
dualdrr2xlabelCh2TripPointStatus = _Dualdrr2xlabelCh2TripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 26),
    _Dualdrr2xlabelCh2TripPointStatus_Type()
)
dualdrr2xlabelCh2TripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelCh2TripPointStatus.setStatus("optional")


class _Dualdrr2xvalueCh2TripPointStatus_Type(Integer32):
    """Custom type dualdrr2xvalueCh2TripPointStatus based on Integer32"""
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


_Dualdrr2xvalueCh2TripPointStatus_Type.__name__ = "Integer32"
_Dualdrr2xvalueCh2TripPointStatus_Object = MibTableColumn
dualdrr2xvalueCh2TripPointStatus = _Dualdrr2xvalueCh2TripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 27),
    _Dualdrr2xvalueCh2TripPointStatus_Type()
)
dualdrr2xvalueCh2TripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueCh2TripPointStatus.setStatus("mandatory")


class _Dualdrr2xstateflagCh2TripPointStatus_Type(Integer32):
    """Custom type dualdrr2xstateflagCh2TripPointStatus based on Integer32"""
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


_Dualdrr2xstateflagCh2TripPointStatus_Type.__name__ = "Integer32"
_Dualdrr2xstateflagCh2TripPointStatus_Object = MibTableColumn
dualdrr2xstateflagCh2TripPointStatus = _Dualdrr2xstateflagCh2TripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 28),
    _Dualdrr2xstateflagCh2TripPointStatus_Type()
)
dualdrr2xstateflagCh2TripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagCh2TripPointStatus.setStatus("mandatory")


class _Dualdrr2xlabelLink2Status_Type(DisplayString):
    """Custom type dualdrr2xlabelLink2Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelLink2Status_Type.__name__ = "DisplayString"
_Dualdrr2xlabelLink2Status_Object = MibTableColumn
dualdrr2xlabelLink2Status = _Dualdrr2xlabelLink2Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 29),
    _Dualdrr2xlabelLink2Status_Type()
)
dualdrr2xlabelLink2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelLink2Status.setStatus("optional")


class _Dualdrr2xvalueLink2Status_Type(Integer32):
    """Custom type dualdrr2xvalueLink2Status based on Integer32"""
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


_Dualdrr2xvalueLink2Status_Type.__name__ = "Integer32"
_Dualdrr2xvalueLink2Status_Object = MibTableColumn
dualdrr2xvalueLink2Status = _Dualdrr2xvalueLink2Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 30),
    _Dualdrr2xvalueLink2Status_Type()
)
dualdrr2xvalueLink2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueLink2Status.setStatus("mandatory")


class _Dualdrr2xstateflagLink2Status_Type(Integer32):
    """Custom type dualdrr2xstateflagLink2Status based on Integer32"""
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


_Dualdrr2xstateflagLink2Status_Type.__name__ = "Integer32"
_Dualdrr2xstateflagLink2Status_Object = MibTableColumn
dualdrr2xstateflagLink2Status = _Dualdrr2xstateflagLink2Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 31),
    _Dualdrr2xstateflagLink2Status_Type()
)
dualdrr2xstateflagLink2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagLink2Status.setStatus("mandatory")


class _Dualdrr2xlabelDRT1Status_Type(DisplayString):
    """Custom type dualdrr2xlabelDRT1Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelDRT1Status_Type.__name__ = "DisplayString"
_Dualdrr2xlabelDRT1Status_Object = MibTableColumn
dualdrr2xlabelDRT1Status = _Dualdrr2xlabelDRT1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 32),
    _Dualdrr2xlabelDRT1Status_Type()
)
dualdrr2xlabelDRT1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelDRT1Status.setStatus("optional")


class _Dualdrr2xvalueDRT1Status_Type(Integer32):
    """Custom type dualdrr2xvalueDRT1Status based on Integer32"""
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


_Dualdrr2xvalueDRT1Status_Type.__name__ = "Integer32"
_Dualdrr2xvalueDRT1Status_Object = MibTableColumn
dualdrr2xvalueDRT1Status = _Dualdrr2xvalueDRT1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 33),
    _Dualdrr2xvalueDRT1Status_Type()
)
dualdrr2xvalueDRT1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueDRT1Status.setStatus("mandatory")


class _Dualdrr2xstateflagDRT1Status_Type(Integer32):
    """Custom type dualdrr2xstateflagDRT1Status based on Integer32"""
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


_Dualdrr2xstateflagDRT1Status_Type.__name__ = "Integer32"
_Dualdrr2xstateflagDRT1Status_Object = MibTableColumn
dualdrr2xstateflagDRT1Status = _Dualdrr2xstateflagDRT1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 34),
    _Dualdrr2xstateflagDRT1Status_Type()
)
dualdrr2xstateflagDRT1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagDRT1Status.setStatus("mandatory")


class _Dualdrr2xlabelSFP0Status_Type(DisplayString):
    """Custom type dualdrr2xlabelSFP0Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelSFP0Status_Type.__name__ = "DisplayString"
_Dualdrr2xlabelSFP0Status_Object = MibTableColumn
dualdrr2xlabelSFP0Status = _Dualdrr2xlabelSFP0Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 35),
    _Dualdrr2xlabelSFP0Status_Type()
)
dualdrr2xlabelSFP0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelSFP0Status.setStatus("optional")


class _Dualdrr2xvalueSFP0Status_Type(Integer32):
    """Custom type dualdrr2xvalueSFP0Status based on Integer32"""
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


_Dualdrr2xvalueSFP0Status_Type.__name__ = "Integer32"
_Dualdrr2xvalueSFP0Status_Object = MibTableColumn
dualdrr2xvalueSFP0Status = _Dualdrr2xvalueSFP0Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 36),
    _Dualdrr2xvalueSFP0Status_Type()
)
dualdrr2xvalueSFP0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueSFP0Status.setStatus("mandatory")


class _Dualdrr2xstateflagSFP0Status_Type(Integer32):
    """Custom type dualdrr2xstateflagSFP0Status based on Integer32"""
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


_Dualdrr2xstateflagSFP0Status_Type.__name__ = "Integer32"
_Dualdrr2xstateflagSFP0Status_Object = MibTableColumn
dualdrr2xstateflagSFP0Status = _Dualdrr2xstateflagSFP0Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 37),
    _Dualdrr2xstateflagSFP0Status_Type()
)
dualdrr2xstateflagSFP0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagSFP0Status.setStatus("mandatory")


class _Dualdrr2xlabelDRT2Status_Type(DisplayString):
    """Custom type dualdrr2xlabelDRT2Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelDRT2Status_Type.__name__ = "DisplayString"
_Dualdrr2xlabelDRT2Status_Object = MibTableColumn
dualdrr2xlabelDRT2Status = _Dualdrr2xlabelDRT2Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 38),
    _Dualdrr2xlabelDRT2Status_Type()
)
dualdrr2xlabelDRT2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelDRT2Status.setStatus("optional")


class _Dualdrr2xvalueDRT2Status_Type(Integer32):
    """Custom type dualdrr2xvalueDRT2Status based on Integer32"""
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


_Dualdrr2xvalueDRT2Status_Type.__name__ = "Integer32"
_Dualdrr2xvalueDRT2Status_Object = MibTableColumn
dualdrr2xvalueDRT2Status = _Dualdrr2xvalueDRT2Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 39),
    _Dualdrr2xvalueDRT2Status_Type()
)
dualdrr2xvalueDRT2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueDRT2Status.setStatus("mandatory")


class _Dualdrr2xstateflagDRT2Status_Type(Integer32):
    """Custom type dualdrr2xstateflagDRT2Status based on Integer32"""
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


_Dualdrr2xstateflagDRT2Status_Type.__name__ = "Integer32"
_Dualdrr2xstateflagDRT2Status_Object = MibTableColumn
dualdrr2xstateflagDRT2Status = _Dualdrr2xstateflagDRT2Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 40),
    _Dualdrr2xstateflagDRT2Status_Type()
)
dualdrr2xstateflagDRT2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagDRT2Status.setStatus("mandatory")


class _Dualdrr2xlabelSFP1Status_Type(DisplayString):
    """Custom type dualdrr2xlabelSFP1Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xlabelSFP1Status_Type.__name__ = "DisplayString"
_Dualdrr2xlabelSFP1Status_Object = MibTableColumn
dualdrr2xlabelSFP1Status = _Dualdrr2xlabelSFP1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 41),
    _Dualdrr2xlabelSFP1Status_Type()
)
dualdrr2xlabelSFP1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xlabelSFP1Status.setStatus("optional")


class _Dualdrr2xvalueSFP1Status_Type(Integer32):
    """Custom type dualdrr2xvalueSFP1Status based on Integer32"""
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


_Dualdrr2xvalueSFP1Status_Type.__name__ = "Integer32"
_Dualdrr2xvalueSFP1Status_Object = MibTableColumn
dualdrr2xvalueSFP1Status = _Dualdrr2xvalueSFP1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 42),
    _Dualdrr2xvalueSFP1Status_Type()
)
dualdrr2xvalueSFP1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xvalueSFP1Status.setStatus("mandatory")


class _Dualdrr2xstateflagSFP1Status_Type(Integer32):
    """Custom type dualdrr2xstateflagSFP1Status based on Integer32"""
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


_Dualdrr2xstateflagSFP1Status_Type.__name__ = "Integer32"
_Dualdrr2xstateflagSFP1Status_Object = MibTableColumn
dualdrr2xstateflagSFP1Status = _Dualdrr2xstateflagSFP1Status_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 4, 3, 43),
    _Dualdrr2xstateflagSFP1Status_Type()
)
dualdrr2xstateflagSFP1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xstateflagSFP1Status.setStatus("mandatory")
_Gx2dualdrr2xFactoryTable_Object = MibTable
gx2dualdrr2xFactoryTable = _Gx2dualdrr2xFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5)
)
if mibBuilder.loadTexts:
    gx2dualdrr2xFactoryTable.setStatus("mandatory")
_Gx2dualdrr2xFactoryEntry_Object = MibTableRow
gx2dualdrr2xFactoryEntry = _Gx2dualdrr2xFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4)
)
gx2dualdrr2xFactoryEntry.setIndexNames(
    (0, "OMNI-gx2dualdrr2x-MIB", "gx2dualdrr2xFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2dualdrr2xFactoryEntry.setStatus("mandatory")


class _Gx2dualdrr2xFactoryTableIndex_Type(Integer32):
    """Custom type gx2dualdrr2xFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2dualdrr2xFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2dualdrr2xFactoryTableIndex_Object = MibTableColumn
gx2dualdrr2xFactoryTableIndex = _Gx2dualdrr2xFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 1),
    _Gx2dualdrr2xFactoryTableIndex_Type()
)
gx2dualdrr2xFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2dualdrr2xFactoryTableIndex.setStatus("mandatory")
_Dualdrr2xbootControlByte_Type = Integer32
_Dualdrr2xbootControlByte_Object = MibTableColumn
dualdrr2xbootControlByte = _Dualdrr2xbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 2),
    _Dualdrr2xbootControlByte_Type()
)
dualdrr2xbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xbootControlByte.setStatus("mandatory")
_Dualdrr2xbootStatusByte_Type = Integer32
_Dualdrr2xbootStatusByte_Object = MibTableColumn
dualdrr2xbootStatusByte = _Dualdrr2xbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 3),
    _Dualdrr2xbootStatusByte_Type()
)
dualdrr2xbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xbootStatusByte.setStatus("mandatory")
_Dualdrr2xbank1CRC_Type = Integer32
_Dualdrr2xbank1CRC_Object = MibTableColumn
dualdrr2xbank1CRC = _Dualdrr2xbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 4),
    _Dualdrr2xbank1CRC_Type()
)
dualdrr2xbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xbank1CRC.setStatus("mandatory")
_Dualdrr2xbank2CRC_Type = Integer32
_Dualdrr2xbank2CRC_Object = MibTableColumn
dualdrr2xbank2CRC = _Dualdrr2xbank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 5),
    _Dualdrr2xbank2CRC_Type()
)
dualdrr2xbank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xbank2CRC.setStatus("mandatory")
_Dualdrr2xprgEEPROMByte_Type = Integer32
_Dualdrr2xprgEEPROMByte_Object = MibTableColumn
dualdrr2xprgEEPROMByte = _Dualdrr2xprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 6),
    _Dualdrr2xprgEEPROMByte_Type()
)
dualdrr2xprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xprgEEPROMByte.setStatus("mandatory")
_Dualdrr2xfactoryCRC_Type = Integer32
_Dualdrr2xfactoryCRC_Object = MibTableColumn
dualdrr2xfactoryCRC = _Dualdrr2xfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 7),
    _Dualdrr2xfactoryCRC_Type()
)
dualdrr2xfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xfactoryCRC.setStatus("mandatory")


class _Dualdrr2xcalculateCRC_Type(Integer32):
    """Custom type dualdrr2xcalculateCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("calibration", 3),
          ("factory", 1))
    )


_Dualdrr2xcalculateCRC_Type.__name__ = "Integer32"
_Dualdrr2xcalculateCRC_Object = MibTableColumn
dualdrr2xcalculateCRC = _Dualdrr2xcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 8),
    _Dualdrr2xcalculateCRC_Type()
)
dualdrr2xcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xcalculateCRC.setStatus("mandatory")
_Dualdrr2xhourMeter_Type = Integer32
_Dualdrr2xhourMeter_Object = MibTableColumn
dualdrr2xhourMeter = _Dualdrr2xhourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 9),
    _Dualdrr2xhourMeter_Type()
)
dualdrr2xhourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xhourMeter.setStatus("mandatory")
_Dualdrr2xflashPrgCntA_Type = Integer32
_Dualdrr2xflashPrgCntA_Object = MibTableColumn
dualdrr2xflashPrgCntA = _Dualdrr2xflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 10),
    _Dualdrr2xflashPrgCntA_Type()
)
dualdrr2xflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xflashPrgCntA.setStatus("mandatory")
_Dualdrr2xflashPrgCntB_Type = Integer32
_Dualdrr2xflashPrgCntB_Object = MibTableColumn
dualdrr2xflashPrgCntB = _Dualdrr2xflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 11),
    _Dualdrr2xflashPrgCntB_Type()
)
dualdrr2xflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xflashPrgCntB.setStatus("mandatory")


class _Dualdrr2xflashBankARev_Type(DisplayString):
    """Custom type dualdrr2xflashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xflashBankARev_Type.__name__ = "DisplayString"
_Dualdrr2xflashBankARev_Object = MibTableColumn
dualdrr2xflashBankARev = _Dualdrr2xflashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 12),
    _Dualdrr2xflashBankARev_Type()
)
dualdrr2xflashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xflashBankARev.setStatus("mandatory")


class _Dualdrr2xflashBankBRev_Type(DisplayString):
    """Custom type dualdrr2xflashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xflashBankBRev_Type.__name__ = "DisplayString"
_Dualdrr2xflashBankBRev_Object = MibTableColumn
dualdrr2xflashBankBRev = _Dualdrr2xflashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 13),
    _Dualdrr2xflashBankBRev_Type()
)
dualdrr2xflashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xflashBankBRev.setStatus("mandatory")


class _Dualdrr2xSubAgentRev_Type(DisplayString):
    """Custom type dualdrr2xSubAgentRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xSubAgentRev_Type.__name__ = "DisplayString"
_Dualdrr2xSubAgentRev_Object = MibTableColumn
dualdrr2xSubAgentRev = _Dualdrr2xSubAgentRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 14),
    _Dualdrr2xSubAgentRev_Type()
)
dualdrr2xSubAgentRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xSubAgentRev.setStatus("mandatory")


class _Dualdrr2xFPGA0FwRev_Type(DisplayString):
    """Custom type dualdrr2xFPGA0FwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xFPGA0FwRev_Type.__name__ = "DisplayString"
_Dualdrr2xFPGA0FwRev_Object = MibTableColumn
dualdrr2xFPGA0FwRev = _Dualdrr2xFPGA0FwRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 15),
    _Dualdrr2xFPGA0FwRev_Type()
)
dualdrr2xFPGA0FwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xFPGA0FwRev.setStatus("mandatory")


class _Dualdrr2xFPGA1FwRev_Type(DisplayString):
    """Custom type dualdrr2xFPGA1FwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xFPGA1FwRev_Type.__name__ = "DisplayString"
_Dualdrr2xFPGA1FwRev_Object = MibTableColumn
dualdrr2xFPGA1FwRev = _Dualdrr2xFPGA1FwRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 16),
    _Dualdrr2xFPGA1FwRev_Type()
)
dualdrr2xFPGA1FwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xFPGA1FwRev.setStatus("mandatory")


class _Dualdrr2xDRT1SerialNo_Type(DisplayString):
    """Custom type dualdrr2xDRT1SerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT1SerialNo_Type.__name__ = "DisplayString"
_Dualdrr2xDRT1SerialNo_Object = MibTableColumn
dualdrr2xDRT1SerialNo = _Dualdrr2xDRT1SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 17),
    _Dualdrr2xDRT1SerialNo_Type()
)
dualdrr2xDRT1SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT1SerialNo.setStatus("mandatory")


class _Dualdrr2xDRT1SFPSerialNo_Type(DisplayString):
    """Custom type dualdrr2xDRT1SFPSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT1SFPSerialNo_Type.__name__ = "DisplayString"
_Dualdrr2xDRT1SFPSerialNo_Object = MibTableColumn
dualdrr2xDRT1SFPSerialNo = _Dualdrr2xDRT1SFPSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 18),
    _Dualdrr2xDRT1SFPSerialNo_Type()
)
dualdrr2xDRT1SFPSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT1SFPSerialNo.setStatus("mandatory")


class _Dualdrr2xDRT1SFPPartNo_Type(DisplayString):
    """Custom type dualdrr2xDRT1SFPPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT1SFPPartNo_Type.__name__ = "DisplayString"
_Dualdrr2xDRT1SFPPartNo_Object = MibTableColumn
dualdrr2xDRT1SFPPartNo = _Dualdrr2xDRT1SFPPartNo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 19),
    _Dualdrr2xDRT1SFPPartNo_Type()
)
dualdrr2xDRT1SFPPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT1SFPPartNo.setStatus("mandatory")


class _Dualdrr2xDRT1FwRev_Type(DisplayString):
    """Custom type dualdrr2xDRT1FwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT1FwRev_Type.__name__ = "DisplayString"
_Dualdrr2xDRT1FwRev_Object = MibTableColumn
dualdrr2xDRT1FwRev = _Dualdrr2xDRT1FwRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 20),
    _Dualdrr2xDRT1FwRev_Type()
)
dualdrr2xDRT1FwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT1FwRev.setStatus("mandatory")


class _Dualdrr2xDRT1FpgaFwRev_Type(DisplayString):
    """Custom type dualdrr2xDRT1FpgaFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT1FpgaFwRev_Type.__name__ = "DisplayString"
_Dualdrr2xDRT1FpgaFwRev_Object = MibTableColumn
dualdrr2xDRT1FpgaFwRev = _Dualdrr2xDRT1FpgaFwRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 21),
    _Dualdrr2xDRT1FpgaFwRev_Type()
)
dualdrr2xDRT1FpgaFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT1FpgaFwRev.setStatus("mandatory")


class _Dualdrr2xDRT2SerialNo_Type(DisplayString):
    """Custom type dualdrr2xDRT2SerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT2SerialNo_Type.__name__ = "DisplayString"
_Dualdrr2xDRT2SerialNo_Object = MibTableColumn
dualdrr2xDRT2SerialNo = _Dualdrr2xDRT2SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 22),
    _Dualdrr2xDRT2SerialNo_Type()
)
dualdrr2xDRT2SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT2SerialNo.setStatus("mandatory")


class _Dualdrr2xDRT2SFPSerialNo_Type(DisplayString):
    """Custom type dualdrr2xDRT2SFPSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT2SFPSerialNo_Type.__name__ = "DisplayString"
_Dualdrr2xDRT2SFPSerialNo_Object = MibTableColumn
dualdrr2xDRT2SFPSerialNo = _Dualdrr2xDRT2SFPSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 23),
    _Dualdrr2xDRT2SFPSerialNo_Type()
)
dualdrr2xDRT2SFPSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT2SFPSerialNo.setStatus("mandatory")


class _Dualdrr2xDRT2SFPPartNo_Type(DisplayString):
    """Custom type dualdrr2xDRT2SFPPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT2SFPPartNo_Type.__name__ = "DisplayString"
_Dualdrr2xDRT2SFPPartNo_Object = MibTableColumn
dualdrr2xDRT2SFPPartNo = _Dualdrr2xDRT2SFPPartNo_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 24),
    _Dualdrr2xDRT2SFPPartNo_Type()
)
dualdrr2xDRT2SFPPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT2SFPPartNo.setStatus("mandatory")


class _Dualdrr2xDRT2FwRev_Type(DisplayString):
    """Custom type dualdrr2xDRT2FwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT2FwRev_Type.__name__ = "DisplayString"
_Dualdrr2xDRT2FwRev_Object = MibTableColumn
dualdrr2xDRT2FwRev = _Dualdrr2xDRT2FwRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 25),
    _Dualdrr2xDRT2FwRev_Type()
)
dualdrr2xDRT2FwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT2FwRev.setStatus("mandatory")


class _Dualdrr2xDRT2FpgaFwRev_Type(DisplayString):
    """Custom type dualdrr2xDRT2FpgaFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Dualdrr2xDRT2FpgaFwRev_Type.__name__ = "DisplayString"
_Dualdrr2xDRT2FpgaFwRev_Object = MibTableColumn
dualdrr2xDRT2FpgaFwRev = _Dualdrr2xDRT2FpgaFwRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 5, 4, 26),
    _Dualdrr2xDRT2FpgaFwRev_Type()
)
dualdrr2xDRT2FpgaFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualdrr2xDRT2FpgaFwRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapdualdrrConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 1)
)
trapdualdrrConfigChangeInteger.setObjects(
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
    trapdualdrrConfigChangeInteger.setStatus(
        ""
    )

trapdualdrrConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 2)
)
trapdualdrrConfigChangeDisplayString.setObjects(
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
    trapdualdrrConfigChangeDisplayString.setStatus(
        ""
    )

trapdualdrr12VCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 3)
)
trapdualdrr12VCurrentAlarm.setObjects(
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
    trapdualdrr12VCurrentAlarm.setStatus(
        ""
    )

trapdualdrrModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 4)
)
trapdualdrrModuleTempAlarm.setObjects(
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
    trapdualdrrModuleTempAlarm.setStatus(
        ""
    )

trapdualdrrFanSpeedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 5)
)
trapdualdrrFanSpeedAlarm.setObjects(
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
    trapdualdrrFanSpeedAlarm.setStatus(
        ""
    )

trapdualdrrFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 6)
)
trapdualdrrFlashAlarm.setObjects(
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
    trapdualdrrFlashAlarm.setStatus(
        ""
    )

trapdualdrrBankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 7)
)
trapdualdrrBankBootAlarm.setObjects(
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
    trapdualdrrBankBootAlarm.setStatus(
        ""
    )

trapdualdrrAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 8)
)
trapdualdrrAlarmDataCRCAlarm.setObjects(
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
    trapdualdrrAlarmDataCRCAlarm.setStatus(
        ""
    )

trapdualdrrHardwareErrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 9)
)
trapdualdrrHardwareErrAlarm.setObjects(
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
    trapdualdrrHardwareErrAlarm.setStatus(
        ""
    )

trapdualdrrOpticalSignal1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 10)
)
trapdualdrrOpticalSignal1Alarm.setObjects(
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
    trapdualdrrOpticalSignal1Alarm.setStatus(
        ""
    )

trapdualdrrOpticalSignal2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 11)
)
trapdualdrrOpticalSignal2Alarm.setObjects(
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
    trapdualdrrOpticalSignal2Alarm.setStatus(
        ""
    )

trapdualdrrFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 12)
)
trapdualdrrFactoryDataCRCAlarm.setObjects(
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
    trapdualdrrFactoryDataCRCAlarm.setStatus(
        ""
    )

trapdualdrrResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 13)
)
trapdualdrrResetFactoryDefaultAlarm.setObjects(
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
    trapdualdrrResetFactoryDefaultAlarm.setStatus(
        ""
    )

trapdualdrrTripPoint1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 14)
)
trapdualdrrTripPoint1Alarm.setObjects(
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
    trapdualdrrTripPoint1Alarm.setStatus(
        ""
    )

trapdualdrrTripPoint2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 15)
)
trapdualdrrTripPoint2Alarm.setObjects(
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
    trapdualdrrTripPoint2Alarm.setStatus(
        ""
    )

trapdualdrrLink1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 16)
)
trapdualdrrLink1Alarm.setObjects(
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
    trapdualdrrLink1Alarm.setStatus(
        ""
    )

trapdualdrrLink2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 17)
)
trapdualdrrLink2Alarm.setObjects(
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
    trapdualdrrLink2Alarm.setStatus(
        ""
    )

trapdualdrrCalibrationDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 18)
)
trapdualdrrCalibrationDataCRCAlarm.setObjects(
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
    trapdualdrrCalibrationDataCRCAlarm.setStatus(
        ""
    )

trapdualdrrSFP1OptPWRAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 19)
)
trapdualdrrSFP1OptPWRAlarm.setObjects(
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
    trapdualdrrSFP1OptPWRAlarm.setStatus(
        ""
    )

trapdualdrrDRT1Cur24VAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 20)
)
trapdualdrrDRT1Cur24VAlarm.setObjects(
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
    trapdualdrrDRT1Cur24VAlarm.setStatus(
        ""
    )

trapdualdrrDRT1ModTempAarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 21)
)
trapdualdrrDRT1ModTempAarm.setObjects(
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
    trapdualdrrDRT1ModTempAarm.setStatus(
        ""
    )

trapdualdrrSFP2OptPWRAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 22)
)
trapdualdrrSFP2OptPWRAlarm.setObjects(
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
    trapdualdrrSFP2OptPWRAlarm.setStatus(
        ""
    )

trapdualdrrDRT2Cur24VAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 23)
)
trapdualdrrDRT2Cur24VAlarm.setObjects(
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
    trapdualdrrDRT2Cur24VAlarm.setStatus(
        ""
    )

trapdualdrrDRT2ModTempAarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35, 0, 24)
)
trapdualdrrDRT2ModTempAarm.setObjects(
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
    trapdualdrrDRT2ModTempAarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2dualdrr2x-MIB",
    **{"Float": Float,
       "trapdualdrrConfigChangeInteger": trapdualdrrConfigChangeInteger,
       "trapdualdrrConfigChangeDisplayString": trapdualdrrConfigChangeDisplayString,
       "trapdualdrr12VCurrentAlarm": trapdualdrr12VCurrentAlarm,
       "trapdualdrrModuleTempAlarm": trapdualdrrModuleTempAlarm,
       "trapdualdrrFanSpeedAlarm": trapdualdrrFanSpeedAlarm,
       "trapdualdrrFlashAlarm": trapdualdrrFlashAlarm,
       "trapdualdrrBankBootAlarm": trapdualdrrBankBootAlarm,
       "trapdualdrrAlarmDataCRCAlarm": trapdualdrrAlarmDataCRCAlarm,
       "trapdualdrrHardwareErrAlarm": trapdualdrrHardwareErrAlarm,
       "trapdualdrrOpticalSignal1Alarm": trapdualdrrOpticalSignal1Alarm,
       "trapdualdrrOpticalSignal2Alarm": trapdualdrrOpticalSignal2Alarm,
       "trapdualdrrFactoryDataCRCAlarm": trapdualdrrFactoryDataCRCAlarm,
       "trapdualdrrResetFactoryDefaultAlarm": trapdualdrrResetFactoryDefaultAlarm,
       "trapdualdrrTripPoint1Alarm": trapdualdrrTripPoint1Alarm,
       "trapdualdrrTripPoint2Alarm": trapdualdrrTripPoint2Alarm,
       "trapdualdrrLink1Alarm": trapdualdrrLink1Alarm,
       "trapdualdrrLink2Alarm": trapdualdrrLink2Alarm,
       "trapdualdrrCalibrationDataCRCAlarm": trapdualdrrCalibrationDataCRCAlarm,
       "trapdualdrrSFP1OptPWRAlarm": trapdualdrrSFP1OptPWRAlarm,
       "trapdualdrrDRT1Cur24VAlarm": trapdualdrrDRT1Cur24VAlarm,
       "trapdualdrrDRT1ModTempAarm": trapdualdrrDRT1ModTempAarm,
       "trapdualdrrSFP2OptPWRAlarm": trapdualdrrSFP2OptPWRAlarm,
       "trapdualdrrDRT2Cur24VAlarm": trapdualdrrDRT2Cur24VAlarm,
       "trapdualdrrDRT2ModTempAarm": trapdualdrrDRT2ModTempAarm,
       "gx2dualdrr2xDescriptor": gx2dualdrr2xDescriptor,
       "gx2dualdrr2xAnalogTable": gx2dualdrr2xAnalogTable,
       "gx2dualdrr2xAnalogEntry": gx2dualdrr2xAnalogEntry,
       "gx2dualdrr2xAnalogTableIndex": gx2dualdrr2xAnalogTableIndex,
       "dualdrr2xlabelRecdOptPwr1": dualdrr2xlabelRecdOptPwr1,
       "dualdrr2xuomRecdOptPwr1": dualdrr2xuomRecdOptPwr1,
       "dualdrr2xmajorHighRecdOptPwr1": dualdrr2xmajorHighRecdOptPwr1,
       "dualdrr2xmajorLowRecdOptPwr1": dualdrr2xmajorLowRecdOptPwr1,
       "dualdrr2xminorHighRecdOptPwr1": dualdrr2xminorHighRecdOptPwr1,
       "dualdrr2xminorLowRecdOptPwr1": dualdrr2xminorLowRecdOptPwr1,
       "dualdrr2xcurrentValueRecdOptPwr1": dualdrr2xcurrentValueRecdOptPwr1,
       "dualdrr2xstateFlagRecdOptPwr1": dualdrr2xstateFlagRecdOptPwr1,
       "dualdrr2xminValueRecdOptPwr1": dualdrr2xminValueRecdOptPwr1,
       "dualdrr2xmaxValueRecdOptPwr1": dualdrr2xmaxValueRecdOptPwr1,
       "dualdrr2xalarmStateRecdOptPwr1": dualdrr2xalarmStateRecdOptPwr1,
       "dualdrr2xlabelRecdOptPwr2": dualdrr2xlabelRecdOptPwr2,
       "dualdrr2xuomRecdOptPwr2": dualdrr2xuomRecdOptPwr2,
       "dualdrr2xmajorHighRecdOptPwr2": dualdrr2xmajorHighRecdOptPwr2,
       "dualdrr2xmajorLowRecdOptPwr2": dualdrr2xmajorLowRecdOptPwr2,
       "dualdrr2xminorHighRecdOptPwr2": dualdrr2xminorHighRecdOptPwr2,
       "dualdrr2xminorLowRecdOptPwr2": dualdrr2xminorLowRecdOptPwr2,
       "dualdrr2xcurrentValueRecdOptPwr2": dualdrr2xcurrentValueRecdOptPwr2,
       "dualdrr2xstateFlagRecdOptPwr2": dualdrr2xstateFlagRecdOptPwr2,
       "dualdrr2xminValueRecdOptPwr2": dualdrr2xminValueRecdOptPwr2,
       "dualdrr2xmaxValueRecdOptPwr2": dualdrr2xmaxValueRecdOptPwr2,
       "dualdrr2xalarmStateRecdOptPwr2": dualdrr2xalarmStateRecdOptPwr2,
       "dualdrr2xlabelModTemp": dualdrr2xlabelModTemp,
       "dualdrr2xuomModTemp": dualdrr2xuomModTemp,
       "dualdrr2xmajorHighModTemp": dualdrr2xmajorHighModTemp,
       "dualdrr2xmajorLowModTemp": dualdrr2xmajorLowModTemp,
       "dualdrr2xminorHighModTemp": dualdrr2xminorHighModTemp,
       "dualdrr2xminorLowModTemp": dualdrr2xminorLowModTemp,
       "dualdrr2xcurrentValueModTemp": dualdrr2xcurrentValueModTemp,
       "dualdrr2xstateFlagModTemp": dualdrr2xstateFlagModTemp,
       "dualdrr2xminValueModTemp": dualdrr2xminValueModTemp,
       "dualdrr2xmaxValueModTemp": dualdrr2xmaxValueModTemp,
       "dualdrr2xalarmStateModTemp": dualdrr2xalarmStateModTemp,
       "dualdrr2xlabel12VCurrent": dualdrr2xlabel12VCurrent,
       "dualdrr2xuom12VCurrent": dualdrr2xuom12VCurrent,
       "dualdrr2xmajorHigh12VCurrent": dualdrr2xmajorHigh12VCurrent,
       "dualdrr2xmajorLow12VCurrent": dualdrr2xmajorLow12VCurrent,
       "dualdrr2xminorHigh12VCurrent": dualdrr2xminorHigh12VCurrent,
       "dualdrr2xminorLow12VCurrent": dualdrr2xminorLow12VCurrent,
       "dualdrr2xcurrentValue12VCurrent": dualdrr2xcurrentValue12VCurrent,
       "dualdrr2xstateFlag12VCurrent": dualdrr2xstateFlag12VCurrent,
       "dualdrr2xminValue12VCurrent": dualdrr2xminValue12VCurrent,
       "dualdrr2xmaxValue12VCurrent": dualdrr2xmaxValue12VCurrent,
       "dualdrr2xalarmState12VCurrent": dualdrr2xalarmState12VCurrent,
       "dualdrr2xlabelFanSpeed": dualdrr2xlabelFanSpeed,
       "dualdrr2xuomFanSpeed": dualdrr2xuomFanSpeed,
       "dualdrr2xmajorHighFanSpeed": dualdrr2xmajorHighFanSpeed,
       "dualdrr2xmajorLowFanSpeed": dualdrr2xmajorLowFanSpeed,
       "dualdrr2xminorHighFanSpeed": dualdrr2xminorHighFanSpeed,
       "dualdrr2xminorLowFanSpeed": dualdrr2xminorLowFanSpeed,
       "dualdrr2xcurrentValueFanSpeed": dualdrr2xcurrentValueFanSpeed,
       "dualdrr2xstateFlagFanSpeed": dualdrr2xstateFlagFanSpeed,
       "dualdrr2xminValueFanSpeed": dualdrr2xminValueFanSpeed,
       "dualdrr2xmaxValueFanSpeed": dualdrr2xmaxValueFanSpeed,
       "dualdrr2xalarmStateFanSpeed": dualdrr2xalarmStateFanSpeed,
       "dualdrr2xlabelTx0SFPWave": dualdrr2xlabelTx0SFPWave,
       "dualdrr2xuomTx0SFPWave": dualdrr2xuomTx0SFPWave,
       "dualdrr2xmajorHighTx0SFPWave": dualdrr2xmajorHighTx0SFPWave,
       "dualdrr2xmajorLowTx0SFPWave": dualdrr2xmajorLowTx0SFPWave,
       "dualdrr2xminorHighTx0SFPWave": dualdrr2xminorHighTx0SFPWave,
       "dualdrr2xminorLowTx0SFPWave": dualdrr2xminorLowTx0SFPWave,
       "dualdrr2xcurrentValueTx0SFPWave": dualdrr2xcurrentValueTx0SFPWave,
       "dualdrr2xstateFlagTx0SFPWave": dualdrr2xstateFlagTx0SFPWave,
       "dualdrr2xminValueTx0SFPWave": dualdrr2xminValueTx0SFPWave,
       "dualdrr2xmaxValueTx0SFPWave": dualdrr2xmaxValueTx0SFPWave,
       "dualdrr2xalarmStateTx0SFPWave": dualdrr2xalarmStateTx0SFPWave,
       "dualdrr2xlabelTx0OptPwr": dualdrr2xlabelTx0OptPwr,
       "dualdrr2xuomTx0OptPwr": dualdrr2xuomTx0OptPwr,
       "dualdrr2xmajorHighTx0OptPwr": dualdrr2xmajorHighTx0OptPwr,
       "dualdrr2xmajorLowTx0OptPwr": dualdrr2xmajorLowTx0OptPwr,
       "dualdrr2xminorHighTx0OptPwr": dualdrr2xminorHighTx0OptPwr,
       "dualdrr2xminorLowTx0OptPwr": dualdrr2xminorLowTx0OptPwr,
       "dualdrr2xcurrentValueTx0OptPwr": dualdrr2xcurrentValueTx0OptPwr,
       "dualdrr2xstateFlagTx0OptPwr": dualdrr2xstateFlagTx0OptPwr,
       "dualdrr2xminValueTx0OptPwr": dualdrr2xminValueTx0OptPwr,
       "dualdrr2xmaxValueTx0OptPwr": dualdrr2xmaxValueTx0OptPwr,
       "dualdrr2xalarmStateTx0OptPwr": dualdrr2xalarmStateTx0OptPwr,
       "dualdrr2xlabelTx024vCurr": dualdrr2xlabelTx024vCurr,
       "dualdrr2xuomTx024vCurr": dualdrr2xuomTx024vCurr,
       "dualdrr2xmajorHighTx024vCurr": dualdrr2xmajorHighTx024vCurr,
       "dualdrr2xmajorLowTx024vCurr": dualdrr2xmajorLowTx024vCurr,
       "dualdrr2xminorHighTx024vCurr": dualdrr2xminorHighTx024vCurr,
       "dualdrr2xminorLowTx024vCurr": dualdrr2xminorLowTx024vCurr,
       "dualdrr2xcurrentValueTx024vCurr": dualdrr2xcurrentValueTx024vCurr,
       "dualdrr2xstateFlagTx024vCurr": dualdrr2xstateFlagTx024vCurr,
       "dualdrr2xminValueTx024vCurr": dualdrr2xminValueTx024vCurr,
       "dualdrr2xmaxValueTx024vCurr": dualdrr2xmaxValueTx024vCurr,
       "dualdrr2xalarmStateTx024vCurr": dualdrr2xalarmStateTx024vCurr,
       "dualdrr2xlabelTx024Volt": dualdrr2xlabelTx024Volt,
       "dualdrr2xuomTx024Volt": dualdrr2xuomTx024Volt,
       "dualdrr2xmajorHighTx024Volt": dualdrr2xmajorHighTx024Volt,
       "dualdrr2xmajorLowTx024Volt": dualdrr2xmajorLowTx024Volt,
       "dualdrr2xminorHighTx024Volt": dualdrr2xminorHighTx024Volt,
       "dualdrr2xminorLowTx024Volt": dualdrr2xminorLowTx024Volt,
       "dualdrr2xcurrentValueTx024Volt": dualdrr2xcurrentValueTx024Volt,
       "dualdrr2xstateFlagTx024Volt": dualdrr2xstateFlagTx024Volt,
       "dualdrr2xminValueTx024Volt": dualdrr2xminValueTx024Volt,
       "dualdrr2xmaxValueTx024Volt": dualdrr2xmaxValueTx024Volt,
       "dualdrr2xalarmStateTx024Volt": dualdrr2xalarmStateTx024Volt,
       "dualdrr2xlabelTx0ModTemp": dualdrr2xlabelTx0ModTemp,
       "dualdrr2xuomTx0ModTemp": dualdrr2xuomTx0ModTemp,
       "dualdrr2xmajorHighTx0ModTemp": dualdrr2xmajorHighTx0ModTemp,
       "dualdrr2xmajorLowTx0ModTemp": dualdrr2xmajorLowTx0ModTemp,
       "dualdrr2xminorHighTx0ModTemp": dualdrr2xminorHighTx0ModTemp,
       "dualdrr2xminorLowTx0ModTemp": dualdrr2xminorLowTx0ModTemp,
       "dualdrr2xcurrentValueTx0ModTemp": dualdrr2xcurrentValueTx0ModTemp,
       "dualdrr2xstateFlagTx0ModTemp": dualdrr2xstateFlagTx0ModTemp,
       "dualdrr2xminValueTx0ModTemp": dualdrr2xminValueTx0ModTemp,
       "dualdrr2xmaxValueTx0ModTemp": dualdrr2xmaxValueTx0ModTemp,
       "dualdrr2xalarmStateTx0ModTemp": dualdrr2xalarmStateTx0ModTemp,
       "dualdrr2xlabelTx1SFPWave": dualdrr2xlabelTx1SFPWave,
       "dualdrr2xuomTx1SFPWave": dualdrr2xuomTx1SFPWave,
       "dualdrr2xmajorHighTx1SFPWave": dualdrr2xmajorHighTx1SFPWave,
       "dualdrr2xmajorLowTx1SFPWave": dualdrr2xmajorLowTx1SFPWave,
       "dualdrr2xminorHighTx1SFPWave": dualdrr2xminorHighTx1SFPWave,
       "dualdrr2xminorLowTx1SFPWave": dualdrr2xminorLowTx1SFPWave,
       "dualdrr2xcurrentValueTx1SFPWave": dualdrr2xcurrentValueTx1SFPWave,
       "dualdrr2xstateFlagTx1SFPWave": dualdrr2xstateFlagTx1SFPWave,
       "dualdrr2xminValueTx1SFPWave": dualdrr2xminValueTx1SFPWave,
       "dualdrr2xmaxValueTx1SFPWave": dualdrr2xmaxValueTx1SFPWave,
       "dualdrr2xalarmStateTx1SFPWave": dualdrr2xalarmStateTx1SFPWave,
       "dualdrr2xlabelTx1OptPwr": dualdrr2xlabelTx1OptPwr,
       "dualdrr2xuomTx1OptPwr": dualdrr2xuomTx1OptPwr,
       "dualdrr2xmajorHighTx1OptPwr": dualdrr2xmajorHighTx1OptPwr,
       "dualdrr2xmajorLowTx1OptPwr": dualdrr2xmajorLowTx1OptPwr,
       "dualdrr2xminorHighTx1OptPwr": dualdrr2xminorHighTx1OptPwr,
       "dualdrr2xminorLowTx1OptPwr": dualdrr2xminorLowTx1OptPwr,
       "dualdrr2xcurrentValueTx1OptPwr": dualdrr2xcurrentValueTx1OptPwr,
       "dualdrr2xstateFlagTx1OptPwr": dualdrr2xstateFlagTx1OptPwr,
       "dualdrr2xminValueTx1OptPwr": dualdrr2xminValueTx1OptPwr,
       "dualdrr2xmaxValueTx1OptPwr": dualdrr2xmaxValueTx1OptPwr,
       "dualdrr2xalarmStateTx1OptPwr": dualdrr2xalarmStateTx1OptPwr,
       "dualdrr2xlabelTx124vCurr": dualdrr2xlabelTx124vCurr,
       "dualdrr2xuomTx124vCurr": dualdrr2xuomTx124vCurr,
       "dualdrr2xmajorHighTx124vCurr": dualdrr2xmajorHighTx124vCurr,
       "dualdrr2xmajorLowTx124vCurr": dualdrr2xmajorLowTx124vCurr,
       "dualdrr2xminorHighTx124vCurr": dualdrr2xminorHighTx124vCurr,
       "dualdrr2xminorLowTx124vCurr": dualdrr2xminorLowTx124vCurr,
       "dualdrr2xcurrentValueTx124vCurr": dualdrr2xcurrentValueTx124vCurr,
       "dualdrr2xstateFlagTx124vCurr": dualdrr2xstateFlagTx124vCurr,
       "dualdrr2xminValueTx124vCurr": dualdrr2xminValueTx124vCurr,
       "dualdrr2xmaxValueTx124vCurr": dualdrr2xmaxValueTx124vCurr,
       "dualdrr2xalarmStateTx124vCurr": dualdrr2xalarmStateTx124vCurr,
       "dualdrr2xlabelTx124Volt": dualdrr2xlabelTx124Volt,
       "dualdrr2xuomTx124Volt": dualdrr2xuomTx124Volt,
       "dualdrr2xmajorHighTx124Volt": dualdrr2xmajorHighTx124Volt,
       "dualdrr2xmajorLowTx124Volt": dualdrr2xmajorLowTx124Volt,
       "dualdrr2xminorHighTx124Volt": dualdrr2xminorHighTx124Volt,
       "dualdrr2xminorLowTx124Volt": dualdrr2xminorLowTx124Volt,
       "dualdrr2xcurrentValueTx124Volt": dualdrr2xcurrentValueTx124Volt,
       "dualdrr2xstateFlagTx124Volt": dualdrr2xstateFlagTx124Volt,
       "dualdrr2xminValueTx124Volt": dualdrr2xminValueTx124Volt,
       "dualdrr2xmaxValueTx124Volt": dualdrr2xmaxValueTx124Volt,
       "dualdrr2xalarmStateTx124Volt": dualdrr2xalarmStateTx124Volt,
       "dualdrr2xlabelTx1ModTemp": dualdrr2xlabelTx1ModTemp,
       "dualdrr2xuomTx1ModTemp": dualdrr2xuomTx1ModTemp,
       "dualdrr2xmajorHighTx1ModTemp": dualdrr2xmajorHighTx1ModTemp,
       "dualdrr2xmajorLowTx1ModTemp": dualdrr2xmajorLowTx1ModTemp,
       "dualdrr2xminorHighTx1ModTemp": dualdrr2xminorHighTx1ModTemp,
       "dualdrr2xminorLowTx1ModTemp": dualdrr2xminorLowTx1ModTemp,
       "dualdrr2xcurrentValueTx1ModTemp": dualdrr2xcurrentValueTx1ModTemp,
       "dualdrr2xstateFlagTx1ModTemp": dualdrr2xstateFlagTx1ModTemp,
       "dualdrr2xminValueTx1ModTemp": dualdrr2xminValueTx1ModTemp,
       "dualdrr2xmaxValueTx1ModTemp": dualdrr2xmaxValueTx1ModTemp,
       "dualdrr2xalarmStateTx1ModTemp": dualdrr2xalarmStateTx1ModTemp,
       "gx2dualdrr2xDigitalTable": gx2dualdrr2xDigitalTable,
       "gx2dualdrr2xDigitalEntry": gx2dualdrr2xDigitalEntry,
       "gx2dualdrr2xDigitalTableIndex": gx2dualdrr2xDigitalTableIndex,
       "dualdrr2xlabelTrippoint1Value": dualdrr2xlabelTrippoint1Value,
       "dualdrr2xenumTrippoint1Value": dualdrr2xenumTrippoint1Value,
       "dualdrr2xvalueTrippoint1Value": dualdrr2xvalueTrippoint1Value,
       "dualdrr2xstateflagTrippoint1Value": dualdrr2xstateflagTrippoint1Value,
       "dualdrr2xlabelTrippoint1Mode": dualdrr2xlabelTrippoint1Mode,
       "dualdrr2xenumTrippoint1Mode": dualdrr2xenumTrippoint1Mode,
       "dualdrr2xvalueTrippoint1Mode": dualdrr2xvalueTrippoint1Mode,
       "dualdrr2xstateflagTrippoint1Mode": dualdrr2xstateflagTrippoint1Mode,
       "dualdrr2xlabelTrippoint2Value": dualdrr2xlabelTrippoint2Value,
       "dualdrr2xenumTrippoint2Value": dualdrr2xenumTrippoint2Value,
       "dualdrr2xvalueTrippoint2Value": dualdrr2xvalueTrippoint2Value,
       "dualdrr2xstateflagTrippoint2Value": dualdrr2xstateflagTrippoint2Value,
       "dualdrr2xlabelTrippoint2Mode": dualdrr2xlabelTrippoint2Mode,
       "dualdrr2xenumTrippoint2Mode": dualdrr2xenumTrippoint2Mode,
       "dualdrr2xvalueTrippoint2Mode": dualdrr2xvalueTrippoint2Mode,
       "dualdrr2xstateflagTrippoint2Mode": dualdrr2xstateflagTrippoint2Mode,
       "dualdrr2xlabelGainChannel1A": dualdrr2xlabelGainChannel1A,
       "dualdrr2xenumGainChannel1A": dualdrr2xenumGainChannel1A,
       "dualdrr2xvalueGainChannel1A": dualdrr2xvalueGainChannel1A,
       "dualdrr2xstateflagGainChannel1A": dualdrr2xstateflagGainChannel1A,
       "dualdrr2xlabelGainChannel1B": dualdrr2xlabelGainChannel1B,
       "dualdrr2xenumGainChannel1B": dualdrr2xenumGainChannel1B,
       "dualdrr2xvalueGainChannel1B": dualdrr2xvalueGainChannel1B,
       "dualdrr2xstateflagGainChannel1B": dualdrr2xstateflagGainChannel1B,
       "dualdrr2xlabelGainChannel2A": dualdrr2xlabelGainChannel2A,
       "dualdrr2xenumGainChannel2A": dualdrr2xenumGainChannel2A,
       "dualdrr2xvalueGainChannel2A": dualdrr2xvalueGainChannel2A,
       "dualdrr2xstateflagGainChannel2A": dualdrr2xstateflagGainChannel2A,
       "dualdrr2xlabelGainChannel2B": dualdrr2xlabelGainChannel2B,
       "dualdrr2xenumGainChannel2B": dualdrr2xenumGainChannel2B,
       "dualdrr2xvalueGainChannel2B": dualdrr2xvalueGainChannel2B,
       "dualdrr2xstateflagGainChannel2B": dualdrr2xstateflagGainChannel2B,
       "dualdrr2xlabelTestpointSelect": dualdrr2xlabelTestpointSelect,
       "dualdrr2xenumTestpointSelect": dualdrr2xenumTestpointSelect,
       "dualdrr2xvalueTestpointSelect": dualdrr2xvalueTestpointSelect,
       "dualdrr2xstateflagTestpointSelect": dualdrr2xstateflagTestpointSelect,
       "dualdrr2xlabelOpFrequency": dualdrr2xlabelOpFrequency,
       "dualdrr2xenumOpFrequency": dualdrr2xenumOpFrequency,
       "dualdrr2xvalueOpFrequency": dualdrr2xvalueOpFrequency,
       "dualdrr2xstateflagOpFrequency": dualdrr2xstateflagOpFrequency,
       "dualdrr2xlabelActChanSelect": dualdrr2xlabelActChanSelect,
       "dualdrr2xenumActChanSelect": dualdrr2xenumActChanSelect,
       "dualdrr2xvalueActChanSelect": dualdrr2xvalueActChanSelect,
       "dualdrr2xstateflagActChanSelect": dualdrr2xstateflagActChanSelect,
       "dualdrr2xlabelFactoryDefaultReset": dualdrr2xlabelFactoryDefaultReset,
       "dualdrr2xenumFactoryDefaultReset": dualdrr2xenumFactoryDefaultReset,
       "dualdrr2xvalueFactoryDefaultReset": dualdrr2xvalueFactoryDefaultReset,
       "dualdrr2xstateflagFactoryDefaultReset": dualdrr2xstateflagFactoryDefaultReset,
       "gx2dualdrr2xStatusTable": gx2dualdrr2xStatusTable,
       "gx2dualdrr2xStatusEntry": gx2dualdrr2xStatusEntry,
       "gx2dualdrr2xStatusTableIndex": gx2dualdrr2xStatusTableIndex,
       "dualdrr2xlabelBoot": dualdrr2xlabelBoot,
       "dualdrr2xvalueBoot": dualdrr2xvalueBoot,
       "dualdrr2xstateflagBoot": dualdrr2xstateflagBoot,
       "dualdrr2xlabelFlash": dualdrr2xlabelFlash,
       "dualdrr2xvalueFlash": dualdrr2xvalueFlash,
       "dualdrr2xstateflagFlash": dualdrr2xstateflagFlash,
       "dualdrr2xlabelFactoryDataCRC": dualdrr2xlabelFactoryDataCRC,
       "dualdrr2xvalueFactoryDataCRC": dualdrr2xvalueFactoryDataCRC,
       "dualdrr2xstateflagFactoryDataCRC": dualdrr2xstateflagFactoryDataCRC,
       "dualdrr2xlabelAlarmDataCrc": dualdrr2xlabelAlarmDataCrc,
       "dualdrr2xvalueAlarmDataCrc": dualdrr2xvalueAlarmDataCrc,
       "dualdrr2xstateflagAlarmDataCrc": dualdrr2xstateflagAlarmDataCrc,
       "dualdrr2xlabelCalibrationDataCrc": dualdrr2xlabelCalibrationDataCrc,
       "dualdrr2xvalueCalibrationDataCrc": dualdrr2xvalueCalibrationDataCrc,
       "dualdrr2xstateflagCalibrationDataCrc": dualdrr2xstateflagCalibrationDataCrc,
       "dualdrr2xlabelHardwareStatus": dualdrr2xlabelHardwareStatus,
       "dualdrr2xvalueHardwareStatus": dualdrr2xvalueHardwareStatus,
       "dualdrr2xstateflagHardwareStatus": dualdrr2xstateflagHardwareStatus,
       "dualdrr2xlabelCh1TripPointStatus": dualdrr2xlabelCh1TripPointStatus,
       "dualdrr2xvalueCh1TripPointStatus": dualdrr2xvalueCh1TripPointStatus,
       "dualdrr2xstateflagCh1TripPointStatus": dualdrr2xstateflagCh1TripPointStatus,
       "dualdrr2xlabelLink1Status": dualdrr2xlabelLink1Status,
       "dualdrr2xvalueLink1Status": dualdrr2xvalueLink1Status,
       "dualdrr2xstateflagLink1Status": dualdrr2xstateflagLink1Status,
       "dualdrr2xlabelCh2TripPointStatus": dualdrr2xlabelCh2TripPointStatus,
       "dualdrr2xvalueCh2TripPointStatus": dualdrr2xvalueCh2TripPointStatus,
       "dualdrr2xstateflagCh2TripPointStatus": dualdrr2xstateflagCh2TripPointStatus,
       "dualdrr2xlabelLink2Status": dualdrr2xlabelLink2Status,
       "dualdrr2xvalueLink2Status": dualdrr2xvalueLink2Status,
       "dualdrr2xstateflagLink2Status": dualdrr2xstateflagLink2Status,
       "dualdrr2xlabelDRT1Status": dualdrr2xlabelDRT1Status,
       "dualdrr2xvalueDRT1Status": dualdrr2xvalueDRT1Status,
       "dualdrr2xstateflagDRT1Status": dualdrr2xstateflagDRT1Status,
       "dualdrr2xlabelSFP0Status": dualdrr2xlabelSFP0Status,
       "dualdrr2xvalueSFP0Status": dualdrr2xvalueSFP0Status,
       "dualdrr2xstateflagSFP0Status": dualdrr2xstateflagSFP0Status,
       "dualdrr2xlabelDRT2Status": dualdrr2xlabelDRT2Status,
       "dualdrr2xvalueDRT2Status": dualdrr2xvalueDRT2Status,
       "dualdrr2xstateflagDRT2Status": dualdrr2xstateflagDRT2Status,
       "dualdrr2xlabelSFP1Status": dualdrr2xlabelSFP1Status,
       "dualdrr2xvalueSFP1Status": dualdrr2xvalueSFP1Status,
       "dualdrr2xstateflagSFP1Status": dualdrr2xstateflagSFP1Status,
       "gx2dualdrr2xFactoryTable": gx2dualdrr2xFactoryTable,
       "gx2dualdrr2xFactoryEntry": gx2dualdrr2xFactoryEntry,
       "gx2dualdrr2xFactoryTableIndex": gx2dualdrr2xFactoryTableIndex,
       "dualdrr2xbootControlByte": dualdrr2xbootControlByte,
       "dualdrr2xbootStatusByte": dualdrr2xbootStatusByte,
       "dualdrr2xbank1CRC": dualdrr2xbank1CRC,
       "dualdrr2xbank2CRC": dualdrr2xbank2CRC,
       "dualdrr2xprgEEPROMByte": dualdrr2xprgEEPROMByte,
       "dualdrr2xfactoryCRC": dualdrr2xfactoryCRC,
       "dualdrr2xcalculateCRC": dualdrr2xcalculateCRC,
       "dualdrr2xhourMeter": dualdrr2xhourMeter,
       "dualdrr2xflashPrgCntA": dualdrr2xflashPrgCntA,
       "dualdrr2xflashPrgCntB": dualdrr2xflashPrgCntB,
       "dualdrr2xflashBankARev": dualdrr2xflashBankARev,
       "dualdrr2xflashBankBRev": dualdrr2xflashBankBRev,
       "dualdrr2xSubAgentRev": dualdrr2xSubAgentRev,
       "dualdrr2xFPGA0FwRev": dualdrr2xFPGA0FwRev,
       "dualdrr2xFPGA1FwRev": dualdrr2xFPGA1FwRev,
       "dualdrr2xDRT1SerialNo": dualdrr2xDRT1SerialNo,
       "dualdrr2xDRT1SFPSerialNo": dualdrr2xDRT1SFPSerialNo,
       "dualdrr2xDRT1SFPPartNo": dualdrr2xDRT1SFPPartNo,
       "dualdrr2xDRT1FwRev": dualdrr2xDRT1FwRev,
       "dualdrr2xDRT1FpgaFwRev": dualdrr2xDRT1FpgaFwRev,
       "dualdrr2xDRT2SerialNo": dualdrr2xDRT2SerialNo,
       "dualdrr2xDRT2SFPSerialNo": dualdrr2xDRT2SFPSerialNo,
       "dualdrr2xDRT2SFPPartNo": dualdrr2xDRT2SFPPartNo,
       "dualdrr2xDRT2FwRev": dualdrr2xDRT2FwRev,
       "dualdrr2xDRT2FpgaFwRev": dualdrr2xDRT2FpgaFwRev}
)
