# SNMP MIB module (Nortel-Magellan-Passport-ShelfMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ShelfMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:10 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "ExtendedAsciiString",
    "Hex",
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

_Shelf_ObjectIdentity = ObjectIdentity
shelf = _Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13)
)
_ShelfRowStatusTable_Object = MibTable
shelfRowStatusTable = _ShelfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    shelfRowStatusTable.setStatus("mandatory")
_ShelfRowStatusEntry_Object = MibTableRow
shelfRowStatusEntry = _ShelfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 1, 1)
)
shelfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
)
if mibBuilder.loadTexts:
    shelfRowStatusEntry.setStatus("mandatory")
_ShelfRowStatus_Type = RowStatus
_ShelfRowStatus_Object = MibTableColumn
shelfRowStatus = _ShelfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 1, 1, 1),
    _ShelfRowStatus_Type()
)
shelfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfRowStatus.setStatus("mandatory")
_ShelfComponentName_Type = DisplayString
_ShelfComponentName_Object = MibTableColumn
shelfComponentName = _ShelfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 1, 1, 2),
    _ShelfComponentName_Type()
)
shelfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfComponentName.setStatus("mandatory")
_ShelfStorageType_Type = StorageType
_ShelfStorageType_Object = MibTableColumn
shelfStorageType = _ShelfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 1, 1, 4),
    _ShelfStorageType_Type()
)
shelfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfStorageType.setStatus("mandatory")
_ShelfIndex_Type = NonReplicated
_ShelfIndex_Object = MibTableColumn
shelfIndex = _ShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 1, 1, 10),
    _ShelfIndex_Type()
)
shelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfIndex.setStatus("mandatory")
_ShelfCard_ObjectIdentity = ObjectIdentity
shelfCard = _ShelfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2)
)
_ShelfCardRowStatusTable_Object = MibTable
shelfCardRowStatusTable = _ShelfCardRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    shelfCardRowStatusTable.setStatus("mandatory")
_ShelfCardRowStatusEntry_Object = MibTableRow
shelfCardRowStatusEntry = _ShelfCardRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 1, 1)
)
shelfCardRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
)
if mibBuilder.loadTexts:
    shelfCardRowStatusEntry.setStatus("mandatory")
_ShelfCardRowStatus_Type = RowStatus
_ShelfCardRowStatus_Object = MibTableColumn
shelfCardRowStatus = _ShelfCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 1, 1, 1),
    _ShelfCardRowStatus_Type()
)
shelfCardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardRowStatus.setStatus("mandatory")
_ShelfCardComponentName_Type = DisplayString
_ShelfCardComponentName_Object = MibTableColumn
shelfCardComponentName = _ShelfCardComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 1, 1, 2),
    _ShelfCardComponentName_Type()
)
shelfCardComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardComponentName.setStatus("mandatory")
_ShelfCardStorageType_Type = StorageType
_ShelfCardStorageType_Object = MibTableColumn
shelfCardStorageType = _ShelfCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 1, 1, 4),
    _ShelfCardStorageType_Type()
)
shelfCardStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardStorageType.setStatus("mandatory")


class _ShelfCardIndex_Type(Integer32):
    """Custom type shelfCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfCardIndex_Type.__name__ = "Integer32"
_ShelfCardIndex_Object = MibTableColumn
shelfCardIndex = _ShelfCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 1, 1, 10),
    _ShelfCardIndex_Type()
)
shelfCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardIndex.setStatus("mandatory")
_ShelfCardBusTap_ObjectIdentity = ObjectIdentity
shelfCardBusTap = _ShelfCardBusTap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2)
)
_ShelfCardBusTapRowStatusTable_Object = MibTable
shelfCardBusTapRowStatusTable = _ShelfCardBusTapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    shelfCardBusTapRowStatusTable.setStatus("mandatory")
_ShelfCardBusTapRowStatusEntry_Object = MibTableRow
shelfCardBusTapRowStatusEntry = _ShelfCardBusTapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 1, 1)
)
shelfCardBusTapRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardBusTapIndex"),
)
if mibBuilder.loadTexts:
    shelfCardBusTapRowStatusEntry.setStatus("mandatory")
_ShelfCardBusTapRowStatus_Type = RowStatus
_ShelfCardBusTapRowStatus_Object = MibTableColumn
shelfCardBusTapRowStatus = _ShelfCardBusTapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 1, 1, 1),
    _ShelfCardBusTapRowStatus_Type()
)
shelfCardBusTapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapRowStatus.setStatus("mandatory")
_ShelfCardBusTapComponentName_Type = DisplayString
_ShelfCardBusTapComponentName_Object = MibTableColumn
shelfCardBusTapComponentName = _ShelfCardBusTapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 1, 1, 2),
    _ShelfCardBusTapComponentName_Type()
)
shelfCardBusTapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapComponentName.setStatus("mandatory")
_ShelfCardBusTapStorageType_Type = StorageType
_ShelfCardBusTapStorageType_Object = MibTableColumn
shelfCardBusTapStorageType = _ShelfCardBusTapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 1, 1, 4),
    _ShelfCardBusTapStorageType_Type()
)
shelfCardBusTapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapStorageType.setStatus("mandatory")


class _ShelfCardBusTapIndex_Type(Integer32):
    """Custom type shelfCardBusTapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("x", 0),
          ("y", 1))
    )


_ShelfCardBusTapIndex_Type.__name__ = "Integer32"
_ShelfCardBusTapIndex_Object = MibTableColumn
shelfCardBusTapIndex = _ShelfCardBusTapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 1, 1, 10),
    _ShelfCardBusTapIndex_Type()
)
shelfCardBusTapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardBusTapIndex.setStatus("mandatory")
_ShelfCardBusTapStateTable_Object = MibTable
shelfCardBusTapStateTable = _ShelfCardBusTapStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10)
)
if mibBuilder.loadTexts:
    shelfCardBusTapStateTable.setStatus("mandatory")
_ShelfCardBusTapStateEntry_Object = MibTableRow
shelfCardBusTapStateEntry = _ShelfCardBusTapStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1)
)
shelfCardBusTapStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardBusTapIndex"),
)
if mibBuilder.loadTexts:
    shelfCardBusTapStateEntry.setStatus("mandatory")


class _ShelfCardBusTapAdminState_Type(Integer32):
    """Custom type shelfCardBusTapAdminState based on Integer32"""
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


_ShelfCardBusTapAdminState_Type.__name__ = "Integer32"
_ShelfCardBusTapAdminState_Object = MibTableColumn
shelfCardBusTapAdminState = _ShelfCardBusTapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1, 1),
    _ShelfCardBusTapAdminState_Type()
)
shelfCardBusTapAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapAdminState.setStatus("mandatory")


class _ShelfCardBusTapOperationalState_Type(Integer32):
    """Custom type shelfCardBusTapOperationalState based on Integer32"""
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


_ShelfCardBusTapOperationalState_Type.__name__ = "Integer32"
_ShelfCardBusTapOperationalState_Object = MibTableColumn
shelfCardBusTapOperationalState = _ShelfCardBusTapOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1, 2),
    _ShelfCardBusTapOperationalState_Type()
)
shelfCardBusTapOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapOperationalState.setStatus("mandatory")


class _ShelfCardBusTapUsageState_Type(Integer32):
    """Custom type shelfCardBusTapUsageState based on Integer32"""
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


_ShelfCardBusTapUsageState_Type.__name__ = "Integer32"
_ShelfCardBusTapUsageState_Object = MibTableColumn
shelfCardBusTapUsageState = _ShelfCardBusTapUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1, 3),
    _ShelfCardBusTapUsageState_Type()
)
shelfCardBusTapUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapUsageState.setStatus("mandatory")


class _ShelfCardBusTapAvailabilityStatus_Type(OctetString):
    """Custom type shelfCardBusTapAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ShelfCardBusTapAvailabilityStatus_Type.__name__ = "OctetString"
_ShelfCardBusTapAvailabilityStatus_Object = MibTableColumn
shelfCardBusTapAvailabilityStatus = _ShelfCardBusTapAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1, 4),
    _ShelfCardBusTapAvailabilityStatus_Type()
)
shelfCardBusTapAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapAvailabilityStatus.setStatus("mandatory")


class _ShelfCardBusTapProceduralStatus_Type(OctetString):
    """Custom type shelfCardBusTapProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardBusTapProceduralStatus_Type.__name__ = "OctetString"
_ShelfCardBusTapProceduralStatus_Object = MibTableColumn
shelfCardBusTapProceduralStatus = _ShelfCardBusTapProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1, 5),
    _ShelfCardBusTapProceduralStatus_Type()
)
shelfCardBusTapProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapProceduralStatus.setStatus("mandatory")


class _ShelfCardBusTapControlStatus_Type(OctetString):
    """Custom type shelfCardBusTapControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardBusTapControlStatus_Type.__name__ = "OctetString"
_ShelfCardBusTapControlStatus_Object = MibTableColumn
shelfCardBusTapControlStatus = _ShelfCardBusTapControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1, 6),
    _ShelfCardBusTapControlStatus_Type()
)
shelfCardBusTapControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapControlStatus.setStatus("mandatory")


class _ShelfCardBusTapAlarmStatus_Type(OctetString):
    """Custom type shelfCardBusTapAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardBusTapAlarmStatus_Type.__name__ = "OctetString"
_ShelfCardBusTapAlarmStatus_Object = MibTableColumn
shelfCardBusTapAlarmStatus = _ShelfCardBusTapAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1, 7),
    _ShelfCardBusTapAlarmStatus_Type()
)
shelfCardBusTapAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapAlarmStatus.setStatus("mandatory")


class _ShelfCardBusTapStandbyStatus_Type(Integer32):
    """Custom type shelfCardBusTapStandbyStatus based on Integer32"""
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


_ShelfCardBusTapStandbyStatus_Type.__name__ = "Integer32"
_ShelfCardBusTapStandbyStatus_Object = MibTableColumn
shelfCardBusTapStandbyStatus = _ShelfCardBusTapStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1, 8),
    _ShelfCardBusTapStandbyStatus_Type()
)
shelfCardBusTapStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapStandbyStatus.setStatus("mandatory")


class _ShelfCardBusTapUnknownStatus_Type(Integer32):
    """Custom type shelfCardBusTapUnknownStatus based on Integer32"""
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


_ShelfCardBusTapUnknownStatus_Type.__name__ = "Integer32"
_ShelfCardBusTapUnknownStatus_Object = MibTableColumn
shelfCardBusTapUnknownStatus = _ShelfCardBusTapUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 10, 1, 9),
    _ShelfCardBusTapUnknownStatus_Type()
)
shelfCardBusTapUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapUnknownStatus.setStatus("mandatory")
_ShelfCardBusTapOperTable_Object = MibTable
shelfCardBusTapOperTable = _ShelfCardBusTapOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 11)
)
if mibBuilder.loadTexts:
    shelfCardBusTapOperTable.setStatus("mandatory")
_ShelfCardBusTapOperEntry_Object = MibTableRow
shelfCardBusTapOperEntry = _ShelfCardBusTapOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 11, 1)
)
shelfCardBusTapOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardBusTapIndex"),
)
if mibBuilder.loadTexts:
    shelfCardBusTapOperEntry.setStatus("mandatory")


class _ShelfCardBusTapFailuresInEffect_Type(OctetString):
    """Custom type shelfCardBusTapFailuresInEffect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardBusTapFailuresInEffect_Type.__name__ = "OctetString"
_ShelfCardBusTapFailuresInEffect_Object = MibTableColumn
shelfCardBusTapFailuresInEffect = _ShelfCardBusTapFailuresInEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 11, 1, 1),
    _ShelfCardBusTapFailuresInEffect_Type()
)
shelfCardBusTapFailuresInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapFailuresInEffect.setStatus("mandatory")


class _ShelfCardBusTapDependenciesInEffect_Type(OctetString):
    """Custom type shelfCardBusTapDependenciesInEffect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardBusTapDependenciesInEffect_Type.__name__ = "OctetString"
_ShelfCardBusTapDependenciesInEffect_Object = MibTableColumn
shelfCardBusTapDependenciesInEffect = _ShelfCardBusTapDependenciesInEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 11, 1, 2),
    _ShelfCardBusTapDependenciesInEffect_Type()
)
shelfCardBusTapDependenciesInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapDependenciesInEffect.setStatus("mandatory")


class _ShelfCardBusTapCardsAvailable_Type(OctetString):
    """Custom type shelfCardBusTapCardsAvailable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ShelfCardBusTapCardsAvailable_Type.__name__ = "OctetString"
_ShelfCardBusTapCardsAvailable_Object = MibTableColumn
shelfCardBusTapCardsAvailable = _ShelfCardBusTapCardsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 11, 1, 3),
    _ShelfCardBusTapCardsAvailable_Type()
)
shelfCardBusTapCardsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapCardsAvailable.setStatus("mandatory")


class _ShelfCardBusTapCardsTxTo_Type(OctetString):
    """Custom type shelfCardBusTapCardsTxTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ShelfCardBusTapCardsTxTo_Type.__name__ = "OctetString"
_ShelfCardBusTapCardsTxTo_Object = MibTableColumn
shelfCardBusTapCardsTxTo = _ShelfCardBusTapCardsTxTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 11, 1, 4),
    _ShelfCardBusTapCardsTxTo_Type()
)
shelfCardBusTapCardsTxTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapCardsTxTo.setStatus("mandatory")
_ShelfCardBusTapErrorsTable_Object = MibTable
shelfCardBusTapErrorsTable = _ShelfCardBusTapErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12)
)
if mibBuilder.loadTexts:
    shelfCardBusTapErrorsTable.setStatus("mandatory")
_ShelfCardBusTapErrorsEntry_Object = MibTableRow
shelfCardBusTapErrorsEntry = _ShelfCardBusTapErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1)
)
shelfCardBusTapErrorsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardBusTapIndex"),
)
if mibBuilder.loadTexts:
    shelfCardBusTapErrorsEntry.setStatus("mandatory")


class _ShelfCardBusTapSelfTestErrorCode_Type(Unsigned32):
    """Custom type shelfCardBusTapSelfTestErrorCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardBusTapSelfTestErrorCode_Type.__name__ = "Unsigned32"
_ShelfCardBusTapSelfTestErrorCode_Object = MibTableColumn
shelfCardBusTapSelfTestErrorCode = _ShelfCardBusTapSelfTestErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1, 1),
    _ShelfCardBusTapSelfTestErrorCode_Type()
)
shelfCardBusTapSelfTestErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapSelfTestErrorCode.setStatus("mandatory")


class _ShelfCardBusTapClockErrors_Type(Unsigned32):
    """Custom type shelfCardBusTapClockErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardBusTapClockErrors_Type.__name__ = "Unsigned32"
_ShelfCardBusTapClockErrors_Object = MibTableColumn
shelfCardBusTapClockErrors = _ShelfCardBusTapClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1, 2),
    _ShelfCardBusTapClockErrors_Type()
)
shelfCardBusTapClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapClockErrors.setStatus("mandatory")


class _ShelfCardBusTapEndOfCellErrors_Type(Unsigned32):
    """Custom type shelfCardBusTapEndOfCellErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardBusTapEndOfCellErrors_Type.__name__ = "Unsigned32"
_ShelfCardBusTapEndOfCellErrors_Object = MibTableColumn
shelfCardBusTapEndOfCellErrors = _ShelfCardBusTapEndOfCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1, 3),
    _ShelfCardBusTapEndOfCellErrors_Type()
)
shelfCardBusTapEndOfCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapEndOfCellErrors.setStatus("mandatory")


class _ShelfCardBusTapParityErrors_Type(Unsigned32):
    """Custom type shelfCardBusTapParityErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardBusTapParityErrors_Type.__name__ = "Unsigned32"
_ShelfCardBusTapParityErrors_Object = MibTableColumn
shelfCardBusTapParityErrors = _ShelfCardBusTapParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1, 4),
    _ShelfCardBusTapParityErrors_Type()
)
shelfCardBusTapParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapParityErrors.setStatus("mandatory")


class _ShelfCardBusTapFrmCongestionErrors_Type(Unsigned32):
    """Custom type shelfCardBusTapFrmCongestionErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardBusTapFrmCongestionErrors_Type.__name__ = "Unsigned32"
_ShelfCardBusTapFrmCongestionErrors_Object = MibTableColumn
shelfCardBusTapFrmCongestionErrors = _ShelfCardBusTapFrmCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1, 5),
    _ShelfCardBusTapFrmCongestionErrors_Type()
)
shelfCardBusTapFrmCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapFrmCongestionErrors.setStatus("mandatory")


class _ShelfCardBusTapFrmCollisionErrors_Type(Unsigned32):
    """Custom type shelfCardBusTapFrmCollisionErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardBusTapFrmCollisionErrors_Type.__name__ = "Unsigned32"
_ShelfCardBusTapFrmCollisionErrors_Object = MibTableColumn
shelfCardBusTapFrmCollisionErrors = _ShelfCardBusTapFrmCollisionErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1, 6),
    _ShelfCardBusTapFrmCollisionErrors_Type()
)
shelfCardBusTapFrmCollisionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapFrmCollisionErrors.setStatus("mandatory")


class _ShelfCardBusTapFrmTimeoutErrors_Type(Unsigned32):
    """Custom type shelfCardBusTapFrmTimeoutErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardBusTapFrmTimeoutErrors_Type.__name__ = "Unsigned32"
_ShelfCardBusTapFrmTimeoutErrors_Object = MibTableColumn
shelfCardBusTapFrmTimeoutErrors = _ShelfCardBusTapFrmTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1, 7),
    _ShelfCardBusTapFrmTimeoutErrors_Type()
)
shelfCardBusTapFrmTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapFrmTimeoutErrors.setStatus("mandatory")


class _ShelfCardBusTapFrmDeliveryErrors_Type(Unsigned32):
    """Custom type shelfCardBusTapFrmDeliveryErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardBusTapFrmDeliveryErrors_Type.__name__ = "Unsigned32"
_ShelfCardBusTapFrmDeliveryErrors_Object = MibTableColumn
shelfCardBusTapFrmDeliveryErrors = _ShelfCardBusTapFrmDeliveryErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1, 8),
    _ShelfCardBusTapFrmDeliveryErrors_Type()
)
shelfCardBusTapFrmDeliveryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapFrmDeliveryErrors.setStatus("mandatory")


