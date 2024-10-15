# SNMP MIB module (OMNI-gx2drr3x-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2drr3x-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:37 2024
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

(gx2Drr3x,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2Drr3x")

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

_Gx2drr3xDescriptor_ObjectIdentity = ObjectIdentity
gx2drr3xDescriptor = _Gx2drr3xDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 1)
)
_Gx2drr3xAnalogTable_Object = MibTable
gx2drr3xAnalogTable = _Gx2drr3xAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    gx2drr3xAnalogTable.setStatus("mandatory")
_Gx2drr3xAnalogEntry_Object = MibTableRow
gx2drr3xAnalogEntry = _Gx2drr3xAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1)
)
gx2drr3xAnalogEntry.setIndexNames(
    (0, "OMNI-gx2drr3x-MIB", "gx2drr3xAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2drr3xAnalogEntry.setStatus("mandatory")


class _Gx2drr3xAnalogTableIndex_Type(Integer32):
    """Custom type gx2drr3xAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2drr3xAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2drr3xAnalogTableIndex_Object = MibTableColumn
gx2drr3xAnalogTableIndex = _Gx2drr3xAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 1),
    _Gx2drr3xAnalogTableIndex_Type()
)
gx2drr3xAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2drr3xAnalogTableIndex.setStatus("mandatory")


class _DrrlabelRFAAttenuation_Type(DisplayString):
    """Custom type drrlabelRFAAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelRFAAttenuation_Type.__name__ = "DisplayString"
_DrrlabelRFAAttenuation_Object = MibTableColumn
drrlabelRFAAttenuation = _DrrlabelRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 2),
    _DrrlabelRFAAttenuation_Type()
)
drrlabelRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelRFAAttenuation.setStatus("optional")


class _DrruomRFAAttenuation_Type(DisplayString):
    """Custom type drruomRFAAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrruomRFAAttenuation_Type.__name__ = "DisplayString"
_DrruomRFAAttenuation_Object = MibTableColumn
drruomRFAAttenuation = _DrruomRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 3),
    _DrruomRFAAttenuation_Type()
)
drruomRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drruomRFAAttenuation.setStatus("optional")
_DrrmajorHighRFAAttenuation_Type = Float
_DrrmajorHighRFAAttenuation_Object = MibTableColumn
drrmajorHighRFAAttenuation = _DrrmajorHighRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 4),
    _DrrmajorHighRFAAttenuation_Type()
)
drrmajorHighRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorHighRFAAttenuation.setStatus("mandatory")
_DrrmajorLowRFAAttenuation_Type = Float
_DrrmajorLowRFAAttenuation_Object = MibTableColumn
drrmajorLowRFAAttenuation = _DrrmajorLowRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 5),
    _DrrmajorLowRFAAttenuation_Type()
)
drrmajorLowRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorLowRFAAttenuation.setStatus("mandatory")
_DrrminorHighRFAAttenuation_Type = Float
_DrrminorHighRFAAttenuation_Object = MibTableColumn
drrminorHighRFAAttenuation = _DrrminorHighRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 6),
    _DrrminorHighRFAAttenuation_Type()
)
drrminorHighRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorHighRFAAttenuation.setStatus("mandatory")
_DrrminorLowRFAAttenuation_Type = Float
_DrrminorLowRFAAttenuation_Object = MibTableColumn
drrminorLowRFAAttenuation = _DrrminorLowRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 7),
    _DrrminorLowRFAAttenuation_Type()
)
drrminorLowRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorLowRFAAttenuation.setStatus("mandatory")
_DrrcurrentValueRFAAttenuation_Type = Float
_DrrcurrentValueRFAAttenuation_Object = MibTableColumn
drrcurrentValueRFAAttenuation = _DrrcurrentValueRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 8),
    _DrrcurrentValueRFAAttenuation_Type()
)
drrcurrentValueRFAAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drrcurrentValueRFAAttenuation.setStatus("mandatory")


class _DrrstateFlagRFAAttenuation_Type(Integer32):
    """Custom type drrstateFlagRFAAttenuation based on Integer32"""
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


_DrrstateFlagRFAAttenuation_Type.__name__ = "Integer32"
_DrrstateFlagRFAAttenuation_Object = MibTableColumn
drrstateFlagRFAAttenuation = _DrrstateFlagRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 9),
    _DrrstateFlagRFAAttenuation_Type()
)
drrstateFlagRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateFlagRFAAttenuation.setStatus("mandatory")
_DrrminValueRFAAttenuation_Type = Float
_DrrminValueRFAAttenuation_Object = MibTableColumn
drrminValueRFAAttenuation = _DrrminValueRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 10),
    _DrrminValueRFAAttenuation_Type()
)
drrminValueRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminValueRFAAttenuation.setStatus("mandatory")
_DrrmaxValueRFAAttenuation_Type = Float
_DrrmaxValueRFAAttenuation_Object = MibTableColumn
drrmaxValueRFAAttenuation = _DrrmaxValueRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 11),
    _DrrmaxValueRFAAttenuation_Type()
)
drrmaxValueRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmaxValueRFAAttenuation.setStatus("mandatory")


class _DrralarmStateRFAAttenuation_Type(Integer32):
    """Custom type drralarmStateRFAAttenuation based on Integer32"""
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


_DrralarmStateRFAAttenuation_Type.__name__ = "Integer32"
_DrralarmStateRFAAttenuation_Object = MibTableColumn
drralarmStateRFAAttenuation = _DrralarmStateRFAAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 12),
    _DrralarmStateRFAAttenuation_Type()
)
drralarmStateRFAAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drralarmStateRFAAttenuation.setStatus("mandatory")


class _DrrlabelRFBAttenuation_Type(DisplayString):
    """Custom type drrlabelRFBAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelRFBAttenuation_Type.__name__ = "DisplayString"
_DrrlabelRFBAttenuation_Object = MibTableColumn
drrlabelRFBAttenuation = _DrrlabelRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 13),
    _DrrlabelRFBAttenuation_Type()
)
drrlabelRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelRFBAttenuation.setStatus("optional")


class _DrruomRFBAttenuation_Type(DisplayString):
    """Custom type drruomRFBAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrruomRFBAttenuation_Type.__name__ = "DisplayString"
_DrruomRFBAttenuation_Object = MibTableColumn
drruomRFBAttenuation = _DrruomRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 14),
    _DrruomRFBAttenuation_Type()
)
drruomRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drruomRFBAttenuation.setStatus("optional")
_DrrmajorHighRFBAttenuation_Type = Float
_DrrmajorHighRFBAttenuation_Object = MibTableColumn
drrmajorHighRFBAttenuation = _DrrmajorHighRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 15),
    _DrrmajorHighRFBAttenuation_Type()
)
drrmajorHighRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorHighRFBAttenuation.setStatus("mandatory")
_DrrmajorLowRFBAttenuation_Type = Float
_DrrmajorLowRFBAttenuation_Object = MibTableColumn
drrmajorLowRFBAttenuation = _DrrmajorLowRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 16),
    _DrrmajorLowRFBAttenuation_Type()
)
drrmajorLowRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorLowRFBAttenuation.setStatus("mandatory")
_DrrminorHighRFBAttenuation_Type = Float
_DrrminorHighRFBAttenuation_Object = MibTableColumn
drrminorHighRFBAttenuation = _DrrminorHighRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 17),
    _DrrminorHighRFBAttenuation_Type()
)
drrminorHighRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorHighRFBAttenuation.setStatus("mandatory")
_DrrminorLowRFBAttenuation_Type = Float
_DrrminorLowRFBAttenuation_Object = MibTableColumn
drrminorLowRFBAttenuation = _DrrminorLowRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 18),
    _DrrminorLowRFBAttenuation_Type()
)
drrminorLowRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorLowRFBAttenuation.setStatus("mandatory")
_DrrcurrentValueRFBAttenuation_Type = Float
_DrrcurrentValueRFBAttenuation_Object = MibTableColumn
drrcurrentValueRFBAttenuation = _DrrcurrentValueRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 19),
    _DrrcurrentValueRFBAttenuation_Type()
)
drrcurrentValueRFBAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drrcurrentValueRFBAttenuation.setStatus("mandatory")


class _DrrstateFlagRFBAttenuation_Type(Integer32):
    """Custom type drrstateFlagRFBAttenuation based on Integer32"""
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


_DrrstateFlagRFBAttenuation_Type.__name__ = "Integer32"
_DrrstateFlagRFBAttenuation_Object = MibTableColumn
drrstateFlagRFBAttenuation = _DrrstateFlagRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 20),
    _DrrstateFlagRFBAttenuation_Type()
)
drrstateFlagRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateFlagRFBAttenuation.setStatus("mandatory")
_DrrminValueRFBAttenuation_Type = Float
_DrrminValueRFBAttenuation_Object = MibTableColumn
drrminValueRFBAttenuation = _DrrminValueRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 21),
    _DrrminValueRFBAttenuation_Type()
)
drrminValueRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminValueRFBAttenuation.setStatus("mandatory")
_DrrmaxValueRFBAttenuation_Type = Float
_DrrmaxValueRFBAttenuation_Object = MibTableColumn
drrmaxValueRFBAttenuation = _DrrmaxValueRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 22),
    _DrrmaxValueRFBAttenuation_Type()
)
drrmaxValueRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmaxValueRFBAttenuation.setStatus("mandatory")


class _DrralarmStateRFBAttenuation_Type(Integer32):
    """Custom type drralarmStateRFBAttenuation based on Integer32"""
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


_DrralarmStateRFBAttenuation_Type.__name__ = "Integer32"
_DrralarmStateRFBAttenuation_Object = MibTableColumn
drralarmStateRFBAttenuation = _DrralarmStateRFBAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 23),
    _DrralarmStateRFBAttenuation_Type()
)
drralarmStateRFBAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drralarmStateRFBAttenuation.setStatus("mandatory")


class _DrrlabelRFCAttenuation_Type(DisplayString):
    """Custom type drrlabelRFCAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelRFCAttenuation_Type.__name__ = "DisplayString"
