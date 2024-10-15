# SNMP MIB module (Nortel-Magellan-Passport-GsmIwfMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-GsmIwfMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:53 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 FixedPoint2,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint2",
    "Link",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GsmCs_ObjectIdentity = ObjectIdentity
gsmCs = _GsmCs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127)
)
_GsmCsRowStatusTable_Object = MibTable
gsmCsRowStatusTable = _GsmCsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 1)
)
if mibBuilder.loadTexts:
    gsmCsRowStatusTable.setStatus("mandatory")
_GsmCsRowStatusEntry_Object = MibTableRow
gsmCsRowStatusEntry = _GsmCsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 1, 1)
)
gsmCsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    gsmCsRowStatusEntry.setStatus("mandatory")
_GsmCsRowStatus_Type = RowStatus
_GsmCsRowStatus_Object = MibTableColumn
gsmCsRowStatus = _GsmCsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 1, 1, 1),
    _GsmCsRowStatus_Type()
)
gsmCsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsRowStatus.setStatus("mandatory")
_GsmCsComponentName_Type = DisplayString
_GsmCsComponentName_Object = MibTableColumn
gsmCsComponentName = _GsmCsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 1, 1, 2),
    _GsmCsComponentName_Type()
)
gsmCsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsComponentName.setStatus("mandatory")
_GsmCsStorageType_Type = StorageType
_GsmCsStorageType_Object = MibTableColumn
gsmCsStorageType = _GsmCsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 1, 1, 4),
    _GsmCsStorageType_Type()
)
gsmCsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsStorageType.setStatus("mandatory")


class _GsmCsTrunkGrpIndex_Type(Integer32):
    """Custom type gsmCsTrunkGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_GsmCsTrunkGrpIndex_Type.__name__ = "Integer32"
_GsmCsTrunkGrpIndex_Object = MibTableColumn
gsmCsTrunkGrpIndex = _GsmCsTrunkGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 1, 1, 10),
    _GsmCsTrunkGrpIndex_Type()
)
gsmCsTrunkGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmCsTrunkGrpIndex.setStatus("mandatory")
_GsmCsModem_ObjectIdentity = ObjectIdentity
gsmCsModem = _GsmCsModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 2)
)
_GsmCsModemRowStatusTable_Object = MibTable
gsmCsModemRowStatusTable = _GsmCsModemRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 2, 1)
)
if mibBuilder.loadTexts:
    gsmCsModemRowStatusTable.setStatus("mandatory")
_GsmCsModemRowStatusEntry_Object = MibTableRow
gsmCsModemRowStatusEntry = _GsmCsModemRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 2, 1, 1)
)
gsmCsModemRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsModemIndex"),
)
if mibBuilder.loadTexts:
    gsmCsModemRowStatusEntry.setStatus("mandatory")
_GsmCsModemRowStatus_Type = RowStatus
_GsmCsModemRowStatus_Object = MibTableColumn
gsmCsModemRowStatus = _GsmCsModemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 2, 1, 1, 1),
    _GsmCsModemRowStatus_Type()
)
gsmCsModemRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsModemRowStatus.setStatus("mandatory")
_GsmCsModemComponentName_Type = DisplayString
_GsmCsModemComponentName_Object = MibTableColumn
gsmCsModemComponentName = _GsmCsModemComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 2, 1, 1, 2),
    _GsmCsModemComponentName_Type()
)
gsmCsModemComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsModemComponentName.setStatus("mandatory")
_GsmCsModemStorageType_Type = StorageType
_GsmCsModemStorageType_Object = MibTableColumn
gsmCsModemStorageType = _GsmCsModemStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 2, 1, 1, 4),
    _GsmCsModemStorageType_Type()
)
gsmCsModemStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsModemStorageType.setStatus("mandatory")


class _GsmCsModemIndex_Type(Integer32):
    """Custom type gsmCsModemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("v17", 0),
          ("v21", 1),
          ("v22", 2),
          ("v22bis", 3),
          ("v23", 4),
          ("v27ter", 6),
          ("v29", 7),
          ("v32", 8),
          ("v32bis", 9))
    )


_GsmCsModemIndex_Type.__name__ = "Integer32"
_GsmCsModemIndex_Object = MibTableColumn
gsmCsModemIndex = _GsmCsModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 2, 1, 1, 10),
    _GsmCsModemIndex_Type()
)
gsmCsModemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmCsModemIndex.setStatus("mandatory")
_GsmCsRlp_ObjectIdentity = ObjectIdentity
gsmCsRlp = _GsmCsRlp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3)
)
_GsmCsRlpRowStatusTable_Object = MibTable
gsmCsRlpRowStatusTable = _GsmCsRlpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 1)
)
if mibBuilder.loadTexts:
    gsmCsRlpRowStatusTable.setStatus("mandatory")
_GsmCsRlpRowStatusEntry_Object = MibTableRow
gsmCsRlpRowStatusEntry = _GsmCsRlpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 1, 1)
)
gsmCsRlpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsRlpIndex"),
)
if mibBuilder.loadTexts:
    gsmCsRlpRowStatusEntry.setStatus("mandatory")
_GsmCsRlpRowStatus_Type = RowStatus
_GsmCsRlpRowStatus_Object = MibTableColumn
gsmCsRlpRowStatus = _GsmCsRlpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 1, 1, 1),
    _GsmCsRlpRowStatus_Type()
)
gsmCsRlpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsRlpRowStatus.setStatus("mandatory")
_GsmCsRlpComponentName_Type = DisplayString
_GsmCsRlpComponentName_Object = MibTableColumn
gsmCsRlpComponentName = _GsmCsRlpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 1, 1, 2),
    _GsmCsRlpComponentName_Type()
)
gsmCsRlpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsRlpComponentName.setStatus("mandatory")
_GsmCsRlpStorageType_Type = StorageType
_GsmCsRlpStorageType_Object = MibTableColumn
gsmCsRlpStorageType = _GsmCsRlpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 1, 1, 4),
    _GsmCsRlpStorageType_Type()
)
gsmCsRlpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsRlpStorageType.setStatus("mandatory")


class _GsmCsRlpIndex_Type(Integer32):
    """Custom type gsmCsRlpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full12kRate", 2),
          ("full14k5Rate", 3),
          ("full6kRate", 1),
          ("half6kRate", 0))
    )


_GsmCsRlpIndex_Type.__name__ = "Integer32"
_GsmCsRlpIndex_Object = MibTableColumn
gsmCsRlpIndex = _GsmCsRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 1, 1, 10),
    _GsmCsRlpIndex_Type()
)
gsmCsRlpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmCsRlpIndex.setStatus("mandatory")
_GsmCsRlpProvTable_Object = MibTable
gsmCsRlpProvTable = _GsmCsRlpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 10)
)
if mibBuilder.loadTexts:
    gsmCsRlpProvTable.setStatus("mandatory")
_GsmCsRlpProvEntry_Object = MibTableRow
gsmCsRlpProvEntry = _GsmCsRlpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 10, 1)
)
gsmCsRlpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsRlpIndex"),
)
if mibBuilder.loadTexts:
    gsmCsRlpProvEntry.setStatus("mandatory")


class _GsmCsRlpHighestVersion_Type(Unsigned32):
    """Custom type gsmCsRlpHighestVersion based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GsmCsRlpHighestVersion_Type.__name__ = "Unsigned32"
_GsmCsRlpHighestVersion_Object = MibTableColumn
gsmCsRlpHighestVersion = _GsmCsRlpHighestVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 10, 1, 1),
    _GsmCsRlpHighestVersion_Type()
)
gsmCsRlpHighestVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsRlpHighestVersion.setStatus("mandatory")


class _GsmCsRlpIwfToMsWindowSize_Type(Unsigned32):
    """Custom type gsmCsRlpIwfToMsWindowSize based on Unsigned32"""
    defaultValue = 61

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61),
    )


_GsmCsRlpIwfToMsWindowSize_Type.__name__ = "Unsigned32"
_GsmCsRlpIwfToMsWindowSize_Object = MibTableColumn
gsmCsRlpIwfToMsWindowSize = _GsmCsRlpIwfToMsWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 10, 1, 2),
    _GsmCsRlpIwfToMsWindowSize_Type()
)
gsmCsRlpIwfToMsWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsRlpIwfToMsWindowSize.setStatus("mandatory")


class _GsmCsRlpMsToIwfWindowSize_Type(Unsigned32):
    """Custom type gsmCsRlpMsToIwfWindowSize based on Unsigned32"""
    defaultValue = 61

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61),
    )


_GsmCsRlpMsToIwfWindowSize_Type.__name__ = "Unsigned32"
_GsmCsRlpMsToIwfWindowSize_Object = MibTableColumn
gsmCsRlpMsToIwfWindowSize = _GsmCsRlpMsToIwfWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 10, 1, 3),
    _GsmCsRlpMsToIwfWindowSize_Type()
)
gsmCsRlpMsToIwfWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsRlpMsToIwfWindowSize.setStatus("mandatory")


class _GsmCsRlpT1AckTimer_Type(Unsigned32):
    """Custom type gsmCsRlpT1AckTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(380, 1020),
    )


_GsmCsRlpT1AckTimer_Type.__name__ = "Unsigned32"
_GsmCsRlpT1AckTimer_Object = MibTableColumn
gsmCsRlpT1AckTimer = _GsmCsRlpT1AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 10, 1, 4),
    _GsmCsRlpT1AckTimer_Type()
)
gsmCsRlpT1AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsRlpT1AckTimer.setStatus("mandatory")


class _GsmCsRlpT2AckDelayTimer_Type(Unsigned32):
    """Custom type gsmCsRlpT2AckDelayTimer based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 79),
    )


_GsmCsRlpT2AckDelayTimer_Type.__name__ = "Unsigned32"
_GsmCsRlpT2AckDelayTimer_Object = MibTableColumn
gsmCsRlpT2AckDelayTimer = _GsmCsRlpT2AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 10, 1, 5),
    _GsmCsRlpT2AckDelayTimer_Type()
)
gsmCsRlpT2AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsRlpT2AckDelayTimer.setStatus("mandatory")


class _GsmCsRlpN2RetransmitCount_Type(Unsigned32):
    """Custom type gsmCsRlpN2RetransmitCount based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GsmCsRlpN2RetransmitCount_Type.__name__ = "Unsigned32"
_GsmCsRlpN2RetransmitCount_Object = MibTableColumn
gsmCsRlpN2RetransmitCount = _GsmCsRlpN2RetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 3, 10, 1, 6),
    _GsmCsRlpN2RetransmitCount_Type()
)
gsmCsRlpN2RetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsRlpN2RetransmitCount.setStatus("mandatory")
_GsmCsFax_ObjectIdentity = ObjectIdentity
gsmCsFax = _GsmCsFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4)
)
_GsmCsFaxRowStatusTable_Object = MibTable
gsmCsFaxRowStatusTable = _GsmCsFaxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4, 1)
)
if mibBuilder.loadTexts:
    gsmCsFaxRowStatusTable.setStatus("mandatory")
_GsmCsFaxRowStatusEntry_Object = MibTableRow
gsmCsFaxRowStatusEntry = _GsmCsFaxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4, 1, 1)
)
gsmCsFaxRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsFaxIndex"),
)
if mibBuilder.loadTexts:
    gsmCsFaxRowStatusEntry.setStatus("mandatory")
_GsmCsFaxRowStatus_Type = RowStatus
_GsmCsFaxRowStatus_Object = MibTableColumn
gsmCsFaxRowStatus = _GsmCsFaxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4, 1, 1, 1),
    _GsmCsFaxRowStatus_Type()
)
gsmCsFaxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsFaxRowStatus.setStatus("mandatory")
_GsmCsFaxComponentName_Type = DisplayString
_GsmCsFaxComponentName_Object = MibTableColumn
gsmCsFaxComponentName = _GsmCsFaxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4, 1, 1, 2),
    _GsmCsFaxComponentName_Type()
)
gsmCsFaxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsFaxComponentName.setStatus("mandatory")
_GsmCsFaxStorageType_Type = StorageType
_GsmCsFaxStorageType_Object = MibTableColumn
gsmCsFaxStorageType = _GsmCsFaxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4, 1, 1, 4),
    _GsmCsFaxStorageType_Type()
)
gsmCsFaxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsFaxStorageType.setStatus("mandatory")
_GsmCsFaxIndex_Type = NonReplicated
_GsmCsFaxIndex_Object = MibTableColumn
gsmCsFaxIndex = _GsmCsFaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4, 1, 1, 10),
    _GsmCsFaxIndex_Type()
)
gsmCsFaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmCsFaxIndex.setStatus("mandatory")
_GsmCsFaxProvTable_Object = MibTable
gsmCsFaxProvTable = _GsmCsFaxProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4, 10)
)
if mibBuilder.loadTexts:
    gsmCsFaxProvTable.setStatus("mandatory")
_GsmCsFaxProvEntry_Object = MibTableRow
gsmCsFaxProvEntry = _GsmCsFaxProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4, 10, 1)
)
gsmCsFaxProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsFaxIndex"),
)
if mibBuilder.loadTexts:
    gsmCsFaxProvEntry.setStatus("mandatory")


class _GsmCsFaxT1CalledToneTimer_Type(FixedPoint2):
    """Custom type gsmCsFaxT1CalledToneTimer based on FixedPoint2"""
    defaultValue = 180

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 300),
    )


_GsmCsFaxT1CalledToneTimer_Type.__name__ = "FixedPoint2"
_GsmCsFaxT1CalledToneTimer_Object = MibTableColumn
gsmCsFaxT1CalledToneTimer = _GsmCsFaxT1CalledToneTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 4, 10, 1, 1),
    _GsmCsFaxT1CalledToneTimer_Type()
)
gsmCsFaxT1CalledToneTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsFaxT1CalledToneTimer.setStatus("mandatory")
_GsmCsV42_ObjectIdentity = ObjectIdentity
gsmCsV42 = _GsmCsV42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5)
)
_GsmCsV42RowStatusTable_Object = MibTable
gsmCsV42RowStatusTable = _GsmCsV42RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 1)
)
if mibBuilder.loadTexts:
    gsmCsV42RowStatusTable.setStatus("mandatory")
_GsmCsV42RowStatusEntry_Object = MibTableRow
gsmCsV42RowStatusEntry = _GsmCsV42RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 1, 1)
)
gsmCsV42RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsV42Index"),
)
if mibBuilder.loadTexts:
    gsmCsV42RowStatusEntry.setStatus("mandatory")
_GsmCsV42RowStatus_Type = RowStatus
_GsmCsV42RowStatus_Object = MibTableColumn
gsmCsV42RowStatus = _GsmCsV42RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 1, 1, 1),
    _GsmCsV42RowStatus_Type()
)
gsmCsV42RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsV42RowStatus.setStatus("mandatory")
_GsmCsV42ComponentName_Type = DisplayString
_GsmCsV42ComponentName_Object = MibTableColumn
gsmCsV42ComponentName = _GsmCsV42ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 1, 1, 2),
    _GsmCsV42ComponentName_Type()
)
gsmCsV42ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsV42ComponentName.setStatus("mandatory")
_GsmCsV42StorageType_Type = StorageType
_GsmCsV42StorageType_Object = MibTableColumn
gsmCsV42StorageType = _GsmCsV42StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 1, 1, 4),
    _GsmCsV42StorageType_Type()
)
gsmCsV42StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsV42StorageType.setStatus("mandatory")
_GsmCsV42Index_Type = NonReplicated
_GsmCsV42Index_Object = MibTableColumn
gsmCsV42Index = _GsmCsV42Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 1, 1, 10),
    _GsmCsV42Index_Type()
)
gsmCsV42Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmCsV42Index.setStatus("mandatory")
_GsmCsV42ProvTable_Object = MibTable
gsmCsV42ProvTable = _GsmCsV42ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10)
)
if mibBuilder.loadTexts:
    gsmCsV42ProvTable.setStatus("mandatory")
_GsmCsV42ProvEntry_Object = MibTableRow
gsmCsV42ProvEntry = _GsmCsV42ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1)
)
gsmCsV42ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsV42Index"),
)
if mibBuilder.loadTexts:
    gsmCsV42ProvEntry.setStatus("mandatory")


class _GsmCsV42T400DetectTimer_Type(FixedPoint2):
    """Custom type gsmCsV42T400DetectTimer based on FixedPoint2"""
    defaultValue = 200

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 254),
    )


_GsmCsV42T400DetectTimer_Type.__name__ = "FixedPoint2"
_GsmCsV42T400DetectTimer_Object = MibTableColumn
gsmCsV42T400DetectTimer = _GsmCsV42T400DetectTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1, 1),
    _GsmCsV42T400DetectTimer_Type()
)
gsmCsV42T400DetectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42T400DetectTimer.setStatus("mandatory")


class _GsmCsV42T401AckTimer_Type(FixedPoint2):
    """Custom type gsmCsV42T401AckTimer based on FixedPoint2"""
    defaultValue = 400

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 900),
    )


_GsmCsV42T401AckTimer_Type.__name__ = "FixedPoint2"
_GsmCsV42T401AckTimer_Object = MibTableColumn
gsmCsV42T401AckTimer = _GsmCsV42T401AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1, 2),
    _GsmCsV42T401AckTimer_Type()
)
gsmCsV42T401AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42T401AckTimer.setStatus("mandatory")


class _GsmCsV42T402AckDelayTimer_Type(FixedPoint2):
    """Custom type gsmCsV42T402AckDelayTimer based on FixedPoint2"""
    defaultValue = 200

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 450),
    )


_GsmCsV42T402AckDelayTimer_Type.__name__ = "FixedPoint2"
_GsmCsV42T402AckDelayTimer_Object = MibTableColumn
gsmCsV42T402AckDelayTimer = _GsmCsV42T402AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1, 3),
    _GsmCsV42T402AckDelayTimer_Type()
)
gsmCsV42T402AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42T402AckDelayTimer.setStatus("mandatory")


class _GsmCsV42T403IdleProbeTimer_Type(Unsigned32):
    """Custom type gsmCsV42T403IdleProbeTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 90),
    )


_GsmCsV42T403IdleProbeTimer_Type.__name__ = "Unsigned32"
_GsmCsV42T403IdleProbeTimer_Object = MibTableColumn
gsmCsV42T403IdleProbeTimer = _GsmCsV42T403IdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1, 4),
    _GsmCsV42T403IdleProbeTimer_Type()
)
gsmCsV42T403IdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42T403IdleProbeTimer.setStatus("mandatory")


class _GsmCsV42TxN401FrameSize_Type(Unsigned32):
    """Custom type gsmCsV42TxN401FrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GsmCsV42TxN401FrameSize_Type.__name__ = "Unsigned32"
_GsmCsV42TxN401FrameSize_Object = MibTableColumn
gsmCsV42TxN401FrameSize = _GsmCsV42TxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1, 5),
    _GsmCsV42TxN401FrameSize_Type()
)
gsmCsV42TxN401FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42TxN401FrameSize.setStatus("mandatory")


class _GsmCsV42RxN401FrameSize_Type(Unsigned32):
    """Custom type gsmCsV42RxN401FrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GsmCsV42RxN401FrameSize_Type.__name__ = "Unsigned32"
_GsmCsV42RxN401FrameSize_Object = MibTableColumn
gsmCsV42RxN401FrameSize = _GsmCsV42RxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1, 6),
    _GsmCsV42RxN401FrameSize_Type()
)
gsmCsV42RxN401FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42RxN401FrameSize.setStatus("mandatory")


class _GsmCsV42TxKwindowSize_Type(Unsigned32):
    """Custom type gsmCsV42TxKwindowSize based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GsmCsV42TxKwindowSize_Type.__name__ = "Unsigned32"
_GsmCsV42TxKwindowSize_Object = MibTableColumn
gsmCsV42TxKwindowSize = _GsmCsV42TxKwindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1, 7),
    _GsmCsV42TxKwindowSize_Type()
)
gsmCsV42TxKwindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42TxKwindowSize.setStatus("mandatory")


class _GsmCsV42RxKwindowSize_Type(Unsigned32):
    """Custom type gsmCsV42RxKwindowSize based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GsmCsV42RxKwindowSize_Type.__name__ = "Unsigned32"
_GsmCsV42RxKwindowSize_Object = MibTableColumn
gsmCsV42RxKwindowSize = _GsmCsV42RxKwindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1, 8),
    _GsmCsV42RxKwindowSize_Type()
)
gsmCsV42RxKwindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42RxKwindowSize.setStatus("mandatory")


