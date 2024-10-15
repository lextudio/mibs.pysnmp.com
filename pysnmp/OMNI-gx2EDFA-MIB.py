# SNMP MIB module (OMNI-gx2EDFA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2EDFA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:19 2024
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

(gx2EDFA,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2EDFA")

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

_Gx2EDFADescriptor_ObjectIdentity = ObjectIdentity
gx2EDFADescriptor = _Gx2EDFADescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 1)
)
_Gx2EDFAAnalogTable_Object = MibTable
gx2EDFAAnalogTable = _Gx2EDFAAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    gx2EDFAAnalogTable.setStatus("mandatory")
_Gx2EDFAAnalogEntry_Object = MibTableRow
gx2EDFAAnalogEntry = _Gx2EDFAAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1)
)
gx2EDFAAnalogEntry.setIndexNames(
    (0, "OMNI-gx2EDFA-MIB", "edfagx2EDFAAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2EDFAAnalogEntry.setStatus("mandatory")


class _Edfagx2EDFAAnalogTableIndex_Type(Integer32):
    """Custom type edfagx2EDFAAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Edfagx2EDFAAnalogTableIndex_Type.__name__ = "Integer32"
_Edfagx2EDFAAnalogTableIndex_Object = MibTableColumn
edfagx2EDFAAnalogTableIndex = _Edfagx2EDFAAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 1),
    _Edfagx2EDFAAnalogTableIndex_Type()
)
edfagx2EDFAAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfagx2EDFAAnalogTableIndex.setStatus("mandatory")


class _EdfalabelModTemp_Type(DisplayString):
    """Custom type edfalabelModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelModTemp_Type.__name__ = "DisplayString"
_EdfalabelModTemp_Object = MibTableColumn
edfalabelModTemp = _EdfalabelModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 2),
    _EdfalabelModTemp_Type()
)
edfalabelModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelModTemp.setStatus("optional")


class _EdfauomModTemp_Type(DisplayString):
    """Custom type edfauomModTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomModTemp_Type.__name__ = "DisplayString"
_EdfauomModTemp_Object = MibTableColumn
edfauomModTemp = _EdfauomModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 3),
    _EdfauomModTemp_Type()
)
edfauomModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomModTemp.setStatus("optional")
_EdfamajorHighModTemp_Type = Float
_EdfamajorHighModTemp_Object = MibTableColumn
edfamajorHighModTemp = _EdfamajorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 4),
    _EdfamajorHighModTemp_Type()
)
edfamajorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighModTemp.setStatus("mandatory")
_EdfamajorLowModTemp_Type = Float
_EdfamajorLowModTemp_Object = MibTableColumn
edfamajorLowModTemp = _EdfamajorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 5),
    _EdfamajorLowModTemp_Type()
)
edfamajorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowModTemp.setStatus("mandatory")
_EdfaminorHighModTemp_Type = Float
_EdfaminorHighModTemp_Object = MibTableColumn
edfaminorHighModTemp = _EdfaminorHighModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 6),
    _EdfaminorHighModTemp_Type()
)
edfaminorHighModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighModTemp.setStatus("mandatory")
_EdfaminorLowModTemp_Type = Float
_EdfaminorLowModTemp_Object = MibTableColumn
edfaminorLowModTemp = _EdfaminorLowModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 7),
    _EdfaminorLowModTemp_Type()
)
edfaminorLowModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowModTemp.setStatus("mandatory")
_EdfacurrentValueModTemp_Type = Float
_EdfacurrentValueModTemp_Object = MibTableColumn
edfacurrentValueModTemp = _EdfacurrentValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 8),
    _EdfacurrentValueModTemp_Type()
)
edfacurrentValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValueModTemp.setStatus("mandatory")


class _EdfastateFlagModTemp_Type(Integer32):
    """Custom type edfastateFlagModTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagModTemp_Type.__name__ = "Integer32"
_EdfastateFlagModTemp_Object = MibTableColumn
edfastateFlagModTemp = _EdfastateFlagModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 9),
    _EdfastateFlagModTemp_Type()
)
edfastateFlagModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagModTemp.setStatus("mandatory")
_EdfaminValueModTemp_Type = Float
_EdfaminValueModTemp_Object = MibTableColumn
edfaminValueModTemp = _EdfaminValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 10),
    _EdfaminValueModTemp_Type()
)
edfaminValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueModTemp.setStatus("mandatory")
_EdfamaxValueModTemp_Type = Float
_EdfamaxValueModTemp_Object = MibTableColumn
edfamaxValueModTemp = _EdfamaxValueModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 11),
    _EdfamaxValueModTemp_Type()
)
edfamaxValueModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueModTemp.setStatus("mandatory")


class _EdfaalarmStateModTemp_Type(Integer32):
    """Custom type edfaalarmStateModTemp based on Integer32"""
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


_EdfaalarmStateModTemp_Type.__name__ = "Integer32"
_EdfaalarmStateModTemp_Object = MibTableColumn
edfaalarmStateModTemp = _EdfaalarmStateModTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 12),
    _EdfaalarmStateModTemp_Type()
)
edfaalarmStateModTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateModTemp.setStatus("mandatory")


class _EdfalabelOptInPower_Type(DisplayString):
    """Custom type edfalabelOptInPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelOptInPower_Type.__name__ = "DisplayString"
_EdfalabelOptInPower_Object = MibTableColumn
edfalabelOptInPower = _EdfalabelOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 13),
    _EdfalabelOptInPower_Type()
)
edfalabelOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelOptInPower.setStatus("optional")


class _EdfauomOptInPower_Type(DisplayString):
    """Custom type edfauomOptInPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomOptInPower_Type.__name__ = "DisplayString"
_EdfauomOptInPower_Object = MibTableColumn
edfauomOptInPower = _EdfauomOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 14),
    _EdfauomOptInPower_Type()
)
edfauomOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomOptInPower.setStatus("optional")
_EdfamajorHighOptInPower_Type = Float
_EdfamajorHighOptInPower_Object = MibTableColumn
edfamajorHighOptInPower = _EdfamajorHighOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 15),
    _EdfamajorHighOptInPower_Type()
)
edfamajorHighOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighOptInPower.setStatus("mandatory")
_EdfamajorLowOptInPower_Type = Float
_EdfamajorLowOptInPower_Object = MibTableColumn
edfamajorLowOptInPower = _EdfamajorLowOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 16),
    _EdfamajorLowOptInPower_Type()
)
edfamajorLowOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowOptInPower.setStatus("mandatory")
_EdfaminorHighOptInPower_Type = Float
_EdfaminorHighOptInPower_Object = MibTableColumn
edfaminorHighOptInPower = _EdfaminorHighOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 17),
    _EdfaminorHighOptInPower_Type()
)
edfaminorHighOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighOptInPower.setStatus("mandatory")
_EdfaminorLowOptInPower_Type = Float
_EdfaminorLowOptInPower_Object = MibTableColumn
edfaminorLowOptInPower = _EdfaminorLowOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 18),
    _EdfaminorLowOptInPower_Type()
)
edfaminorLowOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowOptInPower.setStatus("mandatory")
_EdfacurrentValueOptInPower_Type = Float
_EdfacurrentValueOptInPower_Object = MibTableColumn
edfacurrentValueOptInPower = _EdfacurrentValueOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 19),
    _EdfacurrentValueOptInPower_Type()
)
edfacurrentValueOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValueOptInPower.setStatus("mandatory")


class _EdfastateFlagOptInPower_Type(Integer32):
    """Custom type edfastateFlagOptInPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagOptInPower_Type.__name__ = "Integer32"
_EdfastateFlagOptInPower_Object = MibTableColumn
edfastateFlagOptInPower = _EdfastateFlagOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 20),
    _EdfastateFlagOptInPower_Type()
)
edfastateFlagOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagOptInPower.setStatus("mandatory")
_EdfaminValueOptInPower_Type = Float
_EdfaminValueOptInPower_Object = MibTableColumn
edfaminValueOptInPower = _EdfaminValueOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 21),
    _EdfaminValueOptInPower_Type()
)
edfaminValueOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueOptInPower.setStatus("mandatory")
_EdfamaxValueOptInPower_Type = Float
_EdfamaxValueOptInPower_Object = MibTableColumn
edfamaxValueOptInPower = _EdfamaxValueOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 22),
    _EdfamaxValueOptInPower_Type()
)
edfamaxValueOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueOptInPower.setStatus("mandatory")


class _EdfaalarmStateOptInPower_Type(Integer32):
    """Custom type edfaalarmStateOptInPower based on Integer32"""
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


_EdfaalarmStateOptInPower_Type.__name__ = "Integer32"
_EdfaalarmStateOptInPower_Object = MibTableColumn
edfaalarmStateOptInPower = _EdfaalarmStateOptInPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 23),
    _EdfaalarmStateOptInPower_Type()
)
edfaalarmStateOptInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateOptInPower.setStatus("mandatory")


class _EdfalabelOptOutPower_Type(DisplayString):
    """Custom type edfalabelOptOutPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelOptOutPower_Type.__name__ = "DisplayString"
_EdfalabelOptOutPower_Object = MibTableColumn
edfalabelOptOutPower = _EdfalabelOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 24),
    _EdfalabelOptOutPower_Type()
)
edfalabelOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelOptOutPower.setStatus("optional")


class _EdfauomOptOutPower_Type(DisplayString):
    """Custom type edfauomOptOutPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomOptOutPower_Type.__name__ = "DisplayString"
_EdfauomOptOutPower_Object = MibTableColumn
edfauomOptOutPower = _EdfauomOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 25),
    _EdfauomOptOutPower_Type()
)
edfauomOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomOptOutPower.setStatus("optional")
_EdfamajorHighOptOutPower_Type = Float
_EdfamajorHighOptOutPower_Object = MibTableColumn
edfamajorHighOptOutPower = _EdfamajorHighOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 26),
    _EdfamajorHighOptOutPower_Type()
)
edfamajorHighOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighOptOutPower.setStatus("mandatory")
_EdfamajorLowOptOutPower_Type = Float
_EdfamajorLowOptOutPower_Object = MibTableColumn
edfamajorLowOptOutPower = _EdfamajorLowOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 27),
    _EdfamajorLowOptOutPower_Type()
)
edfamajorLowOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowOptOutPower.setStatus("mandatory")
_EdfaminorHighOptOutPower_Type = Float
_EdfaminorHighOptOutPower_Object = MibTableColumn
edfaminorHighOptOutPower = _EdfaminorHighOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 28),
    _EdfaminorHighOptOutPower_Type()
)
edfaminorHighOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighOptOutPower.setStatus("mandatory")
_EdfaminorLowOptOutPower_Type = Float
_EdfaminorLowOptOutPower_Object = MibTableColumn
edfaminorLowOptOutPower = _EdfaminorLowOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 29),
    _EdfaminorLowOptOutPower_Type()
)
edfaminorLowOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowOptOutPower.setStatus("mandatory")
_EdfacurrentValueOptOutPower_Type = Float
_EdfacurrentValueOptOutPower_Object = MibTableColumn
edfacurrentValueOptOutPower = _EdfacurrentValueOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 30),
    _EdfacurrentValueOptOutPower_Type()
)
edfacurrentValueOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValueOptOutPower.setStatus("mandatory")


class _EdfastateFlagOptOutPower_Type(Integer32):
    """Custom type edfastateFlagOptOutPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagOptOutPower_Type.__name__ = "Integer32"
_EdfastateFlagOptOutPower_Object = MibTableColumn
edfastateFlagOptOutPower = _EdfastateFlagOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 31),
    _EdfastateFlagOptOutPower_Type()
)
edfastateFlagOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagOptOutPower.setStatus("mandatory")
_EdfaminValueOptOutPower_Type = Float
_EdfaminValueOptOutPower_Object = MibTableColumn
edfaminValueOptOutPower = _EdfaminValueOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 32),
    _EdfaminValueOptOutPower_Type()
)
edfaminValueOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueOptOutPower.setStatus("mandatory")
_EdfamaxValueOptOutPower_Type = Float
_EdfamaxValueOptOutPower_Object = MibTableColumn
edfamaxValueOptOutPower = _EdfamaxValueOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 33),
    _EdfamaxValueOptOutPower_Type()
)
edfamaxValueOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueOptOutPower.setStatus("mandatory")


class _EdfaalarmStateOptOutPower_Type(Integer32):
    """Custom type edfaalarmStateOptOutPower based on Integer32"""
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


_EdfaalarmStateOptOutPower_Type.__name__ = "Integer32"
_EdfaalarmStateOptOutPower_Object = MibTableColumn
edfaalarmStateOptOutPower = _EdfaalarmStateOptOutPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 34),
    _EdfaalarmStateOptOutPower_Type()
)
edfaalarmStateOptOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateOptOutPower.setStatus("mandatory")


class _EdfalabelTECTemp_Type(DisplayString):
    """Custom type edfalabelTECTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelTECTemp_Type.__name__ = "DisplayString"
_EdfalabelTECTemp_Object = MibTableColumn
edfalabelTECTemp = _EdfalabelTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 35),
    _EdfalabelTECTemp_Type()
)
edfalabelTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelTECTemp.setStatus("optional")


class _EdfauomTECTemp_Type(DisplayString):
    """Custom type edfauomTECTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomTECTemp_Type.__name__ = "DisplayString"