_DrrlabelRFCAttenuation_Object = MibTableColumn
drrlabelRFCAttenuation = _DrrlabelRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 24),
    _DrrlabelRFCAttenuation_Type()
)
drrlabelRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelRFCAttenuation.setStatus("optional")


class _DrruomRFCAttenuation_Type(DisplayString):
    """Custom type drruomRFCAttenuation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrruomRFCAttenuation_Type.__name__ = "DisplayString"
_DrruomRFCAttenuation_Object = MibTableColumn
drruomRFCAttenuation = _DrruomRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 25),
    _DrruomRFCAttenuation_Type()
)
drruomRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drruomRFCAttenuation.setStatus("optional")
_DrrmajorHighRFCAttenuation_Type = Float
_DrrmajorHighRFCAttenuation_Object = MibTableColumn
drrmajorHighRFCAttenuation = _DrrmajorHighRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 26),
    _DrrmajorHighRFCAttenuation_Type()
)
drrmajorHighRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorHighRFCAttenuation.setStatus("mandatory")
_DrrmajorLowRFCAttenuation_Type = Float
_DrrmajorLowRFCAttenuation_Object = MibTableColumn
drrmajorLowRFCAttenuation = _DrrmajorLowRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 27),
    _DrrmajorLowRFCAttenuation_Type()
)
drrmajorLowRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorLowRFCAttenuation.setStatus("mandatory")
_DrrminorHighRFCAttenuation_Type = Float
_DrrminorHighRFCAttenuation_Object = MibTableColumn
drrminorHighRFCAttenuation = _DrrminorHighRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 28),
    _DrrminorHighRFCAttenuation_Type()
)
drrminorHighRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorHighRFCAttenuation.setStatus("mandatory")
_DrrminorLowRFCAttenuation_Type = Float
_DrrminorLowRFCAttenuation_Object = MibTableColumn
drrminorLowRFCAttenuation = _DrrminorLowRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 29),
    _DrrminorLowRFCAttenuation_Type()
)
drrminorLowRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorLowRFCAttenuation.setStatus("mandatory")
_DrrcurrentValueRFCAttenuation_Type = Float
_DrrcurrentValueRFCAttenuation_Object = MibTableColumn
drrcurrentValueRFCAttenuation = _DrrcurrentValueRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 30),
    _DrrcurrentValueRFCAttenuation_Type()
)
drrcurrentValueRFCAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drrcurrentValueRFCAttenuation.setStatus("mandatory")


class _DrrstateFlagRFCAttenuation_Type(Integer32):
    """Custom type drrstateFlagRFCAttenuation based on Integer32"""
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


_DrrstateFlagRFCAttenuation_Type.__name__ = "Integer32"
_DrrstateFlagRFCAttenuation_Object = MibTableColumn
drrstateFlagRFCAttenuation = _DrrstateFlagRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 31),
    _DrrstateFlagRFCAttenuation_Type()
)
drrstateFlagRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateFlagRFCAttenuation.setStatus("mandatory")
_DrrminValueRFCAttenuation_Type = Float
_DrrminValueRFCAttenuation_Object = MibTableColumn
drrminValueRFCAttenuation = _DrrminValueRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 32),
    _DrrminValueRFCAttenuation_Type()
)
drrminValueRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminValueRFCAttenuation.setStatus("mandatory")
_DrrmaxValueRFCAttenuation_Type = Float
_DrrmaxValueRFCAttenuation_Object = MibTableColumn
drrmaxValueRFCAttenuation = _DrrmaxValueRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 33),
    _DrrmaxValueRFCAttenuation_Type()
)
drrmaxValueRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmaxValueRFCAttenuation.setStatus("mandatory")


class _DrralarmStateRFCAttenuation_Type(Integer32):
    """Custom type drralarmStateRFCAttenuation based on Integer32"""
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


_DrralarmStateRFCAttenuation_Type.__name__ = "Integer32"
_DrralarmStateRFCAttenuation_Object = MibTableColumn
drralarmStateRFCAttenuation = _DrralarmStateRFCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 34),
    _DrralarmStateRFCAttenuation_Type()
)
drralarmStateRFCAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drralarmStateRFCAttenuation.setStatus("mandatory")


class _DrrlabelTrippointLevel_Type(DisplayString):
    """Custom type drrlabelTrippointLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelTrippointLevel_Type.__name__ = "DisplayString"
_DrrlabelTrippointLevel_Object = MibTableColumn
drrlabelTrippointLevel = _DrrlabelTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 35),
    _DrrlabelTrippointLevel_Type()
)
drrlabelTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelTrippointLevel.setStatus("optional")


class _DrruomTrippointLevel_Type(DisplayString):
    """Custom type drruomTrippointLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrruomTrippointLevel_Type.__name__ = "DisplayString"
_DrruomTrippointLevel_Object = MibTableColumn
drruomTrippointLevel = _DrruomTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 36),
    _DrruomTrippointLevel_Type()
)
drruomTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drruomTrippointLevel.setStatus("optional")
_DrrmajorHighTrippointLevel_Type = Float
_DrrmajorHighTrippointLevel_Object = MibTableColumn
drrmajorHighTrippointLevel = _DrrmajorHighTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 37),
    _DrrmajorHighTrippointLevel_Type()
)
drrmajorHighTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorHighTrippointLevel.setStatus("mandatory")
_DrrmajorLowTrippointLevel_Type = Float
_DrrmajorLowTrippointLevel_Object = MibTableColumn
drrmajorLowTrippointLevel = _DrrmajorLowTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 38),
    _DrrmajorLowTrippointLevel_Type()
)
drrmajorLowTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorLowTrippointLevel.setStatus("mandatory")
_DrrminorHighTrippointLevel_Type = Float
_DrrminorHighTrippointLevel_Object = MibTableColumn
drrminorHighTrippointLevel = _DrrminorHighTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 39),
    _DrrminorHighTrippointLevel_Type()
)
drrminorHighTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorHighTrippointLevel.setStatus("mandatory")
_DrrminorLowTrippointLevel_Type = Float
_DrrminorLowTrippointLevel_Object = MibTableColumn
drrminorLowTrippointLevel = _DrrminorLowTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 40),
    _DrrminorLowTrippointLevel_Type()
)
drrminorLowTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorLowTrippointLevel.setStatus("mandatory")
_DrrcurrentValueTrippointLevel_Type = Float
_DrrcurrentValueTrippointLevel_Object = MibTableColumn
drrcurrentValueTrippointLevel = _DrrcurrentValueTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 41),
    _DrrcurrentValueTrippointLevel_Type()
)
drrcurrentValueTrippointLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drrcurrentValueTrippointLevel.setStatus("mandatory")


class _DrrstateFlagTrippointLevel_Type(Integer32):
    """Custom type drrstateFlagTrippointLevel based on Integer32"""
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


_DrrstateFlagTrippointLevel_Type.__name__ = "Integer32"
_DrrstateFlagTrippointLevel_Object = MibTableColumn
drrstateFlagTrippointLevel = _DrrstateFlagTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 42),
    _DrrstateFlagTrippointLevel_Type()
)
drrstateFlagTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateFlagTrippointLevel.setStatus("mandatory")
_DrrminValueTrippointLevel_Type = Float
_DrrminValueTrippointLevel_Object = MibTableColumn
drrminValueTrippointLevel = _DrrminValueTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 43),
    _DrrminValueTrippointLevel_Type()
)
drrminValueTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminValueTrippointLevel.setStatus("mandatory")
_DrrmaxValueTrippointLevel_Type = Float
_DrrmaxValueTrippointLevel_Object = MibTableColumn
drrmaxValueTrippointLevel = _DrrmaxValueTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 44),
    _DrrmaxValueTrippointLevel_Type()
)
drrmaxValueTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmaxValueTrippointLevel.setStatus("mandatory")


class _DrralarmStateTrippointLevel_Type(Integer32):
    """Custom type drralarmStateTrippointLevel based on Integer32"""
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


_DrralarmStateTrippointLevel_Type.__name__ = "Integer32"
_DrralarmStateTrippointLevel_Object = MibTableColumn
drralarmStateTrippointLevel = _DrralarmStateTrippointLevel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 45),
    _DrralarmStateTrippointLevel_Type()
)
drralarmStateTrippointLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drralarmStateTrippointLevel.setStatus("mandatory")


class _DrrlabelOptCurrent_Type(DisplayString):
    """Custom type drrlabelOptCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelOptCurrent_Type.__name__ = "DisplayString"
