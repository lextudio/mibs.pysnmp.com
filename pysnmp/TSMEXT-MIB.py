# SNMP MIB module (TSMEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TSMEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:52 2024
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

(xylanTsmArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanTsmArch")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TsmExtensions_ObjectIdentity = ObjectIdentity
tsmExtensions = _TsmExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1)
)
_TsmAdmin_ObjectIdentity = ObjectIdentity
tsmAdmin = _TsmAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1)
)
_TsmAdminPortTable_Object = MibTable
tsmAdminPortTable = _TsmAdminPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tsmAdminPortTable.setStatus("mandatory")
_TsmAdminPortEntry_Object = MibTableRow
tsmAdminPortEntry = _TsmAdminPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1)
)
tsmAdminPortEntry.setIndexNames(
    (0, "TSMEXT-MIB", "tsmAdminPortSlotNumber"),
    (0, "TSMEXT-MIB", "tsmAdminPortNumber"),
)
if mibBuilder.loadTexts:
    tsmAdminPortEntry.setStatus("mandatory")
_TsmAdminPortSlotNumber_Type = Integer32
_TsmAdminPortSlotNumber_Object = MibTableColumn
tsmAdminPortSlotNumber = _TsmAdminPortSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 1),
    _TsmAdminPortSlotNumber_Type()
)
tsmAdminPortSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmAdminPortSlotNumber.setStatus("mandatory")
_TsmAdminPortNumber_Type = Integer32
_TsmAdminPortNumber_Object = MibTableColumn
tsmAdminPortNumber = _TsmAdminPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 2),
    _TsmAdminPortNumber_Type()
)
tsmAdminPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmAdminPortNumber.setStatus("mandatory")


class _TsmAdminPortState_Type(Integer32):
    """Custom type tsmAdminPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsmAdminPortState_Type.__name__ = "Integer32"
_TsmAdminPortState_Object = MibTableColumn
tsmAdminPortState = _TsmAdminPortState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 3),
    _TsmAdminPortState_Type()
)
tsmAdminPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminPortState.setStatus("mandatory")


class _TsmAdminPortActiveMon_Type(Integer32):
    """Custom type tsmAdminPortActiveMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_TsmAdminPortActiveMon_Type.__name__ = "Integer32"
_TsmAdminPortActiveMon_Object = MibTableColumn
tsmAdminPortActiveMon = _TsmAdminPortActiveMon_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 4),
    _TsmAdminPortActiveMon_Type()
)
tsmAdminPortActiveMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminPortActiveMon.setStatus("mandatory")


class _TsmAdminPortAcBitSet_Type(Integer32):
    """Custom type tsmAdminPortAcBitSet based on Integer32"""
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
        *(("always", 3),
          ("never", 4),
          ("nonLocal", 1),
          ("repeat", 2))
    )


_TsmAdminPortAcBitSet_Type.__name__ = "Integer32"
_TsmAdminPortAcBitSet_Object = MibTableColumn
tsmAdminPortAcBitSet = _TsmAdminPortAcBitSet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 5),
    _TsmAdminPortAcBitSet_Type()
)
tsmAdminPortAcBitSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminPortAcBitSet.setStatus("mandatory")


class _TsmAdminPortConfigType_Type(Integer32):
    """Custom type tsmAdminPortConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_TsmAdminPortConfigType_Type.__name__ = "Integer32"
_TsmAdminPortConfigType_Object = MibTableColumn
tsmAdminPortConfigType = _TsmAdminPortConfigType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 6),
    _TsmAdminPortConfigType_Type()
)
tsmAdminPortConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminPortConfigType.setStatus("mandatory")


class _TsmAdminPortRingSpeed_Type(Integer32):
    """Custom type tsmAdminPortRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fourMegabit", 2),
          ("sixteenMegabit", 3))
    )