class _GsmCsV42N400RetransLimit_Type(Unsigned32):
    """Custom type gsmCsV42N400RetransLimit based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GsmCsV42N400RetransLimit_Type.__name__ = "Unsigned32"
_GsmCsV42N400RetransLimit_Object = MibTableColumn
gsmCsV42N400RetransLimit = _GsmCsV42N400RetransLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 5, 10, 1, 9),
    _GsmCsV42N400RetransLimit_Type()
)
gsmCsV42N400RetransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42N400RetransLimit.setStatus("mandatory")
_GsmCsV42bis_ObjectIdentity = ObjectIdentity
gsmCsV42bis = _GsmCsV42bis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6)
)
_GsmCsV42bisRowStatusTable_Object = MibTable
gsmCsV42bisRowStatusTable = _GsmCsV42bisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 1)
)
if mibBuilder.loadTexts:
    gsmCsV42bisRowStatusTable.setStatus("mandatory")
_GsmCsV42bisRowStatusEntry_Object = MibTableRow
gsmCsV42bisRowStatusEntry = _GsmCsV42bisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 1, 1)
)
gsmCsV42bisRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsV42bisIndex"),
)
if mibBuilder.loadTexts:
    gsmCsV42bisRowStatusEntry.setStatus("mandatory")
_GsmCsV42bisRowStatus_Type = RowStatus
_GsmCsV42bisRowStatus_Object = MibTableColumn
gsmCsV42bisRowStatus = _GsmCsV42bisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 1, 1, 1),
    _GsmCsV42bisRowStatus_Type()
)
gsmCsV42bisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsV42bisRowStatus.setStatus("mandatory")
_GsmCsV42bisComponentName_Type = DisplayString
_GsmCsV42bisComponentName_Object = MibTableColumn
gsmCsV42bisComponentName = _GsmCsV42bisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 1, 1, 2),
    _GsmCsV42bisComponentName_Type()
)
gsmCsV42bisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsV42bisComponentName.setStatus("mandatory")
_GsmCsV42bisStorageType_Type = StorageType
_GsmCsV42bisStorageType_Object = MibTableColumn
gsmCsV42bisStorageType = _GsmCsV42bisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 1, 1, 4),
    _GsmCsV42bisStorageType_Type()
)
gsmCsV42bisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsV42bisStorageType.setStatus("mandatory")
_GsmCsV42bisIndex_Type = NonReplicated
_GsmCsV42bisIndex_Object = MibTableColumn
gsmCsV42bisIndex = _GsmCsV42bisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 1, 1, 10),
    _GsmCsV42bisIndex_Type()
)
gsmCsV42bisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmCsV42bisIndex.setStatus("mandatory")
_GsmCsV42bisProvTable_Object = MibTable
gsmCsV42bisProvTable = _GsmCsV42bisProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 10)
)
if mibBuilder.loadTexts:
    gsmCsV42bisProvTable.setStatus("mandatory")
_GsmCsV42bisProvEntry_Object = MibTableRow
gsmCsV42bisProvEntry = _GsmCsV42bisProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 10, 1)
)
gsmCsV42bisProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsV42bisIndex"),
)
if mibBuilder.loadTexts:
    gsmCsV42bisProvEntry.setStatus("mandatory")


class _GsmCsV42bisCompressionDirection_Type(Integer32):
    """Custom type gsmCsV42bisCompressionDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("decode", 2),
          ("encode", 1),
          ("none", 0))
    )


_GsmCsV42bisCompressionDirection_Type.__name__ = "Integer32"
_GsmCsV42bisCompressionDirection_Object = MibTableColumn
gsmCsV42bisCompressionDirection = _GsmCsV42bisCompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 10, 1, 1),
    _GsmCsV42bisCompressionDirection_Type()
)
gsmCsV42bisCompressionDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42bisCompressionDirection.setStatus("mandatory")


class _GsmCsV42bisMaximumCodewords_Type(Unsigned32):
    """Custom type gsmCsV42bisMaximumCodewords based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_GsmCsV42bisMaximumCodewords_Type.__name__ = "Unsigned32"
_GsmCsV42bisMaximumCodewords_Object = MibTableColumn
gsmCsV42bisMaximumCodewords = _GsmCsV42bisMaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 10, 1, 2),
    _GsmCsV42bisMaximumCodewords_Type()
)
gsmCsV42bisMaximumCodewords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42bisMaximumCodewords.setStatus("mandatory")


class _GsmCsV42bisMaximumStringSize_Type(Unsigned32):
    """Custom type gsmCsV42bisMaximumStringSize based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_GsmCsV42bisMaximumStringSize_Type.__name__ = "Unsigned32"
_GsmCsV42bisMaximumStringSize_Object = MibTableColumn
gsmCsV42bisMaximumStringSize = _GsmCsV42bisMaximumStringSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 10, 1, 3),
    _GsmCsV42bisMaximumStringSize_Type()
)
gsmCsV42bisMaximumStringSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42bisMaximumStringSize.setStatus("mandatory")


class _GsmCsV42bisActionOnError_Type(Integer32):
    """Custom type gsmCsV42bisActionOnError based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resetLink", 0),
          ("takeDownCall", 1))
    )


_GsmCsV42bisActionOnError_Type.__name__ = "Integer32"
_GsmCsV42bisActionOnError_Object = MibTableColumn
gsmCsV42bisActionOnError = _GsmCsV42bisActionOnError_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 6, 10, 1, 4),
    _GsmCsV42bisActionOnError_Type()
)
gsmCsV42bisActionOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsV42bisActionOnError.setStatus("mandatory")
_GsmCsLp_ObjectIdentity = ObjectIdentity
gsmCsLp = _GsmCsLp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7)
)
_GsmCsLpRowStatusTable_Object = MibTable
gsmCsLpRowStatusTable = _GsmCsLpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 1)
)
if mibBuilder.loadTexts:
    gsmCsLpRowStatusTable.setStatus("mandatory")
_GsmCsLpRowStatusEntry_Object = MibTableRow
gsmCsLpRowStatusEntry = _GsmCsLpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 1, 1)
)
gsmCsLpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsLpIndex"),
)
if mibBuilder.loadTexts:
    gsmCsLpRowStatusEntry.setStatus("mandatory")
_GsmCsLpRowStatus_Type = RowStatus
_GsmCsLpRowStatus_Object = MibTableColumn
gsmCsLpRowStatus = _GsmCsLpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 1, 1, 1),
    _GsmCsLpRowStatus_Type()
)
gsmCsLpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsLpRowStatus.setStatus("mandatory")
_GsmCsLpComponentName_Type = DisplayString
_GsmCsLpComponentName_Object = MibTableColumn
gsmCsLpComponentName = _GsmCsLpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 1, 1, 2),
    _GsmCsLpComponentName_Type()
)
gsmCsLpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsLpComponentName.setStatus("mandatory")
_GsmCsLpStorageType_Type = StorageType
_GsmCsLpStorageType_Object = MibTableColumn
gsmCsLpStorageType = _GsmCsLpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 1, 1, 4),
    _GsmCsLpStorageType_Type()
)
gsmCsLpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsLpStorageType.setStatus("mandatory")


class _GsmCsLpIndex_Type(Integer32):
    """Custom type gsmCsLpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GsmCsLpIndex_Type.__name__ = "Integer32"
_GsmCsLpIndex_Object = MibTableColumn
gsmCsLpIndex = _GsmCsLpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 1, 1, 10),
    _GsmCsLpIndex_Type()
)
gsmCsLpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmCsLpIndex.setStatus("mandatory")
_GsmCsLpOperTable_Object = MibTable
gsmCsLpOperTable = _GsmCsLpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 10)
)
if mibBuilder.loadTexts:
    gsmCsLpOperTable.setStatus("mandatory")
_GsmCsLpOperEntry_Object = MibTableRow
gsmCsLpOperEntry = _GsmCsLpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 10, 1)
)
gsmCsLpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsLpIndex"),
)
if mibBuilder.loadTexts:
    gsmCsLpOperEntry.setStatus("mandatory")


class _GsmCsLpConfiguredBearerChannels_Type(Unsigned32):
    """Custom type gsmCsLpConfiguredBearerChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_GsmCsLpConfiguredBearerChannels_Type.__name__ = "Unsigned32"
_GsmCsLpConfiguredBearerChannels_Object = MibTableColumn
gsmCsLpConfiguredBearerChannels = _GsmCsLpConfiguredBearerChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 10, 1, 1),
    _GsmCsLpConfiguredBearerChannels_Type()
)
gsmCsLpConfiguredBearerChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsLpConfiguredBearerChannels.setStatus("mandatory")


class _GsmCsLpActiveCalls_Type(Gauge32):
    """Custom type gsmCsLpActiveCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_GsmCsLpActiveCalls_Type.__name__ = "Gauge32"
_GsmCsLpActiveCalls_Object = MibTableColumn
gsmCsLpActiveCalls = _GsmCsLpActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 10, 1, 2),
    _GsmCsLpActiveCalls_Type()
)
gsmCsLpActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsLpActiveCalls.setStatus("mandatory")


class _GsmCsLpAssignedCapacity_Type(Unsigned32):
    """Custom type gsmCsLpAssignedCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GsmCsLpAssignedCapacity_Type.__name__ = "Unsigned32"
_GsmCsLpAssignedCapacity_Object = MibTableColumn
gsmCsLpAssignedCapacity = _GsmCsLpAssignedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 10, 1, 3),
    _GsmCsLpAssignedCapacity_Type()
)
gsmCsLpAssignedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsLpAssignedCapacity.setStatus("mandatory")


class _GsmCsLpModemsSupported_Type(Integer32):
    """Custom type gsmCsLpModemsSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_GsmCsLpModemsSupported_Type.__name__ = "Integer32"
_GsmCsLpModemsSupported_Object = MibTableColumn
gsmCsLpModemsSupported = _GsmCsLpModemsSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 7, 10, 1, 4),
    _GsmCsLpModemsSupported_Type()
)
gsmCsLpModemsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsLpModemsSupported.setStatus("mandatory")
_GsmCsProvTable_Object = MibTable
gsmCsProvTable = _GsmCsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 100)
)
if mibBuilder.loadTexts:
    gsmCsProvTable.setStatus("mandatory")
_GsmCsProvEntry_Object = MibTableRow
gsmCsProvEntry = _GsmCsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 100, 1)
)
gsmCsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    gsmCsProvEntry.setStatus("mandatory")


class _GsmCsCommentText_Type(AsciiString):
    """Custom type gsmCsCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GsmCsCommentText_Type.__name__ = "AsciiString"
_GsmCsCommentText_Object = MibTableColumn
gsmCsCommentText = _GsmCsCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 100, 1, 1),
    _GsmCsCommentText_Type()
)
gsmCsCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsCommentText.setStatus("mandatory")


class _GsmCsMscIpAddress_Type(IpAddress):
    """Custom type gsmCsMscIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_GsmCsMscIpAddress_Object = MibTableColumn
gsmCsMscIpAddress = _GsmCsMscIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 100, 1, 2),
    _GsmCsMscIpAddress_Type()
)
gsmCsMscIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsMscIpAddress.setStatus("mandatory")
_GsmCsVirtualRouterName_Type = RowPointer
_GsmCsVirtualRouterName_Object = MibTableColumn
gsmCsVirtualRouterName = _GsmCsVirtualRouterName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 100, 1, 4),
    _GsmCsVirtualRouterName_Type()
)
gsmCsVirtualRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsVirtualRouterName.setStatus("mandatory")


class _GsmCsVoiceLaw_Type(Integer32):
    """Custom type gsmCsVoiceLaw based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 0),
          ("muLaw", 1))
    )


_GsmCsVoiceLaw_Type.__name__ = "Integer32"
_GsmCsVoiceLaw_Object = MibTableColumn
gsmCsVoiceLaw = _GsmCsVoiceLaw_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 100, 1, 5),
    _GsmCsVoiceLaw_Type()
)
gsmCsVoiceLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsVoiceLaw.setStatus("mandatory")
_GsmCsCidDataTable_Object = MibTable
gsmCsCidDataTable = _GsmCsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 103)
)
if mibBuilder.loadTexts:
    gsmCsCidDataTable.setStatus("mandatory")
_GsmCsCidDataEntry_Object = MibTableRow
gsmCsCidDataEntry = _GsmCsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 103, 1)
)
gsmCsCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    gsmCsCidDataEntry.setStatus("mandatory")


class _GsmCsCustomerIdentifier_Type(Unsigned32):
    """Custom type gsmCsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_GsmCsCustomerIdentifier_Type.__name__ = "Unsigned32"
_GsmCsCustomerIdentifier_Object = MibTableColumn
gsmCsCustomerIdentifier = _GsmCsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 103, 1, 1),
    _GsmCsCustomerIdentifier_Type()
)
gsmCsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmCsCustomerIdentifier.setStatus("mandatory")
_GsmCsStateTable_Object = MibTable
gsmCsStateTable = _GsmCsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 104)
)
if mibBuilder.loadTexts:
    gsmCsStateTable.setStatus("mandatory")
_GsmCsStateEntry_Object = MibTableRow
gsmCsStateEntry = _GsmCsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 104, 1)
)
gsmCsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    gsmCsStateEntry.setStatus("mandatory")


class _GsmCsAdminState_Type(Integer32):
    """Custom type gsmCsAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_GsmCsAdminState_Type.__name__ = "Integer32"
_GsmCsAdminState_Object = MibTableColumn
gsmCsAdminState = _GsmCsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 104, 1, 1),
    _GsmCsAdminState_Type()
)
gsmCsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsAdminState.setStatus("mandatory")


class _GsmCsOperationalState_Type(Integer32):
    """Custom type gsmCsOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GsmCsOperationalState_Type.__name__ = "Integer32"
_GsmCsOperationalState_Object = MibTableColumn
gsmCsOperationalState = _GsmCsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 104, 1, 2),
    _GsmCsOperationalState_Type()
)
gsmCsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsOperationalState.setStatus("mandatory")


class _GsmCsUsageState_Type(Integer32):
    """Custom type gsmCsUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_GsmCsUsageState_Type.__name__ = "Integer32"
_GsmCsUsageState_Object = MibTableColumn
gsmCsUsageState = _GsmCsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 104, 1, 3),
    _GsmCsUsageState_Type()
)
gsmCsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsUsageState.setStatus("mandatory")
_GsmCsStatsTable_Object = MibTable
gsmCsStatsTable = _GsmCsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121)
)
if mibBuilder.loadTexts:
    gsmCsStatsTable.setStatus("mandatory")
_GsmCsStatsEntry_Object = MibTableRow
gsmCsStatsEntry = _GsmCsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1)
)
gsmCsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    gsmCsStatsEntry.setStatus("mandatory")


class _GsmCsCurrentCalls_Type(Gauge32):
    """Custom type gsmCsCurrentCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_GsmCsCurrentCalls_Type.__name__ = "Gauge32"
_GsmCsCurrentCalls_Object = MibTableColumn
gsmCsCurrentCalls = _GsmCsCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 1),
    _GsmCsCurrentCalls_Type()
)
gsmCsCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsCurrentCalls.setStatus("mandatory")
_GsmCsCallsRequested_Type = Counter32
_GsmCsCallsRequested_Object = MibTableColumn
gsmCsCallsRequested = _GsmCsCallsRequested_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 2),
    _GsmCsCallsRequested_Type()
)
gsmCsCallsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsCallsRequested.setStatus("mandatory")
_GsmCsCallsSetup_Type = Counter32
_GsmCsCallsSetup_Object = MibTableColumn
gsmCsCallsSetup = _GsmCsCallsSetup_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 3),
    _GsmCsCallsSetup_Type()
)
gsmCsCallsSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsCallsSetup.setStatus("mandatory")
_GsmCsCallsActivated_Type = Counter32
_GsmCsCallsActivated_Object = MibTableColumn
gsmCsCallsActivated = _GsmCsCallsActivated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 4),
    _GsmCsCallsActivated_Type()
)
gsmCsCallsActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsCallsActivated.setStatus("mandatory")
_GsmCsCallsReleasedNormal_Type = Counter32
_GsmCsCallsReleasedNormal_Object = MibTableColumn
gsmCsCallsReleasedNormal = _GsmCsCallsReleasedNormal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 5),
    _GsmCsCallsReleasedNormal_Type()
)
gsmCsCallsReleasedNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsCallsReleasedNormal.setStatus("mandatory")
_GsmCsCallsReleasedAbnormal_Type = Counter32
_GsmCsCallsReleasedAbnormal_Object = MibTableColumn
gsmCsCallsReleasedAbnormal = _GsmCsCallsReleasedAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 6),
    _GsmCsCallsReleasedAbnormal_Type()
)
gsmCsCallsReleasedAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsCallsReleasedAbnormal.setStatus("mandatory")
_GsmCsChannelConfigChanges_Type = Counter32
_GsmCsChannelConfigChanges_Object = MibTableColumn
gsmCsChannelConfigChanges = _GsmCsChannelConfigChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 7),
    _GsmCsChannelConfigChanges_Type()
)
gsmCsChannelConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsChannelConfigChanges.setStatus("mandatory")
_GsmCsChannelModeModifyRequests_Type = Counter32
_GsmCsChannelModeModifyRequests_Object = MibTableColumn
gsmCsChannelModeModifyRequests = _GsmCsChannelModeModifyRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 8),
    _GsmCsChannelModeModifyRequests_Type()
)
gsmCsChannelModeModifyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsChannelModeModifyRequests.setStatus("mandatory")
_GsmCsStatusMessagesRx_Type = Counter32
_GsmCsStatusMessagesRx_Object = MibTableColumn
gsmCsStatusMessagesRx = _GsmCsStatusMessagesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 9),
    _GsmCsStatusMessagesRx_Type()
)
gsmCsStatusMessagesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsStatusMessagesRx.setStatus("mandatory")
_GsmCsErroredMipFrames_Type = Counter32
_GsmCsErroredMipFrames_Object = MibTableColumn
gsmCsErroredMipFrames = _GsmCsErroredMipFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 127, 121, 1, 10),
    _GsmCsErroredMipFrames_Type()
)
gsmCsErroredMipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCsErroredMipFrames.setStatus("mandatory")
_GsmBc_ObjectIdentity = ObjectIdentity
gsmBc = _GsmBc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128)
)
_GsmBcRowStatusTable_Object = MibTable
gsmBcRowStatusTable = _GsmBcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 1)
)
if mibBuilder.loadTexts:
    gsmBcRowStatusTable.setStatus("mandatory")
_GsmBcRowStatusEntry_Object = MibTableRow
gsmBcRowStatusEntry = _GsmBcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 1, 1)
)
gsmBcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
)
if mibBuilder.loadTexts:
    gsmBcRowStatusEntry.setStatus("mandatory")
_GsmBcRowStatus_Type = RowStatus
_GsmBcRowStatus_Object = MibTableColumn
gsmBcRowStatus = _GsmBcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 1, 1, 1),
    _GsmBcRowStatus_Type()
)
gsmBcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmBcRowStatus.setStatus("mandatory")
_GsmBcComponentName_Type = DisplayString
_GsmBcComponentName_Object = MibTableColumn
gsmBcComponentName = _GsmBcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 1, 1, 2),
    _GsmBcComponentName_Type()
)
gsmBcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcComponentName.setStatus("mandatory")
_GsmBcStorageType_Type = StorageType
_GsmBcStorageType_Object = MibTableColumn
gsmBcStorageType = _GsmBcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 1, 1, 4),
    _GsmBcStorageType_Type()
)
gsmBcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcStorageType.setStatus("mandatory")


class _GsmBcTrunkGrpIndex_Type(Integer32):
    """Custom type gsmBcTrunkGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_GsmBcTrunkGrpIndex_Type.__name__ = "Integer32"
_GsmBcTrunkGrpIndex_Object = MibTableColumn
gsmBcTrunkGrpIndex = _GsmBcTrunkGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 1, 1, 10),
    _GsmBcTrunkGrpIndex_Type()
)
gsmBcTrunkGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcTrunkGrpIndex.setStatus("mandatory")


class _GsmBcCicIndex_Type(Integer32):
    """Custom type gsmBcCicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_GsmBcCicIndex_Type.__name__ = "Integer32"
_GsmBcCicIndex_Object = MibTableColumn
gsmBcCicIndex = _GsmBcCicIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 1, 1, 11),
    _GsmBcCicIndex_Type()
)
gsmBcCicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcCicIndex.setStatus("mandatory")
_GsmBcFramer_ObjectIdentity = ObjectIdentity
gsmBcFramer = _GsmBcFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2)
)
_GsmBcFramerRowStatusTable_Object = MibTable
gsmBcFramerRowStatusTable = _GsmBcFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 1)
)
if mibBuilder.loadTexts:
    gsmBcFramerRowStatusTable.setStatus("mandatory")
