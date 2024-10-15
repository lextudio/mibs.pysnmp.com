# SNMP MIB module (OMNI-gx2oa100bd-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2oa100bd-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:41 2024
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

(gx2OA100BD,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2OA100BD")

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

_Gx2OA100BDDescriptor_ObjectIdentity = ObjectIdentity
gx2OA100BDDescriptor = _Gx2OA100BDDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 1)
)
_Gx2OA100BDAnalogTable_Object = MibTable
gx2OA100BDAnalogTable = _Gx2OA100BDAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2)
)
if mibBuilder.loadTexts:
    gx2OA100BDAnalogTable.setStatus("mandatory")
_Gx2OA100BDAnalogEntry_Object = MibTableRow
gx2OA100BDAnalogEntry = _Gx2OA100BDAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1)
)
gx2OA100BDAnalogEntry.setIndexNames(
    (0, "OMNI-gx2oa100bd-MIB", "gx2OA100BDAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2OA100BDAnalogEntry.setStatus("mandatory")


class _Gx2OA100BDAnalogTableIndex_Type(Integer32):
    """Custom type gx2OA100BDAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2OA100BDAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2OA100BDAnalogTableIndex_Object = MibTableColumn
gx2OA100BDAnalogTableIndex = _Gx2OA100BDAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 1),
    _Gx2OA100BDAnalogTableIndex_Type()
)
gx2OA100BDAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2OA100BDAnalogTableIndex.setStatus("mandatory")


class _Oa100bdlabelModTemp_Type(DisplayString):
    """Custom type oa100bdlabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelModTemp_Type.__name__ = "DisplayString"
_Oa100bdlabelModTemp_Object = MibTableColumn
oa100bdlabelModTemp = _Oa100bdlabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 2),
    _Oa100bdlabelModTemp_Type()
)
oa100bdlabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelModTemp.setStatus("optional")


class _Oa100bduomModTemp_Type(DisplayString):
    """Custom type oa100bduomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomModTemp_Type.__name__ = "DisplayString"
_Oa100bduomModTemp_Object = MibTableColumn
oa100bduomModTemp = _Oa100bduomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 3),
    _Oa100bduomModTemp_Type()
)
oa100bduomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomModTemp.setStatus("optional")
_Oa100bdmajorHighModTemp_Type = Float
_Oa100bdmajorHighModTemp_Object = MibTableColumn
oa100bdmajorHighModTemp = _Oa100bdmajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 4),
    _Oa100bdmajorHighModTemp_Type()
)
oa100bdmajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighModTemp.setStatus("mandatory")
_Oa100bdmajorLowModTemp_Type = Float
_Oa100bdmajorLowModTemp_Object = MibTableColumn
oa100bdmajorLowModTemp = _Oa100bdmajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 5),
    _Oa100bdmajorLowModTemp_Type()
)
oa100bdmajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowModTemp.setStatus("mandatory")
_Oa100bdminorHighModTemp_Type = Float
_Oa100bdminorHighModTemp_Object = MibTableColumn
oa100bdminorHighModTemp = _Oa100bdminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 6),
    _Oa100bdminorHighModTemp_Type()
)
oa100bdminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighModTemp.setStatus("mandatory")
_Oa100bdminorLowModTemp_Type = Float
_Oa100bdminorLowModTemp_Object = MibTableColumn
oa100bdminorLowModTemp = _Oa100bdminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 7),
    _Oa100bdminorLowModTemp_Type()
)
oa100bdminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowModTemp.setStatus("mandatory")
_Oa100bdcurrentValueModTemp_Type = Float
_Oa100bdcurrentValueModTemp_Object = MibTableColumn
oa100bdcurrentValueModTemp = _Oa100bdcurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 8),
    _Oa100bdcurrentValueModTemp_Type()
)
oa100bdcurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdcurrentValueModTemp.setStatus("mandatory")


class _Oa100bdstateFlagModTemp_Type(Integer32):
    """Custom type oa100bdstateFlagModTemp based on Integer32"""
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


_Oa100bdstateFlagModTemp_Type.__name__ = "Integer32"
_Oa100bdstateFlagModTemp_Object = MibTableColumn
oa100bdstateFlagModTemp = _Oa100bdstateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 9),
    _Oa100bdstateFlagModTemp_Type()
)
oa100bdstateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagModTemp.setStatus("mandatory")
_Oa100bdminValueModTemp_Type = Float
_Oa100bdminValueModTemp_Object = MibTableColumn
oa100bdminValueModTemp = _Oa100bdminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 10),
    _Oa100bdminValueModTemp_Type()
)
oa100bdminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueModTemp.setStatus("mandatory")
_Oa100bdmaxValueModTemp_Type = Float
_Oa100bdmaxValueModTemp_Object = MibTableColumn
oa100bdmaxValueModTemp = _Oa100bdmaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 11),
    _Oa100bdmaxValueModTemp_Type()
)
oa100bdmaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueModTemp.setStatus("mandatory")


class _Oa100bdalarmStateModTemp_Type(Integer32):
    """Custom type oa100bdalarmStateModTemp based on Integer32"""
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


_Oa100bdalarmStateModTemp_Type.__name__ = "Integer32"
_Oa100bdalarmStateModTemp_Object = MibTableColumn
oa100bdalarmStateModTemp = _Oa100bdalarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 12),
    _Oa100bdalarmStateModTemp_Type()
)
oa100bdalarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateModTemp.setStatus("mandatory")


class _Oa100bdlabelOptInPower_Type(DisplayString):
    """Custom type oa100bdlabelOptInPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelOptInPower_Type.__name__ = "DisplayString"
_Oa100bdlabelOptInPower_Object = MibTableColumn
oa100bdlabelOptInPower = _Oa100bdlabelOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 13),
    _Oa100bdlabelOptInPower_Type()
)
oa100bdlabelOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelOptInPower.setStatus("optional")


class _Oa100bduomOptInPower_Type(DisplayString):
    """Custom type oa100bduomOptInPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomOptInPower_Type.__name__ = "DisplayString"
_Oa100bduomOptInPower_Object = MibTableColumn
oa100bduomOptInPower = _Oa100bduomOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 14),
    _Oa100bduomOptInPower_Type()
)
oa100bduomOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomOptInPower.setStatus("optional")
_Oa100bdmajorHighOptInPower_Type = Float
_Oa100bdmajorHighOptInPower_Object = MibTableColumn
oa100bdmajorHighOptInPower = _Oa100bdmajorHighOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 15),
    _Oa100bdmajorHighOptInPower_Type()
)
oa100bdmajorHighOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighOptInPower.setStatus("mandatory")
_Oa100bdmajorLowOptInPower_Type = Float
_Oa100bdmajorLowOptInPower_Object = MibTableColumn
oa100bdmajorLowOptInPower = _Oa100bdmajorLowOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 16),
    _Oa100bdmajorLowOptInPower_Type()
)
oa100bdmajorLowOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowOptInPower.setStatus("mandatory")
_Oa100bdminorHighOptInPower_Type = Float
_Oa100bdminorHighOptInPower_Object = MibTableColumn
oa100bdminorHighOptInPower = _Oa100bdminorHighOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 17),
    _Oa100bdminorHighOptInPower_Type()
)
oa100bdminorHighOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighOptInPower.setStatus("mandatory")
_Oa100bdminorLowOptInPower_Type = Float
_Oa100bdminorLowOptInPower_Object = MibTableColumn
oa100bdminorLowOptInPower = _Oa100bdminorLowOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 18),
    _Oa100bdminorLowOptInPower_Type()
)
oa100bdminorLowOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowOptInPower.setStatus("mandatory")
_Oa100bdcurrentValueOptInPower_Type = Float
_Oa100bdcurrentValueOptInPower_Object = MibTableColumn
oa100bdcurrentValueOptInPower = _Oa100bdcurrentValueOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 19),
    _Oa100bdcurrentValueOptInPower_Type()
)
oa100bdcurrentValueOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdcurrentValueOptInPower.setStatus("mandatory")


class _Oa100bdstateFlagOptInPower_Type(Integer32):
    """Custom type oa100bdstateFlagOptInPower based on Integer32"""
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


_Oa100bdstateFlagOptInPower_Type.__name__ = "Integer32"
_Oa100bdstateFlagOptInPower_Object = MibTableColumn
oa100bdstateFlagOptInPower = _Oa100bdstateFlagOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 20),
    _Oa100bdstateFlagOptInPower_Type()
)
oa100bdstateFlagOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagOptInPower.setStatus("mandatory")
_Oa100bdminValueOptInPower_Type = Float
_Oa100bdminValueOptInPower_Object = MibTableColumn
oa100bdminValueOptInPower = _Oa100bdminValueOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 21),
    _Oa100bdminValueOptInPower_Type()
)
oa100bdminValueOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueOptInPower.setStatus("mandatory")
_Oa100bdmaxValueOptInPower_Type = Float
_Oa100bdmaxValueOptInPower_Object = MibTableColumn
oa100bdmaxValueOptInPower = _Oa100bdmaxValueOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 22),
    _Oa100bdmaxValueOptInPower_Type()
)
oa100bdmaxValueOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueOptInPower.setStatus("mandatory")


class _Oa100bdalarmStateOptInPower_Type(Integer32):
    """Custom type oa100bdalarmStateOptInPower based on Integer32"""
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


_Oa100bdalarmStateOptInPower_Type.__name__ = "Integer32"
_Oa100bdalarmStateOptInPower_Object = MibTableColumn
oa100bdalarmStateOptInPower = _Oa100bdalarmStateOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 23),
    _Oa100bdalarmStateOptInPower_Type()
)
oa100bdalarmStateOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateOptInPower.setStatus("mandatory")


class _Oa100bdlabelOptOutPower_Type(DisplayString):
    """Custom type oa100bdlabelOptOutPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelOptOutPower_Type.__name__ = "DisplayString"
_Oa100bdlabelOptOutPower_Object = MibTableColumn
oa100bdlabelOptOutPower = _Oa100bdlabelOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 24),
    _Oa100bdlabelOptOutPower_Type()
)
oa100bdlabelOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelOptOutPower.setStatus("optional")


class _Oa100bduomOptOutPower_Type(DisplayString):
    """Custom type oa100bduomOptOutPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomOptOutPower_Type.__name__ = "DisplayString"
_Oa100bduomOptOutPower_Object = MibTableColumn
oa100bduomOptOutPower = _Oa100bduomOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 25),
    _Oa100bduomOptOutPower_Type()
)
oa100bduomOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomOptOutPower.setStatus("optional")
_Oa100bdmajorHighOptOutPower_Type = Float
_Oa100bdmajorHighOptOutPower_Object = MibTableColumn
oa100bdmajorHighOptOutPower = _Oa100bdmajorHighOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 26),
    _Oa100bdmajorHighOptOutPower_Type()
)
oa100bdmajorHighOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighOptOutPower.setStatus("mandatory")
_Oa100bdmajorLowOptOutPower_Type = Float
_Oa100bdmajorLowOptOutPower_Object = MibTableColumn
oa100bdmajorLowOptOutPower = _Oa100bdmajorLowOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 27),
    _Oa100bdmajorLowOptOutPower_Type()
)
oa100bdmajorLowOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowOptOutPower.setStatus("mandatory")
_Oa100bdminorHighOptOutPower_Type = Float
_Oa100bdminorHighOptOutPower_Object = MibTableColumn
oa100bdminorHighOptOutPower = _Oa100bdminorHighOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 28),
    _Oa100bdminorHighOptOutPower_Type()
)
oa100bdminorHighOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighOptOutPower.setStatus("mandatory")
_Oa100bdminorLowOptOutPower_Type = Float
_Oa100bdminorLowOptOutPower_Object = MibTableColumn
oa100bdminorLowOptOutPower = _Oa100bdminorLowOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 29),
    _Oa100bdminorLowOptOutPower_Type()
)
oa100bdminorLowOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowOptOutPower.setStatus("mandatory")
_Oa100bdcurrentValueOptOutPower_Type = Float
_Oa100bdcurrentValueOptOutPower_Object = MibTableColumn
oa100bdcurrentValueOptOutPower = _Oa100bdcurrentValueOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 30),
    _Oa100bdcurrentValueOptOutPower_Type()
)
oa100bdcurrentValueOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdcurrentValueOptOutPower.setStatus("mandatory")


class _Oa100bdstateFlagOptOutPower_Type(Integer32):
    """Custom type oa100bdstateFlagOptOutPower based on Integer32"""
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


_Oa100bdstateFlagOptOutPower_Type.__name__ = "Integer32"
_Oa100bdstateFlagOptOutPower_Object = MibTableColumn
oa100bdstateFlagOptOutPower = _Oa100bdstateFlagOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 31),
    _Oa100bdstateFlagOptOutPower_Type()
)
oa100bdstateFlagOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagOptOutPower.setStatus("mandatory")
_Oa100bdminValueOptOutPower_Type = Float
_Oa100bdminValueOptOutPower_Object = MibTableColumn
oa100bdminValueOptOutPower = _Oa100bdminValueOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 32),
    _Oa100bdminValueOptOutPower_Type()
)
oa100bdminValueOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueOptOutPower.setStatus("mandatory")
_Oa100bdmaxValueOptOutPower_Type = Float
_Oa100bdmaxValueOptOutPower_Object = MibTableColumn
oa100bdmaxValueOptOutPower = _Oa100bdmaxValueOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 33),
    _Oa100bdmaxValueOptOutPower_Type()
)
oa100bdmaxValueOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueOptOutPower.setStatus("mandatory")


class _Oa100bdalarmStateOptOutPower_Type(Integer32):
    """Custom type oa100bdalarmStateOptOutPower based on Integer32"""
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


_Oa100bdalarmStateOptOutPower_Type.__name__ = "Integer32"
_Oa100bdalarmStateOptOutPower_Object = MibTableColumn
oa100bdalarmStateOptOutPower = _Oa100bdalarmStateOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 34),
    _Oa100bdalarmStateOptOutPower_Type()
)
oa100bdalarmStateOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateOptOutPower.setStatus("mandatory")


class _Oa100bdlabelMainTECTemp_Type(DisplayString):
    """Custom type oa100bdlabelMainTECTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelMainTECTemp_Type.__name__ = "DisplayString"
_Oa100bdlabelMainTECTemp_Object = MibTableColumn
oa100bdlabelMainTECTemp = _Oa100bdlabelMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 35),
    _Oa100bdlabelMainTECTemp_Type()
)
oa100bdlabelMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelMainTECTemp.setStatus("optional")


