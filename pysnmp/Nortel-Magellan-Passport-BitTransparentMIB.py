# SNMP MIB module (Nortel-Magellan-Passport-BitTransparentMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-BitTransparentMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:27 2024
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
 InterfaceIndex,
 PassportCounter64,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "PassportCounter64",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
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

_Btds_ObjectIdentity = ObjectIdentity
btds = _Btds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81)
)
_BtdsRowStatusTable_Object = MibTable
btdsRowStatusTable = _BtdsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 1)
)
if mibBuilder.loadTexts:
    btdsRowStatusTable.setStatus("mandatory")
_BtdsRowStatusEntry_Object = MibTableRow
btdsRowStatusEntry = _BtdsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 1, 1)
)
btdsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
)
if mibBuilder.loadTexts:
    btdsRowStatusEntry.setStatus("mandatory")
_BtdsRowStatus_Type = RowStatus
_BtdsRowStatus_Object = MibTableColumn
btdsRowStatus = _BtdsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 1, 1, 1),
    _BtdsRowStatus_Type()
)
btdsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsRowStatus.setStatus("mandatory")
_BtdsComponentName_Type = DisplayString
_BtdsComponentName_Object = MibTableColumn
btdsComponentName = _BtdsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 1, 1, 2),
    _BtdsComponentName_Type()
)
btdsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsComponentName.setStatus("mandatory")
_BtdsStorageType_Type = StorageType
_BtdsStorageType_Object = MibTableColumn
btdsStorageType = _BtdsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 1, 1, 4),
    _BtdsStorageType_Type()
)
btdsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsStorageType.setStatus("mandatory")


class _BtdsIndex_Type(Integer32):
    """Custom type btdsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BtdsIndex_Type.__name__ = "Integer32"
_BtdsIndex_Object = MibTableColumn
btdsIndex = _BtdsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 1, 1, 10),
    _BtdsIndex_Type()
)
btdsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btdsIndex.setStatus("mandatory")
_BtdsFramer_ObjectIdentity = ObjectIdentity
btdsFramer = _BtdsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2)
)
_BtdsFramerRowStatusTable_Object = MibTable
btdsFramerRowStatusTable = _BtdsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 1)
)
if mibBuilder.loadTexts:
    btdsFramerRowStatusTable.setStatus("mandatory")
_BtdsFramerRowStatusEntry_Object = MibTableRow
btdsFramerRowStatusEntry = _BtdsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 1, 1)
)
btdsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsFramerIndex"),
)
if mibBuilder.loadTexts:
    btdsFramerRowStatusEntry.setStatus("mandatory")
_BtdsFramerRowStatus_Type = RowStatus
_BtdsFramerRowStatus_Object = MibTableColumn
btdsFramerRowStatus = _BtdsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 1, 1, 1),
    _BtdsFramerRowStatus_Type()
)
btdsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerRowStatus.setStatus("mandatory")
_BtdsFramerComponentName_Type = DisplayString
_BtdsFramerComponentName_Object = MibTableColumn
btdsFramerComponentName = _BtdsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 1, 1, 2),
    _BtdsFramerComponentName_Type()
)
btdsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerComponentName.setStatus("mandatory")
_BtdsFramerStorageType_Type = StorageType
_BtdsFramerStorageType_Object = MibTableColumn
btdsFramerStorageType = _BtdsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 1, 1, 4),
    _BtdsFramerStorageType_Type()
)
btdsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerStorageType.setStatus("mandatory")
_BtdsFramerIndex_Type = NonReplicated
_BtdsFramerIndex_Object = MibTableColumn
btdsFramerIndex = _BtdsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 1, 1, 10),
    _BtdsFramerIndex_Type()
)
btdsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btdsFramerIndex.setStatus("mandatory")
_BtdsFramerProvTable_Object = MibTable
btdsFramerProvTable = _BtdsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 10)
)
if mibBuilder.loadTexts:
    btdsFramerProvTable.setStatus("mandatory")
_BtdsFramerProvEntry_Object = MibTableRow
btdsFramerProvEntry = _BtdsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 10, 1)
)
btdsFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsFramerIndex"),
)
if mibBuilder.loadTexts:
    btdsFramerProvEntry.setStatus("mandatory")
_BtdsFramerInterfaceName_Type = Link
_BtdsFramerInterfaceName_Object = MibTableColumn
btdsFramerInterfaceName = _BtdsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 10, 1, 1),
    _BtdsFramerInterfaceName_Type()
)
btdsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsFramerInterfaceName.setStatus("mandatory")
_BtdsFramerChannelTable_Object = MibTable
btdsFramerChannelTable = _BtdsFramerChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 11)
)
if mibBuilder.loadTexts:
    btdsFramerChannelTable.setStatus("mandatory")
_BtdsFramerChannelEntry_Object = MibTableRow
btdsFramerChannelEntry = _BtdsFramerChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 11, 1)
)
btdsFramerChannelEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsFramerIndex"),
)
if mibBuilder.loadTexts:
    btdsFramerChannelEntry.setStatus("mandatory")


class _BtdsFramerProtocol_Type(Integer32):
    """Custom type btdsFramerProtocol based on Integer32"""
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
        *(("hdlc", 1),
          ("none", 0),
          ("nrziHdlc", 2),
          ("universal", 3))
    )


_BtdsFramerProtocol_Type.__name__ = "Integer32"
_BtdsFramerProtocol_Object = MibTableColumn
btdsFramerProtocol = _BtdsFramerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 11, 1, 7),
    _BtdsFramerProtocol_Type()
)
btdsFramerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsFramerProtocol.setStatus("mandatory")


class _BtdsFramerNumOfIdleBytesToMonitor_Type(Unsigned32):
    """Custom type btdsFramerNumOfIdleBytesToMonitor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_BtdsFramerNumOfIdleBytesToMonitor_Type.__name__ = "Unsigned32"
_BtdsFramerNumOfIdleBytesToMonitor_Object = MibTableColumn
btdsFramerNumOfIdleBytesToMonitor = _BtdsFramerNumOfIdleBytesToMonitor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 11, 1, 8),
    _BtdsFramerNumOfIdleBytesToMonitor_Type()
)
btdsFramerNumOfIdleBytesToMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsFramerNumOfIdleBytesToMonitor.setStatus("mandatory")


class _BtdsFramerIdlePattern_Type(Hex):
    """Custom type btdsFramerIdlePattern based on Hex"""
    defaultValue = 255

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BtdsFramerIdlePattern_Type.__name__ = "Hex"
_BtdsFramerIdlePattern_Object = MibTableColumn
btdsFramerIdlePattern = _BtdsFramerIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 11, 1, 9),
    _BtdsFramerIdlePattern_Type()
)
btdsFramerIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsFramerIdlePattern.setStatus("mandatory")


class _BtdsFramerTimeSlotAlignment_Type(Integer32):
    """Custom type btdsFramerTimeSlotAlignment based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("frameAligned", 1),
          ("unaligned", 0))
    )


_BtdsFramerTimeSlotAlignment_Type.__name__ = "Integer32"
_BtdsFramerTimeSlotAlignment_Object = MibTableColumn
btdsFramerTimeSlotAlignment = _BtdsFramerTimeSlotAlignment_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 11, 1, 10),
    _BtdsFramerTimeSlotAlignment_Type()
)
btdsFramerTimeSlotAlignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsFramerTimeSlotAlignment.setStatus("mandatory")


class _BtdsFramerInsertedOutputDelay_Type(Unsigned32):
    """Custom type btdsFramerInsertedOutputDelay based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_BtdsFramerInsertedOutputDelay_Type.__name__ = "Unsigned32"
_BtdsFramerInsertedOutputDelay_Object = MibTableColumn
btdsFramerInsertedOutputDelay = _BtdsFramerInsertedOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 11, 1, 11),
    _BtdsFramerInsertedOutputDelay_Type()
)
btdsFramerInsertedOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsFramerInsertedOutputDelay.setStatus("mandatory")


