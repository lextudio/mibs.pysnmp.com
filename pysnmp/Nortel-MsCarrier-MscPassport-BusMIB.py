# SNMP MIB module (Nortel-MsCarrier-MscPassport-BusMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-BusMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:03 2024
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

(mscShelf,
 mscShelfCard,
 mscShelfCardIndex,
 mscShelfIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-BaseShelfMIB",
    "mscShelf",
    "mscShelfCard",
    "mscShelfCardIndex",
    "mscShelfIndex")

(DisplayString,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(NonReplicated,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
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

_MscShelfCardBusTap_ObjectIdentity = ObjectIdentity
mscShelfCardBusTap = _MscShelfCardBusTap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2)
)
_MscShelfCardBusTapRowStatusTable_Object = MibTable
mscShelfCardBusTapRowStatusTable = _MscShelfCardBusTapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardBusTapRowStatusTable.setStatus("mandatory")
_MscShelfCardBusTapRowStatusEntry_Object = MibTableRow
mscShelfCardBusTapRowStatusEntry = _MscShelfCardBusTapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 1, 1)
)
mscShelfCardBusTapRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfCardBusTapIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardBusTapRowStatusEntry.setStatus("mandatory")
_MscShelfCardBusTapRowStatus_Type = RowStatus
_MscShelfCardBusTapRowStatus_Object = MibTableColumn
mscShelfCardBusTapRowStatus = _MscShelfCardBusTapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 1, 1, 1),
    _MscShelfCardBusTapRowStatus_Type()
)
mscShelfCardBusTapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapRowStatus.setStatus("mandatory")
_MscShelfCardBusTapComponentName_Type = DisplayString
_MscShelfCardBusTapComponentName_Object = MibTableColumn
mscShelfCardBusTapComponentName = _MscShelfCardBusTapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 1, 1, 2),
    _MscShelfCardBusTapComponentName_Type()
)
mscShelfCardBusTapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapComponentName.setStatus("mandatory")
_MscShelfCardBusTapStorageType_Type = StorageType
_MscShelfCardBusTapStorageType_Object = MibTableColumn
mscShelfCardBusTapStorageType = _MscShelfCardBusTapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 1, 1, 4),
    _MscShelfCardBusTapStorageType_Type()
)
mscShelfCardBusTapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapStorageType.setStatus("mandatory")


class _MscShelfCardBusTapIndex_Type(Integer32):
    """Custom type mscShelfCardBusTapIndex based on Integer32"""
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


_MscShelfCardBusTapIndex_Type.__name__ = "Integer32"
_MscShelfCardBusTapIndex_Object = MibTableColumn
mscShelfCardBusTapIndex = _MscShelfCardBusTapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 1, 1, 10),
    _MscShelfCardBusTapIndex_Type()
)
mscShelfCardBusTapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardBusTapIndex.setStatus("mandatory")
_MscShelfCardBusTapStateTable_Object = MibTable
mscShelfCardBusTapStateTable = _MscShelfCardBusTapStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscShelfCardBusTapStateTable.setStatus("mandatory")
_MscShelfCardBusTapStateEntry_Object = MibTableRow
mscShelfCardBusTapStateEntry = _MscShelfCardBusTapStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1)
)
mscShelfCardBusTapStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfCardBusTapIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardBusTapStateEntry.setStatus("mandatory")


class _MscShelfCardBusTapAdminState_Type(Integer32):
    """Custom type mscShelfCardBusTapAdminState based on Integer32"""
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


_MscShelfCardBusTapAdminState_Type.__name__ = "Integer32"
_MscShelfCardBusTapAdminState_Object = MibTableColumn
mscShelfCardBusTapAdminState = _MscShelfCardBusTapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1, 1),
    _MscShelfCardBusTapAdminState_Type()
)
mscShelfCardBusTapAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapAdminState.setStatus("mandatory")


class _MscShelfCardBusTapOperationalState_Type(Integer32):
    """Custom type mscShelfCardBusTapOperationalState based on Integer32"""
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


_MscShelfCardBusTapOperationalState_Type.__name__ = "Integer32"
_MscShelfCardBusTapOperationalState_Object = MibTableColumn
mscShelfCardBusTapOperationalState = _MscShelfCardBusTapOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1, 2),
    _MscShelfCardBusTapOperationalState_Type()
)
mscShelfCardBusTapOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapOperationalState.setStatus("mandatory")


class _MscShelfCardBusTapUsageState_Type(Integer32):
    """Custom type mscShelfCardBusTapUsageState based on Integer32"""
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


_MscShelfCardBusTapUsageState_Type.__name__ = "Integer32"
_MscShelfCardBusTapUsageState_Object = MibTableColumn
mscShelfCardBusTapUsageState = _MscShelfCardBusTapUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1, 3),
    _MscShelfCardBusTapUsageState_Type()
)
mscShelfCardBusTapUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapUsageState.setStatus("mandatory")


class _MscShelfCardBusTapAvailabilityStatus_Type(OctetString):
    """Custom type mscShelfCardBusTapAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfCardBusTapAvailabilityStatus_Type.__name__ = "OctetString"
_MscShelfCardBusTapAvailabilityStatus_Object = MibTableColumn
mscShelfCardBusTapAvailabilityStatus = _MscShelfCardBusTapAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1, 4),
    _MscShelfCardBusTapAvailabilityStatus_Type()
)
mscShelfCardBusTapAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapAvailabilityStatus.setStatus("mandatory")


class _MscShelfCardBusTapProceduralStatus_Type(OctetString):
    """Custom type mscShelfCardBusTapProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardBusTapProceduralStatus_Type.__name__ = "OctetString"
_MscShelfCardBusTapProceduralStatus_Object = MibTableColumn
mscShelfCardBusTapProceduralStatus = _MscShelfCardBusTapProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1, 5),
    _MscShelfCardBusTapProceduralStatus_Type()
)
mscShelfCardBusTapProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapProceduralStatus.setStatus("mandatory")


class _MscShelfCardBusTapControlStatus_Type(OctetString):
    """Custom type mscShelfCardBusTapControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardBusTapControlStatus_Type.__name__ = "OctetString"
_MscShelfCardBusTapControlStatus_Object = MibTableColumn
mscShelfCardBusTapControlStatus = _MscShelfCardBusTapControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1, 6),
    _MscShelfCardBusTapControlStatus_Type()
)
mscShelfCardBusTapControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapControlStatus.setStatus("mandatory")


class _MscShelfCardBusTapAlarmStatus_Type(OctetString):
    """Custom type mscShelfCardBusTapAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardBusTapAlarmStatus_Type.__name__ = "OctetString"
_MscShelfCardBusTapAlarmStatus_Object = MibTableColumn
mscShelfCardBusTapAlarmStatus = _MscShelfCardBusTapAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1, 7),
    _MscShelfCardBusTapAlarmStatus_Type()
)
mscShelfCardBusTapAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapAlarmStatus.setStatus("mandatory")


class _MscShelfCardBusTapStandbyStatus_Type(Integer32):
    """Custom type mscShelfCardBusTapStandbyStatus based on Integer32"""
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


_MscShelfCardBusTapStandbyStatus_Type.__name__ = "Integer32"
_MscShelfCardBusTapStandbyStatus_Object = MibTableColumn
mscShelfCardBusTapStandbyStatus = _MscShelfCardBusTapStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1, 8),
    _MscShelfCardBusTapStandbyStatus_Type()
)
mscShelfCardBusTapStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapStandbyStatus.setStatus("mandatory")


class _MscShelfCardBusTapUnknownStatus_Type(Integer32):
    """Custom type mscShelfCardBusTapUnknownStatus based on Integer32"""
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


_MscShelfCardBusTapUnknownStatus_Type.__name__ = "Integer32"
_MscShelfCardBusTapUnknownStatus_Object = MibTableColumn
mscShelfCardBusTapUnknownStatus = _MscShelfCardBusTapUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 10, 1, 9),
    _MscShelfCardBusTapUnknownStatus_Type()
)
mscShelfCardBusTapUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapUnknownStatus.setStatus("mandatory")
_MscShelfCardBusTapOperTable_Object = MibTable
mscShelfCardBusTapOperTable = _MscShelfCardBusTapOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscShelfCardBusTapOperTable.setStatus("mandatory")
_MscShelfCardBusTapOperEntry_Object = MibTableRow
mscShelfCardBusTapOperEntry = _MscShelfCardBusTapOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 11, 1)
)
mscShelfCardBusTapOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfCardBusTapIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardBusTapOperEntry.setStatus("mandatory")