class _Oa100bduomMainTECTemp_Type(DisplayString):
    """Custom type oa100bduomMainTECTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomMainTECTemp_Type.__name__ = "DisplayString"
_Oa100bduomMainTECTemp_Object = MibTableColumn
oa100bduomMainTECTemp = _Oa100bduomMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 36),
    _Oa100bduomMainTECTemp_Type()
)
oa100bduomMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomMainTECTemp.setStatus("optional")
_Oa100bdmajorHighMainTECTemp_Type = Float
_Oa100bdmajorHighMainTECTemp_Object = MibTableColumn
oa100bdmajorHighMainTECTemp = _Oa100bdmajorHighMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 37),
    _Oa100bdmajorHighMainTECTemp_Type()
)
oa100bdmajorHighMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighMainTECTemp.setStatus("mandatory")
_Oa100bdmajorLowMainTECTemp_Type = Float
_Oa100bdmajorLowMainTECTemp_Object = MibTableColumn
oa100bdmajorLowMainTECTemp = _Oa100bdmajorLowMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 38),
    _Oa100bdmajorLowMainTECTemp_Type()
)
oa100bdmajorLowMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowMainTECTemp.setStatus("mandatory")
_Oa100bdminorHighMainTECTemp_Type = Float
_Oa100bdminorHighMainTECTemp_Object = MibTableColumn
oa100bdminorHighMainTECTemp = _Oa100bdminorHighMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 39),
    _Oa100bdminorHighMainTECTemp_Type()
)
oa100bdminorHighMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighMainTECTemp.setStatus("mandatory")
_Oa100bdminorLowMainTECTemp_Type = Float
_Oa100bdminorLowMainTECTemp_Object = MibTableColumn
oa100bdminorLowMainTECTemp = _Oa100bdminorLowMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 40),
    _Oa100bdminorLowMainTECTemp_Type()
)
oa100bdminorLowMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowMainTECTemp.setStatus("mandatory")
_Oa100bdcurrentValueMainTECTemp_Type = Float
_Oa100bdcurrentValueMainTECTemp_Object = MibTableColumn
oa100bdcurrentValueMainTECTemp = _Oa100bdcurrentValueMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 41),
    _Oa100bdcurrentValueMainTECTemp_Type()
)
oa100bdcurrentValueMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdcurrentValueMainTECTemp.setStatus("mandatory")


class _Oa100bdstateFlagMainTECTemp_Type(Integer32):
    """Custom type oa100bdstateFlagMainTECTemp based on Integer32"""
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


_Oa100bdstateFlagMainTECTemp_Type.__name__ = "Integer32"
_Oa100bdstateFlagMainTECTemp_Object = MibTableColumn
oa100bdstateFlagMainTECTemp = _Oa100bdstateFlagMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 42),
    _Oa100bdstateFlagMainTECTemp_Type()
)
oa100bdstateFlagMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagMainTECTemp.setStatus("mandatory")
_Oa100bdminValueMainTECTemp_Type = Float
_Oa100bdminValueMainTECTemp_Object = MibTableColumn
oa100bdminValueMainTECTemp = _Oa100bdminValueMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 43),
    _Oa100bdminValueMainTECTemp_Type()
)
oa100bdminValueMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueMainTECTemp.setStatus("mandatory")
_Oa100bdmaxValueMainTECTemp_Type = Float
_Oa100bdmaxValueMainTECTemp_Object = MibTableColumn
oa100bdmaxValueMainTECTemp = _Oa100bdmaxValueMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 44),
    _Oa100bdmaxValueMainTECTemp_Type()
)
oa100bdmaxValueMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueMainTECTemp.setStatus("mandatory")


class _Oa100bdalarmStateMainTECTemp_Type(Integer32):
    """Custom type oa100bdalarmStateMainTECTemp based on Integer32"""
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


_Oa100bdalarmStateMainTECTemp_Type.__name__ = "Integer32"
_Oa100bdalarmStateMainTECTemp_Object = MibTableColumn
oa100bdalarmStateMainTECTemp = _Oa100bdalarmStateMainTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 45),
    _Oa100bdalarmStateMainTECTemp_Type()
)
oa100bdalarmStateMainTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateMainTECTemp.setStatus("mandatory")


class _Oa100bdlabelMainLaserPower_Type(DisplayString):
    """Custom type oa100bdlabelMainLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelMainLaserPower_Type.__name__ = "DisplayString"
_Oa100bdlabelMainLaserPower_Object = MibTableColumn
oa100bdlabelMainLaserPower = _Oa100bdlabelMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 46),
    _Oa100bdlabelMainLaserPower_Type()
)
oa100bdlabelMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelMainLaserPower.setStatus("optional")


class _Oa100bduomMainLaserPower_Type(DisplayString):
    """Custom type oa100bduomMainLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomMainLaserPower_Type.__name__ = "DisplayString"
_Oa100bduomMainLaserPower_Object = MibTableColumn
oa100bduomMainLaserPower = _Oa100bduomMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 47),
    _Oa100bduomMainLaserPower_Type()
)
oa100bduomMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomMainLaserPower.setStatus("optional")
_Oa100bdmajorHighMainLaserPower_Type = Float
_Oa100bdmajorHighMainLaserPower_Object = MibTableColumn
oa100bdmajorHighMainLaserPower = _Oa100bdmajorHighMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 48),
    _Oa100bdmajorHighMainLaserPower_Type()
)
oa100bdmajorHighMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighMainLaserPower.setStatus("mandatory")
_Oa100bdmajorLowMainLaserPower_Type = Float
_Oa100bdmajorLowMainLaserPower_Object = MibTableColumn
oa100bdmajorLowMainLaserPower = _Oa100bdmajorLowMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 49),
    _Oa100bdmajorLowMainLaserPower_Type()
)
oa100bdmajorLowMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowMainLaserPower.setStatus("mandatory")
_Oa100bdminorHighMainLaserPower_Type = Float
_Oa100bdminorHighMainLaserPower_Object = MibTableColumn
oa100bdminorHighMainLaserPower = _Oa100bdminorHighMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 50),
    _Oa100bdminorHighMainLaserPower_Type()
)
oa100bdminorHighMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighMainLaserPower.setStatus("mandatory")
_Oa100bdminorLowMainLaserPower_Type = Float
_Oa100bdminorLowMainLaserPower_Object = MibTableColumn
oa100bdminorLowMainLaserPower = _Oa100bdminorLowMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 51),
    _Oa100bdminorLowMainLaserPower_Type()
)
oa100bdminorLowMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowMainLaserPower.setStatus("mandatory")
_Oa100bdcurrentValueMainLaserPower_Type = Float
_Oa100bdcurrentValueMainLaserPower_Object = MibTableColumn
oa100bdcurrentValueMainLaserPower = _Oa100bdcurrentValueMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 52),
    _Oa100bdcurrentValueMainLaserPower_Type()
)
oa100bdcurrentValueMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdcurrentValueMainLaserPower.setStatus("mandatory")


class _Oa100bdstateFlagMainLaserPower_Type(Integer32):
    """Custom type oa100bdstateFlagMainLaserPower based on Integer32"""
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


_Oa100bdstateFlagMainLaserPower_Type.__name__ = "Integer32"
_Oa100bdstateFlagMainLaserPower_Object = MibTableColumn
oa100bdstateFlagMainLaserPower = _Oa100bdstateFlagMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 53),
    _Oa100bdstateFlagMainLaserPower_Type()
)
oa100bdstateFlagMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagMainLaserPower.setStatus("mandatory")
_Oa100bdminValueMainLaserPower_Type = Float
_Oa100bdminValueMainLaserPower_Object = MibTableColumn
oa100bdminValueMainLaserPower = _Oa100bdminValueMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 54),
    _Oa100bdminValueMainLaserPower_Type()
)
oa100bdminValueMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueMainLaserPower.setStatus("mandatory")
_Oa100bdmaxValueMainLaserPower_Type = Float
_Oa100bdmaxValueMainLaserPower_Object = MibTableColumn
oa100bdmaxValueMainLaserPower = _Oa100bdmaxValueMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 55),
    _Oa100bdmaxValueMainLaserPower_Type()
)
oa100bdmaxValueMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueMainLaserPower.setStatus("mandatory")


class _Oa100bdalarmStateMainLaserPower_Type(Integer32):
    """Custom type oa100bdalarmStateMainLaserPower based on Integer32"""
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


_Oa100bdalarmStateMainLaserPower_Type.__name__ = "Integer32"
_Oa100bdalarmStateMainLaserPower_Object = MibTableColumn
oa100bdalarmStateMainLaserPower = _Oa100bdalarmStateMainLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 56),
    _Oa100bdalarmStateMainLaserPower_Type()
)
oa100bdalarmStateMainLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateMainLaserPower.setStatus("mandatory")


class _Oa100bdlabelAuxTECTemp_Type(DisplayString):
    """Custom type oa100bdlabelAuxTECTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelAuxTECTemp_Type.__name__ = "DisplayString"
_Oa100bdlabelAuxTECTemp_Object = MibTableColumn
oa100bdlabelAuxTECTemp = _Oa100bdlabelAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 57),
    _Oa100bdlabelAuxTECTemp_Type()
)
oa100bdlabelAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelAuxTECTemp.setStatus("optional")


class _Oa100bduomAuxTECTemp_Type(DisplayString):
    """Custom type oa100bduomAuxTECTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomAuxTECTemp_Type.__name__ = "DisplayString"
_Oa100bduomAuxTECTemp_Object = MibTableColumn
oa100bduomAuxTECTemp = _Oa100bduomAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 58),
    _Oa100bduomAuxTECTemp_Type()
)
oa100bduomAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomAuxTECTemp.setStatus("optional")
_Oa100bdmajorHighAuxTECTemp_Type = Float
_Oa100bdmajorHighAuxTECTemp_Object = MibTableColumn
oa100bdmajorHighAuxTECTemp = _Oa100bdmajorHighAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 59),
    _Oa100bdmajorHighAuxTECTemp_Type()
)
oa100bdmajorHighAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighAuxTECTemp.setStatus("mandatory")
_Oa100bdmajorLowAuxTECTemp_Type = Float
_Oa100bdmajorLowAuxTECTemp_Object = MibTableColumn
oa100bdmajorLowAuxTECTemp = _Oa100bdmajorLowAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 60),
    _Oa100bdmajorLowAuxTECTemp_Type()
)
oa100bdmajorLowAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowAuxTECTemp.setStatus("mandatory")
_Oa100bdminorHighAuxTECTemp_Type = Float
_Oa100bdminorHighAuxTECTemp_Object = MibTableColumn
oa100bdminorHighAuxTECTemp = _Oa100bdminorHighAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 61),
    _Oa100bdminorHighAuxTECTemp_Type()
)
oa100bdminorHighAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighAuxTECTemp.setStatus("mandatory")
_Oa100bdminorLowAuxTECTemp_Type = Float
_Oa100bdminorLowAuxTECTemp_Object = MibTableColumn
oa100bdminorLowAuxTECTemp = _Oa100bdminorLowAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 62),
    _Oa100bdminorLowAuxTECTemp_Type()
)
oa100bdminorLowAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowAuxTECTemp.setStatus("mandatory")
_Oa100bdcurrentValueAuxTECTemp_Type = Float
_Oa100bdcurrentValueAuxTECTemp_Object = MibTableColumn
oa100bdcurrentValueAuxTECTemp = _Oa100bdcurrentValueAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 63),
    _Oa100bdcurrentValueAuxTECTemp_Type()
)
oa100bdcurrentValueAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdcurrentValueAuxTECTemp.setStatus("mandatory")


class _Oa100bdstateFlagAuxTECTemp_Type(Integer32):
    """Custom type oa100bdstateFlagAuxTECTemp based on Integer32"""
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


_Oa100bdstateFlagAuxTECTemp_Type.__name__ = "Integer32"
_Oa100bdstateFlagAuxTECTemp_Object = MibTableColumn
oa100bdstateFlagAuxTECTemp = _Oa100bdstateFlagAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 64),
    _Oa100bdstateFlagAuxTECTemp_Type()
)
oa100bdstateFlagAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagAuxTECTemp.setStatus("mandatory")
_Oa100bdminValueAuxTECTemp_Type = Float
_Oa100bdminValueAuxTECTemp_Object = MibTableColumn
oa100bdminValueAuxTECTemp = _Oa100bdminValueAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 65),
    _Oa100bdminValueAuxTECTemp_Type()
)
oa100bdminValueAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueAuxTECTemp.setStatus("mandatory")
_Oa100bdmaxValueAuxTECTemp_Type = Float
_Oa100bdmaxValueAuxTECTemp_Object = MibTableColumn
oa100bdmaxValueAuxTECTemp = _Oa100bdmaxValueAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 66),
    _Oa100bdmaxValueAuxTECTemp_Type()
)
oa100bdmaxValueAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueAuxTECTemp.setStatus("mandatory")


class _Oa100bdalarmStateAuxTECTemp_Type(Integer32):
    """Custom type oa100bdalarmStateAuxTECTemp based on Integer32"""
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


_Oa100bdalarmStateAuxTECTemp_Type.__name__ = "Integer32"
_Oa100bdalarmStateAuxTECTemp_Object = MibTableColumn
oa100bdalarmStateAuxTECTemp = _Oa100bdalarmStateAuxTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 67),
    _Oa100bdalarmStateAuxTECTemp_Type()
)
oa100bdalarmStateAuxTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateAuxTECTemp.setStatus("mandatory")


class _Oa100bdlabelAuxLaserPower_Type(DisplayString):
    """Custom type oa100bdlabelAuxLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelAuxLaserPower_Type.__name__ = "DisplayString"
_Oa100bdlabelAuxLaserPower_Object = MibTableColumn
oa100bdlabelAuxLaserPower = _Oa100bdlabelAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 68),
    _Oa100bdlabelAuxLaserPower_Type()
)
oa100bdlabelAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelAuxLaserPower.setStatus("optional")


class _Oa100bduomAuxLaserPower_Type(DisplayString):
    """Custom type oa100bduomAuxLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomAuxLaserPower_Type.__name__ = "DisplayString"
_Oa100bduomAuxLaserPower_Object = MibTableColumn
oa100bduomAuxLaserPower = _Oa100bduomAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 69),
    _Oa100bduomAuxLaserPower_Type()
)
oa100bduomAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomAuxLaserPower.setStatus("optional")
_Oa100bdmajorHighAuxLaserPower_Type = Float
_Oa100bdmajorHighAuxLaserPower_Object = MibTableColumn
oa100bdmajorHighAuxLaserPower = _Oa100bdmajorHighAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 70),
    _Oa100bdmajorHighAuxLaserPower_Type()
)
oa100bdmajorHighAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighAuxLaserPower.setStatus("mandatory")
_Oa100bdmajorLowAuxLaserPower_Type = Float
_Oa100bdmajorLowAuxLaserPower_Object = MibTableColumn
oa100bdmajorLowAuxLaserPower = _Oa100bdmajorLowAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 71),
    _Oa100bdmajorLowAuxLaserPower_Type()
)
oa100bdmajorLowAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowAuxLaserPower.setStatus("mandatory")
_Oa100bdminorHighAuxLaserPower_Type = Float
_Oa100bdminorHighAuxLaserPower_Object = MibTableColumn
oa100bdminorHighAuxLaserPower = _Oa100bdminorHighAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 72),
    _Oa100bdminorHighAuxLaserPower_Type()
)
oa100bdminorHighAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighAuxLaserPower.setStatus("mandatory")
_Oa100bdminorLowAuxLaserPower_Type = Float
_Oa100bdminorLowAuxLaserPower_Object = MibTableColumn
oa100bdminorLowAuxLaserPower = _Oa100bdminorLowAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 73),
    _Oa100bdminorLowAuxLaserPower_Type()
)
oa100bdminorLowAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowAuxLaserPower.setStatus("mandatory")
_Oa100bdcurrentValueAuxLaserPower_Type = Float
_Oa100bdcurrentValueAuxLaserPower_Object = MibTableColumn
oa100bdcurrentValueAuxLaserPower = _Oa100bdcurrentValueAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 74),
    _Oa100bdcurrentValueAuxLaserPower_Type()
)
oa100bdcurrentValueAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdcurrentValueAuxLaserPower.setStatus("mandatory")


class _Oa100bdstateFlagAuxLaserPower_Type(Integer32):
    """Custom type oa100bdstateFlagAuxLaserPower based on Integer32"""
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


_Oa100bdstateFlagAuxLaserPower_Type.__name__ = "Integer32"
_Oa100bdstateFlagAuxLaserPower_Object = MibTableColumn
oa100bdstateFlagAuxLaserPower = _Oa100bdstateFlagAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 75),
    _Oa100bdstateFlagAuxLaserPower_Type()
)
oa100bdstateFlagAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagAuxLaserPower.setStatus("mandatory")
_Oa100bdminValueAuxLaserPower_Type = Float
_Oa100bdminValueAuxLaserPower_Object = MibTableColumn
oa100bdminValueAuxLaserPower = _Oa100bdminValueAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 76),
    _Oa100bdminValueAuxLaserPower_Type()
)
oa100bdminValueAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueAuxLaserPower.setStatus("mandatory")
_Oa100bdmaxValueAuxLaserPower_Type = Float
_Oa100bdmaxValueAuxLaserPower_Object = MibTableColumn
oa100bdmaxValueAuxLaserPower = _Oa100bdmaxValueAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 77),
    _Oa100bdmaxValueAuxLaserPower_Type()
)
oa100bdmaxValueAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueAuxLaserPower.setStatus("mandatory")


class _Oa100bdalarmStateAuxLaserPower_Type(Integer32):
    """Custom type oa100bdalarmStateAuxLaserPower based on Integer32"""
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


_Oa100bdalarmStateAuxLaserPower_Type.__name__ = "Integer32"
_Oa100bdalarmStateAuxLaserPower_Object = MibTableColumn
oa100bdalarmStateAuxLaserPower = _Oa100bdalarmStateAuxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 78),
    _Oa100bdalarmStateAuxLaserPower_Type()
)
oa100bdalarmStateAuxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateAuxLaserPower.setStatus("mandatory")


class _Oa100bdlabelFanCurrent_Type(DisplayString):
    """Custom type oa100bdlabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelFanCurrent_Type.__name__ = "DisplayString"
