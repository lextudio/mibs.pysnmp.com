# SNMP MIB module (Nortel-MsCarrier-MscPassport-FabricMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FabricMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:20 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 FixedPoint1,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint1",
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

_MscShelfCardFabricPort_ObjectIdentity = ObjectIdentity
mscShelfCardFabricPort = _MscShelfCardFabricPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5)
)
_MscShelfCardFabricPortRowStatusTable_Object = MibTable
mscShelfCardFabricPortRowStatusTable = _MscShelfCardFabricPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mscShelfCardFabricPortRowStatusTable.setStatus("mandatory")
_MscShelfCardFabricPortRowStatusEntry_Object = MibTableRow
mscShelfCardFabricPortRowStatusEntry = _MscShelfCardFabricPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 1, 1)
)
mscShelfCardFabricPortRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfCardFabricPortIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardFabricPortRowStatusEntry.setStatus("mandatory")
_MscShelfCardFabricPortRowStatus_Type = RowStatus
_MscShelfCardFabricPortRowStatus_Object = MibTableColumn
mscShelfCardFabricPortRowStatus = _MscShelfCardFabricPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 1, 1, 1),
    _MscShelfCardFabricPortRowStatus_Type()
)
mscShelfCardFabricPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortRowStatus.setStatus("mandatory")
_MscShelfCardFabricPortComponentName_Type = DisplayString
_MscShelfCardFabricPortComponentName_Object = MibTableColumn
mscShelfCardFabricPortComponentName = _MscShelfCardFabricPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 1, 1, 2),
    _MscShelfCardFabricPortComponentName_Type()
)
mscShelfCardFabricPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortComponentName.setStatus("mandatory")
_MscShelfCardFabricPortStorageType_Type = StorageType
_MscShelfCardFabricPortStorageType_Object = MibTableColumn
mscShelfCardFabricPortStorageType = _MscShelfCardFabricPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 1, 1, 4),
    _MscShelfCardFabricPortStorageType_Type()
)
mscShelfCardFabricPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortStorageType.setStatus("mandatory")


class _MscShelfCardFabricPortIndex_Type(Integer32):
    """Custom type mscShelfCardFabricPortIndex based on Integer32"""
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


_MscShelfCardFabricPortIndex_Type.__name__ = "Integer32"
_MscShelfCardFabricPortIndex_Object = MibTableColumn
mscShelfCardFabricPortIndex = _MscShelfCardFabricPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 1, 1, 10),
    _MscShelfCardFabricPortIndex_Type()
)
mscShelfCardFabricPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortIndex.setStatus("mandatory")
_MscShelfCardFabricPortStateTable_Object = MibTable
mscShelfCardFabricPortStateTable = _MscShelfCardFabricPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10)
)
if mibBuilder.loadTexts:
    mscShelfCardFabricPortStateTable.setStatus("mandatory")
_MscShelfCardFabricPortStateEntry_Object = MibTableRow
mscShelfCardFabricPortStateEntry = _MscShelfCardFabricPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1)
)
mscShelfCardFabricPortStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfCardFabricPortIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardFabricPortStateEntry.setStatus("mandatory")


class _MscShelfCardFabricPortAdminState_Type(Integer32):
    """Custom type mscShelfCardFabricPortAdminState based on Integer32"""
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


_MscShelfCardFabricPortAdminState_Type.__name__ = "Integer32"
_MscShelfCardFabricPortAdminState_Object = MibTableColumn
mscShelfCardFabricPortAdminState = _MscShelfCardFabricPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1, 1),
    _MscShelfCardFabricPortAdminState_Type()
)
mscShelfCardFabricPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortAdminState.setStatus("mandatory")


class _MscShelfCardFabricPortOperationalState_Type(Integer32):
    """Custom type mscShelfCardFabricPortOperationalState based on Integer32"""
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


_MscShelfCardFabricPortOperationalState_Type.__name__ = "Integer32"
_MscShelfCardFabricPortOperationalState_Object = MibTableColumn
mscShelfCardFabricPortOperationalState = _MscShelfCardFabricPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1, 2),
    _MscShelfCardFabricPortOperationalState_Type()
)
mscShelfCardFabricPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortOperationalState.setStatus("mandatory")


class _MscShelfCardFabricPortUsageState_Type(Integer32):
    """Custom type mscShelfCardFabricPortUsageState based on Integer32"""
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


_MscShelfCardFabricPortUsageState_Type.__name__ = "Integer32"
_MscShelfCardFabricPortUsageState_Object = MibTableColumn
mscShelfCardFabricPortUsageState = _MscShelfCardFabricPortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1, 3),
    _MscShelfCardFabricPortUsageState_Type()
)
mscShelfCardFabricPortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortUsageState.setStatus("mandatory")


class _MscShelfCardFabricPortAvailabilityStatus_Type(OctetString):
    """Custom type mscShelfCardFabricPortAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfCardFabricPortAvailabilityStatus_Type.__name__ = "OctetString"
_MscShelfCardFabricPortAvailabilityStatus_Object = MibTableColumn
mscShelfCardFabricPortAvailabilityStatus = _MscShelfCardFabricPortAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1, 4),
    _MscShelfCardFabricPortAvailabilityStatus_Type()
)
mscShelfCardFabricPortAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortAvailabilityStatus.setStatus("mandatory")


class _MscShelfCardFabricPortProceduralStatus_Type(OctetString):
    """Custom type mscShelfCardFabricPortProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardFabricPortProceduralStatus_Type.__name__ = "OctetString"
_MscShelfCardFabricPortProceduralStatus_Object = MibTableColumn
mscShelfCardFabricPortProceduralStatus = _MscShelfCardFabricPortProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1, 5),
    _MscShelfCardFabricPortProceduralStatus_Type()
)
mscShelfCardFabricPortProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortProceduralStatus.setStatus("mandatory")


class _MscShelfCardFabricPortControlStatus_Type(OctetString):
    """Custom type mscShelfCardFabricPortControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardFabricPortControlStatus_Type.__name__ = "OctetString"
_MscShelfCardFabricPortControlStatus_Object = MibTableColumn
mscShelfCardFabricPortControlStatus = _MscShelfCardFabricPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1, 6),
    _MscShelfCardFabricPortControlStatus_Type()
)
mscShelfCardFabricPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortControlStatus.setStatus("mandatory")


class _MscShelfCardFabricPortAlarmStatus_Type(OctetString):
    """Custom type mscShelfCardFabricPortAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardFabricPortAlarmStatus_Type.__name__ = "OctetString"
_MscShelfCardFabricPortAlarmStatus_Object = MibTableColumn
mscShelfCardFabricPortAlarmStatus = _MscShelfCardFabricPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1, 7),
    _MscShelfCardFabricPortAlarmStatus_Type()
)
mscShelfCardFabricPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortAlarmStatus.setStatus("mandatory")


class _MscShelfCardFabricPortStandbyStatus_Type(Integer32):
    """Custom type mscShelfCardFabricPortStandbyStatus based on Integer32"""
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


_MscShelfCardFabricPortStandbyStatus_Type.__name__ = "Integer32"
_MscShelfCardFabricPortStandbyStatus_Object = MibTableColumn
mscShelfCardFabricPortStandbyStatus = _MscShelfCardFabricPortStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1, 8),
    _MscShelfCardFabricPortStandbyStatus_Type()
)
mscShelfCardFabricPortStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortStandbyStatus.setStatus("mandatory")


class _MscShelfCardFabricPortUnknownStatus_Type(Integer32):
    """Custom type mscShelfCardFabricPortUnknownStatus based on Integer32"""
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


_MscShelfCardFabricPortUnknownStatus_Type.__name__ = "Integer32"
_MscShelfCardFabricPortUnknownStatus_Object = MibTableColumn
mscShelfCardFabricPortUnknownStatus = _MscShelfCardFabricPortUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 10, 1, 9),
    _MscShelfCardFabricPortUnknownStatus_Type()
)
mscShelfCardFabricPortUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortUnknownStatus.setStatus("mandatory")
_MscShelfCardFabricPortOperTable_Object = MibTable
mscShelfCardFabricPortOperTable = _MscShelfCardFabricPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 11)
)
if mibBuilder.loadTexts:
    mscShelfCardFabricPortOperTable.setStatus("mandatory")
_MscShelfCardFabricPortOperEntry_Object = MibTableRow
mscShelfCardFabricPortOperEntry = _MscShelfCardFabricPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 11, 1)
)
mscShelfCardFabricPortOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfCardFabricPortIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardFabricPortOperEntry.setStatus("mandatory")


class _MscShelfCardFabricPortFailuresInEffect_Type(OctetString):
    """Custom type mscShelfCardFabricPortFailuresInEffect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardFabricPortFailuresInEffect_Type.__name__ = "OctetString"
_MscShelfCardFabricPortFailuresInEffect_Object = MibTableColumn
mscShelfCardFabricPortFailuresInEffect = _MscShelfCardFabricPortFailuresInEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 11, 1, 1),
    _MscShelfCardFabricPortFailuresInEffect_Type()
)
mscShelfCardFabricPortFailuresInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortFailuresInEffect.setStatus("mandatory")


class _MscShelfCardFabricPortDependenciesInEffect_Type(OctetString):
    """Custom type mscShelfCardFabricPortDependenciesInEffect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfCardFabricPortDependenciesInEffect_Type.__name__ = "OctetString"
_MscShelfCardFabricPortDependenciesInEffect_Object = MibTableColumn
mscShelfCardFabricPortDependenciesInEffect = _MscShelfCardFabricPortDependenciesInEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 11, 1, 2),
    _MscShelfCardFabricPortDependenciesInEffect_Type()
)
mscShelfCardFabricPortDependenciesInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortDependenciesInEffect.setStatus("mandatory")


class _MscShelfCardFabricPortCardsAvailable_Type(OctetString):
    """Custom type mscShelfCardFabricPortCardsAvailable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfCardFabricPortCardsAvailable_Type.__name__ = "OctetString"
_MscShelfCardFabricPortCardsAvailable_Object = MibTableColumn
mscShelfCardFabricPortCardsAvailable = _MscShelfCardFabricPortCardsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 11, 1, 3),
    _MscShelfCardFabricPortCardsAvailable_Type()
)
mscShelfCardFabricPortCardsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortCardsAvailable.setStatus("mandatory")


class _MscShelfCardFabricPortCardsTxTo_Type(OctetString):
    """Custom type mscShelfCardFabricPortCardsTxTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfCardFabricPortCardsTxTo_Type.__name__ = "OctetString"
_MscShelfCardFabricPortCardsTxTo_Object = MibTableColumn
mscShelfCardFabricPortCardsTxTo = _MscShelfCardFabricPortCardsTxTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 11, 1, 4),
    _MscShelfCardFabricPortCardsTxTo_Type()
)
mscShelfCardFabricPortCardsTxTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortCardsTxTo.setStatus("mandatory")
_MscShelfCardFabricPortErrorsTable_Object = MibTable
mscShelfCardFabricPortErrorsTable = _MscShelfCardFabricPortErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 12)
)
if mibBuilder.loadTexts:
    mscShelfCardFabricPortErrorsTable.setStatus("mandatory")
