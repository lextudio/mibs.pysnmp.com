# SNMP MIB module (AVICI-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVICI-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:46 2024
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

(aviciMibs,) = mibBuilder.importSymbols(
    "AVICI-SMI",
    "aviciMibs")

(aviciSysTrapDescr,) = mibBuilder.importSymbols(
    "AVICI-SYSTEM-MIB",
    "aviciSysTrapDescr")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

aviciSonetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3)
)
aviciSonetMIB.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviciSonetObjects_ObjectIdentity = ObjectIdentity
aviciSonetObjects = _AviciSonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1)
)
_AviciSonetMediumTable_Object = MibTable
aviciSonetMediumTable = _AviciSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    aviciSonetMediumTable.setStatus("current")
_AviciSonetMediumEntry_Object = MibTableRow
aviciSonetMediumEntry = _AviciSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 1, 1)
)
aviciSonetMediumEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aviciSonetMediumEntry.setStatus("current")


class _AviciSonetMediumFramingType_Type(Integer32):
    """Custom type aviciSonetMediumFramingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_AviciSonetMediumFramingType_Type.__name__ = "Integer32"
_AviciSonetMediumFramingType_Object = MibTableColumn
aviciSonetMediumFramingType = _AviciSonetMediumFramingType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 1, 1, 1),
    _AviciSonetMediumFramingType_Type()
)
aviciSonetMediumFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviciSonetMediumFramingType.setStatus("current")


class _AviciSonetMediumLoopbackMode_Type(Integer32):
    """Custom type aviciSonetMediumLoopbackMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 3),
          ("line", 2),
          ("none", 1))
    )


_AviciSonetMediumLoopbackMode_Type.__name__ = "Integer32"
_AviciSonetMediumLoopbackMode_Object = MibTableColumn
aviciSonetMediumLoopbackMode = _AviciSonetMediumLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 1, 1, 2),
    _AviciSonetMediumLoopbackMode_Type()
)
aviciSonetMediumLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviciSonetMediumLoopbackMode.setStatus("current")


class _AviciSonetMediumClockSource_Type(Integer32):
    """Custom type aviciSonetMediumClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 2),
          ("line", 1))
    )


_AviciSonetMediumClockSource_Type.__name__ = "Integer32"
_AviciSonetMediumClockSource_Object = MibTableColumn
aviciSonetMediumClockSource = _AviciSonetMediumClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 1, 1, 3),
    _AviciSonetMediumClockSource_Type()
)
aviciSonetMediumClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviciSonetMediumClockSource.setStatus("current")
_AviciSonetSectionTable_Object = MibTable
aviciSonetSectionTable = _AviciSonetSectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    aviciSonetSectionTable.setStatus("current")
_AviciSonetSectionEntry_Object = MibTableRow
aviciSonetSectionEntry = _AviciSonetSectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1)
)
aviciSonetSectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aviciSonetSectionEntry.setStatus("current")


class _AviciSonetTxSectionJ0_Type(DisplayString):
    """Custom type aviciSonetTxSectionJ0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AviciSonetTxSectionJ0_Type.__name__ = "DisplayString"
_AviciSonetTxSectionJ0_Object = MibTableColumn
aviciSonetTxSectionJ0 = _AviciSonetTxSectionJ0_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 1),
    _AviciSonetTxSectionJ0_Type()
)
aviciSonetTxSectionJ0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetTxSectionJ0.setStatus("current")


class _AviciSonetSectionThresholdES_Type(Unsigned32):
    """Custom type aviciSonetSectionThresholdES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetSectionThresholdES_Type.__name__ = "Unsigned32"
_AviciSonetSectionThresholdES_Object = MibTableColumn
aviciSonetSectionThresholdES = _AviciSonetSectionThresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 2),
    _AviciSonetSectionThresholdES_Type()
)
aviciSonetSectionThresholdES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetSectionThresholdES.setStatus("current")


class _AviciSonetSectionThresholdSES_Type(Unsigned32):
    """Custom type aviciSonetSectionThresholdSES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetSectionThresholdSES_Type.__name__ = "Unsigned32"
_AviciSonetSectionThresholdSES_Object = MibTableColumn
aviciSonetSectionThresholdSES = _AviciSonetSectionThresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 3),
    _AviciSonetSectionThresholdSES_Type()
)
aviciSonetSectionThresholdSES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetSectionThresholdSES.setStatus("current")


class _AviciSonetSectionThresholdSEFS_Type(Unsigned32):
    """Custom type aviciSonetSectionThresholdSEFS based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetSectionThresholdSEFS_Type.__name__ = "Unsigned32"
_AviciSonetSectionThresholdSEFS_Object = MibTableColumn
aviciSonetSectionThresholdSEFS = _AviciSonetSectionThresholdSEFS_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 4),
    _AviciSonetSectionThresholdSEFS_Type()
)
aviciSonetSectionThresholdSEFS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetSectionThresholdSEFS.setStatus("current")


class _AviciSonetSectionThresholdCV_Type(Unsigned32):
    """Custom type aviciSonetSectionThresholdCV based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AviciSonetSectionThresholdCV_Type.__name__ = "Unsigned32"
