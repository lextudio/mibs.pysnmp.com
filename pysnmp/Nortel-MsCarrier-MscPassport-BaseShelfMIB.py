# SNMP MIB module (Nortel-MsCarrier-MscPassport-BaseShelfMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-BaseShelfMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:58 2024
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

(DisplayString,
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 ExtendedAsciiString,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "ExtendedAsciiString",
    "Hex",
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

_MscShelf_ObjectIdentity = ObjectIdentity
mscShelf = _MscShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13)
)
_MscShelfRowStatusTable_Object = MibTable
mscShelfRowStatusTable = _MscShelfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 1)
)
if mibBuilder.loadTexts:
    mscShelfRowStatusTable.setStatus("mandatory")
_MscShelfRowStatusEntry_Object = MibTableRow
mscShelfRowStatusEntry = _MscShelfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 1, 1)
)
mscShelfRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
)
if mibBuilder.loadTexts:
    mscShelfRowStatusEntry.setStatus("mandatory")
_MscShelfRowStatus_Type = RowStatus
_MscShelfRowStatus_Object = MibTableColumn
mscShelfRowStatus = _MscShelfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 1, 1, 1),
    _MscShelfRowStatus_Type()
)
mscShelfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfRowStatus.setStatus("mandatory")
_MscShelfComponentName_Type = DisplayString
_MscShelfComponentName_Object = MibTableColumn
mscShelfComponentName = _MscShelfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 1, 1, 2),
    _MscShelfComponentName_Type()
)
mscShelfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfComponentName.setStatus("mandatory")
_MscShelfStorageType_Type = StorageType
_MscShelfStorageType_Object = MibTableColumn
mscShelfStorageType = _MscShelfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 1, 1, 4),
    _MscShelfStorageType_Type()
)
mscShelfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfStorageType.setStatus("mandatory")
_MscShelfIndex_Type = NonReplicated
_MscShelfIndex_Object = MibTableColumn
mscShelfIndex = _MscShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 1, 1, 10),
    _MscShelfIndex_Type()
)
mscShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfIndex.setStatus("mandatory")
_MscShelfCard_ObjectIdentity = ObjectIdentity
mscShelfCard = _MscShelfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2)
)
_MscShelfCardRowStatusTable_Object = MibTable
mscShelfCardRowStatusTable = _MscShelfCardRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardRowStatusTable.setStatus("mandatory")
_MscShelfCardRowStatusEntry_Object = MibTableRow
mscShelfCardRowStatusEntry = _MscShelfCardRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 1, 1)
)
mscShelfCardRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardRowStatusEntry.setStatus("mandatory")
_MscShelfCardRowStatus_Type = RowStatus
_MscShelfCardRowStatus_Object = MibTableColumn
mscShelfCardRowStatus = _MscShelfCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 1, 1, 1),
    _MscShelfCardRowStatus_Type()
)
mscShelfCardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardRowStatus.setStatus("mandatory")
_MscShelfCardComponentName_Type = DisplayString
_MscShelfCardComponentName_Object = MibTableColumn
mscShelfCardComponentName = _MscShelfCardComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 1, 1, 2),
    _MscShelfCardComponentName_Type()
)
mscShelfCardComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardComponentName.setStatus("mandatory")
_MscShelfCardStorageType_Type = StorageType
_MscShelfCardStorageType_Object = MibTableColumn
mscShelfCardStorageType = _MscShelfCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 1, 1, 4),
    _MscShelfCardStorageType_Type()
)
mscShelfCardStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardStorageType.setStatus("mandatory")


class _MscShelfCardIndex_Type(Integer32):
    """Custom type mscShelfCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfCardIndex_Type.__name__ = "Integer32"
_MscShelfCardIndex_Object = MibTableColumn
mscShelfCardIndex = _MscShelfCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 1, 1, 10),
    _MscShelfCardIndex_Type()
)
mscShelfCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardIndex.setStatus("mandatory")
_MscShelfCardTest_ObjectIdentity = ObjectIdentity
mscShelfCardTest = _MscShelfCardTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3)
)
_MscShelfCardTestRowStatusTable_Object = MibTable
mscShelfCardTestRowStatusTable = _MscShelfCardTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardTestRowStatusTable.setStatus("mandatory")
_MscShelfCardTestRowStatusEntry_Object = MibTableRow
mscShelfCardTestRowStatusEntry = _MscShelfCardTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 1, 1)
)
mscShelfCardTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardTestRowStatusEntry.setStatus("mandatory")
_MscShelfCardTestRowStatus_Type = RowStatus
_MscShelfCardTestRowStatus_Object = MibTableColumn
mscShelfCardTestRowStatus = _MscShelfCardTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 1, 1, 1),
    _MscShelfCardTestRowStatus_Type()
)
mscShelfCardTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestRowStatus.setStatus("mandatory")
_MscShelfCardTestComponentName_Type = DisplayString
_MscShelfCardTestComponentName_Object = MibTableColumn
mscShelfCardTestComponentName = _MscShelfCardTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 1, 1, 2),
    _MscShelfCardTestComponentName_Type()
)
mscShelfCardTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestComponentName.setStatus("mandatory")
_MscShelfCardTestStorageType_Type = StorageType
_MscShelfCardTestStorageType_Object = MibTableColumn
mscShelfCardTestStorageType = _MscShelfCardTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 1, 1, 4),
    _MscShelfCardTestStorageType_Type()
)
mscShelfCardTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestStorageType.setStatus("mandatory")
_MscShelfCardTestIndex_Type = NonReplicated
_MscShelfCardTestIndex_Object = MibTableColumn
mscShelfCardTestIndex = _MscShelfCardTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 1, 1, 10),
    _MscShelfCardTestIndex_Type()
)
mscShelfCardTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardTestIndex.setStatus("mandatory")
_MscShelfCardTestStateTable_Object = MibTable
mscShelfCardTestStateTable = _MscShelfCardTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscShelfCardTestStateTable.setStatus("mandatory")
_MscShelfCardTestStateEntry_Object = MibTableRow
mscShelfCardTestStateEntry = _MscShelfCardTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 10, 1)
)
mscShelfCardTestStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardTestStateEntry.setStatus("mandatory")


class _MscShelfCardTestAdminState_Type(Integer32):
    """Custom type mscShelfCardTestAdminState based on Integer32"""
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


_MscShelfCardTestAdminState_Type.__name__ = "Integer32"
_MscShelfCardTestAdminState_Object = MibTableColumn
mscShelfCardTestAdminState = _MscShelfCardTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 10, 1, 1),
    _MscShelfCardTestAdminState_Type()
)
mscShelfCardTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestAdminState.setStatus("mandatory")


class _MscShelfCardTestOperationalState_Type(Integer32):
    """Custom type mscShelfCardTestOperationalState based on Integer32"""
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


_MscShelfCardTestOperationalState_Type.__name__ = "Integer32"
_MscShelfCardTestOperationalState_Object = MibTableColumn
mscShelfCardTestOperationalState = _MscShelfCardTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 10, 1, 2),
    _MscShelfCardTestOperationalState_Type()
)
mscShelfCardTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestOperationalState.setStatus("mandatory")


class _MscShelfCardTestUsageState_Type(Integer32):
    """Custom type mscShelfCardTestUsageState based on Integer32"""
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


_MscShelfCardTestUsageState_Type.__name__ = "Integer32"
_MscShelfCardTestUsageState_Object = MibTableColumn
mscShelfCardTestUsageState = _MscShelfCardTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 10, 1, 3),
    _MscShelfCardTestUsageState_Type()
)
mscShelfCardTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestUsageState.setStatus("mandatory")
_MscShelfCardTestSetupTable_Object = MibTable
mscShelfCardTestSetupTable = _MscShelfCardTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mscShelfCardTestSetupTable.setStatus("mandatory")
_MscShelfCardTestSetupEntry_Object = MibTableRow
mscShelfCardTestSetupEntry = _MscShelfCardTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 11, 1)
)
mscShelfCardTestSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardTestSetupEntry.setStatus("mandatory")


class _MscShelfCardTestTargetCard_Type(Unsigned32):
    """Custom type mscShelfCardTestTargetCard based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfCardTestTargetCard_Type.__name__ = "Unsigned32"
_MscShelfCardTestTargetCard_Object = MibTableColumn
mscShelfCardTestTargetCard = _MscShelfCardTestTargetCard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 11, 1, 1),
    _MscShelfCardTestTargetCard_Type()
)
mscShelfCardTestTargetCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardTestTargetCard.setStatus("mandatory")


class _MscShelfCardTestFrmTypes_Type(OctetString):
    """Custom type mscShelfCardTestFrmTypes based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardTestFrmTypes_Type.__name__ = "OctetString"
_MscShelfCardTestFrmTypes_Object = MibTableColumn
mscShelfCardTestFrmTypes = _MscShelfCardTestFrmTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 11, 1, 2),
    _MscShelfCardTestFrmTypes_Type()
)
mscShelfCardTestFrmTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardTestFrmTypes.setStatus("mandatory")


class _MscShelfCardTestFrmPriorities_Type(OctetString):
    """Custom type mscShelfCardTestFrmPriorities based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardTestFrmPriorities_Type.__name__ = "OctetString"
_MscShelfCardTestFrmPriorities_Object = MibTableColumn
mscShelfCardTestFrmPriorities = _MscShelfCardTestFrmPriorities_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 11, 1, 3),
    _MscShelfCardTestFrmPriorities_Type()
)
mscShelfCardTestFrmPriorities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardTestFrmPriorities.setStatus("mandatory")


class _MscShelfCardTestFrmPatternType_Type(Integer32):
    """Custom type mscShelfCardTestFrmPatternType based on Integer32"""
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
        *(("ccitt32kBitPattern", 0),
          ("ccitt8MBitPattern", 1),
          ("customizedPattern", 2))
    )


_MscShelfCardTestFrmPatternType_Type.__name__ = "Integer32"
_MscShelfCardTestFrmPatternType_Object = MibTableColumn
mscShelfCardTestFrmPatternType = _MscShelfCardTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 11, 1, 4),
    _MscShelfCardTestFrmPatternType_Type()
)
mscShelfCardTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardTestFrmPatternType.setStatus("mandatory")


class _MscShelfCardTestCustomizedPattern_Type(Hex):
    """Custom type mscShelfCardTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardTestCustomizedPattern_Type.__name__ = "Hex"
_MscShelfCardTestCustomizedPattern_Object = MibTableColumn
mscShelfCardTestCustomizedPattern = _MscShelfCardTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 11, 1, 5),
    _MscShelfCardTestCustomizedPattern_Type()
)
mscShelfCardTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardTestCustomizedPattern.setStatus("mandatory")


class _MscShelfCardTestDuration_Type(Unsigned32):
    """Custom type mscShelfCardTestDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 43200),
    )


_MscShelfCardTestDuration_Type.__name__ = "Unsigned32"
_MscShelfCardTestDuration_Object = MibTableColumn
mscShelfCardTestDuration = _MscShelfCardTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 11, 1, 6),
    _MscShelfCardTestDuration_Type()
)
mscShelfCardTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardTestDuration.setStatus("mandatory")
_MscShelfCardTestResultsTable_Object = MibTable
mscShelfCardTestResultsTable = _MscShelfCardTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 12)
)
if mibBuilder.loadTexts:
    mscShelfCardTestResultsTable.setStatus("mandatory")
_MscShelfCardTestResultsEntry_Object = MibTableRow
mscShelfCardTestResultsEntry = _MscShelfCardTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 12, 1)
)
mscShelfCardTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardTestResultsEntry.setStatus("mandatory")


class _MscShelfCardTestElapsedTime_Type(Unsigned32):
    """Custom type mscShelfCardTestElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_MscShelfCardTestElapsedTime_Type.__name__ = "Unsigned32"
_MscShelfCardTestElapsedTime_Object = MibTableColumn
mscShelfCardTestElapsedTime = _MscShelfCardTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 12, 1, 1),
    _MscShelfCardTestElapsedTime_Type()
)
mscShelfCardTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestElapsedTime.setStatus("mandatory")


class _MscShelfCardTestTimeRemaining_Type(Unsigned32):
    """Custom type mscShelfCardTestTimeRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_MscShelfCardTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscShelfCardTestTimeRemaining_Object = MibTableColumn
mscShelfCardTestTimeRemaining = _MscShelfCardTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 12, 1, 2),
    _MscShelfCardTestTimeRemaining_Type()
)
mscShelfCardTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestTimeRemaining.setStatus("mandatory")


class _MscShelfCardTestCauseOfTermination_Type(Integer32):
    """Custom type mscShelfCardTestCauseOfTermination based on Integer32"""
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
        *(("becameActive", 5),
          ("neverStarted", 0),
          ("stoppedByOperator", 3),
          ("targetFailed", 4),
          ("testRunning", 1),
          ("testTimeExpired", 2))
    )


_MscShelfCardTestCauseOfTermination_Type.__name__ = "Integer32"
_MscShelfCardTestCauseOfTermination_Object = MibTableColumn
mscShelfCardTestCauseOfTermination = _MscShelfCardTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 12, 1, 3),
    _MscShelfCardTestCauseOfTermination_Type()
)
mscShelfCardTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestCauseOfTermination.setStatus("mandatory")
_MscShelfCardTestSizeTable_Object = MibTable
mscShelfCardTestSizeTable = _MscShelfCardTestSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 253)
)
if mibBuilder.loadTexts:
    mscShelfCardTestSizeTable.setStatus("mandatory")
_MscShelfCardTestSizeEntry_Object = MibTableRow
mscShelfCardTestSizeEntry = _MscShelfCardTestSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 253, 1)
)
mscShelfCardTestSizeEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestSizeIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardTestSizeEntry.setStatus("mandatory")


