# SNMP MIB module (Nortel-MsCarrier-MscPassport-BitTransparentMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-BitTransparentMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:01 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 Hex,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "Hex",
    "Link",
    "NonReplicated",
    "PassportCounter64")

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

_MscBtds_ObjectIdentity = ObjectIdentity
mscBtds = _MscBtds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81)
)
_MscBtdsRowStatusTable_Object = MibTable
mscBtdsRowStatusTable = _MscBtdsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 1)
)
if mibBuilder.loadTexts:
    mscBtdsRowStatusTable.setStatus("mandatory")
_MscBtdsRowStatusEntry_Object = MibTableRow
mscBtdsRowStatusEntry = _MscBtdsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 1, 1)
)
mscBtdsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsRowStatusEntry.setStatus("mandatory")
_MscBtdsRowStatus_Type = RowStatus
_MscBtdsRowStatus_Object = MibTableColumn
mscBtdsRowStatus = _MscBtdsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 1, 1, 1),
    _MscBtdsRowStatus_Type()
)
mscBtdsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsRowStatus.setStatus("mandatory")
_MscBtdsComponentName_Type = DisplayString
_MscBtdsComponentName_Object = MibTableColumn
mscBtdsComponentName = _MscBtdsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 1, 1, 2),
    _MscBtdsComponentName_Type()
)
mscBtdsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsComponentName.setStatus("mandatory")
_MscBtdsStorageType_Type = StorageType
_MscBtdsStorageType_Object = MibTableColumn
mscBtdsStorageType = _MscBtdsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 1, 1, 4),
    _MscBtdsStorageType_Type()
)
mscBtdsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsStorageType.setStatus("mandatory")


class _MscBtdsIndex_Type(Integer32):
    """Custom type mscBtdsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscBtdsIndex_Type.__name__ = "Integer32"
_MscBtdsIndex_Object = MibTableColumn
mscBtdsIndex = _MscBtdsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 1, 1, 10),
    _MscBtdsIndex_Type()
)
mscBtdsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscBtdsIndex.setStatus("mandatory")
_MscBtdsFramer_ObjectIdentity = ObjectIdentity
mscBtdsFramer = _MscBtdsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2)
)
_MscBtdsFramerRowStatusTable_Object = MibTable
mscBtdsFramerRowStatusTable = _MscBtdsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 1)
)
if mibBuilder.loadTexts:
    mscBtdsFramerRowStatusTable.setStatus("mandatory")
_MscBtdsFramerRowStatusEntry_Object = MibTableRow
mscBtdsFramerRowStatusEntry = _MscBtdsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 1, 1)
)
mscBtdsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsFramerRowStatusEntry.setStatus("mandatory")
_MscBtdsFramerRowStatus_Type = RowStatus
_MscBtdsFramerRowStatus_Object = MibTableColumn
mscBtdsFramerRowStatus = _MscBtdsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 1, 1, 1),
    _MscBtdsFramerRowStatus_Type()
)
mscBtdsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerRowStatus.setStatus("mandatory")
_MscBtdsFramerComponentName_Type = DisplayString
_MscBtdsFramerComponentName_Object = MibTableColumn
mscBtdsFramerComponentName = _MscBtdsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 1, 1, 2),
    _MscBtdsFramerComponentName_Type()
)
mscBtdsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerComponentName.setStatus("mandatory")
_MscBtdsFramerStorageType_Type = StorageType
_MscBtdsFramerStorageType_Object = MibTableColumn
mscBtdsFramerStorageType = _MscBtdsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 1, 1, 4),
    _MscBtdsFramerStorageType_Type()
)
mscBtdsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerStorageType.setStatus("mandatory")
_MscBtdsFramerIndex_Type = NonReplicated
_MscBtdsFramerIndex_Object = MibTableColumn
mscBtdsFramerIndex = _MscBtdsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 1, 1, 10),
    _MscBtdsFramerIndex_Type()
)
mscBtdsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscBtdsFramerIndex.setStatus("mandatory")
_MscBtdsFramerProvTable_Object = MibTable
mscBtdsFramerProvTable = _MscBtdsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 10)
)
if mibBuilder.loadTexts:
    mscBtdsFramerProvTable.setStatus("mandatory")
_MscBtdsFramerProvEntry_Object = MibTableRow
mscBtdsFramerProvEntry = _MscBtdsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 10, 1)
)
mscBtdsFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsFramerProvEntry.setStatus("mandatory")
_MscBtdsFramerInterfaceName_Type = Link
_MscBtdsFramerInterfaceName_Object = MibTableColumn
mscBtdsFramerInterfaceName = _MscBtdsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 10, 1, 1),
    _MscBtdsFramerInterfaceName_Type()
)
mscBtdsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsFramerInterfaceName.setStatus("mandatory")
_MscBtdsFramerChannelTable_Object = MibTable
mscBtdsFramerChannelTable = _MscBtdsFramerChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 11)
)
if mibBuilder.loadTexts:
    mscBtdsFramerChannelTable.setStatus("mandatory")
_MscBtdsFramerChannelEntry_Object = MibTableRow
mscBtdsFramerChannelEntry = _MscBtdsFramerChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 11, 1)
)
mscBtdsFramerChannelEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsFramerChannelEntry.setStatus("mandatory")


class _MscBtdsFramerProtocol_Type(Integer32):
    """Custom type mscBtdsFramerProtocol based on Integer32"""
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


_MscBtdsFramerProtocol_Type.__name__ = "Integer32"
_MscBtdsFramerProtocol_Object = MibTableColumn
mscBtdsFramerProtocol = _MscBtdsFramerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 11, 1, 7),
    _MscBtdsFramerProtocol_Type()
)
mscBtdsFramerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsFramerProtocol.setStatus("mandatory")


class _MscBtdsFramerNumOfIdleBytesToMonitor_Type(Unsigned32):
    """Custom type mscBtdsFramerNumOfIdleBytesToMonitor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MscBtdsFramerNumOfIdleBytesToMonitor_Type.__name__ = "Unsigned32"
_MscBtdsFramerNumOfIdleBytesToMonitor_Object = MibTableColumn
mscBtdsFramerNumOfIdleBytesToMonitor = _MscBtdsFramerNumOfIdleBytesToMonitor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 11, 1, 8),
    _MscBtdsFramerNumOfIdleBytesToMonitor_Type()
)
mscBtdsFramerNumOfIdleBytesToMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsFramerNumOfIdleBytesToMonitor.setStatus("mandatory")


class _MscBtdsFramerIdlePattern_Type(Hex):
    """Custom type mscBtdsFramerIdlePattern based on Hex"""
    defaultValue = 255

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscBtdsFramerIdlePattern_Type.__name__ = "Hex"
_MscBtdsFramerIdlePattern_Object = MibTableColumn
mscBtdsFramerIdlePattern = _MscBtdsFramerIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 11, 1, 9),
    _MscBtdsFramerIdlePattern_Type()
)
mscBtdsFramerIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsFramerIdlePattern.setStatus("mandatory")


class _MscBtdsFramerTimeSlotAlignment_Type(Integer32):
    """Custom type mscBtdsFramerTimeSlotAlignment based on Integer32"""
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


_MscBtdsFramerTimeSlotAlignment_Type.__name__ = "Integer32"
_MscBtdsFramerTimeSlotAlignment_Object = MibTableColumn
mscBtdsFramerTimeSlotAlignment = _MscBtdsFramerTimeSlotAlignment_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 11, 1, 10),
    _MscBtdsFramerTimeSlotAlignment_Type()
)
mscBtdsFramerTimeSlotAlignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsFramerTimeSlotAlignment.setStatus("mandatory")


class _MscBtdsFramerInsertedOutputDelay_Type(Unsigned32):
    """Custom type mscBtdsFramerInsertedOutputDelay based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_MscBtdsFramerInsertedOutputDelay_Type.__name__ = "Unsigned32"
_MscBtdsFramerInsertedOutputDelay_Object = MibTableColumn
mscBtdsFramerInsertedOutputDelay = _MscBtdsFramerInsertedOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 11, 1, 11),
    _MscBtdsFramerInsertedOutputDelay_Type()
)
mscBtdsFramerInsertedOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsFramerInsertedOutputDelay.setStatus("mandatory")


class _MscBtdsFramerBtdsCellSize_Type(Integer32):
    """Custom type mscBtdsFramerBtdsCellSize based on Integer32"""
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


_MscBtdsFramerBtdsCellSize_Type.__name__ = "Integer32"
_MscBtdsFramerBtdsCellSize_Object = MibTableColumn
mscBtdsFramerBtdsCellSize = _MscBtdsFramerBtdsCellSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 11, 1, 12),
    _MscBtdsFramerBtdsCellSize_Type()
)
mscBtdsFramerBtdsCellSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsFramerBtdsCellSize.setStatus("mandatory")
_MscBtdsFramerStateTable_Object = MibTable
mscBtdsFramerStateTable = _MscBtdsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 12)
)
if mibBuilder.loadTexts:
    mscBtdsFramerStateTable.setStatus("mandatory")
_MscBtdsFramerStateEntry_Object = MibTableRow
mscBtdsFramerStateEntry = _MscBtdsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 12, 1)
)
mscBtdsFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsFramerStateEntry.setStatus("mandatory")


class _MscBtdsFramerAdminState_Type(Integer32):
    """Custom type mscBtdsFramerAdminState based on Integer32"""
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


_MscBtdsFramerAdminState_Type.__name__ = "Integer32"
_MscBtdsFramerAdminState_Object = MibTableColumn
mscBtdsFramerAdminState = _MscBtdsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 12, 1, 1),
    _MscBtdsFramerAdminState_Type()
)
mscBtdsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerAdminState.setStatus("mandatory")


class _MscBtdsFramerOperationalState_Type(Integer32):
    """Custom type mscBtdsFramerOperationalState based on Integer32"""
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


_MscBtdsFramerOperationalState_Type.__name__ = "Integer32"
_MscBtdsFramerOperationalState_Object = MibTableColumn
mscBtdsFramerOperationalState = _MscBtdsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 12, 1, 2),
    _MscBtdsFramerOperationalState_Type()
)
mscBtdsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerOperationalState.setStatus("mandatory")


class _MscBtdsFramerUsageState_Type(Integer32):
    """Custom type mscBtdsFramerUsageState based on Integer32"""
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


_MscBtdsFramerUsageState_Type.__name__ = "Integer32"
_MscBtdsFramerUsageState_Object = MibTableColumn
mscBtdsFramerUsageState = _MscBtdsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 12, 1, 3),
    _MscBtdsFramerUsageState_Type()
)
mscBtdsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerUsageState.setStatus("mandatory")
_MscBtdsFramerStatsTable_Object = MibTable
mscBtdsFramerStatsTable = _MscBtdsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 13)
)
if mibBuilder.loadTexts:
    mscBtdsFramerStatsTable.setStatus("mandatory")
_MscBtdsFramerStatsEntry_Object = MibTableRow
mscBtdsFramerStatsEntry = _MscBtdsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 13, 1)
)
mscBtdsFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsFramerStatsEntry.setStatus("mandatory")
_MscBtdsFramerFrmFromIf_Type = Counter32
_MscBtdsFramerFrmFromIf_Object = MibTableColumn
mscBtdsFramerFrmFromIf = _MscBtdsFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 13, 1, 1),
    _MscBtdsFramerFrmFromIf_Type()
)
mscBtdsFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerFrmFromIf.setStatus("mandatory")
_MscBtdsFramerSuppressedFrames_Type = Counter32
_MscBtdsFramerSuppressedFrames_Object = MibTableColumn
mscBtdsFramerSuppressedFrames = _MscBtdsFramerSuppressedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 13, 1, 3),
    _MscBtdsFramerSuppressedFrames_Type()
)
mscBtdsFramerSuppressedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerSuppressedFrames.setStatus("mandatory")
_MscBtdsFramerFrmToIf_Type = Counter32
_MscBtdsFramerFrmToIf_Object = MibTableColumn
mscBtdsFramerFrmToIf = _MscBtdsFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 13, 1, 4),
    _MscBtdsFramerFrmToIf_Type()
)
mscBtdsFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerFrmToIf.setStatus("mandatory")
_MscBtdsFramerLrcErrors_Type = Counter32
_MscBtdsFramerLrcErrors_Object = MibTableColumn
mscBtdsFramerLrcErrors = _MscBtdsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 13, 1, 5),
    _MscBtdsFramerLrcErrors_Type()
)
mscBtdsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerLrcErrors.setStatus("mandatory")
_MscBtdsFramerFrmLostInNetwork_Type = Counter32
_MscBtdsFramerFrmLostInNetwork_Object = MibTableColumn
mscBtdsFramerFrmLostInNetwork = _MscBtdsFramerFrmLostInNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 13, 1, 6),
    _MscBtdsFramerFrmLostInNetwork_Type()
)
mscBtdsFramerFrmLostInNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerFrmLostInNetwork.setStatus("mandatory")
_MscBtdsFramerFrmUnderRuns_Type = Counter32
_MscBtdsFramerFrmUnderRuns_Object = MibTableColumn
mscBtdsFramerFrmUnderRuns = _MscBtdsFramerFrmUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 13, 1, 7),
    _MscBtdsFramerFrmUnderRuns_Type()
)
mscBtdsFramerFrmUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerFrmUnderRuns.setStatus("mandatory")
_MscBtdsFramerFrmDumped_Type = Counter32
_MscBtdsFramerFrmDumped_Object = MibTableColumn
mscBtdsFramerFrmDumped = _MscBtdsFramerFrmDumped_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 2, 13, 1, 8),
    _MscBtdsFramerFrmDumped_Type()
)
mscBtdsFramerFrmDumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsFramerFrmDumped.setStatus("mandatory")
_MscBtdsPlc_ObjectIdentity = ObjectIdentity
mscBtdsPlc = _MscBtdsPlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3)
)
_MscBtdsPlcRowStatusTable_Object = MibTable
mscBtdsPlcRowStatusTable = _MscBtdsPlcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 1)
)
if mibBuilder.loadTexts:
    mscBtdsPlcRowStatusTable.setStatus("mandatory")
_MscBtdsPlcRowStatusEntry_Object = MibTableRow
mscBtdsPlcRowStatusEntry = _MscBtdsPlcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 1, 1)
)
mscBtdsPlcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsPlcIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsPlcRowStatusEntry.setStatus("mandatory")
_MscBtdsPlcRowStatus_Type = RowStatus
_MscBtdsPlcRowStatus_Object = MibTableColumn
mscBtdsPlcRowStatus = _MscBtdsPlcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 1, 1, 1),
    _MscBtdsPlcRowStatus_Type()
)
mscBtdsPlcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsPlcRowStatus.setStatus("mandatory")
_MscBtdsPlcComponentName_Type = DisplayString
_MscBtdsPlcComponentName_Object = MibTableColumn
mscBtdsPlcComponentName = _MscBtdsPlcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 1, 1, 2),
    _MscBtdsPlcComponentName_Type()
)
mscBtdsPlcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsPlcComponentName.setStatus("mandatory")
_MscBtdsPlcStorageType_Type = StorageType
_MscBtdsPlcStorageType_Object = MibTableColumn
mscBtdsPlcStorageType = _MscBtdsPlcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 1, 1, 4),
    _MscBtdsPlcStorageType_Type()
)
mscBtdsPlcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsPlcStorageType.setStatus("mandatory")
_MscBtdsPlcIndex_Type = NonReplicated
_MscBtdsPlcIndex_Object = MibTableColumn
mscBtdsPlcIndex = _MscBtdsPlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 1, 1, 10),
    _MscBtdsPlcIndex_Type()
)
mscBtdsPlcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscBtdsPlcIndex.setStatus("mandatory")
_MscBtdsPlcProvTable_Object = MibTable
mscBtdsPlcProvTable = _MscBtdsPlcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10)
)
if mibBuilder.loadTexts:
    mscBtdsPlcProvTable.setStatus("mandatory")
_MscBtdsPlcProvEntry_Object = MibTableRow
mscBtdsPlcProvEntry = _MscBtdsPlcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1)
)
mscBtdsPlcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsPlcIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsPlcProvEntry.setStatus("mandatory")


class _MscBtdsPlcRemoteName_Type(AsciiString):
    """Custom type mscBtdsPlcRemoteName based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscBtdsPlcRemoteName_Type.__name__ = "AsciiString"