_TsmAdminPortRingSpeed_Type.__name__ = "Integer32"
_TsmAdminPortRingSpeed_Object = MibTableColumn
tsmAdminPortRingSpeed = _TsmAdminPortRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 7),
    _TsmAdminPortRingSpeed_Type()
)
tsmAdminPortRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminPortRingSpeed.setStatus("mandatory")


class _TsmAdminPortPortMode_Type(Integer32):
    """Custom type tsmAdminPortPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adapterMode", 3),
          ("auto", 1),
          ("portMode", 2))
    )


_TsmAdminPortPortMode_Type.__name__ = "Integer32"
_TsmAdminPortPortMode_Object = MibTableColumn
tsmAdminPortPortMode = _TsmAdminPortPortMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 8),
    _TsmAdminPortPortMode_Type()
)
tsmAdminPortPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminPortPortMode.setStatus("mandatory")


class _TsmAdminPortDuplex_Type(Integer32):
    """Custom type tsmAdminPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fullDuplex", 3),
          ("halfDuplex", 2))
    )


_TsmAdminPortDuplex_Type.__name__ = "Integer32"
_TsmAdminPortDuplex_Object = MibTableColumn
tsmAdminPortDuplex = _TsmAdminPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 9),
    _TsmAdminPortDuplex_Type()
)
tsmAdminPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminPortDuplex.setStatus("mandatory")


class _TsmAdminPortSwMode_Type(Integer32):
    """Custom type tsmAdminPortSwMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("cutThrough", 1),
          ("storeAndForward", 2))
    )


_TsmAdminPortSwMode_Type.__name__ = "Integer32"
_TsmAdminPortSwMode_Object = MibTableColumn
tsmAdminPortSwMode = _TsmAdminPortSwMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 10),
    _TsmAdminPortSwMode_Type()
)
tsmAdminPortSwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminPortSwMode.setStatus("mandatory")


class _TsmAdminPortReset_Type(Integer32):
    """Custom type tsmAdminPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("reset", 2))
    )


_TsmAdminPortReset_Type.__name__ = "Integer32"
_TsmAdminPortReset_Object = MibTableColumn
tsmAdminPortReset = _TsmAdminPortReset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 11),
    _TsmAdminPortReset_Type()
)
tsmAdminPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminPortReset.setStatus("mandatory")
_TsmAdminSwModeTable_Object = MibTable
tsmAdminSwModeTable = _TsmAdminSwModeTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tsmAdminSwModeTable.setStatus("mandatory")
_TsmAdminSwModeEntry_Object = MibTableRow
tsmAdminSwModeEntry = _TsmAdminSwModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1)
)
tsmAdminSwModeEntry.setIndexNames(
    (0, "TSMEXT-MIB", "tsmAdminSwModeSlotNumber"),
)
if mibBuilder.loadTexts:
    tsmAdminSwModeEntry.setStatus("mandatory")
_TsmAdminSwModeSlotNumber_Type = Integer32
_TsmAdminSwModeSlotNumber_Object = MibTableColumn
tsmAdminSwModeSlotNumber = _TsmAdminSwModeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 1),
    _TsmAdminSwModeSlotNumber_Type()
)
tsmAdminSwModeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmAdminSwModeSlotNumber.setStatus("mandatory")


class _TsmAdminSwModeHiErrThresh_Type(Integer32):
    """Custom type tsmAdminSwModeHiErrThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsmAdminSwModeHiErrThresh_Type.__name__ = "Integer32"
_TsmAdminSwModeHiErrThresh_Object = MibTableColumn
tsmAdminSwModeHiErrThresh = _TsmAdminSwModeHiErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 2),
    _TsmAdminSwModeHiErrThresh_Type()
)
tsmAdminSwModeHiErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminSwModeHiErrThresh.setStatus("mandatory")


class _TsmAdminSwModeLoErrThresh_Type(Integer32):
    """Custom type tsmAdminSwModeLoErrThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsmAdminSwModeLoErrThresh_Type.__name__ = "Integer32"