_DrrlabelOptCurrent_Object = MibTableColumn
drrlabelOptCurrent = _DrrlabelOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 46),
    _DrrlabelOptCurrent_Type()
)
drrlabelOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelOptCurrent.setStatus("optional")


class _DrruomOptCurrent_Type(DisplayString):
    """Custom type drruomOptCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrruomOptCurrent_Type.__name__ = "DisplayString"
_DrruomOptCurrent_Object = MibTableColumn
drruomOptCurrent = _DrruomOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 47),
    _DrruomOptCurrent_Type()
)
drruomOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drruomOptCurrent.setStatus("optional")
_DrrmajorHighOptCurrent_Type = Float
_DrrmajorHighOptCurrent_Object = MibTableColumn
drrmajorHighOptCurrent = _DrrmajorHighOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 48),
    _DrrmajorHighOptCurrent_Type()
)
drrmajorHighOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorHighOptCurrent.setStatus("mandatory")
_DrrmajorLowOptCurrent_Type = Float
_DrrmajorLowOptCurrent_Object = MibTableColumn
drrmajorLowOptCurrent = _DrrmajorLowOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 49),
    _DrrmajorLowOptCurrent_Type()
)
drrmajorLowOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorLowOptCurrent.setStatus("mandatory")
_DrrminorHighOptCurrent_Type = Float
_DrrminorHighOptCurrent_Object = MibTableColumn
drrminorHighOptCurrent = _DrrminorHighOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 50),
    _DrrminorHighOptCurrent_Type()
)
drrminorHighOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorHighOptCurrent.setStatus("mandatory")
_DrrminorLowOptCurrent_Type = Float
_DrrminorLowOptCurrent_Object = MibTableColumn
drrminorLowOptCurrent = _DrrminorLowOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 51),
    _DrrminorLowOptCurrent_Type()
)
drrminorLowOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorLowOptCurrent.setStatus("mandatory")
_DrrcurrentValueOptCurrent_Type = Float
_DrrcurrentValueOptCurrent_Object = MibTableColumn
drrcurrentValueOptCurrent = _DrrcurrentValueOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 52),
    _DrrcurrentValueOptCurrent_Type()
)
drrcurrentValueOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrcurrentValueOptCurrent.setStatus("mandatory")


class _DrrstateFlagOptCurrent_Type(Integer32):
    """Custom type drrstateFlagOptCurrent based on Integer32"""
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


_DrrstateFlagOptCurrent_Type.__name__ = "Integer32"
_DrrstateFlagOptCurrent_Object = MibTableColumn
drrstateFlagOptCurrent = _DrrstateFlagOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 53),
    _DrrstateFlagOptCurrent_Type()
)
drrstateFlagOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateFlagOptCurrent.setStatus("mandatory")
_DrrminValueOptCurrent_Type = Float
_DrrminValueOptCurrent_Object = MibTableColumn
drrminValueOptCurrent = _DrrminValueOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 54),
    _DrrminValueOptCurrent_Type()
)
drrminValueOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminValueOptCurrent.setStatus("mandatory")
_DrrmaxValueOptCurrent_Type = Float
_DrrmaxValueOptCurrent_Object = MibTableColumn
drrmaxValueOptCurrent = _DrrmaxValueOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 55),
    _DrrmaxValueOptCurrent_Type()
)
drrmaxValueOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmaxValueOptCurrent.setStatus("mandatory")


class _DrralarmStateOptCurrent_Type(Integer32):
    """Custom type drralarmStateOptCurrent based on Integer32"""
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


_DrralarmStateOptCurrent_Type.__name__ = "Integer32"
_DrralarmStateOptCurrent_Object = MibTableColumn
drralarmStateOptCurrent = _DrralarmStateOptCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 56),
    _DrralarmStateOptCurrent_Type()
)
drralarmStateOptCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drralarmStateOptCurrent.setStatus("mandatory")


class _Drrlabel12VCurrent_Type(DisplayString):
    """Custom type drrlabel12VCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drrlabel12VCurrent_Type.__name__ = "DisplayString"
_Drrlabel12VCurrent_Object = MibTableColumn
drrlabel12VCurrent = _Drrlabel12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 57),
    _Drrlabel12VCurrent_Type()
)
drrlabel12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabel12VCurrent.setStatus("optional")


class _Drruom12VCurrent_Type(DisplayString):
    """Custom type drruom12VCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Drruom12VCurrent_Type.__name__ = "DisplayString"
_Drruom12VCurrent_Object = MibTableColumn
drruom12VCurrent = _Drruom12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 58),
    _Drruom12VCurrent_Type()
)
drruom12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drruom12VCurrent.setStatus("optional")
_DrrmajorHigh12VCurrent_Type = Float
_DrrmajorHigh12VCurrent_Object = MibTableColumn
drrmajorHigh12VCurrent = _DrrmajorHigh12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 59),
    _DrrmajorHigh12VCurrent_Type()
)
drrmajorHigh12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorHigh12VCurrent.setStatus("mandatory")
_DrrmajorLow12VCurrent_Type = Float
_DrrmajorLow12VCurrent_Object = MibTableColumn
drrmajorLow12VCurrent = _DrrmajorLow12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 60),
    _DrrmajorLow12VCurrent_Type()
)
drrmajorLow12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorLow12VCurrent.setStatus("mandatory")
_DrrminorHigh12VCurrent_Type = Float
_DrrminorHigh12VCurrent_Object = MibTableColumn
drrminorHigh12VCurrent = _DrrminorHigh12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 61),
    _DrrminorHigh12VCurrent_Type()
)
drrminorHigh12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorHigh12VCurrent.setStatus("mandatory")
_DrrminorLow12VCurrent_Type = Float
_DrrminorLow12VCurrent_Object = MibTableColumn
drrminorLow12VCurrent = _DrrminorLow12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 62),
    _DrrminorLow12VCurrent_Type()
)
drrminorLow12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorLow12VCurrent.setStatus("mandatory")
_DrrcurrentValue12VCurrent_Type = Float
_DrrcurrentValue12VCurrent_Object = MibTableColumn
drrcurrentValue12VCurrent = _DrrcurrentValue12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 63),
    _DrrcurrentValue12VCurrent_Type()
)
drrcurrentValue12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrcurrentValue12VCurrent.setStatus("mandatory")


class _DrrstateFlag12VCurrent_Type(Integer32):
    """Custom type drrstateFlag12VCurrent based on Integer32"""
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


_DrrstateFlag12VCurrent_Type.__name__ = "Integer32"
_DrrstateFlag12VCurrent_Object = MibTableColumn
drrstateFlag12VCurrent = _DrrstateFlag12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 64),
    _DrrstateFlag12VCurrent_Type()
)
drrstateFlag12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateFlag12VCurrent.setStatus("mandatory")
_DrrminValue12VCurrent_Type = Float
_DrrminValue12VCurrent_Object = MibTableColumn
drrminValue12VCurrent = _DrrminValue12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 65),
    _DrrminValue12VCurrent_Type()
)
drrminValue12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminValue12VCurrent.setStatus("mandatory")
_DrrmaxValue12VCurrent_Type = Float
_DrrmaxValue12VCurrent_Object = MibTableColumn
drrmaxValue12VCurrent = _DrrmaxValue12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 66),
    _DrrmaxValue12VCurrent_Type()
)
drrmaxValue12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmaxValue12VCurrent.setStatus("mandatory")


class _DrralarmState12VCurrent_Type(Integer32):
    """Custom type drralarmState12VCurrent based on Integer32"""
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


_DrralarmState12VCurrent_Type.__name__ = "Integer32"
_DrralarmState12VCurrent_Object = MibTableColumn
drralarmState12VCurrent = _DrralarmState12VCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 67),
    _DrralarmState12VCurrent_Type()
)
drralarmState12VCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drralarmState12VCurrent.setStatus("mandatory")


class _DrrlabelModTemp_Type(DisplayString):
    """Custom type drrlabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelModTemp_Type.__name__ = "DisplayString"