_MscBtdsPlcRemoteName_Object = MibTableColumn
mscBtdsPlcRemoteName = _MscBtdsPlcRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 2),
    _MscBtdsPlcRemoteName_Type()
)
mscBtdsPlcRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcRemoteName.setStatus("mandatory")


class _MscBtdsPlcSetupPriority_Type(Unsigned32):
    """Custom type mscBtdsPlcSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscBtdsPlcSetupPriority_Type.__name__ = "Unsigned32"
_MscBtdsPlcSetupPriority_Object = MibTableColumn
mscBtdsPlcSetupPriority = _MscBtdsPlcSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 3),
    _MscBtdsPlcSetupPriority_Type()
)
mscBtdsPlcSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcSetupPriority.setStatus("mandatory")


class _MscBtdsPlcHoldingPriority_Type(Unsigned32):
    """Custom type mscBtdsPlcHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscBtdsPlcHoldingPriority_Type.__name__ = "Unsigned32"
_MscBtdsPlcHoldingPriority_Object = MibTableColumn
mscBtdsPlcHoldingPriority = _MscBtdsPlcHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 4),
    _MscBtdsPlcHoldingPriority_Type()
)
mscBtdsPlcHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcHoldingPriority.setStatus("mandatory")


class _MscBtdsPlcRequiredTxBandwidth_Type(Unsigned32):
    """Custom type mscBtdsPlcRequiredTxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscBtdsPlcRequiredTxBandwidth_Type.__name__ = "Unsigned32"
_MscBtdsPlcRequiredTxBandwidth_Object = MibTableColumn
mscBtdsPlcRequiredTxBandwidth = _MscBtdsPlcRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 5),
    _MscBtdsPlcRequiredTxBandwidth_Type()
)
mscBtdsPlcRequiredTxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcRequiredTxBandwidth.setStatus("mandatory")


class _MscBtdsPlcRequiredRxBandwidth_Type(Unsigned32):
    """Custom type mscBtdsPlcRequiredRxBandwidth based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscBtdsPlcRequiredRxBandwidth_Type.__name__ = "Unsigned32"
_MscBtdsPlcRequiredRxBandwidth_Object = MibTableColumn
mscBtdsPlcRequiredRxBandwidth = _MscBtdsPlcRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 6),
    _MscBtdsPlcRequiredRxBandwidth_Type()
)
mscBtdsPlcRequiredRxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcRequiredRxBandwidth.setStatus("mandatory")


class _MscBtdsPlcRequiredTrafficType_Type(Integer32):
    """Custom type mscBtdsPlcRequiredTrafficType based on Integer32"""
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


_MscBtdsPlcRequiredTrafficType_Type.__name__ = "Integer32"
_MscBtdsPlcRequiredTrafficType_Object = MibTableColumn
mscBtdsPlcRequiredTrafficType = _MscBtdsPlcRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 7),
    _MscBtdsPlcRequiredTrafficType_Type()
)
mscBtdsPlcRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcRequiredTrafficType.setStatus("mandatory")


class _MscBtdsPlcPermittedTrunkTypes_Type(OctetString):
    """Custom type mscBtdsPlcPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscBtdsPlcPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscBtdsPlcPermittedTrunkTypes_Object = MibTableColumn
mscBtdsPlcPermittedTrunkTypes = _MscBtdsPlcPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 8),
    _MscBtdsPlcPermittedTrunkTypes_Type()
)
mscBtdsPlcPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcPermittedTrunkTypes.setStatus("mandatory")


class _MscBtdsPlcRequiredSecurity_Type(Unsigned32):
    """Custom type mscBtdsPlcRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscBtdsPlcRequiredSecurity_Type.__name__ = "Unsigned32"
_MscBtdsPlcRequiredSecurity_Object = MibTableColumn
mscBtdsPlcRequiredSecurity = _MscBtdsPlcRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 9),
    _MscBtdsPlcRequiredSecurity_Type()
)
mscBtdsPlcRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcRequiredSecurity.setStatus("mandatory")


class _MscBtdsPlcRequiredCustomerParm_Type(Unsigned32):
    """Custom type mscBtdsPlcRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscBtdsPlcRequiredCustomerParm_Type.__name__ = "Unsigned32"
_MscBtdsPlcRequiredCustomerParm_Object = MibTableColumn
mscBtdsPlcRequiredCustomerParm = _MscBtdsPlcRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 10),
    _MscBtdsPlcRequiredCustomerParm_Type()
)
mscBtdsPlcRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcRequiredCustomerParm.setStatus("mandatory")


class _MscBtdsPlcPathAttributeToMinimize_Type(Integer32):
    """Custom type mscBtdsPlcPathAttributeToMinimize based on Integer32"""
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


_MscBtdsPlcPathAttributeToMinimize_Type.__name__ = "Integer32"
_MscBtdsPlcPathAttributeToMinimize_Object = MibTableColumn
mscBtdsPlcPathAttributeToMinimize = _MscBtdsPlcPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 11),
    _MscBtdsPlcPathAttributeToMinimize_Type()
)
mscBtdsPlcPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcPathAttributeToMinimize.setStatus("mandatory")


class _MscBtdsPlcMaximumAcceptableCost_Type(Unsigned32):
    """Custom type mscBtdsPlcMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscBtdsPlcMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_MscBtdsPlcMaximumAcceptableCost_Object = MibTableColumn
mscBtdsPlcMaximumAcceptableCost = _MscBtdsPlcMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 12),
    _MscBtdsPlcMaximumAcceptableCost_Type()
)
mscBtdsPlcMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcMaximumAcceptableCost.setStatus("mandatory")


class _MscBtdsPlcMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type mscBtdsPlcMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscBtdsPlcMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_MscBtdsPlcMaximumAcceptableDelay_Object = MibTableColumn
mscBtdsPlcMaximumAcceptableDelay = _MscBtdsPlcMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 13),
    _MscBtdsPlcMaximumAcceptableDelay_Type()
)
mscBtdsPlcMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcMaximumAcceptableDelay.setStatus("mandatory")


class _MscBtdsPlcEmissionPriority_Type(Unsigned32):
    """Custom type mscBtdsPlcEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscBtdsPlcEmissionPriority_Type.__name__ = "Unsigned32"
_MscBtdsPlcEmissionPriority_Object = MibTableColumn
mscBtdsPlcEmissionPriority = _MscBtdsPlcEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 14),
    _MscBtdsPlcEmissionPriority_Type()
)
mscBtdsPlcEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcEmissionPriority.setStatus("mandatory")


class _MscBtdsPlcDiscardPriority_Type(Unsigned32):
    """Custom type mscBtdsPlcDiscardPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscBtdsPlcDiscardPriority_Type.__name__ = "Unsigned32"
_MscBtdsPlcDiscardPriority_Object = MibTableColumn
mscBtdsPlcDiscardPriority = _MscBtdsPlcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 15),
    _MscBtdsPlcDiscardPriority_Type()
)
mscBtdsPlcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcDiscardPriority.setStatus("mandatory")


class _MscBtdsPlcPathType_Type(Integer32):
    """Custom type mscBtdsPlcPathType based on Integer32"""
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


_MscBtdsPlcPathType_Type.__name__ = "Integer32"
_MscBtdsPlcPathType_Object = MibTableColumn
mscBtdsPlcPathType = _MscBtdsPlcPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 16),
    _MscBtdsPlcPathType_Type()
)
mscBtdsPlcPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcPathType.setStatus("mandatory")


class _MscBtdsPlcPathFailureAction_Type(Integer32):
    """Custom type mscBtdsPlcPathFailureAction based on Integer32"""
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


_MscBtdsPlcPathFailureAction_Type.__name__ = "Integer32"
_MscBtdsPlcPathFailureAction_Object = MibTableColumn
mscBtdsPlcPathFailureAction = _MscBtdsPlcPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 17),
    _MscBtdsPlcPathFailureAction_Type()
)
mscBtdsPlcPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcPathFailureAction.setStatus("mandatory")