_MscShelfCardFabricPortErrorsEntry_Object = MibTableRow
mscShelfCardFabricPortErrorsEntry = _MscShelfCardFabricPortErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 12, 1)
)
mscShelfCardFabricPortErrorsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfCardFabricPortIndex"),
)
if mibBuilder.loadTexts:
    mscShelfCardFabricPortErrorsEntry.setStatus("mandatory")


class _MscShelfCardFabricPortSelfTestErrorCode_Type(Unsigned32):
    """Custom type mscShelfCardFabricPortSelfTestErrorCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfCardFabricPortSelfTestErrorCode_Type.__name__ = "Unsigned32"
_MscShelfCardFabricPortSelfTestErrorCode_Object = MibTableColumn
mscShelfCardFabricPortSelfTestErrorCode = _MscShelfCardFabricPortSelfTestErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 12, 1, 1),
    _MscShelfCardFabricPortSelfTestErrorCode_Type()
)
mscShelfCardFabricPortSelfTestErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortSelfTestErrorCode.setStatus("mandatory")
_MscShelfCardFabricPortLivelinessErrors_Type = Counter32
_MscShelfCardFabricPortLivelinessErrors_Object = MibTableColumn
mscShelfCardFabricPortLivelinessErrors = _MscShelfCardFabricPortLivelinessErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 12, 1, 7),
    _MscShelfCardFabricPortLivelinessErrors_Type()
)
mscShelfCardFabricPortLivelinessErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortLivelinessErrors.setStatus("mandatory")
_MscShelfCardFabricPortSwitchClockErrors_Type = Counter32
_MscShelfCardFabricPortSwitchClockErrors_Object = MibTableColumn
mscShelfCardFabricPortSwitchClockErrors = _MscShelfCardFabricPortSwitchClockErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 12, 1, 9),
    _MscShelfCardFabricPortSwitchClockErrors_Type()
)
mscShelfCardFabricPortSwitchClockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortSwitchClockErrors.setStatus("mandatory")
_MscShelfCardFabricPortPortHardwareErrors_Type = Counter32
_MscShelfCardFabricPortPortHardwareErrors_Object = MibTableColumn
mscShelfCardFabricPortPortHardwareErrors = _MscShelfCardFabricPortPortHardwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 12, 1, 18),
    _MscShelfCardFabricPortPortHardwareErrors_Type()
)
mscShelfCardFabricPortPortHardwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortPortHardwareErrors.setStatus("mandatory")
_MscShelfCardFabricPortPortProtocolErrors_Type = Counter32
_MscShelfCardFabricPortPortProtocolErrors_Object = MibTableColumn
mscShelfCardFabricPortPortProtocolErrors = _MscShelfCardFabricPortPortProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 12, 1, 19),
    _MscShelfCardFabricPortPortProtocolErrors_Type()
)
mscShelfCardFabricPortPortProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortPortProtocolErrors.setStatus("mandatory")
_MscShelfCardFabricPortDataCorruptionErrors_Type = Counter32
_MscShelfCardFabricPortDataCorruptionErrors_Object = MibTableColumn
mscShelfCardFabricPortDataCorruptionErrors = _MscShelfCardFabricPortDataCorruptionErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 12, 1, 20),
    _MscShelfCardFabricPortDataCorruptionErrors_Type()
)
mscShelfCardFabricPortDataCorruptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortDataCorruptionErrors.setStatus("mandatory")
_MscShelfCardFabricPortLinkLivelinessErrors_Type = Counter32
_MscShelfCardFabricPortLinkLivelinessErrors_Object = MibTableColumn
mscShelfCardFabricPortLinkLivelinessErrors = _MscShelfCardFabricPortLinkLivelinessErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 2, 5, 12, 1, 21),
    _MscShelfCardFabricPortLinkLivelinessErrors_Type()
)
mscShelfCardFabricPortLinkLivelinessErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfCardFabricPortLinkLivelinessErrors.setStatus("mandatory")
_MscShelfFabricCard_ObjectIdentity = ObjectIdentity
mscShelfFabricCard = _MscShelfFabricCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5)
)
_MscShelfFabricCardRowStatusTable_Object = MibTable
mscShelfFabricCardRowStatusTable = _MscShelfFabricCardRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 1)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardRowStatusTable.setStatus("mandatory")
_MscShelfFabricCardRowStatusEntry_Object = MibTableRow
mscShelfFabricCardRowStatusEntry = _MscShelfFabricCardRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 1, 1)
)
mscShelfFabricCardRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardRowStatusEntry.setStatus("mandatory")
_MscShelfFabricCardRowStatus_Type = RowStatus
_MscShelfFabricCardRowStatus_Object = MibTableColumn
mscShelfFabricCardRowStatus = _MscShelfFabricCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 1, 1, 1),
    _MscShelfFabricCardRowStatus_Type()
)
mscShelfFabricCardRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardRowStatus.setStatus("mandatory")
_MscShelfFabricCardComponentName_Type = DisplayString
_MscShelfFabricCardComponentName_Object = MibTableColumn
mscShelfFabricCardComponentName = _MscShelfFabricCardComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 1, 1, 2),
    _MscShelfFabricCardComponentName_Type()
)
mscShelfFabricCardComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardComponentName.setStatus("mandatory")
_MscShelfFabricCardStorageType_Type = StorageType
_MscShelfFabricCardStorageType_Object = MibTableColumn
mscShelfFabricCardStorageType = _MscShelfFabricCardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 1, 1, 4),
    _MscShelfFabricCardStorageType_Type()
)
mscShelfFabricCardStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardStorageType.setStatus("mandatory")


class _MscShelfFabricCardIndex_Type(Integer32):
    """Custom type mscShelfFabricCardIndex based on Integer32"""
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


_MscShelfFabricCardIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardIndex_Object = MibTableColumn
mscShelfFabricCardIndex = _MscShelfFabricCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 1, 1, 10),
    _MscShelfFabricCardIndex_Type()
)
mscShelfFabricCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardIndex.setStatus("mandatory")
_MscShelfFabricCardTest_ObjectIdentity = ObjectIdentity
mscShelfFabricCardTest = _MscShelfFabricCardTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2)
)
_MscShelfFabricCardTestRowStatusTable_Object = MibTable
mscShelfFabricCardTestRowStatusTable = _MscShelfFabricCardTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestRowStatusTable.setStatus("mandatory")
_MscShelfFabricCardTestRowStatusEntry_Object = MibTableRow
mscShelfFabricCardTestRowStatusEntry = _MscShelfFabricCardTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 1, 1)
)
mscShelfFabricCardTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestRowStatusEntry.setStatus("mandatory")
_MscShelfFabricCardTestRowStatus_Type = RowStatus
_MscShelfFabricCardTestRowStatus_Object = MibTableColumn
mscShelfFabricCardTestRowStatus = _MscShelfFabricCardTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 1, 1, 1),
    _MscShelfFabricCardTestRowStatus_Type()
)
mscShelfFabricCardTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestRowStatus.setStatus("mandatory")
_MscShelfFabricCardTestComponentName_Type = DisplayString
_MscShelfFabricCardTestComponentName_Object = MibTableColumn
mscShelfFabricCardTestComponentName = _MscShelfFabricCardTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 1, 1, 2),
    _MscShelfFabricCardTestComponentName_Type()
)
mscShelfFabricCardTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestComponentName.setStatus("mandatory")
_MscShelfFabricCardTestStorageType_Type = StorageType
_MscShelfFabricCardTestStorageType_Object = MibTableColumn
mscShelfFabricCardTestStorageType = _MscShelfFabricCardTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 1, 1, 4),
    _MscShelfFabricCardTestStorageType_Type()
)
mscShelfFabricCardTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestStorageType.setStatus("mandatory")
_MscShelfFabricCardTestIndex_Type = NonReplicated
_MscShelfFabricCardTestIndex_Object = MibTableColumn
mscShelfFabricCardTestIndex = _MscShelfFabricCardTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 1, 1, 10),
    _MscShelfFabricCardTestIndex_Type()
)
mscShelfFabricCardTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestIndex.setStatus("mandatory")
_MscShelfFabricCardTestStateTable_Object = MibTable
mscShelfFabricCardTestStateTable = _MscShelfFabricCardTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestStateTable.setStatus("mandatory")
_MscShelfFabricCardTestStateEntry_Object = MibTableRow
mscShelfFabricCardTestStateEntry = _MscShelfFabricCardTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 10, 1)
)
mscShelfFabricCardTestStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestStateEntry.setStatus("mandatory")


class _MscShelfFabricCardTestAdminState_Type(Integer32):
    """Custom type mscShelfFabricCardTestAdminState based on Integer32"""
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


_MscShelfFabricCardTestAdminState_Type.__name__ = "Integer32"
_MscShelfFabricCardTestAdminState_Object = MibTableColumn
mscShelfFabricCardTestAdminState = _MscShelfFabricCardTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 10, 1, 1),
    _MscShelfFabricCardTestAdminState_Type()
)
mscShelfFabricCardTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestAdminState.setStatus("mandatory")


class _MscShelfFabricCardTestOperationalState_Type(Integer32):
    """Custom type mscShelfFabricCardTestOperationalState based on Integer32"""
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


_MscShelfFabricCardTestOperationalState_Type.__name__ = "Integer32"
_MscShelfFabricCardTestOperationalState_Object = MibTableColumn
mscShelfFabricCardTestOperationalState = _MscShelfFabricCardTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 10, 1, 2),
    _MscShelfFabricCardTestOperationalState_Type()
)
mscShelfFabricCardTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestOperationalState.setStatus("mandatory")


class _MscShelfFabricCardTestUsageState_Type(Integer32):
    """Custom type mscShelfFabricCardTestUsageState based on Integer32"""
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


_MscShelfFabricCardTestUsageState_Type.__name__ = "Integer32"
_MscShelfFabricCardTestUsageState_Object = MibTableColumn
mscShelfFabricCardTestUsageState = _MscShelfFabricCardTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 10, 1, 3),
    _MscShelfFabricCardTestUsageState_Type()
)
mscShelfFabricCardTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestUsageState.setStatus("mandatory")
_MscShelfFabricCardTestSetupTable_Object = MibTable
mscShelfFabricCardTestSetupTable = _MscShelfFabricCardTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 11)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestSetupTable.setStatus("mandatory")
_MscShelfFabricCardTestSetupEntry_Object = MibTableRow
mscShelfFabricCardTestSetupEntry = _MscShelfFabricCardTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 11, 1)
)
mscShelfFabricCardTestSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestSetupEntry.setStatus("mandatory")


class _MscShelfFabricCardTestDuration_Type(Unsigned32):
    """Custom type mscShelfFabricCardTestDuration based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 43200),
    )


_MscShelfFabricCardTestDuration_Type.__name__ = "Unsigned32"
_MscShelfFabricCardTestDuration_Object = MibTableColumn
mscShelfFabricCardTestDuration = _MscShelfFabricCardTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 11, 1, 1),
    _MscShelfFabricCardTestDuration_Type()
)
mscShelfFabricCardTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestDuration.setStatus("mandatory")
_MscShelfFabricCardTestResultsTable_Object = MibTable
mscShelfFabricCardTestResultsTable = _MscShelfFabricCardTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 12)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestResultsTable.setStatus("mandatory")
_MscShelfFabricCardTestResultsEntry_Object = MibTableRow
mscShelfFabricCardTestResultsEntry = _MscShelfFabricCardTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 12, 1)
)
mscShelfFabricCardTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestResultsEntry.setStatus("mandatory")


