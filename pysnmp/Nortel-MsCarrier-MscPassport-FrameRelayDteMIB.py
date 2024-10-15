# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrameRelayDteMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayDteMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:25 2024
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

(DashedHexString,
 EnterpriseDateAndTime,
 HexString,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "DashedHexString",
    "EnterpriseDateAndTime",
    "HexString",
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

_MscFrDte_ObjectIdentity = ObjectIdentity
mscFrDte = _MscFrDte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101)
)
_MscFrDteRowStatusTable_Object = MibTable
mscFrDteRowStatusTable = _MscFrDteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 1)
)
if mibBuilder.loadTexts:
    mscFrDteRowStatusTable.setStatus("mandatory")
_MscFrDteRowStatusEntry_Object = MibTableRow
mscFrDteRowStatusEntry = _MscFrDteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 1, 1)
)
mscFrDteRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRowStatusEntry.setStatus("mandatory")
_MscFrDteRowStatus_Type = RowStatus
_MscFrDteRowStatus_Object = MibTableColumn
mscFrDteRowStatus = _MscFrDteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 1, 1, 1),
    _MscFrDteRowStatus_Type()
)
mscFrDteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteRowStatus.setStatus("mandatory")
_MscFrDteComponentName_Type = DisplayString
_MscFrDteComponentName_Object = MibTableColumn
mscFrDteComponentName = _MscFrDteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 1, 1, 2),
    _MscFrDteComponentName_Type()
)
mscFrDteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteComponentName.setStatus("mandatory")
_MscFrDteStorageType_Type = StorageType
_MscFrDteStorageType_Object = MibTableColumn
mscFrDteStorageType = _MscFrDteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 1, 1, 4),
    _MscFrDteStorageType_Type()
)
mscFrDteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStorageType.setStatus("mandatory")


class _MscFrDteIndex_Type(Integer32):
    """Custom type mscFrDteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrDteIndex_Type.__name__ = "Integer32"
_MscFrDteIndex_Object = MibTableColumn
mscFrDteIndex = _MscFrDteIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 1, 1, 10),
    _MscFrDteIndex_Type()
)
mscFrDteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteIndex.setStatus("mandatory")
_MscFrDteFramer_ObjectIdentity = ObjectIdentity
mscFrDteFramer = _MscFrDteFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2)
)
_MscFrDteFramerRowStatusTable_Object = MibTable
mscFrDteFramerRowStatusTable = _MscFrDteFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrDteFramerRowStatusTable.setStatus("mandatory")
_MscFrDteFramerRowStatusEntry_Object = MibTableRow
mscFrDteFramerRowStatusEntry = _MscFrDteFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 1, 1)
)
mscFrDteFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteFramerRowStatusEntry.setStatus("mandatory")
_MscFrDteFramerRowStatus_Type = RowStatus
_MscFrDteFramerRowStatus_Object = MibTableColumn
mscFrDteFramerRowStatus = _MscFrDteFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 1, 1, 1),
    _MscFrDteFramerRowStatus_Type()
)
mscFrDteFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteFramerRowStatus.setStatus("mandatory")
_MscFrDteFramerComponentName_Type = DisplayString
_MscFrDteFramerComponentName_Object = MibTableColumn
mscFrDteFramerComponentName = _MscFrDteFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 1, 1, 2),
    _MscFrDteFramerComponentName_Type()
)
mscFrDteFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerComponentName.setStatus("mandatory")
_MscFrDteFramerStorageType_Type = StorageType
_MscFrDteFramerStorageType_Object = MibTableColumn
mscFrDteFramerStorageType = _MscFrDteFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 1, 1, 4),
    _MscFrDteFramerStorageType_Type()
)
mscFrDteFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerStorageType.setStatus("mandatory")
_MscFrDteFramerIndex_Type = NonReplicated
_MscFrDteFramerIndex_Object = MibTableColumn
mscFrDteFramerIndex = _MscFrDteFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 1, 1, 10),
    _MscFrDteFramerIndex_Type()
)
mscFrDteFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteFramerIndex.setStatus("mandatory")
_MscFrDteFramerProvTable_Object = MibTable
mscFrDteFramerProvTable = _MscFrDteFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrDteFramerProvTable.setStatus("mandatory")
_MscFrDteFramerProvEntry_Object = MibTableRow
mscFrDteFramerProvEntry = _MscFrDteFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 10, 1)
)
mscFrDteFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteFramerProvEntry.setStatus("mandatory")
_MscFrDteFramerInterfaceName_Type = Link
_MscFrDteFramerInterfaceName_Object = MibTableColumn
mscFrDteFramerInterfaceName = _MscFrDteFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 10, 1, 1),
    _MscFrDteFramerInterfaceName_Type()
)
mscFrDteFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteFramerInterfaceName.setStatus("mandatory")
_MscFrDteFramerStateTable_Object = MibTable
mscFrDteFramerStateTable = _MscFrDteFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 12)
)
if mibBuilder.loadTexts:
    mscFrDteFramerStateTable.setStatus("mandatory")
_MscFrDteFramerStateEntry_Object = MibTableRow
mscFrDteFramerStateEntry = _MscFrDteFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 12, 1)
)
mscFrDteFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteFramerStateEntry.setStatus("mandatory")


class _MscFrDteFramerAdminState_Type(Integer32):
    """Custom type mscFrDteFramerAdminState based on Integer32"""
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


_MscFrDteFramerAdminState_Type.__name__ = "Integer32"
_MscFrDteFramerAdminState_Object = MibTableColumn
mscFrDteFramerAdminState = _MscFrDteFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 12, 1, 1),
    _MscFrDteFramerAdminState_Type()
)
mscFrDteFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerAdminState.setStatus("mandatory")


class _MscFrDteFramerOperationalState_Type(Integer32):
    """Custom type mscFrDteFramerOperationalState based on Integer32"""
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


_MscFrDteFramerOperationalState_Type.__name__ = "Integer32"
_MscFrDteFramerOperationalState_Object = MibTableColumn
mscFrDteFramerOperationalState = _MscFrDteFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 12, 1, 2),
    _MscFrDteFramerOperationalState_Type()
)
mscFrDteFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerOperationalState.setStatus("mandatory")


class _MscFrDteFramerUsageState_Type(Integer32):
    """Custom type mscFrDteFramerUsageState based on Integer32"""
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


_MscFrDteFramerUsageState_Type.__name__ = "Integer32"
_MscFrDteFramerUsageState_Object = MibTableColumn
mscFrDteFramerUsageState = _MscFrDteFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 12, 1, 3),
    _MscFrDteFramerUsageState_Type()
)
mscFrDteFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerUsageState.setStatus("mandatory")
_MscFrDteFramerStatsTable_Object = MibTable
mscFrDteFramerStatsTable = _MscFrDteFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13)
)
if mibBuilder.loadTexts:
    mscFrDteFramerStatsTable.setStatus("mandatory")
_MscFrDteFramerStatsEntry_Object = MibTableRow
mscFrDteFramerStatsEntry = _MscFrDteFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1)
)
mscFrDteFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteFramerStatsEntry.setStatus("mandatory")
_MscFrDteFramerFrmToIf_Type = Counter32
_MscFrDteFramerFrmToIf_Object = MibTableColumn
mscFrDteFramerFrmToIf = _MscFrDteFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1, 1),
    _MscFrDteFramerFrmToIf_Type()
)
mscFrDteFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerFrmToIf.setStatus("mandatory")
_MscFrDteFramerFrmFromIf_Type = Counter32
_MscFrDteFramerFrmFromIf_Object = MibTableColumn
mscFrDteFramerFrmFromIf = _MscFrDteFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1, 2),
    _MscFrDteFramerFrmFromIf_Type()
)
mscFrDteFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerFrmFromIf.setStatus("mandatory")
_MscFrDteFramerAborts_Type = Counter32
_MscFrDteFramerAborts_Object = MibTableColumn
mscFrDteFramerAborts = _MscFrDteFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1, 3),
    _MscFrDteFramerAborts_Type()
)
mscFrDteFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerAborts.setStatus("mandatory")
_MscFrDteFramerCrcErrors_Type = Counter32
_MscFrDteFramerCrcErrors_Object = MibTableColumn
mscFrDteFramerCrcErrors = _MscFrDteFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1, 4),
    _MscFrDteFramerCrcErrors_Type()
)
mscFrDteFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerCrcErrors.setStatus("mandatory")
_MscFrDteFramerLrcErrors_Type = Counter32
_MscFrDteFramerLrcErrors_Object = MibTableColumn
mscFrDteFramerLrcErrors = _MscFrDteFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1, 5),
    _MscFrDteFramerLrcErrors_Type()
)
mscFrDteFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerLrcErrors.setStatus("mandatory")
_MscFrDteFramerNonOctetErrors_Type = Counter32
_MscFrDteFramerNonOctetErrors_Object = MibTableColumn
mscFrDteFramerNonOctetErrors = _MscFrDteFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1, 6),
    _MscFrDteFramerNonOctetErrors_Type()
)
mscFrDteFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerNonOctetErrors.setStatus("mandatory")
_MscFrDteFramerOverruns_Type = Counter32
_MscFrDteFramerOverruns_Object = MibTableColumn
mscFrDteFramerOverruns = _MscFrDteFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1, 7),
    _MscFrDteFramerOverruns_Type()
)
mscFrDteFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerOverruns.setStatus("mandatory")
_MscFrDteFramerUnderruns_Type = Counter32
_MscFrDteFramerUnderruns_Object = MibTableColumn
mscFrDteFramerUnderruns = _MscFrDteFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1, 8),
    _MscFrDteFramerUnderruns_Type()
)
mscFrDteFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerUnderruns.setStatus("mandatory")
_MscFrDteFramerLargeFrmErrors_Type = Counter32
_MscFrDteFramerLargeFrmErrors_Object = MibTableColumn
mscFrDteFramerLargeFrmErrors = _MscFrDteFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 13, 1, 9),
    _MscFrDteFramerLargeFrmErrors_Type()
)
mscFrDteFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerLargeFrmErrors.setStatus("mandatory")
_MscFrDteFramerUtilTable_Object = MibTable
mscFrDteFramerUtilTable = _MscFrDteFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 14)
)
if mibBuilder.loadTexts:
    mscFrDteFramerUtilTable.setStatus("mandatory")
_MscFrDteFramerUtilEntry_Object = MibTableRow
mscFrDteFramerUtilEntry = _MscFrDteFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 14, 1)
)
mscFrDteFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteFramerUtilEntry.setStatus("mandatory")


class _MscFrDteFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscFrDteFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrDteFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscFrDteFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscFrDteFramerNormPrioLinkUtilToIf = _MscFrDteFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 14, 1, 1),
    _MscFrDteFramerNormPrioLinkUtilToIf_Type()
)
mscFrDteFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscFrDteFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscFrDteFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrDteFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscFrDteFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscFrDteFramerNormPrioLinkUtilFromIf = _MscFrDteFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 2, 14, 1, 3),
    _MscFrDteFramerNormPrioLinkUtilFromIf_Type()
)
mscFrDteFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MscFrDteLmi_ObjectIdentity = ObjectIdentity
mscFrDteLmi = _MscFrDteLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3)
)
_MscFrDteLmiRowStatusTable_Object = MibTable
mscFrDteLmiRowStatusTable = _MscFrDteLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrDteLmiRowStatusTable.setStatus("mandatory")
_MscFrDteLmiRowStatusEntry_Object = MibTableRow
mscFrDteLmiRowStatusEntry = _MscFrDteLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 1, 1)
)
mscFrDteLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteLmiRowStatusEntry.setStatus("mandatory")
_MscFrDteLmiRowStatus_Type = RowStatus
_MscFrDteLmiRowStatus_Object = MibTableColumn
mscFrDteLmiRowStatus = _MscFrDteLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 1, 1, 1),
    _MscFrDteLmiRowStatus_Type()
)
mscFrDteLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLmiRowStatus.setStatus("mandatory")
_MscFrDteLmiComponentName_Type = DisplayString
_MscFrDteLmiComponentName_Object = MibTableColumn
mscFrDteLmiComponentName = _MscFrDteLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 1, 1, 2),
    _MscFrDteLmiComponentName_Type()
)
mscFrDteLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLmiComponentName.setStatus("mandatory")
_MscFrDteLmiStorageType_Type = StorageType
_MscFrDteLmiStorageType_Object = MibTableColumn
mscFrDteLmiStorageType = _MscFrDteLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 1, 1, 4),
    _MscFrDteLmiStorageType_Type()
)
mscFrDteLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLmiStorageType.setStatus("mandatory")
_MscFrDteLmiIndex_Type = NonReplicated
_MscFrDteLmiIndex_Object = MibTableColumn
mscFrDteLmiIndex = _MscFrDteLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 1, 1, 10),
    _MscFrDteLmiIndex_Type()
)
mscFrDteLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteLmiIndex.setStatus("mandatory")
_MscFrDteLmiProvTable_Object = MibTable
mscFrDteLmiProvTable = _MscFrDteLmiProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrDteLmiProvTable.setStatus("mandatory")
_MscFrDteLmiProvEntry_Object = MibTableRow
mscFrDteLmiProvEntry = _MscFrDteLmiProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 10, 1)
)
mscFrDteLmiProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteLmiProvEntry.setStatus("mandatory")


class _MscFrDteLmiProcedures_Type(Integer32):
    """Custom type mscFrDteLmiProcedures based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 3),
          ("ccitt", 5),
          ("none", 1),
          ("vendorForum", 2))
    )


_MscFrDteLmiProcedures_Type.__name__ = "Integer32"
_MscFrDteLmiProcedures_Object = MibTableColumn
mscFrDteLmiProcedures = _MscFrDteLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 10, 1, 1),
    _MscFrDteLmiProcedures_Type()
)
mscFrDteLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLmiProcedures.setStatus("mandatory")


class _MscFrDteLmiPollingInterval_Type(Unsigned32):
    """Custom type mscFrDteLmiPollingInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_MscFrDteLmiPollingInterval_Type.__name__ = "Unsigned32"
_MscFrDteLmiPollingInterval_Object = MibTableColumn
mscFrDteLmiPollingInterval = _MscFrDteLmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 10, 1, 4),
    _MscFrDteLmiPollingInterval_Type()
)
mscFrDteLmiPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLmiPollingInterval.setStatus("mandatory")


class _MscFrDteLmiFullEnquiryInterval_Type(Unsigned32):
    """Custom type mscFrDteLmiFullEnquiryInterval based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrDteLmiFullEnquiryInterval_Type.__name__ = "Unsigned32"
_MscFrDteLmiFullEnquiryInterval_Object = MibTableColumn
mscFrDteLmiFullEnquiryInterval = _MscFrDteLmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 10, 1, 5),
    _MscFrDteLmiFullEnquiryInterval_Type()
)
mscFrDteLmiFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLmiFullEnquiryInterval.setStatus("mandatory")


class _MscFrDteLmiErrorThreshold_Type(Unsigned32):
    """Custom type mscFrDteLmiErrorThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrDteLmiErrorThreshold_Type.__name__ = "Unsigned32"
_MscFrDteLmiErrorThreshold_Object = MibTableColumn
mscFrDteLmiErrorThreshold = _MscFrDteLmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 10, 1, 6),
    _MscFrDteLmiErrorThreshold_Type()
)
mscFrDteLmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLmiErrorThreshold.setStatus("mandatory")


class _MscFrDteLmiMonitoredEvents_Type(Unsigned32):
    """Custom type mscFrDteLmiMonitoredEvents based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrDteLmiMonitoredEvents_Type.__name__ = "Unsigned32"
_MscFrDteLmiMonitoredEvents_Object = MibTableColumn
mscFrDteLmiMonitoredEvents = _MscFrDteLmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 10, 1, 7),
    _MscFrDteLmiMonitoredEvents_Type()
)
mscFrDteLmiMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLmiMonitoredEvents.setStatus("mandatory")
_MscFrDteLmiOperTable_Object = MibTable
mscFrDteLmiOperTable = _MscFrDteLmiOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrDteLmiOperTable.setStatus("mandatory")
_MscFrDteLmiOperEntry_Object = MibTableRow
mscFrDteLmiOperEntry = _MscFrDteLmiOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 11, 1)
)
mscFrDteLmiOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteLmiOperEntry.setStatus("mandatory")


class _MscFrDteLmiLmiStatus_Type(Integer32):
    """Custom type mscFrDteLmiLmiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("initializing", 3),
          ("running", 1))
    )


_MscFrDteLmiLmiStatus_Type.__name__ = "Integer32"
_MscFrDteLmiLmiStatus_Object = MibTableColumn
mscFrDteLmiLmiStatus = _MscFrDteLmiLmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 3, 11, 1, 2),
    _MscFrDteLmiLmiStatus_Type()
)
mscFrDteLmiLmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLmiLmiStatus.setStatus("mandatory")
_MscFrDteRg_ObjectIdentity = ObjectIdentity
mscFrDteRg = _MscFrDteRg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4)
)
_MscFrDteRgRowStatusTable_Object = MibTable
mscFrDteRgRowStatusTable = _MscFrDteRgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrDteRgRowStatusTable.setStatus("mandatory")
_MscFrDteRgRowStatusEntry_Object = MibTableRow
mscFrDteRgRowStatusEntry = _MscFrDteRgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 1, 1)
)
mscFrDteRgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRgRowStatusEntry.setStatus("mandatory")
_MscFrDteRgRowStatus_Type = RowStatus
_MscFrDteRgRowStatus_Object = MibTableColumn
mscFrDteRgRowStatus = _MscFrDteRgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 1, 1, 1),
    _MscFrDteRgRowStatus_Type()
)
mscFrDteRgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteRgRowStatus.setStatus("mandatory")
_MscFrDteRgComponentName_Type = DisplayString
_MscFrDteRgComponentName_Object = MibTableColumn
mscFrDteRgComponentName = _MscFrDteRgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 1, 1, 2),
    _MscFrDteRgComponentName_Type()
)
mscFrDteRgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgComponentName.setStatus("mandatory")
_MscFrDteRgStorageType_Type = StorageType
_MscFrDteRgStorageType_Object = MibTableColumn
mscFrDteRgStorageType = _MscFrDteRgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 1, 1, 4),
    _MscFrDteRgStorageType_Type()
)
mscFrDteRgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgStorageType.setStatus("mandatory")


class _MscFrDteRgIndex_Type(Integer32):
    """Custom type mscFrDteRgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_MscFrDteRgIndex_Type.__name__ = "Integer32"