_Oa100bdlabelFanCurrent_Object = MibTableColumn
oa100bdlabelFanCurrent = _Oa100bdlabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 79),
    _Oa100bdlabelFanCurrent_Type()
)
oa100bdlabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelFanCurrent.setStatus("optional")


class _Oa100bduomFanCurrent_Type(DisplayString):
    """Custom type oa100bduomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomFanCurrent_Type.__name__ = "DisplayString"
_Oa100bduomFanCurrent_Object = MibTableColumn
oa100bduomFanCurrent = _Oa100bduomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 80),
    _Oa100bduomFanCurrent_Type()
)
oa100bduomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomFanCurrent.setStatus("optional")
_Oa100bdmajorHighFanCurrent_Type = Float
_Oa100bdmajorHighFanCurrent_Object = MibTableColumn
oa100bdmajorHighFanCurrent = _Oa100bdmajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 81),
    _Oa100bdmajorHighFanCurrent_Type()
)
oa100bdmajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighFanCurrent.setStatus("mandatory")
_Oa100bdmajorLowFanCurrent_Type = Float
_Oa100bdmajorLowFanCurrent_Object = MibTableColumn
oa100bdmajorLowFanCurrent = _Oa100bdmajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 82),
    _Oa100bdmajorLowFanCurrent_Type()
)
oa100bdmajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowFanCurrent.setStatus("mandatory")
_Oa100bdminorHighFanCurrent_Type = Float
_Oa100bdminorHighFanCurrent_Object = MibTableColumn
oa100bdminorHighFanCurrent = _Oa100bdminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 83),
    _Oa100bdminorHighFanCurrent_Type()
)
oa100bdminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighFanCurrent.setStatus("mandatory")
_Oa100bdminorLowFanCurrent_Type = Float
_Oa100bdminorLowFanCurrent_Object = MibTableColumn
oa100bdminorLowFanCurrent = _Oa100bdminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 84),
    _Oa100bdminorLowFanCurrent_Type()
)
oa100bdminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowFanCurrent.setStatus("mandatory")
_Oa100bdcurrentValueFanCurrent_Type = Float
_Oa100bdcurrentValueFanCurrent_Object = MibTableColumn
oa100bdcurrentValueFanCurrent = _Oa100bdcurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 85),
    _Oa100bdcurrentValueFanCurrent_Type()
)
oa100bdcurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdcurrentValueFanCurrent.setStatus("mandatory")


class _Oa100bdstateFlagFanCurrent_Type(Integer32):
    """Custom type oa100bdstateFlagFanCurrent based on Integer32"""
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


_Oa100bdstateFlagFanCurrent_Type.__name__ = "Integer32"
_Oa100bdstateFlagFanCurrent_Object = MibTableColumn
oa100bdstateFlagFanCurrent = _Oa100bdstateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 86),
    _Oa100bdstateFlagFanCurrent_Type()
)
oa100bdstateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagFanCurrent.setStatus("mandatory")
_Oa100bdminValueFanCurrent_Type = Float
_Oa100bdminValueFanCurrent_Object = MibTableColumn
oa100bdminValueFanCurrent = _Oa100bdminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 87),
    _Oa100bdminValueFanCurrent_Type()
)
oa100bdminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueFanCurrent.setStatus("mandatory")
_Oa100bdmaxValueFanCurrent_Type = Float
_Oa100bdmaxValueFanCurrent_Object = MibTableColumn
oa100bdmaxValueFanCurrent = _Oa100bdmaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 88),
    _Oa100bdmaxValueFanCurrent_Type()
)
oa100bdmaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueFanCurrent.setStatus("mandatory")


class _Oa100bdalarmStateFanCurrent_Type(Integer32):
    """Custom type oa100bdalarmStateFanCurrent based on Integer32"""
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


_Oa100bdalarmStateFanCurrent_Type.__name__ = "Integer32"
_Oa100bdalarmStateFanCurrent_Object = MibTableColumn
oa100bdalarmStateFanCurrent = _Oa100bdalarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 89),
    _Oa100bdalarmStateFanCurrent_Type()
)
oa100bdalarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateFanCurrent.setStatus("mandatory")


class _Oa100bdlabelOPSetting_Type(DisplayString):
    """Custom type oa100bdlabelOPSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelOPSetting_Type.__name__ = "DisplayString"
_Oa100bdlabelOPSetting_Object = MibTableColumn
oa100bdlabelOPSetting = _Oa100bdlabelOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 90),
    _Oa100bdlabelOPSetting_Type()
)
oa100bdlabelOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelOPSetting.setStatus("optional")


class _Oa100bduomOPSetting_Type(DisplayString):
    """Custom type oa100bduomOPSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomOPSetting_Type.__name__ = "DisplayString"
_Oa100bduomOPSetting_Object = MibTableColumn
oa100bduomOPSetting = _Oa100bduomOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 91),
    _Oa100bduomOPSetting_Type()
)
oa100bduomOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomOPSetting.setStatus("optional")
_Oa100bdmajorHighOPSetting_Type = Float
_Oa100bdmajorHighOPSetting_Object = MibTableColumn
oa100bdmajorHighOPSetting = _Oa100bdmajorHighOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 92),
    _Oa100bdmajorHighOPSetting_Type()
)
oa100bdmajorHighOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighOPSetting.setStatus("mandatory")
_Oa100bdmajorLowOPSetting_Type = Float
_Oa100bdmajorLowOPSetting_Object = MibTableColumn
oa100bdmajorLowOPSetting = _Oa100bdmajorLowOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 93),
    _Oa100bdmajorLowOPSetting_Type()
)
oa100bdmajorLowOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowOPSetting.setStatus("mandatory")
_Oa100bdminorHighOPSetting_Type = Float
_Oa100bdminorHighOPSetting_Object = MibTableColumn
oa100bdminorHighOPSetting = _Oa100bdminorHighOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 94),
    _Oa100bdminorHighOPSetting_Type()
)
oa100bdminorHighOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighOPSetting.setStatus("mandatory")
_Oa100bdminorLowOPSetting_Type = Float
_Oa100bdminorLowOPSetting_Object = MibTableColumn
oa100bdminorLowOPSetting = _Oa100bdminorLowOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 95),
    _Oa100bdminorLowOPSetting_Type()
)
oa100bdminorLowOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowOPSetting.setStatus("mandatory")
_Oa100bdcurrentValueOPSetting_Type = Float
_Oa100bdcurrentValueOPSetting_Object = MibTableColumn
oa100bdcurrentValueOPSetting = _Oa100bdcurrentValueOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 96),
    _Oa100bdcurrentValueOPSetting_Type()
)
oa100bdcurrentValueOPSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oa100bdcurrentValueOPSetting.setStatus("mandatory")


class _Oa100bdstateFlagOPSetting_Type(Integer32):
    """Custom type oa100bdstateFlagOPSetting based on Integer32"""
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


_Oa100bdstateFlagOPSetting_Type.__name__ = "Integer32"
_Oa100bdstateFlagOPSetting_Object = MibTableColumn
oa100bdstateFlagOPSetting = _Oa100bdstateFlagOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 97),
    _Oa100bdstateFlagOPSetting_Type()
)
oa100bdstateFlagOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagOPSetting.setStatus("mandatory")
_Oa100bdminValueOPSetting_Type = Float
_Oa100bdminValueOPSetting_Object = MibTableColumn
oa100bdminValueOPSetting = _Oa100bdminValueOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 98),
    _Oa100bdminValueOPSetting_Type()
)
oa100bdminValueOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueOPSetting.setStatus("mandatory")
_Oa100bdmaxValueOPSetting_Type = Float
_Oa100bdmaxValueOPSetting_Object = MibTableColumn
oa100bdmaxValueOPSetting = _Oa100bdmaxValueOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 99),
    _Oa100bdmaxValueOPSetting_Type()
)
oa100bdmaxValueOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueOPSetting.setStatus("mandatory")


class _Oa100bdalarmStateOPSetting_Type(Integer32):
    """Custom type oa100bdalarmStateOPSetting based on Integer32"""
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


_Oa100bdalarmStateOPSetting_Type.__name__ = "Integer32"
_Oa100bdalarmStateOPSetting_Object = MibTableColumn
oa100bdalarmStateOPSetting = _Oa100bdalarmStateOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 100),
    _Oa100bdalarmStateOPSetting_Type()
)
oa100bdalarmStateOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateOPSetting.setStatus("mandatory")


class _Oa100bdlabelLPSetting_Type(DisplayString):
    """Custom type oa100bdlabelLPSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelLPSetting_Type.__name__ = "DisplayString"
_Oa100bdlabelLPSetting_Object = MibTableColumn
oa100bdlabelLPSetting = _Oa100bdlabelLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 101),
    _Oa100bdlabelLPSetting_Type()
)
oa100bdlabelLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelLPSetting.setStatus("optional")


class _Oa100bduomLPSetting_Type(DisplayString):
    """Custom type oa100bduomLPSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomLPSetting_Type.__name__ = "DisplayString"
_Oa100bduomLPSetting_Object = MibTableColumn
oa100bduomLPSetting = _Oa100bduomLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 102),
    _Oa100bduomLPSetting_Type()
)
oa100bduomLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomLPSetting.setStatus("optional")
_Oa100bdmajorHighLPSetting_Type = Float
_Oa100bdmajorHighLPSetting_Object = MibTableColumn
oa100bdmajorHighLPSetting = _Oa100bdmajorHighLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 103),
    _Oa100bdmajorHighLPSetting_Type()
)
oa100bdmajorHighLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighLPSetting.setStatus("mandatory")
_Oa100bdmajorLowLPSetting_Type = Float
_Oa100bdmajorLowLPSetting_Object = MibTableColumn
oa100bdmajorLowLPSetting = _Oa100bdmajorLowLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 104),
    _Oa100bdmajorLowLPSetting_Type()
)
oa100bdmajorLowLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowLPSetting.setStatus("mandatory")
_Oa100bdminorHighLPSetting_Type = Float
_Oa100bdminorHighLPSetting_Object = MibTableColumn
oa100bdminorHighLPSetting = _Oa100bdminorHighLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 105),
    _Oa100bdminorHighLPSetting_Type()
)
oa100bdminorHighLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighLPSetting.setStatus("mandatory")
_Oa100bdminorLowLPSetting_Type = Float
_Oa100bdminorLowLPSetting_Object = MibTableColumn
oa100bdminorLowLPSetting = _Oa100bdminorLowLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 106),
    _Oa100bdminorLowLPSetting_Type()
)
oa100bdminorLowLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowLPSetting.setStatus("mandatory")
_Oa100bdcurrentValueLPSetting_Type = Float
_Oa100bdcurrentValueLPSetting_Object = MibTableColumn
oa100bdcurrentValueLPSetting = _Oa100bdcurrentValueLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 107),
    _Oa100bdcurrentValueLPSetting_Type()
)
oa100bdcurrentValueLPSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oa100bdcurrentValueLPSetting.setStatus("mandatory")


class _Oa100bdstateFlagLPSetting_Type(Integer32):
    """Custom type oa100bdstateFlagLPSetting based on Integer32"""
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


_Oa100bdstateFlagLPSetting_Type.__name__ = "Integer32"
_Oa100bdstateFlagLPSetting_Object = MibTableColumn
oa100bdstateFlagLPSetting = _Oa100bdstateFlagLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 108),
    _Oa100bdstateFlagLPSetting_Type()
)
oa100bdstateFlagLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagLPSetting.setStatus("mandatory")
_Oa100bdminValueLPSetting_Type = Float
_Oa100bdminValueLPSetting_Object = MibTableColumn
oa100bdminValueLPSetting = _Oa100bdminValueLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 109),
    _Oa100bdminValueLPSetting_Type()
)
oa100bdminValueLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueLPSetting.setStatus("mandatory")
_Oa100bdmaxValueLPSetting_Type = Float
_Oa100bdmaxValueLPSetting_Object = MibTableColumn
oa100bdmaxValueLPSetting = _Oa100bdmaxValueLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 110),
    _Oa100bdmaxValueLPSetting_Type()
)
oa100bdmaxValueLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueLPSetting.setStatus("mandatory")


class _Oa100bdalarmStateLPSetting_Type(Integer32):
    """Custom type oa100bdalarmStateLPSetting based on Integer32"""
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


_Oa100bdalarmStateLPSetting_Type.__name__ = "Integer32"
_Oa100bdalarmStateLPSetting_Object = MibTableColumn
oa100bdalarmStateLPSetting = _Oa100bdalarmStateLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 111),
    _Oa100bdalarmStateLPSetting_Type()
)
oa100bdalarmStateLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateLPSetting.setStatus("mandatory")


class _Oa100bdlabelCGSetting_Type(DisplayString):
    """Custom type oa100bdlabelCGSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelCGSetting_Type.__name__ = "DisplayString"
_Oa100bdlabelCGSetting_Object = MibTableColumn
oa100bdlabelCGSetting = _Oa100bdlabelCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 112),
    _Oa100bdlabelCGSetting_Type()
)
oa100bdlabelCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelCGSetting.setStatus("optional")