_EdfauomTECTemp_Object = MibTableColumn
edfauomTECTemp = _EdfauomTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 36),
    _EdfauomTECTemp_Type()
)
edfauomTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomTECTemp.setStatus("optional")
_EdfamajorHighTECTemp_Type = Float
_EdfamajorHighTECTemp_Object = MibTableColumn
edfamajorHighTECTemp = _EdfamajorHighTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 37),
    _EdfamajorHighTECTemp_Type()
)
edfamajorHighTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighTECTemp.setStatus("mandatory")
_EdfamajorLowTECTemp_Type = Float
_EdfamajorLowTECTemp_Object = MibTableColumn
edfamajorLowTECTemp = _EdfamajorLowTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 38),
    _EdfamajorLowTECTemp_Type()
)
edfamajorLowTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowTECTemp.setStatus("mandatory")
_EdfaminorHighTECTemp_Type = Float
_EdfaminorHighTECTemp_Object = MibTableColumn
edfaminorHighTECTemp = _EdfaminorHighTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 39),
    _EdfaminorHighTECTemp_Type()
)
edfaminorHighTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighTECTemp.setStatus("mandatory")
_EdfaminorLowTECTemp_Type = Float
_EdfaminorLowTECTemp_Object = MibTableColumn
edfaminorLowTECTemp = _EdfaminorLowTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 40),
    _EdfaminorLowTECTemp_Type()
)
edfaminorLowTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowTECTemp.setStatus("mandatory")
_EdfacurrentValueTECTemp_Type = Float
_EdfacurrentValueTECTemp_Object = MibTableColumn
edfacurrentValueTECTemp = _EdfacurrentValueTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 41),
    _EdfacurrentValueTECTemp_Type()
)
edfacurrentValueTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValueTECTemp.setStatus("mandatory")


class _EdfastateFlagTECTemp_Type(Integer32):
    """Custom type edfastateFlagTECTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagTECTemp_Type.__name__ = "Integer32"
_EdfastateFlagTECTemp_Object = MibTableColumn
edfastateFlagTECTemp = _EdfastateFlagTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 42),
    _EdfastateFlagTECTemp_Type()
)
edfastateFlagTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagTECTemp.setStatus("mandatory")
_EdfaminValueTECTemp_Type = Float
_EdfaminValueTECTemp_Object = MibTableColumn
edfaminValueTECTemp = _EdfaminValueTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 43),
    _EdfaminValueTECTemp_Type()
)
edfaminValueTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueTECTemp.setStatus("mandatory")
_EdfamaxValueTECTemp_Type = Float
_EdfamaxValueTECTemp_Object = MibTableColumn
edfamaxValueTECTemp = _EdfamaxValueTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 44),
    _EdfamaxValueTECTemp_Type()
)
edfamaxValueTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueTECTemp.setStatus("mandatory")


class _EdfaalarmStateTECTemp_Type(Integer32):
    """Custom type edfaalarmStateTECTemp based on Integer32"""
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


_EdfaalarmStateTECTemp_Type.__name__ = "Integer32"
_EdfaalarmStateTECTemp_Object = MibTableColumn
edfaalarmStateTECTemp = _EdfaalarmStateTECTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 45),
    _EdfaalarmStateTECTemp_Type()
)
edfaalarmStateTECTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateTECTemp.setStatus("mandatory")


class _EdfalabelTECCurrent_Type(DisplayString):
    """Custom type edfalabelTECCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelTECCurrent_Type.__name__ = "DisplayString"
_EdfalabelTECCurrent_Object = MibTableColumn
edfalabelTECCurrent = _EdfalabelTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 46),
    _EdfalabelTECCurrent_Type()
)
edfalabelTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelTECCurrent.setStatus("optional")


class _EdfauomTECCurrent_Type(DisplayString):
    """Custom type edfauomTECCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomTECCurrent_Type.__name__ = "DisplayString"
_EdfauomTECCurrent_Object = MibTableColumn
edfauomTECCurrent = _EdfauomTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 47),
    _EdfauomTECCurrent_Type()
)
edfauomTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomTECCurrent.setStatus("optional")
_EdfamajorHighTECCurrent_Type = Float
_EdfamajorHighTECCurrent_Object = MibTableColumn
edfamajorHighTECCurrent = _EdfamajorHighTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 48),
    _EdfamajorHighTECCurrent_Type()
)
edfamajorHighTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighTECCurrent.setStatus("mandatory")
_EdfamajorLowTECCurrent_Type = Float
_EdfamajorLowTECCurrent_Object = MibTableColumn
edfamajorLowTECCurrent = _EdfamajorLowTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 49),
    _EdfamajorLowTECCurrent_Type()
)
edfamajorLowTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowTECCurrent.setStatus("mandatory")
_EdfaminorHighTECCurrent_Type = Float
_EdfaminorHighTECCurrent_Object = MibTableColumn
edfaminorHighTECCurrent = _EdfaminorHighTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 50),
    _EdfaminorHighTECCurrent_Type()
)
edfaminorHighTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighTECCurrent.setStatus("mandatory")
_EdfaminorLowTECCurrent_Type = Float
_EdfaminorLowTECCurrent_Object = MibTableColumn
edfaminorLowTECCurrent = _EdfaminorLowTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 51),
    _EdfaminorLowTECCurrent_Type()
)
edfaminorLowTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowTECCurrent.setStatus("mandatory")
_EdfacurrentValueTECCurrent_Type = Float
_EdfacurrentValueTECCurrent_Object = MibTableColumn
edfacurrentValueTECCurrent = _EdfacurrentValueTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 52),
    _EdfacurrentValueTECCurrent_Type()
)
edfacurrentValueTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValueTECCurrent.setStatus("mandatory")


class _EdfastateFlagTECCurrent_Type(Integer32):
    """Custom type edfastateFlagTECCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagTECCurrent_Type.__name__ = "Integer32"
_EdfastateFlagTECCurrent_Object = MibTableColumn
edfastateFlagTECCurrent = _EdfastateFlagTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 53),
    _EdfastateFlagTECCurrent_Type()
)
edfastateFlagTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagTECCurrent.setStatus("mandatory")
_EdfaminValueTECCurrent_Type = Float
_EdfaminValueTECCurrent_Object = MibTableColumn
edfaminValueTECCurrent = _EdfaminValueTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 54),
    _EdfaminValueTECCurrent_Type()
)
edfaminValueTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueTECCurrent.setStatus("mandatory")
_EdfamaxValueTECCurrent_Type = Float
_EdfamaxValueTECCurrent_Object = MibTableColumn
edfamaxValueTECCurrent = _EdfamaxValueTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 55),
    _EdfamaxValueTECCurrent_Type()
)
edfamaxValueTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueTECCurrent.setStatus("mandatory")


class _EdfaalarmStateTECCurrent_Type(Integer32):
    """Custom type edfaalarmStateTECCurrent based on Integer32"""
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


_EdfaalarmStateTECCurrent_Type.__name__ = "Integer32"
_EdfaalarmStateTECCurrent_Object = MibTableColumn
edfaalarmStateTECCurrent = _EdfaalarmStateTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 56),
    _EdfaalarmStateTECCurrent_Type()
)
edfaalarmStateTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateTECCurrent.setStatus("mandatory")


class _EdfalabelLaserCurrent_Type(DisplayString):
    """Custom type edfalabelLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelLaserCurrent_Type.__name__ = "DisplayString"
_EdfalabelLaserCurrent_Object = MibTableColumn
edfalabelLaserCurrent = _EdfalabelLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 57),
    _EdfalabelLaserCurrent_Type()
)
edfalabelLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelLaserCurrent.setStatus("optional")


class _EdfauomLaserCurrent_Type(DisplayString):
    """Custom type edfauomLaserCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomLaserCurrent_Type.__name__ = "DisplayString"
_EdfauomLaserCurrent_Object = MibTableColumn
edfauomLaserCurrent = _EdfauomLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 58),
    _EdfauomLaserCurrent_Type()
)
edfauomLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomLaserCurrent.setStatus("optional")
_EdfamajorHighLaserCurrent_Type = Float
_EdfamajorHighLaserCurrent_Object = MibTableColumn
edfamajorHighLaserCurrent = _EdfamajorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 59),
    _EdfamajorHighLaserCurrent_Type()
)
edfamajorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighLaserCurrent.setStatus("mandatory")
_EdfamajorLowLaserCurrent_Type = Float
_EdfamajorLowLaserCurrent_Object = MibTableColumn
edfamajorLowLaserCurrent = _EdfamajorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 60),
    _EdfamajorLowLaserCurrent_Type()
)
edfamajorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowLaserCurrent.setStatus("mandatory")
_EdfaminorHighLaserCurrent_Type = Float
_EdfaminorHighLaserCurrent_Object = MibTableColumn
edfaminorHighLaserCurrent = _EdfaminorHighLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 61),
    _EdfaminorHighLaserCurrent_Type()
)
edfaminorHighLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighLaserCurrent.setStatus("mandatory")
_EdfaminorLowLaserCurrent_Type = Float
_EdfaminorLowLaserCurrent_Object = MibTableColumn
edfaminorLowLaserCurrent = _EdfaminorLowLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 62),
    _EdfaminorLowLaserCurrent_Type()
)
edfaminorLowLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowLaserCurrent.setStatus("mandatory")
_EdfacurrentValueLaserCurrent_Type = Float
_EdfacurrentValueLaserCurrent_Object = MibTableColumn
edfacurrentValueLaserCurrent = _EdfacurrentValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 63),
    _EdfacurrentValueLaserCurrent_Type()
)
edfacurrentValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValueLaserCurrent.setStatus("mandatory")


class _EdfastateFlagLaserCurrent_Type(Integer32):
    """Custom type edfastateFlagLaserCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagLaserCurrent_Type.__name__ = "Integer32"
_EdfastateFlagLaserCurrent_Object = MibTableColumn
edfastateFlagLaserCurrent = _EdfastateFlagLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 64),
    _EdfastateFlagLaserCurrent_Type()
)
edfastateFlagLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagLaserCurrent.setStatus("mandatory")
_EdfaminValueLaserCurrent_Type = Float
_EdfaminValueLaserCurrent_Object = MibTableColumn
edfaminValueLaserCurrent = _EdfaminValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 65),
    _EdfaminValueLaserCurrent_Type()
)
edfaminValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueLaserCurrent.setStatus("mandatory")
_EdfamaxValueLaserCurrent_Type = Float
_EdfamaxValueLaserCurrent_Object = MibTableColumn
edfamaxValueLaserCurrent = _EdfamaxValueLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 66),
    _EdfamaxValueLaserCurrent_Type()
)
edfamaxValueLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueLaserCurrent.setStatus("mandatory")


class _EdfaalarmStateLaserCurrent_Type(Integer32):
    """Custom type edfaalarmStateLaserCurrent based on Integer32"""
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


_EdfaalarmStateLaserCurrent_Type.__name__ = "Integer32"
_EdfaalarmStateLaserCurrent_Object = MibTableColumn
edfaalarmStateLaserCurrent = _EdfaalarmStateLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 67),
    _EdfaalarmStateLaserCurrent_Type()
)
edfaalarmStateLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateLaserCurrent.setStatus("mandatory")


class _EdfalabelLaserPower_Type(DisplayString):
    """Custom type edfalabelLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelLaserPower_Type.__name__ = "DisplayString"
_EdfalabelLaserPower_Object = MibTableColumn
edfalabelLaserPower = _EdfalabelLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 68),
    _EdfalabelLaserPower_Type()
)
edfalabelLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelLaserPower.setStatus("optional")


class _EdfauomLaserPower_Type(DisplayString):
    """Custom type edfauomLaserPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomLaserPower_Type.__name__ = "DisplayString"
_EdfauomLaserPower_Object = MibTableColumn
edfauomLaserPower = _EdfauomLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 69),
    _EdfauomLaserPower_Type()
)
edfauomLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomLaserPower.setStatus("optional")
_EdfamajorHighLaserPower_Type = Float
_EdfamajorHighLaserPower_Object = MibTableColumn
edfamajorHighLaserPower = _EdfamajorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 70),
    _EdfamajorHighLaserPower_Type()
)
edfamajorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighLaserPower.setStatus("mandatory")
_EdfamajorLowLaserPower_Type = Float
_EdfamajorLowLaserPower_Object = MibTableColumn
edfamajorLowLaserPower = _EdfamajorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 71),
    _EdfamajorLowLaserPower_Type()
)
edfamajorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowLaserPower.setStatus("mandatory")
_EdfaminorHighLaserPower_Type = Float
_EdfaminorHighLaserPower_Object = MibTableColumn
edfaminorHighLaserPower = _EdfaminorHighLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 72),
    _EdfaminorHighLaserPower_Type()
)
edfaminorHighLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighLaserPower.setStatus("mandatory")
_EdfaminorLowLaserPower_Type = Float
_EdfaminorLowLaserPower_Object = MibTableColumn
edfaminorLowLaserPower = _EdfaminorLowLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 73),
    _EdfaminorLowLaserPower_Type()
)
edfaminorLowLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowLaserPower.setStatus("mandatory")
_EdfacurrentValueLaserPower_Type = Float
_EdfacurrentValueLaserPower_Object = MibTableColumn
edfacurrentValueLaserPower = _EdfacurrentValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 74),
    _EdfacurrentValueLaserPower_Type()
)
edfacurrentValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValueLaserPower.setStatus("mandatory")


class _EdfastateFlagLaserPower_Type(Integer32):
    """Custom type edfastateFlagLaserPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagLaserPower_Type.__name__ = "Integer32"
_EdfastateFlagLaserPower_Object = MibTableColumn
edfastateFlagLaserPower = _EdfastateFlagLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 75),
    _EdfastateFlagLaserPower_Type()
)
edfastateFlagLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagLaserPower.setStatus("mandatory")
_EdfaminValueLaserPower_Type = Float
_EdfaminValueLaserPower_Object = MibTableColumn
edfaminValueLaserPower = _EdfaminValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 76),
    _EdfaminValueLaserPower_Type()
)
edfaminValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueLaserPower.setStatus("mandatory")
_EdfamaxValueLaserPower_Type = Float
_EdfamaxValueLaserPower_Object = MibTableColumn
edfamaxValueLaserPower = _EdfamaxValueLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 77),
    _EdfamaxValueLaserPower_Type()
)
edfamaxValueLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueLaserPower.setStatus("mandatory")


class _EdfaalarmStateLaserPower_Type(Integer32):
    """Custom type edfaalarmStateLaserPower based on Integer32"""
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


_EdfaalarmStateLaserPower_Type.__name__ = "Integer32"
_EdfaalarmStateLaserPower_Object = MibTableColumn
edfaalarmStateLaserPower = _EdfaalarmStateLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 78),
    _EdfaalarmStateLaserPower_Type()
)
edfaalarmStateLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateLaserPower.setStatus("mandatory")