class _MscShelfFabricCardTestElapsedTime_Type(Unsigned32):
    """Custom type mscShelfFabricCardTestElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_MscShelfFabricCardTestElapsedTime_Type.__name__ = "Unsigned32"
_MscShelfFabricCardTestElapsedTime_Object = MibTableColumn
mscShelfFabricCardTestElapsedTime = _MscShelfFabricCardTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 12, 1, 1),
    _MscShelfFabricCardTestElapsedTime_Type()
)
mscShelfFabricCardTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestElapsedTime.setStatus("mandatory")


class _MscShelfFabricCardTestTimeRemaining_Type(Unsigned32):
    """Custom type mscShelfFabricCardTestTimeRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_MscShelfFabricCardTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscShelfFabricCardTestTimeRemaining_Object = MibTableColumn
mscShelfFabricCardTestTimeRemaining = _MscShelfFabricCardTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 12, 1, 2),
    _MscShelfFabricCardTestTimeRemaining_Type()
)
mscShelfFabricCardTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestTimeRemaining.setStatus("mandatory")


class _MscShelfFabricCardTestCauseOfTermination_Type(Integer32):
    """Custom type mscShelfFabricCardTestCauseOfTermination based on Integer32"""
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
          ("fabricSelfTestFailure", 5),
          ("neverStarted", 0),
          ("portTestFailure", 4),
          ("stoppedByOperator", 3),
          ("testRunning", 1),
          ("testTimeExpired", 2))
    )


_MscShelfFabricCardTestCauseOfTermination_Type.__name__ = "Integer32"
_MscShelfFabricCardTestCauseOfTermination_Object = MibTableColumn
mscShelfFabricCardTestCauseOfTermination = _MscShelfFabricCardTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 12, 1, 3),
    _MscShelfFabricCardTestCauseOfTermination_Type()
)
mscShelfFabricCardTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestCauseOfTermination.setStatus("mandatory")


class _MscShelfFabricCardTestTestsDone_Type(OctetString):
    """Custom type mscShelfFabricCardTestTestsDone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardTestTestsDone_Type.__name__ = "OctetString"
_MscShelfFabricCardTestTestsDone_Object = MibTableColumn
mscShelfFabricCardTestTestsDone = _MscShelfFabricCardTestTestsDone_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 12, 1, 4),
    _MscShelfFabricCardTestTestsDone_Type()
)
mscShelfFabricCardTestTestsDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestTestsDone.setStatus("mandatory")


class _MscShelfFabricCardTestFabricSelfTestResults_Type(Integer32):
    """Custom type mscShelfFabricCardTestFabricSelfTestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("noTest", 2),
          ("ok", 1))
    )


_MscShelfFabricCardTestFabricSelfTestResults_Type.__name__ = "Integer32"
_MscShelfFabricCardTestFabricSelfTestResults_Object = MibTableColumn
mscShelfFabricCardTestFabricSelfTestResults = _MscShelfFabricCardTestFabricSelfTestResults_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 12, 1, 5),
    _MscShelfFabricCardTestFabricSelfTestResults_Type()
)
mscShelfFabricCardTestFabricSelfTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestFabricSelfTestResults.setStatus("mandatory")
_MscShelfFabricCardTestPortTestResultsTable_Object = MibTable
mscShelfFabricCardTestPortTestResultsTable = _MscShelfFabricCardTestPortTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 468)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPortTestResultsTable.setStatus("mandatory")
_MscShelfFabricCardTestPortTestResultsEntry_Object = MibTableRow
mscShelfFabricCardTestPortTestResultsEntry = _MscShelfFabricCardTestPortTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 468, 1)
)
mscShelfFabricCardTestPortTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestPortTestResultsIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPortTestResultsEntry.setStatus("mandatory")


class _MscShelfFabricCardTestPortTestResultsIndex_Type(Integer32):
    """Custom type mscShelfFabricCardTestPortTestResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfFabricCardTestPortTestResultsIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardTestPortTestResultsIndex_Object = MibTableColumn
mscShelfFabricCardTestPortTestResultsIndex = _MscShelfFabricCardTestPortTestResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 468, 1, 1),
    _MscShelfFabricCardTestPortTestResultsIndex_Type()
)
mscShelfFabricCardTestPortTestResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPortTestResultsIndex.setStatus("mandatory")


class _MscShelfFabricCardTestPortTestResultsValue_Type(Integer32):
    """Custom type mscShelfFabricCardTestPortTestResultsValue based on Integer32"""
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


_MscShelfFabricCardTestPortTestResultsValue_Type.__name__ = "Integer32"
_MscShelfFabricCardTestPortTestResultsValue_Object = MibTableColumn
mscShelfFabricCardTestPortTestResultsValue = _MscShelfFabricCardTestPortTestResultsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 468, 1, 2),
    _MscShelfFabricCardTestPortTestResultsValue_Type()
)
mscShelfFabricCardTestPortTestResultsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPortTestResultsValue.setStatus("mandatory")
_MscShelfFabricCardTestBroadcastTestResultsTable_Object = MibTable
mscShelfFabricCardTestBroadcastTestResultsTable = _MscShelfFabricCardTestBroadcastTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 469)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestBroadcastTestResultsTable.setStatus("mandatory")
_MscShelfFabricCardTestBroadcastTestResultsEntry_Object = MibTableRow
mscShelfFabricCardTestBroadcastTestResultsEntry = _MscShelfFabricCardTestBroadcastTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 469, 1)
)
mscShelfFabricCardTestBroadcastTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestBroadcastTestResultsTxCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestBroadcastTestResultsRxCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestBroadcastTestResultsEntry.setStatus("mandatory")


class _MscShelfFabricCardTestBroadcastTestResultsTxCardIndex_Type(Integer32):
    """Custom type mscShelfFabricCardTestBroadcastTestResultsTxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfFabricCardTestBroadcastTestResultsTxCardIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardTestBroadcastTestResultsTxCardIndex_Object = MibTableColumn
mscShelfFabricCardTestBroadcastTestResultsTxCardIndex = _MscShelfFabricCardTestBroadcastTestResultsTxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 469, 1, 1),
    _MscShelfFabricCardTestBroadcastTestResultsTxCardIndex_Type()
)
mscShelfFabricCardTestBroadcastTestResultsTxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestBroadcastTestResultsTxCardIndex.setStatus("mandatory")


class _MscShelfFabricCardTestBroadcastTestResultsRxCardIndex_Type(Integer32):
    """Custom type mscShelfFabricCardTestBroadcastTestResultsRxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfFabricCardTestBroadcastTestResultsRxCardIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardTestBroadcastTestResultsRxCardIndex_Object = MibTableColumn
mscShelfFabricCardTestBroadcastTestResultsRxCardIndex = _MscShelfFabricCardTestBroadcastTestResultsRxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 469, 1, 2),
    _MscShelfFabricCardTestBroadcastTestResultsRxCardIndex_Type()
)
mscShelfFabricCardTestBroadcastTestResultsRxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestBroadcastTestResultsRxCardIndex.setStatus("mandatory")


class _MscShelfFabricCardTestBroadcastTestResultsValue_Type(Integer32):
    """Custom type mscShelfFabricCardTestBroadcastTestResultsValue based on Integer32"""
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


_MscShelfFabricCardTestBroadcastTestResultsValue_Type.__name__ = "Integer32"
_MscShelfFabricCardTestBroadcastTestResultsValue_Object = MibTableColumn
mscShelfFabricCardTestBroadcastTestResultsValue = _MscShelfFabricCardTestBroadcastTestResultsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 469, 1, 3),
    _MscShelfFabricCardTestBroadcastTestResultsValue_Type()
)
mscShelfFabricCardTestBroadcastTestResultsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestBroadcastTestResultsValue.setStatus("mandatory")
_MscShelfFabricCardTestPingTestsTable_Object = MibTable
mscShelfFabricCardTestPingTestsTable = _MscShelfFabricCardTestPingTestsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 470)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingTestsTable.setStatus("mandatory")
_MscShelfFabricCardTestPingTestsEntry_Object = MibTableRow
mscShelfFabricCardTestPingTestsEntry = _MscShelfFabricCardTestPingTestsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 470, 1)
)
mscShelfFabricCardTestPingTestsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestPingTestsTxCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestPingTestsRxCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingTestsEntry.setStatus("mandatory")


class _MscShelfFabricCardTestPingTestsTxCardIndex_Type(Integer32):
    """Custom type mscShelfFabricCardTestPingTestsTxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfFabricCardTestPingTestsTxCardIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardTestPingTestsTxCardIndex_Object = MibTableColumn
mscShelfFabricCardTestPingTestsTxCardIndex = _MscShelfFabricCardTestPingTestsTxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 470, 1, 1),
    _MscShelfFabricCardTestPingTestsTxCardIndex_Type()
)
mscShelfFabricCardTestPingTestsTxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingTestsTxCardIndex.setStatus("mandatory")


class _MscShelfFabricCardTestPingTestsRxCardIndex_Type(Integer32):
    """Custom type mscShelfFabricCardTestPingTestsRxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfFabricCardTestPingTestsRxCardIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardTestPingTestsRxCardIndex_Object = MibTableColumn
mscShelfFabricCardTestPingTestsRxCardIndex = _MscShelfFabricCardTestPingTestsRxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 470, 1, 2),
    _MscShelfFabricCardTestPingTestsRxCardIndex_Type()
)
mscShelfFabricCardTestPingTestsRxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingTestsRxCardIndex.setStatus("mandatory")


class _MscShelfFabricCardTestPingTestsValue_Type(Unsigned32):
    """Custom type mscShelfFabricCardTestPingTestsValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfFabricCardTestPingTestsValue_Type.__name__ = "Unsigned32"
_MscShelfFabricCardTestPingTestsValue_Object = MibTableColumn
mscShelfFabricCardTestPingTestsValue = _MscShelfFabricCardTestPingTestsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 470, 1, 3),
    _MscShelfFabricCardTestPingTestsValue_Type()
)
mscShelfFabricCardTestPingTestsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingTestsValue.setStatus("mandatory")
_MscShelfFabricCardTestPingFailuresTable_Object = MibTable
mscShelfFabricCardTestPingFailuresTable = _MscShelfFabricCardTestPingFailuresTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 471)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingFailuresTable.setStatus("mandatory")
_MscShelfFabricCardTestPingFailuresEntry_Object = MibTableRow
mscShelfFabricCardTestPingFailuresEntry = _MscShelfFabricCardTestPingFailuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 471, 1)
)
mscShelfFabricCardTestPingFailuresEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestPingFailuresTxCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardTestPingFailuresRxCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingFailuresEntry.setStatus("mandatory")


