# SNMP MIB module (Nortel-MsCarrier-MscPassport-AtmMpeMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AtmMpeMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:53 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "Link")

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

_MscAtmMpe_ObjectIdentity = ObjectIdentity
mscAtmMpe = _MscAtmMpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118)
)
_MscAtmMpeRowStatusTable_Object = MibTable
mscAtmMpeRowStatusTable = _MscAtmMpeRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1)
)
if mibBuilder.loadTexts:
    mscAtmMpeRowStatusTable.setStatus("mandatory")
_MscAtmMpeRowStatusEntry_Object = MibTableRow
mscAtmMpeRowStatusEntry = _MscAtmMpeRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1)
)
mscAtmMpeRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeRowStatusEntry.setStatus("mandatory")
_MscAtmMpeRowStatus_Type = RowStatus
_MscAtmMpeRowStatus_Object = MibTableColumn
mscAtmMpeRowStatus = _MscAtmMpeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1, 1),
    _MscAtmMpeRowStatus_Type()
)
mscAtmMpeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeRowStatus.setStatus("mandatory")
_MscAtmMpeComponentName_Type = DisplayString
_MscAtmMpeComponentName_Object = MibTableColumn
mscAtmMpeComponentName = _MscAtmMpeComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1, 2),
    _MscAtmMpeComponentName_Type()
)
mscAtmMpeComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeComponentName.setStatus("mandatory")
_MscAtmMpeStorageType_Type = StorageType
_MscAtmMpeStorageType_Object = MibTableColumn
mscAtmMpeStorageType = _MscAtmMpeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1, 4),
    _MscAtmMpeStorageType_Type()
)
mscAtmMpeStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeStorageType.setStatus("mandatory")


class _MscAtmMpeIndex_Type(Integer32):
    """Custom type mscAtmMpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscAtmMpeIndex_Type.__name__ = "Integer32"
_MscAtmMpeIndex_Object = MibTableColumn
mscAtmMpeIndex = _MscAtmMpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1, 10),
    _MscAtmMpeIndex_Type()
)
mscAtmMpeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmMpeIndex.setStatus("mandatory")
_MscAtmMpeAc_ObjectIdentity = ObjectIdentity
mscAtmMpeAc = _MscAtmMpeAc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2)
)
_MscAtmMpeAcRowStatusTable_Object = MibTable
mscAtmMpeAcRowStatusTable = _MscAtmMpeAcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1)
)
if mibBuilder.loadTexts:
    mscAtmMpeAcRowStatusTable.setStatus("mandatory")
_MscAtmMpeAcRowStatusEntry_Object = MibTableRow
mscAtmMpeAcRowStatusEntry = _MscAtmMpeAcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1)
)
mscAtmMpeAcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeAcRowStatusEntry.setStatus("mandatory")
_MscAtmMpeAcRowStatus_Type = RowStatus
_MscAtmMpeAcRowStatus_Object = MibTableColumn
mscAtmMpeAcRowStatus = _MscAtmMpeAcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1, 1),
    _MscAtmMpeAcRowStatus_Type()
)
mscAtmMpeAcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeAcRowStatus.setStatus("mandatory")
_MscAtmMpeAcComponentName_Type = DisplayString
_MscAtmMpeAcComponentName_Object = MibTableColumn
mscAtmMpeAcComponentName = _MscAtmMpeAcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1, 2),
    _MscAtmMpeAcComponentName_Type()
)
mscAtmMpeAcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcComponentName.setStatus("mandatory")
_MscAtmMpeAcStorageType_Type = StorageType
_MscAtmMpeAcStorageType_Object = MibTableColumn
mscAtmMpeAcStorageType = _MscAtmMpeAcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1, 4),
    _MscAtmMpeAcStorageType_Type()
)
mscAtmMpeAcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcStorageType.setStatus("mandatory")


class _MscAtmMpeAcIndex_Type(Integer32):
    """Custom type mscAtmMpeAcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscAtmMpeAcIndex_Type.__name__ = "Integer32"
_MscAtmMpeAcIndex_Object = MibTableColumn
mscAtmMpeAcIndex = _MscAtmMpeAcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1, 10),
    _MscAtmMpeAcIndex_Type()
)
mscAtmMpeAcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmMpeAcIndex.setStatus("mandatory")
_MscAtmMpeAcProvTable_Object = MibTable
mscAtmMpeAcProvTable = _MscAtmMpeAcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 10)
)
if mibBuilder.loadTexts:
    mscAtmMpeAcProvTable.setStatus("mandatory")