class _Edfalabel12Volt_Type(DisplayString):
    """Custom type edfalabel12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Edfalabel12Volt_Type.__name__ = "DisplayString"
_Edfalabel12Volt_Object = MibTableColumn
edfalabel12Volt = _Edfalabel12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 79),
    _Edfalabel12Volt_Type()
)
edfalabel12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabel12Volt.setStatus("optional")


class _Edfauom12Volt_Type(DisplayString):
    """Custom type edfauom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Edfauom12Volt_Type.__name__ = "DisplayString"
_Edfauom12Volt_Object = MibTableColumn
edfauom12Volt = _Edfauom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 80),
    _Edfauom12Volt_Type()
)
edfauom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauom12Volt.setStatus("optional")
_EdfamajorHigh12Volt_Type = Float
_EdfamajorHigh12Volt_Object = MibTableColumn
edfamajorHigh12Volt = _EdfamajorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 81),
    _EdfamajorHigh12Volt_Type()
)
edfamajorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHigh12Volt.setStatus("mandatory")
_EdfamajorLow12Volt_Type = Float
_EdfamajorLow12Volt_Object = MibTableColumn
edfamajorLow12Volt = _EdfamajorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 82),
    _EdfamajorLow12Volt_Type()
)
edfamajorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLow12Volt.setStatus("mandatory")
_EdfaminorHigh12Volt_Type = Float
_EdfaminorHigh12Volt_Object = MibTableColumn
edfaminorHigh12Volt = _EdfaminorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 83),
    _EdfaminorHigh12Volt_Type()
)
edfaminorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHigh12Volt.setStatus("mandatory")
_EdfaminorLow12Volt_Type = Float
_EdfaminorLow12Volt_Object = MibTableColumn
edfaminorLow12Volt = _EdfaminorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 84),
    _EdfaminorLow12Volt_Type()
)
edfaminorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLow12Volt.setStatus("mandatory")
_EdfacurrentValue12Volt_Type = Float
_EdfacurrentValue12Volt_Object = MibTableColumn
edfacurrentValue12Volt = _EdfacurrentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 85),
    _EdfacurrentValue12Volt_Type()
)
edfacurrentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValue12Volt.setStatus("mandatory")


class _EdfastateFlag12Volt_Type(Integer32):
    """Custom type edfastateFlag12Volt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlag12Volt_Type.__name__ = "Integer32"
_EdfastateFlag12Volt_Object = MibTableColumn
edfastateFlag12Volt = _EdfastateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 86),
    _EdfastateFlag12Volt_Type()
)
edfastateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlag12Volt.setStatus("mandatory")
_EdfaminValue12Volt_Type = Float
_EdfaminValue12Volt_Object = MibTableColumn
edfaminValue12Volt = _EdfaminValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 87),
    _EdfaminValue12Volt_Type()
)
edfaminValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValue12Volt.setStatus("mandatory")
_EdfamaxValue12Volt_Type = Float
_EdfamaxValue12Volt_Object = MibTableColumn
edfamaxValue12Volt = _EdfamaxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 88),
    _EdfamaxValue12Volt_Type()
)
edfamaxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValue12Volt.setStatus("mandatory")


class _EdfaalarmState12Volt_Type(Integer32):
    """Custom type edfaalarmState12Volt based on Integer32"""
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


_EdfaalarmState12Volt_Type.__name__ = "Integer32"
_EdfaalarmState12Volt_Object = MibTableColumn
edfaalarmState12Volt = _EdfaalarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 89),
    _EdfaalarmState12Volt_Type()
)
edfaalarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmState12Volt.setStatus("mandatory")


class _Edfalabel37Volt_Type(DisplayString):
    """Custom type edfalabel37Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Edfalabel37Volt_Type.__name__ = "DisplayString"
_Edfalabel37Volt_Object = MibTableColumn
edfalabel37Volt = _Edfalabel37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 90),
    _Edfalabel37Volt_Type()
)
edfalabel37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabel37Volt.setStatus("optional")


class _Edfauom37Volt_Type(DisplayString):
    """Custom type edfauom37Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Edfauom37Volt_Type.__name__ = "DisplayString"
_Edfauom37Volt_Object = MibTableColumn
edfauom37Volt = _Edfauom37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 91),
    _Edfauom37Volt_Type()
)
edfauom37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauom37Volt.setStatus("optional")
_EdfamajorHigh37Volt_Type = Float
_EdfamajorHigh37Volt_Object = MibTableColumn
edfamajorHigh37Volt = _EdfamajorHigh37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 92),
    _EdfamajorHigh37Volt_Type()
)
edfamajorHigh37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHigh37Volt.setStatus("mandatory")
_EdfamajorLow37Volt_Type = Float
_EdfamajorLow37Volt_Object = MibTableColumn
edfamajorLow37Volt = _EdfamajorLow37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 93),
    _EdfamajorLow37Volt_Type()
)
edfamajorLow37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLow37Volt.setStatus("mandatory")
_EdfaminorHigh37Volt_Type = Float
_EdfaminorHigh37Volt_Object = MibTableColumn
edfaminorHigh37Volt = _EdfaminorHigh37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 94),
    _EdfaminorHigh37Volt_Type()
)
edfaminorHigh37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHigh37Volt.setStatus("mandatory")
_EdfaminorLow37Volt_Type = Float
_EdfaminorLow37Volt_Object = MibTableColumn
edfaminorLow37Volt = _EdfaminorLow37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 95),
    _EdfaminorLow37Volt_Type()
)
edfaminorLow37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLow37Volt.setStatus("mandatory")
_EdfacurrentValue37Volt_Type = Float
_EdfacurrentValue37Volt_Object = MibTableColumn
edfacurrentValue37Volt = _EdfacurrentValue37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 96),
    _EdfacurrentValue37Volt_Type()
)
edfacurrentValue37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValue37Volt.setStatus("mandatory")


class _EdfastateFlag37Volt_Type(Integer32):
    """Custom type edfastateFlag37Volt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlag37Volt_Type.__name__ = "Integer32"
_EdfastateFlag37Volt_Object = MibTableColumn
edfastateFlag37Volt = _EdfastateFlag37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 97),
    _EdfastateFlag37Volt_Type()
)
edfastateFlag37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlag37Volt.setStatus("mandatory")
_EdfaminValue37Volt_Type = Float
_EdfaminValue37Volt_Object = MibTableColumn
edfaminValue37Volt = _EdfaminValue37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 98),
    _EdfaminValue37Volt_Type()
)
edfaminValue37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValue37Volt.setStatus("mandatory")
_EdfamaxValue37Volt_Type = Float
_EdfamaxValue37Volt_Object = MibTableColumn
edfamaxValue37Volt = _EdfamaxValue37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 99),
    _EdfamaxValue37Volt_Type()
)
edfamaxValue37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValue37Volt.setStatus("mandatory")


class _EdfaalarmState37Volt_Type(Integer32):
    """Custom type edfaalarmState37Volt based on Integer32"""
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


_EdfaalarmState37Volt_Type.__name__ = "Integer32"
_EdfaalarmState37Volt_Object = MibTableColumn
edfaalarmState37Volt = _EdfaalarmState37Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 100),
    _EdfaalarmState37Volt_Type()
)
edfaalarmState37Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmState37Volt.setStatus("mandatory")


class _EdfalabelFanCurrent_Type(DisplayString):
    """Custom type edfalabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelFanCurrent_Type.__name__ = "DisplayString"
_EdfalabelFanCurrent_Object = MibTableColumn
edfalabelFanCurrent = _EdfalabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 101),
    _EdfalabelFanCurrent_Type()
)
edfalabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelFanCurrent.setStatus("optional")


class _EdfauomFanCurrent_Type(DisplayString):
    """Custom type edfauomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomFanCurrent_Type.__name__ = "DisplayString"
_EdfauomFanCurrent_Object = MibTableColumn
edfauomFanCurrent = _EdfauomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 102),
    _EdfauomFanCurrent_Type()
)
edfauomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomFanCurrent.setStatus("optional")
_EdfamajorHighFanCurrent_Type = Float
_EdfamajorHighFanCurrent_Object = MibTableColumn
edfamajorHighFanCurrent = _EdfamajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 103),
    _EdfamajorHighFanCurrent_Type()
)
edfamajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighFanCurrent.setStatus("mandatory")
_EdfamajorLowFanCurrent_Type = Float
_EdfamajorLowFanCurrent_Object = MibTableColumn
edfamajorLowFanCurrent = _EdfamajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 104),
    _EdfamajorLowFanCurrent_Type()
)
edfamajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowFanCurrent.setStatus("mandatory")
_EdfaminorHighFanCurrent_Type = Float
_EdfaminorHighFanCurrent_Object = MibTableColumn
edfaminorHighFanCurrent = _EdfaminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 105),
    _EdfaminorHighFanCurrent_Type()
)
edfaminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighFanCurrent.setStatus("mandatory")
_EdfaminorLowFanCurrent_Type = Float
_EdfaminorLowFanCurrent_Object = MibTableColumn
edfaminorLowFanCurrent = _EdfaminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 106),
    _EdfaminorLowFanCurrent_Type()
)
edfaminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowFanCurrent.setStatus("mandatory")
_EdfacurrentValueFanCurrent_Type = Float
_EdfacurrentValueFanCurrent_Object = MibTableColumn
edfacurrentValueFanCurrent = _EdfacurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 107),
    _EdfacurrentValueFanCurrent_Type()
)
edfacurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacurrentValueFanCurrent.setStatus("mandatory")


class _EdfastateFlagFanCurrent_Type(Integer32):
    """Custom type edfastateFlagFanCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagFanCurrent_Type.__name__ = "Integer32"
_EdfastateFlagFanCurrent_Object = MibTableColumn
edfastateFlagFanCurrent = _EdfastateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 108),
    _EdfastateFlagFanCurrent_Type()
)
edfastateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagFanCurrent.setStatus("mandatory")
_EdfaminValueFanCurrent_Type = Float
_EdfaminValueFanCurrent_Object = MibTableColumn
edfaminValueFanCurrent = _EdfaminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 109),
    _EdfaminValueFanCurrent_Type()
)
edfaminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueFanCurrent.setStatus("mandatory")
_EdfamaxValueFanCurrent_Type = Float
_EdfamaxValueFanCurrent_Object = MibTableColumn
edfamaxValueFanCurrent = _EdfamaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 110),
    _EdfamaxValueFanCurrent_Type()
)
edfamaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueFanCurrent.setStatus("mandatory")


class _EdfaalarmStateFanCurrent_Type(Integer32):
    """Custom type edfaalarmStateFanCurrent based on Integer32"""
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


_EdfaalarmStateFanCurrent_Type.__name__ = "Integer32"
_EdfaalarmStateFanCurrent_Object = MibTableColumn
edfaalarmStateFanCurrent = _EdfaalarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 111),
    _EdfaalarmStateFanCurrent_Type()
)
edfaalarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateFanCurrent.setStatus("mandatory")


class _EdfalabelOPSetting_Type(DisplayString):
    """Custom type edfalabelOPSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelOPSetting_Type.__name__ = "DisplayString"
_EdfalabelOPSetting_Object = MibTableColumn
edfalabelOPSetting = _EdfalabelOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 112),
    _EdfalabelOPSetting_Type()
)
edfalabelOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelOPSetting.setStatus("optional")


class _EdfauomOPSetting_Type(DisplayString):
    """Custom type edfauomOPSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomOPSetting_Type.__name__ = "DisplayString"
_EdfauomOPSetting_Object = MibTableColumn
edfauomOPSetting = _EdfauomOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 113),
    _EdfauomOPSetting_Type()
)
edfauomOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomOPSetting.setStatus("optional")
_EdfamajorHighOPSetting_Type = Float
_EdfamajorHighOPSetting_Object = MibTableColumn
edfamajorHighOPSetting = _EdfamajorHighOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 114),
    _EdfamajorHighOPSetting_Type()
)
edfamajorHighOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighOPSetting.setStatus("mandatory")
_EdfamajorLowOPSetting_Type = Float
_EdfamajorLowOPSetting_Object = MibTableColumn
edfamajorLowOPSetting = _EdfamajorLowOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 115),
    _EdfamajorLowOPSetting_Type()
)
edfamajorLowOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowOPSetting.setStatus("mandatory")
_EdfaminorHighOPSetting_Type = Float
_EdfaminorHighOPSetting_Object = MibTableColumn
edfaminorHighOPSetting = _EdfaminorHighOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 116),
    _EdfaminorHighOPSetting_Type()
)
edfaminorHighOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighOPSetting.setStatus("mandatory")
_EdfaminorLowOPSetting_Type = Float
_EdfaminorLowOPSetting_Object = MibTableColumn
edfaminorLowOPSetting = _EdfaminorLowOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 117),
    _EdfaminorLowOPSetting_Type()
)
edfaminorLowOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowOPSetting.setStatus("mandatory")
_EdfacurrentValueOPSetting_Type = Float
_EdfacurrentValueOPSetting_Object = MibTableColumn
edfacurrentValueOPSetting = _EdfacurrentValueOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 118),
    _EdfacurrentValueOPSetting_Type()
)
edfacurrentValueOPSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfacurrentValueOPSetting.setStatus("mandatory")


class _EdfastateFlagOPSetting_Type(Integer32):
    """Custom type edfastateFlagOPSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagOPSetting_Type.__name__ = "Integer32"
_EdfastateFlagOPSetting_Object = MibTableColumn
edfastateFlagOPSetting = _EdfastateFlagOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 119),
    _EdfastateFlagOPSetting_Type()
)
edfastateFlagOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagOPSetting.setStatus("mandatory")
_EdfaminValueOPSetting_Type = Float
_EdfaminValueOPSetting_Object = MibTableColumn
edfaminValueOPSetting = _EdfaminValueOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 120),
    _EdfaminValueOPSetting_Type()
)
edfaminValueOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueOPSetting.setStatus("mandatory")
_EdfamaxValueOPSetting_Type = Float
_EdfamaxValueOPSetting_Object = MibTableColumn
edfamaxValueOPSetting = _EdfamaxValueOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 121),
    _EdfamaxValueOPSetting_Type()
)
edfamaxValueOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueOPSetting.setStatus("mandatory")


class _EdfaalarmStateOPSetting_Type(Integer32):
    """Custom type edfaalarmStateOPSetting based on Integer32"""
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