_GsmBcFramerRowStatusEntry_Object = MibTableRow
gsmBcFramerRowStatusEntry = _GsmBcFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 1, 1)
)
gsmBcFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    gsmBcFramerRowStatusEntry.setStatus("mandatory")
_GsmBcFramerRowStatus_Type = RowStatus
_GsmBcFramerRowStatus_Object = MibTableColumn
gsmBcFramerRowStatus = _GsmBcFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 1, 1, 1),
    _GsmBcFramerRowStatus_Type()
)
gsmBcFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerRowStatus.setStatus("mandatory")
_GsmBcFramerComponentName_Type = DisplayString
_GsmBcFramerComponentName_Object = MibTableColumn
gsmBcFramerComponentName = _GsmBcFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 1, 1, 2),
    _GsmBcFramerComponentName_Type()
)
gsmBcFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerComponentName.setStatus("mandatory")
_GsmBcFramerStorageType_Type = StorageType
_GsmBcFramerStorageType_Object = MibTableColumn
gsmBcFramerStorageType = _GsmBcFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 1, 1, 4),
    _GsmBcFramerStorageType_Type()
)
gsmBcFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerStorageType.setStatus("mandatory")
_GsmBcFramerIndex_Type = NonReplicated
_GsmBcFramerIndex_Object = MibTableColumn
gsmBcFramerIndex = _GsmBcFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 1, 1, 10),
    _GsmBcFramerIndex_Type()
)
gsmBcFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcFramerIndex.setStatus("mandatory")
_GsmBcFramerProvTable_Object = MibTable
gsmBcFramerProvTable = _GsmBcFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 10)
)
if mibBuilder.loadTexts:
    gsmBcFramerProvTable.setStatus("mandatory")
_GsmBcFramerProvEntry_Object = MibTableRow
gsmBcFramerProvEntry = _GsmBcFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 10, 1)
)
gsmBcFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    gsmBcFramerProvEntry.setStatus("mandatory")
_GsmBcFramerInterfaceName_Type = Link
_GsmBcFramerInterfaceName_Object = MibTableColumn
gsmBcFramerInterfaceName = _GsmBcFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 10, 1, 1),
    _GsmBcFramerInterfaceName_Type()
)
gsmBcFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmBcFramerInterfaceName.setStatus("mandatory")
_GsmBcFramerStatsTable_Object = MibTable
gsmBcFramerStatsTable = _GsmBcFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11)
)
if mibBuilder.loadTexts:
    gsmBcFramerStatsTable.setStatus("mandatory")
_GsmBcFramerStatsEntry_Object = MibTableRow
gsmBcFramerStatsEntry = _GsmBcFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11, 1)
)
gsmBcFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    gsmBcFramerStatsEntry.setStatus("mandatory")
_GsmBcFramerFrmToIf_Type = Counter32
_GsmBcFramerFrmToIf_Object = MibTableColumn
gsmBcFramerFrmToIf = _GsmBcFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11, 1, 1),
    _GsmBcFramerFrmToIf_Type()
)
gsmBcFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerFrmToIf.setStatus("mandatory")
_GsmBcFramerFrmFromIf_Type = Counter32
_GsmBcFramerFrmFromIf_Object = MibTableColumn
gsmBcFramerFrmFromIf = _GsmBcFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11, 1, 2),
    _GsmBcFramerFrmFromIf_Type()
)
gsmBcFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerFrmFromIf.setStatus("mandatory")
_GsmBcFramerOctetFromIf_Type = Counter32
_GsmBcFramerOctetFromIf_Object = MibTableColumn
gsmBcFramerOctetFromIf = _GsmBcFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11, 1, 3),
    _GsmBcFramerOctetFromIf_Type()
)
gsmBcFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerOctetFromIf.setStatus("mandatory")
_GsmBcFramerCrcErrors_Type = Counter32
_GsmBcFramerCrcErrors_Object = MibTableColumn
gsmBcFramerCrcErrors = _GsmBcFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11, 1, 5),
    _GsmBcFramerCrcErrors_Type()
)
gsmBcFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerCrcErrors.setStatus("mandatory")
_GsmBcFramerLrcErrors_Type = Counter32
_GsmBcFramerLrcErrors_Object = MibTableColumn
gsmBcFramerLrcErrors = _GsmBcFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11, 1, 6),
    _GsmBcFramerLrcErrors_Type()
)
gsmBcFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerLrcErrors.setStatus("mandatory")
_GsmBcFramerNonOctetErrors_Type = Counter32
_GsmBcFramerNonOctetErrors_Object = MibTableColumn
gsmBcFramerNonOctetErrors = _GsmBcFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11, 1, 7),
    _GsmBcFramerNonOctetErrors_Type()
)
gsmBcFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerNonOctetErrors.setStatus("mandatory")
_GsmBcFramerOverruns_Type = Counter32
_GsmBcFramerOverruns_Object = MibTableColumn
gsmBcFramerOverruns = _GsmBcFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11, 1, 8),
    _GsmBcFramerOverruns_Type()
)
gsmBcFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerOverruns.setStatus("mandatory")
_GsmBcFramerUnderruns_Type = Counter32
_GsmBcFramerUnderruns_Object = MibTableColumn
gsmBcFramerUnderruns = _GsmBcFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 11, 1, 9),
    _GsmBcFramerUnderruns_Type()
)
gsmBcFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerUnderruns.setStatus("mandatory")
_GsmBcFramerLinkTable_Object = MibTable
gsmBcFramerLinkTable = _GsmBcFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 12)
)
if mibBuilder.loadTexts:
    gsmBcFramerLinkTable.setStatus("mandatory")
_GsmBcFramerLinkEntry_Object = MibTableRow
gsmBcFramerLinkEntry = _GsmBcFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 12, 1)
)
gsmBcFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    gsmBcFramerLinkEntry.setStatus("mandatory")


class _GsmBcFramerFramingType_Type(Integer32):
    """Custom type gsmBcFramerFramingType based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("btdsFraming", 2),
          ("gsmFraming", 8))
    )


_GsmBcFramerFramingType_Type.__name__ = "Integer32"
_GsmBcFramerFramingType_Object = MibTableColumn
gsmBcFramerFramingType = _GsmBcFramerFramingType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 12, 1, 1),
    _GsmBcFramerFramingType_Type()
)
gsmBcFramerFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmBcFramerFramingType.setStatus("mandatory")
_GsmBcFramerStateTable_Object = MibTable
gsmBcFramerStateTable = _GsmBcFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 13)
)
if mibBuilder.loadTexts:
    gsmBcFramerStateTable.setStatus("mandatory")
_GsmBcFramerStateEntry_Object = MibTableRow
gsmBcFramerStateEntry = _GsmBcFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 13, 1)
)
gsmBcFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    gsmBcFramerStateEntry.setStatus("mandatory")


class _GsmBcFramerAdminState_Type(Integer32):
    """Custom type gsmBcFramerAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_GsmBcFramerAdminState_Type.__name__ = "Integer32"
_GsmBcFramerAdminState_Object = MibTableColumn
gsmBcFramerAdminState = _GsmBcFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 13, 1, 1),
    _GsmBcFramerAdminState_Type()
)
gsmBcFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerAdminState.setStatus("mandatory")


class _GsmBcFramerOperationalState_Type(Integer32):
    """Custom type gsmBcFramerOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GsmBcFramerOperationalState_Type.__name__ = "Integer32"
_GsmBcFramerOperationalState_Object = MibTableColumn
gsmBcFramerOperationalState = _GsmBcFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 13, 1, 2),
    _GsmBcFramerOperationalState_Type()
)
gsmBcFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerOperationalState.setStatus("mandatory")


class _GsmBcFramerUsageState_Type(Integer32):
    """Custom type gsmBcFramerUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_GsmBcFramerUsageState_Type.__name__ = "Integer32"
_GsmBcFramerUsageState_Object = MibTableColumn
gsmBcFramerUsageState = _GsmBcFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 2, 13, 1, 3),
    _GsmBcFramerUsageState_Type()
)
gsmBcFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFramerUsageState.setStatus("mandatory")
_GsmBcLayer1_ObjectIdentity = ObjectIdentity
gsmBcLayer1 = _GsmBcLayer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3)
)
_GsmBcLayer1RowStatusTable_Object = MibTable
gsmBcLayer1RowStatusTable = _GsmBcLayer1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 1)
)
if mibBuilder.loadTexts:
    gsmBcLayer1RowStatusTable.setStatus("mandatory")
_GsmBcLayer1RowStatusEntry_Object = MibTableRow
gsmBcLayer1RowStatusEntry = _GsmBcLayer1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 1, 1)
)
gsmBcLayer1RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcLayer1Index"),
)
if mibBuilder.loadTexts:
    gsmBcLayer1RowStatusEntry.setStatus("mandatory")
_GsmBcLayer1RowStatus_Type = RowStatus
_GsmBcLayer1RowStatus_Object = MibTableColumn
gsmBcLayer1RowStatus = _GsmBcLayer1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 1, 1, 1),
    _GsmBcLayer1RowStatus_Type()
)
gsmBcLayer1RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1RowStatus.setStatus("mandatory")
_GsmBcLayer1ComponentName_Type = DisplayString
_GsmBcLayer1ComponentName_Object = MibTableColumn
gsmBcLayer1ComponentName = _GsmBcLayer1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 1, 1, 2),
    _GsmBcLayer1ComponentName_Type()
)
gsmBcLayer1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1ComponentName.setStatus("mandatory")
_GsmBcLayer1StorageType_Type = StorageType
_GsmBcLayer1StorageType_Object = MibTableColumn
gsmBcLayer1StorageType = _GsmBcLayer1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 1, 1, 4),
    _GsmBcLayer1StorageType_Type()
)
gsmBcLayer1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1StorageType.setStatus("mandatory")
_GsmBcLayer1Index_Type = NonReplicated
_GsmBcLayer1Index_Object = MibTableColumn
gsmBcLayer1Index = _GsmBcLayer1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 1, 1, 10),
    _GsmBcLayer1Index_Type()
)
gsmBcLayer1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcLayer1Index.setStatus("mandatory")
_GsmBcLayer1OperTable_Object = MibTable
gsmBcLayer1OperTable = _GsmBcLayer1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 10)
)
if mibBuilder.loadTexts:
    gsmBcLayer1OperTable.setStatus("mandatory")
_GsmBcLayer1OperEntry_Object = MibTableRow
gsmBcLayer1OperEntry = _GsmBcLayer1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 10, 1)
)
gsmBcLayer1OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcLayer1Index"),
)
if mibBuilder.loadTexts:
    gsmBcLayer1OperEntry.setStatus("mandatory")


class _GsmBcLayer1ActiveMode_Type(Integer32):
    """Custom type gsmBcLayer1ActiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aTrau", 1),
          ("v110", 0))
    )


_GsmBcLayer1ActiveMode_Type.__name__ = "Integer32"
_GsmBcLayer1ActiveMode_Object = MibTableColumn
gsmBcLayer1ActiveMode = _GsmBcLayer1ActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 10, 1, 1),
    _GsmBcLayer1ActiveMode_Type()
)
gsmBcLayer1ActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1ActiveMode.setStatus("mandatory")


class _GsmBcLayer1Connection_Type(Integer32):
    """Custom type gsmBcLayer1Connection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonTransparent", 1),
          ("transparent", 0))
    )


_GsmBcLayer1Connection_Type.__name__ = "Integer32"
_GsmBcLayer1Connection_Object = MibTableColumn
gsmBcLayer1Connection = _GsmBcLayer1Connection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 10, 1, 2),
    _GsmBcLayer1Connection_Type()
)
gsmBcLayer1Connection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1Connection.setStatus("mandatory")


class _GsmBcLayer1DataRate_Type(Unsigned32):
    """Custom type gsmBcLayer1DataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_GsmBcLayer1DataRate_Type.__name__ = "Unsigned32"
_GsmBcLayer1DataRate_Object = MibTableColumn
gsmBcLayer1DataRate = _GsmBcLayer1DataRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 10, 1, 3),
    _GsmBcLayer1DataRate_Type()
)
gsmBcLayer1DataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1DataRate.setStatus("mandatory")


class _GsmBcLayer1IntermediateRate_Type(Unsigned32):
    """Custom type gsmBcLayer1IntermediateRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
    )


_GsmBcLayer1IntermediateRate_Type.__name__ = "Unsigned32"
_GsmBcLayer1IntermediateRate_Object = MibTableColumn
gsmBcLayer1IntermediateRate = _GsmBcLayer1IntermediateRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 10, 1, 10),
    _GsmBcLayer1IntermediateRate_Type()
)
gsmBcLayer1IntermediateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1IntermediateRate.setStatus("mandatory")
_GsmBcLayer1StatsTable_Object = MibTable
gsmBcLayer1StatsTable = _GsmBcLayer1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11)
)
if mibBuilder.loadTexts:
    gsmBcLayer1StatsTable.setStatus("mandatory")
_GsmBcLayer1StatsEntry_Object = MibTableRow
gsmBcLayer1StatsEntry = _GsmBcLayer1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1)
)
gsmBcLayer1StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcLayer1Index"),
)
if mibBuilder.loadTexts:
    gsmBcLayer1StatsEntry.setStatus("mandatory")
_GsmBcLayer1FramesTx_Type = Counter32
_GsmBcLayer1FramesTx_Object = MibTableColumn
gsmBcLayer1FramesTx = _GsmBcLayer1FramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 1),
    _GsmBcLayer1FramesTx_Type()
)
gsmBcLayer1FramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1FramesTx.setStatus("mandatory")
_GsmBcLayer1FramesRx_Type = Counter32
_GsmBcLayer1FramesRx_Object = MibTableColumn
gsmBcLayer1FramesRx = _GsmBcLayer1FramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 2),
    _GsmBcLayer1FramesRx_Type()
)
gsmBcLayer1FramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1FramesRx.setStatus("mandatory")
_GsmBcLayer1BytesTx_Type = Counter32
_GsmBcLayer1BytesTx_Object = MibTableColumn
gsmBcLayer1BytesTx = _GsmBcLayer1BytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 3),
    _GsmBcLayer1BytesTx_Type()
)
gsmBcLayer1BytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1BytesTx.setStatus("mandatory")
_GsmBcLayer1BytesRx_Type = Counter32
_GsmBcLayer1BytesRx_Object = MibTableColumn
gsmBcLayer1BytesRx = _GsmBcLayer1BytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 4),
    _GsmBcLayer1BytesRx_Type()
)
gsmBcLayer1BytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1BytesRx.setStatus("mandatory")
_GsmBcLayer1UnderRunsTx_Type = Counter32
_GsmBcLayer1UnderRunsTx_Object = MibTableColumn
gsmBcLayer1UnderRunsTx = _GsmBcLayer1UnderRunsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 5),
    _GsmBcLayer1UnderRunsTx_Type()
)
gsmBcLayer1UnderRunsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1UnderRunsTx.setStatus("mandatory")
_GsmBcLayer1OverRunsRx_Type = Counter32
_GsmBcLayer1OverRunsRx_Object = MibTableColumn
gsmBcLayer1OverRunsRx = _GsmBcLayer1OverRunsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 6),
    _GsmBcLayer1OverRunsRx_Type()
)
gsmBcLayer1OverRunsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1OverRunsRx.setStatus("mandatory")
_GsmBcLayer1NonOctetErrorsRx_Type = Counter32
_GsmBcLayer1NonOctetErrorsRx_Object = MibTableColumn
gsmBcLayer1NonOctetErrorsRx = _GsmBcLayer1NonOctetErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 7),
    _GsmBcLayer1NonOctetErrorsRx_Type()
)
gsmBcLayer1NonOctetErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1NonOctetErrorsRx.setStatus("mandatory")
_GsmBcLayer1LargeFrameErrorsRx_Type = Counter32
_GsmBcLayer1LargeFrameErrorsRx_Object = MibTableColumn
gsmBcLayer1LargeFrameErrorsRx = _GsmBcLayer1LargeFrameErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 8),
    _GsmBcLayer1LargeFrameErrorsRx_Type()
)
gsmBcLayer1LargeFrameErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1LargeFrameErrorsRx.setStatus("mandatory")
_GsmBcLayer1FramesDiscarded_Type = Counter32
_GsmBcLayer1FramesDiscarded_Object = MibTableColumn
gsmBcLayer1FramesDiscarded = _GsmBcLayer1FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 9),
    _GsmBcLayer1FramesDiscarded_Type()
)
gsmBcLayer1FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1FramesDiscarded.setStatus("mandatory")
_GsmBcLayer1LrcErrorsTx_Type = Counter32
_GsmBcLayer1LrcErrorsTx_Object = MibTableColumn
gsmBcLayer1LrcErrorsTx = _GsmBcLayer1LrcErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 3, 11, 1, 10),
    _GsmBcLayer1LrcErrorsTx_Type()
)
gsmBcLayer1LrcErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLayer1LrcErrorsTx.setStatus("mandatory")
_GsmBcModem_ObjectIdentity = ObjectIdentity
gsmBcModem = _GsmBcModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4)
)
_GsmBcModemRowStatusTable_Object = MibTable
gsmBcModemRowStatusTable = _GsmBcModemRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 1)
)
if mibBuilder.loadTexts:
    gsmBcModemRowStatusTable.setStatus("mandatory")
_GsmBcModemRowStatusEntry_Object = MibTableRow
gsmBcModemRowStatusEntry = _GsmBcModemRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 1, 1)
)
gsmBcModemRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcModemIndex"),
)
if mibBuilder.loadTexts:
    gsmBcModemRowStatusEntry.setStatus("mandatory")
_GsmBcModemRowStatus_Type = RowStatus
_GsmBcModemRowStatus_Object = MibTableColumn
gsmBcModemRowStatus = _GsmBcModemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 1, 1, 1),
    _GsmBcModemRowStatus_Type()
)
gsmBcModemRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemRowStatus.setStatus("mandatory")
_GsmBcModemComponentName_Type = DisplayString
_GsmBcModemComponentName_Object = MibTableColumn
gsmBcModemComponentName = _GsmBcModemComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 1, 1, 2),
    _GsmBcModemComponentName_Type()
)
gsmBcModemComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemComponentName.setStatus("mandatory")
_GsmBcModemStorageType_Type = StorageType
_GsmBcModemStorageType_Object = MibTableColumn
gsmBcModemStorageType = _GsmBcModemStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 1, 1, 4),
    _GsmBcModemStorageType_Type()
)
gsmBcModemStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemStorageType.setStatus("mandatory")
_GsmBcModemIndex_Type = NonReplicated
_GsmBcModemIndex_Object = MibTableColumn
gsmBcModemIndex = _GsmBcModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 1, 1, 10),
    _GsmBcModemIndex_Type()
)
gsmBcModemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcModemIndex.setStatus("mandatory")
_GsmBcModemOperTable_Object = MibTable
gsmBcModemOperTable = _GsmBcModemOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10)
)
if mibBuilder.loadTexts:
    gsmBcModemOperTable.setStatus("mandatory")
_GsmBcModemOperEntry_Object = MibTableRow
gsmBcModemOperEntry = _GsmBcModemOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1)
)
gsmBcModemOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcModemIndex"),
)
if mibBuilder.loadTexts:
    gsmBcModemOperEntry.setStatus("mandatory")


class _GsmBcModemRate_Type(Integer32):
    """Custom type gsmBcModemRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("n1200", 2),
          ("n12000", 8),
          ("n120075", 3),
          ("n14400", 9),
          ("n16800", 10),
          ("n19200", 11),
          ("n21600", 12),
          ("n2400", 4),
          ("n24000", 13),
          ("n26400", 14),
          ("n28800", 15),
          ("n300", 0),
          ("n31200", 16),
          ("n32000", 17),
          ("n33600", 18),
          ("n38400", 19),
          ("n43200", 20),
          ("n4800", 5),
          ("n48000", 21),
          ("n56000", 22),
          ("n57600", 23),
          ("n600", 1),
          ("n64000", 24),
          ("n7200", 6),
          ("n9600", 7))
    )


_GsmBcModemRate_Type.__name__ = "Integer32"
_GsmBcModemRate_Object = MibTableColumn
gsmBcModemRate = _GsmBcModemRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 2),
    _GsmBcModemRate_Type()
)
gsmBcModemRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemRate.setStatus("mandatory")


class _GsmBcModemAlgorithmInUse_Type(OctetString):
    """Custom type gsmBcModemAlgorithmInUse based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GsmBcModemAlgorithmInUse_Type.__name__ = "OctetString"
_GsmBcModemAlgorithmInUse_Object = MibTableColumn
gsmBcModemAlgorithmInUse = _GsmBcModemAlgorithmInUse_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 3),
    _GsmBcModemAlgorithmInUse_Type()
)
gsmBcModemAlgorithmInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemAlgorithmInUse.setStatus("mandatory")


class _GsmBcModemProtocolState_Type(Integer32):
    """Custom type gsmBcModemProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("idle", 0),
          ("training", 1))
    )


_GsmBcModemProtocolState_Type.__name__ = "Integer32"
_GsmBcModemProtocolState_Object = MibTableColumn
gsmBcModemProtocolState = _GsmBcModemProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 4),
    _GsmBcModemProtocolState_Type()
)
gsmBcModemProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemProtocolState.setStatus("mandatory")


class _GsmBcModemReceiverTransmitter_Type(Integer32):
    """Custom type gsmBcModemReceiverTransmitter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("rxOffTxOn", 2),
          ("rxOnTxOff", 1),
          ("rxTxOn", 3))
    )