_AviciSonetSectionThresholdCV_Object = MibTableColumn
aviciSonetSectionThresholdCV = _AviciSonetSectionThresholdCV_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 5),
    _AviciSonetSectionThresholdCV_Type()
)
aviciSonetSectionThresholdCV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetSectionThresholdCV.setStatus("current")


class _AviciSonetSectionEventEnable_Type(Integer32):
    """Custom type aviciSonetSectionEventEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AviciSonetSectionEventEnable_Type.__name__ = "Integer32"
_AviciSonetSectionEventEnable_Object = MibTableColumn
aviciSonetSectionEventEnable = _AviciSonetSectionEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 6),
    _AviciSonetSectionEventEnable_Type()
)
aviciSonetSectionEventEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetSectionEventEnable.setStatus("current")


class _AviciSonetSectionEventStatus_Type(Integer32):
    """Custom type aviciSonetSectionEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AviciSonetSectionEventStatus_Type.__name__ = "Integer32"
_AviciSonetSectionEventStatus_Object = MibTableColumn
aviciSonetSectionEventStatus = _AviciSonetSectionEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 7),
    _AviciSonetSectionEventStatus_Type()
)
aviciSonetSectionEventStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aviciSonetSectionEventStatus.setStatus("current")


class _AviciSonetSectionEventIndex_Type(Integer32):
    """Custom type aviciSonetSectionEventIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AviciSonetSectionEventIndex_Type.__name__ = "Integer32"
_AviciSonetSectionEventIndex_Object = MibTableColumn
aviciSonetSectionEventIndex = _AviciSonetSectionEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 8),
    _AviciSonetSectionEventIndex_Type()
)
aviciSonetSectionEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetSectionEventIndex.setStatus("current")


class _AviciSonetSectionCurrentFailures_Type(Integer32):
    """Custom type aviciSonetSectionCurrentFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AviciSonetSectionCurrentFailures_Type.__name__ = "Integer32"
_AviciSonetSectionCurrentFailures_Object = MibTableColumn
aviciSonetSectionCurrentFailures = _AviciSonetSectionCurrentFailures_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 9),
    _AviciSonetSectionCurrentFailures_Type()
)
aviciSonetSectionCurrentFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSonetSectionCurrentFailures.setStatus("current")


class _AviciSonetRxSectionJ0_Type(DisplayString):
    """Custom type aviciSonetRxSectionJ0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AviciSonetRxSectionJ0_Type.__name__ = "DisplayString"
_AviciSonetRxSectionJ0_Object = MibTableColumn
aviciSonetRxSectionJ0 = _AviciSonetRxSectionJ0_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 2, 1, 10),
    _AviciSonetRxSectionJ0_Type()
)
aviciSonetRxSectionJ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSonetRxSectionJ0.setStatus("current")
_AviciSonetLineTable_Object = MibTable
aviciSonetLineTable = _AviciSonetLineTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    aviciSonetLineTable.setStatus("current")
_AviciSonetLineEntry_Object = MibTableRow
aviciSonetLineEntry = _AviciSonetLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1)
)
aviciSonetLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aviciSonetLineEntry.setStatus("current")


class _AviciSonetLineS1_Type(Integer32):
    """Custom type aviciSonetLineS1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AviciSonetLineS1_Type.__name__ = "Integer32"
_AviciSonetLineS1_Object = MibTableColumn
aviciSonetLineS1 = _AviciSonetLineS1_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 1),
    _AviciSonetLineS1_Type()
)
aviciSonetLineS1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetLineS1.setStatus("current")


class _AviciSonetLineAPS_Type(Integer32):
    """Custom type aviciSonetLineAPS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AviciSonetLineAPS_Type.__name__ = "Integer32"
_AviciSonetLineAPS_Object = MibTableColumn
aviciSonetLineAPS = _AviciSonetLineAPS_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 2),
    _AviciSonetLineAPS_Type()
)
aviciSonetLineAPS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetLineAPS.setStatus("current")


class _AviciSonetLineThresholdES_Type(Unsigned32):
    """Custom type aviciSonetLineThresholdES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetLineThresholdES_Type.__name__ = "Unsigned32"
_AviciSonetLineThresholdES_Object = MibTableColumn
aviciSonetLineThresholdES = _AviciSonetLineThresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 3),
    _AviciSonetLineThresholdES_Type()
)
aviciSonetLineThresholdES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetLineThresholdES.setStatus("current")


