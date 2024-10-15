# SNMP MIB module (Nortel-Magellan-Passport-FraDpnTrunksMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FraDpnTrunksMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:43 2024
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

(dpnGate,
 dpnGateIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-DpnTrunksMIB",
    "dpnGate",
    "dpnGateIndex")

(Counter32,
 DisplayString,
 Gauge32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "Link",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
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

_DpnGateFrAccess_ObjectIdentity = ObjectIdentity
dpnGateFrAccess = _DpnGateFrAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4)
)
_DpnGateFrAccessRowStatusTable_Object = MibTable
dpnGateFrAccessRowStatusTable = _DpnGateFrAccessRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessRowStatusTable.setStatus("mandatory")
_DpnGateFrAccessRowStatusEntry_Object = MibTableRow
dpnGateFrAccessRowStatusEntry = _DpnGateFrAccessRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1)
)
dpnGateFrAccessRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessRowStatusEntry.setStatus("mandatory")
_DpnGateFrAccessRowStatus_Type = RowStatus
_DpnGateFrAccessRowStatus_Object = MibTableColumn
dpnGateFrAccessRowStatus = _DpnGateFrAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1, 1),
    _DpnGateFrAccessRowStatus_Type()
)
dpnGateFrAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateFrAccessRowStatus.setStatus("mandatory")
_DpnGateFrAccessComponentName_Type = DisplayString
_DpnGateFrAccessComponentName_Object = MibTableColumn
dpnGateFrAccessComponentName = _DpnGateFrAccessComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1, 2),
    _DpnGateFrAccessComponentName_Type()
)
dpnGateFrAccessComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessComponentName.setStatus("mandatory")
_DpnGateFrAccessStorageType_Type = StorageType
_DpnGateFrAccessStorageType_Object = MibTableColumn
dpnGateFrAccessStorageType = _DpnGateFrAccessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1, 4),
    _DpnGateFrAccessStorageType_Type()
)
dpnGateFrAccessStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessStorageType.setStatus("mandatory")
_DpnGateFrAccessIndex_Type = NonReplicated
_DpnGateFrAccessIndex_Object = MibTableColumn
dpnGateFrAccessIndex = _DpnGateFrAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 1, 1, 10),
    _DpnGateFrAccessIndex_Type()
)
dpnGateFrAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpnGateFrAccessIndex.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetup_ObjectIdentity = ObjectIdentity
dpnGateFrAccessFrMuxSetup = _DpnGateFrAccessFrMuxSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2)
)
_DpnGateFrAccessFrMuxSetupRowStatusTable_Object = MibTable
dpnGateFrAccessFrMuxSetupRowStatusTable = _DpnGateFrAccessFrMuxSetupRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupRowStatusTable.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupRowStatusEntry_Object = MibTableRow
dpnGateFrAccessFrMuxSetupRowStatusEntry = _DpnGateFrAccessFrMuxSetupRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1)
)
dpnGateFrAccessFrMuxSetupRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupRowStatusEntry.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupRowStatus_Type = RowStatus
_DpnGateFrAccessFrMuxSetupRowStatus_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupRowStatus = _DpnGateFrAccessFrMuxSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1, 1),
    _DpnGateFrAccessFrMuxSetupRowStatus_Type()
)
dpnGateFrAccessFrMuxSetupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupRowStatus.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupComponentName_Type = DisplayString
_DpnGateFrAccessFrMuxSetupComponentName_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupComponentName = _DpnGateFrAccessFrMuxSetupComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1, 2),
    _DpnGateFrAccessFrMuxSetupComponentName_Type()
)
dpnGateFrAccessFrMuxSetupComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupComponentName.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupStorageType_Type = StorageType
_DpnGateFrAccessFrMuxSetupStorageType_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupStorageType = _DpnGateFrAccessFrMuxSetupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1, 4),
    _DpnGateFrAccessFrMuxSetupStorageType_Type()
)
dpnGateFrAccessFrMuxSetupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupStorageType.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupIndex_Type = NonReplicated
_DpnGateFrAccessFrMuxSetupIndex_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupIndex = _DpnGateFrAccessFrMuxSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 1, 1, 10),
    _DpnGateFrAccessFrMuxSetupIndex_Type()
)
dpnGateFrAccessFrMuxSetupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupIndex.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupPvcSetup_ObjectIdentity = ObjectIdentity
dpnGateFrAccessFrMuxSetupPvcSetup = _DpnGateFrAccessFrMuxSetupPvcSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2)
)
_DpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable_Object = MibTable
dpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable = _DpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry_Object = MibTableRow
dpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry = _DpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1)
)
dpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupPvcSetupIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupPvcSetupRowStatus_Type = RowStatus
_DpnGateFrAccessFrMuxSetupPvcSetupRowStatus_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupPvcSetupRowStatus = _DpnGateFrAccessFrMuxSetupPvcSetupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1, 1),
    _DpnGateFrAccessFrMuxSetupPvcSetupRowStatus_Type()
)
dpnGateFrAccessFrMuxSetupPvcSetupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupPvcSetupRowStatus.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupPvcSetupComponentName_Type = DisplayString
_DpnGateFrAccessFrMuxSetupPvcSetupComponentName_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupPvcSetupComponentName = _DpnGateFrAccessFrMuxSetupPvcSetupComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1, 2),
    _DpnGateFrAccessFrMuxSetupPvcSetupComponentName_Type()
)
dpnGateFrAccessFrMuxSetupPvcSetupComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupPvcSetupComponentName.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupPvcSetupStorageType_Type = StorageType
_DpnGateFrAccessFrMuxSetupPvcSetupStorageType_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupPvcSetupStorageType = _DpnGateFrAccessFrMuxSetupPvcSetupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1, 4),
    _DpnGateFrAccessFrMuxSetupPvcSetupStorageType_Type()
)
dpnGateFrAccessFrMuxSetupPvcSetupStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupPvcSetupStorageType.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupPvcSetupIndex_Type = NonReplicated
_DpnGateFrAccessFrMuxSetupPvcSetupIndex_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupPvcSetupIndex = _DpnGateFrAccessFrMuxSetupPvcSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 1, 1, 10),
    _DpnGateFrAccessFrMuxSetupPvcSetupIndex_Type()
)
dpnGateFrAccessFrMuxSetupPvcSetupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupPvcSetupIndex.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupPvcSetupProvTable_Object = MibTable
dpnGateFrAccessFrMuxSetupPvcSetupProvTable = _DpnGateFrAccessFrMuxSetupPvcSetupProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupPvcSetupProvTable.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupPvcSetupProvEntry_Object = MibTableRow
dpnGateFrAccessFrMuxSetupPvcSetupProvEntry = _DpnGateFrAccessFrMuxSetupPvcSetupProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 10, 1)
)
dpnGateFrAccessFrMuxSetupPvcSetupProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupPvcSetupIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupPvcSetupProvEntry.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupPvcSetupDlciName_Type = Link
_DpnGateFrAccessFrMuxSetupPvcSetupDlciName_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupPvcSetupDlciName = _DpnGateFrAccessFrMuxSetupPvcSetupDlciName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 2, 10, 1, 1),
    _DpnGateFrAccessFrMuxSetupPvcSetupDlciName_Type()
)
dpnGateFrAccessFrMuxSetupPvcSetupDlciName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupPvcSetupDlciName.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupTrafficDescrTable_Object = MibTable
dpnGateFrAccessFrMuxSetupTrafficDescrTable = _DpnGateFrAccessFrMuxSetupTrafficDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupTrafficDescrTable.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupTrafficDescrEntry_Object = MibTableRow
dpnGateFrAccessFrMuxSetupTrafficDescrEntry = _DpnGateFrAccessFrMuxSetupTrafficDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10, 1)
)
dpnGateFrAccessFrMuxSetupTrafficDescrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupTrafficDescrEntry.setStatus("mandatory")