class _MscShelfCardTestSizeIndex_Type(Integer32):
    """Custom type mscShelfCardTestSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 0))
    )


_MscShelfCardTestSizeIndex_Type.__name__ = "Integer32"
_MscShelfCardTestSizeIndex_Object = MibTableColumn
mscShelfCardTestSizeIndex = _MscShelfCardTestSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 253, 1, 1),
    _MscShelfCardTestSizeIndex_Type()
)
mscShelfCardTestSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardTestSizeIndex.setStatus("mandatory")


class _MscShelfCardTestSizeValue_Type(Unsigned32):
    """Custom type mscShelfCardTestSizeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16000),
    )


_MscShelfCardTestSizeValue_Type.__name__ = "Unsigned32"
_MscShelfCardTestSizeValue_Object = MibTableColumn
mscShelfCardTestSizeValue = _MscShelfCardTestSizeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 253, 1, 2),
    _MscShelfCardTestSizeValue_Type()
)
mscShelfCardTestSizeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardTestSizeValue.setStatus("mandatory")
_MscShelfCardTestLoadingFrmDataTable_Object = MibTable
mscShelfCardTestLoadingFrmDataTable = _MscShelfCardTestLoadingFrmDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 254)
)
if mibBuilder.loadTexts:
    mscShelfCardTestLoadingFrmDataTable.setStatus("mandatory")
_MscShelfCardTestLoadingFrmDataEntry_Object = MibTableRow
mscShelfCardTestLoadingFrmDataEntry = _MscShelfCardTestLoadingFrmDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 254, 1)
)
mscShelfCardTestLoadingFrmDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestLoadingFrmDataResultsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestLoadingFrmDataPriorityIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardTestLoadingFrmDataEntry.setStatus("mandatory")


class _MscShelfCardTestLoadingFrmDataResultsIndex_Type(Integer32):
    """Custom type mscShelfCardTestLoadingFrmDataResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("framesLost", 1),
          ("framesSent", 0))
    )


_MscShelfCardTestLoadingFrmDataResultsIndex_Type.__name__ = "Integer32"
_MscShelfCardTestLoadingFrmDataResultsIndex_Object = MibTableColumn
mscShelfCardTestLoadingFrmDataResultsIndex = _MscShelfCardTestLoadingFrmDataResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 254, 1, 1),
    _MscShelfCardTestLoadingFrmDataResultsIndex_Type()
)
mscShelfCardTestLoadingFrmDataResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardTestLoadingFrmDataResultsIndex.setStatus("mandatory")


class _MscShelfCardTestLoadingFrmDataPriorityIndex_Type(Integer32):
    """Custom type mscShelfCardTestLoadingFrmDataPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_MscShelfCardTestLoadingFrmDataPriorityIndex_Type.__name__ = "Integer32"
_MscShelfCardTestLoadingFrmDataPriorityIndex_Object = MibTableColumn
mscShelfCardTestLoadingFrmDataPriorityIndex = _MscShelfCardTestLoadingFrmDataPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 254, 1, 2),
    _MscShelfCardTestLoadingFrmDataPriorityIndex_Type()
)
mscShelfCardTestLoadingFrmDataPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardTestLoadingFrmDataPriorityIndex.setStatus("mandatory")


class _MscShelfCardTestLoadingFrmDataValue_Type(Unsigned32):
    """Custom type mscShelfCardTestLoadingFrmDataValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardTestLoadingFrmDataValue_Type.__name__ = "Unsigned32"
_MscShelfCardTestLoadingFrmDataValue_Object = MibTableColumn
mscShelfCardTestLoadingFrmDataValue = _MscShelfCardTestLoadingFrmDataValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 254, 1, 3),
    _MscShelfCardTestLoadingFrmDataValue_Type()
)
mscShelfCardTestLoadingFrmDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestLoadingFrmDataValue.setStatus("mandatory")
_MscShelfCardTestVerificationFrmDataTable_Object = MibTable
mscShelfCardTestVerificationFrmDataTable = _MscShelfCardTestVerificationFrmDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 255)
)
if mibBuilder.loadTexts:
    mscShelfCardTestVerificationFrmDataTable.setStatus("mandatory")
_MscShelfCardTestVerificationFrmDataEntry_Object = MibTableRow
mscShelfCardTestVerificationFrmDataEntry = _MscShelfCardTestVerificationFrmDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 255, 1)
)
mscShelfCardTestVerificationFrmDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestVerificationFrmDataResultsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardTestVerificationFrmDataPriorityIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardTestVerificationFrmDataEntry.setStatus("mandatory")


class _MscShelfCardTestVerificationFrmDataResultsIndex_Type(Integer32):
    """Custom type mscShelfCardTestVerificationFrmDataResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("framesBad", 1),
          ("framesTested", 0))
    )


_MscShelfCardTestVerificationFrmDataResultsIndex_Type.__name__ = "Integer32"
_MscShelfCardTestVerificationFrmDataResultsIndex_Object = MibTableColumn
mscShelfCardTestVerificationFrmDataResultsIndex = _MscShelfCardTestVerificationFrmDataResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 255, 1, 1),
    _MscShelfCardTestVerificationFrmDataResultsIndex_Type()
)
mscShelfCardTestVerificationFrmDataResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardTestVerificationFrmDataResultsIndex.setStatus("mandatory")


class _MscShelfCardTestVerificationFrmDataPriorityIndex_Type(Integer32):
    """Custom type mscShelfCardTestVerificationFrmDataPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_MscShelfCardTestVerificationFrmDataPriorityIndex_Type.__name__ = "Integer32"
_MscShelfCardTestVerificationFrmDataPriorityIndex_Object = MibTableColumn
mscShelfCardTestVerificationFrmDataPriorityIndex = _MscShelfCardTestVerificationFrmDataPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 255, 1, 2),
    _MscShelfCardTestVerificationFrmDataPriorityIndex_Type()
)
mscShelfCardTestVerificationFrmDataPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardTestVerificationFrmDataPriorityIndex.setStatus("mandatory")


class _MscShelfCardTestVerificationFrmDataValue_Type(Unsigned32):
    """Custom type mscShelfCardTestVerificationFrmDataValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardTestVerificationFrmDataValue_Type.__name__ = "Unsigned32"
_MscShelfCardTestVerificationFrmDataValue_Object = MibTableColumn
mscShelfCardTestVerificationFrmDataValue = _MscShelfCardTestVerificationFrmDataValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 3, 255, 1, 3),
    _MscShelfCardTestVerificationFrmDataValue_Type()
)
mscShelfCardTestVerificationFrmDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTestVerificationFrmDataValue.setStatus("mandatory")
_MscShelfCardDiag_ObjectIdentity = ObjectIdentity
mscShelfCardDiag = _MscShelfCardDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4)
)
_MscShelfCardDiagRowStatusTable_Object = MibTable
mscShelfCardDiagRowStatusTable = _MscShelfCardDiagRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardDiagRowStatusTable.setStatus("mandatory")
_MscShelfCardDiagRowStatusEntry_Object = MibTableRow
mscShelfCardDiagRowStatusEntry = _MscShelfCardDiagRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 1, 1)
)
mscShelfCardDiagRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardDiagRowStatusEntry.setStatus("mandatory")
_MscShelfCardDiagRowStatus_Type = RowStatus
_MscShelfCardDiagRowStatus_Object = MibTableColumn
mscShelfCardDiagRowStatus = _MscShelfCardDiagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 1, 1, 1),
    _MscShelfCardDiagRowStatus_Type()
)
mscShelfCardDiagRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagRowStatus.setStatus("mandatory")
_MscShelfCardDiagComponentName_Type = DisplayString
_MscShelfCardDiagComponentName_Object = MibTableColumn
mscShelfCardDiagComponentName = _MscShelfCardDiagComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 1, 1, 2),
    _MscShelfCardDiagComponentName_Type()
)
mscShelfCardDiagComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagComponentName.setStatus("mandatory")
_MscShelfCardDiagStorageType_Type = StorageType
_MscShelfCardDiagStorageType_Object = MibTableColumn
mscShelfCardDiagStorageType = _MscShelfCardDiagStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 1, 1, 4),
    _MscShelfCardDiagStorageType_Type()
)
mscShelfCardDiagStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagStorageType.setStatus("mandatory")
_MscShelfCardDiagIndex_Type = NonReplicated
_MscShelfCardDiagIndex_Object = MibTableColumn
mscShelfCardDiagIndex = _MscShelfCardDiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 1, 1, 10),
    _MscShelfCardDiagIndex_Type()
)
mscShelfCardDiagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardDiagIndex.setStatus("mandatory")
_MscShelfCardDiagTrapData_ObjectIdentity = ObjectIdentity
mscShelfCardDiagTrapData = _MscShelfCardDiagTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2)
)
_MscShelfCardDiagTrapDataRowStatusTable_Object = MibTable
mscShelfCardDiagTrapDataRowStatusTable = _MscShelfCardDiagTrapDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataRowStatusTable.setStatus("mandatory")
_MscShelfCardDiagTrapDataRowStatusEntry_Object = MibTableRow
mscShelfCardDiagTrapDataRowStatusEntry = _MscShelfCardDiagTrapDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 1, 1)
)
mscShelfCardDiagTrapDataRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagTrapDataIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataRowStatusEntry.setStatus("mandatory")
_MscShelfCardDiagTrapDataRowStatus_Type = RowStatus
_MscShelfCardDiagTrapDataRowStatus_Object = MibTableColumn
mscShelfCardDiagTrapDataRowStatus = _MscShelfCardDiagTrapDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 1, 1, 1),
    _MscShelfCardDiagTrapDataRowStatus_Type()
)
mscShelfCardDiagTrapDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataRowStatus.setStatus("mandatory")
_MscShelfCardDiagTrapDataComponentName_Type = DisplayString
_MscShelfCardDiagTrapDataComponentName_Object = MibTableColumn
mscShelfCardDiagTrapDataComponentName = _MscShelfCardDiagTrapDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 1, 1, 2),
    _MscShelfCardDiagTrapDataComponentName_Type()
)
mscShelfCardDiagTrapDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataComponentName.setStatus("mandatory")
_MscShelfCardDiagTrapDataStorageType_Type = StorageType
_MscShelfCardDiagTrapDataStorageType_Object = MibTableColumn
mscShelfCardDiagTrapDataStorageType = _MscShelfCardDiagTrapDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 1, 1, 4),
    _MscShelfCardDiagTrapDataStorageType_Type()
)
mscShelfCardDiagTrapDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataStorageType.setStatus("mandatory")
_MscShelfCardDiagTrapDataIndex_Type = NonReplicated
_MscShelfCardDiagTrapDataIndex_Object = MibTableColumn
mscShelfCardDiagTrapDataIndex = _MscShelfCardDiagTrapDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 1, 1, 10),
    _MscShelfCardDiagTrapDataIndex_Type()
)
mscShelfCardDiagTrapDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataIndex.setStatus("mandatory")
_MscShelfCardDiagTrapDataLine_ObjectIdentity = ObjectIdentity
mscShelfCardDiagTrapDataLine = _MscShelfCardDiagTrapDataLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2)
)
_MscShelfCardDiagTrapDataLineRowStatusTable_Object = MibTable
mscShelfCardDiagTrapDataLineRowStatusTable = _MscShelfCardDiagTrapDataLineRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataLineRowStatusTable.setStatus("mandatory")
_MscShelfCardDiagTrapDataLineRowStatusEntry_Object = MibTableRow
mscShelfCardDiagTrapDataLineRowStatusEntry = _MscShelfCardDiagTrapDataLineRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2, 1, 1)
)
mscShelfCardDiagTrapDataLineRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagTrapDataIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagTrapDataLineIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataLineRowStatusEntry.setStatus("mandatory")
_MscShelfCardDiagTrapDataLineRowStatus_Type = RowStatus
_MscShelfCardDiagTrapDataLineRowStatus_Object = MibTableColumn
mscShelfCardDiagTrapDataLineRowStatus = _MscShelfCardDiagTrapDataLineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2, 1, 1, 1),
    _MscShelfCardDiagTrapDataLineRowStatus_Type()
)
mscShelfCardDiagTrapDataLineRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataLineRowStatus.setStatus("mandatory")
_MscShelfCardDiagTrapDataLineComponentName_Type = DisplayString
_MscShelfCardDiagTrapDataLineComponentName_Object = MibTableColumn
mscShelfCardDiagTrapDataLineComponentName = _MscShelfCardDiagTrapDataLineComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2, 1, 1, 2),
    _MscShelfCardDiagTrapDataLineComponentName_Type()
)
mscShelfCardDiagTrapDataLineComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataLineComponentName.setStatus("mandatory")
_MscShelfCardDiagTrapDataLineStorageType_Type = StorageType
_MscShelfCardDiagTrapDataLineStorageType_Object = MibTableColumn
mscShelfCardDiagTrapDataLineStorageType = _MscShelfCardDiagTrapDataLineStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2, 1, 1, 4),
    _MscShelfCardDiagTrapDataLineStorageType_Type()
)
mscShelfCardDiagTrapDataLineStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataLineStorageType.setStatus("mandatory")


class _MscShelfCardDiagTrapDataLineIndex_Type(Integer32):
    """Custom type mscShelfCardDiagTrapDataLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_MscShelfCardDiagTrapDataLineIndex_Type.__name__ = "Integer32"
_MscShelfCardDiagTrapDataLineIndex_Object = MibTableColumn
mscShelfCardDiagTrapDataLineIndex = _MscShelfCardDiagTrapDataLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2, 1, 1, 10),
    _MscShelfCardDiagTrapDataLineIndex_Type()
)
mscShelfCardDiagTrapDataLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataLineIndex.setStatus("mandatory")
_MscShelfCardDiagTrapDataLineOperTable_Object = MibTable
mscShelfCardDiagTrapDataLineOperTable = _MscShelfCardDiagTrapDataLineOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataLineOperTable.setStatus("mandatory")
_MscShelfCardDiagTrapDataLineOperEntry_Object = MibTableRow
mscShelfCardDiagTrapDataLineOperEntry = _MscShelfCardDiagTrapDataLineOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2, 10, 1)
)
mscShelfCardDiagTrapDataLineOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagTrapDataIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagTrapDataLineIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataLineOperEntry.setStatus("mandatory")


class _MscShelfCardDiagTrapDataLineData_Type(ExtendedAsciiString):
    """Custom type mscShelfCardDiagTrapDataLineData based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MscShelfCardDiagTrapDataLineData_Type.__name__ = "ExtendedAsciiString"
