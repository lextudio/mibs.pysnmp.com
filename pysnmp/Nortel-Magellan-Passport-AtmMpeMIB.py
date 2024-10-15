# SNMP MIB module (Nortel-Magellan-Passport-AtmMpeMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AtmMpeMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:19 2024
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
 Integer32,
 InterfaceIndex,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "Link")

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

_AtmMpe_ObjectIdentity = ObjectIdentity
atmMpe = _AtmMpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118)
)
_AtmMpeRowStatusTable_Object = MibTable
atmMpeRowStatusTable = _AtmMpeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 1)
)
if mibBuilder.loadTexts:
    atmMpeRowStatusTable.setStatus("mandatory")
_AtmMpeRowStatusEntry_Object = MibTableRow
atmMpeRowStatusEntry = _AtmMpeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 1, 1)
)
atmMpeRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
)
if mibBuilder.loadTexts:
    atmMpeRowStatusEntry.setStatus("mandatory")
_AtmMpeRowStatus_Type = RowStatus
_AtmMpeRowStatus_Object = MibTableColumn
atmMpeRowStatus = _AtmMpeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 1, 1, 1),
    _AtmMpeRowStatus_Type()
)
atmMpeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeRowStatus.setStatus("mandatory")
_AtmMpeComponentName_Type = DisplayString
_AtmMpeComponentName_Object = MibTableColumn
atmMpeComponentName = _AtmMpeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 1, 1, 2),
    _AtmMpeComponentName_Type()
)
atmMpeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeComponentName.setStatus("mandatory")
_AtmMpeStorageType_Type = StorageType
_AtmMpeStorageType_Object = MibTableColumn
atmMpeStorageType = _AtmMpeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 1, 1, 4),
    _AtmMpeStorageType_Type()
)
atmMpeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeStorageType.setStatus("mandatory")


class _AtmMpeIndex_Type(Integer32):
    """Custom type atmMpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmMpeIndex_Type.__name__ = "Integer32"
_AtmMpeIndex_Object = MibTableColumn
atmMpeIndex = _AtmMpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 1, 1, 10),
    _AtmMpeIndex_Type()
)
atmMpeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMpeIndex.setStatus("mandatory")
_AtmMpeAc_ObjectIdentity = ObjectIdentity
atmMpeAc = _AtmMpeAc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2)
)
_AtmMpeAcRowStatusTable_Object = MibTable
atmMpeAcRowStatusTable = _AtmMpeAcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 1)
)
if mibBuilder.loadTexts:
    atmMpeAcRowStatusTable.setStatus("mandatory")
_AtmMpeAcRowStatusEntry_Object = MibTableRow
atmMpeAcRowStatusEntry = _AtmMpeAcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 1, 1)
)
atmMpeAcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    atmMpeAcRowStatusEntry.setStatus("mandatory")
_AtmMpeAcRowStatus_Type = RowStatus
_AtmMpeAcRowStatus_Object = MibTableColumn
atmMpeAcRowStatus = _AtmMpeAcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 1, 1, 1),
    _AtmMpeAcRowStatus_Type()
)
atmMpeAcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeAcRowStatus.setStatus("mandatory")
_AtmMpeAcComponentName_Type = DisplayString
_AtmMpeAcComponentName_Object = MibTableColumn
atmMpeAcComponentName = _AtmMpeAcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 1, 1, 2),
    _AtmMpeAcComponentName_Type()
)
atmMpeAcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcComponentName.setStatus("mandatory")
_AtmMpeAcStorageType_Type = StorageType
_AtmMpeAcStorageType_Object = MibTableColumn
atmMpeAcStorageType = _AtmMpeAcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 1, 1, 4),
    _AtmMpeAcStorageType_Type()
)
atmMpeAcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcStorageType.setStatus("mandatory")


class _AtmMpeAcIndex_Type(Integer32):
    """Custom type atmMpeAcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmMpeAcIndex_Type.__name__ = "Integer32"
_AtmMpeAcIndex_Object = MibTableColumn
atmMpeAcIndex = _AtmMpeAcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 1, 1, 10),
    _AtmMpeAcIndex_Type()
)
atmMpeAcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmMpeAcIndex.setStatus("mandatory")
_AtmMpeAcProvTable_Object = MibTable
atmMpeAcProvTable = _AtmMpeAcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 10)
)
if mibBuilder.loadTexts:
    atmMpeAcProvTable.setStatus("mandatory")