class _DpnGateFrAccessFrMuxSetupCommittedInformationRate_Type(Unsigned32):
    """Custom type dpnGateFrAccessFrMuxSetupCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4800, 2048000),
    )


_DpnGateFrAccessFrMuxSetupCommittedInformationRate_Type.__name__ = "Unsigned32"
_DpnGateFrAccessFrMuxSetupCommittedInformationRate_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupCommittedInformationRate = _DpnGateFrAccessFrMuxSetupCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10, 1, 1),
    _DpnGateFrAccessFrMuxSetupCommittedInformationRate_Type()
)
dpnGateFrAccessFrMuxSetupCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupCommittedInformationRate.setStatus("mandatory")


class _DpnGateFrAccessFrMuxSetupCommittedBurstSize_Type(Unsigned32):
    """Custom type dpnGateFrAccessFrMuxSetupCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_DpnGateFrAccessFrMuxSetupCommittedBurstSize_Type.__name__ = "Unsigned32"
_DpnGateFrAccessFrMuxSetupCommittedBurstSize_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupCommittedBurstSize = _DpnGateFrAccessFrMuxSetupCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10, 1, 2),
    _DpnGateFrAccessFrMuxSetupCommittedBurstSize_Type()
)
dpnGateFrAccessFrMuxSetupCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupCommittedBurstSize.setStatus("obsolete")


