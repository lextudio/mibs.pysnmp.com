# SNMP MIB module (Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:23 2024
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

(mscDpnGate,
 mscDpnGateIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-DpnTrunksMIB",
    "mscDpnGate",
    "mscDpnGateIndex")

(Counter32,
 DisplayString,
 Gauge32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "Link",
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

_MscDpnGateFrAccess_ObjectIdentity = ObjectIdentity
mscDpnGateFrAccess = _MscDpnGateFrAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4)
)
_MscDpnGateFrAccessRowStatusTable_Object = MibTable
mscDpnGateFrAccessRowStatusTable = _MscDpnGateFrAccessRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 1)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessRowStatusTable.setStatus("mandatory")
_MscDpnGateFrAccessRowStatusEntry_Object = MibTableRow
mscDpnGateFrAccessRowStatusEntry = _MscDpnGateFrAccessRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 1, 1)
)
mscDpnGateFrAccessRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessRowStatusEntry.setStatus("mandatory")
_MscDpnGateFrAccessRowStatus_Type = RowStatus
_MscDpnGateFrAccessRowStatus_Object = MibTableColumn
mscDpnGateFrAccessRowStatus = _MscDpnGateFrAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 1, 1, 1),
    _MscDpnGateFrAccessRowStatus_Type()
)
mscDpnGateFrAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessRowStatus.setStatus("mandatory")
_MscDpnGateFrAccessComponentName_Type = DisplayString
_MscDpnGateFrAccessComponentName_Object = MibTableColumn
mscDpnGateFrAccessComponentName = _MscDpnGateFrAccessComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 1, 1, 2),
    _MscDpnGateFrAccessComponentName_Type()
)
mscDpnGateFrAccessComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessComponentName.setStatus("mandatory")
_MscDpnGateFrAccessStorageType_Type = StorageType
_MscDpnGateFrAccessStorageType_Object = MibTableColumn
mscDpnGateFrAccessStorageType = _MscDpnGateFrAccessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 1, 1, 4),
    _MscDpnGateFrAccessStorageType_Type()
)
mscDpnGateFrAccessStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessStorageType.setStatus("mandatory")
_MscDpnGateFrAccessIndex_Type = NonReplicated
_MscDpnGateFrAccessIndex_Object = MibTableColumn
mscDpnGateFrAccessIndex = _MscDpnGateFrAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 1, 1, 10),
    _MscDpnGateFrAccessIndex_Type()
)
mscDpnGateFrAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessIndex.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetup_ObjectIdentity = ObjectIdentity
mscDpnGateFrAccessFrMuxSetup = _MscDpnGateFrAccessFrMuxSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2)
)
_MscDpnGateFrAccessFrMuxSetupRowStatusTable_Object = MibTable
mscDpnGateFrAccessFrMuxSetupRowStatusTable = _MscDpnGateFrAccessFrMuxSetupRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupRowStatusTable.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupRowStatusEntry_Object = MibTableRow
mscDpnGateFrAccessFrMuxSetupRowStatusEntry = _MscDpnGateFrAccessFrMuxSetupRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 1, 1)
)
mscDpnGateFrAccessFrMuxSetupRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupRowStatusEntry.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupRowStatus_Type = RowStatus
_MscDpnGateFrAccessFrMuxSetupRowStatus_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupRowStatus = _MscDpnGateFrAccessFrMuxSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 1, 1, 1),
    _MscDpnGateFrAccessFrMuxSetupRowStatus_Type()
)
mscDpnGateFrAccessFrMuxSetupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupRowStatus.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupComponentName_Type = DisplayString
_MscDpnGateFrAccessFrMuxSetupComponentName_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupComponentName = _MscDpnGateFrAccessFrMuxSetupComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 1, 1, 2),
    _MscDpnGateFrAccessFrMuxSetupComponentName_Type()
)
mscDpnGateFrAccessFrMuxSetupComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupComponentName.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupStorageType_Type = StorageType
_MscDpnGateFrAccessFrMuxSetupStorageType_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupStorageType = _MscDpnGateFrAccessFrMuxSetupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 1, 1, 4),
    _MscDpnGateFrAccessFrMuxSetupStorageType_Type()
)
mscDpnGateFrAccessFrMuxSetupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupStorageType.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupIndex_Type = NonReplicated
_MscDpnGateFrAccessFrMuxSetupIndex_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupIndex = _MscDpnGateFrAccessFrMuxSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 1, 1, 10),
    _MscDpnGateFrAccessFrMuxSetupIndex_Type()
)
mscDpnGateFrAccessFrMuxSetupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupIndex.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupPvcSetup_ObjectIdentity = ObjectIdentity
mscDpnGateFrAccessFrMuxSetupPvcSetup = _MscDpnGateFrAccessFrMuxSetupPvcSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2)
)
_MscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable_Object = MibTable
mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable = _MscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry_Object = MibTableRow
mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry = _MscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2, 1, 1)
)
mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessFrMuxSetupIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessFrMuxSetupPvcSetupIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupPvcSetupRowStatus_Type = RowStatus
_MscDpnGateFrAccessFrMuxSetupPvcSetupRowStatus_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatus = _MscDpnGateFrAccessFrMuxSetupPvcSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2, 1, 1, 1),
    _MscDpnGateFrAccessFrMuxSetupPvcSetupRowStatus_Type()
)
mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatus.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupPvcSetupComponentName_Type = DisplayString
_MscDpnGateFrAccessFrMuxSetupPvcSetupComponentName_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupPvcSetupComponentName = _MscDpnGateFrAccessFrMuxSetupPvcSetupComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2, 1, 1, 2),
    _MscDpnGateFrAccessFrMuxSetupPvcSetupComponentName_Type()
)
mscDpnGateFrAccessFrMuxSetupPvcSetupComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupPvcSetupComponentName.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupPvcSetupStorageType_Type = StorageType
_MscDpnGateFrAccessFrMuxSetupPvcSetupStorageType_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupPvcSetupStorageType = _MscDpnGateFrAccessFrMuxSetupPvcSetupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2, 1, 1, 4),
    _MscDpnGateFrAccessFrMuxSetupPvcSetupStorageType_Type()
)
mscDpnGateFrAccessFrMuxSetupPvcSetupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupPvcSetupStorageType.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupPvcSetupIndex_Type = NonReplicated
_MscDpnGateFrAccessFrMuxSetupPvcSetupIndex_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupPvcSetupIndex = _MscDpnGateFrAccessFrMuxSetupPvcSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2, 1, 1, 10),
    _MscDpnGateFrAccessFrMuxSetupPvcSetupIndex_Type()
)
mscDpnGateFrAccessFrMuxSetupPvcSetupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupPvcSetupIndex.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupPvcSetupProvTable_Object = MibTable
mscDpnGateFrAccessFrMuxSetupPvcSetupProvTable = _MscDpnGateFrAccessFrMuxSetupPvcSetupProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupPvcSetupProvTable.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupPvcSetupProvEntry_Object = MibTableRow
mscDpnGateFrAccessFrMuxSetupPvcSetupProvEntry = _MscDpnGateFrAccessFrMuxSetupPvcSetupProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2, 10, 1)
)
mscDpnGateFrAccessFrMuxSetupPvcSetupProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessFrMuxSetupIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessFrMuxSetupPvcSetupIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupPvcSetupProvEntry.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupPvcSetupDlciName_Type = Link
_MscDpnGateFrAccessFrMuxSetupPvcSetupDlciName_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupPvcSetupDlciName = _MscDpnGateFrAccessFrMuxSetupPvcSetupDlciName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 2, 10, 1, 1),
    _MscDpnGateFrAccessFrMuxSetupPvcSetupDlciName_Type()
)
mscDpnGateFrAccessFrMuxSetupPvcSetupDlciName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupPvcSetupDlciName.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupTrafficDescrTable_Object = MibTable
mscDpnGateFrAccessFrMuxSetupTrafficDescrTable = _MscDpnGateFrAccessFrMuxSetupTrafficDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupTrafficDescrTable.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupTrafficDescrEntry_Object = MibTableRow
mscDpnGateFrAccessFrMuxSetupTrafficDescrEntry = _MscDpnGateFrAccessFrMuxSetupTrafficDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 10, 1)
)
mscDpnGateFrAccessFrMuxSetupTrafficDescrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupTrafficDescrEntry.setStatus("mandatory")