_MscFrDteRgIndex_Object = MibTableColumn
mscFrDteRgIndex = _MscFrDteRgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 1, 1, 10),
    _MscFrDteRgIndex_Type()
)
mscFrDteRgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteRgIndex.setStatus("mandatory")
_MscFrDteRgIfEntryTable_Object = MibTable
mscFrDteRgIfEntryTable = _MscFrDteRgIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 10)
)
if mibBuilder.loadTexts:
    mscFrDteRgIfEntryTable.setStatus("mandatory")
_MscFrDteRgIfEntryEntry_Object = MibTableRow
mscFrDteRgIfEntryEntry = _MscFrDteRgIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 10, 1)
)
mscFrDteRgIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRgIfEntryEntry.setStatus("mandatory")


class _MscFrDteRgIfAdminStatus_Type(Integer32):
    """Custom type mscFrDteRgIfAdminStatus based on Integer32"""
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


_MscFrDteRgIfAdminStatus_Type.__name__ = "Integer32"
_MscFrDteRgIfAdminStatus_Object = MibTableColumn
mscFrDteRgIfAdminStatus = _MscFrDteRgIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 10, 1, 1),
    _MscFrDteRgIfAdminStatus_Type()
)
mscFrDteRgIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteRgIfAdminStatus.setStatus("mandatory")


class _MscFrDteRgIfIndex_Type(InterfaceIndex):
    """Custom type mscFrDteRgIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrDteRgIfIndex_Type.__name__ = "InterfaceIndex"
_MscFrDteRgIfIndex_Object = MibTableColumn
mscFrDteRgIfIndex = _MscFrDteRgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 10, 1, 2),
    _MscFrDteRgIfIndex_Type()
)
mscFrDteRgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgIfIndex.setStatus("mandatory")
_MscFrDteRgProvTable_Object = MibTable
mscFrDteRgProvTable = _MscFrDteRgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 11)
)
if mibBuilder.loadTexts:
    mscFrDteRgProvTable.setStatus("mandatory")
_MscFrDteRgProvEntry_Object = MibTableRow
mscFrDteRgProvEntry = _MscFrDteRgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 11, 1)
)
mscFrDteRgProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRgProvEntry.setStatus("mandatory")


class _MscFrDteRgMaxTransmissionUnit_Type(Unsigned32):
    """Custom type mscFrDteRgMaxTransmissionUnit based on Unsigned32"""
    defaultValue = 1604

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(262, 9190),
    )


_MscFrDteRgMaxTransmissionUnit_Type.__name__ = "Unsigned32"
_MscFrDteRgMaxTransmissionUnit_Object = MibTableColumn
mscFrDteRgMaxTransmissionUnit = _MscFrDteRgMaxTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 11, 1, 1),
    _MscFrDteRgMaxTransmissionUnit_Type()
)
mscFrDteRgMaxTransmissionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteRgMaxTransmissionUnit.setStatus("mandatory")
_MscFrDteRgMpTable_Object = MibTable
mscFrDteRgMpTable = _MscFrDteRgMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 12)
)
if mibBuilder.loadTexts:
    mscFrDteRgMpTable.setStatus("mandatory")
_MscFrDteRgMpEntry_Object = MibTableRow
mscFrDteRgMpEntry = _MscFrDteRgMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 12, 1)
)
mscFrDteRgMpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRgMpEntry.setStatus("mandatory")
_MscFrDteRgLinkToProtocolPort_Type = Link
_MscFrDteRgLinkToProtocolPort_Object = MibTableColumn
mscFrDteRgLinkToProtocolPort = _MscFrDteRgLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 12, 1, 1),
    _MscFrDteRgLinkToProtocolPort_Type()
)
mscFrDteRgLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteRgLinkToProtocolPort.setStatus("mandatory")
_MscFrDteRgStateTable_Object = MibTable
mscFrDteRgStateTable = _MscFrDteRgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 13)
)
if mibBuilder.loadTexts:
    mscFrDteRgStateTable.setStatus("mandatory")
_MscFrDteRgStateEntry_Object = MibTableRow
mscFrDteRgStateEntry = _MscFrDteRgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 13, 1)
)
mscFrDteRgStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRgStateEntry.setStatus("mandatory")


class _MscFrDteRgAdminState_Type(Integer32):
    """Custom type mscFrDteRgAdminState based on Integer32"""
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


_MscFrDteRgAdminState_Type.__name__ = "Integer32"
_MscFrDteRgAdminState_Object = MibTableColumn
mscFrDteRgAdminState = _MscFrDteRgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 13, 1, 1),
    _MscFrDteRgAdminState_Type()
)
mscFrDteRgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgAdminState.setStatus("mandatory")


class _MscFrDteRgOperationalState_Type(Integer32):
    """Custom type mscFrDteRgOperationalState based on Integer32"""
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


_MscFrDteRgOperationalState_Type.__name__ = "Integer32"
_MscFrDteRgOperationalState_Object = MibTableColumn
mscFrDteRgOperationalState = _MscFrDteRgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 13, 1, 2),
    _MscFrDteRgOperationalState_Type()
)
mscFrDteRgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgOperationalState.setStatus("mandatory")


class _MscFrDteRgUsageState_Type(Integer32):
    """Custom type mscFrDteRgUsageState based on Integer32"""
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


_MscFrDteRgUsageState_Type.__name__ = "Integer32"
_MscFrDteRgUsageState_Object = MibTableColumn
mscFrDteRgUsageState = _MscFrDteRgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 13, 1, 3),
    _MscFrDteRgUsageState_Type()
)
mscFrDteRgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgUsageState.setStatus("mandatory")
_MscFrDteRgOperStatusTable_Object = MibTable
mscFrDteRgOperStatusTable = _MscFrDteRgOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 14)
)
if mibBuilder.loadTexts:
    mscFrDteRgOperStatusTable.setStatus("mandatory")
_MscFrDteRgOperStatusEntry_Object = MibTableRow
mscFrDteRgOperStatusEntry = _MscFrDteRgOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 14, 1)
)
mscFrDteRgOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRgOperStatusEntry.setStatus("mandatory")


class _MscFrDteRgSnmpOperStatus_Type(Integer32):
    """Custom type mscFrDteRgSnmpOperStatus based on Integer32"""
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


_MscFrDteRgSnmpOperStatus_Type.__name__ = "Integer32"
_MscFrDteRgSnmpOperStatus_Object = MibTableColumn
mscFrDteRgSnmpOperStatus = _MscFrDteRgSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 14, 1, 1),
    _MscFrDteRgSnmpOperStatus_Type()
)
mscFrDteRgSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgSnmpOperStatus.setStatus("mandatory")
_MscFrDteRgBfr_ObjectIdentity = ObjectIdentity
mscFrDteRgBfr = _MscFrDteRgBfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15)
)
_MscFrDteRgBfrRowStatusTable_Object = MibTable
mscFrDteRgBfrRowStatusTable = _MscFrDteRgBfrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 1)
)
if mibBuilder.loadTexts:
    mscFrDteRgBfrRowStatusTable.setStatus("mandatory")
_MscFrDteRgBfrRowStatusEntry_Object = MibTableRow
mscFrDteRgBfrRowStatusEntry = _MscFrDteRgBfrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 1, 1)
)
mscFrDteRgBfrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgBfrIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRgBfrRowStatusEntry.setStatus("mandatory")
_MscFrDteRgBfrRowStatus_Type = RowStatus
_MscFrDteRgBfrRowStatus_Object = MibTableColumn
mscFrDteRgBfrRowStatus = _MscFrDteRgBfrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 1, 1, 1),
    _MscFrDteRgBfrRowStatus_Type()
)
mscFrDteRgBfrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteRgBfrRowStatus.setStatus("mandatory")
_MscFrDteRgBfrComponentName_Type = DisplayString
_MscFrDteRgBfrComponentName_Object = MibTableColumn
mscFrDteRgBfrComponentName = _MscFrDteRgBfrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 1, 1, 2),
    _MscFrDteRgBfrComponentName_Type()
)
mscFrDteRgBfrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgBfrComponentName.setStatus("mandatory")
_MscFrDteRgBfrStorageType_Type = StorageType
_MscFrDteRgBfrStorageType_Object = MibTableColumn
mscFrDteRgBfrStorageType = _MscFrDteRgBfrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 1, 1, 4),
    _MscFrDteRgBfrStorageType_Type()
)
mscFrDteRgBfrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgBfrStorageType.setStatus("mandatory")
_MscFrDteRgBfrIndex_Type = NonReplicated
_MscFrDteRgBfrIndex_Object = MibTableColumn
mscFrDteRgBfrIndex = _MscFrDteRgBfrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 1, 1, 10),
    _MscFrDteRgBfrIndex_Type()
)
mscFrDteRgBfrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteRgBfrIndex.setStatus("mandatory")
_MscFrDteRgBfrProvTable_Object = MibTable
mscFrDteRgBfrProvTable = _MscFrDteRgBfrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 10)
)
if mibBuilder.loadTexts:
    mscFrDteRgBfrProvTable.setStatus("mandatory")
_MscFrDteRgBfrProvEntry_Object = MibTableRow
mscFrDteRgBfrProvEntry = _MscFrDteRgBfrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 10, 1)
)
mscFrDteRgBfrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgBfrIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRgBfrProvEntry.setStatus("mandatory")


class _MscFrDteRgBfrMacType_Type(Integer32):
    """Custom type mscFrDteRgBfrMacType based on Integer32"""
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
        *(("enet", 1),
          ("fddi", 0),
          ("tokenRing", 2))
    )


_MscFrDteRgBfrMacType_Type.__name__ = "Integer32"
_MscFrDteRgBfrMacType_Object = MibTableColumn
mscFrDteRgBfrMacType = _MscFrDteRgBfrMacType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 10, 1, 1),
    _MscFrDteRgBfrMacType_Type()
)
mscFrDteRgBfrMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteRgBfrMacType.setStatus("mandatory")


class _MscFrDteRgBfrBfrIndex_Type(Integer32):
    """Custom type mscFrDteRgBfrBfrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_MscFrDteRgBfrBfrIndex_Type.__name__ = "Integer32"
_MscFrDteRgBfrBfrIndex_Object = MibTableColumn
mscFrDteRgBfrBfrIndex = _MscFrDteRgBfrBfrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 10, 1, 2),
    _MscFrDteRgBfrBfrIndex_Type()
)
mscFrDteRgBfrBfrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteRgBfrBfrIndex.setStatus("mandatory")
_MscFrDteRgBfrOprTable_Object = MibTable
mscFrDteRgBfrOprTable = _MscFrDteRgBfrOprTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 11)
)
if mibBuilder.loadTexts:
    mscFrDteRgBfrOprTable.setStatus("mandatory")
_MscFrDteRgBfrOprEntry_Object = MibTableRow
mscFrDteRgBfrOprEntry = _MscFrDteRgBfrOprEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 11, 1)
)
mscFrDteRgBfrOprEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgBfrIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteRgBfrOprEntry.setStatus("mandatory")


class _MscFrDteRgBfrMacAddr_Type(DashedHexString):
    """Custom type mscFrDteRgBfrMacAddr based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscFrDteRgBfrMacAddr_Type.__name__ = "DashedHexString"
_MscFrDteRgBfrMacAddr_Object = MibTableColumn
mscFrDteRgBfrMacAddr = _MscFrDteRgBfrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 15, 11, 1, 1),
    _MscFrDteRgBfrMacAddr_Type()
)
mscFrDteRgBfrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRgBfrMacAddr.setStatus("mandatory")
_MscFrDteRgLtDlciTable_Object = MibTable
mscFrDteRgLtDlciTable = _MscFrDteRgLtDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 219)
)
if mibBuilder.loadTexts:
    mscFrDteRgLtDlciTable.setStatus("mandatory")
_MscFrDteRgLtDlciEntry_Object = MibTableRow
mscFrDteRgLtDlciEntry = _MscFrDteRgLtDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 219, 1)
)
mscFrDteRgLtDlciEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteRgLtDlciValue"),
)
if mibBuilder.loadTexts:
    mscFrDteRgLtDlciEntry.setStatus("mandatory")
_MscFrDteRgLtDlciValue_Type = Link
_MscFrDteRgLtDlciValue_Object = MibTableColumn
mscFrDteRgLtDlciValue = _MscFrDteRgLtDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 219, 1, 1),
    _MscFrDteRgLtDlciValue_Type()
)
mscFrDteRgLtDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteRgLtDlciValue.setStatus("mandatory")
_MscFrDteRgLtDlciRowStatus_Type = RowStatus
_MscFrDteRgLtDlciRowStatus_Object = MibTableColumn
mscFrDteRgLtDlciRowStatus = _MscFrDteRgLtDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 4, 219, 1, 2),
    _MscFrDteRgLtDlciRowStatus_Type()
)
mscFrDteRgLtDlciRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFrDteRgLtDlciRowStatus.setStatus("mandatory")
_MscFrDteDynDlciDefs_ObjectIdentity = ObjectIdentity
mscFrDteDynDlciDefs = _MscFrDteDynDlciDefs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5)
)
_MscFrDteDynDlciDefsRowStatusTable_Object = MibTable
mscFrDteDynDlciDefsRowStatusTable = _MscFrDteDynDlciDefsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 1)
)
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsRowStatusTable.setStatus("mandatory")
_MscFrDteDynDlciDefsRowStatusEntry_Object = MibTableRow
mscFrDteDynDlciDefsRowStatusEntry = _MscFrDteDynDlciDefsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 1, 1)
)
mscFrDteDynDlciDefsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteDynDlciDefsIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsRowStatusEntry.setStatus("mandatory")
_MscFrDteDynDlciDefsRowStatus_Type = RowStatus
_MscFrDteDynDlciDefsRowStatus_Object = MibTableColumn
mscFrDteDynDlciDefsRowStatus = _MscFrDteDynDlciDefsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 1, 1, 1),
    _MscFrDteDynDlciDefsRowStatus_Type()
)
mscFrDteDynDlciDefsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsRowStatus.setStatus("mandatory")
_MscFrDteDynDlciDefsComponentName_Type = DisplayString
_MscFrDteDynDlciDefsComponentName_Object = MibTableColumn
mscFrDteDynDlciDefsComponentName = _MscFrDteDynDlciDefsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 1, 1, 2),
    _MscFrDteDynDlciDefsComponentName_Type()
)
mscFrDteDynDlciDefsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsComponentName.setStatus("mandatory")
_MscFrDteDynDlciDefsStorageType_Type = StorageType
_MscFrDteDynDlciDefsStorageType_Object = MibTableColumn
mscFrDteDynDlciDefsStorageType = _MscFrDteDynDlciDefsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 1, 1, 4),
    _MscFrDteDynDlciDefsStorageType_Type()
)
mscFrDteDynDlciDefsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsStorageType.setStatus("mandatory")
_MscFrDteDynDlciDefsIndex_Type = NonReplicated
_MscFrDteDynDlciDefsIndex_Object = MibTableColumn
mscFrDteDynDlciDefsIndex = _MscFrDteDynDlciDefsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 1, 1, 10),
    _MscFrDteDynDlciDefsIndex_Type()
)
mscFrDteDynDlciDefsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsIndex.setStatus("mandatory")
_MscFrDteDynDlciDefsProvTable_Object = MibTable
mscFrDteDynDlciDefsProvTable = _MscFrDteDynDlciDefsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 10)
)
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsProvTable.setStatus("mandatory")
_MscFrDteDynDlciDefsProvEntry_Object = MibTableRow
mscFrDteDynDlciDefsProvEntry = _MscFrDteDynDlciDefsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 10, 1)
)
mscFrDteDynDlciDefsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteDynDlciDefsIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsProvEntry.setStatus("mandatory")


class _MscFrDteDynDlciDefsStdRowStatus_Type(Integer32):
    """Custom type mscFrDteDynDlciDefsStdRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_MscFrDteDynDlciDefsStdRowStatus_Type.__name__ = "Integer32"
_MscFrDteDynDlciDefsStdRowStatus_Object = MibTableColumn
mscFrDteDynDlciDefsStdRowStatus = _MscFrDteDynDlciDefsStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 10, 1, 1),
    _MscFrDteDynDlciDefsStdRowStatus_Type()
)
mscFrDteDynDlciDefsStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsStdRowStatus.setStatus("mandatory")


class _MscFrDteDynDlciDefsRateEnforcement_Type(Integer32):
    """Custom type mscFrDteDynDlciDefsRateEnforcement based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscFrDteDynDlciDefsRateEnforcement_Type.__name__ = "Integer32"
_MscFrDteDynDlciDefsRateEnforcement_Object = MibTableColumn
mscFrDteDynDlciDefsRateEnforcement = _MscFrDteDynDlciDefsRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 10, 1, 2),
    _MscFrDteDynDlciDefsRateEnforcement_Type()
)
mscFrDteDynDlciDefsRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsRateEnforcement.setStatus("mandatory")


class _MscFrDteDynDlciDefsCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrDteDynDlciDefsCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48000000),
    )


_MscFrDteDynDlciDefsCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrDteDynDlciDefsCommittedInformationRate_Object = MibTableColumn
mscFrDteDynDlciDefsCommittedInformationRate = _MscFrDteDynDlciDefsCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 10, 1, 3),
    _MscFrDteDynDlciDefsCommittedInformationRate_Type()
)
mscFrDteDynDlciDefsCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsCommittedInformationRate.setStatus("mandatory")


class _MscFrDteDynDlciDefsCommittedBurst_Type(Unsigned32):
    """Custom type mscFrDteDynDlciDefsCommittedBurst based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscFrDteDynDlciDefsCommittedBurst_Type.__name__ = "Unsigned32"