class _Oa100bduomCGSetting_Type(DisplayString):
    """Custom type oa100bduomCGSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomCGSetting_Type.__name__ = "DisplayString"
_Oa100bduomCGSetting_Object = MibTableColumn
oa100bduomCGSetting = _Oa100bduomCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 113),
    _Oa100bduomCGSetting_Type()
)
oa100bduomCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomCGSetting.setStatus("optional")
_Oa100bdmajorHighCGSetting_Type = Float
_Oa100bdmajorHighCGSetting_Object = MibTableColumn
oa100bdmajorHighCGSetting = _Oa100bdmajorHighCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 114),
    _Oa100bdmajorHighCGSetting_Type()
)
oa100bdmajorHighCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighCGSetting.setStatus("mandatory")
_Oa100bdmajorLowCGSetting_Type = Float
_Oa100bdmajorLowCGSetting_Object = MibTableColumn
oa100bdmajorLowCGSetting = _Oa100bdmajorLowCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 115),
    _Oa100bdmajorLowCGSetting_Type()
)
oa100bdmajorLowCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowCGSetting.setStatus("mandatory")
_Oa100bdminorHighCGSetting_Type = Float
_Oa100bdminorHighCGSetting_Object = MibTableColumn
oa100bdminorHighCGSetting = _Oa100bdminorHighCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 116),
    _Oa100bdminorHighCGSetting_Type()
)
oa100bdminorHighCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighCGSetting.setStatus("mandatory")
_Oa100bdminorLowCGSetting_Type = Float
_Oa100bdminorLowCGSetting_Object = MibTableColumn
oa100bdminorLowCGSetting = _Oa100bdminorLowCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 117),
    _Oa100bdminorLowCGSetting_Type()
)
oa100bdminorLowCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowCGSetting.setStatus("mandatory")
_Oa100bdcurrentValueCGSetting_Type = Float
_Oa100bdcurrentValueCGSetting_Object = MibTableColumn
oa100bdcurrentValueCGSetting = _Oa100bdcurrentValueCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 118),
    _Oa100bdcurrentValueCGSetting_Type()
)
oa100bdcurrentValueCGSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oa100bdcurrentValueCGSetting.setStatus("mandatory")


class _Oa100bdstateFlagCGSetting_Type(Integer32):
    """Custom type oa100bdstateFlagCGSetting based on Integer32"""
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


_Oa100bdstateFlagCGSetting_Type.__name__ = "Integer32"
_Oa100bdstateFlagCGSetting_Object = MibTableColumn
oa100bdstateFlagCGSetting = _Oa100bdstateFlagCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 119),
    _Oa100bdstateFlagCGSetting_Type()
)
oa100bdstateFlagCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagCGSetting.setStatus("mandatory")
_Oa100bdminValueCGSetting_Type = Float
_Oa100bdminValueCGSetting_Object = MibTableColumn
oa100bdminValueCGSetting = _Oa100bdminValueCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 120),
    _Oa100bdminValueCGSetting_Type()
)
oa100bdminValueCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueCGSetting.setStatus("mandatory")
_Oa100bdmaxValueCGSetting_Type = Float
_Oa100bdmaxValueCGSetting_Object = MibTableColumn
oa100bdmaxValueCGSetting = _Oa100bdmaxValueCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 121),
    _Oa100bdmaxValueCGSetting_Type()
)
oa100bdmaxValueCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueCGSetting.setStatus("mandatory")


class _Oa100bdalarmStateCGSetting_Type(Integer32):
    """Custom type oa100bdalarmStateCGSetting based on Integer32"""
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


_Oa100bdalarmStateCGSetting_Type.__name__ = "Integer32"
_Oa100bdalarmStateCGSetting_Object = MibTableColumn
oa100bdalarmStateCGSetting = _Oa100bdalarmStateCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 122),
    _Oa100bdalarmStateCGSetting_Type()
)
oa100bdalarmStateCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateCGSetting.setStatus("mandatory")


class _Oa100bdlabelOptThreshold_Type(DisplayString):
    """Custom type oa100bdlabelOptThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelOptThreshold_Type.__name__ = "DisplayString"
_Oa100bdlabelOptThreshold_Object = MibTableColumn
oa100bdlabelOptThreshold = _Oa100bdlabelOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 123),
    _Oa100bdlabelOptThreshold_Type()
)
oa100bdlabelOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelOptThreshold.setStatus("optional")


class _Oa100bduomOptThreshold_Type(DisplayString):
    """Custom type oa100bduomOptThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bduomOptThreshold_Type.__name__ = "DisplayString"
_Oa100bduomOptThreshold_Object = MibTableColumn
oa100bduomOptThreshold = _Oa100bduomOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 124),
    _Oa100bduomOptThreshold_Type()
)
oa100bduomOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bduomOptThreshold.setStatus("optional")
_Oa100bdmajorHighOptThreshold_Type = Float
_Oa100bdmajorHighOptThreshold_Object = MibTableColumn
oa100bdmajorHighOptThreshold = _Oa100bdmajorHighOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 125),
    _Oa100bdmajorHighOptThreshold_Type()
)
oa100bdmajorHighOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorHighOptThreshold.setStatus("mandatory")
_Oa100bdmajorLowOptThreshold_Type = Float
_Oa100bdmajorLowOptThreshold_Object = MibTableColumn
oa100bdmajorLowOptThreshold = _Oa100bdmajorLowOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 126),
    _Oa100bdmajorLowOptThreshold_Type()
)
oa100bdmajorLowOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmajorLowOptThreshold.setStatus("mandatory")
_Oa100bdminorHighOptThreshold_Type = Float
_Oa100bdminorHighOptThreshold_Object = MibTableColumn
oa100bdminorHighOptThreshold = _Oa100bdminorHighOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 127),
    _Oa100bdminorHighOptThreshold_Type()
)
oa100bdminorHighOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorHighOptThreshold.setStatus("mandatory")
_Oa100bdminorLowOptThreshold_Type = Float
_Oa100bdminorLowOptThreshold_Object = MibTableColumn
oa100bdminorLowOptThreshold = _Oa100bdminorLowOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 128),
    _Oa100bdminorLowOptThreshold_Type()
)
oa100bdminorLowOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminorLowOptThreshold.setStatus("mandatory")
_Oa100bdcurrentValueOptThreshold_Type = Float
_Oa100bdcurrentValueOptThreshold_Object = MibTableColumn
oa100bdcurrentValueOptThreshold = _Oa100bdcurrentValueOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 129),
    _Oa100bdcurrentValueOptThreshold_Type()
)
oa100bdcurrentValueOptThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oa100bdcurrentValueOptThreshold.setStatus("mandatory")


class _Oa100bdstateFlagOptThreshold_Type(Integer32):
    """Custom type oa100bdstateFlagOptThreshold based on Integer32"""
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


_Oa100bdstateFlagOptThreshold_Type.__name__ = "Integer32"
_Oa100bdstateFlagOptThreshold_Object = MibTableColumn
oa100bdstateFlagOptThreshold = _Oa100bdstateFlagOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 130),
    _Oa100bdstateFlagOptThreshold_Type()
)
oa100bdstateFlagOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagOptThreshold.setStatus("mandatory")
_Oa100bdminValueOptThreshold_Type = Float
_Oa100bdminValueOptThreshold_Object = MibTableColumn
oa100bdminValueOptThreshold = _Oa100bdminValueOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 131),
    _Oa100bdminValueOptThreshold_Type()
)
oa100bdminValueOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdminValueOptThreshold.setStatus("mandatory")
_Oa100bdmaxValueOptThreshold_Type = Float
_Oa100bdmaxValueOptThreshold_Object = MibTableColumn
oa100bdmaxValueOptThreshold = _Oa100bdmaxValueOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 132),
    _Oa100bdmaxValueOptThreshold_Type()
)
oa100bdmaxValueOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdmaxValueOptThreshold.setStatus("mandatory")


class _Oa100bdalarmStateOptThreshold_Type(Integer32):
    """Custom type oa100bdalarmStateOptThreshold based on Integer32"""
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


_Oa100bdalarmStateOptThreshold_Type.__name__ = "Integer32"
_Oa100bdalarmStateOptThreshold_Object = MibTableColumn
oa100bdalarmStateOptThreshold = _Oa100bdalarmStateOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 2, 1, 133),
    _Oa100bdalarmStateOptThreshold_Type()
)
oa100bdalarmStateOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdalarmStateOptThreshold.setStatus("mandatory")
_Gx2OA100BDDigitalTable_Object = MibTable
gx2OA100BDDigitalTable = _Gx2OA100BDDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3)
)
if mibBuilder.loadTexts:
    gx2OA100BDDigitalTable.setStatus("mandatory")
_Gx2OA100BDDigitalEntry_Object = MibTableRow
gx2OA100BDDigitalEntry = _Gx2OA100BDDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2)
)
gx2OA100BDDigitalEntry.setIndexNames(
    (0, "OMNI-gx2oa100bd-MIB", "gx2OA100BDDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2OA100BDDigitalEntry.setStatus("mandatory")


class _Gx2OA100BDDigitalTableIndex_Type(Integer32):
    """Custom type gx2OA100BDDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2OA100BDDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2OA100BDDigitalTableIndex_Object = MibTableColumn
gx2OA100BDDigitalTableIndex = _Gx2OA100BDDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 1),
    _Gx2OA100BDDigitalTableIndex_Type()
)
gx2OA100BDDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2OA100BDDigitalTableIndex.setStatus("mandatory")


class _Oa100bdlabelModeSetting_Type(DisplayString):
    """Custom type oa100bdlabelModeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelModeSetting_Type.__name__ = "DisplayString"
_Oa100bdlabelModeSetting_Object = MibTableColumn
oa100bdlabelModeSetting = _Oa100bdlabelModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 2),
    _Oa100bdlabelModeSetting_Type()
)
oa100bdlabelModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelModeSetting.setStatus("optional")


class _Oa100bdenumModeSetting_Type(DisplayString):
    """Custom type oa100bdenumModeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdenumModeSetting_Type.__name__ = "DisplayString"
_Oa100bdenumModeSetting_Object = MibTableColumn
oa100bdenumModeSetting = _Oa100bdenumModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 3),
    _Oa100bdenumModeSetting_Type()
)
oa100bdenumModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdenumModeSetting.setStatus("optional")


class _Oa100bdvalueModeSetting_Type(Integer32):
    """Custom type oa100bdvalueModeSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("constant-gain-preset", 5),
          ("constant-gain-set", 6),
          ("invalid-mode", 7),
          ("laser-power-preset", 3),
          ("laser-power-set", 4),
          ("power-out-preset", 1),
          ("power-out-set", 2))
    )


_Oa100bdvalueModeSetting_Type.__name__ = "Integer32"
_Oa100bdvalueModeSetting_Object = MibTableColumn
oa100bdvalueModeSetting = _Oa100bdvalueModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 4),
    _Oa100bdvalueModeSetting_Type()
)
oa100bdvalueModeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oa100bdvalueModeSetting.setStatus("mandatory")


class _Oa100bdstateFlagModeSetting_Type(Integer32):
    """Custom type oa100bdstateFlagModeSetting based on Integer32"""
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


_Oa100bdstateFlagModeSetting_Type.__name__ = "Integer32"
_Oa100bdstateFlagModeSetting_Object = MibTableColumn
oa100bdstateFlagModeSetting = _Oa100bdstateFlagModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 5),
    _Oa100bdstateFlagModeSetting_Type()
)
oa100bdstateFlagModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagModeSetting.setStatus("mandatory")


class _Oa100bdlabelModuleState_Type(DisplayString):
    """Custom type oa100bdlabelModuleState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelModuleState_Type.__name__ = "DisplayString"
_Oa100bdlabelModuleState_Object = MibTableColumn
oa100bdlabelModuleState = _Oa100bdlabelModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 6),
    _Oa100bdlabelModuleState_Type()
)
oa100bdlabelModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelModuleState.setStatus("optional")


class _Oa100bdenumModuleState_Type(DisplayString):
    """Custom type oa100bdenumModuleState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdenumModuleState_Type.__name__ = "DisplayString"
_Oa100bdenumModuleState_Object = MibTableColumn
oa100bdenumModuleState = _Oa100bdenumModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 7),
    _Oa100bdenumModuleState_Type()
)
oa100bdenumModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdenumModuleState.setStatus("optional")


class _Oa100bdvalueModuleState_Type(Integer32):
    """Custom type oa100bdvalueModuleState based on Integer32"""
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


_Oa100bdvalueModuleState_Type.__name__ = "Integer32"
_Oa100bdvalueModuleState_Object = MibTableColumn
oa100bdvalueModuleState = _Oa100bdvalueModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 8),
    _Oa100bdvalueModuleState_Type()
)
oa100bdvalueModuleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oa100bdvalueModuleState.setStatus("mandatory")


class _Oa100bdstateFlagModuleState_Type(Integer32):
    """Custom type oa100bdstateFlagModuleState based on Integer32"""
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


_Oa100bdstateFlagModuleState_Type.__name__ = "Integer32"
_Oa100bdstateFlagModuleState_Object = MibTableColumn
oa100bdstateFlagModuleState = _Oa100bdstateFlagModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 9),
    _Oa100bdstateFlagModuleState_Type()
)
oa100bdstateFlagModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagModuleState.setStatus("mandatory")


class _Oa100bdlabelFactoryDefault_Type(DisplayString):
    """Custom type oa100bdlabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelFactoryDefault_Type.__name__ = "DisplayString"
_Oa100bdlabelFactoryDefault_Object = MibTableColumn
oa100bdlabelFactoryDefault = _Oa100bdlabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 10),
    _Oa100bdlabelFactoryDefault_Type()
)
oa100bdlabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelFactoryDefault.setStatus("optional")


class _Oa100bdenumFactoryDefault_Type(DisplayString):
    """Custom type oa100bdenumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdenumFactoryDefault_Type.__name__ = "DisplayString"
_Oa100bdenumFactoryDefault_Object = MibTableColumn
oa100bdenumFactoryDefault = _Oa100bdenumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 11),
    _Oa100bdenumFactoryDefault_Type()
)
oa100bdenumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdenumFactoryDefault.setStatus("optional")


class _Oa100bdvalueFactoryDefault_Type(Integer32):
    """Custom type oa100bdvalueFactoryDefault based on Integer32"""
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


_Oa100bdvalueFactoryDefault_Type.__name__ = "Integer32"
_Oa100bdvalueFactoryDefault_Object = MibTableColumn
oa100bdvalueFactoryDefault = _Oa100bdvalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 12),
    _Oa100bdvalueFactoryDefault_Type()
)
oa100bdvalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oa100bdvalueFactoryDefault.setStatus("mandatory")


class _Oa100bdstateFlagFactoryDefault_Type(Integer32):
    """Custom type oa100bdstateFlagFactoryDefault based on Integer32"""
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


_Oa100bdstateFlagFactoryDefault_Type.__name__ = "Integer32"
_Oa100bdstateFlagFactoryDefault_Object = MibTableColumn
oa100bdstateFlagFactoryDefault = _Oa100bdstateFlagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 3, 2, 13),
    _Oa100bdstateFlagFactoryDefault_Type()
)
oa100bdstateFlagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateFlagFactoryDefault.setStatus("mandatory")
_Gx2OA100BDStatusTable_Object = MibTable
gx2OA100BDStatusTable = _Gx2OA100BDStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4)
)
if mibBuilder.loadTexts:
    gx2OA100BDStatusTable.setStatus("mandatory")
_Gx2OA100BDStatusEntry_Object = MibTableRow
gx2OA100BDStatusEntry = _Gx2OA100BDStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3)
)
gx2OA100BDStatusEntry.setIndexNames(
    (0, "OMNI-gx2oa100bd-MIB", "gx2OA100BDStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2OA100BDStatusEntry.setStatus("mandatory")


class _Gx2OA100BDStatusTableIndex_Type(Integer32):
    """Custom type gx2OA100BDStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2OA100BDStatusTableIndex_Type.__name__ = "Integer32"
_Gx2OA100BDStatusTableIndex_Object = MibTableColumn
gx2OA100BDStatusTableIndex = _Gx2OA100BDStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 1),
    _Gx2OA100BDStatusTableIndex_Type()
)
gx2OA100BDStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2OA100BDStatusTableIndex.setStatus("mandatory")


class _Oa100bdlabelBoot_Type(DisplayString):
    """Custom type oa100bdlabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelBoot_Type.__name__ = "DisplayString"
_Oa100bdlabelBoot_Object = MibTableColumn
oa100bdlabelBoot = _Oa100bdlabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 2),
    _Oa100bdlabelBoot_Type()
)
oa100bdlabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelBoot.setStatus("optional")


class _Oa100bdvalueBoot_Type(Integer32):
    """Custom type oa100bdvalueBoot based on Integer32"""
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


_Oa100bdvalueBoot_Type.__name__ = "Integer32"
_Oa100bdvalueBoot_Object = MibTableColumn
oa100bdvalueBoot = _Oa100bdvalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 3),
    _Oa100bdvalueBoot_Type()
)
oa100bdvalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueBoot.setStatus("mandatory")


class _Oa100bdstateflagBoot_Type(Integer32):
    """Custom type oa100bdstateflagBoot based on Integer32"""
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


_Oa100bdstateflagBoot_Type.__name__ = "Integer32"
_Oa100bdstateflagBoot_Object = MibTableColumn
oa100bdstateflagBoot = _Oa100bdstateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 4),
    _Oa100bdstateflagBoot_Type()
)
oa100bdstateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagBoot.setStatus("mandatory")


class _Oa100bdlabelFlash_Type(DisplayString):
    """Custom type oa100bdlabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelFlash_Type.__name__ = "DisplayString"
_Oa100bdlabelFlash_Object = MibTableColumn
oa100bdlabelFlash = _Oa100bdlabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 5),
    _Oa100bdlabelFlash_Type()
)
oa100bdlabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelFlash.setStatus("optional")


