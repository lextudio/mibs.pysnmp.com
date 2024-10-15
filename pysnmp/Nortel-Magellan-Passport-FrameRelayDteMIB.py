# SNMP MIB module (Nortel-Magellan-Passport-FrameRelayDteMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrameRelayDteMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:45 2024
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

(DashedHexString,
 EnterpriseDateAndTime,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "DashedHexString",
    "EnterpriseDateAndTime",
    "HexString",
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

_FrDte_ObjectIdentity = ObjectIdentity
frDte = _FrDte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101)
)
_FrDteRowStatusTable_Object = MibTable
frDteRowStatusTable = _FrDteRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 1)
)
if mibBuilder.loadTexts:
    frDteRowStatusTable.setStatus("mandatory")
_FrDteRowStatusEntry_Object = MibTableRow
frDteRowStatusEntry = _FrDteRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 1, 1)
)
frDteRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
)
if mibBuilder.loadTexts:
    frDteRowStatusEntry.setStatus("mandatory")
_FrDteRowStatus_Type = RowStatus
_FrDteRowStatus_Object = MibTableColumn
frDteRowStatus = _FrDteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 1, 1, 1),
    _FrDteRowStatus_Type()
)
frDteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteRowStatus.setStatus("mandatory")
_FrDteComponentName_Type = DisplayString
_FrDteComponentName_Object = MibTableColumn
frDteComponentName = _FrDteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 1, 1, 2),
    _FrDteComponentName_Type()
)
frDteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteComponentName.setStatus("mandatory")
_FrDteStorageType_Type = StorageType
_FrDteStorageType_Object = MibTableColumn
frDteStorageType = _FrDteStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 1, 1, 4),
    _FrDteStorageType_Type()
)
frDteStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStorageType.setStatus("mandatory")


class _FrDteIndex_Type(Integer32):
    """Custom type frDteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrDteIndex_Type.__name__ = "Integer32"
_FrDteIndex_Object = MibTableColumn
frDteIndex = _FrDteIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 1, 1, 10),
    _FrDteIndex_Type()
)
frDteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteIndex.setStatus("mandatory")
_FrDteFramer_ObjectIdentity = ObjectIdentity
frDteFramer = _FrDteFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2)
)
_FrDteFramerRowStatusTable_Object = MibTable
frDteFramerRowStatusTable = _FrDteFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 1)
)
if mibBuilder.loadTexts:
    frDteFramerRowStatusTable.setStatus("mandatory")
_FrDteFramerRowStatusEntry_Object = MibTableRow
frDteFramerRowStatusEntry = _FrDteFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 1, 1)
)
frDteFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteFramerIndex"),
)
if mibBuilder.loadTexts:
    frDteFramerRowStatusEntry.setStatus("mandatory")
_FrDteFramerRowStatus_Type = RowStatus
_FrDteFramerRowStatus_Object = MibTableColumn
frDteFramerRowStatus = _FrDteFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 1, 1, 1),
    _FrDteFramerRowStatus_Type()
)
frDteFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteFramerRowStatus.setStatus("mandatory")
_FrDteFramerComponentName_Type = DisplayString
_FrDteFramerComponentName_Object = MibTableColumn
frDteFramerComponentName = _FrDteFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 1, 1, 2),
    _FrDteFramerComponentName_Type()
)
frDteFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerComponentName.setStatus("mandatory")
_FrDteFramerStorageType_Type = StorageType
_FrDteFramerStorageType_Object = MibTableColumn
frDteFramerStorageType = _FrDteFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 1, 1, 4),
    _FrDteFramerStorageType_Type()
)
frDteFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerStorageType.setStatus("mandatory")
_FrDteFramerIndex_Type = NonReplicated
_FrDteFramerIndex_Object = MibTableColumn
frDteFramerIndex = _FrDteFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 1, 1, 10),
    _FrDteFramerIndex_Type()
)
frDteFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteFramerIndex.setStatus("mandatory")
_FrDteFramerProvTable_Object = MibTable
frDteFramerProvTable = _FrDteFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 10)
)
if mibBuilder.loadTexts:
    frDteFramerProvTable.setStatus("mandatory")
_FrDteFramerProvEntry_Object = MibTableRow
frDteFramerProvEntry = _FrDteFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 10, 1)
)
frDteFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteFramerIndex"),
)
if mibBuilder.loadTexts:
    frDteFramerProvEntry.setStatus("mandatory")
_FrDteFramerInterfaceName_Type = Link
_FrDteFramerInterfaceName_Object = MibTableColumn
frDteFramerInterfaceName = _FrDteFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 10, 1, 1),
    _FrDteFramerInterfaceName_Type()
)
frDteFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteFramerInterfaceName.setStatus("mandatory")
_FrDteFramerStateTable_Object = MibTable
frDteFramerStateTable = _FrDteFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 12)
)
if mibBuilder.loadTexts:
    frDteFramerStateTable.setStatus("mandatory")
_FrDteFramerStateEntry_Object = MibTableRow
frDteFramerStateEntry = _FrDteFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 12, 1)
)
frDteFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteFramerIndex"),
)
if mibBuilder.loadTexts:
    frDteFramerStateEntry.setStatus("mandatory")


class _FrDteFramerAdminState_Type(Integer32):
    """Custom type frDteFramerAdminState based on Integer32"""
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


_FrDteFramerAdminState_Type.__name__ = "Integer32"
_FrDteFramerAdminState_Object = MibTableColumn
frDteFramerAdminState = _FrDteFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 12, 1, 1),
    _FrDteFramerAdminState_Type()
)
frDteFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerAdminState.setStatus("mandatory")


class _FrDteFramerOperationalState_Type(Integer32):
    """Custom type frDteFramerOperationalState based on Integer32"""
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


_FrDteFramerOperationalState_Type.__name__ = "Integer32"
_FrDteFramerOperationalState_Object = MibTableColumn
frDteFramerOperationalState = _FrDteFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 12, 1, 2),
    _FrDteFramerOperationalState_Type()
)
frDteFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerOperationalState.setStatus("mandatory")


class _FrDteFramerUsageState_Type(Integer32):
    """Custom type frDteFramerUsageState based on Integer32"""
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


_FrDteFramerUsageState_Type.__name__ = "Integer32"
_FrDteFramerUsageState_Object = MibTableColumn
frDteFramerUsageState = _FrDteFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 12, 1, 3),
    _FrDteFramerUsageState_Type()
)
frDteFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerUsageState.setStatus("mandatory")
_FrDteFramerStatsTable_Object = MibTable
frDteFramerStatsTable = _FrDteFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13)
)
if mibBuilder.loadTexts:
    frDteFramerStatsTable.setStatus("mandatory")
_FrDteFramerStatsEntry_Object = MibTableRow
frDteFramerStatsEntry = _FrDteFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1)
)
frDteFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteFramerIndex"),
)
if mibBuilder.loadTexts:
    frDteFramerStatsEntry.setStatus("mandatory")
_FrDteFramerFrmToIf_Type = Counter32
_FrDteFramerFrmToIf_Object = MibTableColumn
frDteFramerFrmToIf = _FrDteFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1, 1),
    _FrDteFramerFrmToIf_Type()
)
frDteFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerFrmToIf.setStatus("mandatory")
_FrDteFramerFrmFromIf_Type = Counter32
_FrDteFramerFrmFromIf_Object = MibTableColumn
frDteFramerFrmFromIf = _FrDteFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1, 2),
    _FrDteFramerFrmFromIf_Type()
)
frDteFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerFrmFromIf.setStatus("mandatory")
_FrDteFramerAborts_Type = Counter32
_FrDteFramerAborts_Object = MibTableColumn
frDteFramerAborts = _FrDteFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1, 3),
    _FrDteFramerAborts_Type()
)
frDteFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerAborts.setStatus("mandatory")
_FrDteFramerCrcErrors_Type = Counter32
_FrDteFramerCrcErrors_Object = MibTableColumn
frDteFramerCrcErrors = _FrDteFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1, 4),
    _FrDteFramerCrcErrors_Type()
)
frDteFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerCrcErrors.setStatus("mandatory")
_FrDteFramerLrcErrors_Type = Counter32
_FrDteFramerLrcErrors_Object = MibTableColumn
frDteFramerLrcErrors = _FrDteFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1, 5),
    _FrDteFramerLrcErrors_Type()
)
frDteFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerLrcErrors.setStatus("mandatory")
_FrDteFramerNonOctetErrors_Type = Counter32
_FrDteFramerNonOctetErrors_Object = MibTableColumn
frDteFramerNonOctetErrors = _FrDteFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1, 6),
    _FrDteFramerNonOctetErrors_Type()
)
frDteFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerNonOctetErrors.setStatus("mandatory")
_FrDteFramerOverruns_Type = Counter32
_FrDteFramerOverruns_Object = MibTableColumn
frDteFramerOverruns = _FrDteFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1, 7),
    _FrDteFramerOverruns_Type()
)
frDteFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerOverruns.setStatus("mandatory")
_FrDteFramerUnderruns_Type = Counter32
_FrDteFramerUnderruns_Object = MibTableColumn
frDteFramerUnderruns = _FrDteFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1, 8),
    _FrDteFramerUnderruns_Type()
)
frDteFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerUnderruns.setStatus("mandatory")
_FrDteFramerLargeFrmErrors_Type = Counter32
_FrDteFramerLargeFrmErrors_Object = MibTableColumn
frDteFramerLargeFrmErrors = _FrDteFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 13, 1, 9),
    _FrDteFramerLargeFrmErrors_Type()
)
frDteFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerLargeFrmErrors.setStatus("mandatory")
_FrDteFramerUtilTable_Object = MibTable
frDteFramerUtilTable = _FrDteFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 14)
)
if mibBuilder.loadTexts:
    frDteFramerUtilTable.setStatus("mandatory")
_FrDteFramerUtilEntry_Object = MibTableRow
frDteFramerUtilEntry = _FrDteFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 14, 1)
)
frDteFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteFramerIndex"),
)
if mibBuilder.loadTexts:
    frDteFramerUtilEntry.setStatus("mandatory")


class _FrDteFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type frDteFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrDteFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_FrDteFramerNormPrioLinkUtilToIf_Object = MibTableColumn
frDteFramerNormPrioLinkUtilToIf = _FrDteFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 14, 1, 1),
    _FrDteFramerNormPrioLinkUtilToIf_Type()
)
frDteFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _FrDteFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type frDteFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrDteFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_FrDteFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
frDteFramerNormPrioLinkUtilFromIf = _FrDteFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 2, 14, 1, 3),
    _FrDteFramerNormPrioLinkUtilFromIf_Type()
)
frDteFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_FrDteLmi_ObjectIdentity = ObjectIdentity
frDteLmi = _FrDteLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3)
)
_FrDteLmiRowStatusTable_Object = MibTable
frDteLmiRowStatusTable = _FrDteLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 1)
)
if mibBuilder.loadTexts:
    frDteLmiRowStatusTable.setStatus("mandatory")
_FrDteLmiRowStatusEntry_Object = MibTableRow
frDteLmiRowStatusEntry = _FrDteLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 1, 1)
)
frDteLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteLmiIndex"),
)
if mibBuilder.loadTexts:
    frDteLmiRowStatusEntry.setStatus("mandatory")
_FrDteLmiRowStatus_Type = RowStatus
_FrDteLmiRowStatus_Object = MibTableColumn
frDteLmiRowStatus = _FrDteLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 1, 1, 1),
    _FrDteLmiRowStatus_Type()
)
frDteLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLmiRowStatus.setStatus("mandatory")
_FrDteLmiComponentName_Type = DisplayString
_FrDteLmiComponentName_Object = MibTableColumn
frDteLmiComponentName = _FrDteLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 1, 1, 2),
    _FrDteLmiComponentName_Type()
)
frDteLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLmiComponentName.setStatus("mandatory")
_FrDteLmiStorageType_Type = StorageType
_FrDteLmiStorageType_Object = MibTableColumn
frDteLmiStorageType = _FrDteLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 1, 1, 4),
    _FrDteLmiStorageType_Type()
)
frDteLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLmiStorageType.setStatus("mandatory")
_FrDteLmiIndex_Type = NonReplicated
_FrDteLmiIndex_Object = MibTableColumn
frDteLmiIndex = _FrDteLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 1, 1, 10),
    _FrDteLmiIndex_Type()
)
frDteLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteLmiIndex.setStatus("mandatory")
_FrDteLmiProvTable_Object = MibTable
frDteLmiProvTable = _FrDteLmiProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 10)
)
if mibBuilder.loadTexts:
    frDteLmiProvTable.setStatus("mandatory")
_FrDteLmiProvEntry_Object = MibTableRow
frDteLmiProvEntry = _FrDteLmiProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 10, 1)
)
frDteLmiProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteLmiIndex"),
)
if mibBuilder.loadTexts:
    frDteLmiProvEntry.setStatus("mandatory")


class _FrDteLmiProcedures_Type(Integer32):
    """Custom type frDteLmiProcedures based on Integer32"""
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
          ("itu", 5),
          ("none", 1),
          ("vendorForum", 2))
    )


_FrDteLmiProcedures_Type.__name__ = "Integer32"
_FrDteLmiProcedures_Object = MibTableColumn
frDteLmiProcedures = _FrDteLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 10, 1, 1),
    _FrDteLmiProcedures_Type()
)
frDteLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLmiProcedures.setStatus("mandatory")


class _FrDteLmiPollingInterval_Type(Unsigned32):
    """Custom type frDteLmiPollingInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrDteLmiPollingInterval_Type.__name__ = "Unsigned32"
_FrDteLmiPollingInterval_Object = MibTableColumn
frDteLmiPollingInterval = _FrDteLmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 10, 1, 4),
    _FrDteLmiPollingInterval_Type()
)
frDteLmiPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLmiPollingInterval.setStatus("mandatory")


class _FrDteLmiFullEnquiryInterval_Type(Unsigned32):
    """Custom type frDteLmiFullEnquiryInterval based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrDteLmiFullEnquiryInterval_Type.__name__ = "Unsigned32"
_FrDteLmiFullEnquiryInterval_Object = MibTableColumn
frDteLmiFullEnquiryInterval = _FrDteLmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 10, 1, 5),
    _FrDteLmiFullEnquiryInterval_Type()
)
frDteLmiFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLmiFullEnquiryInterval.setStatus("mandatory")


class _FrDteLmiErrorThreshold_Type(Unsigned32):
    """Custom type frDteLmiErrorThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrDteLmiErrorThreshold_Type.__name__ = "Unsigned32"
_FrDteLmiErrorThreshold_Object = MibTableColumn
frDteLmiErrorThreshold = _FrDteLmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 10, 1, 6),
    _FrDteLmiErrorThreshold_Type()
)
frDteLmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLmiErrorThreshold.setStatus("mandatory")


class _FrDteLmiMonitoredEvents_Type(Unsigned32):
    """Custom type frDteLmiMonitoredEvents based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrDteLmiMonitoredEvents_Type.__name__ = "Unsigned32"
_FrDteLmiMonitoredEvents_Object = MibTableColumn
frDteLmiMonitoredEvents = _FrDteLmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 10, 1, 7),
    _FrDteLmiMonitoredEvents_Type()
)
frDteLmiMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLmiMonitoredEvents.setStatus("mandatory")
_FrDteLmiOperTable_Object = MibTable
frDteLmiOperTable = _FrDteLmiOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 11)
)
if mibBuilder.loadTexts:
    frDteLmiOperTable.setStatus("mandatory")
_FrDteLmiOperEntry_Object = MibTableRow
frDteLmiOperEntry = _FrDteLmiOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 11, 1)
)
frDteLmiOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteLmiIndex"),
)
if mibBuilder.loadTexts:
    frDteLmiOperEntry.setStatus("mandatory")


class _FrDteLmiLmiStatus_Type(Integer32):
    """Custom type frDteLmiLmiStatus based on Integer32"""
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


_FrDteLmiLmiStatus_Type.__name__ = "Integer32"
_FrDteLmiLmiStatus_Object = MibTableColumn
frDteLmiLmiStatus = _FrDteLmiLmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 3, 11, 1, 2),
    _FrDteLmiLmiStatus_Type()
)
frDteLmiLmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLmiLmiStatus.setStatus("mandatory")
_FrDteRg_ObjectIdentity = ObjectIdentity
frDteRg = _FrDteRg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4)
)
_FrDteRgRowStatusTable_Object = MibTable
frDteRgRowStatusTable = _FrDteRgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 1)
)
if mibBuilder.loadTexts:
    frDteRgRowStatusTable.setStatus("mandatory")
_FrDteRgRowStatusEntry_Object = MibTableRow
frDteRgRowStatusEntry = _FrDteRgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 1, 1)
)
frDteRgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
)
if mibBuilder.loadTexts:
    frDteRgRowStatusEntry.setStatus("mandatory")
_FrDteRgRowStatus_Type = RowStatus
_FrDteRgRowStatus_Object = MibTableColumn
frDteRgRowStatus = _FrDteRgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 1, 1, 1),
    _FrDteRgRowStatus_Type()
)
frDteRgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteRgRowStatus.setStatus("mandatory")
_FrDteRgComponentName_Type = DisplayString
_FrDteRgComponentName_Object = MibTableColumn
frDteRgComponentName = _FrDteRgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 1, 1, 2),
    _FrDteRgComponentName_Type()
)
frDteRgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgComponentName.setStatus("mandatory")
_FrDteRgStorageType_Type = StorageType
_FrDteRgStorageType_Object = MibTableColumn
frDteRgStorageType = _FrDteRgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 1, 1, 4),
    _FrDteRgStorageType_Type()
)
frDteRgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgStorageType.setStatus("mandatory")


class _FrDteRgIndex_Type(Integer32):
    """Custom type frDteRgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FrDteRgIndex_Type.__name__ = "Integer32"