class _MscShelfCardBusTapFailuresInEffect_Type(OctetString):
    """Custom type mscShelfCardBusTapFailuresInEffect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardBusTapFailuresInEffect_Type.__name__ = "OctetString"
_MscShelfCardBusTapFailuresInEffect_Object = MibTableColumn
mscShelfCardBusTapFailuresInEffect = _MscShelfCardBusTapFailuresInEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 11, 1, 1),
    _MscShelfCardBusTapFailuresInEffect_Type()
)
mscShelfCardBusTapFailuresInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapFailuresInEffect.setStatus("mandatory")


class _MscShelfCardBusTapDependenciesInEffect_Type(OctetString):
    """Custom type mscShelfCardBusTapDependenciesInEffect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardBusTapDependenciesInEffect_Type.__name__ = "OctetString"
_MscShelfCardBusTapDependenciesInEffect_Object = MibTableColumn
mscShelfCardBusTapDependenciesInEffect = _MscShelfCardBusTapDependenciesInEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 11, 1, 2),
    _MscShelfCardBusTapDependenciesInEffect_Type()
)
mscShelfCardBusTapDependenciesInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapDependenciesInEffect.setStatus("mandatory")


class _MscShelfCardBusTapCardsAvailable_Type(OctetString):
    """Custom type mscShelfCardBusTapCardsAvailable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfCardBusTapCardsAvailable_Type.__name__ = "OctetString"
_MscShelfCardBusTapCardsAvailable_Object = MibTableColumn
mscShelfCardBusTapCardsAvailable = _MscShelfCardBusTapCardsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 11, 1, 3),
    _MscShelfCardBusTapCardsAvailable_Type()
)
mscShelfCardBusTapCardsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapCardsAvailable.setStatus("mandatory")


class _MscShelfCardBusTapCardsTxTo_Type(OctetString):
    """Custom type mscShelfCardBusTapCardsTxTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfCardBusTapCardsTxTo_Type.__name__ = "OctetString"
_MscShelfCardBusTapCardsTxTo_Object = MibTableColumn
mscShelfCardBusTapCardsTxTo = _MscShelfCardBusTapCardsTxTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 11, 1, 4),
    _MscShelfCardBusTapCardsTxTo_Type()
)
mscShelfCardBusTapCardsTxTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapCardsTxTo.setStatus("mandatory")
_MscShelfCardBusTapErrorsTable_Object = MibTable
mscShelfCardBusTapErrorsTable = _MscShelfCardBusTapErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mscShelfCardBusTapErrorsTable.setStatus("mandatory")
_MscShelfCardBusTapErrorsEntry_Object = MibTableRow
mscShelfCardBusTapErrorsEntry = _MscShelfCardBusTapErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1)
)
mscShelfCardBusTapErrorsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfCardBusTapIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardBusTapErrorsEntry.setStatus("mandatory")


class _MscShelfCardBusTapSelfTestErrorCode_Type(Unsigned32):
    """Custom type mscShelfCardBusTapSelfTestErrorCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardBusTapSelfTestErrorCode_Type.__name__ = "Unsigned32"
_MscShelfCardBusTapSelfTestErrorCode_Object = MibTableColumn
mscShelfCardBusTapSelfTestErrorCode = _MscShelfCardBusTapSelfTestErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1, 1),
    _MscShelfCardBusTapSelfTestErrorCode_Type()
)
mscShelfCardBusTapSelfTestErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapSelfTestErrorCode.setStatus("mandatory")


class _MscShelfCardBusTapClockErrors_Type(Unsigned32):
    """Custom type mscShelfCardBusTapClockErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardBusTapClockErrors_Type.__name__ = "Unsigned32"
_MscShelfCardBusTapClockErrors_Object = MibTableColumn
mscShelfCardBusTapClockErrors = _MscShelfCardBusTapClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1, 2),
    _MscShelfCardBusTapClockErrors_Type()
)
mscShelfCardBusTapClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapClockErrors.setStatus("mandatory")


class _MscShelfCardBusTapEndOfCellErrors_Type(Unsigned32):
    """Custom type mscShelfCardBusTapEndOfCellErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardBusTapEndOfCellErrors_Type.__name__ = "Unsigned32"
_MscShelfCardBusTapEndOfCellErrors_Object = MibTableColumn
mscShelfCardBusTapEndOfCellErrors = _MscShelfCardBusTapEndOfCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1, 3),
    _MscShelfCardBusTapEndOfCellErrors_Type()
)
mscShelfCardBusTapEndOfCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapEndOfCellErrors.setStatus("mandatory")


class _MscShelfCardBusTapParityErrors_Type(Unsigned32):
    """Custom type mscShelfCardBusTapParityErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardBusTapParityErrors_Type.__name__ = "Unsigned32"
_MscShelfCardBusTapParityErrors_Object = MibTableColumn
mscShelfCardBusTapParityErrors = _MscShelfCardBusTapParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1, 4),
    _MscShelfCardBusTapParityErrors_Type()
)
mscShelfCardBusTapParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapParityErrors.setStatus("mandatory")


class _MscShelfCardBusTapFrmCongestionErrors_Type(Unsigned32):
    """Custom type mscShelfCardBusTapFrmCongestionErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardBusTapFrmCongestionErrors_Type.__name__ = "Unsigned32"
_MscShelfCardBusTapFrmCongestionErrors_Object = MibTableColumn
mscShelfCardBusTapFrmCongestionErrors = _MscShelfCardBusTapFrmCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1, 5),
    _MscShelfCardBusTapFrmCongestionErrors_Type()
)
mscShelfCardBusTapFrmCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapFrmCongestionErrors.setStatus("mandatory")


class _MscShelfCardBusTapFrmCollisionErrors_Type(Unsigned32):
    """Custom type mscShelfCardBusTapFrmCollisionErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardBusTapFrmCollisionErrors_Type.__name__ = "Unsigned32"
_MscShelfCardBusTapFrmCollisionErrors_Object = MibTableColumn
mscShelfCardBusTapFrmCollisionErrors = _MscShelfCardBusTapFrmCollisionErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1, 6),
    _MscShelfCardBusTapFrmCollisionErrors_Type()
)
mscShelfCardBusTapFrmCollisionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapFrmCollisionErrors.setStatus("mandatory")


class _MscShelfCardBusTapFrmTimeoutErrors_Type(Unsigned32):
    """Custom type mscShelfCardBusTapFrmTimeoutErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardBusTapFrmTimeoutErrors_Type.__name__ = "Unsigned32"
_MscShelfCardBusTapFrmTimeoutErrors_Object = MibTableColumn
mscShelfCardBusTapFrmTimeoutErrors = _MscShelfCardBusTapFrmTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1, 7),
    _MscShelfCardBusTapFrmTimeoutErrors_Type()
)
mscShelfCardBusTapFrmTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapFrmTimeoutErrors.setStatus("mandatory")


class _MscShelfCardBusTapFrmDeliveryErrors_Type(Unsigned32):
    """Custom type mscShelfCardBusTapFrmDeliveryErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardBusTapFrmDeliveryErrors_Type.__name__ = "Unsigned32"
_MscShelfCardBusTapFrmDeliveryErrors_Object = MibTableColumn
mscShelfCardBusTapFrmDeliveryErrors = _MscShelfCardBusTapFrmDeliveryErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1, 8),
    _MscShelfCardBusTapFrmDeliveryErrors_Type()
)
mscShelfCardBusTapFrmDeliveryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapFrmDeliveryErrors.setStatus("mandatory")