class _ShelfCardBusTapFrmSizeErrors_Type(Unsigned32):
    """Custom type shelfCardBusTapFrmSizeErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardBusTapFrmSizeErrors_Type.__name__ = "Unsigned32"
_ShelfCardBusTapFrmSizeErrors_Object = MibTableColumn
shelfCardBusTapFrmSizeErrors = _ShelfCardBusTapFrmSizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 2, 12, 1, 9),
    _ShelfCardBusTapFrmSizeErrors_Type()
)
shelfCardBusTapFrmSizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardBusTapFrmSizeErrors.setStatus("mandatory")
_ShelfCardTest_ObjectIdentity = ObjectIdentity
shelfCardTest = _ShelfCardTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3)
)
_ShelfCardTestRowStatusTable_Object = MibTable
shelfCardTestRowStatusTable = _ShelfCardTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 1)
)
if mibBuilder.loadTexts:
    shelfCardTestRowStatusTable.setStatus("mandatory")
_ShelfCardTestRowStatusEntry_Object = MibTableRow
shelfCardTestRowStatusEntry = _ShelfCardTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 1, 1)
)
shelfCardTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestIndex"),
)
if mibBuilder.loadTexts:
    shelfCardTestRowStatusEntry.setStatus("mandatory")
_ShelfCardTestRowStatus_Type = RowStatus
_ShelfCardTestRowStatus_Object = MibTableColumn
shelfCardTestRowStatus = _ShelfCardTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 1, 1, 1),
    _ShelfCardTestRowStatus_Type()
)
shelfCardTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestRowStatus.setStatus("mandatory")
_ShelfCardTestComponentName_Type = DisplayString
_ShelfCardTestComponentName_Object = MibTableColumn
shelfCardTestComponentName = _ShelfCardTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 1, 1, 2),
    _ShelfCardTestComponentName_Type()
)
shelfCardTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestComponentName.setStatus("mandatory")
_ShelfCardTestStorageType_Type = StorageType
_ShelfCardTestStorageType_Object = MibTableColumn
shelfCardTestStorageType = _ShelfCardTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 1, 1, 4),
    _ShelfCardTestStorageType_Type()
)
shelfCardTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestStorageType.setStatus("mandatory")
_ShelfCardTestIndex_Type = NonReplicated
_ShelfCardTestIndex_Object = MibTableColumn
shelfCardTestIndex = _ShelfCardTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 1, 1, 10),
    _ShelfCardTestIndex_Type()
)
shelfCardTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardTestIndex.setStatus("mandatory")
_ShelfCardTestStateTable_Object = MibTable
shelfCardTestStateTable = _ShelfCardTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 10)
)
if mibBuilder.loadTexts:
    shelfCardTestStateTable.setStatus("mandatory")
_ShelfCardTestStateEntry_Object = MibTableRow
shelfCardTestStateEntry = _ShelfCardTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 10, 1)
)
shelfCardTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestIndex"),
)
if mibBuilder.loadTexts:
    shelfCardTestStateEntry.setStatus("mandatory")


class _ShelfCardTestAdminState_Type(Integer32):
    """Custom type shelfCardTestAdminState based on Integer32"""
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


_ShelfCardTestAdminState_Type.__name__ = "Integer32"
_ShelfCardTestAdminState_Object = MibTableColumn
shelfCardTestAdminState = _ShelfCardTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 10, 1, 1),
    _ShelfCardTestAdminState_Type()
)
shelfCardTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestAdminState.setStatus("mandatory")


class _ShelfCardTestOperationalState_Type(Integer32):
    """Custom type shelfCardTestOperationalState based on Integer32"""
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


_ShelfCardTestOperationalState_Type.__name__ = "Integer32"
_ShelfCardTestOperationalState_Object = MibTableColumn
shelfCardTestOperationalState = _ShelfCardTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 10, 1, 2),
    _ShelfCardTestOperationalState_Type()
)
shelfCardTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestOperationalState.setStatus("mandatory")


class _ShelfCardTestUsageState_Type(Integer32):
    """Custom type shelfCardTestUsageState based on Integer32"""
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


_ShelfCardTestUsageState_Type.__name__ = "Integer32"
_ShelfCardTestUsageState_Object = MibTableColumn
shelfCardTestUsageState = _ShelfCardTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 10, 1, 3),
    _ShelfCardTestUsageState_Type()
)
shelfCardTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestUsageState.setStatus("mandatory")
_ShelfCardTestSetupTable_Object = MibTable
shelfCardTestSetupTable = _ShelfCardTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 11)
)
if mibBuilder.loadTexts:
    shelfCardTestSetupTable.setStatus("mandatory")
_ShelfCardTestSetupEntry_Object = MibTableRow
shelfCardTestSetupEntry = _ShelfCardTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 11, 1)
)
shelfCardTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestIndex"),
)
if mibBuilder.loadTexts:
    shelfCardTestSetupEntry.setStatus("mandatory")


class _ShelfCardTestTargetCard_Type(Unsigned32):
    """Custom type shelfCardTestTargetCard based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfCardTestTargetCard_Type.__name__ = "Unsigned32"
_ShelfCardTestTargetCard_Object = MibTableColumn
shelfCardTestTargetCard = _ShelfCardTestTargetCard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 11, 1, 1),
    _ShelfCardTestTargetCard_Type()
)
shelfCardTestTargetCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardTestTargetCard.setStatus("mandatory")


class _ShelfCardTestFrmTypes_Type(OctetString):
    """Custom type shelfCardTestFrmTypes based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardTestFrmTypes_Type.__name__ = "OctetString"
_ShelfCardTestFrmTypes_Object = MibTableColumn
shelfCardTestFrmTypes = _ShelfCardTestFrmTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 11, 1, 2),
    _ShelfCardTestFrmTypes_Type()
)
shelfCardTestFrmTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardTestFrmTypes.setStatus("mandatory")


class _ShelfCardTestFrmPriorities_Type(OctetString):
    """Custom type shelfCardTestFrmPriorities based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardTestFrmPriorities_Type.__name__ = "OctetString"
_ShelfCardTestFrmPriorities_Object = MibTableColumn
shelfCardTestFrmPriorities = _ShelfCardTestFrmPriorities_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 11, 1, 3),
    _ShelfCardTestFrmPriorities_Type()
)
shelfCardTestFrmPriorities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardTestFrmPriorities.setStatus("mandatory")


class _ShelfCardTestFrmPatternType_Type(Integer32):
    """Custom type shelfCardTestFrmPatternType based on Integer32"""
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


_ShelfCardTestFrmPatternType_Type.__name__ = "Integer32"
_ShelfCardTestFrmPatternType_Object = MibTableColumn
shelfCardTestFrmPatternType = _ShelfCardTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 11, 1, 4),
    _ShelfCardTestFrmPatternType_Type()
)
shelfCardTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardTestFrmPatternType.setStatus("mandatory")


class _ShelfCardTestCustomizedPattern_Type(Hex):
    """Custom type shelfCardTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardTestCustomizedPattern_Type.__name__ = "Hex"
_ShelfCardTestCustomizedPattern_Object = MibTableColumn
shelfCardTestCustomizedPattern = _ShelfCardTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 11, 1, 5),
    _ShelfCardTestCustomizedPattern_Type()
)
shelfCardTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardTestCustomizedPattern.setStatus("mandatory")


class _ShelfCardTestDuration_Type(Unsigned32):
    """Custom type shelfCardTestDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 43200),
    )


_ShelfCardTestDuration_Type.__name__ = "Unsigned32"
_ShelfCardTestDuration_Object = MibTableColumn
shelfCardTestDuration = _ShelfCardTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 11, 1, 6),
    _ShelfCardTestDuration_Type()
)
shelfCardTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardTestDuration.setStatus("mandatory")
_ShelfCardTestResultsTable_Object = MibTable
shelfCardTestResultsTable = _ShelfCardTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 12)
)
if mibBuilder.loadTexts:
    shelfCardTestResultsTable.setStatus("mandatory")
_ShelfCardTestResultsEntry_Object = MibTableRow
shelfCardTestResultsEntry = _ShelfCardTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 12, 1)
)
shelfCardTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestIndex"),
)
if mibBuilder.loadTexts:
    shelfCardTestResultsEntry.setStatus("mandatory")


class _ShelfCardTestElapsedTime_Type(Unsigned32):
    """Custom type shelfCardTestElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_ShelfCardTestElapsedTime_Type.__name__ = "Unsigned32"
_ShelfCardTestElapsedTime_Object = MibTableColumn
shelfCardTestElapsedTime = _ShelfCardTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 12, 1, 1),
    _ShelfCardTestElapsedTime_Type()
)
shelfCardTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestElapsedTime.setStatus("mandatory")


class _ShelfCardTestTimeRemaining_Type(Unsigned32):
    """Custom type shelfCardTestTimeRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_ShelfCardTestTimeRemaining_Type.__name__ = "Unsigned32"
_ShelfCardTestTimeRemaining_Object = MibTableColumn
shelfCardTestTimeRemaining = _ShelfCardTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 12, 1, 2),
    _ShelfCardTestTimeRemaining_Type()
)
shelfCardTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestTimeRemaining.setStatus("mandatory")


class _ShelfCardTestCauseOfTermination_Type(Integer32):
    """Custom type shelfCardTestCauseOfTermination based on Integer32"""
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


_ShelfCardTestCauseOfTermination_Type.__name__ = "Integer32"
_ShelfCardTestCauseOfTermination_Object = MibTableColumn
shelfCardTestCauseOfTermination = _ShelfCardTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 12, 1, 3),
    _ShelfCardTestCauseOfTermination_Type()
)
shelfCardTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestCauseOfTermination.setStatus("mandatory")
_ShelfCardTestSizeTable_Object = MibTable
shelfCardTestSizeTable = _ShelfCardTestSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 253)
)
if mibBuilder.loadTexts:
    shelfCardTestSizeTable.setStatus("mandatory")
_ShelfCardTestSizeEntry_Object = MibTableRow
shelfCardTestSizeEntry = _ShelfCardTestSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 253, 1)
)
shelfCardTestSizeEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestSizeIndex"),
)
if mibBuilder.loadTexts:
    shelfCardTestSizeEntry.setStatus("mandatory")


class _ShelfCardTestSizeIndex_Type(Integer32):
    """Custom type shelfCardTestSizeIndex based on Integer32"""
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


_ShelfCardTestSizeIndex_Type.__name__ = "Integer32"
_ShelfCardTestSizeIndex_Object = MibTableColumn
shelfCardTestSizeIndex = _ShelfCardTestSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 253, 1, 1),
    _ShelfCardTestSizeIndex_Type()
)
shelfCardTestSizeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardTestSizeIndex.setStatus("mandatory")


class _ShelfCardTestSizeValue_Type(Unsigned32):
    """Custom type shelfCardTestSizeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16000),
    )


_ShelfCardTestSizeValue_Type.__name__ = "Unsigned32"
_ShelfCardTestSizeValue_Object = MibTableColumn
shelfCardTestSizeValue = _ShelfCardTestSizeValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 253, 1, 2),
    _ShelfCardTestSizeValue_Type()
)
shelfCardTestSizeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardTestSizeValue.setStatus("mandatory")
_ShelfCardTestLoadingFrmDataTable_Object = MibTable
shelfCardTestLoadingFrmDataTable = _ShelfCardTestLoadingFrmDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 254)
)
if mibBuilder.loadTexts:
    shelfCardTestLoadingFrmDataTable.setStatus("mandatory")
_ShelfCardTestLoadingFrmDataEntry_Object = MibTableRow
shelfCardTestLoadingFrmDataEntry = _ShelfCardTestLoadingFrmDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 254, 1)
)
shelfCardTestLoadingFrmDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestLoadingFrmDataResultsIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestLoadingFrmDataPriorityIndex"),
)
if mibBuilder.loadTexts:
    shelfCardTestLoadingFrmDataEntry.setStatus("mandatory")


class _ShelfCardTestLoadingFrmDataResultsIndex_Type(Integer32):
    """Custom type shelfCardTestLoadingFrmDataResultsIndex based on Integer32"""
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


_ShelfCardTestLoadingFrmDataResultsIndex_Type.__name__ = "Integer32"
_ShelfCardTestLoadingFrmDataResultsIndex_Object = MibTableColumn
shelfCardTestLoadingFrmDataResultsIndex = _ShelfCardTestLoadingFrmDataResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 254, 1, 1),
    _ShelfCardTestLoadingFrmDataResultsIndex_Type()
)
shelfCardTestLoadingFrmDataResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardTestLoadingFrmDataResultsIndex.setStatus("mandatory")


class _ShelfCardTestLoadingFrmDataPriorityIndex_Type(Integer32):
    """Custom type shelfCardTestLoadingFrmDataPriorityIndex based on Integer32"""
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


_ShelfCardTestLoadingFrmDataPriorityIndex_Type.__name__ = "Integer32"
_ShelfCardTestLoadingFrmDataPriorityIndex_Object = MibTableColumn
shelfCardTestLoadingFrmDataPriorityIndex = _ShelfCardTestLoadingFrmDataPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 254, 1, 2),
    _ShelfCardTestLoadingFrmDataPriorityIndex_Type()
)
shelfCardTestLoadingFrmDataPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardTestLoadingFrmDataPriorityIndex.setStatus("mandatory")


class _ShelfCardTestLoadingFrmDataValue_Type(Unsigned32):
    """Custom type shelfCardTestLoadingFrmDataValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardTestLoadingFrmDataValue_Type.__name__ = "Unsigned32"
_ShelfCardTestLoadingFrmDataValue_Object = MibTableColumn
shelfCardTestLoadingFrmDataValue = _ShelfCardTestLoadingFrmDataValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 254, 1, 3),
    _ShelfCardTestLoadingFrmDataValue_Type()
)
shelfCardTestLoadingFrmDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestLoadingFrmDataValue.setStatus("mandatory")
_ShelfCardTestVerificationFrmDataTable_Object = MibTable
shelfCardTestVerificationFrmDataTable = _ShelfCardTestVerificationFrmDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 255)
)
if mibBuilder.loadTexts:
    shelfCardTestVerificationFrmDataTable.setStatus("mandatory")
_ShelfCardTestVerificationFrmDataEntry_Object = MibTableRow
shelfCardTestVerificationFrmDataEntry = _ShelfCardTestVerificationFrmDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 255, 1)
)
shelfCardTestVerificationFrmDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestVerificationFrmDataResultsIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardTestVerificationFrmDataPriorityIndex"),
)
if mibBuilder.loadTexts:
    shelfCardTestVerificationFrmDataEntry.setStatus("mandatory")


class _ShelfCardTestVerificationFrmDataResultsIndex_Type(Integer32):
    """Custom type shelfCardTestVerificationFrmDataResultsIndex based on Integer32"""
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


_ShelfCardTestVerificationFrmDataResultsIndex_Type.__name__ = "Integer32"
_ShelfCardTestVerificationFrmDataResultsIndex_Object = MibTableColumn
shelfCardTestVerificationFrmDataResultsIndex = _ShelfCardTestVerificationFrmDataResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 255, 1, 1),
    _ShelfCardTestVerificationFrmDataResultsIndex_Type()
)
shelfCardTestVerificationFrmDataResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardTestVerificationFrmDataResultsIndex.setStatus("mandatory")


class _ShelfCardTestVerificationFrmDataPriorityIndex_Type(Integer32):
    """Custom type shelfCardTestVerificationFrmDataPriorityIndex based on Integer32"""
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


_ShelfCardTestVerificationFrmDataPriorityIndex_Type.__name__ = "Integer32"
_ShelfCardTestVerificationFrmDataPriorityIndex_Object = MibTableColumn
shelfCardTestVerificationFrmDataPriorityIndex = _ShelfCardTestVerificationFrmDataPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 255, 1, 2),
    _ShelfCardTestVerificationFrmDataPriorityIndex_Type()
)
shelfCardTestVerificationFrmDataPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardTestVerificationFrmDataPriorityIndex.setStatus("mandatory")


class _ShelfCardTestVerificationFrmDataValue_Type(Unsigned32):
    """Custom type shelfCardTestVerificationFrmDataValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfCardTestVerificationFrmDataValue_Type.__name__ = "Unsigned32"
_ShelfCardTestVerificationFrmDataValue_Object = MibTableColumn
shelfCardTestVerificationFrmDataValue = _ShelfCardTestVerificationFrmDataValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 3, 255, 1, 3),
    _ShelfCardTestVerificationFrmDataValue_Type()
)
shelfCardTestVerificationFrmDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTestVerificationFrmDataValue.setStatus("mandatory")
_ShelfCardDiag_ObjectIdentity = ObjectIdentity
shelfCardDiag = _ShelfCardDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4)
)
_ShelfCardDiagRowStatusTable_Object = MibTable
shelfCardDiagRowStatusTable = _ShelfCardDiagRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 1)
)
if mibBuilder.loadTexts:
    shelfCardDiagRowStatusTable.setStatus("mandatory")
_ShelfCardDiagRowStatusEntry_Object = MibTableRow
shelfCardDiagRowStatusEntry = _ShelfCardDiagRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 1, 1)
)
shelfCardDiagRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagIndex"),
)
if mibBuilder.loadTexts:
    shelfCardDiagRowStatusEntry.setStatus("mandatory")
_ShelfCardDiagRowStatus_Type = RowStatus
_ShelfCardDiagRowStatus_Object = MibTableColumn
shelfCardDiagRowStatus = _ShelfCardDiagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 1, 1, 1),
    _ShelfCardDiagRowStatus_Type()
)
shelfCardDiagRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagRowStatus.setStatus("mandatory")
_ShelfCardDiagComponentName_Type = DisplayString
_ShelfCardDiagComponentName_Object = MibTableColumn
shelfCardDiagComponentName = _ShelfCardDiagComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 1, 1, 2),
    _ShelfCardDiagComponentName_Type()
)
shelfCardDiagComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagComponentName.setStatus("mandatory")
_ShelfCardDiagStorageType_Type = StorageType
_ShelfCardDiagStorageType_Object = MibTableColumn
shelfCardDiagStorageType = _ShelfCardDiagStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 1, 1, 4),
    _ShelfCardDiagStorageType_Type()
)
shelfCardDiagStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagStorageType.setStatus("mandatory")
_ShelfCardDiagIndex_Type = NonReplicated
_ShelfCardDiagIndex_Object = MibTableColumn
shelfCardDiagIndex = _ShelfCardDiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 1, 1, 10),
    _ShelfCardDiagIndex_Type()
)
shelfCardDiagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardDiagIndex.setStatus("mandatory")
_ShelfCardDiagTrapData_ObjectIdentity = ObjectIdentity
shelfCardDiagTrapData = _ShelfCardDiagTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2)
)
_ShelfCardDiagTrapDataRowStatusTable_Object = MibTable
shelfCardDiagTrapDataRowStatusTable = _ShelfCardDiagTrapDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataRowStatusTable.setStatus("mandatory")
_ShelfCardDiagTrapDataRowStatusEntry_Object = MibTableRow
shelfCardDiagTrapDataRowStatusEntry = _ShelfCardDiagTrapDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 1, 1)
)
shelfCardDiagTrapDataRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagTrapDataIndex"),
)
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataRowStatusEntry.setStatus("mandatory")
_ShelfCardDiagTrapDataRowStatus_Type = RowStatus
_ShelfCardDiagTrapDataRowStatus_Object = MibTableColumn
shelfCardDiagTrapDataRowStatus = _ShelfCardDiagTrapDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 1, 1, 1),
    _ShelfCardDiagTrapDataRowStatus_Type()
)
shelfCardDiagTrapDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataRowStatus.setStatus("mandatory")
_ShelfCardDiagTrapDataComponentName_Type = DisplayString
_ShelfCardDiagTrapDataComponentName_Object = MibTableColumn
shelfCardDiagTrapDataComponentName = _ShelfCardDiagTrapDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 1, 1, 2),
    _ShelfCardDiagTrapDataComponentName_Type()
)
shelfCardDiagTrapDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataComponentName.setStatus("mandatory")
_ShelfCardDiagTrapDataStorageType_Type = StorageType
_ShelfCardDiagTrapDataStorageType_Object = MibTableColumn
shelfCardDiagTrapDataStorageType = _ShelfCardDiagTrapDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 1, 1, 4),
    _ShelfCardDiagTrapDataStorageType_Type()
)
shelfCardDiagTrapDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataStorageType.setStatus("mandatory")
_ShelfCardDiagTrapDataIndex_Type = NonReplicated
_ShelfCardDiagTrapDataIndex_Object = MibTableColumn
shelfCardDiagTrapDataIndex = _ShelfCardDiagTrapDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 1, 1, 10),
    _ShelfCardDiagTrapDataIndex_Type()
)
shelfCardDiagTrapDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataIndex.setStatus("mandatory")
_ShelfCardDiagTrapDataLine_ObjectIdentity = ObjectIdentity
shelfCardDiagTrapDataLine = _ShelfCardDiagTrapDataLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2)
)
_ShelfCardDiagTrapDataLineRowStatusTable_Object = MibTable
shelfCardDiagTrapDataLineRowStatusTable = _ShelfCardDiagTrapDataLineRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataLineRowStatusTable.setStatus("mandatory")
_ShelfCardDiagTrapDataLineRowStatusEntry_Object = MibTableRow
shelfCardDiagTrapDataLineRowStatusEntry = _ShelfCardDiagTrapDataLineRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2, 1, 1)
)
shelfCardDiagTrapDataLineRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagTrapDataIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagTrapDataLineIndex"),
)
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataLineRowStatusEntry.setStatus("mandatory")
_ShelfCardDiagTrapDataLineRowStatus_Type = RowStatus
_ShelfCardDiagTrapDataLineRowStatus_Object = MibTableColumn
shelfCardDiagTrapDataLineRowStatus = _ShelfCardDiagTrapDataLineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2, 1, 1, 1),
    _ShelfCardDiagTrapDataLineRowStatus_Type()
)
shelfCardDiagTrapDataLineRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataLineRowStatus.setStatus("mandatory")
_ShelfCardDiagTrapDataLineComponentName_Type = DisplayString
_ShelfCardDiagTrapDataLineComponentName_Object = MibTableColumn
shelfCardDiagTrapDataLineComponentName = _ShelfCardDiagTrapDataLineComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2, 1, 1, 2),
    _ShelfCardDiagTrapDataLineComponentName_Type()
)
shelfCardDiagTrapDataLineComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataLineComponentName.setStatus("mandatory")
_ShelfCardDiagTrapDataLineStorageType_Type = StorageType
_ShelfCardDiagTrapDataLineStorageType_Object = MibTableColumn
shelfCardDiagTrapDataLineStorageType = _ShelfCardDiagTrapDataLineStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2, 1, 1, 4),
    _ShelfCardDiagTrapDataLineStorageType_Type()
)
shelfCardDiagTrapDataLineStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataLineStorageType.setStatus("mandatory")


class _ShelfCardDiagTrapDataLineIndex_Type(Integer32):
    """Custom type shelfCardDiagTrapDataLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ShelfCardDiagTrapDataLineIndex_Type.__name__ = "Integer32"