_MscFrDteDynDlciDefsCommittedBurst_Object = MibTableColumn
mscFrDteDynDlciDefsCommittedBurst = _MscFrDteDynDlciDefsCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 10, 1, 4),
    _MscFrDteDynDlciDefsCommittedBurst_Type()
)
mscFrDteDynDlciDefsCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsCommittedBurst.setStatus("mandatory")


class _MscFrDteDynDlciDefsExcessBurst_Type(Unsigned32):
    """Custom type mscFrDteDynDlciDefsExcessBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscFrDteDynDlciDefsExcessBurst_Type.__name__ = "Unsigned32"
_MscFrDteDynDlciDefsExcessBurst_Object = MibTableColumn
mscFrDteDynDlciDefsExcessBurst = _MscFrDteDynDlciDefsExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 10, 1, 5),
    _MscFrDteDynDlciDefsExcessBurst_Type()
)
mscFrDteDynDlciDefsExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsExcessBurst.setStatus("mandatory")


class _MscFrDteDynDlciDefsExcessBurstAction_Type(Integer32):
    """Custom type mscFrDteDynDlciDefsExcessBurstAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("setDeBit", 2))
    )


_MscFrDteDynDlciDefsExcessBurstAction_Type.__name__ = "Integer32"
_MscFrDteDynDlciDefsExcessBurstAction_Object = MibTableColumn
mscFrDteDynDlciDefsExcessBurstAction = _MscFrDteDynDlciDefsExcessBurstAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 10, 1, 6),
    _MscFrDteDynDlciDefsExcessBurstAction_Type()
)
mscFrDteDynDlciDefsExcessBurstAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsExcessBurstAction.setStatus("mandatory")


class _MscFrDteDynDlciDefsIpCos_Type(Unsigned32):
    """Custom type mscFrDteDynDlciDefsIpCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscFrDteDynDlciDefsIpCos_Type.__name__ = "Unsigned32"
_MscFrDteDynDlciDefsIpCos_Object = MibTableColumn
mscFrDteDynDlciDefsIpCos = _MscFrDteDynDlciDefsIpCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 5, 10, 1, 7),
    _MscFrDteDynDlciDefsIpCos_Type()
)
mscFrDteDynDlciDefsIpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDynDlciDefsIpCos.setStatus("mandatory")
_MscFrDteStDlci_ObjectIdentity = ObjectIdentity
mscFrDteStDlci = _MscFrDteStDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6)
)
_MscFrDteStDlciRowStatusTable_Object = MibTable
mscFrDteStDlciRowStatusTable = _MscFrDteStDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 1)
)
if mibBuilder.loadTexts:
    mscFrDteStDlciRowStatusTable.setStatus("mandatory")
_MscFrDteStDlciRowStatusEntry_Object = MibTableRow
mscFrDteStDlciRowStatusEntry = _MscFrDteStDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 1, 1)
)
mscFrDteStDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStDlciRowStatusEntry.setStatus("mandatory")
_MscFrDteStDlciRowStatus_Type = RowStatus
_MscFrDteStDlciRowStatus_Object = MibTableColumn
mscFrDteStDlciRowStatus = _MscFrDteStDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 1, 1, 1),
    _MscFrDteStDlciRowStatus_Type()
)
mscFrDteStDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciRowStatus.setStatus("mandatory")
_MscFrDteStDlciComponentName_Type = DisplayString
_MscFrDteStDlciComponentName_Object = MibTableColumn
mscFrDteStDlciComponentName = _MscFrDteStDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 1, 1, 2),
    _MscFrDteStDlciComponentName_Type()
)
mscFrDteStDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciComponentName.setStatus("mandatory")
_MscFrDteStDlciStorageType_Type = StorageType
_MscFrDteStDlciStorageType_Object = MibTableColumn
mscFrDteStDlciStorageType = _MscFrDteStDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 1, 1, 4),
    _MscFrDteStDlciStorageType_Type()
)
mscFrDteStDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciStorageType.setStatus("mandatory")


class _MscFrDteStDlciIndex_Type(Integer32):
    """Custom type mscFrDteStDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrDteStDlciIndex_Type.__name__ = "Integer32"
_MscFrDteStDlciIndex_Object = MibTableColumn
mscFrDteStDlciIndex = _MscFrDteStDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 1, 1, 10),
    _MscFrDteStDlciIndex_Type()
)
mscFrDteStDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteStDlciIndex.setStatus("mandatory")
_MscFrDteStDlciHq_ObjectIdentity = ObjectIdentity
mscFrDteStDlciHq = _MscFrDteStDlciHq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2)
)
_MscFrDteStDlciHqRowStatusTable_Object = MibTable
mscFrDteStDlciHqRowStatusTable = _MscFrDteStDlciHqRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqRowStatusTable.setStatus("mandatory")
_MscFrDteStDlciHqRowStatusEntry_Object = MibTableRow
mscFrDteStDlciHqRowStatusEntry = _MscFrDteStDlciHqRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 1, 1)
)
mscFrDteStDlciHqRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqRowStatusEntry.setStatus("mandatory")
_MscFrDteStDlciHqRowStatus_Type = RowStatus
_MscFrDteStDlciHqRowStatus_Object = MibTableColumn
mscFrDteStDlciHqRowStatus = _MscFrDteStDlciHqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 1, 1, 1),
    _MscFrDteStDlciHqRowStatus_Type()
)
mscFrDteStDlciHqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqRowStatus.setStatus("mandatory")
_MscFrDteStDlciHqComponentName_Type = DisplayString
_MscFrDteStDlciHqComponentName_Object = MibTableColumn
mscFrDteStDlciHqComponentName = _MscFrDteStDlciHqComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 1, 1, 2),
    _MscFrDteStDlciHqComponentName_Type()
)
mscFrDteStDlciHqComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqComponentName.setStatus("mandatory")
_MscFrDteStDlciHqStorageType_Type = StorageType
_MscFrDteStDlciHqStorageType_Object = MibTableColumn
mscFrDteStDlciHqStorageType = _MscFrDteStDlciHqStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 1, 1, 4),
    _MscFrDteStDlciHqStorageType_Type()
)
mscFrDteStDlciHqStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqStorageType.setStatus("mandatory")
_MscFrDteStDlciHqIndex_Type = NonReplicated
_MscFrDteStDlciHqIndex_Object = MibTableColumn
mscFrDteStDlciHqIndex = _MscFrDteStDlciHqIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 1, 1, 10),
    _MscFrDteStDlciHqIndex_Type()
)
mscFrDteStDlciHqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqIndex.setStatus("mandatory")
_MscFrDteStDlciHqProvTable_Object = MibTable
mscFrDteStDlciHqProvTable = _MscFrDteStDlciHqProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqProvTable.setStatus("mandatory")
_MscFrDteStDlciHqProvEntry_Object = MibTableRow
mscFrDteStDlciHqProvEntry = _MscFrDteStDlciHqProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 10, 1)
)
mscFrDteStDlciHqProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqProvEntry.setStatus("mandatory")


class _MscFrDteStDlciHqMaxPackets_Type(Unsigned32):
    """Custom type mscFrDteStDlciHqMaxPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_MscFrDteStDlciHqMaxPackets_Type.__name__ = "Unsigned32"
_MscFrDteStDlciHqMaxPackets_Object = MibTableColumn
mscFrDteStDlciHqMaxPackets = _MscFrDteStDlciHqMaxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 10, 1, 1),
    _MscFrDteStDlciHqMaxPackets_Type()
)
mscFrDteStDlciHqMaxPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqMaxPackets.setStatus("mandatory")


class _MscFrDteStDlciHqMaxMsecData_Type(Unsigned32):
    """Custom type mscFrDteStDlciHqMaxMsecData based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_MscFrDteStDlciHqMaxMsecData_Type.__name__ = "Unsigned32"
_MscFrDteStDlciHqMaxMsecData_Object = MibTableColumn
mscFrDteStDlciHqMaxMsecData = _MscFrDteStDlciHqMaxMsecData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 10, 1, 2),
    _MscFrDteStDlciHqMaxMsecData_Type()
)
mscFrDteStDlciHqMaxMsecData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqMaxMsecData.setStatus("mandatory")


class _MscFrDteStDlciHqMaxPercentMulticast_Type(Unsigned32):
    """Custom type mscFrDteStDlciHqMaxPercentMulticast based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscFrDteStDlciHqMaxPercentMulticast_Type.__name__ = "Unsigned32"
_MscFrDteStDlciHqMaxPercentMulticast_Object = MibTableColumn
mscFrDteStDlciHqMaxPercentMulticast = _MscFrDteStDlciHqMaxPercentMulticast_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 10, 1, 3),
    _MscFrDteStDlciHqMaxPercentMulticast_Type()
)
mscFrDteStDlciHqMaxPercentMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqMaxPercentMulticast.setStatus("mandatory")


class _MscFrDteStDlciHqTimeToLive_Type(Unsigned32):
    """Custom type mscFrDteStDlciHqTimeToLive based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_MscFrDteStDlciHqTimeToLive_Type.__name__ = "Unsigned32"
_MscFrDteStDlciHqTimeToLive_Object = MibTableColumn
mscFrDteStDlciHqTimeToLive = _MscFrDteStDlciHqTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 10, 1, 4),
    _MscFrDteStDlciHqTimeToLive_Type()
)
mscFrDteStDlciHqTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqTimeToLive.setStatus("mandatory")
_MscFrDteStDlciHqStatsTable_Object = MibTable
mscFrDteStDlciHqStatsTable = _MscFrDteStDlciHqStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 11)
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqStatsTable.setStatus("mandatory")
_MscFrDteStDlciHqStatsEntry_Object = MibTableRow
mscFrDteStDlciHqStatsEntry = _MscFrDteStDlciHqStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 11, 1)
)
mscFrDteStDlciHqStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqStatsEntry.setStatus("mandatory")
_MscFrDteStDlciHqTimedOutPkt_Type = Counter32
_MscFrDteStDlciHqTimedOutPkt_Object = MibTableColumn
mscFrDteStDlciHqTimedOutPkt = _MscFrDteStDlciHqTimedOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 11, 1, 1),
    _MscFrDteStDlciHqTimedOutPkt_Type()
)
mscFrDteStDlciHqTimedOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqTimedOutPkt.setStatus("mandatory")
_MscFrDteStDlciHqQueuePurgeDiscards_Type = Counter32
_MscFrDteStDlciHqQueuePurgeDiscards_Object = MibTableColumn
mscFrDteStDlciHqQueuePurgeDiscards = _MscFrDteStDlciHqQueuePurgeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 11, 1, 2),
    _MscFrDteStDlciHqQueuePurgeDiscards_Type()
)
mscFrDteStDlciHqQueuePurgeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqQueuePurgeDiscards.setStatus("mandatory")
_MscFrDteStDlciHqTStatsTable_Object = MibTable
mscFrDteStDlciHqTStatsTable = _MscFrDteStDlciHqTStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 12)
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqTStatsTable.setStatus("mandatory")
_MscFrDteStDlciHqTStatsEntry_Object = MibTableRow
mscFrDteStDlciHqTStatsEntry = _MscFrDteStDlciHqTStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 12, 1)
)
mscFrDteStDlciHqTStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqTStatsEntry.setStatus("mandatory")
_MscFrDteStDlciHqTotalPktHandled_Type = Counter32
_MscFrDteStDlciHqTotalPktHandled_Object = MibTableColumn
mscFrDteStDlciHqTotalPktHandled = _MscFrDteStDlciHqTotalPktHandled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 12, 1, 1),
    _MscFrDteStDlciHqTotalPktHandled_Type()
)
mscFrDteStDlciHqTotalPktHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqTotalPktHandled.setStatus("mandatory")
_MscFrDteStDlciHqTotalPktForwarded_Type = Counter32
_MscFrDteStDlciHqTotalPktForwarded_Object = MibTableColumn
mscFrDteStDlciHqTotalPktForwarded = _MscFrDteStDlciHqTotalPktForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 12, 1, 2),
    _MscFrDteStDlciHqTotalPktForwarded_Type()
)
mscFrDteStDlciHqTotalPktForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqTotalPktForwarded.setStatus("mandatory")
_MscFrDteStDlciHqTotalPktQueued_Type = Counter32
_MscFrDteStDlciHqTotalPktQueued_Object = MibTableColumn
mscFrDteStDlciHqTotalPktQueued = _MscFrDteStDlciHqTotalPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 12, 1, 3),
    _MscFrDteStDlciHqTotalPktQueued_Type()
)
mscFrDteStDlciHqTotalPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqTotalPktQueued.setStatus("mandatory")
_MscFrDteStDlciHqTotalMulticastPkt_Type = Counter32
_MscFrDteStDlciHqTotalMulticastPkt_Object = MibTableColumn
mscFrDteStDlciHqTotalMulticastPkt = _MscFrDteStDlciHqTotalMulticastPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 12, 1, 4),
    _MscFrDteStDlciHqTotalMulticastPkt_Type()
)
mscFrDteStDlciHqTotalMulticastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqTotalMulticastPkt.setStatus("mandatory")
_MscFrDteStDlciHqTotalPktDiscards_Type = Counter32
_MscFrDteStDlciHqTotalPktDiscards_Object = MibTableColumn
mscFrDteStDlciHqTotalPktDiscards = _MscFrDteStDlciHqTotalPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 12, 1, 5),
    _MscFrDteStDlciHqTotalPktDiscards_Type()
)
mscFrDteStDlciHqTotalPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqTotalPktDiscards.setStatus("mandatory")
_MscFrDteStDlciHqCStatsTable_Object = MibTable
mscFrDteStDlciHqCStatsTable = _MscFrDteStDlciHqCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 13)
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqCStatsTable.setStatus("mandatory")
_MscFrDteStDlciHqCStatsEntry_Object = MibTableRow
mscFrDteStDlciHqCStatsEntry = _MscFrDteStDlciHqCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 13, 1)
)
mscFrDteStDlciHqCStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqCStatsEntry.setStatus("mandatory")


class _MscFrDteStDlciHqCurrentPktQueued_Type(Gauge32):
    """Custom type mscFrDteStDlciHqCurrentPktQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteStDlciHqCurrentPktQueued_Type.__name__ = "Gauge32"
_MscFrDteStDlciHqCurrentPktQueued_Object = MibTableColumn
mscFrDteStDlciHqCurrentPktQueued = _MscFrDteStDlciHqCurrentPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 13, 1, 1),
    _MscFrDteStDlciHqCurrentPktQueued_Type()
)
mscFrDteStDlciHqCurrentPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqCurrentPktQueued.setStatus("mandatory")


class _MscFrDteStDlciHqCurrentBytesQueued_Type(Gauge32):
    """Custom type mscFrDteStDlciHqCurrentBytesQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteStDlciHqCurrentBytesQueued_Type.__name__ = "Gauge32"
_MscFrDteStDlciHqCurrentBytesQueued_Object = MibTableColumn
mscFrDteStDlciHqCurrentBytesQueued = _MscFrDteStDlciHqCurrentBytesQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 13, 1, 2),
    _MscFrDteStDlciHqCurrentBytesQueued_Type()
)
mscFrDteStDlciHqCurrentBytesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqCurrentBytesQueued.setStatus("mandatory")


class _MscFrDteStDlciHqCurrentMulticastQueued_Type(Gauge32):
    """Custom type mscFrDteStDlciHqCurrentMulticastQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteStDlciHqCurrentMulticastQueued_Type.__name__ = "Gauge32"
_MscFrDteStDlciHqCurrentMulticastQueued_Object = MibTableColumn
mscFrDteStDlciHqCurrentMulticastQueued = _MscFrDteStDlciHqCurrentMulticastQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 13, 1, 3),
    _MscFrDteStDlciHqCurrentMulticastQueued_Type()
)
mscFrDteStDlciHqCurrentMulticastQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqCurrentMulticastQueued.setStatus("mandatory")
_MscFrDteStDlciHqThrStatsTable_Object = MibTable
mscFrDteStDlciHqThrStatsTable = _MscFrDteStDlciHqThrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 14)
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqThrStatsTable.setStatus("mandatory")
_MscFrDteStDlciHqThrStatsEntry_Object = MibTableRow
mscFrDteStDlciHqThrStatsEntry = _MscFrDteStDlciHqThrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 14, 1)
)
mscFrDteStDlciHqThrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStDlciHqThrStatsEntry.setStatus("mandatory")


class _MscFrDteStDlciHqQueuePktThreshold_Type(Unsigned32):
    """Custom type mscFrDteStDlciHqQueuePktThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteStDlciHqQueuePktThreshold_Type.__name__ = "Unsigned32"
_MscFrDteStDlciHqQueuePktThreshold_Object = MibTableColumn
mscFrDteStDlciHqQueuePktThreshold = _MscFrDteStDlciHqQueuePktThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 14, 1, 1),
    _MscFrDteStDlciHqQueuePktThreshold_Type()
)
mscFrDteStDlciHqQueuePktThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqQueuePktThreshold.setStatus("mandatory")
_MscFrDteStDlciHqPktThresholdExceeded_Type = Counter32
_MscFrDteStDlciHqPktThresholdExceeded_Object = MibTableColumn
mscFrDteStDlciHqPktThresholdExceeded = _MscFrDteStDlciHqPktThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 14, 1, 2),
    _MscFrDteStDlciHqPktThresholdExceeded_Type()
)
mscFrDteStDlciHqPktThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqPktThresholdExceeded.setStatus("mandatory")