_AtmMpeAcProvEntry_Object = MibTableRow
atmMpeAcProvEntry = _AtmMpeAcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 10, 1)
)
atmMpeAcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    atmMpeAcProvEntry.setStatus("mandatory")
_AtmMpeAcAtmConnection_Type = Link
_AtmMpeAcAtmConnection_Object = MibTableColumn
atmMpeAcAtmConnection = _AtmMpeAcAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 10, 1, 1),
    _AtmMpeAcAtmConnection_Type()
)
atmMpeAcAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeAcAtmConnection.setStatus("mandatory")


class _AtmMpeAcIpCoS_Type(Unsigned32):
    """Custom type atmMpeAcIpCoS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AtmMpeAcIpCoS_Type.__name__ = "Unsigned32"
_AtmMpeAcIpCoS_Object = MibTableColumn
atmMpeAcIpCoS = _AtmMpeAcIpCoS_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 10, 1, 2),
    _AtmMpeAcIpCoS_Type()
)
atmMpeAcIpCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeAcIpCoS.setStatus("mandatory")
_AtmMpeAcStateTable_Object = MibTable
atmMpeAcStateTable = _AtmMpeAcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 11)
)
if mibBuilder.loadTexts:
    atmMpeAcStateTable.setStatus("mandatory")
_AtmMpeAcStateEntry_Object = MibTableRow
atmMpeAcStateEntry = _AtmMpeAcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 11, 1)
)
atmMpeAcStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    atmMpeAcStateEntry.setStatus("mandatory")


class _AtmMpeAcAdminState_Type(Integer32):
    """Custom type atmMpeAcAdminState based on Integer32"""
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


_AtmMpeAcAdminState_Type.__name__ = "Integer32"
_AtmMpeAcAdminState_Object = MibTableColumn
atmMpeAcAdminState = _AtmMpeAcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 11, 1, 1),
    _AtmMpeAcAdminState_Type()
)
atmMpeAcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcAdminState.setStatus("mandatory")


class _AtmMpeAcOperationalState_Type(Integer32):
    """Custom type atmMpeAcOperationalState based on Integer32"""
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


_AtmMpeAcOperationalState_Type.__name__ = "Integer32"
_AtmMpeAcOperationalState_Object = MibTableColumn
atmMpeAcOperationalState = _AtmMpeAcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 11, 1, 2),
    _AtmMpeAcOperationalState_Type()
)
atmMpeAcOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcOperationalState.setStatus("mandatory")


class _AtmMpeAcUsageState_Type(Integer32):
    """Custom type atmMpeAcUsageState based on Integer32"""
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


_AtmMpeAcUsageState_Type.__name__ = "Integer32"
_AtmMpeAcUsageState_Object = MibTableColumn
atmMpeAcUsageState = _AtmMpeAcUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 11, 1, 3),
    _AtmMpeAcUsageState_Type()
)
atmMpeAcUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcUsageState.setStatus("mandatory")
_AtmMpeAcOperTable_Object = MibTable
atmMpeAcOperTable = _AtmMpeAcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 12)
)
if mibBuilder.loadTexts:
    atmMpeAcOperTable.setStatus("mandatory")
_AtmMpeAcOperEntry_Object = MibTableRow
atmMpeAcOperEntry = _AtmMpeAcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 12, 1)
)
atmMpeAcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    atmMpeAcOperEntry.setStatus("mandatory")
_AtmMpeAcSpeed_Type = Counter32
_AtmMpeAcSpeed_Object = MibTableColumn
atmMpeAcSpeed = _AtmMpeAcSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 12, 1, 1),
    _AtmMpeAcSpeed_Type()
)
atmMpeAcSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcSpeed.setStatus("mandatory")
_AtmMpeAcStatsTable_Object = MibTable
atmMpeAcStatsTable = _AtmMpeAcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 13)
)
if mibBuilder.loadTexts:
    atmMpeAcStatsTable.setStatus("mandatory")
_AtmMpeAcStatsEntry_Object = MibTableRow
atmMpeAcStatsEntry = _AtmMpeAcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 13, 1)
)
atmMpeAcStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    atmMpeAcStatsEntry.setStatus("mandatory")
_AtmMpeAcOutPackets_Type = Counter32
_AtmMpeAcOutPackets_Object = MibTableColumn
atmMpeAcOutPackets = _AtmMpeAcOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 13, 1, 1),
    _AtmMpeAcOutPackets_Type()
)
atmMpeAcOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcOutPackets.setStatus("mandatory")
_AtmMpeAcOutOctets_Type = Counter32
_AtmMpeAcOutOctets_Object = MibTableColumn
atmMpeAcOutOctets = _AtmMpeAcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 13, 1, 2),
    _AtmMpeAcOutOctets_Type()
)
atmMpeAcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcOutOctets.setStatus("mandatory")
_AtmMpeAcOutDiscards_Type = Counter32
_AtmMpeAcOutDiscards_Object = MibTableColumn
atmMpeAcOutDiscards = _AtmMpeAcOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 13, 1, 3),
    _AtmMpeAcOutDiscards_Type()
)
atmMpeAcOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcOutDiscards.setStatus("mandatory")
_AtmMpeAcInPackets_Type = Counter32
_AtmMpeAcInPackets_Object = MibTableColumn
atmMpeAcInPackets = _AtmMpeAcInPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 13, 1, 4),
    _AtmMpeAcInPackets_Type()
)
atmMpeAcInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcInPackets.setStatus("mandatory")
_AtmMpeAcInOctets_Type = Counter32
_AtmMpeAcInOctets_Object = MibTableColumn
atmMpeAcInOctets = _AtmMpeAcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 13, 1, 5),
    _AtmMpeAcInOctets_Type()
)
atmMpeAcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcInOctets.setStatus("mandatory")
_AtmMpeAcInUnknownProtos_Type = Counter32
_AtmMpeAcInUnknownProtos_Object = MibTableColumn
atmMpeAcInUnknownProtos = _AtmMpeAcInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 13, 1, 6),
    _AtmMpeAcInUnknownProtos_Type()
)
atmMpeAcInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcInUnknownProtos.setStatus("mandatory")
_AtmMpeAcInErrors_Type = Counter32
_AtmMpeAcInErrors_Object = MibTableColumn
atmMpeAcInErrors = _AtmMpeAcInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 2, 13, 1, 7),
    _AtmMpeAcInErrors_Type()
)
atmMpeAcInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAcInErrors.setStatus("mandatory")
_AtmMpeCidDataTable_Object = MibTable
atmMpeCidDataTable = _AtmMpeCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 10)
)
if mibBuilder.loadTexts:
    atmMpeCidDataTable.setStatus("mandatory")
_AtmMpeCidDataEntry_Object = MibTableRow
atmMpeCidDataEntry = _AtmMpeCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 10, 1)
)
atmMpeCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
)
if mibBuilder.loadTexts:
    atmMpeCidDataEntry.setStatus("mandatory")


class _AtmMpeCustomerIdentifier_Type(Unsigned32):
    """Custom type atmMpeCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_AtmMpeCustomerIdentifier_Type.__name__ = "Unsigned32"