class _AviciSonetLineThresholdSES_Type(Unsigned32):
    """Custom type aviciSonetLineThresholdSES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetLineThresholdSES_Type.__name__ = "Unsigned32"
_AviciSonetLineThresholdSES_Object = MibTableColumn
aviciSonetLineThresholdSES = _AviciSonetLineThresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 4),
    _AviciSonetLineThresholdSES_Type()
)
aviciSonetLineThresholdSES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetLineThresholdSES.setStatus("current")


class _AviciSonetLineThresholdCV_Type(Unsigned32):
    """Custom type aviciSonetLineThresholdCV based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AviciSonetLineThresholdCV_Type.__name__ = "Unsigned32"
_AviciSonetLineThresholdCV_Object = MibTableColumn
aviciSonetLineThresholdCV = _AviciSonetLineThresholdCV_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 5),
    _AviciSonetLineThresholdCV_Type()
)
aviciSonetLineThresholdCV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetLineThresholdCV.setStatus("current")


class _AviciSonetLineThresholdUAS_Type(Unsigned32):
    """Custom type aviciSonetLineThresholdUAS based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetLineThresholdUAS_Type.__name__ = "Unsigned32"
_AviciSonetLineThresholdUAS_Object = MibTableColumn
aviciSonetLineThresholdUAS = _AviciSonetLineThresholdUAS_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 6),
    _AviciSonetLineThresholdUAS_Type()
)
aviciSonetLineThresholdUAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetLineThresholdUAS.setStatus("current")


class _AviciSonetLineEventEnable_Type(Integer32):
    """Custom type aviciSonetLineEventEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AviciSonetLineEventEnable_Type.__name__ = "Integer32"
_AviciSonetLineEventEnable_Object = MibTableColumn
aviciSonetLineEventEnable = _AviciSonetLineEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 7),
    _AviciSonetLineEventEnable_Type()
)
aviciSonetLineEventEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetLineEventEnable.setStatus("current")


class _AviciSonetLineEventStatus_Type(Integer32):
    """Custom type aviciSonetLineEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AviciSonetLineEventStatus_Type.__name__ = "Integer32"
_AviciSonetLineEventStatus_Object = MibTableColumn
aviciSonetLineEventStatus = _AviciSonetLineEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 8),
    _AviciSonetLineEventStatus_Type()
)
aviciSonetLineEventStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aviciSonetLineEventStatus.setStatus("current")


class _AviciSonetLineEventIndex_Type(Integer32):
    """Custom type aviciSonetLineEventIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AviciSonetLineEventIndex_Type.__name__ = "Integer32"
_AviciSonetLineEventIndex_Object = MibTableColumn
aviciSonetLineEventIndex = _AviciSonetLineEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 9),
    _AviciSonetLineEventIndex_Type()
)
aviciSonetLineEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetLineEventIndex.setStatus("current")


class _AviciSonetLineCurrentFailures_Type(Integer32):
    """Custom type aviciSonetLineCurrentFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AviciSonetLineCurrentFailures_Type.__name__ = "Integer32"
_AviciSonetLineCurrentFailures_Object = MibTableColumn
aviciSonetLineCurrentFailures = _AviciSonetLineCurrentFailures_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 3, 1, 10),
    _AviciSonetLineCurrentFailures_Type()
)
aviciSonetLineCurrentFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSonetLineCurrentFailures.setStatus("current")
_AviciSonetFarEndLineTable_Object = MibTable
aviciSonetFarEndLineTable = _AviciSonetFarEndLineTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    aviciSonetFarEndLineTable.setStatus("current")
_AviciSonetFarEndLineEntry_Object = MibTableRow
aviciSonetFarEndLineEntry = _AviciSonetFarEndLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 4, 1)
)
aviciSonetFarEndLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aviciSonetFarEndLineEntry.setStatus("current")


class _AviciSonetFarEndLineThresholdES_Type(Unsigned32):
    """Custom type aviciSonetFarEndLineThresholdES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetFarEndLineThresholdES_Type.__name__ = "Unsigned32"
_AviciSonetFarEndLineThresholdES_Object = MibTableColumn
aviciSonetFarEndLineThresholdES = _AviciSonetFarEndLineThresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 4, 1, 1),
    _AviciSonetFarEndLineThresholdES_Type()
)
aviciSonetFarEndLineThresholdES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndLineThresholdES.setStatus("current")


class _AviciSonetFarEndLineThresholdSES_Type(Unsigned32):
    """Custom type aviciSonetFarEndLineThresholdSES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetFarEndLineThresholdSES_Type.__name__ = "Unsigned32"
_AviciSonetFarEndLineThresholdSES_Object = MibTableColumn
aviciSonetFarEndLineThresholdSES = _AviciSonetFarEndLineThresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 4, 1, 2),
    _AviciSonetFarEndLineThresholdSES_Type()
)
aviciSonetFarEndLineThresholdSES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndLineThresholdSES.setStatus("current")


class _AviciSonetFarEndLineThresholdCV_Type(Unsigned32):
    """Custom type aviciSonetFarEndLineThresholdCV based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AviciSonetFarEndLineThresholdCV_Type.__name__ = "Unsigned32"
