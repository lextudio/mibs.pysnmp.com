# SNMP MIB module (OMNI-gx2drr4x-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2drr4x-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:38 2024
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

(gx2Drr4x,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Drr4x")

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

_Gx2drr4xDescriptor_ObjectIdentity = ObjectIdentity
gx2drr4xDescriptor = _Gx2drr4xDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 1)
)
_Gx2drr4xAnalogTable_Object = MibTable
gx2drr4xAnalogTable = _Gx2drr4xAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    gx2drr4xAnalogTable.setStatus("mandatory")
_Gx2drr4xAnalogEntry_Object = MibTableRow
gx2drr4xAnalogEntry = _Gx2drr4xAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1)
)
gx2drr4xAnalogEntry.setIndexNames(
    (0, "OMNI-gx2drr4x-MIB", "gx2drr4xAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2drr4xAnalogEntry.setStatus("mandatory")


class _Gx2drr4xAnalogTableIndex_Type(Integer32):
    """Custom type gx2drr4xAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2drr4xAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2drr4xAnalogTableIndex_Object = MibTableColumn
gx2drr4xAnalogTableIndex = _Gx2drr4xAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 1),
    _Gx2drr4xAnalogTableIndex_Type()
)
gx2drr4xAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2drr4xAnalogTableIndex.setStatus("mandatory")


class _Drr4xlabelRFAAttenuation_Type(DisplayString):
    """Custom type drr4xlabelRFAAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelRFAAttenuation_Type.__name__ = "DisplayString"
_Drr4xlabelRFAAttenuation_Object = MibTableColumn
drr4xlabelRFAAttenuation = _Drr4xlabelRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 2),
    _Drr4xlabelRFAAttenuation_Type()
)
drr4xlabelRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelRFAAttenuation.setStatus("optional")


class _Drr4xuomRFAAttenuation_Type(DisplayString):
    """Custom type drr4xuomRFAAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xuomRFAAttenuation_Type.__name__ = "DisplayString"
_Drr4xuomRFAAttenuation_Object = MibTableColumn
drr4xuomRFAAttenuation = _Drr4xuomRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 3),
    _Drr4xuomRFAAttenuation_Type()
)
drr4xuomRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xuomRFAAttenuation.setStatus("optional")
_Drr4xmajorHighRFAAttenuation_Type = Float
_Drr4xmajorHighRFAAttenuation_Object = MibTableColumn
drr4xmajorHighRFAAttenuation = _Drr4xmajorHighRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 4),
    _Drr4xmajorHighRFAAttenuation_Type()
)
drr4xmajorHighRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorHighRFAAttenuation.setStatus("obsolete")
_Drr4xmajorLowRFAAttenuation_Type = Float
_Drr4xmajorLowRFAAttenuation_Object = MibTableColumn
drr4xmajorLowRFAAttenuation = _Drr4xmajorLowRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 5),
    _Drr4xmajorLowRFAAttenuation_Type()
)
drr4xmajorLowRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorLowRFAAttenuation.setStatus("obsolete")
_Drr4xminorHighRFAAttenuation_Type = Float
_Drr4xminorHighRFAAttenuation_Object = MibTableColumn
drr4xminorHighRFAAttenuation = _Drr4xminorHighRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 6),
    _Drr4xminorHighRFAAttenuation_Type()
)
drr4xminorHighRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorHighRFAAttenuation.setStatus("obsolete")
_Drr4xminorLowRFAAttenuation_Type = Float
_Drr4xminorLowRFAAttenuation_Object = MibTableColumn
drr4xminorLowRFAAttenuation = _Drr4xminorLowRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 7),
    _Drr4xminorLowRFAAttenuation_Type()
)
drr4xminorLowRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorLowRFAAttenuation.setStatus("obsolete")
_Drr4xcurrentValueRFAAttenuation_Type = Float
_Drr4xcurrentValueRFAAttenuation_Object = MibTableColumn
drr4xcurrentValueRFAAttenuation = _Drr4xcurrentValueRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 8),
    _Drr4xcurrentValueRFAAttenuation_Type()
)
drr4xcurrentValueRFAAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drr4xcurrentValueRFAAttenuation.setStatus("mandatory")


class _Drr4xstateFlagRFAAttenuation_Type(Integer32):
    """Custom type drr4xstateFlagRFAAttenuation based on Integer32"""
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


_Drr4xstateFlagRFAAttenuation_Type.__name__ = "Integer32"
_Drr4xstateFlagRFAAttenuation_Object = MibTableColumn
drr4xstateFlagRFAAttenuation = _Drr4xstateFlagRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 9),
    _Drr4xstateFlagRFAAttenuation_Type()
)
drr4xstateFlagRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateFlagRFAAttenuation.setStatus("mandatory")
_Drr4xminValueRFAAttenuation_Type = Float
_Drr4xminValueRFAAttenuation_Object = MibTableColumn
drr4xminValueRFAAttenuation = _Drr4xminValueRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 10),
    _Drr4xminValueRFAAttenuation_Type()
)
drr4xminValueRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminValueRFAAttenuation.setStatus("mandatory")
_Drr4xmaxValueRFAAttenuation_Type = Float
_Drr4xmaxValueRFAAttenuation_Object = MibTableColumn
drr4xmaxValueRFAAttenuation = _Drr4xmaxValueRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 11),
    _Drr4xmaxValueRFAAttenuation_Type()
)
drr4xmaxValueRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmaxValueRFAAttenuation.setStatus("mandatory")


class _Drr4xalarmStateRFAAttenuation_Type(Integer32):
    """Custom type drr4xalarmStateRFAAttenuation based on Integer32"""
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


_Drr4xalarmStateRFAAttenuation_Type.__name__ = "Integer32"
_Drr4xalarmStateRFAAttenuation_Object = MibTableColumn
drr4xalarmStateRFAAttenuation = _Drr4xalarmStateRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 12),
    _Drr4xalarmStateRFAAttenuation_Type()
)
drr4xalarmStateRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xalarmStateRFAAttenuation.setStatus("mandatory")


class _Drr4xlabelRFBAttenuation_Type(DisplayString):
    """Custom type drr4xlabelRFBAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelRFBAttenuation_Type.__name__ = "DisplayString"
_Drr4xlabelRFBAttenuation_Object = MibTableColumn
drr4xlabelRFBAttenuation = _Drr4xlabelRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 13),
    _Drr4xlabelRFBAttenuation_Type()
)
drr4xlabelRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelRFBAttenuation.setStatus("optional")


class _Drr4xuomRFBAttenuation_Type(DisplayString):
    """Custom type drr4xuomRFBAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xuomRFBAttenuation_Type.__name__ = "DisplayString"
_Drr4xuomRFBAttenuation_Object = MibTableColumn
drr4xuomRFBAttenuation = _Drr4xuomRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 14),
    _Drr4xuomRFBAttenuation_Type()
)
drr4xuomRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xuomRFBAttenuation.setStatus("optional")
_Drr4xmajorHighRFBAttenuation_Type = Float
_Drr4xmajorHighRFBAttenuation_Object = MibTableColumn
drr4xmajorHighRFBAttenuation = _Drr4xmajorHighRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 15),
    _Drr4xmajorHighRFBAttenuation_Type()
)
drr4xmajorHighRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorHighRFBAttenuation.setStatus("obsolete")
_Drr4xmajorLowRFBAttenuation_Type = Float
_Drr4xmajorLowRFBAttenuation_Object = MibTableColumn
drr4xmajorLowRFBAttenuation = _Drr4xmajorLowRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 16),
    _Drr4xmajorLowRFBAttenuation_Type()
)
drr4xmajorLowRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorLowRFBAttenuation.setStatus("obsolete")
_Drr4xminorHighRFBAttenuation_Type = Float
_Drr4xminorHighRFBAttenuation_Object = MibTableColumn
drr4xminorHighRFBAttenuation = _Drr4xminorHighRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 17),
    _Drr4xminorHighRFBAttenuation_Type()
)
drr4xminorHighRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorHighRFBAttenuation.setStatus("obsolete")
_Drr4xminorLowRFBAttenuation_Type = Float
_Drr4xminorLowRFBAttenuation_Object = MibTableColumn
drr4xminorLowRFBAttenuation = _Drr4xminorLowRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 18),
    _Drr4xminorLowRFBAttenuation_Type()
)
drr4xminorLowRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorLowRFBAttenuation.setStatus("obsolete")
_Drr4xcurrentValueRFBAttenuation_Type = Float
_Drr4xcurrentValueRFBAttenuation_Object = MibTableColumn
drr4xcurrentValueRFBAttenuation = _Drr4xcurrentValueRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 19),
    _Drr4xcurrentValueRFBAttenuation_Type()
)
drr4xcurrentValueRFBAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drr4xcurrentValueRFBAttenuation.setStatus("mandatory")


class _Drr4xstateFlagRFBAttenuation_Type(Integer32):
    """Custom type drr4xstateFlagRFBAttenuation based on Integer32"""
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


_Drr4xstateFlagRFBAttenuation_Type.__name__ = "Integer32"
_Drr4xstateFlagRFBAttenuation_Object = MibTableColumn
drr4xstateFlagRFBAttenuation = _Drr4xstateFlagRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 20),
    _Drr4xstateFlagRFBAttenuation_Type()
)
drr4xstateFlagRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateFlagRFBAttenuation.setStatus("mandatory")
_Drr4xminValueRFBAttenuation_Type = Float
_Drr4xminValueRFBAttenuation_Object = MibTableColumn
drr4xminValueRFBAttenuation = _Drr4xminValueRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 21),
    _Drr4xminValueRFBAttenuation_Type()
)
drr4xminValueRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminValueRFBAttenuation.setStatus("mandatory")
_Drr4xmaxValueRFBAttenuation_Type = Float
_Drr4xmaxValueRFBAttenuation_Object = MibTableColumn
drr4xmaxValueRFBAttenuation = _Drr4xmaxValueRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 22),
    _Drr4xmaxValueRFBAttenuation_Type()
)
drr4xmaxValueRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmaxValueRFBAttenuation.setStatus("mandatory")


class _Drr4xalarmStateRFBAttenuation_Type(Integer32):
    """Custom type drr4xalarmStateRFBAttenuation based on Integer32"""
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


_Drr4xalarmStateRFBAttenuation_Type.__name__ = "Integer32"
_Drr4xalarmStateRFBAttenuation_Object = MibTableColumn
drr4xalarmStateRFBAttenuation = _Drr4xalarmStateRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 23),
    _Drr4xalarmStateRFBAttenuation_Type()
)
drr4xalarmStateRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xalarmStateRFBAttenuation.setStatus("mandatory")


class _Drr4xlabelRFCAttenuation_Type(DisplayString):
    """Custom type drr4xlabelRFCAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelRFCAttenuation_Type.__name__ = "DisplayString"