_MscShelfCardDiagTrapDataLineData_Object = MibTableColumn
mscShelfCardDiagTrapDataLineData = _MscShelfCardDiagTrapDataLineData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 2, 2, 10, 1, 1),
    _MscShelfCardDiagTrapDataLineData_Type()
)
mscShelfCardDiagTrapDataLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagTrapDataLineData.setStatus("mandatory")
_MscShelfCardDiagRecErr_ObjectIdentity = ObjectIdentity
mscShelfCardDiagRecErr = _MscShelfCardDiagRecErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3)
)
_MscShelfCardDiagRecErrRowStatusTable_Object = MibTable
mscShelfCardDiagRecErrRowStatusTable = _MscShelfCardDiagRecErrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrRowStatusTable.setStatus("mandatory")
_MscShelfCardDiagRecErrRowStatusEntry_Object = MibTableRow
mscShelfCardDiagRecErrRowStatusEntry = _MscShelfCardDiagRecErrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 1, 1)
)
mscShelfCardDiagRecErrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagRecErrIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrRowStatusEntry.setStatus("mandatory")
_MscShelfCardDiagRecErrRowStatus_Type = RowStatus
_MscShelfCardDiagRecErrRowStatus_Object = MibTableColumn
mscShelfCardDiagRecErrRowStatus = _MscShelfCardDiagRecErrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 1, 1, 1),
    _MscShelfCardDiagRecErrRowStatus_Type()
)
mscShelfCardDiagRecErrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrRowStatus.setStatus("mandatory")
_MscShelfCardDiagRecErrComponentName_Type = DisplayString
_MscShelfCardDiagRecErrComponentName_Object = MibTableColumn
mscShelfCardDiagRecErrComponentName = _MscShelfCardDiagRecErrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 1, 1, 2),
    _MscShelfCardDiagRecErrComponentName_Type()
)
mscShelfCardDiagRecErrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrComponentName.setStatus("mandatory")
_MscShelfCardDiagRecErrStorageType_Type = StorageType
_MscShelfCardDiagRecErrStorageType_Object = MibTableColumn
mscShelfCardDiagRecErrStorageType = _MscShelfCardDiagRecErrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 1, 1, 4),
    _MscShelfCardDiagRecErrStorageType_Type()
)
mscShelfCardDiagRecErrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrStorageType.setStatus("mandatory")
_MscShelfCardDiagRecErrIndex_Type = NonReplicated
_MscShelfCardDiagRecErrIndex_Object = MibTableColumn
mscShelfCardDiagRecErrIndex = _MscShelfCardDiagRecErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 1, 1, 10),
    _MscShelfCardDiagRecErrIndex_Type()
)
mscShelfCardDiagRecErrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrIndex.setStatus("mandatory")
_MscShelfCardDiagRecErrLine_ObjectIdentity = ObjectIdentity
mscShelfCardDiagRecErrLine = _MscShelfCardDiagRecErrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2)
)
_MscShelfCardDiagRecErrLineRowStatusTable_Object = MibTable
mscShelfCardDiagRecErrLineRowStatusTable = _MscShelfCardDiagRecErrLineRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrLineRowStatusTable.setStatus("mandatory")
_MscShelfCardDiagRecErrLineRowStatusEntry_Object = MibTableRow
mscShelfCardDiagRecErrLineRowStatusEntry = _MscShelfCardDiagRecErrLineRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2, 1, 1)
)
mscShelfCardDiagRecErrLineRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagRecErrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagRecErrLineIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrLineRowStatusEntry.setStatus("mandatory")
_MscShelfCardDiagRecErrLineRowStatus_Type = RowStatus
_MscShelfCardDiagRecErrLineRowStatus_Object = MibTableColumn
mscShelfCardDiagRecErrLineRowStatus = _MscShelfCardDiagRecErrLineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2, 1, 1, 1),
    _MscShelfCardDiagRecErrLineRowStatus_Type()
)
mscShelfCardDiagRecErrLineRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrLineRowStatus.setStatus("mandatory")
_MscShelfCardDiagRecErrLineComponentName_Type = DisplayString
_MscShelfCardDiagRecErrLineComponentName_Object = MibTableColumn
mscShelfCardDiagRecErrLineComponentName = _MscShelfCardDiagRecErrLineComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2, 1, 1, 2),
    _MscShelfCardDiagRecErrLineComponentName_Type()
)
mscShelfCardDiagRecErrLineComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrLineComponentName.setStatus("mandatory")
_MscShelfCardDiagRecErrLineStorageType_Type = StorageType
_MscShelfCardDiagRecErrLineStorageType_Object = MibTableColumn
mscShelfCardDiagRecErrLineStorageType = _MscShelfCardDiagRecErrLineStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2, 1, 1, 4),
    _MscShelfCardDiagRecErrLineStorageType_Type()
)
mscShelfCardDiagRecErrLineStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrLineStorageType.setStatus("mandatory")


class _MscShelfCardDiagRecErrLineIndex_Type(Integer32):
    """Custom type mscShelfCardDiagRecErrLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_MscShelfCardDiagRecErrLineIndex_Type.__name__ = "Integer32"
_MscShelfCardDiagRecErrLineIndex_Object = MibTableColumn
mscShelfCardDiagRecErrLineIndex = _MscShelfCardDiagRecErrLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2, 1, 1, 10),
    _MscShelfCardDiagRecErrLineIndex_Type()
)
mscShelfCardDiagRecErrLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrLineIndex.setStatus("mandatory")
_MscShelfCardDiagRecErrLineOperTable_Object = MibTable
mscShelfCardDiagRecErrLineOperTable = _MscShelfCardDiagRecErrLineOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrLineOperTable.setStatus("mandatory")
_MscShelfCardDiagRecErrLineOperEntry_Object = MibTableRow
mscShelfCardDiagRecErrLineOperEntry = _MscShelfCardDiagRecErrLineOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2, 10, 1)
)
mscShelfCardDiagRecErrLineOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagRecErrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDiagRecErrLineIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrLineOperEntry.setStatus("mandatory")


class _MscShelfCardDiagRecErrLineData_Type(ExtendedAsciiString):
    """Custom type mscShelfCardDiagRecErrLineData based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MscShelfCardDiagRecErrLineData_Type.__name__ = "ExtendedAsciiString"
_MscShelfCardDiagRecErrLineData_Object = MibTableColumn
mscShelfCardDiagRecErrLineData = _MscShelfCardDiagRecErrLineData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 4, 3, 2, 10, 1, 1),
    _MscShelfCardDiagRecErrLineData_Type()
)
mscShelfCardDiagRecErrLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDiagRecErrLineData.setStatus("mandatory")
_MscShelfCardProvTable_Object = MibTable
mscShelfCardProvTable = _MscShelfCardProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 10)
)
if mibBuilder.loadTexts:
    mscShelfCardProvTable.setStatus("mandatory")
_MscShelfCardProvEntry_Object = MibTableRow
mscShelfCardProvEntry = _MscShelfCardProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 10, 1)
)
mscShelfCardProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardProvEntry.setStatus("mandatory")


class _MscShelfCardCardType_Type(Integer32):
    """Custom type mscShelfCardCardType based on Integer32"""
    defaultValue = 9

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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              84,
              85,
              86,
              87,
              88)
        )
    )
    namedValues = NamedValues(
        *(("cFP1", 35),
          ("cFP2", 37),
          ("cP", 0),
          ("cPeD", 59),
          ("cPeE", 60),
          ("dEV1", 36),
          ("dEV2", 38),
          ("dS1", 3),
          ("dS1C", 13),
          ("dS1V", 4),
          ("dS3", 5),
          ("e1", 6),
          ("e1C", 14),
          ("e1V", 7),
          ("e3", 8),
          ("hSSI", 33),
          ("ilsForwarder", 42),
          ("j2MV", 22),
          ("n12mPcusp", 82),
          ("n12mVspAal", 53),
          ("n12pDS3Atm", 63),
          ("n12pE3Atm", 64),
          ("n1pDS1Mvp", 46),
          ("n1pDS1Mvpe", 67),
          ("n1pDS1V", 25),
          ("n1pDS3C", 41),
          ("n1pDS3cAal", 51),
          ("n1pE1Mvp", 45),
          ("n1pE1Mvpe", 66),
          ("n1pE1V", 26),
          ("n1pFddiMultiMode", 10),
          ("n1pFddiSingleMode", 24),
          ("n1pOC12SmLrAtm", 65),
          ("n1pOC48SmSrAtm", 75),
          ("n1pSTM1ChSmIr", 78),
          ("n1pSTM1ChSmIrAtm", 79),
          ("n1pTTC2mMvp", 47),
          ("n1pTTC2mMvpe", 68),
          ("n2pDS3cAal", 52),
          ("n2pEth100BaseT", 54),
          ("n2pJ6MAtm", 27),
          ("n2pOC3MmAtm2", 55),
          ("n2pOC3SmAtm2", 56),
          ("n32pDS1Msa", 69),
          ("n32pDS1MsaMt", 70),
          ("n32pDS1MsaMtp", 71),
          ("n32pDS1MsaSt", 72),
          ("n32pDS1MsaStp", 73),
          ("n32pE1Aal", 74),
          ("n32pE1Msa", 84),
          ("n32pE1MsaMt", 85),
          ("n32pE1MsaMtp", 86),
          ("n32pE1MsaSt", 87),
          ("n32pE1MsaStp", 88),
          ("n3pDS1Atm", 21),
          ("n3pDS3Atm", 16),
          ("n3pDS3Atm2", 57),
          ("n3pE1Atm", 20),
          ("n3pE3Atm", 15),
          ("n3pE3Atm2", 58),
          ("n3pOC3MmAtm", 17),
          ("n3pOC3SmAtm", 19),
          ("n4pDS1Aal1", 39),
          ("n4pDS3Ch", 76),
          ("n4pDS3ChAtm", 77),
          ("n4pE1Aal1", 40),
          ("n4pEthAui", 23),
          ("n4pOC12SmIrAtm", 80),
          ("n4pOC12SmLrAtm", 81),
          ("n4pOC3MmAtm", 62),
          ("n4pOC3SmIrAtm", 61),
          ("n4pTokenRing", 11),
          ("n6pEth10BaseT", 12),
          ("n8pDS1", 34),
          ("n8pDS1Atm", 43),
          ("n8pE1Atm", 44),
          ("none", 9),
          ("v11", 1),
          ("v35", 2))
    )


_MscShelfCardCardType_Type.__name__ = "Integer32"
_MscShelfCardCardType_Object = MibTableColumn
mscShelfCardCardType = _MscShelfCardCardType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 10, 1, 1),
    _MscShelfCardCardType_Type()
)
mscShelfCardCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardCardType.setStatus("mandatory")


class _MscShelfCardSparingConnection_Type(Integer32):
    """Custom type mscShelfCardSparingConnection based on Integer32"""
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
              6,
              16)
        )
    )
    namedValues = NamedValues(
        *(("mainA", 1),
          ("mainB", 2),
          ("mainC", 3),
          ("mainD", 4),
          ("mainE", 5),
          ("mainF", 6),
          ("notApplicable", 0),
          ("spare", 16))
    )


_MscShelfCardSparingConnection_Type.__name__ = "Integer32"
_MscShelfCardSparingConnection_Object = MibTableColumn
mscShelfCardSparingConnection = _MscShelfCardSparingConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 10, 1, 2),
    _MscShelfCardSparingConnection_Type()
)
mscShelfCardSparingConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardSparingConnection.setStatus("mandatory")


class _MscShelfCardCommentText_Type(AsciiString):
    """Custom type mscShelfCardCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MscShelfCardCommentText_Type.__name__ = "AsciiString"
_MscShelfCardCommentText_Object = MibTableColumn
mscShelfCardCommentText = _MscShelfCardCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 10, 1, 4),
    _MscShelfCardCommentText_Type()
)
mscShelfCardCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCardCommentText.setStatus("mandatory")
_MscShelfCardStateTable_Object = MibTable
mscShelfCardStateTable = _MscShelfCardStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11)
)
if mibBuilder.loadTexts:
    mscShelfCardStateTable.setStatus("mandatory")
_MscShelfCardStateEntry_Object = MibTableRow
mscShelfCardStateEntry = _MscShelfCardStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1)
)
mscShelfCardStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardStateEntry.setStatus("mandatory")


class _MscShelfCardAdminState_Type(Integer32):
    """Custom type mscShelfCardAdminState based on Integer32"""
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


_MscShelfCardAdminState_Type.__name__ = "Integer32"
_MscShelfCardAdminState_Object = MibTableColumn
mscShelfCardAdminState = _MscShelfCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1, 1),
    _MscShelfCardAdminState_Type()
)
mscShelfCardAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardAdminState.setStatus("mandatory")


class _MscShelfCardOperationalState_Type(Integer32):
    """Custom type mscShelfCardOperationalState based on Integer32"""
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


_MscShelfCardOperationalState_Type.__name__ = "Integer32"
_MscShelfCardOperationalState_Object = MibTableColumn
mscShelfCardOperationalState = _MscShelfCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1, 2),
    _MscShelfCardOperationalState_Type()
)
mscShelfCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardOperationalState.setStatus("mandatory")


class _MscShelfCardUsageState_Type(Integer32):
    """Custom type mscShelfCardUsageState based on Integer32"""
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


_MscShelfCardUsageState_Type.__name__ = "Integer32"
_MscShelfCardUsageState_Object = MibTableColumn
mscShelfCardUsageState = _MscShelfCardUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1, 3),
    _MscShelfCardUsageState_Type()
)
mscShelfCardUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardUsageState.setStatus("mandatory")


class _MscShelfCardAvailabilityStatus_Type(OctetString):
    """Custom type mscShelfCardAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfCardAvailabilityStatus_Type.__name__ = "OctetString"