class _DpnGateFrAccessFrMuxSetupMaximumFrameSize_Type(Unsigned32):
    """Custom type dpnGateFrAccessFrMuxSetupMaximumFrameSize based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_DpnGateFrAccessFrMuxSetupMaximumFrameSize_Type.__name__ = "Unsigned32"
_DpnGateFrAccessFrMuxSetupMaximumFrameSize_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupMaximumFrameSize = _DpnGateFrAccessFrMuxSetupMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 10, 1, 3),
    _DpnGateFrAccessFrMuxSetupMaximumFrameSize_Type()
)
dpnGateFrAccessFrMuxSetupMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupMaximumFrameSize.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupDlciCompNameOpTable_Object = MibTable
dpnGateFrAccessFrMuxSetupDlciCompNameOpTable = _DpnGateFrAccessFrMuxSetupDlciCompNameOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 11)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupDlciCompNameOpTable.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupDlciCompNameOpEntry_Object = MibTableRow
dpnGateFrAccessFrMuxSetupDlciCompNameOpEntry = _DpnGateFrAccessFrMuxSetupDlciCompNameOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 11, 1)
)
dpnGateFrAccessFrMuxSetupDlciCompNameOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessFrMuxSetupIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupDlciCompNameOpEntry.setStatus("mandatory")
_DpnGateFrAccessFrMuxSetupDlciCompName_Type = RowPointer
_DpnGateFrAccessFrMuxSetupDlciCompName_Object = MibTableColumn
dpnGateFrAccessFrMuxSetupDlciCompName = _DpnGateFrAccessFrMuxSetupDlciCompName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 2, 11, 1, 1),
    _DpnGateFrAccessFrMuxSetupDlciCompName_Type()
)
dpnGateFrAccessFrMuxSetupDlciCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessFrMuxSetupDlciCompName.setStatus("mandatory")
_DpnGateFrAccessProvTable_Object = MibTable
dpnGateFrAccessProvTable = _DpnGateFrAccessProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 10)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessProvTable.setStatus("mandatory")
_DpnGateFrAccessProvEntry_Object = MibTableRow
dpnGateFrAccessProvEntry = _DpnGateFrAccessProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 10, 1)
)
dpnGateFrAccessProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessProvEntry.setStatus("mandatory")


class _DpnGateFrAccessMaximumErroredInterval_Type(Unsigned32):
    """Custom type dpnGateFrAccessMaximumErroredInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_DpnGateFrAccessMaximumErroredInterval_Type.__name__ = "Unsigned32"
_DpnGateFrAccessMaximumErroredInterval_Object = MibTableColumn
dpnGateFrAccessMaximumErroredInterval = _DpnGateFrAccessMaximumErroredInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 10, 1, 1),
    _DpnGateFrAccessMaximumErroredInterval_Type()
)
dpnGateFrAccessMaximumErroredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateFrAccessMaximumErroredInterval.setStatus("mandatory")