_ShelfCardDiagTrapDataLineIndex_Object = MibTableColumn
shelfCardDiagTrapDataLineIndex = _ShelfCardDiagTrapDataLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2, 1, 1, 10),
    _ShelfCardDiagTrapDataLineIndex_Type()
)
shelfCardDiagTrapDataLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataLineIndex.setStatus("mandatory")
_ShelfCardDiagTrapDataLineOperTable_Object = MibTable
shelfCardDiagTrapDataLineOperTable = _ShelfCardDiagTrapDataLineOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataLineOperTable.setStatus("mandatory")
_ShelfCardDiagTrapDataLineOperEntry_Object = MibTableRow
shelfCardDiagTrapDataLineOperEntry = _ShelfCardDiagTrapDataLineOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2, 10, 1)
)
shelfCardDiagTrapDataLineOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagTrapDataIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagTrapDataLineIndex"),
)
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataLineOperEntry.setStatus("mandatory")


class _ShelfCardDiagTrapDataLineData_Type(ExtendedAsciiString):
    """Custom type shelfCardDiagTrapDataLineData based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ShelfCardDiagTrapDataLineData_Type.__name__ = "ExtendedAsciiString"
_ShelfCardDiagTrapDataLineData_Object = MibTableColumn
shelfCardDiagTrapDataLineData = _ShelfCardDiagTrapDataLineData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 2, 2, 10, 1, 1),
    _ShelfCardDiagTrapDataLineData_Type()
)
shelfCardDiagTrapDataLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagTrapDataLineData.setStatus("mandatory")
_ShelfCardDiagRecErr_ObjectIdentity = ObjectIdentity
shelfCardDiagRecErr = _ShelfCardDiagRecErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3)
)
_ShelfCardDiagRecErrRowStatusTable_Object = MibTable
shelfCardDiagRecErrRowStatusTable = _ShelfCardDiagRecErrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    shelfCardDiagRecErrRowStatusTable.setStatus("mandatory")
_ShelfCardDiagRecErrRowStatusEntry_Object = MibTableRow
shelfCardDiagRecErrRowStatusEntry = _ShelfCardDiagRecErrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 1, 1)
)
shelfCardDiagRecErrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagRecErrIndex"),
)
if mibBuilder.loadTexts:
    shelfCardDiagRecErrRowStatusEntry.setStatus("mandatory")
_ShelfCardDiagRecErrRowStatus_Type = RowStatus
_ShelfCardDiagRecErrRowStatus_Object = MibTableColumn
shelfCardDiagRecErrRowStatus = _ShelfCardDiagRecErrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 1, 1, 1),
    _ShelfCardDiagRecErrRowStatus_Type()
)
shelfCardDiagRecErrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagRecErrRowStatus.setStatus("mandatory")
_ShelfCardDiagRecErrComponentName_Type = DisplayString
_ShelfCardDiagRecErrComponentName_Object = MibTableColumn
shelfCardDiagRecErrComponentName = _ShelfCardDiagRecErrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 1, 1, 2),
    _ShelfCardDiagRecErrComponentName_Type()
)
shelfCardDiagRecErrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagRecErrComponentName.setStatus("mandatory")
_ShelfCardDiagRecErrStorageType_Type = StorageType
_ShelfCardDiagRecErrStorageType_Object = MibTableColumn
shelfCardDiagRecErrStorageType = _ShelfCardDiagRecErrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 1, 1, 4),
    _ShelfCardDiagRecErrStorageType_Type()
)
shelfCardDiagRecErrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagRecErrStorageType.setStatus("mandatory")
_ShelfCardDiagRecErrIndex_Type = NonReplicated
_ShelfCardDiagRecErrIndex_Object = MibTableColumn
shelfCardDiagRecErrIndex = _ShelfCardDiagRecErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 1, 1, 10),
    _ShelfCardDiagRecErrIndex_Type()
)
shelfCardDiagRecErrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardDiagRecErrIndex.setStatus("mandatory")
_ShelfCardDiagRecErrLine_ObjectIdentity = ObjectIdentity
shelfCardDiagRecErrLine = _ShelfCardDiagRecErrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2)
)
_ShelfCardDiagRecErrLineRowStatusTable_Object = MibTable
shelfCardDiagRecErrLineRowStatusTable = _ShelfCardDiagRecErrLineRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    shelfCardDiagRecErrLineRowStatusTable.setStatus("mandatory")
_ShelfCardDiagRecErrLineRowStatusEntry_Object = MibTableRow
shelfCardDiagRecErrLineRowStatusEntry = _ShelfCardDiagRecErrLineRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2, 1, 1)
)
shelfCardDiagRecErrLineRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagRecErrIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagRecErrLineIndex"),
)
if mibBuilder.loadTexts:
    shelfCardDiagRecErrLineRowStatusEntry.setStatus("mandatory")
_ShelfCardDiagRecErrLineRowStatus_Type = RowStatus
_ShelfCardDiagRecErrLineRowStatus_Object = MibTableColumn
shelfCardDiagRecErrLineRowStatus = _ShelfCardDiagRecErrLineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2, 1, 1, 1),
    _ShelfCardDiagRecErrLineRowStatus_Type()
)
shelfCardDiagRecErrLineRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagRecErrLineRowStatus.setStatus("mandatory")
_ShelfCardDiagRecErrLineComponentName_Type = DisplayString
_ShelfCardDiagRecErrLineComponentName_Object = MibTableColumn
shelfCardDiagRecErrLineComponentName = _ShelfCardDiagRecErrLineComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2, 1, 1, 2),
    _ShelfCardDiagRecErrLineComponentName_Type()
)
shelfCardDiagRecErrLineComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagRecErrLineComponentName.setStatus("mandatory")
_ShelfCardDiagRecErrLineStorageType_Type = StorageType
_ShelfCardDiagRecErrLineStorageType_Object = MibTableColumn
shelfCardDiagRecErrLineStorageType = _ShelfCardDiagRecErrLineStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2, 1, 1, 4),
    _ShelfCardDiagRecErrLineStorageType_Type()
)
shelfCardDiagRecErrLineStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagRecErrLineStorageType.setStatus("mandatory")


class _ShelfCardDiagRecErrLineIndex_Type(Integer32):
    """Custom type shelfCardDiagRecErrLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ShelfCardDiagRecErrLineIndex_Type.__name__ = "Integer32"
_ShelfCardDiagRecErrLineIndex_Object = MibTableColumn
shelfCardDiagRecErrLineIndex = _ShelfCardDiagRecErrLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2, 1, 1, 10),
    _ShelfCardDiagRecErrLineIndex_Type()
)
shelfCardDiagRecErrLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardDiagRecErrLineIndex.setStatus("mandatory")
_ShelfCardDiagRecErrLineOperTable_Object = MibTable
shelfCardDiagRecErrLineOperTable = _ShelfCardDiagRecErrLineOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2, 10)
)
if mibBuilder.loadTexts:
    shelfCardDiagRecErrLineOperTable.setStatus("mandatory")
_ShelfCardDiagRecErrLineOperEntry_Object = MibTableRow
shelfCardDiagRecErrLineOperEntry = _ShelfCardDiagRecErrLineOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2, 10, 1)
)
shelfCardDiagRecErrLineOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagRecErrIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDiagRecErrLineIndex"),
)
if mibBuilder.loadTexts:
    shelfCardDiagRecErrLineOperEntry.setStatus("mandatory")


class _ShelfCardDiagRecErrLineData_Type(ExtendedAsciiString):
    """Custom type shelfCardDiagRecErrLineData based on ExtendedAsciiString"""
    subtypeSpec = ExtendedAsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ShelfCardDiagRecErrLineData_Type.__name__ = "ExtendedAsciiString"
_ShelfCardDiagRecErrLineData_Object = MibTableColumn
shelfCardDiagRecErrLineData = _ShelfCardDiagRecErrLineData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 4, 3, 2, 10, 1, 1),
    _ShelfCardDiagRecErrLineData_Type()
)
shelfCardDiagRecErrLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDiagRecErrLineData.setStatus("mandatory")
_ShelfCardProvTable_Object = MibTable
shelfCardProvTable = _ShelfCardProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 10)
)
if mibBuilder.loadTexts:
    shelfCardProvTable.setStatus("mandatory")
_ShelfCardProvEntry_Object = MibTableRow
shelfCardProvEntry = _ShelfCardProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 10, 1)
)
shelfCardProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
)
if mibBuilder.loadTexts:
    shelfCardProvEntry.setStatus("mandatory")


class _ShelfCardCardType_Type(Integer32):
    """Custom type shelfCardCardType based on Integer32"""
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
              82)
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
          ("msa32", 69),
          ("msa32mt", 70),
          ("msa32mtp", 71),
          ("msa32st", 72),
          ("msa32stp", 73),
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
          ("n1pTTC2mMvp", 47),
          ("n1pTTC2mMvpe", 68),
          ("n2pDS3cAal", 52),
          ("n2pEth100BaseT", 54),
          ("n2pJ6MAtm", 27),
          ("n2pOC3MmAtm2", 55),
          ("n2pOC3SmAtm2", 56),
          ("n32pE1Aal", 74),
          ("n3pDS1Atm", 21),
          ("n3pDS3Atm", 16),
          ("n3pDS3Atm2", 57),
          ("n3pE1Atm", 20),
          ("n3pE3Atm", 15),
          ("n3pE3Atm2", 58),
          ("n3pOC3MmAtm", 17),
          ("n3pOC3SmAtm", 19),
          ("n4pDS1Aal1", 39),
          ("n4pE1Aal1", 40),
          ("n4pEthAui", 23),
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


_ShelfCardCardType_Type.__name__ = "Integer32"
_ShelfCardCardType_Object = MibTableColumn
shelfCardCardType = _ShelfCardCardType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 10, 1, 1),
    _ShelfCardCardType_Type()
)
shelfCardCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardCardType.setStatus("mandatory")


class _ShelfCardSparingConnection_Type(Integer32):
    """Custom type shelfCardSparingConnection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("mainA", 1),
          ("mainB", 2),
          ("mainC", 3),
          ("mainD", 4),
          ("notApplicable", 0),
          ("spare", 16))
    )


_ShelfCardSparingConnection_Type.__name__ = "Integer32"
_ShelfCardSparingConnection_Object = MibTableColumn
shelfCardSparingConnection = _ShelfCardSparingConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 10, 1, 2),
    _ShelfCardSparingConnection_Type()
)
shelfCardSparingConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardSparingConnection.setStatus("mandatory")


class _ShelfCardCommentText_Type(AsciiString):
    """Custom type shelfCardCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ShelfCardCommentText_Type.__name__ = "AsciiString"
_ShelfCardCommentText_Object = MibTableColumn
shelfCardCommentText = _ShelfCardCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 10, 1, 4),
    _ShelfCardCommentText_Type()
)
shelfCardCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCardCommentText.setStatus("mandatory")
_ShelfCardStateTable_Object = MibTable
shelfCardStateTable = _ShelfCardStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11)
)
if mibBuilder.loadTexts:
    shelfCardStateTable.setStatus("mandatory")
_ShelfCardStateEntry_Object = MibTableRow
shelfCardStateEntry = _ShelfCardStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1)
)
shelfCardStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
)
if mibBuilder.loadTexts:
    shelfCardStateEntry.setStatus("mandatory")


class _ShelfCardAdminState_Type(Integer32):
    """Custom type shelfCardAdminState based on Integer32"""
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


_ShelfCardAdminState_Type.__name__ = "Integer32"
_ShelfCardAdminState_Object = MibTableColumn
shelfCardAdminState = _ShelfCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1, 1),
    _ShelfCardAdminState_Type()
)
shelfCardAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardAdminState.setStatus("mandatory")


class _ShelfCardOperationalState_Type(Integer32):
    """Custom type shelfCardOperationalState based on Integer32"""
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


_ShelfCardOperationalState_Type.__name__ = "Integer32"
_ShelfCardOperationalState_Object = MibTableColumn
shelfCardOperationalState = _ShelfCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1, 2),
    _ShelfCardOperationalState_Type()
)
shelfCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardOperationalState.setStatus("mandatory")


class _ShelfCardUsageState_Type(Integer32):
    """Custom type shelfCardUsageState based on Integer32"""
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


_ShelfCardUsageState_Type.__name__ = "Integer32"
_ShelfCardUsageState_Object = MibTableColumn
shelfCardUsageState = _ShelfCardUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1, 3),
    _ShelfCardUsageState_Type()
)
shelfCardUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardUsageState.setStatus("mandatory")


class _ShelfCardAvailabilityStatus_Type(OctetString):
    """Custom type shelfCardAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ShelfCardAvailabilityStatus_Type.__name__ = "OctetString"
_ShelfCardAvailabilityStatus_Object = MibTableColumn
shelfCardAvailabilityStatus = _ShelfCardAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1, 4),
    _ShelfCardAvailabilityStatus_Type()
)
shelfCardAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardAvailabilityStatus.setStatus("mandatory")


class _ShelfCardProceduralStatus_Type(OctetString):
    """Custom type shelfCardProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardProceduralStatus_Type.__name__ = "OctetString"
_ShelfCardProceduralStatus_Object = MibTableColumn
shelfCardProceduralStatus = _ShelfCardProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1, 5),
    _ShelfCardProceduralStatus_Type()
)
shelfCardProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardProceduralStatus.setStatus("mandatory")


class _ShelfCardControlStatus_Type(OctetString):
    """Custom type shelfCardControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardControlStatus_Type.__name__ = "OctetString"
_ShelfCardControlStatus_Object = MibTableColumn
shelfCardControlStatus = _ShelfCardControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1, 6),
    _ShelfCardControlStatus_Type()
)
shelfCardControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardControlStatus.setStatus("mandatory")


class _ShelfCardAlarmStatus_Type(OctetString):
    """Custom type shelfCardAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfCardAlarmStatus_Type.__name__ = "OctetString"
_ShelfCardAlarmStatus_Object = MibTableColumn
shelfCardAlarmStatus = _ShelfCardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1, 7),
    _ShelfCardAlarmStatus_Type()
)
shelfCardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardAlarmStatus.setStatus("mandatory")


class _ShelfCardStandbyStatus_Type(Integer32):
    """Custom type shelfCardStandbyStatus based on Integer32"""
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


_ShelfCardStandbyStatus_Type.__name__ = "Integer32"
_ShelfCardStandbyStatus_Object = MibTableColumn
shelfCardStandbyStatus = _ShelfCardStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1, 8),
    _ShelfCardStandbyStatus_Type()
)
shelfCardStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardStandbyStatus.setStatus("mandatory")


class _ShelfCardUnknownStatus_Type(Integer32):
    """Custom type shelfCardUnknownStatus based on Integer32"""
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


_ShelfCardUnknownStatus_Type.__name__ = "Integer32"
_ShelfCardUnknownStatus_Object = MibTableColumn
shelfCardUnknownStatus = _ShelfCardUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 11, 1, 9),
    _ShelfCardUnknownStatus_Type()
)
shelfCardUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardUnknownStatus.setStatus("mandatory")
_ShelfCardOperTable_Object = MibTable
shelfCardOperTable = _ShelfCardOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 12)
)
if mibBuilder.loadTexts:
    shelfCardOperTable.setStatus("mandatory")
_ShelfCardOperEntry_Object = MibTableRow
shelfCardOperEntry = _ShelfCardOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 12, 1)
)
shelfCardOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
)
if mibBuilder.loadTexts:
    shelfCardOperEntry.setStatus("mandatory")
_ShelfCardCurrentLP_Type = RowPointer
_ShelfCardCurrentLP_Object = MibTableColumn
shelfCardCurrentLP = _ShelfCardCurrentLP_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 12, 1, 1),
    _ShelfCardCurrentLP_Type()
)
shelfCardCurrentLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardCurrentLP.setStatus("obsolete")


class _ShelfCardFailureCause_Type(Integer32):
    """Custom type shelfCardFailureCause based on Integer32"""
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
        *(("busConnectivityProblem", 6),
          ("cannotLoadSoftware", 3),
          ("failedSelfTests", 4),
          ("none", 0),
          ("notConfigured", 2),
          ("notResponding", 5),
          ("wrongCardType", 1))
    )


_ShelfCardFailureCause_Type.__name__ = "Integer32"
_ShelfCardFailureCause_Object = MibTableColumn
shelfCardFailureCause = _ShelfCardFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 12, 1, 2),
    _ShelfCardFailureCause_Type()
)
shelfCardFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardFailureCause.setStatus("mandatory")


class _ShelfCardSelfTestFault_Type(Integer32):
    """Custom type shelfCardSelfTestFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_ShelfCardSelfTestFault_Type.__name__ = "Integer32"
_ShelfCardSelfTestFault_Object = MibTableColumn
shelfCardSelfTestFault = _ShelfCardSelfTestFault_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 12, 1, 3),
    _ShelfCardSelfTestFault_Type()
)
shelfCardSelfTestFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardSelfTestFault.setStatus("mandatory")


class _ShelfCardSparingConnectionStatus_Type(Integer32):
    """Custom type shelfCardSparingConnectionStatus based on Integer32"""
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


_ShelfCardSparingConnectionStatus_Type.__name__ = "Integer32"
_ShelfCardSparingConnectionStatus_Object = MibTableColumn
shelfCardSparingConnectionStatus = _ShelfCardSparingConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 12, 1, 4),
    _ShelfCardSparingConnectionStatus_Type()
)
shelfCardSparingConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardSparingConnectionStatus.setStatus("mandatory")
_ShelfCardPropTable_Object = MibTable
shelfCardPropTable = _ShelfCardPropTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 13)
)
if mibBuilder.loadTexts:
    shelfCardPropTable.setStatus("mandatory")
_ShelfCardPropEntry_Object = MibTableRow
shelfCardPropEntry = _ShelfCardPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 13, 1)
)
shelfCardPropEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
)
if mibBuilder.loadTexts:
    shelfCardPropEntry.setStatus("mandatory")


class _ShelfCardInsertedCardType_Type(Integer32):
    """Custom type shelfCardInsertedCardType based on Integer32"""
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
              82)
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
          ("msa32", 69),
          ("msa32mt", 70),
          ("msa32mtp", 71),
          ("msa32st", 72),
          ("msa32stp", 73),
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
          ("n1pTTC2mMvp", 47),
          ("n1pTTC2mMvpe", 68),
          ("n2pDS3cAal", 52),
          ("n2pEth100BaseT", 54),
          ("n2pJ6MAtm", 27),
          ("n2pOC3MmAtm2", 55),
          ("n2pOC3SmAtm2", 56),
          ("n32pE1Aal", 74),
          ("n3pDS1Atm", 21),
          ("n3pDS3Atm", 16),
          ("n3pDS3Atm2", 57),
          ("n3pE1Atm", 20),
          ("n3pE3Atm", 15),
          ("n3pE3Atm2", 58),
          ("n3pOC3MmAtm", 17),
          ("n3pOC3SmAtm", 19),
          ("n4pDS1Aal1", 39),
          ("n4pE1Aal1", 40),
          ("n4pEthAui", 23),
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


_ShelfCardInsertedCardType_Type.__name__ = "Integer32"
_ShelfCardInsertedCardType_Object = MibTableColumn
shelfCardInsertedCardType = _ShelfCardInsertedCardType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 13, 1, 1),
    _ShelfCardInsertedCardType_Type()
)
shelfCardInsertedCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardInsertedCardType.setStatus("mandatory")


class _ShelfCardPmRevisionCode_Type(AsciiString):
    """Custom type shelfCardPmRevisionCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ShelfCardPmRevisionCode_Type.__name__ = "AsciiString"