class _BtdsFramerBtdsCellSize_Type(Integer32):
    """Custom type btdsFramerBtdsCellSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("n44", 0),
          ("n84", 1))
    )


_BtdsFramerBtdsCellSize_Type.__name__ = "Integer32"
_BtdsFramerBtdsCellSize_Object = MibTableColumn
btdsFramerBtdsCellSize = _BtdsFramerBtdsCellSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 11, 1, 12),
    _BtdsFramerBtdsCellSize_Type()
)
btdsFramerBtdsCellSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsFramerBtdsCellSize.setStatus("mandatory")
_BtdsFramerStateTable_Object = MibTable
btdsFramerStateTable = _BtdsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 12)
)
if mibBuilder.loadTexts:
    btdsFramerStateTable.setStatus("mandatory")
_BtdsFramerStateEntry_Object = MibTableRow
btdsFramerStateEntry = _BtdsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 12, 1)
)
btdsFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsFramerIndex"),
)
if mibBuilder.loadTexts:
    btdsFramerStateEntry.setStatus("mandatory")


class _BtdsFramerAdminState_Type(Integer32):
    """Custom type btdsFramerAdminState based on Integer32"""
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


_BtdsFramerAdminState_Type.__name__ = "Integer32"
_BtdsFramerAdminState_Object = MibTableColumn
btdsFramerAdminState = _BtdsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 12, 1, 1),
    _BtdsFramerAdminState_Type()
)
btdsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerAdminState.setStatus("mandatory")


class _BtdsFramerOperationalState_Type(Integer32):
    """Custom type btdsFramerOperationalState based on Integer32"""
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


_BtdsFramerOperationalState_Type.__name__ = "Integer32"
_BtdsFramerOperationalState_Object = MibTableColumn
btdsFramerOperationalState = _BtdsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 12, 1, 2),
    _BtdsFramerOperationalState_Type()
)
btdsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerOperationalState.setStatus("mandatory")


class _BtdsFramerUsageState_Type(Integer32):
    """Custom type btdsFramerUsageState based on Integer32"""
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


_BtdsFramerUsageState_Type.__name__ = "Integer32"
_BtdsFramerUsageState_Object = MibTableColumn
btdsFramerUsageState = _BtdsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 12, 1, 3),
    _BtdsFramerUsageState_Type()
)
btdsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerUsageState.setStatus("mandatory")
_BtdsFramerStatsTable_Object = MibTable
btdsFramerStatsTable = _BtdsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 13)
)
if mibBuilder.loadTexts:
    btdsFramerStatsTable.setStatus("mandatory")
_BtdsFramerStatsEntry_Object = MibTableRow
btdsFramerStatsEntry = _BtdsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 13, 1)
)
btdsFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsFramerIndex"),
)
if mibBuilder.loadTexts:
    btdsFramerStatsEntry.setStatus("mandatory")
_BtdsFramerFrmFromIf_Type = Counter32
_BtdsFramerFrmFromIf_Object = MibTableColumn
btdsFramerFrmFromIf = _BtdsFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 13, 1, 1),
    _BtdsFramerFrmFromIf_Type()
)
btdsFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerFrmFromIf.setStatus("mandatory")
_BtdsFramerSuppressedFrames_Type = Counter32
_BtdsFramerSuppressedFrames_Object = MibTableColumn
btdsFramerSuppressedFrames = _BtdsFramerSuppressedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 13, 1, 3),
    _BtdsFramerSuppressedFrames_Type()
)
btdsFramerSuppressedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerSuppressedFrames.setStatus("mandatory")
_BtdsFramerFrmToIf_Type = Counter32
_BtdsFramerFrmToIf_Object = MibTableColumn
btdsFramerFrmToIf = _BtdsFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 13, 1, 4),
    _BtdsFramerFrmToIf_Type()
)
btdsFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerFrmToIf.setStatus("mandatory")
_BtdsFramerLrcErrors_Type = Counter32
_BtdsFramerLrcErrors_Object = MibTableColumn
btdsFramerLrcErrors = _BtdsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 13, 1, 5),
    _BtdsFramerLrcErrors_Type()
)
btdsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerLrcErrors.setStatus("mandatory")
_BtdsFramerFrmLostInNetwork_Type = Counter32
_BtdsFramerFrmLostInNetwork_Object = MibTableColumn
btdsFramerFrmLostInNetwork = _BtdsFramerFrmLostInNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 13, 1, 6),
    _BtdsFramerFrmLostInNetwork_Type()
)
btdsFramerFrmLostInNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerFrmLostInNetwork.setStatus("mandatory")
_BtdsFramerFrmUnderRuns_Type = Counter32
_BtdsFramerFrmUnderRuns_Object = MibTableColumn
btdsFramerFrmUnderRuns = _BtdsFramerFrmUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 13, 1, 7),
    _BtdsFramerFrmUnderRuns_Type()
)
btdsFramerFrmUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerFrmUnderRuns.setStatus("mandatory")
_BtdsFramerFrmDumped_Type = Counter32
_BtdsFramerFrmDumped_Object = MibTableColumn
btdsFramerFrmDumped = _BtdsFramerFrmDumped_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 2, 13, 1, 8),
    _BtdsFramerFrmDumped_Type()
)
btdsFramerFrmDumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsFramerFrmDumped.setStatus("mandatory")
_BtdsPlc_ObjectIdentity = ObjectIdentity
btdsPlc = _BtdsPlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3)
)
_BtdsPlcRowStatusTable_Object = MibTable
btdsPlcRowStatusTable = _BtdsPlcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 1)
)
if mibBuilder.loadTexts:
    btdsPlcRowStatusTable.setStatus("mandatory")
_BtdsPlcRowStatusEntry_Object = MibTableRow
btdsPlcRowStatusEntry = _BtdsPlcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 1, 1)
)
btdsPlcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsPlcIndex"),
)
if mibBuilder.loadTexts:
    btdsPlcRowStatusEntry.setStatus("mandatory")
_BtdsPlcRowStatus_Type = RowStatus
_BtdsPlcRowStatus_Object = MibTableColumn
btdsPlcRowStatus = _BtdsPlcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 1, 1, 1),
    _BtdsPlcRowStatus_Type()
)
btdsPlcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsPlcRowStatus.setStatus("mandatory")
_BtdsPlcComponentName_Type = DisplayString
_BtdsPlcComponentName_Object = MibTableColumn
btdsPlcComponentName = _BtdsPlcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 1, 1, 2),
    _BtdsPlcComponentName_Type()
)
btdsPlcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsPlcComponentName.setStatus("mandatory")
_BtdsPlcStorageType_Type = StorageType
_BtdsPlcStorageType_Object = MibTableColumn
btdsPlcStorageType = _BtdsPlcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 1, 1, 4),
    _BtdsPlcStorageType_Type()
)
btdsPlcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsPlcStorageType.setStatus("mandatory")
_BtdsPlcIndex_Type = NonReplicated
_BtdsPlcIndex_Object = MibTableColumn
btdsPlcIndex = _BtdsPlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 1, 1, 10),
    _BtdsPlcIndex_Type()
)
btdsPlcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btdsPlcIndex.setStatus("mandatory")
_BtdsPlcProvTable_Object = MibTable
btdsPlcProvTable = _BtdsPlcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10)
)
if mibBuilder.loadTexts:
    btdsPlcProvTable.setStatus("mandatory")
_BtdsPlcProvEntry_Object = MibTableRow
btdsPlcProvEntry = _BtdsPlcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1)
)
btdsPlcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsPlcIndex"),
)
if mibBuilder.loadTexts:
    btdsPlcProvEntry.setStatus("mandatory")


class _BtdsPlcRemoteName_Type(AsciiString):
    """Custom type btdsPlcRemoteName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BtdsPlcRemoteName_Type.__name__ = "AsciiString"
_BtdsPlcRemoteName_Object = MibTableColumn
btdsPlcRemoteName = _BtdsPlcRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 2),
    _BtdsPlcRemoteName_Type()
)
btdsPlcRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcRemoteName.setStatus("mandatory")


class _BtdsPlcSetupPriority_Type(Unsigned32):
    """Custom type btdsPlcSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BtdsPlcSetupPriority_Type.__name__ = "Unsigned32"
_BtdsPlcSetupPriority_Object = MibTableColumn
btdsPlcSetupPriority = _BtdsPlcSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 3),
    _BtdsPlcSetupPriority_Type()
)
btdsPlcSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcSetupPriority.setStatus("mandatory")


class _BtdsPlcHoldingPriority_Type(Unsigned32):
    """Custom type btdsPlcHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BtdsPlcHoldingPriority_Type.__name__ = "Unsigned32"
_BtdsPlcHoldingPriority_Object = MibTableColumn
btdsPlcHoldingPriority = _BtdsPlcHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 4),
    _BtdsPlcHoldingPriority_Type()
)
btdsPlcHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcHoldingPriority.setStatus("mandatory")


class _BtdsPlcRequiredTxBandwidth_Type(Unsigned32):
    """Custom type btdsPlcRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BtdsPlcRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_BtdsPlcRequiredTxBandwidth_Object = MibTableColumn
btdsPlcRequiredTxBandwidth = _BtdsPlcRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 5),
    _BtdsPlcRequiredTxBandwidth_Type()
)
btdsPlcRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcRequiredTxBandwidth.setStatus("mandatory")


class _BtdsPlcRequiredRxBandwidth_Type(Unsigned32):
    """Custom type btdsPlcRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BtdsPlcRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_BtdsPlcRequiredRxBandwidth_Object = MibTableColumn
btdsPlcRequiredRxBandwidth = _BtdsPlcRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 6),
    _BtdsPlcRequiredRxBandwidth_Type()
)
btdsPlcRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcRequiredRxBandwidth.setStatus("mandatory")


class _BtdsPlcRequiredTrafficType_Type(Integer32):
    """Custom type btdsPlcRequiredTrafficType based on Integer32"""
    defaultValue = 2

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
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_BtdsPlcRequiredTrafficType_Type.__name__ = "Integer32"
_BtdsPlcRequiredTrafficType_Object = MibTableColumn
btdsPlcRequiredTrafficType = _BtdsPlcRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 7),
    _BtdsPlcRequiredTrafficType_Type()
)
btdsPlcRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcRequiredTrafficType.setStatus("mandatory")


class _BtdsPlcPermittedTrunkTypes_Type(OctetString):
    """Custom type btdsPlcPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BtdsPlcPermittedTrunkTypes_Type.__name__ = "OctetString"
_BtdsPlcPermittedTrunkTypes_Object = MibTableColumn
btdsPlcPermittedTrunkTypes = _BtdsPlcPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 8),
    _BtdsPlcPermittedTrunkTypes_Type()
)
btdsPlcPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcPermittedTrunkTypes.setStatus("mandatory")


class _BtdsPlcRequiredSecurity_Type(Unsigned32):
    """Custom type btdsPlcRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BtdsPlcRequiredSecurity_Type.__name__ = "Unsigned32"
_BtdsPlcRequiredSecurity_Object = MibTableColumn
btdsPlcRequiredSecurity = _BtdsPlcRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 9),
    _BtdsPlcRequiredSecurity_Type()
)
btdsPlcRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcRequiredSecurity.setStatus("mandatory")


class _BtdsPlcRequiredCustomerParm_Type(Unsigned32):
    """Custom type btdsPlcRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BtdsPlcRequiredCustomerParm_Type.__name__ = "Unsigned32"
_BtdsPlcRequiredCustomerParm_Object = MibTableColumn
btdsPlcRequiredCustomerParm = _BtdsPlcRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 10),
    _BtdsPlcRequiredCustomerParm_Type()
)
btdsPlcRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcRequiredCustomerParm.setStatus("mandatory")


class _BtdsPlcPathAttributeToMinimize_Type(Integer32):
    """Custom type btdsPlcPathAttributeToMinimize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cost", 0),
          ("delay", 1))
    )


_BtdsPlcPathAttributeToMinimize_Type.__name__ = "Integer32"
_BtdsPlcPathAttributeToMinimize_Object = MibTableColumn
btdsPlcPathAttributeToMinimize = _BtdsPlcPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 11),
    _BtdsPlcPathAttributeToMinimize_Type()
)
btdsPlcPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcPathAttributeToMinimize.setStatus("mandatory")


class _BtdsPlcMaximumAcceptableCost_Type(Unsigned32):
    """Custom type btdsPlcMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtdsPlcMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_BtdsPlcMaximumAcceptableCost_Object = MibTableColumn
btdsPlcMaximumAcceptableCost = _BtdsPlcMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 12),
    _BtdsPlcMaximumAcceptableCost_Type()
)
btdsPlcMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcMaximumAcceptableCost.setStatus("mandatory")


class _BtdsPlcMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type btdsPlcMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_BtdsPlcMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_BtdsPlcMaximumAcceptableDelay_Object = MibTableColumn
btdsPlcMaximumAcceptableDelay = _BtdsPlcMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 13),
    _BtdsPlcMaximumAcceptableDelay_Type()
)
btdsPlcMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcMaximumAcceptableDelay.setStatus("mandatory")


class _BtdsPlcEmissionPriority_Type(Unsigned32):
    """Custom type btdsPlcEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BtdsPlcEmissionPriority_Type.__name__ = "Unsigned32"
_BtdsPlcEmissionPriority_Object = MibTableColumn
btdsPlcEmissionPriority = _BtdsPlcEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 14),
    _BtdsPlcEmissionPriority_Type()
)
btdsPlcEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcEmissionPriority.setStatus("mandatory")