_DrrlabelModTemp_Object = MibTableColumn
drrlabelModTemp = _DrrlabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 68),
    _DrrlabelModTemp_Type()
)
drrlabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelModTemp.setStatus("optional")


class _DrruomModTemp_Type(DisplayString):
    """Custom type drruomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrruomModTemp_Type.__name__ = "DisplayString"
_DrruomModTemp_Object = MibTableColumn
drruomModTemp = _DrruomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 69),
    _DrruomModTemp_Type()
)
drruomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drruomModTemp.setStatus("optional")
_DrrmajorHighModTemp_Type = Float
_DrrmajorHighModTemp_Object = MibTableColumn
drrmajorHighModTemp = _DrrmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 70),
    _DrrmajorHighModTemp_Type()
)
drrmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorHighModTemp.setStatus("mandatory")
_DrrmajorLowModTemp_Type = Float
_DrrmajorLowModTemp_Object = MibTableColumn
drrmajorLowModTemp = _DrrmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 71),
    _DrrmajorLowModTemp_Type()
)
drrmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorLowModTemp.setStatus("mandatory")
_DrrminorHighModTemp_Type = Float
_DrrminorHighModTemp_Object = MibTableColumn
drrminorHighModTemp = _DrrminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 72),
    _DrrminorHighModTemp_Type()
)
drrminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorHighModTemp.setStatus("mandatory")
_DrrminorLowModTemp_Type = Float
_DrrminorLowModTemp_Object = MibTableColumn
drrminorLowModTemp = _DrrminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 73),
    _DrrminorLowModTemp_Type()
)
drrminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorLowModTemp.setStatus("mandatory")
_DrrcurrentValueModTemp_Type = Float
_DrrcurrentValueModTemp_Object = MibTableColumn
drrcurrentValueModTemp = _DrrcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 74),
    _DrrcurrentValueModTemp_Type()
)
drrcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrcurrentValueModTemp.setStatus("mandatory")


class _DrrstateFlagModTemp_Type(Integer32):
    """Custom type drrstateFlagModTemp based on Integer32"""
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


_DrrstateFlagModTemp_Type.__name__ = "Integer32"
_DrrstateFlagModTemp_Object = MibTableColumn
drrstateFlagModTemp = _DrrstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 75),
    _DrrstateFlagModTemp_Type()
)
drrstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateFlagModTemp.setStatus("mandatory")
_DrrminValueModTemp_Type = Float
_DrrminValueModTemp_Object = MibTableColumn
drrminValueModTemp = _DrrminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 76),
    _DrrminValueModTemp_Type()
)
drrminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminValueModTemp.setStatus("mandatory")
_DrrmaxValueModTemp_Type = Float
_DrrmaxValueModTemp_Object = MibTableColumn
drrmaxValueModTemp = _DrrmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 77),
    _DrrmaxValueModTemp_Type()
)
drrmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmaxValueModTemp.setStatus("mandatory")


class _DrralarmStateModTemp_Type(Integer32):
    """Custom type drralarmStateModTemp based on Integer32"""
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


_DrralarmStateModTemp_Type.__name__ = "Integer32"
_DrralarmStateModTemp_Object = MibTableColumn
drralarmStateModTemp = _DrralarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 78),
    _DrralarmStateModTemp_Type()
)
drralarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drralarmStateModTemp.setStatus("mandatory")


class _DrrlabelFanCurrent_Type(DisplayString):
    """Custom type drrlabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelFanCurrent_Type.__name__ = "DisplayString"
_DrrlabelFanCurrent_Object = MibTableColumn
drrlabelFanCurrent = _DrrlabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 79),
    _DrrlabelFanCurrent_Type()
)
drrlabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelFanCurrent.setStatus("optional")


class _DrruomFanCurrent_Type(DisplayString):
    """Custom type drruomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrruomFanCurrent_Type.__name__ = "DisplayString"
_DrruomFanCurrent_Object = MibTableColumn
drruomFanCurrent = _DrruomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 80),
    _DrruomFanCurrent_Type()
)
drruomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drruomFanCurrent.setStatus("optional")
_DrrmajorHighFanCurrent_Type = Float
_DrrmajorHighFanCurrent_Object = MibTableColumn
drrmajorHighFanCurrent = _DrrmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 81),
    _DrrmajorHighFanCurrent_Type()
)
drrmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorHighFanCurrent.setStatus("mandatory")
_DrrmajorLowFanCurrent_Type = Float
_DrrmajorLowFanCurrent_Object = MibTableColumn
drrmajorLowFanCurrent = _DrrmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 82),
    _DrrmajorLowFanCurrent_Type()
)
drrmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmajorLowFanCurrent.setStatus("mandatory")
_DrrminorHighFanCurrent_Type = Float
_DrrminorHighFanCurrent_Object = MibTableColumn
drrminorHighFanCurrent = _DrrminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 83),
    _DrrminorHighFanCurrent_Type()
)
drrminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorHighFanCurrent.setStatus("mandatory")
_DrrminorLowFanCurrent_Type = Float
_DrrminorLowFanCurrent_Object = MibTableColumn
drrminorLowFanCurrent = _DrrminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 84),
    _DrrminorLowFanCurrent_Type()
)
drrminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminorLowFanCurrent.setStatus("mandatory")
_DrrcurrentValueFanCurrent_Type = Float
_DrrcurrentValueFanCurrent_Object = MibTableColumn
drrcurrentValueFanCurrent = _DrrcurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 85),
    _DrrcurrentValueFanCurrent_Type()
)
drrcurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrcurrentValueFanCurrent.setStatus("mandatory")


class _DrrstateFlagFanCurrent_Type(Integer32):
    """Custom type drrstateFlagFanCurrent based on Integer32"""
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


_DrrstateFlagFanCurrent_Type.__name__ = "Integer32"
_DrrstateFlagFanCurrent_Object = MibTableColumn
drrstateFlagFanCurrent = _DrrstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 86),
    _DrrstateFlagFanCurrent_Type()
)
drrstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateFlagFanCurrent.setStatus("mandatory")
_DrrminValueFanCurrent_Type = Float
_DrrminValueFanCurrent_Object = MibTableColumn
drrminValueFanCurrent = _DrrminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 87),
    _DrrminValueFanCurrent_Type()
)
drrminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrminValueFanCurrent.setStatus("mandatory")
_DrrmaxValueFanCurrent_Type = Float
_DrrmaxValueFanCurrent_Object = MibTableColumn
drrmaxValueFanCurrent = _DrrmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 88),
    _DrrmaxValueFanCurrent_Type()
)
drrmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrmaxValueFanCurrent.setStatus("mandatory")


class _DrralarmStateFanCurrent_Type(Integer32):
    """Custom type drralarmStateFanCurrent based on Integer32"""
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


_DrralarmStateFanCurrent_Type.__name__ = "Integer32"
_DrralarmStateFanCurrent_Object = MibTableColumn
drralarmStateFanCurrent = _DrralarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 2, 1, 89),
    _DrralarmStateFanCurrent_Type()
)
drralarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drralarmStateFanCurrent.setStatus("mandatory")
_Gx2drr3xDigitalTable_Object = MibTable
gx2drr3xDigitalTable = _Gx2drr3xDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3)
)
if mibBuilder.loadTexts:
    gx2drr3xDigitalTable.setStatus("mandatory")
_Gx2drr3xDigitalEntry_Object = MibTableRow
gx2drr3xDigitalEntry = _Gx2drr3xDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2)
)
gx2drr3xDigitalEntry.setIndexNames(
    (0, "OMNI-gx2drr3x-MIB", "gx2drr3xDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2drr3xDigitalEntry.setStatus("mandatory")


class _Gx2drr3xDigitalTableIndex_Type(Integer32):
    """Custom type gx2drr3xDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2drr3xDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2drr3xDigitalTableIndex_Object = MibTableColumn