_TsmAdminSwModeLoErrThresh_Object = MibTableColumn
tsmAdminSwModeLoErrThresh = _TsmAdminSwModeLoErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 3),
    _TsmAdminSwModeLoErrThresh_Type()
)
tsmAdminSwModeLoErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminSwModeLoErrThresh.setStatus("mandatory")


class _TsmAdminSwModeTrendThresh_Type(Integer32):
    """Custom type tsmAdminSwModeTrendThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsmAdminSwModeTrendThresh_Type.__name__ = "Integer32"
_TsmAdminSwModeTrendThresh_Object = MibTableColumn
tsmAdminSwModeTrendThresh = _TsmAdminSwModeTrendThresh_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 4),
    _TsmAdminSwModeTrendThresh_Type()
)
tsmAdminSwModeTrendThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminSwModeTrendThresh.setStatus("mandatory")


class _TsmAdminSwModeSamplePeriod_Type(Integer32):
    """Custom type tsmAdminSwModeSamplePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_TsmAdminSwModeSamplePeriod_Type.__name__ = "Integer32"
_TsmAdminSwModeSamplePeriod_Object = MibTableColumn
tsmAdminSwModeSamplePeriod = _TsmAdminSwModeSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 5),
    _TsmAdminSwModeSamplePeriod_Type()
)
tsmAdminSwModeSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminSwModeSamplePeriod.setStatus("mandatory")


class _TsmAdminSwModeReset_Type(Integer32):
    """Custom type tsmAdminSwModeReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("reset", 2))
    )


_TsmAdminSwModeReset_Type.__name__ = "Integer32"
_TsmAdminSwModeReset_Object = MibTableColumn
tsmAdminSwModeReset = _TsmAdminSwModeReset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 6),
    _TsmAdminSwModeReset_Type()
)
tsmAdminSwModeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsmAdminSwModeReset.setStatus("mandatory")
_TsmOper_ObjectIdentity = ObjectIdentity
tsmOper = _TsmOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2)
)
_TsmOperPortTable_Object = MibTable
tsmOperPortTable = _TsmOperPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tsmOperPortTable.setStatus("mandatory")
_TsmOperPortEntry_Object = MibTableRow
tsmOperPortEntry = _TsmOperPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1)
)
tsmOperPortEntry.setIndexNames(
    (0, "TSMEXT-MIB", "tsmOperPortSlotNumber"),
    (0, "TSMEXT-MIB", "tsmOperPortNumber"),
)
if mibBuilder.loadTexts:
    tsmOperPortEntry.setStatus("mandatory")
_TsmOperPortSlotNumber_Type = Integer32
_TsmOperPortSlotNumber_Object = MibTableColumn
tsmOperPortSlotNumber = _TsmOperPortSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 1),
    _TsmOperPortSlotNumber_Type()
)
tsmOperPortSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortSlotNumber.setStatus("mandatory")
_TsmOperPortNumber_Type = Integer32
_TsmOperPortNumber_Object = MibTableColumn
tsmOperPortNumber = _TsmOperPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 2),
    _TsmOperPortNumber_Type()
)
tsmOperPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortNumber.setStatus("mandatory")


class _TsmOperPortState_Type(Integer32):
    """Custom type tsmOperPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TsmOperPortState_Type.__name__ = "Integer32"
_TsmOperPortState_Object = MibTableColumn
tsmOperPortState = _TsmOperPortState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 3),
    _TsmOperPortState_Type()
)
tsmOperPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortState.setStatus("mandatory")