class _BtdsPlcDiscardPriority_Type(Unsigned32):
    """Custom type btdsPlcDiscardPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BtdsPlcDiscardPriority_Type.__name__ = "Unsigned32"
_BtdsPlcDiscardPriority_Object = MibTableColumn
btdsPlcDiscardPriority = _BtdsPlcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 15),
    _BtdsPlcDiscardPriority_Type()
)
btdsPlcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcDiscardPriority.setStatus("mandatory")


class _BtdsPlcPathType_Type(Integer32):
    """Custom type btdsPlcPathType based on Integer32"""
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
        *(("forced", 2),
          ("manual", 1),
          ("normal", 0))
    )


_BtdsPlcPathType_Type.__name__ = "Integer32"
_BtdsPlcPathType_Object = MibTableColumn
btdsPlcPathType = _BtdsPlcPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 16),
    _BtdsPlcPathType_Type()
)
btdsPlcPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcPathType.setStatus("mandatory")


class _BtdsPlcPathFailureAction_Type(Integer32):
    """Custom type btdsPlcPathFailureAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_BtdsPlcPathFailureAction_Type.__name__ = "Integer32"
_BtdsPlcPathFailureAction_Object = MibTableColumn
btdsPlcPathFailureAction = _BtdsPlcPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 17),
    _BtdsPlcPathFailureAction_Type()
)
btdsPlcPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcPathFailureAction.setStatus("mandatory")


class _BtdsPlcBumpPreference_Type(Integer32):
    """Custom type btdsPlcBumpPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_BtdsPlcBumpPreference_Type.__name__ = "Integer32"
_BtdsPlcBumpPreference_Object = MibTableColumn
btdsPlcBumpPreference = _BtdsPlcBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 18),
    _BtdsPlcBumpPreference_Type()
)
btdsPlcBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcBumpPreference.setStatus("mandatory")


class _BtdsPlcOptimization_Type(Integer32):
    """Custom type btdsPlcOptimization based on Integer32"""
    defaultValue = 1

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


_BtdsPlcOptimization_Type.__name__ = "Integer32"
_BtdsPlcOptimization_Object = MibTableColumn
btdsPlcOptimization = _BtdsPlcOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 10, 1, 19),
    _BtdsPlcOptimization_Type()
)
btdsPlcOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcOptimization.setStatus("mandatory")
_BtdsPlcMpathTable_Object = MibTable
btdsPlcMpathTable = _BtdsPlcMpathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 262)
)
if mibBuilder.loadTexts:
    btdsPlcMpathTable.setStatus("mandatory")
_BtdsPlcMpathEntry_Object = MibTableRow
btdsPlcMpathEntry = _BtdsPlcMpathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 262, 1)
)
btdsPlcMpathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsPlcIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsPlcMpathIndex"),
)
if mibBuilder.loadTexts:
    btdsPlcMpathEntry.setStatus("mandatory")


class _BtdsPlcMpathIndex_Type(Integer32):
    """Custom type btdsPlcMpathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_BtdsPlcMpathIndex_Type.__name__ = "Integer32"
_BtdsPlcMpathIndex_Object = MibTableColumn
btdsPlcMpathIndex = _BtdsPlcMpathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 262, 1, 1),
    _BtdsPlcMpathIndex_Type()
)
btdsPlcMpathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btdsPlcMpathIndex.setStatus("mandatory")


class _BtdsPlcMpathValue_Type(AsciiString):
    """Custom type btdsPlcMpathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BtdsPlcMpathValue_Type.__name__ = "AsciiString"
_BtdsPlcMpathValue_Object = MibTableColumn
btdsPlcMpathValue = _BtdsPlcMpathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 3, 262, 1, 2),
    _BtdsPlcMpathValue_Type()
)
btdsPlcMpathValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsPlcMpathValue.setStatus("mandatory")
_BtdsLCo_ObjectIdentity = ObjectIdentity
btdsLCo = _BtdsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4)
)
_BtdsLCoRowStatusTable_Object = MibTable
btdsLCoRowStatusTable = _BtdsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 1)
)
if mibBuilder.loadTexts:
    btdsLCoRowStatusTable.setStatus("mandatory")
_BtdsLCoRowStatusEntry_Object = MibTableRow
btdsLCoRowStatusEntry = _BtdsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 1, 1)
)
btdsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsLCoIndex"),
)
if mibBuilder.loadTexts:
    btdsLCoRowStatusEntry.setStatus("mandatory")
_BtdsLCoRowStatus_Type = RowStatus
_BtdsLCoRowStatus_Object = MibTableColumn
btdsLCoRowStatus = _BtdsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 1, 1, 1),
    _BtdsLCoRowStatus_Type()
)
btdsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoRowStatus.setStatus("mandatory")
_BtdsLCoComponentName_Type = DisplayString
_BtdsLCoComponentName_Object = MibTableColumn
btdsLCoComponentName = _BtdsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 1, 1, 2),
    _BtdsLCoComponentName_Type()
)
btdsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoComponentName.setStatus("mandatory")
_BtdsLCoStorageType_Type = StorageType
_BtdsLCoStorageType_Object = MibTableColumn
btdsLCoStorageType = _BtdsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 1, 1, 4),
    _BtdsLCoStorageType_Type()
)
btdsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoStorageType.setStatus("mandatory")
_BtdsLCoIndex_Type = NonReplicated
_BtdsLCoIndex_Object = MibTableColumn
btdsLCoIndex = _BtdsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 1, 1, 10),
    _BtdsLCoIndex_Type()
)
btdsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btdsLCoIndex.setStatus("mandatory")
_BtdsLCoPathDataTable_Object = MibTable
btdsLCoPathDataTable = _BtdsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10)
)
if mibBuilder.loadTexts:
    btdsLCoPathDataTable.setStatus("mandatory")
_BtdsLCoPathDataEntry_Object = MibTableRow
btdsLCoPathDataEntry = _BtdsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1)
)
btdsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsLCoIndex"),
)
if mibBuilder.loadTexts:
    btdsLCoPathDataEntry.setStatus("mandatory")


class _BtdsLCoState_Type(Integer32):
    """Custom type btdsLCoState based on Integer32"""
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
        *(("connecting", 2),
          ("pathDown", 0),
          ("pathDownRetrying", 4),
          ("pathUp", 3),
          ("selectingRoute", 1))
    )


_BtdsLCoState_Type.__name__ = "Integer32"
_BtdsLCoState_Object = MibTableColumn
btdsLCoState = _BtdsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 1),
    _BtdsLCoState_Type()
)
btdsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoState.setStatus("mandatory")


class _BtdsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type btdsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BtdsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_BtdsLCoOverrideRemoteName_Object = MibTableColumn
btdsLCoOverrideRemoteName = _BtdsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 2),
    _BtdsLCoOverrideRemoteName_Type()
)
btdsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsLCoOverrideRemoteName.setStatus("mandatory")


class _BtdsLCoEnd_Type(Integer32):
    """Custom type btdsLCoEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 0))
    )


_BtdsLCoEnd_Type.__name__ = "Integer32"
_BtdsLCoEnd_Object = MibTableColumn
btdsLCoEnd = _BtdsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 3),
    _BtdsLCoEnd_Type()
)
btdsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoEnd.setStatus("mandatory")


class _BtdsLCoCostMetric_Type(Unsigned32):
    """Custom type btdsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtdsLCoCostMetric_Type.__name__ = "Unsigned32"
_BtdsLCoCostMetric_Object = MibTableColumn
btdsLCoCostMetric = _BtdsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 4),
    _BtdsLCoCostMetric_Type()
)
btdsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoCostMetric.setStatus("mandatory")


class _BtdsLCoDelayMetric_Type(Unsigned32):
    """Custom type btdsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_BtdsLCoDelayMetric_Type.__name__ = "Unsigned32"
_BtdsLCoDelayMetric_Object = MibTableColumn
btdsLCoDelayMetric = _BtdsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 5),
    _BtdsLCoDelayMetric_Type()
)
btdsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoDelayMetric.setStatus("mandatory")


class _BtdsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type btdsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_BtdsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_BtdsLCoRoundTripDelay_Object = MibTableColumn
btdsLCoRoundTripDelay = _BtdsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 6),
    _BtdsLCoRoundTripDelay_Type()
)
btdsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoRoundTripDelay.setStatus("mandatory")


class _BtdsLCoSetupPriority_Type(Unsigned32):
    """Custom type btdsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BtdsLCoSetupPriority_Type.__name__ = "Unsigned32"
_BtdsLCoSetupPriority_Object = MibTableColumn
btdsLCoSetupPriority = _BtdsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 7),
    _BtdsLCoSetupPriority_Type()
)
btdsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoSetupPriority.setStatus("mandatory")


class _BtdsLCoHoldingPriority_Type(Unsigned32):
    """Custom type btdsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BtdsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_BtdsLCoHoldingPriority_Object = MibTableColumn
btdsLCoHoldingPriority = _BtdsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 8),
    _BtdsLCoHoldingPriority_Type()
)
btdsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoHoldingPriority.setStatus("mandatory")


class _BtdsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type btdsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BtdsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_BtdsLCoRequiredTxBandwidth_Object = MibTableColumn
btdsLCoRequiredTxBandwidth = _BtdsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 9),
    _BtdsLCoRequiredTxBandwidth_Type()
)
btdsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoRequiredTxBandwidth.setStatus("mandatory")


class _BtdsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type btdsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BtdsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_BtdsLCoRequiredRxBandwidth_Object = MibTableColumn
btdsLCoRequiredRxBandwidth = _BtdsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 10),
    _BtdsLCoRequiredRxBandwidth_Type()
)
btdsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoRequiredRxBandwidth.setStatus("mandatory")


class _BtdsLCoRequiredTrafficType_Type(Integer32):
    """Custom type btdsLCoRequiredTrafficType based on Integer32"""
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
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_BtdsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_BtdsLCoRequiredTrafficType_Object = MibTableColumn
btdsLCoRequiredTrafficType = _BtdsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 11),
    _BtdsLCoRequiredTrafficType_Type()
)
btdsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoRequiredTrafficType.setStatus("mandatory")


class _BtdsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type btdsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BtdsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_BtdsLCoPermittedTrunkTypes_Object = MibTableColumn
btdsLCoPermittedTrunkTypes = _BtdsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 12),
    _BtdsLCoPermittedTrunkTypes_Type()
)
btdsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoPermittedTrunkTypes.setStatus("mandatory")


class _BtdsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type btdsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BtdsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_BtdsLCoRequiredSecurity_Object = MibTableColumn
btdsLCoRequiredSecurity = _BtdsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 13),
    _BtdsLCoRequiredSecurity_Type()
)
btdsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoRequiredSecurity.setStatus("mandatory")


class _BtdsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type btdsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BtdsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_BtdsLCoRequiredCustomerParameter_Object = MibTableColumn
btdsLCoRequiredCustomerParameter = _BtdsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 14),
    _BtdsLCoRequiredCustomerParameter_Type()
)
btdsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoRequiredCustomerParameter.setStatus("mandatory")


class _BtdsLCoEmissionPriority_Type(Unsigned32):
    """Custom type btdsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BtdsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_BtdsLCoEmissionPriority_Object = MibTableColumn
btdsLCoEmissionPriority = _BtdsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 15),
    _BtdsLCoEmissionPriority_Type()
)
btdsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoEmissionPriority.setStatus("mandatory")


class _BtdsLCoDiscardPriority_Type(Unsigned32):
    """Custom type btdsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BtdsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_BtdsLCoDiscardPriority_Object = MibTableColumn