gx2drr3xDigitalTableIndex = _Gx2drr3xDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 1),
    _Gx2drr3xDigitalTableIndex_Type()
)
gx2drr3xDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2drr3xDigitalTableIndex.setStatus("mandatory")


class _DrrlabelTrippointMode_Type(DisplayString):
    """Custom type drrlabelTrippointMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelTrippointMode_Type.__name__ = "DisplayString"
_DrrlabelTrippointMode_Object = MibTableColumn
drrlabelTrippointMode = _DrrlabelTrippointMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 2),
    _DrrlabelTrippointMode_Type()
)
drrlabelTrippointMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelTrippointMode.setStatus("optional")


class _DrrenumTrippointMode_Type(DisplayString):
    """Custom type drrenumTrippointMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrenumTrippointMode_Type.__name__ = "DisplayString"
_DrrenumTrippointMode_Object = MibTableColumn
drrenumTrippointMode = _DrrenumTrippointMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 3),
    _DrrenumTrippointMode_Type()
)
drrenumTrippointMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrenumTrippointMode.setStatus("optional")


class _DrrvalueTrippointMode_Type(Integer32):
    """Custom type drrvalueTrippointMode based on Integer32"""
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


_DrrvalueTrippointMode_Type.__name__ = "Integer32"
_DrrvalueTrippointMode_Object = MibTableColumn
drrvalueTrippointMode = _DrrvalueTrippointMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 4),
    _DrrvalueTrippointMode_Type()
)
drrvalueTrippointMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drrvalueTrippointMode.setStatus("mandatory")


class _DrrstateflagTrippointMode_Type(Integer32):
    """Custom type drrstateflagTrippointMode based on Integer32"""
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


_DrrstateflagTrippointMode_Type.__name__ = "Integer32"
_DrrstateflagTrippointMode_Object = MibTableColumn
drrstateflagTrippointMode = _DrrstateflagTrippointMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 5),
    _DrrstateflagTrippointMode_Type()
)
drrstateflagTrippointMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagTrippointMode.setStatus("mandatory")


class _DrrlabelFrontPanelTest_Type(DisplayString):
    """Custom type drrlabelFrontPanelTest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelFrontPanelTest_Type.__name__ = "DisplayString"
_DrrlabelFrontPanelTest_Object = MibTableColumn
drrlabelFrontPanelTest = _DrrlabelFrontPanelTest_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 6),
    _DrrlabelFrontPanelTest_Type()
)
drrlabelFrontPanelTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelFrontPanelTest.setStatus("optional")


class _DrrenumFrontPanelTest_Type(DisplayString):
    """Custom type drrenumFrontPanelTest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrenumFrontPanelTest_Type.__name__ = "DisplayString"
_DrrenumFrontPanelTest_Object = MibTableColumn
drrenumFrontPanelTest = _DrrenumFrontPanelTest_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 7),
    _DrrenumFrontPanelTest_Type()
)
drrenumFrontPanelTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrenumFrontPanelTest.setStatus("optional")


class _DrrvalueFrontPanelTest_Type(Integer32):
    """Custom type drrvalueFrontPanelTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chanA", 1),
          ("chanB", 2),
          ("chanC", 3))
    )


_DrrvalueFrontPanelTest_Type.__name__ = "Integer32"
_DrrvalueFrontPanelTest_Object = MibTableColumn
drrvalueFrontPanelTest = _DrrvalueFrontPanelTest_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 8),
    _DrrvalueFrontPanelTest_Type()
)
drrvalueFrontPanelTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drrvalueFrontPanelTest.setStatus("mandatory")


class _DrrstateflagFrontPanelTest_Type(Integer32):
    """Custom type drrstateflagFrontPanelTest based on Integer32"""
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


_DrrstateflagFrontPanelTest_Type.__name__ = "Integer32"
_DrrstateflagFrontPanelTest_Object = MibTableColumn
drrstateflagFrontPanelTest = _DrrstateflagFrontPanelTest_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 9),
    _DrrstateflagFrontPanelTest_Type()
)
drrstateflagFrontPanelTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagFrontPanelTest.setStatus("mandatory")


class _DrrlabelFactoryDefaultReset_Type(DisplayString):
    """Custom type drrlabelFactoryDefaultReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelFactoryDefaultReset_Type.__name__ = "DisplayString"
_DrrlabelFactoryDefaultReset_Object = MibTableColumn
drrlabelFactoryDefaultReset = _DrrlabelFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 10),
    _DrrlabelFactoryDefaultReset_Type()
)
drrlabelFactoryDefaultReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelFactoryDefaultReset.setStatus("optional")


class _DrrenumFactoryDefaultReset_Type(DisplayString):
    """Custom type drrenumFactoryDefaultReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrenumFactoryDefaultReset_Type.__name__ = "DisplayString"
_DrrenumFactoryDefaultReset_Object = MibTableColumn
drrenumFactoryDefaultReset = _DrrenumFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 11),
    _DrrenumFactoryDefaultReset_Type()
)
drrenumFactoryDefaultReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrenumFactoryDefaultReset.setStatus("optional")


class _DrrvalueFactoryDefaultReset_Type(Integer32):
    """Custom type drrvalueFactoryDefaultReset based on Integer32"""
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


_DrrvalueFactoryDefaultReset_Type.__name__ = "Integer32"
_DrrvalueFactoryDefaultReset_Object = MibTableColumn
drrvalueFactoryDefaultReset = _DrrvalueFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 12),
    _DrrvalueFactoryDefaultReset_Type()
)
drrvalueFactoryDefaultReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drrvalueFactoryDefaultReset.setStatus("mandatory")


class _DrrstateflagFactoryDefaultReset_Type(Integer32):
    """Custom type drrstateflagFactoryDefaultReset based on Integer32"""
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


_DrrstateflagFactoryDefaultReset_Type.__name__ = "Integer32"
_DrrstateflagFactoryDefaultReset_Object = MibTableColumn
drrstateflagFactoryDefaultReset = _DrrstateflagFactoryDefaultReset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 3, 2, 13),
    _DrrstateflagFactoryDefaultReset_Type()
)
drrstateflagFactoryDefaultReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagFactoryDefaultReset.setStatus("mandatory")
_Gx2drr3xStatusTable_Object = MibTable
gx2drr3xStatusTable = _Gx2drr3xStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4)
)
if mibBuilder.loadTexts:
    gx2drr3xStatusTable.setStatus("mandatory")
_Gx2drr3xStatusEntry_Object = MibTableRow
gx2drr3xStatusEntry = _Gx2drr3xStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3)
)
gx2drr3xStatusEntry.setIndexNames(
    (0, "OMNI-gx2drr3x-MIB", "gx2drr3xStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2drr3xStatusEntry.setStatus("mandatory")


class _Gx2drr3xStatusTableIndex_Type(Integer32):
    """Custom type gx2drr3xStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2drr3xStatusTableIndex_Type.__name__ = "Integer32"
_Gx2drr3xStatusTableIndex_Object = MibTableColumn
gx2drr3xStatusTableIndex = _Gx2drr3xStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 1),
    _Gx2drr3xStatusTableIndex_Type()
)
gx2drr3xStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2drr3xStatusTableIndex.setStatus("mandatory")