class _MscShelfCardBusTapFrmSizeErrors_Type(Unsigned32):
    """Custom type mscShelfCardBusTapFrmSizeErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardBusTapFrmSizeErrors_Type.__name__ = "Unsigned32"
_MscShelfCardBusTapFrmSizeErrors_Object = MibTableColumn
mscShelfCardBusTapFrmSizeErrors = _MscShelfCardBusTapFrmSizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 2, 12, 1, 9),
    _MscShelfCardBusTapFrmSizeErrors_Type()
)
mscShelfCardBusTapFrmSizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardBusTapFrmSizeErrors.setStatus("mandatory")
_MscShelfBus_ObjectIdentity = ObjectIdentity
mscShelfBus = _MscShelfBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3)
)
_MscShelfBusRowStatusTable_Object = MibTable
mscShelfBusRowStatusTable = _MscShelfBusRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    mscShelfBusRowStatusTable.setStatus("mandatory")
_MscShelfBusRowStatusEntry_Object = MibTableRow
mscShelfBusRowStatusEntry = _MscShelfBusRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 1, 1)
)
mscShelfBusRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusRowStatusEntry.setStatus("mandatory")
_MscShelfBusRowStatus_Type = RowStatus
_MscShelfBusRowStatus_Object = MibTableColumn
mscShelfBusRowStatus = _MscShelfBusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 1, 1, 1),
    _MscShelfBusRowStatus_Type()
)
mscShelfBusRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusRowStatus.setStatus("mandatory")
_MscShelfBusComponentName_Type = DisplayString
_MscShelfBusComponentName_Object = MibTableColumn
mscShelfBusComponentName = _MscShelfBusComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 1, 1, 2),
    _MscShelfBusComponentName_Type()
)
mscShelfBusComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusComponentName.setStatus("mandatory")
_MscShelfBusStorageType_Type = StorageType
_MscShelfBusStorageType_Object = MibTableColumn
mscShelfBusStorageType = _MscShelfBusStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 1, 1, 4),
    _MscShelfBusStorageType_Type()
)
mscShelfBusStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusStorageType.setStatus("mandatory")


class _MscShelfBusIndex_Type(Integer32):
    """Custom type mscShelfBusIndex based on Integer32"""
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


_MscShelfBusIndex_Type.__name__ = "Integer32"
_MscShelfBusIndex_Object = MibTableColumn
mscShelfBusIndex = _MscShelfBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 1, 1, 10),
    _MscShelfBusIndex_Type()
)
mscShelfBusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusIndex.setStatus("mandatory")
_MscShelfBusTest_ObjectIdentity = ObjectIdentity
mscShelfBusTest = _MscShelfBusTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2)
)
_MscShelfBusTestRowStatusTable_Object = MibTable
mscShelfBusTestRowStatusTable = _MscShelfBusTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscShelfBusTestRowStatusTable.setStatus("mandatory")
_MscShelfBusTestRowStatusEntry_Object = MibTableRow
mscShelfBusTestRowStatusEntry = _MscShelfBusTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 1, 1)
)
mscShelfBusTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusTestRowStatusEntry.setStatus("mandatory")
_MscShelfBusTestRowStatus_Type = RowStatus
_MscShelfBusTestRowStatus_Object = MibTableColumn
mscShelfBusTestRowStatus = _MscShelfBusTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 1, 1, 1),
    _MscShelfBusTestRowStatus_Type()
)
mscShelfBusTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestRowStatus.setStatus("mandatory")
_MscShelfBusTestComponentName_Type = DisplayString
_MscShelfBusTestComponentName_Object = MibTableColumn
mscShelfBusTestComponentName = _MscShelfBusTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 1, 1, 2),
    _MscShelfBusTestComponentName_Type()
)
mscShelfBusTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestComponentName.setStatus("mandatory")
_MscShelfBusTestStorageType_Type = StorageType
_MscShelfBusTestStorageType_Object = MibTableColumn
mscShelfBusTestStorageType = _MscShelfBusTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 1, 1, 4),
    _MscShelfBusTestStorageType_Type()
)
mscShelfBusTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestStorageType.setStatus("mandatory")
_MscShelfBusTestIndex_Type = NonReplicated
_MscShelfBusTestIndex_Object = MibTableColumn
mscShelfBusTestIndex = _MscShelfBusTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 1, 1, 10),
    _MscShelfBusTestIndex_Type()
)
mscShelfBusTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestIndex.setStatus("mandatory")
_MscShelfBusTestStateTable_Object = MibTable
mscShelfBusTestStateTable = _MscShelfBusTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscShelfBusTestStateTable.setStatus("mandatory")
_MscShelfBusTestStateEntry_Object = MibTableRow
mscShelfBusTestStateEntry = _MscShelfBusTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 10, 1)
)
mscShelfBusTestStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusTestStateEntry.setStatus("mandatory")


class _MscShelfBusTestAdminState_Type(Integer32):
    """Custom type mscShelfBusTestAdminState based on Integer32"""
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


_MscShelfBusTestAdminState_Type.__name__ = "Integer32"
_MscShelfBusTestAdminState_Object = MibTableColumn
mscShelfBusTestAdminState = _MscShelfBusTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 10, 1, 1),
    _MscShelfBusTestAdminState_Type()
)
mscShelfBusTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestAdminState.setStatus("mandatory")


class _MscShelfBusTestOperationalState_Type(Integer32):
    """Custom type mscShelfBusTestOperationalState based on Integer32"""
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


_MscShelfBusTestOperationalState_Type.__name__ = "Integer32"
_MscShelfBusTestOperationalState_Object = MibTableColumn
mscShelfBusTestOperationalState = _MscShelfBusTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 10, 1, 2),
    _MscShelfBusTestOperationalState_Type()
)
mscShelfBusTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestOperationalState.setStatus("mandatory")


class _MscShelfBusTestUsageState_Type(Integer32):
    """Custom type mscShelfBusTestUsageState based on Integer32"""
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


_MscShelfBusTestUsageState_Type.__name__ = "Integer32"
_MscShelfBusTestUsageState_Object = MibTableColumn
mscShelfBusTestUsageState = _MscShelfBusTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 10, 1, 3),
    _MscShelfBusTestUsageState_Type()
)
mscShelfBusTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestUsageState.setStatus("mandatory")
_MscShelfBusTestSetupTable_Object = MibTable
mscShelfBusTestSetupTable = _MscShelfBusTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 11)
)
if mibBuilder.loadTexts:
    mscShelfBusTestSetupTable.setStatus("mandatory")
_MscShelfBusTestSetupEntry_Object = MibTableRow
mscShelfBusTestSetupEntry = _MscShelfBusTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 11, 1)
)
mscShelfBusTestSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusTestSetupEntry.setStatus("mandatory")


class _MscShelfBusTestDuration_Type(Unsigned32):
    """Custom type mscShelfBusTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 43200),
    )


_MscShelfBusTestDuration_Type.__name__ = "Unsigned32"
_MscShelfBusTestDuration_Object = MibTableColumn
mscShelfBusTestDuration = _MscShelfBusTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 11, 1, 1),
    _MscShelfBusTestDuration_Type()
)
mscShelfBusTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfBusTestDuration.setStatus("mandatory")
_MscShelfBusTestResultsTable_Object = MibTable
mscShelfBusTestResultsTable = _MscShelfBusTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 12)
)
if mibBuilder.loadTexts:
    mscShelfBusTestResultsTable.setStatus("mandatory")
_MscShelfBusTestResultsEntry_Object = MibTableRow
mscShelfBusTestResultsEntry = _MscShelfBusTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 12, 1)
)
mscShelfBusTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusTestResultsEntry.setStatus("mandatory")


class _MscShelfBusTestElapsedTime_Type(Unsigned32):
    """Custom type mscShelfBusTestElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_MscShelfBusTestElapsedTime_Type.__name__ = "Unsigned32"
_MscShelfBusTestElapsedTime_Object = MibTableColumn
mscShelfBusTestElapsedTime = _MscShelfBusTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 12, 1, 1),
    _MscShelfBusTestElapsedTime_Type()
)
mscShelfBusTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestElapsedTime.setStatus("mandatory")


class _MscShelfBusTestTimeRemaining_Type(Unsigned32):
    """Custom type mscShelfBusTestTimeRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_MscShelfBusTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscShelfBusTestTimeRemaining_Object = MibTableColumn