class _MscBtdsPlcBumpPreference_Type(Integer32):
    """Custom type mscBtdsPlcBumpPreference based on Integer32"""
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


_MscBtdsPlcBumpPreference_Type.__name__ = "Integer32"
_MscBtdsPlcBumpPreference_Object = MibTableColumn
mscBtdsPlcBumpPreference = _MscBtdsPlcBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 18),
    _MscBtdsPlcBumpPreference_Type()
)
mscBtdsPlcBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcBumpPreference.setStatus("mandatory")


class _MscBtdsPlcOptimization_Type(Integer32):
    """Custom type mscBtdsPlcOptimization based on Integer32"""
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


_MscBtdsPlcOptimization_Type.__name__ = "Integer32"
_MscBtdsPlcOptimization_Object = MibTableColumn
mscBtdsPlcOptimization = _MscBtdsPlcOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 19),
    _MscBtdsPlcOptimization_Type()
)
mscBtdsPlcOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcOptimization.setStatus("mandatory")


class _MscBtdsPlcAddressToCall_Type(AsciiString):
    """Custom type mscBtdsPlcAddressToCall based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscBtdsPlcAddressToCall_Type.__name__ = "AsciiString"
_MscBtdsPlcAddressToCall_Object = MibTableColumn
mscBtdsPlcAddressToCall = _MscBtdsPlcAddressToCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 20),
    _MscBtdsPlcAddressToCall_Type()
)
mscBtdsPlcAddressToCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcAddressToCall.setStatus("mandatory")


class _MscBtdsPlcLocalAddress_Type(AsciiString):
    """Custom type mscBtdsPlcLocalAddress based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscBtdsPlcLocalAddress_Type.__name__ = "AsciiString"
_MscBtdsPlcLocalAddress_Object = MibTableColumn
mscBtdsPlcLocalAddress = _MscBtdsPlcLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 21),
    _MscBtdsPlcLocalAddress_Type()
)
mscBtdsPlcLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcLocalAddress.setStatus("mandatory")


class _MscBtdsPlcMaximumAcceptableGatewayCost_Type(Unsigned32):
    """Custom type mscBtdsPlcMaximumAcceptableGatewayCost based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscBtdsPlcMaximumAcceptableGatewayCost_Type.__name__ = "Unsigned32"
_MscBtdsPlcMaximumAcceptableGatewayCost_Object = MibTableColumn
mscBtdsPlcMaximumAcceptableGatewayCost = _MscBtdsPlcMaximumAcceptableGatewayCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 10, 1, 22),
    _MscBtdsPlcMaximumAcceptableGatewayCost_Type()
)
mscBtdsPlcMaximumAcceptableGatewayCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcMaximumAcceptableGatewayCost.setStatus("mandatory")
_MscBtdsPlcMpathTable_Object = MibTable
mscBtdsPlcMpathTable = _MscBtdsPlcMpathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 262)
)
if mibBuilder.loadTexts:
    mscBtdsPlcMpathTable.setStatus("mandatory")
_MscBtdsPlcMpathEntry_Object = MibTableRow
mscBtdsPlcMpathEntry = _MscBtdsPlcMpathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 262, 1)
)
mscBtdsPlcMpathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsPlcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsPlcMpathIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsPlcMpathEntry.setStatus("mandatory")


class _MscBtdsPlcMpathIndex_Type(Integer32):
    """Custom type mscBtdsPlcMpathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MscBtdsPlcMpathIndex_Type.__name__ = "Integer32"
_MscBtdsPlcMpathIndex_Object = MibTableColumn
mscBtdsPlcMpathIndex = _MscBtdsPlcMpathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 262, 1, 1),
    _MscBtdsPlcMpathIndex_Type()
)
mscBtdsPlcMpathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscBtdsPlcMpathIndex.setStatus("mandatory")


class _MscBtdsPlcMpathValue_Type(AsciiString):
    """Custom type mscBtdsPlcMpathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscBtdsPlcMpathValue_Type.__name__ = "AsciiString"
_MscBtdsPlcMpathValue_Object = MibTableColumn
mscBtdsPlcMpathValue = _MscBtdsPlcMpathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 3, 262, 1, 2),
    _MscBtdsPlcMpathValue_Type()
)
mscBtdsPlcMpathValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsPlcMpathValue.setStatus("mandatory")
_MscBtdsLCo_ObjectIdentity = ObjectIdentity
mscBtdsLCo = _MscBtdsLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4)
)
_MscBtdsLCoRowStatusTable_Object = MibTable
mscBtdsLCoRowStatusTable = _MscBtdsLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 1)
)
if mibBuilder.loadTexts:
    mscBtdsLCoRowStatusTable.setStatus("mandatory")
_MscBtdsLCoRowStatusEntry_Object = MibTableRow
mscBtdsLCoRowStatusEntry = _MscBtdsLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 1, 1)
)
mscBtdsLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsLCoRowStatusEntry.setStatus("mandatory")
_MscBtdsLCoRowStatus_Type = RowStatus
_MscBtdsLCoRowStatus_Object = MibTableColumn
mscBtdsLCoRowStatus = _MscBtdsLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 1, 1, 1),
    _MscBtdsLCoRowStatus_Type()
)
mscBtdsLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoRowStatus.setStatus("mandatory")
_MscBtdsLCoComponentName_Type = DisplayString
_MscBtdsLCoComponentName_Object = MibTableColumn
mscBtdsLCoComponentName = _MscBtdsLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 1, 1, 2),
    _MscBtdsLCoComponentName_Type()
)
mscBtdsLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoComponentName.setStatus("mandatory")
_MscBtdsLCoStorageType_Type = StorageType
_MscBtdsLCoStorageType_Object = MibTableColumn
mscBtdsLCoStorageType = _MscBtdsLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 1, 1, 4),
    _MscBtdsLCoStorageType_Type()
)
mscBtdsLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoStorageType.setStatus("mandatory")
_MscBtdsLCoIndex_Type = NonReplicated
_MscBtdsLCoIndex_Object = MibTableColumn
mscBtdsLCoIndex = _MscBtdsLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 1, 1, 10),
    _MscBtdsLCoIndex_Type()
)
mscBtdsLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscBtdsLCoIndex.setStatus("mandatory")
_MscBtdsLCoPathDataTable_Object = MibTable
mscBtdsLCoPathDataTable = _MscBtdsLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10)
)
if mibBuilder.loadTexts:
    mscBtdsLCoPathDataTable.setStatus("mandatory")
_MscBtdsLCoPathDataEntry_Object = MibTableRow
mscBtdsLCoPathDataEntry = _MscBtdsLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1)
)
mscBtdsLCoPathDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsLCoPathDataEntry.setStatus("mandatory")


class _MscBtdsLCoState_Type(Integer32):
    """Custom type mscBtdsLCoState based on Integer32"""
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


_MscBtdsLCoState_Type.__name__ = "Integer32"
_MscBtdsLCoState_Object = MibTableColumn
mscBtdsLCoState = _MscBtdsLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 1),
    _MscBtdsLCoState_Type()
)
mscBtdsLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoState.setStatus("mandatory")


class _MscBtdsLCoOverrideRemoteName_Type(AsciiString):
    """Custom type mscBtdsLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscBtdsLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_MscBtdsLCoOverrideRemoteName_Object = MibTableColumn
mscBtdsLCoOverrideRemoteName = _MscBtdsLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 2),
    _MscBtdsLCoOverrideRemoteName_Type()
)
mscBtdsLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsLCoOverrideRemoteName.setStatus("mandatory")


class _MscBtdsLCoEnd_Type(Integer32):
    """Custom type mscBtdsLCoEnd based on Integer32"""
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


_MscBtdsLCoEnd_Type.__name__ = "Integer32"
_MscBtdsLCoEnd_Object = MibTableColumn
mscBtdsLCoEnd = _MscBtdsLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 3),
    _MscBtdsLCoEnd_Type()
)
mscBtdsLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoEnd.setStatus("mandatory")


class _MscBtdsLCoCostMetric_Type(Unsigned32):
    """Custom type mscBtdsLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscBtdsLCoCostMetric_Type.__name__ = "Unsigned32"
_MscBtdsLCoCostMetric_Object = MibTableColumn
mscBtdsLCoCostMetric = _MscBtdsLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 4),
    _MscBtdsLCoCostMetric_Type()
)
mscBtdsLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoCostMetric.setStatus("mandatory")


class _MscBtdsLCoDelayMetric_Type(Unsigned32):
    """Custom type mscBtdsLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscBtdsLCoDelayMetric_Type.__name__ = "Unsigned32"
_MscBtdsLCoDelayMetric_Object = MibTableColumn
mscBtdsLCoDelayMetric = _MscBtdsLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 5),
    _MscBtdsLCoDelayMetric_Type()
)
mscBtdsLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoDelayMetric.setStatus("mandatory")


class _MscBtdsLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mscBtdsLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_MscBtdsLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_MscBtdsLCoRoundTripDelay_Object = MibTableColumn
mscBtdsLCoRoundTripDelay = _MscBtdsLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 6),
    _MscBtdsLCoRoundTripDelay_Type()
)
mscBtdsLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoRoundTripDelay.setStatus("mandatory")


class _MscBtdsLCoSetupPriority_Type(Unsigned32):
    """Custom type mscBtdsLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscBtdsLCoSetupPriority_Type.__name__ = "Unsigned32"
_MscBtdsLCoSetupPriority_Object = MibTableColumn
mscBtdsLCoSetupPriority = _MscBtdsLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 7),
    _MscBtdsLCoSetupPriority_Type()
)
mscBtdsLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoSetupPriority.setStatus("mandatory")


class _MscBtdsLCoHoldingPriority_Type(Unsigned32):
    """Custom type mscBtdsLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscBtdsLCoHoldingPriority_Type.__name__ = "Unsigned32"
_MscBtdsLCoHoldingPriority_Object = MibTableColumn
mscBtdsLCoHoldingPriority = _MscBtdsLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 8),
    _MscBtdsLCoHoldingPriority_Type()
)
mscBtdsLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoHoldingPriority.setStatus("mandatory")


class _MscBtdsLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mscBtdsLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscBtdsLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_MscBtdsLCoRequiredTxBandwidth_Object = MibTableColumn
mscBtdsLCoRequiredTxBandwidth = _MscBtdsLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 9),
    _MscBtdsLCoRequiredTxBandwidth_Type()
)
mscBtdsLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoRequiredTxBandwidth.setStatus("mandatory")


class _MscBtdsLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mscBtdsLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscBtdsLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_MscBtdsLCoRequiredRxBandwidth_Object = MibTableColumn
mscBtdsLCoRequiredRxBandwidth = _MscBtdsLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 10),
    _MscBtdsLCoRequiredRxBandwidth_Type()
)
mscBtdsLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoRequiredRxBandwidth.setStatus("mandatory")


class _MscBtdsLCoRequiredTrafficType_Type(Integer32):
    """Custom type mscBtdsLCoRequiredTrafficType based on Integer32"""
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


_MscBtdsLCoRequiredTrafficType_Type.__name__ = "Integer32"
_MscBtdsLCoRequiredTrafficType_Object = MibTableColumn
mscBtdsLCoRequiredTrafficType = _MscBtdsLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 11),
    _MscBtdsLCoRequiredTrafficType_Type()
)
mscBtdsLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoRequiredTrafficType.setStatus("mandatory")


class _MscBtdsLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mscBtdsLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscBtdsLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscBtdsLCoPermittedTrunkTypes_Object = MibTableColumn
mscBtdsLCoPermittedTrunkTypes = _MscBtdsLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 12),
    _MscBtdsLCoPermittedTrunkTypes_Type()
)
mscBtdsLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoPermittedTrunkTypes.setStatus("mandatory")


class _MscBtdsLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mscBtdsLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscBtdsLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_MscBtdsLCoRequiredSecurity_Object = MibTableColumn
mscBtdsLCoRequiredSecurity = _MscBtdsLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 13),
    _MscBtdsLCoRequiredSecurity_Type()
)
mscBtdsLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoRequiredSecurity.setStatus("mandatory")