_Drr4xlabelRFCAttenuation_Object = MibTableColumn
drr4xlabelRFCAttenuation = _Drr4xlabelRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 24),
    _Drr4xlabelRFCAttenuation_Type()
)
drr4xlabelRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelRFCAttenuation.setStatus("optional")


class _Drr4xuomRFCAttenuation_Type(DisplayString):
    """Custom type drr4xuomRFCAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xuomRFCAttenuation_Type.__name__ = "DisplayString"
_Drr4xuomRFCAttenuation_Object = MibTableColumn
drr4xuomRFCAttenuation = _Drr4xuomRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 25),
    _Drr4xuomRFCAttenuation_Type()
)
drr4xuomRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xuomRFCAttenuation.setStatus("optional")
_Drr4xmajorHighRFCAttenuation_Type = Float
_Drr4xmajorHighRFCAttenuation_Object = MibTableColumn
drr4xmajorHighRFCAttenuation = _Drr4xmajorHighRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 26),
    _Drr4xmajorHighRFCAttenuation_Type()
)
drr4xmajorHighRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorHighRFCAttenuation.setStatus("obsolete")
_Drr4xmajorLowRFCAttenuation_Type = Float
_Drr4xmajorLowRFCAttenuation_Object = MibTableColumn
drr4xmajorLowRFCAttenuation = _Drr4xmajorLowRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 27),
    _Drr4xmajorLowRFCAttenuation_Type()
)
drr4xmajorLowRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorLowRFCAttenuation.setStatus("obsolete")
_Drr4xminorHighRFCAttenuation_Type = Float
_Drr4xminorHighRFCAttenuation_Object = MibTableColumn
drr4xminorHighRFCAttenuation = _Drr4xminorHighRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 28),
    _Drr4xminorHighRFCAttenuation_Type()
)
drr4xminorHighRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorHighRFCAttenuation.setStatus("obsolete")
_Drr4xminorLowRFCAttenuation_Type = Float
_Drr4xminorLowRFCAttenuation_Object = MibTableColumn
drr4xminorLowRFCAttenuation = _Drr4xminorLowRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 29),
    _Drr4xminorLowRFCAttenuation_Type()
)
drr4xminorLowRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorLowRFCAttenuation.setStatus("obsolete")
_Drr4xcurrentValueRFCAttenuation_Type = Float
_Drr4xcurrentValueRFCAttenuation_Object = MibTableColumn
drr4xcurrentValueRFCAttenuation = _Drr4xcurrentValueRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 30),
    _Drr4xcurrentValueRFCAttenuation_Type()
)
drr4xcurrentValueRFCAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drr4xcurrentValueRFCAttenuation.setStatus("mandatory")


class _Drr4xstateFlagRFCAttenuation_Type(Integer32):
    """Custom type drr4xstateFlagRFCAttenuation based on Integer32"""
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


_Drr4xstateFlagRFCAttenuation_Type.__name__ = "Integer32"
_Drr4xstateFlagRFCAttenuation_Object = MibTableColumn
drr4xstateFlagRFCAttenuation = _Drr4xstateFlagRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 31),
    _Drr4xstateFlagRFCAttenuation_Type()
)
drr4xstateFlagRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateFlagRFCAttenuation.setStatus("mandatory")
_Drr4xminValueRFCAttenuation_Type = Float
_Drr4xminValueRFCAttenuation_Object = MibTableColumn
drr4xminValueRFCAttenuation = _Drr4xminValueRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 32),
    _Drr4xminValueRFCAttenuation_Type()
)
drr4xminValueRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminValueRFCAttenuation.setStatus("mandatory")
_Drr4xmaxValueRFCAttenuation_Type = Float
_Drr4xmaxValueRFCAttenuation_Object = MibTableColumn
drr4xmaxValueRFCAttenuation = _Drr4xmaxValueRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 33),
    _Drr4xmaxValueRFCAttenuation_Type()
)
drr4xmaxValueRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmaxValueRFCAttenuation.setStatus("mandatory")


class _Drr4xalarmStateRFCAttenuation_Type(Integer32):
    """Custom type drr4xalarmStateRFCAttenuation based on Integer32"""
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


_Drr4xalarmStateRFCAttenuation_Type.__name__ = "Integer32"
_Drr4xalarmStateRFCAttenuation_Object = MibTableColumn
drr4xalarmStateRFCAttenuation = _Drr4xalarmStateRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 34),
    _Drr4xalarmStateRFCAttenuation_Type()
)
drr4xalarmStateRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xalarmStateRFCAttenuation.setStatus("mandatory")


class _Drr4xlabelRFDAttenuation_Type(DisplayString):
    """Custom type drr4xlabelRFDAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelRFDAttenuation_Type.__name__ = "DisplayString"
_Drr4xlabelRFDAttenuation_Object = MibTableColumn
drr4xlabelRFDAttenuation = _Drr4xlabelRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 35),
    _Drr4xlabelRFDAttenuation_Type()
)
drr4xlabelRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelRFDAttenuation.setStatus("optional")


class _Drr4xuomRFDAttenuation_Type(DisplayString):
    """Custom type drr4xuomRFDAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xuomRFDAttenuation_Type.__name__ = "DisplayString"
_Drr4xuomRFDAttenuation_Object = MibTableColumn
drr4xuomRFDAttenuation = _Drr4xuomRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 36),
    _Drr4xuomRFDAttenuation_Type()
)
drr4xuomRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xuomRFDAttenuation.setStatus("optional")
_Drr4xmajorHighRFDAttenuation_Type = Float
_Drr4xmajorHighRFDAttenuation_Object = MibTableColumn
drr4xmajorHighRFDAttenuation = _Drr4xmajorHighRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 37),
    _Drr4xmajorHighRFDAttenuation_Type()
)
drr4xmajorHighRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorHighRFDAttenuation.setStatus("obsolete")
_Drr4xmajorLowRFDAttenuation_Type = Float
_Drr4xmajorLowRFDAttenuation_Object = MibTableColumn
drr4xmajorLowRFDAttenuation = _Drr4xmajorLowRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 38),
    _Drr4xmajorLowRFDAttenuation_Type()
)
drr4xmajorLowRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorLowRFDAttenuation.setStatus("obsolete")
_Drr4xminorHighRFDAttenuation_Type = Float
_Drr4xminorHighRFDAttenuation_Object = MibTableColumn
drr4xminorHighRFDAttenuation = _Drr4xminorHighRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 39),
    _Drr4xminorHighRFDAttenuation_Type()
)
drr4xminorHighRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorHighRFDAttenuation.setStatus("obsolete")
_Drr4xminorLowRFDAttenuation_Type = Float
_Drr4xminorLowRFDAttenuation_Object = MibTableColumn
drr4xminorLowRFDAttenuation = _Drr4xminorLowRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 40),
    _Drr4xminorLowRFDAttenuation_Type()
)
drr4xminorLowRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorLowRFDAttenuation.setStatus("obsolete")
_Drr4xcurrentValueRFDAttenuation_Type = Float
_Drr4xcurrentValueRFDAttenuation_Object = MibTableColumn
drr4xcurrentValueRFDAttenuation = _Drr4xcurrentValueRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 41),
    _Drr4xcurrentValueRFDAttenuation_Type()
)
drr4xcurrentValueRFDAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drr4xcurrentValueRFDAttenuation.setStatus("mandatory")


class _Drr4xstateFlagRFDAttenuation_Type(Integer32):
    """Custom type drr4xstateFlagRFDAttenuation based on Integer32"""
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


_Drr4xstateFlagRFDAttenuation_Type.__name__ = "Integer32"
_Drr4xstateFlagRFDAttenuation_Object = MibTableColumn
drr4xstateFlagRFDAttenuation = _Drr4xstateFlagRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 42),
    _Drr4xstateFlagRFDAttenuation_Type()
)
drr4xstateFlagRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateFlagRFDAttenuation.setStatus("mandatory")
_Drr4xminValueRFDAttenuation_Type = Float
_Drr4xminValueRFDAttenuation_Object = MibTableColumn
drr4xminValueRFDAttenuation = _Drr4xminValueRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 43),
    _Drr4xminValueRFDAttenuation_Type()
)
drr4xminValueRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminValueRFDAttenuation.setStatus("mandatory")
_Drr4xmaxValueRFDAttenuation_Type = Float
_Drr4xmaxValueRFDAttenuation_Object = MibTableColumn
drr4xmaxValueRFDAttenuation = _Drr4xmaxValueRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 44),
    _Drr4xmaxValueRFDAttenuation_Type()
)
drr4xmaxValueRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmaxValueRFDAttenuation.setStatus("mandatory")


class _Drr4xalarmStateRFDAttenuation_Type(Integer32):
    """Custom type drr4xalarmStateRFDAttenuation based on Integer32"""
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


_Drr4xalarmStateRFDAttenuation_Type.__name__ = "Integer32"
_Drr4xalarmStateRFDAttenuation_Object = MibTableColumn
drr4xalarmStateRFDAttenuation = _Drr4xalarmStateRFDAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 45),
    _Drr4xalarmStateRFDAttenuation_Type()
)
drr4xalarmStateRFDAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xalarmStateRFDAttenuation.setStatus("mandatory")


class _Drr4xlabelTrippointLevel_Type(DisplayString):
    """Custom type drr4xlabelTrippointLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelTrippointLevel_Type.__name__ = "DisplayString"
_Drr4xlabelTrippointLevel_Object = MibTableColumn
drr4xlabelTrippointLevel = _Drr4xlabelTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 46),
    _Drr4xlabelTrippointLevel_Type()
)
drr4xlabelTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelTrippointLevel.setStatus("optional")