_ShelfCardPmRevisionCode_Object = MibTableColumn
shelfCardPmRevisionCode = _ShelfCardPmRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 13, 1, 2),
    _ShelfCardPmRevisionCode_Type()
)
shelfCardPmRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardPmRevisionCode.setStatus("mandatory")


class _ShelfCardImRevisionCode_Type(AsciiString):
    """Custom type shelfCardImRevisionCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ShelfCardImRevisionCode_Type.__name__ = "AsciiString"
_ShelfCardImRevisionCode_Object = MibTableColumn
shelfCardImRevisionCode = _ShelfCardImRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 13, 1, 3),
    _ShelfCardImRevisionCode_Type()
)
shelfCardImRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardImRevisionCode.setStatus("mandatory")


class _ShelfCardSerialNumber_Type(AsciiString):
    """Custom type shelfCardSerialNumber based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ShelfCardSerialNumber_Type.__name__ = "AsciiString"
_ShelfCardSerialNumber_Object = MibTableColumn
shelfCardSerialNumber = _ShelfCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 13, 1, 4),
    _ShelfCardSerialNumber_Type()
)
shelfCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardSerialNumber.setStatus("mandatory")


class _ShelfCardActiveFirmwareVersion_Type(AsciiString):
    """Custom type shelfCardActiveFirmwareVersion based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ShelfCardActiveFirmwareVersion_Type.__name__ = "AsciiString"
_ShelfCardActiveFirmwareVersion_Object = MibTableColumn
shelfCardActiveFirmwareVersion = _ShelfCardActiveFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 13, 1, 5),
    _ShelfCardActiveFirmwareVersion_Type()
)
shelfCardActiveFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardActiveFirmwareVersion.setStatus("mandatory")


class _ShelfCardInactiveFirmwareVersion_Type(AsciiString):
    """Custom type shelfCardInactiveFirmwareVersion based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ShelfCardInactiveFirmwareVersion_Type.__name__ = "AsciiString"
_ShelfCardInactiveFirmwareVersion_Object = MibTableColumn
shelfCardInactiveFirmwareVersion = _ShelfCardInactiveFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 13, 1, 6),
    _ShelfCardInactiveFirmwareVersion_Type()
)
shelfCardInactiveFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardInactiveFirmwareVersion.setStatus("mandatory")


class _ShelfCardProductCode_Type(AsciiString):
    """Custom type shelfCardProductCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ShelfCardProductCode_Type.__name__ = "AsciiString"
_ShelfCardProductCode_Object = MibTableColumn
shelfCardProductCode = _ShelfCardProductCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 13, 1, 7),
    _ShelfCardProductCode_Type()
)
shelfCardProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardProductCode.setStatus("mandatory")
_ShelfCardUtilTable_Object = MibTable
shelfCardUtilTable = _ShelfCardUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14)
)
if mibBuilder.loadTexts:
    shelfCardUtilTable.setStatus("mandatory")
_ShelfCardUtilEntry_Object = MibTableRow
shelfCardUtilEntry = _ShelfCardUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1)
)
shelfCardUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
)
if mibBuilder.loadTexts:
    shelfCardUtilEntry.setStatus("mandatory")


class _ShelfCardTimeInterval_Type(Unsigned32):
    """Custom type shelfCardTimeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfCardTimeInterval_Type.__name__ = "Unsigned32"
_ShelfCardTimeInterval_Object = MibTableColumn
shelfCardTimeInterval = _ShelfCardTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 1),
    _ShelfCardTimeInterval_Type()
)
shelfCardTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardTimeInterval.setStatus("mandatory")


class _ShelfCardCpuUtil_Type(Gauge32):
    """Custom type shelfCardCpuUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ShelfCardCpuUtil_Type.__name__ = "Gauge32"
_ShelfCardCpuUtil_Object = MibTableColumn
shelfCardCpuUtil = _ShelfCardCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 2),
    _ShelfCardCpuUtil_Type()
)
shelfCardCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardCpuUtil.setStatus("mandatory")


class _ShelfCardCpuUtilAvg_Type(Gauge32):
    """Custom type shelfCardCpuUtilAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ShelfCardCpuUtilAvg_Type.__name__ = "Gauge32"
_ShelfCardCpuUtilAvg_Object = MibTableColumn
shelfCardCpuUtilAvg = _ShelfCardCpuUtilAvg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 3),
    _ShelfCardCpuUtilAvg_Type()
)
shelfCardCpuUtilAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardCpuUtilAvg.setStatus("mandatory")


class _ShelfCardCpuUtilAvgMin_Type(Gauge32):
    """Custom type shelfCardCpuUtilAvgMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ShelfCardCpuUtilAvgMin_Type.__name__ = "Gauge32"
_ShelfCardCpuUtilAvgMin_Object = MibTableColumn
shelfCardCpuUtilAvgMin = _ShelfCardCpuUtilAvgMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 4),
    _ShelfCardCpuUtilAvgMin_Type()
)
shelfCardCpuUtilAvgMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardCpuUtilAvgMin.setStatus("mandatory")


class _ShelfCardCpuUtilAvgMax_Type(Gauge32):
    """Custom type shelfCardCpuUtilAvgMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ShelfCardCpuUtilAvgMax_Type.__name__ = "Gauge32"
_ShelfCardCpuUtilAvgMax_Object = MibTableColumn
shelfCardCpuUtilAvgMax = _ShelfCardCpuUtilAvgMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 5),
    _ShelfCardCpuUtilAvgMax_Type()
)
shelfCardCpuUtilAvgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardCpuUtilAvgMax.setStatus("mandatory")


class _ShelfCardMsgBlockUsage_Type(Gauge32):
    """Custom type shelfCardMsgBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMsgBlockUsage_Type.__name__ = "Gauge32"
_ShelfCardMsgBlockUsage_Object = MibTableColumn
shelfCardMsgBlockUsage = _ShelfCardMsgBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 6),
    _ShelfCardMsgBlockUsage_Type()
)
shelfCardMsgBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMsgBlockUsage.setStatus("mandatory")


class _ShelfCardMsgBlockUsageAvg_Type(Gauge32):
    """Custom type shelfCardMsgBlockUsageAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMsgBlockUsageAvg_Type.__name__ = "Gauge32"
_ShelfCardMsgBlockUsageAvg_Object = MibTableColumn
shelfCardMsgBlockUsageAvg = _ShelfCardMsgBlockUsageAvg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 7),
    _ShelfCardMsgBlockUsageAvg_Type()
)
shelfCardMsgBlockUsageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMsgBlockUsageAvg.setStatus("mandatory")


class _ShelfCardMsgBlockUsageAvgMin_Type(Gauge32):
    """Custom type shelfCardMsgBlockUsageAvgMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMsgBlockUsageAvgMin_Type.__name__ = "Gauge32"
_ShelfCardMsgBlockUsageAvgMin_Object = MibTableColumn
shelfCardMsgBlockUsageAvgMin = _ShelfCardMsgBlockUsageAvgMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 8),
    _ShelfCardMsgBlockUsageAvgMin_Type()
)
shelfCardMsgBlockUsageAvgMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMsgBlockUsageAvgMin.setStatus("mandatory")


class _ShelfCardMsgBlockUsageAvgMax_Type(Gauge32):
    """Custom type shelfCardMsgBlockUsageAvgMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMsgBlockUsageAvgMax_Type.__name__ = "Gauge32"
_ShelfCardMsgBlockUsageAvgMax_Object = MibTableColumn
shelfCardMsgBlockUsageAvgMax = _ShelfCardMsgBlockUsageAvgMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 9),
    _ShelfCardMsgBlockUsageAvgMax_Type()
)
shelfCardMsgBlockUsageAvgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMsgBlockUsageAvgMax.setStatus("mandatory")


class _ShelfCardLocalMsgBlockUsage_Type(Gauge32):
    """Custom type shelfCardLocalMsgBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardLocalMsgBlockUsage_Type.__name__ = "Gauge32"
_ShelfCardLocalMsgBlockUsage_Object = MibTableColumn
shelfCardLocalMsgBlockUsage = _ShelfCardLocalMsgBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 10),
    _ShelfCardLocalMsgBlockUsage_Type()
)
shelfCardLocalMsgBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardLocalMsgBlockUsage.setStatus("mandatory")


class _ShelfCardLocalMsgBlockUsageAvg_Type(Gauge32):
    """Custom type shelfCardLocalMsgBlockUsageAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardLocalMsgBlockUsageAvg_Type.__name__ = "Gauge32"
_ShelfCardLocalMsgBlockUsageAvg_Object = MibTableColumn
shelfCardLocalMsgBlockUsageAvg = _ShelfCardLocalMsgBlockUsageAvg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 11),
    _ShelfCardLocalMsgBlockUsageAvg_Type()
)
shelfCardLocalMsgBlockUsageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardLocalMsgBlockUsageAvg.setStatus("mandatory")


class _ShelfCardLocalMsgBlockUsageMin_Type(Gauge32):
    """Custom type shelfCardLocalMsgBlockUsageMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardLocalMsgBlockUsageMin_Type.__name__ = "Gauge32"
_ShelfCardLocalMsgBlockUsageMin_Object = MibTableColumn
shelfCardLocalMsgBlockUsageMin = _ShelfCardLocalMsgBlockUsageMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 12),
    _ShelfCardLocalMsgBlockUsageMin_Type()
)
shelfCardLocalMsgBlockUsageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardLocalMsgBlockUsageMin.setStatus("mandatory")


class _ShelfCardLocalMsgBlockUsageMax_Type(Gauge32):
    """Custom type shelfCardLocalMsgBlockUsageMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardLocalMsgBlockUsageMax_Type.__name__ = "Gauge32"
_ShelfCardLocalMsgBlockUsageMax_Object = MibTableColumn
shelfCardLocalMsgBlockUsageMax = _ShelfCardLocalMsgBlockUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 14, 1, 13),
    _ShelfCardLocalMsgBlockUsageMax_Type()
)
shelfCardLocalMsgBlockUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardLocalMsgBlockUsageMax.setStatus("mandatory")
_ShelfCardCapTable_Object = MibTable
shelfCardCapTable = _ShelfCardCapTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 15)
)
if mibBuilder.loadTexts:
    shelfCardCapTable.setStatus("mandatory")
_ShelfCardCapEntry_Object = MibTableRow
shelfCardCapEntry = _ShelfCardCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 15, 1)
)
shelfCardCapEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
)
if mibBuilder.loadTexts:
    shelfCardCapEntry.setStatus("mandatory")


class _ShelfCardMsgBlockCapacity_Type(Unsigned32):
    """Custom type shelfCardMsgBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMsgBlockCapacity_Type.__name__ = "Unsigned32"
_ShelfCardMsgBlockCapacity_Object = MibTableColumn
shelfCardMsgBlockCapacity = _ShelfCardMsgBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 15, 1, 1),
    _ShelfCardMsgBlockCapacity_Type()
)
shelfCardMsgBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMsgBlockCapacity.setStatus("mandatory")


class _ShelfCardLocalMsgBlockCapacity_Type(Unsigned32):
    """Custom type shelfCardLocalMsgBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardLocalMsgBlockCapacity_Type.__name__ = "Unsigned32"
_ShelfCardLocalMsgBlockCapacity_Object = MibTableColumn
shelfCardLocalMsgBlockCapacity = _ShelfCardLocalMsgBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 15, 1, 2),
    _ShelfCardLocalMsgBlockCapacity_Type()
)
shelfCardLocalMsgBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardLocalMsgBlockCapacity.setStatus("mandatory")
_ShelfCardDcard_ObjectIdentity = ObjectIdentity
shelfCardDcard = _ShelfCardDcard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16)
)
_ShelfCardDcardRowStatusTable_Object = MibTable
shelfCardDcardRowStatusTable = _ShelfCardDcardRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 1)
)
if mibBuilder.loadTexts:
    shelfCardDcardRowStatusTable.setStatus("mandatory")
_ShelfCardDcardRowStatusEntry_Object = MibTableRow
shelfCardDcardRowStatusEntry = _ShelfCardDcardRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 1, 1)
)
shelfCardDcardRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDcardIndex"),
)
if mibBuilder.loadTexts:
    shelfCardDcardRowStatusEntry.setStatus("mandatory")
_ShelfCardDcardRowStatus_Type = RowStatus
_ShelfCardDcardRowStatus_Object = MibTableColumn
shelfCardDcardRowStatus = _ShelfCardDcardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 1, 1, 1),
    _ShelfCardDcardRowStatus_Type()
)
shelfCardDcardRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDcardRowStatus.setStatus("mandatory")
_ShelfCardDcardComponentName_Type = DisplayString
_ShelfCardDcardComponentName_Object = MibTableColumn
shelfCardDcardComponentName = _ShelfCardDcardComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 1, 1, 2),
    _ShelfCardDcardComponentName_Type()
)
shelfCardDcardComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDcardComponentName.setStatus("mandatory")
_ShelfCardDcardStorageType_Type = StorageType
_ShelfCardDcardStorageType_Object = MibTableColumn
shelfCardDcardStorageType = _ShelfCardDcardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 1, 1, 4),
    _ShelfCardDcardStorageType_Type()
)
shelfCardDcardStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDcardStorageType.setStatus("mandatory")


class _ShelfCardDcardIndex_Type(Integer32):
    """Custom type shelfCardDcardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ShelfCardDcardIndex_Type.__name__ = "Integer32"
_ShelfCardDcardIndex_Object = MibTableColumn
shelfCardDcardIndex = _ShelfCardDcardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 1, 1, 10),
    _ShelfCardDcardIndex_Type()
)
shelfCardDcardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardDcardIndex.setStatus("mandatory")
_ShelfCardDcardDcardOperTable_Object = MibTable
shelfCardDcardDcardOperTable = _ShelfCardDcardDcardOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 17)
)
if mibBuilder.loadTexts:
    shelfCardDcardDcardOperTable.setStatus("mandatory")
_ShelfCardDcardDcardOperEntry_Object = MibTableRow
shelfCardDcardDcardOperEntry = _ShelfCardDcardDcardOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 17, 1)
)
shelfCardDcardDcardOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardDcardIndex"),
)
if mibBuilder.loadTexts:
    shelfCardDcardDcardOperEntry.setStatus("mandatory")


class _ShelfCardDcardType_Type(Integer32):
    """Custom type shelfCardDcardType based on Integer32"""
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
        *(("aqm", 2),
          ("pqc", 3),
          ("ram", 1),
          ("unknown", 0))
    )


_ShelfCardDcardType_Type.__name__ = "Integer32"
_ShelfCardDcardType_Object = MibTableColumn
shelfCardDcardType = _ShelfCardDcardType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 17, 1, 1),
    _ShelfCardDcardType_Type()
)
shelfCardDcardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDcardType.setStatus("mandatory")


class _ShelfCardDcardMemorySize_Type(Unsigned32):
    """Custom type shelfCardDcardMemorySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardDcardMemorySize_Type.__name__ = "Unsigned32"
_ShelfCardDcardMemorySize_Object = MibTableColumn
shelfCardDcardMemorySize = _ShelfCardDcardMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 17, 1, 2),
    _ShelfCardDcardMemorySize_Type()
)
shelfCardDcardMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDcardMemorySize.setStatus("mandatory")


class _ShelfCardDcardProductCode_Type(AsciiString):
    """Custom type shelfCardDcardProductCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ShelfCardDcardProductCode_Type.__name__ = "AsciiString"
_ShelfCardDcardProductCode_Object = MibTableColumn
shelfCardDcardProductCode = _ShelfCardDcardProductCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 16, 17, 1, 3),
    _ShelfCardDcardProductCode_Type()
)
shelfCardDcardProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardDcardProductCode.setStatus("mandatory")
_ShelfCardConfiguredLPsTable_Object = MibTable
shelfCardConfiguredLPsTable = _ShelfCardConfiguredLPsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 243)
)
if mibBuilder.loadTexts:
    shelfCardConfiguredLPsTable.setStatus("mandatory")
_ShelfCardConfiguredLPsEntry_Object = MibTableRow
shelfCardConfiguredLPsEntry = _ShelfCardConfiguredLPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 243, 1)
)
shelfCardConfiguredLPsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardConfiguredLPsValue"),
)
if mibBuilder.loadTexts:
    shelfCardConfiguredLPsEntry.setStatus("mandatory")
_ShelfCardConfiguredLPsValue_Type = Link
_ShelfCardConfiguredLPsValue_Object = MibTableColumn
shelfCardConfiguredLPsValue = _ShelfCardConfiguredLPsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 243, 1, 1),
    _ShelfCardConfiguredLPsValue_Type()
)
shelfCardConfiguredLPsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardConfiguredLPsValue.setStatus("mandatory")
_ShelfCardMemoryCapacityTable_Object = MibTable
shelfCardMemoryCapacityTable = _ShelfCardMemoryCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 244)
)
if mibBuilder.loadTexts:
    shelfCardMemoryCapacityTable.setStatus("mandatory")
_ShelfCardMemoryCapacityEntry_Object = MibTableRow
shelfCardMemoryCapacityEntry = _ShelfCardMemoryCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 244, 1)
)
shelfCardMemoryCapacityEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardMemoryCapacityIndex"),
)
if mibBuilder.loadTexts:
    shelfCardMemoryCapacityEntry.setStatus("mandatory")


class _ShelfCardMemoryCapacityIndex_Type(Integer32):
    """Custom type shelfCardMemoryCapacityIndex based on Integer32"""
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


_ShelfCardMemoryCapacityIndex_Type.__name__ = "Integer32"
_ShelfCardMemoryCapacityIndex_Object = MibTableColumn
shelfCardMemoryCapacityIndex = _ShelfCardMemoryCapacityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 244, 1, 1),
    _ShelfCardMemoryCapacityIndex_Type()
)
shelfCardMemoryCapacityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardMemoryCapacityIndex.setStatus("mandatory")


class _ShelfCardMemoryCapacityValue_Type(Unsigned32):
    """Custom type shelfCardMemoryCapacityValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMemoryCapacityValue_Type.__name__ = "Unsigned32"
_ShelfCardMemoryCapacityValue_Object = MibTableColumn
shelfCardMemoryCapacityValue = _ShelfCardMemoryCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 244, 1, 2),
    _ShelfCardMemoryCapacityValue_Type()
)
shelfCardMemoryCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMemoryCapacityValue.setStatus("mandatory")
_ShelfCardMemoryUsageTable_Object = MibTable
shelfCardMemoryUsageTable = _ShelfCardMemoryUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 245)
)
if mibBuilder.loadTexts:
    shelfCardMemoryUsageTable.setStatus("mandatory")