_AtmMpeCustomerIdentifier_Object = MibTableColumn
atmMpeCustomerIdentifier = _AtmMpeCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 10, 1, 1),
    _AtmMpeCustomerIdentifier_Type()
)
atmMpeCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeCustomerIdentifier.setStatus("mandatory")
_AtmMpeIfEntryTable_Object = MibTable
atmMpeIfEntryTable = _AtmMpeIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 11)
)
if mibBuilder.loadTexts:
    atmMpeIfEntryTable.setStatus("mandatory")
_AtmMpeIfEntryEntry_Object = MibTableRow
atmMpeIfEntryEntry = _AtmMpeIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 11, 1)
)
atmMpeIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
)
if mibBuilder.loadTexts:
    atmMpeIfEntryEntry.setStatus("mandatory")


class _AtmMpeIfAdminStatus_Type(Integer32):
    """Custom type atmMpeIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_AtmMpeIfAdminStatus_Type.__name__ = "Integer32"
_AtmMpeIfAdminStatus_Object = MibTableColumn
atmMpeIfAdminStatus = _AtmMpeIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 11, 1, 1),
    _AtmMpeIfAdminStatus_Type()
)
atmMpeIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeIfAdminStatus.setStatus("mandatory")


class _AtmMpeIfIndex_Type(InterfaceIndex):
    """Custom type atmMpeIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmMpeIfIndex_Type.__name__ = "InterfaceIndex"