mscShelfBusTestTimeRemaining = _MscShelfBusTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 12, 1, 2),
    _MscShelfBusTestTimeRemaining_Type()
)
mscShelfBusTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestTimeRemaining.setStatus("mandatory")


class _MscShelfBusTestCauseOfTermination_Type(Integer32):
    """Custom type mscShelfBusTestCauseOfTermination based on Integer32"""
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


_MscShelfBusTestCauseOfTermination_Type.__name__ = "Integer32"
_MscShelfBusTestCauseOfTermination_Object = MibTableColumn
mscShelfBusTestCauseOfTermination = _MscShelfBusTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 12, 1, 3),
    _MscShelfBusTestCauseOfTermination_Type()
)
mscShelfBusTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestCauseOfTermination.setStatus("mandatory")


class _MscShelfBusTestTestsDone_Type(OctetString):
    """Custom type mscShelfBusTestTestsDone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfBusTestTestsDone_Type.__name__ = "OctetString"
_MscShelfBusTestTestsDone_Object = MibTableColumn
mscShelfBusTestTestsDone = _MscShelfBusTestTestsDone_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 12, 1, 4),
    _MscShelfBusTestTestsDone_Type()
)
mscShelfBusTestTestsDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestTestsDone.setStatus("mandatory")
_MscShelfBusTestSelfTestResultsTable_Object = MibTable
mscShelfBusTestSelfTestResultsTable = _MscShelfBusTestSelfTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 248)
)
if mibBuilder.loadTexts:
    mscShelfBusTestSelfTestResultsTable.setStatus("mandatory")
_MscShelfBusTestSelfTestResultsEntry_Object = MibTableRow
mscShelfBusTestSelfTestResultsEntry = _MscShelfBusTestSelfTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 248, 1)
)
mscShelfBusTestSelfTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestSelfTestResultsIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusTestSelfTestResultsEntry.setStatus("mandatory")


class _MscShelfBusTestSelfTestResultsIndex_Type(Integer32):
    """Custom type mscShelfBusTestSelfTestResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfBusTestSelfTestResultsIndex_Type.__name__ = "Integer32"
_MscShelfBusTestSelfTestResultsIndex_Object = MibTableColumn
mscShelfBusTestSelfTestResultsIndex = _MscShelfBusTestSelfTestResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 248, 1, 1),
    _MscShelfBusTestSelfTestResultsIndex_Type()
)
mscShelfBusTestSelfTestResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestSelfTestResultsIndex.setStatus("mandatory")


class _MscShelfBusTestSelfTestResultsValue_Type(Integer32):
    """Custom type mscShelfBusTestSelfTestResultsValue based on Integer32"""
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


_MscShelfBusTestSelfTestResultsValue_Type.__name__ = "Integer32"
_MscShelfBusTestSelfTestResultsValue_Object = MibTableColumn
mscShelfBusTestSelfTestResultsValue = _MscShelfBusTestSelfTestResultsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 248, 1, 2),
    _MscShelfBusTestSelfTestResultsValue_Type()
)
mscShelfBusTestSelfTestResultsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestSelfTestResultsValue.setStatus("mandatory")
_MscShelfBusTestClockSourceTestResultsTable_Object = MibTable
mscShelfBusTestClockSourceTestResultsTable = _MscShelfBusTestClockSourceTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 249)
)
if mibBuilder.loadTexts:
    mscShelfBusTestClockSourceTestResultsTable.setStatus("mandatory")
_MscShelfBusTestClockSourceTestResultsEntry_Object = MibTableRow
mscShelfBusTestClockSourceTestResultsEntry = _MscShelfBusTestClockSourceTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 249, 1)
)
mscShelfBusTestClockSourceTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestClockSourceTestResultsSourceIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestClockSourceTestResultsCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusTestClockSourceTestResultsEntry.setStatus("mandatory")


class _MscShelfBusTestClockSourceTestResultsSourceIndex_Type(Integer32):
    """Custom type mscShelfBusTestClockSourceTestResultsSourceIndex based on Integer32"""
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


_MscShelfBusTestClockSourceTestResultsSourceIndex_Type.__name__ = "Integer32"
_MscShelfBusTestClockSourceTestResultsSourceIndex_Object = MibTableColumn
mscShelfBusTestClockSourceTestResultsSourceIndex = _MscShelfBusTestClockSourceTestResultsSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 249, 1, 1),
    _MscShelfBusTestClockSourceTestResultsSourceIndex_Type()
)
mscShelfBusTestClockSourceTestResultsSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestClockSourceTestResultsSourceIndex.setStatus("mandatory")


class _MscShelfBusTestClockSourceTestResultsCardIndex_Type(Integer32):
    """Custom type mscShelfBusTestClockSourceTestResultsCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfBusTestClockSourceTestResultsCardIndex_Type.__name__ = "Integer32"
_MscShelfBusTestClockSourceTestResultsCardIndex_Object = MibTableColumn
mscShelfBusTestClockSourceTestResultsCardIndex = _MscShelfBusTestClockSourceTestResultsCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 249, 1, 2),
    _MscShelfBusTestClockSourceTestResultsCardIndex_Type()
)
mscShelfBusTestClockSourceTestResultsCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestClockSourceTestResultsCardIndex.setStatus("mandatory")


class _MscShelfBusTestClockSourceTestResultsValue_Type(Integer32):
    """Custom type mscShelfBusTestClockSourceTestResultsValue based on Integer32"""
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


_MscShelfBusTestClockSourceTestResultsValue_Type.__name__ = "Integer32"
_MscShelfBusTestClockSourceTestResultsValue_Object = MibTableColumn
mscShelfBusTestClockSourceTestResultsValue = _MscShelfBusTestClockSourceTestResultsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 249, 1, 3),
    _MscShelfBusTestClockSourceTestResultsValue_Type()
)
mscShelfBusTestClockSourceTestResultsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestClockSourceTestResultsValue.setStatus("mandatory")
_MscShelfBusTestBroadcastTestResultsTable_Object = MibTable
mscShelfBusTestBroadcastTestResultsTable = _MscShelfBusTestBroadcastTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 250)
)
if mibBuilder.loadTexts:
    mscShelfBusTestBroadcastTestResultsTable.setStatus("mandatory")
_MscShelfBusTestBroadcastTestResultsEntry_Object = MibTableRow
mscShelfBusTestBroadcastTestResultsEntry = _MscShelfBusTestBroadcastTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 250, 1)
)
mscShelfBusTestBroadcastTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestBroadcastTestResultsTxCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestBroadcastTestResultsRxCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusTestBroadcastTestResultsEntry.setStatus("mandatory")


class _MscShelfBusTestBroadcastTestResultsTxCardIndex_Type(Integer32):
    """Custom type mscShelfBusTestBroadcastTestResultsTxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfBusTestBroadcastTestResultsTxCardIndex_Type.__name__ = "Integer32"
_MscShelfBusTestBroadcastTestResultsTxCardIndex_Object = MibTableColumn
mscShelfBusTestBroadcastTestResultsTxCardIndex = _MscShelfBusTestBroadcastTestResultsTxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 250, 1, 1),
    _MscShelfBusTestBroadcastTestResultsTxCardIndex_Type()
)
mscShelfBusTestBroadcastTestResultsTxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestBroadcastTestResultsTxCardIndex.setStatus("mandatory")