class _Oa100bdvalueFlash_Type(Integer32):
    """Custom type oa100bdvalueFlash based on Integer32"""
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


_Oa100bdvalueFlash_Type.__name__ = "Integer32"
_Oa100bdvalueFlash_Object = MibTableColumn
oa100bdvalueFlash = _Oa100bdvalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 6),
    _Oa100bdvalueFlash_Type()
)
oa100bdvalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueFlash.setStatus("mandatory")


class _Oa100bdstateflagFlash_Type(Integer32):
    """Custom type oa100bdstateflagFlash based on Integer32"""
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


_Oa100bdstateflagFlash_Type.__name__ = "Integer32"
_Oa100bdstateflagFlash_Object = MibTableColumn
oa100bdstateflagFlash = _Oa100bdstateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 7),
    _Oa100bdstateflagFlash_Type()
)
oa100bdstateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagFlash.setStatus("mandatory")


class _Oa100bdlabelFactoryDataCRC_Type(DisplayString):
    """Custom type oa100bdlabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelFactoryDataCRC_Type.__name__ = "DisplayString"
_Oa100bdlabelFactoryDataCRC_Object = MibTableColumn
oa100bdlabelFactoryDataCRC = _Oa100bdlabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 8),
    _Oa100bdlabelFactoryDataCRC_Type()
)
oa100bdlabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelFactoryDataCRC.setStatus("optional")


class _Oa100bdvalueFactoryDataCRC_Type(Integer32):
    """Custom type oa100bdvalueFactoryDataCRC based on Integer32"""
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


_Oa100bdvalueFactoryDataCRC_Type.__name__ = "Integer32"
_Oa100bdvalueFactoryDataCRC_Object = MibTableColumn
oa100bdvalueFactoryDataCRC = _Oa100bdvalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 9),
    _Oa100bdvalueFactoryDataCRC_Type()
)
oa100bdvalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueFactoryDataCRC.setStatus("mandatory")


class _Oa100bdstateflagFactoryDataCRC_Type(Integer32):
    """Custom type oa100bdstateflagFactoryDataCRC based on Integer32"""
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


_Oa100bdstateflagFactoryDataCRC_Type.__name__ = "Integer32"
_Oa100bdstateflagFactoryDataCRC_Object = MibTableColumn
oa100bdstateflagFactoryDataCRC = _Oa100bdstateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 10),
    _Oa100bdstateflagFactoryDataCRC_Type()
)
oa100bdstateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagFactoryDataCRC.setStatus("mandatory")


class _Oa100bdlabelAlarmDataCRC_Type(DisplayString):
    """Custom type oa100bdlabelAlarmDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelAlarmDataCRC_Type.__name__ = "DisplayString"
_Oa100bdlabelAlarmDataCRC_Object = MibTableColumn
oa100bdlabelAlarmDataCRC = _Oa100bdlabelAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 11),
    _Oa100bdlabelAlarmDataCRC_Type()
)
oa100bdlabelAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelAlarmDataCRC.setStatus("optional")


class _Oa100bdvalueAlarmDataCRC_Type(Integer32):
    """Custom type oa100bdvalueAlarmDataCRC based on Integer32"""
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


_Oa100bdvalueAlarmDataCRC_Type.__name__ = "Integer32"
_Oa100bdvalueAlarmDataCRC_Object = MibTableColumn
oa100bdvalueAlarmDataCRC = _Oa100bdvalueAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 12),
    _Oa100bdvalueAlarmDataCRC_Type()
)
oa100bdvalueAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueAlarmDataCRC.setStatus("mandatory")


class _Oa100bdstateflagAlarmDataCRC_Type(Integer32):
    """Custom type oa100bdstateflagAlarmDataCRC based on Integer32"""
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


_Oa100bdstateflagAlarmDataCRC_Type.__name__ = "Integer32"
_Oa100bdstateflagAlarmDataCRC_Object = MibTableColumn
oa100bdstateflagAlarmDataCRC = _Oa100bdstateflagAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 13),
    _Oa100bdstateflagAlarmDataCRC_Type()
)
oa100bdstateflagAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagAlarmDataCRC.setStatus("mandatory")


class _Oa100bdlabelCalibrationDataCRC_Type(DisplayString):
    """Custom type oa100bdlabelCalibrationDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelCalibrationDataCRC_Type.__name__ = "DisplayString"
_Oa100bdlabelCalibrationDataCRC_Object = MibTableColumn
oa100bdlabelCalibrationDataCRC = _Oa100bdlabelCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 14),
    _Oa100bdlabelCalibrationDataCRC_Type()
)
oa100bdlabelCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelCalibrationDataCRC.setStatus("optional")


class _Oa100bdvalueCalibrationDataCRC_Type(Integer32):
    """Custom type oa100bdvalueCalibrationDataCRC based on Integer32"""
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


_Oa100bdvalueCalibrationDataCRC_Type.__name__ = "Integer32"
_Oa100bdvalueCalibrationDataCRC_Object = MibTableColumn
oa100bdvalueCalibrationDataCRC = _Oa100bdvalueCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 15),
    _Oa100bdvalueCalibrationDataCRC_Type()
)
oa100bdvalueCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueCalibrationDataCRC.setStatus("mandatory")


class _Oa100bdstateflagCalibrationDataCRC_Type(Integer32):
    """Custom type oa100bdstateflagCalibrationDataCRC based on Integer32"""
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


_Oa100bdstateflagCalibrationDataCRC_Type.__name__ = "Integer32"
_Oa100bdstateflagCalibrationDataCRC_Object = MibTableColumn
oa100bdstateflagCalibrationDataCRC = _Oa100bdstateflagCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 16),
    _Oa100bdstateflagCalibrationDataCRC_Type()
)
oa100bdstateflagCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagCalibrationDataCRC.setStatus("mandatory")


class _Oa100bdlabelOptInShutdown_Type(DisplayString):
    """Custom type oa100bdlabelOptInShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelOptInShutdown_Type.__name__ = "DisplayString"
_Oa100bdlabelOptInShutdown_Object = MibTableColumn
oa100bdlabelOptInShutdown = _Oa100bdlabelOptInShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 17),
    _Oa100bdlabelOptInShutdown_Type()
)
oa100bdlabelOptInShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelOptInShutdown.setStatus("optional")


class _Oa100bdvalueOptInShutdown_Type(Integer32):
    """Custom type oa100bdvalueOptInShutdown based on Integer32"""
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


_Oa100bdvalueOptInShutdown_Type.__name__ = "Integer32"
_Oa100bdvalueOptInShutdown_Object = MibTableColumn
oa100bdvalueOptInShutdown = _Oa100bdvalueOptInShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 18),
    _Oa100bdvalueOptInShutdown_Type()
)
oa100bdvalueOptInShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueOptInShutdown.setStatus("mandatory")


class _Oa100bdstateflagOptInShutdown_Type(Integer32):
    """Custom type oa100bdstateflagOptInShutdown based on Integer32"""
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


_Oa100bdstateflagOptInShutdown_Type.__name__ = "Integer32"
_Oa100bdstateflagOptInShutdown_Object = MibTableColumn
oa100bdstateflagOptInShutdown = _Oa100bdstateflagOptInShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 19),
    _Oa100bdstateflagOptInShutdown_Type()
)
oa100bdstateflagOptInShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagOptInShutdown.setStatus("mandatory")


class _Oa100bdlabelMainTECTempShutdown_Type(DisplayString):
    """Custom type oa100bdlabelMainTECTempShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelMainTECTempShutdown_Type.__name__ = "DisplayString"
_Oa100bdlabelMainTECTempShutdown_Object = MibTableColumn
oa100bdlabelMainTECTempShutdown = _Oa100bdlabelMainTECTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 20),
    _Oa100bdlabelMainTECTempShutdown_Type()
)
oa100bdlabelMainTECTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelMainTECTempShutdown.setStatus("optional")


class _Oa100bdvalueMainTECTempShutdown_Type(Integer32):
    """Custom type oa100bdvalueMainTECTempShutdown based on Integer32"""
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


_Oa100bdvalueMainTECTempShutdown_Type.__name__ = "Integer32"
_Oa100bdvalueMainTECTempShutdown_Object = MibTableColumn
oa100bdvalueMainTECTempShutdown = _Oa100bdvalueMainTECTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 21),
    _Oa100bdvalueMainTECTempShutdown_Type()
)
oa100bdvalueMainTECTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueMainTECTempShutdown.setStatus("mandatory")


class _Oa100bdstateflagMainTECTempShutdown_Type(Integer32):
    """Custom type oa100bdstateflagMainTECTempShutdown based on Integer32"""
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


_Oa100bdstateflagMainTECTempShutdown_Type.__name__ = "Integer32"
_Oa100bdstateflagMainTECTempShutdown_Object = MibTableColumn
oa100bdstateflagMainTECTempShutdown = _Oa100bdstateflagMainTECTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 22),
    _Oa100bdstateflagMainTECTempShutdown_Type()
)
oa100bdstateflagMainTECTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagMainTECTempShutdown.setStatus("mandatory")


class _Oa100bdlabelAuxTECTempShutdown_Type(DisplayString):
    """Custom type oa100bdlabelAuxTECTempShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelAuxTECTempShutdown_Type.__name__ = "DisplayString"
_Oa100bdlabelAuxTECTempShutdown_Object = MibTableColumn
oa100bdlabelAuxTECTempShutdown = _Oa100bdlabelAuxTECTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 23),
    _Oa100bdlabelAuxTECTempShutdown_Type()
)
oa100bdlabelAuxTECTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelAuxTECTempShutdown.setStatus("optional")


class _Oa100bdvalueAuxTECTempShutdown_Type(Integer32):
    """Custom type oa100bdvalueAuxTECTempShutdown based on Integer32"""
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


_Oa100bdvalueAuxTECTempShutdown_Type.__name__ = "Integer32"
_Oa100bdvalueAuxTECTempShutdown_Object = MibTableColumn
oa100bdvalueAuxTECTempShutdown = _Oa100bdvalueAuxTECTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 24),
    _Oa100bdvalueAuxTECTempShutdown_Type()
)
oa100bdvalueAuxTECTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueAuxTECTempShutdown.setStatus("mandatory")


class _Oa100bdstateflagAuxTECTempShutdown_Type(Integer32):
    """Custom type oa100bdstateflagAuxTECTempShutdown based on Integer32"""
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


_Oa100bdstateflagAuxTECTempShutdown_Type.__name__ = "Integer32"
_Oa100bdstateflagAuxTECTempShutdown_Object = MibTableColumn
oa100bdstateflagAuxTECTempShutdown = _Oa100bdstateflagAuxTECTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 25),
    _Oa100bdstateflagAuxTECTempShutdown_Type()
)
oa100bdstateflagAuxTECTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagAuxTECTempShutdown.setStatus("mandatory")


class _Oa100bdlabelPowerFail_Type(DisplayString):
    """Custom type oa100bdlabelPowerFail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelPowerFail_Type.__name__ = "DisplayString"
_Oa100bdlabelPowerFail_Object = MibTableColumn
oa100bdlabelPowerFail = _Oa100bdlabelPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 26),
    _Oa100bdlabelPowerFail_Type()
)
oa100bdlabelPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelPowerFail.setStatus("optional")


class _Oa100bdvaluePowerFail_Type(Integer32):
    """Custom type oa100bdvaluePowerFail based on Integer32"""
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


_Oa100bdvaluePowerFail_Type.__name__ = "Integer32"
_Oa100bdvaluePowerFail_Object = MibTableColumn
oa100bdvaluePowerFail = _Oa100bdvaluePowerFail_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 27),
    _Oa100bdvaluePowerFail_Type()
)
oa100bdvaluePowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvaluePowerFail.setStatus("mandatory")


class _Oa100bdstateflagPowerFail_Type(Integer32):
    """Custom type oa100bdstateflagPowerFail based on Integer32"""
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


_Oa100bdstateflagPowerFail_Type.__name__ = "Integer32"
_Oa100bdstateflagPowerFail_Object = MibTableColumn
oa100bdstateflagPowerFail = _Oa100bdstateflagPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 28),
    _Oa100bdstateflagPowerFail_Type()
)
oa100bdstateflagPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagPowerFail.setStatus("mandatory")


class _Oa100bdlabelKeySwitch_Type(DisplayString):
    """Custom type oa100bdlabelKeySwitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelKeySwitch_Type.__name__ = "DisplayString"
_Oa100bdlabelKeySwitch_Object = MibTableColumn
oa100bdlabelKeySwitch = _Oa100bdlabelKeySwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 29),
    _Oa100bdlabelKeySwitch_Type()
)
oa100bdlabelKeySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelKeySwitch.setStatus("optional")


class _Oa100bdvalueKeySwitch_Type(Integer32):
    """Custom type oa100bdvalueKeySwitch based on Integer32"""
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


_Oa100bdvalueKeySwitch_Type.__name__ = "Integer32"
_Oa100bdvalueKeySwitch_Object = MibTableColumn
oa100bdvalueKeySwitch = _Oa100bdvalueKeySwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 30),
    _Oa100bdvalueKeySwitch_Type()
)
oa100bdvalueKeySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueKeySwitch.setStatus("mandatory")


class _Oa100bdstateflagKeySwitch_Type(Integer32):
    """Custom type oa100bdstateflagKeySwitch based on Integer32"""
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


_Oa100bdstateflagKeySwitch_Type.__name__ = "Integer32"
_Oa100bdstateflagKeySwitch_Object = MibTableColumn
oa100bdstateflagKeySwitch = _Oa100bdstateflagKeySwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 31),
    _Oa100bdstateflagKeySwitch_Type()
)
oa100bdstateflagKeySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagKeySwitch.setStatus("mandatory")


class _Oa100bdlabelMainLaserCurrShutdown_Type(DisplayString):
    """Custom type oa100bdlabelMainLaserCurrShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelMainLaserCurrShutdown_Type.__name__ = "DisplayString"
_Oa100bdlabelMainLaserCurrShutdown_Object = MibTableColumn
oa100bdlabelMainLaserCurrShutdown = _Oa100bdlabelMainLaserCurrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 32),
    _Oa100bdlabelMainLaserCurrShutdown_Type()
)
oa100bdlabelMainLaserCurrShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelMainLaserCurrShutdown.setStatus("optional")


class _Oa100bdvalueMainLaserCurrShutdown_Type(Integer32):
    """Custom type oa100bdvalueMainLaserCurrShutdown based on Integer32"""
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


_Oa100bdvalueMainLaserCurrShutdown_Type.__name__ = "Integer32"
_Oa100bdvalueMainLaserCurrShutdown_Object = MibTableColumn
oa100bdvalueMainLaserCurrShutdown = _Oa100bdvalueMainLaserCurrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 33),
    _Oa100bdvalueMainLaserCurrShutdown_Type()
)
oa100bdvalueMainLaserCurrShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueMainLaserCurrShutdown.setStatus("mandatory")


class _Oa100bdstateflagMainLaserCurrShutdown_Type(Integer32):
    """Custom type oa100bdstateflagMainLaserCurrShutdown based on Integer32"""
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


_Oa100bdstateflagMainLaserCurrShutdown_Type.__name__ = "Integer32"
_Oa100bdstateflagMainLaserCurrShutdown_Object = MibTableColumn
oa100bdstateflagMainLaserCurrShutdown = _Oa100bdstateflagMainLaserCurrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 34),
    _Oa100bdstateflagMainLaserCurrShutdown_Type()
)
oa100bdstateflagMainLaserCurrShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagMainLaserCurrShutdown.setStatus("mandatory")


class _Oa100bdlabelAuxLaserCurrShutdown_Type(DisplayString):
    """Custom type oa100bdlabelAuxLaserCurrShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelAuxLaserCurrShutdown_Type.__name__ = "DisplayString"
