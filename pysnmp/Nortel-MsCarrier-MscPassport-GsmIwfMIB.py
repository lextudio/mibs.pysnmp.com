# SNMP MIB module (Nortel-MsCarrier-MscPassport-GsmIwfMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-GsmIwfMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:34 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint2",
    "Link",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscGsmCs_ObjectIdentity = ObjectIdentity
mscGsmCs = _MscGsmCs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127)
)
_MscGsmCsRowStatusTable_Object = MibTable
mscGsmCsRowStatusTable = _MscGsmCsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 1)
)
if mibBuilder.loadTexts:
    mscGsmCsRowStatusTable.setStatus("mandatory")
_MscGsmCsRowStatusEntry_Object = MibTableRow
mscGsmCsRowStatusEntry = _MscGsmCsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 1, 1)
)
mscGsmCsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsRowStatusEntry.setStatus("mandatory")
_MscGsmCsRowStatus_Type = RowStatus
_MscGsmCsRowStatus_Object = MibTableColumn
mscGsmCsRowStatus = _MscGsmCsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 1, 1, 1),
    _MscGsmCsRowStatus_Type()
)
mscGsmCsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsRowStatus.setStatus("mandatory")
_MscGsmCsComponentName_Type = DisplayString
_MscGsmCsComponentName_Object = MibTableColumn
mscGsmCsComponentName = _MscGsmCsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 1, 1, 2),
    _MscGsmCsComponentName_Type()
)
mscGsmCsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsComponentName.setStatus("mandatory")
_MscGsmCsStorageType_Type = StorageType
_MscGsmCsStorageType_Object = MibTableColumn
mscGsmCsStorageType = _MscGsmCsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 1, 1, 4),
    _MscGsmCsStorageType_Type()
)
mscGsmCsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsStorageType.setStatus("mandatory")


class _MscGsmCsTrunkGrpIndex_Type(Integer32):
    """Custom type mscGsmCsTrunkGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_MscGsmCsTrunkGrpIndex_Type.__name__ = "Integer32"
_MscGsmCsTrunkGrpIndex_Object = MibTableColumn
mscGsmCsTrunkGrpIndex = _MscGsmCsTrunkGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 1, 1, 10),
    _MscGsmCsTrunkGrpIndex_Type()
)
mscGsmCsTrunkGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmCsTrunkGrpIndex.setStatus("mandatory")
_MscGsmCsModem_ObjectIdentity = ObjectIdentity
mscGsmCsModem = _MscGsmCsModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 2)
)
_MscGsmCsModemRowStatusTable_Object = MibTable
mscGsmCsModemRowStatusTable = _MscGsmCsModemRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 2, 1)
)
if mibBuilder.loadTexts:
    mscGsmCsModemRowStatusTable.setStatus("mandatory")
_MscGsmCsModemRowStatusEntry_Object = MibTableRow
mscGsmCsModemRowStatusEntry = _MscGsmCsModemRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 2, 1, 1)
)
mscGsmCsModemRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsModemIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsModemRowStatusEntry.setStatus("mandatory")
_MscGsmCsModemRowStatus_Type = RowStatus
_MscGsmCsModemRowStatus_Object = MibTableColumn
mscGsmCsModemRowStatus = _MscGsmCsModemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 2, 1, 1, 1),
    _MscGsmCsModemRowStatus_Type()
)
mscGsmCsModemRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsModemRowStatus.setStatus("mandatory")
_MscGsmCsModemComponentName_Type = DisplayString
_MscGsmCsModemComponentName_Object = MibTableColumn
mscGsmCsModemComponentName = _MscGsmCsModemComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 2, 1, 1, 2),
    _MscGsmCsModemComponentName_Type()
)
mscGsmCsModemComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsModemComponentName.setStatus("mandatory")
_MscGsmCsModemStorageType_Type = StorageType
_MscGsmCsModemStorageType_Object = MibTableColumn
mscGsmCsModemStorageType = _MscGsmCsModemStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 2, 1, 1, 4),
    _MscGsmCsModemStorageType_Type()
)
mscGsmCsModemStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsModemStorageType.setStatus("mandatory")


class _MscGsmCsModemIndex_Type(Integer32):
    """Custom type mscGsmCsModemIndex based on Integer32"""
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


_MscGsmCsModemIndex_Type.__name__ = "Integer32"
_MscGsmCsModemIndex_Object = MibTableColumn
mscGsmCsModemIndex = _MscGsmCsModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 2, 1, 1, 10),
    _MscGsmCsModemIndex_Type()
)
mscGsmCsModemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmCsModemIndex.setStatus("mandatory")
_MscGsmCsRlp_ObjectIdentity = ObjectIdentity
mscGsmCsRlp = _MscGsmCsRlp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3)
)
_MscGsmCsRlpRowStatusTable_Object = MibTable
mscGsmCsRlpRowStatusTable = _MscGsmCsRlpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 1)
)
if mibBuilder.loadTexts:
    mscGsmCsRlpRowStatusTable.setStatus("mandatory")
_MscGsmCsRlpRowStatusEntry_Object = MibTableRow
mscGsmCsRlpRowStatusEntry = _MscGsmCsRlpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 1, 1)
)
mscGsmCsRlpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsRlpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsRlpRowStatusEntry.setStatus("mandatory")
_MscGsmCsRlpRowStatus_Type = RowStatus
_MscGsmCsRlpRowStatus_Object = MibTableColumn
mscGsmCsRlpRowStatus = _MscGsmCsRlpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 1, 1, 1),
    _MscGsmCsRlpRowStatus_Type()
)
mscGsmCsRlpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsRlpRowStatus.setStatus("mandatory")
_MscGsmCsRlpComponentName_Type = DisplayString
_MscGsmCsRlpComponentName_Object = MibTableColumn
mscGsmCsRlpComponentName = _MscGsmCsRlpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 1, 1, 2),
    _MscGsmCsRlpComponentName_Type()
)
mscGsmCsRlpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsRlpComponentName.setStatus("mandatory")
_MscGsmCsRlpStorageType_Type = StorageType
_MscGsmCsRlpStorageType_Object = MibTableColumn
mscGsmCsRlpStorageType = _MscGsmCsRlpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 1, 1, 4),
    _MscGsmCsRlpStorageType_Type()
)
mscGsmCsRlpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsRlpStorageType.setStatus("mandatory")


class _MscGsmCsRlpIndex_Type(Integer32):
    """Custom type mscGsmCsRlpIndex based on Integer32"""
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


_MscGsmCsRlpIndex_Type.__name__ = "Integer32"
_MscGsmCsRlpIndex_Object = MibTableColumn
mscGsmCsRlpIndex = _MscGsmCsRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 1, 1, 10),
    _MscGsmCsRlpIndex_Type()
)
mscGsmCsRlpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmCsRlpIndex.setStatus("mandatory")
_MscGsmCsRlpProvTable_Object = MibTable
mscGsmCsRlpProvTable = _MscGsmCsRlpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 10)
)
if mibBuilder.loadTexts:
    mscGsmCsRlpProvTable.setStatus("mandatory")
_MscGsmCsRlpProvEntry_Object = MibTableRow
mscGsmCsRlpProvEntry = _MscGsmCsRlpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 10, 1)
)
mscGsmCsRlpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsRlpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsRlpProvEntry.setStatus("mandatory")


class _MscGsmCsRlpHighestVersion_Type(Unsigned32):
    """Custom type mscGsmCsRlpHighestVersion based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscGsmCsRlpHighestVersion_Type.__name__ = "Unsigned32"
_MscGsmCsRlpHighestVersion_Object = MibTableColumn
mscGsmCsRlpHighestVersion = _MscGsmCsRlpHighestVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 10, 1, 1),
    _MscGsmCsRlpHighestVersion_Type()
)
mscGsmCsRlpHighestVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsRlpHighestVersion.setStatus("mandatory")


class _MscGsmCsRlpIwfToMsWindowSize_Type(Unsigned32):
    """Custom type mscGsmCsRlpIwfToMsWindowSize based on Unsigned32"""
    defaultValue = 61

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61),
    )


_MscGsmCsRlpIwfToMsWindowSize_Type.__name__ = "Unsigned32"
_MscGsmCsRlpIwfToMsWindowSize_Object = MibTableColumn
mscGsmCsRlpIwfToMsWindowSize = _MscGsmCsRlpIwfToMsWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 10, 1, 2),
    _MscGsmCsRlpIwfToMsWindowSize_Type()
)
mscGsmCsRlpIwfToMsWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsRlpIwfToMsWindowSize.setStatus("mandatory")


class _MscGsmCsRlpMsToIwfWindowSize_Type(Unsigned32):
    """Custom type mscGsmCsRlpMsToIwfWindowSize based on Unsigned32"""
    defaultValue = 61

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61),
    )


_MscGsmCsRlpMsToIwfWindowSize_Type.__name__ = "Unsigned32"
_MscGsmCsRlpMsToIwfWindowSize_Object = MibTableColumn
mscGsmCsRlpMsToIwfWindowSize = _MscGsmCsRlpMsToIwfWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 10, 1, 3),
    _MscGsmCsRlpMsToIwfWindowSize_Type()
)
mscGsmCsRlpMsToIwfWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsRlpMsToIwfWindowSize.setStatus("mandatory")


class _MscGsmCsRlpT1AckTimer_Type(Unsigned32):
    """Custom type mscGsmCsRlpT1AckTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(380, 1020),
    )


_MscGsmCsRlpT1AckTimer_Type.__name__ = "Unsigned32"
_MscGsmCsRlpT1AckTimer_Object = MibTableColumn
mscGsmCsRlpT1AckTimer = _MscGsmCsRlpT1AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 10, 1, 4),
    _MscGsmCsRlpT1AckTimer_Type()
)
mscGsmCsRlpT1AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsRlpT1AckTimer.setStatus("mandatory")


class _MscGsmCsRlpT2AckDelayTimer_Type(Unsigned32):
    """Custom type mscGsmCsRlpT2AckDelayTimer based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 79),
    )


_MscGsmCsRlpT2AckDelayTimer_Type.__name__ = "Unsigned32"
_MscGsmCsRlpT2AckDelayTimer_Object = MibTableColumn
mscGsmCsRlpT2AckDelayTimer = _MscGsmCsRlpT2AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 10, 1, 5),
    _MscGsmCsRlpT2AckDelayTimer_Type()
)
mscGsmCsRlpT2AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsRlpT2AckDelayTimer.setStatus("mandatory")


class _MscGsmCsRlpN2RetransmitCount_Type(Unsigned32):
    """Custom type mscGsmCsRlpN2RetransmitCount based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscGsmCsRlpN2RetransmitCount_Type.__name__ = "Unsigned32"
_MscGsmCsRlpN2RetransmitCount_Object = MibTableColumn
mscGsmCsRlpN2RetransmitCount = _MscGsmCsRlpN2RetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 3, 10, 1, 6),
    _MscGsmCsRlpN2RetransmitCount_Type()
)
mscGsmCsRlpN2RetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsRlpN2RetransmitCount.setStatus("mandatory")
_MscGsmCsFax_ObjectIdentity = ObjectIdentity
mscGsmCsFax = _MscGsmCsFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4)
)
_MscGsmCsFaxRowStatusTable_Object = MibTable
mscGsmCsFaxRowStatusTable = _MscGsmCsFaxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4, 1)
)
if mibBuilder.loadTexts:
    mscGsmCsFaxRowStatusTable.setStatus("mandatory")
_MscGsmCsFaxRowStatusEntry_Object = MibTableRow
mscGsmCsFaxRowStatusEntry = _MscGsmCsFaxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4, 1, 1)
)
mscGsmCsFaxRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsFaxIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsFaxRowStatusEntry.setStatus("mandatory")
_MscGsmCsFaxRowStatus_Type = RowStatus
_MscGsmCsFaxRowStatus_Object = MibTableColumn
mscGsmCsFaxRowStatus = _MscGsmCsFaxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4, 1, 1, 1),
    _MscGsmCsFaxRowStatus_Type()
)
mscGsmCsFaxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsFaxRowStatus.setStatus("mandatory")
_MscGsmCsFaxComponentName_Type = DisplayString
_MscGsmCsFaxComponentName_Object = MibTableColumn
mscGsmCsFaxComponentName = _MscGsmCsFaxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4, 1, 1, 2),
    _MscGsmCsFaxComponentName_Type()
)
mscGsmCsFaxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsFaxComponentName.setStatus("mandatory")
_MscGsmCsFaxStorageType_Type = StorageType
_MscGsmCsFaxStorageType_Object = MibTableColumn
mscGsmCsFaxStorageType = _MscGsmCsFaxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4, 1, 1, 4),
    _MscGsmCsFaxStorageType_Type()
)
mscGsmCsFaxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsFaxStorageType.setStatus("mandatory")
_MscGsmCsFaxIndex_Type = NonReplicated
_MscGsmCsFaxIndex_Object = MibTableColumn
mscGsmCsFaxIndex = _MscGsmCsFaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4, 1, 1, 10),
    _MscGsmCsFaxIndex_Type()
)
mscGsmCsFaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmCsFaxIndex.setStatus("mandatory")
_MscGsmCsFaxProvTable_Object = MibTable
mscGsmCsFaxProvTable = _MscGsmCsFaxProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4, 10)
)
if mibBuilder.loadTexts:
    mscGsmCsFaxProvTable.setStatus("mandatory")
_MscGsmCsFaxProvEntry_Object = MibTableRow
mscGsmCsFaxProvEntry = _MscGsmCsFaxProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4, 10, 1)
)
mscGsmCsFaxProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsFaxIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsFaxProvEntry.setStatus("mandatory")


class _MscGsmCsFaxT1CalledToneTimer_Type(FixedPoint2):
    """Custom type mscGsmCsFaxT1CalledToneTimer based on FixedPoint2"""
    defaultValue = 180

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 300),
    )


_MscGsmCsFaxT1CalledToneTimer_Type.__name__ = "FixedPoint2"
_MscGsmCsFaxT1CalledToneTimer_Object = MibTableColumn
mscGsmCsFaxT1CalledToneTimer = _MscGsmCsFaxT1CalledToneTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 4, 10, 1, 1),
    _MscGsmCsFaxT1CalledToneTimer_Type()
)
mscGsmCsFaxT1CalledToneTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsFaxT1CalledToneTimer.setStatus("mandatory")
_MscGsmCsV42_ObjectIdentity = ObjectIdentity
mscGsmCsV42 = _MscGsmCsV42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5)
)
_MscGsmCsV42RowStatusTable_Object = MibTable
mscGsmCsV42RowStatusTable = _MscGsmCsV42RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 1)
)
if mibBuilder.loadTexts:
    mscGsmCsV42RowStatusTable.setStatus("mandatory")
_MscGsmCsV42RowStatusEntry_Object = MibTableRow
mscGsmCsV42RowStatusEntry = _MscGsmCsV42RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 1, 1)
)
mscGsmCsV42RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsV42Index"),
)
if mibBuilder.loadTexts:
    mscGsmCsV42RowStatusEntry.setStatus("mandatory")
_MscGsmCsV42RowStatus_Type = RowStatus
_MscGsmCsV42RowStatus_Object = MibTableColumn
mscGsmCsV42RowStatus = _MscGsmCsV42RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 1, 1, 1),
    _MscGsmCsV42RowStatus_Type()
)
mscGsmCsV42RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsV42RowStatus.setStatus("mandatory")
_MscGsmCsV42ComponentName_Type = DisplayString
_MscGsmCsV42ComponentName_Object = MibTableColumn
mscGsmCsV42ComponentName = _MscGsmCsV42ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 1, 1, 2),
    _MscGsmCsV42ComponentName_Type()
)
mscGsmCsV42ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsV42ComponentName.setStatus("mandatory")
_MscGsmCsV42StorageType_Type = StorageType
_MscGsmCsV42StorageType_Object = MibTableColumn
mscGsmCsV42StorageType = _MscGsmCsV42StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 1, 1, 4),
    _MscGsmCsV42StorageType_Type()
)
mscGsmCsV42StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsV42StorageType.setStatus("mandatory")
_MscGsmCsV42Index_Type = NonReplicated
_MscGsmCsV42Index_Object = MibTableColumn
mscGsmCsV42Index = _MscGsmCsV42Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 1, 1, 10),
    _MscGsmCsV42Index_Type()
)
mscGsmCsV42Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmCsV42Index.setStatus("mandatory")
_MscGsmCsV42ProvTable_Object = MibTable
mscGsmCsV42ProvTable = _MscGsmCsV42ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10)
)
if mibBuilder.loadTexts:
    mscGsmCsV42ProvTable.setStatus("mandatory")
_MscGsmCsV42ProvEntry_Object = MibTableRow
mscGsmCsV42ProvEntry = _MscGsmCsV42ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1)
)
mscGsmCsV42ProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsV42Index"),
)
if mibBuilder.loadTexts:
    mscGsmCsV42ProvEntry.setStatus("mandatory")


class _MscGsmCsV42T400DetectTimer_Type(FixedPoint2):
    """Custom type mscGsmCsV42T400DetectTimer based on FixedPoint2"""
    defaultValue = 200

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 254),
    )


_MscGsmCsV42T400DetectTimer_Type.__name__ = "FixedPoint2"
_MscGsmCsV42T400DetectTimer_Object = MibTableColumn
mscGsmCsV42T400DetectTimer = _MscGsmCsV42T400DetectTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1, 1),
    _MscGsmCsV42T400DetectTimer_Type()
)
mscGsmCsV42T400DetectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42T400DetectTimer.setStatus("mandatory")


class _MscGsmCsV42T401AckTimer_Type(FixedPoint2):
    """Custom type mscGsmCsV42T401AckTimer based on FixedPoint2"""
    defaultValue = 400

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 900),
    )


_MscGsmCsV42T401AckTimer_Type.__name__ = "FixedPoint2"
_MscGsmCsV42T401AckTimer_Object = MibTableColumn
mscGsmCsV42T401AckTimer = _MscGsmCsV42T401AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1, 2),
    _MscGsmCsV42T401AckTimer_Type()
)
mscGsmCsV42T401AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42T401AckTimer.setStatus("mandatory")


class _MscGsmCsV42T402AckDelayTimer_Type(FixedPoint2):
    """Custom type mscGsmCsV42T402AckDelayTimer based on FixedPoint2"""
    defaultValue = 200

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 450),
    )


_MscGsmCsV42T402AckDelayTimer_Type.__name__ = "FixedPoint2"
_MscGsmCsV42T402AckDelayTimer_Object = MibTableColumn
mscGsmCsV42T402AckDelayTimer = _MscGsmCsV42T402AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1, 3),
    _MscGsmCsV42T402AckDelayTimer_Type()
)
mscGsmCsV42T402AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42T402AckDelayTimer.setStatus("mandatory")


class _MscGsmCsV42T403IdleProbeTimer_Type(Unsigned32):
    """Custom type mscGsmCsV42T403IdleProbeTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 90),
    )


_MscGsmCsV42T403IdleProbeTimer_Type.__name__ = "Unsigned32"
_MscGsmCsV42T403IdleProbeTimer_Object = MibTableColumn
mscGsmCsV42T403IdleProbeTimer = _MscGsmCsV42T403IdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1, 4),
    _MscGsmCsV42T403IdleProbeTimer_Type()
)
mscGsmCsV42T403IdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42T403IdleProbeTimer.setStatus("mandatory")


class _MscGsmCsV42TxN401FrameSize_Type(Unsigned32):
    """Custom type mscGsmCsV42TxN401FrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscGsmCsV42TxN401FrameSize_Type.__name__ = "Unsigned32"
_MscGsmCsV42TxN401FrameSize_Object = MibTableColumn
mscGsmCsV42TxN401FrameSize = _MscGsmCsV42TxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1, 5),
    _MscGsmCsV42TxN401FrameSize_Type()
)
mscGsmCsV42TxN401FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42TxN401FrameSize.setStatus("mandatory")


class _MscGsmCsV42RxN401FrameSize_Type(Unsigned32):
    """Custom type mscGsmCsV42RxN401FrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscGsmCsV42RxN401FrameSize_Type.__name__ = "Unsigned32"
_MscGsmCsV42RxN401FrameSize_Object = MibTableColumn
mscGsmCsV42RxN401FrameSize = _MscGsmCsV42RxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1, 6),
    _MscGsmCsV42RxN401FrameSize_Type()
)
mscGsmCsV42RxN401FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42RxN401FrameSize.setStatus("mandatory")


class _MscGsmCsV42TxKwindowSize_Type(Unsigned32):
    """Custom type mscGsmCsV42TxKwindowSize based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscGsmCsV42TxKwindowSize_Type.__name__ = "Unsigned32"
_MscGsmCsV42TxKwindowSize_Object = MibTableColumn
mscGsmCsV42TxKwindowSize = _MscGsmCsV42TxKwindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1, 7),
    _MscGsmCsV42TxKwindowSize_Type()
)
mscGsmCsV42TxKwindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42TxKwindowSize.setStatus("mandatory")


class _MscGsmCsV42RxKwindowSize_Type(Unsigned32):
    """Custom type mscGsmCsV42RxKwindowSize based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscGsmCsV42RxKwindowSize_Type.__name__ = "Unsigned32"
_MscGsmCsV42RxKwindowSize_Object = MibTableColumn
mscGsmCsV42RxKwindowSize = _MscGsmCsV42RxKwindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1, 8),
    _MscGsmCsV42RxKwindowSize_Type()
)
mscGsmCsV42RxKwindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42RxKwindowSize.setStatus("mandatory")