class _MscShelfFabricCardTestPingFailuresTxCardIndex_Type(Integer32):
    """Custom type mscShelfFabricCardTestPingFailuresTxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfFabricCardTestPingFailuresTxCardIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardTestPingFailuresTxCardIndex_Object = MibTableColumn
mscShelfFabricCardTestPingFailuresTxCardIndex = _MscShelfFabricCardTestPingFailuresTxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 471, 1, 1),
    _MscShelfFabricCardTestPingFailuresTxCardIndex_Type()
)
mscShelfFabricCardTestPingFailuresTxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingFailuresTxCardIndex.setStatus("mandatory")


class _MscShelfFabricCardTestPingFailuresRxCardIndex_Type(Integer32):
    """Custom type mscShelfFabricCardTestPingFailuresRxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfFabricCardTestPingFailuresRxCardIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardTestPingFailuresRxCardIndex_Object = MibTableColumn
mscShelfFabricCardTestPingFailuresRxCardIndex = _MscShelfFabricCardTestPingFailuresRxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 471, 1, 2),
    _MscShelfFabricCardTestPingFailuresRxCardIndex_Type()
)
mscShelfFabricCardTestPingFailuresRxCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingFailuresRxCardIndex.setStatus("mandatory")


class _MscShelfFabricCardTestPingFailuresValue_Type(Unsigned32):
    """Custom type mscShelfFabricCardTestPingFailuresValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfFabricCardTestPingFailuresValue_Type.__name__ = "Unsigned32"
_MscShelfFabricCardTestPingFailuresValue_Object = MibTableColumn
mscShelfFabricCardTestPingFailuresValue = _MscShelfFabricCardTestPingFailuresValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 2, 471, 1, 3),
    _MscShelfFabricCardTestPingFailuresValue_Type()
)
mscShelfFabricCardTestPingFailuresValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTestPingFailuresValue.setStatus("mandatory")
_MscShelfFabricCardCardPort_ObjectIdentity = ObjectIdentity
mscShelfFabricCardCardPort = _MscShelfFabricCardCardPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3)
)
_MscShelfFabricCardCardPortRowStatusTable_Object = MibTable
mscShelfFabricCardCardPortRowStatusTable = _MscShelfFabricCardCardPortRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortRowStatusTable.setStatus("mandatory")
_MscShelfFabricCardCardPortRowStatusEntry_Object = MibTableRow
mscShelfFabricCardCardPortRowStatusEntry = _MscShelfFabricCardCardPortRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 1, 1)
)
mscShelfFabricCardCardPortRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardCardPortIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortRowStatusEntry.setStatus("mandatory")
_MscShelfFabricCardCardPortRowStatus_Type = RowStatus
_MscShelfFabricCardCardPortRowStatus_Object = MibTableColumn
mscShelfFabricCardCardPortRowStatus = _MscShelfFabricCardCardPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 1, 1, 1),
    _MscShelfFabricCardCardPortRowStatus_Type()
)
mscShelfFabricCardCardPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortRowStatus.setStatus("mandatory")
_MscShelfFabricCardCardPortComponentName_Type = DisplayString
_MscShelfFabricCardCardPortComponentName_Object = MibTableColumn
mscShelfFabricCardCardPortComponentName = _MscShelfFabricCardCardPortComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 1, 1, 2),
    _MscShelfFabricCardCardPortComponentName_Type()
)
mscShelfFabricCardCardPortComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortComponentName.setStatus("mandatory")
_MscShelfFabricCardCardPortStorageType_Type = StorageType
_MscShelfFabricCardCardPortStorageType_Object = MibTableColumn
mscShelfFabricCardCardPortStorageType = _MscShelfFabricCardCardPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 1, 1, 4),
    _MscShelfFabricCardCardPortStorageType_Type()
)
mscShelfFabricCardCardPortStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortStorageType.setStatus("mandatory")


class _MscShelfFabricCardCardPortIndex_Type(Integer32):
    """Custom type mscShelfFabricCardCardPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfFabricCardCardPortIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardCardPortIndex_Object = MibTableColumn
mscShelfFabricCardCardPortIndex = _MscShelfFabricCardCardPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 1, 1, 10),
    _MscShelfFabricCardCardPortIndex_Type()
)
mscShelfFabricCardCardPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortIndex.setStatus("mandatory")
_MscShelfFabricCardCardPortStateTable_Object = MibTable
mscShelfFabricCardCardPortStateTable = _MscShelfFabricCardCardPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortStateTable.setStatus("mandatory")
_MscShelfFabricCardCardPortStateEntry_Object = MibTableRow
mscShelfFabricCardCardPortStateEntry = _MscShelfFabricCardCardPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1)
)
mscShelfFabricCardCardPortStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardCardPortIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortStateEntry.setStatus("mandatory")


class _MscShelfFabricCardCardPortAdminState_Type(Integer32):
    """Custom type mscShelfFabricCardCardPortAdminState based on Integer32"""
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


_MscShelfFabricCardCardPortAdminState_Type.__name__ = "Integer32"
_MscShelfFabricCardCardPortAdminState_Object = MibTableColumn
mscShelfFabricCardCardPortAdminState = _MscShelfFabricCardCardPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1, 1),
    _MscShelfFabricCardCardPortAdminState_Type()
)
mscShelfFabricCardCardPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortAdminState.setStatus("mandatory")


class _MscShelfFabricCardCardPortOperationalState_Type(Integer32):
    """Custom type mscShelfFabricCardCardPortOperationalState based on Integer32"""
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


_MscShelfFabricCardCardPortOperationalState_Type.__name__ = "Integer32"
_MscShelfFabricCardCardPortOperationalState_Object = MibTableColumn
mscShelfFabricCardCardPortOperationalState = _MscShelfFabricCardCardPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1, 2),
    _MscShelfFabricCardCardPortOperationalState_Type()
)
mscShelfFabricCardCardPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortOperationalState.setStatus("mandatory")


class _MscShelfFabricCardCardPortUsageState_Type(Integer32):
    """Custom type mscShelfFabricCardCardPortUsageState based on Integer32"""
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


_MscShelfFabricCardCardPortUsageState_Type.__name__ = "Integer32"
_MscShelfFabricCardCardPortUsageState_Object = MibTableColumn
mscShelfFabricCardCardPortUsageState = _MscShelfFabricCardCardPortUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1, 3),
    _MscShelfFabricCardCardPortUsageState_Type()
)
mscShelfFabricCardCardPortUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortUsageState.setStatus("mandatory")


class _MscShelfFabricCardCardPortAvailabilityStatus_Type(OctetString):
    """Custom type mscShelfFabricCardCardPortAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfFabricCardCardPortAvailabilityStatus_Type.__name__ = "OctetString"
_MscShelfFabricCardCardPortAvailabilityStatus_Object = MibTableColumn
mscShelfFabricCardCardPortAvailabilityStatus = _MscShelfFabricCardCardPortAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1, 4),
    _MscShelfFabricCardCardPortAvailabilityStatus_Type()
)
mscShelfFabricCardCardPortAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortAvailabilityStatus.setStatus("mandatory")


class _MscShelfFabricCardCardPortProceduralStatus_Type(OctetString):
    """Custom type mscShelfFabricCardCardPortProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardCardPortProceduralStatus_Type.__name__ = "OctetString"
_MscShelfFabricCardCardPortProceduralStatus_Object = MibTableColumn
mscShelfFabricCardCardPortProceduralStatus = _MscShelfFabricCardCardPortProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1, 5),
    _MscShelfFabricCardCardPortProceduralStatus_Type()
)
mscShelfFabricCardCardPortProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortProceduralStatus.setStatus("mandatory")


class _MscShelfFabricCardCardPortControlStatus_Type(OctetString):
    """Custom type mscShelfFabricCardCardPortControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardCardPortControlStatus_Type.__name__ = "OctetString"
_MscShelfFabricCardCardPortControlStatus_Object = MibTableColumn
mscShelfFabricCardCardPortControlStatus = _MscShelfFabricCardCardPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1, 6),
    _MscShelfFabricCardCardPortControlStatus_Type()
)
mscShelfFabricCardCardPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortControlStatus.setStatus("mandatory")


class _MscShelfFabricCardCardPortAlarmStatus_Type(OctetString):
    """Custom type mscShelfFabricCardCardPortAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardCardPortAlarmStatus_Type.__name__ = "OctetString"
_MscShelfFabricCardCardPortAlarmStatus_Object = MibTableColumn
mscShelfFabricCardCardPortAlarmStatus = _MscShelfFabricCardCardPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1, 7),
    _MscShelfFabricCardCardPortAlarmStatus_Type()
)
mscShelfFabricCardCardPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortAlarmStatus.setStatus("mandatory")


class _MscShelfFabricCardCardPortStandbyStatus_Type(Integer32):
    """Custom type mscShelfFabricCardCardPortStandbyStatus based on Integer32"""
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


_MscShelfFabricCardCardPortStandbyStatus_Type.__name__ = "Integer32"
_MscShelfFabricCardCardPortStandbyStatus_Object = MibTableColumn
mscShelfFabricCardCardPortStandbyStatus = _MscShelfFabricCardCardPortStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1, 8),
    _MscShelfFabricCardCardPortStandbyStatus_Type()
)
mscShelfFabricCardCardPortStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortStandbyStatus.setStatus("mandatory")


class _MscShelfFabricCardCardPortUnknownStatus_Type(Integer32):
    """Custom type mscShelfFabricCardCardPortUnknownStatus based on Integer32"""
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


_MscShelfFabricCardCardPortUnknownStatus_Type.__name__ = "Integer32"
_MscShelfFabricCardCardPortUnknownStatus_Object = MibTableColumn
mscShelfFabricCardCardPortUnknownStatus = _MscShelfFabricCardCardPortUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 10, 1, 9),
    _MscShelfFabricCardCardPortUnknownStatus_Type()
)
mscShelfFabricCardCardPortUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortUnknownStatus.setStatus("mandatory")
_MscShelfFabricCardCardPortOperTable_Object = MibTable
mscShelfFabricCardCardPortOperTable = _MscShelfFabricCardCardPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 11)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortOperTable.setStatus("mandatory")
_MscShelfFabricCardCardPortOperEntry_Object = MibTableRow
mscShelfFabricCardCardPortOperEntry = _MscShelfFabricCardCardPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 11, 1)
)
mscShelfFabricCardCardPortOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardCardPortIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortOperEntry.setStatus("mandatory")


class _MscShelfFabricCardCardPortFailuresInEffect_Type(OctetString):
    """Custom type mscShelfFabricCardCardPortFailuresInEffect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardCardPortFailuresInEffect_Type.__name__ = "OctetString"
_MscShelfFabricCardCardPortFailuresInEffect_Object = MibTableColumn
mscShelfFabricCardCardPortFailuresInEffect = _MscShelfFabricCardCardPortFailuresInEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 11, 1, 1),
    _MscShelfFabricCardCardPortFailuresInEffect_Type()
)
mscShelfFabricCardCardPortFailuresInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortFailuresInEffect.setStatus("mandatory")


class _MscShelfFabricCardCardPortDependenciesInEffect_Type(OctetString):
    """Custom type mscShelfFabricCardCardPortDependenciesInEffect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardCardPortDependenciesInEffect_Type.__name__ = "OctetString"