_EdfaalarmStateOPSetting_Type.__name__ = "Integer32"
_EdfaalarmStateOPSetting_Object = MibTableColumn
edfaalarmStateOPSetting = _EdfaalarmStateOPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 122),
    _EdfaalarmStateOPSetting_Type()
)
edfaalarmStateOPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateOPSetting.setStatus("mandatory")


class _EdfalabelLPSetting_Type(DisplayString):
    """Custom type edfalabelLPSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelLPSetting_Type.__name__ = "DisplayString"
_EdfalabelLPSetting_Object = MibTableColumn
edfalabelLPSetting = _EdfalabelLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 123),
    _EdfalabelLPSetting_Type()
)
edfalabelLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelLPSetting.setStatus("optional")


class _EdfauomLPSetting_Type(DisplayString):
    """Custom type edfauomLPSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomLPSetting_Type.__name__ = "DisplayString"
_EdfauomLPSetting_Object = MibTableColumn
edfauomLPSetting = _EdfauomLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 124),
    _EdfauomLPSetting_Type()
)
edfauomLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomLPSetting.setStatus("optional")
_EdfamajorHighLPSetting_Type = Float
_EdfamajorHighLPSetting_Object = MibTableColumn
edfamajorHighLPSetting = _EdfamajorHighLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 125),
    _EdfamajorHighLPSetting_Type()
)
edfamajorHighLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighLPSetting.setStatus("mandatory")
_EdfamajorLowLPSetting_Type = Float
_EdfamajorLowLPSetting_Object = MibTableColumn
edfamajorLowLPSetting = _EdfamajorLowLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 126),
    _EdfamajorLowLPSetting_Type()
)
edfamajorLowLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowLPSetting.setStatus("mandatory")
_EdfaminorHighLPSetting_Type = Float
_EdfaminorHighLPSetting_Object = MibTableColumn
edfaminorHighLPSetting = _EdfaminorHighLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 127),
    _EdfaminorHighLPSetting_Type()
)
edfaminorHighLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighLPSetting.setStatus("mandatory")
_EdfaminorLowLPSetting_Type = Float
_EdfaminorLowLPSetting_Object = MibTableColumn
edfaminorLowLPSetting = _EdfaminorLowLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 128),
    _EdfaminorLowLPSetting_Type()
)
edfaminorLowLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowLPSetting.setStatus("mandatory")
_EdfacurrentValueLPSetting_Type = Float
_EdfacurrentValueLPSetting_Object = MibTableColumn
edfacurrentValueLPSetting = _EdfacurrentValueLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 129),
    _EdfacurrentValueLPSetting_Type()
)
edfacurrentValueLPSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfacurrentValueLPSetting.setStatus("mandatory")


class _EdfastateFlagLPSetting_Type(Integer32):
    """Custom type edfastateFlagLPSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagLPSetting_Type.__name__ = "Integer32"
_EdfastateFlagLPSetting_Object = MibTableColumn
edfastateFlagLPSetting = _EdfastateFlagLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 130),
    _EdfastateFlagLPSetting_Type()
)
edfastateFlagLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagLPSetting.setStatus("mandatory")
_EdfaminValueLPSetting_Type = Float
_EdfaminValueLPSetting_Object = MibTableColumn
edfaminValueLPSetting = _EdfaminValueLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 131),
    _EdfaminValueLPSetting_Type()
)
edfaminValueLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueLPSetting.setStatus("mandatory")
_EdfamaxValueLPSetting_Type = Float
_EdfamaxValueLPSetting_Object = MibTableColumn
edfamaxValueLPSetting = _EdfamaxValueLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 132),
    _EdfamaxValueLPSetting_Type()
)
edfamaxValueLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueLPSetting.setStatus("mandatory")


class _EdfaalarmStateLPSetting_Type(Integer32):
    """Custom type edfaalarmStateLPSetting based on Integer32"""
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


_EdfaalarmStateLPSetting_Type.__name__ = "Integer32"
_EdfaalarmStateLPSetting_Object = MibTableColumn
edfaalarmStateLPSetting = _EdfaalarmStateLPSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 133),
    _EdfaalarmStateLPSetting_Type()
)
edfaalarmStateLPSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateLPSetting.setStatus("mandatory")


class _EdfalabelCGSetting_Type(DisplayString):
    """Custom type edfalabelCGSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelCGSetting_Type.__name__ = "DisplayString"
_EdfalabelCGSetting_Object = MibTableColumn
edfalabelCGSetting = _EdfalabelCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 134),
    _EdfalabelCGSetting_Type()
)
edfalabelCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelCGSetting.setStatus("optional")


class _EdfauomCGSetting_Type(DisplayString):
    """Custom type edfauomCGSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomCGSetting_Type.__name__ = "DisplayString"
_EdfauomCGSetting_Object = MibTableColumn
edfauomCGSetting = _EdfauomCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 135),
    _EdfauomCGSetting_Type()
)
edfauomCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomCGSetting.setStatus("optional")
_EdfamajorHighCGSetting_Type = Float
_EdfamajorHighCGSetting_Object = MibTableColumn
edfamajorHighCGSetting = _EdfamajorHighCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 136),
    _EdfamajorHighCGSetting_Type()
)
edfamajorHighCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighCGSetting.setStatus("mandatory")
_EdfamajorLowCGSetting_Type = Float
_EdfamajorLowCGSetting_Object = MibTableColumn
edfamajorLowCGSetting = _EdfamajorLowCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 137),
    _EdfamajorLowCGSetting_Type()
)
edfamajorLowCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowCGSetting.setStatus("mandatory")
_EdfaminorHighCGSetting_Type = Float
_EdfaminorHighCGSetting_Object = MibTableColumn
edfaminorHighCGSetting = _EdfaminorHighCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 138),
    _EdfaminorHighCGSetting_Type()
)
edfaminorHighCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighCGSetting.setStatus("mandatory")
_EdfaminorLowCGSetting_Type = Float
_EdfaminorLowCGSetting_Object = MibTableColumn
edfaminorLowCGSetting = _EdfaminorLowCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 139),
    _EdfaminorLowCGSetting_Type()
)
edfaminorLowCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowCGSetting.setStatus("mandatory")
_EdfacurrentValueCGSetting_Type = Float
_EdfacurrentValueCGSetting_Object = MibTableColumn
edfacurrentValueCGSetting = _EdfacurrentValueCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 140),
    _EdfacurrentValueCGSetting_Type()
)
edfacurrentValueCGSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfacurrentValueCGSetting.setStatus("mandatory")


class _EdfastateFlagCGSetting_Type(Integer32):
    """Custom type edfastateFlagCGSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagCGSetting_Type.__name__ = "Integer32"
_EdfastateFlagCGSetting_Object = MibTableColumn
edfastateFlagCGSetting = _EdfastateFlagCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 141),
    _EdfastateFlagCGSetting_Type()
)
edfastateFlagCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagCGSetting.setStatus("mandatory")
_EdfaminValueCGSetting_Type = Float
_EdfaminValueCGSetting_Object = MibTableColumn
edfaminValueCGSetting = _EdfaminValueCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 142),
    _EdfaminValueCGSetting_Type()
)
edfaminValueCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueCGSetting.setStatus("mandatory")
_EdfamaxValueCGSetting_Type = Float
_EdfamaxValueCGSetting_Object = MibTableColumn
edfamaxValueCGSetting = _EdfamaxValueCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 143),
    _EdfamaxValueCGSetting_Type()
)
edfamaxValueCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueCGSetting.setStatus("mandatory")


class _EdfaalarmStateCGSetting_Type(Integer32):
    """Custom type edfaalarmStateCGSetting based on Integer32"""
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


_EdfaalarmStateCGSetting_Type.__name__ = "Integer32"
_EdfaalarmStateCGSetting_Object = MibTableColumn
edfaalarmStateCGSetting = _EdfaalarmStateCGSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 144),
    _EdfaalarmStateCGSetting_Type()
)
edfaalarmStateCGSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateCGSetting.setStatus("mandatory")


class _EdfalabelOptThreshold_Type(DisplayString):
    """Custom type edfalabelOptThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelOptThreshold_Type.__name__ = "DisplayString"
_EdfalabelOptThreshold_Object = MibTableColumn
edfalabelOptThreshold = _EdfalabelOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 145),
    _EdfalabelOptThreshold_Type()
)
edfalabelOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelOptThreshold.setStatus("optional")


class _EdfauomOptThreshold_Type(DisplayString):
    """Custom type edfauomOptThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfauomOptThreshold_Type.__name__ = "DisplayString"
_EdfauomOptThreshold_Object = MibTableColumn
edfauomOptThreshold = _EdfauomOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 146),
    _EdfauomOptThreshold_Type()
)
edfauomOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfauomOptThreshold.setStatus("optional")
_EdfamajorHighOptThreshold_Type = Float
_EdfamajorHighOptThreshold_Object = MibTableColumn
edfamajorHighOptThreshold = _EdfamajorHighOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 147),
    _EdfamajorHighOptThreshold_Type()
)
edfamajorHighOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorHighOptThreshold.setStatus("mandatory")
_EdfamajorLowOptThreshold_Type = Float
_EdfamajorLowOptThreshold_Object = MibTableColumn
edfamajorLowOptThreshold = _EdfamajorLowOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 148),
    _EdfamajorLowOptThreshold_Type()
)
edfamajorLowOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamajorLowOptThreshold.setStatus("mandatory")
_EdfaminorHighOptThreshold_Type = Float
_EdfaminorHighOptThreshold_Object = MibTableColumn
edfaminorHighOptThreshold = _EdfaminorHighOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 149),
    _EdfaminorHighOptThreshold_Type()
)
edfaminorHighOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorHighOptThreshold.setStatus("mandatory")
_EdfaminorLowOptThreshold_Type = Float
_EdfaminorLowOptThreshold_Object = MibTableColumn
edfaminorLowOptThreshold = _EdfaminorLowOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 150),
    _EdfaminorLowOptThreshold_Type()
)
edfaminorLowOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminorLowOptThreshold.setStatus("mandatory")
_EdfacurrentValueOptThreshold_Type = Float
_EdfacurrentValueOptThreshold_Object = MibTableColumn
edfacurrentValueOptThreshold = _EdfacurrentValueOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 151),
    _EdfacurrentValueOptThreshold_Type()
)
edfacurrentValueOptThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfacurrentValueOptThreshold.setStatus("mandatory")


class _EdfastateFlagOptThreshold_Type(Integer32):
    """Custom type edfastateFlagOptThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagOptThreshold_Type.__name__ = "Integer32"
_EdfastateFlagOptThreshold_Object = MibTableColumn
edfastateFlagOptThreshold = _EdfastateFlagOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 152),
    _EdfastateFlagOptThreshold_Type()
)
edfastateFlagOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagOptThreshold.setStatus("mandatory")
_EdfaminValueOptThreshold_Type = Float
_EdfaminValueOptThreshold_Object = MibTableColumn
edfaminValueOptThreshold = _EdfaminValueOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 153),
    _EdfaminValueOptThreshold_Type()
)
edfaminValueOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaminValueOptThreshold.setStatus("mandatory")
_EdfamaxValueOptThreshold_Type = Float
_EdfamaxValueOptThreshold_Object = MibTableColumn
edfamaxValueOptThreshold = _EdfamaxValueOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 154),
    _EdfamaxValueOptThreshold_Type()
)
edfamaxValueOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfamaxValueOptThreshold.setStatus("mandatory")


class _EdfaalarmStateOptThreshold_Type(Integer32):
    """Custom type edfaalarmStateOptThreshold based on Integer32"""
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


_EdfaalarmStateOptThreshold_Type.__name__ = "Integer32"
_EdfaalarmStateOptThreshold_Object = MibTableColumn
edfaalarmStateOptThreshold = _EdfaalarmStateOptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 2, 1, 155),
    _EdfaalarmStateOptThreshold_Type()
)
edfaalarmStateOptThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaalarmStateOptThreshold.setStatus("mandatory")
_Gx2EDFADigitalTable_Object = MibTable
gx2EDFADigitalTable = _Gx2EDFADigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3)
)
if mibBuilder.loadTexts:
    gx2EDFADigitalTable.setStatus("mandatory")
_Gx2EDFADigitalEntry_Object = MibTableRow
gx2EDFADigitalEntry = _Gx2EDFADigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2)
)
gx2EDFADigitalEntry.setIndexNames(
    (0, "OMNI-gx2EDFA-MIB", "edfagx2EDFADigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2EDFADigitalEntry.setStatus("mandatory")


class _Edfagx2EDFADigitalTableIndex_Type(Integer32):
    """Custom type edfagx2EDFADigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Edfagx2EDFADigitalTableIndex_Type.__name__ = "Integer32"
_Edfagx2EDFADigitalTableIndex_Object = MibTableColumn
edfagx2EDFADigitalTableIndex = _Edfagx2EDFADigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 1),
    _Edfagx2EDFADigitalTableIndex_Type()
)
edfagx2EDFADigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfagx2EDFADigitalTableIndex.setStatus("mandatory")


class _EdfalabelModeSetting_Type(DisplayString):
    """Custom type edfalabelModeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelModeSetting_Type.__name__ = "DisplayString"
_EdfalabelModeSetting_Object = MibTableColumn
edfalabelModeSetting = _EdfalabelModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 2),
    _EdfalabelModeSetting_Type()
)
edfalabelModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelModeSetting.setStatus("optional")


class _EdfaenumModeSetting_Type(DisplayString):
    """Custom type edfaenumModeSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfaenumModeSetting_Type.__name__ = "DisplayString"
_EdfaenumModeSetting_Object = MibTableColumn
edfaenumModeSetting = _EdfaenumModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 3),
    _EdfaenumModeSetting_Type()
)
edfaenumModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaenumModeSetting.setStatus("optional")


class _EdfavalueModeSetting_Type(Integer32):
    """Custom type edfavalueModeSetting based on Integer32"""
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
        *(("constant-gain-preset", 5),
          ("constant-gain-set", 6),
          ("laser-power-preset", 3),
          ("laser-power-set", 4),
          ("power-out-preset", 1),
          ("power-out-set", 2))
    )