_MscShelfCardAvailabilityStatus_Object = MibTableColumn
mscShelfCardAvailabilityStatus = _MscShelfCardAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1, 4),
    _MscShelfCardAvailabilityStatus_Type()
)
mscShelfCardAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardAvailabilityStatus.setStatus("mandatory")


class _MscShelfCardProceduralStatus_Type(OctetString):
    """Custom type mscShelfCardProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardProceduralStatus_Type.__name__ = "OctetString"
_MscShelfCardProceduralStatus_Object = MibTableColumn
mscShelfCardProceduralStatus = _MscShelfCardProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1, 5),
    _MscShelfCardProceduralStatus_Type()
)
mscShelfCardProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardProceduralStatus.setStatus("mandatory")


class _MscShelfCardControlStatus_Type(OctetString):
    """Custom type mscShelfCardControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardControlStatus_Type.__name__ = "OctetString"
_MscShelfCardControlStatus_Object = MibTableColumn
mscShelfCardControlStatus = _MscShelfCardControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1, 6),
    _MscShelfCardControlStatus_Type()
)
mscShelfCardControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardControlStatus.setStatus("mandatory")


class _MscShelfCardAlarmStatus_Type(OctetString):
    """Custom type mscShelfCardAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardAlarmStatus_Type.__name__ = "OctetString"
_MscShelfCardAlarmStatus_Object = MibTableColumn
mscShelfCardAlarmStatus = _MscShelfCardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1, 7),
    _MscShelfCardAlarmStatus_Type()
)
mscShelfCardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardAlarmStatus.setStatus("mandatory")


class _MscShelfCardStandbyStatus_Type(Integer32):
    """Custom type mscShelfCardStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_MscShelfCardStandbyStatus_Type.__name__ = "Integer32"
_MscShelfCardStandbyStatus_Object = MibTableColumn
mscShelfCardStandbyStatus = _MscShelfCardStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1, 8),
    _MscShelfCardStandbyStatus_Type()
)
mscShelfCardStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardStandbyStatus.setStatus("mandatory")


class _MscShelfCardUnknownStatus_Type(Integer32):
    """Custom type mscShelfCardUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MscShelfCardUnknownStatus_Type.__name__ = "Integer32"
_MscShelfCardUnknownStatus_Object = MibTableColumn
mscShelfCardUnknownStatus = _MscShelfCardUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 11, 1, 9),
    _MscShelfCardUnknownStatus_Type()
)
mscShelfCardUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardUnknownStatus.setStatus("mandatory")
_MscShelfCardOperTable_Object = MibTable
mscShelfCardOperTable = _MscShelfCardOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 12)
)
if mibBuilder.loadTexts:
    mscShelfCardOperTable.setStatus("mandatory")
_MscShelfCardOperEntry_Object = MibTableRow
mscShelfCardOperEntry = _MscShelfCardOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 12, 1)
)
mscShelfCardOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardOperEntry.setStatus("mandatory")
_MscShelfCardCurrentLP_Type = RowPointer
_MscShelfCardCurrentLP_Object = MibTableColumn
mscShelfCardCurrentLP = _MscShelfCardCurrentLP_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 12, 1, 1),
    _MscShelfCardCurrentLP_Type()
)
mscShelfCardCurrentLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardCurrentLP.setStatus("obsolete")


class _MscShelfCardFailureCause_Type(Integer32):
    """Custom type mscShelfCardFailureCause based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("backplaneConnectivityProblem", 6),
          ("cannotLoadSoftware", 3),
          ("failedSelfTests", 4),
          ("none", 0),
          ("notConfigured", 2),
          ("notResponding", 5),
          ("unsupportedPecCode", 7),
          ("wrongCardType", 1))
    )


_MscShelfCardFailureCause_Type.__name__ = "Integer32"
_MscShelfCardFailureCause_Object = MibTableColumn
mscShelfCardFailureCause = _MscShelfCardFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 12, 1, 2),
    _MscShelfCardFailureCause_Type()
)
mscShelfCardFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFailureCause.setStatus("mandatory")


class _MscShelfCardSelfTestFault_Type(Integer32):
    """Custom type mscShelfCardSelfTestFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_MscShelfCardSelfTestFault_Type.__name__ = "Integer32"
_MscShelfCardSelfTestFault_Object = MibTableColumn
mscShelfCardSelfTestFault = _MscShelfCardSelfTestFault_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 12, 1, 3),
    _MscShelfCardSelfTestFault_Type()
)
mscShelfCardSelfTestFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardSelfTestFault.setStatus("mandatory")


class _MscShelfCardSparingConnectionStatus_Type(Integer32):
    """Custom type mscShelfCardSparingConnectionStatus based on Integer32"""
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
        *(("inconsistentlyConnected", 6),
          ("incorrectlyConnected", 5),
          ("n1for1Ok", 1),
          ("n1forNOk", 2),
          ("notApplicable", 0),
          ("notConnected", 4),
          ("unconfirmed", 3))
    )


_MscShelfCardSparingConnectionStatus_Type.__name__ = "Integer32"
_MscShelfCardSparingConnectionStatus_Object = MibTableColumn
mscShelfCardSparingConnectionStatus = _MscShelfCardSparingConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 12, 1, 4),
    _MscShelfCardSparingConnectionStatus_Type()
)
mscShelfCardSparingConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardSparingConnectionStatus.setStatus("mandatory")


class _MscShelfCardHardwareAlarm_Type(Integer32):
    """Custom type mscShelfCardHardwareAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("batteryFeedFailure", 1),
          ("none", 0))
    )


_MscShelfCardHardwareAlarm_Type.__name__ = "Integer32"
_MscShelfCardHardwareAlarm_Object = MibTableColumn
mscShelfCardHardwareAlarm = _MscShelfCardHardwareAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 12, 1, 5),
    _MscShelfCardHardwareAlarm_Type()
)
mscShelfCardHardwareAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardHardwareAlarm.setStatus("mandatory")
_MscShelfCardPropTable_Object = MibTable
mscShelfCardPropTable = _MscShelfCardPropTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 13)
)
if mibBuilder.loadTexts:
    mscShelfCardPropTable.setStatus("mandatory")
_MscShelfCardPropEntry_Object = MibTableRow
mscShelfCardPropEntry = _MscShelfCardPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 13, 1)
)
mscShelfCardPropEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardPropEntry.setStatus("mandatory")


class _MscShelfCardInsertedCardType_Type(Integer32):
    """Custom type mscShelfCardInsertedCardType based on Integer32"""
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
              25,
              26,
              27,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              84,
              85,
              86,
              87,
              88)
        )
    )
    namedValues = NamedValues(
        *(("cFP1", 35),
          ("cFP2", 37),
          ("cP", 0),
          ("cPeD", 59),
          ("cPeE", 60),
          ("dEV1", 36),
          ("dEV2", 38),
          ("dS1", 3),
          ("dS1C", 13),
          ("dS1V", 4),
          ("dS3", 5),
          ("e1", 6),
          ("e1C", 14),
          ("e1V", 7),
          ("e3", 8),
          ("hSSI", 33),
          ("ilsForwarder", 42),
          ("j2MV", 22),
          ("n12mPcusp", 82),
          ("n12mVspAal", 53),
          ("n12pDS3Atm", 63),
          ("n12pE3Atm", 64),
          ("n1pDS1Mvp", 46),
          ("n1pDS1Mvpe", 67),
          ("n1pDS1V", 25),
          ("n1pDS3C", 41),
          ("n1pDS3cAal", 51),
          ("n1pE1Mvp", 45),
          ("n1pE1Mvpe", 66),
          ("n1pE1V", 26),
          ("n1pFddiMultiMode", 10),
          ("n1pFddiSingleMode", 24),
          ("n1pOC12SmLrAtm", 65),
          ("n1pOC3MmAtm", 18),
          ("n1pOC48SmSrAtm", 75),
          ("n1pSTM1ChSmIr", 78),
          ("n1pSTM1ChSmIrAtm", 79),
          ("n1pTTC2mMvp", 47),
          ("n1pTTC2mMvpe", 68),
          ("n2pDS3cAal", 52),
          ("n2pEth100BaseT", 54),
          ("n2pJ6MAtm", 27),
          ("n2pOC3MmAtm2", 55),
          ("n2pOC3SmAtm2", 56),
          ("n32pDS1Msa", 69),
          ("n32pDS1MsaMt", 70),
          ("n32pDS1MsaMtp", 71),
          ("n32pDS1MsaSt", 72),
          ("n32pDS1MsaStp", 73),
          ("n32pE1Aal", 74),
          ("n32pE1Msa", 84),
          ("n32pE1MsaMt", 85),
          ("n32pE1MsaMtp", 86),
          ("n32pE1MsaSt", 87),
          ("n32pE1MsaStp", 88),
          ("n3pDS1Atm", 21),
          ("n3pDS3Atm", 16),
          ("n3pDS3Atm2", 57),
          ("n3pE1Atm", 20),
          ("n3pE3Atm", 15),
          ("n3pE3Atm2", 58),
          ("n3pOC3MmAtm", 17),
          ("n3pOC3SmAtm", 19),
          ("n4pDS1Aal1", 39),
          ("n4pDS3Ch", 76),
          ("n4pDS3ChAtm", 77),
          ("n4pE1Aal1", 40),
          ("n4pEthAui", 23),
          ("n4pOC12SmIrAtm", 80),
          ("n4pOC12SmLrAtm", 81),
          ("n4pOC3MmAtm", 62),
          ("n4pOC3SmIrAtm", 61),
          ("n4pTokenRing", 11),
          ("n6pEth10BaseT", 12),
          ("n8pDS1", 34),
          ("n8pDS1Atm", 43),
          ("n8pE1Atm", 44),
          ("none", 9),
          ("v11", 1),
          ("v35", 2))
    )


_MscShelfCardInsertedCardType_Type.__name__ = "Integer32"
_MscShelfCardInsertedCardType_Object = MibTableColumn
mscShelfCardInsertedCardType = _MscShelfCardInsertedCardType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 13, 1, 1),
    _MscShelfCardInsertedCardType_Type()
)
mscShelfCardInsertedCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardInsertedCardType.setStatus("mandatory")


class _MscShelfCardPmRevisionCode_Type(AsciiString):
    """Custom type mscShelfCardPmRevisionCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscShelfCardPmRevisionCode_Type.__name__ = "AsciiString"
_MscShelfCardPmRevisionCode_Object = MibTableColumn
mscShelfCardPmRevisionCode = _MscShelfCardPmRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 13, 1, 2),
    _MscShelfCardPmRevisionCode_Type()
)
mscShelfCardPmRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardPmRevisionCode.setStatus("mandatory")


class _MscShelfCardImRevisionCode_Type(AsciiString):
    """Custom type mscShelfCardImRevisionCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscShelfCardImRevisionCode_Type.__name__ = "AsciiString"
_MscShelfCardImRevisionCode_Object = MibTableColumn
mscShelfCardImRevisionCode = _MscShelfCardImRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 13, 1, 3),
    _MscShelfCardImRevisionCode_Type()
)
mscShelfCardImRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardImRevisionCode.setStatus("mandatory")


class _MscShelfCardSerialNumber_Type(AsciiString):
    """Custom type mscShelfCardSerialNumber based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscShelfCardSerialNumber_Type.__name__ = "AsciiString"
_MscShelfCardSerialNumber_Object = MibTableColumn
mscShelfCardSerialNumber = _MscShelfCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 13, 1, 4),
    _MscShelfCardSerialNumber_Type()
)
mscShelfCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardSerialNumber.setStatus("mandatory")


class _MscShelfCardActiveFirmwareVersion_Type(AsciiString):
    """Custom type mscShelfCardActiveFirmwareVersion based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscShelfCardActiveFirmwareVersion_Type.__name__ = "AsciiString"
_MscShelfCardActiveFirmwareVersion_Object = MibTableColumn
mscShelfCardActiveFirmwareVersion = _MscShelfCardActiveFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 13, 1, 5),
    _MscShelfCardActiveFirmwareVersion_Type()
)
mscShelfCardActiveFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardActiveFirmwareVersion.setStatus("mandatory")


class _MscShelfCardInactiveFirmwareVersion_Type(AsciiString):
    """Custom type mscShelfCardInactiveFirmwareVersion based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscShelfCardInactiveFirmwareVersion_Type.__name__ = "AsciiString"
_MscShelfCardInactiveFirmwareVersion_Object = MibTableColumn
mscShelfCardInactiveFirmwareVersion = _MscShelfCardInactiveFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 13, 1, 6),
    _MscShelfCardInactiveFirmwareVersion_Type()
)
mscShelfCardInactiveFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardInactiveFirmwareVersion.setStatus("mandatory")


class _MscShelfCardProductCode_Type(AsciiString):
    """Custom type mscShelfCardProductCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_MscShelfCardProductCode_Type.__name__ = "AsciiString"
_MscShelfCardProductCode_Object = MibTableColumn
mscShelfCardProductCode = _MscShelfCardProductCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 13, 1, 7),
    _MscShelfCardProductCode_Type()
)
mscShelfCardProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardProductCode.setStatus("mandatory")
_MscShelfCardUtilTable_Object = MibTable
mscShelfCardUtilTable = _MscShelfCardUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14)
)
if mibBuilder.loadTexts:
    mscShelfCardUtilTable.setStatus("mandatory")
_MscShelfCardUtilEntry_Object = MibTableRow
mscShelfCardUtilEntry = _MscShelfCardUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1)
)
mscShelfCardUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardUtilEntry.setStatus("mandatory")


