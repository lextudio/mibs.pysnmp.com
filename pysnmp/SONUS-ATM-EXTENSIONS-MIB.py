# SNMP MIB module (SONUS-ATM-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-ATM-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:52 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusNifIndex,
 sonusNifPort,
 sonusNifShelf,
 sonusNifSlot) = mibBuilder.importSymbols(
    "SONUS-IP-INTERFACE-MIB",
    "sonusNifIndex",
    "sonusNifPort",
    "sonusNifShelf",
    "sonusNifSlot")

(sonusPacketMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusPacketMIBs")

(SonusShelfIndex,
 SonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusShelfIndex",
    "SonusSlotIndex")


# MODULE-IDENTITY

sonusAtmExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusAtmExtMIBObjects_ObjectIdentity = ObjectIdentity
sonusAtmExtMIBObjects = _SonusAtmExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1)
)
_SonusAtmExtVclAdmnTable_Object = MibTable
sonusAtmExtVclAdmnTable = _SonusAtmExtVclAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnTable.setStatus("current")
_SonusAtmExtVclAdmnEntry_Object = MibTableRow
sonusAtmExtVclAdmnEntry = _SonusAtmExtVclAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1)
)
sonusAtmExtVclAdmnEntry.setIndexNames(
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnIfIndex"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
)
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnEntry.setStatus("current")
_SonusAtmExtVclAdmnIfIndex_Type = Integer32
_SonusAtmExtVclAdmnIfIndex_Object = MibTableColumn
sonusAtmExtVclAdmnIfIndex = _SonusAtmExtVclAdmnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 1),
    _SonusAtmExtVclAdmnIfIndex_Type()
)
sonusAtmExtVclAdmnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnIfIndex.setStatus("current")
_SonusAtmExtVclAdmnVpi_Type = Integer32
_SonusAtmExtVclAdmnVpi_Object = MibTableColumn
sonusAtmExtVclAdmnVpi = _SonusAtmExtVclAdmnVpi_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 2),
    _SonusAtmExtVclAdmnVpi_Type()
)
sonusAtmExtVclAdmnVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnVpi.setStatus("current")
_SonusAtmExtVclAdmnVci_Type = Integer32
_SonusAtmExtVclAdmnVci_Object = MibTableColumn
sonusAtmExtVclAdmnVci = _SonusAtmExtVclAdmnVci_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 3),
    _SonusAtmExtVclAdmnVci_Type()
)
sonusAtmExtVclAdmnVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnVci.setStatus("current")


class _SonusAtmExtVclAdmnMode_Type(Integer32):
    """Custom type sonusAtmExtVclAdmnMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 1))
    )


_SonusAtmExtVclAdmnMode_Type.__name__ = "Integer32"
_SonusAtmExtVclAdmnMode_Object = MibTableColumn
sonusAtmExtVclAdmnMode = _SonusAtmExtVclAdmnMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 4),
    _SonusAtmExtVclAdmnMode_Type()
)
sonusAtmExtVclAdmnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnMode.setStatus("current")


class _SonusAtmExtVclAdmnAction_Type(Integer32):
    """Custom type sonusAtmExtVclAdmnAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 1),
          ("force", 2))
    )


_SonusAtmExtVclAdmnAction_Type.__name__ = "Integer32"
_SonusAtmExtVclAdmnAction_Object = MibTableColumn
sonusAtmExtVclAdmnAction = _SonusAtmExtVclAdmnAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 5),
    _SonusAtmExtVclAdmnAction_Type()
)
sonusAtmExtVclAdmnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnAction.setStatus("current")


class _SonusAtmExtVclAdmnTimeout_Type(Integer32):
    """Custom type sonusAtmExtVclAdmnTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusAtmExtVclAdmnTimeout_Type.__name__ = "Integer32"
_SonusAtmExtVclAdmnTimeout_Object = MibTableColumn
sonusAtmExtVclAdmnTimeout = _SonusAtmExtVclAdmnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 6),
    _SonusAtmExtVclAdmnTimeout_Type()
)
sonusAtmExtVclAdmnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnTimeout.setStatus("current")


class _SonusAtmExtVclAdmnState_Type(Integer32):
    """Custom type sonusAtmExtVclAdmnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusAtmExtVclAdmnState_Type.__name__ = "Integer32"