_EdfavalueModeSetting_Type.__name__ = "Integer32"
_EdfavalueModeSetting_Object = MibTableColumn
edfavalueModeSetting = _EdfavalueModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 4),
    _EdfavalueModeSetting_Type()
)
edfavalueModeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfavalueModeSetting.setStatus("mandatory")


class _EdfastateFlagModeSetting_Type(Integer32):
    """Custom type edfastateFlagModeSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagModeSetting_Type.__name__ = "Integer32"
_EdfastateFlagModeSetting_Object = MibTableColumn
edfastateFlagModeSetting = _EdfastateFlagModeSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 5),
    _EdfastateFlagModeSetting_Type()
)
edfastateFlagModeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagModeSetting.setStatus("mandatory")


class _EdfalabelModuleState_Type(DisplayString):
    """Custom type edfalabelModuleState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelModuleState_Type.__name__ = "DisplayString"
_EdfalabelModuleState_Object = MibTableColumn
edfalabelModuleState = _EdfalabelModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 6),
    _EdfalabelModuleState_Type()
)
edfalabelModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelModuleState.setStatus("optional")


class _EdfaenumModuleState_Type(DisplayString):
    """Custom type edfaenumModuleState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfaenumModuleState_Type.__name__ = "DisplayString"
_EdfaenumModuleState_Object = MibTableColumn
edfaenumModuleState = _EdfaenumModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 7),
    _EdfaenumModuleState_Type()
)
edfaenumModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaenumModuleState.setStatus("optional")


class _EdfavalueModuleState_Type(Integer32):
    """Custom type edfavalueModuleState based on Integer32"""
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


_EdfavalueModuleState_Type.__name__ = "Integer32"
_EdfavalueModuleState_Object = MibTableColumn
edfavalueModuleState = _EdfavalueModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 8),
    _EdfavalueModuleState_Type()
)
edfavalueModuleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfavalueModuleState.setStatus("mandatory")


class _EdfastateFlagModuleState_Type(Integer32):
    """Custom type edfastateFlagModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagModuleState_Type.__name__ = "Integer32"
_EdfastateFlagModuleState_Object = MibTableColumn
edfastateFlagModuleState = _EdfastateFlagModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 9),
    _EdfastateFlagModuleState_Type()
)
edfastateFlagModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagModuleState.setStatus("mandatory")


class _EdfalabelFactoryDefault_Type(DisplayString):
    """Custom type edfalabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelFactoryDefault_Type.__name__ = "DisplayString"
_EdfalabelFactoryDefault_Object = MibTableColumn
edfalabelFactoryDefault = _EdfalabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 10),
    _EdfalabelFactoryDefault_Type()
)
edfalabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelFactoryDefault.setStatus("optional")


class _EdfaenumFactoryDefault_Type(DisplayString):
    """Custom type edfaenumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfaenumFactoryDefault_Type.__name__ = "DisplayString"
_EdfaenumFactoryDefault_Object = MibTableColumn
edfaenumFactoryDefault = _EdfaenumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 11),
    _EdfaenumFactoryDefault_Type()
)
edfaenumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaenumFactoryDefault.setStatus("optional")


class _EdfavalueFactoryDefault_Type(Integer32):
    """Custom type edfavalueFactoryDefault based on Integer32"""
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


_EdfavalueFactoryDefault_Type.__name__ = "Integer32"
_EdfavalueFactoryDefault_Object = MibTableColumn
edfavalueFactoryDefault = _EdfavalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 12),
    _EdfavalueFactoryDefault_Type()
)
edfavalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edfavalueFactoryDefault.setStatus("mandatory")


class _EdfastateFlagFactoryDefault_Type(Integer32):
    """Custom type edfastateFlagFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateFlagFactoryDefault_Type.__name__ = "Integer32"
_EdfastateFlagFactoryDefault_Object = MibTableColumn
edfastateFlagFactoryDefault = _EdfastateFlagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 3, 2, 13),
    _EdfastateFlagFactoryDefault_Type()
)
edfastateFlagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateFlagFactoryDefault.setStatus("mandatory")
_Gx2EDFAStatusTable_Object = MibTable
gx2EDFAStatusTable = _Gx2EDFAStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    gx2EDFAStatusTable.setStatus("mandatory")
_Gx2EDFAStatusEntry_Object = MibTableRow
gx2EDFAStatusEntry = _Gx2EDFAStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3)
)
gx2EDFAStatusEntry.setIndexNames(
    (0, "OMNI-gx2EDFA-MIB", "edfagx2EDFAStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2EDFAStatusEntry.setStatus("mandatory")


class _Edfagx2EDFAStatusTableIndex_Type(Integer32):
    """Custom type edfagx2EDFAStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Edfagx2EDFAStatusTableIndex_Type.__name__ = "Integer32"
_Edfagx2EDFAStatusTableIndex_Object = MibTableColumn
edfagx2EDFAStatusTableIndex = _Edfagx2EDFAStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 1),
    _Edfagx2EDFAStatusTableIndex_Type()
)
edfagx2EDFAStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfagx2EDFAStatusTableIndex.setStatus("mandatory")


class _EdfalabelBoot_Type(DisplayString):
    """Custom type edfalabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelBoot_Type.__name__ = "DisplayString"
_EdfalabelBoot_Object = MibTableColumn
edfalabelBoot = _EdfalabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 2),
    _EdfalabelBoot_Type()
)
edfalabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelBoot.setStatus("optional")


class _EdfavalueBoot_Type(Integer32):
    """Custom type edfavalueBoot based on Integer32"""
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


_EdfavalueBoot_Type.__name__ = "Integer32"
_EdfavalueBoot_Object = MibTableColumn
edfavalueBoot = _EdfavalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 3),
    _EdfavalueBoot_Type()
)
edfavalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueBoot.setStatus("mandatory")


class _EdfastateflagBoot_Type(Integer32):
    """Custom type edfastateflagBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagBoot_Type.__name__ = "Integer32"
_EdfastateflagBoot_Object = MibTableColumn
edfastateflagBoot = _EdfastateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 4),
    _EdfastateflagBoot_Type()
)
edfastateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagBoot.setStatus("mandatory")


class _EdfalabelFlash_Type(DisplayString):
    """Custom type edfalabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelFlash_Type.__name__ = "DisplayString"
_EdfalabelFlash_Object = MibTableColumn
edfalabelFlash = _EdfalabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 5),
    _EdfalabelFlash_Type()
)
edfalabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelFlash.setStatus("optional")


class _EdfavalueFlash_Type(Integer32):
    """Custom type edfavalueFlash based on Integer32"""
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


_EdfavalueFlash_Type.__name__ = "Integer32"
_EdfavalueFlash_Object = MibTableColumn
edfavalueFlash = _EdfavalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 6),
    _EdfavalueFlash_Type()
)
edfavalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueFlash.setStatus("mandatory")


class _EdfastateflagFlash_Type(Integer32):
    """Custom type edfastateflagFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagFlash_Type.__name__ = "Integer32"
_EdfastateflagFlash_Object = MibTableColumn
edfastateflagFlash = _EdfastateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 7),
    _EdfastateflagFlash_Type()
)
edfastateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagFlash.setStatus("mandatory")


class _EdfalabelFactoryDataCRC_Type(DisplayString):
    """Custom type edfalabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelFactoryDataCRC_Type.__name__ = "DisplayString"
_EdfalabelFactoryDataCRC_Object = MibTableColumn
edfalabelFactoryDataCRC = _EdfalabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 8),
    _EdfalabelFactoryDataCRC_Type()
)
edfalabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelFactoryDataCRC.setStatus("optional")


class _EdfavalueFactoryDataCRC_Type(Integer32):
    """Custom type edfavalueFactoryDataCRC based on Integer32"""
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


_EdfavalueFactoryDataCRC_Type.__name__ = "Integer32"
_EdfavalueFactoryDataCRC_Object = MibTableColumn
edfavalueFactoryDataCRC = _EdfavalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 9),
    _EdfavalueFactoryDataCRC_Type()
)
edfavalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueFactoryDataCRC.setStatus("mandatory")


class _EdfastateflagFactoryDataCRC_Type(Integer32):
    """Custom type edfastateflagFactoryDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagFactoryDataCRC_Type.__name__ = "Integer32"
_EdfastateflagFactoryDataCRC_Object = MibTableColumn
edfastateflagFactoryDataCRC = _EdfastateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 10),
    _EdfastateflagFactoryDataCRC_Type()
)
edfastateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagFactoryDataCRC.setStatus("mandatory")


class _EdfalabelAlarmDataCRC_Type(DisplayString):
    """Custom type edfalabelAlarmDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelAlarmDataCRC_Type.__name__ = "DisplayString"
_EdfalabelAlarmDataCRC_Object = MibTableColumn
edfalabelAlarmDataCRC = _EdfalabelAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 11),
    _EdfalabelAlarmDataCRC_Type()
)
edfalabelAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelAlarmDataCRC.setStatus("optional")


class _EdfavalueAlarmDataCRC_Type(Integer32):
    """Custom type edfavalueAlarmDataCRC based on Integer32"""
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


_EdfavalueAlarmDataCRC_Type.__name__ = "Integer32"
_EdfavalueAlarmDataCRC_Object = MibTableColumn
edfavalueAlarmDataCRC = _EdfavalueAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 12),
    _EdfavalueAlarmDataCRC_Type()
)
edfavalueAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueAlarmDataCRC.setStatus("mandatory")


class _EdfastateflagAlarmDataCRC_Type(Integer32):
    """Custom type edfastateflagAlarmDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagAlarmDataCRC_Type.__name__ = "Integer32"
_EdfastateflagAlarmDataCRC_Object = MibTableColumn
edfastateflagAlarmDataCRC = _EdfastateflagAlarmDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 13),
    _EdfastateflagAlarmDataCRC_Type()
)
edfastateflagAlarmDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagAlarmDataCRC.setStatus("mandatory")


class _EdfalabelCalibrationDataCRC_Type(DisplayString):
    """Custom type edfalabelCalibrationDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelCalibrationDataCRC_Type.__name__ = "DisplayString"
_EdfalabelCalibrationDataCRC_Object = MibTableColumn
edfalabelCalibrationDataCRC = _EdfalabelCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 14),
    _EdfalabelCalibrationDataCRC_Type()
)
edfalabelCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelCalibrationDataCRC.setStatus("optional")


class _EdfavalueCalibrationDataCRC_Type(Integer32):
    """Custom type edfavalueCalibrationDataCRC based on Integer32"""
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


_EdfavalueCalibrationDataCRC_Type.__name__ = "Integer32"
_EdfavalueCalibrationDataCRC_Object = MibTableColumn
edfavalueCalibrationDataCRC = _EdfavalueCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 15),
    _EdfavalueCalibrationDataCRC_Type()
)
edfavalueCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueCalibrationDataCRC.setStatus("mandatory")


class _EdfastateflagCalibrationDataCRC_Type(Integer32):
    """Custom type edfastateflagCalibrationDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagCalibrationDataCRC_Type.__name__ = "Integer32"
_EdfastateflagCalibrationDataCRC_Object = MibTableColumn
edfastateflagCalibrationDataCRC = _EdfastateflagCalibrationDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 16),
    _EdfastateflagCalibrationDataCRC_Type()
)
edfastateflagCalibrationDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagCalibrationDataCRC.setStatus("mandatory")


class _EdfalabelOptInShutdown_Type(DisplayString):
    """Custom type edfalabelOptInShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelOptInShutdown_Type.__name__ = "DisplayString"
_EdfalabelOptInShutdown_Object = MibTableColumn
edfalabelOptInShutdown = _EdfalabelOptInShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 17),
    _EdfalabelOptInShutdown_Type()
)
edfalabelOptInShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelOptInShutdown.setStatus("optional")


class _EdfavalueOptInShutdown_Type(Integer32):
    """Custom type edfavalueOptInShutdown based on Integer32"""
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


_EdfavalueOptInShutdown_Type.__name__ = "Integer32"
_EdfavalueOptInShutdown_Object = MibTableColumn
edfavalueOptInShutdown = _EdfavalueOptInShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 18),
    _EdfavalueOptInShutdown_Type()
)
edfavalueOptInShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueOptInShutdown.setStatus("mandatory")


class _EdfastateflagOptInShutdown_Type(Integer32):
    """Custom type edfastateflagOptInShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagOptInShutdown_Type.__name__ = "Integer32"
_EdfastateflagOptInShutdown_Object = MibTableColumn
edfastateflagOptInShutdown = _EdfastateflagOptInShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 19),
    _EdfastateflagOptInShutdown_Type()
)
edfastateflagOptInShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagOptInShutdown.setStatus("mandatory")


class _EdfalabelTECTempShutdown_Type(DisplayString):
    """Custom type edfalabelTECTempShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelTECTempShutdown_Type.__name__ = "DisplayString"
_EdfalabelTECTempShutdown_Object = MibTableColumn
edfalabelTECTempShutdown = _EdfalabelTECTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 20),
    _EdfalabelTECTempShutdown_Type()
)
edfalabelTECTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelTECTempShutdown.setStatus("optional")


class _EdfavalueTECTempShutdown_Type(Integer32):
    """Custom type edfavalueTECTempShutdown based on Integer32"""
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


_EdfavalueTECTempShutdown_Type.__name__ = "Integer32"
_EdfavalueTECTempShutdown_Object = MibTableColumn
edfavalueTECTempShutdown = _EdfavalueTECTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 21),
    _EdfavalueTECTempShutdown_Type()
)
edfavalueTECTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueTECTempShutdown.setStatus("mandatory")


class _EdfastateflagTECTempShutdown_Type(Integer32):
    """Custom type edfastateflagTECTempShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagTECTempShutdown_Type.__name__ = "Integer32"
_EdfastateflagTECTempShutdown_Object = MibTableColumn
edfastateflagTECTempShutdown = _EdfastateflagTECTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 22),
    _EdfastateflagTECTempShutdown_Type()
)
edfastateflagTECTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagTECTempShutdown.setStatus("mandatory")