class _MscBtdsLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mscBtdsLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscBtdsLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_MscBtdsLCoRequiredCustomerParameter_Object = MibTableColumn
mscBtdsLCoRequiredCustomerParameter = _MscBtdsLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 14),
    _MscBtdsLCoRequiredCustomerParameter_Type()
)
mscBtdsLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoRequiredCustomerParameter.setStatus("mandatory")


class _MscBtdsLCoEmissionPriority_Type(Unsigned32):
    """Custom type mscBtdsLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscBtdsLCoEmissionPriority_Type.__name__ = "Unsigned32"
_MscBtdsLCoEmissionPriority_Object = MibTableColumn
mscBtdsLCoEmissionPriority = _MscBtdsLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 15),
    _MscBtdsLCoEmissionPriority_Type()
)
mscBtdsLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoEmissionPriority.setStatus("mandatory")


class _MscBtdsLCoDiscardPriority_Type(Unsigned32):
    """Custom type mscBtdsLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscBtdsLCoDiscardPriority_Type.__name__ = "Unsigned32"
_MscBtdsLCoDiscardPriority_Object = MibTableColumn
mscBtdsLCoDiscardPriority = _MscBtdsLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 16),
    _MscBtdsLCoDiscardPriority_Type()
)
mscBtdsLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoDiscardPriority.setStatus("mandatory")


class _MscBtdsLCoPathType_Type(Integer32):
    """Custom type mscBtdsLCoPathType based on Integer32"""
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


_MscBtdsLCoPathType_Type.__name__ = "Integer32"
_MscBtdsLCoPathType_Object = MibTableColumn
mscBtdsLCoPathType = _MscBtdsLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 17),
    _MscBtdsLCoPathType_Type()
)
mscBtdsLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoPathType.setStatus("mandatory")


class _MscBtdsLCoRetryCount_Type(Unsigned32):
    """Custom type mscBtdsLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscBtdsLCoRetryCount_Type.__name__ = "Unsigned32"
_MscBtdsLCoRetryCount_Object = MibTableColumn
mscBtdsLCoRetryCount = _MscBtdsLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 18),
    _MscBtdsLCoRetryCount_Type()
)
mscBtdsLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoRetryCount.setStatus("mandatory")


class _MscBtdsLCoPathFailureCount_Type(Unsigned32):
    """Custom type mscBtdsLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscBtdsLCoPathFailureCount_Type.__name__ = "Unsigned32"
_MscBtdsLCoPathFailureCount_Object = MibTableColumn
mscBtdsLCoPathFailureCount = _MscBtdsLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 19),
    _MscBtdsLCoPathFailureCount_Type()
)
mscBtdsLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoPathFailureCount.setStatus("mandatory")


class _MscBtdsLCoReasonForNoRoute_Type(Integer32):
    """Custom type mscBtdsLCoReasonForNoRoute based on Integer32"""
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


_MscBtdsLCoReasonForNoRoute_Type.__name__ = "Integer32"
_MscBtdsLCoReasonForNoRoute_Object = MibTableColumn
mscBtdsLCoReasonForNoRoute = _MscBtdsLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 20),
    _MscBtdsLCoReasonForNoRoute_Type()
)
mscBtdsLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoReasonForNoRoute.setStatus("mandatory")


class _MscBtdsLCoLastTearDownReason_Type(Integer32):
    """Custom type mscBtdsLCoLastTearDownReason based on Integer32"""
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


_MscBtdsLCoLastTearDownReason_Type.__name__ = "Integer32"
_MscBtdsLCoLastTearDownReason_Object = MibTableColumn
mscBtdsLCoLastTearDownReason = _MscBtdsLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 21),
    _MscBtdsLCoLastTearDownReason_Type()
)
mscBtdsLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoLastTearDownReason.setStatus("mandatory")


class _MscBtdsLCoPathFailureAction_Type(Integer32):
    """Custom type mscBtdsLCoPathFailureAction based on Integer32"""
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


_MscBtdsLCoPathFailureAction_Type.__name__ = "Integer32"
_MscBtdsLCoPathFailureAction_Object = MibTableColumn
mscBtdsLCoPathFailureAction = _MscBtdsLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 22),
    _MscBtdsLCoPathFailureAction_Type()
)
mscBtdsLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoPathFailureAction.setStatus("mandatory")


class _MscBtdsLCoBumpPreference_Type(Integer32):
    """Custom type mscBtdsLCoBumpPreference based on Integer32"""
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


_MscBtdsLCoBumpPreference_Type.__name__ = "Integer32"
_MscBtdsLCoBumpPreference_Object = MibTableColumn
mscBtdsLCoBumpPreference = _MscBtdsLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 23),
    _MscBtdsLCoBumpPreference_Type()
)
mscBtdsLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoBumpPreference.setStatus("mandatory")


class _MscBtdsLCoOptimization_Type(Integer32):
    """Custom type mscBtdsLCoOptimization based on Integer32"""
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


_MscBtdsLCoOptimization_Type.__name__ = "Integer32"
_MscBtdsLCoOptimization_Object = MibTableColumn
mscBtdsLCoOptimization = _MscBtdsLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 24),
    _MscBtdsLCoOptimization_Type()
)
mscBtdsLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoOptimization.setStatus("mandatory")


class _MscBtdsLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mscBtdsLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscBtdsLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_MscBtdsLCoPathUpDateTime_Object = MibTableColumn
mscBtdsLCoPathUpDateTime = _MscBtdsLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 10, 1, 25),
    _MscBtdsLCoPathUpDateTime_Type()
)
mscBtdsLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoPathUpDateTime.setStatus("mandatory")
_MscBtdsLCoStatsTable_Object = MibTable
mscBtdsLCoStatsTable = _MscBtdsLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 11)
)
if mibBuilder.loadTexts:
    mscBtdsLCoStatsTable.setStatus("mandatory")
_MscBtdsLCoStatsEntry_Object = MibTableRow
mscBtdsLCoStatsEntry = _MscBtdsLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 11, 1)
)
mscBtdsLCoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsLCoIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsLCoStatsEntry.setStatus("mandatory")
_MscBtdsLCoPktsToNetwork_Type = PassportCounter64
_MscBtdsLCoPktsToNetwork_Object = MibTableColumn
mscBtdsLCoPktsToNetwork = _MscBtdsLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 11, 1, 1),
    _MscBtdsLCoPktsToNetwork_Type()
)
mscBtdsLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoPktsToNetwork.setStatus("mandatory")
_MscBtdsLCoBytesToNetwork_Type = PassportCounter64
_MscBtdsLCoBytesToNetwork_Object = MibTableColumn
mscBtdsLCoBytesToNetwork = _MscBtdsLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 11, 1, 2),
    _MscBtdsLCoBytesToNetwork_Type()
)
mscBtdsLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoBytesToNetwork.setStatus("mandatory")
_MscBtdsLCoPktsFromNetwork_Type = PassportCounter64
_MscBtdsLCoPktsFromNetwork_Object = MibTableColumn
mscBtdsLCoPktsFromNetwork = _MscBtdsLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 11, 1, 3),
    _MscBtdsLCoPktsFromNetwork_Type()
)
mscBtdsLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoPktsFromNetwork.setStatus("mandatory")
_MscBtdsLCoBytesFromNetwork_Type = PassportCounter64
_MscBtdsLCoBytesFromNetwork_Object = MibTableColumn
mscBtdsLCoBytesFromNetwork = _MscBtdsLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 11, 1, 4),
    _MscBtdsLCoBytesFromNetwork_Type()
)
mscBtdsLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoBytesFromNetwork.setStatus("mandatory")
_MscBtdsLCoPathTable_Object = MibTable
mscBtdsLCoPathTable = _MscBtdsLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 264)
)
if mibBuilder.loadTexts:
    mscBtdsLCoPathTable.setStatus("mandatory")
_MscBtdsLCoPathEntry_Object = MibTableRow
mscBtdsLCoPathEntry = _MscBtdsLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 264, 1)
)
mscBtdsLCoPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsLCoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsLCoPathValue"),
)
if mibBuilder.loadTexts:
    mscBtdsLCoPathEntry.setStatus("mandatory")


class _MscBtdsLCoPathValue_Type(AsciiString):
    """Custom type mscBtdsLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscBtdsLCoPathValue_Type.__name__ = "AsciiString"
_MscBtdsLCoPathValue_Object = MibTableColumn
mscBtdsLCoPathValue = _MscBtdsLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 4, 264, 1, 1),
    _MscBtdsLCoPathValue_Type()
)
mscBtdsLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsLCoPathValue.setStatus("mandatory")
_MscBtdsDpnss1_ObjectIdentity = ObjectIdentity
mscBtdsDpnss1 = _MscBtdsDpnss1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5)
)
_MscBtdsDpnss1RowStatusTable_Object = MibTable
mscBtdsDpnss1RowStatusTable = _MscBtdsDpnss1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 1)
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1RowStatusTable.setStatus("mandatory")
_MscBtdsDpnss1RowStatusEntry_Object = MibTableRow
mscBtdsDpnss1RowStatusEntry = _MscBtdsDpnss1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 1, 1)
)
mscBtdsDpnss1RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1RowStatusEntry.setStatus("mandatory")
_MscBtdsDpnss1RowStatus_Type = RowStatus
_MscBtdsDpnss1RowStatus_Object = MibTableColumn
mscBtdsDpnss1RowStatus = _MscBtdsDpnss1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 1, 1, 1),
    _MscBtdsDpnss1RowStatus_Type()
)
mscBtdsDpnss1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsDpnss1RowStatus.setStatus("mandatory")
_MscBtdsDpnss1ComponentName_Type = DisplayString
_MscBtdsDpnss1ComponentName_Object = MibTableColumn
mscBtdsDpnss1ComponentName = _MscBtdsDpnss1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 1, 1, 2),
    _MscBtdsDpnss1ComponentName_Type()
)
mscBtdsDpnss1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1ComponentName.setStatus("mandatory")
_MscBtdsDpnss1StorageType_Type = StorageType
_MscBtdsDpnss1StorageType_Object = MibTableColumn
mscBtdsDpnss1StorageType = _MscBtdsDpnss1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 1, 1, 4),
    _MscBtdsDpnss1StorageType_Type()
)
mscBtdsDpnss1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1StorageType.setStatus("mandatory")
_MscBtdsDpnss1Index_Type = NonReplicated
_MscBtdsDpnss1Index_Object = MibTableColumn
mscBtdsDpnss1Index = _MscBtdsDpnss1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 1, 1, 10),
    _MscBtdsDpnss1Index_Type()
)
mscBtdsDpnss1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscBtdsDpnss1Index.setStatus("mandatory")
_MscBtdsDpnss1ProvTable_Object = MibTable
mscBtdsDpnss1ProvTable = _MscBtdsDpnss1ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 10)
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1ProvTable.setStatus("mandatory")
_MscBtdsDpnss1ProvEntry_Object = MibTableRow
mscBtdsDpnss1ProvEntry = _MscBtdsDpnss1ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 10, 1)
)
mscBtdsDpnss1ProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1ProvEntry.setStatus("mandatory")


class _MscBtdsDpnss1TimeslotsX_Type(OctetString):
    """Custom type mscBtdsDpnss1TimeslotsX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscBtdsDpnss1TimeslotsX_Type.__name__ = "OctetString"