_ShelfCardMemoryUsageEntry_Object = MibTableRow
shelfCardMemoryUsageEntry = _ShelfCardMemoryUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 245, 1)
)
shelfCardMemoryUsageEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardMemoryUsageIndex"),
)
if mibBuilder.loadTexts:
    shelfCardMemoryUsageEntry.setStatus("mandatory")


class _ShelfCardMemoryUsageIndex_Type(Integer32):
    """Custom type shelfCardMemoryUsageIndex based on Integer32"""
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


_ShelfCardMemoryUsageIndex_Type.__name__ = "Integer32"
_ShelfCardMemoryUsageIndex_Object = MibTableColumn
shelfCardMemoryUsageIndex = _ShelfCardMemoryUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 245, 1, 1),
    _ShelfCardMemoryUsageIndex_Type()
)
shelfCardMemoryUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardMemoryUsageIndex.setStatus("mandatory")


class _ShelfCardMemoryUsageValue_Type(Gauge32):
    """Custom type shelfCardMemoryUsageValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMemoryUsageValue_Type.__name__ = "Gauge32"
_ShelfCardMemoryUsageValue_Object = MibTableColumn
shelfCardMemoryUsageValue = _ShelfCardMemoryUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 245, 1, 2),
    _ShelfCardMemoryUsageValue_Type()
)
shelfCardMemoryUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMemoryUsageValue.setStatus("mandatory")
_ShelfCardMemoryUsageAvgTable_Object = MibTable
shelfCardMemoryUsageAvgTable = _ShelfCardMemoryUsageAvgTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 276)
)
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgTable.setStatus("mandatory")
_ShelfCardMemoryUsageAvgEntry_Object = MibTableRow
shelfCardMemoryUsageAvgEntry = _ShelfCardMemoryUsageAvgEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 276, 1)
)
shelfCardMemoryUsageAvgEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardMemoryUsageAvgIndex"),
)
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgEntry.setStatus("mandatory")


class _ShelfCardMemoryUsageAvgIndex_Type(Integer32):
    """Custom type shelfCardMemoryUsageAvgIndex based on Integer32"""
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


_ShelfCardMemoryUsageAvgIndex_Type.__name__ = "Integer32"
_ShelfCardMemoryUsageAvgIndex_Object = MibTableColumn
shelfCardMemoryUsageAvgIndex = _ShelfCardMemoryUsageAvgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 276, 1, 1),
    _ShelfCardMemoryUsageAvgIndex_Type()
)
shelfCardMemoryUsageAvgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgIndex.setStatus("mandatory")


class _ShelfCardMemoryUsageAvgValue_Type(Gauge32):
    """Custom type shelfCardMemoryUsageAvgValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMemoryUsageAvgValue_Type.__name__ = "Gauge32"
_ShelfCardMemoryUsageAvgValue_Object = MibTableColumn
shelfCardMemoryUsageAvgValue = _ShelfCardMemoryUsageAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 276, 1, 2),
    _ShelfCardMemoryUsageAvgValue_Type()
)
shelfCardMemoryUsageAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgValue.setStatus("mandatory")
_ShelfCardMemoryUsageAvgMinTable_Object = MibTable
shelfCardMemoryUsageAvgMinTable = _ShelfCardMemoryUsageAvgMinTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 277)
)
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgMinTable.setStatus("mandatory")
_ShelfCardMemoryUsageAvgMinEntry_Object = MibTableRow
shelfCardMemoryUsageAvgMinEntry = _ShelfCardMemoryUsageAvgMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 277, 1)
)
shelfCardMemoryUsageAvgMinEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardMemoryUsageAvgMinIndex"),
)
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgMinEntry.setStatus("mandatory")


class _ShelfCardMemoryUsageAvgMinIndex_Type(Integer32):
    """Custom type shelfCardMemoryUsageAvgMinIndex based on Integer32"""
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


_ShelfCardMemoryUsageAvgMinIndex_Type.__name__ = "Integer32"
_ShelfCardMemoryUsageAvgMinIndex_Object = MibTableColumn
shelfCardMemoryUsageAvgMinIndex = _ShelfCardMemoryUsageAvgMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 277, 1, 1),
    _ShelfCardMemoryUsageAvgMinIndex_Type()
)
shelfCardMemoryUsageAvgMinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgMinIndex.setStatus("mandatory")


class _ShelfCardMemoryUsageAvgMinValue_Type(Gauge32):
    """Custom type shelfCardMemoryUsageAvgMinValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMemoryUsageAvgMinValue_Type.__name__ = "Gauge32"
_ShelfCardMemoryUsageAvgMinValue_Object = MibTableColumn
shelfCardMemoryUsageAvgMinValue = _ShelfCardMemoryUsageAvgMinValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 277, 1, 2),
    _ShelfCardMemoryUsageAvgMinValue_Type()
)
shelfCardMemoryUsageAvgMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgMinValue.setStatus("mandatory")
_ShelfCardMemoryUsageAvgMaxTable_Object = MibTable
shelfCardMemoryUsageAvgMaxTable = _ShelfCardMemoryUsageAvgMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 278)
)
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgMaxTable.setStatus("mandatory")
_ShelfCardMemoryUsageAvgMaxEntry_Object = MibTableRow
shelfCardMemoryUsageAvgMaxEntry = _ShelfCardMemoryUsageAvgMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 278, 1)
)
shelfCardMemoryUsageAvgMaxEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardMemoryUsageAvgMaxIndex"),
)
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgMaxEntry.setStatus("mandatory")


class _ShelfCardMemoryUsageAvgMaxIndex_Type(Integer32):
    """Custom type shelfCardMemoryUsageAvgMaxIndex based on Integer32"""
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


_ShelfCardMemoryUsageAvgMaxIndex_Type.__name__ = "Integer32"
_ShelfCardMemoryUsageAvgMaxIndex_Object = MibTableColumn
shelfCardMemoryUsageAvgMaxIndex = _ShelfCardMemoryUsageAvgMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 278, 1, 1),
    _ShelfCardMemoryUsageAvgMaxIndex_Type()
)
shelfCardMemoryUsageAvgMaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgMaxIndex.setStatus("mandatory")


class _ShelfCardMemoryUsageAvgMaxValue_Type(Gauge32):
    """Custom type shelfCardMemoryUsageAvgMaxValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ShelfCardMemoryUsageAvgMaxValue_Type.__name__ = "Gauge32"
_ShelfCardMemoryUsageAvgMaxValue_Object = MibTableColumn
shelfCardMemoryUsageAvgMaxValue = _ShelfCardMemoryUsageAvgMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 278, 1, 2),
    _ShelfCardMemoryUsageAvgMaxValue_Type()
)
shelfCardMemoryUsageAvgMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardMemoryUsageAvgMaxValue.setStatus("mandatory")
_ShelfCardCurrentLpTable_Object = MibTable
shelfCardCurrentLpTable = _ShelfCardCurrentLpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 406)
)
if mibBuilder.loadTexts:
    shelfCardCurrentLpTable.setStatus("mandatory")
_ShelfCardCurrentLpEntry_Object = MibTableRow
shelfCardCurrentLpEntry = _ShelfCardCurrentLpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 406, 1)
)
shelfCardCurrentLpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfCardCurrentLpValue"),
)
if mibBuilder.loadTexts:
    shelfCardCurrentLpEntry.setStatus("mandatory")
_ShelfCardCurrentLpValue_Type = RowPointer
_ShelfCardCurrentLpValue_Object = MibTableColumn
shelfCardCurrentLpValue = _ShelfCardCurrentLpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 2, 406, 1, 1),
    _ShelfCardCurrentLpValue_Type()
)
shelfCardCurrentLpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfCardCurrentLpValue.setStatus("mandatory")
_ShelfBus_ObjectIdentity = ObjectIdentity
shelfBus = _ShelfBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3)
)
_ShelfBusRowStatusTable_Object = MibTable
shelfBusRowStatusTable = _ShelfBusRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    shelfBusRowStatusTable.setStatus("mandatory")
_ShelfBusRowStatusEntry_Object = MibTableRow
shelfBusRowStatusEntry = _ShelfBusRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 1, 1)
)
shelfBusRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
)
if mibBuilder.loadTexts:
    shelfBusRowStatusEntry.setStatus("mandatory")
_ShelfBusRowStatus_Type = RowStatus
_ShelfBusRowStatus_Object = MibTableColumn
shelfBusRowStatus = _ShelfBusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 1, 1, 1),
    _ShelfBusRowStatus_Type()
)
shelfBusRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusRowStatus.setStatus("mandatory")
_ShelfBusComponentName_Type = DisplayString
_ShelfBusComponentName_Object = MibTableColumn
shelfBusComponentName = _ShelfBusComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 1, 1, 2),
    _ShelfBusComponentName_Type()
)
shelfBusComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusComponentName.setStatus("mandatory")
_ShelfBusStorageType_Type = StorageType
_ShelfBusStorageType_Object = MibTableColumn
shelfBusStorageType = _ShelfBusStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 1, 1, 4),
    _ShelfBusStorageType_Type()
)
shelfBusStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusStorageType.setStatus("mandatory")


class _ShelfBusIndex_Type(Integer32):
    """Custom type shelfBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("x", 0),
          ("y", 1))
    )


_ShelfBusIndex_Type.__name__ = "Integer32"
_ShelfBusIndex_Object = MibTableColumn
shelfBusIndex = _ShelfBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 1, 1, 10),
    _ShelfBusIndex_Type()
)
shelfBusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusIndex.setStatus("mandatory")
_ShelfBusTest_ObjectIdentity = ObjectIdentity
shelfBusTest = _ShelfBusTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2)
)
_ShelfBusTestRowStatusTable_Object = MibTable
shelfBusTestRowStatusTable = _ShelfBusTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 1)
)
if mibBuilder.loadTexts:
    shelfBusTestRowStatusTable.setStatus("mandatory")
_ShelfBusTestRowStatusEntry_Object = MibTableRow
shelfBusTestRowStatusEntry = _ShelfBusTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 1, 1)
)
shelfBusTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestIndex"),
)
if mibBuilder.loadTexts:
    shelfBusTestRowStatusEntry.setStatus("mandatory")
_ShelfBusTestRowStatus_Type = RowStatus
_ShelfBusTestRowStatus_Object = MibTableColumn
shelfBusTestRowStatus = _ShelfBusTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 1, 1, 1),
    _ShelfBusTestRowStatus_Type()
)
shelfBusTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestRowStatus.setStatus("mandatory")
_ShelfBusTestComponentName_Type = DisplayString
_ShelfBusTestComponentName_Object = MibTableColumn
shelfBusTestComponentName = _ShelfBusTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 1, 1, 2),
    _ShelfBusTestComponentName_Type()
)
shelfBusTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestComponentName.setStatus("mandatory")
_ShelfBusTestStorageType_Type = StorageType
_ShelfBusTestStorageType_Object = MibTableColumn
shelfBusTestStorageType = _ShelfBusTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 1, 1, 4),
    _ShelfBusTestStorageType_Type()
)
shelfBusTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestStorageType.setStatus("mandatory")
_ShelfBusTestIndex_Type = NonReplicated
_ShelfBusTestIndex_Object = MibTableColumn
shelfBusTestIndex = _ShelfBusTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 1, 1, 10),
    _ShelfBusTestIndex_Type()
)
shelfBusTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestIndex.setStatus("mandatory")
_ShelfBusTestStateTable_Object = MibTable
shelfBusTestStateTable = _ShelfBusTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 10)
)
if mibBuilder.loadTexts:
    shelfBusTestStateTable.setStatus("mandatory")
_ShelfBusTestStateEntry_Object = MibTableRow
shelfBusTestStateEntry = _ShelfBusTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 10, 1)
)
shelfBusTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestIndex"),
)
if mibBuilder.loadTexts:
    shelfBusTestStateEntry.setStatus("mandatory")


class _ShelfBusTestAdminState_Type(Integer32):
    """Custom type shelfBusTestAdminState based on Integer32"""
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


_ShelfBusTestAdminState_Type.__name__ = "Integer32"
_ShelfBusTestAdminState_Object = MibTableColumn
shelfBusTestAdminState = _ShelfBusTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 10, 1, 1),
    _ShelfBusTestAdminState_Type()
)
shelfBusTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestAdminState.setStatus("mandatory")


class _ShelfBusTestOperationalState_Type(Integer32):
    """Custom type shelfBusTestOperationalState based on Integer32"""
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


_ShelfBusTestOperationalState_Type.__name__ = "Integer32"
_ShelfBusTestOperationalState_Object = MibTableColumn
shelfBusTestOperationalState = _ShelfBusTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 10, 1, 2),
    _ShelfBusTestOperationalState_Type()
)
shelfBusTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestOperationalState.setStatus("mandatory")


class _ShelfBusTestUsageState_Type(Integer32):
    """Custom type shelfBusTestUsageState based on Integer32"""
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


_ShelfBusTestUsageState_Type.__name__ = "Integer32"
_ShelfBusTestUsageState_Object = MibTableColumn
shelfBusTestUsageState = _ShelfBusTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 10, 1, 3),
    _ShelfBusTestUsageState_Type()
)
shelfBusTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestUsageState.setStatus("mandatory")
_ShelfBusTestSetupTable_Object = MibTable
shelfBusTestSetupTable = _ShelfBusTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 11)
)
if mibBuilder.loadTexts:
    shelfBusTestSetupTable.setStatus("mandatory")
_ShelfBusTestSetupEntry_Object = MibTableRow
shelfBusTestSetupEntry = _ShelfBusTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 11, 1)
)
shelfBusTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestIndex"),
)
if mibBuilder.loadTexts:
    shelfBusTestSetupEntry.setStatus("mandatory")


class _ShelfBusTestDuration_Type(Unsigned32):
    """Custom type shelfBusTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 43200),
    )


_ShelfBusTestDuration_Type.__name__ = "Unsigned32"
_ShelfBusTestDuration_Object = MibTableColumn
shelfBusTestDuration = _ShelfBusTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 11, 1, 1),
    _ShelfBusTestDuration_Type()
)
shelfBusTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfBusTestDuration.setStatus("mandatory")
_ShelfBusTestResultsTable_Object = MibTable
shelfBusTestResultsTable = _ShelfBusTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 12)
)
if mibBuilder.loadTexts:
    shelfBusTestResultsTable.setStatus("mandatory")
_ShelfBusTestResultsEntry_Object = MibTableRow
shelfBusTestResultsEntry = _ShelfBusTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 12, 1)
)
shelfBusTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestIndex"),
)
if mibBuilder.loadTexts:
    shelfBusTestResultsEntry.setStatus("mandatory")


class _ShelfBusTestElapsedTime_Type(Unsigned32):
    """Custom type shelfBusTestElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_ShelfBusTestElapsedTime_Type.__name__ = "Unsigned32"
_ShelfBusTestElapsedTime_Object = MibTableColumn
shelfBusTestElapsedTime = _ShelfBusTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 12, 1, 1),
    _ShelfBusTestElapsedTime_Type()
)
shelfBusTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestElapsedTime.setStatus("mandatory")


class _ShelfBusTestTimeRemaining_Type(Unsigned32):
    """Custom type shelfBusTestTimeRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_ShelfBusTestTimeRemaining_Type.__name__ = "Unsigned32"
_ShelfBusTestTimeRemaining_Object = MibTableColumn
shelfBusTestTimeRemaining = _ShelfBusTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 12, 1, 2),
    _ShelfBusTestTimeRemaining_Type()
)
shelfBusTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestTimeRemaining.setStatus("mandatory")


class _ShelfBusTestCauseOfTermination_Type(Integer32):
    """Custom type shelfBusTestCauseOfTermination based on Integer32"""
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
        *(("broadcastFailure", 6),
          ("clockSourceFailure", 5),
          ("neverStarted", 0),
          ("selfTestFailure", 4),
          ("stoppedByOperator", 3),
          ("testRunning", 1),
          ("testTimeExpired", 2))
    )


_ShelfBusTestCauseOfTermination_Type.__name__ = "Integer32"
_ShelfBusTestCauseOfTermination_Object = MibTableColumn
shelfBusTestCauseOfTermination = _ShelfBusTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 12, 1, 3),
    _ShelfBusTestCauseOfTermination_Type()
)
shelfBusTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestCauseOfTermination.setStatus("mandatory")


class _ShelfBusTestTestsDone_Type(OctetString):
    """Custom type shelfBusTestTestsDone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfBusTestTestsDone_Type.__name__ = "OctetString"
_ShelfBusTestTestsDone_Object = MibTableColumn
shelfBusTestTestsDone = _ShelfBusTestTestsDone_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 12, 1, 4),
    _ShelfBusTestTestsDone_Type()
)
shelfBusTestTestsDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestTestsDone.setStatus("mandatory")
_ShelfBusTestSelfTestResultsTable_Object = MibTable
shelfBusTestSelfTestResultsTable = _ShelfBusTestSelfTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 248)
)
if mibBuilder.loadTexts:
    shelfBusTestSelfTestResultsTable.setStatus("mandatory")
_ShelfBusTestSelfTestResultsEntry_Object = MibTableRow
shelfBusTestSelfTestResultsEntry = _ShelfBusTestSelfTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 248, 1)
)
shelfBusTestSelfTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestSelfTestResultsIndex"),
)
if mibBuilder.loadTexts:
    shelfBusTestSelfTestResultsEntry.setStatus("mandatory")


class _ShelfBusTestSelfTestResultsIndex_Type(Integer32):
    """Custom type shelfBusTestSelfTestResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfBusTestSelfTestResultsIndex_Type.__name__ = "Integer32"
_ShelfBusTestSelfTestResultsIndex_Object = MibTableColumn
shelfBusTestSelfTestResultsIndex = _ShelfBusTestSelfTestResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 248, 1, 1),
    _ShelfBusTestSelfTestResultsIndex_Type()
)
shelfBusTestSelfTestResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestSelfTestResultsIndex.setStatus("mandatory")


class _ShelfBusTestSelfTestResultsValue_Type(Integer32):
    """Custom type shelfBusTestSelfTestResultsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n1", 1),
          ("n2", 2),
          ("x", 0))
    )


_ShelfBusTestSelfTestResultsValue_Type.__name__ = "Integer32"
_ShelfBusTestSelfTestResultsValue_Object = MibTableColumn
shelfBusTestSelfTestResultsValue = _ShelfBusTestSelfTestResultsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 248, 1, 2),
    _ShelfBusTestSelfTestResultsValue_Type()
)
shelfBusTestSelfTestResultsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestSelfTestResultsValue.setStatus("mandatory")
_ShelfBusTestClockSourceTestResultsTable_Object = MibTable
shelfBusTestClockSourceTestResultsTable = _ShelfBusTestClockSourceTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 249)
)
if mibBuilder.loadTexts:
    shelfBusTestClockSourceTestResultsTable.setStatus("mandatory")
_ShelfBusTestClockSourceTestResultsEntry_Object = MibTableRow
shelfBusTestClockSourceTestResultsEntry = _ShelfBusTestClockSourceTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 249, 1)
)
shelfBusTestClockSourceTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestClockSourceTestResultsSourceIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestClockSourceTestResultsCardIndex"),
)
if mibBuilder.loadTexts:
    shelfBusTestClockSourceTestResultsEntry.setStatus("mandatory")


class _ShelfBusTestClockSourceTestResultsSourceIndex_Type(Integer32):
    """Custom type shelfBusTestClockSourceTestResultsSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeCP", 0),
          ("alternate", 1))
    )


_ShelfBusTestClockSourceTestResultsSourceIndex_Type.__name__ = "Integer32"
_ShelfBusTestClockSourceTestResultsSourceIndex_Object = MibTableColumn
shelfBusTestClockSourceTestResultsSourceIndex = _ShelfBusTestClockSourceTestResultsSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 249, 1, 1),
    _ShelfBusTestClockSourceTestResultsSourceIndex_Type()
)
shelfBusTestClockSourceTestResultsSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestClockSourceTestResultsSourceIndex.setStatus("mandatory")