class _Drr4xuomTrippointLevel_Type(DisplayString):
    """Custom type drr4xuomTrippointLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xuomTrippointLevel_Type.__name__ = "DisplayString"
_Drr4xuomTrippointLevel_Object = MibTableColumn
drr4xuomTrippointLevel = _Drr4xuomTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 47),
    _Drr4xuomTrippointLevel_Type()
)
drr4xuomTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xuomTrippointLevel.setStatus("optional")
_Drr4xmajorHighTrippointLevel_Type = Float
_Drr4xmajorHighTrippointLevel_Object = MibTableColumn
drr4xmajorHighTrippointLevel = _Drr4xmajorHighTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 48),
    _Drr4xmajorHighTrippointLevel_Type()
)
drr4xmajorHighTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorHighTrippointLevel.setStatus("obsolete")
_Drr4xmajorLowTrippointLevel_Type = Float
_Drr4xmajorLowTrippointLevel_Object = MibTableColumn
drr4xmajorLowTrippointLevel = _Drr4xmajorLowTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 49),
    _Drr4xmajorLowTrippointLevel_Type()
)
drr4xmajorLowTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorLowTrippointLevel.setStatus("obsolete")
_Drr4xminorHighTrippointLevel_Type = Float
_Drr4xminorHighTrippointLevel_Object = MibTableColumn
drr4xminorHighTrippointLevel = _Drr4xminorHighTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 50),
    _Drr4xminorHighTrippointLevel_Type()
)
drr4xminorHighTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorHighTrippointLevel.setStatus("obsolete")
_Drr4xminorLowTrippointLevel_Type = Float
_Drr4xminorLowTrippointLevel_Object = MibTableColumn
drr4xminorLowTrippointLevel = _Drr4xminorLowTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 51),
    _Drr4xminorLowTrippointLevel_Type()
)
drr4xminorLowTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorLowTrippointLevel.setStatus("obsolete")
_Drr4xcurrentValueTrippointLevel_Type = Float
_Drr4xcurrentValueTrippointLevel_Object = MibTableColumn
drr4xcurrentValueTrippointLevel = _Drr4xcurrentValueTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 52),
    _Drr4xcurrentValueTrippointLevel_Type()
)
drr4xcurrentValueTrippointLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drr4xcurrentValueTrippointLevel.setStatus("mandatory")


class _Drr4xstateFlagTrippointLevel_Type(Integer32):
    """Custom type drr4xstateFlagTrippointLevel based on Integer32"""
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


_Drr4xstateFlagTrippointLevel_Type.__name__ = "Integer32"
_Drr4xstateFlagTrippointLevel_Object = MibTableColumn
drr4xstateFlagTrippointLevel = _Drr4xstateFlagTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 53),
    _Drr4xstateFlagTrippointLevel_Type()
)
drr4xstateFlagTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateFlagTrippointLevel.setStatus("mandatory")
_Drr4xminValueTrippointLevel_Type = Float
_Drr4xminValueTrippointLevel_Object = MibTableColumn
drr4xminValueTrippointLevel = _Drr4xminValueTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 54),
    _Drr4xminValueTrippointLevel_Type()
)
drr4xminValueTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminValueTrippointLevel.setStatus("mandatory")
_Drr4xmaxValueTrippointLevel_Type = Float
_Drr4xmaxValueTrippointLevel_Object = MibTableColumn
drr4xmaxValueTrippointLevel = _Drr4xmaxValueTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 55),
    _Drr4xmaxValueTrippointLevel_Type()
)
drr4xmaxValueTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmaxValueTrippointLevel.setStatus("mandatory")


class _Drr4xalarmStateTrippointLevel_Type(Integer32):
    """Custom type drr4xalarmStateTrippointLevel based on Integer32"""
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


_Drr4xalarmStateTrippointLevel_Type.__name__ = "Integer32"
_Drr4xalarmStateTrippointLevel_Object = MibTableColumn
drr4xalarmStateTrippointLevel = _Drr4xalarmStateTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 56),
    _Drr4xalarmStateTrippointLevel_Type()
)
drr4xalarmStateTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xalarmStateTrippointLevel.setStatus("mandatory")


class _Drr4xlabelOptCurrent_Type(DisplayString):
    """Custom type drr4xlabelOptCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelOptCurrent_Type.__name__ = "DisplayString"
_Drr4xlabelOptCurrent_Object = MibTableColumn
drr4xlabelOptCurrent = _Drr4xlabelOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 57),
    _Drr4xlabelOptCurrent_Type()
)
drr4xlabelOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelOptCurrent.setStatus("optional")


class _Drr4xuomOptCurrent_Type(DisplayString):
    """Custom type drr4xuomOptCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xuomOptCurrent_Type.__name__ = "DisplayString"
_Drr4xuomOptCurrent_Object = MibTableColumn
drr4xuomOptCurrent = _Drr4xuomOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 58),
    _Drr4xuomOptCurrent_Type()
)
drr4xuomOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xuomOptCurrent.setStatus("optional")
_Drr4xmajorHighOptCurrent_Type = Float
_Drr4xmajorHighOptCurrent_Object = MibTableColumn
drr4xmajorHighOptCurrent = _Drr4xmajorHighOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 59),
    _Drr4xmajorHighOptCurrent_Type()
)
drr4xmajorHighOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorHighOptCurrent.setStatus("mandatory")
_Drr4xmajorLowOptCurrent_Type = Float
_Drr4xmajorLowOptCurrent_Object = MibTableColumn
drr4xmajorLowOptCurrent = _Drr4xmajorLowOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 60),
    _Drr4xmajorLowOptCurrent_Type()
)
drr4xmajorLowOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorLowOptCurrent.setStatus("mandatory")
_Drr4xminorHighOptCurrent_Type = Float
_Drr4xminorHighOptCurrent_Object = MibTableColumn
drr4xminorHighOptCurrent = _Drr4xminorHighOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 61),
    _Drr4xminorHighOptCurrent_Type()
)
drr4xminorHighOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorHighOptCurrent.setStatus("obsolete")
_Drr4xminorLowOptCurrent_Type = Float
_Drr4xminorLowOptCurrent_Object = MibTableColumn
drr4xminorLowOptCurrent = _Drr4xminorLowOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 62),
    _Drr4xminorLowOptCurrent_Type()
)
drr4xminorLowOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorLowOptCurrent.setStatus("obsolete")
_Drr4xcurrentValueOptCurrent_Type = Float
_Drr4xcurrentValueOptCurrent_Object = MibTableColumn
drr4xcurrentValueOptCurrent = _Drr4xcurrentValueOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 63),
    _Drr4xcurrentValueOptCurrent_Type()
)
drr4xcurrentValueOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xcurrentValueOptCurrent.setStatus("mandatory")


class _Drr4xstateFlagOptCurrent_Type(Integer32):
    """Custom type drr4xstateFlagOptCurrent based on Integer32"""
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


_Drr4xstateFlagOptCurrent_Type.__name__ = "Integer32"
_Drr4xstateFlagOptCurrent_Object = MibTableColumn
drr4xstateFlagOptCurrent = _Drr4xstateFlagOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 64),
    _Drr4xstateFlagOptCurrent_Type()
)
drr4xstateFlagOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateFlagOptCurrent.setStatus("mandatory")
_Drr4xminValueOptCurrent_Type = Float
_Drr4xminValueOptCurrent_Object = MibTableColumn
drr4xminValueOptCurrent = _Drr4xminValueOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 65),
    _Drr4xminValueOptCurrent_Type()
)
drr4xminValueOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminValueOptCurrent.setStatus("mandatory")
_Drr4xmaxValueOptCurrent_Type = Float
_Drr4xmaxValueOptCurrent_Object = MibTableColumn
drr4xmaxValueOptCurrent = _Drr4xmaxValueOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 66),
    _Drr4xmaxValueOptCurrent_Type()
)
drr4xmaxValueOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmaxValueOptCurrent.setStatus("mandatory")


class _Drr4xalarmStateOptCurrent_Type(Integer32):
    """Custom type drr4xalarmStateOptCurrent based on Integer32"""
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


_Drr4xalarmStateOptCurrent_Type.__name__ = "Integer32"
_Drr4xalarmStateOptCurrent_Object = MibTableColumn
drr4xalarmStateOptCurrent = _Drr4xalarmStateOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 67),
    _Drr4xalarmStateOptCurrent_Type()
)
drr4xalarmStateOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xalarmStateOptCurrent.setStatus("mandatory")


class _Drr4xlabel12VCurrent_Type(DisplayString):
    """Custom type drr4xlabel12VCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabel12VCurrent_Type.__name__ = "DisplayString"
_Drr4xlabel12VCurrent_Object = MibTableColumn
drr4xlabel12VCurrent = _Drr4xlabel12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 68),
    _Drr4xlabel12VCurrent_Type()
)
drr4xlabel12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabel12VCurrent.setStatus("optional")