_MscShelfFabricCardCardPortDependenciesInEffect_Object = MibTableColumn
mscShelfFabricCardCardPortDependenciesInEffect = _MscShelfFabricCardCardPortDependenciesInEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 11, 1, 2),
    _MscShelfFabricCardCardPortDependenciesInEffect_Type()
)
mscShelfFabricCardCardPortDependenciesInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortDependenciesInEffect.setStatus("mandatory")
_MscShelfFabricCardCardPortCardPortErrorsTable_Object = MibTable
mscShelfFabricCardCardPortCardPortErrorsTable = _MscShelfFabricCardCardPortCardPortErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 12)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortCardPortErrorsTable.setStatus("mandatory")
_MscShelfFabricCardCardPortCardPortErrorsEntry_Object = MibTableRow
mscShelfFabricCardCardPortCardPortErrorsEntry = _MscShelfFabricCardCardPortCardPortErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 12, 1)
)
mscShelfFabricCardCardPortCardPortErrorsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardCardPortIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortCardPortErrorsEntry.setStatus("mandatory")


class _MscShelfFabricCardCardPortSelfTestErrorCode_Type(Unsigned32):
    """Custom type mscShelfFabricCardCardPortSelfTestErrorCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfFabricCardCardPortSelfTestErrorCode_Type.__name__ = "Unsigned32"
_MscShelfFabricCardCardPortSelfTestErrorCode_Object = MibTableColumn
mscShelfFabricCardCardPortSelfTestErrorCode = _MscShelfFabricCardCardPortSelfTestErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 12, 1, 1),
    _MscShelfFabricCardCardPortSelfTestErrorCode_Type()
)
mscShelfFabricCardCardPortSelfTestErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortSelfTestErrorCode.setStatus("mandatory")
_MscShelfFabricCardCardPortDataOrAddressCrcErrors_Type = Counter32
_MscShelfFabricCardCardPortDataOrAddressCrcErrors_Object = MibTableColumn
mscShelfFabricCardCardPortDataOrAddressCrcErrors = _MscShelfFabricCardCardPortDataOrAddressCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 12, 1, 2),
    _MscShelfFabricCardCardPortDataOrAddressCrcErrors_Type()
)
mscShelfFabricCardCardPortDataOrAddressCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortDataOrAddressCrcErrors.setStatus("mandatory")
_MscShelfFabricCardCardPortFlowControlViolationErrors_Type = Counter32
_MscShelfFabricCardCardPortFlowControlViolationErrors_Object = MibTableColumn
mscShelfFabricCardCardPortFlowControlViolationErrors = _MscShelfFabricCardCardPortFlowControlViolationErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 12, 1, 3),
    _MscShelfFabricCardCardPortFlowControlViolationErrors_Type()
)
mscShelfFabricCardCardPortFlowControlViolationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortFlowControlViolationErrors.setStatus("mandatory")
_MscShelfFabricCardCardPortLivelinessErrors_Type = Counter32
_MscShelfFabricCardCardPortLivelinessErrors_Object = MibTableColumn
mscShelfFabricCardCardPortLivelinessErrors = _MscShelfFabricCardCardPortLivelinessErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 12, 1, 4),
    _MscShelfFabricCardCardPortLivelinessErrors_Type()
)
mscShelfFabricCardCardPortLivelinessErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortLivelinessErrors.setStatus("mandatory")
_MscShelfFabricCardCardPortLossOfSignalOrSyncErrors_Type = Counter32
_MscShelfFabricCardCardPortLossOfSignalOrSyncErrors_Object = MibTableColumn
mscShelfFabricCardCardPortLossOfSignalOrSyncErrors = _MscShelfFabricCardCardPortLossOfSignalOrSyncErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 3, 12, 1, 5),
    _MscShelfFabricCardCardPortLossOfSignalOrSyncErrors_Type()
)
mscShelfFabricCardCardPortLossOfSignalOrSyncErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardCardPortLossOfSignalOrSyncErrors.setStatus("mandatory")
_MscShelfFabricCardStateTable_Object = MibTable
mscShelfFabricCardStateTable = _MscShelfFabricCardStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardStateTable.setStatus("mandatory")
_MscShelfFabricCardStateEntry_Object = MibTableRow
mscShelfFabricCardStateEntry = _MscShelfFabricCardStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1)
)
mscShelfFabricCardStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardStateEntry.setStatus("mandatory")


class _MscShelfFabricCardAdminState_Type(Integer32):
    """Custom type mscShelfFabricCardAdminState based on Integer32"""
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


_MscShelfFabricCardAdminState_Type.__name__ = "Integer32"
_MscShelfFabricCardAdminState_Object = MibTableColumn
mscShelfFabricCardAdminState = _MscShelfFabricCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1, 1),
    _MscShelfFabricCardAdminState_Type()
)
mscShelfFabricCardAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardAdminState.setStatus("mandatory")


class _MscShelfFabricCardOperationalState_Type(Integer32):
    """Custom type mscShelfFabricCardOperationalState based on Integer32"""
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


_MscShelfFabricCardOperationalState_Type.__name__ = "Integer32"
_MscShelfFabricCardOperationalState_Object = MibTableColumn
mscShelfFabricCardOperationalState = _MscShelfFabricCardOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1, 2),
    _MscShelfFabricCardOperationalState_Type()
)
mscShelfFabricCardOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardOperationalState.setStatus("mandatory")


class _MscShelfFabricCardUsageState_Type(Integer32):
    """Custom type mscShelfFabricCardUsageState based on Integer32"""
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


_MscShelfFabricCardUsageState_Type.__name__ = "Integer32"
_MscShelfFabricCardUsageState_Object = MibTableColumn
mscShelfFabricCardUsageState = _MscShelfFabricCardUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1, 3),
    _MscShelfFabricCardUsageState_Type()
)
mscShelfFabricCardUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardUsageState.setStatus("mandatory")


class _MscShelfFabricCardAvailabilityStatus_Type(OctetString):
    """Custom type mscShelfFabricCardAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfFabricCardAvailabilityStatus_Type.__name__ = "OctetString"
_MscShelfFabricCardAvailabilityStatus_Object = MibTableColumn
mscShelfFabricCardAvailabilityStatus = _MscShelfFabricCardAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1, 4),
    _MscShelfFabricCardAvailabilityStatus_Type()
)
mscShelfFabricCardAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardAvailabilityStatus.setStatus("mandatory")


class _MscShelfFabricCardProceduralStatus_Type(OctetString):
    """Custom type mscShelfFabricCardProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardProceduralStatus_Type.__name__ = "OctetString"
_MscShelfFabricCardProceduralStatus_Object = MibTableColumn
mscShelfFabricCardProceduralStatus = _MscShelfFabricCardProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1, 5),
    _MscShelfFabricCardProceduralStatus_Type()
)
mscShelfFabricCardProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardProceduralStatus.setStatus("mandatory")


class _MscShelfFabricCardControlStatus_Type(OctetString):
    """Custom type mscShelfFabricCardControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardControlStatus_Type.__name__ = "OctetString"
_MscShelfFabricCardControlStatus_Object = MibTableColumn
mscShelfFabricCardControlStatus = _MscShelfFabricCardControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1, 6),
    _MscShelfFabricCardControlStatus_Type()
)
mscShelfFabricCardControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardControlStatus.setStatus("mandatory")


class _MscShelfFabricCardAlarmStatus_Type(OctetString):
    """Custom type mscShelfFabricCardAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardAlarmStatus_Type.__name__ = "OctetString"
_MscShelfFabricCardAlarmStatus_Object = MibTableColumn
mscShelfFabricCardAlarmStatus = _MscShelfFabricCardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1, 7),
    _MscShelfFabricCardAlarmStatus_Type()
)
mscShelfFabricCardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardAlarmStatus.setStatus("mandatory")


class _MscShelfFabricCardStandbyStatus_Type(Integer32):
    """Custom type mscShelfFabricCardStandbyStatus based on Integer32"""
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


_MscShelfFabricCardStandbyStatus_Type.__name__ = "Integer32"
_MscShelfFabricCardStandbyStatus_Object = MibTableColumn
mscShelfFabricCardStandbyStatus = _MscShelfFabricCardStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1, 8),
    _MscShelfFabricCardStandbyStatus_Type()
)
mscShelfFabricCardStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardStandbyStatus.setStatus("mandatory")


class _MscShelfFabricCardUnknownStatus_Type(Integer32):
    """Custom type mscShelfFabricCardUnknownStatus based on Integer32"""
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


_MscShelfFabricCardUnknownStatus_Type.__name__ = "Integer32"
_MscShelfFabricCardUnknownStatus_Object = MibTableColumn
mscShelfFabricCardUnknownStatus = _MscShelfFabricCardUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 10, 1, 9),
    _MscShelfFabricCardUnknownStatus_Type()
)
mscShelfFabricCardUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardUnknownStatus.setStatus("mandatory")
_MscShelfFabricCardPropTable_Object = MibTable
mscShelfFabricCardPropTable = _MscShelfFabricCardPropTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 11)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardPropTable.setStatus("mandatory")
_MscShelfFabricCardPropEntry_Object = MibTableRow
mscShelfFabricCardPropEntry = _MscShelfFabricCardPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 11, 1)
)
mscShelfFabricCardPropEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardPropEntry.setStatus("mandatory")


class _MscShelfFabricCardProductCode_Type(AsciiString):
    """Custom type mscShelfFabricCardProductCode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_MscShelfFabricCardProductCode_Type.__name__ = "AsciiString"
_MscShelfFabricCardProductCode_Object = MibTableColumn
mscShelfFabricCardProductCode = _MscShelfFabricCardProductCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 11, 1, 1),
    _MscShelfFabricCardProductCode_Type()
)
mscShelfFabricCardProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardProductCode.setStatus("mandatory")


class _MscShelfFabricCardSerialNumber_Type(AsciiString):
    """Custom type mscShelfFabricCardSerialNumber based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MscShelfFabricCardSerialNumber_Type.__name__ = "AsciiString"
_MscShelfFabricCardSerialNumber_Object = MibTableColumn
mscShelfFabricCardSerialNumber = _MscShelfFabricCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 11, 1, 2),
    _MscShelfFabricCardSerialNumber_Type()
)
mscShelfFabricCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardSerialNumber.setStatus("mandatory")
_MscShelfFabricCardOperTable_Object = MibTable
mscShelfFabricCardOperTable = _MscShelfFabricCardOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardOperTable.setStatus("mandatory")
_MscShelfFabricCardOperEntry_Object = MibTableRow
mscShelfFabricCardOperEntry = _MscShelfFabricCardOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1)
)
mscShelfFabricCardOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardOperEntry.setStatus("mandatory")


class _MscShelfFabricCardFailureCause_Type(OctetString):
    """Custom type mscShelfFabricCardFailureCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardFailureCause_Type.__name__ = "OctetString"
_MscShelfFabricCardFailureCause_Object = MibTableColumn
mscShelfFabricCardFailureCause = _MscShelfFabricCardFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1, 1),
    _MscShelfFabricCardFailureCause_Type()
)
mscShelfFabricCardFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardFailureCause.setStatus("mandatory")