_FrDteRgIndex_Object = MibTableColumn
frDteRgIndex = _FrDteRgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 1, 1, 10),
    _FrDteRgIndex_Type()
)
frDteRgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteRgIndex.setStatus("mandatory")
_FrDteRgIfEntryTable_Object = MibTable
frDteRgIfEntryTable = _FrDteRgIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 10)
)
if mibBuilder.loadTexts:
    frDteRgIfEntryTable.setStatus("mandatory")
_FrDteRgIfEntryEntry_Object = MibTableRow
frDteRgIfEntryEntry = _FrDteRgIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 10, 1)
)
frDteRgIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
)
if mibBuilder.loadTexts:
    frDteRgIfEntryEntry.setStatus("mandatory")


class _FrDteRgIfAdminStatus_Type(Integer32):
    """Custom type frDteRgIfAdminStatus based on Integer32"""
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


_FrDteRgIfAdminStatus_Type.__name__ = "Integer32"
_FrDteRgIfAdminStatus_Object = MibTableColumn
frDteRgIfAdminStatus = _FrDteRgIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 10, 1, 1),
    _FrDteRgIfAdminStatus_Type()
)
frDteRgIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteRgIfAdminStatus.setStatus("mandatory")


class _FrDteRgIfIndex_Type(InterfaceIndex):
    """Custom type frDteRgIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrDteRgIfIndex_Type.__name__ = "InterfaceIndex"
_FrDteRgIfIndex_Object = MibTableColumn
frDteRgIfIndex = _FrDteRgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 10, 1, 2),
    _FrDteRgIfIndex_Type()
)
frDteRgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgIfIndex.setStatus("mandatory")
_FrDteRgProvTable_Object = MibTable
frDteRgProvTable = _FrDteRgProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 11)
)
if mibBuilder.loadTexts:
    frDteRgProvTable.setStatus("mandatory")
_FrDteRgProvEntry_Object = MibTableRow
frDteRgProvEntry = _FrDteRgProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 11, 1)
)
frDteRgProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
)
if mibBuilder.loadTexts:
    frDteRgProvEntry.setStatus("mandatory")


class _FrDteRgMaxTransmissionUnit_Type(Unsigned32):
    """Custom type frDteRgMaxTransmissionUnit based on Unsigned32"""
    defaultValue = 1604

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(262, 9190),
    )


_FrDteRgMaxTransmissionUnit_Type.__name__ = "Unsigned32"
_FrDteRgMaxTransmissionUnit_Object = MibTableColumn
frDteRgMaxTransmissionUnit = _FrDteRgMaxTransmissionUnit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 11, 1, 1),
    _FrDteRgMaxTransmissionUnit_Type()
)
frDteRgMaxTransmissionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteRgMaxTransmissionUnit.setStatus("mandatory")
_FrDteRgMpTable_Object = MibTable
frDteRgMpTable = _FrDteRgMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 12)
)
if mibBuilder.loadTexts:
    frDteRgMpTable.setStatus("mandatory")
_FrDteRgMpEntry_Object = MibTableRow
frDteRgMpEntry = _FrDteRgMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 12, 1)
)
frDteRgMpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
)
if mibBuilder.loadTexts:
    frDteRgMpEntry.setStatus("mandatory")
_FrDteRgLinkToProtocolPort_Type = Link
_FrDteRgLinkToProtocolPort_Object = MibTableColumn
frDteRgLinkToProtocolPort = _FrDteRgLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 12, 1, 1),
    _FrDteRgLinkToProtocolPort_Type()
)
frDteRgLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteRgLinkToProtocolPort.setStatus("mandatory")
_FrDteRgStateTable_Object = MibTable
frDteRgStateTable = _FrDteRgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 13)
)
if mibBuilder.loadTexts:
    frDteRgStateTable.setStatus("mandatory")
_FrDteRgStateEntry_Object = MibTableRow
frDteRgStateEntry = _FrDteRgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 13, 1)
)
frDteRgStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
)
if mibBuilder.loadTexts:
    frDteRgStateEntry.setStatus("mandatory")


class _FrDteRgAdminState_Type(Integer32):
    """Custom type frDteRgAdminState based on Integer32"""
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


_FrDteRgAdminState_Type.__name__ = "Integer32"
_FrDteRgAdminState_Object = MibTableColumn
frDteRgAdminState = _FrDteRgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 13, 1, 1),
    _FrDteRgAdminState_Type()
)
frDteRgAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgAdminState.setStatus("mandatory")


class _FrDteRgOperationalState_Type(Integer32):
    """Custom type frDteRgOperationalState based on Integer32"""
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


_FrDteRgOperationalState_Type.__name__ = "Integer32"
_FrDteRgOperationalState_Object = MibTableColumn
frDteRgOperationalState = _FrDteRgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 13, 1, 2),
    _FrDteRgOperationalState_Type()
)
frDteRgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgOperationalState.setStatus("mandatory")


class _FrDteRgUsageState_Type(Integer32):
    """Custom type frDteRgUsageState based on Integer32"""
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


_FrDteRgUsageState_Type.__name__ = "Integer32"
_FrDteRgUsageState_Object = MibTableColumn
frDteRgUsageState = _FrDteRgUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 13, 1, 3),
    _FrDteRgUsageState_Type()
)
frDteRgUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgUsageState.setStatus("mandatory")
_FrDteRgOperStatusTable_Object = MibTable
frDteRgOperStatusTable = _FrDteRgOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 14)
)
if mibBuilder.loadTexts:
    frDteRgOperStatusTable.setStatus("mandatory")
_FrDteRgOperStatusEntry_Object = MibTableRow
frDteRgOperStatusEntry = _FrDteRgOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 14, 1)
)
frDteRgOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
)
if mibBuilder.loadTexts:
    frDteRgOperStatusEntry.setStatus("mandatory")


class _FrDteRgSnmpOperStatus_Type(Integer32):
    """Custom type frDteRgSnmpOperStatus based on Integer32"""
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


_FrDteRgSnmpOperStatus_Type.__name__ = "Integer32"
_FrDteRgSnmpOperStatus_Object = MibTableColumn
frDteRgSnmpOperStatus = _FrDteRgSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 14, 1, 1),
    _FrDteRgSnmpOperStatus_Type()
)
frDteRgSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgSnmpOperStatus.setStatus("mandatory")
_FrDteRgBfr_ObjectIdentity = ObjectIdentity
frDteRgBfr = _FrDteRgBfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15)
)
_FrDteRgBfrRowStatusTable_Object = MibTable
frDteRgBfrRowStatusTable = _FrDteRgBfrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 1)
)
if mibBuilder.loadTexts:
    frDteRgBfrRowStatusTable.setStatus("mandatory")
_FrDteRgBfrRowStatusEntry_Object = MibTableRow
frDteRgBfrRowStatusEntry = _FrDteRgBfrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 1, 1)
)
frDteRgBfrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgBfrIndex"),
)
if mibBuilder.loadTexts:
    frDteRgBfrRowStatusEntry.setStatus("mandatory")
_FrDteRgBfrRowStatus_Type = RowStatus
_FrDteRgBfrRowStatus_Object = MibTableColumn
frDteRgBfrRowStatus = _FrDteRgBfrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 1, 1, 1),
    _FrDteRgBfrRowStatus_Type()
)
frDteRgBfrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteRgBfrRowStatus.setStatus("mandatory")
_FrDteRgBfrComponentName_Type = DisplayString
_FrDteRgBfrComponentName_Object = MibTableColumn
frDteRgBfrComponentName = _FrDteRgBfrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 1, 1, 2),
    _FrDteRgBfrComponentName_Type()
)
frDteRgBfrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgBfrComponentName.setStatus("mandatory")
_FrDteRgBfrStorageType_Type = StorageType
_FrDteRgBfrStorageType_Object = MibTableColumn
frDteRgBfrStorageType = _FrDteRgBfrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 1, 1, 4),
    _FrDteRgBfrStorageType_Type()
)
frDteRgBfrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgBfrStorageType.setStatus("mandatory")
_FrDteRgBfrIndex_Type = NonReplicated
_FrDteRgBfrIndex_Object = MibTableColumn
frDteRgBfrIndex = _FrDteRgBfrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 1, 1, 10),
    _FrDteRgBfrIndex_Type()
)
frDteRgBfrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteRgBfrIndex.setStatus("mandatory")
_FrDteRgBfrProvTable_Object = MibTable
frDteRgBfrProvTable = _FrDteRgBfrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 10)
)
if mibBuilder.loadTexts:
    frDteRgBfrProvTable.setStatus("mandatory")
_FrDteRgBfrProvEntry_Object = MibTableRow
frDteRgBfrProvEntry = _FrDteRgBfrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 10, 1)
)
frDteRgBfrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgBfrIndex"),
)
if mibBuilder.loadTexts:
    frDteRgBfrProvEntry.setStatus("mandatory")


class _FrDteRgBfrMacType_Type(Integer32):
    """Custom type frDteRgBfrMacType based on Integer32"""
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


_FrDteRgBfrMacType_Type.__name__ = "Integer32"
_FrDteRgBfrMacType_Object = MibTableColumn
frDteRgBfrMacType = _FrDteRgBfrMacType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 10, 1, 1),
    _FrDteRgBfrMacType_Type()
)
frDteRgBfrMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteRgBfrMacType.setStatus("mandatory")


class _FrDteRgBfrBfrIndex_Type(Integer32):
    """Custom type frDteRgBfrBfrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_FrDteRgBfrBfrIndex_Type.__name__ = "Integer32"
_FrDteRgBfrBfrIndex_Object = MibTableColumn
frDteRgBfrBfrIndex = _FrDteRgBfrBfrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 10, 1, 2),
    _FrDteRgBfrBfrIndex_Type()
)
frDteRgBfrBfrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteRgBfrBfrIndex.setStatus("mandatory")
_FrDteRgBfrOprTable_Object = MibTable
frDteRgBfrOprTable = _FrDteRgBfrOprTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 11)
)
if mibBuilder.loadTexts:
    frDteRgBfrOprTable.setStatus("mandatory")
_FrDteRgBfrOprEntry_Object = MibTableRow
frDteRgBfrOprEntry = _FrDteRgBfrOprEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 11, 1)
)
frDteRgBfrOprEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgBfrIndex"),
)
if mibBuilder.loadTexts:
    frDteRgBfrOprEntry.setStatus("mandatory")


class _FrDteRgBfrMacAddr_Type(DashedHexString):
    """Custom type frDteRgBfrMacAddr based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FrDteRgBfrMacAddr_Type.__name__ = "DashedHexString"
_FrDteRgBfrMacAddr_Object = MibTableColumn
frDteRgBfrMacAddr = _FrDteRgBfrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 15, 11, 1, 1),
    _FrDteRgBfrMacAddr_Type()
)
frDteRgBfrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRgBfrMacAddr.setStatus("mandatory")
_FrDteRgLtDlciTable_Object = MibTable
frDteRgLtDlciTable = _FrDteRgLtDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 219)
)
if mibBuilder.loadTexts:
    frDteRgLtDlciTable.setStatus("mandatory")
_FrDteRgLtDlciEntry_Object = MibTableRow
frDteRgLtDlciEntry = _FrDteRgLtDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 219, 1)
)
frDteRgLtDlciEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteRgLtDlciValue"),
)
if mibBuilder.loadTexts:
    frDteRgLtDlciEntry.setStatus("mandatory")
_FrDteRgLtDlciValue_Type = Link
_FrDteRgLtDlciValue_Object = MibTableColumn
frDteRgLtDlciValue = _FrDteRgLtDlciValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 219, 1, 1),
    _FrDteRgLtDlciValue_Type()
)
frDteRgLtDlciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteRgLtDlciValue.setStatus("mandatory")
_FrDteRgLtDlciRowStatus_Type = RowStatus
_FrDteRgLtDlciRowStatus_Object = MibTableColumn
frDteRgLtDlciRowStatus = _FrDteRgLtDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 4, 219, 1, 2),
    _FrDteRgLtDlciRowStatus_Type()
)
frDteRgLtDlciRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frDteRgLtDlciRowStatus.setStatus("mandatory")
_FrDteDynDlciDefs_ObjectIdentity = ObjectIdentity
frDteDynDlciDefs = _FrDteDynDlciDefs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5)
)
_FrDteDynDlciDefsRowStatusTable_Object = MibTable
frDteDynDlciDefsRowStatusTable = _FrDteDynDlciDefsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 1)
)
if mibBuilder.loadTexts:
    frDteDynDlciDefsRowStatusTable.setStatus("mandatory")
_FrDteDynDlciDefsRowStatusEntry_Object = MibTableRow
frDteDynDlciDefsRowStatusEntry = _FrDteDynDlciDefsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 1, 1)
)
frDteDynDlciDefsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteDynDlciDefsIndex"),
)
if mibBuilder.loadTexts:
    frDteDynDlciDefsRowStatusEntry.setStatus("mandatory")
_FrDteDynDlciDefsRowStatus_Type = RowStatus
_FrDteDynDlciDefsRowStatus_Object = MibTableColumn
frDteDynDlciDefsRowStatus = _FrDteDynDlciDefsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 1, 1, 1),
    _FrDteDynDlciDefsRowStatus_Type()
)
frDteDynDlciDefsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDynDlciDefsRowStatus.setStatus("mandatory")
_FrDteDynDlciDefsComponentName_Type = DisplayString
_FrDteDynDlciDefsComponentName_Object = MibTableColumn
frDteDynDlciDefsComponentName = _FrDteDynDlciDefsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 1, 1, 2),
    _FrDteDynDlciDefsComponentName_Type()
)
frDteDynDlciDefsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDynDlciDefsComponentName.setStatus("mandatory")
_FrDteDynDlciDefsStorageType_Type = StorageType
_FrDteDynDlciDefsStorageType_Object = MibTableColumn
frDteDynDlciDefsStorageType = _FrDteDynDlciDefsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 1, 1, 4),
    _FrDteDynDlciDefsStorageType_Type()
)
frDteDynDlciDefsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDynDlciDefsStorageType.setStatus("mandatory")
_FrDteDynDlciDefsIndex_Type = NonReplicated
_FrDteDynDlciDefsIndex_Object = MibTableColumn
frDteDynDlciDefsIndex = _FrDteDynDlciDefsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 1, 1, 10),
    _FrDteDynDlciDefsIndex_Type()
)
frDteDynDlciDefsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteDynDlciDefsIndex.setStatus("mandatory")
_FrDteDynDlciDefsProvTable_Object = MibTable
frDteDynDlciDefsProvTable = _FrDteDynDlciDefsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 10)
)
if mibBuilder.loadTexts:
    frDteDynDlciDefsProvTable.setStatus("mandatory")
_FrDteDynDlciDefsProvEntry_Object = MibTableRow
frDteDynDlciDefsProvEntry = _FrDteDynDlciDefsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 10, 1)
)
frDteDynDlciDefsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteDynDlciDefsIndex"),
)
if mibBuilder.loadTexts:
    frDteDynDlciDefsProvEntry.setStatus("mandatory")


class _FrDteDynDlciDefsStdRowStatus_Type(Integer32):
    """Custom type frDteDynDlciDefsStdRowStatus based on Integer32"""
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


_FrDteDynDlciDefsStdRowStatus_Type.__name__ = "Integer32"
_FrDteDynDlciDefsStdRowStatus_Object = MibTableColumn
frDteDynDlciDefsStdRowStatus = _FrDteDynDlciDefsStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 10, 1, 1),
    _FrDteDynDlciDefsStdRowStatus_Type()
)
frDteDynDlciDefsStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDynDlciDefsStdRowStatus.setStatus("mandatory")


class _FrDteDynDlciDefsRateEnforcement_Type(Integer32):
    """Custom type frDteDynDlciDefsRateEnforcement based on Integer32"""
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


_FrDteDynDlciDefsRateEnforcement_Type.__name__ = "Integer32"
_FrDteDynDlciDefsRateEnforcement_Object = MibTableColumn
frDteDynDlciDefsRateEnforcement = _FrDteDynDlciDefsRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 10, 1, 2),
    _FrDteDynDlciDefsRateEnforcement_Type()
)
frDteDynDlciDefsRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDynDlciDefsRateEnforcement.setStatus("mandatory")


class _FrDteDynDlciDefsCommittedInformationRate_Type(Unsigned32):
    """Custom type frDteDynDlciDefsCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48000000),
    )