class _MscDpnGateFrAccessFrMuxSetupCommittedInformationRate_Type(Unsigned32):
    """Custom type mscDpnGateFrAccessFrMuxSetupCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4800, 2048000),
    )


_MscDpnGateFrAccessFrMuxSetupCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscDpnGateFrAccessFrMuxSetupCommittedInformationRate_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupCommittedInformationRate = _MscDpnGateFrAccessFrMuxSetupCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 10, 1, 1),
    _MscDpnGateFrAccessFrMuxSetupCommittedInformationRate_Type()
)
mscDpnGateFrAccessFrMuxSetupCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupCommittedInformationRate.setStatus("mandatory")


class _MscDpnGateFrAccessFrMuxSetupCommittedBurstSize_Type(Unsigned32):
    """Custom type mscDpnGateFrAccessFrMuxSetupCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscDpnGateFrAccessFrMuxSetupCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscDpnGateFrAccessFrMuxSetupCommittedBurstSize_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupCommittedBurstSize = _MscDpnGateFrAccessFrMuxSetupCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 10, 1, 2),
    _MscDpnGateFrAccessFrMuxSetupCommittedBurstSize_Type()
)
mscDpnGateFrAccessFrMuxSetupCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupCommittedBurstSize.setStatus("obsolete")


class _MscDpnGateFrAccessFrMuxSetupMaximumFrameSize_Type(Unsigned32):
    """Custom type mscDpnGateFrAccessFrMuxSetupMaximumFrameSize based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MscDpnGateFrAccessFrMuxSetupMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscDpnGateFrAccessFrMuxSetupMaximumFrameSize_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupMaximumFrameSize = _MscDpnGateFrAccessFrMuxSetupMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 10, 1, 3),
    _MscDpnGateFrAccessFrMuxSetupMaximumFrameSize_Type()
)
mscDpnGateFrAccessFrMuxSetupMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupMaximumFrameSize.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupDlciCompNameOpTable_Object = MibTable
mscDpnGateFrAccessFrMuxSetupDlciCompNameOpTable = _MscDpnGateFrAccessFrMuxSetupDlciCompNameOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 11)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupDlciCompNameOpTable.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupDlciCompNameOpEntry_Object = MibTableRow
mscDpnGateFrAccessFrMuxSetupDlciCompNameOpEntry = _MscDpnGateFrAccessFrMuxSetupDlciCompNameOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 11, 1)
)
mscDpnGateFrAccessFrMuxSetupDlciCompNameOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupDlciCompNameOpEntry.setStatus("mandatory")
_MscDpnGateFrAccessFrMuxSetupDlciCompName_Type = RowPointer
_MscDpnGateFrAccessFrMuxSetupDlciCompName_Object = MibTableColumn
mscDpnGateFrAccessFrMuxSetupDlciCompName = _MscDpnGateFrAccessFrMuxSetupDlciCompName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 2, 11, 1, 1),
    _MscDpnGateFrAccessFrMuxSetupDlciCompName_Type()
)
mscDpnGateFrAccessFrMuxSetupDlciCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessFrMuxSetupDlciCompName.setStatus("mandatory")
_MscDpnGateFrAccessProvTable_Object = MibTable
mscDpnGateFrAccessProvTable = _MscDpnGateFrAccessProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 10)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessProvTable.setStatus("mandatory")
_MscDpnGateFrAccessProvEntry_Object = MibTableRow
mscDpnGateFrAccessProvEntry = _MscDpnGateFrAccessProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 10, 1)
)
mscDpnGateFrAccessProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessProvEntry.setStatus("mandatory")


class _MscDpnGateFrAccessMaximumErroredInterval_Type(Unsigned32):
    """Custom type mscDpnGateFrAccessMaximumErroredInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_MscDpnGateFrAccessMaximumErroredInterval_Type.__name__ = "Unsigned32"