_GsmBcModemReceiverTransmitter_Type.__name__ = "Integer32"
_GsmBcModemReceiverTransmitter_Object = MibTableColumn
gsmBcModemReceiverTransmitter = _GsmBcModemReceiverTransmitter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 5),
    _GsmBcModemReceiverTransmitter_Type()
)
gsmBcModemReceiverTransmitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemReceiverTransmitter.setStatus("mandatory")


class _GsmBcModemTraining_Type(Integer32):
    """Custom type gsmBcModemTraining based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("notApplicable", 99),
          ("short", 0))
    )


_GsmBcModemTraining_Type.__name__ = "Integer32"
_GsmBcModemTraining_Object = MibTableColumn
gsmBcModemTraining = _GsmBcModemTraining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 6),
    _GsmBcModemTraining_Type()
)
gsmBcModemTraining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemTraining.setStatus("mandatory")


class _GsmBcModemToUpperFlowControlActive_Type(Integer32):
    """Custom type gsmBcModemToUpperFlowControlActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_GsmBcModemToUpperFlowControlActive_Type.__name__ = "Integer32"
_GsmBcModemToUpperFlowControlActive_Object = MibTableColumn
gsmBcModemToUpperFlowControlActive = _GsmBcModemToUpperFlowControlActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 8),
    _GsmBcModemToUpperFlowControlActive_Type()
)
gsmBcModemToUpperFlowControlActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemToUpperFlowControlActive.setStatus("mandatory")


class _GsmBcModemToDspFlowControlActive_Type(Integer32):
    """Custom type gsmBcModemToDspFlowControlActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_GsmBcModemToDspFlowControlActive_Type.__name__ = "Integer32"
_GsmBcModemToDspFlowControlActive_Object = MibTableColumn
gsmBcModemToDspFlowControlActive = _GsmBcModemToDspFlowControlActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 9),
    _GsmBcModemToDspFlowControlActive_Type()
)
gsmBcModemToDspFlowControlActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemToDspFlowControlActive.setStatus("mandatory")


class _GsmBcModemAsyncMode_Type(Integer32):
    """Custom type gsmBcModemAsyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_GsmBcModemAsyncMode_Type.__name__ = "Integer32"
_GsmBcModemAsyncMode_Object = MibTableColumn
gsmBcModemAsyncMode = _GsmBcModemAsyncMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 10),
    _GsmBcModemAsyncMode_Type()
)
gsmBcModemAsyncMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemAsyncMode.setStatus("mandatory")


class _GsmBcModemAutoHdlcMode_Type(Integer32):
    """Custom type gsmBcModemAutoHdlcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_GsmBcModemAutoHdlcMode_Type.__name__ = "Integer32"
_GsmBcModemAutoHdlcMode_Object = MibTableColumn
gsmBcModemAutoHdlcMode = _GsmBcModemAutoHdlcMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 11),
    _GsmBcModemAutoHdlcMode_Type()
)
gsmBcModemAutoHdlcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemAutoHdlcMode.setStatus("mandatory")


class _GsmBcModemOutbandFlowControl_Type(Integer32):
    """Custom type gsmBcModemOutbandFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_GsmBcModemOutbandFlowControl_Type.__name__ = "Integer32"
_GsmBcModemOutbandFlowControl_Object = MibTableColumn
gsmBcModemOutbandFlowControl = _GsmBcModemOutbandFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 12),
    _GsmBcModemOutbandFlowControl_Type()
)
gsmBcModemOutbandFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemOutbandFlowControl.setStatus("mandatory")


class _GsmBcModemOutbandBreak_Type(Integer32):
    """Custom type gsmBcModemOutbandBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_GsmBcModemOutbandBreak_Type.__name__ = "Integer32"
_GsmBcModemOutbandBreak_Object = MibTableColumn
gsmBcModemOutbandBreak = _GsmBcModemOutbandBreak_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 13),
    _GsmBcModemOutbandBreak_Type()
)
gsmBcModemOutbandBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemOutbandBreak.setStatus("mandatory")


class _GsmBcModemAutobaud_Type(Integer32):
    """Custom type gsmBcModemAutobaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_GsmBcModemAutobaud_Type.__name__ = "Integer32"
_GsmBcModemAutobaud_Object = MibTableColumn
gsmBcModemAutobaud = _GsmBcModemAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 10, 1, 14),
    _GsmBcModemAutobaud_Type()
)
gsmBcModemAutobaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemAutobaud.setStatus("mandatory")
_GsmBcModemStatsTable_Object = MibTable
gsmBcModemStatsTable = _GsmBcModemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 11)
)
if mibBuilder.loadTexts:
    gsmBcModemStatsTable.setStatus("mandatory")
_GsmBcModemStatsEntry_Object = MibTableRow
gsmBcModemStatsEntry = _GsmBcModemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 11, 1)
)
gsmBcModemStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcModemIndex"),
)
if mibBuilder.loadTexts:
    gsmBcModemStatsEntry.setStatus("mandatory")
_GsmBcModemBytesTx_Type = Counter32
_GsmBcModemBytesTx_Object = MibTableColumn
gsmBcModemBytesTx = _GsmBcModemBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 11, 1, 1),
    _GsmBcModemBytesTx_Type()
)
gsmBcModemBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemBytesTx.setStatus("mandatory")
_GsmBcModemBytesRx_Type = Counter32
_GsmBcModemBytesRx_Object = MibTableColumn
gsmBcModemBytesRx = _GsmBcModemBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 11, 1, 2),
    _GsmBcModemBytesRx_Type()
)
gsmBcModemBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemBytesRx.setStatus("mandatory")
_GsmBcModemFramingErrors_Type = Counter32
_GsmBcModemFramingErrors_Object = MibTableColumn
gsmBcModemFramingErrors = _GsmBcModemFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 4, 11, 1, 6),
    _GsmBcModemFramingErrors_Type()
)
gsmBcModemFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcModemFramingErrors.setStatus("mandatory")
_GsmBcV110_ObjectIdentity = ObjectIdentity
gsmBcV110 = _GsmBcV110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5)
)
_GsmBcV110RowStatusTable_Object = MibTable
gsmBcV110RowStatusTable = _GsmBcV110RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 1)
)
if mibBuilder.loadTexts:
    gsmBcV110RowStatusTable.setStatus("mandatory")
_GsmBcV110RowStatusEntry_Object = MibTableRow
gsmBcV110RowStatusEntry = _GsmBcV110RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 1, 1)
)
gsmBcV110RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcV110Index"),
)
if mibBuilder.loadTexts:
    gsmBcV110RowStatusEntry.setStatus("mandatory")
_GsmBcV110RowStatus_Type = RowStatus
_GsmBcV110RowStatus_Object = MibTableColumn
gsmBcV110RowStatus = _GsmBcV110RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 1, 1, 1),
    _GsmBcV110RowStatus_Type()
)
gsmBcV110RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110RowStatus.setStatus("mandatory")
_GsmBcV110ComponentName_Type = DisplayString
_GsmBcV110ComponentName_Object = MibTableColumn
gsmBcV110ComponentName = _GsmBcV110ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 1, 1, 2),
    _GsmBcV110ComponentName_Type()
)
gsmBcV110ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110ComponentName.setStatus("mandatory")
_GsmBcV110StorageType_Type = StorageType
_GsmBcV110StorageType_Object = MibTableColumn
gsmBcV110StorageType = _GsmBcV110StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 1, 1, 4),
    _GsmBcV110StorageType_Type()
)
gsmBcV110StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110StorageType.setStatus("mandatory")
_GsmBcV110Index_Type = NonReplicated
_GsmBcV110Index_Object = MibTableColumn
gsmBcV110Index = _GsmBcV110Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 1, 1, 10),
    _GsmBcV110Index_Type()
)
gsmBcV110Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcV110Index.setStatus("mandatory")
_GsmBcV110OperTable_Object = MibTable
gsmBcV110OperTable = _GsmBcV110OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 10)
)
if mibBuilder.loadTexts:
    gsmBcV110OperTable.setStatus("mandatory")
_GsmBcV110OperEntry_Object = MibTableRow
gsmBcV110OperEntry = _GsmBcV110OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 10, 1)
)
gsmBcV110OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcV110Index"),
)
if mibBuilder.loadTexts:
    gsmBcV110OperEntry.setStatus("mandatory")


class _GsmBcV110DataRate_Type(Unsigned32):
    """Custom type gsmBcV110DataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_GsmBcV110DataRate_Type.__name__ = "Unsigned32"
_GsmBcV110DataRate_Object = MibTableColumn
gsmBcV110DataRate = _GsmBcV110DataRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 10, 1, 2),
    _GsmBcV110DataRate_Type()
)
gsmBcV110DataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110DataRate.setStatus("mandatory")


class _GsmBcV110IntermediateRate_Type(Integer32):
    """Custom type gsmBcV110IntermediateRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n16KbitS", 1),
          ("n32KbitS", 2),
          ("n8KbitS", 0),
          ("notApplicable", 3))
    )


_GsmBcV110IntermediateRate_Type.__name__ = "Integer32"
_GsmBcV110IntermediateRate_Object = MibTableColumn
gsmBcV110IntermediateRate = _GsmBcV110IntermediateRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 10, 1, 9),
    _GsmBcV110IntermediateRate_Type()
)
gsmBcV110IntermediateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110IntermediateRate.setStatus("mandatory")
_GsmBcV110StatsTable_Object = MibTable
gsmBcV110StatsTable = _GsmBcV110StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11)
)
if mibBuilder.loadTexts:
    gsmBcV110StatsTable.setStatus("mandatory")
_GsmBcV110StatsEntry_Object = MibTableRow
gsmBcV110StatsEntry = _GsmBcV110StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1)
)
gsmBcV110StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcV110Index"),
)
if mibBuilder.loadTexts:
    gsmBcV110StatsEntry.setStatus("mandatory")
_GsmBcV110FramesTx_Type = Counter32
_GsmBcV110FramesTx_Object = MibTableColumn
gsmBcV110FramesTx = _GsmBcV110FramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 1),
    _GsmBcV110FramesTx_Type()
)
gsmBcV110FramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110FramesTx.setStatus("mandatory")
_GsmBcV110FramesRx_Type = Counter32
_GsmBcV110FramesRx_Object = MibTableColumn
gsmBcV110FramesRx = _GsmBcV110FramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 2),
    _GsmBcV110FramesRx_Type()
)
gsmBcV110FramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110FramesRx.setStatus("mandatory")
_GsmBcV110BytesTx_Type = Counter32
_GsmBcV110BytesTx_Object = MibTableColumn
gsmBcV110BytesTx = _GsmBcV110BytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 3),
    _GsmBcV110BytesTx_Type()
)
gsmBcV110BytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110BytesTx.setStatus("mandatory")
_GsmBcV110BytesRx_Type = Counter32
_GsmBcV110BytesRx_Object = MibTableColumn
gsmBcV110BytesRx = _GsmBcV110BytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 4),
    _GsmBcV110BytesRx_Type()
)
gsmBcV110BytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110BytesRx.setStatus("mandatory")
_GsmBcV110UnderRunsTx_Type = Counter32
_GsmBcV110UnderRunsTx_Object = MibTableColumn
gsmBcV110UnderRunsTx = _GsmBcV110UnderRunsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 5),
    _GsmBcV110UnderRunsTx_Type()
)
gsmBcV110UnderRunsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110UnderRunsTx.setStatus("mandatory")
_GsmBcV110OverRunsRx_Type = Counter32
_GsmBcV110OverRunsRx_Object = MibTableColumn
gsmBcV110OverRunsRx = _GsmBcV110OverRunsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 6),
    _GsmBcV110OverRunsRx_Type()
)
gsmBcV110OverRunsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110OverRunsRx.setStatus("mandatory")
_GsmBcV110NonOctetErrorsRx_Type = Counter32
_GsmBcV110NonOctetErrorsRx_Object = MibTableColumn
gsmBcV110NonOctetErrorsRx = _GsmBcV110NonOctetErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 7),
    _GsmBcV110NonOctetErrorsRx_Type()
)
gsmBcV110NonOctetErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110NonOctetErrorsRx.setStatus("mandatory")
_GsmBcV110LargeFrameErrorsRx_Type = Counter32
_GsmBcV110LargeFrameErrorsRx_Object = MibTableColumn
gsmBcV110LargeFrameErrorsRx = _GsmBcV110LargeFrameErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 8),
    _GsmBcV110LargeFrameErrorsRx_Type()
)
gsmBcV110LargeFrameErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110LargeFrameErrorsRx.setStatus("mandatory")
_GsmBcV110FramesDiscarded_Type = Counter32
_GsmBcV110FramesDiscarded_Object = MibTableColumn
gsmBcV110FramesDiscarded = _GsmBcV110FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 9),
    _GsmBcV110FramesDiscarded_Type()
)
gsmBcV110FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110FramesDiscarded.setStatus("mandatory")
_GsmBcV110LrcErrorsTx_Type = Counter32
_GsmBcV110LrcErrorsTx_Object = MibTableColumn
gsmBcV110LrcErrorsTx = _GsmBcV110LrcErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 5, 11, 1, 10),
    _GsmBcV110LrcErrorsTx_Type()
)
gsmBcV110LrcErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV110LrcErrorsTx.setStatus("mandatory")
_GsmBcFax_ObjectIdentity = ObjectIdentity
gsmBcFax = _GsmBcFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6)
)
_GsmBcFaxRowStatusTable_Object = MibTable
gsmBcFaxRowStatusTable = _GsmBcFaxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 1)
)
if mibBuilder.loadTexts:
    gsmBcFaxRowStatusTable.setStatus("mandatory")
_GsmBcFaxRowStatusEntry_Object = MibTableRow
gsmBcFaxRowStatusEntry = _GsmBcFaxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 1, 1)
)
gsmBcFaxRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcFaxIndex"),
)
if mibBuilder.loadTexts:
    gsmBcFaxRowStatusEntry.setStatus("mandatory")
_GsmBcFaxRowStatus_Type = RowStatus
_GsmBcFaxRowStatus_Object = MibTableColumn
gsmBcFaxRowStatus = _GsmBcFaxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 1, 1, 1),
    _GsmBcFaxRowStatus_Type()
)
gsmBcFaxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxRowStatus.setStatus("mandatory")
_GsmBcFaxComponentName_Type = DisplayString
_GsmBcFaxComponentName_Object = MibTableColumn
gsmBcFaxComponentName = _GsmBcFaxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 1, 1, 2),
    _GsmBcFaxComponentName_Type()
)
gsmBcFaxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxComponentName.setStatus("mandatory")
_GsmBcFaxStorageType_Type = StorageType
_GsmBcFaxStorageType_Object = MibTableColumn
gsmBcFaxStorageType = _GsmBcFaxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 1, 1, 4),
    _GsmBcFaxStorageType_Type()
)
gsmBcFaxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxStorageType.setStatus("mandatory")
_GsmBcFaxIndex_Type = NonReplicated
_GsmBcFaxIndex_Object = MibTableColumn
gsmBcFaxIndex = _GsmBcFaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 1, 1, 10),
    _GsmBcFaxIndex_Type()
)
gsmBcFaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcFaxIndex.setStatus("mandatory")
_GsmBcFaxOperTable_Object = MibTable
gsmBcFaxOperTable = _GsmBcFaxOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 10)
)
if mibBuilder.loadTexts:
    gsmBcFaxOperTable.setStatus("mandatory")
_GsmBcFaxOperEntry_Object = MibTableRow
gsmBcFaxOperEntry = _GsmBcFaxOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 10, 1)
)
gsmBcFaxOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcFaxIndex"),
)
if mibBuilder.loadTexts:
    gsmBcFaxOperEntry.setStatus("mandatory")


class _GsmBcFaxActiveMode_Type(Integer32):
    """Custom type gsmBcFaxActiveMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ecm", 1),
          ("normal", 0))
    )


_GsmBcFaxActiveMode_Type.__name__ = "Integer32"
_GsmBcFaxActiveMode_Object = MibTableColumn
gsmBcFaxActiveMode = _GsmBcFaxActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 10, 1, 1),
    _GsmBcFaxActiveMode_Type()
)
gsmBcFaxActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxActiveMode.setStatus("mandatory")


class _GsmBcFaxProtocolState_Type(Integer32):
    """Custom type gsmBcFaxProtocolState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bcsRx", 2),
          ("bcsTx", 3),
          ("idle", 1),
          ("msgRx", 4),
          ("msgTx", 5),
          ("setup", 0))
    )


_GsmBcFaxProtocolState_Type.__name__ = "Integer32"
_GsmBcFaxProtocolState_Object = MibTableColumn
gsmBcFaxProtocolState = _GsmBcFaxProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 10, 1, 2),
    _GsmBcFaxProtocolState_Type()
)
gsmBcFaxProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxProtocolState.setStatus("mandatory")


class _GsmBcFaxMessageRate_Type(Unsigned32):
    """Custom type gsmBcFaxMessageRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_GsmBcFaxMessageRate_Type.__name__ = "Unsigned32"
_GsmBcFaxMessageRate_Object = MibTableColumn
gsmBcFaxMessageRate = _GsmBcFaxMessageRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 10, 1, 3),
    _GsmBcFaxMessageRate_Type()
)
gsmBcFaxMessageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxMessageRate.setStatus("mandatory")
_GsmBcFaxStatsTable_Object = MibTable
gsmBcFaxStatsTable = _GsmBcFaxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11)
)
if mibBuilder.loadTexts:
    gsmBcFaxStatsTable.setStatus("mandatory")
_GsmBcFaxStatsEntry_Object = MibTableRow
gsmBcFaxStatsEntry = _GsmBcFaxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11, 1)
)
gsmBcFaxStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcFaxIndex"),
)
if mibBuilder.loadTexts:
    gsmBcFaxStatsEntry.setStatus("mandatory")
_GsmBcFaxMessageFramesRx_Type = Counter32
_GsmBcFaxMessageFramesRx_Object = MibTableColumn
gsmBcFaxMessageFramesRx = _GsmBcFaxMessageFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11, 1, 1),
    _GsmBcFaxMessageFramesRx_Type()
)
gsmBcFaxMessageFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxMessageFramesRx.setStatus("mandatory")
_GsmBcFaxMessageFramesTx_Type = Counter32
_GsmBcFaxMessageFramesTx_Object = MibTableColumn
gsmBcFaxMessageFramesTx = _GsmBcFaxMessageFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11, 1, 2),
    _GsmBcFaxMessageFramesTx_Type()
)
gsmBcFaxMessageFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxMessageFramesTx.setStatus("mandatory")
_GsmBcFaxBcsFramesRx_Type = Counter32
_GsmBcFaxBcsFramesRx_Object = MibTableColumn
gsmBcFaxBcsFramesRx = _GsmBcFaxBcsFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11, 1, 3),
    _GsmBcFaxBcsFramesRx_Type()
)
gsmBcFaxBcsFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxBcsFramesRx.setStatus("mandatory")
_GsmBcFaxBcsFramesTx_Type = Counter32
_GsmBcFaxBcsFramesTx_Object = MibTableColumn
gsmBcFaxBcsFramesTx = _GsmBcFaxBcsFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11, 1, 4),
    _GsmBcFaxBcsFramesTx_Type()
)
gsmBcFaxBcsFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxBcsFramesTx.setStatus("mandatory")
_GsmBcFaxPagesRxFromMobile_Type = Counter32
_GsmBcFaxPagesRxFromMobile_Object = MibTableColumn
gsmBcFaxPagesRxFromMobile = _GsmBcFaxPagesRxFromMobile_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11, 1, 5),
    _GsmBcFaxPagesRxFromMobile_Type()
)
gsmBcFaxPagesRxFromMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxPagesRxFromMobile.setStatus("mandatory")
_GsmBcFaxPagesTxToMobile_Type = Counter32
_GsmBcFaxPagesTxToMobile_Object = MibTableColumn
gsmBcFaxPagesTxToMobile = _GsmBcFaxPagesTxToMobile_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11, 1, 6),
    _GsmBcFaxPagesTxToMobile_Type()
)
gsmBcFaxPagesTxToMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxPagesTxToMobile.setStatus("mandatory")
_GsmBcFaxChannelModeModify_Type = Counter32
_GsmBcFaxChannelModeModify_Object = MibTableColumn
gsmBcFaxChannelModeModify = _GsmBcFaxChannelModeModify_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11, 1, 7),
    _GsmBcFaxChannelModeModify_Type()
)
gsmBcFaxChannelModeModify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxChannelModeModify.setStatus("mandatory")
_GsmBcFaxBcsFrameErrors_Type = Counter32
_GsmBcFaxBcsFrameErrors_Object = MibTableColumn
gsmBcFaxBcsFrameErrors = _GsmBcFaxBcsFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 6, 11, 1, 8),
    _GsmBcFaxBcsFrameErrors_Type()
)
gsmBcFaxBcsFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFaxBcsFrameErrors.setStatus("mandatory")
_GsmBcRlp_ObjectIdentity = ObjectIdentity
gsmBcRlp = _GsmBcRlp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7)
)
_GsmBcRlpRowStatusTable_Object = MibTable
gsmBcRlpRowStatusTable = _GsmBcRlpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 1)
)
if mibBuilder.loadTexts:
    gsmBcRlpRowStatusTable.setStatus("mandatory")
_GsmBcRlpRowStatusEntry_Object = MibTableRow
gsmBcRlpRowStatusEntry = _GsmBcRlpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 1, 1)
)
gsmBcRlpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcRlpIndex"),
)
if mibBuilder.loadTexts:
    gsmBcRlpRowStatusEntry.setStatus("mandatory")
_GsmBcRlpRowStatus_Type = RowStatus
_GsmBcRlpRowStatus_Object = MibTableColumn
gsmBcRlpRowStatus = _GsmBcRlpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 1, 1, 1),
    _GsmBcRlpRowStatus_Type()
)
gsmBcRlpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpRowStatus.setStatus("mandatory")
_GsmBcRlpComponentName_Type = DisplayString
_GsmBcRlpComponentName_Object = MibTableColumn
gsmBcRlpComponentName = _GsmBcRlpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 1, 1, 2),
    _GsmBcRlpComponentName_Type()
)
gsmBcRlpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpComponentName.setStatus("mandatory")
_GsmBcRlpStorageType_Type = StorageType
_GsmBcRlpStorageType_Object = MibTableColumn
gsmBcRlpStorageType = _GsmBcRlpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 1, 1, 4),
    _GsmBcRlpStorageType_Type()
)
gsmBcRlpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpStorageType.setStatus("mandatory")
_GsmBcRlpIndex_Type = NonReplicated
_GsmBcRlpIndex_Object = MibTableColumn
gsmBcRlpIndex = _GsmBcRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 1, 1, 10),
    _GsmBcRlpIndex_Type()
)
gsmBcRlpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcRlpIndex.setStatus("mandatory")
_GsmBcRlpOperTable_Object = MibTable
gsmBcRlpOperTable = _GsmBcRlpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10)
)
if mibBuilder.loadTexts:
    gsmBcRlpOperTable.setStatus("mandatory")
_GsmBcRlpOperEntry_Object = MibTableRow
gsmBcRlpOperEntry = _GsmBcRlpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10, 1)
)
gsmBcRlpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcRlpIndex"),
)
if mibBuilder.loadTexts:
    gsmBcRlpOperEntry.setStatus("mandatory")


class _GsmBcRlpProtocolState_Type(Integer32):
    """Custom type gsmBcRlpProtocolState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("connPending", 2),
          ("connectEstablished", 4),
          ("detached", 0),
          ("discPending", 3),
          ("disconnected", 1),
          ("synchronized", 5))
    )