class _MscShelfCardTimeInterval_Type(Unsigned32):
    """Custom type mscShelfCardTimeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfCardTimeInterval_Type.__name__ = "Unsigned32"
_MscShelfCardTimeInterval_Object = MibTableColumn
mscShelfCardTimeInterval = _MscShelfCardTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 1),
    _MscShelfCardTimeInterval_Type()
)
mscShelfCardTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardTimeInterval.setStatus("mandatory")


class _MscShelfCardCpuUtil_Type(Gauge32):
    """Custom type mscShelfCardCpuUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscShelfCardCpuUtil_Type.__name__ = "Gauge32"
_MscShelfCardCpuUtil_Object = MibTableColumn
mscShelfCardCpuUtil = _MscShelfCardCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 2),
    _MscShelfCardCpuUtil_Type()
)
mscShelfCardCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardCpuUtil.setStatus("mandatory")


class _MscShelfCardCpuUtilAvg_Type(Gauge32):
    """Custom type mscShelfCardCpuUtilAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscShelfCardCpuUtilAvg_Type.__name__ = "Gauge32"
_MscShelfCardCpuUtilAvg_Object = MibTableColumn
mscShelfCardCpuUtilAvg = _MscShelfCardCpuUtilAvg_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 3),
    _MscShelfCardCpuUtilAvg_Type()
)
mscShelfCardCpuUtilAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardCpuUtilAvg.setStatus("mandatory")


class _MscShelfCardCpuUtilAvgMin_Type(Gauge32):
    """Custom type mscShelfCardCpuUtilAvgMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscShelfCardCpuUtilAvgMin_Type.__name__ = "Gauge32"
_MscShelfCardCpuUtilAvgMin_Object = MibTableColumn
mscShelfCardCpuUtilAvgMin = _MscShelfCardCpuUtilAvgMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 4),
    _MscShelfCardCpuUtilAvgMin_Type()
)
mscShelfCardCpuUtilAvgMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardCpuUtilAvgMin.setStatus("mandatory")


class _MscShelfCardCpuUtilAvgMax_Type(Gauge32):
    """Custom type mscShelfCardCpuUtilAvgMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscShelfCardCpuUtilAvgMax_Type.__name__ = "Gauge32"
_MscShelfCardCpuUtilAvgMax_Object = MibTableColumn
mscShelfCardCpuUtilAvgMax = _MscShelfCardCpuUtilAvgMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 5),
    _MscShelfCardCpuUtilAvgMax_Type()
)
mscShelfCardCpuUtilAvgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardCpuUtilAvgMax.setStatus("mandatory")


class _MscShelfCardMsgBlockUsage_Type(Gauge32):
    """Custom type mscShelfCardMsgBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMsgBlockUsage_Type.__name__ = "Gauge32"
_MscShelfCardMsgBlockUsage_Object = MibTableColumn
mscShelfCardMsgBlockUsage = _MscShelfCardMsgBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 6),
    _MscShelfCardMsgBlockUsage_Type()
)
mscShelfCardMsgBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMsgBlockUsage.setStatus("mandatory")


class _MscShelfCardMsgBlockUsageAvg_Type(Gauge32):
    """Custom type mscShelfCardMsgBlockUsageAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMsgBlockUsageAvg_Type.__name__ = "Gauge32"
_MscShelfCardMsgBlockUsageAvg_Object = MibTableColumn
mscShelfCardMsgBlockUsageAvg = _MscShelfCardMsgBlockUsageAvg_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 7),
    _MscShelfCardMsgBlockUsageAvg_Type()
)
mscShelfCardMsgBlockUsageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMsgBlockUsageAvg.setStatus("mandatory")


class _MscShelfCardMsgBlockUsageAvgMin_Type(Gauge32):
    """Custom type mscShelfCardMsgBlockUsageAvgMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMsgBlockUsageAvgMin_Type.__name__ = "Gauge32"
_MscShelfCardMsgBlockUsageAvgMin_Object = MibTableColumn
mscShelfCardMsgBlockUsageAvgMin = _MscShelfCardMsgBlockUsageAvgMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 8),
    _MscShelfCardMsgBlockUsageAvgMin_Type()
)
mscShelfCardMsgBlockUsageAvgMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMsgBlockUsageAvgMin.setStatus("mandatory")


class _MscShelfCardMsgBlockUsageAvgMax_Type(Gauge32):
    """Custom type mscShelfCardMsgBlockUsageAvgMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMsgBlockUsageAvgMax_Type.__name__ = "Gauge32"
_MscShelfCardMsgBlockUsageAvgMax_Object = MibTableColumn
mscShelfCardMsgBlockUsageAvgMax = _MscShelfCardMsgBlockUsageAvgMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 9),
    _MscShelfCardMsgBlockUsageAvgMax_Type()
)
mscShelfCardMsgBlockUsageAvgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMsgBlockUsageAvgMax.setStatus("mandatory")


class _MscShelfCardLocalMsgBlockUsage_Type(Gauge32):
    """Custom type mscShelfCardLocalMsgBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardLocalMsgBlockUsage_Type.__name__ = "Gauge32"
_MscShelfCardLocalMsgBlockUsage_Object = MibTableColumn
mscShelfCardLocalMsgBlockUsage = _MscShelfCardLocalMsgBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 10),
    _MscShelfCardLocalMsgBlockUsage_Type()
)
mscShelfCardLocalMsgBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardLocalMsgBlockUsage.setStatus("mandatory")


class _MscShelfCardLocalMsgBlockUsageAvg_Type(Gauge32):
    """Custom type mscShelfCardLocalMsgBlockUsageAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardLocalMsgBlockUsageAvg_Type.__name__ = "Gauge32"
_MscShelfCardLocalMsgBlockUsageAvg_Object = MibTableColumn
mscShelfCardLocalMsgBlockUsageAvg = _MscShelfCardLocalMsgBlockUsageAvg_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 11),
    _MscShelfCardLocalMsgBlockUsageAvg_Type()
)
mscShelfCardLocalMsgBlockUsageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardLocalMsgBlockUsageAvg.setStatus("mandatory")


class _MscShelfCardLocalMsgBlockUsageMin_Type(Gauge32):
    """Custom type mscShelfCardLocalMsgBlockUsageMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardLocalMsgBlockUsageMin_Type.__name__ = "Gauge32"
_MscShelfCardLocalMsgBlockUsageMin_Object = MibTableColumn
mscShelfCardLocalMsgBlockUsageMin = _MscShelfCardLocalMsgBlockUsageMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 12),
    _MscShelfCardLocalMsgBlockUsageMin_Type()
)
mscShelfCardLocalMsgBlockUsageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardLocalMsgBlockUsageMin.setStatus("mandatory")


class _MscShelfCardLocalMsgBlockUsageMax_Type(Gauge32):
    """Custom type mscShelfCardLocalMsgBlockUsageMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardLocalMsgBlockUsageMax_Type.__name__ = "Gauge32"
_MscShelfCardLocalMsgBlockUsageMax_Object = MibTableColumn
mscShelfCardLocalMsgBlockUsageMax = _MscShelfCardLocalMsgBlockUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 14, 1, 13),
    _MscShelfCardLocalMsgBlockUsageMax_Type()
)
mscShelfCardLocalMsgBlockUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardLocalMsgBlockUsageMax.setStatus("mandatory")
_MscShelfCardCapTable_Object = MibTable
mscShelfCardCapTable = _MscShelfCardCapTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 15)
)
if mibBuilder.loadTexts:
    mscShelfCardCapTable.setStatus("mandatory")
_MscShelfCardCapEntry_Object = MibTableRow
mscShelfCardCapEntry = _MscShelfCardCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 15, 1)
)
mscShelfCardCapEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardCapEntry.setStatus("mandatory")


class _MscShelfCardMsgBlockCapacity_Type(Unsigned32):
    """Custom type mscShelfCardMsgBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMsgBlockCapacity_Type.__name__ = "Unsigned32"
_MscShelfCardMsgBlockCapacity_Object = MibTableColumn
mscShelfCardMsgBlockCapacity = _MscShelfCardMsgBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 15, 1, 1),
    _MscShelfCardMsgBlockCapacity_Type()
)
mscShelfCardMsgBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMsgBlockCapacity.setStatus("mandatory")


class _MscShelfCardLocalMsgBlockCapacity_Type(Unsigned32):
    """Custom type mscShelfCardLocalMsgBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardLocalMsgBlockCapacity_Type.__name__ = "Unsigned32"
_MscShelfCardLocalMsgBlockCapacity_Object = MibTableColumn
mscShelfCardLocalMsgBlockCapacity = _MscShelfCardLocalMsgBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 15, 1, 2),
    _MscShelfCardLocalMsgBlockCapacity_Type()
)
mscShelfCardLocalMsgBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardLocalMsgBlockCapacity.setStatus("mandatory")
_MscShelfCardDcard_ObjectIdentity = ObjectIdentity
mscShelfCardDcard = _MscShelfCardDcard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16)
)
_MscShelfCardDcardRowStatusTable_Object = MibTable
mscShelfCardDcardRowStatusTable = _MscShelfCardDcardRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardDcardRowStatusTable.setStatus("mandatory")
_MscShelfCardDcardRowStatusEntry_Object = MibTableRow
mscShelfCardDcardRowStatusEntry = _MscShelfCardDcardRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 1, 1)
)
mscShelfCardDcardRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDcardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardDcardRowStatusEntry.setStatus("mandatory")
_MscShelfCardDcardRowStatus_Type = RowStatus
_MscShelfCardDcardRowStatus_Object = MibTableColumn
mscShelfCardDcardRowStatus = _MscShelfCardDcardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 1, 1, 1),
    _MscShelfCardDcardRowStatus_Type()
)
mscShelfCardDcardRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDcardRowStatus.setStatus("mandatory")
_MscShelfCardDcardComponentName_Type = DisplayString
_MscShelfCardDcardComponentName_Object = MibTableColumn
mscShelfCardDcardComponentName = _MscShelfCardDcardComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 1, 1, 2),
    _MscShelfCardDcardComponentName_Type()
)
mscShelfCardDcardComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDcardComponentName.setStatus("mandatory")
_MscShelfCardDcardStorageType_Type = StorageType
_MscShelfCardDcardStorageType_Object = MibTableColumn
mscShelfCardDcardStorageType = _MscShelfCardDcardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 1, 1, 4),
    _MscShelfCardDcardStorageType_Type()
)
mscShelfCardDcardStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDcardStorageType.setStatus("mandatory")


class _MscShelfCardDcardIndex_Type(Integer32):
    """Custom type mscShelfCardDcardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscShelfCardDcardIndex_Type.__name__ = "Integer32"
_MscShelfCardDcardIndex_Object = MibTableColumn
mscShelfCardDcardIndex = _MscShelfCardDcardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 1, 1, 10),
    _MscShelfCardDcardIndex_Type()
)
mscShelfCardDcardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardDcardIndex.setStatus("mandatory")
_MscShelfCardDcardDcardOperTable_Object = MibTable
mscShelfCardDcardDcardOperTable = _MscShelfCardDcardDcardOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 17)
)
if mibBuilder.loadTexts:
    mscShelfCardDcardDcardOperTable.setStatus("mandatory")
_MscShelfCardDcardDcardOperEntry_Object = MibTableRow
mscShelfCardDcardDcardOperEntry = _MscShelfCardDcardDcardOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 17, 1)
)
mscShelfCardDcardDcardOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardDcardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardDcardDcardOperEntry.setStatus("mandatory")


class _MscShelfCardDcardType_Type(Integer32):
    """Custom type mscShelfCardDcardType based on Integer32"""
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
        *(("aqm", 2),
          ("aqmpqc", 4),
          ("pqc", 3),
          ("processor", 5),
          ("ram", 1),
          ("unknown", 0))
    )


_MscShelfCardDcardType_Type.__name__ = "Integer32"
_MscShelfCardDcardType_Object = MibTableColumn
mscShelfCardDcardType = _MscShelfCardDcardType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 17, 1, 1),
    _MscShelfCardDcardType_Type()
)
mscShelfCardDcardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDcardType.setStatus("mandatory")


class _MscShelfCardDcardMemorySize_Type(Unsigned32):
    """Custom type mscShelfCardDcardMemorySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardDcardMemorySize_Type.__name__ = "Unsigned32"
_MscShelfCardDcardMemorySize_Object = MibTableColumn
mscShelfCardDcardMemorySize = _MscShelfCardDcardMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 17, 1, 2),
    _MscShelfCardDcardMemorySize_Type()
)
mscShelfCardDcardMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDcardMemorySize.setStatus("mandatory")


class _MscShelfCardDcardProductCode_Type(AsciiString):
    """Custom type mscShelfCardDcardProductCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_MscShelfCardDcardProductCode_Type.__name__ = "AsciiString"
_MscShelfCardDcardProductCode_Object = MibTableColumn
mscShelfCardDcardProductCode = _MscShelfCardDcardProductCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 16, 17, 1, 3),
    _MscShelfCardDcardProductCode_Type()
)
mscShelfCardDcardProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardDcardProductCode.setStatus("mandatory")
_MscShelfCardConfiguredLPsTable_Object = MibTable
mscShelfCardConfiguredLPsTable = _MscShelfCardConfiguredLPsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 243)
)
if mibBuilder.loadTexts:
    mscShelfCardConfiguredLPsTable.setStatus("mandatory")
_MscShelfCardConfiguredLPsEntry_Object = MibTableRow
mscShelfCardConfiguredLPsEntry = _MscShelfCardConfiguredLPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 243, 1)
)
mscShelfCardConfiguredLPsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardConfiguredLPsValue"),
)
if mibBuilder.loadTexts:
    mscShelfCardConfiguredLPsEntry.setStatus("mandatory")