_MscDpnGateFrAccessMaximumErroredInterval_Object = MibTableColumn
mscDpnGateFrAccessMaximumErroredInterval = _MscDpnGateFrAccessMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 10, 1, 1),
    _MscDpnGateFrAccessMaximumErroredInterval_Type()
)
mscDpnGateFrAccessMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessMaximumErroredInterval.setStatus("mandatory")


class _MscDpnGateFrAccessReceiveErrorSensitivity_Type(Unsigned32):
    """Custom type mscDpnGateFrAccessReceiveErrorSensitivity based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_MscDpnGateFrAccessReceiveErrorSensitivity_Type.__name__ = "Unsigned32"
_MscDpnGateFrAccessReceiveErrorSensitivity_Object = MibTableColumn
mscDpnGateFrAccessReceiveErrorSensitivity = _MscDpnGateFrAccessReceiveErrorSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 10, 1, 2),
    _MscDpnGateFrAccessReceiveErrorSensitivity_Type()
)
mscDpnGateFrAccessReceiveErrorSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessReceiveErrorSensitivity.setStatus("mandatory")
_MscDpnGateFrAccessStateTable_Object = MibTable
mscDpnGateFrAccessStateTable = _MscDpnGateFrAccessStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessStateTable.setStatus("mandatory")
_MscDpnGateFrAccessStateEntry_Object = MibTableRow
mscDpnGateFrAccessStateEntry = _MscDpnGateFrAccessStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1)
)
mscDpnGateFrAccessStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessStateEntry.setStatus("mandatory")


class _MscDpnGateFrAccessAdminState_Type(Integer32):
    """Custom type mscDpnGateFrAccessAdminState based on Integer32"""
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


_MscDpnGateFrAccessAdminState_Type.__name__ = "Integer32"
_MscDpnGateFrAccessAdminState_Object = MibTableColumn
mscDpnGateFrAccessAdminState = _MscDpnGateFrAccessAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1, 1),
    _MscDpnGateFrAccessAdminState_Type()
)
mscDpnGateFrAccessAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessAdminState.setStatus("mandatory")


class _MscDpnGateFrAccessOperationalState_Type(Integer32):
    """Custom type mscDpnGateFrAccessOperationalState based on Integer32"""
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


_MscDpnGateFrAccessOperationalState_Type.__name__ = "Integer32"
_MscDpnGateFrAccessOperationalState_Object = MibTableColumn
mscDpnGateFrAccessOperationalState = _MscDpnGateFrAccessOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1, 2),
    _MscDpnGateFrAccessOperationalState_Type()
)
mscDpnGateFrAccessOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessOperationalState.setStatus("mandatory")


class _MscDpnGateFrAccessUsageState_Type(Integer32):
    """Custom type mscDpnGateFrAccessUsageState based on Integer32"""
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


_MscDpnGateFrAccessUsageState_Type.__name__ = "Integer32"
_MscDpnGateFrAccessUsageState_Object = MibTableColumn
mscDpnGateFrAccessUsageState = _MscDpnGateFrAccessUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1, 3),
    _MscDpnGateFrAccessUsageState_Type()
)
mscDpnGateFrAccessUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessUsageState.setStatus("mandatory")


class _MscDpnGateFrAccessAvailabilityStatus_Type(OctetString):
    """Custom type mscDpnGateFrAccessAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscDpnGateFrAccessAvailabilityStatus_Type.__name__ = "OctetString"