class _MscGsmCsV42N400RetransLimit_Type(Unsigned32):
    """Custom type mscGsmCsV42N400RetransLimit based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscGsmCsV42N400RetransLimit_Type.__name__ = "Unsigned32"
_MscGsmCsV42N400RetransLimit_Object = MibTableColumn
mscGsmCsV42N400RetransLimit = _MscGsmCsV42N400RetransLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 5, 10, 1, 9),
    _MscGsmCsV42N400RetransLimit_Type()
)
mscGsmCsV42N400RetransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42N400RetransLimit.setStatus("mandatory")
_MscGsmCsV42bis_ObjectIdentity = ObjectIdentity
mscGsmCsV42bis = _MscGsmCsV42bis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6)
)
_MscGsmCsV42bisRowStatusTable_Object = MibTable
mscGsmCsV42bisRowStatusTable = _MscGsmCsV42bisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 1)
)
if mibBuilder.loadTexts:
    mscGsmCsV42bisRowStatusTable.setStatus("mandatory")
_MscGsmCsV42bisRowStatusEntry_Object = MibTableRow
mscGsmCsV42bisRowStatusEntry = _MscGsmCsV42bisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 1, 1)
)
mscGsmCsV42bisRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsV42bisIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsV42bisRowStatusEntry.setStatus("mandatory")
_MscGsmCsV42bisRowStatus_Type = RowStatus
_MscGsmCsV42bisRowStatus_Object = MibTableColumn
mscGsmCsV42bisRowStatus = _MscGsmCsV42bisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 1, 1, 1),
    _MscGsmCsV42bisRowStatus_Type()
)
mscGsmCsV42bisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsV42bisRowStatus.setStatus("mandatory")
_MscGsmCsV42bisComponentName_Type = DisplayString
_MscGsmCsV42bisComponentName_Object = MibTableColumn
mscGsmCsV42bisComponentName = _MscGsmCsV42bisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 1, 1, 2),
    _MscGsmCsV42bisComponentName_Type()
)
mscGsmCsV42bisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsV42bisComponentName.setStatus("mandatory")
_MscGsmCsV42bisStorageType_Type = StorageType
_MscGsmCsV42bisStorageType_Object = MibTableColumn
mscGsmCsV42bisStorageType = _MscGsmCsV42bisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 1, 1, 4),
    _MscGsmCsV42bisStorageType_Type()
)
mscGsmCsV42bisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsV42bisStorageType.setStatus("mandatory")
_MscGsmCsV42bisIndex_Type = NonReplicated
_MscGsmCsV42bisIndex_Object = MibTableColumn
mscGsmCsV42bisIndex = _MscGsmCsV42bisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 1, 1, 10),
    _MscGsmCsV42bisIndex_Type()
)
mscGsmCsV42bisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmCsV42bisIndex.setStatus("mandatory")
_MscGsmCsV42bisProvTable_Object = MibTable
mscGsmCsV42bisProvTable = _MscGsmCsV42bisProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 10)
)
if mibBuilder.loadTexts:
    mscGsmCsV42bisProvTable.setStatus("mandatory")
_MscGsmCsV42bisProvEntry_Object = MibTableRow
mscGsmCsV42bisProvEntry = _MscGsmCsV42bisProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 10, 1)
)
mscGsmCsV42bisProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsV42bisIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsV42bisProvEntry.setStatus("mandatory")


class _MscGsmCsV42bisCompressionDirection_Type(Integer32):
    """Custom type mscGsmCsV42bisCompressionDirection based on Integer32"""
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


_MscGsmCsV42bisCompressionDirection_Type.__name__ = "Integer32"
_MscGsmCsV42bisCompressionDirection_Object = MibTableColumn
mscGsmCsV42bisCompressionDirection = _MscGsmCsV42bisCompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 10, 1, 1),
    _MscGsmCsV42bisCompressionDirection_Type()
)
mscGsmCsV42bisCompressionDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42bisCompressionDirection.setStatus("mandatory")


class _MscGsmCsV42bisMaximumCodewords_Type(Unsigned32):
    """Custom type mscGsmCsV42bisMaximumCodewords based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
        ValueRangeConstraint(4096, 4096),
    )


_MscGsmCsV42bisMaximumCodewords_Type.__name__ = "Unsigned32"
_MscGsmCsV42bisMaximumCodewords_Object = MibTableColumn
mscGsmCsV42bisMaximumCodewords = _MscGsmCsV42bisMaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 10, 1, 2),
    _MscGsmCsV42bisMaximumCodewords_Type()
)
mscGsmCsV42bisMaximumCodewords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42bisMaximumCodewords.setStatus("mandatory")


class _MscGsmCsV42bisMaximumStringSize_Type(Unsigned32):
    """Custom type mscGsmCsV42bisMaximumStringSize based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_MscGsmCsV42bisMaximumStringSize_Type.__name__ = "Unsigned32"
_MscGsmCsV42bisMaximumStringSize_Object = MibTableColumn
mscGsmCsV42bisMaximumStringSize = _MscGsmCsV42bisMaximumStringSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 10, 1, 3),
    _MscGsmCsV42bisMaximumStringSize_Type()
)
mscGsmCsV42bisMaximumStringSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42bisMaximumStringSize.setStatus("mandatory")


class _MscGsmCsV42bisActionOnError_Type(Integer32):
    """Custom type mscGsmCsV42bisActionOnError based on Integer32"""
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


_MscGsmCsV42bisActionOnError_Type.__name__ = "Integer32"
_MscGsmCsV42bisActionOnError_Object = MibTableColumn
mscGsmCsV42bisActionOnError = _MscGsmCsV42bisActionOnError_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 6, 10, 1, 4),
    _MscGsmCsV42bisActionOnError_Type()
)
mscGsmCsV42bisActionOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsV42bisActionOnError.setStatus("mandatory")
_MscGsmCsLp_ObjectIdentity = ObjectIdentity
mscGsmCsLp = _MscGsmCsLp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7)
)
_MscGsmCsLpRowStatusTable_Object = MibTable
mscGsmCsLpRowStatusTable = _MscGsmCsLpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 1)
)
if mibBuilder.loadTexts:
    mscGsmCsLpRowStatusTable.setStatus("mandatory")
_MscGsmCsLpRowStatusEntry_Object = MibTableRow
mscGsmCsLpRowStatusEntry = _MscGsmCsLpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 1, 1)
)
mscGsmCsLpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsLpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsLpRowStatusEntry.setStatus("mandatory")
_MscGsmCsLpRowStatus_Type = RowStatus
_MscGsmCsLpRowStatus_Object = MibTableColumn
mscGsmCsLpRowStatus = _MscGsmCsLpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 1, 1, 1),
    _MscGsmCsLpRowStatus_Type()
)
mscGsmCsLpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsLpRowStatus.setStatus("mandatory")
_MscGsmCsLpComponentName_Type = DisplayString
_MscGsmCsLpComponentName_Object = MibTableColumn
mscGsmCsLpComponentName = _MscGsmCsLpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 1, 1, 2),
    _MscGsmCsLpComponentName_Type()
)
mscGsmCsLpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsLpComponentName.setStatus("mandatory")
_MscGsmCsLpStorageType_Type = StorageType
_MscGsmCsLpStorageType_Object = MibTableColumn
mscGsmCsLpStorageType = _MscGsmCsLpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 1, 1, 4),
    _MscGsmCsLpStorageType_Type()
)
mscGsmCsLpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsLpStorageType.setStatus("mandatory")


class _MscGsmCsLpIndex_Type(Integer32):
    """Custom type mscGsmCsLpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscGsmCsLpIndex_Type.__name__ = "Integer32"
_MscGsmCsLpIndex_Object = MibTableColumn
mscGsmCsLpIndex = _MscGsmCsLpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 1, 1, 10),
    _MscGsmCsLpIndex_Type()
)
mscGsmCsLpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmCsLpIndex.setStatus("mandatory")
_MscGsmCsLpOperTable_Object = MibTable
mscGsmCsLpOperTable = _MscGsmCsLpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 10)
)
if mibBuilder.loadTexts:
    mscGsmCsLpOperTable.setStatus("mandatory")
_MscGsmCsLpOperEntry_Object = MibTableRow
mscGsmCsLpOperEntry = _MscGsmCsLpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 10, 1)
)
mscGsmCsLpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsLpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsLpOperEntry.setStatus("mandatory")


class _MscGsmCsLpConfiguredBearerChannels_Type(Unsigned32):
    """Custom type mscGsmCsLpConfiguredBearerChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_MscGsmCsLpConfiguredBearerChannels_Type.__name__ = "Unsigned32"
_MscGsmCsLpConfiguredBearerChannels_Object = MibTableColumn
mscGsmCsLpConfiguredBearerChannels = _MscGsmCsLpConfiguredBearerChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 10, 1, 1),
    _MscGsmCsLpConfiguredBearerChannels_Type()
)
mscGsmCsLpConfiguredBearerChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsLpConfiguredBearerChannels.setStatus("mandatory")


class _MscGsmCsLpActiveCalls_Type(Gauge32):
    """Custom type mscGsmCsLpActiveCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_MscGsmCsLpActiveCalls_Type.__name__ = "Gauge32"
_MscGsmCsLpActiveCalls_Object = MibTableColumn
mscGsmCsLpActiveCalls = _MscGsmCsLpActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 10, 1, 2),
    _MscGsmCsLpActiveCalls_Type()
)
mscGsmCsLpActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsLpActiveCalls.setStatus("mandatory")


class _MscGsmCsLpAssignedCapacity_Type(Unsigned32):
    """Custom type mscGsmCsLpAssignedCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscGsmCsLpAssignedCapacity_Type.__name__ = "Unsigned32"
_MscGsmCsLpAssignedCapacity_Object = MibTableColumn
mscGsmCsLpAssignedCapacity = _MscGsmCsLpAssignedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 10, 1, 3),
    _MscGsmCsLpAssignedCapacity_Type()
)
mscGsmCsLpAssignedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsLpAssignedCapacity.setStatus("mandatory")


class _MscGsmCsLpModemsSupported_Type(Integer32):
    """Custom type mscGsmCsLpModemsSupported based on Integer32"""
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


_MscGsmCsLpModemsSupported_Type.__name__ = "Integer32"
_MscGsmCsLpModemsSupported_Object = MibTableColumn
mscGsmCsLpModemsSupported = _MscGsmCsLpModemsSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 7, 10, 1, 4),
    _MscGsmCsLpModemsSupported_Type()
)
mscGsmCsLpModemsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsLpModemsSupported.setStatus("mandatory")
_MscGsmCsProvTable_Object = MibTable
mscGsmCsProvTable = _MscGsmCsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 100)
)
if mibBuilder.loadTexts:
    mscGsmCsProvTable.setStatus("mandatory")
_MscGsmCsProvEntry_Object = MibTableRow
mscGsmCsProvEntry = _MscGsmCsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 100, 1)
)
mscGsmCsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsProvEntry.setStatus("mandatory")


class _MscGsmCsCommentText_Type(AsciiString):
    """Custom type mscGsmCsCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscGsmCsCommentText_Type.__name__ = "AsciiString"
_MscGsmCsCommentText_Object = MibTableColumn
mscGsmCsCommentText = _MscGsmCsCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 100, 1, 1),
    _MscGsmCsCommentText_Type()
)
mscGsmCsCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsCommentText.setStatus("mandatory")


class _MscGsmCsMscIpAddress_Type(IpAddress):
    """Custom type mscGsmCsMscIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscGsmCsMscIpAddress_Object = MibTableColumn
mscGsmCsMscIpAddress = _MscGsmCsMscIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 100, 1, 2),
    _MscGsmCsMscIpAddress_Type()
)
mscGsmCsMscIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsMscIpAddress.setStatus("mandatory")
_MscGsmCsVirtualRouterName_Type = RowPointer
_MscGsmCsVirtualRouterName_Object = MibTableColumn
mscGsmCsVirtualRouterName = _MscGsmCsVirtualRouterName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 100, 1, 4),
    _MscGsmCsVirtualRouterName_Type()
)
mscGsmCsVirtualRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsVirtualRouterName.setStatus("mandatory")


class _MscGsmCsVoiceLaw_Type(Integer32):
    """Custom type mscGsmCsVoiceLaw based on Integer32"""
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


_MscGsmCsVoiceLaw_Type.__name__ = "Integer32"
_MscGsmCsVoiceLaw_Object = MibTableColumn
mscGsmCsVoiceLaw = _MscGsmCsVoiceLaw_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 100, 1, 5),
    _MscGsmCsVoiceLaw_Type()
)
mscGsmCsVoiceLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsVoiceLaw.setStatus("mandatory")
_MscGsmCsCidDataTable_Object = MibTable
mscGsmCsCidDataTable = _MscGsmCsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 103)
)
if mibBuilder.loadTexts:
    mscGsmCsCidDataTable.setStatus("mandatory")
_MscGsmCsCidDataEntry_Object = MibTableRow
mscGsmCsCidDataEntry = _MscGsmCsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 103, 1)
)
mscGsmCsCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsCidDataEntry.setStatus("mandatory")


class _MscGsmCsCustomerIdentifier_Type(Unsigned32):
    """Custom type mscGsmCsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscGsmCsCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscGsmCsCustomerIdentifier_Object = MibTableColumn
mscGsmCsCustomerIdentifier = _MscGsmCsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 103, 1, 1),
    _MscGsmCsCustomerIdentifier_Type()
)
mscGsmCsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmCsCustomerIdentifier.setStatus("mandatory")
_MscGsmCsStateTable_Object = MibTable
mscGsmCsStateTable = _MscGsmCsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 104)
)
if mibBuilder.loadTexts:
    mscGsmCsStateTable.setStatus("mandatory")
_MscGsmCsStateEntry_Object = MibTableRow
mscGsmCsStateEntry = _MscGsmCsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 104, 1)
)
mscGsmCsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsStateEntry.setStatus("mandatory")


class _MscGsmCsAdminState_Type(Integer32):
    """Custom type mscGsmCsAdminState based on Integer32"""
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


_MscGsmCsAdminState_Type.__name__ = "Integer32"
_MscGsmCsAdminState_Object = MibTableColumn
mscGsmCsAdminState = _MscGsmCsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 104, 1, 1),
    _MscGsmCsAdminState_Type()
)
mscGsmCsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsAdminState.setStatus("mandatory")


class _MscGsmCsOperationalState_Type(Integer32):
    """Custom type mscGsmCsOperationalState based on Integer32"""
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


_MscGsmCsOperationalState_Type.__name__ = "Integer32"
_MscGsmCsOperationalState_Object = MibTableColumn
mscGsmCsOperationalState = _MscGsmCsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 104, 1, 2),
    _MscGsmCsOperationalState_Type()
)
mscGsmCsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsOperationalState.setStatus("mandatory")


class _MscGsmCsUsageState_Type(Integer32):
    """Custom type mscGsmCsUsageState based on Integer32"""
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


_MscGsmCsUsageState_Type.__name__ = "Integer32"
_MscGsmCsUsageState_Object = MibTableColumn
mscGsmCsUsageState = _MscGsmCsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 104, 1, 3),
    _MscGsmCsUsageState_Type()
)
mscGsmCsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsUsageState.setStatus("mandatory")
_MscGsmCsStatsTable_Object = MibTable
mscGsmCsStatsTable = _MscGsmCsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121)
)
if mibBuilder.loadTexts:
    mscGsmCsStatsTable.setStatus("mandatory")
_MscGsmCsStatsEntry_Object = MibTableRow
mscGsmCsStatsEntry = _MscGsmCsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1)
)
mscGsmCsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmCsTrunkGrpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmCsStatsEntry.setStatus("mandatory")


class _MscGsmCsCurrentCalls_Type(Gauge32):
    """Custom type mscGsmCsCurrentCalls based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_MscGsmCsCurrentCalls_Type.__name__ = "Gauge32"
_MscGsmCsCurrentCalls_Object = MibTableColumn
mscGsmCsCurrentCalls = _MscGsmCsCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 1),
    _MscGsmCsCurrentCalls_Type()
)
mscGsmCsCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsCurrentCalls.setStatus("mandatory")
_MscGsmCsCallsRequested_Type = Counter32
_MscGsmCsCallsRequested_Object = MibTableColumn
mscGsmCsCallsRequested = _MscGsmCsCallsRequested_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 2),
    _MscGsmCsCallsRequested_Type()
)
mscGsmCsCallsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsCallsRequested.setStatus("mandatory")
_MscGsmCsCallsSetup_Type = Counter32
_MscGsmCsCallsSetup_Object = MibTableColumn
mscGsmCsCallsSetup = _MscGsmCsCallsSetup_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 3),
    _MscGsmCsCallsSetup_Type()
)
mscGsmCsCallsSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsCallsSetup.setStatus("mandatory")
_MscGsmCsCallsActivated_Type = Counter32
_MscGsmCsCallsActivated_Object = MibTableColumn
mscGsmCsCallsActivated = _MscGsmCsCallsActivated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 4),
    _MscGsmCsCallsActivated_Type()
)
mscGsmCsCallsActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsCallsActivated.setStatus("mandatory")
_MscGsmCsCallsReleasedNormal_Type = Counter32
_MscGsmCsCallsReleasedNormal_Object = MibTableColumn
mscGsmCsCallsReleasedNormal = _MscGsmCsCallsReleasedNormal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 5),
    _MscGsmCsCallsReleasedNormal_Type()
)
mscGsmCsCallsReleasedNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsCallsReleasedNormal.setStatus("mandatory")
_MscGsmCsCallsReleasedAbnormal_Type = Counter32
_MscGsmCsCallsReleasedAbnormal_Object = MibTableColumn
mscGsmCsCallsReleasedAbnormal = _MscGsmCsCallsReleasedAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 6),
    _MscGsmCsCallsReleasedAbnormal_Type()
)
mscGsmCsCallsReleasedAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsCallsReleasedAbnormal.setStatus("mandatory")
_MscGsmCsChannelConfigChanges_Type = Counter32
_MscGsmCsChannelConfigChanges_Object = MibTableColumn
mscGsmCsChannelConfigChanges = _MscGsmCsChannelConfigChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 7),
    _MscGsmCsChannelConfigChanges_Type()
)
mscGsmCsChannelConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsChannelConfigChanges.setStatus("mandatory")
_MscGsmCsChannelModeModifyRequests_Type = Counter32
_MscGsmCsChannelModeModifyRequests_Object = MibTableColumn
mscGsmCsChannelModeModifyRequests = _MscGsmCsChannelModeModifyRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 8),
    _MscGsmCsChannelModeModifyRequests_Type()
)
mscGsmCsChannelModeModifyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsChannelModeModifyRequests.setStatus("mandatory")
_MscGsmCsStatusMessagesRx_Type = Counter32
_MscGsmCsStatusMessagesRx_Object = MibTableColumn
mscGsmCsStatusMessagesRx = _MscGsmCsStatusMessagesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 9),
    _MscGsmCsStatusMessagesRx_Type()
)
mscGsmCsStatusMessagesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsStatusMessagesRx.setStatus("mandatory")
_MscGsmCsErroredMipFrames_Type = Counter32
_MscGsmCsErroredMipFrames_Object = MibTableColumn
mscGsmCsErroredMipFrames = _MscGsmCsErroredMipFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 127, 121, 1, 10),
    _MscGsmCsErroredMipFrames_Type()
)
mscGsmCsErroredMipFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmCsErroredMipFrames.setStatus("mandatory")
_MscGsmBc_ObjectIdentity = ObjectIdentity
mscGsmBc = _MscGsmBc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128)
)
_MscGsmBcRowStatusTable_Object = MibTable
mscGsmBcRowStatusTable = _MscGsmBcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcRowStatusTable.setStatus("mandatory")
_MscGsmBcRowStatusEntry_Object = MibTableRow
mscGsmBcRowStatusEntry = _MscGsmBcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 1, 1)
)
mscGsmBcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcRowStatusEntry.setStatus("mandatory")
_MscGsmBcRowStatus_Type = RowStatus
_MscGsmBcRowStatus_Object = MibTableColumn
mscGsmBcRowStatus = _MscGsmBcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 1, 1, 1),
    _MscGsmBcRowStatus_Type()
)
mscGsmBcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmBcRowStatus.setStatus("mandatory")
_MscGsmBcComponentName_Type = DisplayString
_MscGsmBcComponentName_Object = MibTableColumn
mscGsmBcComponentName = _MscGsmBcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 1, 1, 2),
    _MscGsmBcComponentName_Type()
)
mscGsmBcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcComponentName.setStatus("mandatory")
_MscGsmBcStorageType_Type = StorageType
_MscGsmBcStorageType_Object = MibTableColumn
mscGsmBcStorageType = _MscGsmBcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 1, 1, 4),
    _MscGsmBcStorageType_Type()
)
mscGsmBcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcStorageType.setStatus("mandatory")


class _MscGsmBcTrunkGrpIndex_Type(Integer32):
    """Custom type mscGsmBcTrunkGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_MscGsmBcTrunkGrpIndex_Type.__name__ = "Integer32"
_MscGsmBcTrunkGrpIndex_Object = MibTableColumn
mscGsmBcTrunkGrpIndex = _MscGsmBcTrunkGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 1, 1, 10),
    _MscGsmBcTrunkGrpIndex_Type()
)
mscGsmBcTrunkGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcTrunkGrpIndex.setStatus("mandatory")