_Oa100bdlabelAuxLaserCurrShutdown_Object = MibTableColumn
oa100bdlabelAuxLaserCurrShutdown = _Oa100bdlabelAuxLaserCurrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 35),
    _Oa100bdlabelAuxLaserCurrShutdown_Type()
)
oa100bdlabelAuxLaserCurrShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelAuxLaserCurrShutdown.setStatus("optional")


class _Oa100bdvalueAuxLaserCurrShutdown_Type(Integer32):
    """Custom type oa100bdvalueAuxLaserCurrShutdown based on Integer32"""
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


_Oa100bdvalueAuxLaserCurrShutdown_Type.__name__ = "Integer32"
_Oa100bdvalueAuxLaserCurrShutdown_Object = MibTableColumn
oa100bdvalueAuxLaserCurrShutdown = _Oa100bdvalueAuxLaserCurrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 36),
    _Oa100bdvalueAuxLaserCurrShutdown_Type()
)
oa100bdvalueAuxLaserCurrShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueAuxLaserCurrShutdown.setStatus("mandatory")


class _Oa100bdstateflagAuxLaserCurrShutdown_Type(Integer32):
    """Custom type oa100bdstateflagAuxLaserCurrShutdown based on Integer32"""
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


_Oa100bdstateflagAuxLaserCurrShutdown_Type.__name__ = "Integer32"
_Oa100bdstateflagAuxLaserCurrShutdown_Object = MibTableColumn
oa100bdstateflagAuxLaserCurrShutdown = _Oa100bdstateflagAuxLaserCurrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 37),
    _Oa100bdstateflagAuxLaserCurrShutdown_Type()
)
oa100bdstateflagAuxLaserCurrShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagAuxLaserCurrShutdown.setStatus("mandatory")


class _Oa100bdlabelMainLaserPowShutdown_Type(DisplayString):
    """Custom type oa100bdlabelMainLaserPowShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelMainLaserPowShutdown_Type.__name__ = "DisplayString"
_Oa100bdlabelMainLaserPowShutdown_Object = MibTableColumn
oa100bdlabelMainLaserPowShutdown = _Oa100bdlabelMainLaserPowShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 38),
    _Oa100bdlabelMainLaserPowShutdown_Type()
)
oa100bdlabelMainLaserPowShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelMainLaserPowShutdown.setStatus("optional")


class _Oa100bdvalueMainLaserPowShutdown_Type(Integer32):
    """Custom type oa100bdvalueMainLaserPowShutdown based on Integer32"""
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


_Oa100bdvalueMainLaserPowShutdown_Type.__name__ = "Integer32"
_Oa100bdvalueMainLaserPowShutdown_Object = MibTableColumn
oa100bdvalueMainLaserPowShutdown = _Oa100bdvalueMainLaserPowShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 39),
    _Oa100bdvalueMainLaserPowShutdown_Type()
)
oa100bdvalueMainLaserPowShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueMainLaserPowShutdown.setStatus("mandatory")


class _Oa100bdstateflagMainLaserPowShutdown_Type(Integer32):
    """Custom type oa100bdstateflagMainLaserPowShutdown based on Integer32"""
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


_Oa100bdstateflagMainLaserPowShutdown_Type.__name__ = "Integer32"
_Oa100bdstateflagMainLaserPowShutdown_Object = MibTableColumn
oa100bdstateflagMainLaserPowShutdown = _Oa100bdstateflagMainLaserPowShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 40),
    _Oa100bdstateflagMainLaserPowShutdown_Type()
)
oa100bdstateflagMainLaserPowShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagMainLaserPowShutdown.setStatus("mandatory")


class _Oa100bdlabelAuxLaserPowShutdown_Type(DisplayString):
    """Custom type oa100bdlabelAuxLaserPowShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelAuxLaserPowShutdown_Type.__name__ = "DisplayString"
_Oa100bdlabelAuxLaserPowShutdown_Object = MibTableColumn
oa100bdlabelAuxLaserPowShutdown = _Oa100bdlabelAuxLaserPowShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 41),
    _Oa100bdlabelAuxLaserPowShutdown_Type()
)
oa100bdlabelAuxLaserPowShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelAuxLaserPowShutdown.setStatus("optional")


class _Oa100bdvalueAuxLaserPowShutdown_Type(Integer32):
    """Custom type oa100bdvalueAuxLaserPowShutdown based on Integer32"""
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


_Oa100bdvalueAuxLaserPowShutdown_Type.__name__ = "Integer32"
_Oa100bdvalueAuxLaserPowShutdown_Object = MibTableColumn
oa100bdvalueAuxLaserPowShutdown = _Oa100bdvalueAuxLaserPowShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 42),
    _Oa100bdvalueAuxLaserPowShutdown_Type()
)
oa100bdvalueAuxLaserPowShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueAuxLaserPowShutdown.setStatus("mandatory")


class _Oa100bdstateflagAuxLaserPowShutdown_Type(Integer32):
    """Custom type oa100bdstateflagAuxLaserPowShutdown based on Integer32"""
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


_Oa100bdstateflagAuxLaserPowShutdown_Type.__name__ = "Integer32"
_Oa100bdstateflagAuxLaserPowShutdown_Object = MibTableColumn
oa100bdstateflagAuxLaserPowShutdown = _Oa100bdstateflagAuxLaserPowShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 43),
    _Oa100bdstateflagAuxLaserPowShutdown_Type()
)
oa100bdstateflagAuxLaserPowShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagAuxLaserPowShutdown.setStatus("mandatory")


class _Oa100bdlabelADCStatus_Type(DisplayString):
    """Custom type oa100bdlabelADCStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelADCStatus_Type.__name__ = "DisplayString"
_Oa100bdlabelADCStatus_Object = MibTableColumn
oa100bdlabelADCStatus = _Oa100bdlabelADCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 44),
    _Oa100bdlabelADCStatus_Type()
)
oa100bdlabelADCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelADCStatus.setStatus("optional")


class _Oa100bdvalueADCStatus_Type(Integer32):
    """Custom type oa100bdvalueADCStatus based on Integer32"""
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


_Oa100bdvalueADCStatus_Type.__name__ = "Integer32"
_Oa100bdvalueADCStatus_Object = MibTableColumn
oa100bdvalueADCStatus = _Oa100bdvalueADCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 45),
    _Oa100bdvalueADCStatus_Type()
)
oa100bdvalueADCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueADCStatus.setStatus("mandatory")


class _Oa100bdstateflagADCStatus_Type(Integer32):
    """Custom type oa100bdstateflagADCStatus based on Integer32"""
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


_Oa100bdstateflagADCStatus_Type.__name__ = "Integer32"
_Oa100bdstateflagADCStatus_Object = MibTableColumn
oa100bdstateflagADCStatus = _Oa100bdstateflagADCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 46),
    _Oa100bdstateflagADCStatus_Type()
)
oa100bdstateflagADCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagADCStatus.setStatus("mandatory")


class _Oa100bdlabelConstGainStatus_Type(DisplayString):
    """Custom type oa100bdlabelConstGainStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelConstGainStatus_Type.__name__ = "DisplayString"
_Oa100bdlabelConstGainStatus_Object = MibTableColumn
oa100bdlabelConstGainStatus = _Oa100bdlabelConstGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 47),
    _Oa100bdlabelConstGainStatus_Type()
)
oa100bdlabelConstGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelConstGainStatus.setStatus("optional")


class _Oa100bdvalueConstGainStatus_Type(Integer32):
    """Custom type oa100bdvalueConstGainStatus based on Integer32"""
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


_Oa100bdvalueConstGainStatus_Type.__name__ = "Integer32"
_Oa100bdvalueConstGainStatus_Object = MibTableColumn
oa100bdvalueConstGainStatus = _Oa100bdvalueConstGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 48),
    _Oa100bdvalueConstGainStatus_Type()
)
oa100bdvalueConstGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueConstGainStatus.setStatus("mandatory")


class _Oa100bdstateflagConstGainStatus_Type(Integer32):
    """Custom type oa100bdstateflagConstGainStatus based on Integer32"""
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


_Oa100bdstateflagConstGainStatus_Type.__name__ = "Integer32"
_Oa100bdstateflagConstGainStatus_Object = MibTableColumn
oa100bdstateflagConstGainStatus = _Oa100bdstateflagConstGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 49),
    _Oa100bdstateflagConstGainStatus_Type()
)
oa100bdstateflagConstGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagConstGainStatus.setStatus("mandatory")


class _Oa100bdlabelHardwareErrorStatus_Type(DisplayString):
    """Custom type oa100bdlabelHardwareErrorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelHardwareErrorStatus_Type.__name__ = "DisplayString"
_Oa100bdlabelHardwareErrorStatus_Object = MibTableColumn
oa100bdlabelHardwareErrorStatus = _Oa100bdlabelHardwareErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 50),
    _Oa100bdlabelHardwareErrorStatus_Type()
)
oa100bdlabelHardwareErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelHardwareErrorStatus.setStatus("optional")


class _Oa100bdvalueHardwareErrorStatus_Type(Integer32):
    """Custom type oa100bdvalueHardwareErrorStatus based on Integer32"""
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


_Oa100bdvalueHardwareErrorStatus_Type.__name__ = "Integer32"
_Oa100bdvalueHardwareErrorStatus_Object = MibTableColumn
oa100bdvalueHardwareErrorStatus = _Oa100bdvalueHardwareErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 51),
    _Oa100bdvalueHardwareErrorStatus_Type()
)
oa100bdvalueHardwareErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueHardwareErrorStatus.setStatus("mandatory")


class _Oa100bdstateflagHardwareErrorStatus_Type(Integer32):
    """Custom type oa100bdstateflagHardwareErrorStatus based on Integer32"""
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


_Oa100bdstateflagHardwareErrorStatus_Type.__name__ = "Integer32"
_Oa100bdstateflagHardwareErrorStatus_Object = MibTableColumn
oa100bdstateflagHardwareErrorStatus = _Oa100bdstateflagHardwareErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 52),
    _Oa100bdstateflagHardwareErrorStatus_Type()
)
oa100bdstateflagHardwareErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagHardwareErrorStatus.setStatus("mandatory")


class _Oa100bdlabelStandbyStatus_Type(DisplayString):
    """Custom type oa100bdlabelStandbyStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdlabelStandbyStatus_Type.__name__ = "DisplayString"
_Oa100bdlabelStandbyStatus_Object = MibTableColumn
oa100bdlabelStandbyStatus = _Oa100bdlabelStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 53),
    _Oa100bdlabelStandbyStatus_Type()
)
oa100bdlabelStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdlabelStandbyStatus.setStatus("optional")


class _Oa100bdvalueStandbyStatus_Type(Integer32):
    """Custom type oa100bdvalueStandbyStatus based on Integer32"""
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


_Oa100bdvalueStandbyStatus_Type.__name__ = "Integer32"
_Oa100bdvalueStandbyStatus_Object = MibTableColumn
oa100bdvalueStandbyStatus = _Oa100bdvalueStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 54),
    _Oa100bdvalueStandbyStatus_Type()
)
oa100bdvalueStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdvalueStandbyStatus.setStatus("mandatory")


class _Oa100bdstateflagStandbyStatus_Type(Integer32):
    """Custom type oa100bdstateflagStandbyStatus based on Integer32"""
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


_Oa100bdstateflagStandbyStatus_Type.__name__ = "Integer32"
_Oa100bdstateflagStandbyStatus_Object = MibTableColumn
oa100bdstateflagStandbyStatus = _Oa100bdstateflagStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 4, 3, 55),
    _Oa100bdstateflagStandbyStatus_Type()
)
oa100bdstateflagStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdstateflagStandbyStatus.setStatus("mandatory")
_Gx2OA100BDFactoryTable_Object = MibTable
gx2OA100BDFactoryTable = _Gx2OA100BDFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5)
)
if mibBuilder.loadTexts:
    gx2OA100BDFactoryTable.setStatus("mandatory")
_Gx2OA100BDFactoryEntry_Object = MibTableRow
gx2OA100BDFactoryEntry = _Gx2OA100BDFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4)
)
gx2OA100BDFactoryEntry.setIndexNames(
    (0, "OMNI-gx2oa100bd-MIB", "gx2OA100BDFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2OA100BDFactoryEntry.setStatus("mandatory")


class _Gx2OA100BDFactoryTableIndex_Type(Integer32):
    """Custom type gx2OA100BDFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2OA100BDFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2OA100BDFactoryTableIndex_Object = MibTableColumn
gx2OA100BDFactoryTableIndex = _Gx2OA100BDFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 1),
    _Gx2OA100BDFactoryTableIndex_Type()
)
gx2OA100BDFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2OA100BDFactoryTableIndex.setStatus("mandatory")
_Oa100bdbootControlByte_Type = Integer32
_Oa100bdbootControlByte_Object = MibTableColumn
oa100bdbootControlByte = _Oa100bdbootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 2),
    _Oa100bdbootControlByte_Type()
)
oa100bdbootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdbootControlByte.setStatus("mandatory")
_Oa100bdbootStatusByte_Type = Integer32
_Oa100bdbootStatusByte_Object = MibTableColumn
oa100bdbootStatusByte = _Oa100bdbootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 3),
    _Oa100bdbootStatusByte_Type()
)
oa100bdbootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdbootStatusByte.setStatus("mandatory")
_Oa100bdbank0CRC_Type = Integer32
_Oa100bdbank0CRC_Object = MibTableColumn
oa100bdbank0CRC = _Oa100bdbank0CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 4),
    _Oa100bdbank0CRC_Type()
)
oa100bdbank0CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdbank0CRC.setStatus("mandatory")
_Oa100bdbank1CRC_Type = Integer32
_Oa100bdbank1CRC_Object = MibTableColumn
oa100bdbank1CRC = _Oa100bdbank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 5),
    _Oa100bdbank1CRC_Type()
)
oa100bdbank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdbank1CRC.setStatus("mandatory")
_Oa100bdprgEEPROMByte_Type = Integer32
_Oa100bdprgEEPROMByte_Object = MibTableColumn
oa100bdprgEEPROMByte = _Oa100bdprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 6),
    _Oa100bdprgEEPROMByte_Type()
)
oa100bdprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdprgEEPROMByte.setStatus("mandatory")
_Oa100bdfactoryCRC_Type = Integer32
_Oa100bdfactoryCRC_Object = MibTableColumn
oa100bdfactoryCRC = _Oa100bdfactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 7),
    _Oa100bdfactoryCRC_Type()
)
oa100bdfactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdfactoryCRC.setStatus("mandatory")


class _Oa100bdcalculateCRC_Type(Integer32):
    """Custom type oa100bdcalculateCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmdata", 3),
          ("calibration", 2),
          ("factory", 1))
    )


_Oa100bdcalculateCRC_Type.__name__ = "Integer32"
_Oa100bdcalculateCRC_Object = MibTableColumn
oa100bdcalculateCRC = _Oa100bdcalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 8),
    _Oa100bdcalculateCRC_Type()
)
oa100bdcalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdcalculateCRC.setStatus("obsolete")
_Oa100bdhourMeter_Type = Integer32
_Oa100bdhourMeter_Object = MibTableColumn
oa100bdhourMeter = _Oa100bdhourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 9),
    _Oa100bdhourMeter_Type()
)
oa100bdhourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdhourMeter.setStatus("mandatory")
_Oa100bdflashPrgCntA_Type = Integer32
_Oa100bdflashPrgCntA_Object = MibTableColumn
oa100bdflashPrgCntA = _Oa100bdflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 10),
    _Oa100bdflashPrgCntA_Type()
)
oa100bdflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdflashPrgCntA.setStatus("mandatory")
_Oa100bdflashPrgCntB_Type = Integer32
_Oa100bdflashPrgCntB_Object = MibTableColumn
oa100bdflashPrgCntB = _Oa100bdflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 11),
    _Oa100bdflashPrgCntB_Type()
)
oa100bdflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdflashPrgCntB.setStatus("mandatory")