_FrDteDynDlciDefsCommittedInformationRate_Type.__name__ = "Unsigned32"
_FrDteDynDlciDefsCommittedInformationRate_Object = MibTableColumn
frDteDynDlciDefsCommittedInformationRate = _FrDteDynDlciDefsCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 10, 1, 3),
    _FrDteDynDlciDefsCommittedInformationRate_Type()
)
frDteDynDlciDefsCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDynDlciDefsCommittedInformationRate.setStatus("mandatory")


class _FrDteDynDlciDefsCommittedBurst_Type(Unsigned32):
    """Custom type frDteDynDlciDefsCommittedBurst based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FrDteDynDlciDefsCommittedBurst_Type.__name__ = "Unsigned32"
_FrDteDynDlciDefsCommittedBurst_Object = MibTableColumn
frDteDynDlciDefsCommittedBurst = _FrDteDynDlciDefsCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 10, 1, 4),
    _FrDteDynDlciDefsCommittedBurst_Type()
)
frDteDynDlciDefsCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDynDlciDefsCommittedBurst.setStatus("mandatory")


class _FrDteDynDlciDefsExcessBurst_Type(Unsigned32):
    """Custom type frDteDynDlciDefsExcessBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FrDteDynDlciDefsExcessBurst_Type.__name__ = "Unsigned32"
_FrDteDynDlciDefsExcessBurst_Object = MibTableColumn
frDteDynDlciDefsExcessBurst = _FrDteDynDlciDefsExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 10, 1, 5),
    _FrDteDynDlciDefsExcessBurst_Type()
)
frDteDynDlciDefsExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDynDlciDefsExcessBurst.setStatus("mandatory")


class _FrDteDynDlciDefsExcessBurstAction_Type(Integer32):
    """Custom type frDteDynDlciDefsExcessBurstAction based on Integer32"""
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


_FrDteDynDlciDefsExcessBurstAction_Type.__name__ = "Integer32"
_FrDteDynDlciDefsExcessBurstAction_Object = MibTableColumn
frDteDynDlciDefsExcessBurstAction = _FrDteDynDlciDefsExcessBurstAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 10, 1, 6),
    _FrDteDynDlciDefsExcessBurstAction_Type()
)
frDteDynDlciDefsExcessBurstAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDynDlciDefsExcessBurstAction.setStatus("mandatory")


class _FrDteDynDlciDefsIpCos_Type(Unsigned32):
    """Custom type frDteDynDlciDefsIpCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrDteDynDlciDefsIpCos_Type.__name__ = "Unsigned32"
_FrDteDynDlciDefsIpCos_Object = MibTableColumn
frDteDynDlciDefsIpCos = _FrDteDynDlciDefsIpCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 5, 10, 1, 7),
    _FrDteDynDlciDefsIpCos_Type()
)
frDteDynDlciDefsIpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDynDlciDefsIpCos.setStatus("mandatory")
_FrDteStDlci_ObjectIdentity = ObjectIdentity
frDteStDlci = _FrDteStDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6)
)
_FrDteStDlciRowStatusTable_Object = MibTable
frDteStDlciRowStatusTable = _FrDteStDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 1)
)
if mibBuilder.loadTexts:
    frDteStDlciRowStatusTable.setStatus("mandatory")
_FrDteStDlciRowStatusEntry_Object = MibTableRow
frDteStDlciRowStatusEntry = _FrDteStDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 1, 1)
)
frDteStDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciIndex"),
)
if mibBuilder.loadTexts:
    frDteStDlciRowStatusEntry.setStatus("mandatory")
_FrDteStDlciRowStatus_Type = RowStatus
_FrDteStDlciRowStatus_Object = MibTableColumn
frDteStDlciRowStatus = _FrDteStDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 1, 1, 1),
    _FrDteStDlciRowStatus_Type()
)
frDteStDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciRowStatus.setStatus("mandatory")
_FrDteStDlciComponentName_Type = DisplayString
_FrDteStDlciComponentName_Object = MibTableColumn
frDteStDlciComponentName = _FrDteStDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 1, 1, 2),
    _FrDteStDlciComponentName_Type()
)
frDteStDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciComponentName.setStatus("mandatory")
_FrDteStDlciStorageType_Type = StorageType
_FrDteStDlciStorageType_Object = MibTableColumn
frDteStDlciStorageType = _FrDteStDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 1, 1, 4),
    _FrDteStDlciStorageType_Type()
)
frDteStDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciStorageType.setStatus("mandatory")


class _FrDteStDlciIndex_Type(Integer32):
    """Custom type frDteStDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrDteStDlciIndex_Type.__name__ = "Integer32"
_FrDteStDlciIndex_Object = MibTableColumn
frDteStDlciIndex = _FrDteStDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 1, 1, 10),
    _FrDteStDlciIndex_Type()
)
frDteStDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteStDlciIndex.setStatus("mandatory")
_FrDteStDlciHq_ObjectIdentity = ObjectIdentity
frDteStDlciHq = _FrDteStDlciHq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2)
)
_FrDteStDlciHqRowStatusTable_Object = MibTable
frDteStDlciHqRowStatusTable = _FrDteStDlciHqRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 1)
)
if mibBuilder.loadTexts:
    frDteStDlciHqRowStatusTable.setStatus("mandatory")
_FrDteStDlciHqRowStatusEntry_Object = MibTableRow
frDteStDlciHqRowStatusEntry = _FrDteStDlciHqRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 1, 1)
)
frDteStDlciHqRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    frDteStDlciHqRowStatusEntry.setStatus("mandatory")
_FrDteStDlciHqRowStatus_Type = RowStatus
_FrDteStDlciHqRowStatus_Object = MibTableColumn
frDteStDlciHqRowStatus = _FrDteStDlciHqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 1, 1, 1),
    _FrDteStDlciHqRowStatus_Type()
)
frDteStDlciHqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciHqRowStatus.setStatus("mandatory")
_FrDteStDlciHqComponentName_Type = DisplayString
_FrDteStDlciHqComponentName_Object = MibTableColumn
frDteStDlciHqComponentName = _FrDteStDlciHqComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 1, 1, 2),
    _FrDteStDlciHqComponentName_Type()
)
frDteStDlciHqComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqComponentName.setStatus("mandatory")
_FrDteStDlciHqStorageType_Type = StorageType
_FrDteStDlciHqStorageType_Object = MibTableColumn
frDteStDlciHqStorageType = _FrDteStDlciHqStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 1, 1, 4),
    _FrDteStDlciHqStorageType_Type()
)
frDteStDlciHqStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqStorageType.setStatus("mandatory")
_FrDteStDlciHqIndex_Type = NonReplicated
_FrDteStDlciHqIndex_Object = MibTableColumn
frDteStDlciHqIndex = _FrDteStDlciHqIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 1, 1, 10),
    _FrDteStDlciHqIndex_Type()
)
frDteStDlciHqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteStDlciHqIndex.setStatus("mandatory")
_FrDteStDlciHqProvTable_Object = MibTable
frDteStDlciHqProvTable = _FrDteStDlciHqProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 10)
)
if mibBuilder.loadTexts:
    frDteStDlciHqProvTable.setStatus("mandatory")
_FrDteStDlciHqProvEntry_Object = MibTableRow
frDteStDlciHqProvEntry = _FrDteStDlciHqProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 10, 1)
)
frDteStDlciHqProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    frDteStDlciHqProvEntry.setStatus("mandatory")


class _FrDteStDlciHqMaxPackets_Type(Unsigned32):
    """Custom type frDteStDlciHqMaxPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_FrDteStDlciHqMaxPackets_Type.__name__ = "Unsigned32"
_FrDteStDlciHqMaxPackets_Object = MibTableColumn
frDteStDlciHqMaxPackets = _FrDteStDlciHqMaxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 10, 1, 1),
    _FrDteStDlciHqMaxPackets_Type()
)
frDteStDlciHqMaxPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciHqMaxPackets.setStatus("mandatory")


class _FrDteStDlciHqMaxMsecData_Type(Unsigned32):
    """Custom type frDteStDlciHqMaxMsecData based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_FrDteStDlciHqMaxMsecData_Type.__name__ = "Unsigned32"
_FrDteStDlciHqMaxMsecData_Object = MibTableColumn
frDteStDlciHqMaxMsecData = _FrDteStDlciHqMaxMsecData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 10, 1, 2),
    _FrDteStDlciHqMaxMsecData_Type()
)
frDteStDlciHqMaxMsecData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciHqMaxMsecData.setStatus("mandatory")


class _FrDteStDlciHqMaxPercentMulticast_Type(Unsigned32):
    """Custom type frDteStDlciHqMaxPercentMulticast based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FrDteStDlciHqMaxPercentMulticast_Type.__name__ = "Unsigned32"
_FrDteStDlciHqMaxPercentMulticast_Object = MibTableColumn
frDteStDlciHqMaxPercentMulticast = _FrDteStDlciHqMaxPercentMulticast_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 10, 1, 3),
    _FrDteStDlciHqMaxPercentMulticast_Type()
)
frDteStDlciHqMaxPercentMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciHqMaxPercentMulticast.setStatus("mandatory")


class _FrDteStDlciHqTimeToLive_Type(Unsigned32):
    """Custom type frDteStDlciHqTimeToLive based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_FrDteStDlciHqTimeToLive_Type.__name__ = "Unsigned32"
_FrDteStDlciHqTimeToLive_Object = MibTableColumn
frDteStDlciHqTimeToLive = _FrDteStDlciHqTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 10, 1, 4),
    _FrDteStDlciHqTimeToLive_Type()
)
frDteStDlciHqTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciHqTimeToLive.setStatus("mandatory")
_FrDteStDlciHqStatsTable_Object = MibTable
frDteStDlciHqStatsTable = _FrDteStDlciHqStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 11)
)
if mibBuilder.loadTexts:
    frDteStDlciHqStatsTable.setStatus("mandatory")
_FrDteStDlciHqStatsEntry_Object = MibTableRow
frDteStDlciHqStatsEntry = _FrDteStDlciHqStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 11, 1)
)
frDteStDlciHqStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    frDteStDlciHqStatsEntry.setStatus("mandatory")
_FrDteStDlciHqTimedOutPkt_Type = Counter32
_FrDteStDlciHqTimedOutPkt_Object = MibTableColumn
frDteStDlciHqTimedOutPkt = _FrDteStDlciHqTimedOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 11, 1, 1),
    _FrDteStDlciHqTimedOutPkt_Type()
)
frDteStDlciHqTimedOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqTimedOutPkt.setStatus("mandatory")
_FrDteStDlciHqQueuePurgeDiscards_Type = Counter32
_FrDteStDlciHqQueuePurgeDiscards_Object = MibTableColumn
frDteStDlciHqQueuePurgeDiscards = _FrDteStDlciHqQueuePurgeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 11, 1, 2),
    _FrDteStDlciHqQueuePurgeDiscards_Type()
)
frDteStDlciHqQueuePurgeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqQueuePurgeDiscards.setStatus("mandatory")
_FrDteStDlciHqTStatsTable_Object = MibTable
frDteStDlciHqTStatsTable = _FrDteStDlciHqTStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 12)
)
if mibBuilder.loadTexts:
    frDteStDlciHqTStatsTable.setStatus("mandatory")
_FrDteStDlciHqTStatsEntry_Object = MibTableRow
frDteStDlciHqTStatsEntry = _FrDteStDlciHqTStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 12, 1)
)
frDteStDlciHqTStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    frDteStDlciHqTStatsEntry.setStatus("mandatory")
_FrDteStDlciHqTotalPktHandled_Type = Counter32
_FrDteStDlciHqTotalPktHandled_Object = MibTableColumn
frDteStDlciHqTotalPktHandled = _FrDteStDlciHqTotalPktHandled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 12, 1, 1),
    _FrDteStDlciHqTotalPktHandled_Type()
)
frDteStDlciHqTotalPktHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqTotalPktHandled.setStatus("mandatory")
_FrDteStDlciHqTotalPktForwarded_Type = Counter32
_FrDteStDlciHqTotalPktForwarded_Object = MibTableColumn
frDteStDlciHqTotalPktForwarded = _FrDteStDlciHqTotalPktForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 12, 1, 2),
    _FrDteStDlciHqTotalPktForwarded_Type()
)
frDteStDlciHqTotalPktForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqTotalPktForwarded.setStatus("mandatory")
_FrDteStDlciHqTotalPktQueued_Type = Counter32
_FrDteStDlciHqTotalPktQueued_Object = MibTableColumn
frDteStDlciHqTotalPktQueued = _FrDteStDlciHqTotalPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 12, 1, 3),
    _FrDteStDlciHqTotalPktQueued_Type()
)
frDteStDlciHqTotalPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqTotalPktQueued.setStatus("mandatory")
_FrDteStDlciHqTotalMulticastPkt_Type = Counter32
_FrDteStDlciHqTotalMulticastPkt_Object = MibTableColumn
frDteStDlciHqTotalMulticastPkt = _FrDteStDlciHqTotalMulticastPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 12, 1, 4),
    _FrDteStDlciHqTotalMulticastPkt_Type()
)
frDteStDlciHqTotalMulticastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqTotalMulticastPkt.setStatus("mandatory")
_FrDteStDlciHqTotalPktDiscards_Type = Counter32
_FrDteStDlciHqTotalPktDiscards_Object = MibTableColumn
frDteStDlciHqTotalPktDiscards = _FrDteStDlciHqTotalPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 12, 1, 5),
    _FrDteStDlciHqTotalPktDiscards_Type()
)
frDteStDlciHqTotalPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqTotalPktDiscards.setStatus("mandatory")
_FrDteStDlciHqCStatsTable_Object = MibTable
frDteStDlciHqCStatsTable = _FrDteStDlciHqCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 13)
)
if mibBuilder.loadTexts:
    frDteStDlciHqCStatsTable.setStatus("mandatory")
_FrDteStDlciHqCStatsEntry_Object = MibTableRow
frDteStDlciHqCStatsEntry = _FrDteStDlciHqCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 13, 1)
)
frDteStDlciHqCStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    frDteStDlciHqCStatsEntry.setStatus("mandatory")


class _FrDteStDlciHqCurrentPktQueued_Type(Gauge32):
    """Custom type frDteStDlciHqCurrentPktQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteStDlciHqCurrentPktQueued_Type.__name__ = "Gauge32"
_FrDteStDlciHqCurrentPktQueued_Object = MibTableColumn
frDteStDlciHqCurrentPktQueued = _FrDteStDlciHqCurrentPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 13, 1, 1),
    _FrDteStDlciHqCurrentPktQueued_Type()
)
frDteStDlciHqCurrentPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqCurrentPktQueued.setStatus("mandatory")


class _FrDteStDlciHqCurrentBytesQueued_Type(Gauge32):
    """Custom type frDteStDlciHqCurrentBytesQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteStDlciHqCurrentBytesQueued_Type.__name__ = "Gauge32"
_FrDteStDlciHqCurrentBytesQueued_Object = MibTableColumn
frDteStDlciHqCurrentBytesQueued = _FrDteStDlciHqCurrentBytesQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 13, 1, 2),
    _FrDteStDlciHqCurrentBytesQueued_Type()
)
frDteStDlciHqCurrentBytesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqCurrentBytesQueued.setStatus("mandatory")