class _MscShelfFabricCardUtilization_Type(Gauge32):
    """Custom type mscShelfFabricCardUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscShelfFabricCardUtilization_Type.__name__ = "Gauge32"
_MscShelfFabricCardUtilization_Object = MibTableColumn
mscShelfFabricCardUtilization = _MscShelfFabricCardUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1, 2),
    _MscShelfFabricCardUtilization_Type()
)
mscShelfFabricCardUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardUtilization.setStatus("mandatory")


class _MscShelfFabricCardOperatingTemperature_Type(FixedPoint1):
    """Custom type mscShelfFabricCardOperatingTemperature based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 640),
    )


_MscShelfFabricCardOperatingTemperature_Type.__name__ = "FixedPoint1"
_MscShelfFabricCardOperatingTemperature_Object = MibTableColumn
mscShelfFabricCardOperatingTemperature = _MscShelfFabricCardOperatingTemperature_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1, 3),
    _MscShelfFabricCardOperatingTemperature_Type()
)
mscShelfFabricCardOperatingTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardOperatingTemperature.setStatus("mandatory")


class _MscShelfFabricCardSecondaryControlBusStatus_Type(OctetString):
    """Custom type mscShelfFabricCardSecondaryControlBusStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscShelfFabricCardSecondaryControlBusStatus_Type.__name__ = "OctetString"
_MscShelfFabricCardSecondaryControlBusStatus_Object = MibTableColumn
mscShelfFabricCardSecondaryControlBusStatus = _MscShelfFabricCardSecondaryControlBusStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1, 4),
    _MscShelfFabricCardSecondaryControlBusStatus_Type()
)
mscShelfFabricCardSecondaryControlBusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardSecondaryControlBusStatus.setStatus("mandatory")


class _MscShelfFabricCardSelfTestResults_Type(Unsigned32):
    """Custom type mscShelfFabricCardSelfTestResults based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscShelfFabricCardSelfTestResults_Type.__name__ = "Unsigned32"
_MscShelfFabricCardSelfTestResults_Object = MibTableColumn
mscShelfFabricCardSelfTestResults = _MscShelfFabricCardSelfTestResults_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1, 5),
    _MscShelfFabricCardSelfTestResults_Type()
)
mscShelfFabricCardSelfTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardSelfTestResults.setStatus("mandatory")


class _MscShelfFabricCardDependencyInEffect_Type(OctetString):
    """Custom type mscShelfFabricCardDependencyInEffect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscShelfFabricCardDependencyInEffect_Type.__name__ = "OctetString"
_MscShelfFabricCardDependencyInEffect_Object = MibTableColumn
mscShelfFabricCardDependencyInEffect = _MscShelfFabricCardDependencyInEffect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1, 6),
    _MscShelfFabricCardDependencyInEffect_Type()
)
mscShelfFabricCardDependencyInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardDependencyInEffect.setStatus("mandatory")


class _MscShelfFabricCardVoltageAFeedDetected_Type(Integer32):
    """Custom type mscShelfFabricCardVoltageAFeedDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscShelfFabricCardVoltageAFeedDetected_Type.__name__ = "Integer32"
_MscShelfFabricCardVoltageAFeedDetected_Object = MibTableColumn
mscShelfFabricCardVoltageAFeedDetected = _MscShelfFabricCardVoltageAFeedDetected_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1, 7),
    _MscShelfFabricCardVoltageAFeedDetected_Type()
)
mscShelfFabricCardVoltageAFeedDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardVoltageAFeedDetected.setStatus("mandatory")


class _MscShelfFabricCardVoltageBFeedDetected_Type(Integer32):
    """Custom type mscShelfFabricCardVoltageBFeedDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MscShelfFabricCardVoltageBFeedDetected_Type.__name__ = "Integer32"
_MscShelfFabricCardVoltageBFeedDetected_Object = MibTableColumn
mscShelfFabricCardVoltageBFeedDetected = _MscShelfFabricCardVoltageBFeedDetected_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1, 8),
    _MscShelfFabricCardVoltageBFeedDetected_Type()
)
mscShelfFabricCardVoltageBFeedDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardVoltageBFeedDetected.setStatus("mandatory")


class _MscShelfFabricCardTemperatureThreshold_Type(FixedPoint1):
    """Custom type mscShelfFabricCardTemperatureThreshold based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MscShelfFabricCardTemperatureThreshold_Type.__name__ = "FixedPoint1"
_MscShelfFabricCardTemperatureThreshold_Object = MibTableColumn
mscShelfFabricCardTemperatureThreshold = _MscShelfFabricCardTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 12, 1, 9),
    _MscShelfFabricCardTemperatureThreshold_Type()
)
mscShelfFabricCardTemperatureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTemperatureThreshold.setStatus("mandatory")
_MscShelfFabricCardErrorsTable_Object = MibTable
mscShelfFabricCardErrorsTable = _MscShelfFabricCardErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 13)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardErrorsTable.setStatus("mandatory")
_MscShelfFabricCardErrorsEntry_Object = MibTableRow
mscShelfFabricCardErrorsEntry = _MscShelfFabricCardErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 13, 1)
)
mscShelfFabricCardErrorsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardErrorsEntry.setStatus("mandatory")
_MscShelfFabricCardVoltageErrors_Type = Counter32
_MscShelfFabricCardVoltageErrors_Object = MibTableColumn
mscShelfFabricCardVoltageErrors = _MscShelfFabricCardVoltageErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 13, 1, 1),
    _MscShelfFabricCardVoltageErrors_Type()
)
mscShelfFabricCardVoltageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardVoltageErrors.setStatus("mandatory")
_MscShelfFabricCardTemperatureErrors_Type = Counter32
_MscShelfFabricCardTemperatureErrors_Object = MibTableColumn
mscShelfFabricCardTemperatureErrors = _MscShelfFabricCardTemperatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 13, 1, 2),
    _MscShelfFabricCardTemperatureErrors_Type()
)
mscShelfFabricCardTemperatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardTemperatureErrors.setStatus("mandatory")
_MscShelfFabricCardBanksTable_Object = MibTable
mscShelfFabricCardBanksTable = _MscShelfFabricCardBanksTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 14)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardBanksTable.setStatus("mandatory")
_MscShelfFabricCardBanksEntry_Object = MibTableRow
mscShelfFabricCardBanksEntry = _MscShelfFabricCardBanksEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 14, 1)
)
mscShelfFabricCardBanksEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardBanksEntry.setStatus("mandatory")


class _MscShelfFabricCardFixedBankVersion_Type(FixedPoint1):
    """Custom type mscShelfFabricCardFixedBankVersion based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MscShelfFabricCardFixedBankVersion_Type.__name__ = "FixedPoint1"
_MscShelfFabricCardFixedBankVersion_Object = MibTableColumn
mscShelfFabricCardFixedBankVersion = _MscShelfFabricCardFixedBankVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 14, 1, 1),
    _MscShelfFabricCardFixedBankVersion_Type()
)
mscShelfFabricCardFixedBankVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardFixedBankVersion.setStatus("mandatory")


class _MscShelfFabricCardWritableBankVersion_Type(FixedPoint1):
    """Custom type mscShelfFabricCardWritableBankVersion based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MscShelfFabricCardWritableBankVersion_Type.__name__ = "FixedPoint1"
_MscShelfFabricCardWritableBankVersion_Object = MibTableColumn
mscShelfFabricCardWritableBankVersion = _MscShelfFabricCardWritableBankVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 14, 1, 2),
    _MscShelfFabricCardWritableBankVersion_Type()
)
mscShelfFabricCardWritableBankVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardWritableBankVersion.setStatus("mandatory")


class _MscShelfFabricCardRecommendedVersionToInstall_Type(AsciiString):
    """Custom type mscShelfFabricCardRecommendedVersionToInstall based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_MscShelfFabricCardRecommendedVersionToInstall_Type.__name__ = "AsciiString"
_MscShelfFabricCardRecommendedVersionToInstall_Object = MibTableColumn
mscShelfFabricCardRecommendedVersionToInstall = _MscShelfFabricCardRecommendedVersionToInstall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 14, 1, 3),
    _MscShelfFabricCardRecommendedVersionToInstall_Type()
)
mscShelfFabricCardRecommendedVersionToInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardRecommendedVersionToInstall.setStatus("mandatory")


class _MscShelfFabricCardActiveBank_Type(Integer32):
    """Custom type mscShelfFabricCardActiveBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("unknown", 2),
          ("writable", 1))
    )


_MscShelfFabricCardActiveBank_Type.__name__ = "Integer32"
_MscShelfFabricCardActiveBank_Object = MibTableColumn
mscShelfFabricCardActiveBank = _MscShelfFabricCardActiveBank_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 14, 1, 4),
    _MscShelfFabricCardActiveBank_Type()
)
mscShelfFabricCardActiveBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscShelfFabricCardActiveBank.setStatus("mandatory")


class _MscShelfFabricCardBankOnShelfRestart_Type(Integer32):
    """Custom type mscShelfFabricCardBankOnShelfRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("unknown", 2),
          ("writable", 1))
    )


_MscShelfFabricCardBankOnShelfRestart_Type.__name__ = "Integer32"
_MscShelfFabricCardBankOnShelfRestart_Object = MibTableColumn
mscShelfFabricCardBankOnShelfRestart = _MscShelfFabricCardBankOnShelfRestart_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 14, 1, 5),
    _MscShelfFabricCardBankOnShelfRestart_Type()
)
mscShelfFabricCardBankOnShelfRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardBankOnShelfRestart.setStatus("mandatory")


class _MscShelfFabricCardWritableBankStatus_Type(Integer32):
    """Custom type mscShelfFabricCardWritableBankStatus based on Integer32"""
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
        *(("empty", 1),
          ("loaded", 3),
          ("loading", 2),
          ("unknown", 0))
    )


_MscShelfFabricCardWritableBankStatus_Type.__name__ = "Integer32"
_MscShelfFabricCardWritableBankStatus_Object = MibTableColumn
mscShelfFabricCardWritableBankStatus = _MscShelfFabricCardWritableBankStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 14, 1, 6),
    _MscShelfFabricCardWritableBankStatus_Type()
)
mscShelfFabricCardWritableBankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardWritableBankStatus.setStatus("mandatory")
_MscShelfFabricCardSecondaryControlBusCardBustapsTable_Object = MibTable
mscShelfFabricCardSecondaryControlBusCardBustapsTable = _MscShelfFabricCardSecondaryControlBusCardBustapsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 443)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardSecondaryControlBusCardBustapsTable.setStatus("mandatory")
_MscShelfFabricCardSecondaryControlBusCardBustapsEntry_Object = MibTableRow
mscShelfFabricCardSecondaryControlBusCardBustapsEntry = _MscShelfFabricCardSecondaryControlBusCardBustapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 443, 1)
)
mscShelfFabricCardSecondaryControlBusCardBustapsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardSecondaryControlBusCardBustapsIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardSecondaryControlBusCardBustapsEntry.setStatus("mandatory")


class _MscShelfFabricCardSecondaryControlBusCardBustapsIndex_Type(Integer32):
    """Custom type mscShelfFabricCardSecondaryControlBusCardBustapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscShelfFabricCardSecondaryControlBusCardBustapsIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardSecondaryControlBusCardBustapsIndex_Object = MibTableColumn
mscShelfFabricCardSecondaryControlBusCardBustapsIndex = _MscShelfFabricCardSecondaryControlBusCardBustapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 443, 1, 1),
    _MscShelfFabricCardSecondaryControlBusCardBustapsIndex_Type()
)
mscShelfFabricCardSecondaryControlBusCardBustapsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardSecondaryControlBusCardBustapsIndex.setStatus("mandatory")