class _MscShelfBusTestBroadcastTestResultsRxCardIndex_Type(Integer32):
    """Custom type mscShelfBusTestBroadcastTestResultsRxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfBusTestBroadcastTestResultsRxCardIndex_Type.__name__ = "Integer32"
_MscShelfBusTestBroadcastTestResultsRxCardIndex_Object = MibTableColumn
mscShelfBusTestBroadcastTestResultsRxCardIndex = _MscShelfBusTestBroadcastTestResultsRxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 250, 1, 2),
    _MscShelfBusTestBroadcastTestResultsRxCardIndex_Type()
)
mscShelfBusTestBroadcastTestResultsRxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestBroadcastTestResultsRxCardIndex.setStatus("mandatory")


class _MscShelfBusTestBroadcastTestResultsValue_Type(Integer32):
    """Custom type mscShelfBusTestBroadcastTestResultsValue based on Integer32"""
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


_MscShelfBusTestBroadcastTestResultsValue_Type.__name__ = "Integer32"
_MscShelfBusTestBroadcastTestResultsValue_Object = MibTableColumn
mscShelfBusTestBroadcastTestResultsValue = _MscShelfBusTestBroadcastTestResultsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 250, 1, 3),
    _MscShelfBusTestBroadcastTestResultsValue_Type()
)
mscShelfBusTestBroadcastTestResultsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestBroadcastTestResultsValue.setStatus("mandatory")
_MscShelfBusTestPingTestsTable_Object = MibTable
mscShelfBusTestPingTestsTable = _MscShelfBusTestPingTestsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 251)
)
if mibBuilder.loadTexts:
    mscShelfBusTestPingTestsTable.setStatus("mandatory")
_MscShelfBusTestPingTestsEntry_Object = MibTableRow
mscShelfBusTestPingTestsEntry = _MscShelfBusTestPingTestsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 251, 1)
)
mscShelfBusTestPingTestsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestPingTestsTxCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestPingTestsRxCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusTestPingTestsEntry.setStatus("mandatory")


class _MscShelfBusTestPingTestsTxCardIndex_Type(Integer32):
    """Custom type mscShelfBusTestPingTestsTxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfBusTestPingTestsTxCardIndex_Type.__name__ = "Integer32"
_MscShelfBusTestPingTestsTxCardIndex_Object = MibTableColumn
mscShelfBusTestPingTestsTxCardIndex = _MscShelfBusTestPingTestsTxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 251, 1, 1),
    _MscShelfBusTestPingTestsTxCardIndex_Type()
)
mscShelfBusTestPingTestsTxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestPingTestsTxCardIndex.setStatus("mandatory")


class _MscShelfBusTestPingTestsRxCardIndex_Type(Integer32):
    """Custom type mscShelfBusTestPingTestsRxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfBusTestPingTestsRxCardIndex_Type.__name__ = "Integer32"
_MscShelfBusTestPingTestsRxCardIndex_Object = MibTableColumn
mscShelfBusTestPingTestsRxCardIndex = _MscShelfBusTestPingTestsRxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 251, 1, 2),
    _MscShelfBusTestPingTestsRxCardIndex_Type()
)
mscShelfBusTestPingTestsRxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestPingTestsRxCardIndex.setStatus("mandatory")


class _MscShelfBusTestPingTestsValue_Type(Unsigned32):
    """Custom type mscShelfBusTestPingTestsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfBusTestPingTestsValue_Type.__name__ = "Unsigned32"
_MscShelfBusTestPingTestsValue_Object = MibTableColumn
mscShelfBusTestPingTestsValue = _MscShelfBusTestPingTestsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 251, 1, 3),
    _MscShelfBusTestPingTestsValue_Type()
)
mscShelfBusTestPingTestsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestPingTestsValue.setStatus("mandatory")
_MscShelfBusTestPingFailuresTable_Object = MibTable
mscShelfBusTestPingFailuresTable = _MscShelfBusTestPingFailuresTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 252)
)
if mibBuilder.loadTexts:
    mscShelfBusTestPingFailuresTable.setStatus("mandatory")
_MscShelfBusTestPingFailuresEntry_Object = MibTableRow
mscShelfBusTestPingFailuresEntry = _MscShelfBusTestPingFailuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 252, 1)
)
mscShelfBusTestPingFailuresEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestPingFailuresTxCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusTestPingFailuresRxCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusTestPingFailuresEntry.setStatus("mandatory")


class _MscShelfBusTestPingFailuresTxCardIndex_Type(Integer32):
    """Custom type mscShelfBusTestPingFailuresTxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfBusTestPingFailuresTxCardIndex_Type.__name__ = "Integer32"
_MscShelfBusTestPingFailuresTxCardIndex_Object = MibTableColumn
mscShelfBusTestPingFailuresTxCardIndex = _MscShelfBusTestPingFailuresTxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 252, 1, 1),
    _MscShelfBusTestPingFailuresTxCardIndex_Type()
)
mscShelfBusTestPingFailuresTxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestPingFailuresTxCardIndex.setStatus("mandatory")


class _MscShelfBusTestPingFailuresRxCardIndex_Type(Integer32):
    """Custom type mscShelfBusTestPingFailuresRxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfBusTestPingFailuresRxCardIndex_Type.__name__ = "Integer32"
_MscShelfBusTestPingFailuresRxCardIndex_Object = MibTableColumn
mscShelfBusTestPingFailuresRxCardIndex = _MscShelfBusTestPingFailuresRxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 252, 1, 2),
    _MscShelfBusTestPingFailuresRxCardIndex_Type()
)
mscShelfBusTestPingFailuresRxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusTestPingFailuresRxCardIndex.setStatus("mandatory")


class _MscShelfBusTestPingFailuresValue_Type(Unsigned32):
    """Custom type mscShelfBusTestPingFailuresValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfBusTestPingFailuresValue_Type.__name__ = "Unsigned32"
_MscShelfBusTestPingFailuresValue_Object = MibTableColumn
mscShelfBusTestPingFailuresValue = _MscShelfBusTestPingFailuresValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 2, 252, 1, 3),
    _MscShelfBusTestPingFailuresValue_Type()
)
mscShelfBusTestPingFailuresValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusTestPingFailuresValue.setStatus("mandatory")
_MscShelfBusStateTable_Object = MibTable
mscShelfBusStateTable = _MscShelfBusStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10)
)
if mibBuilder.loadTexts:
    mscShelfBusStateTable.setStatus("mandatory")
_MscShelfBusStateEntry_Object = MibTableRow
mscShelfBusStateEntry = _MscShelfBusStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1)
)
mscShelfBusStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusStateEntry.setStatus("mandatory")


class _MscShelfBusAdminState_Type(Integer32):
    """Custom type mscShelfBusAdminState based on Integer32"""
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


_MscShelfBusAdminState_Type.__name__ = "Integer32"
_MscShelfBusAdminState_Object = MibTableColumn
mscShelfBusAdminState = _MscShelfBusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1, 1),
    _MscShelfBusAdminState_Type()
)
mscShelfBusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusAdminState.setStatus("mandatory")


class _MscShelfBusOperationalState_Type(Integer32):
    """Custom type mscShelfBusOperationalState based on Integer32"""
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


_MscShelfBusOperationalState_Type.__name__ = "Integer32"
_MscShelfBusOperationalState_Object = MibTableColumn
mscShelfBusOperationalState = _MscShelfBusOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1, 2),
    _MscShelfBusOperationalState_Type()
)
mscShelfBusOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusOperationalState.setStatus("mandatory")


class _MscShelfBusUsageState_Type(Integer32):
    """Custom type mscShelfBusUsageState based on Integer32"""
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


_MscShelfBusUsageState_Type.__name__ = "Integer32"
_MscShelfBusUsageState_Object = MibTableColumn
mscShelfBusUsageState = _MscShelfBusUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1, 3),
    _MscShelfBusUsageState_Type()
)
mscShelfBusUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusUsageState.setStatus("mandatory")


class _MscShelfBusAvailabilityStatus_Type(OctetString):
    """Custom type mscShelfBusAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfBusAvailabilityStatus_Type.__name__ = "OctetString"
_MscShelfBusAvailabilityStatus_Object = MibTableColumn
mscShelfBusAvailabilityStatus = _MscShelfBusAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1, 4),
    _MscShelfBusAvailabilityStatus_Type()
)
mscShelfBusAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusAvailabilityStatus.setStatus("mandatory")


class _MscShelfBusProceduralStatus_Type(OctetString):
    """Custom type mscShelfBusProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfBusProceduralStatus_Type.__name__ = "OctetString"
_MscShelfBusProceduralStatus_Object = MibTableColumn
mscShelfBusProceduralStatus = _MscShelfBusProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1, 5),
    _MscShelfBusProceduralStatus_Type()
)
mscShelfBusProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusProceduralStatus.setStatus("mandatory")


class _MscShelfBusControlStatus_Type(OctetString):
    """Custom type mscShelfBusControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfBusControlStatus_Type.__name__ = "OctetString"