_MscBtdsDpnss1TimeslotsX_Object = MibTableColumn
mscBtdsDpnss1TimeslotsX = _MscBtdsDpnss1TimeslotsX_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 10, 1, 1),
    _MscBtdsDpnss1TimeslotsX_Type()
)
mscBtdsDpnss1TimeslotsX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsDpnss1TimeslotsX.setStatus("mandatory")
_MscBtdsDpnss1VdcdTable_Object = MibTable
mscBtdsDpnss1VdcdTable = _MscBtdsDpnss1VdcdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 12)
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1VdcdTable.setStatus("mandatory")
_MscBtdsDpnss1VdcdEntry_Object = MibTableRow
mscBtdsDpnss1VdcdEntry = _MscBtdsDpnss1VdcdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 12, 1)
)
mscBtdsDpnss1VdcdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1VdcdEntry.setStatus("mandatory")
_MscBtdsDpnss1NewVoiceCalls_Type = Counter32
_MscBtdsDpnss1NewVoiceCalls_Object = MibTableColumn
mscBtdsDpnss1NewVoiceCalls = _MscBtdsDpnss1NewVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 12, 1, 1),
    _MscBtdsDpnss1NewVoiceCalls_Type()
)
mscBtdsDpnss1NewVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1NewVoiceCalls.setStatus("mandatory")
_MscBtdsDpnss1NewDataCalls_Type = Counter32
_MscBtdsDpnss1NewDataCalls_Object = MibTableColumn
mscBtdsDpnss1NewDataCalls = _MscBtdsDpnss1NewDataCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 12, 1, 2),
    _MscBtdsDpnss1NewDataCalls_Type()
)
mscBtdsDpnss1NewDataCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1NewDataCalls.setStatus("mandatory")
_MscBtdsDpnss1VoiceToData_Type = Counter32
_MscBtdsDpnss1VoiceToData_Object = MibTableColumn
mscBtdsDpnss1VoiceToData = _MscBtdsDpnss1VoiceToData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 12, 1, 3),
    _MscBtdsDpnss1VoiceToData_Type()
)
mscBtdsDpnss1VoiceToData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1VoiceToData.setStatus("mandatory")
_MscBtdsDpnss1DataToVoice_Type = Counter32
_MscBtdsDpnss1DataToVoice_Object = MibTableColumn
mscBtdsDpnss1DataToVoice = _MscBtdsDpnss1DataToVoice_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 12, 1, 4),
    _MscBtdsDpnss1DataToVoice_Type()
)
mscBtdsDpnss1DataToVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1DataToVoice.setStatus("mandatory")
_MscBtdsDpnss1CallClears_Type = Counter32
_MscBtdsDpnss1CallClears_Object = MibTableColumn
mscBtdsDpnss1CallClears = _MscBtdsDpnss1CallClears_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 12, 1, 5),
    _MscBtdsDpnss1CallClears_Type()
)
mscBtdsDpnss1CallClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1CallClears.setStatus("mandatory")
_MscBtdsDpnss1FramesTable_Object = MibTable
mscBtdsDpnss1FramesTable = _MscBtdsDpnss1FramesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 13)
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1FramesTable.setStatus("mandatory")
_MscBtdsDpnss1FramesEntry_Object = MibTableRow
mscBtdsDpnss1FramesEntry = _MscBtdsDpnss1FramesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 13, 1)
)
mscBtdsDpnss1FramesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1FramesEntry.setStatus("mandatory")
_MscBtdsDpnss1FrmProcessed_Type = Counter32
_MscBtdsDpnss1FrmProcessed_Object = MibTableColumn
mscBtdsDpnss1FrmProcessed = _MscBtdsDpnss1FrmProcessed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 13, 1, 1),
    _MscBtdsDpnss1FrmProcessed_Type()
)
mscBtdsDpnss1FrmProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1FrmProcessed.setStatus("mandatory")
_MscBtdsDpnss1FrmInvalid_Type = Counter32
_MscBtdsDpnss1FrmInvalid_Object = MibTableColumn
mscBtdsDpnss1FrmInvalid = _MscBtdsDpnss1FrmInvalid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 13, 1, 2),
    _MscBtdsDpnss1FrmInvalid_Type()
)
mscBtdsDpnss1FrmInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1FrmInvalid.setStatus("mandatory")
_MscBtdsDpnss1HdlcTable_Object = MibTable
mscBtdsDpnss1HdlcTable = _MscBtdsDpnss1HdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 14)
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1HdlcTable.setStatus("mandatory")
_MscBtdsDpnss1HdlcEntry_Object = MibTableRow
mscBtdsDpnss1HdlcEntry = _MscBtdsDpnss1HdlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 14, 1)
)
mscBtdsDpnss1HdlcEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsDpnss1Index"),
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1HdlcEntry.setStatus("mandatory")
_MscBtdsDpnss1FrmFromIf_Type = Counter32
_MscBtdsDpnss1FrmFromIf_Object = MibTableColumn
mscBtdsDpnss1FrmFromIf = _MscBtdsDpnss1FrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 14, 1, 2),
    _MscBtdsDpnss1FrmFromIf_Type()
)
mscBtdsDpnss1FrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1FrmFromIf.setStatus("mandatory")
_MscBtdsDpnss1Aborts_Type = Counter32
_MscBtdsDpnss1Aborts_Object = MibTableColumn
mscBtdsDpnss1Aborts = _MscBtdsDpnss1Aborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 14, 1, 3),
    _MscBtdsDpnss1Aborts_Type()
)
mscBtdsDpnss1Aborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1Aborts.setStatus("mandatory")
_MscBtdsDpnss1CrcErrors_Type = Counter32
_MscBtdsDpnss1CrcErrors_Object = MibTableColumn
mscBtdsDpnss1CrcErrors = _MscBtdsDpnss1CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 14, 1, 4),
    _MscBtdsDpnss1CrcErrors_Type()
)
mscBtdsDpnss1CrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1CrcErrors.setStatus("mandatory")
_MscBtdsDpnss1NonOctetErrors_Type = Counter32
_MscBtdsDpnss1NonOctetErrors_Object = MibTableColumn
mscBtdsDpnss1NonOctetErrors = _MscBtdsDpnss1NonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 14, 1, 5),
    _MscBtdsDpnss1NonOctetErrors_Type()
)
mscBtdsDpnss1NonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1NonOctetErrors.setStatus("mandatory")
_MscBtdsDpnss1Overruns_Type = Counter32
_MscBtdsDpnss1Overruns_Object = MibTableColumn
mscBtdsDpnss1Overruns = _MscBtdsDpnss1Overruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 14, 1, 6),
    _MscBtdsDpnss1Overruns_Type()
)
mscBtdsDpnss1Overruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1Overruns.setStatus("mandatory")
_MscBtdsDpnss1LargeFrmErrors_Type = Counter32
_MscBtdsDpnss1LargeFrmErrors_Object = MibTableColumn
mscBtdsDpnss1LargeFrmErrors = _MscBtdsDpnss1LargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 14, 1, 8),
    _MscBtdsDpnss1LargeFrmErrors_Type()
)
mscBtdsDpnss1LargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1LargeFrmErrors.setStatus("mandatory")
_MscBtdsDpnss1TSlotTable_Object = MibTable
mscBtdsDpnss1TSlotTable = _MscBtdsDpnss1TSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 286)
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1TSlotTable.setStatus("mandatory")
_MscBtdsDpnss1TSlotEntry_Object = MibTableRow
mscBtdsDpnss1TSlotEntry = _MscBtdsDpnss1TSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 286, 1)
)
mscBtdsDpnss1TSlotEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsDpnss1Index"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsDpnss1TSlotIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsDpnss1TSlotEntry.setStatus("mandatory")