_MscDpnGateFrAccessAvailabilityStatus_Object = MibTableColumn
mscDpnGateFrAccessAvailabilityStatus = _MscDpnGateFrAccessAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1, 4),
    _MscDpnGateFrAccessAvailabilityStatus_Type()
)
mscDpnGateFrAccessAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessAvailabilityStatus.setStatus("mandatory")


class _MscDpnGateFrAccessProceduralStatus_Type(OctetString):
    """Custom type mscDpnGateFrAccessProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDpnGateFrAccessProceduralStatus_Type.__name__ = "OctetString"
_MscDpnGateFrAccessProceduralStatus_Object = MibTableColumn
mscDpnGateFrAccessProceduralStatus = _MscDpnGateFrAccessProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1, 5),
    _MscDpnGateFrAccessProceduralStatus_Type()
)
mscDpnGateFrAccessProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessProceduralStatus.setStatus("mandatory")


class _MscDpnGateFrAccessControlStatus_Type(OctetString):
    """Custom type mscDpnGateFrAccessControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDpnGateFrAccessControlStatus_Type.__name__ = "OctetString"
_MscDpnGateFrAccessControlStatus_Object = MibTableColumn
mscDpnGateFrAccessControlStatus = _MscDpnGateFrAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1, 6),
    _MscDpnGateFrAccessControlStatus_Type()
)
mscDpnGateFrAccessControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessControlStatus.setStatus("mandatory")