_MscShelfCardConfiguredLPsValue_Type = Link
_MscShelfCardConfiguredLPsValue_Object = MibTableColumn
mscShelfCardConfiguredLPsValue = _MscShelfCardConfiguredLPsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 243, 1, 1),
    _MscShelfCardConfiguredLPsValue_Type()
)
mscShelfCardConfiguredLPsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardConfiguredLPsValue.setStatus("mandatory")
_MscShelfCardMemoryCapacityTable_Object = MibTable
mscShelfCardMemoryCapacityTable = _MscShelfCardMemoryCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 244)
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryCapacityTable.setStatus("mandatory")
_MscShelfCardMemoryCapacityEntry_Object = MibTableRow
mscShelfCardMemoryCapacityEntry = _MscShelfCardMemoryCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 244, 1)
)
mscShelfCardMemoryCapacityEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardMemoryCapacityIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryCapacityEntry.setStatus("mandatory")


class _MscShelfCardMemoryCapacityIndex_Type(Integer32):
    """Custom type mscShelfCardMemoryCapacityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_MscShelfCardMemoryCapacityIndex_Type.__name__ = "Integer32"
_MscShelfCardMemoryCapacityIndex_Object = MibTableColumn
mscShelfCardMemoryCapacityIndex = _MscShelfCardMemoryCapacityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 244, 1, 1),
    _MscShelfCardMemoryCapacityIndex_Type()
)
mscShelfCardMemoryCapacityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardMemoryCapacityIndex.setStatus("mandatory")


class _MscShelfCardMemoryCapacityValue_Type(Unsigned32):
    """Custom type mscShelfCardMemoryCapacityValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMemoryCapacityValue_Type.__name__ = "Unsigned32"
_MscShelfCardMemoryCapacityValue_Object = MibTableColumn
mscShelfCardMemoryCapacityValue = _MscShelfCardMemoryCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 244, 1, 2),
    _MscShelfCardMemoryCapacityValue_Type()
)
mscShelfCardMemoryCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMemoryCapacityValue.setStatus("mandatory")
_MscShelfCardMemoryUsageTable_Object = MibTable
mscShelfCardMemoryUsageTable = _MscShelfCardMemoryUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 245)
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageTable.setStatus("mandatory")
_MscShelfCardMemoryUsageEntry_Object = MibTableRow
mscShelfCardMemoryUsageEntry = _MscShelfCardMemoryUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 245, 1)
)
mscShelfCardMemoryUsageEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardMemoryUsageIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageEntry.setStatus("mandatory")


class _MscShelfCardMemoryUsageIndex_Type(Integer32):
    """Custom type mscShelfCardMemoryUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_MscShelfCardMemoryUsageIndex_Type.__name__ = "Integer32"
_MscShelfCardMemoryUsageIndex_Object = MibTableColumn
mscShelfCardMemoryUsageIndex = _MscShelfCardMemoryUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 245, 1, 1),
    _MscShelfCardMemoryUsageIndex_Type()
)
mscShelfCardMemoryUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageIndex.setStatus("mandatory")


class _MscShelfCardMemoryUsageValue_Type(Gauge32):
    """Custom type mscShelfCardMemoryUsageValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMemoryUsageValue_Type.__name__ = "Gauge32"
_MscShelfCardMemoryUsageValue_Object = MibTableColumn
mscShelfCardMemoryUsageValue = _MscShelfCardMemoryUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 245, 1, 2),
    _MscShelfCardMemoryUsageValue_Type()
)
mscShelfCardMemoryUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageValue.setStatus("mandatory")
_MscShelfCardMemoryUsageAvgTable_Object = MibTable
mscShelfCardMemoryUsageAvgTable = _MscShelfCardMemoryUsageAvgTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 276)
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgTable.setStatus("mandatory")
_MscShelfCardMemoryUsageAvgEntry_Object = MibTableRow
mscShelfCardMemoryUsageAvgEntry = _MscShelfCardMemoryUsageAvgEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 276, 1)
)
mscShelfCardMemoryUsageAvgEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardMemoryUsageAvgIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgEntry.setStatus("mandatory")


class _MscShelfCardMemoryUsageAvgIndex_Type(Integer32):
    """Custom type mscShelfCardMemoryUsageAvgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_MscShelfCardMemoryUsageAvgIndex_Type.__name__ = "Integer32"
_MscShelfCardMemoryUsageAvgIndex_Object = MibTableColumn
mscShelfCardMemoryUsageAvgIndex = _MscShelfCardMemoryUsageAvgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 276, 1, 1),
    _MscShelfCardMemoryUsageAvgIndex_Type()
)
mscShelfCardMemoryUsageAvgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgIndex.setStatus("mandatory")


class _MscShelfCardMemoryUsageAvgValue_Type(Gauge32):
    """Custom type mscShelfCardMemoryUsageAvgValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMemoryUsageAvgValue_Type.__name__ = "Gauge32"
_MscShelfCardMemoryUsageAvgValue_Object = MibTableColumn
mscShelfCardMemoryUsageAvgValue = _MscShelfCardMemoryUsageAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 276, 1, 2),
    _MscShelfCardMemoryUsageAvgValue_Type()
)
mscShelfCardMemoryUsageAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgValue.setStatus("mandatory")
_MscShelfCardMemoryUsageAvgMinTable_Object = MibTable
mscShelfCardMemoryUsageAvgMinTable = _MscShelfCardMemoryUsageAvgMinTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 277)
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgMinTable.setStatus("mandatory")
_MscShelfCardMemoryUsageAvgMinEntry_Object = MibTableRow
mscShelfCardMemoryUsageAvgMinEntry = _MscShelfCardMemoryUsageAvgMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 277, 1)
)
mscShelfCardMemoryUsageAvgMinEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardMemoryUsageAvgMinIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgMinEntry.setStatus("mandatory")


class _MscShelfCardMemoryUsageAvgMinIndex_Type(Integer32):
    """Custom type mscShelfCardMemoryUsageAvgMinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_MscShelfCardMemoryUsageAvgMinIndex_Type.__name__ = "Integer32"
_MscShelfCardMemoryUsageAvgMinIndex_Object = MibTableColumn
mscShelfCardMemoryUsageAvgMinIndex = _MscShelfCardMemoryUsageAvgMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 277, 1, 1),
    _MscShelfCardMemoryUsageAvgMinIndex_Type()
)
mscShelfCardMemoryUsageAvgMinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgMinIndex.setStatus("mandatory")


class _MscShelfCardMemoryUsageAvgMinValue_Type(Gauge32):
    """Custom type mscShelfCardMemoryUsageAvgMinValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMemoryUsageAvgMinValue_Type.__name__ = "Gauge32"
_MscShelfCardMemoryUsageAvgMinValue_Object = MibTableColumn
mscShelfCardMemoryUsageAvgMinValue = _MscShelfCardMemoryUsageAvgMinValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 277, 1, 2),
    _MscShelfCardMemoryUsageAvgMinValue_Type()
)
mscShelfCardMemoryUsageAvgMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgMinValue.setStatus("mandatory")
_MscShelfCardMemoryUsageAvgMaxTable_Object = MibTable
mscShelfCardMemoryUsageAvgMaxTable = _MscShelfCardMemoryUsageAvgMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 278)
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgMaxTable.setStatus("mandatory")
_MscShelfCardMemoryUsageAvgMaxEntry_Object = MibTableRow
mscShelfCardMemoryUsageAvgMaxEntry = _MscShelfCardMemoryUsageAvgMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 278, 1)
)
mscShelfCardMemoryUsageAvgMaxEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardMemoryUsageAvgMaxIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgMaxEntry.setStatus("mandatory")


class _MscShelfCardMemoryUsageAvgMaxIndex_Type(Integer32):
    """Custom type mscShelfCardMemoryUsageAvgMaxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_MscShelfCardMemoryUsageAvgMaxIndex_Type.__name__ = "Integer32"
_MscShelfCardMemoryUsageAvgMaxIndex_Object = MibTableColumn
mscShelfCardMemoryUsageAvgMaxIndex = _MscShelfCardMemoryUsageAvgMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 278, 1, 1),
    _MscShelfCardMemoryUsageAvgMaxIndex_Type()
)
mscShelfCardMemoryUsageAvgMaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgMaxIndex.setStatus("mandatory")


class _MscShelfCardMemoryUsageAvgMaxValue_Type(Gauge32):
    """Custom type mscShelfCardMemoryUsageAvgMaxValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscShelfCardMemoryUsageAvgMaxValue_Type.__name__ = "Gauge32"
_MscShelfCardMemoryUsageAvgMaxValue_Object = MibTableColumn
mscShelfCardMemoryUsageAvgMaxValue = _MscShelfCardMemoryUsageAvgMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 278, 1, 2),
    _MscShelfCardMemoryUsageAvgMaxValue_Type()
)
mscShelfCardMemoryUsageAvgMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardMemoryUsageAvgMaxValue.setStatus("mandatory")
_MscShelfCardCurrentLpTable_Object = MibTable
mscShelfCardCurrentLpTable = _MscShelfCardCurrentLpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 406)
)
if mibBuilder.loadTexts:
    mscShelfCardCurrentLpTable.setStatus("mandatory")
_MscShelfCardCurrentLpEntry_Object = MibTableRow
mscShelfCardCurrentLpEntry = _MscShelfCardCurrentLpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 406, 1)
)
mscShelfCardCurrentLpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardCurrentLpValue"),
)
if mibBuilder.loadTexts:
    mscShelfCardCurrentLpEntry.setStatus("mandatory")
_MscShelfCardCurrentLpValue_Type = RowPointer
_MscShelfCardCurrentLpValue_Object = MibTableColumn
mscShelfCardCurrentLpValue = _MscShelfCardCurrentLpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 406, 1, 1),
    _MscShelfCardCurrentLpValue_Type()
)
mscShelfCardCurrentLpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardCurrentLpValue.setStatus("mandatory")
_MscShelfProvTable_Object = MibTable
mscShelfProvTable = _MscShelfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 10)
)
if mibBuilder.loadTexts:
    mscShelfProvTable.setStatus("mandatory")
_MscShelfProvEntry_Object = MibTableRow
mscShelfProvEntry = _MscShelfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 10, 1)
)
mscShelfProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
)
if mibBuilder.loadTexts:
    mscShelfProvEntry.setStatus("mandatory")


class _MscShelfCommentText_Type(AsciiString):
    """Custom type mscShelfCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MscShelfCommentText_Type.__name__ = "AsciiString"
_MscShelfCommentText_Object = MibTableColumn
mscShelfCommentText = _MscShelfCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 10, 1, 1),
    _MscShelfCommentText_Type()
)
mscShelfCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfCommentText.setStatus("mandatory")
_MscShelfOperTable_Object = MibTable
mscShelfOperTable = _MscShelfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 11)
)
if mibBuilder.loadTexts:
    mscShelfOperTable.setStatus("mandatory")
_MscShelfOperEntry_Object = MibTableRow
mscShelfOperEntry = _MscShelfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 11, 1)
)
mscShelfOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
)
if mibBuilder.loadTexts:
    mscShelfOperEntry.setStatus("mandatory")


class _MscShelfBusOperatingMode_Type(Integer32):
    """Custom type mscShelfBusOperatingMode based on Integer32"""
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
        *(("dualBus", 3),
          ("noBus", 0),
          ("singleBusX", 1),
          ("singleBusY", 2))
    )


_MscShelfBusOperatingMode_Type.__name__ = "Integer32"
_MscShelfBusOperatingMode_Object = MibTableColumn
mscShelfBusOperatingMode = _MscShelfBusOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 11, 1, 1),
    _MscShelfBusOperatingMode_Type()
)
mscShelfBusOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusOperatingMode.setStatus("obsolete")


class _MscShelfHardwareFailures_Type(OctetString):
    """Custom type mscShelfHardwareFailures based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfHardwareFailures_Type.__name__ = "OctetString"
_MscShelfHardwareFailures_Object = MibTableColumn
mscShelfHardwareFailures = _MscShelfHardwareFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 11, 1, 2),
    _MscShelfHardwareFailures_Type()
)
mscShelfHardwareFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfHardwareFailures.setStatus("mandatory")


class _MscShelfNumberOfSlots_Type(Unsigned32):
    """Custom type mscShelfNumberOfSlots based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscShelfNumberOfSlots_Type.__name__ = "Unsigned32"
_MscShelfNumberOfSlots_Object = MibTableColumn
mscShelfNumberOfSlots = _MscShelfNumberOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 11, 1, 3),
    _MscShelfNumberOfSlots_Type()
)
mscShelfNumberOfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfNumberOfSlots.setStatus("mandatory")


class _MscShelfShelfType_Type(Integer32):
    """Custom type mscShelfShelfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("busBasedShelf", 0),
          ("fabricBasedShelf", 1))
    )


_MscShelfShelfType_Type.__name__ = "Integer32"
_MscShelfShelfType_Object = MibTableColumn
mscShelfShelfType = _MscShelfShelfType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 11, 1, 5),
    _MscShelfShelfType_Type()
)
mscShelfShelfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfShelfType.setStatus("mandatory")