class _MscShelfFabricCardSecondaryControlBusCardBustapsValue_Type(Integer32):
    """Custom type mscShelfFabricCardSecondaryControlBusCardBustapsValue based on Integer32"""
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
        *(("hardwareFailure", 1),
          ("none", 6),
          ("ok", 0),
          ("parityOrCrcErrors", 2),
          ("pollError", 5),
          ("timeOutError", 3),
          ("txOrRxError", 4))
    )


_MscShelfFabricCardSecondaryControlBusCardBustapsValue_Type.__name__ = "Integer32"
_MscShelfFabricCardSecondaryControlBusCardBustapsValue_Object = MibTableColumn
mscShelfFabricCardSecondaryControlBusCardBustapsValue = _MscShelfFabricCardSecondaryControlBusCardBustapsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 443, 1, 2),
    _MscShelfFabricCardSecondaryControlBusCardBustapsValue_Type()
)
mscShelfFabricCardSecondaryControlBusCardBustapsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardSecondaryControlBusCardBustapsValue.setStatus("mandatory")
_MscShelfFabricCardSecondaryControlBusFabricBustapsTable_Object = MibTable
mscShelfFabricCardSecondaryControlBusFabricBustapsTable = _MscShelfFabricCardSecondaryControlBusFabricBustapsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 445)
)
if mibBuilder.loadTexts:
    mscShelfFabricCardSecondaryControlBusFabricBustapsTable.setStatus("mandatory")
_MscShelfFabricCardSecondaryControlBusFabricBustapsEntry_Object = MibTableRow
mscShelfFabricCardSecondaryControlBusFabricBustapsEntry = _MscShelfFabricCardSecondaryControlBusFabricBustapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 445, 1)
)
mscShelfFabricCardSecondaryControlBusFabricBustapsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BaseShelfMIB", "mscShelfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FabricMIB", "mscShelfFabricCardSecondaryControlBusFabricBustapsIndex"),
)
if mibBuilder.loadTexts:
    mscShelfFabricCardSecondaryControlBusFabricBustapsEntry.setStatus("mandatory")


class _MscShelfFabricCardSecondaryControlBusFabricBustapsIndex_Type(Integer32):
    """Custom type mscShelfFabricCardSecondaryControlBusFabricBustapsIndex based on Integer32"""
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


_MscShelfFabricCardSecondaryControlBusFabricBustapsIndex_Type.__name__ = "Integer32"
_MscShelfFabricCardSecondaryControlBusFabricBustapsIndex_Object = MibTableColumn
mscShelfFabricCardSecondaryControlBusFabricBustapsIndex = _MscShelfFabricCardSecondaryControlBusFabricBustapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 445, 1, 1),
    _MscShelfFabricCardSecondaryControlBusFabricBustapsIndex_Type()
)
mscShelfFabricCardSecondaryControlBusFabricBustapsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscShelfFabricCardSecondaryControlBusFabricBustapsIndex.setStatus("mandatory")


class _MscShelfFabricCardSecondaryControlBusFabricBustapsValue_Type(Integer32):
    """Custom type mscShelfFabricCardSecondaryControlBusFabricBustapsValue based on Integer32"""
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
        *(("none", 4),
          ("ok", 0),
          ("pollError", 2),
          ("testMessageError", 3),
          ("txOrRxError", 1),
          ("unknown", 5))
    )