class _FrDteStDlciHqCurrentMulticastQueued_Type(Gauge32):
    """Custom type frDteStDlciHqCurrentMulticastQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteStDlciHqCurrentMulticastQueued_Type.__name__ = "Gauge32"
_FrDteStDlciHqCurrentMulticastQueued_Object = MibTableColumn
frDteStDlciHqCurrentMulticastQueued = _FrDteStDlciHqCurrentMulticastQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 13, 1, 3),
    _FrDteStDlciHqCurrentMulticastQueued_Type()
)
frDteStDlciHqCurrentMulticastQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqCurrentMulticastQueued.setStatus("mandatory")
_FrDteStDlciHqThrStatsTable_Object = MibTable
frDteStDlciHqThrStatsTable = _FrDteStDlciHqThrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 14)
)
if mibBuilder.loadTexts:
    frDteStDlciHqThrStatsTable.setStatus("mandatory")
_FrDteStDlciHqThrStatsEntry_Object = MibTableRow
frDteStDlciHqThrStatsEntry = _FrDteStDlciHqThrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 14, 1)
)
frDteStDlciHqThrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciHqIndex"),
)
if mibBuilder.loadTexts:
    frDteStDlciHqThrStatsEntry.setStatus("mandatory")


class _FrDteStDlciHqQueuePktThreshold_Type(Unsigned32):
    """Custom type frDteStDlciHqQueuePktThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteStDlciHqQueuePktThreshold_Type.__name__ = "Unsigned32"
_FrDteStDlciHqQueuePktThreshold_Object = MibTableColumn
frDteStDlciHqQueuePktThreshold = _FrDteStDlciHqQueuePktThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 14, 1, 1),
    _FrDteStDlciHqQueuePktThreshold_Type()
)
frDteStDlciHqQueuePktThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqQueuePktThreshold.setStatus("mandatory")
_FrDteStDlciHqPktThresholdExceeded_Type = Counter32
_FrDteStDlciHqPktThresholdExceeded_Object = MibTableColumn
frDteStDlciHqPktThresholdExceeded = _FrDteStDlciHqPktThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 14, 1, 2),
    _FrDteStDlciHqPktThresholdExceeded_Type()
)
frDteStDlciHqPktThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqPktThresholdExceeded.setStatus("mandatory")


class _FrDteStDlciHqQueueByteThreshold_Type(Unsigned32):
    """Custom type frDteStDlciHqQueueByteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteStDlciHqQueueByteThreshold_Type.__name__ = "Unsigned32"
_FrDteStDlciHqQueueByteThreshold_Object = MibTableColumn
frDteStDlciHqQueueByteThreshold = _FrDteStDlciHqQueueByteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 14, 1, 3),
    _FrDteStDlciHqQueueByteThreshold_Type()
)
frDteStDlciHqQueueByteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqQueueByteThreshold.setStatus("mandatory")
_FrDteStDlciHqByteThresholdExceeded_Type = Counter32
_FrDteStDlciHqByteThresholdExceeded_Object = MibTableColumn
frDteStDlciHqByteThresholdExceeded = _FrDteStDlciHqByteThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 14, 1, 4),
    _FrDteStDlciHqByteThresholdExceeded_Type()
)
frDteStDlciHqByteThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqByteThresholdExceeded.setStatus("mandatory")


class _FrDteStDlciHqQueueMulticastThreshold_Type(Unsigned32):
    """Custom type frDteStDlciHqQueueMulticastThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteStDlciHqQueueMulticastThreshold_Type.__name__ = "Unsigned32"
_FrDteStDlciHqQueueMulticastThreshold_Object = MibTableColumn
frDteStDlciHqQueueMulticastThreshold = _FrDteStDlciHqQueueMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 14, 1, 5),
    _FrDteStDlciHqQueueMulticastThreshold_Type()
)
frDteStDlciHqQueueMulticastThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqQueueMulticastThreshold.setStatus("mandatory")
_FrDteStDlciHqMulThresholdExceeded_Type = Counter32
_FrDteStDlciHqMulThresholdExceeded_Object = MibTableColumn
frDteStDlciHqMulThresholdExceeded = _FrDteStDlciHqMulThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 14, 1, 6),
    _FrDteStDlciHqMulThresholdExceeded_Type()
)
frDteStDlciHqMulThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqMulThresholdExceeded.setStatus("mandatory")
_FrDteStDlciHqMemThresholdExceeded_Type = Counter32
_FrDteStDlciHqMemThresholdExceeded_Object = MibTableColumn
frDteStDlciHqMemThresholdExceeded = _FrDteStDlciHqMemThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 2, 14, 1, 7),
    _FrDteStDlciHqMemThresholdExceeded_Type()
)
frDteStDlciHqMemThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteStDlciHqMemThresholdExceeded.setStatus("mandatory")
_FrDteStDlciProvTable_Object = MibTable
frDteStDlciProvTable = _FrDteStDlciProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 10)
)
if mibBuilder.loadTexts:
    frDteStDlciProvTable.setStatus("mandatory")
_FrDteStDlciProvEntry_Object = MibTableRow
frDteStDlciProvEntry = _FrDteStDlciProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 10, 1)
)
frDteStDlciProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciIndex"),
)
if mibBuilder.loadTexts:
    frDteStDlciProvEntry.setStatus("mandatory")


class _FrDteStDlciStdRowStatus_Type(Integer32):
    """Custom type frDteStDlciStdRowStatus based on Integer32"""
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


_FrDteStDlciStdRowStatus_Type.__name__ = "Integer32"
_FrDteStDlciStdRowStatus_Object = MibTableColumn
frDteStDlciStdRowStatus = _FrDteStDlciStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 10, 1, 1),
    _FrDteStDlciStdRowStatus_Type()
)
frDteStDlciStdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciStdRowStatus.setStatus("mandatory")


class _FrDteStDlciRateEnforcement_Type(Integer32):
    """Custom type frDteStDlciRateEnforcement based on Integer32"""
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


_FrDteStDlciRateEnforcement_Type.__name__ = "Integer32"
_FrDteStDlciRateEnforcement_Object = MibTableColumn
frDteStDlciRateEnforcement = _FrDteStDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 10, 1, 2),
    _FrDteStDlciRateEnforcement_Type()
)
frDteStDlciRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciRateEnforcement.setStatus("mandatory")


class _FrDteStDlciCommittedInformationRate_Type(Unsigned32):
    """Custom type frDteStDlciCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48000000),
    )


_FrDteStDlciCommittedInformationRate_Type.__name__ = "Unsigned32"
_FrDteStDlciCommittedInformationRate_Object = MibTableColumn
frDteStDlciCommittedInformationRate = _FrDteStDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 10, 1, 3),
    _FrDteStDlciCommittedInformationRate_Type()
)
frDteStDlciCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciCommittedInformationRate.setStatus("mandatory")


class _FrDteStDlciCommittedBurst_Type(Unsigned32):
    """Custom type frDteStDlciCommittedBurst based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FrDteStDlciCommittedBurst_Type.__name__ = "Unsigned32"
_FrDteStDlciCommittedBurst_Object = MibTableColumn
frDteStDlciCommittedBurst = _FrDteStDlciCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 10, 1, 4),
    _FrDteStDlciCommittedBurst_Type()
)
frDteStDlciCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciCommittedBurst.setStatus("mandatory")


class _FrDteStDlciExcessBurst_Type(Unsigned32):
    """Custom type frDteStDlciExcessBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FrDteStDlciExcessBurst_Type.__name__ = "Unsigned32"
_FrDteStDlciExcessBurst_Object = MibTableColumn
frDteStDlciExcessBurst = _FrDteStDlciExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 10, 1, 5),
    _FrDteStDlciExcessBurst_Type()
)
frDteStDlciExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciExcessBurst.setStatus("mandatory")


class _FrDteStDlciExcessBurstAction_Type(Integer32):
    """Custom type frDteStDlciExcessBurstAction based on Integer32"""
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


_FrDteStDlciExcessBurstAction_Type.__name__ = "Integer32"
_FrDteStDlciExcessBurstAction_Object = MibTableColumn
frDteStDlciExcessBurstAction = _FrDteStDlciExcessBurstAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 10, 1, 6),
    _FrDteStDlciExcessBurstAction_Type()
)
frDteStDlciExcessBurstAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciExcessBurstAction.setStatus("mandatory")


class _FrDteStDlciIpCos_Type(Unsigned32):
    """Custom type frDteStDlciIpCos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrDteStDlciIpCos_Type.__name__ = "Unsigned32"
_FrDteStDlciIpCos_Object = MibTableColumn
frDteStDlciIpCos = _FrDteStDlciIpCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 10, 1, 7),
    _FrDteStDlciIpCos_Type()
)
frDteStDlciIpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciIpCos.setStatus("mandatory")
_FrDteStDlciRgLinkTable_Object = MibTable
frDteStDlciRgLinkTable = _FrDteStDlciRgLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 11)
)
if mibBuilder.loadTexts:
    frDteStDlciRgLinkTable.setStatus("mandatory")
_FrDteStDlciRgLinkEntry_Object = MibTableRow
frDteStDlciRgLinkEntry = _FrDteStDlciRgLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 11, 1)
)
frDteStDlciRgLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteStDlciIndex"),
)
if mibBuilder.loadTexts:
    frDteStDlciRgLinkEntry.setStatus("mandatory")
_FrDteStDlciLinkToRemoteGroup_Type = Link
_FrDteStDlciLinkToRemoteGroup_Object = MibTableColumn
frDteStDlciLinkToRemoteGroup = _FrDteStDlciLinkToRemoteGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 6, 11, 1, 1),
    _FrDteStDlciLinkToRemoteGroup_Type()
)
frDteStDlciLinkToRemoteGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteStDlciLinkToRemoteGroup.setStatus("mandatory")
_FrDteLeq_ObjectIdentity = ObjectIdentity
frDteLeq = _FrDteLeq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7)
)
_FrDteLeqRowStatusTable_Object = MibTable
frDteLeqRowStatusTable = _FrDteLeqRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 1)
)
if mibBuilder.loadTexts:
    frDteLeqRowStatusTable.setStatus("mandatory")
_FrDteLeqRowStatusEntry_Object = MibTableRow
frDteLeqRowStatusEntry = _FrDteLeqRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 1, 1)
)
frDteLeqRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteLeqIndex"),
)
if mibBuilder.loadTexts:
    frDteLeqRowStatusEntry.setStatus("mandatory")
_FrDteLeqRowStatus_Type = RowStatus
_FrDteLeqRowStatus_Object = MibTableColumn
frDteLeqRowStatus = _FrDteLeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 1, 1, 1),
    _FrDteLeqRowStatus_Type()
)
frDteLeqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLeqRowStatus.setStatus("mandatory")
_FrDteLeqComponentName_Type = DisplayString
_FrDteLeqComponentName_Object = MibTableColumn
frDteLeqComponentName = _FrDteLeqComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 1, 1, 2),
    _FrDteLeqComponentName_Type()
)
frDteLeqComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqComponentName.setStatus("mandatory")
_FrDteLeqStorageType_Type = StorageType
_FrDteLeqStorageType_Object = MibTableColumn
frDteLeqStorageType = _FrDteLeqStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 1, 1, 4),
    _FrDteLeqStorageType_Type()
)
frDteLeqStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqStorageType.setStatus("mandatory")
_FrDteLeqIndex_Type = NonReplicated
_FrDteLeqIndex_Object = MibTableColumn
frDteLeqIndex = _FrDteLeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 1, 1, 10),
    _FrDteLeqIndex_Type()
)
frDteLeqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteLeqIndex.setStatus("mandatory")
_FrDteLeqProvTable_Object = MibTable
frDteLeqProvTable = _FrDteLeqProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 10)
)
if mibBuilder.loadTexts:
    frDteLeqProvTable.setStatus("mandatory")
_FrDteLeqProvEntry_Object = MibTableRow
frDteLeqProvEntry = _FrDteLeqProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 10, 1)
)
frDteLeqProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteLeqIndex"),
)
if mibBuilder.loadTexts:
    frDteLeqProvEntry.setStatus("mandatory")


class _FrDteLeqMaxPackets_Type(Unsigned32):
    """Custom type frDteLeqMaxPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_FrDteLeqMaxPackets_Type.__name__ = "Unsigned32"
_FrDteLeqMaxPackets_Object = MibTableColumn
frDteLeqMaxPackets = _FrDteLeqMaxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 10, 1, 1),
    _FrDteLeqMaxPackets_Type()
)
frDteLeqMaxPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLeqMaxPackets.setStatus("mandatory")


class _FrDteLeqMaxMsecData_Type(Unsigned32):
    """Custom type frDteLeqMaxMsecData based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_FrDteLeqMaxMsecData_Type.__name__ = "Unsigned32"
_FrDteLeqMaxMsecData_Object = MibTableColumn
frDteLeqMaxMsecData = _FrDteLeqMaxMsecData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 10, 1, 2),
    _FrDteLeqMaxMsecData_Type()
)
frDteLeqMaxMsecData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLeqMaxMsecData.setStatus("mandatory")


class _FrDteLeqMaxPercentMulticast_Type(Unsigned32):
    """Custom type frDteLeqMaxPercentMulticast based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FrDteLeqMaxPercentMulticast_Type.__name__ = "Unsigned32"
_FrDteLeqMaxPercentMulticast_Object = MibTableColumn
frDteLeqMaxPercentMulticast = _FrDteLeqMaxPercentMulticast_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 10, 1, 3),
    _FrDteLeqMaxPercentMulticast_Type()
)
frDteLeqMaxPercentMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLeqMaxPercentMulticast.setStatus("mandatory")


class _FrDteLeqTimeToLive_Type(Unsigned32):
    """Custom type frDteLeqTimeToLive based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_FrDteLeqTimeToLive_Type.__name__ = "Unsigned32"
_FrDteLeqTimeToLive_Object = MibTableColumn
frDteLeqTimeToLive = _FrDteLeqTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 10, 1, 4),
    _FrDteLeqTimeToLive_Type()
)
frDteLeqTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteLeqTimeToLive.setStatus("mandatory")
_FrDteLeqStatsTable_Object = MibTable
frDteLeqStatsTable = _FrDteLeqStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 11)
)
if mibBuilder.loadTexts:
    frDteLeqStatsTable.setStatus("mandatory")
_FrDteLeqStatsEntry_Object = MibTableRow
frDteLeqStatsEntry = _FrDteLeqStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 11, 1)
)
frDteLeqStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteLeqIndex"),
)
if mibBuilder.loadTexts:
    frDteLeqStatsEntry.setStatus("mandatory")
_FrDteLeqTimedOutPkt_Type = Counter32
_FrDteLeqTimedOutPkt_Object = MibTableColumn
frDteLeqTimedOutPkt = _FrDteLeqTimedOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 11, 1, 1),
    _FrDteLeqTimedOutPkt_Type()
)
frDteLeqTimedOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqTimedOutPkt.setStatus("mandatory")
_FrDteLeqHardwareForcedPkt_Type = Counter32
_FrDteLeqHardwareForcedPkt_Object = MibTableColumn
frDteLeqHardwareForcedPkt = _FrDteLeqHardwareForcedPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 11, 1, 2),
    _FrDteLeqHardwareForcedPkt_Type()
)
frDteLeqHardwareForcedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqHardwareForcedPkt.setStatus("mandatory")
_FrDteLeqForcedPktDiscards_Type = Counter32
_FrDteLeqForcedPktDiscards_Object = MibTableColumn
frDteLeqForcedPktDiscards = _FrDteLeqForcedPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 11, 1, 3),
    _FrDteLeqForcedPktDiscards_Type()
)
frDteLeqForcedPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqForcedPktDiscards.setStatus("mandatory")
_FrDteLeqQueuePurgeDiscards_Type = Counter32
_FrDteLeqQueuePurgeDiscards_Object = MibTableColumn
frDteLeqQueuePurgeDiscards = _FrDteLeqQueuePurgeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 11, 1, 4),
    _FrDteLeqQueuePurgeDiscards_Type()
)
frDteLeqQueuePurgeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqQueuePurgeDiscards.setStatus("mandatory")
_FrDteLeqTStatsTable_Object = MibTable
frDteLeqTStatsTable = _FrDteLeqTStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 12)
)
if mibBuilder.loadTexts:
    frDteLeqTStatsTable.setStatus("mandatory")