class _Drr4xuom12VCurrent_Type(DisplayString):
    """Custom type drr4xuom12VCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xuom12VCurrent_Type.__name__ = "DisplayString"
_Drr4xuom12VCurrent_Object = MibTableColumn
drr4xuom12VCurrent = _Drr4xuom12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 69),
    _Drr4xuom12VCurrent_Type()
)
drr4xuom12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xuom12VCurrent.setStatus("optional")
_Drr4xmajorHigh12VCurrent_Type = Float
_Drr4xmajorHigh12VCurrent_Object = MibTableColumn
drr4xmajorHigh12VCurrent = _Drr4xmajorHigh12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 70),
    _Drr4xmajorHigh12VCurrent_Type()
)
drr4xmajorHigh12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorHigh12VCurrent.setStatus("mandatory")
_Drr4xmajorLow12VCurrent_Type = Float
_Drr4xmajorLow12VCurrent_Object = MibTableColumn
drr4xmajorLow12VCurrent = _Drr4xmajorLow12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 71),
    _Drr4xmajorLow12VCurrent_Type()
)
drr4xmajorLow12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorLow12VCurrent.setStatus("mandatory")
_Drr4xminorHigh12VCurrent_Type = Float
_Drr4xminorHigh12VCurrent_Object = MibTableColumn
drr4xminorHigh12VCurrent = _Drr4xminorHigh12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 72),
    _Drr4xminorHigh12VCurrent_Type()
)
drr4xminorHigh12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorHigh12VCurrent.setStatus("mandatory")
_Drr4xminorLow12VCurrent_Type = Float
_Drr4xminorLow12VCurrent_Object = MibTableColumn
drr4xminorLow12VCurrent = _Drr4xminorLow12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 73),
    _Drr4xminorLow12VCurrent_Type()
)
drr4xminorLow12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorLow12VCurrent.setStatus("mandatory")
_Drr4xcurrentValue12VCurrent_Type = Float
_Drr4xcurrentValue12VCurrent_Object = MibTableColumn
drr4xcurrentValue12VCurrent = _Drr4xcurrentValue12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 74),
    _Drr4xcurrentValue12VCurrent_Type()
)
drr4xcurrentValue12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xcurrentValue12VCurrent.setStatus("mandatory")


class _Drr4xstateFlag12VCurrent_Type(Integer32):
    """Custom type drr4xstateFlag12VCurrent based on Integer32"""
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


_Drr4xstateFlag12VCurrent_Type.__name__ = "Integer32"
_Drr4xstateFlag12VCurrent_Object = MibTableColumn
drr4xstateFlag12VCurrent = _Drr4xstateFlag12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 75),
    _Drr4xstateFlag12VCurrent_Type()
)
drr4xstateFlag12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateFlag12VCurrent.setStatus("mandatory")
_Drr4xminValue12VCurrent_Type = Float
_Drr4xminValue12VCurrent_Object = MibTableColumn
drr4xminValue12VCurrent = _Drr4xminValue12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 76),
    _Drr4xminValue12VCurrent_Type()
)
drr4xminValue12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminValue12VCurrent.setStatus("mandatory")
_Drr4xmaxValue12VCurrent_Type = Float
_Drr4xmaxValue12VCurrent_Object = MibTableColumn
drr4xmaxValue12VCurrent = _Drr4xmaxValue12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 77),
    _Drr4xmaxValue12VCurrent_Type()
)
drr4xmaxValue12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmaxValue12VCurrent.setStatus("mandatory")


class _Drr4xalarmState12VCurrent_Type(Integer32):
    """Custom type drr4xalarmState12VCurrent based on Integer32"""
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


_Drr4xalarmState12VCurrent_Type.__name__ = "Integer32"
_Drr4xalarmState12VCurrent_Object = MibTableColumn
drr4xalarmState12VCurrent = _Drr4xalarmState12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 78),
    _Drr4xalarmState12VCurrent_Type()
)
drr4xalarmState12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xalarmState12VCurrent.setStatus("mandatory")


class _Drr4xlabelModTemp_Type(DisplayString):
    """Custom type drr4xlabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelModTemp_Type.__name__ = "DisplayString"
_Drr4xlabelModTemp_Object = MibTableColumn
drr4xlabelModTemp = _Drr4xlabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 79),
    _Drr4xlabelModTemp_Type()
)
drr4xlabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelModTemp.setStatus("optional")


class _Drr4xuomModTemp_Type(DisplayString):
    """Custom type drr4xuomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xuomModTemp_Type.__name__ = "DisplayString"
_Drr4xuomModTemp_Object = MibTableColumn
drr4xuomModTemp = _Drr4xuomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 80),
    _Drr4xuomModTemp_Type()
)
drr4xuomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xuomModTemp.setStatus("optional")
_Drr4xmajorHighModTemp_Type = Float
_Drr4xmajorHighModTemp_Object = MibTableColumn
drr4xmajorHighModTemp = _Drr4xmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 81),
    _Drr4xmajorHighModTemp_Type()
)
drr4xmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorHighModTemp.setStatus("mandatory")
_Drr4xmajorLowModTemp_Type = Float
_Drr4xmajorLowModTemp_Object = MibTableColumn
drr4xmajorLowModTemp = _Drr4xmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 82),
    _Drr4xmajorLowModTemp_Type()
)
drr4xmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorLowModTemp.setStatus("mandatory")
_Drr4xminorHighModTemp_Type = Float
_Drr4xminorHighModTemp_Object = MibTableColumn
drr4xminorHighModTemp = _Drr4xminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 83),
    _Drr4xminorHighModTemp_Type()
)
drr4xminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorHighModTemp.setStatus("mandatory")
_Drr4xminorLowModTemp_Type = Float
_Drr4xminorLowModTemp_Object = MibTableColumn
drr4xminorLowModTemp = _Drr4xminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 84),
    _Drr4xminorLowModTemp_Type()
)
drr4xminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorLowModTemp.setStatus("mandatory")
_Drr4xcurrentValueModTemp_Type = Float
_Drr4xcurrentValueModTemp_Object = MibTableColumn
drr4xcurrentValueModTemp = _Drr4xcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 85),
    _Drr4xcurrentValueModTemp_Type()
)
drr4xcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xcurrentValueModTemp.setStatus("mandatory")


class _Drr4xstateFlagModTemp_Type(Integer32):
    """Custom type drr4xstateFlagModTemp based on Integer32"""
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


_Drr4xstateFlagModTemp_Type.__name__ = "Integer32"
_Drr4xstateFlagModTemp_Object = MibTableColumn
drr4xstateFlagModTemp = _Drr4xstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 86),
    _Drr4xstateFlagModTemp_Type()
)
drr4xstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateFlagModTemp.setStatus("mandatory")
_Drr4xminValueModTemp_Type = Float
_Drr4xminValueModTemp_Object = MibTableColumn
drr4xminValueModTemp = _Drr4xminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 87),
    _Drr4xminValueModTemp_Type()
)
drr4xminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminValueModTemp.setStatus("mandatory")
_Drr4xmaxValueModTemp_Type = Float
_Drr4xmaxValueModTemp_Object = MibTableColumn
drr4xmaxValueModTemp = _Drr4xmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 88),
    _Drr4xmaxValueModTemp_Type()
)
drr4xmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmaxValueModTemp.setStatus("mandatory")


class _Drr4xalarmStateModTemp_Type(Integer32):
    """Custom type drr4xalarmStateModTemp based on Integer32"""
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


_Drr4xalarmStateModTemp_Type.__name__ = "Integer32"
_Drr4xalarmStateModTemp_Object = MibTableColumn
drr4xalarmStateModTemp = _Drr4xalarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 89),
    _Drr4xalarmStateModTemp_Type()
)
drr4xalarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xalarmStateModTemp.setStatus("mandatory")


class _Drr4xlabelFanCurrent_Type(DisplayString):
    """Custom type drr4xlabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelFanCurrent_Type.__name__ = "DisplayString"
_Drr4xlabelFanCurrent_Object = MibTableColumn
drr4xlabelFanCurrent = _Drr4xlabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 90),
    _Drr4xlabelFanCurrent_Type()
)
drr4xlabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelFanCurrent.setStatus("optional")


class _Drr4xuomFanCurrent_Type(DisplayString):
    """Custom type drr4xuomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xuomFanCurrent_Type.__name__ = "DisplayString"
_Drr4xuomFanCurrent_Object = MibTableColumn
drr4xuomFanCurrent = _Drr4xuomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 91),
    _Drr4xuomFanCurrent_Type()
)
drr4xuomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xuomFanCurrent.setStatus("optional")
_Drr4xmajorHighFanCurrent_Type = Float
_Drr4xmajorHighFanCurrent_Object = MibTableColumn
drr4xmajorHighFanCurrent = _Drr4xmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 92),
    _Drr4xmajorHighFanCurrent_Type()
)
drr4xmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorHighFanCurrent.setStatus("mandatory")
_Drr4xmajorLowFanCurrent_Type = Float
_Drr4xmajorLowFanCurrent_Object = MibTableColumn
drr4xmajorLowFanCurrent = _Drr4xmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 93),
    _Drr4xmajorLowFanCurrent_Type()
)
drr4xmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmajorLowFanCurrent.setStatus("mandatory")
_Drr4xminorHighFanCurrent_Type = Float
_Drr4xminorHighFanCurrent_Object = MibTableColumn
drr4xminorHighFanCurrent = _Drr4xminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 94),
    _Drr4xminorHighFanCurrent_Type()
)
drr4xminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorHighFanCurrent.setStatus("obsolete")
_Drr4xminorLowFanCurrent_Type = Float
_Drr4xminorLowFanCurrent_Object = MibTableColumn
drr4xminorLowFanCurrent = _Drr4xminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 95),
    _Drr4xminorLowFanCurrent_Type()
)
drr4xminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminorLowFanCurrent.setStatus("obsolete")
_Drr4xcurrentValueFanCurrent_Type = Float
_Drr4xcurrentValueFanCurrent_Object = MibTableColumn
drr4xcurrentValueFanCurrent = _Drr4xcurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 96),
    _Drr4xcurrentValueFanCurrent_Type()
)
drr4xcurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xcurrentValueFanCurrent.setStatus("mandatory")


class _Drr4xstateFlagFanCurrent_Type(Integer32):
    """Custom type drr4xstateFlagFanCurrent based on Integer32"""
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


_Drr4xstateFlagFanCurrent_Type.__name__ = "Integer32"
_Drr4xstateFlagFanCurrent_Object = MibTableColumn
drr4xstateFlagFanCurrent = _Drr4xstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 97),
    _Drr4xstateFlagFanCurrent_Type()
)
drr4xstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateFlagFanCurrent.setStatus("mandatory")
_Drr4xminValueFanCurrent_Type = Float
_Drr4xminValueFanCurrent_Object = MibTableColumn
drr4xminValueFanCurrent = _Drr4xminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 98),
    _Drr4xminValueFanCurrent_Type()
)
drr4xminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xminValueFanCurrent.setStatus("mandatory")
_Drr4xmaxValueFanCurrent_Type = Float
_Drr4xmaxValueFanCurrent_Object = MibTableColumn
drr4xmaxValueFanCurrent = _Drr4xmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 99),
    _Drr4xmaxValueFanCurrent_Type()
)
drr4xmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xmaxValueFanCurrent.setStatus("mandatory")


class _Drr4xalarmStateFanCurrent_Type(Integer32):
    """Custom type drr4xalarmStateFanCurrent based on Integer32"""
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


_Drr4xalarmStateFanCurrent_Type.__name__ = "Integer32"
_Drr4xalarmStateFanCurrent_Object = MibTableColumn
drr4xalarmStateFanCurrent = _Drr4xalarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 2, 1, 100),
    _Drr4xalarmStateFanCurrent_Type()
)
drr4xalarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xalarmStateFanCurrent.setStatus("mandatory")
_Gx2drr4xDigitalTable_Object = MibTable
gx2drr4xDigitalTable = _Gx2drr4xDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3)
)
if mibBuilder.loadTexts:
    gx2drr4xDigitalTable.setStatus("mandatory")
_Gx2drr4xDigitalEntry_Object = MibTableRow
gx2drr4xDigitalEntry = _Gx2drr4xDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2)
)
gx2drr4xDigitalEntry.setIndexNames(
    (0, "OMNI-gx2drr4x-MIB", "gx2drr4xDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2drr4xDigitalEntry.setStatus("mandatory")


class _Gx2drr4xDigitalTableIndex_Type(Integer32):
    """Custom type gx2drr4xDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2drr4xDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2drr4xDigitalTableIndex_Object = MibTableColumn