class _EdfalabelTECShutOverride_Type(DisplayString):
    """Custom type edfalabelTECShutOverride based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelTECShutOverride_Type.__name__ = "DisplayString"
_EdfalabelTECShutOverride_Object = MibTableColumn
edfalabelTECShutOverride = _EdfalabelTECShutOverride_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 23),
    _EdfalabelTECShutOverride_Type()
)
edfalabelTECShutOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelTECShutOverride.setStatus("optional")


class _EdfavalueTECShutOverride_Type(Integer32):
    """Custom type edfavalueTECShutOverride based on Integer32"""
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


_EdfavalueTECShutOverride_Type.__name__ = "Integer32"
_EdfavalueTECShutOverride_Object = MibTableColumn
edfavalueTECShutOverride = _EdfavalueTECShutOverride_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 24),
    _EdfavalueTECShutOverride_Type()
)
edfavalueTECShutOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueTECShutOverride.setStatus("mandatory")


class _EdfastateflagTECShutOverride_Type(Integer32):
    """Custom type edfastateflagTECShutOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagTECShutOverride_Type.__name__ = "Integer32"
_EdfastateflagTECShutOverride_Object = MibTableColumn
edfastateflagTECShutOverride = _EdfastateflagTECShutOverride_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 25),
    _EdfastateflagTECShutOverride_Type()
)
edfastateflagTECShutOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagTECShutOverride.setStatus("mandatory")


class _EdfalabelPowerFail_Type(DisplayString):
    """Custom type edfalabelPowerFail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelPowerFail_Type.__name__ = "DisplayString"
_EdfalabelPowerFail_Object = MibTableColumn
edfalabelPowerFail = _EdfalabelPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 26),
    _EdfalabelPowerFail_Type()
)
edfalabelPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelPowerFail.setStatus("optional")


class _EdfavaluePowerFail_Type(Integer32):
    """Custom type edfavaluePowerFail based on Integer32"""
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


_EdfavaluePowerFail_Type.__name__ = "Integer32"
_EdfavaluePowerFail_Object = MibTableColumn
edfavaluePowerFail = _EdfavaluePowerFail_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 27),
    _EdfavaluePowerFail_Type()
)
edfavaluePowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavaluePowerFail.setStatus("mandatory")


class _EdfastateflagPowerFail_Type(Integer32):
    """Custom type edfastateflagPowerFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagPowerFail_Type.__name__ = "Integer32"
_EdfastateflagPowerFail_Object = MibTableColumn
edfastateflagPowerFail = _EdfastateflagPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 28),
    _EdfastateflagPowerFail_Type()
)
edfastateflagPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagPowerFail.setStatus("mandatory")


class _EdfalabelKeySwitch_Type(DisplayString):
    """Custom type edfalabelKeySwitch based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelKeySwitch_Type.__name__ = "DisplayString"
_EdfalabelKeySwitch_Object = MibTableColumn
edfalabelKeySwitch = _EdfalabelKeySwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 29),
    _EdfalabelKeySwitch_Type()
)
edfalabelKeySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelKeySwitch.setStatus("optional")


class _EdfavalueKeySwitch_Type(Integer32):
    """Custom type edfavalueKeySwitch based on Integer32"""
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


_EdfavalueKeySwitch_Type.__name__ = "Integer32"
_EdfavalueKeySwitch_Object = MibTableColumn
edfavalueKeySwitch = _EdfavalueKeySwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 30),
    _EdfavalueKeySwitch_Type()
)
edfavalueKeySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueKeySwitch.setStatus("mandatory")


class _EdfastateflagKeySwitch_Type(Integer32):
    """Custom type edfastateflagKeySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagKeySwitch_Type.__name__ = "Integer32"
_EdfastateflagKeySwitch_Object = MibTableColumn
edfastateflagKeySwitch = _EdfastateflagKeySwitch_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 31),
    _EdfastateflagKeySwitch_Type()
)
edfastateflagKeySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagKeySwitch.setStatus("mandatory")


class _EdfalabelLaserCurrShutdown_Type(DisplayString):
    """Custom type edfalabelLaserCurrShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelLaserCurrShutdown_Type.__name__ = "DisplayString"
_EdfalabelLaserCurrShutdown_Object = MibTableColumn
edfalabelLaserCurrShutdown = _EdfalabelLaserCurrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 32),
    _EdfalabelLaserCurrShutdown_Type()
)
edfalabelLaserCurrShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelLaserCurrShutdown.setStatus("optional")


class _EdfavalueLaserCurrShutdown_Type(Integer32):
    """Custom type edfavalueLaserCurrShutdown based on Integer32"""
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


_EdfavalueLaserCurrShutdown_Type.__name__ = "Integer32"
_EdfavalueLaserCurrShutdown_Object = MibTableColumn
edfavalueLaserCurrShutdown = _EdfavalueLaserCurrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 33),
    _EdfavalueLaserCurrShutdown_Type()
)
edfavalueLaserCurrShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueLaserCurrShutdown.setStatus("mandatory")


class _EdfastateflagLaserCurrShutdown_Type(Integer32):
    """Custom type edfastateflagLaserCurrShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagLaserCurrShutdown_Type.__name__ = "Integer32"
_EdfastateflagLaserCurrShutdown_Object = MibTableColumn
edfastateflagLaserCurrShutdown = _EdfastateflagLaserCurrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 34),
    _EdfastateflagLaserCurrShutdown_Type()
)
edfastateflagLaserCurrShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagLaserCurrShutdown.setStatus("mandatory")


class _EdfalabelLaserPowShutdown_Type(DisplayString):
    """Custom type edfalabelLaserPowShutdown based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelLaserPowShutdown_Type.__name__ = "DisplayString"
_EdfalabelLaserPowShutdown_Object = MibTableColumn
edfalabelLaserPowShutdown = _EdfalabelLaserPowShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 35),
    _EdfalabelLaserPowShutdown_Type()
)
edfalabelLaserPowShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelLaserPowShutdown.setStatus("optional")


class _EdfavalueLaserPowShutdown_Type(Integer32):
    """Custom type edfavalueLaserPowShutdown based on Integer32"""
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


_EdfavalueLaserPowShutdown_Type.__name__ = "Integer32"
_EdfavalueLaserPowShutdown_Object = MibTableColumn
edfavalueLaserPowShutdown = _EdfavalueLaserPowShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 36),
    _EdfavalueLaserPowShutdown_Type()
)
edfavalueLaserPowShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueLaserPowShutdown.setStatus("mandatory")


class _EdfastateflagLaserPowShutdown_Type(Integer32):
    """Custom type edfastateflagLaserPowShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagLaserPowShutdown_Type.__name__ = "Integer32"
_EdfastateflagLaserPowShutdown_Object = MibTableColumn
edfastateflagLaserPowShutdown = _EdfastateflagLaserPowShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 37),
    _EdfastateflagLaserPowShutdown_Type()
)
edfastateflagLaserPowShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagLaserPowShutdown.setStatus("mandatory")


class _EdfalabelADCStatus_Type(DisplayString):
    """Custom type edfalabelADCStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelADCStatus_Type.__name__ = "DisplayString"
_EdfalabelADCStatus_Object = MibTableColumn
edfalabelADCStatus = _EdfalabelADCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 38),
    _EdfalabelADCStatus_Type()
)
edfalabelADCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelADCStatus.setStatus("optional")


class _EdfavalueADCStatus_Type(Integer32):
    """Custom type edfavalueADCStatus based on Integer32"""
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


_EdfavalueADCStatus_Type.__name__ = "Integer32"
_EdfavalueADCStatus_Object = MibTableColumn
edfavalueADCStatus = _EdfavalueADCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 39),
    _EdfavalueADCStatus_Type()
)
edfavalueADCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueADCStatus.setStatus("mandatory")


class _EdfastateflagADCStatus_Type(Integer32):
    """Custom type edfastateflagADCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagADCStatus_Type.__name__ = "Integer32"
_EdfastateflagADCStatus_Object = MibTableColumn
edfastateflagADCStatus = _EdfastateflagADCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 40),
    _EdfastateflagADCStatus_Type()
)
edfastateflagADCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagADCStatus.setStatus("mandatory")


class _EdfalabelConstGainStatus_Type(DisplayString):
    """Custom type edfalabelConstGainStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelConstGainStatus_Type.__name__ = "DisplayString"
_EdfalabelConstGainStatus_Object = MibTableColumn
edfalabelConstGainStatus = _EdfalabelConstGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 41),
    _EdfalabelConstGainStatus_Type()
)
edfalabelConstGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelConstGainStatus.setStatus("optional")


class _EdfavalueConstGainStatus_Type(Integer32):
    """Custom type edfavalueConstGainStatus based on Integer32"""
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


_EdfavalueConstGainStatus_Type.__name__ = "Integer32"
_EdfavalueConstGainStatus_Object = MibTableColumn
edfavalueConstGainStatus = _EdfavalueConstGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 42),
    _EdfavalueConstGainStatus_Type()
)
edfavalueConstGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueConstGainStatus.setStatus("mandatory")


class _EdfastateflagConstGainStatus_Type(Integer32):
    """Custom type edfastateflagConstGainStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagConstGainStatus_Type.__name__ = "Integer32"
_EdfastateflagConstGainStatus_Object = MibTableColumn
edfastateflagConstGainStatus = _EdfastateflagConstGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 43),
    _EdfastateflagConstGainStatus_Type()
)
edfastateflagConstGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagConstGainStatus.setStatus("mandatory")


class _EdfalabelStandbyStatus_Type(DisplayString):
    """Custom type edfalabelStandbyStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfalabelStandbyStatus_Type.__name__ = "DisplayString"
_EdfalabelStandbyStatus_Object = MibTableColumn
edfalabelStandbyStatus = _EdfalabelStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 44),
    _EdfalabelStandbyStatus_Type()
)
edfalabelStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfalabelStandbyStatus.setStatus("optional")


class _EdfavalueStandbyStatus_Type(Integer32):
    """Custom type edfavalueStandbyStatus based on Integer32"""
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


_EdfavalueStandbyStatus_Type.__name__ = "Integer32"
_EdfavalueStandbyStatus_Object = MibTableColumn
edfavalueStandbyStatus = _EdfavalueStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 45),
    _EdfavalueStandbyStatus_Type()
)
edfavalueStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfavalueStandbyStatus.setStatus("mandatory")


class _EdfastateflagStandbyStatus_Type(Integer32):
    """Custom type edfastateflagStandbyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_EdfastateflagStandbyStatus_Type.__name__ = "Integer32"
_EdfastateflagStandbyStatus_Object = MibTableColumn
edfastateflagStandbyStatus = _EdfastateflagStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 4, 3, 46),
    _EdfastateflagStandbyStatus_Type()
)
edfastateflagStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfastateflagStandbyStatus.setStatus("mandatory")
_Gx2EDFAFactoryTable_Object = MibTable
gx2EDFAFactoryTable = _Gx2EDFAFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5)
)
if mibBuilder.loadTexts:
    gx2EDFAFactoryTable.setStatus("mandatory")
_Gx2EDFAFactoryEntry_Object = MibTableRow
gx2EDFAFactoryEntry = _Gx2EDFAFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4)
)
gx2EDFAFactoryEntry.setIndexNames(
    (0, "OMNI-gx2EDFA-MIB", "edfagx2EDFAFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2EDFAFactoryEntry.setStatus("mandatory")


class _Edfagx2EDFAFactoryTableIndex_Type(Integer32):
    """Custom type edfagx2EDFAFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Edfagx2EDFAFactoryTableIndex_Type.__name__ = "Integer32"
_Edfagx2EDFAFactoryTableIndex_Object = MibTableColumn
edfagx2EDFAFactoryTableIndex = _Edfagx2EDFAFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 1),
    _Edfagx2EDFAFactoryTableIndex_Type()
)
edfagx2EDFAFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfagx2EDFAFactoryTableIndex.setStatus("mandatory")
_EdfabootControlByte_Type = Integer32
_EdfabootControlByte_Object = MibTableColumn
edfabootControlByte = _EdfabootControlByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 2),
    _EdfabootControlByte_Type()
)
edfabootControlByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfabootControlByte.setStatus("mandatory")
_EdfabootStatusByte_Type = Integer32
_EdfabootStatusByte_Object = MibTableColumn
edfabootStatusByte = _EdfabootStatusByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 3),
    _EdfabootStatusByte_Type()
)
edfabootStatusByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfabootStatusByte.setStatus("mandatory")
_Edfabank0CRC_Type = Integer32
_Edfabank0CRC_Object = MibTableColumn
edfabank0CRC = _Edfabank0CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 4),
    _Edfabank0CRC_Type()
)
edfabank0CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfabank0CRC.setStatus("mandatory")
_Edfabank1CRC_Type = Integer32
_Edfabank1CRC_Object = MibTableColumn
edfabank1CRC = _Edfabank1CRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 5),
    _Edfabank1CRC_Type()
)
edfabank1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfabank1CRC.setStatus("mandatory")
_EdfaprgEEPROMByte_Type = Integer32
_EdfaprgEEPROMByte_Object = MibTableColumn
edfaprgEEPROMByte = _EdfaprgEEPROMByte_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 6),
    _EdfaprgEEPROMByte_Type()
)
edfaprgEEPROMByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaprgEEPROMByte.setStatus("mandatory")
_EdfafactoryCRC_Type = Integer32
_EdfafactoryCRC_Object = MibTableColumn
edfafactoryCRC = _EdfafactoryCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 7),
    _EdfafactoryCRC_Type()
)
edfafactoryCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfafactoryCRC.setStatus("mandatory")


class _EdfacalculateCRC_Type(Integer32):
    """Custom type edfacalculateCRC based on Integer32"""
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


_EdfacalculateCRC_Type.__name__ = "Integer32"
_EdfacalculateCRC_Object = MibTableColumn
edfacalculateCRC = _EdfacalculateCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 8),
    _EdfacalculateCRC_Type()
)
edfacalculateCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfacalculateCRC.setStatus("mandatory")
_EdfahourMeter_Type = Integer32
_EdfahourMeter_Object = MibTableColumn
edfahourMeter = _EdfahourMeter_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 9),
    _EdfahourMeter_Type()
)
edfahourMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfahourMeter.setStatus("mandatory")
_EdfaflashPrgCntA_Type = Integer32
_EdfaflashPrgCntA_Object = MibTableColumn
edfaflashPrgCntA = _EdfaflashPrgCntA_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 10),
    _EdfaflashPrgCntA_Type()
)
edfaflashPrgCntA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaflashPrgCntA.setStatus("mandatory")
_EdfaflashPrgCntB_Type = Integer32
_EdfaflashPrgCntB_Object = MibTableColumn
edfaflashPrgCntB = _EdfaflashPrgCntB_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 11),
    _EdfaflashPrgCntB_Type()
)
edfaflashPrgCntB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfaflashPrgCntB.setStatus("mandatory")


class _EdfafwRev0_Type(DisplayString):
    """Custom type edfafwRev0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfafwRev0_Type.__name__ = "DisplayString"
_EdfafwRev0_Object = MibTableColumn
edfafwRev0 = _EdfafwRev0_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 12),
    _EdfafwRev0_Type()
)
edfafwRev0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfafwRev0.setStatus("mandatory")