_AviciSonetFarEndLineThresholdCV_Object = MibTableColumn
aviciSonetFarEndLineThresholdCV = _AviciSonetFarEndLineThresholdCV_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 4, 1, 3),
    _AviciSonetFarEndLineThresholdCV_Type()
)
aviciSonetFarEndLineThresholdCV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndLineThresholdCV.setStatus("current")


class _AviciSonetFarEndLineThresholdUAS_Type(Unsigned32):
    """Custom type aviciSonetFarEndLineThresholdUAS based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetFarEndLineThresholdUAS_Type.__name__ = "Unsigned32"
_AviciSonetFarEndLineThresholdUAS_Object = MibTableColumn
aviciSonetFarEndLineThresholdUAS = _AviciSonetFarEndLineThresholdUAS_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 4, 1, 4),
    _AviciSonetFarEndLineThresholdUAS_Type()
)
aviciSonetFarEndLineThresholdUAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndLineThresholdUAS.setStatus("current")


class _AviciSonetFarEndLineEventEnable_Type(Integer32):
    """Custom type aviciSonetFarEndLineEventEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AviciSonetFarEndLineEventEnable_Type.__name__ = "Integer32"
_AviciSonetFarEndLineEventEnable_Object = MibTableColumn
aviciSonetFarEndLineEventEnable = _AviciSonetFarEndLineEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 4, 1, 5),
    _AviciSonetFarEndLineEventEnable_Type()
)
aviciSonetFarEndLineEventEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndLineEventEnable.setStatus("current")


class _AviciSonetFarEndLineEventStatus_Type(Integer32):
    """Custom type aviciSonetFarEndLineEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AviciSonetFarEndLineEventStatus_Type.__name__ = "Integer32"
_AviciSonetFarEndLineEventStatus_Object = MibTableColumn
aviciSonetFarEndLineEventStatus = _AviciSonetFarEndLineEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 4, 1, 6),
    _AviciSonetFarEndLineEventStatus_Type()
)
aviciSonetFarEndLineEventStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aviciSonetFarEndLineEventStatus.setStatus("current")


class _AviciSonetFarEndLineEventIndex_Type(Integer32):
    """Custom type aviciSonetFarEndLineEventIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AviciSonetFarEndLineEventIndex_Type.__name__ = "Integer32"
_AviciSonetFarEndLineEventIndex_Object = MibTableColumn
aviciSonetFarEndLineEventIndex = _AviciSonetFarEndLineEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 4, 1, 7),
    _AviciSonetFarEndLineEventIndex_Type()
)
aviciSonetFarEndLineEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndLineEventIndex.setStatus("current")
_AviciSonetPathTable_Object = MibTable
aviciSonetPathTable = _AviciSonetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    aviciSonetPathTable.setStatus("current")
_AviciSonetPathEntry_Object = MibTableRow
aviciSonetPathEntry = _AviciSonetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1)
)
aviciSonetPathEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aviciSonetPathEntry.setStatus("current")


class _AviciSonetPathC2_Type(Integer32):
    """Custom type aviciSonetPathC2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AviciSonetPathC2_Type.__name__ = "Integer32"
_AviciSonetPathC2_Object = MibTableColumn
aviciSonetPathC2 = _AviciSonetPathC2_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 1),
    _AviciSonetPathC2_Type()
)
aviciSonetPathC2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetPathC2.setStatus("current")


class _AviciSonetPathTxTrace_Type(DisplayString):
    """Custom type aviciSonetPathTxTrace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_AviciSonetPathTxTrace_Type.__name__ = "DisplayString"
_AviciSonetPathTxTrace_Object = MibTableColumn
aviciSonetPathTxTrace = _AviciSonetPathTxTrace_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 2),
    _AviciSonetPathTxTrace_Type()
)
aviciSonetPathTxTrace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetPathTxTrace.setStatus("current")


class _AviciSonetPathRxTrace_Type(DisplayString):
    """Custom type aviciSonetPathRxTrace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_AviciSonetPathRxTrace_Type.__name__ = "DisplayString"
_AviciSonetPathRxTrace_Object = MibTableColumn
aviciSonetPathRxTrace = _AviciSonetPathRxTrace_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 3),
    _AviciSonetPathRxTrace_Type()
)
aviciSonetPathRxTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSonetPathRxTrace.setStatus("current")


class _AviciSonetPathThresholdES_Type(Unsigned32):
    """Custom type aviciSonetPathThresholdES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetPathThresholdES_Type.__name__ = "Unsigned32"
_AviciSonetPathThresholdES_Object = MibTableColumn
aviciSonetPathThresholdES = _AviciSonetPathThresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 4),
    _AviciSonetPathThresholdES_Type()
)
aviciSonetPathThresholdES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetPathThresholdES.setStatus("current")