class _MscGsmBcCicIndex_Type(Integer32):
    """Custom type mscGsmBcCicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_MscGsmBcCicIndex_Type.__name__ = "Integer32"
_MscGsmBcCicIndex_Object = MibTableColumn
mscGsmBcCicIndex = _MscGsmBcCicIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 1, 1, 11),
    _MscGsmBcCicIndex_Type()
)
mscGsmBcCicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcCicIndex.setStatus("mandatory")
_MscGsmBcFramer_ObjectIdentity = ObjectIdentity
mscGsmBcFramer = _MscGsmBcFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2)
)
_MscGsmBcFramerRowStatusTable_Object = MibTable
mscGsmBcFramerRowStatusTable = _MscGsmBcFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcFramerRowStatusTable.setStatus("mandatory")
_MscGsmBcFramerRowStatusEntry_Object = MibTableRow
mscGsmBcFramerRowStatusEntry = _MscGsmBcFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 1, 1)
)
mscGsmBcFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcFramerRowStatusEntry.setStatus("mandatory")
_MscGsmBcFramerRowStatus_Type = RowStatus
_MscGsmBcFramerRowStatus_Object = MibTableColumn
mscGsmBcFramerRowStatus = _MscGsmBcFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 1, 1, 1),
    _MscGsmBcFramerRowStatus_Type()
)
mscGsmBcFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerRowStatus.setStatus("mandatory")
_MscGsmBcFramerComponentName_Type = DisplayString
_MscGsmBcFramerComponentName_Object = MibTableColumn
mscGsmBcFramerComponentName = _MscGsmBcFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 1, 1, 2),
    _MscGsmBcFramerComponentName_Type()
)
mscGsmBcFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerComponentName.setStatus("mandatory")
_MscGsmBcFramerStorageType_Type = StorageType
_MscGsmBcFramerStorageType_Object = MibTableColumn
mscGsmBcFramerStorageType = _MscGsmBcFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 1, 1, 4),
    _MscGsmBcFramerStorageType_Type()
)
mscGsmBcFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerStorageType.setStatus("mandatory")
_MscGsmBcFramerIndex_Type = NonReplicated
_MscGsmBcFramerIndex_Object = MibTableColumn
mscGsmBcFramerIndex = _MscGsmBcFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 1, 1, 10),
    _MscGsmBcFramerIndex_Type()
)
mscGsmBcFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcFramerIndex.setStatus("mandatory")
_MscGsmBcFramerProvTable_Object = MibTable
mscGsmBcFramerProvTable = _MscGsmBcFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcFramerProvTable.setStatus("mandatory")
_MscGsmBcFramerProvEntry_Object = MibTableRow
mscGsmBcFramerProvEntry = _MscGsmBcFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 10, 1)
)
mscGsmBcFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcFramerProvEntry.setStatus("mandatory")
_MscGsmBcFramerInterfaceName_Type = Link
_MscGsmBcFramerInterfaceName_Object = MibTableColumn
mscGsmBcFramerInterfaceName = _MscGsmBcFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 10, 1, 1),
    _MscGsmBcFramerInterfaceName_Type()
)
mscGsmBcFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmBcFramerInterfaceName.setStatus("mandatory")
_MscGsmBcFramerStatsTable_Object = MibTable
mscGsmBcFramerStatsTable = _MscGsmBcFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcFramerStatsTable.setStatus("mandatory")
_MscGsmBcFramerStatsEntry_Object = MibTableRow
mscGsmBcFramerStatsEntry = _MscGsmBcFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11, 1)
)
mscGsmBcFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcFramerStatsEntry.setStatus("mandatory")
_MscGsmBcFramerFrmToIf_Type = Counter32
_MscGsmBcFramerFrmToIf_Object = MibTableColumn
mscGsmBcFramerFrmToIf = _MscGsmBcFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11, 1, 1),
    _MscGsmBcFramerFrmToIf_Type()
)
mscGsmBcFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerFrmToIf.setStatus("mandatory")
_MscGsmBcFramerFrmFromIf_Type = Counter32
_MscGsmBcFramerFrmFromIf_Object = MibTableColumn
mscGsmBcFramerFrmFromIf = _MscGsmBcFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11, 1, 2),
    _MscGsmBcFramerFrmFromIf_Type()
)
mscGsmBcFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerFrmFromIf.setStatus("mandatory")
_MscGsmBcFramerOctetFromIf_Type = Counter32
_MscGsmBcFramerOctetFromIf_Object = MibTableColumn
mscGsmBcFramerOctetFromIf = _MscGsmBcFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11, 1, 3),
    _MscGsmBcFramerOctetFromIf_Type()
)
mscGsmBcFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerOctetFromIf.setStatus("mandatory")
_MscGsmBcFramerCrcErrors_Type = Counter32
_MscGsmBcFramerCrcErrors_Object = MibTableColumn
mscGsmBcFramerCrcErrors = _MscGsmBcFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11, 1, 5),
    _MscGsmBcFramerCrcErrors_Type()
)
mscGsmBcFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerCrcErrors.setStatus("mandatory")
_MscGsmBcFramerLrcErrors_Type = Counter32
_MscGsmBcFramerLrcErrors_Object = MibTableColumn
mscGsmBcFramerLrcErrors = _MscGsmBcFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11, 1, 6),
    _MscGsmBcFramerLrcErrors_Type()
)
mscGsmBcFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerLrcErrors.setStatus("mandatory")
_MscGsmBcFramerNonOctetErrors_Type = Counter32
_MscGsmBcFramerNonOctetErrors_Object = MibTableColumn
mscGsmBcFramerNonOctetErrors = _MscGsmBcFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11, 1, 7),
    _MscGsmBcFramerNonOctetErrors_Type()
)
mscGsmBcFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerNonOctetErrors.setStatus("mandatory")
_MscGsmBcFramerOverruns_Type = Counter32
_MscGsmBcFramerOverruns_Object = MibTableColumn
mscGsmBcFramerOverruns = _MscGsmBcFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11, 1, 8),
    _MscGsmBcFramerOverruns_Type()
)
mscGsmBcFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerOverruns.setStatus("mandatory")
_MscGsmBcFramerUnderruns_Type = Counter32
_MscGsmBcFramerUnderruns_Object = MibTableColumn
mscGsmBcFramerUnderruns = _MscGsmBcFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 11, 1, 9),
    _MscGsmBcFramerUnderruns_Type()
)
mscGsmBcFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerUnderruns.setStatus("mandatory")
_MscGsmBcFramerLinkTable_Object = MibTable
mscGsmBcFramerLinkTable = _MscGsmBcFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 12)
)
if mibBuilder.loadTexts:
    mscGsmBcFramerLinkTable.setStatus("mandatory")
_MscGsmBcFramerLinkEntry_Object = MibTableRow
mscGsmBcFramerLinkEntry = _MscGsmBcFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 12, 1)
)
mscGsmBcFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcFramerLinkEntry.setStatus("mandatory")


class _MscGsmBcFramerFramingType_Type(Integer32):
    """Custom type mscGsmBcFramerFramingType based on Integer32"""
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


_MscGsmBcFramerFramingType_Type.__name__ = "Integer32"
_MscGsmBcFramerFramingType_Object = MibTableColumn
mscGsmBcFramerFramingType = _MscGsmBcFramerFramingType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 12, 1, 1),
    _MscGsmBcFramerFramingType_Type()
)
mscGsmBcFramerFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmBcFramerFramingType.setStatus("mandatory")
_MscGsmBcFramerStateTable_Object = MibTable
mscGsmBcFramerStateTable = _MscGsmBcFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 13)
)
if mibBuilder.loadTexts:
    mscGsmBcFramerStateTable.setStatus("mandatory")
_MscGsmBcFramerStateEntry_Object = MibTableRow
mscGsmBcFramerStateEntry = _MscGsmBcFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 13, 1)
)
mscGsmBcFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcFramerIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcFramerStateEntry.setStatus("mandatory")


class _MscGsmBcFramerAdminState_Type(Integer32):
    """Custom type mscGsmBcFramerAdminState based on Integer32"""
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


_MscGsmBcFramerAdminState_Type.__name__ = "Integer32"
_MscGsmBcFramerAdminState_Object = MibTableColumn
mscGsmBcFramerAdminState = _MscGsmBcFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 13, 1, 1),
    _MscGsmBcFramerAdminState_Type()
)
mscGsmBcFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerAdminState.setStatus("mandatory")


class _MscGsmBcFramerOperationalState_Type(Integer32):
    """Custom type mscGsmBcFramerOperationalState based on Integer32"""
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


_MscGsmBcFramerOperationalState_Type.__name__ = "Integer32"
_MscGsmBcFramerOperationalState_Object = MibTableColumn
mscGsmBcFramerOperationalState = _MscGsmBcFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 13, 1, 2),
    _MscGsmBcFramerOperationalState_Type()
)
mscGsmBcFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerOperationalState.setStatus("mandatory")


class _MscGsmBcFramerUsageState_Type(Integer32):
    """Custom type mscGsmBcFramerUsageState based on Integer32"""
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


_MscGsmBcFramerUsageState_Type.__name__ = "Integer32"
_MscGsmBcFramerUsageState_Object = MibTableColumn
mscGsmBcFramerUsageState = _MscGsmBcFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 2, 13, 1, 3),
    _MscGsmBcFramerUsageState_Type()
)
mscGsmBcFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFramerUsageState.setStatus("mandatory")
_MscGsmBcLayer1_ObjectIdentity = ObjectIdentity
mscGsmBcLayer1 = _MscGsmBcLayer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3)
)
_MscGsmBcLayer1RowStatusTable_Object = MibTable
mscGsmBcLayer1RowStatusTable = _MscGsmBcLayer1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcLayer1RowStatusTable.setStatus("mandatory")
_MscGsmBcLayer1RowStatusEntry_Object = MibTableRow
mscGsmBcLayer1RowStatusEntry = _MscGsmBcLayer1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 1, 1)
)
mscGsmBcLayer1RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcLayer1Index"),
)
if mibBuilder.loadTexts:
    mscGsmBcLayer1RowStatusEntry.setStatus("mandatory")
_MscGsmBcLayer1RowStatus_Type = RowStatus
_MscGsmBcLayer1RowStatus_Object = MibTableColumn
mscGsmBcLayer1RowStatus = _MscGsmBcLayer1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 1, 1, 1),
    _MscGsmBcLayer1RowStatus_Type()
)
mscGsmBcLayer1RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1RowStatus.setStatus("mandatory")
_MscGsmBcLayer1ComponentName_Type = DisplayString
_MscGsmBcLayer1ComponentName_Object = MibTableColumn
mscGsmBcLayer1ComponentName = _MscGsmBcLayer1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 1, 1, 2),
    _MscGsmBcLayer1ComponentName_Type()
)
mscGsmBcLayer1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1ComponentName.setStatus("mandatory")
_MscGsmBcLayer1StorageType_Type = StorageType
_MscGsmBcLayer1StorageType_Object = MibTableColumn
mscGsmBcLayer1StorageType = _MscGsmBcLayer1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 1, 1, 4),
    _MscGsmBcLayer1StorageType_Type()
)
mscGsmBcLayer1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1StorageType.setStatus("mandatory")
_MscGsmBcLayer1Index_Type = NonReplicated
_MscGsmBcLayer1Index_Object = MibTableColumn
mscGsmBcLayer1Index = _MscGsmBcLayer1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 1, 1, 10),
    _MscGsmBcLayer1Index_Type()
)
mscGsmBcLayer1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcLayer1Index.setStatus("mandatory")
_MscGsmBcLayer1OperTable_Object = MibTable
mscGsmBcLayer1OperTable = _MscGsmBcLayer1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcLayer1OperTable.setStatus("mandatory")
_MscGsmBcLayer1OperEntry_Object = MibTableRow
mscGsmBcLayer1OperEntry = _MscGsmBcLayer1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 10, 1)
)
mscGsmBcLayer1OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcLayer1Index"),
)
if mibBuilder.loadTexts:
    mscGsmBcLayer1OperEntry.setStatus("mandatory")


class _MscGsmBcLayer1ActiveMode_Type(Integer32):
    """Custom type mscGsmBcLayer1ActiveMode based on Integer32"""
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


_MscGsmBcLayer1ActiveMode_Type.__name__ = "Integer32"
_MscGsmBcLayer1ActiveMode_Object = MibTableColumn
mscGsmBcLayer1ActiveMode = _MscGsmBcLayer1ActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 10, 1, 1),
    _MscGsmBcLayer1ActiveMode_Type()
)
mscGsmBcLayer1ActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1ActiveMode.setStatus("mandatory")


class _MscGsmBcLayer1Connection_Type(Integer32):
    """Custom type mscGsmBcLayer1Connection based on Integer32"""
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


_MscGsmBcLayer1Connection_Type.__name__ = "Integer32"
_MscGsmBcLayer1Connection_Object = MibTableColumn
mscGsmBcLayer1Connection = _MscGsmBcLayer1Connection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 10, 1, 2),
    _MscGsmBcLayer1Connection_Type()
)
mscGsmBcLayer1Connection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1Connection.setStatus("mandatory")


class _MscGsmBcLayer1DataRate_Type(Unsigned32):
    """Custom type mscGsmBcLayer1DataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_MscGsmBcLayer1DataRate_Type.__name__ = "Unsigned32"
_MscGsmBcLayer1DataRate_Object = MibTableColumn
mscGsmBcLayer1DataRate = _MscGsmBcLayer1DataRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 10, 1, 3),
    _MscGsmBcLayer1DataRate_Type()
)
mscGsmBcLayer1DataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1DataRate.setStatus("mandatory")


class _MscGsmBcLayer1IntermediateRate_Type(Unsigned32):
    """Custom type mscGsmBcLayer1IntermediateRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
    )


_MscGsmBcLayer1IntermediateRate_Type.__name__ = "Unsigned32"
_MscGsmBcLayer1IntermediateRate_Object = MibTableColumn
mscGsmBcLayer1IntermediateRate = _MscGsmBcLayer1IntermediateRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 10, 1, 10),
    _MscGsmBcLayer1IntermediateRate_Type()
)
mscGsmBcLayer1IntermediateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1IntermediateRate.setStatus("mandatory")
_MscGsmBcLayer1StatsTable_Object = MibTable
mscGsmBcLayer1StatsTable = _MscGsmBcLayer1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcLayer1StatsTable.setStatus("mandatory")
_MscGsmBcLayer1StatsEntry_Object = MibTableRow
mscGsmBcLayer1StatsEntry = _MscGsmBcLayer1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1)
)
mscGsmBcLayer1StatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcLayer1Index"),
)
if mibBuilder.loadTexts:
    mscGsmBcLayer1StatsEntry.setStatus("mandatory")
_MscGsmBcLayer1FramesTx_Type = Counter32
_MscGsmBcLayer1FramesTx_Object = MibTableColumn
mscGsmBcLayer1FramesTx = _MscGsmBcLayer1FramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 1),
    _MscGsmBcLayer1FramesTx_Type()
)
mscGsmBcLayer1FramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1FramesTx.setStatus("mandatory")
_MscGsmBcLayer1FramesRx_Type = Counter32
_MscGsmBcLayer1FramesRx_Object = MibTableColumn
mscGsmBcLayer1FramesRx = _MscGsmBcLayer1FramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 2),
    _MscGsmBcLayer1FramesRx_Type()
)
mscGsmBcLayer1FramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1FramesRx.setStatus("mandatory")
_MscGsmBcLayer1BytesTx_Type = Counter32
_MscGsmBcLayer1BytesTx_Object = MibTableColumn
mscGsmBcLayer1BytesTx = _MscGsmBcLayer1BytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 3),
    _MscGsmBcLayer1BytesTx_Type()
)
mscGsmBcLayer1BytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1BytesTx.setStatus("mandatory")
_MscGsmBcLayer1BytesRx_Type = Counter32
_MscGsmBcLayer1BytesRx_Object = MibTableColumn
mscGsmBcLayer1BytesRx = _MscGsmBcLayer1BytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 4),
    _MscGsmBcLayer1BytesRx_Type()
)
mscGsmBcLayer1BytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1BytesRx.setStatus("mandatory")
_MscGsmBcLayer1UnderRunsTx_Type = Counter32
_MscGsmBcLayer1UnderRunsTx_Object = MibTableColumn
mscGsmBcLayer1UnderRunsTx = _MscGsmBcLayer1UnderRunsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 5),
    _MscGsmBcLayer1UnderRunsTx_Type()
)
mscGsmBcLayer1UnderRunsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1UnderRunsTx.setStatus("mandatory")
_MscGsmBcLayer1OverRunsRx_Type = Counter32
_MscGsmBcLayer1OverRunsRx_Object = MibTableColumn
mscGsmBcLayer1OverRunsRx = _MscGsmBcLayer1OverRunsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 6),
    _MscGsmBcLayer1OverRunsRx_Type()
)
mscGsmBcLayer1OverRunsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1OverRunsRx.setStatus("mandatory")
_MscGsmBcLayer1NonOctetErrorsRx_Type = Counter32
_MscGsmBcLayer1NonOctetErrorsRx_Object = MibTableColumn
mscGsmBcLayer1NonOctetErrorsRx = _MscGsmBcLayer1NonOctetErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 7),
    _MscGsmBcLayer1NonOctetErrorsRx_Type()
)
mscGsmBcLayer1NonOctetErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1NonOctetErrorsRx.setStatus("mandatory")
_MscGsmBcLayer1LargeFrameErrorsRx_Type = Counter32
_MscGsmBcLayer1LargeFrameErrorsRx_Object = MibTableColumn
mscGsmBcLayer1LargeFrameErrorsRx = _MscGsmBcLayer1LargeFrameErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 8),
    _MscGsmBcLayer1LargeFrameErrorsRx_Type()
)
mscGsmBcLayer1LargeFrameErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1LargeFrameErrorsRx.setStatus("mandatory")
_MscGsmBcLayer1FramesDiscarded_Type = Counter32
_MscGsmBcLayer1FramesDiscarded_Object = MibTableColumn
mscGsmBcLayer1FramesDiscarded = _MscGsmBcLayer1FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 9),
    _MscGsmBcLayer1FramesDiscarded_Type()
)
mscGsmBcLayer1FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1FramesDiscarded.setStatus("mandatory")
_MscGsmBcLayer1LrcErrorsTx_Type = Counter32
_MscGsmBcLayer1LrcErrorsTx_Object = MibTableColumn
mscGsmBcLayer1LrcErrorsTx = _MscGsmBcLayer1LrcErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 3, 11, 1, 10),
    _MscGsmBcLayer1LrcErrorsTx_Type()
)
mscGsmBcLayer1LrcErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLayer1LrcErrorsTx.setStatus("mandatory")
_MscGsmBcModem_ObjectIdentity = ObjectIdentity
mscGsmBcModem = _MscGsmBcModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4)
)
_MscGsmBcModemRowStatusTable_Object = MibTable
mscGsmBcModemRowStatusTable = _MscGsmBcModemRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcModemRowStatusTable.setStatus("mandatory")
_MscGsmBcModemRowStatusEntry_Object = MibTableRow
mscGsmBcModemRowStatusEntry = _MscGsmBcModemRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 1, 1)
)
mscGsmBcModemRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcModemIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcModemRowStatusEntry.setStatus("mandatory")
_MscGsmBcModemRowStatus_Type = RowStatus
_MscGsmBcModemRowStatus_Object = MibTableColumn
mscGsmBcModemRowStatus = _MscGsmBcModemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 1, 1, 1),
    _MscGsmBcModemRowStatus_Type()
)
mscGsmBcModemRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemRowStatus.setStatus("mandatory")
_MscGsmBcModemComponentName_Type = DisplayString
_MscGsmBcModemComponentName_Object = MibTableColumn
mscGsmBcModemComponentName = _MscGsmBcModemComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 1, 1, 2),
    _MscGsmBcModemComponentName_Type()
)
mscGsmBcModemComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemComponentName.setStatus("mandatory")
_MscGsmBcModemStorageType_Type = StorageType
_MscGsmBcModemStorageType_Object = MibTableColumn
mscGsmBcModemStorageType = _MscGsmBcModemStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 1, 1, 4),
    _MscGsmBcModemStorageType_Type()
)
mscGsmBcModemStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemStorageType.setStatus("mandatory")
_MscGsmBcModemIndex_Type = NonReplicated
_MscGsmBcModemIndex_Object = MibTableColumn
mscGsmBcModemIndex = _MscGsmBcModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 1, 1, 10),
    _MscGsmBcModemIndex_Type()
)
mscGsmBcModemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcModemIndex.setStatus("mandatory")
_MscGsmBcModemOperTable_Object = MibTable
mscGsmBcModemOperTable = _MscGsmBcModemOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcModemOperTable.setStatus("mandatory")
_MscGsmBcModemOperEntry_Object = MibTableRow
mscGsmBcModemOperEntry = _MscGsmBcModemOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1)
)
mscGsmBcModemOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcModemIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcModemOperEntry.setStatus("mandatory")


class _MscGsmBcModemRate_Type(Integer32):
    """Custom type mscGsmBcModemRate based on Integer32"""
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


_MscGsmBcModemRate_Type.__name__ = "Integer32"
_MscGsmBcModemRate_Object = MibTableColumn
mscGsmBcModemRate = _MscGsmBcModemRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 2),
    _MscGsmBcModemRate_Type()
)
mscGsmBcModemRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemRate.setStatus("mandatory")


class _MscGsmBcModemAlgorithmInUse_Type(OctetString):
    """Custom type mscGsmBcModemAlgorithmInUse based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscGsmBcModemAlgorithmInUse_Type.__name__ = "OctetString"
_MscGsmBcModemAlgorithmInUse_Object = MibTableColumn
mscGsmBcModemAlgorithmInUse = _MscGsmBcModemAlgorithmInUse_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 3),
    _MscGsmBcModemAlgorithmInUse_Type()
)
mscGsmBcModemAlgorithmInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemAlgorithmInUse.setStatus("mandatory")


class _MscGsmBcModemProtocolState_Type(Integer32):
    """Custom type mscGsmBcModemProtocolState based on Integer32"""
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


_MscGsmBcModemProtocolState_Type.__name__ = "Integer32"
_MscGsmBcModemProtocolState_Object = MibTableColumn
mscGsmBcModemProtocolState = _MscGsmBcModemProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 4),
    _MscGsmBcModemProtocolState_Type()
)
mscGsmBcModemProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemProtocolState.setStatus("mandatory")


class _MscGsmBcModemReceiverTransmitter_Type(Integer32):
    """Custom type mscGsmBcModemReceiverTransmitter based on Integer32"""
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