btdsLCoDiscardPriority = _BtdsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 16),
    _BtdsLCoDiscardPriority_Type()
)
btdsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoDiscardPriority.setStatus("mandatory")


class _BtdsLCoPathType_Type(Integer32):
    """Custom type btdsLCoPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("manual", 1),
          ("normal", 0))
    )


_BtdsLCoPathType_Type.__name__ = "Integer32"
_BtdsLCoPathType_Object = MibTableColumn
btdsLCoPathType = _BtdsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 17),
    _BtdsLCoPathType_Type()
)
btdsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoPathType.setStatus("mandatory")


class _BtdsLCoRetryCount_Type(Unsigned32):
    """Custom type btdsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BtdsLCoRetryCount_Type.__name__ = "Unsigned32"
_BtdsLCoRetryCount_Object = MibTableColumn
btdsLCoRetryCount = _BtdsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 18),
    _BtdsLCoRetryCount_Type()
)
btdsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoRetryCount.setStatus("mandatory")


class _BtdsLCoPathFailureCount_Type(Unsigned32):
    """Custom type btdsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BtdsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_BtdsLCoPathFailureCount_Object = MibTableColumn
btdsLCoPathFailureCount = _BtdsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 19),
    _BtdsLCoPathFailureCount_Type()
)
btdsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoPathFailureCount.setStatus("mandatory")


class _BtdsLCoReasonForNoRoute_Type(Integer32):
    """Custom type btdsLCoReasonForNoRoute based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("anError", 12),
          ("attributeProfileProblem", 13),
          ("attributesNotMet", 11),
          ("destinationNameTooLong", 1),
          ("destinationNotSpecified", 2),
          ("incorrectDestination", 4),
          ("incorrectDestinationEndPoint", 5),
          ("manualPathIndexProblem", 14),
          ("none", 0),
          ("routeCostTooMuch", 9),
          ("routesDelayTooLong", 10),
          ("sameNode", 8),
          ("unknownDestination", 7),
          ("unknownDestinationName", 3),
          ("unknownSource", 6))
    )


_BtdsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_BtdsLCoReasonForNoRoute_Object = MibTableColumn
btdsLCoReasonForNoRoute = _BtdsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 20),
    _BtdsLCoReasonForNoRoute_Type()
)
btdsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoReasonForNoRoute.setStatus("mandatory")


class _BtdsLCoLastTearDownReason_Type(Integer32):
    """Custom type btdsLCoLastTearDownReason based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("accessCardFailure", 20),
          ("bumped", 19),
          ("callLoopedBack", 13),
          ("farEndBusy", 12),
          ("farEndNotFound", 10),
          ("farEndNotReady", 15),
          ("insufficientRxLcOrBandwidth", 3),
          ("insufficientTxLcOrBandwidth", 2),
          ("lostLcnClash", 7),
          ("networkCongestion", 8),
          ("none", 0),
          ("normalShutDown", 1),
          ("operatorForced", 6),
          ("optimized", 21),
          ("overrideRemoteName", 22),
          ("reconnectFromFarEnd", 18),
          ("remoteNameMismatch", 16),
          ("serviceTypeMismatch", 17),
          ("trunkCardFailure", 5),
          ("trunkFailure", 4),
          ("trunkNotFound", 9),
          ("trunkOrFarEndDidNotSupportMode", 23),
          ("unknownReason", 14),
          ("wrongModuleReached", 11))
    )


_BtdsLCoLastTearDownReason_Type.__name__ = "Integer32"
_BtdsLCoLastTearDownReason_Object = MibTableColumn
btdsLCoLastTearDownReason = _BtdsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 21),
    _BtdsLCoLastTearDownReason_Type()
)
btdsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoLastTearDownReason.setStatus("mandatory")


class _BtdsLCoPathFailureAction_Type(Integer32):
    """Custom type btdsLCoPathFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_BtdsLCoPathFailureAction_Type.__name__ = "Integer32"
_BtdsLCoPathFailureAction_Object = MibTableColumn
btdsLCoPathFailureAction = _BtdsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 22),
    _BtdsLCoPathFailureAction_Type()
)
btdsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoPathFailureAction.setStatus("mandatory")


class _BtdsLCoBumpPreference_Type(Integer32):
    """Custom type btdsLCoBumpPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_BtdsLCoBumpPreference_Type.__name__ = "Integer32"
_BtdsLCoBumpPreference_Object = MibTableColumn
btdsLCoBumpPreference = _BtdsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 23),
    _BtdsLCoBumpPreference_Type()
)
btdsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoBumpPreference.setStatus("mandatory")


class _BtdsLCoOptimization_Type(Integer32):
    """Custom type btdsLCoOptimization based on Integer32"""
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


_BtdsLCoOptimization_Type.__name__ = "Integer32"
_BtdsLCoOptimization_Object = MibTableColumn
btdsLCoOptimization = _BtdsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 24),
    _BtdsLCoOptimization_Type()
)
btdsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoOptimization.setStatus("mandatory")


class _BtdsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type btdsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_BtdsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_BtdsLCoPathUpDateTime_Object = MibTableColumn
btdsLCoPathUpDateTime = _BtdsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 10, 1, 25),
    _BtdsLCoPathUpDateTime_Type()
)
btdsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoPathUpDateTime.setStatus("mandatory")
_BtdsLCoStatsTable_Object = MibTable
btdsLCoStatsTable = _BtdsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 11)
)
if mibBuilder.loadTexts:
    btdsLCoStatsTable.setStatus("mandatory")
_BtdsLCoStatsEntry_Object = MibTableRow
btdsLCoStatsEntry = _BtdsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 11, 1)
)
btdsLCoStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsLCoIndex"),
)
if mibBuilder.loadTexts:
    btdsLCoStatsEntry.setStatus("mandatory")
_BtdsLCoPktsToNetwork_Type = PassportCounter64
_BtdsLCoPktsToNetwork_Object = MibTableColumn
btdsLCoPktsToNetwork = _BtdsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 11, 1, 1),
    _BtdsLCoPktsToNetwork_Type()
)
btdsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoPktsToNetwork.setStatus("mandatory")
_BtdsLCoBytesToNetwork_Type = PassportCounter64
_BtdsLCoBytesToNetwork_Object = MibTableColumn
btdsLCoBytesToNetwork = _BtdsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 11, 1, 2),
    _BtdsLCoBytesToNetwork_Type()
)
btdsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoBytesToNetwork.setStatus("mandatory")
_BtdsLCoPktsFromNetwork_Type = PassportCounter64
_BtdsLCoPktsFromNetwork_Object = MibTableColumn
btdsLCoPktsFromNetwork = _BtdsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 11, 1, 3),
    _BtdsLCoPktsFromNetwork_Type()
)
btdsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoPktsFromNetwork.setStatus("mandatory")
_BtdsLCoBytesFromNetwork_Type = PassportCounter64
_BtdsLCoBytesFromNetwork_Object = MibTableColumn
btdsLCoBytesFromNetwork = _BtdsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 11, 1, 4),
    _BtdsLCoBytesFromNetwork_Type()
)
btdsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoBytesFromNetwork.setStatus("mandatory")
_BtdsLCoPathTable_Object = MibTable
btdsLCoPathTable = _BtdsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 264)
)
if mibBuilder.loadTexts:
    btdsLCoPathTable.setStatus("mandatory")
_BtdsLCoPathEntry_Object = MibTableRow
btdsLCoPathEntry = _BtdsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 264, 1)
)
btdsLCoPathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsLCoIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsLCoPathValue"),
)
if mibBuilder.loadTexts:
    btdsLCoPathEntry.setStatus("mandatory")


class _BtdsLCoPathValue_Type(AsciiString):
    """Custom type btdsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BtdsLCoPathValue_Type.__name__ = "AsciiString"
_BtdsLCoPathValue_Object = MibTableColumn
btdsLCoPathValue = _BtdsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 4, 264, 1, 1),
    _BtdsLCoPathValue_Type()
)
btdsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsLCoPathValue.setStatus("mandatory")
_BtdsDpnss1_ObjectIdentity = ObjectIdentity
btdsDpnss1 = _BtdsDpnss1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5)
)
_BtdsDpnss1RowStatusTable_Object = MibTable
btdsDpnss1RowStatusTable = _BtdsDpnss1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 1)
)
if mibBuilder.loadTexts:
    btdsDpnss1RowStatusTable.setStatus("mandatory")
_BtdsDpnss1RowStatusEntry_Object = MibTableRow
btdsDpnss1RowStatusEntry = _BtdsDpnss1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 1, 1)
)
btdsDpnss1RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    btdsDpnss1RowStatusEntry.setStatus("mandatory")
_BtdsDpnss1RowStatus_Type = RowStatus
_BtdsDpnss1RowStatus_Object = MibTableColumn
btdsDpnss1RowStatus = _BtdsDpnss1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 1, 1, 1),
    _BtdsDpnss1RowStatus_Type()
)
btdsDpnss1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsDpnss1RowStatus.setStatus("mandatory")
_BtdsDpnss1ComponentName_Type = DisplayString
_BtdsDpnss1ComponentName_Object = MibTableColumn
btdsDpnss1ComponentName = _BtdsDpnss1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 1, 1, 2),
    _BtdsDpnss1ComponentName_Type()
)
btdsDpnss1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1ComponentName.setStatus("mandatory")
_BtdsDpnss1StorageType_Type = StorageType
_BtdsDpnss1StorageType_Object = MibTableColumn
btdsDpnss1StorageType = _BtdsDpnss1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 1, 1, 4),
    _BtdsDpnss1StorageType_Type()
)
btdsDpnss1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1StorageType.setStatus("mandatory")
_BtdsDpnss1Index_Type = NonReplicated
_BtdsDpnss1Index_Object = MibTableColumn
btdsDpnss1Index = _BtdsDpnss1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 1, 1, 10),
    _BtdsDpnss1Index_Type()
)
btdsDpnss1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btdsDpnss1Index.setStatus("mandatory")
_BtdsDpnss1ProvTable_Object = MibTable
btdsDpnss1ProvTable = _BtdsDpnss1ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 10)
)
if mibBuilder.loadTexts:
    btdsDpnss1ProvTable.setStatus("mandatory")
_BtdsDpnss1ProvEntry_Object = MibTableRow
btdsDpnss1ProvEntry = _BtdsDpnss1ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 10, 1)
)
btdsDpnss1ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    btdsDpnss1ProvEntry.setStatus("mandatory")