_FrDteLeqTStatsEntry_Object = MibTableRow
frDteLeqTStatsEntry = _FrDteLeqTStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 12, 1)
)
frDteLeqTStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteLeqIndex"),
)
if mibBuilder.loadTexts:
    frDteLeqTStatsEntry.setStatus("mandatory")
_FrDteLeqTotalPktHandled_Type = Counter32
_FrDteLeqTotalPktHandled_Object = MibTableColumn
frDteLeqTotalPktHandled = _FrDteLeqTotalPktHandled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 12, 1, 1),
    _FrDteLeqTotalPktHandled_Type()
)
frDteLeqTotalPktHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqTotalPktHandled.setStatus("mandatory")
_FrDteLeqTotalPktForwarded_Type = Counter32
_FrDteLeqTotalPktForwarded_Object = MibTableColumn
frDteLeqTotalPktForwarded = _FrDteLeqTotalPktForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 12, 1, 2),
    _FrDteLeqTotalPktForwarded_Type()
)
frDteLeqTotalPktForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqTotalPktForwarded.setStatus("mandatory")
_FrDteLeqTotalPktQueued_Type = Counter32
_FrDteLeqTotalPktQueued_Object = MibTableColumn
frDteLeqTotalPktQueued = _FrDteLeqTotalPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 12, 1, 3),
    _FrDteLeqTotalPktQueued_Type()
)
frDteLeqTotalPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqTotalPktQueued.setStatus("mandatory")
_FrDteLeqTotalMulticastPkt_Type = Counter32
_FrDteLeqTotalMulticastPkt_Object = MibTableColumn
frDteLeqTotalMulticastPkt = _FrDteLeqTotalMulticastPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 12, 1, 4),
    _FrDteLeqTotalMulticastPkt_Type()
)
frDteLeqTotalMulticastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqTotalMulticastPkt.setStatus("mandatory")
_FrDteLeqTotalPktDiscards_Type = Counter32
_FrDteLeqTotalPktDiscards_Object = MibTableColumn
frDteLeqTotalPktDiscards = _FrDteLeqTotalPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 12, 1, 5),
    _FrDteLeqTotalPktDiscards_Type()
)
frDteLeqTotalPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqTotalPktDiscards.setStatus("mandatory")
_FrDteLeqCStatsTable_Object = MibTable
frDteLeqCStatsTable = _FrDteLeqCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 13)
)
if mibBuilder.loadTexts:
    frDteLeqCStatsTable.setStatus("mandatory")
_FrDteLeqCStatsEntry_Object = MibTableRow
frDteLeqCStatsEntry = _FrDteLeqCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 13, 1)
)
frDteLeqCStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteLeqIndex"),
)
if mibBuilder.loadTexts:
    frDteLeqCStatsEntry.setStatus("mandatory")


class _FrDteLeqCurrentPktQueued_Type(Gauge32):
    """Custom type frDteLeqCurrentPktQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteLeqCurrentPktQueued_Type.__name__ = "Gauge32"
_FrDteLeqCurrentPktQueued_Object = MibTableColumn
frDteLeqCurrentPktQueued = _FrDteLeqCurrentPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 13, 1, 1),
    _FrDteLeqCurrentPktQueued_Type()
)
frDteLeqCurrentPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqCurrentPktQueued.setStatus("mandatory")


class _FrDteLeqCurrentBytesQueued_Type(Gauge32):
    """Custom type frDteLeqCurrentBytesQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteLeqCurrentBytesQueued_Type.__name__ = "Gauge32"
_FrDteLeqCurrentBytesQueued_Object = MibTableColumn
frDteLeqCurrentBytesQueued = _FrDteLeqCurrentBytesQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 13, 1, 2),
    _FrDteLeqCurrentBytesQueued_Type()
)
frDteLeqCurrentBytesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqCurrentBytesQueued.setStatus("mandatory")


class _FrDteLeqCurrentMulticastQueued_Type(Gauge32):
    """Custom type frDteLeqCurrentMulticastQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteLeqCurrentMulticastQueued_Type.__name__ = "Gauge32"
_FrDteLeqCurrentMulticastQueued_Object = MibTableColumn
frDteLeqCurrentMulticastQueued = _FrDteLeqCurrentMulticastQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 13, 1, 3),
    _FrDteLeqCurrentMulticastQueued_Type()
)
frDteLeqCurrentMulticastQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqCurrentMulticastQueued.setStatus("mandatory")
_FrDteLeqThrStatsTable_Object = MibTable
frDteLeqThrStatsTable = _FrDteLeqThrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 14)
)
if mibBuilder.loadTexts:
    frDteLeqThrStatsTable.setStatus("mandatory")
_FrDteLeqThrStatsEntry_Object = MibTableRow
frDteLeqThrStatsEntry = _FrDteLeqThrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 14, 1)
)
frDteLeqThrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteLeqIndex"),
)
if mibBuilder.loadTexts:
    frDteLeqThrStatsEntry.setStatus("mandatory")


class _FrDteLeqQueuePktThreshold_Type(Unsigned32):
    """Custom type frDteLeqQueuePktThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteLeqQueuePktThreshold_Type.__name__ = "Unsigned32"
_FrDteLeqQueuePktThreshold_Object = MibTableColumn
frDteLeqQueuePktThreshold = _FrDteLeqQueuePktThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 14, 1, 1),
    _FrDteLeqQueuePktThreshold_Type()
)
frDteLeqQueuePktThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqQueuePktThreshold.setStatus("mandatory")
_FrDteLeqPktThresholdExceeded_Type = Counter32
_FrDteLeqPktThresholdExceeded_Object = MibTableColumn
frDteLeqPktThresholdExceeded = _FrDteLeqPktThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 14, 1, 2),
    _FrDteLeqPktThresholdExceeded_Type()
)
frDteLeqPktThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqPktThresholdExceeded.setStatus("mandatory")


class _FrDteLeqQueueByteThreshold_Type(Unsigned32):
    """Custom type frDteLeqQueueByteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteLeqQueueByteThreshold_Type.__name__ = "Unsigned32"
_FrDteLeqQueueByteThreshold_Object = MibTableColumn
frDteLeqQueueByteThreshold = _FrDteLeqQueueByteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 14, 1, 3),
    _FrDteLeqQueueByteThreshold_Type()
)
frDteLeqQueueByteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqQueueByteThreshold.setStatus("mandatory")
_FrDteLeqByteThresholdExceeded_Type = Counter32
_FrDteLeqByteThresholdExceeded_Object = MibTableColumn
frDteLeqByteThresholdExceeded = _FrDteLeqByteThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 14, 1, 4),
    _FrDteLeqByteThresholdExceeded_Type()
)
frDteLeqByteThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqByteThresholdExceeded.setStatus("mandatory")


class _FrDteLeqQueueMulticastThreshold_Type(Unsigned32):
    """Custom type frDteLeqQueueMulticastThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrDteLeqQueueMulticastThreshold_Type.__name__ = "Unsigned32"
_FrDteLeqQueueMulticastThreshold_Object = MibTableColumn
frDteLeqQueueMulticastThreshold = _FrDteLeqQueueMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 14, 1, 5),
    _FrDteLeqQueueMulticastThreshold_Type()
)
frDteLeqQueueMulticastThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqQueueMulticastThreshold.setStatus("mandatory")
_FrDteLeqMulThresholdExceeded_Type = Counter32
_FrDteLeqMulThresholdExceeded_Object = MibTableColumn
frDteLeqMulThresholdExceeded = _FrDteLeqMulThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 14, 1, 6),
    _FrDteLeqMulThresholdExceeded_Type()
)
frDteLeqMulThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqMulThresholdExceeded.setStatus("mandatory")
_FrDteLeqMemThresholdExceeded_Type = Counter32
_FrDteLeqMemThresholdExceeded_Object = MibTableColumn
frDteLeqMemThresholdExceeded = _FrDteLeqMemThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 7, 14, 1, 7),
    _FrDteLeqMemThresholdExceeded_Type()
)
frDteLeqMemThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLeqMemThresholdExceeded.setStatus("mandatory")
_FrDteDlci_ObjectIdentity = ObjectIdentity
frDteDlci = _FrDteDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8)
)
_FrDteDlciRowStatusTable_Object = MibTable
frDteDlciRowStatusTable = _FrDteDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 1)
)
if mibBuilder.loadTexts:
    frDteDlciRowStatusTable.setStatus("mandatory")
_FrDteDlciRowStatusEntry_Object = MibTableRow
frDteDlciRowStatusEntry = _FrDteDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 1, 1)
)
frDteDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteDlciIndex"),
)
if mibBuilder.loadTexts:
    frDteDlciRowStatusEntry.setStatus("mandatory")
_FrDteDlciRowStatus_Type = RowStatus
_FrDteDlciRowStatus_Object = MibTableColumn
frDteDlciRowStatus = _FrDteDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 1, 1, 1),
    _FrDteDlciRowStatus_Type()
)
frDteDlciRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciRowStatus.setStatus("mandatory")
_FrDteDlciComponentName_Type = DisplayString
_FrDteDlciComponentName_Object = MibTableColumn
frDteDlciComponentName = _FrDteDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 1, 1, 2),
    _FrDteDlciComponentName_Type()
)
frDteDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciComponentName.setStatus("mandatory")
_FrDteDlciStorageType_Type = StorageType
_FrDteDlciStorageType_Object = MibTableColumn
frDteDlciStorageType = _FrDteDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 1, 1, 4),
    _FrDteDlciStorageType_Type()
)
frDteDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciStorageType.setStatus("mandatory")


class _FrDteDlciIndex_Type(Integer32):
    """Custom type frDteDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_FrDteDlciIndex_Type.__name__ = "Integer32"
_FrDteDlciIndex_Object = MibTableColumn
frDteDlciIndex = _FrDteDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 1, 1, 10),
    _FrDteDlciIndex_Type()
)
frDteDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteDlciIndex.setStatus("mandatory")
_FrDteDlciStateTable_Object = MibTable
frDteDlciStateTable = _FrDteDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 10)
)
if mibBuilder.loadTexts:
    frDteDlciStateTable.setStatus("mandatory")
_FrDteDlciStateEntry_Object = MibTableRow
frDteDlciStateEntry = _FrDteDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 10, 1)
)
frDteDlciStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteDlciIndex"),
)
if mibBuilder.loadTexts:
    frDteDlciStateEntry.setStatus("mandatory")


class _FrDteDlciAdminState_Type(Integer32):
    """Custom type frDteDlciAdminState based on Integer32"""
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


_FrDteDlciAdminState_Type.__name__ = "Integer32"
_FrDteDlciAdminState_Object = MibTableColumn
frDteDlciAdminState = _FrDteDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 10, 1, 1),
    _FrDteDlciAdminState_Type()
)
frDteDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciAdminState.setStatus("mandatory")


class _FrDteDlciOperationalState_Type(Integer32):
    """Custom type frDteDlciOperationalState based on Integer32"""
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


_FrDteDlciOperationalState_Type.__name__ = "Integer32"
_FrDteDlciOperationalState_Object = MibTableColumn
frDteDlciOperationalState = _FrDteDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 10, 1, 2),
    _FrDteDlciOperationalState_Type()
)
frDteDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciOperationalState.setStatus("mandatory")


class _FrDteDlciUsageState_Type(Integer32):
    """Custom type frDteDlciUsageState based on Integer32"""
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


_FrDteDlciUsageState_Type.__name__ = "Integer32"
_FrDteDlciUsageState_Object = MibTableColumn
frDteDlciUsageState = _FrDteDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 10, 1, 3),
    _FrDteDlciUsageState_Type()
)
frDteDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciUsageState.setStatus("mandatory")
_FrDteDlciOperTable_Object = MibTable
frDteDlciOperTable = _FrDteDlciOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11)
)
if mibBuilder.loadTexts:
    frDteDlciOperTable.setStatus("mandatory")
_FrDteDlciOperEntry_Object = MibTableRow
frDteDlciOperEntry = _FrDteDlciOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1)
)
frDteDlciOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteDlciIndex"),
)
if mibBuilder.loadTexts:
    frDteDlciOperEntry.setStatus("mandatory")


class _FrDteDlciDlciState_Type(Integer32):
    """Custom type frDteDlciDlciState based on Integer32"""
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


_FrDteDlciDlciState_Type.__name__ = "Integer32"
_FrDteDlciDlciState_Object = MibTableColumn
frDteDlciDlciState = _FrDteDlciDlciState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 4),
    _FrDteDlciDlciState_Type()
)
frDteDlciDlciState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciDlciState.setStatus("mandatory")


class _FrDteDlciLastTimeChange_Type(EnterpriseDateAndTime):
    """Custom type frDteDlciLastTimeChange based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_FrDteDlciLastTimeChange_Type.__name__ = "EnterpriseDateAndTime"
_FrDteDlciLastTimeChange_Object = MibTableColumn
frDteDlciLastTimeChange = _FrDteDlciLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 5),
    _FrDteDlciLastTimeChange_Type()
)
frDteDlciLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciLastTimeChange.setStatus("mandatory")
_FrDteDlciSentFrames_Type = Counter32
_FrDteDlciSentFrames_Object = MibTableColumn
frDteDlciSentFrames = _FrDteDlciSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 7),
    _FrDteDlciSentFrames_Type()
)
frDteDlciSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciSentFrames.setStatus("mandatory")
_FrDteDlciSentOctets_Type = Counter32
_FrDteDlciSentOctets_Object = MibTableColumn
frDteDlciSentOctets = _FrDteDlciSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 8),
    _FrDteDlciSentOctets_Type()
)
frDteDlciSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciSentOctets.setStatus("mandatory")
_FrDteDlciReceivedFrames_Type = Counter32
_FrDteDlciReceivedFrames_Object = MibTableColumn
frDteDlciReceivedFrames = _FrDteDlciReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 9),
    _FrDteDlciReceivedFrames_Type()
)
frDteDlciReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciReceivedFrames.setStatus("mandatory")
_FrDteDlciReceivedOctets_Type = Counter32
_FrDteDlciReceivedOctets_Object = MibTableColumn
frDteDlciReceivedOctets = _FrDteDlciReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 10),
    _FrDteDlciReceivedOctets_Type()
)
frDteDlciReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciReceivedOctets.setStatus("mandatory")
_FrDteDlciReceivedFECNs_Type = Counter32
_FrDteDlciReceivedFECNs_Object = MibTableColumn
frDteDlciReceivedFECNs = _FrDteDlciReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 11),
    _FrDteDlciReceivedFECNs_Type()
)
frDteDlciReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciReceivedFECNs.setStatus("mandatory")
_FrDteDlciReceivedBECNs_Type = Counter32
_FrDteDlciReceivedBECNs_Object = MibTableColumn
frDteDlciReceivedBECNs = _FrDteDlciReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 12),
    _FrDteDlciReceivedBECNs_Type()
)
frDteDlciReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciReceivedBECNs.setStatus("mandatory")
_FrDteDlciDiscardedFrames_Type = Counter32
_FrDteDlciDiscardedFrames_Object = MibTableColumn
frDteDlciDiscardedFrames = _FrDteDlciDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 13),
    _FrDteDlciDiscardedFrames_Type()
)
frDteDlciDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciDiscardedFrames.setStatus("mandatory")


class _FrDteDlciCreationType_Type(Integer32):
    """Custom type frDteDlciCreationType based on Integer32"""
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


_FrDteDlciCreationType_Type.__name__ = "Integer32"
_FrDteDlciCreationType_Object = MibTableColumn
frDteDlciCreationType = _FrDteDlciCreationType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 14),
    _FrDteDlciCreationType_Type()
)
frDteDlciCreationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciCreationType.setStatus("mandatory")


class _FrDteDlciCreationTime_Type(EnterpriseDateAndTime):
    """Custom type frDteDlciCreationTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_FrDteDlciCreationTime_Type.__name__ = "EnterpriseDateAndTime"
_FrDteDlciCreationTime_Object = MibTableColumn
frDteDlciCreationTime = _FrDteDlciCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 15),
    _FrDteDlciCreationTime_Type()
)
frDteDlciCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlciCreationTime.setStatus("mandatory")


class _FrDteDlciRateEnforcement_Type(Integer32):
    """Custom type frDteDlciRateEnforcement based on Integer32"""
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


_FrDteDlciRateEnforcement_Type.__name__ = "Integer32"
_FrDteDlciRateEnforcement_Object = MibTableColumn
frDteDlciRateEnforcement = _FrDteDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 17),
    _FrDteDlciRateEnforcement_Type()
)
frDteDlciRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDlciRateEnforcement.setStatus("mandatory")


class _FrDteDlciCommittedInformationRate_Type(Gauge32):
    """Custom type frDteDlciCommittedInformationRate based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48000000),
    )