class _EdfafwRev1_Type(DisplayString):
    """Custom type edfafwRev1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EdfafwRev1_Type.__name__ = "DisplayString"
_EdfafwRev1_Object = MibTableColumn
edfafwRev1 = _EdfafwRev1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 5, 4, 13),
    _EdfafwRev1_Type()
)
edfafwRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edfafwRev1.setStatus("mandatory")
_Gx2EDFAHoldTimeTable_Object = MibTable
gx2EDFAHoldTimeTable = _Gx2EDFAHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 6)
)
if mibBuilder.loadTexts:
    gx2EDFAHoldTimeTable.setStatus("mandatory")
_Gx2EDFAHoldTimeEntry_Object = MibTableRow
gx2EDFAHoldTimeEntry = _Gx2EDFAHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 6, 5)
)
gx2EDFAHoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2EDFA-MIB", "gx2EDFAHoldTimeTableIndex"),
    (0, "OMNI-gx2EDFA-MIB", "gx2EDFAHoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2EDFAHoldTimeEntry.setStatus("mandatory")


class _Gx2EDFAHoldTimeTableIndex_Type(Integer32):
    """Custom type gx2EDFAHoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2EDFAHoldTimeTableIndex_Type.__name__ = "Integer32"
_Gx2EDFAHoldTimeTableIndex_Object = MibTableColumn
gx2EDFAHoldTimeTableIndex = _Gx2EDFAHoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 6, 5, 1),
    _Gx2EDFAHoldTimeTableIndex_Type()
)
gx2EDFAHoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2EDFAHoldTimeTableIndex.setStatus("mandatory")