class _DpnGateFrAccessReceiveErrorSensitivity_Type(Unsigned32):
    """Custom type dpnGateFrAccessReceiveErrorSensitivity based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_DpnGateFrAccessReceiveErrorSensitivity_Type.__name__ = "Unsigned32"
_DpnGateFrAccessReceiveErrorSensitivity_Object = MibTableColumn
dpnGateFrAccessReceiveErrorSensitivity = _DpnGateFrAccessReceiveErrorSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 10, 1, 2),
    _DpnGateFrAccessReceiveErrorSensitivity_Type()
)
dpnGateFrAccessReceiveErrorSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpnGateFrAccessReceiveErrorSensitivity.setStatus("mandatory")
_DpnGateFrAccessStateTable_Object = MibTable
dpnGateFrAccessStateTable = _DpnGateFrAccessStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessStateTable.setStatus("mandatory")
_DpnGateFrAccessStateEntry_Object = MibTableRow
dpnGateFrAccessStateEntry = _DpnGateFrAccessStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1)
)
dpnGateFrAccessStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessStateEntry.setStatus("mandatory")


class _DpnGateFrAccessAdminState_Type(Integer32):
    """Custom type dpnGateFrAccessAdminState based on Integer32"""
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


_DpnGateFrAccessAdminState_Type.__name__ = "Integer32"
_DpnGateFrAccessAdminState_Object = MibTableColumn
dpnGateFrAccessAdminState = _DpnGateFrAccessAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 1),
    _DpnGateFrAccessAdminState_Type()
)
dpnGateFrAccessAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessAdminState.setStatus("mandatory")


class _DpnGateFrAccessOperationalState_Type(Integer32):
    """Custom type dpnGateFrAccessOperationalState based on Integer32"""
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


_DpnGateFrAccessOperationalState_Type.__name__ = "Integer32"
_DpnGateFrAccessOperationalState_Object = MibTableColumn
dpnGateFrAccessOperationalState = _DpnGateFrAccessOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 2),
    _DpnGateFrAccessOperationalState_Type()
)
dpnGateFrAccessOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessOperationalState.setStatus("mandatory")


class _DpnGateFrAccessUsageState_Type(Integer32):
    """Custom type dpnGateFrAccessUsageState based on Integer32"""
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


_DpnGateFrAccessUsageState_Type.__name__ = "Integer32"
_DpnGateFrAccessUsageState_Object = MibTableColumn
dpnGateFrAccessUsageState = _DpnGateFrAccessUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 3),
    _DpnGateFrAccessUsageState_Type()
)
dpnGateFrAccessUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessUsageState.setStatus("mandatory")


class _DpnGateFrAccessAvailabilityStatus_Type(OctetString):
    """Custom type dpnGateFrAccessAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DpnGateFrAccessAvailabilityStatus_Type.__name__ = "OctetString"
_DpnGateFrAccessAvailabilityStatus_Object = MibTableColumn
dpnGateFrAccessAvailabilityStatus = _DpnGateFrAccessAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 4),
    _DpnGateFrAccessAvailabilityStatus_Type()
)
dpnGateFrAccessAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessAvailabilityStatus.setStatus("mandatory")


class _DpnGateFrAccessProceduralStatus_Type(OctetString):
    """Custom type dpnGateFrAccessProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DpnGateFrAccessProceduralStatus_Type.__name__ = "OctetString"
_DpnGateFrAccessProceduralStatus_Object = MibTableColumn
dpnGateFrAccessProceduralStatus = _DpnGateFrAccessProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 5),
    _DpnGateFrAccessProceduralStatus_Type()
)
dpnGateFrAccessProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessProceduralStatus.setStatus("mandatory")


class _DpnGateFrAccessControlStatus_Type(OctetString):
    """Custom type dpnGateFrAccessControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DpnGateFrAccessControlStatus_Type.__name__ = "OctetString"
_DpnGateFrAccessControlStatus_Object = MibTableColumn
dpnGateFrAccessControlStatus = _DpnGateFrAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 6),
    _DpnGateFrAccessControlStatus_Type()
)
dpnGateFrAccessControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessControlStatus.setStatus("mandatory")