_AtmMpeIfIndex_Object = MibTableColumn
atmMpeIfIndex = _AtmMpeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 11, 1, 2),
    _AtmMpeIfIndex_Type()
)
atmMpeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeIfIndex.setStatus("mandatory")
_AtmMpeProvTable_Object = MibTable
atmMpeProvTable = _AtmMpeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 12)
)
if mibBuilder.loadTexts:
    atmMpeProvTable.setStatus("mandatory")
_AtmMpeProvEntry_Object = MibTableRow
atmMpeProvEntry = _AtmMpeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 12, 1)
)
atmMpeProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
)
if mibBuilder.loadTexts:
    atmMpeProvEntry.setStatus("mandatory")


class _AtmMpeMaxTransmissionUnit_Type(Unsigned32):
    """Custom type atmMpeMaxTransmissionUnit based on Unsigned32"""
    defaultValue = 9188

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 9188),
    )


_AtmMpeMaxTransmissionUnit_Type.__name__ = "Unsigned32"
_AtmMpeMaxTransmissionUnit_Object = MibTableColumn
atmMpeMaxTransmissionUnit = _AtmMpeMaxTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 12, 1, 1),
    _AtmMpeMaxTransmissionUnit_Type()
)
atmMpeMaxTransmissionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeMaxTransmissionUnit.setStatus("mandatory")


class _AtmMpeEncapType_Type(Integer32):
    """Custom type atmMpeEncapType based on Integer32"""
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
        *(("ipVcEncap", 2),
          ("ipxVcEncap", 3),
          ("llcEncap", 1))
    )


_AtmMpeEncapType_Type.__name__ = "Integer32"
_AtmMpeEncapType_Object = MibTableColumn
atmMpeEncapType = _AtmMpeEncapType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 12, 1, 2),
    _AtmMpeEncapType_Type()
)
atmMpeEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeEncapType.setStatus("mandatory")
_AtmMpeIlsForwarder_Type = Link
_AtmMpeIlsForwarder_Object = MibTableColumn
atmMpeIlsForwarder = _AtmMpeIlsForwarder_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 12, 1, 3),
    _AtmMpeIlsForwarder_Type()
)
atmMpeIlsForwarder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeIlsForwarder.setStatus("mandatory")
_AtmMpeMediaProvTable_Object = MibTable
atmMpeMediaProvTable = _AtmMpeMediaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 13)
)
if mibBuilder.loadTexts:
    atmMpeMediaProvTable.setStatus("mandatory")
_AtmMpeMediaProvEntry_Object = MibTableRow
atmMpeMediaProvEntry = _AtmMpeMediaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 13, 1)
)
atmMpeMediaProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
)
if mibBuilder.loadTexts:
    atmMpeMediaProvEntry.setStatus("mandatory")
_AtmMpeLinkToProtocolPort_Type = Link
_AtmMpeLinkToProtocolPort_Object = MibTableColumn
atmMpeLinkToProtocolPort = _AtmMpeLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 13, 1, 1),
    _AtmMpeLinkToProtocolPort_Type()
)
atmMpeLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmMpeLinkToProtocolPort.setStatus("mandatory")
_AtmMpeStateTable_Object = MibTable
atmMpeStateTable = _AtmMpeStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 14)
)
if mibBuilder.loadTexts:
    atmMpeStateTable.setStatus("mandatory")
_AtmMpeStateEntry_Object = MibTableRow
atmMpeStateEntry = _AtmMpeStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 14, 1)
)
atmMpeStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
)
if mibBuilder.loadTexts:
    atmMpeStateEntry.setStatus("mandatory")


class _AtmMpeAdminState_Type(Integer32):
    """Custom type atmMpeAdminState based on Integer32"""
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