class _BtdsDpnss1TimeslotsX_Type(OctetString):
    """Custom type btdsDpnss1TimeslotsX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BtdsDpnss1TimeslotsX_Type.__name__ = "OctetString"
_BtdsDpnss1TimeslotsX_Object = MibTableColumn
btdsDpnss1TimeslotsX = _BtdsDpnss1TimeslotsX_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 10, 1, 1),
    _BtdsDpnss1TimeslotsX_Type()
)
btdsDpnss1TimeslotsX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsDpnss1TimeslotsX.setStatus("mandatory")
_BtdsDpnss1VdcdTable_Object = MibTable
btdsDpnss1VdcdTable = _BtdsDpnss1VdcdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 12)
)
if mibBuilder.loadTexts:
    btdsDpnss1VdcdTable.setStatus("mandatory")
_BtdsDpnss1VdcdEntry_Object = MibTableRow
btdsDpnss1VdcdEntry = _BtdsDpnss1VdcdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 12, 1)
)
btdsDpnss1VdcdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    btdsDpnss1VdcdEntry.setStatus("mandatory")
_BtdsDpnss1NewVoiceCalls_Type = Counter32
_BtdsDpnss1NewVoiceCalls_Object = MibTableColumn
btdsDpnss1NewVoiceCalls = _BtdsDpnss1NewVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 12, 1, 1),
    _BtdsDpnss1NewVoiceCalls_Type()
)
btdsDpnss1NewVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1NewVoiceCalls.setStatus("mandatory")
_BtdsDpnss1NewDataCalls_Type = Counter32
_BtdsDpnss1NewDataCalls_Object = MibTableColumn
btdsDpnss1NewDataCalls = _BtdsDpnss1NewDataCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 12, 1, 2),
    _BtdsDpnss1NewDataCalls_Type()
)
btdsDpnss1NewDataCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1NewDataCalls.setStatus("mandatory")
_BtdsDpnss1VoiceToData_Type = Counter32
_BtdsDpnss1VoiceToData_Object = MibTableColumn
btdsDpnss1VoiceToData = _BtdsDpnss1VoiceToData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 12, 1, 3),
    _BtdsDpnss1VoiceToData_Type()
)
btdsDpnss1VoiceToData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1VoiceToData.setStatus("mandatory")
_BtdsDpnss1DataToVoice_Type = Counter32
_BtdsDpnss1DataToVoice_Object = MibTableColumn
btdsDpnss1DataToVoice = _BtdsDpnss1DataToVoice_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 12, 1, 4),
    _BtdsDpnss1DataToVoice_Type()
)
btdsDpnss1DataToVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1DataToVoice.setStatus("mandatory")
_BtdsDpnss1CallClears_Type = Counter32
_BtdsDpnss1CallClears_Object = MibTableColumn
btdsDpnss1CallClears = _BtdsDpnss1CallClears_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 12, 1, 5),
    _BtdsDpnss1CallClears_Type()
)
btdsDpnss1CallClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1CallClears.setStatus("mandatory")
_BtdsDpnss1FramesTable_Object = MibTable
btdsDpnss1FramesTable = _BtdsDpnss1FramesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 13)
)
if mibBuilder.loadTexts:
    btdsDpnss1FramesTable.setStatus("mandatory")
_BtdsDpnss1FramesEntry_Object = MibTableRow
btdsDpnss1FramesEntry = _BtdsDpnss1FramesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 13, 1)
)
btdsDpnss1FramesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    btdsDpnss1FramesEntry.setStatus("mandatory")
_BtdsDpnss1FrmProcessed_Type = Counter32
_BtdsDpnss1FrmProcessed_Object = MibTableColumn
btdsDpnss1FrmProcessed = _BtdsDpnss1FrmProcessed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 13, 1, 1),
    _BtdsDpnss1FrmProcessed_Type()
)
btdsDpnss1FrmProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1FrmProcessed.setStatus("mandatory")
_BtdsDpnss1FrmInvalid_Type = Counter32
_BtdsDpnss1FrmInvalid_Object = MibTableColumn
btdsDpnss1FrmInvalid = _BtdsDpnss1FrmInvalid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 13, 1, 2),
    _BtdsDpnss1FrmInvalid_Type()
)
btdsDpnss1FrmInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1FrmInvalid.setStatus("mandatory")
_BtdsDpnss1HdlcTable_Object = MibTable
btdsDpnss1HdlcTable = _BtdsDpnss1HdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 14)
)
if mibBuilder.loadTexts:
    btdsDpnss1HdlcTable.setStatus("mandatory")
_BtdsDpnss1HdlcEntry_Object = MibTableRow
btdsDpnss1HdlcEntry = _BtdsDpnss1HdlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 14, 1)
)
btdsDpnss1HdlcEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    btdsDpnss1HdlcEntry.setStatus("mandatory")
_BtdsDpnss1FrmFromIf_Type = Counter32
_BtdsDpnss1FrmFromIf_Object = MibTableColumn
btdsDpnss1FrmFromIf = _BtdsDpnss1FrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 14, 1, 2),
    _BtdsDpnss1FrmFromIf_Type()
)
btdsDpnss1FrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1FrmFromIf.setStatus("mandatory")
_BtdsDpnss1Aborts_Type = Counter32
_BtdsDpnss1Aborts_Object = MibTableColumn
btdsDpnss1Aborts = _BtdsDpnss1Aborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 14, 1, 3),
    _BtdsDpnss1Aborts_Type()
)
btdsDpnss1Aborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1Aborts.setStatus("mandatory")
_BtdsDpnss1CrcErrors_Type = Counter32
_BtdsDpnss1CrcErrors_Object = MibTableColumn
btdsDpnss1CrcErrors = _BtdsDpnss1CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 14, 1, 4),
    _BtdsDpnss1CrcErrors_Type()
)
btdsDpnss1CrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1CrcErrors.setStatus("mandatory")
_BtdsDpnss1NonOctetErrors_Type = Counter32
_BtdsDpnss1NonOctetErrors_Object = MibTableColumn
btdsDpnss1NonOctetErrors = _BtdsDpnss1NonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 14, 1, 5),
    _BtdsDpnss1NonOctetErrors_Type()
)
btdsDpnss1NonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1NonOctetErrors.setStatus("mandatory")
_BtdsDpnss1Overruns_Type = Counter32
_BtdsDpnss1Overruns_Object = MibTableColumn
btdsDpnss1Overruns = _BtdsDpnss1Overruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 14, 1, 6),
    _BtdsDpnss1Overruns_Type()
)
btdsDpnss1Overruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1Overruns.setStatus("mandatory")
_BtdsDpnss1LargeFrmErrors_Type = Counter32
_BtdsDpnss1LargeFrmErrors_Object = MibTableColumn
btdsDpnss1LargeFrmErrors = _BtdsDpnss1LargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 14, 1, 8),
    _BtdsDpnss1LargeFrmErrors_Type()
)
btdsDpnss1LargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1LargeFrmErrors.setStatus("mandatory")
_BtdsDpnss1TSlotTable_Object = MibTable
btdsDpnss1TSlotTable = _BtdsDpnss1TSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 286)
)
if mibBuilder.loadTexts:
    btdsDpnss1TSlotTable.setStatus("mandatory")
_BtdsDpnss1TSlotEntry_Object = MibTableRow
btdsDpnss1TSlotEntry = _BtdsDpnss1TSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 286, 1)
)
btdsDpnss1TSlotEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsDpnss1Index"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsDpnss1TSlotIndex"),
)
if mibBuilder.loadTexts:
    btdsDpnss1TSlotEntry.setStatus("mandatory")


class _BtdsDpnss1TSlotIndex_Type(Integer32):
    """Custom type btdsDpnss1TSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_BtdsDpnss1TSlotIndex_Type.__name__ = "Integer32"
_BtdsDpnss1TSlotIndex_Object = MibTableColumn
btdsDpnss1TSlotIndex = _BtdsDpnss1TSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 286, 1, 1),
    _BtdsDpnss1TSlotIndex_Type()
)
btdsDpnss1TSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btdsDpnss1TSlotIndex.setStatus("mandatory")


class _BtdsDpnss1TSlotValue_Type(Integer32):
    """Custom type btdsDpnss1TSlotValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("idle", 0),
          ("voice", 1))
    )


_BtdsDpnss1TSlotValue_Type.__name__ = "Integer32"
_BtdsDpnss1TSlotValue_Object = MibTableColumn
btdsDpnss1TSlotValue = _BtdsDpnss1TSlotValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 5, 286, 1, 2),
    _BtdsDpnss1TSlotValue_Type()
)
btdsDpnss1TSlotValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsDpnss1TSlotValue.setStatus("mandatory")
_BtdsMcdn_ObjectIdentity = ObjectIdentity
btdsMcdn = _BtdsMcdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6)
)
_BtdsMcdnRowStatusTable_Object = MibTable
btdsMcdnRowStatusTable = _BtdsMcdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 1)
)
if mibBuilder.loadTexts:
    btdsMcdnRowStatusTable.setStatus("mandatory")
_BtdsMcdnRowStatusEntry_Object = MibTableRow
btdsMcdnRowStatusEntry = _BtdsMcdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 1, 1)
)
btdsMcdnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    btdsMcdnRowStatusEntry.setStatus("mandatory")
_BtdsMcdnRowStatus_Type = RowStatus
_BtdsMcdnRowStatus_Object = MibTableColumn
btdsMcdnRowStatus = _BtdsMcdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 1, 1, 1),
    _BtdsMcdnRowStatus_Type()
)
btdsMcdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsMcdnRowStatus.setStatus("mandatory")
_BtdsMcdnComponentName_Type = DisplayString
_BtdsMcdnComponentName_Object = MibTableColumn
btdsMcdnComponentName = _BtdsMcdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 1, 1, 2),
    _BtdsMcdnComponentName_Type()
)
btdsMcdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnComponentName.setStatus("mandatory")
_BtdsMcdnStorageType_Type = StorageType
_BtdsMcdnStorageType_Object = MibTableColumn
btdsMcdnStorageType = _BtdsMcdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 1, 1, 4),
    _BtdsMcdnStorageType_Type()
)
btdsMcdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnStorageType.setStatus("mandatory")
_BtdsMcdnIndex_Type = NonReplicated
_BtdsMcdnIndex_Object = MibTableColumn
btdsMcdnIndex = _BtdsMcdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 1, 1, 10),
    _BtdsMcdnIndex_Type()
)
btdsMcdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btdsMcdnIndex.setStatus("mandatory")
_BtdsMcdnProvTable_Object = MibTable
btdsMcdnProvTable = _BtdsMcdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 10)
)
if mibBuilder.loadTexts:
    btdsMcdnProvTable.setStatus("mandatory")
_BtdsMcdnProvEntry_Object = MibTableRow
btdsMcdnProvEntry = _BtdsMcdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 10, 1)
)
btdsMcdnProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    btdsMcdnProvEntry.setStatus("mandatory")


class _BtdsMcdnAdjPbxSide_Type(Integer32):
    """Custom type btdsMcdnAdjPbxSide based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 0))
    )