_MscGsmBcModemReceiverTransmitter_Type.__name__ = "Integer32"
_MscGsmBcModemReceiverTransmitter_Object = MibTableColumn
mscGsmBcModemReceiverTransmitter = _MscGsmBcModemReceiverTransmitter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 5),
    _MscGsmBcModemReceiverTransmitter_Type()
)
mscGsmBcModemReceiverTransmitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemReceiverTransmitter.setStatus("mandatory")


class _MscGsmBcModemTraining_Type(Integer32):
    """Custom type mscGsmBcModemTraining based on Integer32"""
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


_MscGsmBcModemTraining_Type.__name__ = "Integer32"
_MscGsmBcModemTraining_Object = MibTableColumn
mscGsmBcModemTraining = _MscGsmBcModemTraining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 6),
    _MscGsmBcModemTraining_Type()
)
mscGsmBcModemTraining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemTraining.setStatus("mandatory")


class _MscGsmBcModemToUpperFlowControlActive_Type(Integer32):
    """Custom type mscGsmBcModemToUpperFlowControlActive based on Integer32"""
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


_MscGsmBcModemToUpperFlowControlActive_Type.__name__ = "Integer32"
_MscGsmBcModemToUpperFlowControlActive_Object = MibTableColumn
mscGsmBcModemToUpperFlowControlActive = _MscGsmBcModemToUpperFlowControlActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 8),
    _MscGsmBcModemToUpperFlowControlActive_Type()
)
mscGsmBcModemToUpperFlowControlActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemToUpperFlowControlActive.setStatus("mandatory")


class _MscGsmBcModemToDspFlowControlActive_Type(Integer32):
    """Custom type mscGsmBcModemToDspFlowControlActive based on Integer32"""
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


_MscGsmBcModemToDspFlowControlActive_Type.__name__ = "Integer32"
_MscGsmBcModemToDspFlowControlActive_Object = MibTableColumn
mscGsmBcModemToDspFlowControlActive = _MscGsmBcModemToDspFlowControlActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 9),
    _MscGsmBcModemToDspFlowControlActive_Type()
)
mscGsmBcModemToDspFlowControlActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemToDspFlowControlActive.setStatus("mandatory")


class _MscGsmBcModemAsyncMode_Type(Integer32):
    """Custom type mscGsmBcModemAsyncMode based on Integer32"""
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


_MscGsmBcModemAsyncMode_Type.__name__ = "Integer32"
_MscGsmBcModemAsyncMode_Object = MibTableColumn
mscGsmBcModemAsyncMode = _MscGsmBcModemAsyncMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 10),
    _MscGsmBcModemAsyncMode_Type()
)
mscGsmBcModemAsyncMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemAsyncMode.setStatus("mandatory")


class _MscGsmBcModemAutoHdlcMode_Type(Integer32):
    """Custom type mscGsmBcModemAutoHdlcMode based on Integer32"""
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


_MscGsmBcModemAutoHdlcMode_Type.__name__ = "Integer32"
_MscGsmBcModemAutoHdlcMode_Object = MibTableColumn
mscGsmBcModemAutoHdlcMode = _MscGsmBcModemAutoHdlcMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 11),
    _MscGsmBcModemAutoHdlcMode_Type()
)
mscGsmBcModemAutoHdlcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemAutoHdlcMode.setStatus("mandatory")


class _MscGsmBcModemOutbandFlowControl_Type(Integer32):
    """Custom type mscGsmBcModemOutbandFlowControl based on Integer32"""
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


_MscGsmBcModemOutbandFlowControl_Type.__name__ = "Integer32"
_MscGsmBcModemOutbandFlowControl_Object = MibTableColumn
mscGsmBcModemOutbandFlowControl = _MscGsmBcModemOutbandFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 12),
    _MscGsmBcModemOutbandFlowControl_Type()
)
mscGsmBcModemOutbandFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemOutbandFlowControl.setStatus("mandatory")


class _MscGsmBcModemOutbandBreak_Type(Integer32):
    """Custom type mscGsmBcModemOutbandBreak based on Integer32"""
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


_MscGsmBcModemOutbandBreak_Type.__name__ = "Integer32"
_MscGsmBcModemOutbandBreak_Object = MibTableColumn
mscGsmBcModemOutbandBreak = _MscGsmBcModemOutbandBreak_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 13),
    _MscGsmBcModemOutbandBreak_Type()
)
mscGsmBcModemOutbandBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemOutbandBreak.setStatus("mandatory")


class _MscGsmBcModemAutobaud_Type(Integer32):
    """Custom type mscGsmBcModemAutobaud based on Integer32"""
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


_MscGsmBcModemAutobaud_Type.__name__ = "Integer32"
_MscGsmBcModemAutobaud_Object = MibTableColumn
mscGsmBcModemAutobaud = _MscGsmBcModemAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 10, 1, 14),
    _MscGsmBcModemAutobaud_Type()
)
mscGsmBcModemAutobaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemAutobaud.setStatus("mandatory")
_MscGsmBcModemStatsTable_Object = MibTable
mscGsmBcModemStatsTable = _MscGsmBcModemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcModemStatsTable.setStatus("mandatory")
_MscGsmBcModemStatsEntry_Object = MibTableRow
mscGsmBcModemStatsEntry = _MscGsmBcModemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 11, 1)
)
mscGsmBcModemStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcModemIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcModemStatsEntry.setStatus("mandatory")
_MscGsmBcModemBytesTx_Type = Counter32
_MscGsmBcModemBytesTx_Object = MibTableColumn
mscGsmBcModemBytesTx = _MscGsmBcModemBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 11, 1, 1),
    _MscGsmBcModemBytesTx_Type()
)
mscGsmBcModemBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemBytesTx.setStatus("mandatory")
_MscGsmBcModemBytesRx_Type = Counter32
_MscGsmBcModemBytesRx_Object = MibTableColumn
mscGsmBcModemBytesRx = _MscGsmBcModemBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 11, 1, 2),
    _MscGsmBcModemBytesRx_Type()
)
mscGsmBcModemBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemBytesRx.setStatus("mandatory")
_MscGsmBcModemFramingErrors_Type = Counter32
_MscGsmBcModemFramingErrors_Object = MibTableColumn
mscGsmBcModemFramingErrors = _MscGsmBcModemFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 4, 11, 1, 6),
    _MscGsmBcModemFramingErrors_Type()
)
mscGsmBcModemFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcModemFramingErrors.setStatus("mandatory")
_MscGsmBcV110_ObjectIdentity = ObjectIdentity
mscGsmBcV110 = _MscGsmBcV110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5)
)
_MscGsmBcV110RowStatusTable_Object = MibTable
mscGsmBcV110RowStatusTable = _MscGsmBcV110RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcV110RowStatusTable.setStatus("mandatory")
_MscGsmBcV110RowStatusEntry_Object = MibTableRow
mscGsmBcV110RowStatusEntry = _MscGsmBcV110RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 1, 1)
)
mscGsmBcV110RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcV110Index"),
)
if mibBuilder.loadTexts:
    mscGsmBcV110RowStatusEntry.setStatus("mandatory")
_MscGsmBcV110RowStatus_Type = RowStatus
_MscGsmBcV110RowStatus_Object = MibTableColumn
mscGsmBcV110RowStatus = _MscGsmBcV110RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 1, 1, 1),
    _MscGsmBcV110RowStatus_Type()
)
mscGsmBcV110RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110RowStatus.setStatus("mandatory")
_MscGsmBcV110ComponentName_Type = DisplayString
_MscGsmBcV110ComponentName_Object = MibTableColumn
mscGsmBcV110ComponentName = _MscGsmBcV110ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 1, 1, 2),
    _MscGsmBcV110ComponentName_Type()
)
mscGsmBcV110ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110ComponentName.setStatus("mandatory")
_MscGsmBcV110StorageType_Type = StorageType
_MscGsmBcV110StorageType_Object = MibTableColumn
mscGsmBcV110StorageType = _MscGsmBcV110StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 1, 1, 4),
    _MscGsmBcV110StorageType_Type()
)
mscGsmBcV110StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110StorageType.setStatus("mandatory")
_MscGsmBcV110Index_Type = NonReplicated
_MscGsmBcV110Index_Object = MibTableColumn
mscGsmBcV110Index = _MscGsmBcV110Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 1, 1, 10),
    _MscGsmBcV110Index_Type()
)
mscGsmBcV110Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcV110Index.setStatus("mandatory")
_MscGsmBcV110OperTable_Object = MibTable
mscGsmBcV110OperTable = _MscGsmBcV110OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcV110OperTable.setStatus("mandatory")
_MscGsmBcV110OperEntry_Object = MibTableRow
mscGsmBcV110OperEntry = _MscGsmBcV110OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 10, 1)
)
mscGsmBcV110OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcV110Index"),
)
if mibBuilder.loadTexts:
    mscGsmBcV110OperEntry.setStatus("mandatory")


class _MscGsmBcV110DataRate_Type(Unsigned32):
    """Custom type mscGsmBcV110DataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_MscGsmBcV110DataRate_Type.__name__ = "Unsigned32"
_MscGsmBcV110DataRate_Object = MibTableColumn
mscGsmBcV110DataRate = _MscGsmBcV110DataRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 10, 1, 2),
    _MscGsmBcV110DataRate_Type()
)
mscGsmBcV110DataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110DataRate.setStatus("mandatory")


class _MscGsmBcV110IntermediateRate_Type(Integer32):
    """Custom type mscGsmBcV110IntermediateRate based on Integer32"""
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


_MscGsmBcV110IntermediateRate_Type.__name__ = "Integer32"
_MscGsmBcV110IntermediateRate_Object = MibTableColumn
mscGsmBcV110IntermediateRate = _MscGsmBcV110IntermediateRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 10, 1, 9),
    _MscGsmBcV110IntermediateRate_Type()
)
mscGsmBcV110IntermediateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110IntermediateRate.setStatus("mandatory")
_MscGsmBcV110StatsTable_Object = MibTable
mscGsmBcV110StatsTable = _MscGsmBcV110StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcV110StatsTable.setStatus("mandatory")
_MscGsmBcV110StatsEntry_Object = MibTableRow
mscGsmBcV110StatsEntry = _MscGsmBcV110StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1)
)
mscGsmBcV110StatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcV110Index"),
)
if mibBuilder.loadTexts:
    mscGsmBcV110StatsEntry.setStatus("mandatory")
_MscGsmBcV110FramesTx_Type = Counter32
_MscGsmBcV110FramesTx_Object = MibTableColumn
mscGsmBcV110FramesTx = _MscGsmBcV110FramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 1),
    _MscGsmBcV110FramesTx_Type()
)
mscGsmBcV110FramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110FramesTx.setStatus("mandatory")
_MscGsmBcV110FramesRx_Type = Counter32
_MscGsmBcV110FramesRx_Object = MibTableColumn
mscGsmBcV110FramesRx = _MscGsmBcV110FramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 2),
    _MscGsmBcV110FramesRx_Type()
)
mscGsmBcV110FramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110FramesRx.setStatus("mandatory")
_MscGsmBcV110BytesTx_Type = Counter32
_MscGsmBcV110BytesTx_Object = MibTableColumn
mscGsmBcV110BytesTx = _MscGsmBcV110BytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 3),
    _MscGsmBcV110BytesTx_Type()
)
mscGsmBcV110BytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110BytesTx.setStatus("mandatory")
_MscGsmBcV110BytesRx_Type = Counter32
_MscGsmBcV110BytesRx_Object = MibTableColumn
mscGsmBcV110BytesRx = _MscGsmBcV110BytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 4),
    _MscGsmBcV110BytesRx_Type()
)
mscGsmBcV110BytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110BytesRx.setStatus("mandatory")
_MscGsmBcV110UnderRunsTx_Type = Counter32
_MscGsmBcV110UnderRunsTx_Object = MibTableColumn
mscGsmBcV110UnderRunsTx = _MscGsmBcV110UnderRunsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 5),
    _MscGsmBcV110UnderRunsTx_Type()
)
mscGsmBcV110UnderRunsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110UnderRunsTx.setStatus("mandatory")
_MscGsmBcV110OverRunsRx_Type = Counter32
_MscGsmBcV110OverRunsRx_Object = MibTableColumn
mscGsmBcV110OverRunsRx = _MscGsmBcV110OverRunsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 6),
    _MscGsmBcV110OverRunsRx_Type()
)
mscGsmBcV110OverRunsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110OverRunsRx.setStatus("mandatory")
_MscGsmBcV110NonOctetErrorsRx_Type = Counter32
_MscGsmBcV110NonOctetErrorsRx_Object = MibTableColumn
mscGsmBcV110NonOctetErrorsRx = _MscGsmBcV110NonOctetErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 7),
    _MscGsmBcV110NonOctetErrorsRx_Type()
)
mscGsmBcV110NonOctetErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110NonOctetErrorsRx.setStatus("mandatory")
_MscGsmBcV110LargeFrameErrorsRx_Type = Counter32
_MscGsmBcV110LargeFrameErrorsRx_Object = MibTableColumn
mscGsmBcV110LargeFrameErrorsRx = _MscGsmBcV110LargeFrameErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 8),
    _MscGsmBcV110LargeFrameErrorsRx_Type()
)
mscGsmBcV110LargeFrameErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110LargeFrameErrorsRx.setStatus("mandatory")
_MscGsmBcV110FramesDiscarded_Type = Counter32
_MscGsmBcV110FramesDiscarded_Object = MibTableColumn
mscGsmBcV110FramesDiscarded = _MscGsmBcV110FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 9),
    _MscGsmBcV110FramesDiscarded_Type()
)
mscGsmBcV110FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110FramesDiscarded.setStatus("mandatory")
_MscGsmBcV110LrcErrorsTx_Type = Counter32
_MscGsmBcV110LrcErrorsTx_Object = MibTableColumn
mscGsmBcV110LrcErrorsTx = _MscGsmBcV110LrcErrorsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 5, 11, 1, 10),
    _MscGsmBcV110LrcErrorsTx_Type()
)
mscGsmBcV110LrcErrorsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV110LrcErrorsTx.setStatus("mandatory")
_MscGsmBcFax_ObjectIdentity = ObjectIdentity
mscGsmBcFax = _MscGsmBcFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6)
)
_MscGsmBcFaxRowStatusTable_Object = MibTable
mscGsmBcFaxRowStatusTable = _MscGsmBcFaxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcFaxRowStatusTable.setStatus("mandatory")
_MscGsmBcFaxRowStatusEntry_Object = MibTableRow
mscGsmBcFaxRowStatusEntry = _MscGsmBcFaxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 1, 1)
)
mscGsmBcFaxRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcFaxIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcFaxRowStatusEntry.setStatus("mandatory")
_MscGsmBcFaxRowStatus_Type = RowStatus
_MscGsmBcFaxRowStatus_Object = MibTableColumn
mscGsmBcFaxRowStatus = _MscGsmBcFaxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 1, 1, 1),
    _MscGsmBcFaxRowStatus_Type()
)
mscGsmBcFaxRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxRowStatus.setStatus("mandatory")
_MscGsmBcFaxComponentName_Type = DisplayString
_MscGsmBcFaxComponentName_Object = MibTableColumn
mscGsmBcFaxComponentName = _MscGsmBcFaxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 1, 1, 2),
    _MscGsmBcFaxComponentName_Type()
)
mscGsmBcFaxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxComponentName.setStatus("mandatory")
_MscGsmBcFaxStorageType_Type = StorageType
_MscGsmBcFaxStorageType_Object = MibTableColumn
mscGsmBcFaxStorageType = _MscGsmBcFaxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 1, 1, 4),
    _MscGsmBcFaxStorageType_Type()
)
mscGsmBcFaxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxStorageType.setStatus("mandatory")
_MscGsmBcFaxIndex_Type = NonReplicated
_MscGsmBcFaxIndex_Object = MibTableColumn
mscGsmBcFaxIndex = _MscGsmBcFaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 1, 1, 10),
    _MscGsmBcFaxIndex_Type()
)
mscGsmBcFaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcFaxIndex.setStatus("mandatory")
_MscGsmBcFaxOperTable_Object = MibTable
mscGsmBcFaxOperTable = _MscGsmBcFaxOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcFaxOperTable.setStatus("mandatory")
_MscGsmBcFaxOperEntry_Object = MibTableRow
mscGsmBcFaxOperEntry = _MscGsmBcFaxOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 10, 1)
)
mscGsmBcFaxOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcFaxIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcFaxOperEntry.setStatus("mandatory")


class _MscGsmBcFaxActiveMode_Type(Integer32):
    """Custom type mscGsmBcFaxActiveMode based on Integer32"""
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


_MscGsmBcFaxActiveMode_Type.__name__ = "Integer32"
_MscGsmBcFaxActiveMode_Object = MibTableColumn
mscGsmBcFaxActiveMode = _MscGsmBcFaxActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 10, 1, 1),
    _MscGsmBcFaxActiveMode_Type()
)
mscGsmBcFaxActiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxActiveMode.setStatus("mandatory")


class _MscGsmBcFaxProtocolState_Type(Integer32):
    """Custom type mscGsmBcFaxProtocolState based on Integer32"""
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


_MscGsmBcFaxProtocolState_Type.__name__ = "Integer32"
_MscGsmBcFaxProtocolState_Object = MibTableColumn
mscGsmBcFaxProtocolState = _MscGsmBcFaxProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 10, 1, 2),
    _MscGsmBcFaxProtocolState_Type()
)
mscGsmBcFaxProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxProtocolState.setStatus("mandatory")


class _MscGsmBcFaxMessageRate_Type(Unsigned32):
    """Custom type mscGsmBcFaxMessageRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_MscGsmBcFaxMessageRate_Type.__name__ = "Unsigned32"
_MscGsmBcFaxMessageRate_Object = MibTableColumn
mscGsmBcFaxMessageRate = _MscGsmBcFaxMessageRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 10, 1, 3),
    _MscGsmBcFaxMessageRate_Type()
)
mscGsmBcFaxMessageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxMessageRate.setStatus("mandatory")
_MscGsmBcFaxStatsTable_Object = MibTable
mscGsmBcFaxStatsTable = _MscGsmBcFaxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcFaxStatsTable.setStatus("mandatory")
_MscGsmBcFaxStatsEntry_Object = MibTableRow
mscGsmBcFaxStatsEntry = _MscGsmBcFaxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11, 1)
)
mscGsmBcFaxStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcFaxIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcFaxStatsEntry.setStatus("mandatory")
_MscGsmBcFaxMessageFramesRx_Type = Counter32
_MscGsmBcFaxMessageFramesRx_Object = MibTableColumn
mscGsmBcFaxMessageFramesRx = _MscGsmBcFaxMessageFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11, 1, 1),
    _MscGsmBcFaxMessageFramesRx_Type()
)
mscGsmBcFaxMessageFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxMessageFramesRx.setStatus("mandatory")
_MscGsmBcFaxMessageFramesTx_Type = Counter32
_MscGsmBcFaxMessageFramesTx_Object = MibTableColumn
mscGsmBcFaxMessageFramesTx = _MscGsmBcFaxMessageFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11, 1, 2),
    _MscGsmBcFaxMessageFramesTx_Type()
)
mscGsmBcFaxMessageFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxMessageFramesTx.setStatus("mandatory")
_MscGsmBcFaxBcsFramesRx_Type = Counter32
_MscGsmBcFaxBcsFramesRx_Object = MibTableColumn
mscGsmBcFaxBcsFramesRx = _MscGsmBcFaxBcsFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11, 1, 3),
    _MscGsmBcFaxBcsFramesRx_Type()
)
mscGsmBcFaxBcsFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxBcsFramesRx.setStatus("mandatory")
_MscGsmBcFaxBcsFramesTx_Type = Counter32
_MscGsmBcFaxBcsFramesTx_Object = MibTableColumn
mscGsmBcFaxBcsFramesTx = _MscGsmBcFaxBcsFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11, 1, 4),
    _MscGsmBcFaxBcsFramesTx_Type()
)
mscGsmBcFaxBcsFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxBcsFramesTx.setStatus("mandatory")
_MscGsmBcFaxPagesRxFromMobile_Type = Counter32
_MscGsmBcFaxPagesRxFromMobile_Object = MibTableColumn
mscGsmBcFaxPagesRxFromMobile = _MscGsmBcFaxPagesRxFromMobile_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11, 1, 5),
    _MscGsmBcFaxPagesRxFromMobile_Type()
)
mscGsmBcFaxPagesRxFromMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxPagesRxFromMobile.setStatus("mandatory")
_MscGsmBcFaxPagesTxToMobile_Type = Counter32
_MscGsmBcFaxPagesTxToMobile_Object = MibTableColumn
mscGsmBcFaxPagesTxToMobile = _MscGsmBcFaxPagesTxToMobile_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11, 1, 6),
    _MscGsmBcFaxPagesTxToMobile_Type()
)
mscGsmBcFaxPagesTxToMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxPagesTxToMobile.setStatus("mandatory")
_MscGsmBcFaxChannelModeModify_Type = Counter32
_MscGsmBcFaxChannelModeModify_Object = MibTableColumn
mscGsmBcFaxChannelModeModify = _MscGsmBcFaxChannelModeModify_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11, 1, 7),
    _MscGsmBcFaxChannelModeModify_Type()
)
mscGsmBcFaxChannelModeModify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxChannelModeModify.setStatus("mandatory")
_MscGsmBcFaxBcsFrameErrors_Type = Counter32
_MscGsmBcFaxBcsFrameErrors_Object = MibTableColumn
mscGsmBcFaxBcsFrameErrors = _MscGsmBcFaxBcsFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 6, 11, 1, 8),
    _MscGsmBcFaxBcsFrameErrors_Type()
)
mscGsmBcFaxBcsFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFaxBcsFrameErrors.setStatus("mandatory")
_MscGsmBcRlp_ObjectIdentity = ObjectIdentity
mscGsmBcRlp = _MscGsmBcRlp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7)
)
_MscGsmBcRlpRowStatusTable_Object = MibTable
mscGsmBcRlpRowStatusTable = _MscGsmBcRlpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcRlpRowStatusTable.setStatus("mandatory")
_MscGsmBcRlpRowStatusEntry_Object = MibTableRow
mscGsmBcRlpRowStatusEntry = _MscGsmBcRlpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 1, 1)
)
mscGsmBcRlpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcRlpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcRlpRowStatusEntry.setStatus("mandatory")
_MscGsmBcRlpRowStatus_Type = RowStatus
_MscGsmBcRlpRowStatus_Object = MibTableColumn
mscGsmBcRlpRowStatus = _MscGsmBcRlpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 1, 1, 1),
    _MscGsmBcRlpRowStatus_Type()
)
mscGsmBcRlpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpRowStatus.setStatus("mandatory")
_MscGsmBcRlpComponentName_Type = DisplayString
_MscGsmBcRlpComponentName_Object = MibTableColumn
mscGsmBcRlpComponentName = _MscGsmBcRlpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 1, 1, 2),
    _MscGsmBcRlpComponentName_Type()
)
mscGsmBcRlpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpComponentName.setStatus("mandatory")
_MscGsmBcRlpStorageType_Type = StorageType
_MscGsmBcRlpStorageType_Object = MibTableColumn
mscGsmBcRlpStorageType = _MscGsmBcRlpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 1, 1, 4),
    _MscGsmBcRlpStorageType_Type()
)
mscGsmBcRlpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpStorageType.setStatus("mandatory")
_MscGsmBcRlpIndex_Type = NonReplicated
_MscGsmBcRlpIndex_Object = MibTableColumn
mscGsmBcRlpIndex = _MscGsmBcRlpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 1, 1, 10),
    _MscGsmBcRlpIndex_Type()
)
mscGsmBcRlpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcRlpIndex.setStatus("mandatory")
_MscGsmBcRlpOperTable_Object = MibTable
mscGsmBcRlpOperTable = _MscGsmBcRlpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcRlpOperTable.setStatus("mandatory")
_MscGsmBcRlpOperEntry_Object = MibTableRow
mscGsmBcRlpOperEntry = _MscGsmBcRlpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10, 1)
)
mscGsmBcRlpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcRlpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcRlpOperEntry.setStatus("mandatory")