class _MscFrDteStDlciHqQueueByteThreshold_Type(Unsigned32):
    """Custom type mscFrDteStDlciHqQueueByteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteStDlciHqQueueByteThreshold_Type.__name__ = "Unsigned32"
_MscFrDteStDlciHqQueueByteThreshold_Object = MibTableColumn
mscFrDteStDlciHqQueueByteThreshold = _MscFrDteStDlciHqQueueByteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 14, 1, 3),
    _MscFrDteStDlciHqQueueByteThreshold_Type()
)
mscFrDteStDlciHqQueueByteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqQueueByteThreshold.setStatus("mandatory")
_MscFrDteStDlciHqByteThresholdExceeded_Type = Counter32
_MscFrDteStDlciHqByteThresholdExceeded_Object = MibTableColumn
mscFrDteStDlciHqByteThresholdExceeded = _MscFrDteStDlciHqByteThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 14, 1, 4),
    _MscFrDteStDlciHqByteThresholdExceeded_Type()
)
mscFrDteStDlciHqByteThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqByteThresholdExceeded.setStatus("mandatory")


class _MscFrDteStDlciHqQueueMulticastThreshold_Type(Unsigned32):
    """Custom type mscFrDteStDlciHqQueueMulticastThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteStDlciHqQueueMulticastThreshold_Type.__name__ = "Unsigned32"
_MscFrDteStDlciHqQueueMulticastThreshold_Object = MibTableColumn
mscFrDteStDlciHqQueueMulticastThreshold = _MscFrDteStDlciHqQueueMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 14, 1, 5),
    _MscFrDteStDlciHqQueueMulticastThreshold_Type()
)
mscFrDteStDlciHqQueueMulticastThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqQueueMulticastThreshold.setStatus("mandatory")
_MscFrDteStDlciHqMulThresholdExceeded_Type = Counter32
_MscFrDteStDlciHqMulThresholdExceeded_Object = MibTableColumn
mscFrDteStDlciHqMulThresholdExceeded = _MscFrDteStDlciHqMulThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 14, 1, 6),
    _MscFrDteStDlciHqMulThresholdExceeded_Type()
)
mscFrDteStDlciHqMulThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqMulThresholdExceeded.setStatus("mandatory")
_MscFrDteStDlciHqMemThresholdExceeded_Type = Counter32
_MscFrDteStDlciHqMemThresholdExceeded_Object = MibTableColumn
mscFrDteStDlciHqMemThresholdExceeded = _MscFrDteStDlciHqMemThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 2, 14, 1, 7),
    _MscFrDteStDlciHqMemThresholdExceeded_Type()
)
mscFrDteStDlciHqMemThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteStDlciHqMemThresholdExceeded.setStatus("mandatory")
_MscFrDteStDlciProvTable_Object = MibTable
mscFrDteStDlciProvTable = _MscFrDteStDlciProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 10)
)
if mibBuilder.loadTexts:
    mscFrDteStDlciProvTable.setStatus("mandatory")
_MscFrDteStDlciProvEntry_Object = MibTableRow
mscFrDteStDlciProvEntry = _MscFrDteStDlciProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 10, 1)
)
mscFrDteStDlciProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStDlciProvEntry.setStatus("mandatory")


class _MscFrDteStDlciStdRowStatus_Type(Integer32):
    """Custom type mscFrDteStDlciStdRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2))
    )


_MscFrDteStDlciStdRowStatus_Type.__name__ = "Integer32"
_MscFrDteStDlciStdRowStatus_Object = MibTableColumn
mscFrDteStDlciStdRowStatus = _MscFrDteStDlciStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 10, 1, 1),
    _MscFrDteStDlciStdRowStatus_Type()
)
mscFrDteStDlciStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciStdRowStatus.setStatus("mandatory")


class _MscFrDteStDlciRateEnforcement_Type(Integer32):
    """Custom type mscFrDteStDlciRateEnforcement based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscFrDteStDlciRateEnforcement_Type.__name__ = "Integer32"
_MscFrDteStDlciRateEnforcement_Object = MibTableColumn
mscFrDteStDlciRateEnforcement = _MscFrDteStDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 10, 1, 2),
    _MscFrDteStDlciRateEnforcement_Type()
)
mscFrDteStDlciRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciRateEnforcement.setStatus("mandatory")


class _MscFrDteStDlciCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrDteStDlciCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48000000),
    )


_MscFrDteStDlciCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrDteStDlciCommittedInformationRate_Object = MibTableColumn
mscFrDteStDlciCommittedInformationRate = _MscFrDteStDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 10, 1, 3),
    _MscFrDteStDlciCommittedInformationRate_Type()
)
mscFrDteStDlciCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciCommittedInformationRate.setStatus("mandatory")


class _MscFrDteStDlciCommittedBurst_Type(Unsigned32):
    """Custom type mscFrDteStDlciCommittedBurst based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscFrDteStDlciCommittedBurst_Type.__name__ = "Unsigned32"
_MscFrDteStDlciCommittedBurst_Object = MibTableColumn
mscFrDteStDlciCommittedBurst = _MscFrDteStDlciCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 10, 1, 4),
    _MscFrDteStDlciCommittedBurst_Type()
)
mscFrDteStDlciCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciCommittedBurst.setStatus("mandatory")


class _MscFrDteStDlciExcessBurst_Type(Unsigned32):
    """Custom type mscFrDteStDlciExcessBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscFrDteStDlciExcessBurst_Type.__name__ = "Unsigned32"
_MscFrDteStDlciExcessBurst_Object = MibTableColumn
mscFrDteStDlciExcessBurst = _MscFrDteStDlciExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 10, 1, 5),
    _MscFrDteStDlciExcessBurst_Type()
)
mscFrDteStDlciExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciExcessBurst.setStatus("mandatory")


class _MscFrDteStDlciExcessBurstAction_Type(Integer32):
    """Custom type mscFrDteStDlciExcessBurstAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("setDeBit", 2))
    )


_MscFrDteStDlciExcessBurstAction_Type.__name__ = "Integer32"
_MscFrDteStDlciExcessBurstAction_Object = MibTableColumn
mscFrDteStDlciExcessBurstAction = _MscFrDteStDlciExcessBurstAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 10, 1, 6),
    _MscFrDteStDlciExcessBurstAction_Type()
)
mscFrDteStDlciExcessBurstAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciExcessBurstAction.setStatus("mandatory")


class _MscFrDteStDlciIpCos_Type(Unsigned32):
    """Custom type mscFrDteStDlciIpCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscFrDteStDlciIpCos_Type.__name__ = "Unsigned32"
_MscFrDteStDlciIpCos_Object = MibTableColumn
mscFrDteStDlciIpCos = _MscFrDteStDlciIpCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 10, 1, 7),
    _MscFrDteStDlciIpCos_Type()
)
mscFrDteStDlciIpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciIpCos.setStatus("mandatory")
_MscFrDteStDlciRgLinkTable_Object = MibTable
mscFrDteStDlciRgLinkTable = _MscFrDteStDlciRgLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 11)
)
if mibBuilder.loadTexts:
    mscFrDteStDlciRgLinkTable.setStatus("mandatory")
_MscFrDteStDlciRgLinkEntry_Object = MibTableRow
mscFrDteStDlciRgLinkEntry = _MscFrDteStDlciRgLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 11, 1)
)
mscFrDteStDlciRgLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteStDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStDlciRgLinkEntry.setStatus("mandatory")
_MscFrDteStDlciLinkToRemoteGroup_Type = Link
_MscFrDteStDlciLinkToRemoteGroup_Object = MibTableColumn
mscFrDteStDlciLinkToRemoteGroup = _MscFrDteStDlciLinkToRemoteGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 6, 11, 1, 1),
    _MscFrDteStDlciLinkToRemoteGroup_Type()
)
mscFrDteStDlciLinkToRemoteGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteStDlciLinkToRemoteGroup.setStatus("mandatory")
_MscFrDteLeq_ObjectIdentity = ObjectIdentity
mscFrDteLeq = _MscFrDteLeq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7)
)
_MscFrDteLeqRowStatusTable_Object = MibTable
mscFrDteLeqRowStatusTable = _MscFrDteLeqRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 1)
)
if mibBuilder.loadTexts:
    mscFrDteLeqRowStatusTable.setStatus("mandatory")
_MscFrDteLeqRowStatusEntry_Object = MibTableRow
mscFrDteLeqRowStatusEntry = _MscFrDteLeqRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 1, 1)
)
mscFrDteLeqRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteLeqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteLeqRowStatusEntry.setStatus("mandatory")
_MscFrDteLeqRowStatus_Type = RowStatus
_MscFrDteLeqRowStatus_Object = MibTableColumn
mscFrDteLeqRowStatus = _MscFrDteLeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 1, 1, 1),
    _MscFrDteLeqRowStatus_Type()
)
mscFrDteLeqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLeqRowStatus.setStatus("mandatory")
_MscFrDteLeqComponentName_Type = DisplayString
_MscFrDteLeqComponentName_Object = MibTableColumn
mscFrDteLeqComponentName = _MscFrDteLeqComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 1, 1, 2),
    _MscFrDteLeqComponentName_Type()
)
mscFrDteLeqComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqComponentName.setStatus("mandatory")
_MscFrDteLeqStorageType_Type = StorageType
_MscFrDteLeqStorageType_Object = MibTableColumn
mscFrDteLeqStorageType = _MscFrDteLeqStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 1, 1, 4),
    _MscFrDteLeqStorageType_Type()
)
mscFrDteLeqStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqStorageType.setStatus("mandatory")
_MscFrDteLeqIndex_Type = NonReplicated
_MscFrDteLeqIndex_Object = MibTableColumn
mscFrDteLeqIndex = _MscFrDteLeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 1, 1, 10),
    _MscFrDteLeqIndex_Type()
)
mscFrDteLeqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteLeqIndex.setStatus("mandatory")
_MscFrDteLeqProvTable_Object = MibTable
mscFrDteLeqProvTable = _MscFrDteLeqProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 10)
)
if mibBuilder.loadTexts:
    mscFrDteLeqProvTable.setStatus("mandatory")
_MscFrDteLeqProvEntry_Object = MibTableRow
mscFrDteLeqProvEntry = _MscFrDteLeqProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 10, 1)
)
mscFrDteLeqProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteLeqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteLeqProvEntry.setStatus("mandatory")


class _MscFrDteLeqMaxPackets_Type(Unsigned32):
    """Custom type mscFrDteLeqMaxPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_MscFrDteLeqMaxPackets_Type.__name__ = "Unsigned32"
_MscFrDteLeqMaxPackets_Object = MibTableColumn
mscFrDteLeqMaxPackets = _MscFrDteLeqMaxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 10, 1, 1),
    _MscFrDteLeqMaxPackets_Type()
)
mscFrDteLeqMaxPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLeqMaxPackets.setStatus("mandatory")


class _MscFrDteLeqMaxMsecData_Type(Unsigned32):
    """Custom type mscFrDteLeqMaxMsecData based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_MscFrDteLeqMaxMsecData_Type.__name__ = "Unsigned32"
_MscFrDteLeqMaxMsecData_Object = MibTableColumn
mscFrDteLeqMaxMsecData = _MscFrDteLeqMaxMsecData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 10, 1, 2),
    _MscFrDteLeqMaxMsecData_Type()
)
mscFrDteLeqMaxMsecData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLeqMaxMsecData.setStatus("mandatory")


class _MscFrDteLeqMaxPercentMulticast_Type(Unsigned32):
    """Custom type mscFrDteLeqMaxPercentMulticast based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscFrDteLeqMaxPercentMulticast_Type.__name__ = "Unsigned32"
_MscFrDteLeqMaxPercentMulticast_Object = MibTableColumn
mscFrDteLeqMaxPercentMulticast = _MscFrDteLeqMaxPercentMulticast_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 10, 1, 3),
    _MscFrDteLeqMaxPercentMulticast_Type()
)
mscFrDteLeqMaxPercentMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLeqMaxPercentMulticast.setStatus("mandatory")


class _MscFrDteLeqTimeToLive_Type(Unsigned32):
    """Custom type mscFrDteLeqTimeToLive based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_MscFrDteLeqTimeToLive_Type.__name__ = "Unsigned32"
_MscFrDteLeqTimeToLive_Object = MibTableColumn
mscFrDteLeqTimeToLive = _MscFrDteLeqTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 10, 1, 4),
    _MscFrDteLeqTimeToLive_Type()
)
mscFrDteLeqTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteLeqTimeToLive.setStatus("mandatory")
_MscFrDteLeqStatsTable_Object = MibTable
mscFrDteLeqStatsTable = _MscFrDteLeqStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 11)
)
if mibBuilder.loadTexts:
    mscFrDteLeqStatsTable.setStatus("mandatory")
_MscFrDteLeqStatsEntry_Object = MibTableRow
mscFrDteLeqStatsEntry = _MscFrDteLeqStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 11, 1)
)
mscFrDteLeqStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteLeqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteLeqStatsEntry.setStatus("mandatory")
_MscFrDteLeqTimedOutPkt_Type = Counter32
_MscFrDteLeqTimedOutPkt_Object = MibTableColumn
mscFrDteLeqTimedOutPkt = _MscFrDteLeqTimedOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 11, 1, 1),
    _MscFrDteLeqTimedOutPkt_Type()
)
mscFrDteLeqTimedOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqTimedOutPkt.setStatus("mandatory")
_MscFrDteLeqHardwareForcedPkt_Type = Counter32
_MscFrDteLeqHardwareForcedPkt_Object = MibTableColumn
mscFrDteLeqHardwareForcedPkt = _MscFrDteLeqHardwareForcedPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 11, 1, 2),
    _MscFrDteLeqHardwareForcedPkt_Type()
)
mscFrDteLeqHardwareForcedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqHardwareForcedPkt.setStatus("mandatory")
_MscFrDteLeqForcedPktDiscards_Type = Counter32
_MscFrDteLeqForcedPktDiscards_Object = MibTableColumn
mscFrDteLeqForcedPktDiscards = _MscFrDteLeqForcedPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 11, 1, 3),
    _MscFrDteLeqForcedPktDiscards_Type()
)
mscFrDteLeqForcedPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqForcedPktDiscards.setStatus("mandatory")
_MscFrDteLeqQueuePurgeDiscards_Type = Counter32
_MscFrDteLeqQueuePurgeDiscards_Object = MibTableColumn
mscFrDteLeqQueuePurgeDiscards = _MscFrDteLeqQueuePurgeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 11, 1, 4),
    _MscFrDteLeqQueuePurgeDiscards_Type()
)
mscFrDteLeqQueuePurgeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqQueuePurgeDiscards.setStatus("mandatory")
_MscFrDteLeqTStatsTable_Object = MibTable
mscFrDteLeqTStatsTable = _MscFrDteLeqTStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 12)
)
if mibBuilder.loadTexts:
    mscFrDteLeqTStatsTable.setStatus("mandatory")
_MscFrDteLeqTStatsEntry_Object = MibTableRow
mscFrDteLeqTStatsEntry = _MscFrDteLeqTStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 12, 1)
)
mscFrDteLeqTStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteLeqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteLeqTStatsEntry.setStatus("mandatory")
_MscFrDteLeqTotalPktHandled_Type = Counter32
_MscFrDteLeqTotalPktHandled_Object = MibTableColumn
mscFrDteLeqTotalPktHandled = _MscFrDteLeqTotalPktHandled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 12, 1, 1),
    _MscFrDteLeqTotalPktHandled_Type()
)
mscFrDteLeqTotalPktHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqTotalPktHandled.setStatus("mandatory")
_MscFrDteLeqTotalPktForwarded_Type = Counter32
_MscFrDteLeqTotalPktForwarded_Object = MibTableColumn
mscFrDteLeqTotalPktForwarded = _MscFrDteLeqTotalPktForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 12, 1, 2),
    _MscFrDteLeqTotalPktForwarded_Type()
)
mscFrDteLeqTotalPktForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqTotalPktForwarded.setStatus("mandatory")
_MscFrDteLeqTotalPktQueued_Type = Counter32
_MscFrDteLeqTotalPktQueued_Object = MibTableColumn
mscFrDteLeqTotalPktQueued = _MscFrDteLeqTotalPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 12, 1, 3),
    _MscFrDteLeqTotalPktQueued_Type()
)
mscFrDteLeqTotalPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqTotalPktQueued.setStatus("mandatory")
_MscFrDteLeqTotalMulticastPkt_Type = Counter32
_MscFrDteLeqTotalMulticastPkt_Object = MibTableColumn
mscFrDteLeqTotalMulticastPkt = _MscFrDteLeqTotalMulticastPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 12, 1, 4),
    _MscFrDteLeqTotalMulticastPkt_Type()
)
mscFrDteLeqTotalMulticastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqTotalMulticastPkt.setStatus("mandatory")
_MscFrDteLeqTotalPktDiscards_Type = Counter32
_MscFrDteLeqTotalPktDiscards_Object = MibTableColumn
mscFrDteLeqTotalPktDiscards = _MscFrDteLeqTotalPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 12, 1, 5),
    _MscFrDteLeqTotalPktDiscards_Type()
)
mscFrDteLeqTotalPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqTotalPktDiscards.setStatus("mandatory")
_MscFrDteLeqCStatsTable_Object = MibTable
mscFrDteLeqCStatsTable = _MscFrDteLeqCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 13)
)
if mibBuilder.loadTexts:
    mscFrDteLeqCStatsTable.setStatus("mandatory")