_MscShelfBusControlStatus_Object = MibTableColumn
mscShelfBusControlStatus = _MscShelfBusControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1, 6),
    _MscShelfBusControlStatus_Type()
)
mscShelfBusControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusControlStatus.setStatus("mandatory")


class _MscShelfBusAlarmStatus_Type(OctetString):
    """Custom type mscShelfBusAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfBusAlarmStatus_Type.__name__ = "OctetString"
_MscShelfBusAlarmStatus_Object = MibTableColumn
mscShelfBusAlarmStatus = _MscShelfBusAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1, 7),
    _MscShelfBusAlarmStatus_Type()
)
mscShelfBusAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusAlarmStatus.setStatus("mandatory")


class _MscShelfBusStandbyStatus_Type(Integer32):
    """Custom type mscShelfBusStandbyStatus based on Integer32"""
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


_MscShelfBusStandbyStatus_Type.__name__ = "Integer32"
_MscShelfBusStandbyStatus_Object = MibTableColumn
mscShelfBusStandbyStatus = _MscShelfBusStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1, 8),
    _MscShelfBusStandbyStatus_Type()
)
mscShelfBusStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusStandbyStatus.setStatus("mandatory")


class _MscShelfBusUnknownStatus_Type(Integer32):
    """Custom type mscShelfBusUnknownStatus based on Integer32"""
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


_MscShelfBusUnknownStatus_Type.__name__ = "Integer32"
_MscShelfBusUnknownStatus_Object = MibTableColumn
mscShelfBusUnknownStatus = _MscShelfBusUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 10, 1, 9),
    _MscShelfBusUnknownStatus_Type()
)
mscShelfBusUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusUnknownStatus.setStatus("mandatory")
_MscShelfBusOperTable_Object = MibTable
mscShelfBusOperTable = _MscShelfBusOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 11)
)
if mibBuilder.loadTexts:
    mscShelfBusOperTable.setStatus("mandatory")
_MscShelfBusOperEntry_Object = MibTableRow
mscShelfBusOperEntry = _MscShelfBusOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 11, 1)
)
mscShelfBusOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusOperEntry.setStatus("mandatory")


class _MscShelfBusClockSource_Type(Integer32):
    """Custom type mscShelfBusClockSource based on Integer32"""
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


_MscShelfBusClockSource_Type.__name__ = "Integer32"
_MscShelfBusClockSource_Object = MibTableColumn
mscShelfBusClockSource = _MscShelfBusClockSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 11, 1, 1),
    _MscShelfBusClockSource_Type()
)
mscShelfBusClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusClockSource.setStatus("mandatory")


class _MscShelfBusUtilization_Type(Unsigned32):
    """Custom type mscShelfBusUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscShelfBusUtilization_Type.__name__ = "Unsigned32"
_MscShelfBusUtilization_Object = MibTableColumn
mscShelfBusUtilization = _MscShelfBusUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 11, 1, 2),
    _MscShelfBusUtilization_Type()
)
mscShelfBusUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusUtilization.setStatus("mandatory")
_MscShelfBusBusTapStatusTable_Object = MibTable
mscShelfBusBusTapStatusTable = _MscShelfBusBusTapStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 246)
)
if mibBuilder.loadTexts:
    mscShelfBusBusTapStatusTable.setStatus("mandatory")
_MscShelfBusBusTapStatusEntry_Object = MibTableRow
mscShelfBusBusTapStatusEntry = _MscShelfBusBusTapStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 246, 1)
)
mscShelfBusBusTapStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusBusTapStatusIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusBusTapStatusEntry.setStatus("mandatory")