_BtdsMcdnAdjPbxSide_Type.__name__ = "Integer32"
_BtdsMcdnAdjPbxSide_Object = MibTableColumn
btdsMcdnAdjPbxSide = _BtdsMcdnAdjPbxSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 10, 1, 1),
    _BtdsMcdnAdjPbxSide_Type()
)
btdsMcdnAdjPbxSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsMcdnAdjPbxSide.setStatus("mandatory")
_BtdsMcdnVdcdTable_Object = MibTable
btdsMcdnVdcdTable = _BtdsMcdnVdcdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 12)
)
if mibBuilder.loadTexts:
    btdsMcdnVdcdTable.setStatus("mandatory")
_BtdsMcdnVdcdEntry_Object = MibTableRow
btdsMcdnVdcdEntry = _BtdsMcdnVdcdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 12, 1)
)
btdsMcdnVdcdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    btdsMcdnVdcdEntry.setStatus("mandatory")
_BtdsMcdnNewVoiceCalls_Type = Counter32
_BtdsMcdnNewVoiceCalls_Object = MibTableColumn
btdsMcdnNewVoiceCalls = _BtdsMcdnNewVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 12, 1, 1),
    _BtdsMcdnNewVoiceCalls_Type()
)
btdsMcdnNewVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnNewVoiceCalls.setStatus("mandatory")
_BtdsMcdnNewDataCalls_Type = Counter32
_BtdsMcdnNewDataCalls_Object = MibTableColumn
btdsMcdnNewDataCalls = _BtdsMcdnNewDataCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 12, 1, 2),
    _BtdsMcdnNewDataCalls_Type()
)
btdsMcdnNewDataCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnNewDataCalls.setStatus("mandatory")
_BtdsMcdnVoiceToData_Type = Counter32
_BtdsMcdnVoiceToData_Object = MibTableColumn
btdsMcdnVoiceToData = _BtdsMcdnVoiceToData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 12, 1, 3),
    _BtdsMcdnVoiceToData_Type()
)
btdsMcdnVoiceToData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnVoiceToData.setStatus("mandatory")
_BtdsMcdnDataToVoice_Type = Counter32
_BtdsMcdnDataToVoice_Object = MibTableColumn
btdsMcdnDataToVoice = _BtdsMcdnDataToVoice_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 12, 1, 4),
    _BtdsMcdnDataToVoice_Type()
)
btdsMcdnDataToVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnDataToVoice.setStatus("mandatory")
_BtdsMcdnCallClears_Type = Counter32
_BtdsMcdnCallClears_Object = MibTableColumn
btdsMcdnCallClears = _BtdsMcdnCallClears_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 12, 1, 5),
    _BtdsMcdnCallClears_Type()
)
btdsMcdnCallClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnCallClears.setStatus("mandatory")
_BtdsMcdnFramesTable_Object = MibTable
btdsMcdnFramesTable = _BtdsMcdnFramesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 13)
)
if mibBuilder.loadTexts:
    btdsMcdnFramesTable.setStatus("mandatory")
_BtdsMcdnFramesEntry_Object = MibTableRow
btdsMcdnFramesEntry = _BtdsMcdnFramesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 13, 1)
)
btdsMcdnFramesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    btdsMcdnFramesEntry.setStatus("mandatory")
_BtdsMcdnFrmProcessed_Type = Counter32
_BtdsMcdnFrmProcessed_Object = MibTableColumn
btdsMcdnFrmProcessed = _BtdsMcdnFrmProcessed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 13, 1, 1),
    _BtdsMcdnFrmProcessed_Type()
)
btdsMcdnFrmProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnFrmProcessed.setStatus("mandatory")
_BtdsMcdnFrmInvalid_Type = Counter32
_BtdsMcdnFrmInvalid_Object = MibTableColumn
btdsMcdnFrmInvalid = _BtdsMcdnFrmInvalid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 13, 1, 2),
    _BtdsMcdnFrmInvalid_Type()
)
btdsMcdnFrmInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnFrmInvalid.setStatus("mandatory")
_BtdsMcdnHdlcTable_Object = MibTable
btdsMcdnHdlcTable = _BtdsMcdnHdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 14)
)
if mibBuilder.loadTexts:
    btdsMcdnHdlcTable.setStatus("mandatory")
_BtdsMcdnHdlcEntry_Object = MibTableRow
btdsMcdnHdlcEntry = _BtdsMcdnHdlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 14, 1)
)
btdsMcdnHdlcEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    btdsMcdnHdlcEntry.setStatus("mandatory")
_BtdsMcdnFrmFromIf_Type = Counter32
_BtdsMcdnFrmFromIf_Object = MibTableColumn
btdsMcdnFrmFromIf = _BtdsMcdnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 14, 1, 2),
    _BtdsMcdnFrmFromIf_Type()
)
btdsMcdnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnFrmFromIf.setStatus("mandatory")
_BtdsMcdnAborts_Type = Counter32
_BtdsMcdnAborts_Object = MibTableColumn
btdsMcdnAborts = _BtdsMcdnAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 14, 1, 3),
    _BtdsMcdnAborts_Type()
)
btdsMcdnAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnAborts.setStatus("mandatory")
_BtdsMcdnCrcErrors_Type = Counter32
_BtdsMcdnCrcErrors_Object = MibTableColumn
btdsMcdnCrcErrors = _BtdsMcdnCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 14, 1, 4),
    _BtdsMcdnCrcErrors_Type()
)
btdsMcdnCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnCrcErrors.setStatus("mandatory")
_BtdsMcdnNonOctetErrors_Type = Counter32
_BtdsMcdnNonOctetErrors_Object = MibTableColumn
btdsMcdnNonOctetErrors = _BtdsMcdnNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 14, 1, 5),
    _BtdsMcdnNonOctetErrors_Type()
)
btdsMcdnNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnNonOctetErrors.setStatus("mandatory")
_BtdsMcdnOverruns_Type = Counter32
_BtdsMcdnOverruns_Object = MibTableColumn
btdsMcdnOverruns = _BtdsMcdnOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 14, 1, 6),
    _BtdsMcdnOverruns_Type()
)
btdsMcdnOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnOverruns.setStatus("mandatory")
_BtdsMcdnLargeFrmErrors_Type = Counter32
_BtdsMcdnLargeFrmErrors_Object = MibTableColumn
btdsMcdnLargeFrmErrors = _BtdsMcdnLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 14, 1, 8),
    _BtdsMcdnLargeFrmErrors_Type()
)
btdsMcdnLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnLargeFrmErrors.setStatus("mandatory")
_BtdsMcdnTSlotTable_Object = MibTable
btdsMcdnTSlotTable = _BtdsMcdnTSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 286)
)
if mibBuilder.loadTexts:
    btdsMcdnTSlotTable.setStatus("mandatory")
_BtdsMcdnTSlotEntry_Object = MibTableRow
btdsMcdnTSlotEntry = _BtdsMcdnTSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 286, 1)
)
btdsMcdnTSlotEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsMcdnIndex"),
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsMcdnTSlotIndex"),
)
if mibBuilder.loadTexts:
    btdsMcdnTSlotEntry.setStatus("mandatory")


class _BtdsMcdnTSlotIndex_Type(Integer32):
    """Custom type btdsMcdnTSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_BtdsMcdnTSlotIndex_Type.__name__ = "Integer32"
_BtdsMcdnTSlotIndex_Object = MibTableColumn
btdsMcdnTSlotIndex = _BtdsMcdnTSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 286, 1, 1),
    _BtdsMcdnTSlotIndex_Type()
)
btdsMcdnTSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    btdsMcdnTSlotIndex.setStatus("mandatory")


class _BtdsMcdnTSlotValue_Type(Integer32):
    """Custom type btdsMcdnTSlotValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("idle", 0),
          ("voice", 1))
    )


_BtdsMcdnTSlotValue_Type.__name__ = "Integer32"
_BtdsMcdnTSlotValue_Object = MibTableColumn
btdsMcdnTSlotValue = _BtdsMcdnTSlotValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 6, 286, 1, 2),
    _BtdsMcdnTSlotValue_Type()
)
btdsMcdnTSlotValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsMcdnTSlotValue.setStatus("mandatory")
_BtdsCidDataTable_Object = MibTable
btdsCidDataTable = _BtdsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 100)
)
if mibBuilder.loadTexts:
    btdsCidDataTable.setStatus("mandatory")
_BtdsCidDataEntry_Object = MibTableRow
btdsCidDataEntry = _BtdsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 100, 1)
)
btdsCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
)
if mibBuilder.loadTexts:
    btdsCidDataEntry.setStatus("mandatory")


class _BtdsCustomerIdentifier_Type(Unsigned32):
    """Custom type btdsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_BtdsCustomerIdentifier_Type.__name__ = "Unsigned32"
_BtdsCustomerIdentifier_Object = MibTableColumn
btdsCustomerIdentifier = _BtdsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 100, 1, 1),
    _BtdsCustomerIdentifier_Type()
)
btdsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsCustomerIdentifier.setStatus("mandatory")
_BtdsIfEntryTable_Object = MibTable
btdsIfEntryTable = _BtdsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 101)
)
if mibBuilder.loadTexts:
    btdsIfEntryTable.setStatus("mandatory")
_BtdsIfEntryEntry_Object = MibTableRow
btdsIfEntryEntry = _BtdsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 101, 1)
)
btdsIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
)
if mibBuilder.loadTexts:
    btdsIfEntryEntry.setStatus("mandatory")


class _BtdsIfAdminStatus_Type(Integer32):
    """Custom type btdsIfAdminStatus based on Integer32"""
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


_BtdsIfAdminStatus_Type.__name__ = "Integer32"
_BtdsIfAdminStatus_Object = MibTableColumn
btdsIfAdminStatus = _BtdsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 101, 1, 1),
    _BtdsIfAdminStatus_Type()
)
btdsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btdsIfAdminStatus.setStatus("mandatory")


class _BtdsIfIndex_Type(InterfaceIndex):
    """Custom type btdsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BtdsIfIndex_Type.__name__ = "InterfaceIndex"
_BtdsIfIndex_Object = MibTableColumn
btdsIfIndex = _BtdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 101, 1, 2),
    _BtdsIfIndex_Type()
)
btdsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsIfIndex.setStatus("mandatory")
_BtdsOperStatusTable_Object = MibTable
btdsOperStatusTable = _BtdsOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 102)
)
if mibBuilder.loadTexts:
    btdsOperStatusTable.setStatus("mandatory")
_BtdsOperStatusEntry_Object = MibTableRow
btdsOperStatusEntry = _BtdsOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 102, 1)
)
btdsOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
)
if mibBuilder.loadTexts:
    btdsOperStatusEntry.setStatus("mandatory")


class _BtdsSnmpOperStatus_Type(Integer32):
    """Custom type btdsSnmpOperStatus based on Integer32"""
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