class _AviciSonetPathThresholdSES_Type(Unsigned32):
    """Custom type aviciSonetPathThresholdSES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetPathThresholdSES_Type.__name__ = "Unsigned32"
_AviciSonetPathThresholdSES_Object = MibTableColumn
aviciSonetPathThresholdSES = _AviciSonetPathThresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 5),
    _AviciSonetPathThresholdSES_Type()
)
aviciSonetPathThresholdSES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetPathThresholdSES.setStatus("current")


class _AviciSonetPathThresholdCV_Type(Unsigned32):
    """Custom type aviciSonetPathThresholdCV based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AviciSonetPathThresholdCV_Type.__name__ = "Unsigned32"
_AviciSonetPathThresholdCV_Object = MibTableColumn
aviciSonetPathThresholdCV = _AviciSonetPathThresholdCV_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 6),
    _AviciSonetPathThresholdCV_Type()
)
aviciSonetPathThresholdCV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetPathThresholdCV.setStatus("current")


class _AviciSonetPathThresholdUAS_Type(Unsigned32):
    """Custom type aviciSonetPathThresholdUAS based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetPathThresholdUAS_Type.__name__ = "Unsigned32"
_AviciSonetPathThresholdUAS_Object = MibTableColumn
aviciSonetPathThresholdUAS = _AviciSonetPathThresholdUAS_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 7),
    _AviciSonetPathThresholdUAS_Type()
)
aviciSonetPathThresholdUAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetPathThresholdUAS.setStatus("current")


class _AviciSonetPathEventEnable_Type(Integer32):
    """Custom type aviciSonetPathEventEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AviciSonetPathEventEnable_Type.__name__ = "Integer32"
_AviciSonetPathEventEnable_Object = MibTableColumn
aviciSonetPathEventEnable = _AviciSonetPathEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 8),
    _AviciSonetPathEventEnable_Type()
)
aviciSonetPathEventEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetPathEventEnable.setStatus("current")


class _AviciSonetPathEventStatus_Type(Integer32):
    """Custom type aviciSonetPathEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AviciSonetPathEventStatus_Type.__name__ = "Integer32"
_AviciSonetPathEventStatus_Object = MibTableColumn
aviciSonetPathEventStatus = _AviciSonetPathEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 9),
    _AviciSonetPathEventStatus_Type()
)
aviciSonetPathEventStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aviciSonetPathEventStatus.setStatus("current")


class _AviciSonetPathEventIndex_Type(Integer32):
    """Custom type aviciSonetPathEventIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AviciSonetPathEventIndex_Type.__name__ = "Integer32"
_AviciSonetPathEventIndex_Object = MibTableColumn
aviciSonetPathEventIndex = _AviciSonetPathEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 10),
    _AviciSonetPathEventIndex_Type()
)
aviciSonetPathEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetPathEventIndex.setStatus("current")


class _AviciSonetPathCurrentFailures_Type(Integer32):
    """Custom type aviciSonetPathCurrentFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AviciSonetPathCurrentFailures_Type.__name__ = "Integer32"
_AviciSonetPathCurrentFailures_Object = MibTableColumn
aviciSonetPathCurrentFailures = _AviciSonetPathCurrentFailures_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 5, 1, 11),
    _AviciSonetPathCurrentFailures_Type()
)
aviciSonetPathCurrentFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSonetPathCurrentFailures.setStatus("current")
_AviciSonetFarEndPathTable_Object = MibTable
aviciSonetFarEndPathTable = _AviciSonetFarEndPathTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    aviciSonetFarEndPathTable.setStatus("current")
_AviciSonetFarEndPathEntry_Object = MibTableRow
aviciSonetFarEndPathEntry = _AviciSonetFarEndPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 6, 1)
)
aviciSonetFarEndPathEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aviciSonetFarEndPathEntry.setStatus("current")


class _AviciSonetFarEndPathThresholdES_Type(Unsigned32):
    """Custom type aviciSonetFarEndPathThresholdES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetFarEndPathThresholdES_Type.__name__ = "Unsigned32"
_AviciSonetFarEndPathThresholdES_Object = MibTableColumn
aviciSonetFarEndPathThresholdES = _AviciSonetFarEndPathThresholdES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 6, 1, 1),
    _AviciSonetFarEndPathThresholdES_Type()
)
aviciSonetFarEndPathThresholdES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndPathThresholdES.setStatus("current")


class _AviciSonetFarEndPathThresholdSES_Type(Unsigned32):
    """Custom type aviciSonetFarEndPathThresholdSES based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetFarEndPathThresholdSES_Type.__name__ = "Unsigned32"
_AviciSonetFarEndPathThresholdSES_Object = MibTableColumn
aviciSonetFarEndPathThresholdSES = _AviciSonetFarEndPathThresholdSES_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 6, 1, 2),
    _AviciSonetFarEndPathThresholdSES_Type()
)
aviciSonetFarEndPathThresholdSES.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndPathThresholdSES.setStatus("current")


class _AviciSonetFarEndPathThresholdCV_Type(Unsigned32):
    """Custom type aviciSonetFarEndPathThresholdCV based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AviciSonetFarEndPathThresholdCV_Type.__name__ = "Unsigned32"