gx2drr4xDigitalTableIndex = _Gx2drr4xDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2, 1),
    _Gx2drr4xDigitalTableIndex_Type()
)
gx2drr4xDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2drr4xDigitalTableIndex.setStatus("mandatory")


class _Drr4xlabelTrippointMode_Type(DisplayString):
    """Custom type drr4xlabelTrippointMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelTrippointMode_Type.__name__ = "DisplayString"
_Drr4xlabelTrippointMode_Object = MibTableColumn
drr4xlabelTrippointMode = _Drr4xlabelTrippointMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2, 2),
    _Drr4xlabelTrippointMode_Type()
)
drr4xlabelTrippointMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelTrippointMode.setStatus("optional")


class _Drr4xenumTrippointMode_Type(DisplayString):
    """Custom type drr4xenumTrippointMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xenumTrippointMode_Type.__name__ = "DisplayString"
_Drr4xenumTrippointMode_Object = MibTableColumn
drr4xenumTrippointMode = _Drr4xenumTrippointMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2, 3),
    _Drr4xenumTrippointMode_Type()
)
drr4xenumTrippointMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xenumTrippointMode.setStatus("optional")


class _Drr4xvalueTrippointMode_Type(Integer32):
    """Custom type drr4xvalueTrippointMode based on Integer32"""
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


_Drr4xvalueTrippointMode_Type.__name__ = "Integer32"
_Drr4xvalueTrippointMode_Object = MibTableColumn
drr4xvalueTrippointMode = _Drr4xvalueTrippointMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2, 4),
    _Drr4xvalueTrippointMode_Type()
)
drr4xvalueTrippointMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drr4xvalueTrippointMode.setStatus("mandatory")


class _Drr4xstateflagTrippointMode_Type(Integer32):
    """Custom type drr4xstateflagTrippointMode based on Integer32"""
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


_Drr4xstateflagTrippointMode_Type.__name__ = "Integer32"
_Drr4xstateflagTrippointMode_Object = MibTableColumn
drr4xstateflagTrippointMode = _Drr4xstateflagTrippointMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2, 5),
    _Drr4xstateflagTrippointMode_Type()
)
drr4xstateflagTrippointMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagTrippointMode.setStatus("mandatory")


class _Drr4xlabelFactoryDefaultReset_Type(DisplayString):
    """Custom type drr4xlabelFactoryDefaultReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelFactoryDefaultReset_Type.__name__ = "DisplayString"
_Drr4xlabelFactoryDefaultReset_Object = MibTableColumn
drr4xlabelFactoryDefaultReset = _Drr4xlabelFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2, 6),
    _Drr4xlabelFactoryDefaultReset_Type()
)
drr4xlabelFactoryDefaultReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelFactoryDefaultReset.setStatus("optional")


class _Drr4xenumFactoryDefaultReset_Type(DisplayString):
    """Custom type drr4xenumFactoryDefaultReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xenumFactoryDefaultReset_Type.__name__ = "DisplayString"
_Drr4xenumFactoryDefaultReset_Object = MibTableColumn
drr4xenumFactoryDefaultReset = _Drr4xenumFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2, 7),
    _Drr4xenumFactoryDefaultReset_Type()
)
drr4xenumFactoryDefaultReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xenumFactoryDefaultReset.setStatus("optional")


class _Drr4xvalueFactoryDefaultReset_Type(Integer32):
    """Custom type drr4xvalueFactoryDefaultReset based on Integer32"""
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


_Drr4xvalueFactoryDefaultReset_Type.__name__ = "Integer32"
_Drr4xvalueFactoryDefaultReset_Object = MibTableColumn
drr4xvalueFactoryDefaultReset = _Drr4xvalueFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2, 8),
    _Drr4xvalueFactoryDefaultReset_Type()
)
drr4xvalueFactoryDefaultReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drr4xvalueFactoryDefaultReset.setStatus("mandatory")


class _Drr4xstateflagFactoryDefaultReset_Type(Integer32):
    """Custom type drr4xstateflagFactoryDefaultReset based on Integer32"""
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


_Drr4xstateflagFactoryDefaultReset_Type.__name__ = "Integer32"
_Drr4xstateflagFactoryDefaultReset_Object = MibTableColumn
drr4xstateflagFactoryDefaultReset = _Drr4xstateflagFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 3, 2, 9),
    _Drr4xstateflagFactoryDefaultReset_Type()
)
drr4xstateflagFactoryDefaultReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagFactoryDefaultReset.setStatus("mandatory")
_Gx2drr4xStatusTable_Object = MibTable
gx2drr4xStatusTable = _Gx2drr4xStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4)
)
if mibBuilder.loadTexts:
    gx2drr4xStatusTable.setStatus("mandatory")
_Gx2drr4xStatusEntry_Object = MibTableRow
gx2drr4xStatusEntry = _Gx2drr4xStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3)
)
gx2drr4xStatusEntry.setIndexNames(
    (0, "OMNI-gx2drr4x-MIB", "gx2drr4xStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2drr4xStatusEntry.setStatus("mandatory")


class _Gx2drr4xStatusTableIndex_Type(Integer32):
    """Custom type gx2drr4xStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2drr4xStatusTableIndex_Type.__name__ = "Integer32"
_Gx2drr4xStatusTableIndex_Object = MibTableColumn
gx2drr4xStatusTableIndex = _Gx2drr4xStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 1),
    _Gx2drr4xStatusTableIndex_Type()
)
gx2drr4xStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2drr4xStatusTableIndex.setStatus("mandatory")


class _Drr4xlabelBoot_Type(DisplayString):
    """Custom type drr4xlabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelBoot_Type.__name__ = "DisplayString"
_Drr4xlabelBoot_Object = MibTableColumn
drr4xlabelBoot = _Drr4xlabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 2),
    _Drr4xlabelBoot_Type()
)
drr4xlabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelBoot.setStatus("optional")


class _Drr4xvalueBoot_Type(Integer32):
    """Custom type drr4xvalueBoot based on Integer32"""
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


_Drr4xvalueBoot_Type.__name__ = "Integer32"
_Drr4xvalueBoot_Object = MibTableColumn
drr4xvalueBoot = _Drr4xvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 3),
    _Drr4xvalueBoot_Type()
)
drr4xvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xvalueBoot.setStatus("mandatory")


class _Drr4xstateflagBoot_Type(Integer32):
    """Custom type drr4xstateflagBoot based on Integer32"""
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


_Drr4xstateflagBoot_Type.__name__ = "Integer32"
_Drr4xstateflagBoot_Object = MibTableColumn
drr4xstateflagBoot = _Drr4xstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 4),
    _Drr4xstateflagBoot_Type()
)
drr4xstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagBoot.setStatus("mandatory")


class _Drr4xlabelFlash_Type(DisplayString):
    """Custom type drr4xlabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelFlash_Type.__name__ = "DisplayString"
_Drr4xlabelFlash_Object = MibTableColumn
drr4xlabelFlash = _Drr4xlabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 5),
    _Drr4xlabelFlash_Type()
)
drr4xlabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelFlash.setStatus("optional")


class _Drr4xvalueFlash_Type(Integer32):
    """Custom type drr4xvalueFlash based on Integer32"""
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


_Drr4xvalueFlash_Type.__name__ = "Integer32"
_Drr4xvalueFlash_Object = MibTableColumn
drr4xvalueFlash = _Drr4xvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 6),
    _Drr4xvalueFlash_Type()
)
drr4xvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xvalueFlash.setStatus("mandatory")


class _Drr4xstateflagFlash_Type(Integer32):
    """Custom type drr4xstateflagFlash based on Integer32"""
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


_Drr4xstateflagFlash_Type.__name__ = "Integer32"
_Drr4xstateflagFlash_Object = MibTableColumn
drr4xstateflagFlash = _Drr4xstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 7),
    _Drr4xstateflagFlash_Type()
)
drr4xstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagFlash.setStatus("mandatory")


class _Drr4xlabelFactoryDataCRC_Type(DisplayString):
    """Custom type drr4xlabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelFactoryDataCRC_Type.__name__ = "DisplayString"
_Drr4xlabelFactoryDataCRC_Object = MibTableColumn
drr4xlabelFactoryDataCRC = _Drr4xlabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 8),
    _Drr4xlabelFactoryDataCRC_Type()
)
drr4xlabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelFactoryDataCRC.setStatus("optional")


class _Drr4xvalueFactoryDataCRC_Type(Integer32):
    """Custom type drr4xvalueFactoryDataCRC based on Integer32"""
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


_Drr4xvalueFactoryDataCRC_Type.__name__ = "Integer32"
_Drr4xvalueFactoryDataCRC_Object = MibTableColumn
drr4xvalueFactoryDataCRC = _Drr4xvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 9),
    _Drr4xvalueFactoryDataCRC_Type()
)
drr4xvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xvalueFactoryDataCRC.setStatus("mandatory")


class _Drr4xstateflagFactoryDataCRC_Type(Integer32):
    """Custom type drr4xstateflagFactoryDataCRC based on Integer32"""
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