class _MscGsmBcRlpProtocolState_Type(Integer32):
    """Custom type mscGsmBcRlpProtocolState based on Integer32"""
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


_MscGsmBcRlpProtocolState_Type.__name__ = "Integer32"
_MscGsmBcRlpProtocolState_Object = MibTableColumn
mscGsmBcRlpProtocolState = _MscGsmBcRlpProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10, 1, 1),
    _MscGsmBcRlpProtocolState_Type()
)
mscGsmBcRlpProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpProtocolState.setStatus("mandatory")


class _MscGsmBcRlpFrameSize_Type(Unsigned32):
    """Custom type mscGsmBcRlpFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_MscGsmBcRlpFrameSize_Type.__name__ = "Unsigned32"
_MscGsmBcRlpFrameSize_Object = MibTableColumn
mscGsmBcRlpFrameSize = _MscGsmBcRlpFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10, 1, 2),
    _MscGsmBcRlpFrameSize_Type()
)
mscGsmBcRlpFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpFrameSize.setStatus("mandatory")


class _MscGsmBcRlpHighestVersion_Type(Unsigned32):
    """Custom type mscGsmBcRlpHighestVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscGsmBcRlpHighestVersion_Type.__name__ = "Unsigned32"
_MscGsmBcRlpHighestVersion_Object = MibTableColumn
mscGsmBcRlpHighestVersion = _MscGsmBcRlpHighestVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10, 1, 3),
    _MscGsmBcRlpHighestVersion_Type()
)
mscGsmBcRlpHighestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpHighestVersion.setStatus("mandatory")


class _MscGsmBcRlpIwfToMsWindowSize_Type(Unsigned32):
    """Custom type mscGsmBcRlpIwfToMsWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61),
    )


_MscGsmBcRlpIwfToMsWindowSize_Type.__name__ = "Unsigned32"
_MscGsmBcRlpIwfToMsWindowSize_Object = MibTableColumn
mscGsmBcRlpIwfToMsWindowSize = _MscGsmBcRlpIwfToMsWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10, 1, 4),
    _MscGsmBcRlpIwfToMsWindowSize_Type()
)
mscGsmBcRlpIwfToMsWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpIwfToMsWindowSize.setStatus("mandatory")


class _MscGsmBcRlpMsToIwfWindowSize_Type(Unsigned32):
    """Custom type mscGsmBcRlpMsToIwfWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61),
    )


_MscGsmBcRlpMsToIwfWindowSize_Type.__name__ = "Unsigned32"
_MscGsmBcRlpMsToIwfWindowSize_Object = MibTableColumn
mscGsmBcRlpMsToIwfWindowSize = _MscGsmBcRlpMsToIwfWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10, 1, 5),
    _MscGsmBcRlpMsToIwfWindowSize_Type()
)
mscGsmBcRlpMsToIwfWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpMsToIwfWindowSize.setStatus("mandatory")


class _MscGsmBcRlpT1AckTimer_Type(Unsigned32):
    """Custom type mscGsmBcRlpT1AckTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(380, 1020),
    )


_MscGsmBcRlpT1AckTimer_Type.__name__ = "Unsigned32"
_MscGsmBcRlpT1AckTimer_Object = MibTableColumn
mscGsmBcRlpT1AckTimer = _MscGsmBcRlpT1AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10, 1, 6),
    _MscGsmBcRlpT1AckTimer_Type()
)
mscGsmBcRlpT1AckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpT1AckTimer.setStatus("mandatory")


class _MscGsmBcRlpT2AckDelayTimer_Type(Unsigned32):
    """Custom type mscGsmBcRlpT2AckDelayTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 70),
    )


_MscGsmBcRlpT2AckDelayTimer_Type.__name__ = "Unsigned32"
_MscGsmBcRlpT2AckDelayTimer_Object = MibTableColumn
mscGsmBcRlpT2AckDelayTimer = _MscGsmBcRlpT2AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10, 1, 7),
    _MscGsmBcRlpT2AckDelayTimer_Type()
)
mscGsmBcRlpT2AckDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpT2AckDelayTimer.setStatus("mandatory")


class _MscGsmBcRlpN2RetransmitCount_Type(Unsigned32):
    """Custom type mscGsmBcRlpN2RetransmitCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscGsmBcRlpN2RetransmitCount_Type.__name__ = "Unsigned32"
_MscGsmBcRlpN2RetransmitCount_Object = MibTableColumn
mscGsmBcRlpN2RetransmitCount = _MscGsmBcRlpN2RetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 10, 1, 8),
    _MscGsmBcRlpN2RetransmitCount_Type()
)
mscGsmBcRlpN2RetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmBcRlpN2RetransmitCount.setStatus("mandatory")
_MscGsmBcRlpStatsTable_Object = MibTable
mscGsmBcRlpStatsTable = _MscGsmBcRlpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcRlpStatsTable.setStatus("mandatory")
_MscGsmBcRlpStatsEntry_Object = MibTableRow
mscGsmBcRlpStatsEntry = _MscGsmBcRlpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1)
)
mscGsmBcRlpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcRlpIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcRlpStatsEntry.setStatus("mandatory")
_MscGsmBcRlpIFramesTx_Type = Counter32
_MscGsmBcRlpIFramesTx_Object = MibTableColumn
mscGsmBcRlpIFramesTx = _MscGsmBcRlpIFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 1),
    _MscGsmBcRlpIFramesTx_Type()
)
mscGsmBcRlpIFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpIFramesTx.setStatus("mandatory")
_MscGsmBcRlpIFramesRx_Type = Counter32
_MscGsmBcRlpIFramesRx_Object = MibTableColumn
mscGsmBcRlpIFramesRx = _MscGsmBcRlpIFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 2),
    _MscGsmBcRlpIFramesRx_Type()
)
mscGsmBcRlpIFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpIFramesRx.setStatus("mandatory")
_MscGsmBcRlpFramesRetransmitted_Type = Counter32
_MscGsmBcRlpFramesRetransmitted_Object = MibTableColumn
mscGsmBcRlpFramesRetransmitted = _MscGsmBcRlpFramesRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 3),
    _MscGsmBcRlpFramesRetransmitted_Type()
)
mscGsmBcRlpFramesRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpFramesRetransmitted.setStatus("mandatory")
_MscGsmBcRlpT1AckTimeouts_Type = Counter32
_MscGsmBcRlpT1AckTimeouts_Object = MibTableColumn
mscGsmBcRlpT1AckTimeouts = _MscGsmBcRlpT1AckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 4),
    _MscGsmBcRlpT1AckTimeouts_Type()
)
mscGsmBcRlpT1AckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpT1AckTimeouts.setStatus("mandatory")
_MscGsmBcRlpInvalidFrames_Type = Counter32
_MscGsmBcRlpInvalidFrames_Object = MibTableColumn
mscGsmBcRlpInvalidFrames = _MscGsmBcRlpInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 5),
    _MscGsmBcRlpInvalidFrames_Type()
)
mscGsmBcRlpInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpInvalidFrames.setStatus("mandatory")
_MscGsmBcRlpCrcErrorsRx_Type = Counter32
_MscGsmBcRlpCrcErrorsRx_Object = MibTableColumn
mscGsmBcRlpCrcErrorsRx = _MscGsmBcRlpCrcErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 6),
    _MscGsmBcRlpCrcErrorsRx_Type()
)
mscGsmBcRlpCrcErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpCrcErrorsRx.setStatus("mandatory")
_MscGsmBcRlpOutOfSequenceFrames_Type = Counter32
_MscGsmBcRlpOutOfSequenceFrames_Object = MibTableColumn
mscGsmBcRlpOutOfSequenceFrames = _MscGsmBcRlpOutOfSequenceFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 7),
    _MscGsmBcRlpOutOfSequenceFrames_Type()
)
mscGsmBcRlpOutOfSequenceFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpOutOfSequenceFrames.setStatus("mandatory")
_MscGsmBcRlpRemoteBusyIndications_Type = Counter32
_MscGsmBcRlpRemoteBusyIndications_Object = MibTableColumn
mscGsmBcRlpRemoteBusyIndications = _MscGsmBcRlpRemoteBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 8),
    _MscGsmBcRlpRemoteBusyIndications_Type()
)
mscGsmBcRlpRemoteBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpRemoteBusyIndications.setStatus("mandatory")
_MscGsmBcRlpLocalBusyIndications_Type = Counter32
_MscGsmBcRlpLocalBusyIndications_Object = MibTableColumn
mscGsmBcRlpLocalBusyIndications = _MscGsmBcRlpLocalBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 9),
    _MscGsmBcRlpLocalBusyIndications_Type()
)
mscGsmBcRlpLocalBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpLocalBusyIndications.setStatus("mandatory")
_MscGsmBcRlpIFramesTxDiscarded_Type = Counter32
_MscGsmBcRlpIFramesTxDiscarded_Object = MibTableColumn
mscGsmBcRlpIFramesTxDiscarded = _MscGsmBcRlpIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 10),
    _MscGsmBcRlpIFramesTxDiscarded_Type()
)
mscGsmBcRlpIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpIFramesTxDiscarded.setStatus("mandatory")
_MscGsmBcRlpResetsRx_Type = Counter32
_MscGsmBcRlpResetsRx_Object = MibTableColumn
mscGsmBcRlpResetsRx = _MscGsmBcRlpResetsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 7, 11, 1, 11),
    _MscGsmBcRlpResetsRx_Type()
)
mscGsmBcRlpResetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcRlpResetsRx.setStatus("mandatory")
_MscGsmBcV42_ObjectIdentity = ObjectIdentity
mscGsmBcV42 = _MscGsmBcV42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8)
)
_MscGsmBcV42RowStatusTable_Object = MibTable
mscGsmBcV42RowStatusTable = _MscGsmBcV42RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcV42RowStatusTable.setStatus("mandatory")
_MscGsmBcV42RowStatusEntry_Object = MibTableRow
mscGsmBcV42RowStatusEntry = _MscGsmBcV42RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 1, 1)
)
mscGsmBcV42RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcV42Index"),
)
if mibBuilder.loadTexts:
    mscGsmBcV42RowStatusEntry.setStatus("mandatory")
_MscGsmBcV42RowStatus_Type = RowStatus
_MscGsmBcV42RowStatus_Object = MibTableColumn
mscGsmBcV42RowStatus = _MscGsmBcV42RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 1, 1, 1),
    _MscGsmBcV42RowStatus_Type()
)
mscGsmBcV42RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42RowStatus.setStatus("mandatory")
_MscGsmBcV42ComponentName_Type = DisplayString
_MscGsmBcV42ComponentName_Object = MibTableColumn
mscGsmBcV42ComponentName = _MscGsmBcV42ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 1, 1, 2),
    _MscGsmBcV42ComponentName_Type()
)
mscGsmBcV42ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42ComponentName.setStatus("mandatory")
_MscGsmBcV42StorageType_Type = StorageType
_MscGsmBcV42StorageType_Object = MibTableColumn
mscGsmBcV42StorageType = _MscGsmBcV42StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 1, 1, 4),
    _MscGsmBcV42StorageType_Type()
)
mscGsmBcV42StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42StorageType.setStatus("mandatory")
_MscGsmBcV42Index_Type = NonReplicated
_MscGsmBcV42Index_Object = MibTableColumn
mscGsmBcV42Index = _MscGsmBcV42Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 1, 1, 10),
    _MscGsmBcV42Index_Type()
)
mscGsmBcV42Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcV42Index.setStatus("mandatory")
_MscGsmBcV42OperTable_Object = MibTable
mscGsmBcV42OperTable = _MscGsmBcV42OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcV42OperTable.setStatus("mandatory")
_MscGsmBcV42OperEntry_Object = MibTableRow
mscGsmBcV42OperEntry = _MscGsmBcV42OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 10, 1)
)
mscGsmBcV42OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcV42Index"),
)
if mibBuilder.loadTexts:
    mscGsmBcV42OperEntry.setStatus("mandatory")


class _MscGsmBcV42ProtocolState_Type(Integer32):
    """Custom type mscGsmBcV42ProtocolState based on Integer32"""
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


_MscGsmBcV42ProtocolState_Type.__name__ = "Integer32"
_MscGsmBcV42ProtocolState_Object = MibTableColumn
mscGsmBcV42ProtocolState = _MscGsmBcV42ProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 10, 1, 1),
    _MscGsmBcV42ProtocolState_Type()
)
mscGsmBcV42ProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42ProtocolState.setStatus("mandatory")


class _MscGsmBcV42TxN401FrameSize_Type(Unsigned32):
    """Custom type mscGsmBcV42TxN401FrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65355),
    )


_MscGsmBcV42TxN401FrameSize_Type.__name__ = "Unsigned32"
_MscGsmBcV42TxN401FrameSize_Object = MibTableColumn
mscGsmBcV42TxN401FrameSize = _MscGsmBcV42TxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 10, 1, 2),
    _MscGsmBcV42TxN401FrameSize_Type()
)
mscGsmBcV42TxN401FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42TxN401FrameSize.setStatus("mandatory")


class _MscGsmBcV42RxN401FrameSize_Type(Unsigned32):
    """Custom type mscGsmBcV42RxN401FrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscGsmBcV42RxN401FrameSize_Type.__name__ = "Unsigned32"
_MscGsmBcV42RxN401FrameSize_Object = MibTableColumn
mscGsmBcV42RxN401FrameSize = _MscGsmBcV42RxN401FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 10, 1, 3),
    _MscGsmBcV42RxN401FrameSize_Type()
)
mscGsmBcV42RxN401FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42RxN401FrameSize.setStatus("mandatory")


class _MscGsmBcV42TxKwindowSize_Type(Unsigned32):
    """Custom type mscGsmBcV42TxKwindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscGsmBcV42TxKwindowSize_Type.__name__ = "Unsigned32"
_MscGsmBcV42TxKwindowSize_Object = MibTableColumn
mscGsmBcV42TxKwindowSize = _MscGsmBcV42TxKwindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 10, 1, 4),
    _MscGsmBcV42TxKwindowSize_Type()
)
mscGsmBcV42TxKwindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42TxKwindowSize.setStatus("mandatory")


class _MscGsmBcV42RxKwindowSize_Type(Unsigned32):
    """Custom type mscGsmBcV42RxKwindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscGsmBcV42RxKwindowSize_Type.__name__ = "Unsigned32"
_MscGsmBcV42RxKwindowSize_Object = MibTableColumn
mscGsmBcV42RxKwindowSize = _MscGsmBcV42RxKwindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 10, 1, 5),
    _MscGsmBcV42RxKwindowSize_Type()
)
mscGsmBcV42RxKwindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42RxKwindowSize.setStatus("mandatory")
_MscGsmBcV42StatsTable_Object = MibTable
mscGsmBcV42StatsTable = _MscGsmBcV42StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcV42StatsTable.setStatus("mandatory")
_MscGsmBcV42StatsEntry_Object = MibTableRow
mscGsmBcV42StatsEntry = _MscGsmBcV42StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1)
)
mscGsmBcV42StatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcV42Index"),
)
if mibBuilder.loadTexts:
    mscGsmBcV42StatsEntry.setStatus("mandatory")
_MscGsmBcV42IBytesRx_Type = Counter32
_MscGsmBcV42IBytesRx_Object = MibTableColumn
mscGsmBcV42IBytesRx = _MscGsmBcV42IBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 1),
    _MscGsmBcV42IBytesRx_Type()
)
mscGsmBcV42IBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42IBytesRx.setStatus("mandatory")
_MscGsmBcV42IBytesTx_Type = Counter32
_MscGsmBcV42IBytesTx_Object = MibTableColumn
mscGsmBcV42IBytesTx = _MscGsmBcV42IBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 2),
    _MscGsmBcV42IBytesTx_Type()
)
mscGsmBcV42IBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42IBytesTx.setStatus("mandatory")
_MscGsmBcV42IFramesRx_Type = Counter32
_MscGsmBcV42IFramesRx_Object = MibTableColumn
mscGsmBcV42IFramesRx = _MscGsmBcV42IFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 3),
    _MscGsmBcV42IFramesRx_Type()
)
mscGsmBcV42IFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42IFramesRx.setStatus("mandatory")
_MscGsmBcV42IFramesTx_Type = Counter32
_MscGsmBcV42IFramesTx_Object = MibTableColumn
mscGsmBcV42IFramesTx = _MscGsmBcV42IFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 4),
    _MscGsmBcV42IFramesTx_Type()
)
mscGsmBcV42IFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42IFramesTx.setStatus("mandatory")
_MscGsmBcV42FramesRetransmitted_Type = Counter32
_MscGsmBcV42FramesRetransmitted_Object = MibTableColumn
mscGsmBcV42FramesRetransmitted = _MscGsmBcV42FramesRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 5),
    _MscGsmBcV42FramesRetransmitted_Type()
)
mscGsmBcV42FramesRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42FramesRetransmitted.setStatus("mandatory")
_MscGsmBcV42T1AckTimeouts_Type = Counter32
_MscGsmBcV42T1AckTimeouts_Object = MibTableColumn
mscGsmBcV42T1AckTimeouts = _MscGsmBcV42T1AckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 6),
    _MscGsmBcV42T1AckTimeouts_Type()
)
mscGsmBcV42T1AckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42T1AckTimeouts.setStatus("mandatory")
_MscGsmBcV42RemoteBusyIndications_Type = Counter32
_MscGsmBcV42RemoteBusyIndications_Object = MibTableColumn
mscGsmBcV42RemoteBusyIndications = _MscGsmBcV42RemoteBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 7),
    _MscGsmBcV42RemoteBusyIndications_Type()
)
mscGsmBcV42RemoteBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42RemoteBusyIndications.setStatus("mandatory")
_MscGsmBcV42LocalBusyIndications_Type = Counter32
_MscGsmBcV42LocalBusyIndications_Object = MibTableColumn
mscGsmBcV42LocalBusyIndications = _MscGsmBcV42LocalBusyIndications_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 8),
    _MscGsmBcV42LocalBusyIndications_Type()
)
mscGsmBcV42LocalBusyIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42LocalBusyIndications.setStatus("mandatory")
_MscGsmBcV42BadFramesRx_Type = Counter32
_MscGsmBcV42BadFramesRx_Object = MibTableColumn
mscGsmBcV42BadFramesRx = _MscGsmBcV42BadFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 9),
    _MscGsmBcV42BadFramesRx_Type()
)
mscGsmBcV42BadFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42BadFramesRx.setStatus("mandatory")
_MscGsmBcV42CrcErrorsRx_Type = Counter32
_MscGsmBcV42CrcErrorsRx_Object = MibTableColumn
mscGsmBcV42CrcErrorsRx = _MscGsmBcV42CrcErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 8, 11, 1, 10),
    _MscGsmBcV42CrcErrorsRx_Type()
)
mscGsmBcV42CrcErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42CrcErrorsRx.setStatus("mandatory")
_MscGsmBcV42bis_ObjectIdentity = ObjectIdentity
mscGsmBcV42bis = _MscGsmBcV42bis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9)
)
_MscGsmBcV42bisRowStatusTable_Object = MibTable
mscGsmBcV42bisRowStatusTable = _MscGsmBcV42bisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcV42bisRowStatusTable.setStatus("mandatory")
_MscGsmBcV42bisRowStatusEntry_Object = MibTableRow
mscGsmBcV42bisRowStatusEntry = _MscGsmBcV42bisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 1, 1)
)
mscGsmBcV42bisRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcV42bisIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcV42bisRowStatusEntry.setStatus("mandatory")
_MscGsmBcV42bisRowStatus_Type = RowStatus
_MscGsmBcV42bisRowStatus_Object = MibTableColumn
mscGsmBcV42bisRowStatus = _MscGsmBcV42bisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 1, 1, 1),
    _MscGsmBcV42bisRowStatus_Type()
)
mscGsmBcV42bisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisRowStatus.setStatus("mandatory")
_MscGsmBcV42bisComponentName_Type = DisplayString
_MscGsmBcV42bisComponentName_Object = MibTableColumn
mscGsmBcV42bisComponentName = _MscGsmBcV42bisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 1, 1, 2),
    _MscGsmBcV42bisComponentName_Type()
)
mscGsmBcV42bisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisComponentName.setStatus("mandatory")
_MscGsmBcV42bisStorageType_Type = StorageType
_MscGsmBcV42bisStorageType_Object = MibTableColumn
mscGsmBcV42bisStorageType = _MscGsmBcV42bisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 1, 1, 4),
    _MscGsmBcV42bisStorageType_Type()
)
mscGsmBcV42bisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisStorageType.setStatus("mandatory")
_MscGsmBcV42bisIndex_Type = NonReplicated
_MscGsmBcV42bisIndex_Object = MibTableColumn
mscGsmBcV42bisIndex = _MscGsmBcV42bisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 1, 1, 10),
    _MscGsmBcV42bisIndex_Type()
)
mscGsmBcV42bisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcV42bisIndex.setStatus("mandatory")
_MscGsmBcV42bisOperTable_Object = MibTable
mscGsmBcV42bisOperTable = _MscGsmBcV42bisOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcV42bisOperTable.setStatus("mandatory")
_MscGsmBcV42bisOperEntry_Object = MibTableRow
mscGsmBcV42bisOperEntry = _MscGsmBcV42bisOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10, 1)
)
mscGsmBcV42bisOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcV42bisIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcV42bisOperEntry.setStatus("mandatory")


class _MscGsmBcV42bisProtocolModeEncoder_Type(Integer32):
    """Custom type mscGsmBcV42bisProtocolModeEncoder based on Integer32"""
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


_MscGsmBcV42bisProtocolModeEncoder_Type.__name__ = "Integer32"
_MscGsmBcV42bisProtocolModeEncoder_Object = MibTableColumn
mscGsmBcV42bisProtocolModeEncoder = _MscGsmBcV42bisProtocolModeEncoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10, 1, 1),
    _MscGsmBcV42bisProtocolModeEncoder_Type()
)
mscGsmBcV42bisProtocolModeEncoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisProtocolModeEncoder.setStatus("mandatory")


class _MscGsmBcV42bisProtocolModeDecoder_Type(Integer32):
    """Custom type mscGsmBcV42bisProtocolModeDecoder based on Integer32"""
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


_MscGsmBcV42bisProtocolModeDecoder_Type.__name__ = "Integer32"
_MscGsmBcV42bisProtocolModeDecoder_Object = MibTableColumn
mscGsmBcV42bisProtocolModeDecoder = _MscGsmBcV42bisProtocolModeDecoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10, 1, 2),
    _MscGsmBcV42bisProtocolModeDecoder_Type()
)
mscGsmBcV42bisProtocolModeDecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisProtocolModeDecoder.setStatus("mandatory")


class _MscGsmBcV42bisCompressionDirection_Type(Integer32):
    """Custom type mscGsmBcV42bisCompressionDirection based on Integer32"""
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


_MscGsmBcV42bisCompressionDirection_Type.__name__ = "Integer32"
_MscGsmBcV42bisCompressionDirection_Object = MibTableColumn
mscGsmBcV42bisCompressionDirection = _MscGsmBcV42bisCompressionDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10, 1, 3),
    _MscGsmBcV42bisCompressionDirection_Type()
)
mscGsmBcV42bisCompressionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisCompressionDirection.setStatus("mandatory")


class _MscGsmBcV42bisMaximumCodewords_Type(Unsigned32):
    """Custom type mscGsmBcV42bisMaximumCodewords based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscGsmBcV42bisMaximumCodewords_Type.__name__ = "Unsigned32"