class _ShelfBusTestClockSourceTestResultsCardIndex_Type(Integer32):
    """Custom type shelfBusTestClockSourceTestResultsCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfBusTestClockSourceTestResultsCardIndex_Type.__name__ = "Integer32"
_ShelfBusTestClockSourceTestResultsCardIndex_Object = MibTableColumn
shelfBusTestClockSourceTestResultsCardIndex = _ShelfBusTestClockSourceTestResultsCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 249, 1, 2),
    _ShelfBusTestClockSourceTestResultsCardIndex_Type()
)
shelfBusTestClockSourceTestResultsCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestClockSourceTestResultsCardIndex.setStatus("mandatory")


class _ShelfBusTestClockSourceTestResultsValue_Type(Integer32):
    """Custom type shelfBusTestClockSourceTestResultsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n1", 1),
          ("n2", 2),
          ("x", 0))
    )


_ShelfBusTestClockSourceTestResultsValue_Type.__name__ = "Integer32"
_ShelfBusTestClockSourceTestResultsValue_Object = MibTableColumn
shelfBusTestClockSourceTestResultsValue = _ShelfBusTestClockSourceTestResultsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 249, 1, 3),
    _ShelfBusTestClockSourceTestResultsValue_Type()
)
shelfBusTestClockSourceTestResultsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestClockSourceTestResultsValue.setStatus("mandatory")
_ShelfBusTestBroadcastTestResultsTable_Object = MibTable
shelfBusTestBroadcastTestResultsTable = _ShelfBusTestBroadcastTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 250)
)
if mibBuilder.loadTexts:
    shelfBusTestBroadcastTestResultsTable.setStatus("mandatory")
_ShelfBusTestBroadcastTestResultsEntry_Object = MibTableRow
shelfBusTestBroadcastTestResultsEntry = _ShelfBusTestBroadcastTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 250, 1)
)
shelfBusTestBroadcastTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestBroadcastTestResultsTxCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestBroadcastTestResultsRxCardIndex"),
)
if mibBuilder.loadTexts:
    shelfBusTestBroadcastTestResultsEntry.setStatus("mandatory")


class _ShelfBusTestBroadcastTestResultsTxCardIndex_Type(Integer32):
    """Custom type shelfBusTestBroadcastTestResultsTxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfBusTestBroadcastTestResultsTxCardIndex_Type.__name__ = "Integer32"
_ShelfBusTestBroadcastTestResultsTxCardIndex_Object = MibTableColumn
shelfBusTestBroadcastTestResultsTxCardIndex = _ShelfBusTestBroadcastTestResultsTxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 250, 1, 1),
    _ShelfBusTestBroadcastTestResultsTxCardIndex_Type()
)
shelfBusTestBroadcastTestResultsTxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestBroadcastTestResultsTxCardIndex.setStatus("mandatory")


class _ShelfBusTestBroadcastTestResultsRxCardIndex_Type(Integer32):
    """Custom type shelfBusTestBroadcastTestResultsRxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfBusTestBroadcastTestResultsRxCardIndex_Type.__name__ = "Integer32"
_ShelfBusTestBroadcastTestResultsRxCardIndex_Object = MibTableColumn
shelfBusTestBroadcastTestResultsRxCardIndex = _ShelfBusTestBroadcastTestResultsRxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 250, 1, 2),
    _ShelfBusTestBroadcastTestResultsRxCardIndex_Type()
)
shelfBusTestBroadcastTestResultsRxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestBroadcastTestResultsRxCardIndex.setStatus("mandatory")


class _ShelfBusTestBroadcastTestResultsValue_Type(Integer32):
    """Custom type shelfBusTestBroadcastTestResultsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n1", 1),
          ("n2", 2),
          ("x", 0))
    )


_ShelfBusTestBroadcastTestResultsValue_Type.__name__ = "Integer32"
_ShelfBusTestBroadcastTestResultsValue_Object = MibTableColumn
shelfBusTestBroadcastTestResultsValue = _ShelfBusTestBroadcastTestResultsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 250, 1, 3),
    _ShelfBusTestBroadcastTestResultsValue_Type()
)
shelfBusTestBroadcastTestResultsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestBroadcastTestResultsValue.setStatus("mandatory")
_ShelfBusTestPingTestsTable_Object = MibTable
shelfBusTestPingTestsTable = _ShelfBusTestPingTestsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 251)
)
if mibBuilder.loadTexts:
    shelfBusTestPingTestsTable.setStatus("mandatory")
_ShelfBusTestPingTestsEntry_Object = MibTableRow
shelfBusTestPingTestsEntry = _ShelfBusTestPingTestsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 251, 1)
)
shelfBusTestPingTestsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestPingTestsTxCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestPingTestsRxCardIndex"),
)
if mibBuilder.loadTexts:
    shelfBusTestPingTestsEntry.setStatus("mandatory")


class _ShelfBusTestPingTestsTxCardIndex_Type(Integer32):
    """Custom type shelfBusTestPingTestsTxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfBusTestPingTestsTxCardIndex_Type.__name__ = "Integer32"
_ShelfBusTestPingTestsTxCardIndex_Object = MibTableColumn
shelfBusTestPingTestsTxCardIndex = _ShelfBusTestPingTestsTxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 251, 1, 1),
    _ShelfBusTestPingTestsTxCardIndex_Type()
)
shelfBusTestPingTestsTxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestPingTestsTxCardIndex.setStatus("mandatory")


class _ShelfBusTestPingTestsRxCardIndex_Type(Integer32):
    """Custom type shelfBusTestPingTestsRxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfBusTestPingTestsRxCardIndex_Type.__name__ = "Integer32"
_ShelfBusTestPingTestsRxCardIndex_Object = MibTableColumn
shelfBusTestPingTestsRxCardIndex = _ShelfBusTestPingTestsRxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 251, 1, 2),
    _ShelfBusTestPingTestsRxCardIndex_Type()
)
shelfBusTestPingTestsRxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestPingTestsRxCardIndex.setStatus("mandatory")


class _ShelfBusTestPingTestsValue_Type(Unsigned32):
    """Custom type shelfBusTestPingTestsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfBusTestPingTestsValue_Type.__name__ = "Unsigned32"
_ShelfBusTestPingTestsValue_Object = MibTableColumn
shelfBusTestPingTestsValue = _ShelfBusTestPingTestsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 251, 1, 3),
    _ShelfBusTestPingTestsValue_Type()
)
shelfBusTestPingTestsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestPingTestsValue.setStatus("mandatory")
_ShelfBusTestPingFailuresTable_Object = MibTable
shelfBusTestPingFailuresTable = _ShelfBusTestPingFailuresTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 252)
)
if mibBuilder.loadTexts:
    shelfBusTestPingFailuresTable.setStatus("mandatory")
_ShelfBusTestPingFailuresEntry_Object = MibTableRow
shelfBusTestPingFailuresEntry = _ShelfBusTestPingFailuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 252, 1)
)
shelfBusTestPingFailuresEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestPingFailuresTxCardIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusTestPingFailuresRxCardIndex"),
)
if mibBuilder.loadTexts:
    shelfBusTestPingFailuresEntry.setStatus("mandatory")


class _ShelfBusTestPingFailuresTxCardIndex_Type(Integer32):
    """Custom type shelfBusTestPingFailuresTxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfBusTestPingFailuresTxCardIndex_Type.__name__ = "Integer32"
_ShelfBusTestPingFailuresTxCardIndex_Object = MibTableColumn
shelfBusTestPingFailuresTxCardIndex = _ShelfBusTestPingFailuresTxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 252, 1, 1),
    _ShelfBusTestPingFailuresTxCardIndex_Type()
)
shelfBusTestPingFailuresTxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestPingFailuresTxCardIndex.setStatus("mandatory")


class _ShelfBusTestPingFailuresRxCardIndex_Type(Integer32):
    """Custom type shelfBusTestPingFailuresRxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfBusTestPingFailuresRxCardIndex_Type.__name__ = "Integer32"
_ShelfBusTestPingFailuresRxCardIndex_Object = MibTableColumn
shelfBusTestPingFailuresRxCardIndex = _ShelfBusTestPingFailuresRxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 252, 1, 2),
    _ShelfBusTestPingFailuresRxCardIndex_Type()
)
shelfBusTestPingFailuresRxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusTestPingFailuresRxCardIndex.setStatus("mandatory")


class _ShelfBusTestPingFailuresValue_Type(Unsigned32):
    """Custom type shelfBusTestPingFailuresValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ShelfBusTestPingFailuresValue_Type.__name__ = "Unsigned32"
_ShelfBusTestPingFailuresValue_Object = MibTableColumn
shelfBusTestPingFailuresValue = _ShelfBusTestPingFailuresValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 2, 252, 1, 3),
    _ShelfBusTestPingFailuresValue_Type()
)
shelfBusTestPingFailuresValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusTestPingFailuresValue.setStatus("mandatory")
_ShelfBusStateTable_Object = MibTable
shelfBusStateTable = _ShelfBusStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10)
)
if mibBuilder.loadTexts:
    shelfBusStateTable.setStatus("mandatory")
_ShelfBusStateEntry_Object = MibTableRow
shelfBusStateEntry = _ShelfBusStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1)
)
shelfBusStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
)
if mibBuilder.loadTexts:
    shelfBusStateEntry.setStatus("mandatory")


class _ShelfBusAdminState_Type(Integer32):
    """Custom type shelfBusAdminState based on Integer32"""
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


_ShelfBusAdminState_Type.__name__ = "Integer32"
_ShelfBusAdminState_Object = MibTableColumn
shelfBusAdminState = _ShelfBusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1, 1),
    _ShelfBusAdminState_Type()
)
shelfBusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusAdminState.setStatus("mandatory")


class _ShelfBusOperationalState_Type(Integer32):
    """Custom type shelfBusOperationalState based on Integer32"""
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


_ShelfBusOperationalState_Type.__name__ = "Integer32"
_ShelfBusOperationalState_Object = MibTableColumn
shelfBusOperationalState = _ShelfBusOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1, 2),
    _ShelfBusOperationalState_Type()
)
shelfBusOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusOperationalState.setStatus("mandatory")


class _ShelfBusUsageState_Type(Integer32):
    """Custom type shelfBusUsageState based on Integer32"""
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


_ShelfBusUsageState_Type.__name__ = "Integer32"
_ShelfBusUsageState_Object = MibTableColumn
shelfBusUsageState = _ShelfBusUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1, 3),
    _ShelfBusUsageState_Type()
)
shelfBusUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusUsageState.setStatus("mandatory")


class _ShelfBusAvailabilityStatus_Type(OctetString):
    """Custom type shelfBusAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ShelfBusAvailabilityStatus_Type.__name__ = "OctetString"
_ShelfBusAvailabilityStatus_Object = MibTableColumn
shelfBusAvailabilityStatus = _ShelfBusAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1, 4),
    _ShelfBusAvailabilityStatus_Type()
)
shelfBusAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusAvailabilityStatus.setStatus("mandatory")


class _ShelfBusProceduralStatus_Type(OctetString):
    """Custom type shelfBusProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfBusProceduralStatus_Type.__name__ = "OctetString"
_ShelfBusProceduralStatus_Object = MibTableColumn
shelfBusProceduralStatus = _ShelfBusProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1, 5),
    _ShelfBusProceduralStatus_Type()
)
shelfBusProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusProceduralStatus.setStatus("mandatory")


class _ShelfBusControlStatus_Type(OctetString):
    """Custom type shelfBusControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfBusControlStatus_Type.__name__ = "OctetString"
_ShelfBusControlStatus_Object = MibTableColumn
shelfBusControlStatus = _ShelfBusControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1, 6),
    _ShelfBusControlStatus_Type()
)
shelfBusControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusControlStatus.setStatus("mandatory")


class _ShelfBusAlarmStatus_Type(OctetString):
    """Custom type shelfBusAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfBusAlarmStatus_Type.__name__ = "OctetString"
_ShelfBusAlarmStatus_Object = MibTableColumn
shelfBusAlarmStatus = _ShelfBusAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1, 7),
    _ShelfBusAlarmStatus_Type()
)
shelfBusAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusAlarmStatus.setStatus("mandatory")


class _ShelfBusStandbyStatus_Type(Integer32):
    """Custom type shelfBusStandbyStatus based on Integer32"""
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


_ShelfBusStandbyStatus_Type.__name__ = "Integer32"
_ShelfBusStandbyStatus_Object = MibTableColumn
shelfBusStandbyStatus = _ShelfBusStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1, 8),
    _ShelfBusStandbyStatus_Type()
)
shelfBusStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusStandbyStatus.setStatus("mandatory")


class _ShelfBusUnknownStatus_Type(Integer32):
    """Custom type shelfBusUnknownStatus based on Integer32"""
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


_ShelfBusUnknownStatus_Type.__name__ = "Integer32"
_ShelfBusUnknownStatus_Object = MibTableColumn
shelfBusUnknownStatus = _ShelfBusUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 10, 1, 9),
    _ShelfBusUnknownStatus_Type()
)
shelfBusUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusUnknownStatus.setStatus("mandatory")
_ShelfBusOperTable_Object = MibTable
shelfBusOperTable = _ShelfBusOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 11)
)
if mibBuilder.loadTexts:
    shelfBusOperTable.setStatus("mandatory")
_ShelfBusOperEntry_Object = MibTableRow
shelfBusOperEntry = _ShelfBusOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 11, 1)
)
shelfBusOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
)
if mibBuilder.loadTexts:
    shelfBusOperEntry.setStatus("mandatory")


class _ShelfBusClockSource_Type(Integer32):
    """Custom type shelfBusClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeCP", 0),
          ("alternate", 1))
    )


_ShelfBusClockSource_Type.__name__ = "Integer32"
_ShelfBusClockSource_Object = MibTableColumn
shelfBusClockSource = _ShelfBusClockSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 11, 1, 1),
    _ShelfBusClockSource_Type()
)
shelfBusClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusClockSource.setStatus("mandatory")


class _ShelfBusUtilization_Type(Unsigned32):
    """Custom type shelfBusUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ShelfBusUtilization_Type.__name__ = "Unsigned32"
_ShelfBusUtilization_Object = MibTableColumn
shelfBusUtilization = _ShelfBusUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 11, 1, 2),
    _ShelfBusUtilization_Type()
)
shelfBusUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusUtilization.setStatus("mandatory")
_ShelfBusBusTapStatusTable_Object = MibTable
shelfBusBusTapStatusTable = _ShelfBusBusTapStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 246)
)
if mibBuilder.loadTexts:
    shelfBusBusTapStatusTable.setStatus("mandatory")
_ShelfBusBusTapStatusEntry_Object = MibTableRow
shelfBusBusTapStatusEntry = _ShelfBusBusTapStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 246, 1)
)
shelfBusBusTapStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusBusTapStatusIndex"),
)
if mibBuilder.loadTexts:
    shelfBusBusTapStatusEntry.setStatus("mandatory")


class _ShelfBusBusTapStatusIndex_Type(Integer32):
    """Custom type shelfBusBusTapStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ShelfBusBusTapStatusIndex_Type.__name__ = "Integer32"
_ShelfBusBusTapStatusIndex_Object = MibTableColumn
shelfBusBusTapStatusIndex = _ShelfBusBusTapStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 246, 1, 1),
    _ShelfBusBusTapStatusIndex_Type()
)
shelfBusBusTapStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusBusTapStatusIndex.setStatus("mandatory")


class _ShelfBusBusTapStatusValue_Type(Integer32):
    """Custom type shelfBusBusTapStatusValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("none", 2),
          ("ok", 0))
    )


_ShelfBusBusTapStatusValue_Type.__name__ = "Integer32"
_ShelfBusBusTapStatusValue_Object = MibTableColumn
shelfBusBusTapStatusValue = _ShelfBusBusTapStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 246, 1, 2),
    _ShelfBusBusTapStatusValue_Type()
)
shelfBusBusTapStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusBusTapStatusValue.setStatus("mandatory")
_ShelfBusClockSourceStatusTable_Object = MibTable
shelfBusClockSourceStatusTable = _ShelfBusClockSourceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 247)
)
if mibBuilder.loadTexts:
    shelfBusClockSourceStatusTable.setStatus("mandatory")
_ShelfBusClockSourceStatusEntry_Object = MibTableRow
shelfBusClockSourceStatusEntry = _ShelfBusClockSourceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 247, 1)
)
shelfBusClockSourceStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfBusClockSourceStatusIndex"),
)
if mibBuilder.loadTexts:
    shelfBusClockSourceStatusEntry.setStatus("mandatory")


class _ShelfBusClockSourceStatusIndex_Type(Integer32):
    """Custom type shelfBusClockSourceStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeCP", 0),
          ("alternate", 1))
    )


_ShelfBusClockSourceStatusIndex_Type.__name__ = "Integer32"
_ShelfBusClockSourceStatusIndex_Object = MibTableColumn
shelfBusClockSourceStatusIndex = _ShelfBusClockSourceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 247, 1, 1),
    _ShelfBusClockSourceStatusIndex_Type()
)
shelfBusClockSourceStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfBusClockSourceStatusIndex.setStatus("mandatory")


class _ShelfBusClockSourceStatusValue_Type(Integer32):
    """Custom type shelfBusClockSourceStatusValue based on Integer32"""
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
        *(("failed", 1),
          ("notApplicable", 4),
          ("ok", 0),
          ("testInProgress", 3),
          ("unknown", 2))
    )


_ShelfBusClockSourceStatusValue_Type.__name__ = "Integer32"
_ShelfBusClockSourceStatusValue_Object = MibTableColumn
shelfBusClockSourceStatusValue = _ShelfBusClockSourceStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 3, 247, 1, 2),
    _ShelfBusClockSourceStatusValue_Type()
)
shelfBusClockSourceStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusClockSourceStatusValue.setStatus("mandatory")
_ShelfTest_ObjectIdentity = ObjectIdentity
shelfTest = _ShelfTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4)
)
_ShelfTestRowStatusTable_Object = MibTable
shelfTestRowStatusTable = _ShelfTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 1)
)
if mibBuilder.loadTexts:
    shelfTestRowStatusTable.setStatus("mandatory")
_ShelfTestRowStatusEntry_Object = MibTableRow
shelfTestRowStatusEntry = _ShelfTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 1, 1)
)
shelfTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfTestIndex"),
)
if mibBuilder.loadTexts:
    shelfTestRowStatusEntry.setStatus("mandatory")
_ShelfTestRowStatus_Type = RowStatus
_ShelfTestRowStatus_Object = MibTableColumn
shelfTestRowStatus = _ShelfTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 1, 1, 1),
    _ShelfTestRowStatus_Type()
)
shelfTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTestRowStatus.setStatus("mandatory")
_ShelfTestComponentName_Type = DisplayString
_ShelfTestComponentName_Object = MibTableColumn
shelfTestComponentName = _ShelfTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 1, 1, 2),
    _ShelfTestComponentName_Type()
)
shelfTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTestComponentName.setStatus("mandatory")
_ShelfTestStorageType_Type = StorageType
_ShelfTestStorageType_Object = MibTableColumn
shelfTestStorageType = _ShelfTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 1, 1, 4),
    _ShelfTestStorageType_Type()
)
shelfTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTestStorageType.setStatus("mandatory")
_ShelfTestIndex_Type = NonReplicated
_ShelfTestIndex_Object = MibTableColumn
shelfTestIndex = _ShelfTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 1, 1, 10),
    _ShelfTestIndex_Type()
)
shelfTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelfTestIndex.setStatus("mandatory")
_ShelfTestProvTable_Object = MibTable
shelfTestProvTable = _ShelfTestProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 10)
)
if mibBuilder.loadTexts:
    shelfTestProvTable.setStatus("mandatory")
_ShelfTestProvEntry_Object = MibTableRow
shelfTestProvEntry = _ShelfTestProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 10, 1)
)
shelfTestProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfTestIndex"),
)
if mibBuilder.loadTexts:
    shelfTestProvEntry.setStatus("mandatory")