class _MscBtdsDpnss1TSlotIndex_Type(Integer32):
    """Custom type mscBtdsDpnss1TSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MscBtdsDpnss1TSlotIndex_Type.__name__ = "Integer32"
_MscBtdsDpnss1TSlotIndex_Object = MibTableColumn
mscBtdsDpnss1TSlotIndex = _MscBtdsDpnss1TSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 286, 1, 1),
    _MscBtdsDpnss1TSlotIndex_Type()
)
mscBtdsDpnss1TSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscBtdsDpnss1TSlotIndex.setStatus("mandatory")


class _MscBtdsDpnss1TSlotValue_Type(Integer32):
    """Custom type mscBtdsDpnss1TSlotValue based on Integer32"""
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


_MscBtdsDpnss1TSlotValue_Type.__name__ = "Integer32"
_MscBtdsDpnss1TSlotValue_Object = MibTableColumn
mscBtdsDpnss1TSlotValue = _MscBtdsDpnss1TSlotValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 5, 286, 1, 2),
    _MscBtdsDpnss1TSlotValue_Type()
)
mscBtdsDpnss1TSlotValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsDpnss1TSlotValue.setStatus("mandatory")
_MscBtdsMcdn_ObjectIdentity = ObjectIdentity
mscBtdsMcdn = _MscBtdsMcdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6)
)
_MscBtdsMcdnRowStatusTable_Object = MibTable
mscBtdsMcdnRowStatusTable = _MscBtdsMcdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 1)
)
if mibBuilder.loadTexts:
    mscBtdsMcdnRowStatusTable.setStatus("mandatory")
_MscBtdsMcdnRowStatusEntry_Object = MibTableRow
mscBtdsMcdnRowStatusEntry = _MscBtdsMcdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 1, 1)
)
mscBtdsMcdnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsMcdnRowStatusEntry.setStatus("mandatory")
_MscBtdsMcdnRowStatus_Type = RowStatus
_MscBtdsMcdnRowStatus_Object = MibTableColumn
mscBtdsMcdnRowStatus = _MscBtdsMcdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 1, 1, 1),
    _MscBtdsMcdnRowStatus_Type()
)
mscBtdsMcdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsMcdnRowStatus.setStatus("mandatory")
_MscBtdsMcdnComponentName_Type = DisplayString
_MscBtdsMcdnComponentName_Object = MibTableColumn
mscBtdsMcdnComponentName = _MscBtdsMcdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 1, 1, 2),
    _MscBtdsMcdnComponentName_Type()
)
mscBtdsMcdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnComponentName.setStatus("mandatory")
_MscBtdsMcdnStorageType_Type = StorageType
_MscBtdsMcdnStorageType_Object = MibTableColumn
mscBtdsMcdnStorageType = _MscBtdsMcdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 1, 1, 4),
    _MscBtdsMcdnStorageType_Type()
)
mscBtdsMcdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnStorageType.setStatus("mandatory")
_MscBtdsMcdnIndex_Type = NonReplicated
_MscBtdsMcdnIndex_Object = MibTableColumn
mscBtdsMcdnIndex = _MscBtdsMcdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 1, 1, 10),
    _MscBtdsMcdnIndex_Type()
)
mscBtdsMcdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscBtdsMcdnIndex.setStatus("mandatory")
_MscBtdsMcdnProvTable_Object = MibTable
mscBtdsMcdnProvTable = _MscBtdsMcdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 10)
)
if mibBuilder.loadTexts:
    mscBtdsMcdnProvTable.setStatus("mandatory")
_MscBtdsMcdnProvEntry_Object = MibTableRow
mscBtdsMcdnProvEntry = _MscBtdsMcdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 10, 1)
)
mscBtdsMcdnProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsMcdnProvEntry.setStatus("mandatory")


class _MscBtdsMcdnAdjPbxSide_Type(Integer32):
    """Custom type mscBtdsMcdnAdjPbxSide based on Integer32"""
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


_MscBtdsMcdnAdjPbxSide_Type.__name__ = "Integer32"
_MscBtdsMcdnAdjPbxSide_Object = MibTableColumn
mscBtdsMcdnAdjPbxSide = _MscBtdsMcdnAdjPbxSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 10, 1, 1),
    _MscBtdsMcdnAdjPbxSide_Type()
)
mscBtdsMcdnAdjPbxSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsMcdnAdjPbxSide.setStatus("mandatory")
_MscBtdsMcdnVdcdTable_Object = MibTable
mscBtdsMcdnVdcdTable = _MscBtdsMcdnVdcdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 12)
)
if mibBuilder.loadTexts:
    mscBtdsMcdnVdcdTable.setStatus("mandatory")
_MscBtdsMcdnVdcdEntry_Object = MibTableRow
mscBtdsMcdnVdcdEntry = _MscBtdsMcdnVdcdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 12, 1)
)
mscBtdsMcdnVdcdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsMcdnVdcdEntry.setStatus("mandatory")
_MscBtdsMcdnNewVoiceCalls_Type = Counter32
_MscBtdsMcdnNewVoiceCalls_Object = MibTableColumn
mscBtdsMcdnNewVoiceCalls = _MscBtdsMcdnNewVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 12, 1, 1),
    _MscBtdsMcdnNewVoiceCalls_Type()
)
mscBtdsMcdnNewVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnNewVoiceCalls.setStatus("mandatory")
_MscBtdsMcdnNewDataCalls_Type = Counter32
_MscBtdsMcdnNewDataCalls_Object = MibTableColumn
mscBtdsMcdnNewDataCalls = _MscBtdsMcdnNewDataCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 12, 1, 2),
    _MscBtdsMcdnNewDataCalls_Type()
)
mscBtdsMcdnNewDataCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnNewDataCalls.setStatus("mandatory")
_MscBtdsMcdnVoiceToData_Type = Counter32
_MscBtdsMcdnVoiceToData_Object = MibTableColumn
mscBtdsMcdnVoiceToData = _MscBtdsMcdnVoiceToData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 12, 1, 3),
    _MscBtdsMcdnVoiceToData_Type()
)
mscBtdsMcdnVoiceToData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnVoiceToData.setStatus("mandatory")
_MscBtdsMcdnDataToVoice_Type = Counter32
_MscBtdsMcdnDataToVoice_Object = MibTableColumn
mscBtdsMcdnDataToVoice = _MscBtdsMcdnDataToVoice_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 12, 1, 4),
    _MscBtdsMcdnDataToVoice_Type()
)
mscBtdsMcdnDataToVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnDataToVoice.setStatus("mandatory")
_MscBtdsMcdnCallClears_Type = Counter32
_MscBtdsMcdnCallClears_Object = MibTableColumn
mscBtdsMcdnCallClears = _MscBtdsMcdnCallClears_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 12, 1, 5),
    _MscBtdsMcdnCallClears_Type()
)
mscBtdsMcdnCallClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnCallClears.setStatus("mandatory")
_MscBtdsMcdnFramesTable_Object = MibTable
mscBtdsMcdnFramesTable = _MscBtdsMcdnFramesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 13)
)
if mibBuilder.loadTexts:
    mscBtdsMcdnFramesTable.setStatus("mandatory")
_MscBtdsMcdnFramesEntry_Object = MibTableRow
mscBtdsMcdnFramesEntry = _MscBtdsMcdnFramesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 13, 1)
)
mscBtdsMcdnFramesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsMcdnFramesEntry.setStatus("mandatory")
_MscBtdsMcdnFrmProcessed_Type = Counter32
_MscBtdsMcdnFrmProcessed_Object = MibTableColumn
mscBtdsMcdnFrmProcessed = _MscBtdsMcdnFrmProcessed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 13, 1, 1),
    _MscBtdsMcdnFrmProcessed_Type()
)
mscBtdsMcdnFrmProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnFrmProcessed.setStatus("mandatory")
_MscBtdsMcdnFrmInvalid_Type = Counter32
_MscBtdsMcdnFrmInvalid_Object = MibTableColumn
mscBtdsMcdnFrmInvalid = _MscBtdsMcdnFrmInvalid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 13, 1, 2),
    _MscBtdsMcdnFrmInvalid_Type()
)
mscBtdsMcdnFrmInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnFrmInvalid.setStatus("mandatory")
_MscBtdsMcdnHdlcTable_Object = MibTable
mscBtdsMcdnHdlcTable = _MscBtdsMcdnHdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 14)
)
if mibBuilder.loadTexts:
    mscBtdsMcdnHdlcTable.setStatus("mandatory")
_MscBtdsMcdnHdlcEntry_Object = MibTableRow
mscBtdsMcdnHdlcEntry = _MscBtdsMcdnHdlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 14, 1)
)
mscBtdsMcdnHdlcEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsMcdnHdlcEntry.setStatus("mandatory")
_MscBtdsMcdnFrmFromIf_Type = Counter32
_MscBtdsMcdnFrmFromIf_Object = MibTableColumn
mscBtdsMcdnFrmFromIf = _MscBtdsMcdnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 14, 1, 2),
    _MscBtdsMcdnFrmFromIf_Type()
)
mscBtdsMcdnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnFrmFromIf.setStatus("mandatory")
_MscBtdsMcdnAborts_Type = Counter32
_MscBtdsMcdnAborts_Object = MibTableColumn
mscBtdsMcdnAborts = _MscBtdsMcdnAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 14, 1, 3),
    _MscBtdsMcdnAborts_Type()
)
mscBtdsMcdnAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnAborts.setStatus("mandatory")
_MscBtdsMcdnCrcErrors_Type = Counter32
_MscBtdsMcdnCrcErrors_Object = MibTableColumn
mscBtdsMcdnCrcErrors = _MscBtdsMcdnCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 14, 1, 4),
    _MscBtdsMcdnCrcErrors_Type()
)
mscBtdsMcdnCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnCrcErrors.setStatus("mandatory")
_MscBtdsMcdnNonOctetErrors_Type = Counter32
_MscBtdsMcdnNonOctetErrors_Object = MibTableColumn
mscBtdsMcdnNonOctetErrors = _MscBtdsMcdnNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 14, 1, 5),
    _MscBtdsMcdnNonOctetErrors_Type()
)
mscBtdsMcdnNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnNonOctetErrors.setStatus("mandatory")
_MscBtdsMcdnOverruns_Type = Counter32
_MscBtdsMcdnOverruns_Object = MibTableColumn
mscBtdsMcdnOverruns = _MscBtdsMcdnOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 14, 1, 6),
    _MscBtdsMcdnOverruns_Type()
)
mscBtdsMcdnOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnOverruns.setStatus("mandatory")
_MscBtdsMcdnLargeFrmErrors_Type = Counter32
_MscBtdsMcdnLargeFrmErrors_Object = MibTableColumn
mscBtdsMcdnLargeFrmErrors = _MscBtdsMcdnLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 14, 1, 8),
    _MscBtdsMcdnLargeFrmErrors_Type()
)
mscBtdsMcdnLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnLargeFrmErrors.setStatus("mandatory")
_MscBtdsMcdnTSlotTable_Object = MibTable
mscBtdsMcdnTSlotTable = _MscBtdsMcdnTSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 286)
)
if mibBuilder.loadTexts:
    mscBtdsMcdnTSlotTable.setStatus("mandatory")
_MscBtdsMcdnTSlotEntry_Object = MibTableRow
mscBtdsMcdnTSlotEntry = _MscBtdsMcdnTSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 286, 1)
)
mscBtdsMcdnTSlotEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsMcdnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsMcdnTSlotIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsMcdnTSlotEntry.setStatus("mandatory")


class _MscBtdsMcdnTSlotIndex_Type(Integer32):
    """Custom type mscBtdsMcdnTSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_MscBtdsMcdnTSlotIndex_Type.__name__ = "Integer32"
_MscBtdsMcdnTSlotIndex_Object = MibTableColumn
mscBtdsMcdnTSlotIndex = _MscBtdsMcdnTSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 286, 1, 1),
    _MscBtdsMcdnTSlotIndex_Type()
)
mscBtdsMcdnTSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscBtdsMcdnTSlotIndex.setStatus("mandatory")


class _MscBtdsMcdnTSlotValue_Type(Integer32):
    """Custom type mscBtdsMcdnTSlotValue based on Integer32"""
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


_MscBtdsMcdnTSlotValue_Type.__name__ = "Integer32"
_MscBtdsMcdnTSlotValue_Object = MibTableColumn
mscBtdsMcdnTSlotValue = _MscBtdsMcdnTSlotValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 6, 286, 1, 2),
    _MscBtdsMcdnTSlotValue_Type()
)
mscBtdsMcdnTSlotValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsMcdnTSlotValue.setStatus("mandatory")
_MscBtdsCidDataTable_Object = MibTable
mscBtdsCidDataTable = _MscBtdsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 100)
)
if mibBuilder.loadTexts:
    mscBtdsCidDataTable.setStatus("mandatory")
_MscBtdsCidDataEntry_Object = MibTableRow
mscBtdsCidDataEntry = _MscBtdsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 100, 1)
)
mscBtdsCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsCidDataEntry.setStatus("mandatory")


class _MscBtdsCustomerIdentifier_Type(Unsigned32):
    """Custom type mscBtdsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscBtdsCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscBtdsCustomerIdentifier_Object = MibTableColumn
mscBtdsCustomerIdentifier = _MscBtdsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 100, 1, 1),
    _MscBtdsCustomerIdentifier_Type()
)
mscBtdsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsCustomerIdentifier.setStatus("mandatory")
_MscBtdsIfEntryTable_Object = MibTable
mscBtdsIfEntryTable = _MscBtdsIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 101)
)
if mibBuilder.loadTexts:
    mscBtdsIfEntryTable.setStatus("mandatory")
_MscBtdsIfEntryEntry_Object = MibTableRow
mscBtdsIfEntryEntry = _MscBtdsIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 101, 1)
)
mscBtdsIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsIfEntryEntry.setStatus("mandatory")


class _MscBtdsIfAdminStatus_Type(Integer32):
    """Custom type mscBtdsIfAdminStatus based on Integer32"""
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


_MscBtdsIfAdminStatus_Type.__name__ = "Integer32"
_MscBtdsIfAdminStatus_Object = MibTableColumn
mscBtdsIfAdminStatus = _MscBtdsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 101, 1, 1),
    _MscBtdsIfAdminStatus_Type()
)
mscBtdsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscBtdsIfAdminStatus.setStatus("mandatory")


class _MscBtdsIfIndex_Type(InterfaceIndex):
    """Custom type mscBtdsIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscBtdsIfIndex_Type.__name__ = "InterfaceIndex"
_MscBtdsIfIndex_Object = MibTableColumn
mscBtdsIfIndex = _MscBtdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 101, 1, 2),
    _MscBtdsIfIndex_Type()
)
mscBtdsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsIfIndex.setStatus("mandatory")
_MscBtdsOperStatusTable_Object = MibTable
mscBtdsOperStatusTable = _MscBtdsOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 102)
)
if mibBuilder.loadTexts:
    mscBtdsOperStatusTable.setStatus("mandatory")
_MscBtdsOperStatusEntry_Object = MibTableRow
mscBtdsOperStatusEntry = _MscBtdsOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 102, 1)
)
mscBtdsOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsOperStatusEntry.setStatus("mandatory")


class _MscBtdsSnmpOperStatus_Type(Integer32):
    """Custom type mscBtdsSnmpOperStatus based on Integer32"""
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


_MscBtdsSnmpOperStatus_Type.__name__ = "Integer32"
_MscBtdsSnmpOperStatus_Object = MibTableColumn
mscBtdsSnmpOperStatus = _MscBtdsSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 102, 1, 1),
    _MscBtdsSnmpOperStatus_Type()
)
mscBtdsSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsSnmpOperStatus.setStatus("mandatory")
_MscBtdsStateTable_Object = MibTable
mscBtdsStateTable = _MscBtdsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103)
)
if mibBuilder.loadTexts:
    mscBtdsStateTable.setStatus("mandatory")
_MscBtdsStateEntry_Object = MibTableRow
mscBtdsStateEntry = _MscBtdsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1)
)
mscBtdsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsStateEntry.setStatus("mandatory")


class _MscBtdsAdminState_Type(Integer32):
    """Custom type mscBtdsAdminState based on Integer32"""
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


_MscBtdsAdminState_Type.__name__ = "Integer32"
_MscBtdsAdminState_Object = MibTableColumn
mscBtdsAdminState = _MscBtdsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1, 1),
    _MscBtdsAdminState_Type()
)
mscBtdsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsAdminState.setStatus("mandatory")


class _MscBtdsOperationalState_Type(Integer32):
    """Custom type mscBtdsOperationalState based on Integer32"""
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


_MscBtdsOperationalState_Type.__name__ = "Integer32"
_MscBtdsOperationalState_Object = MibTableColumn
mscBtdsOperationalState = _MscBtdsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1, 2),
    _MscBtdsOperationalState_Type()
)
mscBtdsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsOperationalState.setStatus("mandatory")


class _MscBtdsUsageState_Type(Integer32):
    """Custom type mscBtdsUsageState based on Integer32"""
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