class _MscShelfBackplaneOperatingMode_Type(Integer32):
    """Custom type mscShelfBackplaneOperatingMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dualBus", 3),
          ("dualFabric", 7),
          ("noBus", 0),
          ("noFabric", 4),
          ("singleBusX", 1),
          ("singleBusY", 2),
          ("singleFabricX", 5),
          ("singleFabricY", 6))
    )


_MscShelfBackplaneOperatingMode_Type.__name__ = "Integer32"
_MscShelfBackplaneOperatingMode_Object = MibTableColumn
mscShelfBackplaneOperatingMode = _MscShelfBackplaneOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 11, 1, 7),
    _MscShelfBackplaneOperatingMode_Type()
)
mscShelfBackplaneOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBackplaneOperatingMode.setStatus("mandatory")
_MscMod_ObjectIdentity = ObjectIdentity
mscMod = _MscMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16)
)
_MscModRowStatusTable_Object = MibTable
mscModRowStatusTable = _MscModRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 1)
)
if mibBuilder.loadTexts:
    mscModRowStatusTable.setStatus("mandatory")
_MscModRowStatusEntry_Object = MibTableRow
mscModRowStatusEntry = _MscModRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 1, 1)
)
mscModRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
)
if mibBuilder.loadTexts:
    mscModRowStatusEntry.setStatus("mandatory")
_MscModRowStatus_Type = RowStatus
_MscModRowStatus_Object = MibTableColumn
mscModRowStatus = _MscModRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 1, 1, 1),
    _MscModRowStatus_Type()
)
mscModRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModRowStatus.setStatus("mandatory")
_MscModComponentName_Type = DisplayString
_MscModComponentName_Object = MibTableColumn
mscModComponentName = _MscModComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 1, 1, 2),
    _MscModComponentName_Type()
)
mscModComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModComponentName.setStatus("mandatory")
_MscModStorageType_Type = StorageType
_MscModStorageType_Object = MibTableColumn
mscModStorageType = _MscModStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 1, 1, 4),
    _MscModStorageType_Type()
)
mscModStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscModStorageType.setStatus("mandatory")
_MscModIndex_Type = NonReplicated
_MscModIndex_Object = MibTableColumn
mscModIndex = _MscModIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 1, 1, 10),
    _MscModIndex_Type()
)
mscModIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModIndex.setStatus("mandatory")
_MscModProvTable_Object = MibTable
mscModProvTable = _MscModProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 10)
)
if mibBuilder.loadTexts:
    mscModProvTable.setStatus("mandatory")
_MscModProvEntry_Object = MibTableRow
mscModProvEntry = _MscModProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 10, 1)
)
mscModProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
)
if mibBuilder.loadTexts:
    mscModProvEntry.setStatus("mandatory")


class _MscModNodeId_Type(Unsigned32):
    """Custom type mscModNodeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_MscModNodeId_Type.__name__ = "Unsigned32"
_MscModNodeId_Object = MibTableColumn
mscModNodeId = _MscModNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 10, 1, 1),
    _MscModNodeId_Type()
)
mscModNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModNodeId.setStatus("mandatory")


class _MscModNodeName_Type(AsciiString):
    """Custom type mscModNodeName based on AsciiString"""
    defaultHexValue = "4e4f4e414d45"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscModNodeName_Type.__name__ = "AsciiString"
_MscModNodeName_Object = MibTableColumn
mscModNodeName = _MscModNodeName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 10, 1, 2),
    _MscModNodeName_Type()
)
mscModNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModNodeName.setStatus("mandatory")


class _MscModNamsId_Type(Unsigned32):
    """Custom type mscModNamsId based on Unsigned32"""
    defaultValue = 49151

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 49151),
    )


_MscModNamsId_Type.__name__ = "Unsigned32"
_MscModNamsId_Object = MibTableColumn
mscModNamsId = _MscModNamsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 10, 1, 3),
    _MscModNamsId_Type()
)
mscModNamsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModNamsId.setStatus("mandatory")


class _MscModRegionId_Type(Unsigned32):
    """Custom type mscModRegionId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_MscModRegionId_Type.__name__ = "Unsigned32"
_MscModRegionId_Object = MibTableColumn
mscModRegionId = _MscModRegionId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 10, 1, 4),
    _MscModRegionId_Type()
)
mscModRegionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModRegionId.setStatus("mandatory")


class _MscModNodePrefix_Type(AsciiString):
    """Custom type mscModNodePrefix based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_MscModNodePrefix_Type.__name__ = "AsciiString"
_MscModNodePrefix_Object = MibTableColumn
mscModNodePrefix = _MscModNodePrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 10, 1, 5),
    _MscModNodePrefix_Type()
)
mscModNodePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModNodePrefix.setStatus("mandatory")
_MscModNodePrefixesTable_Object = MibTable
mscModNodePrefixesTable = _MscModNodePrefixesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 338)
)
if mibBuilder.loadTexts:
    mscModNodePrefixesTable.setStatus("obsolete")
_MscModNodePrefixesEntry_Object = MibTableRow
mscModNodePrefixesEntry = _MscModNodePrefixesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 338, 1)
)
mscModNodePrefixesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModNodePrefixesIndex"),
)
if mibBuilder.loadTexts:
    mscModNodePrefixesEntry.setStatus("obsolete")


class _MscModNodePrefixesIndex_Type(Integer32):
    """Custom type mscModNodePrefixesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscModNodePrefixesIndex_Type.__name__ = "Integer32"
_MscModNodePrefixesIndex_Object = MibTableColumn
mscModNodePrefixesIndex = _MscModNodePrefixesIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 338, 1, 1),
    _MscModNodePrefixesIndex_Type()
)
mscModNodePrefixesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModNodePrefixesIndex.setStatus("obsolete")


class _MscModNodePrefixesValue_Type(AsciiString):
    """Custom type mscModNodePrefixesValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscModNodePrefixesValue_Type.__name__ = "AsciiString"
_MscModNodePrefixesValue_Object = MibTableColumn
mscModNodePrefixesValue = _MscModNodePrefixesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 338, 1, 2),
    _MscModNodePrefixesValue_Type()
)
mscModNodePrefixesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModNodePrefixesValue.setStatus("obsolete")
_MscModAlternatePorsPrefixesTable_Object = MibTable
mscModAlternatePorsPrefixesTable = _MscModAlternatePorsPrefixesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 405)
)
if mibBuilder.loadTexts:
    mscModAlternatePorsPrefixesTable.setStatus("mandatory")
_MscModAlternatePorsPrefixesEntry_Object = MibTableRow
mscModAlternatePorsPrefixesEntry = _MscModAlternatePorsPrefixesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 405, 1)
)
mscModAlternatePorsPrefixesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscModAlternatePorsPrefixesIndex"),
)
if mibBuilder.loadTexts:
    mscModAlternatePorsPrefixesEntry.setStatus("mandatory")


class _MscModAlternatePorsPrefixesIndex_Type(Integer32):
    """Custom type mscModAlternatePorsPrefixesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscModAlternatePorsPrefixesIndex_Type.__name__ = "Integer32"
_MscModAlternatePorsPrefixesIndex_Object = MibTableColumn
mscModAlternatePorsPrefixesIndex = _MscModAlternatePorsPrefixesIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 405, 1, 1),
    _MscModAlternatePorsPrefixesIndex_Type()
)
mscModAlternatePorsPrefixesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscModAlternatePorsPrefixesIndex.setStatus("mandatory")


class _MscModAlternatePorsPrefixesValue_Type(AsciiString):
    """Custom type mscModAlternatePorsPrefixesValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscModAlternatePorsPrefixesValue_Type.__name__ = "AsciiString"