class _DrrlabelBoot_Type(DisplayString):
    """Custom type drrlabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelBoot_Type.__name__ = "DisplayString"
_DrrlabelBoot_Object = MibTableColumn
drrlabelBoot = _DrrlabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 2),
    _DrrlabelBoot_Type()
)
drrlabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelBoot.setStatus("optional")


class _DrrvalueBoot_Type(Integer32):
    """Custom type drrvalueBoot based on Integer32"""
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


_DrrvalueBoot_Type.__name__ = "Integer32"
_DrrvalueBoot_Object = MibTableColumn
drrvalueBoot = _DrrvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 3),
    _DrrvalueBoot_Type()
)
drrvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrvalueBoot.setStatus("mandatory")


class _DrrstateflagBoot_Type(Integer32):
    """Custom type drrstateflagBoot based on Integer32"""
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


_DrrstateflagBoot_Type.__name__ = "Integer32"
_DrrstateflagBoot_Object = MibTableColumn
drrstateflagBoot = _DrrstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 4),
    _DrrstateflagBoot_Type()
)
drrstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagBoot.setStatus("mandatory")


class _DrrlabelFlash_Type(DisplayString):
    """Custom type drrlabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelFlash_Type.__name__ = "DisplayString"
_DrrlabelFlash_Object = MibTableColumn
drrlabelFlash = _DrrlabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 5),
    _DrrlabelFlash_Type()
)
drrlabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelFlash.setStatus("optional")


class _DrrvalueFlash_Type(Integer32):
    """Custom type drrvalueFlash based on Integer32"""
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


_DrrvalueFlash_Type.__name__ = "Integer32"
_DrrvalueFlash_Object = MibTableColumn
drrvalueFlash = _DrrvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 6),
    _DrrvalueFlash_Type()
)
drrvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrvalueFlash.setStatus("mandatory")


class _DrrstateflagFlash_Type(Integer32):
    """Custom type drrstateflagFlash based on Integer32"""
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


_DrrstateflagFlash_Type.__name__ = "Integer32"
_DrrstateflagFlash_Object = MibTableColumn
drrstateflagFlash = _DrrstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 7),
    _DrrstateflagFlash_Type()
)
drrstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagFlash.setStatus("mandatory")


class _DrrlabelFactoryDataCRC_Type(DisplayString):
    """Custom type drrlabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelFactoryDataCRC_Type.__name__ = "DisplayString"
_DrrlabelFactoryDataCRC_Object = MibTableColumn
drrlabelFactoryDataCRC = _DrrlabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 8),
    _DrrlabelFactoryDataCRC_Type()
)
drrlabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelFactoryDataCRC.setStatus("optional")


class _DrrvalueFactoryDataCRC_Type(Integer32):
    """Custom type drrvalueFactoryDataCRC based on Integer32"""
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


_DrrvalueFactoryDataCRC_Type.__name__ = "Integer32"
_DrrvalueFactoryDataCRC_Object = MibTableColumn
drrvalueFactoryDataCRC = _DrrvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 9),
    _DrrvalueFactoryDataCRC_Type()
)
drrvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrvalueFactoryDataCRC.setStatus("mandatory")


class _DrrstateflagFactoryDataCRC_Type(Integer32):
    """Custom type drrstateflagFactoryDataCRC based on Integer32"""
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


_DrrstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_DrrstateflagFactoryDataCRC_Object = MibTableColumn
drrstateflagFactoryDataCRC = _DrrstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 10),
    _DrrstateflagFactoryDataCRC_Type()
)
drrstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagFactoryDataCRC.setStatus("mandatory")


class _DrrlabelAlarmDataCrc_Type(DisplayString):
    """Custom type drrlabelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelAlarmDataCrc_Type.__name__ = "DisplayString"
_DrrlabelAlarmDataCrc_Object = MibTableColumn
drrlabelAlarmDataCrc = _DrrlabelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 11),
    _DrrlabelAlarmDataCrc_Type()
)
drrlabelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelAlarmDataCrc.setStatus("optional")


class _DrrvalueAlarmDataCrc_Type(Integer32):
    """Custom type drrvalueAlarmDataCrc based on Integer32"""
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


_DrrvalueAlarmDataCrc_Type.__name__ = "Integer32"
_DrrvalueAlarmDataCrc_Object = MibTableColumn
drrvalueAlarmDataCrc = _DrrvalueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 12),
    _DrrvalueAlarmDataCrc_Type()
)
drrvalueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrvalueAlarmDataCrc.setStatus("mandatory")


class _DrrstateflagAlarmDataCrc_Type(Integer32):
    """Custom type drrstateflagAlarmDataCrc based on Integer32"""
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


_DrrstateflagAlarmDataCrc_Type.__name__ = "Integer32"
_DrrstateflagAlarmDataCrc_Object = MibTableColumn
drrstateflagAlarmDataCrc = _DrrstateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 13),
    _DrrstateflagAlarmDataCrc_Type()
)
drrstateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagAlarmDataCrc.setStatus("mandatory")


class _DrrlabelHardwareStatus_Type(DisplayString):
    """Custom type drrlabelHardwareStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelHardwareStatus_Type.__name__ = "DisplayString"
_DrrlabelHardwareStatus_Object = MibTableColumn
drrlabelHardwareStatus = _DrrlabelHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 14),
    _DrrlabelHardwareStatus_Type()
)
drrlabelHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelHardwareStatus.setStatus("optional")


class _DrrvalueHardwareStatus_Type(Integer32):
    """Custom type drrvalueHardwareStatus based on Integer32"""
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


_DrrvalueHardwareStatus_Type.__name__ = "Integer32"
_DrrvalueHardwareStatus_Object = MibTableColumn
drrvalueHardwareStatus = _DrrvalueHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 15),
    _DrrvalueHardwareStatus_Type()
)
drrvalueHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrvalueHardwareStatus.setStatus("mandatory")


class _DrrstateflagHardwareStatus_Type(Integer32):
    """Custom type drrstateflagHardwareStatus based on Integer32"""
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


_DrrstateflagHardwareStatus_Type.__name__ = "Integer32"
_DrrstateflagHardwareStatus_Object = MibTableColumn
drrstateflagHardwareStatus = _DrrstateflagHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 16),
    _DrrstateflagHardwareStatus_Type()
)
drrstateflagHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagHardwareStatus.setStatus("mandatory")


class _DrrlabelOpticTripPointStatus_Type(DisplayString):
    """Custom type drrlabelOpticTripPointStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelOpticTripPointStatus_Type.__name__ = "DisplayString"
_DrrlabelOpticTripPointStatus_Object = MibTableColumn
drrlabelOpticTripPointStatus = _DrrlabelOpticTripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 17),
    _DrrlabelOpticTripPointStatus_Type()
)
drrlabelOpticTripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelOpticTripPointStatus.setStatus("optional")


class _DrrvalueOpticTripPointStatus_Type(Integer32):
    """Custom type drrvalueOpticTripPointStatus based on Integer32"""
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


_DrrvalueOpticTripPointStatus_Type.__name__ = "Integer32"
_DrrvalueOpticTripPointStatus_Object = MibTableColumn
drrvalueOpticTripPointStatus = _DrrvalueOpticTripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 18),
    _DrrvalueOpticTripPointStatus_Type()
)
drrvalueOpticTripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrvalueOpticTripPointStatus.setStatus("mandatory")


class _DrrstateflagOpticTripPointStatus_Type(Integer32):
    """Custom type drrstateflagOpticTripPointStatus based on Integer32"""
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


_DrrstateflagOpticTripPointStatus_Type.__name__ = "Integer32"
_DrrstateflagOpticTripPointStatus_Object = MibTableColumn
drrstateflagOpticTripPointStatus = _DrrstateflagOpticTripPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 19),
    _DrrstateflagOpticTripPointStatus_Type()
)
drrstateflagOpticTripPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagOpticTripPointStatus.setStatus("mandatory")