_Drr4xstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Drr4xstateflagFactoryDataCRC_Object = MibTableColumn
drr4xstateflagFactoryDataCRC = _Drr4xstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 10),
    _Drr4xstateflagFactoryDataCRC_Type()
)
drr4xstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagFactoryDataCRC.setStatus("mandatory")


class _Drr4xlabelAlarmDataCrc_Type(DisplayString):
    """Custom type drr4xlabelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelAlarmDataCrc_Type.__name__ = "DisplayString"
_Drr4xlabelAlarmDataCrc_Object = MibTableColumn
drr4xlabelAlarmDataCrc = _Drr4xlabelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 11),
    _Drr4xlabelAlarmDataCrc_Type()
)
drr4xlabelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelAlarmDataCrc.setStatus("optional")


class _Drr4xvalueAlarmDataCrc_Type(Integer32):
    """Custom type drr4xvalueAlarmDataCrc based on Integer32"""
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


_Drr4xvalueAlarmDataCrc_Type.__name__ = "Integer32"
_Drr4xvalueAlarmDataCrc_Object = MibTableColumn
drr4xvalueAlarmDataCrc = _Drr4xvalueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 12),
    _Drr4xvalueAlarmDataCrc_Type()
)
drr4xvalueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xvalueAlarmDataCrc.setStatus("mandatory")


class _Drr4xstateflagAlarmDataCrc_Type(Integer32):
    """Custom type drr4xstateflagAlarmDataCrc based on Integer32"""
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


_Drr4xstateflagAlarmDataCrc_Type.__name__ = "Integer32"
_Drr4xstateflagAlarmDataCrc_Object = MibTableColumn
drr4xstateflagAlarmDataCrc = _Drr4xstateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 13),
    _Drr4xstateflagAlarmDataCrc_Type()
)
drr4xstateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagAlarmDataCrc.setStatus("mandatory")


class _Drr4xlabelCalibrationDataCrc_Type(DisplayString):
    """Custom type drr4xlabelCalibrationDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelCalibrationDataCrc_Type.__name__ = "DisplayString"
_Drr4xlabelCalibrationDataCrc_Object = MibTableColumn
drr4xlabelCalibrationDataCrc = _Drr4xlabelCalibrationDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 14),
    _Drr4xlabelCalibrationDataCrc_Type()
)
drr4xlabelCalibrationDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelCalibrationDataCrc.setStatus("optional")


class _Drr4xvalueCalibrationDataCrc_Type(Integer32):
    """Custom type drr4xvalueCalibrationDataCrc based on Integer32"""
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


_Drr4xvalueCalibrationDataCrc_Type.__name__ = "Integer32"
_Drr4xvalueCalibrationDataCrc_Object = MibTableColumn
drr4xvalueCalibrationDataCrc = _Drr4xvalueCalibrationDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 15),
    _Drr4xvalueCalibrationDataCrc_Type()
)
drr4xvalueCalibrationDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xvalueCalibrationDataCrc.setStatus("mandatory")


class _Drr4xstateflagCalibrationDataCrc_Type(Integer32):
    """Custom type drr4xstateflagCalibrationDataCrc based on Integer32"""
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


_Drr4xstateflagCalibrationDataCrc_Type.__name__ = "Integer32"
_Drr4xstateflagCalibrationDataCrc_Object = MibTableColumn
drr4xstateflagCalibrationDataCrc = _Drr4xstateflagCalibrationDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 16),
    _Drr4xstateflagCalibrationDataCrc_Type()
)
drr4xstateflagCalibrationDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagCalibrationDataCrc.setStatus("mandatory")


class _Drr4xlabelHardwareStatus_Type(DisplayString):
    """Custom type drr4xlabelHardwareStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelHardwareStatus_Type.__name__ = "DisplayString"
_Drr4xlabelHardwareStatus_Object = MibTableColumn
drr4xlabelHardwareStatus = _Drr4xlabelHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 17),
    _Drr4xlabelHardwareStatus_Type()
)
drr4xlabelHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelHardwareStatus.setStatus("optional")


class _Drr4xvalueHardwareStatus_Type(Integer32):
    """Custom type drr4xvalueHardwareStatus based on Integer32"""
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


_Drr4xvalueHardwareStatus_Type.__name__ = "Integer32"
_Drr4xvalueHardwareStatus_Object = MibTableColumn
drr4xvalueHardwareStatus = _Drr4xvalueHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 18),
    _Drr4xvalueHardwareStatus_Type()
)
drr4xvalueHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xvalueHardwareStatus.setStatus("mandatory")


class _Drr4xstateflagHardwareStatus_Type(Integer32):
    """Custom type drr4xstateflagHardwareStatus based on Integer32"""
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


_Drr4xstateflagHardwareStatus_Type.__name__ = "Integer32"
_Drr4xstateflagHardwareStatus_Object = MibTableColumn
drr4xstateflagHardwareStatus = _Drr4xstateflagHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 19),
    _Drr4xstateflagHardwareStatus_Type()
)
drr4xstateflagHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagHardwareStatus.setStatus("mandatory")


class _Drr4xlabelOpticTripPointStatus_Type(DisplayString):
    """Custom type drr4xlabelOpticTripPointStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelOpticTripPointStatus_Type.__name__ = "DisplayString"
_Drr4xlabelOpticTripPointStatus_Object = MibTableColumn
drr4xlabelOpticTripPointStatus = _Drr4xlabelOpticTripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 20),
    _Drr4xlabelOpticTripPointStatus_Type()
)
drr4xlabelOpticTripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelOpticTripPointStatus.setStatus("optional")


class _Drr4xvalueOpticTripPointStatus_Type(Integer32):
    """Custom type drr4xvalueOpticTripPointStatus based on Integer32"""
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


_Drr4xvalueOpticTripPointStatus_Type.__name__ = "Integer32"
_Drr4xvalueOpticTripPointStatus_Object = MibTableColumn
drr4xvalueOpticTripPointStatus = _Drr4xvalueOpticTripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 21),
    _Drr4xvalueOpticTripPointStatus_Type()
)
drr4xvalueOpticTripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xvalueOpticTripPointStatus.setStatus("mandatory")


class _Drr4xstateflagOpticTripPointStatus_Type(Integer32):
    """Custom type drr4xstateflagOpticTripPointStatus based on Integer32"""
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


_Drr4xstateflagOpticTripPointStatus_Type.__name__ = "Integer32"
_Drr4xstateflagOpticTripPointStatus_Object = MibTableColumn
drr4xstateflagOpticTripPointStatus = _Drr4xstateflagOpticTripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 22),
    _Drr4xstateflagOpticTripPointStatus_Type()
)
drr4xstateflagOpticTripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagOpticTripPointStatus.setStatus("mandatory")


class _Drr4xlabelLinkStatus_Type(DisplayString):
    """Custom type drr4xlabelLinkStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xlabelLinkStatus_Type.__name__ = "DisplayString"
_Drr4xlabelLinkStatus_Object = MibTableColumn
drr4xlabelLinkStatus = _Drr4xlabelLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 23),
    _Drr4xlabelLinkStatus_Type()
)
drr4xlabelLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xlabelLinkStatus.setStatus("optional")


class _Drr4xvalueLinkStatus_Type(Integer32):
    """Custom type drr4xvalueLinkStatus based on Integer32"""
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


_Drr4xvalueLinkStatus_Type.__name__ = "Integer32"
_Drr4xvalueLinkStatus_Object = MibTableColumn
drr4xvalueLinkStatus = _Drr4xvalueLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 24),
    _Drr4xvalueLinkStatus_Type()
)
drr4xvalueLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xvalueLinkStatus.setStatus("mandatory")


class _Drr4xstateflagLinkStatus_Type(Integer32):
    """Custom type drr4xstateflagLinkStatus based on Integer32"""
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


_Drr4xstateflagLinkStatus_Type.__name__ = "Integer32"
_Drr4xstateflagLinkStatus_Object = MibTableColumn
drr4xstateflagLinkStatus = _Drr4xstateflagLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 4, 3, 25),
    _Drr4xstateflagLinkStatus_Type()
)
drr4xstateflagLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xstateflagLinkStatus.setStatus("mandatory")
_Gx2drr4xFactoryTable_Object = MibTable
gx2drr4xFactoryTable = _Gx2drr4xFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5)
)
if mibBuilder.loadTexts:
    gx2drr4xFactoryTable.setStatus("mandatory")
_Gx2drr4xFactoryEntry_Object = MibTableRow
gx2drr4xFactoryEntry = _Gx2drr4xFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4)
)
gx2drr4xFactoryEntry.setIndexNames(
    (0, "OMNI-gx2drr4x-MIB", "gx2drr4xFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2drr4xFactoryEntry.setStatus("mandatory")


class _Gx2drr4xFactoryTableIndex_Type(Integer32):
    """Custom type gx2drr4xFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Gx2drr4xFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2drr4xFactoryTableIndex_Object = MibTableColumn
gx2drr4xFactoryTableIndex = _Gx2drr4xFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 1),
    _Gx2drr4xFactoryTableIndex_Type()
)
gx2drr4xFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2drr4xFactoryTableIndex.setStatus("mandatory")
_Drr4xbootControlByte_Type = Integer32
_Drr4xbootControlByte_Object = MibTableColumn
drr4xbootControlByte = _Drr4xbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 2),
    _Drr4xbootControlByte_Type()
)
drr4xbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xbootControlByte.setStatus("mandatory")
_Drr4xbootStatusByte_Type = Integer32
_Drr4xbootStatusByte_Object = MibTableColumn
drr4xbootStatusByte = _Drr4xbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 3),
    _Drr4xbootStatusByte_Type()
)
drr4xbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xbootStatusByte.setStatus("mandatory")
_Drr4xbank1CRC_Type = Integer32
_Drr4xbank1CRC_Object = MibTableColumn
drr4xbank1CRC = _Drr4xbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 4),
    _Drr4xbank1CRC_Type()
)
drr4xbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xbank1CRC.setStatus("mandatory")
_Drr4xbank2CRC_Type = Integer32
_Drr4xbank2CRC_Object = MibTableColumn
drr4xbank2CRC = _Drr4xbank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 5),
    _Drr4xbank2CRC_Type()
)
drr4xbank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xbank2CRC.setStatus("mandatory")
_Drr4xprgEEPROMByte_Type = Integer32
_Drr4xprgEEPROMByte_Object = MibTableColumn
drr4xprgEEPROMByte = _Drr4xprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 6),
    _Drr4xprgEEPROMByte_Type()
)
drr4xprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xprgEEPROMByte.setStatus("mandatory")
_Drr4xfactoryCRC_Type = Integer32
_Drr4xfactoryCRC_Object = MibTableColumn
drr4xfactoryCRC = _Drr4xfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 7),
    _Drr4xfactoryCRC_Type()
)
drr4xfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xfactoryCRC.setStatus("mandatory")