class _Oa100bdfwRev0_Type(DisplayString):
    """Custom type oa100bdfwRev0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdfwRev0_Type.__name__ = "DisplayString"
_Oa100bdfwRev0_Object = MibTableColumn
oa100bdfwRev0 = _Oa100bdfwRev0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 12),
    _Oa100bdfwRev0_Type()
)
oa100bdfwRev0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdfwRev0.setStatus("mandatory")


class _Oa100bdfwRev1_Type(DisplayString):
    """Custom type oa100bdfwRev1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Oa100bdfwRev1_Type.__name__ = "DisplayString"
_Oa100bdfwRev1_Object = MibTableColumn
oa100bdfwRev1 = _Oa100bdfwRev1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 5, 4, 13),
    _Oa100bdfwRev1_Type()
)
oa100bdfwRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oa100bdfwRev1.setStatus("mandatory")
_Gx2OA100BDHoldTimeTable_Object = MibTable
gx2OA100BDHoldTimeTable = _Gx2OA100BDHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 6)
)
if mibBuilder.loadTexts:
    gx2OA100BDHoldTimeTable.setStatus("mandatory")
_Gx2OA100BDHoldTimeEntry_Object = MibTableRow
gx2OA100BDHoldTimeEntry = _Gx2OA100BDHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 6, 5)
)
gx2OA100BDHoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2oa100bd-MIB", "gx2OA100BDHoldTimeTableIndex"),
    (0, "OMNI-gx2oa100bd-MIB", "gx2OA100BDHoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2OA100BDHoldTimeEntry.setStatus("mandatory")


class _Gx2OA100BDHoldTimeTableIndex_Type(Integer32):
    """Custom type gx2OA100BDHoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2OA100BDHoldTimeTableIndex_Type.__name__ = "Integer32"
_Gx2OA100BDHoldTimeTableIndex_Object = MibTableColumn
gx2OA100BDHoldTimeTableIndex = _Gx2OA100BDHoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 6, 5, 1),
    _Gx2OA100BDHoldTimeTableIndex_Type()
)
gx2OA100BDHoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2OA100BDHoldTimeTableIndex.setStatus("mandatory")


class _Gx2OA100BDHoldTimeSpecIndex_Type(Integer32):
    """Custom type gx2OA100BDHoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2OA100BDHoldTimeSpecIndex_Type.__name__ = "Integer32"
_Gx2OA100BDHoldTimeSpecIndex_Object = MibTableColumn
gx2OA100BDHoldTimeSpecIndex = _Gx2OA100BDHoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 6, 5, 2),
    _Gx2OA100BDHoldTimeSpecIndex_Type()
)
gx2OA100BDHoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2OA100BDHoldTimeSpecIndex.setStatus("mandatory")
_Gx2OA100BDHoldTimeData_Type = Integer32
_Gx2OA100BDHoldTimeData_Object = MibTableColumn
gx2OA100BDHoldTimeData = _Gx2OA100BDHoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 6, 5, 3),
    _Gx2OA100BDHoldTimeData_Type()
)
gx2OA100BDHoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gx2OA100BDHoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapOA100BDConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 1)
)
trapOA100BDConfigChangeInteger.setObjects(
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
    trapOA100BDConfigChangeInteger.setStatus(
        ""
    )

trapOA100BDConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 2)
)
trapOA100BDConfigChangeDisplayString.setObjects(
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
    trapOA100BDConfigChangeDisplayString.setStatus(
        ""
    )

trapOA100BDModuleTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 3)
)
trapOA100BDModuleTemperatureAlarm.setObjects(
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
    trapOA100BDModuleTemperatureAlarm.setStatus(
        ""
    )

trapOA100BDOpticalInPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 4)
)
trapOA100BDOpticalInPowerAlarm.setObjects(
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
    trapOA100BDOpticalInPowerAlarm.setStatus(
        ""
    )

trapOA100BDOpticalOutPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 5)
)
trapOA100BDOpticalOutPowerAlarm.setObjects(
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
    trapOA100BDOpticalOutPowerAlarm.setStatus(
        ""
    )

trapOA100BDMainTECTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 6)
)
trapOA100BDMainTECTemperatureAlarm.setObjects(
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
    trapOA100BDMainTECTemperatureAlarm.setStatus(
        ""
    )

trapOA100BDMainLaserPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 7)
)
trapOA100BDMainLaserPowerAlarm.setObjects(
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
    trapOA100BDMainLaserPowerAlarm.setStatus(
        ""
    )

trapOA100BDAuxTECTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 8)
)
trapOA100BDAuxTECTemperatureAlarm.setObjects(
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
    trapOA100BDAuxTECTemperatureAlarm.setStatus(
        ""
    )

trapOA100BDAuxLaserPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 9)
)
trapOA100BDAuxLaserPowerAlarm.setObjects(
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
    trapOA100BDAuxLaserPowerAlarm.setStatus(
        ""
    )

trapOA100BDFanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 10)
)
trapOA100BDFanCurrentAlarm.setObjects(
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
    trapOA100BDFanCurrentAlarm.setStatus(
        ""
    )

trapOA100BDResetFacDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 11)
)
trapOA100BDResetFacDefault.setObjects(
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
    trapOA100BDResetFacDefault.setStatus(
        ""
    )

trapOA100BDStandbyMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 12)
)
trapOA100BDStandbyMode.setObjects(
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
    trapOA100BDStandbyMode.setStatus(
        ""
    )

trapOA100BDOptInShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 13)
)
trapOA100BDOptInShutdown.setObjects(
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
    trapOA100BDOptInShutdown.setStatus(
        ""
    )

trapOA100BDMainTECTempShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 14)
)
trapOA100BDMainTECTempShutdown.setObjects(
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
    trapOA100BDMainTECTempShutdown.setStatus(
        ""
    )

trapOA100BDAuxTECTempShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 15)
)
trapOA100BDAuxTECTempShutdown.setObjects(
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
    trapOA100BDAuxTECTempShutdown.setStatus(
        ""
    )

trapOA100BDKeySwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 16)
)
trapOA100BDKeySwitch.setObjects(
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
    trapOA100BDKeySwitch.setStatus(
        ""
    )

trapOA100BDPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 17)
)
trapOA100BDPowerFail.setObjects(
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
    trapOA100BDPowerFail.setStatus(
        ""
    )

trapOA100BDMainLasCurrShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 18)
)
trapOA100BDMainLasCurrShutdown.setObjects(
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
    trapOA100BDMainLasCurrShutdown.setStatus(
        ""
    )

trapOA100BDAuxLasCurrShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 19)
)
trapOA100BDAuxLasCurrShutdown.setObjects(
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
    trapOA100BDAuxLasCurrShutdown.setStatus(
        ""
    )

trapOA100BDMainLasPowerShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 20)
)
trapOA100BDMainLasPowerShutdown.setObjects(
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
    trapOA100BDMainLasPowerShutdown.setStatus(
        ""
    )

trapOA100BDAuxLasPowerShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 21)
)
trapOA100BDAuxLasPowerShutdown.setObjects(
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
    trapOA100BDAuxLasPowerShutdown.setStatus(
        ""
    )

trapOA100BDInvalidMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 22)
)
trapOA100BDInvalidMode.setObjects(
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
    trapOA100BDInvalidMode.setStatus(
        ""
    )

trapOA100BDFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 23)
)
trapOA100BDFlashAlarm.setObjects(
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
    trapOA100BDFlashAlarm.setStatus(
        ""
    )

trapOA100BDBoot0Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 24)
)
trapOA100BDBoot0Alarm.setObjects(
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
    trapOA100BDBoot0Alarm.setStatus(
        ""
    )

trapOA100BDBoot1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 25)
)
trapOA100BDBoot1Alarm.setObjects(
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
    trapOA100BDBoot1Alarm.setStatus(
        ""
    )

trapOA100BDAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 26)
)
trapOA100BDAlarmDataCRCAlarm.setObjects(
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
    trapOA100BDAlarmDataCRCAlarm.setStatus(
        ""
    )

trapOA100BDFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 27)
)
trapOA100BDFactoryDataCRCAlarm.setObjects(
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
    trapOA100BDFactoryDataCRCAlarm.setStatus(
        ""
    )

trapOA100BDCalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 28)
)
trapOA100BDCalDataCRCAlarm.setObjects(
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
    trapOA100BDCalDataCRCAlarm.setStatus(
        ""
    )

trapOA100BDFacCalFloatAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 29)
)
trapOA100BDFacCalFloatAlarm.setObjects(
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
    trapOA100BDFacCalFloatAlarm.setStatus(
        ""
    )

trapOA100BDOptInThreshAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 30)
)
trapOA100BDOptInThreshAlarm.setObjects(
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
    trapOA100BDOptInThreshAlarm.setStatus(
        ""
    )

trapOA100BDGainErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 31)
)
trapOA100BDGainErrorAlarm.setObjects(
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
    trapOA100BDGainErrorAlarm.setStatus(
        ""
    )

trapOA100BDHardwareErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17, 0, 32)
)
trapOA100BDHardwareErrorAlarm.setObjects(
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
    trapOA100BDHardwareErrorAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2oa100bd-MIB",
    **{"Float": Float,
       "trapOA100BDConfigChangeInteger": trapOA100BDConfigChangeInteger,
       "trapOA100BDConfigChangeDisplayString": trapOA100BDConfigChangeDisplayString,
       "trapOA100BDModuleTemperatureAlarm": trapOA100BDModuleTemperatureAlarm,
       "trapOA100BDOpticalInPowerAlarm": trapOA100BDOpticalInPowerAlarm,
       "trapOA100BDOpticalOutPowerAlarm": trapOA100BDOpticalOutPowerAlarm,
       "trapOA100BDMainTECTemperatureAlarm": trapOA100BDMainTECTemperatureAlarm,
       "trapOA100BDMainLaserPowerAlarm": trapOA100BDMainLaserPowerAlarm,
       "trapOA100BDAuxTECTemperatureAlarm": trapOA100BDAuxTECTemperatureAlarm,
       "trapOA100BDAuxLaserPowerAlarm": trapOA100BDAuxLaserPowerAlarm,
       "trapOA100BDFanCurrentAlarm": trapOA100BDFanCurrentAlarm,
       "trapOA100BDResetFacDefault": trapOA100BDResetFacDefault,
       "trapOA100BDStandbyMode": trapOA100BDStandbyMode,
       "trapOA100BDOptInShutdown": trapOA100BDOptInShutdown,
       "trapOA100BDMainTECTempShutdown": trapOA100BDMainTECTempShutdown,
       "trapOA100BDAuxTECTempShutdown": trapOA100BDAuxTECTempShutdown,
       "trapOA100BDKeySwitch": trapOA100BDKeySwitch,
       "trapOA100BDPowerFail": trapOA100BDPowerFail,
       "trapOA100BDMainLasCurrShutdown": trapOA100BDMainLasCurrShutdown,
       "trapOA100BDAuxLasCurrShutdown": trapOA100BDAuxLasCurrShutdown,
       "trapOA100BDMainLasPowerShutdown": trapOA100BDMainLasPowerShutdown,
       "trapOA100BDAuxLasPowerShutdown": trapOA100BDAuxLasPowerShutdown,
       "trapOA100BDInvalidMode": trapOA100BDInvalidMode,
       "trapOA100BDFlashAlarm": trapOA100BDFlashAlarm,
       "trapOA100BDBoot0Alarm": trapOA100BDBoot0Alarm,
       "trapOA100BDBoot1Alarm": trapOA100BDBoot1Alarm,
       "trapOA100BDAlarmDataCRCAlarm": trapOA100BDAlarmDataCRCAlarm,
       "trapOA100BDFactoryDataCRCAlarm": trapOA100BDFactoryDataCRCAlarm,
       "trapOA100BDCalDataCRCAlarm": trapOA100BDCalDataCRCAlarm,
       "trapOA100BDFacCalFloatAlarm": trapOA100BDFacCalFloatAlarm,
       "trapOA100BDOptInThreshAlarm": trapOA100BDOptInThreshAlarm,
       "trapOA100BDGainErrorAlarm": trapOA100BDGainErrorAlarm,
       "trapOA100BDHardwareErrorAlarm": trapOA100BDHardwareErrorAlarm,
       "gx2OA100BDDescriptor": gx2OA100BDDescriptor,
       "gx2OA100BDAnalogTable": gx2OA100BDAnalogTable,
       "gx2OA100BDAnalogEntry": gx2OA100BDAnalogEntry,
       "gx2OA100BDAnalogTableIndex": gx2OA100BDAnalogTableIndex,
       "oa100bdlabelModTemp": oa100bdlabelModTemp,
       "oa100bduomModTemp": oa100bduomModTemp,
       "oa100bdmajorHighModTemp": oa100bdmajorHighModTemp,
       "oa100bdmajorLowModTemp": oa100bdmajorLowModTemp,
       "oa100bdminorHighModTemp": oa100bdminorHighModTemp,
       "oa100bdminorLowModTemp": oa100bdminorLowModTemp,
       "oa100bdcurrentValueModTemp": oa100bdcurrentValueModTemp,
       "oa100bdstateFlagModTemp": oa100bdstateFlagModTemp,
       "oa100bdminValueModTemp": oa100bdminValueModTemp,
       "oa100bdmaxValueModTemp": oa100bdmaxValueModTemp,
       "oa100bdalarmStateModTemp": oa100bdalarmStateModTemp,
       "oa100bdlabelOptInPower": oa100bdlabelOptInPower,
       "oa100bduomOptInPower": oa100bduomOptInPower,
       "oa100bdmajorHighOptInPower": oa100bdmajorHighOptInPower,
       "oa100bdmajorLowOptInPower": oa100bdmajorLowOptInPower,
       "oa100bdminorHighOptInPower": oa100bdminorHighOptInPower,
       "oa100bdminorLowOptInPower": oa100bdminorLowOptInPower,
       "oa100bdcurrentValueOptInPower": oa100bdcurrentValueOptInPower,
       "oa100bdstateFlagOptInPower": oa100bdstateFlagOptInPower,
       "oa100bdminValueOptInPower": oa100bdminValueOptInPower,
       "oa100bdmaxValueOptInPower": oa100bdmaxValueOptInPower,
       "oa100bdalarmStateOptInPower": oa100bdalarmStateOptInPower,
       "oa100bdlabelOptOutPower": oa100bdlabelOptOutPower,
       "oa100bduomOptOutPower": oa100bduomOptOutPower,
       "oa100bdmajorHighOptOutPower": oa100bdmajorHighOptOutPower,
       "oa100bdmajorLowOptOutPower": oa100bdmajorLowOptOutPower,
       "oa100bdminorHighOptOutPower": oa100bdminorHighOptOutPower,
       "oa100bdminorLowOptOutPower": oa100bdminorLowOptOutPower,
       "oa100bdcurrentValueOptOutPower": oa100bdcurrentValueOptOutPower,
       "oa100bdstateFlagOptOutPower": oa100bdstateFlagOptOutPower,
       "oa100bdminValueOptOutPower": oa100bdminValueOptOutPower,
       "oa100bdmaxValueOptOutPower": oa100bdmaxValueOptOutPower,
       "oa100bdalarmStateOptOutPower": oa100bdalarmStateOptOutPower,
       "oa100bdlabelMainTECTemp": oa100bdlabelMainTECTemp,
       "oa100bduomMainTECTemp": oa100bduomMainTECTemp,
       "oa100bdmajorHighMainTECTemp": oa100bdmajorHighMainTECTemp,
       "oa100bdmajorLowMainTECTemp": oa100bdmajorLowMainTECTemp,
       "oa100bdminorHighMainTECTemp": oa100bdminorHighMainTECTemp,
       "oa100bdminorLowMainTECTemp": oa100bdminorLowMainTECTemp,
       "oa100bdcurrentValueMainTECTemp": oa100bdcurrentValueMainTECTemp,
       "oa100bdstateFlagMainTECTemp": oa100bdstateFlagMainTECTemp,
       "oa100bdminValueMainTECTemp": oa100bdminValueMainTECTemp,
       "oa100bdmaxValueMainTECTemp": oa100bdmaxValueMainTECTemp,
       "oa100bdalarmStateMainTECTemp": oa100bdalarmStateMainTECTemp,
       "oa100bdlabelMainLaserPower": oa100bdlabelMainLaserPower,
       "oa100bduomMainLaserPower": oa100bduomMainLaserPower,
       "oa100bdmajorHighMainLaserPower": oa100bdmajorHighMainLaserPower,
       "oa100bdmajorLowMainLaserPower": oa100bdmajorLowMainLaserPower,
       "oa100bdminorHighMainLaserPower": oa100bdminorHighMainLaserPower,
       "oa100bdminorLowMainLaserPower": oa100bdminorLowMainLaserPower,
       "oa100bdcurrentValueMainLaserPower": oa100bdcurrentValueMainLaserPower,
       "oa100bdstateFlagMainLaserPower": oa100bdstateFlagMainLaserPower,
       "oa100bdminValueMainLaserPower": oa100bdminValueMainLaserPower,
       "oa100bdmaxValueMainLaserPower": oa100bdmaxValueMainLaserPower,
       "oa100bdalarmStateMainLaserPower": oa100bdalarmStateMainLaserPower,
       "oa100bdlabelAuxTECTemp": oa100bdlabelAuxTECTemp,
       "oa100bduomAuxTECTemp": oa100bduomAuxTECTemp,
       "oa100bdmajorHighAuxTECTemp": oa100bdmajorHighAuxTECTemp,
       "oa100bdmajorLowAuxTECTemp": oa100bdmajorLowAuxTECTemp,
       "oa100bdminorHighAuxTECTemp": oa100bdminorHighAuxTECTemp,
       "oa100bdminorLowAuxTECTemp": oa100bdminorLowAuxTECTemp,
       "oa100bdcurrentValueAuxTECTemp": oa100bdcurrentValueAuxTECTemp,
       "oa100bdstateFlagAuxTECTemp": oa100bdstateFlagAuxTECTemp,
       "oa100bdminValueAuxTECTemp": oa100bdminValueAuxTECTemp,
       "oa100bdmaxValueAuxTECTemp": oa100bdmaxValueAuxTECTemp,
       "oa100bdalarmStateAuxTECTemp": oa100bdalarmStateAuxTECTemp,
       "oa100bdlabelAuxLaserPower": oa100bdlabelAuxLaserPower,
       "oa100bduomAuxLaserPower": oa100bduomAuxLaserPower,
       "oa100bdmajorHighAuxLaserPower": oa100bdmajorHighAuxLaserPower,
       "oa100bdmajorLowAuxLaserPower": oa100bdmajorLowAuxLaserPower,
       "oa100bdminorHighAuxLaserPower": oa100bdminorHighAuxLaserPower,
       "oa100bdminorLowAuxLaserPower": oa100bdminorLowAuxLaserPower,
       "oa100bdcurrentValueAuxLaserPower": oa100bdcurrentValueAuxLaserPower,
       "oa100bdstateFlagAuxLaserPower": oa100bdstateFlagAuxLaserPower,
       "oa100bdminValueAuxLaserPower": oa100bdminValueAuxLaserPower,
       "oa100bdmaxValueAuxLaserPower": oa100bdmaxValueAuxLaserPower,
       "oa100bdalarmStateAuxLaserPower": oa100bdalarmStateAuxLaserPower,
       "oa100bdlabelFanCurrent": oa100bdlabelFanCurrent,
       "oa100bduomFanCurrent": oa100bduomFanCurrent,
       "oa100bdmajorHighFanCurrent": oa100bdmajorHighFanCurrent,
       "oa100bdmajorLowFanCurrent": oa100bdmajorLowFanCurrent,
       "oa100bdminorHighFanCurrent": oa100bdminorHighFanCurrent,
       "oa100bdminorLowFanCurrent": oa100bdminorLowFanCurrent,
       "oa100bdcurrentValueFanCurrent": oa100bdcurrentValueFanCurrent,
       "oa100bdstateFlagFanCurrent": oa100bdstateFlagFanCurrent,
       "oa100bdminValueFanCurrent": oa100bdminValueFanCurrent,
       "oa100bdmaxValueFanCurrent": oa100bdmaxValueFanCurrent,
       "oa100bdalarmStateFanCurrent": oa100bdalarmStateFanCurrent,
       "oa100bdlabelOPSetting": oa100bdlabelOPSetting,
       "oa100bduomOPSetting": oa100bduomOPSetting,
       "oa100bdmajorHighOPSetting": oa100bdmajorHighOPSetting,
       "oa100bdmajorLowOPSetting": oa100bdmajorLowOPSetting,
       "oa100bdminorHighOPSetting": oa100bdminorHighOPSetting,
       "oa100bdminorLowOPSetting": oa100bdminorLowOPSetting,
       "oa100bdcurrentValueOPSetting": oa100bdcurrentValueOPSetting,
       "oa100bdstateFlagOPSetting": oa100bdstateFlagOPSetting,
       "oa100bdminValueOPSetting": oa100bdminValueOPSetting,
       "oa100bdmaxValueOPSetting": oa100bdmaxValueOPSetting,
       "oa100bdalarmStateOPSetting": oa100bdalarmStateOPSetting,
       "oa100bdlabelLPSetting": oa100bdlabelLPSetting,
       "oa100bduomLPSetting": oa100bduomLPSetting,
       "oa100bdmajorHighLPSetting": oa100bdmajorHighLPSetting,
       "oa100bdmajorLowLPSetting": oa100bdmajorLowLPSetting,
       "oa100bdminorHighLPSetting": oa100bdminorHighLPSetting,
       "oa100bdminorLowLPSetting": oa100bdminorLowLPSetting,
       "oa100bdcurrentValueLPSetting": oa100bdcurrentValueLPSetting,
       "oa100bdstateFlagLPSetting": oa100bdstateFlagLPSetting,
       "oa100bdminValueLPSetting": oa100bdminValueLPSetting,
       "oa100bdmaxValueLPSetting": oa100bdmaxValueLPSetting,
       "oa100bdalarmStateLPSetting": oa100bdalarmStateLPSetting,
       "oa100bdlabelCGSetting": oa100bdlabelCGSetting,
       "oa100bduomCGSetting": oa100bduomCGSetting,
       "oa100bdmajorHighCGSetting": oa100bdmajorHighCGSetting,
       "oa100bdmajorLowCGSetting": oa100bdmajorLowCGSetting,
       "oa100bdminorHighCGSetting": oa100bdminorHighCGSetting,
       "oa100bdminorLowCGSetting": oa100bdminorLowCGSetting,
       "oa100bdcurrentValueCGSetting": oa100bdcurrentValueCGSetting,
       "oa100bdstateFlagCGSetting": oa100bdstateFlagCGSetting,
       "oa100bdminValueCGSetting": oa100bdminValueCGSetting,
       "oa100bdmaxValueCGSetting": oa100bdmaxValueCGSetting,
       "oa100bdalarmStateCGSetting": oa100bdalarmStateCGSetting,
       "oa100bdlabelOptThreshold": oa100bdlabelOptThreshold,
       "oa100bduomOptThreshold": oa100bduomOptThreshold,
       "oa100bdmajorHighOptThreshold": oa100bdmajorHighOptThreshold,
       "oa100bdmajorLowOptThreshold": oa100bdmajorLowOptThreshold,
       "oa100bdminorHighOptThreshold": oa100bdminorHighOptThreshold,
       "oa100bdminorLowOptThreshold": oa100bdminorLowOptThreshold,
       "oa100bdcurrentValueOptThreshold": oa100bdcurrentValueOptThreshold,
       "oa100bdstateFlagOptThreshold": oa100bdstateFlagOptThreshold,
       "oa100bdminValueOptThreshold": oa100bdminValueOptThreshold,
       "oa100bdmaxValueOptThreshold": oa100bdmaxValueOptThreshold,
       "oa100bdalarmStateOptThreshold": oa100bdalarmStateOptThreshold,
       "gx2OA100BDDigitalTable": gx2OA100BDDigitalTable,
       "gx2OA100BDDigitalEntry": gx2OA100BDDigitalEntry,
       "gx2OA100BDDigitalTableIndex": gx2OA100BDDigitalTableIndex,
       "oa100bdlabelModeSetting": oa100bdlabelModeSetting,
       "oa100bdenumModeSetting": oa100bdenumModeSetting,
       "oa100bdvalueModeSetting": oa100bdvalueModeSetting,
       "oa100bdstateFlagModeSetting": oa100bdstateFlagModeSetting,
       "oa100bdlabelModuleState": oa100bdlabelModuleState,
       "oa100bdenumModuleState": oa100bdenumModuleState,
       "oa100bdvalueModuleState": oa100bdvalueModuleState,
       "oa100bdstateFlagModuleState": oa100bdstateFlagModuleState,
       "oa100bdlabelFactoryDefault": oa100bdlabelFactoryDefault,
       "oa100bdenumFactoryDefault": oa100bdenumFactoryDefault,
       "oa100bdvalueFactoryDefault": oa100bdvalueFactoryDefault,
       "oa100bdstateFlagFactoryDefault": oa100bdstateFlagFactoryDefault,
       "gx2OA100BDStatusTable": gx2OA100BDStatusTable,
       "gx2OA100BDStatusEntry": gx2OA100BDStatusEntry,
       "gx2OA100BDStatusTableIndex": gx2OA100BDStatusTableIndex,
       "oa100bdlabelBoot": oa100bdlabelBoot,
       "oa100bdvalueBoot": oa100bdvalueBoot,
       "oa100bdstateflagBoot": oa100bdstateflagBoot,
       "oa100bdlabelFlash": oa100bdlabelFlash,
       "oa100bdvalueFlash": oa100bdvalueFlash,
       "oa100bdstateflagFlash": oa100bdstateflagFlash,
       "oa100bdlabelFactoryDataCRC": oa100bdlabelFactoryDataCRC,
       "oa100bdvalueFactoryDataCRC": oa100bdvalueFactoryDataCRC,
       "oa100bdstateflagFactoryDataCRC": oa100bdstateflagFactoryDataCRC,
       "oa100bdlabelAlarmDataCRC": oa100bdlabelAlarmDataCRC,
       "oa100bdvalueAlarmDataCRC": oa100bdvalueAlarmDataCRC,
       "oa100bdstateflagAlarmDataCRC": oa100bdstateflagAlarmDataCRC,
       "oa100bdlabelCalibrationDataCRC": oa100bdlabelCalibrationDataCRC,
       "oa100bdvalueCalibrationDataCRC": oa100bdvalueCalibrationDataCRC,
       "oa100bdstateflagCalibrationDataCRC": oa100bdstateflagCalibrationDataCRC,
       "oa100bdlabelOptInShutdown": oa100bdlabelOptInShutdown,
       "oa100bdvalueOptInShutdown": oa100bdvalueOptInShutdown,
       "oa100bdstateflagOptInShutdown": oa100bdstateflagOptInShutdown,
       "oa100bdlabelMainTECTempShutdown": oa100bdlabelMainTECTempShutdown,
       "oa100bdvalueMainTECTempShutdown": oa100bdvalueMainTECTempShutdown,
       "oa100bdstateflagMainTECTempShutdown": oa100bdstateflagMainTECTempShutdown,
       "oa100bdlabelAuxTECTempShutdown": oa100bdlabelAuxTECTempShutdown,
       "oa100bdvalueAuxTECTempShutdown": oa100bdvalueAuxTECTempShutdown,
       "oa100bdstateflagAuxTECTempShutdown": oa100bdstateflagAuxTECTempShutdown,
       "oa100bdlabelPowerFail": oa100bdlabelPowerFail,
       "oa100bdvaluePowerFail": oa100bdvaluePowerFail,
       "oa100bdstateflagPowerFail": oa100bdstateflagPowerFail,
       "oa100bdlabelKeySwitch": oa100bdlabelKeySwitch,
       "oa100bdvalueKeySwitch": oa100bdvalueKeySwitch,
       "oa100bdstateflagKeySwitch": oa100bdstateflagKeySwitch,
       "oa100bdlabelMainLaserCurrShutdown": oa100bdlabelMainLaserCurrShutdown,
       "oa100bdvalueMainLaserCurrShutdown": oa100bdvalueMainLaserCurrShutdown,
       "oa100bdstateflagMainLaserCurrShutdown": oa100bdstateflagMainLaserCurrShutdown,
       "oa100bdlabelAuxLaserCurrShutdown": oa100bdlabelAuxLaserCurrShutdown,
       "oa100bdvalueAuxLaserCurrShutdown": oa100bdvalueAuxLaserCurrShutdown,
       "oa100bdstateflagAuxLaserCurrShutdown": oa100bdstateflagAuxLaserCurrShutdown,
       "oa100bdlabelMainLaserPowShutdown": oa100bdlabelMainLaserPowShutdown,
       "oa100bdvalueMainLaserPowShutdown": oa100bdvalueMainLaserPowShutdown,
       "oa100bdstateflagMainLaserPowShutdown": oa100bdstateflagMainLaserPowShutdown,
       "oa100bdlabelAuxLaserPowShutdown": oa100bdlabelAuxLaserPowShutdown,
       "oa100bdvalueAuxLaserPowShutdown": oa100bdvalueAuxLaserPowShutdown,
       "oa100bdstateflagAuxLaserPowShutdown": oa100bdstateflagAuxLaserPowShutdown,
       "oa100bdlabelADCStatus": oa100bdlabelADCStatus,
       "oa100bdvalueADCStatus": oa100bdvalueADCStatus,
       "oa100bdstateflagADCStatus": oa100bdstateflagADCStatus,
       "oa100bdlabelConstGainStatus": oa100bdlabelConstGainStatus,
       "oa100bdvalueConstGainStatus": oa100bdvalueConstGainStatus,
       "oa100bdstateflagConstGainStatus": oa100bdstateflagConstGainStatus,
       "oa100bdlabelHardwareErrorStatus": oa100bdlabelHardwareErrorStatus,
       "oa100bdvalueHardwareErrorStatus": oa100bdvalueHardwareErrorStatus,
       "oa100bdstateflagHardwareErrorStatus": oa100bdstateflagHardwareErrorStatus,
       "oa100bdlabelStandbyStatus": oa100bdlabelStandbyStatus,
       "oa100bdvalueStandbyStatus": oa100bdvalueStandbyStatus,
       "oa100bdstateflagStandbyStatus": oa100bdstateflagStandbyStatus,
       "gx2OA100BDFactoryTable": gx2OA100BDFactoryTable,
       "gx2OA100BDFactoryEntry": gx2OA100BDFactoryEntry,
       "gx2OA100BDFactoryTableIndex": gx2OA100BDFactoryTableIndex,
       "oa100bdbootControlByte": oa100bdbootControlByte,
       "oa100bdbootStatusByte": oa100bdbootStatusByte,
       "oa100bdbank0CRC": oa100bdbank0CRC,
       "oa100bdbank1CRC": oa100bdbank1CRC,
       "oa100bdprgEEPROMByte": oa100bdprgEEPROMByte,
       "oa100bdfactoryCRC": oa100bdfactoryCRC,
       "oa100bdcalculateCRC": oa100bdcalculateCRC,
       "oa100bdhourMeter": oa100bdhourMeter,
       "oa100bdflashPrgCntA": oa100bdflashPrgCntA,
       "oa100bdflashPrgCntB": oa100bdflashPrgCntB,
       "oa100bdfwRev0": oa100bdfwRev0,
       "oa100bdfwRev1": oa100bdfwRev1,
       "gx2OA100BDHoldTimeTable": gx2OA100BDHoldTimeTable,
       "gx2OA100BDHoldTimeEntry": gx2OA100BDHoldTimeEntry,
       "gx2OA100BDHoldTimeTableIndex": gx2OA100BDHoldTimeTableIndex,
       "gx2OA100BDHoldTimeSpecIndex": gx2OA100BDHoldTimeSpecIndex,
       "gx2OA100BDHoldTimeData": gx2OA100BDHoldTimeData}
)