_MscFrDteLeqCStatsEntry_Object = MibTableRow
mscFrDteLeqCStatsEntry = _MscFrDteLeqCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 13, 1)
)
mscFrDteLeqCStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteLeqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteLeqCStatsEntry.setStatus("mandatory")


class _MscFrDteLeqCurrentPktQueued_Type(Gauge32):
    """Custom type mscFrDteLeqCurrentPktQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteLeqCurrentPktQueued_Type.__name__ = "Gauge32"
_MscFrDteLeqCurrentPktQueued_Object = MibTableColumn
mscFrDteLeqCurrentPktQueued = _MscFrDteLeqCurrentPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 13, 1, 1),
    _MscFrDteLeqCurrentPktQueued_Type()
)
mscFrDteLeqCurrentPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqCurrentPktQueued.setStatus("mandatory")


class _MscFrDteLeqCurrentBytesQueued_Type(Gauge32):
    """Custom type mscFrDteLeqCurrentBytesQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteLeqCurrentBytesQueued_Type.__name__ = "Gauge32"
_MscFrDteLeqCurrentBytesQueued_Object = MibTableColumn
mscFrDteLeqCurrentBytesQueued = _MscFrDteLeqCurrentBytesQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 13, 1, 2),
    _MscFrDteLeqCurrentBytesQueued_Type()
)
mscFrDteLeqCurrentBytesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqCurrentBytesQueued.setStatus("mandatory")


class _MscFrDteLeqCurrentMulticastQueued_Type(Gauge32):
    """Custom type mscFrDteLeqCurrentMulticastQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteLeqCurrentMulticastQueued_Type.__name__ = "Gauge32"
_MscFrDteLeqCurrentMulticastQueued_Object = MibTableColumn
mscFrDteLeqCurrentMulticastQueued = _MscFrDteLeqCurrentMulticastQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 13, 1, 3),
    _MscFrDteLeqCurrentMulticastQueued_Type()
)
mscFrDteLeqCurrentMulticastQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqCurrentMulticastQueued.setStatus("mandatory")
_MscFrDteLeqThrStatsTable_Object = MibTable
mscFrDteLeqThrStatsTable = _MscFrDteLeqThrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 14)
)
if mibBuilder.loadTexts:
    mscFrDteLeqThrStatsTable.setStatus("mandatory")
_MscFrDteLeqThrStatsEntry_Object = MibTableRow
mscFrDteLeqThrStatsEntry = _MscFrDteLeqThrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 14, 1)
)
mscFrDteLeqThrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteLeqIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteLeqThrStatsEntry.setStatus("mandatory")


class _MscFrDteLeqQueuePktThreshold_Type(Unsigned32):
    """Custom type mscFrDteLeqQueuePktThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteLeqQueuePktThreshold_Type.__name__ = "Unsigned32"
_MscFrDteLeqQueuePktThreshold_Object = MibTableColumn
mscFrDteLeqQueuePktThreshold = _MscFrDteLeqQueuePktThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 14, 1, 1),
    _MscFrDteLeqQueuePktThreshold_Type()
)
mscFrDteLeqQueuePktThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqQueuePktThreshold.setStatus("mandatory")
_MscFrDteLeqPktThresholdExceeded_Type = Counter32
_MscFrDteLeqPktThresholdExceeded_Object = MibTableColumn
mscFrDteLeqPktThresholdExceeded = _MscFrDteLeqPktThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 14, 1, 2),
    _MscFrDteLeqPktThresholdExceeded_Type()
)
mscFrDteLeqPktThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqPktThresholdExceeded.setStatus("mandatory")


class _MscFrDteLeqQueueByteThreshold_Type(Unsigned32):
    """Custom type mscFrDteLeqQueueByteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteLeqQueueByteThreshold_Type.__name__ = "Unsigned32"
_MscFrDteLeqQueueByteThreshold_Object = MibTableColumn
mscFrDteLeqQueueByteThreshold = _MscFrDteLeqQueueByteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 14, 1, 3),
    _MscFrDteLeqQueueByteThreshold_Type()
)
mscFrDteLeqQueueByteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqQueueByteThreshold.setStatus("mandatory")
_MscFrDteLeqByteThresholdExceeded_Type = Counter32
_MscFrDteLeqByteThresholdExceeded_Object = MibTableColumn
mscFrDteLeqByteThresholdExceeded = _MscFrDteLeqByteThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 14, 1, 4),
    _MscFrDteLeqByteThresholdExceeded_Type()
)
mscFrDteLeqByteThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqByteThresholdExceeded.setStatus("mandatory")


class _MscFrDteLeqQueueMulticastThreshold_Type(Unsigned32):
    """Custom type mscFrDteLeqQueueMulticastThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrDteLeqQueueMulticastThreshold_Type.__name__ = "Unsigned32"
_MscFrDteLeqQueueMulticastThreshold_Object = MibTableColumn
mscFrDteLeqQueueMulticastThreshold = _MscFrDteLeqQueueMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 14, 1, 5),
    _MscFrDteLeqQueueMulticastThreshold_Type()
)
mscFrDteLeqQueueMulticastThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqQueueMulticastThreshold.setStatus("mandatory")
_MscFrDteLeqMulThresholdExceeded_Type = Counter32
_MscFrDteLeqMulThresholdExceeded_Object = MibTableColumn
mscFrDteLeqMulThresholdExceeded = _MscFrDteLeqMulThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 14, 1, 6),
    _MscFrDteLeqMulThresholdExceeded_Type()
)
mscFrDteLeqMulThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqMulThresholdExceeded.setStatus("mandatory")
_MscFrDteLeqMemThresholdExceeded_Type = Counter32
_MscFrDteLeqMemThresholdExceeded_Object = MibTableColumn
mscFrDteLeqMemThresholdExceeded = _MscFrDteLeqMemThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 7, 14, 1, 7),
    _MscFrDteLeqMemThresholdExceeded_Type()
)
mscFrDteLeqMemThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLeqMemThresholdExceeded.setStatus("mandatory")
_MscFrDteDlci_ObjectIdentity = ObjectIdentity
mscFrDteDlci = _MscFrDteDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8)
)
_MscFrDteDlciRowStatusTable_Object = MibTable
mscFrDteDlciRowStatusTable = _MscFrDteDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 1)
)
if mibBuilder.loadTexts:
    mscFrDteDlciRowStatusTable.setStatus("mandatory")
_MscFrDteDlciRowStatusEntry_Object = MibTableRow
mscFrDteDlciRowStatusEntry = _MscFrDteDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 1, 1)
)
mscFrDteDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteDlciRowStatusEntry.setStatus("mandatory")
_MscFrDteDlciRowStatus_Type = RowStatus
_MscFrDteDlciRowStatus_Object = MibTableColumn
mscFrDteDlciRowStatus = _MscFrDteDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 1, 1, 1),
    _MscFrDteDlciRowStatus_Type()
)
mscFrDteDlciRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciRowStatus.setStatus("mandatory")
_MscFrDteDlciComponentName_Type = DisplayString
_MscFrDteDlciComponentName_Object = MibTableColumn
mscFrDteDlciComponentName = _MscFrDteDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 1, 1, 2),
    _MscFrDteDlciComponentName_Type()
)
mscFrDteDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciComponentName.setStatus("mandatory")
_MscFrDteDlciStorageType_Type = StorageType
_MscFrDteDlciStorageType_Object = MibTableColumn
mscFrDteDlciStorageType = _MscFrDteDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 1, 1, 4),
    _MscFrDteDlciStorageType_Type()
)
mscFrDteDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciStorageType.setStatus("mandatory")


class _MscFrDteDlciIndex_Type(Integer32):
    """Custom type mscFrDteDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscFrDteDlciIndex_Type.__name__ = "Integer32"
_MscFrDteDlciIndex_Object = MibTableColumn
mscFrDteDlciIndex = _MscFrDteDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 1, 1, 10),
    _MscFrDteDlciIndex_Type()
)
mscFrDteDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteDlciIndex.setStatus("mandatory")
_MscFrDteDlciStateTable_Object = MibTable
mscFrDteDlciStateTable = _MscFrDteDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 10)
)
if mibBuilder.loadTexts:
    mscFrDteDlciStateTable.setStatus("mandatory")
_MscFrDteDlciStateEntry_Object = MibTableRow
mscFrDteDlciStateEntry = _MscFrDteDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 10, 1)
)
mscFrDteDlciStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteDlciStateEntry.setStatus("mandatory")


class _MscFrDteDlciAdminState_Type(Integer32):
    """Custom type mscFrDteDlciAdminState based on Integer32"""
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


_MscFrDteDlciAdminState_Type.__name__ = "Integer32"
_MscFrDteDlciAdminState_Object = MibTableColumn
mscFrDteDlciAdminState = _MscFrDteDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 10, 1, 1),
    _MscFrDteDlciAdminState_Type()
)
mscFrDteDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciAdminState.setStatus("mandatory")


class _MscFrDteDlciOperationalState_Type(Integer32):
    """Custom type mscFrDteDlciOperationalState based on Integer32"""
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


_MscFrDteDlciOperationalState_Type.__name__ = "Integer32"
_MscFrDteDlciOperationalState_Object = MibTableColumn
mscFrDteDlciOperationalState = _MscFrDteDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 10, 1, 2),
    _MscFrDteDlciOperationalState_Type()
)
mscFrDteDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciOperationalState.setStatus("mandatory")


class _MscFrDteDlciUsageState_Type(Integer32):
    """Custom type mscFrDteDlciUsageState based on Integer32"""
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


_MscFrDteDlciUsageState_Type.__name__ = "Integer32"
_MscFrDteDlciUsageState_Object = MibTableColumn
mscFrDteDlciUsageState = _MscFrDteDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 10, 1, 3),
    _MscFrDteDlciUsageState_Type()
)
mscFrDteDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciUsageState.setStatus("mandatory")
_MscFrDteDlciOperTable_Object = MibTable
mscFrDteDlciOperTable = _MscFrDteDlciOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11)
)
if mibBuilder.loadTexts:
    mscFrDteDlciOperTable.setStatus("mandatory")
_MscFrDteDlciOperEntry_Object = MibTableRow
mscFrDteDlciOperEntry = _MscFrDteDlciOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1)
)
mscFrDteDlciOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteDlciOperEntry.setStatus("mandatory")


class _MscFrDteDlciDlciState_Type(Integer32):
    """Custom type mscFrDteDlciDlciState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_MscFrDteDlciDlciState_Type.__name__ = "Integer32"
_MscFrDteDlciDlciState_Object = MibTableColumn
mscFrDteDlciDlciState = _MscFrDteDlciDlciState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 4),
    _MscFrDteDlciDlciState_Type()
)
mscFrDteDlciDlciState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciDlciState.setStatus("mandatory")


class _MscFrDteDlciLastTimeChange_Type(EnterpriseDateAndTime):
    """Custom type mscFrDteDlciLastTimeChange based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscFrDteDlciLastTimeChange_Type.__name__ = "EnterpriseDateAndTime"
_MscFrDteDlciLastTimeChange_Object = MibTableColumn
mscFrDteDlciLastTimeChange = _MscFrDteDlciLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 5),
    _MscFrDteDlciLastTimeChange_Type()
)
mscFrDteDlciLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciLastTimeChange.setStatus("mandatory")
_MscFrDteDlciSentFrames_Type = Counter32
_MscFrDteDlciSentFrames_Object = MibTableColumn
mscFrDteDlciSentFrames = _MscFrDteDlciSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 7),
    _MscFrDteDlciSentFrames_Type()
)
mscFrDteDlciSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciSentFrames.setStatus("mandatory")
_MscFrDteDlciSentOctets_Type = Counter32
_MscFrDteDlciSentOctets_Object = MibTableColumn
mscFrDteDlciSentOctets = _MscFrDteDlciSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 8),
    _MscFrDteDlciSentOctets_Type()
)
mscFrDteDlciSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciSentOctets.setStatus("mandatory")
_MscFrDteDlciReceivedFrames_Type = Counter32
_MscFrDteDlciReceivedFrames_Object = MibTableColumn
mscFrDteDlciReceivedFrames = _MscFrDteDlciReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 9),
    _MscFrDteDlciReceivedFrames_Type()
)
mscFrDteDlciReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciReceivedFrames.setStatus("mandatory")
_MscFrDteDlciReceivedOctets_Type = Counter32
_MscFrDteDlciReceivedOctets_Object = MibTableColumn
mscFrDteDlciReceivedOctets = _MscFrDteDlciReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 10),
    _MscFrDteDlciReceivedOctets_Type()
)
mscFrDteDlciReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciReceivedOctets.setStatus("mandatory")
_MscFrDteDlciReceivedFECNs_Type = Counter32
_MscFrDteDlciReceivedFECNs_Object = MibTableColumn
mscFrDteDlciReceivedFECNs = _MscFrDteDlciReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 11),
    _MscFrDteDlciReceivedFECNs_Type()
)
mscFrDteDlciReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciReceivedFECNs.setStatus("mandatory")
_MscFrDteDlciReceivedBECNs_Type = Counter32
_MscFrDteDlciReceivedBECNs_Object = MibTableColumn
mscFrDteDlciReceivedBECNs = _MscFrDteDlciReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 12),
    _MscFrDteDlciReceivedBECNs_Type()
)
mscFrDteDlciReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciReceivedBECNs.setStatus("mandatory")
_MscFrDteDlciDiscardedFrames_Type = Counter32
_MscFrDteDlciDiscardedFrames_Object = MibTableColumn
mscFrDteDlciDiscardedFrames = _MscFrDteDlciDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 13),
    _MscFrDteDlciDiscardedFrames_Type()
)
mscFrDteDlciDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciDiscardedFrames.setStatus("mandatory")


class _MscFrDteDlciCreationType_Type(Integer32):
    """Custom type mscFrDteDlciCreationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MscFrDteDlciCreationType_Type.__name__ = "Integer32"
_MscFrDteDlciCreationType_Object = MibTableColumn
mscFrDteDlciCreationType = _MscFrDteDlciCreationType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 14),
    _MscFrDteDlciCreationType_Type()
)
mscFrDteDlciCreationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciCreationType.setStatus("mandatory")


class _MscFrDteDlciCreationTime_Type(EnterpriseDateAndTime):
    """Custom type mscFrDteDlciCreationTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscFrDteDlciCreationTime_Type.__name__ = "EnterpriseDateAndTime"
_MscFrDteDlciCreationTime_Object = MibTableColumn
mscFrDteDlciCreationTime = _MscFrDteDlciCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 15),
    _MscFrDteDlciCreationTime_Type()
)
mscFrDteDlciCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlciCreationTime.setStatus("mandatory")


class _MscFrDteDlciRateEnforcement_Type(Integer32):
    """Custom type mscFrDteDlciRateEnforcement based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscFrDteDlciRateEnforcement_Type.__name__ = "Integer32"
_MscFrDteDlciRateEnforcement_Object = MibTableColumn
mscFrDteDlciRateEnforcement = _MscFrDteDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 17),
    _MscFrDteDlciRateEnforcement_Type()
)
mscFrDteDlciRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDlciRateEnforcement.setStatus("mandatory")


class _MscFrDteDlciCommittedInformationRate_Type(Gauge32):
    """Custom type mscFrDteDlciCommittedInformationRate based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48000000),
    )


_MscFrDteDlciCommittedInformationRate_Type.__name__ = "Gauge32"
_MscFrDteDlciCommittedInformationRate_Object = MibTableColumn
mscFrDteDlciCommittedInformationRate = _MscFrDteDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 18),
    _MscFrDteDlciCommittedInformationRate_Type()
)
mscFrDteDlciCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDlciCommittedInformationRate.setStatus("mandatory")


class _MscFrDteDlciCommittedBurst_Type(Unsigned32):
    """Custom type mscFrDteDlciCommittedBurst based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscFrDteDlciCommittedBurst_Type.__name__ = "Unsigned32"
_MscFrDteDlciCommittedBurst_Object = MibTableColumn
mscFrDteDlciCommittedBurst = _MscFrDteDlciCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 19),
    _MscFrDteDlciCommittedBurst_Type()
)
mscFrDteDlciCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDlciCommittedBurst.setStatus("mandatory")


class _MscFrDteDlciExcessBurst_Type(Unsigned32):
    """Custom type mscFrDteDlciExcessBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscFrDteDlciExcessBurst_Type.__name__ = "Unsigned32"
_MscFrDteDlciExcessBurst_Object = MibTableColumn
mscFrDteDlciExcessBurst = _MscFrDteDlciExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 20),
    _MscFrDteDlciExcessBurst_Type()
)
mscFrDteDlciExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDlciExcessBurst.setStatus("mandatory")


class _MscFrDteDlciExcessBurstAction_Type(Integer32):
    """Custom type mscFrDteDlciExcessBurstAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("setDeBit", 2))
    )


_MscFrDteDlciExcessBurstAction_Type.__name__ = "Integer32"
_MscFrDteDlciExcessBurstAction_Object = MibTableColumn
mscFrDteDlciExcessBurstAction = _MscFrDteDlciExcessBurstAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 8, 11, 1, 21),
    _MscFrDteDlciExcessBurstAction_Type()
)
mscFrDteDlciExcessBurstAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteDlciExcessBurstAction.setStatus("mandatory")
_MscFrDteVFramer_ObjectIdentity = ObjectIdentity
mscFrDteVFramer = _MscFrDteVFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9)
)
_MscFrDteVFramerRowStatusTable_Object = MibTable
mscFrDteVFramerRowStatusTable = _MscFrDteVFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 1)
)
if mibBuilder.loadTexts:
    mscFrDteVFramerRowStatusTable.setStatus("mandatory")