class _ShelfTestAutomaticBusClockTest_Type(Integer32):
    """Custom type shelfTestAutomaticBusClockTest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_ShelfTestAutomaticBusClockTest_Type.__name__ = "Integer32"
_ShelfTestAutomaticBusClockTest_Object = MibTableColumn
shelfTestAutomaticBusClockTest = _ShelfTestAutomaticBusClockTest_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 10, 1, 1),
    _ShelfTestAutomaticBusClockTest_Type()
)
shelfTestAutomaticBusClockTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfTestAutomaticBusClockTest.setStatus("mandatory")
_ShelfTestSetupTable_Object = MibTable
shelfTestSetupTable = _ShelfTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 11)
)
if mibBuilder.loadTexts:
    shelfTestSetupTable.setStatus("mandatory")
_ShelfTestSetupEntry_Object = MibTableRow
shelfTestSetupEntry = _ShelfTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 11, 1)
)
shelfTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfTestIndex"),
)
if mibBuilder.loadTexts:
    shelfTestSetupEntry.setStatus("mandatory")


class _ShelfTestType_Type(Integer32):
    """Custom type shelfTestType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("busClock", 0)
    )


_ShelfTestType_Type.__name__ = "Integer32"
_ShelfTestType_Object = MibTableColumn
shelfTestType = _ShelfTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 11, 1, 1),
    _ShelfTestType_Type()
)
shelfTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfTestType.setStatus("mandatory")
_ShelfTestResultsTable_Object = MibTable
shelfTestResultsTable = _ShelfTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 12)
)
if mibBuilder.loadTexts:
    shelfTestResultsTable.setStatus("mandatory")
_ShelfTestResultsEntry_Object = MibTableRow
shelfTestResultsEntry = _ShelfTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 12, 1)
)
shelfTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfTestIndex"),
)
if mibBuilder.loadTexts:
    shelfTestResultsEntry.setStatus("mandatory")


class _ShelfTestBusClockTestResult_Type(Integer32):
    """Custom type shelfTestBusClockTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("noTest", 0),
          ("pass", 2))
    )


_ShelfTestBusClockTestResult_Type.__name__ = "Integer32"
_ShelfTestBusClockTestResult_Object = MibTableColumn
shelfTestBusClockTestResult = _ShelfTestBusClockTestResult_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 4, 12, 1, 1),
    _ShelfTestBusClockTestResult_Type()
)
shelfTestBusClockTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfTestBusClockTestResult.setStatus("mandatory")
_ShelfProvTable_Object = MibTable
shelfProvTable = _ShelfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 10)
)
if mibBuilder.loadTexts:
    shelfProvTable.setStatus("mandatory")
_ShelfProvEntry_Object = MibTableRow
shelfProvEntry = _ShelfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 10, 1)
)
shelfProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
)
if mibBuilder.loadTexts:
    shelfProvEntry.setStatus("mandatory")


class _ShelfCommentText_Type(AsciiString):
    """Custom type shelfCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ShelfCommentText_Type.__name__ = "AsciiString"
_ShelfCommentText_Object = MibTableColumn
shelfCommentText = _ShelfCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 10, 1, 1),
    _ShelfCommentText_Type()
)
shelfCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfCommentText.setStatus("mandatory")
_ShelfOperTable_Object = MibTable
shelfOperTable = _ShelfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 11)
)
if mibBuilder.loadTexts:
    shelfOperTable.setStatus("mandatory")
_ShelfOperEntry_Object = MibTableRow
shelfOperEntry = _ShelfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 11, 1)
)
shelfOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "shelfIndex"),
)
if mibBuilder.loadTexts:
    shelfOperEntry.setStatus("mandatory")


class _ShelfBusOperatingMode_Type(Integer32):
    """Custom type shelfBusOperatingMode based on Integer32"""
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


_ShelfBusOperatingMode_Type.__name__ = "Integer32"
_ShelfBusOperatingMode_Object = MibTableColumn
shelfBusOperatingMode = _ShelfBusOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 11, 1, 1),
    _ShelfBusOperatingMode_Type()
)
shelfBusOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfBusOperatingMode.setStatus("mandatory")


class _ShelfHardwareFailures_Type(OctetString):
    """Custom type shelfHardwareFailures based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ShelfHardwareFailures_Type.__name__ = "OctetString"
_ShelfHardwareFailures_Object = MibTableColumn
shelfHardwareFailures = _ShelfHardwareFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 11, 1, 2),
    _ShelfHardwareFailures_Type()
)
shelfHardwareFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfHardwareFailures.setStatus("mandatory")


class _ShelfNumberOfSlots_Type(Unsigned32):
    """Custom type shelfNumberOfSlots based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ShelfNumberOfSlots_Type.__name__ = "Unsigned32"
_ShelfNumberOfSlots_Object = MibTableColumn
shelfNumberOfSlots = _ShelfNumberOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 13, 11, 1, 3),
    _ShelfNumberOfSlots_Type()
)
shelfNumberOfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfNumberOfSlots.setStatus("mandatory")
_Mod_ObjectIdentity = ObjectIdentity
mod = _Mod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16)
)
_ModRowStatusTable_Object = MibTable
modRowStatusTable = _ModRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 1)
)
if mibBuilder.loadTexts:
    modRowStatusTable.setStatus("mandatory")
_ModRowStatusEntry_Object = MibTableRow
modRowStatusEntry = _ModRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 1, 1)
)
modRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
)
if mibBuilder.loadTexts:
    modRowStatusEntry.setStatus("mandatory")
_ModRowStatus_Type = RowStatus
_ModRowStatus_Object = MibTableColumn
modRowStatus = _ModRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 1, 1, 1),
    _ModRowStatus_Type()
)
modRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modRowStatus.setStatus("mandatory")
_ModComponentName_Type = DisplayString
_ModComponentName_Object = MibTableColumn
modComponentName = _ModComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 1, 1, 2),
    _ModComponentName_Type()
)
modComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modComponentName.setStatus("mandatory")
_ModStorageType_Type = StorageType
_ModStorageType_Object = MibTableColumn
modStorageType = _ModStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 1, 1, 4),
    _ModStorageType_Type()
)
modStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modStorageType.setStatus("mandatory")
_ModIndex_Type = NonReplicated
_ModIndex_Object = MibTableColumn
modIndex = _ModIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 1, 1, 10),
    _ModIndex_Type()
)
modIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modIndex.setStatus("mandatory")
_ModProvTable_Object = MibTable
modProvTable = _ModProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 10)
)
if mibBuilder.loadTexts:
    modProvTable.setStatus("mandatory")
_ModProvEntry_Object = MibTableRow
modProvEntry = _ModProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 10, 1)
)
modProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
)
if mibBuilder.loadTexts:
    modProvEntry.setStatus("mandatory")


class _ModNodeId_Type(Unsigned32):
    """Custom type modNodeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ModNodeId_Type.__name__ = "Unsigned32"
_ModNodeId_Object = MibTableColumn
modNodeId = _ModNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 10, 1, 1),
    _ModNodeId_Type()
)
modNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modNodeId.setStatus("mandatory")


class _ModNodeName_Type(AsciiString):
    """Custom type modNodeName based on AsciiString"""
    defaultHexValue = "4e4f4e414d45"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ModNodeName_Type.__name__ = "AsciiString"
_ModNodeName_Object = MibTableColumn
modNodeName = _ModNodeName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 10, 1, 2),
    _ModNodeName_Type()
)
modNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modNodeName.setStatus("mandatory")


class _ModNamsId_Type(Unsigned32):
    """Custom type modNamsId based on Unsigned32"""
    defaultValue = 49151

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 49151),
    )


_ModNamsId_Type.__name__ = "Unsigned32"
_ModNamsId_Object = MibTableColumn
modNamsId = _ModNamsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 10, 1, 3),
    _ModNamsId_Type()
)
modNamsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modNamsId.setStatus("mandatory")


class _ModRegionId_Type(Unsigned32):
    """Custom type modRegionId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_ModRegionId_Type.__name__ = "Unsigned32"
_ModRegionId_Object = MibTableColumn
modRegionId = _ModRegionId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 10, 1, 4),
    _ModRegionId_Type()
)
modRegionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modRegionId.setStatus("mandatory")


class _ModNodePrefix_Type(AsciiString):
    """Custom type modNodePrefix based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_ModNodePrefix_Type.__name__ = "AsciiString"
_ModNodePrefix_Object = MibTableColumn
modNodePrefix = _ModNodePrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 10, 1, 5),
    _ModNodePrefix_Type()
)
modNodePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modNodePrefix.setStatus("mandatory")
_ModNodePrefixesTable_Object = MibTable
modNodePrefixesTable = _ModNodePrefixesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 338)
)
if mibBuilder.loadTexts:
    modNodePrefixesTable.setStatus("obsolete")
_ModNodePrefixesEntry_Object = MibTableRow
modNodePrefixesEntry = _ModNodePrefixesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 338, 1)
)
modNodePrefixesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modNodePrefixesIndex"),
)
if mibBuilder.loadTexts:
    modNodePrefixesEntry.setStatus("obsolete")


class _ModNodePrefixesIndex_Type(Integer32):
    """Custom type modNodePrefixesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ModNodePrefixesIndex_Type.__name__ = "Integer32"
_ModNodePrefixesIndex_Object = MibTableColumn
modNodePrefixesIndex = _ModNodePrefixesIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 338, 1, 1),
    _ModNodePrefixesIndex_Type()
)
modNodePrefixesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modNodePrefixesIndex.setStatus("obsolete")


class _ModNodePrefixesValue_Type(AsciiString):
    """Custom type modNodePrefixesValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ModNodePrefixesValue_Type.__name__ = "AsciiString"
_ModNodePrefixesValue_Object = MibTableColumn
modNodePrefixesValue = _ModNodePrefixesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 338, 1, 2),
    _ModNodePrefixesValue_Type()
)
modNodePrefixesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modNodePrefixesValue.setStatus("obsolete")
_ModAlternatePorsPrefixesTable_Object = MibTable
modAlternatePorsPrefixesTable = _ModAlternatePorsPrefixesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 405)
)
if mibBuilder.loadTexts:
    modAlternatePorsPrefixesTable.setStatus("mandatory")
_ModAlternatePorsPrefixesEntry_Object = MibTableRow
modAlternatePorsPrefixesEntry = _ModAlternatePorsPrefixesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 405, 1)
)
modAlternatePorsPrefixesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modIndex"),
    (0, "Nortel-Magellan-Passport-ShelfMIB", "modAlternatePorsPrefixesIndex"),
)
if mibBuilder.loadTexts:
    modAlternatePorsPrefixesEntry.setStatus("mandatory")


class _ModAlternatePorsPrefixesIndex_Type(Integer32):
    """Custom type modAlternatePorsPrefixesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ModAlternatePorsPrefixesIndex_Type.__name__ = "Integer32"
_ModAlternatePorsPrefixesIndex_Object = MibTableColumn
modAlternatePorsPrefixesIndex = _ModAlternatePorsPrefixesIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 405, 1, 1),
    _ModAlternatePorsPrefixesIndex_Type()
)
modAlternatePorsPrefixesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modAlternatePorsPrefixesIndex.setStatus("mandatory")