class _DrrlabelLinkStatus_Type(DisplayString):
    """Custom type drrlabelLinkStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrlabelLinkStatus_Type.__name__ = "DisplayString"
_DrrlabelLinkStatus_Object = MibTableColumn
drrlabelLinkStatus = _DrrlabelLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 20),
    _DrrlabelLinkStatus_Type()
)
drrlabelLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrlabelLinkStatus.setStatus("optional")


class _DrrvalueLinkStatus_Type(Integer32):
    """Custom type drrvalueLinkStatus based on Integer32"""
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


_DrrvalueLinkStatus_Type.__name__ = "Integer32"
_DrrvalueLinkStatus_Object = MibTableColumn
drrvalueLinkStatus = _DrrvalueLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 21),
    _DrrvalueLinkStatus_Type()
)
drrvalueLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrvalueLinkStatus.setStatus("mandatory")


class _DrrstateflagLinkStatus_Type(Integer32):
    """Custom type drrstateflagLinkStatus based on Integer32"""
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


_DrrstateflagLinkStatus_Type.__name__ = "Integer32"
_DrrstateflagLinkStatus_Object = MibTableColumn
drrstateflagLinkStatus = _DrrstateflagLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 4, 3, 22),
    _DrrstateflagLinkStatus_Type()
)
drrstateflagLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrstateflagLinkStatus.setStatus("mandatory")
_Gx2drr3xFactoryTable_Object = MibTable
gx2drr3xFactoryTable = _Gx2drr3xFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5)
)
if mibBuilder.loadTexts:
    gx2drr3xFactoryTable.setStatus("mandatory")
_Gx2drr3xFactoryEntry_Object = MibTableRow
gx2drr3xFactoryEntry = _Gx2drr3xFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4)
)
gx2drr3xFactoryEntry.setIndexNames(
    (0, "OMNI-gx2drr3x-MIB", "gx2drr3xFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2drr3xFactoryEntry.setStatus("mandatory")


class _Gx2drr3xFactoryTableIndex_Type(Integer32):
    """Custom type gx2drr3xFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2drr3xFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2drr3xFactoryTableIndex_Object = MibTableColumn
gx2drr3xFactoryTableIndex = _Gx2drr3xFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 1),
    _Gx2drr3xFactoryTableIndex_Type()
)
gx2drr3xFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2drr3xFactoryTableIndex.setStatus("mandatory")
_DrrbootControlByte_Type = Integer32
_DrrbootControlByte_Object = MibTableColumn
drrbootControlByte = _DrrbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 2),
    _DrrbootControlByte_Type()
)
drrbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrbootControlByte.setStatus("mandatory")
_DrrbootStatusByte_Type = Integer32
_DrrbootStatusByte_Object = MibTableColumn
drrbootStatusByte = _DrrbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 3),
    _DrrbootStatusByte_Type()
)
drrbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrbootStatusByte.setStatus("mandatory")
_Drrbank1CRC_Type = Integer32
_Drrbank1CRC_Object = MibTableColumn
drrbank1CRC = _Drrbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 4),
    _Drrbank1CRC_Type()
)
drrbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrbank1CRC.setStatus("mandatory")
_Drrbank2CRC_Type = Integer32
_Drrbank2CRC_Object = MibTableColumn
drrbank2CRC = _Drrbank2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 5),
    _Drrbank2CRC_Type()
)
drrbank2CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrbank2CRC.setStatus("mandatory")
_DrrprgEEPROMByte_Type = Integer32
_DrrprgEEPROMByte_Object = MibTableColumn
drrprgEEPROMByte = _DrrprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 6),
    _DrrprgEEPROMByte_Type()
)
drrprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrprgEEPROMByte.setStatus("mandatory")
_DrrfactoryCRC_Type = Integer32
_DrrfactoryCRC_Object = MibTableColumn
drrfactoryCRC = _DrrfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 7),
    _DrrfactoryCRC_Type()
)
drrfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrfactoryCRC.setStatus("mandatory")


class _DrrcalculateCRC_Type(Integer32):
    """Custom type drrcalculateCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("factory", 1))
    )


_DrrcalculateCRC_Type.__name__ = "Integer32"
_DrrcalculateCRC_Object = MibTableColumn
drrcalculateCRC = _DrrcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 8),
    _DrrcalculateCRC_Type()
)
drrcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrcalculateCRC.setStatus("mandatory")
_DrrhourMeter_Type = Integer32
_DrrhourMeter_Object = MibTableColumn
drrhourMeter = _DrrhourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 9),
    _DrrhourMeter_Type()
)
drrhourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrhourMeter.setStatus("mandatory")
_DrrflashPrgCntA_Type = Integer32
_DrrflashPrgCntA_Object = MibTableColumn
drrflashPrgCntA = _DrrflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 10),
    _DrrflashPrgCntA_Type()
)
drrflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrflashPrgCntA.setStatus("mandatory")
_DrrflashPrgCntB_Type = Integer32
_DrrflashPrgCntB_Object = MibTableColumn
drrflashPrgCntB = _DrrflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 11),
    _DrrflashPrgCntB_Type()
)
drrflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrflashPrgCntB.setStatus("mandatory")


class _DrrflashBankARev_Type(DisplayString):
    """Custom type drrflashBankARev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrflashBankARev_Type.__name__ = "DisplayString"
_DrrflashBankARev_Object = MibTableColumn
drrflashBankARev = _DrrflashBankARev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 12),
    _DrrflashBankARev_Type()
)
drrflashBankARev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrflashBankARev.setStatus("mandatory")