_BtdsSnmpOperStatus_Type.__name__ = "Integer32"
_BtdsSnmpOperStatus_Object = MibTableColumn
btdsSnmpOperStatus = _BtdsSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 102, 1, 1),
    _BtdsSnmpOperStatus_Type()
)
btdsSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsSnmpOperStatus.setStatus("mandatory")
_BtdsStateTable_Object = MibTable
btdsStateTable = _BtdsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103)
)
if mibBuilder.loadTexts:
    btdsStateTable.setStatus("mandatory")
_BtdsStateEntry_Object = MibTableRow
btdsStateEntry = _BtdsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1)
)
btdsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
)
if mibBuilder.loadTexts:
    btdsStateEntry.setStatus("mandatory")


class _BtdsAdminState_Type(Integer32):
    """Custom type btdsAdminState based on Integer32"""
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


_BtdsAdminState_Type.__name__ = "Integer32"
_BtdsAdminState_Object = MibTableColumn
btdsAdminState = _BtdsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1, 1),
    _BtdsAdminState_Type()
)
btdsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsAdminState.setStatus("mandatory")


class _BtdsOperationalState_Type(Integer32):
    """Custom type btdsOperationalState based on Integer32"""
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


_BtdsOperationalState_Type.__name__ = "Integer32"
_BtdsOperationalState_Object = MibTableColumn
btdsOperationalState = _BtdsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1, 2),
    _BtdsOperationalState_Type()
)
btdsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsOperationalState.setStatus("mandatory")


class _BtdsUsageState_Type(Integer32):
    """Custom type btdsUsageState based on Integer32"""
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


_BtdsUsageState_Type.__name__ = "Integer32"
_BtdsUsageState_Object = MibTableColumn
btdsUsageState = _BtdsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1, 3),
    _BtdsUsageState_Type()
)
btdsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsUsageState.setStatus("mandatory")


class _BtdsAvailabilityStatus_Type(OctetString):
    """Custom type btdsAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BtdsAvailabilityStatus_Type.__name__ = "OctetString"
_BtdsAvailabilityStatus_Object = MibTableColumn
btdsAvailabilityStatus = _BtdsAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1, 4),
    _BtdsAvailabilityStatus_Type()
)
btdsAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsAvailabilityStatus.setStatus("mandatory")


class _BtdsProceduralStatus_Type(OctetString):
    """Custom type btdsProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BtdsProceduralStatus_Type.__name__ = "OctetString"
_BtdsProceduralStatus_Object = MibTableColumn
btdsProceduralStatus = _BtdsProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1, 5),
    _BtdsProceduralStatus_Type()
)
btdsProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsProceduralStatus.setStatus("mandatory")


class _BtdsControlStatus_Type(OctetString):
    """Custom type btdsControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BtdsControlStatus_Type.__name__ = "OctetString"
_BtdsControlStatus_Object = MibTableColumn
btdsControlStatus = _BtdsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1, 6),
    _BtdsControlStatus_Type()
)
btdsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsControlStatus.setStatus("mandatory")


class _BtdsAlarmStatus_Type(OctetString):
    """Custom type btdsAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BtdsAlarmStatus_Type.__name__ = "OctetString"
_BtdsAlarmStatus_Object = MibTableColumn
btdsAlarmStatus = _BtdsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1, 7),
    _BtdsAlarmStatus_Type()
)
btdsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsAlarmStatus.setStatus("mandatory")


class _BtdsStandbyStatus_Type(Integer32):
    """Custom type btdsStandbyStatus based on Integer32"""
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


_BtdsStandbyStatus_Type.__name__ = "Integer32"
_BtdsStandbyStatus_Object = MibTableColumn
btdsStandbyStatus = _BtdsStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1, 8),
    _BtdsStandbyStatus_Type()
)
btdsStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsStandbyStatus.setStatus("mandatory")


class _BtdsUnknownStatus_Type(Integer32):
    """Custom type btdsUnknownStatus based on Integer32"""
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


_BtdsUnknownStatus_Type.__name__ = "Integer32"
_BtdsUnknownStatus_Object = MibTableColumn
btdsUnknownStatus = _BtdsUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 103, 1, 9),
    _BtdsUnknownStatus_Type()
)
btdsUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsUnknownStatus.setStatus("mandatory")
_BtdsOperationalTable_Object = MibTable
btdsOperationalTable = _BtdsOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 105)
)
if mibBuilder.loadTexts:
    btdsOperationalTable.setStatus("mandatory")
_BtdsOperationalEntry_Object = MibTableRow
btdsOperationalEntry = _BtdsOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 105, 1)
)
btdsOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-BitTransparentMIB", "btdsIndex"),
)
if mibBuilder.loadTexts:
    btdsOperationalEntry.setStatus("mandatory")