class _TsmOperPortActiveMon_Type(Integer32):
    """Custom type tsmOperPortActiveMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_TsmOperPortActiveMon_Type.__name__ = "Integer32"
_TsmOperPortActiveMon_Object = MibTableColumn
tsmOperPortActiveMon = _TsmOperPortActiveMon_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 4),
    _TsmOperPortActiveMon_Type()
)
tsmOperPortActiveMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortActiveMon.setStatus("mandatory")


class _TsmOperPortAcBitSet_Type(Integer32):
    """Custom type tsmOperPortAcBitSet based on Integer32"""
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
        *(("always", 3),
          ("never", 4),
          ("nonLocal", 1),
          ("repeat", 2))
    )


_TsmOperPortAcBitSet_Type.__name__ = "Integer32"
_TsmOperPortAcBitSet_Object = MibTableColumn
tsmOperPortAcBitSet = _TsmOperPortAcBitSet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 5),
    _TsmOperPortAcBitSet_Type()
)
tsmOperPortAcBitSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortAcBitSet.setStatus("mandatory")


class _TsmOperPortConfigType_Type(Integer32):
    """Custom type tsmOperPortConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_TsmOperPortConfigType_Type.__name__ = "Integer32"
_TsmOperPortConfigType_Object = MibTableColumn
tsmOperPortConfigType = _TsmOperPortConfigType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 6),
    _TsmOperPortConfigType_Type()
)
tsmOperPortConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortConfigType.setStatus("mandatory")


class _TsmOperPortRingSpeed_Type(Integer32):
    """Custom type tsmOperPortRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fourMegabit", 2),
          ("sixteenMegabit", 3))
    )


_TsmOperPortRingSpeed_Type.__name__ = "Integer32"
_TsmOperPortRingSpeed_Object = MibTableColumn
tsmOperPortRingSpeed = _TsmOperPortRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 7),
    _TsmOperPortRingSpeed_Type()
)
tsmOperPortRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortRingSpeed.setStatus("mandatory")


class _TsmOperPortPortMode_Type(Integer32):
    """Custom type tsmOperPortPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adapterMode", 3),
          ("auto", 1),
          ("portMode", 2))
    )


_TsmOperPortPortMode_Type.__name__ = "Integer32"
_TsmOperPortPortMode_Object = MibTableColumn
tsmOperPortPortMode = _TsmOperPortPortMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 8),
    _TsmOperPortPortMode_Type()
)
tsmOperPortPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortPortMode.setStatus("mandatory")


class _TsmOperPortDuplex_Type(Integer32):
    """Custom type tsmOperPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fullDuplex", 3),
          ("halfDuplex", 2))
    )


_TsmOperPortDuplex_Type.__name__ = "Integer32"
_TsmOperPortDuplex_Object = MibTableColumn
tsmOperPortDuplex = _TsmOperPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 9),
    _TsmOperPortDuplex_Type()
)
tsmOperPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortDuplex.setStatus("mandatory")


class _TsmOperPortSwMode_Type(Integer32):
    """Custom type tsmOperPortSwMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("cutThrough", 1),
          ("storeAndForward", 2))
    )


_TsmOperPortSwMode_Type.__name__ = "Integer32"
_TsmOperPortSwMode_Object = MibTableColumn
tsmOperPortSwMode = _TsmOperPortSwMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 10),
    _TsmOperPortSwMode_Type()
)
tsmOperPortSwMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortSwMode.setStatus("mandatory")