_GsmBcRlpProtocolState_Type.__name__ = "Integer32"
_GsmBcRlpProtocolState_Object = MibTableColumn
gsmBcRlpProtocolState = _GsmBcRlpProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10, 1, 1),
    _GsmBcRlpProtocolState_Type()
)
gsmBcRlpProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpProtocolState.setStatus("mandatory")


class _GsmBcRlpFrameSize_Type(Unsigned32):
    """Custom type gsmBcRlpFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_GsmBcRlpFrameSize_Type.__name__ = "Unsigned32"
_GsmBcRlpFrameSize_Object = MibTableColumn
gsmBcRlpFrameSize = _GsmBcRlpFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10, 1, 2),
    _GsmBcRlpFrameSize_Type()
)
gsmBcRlpFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpFrameSize.setStatus("mandatory")


class _GsmBcRlpHighestVersion_Type(Unsigned32):
    """Custom type gsmBcRlpHighestVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GsmBcRlpHighestVersion_Type.__name__ = "Unsigned32"
_GsmBcRlpHighestVersion_Object = MibTableColumn
gsmBcRlpHighestVersion = _GsmBcRlpHighestVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10, 1, 3),
    _GsmBcRlpHighestVersion_Type()
)
gsmBcRlpHighestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpHighestVersion.setStatus("mandatory")


class _GsmBcRlpIwfToMsWindowSize_Type(Unsigned32):
    """Custom type gsmBcRlpIwfToMsWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61),
    )


_GsmBcRlpIwfToMsWindowSize_Type.__name__ = "Unsigned32"
_GsmBcRlpIwfToMsWindowSize_Object = MibTableColumn
gsmBcRlpIwfToMsWindowSize = _GsmBcRlpIwfToMsWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10, 1, 4),
    _GsmBcRlpIwfToMsWindowSize_Type()
)
gsmBcRlpIwfToMsWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpIwfToMsWindowSize.setStatus("mandatory")


class _GsmBcRlpMsToIwfWindowSize_Type(Unsigned32):
    """Custom type gsmBcRlpMsToIwfWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61),
    )


_GsmBcRlpMsToIwfWindowSize_Type.__name__ = "Unsigned32"
_GsmBcRlpMsToIwfWindowSize_Object = MibTableColumn
gsmBcRlpMsToIwfWindowSize = _GsmBcRlpMsToIwfWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10, 1, 5),
    _GsmBcRlpMsToIwfWindowSize_Type()
)
gsmBcRlpMsToIwfWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpMsToIwfWindowSize.setStatus("mandatory")


class _GsmBcRlpT1AckTimer_Type(Unsigned32):
    """Custom type gsmBcRlpT1AckTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(380, 1020),
    )


_GsmBcRlpT1AckTimer_Type.__name__ = "Unsigned32"
_GsmBcRlpT1AckTimer_Object = MibTableColumn
gsmBcRlpT1AckTimer = _GsmBcRlpT1AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10, 1, 6),
    _GsmBcRlpT1AckTimer_Type()
)
gsmBcRlpT1AckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpT1AckTimer.setStatus("mandatory")


class _GsmBcRlpT2AckDelayTimer_Type(Unsigned32):
    """Custom type gsmBcRlpT2AckDelayTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 70),
    )


_GsmBcRlpT2AckDelayTimer_Type.__name__ = "Unsigned32"
_GsmBcRlpT2AckDelayTimer_Object = MibTableColumn
gsmBcRlpT2AckDelayTimer = _GsmBcRlpT2AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10, 1, 7),
    _GsmBcRlpT2AckDelayTimer_Type()
)
gsmBcRlpT2AckDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpT2AckDelayTimer.setStatus("mandatory")


class _GsmBcRlpN2RetransmitCount_Type(Unsigned32):
    """Custom type gsmBcRlpN2RetransmitCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GsmBcRlpN2RetransmitCount_Type.__name__ = "Unsigned32"
_GsmBcRlpN2RetransmitCount_Object = MibTableColumn
gsmBcRlpN2RetransmitCount = _GsmBcRlpN2RetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 10, 1, 8),
    _GsmBcRlpN2RetransmitCount_Type()
)
gsmBcRlpN2RetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmBcRlpN2RetransmitCount.setStatus("mandatory")
_GsmBcRlpStatsTable_Object = MibTable
gsmBcRlpStatsTable = _GsmBcRlpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11)
)
if mibBuilder.loadTexts:
    gsmBcRlpStatsTable.setStatus("mandatory")
_GsmBcRlpStatsEntry_Object = MibTableRow
gsmBcRlpStatsEntry = _GsmBcRlpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1)
)
gsmBcRlpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcRlpIndex"),
)
if mibBuilder.loadTexts:
    gsmBcRlpStatsEntry.setStatus("mandatory")
_GsmBcRlpIFramesTx_Type = Counter32
_GsmBcRlpIFramesTx_Object = MibTableColumn
gsmBcRlpIFramesTx = _GsmBcRlpIFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 1),
    _GsmBcRlpIFramesTx_Type()
)
gsmBcRlpIFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpIFramesTx.setStatus("mandatory")
_GsmBcRlpIFramesRx_Type = Counter32
_GsmBcRlpIFramesRx_Object = MibTableColumn
gsmBcRlpIFramesRx = _GsmBcRlpIFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 2),
    _GsmBcRlpIFramesRx_Type()
)
gsmBcRlpIFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpIFramesRx.setStatus("mandatory")
_GsmBcRlpFramesRetransmitted_Type = Counter32
_GsmBcRlpFramesRetransmitted_Object = MibTableColumn
gsmBcRlpFramesRetransmitted = _GsmBcRlpFramesRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 3),
    _GsmBcRlpFramesRetransmitted_Type()
)
gsmBcRlpFramesRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpFramesRetransmitted.setStatus("mandatory")
_GsmBcRlpT1AckTimeouts_Type = Counter32
_GsmBcRlpT1AckTimeouts_Object = MibTableColumn
gsmBcRlpT1AckTimeouts = _GsmBcRlpT1AckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 4),
    _GsmBcRlpT1AckTimeouts_Type()
)
gsmBcRlpT1AckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpT1AckTimeouts.setStatus("mandatory")
_GsmBcRlpInvalidFrames_Type = Counter32
_GsmBcRlpInvalidFrames_Object = MibTableColumn
gsmBcRlpInvalidFrames = _GsmBcRlpInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 5),
    _GsmBcRlpInvalidFrames_Type()
)
gsmBcRlpInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpInvalidFrames.setStatus("mandatory")
_GsmBcRlpCrcErrorsRx_Type = Counter32
_GsmBcRlpCrcErrorsRx_Object = MibTableColumn
gsmBcRlpCrcErrorsRx = _GsmBcRlpCrcErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 6),
    _GsmBcRlpCrcErrorsRx_Type()
)
gsmBcRlpCrcErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpCrcErrorsRx.setStatus("mandatory")
_GsmBcRlpOutOfSequenceFrames_Type = Counter32
_GsmBcRlpOutOfSequenceFrames_Object = MibTableColumn
gsmBcRlpOutOfSequenceFrames = _GsmBcRlpOutOfSequenceFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 7),
    _GsmBcRlpOutOfSequenceFrames_Type()
)
gsmBcRlpOutOfSequenceFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpOutOfSequenceFrames.setStatus("mandatory")
_GsmBcRlpRemoteBusyIndications_Type = Counter32
_GsmBcRlpRemoteBusyIndications_Object = MibTableColumn
gsmBcRlpRemoteBusyIndications = _GsmBcRlpRemoteBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 8),
    _GsmBcRlpRemoteBusyIndications_Type()
)
gsmBcRlpRemoteBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpRemoteBusyIndications.setStatus("mandatory")
_GsmBcRlpLocalBusyIndications_Type = Counter32
_GsmBcRlpLocalBusyIndications_Object = MibTableColumn
gsmBcRlpLocalBusyIndications = _GsmBcRlpLocalBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 9),
    _GsmBcRlpLocalBusyIndications_Type()
)
gsmBcRlpLocalBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpLocalBusyIndications.setStatus("mandatory")
_GsmBcRlpIFramesTxDiscarded_Type = Counter32
_GsmBcRlpIFramesTxDiscarded_Object = MibTableColumn
gsmBcRlpIFramesTxDiscarded = _GsmBcRlpIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 10),
    _GsmBcRlpIFramesTxDiscarded_Type()
)
gsmBcRlpIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpIFramesTxDiscarded.setStatus("mandatory")
_GsmBcRlpResetsRx_Type = Counter32
_GsmBcRlpResetsRx_Object = MibTableColumn
gsmBcRlpResetsRx = _GsmBcRlpResetsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 7, 11, 1, 11),
    _GsmBcRlpResetsRx_Type()
)
gsmBcRlpResetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcRlpResetsRx.setStatus("mandatory")
_GsmBcV42_ObjectIdentity = ObjectIdentity
gsmBcV42 = _GsmBcV42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8)
)
_GsmBcV42RowStatusTable_Object = MibTable
gsmBcV42RowStatusTable = _GsmBcV42RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 1)
)
if mibBuilder.loadTexts:
    gsmBcV42RowStatusTable.setStatus("mandatory")
_GsmBcV42RowStatusEntry_Object = MibTableRow
gsmBcV42RowStatusEntry = _GsmBcV42RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 1, 1)
)
gsmBcV42RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcV42Index"),
)
if mibBuilder.loadTexts:
    gsmBcV42RowStatusEntry.setStatus("mandatory")
_GsmBcV42RowStatus_Type = RowStatus
_GsmBcV42RowStatus_Object = MibTableColumn
gsmBcV42RowStatus = _GsmBcV42RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 1, 1, 1),
    _GsmBcV42RowStatus_Type()
)
gsmBcV42RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42RowStatus.setStatus("mandatory")
_GsmBcV42ComponentName_Type = DisplayString
_GsmBcV42ComponentName_Object = MibTableColumn
gsmBcV42ComponentName = _GsmBcV42ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 1, 1, 2),
    _GsmBcV42ComponentName_Type()
)
gsmBcV42ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42ComponentName.setStatus("mandatory")
_GsmBcV42StorageType_Type = StorageType
_GsmBcV42StorageType_Object = MibTableColumn
gsmBcV42StorageType = _GsmBcV42StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 1, 1, 4),
    _GsmBcV42StorageType_Type()
)
gsmBcV42StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42StorageType.setStatus("mandatory")
_GsmBcV42Index_Type = NonReplicated
_GsmBcV42Index_Object = MibTableColumn
gsmBcV42Index = _GsmBcV42Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 1, 1, 10),
    _GsmBcV42Index_Type()
)
gsmBcV42Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcV42Index.setStatus("mandatory")
_GsmBcV42OperTable_Object = MibTable
gsmBcV42OperTable = _GsmBcV42OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 10)
)
if mibBuilder.loadTexts:
    gsmBcV42OperTable.setStatus("mandatory")
_GsmBcV42OperEntry_Object = MibTableRow
gsmBcV42OperEntry = _GsmBcV42OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 10, 1)
)
gsmBcV42OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcV42Index"),
)
if mibBuilder.loadTexts:
    gsmBcV42OperEntry.setStatus("mandatory")


class _GsmBcV42ProtocolState_Type(Integer32):
    """Custom type gsmBcV42ProtocolState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disconnectRequest", 4),
          ("disconnected", 1),
          ("frameReject", 3),
          ("informationTransfer", 5),
          ("linksetup", 2),
          ("notActive", 0),
          ("waitingAck", 6))
    )


_GsmBcV42ProtocolState_Type.__name__ = "Integer32"
_GsmBcV42ProtocolState_Object = MibTableColumn
gsmBcV42ProtocolState = _GsmBcV42ProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 10, 1, 1),
    _GsmBcV42ProtocolState_Type()
)
gsmBcV42ProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42ProtocolState.setStatus("mandatory")


class _GsmBcV42TxN401FrameSize_Type(Unsigned32):
    """Custom type gsmBcV42TxN401FrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65355),
    )


_GsmBcV42TxN401FrameSize_Type.__name__ = "Unsigned32"
_GsmBcV42TxN401FrameSize_Object = MibTableColumn
gsmBcV42TxN401FrameSize = _GsmBcV42TxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 10, 1, 2),
    _GsmBcV42TxN401FrameSize_Type()
)
gsmBcV42TxN401FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42TxN401FrameSize.setStatus("mandatory")


class _GsmBcV42RxN401FrameSize_Type(Unsigned32):
    """Custom type gsmBcV42RxN401FrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GsmBcV42RxN401FrameSize_Type.__name__ = "Unsigned32"
_GsmBcV42RxN401FrameSize_Object = MibTableColumn
gsmBcV42RxN401FrameSize = _GsmBcV42RxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 10, 1, 3),
    _GsmBcV42RxN401FrameSize_Type()
)
gsmBcV42RxN401FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42RxN401FrameSize.setStatus("mandatory")


class _GsmBcV42TxKwindowSize_Type(Unsigned32):
    """Custom type gsmBcV42TxKwindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_GsmBcV42TxKwindowSize_Type.__name__ = "Unsigned32"
_GsmBcV42TxKwindowSize_Object = MibTableColumn
gsmBcV42TxKwindowSize = _GsmBcV42TxKwindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 10, 1, 4),
    _GsmBcV42TxKwindowSize_Type()
)
gsmBcV42TxKwindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42TxKwindowSize.setStatus("mandatory")


class _GsmBcV42RxKwindowSize_Type(Unsigned32):
    """Custom type gsmBcV42RxKwindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_GsmBcV42RxKwindowSize_Type.__name__ = "Unsigned32"
_GsmBcV42RxKwindowSize_Object = MibTableColumn
gsmBcV42RxKwindowSize = _GsmBcV42RxKwindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 10, 1, 5),
    _GsmBcV42RxKwindowSize_Type()
)
gsmBcV42RxKwindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42RxKwindowSize.setStatus("mandatory")
_GsmBcV42StatsTable_Object = MibTable
gsmBcV42StatsTable = _GsmBcV42StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11)
)
if mibBuilder.loadTexts:
    gsmBcV42StatsTable.setStatus("mandatory")
_GsmBcV42StatsEntry_Object = MibTableRow
gsmBcV42StatsEntry = _GsmBcV42StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1)
)
gsmBcV42StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcV42Index"),
)
if mibBuilder.loadTexts:
    gsmBcV42StatsEntry.setStatus("mandatory")
_GsmBcV42IBytesRx_Type = Counter32
_GsmBcV42IBytesRx_Object = MibTableColumn
gsmBcV42IBytesRx = _GsmBcV42IBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 1),
    _GsmBcV42IBytesRx_Type()
)
gsmBcV42IBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42IBytesRx.setStatus("mandatory")
_GsmBcV42IBytesTx_Type = Counter32
_GsmBcV42IBytesTx_Object = MibTableColumn
gsmBcV42IBytesTx = _GsmBcV42IBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 2),
    _GsmBcV42IBytesTx_Type()
)
gsmBcV42IBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42IBytesTx.setStatus("mandatory")
_GsmBcV42IFramesRx_Type = Counter32
_GsmBcV42IFramesRx_Object = MibTableColumn
gsmBcV42IFramesRx = _GsmBcV42IFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 3),
    _GsmBcV42IFramesRx_Type()
)
gsmBcV42IFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42IFramesRx.setStatus("mandatory")
_GsmBcV42IFramesTx_Type = Counter32
_GsmBcV42IFramesTx_Object = MibTableColumn
gsmBcV42IFramesTx = _GsmBcV42IFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 4),
    _GsmBcV42IFramesTx_Type()
)
gsmBcV42IFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42IFramesTx.setStatus("mandatory")
_GsmBcV42FramesRetransmitted_Type = Counter32
_GsmBcV42FramesRetransmitted_Object = MibTableColumn
gsmBcV42FramesRetransmitted = _GsmBcV42FramesRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 5),
    _GsmBcV42FramesRetransmitted_Type()
)
gsmBcV42FramesRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42FramesRetransmitted.setStatus("mandatory")
_GsmBcV42T1AckTimeouts_Type = Counter32
_GsmBcV42T1AckTimeouts_Object = MibTableColumn
gsmBcV42T1AckTimeouts = _GsmBcV42T1AckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 6),
    _GsmBcV42T1AckTimeouts_Type()
)
gsmBcV42T1AckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42T1AckTimeouts.setStatus("mandatory")
_GsmBcV42RemoteBusyIndications_Type = Counter32
_GsmBcV42RemoteBusyIndications_Object = MibTableColumn
gsmBcV42RemoteBusyIndications = _GsmBcV42RemoteBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 7),
    _GsmBcV42RemoteBusyIndications_Type()
)
gsmBcV42RemoteBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42RemoteBusyIndications.setStatus("mandatory")
_GsmBcV42LocalBusyIndications_Type = Counter32
_GsmBcV42LocalBusyIndications_Object = MibTableColumn
gsmBcV42LocalBusyIndications = _GsmBcV42LocalBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 8),
    _GsmBcV42LocalBusyIndications_Type()
)
gsmBcV42LocalBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42LocalBusyIndications.setStatus("mandatory")
_GsmBcV42BadFramesRx_Type = Counter32
_GsmBcV42BadFramesRx_Object = MibTableColumn
gsmBcV42BadFramesRx = _GsmBcV42BadFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 9),
    _GsmBcV42BadFramesRx_Type()
)
gsmBcV42BadFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42BadFramesRx.setStatus("mandatory")
_GsmBcV42CrcErrorsRx_Type = Counter32
_GsmBcV42CrcErrorsRx_Object = MibTableColumn
gsmBcV42CrcErrorsRx = _GsmBcV42CrcErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 8, 11, 1, 10),
    _GsmBcV42CrcErrorsRx_Type()
)
gsmBcV42CrcErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42CrcErrorsRx.setStatus("mandatory")
_GsmBcV42bis_ObjectIdentity = ObjectIdentity
gsmBcV42bis = _GsmBcV42bis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9)
)
_GsmBcV42bisRowStatusTable_Object = MibTable
gsmBcV42bisRowStatusTable = _GsmBcV42bisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 1)
)
if mibBuilder.loadTexts:
    gsmBcV42bisRowStatusTable.setStatus("mandatory")
_GsmBcV42bisRowStatusEntry_Object = MibTableRow
gsmBcV42bisRowStatusEntry = _GsmBcV42bisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 1, 1)
)
gsmBcV42bisRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcV42bisIndex"),
)
if mibBuilder.loadTexts:
    gsmBcV42bisRowStatusEntry.setStatus("mandatory")