class _BtdsServiceFailureReason_Type(OctetString):
    """Custom type btdsServiceFailureReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BtdsServiceFailureReason_Type.__name__ = "OctetString"
_BtdsServiceFailureReason_Object = MibTableColumn
btdsServiceFailureReason = _BtdsServiceFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 81, 105, 1, 1),
    _BtdsServiceFailureReason_Type()
)
btdsServiceFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btdsServiceFailureReason.setStatus("mandatory")
_BitTransparentMIB_ObjectIdentity = ObjectIdentity
bitTransparentMIB = _BitTransparentMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 46)
)
_BitTransparentGroup_ObjectIdentity = ObjectIdentity
bitTransparentGroup = _BitTransparentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 46, 1)
)
_BitTransparentGroupBE_ObjectIdentity = ObjectIdentity
bitTransparentGroupBE = _BitTransparentGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 46, 1, 5)
)
_BitTransparentGroupBE01_ObjectIdentity = ObjectIdentity
bitTransparentGroupBE01 = _BitTransparentGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 46, 1, 5, 2)
)
_BitTransparentGroupBE01A_ObjectIdentity = ObjectIdentity
bitTransparentGroupBE01A = _BitTransparentGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 46, 1, 5, 2, 2)
)
_BitTransparentCapabilities_ObjectIdentity = ObjectIdentity
bitTransparentCapabilities = _BitTransparentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 46, 3)
)
_BitTransparentCapabilitiesBE_ObjectIdentity = ObjectIdentity
bitTransparentCapabilitiesBE = _BitTransparentCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 46, 3, 5)
)
_BitTransparentCapabilitiesBE01_ObjectIdentity = ObjectIdentity
bitTransparentCapabilitiesBE01 = _BitTransparentCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 46, 3, 5, 2)
)
_BitTransparentCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
bitTransparentCapabilitiesBE01A = _BitTransparentCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 46, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-BitTransparentMIB",
    **{"btds": btds,
       "btdsRowStatusTable": btdsRowStatusTable,
       "btdsRowStatusEntry": btdsRowStatusEntry,
       "btdsRowStatus": btdsRowStatus,
       "btdsComponentName": btdsComponentName,
       "btdsStorageType": btdsStorageType,
       "btdsIndex": btdsIndex,
       "btdsFramer": btdsFramer,
       "btdsFramerRowStatusTable": btdsFramerRowStatusTable,
       "btdsFramerRowStatusEntry": btdsFramerRowStatusEntry,
       "btdsFramerRowStatus": btdsFramerRowStatus,
       "btdsFramerComponentName": btdsFramerComponentName,
       "btdsFramerStorageType": btdsFramerStorageType,
       "btdsFramerIndex": btdsFramerIndex,
       "btdsFramerProvTable": btdsFramerProvTable,
       "btdsFramerProvEntry": btdsFramerProvEntry,
       "btdsFramerInterfaceName": btdsFramerInterfaceName,
       "btdsFramerChannelTable": btdsFramerChannelTable,
       "btdsFramerChannelEntry": btdsFramerChannelEntry,
       "btdsFramerProtocol": btdsFramerProtocol,
       "btdsFramerNumOfIdleBytesToMonitor": btdsFramerNumOfIdleBytesToMonitor,
       "btdsFramerIdlePattern": btdsFramerIdlePattern,
       "btdsFramerTimeSlotAlignment": btdsFramerTimeSlotAlignment,
       "btdsFramerInsertedOutputDelay": btdsFramerInsertedOutputDelay,
       "btdsFramerBtdsCellSize": btdsFramerBtdsCellSize,
       "btdsFramerStateTable": btdsFramerStateTable,
       "btdsFramerStateEntry": btdsFramerStateEntry,
       "btdsFramerAdminState": btdsFramerAdminState,
       "btdsFramerOperationalState": btdsFramerOperationalState,
       "btdsFramerUsageState": btdsFramerUsageState,
       "btdsFramerStatsTable": btdsFramerStatsTable,
       "btdsFramerStatsEntry": btdsFramerStatsEntry,
       "btdsFramerFrmFromIf": btdsFramerFrmFromIf,
       "btdsFramerSuppressedFrames": btdsFramerSuppressedFrames,
       "btdsFramerFrmToIf": btdsFramerFrmToIf,
       "btdsFramerLrcErrors": btdsFramerLrcErrors,
       "btdsFramerFrmLostInNetwork": btdsFramerFrmLostInNetwork,
       "btdsFramerFrmUnderRuns": btdsFramerFrmUnderRuns,
       "btdsFramerFrmDumped": btdsFramerFrmDumped,
       "btdsPlc": btdsPlc,
       "btdsPlcRowStatusTable": btdsPlcRowStatusTable,
       "btdsPlcRowStatusEntry": btdsPlcRowStatusEntry,
       "btdsPlcRowStatus": btdsPlcRowStatus,
       "btdsPlcComponentName": btdsPlcComponentName,
       "btdsPlcStorageType": btdsPlcStorageType,
       "btdsPlcIndex": btdsPlcIndex,
       "btdsPlcProvTable": btdsPlcProvTable,
       "btdsPlcProvEntry": btdsPlcProvEntry,
       "btdsPlcRemoteName": btdsPlcRemoteName,
       "btdsPlcSetupPriority": btdsPlcSetupPriority,
       "btdsPlcHoldingPriority": btdsPlcHoldingPriority,
       "btdsPlcRequiredTxBandwidth": btdsPlcRequiredTxBandwidth,
       "btdsPlcRequiredRxBandwidth": btdsPlcRequiredRxBandwidth,
       "btdsPlcRequiredTrafficType": btdsPlcRequiredTrafficType,
       "btdsPlcPermittedTrunkTypes": btdsPlcPermittedTrunkTypes,
       "btdsPlcRequiredSecurity": btdsPlcRequiredSecurity,
       "btdsPlcRequiredCustomerParm": btdsPlcRequiredCustomerParm,
       "btdsPlcPathAttributeToMinimize": btdsPlcPathAttributeToMinimize,
       "btdsPlcMaximumAcceptableCost": btdsPlcMaximumAcceptableCost,
       "btdsPlcMaximumAcceptableDelay": btdsPlcMaximumAcceptableDelay,
       "btdsPlcEmissionPriority": btdsPlcEmissionPriority,
       "btdsPlcDiscardPriority": btdsPlcDiscardPriority,
       "btdsPlcPathType": btdsPlcPathType,
       "btdsPlcPathFailureAction": btdsPlcPathFailureAction,
       "btdsPlcBumpPreference": btdsPlcBumpPreference,
       "btdsPlcOptimization": btdsPlcOptimization,
       "btdsPlcMpathTable": btdsPlcMpathTable,
       "btdsPlcMpathEntry": btdsPlcMpathEntry,
       "btdsPlcMpathIndex": btdsPlcMpathIndex,
       "btdsPlcMpathValue": btdsPlcMpathValue,
       "btdsLCo": btdsLCo,
       "btdsLCoRowStatusTable": btdsLCoRowStatusTable,
       "btdsLCoRowStatusEntry": btdsLCoRowStatusEntry,
       "btdsLCoRowStatus": btdsLCoRowStatus,
       "btdsLCoComponentName": btdsLCoComponentName,
       "btdsLCoStorageType": btdsLCoStorageType,
       "btdsLCoIndex": btdsLCoIndex,
       "btdsLCoPathDataTable": btdsLCoPathDataTable,
       "btdsLCoPathDataEntry": btdsLCoPathDataEntry,
       "btdsLCoState": btdsLCoState,
       "btdsLCoOverrideRemoteName": btdsLCoOverrideRemoteName,
       "btdsLCoEnd": btdsLCoEnd,
       "btdsLCoCostMetric": btdsLCoCostMetric,
       "btdsLCoDelayMetric": btdsLCoDelayMetric,
       "btdsLCoRoundTripDelay": btdsLCoRoundTripDelay,
       "btdsLCoSetupPriority": btdsLCoSetupPriority,
       "btdsLCoHoldingPriority": btdsLCoHoldingPriority,
       "btdsLCoRequiredTxBandwidth": btdsLCoRequiredTxBandwidth,
       "btdsLCoRequiredRxBandwidth": btdsLCoRequiredRxBandwidth,
       "btdsLCoRequiredTrafficType": btdsLCoRequiredTrafficType,
       "btdsLCoPermittedTrunkTypes": btdsLCoPermittedTrunkTypes,
       "btdsLCoRequiredSecurity": btdsLCoRequiredSecurity,
       "btdsLCoRequiredCustomerParameter": btdsLCoRequiredCustomerParameter,
       "btdsLCoEmissionPriority": btdsLCoEmissionPriority,
       "btdsLCoDiscardPriority": btdsLCoDiscardPriority,
       "btdsLCoPathType": btdsLCoPathType,
       "btdsLCoRetryCount": btdsLCoRetryCount,
       "btdsLCoPathFailureCount": btdsLCoPathFailureCount,
       "btdsLCoReasonForNoRoute": btdsLCoReasonForNoRoute,
       "btdsLCoLastTearDownReason": btdsLCoLastTearDownReason,
       "btdsLCoPathFailureAction": btdsLCoPathFailureAction,
       "btdsLCoBumpPreference": btdsLCoBumpPreference,
       "btdsLCoOptimization": btdsLCoOptimization,
       "btdsLCoPathUpDateTime": btdsLCoPathUpDateTime,
       "btdsLCoStatsTable": btdsLCoStatsTable,
       "btdsLCoStatsEntry": btdsLCoStatsEntry,
       "btdsLCoPktsToNetwork": btdsLCoPktsToNetwork,
       "btdsLCoBytesToNetwork": btdsLCoBytesToNetwork,
       "btdsLCoPktsFromNetwork": btdsLCoPktsFromNetwork,
       "btdsLCoBytesFromNetwork": btdsLCoBytesFromNetwork,
       "btdsLCoPathTable": btdsLCoPathTable,
       "btdsLCoPathEntry": btdsLCoPathEntry,
       "btdsLCoPathValue": btdsLCoPathValue,
       "btdsDpnss1": btdsDpnss1,
       "btdsDpnss1RowStatusTable": btdsDpnss1RowStatusTable,
       "btdsDpnss1RowStatusEntry": btdsDpnss1RowStatusEntry,
       "btdsDpnss1RowStatus": btdsDpnss1RowStatus,
       "btdsDpnss1ComponentName": btdsDpnss1ComponentName,
       "btdsDpnss1StorageType": btdsDpnss1StorageType,
       "btdsDpnss1Index": btdsDpnss1Index,
       "btdsDpnss1ProvTable": btdsDpnss1ProvTable,
       "btdsDpnss1ProvEntry": btdsDpnss1ProvEntry,
       "btdsDpnss1TimeslotsX": btdsDpnss1TimeslotsX,
       "btdsDpnss1VdcdTable": btdsDpnss1VdcdTable,
       "btdsDpnss1VdcdEntry": btdsDpnss1VdcdEntry,
       "btdsDpnss1NewVoiceCalls": btdsDpnss1NewVoiceCalls,
       "btdsDpnss1NewDataCalls": btdsDpnss1NewDataCalls,
       "btdsDpnss1VoiceToData": btdsDpnss1VoiceToData,
       "btdsDpnss1DataToVoice": btdsDpnss1DataToVoice,
       "btdsDpnss1CallClears": btdsDpnss1CallClears,
       "btdsDpnss1FramesTable": btdsDpnss1FramesTable,
       "btdsDpnss1FramesEntry": btdsDpnss1FramesEntry,
       "btdsDpnss1FrmProcessed": btdsDpnss1FrmProcessed,
       "btdsDpnss1FrmInvalid": btdsDpnss1FrmInvalid,
       "btdsDpnss1HdlcTable": btdsDpnss1HdlcTable,
       "btdsDpnss1HdlcEntry": btdsDpnss1HdlcEntry,
       "btdsDpnss1FrmFromIf": btdsDpnss1FrmFromIf,
       "btdsDpnss1Aborts": btdsDpnss1Aborts,
       "btdsDpnss1CrcErrors": btdsDpnss1CrcErrors,
       "btdsDpnss1NonOctetErrors": btdsDpnss1NonOctetErrors,
       "btdsDpnss1Overruns": btdsDpnss1Overruns,
       "btdsDpnss1LargeFrmErrors": btdsDpnss1LargeFrmErrors,
       "btdsDpnss1TSlotTable": btdsDpnss1TSlotTable,
       "btdsDpnss1TSlotEntry": btdsDpnss1TSlotEntry,
       "btdsDpnss1TSlotIndex": btdsDpnss1TSlotIndex,
       "btdsDpnss1TSlotValue": btdsDpnss1TSlotValue,
       "btdsMcdn": btdsMcdn,
       "btdsMcdnRowStatusTable": btdsMcdnRowStatusTable,
       "btdsMcdnRowStatusEntry": btdsMcdnRowStatusEntry,
       "btdsMcdnRowStatus": btdsMcdnRowStatus,
       "btdsMcdnComponentName": btdsMcdnComponentName,
       "btdsMcdnStorageType": btdsMcdnStorageType,
       "btdsMcdnIndex": btdsMcdnIndex,
       "btdsMcdnProvTable": btdsMcdnProvTable,
       "btdsMcdnProvEntry": btdsMcdnProvEntry,
       "btdsMcdnAdjPbxSide": btdsMcdnAdjPbxSide,
       "btdsMcdnVdcdTable": btdsMcdnVdcdTable,
       "btdsMcdnVdcdEntry": btdsMcdnVdcdEntry,
       "btdsMcdnNewVoiceCalls": btdsMcdnNewVoiceCalls,
       "btdsMcdnNewDataCalls": btdsMcdnNewDataCalls,
       "btdsMcdnVoiceToData": btdsMcdnVoiceToData,
       "btdsMcdnDataToVoice": btdsMcdnDataToVoice,
       "btdsMcdnCallClears": btdsMcdnCallClears,
       "btdsMcdnFramesTable": btdsMcdnFramesTable,
       "btdsMcdnFramesEntry": btdsMcdnFramesEntry,
       "btdsMcdnFrmProcessed": btdsMcdnFrmProcessed,
       "btdsMcdnFrmInvalid": btdsMcdnFrmInvalid,
       "btdsMcdnHdlcTable": btdsMcdnHdlcTable,
       "btdsMcdnHdlcEntry": btdsMcdnHdlcEntry,
       "btdsMcdnFrmFromIf": btdsMcdnFrmFromIf,
       "btdsMcdnAborts": btdsMcdnAborts,
       "btdsMcdnCrcErrors": btdsMcdnCrcErrors,
       "btdsMcdnNonOctetErrors": btdsMcdnNonOctetErrors,
       "btdsMcdnOverruns": btdsMcdnOverruns,
       "btdsMcdnLargeFrmErrors": btdsMcdnLargeFrmErrors,
       "btdsMcdnTSlotTable": btdsMcdnTSlotTable,
       "btdsMcdnTSlotEntry": btdsMcdnTSlotEntry,
       "btdsMcdnTSlotIndex": btdsMcdnTSlotIndex,
       "btdsMcdnTSlotValue": btdsMcdnTSlotValue,
       "btdsCidDataTable": btdsCidDataTable,
       "btdsCidDataEntry": btdsCidDataEntry,
       "btdsCustomerIdentifier": btdsCustomerIdentifier,
       "btdsIfEntryTable": btdsIfEntryTable,
       "btdsIfEntryEntry": btdsIfEntryEntry,
       "btdsIfAdminStatus": btdsIfAdminStatus,
       "btdsIfIndex": btdsIfIndex,
       "btdsOperStatusTable": btdsOperStatusTable,
       "btdsOperStatusEntry": btdsOperStatusEntry,
       "btdsSnmpOperStatus": btdsSnmpOperStatus,
       "btdsStateTable": btdsStateTable,
       "btdsStateEntry": btdsStateEntry,
       "btdsAdminState": btdsAdminState,
       "btdsOperationalState": btdsOperationalState,
       "btdsUsageState": btdsUsageState,
       "btdsAvailabilityStatus": btdsAvailabilityStatus,
       "btdsProceduralStatus": btdsProceduralStatus,
       "btdsControlStatus": btdsControlStatus,
       "btdsAlarmStatus": btdsAlarmStatus,
       "btdsStandbyStatus": btdsStandbyStatus,
       "btdsUnknownStatus": btdsUnknownStatus,
       "btdsOperationalTable": btdsOperationalTable,
       "btdsOperationalEntry": btdsOperationalEntry,
       "btdsServiceFailureReason": btdsServiceFailureReason,
       "bitTransparentMIB": bitTransparentMIB,
       "bitTransparentGroup": bitTransparentGroup,
       "bitTransparentGroupBE": bitTransparentGroupBE,
       "bitTransparentGroupBE01": bitTransparentGroupBE01,
       "bitTransparentGroupBE01A": bitTransparentGroupBE01A,
       "bitTransparentCapabilities": bitTransparentCapabilities,
       "bitTransparentCapabilitiesBE": bitTransparentCapabilitiesBE,
       "bitTransparentCapabilitiesBE01": bitTransparentCapabilitiesBE01,
       "bitTransparentCapabilitiesBE01A": bitTransparentCapabilitiesBE01A}
)