_MscBtdsUsageState_Type.__name__ = "Integer32"
_MscBtdsUsageState_Object = MibTableColumn
mscBtdsUsageState = _MscBtdsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1, 3),
    _MscBtdsUsageState_Type()
)
mscBtdsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsUsageState.setStatus("mandatory")


class _MscBtdsAvailabilityStatus_Type(OctetString):
    """Custom type mscBtdsAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscBtdsAvailabilityStatus_Type.__name__ = "OctetString"
_MscBtdsAvailabilityStatus_Object = MibTableColumn
mscBtdsAvailabilityStatus = _MscBtdsAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1, 4),
    _MscBtdsAvailabilityStatus_Type()
)
mscBtdsAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsAvailabilityStatus.setStatus("mandatory")


class _MscBtdsProceduralStatus_Type(OctetString):
    """Custom type mscBtdsProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscBtdsProceduralStatus_Type.__name__ = "OctetString"
_MscBtdsProceduralStatus_Object = MibTableColumn
mscBtdsProceduralStatus = _MscBtdsProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1, 5),
    _MscBtdsProceduralStatus_Type()
)
mscBtdsProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsProceduralStatus.setStatus("mandatory")


class _MscBtdsControlStatus_Type(OctetString):
    """Custom type mscBtdsControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscBtdsControlStatus_Type.__name__ = "OctetString"
_MscBtdsControlStatus_Object = MibTableColumn
mscBtdsControlStatus = _MscBtdsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1, 6),
    _MscBtdsControlStatus_Type()
)
mscBtdsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsControlStatus.setStatus("mandatory")


class _MscBtdsAlarmStatus_Type(OctetString):
    """Custom type mscBtdsAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscBtdsAlarmStatus_Type.__name__ = "OctetString"
_MscBtdsAlarmStatus_Object = MibTableColumn
mscBtdsAlarmStatus = _MscBtdsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1, 7),
    _MscBtdsAlarmStatus_Type()
)
mscBtdsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsAlarmStatus.setStatus("mandatory")


class _MscBtdsStandbyStatus_Type(Integer32):
    """Custom type mscBtdsStandbyStatus based on Integer32"""
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


_MscBtdsStandbyStatus_Type.__name__ = "Integer32"
_MscBtdsStandbyStatus_Object = MibTableColumn
mscBtdsStandbyStatus = _MscBtdsStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1, 8),
    _MscBtdsStandbyStatus_Type()
)
mscBtdsStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsStandbyStatus.setStatus("mandatory")


class _MscBtdsUnknownStatus_Type(Integer32):
    """Custom type mscBtdsUnknownStatus based on Integer32"""
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


_MscBtdsUnknownStatus_Type.__name__ = "Integer32"
_MscBtdsUnknownStatus_Object = MibTableColumn
mscBtdsUnknownStatus = _MscBtdsUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 103, 1, 9),
    _MscBtdsUnknownStatus_Type()
)
mscBtdsUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsUnknownStatus.setStatus("mandatory")
_MscBtdsOperationalTable_Object = MibTable
mscBtdsOperationalTable = _MscBtdsOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 105)
)
if mibBuilder.loadTexts:
    mscBtdsOperationalTable.setStatus("mandatory")
_MscBtdsOperationalEntry_Object = MibTableRow
mscBtdsOperationalEntry = _MscBtdsOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 105, 1)
)
mscBtdsOperationalEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-BitTransparentMIB", "mscBtdsIndex"),
)
if mibBuilder.loadTexts:
    mscBtdsOperationalEntry.setStatus("mandatory")