class _Gx2EDFAHoldTimeSpecIndex_Type(Integer32):
    """Custom type gx2EDFAHoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2EDFAHoldTimeSpecIndex_Type.__name__ = "Integer32"
_Gx2EDFAHoldTimeSpecIndex_Object = MibTableColumn
gx2EDFAHoldTimeSpecIndex = _Gx2EDFAHoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 6, 5, 2),
    _Gx2EDFAHoldTimeSpecIndex_Type()
)
gx2EDFAHoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2EDFAHoldTimeSpecIndex.setStatus("mandatory")
_Gx2EDFAHoldTimeData_Type = Integer32
_Gx2EDFAHoldTimeData_Object = MibTableColumn
gx2EDFAHoldTimeData = _Gx2EDFAHoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 6, 5, 3),
    _Gx2EDFAHoldTimeData_Type()
)
gx2EDFAHoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gx2EDFAHoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapEDFAConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 1)
)
trapEDFAConfigChangeInteger.setObjects(
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
    trapEDFAConfigChangeInteger.setStatus(
        ""
    )

trapEDFAConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 2)
)
trapEDFAConfigChangeDisplayString.setObjects(
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
    trapEDFAConfigChangeDisplayString.setStatus(
        ""
    )

trapEDFAModuleTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 3)
)
trapEDFAModuleTemperatureAlarm.setObjects(
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
    trapEDFAModuleTemperatureAlarm.setStatus(
        ""
    )

trapEDFAOpticalInPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 4)
)
trapEDFAOpticalInPowerAlarm.setObjects(
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
    trapEDFAOpticalInPowerAlarm.setStatus(
        ""
    )

trapEDFAOpticalOutPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 5)
)
trapEDFAOpticalOutPowerAlarm.setObjects(
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
    trapEDFAOpticalOutPowerAlarm.setStatus(
        ""
    )

trapEDFATECTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 6)
)
trapEDFATECTemperatureAlarm.setObjects(
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
    trapEDFATECTemperatureAlarm.setStatus(
        ""
    )

trapEDFATECCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 7)
)
trapEDFATECCurrentAlarm.setObjects(
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
    trapEDFATECCurrentAlarm.setStatus(
        ""
    )

trapEDFALaserCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 8)
)
trapEDFALaserCurrentAlarm.setObjects(
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
    trapEDFALaserCurrentAlarm.setStatus(
        ""
    )

trapEDFALaserPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 9)
)
trapEDFALaserPowerAlarm.setObjects(
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
    trapEDFALaserPowerAlarm.setStatus(
        ""
    )

trapEDFAPlus12CurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 10)
)
trapEDFAPlus12CurrentAlarm.setObjects(
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
    trapEDFAPlus12CurrentAlarm.setStatus(
        ""
    )

trapEDFAPlus37CurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 11)
)
trapEDFAPlus37CurrentAlarm.setObjects(
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
    trapEDFAPlus37CurrentAlarm.setStatus(
        ""
    )

trapEDFAFanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 12)
)
trapEDFAFanCurrentAlarm.setObjects(
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
    trapEDFAFanCurrentAlarm.setStatus(
        ""
    )

trapEDFAResetFacDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 13)
)
trapEDFAResetFacDefault.setObjects(
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
    trapEDFAResetFacDefault.setStatus(
        ""
    )

trapEDFAStandbyMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 14)
)
trapEDFAStandbyMode.setObjects(
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
    trapEDFAStandbyMode.setStatus(
        ""
    )

trapEDFAOptInShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 15)
)
trapEDFAOptInShutdown.setObjects(
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
    trapEDFAOptInShutdown.setStatus(
        ""
    )

trapEDFATECTempShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 16)
)
trapEDFATECTempShutdown.setObjects(
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
    trapEDFATECTempShutdown.setStatus(
        ""
    )

trapEDFAKeySwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 17)
)
trapEDFAKeySwitch.setObjects(
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
    trapEDFAKeySwitch.setStatus(
        ""
    )

trapEDFAPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 18)
)
trapEDFAPowerFail.setObjects(
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
    trapEDFAPowerFail.setStatus(
        ""
    )

trapEDFALasCurrShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 19)
)
trapEDFALasCurrShutdown.setObjects(
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
    trapEDFALasCurrShutdown.setStatus(
        ""
    )

trapEDFALasPowerShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 20)
)
trapEDFALasPowerShutdown.setObjects(
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
    trapEDFALasPowerShutdown.setStatus(
        ""
    )

trapEDFAInvalidMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 21)
)
trapEDFAInvalidMode.setObjects(
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
    trapEDFAInvalidMode.setStatus(
        ""
    )

trapEDFAFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 22)
)
trapEDFAFlashAlarm.setObjects(
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
    trapEDFAFlashAlarm.setStatus(
        ""
    )

trapEDFABoot0Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 23)
)
trapEDFABoot0Alarm.setObjects(
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
    trapEDFABoot0Alarm.setStatus(
        ""
    )

trapEDFABoot1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 24)
)
trapEDFABoot1Alarm.setObjects(
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
    trapEDFABoot1Alarm.setStatus(
        ""
    )

trapEDFAAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 25)
)
trapEDFAAlarmDataCRCAlarm.setObjects(
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
    trapEDFAAlarmDataCRCAlarm.setStatus(
        ""
    )

trapEDFAFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 26)
)
trapEDFAFactoryDataCRCAlarm.setObjects(
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
    trapEDFAFactoryDataCRCAlarm.setStatus(
        ""
    )

trapEDFACalDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 27)
)
trapEDFACalDataCRCAlarm.setObjects(
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
    trapEDFACalDataCRCAlarm.setStatus(
        ""
    )

trapEDFAFacCalFloatAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 28)
)
trapEDFAFacCalFloatAlarm.setObjects(
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
    trapEDFAFacCalFloatAlarm.setStatus(
        ""
    )

trapEDFAOptInThreshAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 29)
)
trapEDFAOptInThreshAlarm.setObjects(
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
    trapEDFAOptInThreshAlarm.setStatus(
        ""
    )

trapEDFAGainErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11, 0, 30)
)
trapEDFAGainErrorAlarm.setObjects(
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
    trapEDFAGainErrorAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2EDFA-MIB",
    **{"Float": Float,
       "trapEDFAConfigChangeInteger": trapEDFAConfigChangeInteger,
       "trapEDFAConfigChangeDisplayString": trapEDFAConfigChangeDisplayString,
       "trapEDFAModuleTemperatureAlarm": trapEDFAModuleTemperatureAlarm,
       "trapEDFAOpticalInPowerAlarm": trapEDFAOpticalInPowerAlarm,
       "trapEDFAOpticalOutPowerAlarm": trapEDFAOpticalOutPowerAlarm,
       "trapEDFATECTemperatureAlarm": trapEDFATECTemperatureAlarm,
       "trapEDFATECCurrentAlarm": trapEDFATECCurrentAlarm,
       "trapEDFALaserCurrentAlarm": trapEDFALaserCurrentAlarm,
       "trapEDFALaserPowerAlarm": trapEDFALaserPowerAlarm,
       "trapEDFAPlus12CurrentAlarm": trapEDFAPlus12CurrentAlarm,
       "trapEDFAPlus37CurrentAlarm": trapEDFAPlus37CurrentAlarm,
       "trapEDFAFanCurrentAlarm": trapEDFAFanCurrentAlarm,
       "trapEDFAResetFacDefault": trapEDFAResetFacDefault,
       "trapEDFAStandbyMode": trapEDFAStandbyMode,
       "trapEDFAOptInShutdown": trapEDFAOptInShutdown,
       "trapEDFATECTempShutdown": trapEDFATECTempShutdown,
       "trapEDFAKeySwitch": trapEDFAKeySwitch,
       "trapEDFAPowerFail": trapEDFAPowerFail,
       "trapEDFALasCurrShutdown": trapEDFALasCurrShutdown,
       "trapEDFALasPowerShutdown": trapEDFALasPowerShutdown,
       "trapEDFAInvalidMode": trapEDFAInvalidMode,
       "trapEDFAFlashAlarm": trapEDFAFlashAlarm,
       "trapEDFABoot0Alarm": trapEDFABoot0Alarm,
       "trapEDFABoot1Alarm": trapEDFABoot1Alarm,
       "trapEDFAAlarmDataCRCAlarm": trapEDFAAlarmDataCRCAlarm,
       "trapEDFAFactoryDataCRCAlarm": trapEDFAFactoryDataCRCAlarm,
       "trapEDFACalDataCRCAlarm": trapEDFACalDataCRCAlarm,
       "trapEDFAFacCalFloatAlarm": trapEDFAFacCalFloatAlarm,
       "trapEDFAOptInThreshAlarm": trapEDFAOptInThreshAlarm,
       "trapEDFAGainErrorAlarm": trapEDFAGainErrorAlarm,
       "gx2EDFADescriptor": gx2EDFADescriptor,
       "gx2EDFAAnalogTable": gx2EDFAAnalogTable,
       "gx2EDFAAnalogEntry": gx2EDFAAnalogEntry,
       "edfagx2EDFAAnalogTableIndex": edfagx2EDFAAnalogTableIndex,
       "edfalabelModTemp": edfalabelModTemp,
       "edfauomModTemp": edfauomModTemp,
       "edfamajorHighModTemp": edfamajorHighModTemp,
       "edfamajorLowModTemp": edfamajorLowModTemp,
       "edfaminorHighModTemp": edfaminorHighModTemp,
       "edfaminorLowModTemp": edfaminorLowModTemp,
       "edfacurrentValueModTemp": edfacurrentValueModTemp,
       "edfastateFlagModTemp": edfastateFlagModTemp,
       "edfaminValueModTemp": edfaminValueModTemp,
       "edfamaxValueModTemp": edfamaxValueModTemp,
       "edfaalarmStateModTemp": edfaalarmStateModTemp,
       "edfalabelOptInPower": edfalabelOptInPower,
       "edfauomOptInPower": edfauomOptInPower,
       "edfamajorHighOptInPower": edfamajorHighOptInPower,
       "edfamajorLowOptInPower": edfamajorLowOptInPower,
       "edfaminorHighOptInPower": edfaminorHighOptInPower,
       "edfaminorLowOptInPower": edfaminorLowOptInPower,
       "edfacurrentValueOptInPower": edfacurrentValueOptInPower,
       "edfastateFlagOptInPower": edfastateFlagOptInPower,
       "edfaminValueOptInPower": edfaminValueOptInPower,
       "edfamaxValueOptInPower": edfamaxValueOptInPower,
       "edfaalarmStateOptInPower": edfaalarmStateOptInPower,
       "edfalabelOptOutPower": edfalabelOptOutPower,
       "edfauomOptOutPower": edfauomOptOutPower,
       "edfamajorHighOptOutPower": edfamajorHighOptOutPower,
       "edfamajorLowOptOutPower": edfamajorLowOptOutPower,
       "edfaminorHighOptOutPower": edfaminorHighOptOutPower,
       "edfaminorLowOptOutPower": edfaminorLowOptOutPower,
       "edfacurrentValueOptOutPower": edfacurrentValueOptOutPower,
       "edfastateFlagOptOutPower": edfastateFlagOptOutPower,
       "edfaminValueOptOutPower": edfaminValueOptOutPower,
       "edfamaxValueOptOutPower": edfamaxValueOptOutPower,
       "edfaalarmStateOptOutPower": edfaalarmStateOptOutPower,
       "edfalabelTECTemp": edfalabelTECTemp,
       "edfauomTECTemp": edfauomTECTemp,
       "edfamajorHighTECTemp": edfamajorHighTECTemp,
       "edfamajorLowTECTemp": edfamajorLowTECTemp,
       "edfaminorHighTECTemp": edfaminorHighTECTemp,
       "edfaminorLowTECTemp": edfaminorLowTECTemp,
       "edfacurrentValueTECTemp": edfacurrentValueTECTemp,
       "edfastateFlagTECTemp": edfastateFlagTECTemp,
       "edfaminValueTECTemp": edfaminValueTECTemp,
       "edfamaxValueTECTemp": edfamaxValueTECTemp,
       "edfaalarmStateTECTemp": edfaalarmStateTECTemp,
       "edfalabelTECCurrent": edfalabelTECCurrent,
       "edfauomTECCurrent": edfauomTECCurrent,
       "edfamajorHighTECCurrent": edfamajorHighTECCurrent,
       "edfamajorLowTECCurrent": edfamajorLowTECCurrent,
       "edfaminorHighTECCurrent": edfaminorHighTECCurrent,
       "edfaminorLowTECCurrent": edfaminorLowTECCurrent,
       "edfacurrentValueTECCurrent": edfacurrentValueTECCurrent,
       "edfastateFlagTECCurrent": edfastateFlagTECCurrent,
       "edfaminValueTECCurrent": edfaminValueTECCurrent,
       "edfamaxValueTECCurrent": edfamaxValueTECCurrent,
       "edfaalarmStateTECCurrent": edfaalarmStateTECCurrent,
       "edfalabelLaserCurrent": edfalabelLaserCurrent,
       "edfauomLaserCurrent": edfauomLaserCurrent,
       "edfamajorHighLaserCurrent": edfamajorHighLaserCurrent,
       "edfamajorLowLaserCurrent": edfamajorLowLaserCurrent,
       "edfaminorHighLaserCurrent": edfaminorHighLaserCurrent,
       "edfaminorLowLaserCurrent": edfaminorLowLaserCurrent,
       "edfacurrentValueLaserCurrent": edfacurrentValueLaserCurrent,
       "edfastateFlagLaserCurrent": edfastateFlagLaserCurrent,
       "edfaminValueLaserCurrent": edfaminValueLaserCurrent,
       "edfamaxValueLaserCurrent": edfamaxValueLaserCurrent,
       "edfaalarmStateLaserCurrent": edfaalarmStateLaserCurrent,
       "edfalabelLaserPower": edfalabelLaserPower,
       "edfauomLaserPower": edfauomLaserPower,
       "edfamajorHighLaserPower": edfamajorHighLaserPower,
       "edfamajorLowLaserPower": edfamajorLowLaserPower,
       "edfaminorHighLaserPower": edfaminorHighLaserPower,
       "edfaminorLowLaserPower": edfaminorLowLaserPower,
       "edfacurrentValueLaserPower": edfacurrentValueLaserPower,
       "edfastateFlagLaserPower": edfastateFlagLaserPower,
       "edfaminValueLaserPower": edfaminValueLaserPower,
       "edfamaxValueLaserPower": edfamaxValueLaserPower,
       "edfaalarmStateLaserPower": edfaalarmStateLaserPower,
       "edfalabel12Volt": edfalabel12Volt,
       "edfauom12Volt": edfauom12Volt,
       "edfamajorHigh12Volt": edfamajorHigh12Volt,
       "edfamajorLow12Volt": edfamajorLow12Volt,
       "edfaminorHigh12Volt": edfaminorHigh12Volt,
       "edfaminorLow12Volt": edfaminorLow12Volt,
       "edfacurrentValue12Volt": edfacurrentValue12Volt,
       "edfastateFlag12Volt": edfastateFlag12Volt,
       "edfaminValue12Volt": edfaminValue12Volt,
       "edfamaxValue12Volt": edfamaxValue12Volt,
       "edfaalarmState12Volt": edfaalarmState12Volt,
       "edfalabel37Volt": edfalabel37Volt,
       "edfauom37Volt": edfauom37Volt,
       "edfamajorHigh37Volt": edfamajorHigh37Volt,
       "edfamajorLow37Volt": edfamajorLow37Volt,
       "edfaminorHigh37Volt": edfaminorHigh37Volt,
       "edfaminorLow37Volt": edfaminorLow37Volt,
       "edfacurrentValue37Volt": edfacurrentValue37Volt,
       "edfastateFlag37Volt": edfastateFlag37Volt,
       "edfaminValue37Volt": edfaminValue37Volt,
       "edfamaxValue37Volt": edfamaxValue37Volt,
       "edfaalarmState37Volt": edfaalarmState37Volt,
       "edfalabelFanCurrent": edfalabelFanCurrent,
       "edfauomFanCurrent": edfauomFanCurrent,
       "edfamajorHighFanCurrent": edfamajorHighFanCurrent,
       "edfamajorLowFanCurrent": edfamajorLowFanCurrent,
       "edfaminorHighFanCurrent": edfaminorHighFanCurrent,
       "edfaminorLowFanCurrent": edfaminorLowFanCurrent,
       "edfacurrentValueFanCurrent": edfacurrentValueFanCurrent,
       "edfastateFlagFanCurrent": edfastateFlagFanCurrent,
       "edfaminValueFanCurrent": edfaminValueFanCurrent,
       "edfamaxValueFanCurrent": edfamaxValueFanCurrent,
       "edfaalarmStateFanCurrent": edfaalarmStateFanCurrent,
       "edfalabelOPSetting": edfalabelOPSetting,
       "edfauomOPSetting": edfauomOPSetting,
       "edfamajorHighOPSetting": edfamajorHighOPSetting,
       "edfamajorLowOPSetting": edfamajorLowOPSetting,
       "edfaminorHighOPSetting": edfaminorHighOPSetting,
       "edfaminorLowOPSetting": edfaminorLowOPSetting,
       "edfacurrentValueOPSetting": edfacurrentValueOPSetting,
       "edfastateFlagOPSetting": edfastateFlagOPSetting,
       "edfaminValueOPSetting": edfaminValueOPSetting,
       "edfamaxValueOPSetting": edfamaxValueOPSetting,
       "edfaalarmStateOPSetting": edfaalarmStateOPSetting,
       "edfalabelLPSetting": edfalabelLPSetting,
       "edfauomLPSetting": edfauomLPSetting,
       "edfamajorHighLPSetting": edfamajorHighLPSetting,
       "edfamajorLowLPSetting": edfamajorLowLPSetting,
       "edfaminorHighLPSetting": edfaminorHighLPSetting,
       "edfaminorLowLPSetting": edfaminorLowLPSetting,
       "edfacurrentValueLPSetting": edfacurrentValueLPSetting,
       "edfastateFlagLPSetting": edfastateFlagLPSetting,
       "edfaminValueLPSetting": edfaminValueLPSetting,
       "edfamaxValueLPSetting": edfamaxValueLPSetting,
       "edfaalarmStateLPSetting": edfaalarmStateLPSetting,
       "edfalabelCGSetting": edfalabelCGSetting,
       "edfauomCGSetting": edfauomCGSetting,
       "edfamajorHighCGSetting": edfamajorHighCGSetting,
       "edfamajorLowCGSetting": edfamajorLowCGSetting,
       "edfaminorHighCGSetting": edfaminorHighCGSetting,
       "edfaminorLowCGSetting": edfaminorLowCGSetting,
       "edfacurrentValueCGSetting": edfacurrentValueCGSetting,
       "edfastateFlagCGSetting": edfastateFlagCGSetting,
       "edfaminValueCGSetting": edfaminValueCGSetting,
       "edfamaxValueCGSetting": edfamaxValueCGSetting,
       "edfaalarmStateCGSetting": edfaalarmStateCGSetting,
       "edfalabelOptThreshold": edfalabelOptThreshold,
       "edfauomOptThreshold": edfauomOptThreshold,
       "edfamajorHighOptThreshold": edfamajorHighOptThreshold,
       "edfamajorLowOptThreshold": edfamajorLowOptThreshold,
       "edfaminorHighOptThreshold": edfaminorHighOptThreshold,
       "edfaminorLowOptThreshold": edfaminorLowOptThreshold,
       "edfacurrentValueOptThreshold": edfacurrentValueOptThreshold,
       "edfastateFlagOptThreshold": edfastateFlagOptThreshold,
       "edfaminValueOptThreshold": edfaminValueOptThreshold,
       "edfamaxValueOptThreshold": edfamaxValueOptThreshold,
       "edfaalarmStateOptThreshold": edfaalarmStateOptThreshold,
       "gx2EDFADigitalTable": gx2EDFADigitalTable,
       "gx2EDFADigitalEntry": gx2EDFADigitalEntry,
       "edfagx2EDFADigitalTableIndex": edfagx2EDFADigitalTableIndex,
       "edfalabelModeSetting": edfalabelModeSetting,
       "edfaenumModeSetting": edfaenumModeSetting,
       "edfavalueModeSetting": edfavalueModeSetting,
       "edfastateFlagModeSetting": edfastateFlagModeSetting,
       "edfalabelModuleState": edfalabelModuleState,
       "edfaenumModuleState": edfaenumModuleState,
       "edfavalueModuleState": edfavalueModuleState,
       "edfastateFlagModuleState": edfastateFlagModuleState,
       "edfalabelFactoryDefault": edfalabelFactoryDefault,
       "edfaenumFactoryDefault": edfaenumFactoryDefault,
       "edfavalueFactoryDefault": edfavalueFactoryDefault,
       "edfastateFlagFactoryDefault": edfastateFlagFactoryDefault,
       "gx2EDFAStatusTable": gx2EDFAStatusTable,
       "gx2EDFAStatusEntry": gx2EDFAStatusEntry,
       "edfagx2EDFAStatusTableIndex": edfagx2EDFAStatusTableIndex,
       "edfalabelBoot": edfalabelBoot,
       "edfavalueBoot": edfavalueBoot,
       "edfastateflagBoot": edfastateflagBoot,
       "edfalabelFlash": edfalabelFlash,
       "edfavalueFlash": edfavalueFlash,
       "edfastateflagFlash": edfastateflagFlash,
       "edfalabelFactoryDataCRC": edfalabelFactoryDataCRC,
       "edfavalueFactoryDataCRC": edfavalueFactoryDataCRC,
       "edfastateflagFactoryDataCRC": edfastateflagFactoryDataCRC,
       "edfalabelAlarmDataCRC": edfalabelAlarmDataCRC,
       "edfavalueAlarmDataCRC": edfavalueAlarmDataCRC,
       "edfastateflagAlarmDataCRC": edfastateflagAlarmDataCRC,
       "edfalabelCalibrationDataCRC": edfalabelCalibrationDataCRC,
       "edfavalueCalibrationDataCRC": edfavalueCalibrationDataCRC,
       "edfastateflagCalibrationDataCRC": edfastateflagCalibrationDataCRC,
       "edfalabelOptInShutdown": edfalabelOptInShutdown,
       "edfavalueOptInShutdown": edfavalueOptInShutdown,
       "edfastateflagOptInShutdown": edfastateflagOptInShutdown,
       "edfalabelTECTempShutdown": edfalabelTECTempShutdown,
       "edfavalueTECTempShutdown": edfavalueTECTempShutdown,
       "edfastateflagTECTempShutdown": edfastateflagTECTempShutdown,
       "edfalabelTECShutOverride": edfalabelTECShutOverride,
       "edfavalueTECShutOverride": edfavalueTECShutOverride,
       "edfastateflagTECShutOverride": edfastateflagTECShutOverride,
       "edfalabelPowerFail": edfalabelPowerFail,
       "edfavaluePowerFail": edfavaluePowerFail,
       "edfastateflagPowerFail": edfastateflagPowerFail,
       "edfalabelKeySwitch": edfalabelKeySwitch,
       "edfavalueKeySwitch": edfavalueKeySwitch,
       "edfastateflagKeySwitch": edfastateflagKeySwitch,
       "edfalabelLaserCurrShutdown": edfalabelLaserCurrShutdown,
       "edfavalueLaserCurrShutdown": edfavalueLaserCurrShutdown,
       "edfastateflagLaserCurrShutdown": edfastateflagLaserCurrShutdown,
       "edfalabelLaserPowShutdown": edfalabelLaserPowShutdown,
       "edfavalueLaserPowShutdown": edfavalueLaserPowShutdown,
       "edfastateflagLaserPowShutdown": edfastateflagLaserPowShutdown,
       "edfalabelADCStatus": edfalabelADCStatus,
       "edfavalueADCStatus": edfavalueADCStatus,
       "edfastateflagADCStatus": edfastateflagADCStatus,
       "edfalabelConstGainStatus": edfalabelConstGainStatus,
       "edfavalueConstGainStatus": edfavalueConstGainStatus,
       "edfastateflagConstGainStatus": edfastateflagConstGainStatus,
       "edfalabelStandbyStatus": edfalabelStandbyStatus,
       "edfavalueStandbyStatus": edfavalueStandbyStatus,
       "edfastateflagStandbyStatus": edfastateflagStandbyStatus,
       "gx2EDFAFactoryTable": gx2EDFAFactoryTable,
       "gx2EDFAFactoryEntry": gx2EDFAFactoryEntry,
       "edfagx2EDFAFactoryTableIndex": edfagx2EDFAFactoryTableIndex,
       "edfabootControlByte": edfabootControlByte,
       "edfabootStatusByte": edfabootStatusByte,
       "edfabank0CRC": edfabank0CRC,
       "edfabank1CRC": edfabank1CRC,
       "edfaprgEEPROMByte": edfaprgEEPROMByte,
       "edfafactoryCRC": edfafactoryCRC,
       "edfacalculateCRC": edfacalculateCRC,
       "edfahourMeter": edfahourMeter,
       "edfaflashPrgCntA": edfaflashPrgCntA,
       "edfaflashPrgCntB": edfaflashPrgCntB,
       "edfafwRev0": edfafwRev0,
       "edfafwRev1": edfafwRev1,
       "gx2EDFAHoldTimeTable": gx2EDFAHoldTimeTable,
       "gx2EDFAHoldTimeEntry": gx2EDFAHoldTimeEntry,
       "gx2EDFAHoldTimeTableIndex": gx2EDFAHoldTimeTableIndex,
       "gx2EDFAHoldTimeSpecIndex": gx2EDFAHoldTimeSpecIndex,
       "gx2EDFAHoldTimeData": gx2EDFAHoldTimeData}
)