_GsmBcV42bisRowStatus_Type = RowStatus
_GsmBcV42bisRowStatus_Object = MibTableColumn
gsmBcV42bisRowStatus = _GsmBcV42bisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 1, 1, 1),
    _GsmBcV42bisRowStatus_Type()
)
gsmBcV42bisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisRowStatus.setStatus("mandatory")
_GsmBcV42bisComponentName_Type = DisplayString
_GsmBcV42bisComponentName_Object = MibTableColumn
gsmBcV42bisComponentName = _GsmBcV42bisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 1, 1, 2),
    _GsmBcV42bisComponentName_Type()
)
gsmBcV42bisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisComponentName.setStatus("mandatory")
_GsmBcV42bisStorageType_Type = StorageType
_GsmBcV42bisStorageType_Object = MibTableColumn
gsmBcV42bisStorageType = _GsmBcV42bisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 1, 1, 4),
    _GsmBcV42bisStorageType_Type()
)
gsmBcV42bisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisStorageType.setStatus("mandatory")
_GsmBcV42bisIndex_Type = NonReplicated
_GsmBcV42bisIndex_Object = MibTableColumn
gsmBcV42bisIndex = _GsmBcV42bisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 1, 1, 10),
    _GsmBcV42bisIndex_Type()
)
gsmBcV42bisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcV42bisIndex.setStatus("mandatory")
_GsmBcV42bisOperTable_Object = MibTable
gsmBcV42bisOperTable = _GsmBcV42bisOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10)
)
if mibBuilder.loadTexts:
    gsmBcV42bisOperTable.setStatus("mandatory")
_GsmBcV42bisOperEntry_Object = MibTableRow
gsmBcV42bisOperEntry = _GsmBcV42bisOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10, 1)
)
gsmBcV42bisOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcV42bisIndex"),
)
if mibBuilder.loadTexts:
    gsmBcV42bisOperEntry.setStatus("mandatory")


class _GsmBcV42bisProtocolModeEncoder_Type(Integer32):
    """Custom type gsmBcV42bisProtocolModeEncoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compressed", 1),
          ("transparent", 0))
    )


_GsmBcV42bisProtocolModeEncoder_Type.__name__ = "Integer32"
_GsmBcV42bisProtocolModeEncoder_Object = MibTableColumn
gsmBcV42bisProtocolModeEncoder = _GsmBcV42bisProtocolModeEncoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10, 1, 1),
    _GsmBcV42bisProtocolModeEncoder_Type()
)
gsmBcV42bisProtocolModeEncoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisProtocolModeEncoder.setStatus("mandatory")


class _GsmBcV42bisProtocolModeDecoder_Type(Integer32):
    """Custom type gsmBcV42bisProtocolModeDecoder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compressed", 1),
          ("transparent", 0))
    )


_GsmBcV42bisProtocolModeDecoder_Type.__name__ = "Integer32"
_GsmBcV42bisProtocolModeDecoder_Object = MibTableColumn
gsmBcV42bisProtocolModeDecoder = _GsmBcV42bisProtocolModeDecoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10, 1, 2),
    _GsmBcV42bisProtocolModeDecoder_Type()
)
gsmBcV42bisProtocolModeDecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisProtocolModeDecoder.setStatus("mandatory")


class _GsmBcV42bisCompressionDirection_Type(Integer32):
    """Custom type gsmBcV42bisCompressionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("decode", 2),
          ("encode", 1),
          ("none", 0))
    )


_GsmBcV42bisCompressionDirection_Type.__name__ = "Integer32"
_GsmBcV42bisCompressionDirection_Object = MibTableColumn
gsmBcV42bisCompressionDirection = _GsmBcV42bisCompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10, 1, 3),
    _GsmBcV42bisCompressionDirection_Type()
)
gsmBcV42bisCompressionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisCompressionDirection.setStatus("mandatory")


class _GsmBcV42bisMaximumCodewords_Type(Unsigned32):
    """Custom type gsmBcV42bisMaximumCodewords based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_GsmBcV42bisMaximumCodewords_Type.__name__ = "Unsigned32"
_GsmBcV42bisMaximumCodewords_Object = MibTableColumn
gsmBcV42bisMaximumCodewords = _GsmBcV42bisMaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10, 1, 4),
    _GsmBcV42bisMaximumCodewords_Type()
)
gsmBcV42bisMaximumCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisMaximumCodewords.setStatus("mandatory")


class _GsmBcV42bisMaximumStringSize_Type(Unsigned32):
    """Custom type gsmBcV42bisMaximumStringSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_GsmBcV42bisMaximumStringSize_Type.__name__ = "Unsigned32"
_GsmBcV42bisMaximumStringSize_Object = MibTableColumn
gsmBcV42bisMaximumStringSize = _GsmBcV42bisMaximumStringSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10, 1, 5),
    _GsmBcV42bisMaximumStringSize_Type()
)
gsmBcV42bisMaximumStringSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisMaximumStringSize.setStatus("mandatory")


class _GsmBcV42bisLastDecodeError_Type(Integer32):
    """Custom type gsmBcV42bisLastDecodeError based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("badStepup", 1),
          ("codewordEqC1", 2),
          ("emptyCodeword", 3),
          ("generalError", 5),
          ("none", 0),
          ("reservedCommand", 4))
    )


_GsmBcV42bisLastDecodeError_Type.__name__ = "Integer32"
_GsmBcV42bisLastDecodeError_Object = MibTableColumn
gsmBcV42bisLastDecodeError = _GsmBcV42bisLastDecodeError_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10, 1, 6),
    _GsmBcV42bisLastDecodeError_Type()
)
gsmBcV42bisLastDecodeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisLastDecodeError.setStatus("mandatory")


class _GsmBcV42bisCompRatioEncoder_Type(FixedPoint2):
    """Custom type gsmBcV42bisCompRatioEncoder based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_GsmBcV42bisCompRatioEncoder_Type.__name__ = "FixedPoint2"
_GsmBcV42bisCompRatioEncoder_Object = MibTableColumn
gsmBcV42bisCompRatioEncoder = _GsmBcV42bisCompRatioEncoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10, 1, 7),
    _GsmBcV42bisCompRatioEncoder_Type()
)
gsmBcV42bisCompRatioEncoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisCompRatioEncoder.setStatus("mandatory")


class _GsmBcV42bisCompRatioDecoder_Type(FixedPoint2):
    """Custom type gsmBcV42bisCompRatioDecoder based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_GsmBcV42bisCompRatioDecoder_Type.__name__ = "FixedPoint2"
_GsmBcV42bisCompRatioDecoder_Object = MibTableColumn
gsmBcV42bisCompRatioDecoder = _GsmBcV42bisCompRatioDecoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 10, 1, 8),
    _GsmBcV42bisCompRatioDecoder_Type()
)
gsmBcV42bisCompRatioDecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisCompRatioDecoder.setStatus("mandatory")
_GsmBcV42bisStatsTable_Object = MibTable
gsmBcV42bisStatsTable = _GsmBcV42bisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 11)
)
if mibBuilder.loadTexts:
    gsmBcV42bisStatsTable.setStatus("mandatory")
_GsmBcV42bisStatsEntry_Object = MibTableRow
gsmBcV42bisStatsEntry = _GsmBcV42bisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 11, 1)
)
gsmBcV42bisStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcV42bisIndex"),
)
if mibBuilder.loadTexts:
    gsmBcV42bisStatsEntry.setStatus("mandatory")
_GsmBcV42bisModeChangesEncode_Type = Counter32
_GsmBcV42bisModeChangesEncode_Object = MibTableColumn
gsmBcV42bisModeChangesEncode = _GsmBcV42bisModeChangesEncode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 11, 1, 1),
    _GsmBcV42bisModeChangesEncode_Type()
)
gsmBcV42bisModeChangesEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisModeChangesEncode.setStatus("mandatory")
_GsmBcV42bisModeChangesDecode_Type = Counter32
_GsmBcV42bisModeChangesDecode_Object = MibTableColumn
gsmBcV42bisModeChangesDecode = _GsmBcV42bisModeChangesDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 11, 1, 2),
    _GsmBcV42bisModeChangesDecode_Type()
)
gsmBcV42bisModeChangesDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisModeChangesDecode.setStatus("mandatory")
_GsmBcV42bisResetsEncode_Type = Counter32
_GsmBcV42bisResetsEncode_Object = MibTableColumn
gsmBcV42bisResetsEncode = _GsmBcV42bisResetsEncode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 11, 1, 3),
    _GsmBcV42bisResetsEncode_Type()
)
gsmBcV42bisResetsEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisResetsEncode.setStatus("mandatory")
_GsmBcV42bisResetsDecode_Type = Counter32
_GsmBcV42bisResetsDecode_Object = MibTableColumn
gsmBcV42bisResetsDecode = _GsmBcV42bisResetsDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 11, 1, 4),
    _GsmBcV42bisResetsDecode_Type()
)
gsmBcV42bisResetsDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisResetsDecode.setStatus("mandatory")
_GsmBcV42bisReInitializations_Type = Counter32
_GsmBcV42bisReInitializations_Object = MibTableColumn
gsmBcV42bisReInitializations = _GsmBcV42bisReInitializations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 11, 1, 5),
    _GsmBcV42bisReInitializations_Type()
)
gsmBcV42bisReInitializations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisReInitializations.setStatus("mandatory")
_GsmBcV42bisErrorsInDecode_Type = Counter32
_GsmBcV42bisErrorsInDecode_Object = MibTableColumn
gsmBcV42bisErrorsInDecode = _GsmBcV42bisErrorsInDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 9, 11, 1, 6),
    _GsmBcV42bisErrorsInDecode_Type()
)
gsmBcV42bisErrorsInDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcV42bisErrorsInDecode.setStatus("mandatory")
_GsmBcL2RCop_ObjectIdentity = ObjectIdentity
gsmBcL2RCop = _GsmBcL2RCop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10)
)
_GsmBcL2RCopRowStatusTable_Object = MibTable
gsmBcL2RCopRowStatusTable = _GsmBcL2RCopRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 1)
)
if mibBuilder.loadTexts:
    gsmBcL2RCopRowStatusTable.setStatus("mandatory")
_GsmBcL2RCopRowStatusEntry_Object = MibTableRow
gsmBcL2RCopRowStatusEntry = _GsmBcL2RCopRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 1, 1)
)
gsmBcL2RCopRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcL2RCopIndex"),
)
if mibBuilder.loadTexts:
    gsmBcL2RCopRowStatusEntry.setStatus("mandatory")
_GsmBcL2RCopRowStatus_Type = RowStatus
_GsmBcL2RCopRowStatus_Object = MibTableColumn
gsmBcL2RCopRowStatus = _GsmBcL2RCopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 1, 1, 1),
    _GsmBcL2RCopRowStatus_Type()
)
gsmBcL2RCopRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcL2RCopRowStatus.setStatus("mandatory")
_GsmBcL2RCopComponentName_Type = DisplayString
_GsmBcL2RCopComponentName_Object = MibTableColumn
gsmBcL2RCopComponentName = _GsmBcL2RCopComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 1, 1, 2),
    _GsmBcL2RCopComponentName_Type()
)
gsmBcL2RCopComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcL2RCopComponentName.setStatus("mandatory")
_GsmBcL2RCopStorageType_Type = StorageType
_GsmBcL2RCopStorageType_Object = MibTableColumn
gsmBcL2RCopStorageType = _GsmBcL2RCopStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 1, 1, 4),
    _GsmBcL2RCopStorageType_Type()
)
gsmBcL2RCopStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcL2RCopStorageType.setStatus("mandatory")
_GsmBcL2RCopIndex_Type = NonReplicated
_GsmBcL2RCopIndex_Object = MibTableColumn
gsmBcL2RCopIndex = _GsmBcL2RCopIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 1, 1, 10),
    _GsmBcL2RCopIndex_Type()
)
gsmBcL2RCopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcL2RCopIndex.setStatus("mandatory")
_GsmBcL2RCopOperTable_Object = MibTable
gsmBcL2RCopOperTable = _GsmBcL2RCopOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 10)
)
if mibBuilder.loadTexts:
    gsmBcL2RCopOperTable.setStatus("mandatory")
_GsmBcL2RCopOperEntry_Object = MibTableRow
gsmBcL2RCopOperEntry = _GsmBcL2RCopOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 10, 1)
)
gsmBcL2RCopOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcL2RCopIndex"),
)
if mibBuilder.loadTexts:
    gsmBcL2RCopOperEntry.setStatus("mandatory")


class _GsmBcL2RCopFlowControlStateTx_Type(Integer32):
    """Custom type gsmBcL2RCopFlowControlStateTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_GsmBcL2RCopFlowControlStateTx_Type.__name__ = "Integer32"
_GsmBcL2RCopFlowControlStateTx_Object = MibTableColumn
gsmBcL2RCopFlowControlStateTx = _GsmBcL2RCopFlowControlStateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 10, 1, 1),
    _GsmBcL2RCopFlowControlStateTx_Type()
)
gsmBcL2RCopFlowControlStateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcL2RCopFlowControlStateTx.setStatus("mandatory")


class _GsmBcL2RCopFlowControlStateRx_Type(Integer32):
    """Custom type gsmBcL2RCopFlowControlStateRx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_GsmBcL2RCopFlowControlStateRx_Type.__name__ = "Integer32"
_GsmBcL2RCopFlowControlStateRx_Object = MibTableColumn
gsmBcL2RCopFlowControlStateRx = _GsmBcL2RCopFlowControlStateRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 10, 1, 2),
    _GsmBcL2RCopFlowControlStateRx_Type()
)
gsmBcL2RCopFlowControlStateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcL2RCopFlowControlStateRx.setStatus("mandatory")
_GsmBcL2RCopStatsTable_Object = MibTable
gsmBcL2RCopStatsTable = _GsmBcL2RCopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 11)
)
if mibBuilder.loadTexts:
    gsmBcL2RCopStatsTable.setStatus("mandatory")
_GsmBcL2RCopStatsEntry_Object = MibTableRow
gsmBcL2RCopStatsEntry = _GsmBcL2RCopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 11, 1)
)
gsmBcL2RCopStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcL2RCopIndex"),
)
if mibBuilder.loadTexts:
    gsmBcL2RCopStatsEntry.setStatus("mandatory")
_GsmBcL2RCopBytesTx_Type = Counter32
_GsmBcL2RCopBytesTx_Object = MibTableColumn
gsmBcL2RCopBytesTx = _GsmBcL2RCopBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 11, 1, 1),
    _GsmBcL2RCopBytesTx_Type()
)
gsmBcL2RCopBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcL2RCopBytesTx.setStatus("mandatory")
_GsmBcL2RCopBytesRx_Type = Counter32
_GsmBcL2RCopBytesRx_Object = MibTableColumn
gsmBcL2RCopBytesRx = _GsmBcL2RCopBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 11, 1, 2),
    _GsmBcL2RCopBytesRx_Type()
)
gsmBcL2RCopBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcL2RCopBytesRx.setStatus("mandatory")
_GsmBcL2RCopBreakCountRx_Type = Counter32
_GsmBcL2RCopBreakCountRx_Object = MibTableColumn
gsmBcL2RCopBreakCountRx = _GsmBcL2RCopBreakCountRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 11, 1, 3),
    _GsmBcL2RCopBreakCountRx_Type()
)
gsmBcL2RCopBreakCountRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcL2RCopBreakCountRx.setStatus("mandatory")
_GsmBcL2RCopBreakCountTx_Type = Counter32
_GsmBcL2RCopBreakCountTx_Object = MibTableColumn
gsmBcL2RCopBreakCountTx = _GsmBcL2RCopBreakCountTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 10, 11, 1, 4),
    _GsmBcL2RCopBreakCountTx_Type()
)
gsmBcL2RCopBreakCountTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcL2RCopBreakCountTx.setStatus("mandatory")
_GsmBcUpperRelay_ObjectIdentity = ObjectIdentity
gsmBcUpperRelay = _GsmBcUpperRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11)
)
_GsmBcUpperRelayRowStatusTable_Object = MibTable
gsmBcUpperRelayRowStatusTable = _GsmBcUpperRelayRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 1)
)
if mibBuilder.loadTexts:
    gsmBcUpperRelayRowStatusTable.setStatus("mandatory")
_GsmBcUpperRelayRowStatusEntry_Object = MibTableRow
gsmBcUpperRelayRowStatusEntry = _GsmBcUpperRelayRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 1, 1)
)
gsmBcUpperRelayRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcUpperRelayIndex"),
)
if mibBuilder.loadTexts:
    gsmBcUpperRelayRowStatusEntry.setStatus("mandatory")
_GsmBcUpperRelayRowStatus_Type = RowStatus
_GsmBcUpperRelayRowStatus_Object = MibTableColumn
gsmBcUpperRelayRowStatus = _GsmBcUpperRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 1, 1, 1),
    _GsmBcUpperRelayRowStatus_Type()
)
gsmBcUpperRelayRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUpperRelayRowStatus.setStatus("mandatory")
_GsmBcUpperRelayComponentName_Type = DisplayString
_GsmBcUpperRelayComponentName_Object = MibTableColumn
gsmBcUpperRelayComponentName = _GsmBcUpperRelayComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 1, 1, 2),
    _GsmBcUpperRelayComponentName_Type()
)
gsmBcUpperRelayComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUpperRelayComponentName.setStatus("mandatory")
_GsmBcUpperRelayStorageType_Type = StorageType
_GsmBcUpperRelayStorageType_Object = MibTableColumn
gsmBcUpperRelayStorageType = _GsmBcUpperRelayStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 1, 1, 4),
    _GsmBcUpperRelayStorageType_Type()
)
gsmBcUpperRelayStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUpperRelayStorageType.setStatus("mandatory")
_GsmBcUpperRelayIndex_Type = NonReplicated
_GsmBcUpperRelayIndex_Object = MibTableColumn
gsmBcUpperRelayIndex = _GsmBcUpperRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 1, 1, 10),
    _GsmBcUpperRelayIndex_Type()
)
gsmBcUpperRelayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gsmBcUpperRelayIndex.setStatus("mandatory")
_GsmBcUpperRelayOperTable_Object = MibTable
gsmBcUpperRelayOperTable = _GsmBcUpperRelayOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 10)
)
if mibBuilder.loadTexts:
    gsmBcUpperRelayOperTable.setStatus("mandatory")
_GsmBcUpperRelayOperEntry_Object = MibTableRow
gsmBcUpperRelayOperEntry = _GsmBcUpperRelayOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 10, 1)
)
gsmBcUpperRelayOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcUpperRelayIndex"),
)
if mibBuilder.loadTexts:
    gsmBcUpperRelayOperEntry.setStatus("mandatory")


class _GsmBcUpperRelayBufferSize_Type(Unsigned32):
    """Custom type gsmBcUpperRelayBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GsmBcUpperRelayBufferSize_Type.__name__ = "Unsigned32"
_GsmBcUpperRelayBufferSize_Object = MibTableColumn
gsmBcUpperRelayBufferSize = _GsmBcUpperRelayBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 10, 1, 1),
    _GsmBcUpperRelayBufferSize_Type()
)
gsmBcUpperRelayBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUpperRelayBufferSize.setStatus("mandatory")


class _GsmBcUpperRelayFlowControlStateTx_Type(Integer32):
    """Custom type gsmBcUpperRelayFlowControlStateTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_GsmBcUpperRelayFlowControlStateTx_Type.__name__ = "Integer32"
_GsmBcUpperRelayFlowControlStateTx_Object = MibTableColumn
gsmBcUpperRelayFlowControlStateTx = _GsmBcUpperRelayFlowControlStateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 10, 1, 2),
    _GsmBcUpperRelayFlowControlStateTx_Type()
)
gsmBcUpperRelayFlowControlStateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUpperRelayFlowControlStateTx.setStatus("mandatory")