_FrDteDlciCommittedInformationRate_Type.__name__ = "Gauge32"
_FrDteDlciCommittedInformationRate_Object = MibTableColumn
frDteDlciCommittedInformationRate = _FrDteDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 18),
    _FrDteDlciCommittedInformationRate_Type()
)
frDteDlciCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDlciCommittedInformationRate.setStatus("mandatory")


class _FrDteDlciCommittedBurst_Type(Unsigned32):
    """Custom type frDteDlciCommittedBurst based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FrDteDlciCommittedBurst_Type.__name__ = "Unsigned32"
_FrDteDlciCommittedBurst_Object = MibTableColumn
frDteDlciCommittedBurst = _FrDteDlciCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 19),
    _FrDteDlciCommittedBurst_Type()
)
frDteDlciCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDlciCommittedBurst.setStatus("mandatory")


class _FrDteDlciExcessBurst_Type(Unsigned32):
    """Custom type frDteDlciExcessBurst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FrDteDlciExcessBurst_Type.__name__ = "Unsigned32"
_FrDteDlciExcessBurst_Object = MibTableColumn
frDteDlciExcessBurst = _FrDteDlciExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 20),
    _FrDteDlciExcessBurst_Type()
)
frDteDlciExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDlciExcessBurst.setStatus("mandatory")


class _FrDteDlciExcessBurstAction_Type(Integer32):
    """Custom type frDteDlciExcessBurstAction based on Integer32"""
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


_FrDteDlciExcessBurstAction_Type.__name__ = "Integer32"
_FrDteDlciExcessBurstAction_Object = MibTableColumn
frDteDlciExcessBurstAction = _FrDteDlciExcessBurstAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 8, 11, 1, 21),
    _FrDteDlciExcessBurstAction_Type()
)
frDteDlciExcessBurstAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteDlciExcessBurstAction.setStatus("mandatory")
_FrDteVFramer_ObjectIdentity = ObjectIdentity
frDteVFramer = _FrDteVFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9)
)
_FrDteVFramerRowStatusTable_Object = MibTable
frDteVFramerRowStatusTable = _FrDteVFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 1)
)
if mibBuilder.loadTexts:
    frDteVFramerRowStatusTable.setStatus("mandatory")
_FrDteVFramerRowStatusEntry_Object = MibTableRow
frDteVFramerRowStatusEntry = _FrDteVFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 1, 1)
)
frDteVFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteVFramerIndex"),
)
if mibBuilder.loadTexts:
    frDteVFramerRowStatusEntry.setStatus("mandatory")
_FrDteVFramerRowStatus_Type = RowStatus
_FrDteVFramerRowStatus_Object = MibTableColumn
frDteVFramerRowStatus = _FrDteVFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 1, 1, 1),
    _FrDteVFramerRowStatus_Type()
)
frDteVFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteVFramerRowStatus.setStatus("mandatory")
_FrDteVFramerComponentName_Type = DisplayString
_FrDteVFramerComponentName_Object = MibTableColumn
frDteVFramerComponentName = _FrDteVFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 1, 1, 2),
    _FrDteVFramerComponentName_Type()
)
frDteVFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteVFramerComponentName.setStatus("mandatory")
_FrDteVFramerStorageType_Type = StorageType
_FrDteVFramerStorageType_Object = MibTableColumn
frDteVFramerStorageType = _FrDteVFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 1, 1, 4),
    _FrDteVFramerStorageType_Type()
)
frDteVFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteVFramerStorageType.setStatus("mandatory")
_FrDteVFramerIndex_Type = NonReplicated
_FrDteVFramerIndex_Object = MibTableColumn
frDteVFramerIndex = _FrDteVFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 1, 1, 10),
    _FrDteVFramerIndex_Type()
)
frDteVFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frDteVFramerIndex.setStatus("mandatory")
_FrDteVFramerProvTable_Object = MibTable
frDteVFramerProvTable = _FrDteVFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 10)
)
if mibBuilder.loadTexts:
    frDteVFramerProvTable.setStatus("mandatory")
_FrDteVFramerProvEntry_Object = MibTableRow
frDteVFramerProvEntry = _FrDteVFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 10, 1)
)
frDteVFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteVFramerIndex"),
)
if mibBuilder.loadTexts:
    frDteVFramerProvEntry.setStatus("mandatory")
_FrDteVFramerOtherVirtualFramer_Type = Link
_FrDteVFramerOtherVirtualFramer_Object = MibTableColumn
frDteVFramerOtherVirtualFramer = _FrDteVFramerOtherVirtualFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 10, 1, 1),
    _FrDteVFramerOtherVirtualFramer_Type()
)
frDteVFramerOtherVirtualFramer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteVFramerOtherVirtualFramer.setStatus("mandatory")
_FrDteVFramerLogicalProcessor_Type = Link
_FrDteVFramerLogicalProcessor_Object = MibTableColumn
frDteVFramerLogicalProcessor = _FrDteVFramerLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 10, 1, 2),
    _FrDteVFramerLogicalProcessor_Type()
)
frDteVFramerLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteVFramerLogicalProcessor.setStatus("mandatory")
_FrDteVFramerStateTable_Object = MibTable
frDteVFramerStateTable = _FrDteVFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 11)
)
if mibBuilder.loadTexts:
    frDteVFramerStateTable.setStatus("mandatory")
_FrDteVFramerStateEntry_Object = MibTableRow
frDteVFramerStateEntry = _FrDteVFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 11, 1)
)
frDteVFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteVFramerIndex"),
)
if mibBuilder.loadTexts:
    frDteVFramerStateEntry.setStatus("mandatory")


class _FrDteVFramerAdminState_Type(Integer32):
    """Custom type frDteVFramerAdminState based on Integer32"""
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


_FrDteVFramerAdminState_Type.__name__ = "Integer32"
_FrDteVFramerAdminState_Object = MibTableColumn
frDteVFramerAdminState = _FrDteVFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 11, 1, 1),
    _FrDteVFramerAdminState_Type()
)
frDteVFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteVFramerAdminState.setStatus("mandatory")


class _FrDteVFramerOperationalState_Type(Integer32):
    """Custom type frDteVFramerOperationalState based on Integer32"""
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


_FrDteVFramerOperationalState_Type.__name__ = "Integer32"
_FrDteVFramerOperationalState_Object = MibTableColumn
frDteVFramerOperationalState = _FrDteVFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 11, 1, 2),
    _FrDteVFramerOperationalState_Type()
)
frDteVFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteVFramerOperationalState.setStatus("mandatory")


class _FrDteVFramerUsageState_Type(Integer32):
    """Custom type frDteVFramerUsageState based on Integer32"""
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


_FrDteVFramerUsageState_Type.__name__ = "Integer32"
_FrDteVFramerUsageState_Object = MibTableColumn
frDteVFramerUsageState = _FrDteVFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 11, 1, 3),
    _FrDteVFramerUsageState_Type()
)
frDteVFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteVFramerUsageState.setStatus("mandatory")
_FrDteVFramerStatsTable_Object = MibTable
frDteVFramerStatsTable = _FrDteVFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 12)
)
if mibBuilder.loadTexts:
    frDteVFramerStatsTable.setStatus("mandatory")
_FrDteVFramerStatsEntry_Object = MibTableRow
frDteVFramerStatsEntry = _FrDteVFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 12, 1)
)
frDteVFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteVFramerIndex"),
)
if mibBuilder.loadTexts:
    frDteVFramerStatsEntry.setStatus("mandatory")
_FrDteVFramerFrmToOtherVFramer_Type = PassportCounter64
_FrDteVFramerFrmToOtherVFramer_Object = MibTableColumn
frDteVFramerFrmToOtherVFramer = _FrDteVFramerFrmToOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 12, 1, 2),
    _FrDteVFramerFrmToOtherVFramer_Type()
)
frDteVFramerFrmToOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteVFramerFrmToOtherVFramer.setStatus("mandatory")
_FrDteVFramerFrmFromOtherVFramer_Type = PassportCounter64
_FrDteVFramerFrmFromOtherVFramer_Object = MibTableColumn
frDteVFramerFrmFromOtherVFramer = _FrDteVFramerFrmFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 12, 1, 3),
    _FrDteVFramerFrmFromOtherVFramer_Type()
)
frDteVFramerFrmFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteVFramerFrmFromOtherVFramer.setStatus("mandatory")
_FrDteVFramerOctetFromOtherVFramer_Type = PassportCounter64
_FrDteVFramerOctetFromOtherVFramer_Object = MibTableColumn
frDteVFramerOctetFromOtherVFramer = _FrDteVFramerOctetFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 9, 12, 1, 5),
    _FrDteVFramerOctetFromOtherVFramer_Type()
)
frDteVFramerOctetFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteVFramerOctetFromOtherVFramer.setStatus("mandatory")
_FrDteCidDataTable_Object = MibTable
frDteCidDataTable = _FrDteCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 20)
)
if mibBuilder.loadTexts:
    frDteCidDataTable.setStatus("mandatory")
_FrDteCidDataEntry_Object = MibTableRow
frDteCidDataEntry = _FrDteCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 20, 1)
)
frDteCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
)
if mibBuilder.loadTexts:
    frDteCidDataEntry.setStatus("mandatory")


class _FrDteCustomerIdentifier_Type(Unsigned32):
    """Custom type frDteCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_FrDteCustomerIdentifier_Type.__name__ = "Unsigned32"
_FrDteCustomerIdentifier_Object = MibTableColumn
frDteCustomerIdentifier = _FrDteCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 20, 1, 1),
    _FrDteCustomerIdentifier_Type()
)
frDteCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteCustomerIdentifier.setStatus("mandatory")
_FrDteIfEntryTable_Object = MibTable
frDteIfEntryTable = _FrDteIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 21)
)
if mibBuilder.loadTexts:
    frDteIfEntryTable.setStatus("mandatory")
_FrDteIfEntryEntry_Object = MibTableRow
frDteIfEntryEntry = _FrDteIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 21, 1)
)
frDteIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
)
if mibBuilder.loadTexts:
    frDteIfEntryEntry.setStatus("mandatory")


class _FrDteIfAdminStatus_Type(Integer32):
    """Custom type frDteIfAdminStatus based on Integer32"""
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


_FrDteIfAdminStatus_Type.__name__ = "Integer32"
_FrDteIfAdminStatus_Object = MibTableColumn
frDteIfAdminStatus = _FrDteIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 21, 1, 1),
    _FrDteIfAdminStatus_Type()
)
frDteIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteIfAdminStatus.setStatus("mandatory")


class _FrDteIfIndex_Type(InterfaceIndex):
    """Custom type frDteIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrDteIfIndex_Type.__name__ = "InterfaceIndex"
_FrDteIfIndex_Object = MibTableColumn
frDteIfIndex = _FrDteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 21, 1, 2),
    _FrDteIfIndex_Type()
)
frDteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteIfIndex.setStatus("mandatory")
_FrDteProvTable_Object = MibTable
frDteProvTable = _FrDteProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 22)
)
if mibBuilder.loadTexts:
    frDteProvTable.setStatus("mandatory")
_FrDteProvEntry_Object = MibTableRow
frDteProvEntry = _FrDteProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 22, 1)
)
frDteProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
)
if mibBuilder.loadTexts:
    frDteProvEntry.setStatus("mandatory")


class _FrDteAcceptUndefinedDlci_Type(Integer32):
    """Custom type frDteAcceptUndefinedDlci based on Integer32"""
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


_FrDteAcceptUndefinedDlci_Type.__name__ = "Integer32"
_FrDteAcceptUndefinedDlci_Object = MibTableColumn
frDteAcceptUndefinedDlci = _FrDteAcceptUndefinedDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 22, 1, 1),
    _FrDteAcceptUndefinedDlci_Type()
)
frDteAcceptUndefinedDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDteAcceptUndefinedDlci.setStatus("mandatory")
_FrDteStateTable_Object = MibTable
frDteStateTable = _FrDteStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 23)
)
if mibBuilder.loadTexts:
    frDteStateTable.setStatus("mandatory")
_FrDteStateEntry_Object = MibTableRow
frDteStateEntry = _FrDteStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 23, 1)
)
frDteStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
)
if mibBuilder.loadTexts:
    frDteStateEntry.setStatus("mandatory")


class _FrDteAdminState_Type(Integer32):
    """Custom type frDteAdminState based on Integer32"""
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


_FrDteAdminState_Type.__name__ = "Integer32"
_FrDteAdminState_Object = MibTableColumn
frDteAdminState = _FrDteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 23, 1, 1),
    _FrDteAdminState_Type()
)
frDteAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteAdminState.setStatus("mandatory")


class _FrDteOperationalState_Type(Integer32):
    """Custom type frDteOperationalState based on Integer32"""
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


_FrDteOperationalState_Type.__name__ = "Integer32"
_FrDteOperationalState_Object = MibTableColumn
frDteOperationalState = _FrDteOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 23, 1, 2),
    _FrDteOperationalState_Type()
)
frDteOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteOperationalState.setStatus("mandatory")


class _FrDteUsageState_Type(Integer32):
    """Custom type frDteUsageState based on Integer32"""
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


_FrDteUsageState_Type.__name__ = "Integer32"
_FrDteUsageState_Object = MibTableColumn
frDteUsageState = _FrDteUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 23, 1, 3),
    _FrDteUsageState_Type()
)
frDteUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteUsageState.setStatus("mandatory")
_FrDteOperStatusTable_Object = MibTable
frDteOperStatusTable = _FrDteOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 24)
)
if mibBuilder.loadTexts:
    frDteOperStatusTable.setStatus("mandatory")
_FrDteOperStatusEntry_Object = MibTableRow
frDteOperStatusEntry = _FrDteOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 24, 1)
)
frDteOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
)
if mibBuilder.loadTexts:
    frDteOperStatusEntry.setStatus("mandatory")


class _FrDteSnmpOperStatus_Type(Integer32):
    """Custom type frDteSnmpOperStatus based on Integer32"""
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


_FrDteSnmpOperStatus_Type.__name__ = "Integer32"
_FrDteSnmpOperStatus_Object = MibTableColumn
frDteSnmpOperStatus = _FrDteSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 24, 1, 1),
    _FrDteSnmpOperStatus_Type()
)
frDteSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteSnmpOperStatus.setStatus("mandatory")
_FrDteOperTable_Object = MibTable
frDteOperTable = _FrDteOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 25)
)
if mibBuilder.loadTexts:
    frDteOperTable.setStatus("mandatory")
_FrDteOperEntry_Object = MibTableRow
frDteOperEntry = _FrDteOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 25, 1)
)
frDteOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
)
if mibBuilder.loadTexts:
    frDteOperEntry.setStatus("mandatory")


class _FrDteLinkOperState_Type(Integer32):
    """Custom type frDteLinkOperState based on Integer32"""
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


_FrDteLinkOperState_Type.__name__ = "Integer32"
_FrDteLinkOperState_Object = MibTableColumn
frDteLinkOperState = _FrDteLinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 25, 1, 1),
    _FrDteLinkOperState_Type()
)
frDteLinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteLinkOperState.setStatus("mandatory")
_FrDteErrTable_Object = MibTable
frDteErrTable = _FrDteErrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 26)
)
if mibBuilder.loadTexts:
    frDteErrTable.setStatus("mandatory")
_FrDteErrEntry_Object = MibTableRow
frDteErrEntry = _FrDteErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 26, 1)
)
frDteErrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
)
if mibBuilder.loadTexts:
    frDteErrEntry.setStatus("mandatory")


class _FrDteErrType_Type(Integer32):
    """Custom type frDteErrType based on Integer32"""
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


_FrDteErrType_Type.__name__ = "Integer32"
_FrDteErrType_Object = MibTableColumn
frDteErrType = _FrDteErrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 26, 1, 2),
    _FrDteErrType_Type()
)
frDteErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteErrType.setStatus("mandatory")


class _FrDteErrData_Type(HexString):
    """Custom type frDteErrData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_FrDteErrData_Type.__name__ = "HexString"
_FrDteErrData_Object = MibTableColumn
frDteErrData = _FrDteErrData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 26, 1, 3),
    _FrDteErrData_Type()
)
frDteErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteErrData.setStatus("mandatory")


class _FrDteErrTime_Type(EnterpriseDateAndTime):
    """Custom type frDteErrTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_FrDteErrTime_Type.__name__ = "EnterpriseDateAndTime"