_MscGsmBcV42bisMaximumCodewords_Object = MibTableColumn
mscGsmBcV42bisMaximumCodewords = _MscGsmBcV42bisMaximumCodewords_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10, 1, 4),
    _MscGsmBcV42bisMaximumCodewords_Type()
)
mscGsmBcV42bisMaximumCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisMaximumCodewords.setStatus("mandatory")


class _MscGsmBcV42bisMaximumStringSize_Type(Unsigned32):
    """Custom type mscGsmBcV42bisMaximumStringSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_MscGsmBcV42bisMaximumStringSize_Type.__name__ = "Unsigned32"
_MscGsmBcV42bisMaximumStringSize_Object = MibTableColumn
mscGsmBcV42bisMaximumStringSize = _MscGsmBcV42bisMaximumStringSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10, 1, 5),
    _MscGsmBcV42bisMaximumStringSize_Type()
)
mscGsmBcV42bisMaximumStringSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisMaximumStringSize.setStatus("mandatory")


class _MscGsmBcV42bisLastDecodeError_Type(Integer32):
    """Custom type mscGsmBcV42bisLastDecodeError based on Integer32"""
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


_MscGsmBcV42bisLastDecodeError_Type.__name__ = "Integer32"
_MscGsmBcV42bisLastDecodeError_Object = MibTableColumn
mscGsmBcV42bisLastDecodeError = _MscGsmBcV42bisLastDecodeError_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10, 1, 6),
    _MscGsmBcV42bisLastDecodeError_Type()
)
mscGsmBcV42bisLastDecodeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisLastDecodeError.setStatus("mandatory")


class _MscGsmBcV42bisCompRatioEncoder_Type(FixedPoint2):
    """Custom type mscGsmBcV42bisCompRatioEncoder based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_MscGsmBcV42bisCompRatioEncoder_Type.__name__ = "FixedPoint2"
_MscGsmBcV42bisCompRatioEncoder_Object = MibTableColumn
mscGsmBcV42bisCompRatioEncoder = _MscGsmBcV42bisCompRatioEncoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10, 1, 7),
    _MscGsmBcV42bisCompRatioEncoder_Type()
)
mscGsmBcV42bisCompRatioEncoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisCompRatioEncoder.setStatus("mandatory")


class _MscGsmBcV42bisCompRatioDecoder_Type(FixedPoint2):
    """Custom type mscGsmBcV42bisCompRatioDecoder based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_MscGsmBcV42bisCompRatioDecoder_Type.__name__ = "FixedPoint2"
_MscGsmBcV42bisCompRatioDecoder_Object = MibTableColumn
mscGsmBcV42bisCompRatioDecoder = _MscGsmBcV42bisCompRatioDecoder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 10, 1, 8),
    _MscGsmBcV42bisCompRatioDecoder_Type()
)
mscGsmBcV42bisCompRatioDecoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisCompRatioDecoder.setStatus("mandatory")
_MscGsmBcV42bisStatsTable_Object = MibTable
mscGsmBcV42bisStatsTable = _MscGsmBcV42bisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcV42bisStatsTable.setStatus("mandatory")
_MscGsmBcV42bisStatsEntry_Object = MibTableRow
mscGsmBcV42bisStatsEntry = _MscGsmBcV42bisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 11, 1)
)
mscGsmBcV42bisStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcV42bisIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcV42bisStatsEntry.setStatus("mandatory")
_MscGsmBcV42bisModeChangesEncode_Type = Counter32
_MscGsmBcV42bisModeChangesEncode_Object = MibTableColumn
mscGsmBcV42bisModeChangesEncode = _MscGsmBcV42bisModeChangesEncode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 11, 1, 1),
    _MscGsmBcV42bisModeChangesEncode_Type()
)
mscGsmBcV42bisModeChangesEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisModeChangesEncode.setStatus("mandatory")
_MscGsmBcV42bisModeChangesDecode_Type = Counter32
_MscGsmBcV42bisModeChangesDecode_Object = MibTableColumn
mscGsmBcV42bisModeChangesDecode = _MscGsmBcV42bisModeChangesDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 11, 1, 2),
    _MscGsmBcV42bisModeChangesDecode_Type()
)
mscGsmBcV42bisModeChangesDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisModeChangesDecode.setStatus("mandatory")
_MscGsmBcV42bisResetsEncode_Type = Counter32
_MscGsmBcV42bisResetsEncode_Object = MibTableColumn
mscGsmBcV42bisResetsEncode = _MscGsmBcV42bisResetsEncode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 11, 1, 3),
    _MscGsmBcV42bisResetsEncode_Type()
)
mscGsmBcV42bisResetsEncode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisResetsEncode.setStatus("mandatory")
_MscGsmBcV42bisResetsDecode_Type = Counter32
_MscGsmBcV42bisResetsDecode_Object = MibTableColumn
mscGsmBcV42bisResetsDecode = _MscGsmBcV42bisResetsDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 11, 1, 4),
    _MscGsmBcV42bisResetsDecode_Type()
)
mscGsmBcV42bisResetsDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisResetsDecode.setStatus("mandatory")
_MscGsmBcV42bisReInitializations_Type = Counter32
_MscGsmBcV42bisReInitializations_Object = MibTableColumn
mscGsmBcV42bisReInitializations = _MscGsmBcV42bisReInitializations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 11, 1, 5),
    _MscGsmBcV42bisReInitializations_Type()
)
mscGsmBcV42bisReInitializations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisReInitializations.setStatus("mandatory")
_MscGsmBcV42bisErrorsInDecode_Type = Counter32
_MscGsmBcV42bisErrorsInDecode_Object = MibTableColumn
mscGsmBcV42bisErrorsInDecode = _MscGsmBcV42bisErrorsInDecode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 9, 11, 1, 6),
    _MscGsmBcV42bisErrorsInDecode_Type()
)
mscGsmBcV42bisErrorsInDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcV42bisErrorsInDecode.setStatus("mandatory")
_MscGsmBcL2RCop_ObjectIdentity = ObjectIdentity
mscGsmBcL2RCop = _MscGsmBcL2RCop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10)
)
_MscGsmBcL2RCopRowStatusTable_Object = MibTable
mscGsmBcL2RCopRowStatusTable = _MscGsmBcL2RCopRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcL2RCopRowStatusTable.setStatus("mandatory")
_MscGsmBcL2RCopRowStatusEntry_Object = MibTableRow
mscGsmBcL2RCopRowStatusEntry = _MscGsmBcL2RCopRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 1, 1)
)
mscGsmBcL2RCopRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcL2RCopIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcL2RCopRowStatusEntry.setStatus("mandatory")
_MscGsmBcL2RCopRowStatus_Type = RowStatus
_MscGsmBcL2RCopRowStatus_Object = MibTableColumn
mscGsmBcL2RCopRowStatus = _MscGsmBcL2RCopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 1, 1, 1),
    _MscGsmBcL2RCopRowStatus_Type()
)
mscGsmBcL2RCopRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopRowStatus.setStatus("mandatory")
_MscGsmBcL2RCopComponentName_Type = DisplayString
_MscGsmBcL2RCopComponentName_Object = MibTableColumn
mscGsmBcL2RCopComponentName = _MscGsmBcL2RCopComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 1, 1, 2),
    _MscGsmBcL2RCopComponentName_Type()
)
mscGsmBcL2RCopComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopComponentName.setStatus("mandatory")
_MscGsmBcL2RCopStorageType_Type = StorageType
_MscGsmBcL2RCopStorageType_Object = MibTableColumn
mscGsmBcL2RCopStorageType = _MscGsmBcL2RCopStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 1, 1, 4),
    _MscGsmBcL2RCopStorageType_Type()
)
mscGsmBcL2RCopStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopStorageType.setStatus("mandatory")
_MscGsmBcL2RCopIndex_Type = NonReplicated
_MscGsmBcL2RCopIndex_Object = MibTableColumn
mscGsmBcL2RCopIndex = _MscGsmBcL2RCopIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 1, 1, 10),
    _MscGsmBcL2RCopIndex_Type()
)
mscGsmBcL2RCopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopIndex.setStatus("mandatory")
_MscGsmBcL2RCopOperTable_Object = MibTable
mscGsmBcL2RCopOperTable = _MscGsmBcL2RCopOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcL2RCopOperTable.setStatus("mandatory")
_MscGsmBcL2RCopOperEntry_Object = MibTableRow
mscGsmBcL2RCopOperEntry = _MscGsmBcL2RCopOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 10, 1)
)
mscGsmBcL2RCopOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcL2RCopIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcL2RCopOperEntry.setStatus("mandatory")


class _MscGsmBcL2RCopFlowControlStateTx_Type(Integer32):
    """Custom type mscGsmBcL2RCopFlowControlStateTx based on Integer32"""
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


_MscGsmBcL2RCopFlowControlStateTx_Type.__name__ = "Integer32"
_MscGsmBcL2RCopFlowControlStateTx_Object = MibTableColumn
mscGsmBcL2RCopFlowControlStateTx = _MscGsmBcL2RCopFlowControlStateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 10, 1, 1),
    _MscGsmBcL2RCopFlowControlStateTx_Type()
)
mscGsmBcL2RCopFlowControlStateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopFlowControlStateTx.setStatus("mandatory")


class _MscGsmBcL2RCopFlowControlStateRx_Type(Integer32):
    """Custom type mscGsmBcL2RCopFlowControlStateRx based on Integer32"""
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


_MscGsmBcL2RCopFlowControlStateRx_Type.__name__ = "Integer32"
_MscGsmBcL2RCopFlowControlStateRx_Object = MibTableColumn
mscGsmBcL2RCopFlowControlStateRx = _MscGsmBcL2RCopFlowControlStateRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 10, 1, 2),
    _MscGsmBcL2RCopFlowControlStateRx_Type()
)
mscGsmBcL2RCopFlowControlStateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopFlowControlStateRx.setStatus("mandatory")
_MscGsmBcL2RCopStatsTable_Object = MibTable
mscGsmBcL2RCopStatsTable = _MscGsmBcL2RCopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcL2RCopStatsTable.setStatus("mandatory")
_MscGsmBcL2RCopStatsEntry_Object = MibTableRow
mscGsmBcL2RCopStatsEntry = _MscGsmBcL2RCopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 11, 1)
)
mscGsmBcL2RCopStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcL2RCopIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcL2RCopStatsEntry.setStatus("mandatory")
_MscGsmBcL2RCopBytesTx_Type = Counter32
_MscGsmBcL2RCopBytesTx_Object = MibTableColumn
mscGsmBcL2RCopBytesTx = _MscGsmBcL2RCopBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 11, 1, 1),
    _MscGsmBcL2RCopBytesTx_Type()
)
mscGsmBcL2RCopBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopBytesTx.setStatus("mandatory")
_MscGsmBcL2RCopBytesRx_Type = Counter32
_MscGsmBcL2RCopBytesRx_Object = MibTableColumn
mscGsmBcL2RCopBytesRx = _MscGsmBcL2RCopBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 11, 1, 2),
    _MscGsmBcL2RCopBytesRx_Type()
)
mscGsmBcL2RCopBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopBytesRx.setStatus("mandatory")
_MscGsmBcL2RCopBreakCountRx_Type = Counter32
_MscGsmBcL2RCopBreakCountRx_Object = MibTableColumn
mscGsmBcL2RCopBreakCountRx = _MscGsmBcL2RCopBreakCountRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 11, 1, 3),
    _MscGsmBcL2RCopBreakCountRx_Type()
)
mscGsmBcL2RCopBreakCountRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopBreakCountRx.setStatus("mandatory")
_MscGsmBcL2RCopBreakCountTx_Type = Counter32
_MscGsmBcL2RCopBreakCountTx_Object = MibTableColumn
mscGsmBcL2RCopBreakCountTx = _MscGsmBcL2RCopBreakCountTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 10, 11, 1, 4),
    _MscGsmBcL2RCopBreakCountTx_Type()
)
mscGsmBcL2RCopBreakCountTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcL2RCopBreakCountTx.setStatus("mandatory")
_MscGsmBcUpperRelay_ObjectIdentity = ObjectIdentity
mscGsmBcUpperRelay = _MscGsmBcUpperRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11)
)
_MscGsmBcUpperRelayRowStatusTable_Object = MibTable
mscGsmBcUpperRelayRowStatusTable = _MscGsmBcUpperRelayRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 1)
)
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayRowStatusTable.setStatus("mandatory")
_MscGsmBcUpperRelayRowStatusEntry_Object = MibTableRow
mscGsmBcUpperRelayRowStatusEntry = _MscGsmBcUpperRelayRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 1, 1)
)
mscGsmBcUpperRelayRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcUpperRelayIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayRowStatusEntry.setStatus("mandatory")
_MscGsmBcUpperRelayRowStatus_Type = RowStatus
_MscGsmBcUpperRelayRowStatus_Object = MibTableColumn
mscGsmBcUpperRelayRowStatus = _MscGsmBcUpperRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 1, 1, 1),
    _MscGsmBcUpperRelayRowStatus_Type()
)
mscGsmBcUpperRelayRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayRowStatus.setStatus("mandatory")
_MscGsmBcUpperRelayComponentName_Type = DisplayString
_MscGsmBcUpperRelayComponentName_Object = MibTableColumn
mscGsmBcUpperRelayComponentName = _MscGsmBcUpperRelayComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 1, 1, 2),
    _MscGsmBcUpperRelayComponentName_Type()
)
mscGsmBcUpperRelayComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayComponentName.setStatus("mandatory")
_MscGsmBcUpperRelayStorageType_Type = StorageType
_MscGsmBcUpperRelayStorageType_Object = MibTableColumn
mscGsmBcUpperRelayStorageType = _MscGsmBcUpperRelayStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 1, 1, 4),
    _MscGsmBcUpperRelayStorageType_Type()
)
mscGsmBcUpperRelayStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayStorageType.setStatus("mandatory")
_MscGsmBcUpperRelayIndex_Type = NonReplicated
_MscGsmBcUpperRelayIndex_Object = MibTableColumn
mscGsmBcUpperRelayIndex = _MscGsmBcUpperRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 1, 1, 10),
    _MscGsmBcUpperRelayIndex_Type()
)
mscGsmBcUpperRelayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayIndex.setStatus("mandatory")
_MscGsmBcUpperRelayOperTable_Object = MibTable
mscGsmBcUpperRelayOperTable = _MscGsmBcUpperRelayOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 10)
)
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayOperTable.setStatus("mandatory")
_MscGsmBcUpperRelayOperEntry_Object = MibTableRow
mscGsmBcUpperRelayOperEntry = _MscGsmBcUpperRelayOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 10, 1)
)
mscGsmBcUpperRelayOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcUpperRelayIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayOperEntry.setStatus("mandatory")


class _MscGsmBcUpperRelayBufferSize_Type(Unsigned32):
    """Custom type mscGsmBcUpperRelayBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscGsmBcUpperRelayBufferSize_Type.__name__ = "Unsigned32"
_MscGsmBcUpperRelayBufferSize_Object = MibTableColumn
mscGsmBcUpperRelayBufferSize = _MscGsmBcUpperRelayBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 10, 1, 1),
    _MscGsmBcUpperRelayBufferSize_Type()
)
mscGsmBcUpperRelayBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayBufferSize.setStatus("mandatory")


class _MscGsmBcUpperRelayFlowControlStateTx_Type(Integer32):
    """Custom type mscGsmBcUpperRelayFlowControlStateTx based on Integer32"""
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


_MscGsmBcUpperRelayFlowControlStateTx_Type.__name__ = "Integer32"
_MscGsmBcUpperRelayFlowControlStateTx_Object = MibTableColumn
mscGsmBcUpperRelayFlowControlStateTx = _MscGsmBcUpperRelayFlowControlStateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 10, 1, 2),
    _MscGsmBcUpperRelayFlowControlStateTx_Type()
)
mscGsmBcUpperRelayFlowControlStateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayFlowControlStateTx.setStatus("mandatory")


class _MscGsmBcUpperRelayFlowControlStateRx_Type(Integer32):
    """Custom type mscGsmBcUpperRelayFlowControlStateRx based on Integer32"""
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


_MscGsmBcUpperRelayFlowControlStateRx_Type.__name__ = "Integer32"
_MscGsmBcUpperRelayFlowControlStateRx_Object = MibTableColumn
mscGsmBcUpperRelayFlowControlStateRx = _MscGsmBcUpperRelayFlowControlStateRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 10, 1, 3),
    _MscGsmBcUpperRelayFlowControlStateRx_Type()
)
mscGsmBcUpperRelayFlowControlStateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayFlowControlStateRx.setStatus("mandatory")
_MscGsmBcUpperRelayStatsTable_Object = MibTable
mscGsmBcUpperRelayStatsTable = _MscGsmBcUpperRelayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 11)
)
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayStatsTable.setStatus("mandatory")
_MscGsmBcUpperRelayStatsEntry_Object = MibTableRow
mscGsmBcUpperRelayStatsEntry = _MscGsmBcUpperRelayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 11, 1)
)
mscGsmBcUpperRelayStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcUpperRelayIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayStatsEntry.setStatus("mandatory")
_MscGsmBcUpperRelayFramesTx_Type = Counter32
_MscGsmBcUpperRelayFramesTx_Object = MibTableColumn
mscGsmBcUpperRelayFramesTx = _MscGsmBcUpperRelayFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 11, 1, 1),
    _MscGsmBcUpperRelayFramesTx_Type()
)
mscGsmBcUpperRelayFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayFramesTx.setStatus("mandatory")
_MscGsmBcUpperRelayFramesRx_Type = Counter32
_MscGsmBcUpperRelayFramesRx_Object = MibTableColumn
mscGsmBcUpperRelayFramesRx = _MscGsmBcUpperRelayFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 11, 1, 2),
    _MscGsmBcUpperRelayFramesRx_Type()
)
mscGsmBcUpperRelayFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayFramesRx.setStatus("mandatory")