class _MscShelfBusBusTapStatusIndex_Type(Integer32):
    """Custom type mscShelfBusBusTapStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfBusBusTapStatusIndex_Type.__name__ = "Integer32"
_MscShelfBusBusTapStatusIndex_Object = MibTableColumn
mscShelfBusBusTapStatusIndex = _MscShelfBusBusTapStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 246, 1, 1),
    _MscShelfBusBusTapStatusIndex_Type()
)
mscShelfBusBusTapStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusBusTapStatusIndex.setStatus("mandatory")


class _MscShelfBusBusTapStatusValue_Type(Integer32):
    """Custom type mscShelfBusBusTapStatusValue based on Integer32"""
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


_MscShelfBusBusTapStatusValue_Type.__name__ = "Integer32"
_MscShelfBusBusTapStatusValue_Object = MibTableColumn
mscShelfBusBusTapStatusValue = _MscShelfBusBusTapStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 246, 1, 2),
    _MscShelfBusBusTapStatusValue_Type()
)
mscShelfBusBusTapStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusBusTapStatusValue.setStatus("mandatory")
_MscShelfBusClockSourceStatusTable_Object = MibTable
mscShelfBusClockSourceStatusTable = _MscShelfBusClockSourceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 247)
)
if mibBuilder.loadTexts:
    mscShelfBusClockSourceStatusTable.setStatus("mandatory")
_MscShelfBusClockSourceStatusEntry_Object = MibTableRow
mscShelfBusClockSourceStatusEntry = _MscShelfBusClockSourceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 247, 1)
)
mscShelfBusClockSourceStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfBusClockSourceStatusIndex"),
)
if mibBuilder.loadTexts:
    mscShelfBusClockSourceStatusEntry.setStatus("mandatory")


class _MscShelfBusClockSourceStatusIndex_Type(Integer32):
    """Custom type mscShelfBusClockSourceStatusIndex based on Integer32"""
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


_MscShelfBusClockSourceStatusIndex_Type.__name__ = "Integer32"
_MscShelfBusClockSourceStatusIndex_Object = MibTableColumn
mscShelfBusClockSourceStatusIndex = _MscShelfBusClockSourceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 247, 1, 1),
    _MscShelfBusClockSourceStatusIndex_Type()
)
mscShelfBusClockSourceStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfBusClockSourceStatusIndex.setStatus("mandatory")


class _MscShelfBusClockSourceStatusValue_Type(Integer32):
    """Custom type mscShelfBusClockSourceStatusValue based on Integer32"""
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


_MscShelfBusClockSourceStatusValue_Type.__name__ = "Integer32"
_MscShelfBusClockSourceStatusValue_Object = MibTableColumn
mscShelfBusClockSourceStatusValue = _MscShelfBusClockSourceStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 3, 247, 1, 2),
    _MscShelfBusClockSourceStatusValue_Type()
)
mscShelfBusClockSourceStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfBusClockSourceStatusValue.setStatus("mandatory")
_MscShelfTest_ObjectIdentity = ObjectIdentity
mscShelfTest = _MscShelfTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4)
)
_MscShelfTestRowStatusTable_Object = MibTable
mscShelfTestRowStatusTable = _MscShelfTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 1)
)
if mibBuilder.loadTexts:
    mscShelfTestRowStatusTable.setStatus("mandatory")
_MscShelfTestRowStatusEntry_Object = MibTableRow
mscShelfTestRowStatusEntry = _MscShelfTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 1, 1)
)
mscShelfTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfTestRowStatusEntry.setStatus("mandatory")
_MscShelfTestRowStatus_Type = RowStatus
_MscShelfTestRowStatus_Object = MibTableColumn
mscShelfTestRowStatus = _MscShelfTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 1, 1, 1),
    _MscShelfTestRowStatus_Type()
)
mscShelfTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfTestRowStatus.setStatus("mandatory")
_MscShelfTestComponentName_Type = DisplayString
_MscShelfTestComponentName_Object = MibTableColumn
mscShelfTestComponentName = _MscShelfTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 1, 1, 2),
    _MscShelfTestComponentName_Type()
)
mscShelfTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfTestComponentName.setStatus("mandatory")
_MscShelfTestStorageType_Type = StorageType
_MscShelfTestStorageType_Object = MibTableColumn
mscShelfTestStorageType = _MscShelfTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 1, 1, 4),
    _MscShelfTestStorageType_Type()
)
mscShelfTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfTestStorageType.setStatus("mandatory")
_MscShelfTestIndex_Type = NonReplicated
_MscShelfTestIndex_Object = MibTableColumn
mscShelfTestIndex = _MscShelfTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 1, 1, 10),
    _MscShelfTestIndex_Type()
)
mscShelfTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfTestIndex.setStatus("mandatory")
_MscShelfTestProvTable_Object = MibTable
mscShelfTestProvTable = _MscShelfTestProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 10)
)
if mibBuilder.loadTexts:
    mscShelfTestProvTable.setStatus("mandatory")
_MscShelfTestProvEntry_Object = MibTableRow
mscShelfTestProvEntry = _MscShelfTestProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 10, 1)
)
mscShelfTestProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfTestProvEntry.setStatus("mandatory")


class _MscShelfTestAutomaticBusClockTest_Type(Integer32):
    """Custom type mscShelfTestAutomaticBusClockTest based on Integer32"""
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


_MscShelfTestAutomaticBusClockTest_Type.__name__ = "Integer32"
_MscShelfTestAutomaticBusClockTest_Object = MibTableColumn
mscShelfTestAutomaticBusClockTest = _MscShelfTestAutomaticBusClockTest_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 10, 1, 1),
    _MscShelfTestAutomaticBusClockTest_Type()
)
mscShelfTestAutomaticBusClockTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfTestAutomaticBusClockTest.setStatus("mandatory")
_MscShelfTestSetupTable_Object = MibTable
mscShelfTestSetupTable = _MscShelfTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 11)
)
if mibBuilder.loadTexts:
    mscShelfTestSetupTable.setStatus("mandatory")
_MscShelfTestSetupEntry_Object = MibTableRow
mscShelfTestSetupEntry = _MscShelfTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 11, 1)
)
mscShelfTestSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfTestSetupEntry.setStatus("mandatory")


class _MscShelfTestType_Type(Integer32):
    """Custom type mscShelfTestType based on Integer32"""
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


_MscShelfTestType_Type.__name__ = "Integer32"
_MscShelfTestType_Object = MibTableColumn
mscShelfTestType = _MscShelfTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 11, 1, 1),
    _MscShelfTestType_Type()
)
mscShelfTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfTestType.setStatus("mandatory")
_MscShelfTestResultsTable_Object = MibTable
mscShelfTestResultsTable = _MscShelfTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 12)
)
if mibBuilder.loadTexts:
    mscShelfTestResultsTable.setStatus("mandatory")
_MscShelfTestResultsEntry_Object = MibTableRow
mscShelfTestResultsEntry = _MscShelfTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 12, 1)
)
mscShelfTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BusMIB", "mscShelfTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfTestResultsEntry.setStatus("mandatory")


class _MscShelfTestBusClockTestResult_Type(Integer32):
    """Custom type mscShelfTestBusClockTestResult based on Integer32"""
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


_MscShelfTestBusClockTestResult_Type.__name__ = "Integer32"
_MscShelfTestBusClockTestResult_Object = MibTableColumn
mscShelfTestBusClockTestResult = _MscShelfTestBusClockTestResult_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 4, 12, 1, 1),
    _MscShelfTestBusClockTestResult_Type()
)
mscShelfTestBusClockTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfTestBusClockTestResult.setStatus("mandatory")
_BusMIB_ObjectIdentity = ObjectIdentity
busMIB = _BusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 144)
)
_BusGroup_ObjectIdentity = ObjectIdentity
busGroup = _BusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 144, 1)
)
_BusGroupCA_ObjectIdentity = ObjectIdentity
busGroupCA = _BusGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 144, 1, 1)
)
_BusGroupCA02_ObjectIdentity = ObjectIdentity
busGroupCA02 = _BusGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 144, 1, 1, 3)
)
_BusGroupCA02A_ObjectIdentity = ObjectIdentity
busGroupCA02A = _BusGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 144, 1, 1, 3, 2)
)
_BusCapabilities_ObjectIdentity = ObjectIdentity
busCapabilities = _BusCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 144, 3)
)
_BusCapabilitiesCA_ObjectIdentity = ObjectIdentity
busCapabilitiesCA = _BusCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 144, 3, 1)
)
_BusCapabilitiesCA02_ObjectIdentity = ObjectIdentity
busCapabilitiesCA02 = _BusCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 144, 3, 1, 3)
)
_BusCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
busCapabilitiesCA02A = _BusCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 144, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-BusMIB",
    **{"mscShelfCardBusTap": mscShelfCardBusTap,
       "mscShelfCardBusTapRowStatusTable": mscShelfCardBusTapRowStatusTable,
       "mscShelfCardBusTapRowStatusEntry": mscShelfCardBusTapRowStatusEntry,
       "mscShelfCardBusTapRowStatus": mscShelfCardBusTapRowStatus,
       "mscShelfCardBusTapComponentName": mscShelfCardBusTapComponentName,
       "mscShelfCardBusTapStorageType": mscShelfCardBusTapStorageType,
       "mscShelfCardBusTapIndex": mscShelfCardBusTapIndex,
       "mscShelfCardBusTapStateTable": mscShelfCardBusTapStateTable,
       "mscShelfCardBusTapStateEntry": mscShelfCardBusTapStateEntry,
       "mscShelfCardBusTapAdminState": mscShelfCardBusTapAdminState,
       "mscShelfCardBusTapOperationalState": mscShelfCardBusTapOperationalState,
       "mscShelfCardBusTapUsageState": mscShelfCardBusTapUsageState,
       "mscShelfCardBusTapAvailabilityStatus": mscShelfCardBusTapAvailabilityStatus,
       "mscShelfCardBusTapProceduralStatus": mscShelfCardBusTapProceduralStatus,
       "mscShelfCardBusTapControlStatus": mscShelfCardBusTapControlStatus,
       "mscShelfCardBusTapAlarmStatus": mscShelfCardBusTapAlarmStatus,
       "mscShelfCardBusTapStandbyStatus": mscShelfCardBusTapStandbyStatus,
       "mscShelfCardBusTapUnknownStatus": mscShelfCardBusTapUnknownStatus,
       "mscShelfCardBusTapOperTable": mscShelfCardBusTapOperTable,
       "mscShelfCardBusTapOperEntry": mscShelfCardBusTapOperEntry,
       "mscShelfCardBusTapFailuresInEffect": mscShelfCardBusTapFailuresInEffect,
       "mscShelfCardBusTapDependenciesInEffect": mscShelfCardBusTapDependenciesInEffect,
       "mscShelfCardBusTapCardsAvailable": mscShelfCardBusTapCardsAvailable,
       "mscShelfCardBusTapCardsTxTo": mscShelfCardBusTapCardsTxTo,
       "mscShelfCardBusTapErrorsTable": mscShelfCardBusTapErrorsTable,
       "mscShelfCardBusTapErrorsEntry": mscShelfCardBusTapErrorsEntry,
       "mscShelfCardBusTapSelfTestErrorCode": mscShelfCardBusTapSelfTestErrorCode,
       "mscShelfCardBusTapClockErrors": mscShelfCardBusTapClockErrors,
       "mscShelfCardBusTapEndOfCellErrors": mscShelfCardBusTapEndOfCellErrors,
       "mscShelfCardBusTapParityErrors": mscShelfCardBusTapParityErrors,
       "mscShelfCardBusTapFrmCongestionErrors": mscShelfCardBusTapFrmCongestionErrors,
       "mscShelfCardBusTapFrmCollisionErrors": mscShelfCardBusTapFrmCollisionErrors,
       "mscShelfCardBusTapFrmTimeoutErrors": mscShelfCardBusTapFrmTimeoutErrors,
       "mscShelfCardBusTapFrmDeliveryErrors": mscShelfCardBusTapFrmDeliveryErrors,
       "mscShelfCardBusTapFrmSizeErrors": mscShelfCardBusTapFrmSizeErrors,
       "mscShelfBus": mscShelfBus,
       "mscShelfBusRowStatusTable": mscShelfBusRowStatusTable,
       "mscShelfBusRowStatusEntry": mscShelfBusRowStatusEntry,
       "mscShelfBusRowStatus": mscShelfBusRowStatus,
       "mscShelfBusComponentName": mscShelfBusComponentName,
       "mscShelfBusStorageType": mscShelfBusStorageType,
       "mscShelfBusIndex": mscShelfBusIndex,
       "mscShelfBusTest": mscShelfBusTest,
       "mscShelfBusTestRowStatusTable": mscShelfBusTestRowStatusTable,
       "mscShelfBusTestRowStatusEntry": mscShelfBusTestRowStatusEntry,
       "mscShelfBusTestRowStatus": mscShelfBusTestRowStatus,
       "mscShelfBusTestComponentName": mscShelfBusTestComponentName,
       "mscShelfBusTestStorageType": mscShelfBusTestStorageType,
       "mscShelfBusTestIndex": mscShelfBusTestIndex,
       "mscShelfBusTestStateTable": mscShelfBusTestStateTable,
       "mscShelfBusTestStateEntry": mscShelfBusTestStateEntry,
       "mscShelfBusTestAdminState": mscShelfBusTestAdminState,
       "mscShelfBusTestOperationalState": mscShelfBusTestOperationalState,
       "mscShelfBusTestUsageState": mscShelfBusTestUsageState,
       "mscShelfBusTestSetupTable": mscShelfBusTestSetupTable,
       "mscShelfBusTestSetupEntry": mscShelfBusTestSetupEntry,
       "mscShelfBusTestDuration": mscShelfBusTestDuration,
       "mscShelfBusTestResultsTable": mscShelfBusTestResultsTable,
       "mscShelfBusTestResultsEntry": mscShelfBusTestResultsEntry,
       "mscShelfBusTestElapsedTime": mscShelfBusTestElapsedTime,
       "mscShelfBusTestTimeRemaining": mscShelfBusTestTimeRemaining,
       "mscShelfBusTestCauseOfTermination": mscShelfBusTestCauseOfTermination,
       "mscShelfBusTestTestsDone": mscShelfBusTestTestsDone,
       "mscShelfBusTestSelfTestResultsTable": mscShelfBusTestSelfTestResultsTable,
       "mscShelfBusTestSelfTestResultsEntry": mscShelfBusTestSelfTestResultsEntry,
       "mscShelfBusTestSelfTestResultsIndex": mscShelfBusTestSelfTestResultsIndex,
       "mscShelfBusTestSelfTestResultsValue": mscShelfBusTestSelfTestResultsValue,
       "mscShelfBusTestClockSourceTestResultsTable": mscShelfBusTestClockSourceTestResultsTable,
       "mscShelfBusTestClockSourceTestResultsEntry": mscShelfBusTestClockSourceTestResultsEntry,
       "mscShelfBusTestClockSourceTestResultsSourceIndex": mscShelfBusTestClockSourceTestResultsSourceIndex,
       "mscShelfBusTestClockSourceTestResultsCardIndex": mscShelfBusTestClockSourceTestResultsCardIndex,
       "mscShelfBusTestClockSourceTestResultsValue": mscShelfBusTestClockSourceTestResultsValue,
       "mscShelfBusTestBroadcastTestResultsTable": mscShelfBusTestBroadcastTestResultsTable,
       "mscShelfBusTestBroadcastTestResultsEntry": mscShelfBusTestBroadcastTestResultsEntry,
       "mscShelfBusTestBroadcastTestResultsTxCardIndex": mscShelfBusTestBroadcastTestResultsTxCardIndex,
       "mscShelfBusTestBroadcastTestResultsRxCardIndex": mscShelfBusTestBroadcastTestResultsRxCardIndex,
       "mscShelfBusTestBroadcastTestResultsValue": mscShelfBusTestBroadcastTestResultsValue,
       "mscShelfBusTestPingTestsTable": mscShelfBusTestPingTestsTable,
       "mscShelfBusTestPingTestsEntry": mscShelfBusTestPingTestsEntry,
       "mscShelfBusTestPingTestsTxCardIndex": mscShelfBusTestPingTestsTxCardIndex,
       "mscShelfBusTestPingTestsRxCardIndex": mscShelfBusTestPingTestsRxCardIndex,
       "mscShelfBusTestPingTestsValue": mscShelfBusTestPingTestsValue,
       "mscShelfBusTestPingFailuresTable": mscShelfBusTestPingFailuresTable,
       "mscShelfBusTestPingFailuresEntry": mscShelfBusTestPingFailuresEntry,
       "mscShelfBusTestPingFailuresTxCardIndex": mscShelfBusTestPingFailuresTxCardIndex,
       "mscShelfBusTestPingFailuresRxCardIndex": mscShelfBusTestPingFailuresRxCardIndex,
       "mscShelfBusTestPingFailuresValue": mscShelfBusTestPingFailuresValue,
       "mscShelfBusStateTable": mscShelfBusStateTable,
       "mscShelfBusStateEntry": mscShelfBusStateEntry,
       "mscShelfBusAdminState": mscShelfBusAdminState,
       "mscShelfBusOperationalState": mscShelfBusOperationalState,
       "mscShelfBusUsageState": mscShelfBusUsageState,
       "mscShelfBusAvailabilityStatus": mscShelfBusAvailabilityStatus,
       "mscShelfBusProceduralStatus": mscShelfBusProceduralStatus,
       "mscShelfBusControlStatus": mscShelfBusControlStatus,
       "mscShelfBusAlarmStatus": mscShelfBusAlarmStatus,
       "mscShelfBusStandbyStatus": mscShelfBusStandbyStatus,
       "mscShelfBusUnknownStatus": mscShelfBusUnknownStatus,
       "mscShelfBusOperTable": mscShelfBusOperTable,
       "mscShelfBusOperEntry": mscShelfBusOperEntry,
       "mscShelfBusClockSource": mscShelfBusClockSource,
       "mscShelfBusUtilization": mscShelfBusUtilization,
       "mscShelfBusBusTapStatusTable": mscShelfBusBusTapStatusTable,
       "mscShelfBusBusTapStatusEntry": mscShelfBusBusTapStatusEntry,
       "mscShelfBusBusTapStatusIndex": mscShelfBusBusTapStatusIndex,
       "mscShelfBusBusTapStatusValue": mscShelfBusBusTapStatusValue,
       "mscShelfBusClockSourceStatusTable": mscShelfBusClockSourceStatusTable,
       "mscShelfBusClockSourceStatusEntry": mscShelfBusClockSourceStatusEntry,
       "mscShelfBusClockSourceStatusIndex": mscShelfBusClockSourceStatusIndex,
       "mscShelfBusClockSourceStatusValue": mscShelfBusClockSourceStatusValue,
       "mscShelfTest": mscShelfTest,
       "mscShelfTestRowStatusTable": mscShelfTestRowStatusTable,
       "mscShelfTestRowStatusEntry": mscShelfTestRowStatusEntry,
       "mscShelfTestRowStatus": mscShelfTestRowStatus,
       "mscShelfTestComponentName": mscShelfTestComponentName,
       "mscShelfTestStorageType": mscShelfTestStorageType,
       "mscShelfTestIndex": mscShelfTestIndex,
       "mscShelfTestProvTable": mscShelfTestProvTable,
       "mscShelfTestProvEntry": mscShelfTestProvEntry,
       "mscShelfTestAutomaticBusClockTest": mscShelfTestAutomaticBusClockTest,
       "mscShelfTestSetupTable": mscShelfTestSetupTable,
       "mscShelfTestSetupEntry": mscShelfTestSetupEntry,
       "mscShelfTestType": mscShelfTestType,
       "mscShelfTestResultsTable": mscShelfTestResultsTable,
       "mscShelfTestResultsEntry": mscShelfTestResultsEntry,
       "mscShelfTestBusClockTestResult": mscShelfTestBusClockTestResult,
       "busMIB": busMIB,
       "busGroup": busGroup,
       "busGroupCA": busGroupCA,
       "busGroupCA02": busGroupCA02,
       "busGroupCA02A": busGroupCA02A,
       "busCapabilities": busCapabilities,
       "busCapabilitiesCA": busCapabilitiesCA,
       "busCapabilitiesCA02": busCapabilitiesCA02,
       "busCapabilitiesCA02A": busCapabilitiesCA02A}
)