_FrDteErrTime_Object = MibTableColumn
frDteErrTime = _FrDteErrTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 26, 1, 4),
    _FrDteErrTime_Type()
)
frDteErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteErrTime.setStatus("mandatory")
_FrDteErrDiscards_Type = Counter32
_FrDteErrDiscards_Object = MibTableColumn
frDteErrDiscards = _FrDteErrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 26, 1, 6),
    _FrDteErrDiscards_Type()
)
frDteErrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteErrDiscards.setStatus("mandatory")
_FrDteErrFaults_Type = Counter32
_FrDteErrFaults_Object = MibTableColumn
frDteErrFaults = _FrDteErrFaults_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 26, 1, 7),
    _FrDteErrFaults_Type()
)
frDteErrFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteErrFaults.setStatus("mandatory")


class _FrDteErrFaultTime_Type(EnterpriseDateAndTime):
    """Custom type frDteErrFaultTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_FrDteErrFaultTime_Type.__name__ = "EnterpriseDateAndTime"
_FrDteErrFaultTime_Object = MibTableColumn
frDteErrFaultTime = _FrDteErrFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 26, 1, 8),
    _FrDteErrFaultTime_Type()
)
frDteErrFaultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteErrFaultTime.setStatus("mandatory")
_FrDteErrStatsTable_Object = MibTable
frDteErrStatsTable = _FrDteErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27)
)
if mibBuilder.loadTexts:
    frDteErrStatsTable.setStatus("mandatory")
_FrDteErrStatsEntry_Object = MibTableRow
frDteErrStatsEntry = _FrDteErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1)
)
frDteErrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayDteMIB", "frDteIndex"),
)
if mibBuilder.loadTexts:
    frDteErrStatsEntry.setStatus("mandatory")
_FrDteXmitDiscardPvcDown_Type = Counter32
_FrDteXmitDiscardPvcDown_Object = MibTableColumn
frDteXmitDiscardPvcDown = _FrDteXmitDiscardPvcDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 1),
    _FrDteXmitDiscardPvcDown_Type()
)
frDteXmitDiscardPvcDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteXmitDiscardPvcDown.setStatus("mandatory")
_FrDteXmitDiscardLmiInactive_Type = Counter32
_FrDteXmitDiscardLmiInactive_Object = MibTableColumn
frDteXmitDiscardLmiInactive = _FrDteXmitDiscardLmiInactive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 2),
    _FrDteXmitDiscardLmiInactive_Type()
)
frDteXmitDiscardLmiInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteXmitDiscardLmiInactive.setStatus("mandatory")
_FrDteXmitDiscardFramerDown_Type = Counter32
_FrDteXmitDiscardFramerDown_Object = MibTableColumn
frDteXmitDiscardFramerDown = _FrDteXmitDiscardFramerDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 3),
    _FrDteXmitDiscardFramerDown_Type()
)
frDteXmitDiscardFramerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteXmitDiscardFramerDown.setStatus("mandatory")
_FrDteXmitDiscardPvcInactive_Type = Counter32
_FrDteXmitDiscardPvcInactive_Object = MibTableColumn
frDteXmitDiscardPvcInactive = _FrDteXmitDiscardPvcInactive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 4),
    _FrDteXmitDiscardPvcInactive_Type()
)
frDteXmitDiscardPvcInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteXmitDiscardPvcInactive.setStatus("mandatory")
_FrDteXmitDiscardCirExceeded_Type = Counter32
_FrDteXmitDiscardCirExceeded_Object = MibTableColumn
frDteXmitDiscardCirExceeded = _FrDteXmitDiscardCirExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 5),
    _FrDteXmitDiscardCirExceeded_Type()
)
frDteXmitDiscardCirExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteXmitDiscardCirExceeded.setStatus("mandatory")
_FrDteRecvDiscardPvcDown_Type = Counter32
_FrDteRecvDiscardPvcDown_Object = MibTableColumn
frDteRecvDiscardPvcDown = _FrDteRecvDiscardPvcDown_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 6),
    _FrDteRecvDiscardPvcDown_Type()
)
frDteRecvDiscardPvcDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRecvDiscardPvcDown.setStatus("mandatory")
_FrDteRecvDiscardLmiInactive_Type = Counter32
_FrDteRecvDiscardLmiInactive_Object = MibTableColumn
frDteRecvDiscardLmiInactive = _FrDteRecvDiscardLmiInactive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 7),
    _FrDteRecvDiscardLmiInactive_Type()
)
frDteRecvDiscardLmiInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRecvDiscardLmiInactive.setStatus("mandatory")
_FrDteRecvDiscardPvcInactive_Type = Counter32
_FrDteRecvDiscardPvcInactive_Object = MibTableColumn
frDteRecvDiscardPvcInactive = _FrDteRecvDiscardPvcInactive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 8),
    _FrDteRecvDiscardPvcInactive_Type()
)
frDteRecvDiscardPvcInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteRecvDiscardPvcInactive.setStatus("mandatory")
_FrDteBadFc_Type = Counter32
_FrDteBadFc_Object = MibTableColumn
frDteBadFc = _FrDteBadFc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 9),
    _FrDteBadFc_Type()
)
frDteBadFc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteBadFc.setStatus("mandatory")
_FrDteUlpUnknownProtocol_Type = Counter32
_FrDteUlpUnknownProtocol_Object = MibTableColumn
frDteUlpUnknownProtocol = _FrDteUlpUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 10),
    _FrDteUlpUnknownProtocol_Type()
)
frDteUlpUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteUlpUnknownProtocol.setStatus("mandatory")
_FrDteDefragSequenceErrors_Type = Counter32
_FrDteDefragSequenceErrors_Object = MibTableColumn
frDteDefragSequenceErrors = _FrDteDefragSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 11),
    _FrDteDefragSequenceErrors_Type()
)
frDteDefragSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDefragSequenceErrors.setStatus("mandatory")
_FrDteReceiveShort_Type = Counter32
_FrDteReceiveShort_Object = MibTableColumn
frDteReceiveShort = _FrDteReceiveShort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 12),
    _FrDteReceiveShort_Type()
)
frDteReceiveShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteReceiveShort.setStatus("mandatory")
_FrDteIllegalDlci_Type = Counter32
_FrDteIllegalDlci_Object = MibTableColumn
frDteIllegalDlci = _FrDteIllegalDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 13),
    _FrDteIllegalDlci_Type()
)
frDteIllegalDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteIllegalDlci.setStatus("mandatory")
_FrDteDlcmiProtoErr_Type = Counter32
_FrDteDlcmiProtoErr_Object = MibTableColumn
frDteDlcmiProtoErr = _FrDteDlcmiProtoErr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 14),
    _FrDteDlcmiProtoErr_Type()
)
frDteDlcmiProtoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlcmiProtoErr.setStatus("mandatory")
_FrDteDlcmiUnknownIe_Type = Counter32
_FrDteDlcmiUnknownIe_Object = MibTableColumn
frDteDlcmiUnknownIe = _FrDteDlcmiUnknownIe_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 15),
    _FrDteDlcmiUnknownIe_Type()
)
frDteDlcmiUnknownIe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlcmiUnknownIe.setStatus("mandatory")
_FrDteDlcmiSequenceErr_Type = Counter32
_FrDteDlcmiSequenceErr_Object = MibTableColumn
frDteDlcmiSequenceErr = _FrDteDlcmiSequenceErr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 16),
    _FrDteDlcmiSequenceErr_Type()
)
frDteDlcmiSequenceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlcmiSequenceErr.setStatus("mandatory")
_FrDteDlcmiUnknownRpt_Type = Counter32
_FrDteDlcmiUnknownRpt_Object = MibTableColumn
frDteDlcmiUnknownRpt = _FrDteDlcmiUnknownRpt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 101, 27, 1, 17),
    _FrDteDlcmiUnknownRpt_Type()
)
frDteDlcmiUnknownRpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDteDlcmiUnknownRpt.setStatus("mandatory")
_FrameRelayDteMIB_ObjectIdentity = ObjectIdentity
frameRelayDteMIB = _FrameRelayDteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 32)
)
_FrameRelayDteGroup_ObjectIdentity = ObjectIdentity
frameRelayDteGroup = _FrameRelayDteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 32, 1)
)
_FrameRelayDteGroupBE_ObjectIdentity = ObjectIdentity
frameRelayDteGroupBE = _FrameRelayDteGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 32, 1, 5)
)
_FrameRelayDteGroupBE00_ObjectIdentity = ObjectIdentity
frameRelayDteGroupBE00 = _FrameRelayDteGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 32, 1, 5, 1)
)
_FrameRelayDteGroupBE00A_ObjectIdentity = ObjectIdentity
frameRelayDteGroupBE00A = _FrameRelayDteGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 32, 1, 5, 1, 2)
)
_FrameRelayDteCapabilities_ObjectIdentity = ObjectIdentity
frameRelayDteCapabilities = _FrameRelayDteCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 32, 3)
)
_FrameRelayDteCapabilitiesBE_ObjectIdentity = ObjectIdentity
frameRelayDteCapabilitiesBE = _FrameRelayDteCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 32, 3, 5)
)
_FrameRelayDteCapabilitiesBE00_ObjectIdentity = ObjectIdentity
frameRelayDteCapabilitiesBE00 = _FrameRelayDteCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 32, 3, 5, 1)
)
_FrameRelayDteCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
frameRelayDteCapabilitiesBE00A = _FrameRelayDteCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 32, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrameRelayDteMIB",
    **{"frDte": frDte,
       "frDteRowStatusTable": frDteRowStatusTable,
       "frDteRowStatusEntry": frDteRowStatusEntry,
       "frDteRowStatus": frDteRowStatus,
       "frDteComponentName": frDteComponentName,
       "frDteStorageType": frDteStorageType,
       "frDteIndex": frDteIndex,
       "frDteFramer": frDteFramer,
       "frDteFramerRowStatusTable": frDteFramerRowStatusTable,
       "frDteFramerRowStatusEntry": frDteFramerRowStatusEntry,
       "frDteFramerRowStatus": frDteFramerRowStatus,
       "frDteFramerComponentName": frDteFramerComponentName,
       "frDteFramerStorageType": frDteFramerStorageType,
       "frDteFramerIndex": frDteFramerIndex,
       "frDteFramerProvTable": frDteFramerProvTable,
       "frDteFramerProvEntry": frDteFramerProvEntry,
       "frDteFramerInterfaceName": frDteFramerInterfaceName,
       "frDteFramerStateTable": frDteFramerStateTable,
       "frDteFramerStateEntry": frDteFramerStateEntry,
       "frDteFramerAdminState": frDteFramerAdminState,
       "frDteFramerOperationalState": frDteFramerOperationalState,
       "frDteFramerUsageState": frDteFramerUsageState,
       "frDteFramerStatsTable": frDteFramerStatsTable,
       "frDteFramerStatsEntry": frDteFramerStatsEntry,
       "frDteFramerFrmToIf": frDteFramerFrmToIf,
       "frDteFramerFrmFromIf": frDteFramerFrmFromIf,
       "frDteFramerAborts": frDteFramerAborts,
       "frDteFramerCrcErrors": frDteFramerCrcErrors,
       "frDteFramerLrcErrors": frDteFramerLrcErrors,
       "frDteFramerNonOctetErrors": frDteFramerNonOctetErrors,
       "frDteFramerOverruns": frDteFramerOverruns,
       "frDteFramerUnderruns": frDteFramerUnderruns,
       "frDteFramerLargeFrmErrors": frDteFramerLargeFrmErrors,
       "frDteFramerUtilTable": frDteFramerUtilTable,
       "frDteFramerUtilEntry": frDteFramerUtilEntry,
       "frDteFramerNormPrioLinkUtilToIf": frDteFramerNormPrioLinkUtilToIf,
       "frDteFramerNormPrioLinkUtilFromIf": frDteFramerNormPrioLinkUtilFromIf,
       "frDteLmi": frDteLmi,
       "frDteLmiRowStatusTable": frDteLmiRowStatusTable,
       "frDteLmiRowStatusEntry": frDteLmiRowStatusEntry,
       "frDteLmiRowStatus": frDteLmiRowStatus,
       "frDteLmiComponentName": frDteLmiComponentName,
       "frDteLmiStorageType": frDteLmiStorageType,
       "frDteLmiIndex": frDteLmiIndex,
       "frDteLmiProvTable": frDteLmiProvTable,
       "frDteLmiProvEntry": frDteLmiProvEntry,
       "frDteLmiProcedures": frDteLmiProcedures,
       "frDteLmiPollingInterval": frDteLmiPollingInterval,
       "frDteLmiFullEnquiryInterval": frDteLmiFullEnquiryInterval,
       "frDteLmiErrorThreshold": frDteLmiErrorThreshold,
       "frDteLmiMonitoredEvents": frDteLmiMonitoredEvents,
       "frDteLmiOperTable": frDteLmiOperTable,
       "frDteLmiOperEntry": frDteLmiOperEntry,
       "frDteLmiLmiStatus": frDteLmiLmiStatus,
       "frDteRg": frDteRg,
       "frDteRgRowStatusTable": frDteRgRowStatusTable,
       "frDteRgRowStatusEntry": frDteRgRowStatusEntry,
       "frDteRgRowStatus": frDteRgRowStatus,
       "frDteRgComponentName": frDteRgComponentName,
       "frDteRgStorageType": frDteRgStorageType,
       "frDteRgIndex": frDteRgIndex,
       "frDteRgIfEntryTable": frDteRgIfEntryTable,
       "frDteRgIfEntryEntry": frDteRgIfEntryEntry,
       "frDteRgIfAdminStatus": frDteRgIfAdminStatus,
       "frDteRgIfIndex": frDteRgIfIndex,
       "frDteRgProvTable": frDteRgProvTable,
       "frDteRgProvEntry": frDteRgProvEntry,
       "frDteRgMaxTransmissionUnit": frDteRgMaxTransmissionUnit,
       "frDteRgMpTable": frDteRgMpTable,
       "frDteRgMpEntry": frDteRgMpEntry,
       "frDteRgLinkToProtocolPort": frDteRgLinkToProtocolPort,
       "frDteRgStateTable": frDteRgStateTable,
       "frDteRgStateEntry": frDteRgStateEntry,
       "frDteRgAdminState": frDteRgAdminState,
       "frDteRgOperationalState": frDteRgOperationalState,
       "frDteRgUsageState": frDteRgUsageState,
       "frDteRgOperStatusTable": frDteRgOperStatusTable,
       "frDteRgOperStatusEntry": frDteRgOperStatusEntry,
       "frDteRgSnmpOperStatus": frDteRgSnmpOperStatus,
       "frDteRgBfr": frDteRgBfr,
       "frDteRgBfrRowStatusTable": frDteRgBfrRowStatusTable,
       "frDteRgBfrRowStatusEntry": frDteRgBfrRowStatusEntry,
       "frDteRgBfrRowStatus": frDteRgBfrRowStatus,
       "frDteRgBfrComponentName": frDteRgBfrComponentName,
       "frDteRgBfrStorageType": frDteRgBfrStorageType,
       "frDteRgBfrIndex": frDteRgBfrIndex,
       "frDteRgBfrProvTable": frDteRgBfrProvTable,
       "frDteRgBfrProvEntry": frDteRgBfrProvEntry,
       "frDteRgBfrMacType": frDteRgBfrMacType,
       "frDteRgBfrBfrIndex": frDteRgBfrBfrIndex,
       "frDteRgBfrOprTable": frDteRgBfrOprTable,
       "frDteRgBfrOprEntry": frDteRgBfrOprEntry,
       "frDteRgBfrMacAddr": frDteRgBfrMacAddr,
       "frDteRgLtDlciTable": frDteRgLtDlciTable,
       "frDteRgLtDlciEntry": frDteRgLtDlciEntry,
       "frDteRgLtDlciValue": frDteRgLtDlciValue,
       "frDteRgLtDlciRowStatus": frDteRgLtDlciRowStatus,
       "frDteDynDlciDefs": frDteDynDlciDefs,
       "frDteDynDlciDefsRowStatusTable": frDteDynDlciDefsRowStatusTable,
       "frDteDynDlciDefsRowStatusEntry": frDteDynDlciDefsRowStatusEntry,
       "frDteDynDlciDefsRowStatus": frDteDynDlciDefsRowStatus,
       "frDteDynDlciDefsComponentName": frDteDynDlciDefsComponentName,
       "frDteDynDlciDefsStorageType": frDteDynDlciDefsStorageType,
       "frDteDynDlciDefsIndex": frDteDynDlciDefsIndex,
       "frDteDynDlciDefsProvTable": frDteDynDlciDefsProvTable,
       "frDteDynDlciDefsProvEntry": frDteDynDlciDefsProvEntry,
       "frDteDynDlciDefsStdRowStatus": frDteDynDlciDefsStdRowStatus,
       "frDteDynDlciDefsRateEnforcement": frDteDynDlciDefsRateEnforcement,
       "frDteDynDlciDefsCommittedInformationRate": frDteDynDlciDefsCommittedInformationRate,
       "frDteDynDlciDefsCommittedBurst": frDteDynDlciDefsCommittedBurst,
       "frDteDynDlciDefsExcessBurst": frDteDynDlciDefsExcessBurst,
       "frDteDynDlciDefsExcessBurstAction": frDteDynDlciDefsExcessBurstAction,
       "frDteDynDlciDefsIpCos": frDteDynDlciDefsIpCos,
       "frDteStDlci": frDteStDlci,
       "frDteStDlciRowStatusTable": frDteStDlciRowStatusTable,
       "frDteStDlciRowStatusEntry": frDteStDlciRowStatusEntry,
       "frDteStDlciRowStatus": frDteStDlciRowStatus,
       "frDteStDlciComponentName": frDteStDlciComponentName,
       "frDteStDlciStorageType": frDteStDlciStorageType,
       "frDteStDlciIndex": frDteStDlciIndex,
       "frDteStDlciHq": frDteStDlciHq,
       "frDteStDlciHqRowStatusTable": frDteStDlciHqRowStatusTable,
       "frDteStDlciHqRowStatusEntry": frDteStDlciHqRowStatusEntry,
       "frDteStDlciHqRowStatus": frDteStDlciHqRowStatus,
       "frDteStDlciHqComponentName": frDteStDlciHqComponentName,
       "frDteStDlciHqStorageType": frDteStDlciHqStorageType,
       "frDteStDlciHqIndex": frDteStDlciHqIndex,
       "frDteStDlciHqProvTable": frDteStDlciHqProvTable,
       "frDteStDlciHqProvEntry": frDteStDlciHqProvEntry,
       "frDteStDlciHqMaxPackets": frDteStDlciHqMaxPackets,
       "frDteStDlciHqMaxMsecData": frDteStDlciHqMaxMsecData,
       "frDteStDlciHqMaxPercentMulticast": frDteStDlciHqMaxPercentMulticast,
       "frDteStDlciHqTimeToLive": frDteStDlciHqTimeToLive,
       "frDteStDlciHqStatsTable": frDteStDlciHqStatsTable,
       "frDteStDlciHqStatsEntry": frDteStDlciHqStatsEntry,
       "frDteStDlciHqTimedOutPkt": frDteStDlciHqTimedOutPkt,
       "frDteStDlciHqQueuePurgeDiscards": frDteStDlciHqQueuePurgeDiscards,
       "frDteStDlciHqTStatsTable": frDteStDlciHqTStatsTable,
       "frDteStDlciHqTStatsEntry": frDteStDlciHqTStatsEntry,
       "frDteStDlciHqTotalPktHandled": frDteStDlciHqTotalPktHandled,
       "frDteStDlciHqTotalPktForwarded": frDteStDlciHqTotalPktForwarded,
       "frDteStDlciHqTotalPktQueued": frDteStDlciHqTotalPktQueued,
       "frDteStDlciHqTotalMulticastPkt": frDteStDlciHqTotalMulticastPkt,
       "frDteStDlciHqTotalPktDiscards": frDteStDlciHqTotalPktDiscards,
       "frDteStDlciHqCStatsTable": frDteStDlciHqCStatsTable,
       "frDteStDlciHqCStatsEntry": frDteStDlciHqCStatsEntry,
       "frDteStDlciHqCurrentPktQueued": frDteStDlciHqCurrentPktQueued,
       "frDteStDlciHqCurrentBytesQueued": frDteStDlciHqCurrentBytesQueued,
       "frDteStDlciHqCurrentMulticastQueued": frDteStDlciHqCurrentMulticastQueued,
       "frDteStDlciHqThrStatsTable": frDteStDlciHqThrStatsTable,
       "frDteStDlciHqThrStatsEntry": frDteStDlciHqThrStatsEntry,
       "frDteStDlciHqQueuePktThreshold": frDteStDlciHqQueuePktThreshold,
       "frDteStDlciHqPktThresholdExceeded": frDteStDlciHqPktThresholdExceeded,
       "frDteStDlciHqQueueByteThreshold": frDteStDlciHqQueueByteThreshold,
       "frDteStDlciHqByteThresholdExceeded": frDteStDlciHqByteThresholdExceeded,
       "frDteStDlciHqQueueMulticastThreshold": frDteStDlciHqQueueMulticastThreshold,
       "frDteStDlciHqMulThresholdExceeded": frDteStDlciHqMulThresholdExceeded,
       "frDteStDlciHqMemThresholdExceeded": frDteStDlciHqMemThresholdExceeded,
       "frDteStDlciProvTable": frDteStDlciProvTable,
       "frDteStDlciProvEntry": frDteStDlciProvEntry,
       "frDteStDlciStdRowStatus": frDteStDlciStdRowStatus,
       "frDteStDlciRateEnforcement": frDteStDlciRateEnforcement,
       "frDteStDlciCommittedInformationRate": frDteStDlciCommittedInformationRate,
       "frDteStDlciCommittedBurst": frDteStDlciCommittedBurst,
       "frDteStDlciExcessBurst": frDteStDlciExcessBurst,
       "frDteStDlciExcessBurstAction": frDteStDlciExcessBurstAction,
       "frDteStDlciIpCos": frDteStDlciIpCos,
       "frDteStDlciRgLinkTable": frDteStDlciRgLinkTable,
       "frDteStDlciRgLinkEntry": frDteStDlciRgLinkEntry,
       "frDteStDlciLinkToRemoteGroup": frDteStDlciLinkToRemoteGroup,
       "frDteLeq": frDteLeq,
       "frDteLeqRowStatusTable": frDteLeqRowStatusTable,
       "frDteLeqRowStatusEntry": frDteLeqRowStatusEntry,
       "frDteLeqRowStatus": frDteLeqRowStatus,
       "frDteLeqComponentName": frDteLeqComponentName,
       "frDteLeqStorageType": frDteLeqStorageType,
       "frDteLeqIndex": frDteLeqIndex,
       "frDteLeqProvTable": frDteLeqProvTable,
       "frDteLeqProvEntry": frDteLeqProvEntry,
       "frDteLeqMaxPackets": frDteLeqMaxPackets,
       "frDteLeqMaxMsecData": frDteLeqMaxMsecData,
       "frDteLeqMaxPercentMulticast": frDteLeqMaxPercentMulticast,
       "frDteLeqTimeToLive": frDteLeqTimeToLive,
       "frDteLeqStatsTable": frDteLeqStatsTable,
       "frDteLeqStatsEntry": frDteLeqStatsEntry,
       "frDteLeqTimedOutPkt": frDteLeqTimedOutPkt,
       "frDteLeqHardwareForcedPkt": frDteLeqHardwareForcedPkt,
       "frDteLeqForcedPktDiscards": frDteLeqForcedPktDiscards,
       "frDteLeqQueuePurgeDiscards": frDteLeqQueuePurgeDiscards,
       "frDteLeqTStatsTable": frDteLeqTStatsTable,
       "frDteLeqTStatsEntry": frDteLeqTStatsEntry,
       "frDteLeqTotalPktHandled": frDteLeqTotalPktHandled,
       "frDteLeqTotalPktForwarded": frDteLeqTotalPktForwarded,
       "frDteLeqTotalPktQueued": frDteLeqTotalPktQueued,
       "frDteLeqTotalMulticastPkt": frDteLeqTotalMulticastPkt,
       "frDteLeqTotalPktDiscards": frDteLeqTotalPktDiscards,
       "frDteLeqCStatsTable": frDteLeqCStatsTable,
       "frDteLeqCStatsEntry": frDteLeqCStatsEntry,
       "frDteLeqCurrentPktQueued": frDteLeqCurrentPktQueued,
       "frDteLeqCurrentBytesQueued": frDteLeqCurrentBytesQueued,
       "frDteLeqCurrentMulticastQueued": frDteLeqCurrentMulticastQueued,
       "frDteLeqThrStatsTable": frDteLeqThrStatsTable,
       "frDteLeqThrStatsEntry": frDteLeqThrStatsEntry,
       "frDteLeqQueuePktThreshold": frDteLeqQueuePktThreshold,
       "frDteLeqPktThresholdExceeded": frDteLeqPktThresholdExceeded,
       "frDteLeqQueueByteThreshold": frDteLeqQueueByteThreshold,
       "frDteLeqByteThresholdExceeded": frDteLeqByteThresholdExceeded,
       "frDteLeqQueueMulticastThreshold": frDteLeqQueueMulticastThreshold,
       "frDteLeqMulThresholdExceeded": frDteLeqMulThresholdExceeded,
       "frDteLeqMemThresholdExceeded": frDteLeqMemThresholdExceeded,
       "frDteDlci": frDteDlci,
       "frDteDlciRowStatusTable": frDteDlciRowStatusTable,
       "frDteDlciRowStatusEntry": frDteDlciRowStatusEntry,
       "frDteDlciRowStatus": frDteDlciRowStatus,
       "frDteDlciComponentName": frDteDlciComponentName,
       "frDteDlciStorageType": frDteDlciStorageType,
       "frDteDlciIndex": frDteDlciIndex,
       "frDteDlciStateTable": frDteDlciStateTable,
       "frDteDlciStateEntry": frDteDlciStateEntry,
       "frDteDlciAdminState": frDteDlciAdminState,
       "frDteDlciOperationalState": frDteDlciOperationalState,
       "frDteDlciUsageState": frDteDlciUsageState,
       "frDteDlciOperTable": frDteDlciOperTable,
       "frDteDlciOperEntry": frDteDlciOperEntry,
       "frDteDlciDlciState": frDteDlciDlciState,
       "frDteDlciLastTimeChange": frDteDlciLastTimeChange,
       "frDteDlciSentFrames": frDteDlciSentFrames,
       "frDteDlciSentOctets": frDteDlciSentOctets,
       "frDteDlciReceivedFrames": frDteDlciReceivedFrames,
       "frDteDlciReceivedOctets": frDteDlciReceivedOctets,
       "frDteDlciReceivedFECNs": frDteDlciReceivedFECNs,
       "frDteDlciReceivedBECNs": frDteDlciReceivedBECNs,
       "frDteDlciDiscardedFrames": frDteDlciDiscardedFrames,
       "frDteDlciCreationType": frDteDlciCreationType,
       "frDteDlciCreationTime": frDteDlciCreationTime,
       "frDteDlciRateEnforcement": frDteDlciRateEnforcement,
       "frDteDlciCommittedInformationRate": frDteDlciCommittedInformationRate,
       "frDteDlciCommittedBurst": frDteDlciCommittedBurst,
       "frDteDlciExcessBurst": frDteDlciExcessBurst,
       "frDteDlciExcessBurstAction": frDteDlciExcessBurstAction,
       "frDteVFramer": frDteVFramer,
       "frDteVFramerRowStatusTable": frDteVFramerRowStatusTable,
       "frDteVFramerRowStatusEntry": frDteVFramerRowStatusEntry,
       "frDteVFramerRowStatus": frDteVFramerRowStatus,
       "frDteVFramerComponentName": frDteVFramerComponentName,
       "frDteVFramerStorageType": frDteVFramerStorageType,
       "frDteVFramerIndex": frDteVFramerIndex,
       "frDteVFramerProvTable": frDteVFramerProvTable,
       "frDteVFramerProvEntry": frDteVFramerProvEntry,
       "frDteVFramerOtherVirtualFramer": frDteVFramerOtherVirtualFramer,
       "frDteVFramerLogicalProcessor": frDteVFramerLogicalProcessor,
       "frDteVFramerStateTable": frDteVFramerStateTable,
       "frDteVFramerStateEntry": frDteVFramerStateEntry,
       "frDteVFramerAdminState": frDteVFramerAdminState,
       "frDteVFramerOperationalState": frDteVFramerOperationalState,
       "frDteVFramerUsageState": frDteVFramerUsageState,
       "frDteVFramerStatsTable": frDteVFramerStatsTable,
       "frDteVFramerStatsEntry": frDteVFramerStatsEntry,
       "frDteVFramerFrmToOtherVFramer": frDteVFramerFrmToOtherVFramer,
       "frDteVFramerFrmFromOtherVFramer": frDteVFramerFrmFromOtherVFramer,
       "frDteVFramerOctetFromOtherVFramer": frDteVFramerOctetFromOtherVFramer,
       "frDteCidDataTable": frDteCidDataTable,
       "frDteCidDataEntry": frDteCidDataEntry,
       "frDteCustomerIdentifier": frDteCustomerIdentifier,
       "frDteIfEntryTable": frDteIfEntryTable,
       "frDteIfEntryEntry": frDteIfEntryEntry,
       "frDteIfAdminStatus": frDteIfAdminStatus,
       "frDteIfIndex": frDteIfIndex,
       "frDteProvTable": frDteProvTable,
       "frDteProvEntry": frDteProvEntry,
       "frDteAcceptUndefinedDlci": frDteAcceptUndefinedDlci,
       "frDteStateTable": frDteStateTable,
       "frDteStateEntry": frDteStateEntry,
       "frDteAdminState": frDteAdminState,
       "frDteOperationalState": frDteOperationalState,
       "frDteUsageState": frDteUsageState,
       "frDteOperStatusTable": frDteOperStatusTable,
       "frDteOperStatusEntry": frDteOperStatusEntry,
       "frDteSnmpOperStatus": frDteSnmpOperStatus,
       "frDteOperTable": frDteOperTable,
       "frDteOperEntry": frDteOperEntry,
       "frDteLinkOperState": frDteLinkOperState,
       "frDteErrTable": frDteErrTable,
       "frDteErrEntry": frDteErrEntry,
       "frDteErrType": frDteErrType,
       "frDteErrData": frDteErrData,
       "frDteErrTime": frDteErrTime,
       "frDteErrDiscards": frDteErrDiscards,
       "frDteErrFaults": frDteErrFaults,
       "frDteErrFaultTime": frDteErrFaultTime,
       "frDteErrStatsTable": frDteErrStatsTable,
       "frDteErrStatsEntry": frDteErrStatsEntry,
       "frDteXmitDiscardPvcDown": frDteXmitDiscardPvcDown,
       "frDteXmitDiscardLmiInactive": frDteXmitDiscardLmiInactive,
       "frDteXmitDiscardFramerDown": frDteXmitDiscardFramerDown,
       "frDteXmitDiscardPvcInactive": frDteXmitDiscardPvcInactive,
       "frDteXmitDiscardCirExceeded": frDteXmitDiscardCirExceeded,
       "frDteRecvDiscardPvcDown": frDteRecvDiscardPvcDown,
       "frDteRecvDiscardLmiInactive": frDteRecvDiscardLmiInactive,
       "frDteRecvDiscardPvcInactive": frDteRecvDiscardPvcInactive,
       "frDteBadFc": frDteBadFc,
       "frDteUlpUnknownProtocol": frDteUlpUnknownProtocol,
       "frDteDefragSequenceErrors": frDteDefragSequenceErrors,
       "frDteReceiveShort": frDteReceiveShort,
       "frDteIllegalDlci": frDteIllegalDlci,
       "frDteDlcmiProtoErr": frDteDlcmiProtoErr,
       "frDteDlcmiUnknownIe": frDteDlcmiUnknownIe,
       "frDteDlcmiSequenceErr": frDteDlcmiSequenceErr,
       "frDteDlcmiUnknownRpt": frDteDlcmiUnknownRpt,
       "frameRelayDteMIB": frameRelayDteMIB,
       "frameRelayDteGroup": frameRelayDteGroup,
       "frameRelayDteGroupBE": frameRelayDteGroupBE,
       "frameRelayDteGroupBE00": frameRelayDteGroupBE00,
       "frameRelayDteGroupBE00A": frameRelayDteGroupBE00A,
       "frameRelayDteCapabilities": frameRelayDteCapabilities,
       "frameRelayDteCapabilitiesBE": frameRelayDteCapabilitiesBE,
       "frameRelayDteCapabilitiesBE00": frameRelayDteCapabilitiesBE00,
       "frameRelayDteCapabilitiesBE00A": frameRelayDteCapabilitiesBE00A}
)