_MscAtmMpeAcProvEntry_Object = MibTableRow
mscAtmMpeAcProvEntry = _MscAtmMpeAcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 10, 1)
)
mscAtmMpeAcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeAcProvEntry.setStatus("mandatory")
_MscAtmMpeAcAtmConnection_Type = Link
_MscAtmMpeAcAtmConnection_Object = MibTableColumn
mscAtmMpeAcAtmConnection = _MscAtmMpeAcAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 10, 1, 1),
    _MscAtmMpeAcAtmConnection_Type()
)
mscAtmMpeAcAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeAcAtmConnection.setStatus("mandatory")


class _MscAtmMpeAcIpCoS_Type(Unsigned32):
    """Custom type mscAtmMpeAcIpCoS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscAtmMpeAcIpCoS_Type.__name__ = "Unsigned32"
_MscAtmMpeAcIpCoS_Object = MibTableColumn
mscAtmMpeAcIpCoS = _MscAtmMpeAcIpCoS_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 10, 1, 2),
    _MscAtmMpeAcIpCoS_Type()
)
mscAtmMpeAcIpCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeAcIpCoS.setStatus("mandatory")
_MscAtmMpeAcStateTable_Object = MibTable
mscAtmMpeAcStateTable = _MscAtmMpeAcStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11)
)
if mibBuilder.loadTexts:
    mscAtmMpeAcStateTable.setStatus("mandatory")
_MscAtmMpeAcStateEntry_Object = MibTableRow
mscAtmMpeAcStateEntry = _MscAtmMpeAcStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11, 1)
)
mscAtmMpeAcStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeAcStateEntry.setStatus("mandatory")


class _MscAtmMpeAcAdminState_Type(Integer32):
    """Custom type mscAtmMpeAcAdminState based on Integer32"""
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


_MscAtmMpeAcAdminState_Type.__name__ = "Integer32"
_MscAtmMpeAcAdminState_Object = MibTableColumn
mscAtmMpeAcAdminState = _MscAtmMpeAcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11, 1, 1),
    _MscAtmMpeAcAdminState_Type()
)
mscAtmMpeAcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcAdminState.setStatus("mandatory")


class _MscAtmMpeAcOperationalState_Type(Integer32):
    """Custom type mscAtmMpeAcOperationalState based on Integer32"""
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


_MscAtmMpeAcOperationalState_Type.__name__ = "Integer32"
_MscAtmMpeAcOperationalState_Object = MibTableColumn
mscAtmMpeAcOperationalState = _MscAtmMpeAcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11, 1, 2),
    _MscAtmMpeAcOperationalState_Type()
)
mscAtmMpeAcOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcOperationalState.setStatus("mandatory")


class _MscAtmMpeAcUsageState_Type(Integer32):
    """Custom type mscAtmMpeAcUsageState based on Integer32"""
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


_MscAtmMpeAcUsageState_Type.__name__ = "Integer32"
_MscAtmMpeAcUsageState_Object = MibTableColumn
mscAtmMpeAcUsageState = _MscAtmMpeAcUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11, 1, 3),
    _MscAtmMpeAcUsageState_Type()
)
mscAtmMpeAcUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcUsageState.setStatus("mandatory")
_MscAtmMpeAcOperTable_Object = MibTable
mscAtmMpeAcOperTable = _MscAtmMpeAcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 12)
)
if mibBuilder.loadTexts:
    mscAtmMpeAcOperTable.setStatus("mandatory")
_MscAtmMpeAcOperEntry_Object = MibTableRow
mscAtmMpeAcOperEntry = _MscAtmMpeAcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 12, 1)
)
mscAtmMpeAcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeAcOperEntry.setStatus("mandatory")
_MscAtmMpeAcSpeed_Type = Counter32
_MscAtmMpeAcSpeed_Object = MibTableColumn
mscAtmMpeAcSpeed = _MscAtmMpeAcSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 12, 1, 1),
    _MscAtmMpeAcSpeed_Type()
)
mscAtmMpeAcSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcSpeed.setStatus("mandatory")
_MscAtmMpeAcStatsTable_Object = MibTable
mscAtmMpeAcStatsTable = _MscAtmMpeAcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13)
)
if mibBuilder.loadTexts:
    mscAtmMpeAcStatsTable.setStatus("mandatory")
_MscAtmMpeAcStatsEntry_Object = MibTableRow
mscAtmMpeAcStatsEntry = _MscAtmMpeAcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1)
)
mscAtmMpeAcStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeAcStatsEntry.setStatus("mandatory")
_MscAtmMpeAcOutPackets_Type = Counter32
_MscAtmMpeAcOutPackets_Object = MibTableColumn
mscAtmMpeAcOutPackets = _MscAtmMpeAcOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 1),
    _MscAtmMpeAcOutPackets_Type()
)
mscAtmMpeAcOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcOutPackets.setStatus("mandatory")
_MscAtmMpeAcOutOctets_Type = Counter32
_MscAtmMpeAcOutOctets_Object = MibTableColumn
mscAtmMpeAcOutOctets = _MscAtmMpeAcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 2),
    _MscAtmMpeAcOutOctets_Type()
)
mscAtmMpeAcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcOutOctets.setStatus("mandatory")
_MscAtmMpeAcOutDiscards_Type = Counter32
_MscAtmMpeAcOutDiscards_Object = MibTableColumn
mscAtmMpeAcOutDiscards = _MscAtmMpeAcOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 3),
    _MscAtmMpeAcOutDiscards_Type()
)
mscAtmMpeAcOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcOutDiscards.setStatus("mandatory")
_MscAtmMpeAcInPackets_Type = Counter32
_MscAtmMpeAcInPackets_Object = MibTableColumn
mscAtmMpeAcInPackets = _MscAtmMpeAcInPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 4),
    _MscAtmMpeAcInPackets_Type()
)
mscAtmMpeAcInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcInPackets.setStatus("mandatory")
_MscAtmMpeAcInOctets_Type = Counter32
_MscAtmMpeAcInOctets_Object = MibTableColumn
mscAtmMpeAcInOctets = _MscAtmMpeAcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 5),
    _MscAtmMpeAcInOctets_Type()
)
mscAtmMpeAcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcInOctets.setStatus("mandatory")
_MscAtmMpeAcInUnknownProtos_Type = Counter32
_MscAtmMpeAcInUnknownProtos_Object = MibTableColumn
mscAtmMpeAcInUnknownProtos = _MscAtmMpeAcInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 6),
    _MscAtmMpeAcInUnknownProtos_Type()
)
mscAtmMpeAcInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcInUnknownProtos.setStatus("mandatory")
_MscAtmMpeAcInErrors_Type = Counter32
_MscAtmMpeAcInErrors_Object = MibTableColumn
mscAtmMpeAcInErrors = _MscAtmMpeAcInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 7),
    _MscAtmMpeAcInErrors_Type()
)
mscAtmMpeAcInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAcInErrors.setStatus("mandatory")
_MscAtmMpeCidDataTable_Object = MibTable
mscAtmMpeCidDataTable = _MscAtmMpeCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 10)
)
if mibBuilder.loadTexts:
    mscAtmMpeCidDataTable.setStatus("mandatory")
_MscAtmMpeCidDataEntry_Object = MibTableRow
mscAtmMpeCidDataEntry = _MscAtmMpeCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 10, 1)
)
mscAtmMpeCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeCidDataEntry.setStatus("mandatory")


class _MscAtmMpeCustomerIdentifier_Type(Unsigned32):
    """Custom type mscAtmMpeCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscAtmMpeCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscAtmMpeCustomerIdentifier_Object = MibTableColumn