_AtmMpeAdminState_Type.__name__ = "Integer32"
_AtmMpeAdminState_Object = MibTableColumn
atmMpeAdminState = _AtmMpeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 14, 1, 1),
    _AtmMpeAdminState_Type()
)
atmMpeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeAdminState.setStatus("mandatory")


class _AtmMpeOperationalState_Type(Integer32):
    """Custom type atmMpeOperationalState based on Integer32"""
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


_AtmMpeOperationalState_Type.__name__ = "Integer32"
_AtmMpeOperationalState_Object = MibTableColumn
atmMpeOperationalState = _AtmMpeOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 14, 1, 2),
    _AtmMpeOperationalState_Type()
)
atmMpeOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeOperationalState.setStatus("mandatory")


class _AtmMpeUsageState_Type(Integer32):
    """Custom type atmMpeUsageState based on Integer32"""
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


_AtmMpeUsageState_Type.__name__ = "Integer32"
_AtmMpeUsageState_Object = MibTableColumn
atmMpeUsageState = _AtmMpeUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 14, 1, 3),
    _AtmMpeUsageState_Type()
)
atmMpeUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeUsageState.setStatus("mandatory")
_AtmMpeOperStatusTable_Object = MibTable
atmMpeOperStatusTable = _AtmMpeOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 15)
)
if mibBuilder.loadTexts:
    atmMpeOperStatusTable.setStatus("mandatory")
_AtmMpeOperStatusEntry_Object = MibTableRow
atmMpeOperStatusEntry = _AtmMpeOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 15, 1)
)
atmMpeOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmMpeMIB", "atmMpeIndex"),
)
if mibBuilder.loadTexts:
    atmMpeOperStatusEntry.setStatus("mandatory")