class _DpnGateFrAccessAlarmStatus_Type(OctetString):
    """Custom type dpnGateFrAccessAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DpnGateFrAccessAlarmStatus_Type.__name__ = "OctetString"
_DpnGateFrAccessAlarmStatus_Object = MibTableColumn
dpnGateFrAccessAlarmStatus = _DpnGateFrAccessAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 7),
    _DpnGateFrAccessAlarmStatus_Type()
)
dpnGateFrAccessAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessAlarmStatus.setStatus("mandatory")


class _DpnGateFrAccessStandbyStatus_Type(Integer32):
    """Custom type dpnGateFrAccessStandbyStatus based on Integer32"""
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


_DpnGateFrAccessStandbyStatus_Type.__name__ = "Integer32"
_DpnGateFrAccessStandbyStatus_Object = MibTableColumn
dpnGateFrAccessStandbyStatus = _DpnGateFrAccessStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 8),
    _DpnGateFrAccessStandbyStatus_Type()
)
dpnGateFrAccessStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessStandbyStatus.setStatus("mandatory")


class _DpnGateFrAccessUnknownStatus_Type(Integer32):
    """Custom type dpnGateFrAccessUnknownStatus based on Integer32"""
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


_DpnGateFrAccessUnknownStatus_Type.__name__ = "Integer32"
_DpnGateFrAccessUnknownStatus_Object = MibTableColumn
dpnGateFrAccessUnknownStatus = _DpnGateFrAccessUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 11, 1, 9),
    _DpnGateFrAccessUnknownStatus_Type()
)
dpnGateFrAccessUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessUnknownStatus.setStatus("mandatory")
_DpnGateFrAccessOpTable_Object = MibTable
dpnGateFrAccessOpTable = _DpnGateFrAccessOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 12)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessOpTable.setStatus("mandatory")
_DpnGateFrAccessOpEntry_Object = MibTableRow
dpnGateFrAccessOpEntry = _DpnGateFrAccessOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 12, 1)
)
dpnGateFrAccessOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessOpEntry.setStatus("mandatory")


class _DpnGateFrAccessRoundTripDelay_Type(Gauge32):
    """Custom type dpnGateFrAccessRoundTripDelay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_DpnGateFrAccessRoundTripDelay_Type.__name__ = "Gauge32"
_DpnGateFrAccessRoundTripDelay_Object = MibTableColumn
dpnGateFrAccessRoundTripDelay = _DpnGateFrAccessRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 12, 1, 1),
    _DpnGateFrAccessRoundTripDelay_Type()
)
dpnGateFrAccessRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessRoundTripDelay.setStatus("mandatory")
_DpnGateFrAccessStatsTable_Object = MibTable
dpnGateFrAccessStatsTable = _DpnGateFrAccessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13)
)
if mibBuilder.loadTexts:
    dpnGateFrAccessStatsTable.setStatus("mandatory")
_DpnGateFrAccessStatsEntry_Object = MibTableRow
dpnGateFrAccessStatsEntry = _DpnGateFrAccessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1)
)
dpnGateFrAccessStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DpnTrunksMIB", "dpnGateIndex"),
    (0, "Nortel-Magellan-Passport-FraDpnTrunksMIB", "dpnGateFrAccessIndex"),
)
if mibBuilder.loadTexts:
    dpnGateFrAccessStatsEntry.setStatus("mandatory")