class _MscGsmBcUpperRelayUnacknowledgedFrames_Type(Gauge32):
    """Custom type mscGsmBcUpperRelayUnacknowledgedFrames based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscGsmBcUpperRelayUnacknowledgedFrames_Type.__name__ = "Gauge32"
_MscGsmBcUpperRelayUnacknowledgedFrames_Object = MibTableColumn
mscGsmBcUpperRelayUnacknowledgedFrames = _MscGsmBcUpperRelayUnacknowledgedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 11, 11, 1, 3),
    _MscGsmBcUpperRelayUnacknowledgedFrames_Type()
)
mscGsmBcUpperRelayUnacknowledgedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUpperRelayUnacknowledgedFrames.setStatus("mandatory")
_MscGsmBcOperTable_Object = MibTable
mscGsmBcOperTable = _MscGsmBcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101)
)
if mibBuilder.loadTexts:
    mscGsmBcOperTable.setStatus("mandatory")
_MscGsmBcOperEntry_Object = MibTableRow
mscGsmBcOperEntry = _MscGsmBcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1)
)
mscGsmBcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcOperEntry.setStatus("mandatory")


class _MscGsmBcMipState_Type(Integer32):
    """Custom type mscGsmBcMipState based on Integer32"""
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


_MscGsmBcMipState_Type.__name__ = "Integer32"
_MscGsmBcMipState_Object = MibTableColumn
mscGsmBcMipState = _MscGsmBcMipState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 1),
    _MscGsmBcMipState_Type()
)
mscGsmBcMipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcMipState.setStatus("mandatory")


class _MscGsmBcMaxUserDataRate_Type(Integer32):
    """Custom type mscGsmBcMaxUserDataRate based on Integer32"""
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


_MscGsmBcMaxUserDataRate_Type.__name__ = "Integer32"
_MscGsmBcMaxUserDataRate_Object = MibTableColumn
mscGsmBcMaxUserDataRate = _MscGsmBcMaxUserDataRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 2),
    _MscGsmBcMaxUserDataRate_Type()
)
mscGsmBcMaxUserDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcMaxUserDataRate.setStatus("mandatory")


class _MscGsmBcConnectionType_Type(Integer32):
    """Custom type mscGsmBcConnectionType based on Integer32"""
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


_MscGsmBcConnectionType_Type.__name__ = "Integer32"
_MscGsmBcConnectionType_Object = MibTableColumn
mscGsmBcConnectionType = _MscGsmBcConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 3),
    _MscGsmBcConnectionType_Type()
)
mscGsmBcConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcConnectionType.setStatus("mandatory")


class _MscGsmBcDataBits_Type(Integer32):
    """Custom type mscGsmBcDataBits based on Integer32"""
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


_MscGsmBcDataBits_Type.__name__ = "Integer32"
_MscGsmBcDataBits_Object = MibTableColumn
mscGsmBcDataBits = _MscGsmBcDataBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 4),
    _MscGsmBcDataBits_Type()
)
mscGsmBcDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcDataBits.setStatus("mandatory")


class _MscGsmBcStopBits_Type(Integer32):
    """Custom type mscGsmBcStopBits based on Integer32"""
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


_MscGsmBcStopBits_Type.__name__ = "Integer32"
_MscGsmBcStopBits_Object = MibTableColumn
mscGsmBcStopBits = _MscGsmBcStopBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 5),
    _MscGsmBcStopBits_Type()
)
mscGsmBcStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcStopBits.setStatus("mandatory")


class _MscGsmBcParity_Type(Integer32):
    """Custom type mscGsmBcParity based on Integer32"""
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


_MscGsmBcParity_Type.__name__ = "Integer32"
_MscGsmBcParity_Object = MibTableColumn
mscGsmBcParity = _MscGsmBcParity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 6),
    _MscGsmBcParity_Type()
)
mscGsmBcParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcParity.setStatus("mandatory")


class _MscGsmBcFlowControl_Type(Integer32):
    """Custom type mscGsmBcFlowControl based on Integer32"""
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


_MscGsmBcFlowControl_Type.__name__ = "Integer32"
_MscGsmBcFlowControl_Object = MibTableColumn
mscGsmBcFlowControl = _MscGsmBcFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 7),
    _MscGsmBcFlowControl_Type()
)
mscGsmBcFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcFlowControl.setStatus("mandatory")


class _MscGsmBcCallType_Type(Integer32):
    """Custom type mscGsmBcCallType based on Integer32"""
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


_MscGsmBcCallType_Type.__name__ = "Integer32"
_MscGsmBcCallType_Object = MibTableColumn
mscGsmBcCallType = _MscGsmBcCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 8),
    _MscGsmBcCallType_Type()
)
mscGsmBcCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcCallType.setStatus("mandatory")


class _MscGsmBcLastResponseCode_Type(Integer32):
    """Custom type mscGsmBcLastResponseCode based on Integer32"""
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


_MscGsmBcLastResponseCode_Type.__name__ = "Integer32"
_MscGsmBcLastResponseCode_Object = MibTableColumn
mscGsmBcLastResponseCode = _MscGsmBcLastResponseCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 9),
    _MscGsmBcLastResponseCode_Type()
)
mscGsmBcLastResponseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcLastResponseCode.setStatus("mandatory")
_MscGsmBcMateBearerChannel_Type = RowPointer
_MscGsmBcMateBearerChannel_Object = MibTableColumn
mscGsmBcMateBearerChannel = _MscGsmBcMateBearerChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 101, 1, 10),
    _MscGsmBcMateBearerChannel_Type()
)
mscGsmBcMateBearerChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcMateBearerChannel.setStatus("mandatory")
_MscGsmBcCidDataTable_Object = MibTable
mscGsmBcCidDataTable = _MscGsmBcCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 104)
)
if mibBuilder.loadTexts:
    mscGsmBcCidDataTable.setStatus("mandatory")
_MscGsmBcCidDataEntry_Object = MibTableRow
mscGsmBcCidDataEntry = _MscGsmBcCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 104, 1)
)
mscGsmBcCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcCidDataEntry.setStatus("mandatory")


class _MscGsmBcCustomerIdentifier_Type(Unsigned32):
    """Custom type mscGsmBcCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscGsmBcCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscGsmBcCustomerIdentifier_Object = MibTableColumn
mscGsmBcCustomerIdentifier = _MscGsmBcCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 104, 1, 1),
    _MscGsmBcCustomerIdentifier_Type()
)
mscGsmBcCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscGsmBcCustomerIdentifier.setStatus("mandatory")
_MscGsmBcStateTable_Object = MibTable
mscGsmBcStateTable = _MscGsmBcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 105)
)
if mibBuilder.loadTexts:
    mscGsmBcStateTable.setStatus("mandatory")
_MscGsmBcStateEntry_Object = MibTableRow
mscGsmBcStateEntry = _MscGsmBcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 105, 1)
)
mscGsmBcStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcTrunkGrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-GsmIwfMIB", "mscGsmBcCicIndex"),
)
if mibBuilder.loadTexts:
    mscGsmBcStateEntry.setStatus("mandatory")


class _MscGsmBcAdminState_Type(Integer32):
    """Custom type mscGsmBcAdminState based on Integer32"""
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


_MscGsmBcAdminState_Type.__name__ = "Integer32"
_MscGsmBcAdminState_Object = MibTableColumn
mscGsmBcAdminState = _MscGsmBcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 105, 1, 1),
    _MscGsmBcAdminState_Type()
)
mscGsmBcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcAdminState.setStatus("mandatory")


class _MscGsmBcOperationalState_Type(Integer32):
    """Custom type mscGsmBcOperationalState based on Integer32"""
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


_MscGsmBcOperationalState_Type.__name__ = "Integer32"
_MscGsmBcOperationalState_Object = MibTableColumn
mscGsmBcOperationalState = _MscGsmBcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 105, 1, 2),
    _MscGsmBcOperationalState_Type()
)
mscGsmBcOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcOperationalState.setStatus("mandatory")


class _MscGsmBcUsageState_Type(Integer32):
    """Custom type mscGsmBcUsageState based on Integer32"""
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