class _TsmOperPortAdaptSwMode_Type(Integer32):
    """Custom type tsmOperPortAdaptSwMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cutThrough", 1),
          ("notAdaptive", 3),
          ("storeAndForward", 2))
    )


_TsmOperPortAdaptSwMode_Type.__name__ = "Integer32"
_TsmOperPortAdaptSwMode_Object = MibTableColumn
tsmOperPortAdaptSwMode = _TsmOperPortAdaptSwMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 11),
    _TsmOperPortAdaptSwMode_Type()
)
tsmOperPortAdaptSwMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortAdaptSwMode.setStatus("mandatory")
_TsmOperPortAdaptErrRate_Type = Integer32
_TsmOperPortAdaptErrRate_Object = MibTableColumn
tsmOperPortAdaptErrRate = _TsmOperPortAdaptErrRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 12),
    _TsmOperPortAdaptErrRate_Type()
)
tsmOperPortAdaptErrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortAdaptErrRate.setStatus("mandatory")
_TsmOperPortAdaptTrend_Type = Integer32
_TsmOperPortAdaptTrend_Object = MibTableColumn
tsmOperPortAdaptTrend = _TsmOperPortAdaptTrend_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 13),
    _TsmOperPortAdaptTrend_Type()
)
tsmOperPortAdaptTrend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortAdaptTrend.setStatus("mandatory")


class _TsmOperPortOpenState_Type(Integer32):
    """Custom type tsmOperPortOpenState based on Integer32"""
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
        *(("closed", 2),
          ("closing", 4),
          ("openFailure", 5),
          ("opened", 1),
          ("opening", 3),
          ("ringFailure", 6))
    )


_TsmOperPortOpenState_Type.__name__ = "Integer32"
_TsmOperPortOpenState_Object = MibTableColumn
tsmOperPortOpenState = _TsmOperPortOpenState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 14),
    _TsmOperPortOpenState_Type()
)
tsmOperPortOpenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortOpenState.setStatus("mandatory")
_TsmOperPortUpStream_Type = MacAddress
_TsmOperPortUpStream_Object = MibTableColumn
tsmOperPortUpStream = _TsmOperPortUpStream_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 15),
    _TsmOperPortUpStream_Type()
)
tsmOperPortUpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperPortUpStream.setStatus("mandatory")
_TsmOperSwModeTable_Object = MibTable
tsmOperSwModeTable = _TsmOperSwModeTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tsmOperSwModeTable.setStatus("mandatory")
_TsmOperSwModeEntry_Object = MibTableRow
tsmOperSwModeEntry = _TsmOperSwModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1)
)
tsmOperSwModeEntry.setIndexNames(
    (0, "TSMEXT-MIB", "tsmOperSwModeSlotNumber"),
)
if mibBuilder.loadTexts:
    tsmOperSwModeEntry.setStatus("mandatory")
_TsmOperSwModeSlotNumber_Type = Integer32
_TsmOperSwModeSlotNumber_Object = MibTableColumn
tsmOperSwModeSlotNumber = _TsmOperSwModeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 1),
    _TsmOperSwModeSlotNumber_Type()
)
tsmOperSwModeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperSwModeSlotNumber.setStatus("mandatory")


class _TsmOperSwModeHiErrThresh_Type(Integer32):
    """Custom type tsmOperSwModeHiErrThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsmOperSwModeHiErrThresh_Type.__name__ = "Integer32"
_TsmOperSwModeHiErrThresh_Object = MibTableColumn
tsmOperSwModeHiErrThresh = _TsmOperSwModeHiErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 2),
    _TsmOperSwModeHiErrThresh_Type()
)
tsmOperSwModeHiErrThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperSwModeHiErrThresh.setStatus("mandatory")


class _TsmOperSwModeLoErrThresh_Type(Integer32):
    """Custom type tsmOperSwModeLoErrThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsmOperSwModeLoErrThresh_Type.__name__ = "Integer32"
_TsmOperSwModeLoErrThresh_Object = MibTableColumn
tsmOperSwModeLoErrThresh = _TsmOperSwModeLoErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 3),
    _TsmOperSwModeLoErrThresh_Type()
)
tsmOperSwModeLoErrThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperSwModeLoErrThresh.setStatus("mandatory")


class _TsmOperSwModeTrendThresh_Type(Integer32):
    """Custom type tsmOperSwModeTrendThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsmOperSwModeTrendThresh_Type.__name__ = "Integer32"
_TsmOperSwModeTrendThresh_Object = MibTableColumn
tsmOperSwModeTrendThresh = _TsmOperSwModeTrendThresh_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 4),
    _TsmOperSwModeTrendThresh_Type()
)
tsmOperSwModeTrendThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperSwModeTrendThresh.setStatus("mandatory")