_MscFrDteVFramerRowStatusEntry_Object = MibTableRow
mscFrDteVFramerRowStatusEntry = _MscFrDteVFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 1, 1)
)
mscFrDteVFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteVFramerRowStatusEntry.setStatus("mandatory")
_MscFrDteVFramerRowStatus_Type = RowStatus
_MscFrDteVFramerRowStatus_Object = MibTableColumn
mscFrDteVFramerRowStatus = _MscFrDteVFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 1, 1, 1),
    _MscFrDteVFramerRowStatus_Type()
)
mscFrDteVFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteVFramerRowStatus.setStatus("mandatory")
_MscFrDteVFramerComponentName_Type = DisplayString
_MscFrDteVFramerComponentName_Object = MibTableColumn
mscFrDteVFramerComponentName = _MscFrDteVFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 1, 1, 2),
    _MscFrDteVFramerComponentName_Type()
)
mscFrDteVFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteVFramerComponentName.setStatus("mandatory")
_MscFrDteVFramerStorageType_Type = StorageType
_MscFrDteVFramerStorageType_Object = MibTableColumn
mscFrDteVFramerStorageType = _MscFrDteVFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 1, 1, 4),
    _MscFrDteVFramerStorageType_Type()
)
mscFrDteVFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteVFramerStorageType.setStatus("mandatory")
_MscFrDteVFramerIndex_Type = NonReplicated
_MscFrDteVFramerIndex_Object = MibTableColumn
mscFrDteVFramerIndex = _MscFrDteVFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 1, 1, 10),
    _MscFrDteVFramerIndex_Type()
)
mscFrDteVFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrDteVFramerIndex.setStatus("mandatory")
_MscFrDteVFramerProvTable_Object = MibTable
mscFrDteVFramerProvTable = _MscFrDteVFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 10)
)
if mibBuilder.loadTexts:
    mscFrDteVFramerProvTable.setStatus("mandatory")
_MscFrDteVFramerProvEntry_Object = MibTableRow
mscFrDteVFramerProvEntry = _MscFrDteVFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 10, 1)
)
mscFrDteVFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteVFramerProvEntry.setStatus("mandatory")
_MscFrDteVFramerOtherVirtualFramer_Type = Link
_MscFrDteVFramerOtherVirtualFramer_Object = MibTableColumn
mscFrDteVFramerOtherVirtualFramer = _MscFrDteVFramerOtherVirtualFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 10, 1, 1),
    _MscFrDteVFramerOtherVirtualFramer_Type()
)
mscFrDteVFramerOtherVirtualFramer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteVFramerOtherVirtualFramer.setStatus("mandatory")
_MscFrDteVFramerLogicalProcessor_Type = Link
_MscFrDteVFramerLogicalProcessor_Object = MibTableColumn
mscFrDteVFramerLogicalProcessor = _MscFrDteVFramerLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 10, 1, 2),
    _MscFrDteVFramerLogicalProcessor_Type()
)
mscFrDteVFramerLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteVFramerLogicalProcessor.setStatus("mandatory")
_MscFrDteVFramerStateTable_Object = MibTable
mscFrDteVFramerStateTable = _MscFrDteVFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 11)
)
if mibBuilder.loadTexts:
    mscFrDteVFramerStateTable.setStatus("mandatory")
_MscFrDteVFramerStateEntry_Object = MibTableRow
mscFrDteVFramerStateEntry = _MscFrDteVFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 11, 1)
)
mscFrDteVFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteVFramerStateEntry.setStatus("mandatory")


class _MscFrDteVFramerAdminState_Type(Integer32):
    """Custom type mscFrDteVFramerAdminState based on Integer32"""
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


_MscFrDteVFramerAdminState_Type.__name__ = "Integer32"
_MscFrDteVFramerAdminState_Object = MibTableColumn
mscFrDteVFramerAdminState = _MscFrDteVFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 11, 1, 1),
    _MscFrDteVFramerAdminState_Type()
)
mscFrDteVFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteVFramerAdminState.setStatus("mandatory")


class _MscFrDteVFramerOperationalState_Type(Integer32):
    """Custom type mscFrDteVFramerOperationalState based on Integer32"""
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


_MscFrDteVFramerOperationalState_Type.__name__ = "Integer32"
_MscFrDteVFramerOperationalState_Object = MibTableColumn
mscFrDteVFramerOperationalState = _MscFrDteVFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 11, 1, 2),
    _MscFrDteVFramerOperationalState_Type()
)
mscFrDteVFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteVFramerOperationalState.setStatus("mandatory")


class _MscFrDteVFramerUsageState_Type(Integer32):
    """Custom type mscFrDteVFramerUsageState based on Integer32"""
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


_MscFrDteVFramerUsageState_Type.__name__ = "Integer32"
_MscFrDteVFramerUsageState_Object = MibTableColumn
mscFrDteVFramerUsageState = _MscFrDteVFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 11, 1, 3),
    _MscFrDteVFramerUsageState_Type()
)
mscFrDteVFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteVFramerUsageState.setStatus("mandatory")
_MscFrDteVFramerStatsTable_Object = MibTable
mscFrDteVFramerStatsTable = _MscFrDteVFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 12)
)
if mibBuilder.loadTexts:
    mscFrDteVFramerStatsTable.setStatus("mandatory")
_MscFrDteVFramerStatsEntry_Object = MibTableRow
mscFrDteVFramerStatsEntry = _MscFrDteVFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 12, 1)
)
mscFrDteVFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteVFramerStatsEntry.setStatus("mandatory")
_MscFrDteVFramerFrmToOtherVFramer_Type = PassportCounter64
_MscFrDteVFramerFrmToOtherVFramer_Object = MibTableColumn
mscFrDteVFramerFrmToOtherVFramer = _MscFrDteVFramerFrmToOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 12, 1, 2),
    _MscFrDteVFramerFrmToOtherVFramer_Type()
)
mscFrDteVFramerFrmToOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteVFramerFrmToOtherVFramer.setStatus("mandatory")
_MscFrDteVFramerFrmFromOtherVFramer_Type = PassportCounter64
_MscFrDteVFramerFrmFromOtherVFramer_Object = MibTableColumn
mscFrDteVFramerFrmFromOtherVFramer = _MscFrDteVFramerFrmFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 12, 1, 3),
    _MscFrDteVFramerFrmFromOtherVFramer_Type()
)
mscFrDteVFramerFrmFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteVFramerFrmFromOtherVFramer.setStatus("mandatory")
_MscFrDteVFramerOctetFromOtherVFramer_Type = PassportCounter64
_MscFrDteVFramerOctetFromOtherVFramer_Object = MibTableColumn
mscFrDteVFramerOctetFromOtherVFramer = _MscFrDteVFramerOctetFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 9, 12, 1, 5),
    _MscFrDteVFramerOctetFromOtherVFramer_Type()
)
mscFrDteVFramerOctetFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteVFramerOctetFromOtherVFramer.setStatus("mandatory")
_MscFrDteCidDataTable_Object = MibTable
mscFrDteCidDataTable = _MscFrDteCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 20)
)
if mibBuilder.loadTexts:
    mscFrDteCidDataTable.setStatus("mandatory")
_MscFrDteCidDataEntry_Object = MibTableRow
mscFrDteCidDataEntry = _MscFrDteCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 20, 1)
)
mscFrDteCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteCidDataEntry.setStatus("mandatory")


class _MscFrDteCustomerIdentifier_Type(Unsigned32):
    """Custom type mscFrDteCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscFrDteCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscFrDteCustomerIdentifier_Object = MibTableColumn
mscFrDteCustomerIdentifier = _MscFrDteCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 20, 1, 1),
    _MscFrDteCustomerIdentifier_Type()
)
mscFrDteCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteCustomerIdentifier.setStatus("mandatory")
_MscFrDteIfEntryTable_Object = MibTable
mscFrDteIfEntryTable = _MscFrDteIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 21)
)
if mibBuilder.loadTexts:
    mscFrDteIfEntryTable.setStatus("mandatory")
_MscFrDteIfEntryEntry_Object = MibTableRow
mscFrDteIfEntryEntry = _MscFrDteIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 21, 1)
)
mscFrDteIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteIfEntryEntry.setStatus("mandatory")


class _MscFrDteIfAdminStatus_Type(Integer32):
    """Custom type mscFrDteIfAdminStatus based on Integer32"""
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


_MscFrDteIfAdminStatus_Type.__name__ = "Integer32"
_MscFrDteIfAdminStatus_Object = MibTableColumn
mscFrDteIfAdminStatus = _MscFrDteIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 21, 1, 1),
    _MscFrDteIfAdminStatus_Type()
)
mscFrDteIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteIfAdminStatus.setStatus("mandatory")


class _MscFrDteIfIndex_Type(InterfaceIndex):
    """Custom type mscFrDteIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrDteIfIndex_Type.__name__ = "InterfaceIndex"
_MscFrDteIfIndex_Object = MibTableColumn
mscFrDteIfIndex = _MscFrDteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 21, 1, 2),
    _MscFrDteIfIndex_Type()
)
mscFrDteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteIfIndex.setStatus("mandatory")
_MscFrDteProvTable_Object = MibTable
mscFrDteProvTable = _MscFrDteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 22)
)
if mibBuilder.loadTexts:
    mscFrDteProvTable.setStatus("mandatory")
_MscFrDteProvEntry_Object = MibTableRow
mscFrDteProvEntry = _MscFrDteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 22, 1)
)
mscFrDteProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteProvEntry.setStatus("mandatory")


class _MscFrDteAcceptUndefinedDlci_Type(Integer32):
    """Custom type mscFrDteAcceptUndefinedDlci based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscFrDteAcceptUndefinedDlci_Type.__name__ = "Integer32"
_MscFrDteAcceptUndefinedDlci_Object = MibTableColumn
mscFrDteAcceptUndefinedDlci = _MscFrDteAcceptUndefinedDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 22, 1, 1),
    _MscFrDteAcceptUndefinedDlci_Type()
)
mscFrDteAcceptUndefinedDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrDteAcceptUndefinedDlci.setStatus("mandatory")
_MscFrDteStateTable_Object = MibTable
mscFrDteStateTable = _MscFrDteStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 23)
)
if mibBuilder.loadTexts:
    mscFrDteStateTable.setStatus("mandatory")
_MscFrDteStateEntry_Object = MibTableRow
mscFrDteStateEntry = _MscFrDteStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 23, 1)
)
mscFrDteStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteStateEntry.setStatus("mandatory")


class _MscFrDteAdminState_Type(Integer32):
    """Custom type mscFrDteAdminState based on Integer32"""
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


_MscFrDteAdminState_Type.__name__ = "Integer32"
_MscFrDteAdminState_Object = MibTableColumn
mscFrDteAdminState = _MscFrDteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 23, 1, 1),
    _MscFrDteAdminState_Type()
)
mscFrDteAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteAdminState.setStatus("mandatory")


class _MscFrDteOperationalState_Type(Integer32):
    """Custom type mscFrDteOperationalState based on Integer32"""
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


_MscFrDteOperationalState_Type.__name__ = "Integer32"
_MscFrDteOperationalState_Object = MibTableColumn
mscFrDteOperationalState = _MscFrDteOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 23, 1, 2),
    _MscFrDteOperationalState_Type()
)
mscFrDteOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteOperationalState.setStatus("mandatory")


class _MscFrDteUsageState_Type(Integer32):
    """Custom type mscFrDteUsageState based on Integer32"""
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


_MscFrDteUsageState_Type.__name__ = "Integer32"
_MscFrDteUsageState_Object = MibTableColumn
mscFrDteUsageState = _MscFrDteUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 23, 1, 3),
    _MscFrDteUsageState_Type()
)
mscFrDteUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteUsageState.setStatus("mandatory")
_MscFrDteOperStatusTable_Object = MibTable
mscFrDteOperStatusTable = _MscFrDteOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 24)
)
if mibBuilder.loadTexts:
    mscFrDteOperStatusTable.setStatus("mandatory")
_MscFrDteOperStatusEntry_Object = MibTableRow
mscFrDteOperStatusEntry = _MscFrDteOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 24, 1)
)
mscFrDteOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteOperStatusEntry.setStatus("mandatory")


class _MscFrDteSnmpOperStatus_Type(Integer32):
    """Custom type mscFrDteSnmpOperStatus based on Integer32"""
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


_MscFrDteSnmpOperStatus_Type.__name__ = "Integer32"
_MscFrDteSnmpOperStatus_Object = MibTableColumn
mscFrDteSnmpOperStatus = _MscFrDteSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 24, 1, 1),
    _MscFrDteSnmpOperStatus_Type()
)
mscFrDteSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteSnmpOperStatus.setStatus("mandatory")
_MscFrDteOperTable_Object = MibTable
mscFrDteOperTable = _MscFrDteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 25)
)
if mibBuilder.loadTexts:
    mscFrDteOperTable.setStatus("mandatory")
_MscFrDteOperEntry_Object = MibTableRow
mscFrDteOperEntry = _MscFrDteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 25, 1)
)
mscFrDteOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteOperEntry.setStatus("mandatory")


class _MscFrDteLinkOperState_Type(Integer32):
    """Custom type mscFrDteLinkOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 2),
          ("polling", 3))
    )


_MscFrDteLinkOperState_Type.__name__ = "Integer32"
_MscFrDteLinkOperState_Object = MibTableColumn
mscFrDteLinkOperState = _MscFrDteLinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 25, 1, 1),
    _MscFrDteLinkOperState_Type()
)
mscFrDteLinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteLinkOperState.setStatus("mandatory")
_MscFrDteErrTable_Object = MibTable
mscFrDteErrTable = _MscFrDteErrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 26)
)
if mibBuilder.loadTexts:
    mscFrDteErrTable.setStatus("mandatory")
_MscFrDteErrEntry_Object = MibTableRow
mscFrDteErrEntry = _MscFrDteErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 26, 1)
)
mscFrDteErrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteErrEntry.setStatus("mandatory")


class _MscFrDteErrType_Type(Integer32):
    """Custom type mscFrDteErrType based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dlcmiProtoErr", 5),
          ("dlcmiSequenceErr", 7),
          ("dlcmiUnknownIe", 6),
          ("dlcmiUnknownRpt", 8),
          ("illegalDlci", 4),
          ("noErrorSinceReset", 9),
          ("receiveLong", 3),
          ("receiveShort", 2),
          ("unknownError", 1))
    )


_MscFrDteErrType_Type.__name__ = "Integer32"
_MscFrDteErrType_Object = MibTableColumn
mscFrDteErrType = _MscFrDteErrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 26, 1, 2),
    _MscFrDteErrType_Type()
)
mscFrDteErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteErrType.setStatus("mandatory")


class _MscFrDteErrData_Type(HexString):
    """Custom type mscFrDteErrData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_MscFrDteErrData_Type.__name__ = "HexString"
_MscFrDteErrData_Object = MibTableColumn
mscFrDteErrData = _MscFrDteErrData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 26, 1, 3),
    _MscFrDteErrData_Type()
)
mscFrDteErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteErrData.setStatus("mandatory")


class _MscFrDteErrTime_Type(EnterpriseDateAndTime):
    """Custom type mscFrDteErrTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscFrDteErrTime_Type.__name__ = "EnterpriseDateAndTime"
_MscFrDteErrTime_Object = MibTableColumn
mscFrDteErrTime = _MscFrDteErrTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 26, 1, 4),
    _MscFrDteErrTime_Type()
)
mscFrDteErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteErrTime.setStatus("mandatory")
_MscFrDteErrDiscards_Type = Counter32
_MscFrDteErrDiscards_Object = MibTableColumn
mscFrDteErrDiscards = _MscFrDteErrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 26, 1, 6),
    _MscFrDteErrDiscards_Type()
)
mscFrDteErrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteErrDiscards.setStatus("mandatory")
_MscFrDteErrFaults_Type = Counter32
_MscFrDteErrFaults_Object = MibTableColumn
mscFrDteErrFaults = _MscFrDteErrFaults_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 26, 1, 7),
    _MscFrDteErrFaults_Type()
)
mscFrDteErrFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteErrFaults.setStatus("mandatory")


class _MscFrDteErrFaultTime_Type(EnterpriseDateAndTime):
    """Custom type mscFrDteErrFaultTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscFrDteErrFaultTime_Type.__name__ = "EnterpriseDateAndTime"
_MscFrDteErrFaultTime_Object = MibTableColumn
mscFrDteErrFaultTime = _MscFrDteErrFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 26, 1, 8),
    _MscFrDteErrFaultTime_Type()
)
mscFrDteErrFaultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteErrFaultTime.setStatus("mandatory")
_MscFrDteErrStatsTable_Object = MibTable
mscFrDteErrStatsTable = _MscFrDteErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27)
)
if mibBuilder.loadTexts:
    mscFrDteErrStatsTable.setStatus("mandatory")
_MscFrDteErrStatsEntry_Object = MibTableRow
mscFrDteErrStatsEntry = _MscFrDteErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1)
)
mscFrDteErrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB", "mscFrDteIndex"),
)
if mibBuilder.loadTexts:
    mscFrDteErrStatsEntry.setStatus("mandatory")