class _ModAlternatePorsPrefixesValue_Type(AsciiString):
    """Custom type modAlternatePorsPrefixesValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ModAlternatePorsPrefixesValue_Type.__name__ = "AsciiString"
_ModAlternatePorsPrefixesValue_Object = MibTableColumn
modAlternatePorsPrefixesValue = _ModAlternatePorsPrefixesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 16, 405, 1, 2),
    _ModAlternatePorsPrefixesValue_Type()
)
modAlternatePorsPrefixesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modAlternatePorsPrefixesValue.setStatus("mandatory")
_ShelfMIB_ObjectIdentity = ObjectIdentity
shelfMIB = _ShelfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 12)
)
_ShelfGroup_ObjectIdentity = ObjectIdentity
shelfGroup = _ShelfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 12, 1)
)
_ShelfGroupBE_ObjectIdentity = ObjectIdentity
shelfGroupBE = _ShelfGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 12, 1, 5)
)
_ShelfGroupBE01_ObjectIdentity = ObjectIdentity
shelfGroupBE01 = _ShelfGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 12, 1, 5, 2)
)
_ShelfGroupBE01A_ObjectIdentity = ObjectIdentity
shelfGroupBE01A = _ShelfGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 12, 1, 5, 2, 2)
)
_ShelfCapabilities_ObjectIdentity = ObjectIdentity
shelfCapabilities = _ShelfCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 12, 3)
)
_ShelfCapabilitiesBE_ObjectIdentity = ObjectIdentity
shelfCapabilitiesBE = _ShelfCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 12, 3, 5)
)
_ShelfCapabilitiesBE01_ObjectIdentity = ObjectIdentity
shelfCapabilitiesBE01 = _ShelfCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 12, 3, 5, 2)
)
_ShelfCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
shelfCapabilitiesBE01A = _ShelfCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 12, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ShelfMIB",
    **{"shelf": shelf,
       "shelfRowStatusTable": shelfRowStatusTable,
       "shelfRowStatusEntry": shelfRowStatusEntry,
       "shelfRowStatus": shelfRowStatus,
       "shelfComponentName": shelfComponentName,
       "shelfStorageType": shelfStorageType,
       "shelfIndex": shelfIndex,
       "shelfCard": shelfCard,
       "shelfCardRowStatusTable": shelfCardRowStatusTable,
       "shelfCardRowStatusEntry": shelfCardRowStatusEntry,
       "shelfCardRowStatus": shelfCardRowStatus,
       "shelfCardComponentName": shelfCardComponentName,
       "shelfCardStorageType": shelfCardStorageType,
       "shelfCardIndex": shelfCardIndex,
       "shelfCardBusTap": shelfCardBusTap,
       "shelfCardBusTapRowStatusTable": shelfCardBusTapRowStatusTable,
       "shelfCardBusTapRowStatusEntry": shelfCardBusTapRowStatusEntry,
       "shelfCardBusTapRowStatus": shelfCardBusTapRowStatus,
       "shelfCardBusTapComponentName": shelfCardBusTapComponentName,
       "shelfCardBusTapStorageType": shelfCardBusTapStorageType,
       "shelfCardBusTapIndex": shelfCardBusTapIndex,
       "shelfCardBusTapStateTable": shelfCardBusTapStateTable,
       "shelfCardBusTapStateEntry": shelfCardBusTapStateEntry,
       "shelfCardBusTapAdminState": shelfCardBusTapAdminState,
       "shelfCardBusTapOperationalState": shelfCardBusTapOperationalState,
       "shelfCardBusTapUsageState": shelfCardBusTapUsageState,
       "shelfCardBusTapAvailabilityStatus": shelfCardBusTapAvailabilityStatus,
       "shelfCardBusTapProceduralStatus": shelfCardBusTapProceduralStatus,
       "shelfCardBusTapControlStatus": shelfCardBusTapControlStatus,
       "shelfCardBusTapAlarmStatus": shelfCardBusTapAlarmStatus,
       "shelfCardBusTapStandbyStatus": shelfCardBusTapStandbyStatus,
       "shelfCardBusTapUnknownStatus": shelfCardBusTapUnknownStatus,
       "shelfCardBusTapOperTable": shelfCardBusTapOperTable,
       "shelfCardBusTapOperEntry": shelfCardBusTapOperEntry,
       "shelfCardBusTapFailuresInEffect": shelfCardBusTapFailuresInEffect,
       "shelfCardBusTapDependenciesInEffect": shelfCardBusTapDependenciesInEffect,
       "shelfCardBusTapCardsAvailable": shelfCardBusTapCardsAvailable,
       "shelfCardBusTapCardsTxTo": shelfCardBusTapCardsTxTo,
       "shelfCardBusTapErrorsTable": shelfCardBusTapErrorsTable,
       "shelfCardBusTapErrorsEntry": shelfCardBusTapErrorsEntry,
       "shelfCardBusTapSelfTestErrorCode": shelfCardBusTapSelfTestErrorCode,
       "shelfCardBusTapClockErrors": shelfCardBusTapClockErrors,
       "shelfCardBusTapEndOfCellErrors": shelfCardBusTapEndOfCellErrors,
       "shelfCardBusTapParityErrors": shelfCardBusTapParityErrors,
       "shelfCardBusTapFrmCongestionErrors": shelfCardBusTapFrmCongestionErrors,
       "shelfCardBusTapFrmCollisionErrors": shelfCardBusTapFrmCollisionErrors,
       "shelfCardBusTapFrmTimeoutErrors": shelfCardBusTapFrmTimeoutErrors,
       "shelfCardBusTapFrmDeliveryErrors": shelfCardBusTapFrmDeliveryErrors,
       "shelfCardBusTapFrmSizeErrors": shelfCardBusTapFrmSizeErrors,
       "shelfCardTest": shelfCardTest,
       "shelfCardTestRowStatusTable": shelfCardTestRowStatusTable,
       "shelfCardTestRowStatusEntry": shelfCardTestRowStatusEntry,
       "shelfCardTestRowStatus": shelfCardTestRowStatus,
       "shelfCardTestComponentName": shelfCardTestComponentName,
       "shelfCardTestStorageType": shelfCardTestStorageType,
       "shelfCardTestIndex": shelfCardTestIndex,
       "shelfCardTestStateTable": shelfCardTestStateTable,
       "shelfCardTestStateEntry": shelfCardTestStateEntry,
       "shelfCardTestAdminState": shelfCardTestAdminState,
       "shelfCardTestOperationalState": shelfCardTestOperationalState,
       "shelfCardTestUsageState": shelfCardTestUsageState,
       "shelfCardTestSetupTable": shelfCardTestSetupTable,
       "shelfCardTestSetupEntry": shelfCardTestSetupEntry,
       "shelfCardTestTargetCard": shelfCardTestTargetCard,
       "shelfCardTestFrmTypes": shelfCardTestFrmTypes,
       "shelfCardTestFrmPriorities": shelfCardTestFrmPriorities,
       "shelfCardTestFrmPatternType": shelfCardTestFrmPatternType,
       "shelfCardTestCustomizedPattern": shelfCardTestCustomizedPattern,
       "shelfCardTestDuration": shelfCardTestDuration,
       "shelfCardTestResultsTable": shelfCardTestResultsTable,
       "shelfCardTestResultsEntry": shelfCardTestResultsEntry,
       "shelfCardTestElapsedTime": shelfCardTestElapsedTime,
       "shelfCardTestTimeRemaining": shelfCardTestTimeRemaining,
       "shelfCardTestCauseOfTermination": shelfCardTestCauseOfTermination,
       "shelfCardTestSizeTable": shelfCardTestSizeTable,
       "shelfCardTestSizeEntry": shelfCardTestSizeEntry,
       "shelfCardTestSizeIndex": shelfCardTestSizeIndex,
       "shelfCardTestSizeValue": shelfCardTestSizeValue,
       "shelfCardTestLoadingFrmDataTable": shelfCardTestLoadingFrmDataTable,
       "shelfCardTestLoadingFrmDataEntry": shelfCardTestLoadingFrmDataEntry,
       "shelfCardTestLoadingFrmDataResultsIndex": shelfCardTestLoadingFrmDataResultsIndex,
       "shelfCardTestLoadingFrmDataPriorityIndex": shelfCardTestLoadingFrmDataPriorityIndex,
       "shelfCardTestLoadingFrmDataValue": shelfCardTestLoadingFrmDataValue,
       "shelfCardTestVerificationFrmDataTable": shelfCardTestVerificationFrmDataTable,
       "shelfCardTestVerificationFrmDataEntry": shelfCardTestVerificationFrmDataEntry,
       "shelfCardTestVerificationFrmDataResultsIndex": shelfCardTestVerificationFrmDataResultsIndex,
       "shelfCardTestVerificationFrmDataPriorityIndex": shelfCardTestVerificationFrmDataPriorityIndex,
       "shelfCardTestVerificationFrmDataValue": shelfCardTestVerificationFrmDataValue,
       "shelfCardDiag": shelfCardDiag,
       "shelfCardDiagRowStatusTable": shelfCardDiagRowStatusTable,
       "shelfCardDiagRowStatusEntry": shelfCardDiagRowStatusEntry,
       "shelfCardDiagRowStatus": shelfCardDiagRowStatus,
       "shelfCardDiagComponentName": shelfCardDiagComponentName,
       "shelfCardDiagStorageType": shelfCardDiagStorageType,
       "shelfCardDiagIndex": shelfCardDiagIndex,
       "shelfCardDiagTrapData": shelfCardDiagTrapData,
       "shelfCardDiagTrapDataRowStatusTable": shelfCardDiagTrapDataRowStatusTable,
       "shelfCardDiagTrapDataRowStatusEntry": shelfCardDiagTrapDataRowStatusEntry,
       "shelfCardDiagTrapDataRowStatus": shelfCardDiagTrapDataRowStatus,
       "shelfCardDiagTrapDataComponentName": shelfCardDiagTrapDataComponentName,
       "shelfCardDiagTrapDataStorageType": shelfCardDiagTrapDataStorageType,
       "shelfCardDiagTrapDataIndex": shelfCardDiagTrapDataIndex,
       "shelfCardDiagTrapDataLine": shelfCardDiagTrapDataLine,
       "shelfCardDiagTrapDataLineRowStatusTable": shelfCardDiagTrapDataLineRowStatusTable,
       "shelfCardDiagTrapDataLineRowStatusEntry": shelfCardDiagTrapDataLineRowStatusEntry,
       "shelfCardDiagTrapDataLineRowStatus": shelfCardDiagTrapDataLineRowStatus,
       "shelfCardDiagTrapDataLineComponentName": shelfCardDiagTrapDataLineComponentName,
       "shelfCardDiagTrapDataLineStorageType": shelfCardDiagTrapDataLineStorageType,
       "shelfCardDiagTrapDataLineIndex": shelfCardDiagTrapDataLineIndex,
       "shelfCardDiagTrapDataLineOperTable": shelfCardDiagTrapDataLineOperTable,
       "shelfCardDiagTrapDataLineOperEntry": shelfCardDiagTrapDataLineOperEntry,
       "shelfCardDiagTrapDataLineData": shelfCardDiagTrapDataLineData,
       "shelfCardDiagRecErr": shelfCardDiagRecErr,
       "shelfCardDiagRecErrRowStatusTable": shelfCardDiagRecErrRowStatusTable,
       "shelfCardDiagRecErrRowStatusEntry": shelfCardDiagRecErrRowStatusEntry,
       "shelfCardDiagRecErrRowStatus": shelfCardDiagRecErrRowStatus,
       "shelfCardDiagRecErrComponentName": shelfCardDiagRecErrComponentName,
       "shelfCardDiagRecErrStorageType": shelfCardDiagRecErrStorageType,
       "shelfCardDiagRecErrIndex": shelfCardDiagRecErrIndex,
       "shelfCardDiagRecErrLine": shelfCardDiagRecErrLine,
       "shelfCardDiagRecErrLineRowStatusTable": shelfCardDiagRecErrLineRowStatusTable,
       "shelfCardDiagRecErrLineRowStatusEntry": shelfCardDiagRecErrLineRowStatusEntry,
       "shelfCardDiagRecErrLineRowStatus": shelfCardDiagRecErrLineRowStatus,
       "shelfCardDiagRecErrLineComponentName": shelfCardDiagRecErrLineComponentName,
       "shelfCardDiagRecErrLineStorageType": shelfCardDiagRecErrLineStorageType,
       "shelfCardDiagRecErrLineIndex": shelfCardDiagRecErrLineIndex,
       "shelfCardDiagRecErrLineOperTable": shelfCardDiagRecErrLineOperTable,
       "shelfCardDiagRecErrLineOperEntry": shelfCardDiagRecErrLineOperEntry,
       "shelfCardDiagRecErrLineData": shelfCardDiagRecErrLineData,
       "shelfCardProvTable": shelfCardProvTable,
       "shelfCardProvEntry": shelfCardProvEntry,
       "shelfCardCardType": shelfCardCardType,
       "shelfCardSparingConnection": shelfCardSparingConnection,
       "shelfCardCommentText": shelfCardCommentText,
       "shelfCardStateTable": shelfCardStateTable,
       "shelfCardStateEntry": shelfCardStateEntry,
       "shelfCardAdminState": shelfCardAdminState,
       "shelfCardOperationalState": shelfCardOperationalState,
       "shelfCardUsageState": shelfCardUsageState,
       "shelfCardAvailabilityStatus": shelfCardAvailabilityStatus,
       "shelfCardProceduralStatus": shelfCardProceduralStatus,
       "shelfCardControlStatus": shelfCardControlStatus,
       "shelfCardAlarmStatus": shelfCardAlarmStatus,
       "shelfCardStandbyStatus": shelfCardStandbyStatus,
       "shelfCardUnknownStatus": shelfCardUnknownStatus,
       "shelfCardOperTable": shelfCardOperTable,
       "shelfCardOperEntry": shelfCardOperEntry,
       "shelfCardCurrentLP": shelfCardCurrentLP,
       "shelfCardFailureCause": shelfCardFailureCause,
       "shelfCardSelfTestFault": shelfCardSelfTestFault,
       "shelfCardSparingConnectionStatus": shelfCardSparingConnectionStatus,
       "shelfCardPropTable": shelfCardPropTable,
       "shelfCardPropEntry": shelfCardPropEntry,
       "shelfCardInsertedCardType": shelfCardInsertedCardType,
       "shelfCardPmRevisionCode": shelfCardPmRevisionCode,
       "shelfCardImRevisionCode": shelfCardImRevisionCode,
       "shelfCardSerialNumber": shelfCardSerialNumber,
       "shelfCardActiveFirmwareVersion": shelfCardActiveFirmwareVersion,
       "shelfCardInactiveFirmwareVersion": shelfCardInactiveFirmwareVersion,
       "shelfCardProductCode": shelfCardProductCode,
       "shelfCardUtilTable": shelfCardUtilTable,
       "shelfCardUtilEntry": shelfCardUtilEntry,
       "shelfCardTimeInterval": shelfCardTimeInterval,
       "shelfCardCpuUtil": shelfCardCpuUtil,
       "shelfCardCpuUtilAvg": shelfCardCpuUtilAvg,
       "shelfCardCpuUtilAvgMin": shelfCardCpuUtilAvgMin,
       "shelfCardCpuUtilAvgMax": shelfCardCpuUtilAvgMax,
       "shelfCardMsgBlockUsage": shelfCardMsgBlockUsage,
       "shelfCardMsgBlockUsageAvg": shelfCardMsgBlockUsageAvg,
       "shelfCardMsgBlockUsageAvgMin": shelfCardMsgBlockUsageAvgMin,
       "shelfCardMsgBlockUsageAvgMax": shelfCardMsgBlockUsageAvgMax,
       "shelfCardLocalMsgBlockUsage": shelfCardLocalMsgBlockUsage,
       "shelfCardLocalMsgBlockUsageAvg": shelfCardLocalMsgBlockUsageAvg,
       "shelfCardLocalMsgBlockUsageMin": shelfCardLocalMsgBlockUsageMin,
       "shelfCardLocalMsgBlockUsageMax": shelfCardLocalMsgBlockUsageMax,
       "shelfCardCapTable": shelfCardCapTable,
       "shelfCardCapEntry": shelfCardCapEntry,
       "shelfCardMsgBlockCapacity": shelfCardMsgBlockCapacity,
       "shelfCardLocalMsgBlockCapacity": shelfCardLocalMsgBlockCapacity,
       "shelfCardDcard": shelfCardDcard,
       "shelfCardDcardRowStatusTable": shelfCardDcardRowStatusTable,
       "shelfCardDcardRowStatusEntry": shelfCardDcardRowStatusEntry,
       "shelfCardDcardRowStatus": shelfCardDcardRowStatus,
       "shelfCardDcardComponentName": shelfCardDcardComponentName,
       "shelfCardDcardStorageType": shelfCardDcardStorageType,
       "shelfCardDcardIndex": shelfCardDcardIndex,
       "shelfCardDcardDcardOperTable": shelfCardDcardDcardOperTable,
       "shelfCardDcardDcardOperEntry": shelfCardDcardDcardOperEntry,
       "shelfCardDcardType": shelfCardDcardType,
       "shelfCardDcardMemorySize": shelfCardDcardMemorySize,
       "shelfCardDcardProductCode": shelfCardDcardProductCode,
       "shelfCardConfiguredLPsTable": shelfCardConfiguredLPsTable,
       "shelfCardConfiguredLPsEntry": shelfCardConfiguredLPsEntry,
       "shelfCardConfiguredLPsValue": shelfCardConfiguredLPsValue,
       "shelfCardMemoryCapacityTable": shelfCardMemoryCapacityTable,
       "shelfCardMemoryCapacityEntry": shelfCardMemoryCapacityEntry,
       "shelfCardMemoryCapacityIndex": shelfCardMemoryCapacityIndex,
       "shelfCardMemoryCapacityValue": shelfCardMemoryCapacityValue,
       "shelfCardMemoryUsageTable": shelfCardMemoryUsageTable,
       "shelfCardMemoryUsageEntry": shelfCardMemoryUsageEntry,
       "shelfCardMemoryUsageIndex": shelfCardMemoryUsageIndex,
       "shelfCardMemoryUsageValue": shelfCardMemoryUsageValue,
       "shelfCardMemoryUsageAvgTable": shelfCardMemoryUsageAvgTable,
       "shelfCardMemoryUsageAvgEntry": shelfCardMemoryUsageAvgEntry,
       "shelfCardMemoryUsageAvgIndex": shelfCardMemoryUsageAvgIndex,
       "shelfCardMemoryUsageAvgValue": shelfCardMemoryUsageAvgValue,
       "shelfCardMemoryUsageAvgMinTable": shelfCardMemoryUsageAvgMinTable,
       "shelfCardMemoryUsageAvgMinEntry": shelfCardMemoryUsageAvgMinEntry,
       "shelfCardMemoryUsageAvgMinIndex": shelfCardMemoryUsageAvgMinIndex,
       "shelfCardMemoryUsageAvgMinValue": shelfCardMemoryUsageAvgMinValue,
       "shelfCardMemoryUsageAvgMaxTable": shelfCardMemoryUsageAvgMaxTable,
       "shelfCardMemoryUsageAvgMaxEntry": shelfCardMemoryUsageAvgMaxEntry,
       "shelfCardMemoryUsageAvgMaxIndex": shelfCardMemoryUsageAvgMaxIndex,
       "shelfCardMemoryUsageAvgMaxValue": shelfCardMemoryUsageAvgMaxValue,
       "shelfCardCurrentLpTable": shelfCardCurrentLpTable,
       "shelfCardCurrentLpEntry": shelfCardCurrentLpEntry,
       "shelfCardCurrentLpValue": shelfCardCurrentLpValue,
       "shelfBus": shelfBus,
       "shelfBusRowStatusTable": shelfBusRowStatusTable,
       "shelfBusRowStatusEntry": shelfBusRowStatusEntry,
       "shelfBusRowStatus": shelfBusRowStatus,
       "shelfBusComponentName": shelfBusComponentName,
       "shelfBusStorageType": shelfBusStorageType,
       "shelfBusIndex": shelfBusIndex,
       "shelfBusTest": shelfBusTest,
       "shelfBusTestRowStatusTable": shelfBusTestRowStatusTable,
       "shelfBusTestRowStatusEntry": shelfBusTestRowStatusEntry,
       "shelfBusTestRowStatus": shelfBusTestRowStatus,
       "shelfBusTestComponentName": shelfBusTestComponentName,
       "shelfBusTestStorageType": shelfBusTestStorageType,
       "shelfBusTestIndex": shelfBusTestIndex,
       "shelfBusTestStateTable": shelfBusTestStateTable,
       "shelfBusTestStateEntry": shelfBusTestStateEntry,
       "shelfBusTestAdminState": shelfBusTestAdminState,
       "shelfBusTestOperationalState": shelfBusTestOperationalState,
       "shelfBusTestUsageState": shelfBusTestUsageState,
       "shelfBusTestSetupTable": shelfBusTestSetupTable,
       "shelfBusTestSetupEntry": shelfBusTestSetupEntry,
       "shelfBusTestDuration": shelfBusTestDuration,
       "shelfBusTestResultsTable": shelfBusTestResultsTable,
       "shelfBusTestResultsEntry": shelfBusTestResultsEntry,
       "shelfBusTestElapsedTime": shelfBusTestElapsedTime,
       "shelfBusTestTimeRemaining": shelfBusTestTimeRemaining,
       "shelfBusTestCauseOfTermination": shelfBusTestCauseOfTermination,
       "shelfBusTestTestsDone": shelfBusTestTestsDone,
       "shelfBusTestSelfTestResultsTable": shelfBusTestSelfTestResultsTable,
       "shelfBusTestSelfTestResultsEntry": shelfBusTestSelfTestResultsEntry,
       "shelfBusTestSelfTestResultsIndex": shelfBusTestSelfTestResultsIndex,
       "shelfBusTestSelfTestResultsValue": shelfBusTestSelfTestResultsValue,
       "shelfBusTestClockSourceTestResultsTable": shelfBusTestClockSourceTestResultsTable,
       "shelfBusTestClockSourceTestResultsEntry": shelfBusTestClockSourceTestResultsEntry,
       "shelfBusTestClockSourceTestResultsSourceIndex": shelfBusTestClockSourceTestResultsSourceIndex,
       "shelfBusTestClockSourceTestResultsCardIndex": shelfBusTestClockSourceTestResultsCardIndex,
       "shelfBusTestClockSourceTestResultsValue": shelfBusTestClockSourceTestResultsValue,
       "shelfBusTestBroadcastTestResultsTable": shelfBusTestBroadcastTestResultsTable,
       "shelfBusTestBroadcastTestResultsEntry": shelfBusTestBroadcastTestResultsEntry,
       "shelfBusTestBroadcastTestResultsTxCardIndex": shelfBusTestBroadcastTestResultsTxCardIndex,
       "shelfBusTestBroadcastTestResultsRxCardIndex": shelfBusTestBroadcastTestResultsRxCardIndex,
       "shelfBusTestBroadcastTestResultsValue": shelfBusTestBroadcastTestResultsValue,
       "shelfBusTestPingTestsTable": shelfBusTestPingTestsTable,
       "shelfBusTestPingTestsEntry": shelfBusTestPingTestsEntry,
       "shelfBusTestPingTestsTxCardIndex": shelfBusTestPingTestsTxCardIndex,
       "shelfBusTestPingTestsRxCardIndex": shelfBusTestPingTestsRxCardIndex,
       "shelfBusTestPingTestsValue": shelfBusTestPingTestsValue,
       "shelfBusTestPingFailuresTable": shelfBusTestPingFailuresTable,
       "shelfBusTestPingFailuresEntry": shelfBusTestPingFailuresEntry,
       "shelfBusTestPingFailuresTxCardIndex": shelfBusTestPingFailuresTxCardIndex,
       "shelfBusTestPingFailuresRxCardIndex": shelfBusTestPingFailuresRxCardIndex,
       "shelfBusTestPingFailuresValue": shelfBusTestPingFailuresValue,
       "shelfBusStateTable": shelfBusStateTable,
       "shelfBusStateEntry": shelfBusStateEntry,
       "shelfBusAdminState": shelfBusAdminState,
       "shelfBusOperationalState": shelfBusOperationalState,
       "shelfBusUsageState": shelfBusUsageState,
       "shelfBusAvailabilityStatus": shelfBusAvailabilityStatus,
       "shelfBusProceduralStatus": shelfBusProceduralStatus,
       "shelfBusControlStatus": shelfBusControlStatus,
       "shelfBusAlarmStatus": shelfBusAlarmStatus,
       "shelfBusStandbyStatus": shelfBusStandbyStatus,
       "shelfBusUnknownStatus": shelfBusUnknownStatus,
       "shelfBusOperTable": shelfBusOperTable,
       "shelfBusOperEntry": shelfBusOperEntry,
       "shelfBusClockSource": shelfBusClockSource,
       "shelfBusUtilization": shelfBusUtilization,
       "shelfBusBusTapStatusTable": shelfBusBusTapStatusTable,
       "shelfBusBusTapStatusEntry": shelfBusBusTapStatusEntry,
       "shelfBusBusTapStatusIndex": shelfBusBusTapStatusIndex,
       "shelfBusBusTapStatusValue": shelfBusBusTapStatusValue,
       "shelfBusClockSourceStatusTable": shelfBusClockSourceStatusTable,
       "shelfBusClockSourceStatusEntry": shelfBusClockSourceStatusEntry,
       "shelfBusClockSourceStatusIndex": shelfBusClockSourceStatusIndex,
       "shelfBusClockSourceStatusValue": shelfBusClockSourceStatusValue,
       "shelfTest": shelfTest,
       "shelfTestRowStatusTable": shelfTestRowStatusTable,
       "shelfTestRowStatusEntry": shelfTestRowStatusEntry,
       "shelfTestRowStatus": shelfTestRowStatus,
       "shelfTestComponentName": shelfTestComponentName,
       "shelfTestStorageType": shelfTestStorageType,
       "shelfTestIndex": shelfTestIndex,
       "shelfTestProvTable": shelfTestProvTable,
       "shelfTestProvEntry": shelfTestProvEntry,
       "shelfTestAutomaticBusClockTest": shelfTestAutomaticBusClockTest,
       "shelfTestSetupTable": shelfTestSetupTable,
       "shelfTestSetupEntry": shelfTestSetupEntry,
       "shelfTestType": shelfTestType,
       "shelfTestResultsTable": shelfTestResultsTable,
       "shelfTestResultsEntry": shelfTestResultsEntry,
       "shelfTestBusClockTestResult": shelfTestBusClockTestResult,
       "shelfProvTable": shelfProvTable,
       "shelfProvEntry": shelfProvEntry,
       "shelfCommentText": shelfCommentText,
       "shelfOperTable": shelfOperTable,
       "shelfOperEntry": shelfOperEntry,
       "shelfBusOperatingMode": shelfBusOperatingMode,
       "shelfHardwareFailures": shelfHardwareFailures,
       "shelfNumberOfSlots": shelfNumberOfSlots,
       "mod": mod,
       "modRowStatusTable": modRowStatusTable,
       "modRowStatusEntry": modRowStatusEntry,
       "modRowStatus": modRowStatus,
       "modComponentName": modComponentName,
       "modStorageType": modStorageType,
       "modIndex": modIndex,
       "modProvTable": modProvTable,
       "modProvEntry": modProvEntry,
       "modNodeId": modNodeId,
       "modNodeName": modNodeName,
       "modNamsId": modNamsId,
       "modRegionId": modRegionId,
       "modNodePrefix": modNodePrefix,
       "modNodePrefixesTable": modNodePrefixesTable,
       "modNodePrefixesEntry": modNodePrefixesEntry,
       "modNodePrefixesIndex": modNodePrefixesIndex,
       "modNodePrefixesValue": modNodePrefixesValue,
       "modAlternatePorsPrefixesTable": modAlternatePorsPrefixesTable,
       "modAlternatePorsPrefixesEntry": modAlternatePorsPrefixesEntry,
       "modAlternatePorsPrefixesIndex": modAlternatePorsPrefixesIndex,
       "modAlternatePorsPrefixesValue": modAlternatePorsPrefixesValue,
       "shelfMIB": shelfMIB,
       "shelfGroup": shelfGroup,
       "shelfGroupBE": shelfGroupBE,
       "shelfGroupBE01": shelfGroupBE01,
       "shelfGroupBE01A": shelfGroupBE01A,
       "shelfCapabilities": shelfCapabilities,
       "shelfCapabilitiesBE": shelfCapabilitiesBE,
       "shelfCapabilitiesBE01": shelfCapabilitiesBE01,
       "shelfCapabilitiesBE01A": shelfCapabilitiesBE01A}
)