class _TsmOperSwModeSamplePeriod_Type(Integer32):
    """Custom type tsmOperSwModeSamplePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_TsmOperSwModeSamplePeriod_Type.__name__ = "Integer32"
_TsmOperSwModeSamplePeriod_Object = MibTableColumn
tsmOperSwModeSamplePeriod = _TsmOperSwModeSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 5),
    _TsmOperSwModeSamplePeriod_Type()
)
tsmOperSwModeSamplePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsmOperSwModeSamplePeriod.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TSMEXT-MIB",
    **{"MacAddress": MacAddress,
       "tsmExtensions": tsmExtensions,
       "tsmAdmin": tsmAdmin,
       "tsmAdminPortTable": tsmAdminPortTable,
       "tsmAdminPortEntry": tsmAdminPortEntry,
       "tsmAdminPortSlotNumber": tsmAdminPortSlotNumber,
       "tsmAdminPortNumber": tsmAdminPortNumber,
       "tsmAdminPortState": tsmAdminPortState,
       "tsmAdminPortActiveMon": tsmAdminPortActiveMon,
       "tsmAdminPortAcBitSet": tsmAdminPortAcBitSet,
       "tsmAdminPortConfigType": tsmAdminPortConfigType,
       "tsmAdminPortRingSpeed": tsmAdminPortRingSpeed,
       "tsmAdminPortPortMode": tsmAdminPortPortMode,
       "tsmAdminPortDuplex": tsmAdminPortDuplex,
       "tsmAdminPortSwMode": tsmAdminPortSwMode,
       "tsmAdminPortReset": tsmAdminPortReset,
       "tsmAdminSwModeTable": tsmAdminSwModeTable,
       "tsmAdminSwModeEntry": tsmAdminSwModeEntry,
       "tsmAdminSwModeSlotNumber": tsmAdminSwModeSlotNumber,
       "tsmAdminSwModeHiErrThresh": tsmAdminSwModeHiErrThresh,
       "tsmAdminSwModeLoErrThresh": tsmAdminSwModeLoErrThresh,
       "tsmAdminSwModeTrendThresh": tsmAdminSwModeTrendThresh,
       "tsmAdminSwModeSamplePeriod": tsmAdminSwModeSamplePeriod,
       "tsmAdminSwModeReset": tsmAdminSwModeReset,
       "tsmOper": tsmOper,
       "tsmOperPortTable": tsmOperPortTable,
       "tsmOperPortEntry": tsmOperPortEntry,
       "tsmOperPortSlotNumber": tsmOperPortSlotNumber,
       "tsmOperPortNumber": tsmOperPortNumber,
       "tsmOperPortState": tsmOperPortState,
       "tsmOperPortActiveMon": tsmOperPortActiveMon,
       "tsmOperPortAcBitSet": tsmOperPortAcBitSet,
       "tsmOperPortConfigType": tsmOperPortConfigType,
       "tsmOperPortRingSpeed": tsmOperPortRingSpeed,
       "tsmOperPortPortMode": tsmOperPortPortMode,
       "tsmOperPortDuplex": tsmOperPortDuplex,
       "tsmOperPortSwMode": tsmOperPortSwMode,
       "tsmOperPortAdaptSwMode": tsmOperPortAdaptSwMode,
       "tsmOperPortAdaptErrRate": tsmOperPortAdaptErrRate,
       "tsmOperPortAdaptTrend": tsmOperPortAdaptTrend,
       "tsmOperPortOpenState": tsmOperPortOpenState,
       "tsmOperPortUpStream": tsmOperPortUpStream,
       "tsmOperSwModeTable": tsmOperSwModeTable,
       "tsmOperSwModeEntry": tsmOperSwModeEntry,
       "tsmOperSwModeSlotNumber": tsmOperSwModeSlotNumber,
       "tsmOperSwModeHiErrThresh": tsmOperSwModeHiErrThresh,
       "tsmOperSwModeLoErrThresh": tsmOperSwModeLoErrThresh,
       "tsmOperSwModeTrendThresh": tsmOperSwModeTrendThresh,
       "tsmOperSwModeSamplePeriod": tsmOperSwModeSamplePeriod}
)