_DpnGateFrAccessReceivedBytesFromIf_Type = Counter32
_DpnGateFrAccessReceivedBytesFromIf_Object = MibTableColumn
dpnGateFrAccessReceivedBytesFromIf = _DpnGateFrAccessReceivedBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1, 1),
    _DpnGateFrAccessReceivedBytesFromIf_Type()
)
dpnGateFrAccessReceivedBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessReceivedBytesFromIf.setStatus("mandatory")
_DpnGateFrAccessLostFramesFromIf_Type = Counter32
_DpnGateFrAccessLostFramesFromIf_Object = MibTableColumn
dpnGateFrAccessLostFramesFromIf = _DpnGateFrAccessLostFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1, 2),
    _DpnGateFrAccessLostFramesFromIf_Type()
)
dpnGateFrAccessLostFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessLostFramesFromIf.setStatus("mandatory")
_DpnGateFrAccessDiscardBadFromIf_Type = Counter32
_DpnGateFrAccessDiscardBadFromIf_Object = MibTableColumn
dpnGateFrAccessDiscardBadFromIf = _DpnGateFrAccessDiscardBadFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1, 3),
    _DpnGateFrAccessDiscardBadFromIf_Type()
)
dpnGateFrAccessDiscardBadFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessDiscardBadFromIf.setStatus("mandatory")
_DpnGateFrAccessDiscardExcessToIf_Type = Counter32
_DpnGateFrAccessDiscardExcessToIf_Object = MibTableColumn
dpnGateFrAccessDiscardExcessToIf = _DpnGateFrAccessDiscardExcessToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 61, 4, 13, 1, 4),
    _DpnGateFrAccessDiscardExcessToIf_Type()
)
dpnGateFrAccessDiscardExcessToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpnGateFrAccessDiscardExcessToIf.setStatus("mandatory")
_FraDpnTrunksMIB_ObjectIdentity = ObjectIdentity
fraDpnTrunksMIB = _FraDpnTrunksMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68)
)
_FraDpnTrunksGroup_ObjectIdentity = ObjectIdentity
fraDpnTrunksGroup = _FraDpnTrunksGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 1)
)
_FraDpnTrunksGroupBE_ObjectIdentity = ObjectIdentity
fraDpnTrunksGroupBE = _FraDpnTrunksGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 1, 5)
)
_FraDpnTrunksGroupBE00_ObjectIdentity = ObjectIdentity
fraDpnTrunksGroupBE00 = _FraDpnTrunksGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 1, 5, 1)
)
_FraDpnTrunksGroupBE00A_ObjectIdentity = ObjectIdentity
fraDpnTrunksGroupBE00A = _FraDpnTrunksGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 1, 5, 1, 2)
)
_FraDpnTrunksCapabilities_ObjectIdentity = ObjectIdentity
fraDpnTrunksCapabilities = _FraDpnTrunksCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 3)
)
_FraDpnTrunksCapabilitiesBE_ObjectIdentity = ObjectIdentity
fraDpnTrunksCapabilitiesBE = _FraDpnTrunksCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 3, 5)
)
_FraDpnTrunksCapabilitiesBE00_ObjectIdentity = ObjectIdentity
fraDpnTrunksCapabilitiesBE00 = _FraDpnTrunksCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 3, 5, 1)
)
_FraDpnTrunksCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
fraDpnTrunksCapabilitiesBE00A = _FraDpnTrunksCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 68, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FraDpnTrunksMIB",
    **{"dpnGateFrAccess": dpnGateFrAccess,
       "dpnGateFrAccessRowStatusTable": dpnGateFrAccessRowStatusTable,
       "dpnGateFrAccessRowStatusEntry": dpnGateFrAccessRowStatusEntry,
       "dpnGateFrAccessRowStatus": dpnGateFrAccessRowStatus,
       "dpnGateFrAccessComponentName": dpnGateFrAccessComponentName,
       "dpnGateFrAccessStorageType": dpnGateFrAccessStorageType,
       "dpnGateFrAccessIndex": dpnGateFrAccessIndex,
       "dpnGateFrAccessFrMuxSetup": dpnGateFrAccessFrMuxSetup,
       "dpnGateFrAccessFrMuxSetupRowStatusTable": dpnGateFrAccessFrMuxSetupRowStatusTable,
       "dpnGateFrAccessFrMuxSetupRowStatusEntry": dpnGateFrAccessFrMuxSetupRowStatusEntry,
       "dpnGateFrAccessFrMuxSetupRowStatus": dpnGateFrAccessFrMuxSetupRowStatus,
       "dpnGateFrAccessFrMuxSetupComponentName": dpnGateFrAccessFrMuxSetupComponentName,
       "dpnGateFrAccessFrMuxSetupStorageType": dpnGateFrAccessFrMuxSetupStorageType,
       "dpnGateFrAccessFrMuxSetupIndex": dpnGateFrAccessFrMuxSetupIndex,
       "dpnGateFrAccessFrMuxSetupPvcSetup": dpnGateFrAccessFrMuxSetupPvcSetup,
       "dpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable": dpnGateFrAccessFrMuxSetupPvcSetupRowStatusTable,
       "dpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry": dpnGateFrAccessFrMuxSetupPvcSetupRowStatusEntry,
       "dpnGateFrAccessFrMuxSetupPvcSetupRowStatus": dpnGateFrAccessFrMuxSetupPvcSetupRowStatus,
       "dpnGateFrAccessFrMuxSetupPvcSetupComponentName": dpnGateFrAccessFrMuxSetupPvcSetupComponentName,
       "dpnGateFrAccessFrMuxSetupPvcSetupStorageType": dpnGateFrAccessFrMuxSetupPvcSetupStorageType,
       "dpnGateFrAccessFrMuxSetupPvcSetupIndex": dpnGateFrAccessFrMuxSetupPvcSetupIndex,
       "dpnGateFrAccessFrMuxSetupPvcSetupProvTable": dpnGateFrAccessFrMuxSetupPvcSetupProvTable,
       "dpnGateFrAccessFrMuxSetupPvcSetupProvEntry": dpnGateFrAccessFrMuxSetupPvcSetupProvEntry,
       "dpnGateFrAccessFrMuxSetupPvcSetupDlciName": dpnGateFrAccessFrMuxSetupPvcSetupDlciName,
       "dpnGateFrAccessFrMuxSetupTrafficDescrTable": dpnGateFrAccessFrMuxSetupTrafficDescrTable,
       "dpnGateFrAccessFrMuxSetupTrafficDescrEntry": dpnGateFrAccessFrMuxSetupTrafficDescrEntry,
       "dpnGateFrAccessFrMuxSetupCommittedInformationRate": dpnGateFrAccessFrMuxSetupCommittedInformationRate,
       "dpnGateFrAccessFrMuxSetupCommittedBurstSize": dpnGateFrAccessFrMuxSetupCommittedBurstSize,
       "dpnGateFrAccessFrMuxSetupMaximumFrameSize": dpnGateFrAccessFrMuxSetupMaximumFrameSize,
       "dpnGateFrAccessFrMuxSetupDlciCompNameOpTable": dpnGateFrAccessFrMuxSetupDlciCompNameOpTable,
       "dpnGateFrAccessFrMuxSetupDlciCompNameOpEntry": dpnGateFrAccessFrMuxSetupDlciCompNameOpEntry,
       "dpnGateFrAccessFrMuxSetupDlciCompName": dpnGateFrAccessFrMuxSetupDlciCompName,
       "dpnGateFrAccessProvTable": dpnGateFrAccessProvTable,
       "dpnGateFrAccessProvEntry": dpnGateFrAccessProvEntry,
       "dpnGateFrAccessMaximumErroredInterval": dpnGateFrAccessMaximumErroredInterval,
       "dpnGateFrAccessReceiveErrorSensitivity": dpnGateFrAccessReceiveErrorSensitivity,
       "dpnGateFrAccessStateTable": dpnGateFrAccessStateTable,
       "dpnGateFrAccessStateEntry": dpnGateFrAccessStateEntry,
       "dpnGateFrAccessAdminState": dpnGateFrAccessAdminState,
       "dpnGateFrAccessOperationalState": dpnGateFrAccessOperationalState,
       "dpnGateFrAccessUsageState": dpnGateFrAccessUsageState,
       "dpnGateFrAccessAvailabilityStatus": dpnGateFrAccessAvailabilityStatus,
       "dpnGateFrAccessProceduralStatus": dpnGateFrAccessProceduralStatus,
       "dpnGateFrAccessControlStatus": dpnGateFrAccessControlStatus,
       "dpnGateFrAccessAlarmStatus": dpnGateFrAccessAlarmStatus,
       "dpnGateFrAccessStandbyStatus": dpnGateFrAccessStandbyStatus,
       "dpnGateFrAccessUnknownStatus": dpnGateFrAccessUnknownStatus,
       "dpnGateFrAccessOpTable": dpnGateFrAccessOpTable,
       "dpnGateFrAccessOpEntry": dpnGateFrAccessOpEntry,
       "dpnGateFrAccessRoundTripDelay": dpnGateFrAccessRoundTripDelay,
       "dpnGateFrAccessStatsTable": dpnGateFrAccessStatsTable,
       "dpnGateFrAccessStatsEntry": dpnGateFrAccessStatsEntry,
       "dpnGateFrAccessReceivedBytesFromIf": dpnGateFrAccessReceivedBytesFromIf,
       "dpnGateFrAccessLostFramesFromIf": dpnGateFrAccessLostFramesFromIf,
       "dpnGateFrAccessDiscardBadFromIf": dpnGateFrAccessDiscardBadFromIf,
       "dpnGateFrAccessDiscardExcessToIf": dpnGateFrAccessDiscardExcessToIf,
       "fraDpnTrunksMIB": fraDpnTrunksMIB,
       "fraDpnTrunksGroup": fraDpnTrunksGroup,
       "fraDpnTrunksGroupBE": fraDpnTrunksGroupBE,
       "fraDpnTrunksGroupBE00": fraDpnTrunksGroupBE00,
       "fraDpnTrunksGroupBE00A": fraDpnTrunksGroupBE00A,
       "fraDpnTrunksCapabilities": fraDpnTrunksCapabilities,
       "fraDpnTrunksCapabilitiesBE": fraDpnTrunksCapabilitiesBE,
       "fraDpnTrunksCapabilitiesBE00": fraDpnTrunksCapabilitiesBE00,
       "fraDpnTrunksCapabilitiesBE00A": fraDpnTrunksCapabilitiesBE00A}
)