class _GsmBcUpperRelayFlowControlStateRx_Type(Integer32):
    """Custom type gsmBcUpperRelayFlowControlStateRx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_GsmBcUpperRelayFlowControlStateRx_Type.__name__ = "Integer32"
_GsmBcUpperRelayFlowControlStateRx_Object = MibTableColumn
gsmBcUpperRelayFlowControlStateRx = _GsmBcUpperRelayFlowControlStateRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 10, 1, 3),
    _GsmBcUpperRelayFlowControlStateRx_Type()
)
gsmBcUpperRelayFlowControlStateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUpperRelayFlowControlStateRx.setStatus("mandatory")
_GsmBcUpperRelayStatsTable_Object = MibTable
gsmBcUpperRelayStatsTable = _GsmBcUpperRelayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 11)
)
if mibBuilder.loadTexts:
    gsmBcUpperRelayStatsTable.setStatus("mandatory")
_GsmBcUpperRelayStatsEntry_Object = MibTableRow
gsmBcUpperRelayStatsEntry = _GsmBcUpperRelayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 11, 1)
)
gsmBcUpperRelayStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcUpperRelayIndex"),
)
if mibBuilder.loadTexts:
    gsmBcUpperRelayStatsEntry.setStatus("mandatory")
_GsmBcUpperRelayFramesTx_Type = Counter32
_GsmBcUpperRelayFramesTx_Object = MibTableColumn
gsmBcUpperRelayFramesTx = _GsmBcUpperRelayFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 11, 1, 1),
    _GsmBcUpperRelayFramesTx_Type()
)
gsmBcUpperRelayFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUpperRelayFramesTx.setStatus("mandatory")
_GsmBcUpperRelayFramesRx_Type = Counter32
_GsmBcUpperRelayFramesRx_Object = MibTableColumn
gsmBcUpperRelayFramesRx = _GsmBcUpperRelayFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 11, 1, 2),
    _GsmBcUpperRelayFramesRx_Type()
)
gsmBcUpperRelayFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUpperRelayFramesRx.setStatus("mandatory")


class _GsmBcUpperRelayUnacknowledgedFrames_Type(Gauge32):
    """Custom type gsmBcUpperRelayUnacknowledgedFrames based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GsmBcUpperRelayUnacknowledgedFrames_Type.__name__ = "Gauge32"
_GsmBcUpperRelayUnacknowledgedFrames_Object = MibTableColumn
gsmBcUpperRelayUnacknowledgedFrames = _GsmBcUpperRelayUnacknowledgedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 11, 11, 1, 3),
    _GsmBcUpperRelayUnacknowledgedFrames_Type()
)
gsmBcUpperRelayUnacknowledgedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUpperRelayUnacknowledgedFrames.setStatus("mandatory")
_GsmBcOperTable_Object = MibTable
gsmBcOperTable = _GsmBcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101)
)
if mibBuilder.loadTexts:
    gsmBcOperTable.setStatus("mandatory")
_GsmBcOperEntry_Object = MibTableRow
gsmBcOperEntry = _GsmBcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1)
)
gsmBcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
)
if mibBuilder.loadTexts:
    gsmBcOperEntry.setStatus("mandatory")


class _GsmBcMipState_Type(Integer32):
    """Custom type gsmBcMipState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("activated", 4),
          ("holdDisconnect", 5),
          ("idle", 0),
          ("pendingActivation", 3),
          ("pendingSetup", 1),
          ("setup", 2),
          ("suspended", 6))
    )


_GsmBcMipState_Type.__name__ = "Integer32"
_GsmBcMipState_Object = MibTableColumn
gsmBcMipState = _GsmBcMipState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 1),
    _GsmBcMipState_Type()
)
gsmBcMipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcMipState.setStatus("mandatory")


class _GsmBcMaxUserDataRate_Type(Integer32):
    """Custom type gsmBcMaxUserDataRate based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("n1200", 2),
          ("n12000", 8),
          ("n120075", 3),
          ("n14400", 9),
          ("n16800", 10),
          ("n19200", 11),
          ("n21600", 12),
          ("n2400", 4),
          ("n24000", 13),
          ("n26400", 14),
          ("n28800", 15),
          ("n300", 0),
          ("n31200", 16),
          ("n32000", 17),
          ("n33600", 18),
          ("n38400", 19),
          ("n43200", 20),
          ("n4800", 5),
          ("n48000", 21),
          ("n56000", 22),
          ("n57600", 23),
          ("n600", 1),
          ("n64000", 24),
          ("n7200", 6),
          ("n9600", 7),
          ("none", 25))
    )


_GsmBcMaxUserDataRate_Type.__name__ = "Integer32"
_GsmBcMaxUserDataRate_Object = MibTableColumn
gsmBcMaxUserDataRate = _GsmBcMaxUserDataRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 2),
    _GsmBcMaxUserDataRate_Type()
)
gsmBcMaxUserDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcMaxUserDataRate.setStatus("mandatory")


class _GsmBcConnectionType_Type(Integer32):
    """Custom type gsmBcConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("synchronous", 0))
    )


_GsmBcConnectionType_Type.__name__ = "Integer32"
_GsmBcConnectionType_Object = MibTableColumn
gsmBcConnectionType = _GsmBcConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 3),
    _GsmBcConnectionType_Type()
)
gsmBcConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcConnectionType.setStatus("mandatory")


class _GsmBcDataBits_Type(Integer32):
    """Custom type gsmBcDataBits based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("n7", 0),
          ("n8", 1),
          ("notApplicable", 99))
    )


_GsmBcDataBits_Type.__name__ = "Integer32"
_GsmBcDataBits_Object = MibTableColumn
gsmBcDataBits = _GsmBcDataBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 4),
    _GsmBcDataBits_Type()
)
gsmBcDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcDataBits.setStatus("mandatory")


class _GsmBcStopBits_Type(Integer32):
    """Custom type gsmBcStopBits based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("n1", 0),
          ("n2", 1),
          ("notApplicable", 99))
    )


_GsmBcStopBits_Type.__name__ = "Integer32"
_GsmBcStopBits_Object = MibTableColumn
gsmBcStopBits = _GsmBcStopBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 5),
    _GsmBcStopBits_Type()
)
gsmBcStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcStopBits.setStatus("mandatory")


class _GsmBcParity_Type(Integer32):
    """Custom type gsmBcParity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("forced0", 3),
          ("forced1", 4),
          ("none", 0),
          ("notApplicable", 99),
          ("odd", 1))
    )


_GsmBcParity_Type.__name__ = "Integer32"
_GsmBcParity_Object = MibTableColumn
gsmBcParity = _GsmBcParity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 6),
    _GsmBcParity_Type()
)
gsmBcParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcParity.setStatus("mandatory")


class _GsmBcFlowControl_Type(Integer32):
    """Custom type gsmBcFlowControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("errorCntrl", 3),
          ("inband", 1),
          ("noFlowControlActive", 0),
          ("v110FlowCntrl", 2))
    )


_GsmBcFlowControl_Type.__name__ = "Integer32"
_GsmBcFlowControl_Object = MibTableColumn
gsmBcFlowControl = _GsmBcFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 7),
    _GsmBcFlowControl_Type()
)
gsmBcFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcFlowControl.setStatus("mandatory")


class _GsmBcCallType_Type(Integer32):
    """Custom type gsmBcCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cda31khz", 1),
          ("cdaUdi", 2),
          ("cds31khz", 4),
          ("cdsUdi", 3),
          ("faxG3", 0))
    )


_GsmBcCallType_Type.__name__ = "Integer32"
_GsmBcCallType_Object = MibTableColumn
gsmBcCallType = _GsmBcCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 8),
    _GsmBcCallType_Type()
)
gsmBcCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcCallType.setStatus("mandatory")


class _GsmBcLastResponseCode_Type(Integer32):
    """Custom type gsmBcLastResponseCode based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              99)
        )
    )
    namedValues = NamedValues(
        *(("applicationError", 2),
          ("bufferNotFlushed", 9),
          ("invalidMessage", 8),
          ("msgSizeMismatch", 4),
          ("noResources", 3),
          ("notApplicable", 99),
          ("protocolViolation", 5),
          ("requestDenied", 7),
          ("requestDone", 0),
          ("requestNotSupported", 6),
          ("systemError", 1))
    )


_GsmBcLastResponseCode_Type.__name__ = "Integer32"
_GsmBcLastResponseCode_Object = MibTableColumn
gsmBcLastResponseCode = _GsmBcLastResponseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 9),
    _GsmBcLastResponseCode_Type()
)
gsmBcLastResponseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcLastResponseCode.setStatus("mandatory")
_GsmBcMateBearerChannel_Type = RowPointer
_GsmBcMateBearerChannel_Object = MibTableColumn
gsmBcMateBearerChannel = _GsmBcMateBearerChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 101, 1, 10),
    _GsmBcMateBearerChannel_Type()
)
gsmBcMateBearerChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcMateBearerChannel.setStatus("mandatory")
_GsmBcCidDataTable_Object = MibTable
gsmBcCidDataTable = _GsmBcCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 104)
)
if mibBuilder.loadTexts:
    gsmBcCidDataTable.setStatus("mandatory")
_GsmBcCidDataEntry_Object = MibTableRow
gsmBcCidDataEntry = _GsmBcCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 104, 1)
)
gsmBcCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
)
if mibBuilder.loadTexts:
    gsmBcCidDataEntry.setStatus("mandatory")


class _GsmBcCustomerIdentifier_Type(Unsigned32):
    """Custom type gsmBcCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_GsmBcCustomerIdentifier_Type.__name__ = "Unsigned32"
_GsmBcCustomerIdentifier_Object = MibTableColumn
gsmBcCustomerIdentifier = _GsmBcCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 104, 1, 1),
    _GsmBcCustomerIdentifier_Type()
)
gsmBcCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmBcCustomerIdentifier.setStatus("mandatory")
_GsmBcStateTable_Object = MibTable
gsmBcStateTable = _GsmBcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 105)
)
if mibBuilder.loadTexts:
    gsmBcStateTable.setStatus("mandatory")
_GsmBcStateEntry_Object = MibTableRow
gsmBcStateEntry = _GsmBcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 105, 1)
)
gsmBcStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcTrunkGrpIndex"),
    (0, "Nortel-Magellan-Passport-GsmIwfMIB", "gsmBcCicIndex"),
)
if mibBuilder.loadTexts:
    gsmBcStateEntry.setStatus("mandatory")


class _GsmBcAdminState_Type(Integer32):
    """Custom type gsmBcAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_GsmBcAdminState_Type.__name__ = "Integer32"
_GsmBcAdminState_Object = MibTableColumn
gsmBcAdminState = _GsmBcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 105, 1, 1),
    _GsmBcAdminState_Type()
)
gsmBcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcAdminState.setStatus("mandatory")


class _GsmBcOperationalState_Type(Integer32):
    """Custom type gsmBcOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GsmBcOperationalState_Type.__name__ = "Integer32"
_GsmBcOperationalState_Object = MibTableColumn
gsmBcOperationalState = _GsmBcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 105, 1, 2),
    _GsmBcOperationalState_Type()
)
gsmBcOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcOperationalState.setStatus("mandatory")