_SonusAtmExtVclAdmnState_Object = MibTableColumn
sonusAtmExtVclAdmnState = _SonusAtmExtVclAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 7),
    _SonusAtmExtVclAdmnState_Type()
)
sonusAtmExtVclAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnState.setStatus("current")


class _SonusAtmExtVclAdmnOutOfServiceReason_Type(Integer32):
    """Custom type sonusAtmExtVclAdmnOutOfServiceReason based on Integer32"""
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
        *(("admin", 2),
          ("gateway", 3),
          ("notApplicable", 1),
          ("portDown", 4),
          ("serverDown", 5),
          ("srvrAbsent", 6))
    )


_SonusAtmExtVclAdmnOutOfServiceReason_Type.__name__ = "Integer32"
_SonusAtmExtVclAdmnOutOfServiceReason_Object = MibTableColumn
sonusAtmExtVclAdmnOutOfServiceReason = _SonusAtmExtVclAdmnOutOfServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 8),
    _SonusAtmExtVclAdmnOutOfServiceReason_Type()
)
sonusAtmExtVclAdmnOutOfServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnOutOfServiceReason.setStatus("current")
_SonusAtmExtVclAdmnRowStatus_Type = RowStatus
_SonusAtmExtVclAdmnRowStatus_Object = MibTableColumn
sonusAtmExtVclAdmnRowStatus = _SonusAtmExtVclAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 9),
    _SonusAtmExtVclAdmnRowStatus_Type()
)
sonusAtmExtVclAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnRowStatus.setStatus("current")


class _SonusAtmExtVclAdmnBwDeviation_Type(Integer32):
    """Custom type sonusAtmExtVclAdmnBwDeviation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusAtmExtVclAdmnBwDeviation_Type.__name__ = "Integer32"
_SonusAtmExtVclAdmnBwDeviation_Object = MibTableColumn
sonusAtmExtVclAdmnBwDeviation = _SonusAtmExtVclAdmnBwDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 10),
    _SonusAtmExtVclAdmnBwDeviation_Type()
)
sonusAtmExtVclAdmnBwDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnBwDeviation.setStatus("current")


class _SonusAtmExtVclAdmnBwContingency_Type(Integer32):
    """Custom type sonusAtmExtVclAdmnBwContingency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusAtmExtVclAdmnBwContingency_Type.__name__ = "Integer32"
_SonusAtmExtVclAdmnBwContingency_Object = MibTableColumn
sonusAtmExtVclAdmnBwContingency = _SonusAtmExtVclAdmnBwContingency_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 1, 1, 11),
    _SonusAtmExtVclAdmnBwContingency_Type()
)
sonusAtmExtVclAdmnBwContingency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtVclAdmnBwContingency.setStatus("current")
_SonusAtmExtVclStatTable_Object = MibTable
sonusAtmExtVclStatTable = _SonusAtmExtVclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    sonusAtmExtVclStatTable.setStatus("current")
_SonusAtmExtVclStatEntry_Object = MibTableRow
sonusAtmExtVclStatEntry = _SonusAtmExtVclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1)
)
sonusAtmExtVclStatEntry.setIndexNames(
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclStatIfIndex"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclStatVpi"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclStatVci"),
)
if mibBuilder.loadTexts:
    sonusAtmExtVclStatEntry.setStatus("current")
_SonusAtmExtVclStatIfIndex_Type = Integer32
_SonusAtmExtVclStatIfIndex_Object = MibTableColumn
sonusAtmExtVclStatIfIndex = _SonusAtmExtVclStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 1),
    _SonusAtmExtVclStatIfIndex_Type()
)
sonusAtmExtVclStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclStatIfIndex.setStatus("current")
_SonusAtmExtVclStatVpi_Type = Integer32
_SonusAtmExtVclStatVpi_Object = MibTableColumn
sonusAtmExtVclStatVpi = _SonusAtmExtVclStatVpi_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 2),
    _SonusAtmExtVclStatVpi_Type()
)
sonusAtmExtVclStatVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclStatVpi.setStatus("current")
_SonusAtmExtVclStatVci_Type = Integer32
_SonusAtmExtVclStatVci_Object = MibTableColumn
sonusAtmExtVclStatVci = _SonusAtmExtVclStatVci_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 3),
    _SonusAtmExtVclStatVci_Type()
)
sonusAtmExtVclStatVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclStatVci.setStatus("current")