_MscShelfFabricCardSecondaryControlBusFabricBustapsValue_Type.__name__ = "Integer32"
_MscShelfFabricCardSecondaryControlBusFabricBustapsValue_Object = MibTableColumn
mscShelfFabricCardSecondaryControlBusFabricBustapsValue = _MscShelfFabricCardSecondaryControlBusFabricBustapsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 13, 5, 445, 1, 2),
    _MscShelfFabricCardSecondaryControlBusFabricBustapsValue_Type()
)
mscShelfFabricCardSecondaryControlBusFabricBustapsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscShelfFabricCardSecondaryControlBusFabricBustapsValue.setStatus("mandatory")
_FabricMIB_ObjectIdentity = ObjectIdentity
fabricMIB = _FabricMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 145)
)
_FabricGroup_ObjectIdentity = ObjectIdentity
fabricGroup = _FabricGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 145, 1)
)
_FabricGroupCA_ObjectIdentity = ObjectIdentity
fabricGroupCA = _FabricGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 145, 1, 1)
)
_FabricGroupCA02_ObjectIdentity = ObjectIdentity
fabricGroupCA02 = _FabricGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 145, 1, 1, 3)
)
_FabricGroupCA02A_ObjectIdentity = ObjectIdentity
fabricGroupCA02A = _FabricGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 145, 1, 1, 3, 2)
)
_FabricCapabilities_ObjectIdentity = ObjectIdentity
fabricCapabilities = _FabricCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 145, 3)
)
_FabricCapabilitiesCA_ObjectIdentity = ObjectIdentity
fabricCapabilitiesCA = _FabricCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 145, 3, 1)
)
_FabricCapabilitiesCA02_ObjectIdentity = ObjectIdentity
fabricCapabilitiesCA02 = _FabricCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 145, 3, 1, 3)
)
_FabricCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
fabricCapabilitiesCA02A = _FabricCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 145, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FabricMIB",
    **{"mscShelfCardFabricPort": mscShelfCardFabricPort,
       "mscShelfCardFabricPortRowStatusTable": mscShelfCardFabricPortRowStatusTable,
       "mscShelfCardFabricPortRowStatusEntry": mscShelfCardFabricPortRowStatusEntry,
       "mscShelfCardFabricPortRowStatus": mscShelfCardFabricPortRowStatus,
       "mscShelfCardFabricPortComponentName": mscShelfCardFabricPortComponentName,
       "mscShelfCardFabricPortStorageType": mscShelfCardFabricPortStorageType,
       "mscShelfCardFabricPortIndex": mscShelfCardFabricPortIndex,
       "mscShelfCardFabricPortStateTable": mscShelfCardFabricPortStateTable,
       "mscShelfCardFabricPortStateEntry": mscShelfCardFabricPortStateEntry,
       "mscShelfCardFabricPortAdminState": mscShelfCardFabricPortAdminState,
       "mscShelfCardFabricPortOperationalState": mscShelfCardFabricPortOperationalState,
       "mscShelfCardFabricPortUsageState": mscShelfCardFabricPortUsageState,
       "mscShelfCardFabricPortAvailabilityStatus": mscShelfCardFabricPortAvailabilityStatus,
       "mscShelfCardFabricPortProceduralStatus": mscShelfCardFabricPortProceduralStatus,
       "mscShelfCardFabricPortControlStatus": mscShelfCardFabricPortControlStatus,
       "mscShelfCardFabricPortAlarmStatus": mscShelfCardFabricPortAlarmStatus,
       "mscShelfCardFabricPortStandbyStatus": mscShelfCardFabricPortStandbyStatus,
       "mscShelfCardFabricPortUnknownStatus": mscShelfCardFabricPortUnknownStatus,
       "mscShelfCardFabricPortOperTable": mscShelfCardFabricPortOperTable,
       "mscShelfCardFabricPortOperEntry": mscShelfCardFabricPortOperEntry,
       "mscShelfCardFabricPortFailuresInEffect": mscShelfCardFabricPortFailuresInEffect,
       "mscShelfCardFabricPortDependenciesInEffect": mscShelfCardFabricPortDependenciesInEffect,
       "mscShelfCardFabricPortCardsAvailable": mscShelfCardFabricPortCardsAvailable,
       "mscShelfCardFabricPortCardsTxTo": mscShelfCardFabricPortCardsTxTo,
       "mscShelfCardFabricPortErrorsTable": mscShelfCardFabricPortErrorsTable,
       "mscShelfCardFabricPortErrorsEntry": mscShelfCardFabricPortErrorsEntry,
       "mscShelfCardFabricPortSelfTestErrorCode": mscShelfCardFabricPortSelfTestErrorCode,
       "mscShelfCardFabricPortLivelinessErrors": mscShelfCardFabricPortLivelinessErrors,
       "mscShelfCardFabricPortSwitchClockErrors": mscShelfCardFabricPortSwitchClockErrors,
       "mscShelfCardFabricPortPortHardwareErrors": mscShelfCardFabricPortPortHardwareErrors,
       "mscShelfCardFabricPortPortProtocolErrors": mscShelfCardFabricPortPortProtocolErrors,
       "mscShelfCardFabricPortDataCorruptionErrors": mscShelfCardFabricPortDataCorruptionErrors,
       "mscShelfCardFabricPortLinkLivelinessErrors": mscShelfCardFabricPortLinkLivelinessErrors,
       "mscShelfFabricCard": mscShelfFabricCard,
       "mscShelfFabricCardRowStatusTable": mscShelfFabricCardRowStatusTable,
       "mscShelfFabricCardRowStatusEntry": mscShelfFabricCardRowStatusEntry,
       "mscShelfFabricCardRowStatus": mscShelfFabricCardRowStatus,
       "mscShelfFabricCardComponentName": mscShelfFabricCardComponentName,
       "mscShelfFabricCardStorageType": mscShelfFabricCardStorageType,
       "mscShelfFabricCardIndex": mscShelfFabricCardIndex,
       "mscShelfFabricCardTest": mscShelfFabricCardTest,
       "mscShelfFabricCardTestRowStatusTable": mscShelfFabricCardTestRowStatusTable,
       "mscShelfFabricCardTestRowStatusEntry": mscShelfFabricCardTestRowStatusEntry,
       "mscShelfFabricCardTestRowStatus": mscShelfFabricCardTestRowStatus,
       "mscShelfFabricCardTestComponentName": mscShelfFabricCardTestComponentName,
       "mscShelfFabricCardTestStorageType": mscShelfFabricCardTestStorageType,
       "mscShelfFabricCardTestIndex": mscShelfFabricCardTestIndex,
       "mscShelfFabricCardTestStateTable": mscShelfFabricCardTestStateTable,
       "mscShelfFabricCardTestStateEntry": mscShelfFabricCardTestStateEntry,
       "mscShelfFabricCardTestAdminState": mscShelfFabricCardTestAdminState,
       "mscShelfFabricCardTestOperationalState": mscShelfFabricCardTestOperationalState,
       "mscShelfFabricCardTestUsageState": mscShelfFabricCardTestUsageState,
       "mscShelfFabricCardTestSetupTable": mscShelfFabricCardTestSetupTable,
       "mscShelfFabricCardTestSetupEntry": mscShelfFabricCardTestSetupEntry,
       "mscShelfFabricCardTestDuration": mscShelfFabricCardTestDuration,
       "mscShelfFabricCardTestResultsTable": mscShelfFabricCardTestResultsTable,
       "mscShelfFabricCardTestResultsEntry": mscShelfFabricCardTestResultsEntry,
       "mscShelfFabricCardTestElapsedTime": mscShelfFabricCardTestElapsedTime,
       "mscShelfFabricCardTestTimeRemaining": mscShelfFabricCardTestTimeRemaining,
       "mscShelfFabricCardTestCauseOfTermination": mscShelfFabricCardTestCauseOfTermination,
       "mscShelfFabricCardTestTestsDone": mscShelfFabricCardTestTestsDone,
       "mscShelfFabricCardTestFabricSelfTestResults": mscShelfFabricCardTestFabricSelfTestResults,
       "mscShelfFabricCardTestPortTestResultsTable": mscShelfFabricCardTestPortTestResultsTable,
       "mscShelfFabricCardTestPortTestResultsEntry": mscShelfFabricCardTestPortTestResultsEntry,
       "mscShelfFabricCardTestPortTestResultsIndex": mscShelfFabricCardTestPortTestResultsIndex,
       "mscShelfFabricCardTestPortTestResultsValue": mscShelfFabricCardTestPortTestResultsValue,
       "mscShelfFabricCardTestBroadcastTestResultsTable": mscShelfFabricCardTestBroadcastTestResultsTable,
       "mscShelfFabricCardTestBroadcastTestResultsEntry": mscShelfFabricCardTestBroadcastTestResultsEntry,
       "mscShelfFabricCardTestBroadcastTestResultsTxCardIndex": mscShelfFabricCardTestBroadcastTestResultsTxCardIndex,
       "mscShelfFabricCardTestBroadcastTestResultsRxCardIndex": mscShelfFabricCardTestBroadcastTestResultsRxCardIndex,
       "mscShelfFabricCardTestBroadcastTestResultsValue": mscShelfFabricCardTestBroadcastTestResultsValue,
       "mscShelfFabricCardTestPingTestsTable": mscShelfFabricCardTestPingTestsTable,
       "mscShelfFabricCardTestPingTestsEntry": mscShelfFabricCardTestPingTestsEntry,
       "mscShelfFabricCardTestPingTestsTxCardIndex": mscShelfFabricCardTestPingTestsTxCardIndex,
       "mscShelfFabricCardTestPingTestsRxCardIndex": mscShelfFabricCardTestPingTestsRxCardIndex,
       "mscShelfFabricCardTestPingTestsValue": mscShelfFabricCardTestPingTestsValue,
       "mscShelfFabricCardTestPingFailuresTable": mscShelfFabricCardTestPingFailuresTable,
       "mscShelfFabricCardTestPingFailuresEntry": mscShelfFabricCardTestPingFailuresEntry,
       "mscShelfFabricCardTestPingFailuresTxCardIndex": mscShelfFabricCardTestPingFailuresTxCardIndex,
       "mscShelfFabricCardTestPingFailuresRxCardIndex": mscShelfFabricCardTestPingFailuresRxCardIndex,
       "mscShelfFabricCardTestPingFailuresValue": mscShelfFabricCardTestPingFailuresValue,
       "mscShelfFabricCardCardPort": mscShelfFabricCardCardPort,
       "mscShelfFabricCardCardPortRowStatusTable": mscShelfFabricCardCardPortRowStatusTable,
       "mscShelfFabricCardCardPortRowStatusEntry": mscShelfFabricCardCardPortRowStatusEntry,
       "mscShelfFabricCardCardPortRowStatus": mscShelfFabricCardCardPortRowStatus,
       "mscShelfFabricCardCardPortComponentName": mscShelfFabricCardCardPortComponentName,
       "mscShelfFabricCardCardPortStorageType": mscShelfFabricCardCardPortStorageType,
       "mscShelfFabricCardCardPortIndex": mscShelfFabricCardCardPortIndex,
       "mscShelfFabricCardCardPortStateTable": mscShelfFabricCardCardPortStateTable,
       "mscShelfFabricCardCardPortStateEntry": mscShelfFabricCardCardPortStateEntry,
       "mscShelfFabricCardCardPortAdminState": mscShelfFabricCardCardPortAdminState,
       "mscShelfFabricCardCardPortOperationalState": mscShelfFabricCardCardPortOperationalState,
       "mscShelfFabricCardCardPortUsageState": mscShelfFabricCardCardPortUsageState,
       "mscShelfFabricCardCardPortAvailabilityStatus": mscShelfFabricCardCardPortAvailabilityStatus,
       "mscShelfFabricCardCardPortProceduralStatus": mscShelfFabricCardCardPortProceduralStatus,
       "mscShelfFabricCardCardPortControlStatus": mscShelfFabricCardCardPortControlStatus,
       "mscShelfFabricCardCardPortAlarmStatus": mscShelfFabricCardCardPortAlarmStatus,
       "mscShelfFabricCardCardPortStandbyStatus": mscShelfFabricCardCardPortStandbyStatus,
       "mscShelfFabricCardCardPortUnknownStatus": mscShelfFabricCardCardPortUnknownStatus,
       "mscShelfFabricCardCardPortOperTable": mscShelfFabricCardCardPortOperTable,
       "mscShelfFabricCardCardPortOperEntry": mscShelfFabricCardCardPortOperEntry,
       "mscShelfFabricCardCardPortFailuresInEffect": mscShelfFabricCardCardPortFailuresInEffect,
       "mscShelfFabricCardCardPortDependenciesInEffect": mscShelfFabricCardCardPortDependenciesInEffect,
       "mscShelfFabricCardCardPortCardPortErrorsTable": mscShelfFabricCardCardPortCardPortErrorsTable,
       "mscShelfFabricCardCardPortCardPortErrorsEntry": mscShelfFabricCardCardPortCardPortErrorsEntry,
       "mscShelfFabricCardCardPortSelfTestErrorCode": mscShelfFabricCardCardPortSelfTestErrorCode,
       "mscShelfFabricCardCardPortDataOrAddressCrcErrors": mscShelfFabricCardCardPortDataOrAddressCrcErrors,
       "mscShelfFabricCardCardPortFlowControlViolationErrors": mscShelfFabricCardCardPortFlowControlViolationErrors,
       "mscShelfFabricCardCardPortLivelinessErrors": mscShelfFabricCardCardPortLivelinessErrors,
       "mscShelfFabricCardCardPortLossOfSignalOrSyncErrors": mscShelfFabricCardCardPortLossOfSignalOrSyncErrors,
       "mscShelfFabricCardStateTable": mscShelfFabricCardStateTable,
       "mscShelfFabricCardStateEntry": mscShelfFabricCardStateEntry,
       "mscShelfFabricCardAdminState": mscShelfFabricCardAdminState,
       "mscShelfFabricCardOperationalState": mscShelfFabricCardOperationalState,
       "mscShelfFabricCardUsageState": mscShelfFabricCardUsageState,
       "mscShelfFabricCardAvailabilityStatus": mscShelfFabricCardAvailabilityStatus,
       "mscShelfFabricCardProceduralStatus": mscShelfFabricCardProceduralStatus,
       "mscShelfFabricCardControlStatus": mscShelfFabricCardControlStatus,
       "mscShelfFabricCardAlarmStatus": mscShelfFabricCardAlarmStatus,
       "mscShelfFabricCardStandbyStatus": mscShelfFabricCardStandbyStatus,
       "mscShelfFabricCardUnknownStatus": mscShelfFabricCardUnknownStatus,
       "mscShelfFabricCardPropTable": mscShelfFabricCardPropTable,
       "mscShelfFabricCardPropEntry": mscShelfFabricCardPropEntry,
       "mscShelfFabricCardProductCode": mscShelfFabricCardProductCode,
       "mscShelfFabricCardSerialNumber": mscShelfFabricCardSerialNumber,
       "mscShelfFabricCardOperTable": mscShelfFabricCardOperTable,
       "mscShelfFabricCardOperEntry": mscShelfFabricCardOperEntry,
       "mscShelfFabricCardFailureCause": mscShelfFabricCardFailureCause,
       "mscShelfFabricCardUtilization": mscShelfFabricCardUtilization,
       "mscShelfFabricCardOperatingTemperature": mscShelfFabricCardOperatingTemperature,
       "mscShelfFabricCardSecondaryControlBusStatus": mscShelfFabricCardSecondaryControlBusStatus,
       "mscShelfFabricCardSelfTestResults": mscShelfFabricCardSelfTestResults,
       "mscShelfFabricCardDependencyInEffect": mscShelfFabricCardDependencyInEffect,
       "mscShelfFabricCardVoltageAFeedDetected": mscShelfFabricCardVoltageAFeedDetected,
       "mscShelfFabricCardVoltageBFeedDetected": mscShelfFabricCardVoltageBFeedDetected,
       "mscShelfFabricCardTemperatureThreshold": mscShelfFabricCardTemperatureThreshold,
       "mscShelfFabricCardErrorsTable": mscShelfFabricCardErrorsTable,
       "mscShelfFabricCardErrorsEntry": mscShelfFabricCardErrorsEntry,
       "mscShelfFabricCardVoltageErrors": mscShelfFabricCardVoltageErrors,
       "mscShelfFabricCardTemperatureErrors": mscShelfFabricCardTemperatureErrors,
       "mscShelfFabricCardBanksTable": mscShelfFabricCardBanksTable,
       "mscShelfFabricCardBanksEntry": mscShelfFabricCardBanksEntry,
       "mscShelfFabricCardFixedBankVersion": mscShelfFabricCardFixedBankVersion,
       "mscShelfFabricCardWritableBankVersion": mscShelfFabricCardWritableBankVersion,
       "mscShelfFabricCardRecommendedVersionToInstall": mscShelfFabricCardRecommendedVersionToInstall,
       "mscShelfFabricCardActiveBank": mscShelfFabricCardActiveBank,
       "mscShelfFabricCardBankOnShelfRestart": mscShelfFabricCardBankOnShelfRestart,
       "mscShelfFabricCardWritableBankStatus": mscShelfFabricCardWritableBankStatus,
       "mscShelfFabricCardSecondaryControlBusCardBustapsTable": mscShelfFabricCardSecondaryControlBusCardBustapsTable,
       "mscShelfFabricCardSecondaryControlBusCardBustapsEntry": mscShelfFabricCardSecondaryControlBusCardBustapsEntry,
       "mscShelfFabricCardSecondaryControlBusCardBustapsIndex": mscShelfFabricCardSecondaryControlBusCardBustapsIndex,
       "mscShelfFabricCardSecondaryControlBusCardBustapsValue": mscShelfFabricCardSecondaryControlBusCardBustapsValue,
       "mscShelfFabricCardSecondaryControlBusFabricBustapsTable": mscShelfFabricCardSecondaryControlBusFabricBustapsTable,
       "mscShelfFabricCardSecondaryControlBusFabricBustapsEntry": mscShelfFabricCardSecondaryControlBusFabricBustapsEntry,
       "mscShelfFabricCardSecondaryControlBusFabricBustapsIndex": mscShelfFabricCardSecondaryControlBusFabricBustapsIndex,
       "mscShelfFabricCardSecondaryControlBusFabricBustapsValue": mscShelfFabricCardSecondaryControlBusFabricBustapsValue,
       "fabricMIB": fabricMIB,
       "fabricGroup": fabricGroup,
       "fabricGroupCA": fabricGroupCA,
       "fabricGroupCA02": fabricGroupCA02,
       "fabricGroupCA02A": fabricGroupCA02A,
       "fabricCapabilities": fabricCapabilities,
       "fabricCapabilitiesCA": fabricCapabilitiesCA,
       "fabricCapabilitiesCA02": fabricCapabilitiesCA02,
       "fabricCapabilitiesCA02A": fabricCapabilitiesCA02A}
)