class _MscDpnGateFrAccessAlarmStatus_Type(OctetString):
    """Custom type mscDpnGateFrAccessAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDpnGateFrAccessAlarmStatus_Type.__name__ = "OctetString"
_MscDpnGateFrAccessAlarmStatus_Object = MibTableColumn
mscDpnGateFrAccessAlarmStatus = _MscDpnGateFrAccessAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1, 7),
    _MscDpnGateFrAccessAlarmStatus_Type()
)
mscDpnGateFrAccessAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessAlarmStatus.setStatus("mandatory")


class _MscDpnGateFrAccessStandbyStatus_Type(Integer32):
    """Custom type mscDpnGateFrAccessStandbyStatus based on Integer32"""
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


_MscDpnGateFrAccessStandbyStatus_Type.__name__ = "Integer32"
_MscDpnGateFrAccessStandbyStatus_Object = MibTableColumn
mscDpnGateFrAccessStandbyStatus = _MscDpnGateFrAccessStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1, 8),
    _MscDpnGateFrAccessStandbyStatus_Type()
)
mscDpnGateFrAccessStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessStandbyStatus.setStatus("mandatory")


class _MscDpnGateFrAccessUnknownStatus_Type(Integer32):
    """Custom type mscDpnGateFrAccessUnknownStatus based on Integer32"""
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


_MscDpnGateFrAccessUnknownStatus_Type.__name__ = "Integer32"
_MscDpnGateFrAccessUnknownStatus_Object = MibTableColumn
mscDpnGateFrAccessUnknownStatus = _MscDpnGateFrAccessUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 11, 1, 9),
    _MscDpnGateFrAccessUnknownStatus_Type()
)
mscDpnGateFrAccessUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessUnknownStatus.setStatus("mandatory")
_MscDpnGateFrAccessOpTable_Object = MibTable
mscDpnGateFrAccessOpTable = _MscDpnGateFrAccessOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 12)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessOpTable.setStatus("mandatory")
_MscDpnGateFrAccessOpEntry_Object = MibTableRow
mscDpnGateFrAccessOpEntry = _MscDpnGateFrAccessOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 12, 1)
)
mscDpnGateFrAccessOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessOpEntry.setStatus("mandatory")


class _MscDpnGateFrAccessRoundTripDelay_Type(Gauge32):
    """Custom type mscDpnGateFrAccessRoundTripDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_MscDpnGateFrAccessRoundTripDelay_Type.__name__ = "Gauge32"