class _Drr4xcalculateCRC_Type(Integer32):
    """Custom type drr4xcalculateCRC based on Integer32"""
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


_Drr4xcalculateCRC_Type.__name__ = "Integer32"
_Drr4xcalculateCRC_Object = MibTableColumn
drr4xcalculateCRC = _Drr4xcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 8),
    _Drr4xcalculateCRC_Type()
)
drr4xcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xcalculateCRC.setStatus("mandatory")
_Drr4xhourMeter_Type = Integer32
_Drr4xhourMeter_Object = MibTableColumn
drr4xhourMeter = _Drr4xhourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 9),
    _Drr4xhourMeter_Type()
)
drr4xhourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xhourMeter.setStatus("mandatory")
_Drr4xflashPrgCntA_Type = Integer32
_Drr4xflashPrgCntA_Object = MibTableColumn
drr4xflashPrgCntA = _Drr4xflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 10),
    _Drr4xflashPrgCntA_Type()
)
drr4xflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xflashPrgCntA.setStatus("mandatory")
_Drr4xflashPrgCntB_Type = Integer32
_Drr4xflashPrgCntB_Object = MibTableColumn
drr4xflashPrgCntB = _Drr4xflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 11),
    _Drr4xflashPrgCntB_Type()
)
drr4xflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xflashPrgCntB.setStatus("mandatory")


class _Drr4xflashBankARev_Type(DisplayString):
    """Custom type drr4xflashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xflashBankARev_Type.__name__ = "DisplayString"
_Drr4xflashBankARev_Object = MibTableColumn
drr4xflashBankARev = _Drr4xflashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 12),
    _Drr4xflashBankARev_Type()
)
drr4xflashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xflashBankARev.setStatus("mandatory")


class _Drr4xflashBankBRev_Type(DisplayString):
    """Custom type drr4xflashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xflashBankBRev_Type.__name__ = "DisplayString"
_Drr4xflashBankBRev_Object = MibTableColumn
drr4xflashBankBRev = _Drr4xflashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 13),
    _Drr4xflashBankBRev_Type()
)
drr4xflashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xflashBankBRev.setStatus("mandatory")