class _SonusAtmExtVclStatState_Type(Integer32):
    """Custom type sonusAtmExtVclStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 3),
          ("inService", 2),
          ("outOfService", 1))
    )


_SonusAtmExtVclStatState_Type.__name__ = "Integer32"
_SonusAtmExtVclStatState_Object = MibTableColumn
sonusAtmExtVclStatState = _SonusAtmExtVclStatState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 4),
    _SonusAtmExtVclStatState_Type()
)
sonusAtmExtVclStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclStatState.setStatus("current")
_SonusAtmExtVclStatCallNum_Type = Integer32
_SonusAtmExtVclStatCallNum_Object = MibTableColumn
sonusAtmExtVclStatCallNum = _SonusAtmExtVclStatCallNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 5),
    _SonusAtmExtVclStatCallNum_Type()
)
sonusAtmExtVclStatCallNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclStatCallNum.setStatus("current")
_SonusAtmExtVclStatSpeedCur_Type = Integer32
_SonusAtmExtVclStatSpeedCur_Object = MibTableColumn
sonusAtmExtVclStatSpeedCur = _SonusAtmExtVclStatSpeedCur_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 6),
    _SonusAtmExtVclStatSpeedCur_Type()
)
sonusAtmExtVclStatSpeedCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclStatSpeedCur.setStatus("current")
_SonusAtmExtVclStatSpeedMax_Type = Integer32
_SonusAtmExtVclStatSpeedMax_Object = MibTableColumn
sonusAtmExtVclStatSpeedMax = _SonusAtmExtVclStatSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 7),
    _SonusAtmExtVclStatSpeedMax_Type()
)
sonusAtmExtVclStatSpeedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclStatSpeedMax.setStatus("current")
_SonusAtmExtVclStatSpeedActual_Type = Integer32
_SonusAtmExtVclStatSpeedActual_Object = MibTableColumn
sonusAtmExtVclStatSpeedActual = _SonusAtmExtVclStatSpeedActual_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 8),
    _SonusAtmExtVclStatSpeedActual_Type()
)
sonusAtmExtVclStatSpeedActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclStatSpeedActual.setStatus("current")
_SonusAtmExtVclStatSpeedDeviation_Type = Integer32
_SonusAtmExtVclStatSpeedDeviation_Object = MibTableColumn
sonusAtmExtVclStatSpeedDeviation = _SonusAtmExtVclStatSpeedDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 2, 1, 9),
    _SonusAtmExtVclStatSpeedDeviation_Type()
)
sonusAtmExtVclStatSpeedDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtVclStatSpeedDeviation.setStatus("current")
_SonusAtmExtAtmLayerTable_Object = MibTable
sonusAtmExtAtmLayerTable = _SonusAtmExtAtmLayerTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    sonusAtmExtAtmLayerTable.setStatus("current")
_SonusAtmExtAtmLayerEntry_Object = MibTableRow
sonusAtmExtAtmLayerEntry = _SonusAtmExtAtmLayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1)
)
sonusAtmExtAtmLayerEntry.setIndexNames(
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAtmLayerShelfIndex"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAtmLayerSlotIndex"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAtmLayerPortIndex"),
)
if mibBuilder.loadTexts:
    sonusAtmExtAtmLayerEntry.setStatus("current")
_SonusAtmExtAtmLayerShelfIndex_Type = SonusShelfIndex
_SonusAtmExtAtmLayerShelfIndex_Object = MibTableColumn
sonusAtmExtAtmLayerShelfIndex = _SonusAtmExtAtmLayerShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 1),
    _SonusAtmExtAtmLayerShelfIndex_Type()
)
sonusAtmExtAtmLayerShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusAtmExtAtmLayerShelfIndex.setStatus("current")
_SonusAtmExtAtmLayerSlotIndex_Type = SonusSlotIndex
_SonusAtmExtAtmLayerSlotIndex_Object = MibTableColumn
sonusAtmExtAtmLayerSlotIndex = _SonusAtmExtAtmLayerSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 2),
    _SonusAtmExtAtmLayerSlotIndex_Type()
)
sonusAtmExtAtmLayerSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusAtmExtAtmLayerSlotIndex.setStatus("current")
_SonusAtmExtAtmLayerPortIndex_Type = Integer32
_SonusAtmExtAtmLayerPortIndex_Object = MibTableColumn
sonusAtmExtAtmLayerPortIndex = _SonusAtmExtAtmLayerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 3),
    _SonusAtmExtAtmLayerPortIndex_Type()
)
sonusAtmExtAtmLayerPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusAtmExtAtmLayerPortIndex.setStatus("current")
_SonusAtmExtAtmLayerIfIndex_Type = Integer32
_SonusAtmExtAtmLayerIfIndex_Object = MibTableColumn
sonusAtmExtAtmLayerIfIndex = _SonusAtmExtAtmLayerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 4),
    _SonusAtmExtAtmLayerIfIndex_Type()
)
sonusAtmExtAtmLayerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtAtmLayerIfIndex.setStatus("current")
_SonusAtmExtAtmLayerRowStatus_Type = RowStatus
_SonusAtmExtAtmLayerRowStatus_Object = MibTableColumn
sonusAtmExtAtmLayerRowStatus = _SonusAtmExtAtmLayerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 3, 1, 5),
    _SonusAtmExtAtmLayerRowStatus_Type()
)
sonusAtmExtAtmLayerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusAtmExtAtmLayerRowStatus.setStatus("current")
_SonusAtmExtAal5LayerTable_Object = MibTable
sonusAtmExtAal5LayerTable = _SonusAtmExtAal5LayerTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4)
)
if mibBuilder.loadTexts:
    sonusAtmExtAal5LayerTable.setStatus("current")
_SonusAtmExtAal5LayerEntry_Object = MibTableRow
sonusAtmExtAal5LayerEntry = _SonusAtmExtAal5LayerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1)
)
sonusAtmExtAal5LayerEntry.setIndexNames(
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAal5LayerShelfIndex"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAal5LayerSlotIndex"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtAal5LayerPortIndex"),
)
if mibBuilder.loadTexts:
    sonusAtmExtAal5LayerEntry.setStatus("current")
_SonusAtmExtAal5LayerShelfIndex_Type = SonusShelfIndex
_SonusAtmExtAal5LayerShelfIndex_Object = MibTableColumn
sonusAtmExtAal5LayerShelfIndex = _SonusAtmExtAal5LayerShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 1),
    _SonusAtmExtAal5LayerShelfIndex_Type()
)
sonusAtmExtAal5LayerShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusAtmExtAal5LayerShelfIndex.setStatus("current")
_SonusAtmExtAal5LayerSlotIndex_Type = SonusSlotIndex
_SonusAtmExtAal5LayerSlotIndex_Object = MibTableColumn
sonusAtmExtAal5LayerSlotIndex = _SonusAtmExtAal5LayerSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 2),
    _SonusAtmExtAal5LayerSlotIndex_Type()
)
sonusAtmExtAal5LayerSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusAtmExtAal5LayerSlotIndex.setStatus("current")
_SonusAtmExtAal5LayerPortIndex_Type = Integer32
_SonusAtmExtAal5LayerPortIndex_Object = MibTableColumn
sonusAtmExtAal5LayerPortIndex = _SonusAtmExtAal5LayerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 3),
    _SonusAtmExtAal5LayerPortIndex_Type()
)
sonusAtmExtAal5LayerPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusAtmExtAal5LayerPortIndex.setStatus("current")
_SonusAtmExtAal5LayerIfIndex_Type = Integer32
_SonusAtmExtAal5LayerIfIndex_Object = MibTableColumn
sonusAtmExtAal5LayerIfIndex = _SonusAtmExtAal5LayerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 4),
    _SonusAtmExtAal5LayerIfIndex_Type()
)
sonusAtmExtAal5LayerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtAal5LayerIfIndex.setStatus("current")
_SonusAtmExtAal5LayerRowStatus_Type = RowStatus
_SonusAtmExtAal5LayerRowStatus_Object = MibTableColumn
sonusAtmExtAal5LayerRowStatus = _SonusAtmExtAal5LayerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 4, 1, 5),
    _SonusAtmExtAal5LayerRowStatus_Type()
)
sonusAtmExtAal5LayerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusAtmExtAal5LayerRowStatus.setStatus("current")
_SonusAtmExtOamF5Table_Object = MibTable
sonusAtmExtOamF5Table = _SonusAtmExtOamF5Table_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5)
)
if mibBuilder.loadTexts:
    sonusAtmExtOamF5Table.setStatus("current")
_SonusAtmExtOamF5Entry_Object = MibTableRow
sonusAtmExtOamF5Entry = _SonusAtmExtOamF5Entry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1)
)
sonusAtmExtOamF5Entry.setIndexNames(
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtOamF5IfIndex"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtOamF5Vpi"),
    (0, "SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtOamF5Vci"),
)
if mibBuilder.loadTexts:
    sonusAtmExtOamF5Entry.setStatus("current")
_SonusAtmExtOamF5IfIndex_Type = InterfaceIndex
_SonusAtmExtOamF5IfIndex_Object = MibTableColumn
sonusAtmExtOamF5IfIndex = _SonusAtmExtOamF5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 1),
    _SonusAtmExtOamF5IfIndex_Type()
)
sonusAtmExtOamF5IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5IfIndex.setStatus("current")
_SonusAtmExtOamF5Vpi_Type = AtmVpIdentifier
_SonusAtmExtOamF5Vpi_Object = MibTableColumn
sonusAtmExtOamF5Vpi = _SonusAtmExtOamF5Vpi_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 2),
    _SonusAtmExtOamF5Vpi_Type()
)
sonusAtmExtOamF5Vpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5Vpi.setStatus("current")
_SonusAtmExtOamF5Vci_Type = AtmVcIdentifier
_SonusAtmExtOamF5Vci_Object = MibTableColumn
sonusAtmExtOamF5Vci = _SonusAtmExtOamF5Vci_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 3),
    _SonusAtmExtOamF5Vci_Type()
)
sonusAtmExtOamF5Vci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5Vci.setStatus("current")


class _SonusAtmExtOamF5Enable_Type(Integer32):
    """Custom type sonusAtmExtOamF5Enable based on Integer32"""
    defaultValue = 2

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


_SonusAtmExtOamF5Enable_Type.__name__ = "Integer32"
_SonusAtmExtOamF5Enable_Object = MibTableColumn
sonusAtmExtOamF5Enable = _SonusAtmExtOamF5Enable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 4),
    _SonusAtmExtOamF5Enable_Type()
)
sonusAtmExtOamF5Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5Enable.setStatus("current")


class _SonusAtmExtOamF5LoopbackType_Type(Integer32):
    """Custom type sonusAtmExtOamF5LoopbackType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end2end", 1),
          ("uni", 2))
    )