_MscFrDteXmitDiscardPvcDown_Type = Counter32
_MscFrDteXmitDiscardPvcDown_Object = MibTableColumn
mscFrDteXmitDiscardPvcDown = _MscFrDteXmitDiscardPvcDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 1),
    _MscFrDteXmitDiscardPvcDown_Type()
)
mscFrDteXmitDiscardPvcDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteXmitDiscardPvcDown.setStatus("mandatory")
_MscFrDteXmitDiscardLmiInactive_Type = Counter32
_MscFrDteXmitDiscardLmiInactive_Object = MibTableColumn
mscFrDteXmitDiscardLmiInactive = _MscFrDteXmitDiscardLmiInactive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 2),
    _MscFrDteXmitDiscardLmiInactive_Type()
)
mscFrDteXmitDiscardLmiInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteXmitDiscardLmiInactive.setStatus("mandatory")
_MscFrDteXmitDiscardFramerDown_Type = Counter32
_MscFrDteXmitDiscardFramerDown_Object = MibTableColumn
mscFrDteXmitDiscardFramerDown = _MscFrDteXmitDiscardFramerDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 3),
    _MscFrDteXmitDiscardFramerDown_Type()
)
mscFrDteXmitDiscardFramerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteXmitDiscardFramerDown.setStatus("mandatory")
_MscFrDteXmitDiscardPvcInactive_Type = Counter32
_MscFrDteXmitDiscardPvcInactive_Object = MibTableColumn
mscFrDteXmitDiscardPvcInactive = _MscFrDteXmitDiscardPvcInactive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 4),
    _MscFrDteXmitDiscardPvcInactive_Type()
)
mscFrDteXmitDiscardPvcInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteXmitDiscardPvcInactive.setStatus("mandatory")
_MscFrDteXmitDiscardCirExceeded_Type = Counter32
_MscFrDteXmitDiscardCirExceeded_Object = MibTableColumn
mscFrDteXmitDiscardCirExceeded = _MscFrDteXmitDiscardCirExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 5),
    _MscFrDteXmitDiscardCirExceeded_Type()
)
mscFrDteXmitDiscardCirExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteXmitDiscardCirExceeded.setStatus("mandatory")
_MscFrDteRecvDiscardPvcDown_Type = Counter32
_MscFrDteRecvDiscardPvcDown_Object = MibTableColumn
mscFrDteRecvDiscardPvcDown = _MscFrDteRecvDiscardPvcDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 6),
    _MscFrDteRecvDiscardPvcDown_Type()
)
mscFrDteRecvDiscardPvcDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRecvDiscardPvcDown.setStatus("mandatory")
_MscFrDteRecvDiscardLmiInactive_Type = Counter32
_MscFrDteRecvDiscardLmiInactive_Object = MibTableColumn
mscFrDteRecvDiscardLmiInactive = _MscFrDteRecvDiscardLmiInactive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 7),
    _MscFrDteRecvDiscardLmiInactive_Type()
)
mscFrDteRecvDiscardLmiInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRecvDiscardLmiInactive.setStatus("mandatory")
_MscFrDteRecvDiscardPvcInactive_Type = Counter32
_MscFrDteRecvDiscardPvcInactive_Object = MibTableColumn
mscFrDteRecvDiscardPvcInactive = _MscFrDteRecvDiscardPvcInactive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 8),
    _MscFrDteRecvDiscardPvcInactive_Type()
)
mscFrDteRecvDiscardPvcInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteRecvDiscardPvcInactive.setStatus("mandatory")
_MscFrDteBadFc_Type = Counter32
_MscFrDteBadFc_Object = MibTableColumn
mscFrDteBadFc = _MscFrDteBadFc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 9),
    _MscFrDteBadFc_Type()
)
mscFrDteBadFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteBadFc.setStatus("mandatory")
_MscFrDteUlpUnknownProtocol_Type = Counter32
_MscFrDteUlpUnknownProtocol_Object = MibTableColumn
mscFrDteUlpUnknownProtocol = _MscFrDteUlpUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 10),
    _MscFrDteUlpUnknownProtocol_Type()
)
mscFrDteUlpUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteUlpUnknownProtocol.setStatus("mandatory")
_MscFrDteDefragSequenceErrors_Type = Counter32
_MscFrDteDefragSequenceErrors_Object = MibTableColumn
mscFrDteDefragSequenceErrors = _MscFrDteDefragSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 11),
    _MscFrDteDefragSequenceErrors_Type()
)
mscFrDteDefragSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDefragSequenceErrors.setStatus("mandatory")
_MscFrDteReceiveShort_Type = Counter32
_MscFrDteReceiveShort_Object = MibTableColumn
mscFrDteReceiveShort = _MscFrDteReceiveShort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 12),
    _MscFrDteReceiveShort_Type()
)
mscFrDteReceiveShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteReceiveShort.setStatus("mandatory")
_MscFrDteIllegalDlci_Type = Counter32
_MscFrDteIllegalDlci_Object = MibTableColumn
mscFrDteIllegalDlci = _MscFrDteIllegalDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 13),
    _MscFrDteIllegalDlci_Type()
)
mscFrDteIllegalDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteIllegalDlci.setStatus("mandatory")
_MscFrDteDlcmiProtoErr_Type = Counter32
_MscFrDteDlcmiProtoErr_Object = MibTableColumn
mscFrDteDlcmiProtoErr = _MscFrDteDlcmiProtoErr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 14),
    _MscFrDteDlcmiProtoErr_Type()
)
mscFrDteDlcmiProtoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlcmiProtoErr.setStatus("mandatory")
_MscFrDteDlcmiUnknownIe_Type = Counter32
_MscFrDteDlcmiUnknownIe_Object = MibTableColumn
mscFrDteDlcmiUnknownIe = _MscFrDteDlcmiUnknownIe_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 15),
    _MscFrDteDlcmiUnknownIe_Type()
)
mscFrDteDlcmiUnknownIe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlcmiUnknownIe.setStatus("mandatory")
_MscFrDteDlcmiSequenceErr_Type = Counter32
_MscFrDteDlcmiSequenceErr_Object = MibTableColumn
mscFrDteDlcmiSequenceErr = _MscFrDteDlcmiSequenceErr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 16),
    _MscFrDteDlcmiSequenceErr_Type()
)
mscFrDteDlcmiSequenceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlcmiSequenceErr.setStatus("mandatory")
_MscFrDteDlcmiUnknownRpt_Type = Counter32
_MscFrDteDlcmiUnknownRpt_Object = MibTableColumn
mscFrDteDlcmiUnknownRpt = _MscFrDteDlcmiUnknownRpt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 101, 27, 1, 17),
    _MscFrDteDlcmiUnknownRpt_Type()
)
mscFrDteDlcmiUnknownRpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrDteDlcmiUnknownRpt.setStatus("mandatory")
_FrameRelayDteMIB_ObjectIdentity = ObjectIdentity
frameRelayDteMIB = _FrameRelayDteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 32)
)
_FrameRelayDteGroup_ObjectIdentity = ObjectIdentity
frameRelayDteGroup = _FrameRelayDteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 32, 1)
)
_FrameRelayDteGroupCA_ObjectIdentity = ObjectIdentity
frameRelayDteGroupCA = _FrameRelayDteGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 32, 1, 1)
)
_FrameRelayDteGroupCA02_ObjectIdentity = ObjectIdentity
frameRelayDteGroupCA02 = _FrameRelayDteGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 32, 1, 1, 3)
)
_FrameRelayDteGroupCA02A_ObjectIdentity = ObjectIdentity
frameRelayDteGroupCA02A = _FrameRelayDteGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 32, 1, 1, 3, 2)
)
_FrameRelayDteCapabilities_ObjectIdentity = ObjectIdentity
frameRelayDteCapabilities = _FrameRelayDteCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 32, 3)
)
_FrameRelayDteCapabilitiesCA_ObjectIdentity = ObjectIdentity
frameRelayDteCapabilitiesCA = _FrameRelayDteCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 32, 3, 1)
)
_FrameRelayDteCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frameRelayDteCapabilitiesCA02 = _FrameRelayDteCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 32, 3, 1, 3)
)
_FrameRelayDteCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frameRelayDteCapabilitiesCA02A = _FrameRelayDteCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 32, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayDteMIB",
    **{"mscFrDte": mscFrDte,
       "mscFrDteRowStatusTable": mscFrDteRowStatusTable,
       "mscFrDteRowStatusEntry": mscFrDteRowStatusEntry,
       "mscFrDteRowStatus": mscFrDteRowStatus,
       "mscFrDteComponentName": mscFrDteComponentName,
       "mscFrDteStorageType": mscFrDteStorageType,
       "mscFrDteIndex": mscFrDteIndex,
       "mscFrDteFramer": mscFrDteFramer,
       "mscFrDteFramerRowStatusTable": mscFrDteFramerRowStatusTable,
       "mscFrDteFramerRowStatusEntry": mscFrDteFramerRowStatusEntry,
       "mscFrDteFramerRowStatus": mscFrDteFramerRowStatus,
       "mscFrDteFramerComponentName": mscFrDteFramerComponentName,
       "mscFrDteFramerStorageType": mscFrDteFramerStorageType,
       "mscFrDteFramerIndex": mscFrDteFramerIndex,
       "mscFrDteFramerProvTable": mscFrDteFramerProvTable,
       "mscFrDteFramerProvEntry": mscFrDteFramerProvEntry,
       "mscFrDteFramerInterfaceName": mscFrDteFramerInterfaceName,
       "mscFrDteFramerStateTable": mscFrDteFramerStateTable,
       "mscFrDteFramerStateEntry": mscFrDteFramerStateEntry,
       "mscFrDteFramerAdminState": mscFrDteFramerAdminState,
       "mscFrDteFramerOperationalState": mscFrDteFramerOperationalState,
       "mscFrDteFramerUsageState": mscFrDteFramerUsageState,
       "mscFrDteFramerStatsTable": mscFrDteFramerStatsTable,
       "mscFrDteFramerStatsEntry": mscFrDteFramerStatsEntry,
       "mscFrDteFramerFrmToIf": mscFrDteFramerFrmToIf,
       "mscFrDteFramerFrmFromIf": mscFrDteFramerFrmFromIf,
       "mscFrDteFramerAborts": mscFrDteFramerAborts,
       "mscFrDteFramerCrcErrors": mscFrDteFramerCrcErrors,
       "mscFrDteFramerLrcErrors": mscFrDteFramerLrcErrors,
       "mscFrDteFramerNonOctetErrors": mscFrDteFramerNonOctetErrors,
       "mscFrDteFramerOverruns": mscFrDteFramerOverruns,
       "mscFrDteFramerUnderruns": mscFrDteFramerUnderruns,
       "mscFrDteFramerLargeFrmErrors": mscFrDteFramerLargeFrmErrors,
       "mscFrDteFramerUtilTable": mscFrDteFramerUtilTable,
       "mscFrDteFramerUtilEntry": mscFrDteFramerUtilEntry,
       "mscFrDteFramerNormPrioLinkUtilToIf": mscFrDteFramerNormPrioLinkUtilToIf,
       "mscFrDteFramerNormPrioLinkUtilFromIf": mscFrDteFramerNormPrioLinkUtilFromIf,
       "mscFrDteLmi": mscFrDteLmi,
       "mscFrDteLmiRowStatusTable": mscFrDteLmiRowStatusTable,
       "mscFrDteLmiRowStatusEntry": mscFrDteLmiRowStatusEntry,
       "mscFrDteLmiRowStatus": mscFrDteLmiRowStatus,
       "mscFrDteLmiComponentName": mscFrDteLmiComponentName,
       "mscFrDteLmiStorageType": mscFrDteLmiStorageType,
       "mscFrDteLmiIndex": mscFrDteLmiIndex,
       "mscFrDteLmiProvTable": mscFrDteLmiProvTable,
       "mscFrDteLmiProvEntry": mscFrDteLmiProvEntry,
       "mscFrDteLmiProcedures": mscFrDteLmiProcedures,
       "mscFrDteLmiPollingInterval": mscFrDteLmiPollingInterval,
       "mscFrDteLmiFullEnquiryInterval": mscFrDteLmiFullEnquiryInterval,
       "mscFrDteLmiErrorThreshold": mscFrDteLmiErrorThreshold,
       "mscFrDteLmiMonitoredEvents": mscFrDteLmiMonitoredEvents,
       "mscFrDteLmiOperTable": mscFrDteLmiOperTable,
       "mscFrDteLmiOperEntry": mscFrDteLmiOperEntry,
       "mscFrDteLmiLmiStatus": mscFrDteLmiLmiStatus,
       "mscFrDteRg": mscFrDteRg,
       "mscFrDteRgRowStatusTable": mscFrDteRgRowStatusTable,
       "mscFrDteRgRowStatusEntry": mscFrDteRgRowStatusEntry,
       "mscFrDteRgRowStatus": mscFrDteRgRowStatus,
       "mscFrDteRgComponentName": mscFrDteRgComponentName,
       "mscFrDteRgStorageType": mscFrDteRgStorageType,
       "mscFrDteRgIndex": mscFrDteRgIndex,
       "mscFrDteRgIfEntryTable": mscFrDteRgIfEntryTable,
       "mscFrDteRgIfEntryEntry": mscFrDteRgIfEntryEntry,
       "mscFrDteRgIfAdminStatus": mscFrDteRgIfAdminStatus,
       "mscFrDteRgIfIndex": mscFrDteRgIfIndex,
       "mscFrDteRgProvTable": mscFrDteRgProvTable,
       "mscFrDteRgProvEntry": mscFrDteRgProvEntry,
       "mscFrDteRgMaxTransmissionUnit": mscFrDteRgMaxTransmissionUnit,
       "mscFrDteRgMpTable": mscFrDteRgMpTable,
       "mscFrDteRgMpEntry": mscFrDteRgMpEntry,
       "mscFrDteRgLinkToProtocolPort": mscFrDteRgLinkToProtocolPort,
       "mscFrDteRgStateTable": mscFrDteRgStateTable,
       "mscFrDteRgStateEntry": mscFrDteRgStateEntry,
       "mscFrDteRgAdminState": mscFrDteRgAdminState,
       "mscFrDteRgOperationalState": mscFrDteRgOperationalState,
       "mscFrDteRgUsageState": mscFrDteRgUsageState,
       "mscFrDteRgOperStatusTable": mscFrDteRgOperStatusTable,
       "mscFrDteRgOperStatusEntry": mscFrDteRgOperStatusEntry,
       "mscFrDteRgSnmpOperStatus": mscFrDteRgSnmpOperStatus,
       "mscFrDteRgBfr": mscFrDteRgBfr,
       "mscFrDteRgBfrRowStatusTable": mscFrDteRgBfrRowStatusTable,
       "mscFrDteRgBfrRowStatusEntry": mscFrDteRgBfrRowStatusEntry,
       "mscFrDteRgBfrRowStatus": mscFrDteRgBfrRowStatus,
       "mscFrDteRgBfrComponentName": mscFrDteRgBfrComponentName,
       "mscFrDteRgBfrStorageType": mscFrDteRgBfrStorageType,
       "mscFrDteRgBfrIndex": mscFrDteRgBfrIndex,
       "mscFrDteRgBfrProvTable": mscFrDteRgBfrProvTable,
       "mscFrDteRgBfrProvEntry": mscFrDteRgBfrProvEntry,
       "mscFrDteRgBfrMacType": mscFrDteRgBfrMacType,
       "mscFrDteRgBfrBfrIndex": mscFrDteRgBfrBfrIndex,
       "mscFrDteRgBfrOprTable": mscFrDteRgBfrOprTable,
       "mscFrDteRgBfrOprEntry": mscFrDteRgBfrOprEntry,
       "mscFrDteRgBfrMacAddr": mscFrDteRgBfrMacAddr,
       "mscFrDteRgLtDlciTable": mscFrDteRgLtDlciTable,
       "mscFrDteRgLtDlciEntry": mscFrDteRgLtDlciEntry,
       "mscFrDteRgLtDlciValue": mscFrDteRgLtDlciValue,
       "mscFrDteRgLtDlciRowStatus": mscFrDteRgLtDlciRowStatus,
       "mscFrDteDynDlciDefs": mscFrDteDynDlciDefs,
       "mscFrDteDynDlciDefsRowStatusTable": mscFrDteDynDlciDefsRowStatusTable,
       "mscFrDteDynDlciDefsRowStatusEntry": mscFrDteDynDlciDefsRowStatusEntry,
       "mscFrDteDynDlciDefsRowStatus": mscFrDteDynDlciDefsRowStatus,
       "mscFrDteDynDlciDefsComponentName": mscFrDteDynDlciDefsComponentName,
       "mscFrDteDynDlciDefsStorageType": mscFrDteDynDlciDefsStorageType,
       "mscFrDteDynDlciDefsIndex": mscFrDteDynDlciDefsIndex,
       "mscFrDteDynDlciDefsProvTable": mscFrDteDynDlciDefsProvTable,
       "mscFrDteDynDlciDefsProvEntry": mscFrDteDynDlciDefsProvEntry,
       "mscFrDteDynDlciDefsStdRowStatus": mscFrDteDynDlciDefsStdRowStatus,
       "mscFrDteDynDlciDefsRateEnforcement": mscFrDteDynDlciDefsRateEnforcement,
       "mscFrDteDynDlciDefsCommittedInformationRate": mscFrDteDynDlciDefsCommittedInformationRate,
       "mscFrDteDynDlciDefsCommittedBurst": mscFrDteDynDlciDefsCommittedBurst,
       "mscFrDteDynDlciDefsExcessBurst": mscFrDteDynDlciDefsExcessBurst,
       "mscFrDteDynDlciDefsExcessBurstAction": mscFrDteDynDlciDefsExcessBurstAction,
       "mscFrDteDynDlciDefsIpCos": mscFrDteDynDlciDefsIpCos,
       "mscFrDteStDlci": mscFrDteStDlci,
       "mscFrDteStDlciRowStatusTable": mscFrDteStDlciRowStatusTable,
       "mscFrDteStDlciRowStatusEntry": mscFrDteStDlciRowStatusEntry,
       "mscFrDteStDlciRowStatus": mscFrDteStDlciRowStatus,
       "mscFrDteStDlciComponentName": mscFrDteStDlciComponentName,
       "mscFrDteStDlciStorageType": mscFrDteStDlciStorageType,
       "mscFrDteStDlciIndex": mscFrDteStDlciIndex,
       "mscFrDteStDlciHq": mscFrDteStDlciHq,
       "mscFrDteStDlciHqRowStatusTable": mscFrDteStDlciHqRowStatusTable,
       "mscFrDteStDlciHqRowStatusEntry": mscFrDteStDlciHqRowStatusEntry,
       "mscFrDteStDlciHqRowStatus": mscFrDteStDlciHqRowStatus,
       "mscFrDteStDlciHqComponentName": mscFrDteStDlciHqComponentName,
       "mscFrDteStDlciHqStorageType": mscFrDteStDlciHqStorageType,
       "mscFrDteStDlciHqIndex": mscFrDteStDlciHqIndex,
       "mscFrDteStDlciHqProvTable": mscFrDteStDlciHqProvTable,
       "mscFrDteStDlciHqProvEntry": mscFrDteStDlciHqProvEntry,
       "mscFrDteStDlciHqMaxPackets": mscFrDteStDlciHqMaxPackets,
       "mscFrDteStDlciHqMaxMsecData": mscFrDteStDlciHqMaxMsecData,
       "mscFrDteStDlciHqMaxPercentMulticast": mscFrDteStDlciHqMaxPercentMulticast,
       "mscFrDteStDlciHqTimeToLive": mscFrDteStDlciHqTimeToLive,
       "mscFrDteStDlciHqStatsTable": mscFrDteStDlciHqStatsTable,
       "mscFrDteStDlciHqStatsEntry": mscFrDteStDlciHqStatsEntry,
       "mscFrDteStDlciHqTimedOutPkt": mscFrDteStDlciHqTimedOutPkt,
       "mscFrDteStDlciHqQueuePurgeDiscards": mscFrDteStDlciHqQueuePurgeDiscards,
       "mscFrDteStDlciHqTStatsTable": mscFrDteStDlciHqTStatsTable,
       "mscFrDteStDlciHqTStatsEntry": mscFrDteStDlciHqTStatsEntry,
       "mscFrDteStDlciHqTotalPktHandled": mscFrDteStDlciHqTotalPktHandled,
       "mscFrDteStDlciHqTotalPktForwarded": mscFrDteStDlciHqTotalPktForwarded,
       "mscFrDteStDlciHqTotalPktQueued": mscFrDteStDlciHqTotalPktQueued,
       "mscFrDteStDlciHqTotalMulticastPkt": mscFrDteStDlciHqTotalMulticastPkt,
       "mscFrDteStDlciHqTotalPktDiscards": mscFrDteStDlciHqTotalPktDiscards,
       "mscFrDteStDlciHqCStatsTable": mscFrDteStDlciHqCStatsTable,
       "mscFrDteStDlciHqCStatsEntry": mscFrDteStDlciHqCStatsEntry,
       "mscFrDteStDlciHqCurrentPktQueued": mscFrDteStDlciHqCurrentPktQueued,
       "mscFrDteStDlciHqCurrentBytesQueued": mscFrDteStDlciHqCurrentBytesQueued,
       "mscFrDteStDlciHqCurrentMulticastQueued": mscFrDteStDlciHqCurrentMulticastQueued,
       "mscFrDteStDlciHqThrStatsTable": mscFrDteStDlciHqThrStatsTable,
       "mscFrDteStDlciHqThrStatsEntry": mscFrDteStDlciHqThrStatsEntry,
       "mscFrDteStDlciHqQueuePktThreshold": mscFrDteStDlciHqQueuePktThreshold,
       "mscFrDteStDlciHqPktThresholdExceeded": mscFrDteStDlciHqPktThresholdExceeded,
       "mscFrDteStDlciHqQueueByteThreshold": mscFrDteStDlciHqQueueByteThreshold,
       "mscFrDteStDlciHqByteThresholdExceeded": mscFrDteStDlciHqByteThresholdExceeded,
       "mscFrDteStDlciHqQueueMulticastThreshold": mscFrDteStDlciHqQueueMulticastThreshold,
       "mscFrDteStDlciHqMulThresholdExceeded": mscFrDteStDlciHqMulThresholdExceeded,
       "mscFrDteStDlciHqMemThresholdExceeded": mscFrDteStDlciHqMemThresholdExceeded,
       "mscFrDteStDlciProvTable": mscFrDteStDlciProvTable,
       "mscFrDteStDlciProvEntry": mscFrDteStDlciProvEntry,
       "mscFrDteStDlciStdRowStatus": mscFrDteStDlciStdRowStatus,
       "mscFrDteStDlciRateEnforcement": mscFrDteStDlciRateEnforcement,
       "mscFrDteStDlciCommittedInformationRate": mscFrDteStDlciCommittedInformationRate,
       "mscFrDteStDlciCommittedBurst": mscFrDteStDlciCommittedBurst,
       "mscFrDteStDlciExcessBurst": mscFrDteStDlciExcessBurst,
       "mscFrDteStDlciExcessBurstAction": mscFrDteStDlciExcessBurstAction,
       "mscFrDteStDlciIpCos": mscFrDteStDlciIpCos,
       "mscFrDteStDlciRgLinkTable": mscFrDteStDlciRgLinkTable,
       "mscFrDteStDlciRgLinkEntry": mscFrDteStDlciRgLinkEntry,
       "mscFrDteStDlciLinkToRemoteGroup": mscFrDteStDlciLinkToRemoteGroup,
       "mscFrDteLeq": mscFrDteLeq,
       "mscFrDteLeqRowStatusTable": mscFrDteLeqRowStatusTable,
       "mscFrDteLeqRowStatusEntry": mscFrDteLeqRowStatusEntry,
       "mscFrDteLeqRowStatus": mscFrDteLeqRowStatus,
       "mscFrDteLeqComponentName": mscFrDteLeqComponentName,
       "mscFrDteLeqStorageType": mscFrDteLeqStorageType,
       "mscFrDteLeqIndex": mscFrDteLeqIndex,
       "mscFrDteLeqProvTable": mscFrDteLeqProvTable,
       "mscFrDteLeqProvEntry": mscFrDteLeqProvEntry,
       "mscFrDteLeqMaxPackets": mscFrDteLeqMaxPackets,
       "mscFrDteLeqMaxMsecData": mscFrDteLeqMaxMsecData,
       "mscFrDteLeqMaxPercentMulticast": mscFrDteLeqMaxPercentMulticast,
       "mscFrDteLeqTimeToLive": mscFrDteLeqTimeToLive,
       "mscFrDteLeqStatsTable": mscFrDteLeqStatsTable,
       "mscFrDteLeqStatsEntry": mscFrDteLeqStatsEntry,
       "mscFrDteLeqTimedOutPkt": mscFrDteLeqTimedOutPkt,
       "mscFrDteLeqHardwareForcedPkt": mscFrDteLeqHardwareForcedPkt,
       "mscFrDteLeqForcedPktDiscards": mscFrDteLeqForcedPktDiscards,
       "mscFrDteLeqQueuePurgeDiscards": mscFrDteLeqQueuePurgeDiscards,
       "mscFrDteLeqTStatsTable": mscFrDteLeqTStatsTable,
       "mscFrDteLeqTStatsEntry": mscFrDteLeqTStatsEntry,
       "mscFrDteLeqTotalPktHandled": mscFrDteLeqTotalPktHandled,
       "mscFrDteLeqTotalPktForwarded": mscFrDteLeqTotalPktForwarded,
       "mscFrDteLeqTotalPktQueued": mscFrDteLeqTotalPktQueued,
       "mscFrDteLeqTotalMulticastPkt": mscFrDteLeqTotalMulticastPkt,
       "mscFrDteLeqTotalPktDiscards": mscFrDteLeqTotalPktDiscards,
       "mscFrDteLeqCStatsTable": mscFrDteLeqCStatsTable,
       "mscFrDteLeqCStatsEntry": mscFrDteLeqCStatsEntry,
       "mscFrDteLeqCurrentPktQueued": mscFrDteLeqCurrentPktQueued,
       "mscFrDteLeqCurrentBytesQueued": mscFrDteLeqCurrentBytesQueued,
       "mscFrDteLeqCurrentMulticastQueued": mscFrDteLeqCurrentMulticastQueued,
       "mscFrDteLeqThrStatsTable": mscFrDteLeqThrStatsTable,
       "mscFrDteLeqThrStatsEntry": mscFrDteLeqThrStatsEntry,
       "mscFrDteLeqQueuePktThreshold": mscFrDteLeqQueuePktThreshold,
       "mscFrDteLeqPktThresholdExceeded": mscFrDteLeqPktThresholdExceeded,
       "mscFrDteLeqQueueByteThreshold": mscFrDteLeqQueueByteThreshold,
       "mscFrDteLeqByteThresholdExceeded": mscFrDteLeqByteThresholdExceeded,
       "mscFrDteLeqQueueMulticastThreshold": mscFrDteLeqQueueMulticastThreshold,
       "mscFrDteLeqMulThresholdExceeded": mscFrDteLeqMulThresholdExceeded,
       "mscFrDteLeqMemThresholdExceeded": mscFrDteLeqMemThresholdExceeded,
       "mscFrDteDlci": mscFrDteDlci,
       "mscFrDteDlciRowStatusTable": mscFrDteDlciRowStatusTable,
       "mscFrDteDlciRowStatusEntry": mscFrDteDlciRowStatusEntry,
       "mscFrDteDlciRowStatus": mscFrDteDlciRowStatus,
       "mscFrDteDlciComponentName": mscFrDteDlciComponentName,
       "mscFrDteDlciStorageType": mscFrDteDlciStorageType,
       "mscFrDteDlciIndex": mscFrDteDlciIndex,
       "mscFrDteDlciStateTable": mscFrDteDlciStateTable,
       "mscFrDteDlciStateEntry": mscFrDteDlciStateEntry,
       "mscFrDteDlciAdminState": mscFrDteDlciAdminState,
       "mscFrDteDlciOperationalState": mscFrDteDlciOperationalState,
       "mscFrDteDlciUsageState": mscFrDteDlciUsageState,
       "mscFrDteDlciOperTable": mscFrDteDlciOperTable,
       "mscFrDteDlciOperEntry": mscFrDteDlciOperEntry,
       "mscFrDteDlciDlciState": mscFrDteDlciDlciState,
       "mscFrDteDlciLastTimeChange": mscFrDteDlciLastTimeChange,
       "mscFrDteDlciSentFrames": mscFrDteDlciSentFrames,
       "mscFrDteDlciSentOctets": mscFrDteDlciSentOctets,
       "mscFrDteDlciReceivedFrames": mscFrDteDlciReceivedFrames,
       "mscFrDteDlciReceivedOctets": mscFrDteDlciReceivedOctets,
       "mscFrDteDlciReceivedFECNs": mscFrDteDlciReceivedFECNs,
       "mscFrDteDlciReceivedBECNs": mscFrDteDlciReceivedBECNs,
       "mscFrDteDlciDiscardedFrames": mscFrDteDlciDiscardedFrames,
       "mscFrDteDlciCreationType": mscFrDteDlciCreationType,
       "mscFrDteDlciCreationTime": mscFrDteDlciCreationTime,
       "mscFrDteDlciRateEnforcement": mscFrDteDlciRateEnforcement,
       "mscFrDteDlciCommittedInformationRate": mscFrDteDlciCommittedInformationRate,
       "mscFrDteDlciCommittedBurst": mscFrDteDlciCommittedBurst,
       "mscFrDteDlciExcessBurst": mscFrDteDlciExcessBurst,
       "mscFrDteDlciExcessBurstAction": mscFrDteDlciExcessBurstAction,
       "mscFrDteVFramer": mscFrDteVFramer,
       "mscFrDteVFramerRowStatusTable": mscFrDteVFramerRowStatusTable,
       "mscFrDteVFramerRowStatusEntry": mscFrDteVFramerRowStatusEntry,
       "mscFrDteVFramerRowStatus": mscFrDteVFramerRowStatus,
       "mscFrDteVFramerComponentName": mscFrDteVFramerComponentName,
       "mscFrDteVFramerStorageType": mscFrDteVFramerStorageType,
       "mscFrDteVFramerIndex": mscFrDteVFramerIndex,
       "mscFrDteVFramerProvTable": mscFrDteVFramerProvTable,
       "mscFrDteVFramerProvEntry": mscFrDteVFramerProvEntry,
       "mscFrDteVFramerOtherVirtualFramer": mscFrDteVFramerOtherVirtualFramer,
       "mscFrDteVFramerLogicalProcessor": mscFrDteVFramerLogicalProcessor,
       "mscFrDteVFramerStateTable": mscFrDteVFramerStateTable,
       "mscFrDteVFramerStateEntry": mscFrDteVFramerStateEntry,
       "mscFrDteVFramerAdminState": mscFrDteVFramerAdminState,
       "mscFrDteVFramerOperationalState": mscFrDteVFramerOperationalState,
       "mscFrDteVFramerUsageState": mscFrDteVFramerUsageState,
       "mscFrDteVFramerStatsTable": mscFrDteVFramerStatsTable,
       "mscFrDteVFramerStatsEntry": mscFrDteVFramerStatsEntry,
       "mscFrDteVFramerFrmToOtherVFramer": mscFrDteVFramerFrmToOtherVFramer,
       "mscFrDteVFramerFrmFromOtherVFramer": mscFrDteVFramerFrmFromOtherVFramer,
       "mscFrDteVFramerOctetFromOtherVFramer": mscFrDteVFramerOctetFromOtherVFramer,
       "mscFrDteCidDataTable": mscFrDteCidDataTable,
       "mscFrDteCidDataEntry": mscFrDteCidDataEntry,
       "mscFrDteCustomerIdentifier": mscFrDteCustomerIdentifier,
       "mscFrDteIfEntryTable": mscFrDteIfEntryTable,
       "mscFrDteIfEntryEntry": mscFrDteIfEntryEntry,
       "mscFrDteIfAdminStatus": mscFrDteIfAdminStatus,
       "mscFrDteIfIndex": mscFrDteIfIndex,
       "mscFrDteProvTable": mscFrDteProvTable,
       "mscFrDteProvEntry": mscFrDteProvEntry,
       "mscFrDteAcceptUndefinedDlci": mscFrDteAcceptUndefinedDlci,
       "mscFrDteStateTable": mscFrDteStateTable,
       "mscFrDteStateEntry": mscFrDteStateEntry,
       "mscFrDteAdminState": mscFrDteAdminState,
       "mscFrDteOperationalState": mscFrDteOperationalState,
       "mscFrDteUsageState": mscFrDteUsageState,
       "mscFrDteOperStatusTable": mscFrDteOperStatusTable,
       "mscFrDteOperStatusEntry": mscFrDteOperStatusEntry,
       "mscFrDteSnmpOperStatus": mscFrDteSnmpOperStatus,
       "mscFrDteOperTable": mscFrDteOperTable,
       "mscFrDteOperEntry": mscFrDteOperEntry,
       "mscFrDteLinkOperState": mscFrDteLinkOperState,
       "mscFrDteErrTable": mscFrDteErrTable,
       "mscFrDteErrEntry": mscFrDteErrEntry,
       "mscFrDteErrType": mscFrDteErrType,
       "mscFrDteErrData": mscFrDteErrData,
       "mscFrDteErrTime": mscFrDteErrTime,
       "mscFrDteErrDiscards": mscFrDteErrDiscards,
       "mscFrDteErrFaults": mscFrDteErrFaults,
       "mscFrDteErrFaultTime": mscFrDteErrFaultTime,
       "mscFrDteErrStatsTable": mscFrDteErrStatsTable,
       "mscFrDteErrStatsEntry": mscFrDteErrStatsEntry,
       "mscFrDteXmitDiscardPvcDown": mscFrDteXmitDiscardPvcDown,
       "mscFrDteXmitDiscardLmiInactive": mscFrDteXmitDiscardLmiInactive,
       "mscFrDteXmitDiscardFramerDown": mscFrDteXmitDiscardFramerDown,
       "mscFrDteXmitDiscardPvcInactive": mscFrDteXmitDiscardPvcInactive,
       "mscFrDteXmitDiscardCirExceeded": mscFrDteXmitDiscardCirExceeded,
       "mscFrDteRecvDiscardPvcDown": mscFrDteRecvDiscardPvcDown,
       "mscFrDteRecvDiscardLmiInactive": mscFrDteRecvDiscardLmiInactive,
       "mscFrDteRecvDiscardPvcInactive": mscFrDteRecvDiscardPvcInactive,
       "mscFrDteBadFc": mscFrDteBadFc,
       "mscFrDteUlpUnknownProtocol": mscFrDteUlpUnknownProtocol,
       "mscFrDteDefragSequenceErrors": mscFrDteDefragSequenceErrors,
       "mscFrDteReceiveShort": mscFrDteReceiveShort,
       "mscFrDteIllegalDlci": mscFrDteIllegalDlci,
       "mscFrDteDlcmiProtoErr": mscFrDteDlcmiProtoErr,
       "mscFrDteDlcmiUnknownIe": mscFrDteDlcmiUnknownIe,
       "mscFrDteDlcmiSequenceErr": mscFrDteDlcmiSequenceErr,
       "mscFrDteDlcmiUnknownRpt": mscFrDteDlcmiUnknownRpt,
       "frameRelayDteMIB": frameRelayDteMIB,
       "frameRelayDteGroup": frameRelayDteGroup,
       "frameRelayDteGroupCA": frameRelayDteGroupCA,
       "frameRelayDteGroupCA02": frameRelayDteGroupCA02,
       "frameRelayDteGroupCA02A": frameRelayDteGroupCA02A,
       "frameRelayDteCapabilities": frameRelayDteCapabilities,
       "frameRelayDteCapabilitiesCA": frameRelayDteCapabilitiesCA,
       "frameRelayDteCapabilitiesCA02": frameRelayDteCapabilitiesCA02,
       "frameRelayDteCapabilitiesCA02A": frameRelayDteCapabilitiesCA02A}
)