_MscModAlternatePorsPrefixesValue_Object = MibTableColumn
mscModAlternatePorsPrefixesValue = _MscModAlternatePorsPrefixesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 16, 405, 1, 2),
    _MscModAlternatePorsPrefixesValue_Type()
)
mscModAlternatePorsPrefixesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscModAlternatePorsPrefixesValue.setStatus("mandatory")
_BaseShelfMIB_ObjectIdentity = ObjectIdentity
baseShelfMIB = _BaseShelfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 146)
)
_BaseShelfGroup_ObjectIdentity = ObjectIdentity
baseShelfGroup = _BaseShelfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 146, 1)
)
_BaseShelfGroupCA_ObjectIdentity = ObjectIdentity
baseShelfGroupCA = _BaseShelfGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 146, 1, 1)
)
_BaseShelfGroupCA02_ObjectIdentity = ObjectIdentity
baseShelfGroupCA02 = _BaseShelfGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 146, 1, 1, 3)
)
_BaseShelfGroupCA02A_ObjectIdentity = ObjectIdentity
baseShelfGroupCA02A = _BaseShelfGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 146, 1, 1, 3, 2)
)
_BaseShelfCapabilities_ObjectIdentity = ObjectIdentity
baseShelfCapabilities = _BaseShelfCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 146, 3)
)
_BaseShelfCapabilitiesCA_ObjectIdentity = ObjectIdentity
baseShelfCapabilitiesCA = _BaseShelfCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 146, 3, 1)
)
_BaseShelfCapabilitiesCA02_ObjectIdentity = ObjectIdentity
baseShelfCapabilitiesCA02 = _BaseShelfCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 146, 3, 1, 3)
)
_BaseShelfCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
baseShelfCapabilitiesCA02A = _BaseShelfCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 146, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-BaseShelfMIB",
    **{"mscShelf": mscShelf,
       "mscShelfRowStatusTable": mscShelfRowStatusTable,
       "mscShelfRowStatusEntry": mscShelfRowStatusEntry,
       "mscShelfRowStatus": mscShelfRowStatus,
       "mscShelfComponentName": mscShelfComponentName,
       "mscShelfStorageType": mscShelfStorageType,
       "mscShelfIndex": mscShelfIndex,
       "mscShelfCard": mscShelfCard,
       "mscShelfCardRowStatusTable": mscShelfCardRowStatusTable,
       "mscShelfCardRowStatusEntry": mscShelfCardRowStatusEntry,
       "mscShelfCardRowStatus": mscShelfCardRowStatus,
       "mscShelfCardComponentName": mscShelfCardComponentName,
       "mscShelfCardStorageType": mscShelfCardStorageType,
       "mscShelfCardIndex": mscShelfCardIndex,
       "mscShelfCardTest": mscShelfCardTest,
       "mscShelfCardTestRowStatusTable": mscShelfCardTestRowStatusTable,
       "mscShelfCardTestRowStatusEntry": mscShelfCardTestRowStatusEntry,
       "mscShelfCardTestRowStatus": mscShelfCardTestRowStatus,
       "mscShelfCardTestComponentName": mscShelfCardTestComponentName,
       "mscShelfCardTestStorageType": mscShelfCardTestStorageType,
       "mscShelfCardTestIndex": mscShelfCardTestIndex,
       "mscShelfCardTestStateTable": mscShelfCardTestStateTable,
       "mscShelfCardTestStateEntry": mscShelfCardTestStateEntry,
       "mscShelfCardTestAdminState": mscShelfCardTestAdminState,
       "mscShelfCardTestOperationalState": mscShelfCardTestOperationalState,
       "mscShelfCardTestUsageState": mscShelfCardTestUsageState,
       "mscShelfCardTestSetupTable": mscShelfCardTestSetupTable,
       "mscShelfCardTestSetupEntry": mscShelfCardTestSetupEntry,
       "mscShelfCardTestTargetCard": mscShelfCardTestTargetCard,
       "mscShelfCardTestFrmTypes": mscShelfCardTestFrmTypes,
       "mscShelfCardTestFrmPriorities": mscShelfCardTestFrmPriorities,
       "mscShelfCardTestFrmPatternType": mscShelfCardTestFrmPatternType,
       "mscShelfCardTestCustomizedPattern": mscShelfCardTestCustomizedPattern,
       "mscShelfCardTestDuration": mscShelfCardTestDuration,
       "mscShelfCardTestResultsTable": mscShelfCardTestResultsTable,
       "mscShelfCardTestResultsEntry": mscShelfCardTestResultsEntry,
       "mscShelfCardTestElapsedTime": mscShelfCardTestElapsedTime,
       "mscShelfCardTestTimeRemaining": mscShelfCardTestTimeRemaining,
       "mscShelfCardTestCauseOfTermination": mscShelfCardTestCauseOfTermination,
       "mscShelfCardTestSizeTable": mscShelfCardTestSizeTable,
       "mscShelfCardTestSizeEntry": mscShelfCardTestSizeEntry,
       "mscShelfCardTestSizeIndex": mscShelfCardTestSizeIndex,
       "mscShelfCardTestSizeValue": mscShelfCardTestSizeValue,
       "mscShelfCardTestLoadingFrmDataTable": mscShelfCardTestLoadingFrmDataTable,
       "mscShelfCardTestLoadingFrmDataEntry": mscShelfCardTestLoadingFrmDataEntry,
       "mscShelfCardTestLoadingFrmDataResultsIndex": mscShelfCardTestLoadingFrmDataResultsIndex,
       "mscShelfCardTestLoadingFrmDataPriorityIndex": mscShelfCardTestLoadingFrmDataPriorityIndex,
       "mscShelfCardTestLoadingFrmDataValue": mscShelfCardTestLoadingFrmDataValue,
       "mscShelfCardTestVerificationFrmDataTable": mscShelfCardTestVerificationFrmDataTable,
       "mscShelfCardTestVerificationFrmDataEntry": mscShelfCardTestVerificationFrmDataEntry,
       "mscShelfCardTestVerificationFrmDataResultsIndex": mscShelfCardTestVerificationFrmDataResultsIndex,
       "mscShelfCardTestVerificationFrmDataPriorityIndex": mscShelfCardTestVerificationFrmDataPriorityIndex,
       "mscShelfCardTestVerificationFrmDataValue": mscShelfCardTestVerificationFrmDataValue,
       "mscShelfCardDiag": mscShelfCardDiag,
       "mscShelfCardDiagRowStatusTable": mscShelfCardDiagRowStatusTable,
       "mscShelfCardDiagRowStatusEntry": mscShelfCardDiagRowStatusEntry,
       "mscShelfCardDiagRowStatus": mscShelfCardDiagRowStatus,
       "mscShelfCardDiagComponentName": mscShelfCardDiagComponentName,
       "mscShelfCardDiagStorageType": mscShelfCardDiagStorageType,
       "mscShelfCardDiagIndex": mscShelfCardDiagIndex,
       "mscShelfCardDiagTrapData": mscShelfCardDiagTrapData,
       "mscShelfCardDiagTrapDataRowStatusTable": mscShelfCardDiagTrapDataRowStatusTable,
       "mscShelfCardDiagTrapDataRowStatusEntry": mscShelfCardDiagTrapDataRowStatusEntry,
       "mscShelfCardDiagTrapDataRowStatus": mscShelfCardDiagTrapDataRowStatus,
       "mscShelfCardDiagTrapDataComponentName": mscShelfCardDiagTrapDataComponentName,
       "mscShelfCardDiagTrapDataStorageType": mscShelfCardDiagTrapDataStorageType,
       "mscShelfCardDiagTrapDataIndex": mscShelfCardDiagTrapDataIndex,
       "mscShelfCardDiagTrapDataLine": mscShelfCardDiagTrapDataLine,
       "mscShelfCardDiagTrapDataLineRowStatusTable": mscShelfCardDiagTrapDataLineRowStatusTable,
       "mscShelfCardDiagTrapDataLineRowStatusEntry": mscShelfCardDiagTrapDataLineRowStatusEntry,
       "mscShelfCardDiagTrapDataLineRowStatus": mscShelfCardDiagTrapDataLineRowStatus,
       "mscShelfCardDiagTrapDataLineComponentName": mscShelfCardDiagTrapDataLineComponentName,
       "mscShelfCardDiagTrapDataLineStorageType": mscShelfCardDiagTrapDataLineStorageType,
       "mscShelfCardDiagTrapDataLineIndex": mscShelfCardDiagTrapDataLineIndex,
       "mscShelfCardDiagTrapDataLineOperTable": mscShelfCardDiagTrapDataLineOperTable,
       "mscShelfCardDiagTrapDataLineOperEntry": mscShelfCardDiagTrapDataLineOperEntry,
       "mscShelfCardDiagTrapDataLineData": mscShelfCardDiagTrapDataLineData,
       "mscShelfCardDiagRecErr": mscShelfCardDiagRecErr,
       "mscShelfCardDiagRecErrRowStatusTable": mscShelfCardDiagRecErrRowStatusTable,
       "mscShelfCardDiagRecErrRowStatusEntry": mscShelfCardDiagRecErrRowStatusEntry,
       "mscShelfCardDiagRecErrRowStatus": mscShelfCardDiagRecErrRowStatus,
       "mscShelfCardDiagRecErrComponentName": mscShelfCardDiagRecErrComponentName,
       "mscShelfCardDiagRecErrStorageType": mscShelfCardDiagRecErrStorageType,
       "mscShelfCardDiagRecErrIndex": mscShelfCardDiagRecErrIndex,
       "mscShelfCardDiagRecErrLine": mscShelfCardDiagRecErrLine,
       "mscShelfCardDiagRecErrLineRowStatusTable": mscShelfCardDiagRecErrLineRowStatusTable,
       "mscShelfCardDiagRecErrLineRowStatusEntry": mscShelfCardDiagRecErrLineRowStatusEntry,
       "mscShelfCardDiagRecErrLineRowStatus": mscShelfCardDiagRecErrLineRowStatus,
       "mscShelfCardDiagRecErrLineComponentName": mscShelfCardDiagRecErrLineComponentName,
       "mscShelfCardDiagRecErrLineStorageType": mscShelfCardDiagRecErrLineStorageType,
       "mscShelfCardDiagRecErrLineIndex": mscShelfCardDiagRecErrLineIndex,
       "mscShelfCardDiagRecErrLineOperTable": mscShelfCardDiagRecErrLineOperTable,
       "mscShelfCardDiagRecErrLineOperEntry": mscShelfCardDiagRecErrLineOperEntry,
       "mscShelfCardDiagRecErrLineData": mscShelfCardDiagRecErrLineData,
       "mscShelfCardProvTable": mscShelfCardProvTable,
       "mscShelfCardProvEntry": mscShelfCardProvEntry,
       "mscShelfCardCardType": mscShelfCardCardType,
       "mscShelfCardSparingConnection": mscShelfCardSparingConnection,
       "mscShelfCardCommentText": mscShelfCardCommentText,
       "mscShelfCardStateTable": mscShelfCardStateTable,
       "mscShelfCardStateEntry": mscShelfCardStateEntry,
       "mscShelfCardAdminState": mscShelfCardAdminState,
       "mscShelfCardOperationalState": mscShelfCardOperationalState,
       "mscShelfCardUsageState": mscShelfCardUsageState,
       "mscShelfCardAvailabilityStatus": mscShelfCardAvailabilityStatus,
       "mscShelfCardProceduralStatus": mscShelfCardProceduralStatus,
       "mscShelfCardControlStatus": mscShelfCardControlStatus,
       "mscShelfCardAlarmStatus": mscShelfCardAlarmStatus,
       "mscShelfCardStandbyStatus": mscShelfCardStandbyStatus,
       "mscShelfCardUnknownStatus": mscShelfCardUnknownStatus,
       "mscShelfCardOperTable": mscShelfCardOperTable,
       "mscShelfCardOperEntry": mscShelfCardOperEntry,
       "mscShelfCardCurrentLP": mscShelfCardCurrentLP,
       "mscShelfCardFailureCause": mscShelfCardFailureCause,
       "mscShelfCardSelfTestFault": mscShelfCardSelfTestFault,
       "mscShelfCardSparingConnectionStatus": mscShelfCardSparingConnectionStatus,
       "mscShelfCardHardwareAlarm": mscShelfCardHardwareAlarm,
       "mscShelfCardPropTable": mscShelfCardPropTable,
       "mscShelfCardPropEntry": mscShelfCardPropEntry,
       "mscShelfCardInsertedCardType": mscShelfCardInsertedCardType,
       "mscShelfCardPmRevisionCode": mscShelfCardPmRevisionCode,
       "mscShelfCardImRevisionCode": mscShelfCardImRevisionCode,
       "mscShelfCardSerialNumber": mscShelfCardSerialNumber,
       "mscShelfCardActiveFirmwareVersion": mscShelfCardActiveFirmwareVersion,
       "mscShelfCardInactiveFirmwareVersion": mscShelfCardInactiveFirmwareVersion,
       "mscShelfCardProductCode": mscShelfCardProductCode,
       "mscShelfCardUtilTable": mscShelfCardUtilTable,
       "mscShelfCardUtilEntry": mscShelfCardUtilEntry,
       "mscShelfCardTimeInterval": mscShelfCardTimeInterval,
       "mscShelfCardCpuUtil": mscShelfCardCpuUtil,
       "mscShelfCardCpuUtilAvg": mscShelfCardCpuUtilAvg,
       "mscShelfCardCpuUtilAvgMin": mscShelfCardCpuUtilAvgMin,
       "mscShelfCardCpuUtilAvgMax": mscShelfCardCpuUtilAvgMax,
       "mscShelfCardMsgBlockUsage": mscShelfCardMsgBlockUsage,
       "mscShelfCardMsgBlockUsageAvg": mscShelfCardMsgBlockUsageAvg,
       "mscShelfCardMsgBlockUsageAvgMin": mscShelfCardMsgBlockUsageAvgMin,
       "mscShelfCardMsgBlockUsageAvgMax": mscShelfCardMsgBlockUsageAvgMax,
       "mscShelfCardLocalMsgBlockUsage": mscShelfCardLocalMsgBlockUsage,
       "mscShelfCardLocalMsgBlockUsageAvg": mscShelfCardLocalMsgBlockUsageAvg,
       "mscShelfCardLocalMsgBlockUsageMin": mscShelfCardLocalMsgBlockUsageMin,
       "mscShelfCardLocalMsgBlockUsageMax": mscShelfCardLocalMsgBlockUsageMax,
       "mscShelfCardCapTable": mscShelfCardCapTable,
       "mscShelfCardCapEntry": mscShelfCardCapEntry,
       "mscShelfCardMsgBlockCapacity": mscShelfCardMsgBlockCapacity,
       "mscShelfCardLocalMsgBlockCapacity": mscShelfCardLocalMsgBlockCapacity,
       "mscShelfCardDcard": mscShelfCardDcard,
       "mscShelfCardDcardRowStatusTable": mscShelfCardDcardRowStatusTable,
       "mscShelfCardDcardRowStatusEntry": mscShelfCardDcardRowStatusEntry,
       "mscShelfCardDcardRowStatus": mscShelfCardDcardRowStatus,
       "mscShelfCardDcardComponentName": mscShelfCardDcardComponentName,
       "mscShelfCardDcardStorageType": mscShelfCardDcardStorageType,
       "mscShelfCardDcardIndex": mscShelfCardDcardIndex,
       "mscShelfCardDcardDcardOperTable": mscShelfCardDcardDcardOperTable,
       "mscShelfCardDcardDcardOperEntry": mscShelfCardDcardDcardOperEntry,
       "mscShelfCardDcardType": mscShelfCardDcardType,
       "mscShelfCardDcardMemorySize": mscShelfCardDcardMemorySize,
       "mscShelfCardDcardProductCode": mscShelfCardDcardProductCode,
       "mscShelfCardConfiguredLPsTable": mscShelfCardConfiguredLPsTable,
       "mscShelfCardConfiguredLPsEntry": mscShelfCardConfiguredLPsEntry,
       "mscShelfCardConfiguredLPsValue": mscShelfCardConfiguredLPsValue,
       "mscShelfCardMemoryCapacityTable": mscShelfCardMemoryCapacityTable,
       "mscShelfCardMemoryCapacityEntry": mscShelfCardMemoryCapacityEntry,
       "mscShelfCardMemoryCapacityIndex": mscShelfCardMemoryCapacityIndex,
       "mscShelfCardMemoryCapacityValue": mscShelfCardMemoryCapacityValue,
       "mscShelfCardMemoryUsageTable": mscShelfCardMemoryUsageTable,
       "mscShelfCardMemoryUsageEntry": mscShelfCardMemoryUsageEntry,
       "mscShelfCardMemoryUsageIndex": mscShelfCardMemoryUsageIndex,
       "mscShelfCardMemoryUsageValue": mscShelfCardMemoryUsageValue,
       "mscShelfCardMemoryUsageAvgTable": mscShelfCardMemoryUsageAvgTable,
       "mscShelfCardMemoryUsageAvgEntry": mscShelfCardMemoryUsageAvgEntry,
       "mscShelfCardMemoryUsageAvgIndex": mscShelfCardMemoryUsageAvgIndex,
       "mscShelfCardMemoryUsageAvgValue": mscShelfCardMemoryUsageAvgValue,
       "mscShelfCardMemoryUsageAvgMinTable": mscShelfCardMemoryUsageAvgMinTable,
       "mscShelfCardMemoryUsageAvgMinEntry": mscShelfCardMemoryUsageAvgMinEntry,
       "mscShelfCardMemoryUsageAvgMinIndex": mscShelfCardMemoryUsageAvgMinIndex,
       "mscShelfCardMemoryUsageAvgMinValue": mscShelfCardMemoryUsageAvgMinValue,
       "mscShelfCardMemoryUsageAvgMaxTable": mscShelfCardMemoryUsageAvgMaxTable,
       "mscShelfCardMemoryUsageAvgMaxEntry": mscShelfCardMemoryUsageAvgMaxEntry,
       "mscShelfCardMemoryUsageAvgMaxIndex": mscShelfCardMemoryUsageAvgMaxIndex,
       "mscShelfCardMemoryUsageAvgMaxValue": mscShelfCardMemoryUsageAvgMaxValue,
       "mscShelfCardCurrentLpTable": mscShelfCardCurrentLpTable,
       "mscShelfCardCurrentLpEntry": mscShelfCardCurrentLpEntry,
       "mscShelfCardCurrentLpValue": mscShelfCardCurrentLpValue,
       "mscShelfProvTable": mscShelfProvTable,
       "mscShelfProvEntry": mscShelfProvEntry,
       "mscShelfCommentText": mscShelfCommentText,
       "mscShelfOperTable": mscShelfOperTable,
       "mscShelfOperEntry": mscShelfOperEntry,
       "mscShelfBusOperatingMode": mscShelfBusOperatingMode,
       "mscShelfHardwareFailures": mscShelfHardwareFailures,
       "mscShelfNumberOfSlots": mscShelfNumberOfSlots,
       "mscShelfShelfType": mscShelfShelfType,
       "mscShelfBackplaneOperatingMode": mscShelfBackplaneOperatingMode,
       "mscMod": mscMod,
       "mscModRowStatusTable": mscModRowStatusTable,
       "mscModRowStatusEntry": mscModRowStatusEntry,
       "mscModRowStatus": mscModRowStatus,
       "mscModComponentName": mscModComponentName,
       "mscModStorageType": mscModStorageType,
       "mscModIndex": mscModIndex,
       "mscModProvTable": mscModProvTable,
       "mscModProvEntry": mscModProvEntry,
       "mscModNodeId": mscModNodeId,
       "mscModNodeName": mscModNodeName,
       "mscModNamsId": mscModNamsId,
       "mscModRegionId": mscModRegionId,
       "mscModNodePrefix": mscModNodePrefix,
       "mscModNodePrefixesTable": mscModNodePrefixesTable,
       "mscModNodePrefixesEntry": mscModNodePrefixesEntry,
       "mscModNodePrefixesIndex": mscModNodePrefixesIndex,
       "mscModNodePrefixesValue": mscModNodePrefixesValue,
       "mscModAlternatePorsPrefixesTable": mscModAlternatePorsPrefixesTable,
       "mscModAlternatePorsPrefixesEntry": mscModAlternatePorsPrefixesEntry,
       "mscModAlternatePorsPrefixesIndex": mscModAlternatePorsPrefixesIndex,
       "mscModAlternatePorsPrefixesValue": mscModAlternatePorsPrefixesValue,
       "baseShelfMIB": baseShelfMIB,
       "baseShelfGroup": baseShelfGroup,
       "baseShelfGroupCA": baseShelfGroupCA,
       "baseShelfGroupCA02": baseShelfGroupCA02,
       "baseShelfGroupCA02A": baseShelfGroupCA02A,
       "baseShelfCapabilities": baseShelfCapabilities,
       "baseShelfCapabilitiesCA": baseShelfCapabilitiesCA,
       "baseShelfCapabilitiesCA02": baseShelfCapabilitiesCA02,
       "baseShelfCapabilitiesCA02A": baseShelfCapabilitiesCA02A}
)