mscAtmMpeCustomerIdentifier = _MscAtmMpeCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 10, 1, 1),
    _MscAtmMpeCustomerIdentifier_Type()
)
mscAtmMpeCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeCustomerIdentifier.setStatus("mandatory")
_MscAtmMpeIfEntryTable_Object = MibTable
mscAtmMpeIfEntryTable = _MscAtmMpeIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 11)
)
if mibBuilder.loadTexts:
    mscAtmMpeIfEntryTable.setStatus("mandatory")
_MscAtmMpeIfEntryEntry_Object = MibTableRow
mscAtmMpeIfEntryEntry = _MscAtmMpeIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 11, 1)
)
mscAtmMpeIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeIfEntryEntry.setStatus("mandatory")


class _MscAtmMpeIfAdminStatus_Type(Integer32):
    """Custom type mscAtmMpeIfAdminStatus based on Integer32"""
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


_MscAtmMpeIfAdminStatus_Type.__name__ = "Integer32"
_MscAtmMpeIfAdminStatus_Object = MibTableColumn
mscAtmMpeIfAdminStatus = _MscAtmMpeIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 11, 1, 1),
    _MscAtmMpeIfAdminStatus_Type()
)
mscAtmMpeIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeIfAdminStatus.setStatus("mandatory")


class _MscAtmMpeIfIndex_Type(InterfaceIndex):
    """Custom type mscAtmMpeIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscAtmMpeIfIndex_Type.__name__ = "InterfaceIndex"
_MscAtmMpeIfIndex_Object = MibTableColumn
mscAtmMpeIfIndex = _MscAtmMpeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 11, 1, 2),
    _MscAtmMpeIfIndex_Type()
)
mscAtmMpeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeIfIndex.setStatus("mandatory")
_MscAtmMpeProvTable_Object = MibTable
mscAtmMpeProvTable = _MscAtmMpeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12)
)
if mibBuilder.loadTexts:
    mscAtmMpeProvTable.setStatus("mandatory")
_MscAtmMpeProvEntry_Object = MibTableRow
mscAtmMpeProvEntry = _MscAtmMpeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12, 1)
)
mscAtmMpeProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeProvEntry.setStatus("mandatory")


class _MscAtmMpeMaxTransmissionUnit_Type(Unsigned32):
    """Custom type mscAtmMpeMaxTransmissionUnit based on Unsigned32"""
    defaultValue = 9188

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 9188),
    )


_MscAtmMpeMaxTransmissionUnit_Type.__name__ = "Unsigned32"
_MscAtmMpeMaxTransmissionUnit_Object = MibTableColumn
mscAtmMpeMaxTransmissionUnit = _MscAtmMpeMaxTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12, 1, 1),
    _MscAtmMpeMaxTransmissionUnit_Type()
)
mscAtmMpeMaxTransmissionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeMaxTransmissionUnit.setStatus("mandatory")


class _MscAtmMpeEncapType_Type(Integer32):
    """Custom type mscAtmMpeEncapType based on Integer32"""
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


_MscAtmMpeEncapType_Type.__name__ = "Integer32"
_MscAtmMpeEncapType_Object = MibTableColumn
mscAtmMpeEncapType = _MscAtmMpeEncapType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12, 1, 2),
    _MscAtmMpeEncapType_Type()
)
mscAtmMpeEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeEncapType.setStatus("mandatory")
_MscAtmMpeIlsForwarder_Type = Link
_MscAtmMpeIlsForwarder_Object = MibTableColumn
mscAtmMpeIlsForwarder = _MscAtmMpeIlsForwarder_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12, 1, 3),
    _MscAtmMpeIlsForwarder_Type()
)
mscAtmMpeIlsForwarder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeIlsForwarder.setStatus("mandatory")
_MscAtmMpeMediaProvTable_Object = MibTable
mscAtmMpeMediaProvTable = _MscAtmMpeMediaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 13)
)
if mibBuilder.loadTexts:
    mscAtmMpeMediaProvTable.setStatus("mandatory")
_MscAtmMpeMediaProvEntry_Object = MibTableRow
mscAtmMpeMediaProvEntry = _MscAtmMpeMediaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 13, 1)
)
mscAtmMpeMediaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeMediaProvEntry.setStatus("mandatory")
_MscAtmMpeLinkToProtocolPort_Type = Link
_MscAtmMpeLinkToProtocolPort_Object = MibTableColumn
mscAtmMpeLinkToProtocolPort = _MscAtmMpeLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 13, 1, 1),
    _MscAtmMpeLinkToProtocolPort_Type()
)
mscAtmMpeLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmMpeLinkToProtocolPort.setStatus("mandatory")
_MscAtmMpeStateTable_Object = MibTable
mscAtmMpeStateTable = _MscAtmMpeStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14)
)
if mibBuilder.loadTexts:
    mscAtmMpeStateTable.setStatus("mandatory")
_MscAtmMpeStateEntry_Object = MibTableRow
mscAtmMpeStateEntry = _MscAtmMpeStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14, 1)
)
mscAtmMpeStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeStateEntry.setStatus("mandatory")


class _MscAtmMpeAdminState_Type(Integer32):
    """Custom type mscAtmMpeAdminState based on Integer32"""
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


_MscAtmMpeAdminState_Type.__name__ = "Integer32"
_MscAtmMpeAdminState_Object = MibTableColumn
mscAtmMpeAdminState = _MscAtmMpeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14, 1, 1),
    _MscAtmMpeAdminState_Type()
)
mscAtmMpeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeAdminState.setStatus("mandatory")


class _MscAtmMpeOperationalState_Type(Integer32):
    """Custom type mscAtmMpeOperationalState based on Integer32"""
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


_MscAtmMpeOperationalState_Type.__name__ = "Integer32"
_MscAtmMpeOperationalState_Object = MibTableColumn
mscAtmMpeOperationalState = _MscAtmMpeOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14, 1, 2),
    _MscAtmMpeOperationalState_Type()
)
mscAtmMpeOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeOperationalState.setStatus("mandatory")


class _MscAtmMpeUsageState_Type(Integer32):
    """Custom type mscAtmMpeUsageState based on Integer32"""
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


_MscAtmMpeUsageState_Type.__name__ = "Integer32"
_MscAtmMpeUsageState_Object = MibTableColumn
mscAtmMpeUsageState = _MscAtmMpeUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14, 1, 3),
    _MscAtmMpeUsageState_Type()
)
mscAtmMpeUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeUsageState.setStatus("mandatory")
_MscAtmMpeOperStatusTable_Object = MibTable
mscAtmMpeOperStatusTable = _MscAtmMpeOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 15)
)
if mibBuilder.loadTexts:
    mscAtmMpeOperStatusTable.setStatus("mandatory")
_MscAtmMpeOperStatusEntry_Object = MibTableRow
mscAtmMpeOperStatusEntry = _MscAtmMpeOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 15, 1)
)
mscAtmMpeOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"),
)
if mibBuilder.loadTexts:
    mscAtmMpeOperStatusEntry.setStatus("mandatory")


class _MscAtmMpeSnmpOperStatus_Type(Integer32):
    """Custom type mscAtmMpeSnmpOperStatus based on Integer32"""
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


_MscAtmMpeSnmpOperStatus_Type.__name__ = "Integer32"
_MscAtmMpeSnmpOperStatus_Object = MibTableColumn
mscAtmMpeSnmpOperStatus = _MscAtmMpeSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 15, 1, 1),
    _MscAtmMpeSnmpOperStatus_Type()
)
mscAtmMpeSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmMpeSnmpOperStatus.setStatus("mandatory")
_AtmMpeMIB_ObjectIdentity = ObjectIdentity
atmMpeMIB = _AtmMpeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65)
)
_AtmMpeGroup_ObjectIdentity = ObjectIdentity
atmMpeGroup = _AtmMpeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 1)
)
_AtmMpeGroupCA_ObjectIdentity = ObjectIdentity
atmMpeGroupCA = _AtmMpeGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 1, 1)
)
_AtmMpeGroupCA02_ObjectIdentity = ObjectIdentity
atmMpeGroupCA02 = _AtmMpeGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 1, 1, 3)
)
_AtmMpeGroupCA02A_ObjectIdentity = ObjectIdentity
atmMpeGroupCA02A = _AtmMpeGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 1, 1, 3, 2)
)
_AtmMpeCapabilities_ObjectIdentity = ObjectIdentity
atmMpeCapabilities = _AtmMpeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 3)
)
_AtmMpeCapabilitiesCA_ObjectIdentity = ObjectIdentity
atmMpeCapabilitiesCA = _AtmMpeCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 3, 1)
)
_AtmMpeCapabilitiesCA02_ObjectIdentity = ObjectIdentity
atmMpeCapabilitiesCA02 = _AtmMpeCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 3, 1, 3)
)
_AtmMpeCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
atmMpeCapabilitiesCA02A = _AtmMpeCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AtmMpeMIB",
    **{"mscAtmMpe": mscAtmMpe,
       "mscAtmMpeRowStatusTable": mscAtmMpeRowStatusTable,
       "mscAtmMpeRowStatusEntry": mscAtmMpeRowStatusEntry,
       "mscAtmMpeRowStatus": mscAtmMpeRowStatus,
       "mscAtmMpeComponentName": mscAtmMpeComponentName,
       "mscAtmMpeStorageType": mscAtmMpeStorageType,
       "mscAtmMpeIndex": mscAtmMpeIndex,
       "mscAtmMpeAc": mscAtmMpeAc,
       "mscAtmMpeAcRowStatusTable": mscAtmMpeAcRowStatusTable,
       "mscAtmMpeAcRowStatusEntry": mscAtmMpeAcRowStatusEntry,
       "mscAtmMpeAcRowStatus": mscAtmMpeAcRowStatus,
       "mscAtmMpeAcComponentName": mscAtmMpeAcComponentName,
       "mscAtmMpeAcStorageType": mscAtmMpeAcStorageType,
       "mscAtmMpeAcIndex": mscAtmMpeAcIndex,
       "mscAtmMpeAcProvTable": mscAtmMpeAcProvTable,
       "mscAtmMpeAcProvEntry": mscAtmMpeAcProvEntry,
       "mscAtmMpeAcAtmConnection": mscAtmMpeAcAtmConnection,
       "mscAtmMpeAcIpCoS": mscAtmMpeAcIpCoS,
       "mscAtmMpeAcStateTable": mscAtmMpeAcStateTable,
       "mscAtmMpeAcStateEntry": mscAtmMpeAcStateEntry,
       "mscAtmMpeAcAdminState": mscAtmMpeAcAdminState,
       "mscAtmMpeAcOperationalState": mscAtmMpeAcOperationalState,
       "mscAtmMpeAcUsageState": mscAtmMpeAcUsageState,
       "mscAtmMpeAcOperTable": mscAtmMpeAcOperTable,
       "mscAtmMpeAcOperEntry": mscAtmMpeAcOperEntry,
       "mscAtmMpeAcSpeed": mscAtmMpeAcSpeed,
       "mscAtmMpeAcStatsTable": mscAtmMpeAcStatsTable,
       "mscAtmMpeAcStatsEntry": mscAtmMpeAcStatsEntry,
       "mscAtmMpeAcOutPackets": mscAtmMpeAcOutPackets,
       "mscAtmMpeAcOutOctets": mscAtmMpeAcOutOctets,
       "mscAtmMpeAcOutDiscards": mscAtmMpeAcOutDiscards,
       "mscAtmMpeAcInPackets": mscAtmMpeAcInPackets,
       "mscAtmMpeAcInOctets": mscAtmMpeAcInOctets,
       "mscAtmMpeAcInUnknownProtos": mscAtmMpeAcInUnknownProtos,
       "mscAtmMpeAcInErrors": mscAtmMpeAcInErrors,
       "mscAtmMpeCidDataTable": mscAtmMpeCidDataTable,
       "mscAtmMpeCidDataEntry": mscAtmMpeCidDataEntry,
       "mscAtmMpeCustomerIdentifier": mscAtmMpeCustomerIdentifier,
       "mscAtmMpeIfEntryTable": mscAtmMpeIfEntryTable,
       "mscAtmMpeIfEntryEntry": mscAtmMpeIfEntryEntry,
       "mscAtmMpeIfAdminStatus": mscAtmMpeIfAdminStatus,
       "mscAtmMpeIfIndex": mscAtmMpeIfIndex,
       "mscAtmMpeProvTable": mscAtmMpeProvTable,
       "mscAtmMpeProvEntry": mscAtmMpeProvEntry,
       "mscAtmMpeMaxTransmissionUnit": mscAtmMpeMaxTransmissionUnit,
       "mscAtmMpeEncapType": mscAtmMpeEncapType,
       "mscAtmMpeIlsForwarder": mscAtmMpeIlsForwarder,
       "mscAtmMpeMediaProvTable": mscAtmMpeMediaProvTable,
       "mscAtmMpeMediaProvEntry": mscAtmMpeMediaProvEntry,
       "mscAtmMpeLinkToProtocolPort": mscAtmMpeLinkToProtocolPort,
       "mscAtmMpeStateTable": mscAtmMpeStateTable,
       "mscAtmMpeStateEntry": mscAtmMpeStateEntry,
       "mscAtmMpeAdminState": mscAtmMpeAdminState,
       "mscAtmMpeOperationalState": mscAtmMpeOperationalState,
       "mscAtmMpeUsageState": mscAtmMpeUsageState,
       "mscAtmMpeOperStatusTable": mscAtmMpeOperStatusTable,
       "mscAtmMpeOperStatusEntry": mscAtmMpeOperStatusEntry,
       "mscAtmMpeSnmpOperStatus": mscAtmMpeSnmpOperStatus,
       "atmMpeMIB": atmMpeMIB,
       "atmMpeGroup": atmMpeGroup,
       "atmMpeGroupCA": atmMpeGroupCA,
       "atmMpeGroupCA02": atmMpeGroupCA02,
       "atmMpeGroupCA02A": atmMpeGroupCA02A,
       "atmMpeCapabilities": atmMpeCapabilities,
       "atmMpeCapabilitiesCA": atmMpeCapabilitiesCA,
       "atmMpeCapabilitiesCA02": atmMpeCapabilitiesCA02,
       "atmMpeCapabilitiesCA02A": atmMpeCapabilitiesCA02A}
)