class _MscBtdsServiceFailureReason_Type(OctetString):
    """Custom type mscBtdsServiceFailureReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscBtdsServiceFailureReason_Type.__name__ = "OctetString"
_MscBtdsServiceFailureReason_Object = MibTableColumn
mscBtdsServiceFailureReason = _MscBtdsServiceFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 81, 105, 1, 1),
    _MscBtdsServiceFailureReason_Type()
)
mscBtdsServiceFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscBtdsServiceFailureReason.setStatus("mandatory")
_BitTransparentMIB_ObjectIdentity = ObjectIdentity
bitTransparentMIB = _BitTransparentMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 46)
)
_BitTransparentGroup_ObjectIdentity = ObjectIdentity
bitTransparentGroup = _BitTransparentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 46, 1)
)
_BitTransparentGroupCA_ObjectIdentity = ObjectIdentity
bitTransparentGroupCA = _BitTransparentGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 46, 1, 1)
)
_BitTransparentGroupCA02_ObjectIdentity = ObjectIdentity
bitTransparentGroupCA02 = _BitTransparentGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 46, 1, 1, 3)
)
_BitTransparentGroupCA02A_ObjectIdentity = ObjectIdentity
bitTransparentGroupCA02A = _BitTransparentGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 46, 1, 1, 3, 2)
)
_BitTransparentCapabilities_ObjectIdentity = ObjectIdentity
bitTransparentCapabilities = _BitTransparentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 46, 3)
)
_BitTransparentCapabilitiesCA_ObjectIdentity = ObjectIdentity
bitTransparentCapabilitiesCA = _BitTransparentCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 46, 3, 1)
)
_BitTransparentCapabilitiesCA02_ObjectIdentity = ObjectIdentity
bitTransparentCapabilitiesCA02 = _BitTransparentCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 46, 3, 1, 3)
)
_BitTransparentCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
bitTransparentCapabilitiesCA02A = _BitTransparentCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 46, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-BitTransparentMIB",
    **{"mscBtds": mscBtds,
       "mscBtdsRowStatusTable": mscBtdsRowStatusTable,
       "mscBtdsRowStatusEntry": mscBtdsRowStatusEntry,
       "mscBtdsRowStatus": mscBtdsRowStatus,
       "mscBtdsComponentName": mscBtdsComponentName,
       "mscBtdsStorageType": mscBtdsStorageType,
       "mscBtdsIndex": mscBtdsIndex,
       "mscBtdsFramer": mscBtdsFramer,
       "mscBtdsFramerRowStatusTable": mscBtdsFramerRowStatusTable,
       "mscBtdsFramerRowStatusEntry": mscBtdsFramerRowStatusEntry,
       "mscBtdsFramerRowStatus": mscBtdsFramerRowStatus,
       "mscBtdsFramerComponentName": mscBtdsFramerComponentName,
       "mscBtdsFramerStorageType": mscBtdsFramerStorageType,
       "mscBtdsFramerIndex": mscBtdsFramerIndex,
       "mscBtdsFramerProvTable": mscBtdsFramerProvTable,
       "mscBtdsFramerProvEntry": mscBtdsFramerProvEntry,
       "mscBtdsFramerInterfaceName": mscBtdsFramerInterfaceName,
       "mscBtdsFramerChannelTable": mscBtdsFramerChannelTable,
       "mscBtdsFramerChannelEntry": mscBtdsFramerChannelEntry,
       "mscBtdsFramerProtocol": mscBtdsFramerProtocol,
       "mscBtdsFramerNumOfIdleBytesToMonitor": mscBtdsFramerNumOfIdleBytesToMonitor,
       "mscBtdsFramerIdlePattern": mscBtdsFramerIdlePattern,
       "mscBtdsFramerTimeSlotAlignment": mscBtdsFramerTimeSlotAlignment,
       "mscBtdsFramerInsertedOutputDelay": mscBtdsFramerInsertedOutputDelay,
       "mscBtdsFramerBtdsCellSize": mscBtdsFramerBtdsCellSize,
       "mscBtdsFramerStateTable": mscBtdsFramerStateTable,
       "mscBtdsFramerStateEntry": mscBtdsFramerStateEntry,
       "mscBtdsFramerAdminState": mscBtdsFramerAdminState,
       "mscBtdsFramerOperationalState": mscBtdsFramerOperationalState,
       "mscBtdsFramerUsageState": mscBtdsFramerUsageState,
       "mscBtdsFramerStatsTable": mscBtdsFramerStatsTable,
       "mscBtdsFramerStatsEntry": mscBtdsFramerStatsEntry,
       "mscBtdsFramerFrmFromIf": mscBtdsFramerFrmFromIf,
       "mscBtdsFramerSuppressedFrames": mscBtdsFramerSuppressedFrames,
       "mscBtdsFramerFrmToIf": mscBtdsFramerFrmToIf,
       "mscBtdsFramerLrcErrors": mscBtdsFramerLrcErrors,
       "mscBtdsFramerFrmLostInNetwork": mscBtdsFramerFrmLostInNetwork,
       "mscBtdsFramerFrmUnderRuns": mscBtdsFramerFrmUnderRuns,
       "mscBtdsFramerFrmDumped": mscBtdsFramerFrmDumped,
       "mscBtdsPlc": mscBtdsPlc,
       "mscBtdsPlcRowStatusTable": mscBtdsPlcRowStatusTable,
       "mscBtdsPlcRowStatusEntry": mscBtdsPlcRowStatusEntry,
       "mscBtdsPlcRowStatus": mscBtdsPlcRowStatus,
       "mscBtdsPlcComponentName": mscBtdsPlcComponentName,
       "mscBtdsPlcStorageType": mscBtdsPlcStorageType,
       "mscBtdsPlcIndex": mscBtdsPlcIndex,
       "mscBtdsPlcProvTable": mscBtdsPlcProvTable,
       "mscBtdsPlcProvEntry": mscBtdsPlcProvEntry,
       "mscBtdsPlcRemoteName": mscBtdsPlcRemoteName,
       "mscBtdsPlcSetupPriority": mscBtdsPlcSetupPriority,
       "mscBtdsPlcHoldingPriority": mscBtdsPlcHoldingPriority,
       "mscBtdsPlcRequiredTxBandwidth": mscBtdsPlcRequiredTxBandwidth,
       "mscBtdsPlcRequiredRxBandwidth": mscBtdsPlcRequiredRxBandwidth,
       "mscBtdsPlcRequiredTrafficType": mscBtdsPlcRequiredTrafficType,
       "mscBtdsPlcPermittedTrunkTypes": mscBtdsPlcPermittedTrunkTypes,
       "mscBtdsPlcRequiredSecurity": mscBtdsPlcRequiredSecurity,
       "mscBtdsPlcRequiredCustomerParm": mscBtdsPlcRequiredCustomerParm,
       "mscBtdsPlcPathAttributeToMinimize": mscBtdsPlcPathAttributeToMinimize,
       "mscBtdsPlcMaximumAcceptableCost": mscBtdsPlcMaximumAcceptableCost,
       "mscBtdsPlcMaximumAcceptableDelay": mscBtdsPlcMaximumAcceptableDelay,
       "mscBtdsPlcEmissionPriority": mscBtdsPlcEmissionPriority,
       "mscBtdsPlcDiscardPriority": mscBtdsPlcDiscardPriority,
       "mscBtdsPlcPathType": mscBtdsPlcPathType,
       "mscBtdsPlcPathFailureAction": mscBtdsPlcPathFailureAction,
       "mscBtdsPlcBumpPreference": mscBtdsPlcBumpPreference,
       "mscBtdsPlcOptimization": mscBtdsPlcOptimization,
       "mscBtdsPlcAddressToCall": mscBtdsPlcAddressToCall,
       "mscBtdsPlcLocalAddress": mscBtdsPlcLocalAddress,
       "mscBtdsPlcMaximumAcceptableGatewayCost": mscBtdsPlcMaximumAcceptableGatewayCost,
       "mscBtdsPlcMpathTable": mscBtdsPlcMpathTable,
       "mscBtdsPlcMpathEntry": mscBtdsPlcMpathEntry,
       "mscBtdsPlcMpathIndex": mscBtdsPlcMpathIndex,
       "mscBtdsPlcMpathValue": mscBtdsPlcMpathValue,
       "mscBtdsLCo": mscBtdsLCo,
       "mscBtdsLCoRowStatusTable": mscBtdsLCoRowStatusTable,
       "mscBtdsLCoRowStatusEntry": mscBtdsLCoRowStatusEntry,
       "mscBtdsLCoRowStatus": mscBtdsLCoRowStatus,
       "mscBtdsLCoComponentName": mscBtdsLCoComponentName,
       "mscBtdsLCoStorageType": mscBtdsLCoStorageType,
       "mscBtdsLCoIndex": mscBtdsLCoIndex,
       "mscBtdsLCoPathDataTable": mscBtdsLCoPathDataTable,
       "mscBtdsLCoPathDataEntry": mscBtdsLCoPathDataEntry,
       "mscBtdsLCoState": mscBtdsLCoState,
       "mscBtdsLCoOverrideRemoteName": mscBtdsLCoOverrideRemoteName,
       "mscBtdsLCoEnd": mscBtdsLCoEnd,
       "mscBtdsLCoCostMetric": mscBtdsLCoCostMetric,
       "mscBtdsLCoDelayMetric": mscBtdsLCoDelayMetric,
       "mscBtdsLCoRoundTripDelay": mscBtdsLCoRoundTripDelay,
       "mscBtdsLCoSetupPriority": mscBtdsLCoSetupPriority,
       "mscBtdsLCoHoldingPriority": mscBtdsLCoHoldingPriority,
       "mscBtdsLCoRequiredTxBandwidth": mscBtdsLCoRequiredTxBandwidth,
       "mscBtdsLCoRequiredRxBandwidth": mscBtdsLCoRequiredRxBandwidth,
       "mscBtdsLCoRequiredTrafficType": mscBtdsLCoRequiredTrafficType,
       "mscBtdsLCoPermittedTrunkTypes": mscBtdsLCoPermittedTrunkTypes,
       "mscBtdsLCoRequiredSecurity": mscBtdsLCoRequiredSecurity,
       "mscBtdsLCoRequiredCustomerParameter": mscBtdsLCoRequiredCustomerParameter,
       "mscBtdsLCoEmissionPriority": mscBtdsLCoEmissionPriority,
       "mscBtdsLCoDiscardPriority": mscBtdsLCoDiscardPriority,
       "mscBtdsLCoPathType": mscBtdsLCoPathType,
       "mscBtdsLCoRetryCount": mscBtdsLCoRetryCount,
       "mscBtdsLCoPathFailureCount": mscBtdsLCoPathFailureCount,
       "mscBtdsLCoReasonForNoRoute": mscBtdsLCoReasonForNoRoute,
       "mscBtdsLCoLastTearDownReason": mscBtdsLCoLastTearDownReason,
       "mscBtdsLCoPathFailureAction": mscBtdsLCoPathFailureAction,
       "mscBtdsLCoBumpPreference": mscBtdsLCoBumpPreference,
       "mscBtdsLCoOptimization": mscBtdsLCoOptimization,
       "mscBtdsLCoPathUpDateTime": mscBtdsLCoPathUpDateTime,
       "mscBtdsLCoStatsTable": mscBtdsLCoStatsTable,
       "mscBtdsLCoStatsEntry": mscBtdsLCoStatsEntry,
       "mscBtdsLCoPktsToNetwork": mscBtdsLCoPktsToNetwork,
       "mscBtdsLCoBytesToNetwork": mscBtdsLCoBytesToNetwork,
       "mscBtdsLCoPktsFromNetwork": mscBtdsLCoPktsFromNetwork,
       "mscBtdsLCoBytesFromNetwork": mscBtdsLCoBytesFromNetwork,
       "mscBtdsLCoPathTable": mscBtdsLCoPathTable,
       "mscBtdsLCoPathEntry": mscBtdsLCoPathEntry,
       "mscBtdsLCoPathValue": mscBtdsLCoPathValue,
       "mscBtdsDpnss1": mscBtdsDpnss1,
       "mscBtdsDpnss1RowStatusTable": mscBtdsDpnss1RowStatusTable,
       "mscBtdsDpnss1RowStatusEntry": mscBtdsDpnss1RowStatusEntry,
       "mscBtdsDpnss1RowStatus": mscBtdsDpnss1RowStatus,
       "mscBtdsDpnss1ComponentName": mscBtdsDpnss1ComponentName,
       "mscBtdsDpnss1StorageType": mscBtdsDpnss1StorageType,
       "mscBtdsDpnss1Index": mscBtdsDpnss1Index,
       "mscBtdsDpnss1ProvTable": mscBtdsDpnss1ProvTable,
       "mscBtdsDpnss1ProvEntry": mscBtdsDpnss1ProvEntry,
       "mscBtdsDpnss1TimeslotsX": mscBtdsDpnss1TimeslotsX,
       "mscBtdsDpnss1VdcdTable": mscBtdsDpnss1VdcdTable,
       "mscBtdsDpnss1VdcdEntry": mscBtdsDpnss1VdcdEntry,
       "mscBtdsDpnss1NewVoiceCalls": mscBtdsDpnss1NewVoiceCalls,
       "mscBtdsDpnss1NewDataCalls": mscBtdsDpnss1NewDataCalls,
       "mscBtdsDpnss1VoiceToData": mscBtdsDpnss1VoiceToData,
       "mscBtdsDpnss1DataToVoice": mscBtdsDpnss1DataToVoice,
       "mscBtdsDpnss1CallClears": mscBtdsDpnss1CallClears,
       "mscBtdsDpnss1FramesTable": mscBtdsDpnss1FramesTable,
       "mscBtdsDpnss1FramesEntry": mscBtdsDpnss1FramesEntry,
       "mscBtdsDpnss1FrmProcessed": mscBtdsDpnss1FrmProcessed,
       "mscBtdsDpnss1FrmInvalid": mscBtdsDpnss1FrmInvalid,
       "mscBtdsDpnss1HdlcTable": mscBtdsDpnss1HdlcTable,
       "mscBtdsDpnss1HdlcEntry": mscBtdsDpnss1HdlcEntry,
       "mscBtdsDpnss1FrmFromIf": mscBtdsDpnss1FrmFromIf,
       "mscBtdsDpnss1Aborts": mscBtdsDpnss1Aborts,
       "mscBtdsDpnss1CrcErrors": mscBtdsDpnss1CrcErrors,
       "mscBtdsDpnss1NonOctetErrors": mscBtdsDpnss1NonOctetErrors,
       "mscBtdsDpnss1Overruns": mscBtdsDpnss1Overruns,
       "mscBtdsDpnss1LargeFrmErrors": mscBtdsDpnss1LargeFrmErrors,
       "mscBtdsDpnss1TSlotTable": mscBtdsDpnss1TSlotTable,
       "mscBtdsDpnss1TSlotEntry": mscBtdsDpnss1TSlotEntry,
       "mscBtdsDpnss1TSlotIndex": mscBtdsDpnss1TSlotIndex,
       "mscBtdsDpnss1TSlotValue": mscBtdsDpnss1TSlotValue,
       "mscBtdsMcdn": mscBtdsMcdn,
       "mscBtdsMcdnRowStatusTable": mscBtdsMcdnRowStatusTable,
       "mscBtdsMcdnRowStatusEntry": mscBtdsMcdnRowStatusEntry,
       "mscBtdsMcdnRowStatus": mscBtdsMcdnRowStatus,
       "mscBtdsMcdnComponentName": mscBtdsMcdnComponentName,
       "mscBtdsMcdnStorageType": mscBtdsMcdnStorageType,
       "mscBtdsMcdnIndex": mscBtdsMcdnIndex,
       "mscBtdsMcdnProvTable": mscBtdsMcdnProvTable,
       "mscBtdsMcdnProvEntry": mscBtdsMcdnProvEntry,
       "mscBtdsMcdnAdjPbxSide": mscBtdsMcdnAdjPbxSide,
       "mscBtdsMcdnVdcdTable": mscBtdsMcdnVdcdTable,
       "mscBtdsMcdnVdcdEntry": mscBtdsMcdnVdcdEntry,
       "mscBtdsMcdnNewVoiceCalls": mscBtdsMcdnNewVoiceCalls,
       "mscBtdsMcdnNewDataCalls": mscBtdsMcdnNewDataCalls,
       "mscBtdsMcdnVoiceToData": mscBtdsMcdnVoiceToData,
       "mscBtdsMcdnDataToVoice": mscBtdsMcdnDataToVoice,
       "mscBtdsMcdnCallClears": mscBtdsMcdnCallClears,
       "mscBtdsMcdnFramesTable": mscBtdsMcdnFramesTable,
       "mscBtdsMcdnFramesEntry": mscBtdsMcdnFramesEntry,
       "mscBtdsMcdnFrmProcessed": mscBtdsMcdnFrmProcessed,
       "mscBtdsMcdnFrmInvalid": mscBtdsMcdnFrmInvalid,
       "mscBtdsMcdnHdlcTable": mscBtdsMcdnHdlcTable,
       "mscBtdsMcdnHdlcEntry": mscBtdsMcdnHdlcEntry,
       "mscBtdsMcdnFrmFromIf": mscBtdsMcdnFrmFromIf,
       "mscBtdsMcdnAborts": mscBtdsMcdnAborts,
       "mscBtdsMcdnCrcErrors": mscBtdsMcdnCrcErrors,
       "mscBtdsMcdnNonOctetErrors": mscBtdsMcdnNonOctetErrors,
       "mscBtdsMcdnOverruns": mscBtdsMcdnOverruns,
       "mscBtdsMcdnLargeFrmErrors": mscBtdsMcdnLargeFrmErrors,
       "mscBtdsMcdnTSlotTable": mscBtdsMcdnTSlotTable,
       "mscBtdsMcdnTSlotEntry": mscBtdsMcdnTSlotEntry,
       "mscBtdsMcdnTSlotIndex": mscBtdsMcdnTSlotIndex,
       "mscBtdsMcdnTSlotValue": mscBtdsMcdnTSlotValue,
       "mscBtdsCidDataTable": mscBtdsCidDataTable,
       "mscBtdsCidDataEntry": mscBtdsCidDataEntry,
       "mscBtdsCustomerIdentifier": mscBtdsCustomerIdentifier,
       "mscBtdsIfEntryTable": mscBtdsIfEntryTable,
       "mscBtdsIfEntryEntry": mscBtdsIfEntryEntry,
       "mscBtdsIfAdminStatus": mscBtdsIfAdminStatus,
       "mscBtdsIfIndex": mscBtdsIfIndex,
       "mscBtdsOperStatusTable": mscBtdsOperStatusTable,
       "mscBtdsOperStatusEntry": mscBtdsOperStatusEntry,
       "mscBtdsSnmpOperStatus": mscBtdsSnmpOperStatus,
       "mscBtdsStateTable": mscBtdsStateTable,
       "mscBtdsStateEntry": mscBtdsStateEntry,
       "mscBtdsAdminState": mscBtdsAdminState,
       "mscBtdsOperationalState": mscBtdsOperationalState,
       "mscBtdsUsageState": mscBtdsUsageState,
       "mscBtdsAvailabilityStatus": mscBtdsAvailabilityStatus,
       "mscBtdsProceduralStatus": mscBtdsProceduralStatus,
       "mscBtdsControlStatus": mscBtdsControlStatus,
       "mscBtdsAlarmStatus": mscBtdsAlarmStatus,
       "mscBtdsStandbyStatus": mscBtdsStandbyStatus,
       "mscBtdsUnknownStatus": mscBtdsUnknownStatus,
       "mscBtdsOperationalTable": mscBtdsOperationalTable,
       "mscBtdsOperationalEntry": mscBtdsOperationalEntry,
       "mscBtdsServiceFailureReason": mscBtdsServiceFailureReason,
       "bitTransparentMIB": bitTransparentMIB,
       "bitTransparentGroup": bitTransparentGroup,
       "bitTransparentGroupCA": bitTransparentGroupCA,
       "bitTransparentGroupCA02": bitTransparentGroupCA02,
       "bitTransparentGroupCA02A": bitTransparentGroupCA02A,
       "bitTransparentCapabilities": bitTransparentCapabilities,
       "bitTransparentCapabilitiesCA": bitTransparentCapabilitiesCA,
       "bitTransparentCapabilitiesCA02": bitTransparentCapabilitiesCA02,
       "bitTransparentCapabilitiesCA02A": bitTransparentCapabilitiesCA02A}
)