class _Drr4xSubAgentRev_Type(DisplayString):
    """Custom type drr4xSubAgentRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drr4xSubAgentRev_Type.__name__ = "DisplayString"
_Drr4xSubAgentRev_Object = MibTableColumn
drr4xSubAgentRev = _Drr4xSubAgentRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 5, 4, 14),
    _Drr4xSubAgentRev_Type()
)
drr4xSubAgentRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drr4xSubAgentRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapdrrConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 1)
)
trapdrrConfigChangeInteger.setObjects(
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
    trapdrrConfigChangeInteger.setStatus(
        ""
    )

trapdrrConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 2)
)
trapdrrConfigChangeDisplayString.setObjects(
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
    trapdrrConfigChangeDisplayString.setStatus(
        ""
    )

trapdrr12VCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 3)
)
trapdrr12VCurrentAlarm.setObjects(
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
    trapdrr12VCurrentAlarm.setStatus(
        ""
    )

trapdrrModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 4)
)
trapdrrModuleTempAlarm.setObjects(
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
    trapdrrModuleTempAlarm.setStatus(
        ""
    )

trapdrrFanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 5)
)
trapdrrFanCurrentAlarm.setObjects(
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
    trapdrrFanCurrentAlarm.setStatus(
        ""
    )

trapdrrFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 6)
)
trapdrrFlashAlarm.setObjects(
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
    trapdrrFlashAlarm.setStatus(
        ""
    )

trapdrrBankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 7)
)
trapdrrBankBootAlarm.setObjects(
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
    trapdrrBankBootAlarm.setStatus(
        ""
    )

trapdrrAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 8)
)
trapdrrAlarmDataCRCAlarm.setObjects(
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
    trapdrrAlarmDataCRCAlarm.setStatus(
        ""
    )

trapdrrHardwareErrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 9)
)
trapdrrHardwareErrAlarm.setObjects(
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
    trapdrrHardwareErrAlarm.setStatus(
        ""
    )

trapdrrOpticalSignalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 10)
)
trapdrrOpticalSignalAlarm.setObjects(
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
    trapdrrOpticalSignalAlarm.setStatus(
        ""
    )

trapdrrFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 11)
)
trapdrrFactoryDataCRCAlarm.setObjects(
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
    trapdrrFactoryDataCRCAlarm.setStatus(
        ""
    )

trapdrrResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 12)
)
trapdrrResetFactoryDefaultAlarm.setObjects(
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
    trapdrrResetFactoryDefaultAlarm.setStatus(
        ""
    )

trapdrrTripPointAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 13)
)
trapdrrTripPointAlarm.setObjects(
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
    trapdrrTripPointAlarm.setStatus(
        ""
    )

trapdrrLinkAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 14)
)
trapdrrLinkAlarm.setObjects(
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
    trapdrrLinkAlarm.setStatus(
        ""
    )

trapdrrCalibrationDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14, 0, 15)
)
trapdrrCalibrationDataCRCAlarm.setObjects(
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
    trapdrrCalibrationDataCRCAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2drr4x-MIB",
    **{"Float": Float,
       "trapdrrConfigChangeInteger": trapdrrConfigChangeInteger,
       "trapdrrConfigChangeDisplayString": trapdrrConfigChangeDisplayString,
       "trapdrr12VCurrentAlarm": trapdrr12VCurrentAlarm,
       "trapdrrModuleTempAlarm": trapdrrModuleTempAlarm,
       "trapdrrFanCurrentAlarm": trapdrrFanCurrentAlarm,
       "trapdrrFlashAlarm": trapdrrFlashAlarm,
       "trapdrrBankBootAlarm": trapdrrBankBootAlarm,
       "trapdrrAlarmDataCRCAlarm": trapdrrAlarmDataCRCAlarm,
       "trapdrrHardwareErrAlarm": trapdrrHardwareErrAlarm,
       "trapdrrOpticalSignalAlarm": trapdrrOpticalSignalAlarm,
       "trapdrrFactoryDataCRCAlarm": trapdrrFactoryDataCRCAlarm,
       "trapdrrResetFactoryDefaultAlarm": trapdrrResetFactoryDefaultAlarm,
       "trapdrrTripPointAlarm": trapdrrTripPointAlarm,
       "trapdrrLinkAlarm": trapdrrLinkAlarm,
       "trapdrrCalibrationDataCRCAlarm": trapdrrCalibrationDataCRCAlarm,
       "gx2drr4xDescriptor": gx2drr4xDescriptor,
       "gx2drr4xAnalogTable": gx2drr4xAnalogTable,
       "gx2drr4xAnalogEntry": gx2drr4xAnalogEntry,
       "gx2drr4xAnalogTableIndex": gx2drr4xAnalogTableIndex,
       "drr4xlabelRFAAttenuation": drr4xlabelRFAAttenuation,
       "drr4xuomRFAAttenuation": drr4xuomRFAAttenuation,
       "drr4xmajorHighRFAAttenuation": drr4xmajorHighRFAAttenuation,
       "drr4xmajorLowRFAAttenuation": drr4xmajorLowRFAAttenuation,
       "drr4xminorHighRFAAttenuation": drr4xminorHighRFAAttenuation,
       "drr4xminorLowRFAAttenuation": drr4xminorLowRFAAttenuation,
       "drr4xcurrentValueRFAAttenuation": drr4xcurrentValueRFAAttenuation,
       "drr4xstateFlagRFAAttenuation": drr4xstateFlagRFAAttenuation,
       "drr4xminValueRFAAttenuation": drr4xminValueRFAAttenuation,
       "drr4xmaxValueRFAAttenuation": drr4xmaxValueRFAAttenuation,
       "drr4xalarmStateRFAAttenuation": drr4xalarmStateRFAAttenuation,
       "drr4xlabelRFBAttenuation": drr4xlabelRFBAttenuation,
       "drr4xuomRFBAttenuation": drr4xuomRFBAttenuation,
       "drr4xmajorHighRFBAttenuation": drr4xmajorHighRFBAttenuation,
       "drr4xmajorLowRFBAttenuation": drr4xmajorLowRFBAttenuation,
       "drr4xminorHighRFBAttenuation": drr4xminorHighRFBAttenuation,
       "drr4xminorLowRFBAttenuation": drr4xminorLowRFBAttenuation,
       "drr4xcurrentValueRFBAttenuation": drr4xcurrentValueRFBAttenuation,
       "drr4xstateFlagRFBAttenuation": drr4xstateFlagRFBAttenuation,
       "drr4xminValueRFBAttenuation": drr4xminValueRFBAttenuation,
       "drr4xmaxValueRFBAttenuation": drr4xmaxValueRFBAttenuation,
       "drr4xalarmStateRFBAttenuation": drr4xalarmStateRFBAttenuation,
       "drr4xlabelRFCAttenuation": drr4xlabelRFCAttenuation,
       "drr4xuomRFCAttenuation": drr4xuomRFCAttenuation,
       "drr4xmajorHighRFCAttenuation": drr4xmajorHighRFCAttenuation,
       "drr4xmajorLowRFCAttenuation": drr4xmajorLowRFCAttenuation,
       "drr4xminorHighRFCAttenuation": drr4xminorHighRFCAttenuation,
       "drr4xminorLowRFCAttenuation": drr4xminorLowRFCAttenuation,
       "drr4xcurrentValueRFCAttenuation": drr4xcurrentValueRFCAttenuation,
       "drr4xstateFlagRFCAttenuation": drr4xstateFlagRFCAttenuation,
       "drr4xminValueRFCAttenuation": drr4xminValueRFCAttenuation,
       "drr4xmaxValueRFCAttenuation": drr4xmaxValueRFCAttenuation,
       "drr4xalarmStateRFCAttenuation": drr4xalarmStateRFCAttenuation,
       "drr4xlabelRFDAttenuation": drr4xlabelRFDAttenuation,
       "drr4xuomRFDAttenuation": drr4xuomRFDAttenuation,
       "drr4xmajorHighRFDAttenuation": drr4xmajorHighRFDAttenuation,
       "drr4xmajorLowRFDAttenuation": drr4xmajorLowRFDAttenuation,
       "drr4xminorHighRFDAttenuation": drr4xminorHighRFDAttenuation,
       "drr4xminorLowRFDAttenuation": drr4xminorLowRFDAttenuation,
       "drr4xcurrentValueRFDAttenuation": drr4xcurrentValueRFDAttenuation,
       "drr4xstateFlagRFDAttenuation": drr4xstateFlagRFDAttenuation,
       "drr4xminValueRFDAttenuation": drr4xminValueRFDAttenuation,
       "drr4xmaxValueRFDAttenuation": drr4xmaxValueRFDAttenuation,
       "drr4xalarmStateRFDAttenuation": drr4xalarmStateRFDAttenuation,
       "drr4xlabelTrippointLevel": drr4xlabelTrippointLevel,
       "drr4xuomTrippointLevel": drr4xuomTrippointLevel,
       "drr4xmajorHighTrippointLevel": drr4xmajorHighTrippointLevel,
       "drr4xmajorLowTrippointLevel": drr4xmajorLowTrippointLevel,
       "drr4xminorHighTrippointLevel": drr4xminorHighTrippointLevel,
       "drr4xminorLowTrippointLevel": drr4xminorLowTrippointLevel,
       "drr4xcurrentValueTrippointLevel": drr4xcurrentValueTrippointLevel,
       "drr4xstateFlagTrippointLevel": drr4xstateFlagTrippointLevel,
       "drr4xminValueTrippointLevel": drr4xminValueTrippointLevel,
       "drr4xmaxValueTrippointLevel": drr4xmaxValueTrippointLevel,
       "drr4xalarmStateTrippointLevel": drr4xalarmStateTrippointLevel,
       "drr4xlabelOptCurrent": drr4xlabelOptCurrent,
       "drr4xuomOptCurrent": drr4xuomOptCurrent,
       "drr4xmajorHighOptCurrent": drr4xmajorHighOptCurrent,
       "drr4xmajorLowOptCurrent": drr4xmajorLowOptCurrent,
       "drr4xminorHighOptCurrent": drr4xminorHighOptCurrent,
       "drr4xminorLowOptCurrent": drr4xminorLowOptCurrent,
       "drr4xcurrentValueOptCurrent": drr4xcurrentValueOptCurrent,
       "drr4xstateFlagOptCurrent": drr4xstateFlagOptCurrent,
       "drr4xminValueOptCurrent": drr4xminValueOptCurrent,
       "drr4xmaxValueOptCurrent": drr4xmaxValueOptCurrent,
       "drr4xalarmStateOptCurrent": drr4xalarmStateOptCurrent,
       "drr4xlabel12VCurrent": drr4xlabel12VCurrent,
       "drr4xuom12VCurrent": drr4xuom12VCurrent,
       "drr4xmajorHigh12VCurrent": drr4xmajorHigh12VCurrent,
       "drr4xmajorLow12VCurrent": drr4xmajorLow12VCurrent,
       "drr4xminorHigh12VCurrent": drr4xminorHigh12VCurrent,
       "drr4xminorLow12VCurrent": drr4xminorLow12VCurrent,
       "drr4xcurrentValue12VCurrent": drr4xcurrentValue12VCurrent,
       "drr4xstateFlag12VCurrent": drr4xstateFlag12VCurrent,
       "drr4xminValue12VCurrent": drr4xminValue12VCurrent,
       "drr4xmaxValue12VCurrent": drr4xmaxValue12VCurrent,
       "drr4xalarmState12VCurrent": drr4xalarmState12VCurrent,
       "drr4xlabelModTemp": drr4xlabelModTemp,
       "drr4xuomModTemp": drr4xuomModTemp,
       "drr4xmajorHighModTemp": drr4xmajorHighModTemp,
       "drr4xmajorLowModTemp": drr4xmajorLowModTemp,
       "drr4xminorHighModTemp": drr4xminorHighModTemp,
       "drr4xminorLowModTemp": drr4xminorLowModTemp,
       "drr4xcurrentValueModTemp": drr4xcurrentValueModTemp,
       "drr4xstateFlagModTemp": drr4xstateFlagModTemp,
       "drr4xminValueModTemp": drr4xminValueModTemp,
       "drr4xmaxValueModTemp": drr4xmaxValueModTemp,
       "drr4xalarmStateModTemp": drr4xalarmStateModTemp,
       "drr4xlabelFanCurrent": drr4xlabelFanCurrent,
       "drr4xuomFanCurrent": drr4xuomFanCurrent,
       "drr4xmajorHighFanCurrent": drr4xmajorHighFanCurrent,
       "drr4xmajorLowFanCurrent": drr4xmajorLowFanCurrent,
       "drr4xminorHighFanCurrent": drr4xminorHighFanCurrent,
       "drr4xminorLowFanCurrent": drr4xminorLowFanCurrent,
       "drr4xcurrentValueFanCurrent": drr4xcurrentValueFanCurrent,
       "drr4xstateFlagFanCurrent": drr4xstateFlagFanCurrent,
       "drr4xminValueFanCurrent": drr4xminValueFanCurrent,
       "drr4xmaxValueFanCurrent": drr4xmaxValueFanCurrent,
       "drr4xalarmStateFanCurrent": drr4xalarmStateFanCurrent,
       "gx2drr4xDigitalTable": gx2drr4xDigitalTable,
       "gx2drr4xDigitalEntry": gx2drr4xDigitalEntry,
       "gx2drr4xDigitalTableIndex": gx2drr4xDigitalTableIndex,
       "drr4xlabelTrippointMode": drr4xlabelTrippointMode,
       "drr4xenumTrippointMode": drr4xenumTrippointMode,
       "drr4xvalueTrippointMode": drr4xvalueTrippointMode,
       "drr4xstateflagTrippointMode": drr4xstateflagTrippointMode,
       "drr4xlabelFactoryDefaultReset": drr4xlabelFactoryDefaultReset,
       "drr4xenumFactoryDefaultReset": drr4xenumFactoryDefaultReset,
       "drr4xvalueFactoryDefaultReset": drr4xvalueFactoryDefaultReset,
       "drr4xstateflagFactoryDefaultReset": drr4xstateflagFactoryDefaultReset,
       "gx2drr4xStatusTable": gx2drr4xStatusTable,
       "gx2drr4xStatusEntry": gx2drr4xStatusEntry,
       "gx2drr4xStatusTableIndex": gx2drr4xStatusTableIndex,
       "drr4xlabelBoot": drr4xlabelBoot,
       "drr4xvalueBoot": drr4xvalueBoot,
       "drr4xstateflagBoot": drr4xstateflagBoot,
       "drr4xlabelFlash": drr4xlabelFlash,
       "drr4xvalueFlash": drr4xvalueFlash,
       "drr4xstateflagFlash": drr4xstateflagFlash,
       "drr4xlabelFactoryDataCRC": drr4xlabelFactoryDataCRC,
       "drr4xvalueFactoryDataCRC": drr4xvalueFactoryDataCRC,
       "drr4xstateflagFactoryDataCRC": drr4xstateflagFactoryDataCRC,
       "drr4xlabelAlarmDataCrc": drr4xlabelAlarmDataCrc,
       "drr4xvalueAlarmDataCrc": drr4xvalueAlarmDataCrc,
       "drr4xstateflagAlarmDataCrc": drr4xstateflagAlarmDataCrc,
       "drr4xlabelCalibrationDataCrc": drr4xlabelCalibrationDataCrc,
       "drr4xvalueCalibrationDataCrc": drr4xvalueCalibrationDataCrc,
       "drr4xstateflagCalibrationDataCrc": drr4xstateflagCalibrationDataCrc,
       "drr4xlabelHardwareStatus": drr4xlabelHardwareStatus,
       "drr4xvalueHardwareStatus": drr4xvalueHardwareStatus,
       "drr4xstateflagHardwareStatus": drr4xstateflagHardwareStatus,
       "drr4xlabelOpticTripPointStatus": drr4xlabelOpticTripPointStatus,
       "drr4xvalueOpticTripPointStatus": drr4xvalueOpticTripPointStatus,
       "drr4xstateflagOpticTripPointStatus": drr4xstateflagOpticTripPointStatus,
       "drr4xlabelLinkStatus": drr4xlabelLinkStatus,
       "drr4xvalueLinkStatus": drr4xvalueLinkStatus,
       "drr4xstateflagLinkStatus": drr4xstateflagLinkStatus,
       "gx2drr4xFactoryTable": gx2drr4xFactoryTable,
       "gx2drr4xFactoryEntry": gx2drr4xFactoryEntry,
       "gx2drr4xFactoryTableIndex": gx2drr4xFactoryTableIndex,
       "drr4xbootControlByte": drr4xbootControlByte,
       "drr4xbootStatusByte": drr4xbootStatusByte,
       "drr4xbank1CRC": drr4xbank1CRC,
       "drr4xbank2CRC": drr4xbank2CRC,
       "drr4xprgEEPROMByte": drr4xprgEEPROMByte,
       "drr4xfactoryCRC": drr4xfactoryCRC,
       "drr4xcalculateCRC": drr4xcalculateCRC,
       "drr4xhourMeter": drr4xhourMeter,
       "drr4xflashPrgCntA": drr4xflashPrgCntA,
       "drr4xflashPrgCntB": drr4xflashPrgCntB,
       "drr4xflashBankARev": drr4xflashBankARev,
       "drr4xflashBankBRev": drr4xflashBankBRev,
       "drr4xSubAgentRev": drr4xSubAgentRev}
)