class _AtmMpeSnmpOperStatus_Type(Integer32):
    """Custom type atmMpeSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_AtmMpeSnmpOperStatus_Type.__name__ = "Integer32"
_AtmMpeSnmpOperStatus_Object = MibTableColumn
atmMpeSnmpOperStatus = _AtmMpeSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 118, 15, 1, 1),
    _AtmMpeSnmpOperStatus_Type()
)
atmMpeSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmMpeSnmpOperStatus.setStatus("mandatory")
_AtmMpeMIB_ObjectIdentity = ObjectIdentity
atmMpeMIB = _AtmMpeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 65)
)
_AtmMpeGroup_ObjectIdentity = ObjectIdentity
atmMpeGroup = _AtmMpeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 65, 1)
)
_AtmMpeGroupBD_ObjectIdentity = ObjectIdentity
atmMpeGroupBD = _AtmMpeGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 65, 1, 4)
)
_AtmMpeGroupBD00_ObjectIdentity = ObjectIdentity
atmMpeGroupBD00 = _AtmMpeGroupBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 65, 1, 4, 1)
)
_AtmMpeGroupBD00A_ObjectIdentity = ObjectIdentity
atmMpeGroupBD00A = _AtmMpeGroupBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 65, 1, 4, 1, 2)
)
_AtmMpeCapabilities_ObjectIdentity = ObjectIdentity
atmMpeCapabilities = _AtmMpeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 65, 3)
)
_AtmMpeCapabilitiesBD_ObjectIdentity = ObjectIdentity
atmMpeCapabilitiesBD = _AtmMpeCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 65, 3, 4)
)
_AtmMpeCapabilitiesBD00_ObjectIdentity = ObjectIdentity
atmMpeCapabilitiesBD00 = _AtmMpeCapabilitiesBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 65, 3, 4, 1)
)
_AtmMpeCapabilitiesBD00A_ObjectIdentity = ObjectIdentity
atmMpeCapabilitiesBD00A = _AtmMpeCapabilitiesBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 65, 3, 4, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AtmMpeMIB",
    **{"atmMpe": atmMpe,
       "atmMpeRowStatusTable": atmMpeRowStatusTable,
       "atmMpeRowStatusEntry": atmMpeRowStatusEntry,
       "atmMpeRowStatus": atmMpeRowStatus,
       "atmMpeComponentName": atmMpeComponentName,
       "atmMpeStorageType": atmMpeStorageType,
       "atmMpeIndex": atmMpeIndex,
       "atmMpeAc": atmMpeAc,
       "atmMpeAcRowStatusTable": atmMpeAcRowStatusTable,
       "atmMpeAcRowStatusEntry": atmMpeAcRowStatusEntry,
       "atmMpeAcRowStatus": atmMpeAcRowStatus,
       "atmMpeAcComponentName": atmMpeAcComponentName,
       "atmMpeAcStorageType": atmMpeAcStorageType,
       "atmMpeAcIndex": atmMpeAcIndex,
       "atmMpeAcProvTable": atmMpeAcProvTable,
       "atmMpeAcProvEntry": atmMpeAcProvEntry,
       "atmMpeAcAtmConnection": atmMpeAcAtmConnection,
       "atmMpeAcIpCoS": atmMpeAcIpCoS,
       "atmMpeAcStateTable": atmMpeAcStateTable,
       "atmMpeAcStateEntry": atmMpeAcStateEntry,
       "atmMpeAcAdminState": atmMpeAcAdminState,
       "atmMpeAcOperationalState": atmMpeAcOperationalState,
       "atmMpeAcUsageState": atmMpeAcUsageState,
       "atmMpeAcOperTable": atmMpeAcOperTable,
       "atmMpeAcOperEntry": atmMpeAcOperEntry,
       "atmMpeAcSpeed": atmMpeAcSpeed,
       "atmMpeAcStatsTable": atmMpeAcStatsTable,
       "atmMpeAcStatsEntry": atmMpeAcStatsEntry,
       "atmMpeAcOutPackets": atmMpeAcOutPackets,
       "atmMpeAcOutOctets": atmMpeAcOutOctets,
       "atmMpeAcOutDiscards": atmMpeAcOutDiscards,
       "atmMpeAcInPackets": atmMpeAcInPackets,
       "atmMpeAcInOctets": atmMpeAcInOctets,
       "atmMpeAcInUnknownProtos": atmMpeAcInUnknownProtos,
       "atmMpeAcInErrors": atmMpeAcInErrors,
       "atmMpeCidDataTable": atmMpeCidDataTable,
       "atmMpeCidDataEntry": atmMpeCidDataEntry,
       "atmMpeCustomerIdentifier": atmMpeCustomerIdentifier,
       "atmMpeIfEntryTable": atmMpeIfEntryTable,
       "atmMpeIfEntryEntry": atmMpeIfEntryEntry,
       "atmMpeIfAdminStatus": atmMpeIfAdminStatus,
       "atmMpeIfIndex": atmMpeIfIndex,
       "atmMpeProvTable": atmMpeProvTable,
       "atmMpeProvEntry": atmMpeProvEntry,
       "atmMpeMaxTransmissionUnit": atmMpeMaxTransmissionUnit,
       "atmMpeEncapType": atmMpeEncapType,
       "atmMpeIlsForwarder": atmMpeIlsForwarder,
       "atmMpeMediaProvTable": atmMpeMediaProvTable,
       "atmMpeMediaProvEntry": atmMpeMediaProvEntry,
       "atmMpeLinkToProtocolPort": atmMpeLinkToProtocolPort,
       "atmMpeStateTable": atmMpeStateTable,
       "atmMpeStateEntry": atmMpeStateEntry,
       "atmMpeAdminState": atmMpeAdminState,
       "atmMpeOperationalState": atmMpeOperationalState,
       "atmMpeUsageState": atmMpeUsageState,
       "atmMpeOperStatusTable": atmMpeOperStatusTable,
       "atmMpeOperStatusEntry": atmMpeOperStatusEntry,
       "atmMpeSnmpOperStatus": atmMpeSnmpOperStatus,
       "atmMpeMIB": atmMpeMIB,
       "atmMpeGroup": atmMpeGroup,
       "atmMpeGroupBD": atmMpeGroupBD,
       "atmMpeGroupBD00": atmMpeGroupBD00,
       "atmMpeGroupBD00A": atmMpeGroupBD00A,
       "atmMpeCapabilities": atmMpeCapabilities,
       "atmMpeCapabilitiesBD": atmMpeCapabilitiesBD,
       "atmMpeCapabilitiesBD00": atmMpeCapabilitiesBD00,
       "atmMpeCapabilitiesBD00A": atmMpeCapabilitiesBD00A}
)