_AviciSonetFarEndPathThresholdCV_Object = MibTableColumn
aviciSonetFarEndPathThresholdCV = _AviciSonetFarEndPathThresholdCV_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 6, 1, 3),
    _AviciSonetFarEndPathThresholdCV_Type()
)
aviciSonetFarEndPathThresholdCV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndPathThresholdCV.setStatus("current")


class _AviciSonetFarEndPathThresholdUAS_Type(Unsigned32):
    """Custom type aviciSonetFarEndPathThresholdUAS based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AviciSonetFarEndPathThresholdUAS_Type.__name__ = "Unsigned32"
_AviciSonetFarEndPathThresholdUAS_Object = MibTableColumn
aviciSonetFarEndPathThresholdUAS = _AviciSonetFarEndPathThresholdUAS_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 6, 1, 4),
    _AviciSonetFarEndPathThresholdUAS_Type()
)
aviciSonetFarEndPathThresholdUAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndPathThresholdUAS.setStatus("current")


class _AviciSonetFarEndPathEventEnable_Type(Integer32):
    """Custom type aviciSonetFarEndPathEventEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AviciSonetFarEndPathEventEnable_Type.__name__ = "Integer32"
_AviciSonetFarEndPathEventEnable_Object = MibTableColumn
aviciSonetFarEndPathEventEnable = _AviciSonetFarEndPathEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 6, 1, 5),
    _AviciSonetFarEndPathEventEnable_Type()
)
aviciSonetFarEndPathEventEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndPathEventEnable.setStatus("current")


class _AviciSonetFarEndPathEventStatus_Type(Integer32):
    """Custom type aviciSonetFarEndPathEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AviciSonetFarEndPathEventStatus_Type.__name__ = "Integer32"
_AviciSonetFarEndPathEventStatus_Object = MibTableColumn
aviciSonetFarEndPathEventStatus = _AviciSonetFarEndPathEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 6, 1, 6),
    _AviciSonetFarEndPathEventStatus_Type()
)
aviciSonetFarEndPathEventStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aviciSonetFarEndPathEventStatus.setStatus("current")


class _AviciSonetFarEndPathEventIndex_Type(Integer32):
    """Custom type aviciSonetFarEndPathEventIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AviciSonetFarEndPathEventIndex_Type.__name__ = "Integer32"
_AviciSonetFarEndPathEventIndex_Object = MibTableColumn
aviciSonetFarEndPathEventIndex = _AviciSonetFarEndPathEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 1, 6, 1, 7),
    _AviciSonetFarEndPathEventIndex_Type()
)
aviciSonetFarEndPathEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aviciSonetFarEndPathEventIndex.setStatus("current")
_AviciSonetNotifications_ObjectIdentity = ObjectIdentity
aviciSonetNotifications = _AviciSonetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 2)
)
_AviciSonetNotificationPrefix_ObjectIdentity = ObjectIdentity
aviciSonetNotificationPrefix = _AviciSonetNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 2, 0)
)
_AviciSonetMIBConformance_ObjectIdentity = ObjectIdentity
aviciSonetMIBConformance = _AviciSonetMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 3)
)
_AviciSonetMIBCompliances_ObjectIdentity = ObjectIdentity
aviciSonetMIBCompliances = _AviciSonetMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 3, 1)
)
_AviciSonetMIBGroups_ObjectIdentity = ObjectIdentity
aviciSonetMIBGroups = _AviciSonetMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 3, 2)
)

# Managed Objects groups

aviciSonetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 3, 2, 1)
)
aviciSonetGroup.setObjects(
      *(("AVICI-SONET-MIB", "aviciSonetMediumFramingType"),
        ("AVICI-SONET-MIB", "aviciSonetMediumLoopbackMode"),
        ("AVICI-SONET-MIB", "aviciSonetMediumClockSource"),
        ("AVICI-SONET-MIB", "aviciSonetTxSectionJ0"),
        ("AVICI-SONET-MIB", "aviciSonetRxSectionJ0"),
        ("AVICI-SONET-MIB", "aviciSonetSectionThresholdES"),
        ("AVICI-SONET-MIB", "aviciSonetSectionThresholdSES"),
        ("AVICI-SONET-MIB", "aviciSonetSectionThresholdSEFS"),
        ("AVICI-SONET-MIB", "aviciSonetSectionThresholdCV"),
        ("AVICI-SONET-MIB", "aviciSonetSectionEventEnable"),
        ("AVICI-SONET-MIB", "aviciSonetSectionEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetSectionEventIndex"),
        ("AVICI-SONET-MIB", "aviciSonetLineS1"),
        ("AVICI-SONET-MIB", "aviciSonetLineAPS"),
        ("AVICI-SONET-MIB", "aviciSonetLineThresholdES"),
        ("AVICI-SONET-MIB", "aviciSonetLineThresholdSES"),
        ("AVICI-SONET-MIB", "aviciSonetLineThresholdCV"),
        ("AVICI-SONET-MIB", "aviciSonetLineThresholdUAS"),
        ("AVICI-SONET-MIB", "aviciSonetLineEventEnable"),
        ("AVICI-SONET-MIB", "aviciSonetLineEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetLineEventIndex"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineThresholdES"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineThresholdSES"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineThresholdCV"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineThresholdUAS"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineEventEnable"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineEventIndex"))
)
if mibBuilder.loadTexts:
    aviciSonetGroup.setStatus("current")

aviciSonetPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 3, 2, 2)
)
aviciSonetPathGroup.setObjects(
      *(("AVICI-SONET-MIB", "aviciSonetPathC2"),
        ("AVICI-SONET-MIB", "aviciSonetPathTxTrace"),
        ("AVICI-SONET-MIB", "aviciSonetPathRxTrace"),
        ("AVICI-SONET-MIB", "aviciSonetPathThresholdES"),
        ("AVICI-SONET-MIB", "aviciSonetPathThresholdSES"),
        ("AVICI-SONET-MIB", "aviciSonetPathThresholdCV"),
        ("AVICI-SONET-MIB", "aviciSonetPathThresholdUAS"),
        ("AVICI-SONET-MIB", "aviciSonetPathEventEnable"),
        ("AVICI-SONET-MIB", "aviciSonetPathEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetPathEventIndex"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathThresholdES"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathThresholdSES"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathThresholdCV"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathThresholdUAS"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathEventEnable"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathEventIndex"))
)
if mibBuilder.loadTexts:
    aviciSonetPathGroup.setStatus("current")


# Notification objects

aviciSonetSectionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 2, 0, 1)
)
aviciSonetSectionEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("AVICI-SONET-MIB", "aviciSonetSectionEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetSectionEventIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciSonetSectionEvent.setStatus(
        "current"
    )

aviciSonetLineEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 2, 0, 2)
)
aviciSonetLineEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("AVICI-SONET-MIB", "aviciSonetLineEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetLineEventIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciSonetLineEvent.setStatus(
        "current"
    )

aviciSonetFarEndLineEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 2, 0, 3)
)
aviciSonetFarEndLineEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineEventIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciSonetFarEndLineEvent.setStatus(
        "current"
    )

aviciSonetPathEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 2, 0, 4)
)
aviciSonetPathEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("AVICI-SONET-MIB", "aviciSonetPathEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetPathEventIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciSonetPathEvent.setStatus(
        "current"
    )

aviciSonetFarEndPathEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 2, 0, 5)
)
aviciSonetFarEndPathEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathEventStatus"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathEventIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciSonetFarEndPathEvent.setStatus(
        "current"
    )


# Notifications groups

aviciSonetNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 3, 2, 3)
)
aviciSonetNotificationGroup.setObjects(
      *(("AVICI-SONET-MIB", "aviciSonetSectionEvent"),
        ("AVICI-SONET-MIB", "aviciSonetLineEvent"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndLineEvent"))
)
if mibBuilder.loadTexts:
    aviciSonetNotificationGroup.setStatus(
        "current"
    )

aviciSonetPathNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 3, 2, 4)
)
aviciSonetPathNotificationGroup.setObjects(
      *(("AVICI-SONET-MIB", "aviciSonetPathEvent"),
        ("AVICI-SONET-MIB", "aviciSonetFarEndPathEvent"))
)
if mibBuilder.loadTexts:
    aviciSonetPathNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aviciSonetMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2474, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    aviciSonetMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVICI-SONET-MIB",
    **{"aviciSonetMIB": aviciSonetMIB,
       "aviciSonetObjects": aviciSonetObjects,
       "aviciSonetMediumTable": aviciSonetMediumTable,
       "aviciSonetMediumEntry": aviciSonetMediumEntry,
       "aviciSonetMediumFramingType": aviciSonetMediumFramingType,
       "aviciSonetMediumLoopbackMode": aviciSonetMediumLoopbackMode,
       "aviciSonetMediumClockSource": aviciSonetMediumClockSource,
       "aviciSonetSectionTable": aviciSonetSectionTable,
       "aviciSonetSectionEntry": aviciSonetSectionEntry,
       "aviciSonetTxSectionJ0": aviciSonetTxSectionJ0,
       "aviciSonetSectionThresholdES": aviciSonetSectionThresholdES,
       "aviciSonetSectionThresholdSES": aviciSonetSectionThresholdSES,
       "aviciSonetSectionThresholdSEFS": aviciSonetSectionThresholdSEFS,
       "aviciSonetSectionThresholdCV": aviciSonetSectionThresholdCV,
       "aviciSonetSectionEventEnable": aviciSonetSectionEventEnable,
       "aviciSonetSectionEventStatus": aviciSonetSectionEventStatus,
       "aviciSonetSectionEventIndex": aviciSonetSectionEventIndex,
       "aviciSonetSectionCurrentFailures": aviciSonetSectionCurrentFailures,
       "aviciSonetRxSectionJ0": aviciSonetRxSectionJ0,
       "aviciSonetLineTable": aviciSonetLineTable,
       "aviciSonetLineEntry": aviciSonetLineEntry,
       "aviciSonetLineS1": aviciSonetLineS1,
       "aviciSonetLineAPS": aviciSonetLineAPS,
       "aviciSonetLineThresholdES": aviciSonetLineThresholdES,
       "aviciSonetLineThresholdSES": aviciSonetLineThresholdSES,
       "aviciSonetLineThresholdCV": aviciSonetLineThresholdCV,
       "aviciSonetLineThresholdUAS": aviciSonetLineThresholdUAS,
       "aviciSonetLineEventEnable": aviciSonetLineEventEnable,
       "aviciSonetLineEventStatus": aviciSonetLineEventStatus,
       "aviciSonetLineEventIndex": aviciSonetLineEventIndex,
       "aviciSonetLineCurrentFailures": aviciSonetLineCurrentFailures,
       "aviciSonetFarEndLineTable": aviciSonetFarEndLineTable,
       "aviciSonetFarEndLineEntry": aviciSonetFarEndLineEntry,
       "aviciSonetFarEndLineThresholdES": aviciSonetFarEndLineThresholdES,
       "aviciSonetFarEndLineThresholdSES": aviciSonetFarEndLineThresholdSES,
       "aviciSonetFarEndLineThresholdCV": aviciSonetFarEndLineThresholdCV,
       "aviciSonetFarEndLineThresholdUAS": aviciSonetFarEndLineThresholdUAS,
       "aviciSonetFarEndLineEventEnable": aviciSonetFarEndLineEventEnable,
       "aviciSonetFarEndLineEventStatus": aviciSonetFarEndLineEventStatus,
       "aviciSonetFarEndLineEventIndex": aviciSonetFarEndLineEventIndex,
       "aviciSonetPathTable": aviciSonetPathTable,
       "aviciSonetPathEntry": aviciSonetPathEntry,
       "aviciSonetPathC2": aviciSonetPathC2,
       "aviciSonetPathTxTrace": aviciSonetPathTxTrace,
       "aviciSonetPathRxTrace": aviciSonetPathRxTrace,
       "aviciSonetPathThresholdES": aviciSonetPathThresholdES,
       "aviciSonetPathThresholdSES": aviciSonetPathThresholdSES,
       "aviciSonetPathThresholdCV": aviciSonetPathThresholdCV,
       "aviciSonetPathThresholdUAS": aviciSonetPathThresholdUAS,
       "aviciSonetPathEventEnable": aviciSonetPathEventEnable,
       "aviciSonetPathEventStatus": aviciSonetPathEventStatus,
       "aviciSonetPathEventIndex": aviciSonetPathEventIndex,
       "aviciSonetPathCurrentFailures": aviciSonetPathCurrentFailures,
       "aviciSonetFarEndPathTable": aviciSonetFarEndPathTable,
       "aviciSonetFarEndPathEntry": aviciSonetFarEndPathEntry,
       "aviciSonetFarEndPathThresholdES": aviciSonetFarEndPathThresholdES,
       "aviciSonetFarEndPathThresholdSES": aviciSonetFarEndPathThresholdSES,
       "aviciSonetFarEndPathThresholdCV": aviciSonetFarEndPathThresholdCV,
       "aviciSonetFarEndPathThresholdUAS": aviciSonetFarEndPathThresholdUAS,
       "aviciSonetFarEndPathEventEnable": aviciSonetFarEndPathEventEnable,
       "aviciSonetFarEndPathEventStatus": aviciSonetFarEndPathEventStatus,
       "aviciSonetFarEndPathEventIndex": aviciSonetFarEndPathEventIndex,
       "aviciSonetNotifications": aviciSonetNotifications,
       "aviciSonetNotificationPrefix": aviciSonetNotificationPrefix,
       "aviciSonetSectionEvent": aviciSonetSectionEvent,
       "aviciSonetLineEvent": aviciSonetLineEvent,
       "aviciSonetFarEndLineEvent": aviciSonetFarEndLineEvent,
       "aviciSonetPathEvent": aviciSonetPathEvent,
       "aviciSonetFarEndPathEvent": aviciSonetFarEndPathEvent,
       "aviciSonetMIBConformance": aviciSonetMIBConformance,
       "aviciSonetMIBCompliances": aviciSonetMIBCompliances,
       "aviciSonetMIBCompliance": aviciSonetMIBCompliance,
       "aviciSonetMIBGroups": aviciSonetMIBGroups,
       "aviciSonetGroup": aviciSonetGroup,
       "aviciSonetPathGroup": aviciSonetPathGroup,
       "aviciSonetNotificationGroup": aviciSonetNotificationGroup,
       "aviciSonetPathNotificationGroup": aviciSonetPathNotificationGroup}
)