_MscDpnGateFrAccessRoundTripDelay_Object = MibTableColumn
mscDpnGateFrAccessRoundTripDelay = _MscDpnGateFrAccessRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 12, 1, 1),
    _MscDpnGateFrAccessRoundTripDelay_Type()
)
mscDpnGateFrAccessRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessRoundTripDelay.setStatus("mandatory")
_MscDpnGateFrAccessStatsTable_Object = MibTable
mscDpnGateFrAccessStatsTable = _MscDpnGateFrAccessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 13)
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessStatsTable.setStatus("mandatory")
_MscDpnGateFrAccessStatsEntry_Object = MibTableRow
mscDpnGateFrAccessStatsEntry = _MscDpnGateFrAccessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 13, 1)
)
mscDpnGateFrAccessStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DpnTrunksMIB", "mscDpnGateIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB", "mscDpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    mscDpnGateFrAccessStatsEntry.setStatus("mandatory")
_MscDpnGateFrAccessReceivedBytesFromIf_Type = Counter32
_MscDpnGateFrAccessReceivedBytesFromIf_Object = MibTableColumn
mscDpnGateFrAccessReceivedBytesFromIf = _MscDpnGateFrAccessReceivedBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 13, 1, 1),
    _MscDpnGateFrAccessReceivedBytesFromIf_Type()
)
mscDpnGateFrAccessReceivedBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessReceivedBytesFromIf.setStatus("mandatory")
_MscDpnGateFrAccessLostFramesFromIf_Type = Counter32
_MscDpnGateFrAccessLostFramesFromIf_Object = MibTableColumn
mscDpnGateFrAccessLostFramesFromIf = _MscDpnGateFrAccessLostFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 13, 1, 2),
    _MscDpnGateFrAccessLostFramesFromIf_Type()
)
mscDpnGateFrAccessLostFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessLostFramesFromIf.setStatus("mandatory")
_MscDpnGateFrAccessDiscardBadFromIf_Type = Counter32
_MscDpnGateFrAccessDiscardBadFromIf_Object = MibTableColumn
mscDpnGateFrAccessDiscardBadFromIf = _MscDpnGateFrAccessDiscardBadFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 13, 1, 3),
    _MscDpnGateFrAccessDiscardBadFromIf_Type()
)
mscDpnGateFrAccessDiscardBadFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessDiscardBadFromIf.setStatus("mandatory")
_MscDpnGateFrAccessDiscardExcessToIf_Type = Counter32
_MscDpnGateFrAccessDiscardExcessToIf_Object = MibTableColumn
mscDpnGateFrAccessDiscardExcessToIf = _MscDpnGateFrAccessDiscardExcessToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 61, 4, 13, 1, 4),
    _MscDpnGateFrAccessDiscardExcessToIf_Type()
)
mscDpnGateFrAccessDiscardExcessToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDpnGateFrAccessDiscardExcessToIf.setStatus("mandatory")
_FraDpnTrunksMIB_ObjectIdentity = ObjectIdentity
fraDpnTrunksMIB = _FraDpnTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 68)
)
_FraDpnTrunksGroup_ObjectIdentity = ObjectIdentity
fraDpnTrunksGroup = _FraDpnTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 68, 1)
)
_FraDpnTrunksGroupCA_ObjectIdentity = ObjectIdentity
fraDpnTrunksGroupCA = _FraDpnTrunksGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 68, 1, 1)
)
_FraDpnTrunksGroupCA02_ObjectIdentity = ObjectIdentity
fraDpnTrunksGroupCA02 = _FraDpnTrunksGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 68, 1, 1, 3)
)
_FraDpnTrunksGroupCA02A_ObjectIdentity = ObjectIdentity
fraDpnTrunksGroupCA02A = _FraDpnTrunksGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 68, 1, 1, 3, 2)
)
_FraDpnTrunksCapabilities_ObjectIdentity = ObjectIdentity
fraDpnTrunksCapabilities = _FraDpnTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 68, 3)
)
_FraDpnTrunksCapabilitiesCA_ObjectIdentity = ObjectIdentity
fraDpnTrunksCapabilitiesCA = _FraDpnTrunksCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 68, 3, 1)
)
_FraDpnTrunksCapabilitiesCA02_ObjectIdentity = ObjectIdentity
fraDpnTrunksCapabilitiesCA02 = _FraDpnTrunksCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 68, 3, 1, 3)
)
_FraDpnTrunksCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
fraDpnTrunksCapabilitiesCA02A = _FraDpnTrunksCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 68, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FraDpnTrunksMIB",
    **{"mscDpnGateFrAccess": mscDpnGateFrAccess,
       "mscDpnGateFrAccessRowStatusTable": mscDpnGateFrAccessRowStatusTable,
       "mscDpnGateFrAccessRowStatusEntry": mscDpnGateFrAccessRowStatusEntry,
       "mscDpnGateFrAccessRowStatus": mscDpnGateFrAccessRowStatus,
       "mscDpnGateFrAccessComponentName": mscDpnGateFrAccessComponentName,
       "mscDpnGateFrAccessStorageType": mscDpnGateFrAccessStorageType,
       "mscDpnGateFrAccessIndex": mscDpnGateFrAccessIndex,
       "mscDpnGateFrAccessFrMuxSetup": mscDpnGateFrAccessFrMuxSetup,
       "mscDpnGateFrAccessFrMuxSetupRowStatusTable": mscDpnGateFrAccessFrMuxSetupRowStatusTable,
       "mscDpnGateFrAccessFrMuxSetupRowStatusEntry": mscDpnGateFrAccessFrMuxSetupRowStatusEntry,
       "mscDpnGateFrAccessFrMuxSetupRowStatus": mscDpnGateFrAccessFrMuxSetupRowStatus,
       "mscDpnGateFrAccessFrMuxSetupComponentName": mscDpnGateFrAccessFrMuxSetupComponentName,
       "mscDpnGateFrAccessFrMuxSetupStorageType": mscDpnGateFrAccessFrMuxSetupStorageType,
       "mscDpnGateFrAccessFrMuxSetupIndex": mscDpnGateFrAccessFrMuxSetupIndex,
       "mscDpnGateFrAccessFrMuxSetupPvcSetup": mscDpnGateFrAccessFrMuxSetupPvcSetup,
       "mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable": mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable,
       "mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry": mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry,
       "mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatus": mscDpnGateFrAccessFrMuxSetupPvcSetupRowStatus,
       "mscDpnGateFrAccessFrMuxSetupPvcSetupComponentName": mscDpnGateFrAccessFrMuxSetupPvcSetupComponentName,
       "mscDpnGateFrAccessFrMuxSetupPvcSetupStorageType": mscDpnGateFrAccessFrMuxSetupPvcSetupStorageType,
       "mscDpnGateFrAccessFrMuxSetupPvcSetupIndex": mscDpnGateFrAccessFrMuxSetupPvcSetupIndex,
       "mscDpnGateFrAccessFrMuxSetupPvcSetupProvTable": mscDpnGateFrAccessFrMuxSetupPvcSetupProvTable,
       "mscDpnGateFrAccessFrMuxSetupPvcSetupProvEntry": mscDpnGateFrAccessFrMuxSetupPvcSetupProvEntry,
       "mscDpnGateFrAccessFrMuxSetupPvcSetupDlciName": mscDpnGateFrAccessFrMuxSetupPvcSetupDlciName,
       "mscDpnGateFrAccessFrMuxSetupTrafficDescrTable": mscDpnGateFrAccessFrMuxSetupTrafficDescrTable,
       "mscDpnGateFrAccessFrMuxSetupTrafficDescrEntry": mscDpnGateFrAccessFrMuxSetupTrafficDescrEntry,
       "mscDpnGateFrAccessFrMuxSetupCommittedInformationRate": mscDpnGateFrAccessFrMuxSetupCommittedInformationRate,
       "mscDpnGateFrAccessFrMuxSetupCommittedBurstSize": mscDpnGateFrAccessFrMuxSetupCommittedBurstSize,
       "mscDpnGateFrAccessFrMuxSetupMaximumFrameSize": mscDpnGateFrAccessFrMuxSetupMaximumFrameSize,
       "mscDpnGateFrAccessFrMuxSetupDlciCompNameOpTable": mscDpnGateFrAccessFrMuxSetupDlciCompNameOpTable,
       "mscDpnGateFrAccessFrMuxSetupDlciCompNameOpEntry": mscDpnGateFrAccessFrMuxSetupDlciCompNameOpEntry,
       "mscDpnGateFrAccessFrMuxSetupDlciCompName": mscDpnGateFrAccessFrMuxSetupDlciCompName,
       "mscDpnGateFrAccessProvTable": mscDpnGateFrAccessProvTable,
       "mscDpnGateFrAccessProvEntry": mscDpnGateFrAccessProvEntry,
       "mscDpnGateFrAccessMaximumErroredInterval": mscDpnGateFrAccessMaximumErroredInterval,
       "mscDpnGateFrAccessReceiveErrorSensitivity": mscDpnGateFrAccessReceiveErrorSensitivity,
       "mscDpnGateFrAccessStateTable": mscDpnGateFrAccessStateTable,
       "mscDpnGateFrAccessStateEntry": mscDpnGateFrAccessStateEntry,
       "mscDpnGateFrAccessAdminState": mscDpnGateFrAccessAdminState,
       "mscDpnGateFrAccessOperationalState": mscDpnGateFrAccessOperationalState,
       "mscDpnGateFrAccessUsageState": mscDpnGateFrAccessUsageState,
       "mscDpnGateFrAccessAvailabilityStatus": mscDpnGateFrAccessAvailabilityStatus,
       "mscDpnGateFrAccessProceduralStatus": mscDpnGateFrAccessProceduralStatus,
       "mscDpnGateFrAccessControlStatus": mscDpnGateFrAccessControlStatus,
       "mscDpnGateFrAccessAlarmStatus": mscDpnGateFrAccessAlarmStatus,
       "mscDpnGateFrAccessStandbyStatus": mscDpnGateFrAccessStandbyStatus,
       "mscDpnGateFrAccessUnknownStatus": mscDpnGateFrAccessUnknownStatus,
       "mscDpnGateFrAccessOpTable": mscDpnGateFrAccessOpTable,
       "mscDpnGateFrAccessOpEntry": mscDpnGateFrAccessOpEntry,
       "mscDpnGateFrAccessRoundTripDelay": mscDpnGateFrAccessRoundTripDelay,
       "mscDpnGateFrAccessStatsTable": mscDpnGateFrAccessStatsTable,
       "mscDpnGateFrAccessStatsEntry": mscDpnGateFrAccessStatsEntry,
       "mscDpnGateFrAccessReceivedBytesFromIf": mscDpnGateFrAccessReceivedBytesFromIf,
       "mscDpnGateFrAccessLostFramesFromIf": mscDpnGateFrAccessLostFramesFromIf,
       "mscDpnGateFrAccessDiscardBadFromIf": mscDpnGateFrAccessDiscardBadFromIf,
       "mscDpnGateFrAccessDiscardExcessToIf": mscDpnGateFrAccessDiscardExcessToIf,
       "fraDpnTrunksMIB": fraDpnTrunksMIB,
       "fraDpnTrunksGroup": fraDpnTrunksGroup,
       "fraDpnTrunksGroupCA": fraDpnTrunksGroupCA,
       "fraDpnTrunksGroupCA02": fraDpnTrunksGroupCA02,
       "fraDpnTrunksGroupCA02A": fraDpnTrunksGroupCA02A,
       "fraDpnTrunksCapabilities": fraDpnTrunksCapabilities,
       "fraDpnTrunksCapabilitiesCA": fraDpnTrunksCapabilitiesCA,
       "fraDpnTrunksCapabilitiesCA02": fraDpnTrunksCapabilitiesCA02,
       "fraDpnTrunksCapabilitiesCA02A": fraDpnTrunksCapabilitiesCA02A}
)