_MscGsmBcUsageState_Type.__name__ = "Integer32"
_MscGsmBcUsageState_Object = MibTableColumn
mscGsmBcUsageState = _MscGsmBcUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 128, 105, 1, 3),
    _MscGsmBcUsageState_Type()
)
mscGsmBcUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscGsmBcUsageState.setStatus("mandatory")
_GsmIwfMIB_ObjectIdentity = ObjectIdentity
gsmIwfMIB = _GsmIwfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 129)
)
_GsmIwfGroup_ObjectIdentity = ObjectIdentity
gsmIwfGroup = _GsmIwfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 129, 1)
)
_GsmIwfGroupCA_ObjectIdentity = ObjectIdentity
gsmIwfGroupCA = _GsmIwfGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 129, 1, 1)
)
_GsmIwfGroupCA02_ObjectIdentity = ObjectIdentity
gsmIwfGroupCA02 = _GsmIwfGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 129, 1, 1, 3)
)
_GsmIwfGroupCA02A_ObjectIdentity = ObjectIdentity
gsmIwfGroupCA02A = _GsmIwfGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 129, 1, 1, 3, 2)
)
_GsmIwfCapabilities_ObjectIdentity = ObjectIdentity
gsmIwfCapabilities = _GsmIwfCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 129, 3)
)
_GsmIwfCapabilitiesCA_ObjectIdentity = ObjectIdentity
gsmIwfCapabilitiesCA = _GsmIwfCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 129, 3, 1)
)
_GsmIwfCapabilitiesCA02_ObjectIdentity = ObjectIdentity
gsmIwfCapabilitiesCA02 = _GsmIwfCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 129, 3, 1, 3)
)
_GsmIwfCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
gsmIwfCapabilitiesCA02A = _GsmIwfCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 129, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-GsmIwfMIB",
    **{"mscGsmCs": mscGsmCs,
       "mscGsmCsRowStatusTable": mscGsmCsRowStatusTable,
       "mscGsmCsRowStatusEntry": mscGsmCsRowStatusEntry,
       "mscGsmCsRowStatus": mscGsmCsRowStatus,
       "mscGsmCsComponentName": mscGsmCsComponentName,
       "mscGsmCsStorageType": mscGsmCsStorageType,
       "mscGsmCsTrunkGrpIndex": mscGsmCsTrunkGrpIndex,
       "mscGsmCsModem": mscGsmCsModem,
       "mscGsmCsModemRowStatusTable": mscGsmCsModemRowStatusTable,
       "mscGsmCsModemRowStatusEntry": mscGsmCsModemRowStatusEntry,
       "mscGsmCsModemRowStatus": mscGsmCsModemRowStatus,
       "mscGsmCsModemComponentName": mscGsmCsModemComponentName,
       "mscGsmCsModemStorageType": mscGsmCsModemStorageType,
       "mscGsmCsModemIndex": mscGsmCsModemIndex,
       "mscGsmCsRlp": mscGsmCsRlp,
       "mscGsmCsRlpRowStatusTable": mscGsmCsRlpRowStatusTable,
       "mscGsmCsRlpRowStatusEntry": mscGsmCsRlpRowStatusEntry,
       "mscGsmCsRlpRowStatus": mscGsmCsRlpRowStatus,
       "mscGsmCsRlpComponentName": mscGsmCsRlpComponentName,
       "mscGsmCsRlpStorageType": mscGsmCsRlpStorageType,
       "mscGsmCsRlpIndex": mscGsmCsRlpIndex,
       "mscGsmCsRlpProvTable": mscGsmCsRlpProvTable,
       "mscGsmCsRlpProvEntry": mscGsmCsRlpProvEntry,
       "mscGsmCsRlpHighestVersion": mscGsmCsRlpHighestVersion,
       "mscGsmCsRlpIwfToMsWindowSize": mscGsmCsRlpIwfToMsWindowSize,
       "mscGsmCsRlpMsToIwfWindowSize": mscGsmCsRlpMsToIwfWindowSize,
       "mscGsmCsRlpT1AckTimer": mscGsmCsRlpT1AckTimer,
       "mscGsmCsRlpT2AckDelayTimer": mscGsmCsRlpT2AckDelayTimer,
       "mscGsmCsRlpN2RetransmitCount": mscGsmCsRlpN2RetransmitCount,
       "mscGsmCsFax": mscGsmCsFax,
       "mscGsmCsFaxRowStatusTable": mscGsmCsFaxRowStatusTable,
       "mscGsmCsFaxRowStatusEntry": mscGsmCsFaxRowStatusEntry,
       "mscGsmCsFaxRowStatus": mscGsmCsFaxRowStatus,
       "mscGsmCsFaxComponentName": mscGsmCsFaxComponentName,
       "mscGsmCsFaxStorageType": mscGsmCsFaxStorageType,
       "mscGsmCsFaxIndex": mscGsmCsFaxIndex,
       "mscGsmCsFaxProvTable": mscGsmCsFaxProvTable,
       "mscGsmCsFaxProvEntry": mscGsmCsFaxProvEntry,
       "mscGsmCsFaxT1CalledToneTimer": mscGsmCsFaxT1CalledToneTimer,
       "mscGsmCsV42": mscGsmCsV42,
       "mscGsmCsV42RowStatusTable": mscGsmCsV42RowStatusTable,
       "mscGsmCsV42RowStatusEntry": mscGsmCsV42RowStatusEntry,
       "mscGsmCsV42RowStatus": mscGsmCsV42RowStatus,
       "mscGsmCsV42ComponentName": mscGsmCsV42ComponentName,
       "mscGsmCsV42StorageType": mscGsmCsV42StorageType,
       "mscGsmCsV42Index": mscGsmCsV42Index,
       "mscGsmCsV42ProvTable": mscGsmCsV42ProvTable,
       "mscGsmCsV42ProvEntry": mscGsmCsV42ProvEntry,
       "mscGsmCsV42T400DetectTimer": mscGsmCsV42T400DetectTimer,
       "mscGsmCsV42T401AckTimer": mscGsmCsV42T401AckTimer,
       "mscGsmCsV42T402AckDelayTimer": mscGsmCsV42T402AckDelayTimer,
       "mscGsmCsV42T403IdleProbeTimer": mscGsmCsV42T403IdleProbeTimer,
       "mscGsmCsV42TxN401FrameSize": mscGsmCsV42TxN401FrameSize,
       "mscGsmCsV42RxN401FrameSize": mscGsmCsV42RxN401FrameSize,
       "mscGsmCsV42TxKwindowSize": mscGsmCsV42TxKwindowSize,
       "mscGsmCsV42RxKwindowSize": mscGsmCsV42RxKwindowSize,
       "mscGsmCsV42N400RetransLimit": mscGsmCsV42N400RetransLimit,
       "mscGsmCsV42bis": mscGsmCsV42bis,
       "mscGsmCsV42bisRowStatusTable": mscGsmCsV42bisRowStatusTable,
       "mscGsmCsV42bisRowStatusEntry": mscGsmCsV42bisRowStatusEntry,
       "mscGsmCsV42bisRowStatus": mscGsmCsV42bisRowStatus,
       "mscGsmCsV42bisComponentName": mscGsmCsV42bisComponentName,
       "mscGsmCsV42bisStorageType": mscGsmCsV42bisStorageType,
       "mscGsmCsV42bisIndex": mscGsmCsV42bisIndex,
       "mscGsmCsV42bisProvTable": mscGsmCsV42bisProvTable,
       "mscGsmCsV42bisProvEntry": mscGsmCsV42bisProvEntry,
       "mscGsmCsV42bisCompressionDirection": mscGsmCsV42bisCompressionDirection,
       "mscGsmCsV42bisMaximumCodewords": mscGsmCsV42bisMaximumCodewords,
       "mscGsmCsV42bisMaximumStringSize": mscGsmCsV42bisMaximumStringSize,
       "mscGsmCsV42bisActionOnError": mscGsmCsV42bisActionOnError,
       "mscGsmCsLp": mscGsmCsLp,
       "mscGsmCsLpRowStatusTable": mscGsmCsLpRowStatusTable,
       "mscGsmCsLpRowStatusEntry": mscGsmCsLpRowStatusEntry,
       "mscGsmCsLpRowStatus": mscGsmCsLpRowStatus,
       "mscGsmCsLpComponentName": mscGsmCsLpComponentName,
       "mscGsmCsLpStorageType": mscGsmCsLpStorageType,
       "mscGsmCsLpIndex": mscGsmCsLpIndex,
       "mscGsmCsLpOperTable": mscGsmCsLpOperTable,
       "mscGsmCsLpOperEntry": mscGsmCsLpOperEntry,
       "mscGsmCsLpConfiguredBearerChannels": mscGsmCsLpConfiguredBearerChannels,
       "mscGsmCsLpActiveCalls": mscGsmCsLpActiveCalls,
       "mscGsmCsLpAssignedCapacity": mscGsmCsLpAssignedCapacity,
       "mscGsmCsLpModemsSupported": mscGsmCsLpModemsSupported,
       "mscGsmCsProvTable": mscGsmCsProvTable,
       "mscGsmCsProvEntry": mscGsmCsProvEntry,
       "mscGsmCsCommentText": mscGsmCsCommentText,
       "mscGsmCsMscIpAddress": mscGsmCsMscIpAddress,
       "mscGsmCsVirtualRouterName": mscGsmCsVirtualRouterName,
       "mscGsmCsVoiceLaw": mscGsmCsVoiceLaw,
       "mscGsmCsCidDataTable": mscGsmCsCidDataTable,
       "mscGsmCsCidDataEntry": mscGsmCsCidDataEntry,
       "mscGsmCsCustomerIdentifier": mscGsmCsCustomerIdentifier,
       "mscGsmCsStateTable": mscGsmCsStateTable,
       "mscGsmCsStateEntry": mscGsmCsStateEntry,
       "mscGsmCsAdminState": mscGsmCsAdminState,
       "mscGsmCsOperationalState": mscGsmCsOperationalState,
       "mscGsmCsUsageState": mscGsmCsUsageState,
       "mscGsmCsStatsTable": mscGsmCsStatsTable,
       "mscGsmCsStatsEntry": mscGsmCsStatsEntry,
       "mscGsmCsCurrentCalls": mscGsmCsCurrentCalls,
       "mscGsmCsCallsRequested": mscGsmCsCallsRequested,
       "mscGsmCsCallsSetup": mscGsmCsCallsSetup,
       "mscGsmCsCallsActivated": mscGsmCsCallsActivated,
       "mscGsmCsCallsReleasedNormal": mscGsmCsCallsReleasedNormal,
       "mscGsmCsCallsReleasedAbnormal": mscGsmCsCallsReleasedAbnormal,
       "mscGsmCsChannelConfigChanges": mscGsmCsChannelConfigChanges,
       "mscGsmCsChannelModeModifyRequests": mscGsmCsChannelModeModifyRequests,
       "mscGsmCsStatusMessagesRx": mscGsmCsStatusMessagesRx,
       "mscGsmCsErroredMipFrames": mscGsmCsErroredMipFrames,
       "mscGsmBc": mscGsmBc,
       "mscGsmBcRowStatusTable": mscGsmBcRowStatusTable,
       "mscGsmBcRowStatusEntry": mscGsmBcRowStatusEntry,
       "mscGsmBcRowStatus": mscGsmBcRowStatus,
       "mscGsmBcComponentName": mscGsmBcComponentName,
       "mscGsmBcStorageType": mscGsmBcStorageType,
       "mscGsmBcTrunkGrpIndex": mscGsmBcTrunkGrpIndex,
       "mscGsmBcCicIndex": mscGsmBcCicIndex,
       "mscGsmBcFramer": mscGsmBcFramer,
       "mscGsmBcFramerRowStatusTable": mscGsmBcFramerRowStatusTable,
       "mscGsmBcFramerRowStatusEntry": mscGsmBcFramerRowStatusEntry,
       "mscGsmBcFramerRowStatus": mscGsmBcFramerRowStatus,
       "mscGsmBcFramerComponentName": mscGsmBcFramerComponentName,
       "mscGsmBcFramerStorageType": mscGsmBcFramerStorageType,
       "mscGsmBcFramerIndex": mscGsmBcFramerIndex,
       "mscGsmBcFramerProvTable": mscGsmBcFramerProvTable,
       "mscGsmBcFramerProvEntry": mscGsmBcFramerProvEntry,
       "mscGsmBcFramerInterfaceName": mscGsmBcFramerInterfaceName,
       "mscGsmBcFramerStatsTable": mscGsmBcFramerStatsTable,
       "mscGsmBcFramerStatsEntry": mscGsmBcFramerStatsEntry,
       "mscGsmBcFramerFrmToIf": mscGsmBcFramerFrmToIf,
       "mscGsmBcFramerFrmFromIf": mscGsmBcFramerFrmFromIf,
       "mscGsmBcFramerOctetFromIf": mscGsmBcFramerOctetFromIf,
       "mscGsmBcFramerCrcErrors": mscGsmBcFramerCrcErrors,
       "mscGsmBcFramerLrcErrors": mscGsmBcFramerLrcErrors,
       "mscGsmBcFramerNonOctetErrors": mscGsmBcFramerNonOctetErrors,
       "mscGsmBcFramerOverruns": mscGsmBcFramerOverruns,
       "mscGsmBcFramerUnderruns": mscGsmBcFramerUnderruns,
       "mscGsmBcFramerLinkTable": mscGsmBcFramerLinkTable,
       "mscGsmBcFramerLinkEntry": mscGsmBcFramerLinkEntry,
       "mscGsmBcFramerFramingType": mscGsmBcFramerFramingType,
       "mscGsmBcFramerStateTable": mscGsmBcFramerStateTable,
       "mscGsmBcFramerStateEntry": mscGsmBcFramerStateEntry,
       "mscGsmBcFramerAdminState": mscGsmBcFramerAdminState,
       "mscGsmBcFramerOperationalState": mscGsmBcFramerOperationalState,
       "mscGsmBcFramerUsageState": mscGsmBcFramerUsageState,
       "mscGsmBcLayer1": mscGsmBcLayer1,
       "mscGsmBcLayer1RowStatusTable": mscGsmBcLayer1RowStatusTable,
       "mscGsmBcLayer1RowStatusEntry": mscGsmBcLayer1RowStatusEntry,
       "mscGsmBcLayer1RowStatus": mscGsmBcLayer1RowStatus,
       "mscGsmBcLayer1ComponentName": mscGsmBcLayer1ComponentName,
       "mscGsmBcLayer1StorageType": mscGsmBcLayer1StorageType,
       "mscGsmBcLayer1Index": mscGsmBcLayer1Index,
       "mscGsmBcLayer1OperTable": mscGsmBcLayer1OperTable,
       "mscGsmBcLayer1OperEntry": mscGsmBcLayer1OperEntry,
       "mscGsmBcLayer1ActiveMode": mscGsmBcLayer1ActiveMode,
       "mscGsmBcLayer1Connection": mscGsmBcLayer1Connection,
       "mscGsmBcLayer1DataRate": mscGsmBcLayer1DataRate,
       "mscGsmBcLayer1IntermediateRate": mscGsmBcLayer1IntermediateRate,
       "mscGsmBcLayer1StatsTable": mscGsmBcLayer1StatsTable,
       "mscGsmBcLayer1StatsEntry": mscGsmBcLayer1StatsEntry,
       "mscGsmBcLayer1FramesTx": mscGsmBcLayer1FramesTx,
       "mscGsmBcLayer1FramesRx": mscGsmBcLayer1FramesRx,
       "mscGsmBcLayer1BytesTx": mscGsmBcLayer1BytesTx,
       "mscGsmBcLayer1BytesRx": mscGsmBcLayer1BytesRx,
       "mscGsmBcLayer1UnderRunsTx": mscGsmBcLayer1UnderRunsTx,
       "mscGsmBcLayer1OverRunsRx": mscGsmBcLayer1OverRunsRx,
       "mscGsmBcLayer1NonOctetErrorsRx": mscGsmBcLayer1NonOctetErrorsRx,
       "mscGsmBcLayer1LargeFrameErrorsRx": mscGsmBcLayer1LargeFrameErrorsRx,
       "mscGsmBcLayer1FramesDiscarded": mscGsmBcLayer1FramesDiscarded,
       "mscGsmBcLayer1LrcErrorsTx": mscGsmBcLayer1LrcErrorsTx,
       "mscGsmBcModem": mscGsmBcModem,
       "mscGsmBcModemRowStatusTable": mscGsmBcModemRowStatusTable,
       "mscGsmBcModemRowStatusEntry": mscGsmBcModemRowStatusEntry,
       "mscGsmBcModemRowStatus": mscGsmBcModemRowStatus,
       "mscGsmBcModemComponentName": mscGsmBcModemComponentName,
       "mscGsmBcModemStorageType": mscGsmBcModemStorageType,
       "mscGsmBcModemIndex": mscGsmBcModemIndex,
       "mscGsmBcModemOperTable": mscGsmBcModemOperTable,
       "mscGsmBcModemOperEntry": mscGsmBcModemOperEntry,
       "mscGsmBcModemRate": mscGsmBcModemRate,
       "mscGsmBcModemAlgorithmInUse": mscGsmBcModemAlgorithmInUse,
       "mscGsmBcModemProtocolState": mscGsmBcModemProtocolState,
       "mscGsmBcModemReceiverTransmitter": mscGsmBcModemReceiverTransmitter,
       "mscGsmBcModemTraining": mscGsmBcModemTraining,
       "mscGsmBcModemToUpperFlowControlActive": mscGsmBcModemToUpperFlowControlActive,
       "mscGsmBcModemToDspFlowControlActive": mscGsmBcModemToDspFlowControlActive,
       "mscGsmBcModemAsyncMode": mscGsmBcModemAsyncMode,
       "mscGsmBcModemAutoHdlcMode": mscGsmBcModemAutoHdlcMode,
       "mscGsmBcModemOutbandFlowControl": mscGsmBcModemOutbandFlowControl,
       "mscGsmBcModemOutbandBreak": mscGsmBcModemOutbandBreak,
       "mscGsmBcModemAutobaud": mscGsmBcModemAutobaud,
       "mscGsmBcModemStatsTable": mscGsmBcModemStatsTable,
       "mscGsmBcModemStatsEntry": mscGsmBcModemStatsEntry,
       "mscGsmBcModemBytesTx": mscGsmBcModemBytesTx,
       "mscGsmBcModemBytesRx": mscGsmBcModemBytesRx,
       "mscGsmBcModemFramingErrors": mscGsmBcModemFramingErrors,
       "mscGsmBcV110": mscGsmBcV110,
       "mscGsmBcV110RowStatusTable": mscGsmBcV110RowStatusTable,
       "mscGsmBcV110RowStatusEntry": mscGsmBcV110RowStatusEntry,
       "mscGsmBcV110RowStatus": mscGsmBcV110RowStatus,
       "mscGsmBcV110ComponentName": mscGsmBcV110ComponentName,
       "mscGsmBcV110StorageType": mscGsmBcV110StorageType,
       "mscGsmBcV110Index": mscGsmBcV110Index,
       "mscGsmBcV110OperTable": mscGsmBcV110OperTable,
       "mscGsmBcV110OperEntry": mscGsmBcV110OperEntry,
       "mscGsmBcV110DataRate": mscGsmBcV110DataRate,
       "mscGsmBcV110IntermediateRate": mscGsmBcV110IntermediateRate,
       "mscGsmBcV110StatsTable": mscGsmBcV110StatsTable,
       "mscGsmBcV110StatsEntry": mscGsmBcV110StatsEntry,
       "mscGsmBcV110FramesTx": mscGsmBcV110FramesTx,
       "mscGsmBcV110FramesRx": mscGsmBcV110FramesRx,
       "mscGsmBcV110BytesTx": mscGsmBcV110BytesTx,
       "mscGsmBcV110BytesRx": mscGsmBcV110BytesRx,
       "mscGsmBcV110UnderRunsTx": mscGsmBcV110UnderRunsTx,
       "mscGsmBcV110OverRunsRx": mscGsmBcV110OverRunsRx,
       "mscGsmBcV110NonOctetErrorsRx": mscGsmBcV110NonOctetErrorsRx,
       "mscGsmBcV110LargeFrameErrorsRx": mscGsmBcV110LargeFrameErrorsRx,
       "mscGsmBcV110FramesDiscarded": mscGsmBcV110FramesDiscarded,
       "mscGsmBcV110LrcErrorsTx": mscGsmBcV110LrcErrorsTx,
       "mscGsmBcFax": mscGsmBcFax,
       "mscGsmBcFaxRowStatusTable": mscGsmBcFaxRowStatusTable,
       "mscGsmBcFaxRowStatusEntry": mscGsmBcFaxRowStatusEntry,
       "mscGsmBcFaxRowStatus": mscGsmBcFaxRowStatus,
       "mscGsmBcFaxComponentName": mscGsmBcFaxComponentName,
       "mscGsmBcFaxStorageType": mscGsmBcFaxStorageType,
       "mscGsmBcFaxIndex": mscGsmBcFaxIndex,
       "mscGsmBcFaxOperTable": mscGsmBcFaxOperTable,
       "mscGsmBcFaxOperEntry": mscGsmBcFaxOperEntry,
       "mscGsmBcFaxActiveMode": mscGsmBcFaxActiveMode,
       "mscGsmBcFaxProtocolState": mscGsmBcFaxProtocolState,
       "mscGsmBcFaxMessageRate": mscGsmBcFaxMessageRate,
       "mscGsmBcFaxStatsTable": mscGsmBcFaxStatsTable,
       "mscGsmBcFaxStatsEntry": mscGsmBcFaxStatsEntry,
       "mscGsmBcFaxMessageFramesRx": mscGsmBcFaxMessageFramesRx,
       "mscGsmBcFaxMessageFramesTx": mscGsmBcFaxMessageFramesTx,
       "mscGsmBcFaxBcsFramesRx": mscGsmBcFaxBcsFramesRx,
       "mscGsmBcFaxBcsFramesTx": mscGsmBcFaxBcsFramesTx,
       "mscGsmBcFaxPagesRxFromMobile": mscGsmBcFaxPagesRxFromMobile,
       "mscGsmBcFaxPagesTxToMobile": mscGsmBcFaxPagesTxToMobile,
       "mscGsmBcFaxChannelModeModify": mscGsmBcFaxChannelModeModify,
       "mscGsmBcFaxBcsFrameErrors": mscGsmBcFaxBcsFrameErrors,
       "mscGsmBcRlp": mscGsmBcRlp,
       "mscGsmBcRlpRowStatusTable": mscGsmBcRlpRowStatusTable,
       "mscGsmBcRlpRowStatusEntry": mscGsmBcRlpRowStatusEntry,
       "mscGsmBcRlpRowStatus": mscGsmBcRlpRowStatus,
       "mscGsmBcRlpComponentName": mscGsmBcRlpComponentName,
       "mscGsmBcRlpStorageType": mscGsmBcRlpStorageType,
       "mscGsmBcRlpIndex": mscGsmBcRlpIndex,
       "mscGsmBcRlpOperTable": mscGsmBcRlpOperTable,
       "mscGsmBcRlpOperEntry": mscGsmBcRlpOperEntry,
       "mscGsmBcRlpProtocolState": mscGsmBcRlpProtocolState,
       "mscGsmBcRlpFrameSize": mscGsmBcRlpFrameSize,
       "mscGsmBcRlpHighestVersion": mscGsmBcRlpHighestVersion,
       "mscGsmBcRlpIwfToMsWindowSize": mscGsmBcRlpIwfToMsWindowSize,
       "mscGsmBcRlpMsToIwfWindowSize": mscGsmBcRlpMsToIwfWindowSize,
       "mscGsmBcRlpT1AckTimer": mscGsmBcRlpT1AckTimer,
       "mscGsmBcRlpT2AckDelayTimer": mscGsmBcRlpT2AckDelayTimer,
       "mscGsmBcRlpN2RetransmitCount": mscGsmBcRlpN2RetransmitCount,
       "mscGsmBcRlpStatsTable": mscGsmBcRlpStatsTable,
       "mscGsmBcRlpStatsEntry": mscGsmBcRlpStatsEntry,
       "mscGsmBcRlpIFramesTx": mscGsmBcRlpIFramesTx,
       "mscGsmBcRlpIFramesRx": mscGsmBcRlpIFramesRx,
       "mscGsmBcRlpFramesRetransmitted": mscGsmBcRlpFramesRetransmitted,
       "mscGsmBcRlpT1AckTimeouts": mscGsmBcRlpT1AckTimeouts,
       "mscGsmBcRlpInvalidFrames": mscGsmBcRlpInvalidFrames,
       "mscGsmBcRlpCrcErrorsRx": mscGsmBcRlpCrcErrorsRx,
       "mscGsmBcRlpOutOfSequenceFrames": mscGsmBcRlpOutOfSequenceFrames,
       "mscGsmBcRlpRemoteBusyIndications": mscGsmBcRlpRemoteBusyIndications,
       "mscGsmBcRlpLocalBusyIndications": mscGsmBcRlpLocalBusyIndications,
       "mscGsmBcRlpIFramesTxDiscarded": mscGsmBcRlpIFramesTxDiscarded,
       "mscGsmBcRlpResetsRx": mscGsmBcRlpResetsRx,
       "mscGsmBcV42": mscGsmBcV42,
       "mscGsmBcV42RowStatusTable": mscGsmBcV42RowStatusTable,
       "mscGsmBcV42RowStatusEntry": mscGsmBcV42RowStatusEntry,
       "mscGsmBcV42RowStatus": mscGsmBcV42RowStatus,
       "mscGsmBcV42ComponentName": mscGsmBcV42ComponentName,
       "mscGsmBcV42StorageType": mscGsmBcV42StorageType,
       "mscGsmBcV42Index": mscGsmBcV42Index,
       "mscGsmBcV42OperTable": mscGsmBcV42OperTable,
       "mscGsmBcV42OperEntry": mscGsmBcV42OperEntry,
       "mscGsmBcV42ProtocolState": mscGsmBcV42ProtocolState,
       "mscGsmBcV42TxN401FrameSize": mscGsmBcV42TxN401FrameSize,
       "mscGsmBcV42RxN401FrameSize": mscGsmBcV42RxN401FrameSize,
       "mscGsmBcV42TxKwindowSize": mscGsmBcV42TxKwindowSize,
       "mscGsmBcV42RxKwindowSize": mscGsmBcV42RxKwindowSize,
       "mscGsmBcV42StatsTable": mscGsmBcV42StatsTable,
       "mscGsmBcV42StatsEntry": mscGsmBcV42StatsEntry,
       "mscGsmBcV42IBytesRx": mscGsmBcV42IBytesRx,
       "mscGsmBcV42IBytesTx": mscGsmBcV42IBytesTx,
       "mscGsmBcV42IFramesRx": mscGsmBcV42IFramesRx,
       "mscGsmBcV42IFramesTx": mscGsmBcV42IFramesTx,
       "mscGsmBcV42FramesRetransmitted": mscGsmBcV42FramesRetransmitted,
       "mscGsmBcV42T1AckTimeouts": mscGsmBcV42T1AckTimeouts,
       "mscGsmBcV42RemoteBusyIndications": mscGsmBcV42RemoteBusyIndications,
       "mscGsmBcV42LocalBusyIndications": mscGsmBcV42LocalBusyIndications,
       "mscGsmBcV42BadFramesRx": mscGsmBcV42BadFramesRx,
       "mscGsmBcV42CrcErrorsRx": mscGsmBcV42CrcErrorsRx,
       "mscGsmBcV42bis": mscGsmBcV42bis,
       "mscGsmBcV42bisRowStatusTable": mscGsmBcV42bisRowStatusTable,
       "mscGsmBcV42bisRowStatusEntry": mscGsmBcV42bisRowStatusEntry,
       "mscGsmBcV42bisRowStatus": mscGsmBcV42bisRowStatus,
       "mscGsmBcV42bisComponentName": mscGsmBcV42bisComponentName,
       "mscGsmBcV42bisStorageType": mscGsmBcV42bisStorageType,
       "mscGsmBcV42bisIndex": mscGsmBcV42bisIndex,
       "mscGsmBcV42bisOperTable": mscGsmBcV42bisOperTable,
       "mscGsmBcV42bisOperEntry": mscGsmBcV42bisOperEntry,
       "mscGsmBcV42bisProtocolModeEncoder": mscGsmBcV42bisProtocolModeEncoder,
       "mscGsmBcV42bisProtocolModeDecoder": mscGsmBcV42bisProtocolModeDecoder,
       "mscGsmBcV42bisCompressionDirection": mscGsmBcV42bisCompressionDirection,
       "mscGsmBcV42bisMaximumCodewords": mscGsmBcV42bisMaximumCodewords,
       "mscGsmBcV42bisMaximumStringSize": mscGsmBcV42bisMaximumStringSize,
       "mscGsmBcV42bisLastDecodeError": mscGsmBcV42bisLastDecodeError,
       "mscGsmBcV42bisCompRatioEncoder": mscGsmBcV42bisCompRatioEncoder,
       "mscGsmBcV42bisCompRatioDecoder": mscGsmBcV42bisCompRatioDecoder,
       "mscGsmBcV42bisStatsTable": mscGsmBcV42bisStatsTable,
       "mscGsmBcV42bisStatsEntry": mscGsmBcV42bisStatsEntry,
       "mscGsmBcV42bisModeChangesEncode": mscGsmBcV42bisModeChangesEncode,
       "mscGsmBcV42bisModeChangesDecode": mscGsmBcV42bisModeChangesDecode,
       "mscGsmBcV42bisResetsEncode": mscGsmBcV42bisResetsEncode,
       "mscGsmBcV42bisResetsDecode": mscGsmBcV42bisResetsDecode,
       "mscGsmBcV42bisReInitializations": mscGsmBcV42bisReInitializations,
       "mscGsmBcV42bisErrorsInDecode": mscGsmBcV42bisErrorsInDecode,
       "mscGsmBcL2RCop": mscGsmBcL2RCop,
       "mscGsmBcL2RCopRowStatusTable": mscGsmBcL2RCopRowStatusTable,
       "mscGsmBcL2RCopRowStatusEntry": mscGsmBcL2RCopRowStatusEntry,
       "mscGsmBcL2RCopRowStatus": mscGsmBcL2RCopRowStatus,
       "mscGsmBcL2RCopComponentName": mscGsmBcL2RCopComponentName,
       "mscGsmBcL2RCopStorageType": mscGsmBcL2RCopStorageType,
       "mscGsmBcL2RCopIndex": mscGsmBcL2RCopIndex,
       "mscGsmBcL2RCopOperTable": mscGsmBcL2RCopOperTable,
       "mscGsmBcL2RCopOperEntry": mscGsmBcL2RCopOperEntry,
       "mscGsmBcL2RCopFlowControlStateTx": mscGsmBcL2RCopFlowControlStateTx,
       "mscGsmBcL2RCopFlowControlStateRx": mscGsmBcL2RCopFlowControlStateRx,
       "mscGsmBcL2RCopStatsTable": mscGsmBcL2RCopStatsTable,
       "mscGsmBcL2RCopStatsEntry": mscGsmBcL2RCopStatsEntry,
       "mscGsmBcL2RCopBytesTx": mscGsmBcL2RCopBytesTx,
       "mscGsmBcL2RCopBytesRx": mscGsmBcL2RCopBytesRx,
       "mscGsmBcL2RCopBreakCountRx": mscGsmBcL2RCopBreakCountRx,
       "mscGsmBcL2RCopBreakCountTx": mscGsmBcL2RCopBreakCountTx,
       "mscGsmBcUpperRelay": mscGsmBcUpperRelay,
       "mscGsmBcUpperRelayRowStatusTable": mscGsmBcUpperRelayRowStatusTable,
       "mscGsmBcUpperRelayRowStatusEntry": mscGsmBcUpperRelayRowStatusEntry,
       "mscGsmBcUpperRelayRowStatus": mscGsmBcUpperRelayRowStatus,
       "mscGsmBcUpperRelayComponentName": mscGsmBcUpperRelayComponentName,
       "mscGsmBcUpperRelayStorageType": mscGsmBcUpperRelayStorageType,
       "mscGsmBcUpperRelayIndex": mscGsmBcUpperRelayIndex,
       "mscGsmBcUpperRelayOperTable": mscGsmBcUpperRelayOperTable,
       "mscGsmBcUpperRelayOperEntry": mscGsmBcUpperRelayOperEntry,
       "mscGsmBcUpperRelayBufferSize": mscGsmBcUpperRelayBufferSize,
       "mscGsmBcUpperRelayFlowControlStateTx": mscGsmBcUpperRelayFlowControlStateTx,
       "mscGsmBcUpperRelayFlowControlStateRx": mscGsmBcUpperRelayFlowControlStateRx,
       "mscGsmBcUpperRelayStatsTable": mscGsmBcUpperRelayStatsTable,
       "mscGsmBcUpperRelayStatsEntry": mscGsmBcUpperRelayStatsEntry,
       "mscGsmBcUpperRelayFramesTx": mscGsmBcUpperRelayFramesTx,
       "mscGsmBcUpperRelayFramesRx": mscGsmBcUpperRelayFramesRx,
       "mscGsmBcUpperRelayUnacknowledgedFrames": mscGsmBcUpperRelayUnacknowledgedFrames,
       "mscGsmBcOperTable": mscGsmBcOperTable,
       "mscGsmBcOperEntry": mscGsmBcOperEntry,
       "mscGsmBcMipState": mscGsmBcMipState,
       "mscGsmBcMaxUserDataRate": mscGsmBcMaxUserDataRate,
       "mscGsmBcConnectionType": mscGsmBcConnectionType,
       "mscGsmBcDataBits": mscGsmBcDataBits,
       "mscGsmBcStopBits": mscGsmBcStopBits,
       "mscGsmBcParity": mscGsmBcParity,
       "mscGsmBcFlowControl": mscGsmBcFlowControl,
       "mscGsmBcCallType": mscGsmBcCallType,
       "mscGsmBcLastResponseCode": mscGsmBcLastResponseCode,
       "mscGsmBcMateBearerChannel": mscGsmBcMateBearerChannel,
       "mscGsmBcCidDataTable": mscGsmBcCidDataTable,
       "mscGsmBcCidDataEntry": mscGsmBcCidDataEntry,
       "mscGsmBcCustomerIdentifier": mscGsmBcCustomerIdentifier,
       "mscGsmBcStateTable": mscGsmBcStateTable,
       "mscGsmBcStateEntry": mscGsmBcStateEntry,
       "mscGsmBcAdminState": mscGsmBcAdminState,
       "mscGsmBcOperationalState": mscGsmBcOperationalState,
       "mscGsmBcUsageState": mscGsmBcUsageState,
       "gsmIwfMIB": gsmIwfMIB,
       "gsmIwfGroup": gsmIwfGroup,
       "gsmIwfGroupCA": gsmIwfGroupCA,
       "gsmIwfGroupCA02": gsmIwfGroupCA02,
       "gsmIwfGroupCA02A": gsmIwfGroupCA02A,
       "gsmIwfCapabilities": gsmIwfCapabilities,
       "gsmIwfCapabilitiesCA": gsmIwfCapabilitiesCA,
       "gsmIwfCapabilitiesCA02": gsmIwfCapabilitiesCA02,
       "gsmIwfCapabilitiesCA02A": gsmIwfCapabilitiesCA02A}
)