class _DrrflashBankBRev_Type(DisplayString):
    """Custom type drrflashBankBRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrrflashBankBRev_Type.__name__ = "DisplayString"
_DrrflashBankBRev_Object = MibTableColumn
drrflashBankBRev = _DrrflashBankBRev_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 5, 4, 13),
    _DrrflashBankBRev_Type()
)
drrflashBankBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drrflashBankBRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapdrrConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 1)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 2)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 3)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 4)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 5)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 6)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 7)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 8)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 9)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 10)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 11)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 12)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 13)
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
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13, 0, 14)
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


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2drr3x-MIB",
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
       "gx2drr3xDescriptor": gx2drr3xDescriptor,
       "gx2drr3xAnalogTable": gx2drr3xAnalogTable,
       "gx2drr3xAnalogEntry": gx2drr3xAnalogEntry,
       "gx2drr3xAnalogTableIndex": gx2drr3xAnalogTableIndex,
       "drrlabelRFAAttenuation": drrlabelRFAAttenuation,
       "drruomRFAAttenuation": drruomRFAAttenuation,
       "drrmajorHighRFAAttenuation": drrmajorHighRFAAttenuation,
       "drrmajorLowRFAAttenuation": drrmajorLowRFAAttenuation,
       "drrminorHighRFAAttenuation": drrminorHighRFAAttenuation,
       "drrminorLowRFAAttenuation": drrminorLowRFAAttenuation,
       "drrcurrentValueRFAAttenuation": drrcurrentValueRFAAttenuation,
       "drrstateFlagRFAAttenuation": drrstateFlagRFAAttenuation,
       "drrminValueRFAAttenuation": drrminValueRFAAttenuation,
       "drrmaxValueRFAAttenuation": drrmaxValueRFAAttenuation,
       "drralarmStateRFAAttenuation": drralarmStateRFAAttenuation,
       "drrlabelRFBAttenuation": drrlabelRFBAttenuation,
       "drruomRFBAttenuation": drruomRFBAttenuation,
       "drrmajorHighRFBAttenuation": drrmajorHighRFBAttenuation,
       "drrmajorLowRFBAttenuation": drrmajorLowRFBAttenuation,
       "drrminorHighRFBAttenuation": drrminorHighRFBAttenuation,
       "drrminorLowRFBAttenuation": drrminorLowRFBAttenuation,
       "drrcurrentValueRFBAttenuation": drrcurrentValueRFBAttenuation,
       "drrstateFlagRFBAttenuation": drrstateFlagRFBAttenuation,
       "drrminValueRFBAttenuation": drrminValueRFBAttenuation,
       "drrmaxValueRFBAttenuation": drrmaxValueRFBAttenuation,
       "drralarmStateRFBAttenuation": drralarmStateRFBAttenuation,
       "drrlabelRFCAttenuation": drrlabelRFCAttenuation,
       "drruomRFCAttenuation": drruomRFCAttenuation,
       "drrmajorHighRFCAttenuation": drrmajorHighRFCAttenuation,
       "drrmajorLowRFCAttenuation": drrmajorLowRFCAttenuation,
       "drrminorHighRFCAttenuation": drrminorHighRFCAttenuation,
       "drrminorLowRFCAttenuation": drrminorLowRFCAttenuation,
       "drrcurrentValueRFCAttenuation": drrcurrentValueRFCAttenuation,
       "drrstateFlagRFCAttenuation": drrstateFlagRFCAttenuation,
       "drrminValueRFCAttenuation": drrminValueRFCAttenuation,
       "drrmaxValueRFCAttenuation": drrmaxValueRFCAttenuation,
       "drralarmStateRFCAttenuation": drralarmStateRFCAttenuation,
       "drrlabelTrippointLevel": drrlabelTrippointLevel,
       "drruomTrippointLevel": drruomTrippointLevel,
       "drrmajorHighTrippointLevel": drrmajorHighTrippointLevel,
       "drrmajorLowTrippointLevel": drrmajorLowTrippointLevel,
       "drrminorHighTrippointLevel": drrminorHighTrippointLevel,
       "drrminorLowTrippointLevel": drrminorLowTrippointLevel,
       "drrcurrentValueTrippointLevel": drrcurrentValueTrippointLevel,
       "drrstateFlagTrippointLevel": drrstateFlagTrippointLevel,
       "drrminValueTrippointLevel": drrminValueTrippointLevel,
       "drrmaxValueTrippointLevel": drrmaxValueTrippointLevel,
       "drralarmStateTrippointLevel": drralarmStateTrippointLevel,
       "drrlabelOptCurrent": drrlabelOptCurrent,
       "drruomOptCurrent": drruomOptCurrent,
       "drrmajorHighOptCurrent": drrmajorHighOptCurrent,
       "drrmajorLowOptCurrent": drrmajorLowOptCurrent,
       "drrminorHighOptCurrent": drrminorHighOptCurrent,
       "drrminorLowOptCurrent": drrminorLowOptCurrent,
       "drrcurrentValueOptCurrent": drrcurrentValueOptCurrent,
       "drrstateFlagOptCurrent": drrstateFlagOptCurrent,
       "drrminValueOptCurrent": drrminValueOptCurrent,
       "drrmaxValueOptCurrent": drrmaxValueOptCurrent,
       "drralarmStateOptCurrent": drralarmStateOptCurrent,
       "drrlabel12VCurrent": drrlabel12VCurrent,
       "drruom12VCurrent": drruom12VCurrent,
       "drrmajorHigh12VCurrent": drrmajorHigh12VCurrent,
       "drrmajorLow12VCurrent": drrmajorLow12VCurrent,
       "drrminorHigh12VCurrent": drrminorHigh12VCurrent,
       "drrminorLow12VCurrent": drrminorLow12VCurrent,
       "drrcurrentValue12VCurrent": drrcurrentValue12VCurrent,
       "drrstateFlag12VCurrent": drrstateFlag12VCurrent,
       "drrminValue12VCurrent": drrminValue12VCurrent,
       "drrmaxValue12VCurrent": drrmaxValue12VCurrent,
       "drralarmState12VCurrent": drralarmState12VCurrent,
       "drrlabelModTemp": drrlabelModTemp,
       "drruomModTemp": drruomModTemp,
       "drrmajorHighModTemp": drrmajorHighModTemp,
       "drrmajorLowModTemp": drrmajorLowModTemp,
       "drrminorHighModTemp": drrminorHighModTemp,
       "drrminorLowModTemp": drrminorLowModTemp,
       "drrcurrentValueModTemp": drrcurrentValueModTemp,
       "drrstateFlagModTemp": drrstateFlagModTemp,
       "drrminValueModTemp": drrminValueModTemp,
       "drrmaxValueModTemp": drrmaxValueModTemp,
       "drralarmStateModTemp": drralarmStateModTemp,
       "drrlabelFanCurrent": drrlabelFanCurrent,
       "drruomFanCurrent": drruomFanCurrent,
       "drrmajorHighFanCurrent": drrmajorHighFanCurrent,
       "drrmajorLowFanCurrent": drrmajorLowFanCurrent,
       "drrminorHighFanCurrent": drrminorHighFanCurrent,
       "drrminorLowFanCurrent": drrminorLowFanCurrent,
       "drrcurrentValueFanCurrent": drrcurrentValueFanCurrent,
       "drrstateFlagFanCurrent": drrstateFlagFanCurrent,
       "drrminValueFanCurrent": drrminValueFanCurrent,
       "drrmaxValueFanCurrent": drrmaxValueFanCurrent,
       "drralarmStateFanCurrent": drralarmStateFanCurrent,
       "gx2drr3xDigitalTable": gx2drr3xDigitalTable,
       "gx2drr3xDigitalEntry": gx2drr3xDigitalEntry,
       "gx2drr3xDigitalTableIndex": gx2drr3xDigitalTableIndex,
       "drrlabelTrippointMode": drrlabelTrippointMode,
       "drrenumTrippointMode": drrenumTrippointMode,
       "drrvalueTrippointMode": drrvalueTrippointMode,
       "drrstateflagTrippointMode": drrstateflagTrippointMode,
       "drrlabelFrontPanelTest": drrlabelFrontPanelTest,
       "drrenumFrontPanelTest": drrenumFrontPanelTest,
       "drrvalueFrontPanelTest": drrvalueFrontPanelTest,
       "drrstateflagFrontPanelTest": drrstateflagFrontPanelTest,
       "drrlabelFactoryDefaultReset": drrlabelFactoryDefaultReset,
       "drrenumFactoryDefaultReset": drrenumFactoryDefaultReset,
       "drrvalueFactoryDefaultReset": drrvalueFactoryDefaultReset,
       "drrstateflagFactoryDefaultReset": drrstateflagFactoryDefaultReset,
       "gx2drr3xStatusTable": gx2drr3xStatusTable,
       "gx2drr3xStatusEntry": gx2drr3xStatusEntry,
       "gx2drr3xStatusTableIndex": gx2drr3xStatusTableIndex,
       "drrlabelBoot": drrlabelBoot,
       "drrvalueBoot": drrvalueBoot,
       "drrstateflagBoot": drrstateflagBoot,
       "drrlabelFlash": drrlabelFlash,
       "drrvalueFlash": drrvalueFlash,
       "drrstateflagFlash": drrstateflagFlash,
       "drrlabelFactoryDataCRC": drrlabelFactoryDataCRC,
       "drrvalueFactoryDataCRC": drrvalueFactoryDataCRC,
       "drrstateflagFactoryDataCRC": drrstateflagFactoryDataCRC,
       "drrlabelAlarmDataCrc": drrlabelAlarmDataCrc,
       "drrvalueAlarmDataCrc": drrvalueAlarmDataCrc,
       "drrstateflagAlarmDataCrc": drrstateflagAlarmDataCrc,
       "drrlabelHardwareStatus": drrlabelHardwareStatus,
       "drrvalueHardwareStatus": drrvalueHardwareStatus,
       "drrstateflagHardwareStatus": drrstateflagHardwareStatus,
       "drrlabelOpticTripPointStatus": drrlabelOpticTripPointStatus,
       "drrvalueOpticTripPointStatus": drrvalueOpticTripPointStatus,
       "drrstateflagOpticTripPointStatus": drrstateflagOpticTripPointStatus,
       "drrlabelLinkStatus": drrlabelLinkStatus,
       "drrvalueLinkStatus": drrvalueLinkStatus,
       "drrstateflagLinkStatus": drrstateflagLinkStatus,
       "gx2drr3xFactoryTable": gx2drr3xFactoryTable,
       "gx2drr3xFactoryEntry": gx2drr3xFactoryEntry,
       "gx2drr3xFactoryTableIndex": gx2drr3xFactoryTableIndex,
       "drrbootControlByte": drrbootControlByte,
       "drrbootStatusByte": drrbootStatusByte,
       "drrbank1CRC": drrbank1CRC,
       "drrbank2CRC": drrbank2CRC,
       "drrprgEEPROMByte": drrprgEEPROMByte,
       "drrfactoryCRC": drrfactoryCRC,
       "drrcalculateCRC": drrcalculateCRC,
       "drrhourMeter": drrhourMeter,
       "drrflashPrgCntA": drrflashPrgCntA,
       "drrflashPrgCntB": drrflashPrgCntB,
       "drrflashBankARev": drrflashBankARev,
       "drrflashBankBRev": drrflashBankBRev}
)