class _GsmBcUsageState_Type(Integer32):
    """Custom type gsmBcUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_GsmBcUsageState_Type.__name__ = "Integer32"
_GsmBcUsageState_Object = MibTableColumn
gsmBcUsageState = _GsmBcUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 128, 105, 1, 3),
    _GsmBcUsageState_Type()
)
gsmBcUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmBcUsageState.setStatus("mandatory")
_GsmIwfMIB_ObjectIdentity = ObjectIdentity
gsmIwfMIB = _GsmIwfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 129)
)
_GsmIwfGroup_ObjectIdentity = ObjectIdentity
gsmIwfGroup = _GsmIwfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 129, 1)
)
_GsmIwfGroupBE_ObjectIdentity = ObjectIdentity
gsmIwfGroupBE = _GsmIwfGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 129, 1, 5)
)
_GsmIwfGroupBE01_ObjectIdentity = ObjectIdentity
gsmIwfGroupBE01 = _GsmIwfGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 129, 1, 5, 2)
)
_GsmIwfGroupBE01A_ObjectIdentity = ObjectIdentity
gsmIwfGroupBE01A = _GsmIwfGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 129, 1, 5, 2, 2)
)
_GsmIwfCapabilities_ObjectIdentity = ObjectIdentity
gsmIwfCapabilities = _GsmIwfCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 129, 3)
)
_GsmIwfCapabilitiesBE_ObjectIdentity = ObjectIdentity
gsmIwfCapabilitiesBE = _GsmIwfCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 129, 3, 5)
)
_GsmIwfCapabilitiesBE01_ObjectIdentity = ObjectIdentity
gsmIwfCapabilitiesBE01 = _GsmIwfCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 129, 3, 5, 2)
)
_GsmIwfCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
gsmIwfCapabilitiesBE01A = _GsmIwfCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 129, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-GsmIwfMIB",
    **{"gsmCs": gsmCs,
       "gsmCsRowStatusTable": gsmCsRowStatusTable,
       "gsmCsRowStatusEntry": gsmCsRowStatusEntry,
       "gsmCsRowStatus": gsmCsRowStatus,
       "gsmCsComponentName": gsmCsComponentName,
       "gsmCsStorageType": gsmCsStorageType,
       "gsmCsTrunkGrpIndex": gsmCsTrunkGrpIndex,
       "gsmCsModem": gsmCsModem,
       "gsmCsModemRowStatusTable": gsmCsModemRowStatusTable,
       "gsmCsModemRowStatusEntry": gsmCsModemRowStatusEntry,
       "gsmCsModemRowStatus": gsmCsModemRowStatus,
       "gsmCsModemComponentName": gsmCsModemComponentName,
       "gsmCsModemStorageType": gsmCsModemStorageType,
       "gsmCsModemIndex": gsmCsModemIndex,
       "gsmCsRlp": gsmCsRlp,
       "gsmCsRlpRowStatusTable": gsmCsRlpRowStatusTable,
       "gsmCsRlpRowStatusEntry": gsmCsRlpRowStatusEntry,
       "gsmCsRlpRowStatus": gsmCsRlpRowStatus,
       "gsmCsRlpComponentName": gsmCsRlpComponentName,
       "gsmCsRlpStorageType": gsmCsRlpStorageType,
       "gsmCsRlpIndex": gsmCsRlpIndex,
       "gsmCsRlpProvTable": gsmCsRlpProvTable,
       "gsmCsRlpProvEntry": gsmCsRlpProvEntry,
       "gsmCsRlpHighestVersion": gsmCsRlpHighestVersion,
       "gsmCsRlpIwfToMsWindowSize": gsmCsRlpIwfToMsWindowSize,
       "gsmCsRlpMsToIwfWindowSize": gsmCsRlpMsToIwfWindowSize,
       "gsmCsRlpT1AckTimer": gsmCsRlpT1AckTimer,
       "gsmCsRlpT2AckDelayTimer": gsmCsRlpT2AckDelayTimer,
       "gsmCsRlpN2RetransmitCount": gsmCsRlpN2RetransmitCount,
       "gsmCsFax": gsmCsFax,
       "gsmCsFaxRowStatusTable": gsmCsFaxRowStatusTable,
       "gsmCsFaxRowStatusEntry": gsmCsFaxRowStatusEntry,
       "gsmCsFaxRowStatus": gsmCsFaxRowStatus,
       "gsmCsFaxComponentName": gsmCsFaxComponentName,
       "gsmCsFaxStorageType": gsmCsFaxStorageType,
       "gsmCsFaxIndex": gsmCsFaxIndex,
       "gsmCsFaxProvTable": gsmCsFaxProvTable,
       "gsmCsFaxProvEntry": gsmCsFaxProvEntry,
       "gsmCsFaxT1CalledToneTimer": gsmCsFaxT1CalledToneTimer,
       "gsmCsV42": gsmCsV42,
       "gsmCsV42RowStatusTable": gsmCsV42RowStatusTable,
       "gsmCsV42RowStatusEntry": gsmCsV42RowStatusEntry,
       "gsmCsV42RowStatus": gsmCsV42RowStatus,
       "gsmCsV42ComponentName": gsmCsV42ComponentName,
       "gsmCsV42StorageType": gsmCsV42StorageType,
       "gsmCsV42Index": gsmCsV42Index,
       "gsmCsV42ProvTable": gsmCsV42ProvTable,
       "gsmCsV42ProvEntry": gsmCsV42ProvEntry,
       "gsmCsV42T400DetectTimer": gsmCsV42T400DetectTimer,
       "gsmCsV42T401AckTimer": gsmCsV42T401AckTimer,
       "gsmCsV42T402AckDelayTimer": gsmCsV42T402AckDelayTimer,
       "gsmCsV42T403IdleProbeTimer": gsmCsV42T403IdleProbeTimer,
       "gsmCsV42TxN401FrameSize": gsmCsV42TxN401FrameSize,
       "gsmCsV42RxN401FrameSize": gsmCsV42RxN401FrameSize,
       "gsmCsV42TxKwindowSize": gsmCsV42TxKwindowSize,
       "gsmCsV42RxKwindowSize": gsmCsV42RxKwindowSize,
       "gsmCsV42N400RetransLimit": gsmCsV42N400RetransLimit,
       "gsmCsV42bis": gsmCsV42bis,
       "gsmCsV42bisRowStatusTable": gsmCsV42bisRowStatusTable,
       "gsmCsV42bisRowStatusEntry": gsmCsV42bisRowStatusEntry,
       "gsmCsV42bisRowStatus": gsmCsV42bisRowStatus,
       "gsmCsV42bisComponentName": gsmCsV42bisComponentName,
       "gsmCsV42bisStorageType": gsmCsV42bisStorageType,
       "gsmCsV42bisIndex": gsmCsV42bisIndex,
       "gsmCsV42bisProvTable": gsmCsV42bisProvTable,
       "gsmCsV42bisProvEntry": gsmCsV42bisProvEntry,
       "gsmCsV42bisCompressionDirection": gsmCsV42bisCompressionDirection,
       "gsmCsV42bisMaximumCodewords": gsmCsV42bisMaximumCodewords,
       "gsmCsV42bisMaximumStringSize": gsmCsV42bisMaximumStringSize,
       "gsmCsV42bisActionOnError": gsmCsV42bisActionOnError,
       "gsmCsLp": gsmCsLp,
       "gsmCsLpRowStatusTable": gsmCsLpRowStatusTable,
       "gsmCsLpRowStatusEntry": gsmCsLpRowStatusEntry,
       "gsmCsLpRowStatus": gsmCsLpRowStatus,
       "gsmCsLpComponentName": gsmCsLpComponentName,
       "gsmCsLpStorageType": gsmCsLpStorageType,
       "gsmCsLpIndex": gsmCsLpIndex,
       "gsmCsLpOperTable": gsmCsLpOperTable,
       "gsmCsLpOperEntry": gsmCsLpOperEntry,
       "gsmCsLpConfiguredBearerChannels": gsmCsLpConfiguredBearerChannels,
       "gsmCsLpActiveCalls": gsmCsLpActiveCalls,
       "gsmCsLpAssignedCapacity": gsmCsLpAssignedCapacity,
       "gsmCsLpModemsSupported": gsmCsLpModemsSupported,
       "gsmCsProvTable": gsmCsProvTable,
       "gsmCsProvEntry": gsmCsProvEntry,
       "gsmCsCommentText": gsmCsCommentText,
       "gsmCsMscIpAddress": gsmCsMscIpAddress,
       "gsmCsVirtualRouterName": gsmCsVirtualRouterName,
       "gsmCsVoiceLaw": gsmCsVoiceLaw,
       "gsmCsCidDataTable": gsmCsCidDataTable,
       "gsmCsCidDataEntry": gsmCsCidDataEntry,
       "gsmCsCustomerIdentifier": gsmCsCustomerIdentifier,
       "gsmCsStateTable": gsmCsStateTable,
       "gsmCsStateEntry": gsmCsStateEntry,
       "gsmCsAdminState": gsmCsAdminState,
       "gsmCsOperationalState": gsmCsOperationalState,
       "gsmCsUsageState": gsmCsUsageState,
       "gsmCsStatsTable": gsmCsStatsTable,
       "gsmCsStatsEntry": gsmCsStatsEntry,
       "gsmCsCurrentCalls": gsmCsCurrentCalls,
       "gsmCsCallsRequested": gsmCsCallsRequested,
       "gsmCsCallsSetup": gsmCsCallsSetup,
       "gsmCsCallsActivated": gsmCsCallsActivated,
       "gsmCsCallsReleasedNormal": gsmCsCallsReleasedNormal,
       "gsmCsCallsReleasedAbnormal": gsmCsCallsReleasedAbnormal,
       "gsmCsChannelConfigChanges": gsmCsChannelConfigChanges,
       "gsmCsChannelModeModifyRequests": gsmCsChannelModeModifyRequests,
       "gsmCsStatusMessagesRx": gsmCsStatusMessagesRx,
       "gsmCsErroredMipFrames": gsmCsErroredMipFrames,
       "gsmBc": gsmBc,
       "gsmBcRowStatusTable": gsmBcRowStatusTable,
       "gsmBcRowStatusEntry": gsmBcRowStatusEntry,
       "gsmBcRowStatus": gsmBcRowStatus,
       "gsmBcComponentName": gsmBcComponentName,
       "gsmBcStorageType": gsmBcStorageType,
       "gsmBcTrunkGrpIndex": gsmBcTrunkGrpIndex,
       "gsmBcCicIndex": gsmBcCicIndex,
       "gsmBcFramer": gsmBcFramer,
       "gsmBcFramerRowStatusTable": gsmBcFramerRowStatusTable,
       "gsmBcFramerRowStatusEntry": gsmBcFramerRowStatusEntry,
       "gsmBcFramerRowStatus": gsmBcFramerRowStatus,
       "gsmBcFramerComponentName": gsmBcFramerComponentName,
       "gsmBcFramerStorageType": gsmBcFramerStorageType,
       "gsmBcFramerIndex": gsmBcFramerIndex,
       "gsmBcFramerProvTable": gsmBcFramerProvTable,
       "gsmBcFramerProvEntry": gsmBcFramerProvEntry,
       "gsmBcFramerInterfaceName": gsmBcFramerInterfaceName,
       "gsmBcFramerStatsTable": gsmBcFramerStatsTable,
       "gsmBcFramerStatsEntry": gsmBcFramerStatsEntry,
       "gsmBcFramerFrmToIf": gsmBcFramerFrmToIf,
       "gsmBcFramerFrmFromIf": gsmBcFramerFrmFromIf,
       "gsmBcFramerOctetFromIf": gsmBcFramerOctetFromIf,
       "gsmBcFramerCrcErrors": gsmBcFramerCrcErrors,
       "gsmBcFramerLrcErrors": gsmBcFramerLrcErrors,
       "gsmBcFramerNonOctetErrors": gsmBcFramerNonOctetErrors,
       "gsmBcFramerOverruns": gsmBcFramerOverruns,
       "gsmBcFramerUnderruns": gsmBcFramerUnderruns,
       "gsmBcFramerLinkTable": gsmBcFramerLinkTable,
       "gsmBcFramerLinkEntry": gsmBcFramerLinkEntry,
       "gsmBcFramerFramingType": gsmBcFramerFramingType,
       "gsmBcFramerStateTable": gsmBcFramerStateTable,
       "gsmBcFramerStateEntry": gsmBcFramerStateEntry,
       "gsmBcFramerAdminState": gsmBcFramerAdminState,
       "gsmBcFramerOperationalState": gsmBcFramerOperationalState,
       "gsmBcFramerUsageState": gsmBcFramerUsageState,
       "gsmBcLayer1": gsmBcLayer1,
       "gsmBcLayer1RowStatusTable": gsmBcLayer1RowStatusTable,
       "gsmBcLayer1RowStatusEntry": gsmBcLayer1RowStatusEntry,
       "gsmBcLayer1RowStatus": gsmBcLayer1RowStatus,
       "gsmBcLayer1ComponentName": gsmBcLayer1ComponentName,
       "gsmBcLayer1StorageType": gsmBcLayer1StorageType,
       "gsmBcLayer1Index": gsmBcLayer1Index,
       "gsmBcLayer1OperTable": gsmBcLayer1OperTable,
       "gsmBcLayer1OperEntry": gsmBcLayer1OperEntry,
       "gsmBcLayer1ActiveMode": gsmBcLayer1ActiveMode,
       "gsmBcLayer1Connection": gsmBcLayer1Connection,
       "gsmBcLayer1DataRate": gsmBcLayer1DataRate,
       "gsmBcLayer1IntermediateRate": gsmBcLayer1IntermediateRate,
       "gsmBcLayer1StatsTable": gsmBcLayer1StatsTable,
       "gsmBcLayer1StatsEntry": gsmBcLayer1StatsEntry,
       "gsmBcLayer1FramesTx": gsmBcLayer1FramesTx,
       "gsmBcLayer1FramesRx": gsmBcLayer1FramesRx,
       "gsmBcLayer1BytesTx": gsmBcLayer1BytesTx,
       "gsmBcLayer1BytesRx": gsmBcLayer1BytesRx,
       "gsmBcLayer1UnderRunsTx": gsmBcLayer1UnderRunsTx,
       "gsmBcLayer1OverRunsRx": gsmBcLayer1OverRunsRx,
       "gsmBcLayer1NonOctetErrorsRx": gsmBcLayer1NonOctetErrorsRx,
       "gsmBcLayer1LargeFrameErrorsRx": gsmBcLayer1LargeFrameErrorsRx,
       "gsmBcLayer1FramesDiscarded": gsmBcLayer1FramesDiscarded,
       "gsmBcLayer1LrcErrorsTx": gsmBcLayer1LrcErrorsTx,
       "gsmBcModem": gsmBcModem,
       "gsmBcModemRowStatusTable": gsmBcModemRowStatusTable,
       "gsmBcModemRowStatusEntry": gsmBcModemRowStatusEntry,
       "gsmBcModemRowStatus": gsmBcModemRowStatus,
       "gsmBcModemComponentName": gsmBcModemComponentName,
       "gsmBcModemStorageType": gsmBcModemStorageType,
       "gsmBcModemIndex": gsmBcModemIndex,
       "gsmBcModemOperTable": gsmBcModemOperTable,
       "gsmBcModemOperEntry": gsmBcModemOperEntry,
       "gsmBcModemRate": gsmBcModemRate,
       "gsmBcModemAlgorithmInUse": gsmBcModemAlgorithmInUse,
       "gsmBcModemProtocolState": gsmBcModemProtocolState,
       "gsmBcModemReceiverTransmitter": gsmBcModemReceiverTransmitter,
       "gsmBcModemTraining": gsmBcModemTraining,
       "gsmBcModemToUpperFlowControlActive": gsmBcModemToUpperFlowControlActive,
       "gsmBcModemToDspFlowControlActive": gsmBcModemToDspFlowControlActive,
       "gsmBcModemAsyncMode": gsmBcModemAsyncMode,
       "gsmBcModemAutoHdlcMode": gsmBcModemAutoHdlcMode,
       "gsmBcModemOutbandFlowControl": gsmBcModemOutbandFlowControl,
       "gsmBcModemOutbandBreak": gsmBcModemOutbandBreak,
       "gsmBcModemAutobaud": gsmBcModemAutobaud,
       "gsmBcModemStatsTable": gsmBcModemStatsTable,
       "gsmBcModemStatsEntry": gsmBcModemStatsEntry,
       "gsmBcModemBytesTx": gsmBcModemBytesTx,
       "gsmBcModemBytesRx": gsmBcModemBytesRx,
       "gsmBcModemFramingErrors": gsmBcModemFramingErrors,
       "gsmBcV110": gsmBcV110,
       "gsmBcV110RowStatusTable": gsmBcV110RowStatusTable,
       "gsmBcV110RowStatusEntry": gsmBcV110RowStatusEntry,
       "gsmBcV110RowStatus": gsmBcV110RowStatus,
       "gsmBcV110ComponentName": gsmBcV110ComponentName,
       "gsmBcV110StorageType": gsmBcV110StorageType,
       "gsmBcV110Index": gsmBcV110Index,
       "gsmBcV110OperTable": gsmBcV110OperTable,
       "gsmBcV110OperEntry": gsmBcV110OperEntry,
       "gsmBcV110DataRate": gsmBcV110DataRate,
       "gsmBcV110IntermediateRate": gsmBcV110IntermediateRate,
       "gsmBcV110StatsTable": gsmBcV110StatsTable,
       "gsmBcV110StatsEntry": gsmBcV110StatsEntry,
       "gsmBcV110FramesTx": gsmBcV110FramesTx,
       "gsmBcV110FramesRx": gsmBcV110FramesRx,
       "gsmBcV110BytesTx": gsmBcV110BytesTx,
       "gsmBcV110BytesRx": gsmBcV110BytesRx,
       "gsmBcV110UnderRunsTx": gsmBcV110UnderRunsTx,
       "gsmBcV110OverRunsRx": gsmBcV110OverRunsRx,
       "gsmBcV110NonOctetErrorsRx": gsmBcV110NonOctetErrorsRx,
       "gsmBcV110LargeFrameErrorsRx": gsmBcV110LargeFrameErrorsRx,
       "gsmBcV110FramesDiscarded": gsmBcV110FramesDiscarded,
       "gsmBcV110LrcErrorsTx": gsmBcV110LrcErrorsTx,
       "gsmBcFax": gsmBcFax,
       "gsmBcFaxRowStatusTable": gsmBcFaxRowStatusTable,
       "gsmBcFaxRowStatusEntry": gsmBcFaxRowStatusEntry,
       "gsmBcFaxRowStatus": gsmBcFaxRowStatus,
       "gsmBcFaxComponentName": gsmBcFaxComponentName,
       "gsmBcFaxStorageType": gsmBcFaxStorageType,
       "gsmBcFaxIndex": gsmBcFaxIndex,
       "gsmBcFaxOperTable": gsmBcFaxOperTable,
       "gsmBcFaxOperEntry": gsmBcFaxOperEntry,
       "gsmBcFaxActiveMode": gsmBcFaxActiveMode,
       "gsmBcFaxProtocolState": gsmBcFaxProtocolState,
       "gsmBcFaxMessageRate": gsmBcFaxMessageRate,
       "gsmBcFaxStatsTable": gsmBcFaxStatsTable,
       "gsmBcFaxStatsEntry": gsmBcFaxStatsEntry,
       "gsmBcFaxMessageFramesRx": gsmBcFaxMessageFramesRx,
       "gsmBcFaxMessageFramesTx": gsmBcFaxMessageFramesTx,
       "gsmBcFaxBcsFramesRx": gsmBcFaxBcsFramesRx,
       "gsmBcFaxBcsFramesTx": gsmBcFaxBcsFramesTx,
       "gsmBcFaxPagesRxFromMobile": gsmBcFaxPagesRxFromMobile,
       "gsmBcFaxPagesTxToMobile": gsmBcFaxPagesTxToMobile,
       "gsmBcFaxChannelModeModify": gsmBcFaxChannelModeModify,
       "gsmBcFaxBcsFrameErrors": gsmBcFaxBcsFrameErrors,
       "gsmBcRlp": gsmBcRlp,
       "gsmBcRlpRowStatusTable": gsmBcRlpRowStatusTable,
       "gsmBcRlpRowStatusEntry": gsmBcRlpRowStatusEntry,
       "gsmBcRlpRowStatus": gsmBcRlpRowStatus,
       "gsmBcRlpComponentName": gsmBcRlpComponentName,
       "gsmBcRlpStorageType": gsmBcRlpStorageType,
       "gsmBcRlpIndex": gsmBcRlpIndex,
       "gsmBcRlpOperTable": gsmBcRlpOperTable,
       "gsmBcRlpOperEntry": gsmBcRlpOperEntry,
       "gsmBcRlpProtocolState": gsmBcRlpProtocolState,
       "gsmBcRlpFrameSize": gsmBcRlpFrameSize,
       "gsmBcRlpHighestVersion": gsmBcRlpHighestVersion,
       "gsmBcRlpIwfToMsWindowSize": gsmBcRlpIwfToMsWindowSize,
       "gsmBcRlpMsToIwfWindowSize": gsmBcRlpMsToIwfWindowSize,
       "gsmBcRlpT1AckTimer": gsmBcRlpT1AckTimer,
       "gsmBcRlpT2AckDelayTimer": gsmBcRlpT2AckDelayTimer,
       "gsmBcRlpN2RetransmitCount": gsmBcRlpN2RetransmitCount,
       "gsmBcRlpStatsTable": gsmBcRlpStatsTable,
       "gsmBcRlpStatsEntry": gsmBcRlpStatsEntry,
       "gsmBcRlpIFramesTx": gsmBcRlpIFramesTx,
       "gsmBcRlpIFramesRx": gsmBcRlpIFramesRx,
       "gsmBcRlpFramesRetransmitted": gsmBcRlpFramesRetransmitted,
       "gsmBcRlpT1AckTimeouts": gsmBcRlpT1AckTimeouts,
       "gsmBcRlpInvalidFrames": gsmBcRlpInvalidFrames,
       "gsmBcRlpCrcErrorsRx": gsmBcRlpCrcErrorsRx,
       "gsmBcRlpOutOfSequenceFrames": gsmBcRlpOutOfSequenceFrames,
       "gsmBcRlpRemoteBusyIndications": gsmBcRlpRemoteBusyIndications,
       "gsmBcRlpLocalBusyIndications": gsmBcRlpLocalBusyIndications,
       "gsmBcRlpIFramesTxDiscarded": gsmBcRlpIFramesTxDiscarded,
       "gsmBcRlpResetsRx": gsmBcRlpResetsRx,
       "gsmBcV42": gsmBcV42,
       "gsmBcV42RowStatusTable": gsmBcV42RowStatusTable,
       "gsmBcV42RowStatusEntry": gsmBcV42RowStatusEntry,
       "gsmBcV42RowStatus": gsmBcV42RowStatus,
       "gsmBcV42ComponentName": gsmBcV42ComponentName,
       "gsmBcV42StorageType": gsmBcV42StorageType,
       "gsmBcV42Index": gsmBcV42Index,
       "gsmBcV42OperTable": gsmBcV42OperTable,
       "gsmBcV42OperEntry": gsmBcV42OperEntry,
       "gsmBcV42ProtocolState": gsmBcV42ProtocolState,
       "gsmBcV42TxN401FrameSize": gsmBcV42TxN401FrameSize,
       "gsmBcV42RxN401FrameSize": gsmBcV42RxN401FrameSize,
       "gsmBcV42TxKwindowSize": gsmBcV42TxKwindowSize,
       "gsmBcV42RxKwindowSize": gsmBcV42RxKwindowSize,
       "gsmBcV42StatsTable": gsmBcV42StatsTable,
       "gsmBcV42StatsEntry": gsmBcV42StatsEntry,
       "gsmBcV42IBytesRx": gsmBcV42IBytesRx,
       "gsmBcV42IBytesTx": gsmBcV42IBytesTx,
       "gsmBcV42IFramesRx": gsmBcV42IFramesRx,
       "gsmBcV42IFramesTx": gsmBcV42IFramesTx,
       "gsmBcV42FramesRetransmitted": gsmBcV42FramesRetransmitted,
       "gsmBcV42T1AckTimeouts": gsmBcV42T1AckTimeouts,
       "gsmBcV42RemoteBusyIndications": gsmBcV42RemoteBusyIndications,
       "gsmBcV42LocalBusyIndications": gsmBcV42LocalBusyIndications,
       "gsmBcV42BadFramesRx": gsmBcV42BadFramesRx,
       "gsmBcV42CrcErrorsRx": gsmBcV42CrcErrorsRx,
       "gsmBcV42bis": gsmBcV42bis,
       "gsmBcV42bisRowStatusTable": gsmBcV42bisRowStatusTable,
       "gsmBcV42bisRowStatusEntry": gsmBcV42bisRowStatusEntry,
       "gsmBcV42bisRowStatus": gsmBcV42bisRowStatus,
       "gsmBcV42bisComponentName": gsmBcV42bisComponentName,
       "gsmBcV42bisStorageType": gsmBcV42bisStorageType,
       "gsmBcV42bisIndex": gsmBcV42bisIndex,
       "gsmBcV42bisOperTable": gsmBcV42bisOperTable,
       "gsmBcV42bisOperEntry": gsmBcV42bisOperEntry,
       "gsmBcV42bisProtocolModeEncoder": gsmBcV42bisProtocolModeEncoder,
       "gsmBcV42bisProtocolModeDecoder": gsmBcV42bisProtocolModeDecoder,
       "gsmBcV42bisCompressionDirection": gsmBcV42bisCompressionDirection,
       "gsmBcV42bisMaximumCodewords": gsmBcV42bisMaximumCodewords,
       "gsmBcV42bisMaximumStringSize": gsmBcV42bisMaximumStringSize,
       "gsmBcV42bisLastDecodeError": gsmBcV42bisLastDecodeError,
       "gsmBcV42bisCompRatioEncoder": gsmBcV42bisCompRatioEncoder,
       "gsmBcV42bisCompRatioDecoder": gsmBcV42bisCompRatioDecoder,
       "gsmBcV42bisStatsTable": gsmBcV42bisStatsTable,
       "gsmBcV42bisStatsEntry": gsmBcV42bisStatsEntry,
       "gsmBcV42bisModeChangesEncode": gsmBcV42bisModeChangesEncode,
       "gsmBcV42bisModeChangesDecode": gsmBcV42bisModeChangesDecode,
       "gsmBcV42bisResetsEncode": gsmBcV42bisResetsEncode,
       "gsmBcV42bisResetsDecode": gsmBcV42bisResetsDecode,
       "gsmBcV42bisReInitializations": gsmBcV42bisReInitializations,
       "gsmBcV42bisErrorsInDecode": gsmBcV42bisErrorsInDecode,
       "gsmBcL2RCop": gsmBcL2RCop,
       "gsmBcL2RCopRowStatusTable": gsmBcL2RCopRowStatusTable,
       "gsmBcL2RCopRowStatusEntry": gsmBcL2RCopRowStatusEntry,
       "gsmBcL2RCopRowStatus": gsmBcL2RCopRowStatus,
       "gsmBcL2RCopComponentName": gsmBcL2RCopComponentName,
       "gsmBcL2RCopStorageType": gsmBcL2RCopStorageType,
       "gsmBcL2RCopIndex": gsmBcL2RCopIndex,
       "gsmBcL2RCopOperTable": gsmBcL2RCopOperTable,
       "gsmBcL2RCopOperEntry": gsmBcL2RCopOperEntry,
       "gsmBcL2RCopFlowControlStateTx": gsmBcL2RCopFlowControlStateTx,
       "gsmBcL2RCopFlowControlStateRx": gsmBcL2RCopFlowControlStateRx,
       "gsmBcL2RCopStatsTable": gsmBcL2RCopStatsTable,
       "gsmBcL2RCopStatsEntry": gsmBcL2RCopStatsEntry,
       "gsmBcL2RCopBytesTx": gsmBcL2RCopBytesTx,
       "gsmBcL2RCopBytesRx": gsmBcL2RCopBytesRx,
       "gsmBcL2RCopBreakCountRx": gsmBcL2RCopBreakCountRx,
       "gsmBcL2RCopBreakCountTx": gsmBcL2RCopBreakCountTx,
       "gsmBcUpperRelay": gsmBcUpperRelay,
       "gsmBcUpperRelayRowStatusTable": gsmBcUpperRelayRowStatusTable,
       "gsmBcUpperRelayRowStatusEntry": gsmBcUpperRelayRowStatusEntry,
       "gsmBcUpperRelayRowStatus": gsmBcUpperRelayRowStatus,
       "gsmBcUpperRelayComponentName": gsmBcUpperRelayComponentName,
       "gsmBcUpperRelayStorageType": gsmBcUpperRelayStorageType,
       "gsmBcUpperRelayIndex": gsmBcUpperRelayIndex,
       "gsmBcUpperRelayOperTable": gsmBcUpperRelayOperTable,
       "gsmBcUpperRelayOperEntry": gsmBcUpperRelayOperEntry,
       "gsmBcUpperRelayBufferSize": gsmBcUpperRelayBufferSize,
       "gsmBcUpperRelayFlowControlStateTx": gsmBcUpperRelayFlowControlStateTx,
       "gsmBcUpperRelayFlowControlStateRx": gsmBcUpperRelayFlowControlStateRx,
       "gsmBcUpperRelayStatsTable": gsmBcUpperRelayStatsTable,
       "gsmBcUpperRelayStatsEntry": gsmBcUpperRelayStatsEntry,
       "gsmBcUpperRelayFramesTx": gsmBcUpperRelayFramesTx,
       "gsmBcUpperRelayFramesRx": gsmBcUpperRelayFramesRx,
       "gsmBcUpperRelayUnacknowledgedFrames": gsmBcUpperRelayUnacknowledgedFrames,
       "gsmBcOperTable": gsmBcOperTable,
       "gsmBcOperEntry": gsmBcOperEntry,
       "gsmBcMipState": gsmBcMipState,
       "gsmBcMaxUserDataRate": gsmBcMaxUserDataRate,
       "gsmBcConnectionType": gsmBcConnectionType,
       "gsmBcDataBits": gsmBcDataBits,
       "gsmBcStopBits": gsmBcStopBits,
       "gsmBcParity": gsmBcParity,
       "gsmBcFlowControl": gsmBcFlowControl,
       "gsmBcCallType": gsmBcCallType,
       "gsmBcLastResponseCode": gsmBcLastResponseCode,
       "gsmBcMateBearerChannel": gsmBcMateBearerChannel,
       "gsmBcCidDataTable": gsmBcCidDataTable,
       "gsmBcCidDataEntry": gsmBcCidDataEntry,
       "gsmBcCustomerIdentifier": gsmBcCustomerIdentifier,
       "gsmBcStateTable": gsmBcStateTable,
       "gsmBcStateEntry": gsmBcStateEntry,
       "gsmBcAdminState": gsmBcAdminState,
       "gsmBcOperationalState": gsmBcOperationalState,
       "gsmBcUsageState": gsmBcUsageState,
       "gsmIwfMIB": gsmIwfMIB,
       "gsmIwfGroup": gsmIwfGroup,
       "gsmIwfGroupBE": gsmIwfGroupBE,
       "gsmIwfGroupBE01": gsmIwfGroupBE01,
       "gsmIwfGroupBE01A": gsmIwfGroupBE01A,
       "gsmIwfCapabilities": gsmIwfCapabilities,
       "gsmIwfCapabilitiesBE": gsmIwfCapabilitiesBE,
       "gsmIwfCapabilitiesBE01": gsmIwfCapabilitiesBE01,
       "gsmIwfCapabilitiesBE01A": gsmIwfCapabilitiesBE01A}
)