_SonusAtmExtOamF5LoopbackType_Type.__name__ = "Integer32"
_SonusAtmExtOamF5LoopbackType_Object = MibTableColumn
sonusAtmExtOamF5LoopbackType = _SonusAtmExtOamF5LoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 5),
    _SonusAtmExtOamF5LoopbackType_Type()
)
sonusAtmExtOamF5LoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5LoopbackType.setStatus("current")


class _SonusAtmExtOamF5LoopbackTimer_Type(Integer32):
    """Custom type sonusAtmExtOamF5LoopbackTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SonusAtmExtOamF5LoopbackTimer_Type.__name__ = "Integer32"
_SonusAtmExtOamF5LoopbackTimer_Object = MibTableColumn
sonusAtmExtOamF5LoopbackTimer = _SonusAtmExtOamF5LoopbackTimer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 6),
    _SonusAtmExtOamF5LoopbackTimer_Type()
)
sonusAtmExtOamF5LoopbackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5LoopbackTimer.setStatus("current")
_SonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure_Type = Counter32
_SonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure_Object = MibTableColumn
sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure = _SonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 7),
    _SonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure_Type()
)
sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure.setStatus("current")
_SonusAtmExtOamF5ReceiveUNILoopbackFailure_Type = Counter32
_SonusAtmExtOamF5ReceiveUNILoopbackFailure_Object = MibTableColumn
sonusAtmExtOamF5ReceiveUNILoopbackFailure = _SonusAtmExtOamF5ReceiveUNILoopbackFailure_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 8),
    _SonusAtmExtOamF5ReceiveUNILoopbackFailure_Type()
)
sonusAtmExtOamF5ReceiveUNILoopbackFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5ReceiveUNILoopbackFailure.setStatus("current")
_SonusAtmExtOamF5TransmitEnd2EndLoopback_Type = Counter32
_SonusAtmExtOamF5TransmitEnd2EndLoopback_Object = MibTableColumn
sonusAtmExtOamF5TransmitEnd2EndLoopback = _SonusAtmExtOamF5TransmitEnd2EndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 9),
    _SonusAtmExtOamF5TransmitEnd2EndLoopback_Type()
)
sonusAtmExtOamF5TransmitEnd2EndLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5TransmitEnd2EndLoopback.setStatus("current")
_SonusAtmExtOamF5TransmitUNILoopback_Type = Counter32
_SonusAtmExtOamF5TransmitUNILoopback_Object = MibTableColumn
sonusAtmExtOamF5TransmitUNILoopback = _SonusAtmExtOamF5TransmitUNILoopback_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 10),
    _SonusAtmExtOamF5TransmitUNILoopback_Type()
)
sonusAtmExtOamF5TransmitUNILoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5TransmitUNILoopback.setStatus("current")
_SonusAtmExtOamF5ReceiveEnd2EndLoopback_Type = Counter32
_SonusAtmExtOamF5ReceiveEnd2EndLoopback_Object = MibTableColumn
sonusAtmExtOamF5ReceiveEnd2EndLoopback = _SonusAtmExtOamF5ReceiveEnd2EndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 11),
    _SonusAtmExtOamF5ReceiveEnd2EndLoopback_Type()
)
sonusAtmExtOamF5ReceiveEnd2EndLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5ReceiveEnd2EndLoopback.setStatus("current")
_SonusAtmExtOamF5ReceiveUNILoopback_Type = Counter32
_SonusAtmExtOamF5ReceiveUNILoopback_Object = MibTableColumn
sonusAtmExtOamF5ReceiveUNILoopback = _SonusAtmExtOamF5ReceiveUNILoopback_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 12),
    _SonusAtmExtOamF5ReceiveUNILoopback_Type()
)
sonusAtmExtOamF5ReceiveUNILoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5ReceiveUNILoopback.setStatus("current")
_SonusAtmExtOamF5ReceiveEnd2EndAIS_Type = Counter32
_SonusAtmExtOamF5ReceiveEnd2EndAIS_Object = MibTableColumn
sonusAtmExtOamF5ReceiveEnd2EndAIS = _SonusAtmExtOamF5ReceiveEnd2EndAIS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 13),
    _SonusAtmExtOamF5ReceiveEnd2EndAIS_Type()
)
sonusAtmExtOamF5ReceiveEnd2EndAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5ReceiveEnd2EndAIS.setStatus("current")
_SonusAtmExtOamF5ReceiveEnd2EndRDI_Type = Counter32
_SonusAtmExtOamF5ReceiveEnd2EndRDI_Object = MibTableColumn
sonusAtmExtOamF5ReceiveEnd2EndRDI = _SonusAtmExtOamF5ReceiveEnd2EndRDI_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 14),
    _SonusAtmExtOamF5ReceiveEnd2EndRDI_Type()
)
sonusAtmExtOamF5ReceiveEnd2EndRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5ReceiveEnd2EndRDI.setStatus("current")
_SonusAtmExtOamF5TransmitEnd2EndRDI_Type = Counter32
_SonusAtmExtOamF5TransmitEnd2EndRDI_Object = MibTableColumn
sonusAtmExtOamF5TransmitEnd2EndRDI = _SonusAtmExtOamF5TransmitEnd2EndRDI_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 1, 5, 1, 15),
    _SonusAtmExtOamF5TransmitEnd2EndRDI_Type()
)
sonusAtmExtOamF5TransmitEnd2EndRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAtmExtOamF5TransmitEnd2EndRDI.setStatus("current")
_SonusAtmExtVclMIBNotifications_ObjectIdentity = ObjectIdentity
sonusAtmExtVclMIBNotifications = _SonusAtmExtVclMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2)
)
_SonusAtmExtVclMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusAtmExtVclMIBNotificationsPrefix = _SonusAtmExtVclMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0)
)
_SonusAtmExtVclMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusAtmExtVclMIBNotificationsObjects = _SonusAtmExtVclMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 1)
)

# Managed Objects groups


# Notification objects

sonusAtmExtVclInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 1)
)
sonusAtmExtVclInServiceNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAtmExtVclInServiceNotification.setStatus(
        "current"
    )

sonusAtmExtVclOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 2)
)
sonusAtmExtVclOutOfServiceNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnOutOfServiceReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAtmExtVclOutOfServiceNotification.setStatus(
        "current"
    )

sonusAtmExtVclEnabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 3)
)
sonusAtmExtVclEnabledNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAtmExtVclEnabledNotification.setStatus(
        "current"
    )

sonusAtmExtVclDisabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 4)
)
sonusAtmExtVclDisabledNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAtmExtVclDisabledNotification.setStatus(
        "current"
    )

sonusAtmExtVclDeletedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 5)
)
sonusAtmExtVclDeletedNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAtmExtVclDeletedNotification.setStatus(
        "current"
    )

sonusAtmExtVclHighWatermarkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 6)
)
sonusAtmExtVclHighWatermarkNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAtmExtVclHighWatermarkNotification.setStatus(
        "current"
    )

sonusAtmExtVclLowWatermarkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 7)
)
sonusAtmExtVclLowWatermarkNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAtmExtVclLowWatermarkNotification.setStatus(
        "current"
    )

sonusAtmExtVclBwHighDeviationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 8)
)
sonusAtmExtVclBwHighDeviationNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAtmExtVclBwHighDeviationNotification.setStatus(
        "current"
    )

sonusAtmExtVclBwLowDeviationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 5, 2, 0, 9)
)
sonusAtmExtVclBwLowDeviationNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVpi"),
        ("SONUS-ATM-EXTENSIONS-MIB", "sonusAtmExtVclAdmnVci"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAtmExtVclBwLowDeviationNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-ATM-EXTENSIONS-MIB",
    **{"sonusAtmExtMIB": sonusAtmExtMIB,
       "sonusAtmExtMIBObjects": sonusAtmExtMIBObjects,
       "sonusAtmExtVclAdmnTable": sonusAtmExtVclAdmnTable,
       "sonusAtmExtVclAdmnEntry": sonusAtmExtVclAdmnEntry,
       "sonusAtmExtVclAdmnIfIndex": sonusAtmExtVclAdmnIfIndex,
       "sonusAtmExtVclAdmnVpi": sonusAtmExtVclAdmnVpi,
       "sonusAtmExtVclAdmnVci": sonusAtmExtVclAdmnVci,
       "sonusAtmExtVclAdmnMode": sonusAtmExtVclAdmnMode,
       "sonusAtmExtVclAdmnAction": sonusAtmExtVclAdmnAction,
       "sonusAtmExtVclAdmnTimeout": sonusAtmExtVclAdmnTimeout,
       "sonusAtmExtVclAdmnState": sonusAtmExtVclAdmnState,
       "sonusAtmExtVclAdmnOutOfServiceReason": sonusAtmExtVclAdmnOutOfServiceReason,
       "sonusAtmExtVclAdmnRowStatus": sonusAtmExtVclAdmnRowStatus,
       "sonusAtmExtVclAdmnBwDeviation": sonusAtmExtVclAdmnBwDeviation,
       "sonusAtmExtVclAdmnBwContingency": sonusAtmExtVclAdmnBwContingency,
       "sonusAtmExtVclStatTable": sonusAtmExtVclStatTable,
       "sonusAtmExtVclStatEntry": sonusAtmExtVclStatEntry,
       "sonusAtmExtVclStatIfIndex": sonusAtmExtVclStatIfIndex,
       "sonusAtmExtVclStatVpi": sonusAtmExtVclStatVpi,
       "sonusAtmExtVclStatVci": sonusAtmExtVclStatVci,
       "sonusAtmExtVclStatState": sonusAtmExtVclStatState,
       "sonusAtmExtVclStatCallNum": sonusAtmExtVclStatCallNum,
       "sonusAtmExtVclStatSpeedCur": sonusAtmExtVclStatSpeedCur,
       "sonusAtmExtVclStatSpeedMax": sonusAtmExtVclStatSpeedMax,
       "sonusAtmExtVclStatSpeedActual": sonusAtmExtVclStatSpeedActual,
       "sonusAtmExtVclStatSpeedDeviation": sonusAtmExtVclStatSpeedDeviation,
       "sonusAtmExtAtmLayerTable": sonusAtmExtAtmLayerTable,
       "sonusAtmExtAtmLayerEntry": sonusAtmExtAtmLayerEntry,
       "sonusAtmExtAtmLayerShelfIndex": sonusAtmExtAtmLayerShelfIndex,
       "sonusAtmExtAtmLayerSlotIndex": sonusAtmExtAtmLayerSlotIndex,
       "sonusAtmExtAtmLayerPortIndex": sonusAtmExtAtmLayerPortIndex,
       "sonusAtmExtAtmLayerIfIndex": sonusAtmExtAtmLayerIfIndex,
       "sonusAtmExtAtmLayerRowStatus": sonusAtmExtAtmLayerRowStatus,
       "sonusAtmExtAal5LayerTable": sonusAtmExtAal5LayerTable,
       "sonusAtmExtAal5LayerEntry": sonusAtmExtAal5LayerEntry,
       "sonusAtmExtAal5LayerShelfIndex": sonusAtmExtAal5LayerShelfIndex,
       "sonusAtmExtAal5LayerSlotIndex": sonusAtmExtAal5LayerSlotIndex,
       "sonusAtmExtAal5LayerPortIndex": sonusAtmExtAal5LayerPortIndex,
       "sonusAtmExtAal5LayerIfIndex": sonusAtmExtAal5LayerIfIndex,
       "sonusAtmExtAal5LayerRowStatus": sonusAtmExtAal5LayerRowStatus,
       "sonusAtmExtOamF5Table": sonusAtmExtOamF5Table,
       "sonusAtmExtOamF5Entry": sonusAtmExtOamF5Entry,
       "sonusAtmExtOamF5IfIndex": sonusAtmExtOamF5IfIndex,
       "sonusAtmExtOamF5Vpi": sonusAtmExtOamF5Vpi,
       "sonusAtmExtOamF5Vci": sonusAtmExtOamF5Vci,
       "sonusAtmExtOamF5Enable": sonusAtmExtOamF5Enable,
       "sonusAtmExtOamF5LoopbackType": sonusAtmExtOamF5LoopbackType,
       "sonusAtmExtOamF5LoopbackTimer": sonusAtmExtOamF5LoopbackTimer,
       "sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure": sonusAtmExtOamF5ReceiveEnd2EndLoopbackFailure,
       "sonusAtmExtOamF5ReceiveUNILoopbackFailure": sonusAtmExtOamF5ReceiveUNILoopbackFailure,
       "sonusAtmExtOamF5TransmitEnd2EndLoopback": sonusAtmExtOamF5TransmitEnd2EndLoopback,
       "sonusAtmExtOamF5TransmitUNILoopback": sonusAtmExtOamF5TransmitUNILoopback,
       "sonusAtmExtOamF5ReceiveEnd2EndLoopback": sonusAtmExtOamF5ReceiveEnd2EndLoopback,
       "sonusAtmExtOamF5ReceiveUNILoopback": sonusAtmExtOamF5ReceiveUNILoopback,
       "sonusAtmExtOamF5ReceiveEnd2EndAIS": sonusAtmExtOamF5ReceiveEnd2EndAIS,
       "sonusAtmExtOamF5ReceiveEnd2EndRDI": sonusAtmExtOamF5ReceiveEnd2EndRDI,
       "sonusAtmExtOamF5TransmitEnd2EndRDI": sonusAtmExtOamF5TransmitEnd2EndRDI,
       "sonusAtmExtVclMIBNotifications": sonusAtmExtVclMIBNotifications,
       "sonusAtmExtVclMIBNotificationsPrefix": sonusAtmExtVclMIBNotificationsPrefix,
       "sonusAtmExtVclInServiceNotification": sonusAtmExtVclInServiceNotification,
       "sonusAtmExtVclOutOfServiceNotification": sonusAtmExtVclOutOfServiceNotification,
       "sonusAtmExtVclEnabledNotification": sonusAtmExtVclEnabledNotification,
       "sonusAtmExtVclDisabledNotification": sonusAtmExtVclDisabledNotification,
       "sonusAtmExtVclDeletedNotification": sonusAtmExtVclDeletedNotification,
       "sonusAtmExtVclHighWatermarkNotification": sonusAtmExtVclHighWatermarkNotification,
       "sonusAtmExtVclLowWatermarkNotification": sonusAtmExtVclLowWatermarkNotification,
       "sonusAtmExtVclBwHighDeviationNotification": sonusAtmExtVclBwHighDeviationNotification,
       "sonusAtmExtVclBwLowDeviationNotification": sonusAtmExtVclBwLowDeviationNotification,
       "sonusAtmExtVclMIBNotificationsObjects": sonusAtmExtVclMIBNotificationsObjects}
)
