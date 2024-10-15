# SNMP MIB module (Nortel-Magellan-Passport-FrameRelayAtmMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrameRelayAtmMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:44 2024
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
 RowPointer,
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
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 HexString,
 IntegerSequence,
 Link,
 NonReplicated,
 Unsigned64) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "HexString",
    "IntegerSequence",
    "Link",
    "NonReplicated",
    "Unsigned64")

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

_FrAtm_ObjectIdentity = ObjectIdentity
frAtm = _FrAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72)
)
_FrAtmRowStatusTable_Object = MibTable
frAtmRowStatusTable = _FrAtmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 1)
)
if mibBuilder.loadTexts:
    frAtmRowStatusTable.setStatus("mandatory")
_FrAtmRowStatusEntry_Object = MibTableRow
frAtmRowStatusEntry = _FrAtmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 1, 1)
)
frAtmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
)
if mibBuilder.loadTexts:
    frAtmRowStatusEntry.setStatus("mandatory")
_FrAtmRowStatus_Type = RowStatus
_FrAtmRowStatus_Object = MibTableColumn
frAtmRowStatus = _FrAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 1, 1, 1),
    _FrAtmRowStatus_Type()
)
frAtmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmRowStatus.setStatus("mandatory")
_FrAtmComponentName_Type = DisplayString
_FrAtmComponentName_Object = MibTableColumn
frAtmComponentName = _FrAtmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 1, 1, 2),
    _FrAtmComponentName_Type()
)
frAtmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmComponentName.setStatus("mandatory")
_FrAtmStorageType_Type = StorageType
_FrAtmStorageType_Object = MibTableColumn
frAtmStorageType = _FrAtmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 1, 1, 4),
    _FrAtmStorageType_Type()
)
frAtmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmStorageType.setStatus("mandatory")


class _FrAtmIndex_Type(Integer32):
    """Custom type frAtmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrAtmIndex_Type.__name__ = "Integer32"
_FrAtmIndex_Object = MibTableColumn
frAtmIndex = _FrAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 1, 1, 10),
    _FrAtmIndex_Type()
)
frAtmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmIndex.setStatus("mandatory")
_FrAtmFramer_ObjectIdentity = ObjectIdentity
frAtmFramer = _FrAtmFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2)
)
_FrAtmFramerRowStatusTable_Object = MibTable
frAtmFramerRowStatusTable = _FrAtmFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 1)
)
if mibBuilder.loadTexts:
    frAtmFramerRowStatusTable.setStatus("mandatory")
_FrAtmFramerRowStatusEntry_Object = MibTableRow
frAtmFramerRowStatusEntry = _FrAtmFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 1, 1)
)
frAtmFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmFramerRowStatusEntry.setStatus("mandatory")
_FrAtmFramerRowStatus_Type = RowStatus
_FrAtmFramerRowStatus_Object = MibTableColumn
frAtmFramerRowStatus = _FrAtmFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 1, 1, 1),
    _FrAtmFramerRowStatus_Type()
)
frAtmFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmFramerRowStatus.setStatus("mandatory")
_FrAtmFramerComponentName_Type = DisplayString
_FrAtmFramerComponentName_Object = MibTableColumn
frAtmFramerComponentName = _FrAtmFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 1, 1, 2),
    _FrAtmFramerComponentName_Type()
)
frAtmFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerComponentName.setStatus("mandatory")
_FrAtmFramerStorageType_Type = StorageType
_FrAtmFramerStorageType_Object = MibTableColumn
frAtmFramerStorageType = _FrAtmFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 1, 1, 4),
    _FrAtmFramerStorageType_Type()
)
frAtmFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerStorageType.setStatus("mandatory")
_FrAtmFramerIndex_Type = NonReplicated
_FrAtmFramerIndex_Object = MibTableColumn
frAtmFramerIndex = _FrAtmFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 1, 1, 10),
    _FrAtmFramerIndex_Type()
)
frAtmFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmFramerIndex.setStatus("mandatory")
_FrAtmFramerProvTable_Object = MibTable
frAtmFramerProvTable = _FrAtmFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 10)
)
if mibBuilder.loadTexts:
    frAtmFramerProvTable.setStatus("mandatory")
_FrAtmFramerProvEntry_Object = MibTableRow
frAtmFramerProvEntry = _FrAtmFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 10, 1)
)
frAtmFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmFramerProvEntry.setStatus("mandatory")
_FrAtmFramerInterfaceName_Type = Link
_FrAtmFramerInterfaceName_Object = MibTableColumn
frAtmFramerInterfaceName = _FrAtmFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 10, 1, 1),
    _FrAtmFramerInterfaceName_Type()
)
frAtmFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmFramerInterfaceName.setStatus("mandatory")
_FrAtmFramerLinkTable_Object = MibTable
frAtmFramerLinkTable = _FrAtmFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 11)
)
if mibBuilder.loadTexts:
    frAtmFramerLinkTable.setStatus("mandatory")
_FrAtmFramerLinkEntry_Object = MibTableRow
frAtmFramerLinkEntry = _FrAtmFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 11, 1)
)
frAtmFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmFramerLinkEntry.setStatus("mandatory")


class _FrAtmFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type frAtmFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FrAtmFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_FrAtmFramerFlagsBetweenFrames_Object = MibTableColumn
frAtmFramerFlagsBetweenFrames = _FrAtmFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 11, 1, 4),
    _FrAtmFramerFlagsBetweenFrames_Type()
)
frAtmFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmFramerFlagsBetweenFrames.setStatus("mandatory")
_FrAtmFramerStateTable_Object = MibTable
frAtmFramerStateTable = _FrAtmFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 12)
)
if mibBuilder.loadTexts:
    frAtmFramerStateTable.setStatus("mandatory")
_FrAtmFramerStateEntry_Object = MibTableRow
frAtmFramerStateEntry = _FrAtmFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 12, 1)
)
frAtmFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmFramerStateEntry.setStatus("mandatory")


class _FrAtmFramerAdminState_Type(Integer32):
    """Custom type frAtmFramerAdminState based on Integer32"""
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


_FrAtmFramerAdminState_Type.__name__ = "Integer32"
_FrAtmFramerAdminState_Object = MibTableColumn
frAtmFramerAdminState = _FrAtmFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 12, 1, 1),
    _FrAtmFramerAdminState_Type()
)
frAtmFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerAdminState.setStatus("mandatory")


class _FrAtmFramerOperationalState_Type(Integer32):
    """Custom type frAtmFramerOperationalState based on Integer32"""
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


_FrAtmFramerOperationalState_Type.__name__ = "Integer32"
_FrAtmFramerOperationalState_Object = MibTableColumn
frAtmFramerOperationalState = _FrAtmFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 12, 1, 2),
    _FrAtmFramerOperationalState_Type()
)
frAtmFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerOperationalState.setStatus("mandatory")


class _FrAtmFramerUsageState_Type(Integer32):
    """Custom type frAtmFramerUsageState based on Integer32"""
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


_FrAtmFramerUsageState_Type.__name__ = "Integer32"
_FrAtmFramerUsageState_Object = MibTableColumn
frAtmFramerUsageState = _FrAtmFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 12, 1, 3),
    _FrAtmFramerUsageState_Type()
)
frAtmFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerUsageState.setStatus("mandatory")
_FrAtmFramerStatsTable_Object = MibTable
frAtmFramerStatsTable = _FrAtmFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13)
)
if mibBuilder.loadTexts:
    frAtmFramerStatsTable.setStatus("mandatory")
_FrAtmFramerStatsEntry_Object = MibTableRow
frAtmFramerStatsEntry = _FrAtmFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1)
)
frAtmFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmFramerStatsEntry.setStatus("mandatory")
_FrAtmFramerFrmToIf_Type = Counter32
_FrAtmFramerFrmToIf_Object = MibTableColumn
frAtmFramerFrmToIf = _FrAtmFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 1),
    _FrAtmFramerFrmToIf_Type()
)
frAtmFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerFrmToIf.setStatus("mandatory")
_FrAtmFramerFrmFromIf_Type = Counter32
_FrAtmFramerFrmFromIf_Object = MibTableColumn
frAtmFramerFrmFromIf = _FrAtmFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 2),
    _FrAtmFramerFrmFromIf_Type()
)
frAtmFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerFrmFromIf.setStatus("mandatory")
_FrAtmFramerOctetFromIf_Type = Counter32
_FrAtmFramerOctetFromIf_Object = MibTableColumn
frAtmFramerOctetFromIf = _FrAtmFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 3),
    _FrAtmFramerOctetFromIf_Type()
)
frAtmFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerOctetFromIf.setStatus("mandatory")
_FrAtmFramerAborts_Type = Counter32
_FrAtmFramerAborts_Object = MibTableColumn
frAtmFramerAborts = _FrAtmFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 4),
    _FrAtmFramerAborts_Type()
)
frAtmFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerAborts.setStatus("mandatory")
_FrAtmFramerCrcErrors_Type = Counter32
_FrAtmFramerCrcErrors_Object = MibTableColumn
frAtmFramerCrcErrors = _FrAtmFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 5),
    _FrAtmFramerCrcErrors_Type()
)
frAtmFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerCrcErrors.setStatus("mandatory")
_FrAtmFramerLrcErrors_Type = Counter32
_FrAtmFramerLrcErrors_Object = MibTableColumn
frAtmFramerLrcErrors = _FrAtmFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 6),
    _FrAtmFramerLrcErrors_Type()
)
frAtmFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerLrcErrors.setStatus("mandatory")
_FrAtmFramerNonOctetErrors_Type = Counter32
_FrAtmFramerNonOctetErrors_Object = MibTableColumn
frAtmFramerNonOctetErrors = _FrAtmFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 7),
    _FrAtmFramerNonOctetErrors_Type()
)
frAtmFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerNonOctetErrors.setStatus("mandatory")
_FrAtmFramerOverruns_Type = Counter32
_FrAtmFramerOverruns_Object = MibTableColumn
frAtmFramerOverruns = _FrAtmFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 8),
    _FrAtmFramerOverruns_Type()
)
frAtmFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerOverruns.setStatus("mandatory")
_FrAtmFramerUnderruns_Type = Counter32
_FrAtmFramerUnderruns_Object = MibTableColumn
frAtmFramerUnderruns = _FrAtmFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 9),
    _FrAtmFramerUnderruns_Type()
)
frAtmFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerUnderruns.setStatus("mandatory")
_FrAtmFramerLargeFrmErrors_Type = Counter32
_FrAtmFramerLargeFrmErrors_Object = MibTableColumn
frAtmFramerLargeFrmErrors = _FrAtmFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 10),
    _FrAtmFramerLargeFrmErrors_Type()
)
frAtmFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerLargeFrmErrors.setStatus("mandatory")
_FrAtmFramerFrmModeErrors_Type = Counter32
_FrAtmFramerFrmModeErrors_Object = MibTableColumn
frAtmFramerFrmModeErrors = _FrAtmFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 13, 1, 11),
    _FrAtmFramerFrmModeErrors_Type()
)
frAtmFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerFrmModeErrors.setStatus("mandatory")
_FrAtmFramerUtilTable_Object = MibTable
frAtmFramerUtilTable = _FrAtmFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 14)
)
if mibBuilder.loadTexts:
    frAtmFramerUtilTable.setStatus("mandatory")
_FrAtmFramerUtilEntry_Object = MibTableRow
frAtmFramerUtilEntry = _FrAtmFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 14, 1)
)
frAtmFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmFramerUtilEntry.setStatus("mandatory")


class _FrAtmFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type frAtmFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrAtmFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_FrAtmFramerNormPrioLinkUtilToIf_Object = MibTableColumn
frAtmFramerNormPrioLinkUtilToIf = _FrAtmFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 14, 1, 1),
    _FrAtmFramerNormPrioLinkUtilToIf_Type()
)
frAtmFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _FrAtmFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type frAtmFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrAtmFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_FrAtmFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
frAtmFramerNormPrioLinkUtilFromIf = _FrAtmFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 2, 14, 1, 3),
    _FrAtmFramerNormPrioLinkUtilFromIf_Type()
)
frAtmFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_FrAtmLmi_ObjectIdentity = ObjectIdentity
frAtmLmi = _FrAtmLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3)
)
_FrAtmLmiRowStatusTable_Object = MibTable
frAtmLmiRowStatusTable = _FrAtmLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 1)
)
if mibBuilder.loadTexts:
    frAtmLmiRowStatusTable.setStatus("mandatory")
_FrAtmLmiRowStatusEntry_Object = MibTableRow
frAtmLmiRowStatusEntry = _FrAtmLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 1, 1)
)
frAtmLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    frAtmLmiRowStatusEntry.setStatus("mandatory")
_FrAtmLmiRowStatus_Type = RowStatus
_FrAtmLmiRowStatus_Object = MibTableColumn
frAtmLmiRowStatus = _FrAtmLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 1, 1, 1),
    _FrAtmLmiRowStatus_Type()
)
frAtmLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiRowStatus.setStatus("mandatory")
_FrAtmLmiComponentName_Type = DisplayString
_FrAtmLmiComponentName_Object = MibTableColumn
frAtmLmiComponentName = _FrAtmLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 1, 1, 2),
    _FrAtmLmiComponentName_Type()
)
frAtmLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiComponentName.setStatus("mandatory")
_FrAtmLmiStorageType_Type = StorageType
_FrAtmLmiStorageType_Object = MibTableColumn
frAtmLmiStorageType = _FrAtmLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 1, 1, 4),
    _FrAtmLmiStorageType_Type()
)
frAtmLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiStorageType.setStatus("mandatory")
_FrAtmLmiIndex_Type = NonReplicated
_FrAtmLmiIndex_Object = MibTableColumn
frAtmLmiIndex = _FrAtmLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 1, 1, 10),
    _FrAtmLmiIndex_Type()
)
frAtmLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmLmiIndex.setStatus("mandatory")
_FrAtmLmiParmsTable_Object = MibTable
frAtmLmiParmsTable = _FrAtmLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10)
)
if mibBuilder.loadTexts:
    frAtmLmiParmsTable.setStatus("mandatory")
_FrAtmLmiParmsEntry_Object = MibTableRow
frAtmLmiParmsEntry = _FrAtmLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1)
)
frAtmLmiParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    frAtmLmiParmsEntry.setStatus("mandatory")


class _FrAtmLmiProcedures_Type(Integer32):
    """Custom type frAtmLmiProcedures based on Integer32"""
    defaultValue = 4

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
        *(("ansi", 2),
          ("autoConfigure", 4),
          ("itu", 3),
          ("none", 0),
          ("vendorForum", 1))
    )


_FrAtmLmiProcedures_Type.__name__ = "Integer32"
_FrAtmLmiProcedures_Object = MibTableColumn
frAtmLmiProcedures = _FrAtmLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1, 1),
    _FrAtmLmiProcedures_Type()
)
frAtmLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiProcedures.setStatus("mandatory")


class _FrAtmLmiAsyncStatusReport_Type(Integer32):
    """Custom type frAtmLmiAsyncStatusReport based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FrAtmLmiAsyncStatusReport_Type.__name__ = "Integer32"
_FrAtmLmiAsyncStatusReport_Object = MibTableColumn
frAtmLmiAsyncStatusReport = _FrAtmLmiAsyncStatusReport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1, 2),
    _FrAtmLmiAsyncStatusReport_Type()
)
frAtmLmiAsyncStatusReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiAsyncStatusReport.setStatus("mandatory")


class _FrAtmLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type frAtmLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrAtmLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_FrAtmLmiErrorEventThreshold_Object = MibTableColumn
frAtmLmiErrorEventThreshold = _FrAtmLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1, 3),
    _FrAtmLmiErrorEventThreshold_Type()
)
frAtmLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiErrorEventThreshold.setStatus("mandatory")


class _FrAtmLmiEventCount_Type(Unsigned32):
    """Custom type frAtmLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrAtmLmiEventCount_Type.__name__ = "Unsigned32"
_FrAtmLmiEventCount_Object = MibTableColumn
frAtmLmiEventCount = _FrAtmLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1, 4),
    _FrAtmLmiEventCount_Type()
)
frAtmLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiEventCount.setStatus("mandatory")


class _FrAtmLmiCheckPointTimer_Type(Unsigned32):
    """Custom type frAtmLmiCheckPointTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_FrAtmLmiCheckPointTimer_Type.__name__ = "Unsigned32"
_FrAtmLmiCheckPointTimer_Object = MibTableColumn
frAtmLmiCheckPointTimer = _FrAtmLmiCheckPointTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1, 5),
    _FrAtmLmiCheckPointTimer_Type()
)
frAtmLmiCheckPointTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiCheckPointTimer.setStatus("mandatory")


class _FrAtmLmiMessageCountTimer_Type(Unsigned32):
    """Custom type frAtmLmiMessageCountTimer based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_FrAtmLmiMessageCountTimer_Type.__name__ = "Unsigned32"
_FrAtmLmiMessageCountTimer_Object = MibTableColumn
frAtmLmiMessageCountTimer = _FrAtmLmiMessageCountTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1, 6),
    _FrAtmLmiMessageCountTimer_Type()
)
frAtmLmiMessageCountTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiMessageCountTimer.setStatus("mandatory")


class _FrAtmLmiIgnoreActiveBit_Type(Integer32):
    """Custom type frAtmLmiIgnoreActiveBit based on Integer32"""
    defaultValue = 0

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


_FrAtmLmiIgnoreActiveBit_Type.__name__ = "Integer32"
_FrAtmLmiIgnoreActiveBit_Object = MibTableColumn
frAtmLmiIgnoreActiveBit = _FrAtmLmiIgnoreActiveBit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1, 7),
    _FrAtmLmiIgnoreActiveBit_Type()
)
frAtmLmiIgnoreActiveBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiIgnoreActiveBit.setStatus("mandatory")


class _FrAtmLmiSide_Type(Integer32):
    """Custom type frAtmLmiSide based on Integer32"""
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
        *(("both", 2),
          ("network", 0),
          ("user", 1))
    )


_FrAtmLmiSide_Type.__name__ = "Integer32"
_FrAtmLmiSide_Object = MibTableColumn
frAtmLmiSide = _FrAtmLmiSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1, 8),
    _FrAtmLmiSide_Type()
)
frAtmLmiSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiSide.setStatus("mandatory")


class _FrAtmLmiPvcConfigParmsInFsr_Type(Integer32):
    """Custom type frAtmLmiPvcConfigParmsInFsr based on Integer32"""
    defaultValue = 0

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


_FrAtmLmiPvcConfigParmsInFsr_Type.__name__ = "Integer32"
_FrAtmLmiPvcConfigParmsInFsr_Object = MibTableColumn
frAtmLmiPvcConfigParmsInFsr = _FrAtmLmiPvcConfigParmsInFsr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 10, 1, 9),
    _FrAtmLmiPvcConfigParmsInFsr_Type()
)
frAtmLmiPvcConfigParmsInFsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiPvcConfigParmsInFsr.setStatus("mandatory")
_FrAtmLmiStateTable_Object = MibTable
frAtmLmiStateTable = _FrAtmLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 11)
)
if mibBuilder.loadTexts:
    frAtmLmiStateTable.setStatus("mandatory")
_FrAtmLmiStateEntry_Object = MibTableRow
frAtmLmiStateEntry = _FrAtmLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 11, 1)
)
frAtmLmiStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    frAtmLmiStateEntry.setStatus("mandatory")


class _FrAtmLmiAdminState_Type(Integer32):
    """Custom type frAtmLmiAdminState based on Integer32"""
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


_FrAtmLmiAdminState_Type.__name__ = "Integer32"
_FrAtmLmiAdminState_Object = MibTableColumn
frAtmLmiAdminState = _FrAtmLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 11, 1, 1),
    _FrAtmLmiAdminState_Type()
)
frAtmLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiAdminState.setStatus("mandatory")


class _FrAtmLmiOperationalState_Type(Integer32):
    """Custom type frAtmLmiOperationalState based on Integer32"""
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


_FrAtmLmiOperationalState_Type.__name__ = "Integer32"
_FrAtmLmiOperationalState_Object = MibTableColumn
frAtmLmiOperationalState = _FrAtmLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 11, 1, 2),
    _FrAtmLmiOperationalState_Type()
)
frAtmLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiOperationalState.setStatus("mandatory")


class _FrAtmLmiUsageState_Type(Integer32):
    """Custom type frAtmLmiUsageState based on Integer32"""
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


_FrAtmLmiUsageState_Type.__name__ = "Integer32"
_FrAtmLmiUsageState_Object = MibTableColumn
frAtmLmiUsageState = _FrAtmLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 11, 1, 3),
    _FrAtmLmiUsageState_Type()
)
frAtmLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiUsageState.setStatus("mandatory")
_FrAtmLmiPsiTable_Object = MibTable
frAtmLmiPsiTable = _FrAtmLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 12)
)
if mibBuilder.loadTexts:
    frAtmLmiPsiTable.setStatus("mandatory")
_FrAtmLmiPsiEntry_Object = MibTableRow
frAtmLmiPsiEntry = _FrAtmLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 12, 1)
)
frAtmLmiPsiEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    frAtmLmiPsiEntry.setStatus("mandatory")


class _FrAtmLmiProtocolStatus_Type(Integer32):
    """Custom type frAtmLmiProtocolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuring", 2),
          ("errorCondition", 0),
          ("normalCondition", 1))
    )


_FrAtmLmiProtocolStatus_Type.__name__ = "Integer32"
_FrAtmLmiProtocolStatus_Object = MibTableColumn
frAtmLmiProtocolStatus = _FrAtmLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 12, 1, 1),
    _FrAtmLmiProtocolStatus_Type()
)
frAtmLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiProtocolStatus.setStatus("mandatory")


class _FrAtmLmiOpProcedures_Type(Integer32):
    """Custom type frAtmLmiOpProcedures based on Integer32"""
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
        *(("ansi", 2),
          ("itu", 3),
          ("none", 0),
          ("unknown", 4),
          ("vendorForum", 1))
    )


_FrAtmLmiOpProcedures_Type.__name__ = "Integer32"
_FrAtmLmiOpProcedures_Object = MibTableColumn
frAtmLmiOpProcedures = _FrAtmLmiOpProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 12, 1, 2),
    _FrAtmLmiOpProcedures_Type()
)
frAtmLmiOpProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiOpProcedures.setStatus("mandatory")
_FrAtmLmiStatsTable_Object = MibTable
frAtmLmiStatsTable = _FrAtmLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13)
)
if mibBuilder.loadTexts:
    frAtmLmiStatsTable.setStatus("mandatory")
_FrAtmLmiStatsEntry_Object = MibTableRow
frAtmLmiStatsEntry = _FrAtmLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1)
)
frAtmLmiStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    frAtmLmiStatsEntry.setStatus("mandatory")
_FrAtmLmiKeepAliveStatusToIf_Type = Counter32
_FrAtmLmiKeepAliveStatusToIf_Object = MibTableColumn
frAtmLmiKeepAliveStatusToIf = _FrAtmLmiKeepAliveStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 1),
    _FrAtmLmiKeepAliveStatusToIf_Type()
)
frAtmLmiKeepAliveStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiKeepAliveStatusToIf.setStatus("mandatory")
_FrAtmLmiFullStatusToIf_Type = Counter32
_FrAtmLmiFullStatusToIf_Object = MibTableColumn
frAtmLmiFullStatusToIf = _FrAtmLmiFullStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 2),
    _FrAtmLmiFullStatusToIf_Type()
)
frAtmLmiFullStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiFullStatusToIf.setStatus("mandatory")
_FrAtmLmiKeepAliveStatusEnqFromIf_Type = Counter32
_FrAtmLmiKeepAliveStatusEnqFromIf_Object = MibTableColumn
frAtmLmiKeepAliveStatusEnqFromIf = _FrAtmLmiKeepAliveStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 3),
    _FrAtmLmiKeepAliveStatusEnqFromIf_Type()
)
frAtmLmiKeepAliveStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiKeepAliveStatusEnqFromIf.setStatus("mandatory")
_FrAtmLmiFullStatusEnqFromIf_Type = Counter32
_FrAtmLmiFullStatusEnqFromIf_Object = MibTableColumn
frAtmLmiFullStatusEnqFromIf = _FrAtmLmiFullStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 4),
    _FrAtmLmiFullStatusEnqFromIf_Type()
)
frAtmLmiFullStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiFullStatusEnqFromIf.setStatus("mandatory")


class _FrAtmLmiNetworkSideEventHistory_Type(AsciiString):
    """Custom type frAtmLmiNetworkSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FrAtmLmiNetworkSideEventHistory_Type.__name__ = "AsciiString"
_FrAtmLmiNetworkSideEventHistory_Object = MibTableColumn
frAtmLmiNetworkSideEventHistory = _FrAtmLmiNetworkSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 5),
    _FrAtmLmiNetworkSideEventHistory_Type()
)
frAtmLmiNetworkSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiNetworkSideEventHistory.setStatus("mandatory")
_FrAtmLmiProtocolErrors_Type = Counter32
_FrAtmLmiProtocolErrors_Object = MibTableColumn
frAtmLmiProtocolErrors = _FrAtmLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 6),
    _FrAtmLmiProtocolErrors_Type()
)
frAtmLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiProtocolErrors.setStatus("mandatory")
_FrAtmLmiUnexpectedIes_Type = Counter32
_FrAtmLmiUnexpectedIes_Object = MibTableColumn
frAtmLmiUnexpectedIes = _FrAtmLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 7),
    _FrAtmLmiUnexpectedIes_Type()
)
frAtmLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiUnexpectedIes.setStatus("mandatory")
_FrAtmLmiSequenceErrors_Type = Counter32
_FrAtmLmiSequenceErrors_Object = MibTableColumn
frAtmLmiSequenceErrors = _FrAtmLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 8),
    _FrAtmLmiSequenceErrors_Type()
)
frAtmLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiSequenceErrors.setStatus("mandatory")
_FrAtmLmiUnexpectedReports_Type = Counter32
_FrAtmLmiUnexpectedReports_Object = MibTableColumn
frAtmLmiUnexpectedReports = _FrAtmLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 9),
    _FrAtmLmiUnexpectedReports_Type()
)
frAtmLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiUnexpectedReports.setStatus("mandatory")
_FrAtmLmiPollingVerifTimeouts_Type = Counter32
_FrAtmLmiPollingVerifTimeouts_Object = MibTableColumn
frAtmLmiPollingVerifTimeouts = _FrAtmLmiPollingVerifTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 10),
    _FrAtmLmiPollingVerifTimeouts_Type()
)
frAtmLmiPollingVerifTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiPollingVerifTimeouts.setStatus("mandatory")
_FrAtmLmiKeepAliveEnqToIf_Type = Counter32
_FrAtmLmiKeepAliveEnqToIf_Object = MibTableColumn
frAtmLmiKeepAliveEnqToIf = _FrAtmLmiKeepAliveEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 11),
    _FrAtmLmiKeepAliveEnqToIf_Type()
)
frAtmLmiKeepAliveEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiKeepAliveEnqToIf.setStatus("mandatory")
_FrAtmLmiFullStatusEnqToIf_Type = Counter32
_FrAtmLmiFullStatusEnqToIf_Object = MibTableColumn
frAtmLmiFullStatusEnqToIf = _FrAtmLmiFullStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 12),
    _FrAtmLmiFullStatusEnqToIf_Type()
)
frAtmLmiFullStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiFullStatusEnqToIf.setStatus("mandatory")


class _FrAtmLmiUserSideEventHistory_Type(AsciiString):
    """Custom type frAtmLmiUserSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FrAtmLmiUserSideEventHistory_Type.__name__ = "AsciiString"
_FrAtmLmiUserSideEventHistory_Object = MibTableColumn
frAtmLmiUserSideEventHistory = _FrAtmLmiUserSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 13),
    _FrAtmLmiUserSideEventHistory_Type()
)
frAtmLmiUserSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiUserSideEventHistory.setStatus("mandatory")
_FrAtmLmiStatusSequenceErrors_Type = Counter32
_FrAtmLmiStatusSequenceErrors_Object = MibTableColumn
frAtmLmiStatusSequenceErrors = _FrAtmLmiStatusSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 14),
    _FrAtmLmiStatusSequenceErrors_Type()
)
frAtmLmiStatusSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiStatusSequenceErrors.setStatus("mandatory")
_FrAtmLmiNoStatusReportCount_Type = Counter32
_FrAtmLmiNoStatusReportCount_Object = MibTableColumn
frAtmLmiNoStatusReportCount = _FrAtmLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 13, 1, 15),
    _FrAtmLmiNoStatusReportCount_Type()
)
frAtmLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLmiNoStatusReportCount.setStatus("mandatory")
_FrAtmLmiUspParmsTable_Object = MibTable
frAtmLmiUspParmsTable = _FrAtmLmiUspParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 14)
)
if mibBuilder.loadTexts:
    frAtmLmiUspParmsTable.setStatus("mandatory")
_FrAtmLmiUspParmsEntry_Object = MibTableRow
frAtmLmiUspParmsEntry = _FrAtmLmiUspParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 14, 1)
)
frAtmLmiUspParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmLmiIndex"),
)
if mibBuilder.loadTexts:
    frAtmLmiUspParmsEntry.setStatus("mandatory")


class _FrAtmLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type frAtmLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrAtmLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_FrAtmLmiFullStatusPollingCycles_Object = MibTableColumn
frAtmLmiFullStatusPollingCycles = _FrAtmLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 14, 1, 1),
    _FrAtmLmiFullStatusPollingCycles_Type()
)
frAtmLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiFullStatusPollingCycles.setStatus("mandatory")


class _FrAtmLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type frAtmLmiLinkVerificationTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_FrAtmLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_FrAtmLmiLinkVerificationTimer_Object = MibTableColumn
frAtmLmiLinkVerificationTimer = _FrAtmLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 3, 14, 1, 2),
    _FrAtmLmiLinkVerificationTimer_Type()
)
frAtmLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmLmiLinkVerificationTimer.setStatus("mandatory")
_FrAtmDlci_ObjectIdentity = ObjectIdentity
frAtmDlci = _FrAtmDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4)
)
_FrAtmDlciRowStatusTable_Object = MibTable
frAtmDlciRowStatusTable = _FrAtmDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciRowStatusTable.setStatus("mandatory")
_FrAtmDlciRowStatusEntry_Object = MibTableRow
frAtmDlciRowStatusEntry = _FrAtmDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 1, 1)
)
frAtmDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciRowStatusEntry.setStatus("mandatory")
_FrAtmDlciRowStatus_Type = RowStatus
_FrAtmDlciRowStatus_Object = MibTableColumn
frAtmDlciRowStatus = _FrAtmDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 1, 1, 1),
    _FrAtmDlciRowStatus_Type()
)
frAtmDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciRowStatus.setStatus("mandatory")
_FrAtmDlciComponentName_Type = DisplayString
_FrAtmDlciComponentName_Object = MibTableColumn
frAtmDlciComponentName = _FrAtmDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 1, 1, 2),
    _FrAtmDlciComponentName_Type()
)
frAtmDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciComponentName.setStatus("mandatory")
_FrAtmDlciStorageType_Type = StorageType
_FrAtmDlciStorageType_Object = MibTableColumn
frAtmDlciStorageType = _FrAtmDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 1, 1, 4),
    _FrAtmDlciStorageType_Type()
)
frAtmDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciStorageType.setStatus("mandatory")


class _FrAtmDlciIndex_Type(Integer32):
    """Custom type frAtmDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrAtmDlciIndex_Type.__name__ = "Integer32"
_FrAtmDlciIndex_Object = MibTableColumn
frAtmDlciIndex = _FrAtmDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 1, 1, 10),
    _FrAtmDlciIndex_Type()
)
frAtmDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciIndex.setStatus("mandatory")
_FrAtmDlciSp_ObjectIdentity = ObjectIdentity
frAtmDlciSp = _FrAtmDlciSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2)
)
_FrAtmDlciSpRowStatusTable_Object = MibTable
frAtmDlciSpRowStatusTable = _FrAtmDlciSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciSpRowStatusTable.setStatus("mandatory")
_FrAtmDlciSpRowStatusEntry_Object = MibTableRow
frAtmDlciSpRowStatusEntry = _FrAtmDlciSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 1, 1)
)
frAtmDlciSpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSpIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSpRowStatusEntry.setStatus("mandatory")
_FrAtmDlciSpRowStatus_Type = RowStatus
_FrAtmDlciSpRowStatus_Object = MibTableColumn
frAtmDlciSpRowStatus = _FrAtmDlciSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 1, 1, 1),
    _FrAtmDlciSpRowStatus_Type()
)
frAtmDlciSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSpRowStatus.setStatus("mandatory")
_FrAtmDlciSpComponentName_Type = DisplayString
_FrAtmDlciSpComponentName_Object = MibTableColumn
frAtmDlciSpComponentName = _FrAtmDlciSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 1, 1, 2),
    _FrAtmDlciSpComponentName_Type()
)
frAtmDlciSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSpComponentName.setStatus("mandatory")
_FrAtmDlciSpStorageType_Type = StorageType
_FrAtmDlciSpStorageType_Object = MibTableColumn
frAtmDlciSpStorageType = _FrAtmDlciSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 1, 1, 4),
    _FrAtmDlciSpStorageType_Type()
)
frAtmDlciSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSpStorageType.setStatus("mandatory")
_FrAtmDlciSpIndex_Type = NonReplicated
_FrAtmDlciSpIndex_Object = MibTableColumn
frAtmDlciSpIndex = _FrAtmDlciSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 1, 1, 10),
    _FrAtmDlciSpIndex_Type()
)
frAtmDlciSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciSpIndex.setStatus("mandatory")
_FrAtmDlciSpProvTable_Object = MibTable
frAtmDlciSpProvTable = _FrAtmDlciSpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciSpProvTable.setStatus("mandatory")
_FrAtmDlciSpProvEntry_Object = MibTableRow
frAtmDlciSpProvEntry = _FrAtmDlciSpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1)
)
frAtmDlciSpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSpIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSpProvEntry.setStatus("mandatory")


class _FrAtmDlciSpMaximumFrameSize_Type(Unsigned32):
    """Custom type frAtmDlciSpMaximumFrameSize based on Unsigned32"""
    defaultValue = 2100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_FrAtmDlciSpMaximumFrameSize_Type.__name__ = "Unsigned32"
_FrAtmDlciSpMaximumFrameSize_Object = MibTableColumn
frAtmDlciSpMaximumFrameSize = _FrAtmDlciSpMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1, 1),
    _FrAtmDlciSpMaximumFrameSize_Type()
)
frAtmDlciSpMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSpMaximumFrameSize.setStatus("mandatory")


class _FrAtmDlciSpRateEnforcement_Type(Integer32):
    """Custom type frAtmDlciSpRateEnforcement based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FrAtmDlciSpRateEnforcement_Type.__name__ = "Integer32"
_FrAtmDlciSpRateEnforcement_Object = MibTableColumn
frAtmDlciSpRateEnforcement = _FrAtmDlciSpRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1, 2),
    _FrAtmDlciSpRateEnforcement_Type()
)
frAtmDlciSpRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSpRateEnforcement.setStatus("mandatory")


class _FrAtmDlciSpCommittedInformationRate_Type(Unsigned32):
    """Custom type frAtmDlciSpCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrAtmDlciSpCommittedInformationRate_Type.__name__ = "Unsigned32"
_FrAtmDlciSpCommittedInformationRate_Object = MibTableColumn
frAtmDlciSpCommittedInformationRate = _FrAtmDlciSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1, 3),
    _FrAtmDlciSpCommittedInformationRate_Type()
)
frAtmDlciSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSpCommittedInformationRate.setStatus("mandatory")


class _FrAtmDlciSpCommittedBurstSize_Type(Unsigned32):
    """Custom type frAtmDlciSpCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrAtmDlciSpCommittedBurstSize_Type.__name__ = "Unsigned32"
_FrAtmDlciSpCommittedBurstSize_Object = MibTableColumn
frAtmDlciSpCommittedBurstSize = _FrAtmDlciSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1, 4),
    _FrAtmDlciSpCommittedBurstSize_Type()
)
frAtmDlciSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSpCommittedBurstSize.setStatus("mandatory")


class _FrAtmDlciSpExcessBurstSize_Type(Unsigned32):
    """Custom type frAtmDlciSpExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrAtmDlciSpExcessBurstSize_Type.__name__ = "Unsigned32"
_FrAtmDlciSpExcessBurstSize_Object = MibTableColumn
frAtmDlciSpExcessBurstSize = _FrAtmDlciSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1, 5),
    _FrAtmDlciSpExcessBurstSize_Type()
)
frAtmDlciSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSpExcessBurstSize.setStatus("mandatory")


class _FrAtmDlciSpMeasurementInterval_Type(Unsigned32):
    """Custom type frAtmDlciSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_FrAtmDlciSpMeasurementInterval_Type.__name__ = "Unsigned32"
_FrAtmDlciSpMeasurementInterval_Object = MibTableColumn
frAtmDlciSpMeasurementInterval = _FrAtmDlciSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1, 6),
    _FrAtmDlciSpMeasurementInterval_Type()
)
frAtmDlciSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSpMeasurementInterval.setStatus("mandatory")


class _FrAtmDlciSpEmissionPriorityToIf_Type(Integer32):
    """Custom type frAtmDlciSpEmissionPriorityToIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 0))
    )


_FrAtmDlciSpEmissionPriorityToIf_Type.__name__ = "Integer32"
_FrAtmDlciSpEmissionPriorityToIf_Object = MibTableColumn
frAtmDlciSpEmissionPriorityToIf = _FrAtmDlciSpEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1, 7),
    _FrAtmDlciSpEmissionPriorityToIf_Type()
)
frAtmDlciSpEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSpEmissionPriorityToIf.setStatus("obsolete")


class _FrAtmDlciSpEmissionPrioToIf_Type(Integer32):
    """Custom type frAtmDlciSpEmissionPrioToIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_FrAtmDlciSpEmissionPrioToIf_Type.__name__ = "Integer32"
_FrAtmDlciSpEmissionPrioToIf_Object = MibTableColumn
frAtmDlciSpEmissionPrioToIf = _FrAtmDlciSpEmissionPrioToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1, 8),
    _FrAtmDlciSpEmissionPrioToIf_Type()
)
frAtmDlciSpEmissionPrioToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSpEmissionPrioToIf.setStatus("obsolete")


class _FrAtmDlciSpAccounting_Type(Integer32):
    """Custom type frAtmDlciSpAccounting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FrAtmDlciSpAccounting_Type.__name__ = "Integer32"
_FrAtmDlciSpAccounting_Object = MibTableColumn
frAtmDlciSpAccounting = _FrAtmDlciSpAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 2, 10, 1, 9),
    _FrAtmDlciSpAccounting_Type()
)
frAtmDlciSpAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSpAccounting.setStatus("mandatory")
_FrAtmDlciSiwf_ObjectIdentity = ObjectIdentity
frAtmDlciSiwf = _FrAtmDlciSiwf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3)
)
_FrAtmDlciSiwfRowStatusTable_Object = MibTable
frAtmDlciSiwfRowStatusTable = _FrAtmDlciSiwfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfRowStatusTable.setStatus("mandatory")
_FrAtmDlciSiwfRowStatusEntry_Object = MibTableRow
frAtmDlciSiwfRowStatusEntry = _FrAtmDlciSiwfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 1, 1)
)
frAtmDlciSiwfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfRowStatusEntry.setStatus("mandatory")
_FrAtmDlciSiwfRowStatus_Type = RowStatus
_FrAtmDlciSiwfRowStatus_Object = MibTableColumn
frAtmDlciSiwfRowStatus = _FrAtmDlciSiwfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 1, 1, 1),
    _FrAtmDlciSiwfRowStatus_Type()
)
frAtmDlciSiwfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfRowStatus.setStatus("mandatory")
_FrAtmDlciSiwfComponentName_Type = DisplayString
_FrAtmDlciSiwfComponentName_Object = MibTableColumn
frAtmDlciSiwfComponentName = _FrAtmDlciSiwfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 1, 1, 2),
    _FrAtmDlciSiwfComponentName_Type()
)
frAtmDlciSiwfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfComponentName.setStatus("mandatory")
_FrAtmDlciSiwfStorageType_Type = StorageType
_FrAtmDlciSiwfStorageType_Object = MibTableColumn
frAtmDlciSiwfStorageType = _FrAtmDlciSiwfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 1, 1, 4),
    _FrAtmDlciSiwfStorageType_Type()
)
frAtmDlciSiwfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfStorageType.setStatus("mandatory")
_FrAtmDlciSiwfIndex_Type = NonReplicated
_FrAtmDlciSiwfIndex_Object = MibTableColumn
frAtmDlciSiwfIndex = _FrAtmDlciSiwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 1, 1, 10),
    _FrAtmDlciSiwfIndex_Type()
)
frAtmDlciSiwfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciSiwfIndex.setStatus("mandatory")
_FrAtmDlciSiwfSd_ObjectIdentity = ObjectIdentity
frAtmDlciSiwfSd = _FrAtmDlciSiwfSd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2)
)
_FrAtmDlciSiwfSdRowStatusTable_Object = MibTable
frAtmDlciSiwfSdRowStatusTable = _FrAtmDlciSiwfSdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdRowStatusTable.setStatus("mandatory")
_FrAtmDlciSiwfSdRowStatusEntry_Object = MibTableRow
frAtmDlciSiwfSdRowStatusEntry = _FrAtmDlciSiwfSdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 1, 1)
)
frAtmDlciSiwfSdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfSdIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdRowStatusEntry.setStatus("mandatory")
_FrAtmDlciSiwfSdRowStatus_Type = RowStatus
_FrAtmDlciSiwfSdRowStatus_Object = MibTableColumn
frAtmDlciSiwfSdRowStatus = _FrAtmDlciSiwfSdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 1, 1, 1),
    _FrAtmDlciSiwfSdRowStatus_Type()
)
frAtmDlciSiwfSdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdRowStatus.setStatus("mandatory")
_FrAtmDlciSiwfSdComponentName_Type = DisplayString
_FrAtmDlciSiwfSdComponentName_Object = MibTableColumn
frAtmDlciSiwfSdComponentName = _FrAtmDlciSiwfSdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 1, 1, 2),
    _FrAtmDlciSiwfSdComponentName_Type()
)
frAtmDlciSiwfSdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdComponentName.setStatus("mandatory")
_FrAtmDlciSiwfSdStorageType_Type = StorageType
_FrAtmDlciSiwfSdStorageType_Object = MibTableColumn
frAtmDlciSiwfSdStorageType = _FrAtmDlciSiwfSdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 1, 1, 4),
    _FrAtmDlciSiwfSdStorageType_Type()
)
frAtmDlciSiwfSdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdStorageType.setStatus("mandatory")
_FrAtmDlciSiwfSdIndex_Type = NonReplicated
_FrAtmDlciSiwfSdIndex_Object = MibTableColumn
frAtmDlciSiwfSdIndex = _FrAtmDlciSiwfSdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 1, 1, 10),
    _FrAtmDlciSiwfSdIndex_Type()
)
frAtmDlciSiwfSdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdIndex.setStatus("mandatory")
_FrAtmDlciSiwfSdProvTable_Object = MibTable
frAtmDlciSiwfSdProvTable = _FrAtmDlciSiwfSdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdProvTable.setStatus("mandatory")
_FrAtmDlciSiwfSdProvEntry_Object = MibTableRow
frAtmDlciSiwfSdProvEntry = _FrAtmDlciSiwfSdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 10, 1)
)
frAtmDlciSiwfSdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfSdIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdProvEntry.setStatus("mandatory")


class _FrAtmDlciSiwfSdMode_Type(Integer32):
    """Custom type frAtmDlciSiwfSdMode based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sameAsInterface", 255),
          ("speTranslationMode", 2),
          ("translationMode", 0),
          ("transparentMode", 1))
    )


_FrAtmDlciSiwfSdMode_Type.__name__ = "Integer32"
_FrAtmDlciSiwfSdMode_Object = MibTableColumn
frAtmDlciSiwfSdMode = _FrAtmDlciSiwfSdMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 10, 1, 1),
    _FrAtmDlciSiwfSdMode_Type()
)
frAtmDlciSiwfSdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdMode.setStatus("mandatory")


class _FrAtmDlciSiwfSdDeToClpMapping_Type(Integer32):
    """Custom type frAtmDlciSiwfSdDeToClpMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_FrAtmDlciSiwfSdDeToClpMapping_Type.__name__ = "Integer32"
_FrAtmDlciSiwfSdDeToClpMapping_Object = MibTableColumn
frAtmDlciSiwfSdDeToClpMapping = _FrAtmDlciSiwfSdDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 10, 1, 2),
    _FrAtmDlciSiwfSdDeToClpMapping_Type()
)
frAtmDlciSiwfSdDeToClpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdDeToClpMapping.setStatus("mandatory")


class _FrAtmDlciSiwfSdClpToDeMapping_Type(Integer32):
    """Custom type frAtmDlciSiwfSdClpToDeMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_FrAtmDlciSiwfSdClpToDeMapping_Type.__name__ = "Integer32"
_FrAtmDlciSiwfSdClpToDeMapping_Object = MibTableColumn
frAtmDlciSiwfSdClpToDeMapping = _FrAtmDlciSiwfSdClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 10, 1, 3),
    _FrAtmDlciSiwfSdClpToDeMapping_Type()
)
frAtmDlciSiwfSdClpToDeMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdClpToDeMapping.setStatus("mandatory")


class _FrAtmDlciSiwfSdFecnToEfciMapping_Type(Integer32):
    """Custom type frAtmDlciSiwfSdFecnToEfciMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_FrAtmDlciSiwfSdFecnToEfciMapping_Type.__name__ = "Integer32"
_FrAtmDlciSiwfSdFecnToEfciMapping_Object = MibTableColumn
frAtmDlciSiwfSdFecnToEfciMapping = _FrAtmDlciSiwfSdFecnToEfciMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 10, 1, 4),
    _FrAtmDlciSiwfSdFecnToEfciMapping_Type()
)
frAtmDlciSiwfSdFecnToEfciMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdFecnToEfciMapping.setStatus("mandatory")


class _FrAtmDlciSiwfSdCrToUuMapping_Type(Integer32):
    """Custom type frAtmDlciSiwfSdCrToUuMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_FrAtmDlciSiwfSdCrToUuMapping_Type.__name__ = "Integer32"
_FrAtmDlciSiwfSdCrToUuMapping_Object = MibTableColumn
frAtmDlciSiwfSdCrToUuMapping = _FrAtmDlciSiwfSdCrToUuMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 2, 10, 1, 5),
    _FrAtmDlciSiwfSdCrToUuMapping_Type()
)
frAtmDlciSiwfSdCrToUuMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdCrToUuMapping.setStatus("obsolete")
_FrAtmDlciSiwfNPvc_ObjectIdentity = ObjectIdentity
frAtmDlciSiwfNPvc = _FrAtmDlciSiwfNPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3)
)
_FrAtmDlciSiwfNPvcRowStatusTable_Object = MibTable
frAtmDlciSiwfNPvcRowStatusTable = _FrAtmDlciSiwfNPvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcRowStatusTable.setStatus("mandatory")
_FrAtmDlciSiwfNPvcRowStatusEntry_Object = MibTableRow
frAtmDlciSiwfNPvcRowStatusEntry = _FrAtmDlciSiwfNPvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 1, 1)
)
frAtmDlciSiwfNPvcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfNPvcIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcRowStatusEntry.setStatus("mandatory")
_FrAtmDlciSiwfNPvcRowStatus_Type = RowStatus
_FrAtmDlciSiwfNPvcRowStatus_Object = MibTableColumn
frAtmDlciSiwfNPvcRowStatus = _FrAtmDlciSiwfNPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 1, 1, 1),
    _FrAtmDlciSiwfNPvcRowStatus_Type()
)
frAtmDlciSiwfNPvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcRowStatus.setStatus("mandatory")
_FrAtmDlciSiwfNPvcComponentName_Type = DisplayString
_FrAtmDlciSiwfNPvcComponentName_Object = MibTableColumn
frAtmDlciSiwfNPvcComponentName = _FrAtmDlciSiwfNPvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 1, 1, 2),
    _FrAtmDlciSiwfNPvcComponentName_Type()
)
frAtmDlciSiwfNPvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcComponentName.setStatus("mandatory")
_FrAtmDlciSiwfNPvcStorageType_Type = StorageType
_FrAtmDlciSiwfNPvcStorageType_Object = MibTableColumn
frAtmDlciSiwfNPvcStorageType = _FrAtmDlciSiwfNPvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 1, 1, 4),
    _FrAtmDlciSiwfNPvcStorageType_Type()
)
frAtmDlciSiwfNPvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcStorageType.setStatus("mandatory")
_FrAtmDlciSiwfNPvcIndex_Type = NonReplicated
_FrAtmDlciSiwfNPvcIndex_Object = MibTableColumn
frAtmDlciSiwfNPvcIndex = _FrAtmDlciSiwfNPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 1, 1, 10),
    _FrAtmDlciSiwfNPvcIndex_Type()
)
frAtmDlciSiwfNPvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcIndex.setStatus("mandatory")
_FrAtmDlciSiwfNPvcProvTable_Object = MibTable
frAtmDlciSiwfNPvcProvTable = _FrAtmDlciSiwfNPvcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcProvTable.setStatus("mandatory")
_FrAtmDlciSiwfNPvcProvEntry_Object = MibTableRow
frAtmDlciSiwfNPvcProvEntry = _FrAtmDlciSiwfNPvcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 10, 1)
)
frAtmDlciSiwfNPvcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfNPvcIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcProvEntry.setStatus("mandatory")
_FrAtmDlciSiwfNPvcAtmConnection_Type = Link
_FrAtmDlciSiwfNPvcAtmConnection_Object = MibTableColumn
frAtmDlciSiwfNPvcAtmConnection = _FrAtmDlciSiwfNPvcAtmConnection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 10, 1, 1),
    _FrAtmDlciSiwfNPvcAtmConnection_Type()
)
frAtmDlciSiwfNPvcAtmConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcAtmConnection.setStatus("mandatory")


class _FrAtmDlciSiwfNPvcCorrelationTag_Type(HexString):
    """Custom type frAtmDlciSiwfNPvcCorrelationTag based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_FrAtmDlciSiwfNPvcCorrelationTag_Type.__name__ = "HexString"
_FrAtmDlciSiwfNPvcCorrelationTag_Object = MibTableColumn
frAtmDlciSiwfNPvcCorrelationTag = _FrAtmDlciSiwfNPvcCorrelationTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 10, 1, 3),
    _FrAtmDlciSiwfNPvcCorrelationTag_Type()
)
frAtmDlciSiwfNPvcCorrelationTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcCorrelationTag.setStatus("mandatory")
_FrAtmDlciSiwfNPvcSiwfNpvcOpTable_Object = MibTable
frAtmDlciSiwfNPvcSiwfNpvcOpTable = _FrAtmDlciSiwfNPvcSiwfNpvcOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 11)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcSiwfNpvcOpTable.setStatus("mandatory")
_FrAtmDlciSiwfNPvcSiwfNpvcOpEntry_Object = MibTableRow
frAtmDlciSiwfNPvcSiwfNpvcOpEntry = _FrAtmDlciSiwfNPvcSiwfNpvcOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 11, 1)
)
frAtmDlciSiwfNPvcSiwfNpvcOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfNPvcIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcSiwfNpvcOpEntry.setStatus("mandatory")
_FrAtmDlciSiwfNPvcConnectionToAtm_Type = RowPointer
_FrAtmDlciSiwfNPvcConnectionToAtm_Object = MibTableColumn
frAtmDlciSiwfNPvcConnectionToAtm = _FrAtmDlciSiwfNPvcConnectionToAtm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 3, 11, 1, 1),
    _FrAtmDlciSiwfNPvcConnectionToAtm_Type()
)
frAtmDlciSiwfNPvcConnectionToAtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfNPvcConnectionToAtm.setStatus("mandatory")
_FrAtmDlciSiwfSPvc_ObjectIdentity = ObjectIdentity
frAtmDlciSiwfSPvc = _FrAtmDlciSiwfSPvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4)
)
_FrAtmDlciSiwfSPvcRowStatusTable_Object = MibTable
frAtmDlciSiwfSPvcRowStatusTable = _FrAtmDlciSiwfSPvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcRowStatusTable.setStatus("mandatory")
_FrAtmDlciSiwfSPvcRowStatusEntry_Object = MibTableRow
frAtmDlciSiwfSPvcRowStatusEntry = _FrAtmDlciSiwfSPvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 1, 1)
)
frAtmDlciSiwfSPvcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfSPvcIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcRowStatusEntry.setStatus("mandatory")
_FrAtmDlciSiwfSPvcRowStatus_Type = RowStatus
_FrAtmDlciSiwfSPvcRowStatus_Object = MibTableColumn
frAtmDlciSiwfSPvcRowStatus = _FrAtmDlciSiwfSPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 1, 1, 1),
    _FrAtmDlciSiwfSPvcRowStatus_Type()
)
frAtmDlciSiwfSPvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcRowStatus.setStatus("mandatory")
_FrAtmDlciSiwfSPvcComponentName_Type = DisplayString
_FrAtmDlciSiwfSPvcComponentName_Object = MibTableColumn
frAtmDlciSiwfSPvcComponentName = _FrAtmDlciSiwfSPvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 1, 1, 2),
    _FrAtmDlciSiwfSPvcComponentName_Type()
)
frAtmDlciSiwfSPvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcComponentName.setStatus("mandatory")
_FrAtmDlciSiwfSPvcStorageType_Type = StorageType
_FrAtmDlciSiwfSPvcStorageType_Object = MibTableColumn
frAtmDlciSiwfSPvcStorageType = _FrAtmDlciSiwfSPvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 1, 1, 4),
    _FrAtmDlciSiwfSPvcStorageType_Type()
)
frAtmDlciSiwfSPvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcStorageType.setStatus("mandatory")
_FrAtmDlciSiwfSPvcIndex_Type = NonReplicated
_FrAtmDlciSiwfSPvcIndex_Object = MibTableColumn
frAtmDlciSiwfSPvcIndex = _FrAtmDlciSiwfSPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 1, 1, 10),
    _FrAtmDlciSiwfSPvcIndex_Type()
)
frAtmDlciSiwfSPvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcIndex.setStatus("mandatory")
_FrAtmDlciSiwfSPvcProvTable_Object = MibTable
frAtmDlciSiwfSPvcProvTable = _FrAtmDlciSiwfSPvcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcProvTable.setStatus("mandatory")
_FrAtmDlciSiwfSPvcProvEntry_Object = MibTableRow
frAtmDlciSiwfSPvcProvEntry = _FrAtmDlciSiwfSPvcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 10, 1)
)
frAtmDlciSiwfSPvcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfSPvcIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcProvEntry.setStatus("mandatory")


class _FrAtmDlciSiwfSPvcRemoteAddress_Type(AsciiString):
    """Custom type frAtmDlciSiwfSPvcRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 44),
    )


_FrAtmDlciSiwfSPvcRemoteAddress_Type.__name__ = "AsciiString"
_FrAtmDlciSiwfSPvcRemoteAddress_Object = MibTableColumn
frAtmDlciSiwfSPvcRemoteAddress = _FrAtmDlciSiwfSPvcRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 10, 1, 2),
    _FrAtmDlciSiwfSPvcRemoteAddress_Type()
)
frAtmDlciSiwfSPvcRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcRemoteAddress.setStatus("mandatory")


class _FrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Type(IntegerSequence):
    """Custom type frAtmDlciSiwfSPvcRemoteConnectionIdentifier based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_FrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Type.__name__ = "IntegerSequence"
_FrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Object = MibTableColumn
frAtmDlciSiwfSPvcRemoteConnectionIdentifier = _FrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 10, 1, 3),
    _FrAtmDlciSiwfSPvcRemoteConnectionIdentifier_Type()
)
frAtmDlciSiwfSPvcRemoteConnectionIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcRemoteConnectionIdentifier.setStatus("mandatory")


class _FrAtmDlciSiwfSPvcCorrelationTag_Type(HexString):
    """Custom type frAtmDlciSiwfSPvcCorrelationTag based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_FrAtmDlciSiwfSPvcCorrelationTag_Type.__name__ = "HexString"
_FrAtmDlciSiwfSPvcCorrelationTag_Object = MibTableColumn
frAtmDlciSiwfSPvcCorrelationTag = _FrAtmDlciSiwfSPvcCorrelationTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 4, 10, 1, 4),
    _FrAtmDlciSiwfSPvcCorrelationTag_Type()
)
frAtmDlciSiwfSPvcCorrelationTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSPvcCorrelationTag.setStatus("mandatory")
_FrAtmDlciSiwfQoS_ObjectIdentity = ObjectIdentity
frAtmDlciSiwfQoS = _FrAtmDlciSiwfQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5)
)
_FrAtmDlciSiwfQoSRowStatusTable_Object = MibTable
frAtmDlciSiwfQoSRowStatusTable = _FrAtmDlciSiwfQoSRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSRowStatusTable.setStatus("mandatory")
_FrAtmDlciSiwfQoSRowStatusEntry_Object = MibTableRow
frAtmDlciSiwfQoSRowStatusEntry = _FrAtmDlciSiwfQoSRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 1, 1)
)
frAtmDlciSiwfQoSRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfQoSIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSRowStatusEntry.setStatus("mandatory")
_FrAtmDlciSiwfQoSRowStatus_Type = RowStatus
_FrAtmDlciSiwfQoSRowStatus_Object = MibTableColumn
frAtmDlciSiwfQoSRowStatus = _FrAtmDlciSiwfQoSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 1, 1, 1),
    _FrAtmDlciSiwfQoSRowStatus_Type()
)
frAtmDlciSiwfQoSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSRowStatus.setStatus("mandatory")
_FrAtmDlciSiwfQoSComponentName_Type = DisplayString
_FrAtmDlciSiwfQoSComponentName_Object = MibTableColumn
frAtmDlciSiwfQoSComponentName = _FrAtmDlciSiwfQoSComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 1, 1, 2),
    _FrAtmDlciSiwfQoSComponentName_Type()
)
frAtmDlciSiwfQoSComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSComponentName.setStatus("mandatory")
_FrAtmDlciSiwfQoSStorageType_Type = StorageType
_FrAtmDlciSiwfQoSStorageType_Object = MibTableColumn
frAtmDlciSiwfQoSStorageType = _FrAtmDlciSiwfQoSStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 1, 1, 4),
    _FrAtmDlciSiwfQoSStorageType_Type()
)
frAtmDlciSiwfQoSStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSStorageType.setStatus("mandatory")
_FrAtmDlciSiwfQoSIndex_Type = NonReplicated
_FrAtmDlciSiwfQoSIndex_Object = MibTableColumn
frAtmDlciSiwfQoSIndex = _FrAtmDlciSiwfQoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 1, 1, 10),
    _FrAtmDlciSiwfQoSIndex_Type()
)
frAtmDlciSiwfQoSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSIndex.setStatus("mandatory")
_FrAtmDlciSiwfQoSProvTable_Object = MibTable
frAtmDlciSiwfQoSProvTable = _FrAtmDlciSiwfQoSProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSProvTable.setStatus("mandatory")
_FrAtmDlciSiwfQoSProvEntry_Object = MibTableRow
frAtmDlciSiwfQoSProvEntry = _FrAtmDlciSiwfQoSProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 10, 1)
)
frAtmDlciSiwfQoSProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfQoSIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSProvEntry.setStatus("mandatory")


class _FrAtmDlciSiwfQoSEmissionPriorityToIf_Type(Integer32):
    """Custom type frAtmDlciSiwfQoSEmissionPriorityToIf based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromTp", 254),
          ("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("sameAsInterface", 255))
    )


_FrAtmDlciSiwfQoSEmissionPriorityToIf_Type.__name__ = "Integer32"
_FrAtmDlciSiwfQoSEmissionPriorityToIf_Object = MibTableColumn
frAtmDlciSiwfQoSEmissionPriorityToIf = _FrAtmDlciSiwfQoSEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 10, 1, 1),
    _FrAtmDlciSiwfQoSEmissionPriorityToIf_Type()
)
frAtmDlciSiwfQoSEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSEmissionPriorityToIf.setStatus("mandatory")


class _FrAtmDlciSiwfQoSTransferPriority_Type(Integer32):
    """Custom type frAtmDlciSiwfQoSTransferPriority based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("sameAsInterface", 255))
    )


_FrAtmDlciSiwfQoSTransferPriority_Type.__name__ = "Integer32"
_FrAtmDlciSiwfQoSTransferPriority_Object = MibTableColumn
frAtmDlciSiwfQoSTransferPriority = _FrAtmDlciSiwfQoSTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 5, 10, 1, 2),
    _FrAtmDlciSiwfQoSTransferPriority_Type()
)
frAtmDlciSiwfQoSTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciSiwfQoSTransferPriority.setStatus("mandatory")
_FrAtmDlciSiwfAtmCon_ObjectIdentity = ObjectIdentity
frAtmDlciSiwfAtmCon = _FrAtmDlciSiwfAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6)
)
_FrAtmDlciSiwfAtmConRowStatusTable_Object = MibTable
frAtmDlciSiwfAtmConRowStatusTable = _FrAtmDlciSiwfAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmConRowStatusTable.setStatus("mandatory")
_FrAtmDlciSiwfAtmConRowStatusEntry_Object = MibTableRow
frAtmDlciSiwfAtmConRowStatusEntry = _FrAtmDlciSiwfAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6, 1, 1)
)
frAtmDlciSiwfAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfAtmConIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmConRowStatusEntry.setStatus("mandatory")
_FrAtmDlciSiwfAtmConRowStatus_Type = RowStatus
_FrAtmDlciSiwfAtmConRowStatus_Object = MibTableColumn
frAtmDlciSiwfAtmConRowStatus = _FrAtmDlciSiwfAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6, 1, 1, 1),
    _FrAtmDlciSiwfAtmConRowStatus_Type()
)
frAtmDlciSiwfAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmConRowStatus.setStatus("mandatory")
_FrAtmDlciSiwfAtmConComponentName_Type = DisplayString
_FrAtmDlciSiwfAtmConComponentName_Object = MibTableColumn
frAtmDlciSiwfAtmConComponentName = _FrAtmDlciSiwfAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6, 1, 1, 2),
    _FrAtmDlciSiwfAtmConComponentName_Type()
)
frAtmDlciSiwfAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmConComponentName.setStatus("mandatory")
_FrAtmDlciSiwfAtmConStorageType_Type = StorageType
_FrAtmDlciSiwfAtmConStorageType_Object = MibTableColumn
frAtmDlciSiwfAtmConStorageType = _FrAtmDlciSiwfAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6, 1, 1, 4),
    _FrAtmDlciSiwfAtmConStorageType_Type()
)
frAtmDlciSiwfAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmConStorageType.setStatus("mandatory")
_FrAtmDlciSiwfAtmConIndex_Type = NonReplicated
_FrAtmDlciSiwfAtmConIndex_Object = MibTableColumn
frAtmDlciSiwfAtmConIndex = _FrAtmDlciSiwfAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6, 1, 1, 10),
    _FrAtmDlciSiwfAtmConIndex_Type()
)
frAtmDlciSiwfAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmConIndex.setStatus("mandatory")
_FrAtmDlciSiwfAtmConOperTable_Object = MibTable
frAtmDlciSiwfAtmConOperTable = _FrAtmDlciSiwfAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmConOperTable.setStatus("mandatory")
_FrAtmDlciSiwfAtmConOperEntry_Object = MibTableRow
frAtmDlciSiwfAtmConOperEntry = _FrAtmDlciSiwfAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6, 10, 1)
)
frAtmDlciSiwfAtmConOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfAtmConIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmConOperEntry.setStatus("mandatory")
_FrAtmDlciSiwfAtmConNextHop_Type = RowPointer
_FrAtmDlciSiwfAtmConNextHop_Object = MibTableColumn
frAtmDlciSiwfAtmConNextHop = _FrAtmDlciSiwfAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 6, 10, 1, 1),
    _FrAtmDlciSiwfAtmConNextHop_Type()
)
frAtmDlciSiwfAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmConNextHop.setStatus("mandatory")
_FrAtmDlciSiwfConnOpTable_Object = MibTable
frAtmDlciSiwfConnOpTable = _FrAtmDlciSiwfConnOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 11)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfConnOpTable.setStatus("mandatory")
_FrAtmDlciSiwfConnOpEntry_Object = MibTableRow
frAtmDlciSiwfConnOpEntry = _FrAtmDlciSiwfConnOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 11, 1)
)
frAtmDlciSiwfConnOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfConnOpEntry.setStatus("mandatory")


class _FrAtmDlciSiwfDiscardPriority_Type(Integer32):
    """Custom type frAtmDlciSiwfDiscardPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp1", 1),
          ("dp2", 2),
          ("dp3", 3))
    )


_FrAtmDlciSiwfDiscardPriority_Type.__name__ = "Integer32"
_FrAtmDlciSiwfDiscardPriority_Object = MibTableColumn
frAtmDlciSiwfDiscardPriority = _FrAtmDlciSiwfDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 11, 1, 2),
    _FrAtmDlciSiwfDiscardPriority_Type()
)
frAtmDlciSiwfDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfDiscardPriority.setStatus("mandatory")


class _FrAtmDlciSiwfAtmServiceCategory_Type(Integer32):
    """Custom type frAtmDlciSiwfAtmServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("notApplicable", 5),
          ("nrtVbr", 3),
          ("rtVbr", 2),
          ("ubr", 0))
    )


_FrAtmDlciSiwfAtmServiceCategory_Type.__name__ = "Integer32"
_FrAtmDlciSiwfAtmServiceCategory_Object = MibTableColumn
frAtmDlciSiwfAtmServiceCategory = _FrAtmDlciSiwfAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 11, 1, 4),
    _FrAtmDlciSiwfAtmServiceCategory_Type()
)
frAtmDlciSiwfAtmServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfAtmServiceCategory.setStatus("mandatory")


class _FrAtmDlciSiwfTrafficParmConvPolicy_Type(Integer32):
    """Custom type frAtmDlciSiwfTrafficParmConvPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("notApplicable", 7))
    )


_FrAtmDlciSiwfTrafficParmConvPolicy_Type.__name__ = "Integer32"
_FrAtmDlciSiwfTrafficParmConvPolicy_Object = MibTableColumn
frAtmDlciSiwfTrafficParmConvPolicy = _FrAtmDlciSiwfTrafficParmConvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 11, 1, 5),
    _FrAtmDlciSiwfTrafficParmConvPolicy_Type()
)
frAtmDlciSiwfTrafficParmConvPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfTrafficParmConvPolicy.setStatus("mandatory")


class _FrAtmDlciSiwfAvgFrameSize_Type(Integer32):
    """Custom type frAtmDlciSiwfAvgFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8187),
    )


_FrAtmDlciSiwfAvgFrameSize_Type.__name__ = "Integer32"
_FrAtmDlciSiwfAvgFrameSize_Object = MibTableColumn
frAtmDlciSiwfAvgFrameSize = _FrAtmDlciSiwfAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 11, 1, 6),
    _FrAtmDlciSiwfAvgFrameSize_Type()
)
frAtmDlciSiwfAvgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfAvgFrameSize.setStatus("mandatory")


class _FrAtmDlciSiwfRemoteAddress_Type(AsciiString):
    """Custom type frAtmDlciSiwfRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_FrAtmDlciSiwfRemoteAddress_Type.__name__ = "AsciiString"
_FrAtmDlciSiwfRemoteAddress_Object = MibTableColumn
frAtmDlciSiwfRemoteAddress = _FrAtmDlciSiwfRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 11, 1, 8),
    _FrAtmDlciSiwfRemoteAddress_Type()
)
frAtmDlciSiwfRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfRemoteAddress.setStatus("mandatory")


class _FrAtmDlciSiwfRemoteConnectionIdentifier_Type(IntegerSequence):
    """Custom type frAtmDlciSiwfRemoteConnectionIdentifier based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_FrAtmDlciSiwfRemoteConnectionIdentifier_Type.__name__ = "IntegerSequence"
_FrAtmDlciSiwfRemoteConnectionIdentifier_Object = MibTableColumn
frAtmDlciSiwfRemoteConnectionIdentifier = _FrAtmDlciSiwfRemoteConnectionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 11, 1, 9),
    _FrAtmDlciSiwfRemoteConnectionIdentifier_Type()
)
frAtmDlciSiwfRemoteConnectionIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfRemoteConnectionIdentifier.setStatus("mandatory")
_FrAtmDlciSiwfSdOpTable_Object = MibTable
frAtmDlciSiwfSdOpTable = _FrAtmDlciSiwfSdOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 12)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdOpTable.setStatus("mandatory")
_FrAtmDlciSiwfSdOpEntry_Object = MibTableRow
frAtmDlciSiwfSdOpEntry = _FrAtmDlciSiwfSdOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 12, 1)
)
frAtmDlciSiwfSdOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSdOpEntry.setStatus("mandatory")


class _FrAtmDlciSiwfMode_Type(Integer32):
    """Custom type frAtmDlciSiwfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speTranslationMode", 2),
          ("translationMode", 0),
          ("transparentMode", 1))
    )


_FrAtmDlciSiwfMode_Type.__name__ = "Integer32"
_FrAtmDlciSiwfMode_Object = MibTableColumn
frAtmDlciSiwfMode = _FrAtmDlciSiwfMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 12, 1, 1),
    _FrAtmDlciSiwfMode_Type()
)
frAtmDlciSiwfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfMode.setStatus("mandatory")


class _FrAtmDlciSiwfDeToClpMapping_Type(Integer32):
    """Custom type frAtmDlciSiwfDeToClpMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_FrAtmDlciSiwfDeToClpMapping_Type.__name__ = "Integer32"
_FrAtmDlciSiwfDeToClpMapping_Object = MibTableColumn
frAtmDlciSiwfDeToClpMapping = _FrAtmDlciSiwfDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 12, 1, 2),
    _FrAtmDlciSiwfDeToClpMapping_Type()
)
frAtmDlciSiwfDeToClpMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfDeToClpMapping.setStatus("mandatory")


class _FrAtmDlciSiwfClpToDeMapping_Type(Integer32):
    """Custom type frAtmDlciSiwfClpToDeMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_FrAtmDlciSiwfClpToDeMapping_Type.__name__ = "Integer32"
_FrAtmDlciSiwfClpToDeMapping_Object = MibTableColumn
frAtmDlciSiwfClpToDeMapping = _FrAtmDlciSiwfClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 12, 1, 3),
    _FrAtmDlciSiwfClpToDeMapping_Type()
)
frAtmDlciSiwfClpToDeMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfClpToDeMapping.setStatus("mandatory")


class _FrAtmDlciSiwfFecnToEfciMapping_Type(Integer32):
    """Custom type frAtmDlciSiwfFecnToEfciMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2))
    )


_FrAtmDlciSiwfFecnToEfciMapping_Type.__name__ = "Integer32"
_FrAtmDlciSiwfFecnToEfciMapping_Object = MibTableColumn
frAtmDlciSiwfFecnToEfciMapping = _FrAtmDlciSiwfFecnToEfciMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 12, 1, 4),
    _FrAtmDlciSiwfFecnToEfciMapping_Type()
)
frAtmDlciSiwfFecnToEfciMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfFecnToEfciMapping.setStatus("mandatory")


class _FrAtmDlciSiwfCrToUuMapping_Type(Integer32):
    """Custom type frAtmDlciSiwfCrToUuMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2))
    )


_FrAtmDlciSiwfCrToUuMapping_Type.__name__ = "Integer32"
_FrAtmDlciSiwfCrToUuMapping_Object = MibTableColumn
frAtmDlciSiwfCrToUuMapping = _FrAtmDlciSiwfCrToUuMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 12, 1, 5),
    _FrAtmDlciSiwfCrToUuMapping_Type()
)
frAtmDlciSiwfCrToUuMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfCrToUuMapping.setStatus("obsolete")


class _FrAtmDlciSiwfTransferPriority_Type(Integer32):
    """Custom type frAtmDlciSiwfTransferPriority based on Integer32"""
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
              253)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("notApplicable", 253))
    )


_FrAtmDlciSiwfTransferPriority_Type.__name__ = "Integer32"
_FrAtmDlciSiwfTransferPriority_Object = MibTableColumn
frAtmDlciSiwfTransferPriority = _FrAtmDlciSiwfTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 12, 1, 6),
    _FrAtmDlciSiwfTransferPriority_Type()
)
frAtmDlciSiwfTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfTransferPriority.setStatus("mandatory")


class _FrAtmDlciSiwfAssignedBandwidthPool_Type(Integer32):
    """Custom type frAtmDlciSiwfAssignedBandwidthPool based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_FrAtmDlciSiwfAssignedBandwidthPool_Type.__name__ = "Integer32"
_FrAtmDlciSiwfAssignedBandwidthPool_Object = MibTableColumn
frAtmDlciSiwfAssignedBandwidthPool = _FrAtmDlciSiwfAssignedBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 12, 1, 7),
    _FrAtmDlciSiwfAssignedBandwidthPool_Type()
)
frAtmDlciSiwfAssignedBandwidthPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfAssignedBandwidthPool.setStatus("mandatory")
_FrAtmDlciSiwfSiwfSpvcOpTable_Object = MibTable
frAtmDlciSiwfSiwfSpvcOpTable = _FrAtmDlciSiwfSiwfSpvcOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSiwfSpvcOpTable.setStatus("mandatory")
_FrAtmDlciSiwfSiwfSpvcOpEntry_Object = MibTableRow
frAtmDlciSiwfSiwfSpvcOpEntry = _FrAtmDlciSiwfSiwfSpvcOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1)
)
frAtmDlciSiwfSiwfSpvcOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfSiwfSpvcOpEntry.setStatus("mandatory")


class _FrAtmDlciSiwfPeakCellRate0_Type(Unsigned32):
    """Custom type frAtmDlciSiwfPeakCellRate0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciSiwfPeakCellRate0_Type.__name__ = "Unsigned32"
_FrAtmDlciSiwfPeakCellRate0_Object = MibTableColumn
frAtmDlciSiwfPeakCellRate0 = _FrAtmDlciSiwfPeakCellRate0_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 1),
    _FrAtmDlciSiwfPeakCellRate0_Type()
)
frAtmDlciSiwfPeakCellRate0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfPeakCellRate0.setStatus("mandatory")


class _FrAtmDlciSiwfPeakCellRate01_Type(Unsigned32):
    """Custom type frAtmDlciSiwfPeakCellRate01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciSiwfPeakCellRate01_Type.__name__ = "Unsigned32"
_FrAtmDlciSiwfPeakCellRate01_Object = MibTableColumn
frAtmDlciSiwfPeakCellRate01 = _FrAtmDlciSiwfPeakCellRate01_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 2),
    _FrAtmDlciSiwfPeakCellRate01_Type()
)
frAtmDlciSiwfPeakCellRate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfPeakCellRate01.setStatus("mandatory")


class _FrAtmDlciSiwfSustainedCellRate0_Type(Unsigned32):
    """Custom type frAtmDlciSiwfSustainedCellRate0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciSiwfSustainedCellRate0_Type.__name__ = "Unsigned32"
_FrAtmDlciSiwfSustainedCellRate0_Object = MibTableColumn
frAtmDlciSiwfSustainedCellRate0 = _FrAtmDlciSiwfSustainedCellRate0_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 3),
    _FrAtmDlciSiwfSustainedCellRate0_Type()
)
frAtmDlciSiwfSustainedCellRate0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSustainedCellRate0.setStatus("mandatory")


class _FrAtmDlciSiwfSustainedCellRate01_Type(Unsigned32):
    """Custom type frAtmDlciSiwfSustainedCellRate01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciSiwfSustainedCellRate01_Type.__name__ = "Unsigned32"
_FrAtmDlciSiwfSustainedCellRate01_Object = MibTableColumn
frAtmDlciSiwfSustainedCellRate01 = _FrAtmDlciSiwfSustainedCellRate01_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 4),
    _FrAtmDlciSiwfSustainedCellRate01_Type()
)
frAtmDlciSiwfSustainedCellRate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfSustainedCellRate01.setStatus("mandatory")


class _FrAtmDlciSiwfMaximumBurstSize0_Type(Unsigned32):
    """Custom type frAtmDlciSiwfMaximumBurstSize0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciSiwfMaximumBurstSize0_Type.__name__ = "Unsigned32"
_FrAtmDlciSiwfMaximumBurstSize0_Object = MibTableColumn
frAtmDlciSiwfMaximumBurstSize0 = _FrAtmDlciSiwfMaximumBurstSize0_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 5),
    _FrAtmDlciSiwfMaximumBurstSize0_Type()
)
frAtmDlciSiwfMaximumBurstSize0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfMaximumBurstSize0.setStatus("mandatory")


class _FrAtmDlciSiwfMaximumBurstSize01_Type(Unsigned32):
    """Custom type frAtmDlciSiwfMaximumBurstSize01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciSiwfMaximumBurstSize01_Type.__name__ = "Unsigned32"
_FrAtmDlciSiwfMaximumBurstSize01_Object = MibTableColumn
frAtmDlciSiwfMaximumBurstSize01 = _FrAtmDlciSiwfMaximumBurstSize01_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 6),
    _FrAtmDlciSiwfMaximumBurstSize01_Type()
)
frAtmDlciSiwfMaximumBurstSize01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfMaximumBurstSize01.setStatus("mandatory")


class _FrAtmDlciSiwfEquivalentBitRate_Type(Unsigned32):
    """Custom type frAtmDlciSiwfEquivalentBitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciSiwfEquivalentBitRate_Type.__name__ = "Unsigned32"
_FrAtmDlciSiwfEquivalentBitRate_Object = MibTableColumn
frAtmDlciSiwfEquivalentBitRate = _FrAtmDlciSiwfEquivalentBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 7),
    _FrAtmDlciSiwfEquivalentBitRate_Type()
)
frAtmDlciSiwfEquivalentBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfEquivalentBitRate.setStatus("mandatory")


class _FrAtmDlciSiwfType_Type(Integer32):
    """Custom type frAtmDlciSiwfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("notApplicable", 2),
          ("slave", 1))
    )


_FrAtmDlciSiwfType_Type.__name__ = "Integer32"
_FrAtmDlciSiwfType_Object = MibTableColumn
frAtmDlciSiwfType = _FrAtmDlciSiwfType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 9),
    _FrAtmDlciSiwfType_Type()
)
frAtmDlciSiwfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfType.setStatus("mandatory")


class _FrAtmDlciSiwfVccClearCause_Type(Unsigned32):
    """Custom type frAtmDlciSiwfVccClearCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrAtmDlciSiwfVccClearCause_Type.__name__ = "Unsigned32"
_FrAtmDlciSiwfVccClearCause_Object = MibTableColumn
frAtmDlciSiwfVccClearCause = _FrAtmDlciSiwfVccClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 10),
    _FrAtmDlciSiwfVccClearCause_Type()
)
frAtmDlciSiwfVccClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfVccClearCause.setStatus("mandatory")


class _FrAtmDlciSiwfVccCauseDiag_Type(HexString):
    """Custom type frAtmDlciSiwfVccCauseDiag based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FrAtmDlciSiwfVccCauseDiag_Type.__name__ = "HexString"
_FrAtmDlciSiwfVccCauseDiag_Object = MibTableColumn
frAtmDlciSiwfVccCauseDiag = _FrAtmDlciSiwfVccCauseDiag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 13, 1, 15),
    _FrAtmDlciSiwfVccCauseDiag_Type()
)
frAtmDlciSiwfVccCauseDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfVccCauseDiag.setStatus("mandatory")
_FrAtmDlciSiwfStatsTable_Object = MibTable
frAtmDlciSiwfStatsTable = _FrAtmDlciSiwfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 14)
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfStatsTable.setStatus("mandatory")
_FrAtmDlciSiwfStatsEntry_Object = MibTableRow
frAtmDlciSiwfStatsEntry = _FrAtmDlciSiwfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 14, 1)
)
frAtmDlciSiwfStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciSiwfIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSiwfStatsEntry.setStatus("mandatory")
_FrAtmDlciSiwfUnknown1490Frames_Type = Counter32
_FrAtmDlciSiwfUnknown1490Frames_Object = MibTableColumn
frAtmDlciSiwfUnknown1490Frames = _FrAtmDlciSiwfUnknown1490Frames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 14, 1, 1),
    _FrAtmDlciSiwfUnknown1490Frames_Type()
)
frAtmDlciSiwfUnknown1490Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfUnknown1490Frames.setStatus("mandatory")
_FrAtmDlciSiwfInvalid1490Frames_Type = Counter32
_FrAtmDlciSiwfInvalid1490Frames_Object = MibTableColumn
frAtmDlciSiwfInvalid1490Frames = _FrAtmDlciSiwfInvalid1490Frames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 14, 1, 2),
    _FrAtmDlciSiwfInvalid1490Frames_Type()
)
frAtmDlciSiwfInvalid1490Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfInvalid1490Frames.setStatus("mandatory")


class _FrAtmDlciSiwfLastUnknown1490ProtocolHeader_Type(HexString):
    """Custom type frAtmDlciSiwfLastUnknown1490ProtocolHeader based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FrAtmDlciSiwfLastUnknown1490ProtocolHeader_Type.__name__ = "HexString"
_FrAtmDlciSiwfLastUnknown1490ProtocolHeader_Object = MibTableColumn
frAtmDlciSiwfLastUnknown1490ProtocolHeader = _FrAtmDlciSiwfLastUnknown1490ProtocolHeader_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 14, 1, 3),
    _FrAtmDlciSiwfLastUnknown1490ProtocolHeader_Type()
)
frAtmDlciSiwfLastUnknown1490ProtocolHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfLastUnknown1490ProtocolHeader.setStatus("mandatory")
_FrAtmDlciSiwfUnknown1483Frames_Type = Counter32
_FrAtmDlciSiwfUnknown1483Frames_Object = MibTableColumn
frAtmDlciSiwfUnknown1483Frames = _FrAtmDlciSiwfUnknown1483Frames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 14, 1, 4),
    _FrAtmDlciSiwfUnknown1483Frames_Type()
)
frAtmDlciSiwfUnknown1483Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfUnknown1483Frames.setStatus("mandatory")
_FrAtmDlciSiwfInvalid1483Frames_Type = Counter32
_FrAtmDlciSiwfInvalid1483Frames_Object = MibTableColumn
frAtmDlciSiwfInvalid1483Frames = _FrAtmDlciSiwfInvalid1483Frames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 14, 1, 5),
    _FrAtmDlciSiwfInvalid1483Frames_Type()
)
frAtmDlciSiwfInvalid1483Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfInvalid1483Frames.setStatus("mandatory")


class _FrAtmDlciSiwfLastUnknown1483ProtocolHeader_Type(HexString):
    """Custom type frAtmDlciSiwfLastUnknown1483ProtocolHeader based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FrAtmDlciSiwfLastUnknown1483ProtocolHeader_Type.__name__ = "HexString"
_FrAtmDlciSiwfLastUnknown1483ProtocolHeader_Object = MibTableColumn
frAtmDlciSiwfLastUnknown1483ProtocolHeader = _FrAtmDlciSiwfLastUnknown1483ProtocolHeader_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 3, 14, 1, 6),
    _FrAtmDlciSiwfLastUnknown1483ProtocolHeader_Type()
)
frAtmDlciSiwfLastUnknown1483ProtocolHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciSiwfLastUnknown1483ProtocolHeader.setStatus("mandatory")
_FrAtmDlciNiwf_ObjectIdentity = ObjectIdentity
frAtmDlciNiwf = _FrAtmDlciNiwf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4)
)
_FrAtmDlciNiwfRowStatusTable_Object = MibTable
frAtmDlciNiwfRowStatusTable = _FrAtmDlciNiwfRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfRowStatusTable.setStatus("mandatory")
_FrAtmDlciNiwfRowStatusEntry_Object = MibTableRow
frAtmDlciNiwfRowStatusEntry = _FrAtmDlciNiwfRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 1, 1)
)
frAtmDlciNiwfRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfRowStatusEntry.setStatus("mandatory")
_FrAtmDlciNiwfRowStatus_Type = RowStatus
_FrAtmDlciNiwfRowStatus_Object = MibTableColumn
frAtmDlciNiwfRowStatus = _FrAtmDlciNiwfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 1, 1, 1),
    _FrAtmDlciNiwfRowStatus_Type()
)
frAtmDlciNiwfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfRowStatus.setStatus("mandatory")
_FrAtmDlciNiwfComponentName_Type = DisplayString
_FrAtmDlciNiwfComponentName_Object = MibTableColumn
frAtmDlciNiwfComponentName = _FrAtmDlciNiwfComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 1, 1, 2),
    _FrAtmDlciNiwfComponentName_Type()
)
frAtmDlciNiwfComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfComponentName.setStatus("mandatory")
_FrAtmDlciNiwfStorageType_Type = StorageType
_FrAtmDlciNiwfStorageType_Object = MibTableColumn
frAtmDlciNiwfStorageType = _FrAtmDlciNiwfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 1, 1, 4),
    _FrAtmDlciNiwfStorageType_Type()
)
frAtmDlciNiwfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfStorageType.setStatus("mandatory")
_FrAtmDlciNiwfIndex_Type = NonReplicated
_FrAtmDlciNiwfIndex_Object = MibTableColumn
frAtmDlciNiwfIndex = _FrAtmDlciNiwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 1, 1, 10),
    _FrAtmDlciNiwfIndex_Type()
)
frAtmDlciNiwfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciNiwfIndex.setStatus("mandatory")
_FrAtmDlciNiwfSpvc_ObjectIdentity = ObjectIdentity
frAtmDlciNiwfSpvc = _FrAtmDlciNiwfSpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2)
)
_FrAtmDlciNiwfSpvcRowStatusTable_Object = MibTable
frAtmDlciNiwfSpvcRowStatusTable = _FrAtmDlciNiwfSpvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcRowStatusTable.setStatus("mandatory")
_FrAtmDlciNiwfSpvcRowStatusEntry_Object = MibTableRow
frAtmDlciNiwfSpvcRowStatusEntry = _FrAtmDlciNiwfSpvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 1, 1)
)
frAtmDlciNiwfSpvcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfSpvcIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcRowStatusEntry.setStatus("mandatory")
_FrAtmDlciNiwfSpvcRowStatus_Type = RowStatus
_FrAtmDlciNiwfSpvcRowStatus_Object = MibTableColumn
frAtmDlciNiwfSpvcRowStatus = _FrAtmDlciNiwfSpvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 1, 1, 1),
    _FrAtmDlciNiwfSpvcRowStatus_Type()
)
frAtmDlciNiwfSpvcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcRowStatus.setStatus("mandatory")
_FrAtmDlciNiwfSpvcComponentName_Type = DisplayString
_FrAtmDlciNiwfSpvcComponentName_Object = MibTableColumn
frAtmDlciNiwfSpvcComponentName = _FrAtmDlciNiwfSpvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 1, 1, 2),
    _FrAtmDlciNiwfSpvcComponentName_Type()
)
frAtmDlciNiwfSpvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcComponentName.setStatus("mandatory")
_FrAtmDlciNiwfSpvcStorageType_Type = StorageType
_FrAtmDlciNiwfSpvcStorageType_Object = MibTableColumn
frAtmDlciNiwfSpvcStorageType = _FrAtmDlciNiwfSpvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 1, 1, 4),
    _FrAtmDlciNiwfSpvcStorageType_Type()
)
frAtmDlciNiwfSpvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcStorageType.setStatus("mandatory")
_FrAtmDlciNiwfSpvcIndex_Type = NonReplicated
_FrAtmDlciNiwfSpvcIndex_Object = MibTableColumn
frAtmDlciNiwfSpvcIndex = _FrAtmDlciNiwfSpvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 1, 1, 10),
    _FrAtmDlciNiwfSpvcIndex_Type()
)
frAtmDlciNiwfSpvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcIndex.setStatus("mandatory")
_FrAtmDlciNiwfSpvcProvTable_Object = MibTable
frAtmDlciNiwfSpvcProvTable = _FrAtmDlciNiwfSpvcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcProvTable.setStatus("mandatory")
_FrAtmDlciNiwfSpvcProvEntry_Object = MibTableRow
frAtmDlciNiwfSpvcProvEntry = _FrAtmDlciNiwfSpvcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 10, 1)
)
frAtmDlciNiwfSpvcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfSpvcIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcProvEntry.setStatus("mandatory")


class _FrAtmDlciNiwfSpvcRemoteAddress_Type(AsciiString):
    """Custom type frAtmDlciNiwfSpvcRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_FrAtmDlciNiwfSpvcRemoteAddress_Type.__name__ = "AsciiString"
_FrAtmDlciNiwfSpvcRemoteAddress_Object = MibTableColumn
frAtmDlciNiwfSpvcRemoteAddress = _FrAtmDlciNiwfSpvcRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 10, 1, 1),
    _FrAtmDlciNiwfSpvcRemoteAddress_Type()
)
frAtmDlciNiwfSpvcRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcRemoteAddress.setStatus("mandatory")


class _FrAtmDlciNiwfSpvcRemoteDlci_Type(Integer32):
    """Custom type frAtmDlciNiwfSpvcRemoteDlci based on Integer32"""
    defaultValue = 1022

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
        ValueRangeConstraint(1022, 1022),
    )


_FrAtmDlciNiwfSpvcRemoteDlci_Type.__name__ = "Integer32"
_FrAtmDlciNiwfSpvcRemoteDlci_Object = MibTableColumn
frAtmDlciNiwfSpvcRemoteDlci = _FrAtmDlciNiwfSpvcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 10, 1, 2),
    _FrAtmDlciNiwfSpvcRemoteDlci_Type()
)
frAtmDlciNiwfSpvcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcRemoteDlci.setStatus("mandatory")


class _FrAtmDlciNiwfSpvcCorrelationTag_Type(HexString):
    """Custom type frAtmDlciNiwfSpvcCorrelationTag based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_FrAtmDlciNiwfSpvcCorrelationTag_Type.__name__ = "HexString"
_FrAtmDlciNiwfSpvcCorrelationTag_Object = MibTableColumn
frAtmDlciNiwfSpvcCorrelationTag = _FrAtmDlciNiwfSpvcCorrelationTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 2, 10, 1, 3),
    _FrAtmDlciNiwfSpvcCorrelationTag_Type()
)
frAtmDlciNiwfSpvcCorrelationTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfSpvcCorrelationTag.setStatus("mandatory")
_FrAtmDlciNiwfNd_ObjectIdentity = ObjectIdentity
frAtmDlciNiwfNd = _FrAtmDlciNiwfNd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3)
)
_FrAtmDlciNiwfNdRowStatusTable_Object = MibTable
frAtmDlciNiwfNdRowStatusTable = _FrAtmDlciNiwfNdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdRowStatusTable.setStatus("mandatory")
_FrAtmDlciNiwfNdRowStatusEntry_Object = MibTableRow
frAtmDlciNiwfNdRowStatusEntry = _FrAtmDlciNiwfNdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 1, 1)
)
frAtmDlciNiwfNdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfNdIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdRowStatusEntry.setStatus("mandatory")
_FrAtmDlciNiwfNdRowStatus_Type = RowStatus
_FrAtmDlciNiwfNdRowStatus_Object = MibTableColumn
frAtmDlciNiwfNdRowStatus = _FrAtmDlciNiwfNdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 1, 1, 1),
    _FrAtmDlciNiwfNdRowStatus_Type()
)
frAtmDlciNiwfNdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdRowStatus.setStatus("mandatory")
_FrAtmDlciNiwfNdComponentName_Type = DisplayString
_FrAtmDlciNiwfNdComponentName_Object = MibTableColumn
frAtmDlciNiwfNdComponentName = _FrAtmDlciNiwfNdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 1, 1, 2),
    _FrAtmDlciNiwfNdComponentName_Type()
)
frAtmDlciNiwfNdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdComponentName.setStatus("mandatory")
_FrAtmDlciNiwfNdStorageType_Type = StorageType
_FrAtmDlciNiwfNdStorageType_Object = MibTableColumn
frAtmDlciNiwfNdStorageType = _FrAtmDlciNiwfNdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 1, 1, 4),
    _FrAtmDlciNiwfNdStorageType_Type()
)
frAtmDlciNiwfNdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdStorageType.setStatus("mandatory")
_FrAtmDlciNiwfNdIndex_Type = NonReplicated
_FrAtmDlciNiwfNdIndex_Object = MibTableColumn
frAtmDlciNiwfNdIndex = _FrAtmDlciNiwfNdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 1, 1, 10),
    _FrAtmDlciNiwfNdIndex_Type()
)
frAtmDlciNiwfNdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdIndex.setStatus("mandatory")
_FrAtmDlciNiwfNdProvTable_Object = MibTable
frAtmDlciNiwfNdProvTable = _FrAtmDlciNiwfNdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdProvTable.setStatus("mandatory")
_FrAtmDlciNiwfNdProvEntry_Object = MibTableRow
frAtmDlciNiwfNdProvEntry = _FrAtmDlciNiwfNdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 10, 1)
)
frAtmDlciNiwfNdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfNdIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdProvEntry.setStatus("mandatory")


class _FrAtmDlciNiwfNdDeToClpMapping_Type(Integer32):
    """Custom type frAtmDlciNiwfNdDeToClpMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2),
          ("sameAsInterface", 255))
    )


_FrAtmDlciNiwfNdDeToClpMapping_Type.__name__ = "Integer32"
_FrAtmDlciNiwfNdDeToClpMapping_Object = MibTableColumn
frAtmDlciNiwfNdDeToClpMapping = _FrAtmDlciNiwfNdDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 10, 1, 1),
    _FrAtmDlciNiwfNdDeToClpMapping_Type()
)
frAtmDlciNiwfNdDeToClpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdDeToClpMapping.setStatus("mandatory")


class _FrAtmDlciNiwfNdClpToDeMapping_Type(Integer32):
    """Custom type frAtmDlciNiwfNdClpToDeMapping based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("preserve", 2),
          ("sameAsInterface", 255),
          ("transparent", 3))
    )


_FrAtmDlciNiwfNdClpToDeMapping_Type.__name__ = "Integer32"
_FrAtmDlciNiwfNdClpToDeMapping_Object = MibTableColumn
frAtmDlciNiwfNdClpToDeMapping = _FrAtmDlciNiwfNdClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 10, 1, 2),
    _FrAtmDlciNiwfNdClpToDeMapping_Type()
)
frAtmDlciNiwfNdClpToDeMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdClpToDeMapping.setStatus("mandatory")


class _FrAtmDlciNiwfNdTransferPriority_Type(Integer32):
    """Custom type frAtmDlciNiwfNdTransferPriority based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("sameAsInterface", 255))
    )


_FrAtmDlciNiwfNdTransferPriority_Type.__name__ = "Integer32"
_FrAtmDlciNiwfNdTransferPriority_Object = MibTableColumn
frAtmDlciNiwfNdTransferPriority = _FrAtmDlciNiwfNdTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 3, 10, 1, 3),
    _FrAtmDlciNiwfNdTransferPriority_Type()
)
frAtmDlciNiwfNdTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfNdTransferPriority.setStatus("obsolete")
_FrAtmDlciNiwfQoS_ObjectIdentity = ObjectIdentity
frAtmDlciNiwfQoS = _FrAtmDlciNiwfQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4)
)
_FrAtmDlciNiwfQoSRowStatusTable_Object = MibTable
frAtmDlciNiwfQoSRowStatusTable = _FrAtmDlciNiwfQoSRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSRowStatusTable.setStatus("mandatory")
_FrAtmDlciNiwfQoSRowStatusEntry_Object = MibTableRow
frAtmDlciNiwfQoSRowStatusEntry = _FrAtmDlciNiwfQoSRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 1, 1)
)
frAtmDlciNiwfQoSRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfQoSIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSRowStatusEntry.setStatus("mandatory")
_FrAtmDlciNiwfQoSRowStatus_Type = RowStatus
_FrAtmDlciNiwfQoSRowStatus_Object = MibTableColumn
frAtmDlciNiwfQoSRowStatus = _FrAtmDlciNiwfQoSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 1, 1, 1),
    _FrAtmDlciNiwfQoSRowStatus_Type()
)
frAtmDlciNiwfQoSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSRowStatus.setStatus("mandatory")
_FrAtmDlciNiwfQoSComponentName_Type = DisplayString
_FrAtmDlciNiwfQoSComponentName_Object = MibTableColumn
frAtmDlciNiwfQoSComponentName = _FrAtmDlciNiwfQoSComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 1, 1, 2),
    _FrAtmDlciNiwfQoSComponentName_Type()
)
frAtmDlciNiwfQoSComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSComponentName.setStatus("mandatory")
_FrAtmDlciNiwfQoSStorageType_Type = StorageType
_FrAtmDlciNiwfQoSStorageType_Object = MibTableColumn
frAtmDlciNiwfQoSStorageType = _FrAtmDlciNiwfQoSStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 1, 1, 4),
    _FrAtmDlciNiwfQoSStorageType_Type()
)
frAtmDlciNiwfQoSStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSStorageType.setStatus("mandatory")
_FrAtmDlciNiwfQoSIndex_Type = NonReplicated
_FrAtmDlciNiwfQoSIndex_Object = MibTableColumn
frAtmDlciNiwfQoSIndex = _FrAtmDlciNiwfQoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 1, 1, 10),
    _FrAtmDlciNiwfQoSIndex_Type()
)
frAtmDlciNiwfQoSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSIndex.setStatus("mandatory")
_FrAtmDlciNiwfQoSProvTable_Object = MibTable
frAtmDlciNiwfQoSProvTable = _FrAtmDlciNiwfQoSProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSProvTable.setStatus("mandatory")
_FrAtmDlciNiwfQoSProvEntry_Object = MibTableRow
frAtmDlciNiwfQoSProvEntry = _FrAtmDlciNiwfQoSProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 10, 1)
)
frAtmDlciNiwfQoSProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfQoSIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSProvEntry.setStatus("mandatory")


class _FrAtmDlciNiwfQoSEmissionPriorityToIf_Type(Integer32):
    """Custom type frAtmDlciNiwfQoSEmissionPriorityToIf based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromTp", 254),
          ("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("sameAsInterface", 255))
    )


_FrAtmDlciNiwfQoSEmissionPriorityToIf_Type.__name__ = "Integer32"
_FrAtmDlciNiwfQoSEmissionPriorityToIf_Object = MibTableColumn
frAtmDlciNiwfQoSEmissionPriorityToIf = _FrAtmDlciNiwfQoSEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 10, 1, 1),
    _FrAtmDlciNiwfQoSEmissionPriorityToIf_Type()
)
frAtmDlciNiwfQoSEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSEmissionPriorityToIf.setStatus("mandatory")


class _FrAtmDlciNiwfQoSTransferPriority_Type(Integer32):
    """Custom type frAtmDlciNiwfQoSTransferPriority based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("sameAsInterface", 255))
    )


_FrAtmDlciNiwfQoSTransferPriority_Type.__name__ = "Integer32"
_FrAtmDlciNiwfQoSTransferPriority_Object = MibTableColumn
frAtmDlciNiwfQoSTransferPriority = _FrAtmDlciNiwfQoSTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 4, 10, 1, 2),
    _FrAtmDlciNiwfQoSTransferPriority_Type()
)
frAtmDlciNiwfQoSTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciNiwfQoSTransferPriority.setStatus("mandatory")
_FrAtmDlciNiwfOperTable_Object = MibTable
frAtmDlciNiwfOperTable = _FrAtmDlciNiwfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfOperTable.setStatus("mandatory")
_FrAtmDlciNiwfOperEntry_Object = MibTableRow
frAtmDlciNiwfOperEntry = _FrAtmDlciNiwfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1)
)
frAtmDlciNiwfOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciNiwfIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciNiwfOperEntry.setStatus("mandatory")


class _FrAtmDlciNiwfDeToClpMapping_Type(Integer32):
    """Custom type frAtmDlciNiwfDeToClpMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_FrAtmDlciNiwfDeToClpMapping_Type.__name__ = "Integer32"
_FrAtmDlciNiwfDeToClpMapping_Object = MibTableColumn
frAtmDlciNiwfDeToClpMapping = _FrAtmDlciNiwfDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1, 1),
    _FrAtmDlciNiwfDeToClpMapping_Type()
)
frAtmDlciNiwfDeToClpMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfDeToClpMapping.setStatus("mandatory")


class _FrAtmDlciNiwfClpToDeMapping_Type(Integer32):
    """Custom type frAtmDlciNiwfClpToDeMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preserve", 2),
          ("transparent", 3))
    )


_FrAtmDlciNiwfClpToDeMapping_Type.__name__ = "Integer32"
_FrAtmDlciNiwfClpToDeMapping_Object = MibTableColumn
frAtmDlciNiwfClpToDeMapping = _FrAtmDlciNiwfClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1, 2),
    _FrAtmDlciNiwfClpToDeMapping_Type()
)
frAtmDlciNiwfClpToDeMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfClpToDeMapping.setStatus("mandatory")


class _FrAtmDlciNiwfTransferPriority_Type(Unsigned32):
    """Custom type frAtmDlciNiwfTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrAtmDlciNiwfTransferPriority_Type.__name__ = "Unsigned32"
_FrAtmDlciNiwfTransferPriority_Object = MibTableColumn
frAtmDlciNiwfTransferPriority = _FrAtmDlciNiwfTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1, 3),
    _FrAtmDlciNiwfTransferPriority_Type()
)
frAtmDlciNiwfTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfTransferPriority.setStatus("mandatory")


class _FrAtmDlciNiwfAtmServiceCategory_Type(Integer32):
    """Custom type frAtmDlciNiwfAtmServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("nrtVbr", 3),
          ("rtVbr", 2),
          ("scNotAvailable", 255),
          ("ubr", 0))
    )


_FrAtmDlciNiwfAtmServiceCategory_Type.__name__ = "Integer32"
_FrAtmDlciNiwfAtmServiceCategory_Object = MibTableColumn
frAtmDlciNiwfAtmServiceCategory = _FrAtmDlciNiwfAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1, 4),
    _FrAtmDlciNiwfAtmServiceCategory_Type()
)
frAtmDlciNiwfAtmServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfAtmServiceCategory.setStatus("mandatory")


class _FrAtmDlciNiwfTrafficParmConvPolicy_Type(Integer32):
    """Custom type frAtmDlciNiwfTrafficParmConvPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("policyNotAvailable", 0))
    )


_FrAtmDlciNiwfTrafficParmConvPolicy_Type.__name__ = "Integer32"
_FrAtmDlciNiwfTrafficParmConvPolicy_Object = MibTableColumn
frAtmDlciNiwfTrafficParmConvPolicy = _FrAtmDlciNiwfTrafficParmConvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1, 5),
    _FrAtmDlciNiwfTrafficParmConvPolicy_Type()
)
frAtmDlciNiwfTrafficParmConvPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfTrafficParmConvPolicy.setStatus("mandatory")


class _FrAtmDlciNiwfAvgFrameSize_Type(Integer32):
    """Custom type frAtmDlciNiwfAvgFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8187),
    )


_FrAtmDlciNiwfAvgFrameSize_Type.__name__ = "Integer32"
_FrAtmDlciNiwfAvgFrameSize_Object = MibTableColumn
frAtmDlciNiwfAvgFrameSize = _FrAtmDlciNiwfAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1, 6),
    _FrAtmDlciNiwfAvgFrameSize_Type()
)
frAtmDlciNiwfAvgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfAvgFrameSize.setStatus("mandatory")


class _FrAtmDlciNiwfEquivalentBitRate_Type(Unsigned32):
    """Custom type frAtmDlciNiwfEquivalentBitRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciNiwfEquivalentBitRate_Type.__name__ = "Unsigned32"
_FrAtmDlciNiwfEquivalentBitRate_Object = MibTableColumn
frAtmDlciNiwfEquivalentBitRate = _FrAtmDlciNiwfEquivalentBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1, 7),
    _FrAtmDlciNiwfEquivalentBitRate_Type()
)
frAtmDlciNiwfEquivalentBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfEquivalentBitRate.setStatus("mandatory")


class _FrAtmDlciNiwfAtmDlci_Type(AsciiString):
    """Custom type frAtmDlciNiwfAtmDlci based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FrAtmDlciNiwfAtmDlci_Type.__name__ = "AsciiString"
_FrAtmDlciNiwfAtmDlci_Object = MibTableColumn
frAtmDlciNiwfAtmDlci = _FrAtmDlciNiwfAtmDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1, 8),
    _FrAtmDlciNiwfAtmDlci_Type()
)
frAtmDlciNiwfAtmDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfAtmDlci.setStatus("mandatory")


class _FrAtmDlciNiwfAssignedBandwidthPool_Type(Integer32):
    """Custom type frAtmDlciNiwfAssignedBandwidthPool based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_FrAtmDlciNiwfAssignedBandwidthPool_Type.__name__ = "Integer32"
_FrAtmDlciNiwfAssignedBandwidthPool_Object = MibTableColumn
frAtmDlciNiwfAssignedBandwidthPool = _FrAtmDlciNiwfAssignedBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 4, 10, 1, 9),
    _FrAtmDlciNiwfAssignedBandwidthPool_Type()
)
frAtmDlciNiwfAssignedBandwidthPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciNiwfAssignedBandwidthPool.setStatus("mandatory")
_FrAtmDlciEgSp_ObjectIdentity = ObjectIdentity
frAtmDlciEgSp = _FrAtmDlciEgSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5)
)
_FrAtmDlciEgSpRowStatusTable_Object = MibTable
frAtmDlciEgSpRowStatusTable = _FrAtmDlciEgSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 1)
)
if mibBuilder.loadTexts:
    frAtmDlciEgSpRowStatusTable.setStatus("mandatory")
_FrAtmDlciEgSpRowStatusEntry_Object = MibTableRow
frAtmDlciEgSpRowStatusEntry = _FrAtmDlciEgSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 1, 1)
)
frAtmDlciEgSpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciEgSpIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciEgSpRowStatusEntry.setStatus("mandatory")
_FrAtmDlciEgSpRowStatus_Type = RowStatus
_FrAtmDlciEgSpRowStatus_Object = MibTableColumn
frAtmDlciEgSpRowStatus = _FrAtmDlciEgSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 1, 1, 1),
    _FrAtmDlciEgSpRowStatus_Type()
)
frAtmDlciEgSpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciEgSpRowStatus.setStatus("mandatory")
_FrAtmDlciEgSpComponentName_Type = DisplayString
_FrAtmDlciEgSpComponentName_Object = MibTableColumn
frAtmDlciEgSpComponentName = _FrAtmDlciEgSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 1, 1, 2),
    _FrAtmDlciEgSpComponentName_Type()
)
frAtmDlciEgSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciEgSpComponentName.setStatus("mandatory")
_FrAtmDlciEgSpStorageType_Type = StorageType
_FrAtmDlciEgSpStorageType_Object = MibTableColumn
frAtmDlciEgSpStorageType = _FrAtmDlciEgSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 1, 1, 4),
    _FrAtmDlciEgSpStorageType_Type()
)
frAtmDlciEgSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciEgSpStorageType.setStatus("mandatory")
_FrAtmDlciEgSpIndex_Type = NonReplicated
_FrAtmDlciEgSpIndex_Object = MibTableColumn
frAtmDlciEgSpIndex = _FrAtmDlciEgSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 1, 1, 10),
    _FrAtmDlciEgSpIndex_Type()
)
frAtmDlciEgSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmDlciEgSpIndex.setStatus("mandatory")
_FrAtmDlciEgSpProvTable_Object = MibTable
frAtmDlciEgSpProvTable = _FrAtmDlciEgSpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciEgSpProvTable.setStatus("mandatory")
_FrAtmDlciEgSpProvEntry_Object = MibTableRow
frAtmDlciEgSpProvEntry = _FrAtmDlciEgSpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 10, 1)
)
frAtmDlciEgSpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciEgSpIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciEgSpProvEntry.setStatus("mandatory")


class _FrAtmDlciEgSpCommittedInformationRate_Type(Unsigned32):
    """Custom type frAtmDlciEgSpCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrAtmDlciEgSpCommittedInformationRate_Type.__name__ = "Unsigned32"
_FrAtmDlciEgSpCommittedInformationRate_Object = MibTableColumn
frAtmDlciEgSpCommittedInformationRate = _FrAtmDlciEgSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 10, 1, 1),
    _FrAtmDlciEgSpCommittedInformationRate_Type()
)
frAtmDlciEgSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciEgSpCommittedInformationRate.setStatus("mandatory")


class _FrAtmDlciEgSpCommittedBurstSize_Type(Unsigned32):
    """Custom type frAtmDlciEgSpCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrAtmDlciEgSpCommittedBurstSize_Type.__name__ = "Unsigned32"
_FrAtmDlciEgSpCommittedBurstSize_Object = MibTableColumn
frAtmDlciEgSpCommittedBurstSize = _FrAtmDlciEgSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 10, 1, 2),
    _FrAtmDlciEgSpCommittedBurstSize_Type()
)
frAtmDlciEgSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciEgSpCommittedBurstSize.setStatus("mandatory")


class _FrAtmDlciEgSpExcessBurstSize_Type(Unsigned32):
    """Custom type frAtmDlciEgSpExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrAtmDlciEgSpExcessBurstSize_Type.__name__ = "Unsigned32"
_FrAtmDlciEgSpExcessBurstSize_Object = MibTableColumn
frAtmDlciEgSpExcessBurstSize = _FrAtmDlciEgSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 10, 1, 3),
    _FrAtmDlciEgSpExcessBurstSize_Type()
)
frAtmDlciEgSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciEgSpExcessBurstSize.setStatus("mandatory")


class _FrAtmDlciEgSpMeasurementInterval_Type(Unsigned32):
    """Custom type frAtmDlciEgSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_FrAtmDlciEgSpMeasurementInterval_Type.__name__ = "Unsigned32"
_FrAtmDlciEgSpMeasurementInterval_Object = MibTableColumn
frAtmDlciEgSpMeasurementInterval = _FrAtmDlciEgSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 5, 10, 1, 4),
    _FrAtmDlciEgSpMeasurementInterval_Type()
)
frAtmDlciEgSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmDlciEgSpMeasurementInterval.setStatus("mandatory")
_FrAtmDlciStateTable_Object = MibTable
frAtmDlciStateTable = _FrAtmDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 10)
)
if mibBuilder.loadTexts:
    frAtmDlciStateTable.setStatus("mandatory")
_FrAtmDlciStateEntry_Object = MibTableRow
frAtmDlciStateEntry = _FrAtmDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 10, 1)
)
frAtmDlciStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciStateEntry.setStatus("mandatory")


class _FrAtmDlciAdminState_Type(Integer32):
    """Custom type frAtmDlciAdminState based on Integer32"""
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


_FrAtmDlciAdminState_Type.__name__ = "Integer32"
_FrAtmDlciAdminState_Object = MibTableColumn
frAtmDlciAdminState = _FrAtmDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 10, 1, 1),
    _FrAtmDlciAdminState_Type()
)
frAtmDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciAdminState.setStatus("mandatory")


class _FrAtmDlciOperationalState_Type(Integer32):
    """Custom type frAtmDlciOperationalState based on Integer32"""
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


_FrAtmDlciOperationalState_Type.__name__ = "Integer32"
_FrAtmDlciOperationalState_Object = MibTableColumn
frAtmDlciOperationalState = _FrAtmDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 10, 1, 2),
    _FrAtmDlciOperationalState_Type()
)
frAtmDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciOperationalState.setStatus("mandatory")


class _FrAtmDlciUsageState_Type(Integer32):
    """Custom type frAtmDlciUsageState based on Integer32"""
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


_FrAtmDlciUsageState_Type.__name__ = "Integer32"
_FrAtmDlciUsageState_Object = MibTableColumn
frAtmDlciUsageState = _FrAtmDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 10, 1, 3),
    _FrAtmDlciUsageState_Type()
)
frAtmDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciUsageState.setStatus("mandatory")
_FrAtmDlciABitTable_Object = MibTable
frAtmDlciABitTable = _FrAtmDlciABitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 11)
)
if mibBuilder.loadTexts:
    frAtmDlciABitTable.setStatus("mandatory")
_FrAtmDlciABitEntry_Object = MibTableRow
frAtmDlciABitEntry = _FrAtmDlciABitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 11, 1)
)
frAtmDlciABitEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciABitEntry.setStatus("mandatory")


class _FrAtmDlciABitStatusToIf_Type(Integer32):
    """Custom type frAtmDlciABitStatusToIf based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_FrAtmDlciABitStatusToIf_Type.__name__ = "Integer32"
_FrAtmDlciABitStatusToIf_Object = MibTableColumn
frAtmDlciABitStatusToIf = _FrAtmDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 11, 1, 1),
    _FrAtmDlciABitStatusToIf_Type()
)
frAtmDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciABitStatusToIf.setStatus("mandatory")


class _FrAtmDlciABitReasonToIf_Type(Integer32):
    """Custom type frAtmDlciABitReasonToIf based on Integer32"""
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
        *(("localLinkDown", 4),
          ("localLmiError", 2),
          ("notApplicable", 0),
          ("pvcDown", 6),
          ("remoteLinkDown", 5),
          ("remoteLmiError", 3),
          ("remoteUserSignaled", 1))
    )


_FrAtmDlciABitReasonToIf_Type.__name__ = "Integer32"
_FrAtmDlciABitReasonToIf_Object = MibTableColumn
frAtmDlciABitReasonToIf = _FrAtmDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 11, 1, 2),
    _FrAtmDlciABitReasonToIf_Type()
)
frAtmDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciABitReasonToIf.setStatus("mandatory")


class _FrAtmDlciABitStatusFromIf_Type(Integer32):
    """Custom type frAtmDlciABitStatusFromIf based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_FrAtmDlciABitStatusFromIf_Type.__name__ = "Integer32"
_FrAtmDlciABitStatusFromIf_Object = MibTableColumn
frAtmDlciABitStatusFromIf = _FrAtmDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 11, 1, 3),
    _FrAtmDlciABitStatusFromIf_Type()
)
frAtmDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciABitStatusFromIf.setStatus("mandatory")


class _FrAtmDlciABitReasonFromIf_Type(Integer32):
    """Custom type frAtmDlciABitReasonFromIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localLinkDown", 4),
          ("localLmiError", 2),
          ("missingFromLmiReport", 7),
          ("notApplicable", 0),
          ("pvcDown", 6),
          ("remoteUserSignaled", 1))
    )


_FrAtmDlciABitReasonFromIf_Type.__name__ = "Integer32"
_FrAtmDlciABitReasonFromIf_Object = MibTableColumn
frAtmDlciABitReasonFromIf = _FrAtmDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 11, 1, 4),
    _FrAtmDlciABitReasonFromIf_Type()
)
frAtmDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciABitReasonFromIf.setStatus("mandatory")
_FrAtmDlciSpOpTable_Object = MibTable
frAtmDlciSpOpTable = _FrAtmDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12)
)
if mibBuilder.loadTexts:
    frAtmDlciSpOpTable.setStatus("mandatory")
_FrAtmDlciSpOpEntry_Object = MibTableRow
frAtmDlciSpOpEntry = _FrAtmDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1)
)
frAtmDlciSpOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciSpOpEntry.setStatus("mandatory")


class _FrAtmDlciMaximumFrameSize_Type(Unsigned32):
    """Custom type frAtmDlciMaximumFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_FrAtmDlciMaximumFrameSize_Type.__name__ = "Unsigned32"
_FrAtmDlciMaximumFrameSize_Object = MibTableColumn
frAtmDlciMaximumFrameSize = _FrAtmDlciMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 1),
    _FrAtmDlciMaximumFrameSize_Type()
)
frAtmDlciMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciMaximumFrameSize.setStatus("mandatory")


class _FrAtmDlciRateEnforcement_Type(Integer32):
    """Custom type frAtmDlciRateEnforcement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FrAtmDlciRateEnforcement_Type.__name__ = "Integer32"
_FrAtmDlciRateEnforcement_Object = MibTableColumn
frAtmDlciRateEnforcement = _FrAtmDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 2),
    _FrAtmDlciRateEnforcement_Type()
)
frAtmDlciRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciRateEnforcement.setStatus("mandatory")


class _FrAtmDlciCommittedInformationRate_Type(Unsigned32):
    """Custom type frAtmDlciCommittedInformationRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrAtmDlciCommittedInformationRate_Type.__name__ = "Unsigned32"
_FrAtmDlciCommittedInformationRate_Object = MibTableColumn
frAtmDlciCommittedInformationRate = _FrAtmDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 3),
    _FrAtmDlciCommittedInformationRate_Type()
)
frAtmDlciCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciCommittedInformationRate.setStatus("mandatory")


class _FrAtmDlciCommittedBurstSize_Type(Unsigned32):
    """Custom type frAtmDlciCommittedBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrAtmDlciCommittedBurstSize_Type.__name__ = "Unsigned32"
_FrAtmDlciCommittedBurstSize_Object = MibTableColumn
frAtmDlciCommittedBurstSize = _FrAtmDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 4),
    _FrAtmDlciCommittedBurstSize_Type()
)
frAtmDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciCommittedBurstSize.setStatus("mandatory")


class _FrAtmDlciExcessBurstSize_Type(Unsigned32):
    """Custom type frAtmDlciExcessBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrAtmDlciExcessBurstSize_Type.__name__ = "Unsigned32"
_FrAtmDlciExcessBurstSize_Object = MibTableColumn
frAtmDlciExcessBurstSize = _FrAtmDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 5),
    _FrAtmDlciExcessBurstSize_Type()
)
frAtmDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciExcessBurstSize.setStatus("mandatory")


class _FrAtmDlciMeasurementInterval_Type(Unsigned32):
    """Custom type frAtmDlciMeasurementInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciMeasurementInterval_Type.__name__ = "Unsigned32"
_FrAtmDlciMeasurementInterval_Object = MibTableColumn
frAtmDlciMeasurementInterval = _FrAtmDlciMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 6),
    _FrAtmDlciMeasurementInterval_Type()
)
frAtmDlciMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciMeasurementInterval.setStatus("mandatory")


class _FrAtmDlciEmissionPriorityToIf_Type(Integer32):
    """Custom type frAtmDlciEmissionPriorityToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_FrAtmDlciEmissionPriorityToIf_Type.__name__ = "Integer32"
_FrAtmDlciEmissionPriorityToIf_Object = MibTableColumn
frAtmDlciEmissionPriorityToIf = _FrAtmDlciEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 7),
    _FrAtmDlciEmissionPriorityToIf_Type()
)
frAtmDlciEmissionPriorityToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciEmissionPriorityToIf.setStatus("mandatory")


class _FrAtmDlciDlciType_Type(Integer32):
    """Custom type frAtmDlciDlciType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("networkInterworking", 1),
          ("serviceInterworking", 0))
    )


_FrAtmDlciDlciType_Type.__name__ = "Integer32"
_FrAtmDlciDlciType_Object = MibTableColumn
frAtmDlciDlciType = _FrAtmDlciDlciType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 8),
    _FrAtmDlciDlciType_Type()
)
frAtmDlciDlciType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDlciType.setStatus("mandatory")


class _FrAtmDlciTroubled_Type(Integer32):
    """Custom type frAtmDlciTroubled based on Integer32"""
    defaultValue = 0

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


_FrAtmDlciTroubled_Type.__name__ = "Integer32"
_FrAtmDlciTroubled_Object = MibTableColumn
frAtmDlciTroubled = _FrAtmDlciTroubled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 9),
    _FrAtmDlciTroubled_Type()
)
frAtmDlciTroubled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciTroubled.setStatus("mandatory")


class _FrAtmDlciTroubledReason_Type(Integer32):
    """Custom type frAtmDlciTroubledReason based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAdmitted", 1),
          ("notApplicable", 0))
    )


_FrAtmDlciTroubledReason_Type.__name__ = "Integer32"
_FrAtmDlciTroubledReason_Object = MibTableColumn
frAtmDlciTroubledReason = _FrAtmDlciTroubledReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 12, 1, 10),
    _FrAtmDlciTroubledReason_Type()
)
frAtmDlciTroubledReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciTroubledReason.setStatus("mandatory")
_FrAtmDlciStatsTable_Object = MibTable
frAtmDlciStatsTable = _FrAtmDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13)
)
if mibBuilder.loadTexts:
    frAtmDlciStatsTable.setStatus("mandatory")
_FrAtmDlciStatsEntry_Object = MibTableRow
frAtmDlciStatsEntry = _FrAtmDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1)
)
frAtmDlciStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciStatsEntry.setStatus("mandatory")
_FrAtmDlciFrmToIf_Type = Counter32
_FrAtmDlciFrmToIf_Object = MibTableColumn
frAtmDlciFrmToIf = _FrAtmDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 1),
    _FrAtmDlciFrmToIf_Type()
)
frAtmDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciFrmToIf.setStatus("mandatory")
_FrAtmDlciFecnFrmToIf_Type = Counter32
_FrAtmDlciFecnFrmToIf_Object = MibTableColumn
frAtmDlciFecnFrmToIf = _FrAtmDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 2),
    _FrAtmDlciFecnFrmToIf_Type()
)
frAtmDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciFecnFrmToIf.setStatus("mandatory")
_FrAtmDlciBecnFrmToIf_Type = Counter32
_FrAtmDlciBecnFrmToIf_Object = MibTableColumn
frAtmDlciBecnFrmToIf = _FrAtmDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 3),
    _FrAtmDlciBecnFrmToIf_Type()
)
frAtmDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciBecnFrmToIf.setStatus("mandatory")
_FrAtmDlciDeFrmToIf_Type = Counter32
_FrAtmDlciDeFrmToIf_Object = MibTableColumn
frAtmDlciDeFrmToIf = _FrAtmDlciDeFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 4),
    _FrAtmDlciDeFrmToIf_Type()
)
frAtmDlciDeFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDeFrmToIf.setStatus("mandatory")
_FrAtmDlciDiscCongestedToIf_Type = Counter32
_FrAtmDlciDiscCongestedToIf_Object = MibTableColumn
frAtmDlciDiscCongestedToIf = _FrAtmDlciDiscCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 5),
    _FrAtmDlciDiscCongestedToIf_Type()
)
frAtmDlciDiscCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscCongestedToIf.setStatus("mandatory")
_FrAtmDlciDiscDeCongestedToIf_Type = Counter32
_FrAtmDlciDiscDeCongestedToIf_Object = MibTableColumn
frAtmDlciDiscDeCongestedToIf = _FrAtmDlciDiscDeCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 6),
    _FrAtmDlciDiscDeCongestedToIf_Type()
)
frAtmDlciDiscDeCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscDeCongestedToIf.setStatus("mandatory")
_FrAtmDlciFrmFromIf_Type = Counter32
_FrAtmDlciFrmFromIf_Object = MibTableColumn
frAtmDlciFrmFromIf = _FrAtmDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 7),
    _FrAtmDlciFrmFromIf_Type()
)
frAtmDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciFrmFromIf.setStatus("mandatory")
_FrAtmDlciFecnFrmFromIf_Type = Counter32
_FrAtmDlciFecnFrmFromIf_Object = MibTableColumn
frAtmDlciFecnFrmFromIf = _FrAtmDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 8),
    _FrAtmDlciFecnFrmFromIf_Type()
)
frAtmDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciFecnFrmFromIf.setStatus("mandatory")
_FrAtmDlciBecnFrmFromIf_Type = Counter32
_FrAtmDlciBecnFrmFromIf_Object = MibTableColumn
frAtmDlciBecnFrmFromIf = _FrAtmDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 9),
    _FrAtmDlciBecnFrmFromIf_Type()
)
frAtmDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciBecnFrmFromIf.setStatus("mandatory")
_FrAtmDlciEfciFrmFromNetwork_Type = Counter32
_FrAtmDlciEfciFrmFromNetwork_Object = MibTableColumn
frAtmDlciEfciFrmFromNetwork = _FrAtmDlciEfciFrmFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 10),
    _FrAtmDlciEfciFrmFromNetwork_Type()
)
frAtmDlciEfciFrmFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciEfciFrmFromNetwork.setStatus("mandatory")
_FrAtmDlciDeFrmFromIf_Type = Counter32
_FrAtmDlciDeFrmFromIf_Object = MibTableColumn
frAtmDlciDeFrmFromIf = _FrAtmDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 11),
    _FrAtmDlciDeFrmFromIf_Type()
)
frAtmDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDeFrmFromIf.setStatus("mandatory")
_FrAtmDlciExcessFrmFromIf_Type = Counter32
_FrAtmDlciExcessFrmFromIf_Object = MibTableColumn
frAtmDlciExcessFrmFromIf = _FrAtmDlciExcessFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 12),
    _FrAtmDlciExcessFrmFromIf_Type()
)
frAtmDlciExcessFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciExcessFrmFromIf.setStatus("mandatory")
_FrAtmDlciDiscExcessFromIf_Type = Counter32
_FrAtmDlciDiscExcessFromIf_Object = MibTableColumn
frAtmDlciDiscExcessFromIf = _FrAtmDlciDiscExcessFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 13),
    _FrAtmDlciDiscExcessFromIf_Type()
)
frAtmDlciDiscExcessFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscExcessFromIf.setStatus("mandatory")
_FrAtmDlciDiscFrameAbit_Type = Counter32
_FrAtmDlciDiscFrameAbit_Object = MibTableColumn
frAtmDlciDiscFrameAbit = _FrAtmDlciDiscFrameAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 14),
    _FrAtmDlciDiscFrameAbit_Type()
)
frAtmDlciDiscFrameAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscFrameAbit.setStatus("mandatory")
_FrAtmDlciDiscCongestedFromIf_Type = Counter32
_FrAtmDlciDiscCongestedFromIf_Object = MibTableColumn
frAtmDlciDiscCongestedFromIf = _FrAtmDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 15),
    _FrAtmDlciDiscCongestedFromIf_Type()
)
frAtmDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscCongestedFromIf.setStatus("mandatory")
_FrAtmDlciDiscDeCongestedFromIf_Type = Counter32
_FrAtmDlciDiscDeCongestedFromIf_Object = MibTableColumn
frAtmDlciDiscDeCongestedFromIf = _FrAtmDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 16),
    _FrAtmDlciDiscDeCongestedFromIf_Type()
)
frAtmDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscDeCongestedFromIf.setStatus("mandatory")
_FrAtmDlciErrorShortFrmFromIf_Type = Counter32
_FrAtmDlciErrorShortFrmFromIf_Object = MibTableColumn
frAtmDlciErrorShortFrmFromIf = _FrAtmDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 17),
    _FrAtmDlciErrorShortFrmFromIf_Type()
)
frAtmDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciErrorShortFrmFromIf.setStatus("mandatory")
_FrAtmDlciErrorLongFrmFromIf_Type = Counter32
_FrAtmDlciErrorLongFrmFromIf_Object = MibTableColumn
frAtmDlciErrorLongFrmFromIf = _FrAtmDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 18),
    _FrAtmDlciErrorLongFrmFromIf_Type()
)
frAtmDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciErrorLongFrmFromIf.setStatus("mandatory")
_FrAtmDlciBecnFrmSetByService_Type = Counter32
_FrAtmDlciBecnFrmSetByService_Object = MibTableColumn
frAtmDlciBecnFrmSetByService = _FrAtmDlciBecnFrmSetByService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 19),
    _FrAtmDlciBecnFrmSetByService_Type()
)
frAtmDlciBecnFrmSetByService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciBecnFrmSetByService.setStatus("mandatory")
_FrAtmDlciBytesToIf_Type = Counter32
_FrAtmDlciBytesToIf_Object = MibTableColumn
frAtmDlciBytesToIf = _FrAtmDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 20),
    _FrAtmDlciBytesToIf_Type()
)
frAtmDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciBytesToIf.setStatus("mandatory")
_FrAtmDlciDeBytesToIf_Type = Counter32
_FrAtmDlciDeBytesToIf_Object = MibTableColumn
frAtmDlciDeBytesToIf = _FrAtmDlciDeBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 21),
    _FrAtmDlciDeBytesToIf_Type()
)
frAtmDlciDeBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDeBytesToIf.setStatus("mandatory")
_FrAtmDlciDiscCongestedToIfBytes_Type = Counter32
_FrAtmDlciDiscCongestedToIfBytes_Object = MibTableColumn
frAtmDlciDiscCongestedToIfBytes = _FrAtmDlciDiscCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 22),
    _FrAtmDlciDiscCongestedToIfBytes_Type()
)
frAtmDlciDiscCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscCongestedToIfBytes.setStatus("mandatory")
_FrAtmDlciDiscDeCongestedToIfBytes_Type = Counter32
_FrAtmDlciDiscDeCongestedToIfBytes_Object = MibTableColumn
frAtmDlciDiscDeCongestedToIfBytes = _FrAtmDlciDiscDeCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 23),
    _FrAtmDlciDiscDeCongestedToIfBytes_Type()
)
frAtmDlciDiscDeCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscDeCongestedToIfBytes.setStatus("mandatory")
_FrAtmDlciBytesFromIf_Type = Counter32
_FrAtmDlciBytesFromIf_Object = MibTableColumn
frAtmDlciBytesFromIf = _FrAtmDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 24),
    _FrAtmDlciBytesFromIf_Type()
)
frAtmDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciBytesFromIf.setStatus("mandatory")
_FrAtmDlciDeBytesFromIf_Type = Counter32
_FrAtmDlciDeBytesFromIf_Object = MibTableColumn
frAtmDlciDeBytesFromIf = _FrAtmDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 25),
    _FrAtmDlciDeBytesFromIf_Type()
)
frAtmDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDeBytesFromIf.setStatus("mandatory")
_FrAtmDlciExcessBytesFromIf_Type = Counter32
_FrAtmDlciExcessBytesFromIf_Object = MibTableColumn
frAtmDlciExcessBytesFromIf = _FrAtmDlciExcessBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 26),
    _FrAtmDlciExcessBytesFromIf_Type()
)
frAtmDlciExcessBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciExcessBytesFromIf.setStatus("mandatory")
_FrAtmDlciDiscExcessFromIfBytes_Type = Counter32
_FrAtmDlciDiscExcessFromIfBytes_Object = MibTableColumn
frAtmDlciDiscExcessFromIfBytes = _FrAtmDlciDiscExcessFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 27),
    _FrAtmDlciDiscExcessFromIfBytes_Type()
)
frAtmDlciDiscExcessFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscExcessFromIfBytes.setStatus("mandatory")
_FrAtmDlciDiscByteAbit_Type = Counter32
_FrAtmDlciDiscByteAbit_Object = MibTableColumn
frAtmDlciDiscByteAbit = _FrAtmDlciDiscByteAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 28),
    _FrAtmDlciDiscByteAbit_Type()
)
frAtmDlciDiscByteAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscByteAbit.setStatus("mandatory")
_FrAtmDlciDiscCongestedFromIfBytes_Type = Counter32
_FrAtmDlciDiscCongestedFromIfBytes_Object = MibTableColumn
frAtmDlciDiscCongestedFromIfBytes = _FrAtmDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 29),
    _FrAtmDlciDiscCongestedFromIfBytes_Type()
)
frAtmDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscCongestedFromIfBytes.setStatus("mandatory")
_FrAtmDlciDiscDeCongestedFromIfBytes_Type = Counter32
_FrAtmDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
frAtmDlciDiscDeCongestedFromIfBytes = _FrAtmDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 30),
    _FrAtmDlciDiscDeCongestedFromIfBytes_Type()
)
frAtmDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")
_FrAtmDlciErrorShortBytesFromIf_Type = Counter32
_FrAtmDlciErrorShortBytesFromIf_Object = MibTableColumn
frAtmDlciErrorShortBytesFromIf = _FrAtmDlciErrorShortBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 31),
    _FrAtmDlciErrorShortBytesFromIf_Type()
)
frAtmDlciErrorShortBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciErrorShortBytesFromIf.setStatus("mandatory")
_FrAtmDlciErrorLongBytesFromIf_Type = Counter32
_FrAtmDlciErrorLongBytesFromIf_Object = MibTableColumn
frAtmDlciErrorLongBytesFromIf = _FrAtmDlciErrorLongBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 13, 1, 32),
    _FrAtmDlciErrorLongBytesFromIf_Type()
)
frAtmDlciErrorLongBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciErrorLongBytesFromIf.setStatus("mandatory")
_FrAtmDlciCalldTable_Object = MibTable
frAtmDlciCalldTable = _FrAtmDlciCalldTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 14)
)
if mibBuilder.loadTexts:
    frAtmDlciCalldTable.setStatus("mandatory")
_FrAtmDlciCalldEntry_Object = MibTableRow
frAtmDlciCalldEntry = _FrAtmDlciCalldEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 14, 1)
)
frAtmDlciCalldEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciCalldEntry.setStatus("mandatory")


class _FrAtmDlciAccountingEnabled_Type(Integer32):
    """Custom type frAtmDlciAccountingEnabled based on Integer32"""
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


_FrAtmDlciAccountingEnabled_Type.__name__ = "Integer32"
_FrAtmDlciAccountingEnabled_Object = MibTableColumn
frAtmDlciAccountingEnabled = _FrAtmDlciAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 14, 1, 1),
    _FrAtmDlciAccountingEnabled_Type()
)
frAtmDlciAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciAccountingEnabled.setStatus("mandatory")


class _FrAtmDlciAccountingEnd_Type(Integer32):
    """Custom type frAtmDlciAccountingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calledEnd", 1),
          ("callingEnd", 0))
    )


_FrAtmDlciAccountingEnd_Type.__name__ = "Integer32"
_FrAtmDlciAccountingEnd_Object = MibTableColumn
frAtmDlciAccountingEnd = _FrAtmDlciAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 14, 1, 2),
    _FrAtmDlciAccountingEnd_Type()
)
frAtmDlciAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciAccountingEnd.setStatus("mandatory")


class _FrAtmDlciCorrelationTag_Type(HexString):
    """Custom type frAtmDlciCorrelationTag based on HexString"""
    defaultHexValue = ""

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_FrAtmDlciCorrelationTag_Type.__name__ = "HexString"
_FrAtmDlciCorrelationTag_Object = MibTableColumn
frAtmDlciCorrelationTag = _FrAtmDlciCorrelationTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 14, 1, 3),
    _FrAtmDlciCorrelationTag_Type()
)
frAtmDlciCorrelationTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciCorrelationTag.setStatus("mandatory")
_FrAtmDlciIntTable_Object = MibTable
frAtmDlciIntTable = _FrAtmDlciIntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15)
)
if mibBuilder.loadTexts:
    frAtmDlciIntTable.setStatus("mandatory")
_FrAtmDlciIntEntry_Object = MibTableRow
frAtmDlciIntEntry = _FrAtmDlciIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1)
)
frAtmDlciIntEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmDlciIndex"),
)
if mibBuilder.loadTexts:
    frAtmDlciIntEntry.setStatus("mandatory")


class _FrAtmDlciStartTime_Type(EnterpriseDateAndTime):
    """Custom type frAtmDlciStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_FrAtmDlciStartTime_Type.__name__ = "EnterpriseDateAndTime"
_FrAtmDlciStartTime_Object = MibTableColumn
frAtmDlciStartTime = _FrAtmDlciStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 1),
    _FrAtmDlciStartTime_Type()
)
frAtmDlciStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciStartTime.setStatus("mandatory")


class _FrAtmDlciTotalIngressBytes_Type(Unsigned64):
    """Custom type frAtmDlciTotalIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrAtmDlciTotalIngressBytes_Type.__name__ = "Unsigned64"
_FrAtmDlciTotalIngressBytes_Object = MibTableColumn
frAtmDlciTotalIngressBytes = _FrAtmDlciTotalIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 2),
    _FrAtmDlciTotalIngressBytes_Type()
)
frAtmDlciTotalIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciTotalIngressBytes.setStatus("mandatory")


class _FrAtmDlciTotalEgressBytes_Type(Unsigned64):
    """Custom type frAtmDlciTotalEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrAtmDlciTotalEgressBytes_Type.__name__ = "Unsigned64"
_FrAtmDlciTotalEgressBytes_Object = MibTableColumn
frAtmDlciTotalEgressBytes = _FrAtmDlciTotalEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 3),
    _FrAtmDlciTotalEgressBytes_Type()
)
frAtmDlciTotalEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciTotalEgressBytes.setStatus("mandatory")


class _FrAtmDlciEirIngressBytes_Type(Unsigned64):
    """Custom type frAtmDlciEirIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrAtmDlciEirIngressBytes_Type.__name__ = "Unsigned64"
_FrAtmDlciEirIngressBytes_Object = MibTableColumn
frAtmDlciEirIngressBytes = _FrAtmDlciEirIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 4),
    _FrAtmDlciEirIngressBytes_Type()
)
frAtmDlciEirIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciEirIngressBytes.setStatus("mandatory")


class _FrAtmDlciEirEgressBytes_Type(Unsigned64):
    """Custom type frAtmDlciEirEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrAtmDlciEirEgressBytes_Type.__name__ = "Unsigned64"
_FrAtmDlciEirEgressBytes_Object = MibTableColumn
frAtmDlciEirEgressBytes = _FrAtmDlciEirEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 5),
    _FrAtmDlciEirEgressBytes_Type()
)
frAtmDlciEirEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciEirEgressBytes.setStatus("mandatory")


class _FrAtmDlciDiscardedBytes_Type(Unsigned64):
    """Custom type frAtmDlciDiscardedBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrAtmDlciDiscardedBytes_Type.__name__ = "Unsigned64"
_FrAtmDlciDiscardedBytes_Object = MibTableColumn
frAtmDlciDiscardedBytes = _FrAtmDlciDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 6),
    _FrAtmDlciDiscardedBytes_Type()
)
frAtmDlciDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscardedBytes.setStatus("mandatory")


class _FrAtmDlciTotalIngressFrames_Type(Unsigned32):
    """Custom type frAtmDlciTotalIngressFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciTotalIngressFrames_Type.__name__ = "Unsigned32"
_FrAtmDlciTotalIngressFrames_Object = MibTableColumn
frAtmDlciTotalIngressFrames = _FrAtmDlciTotalIngressFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 7),
    _FrAtmDlciTotalIngressFrames_Type()
)
frAtmDlciTotalIngressFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciTotalIngressFrames.setStatus("mandatory")


class _FrAtmDlciTotalEgressFrames_Type(Unsigned32):
    """Custom type frAtmDlciTotalEgressFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciTotalEgressFrames_Type.__name__ = "Unsigned32"
_FrAtmDlciTotalEgressFrames_Object = MibTableColumn
frAtmDlciTotalEgressFrames = _FrAtmDlciTotalEgressFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 8),
    _FrAtmDlciTotalEgressFrames_Type()
)
frAtmDlciTotalEgressFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciTotalEgressFrames.setStatus("mandatory")


class _FrAtmDlciEirIngressFrames_Type(Unsigned32):
    """Custom type frAtmDlciEirIngressFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciEirIngressFrames_Type.__name__ = "Unsigned32"
_FrAtmDlciEirIngressFrames_Object = MibTableColumn
frAtmDlciEirIngressFrames = _FrAtmDlciEirIngressFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 9),
    _FrAtmDlciEirIngressFrames_Type()
)
frAtmDlciEirIngressFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciEirIngressFrames.setStatus("mandatory")


class _FrAtmDlciEirEgressFrames_Type(Unsigned32):
    """Custom type frAtmDlciEirEgressFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciEirEgressFrames_Type.__name__ = "Unsigned32"
_FrAtmDlciEirEgressFrames_Object = MibTableColumn
frAtmDlciEirEgressFrames = _FrAtmDlciEirEgressFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 10),
    _FrAtmDlciEirEgressFrames_Type()
)
frAtmDlciEirEgressFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciEirEgressFrames.setStatus("mandatory")


class _FrAtmDlciDiscardedFrames_Type(Unsigned32):
    """Custom type frAtmDlciDiscardedFrames based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciDiscardedFrames_Type.__name__ = "Unsigned32"
_FrAtmDlciDiscardedFrames_Object = MibTableColumn
frAtmDlciDiscardedFrames = _FrAtmDlciDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 11),
    _FrAtmDlciDiscardedFrames_Type()
)
frAtmDlciDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciDiscardedFrames.setStatus("mandatory")


class _FrAtmDlciElapsedDifference_Type(Unsigned32):
    """Custom type frAtmDlciElapsedDifference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmDlciElapsedDifference_Type.__name__ = "Unsigned32"
_FrAtmDlciElapsedDifference_Object = MibTableColumn
frAtmDlciElapsedDifference = _FrAtmDlciElapsedDifference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 4, 15, 1, 12),
    _FrAtmDlciElapsedDifference_Type()
)
frAtmDlciElapsedDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmDlciElapsedDifference.setStatus("mandatory")
_FrAtmVFramer_ObjectIdentity = ObjectIdentity
frAtmVFramer = _FrAtmVFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5)
)
_FrAtmVFramerRowStatusTable_Object = MibTable
frAtmVFramerRowStatusTable = _FrAtmVFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 1)
)
if mibBuilder.loadTexts:
    frAtmVFramerRowStatusTable.setStatus("mandatory")
_FrAtmVFramerRowStatusEntry_Object = MibTableRow
frAtmVFramerRowStatusEntry = _FrAtmVFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 1, 1)
)
frAtmVFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmVFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmVFramerRowStatusEntry.setStatus("mandatory")
_FrAtmVFramerRowStatus_Type = RowStatus
_FrAtmVFramerRowStatus_Object = MibTableColumn
frAtmVFramerRowStatus = _FrAtmVFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 1, 1, 1),
    _FrAtmVFramerRowStatus_Type()
)
frAtmVFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmVFramerRowStatus.setStatus("mandatory")
_FrAtmVFramerComponentName_Type = DisplayString
_FrAtmVFramerComponentName_Object = MibTableColumn
frAtmVFramerComponentName = _FrAtmVFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 1, 1, 2),
    _FrAtmVFramerComponentName_Type()
)
frAtmVFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmVFramerComponentName.setStatus("mandatory")
_FrAtmVFramerStorageType_Type = StorageType
_FrAtmVFramerStorageType_Object = MibTableColumn
frAtmVFramerStorageType = _FrAtmVFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 1, 1, 4),
    _FrAtmVFramerStorageType_Type()
)
frAtmVFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmVFramerStorageType.setStatus("mandatory")
_FrAtmVFramerIndex_Type = NonReplicated
_FrAtmVFramerIndex_Object = MibTableColumn
frAtmVFramerIndex = _FrAtmVFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 1, 1, 10),
    _FrAtmVFramerIndex_Type()
)
frAtmVFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmVFramerIndex.setStatus("mandatory")
_FrAtmVFramerProvTable_Object = MibTable
frAtmVFramerProvTable = _FrAtmVFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 10)
)
if mibBuilder.loadTexts:
    frAtmVFramerProvTable.setStatus("mandatory")
_FrAtmVFramerProvEntry_Object = MibTableRow
frAtmVFramerProvEntry = _FrAtmVFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 10, 1)
)
frAtmVFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmVFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmVFramerProvEntry.setStatus("mandatory")
_FrAtmVFramerOtherVirtualFramer_Type = Link
_FrAtmVFramerOtherVirtualFramer_Object = MibTableColumn
frAtmVFramerOtherVirtualFramer = _FrAtmVFramerOtherVirtualFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 10, 1, 1),
    _FrAtmVFramerOtherVirtualFramer_Type()
)
frAtmVFramerOtherVirtualFramer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmVFramerOtherVirtualFramer.setStatus("mandatory")
_FrAtmVFramerLogicalProcessor_Type = Link
_FrAtmVFramerLogicalProcessor_Object = MibTableColumn
frAtmVFramerLogicalProcessor = _FrAtmVFramerLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 10, 1, 2),
    _FrAtmVFramerLogicalProcessor_Type()
)
frAtmVFramerLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmVFramerLogicalProcessor.setStatus("mandatory")
_FrAtmVFramerStateTable_Object = MibTable
frAtmVFramerStateTable = _FrAtmVFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 11)
)
if mibBuilder.loadTexts:
    frAtmVFramerStateTable.setStatus("mandatory")
_FrAtmVFramerStateEntry_Object = MibTableRow
frAtmVFramerStateEntry = _FrAtmVFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 11, 1)
)
frAtmVFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmVFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmVFramerStateEntry.setStatus("mandatory")


class _FrAtmVFramerAdminState_Type(Integer32):
    """Custom type frAtmVFramerAdminState based on Integer32"""
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


_FrAtmVFramerAdminState_Type.__name__ = "Integer32"
_FrAtmVFramerAdminState_Object = MibTableColumn
frAtmVFramerAdminState = _FrAtmVFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 11, 1, 1),
    _FrAtmVFramerAdminState_Type()
)
frAtmVFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmVFramerAdminState.setStatus("mandatory")


class _FrAtmVFramerOperationalState_Type(Integer32):
    """Custom type frAtmVFramerOperationalState based on Integer32"""
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


_FrAtmVFramerOperationalState_Type.__name__ = "Integer32"
_FrAtmVFramerOperationalState_Object = MibTableColumn
frAtmVFramerOperationalState = _FrAtmVFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 11, 1, 2),
    _FrAtmVFramerOperationalState_Type()
)
frAtmVFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmVFramerOperationalState.setStatus("mandatory")


class _FrAtmVFramerUsageState_Type(Integer32):
    """Custom type frAtmVFramerUsageState based on Integer32"""
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


_FrAtmVFramerUsageState_Type.__name__ = "Integer32"
_FrAtmVFramerUsageState_Object = MibTableColumn
frAtmVFramerUsageState = _FrAtmVFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 11, 1, 3),
    _FrAtmVFramerUsageState_Type()
)
frAtmVFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmVFramerUsageState.setStatus("mandatory")
_FrAtmVFramerStatsTable_Object = MibTable
frAtmVFramerStatsTable = _FrAtmVFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 12)
)
if mibBuilder.loadTexts:
    frAtmVFramerStatsTable.setStatus("mandatory")
_FrAtmVFramerStatsEntry_Object = MibTableRow
frAtmVFramerStatsEntry = _FrAtmVFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 12, 1)
)
frAtmVFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmVFramerIndex"),
)
if mibBuilder.loadTexts:
    frAtmVFramerStatsEntry.setStatus("mandatory")
_FrAtmVFramerFrmToOtherVFramer_Type = PassportCounter64
_FrAtmVFramerFrmToOtherVFramer_Object = MibTableColumn
frAtmVFramerFrmToOtherVFramer = _FrAtmVFramerFrmToOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 12, 1, 2),
    _FrAtmVFramerFrmToOtherVFramer_Type()
)
frAtmVFramerFrmToOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmVFramerFrmToOtherVFramer.setStatus("mandatory")
_FrAtmVFramerFrmFromOtherVFramer_Type = PassportCounter64
_FrAtmVFramerFrmFromOtherVFramer_Object = MibTableColumn
frAtmVFramerFrmFromOtherVFramer = _FrAtmVFramerFrmFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 12, 1, 3),
    _FrAtmVFramerFrmFromOtherVFramer_Type()
)
frAtmVFramerFrmFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmVFramerFrmFromOtherVFramer.setStatus("mandatory")
_FrAtmVFramerOctetFromOtherVFramer_Type = PassportCounter64
_FrAtmVFramerOctetFromOtherVFramer_Object = MibTableColumn
frAtmVFramerOctetFromOtherVFramer = _FrAtmVFramerOctetFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 5, 12, 1, 5),
    _FrAtmVFramerOctetFromOtherVFramer_Type()
)
frAtmVFramerOctetFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmVFramerOctetFromOtherVFramer.setStatus("mandatory")
_FrAtmAddr_ObjectIdentity = ObjectIdentity
frAtmAddr = _FrAtmAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6)
)
_FrAtmAddrRowStatusTable_Object = MibTable
frAtmAddrRowStatusTable = _FrAtmAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 1)
)
if mibBuilder.loadTexts:
    frAtmAddrRowStatusTable.setStatus("mandatory")
_FrAtmAddrRowStatusEntry_Object = MibTableRow
frAtmAddrRowStatusEntry = _FrAtmAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 1, 1)
)
frAtmAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmAddrIndex"),
)
if mibBuilder.loadTexts:
    frAtmAddrRowStatusEntry.setStatus("mandatory")
_FrAtmAddrRowStatus_Type = RowStatus
_FrAtmAddrRowStatus_Object = MibTableColumn
frAtmAddrRowStatus = _FrAtmAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 1, 1, 1),
    _FrAtmAddrRowStatus_Type()
)
frAtmAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmAddrRowStatus.setStatus("mandatory")
_FrAtmAddrComponentName_Type = DisplayString
_FrAtmAddrComponentName_Object = MibTableColumn
frAtmAddrComponentName = _FrAtmAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 1, 1, 2),
    _FrAtmAddrComponentName_Type()
)
frAtmAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmAddrComponentName.setStatus("mandatory")
_FrAtmAddrStorageType_Type = StorageType
_FrAtmAddrStorageType_Object = MibTableColumn
frAtmAddrStorageType = _FrAtmAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 1, 1, 4),
    _FrAtmAddrStorageType_Type()
)
frAtmAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmAddrStorageType.setStatus("mandatory")
_FrAtmAddrIndex_Type = NonReplicated
_FrAtmAddrIndex_Object = MibTableColumn
frAtmAddrIndex = _FrAtmAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 1, 1, 10),
    _FrAtmAddrIndex_Type()
)
frAtmAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmAddrIndex.setStatus("mandatory")
_FrAtmAddrProvTable_Object = MibTable
frAtmAddrProvTable = _FrAtmAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 10)
)
if mibBuilder.loadTexts:
    frAtmAddrProvTable.setStatus("mandatory")
_FrAtmAddrProvEntry_Object = MibTableRow
frAtmAddrProvEntry = _FrAtmAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 10, 1)
)
frAtmAddrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmAddrIndex"),
)
if mibBuilder.loadTexts:
    frAtmAddrProvEntry.setStatus("mandatory")


class _FrAtmAddrAddress_Type(AsciiString):
    """Custom type frAtmAddrAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_FrAtmAddrAddress_Type.__name__ = "AsciiString"
_FrAtmAddrAddress_Object = MibTableColumn
frAtmAddrAddress = _FrAtmAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 10, 1, 2),
    _FrAtmAddrAddress_Type()
)
frAtmAddrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmAddrAddress.setStatus("mandatory")
_FrAtmAddrAddrOpTable_Object = MibTable
frAtmAddrAddrOpTable = _FrAtmAddrAddrOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 11)
)
if mibBuilder.loadTexts:
    frAtmAddrAddrOpTable.setStatus("mandatory")
_FrAtmAddrAddrOpEntry_Object = MibTableRow
frAtmAddrAddrOpEntry = _FrAtmAddrAddrOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 11, 1)
)
frAtmAddrAddrOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmAddrIndex"),
)
if mibBuilder.loadTexts:
    frAtmAddrAddrOpEntry.setStatus("mandatory")


class _FrAtmAddrMyAddress_Type(AsciiString):
    """Custom type frAtmAddrMyAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_FrAtmAddrMyAddress_Type.__name__ = "AsciiString"
_FrAtmAddrMyAddress_Object = MibTableColumn
frAtmAddrMyAddress = _FrAtmAddrMyAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 6, 11, 1, 1),
    _FrAtmAddrMyAddress_Type()
)
frAtmAddrMyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmAddrMyAddress.setStatus("mandatory")
_FrAtmCa_ObjectIdentity = ObjectIdentity
frAtmCa = _FrAtmCa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7)
)
_FrAtmCaRowStatusTable_Object = MibTable
frAtmCaRowStatusTable = _FrAtmCaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 1)
)
if mibBuilder.loadTexts:
    frAtmCaRowStatusTable.setStatus("mandatory")
_FrAtmCaRowStatusEntry_Object = MibTableRow
frAtmCaRowStatusEntry = _FrAtmCaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 1, 1)
)
frAtmCaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaRowStatusEntry.setStatus("mandatory")
_FrAtmCaRowStatus_Type = RowStatus
_FrAtmCaRowStatus_Object = MibTableColumn
frAtmCaRowStatus = _FrAtmCaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 1, 1, 1),
    _FrAtmCaRowStatus_Type()
)
frAtmCaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaRowStatus.setStatus("mandatory")
_FrAtmCaComponentName_Type = DisplayString
_FrAtmCaComponentName_Object = MibTableColumn
frAtmCaComponentName = _FrAtmCaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 1, 1, 2),
    _FrAtmCaComponentName_Type()
)
frAtmCaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaComponentName.setStatus("mandatory")
_FrAtmCaStorageType_Type = StorageType
_FrAtmCaStorageType_Object = MibTableColumn
frAtmCaStorageType = _FrAtmCaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 1, 1, 4),
    _FrAtmCaStorageType_Type()
)
frAtmCaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaStorageType.setStatus("mandatory")
_FrAtmCaIndex_Type = NonReplicated
_FrAtmCaIndex_Object = MibTableColumn
frAtmCaIndex = _FrAtmCaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 1, 1, 10),
    _FrAtmCaIndex_Type()
)
frAtmCaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmCaIndex.setStatus("mandatory")
_FrAtmCaTpm_ObjectIdentity = ObjectIdentity
frAtmCaTpm = _FrAtmCaTpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2)
)
_FrAtmCaTpmRowStatusTable_Object = MibTable
frAtmCaTpmRowStatusTable = _FrAtmCaTpmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 1)
)
if mibBuilder.loadTexts:
    frAtmCaTpmRowStatusTable.setStatus("mandatory")
_FrAtmCaTpmRowStatusEntry_Object = MibTableRow
frAtmCaTpmRowStatusEntry = _FrAtmCaTpmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 1, 1)
)
frAtmCaTpmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaTpmIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaTpmRowStatusEntry.setStatus("mandatory")
_FrAtmCaTpmRowStatus_Type = RowStatus
_FrAtmCaTpmRowStatus_Object = MibTableColumn
frAtmCaTpmRowStatus = _FrAtmCaTpmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 1, 1, 1),
    _FrAtmCaTpmRowStatus_Type()
)
frAtmCaTpmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaTpmRowStatus.setStatus("mandatory")
_FrAtmCaTpmComponentName_Type = DisplayString
_FrAtmCaTpmComponentName_Object = MibTableColumn
frAtmCaTpmComponentName = _FrAtmCaTpmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 1, 1, 2),
    _FrAtmCaTpmComponentName_Type()
)
frAtmCaTpmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaTpmComponentName.setStatus("mandatory")
_FrAtmCaTpmStorageType_Type = StorageType
_FrAtmCaTpmStorageType_Object = MibTableColumn
frAtmCaTpmStorageType = _FrAtmCaTpmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 1, 1, 4),
    _FrAtmCaTpmStorageType_Type()
)
frAtmCaTpmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaTpmStorageType.setStatus("mandatory")


class _FrAtmCaTpmIndex_Type(Integer32):
    """Custom type frAtmCaTpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrAtmCaTpmIndex_Type.__name__ = "Integer32"
_FrAtmCaTpmIndex_Object = MibTableColumn
frAtmCaTpmIndex = _FrAtmCaTpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 1, 1, 10),
    _FrAtmCaTpmIndex_Type()
)
frAtmCaTpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmCaTpmIndex.setStatus("mandatory")
_FrAtmCaTpmProvTable_Object = MibTable
frAtmCaTpmProvTable = _FrAtmCaTpmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 10)
)
if mibBuilder.loadTexts:
    frAtmCaTpmProvTable.setStatus("mandatory")
_FrAtmCaTpmProvEntry_Object = MibTableRow
frAtmCaTpmProvEntry = _FrAtmCaTpmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 10, 1)
)
frAtmCaTpmProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaTpmIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaTpmProvEntry.setStatus("mandatory")


class _FrAtmCaTpmAssignedBandwidthPool_Type(Integer32):
    """Custom type frAtmCaTpmAssignedBandwidthPool based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("samePoolAsModule", 255))
    )


_FrAtmCaTpmAssignedBandwidthPool_Type.__name__ = "Integer32"
_FrAtmCaTpmAssignedBandwidthPool_Object = MibTableColumn
frAtmCaTpmAssignedBandwidthPool = _FrAtmCaTpmAssignedBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 10, 1, 1),
    _FrAtmCaTpmAssignedBandwidthPool_Type()
)
frAtmCaTpmAssignedBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaTpmAssignedBandwidthPool.setStatus("mandatory")


class _FrAtmCaTpmTrafficParmConvPolicy_Type(Integer32):
    """Custom type frAtmCaTpmTrafficParmConvPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("sameAsModule", 0))
    )


_FrAtmCaTpmTrafficParmConvPolicy_Type.__name__ = "Integer32"
_FrAtmCaTpmTrafficParmConvPolicy_Object = MibTableColumn
frAtmCaTpmTrafficParmConvPolicy = _FrAtmCaTpmTrafficParmConvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 10, 1, 2),
    _FrAtmCaTpmTrafficParmConvPolicy_Type()
)
frAtmCaTpmTrafficParmConvPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaTpmTrafficParmConvPolicy.setStatus("mandatory")


class _FrAtmCaTpmAverageFrameSize_Type(Integer32):
    """Custom type frAtmCaTpmAverageFrameSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8187),
    )


_FrAtmCaTpmAverageFrameSize_Type.__name__ = "Integer32"
_FrAtmCaTpmAverageFrameSize_Object = MibTableColumn
frAtmCaTpmAverageFrameSize = _FrAtmCaTpmAverageFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 2, 10, 1, 3),
    _FrAtmCaTpmAverageFrameSize_Type()
)
frAtmCaTpmAverageFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaTpmAverageFrameSize.setStatus("mandatory")
_FrAtmCaProvTable_Object = MibTable
frAtmCaProvTable = _FrAtmCaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 10)
)
if mibBuilder.loadTexts:
    frAtmCaProvTable.setStatus("mandatory")
_FrAtmCaProvEntry_Object = MibTableRow
frAtmCaProvEntry = _FrAtmCaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 10, 1)
)
frAtmCaProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaProvEntry.setStatus("mandatory")


class _FrAtmCaCallAdmissionControl_Type(Integer32):
    """Custom type frAtmCaCallAdmissionControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FrAtmCaCallAdmissionControl_Type.__name__ = "Integer32"
_FrAtmCaCallAdmissionControl_Object = MibTableColumn
frAtmCaCallAdmissionControl = _FrAtmCaCallAdmissionControl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 10, 1, 1),
    _FrAtmCaCallAdmissionControl_Type()
)
frAtmCaCallAdmissionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaCallAdmissionControl.setStatus("mandatory")


class _FrAtmCaOverrideLinkRate_Type(Unsigned32):
    """Custom type frAtmCaOverrideLinkRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_FrAtmCaOverrideLinkRate_Type.__name__ = "Unsigned32"
_FrAtmCaOverrideLinkRate_Object = MibTableColumn
frAtmCaOverrideLinkRate = _FrAtmCaOverrideLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 10, 1, 2),
    _FrAtmCaOverrideLinkRate_Type()
)
frAtmCaOverrideLinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaOverrideLinkRate.setStatus("mandatory")
_FrAtmCaSdTable_Object = MibTable
frAtmCaSdTable = _FrAtmCaSdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 11)
)
if mibBuilder.loadTexts:
    frAtmCaSdTable.setStatus("mandatory")
_FrAtmCaSdEntry_Object = MibTableRow
frAtmCaSdEntry = _FrAtmCaSdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 11, 1)
)
frAtmCaSdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaSdEntry.setStatus("mandatory")


class _FrAtmCaSdMode_Type(Integer32):
    """Custom type frAtmCaSdMode based on Integer32"""
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
        *(("speTranslationMode", 2),
          ("translationMode", 0),
          ("transparentMode", 1))
    )


_FrAtmCaSdMode_Type.__name__ = "Integer32"
_FrAtmCaSdMode_Object = MibTableColumn
frAtmCaSdMode = _FrAtmCaSdMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 11, 1, 1),
    _FrAtmCaSdMode_Type()
)
frAtmCaSdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaSdMode.setStatus("mandatory")


class _FrAtmCaSdDeToClpMapping_Type(Integer32):
    """Custom type frAtmCaSdDeToClpMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_FrAtmCaSdDeToClpMapping_Type.__name__ = "Integer32"
_FrAtmCaSdDeToClpMapping_Object = MibTableColumn
frAtmCaSdDeToClpMapping = _FrAtmCaSdDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 11, 1, 2),
    _FrAtmCaSdDeToClpMapping_Type()
)
frAtmCaSdDeToClpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaSdDeToClpMapping.setStatus("mandatory")


class _FrAtmCaSdClpToDeMapping_Type(Integer32):
    """Custom type frAtmCaSdClpToDeMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_FrAtmCaSdClpToDeMapping_Type.__name__ = "Integer32"
_FrAtmCaSdClpToDeMapping_Object = MibTableColumn
frAtmCaSdClpToDeMapping = _FrAtmCaSdClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 11, 1, 3),
    _FrAtmCaSdClpToDeMapping_Type()
)
frAtmCaSdClpToDeMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaSdClpToDeMapping.setStatus("mandatory")


class _FrAtmCaSdFecnToEfciMapping_Type(Integer32):
    """Custom type frAtmCaSdFecnToEfciMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2))
    )


_FrAtmCaSdFecnToEfciMapping_Type.__name__ = "Integer32"
_FrAtmCaSdFecnToEfciMapping_Object = MibTableColumn
frAtmCaSdFecnToEfciMapping = _FrAtmCaSdFecnToEfciMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 11, 1, 4),
    _FrAtmCaSdFecnToEfciMapping_Type()
)
frAtmCaSdFecnToEfciMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaSdFecnToEfciMapping.setStatus("mandatory")


class _FrAtmCaSdCrToUuMapping_Type(Integer32):
    """Custom type frAtmCaSdCrToUuMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("preserve", 2))
    )


_FrAtmCaSdCrToUuMapping_Type.__name__ = "Integer32"
_FrAtmCaSdCrToUuMapping_Object = MibTableColumn
frAtmCaSdCrToUuMapping = _FrAtmCaSdCrToUuMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 11, 1, 5),
    _FrAtmCaSdCrToUuMapping_Type()
)
frAtmCaSdCrToUuMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaSdCrToUuMapping.setStatus("obsolete")
_FrAtmCaNdTable_Object = MibTable
frAtmCaNdTable = _FrAtmCaNdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 12)
)
if mibBuilder.loadTexts:
    frAtmCaNdTable.setStatus("mandatory")
_FrAtmCaNdEntry_Object = MibTableRow
frAtmCaNdEntry = _FrAtmCaNdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 12, 1)
)
frAtmCaNdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaNdEntry.setStatus("mandatory")


class _FrAtmCaNdDeToClpMapping_Type(Integer32):
    """Custom type frAtmCaNdDeToClpMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 0),
          ("always1", 1),
          ("preserve", 2))
    )


_FrAtmCaNdDeToClpMapping_Type.__name__ = "Integer32"
_FrAtmCaNdDeToClpMapping_Object = MibTableColumn
frAtmCaNdDeToClpMapping = _FrAtmCaNdDeToClpMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 12, 1, 1),
    _FrAtmCaNdDeToClpMapping_Type()
)
frAtmCaNdDeToClpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaNdDeToClpMapping.setStatus("mandatory")


class _FrAtmCaNdClpToDeMapping_Type(Integer32):
    """Custom type frAtmCaNdClpToDeMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preserve", 2),
          ("transparent", 3))
    )


_FrAtmCaNdClpToDeMapping_Type.__name__ = "Integer32"
_FrAtmCaNdClpToDeMapping_Object = MibTableColumn
frAtmCaNdClpToDeMapping = _FrAtmCaNdClpToDeMapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 12, 1, 2),
    _FrAtmCaNdClpToDeMapping_Type()
)
frAtmCaNdClpToDeMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaNdClpToDeMapping.setStatus("mandatory")
_FrAtmCaIfQoSTable_Object = MibTable
frAtmCaIfQoSTable = _FrAtmCaIfQoSTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 13)
)
if mibBuilder.loadTexts:
    frAtmCaIfQoSTable.setStatus("mandatory")
_FrAtmCaIfQoSEntry_Object = MibTableRow
frAtmCaIfQoSEntry = _FrAtmCaIfQoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 13, 1)
)
frAtmCaIfQoSEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaIfQoSEntry.setStatus("mandatory")


class _FrAtmCaSiwfEmissionPriorityToIf_Type(Integer32):
    """Custom type frAtmCaSiwfEmissionPriorityToIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromTp", 254),
          ("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3))
    )


_FrAtmCaSiwfEmissionPriorityToIf_Type.__name__ = "Integer32"
_FrAtmCaSiwfEmissionPriorityToIf_Object = MibTableColumn
frAtmCaSiwfEmissionPriorityToIf = _FrAtmCaSiwfEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 13, 1, 1),
    _FrAtmCaSiwfEmissionPriorityToIf_Type()
)
frAtmCaSiwfEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaSiwfEmissionPriorityToIf.setStatus("mandatory")


class _FrAtmCaSiwfTransferPriority_Type(Integer32):
    """Custom type frAtmCaSiwfTransferPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrAtmCaSiwfTransferPriority_Type.__name__ = "Integer32"
_FrAtmCaSiwfTransferPriority_Object = MibTableColumn
frAtmCaSiwfTransferPriority = _FrAtmCaSiwfTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 13, 1, 2),
    _FrAtmCaSiwfTransferPriority_Type()
)
frAtmCaSiwfTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaSiwfTransferPriority.setStatus("mandatory")


class _FrAtmCaNiwfEmissionPriorityToIf_Type(Integer32):
    """Custom type frAtmCaNiwfEmissionPriorityToIf based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("deriveFromTp", 254),
          ("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3))
    )


_FrAtmCaNiwfEmissionPriorityToIf_Type.__name__ = "Integer32"
_FrAtmCaNiwfEmissionPriorityToIf_Object = MibTableColumn
frAtmCaNiwfEmissionPriorityToIf = _FrAtmCaNiwfEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 13, 1, 3),
    _FrAtmCaNiwfEmissionPriorityToIf_Type()
)
frAtmCaNiwfEmissionPriorityToIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaNiwfEmissionPriorityToIf.setStatus("mandatory")


class _FrAtmCaNiwfTransferPriority_Type(Integer32):
    """Custom type frAtmCaNiwfTransferPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrAtmCaNiwfTransferPriority_Type.__name__ = "Integer32"
_FrAtmCaNiwfTransferPriority_Object = MibTableColumn
frAtmCaNiwfTransferPriority = _FrAtmCaNiwfTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 13, 1, 4),
    _FrAtmCaNiwfTransferPriority_Type()
)
frAtmCaNiwfTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaNiwfTransferPriority.setStatus("mandatory")
_FrAtmCaOpTable_Object = MibTable
frAtmCaOpTable = _FrAtmCaOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 14)
)
if mibBuilder.loadTexts:
    frAtmCaOpTable.setStatus("mandatory")
_FrAtmCaOpEntry_Object = MibTableRow
frAtmCaOpEntry = _FrAtmCaOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 14, 1)
)
frAtmCaOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaOpEntry.setStatus("mandatory")


class _FrAtmCaLinkRate_Type(Unsigned32):
    """Custom type frAtmCaLinkRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_FrAtmCaLinkRate_Type.__name__ = "Unsigned32"
_FrAtmCaLinkRate_Object = MibTableColumn
frAtmCaLinkRate = _FrAtmCaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 14, 1, 1),
    _FrAtmCaLinkRate_Type()
)
frAtmCaLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaLinkRate.setStatus("mandatory")


class _FrAtmCaNailedUpPvcs_Type(Gauge32):
    """Custom type frAtmCaNailedUpPvcs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrAtmCaNailedUpPvcs_Type.__name__ = "Gauge32"
_FrAtmCaNailedUpPvcs_Object = MibTableColumn
frAtmCaNailedUpPvcs = _FrAtmCaNailedUpPvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 14, 1, 3),
    _FrAtmCaNailedUpPvcs_Type()
)
frAtmCaNailedUpPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaNailedUpPvcs.setStatus("mandatory")


class _FrAtmCaTroubledDlcis_Type(Gauge32):
    """Custom type frAtmCaTroubledDlcis based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrAtmCaTroubledDlcis_Type.__name__ = "Gauge32"
_FrAtmCaTroubledDlcis_Object = MibTableColumn
frAtmCaTroubledDlcis = _FrAtmCaTroubledDlcis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 14, 1, 5),
    _FrAtmCaTroubledDlcis_Type()
)
frAtmCaTroubledDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaTroubledDlcis.setStatus("mandatory")


class _FrAtmCaSoftPvcs_Type(Gauge32):
    """Custom type frAtmCaSoftPvcs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrAtmCaSoftPvcs_Type.__name__ = "Gauge32"
_FrAtmCaSoftPvcs_Object = MibTableColumn
frAtmCaSoftPvcs = _FrAtmCaSoftPvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 14, 1, 6),
    _FrAtmCaSoftPvcs_Type()
)
frAtmCaSoftPvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaSoftPvcs.setStatus("mandatory")
_FrAtmCaAccountingOptionsTable_Object = MibTable
frAtmCaAccountingOptionsTable = _FrAtmCaAccountingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 15)
)
if mibBuilder.loadTexts:
    frAtmCaAccountingOptionsTable.setStatus("mandatory")
_FrAtmCaAccountingOptionsEntry_Object = MibTableRow
frAtmCaAccountingOptionsEntry = _FrAtmCaAccountingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 15, 1)
)
frAtmCaAccountingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaAccountingOptionsEntry.setStatus("mandatory")


class _FrAtmCaAccountClass_Type(Unsigned32):
    """Custom type frAtmCaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrAtmCaAccountClass_Type.__name__ = "Unsigned32"
_FrAtmCaAccountClass_Object = MibTableColumn
frAtmCaAccountClass = _FrAtmCaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 15, 1, 1),
    _FrAtmCaAccountClass_Type()
)
frAtmCaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaAccountClass.setStatus("mandatory")


class _FrAtmCaAccountCollection_Type(OctetString):
    """Custom type frAtmCaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrAtmCaAccountCollection_Type.__name__ = "OctetString"
_FrAtmCaAccountCollection_Object = MibTableColumn
frAtmCaAccountCollection = _FrAtmCaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 15, 1, 2),
    _FrAtmCaAccountCollection_Type()
)
frAtmCaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaAccountCollection.setStatus("mandatory")


class _FrAtmCaServiceExchange_Type(Unsigned32):
    """Custom type frAtmCaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrAtmCaServiceExchange_Type.__name__ = "Unsigned32"
_FrAtmCaServiceExchange_Object = MibTableColumn
frAtmCaServiceExchange = _FrAtmCaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 15, 1, 3),
    _FrAtmCaServiceExchange_Type()
)
frAtmCaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaServiceExchange.setStatus("mandatory")
_FrAtmCaBwPoolTable_Object = MibTable
frAtmCaBwPoolTable = _FrAtmCaBwPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 365)
)
if mibBuilder.loadTexts:
    frAtmCaBwPoolTable.setStatus("mandatory")
_FrAtmCaBwPoolEntry_Object = MibTableRow
frAtmCaBwPoolEntry = _FrAtmCaBwPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 365, 1)
)
frAtmCaBwPoolEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaBwPoolIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaBwPoolEntry.setStatus("mandatory")


class _FrAtmCaBwPoolIndex_Type(Integer32):
    """Custom type frAtmCaBwPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrAtmCaBwPoolIndex_Type.__name__ = "Integer32"
_FrAtmCaBwPoolIndex_Object = MibTableColumn
frAtmCaBwPoolIndex = _FrAtmCaBwPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 365, 1, 1),
    _FrAtmCaBwPoolIndex_Type()
)
frAtmCaBwPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmCaBwPoolIndex.setStatus("mandatory")


class _FrAtmCaBwPoolValue_Type(Unsigned32):
    """Custom type frAtmCaBwPoolValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FrAtmCaBwPoolValue_Type.__name__ = "Unsigned32"
_FrAtmCaBwPoolValue_Object = MibTableColumn
frAtmCaBwPoolValue = _FrAtmCaBwPoolValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 365, 1, 2),
    _FrAtmCaBwPoolValue_Type()
)
frAtmCaBwPoolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCaBwPoolValue.setStatus("mandatory")
_FrAtmCaPoolProvBwTable_Object = MibTable
frAtmCaPoolProvBwTable = _FrAtmCaPoolProvBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 366)
)
if mibBuilder.loadTexts:
    frAtmCaPoolProvBwTable.setStatus("mandatory")
_FrAtmCaPoolProvBwEntry_Object = MibTableRow
frAtmCaPoolProvBwEntry = _FrAtmCaPoolProvBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 366, 1)
)
frAtmCaPoolProvBwEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaPoolProvBwIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaPoolProvBwEntry.setStatus("mandatory")


class _FrAtmCaPoolProvBwIndex_Type(Integer32):
    """Custom type frAtmCaPoolProvBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrAtmCaPoolProvBwIndex_Type.__name__ = "Integer32"
_FrAtmCaPoolProvBwIndex_Object = MibTableColumn
frAtmCaPoolProvBwIndex = _FrAtmCaPoolProvBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 366, 1, 1),
    _FrAtmCaPoolProvBwIndex_Type()
)
frAtmCaPoolProvBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmCaPoolProvBwIndex.setStatus("mandatory")


class _FrAtmCaPoolProvBwValue_Type(Gauge32):
    """Custom type frAtmCaPoolProvBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_FrAtmCaPoolProvBwValue_Type.__name__ = "Gauge32"
_FrAtmCaPoolProvBwValue_Object = MibTableColumn
frAtmCaPoolProvBwValue = _FrAtmCaPoolProvBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 366, 1, 2),
    _FrAtmCaPoolProvBwValue_Type()
)
frAtmCaPoolProvBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaPoolProvBwValue.setStatus("mandatory")
_FrAtmCaPoolAvailBwTable_Object = MibTable
frAtmCaPoolAvailBwTable = _FrAtmCaPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 367)
)
if mibBuilder.loadTexts:
    frAtmCaPoolAvailBwTable.setStatus("mandatory")
_FrAtmCaPoolAvailBwEntry_Object = MibTableRow
frAtmCaPoolAvailBwEntry = _FrAtmCaPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 367, 1)
)
frAtmCaPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaPoolAvailBwEntry.setStatus("mandatory")


class _FrAtmCaPoolAvailBwIndex_Type(Integer32):
    """Custom type frAtmCaPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrAtmCaPoolAvailBwIndex_Type.__name__ = "Integer32"
_FrAtmCaPoolAvailBwIndex_Object = MibTableColumn
frAtmCaPoolAvailBwIndex = _FrAtmCaPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 367, 1, 1),
    _FrAtmCaPoolAvailBwIndex_Type()
)
frAtmCaPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmCaPoolAvailBwIndex.setStatus("mandatory")


class _FrAtmCaPoolAvailBwValue_Type(Gauge32):
    """Custom type frAtmCaPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_FrAtmCaPoolAvailBwValue_Type.__name__ = "Gauge32"
_FrAtmCaPoolAvailBwValue_Object = MibTableColumn
frAtmCaPoolAvailBwValue = _FrAtmCaPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 367, 1, 2),
    _FrAtmCaPoolAvailBwValue_Type()
)
frAtmCaPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaPoolAvailBwValue.setStatus("mandatory")
_FrAtmCaPoolAdmitBwTable_Object = MibTable
frAtmCaPoolAdmitBwTable = _FrAtmCaPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 380)
)
if mibBuilder.loadTexts:
    frAtmCaPoolAdmitBwTable.setStatus("mandatory")
_FrAtmCaPoolAdmitBwEntry_Object = MibTableRow
frAtmCaPoolAdmitBwEntry = _FrAtmCaPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 380, 1)
)
frAtmCaPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmCaPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    frAtmCaPoolAdmitBwEntry.setStatus("mandatory")


class _FrAtmCaPoolAdmitBwIndex_Type(Integer32):
    """Custom type frAtmCaPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrAtmCaPoolAdmitBwIndex_Type.__name__ = "Integer32"
_FrAtmCaPoolAdmitBwIndex_Object = MibTableColumn
frAtmCaPoolAdmitBwIndex = _FrAtmCaPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 380, 1, 1),
    _FrAtmCaPoolAdmitBwIndex_Type()
)
frAtmCaPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmCaPoolAdmitBwIndex.setStatus("mandatory")


class _FrAtmCaPoolAdmitBwValue_Type(Gauge32):
    """Custom type frAtmCaPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_FrAtmCaPoolAdmitBwValue_Type.__name__ = "Gauge32"
_FrAtmCaPoolAdmitBwValue_Object = MibTableColumn
frAtmCaPoolAdmitBwValue = _FrAtmCaPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 7, 380, 1, 2),
    _FrAtmCaPoolAdmitBwValue_Type()
)
frAtmCaPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmCaPoolAdmitBwValue.setStatus("mandatory")
_FrAtmCidDataTable_Object = MibTable
frAtmCidDataTable = _FrAtmCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 10)
)
if mibBuilder.loadTexts:
    frAtmCidDataTable.setStatus("mandatory")
_FrAtmCidDataEntry_Object = MibTableRow
frAtmCidDataEntry = _FrAtmCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 10, 1)
)
frAtmCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
)
if mibBuilder.loadTexts:
    frAtmCidDataEntry.setStatus("mandatory")


class _FrAtmCustomerIdentifier_Type(Unsigned32):
    """Custom type frAtmCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_FrAtmCustomerIdentifier_Type.__name__ = "Unsigned32"
_FrAtmCustomerIdentifier_Object = MibTableColumn
frAtmCustomerIdentifier = _FrAtmCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 10, 1, 1),
    _FrAtmCustomerIdentifier_Type()
)
frAtmCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmCustomerIdentifier.setStatus("mandatory")
_FrAtmStateTable_Object = MibTable
frAtmStateTable = _FrAtmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11)
)
if mibBuilder.loadTexts:
    frAtmStateTable.setStatus("mandatory")
_FrAtmStateEntry_Object = MibTableRow
frAtmStateEntry = _FrAtmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1)
)
frAtmStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
)
if mibBuilder.loadTexts:
    frAtmStateEntry.setStatus("mandatory")


class _FrAtmAdminState_Type(Integer32):
    """Custom type frAtmAdminState based on Integer32"""
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


_FrAtmAdminState_Type.__name__ = "Integer32"
_FrAtmAdminState_Object = MibTableColumn
frAtmAdminState = _FrAtmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1, 1),
    _FrAtmAdminState_Type()
)
frAtmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmAdminState.setStatus("mandatory")


class _FrAtmOperationalState_Type(Integer32):
    """Custom type frAtmOperationalState based on Integer32"""
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


_FrAtmOperationalState_Type.__name__ = "Integer32"
_FrAtmOperationalState_Object = MibTableColumn
frAtmOperationalState = _FrAtmOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1, 2),
    _FrAtmOperationalState_Type()
)
frAtmOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmOperationalState.setStatus("mandatory")


class _FrAtmUsageState_Type(Integer32):
    """Custom type frAtmUsageState based on Integer32"""
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


_FrAtmUsageState_Type.__name__ = "Integer32"
_FrAtmUsageState_Object = MibTableColumn
frAtmUsageState = _FrAtmUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1, 3),
    _FrAtmUsageState_Type()
)
frAtmUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmUsageState.setStatus("mandatory")


class _FrAtmAvailabilityStatus_Type(OctetString):
    """Custom type frAtmAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FrAtmAvailabilityStatus_Type.__name__ = "OctetString"
_FrAtmAvailabilityStatus_Object = MibTableColumn
frAtmAvailabilityStatus = _FrAtmAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1, 4),
    _FrAtmAvailabilityStatus_Type()
)
frAtmAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmAvailabilityStatus.setStatus("mandatory")


class _FrAtmProceduralStatus_Type(OctetString):
    """Custom type frAtmProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrAtmProceduralStatus_Type.__name__ = "OctetString"
_FrAtmProceduralStatus_Object = MibTableColumn
frAtmProceduralStatus = _FrAtmProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1, 5),
    _FrAtmProceduralStatus_Type()
)
frAtmProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmProceduralStatus.setStatus("mandatory")


class _FrAtmControlStatus_Type(OctetString):
    """Custom type frAtmControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrAtmControlStatus_Type.__name__ = "OctetString"
_FrAtmControlStatus_Object = MibTableColumn
frAtmControlStatus = _FrAtmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1, 6),
    _FrAtmControlStatus_Type()
)
frAtmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmControlStatus.setStatus("mandatory")


class _FrAtmAlarmStatus_Type(OctetString):
    """Custom type frAtmAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrAtmAlarmStatus_Type.__name__ = "OctetString"
_FrAtmAlarmStatus_Object = MibTableColumn
frAtmAlarmStatus = _FrAtmAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1, 7),
    _FrAtmAlarmStatus_Type()
)
frAtmAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmAlarmStatus.setStatus("mandatory")


class _FrAtmStandbyStatus_Type(Integer32):
    """Custom type frAtmStandbyStatus based on Integer32"""
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


_FrAtmStandbyStatus_Type.__name__ = "Integer32"
_FrAtmStandbyStatus_Object = MibTableColumn
frAtmStandbyStatus = _FrAtmStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1, 8),
    _FrAtmStandbyStatus_Type()
)
frAtmStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmStandbyStatus.setStatus("mandatory")


class _FrAtmUnknownStatus_Type(Integer32):
    """Custom type frAtmUnknownStatus based on Integer32"""
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


_FrAtmUnknownStatus_Type.__name__ = "Integer32"
_FrAtmUnknownStatus_Object = MibTableColumn
frAtmUnknownStatus = _FrAtmUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 11, 1, 9),
    _FrAtmUnknownStatus_Type()
)
frAtmUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmUnknownStatus.setStatus("mandatory")
_FrAtmStatsTable_Object = MibTable
frAtmStatsTable = _FrAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 12)
)
if mibBuilder.loadTexts:
    frAtmStatsTable.setStatus("mandatory")
_FrAtmStatsEntry_Object = MibTableRow
frAtmStatsEntry = _FrAtmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 12, 1)
)
frAtmStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
)
if mibBuilder.loadTexts:
    frAtmStatsEntry.setStatus("mandatory")


class _FrAtmLastUnknownDlci_Type(Unsigned32):
    """Custom type frAtmLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_FrAtmLastUnknownDlci_Type.__name__ = "Unsigned32"
_FrAtmLastUnknownDlci_Object = MibTableColumn
frAtmLastUnknownDlci = _FrAtmLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 12, 1, 1),
    _FrAtmLastUnknownDlci_Type()
)
frAtmLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmLastUnknownDlci.setStatus("mandatory")
_FrAtmUnknownDlciFramesFromIf_Type = Counter32
_FrAtmUnknownDlciFramesFromIf_Object = MibTableColumn
frAtmUnknownDlciFramesFromIf = _FrAtmUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 12, 1, 2),
    _FrAtmUnknownDlciFramesFromIf_Type()
)
frAtmUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmUnknownDlciFramesFromIf.setStatus("mandatory")
_FrAtmInvalidHeaderFramesFromIf_Type = Counter32
_FrAtmInvalidHeaderFramesFromIf_Object = MibTableColumn
frAtmInvalidHeaderFramesFromIf = _FrAtmInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 12, 1, 3),
    _FrAtmInvalidHeaderFramesFromIf_Type()
)
frAtmInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmInvalidHeaderFramesFromIf.setStatus("mandatory")
_FrAtmIfEntryTable_Object = MibTable
frAtmIfEntryTable = _FrAtmIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 13)
)
if mibBuilder.loadTexts:
    frAtmIfEntryTable.setStatus("mandatory")
_FrAtmIfEntryEntry_Object = MibTableRow
frAtmIfEntryEntry = _FrAtmIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 13, 1)
)
frAtmIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
)
if mibBuilder.loadTexts:
    frAtmIfEntryEntry.setStatus("mandatory")


class _FrAtmIfAdminStatus_Type(Integer32):
    """Custom type frAtmIfAdminStatus based on Integer32"""
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


_FrAtmIfAdminStatus_Type.__name__ = "Integer32"
_FrAtmIfAdminStatus_Object = MibTableColumn
frAtmIfAdminStatus = _FrAtmIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 13, 1, 1),
    _FrAtmIfAdminStatus_Type()
)
frAtmIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmIfAdminStatus.setStatus("mandatory")


class _FrAtmIfIndex_Type(InterfaceIndex):
    """Custom type frAtmIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrAtmIfIndex_Type.__name__ = "InterfaceIndex"
_FrAtmIfIndex_Object = MibTableColumn
frAtmIfIndex = _FrAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 13, 1, 2),
    _FrAtmIfIndex_Type()
)
frAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmIfIndex.setStatus("mandatory")
_FrAtmOperStatusTable_Object = MibTable
frAtmOperStatusTable = _FrAtmOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 14)
)
if mibBuilder.loadTexts:
    frAtmOperStatusTable.setStatus("mandatory")
_FrAtmOperStatusEntry_Object = MibTableRow
frAtmOperStatusEntry = _FrAtmOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 14, 1)
)
frAtmOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
)
if mibBuilder.loadTexts:
    frAtmOperStatusEntry.setStatus("mandatory")


class _FrAtmSnmpOperStatus_Type(Integer32):
    """Custom type frAtmSnmpOperStatus based on Integer32"""
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


_FrAtmSnmpOperStatus_Type.__name__ = "Integer32"
_FrAtmSnmpOperStatus_Object = MibTableColumn
frAtmSnmpOperStatus = _FrAtmSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 14, 1, 1),
    _FrAtmSnmpOperStatus_Type()
)
frAtmSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmSnmpOperStatus.setStatus("mandatory")
_FrAtmEmissionPriorityQsTable_Object = MibTable
frAtmEmissionPriorityQsTable = _FrAtmEmissionPriorityQsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 15)
)
if mibBuilder.loadTexts:
    frAtmEmissionPriorityQsTable.setStatus("mandatory")
_FrAtmEmissionPriorityQsEntry_Object = MibTableRow
frAtmEmissionPriorityQsEntry = _FrAtmEmissionPriorityQsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 15, 1)
)
frAtmEmissionPriorityQsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
)
if mibBuilder.loadTexts:
    frAtmEmissionPriorityQsEntry.setStatus("mandatory")


class _FrAtmNumberOfEmissionQs_Type(Unsigned32):
    """Custom type frAtmNumberOfEmissionQs based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_FrAtmNumberOfEmissionQs_Type.__name__ = "Unsigned32"
_FrAtmNumberOfEmissionQs_Object = MibTableColumn
frAtmNumberOfEmissionQs = _FrAtmNumberOfEmissionQs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 15, 1, 1),
    _FrAtmNumberOfEmissionQs_Type()
)
frAtmNumberOfEmissionQs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frAtmNumberOfEmissionQs.setStatus("mandatory")
_FrAtmFrmToIfByQueueTable_Object = MibTable
frAtmFrmToIfByQueueTable = _FrAtmFrmToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 341)
)
if mibBuilder.loadTexts:
    frAtmFrmToIfByQueueTable.setStatus("mandatory")
_FrAtmFrmToIfByQueueEntry_Object = MibTableRow
frAtmFrmToIfByQueueEntry = _FrAtmFrmToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 341, 1)
)
frAtmFrmToIfByQueueEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmFrmToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    frAtmFrmToIfByQueueEntry.setStatus("mandatory")


class _FrAtmFrmToIfByQueueIndex_Type(Integer32):
    """Custom type frAtmFrmToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrAtmFrmToIfByQueueIndex_Type.__name__ = "Integer32"
_FrAtmFrmToIfByQueueIndex_Object = MibTableColumn
frAtmFrmToIfByQueueIndex = _FrAtmFrmToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 341, 1, 1),
    _FrAtmFrmToIfByQueueIndex_Type()
)
frAtmFrmToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmFrmToIfByQueueIndex.setStatus("mandatory")


class _FrAtmFrmToIfByQueueValue_Type(Unsigned32):
    """Custom type frAtmFrmToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmFrmToIfByQueueValue_Type.__name__ = "Unsigned32"
_FrAtmFrmToIfByQueueValue_Object = MibTableColumn
frAtmFrmToIfByQueueValue = _FrAtmFrmToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 341, 1, 2),
    _FrAtmFrmToIfByQueueValue_Type()
)
frAtmFrmToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmFrmToIfByQueueValue.setStatus("mandatory")
_FrAtmOctetToIfByQueueTable_Object = MibTable
frAtmOctetToIfByQueueTable = _FrAtmOctetToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 342)
)
if mibBuilder.loadTexts:
    frAtmOctetToIfByQueueTable.setStatus("mandatory")
_FrAtmOctetToIfByQueueEntry_Object = MibTableRow
frAtmOctetToIfByQueueEntry = _FrAtmOctetToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 342, 1)
)
frAtmOctetToIfByQueueEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayAtmMIB", "frAtmOctetToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    frAtmOctetToIfByQueueEntry.setStatus("mandatory")


class _FrAtmOctetToIfByQueueIndex_Type(Integer32):
    """Custom type frAtmOctetToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrAtmOctetToIfByQueueIndex_Type.__name__ = "Integer32"
_FrAtmOctetToIfByQueueIndex_Object = MibTableColumn
frAtmOctetToIfByQueueIndex = _FrAtmOctetToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 342, 1, 1),
    _FrAtmOctetToIfByQueueIndex_Type()
)
frAtmOctetToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frAtmOctetToIfByQueueIndex.setStatus("mandatory")


class _FrAtmOctetToIfByQueueValue_Type(Unsigned32):
    """Custom type frAtmOctetToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrAtmOctetToIfByQueueValue_Type.__name__ = "Unsigned32"
_FrAtmOctetToIfByQueueValue_Object = MibTableColumn
frAtmOctetToIfByQueueValue = _FrAtmOctetToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 72, 342, 1, 2),
    _FrAtmOctetToIfByQueueValue_Type()
)
frAtmOctetToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frAtmOctetToIfByQueueValue.setStatus("mandatory")
_FrameRelayAtmMIB_ObjectIdentity = ObjectIdentity
frameRelayAtmMIB = _FrameRelayAtmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 51)
)
_FrameRelayAtmGroup_ObjectIdentity = ObjectIdentity
frameRelayAtmGroup = _FrameRelayAtmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 51, 1)
)
_FrameRelayAtmGroupBE_ObjectIdentity = ObjectIdentity
frameRelayAtmGroupBE = _FrameRelayAtmGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 51, 1, 5)
)
_FrameRelayAtmGroupBE01_ObjectIdentity = ObjectIdentity
frameRelayAtmGroupBE01 = _FrameRelayAtmGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 51, 1, 5, 2)
)
_FrameRelayAtmGroupBE01A_ObjectIdentity = ObjectIdentity
frameRelayAtmGroupBE01A = _FrameRelayAtmGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 51, 1, 5, 2, 2)
)
_FrameRelayAtmCapabilities_ObjectIdentity = ObjectIdentity
frameRelayAtmCapabilities = _FrameRelayAtmCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 51, 3)
)
_FrameRelayAtmCapabilitiesBE_ObjectIdentity = ObjectIdentity
frameRelayAtmCapabilitiesBE = _FrameRelayAtmCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 51, 3, 5)
)
_FrameRelayAtmCapabilitiesBE01_ObjectIdentity = ObjectIdentity
frameRelayAtmCapabilitiesBE01 = _FrameRelayAtmCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 51, 3, 5, 2)
)
_FrameRelayAtmCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
frameRelayAtmCapabilitiesBE01A = _FrameRelayAtmCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 51, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrameRelayAtmMIB",
    **{"frAtm": frAtm,
       "frAtmRowStatusTable": frAtmRowStatusTable,
       "frAtmRowStatusEntry": frAtmRowStatusEntry,
       "frAtmRowStatus": frAtmRowStatus,
       "frAtmComponentName": frAtmComponentName,
       "frAtmStorageType": frAtmStorageType,
       "frAtmIndex": frAtmIndex,
       "frAtmFramer": frAtmFramer,
       "frAtmFramerRowStatusTable": frAtmFramerRowStatusTable,
       "frAtmFramerRowStatusEntry": frAtmFramerRowStatusEntry,
       "frAtmFramerRowStatus": frAtmFramerRowStatus,
       "frAtmFramerComponentName": frAtmFramerComponentName,
       "frAtmFramerStorageType": frAtmFramerStorageType,
       "frAtmFramerIndex": frAtmFramerIndex,
       "frAtmFramerProvTable": frAtmFramerProvTable,
       "frAtmFramerProvEntry": frAtmFramerProvEntry,
       "frAtmFramerInterfaceName": frAtmFramerInterfaceName,
       "frAtmFramerLinkTable": frAtmFramerLinkTable,
       "frAtmFramerLinkEntry": frAtmFramerLinkEntry,
       "frAtmFramerFlagsBetweenFrames": frAtmFramerFlagsBetweenFrames,
       "frAtmFramerStateTable": frAtmFramerStateTable,
       "frAtmFramerStateEntry": frAtmFramerStateEntry,
       "frAtmFramerAdminState": frAtmFramerAdminState,
       "frAtmFramerOperationalState": frAtmFramerOperationalState,
       "frAtmFramerUsageState": frAtmFramerUsageState,
       "frAtmFramerStatsTable": frAtmFramerStatsTable,
       "frAtmFramerStatsEntry": frAtmFramerStatsEntry,
       "frAtmFramerFrmToIf": frAtmFramerFrmToIf,
       "frAtmFramerFrmFromIf": frAtmFramerFrmFromIf,
       "frAtmFramerOctetFromIf": frAtmFramerOctetFromIf,
       "frAtmFramerAborts": frAtmFramerAborts,
       "frAtmFramerCrcErrors": frAtmFramerCrcErrors,
       "frAtmFramerLrcErrors": frAtmFramerLrcErrors,
       "frAtmFramerNonOctetErrors": frAtmFramerNonOctetErrors,
       "frAtmFramerOverruns": frAtmFramerOverruns,
       "frAtmFramerUnderruns": frAtmFramerUnderruns,
       "frAtmFramerLargeFrmErrors": frAtmFramerLargeFrmErrors,
       "frAtmFramerFrmModeErrors": frAtmFramerFrmModeErrors,
       "frAtmFramerUtilTable": frAtmFramerUtilTable,
       "frAtmFramerUtilEntry": frAtmFramerUtilEntry,
       "frAtmFramerNormPrioLinkUtilToIf": frAtmFramerNormPrioLinkUtilToIf,
       "frAtmFramerNormPrioLinkUtilFromIf": frAtmFramerNormPrioLinkUtilFromIf,
       "frAtmLmi": frAtmLmi,
       "frAtmLmiRowStatusTable": frAtmLmiRowStatusTable,
       "frAtmLmiRowStatusEntry": frAtmLmiRowStatusEntry,
       "frAtmLmiRowStatus": frAtmLmiRowStatus,
       "frAtmLmiComponentName": frAtmLmiComponentName,
       "frAtmLmiStorageType": frAtmLmiStorageType,
       "frAtmLmiIndex": frAtmLmiIndex,
       "frAtmLmiParmsTable": frAtmLmiParmsTable,
       "frAtmLmiParmsEntry": frAtmLmiParmsEntry,
       "frAtmLmiProcedures": frAtmLmiProcedures,
       "frAtmLmiAsyncStatusReport": frAtmLmiAsyncStatusReport,
       "frAtmLmiErrorEventThreshold": frAtmLmiErrorEventThreshold,
       "frAtmLmiEventCount": frAtmLmiEventCount,
       "frAtmLmiCheckPointTimer": frAtmLmiCheckPointTimer,
       "frAtmLmiMessageCountTimer": frAtmLmiMessageCountTimer,
       "frAtmLmiIgnoreActiveBit": frAtmLmiIgnoreActiveBit,
       "frAtmLmiSide": frAtmLmiSide,
       "frAtmLmiPvcConfigParmsInFsr": frAtmLmiPvcConfigParmsInFsr,
       "frAtmLmiStateTable": frAtmLmiStateTable,
       "frAtmLmiStateEntry": frAtmLmiStateEntry,
       "frAtmLmiAdminState": frAtmLmiAdminState,
       "frAtmLmiOperationalState": frAtmLmiOperationalState,
       "frAtmLmiUsageState": frAtmLmiUsageState,
       "frAtmLmiPsiTable": frAtmLmiPsiTable,
       "frAtmLmiPsiEntry": frAtmLmiPsiEntry,
       "frAtmLmiProtocolStatus": frAtmLmiProtocolStatus,
       "frAtmLmiOpProcedures": frAtmLmiOpProcedures,
       "frAtmLmiStatsTable": frAtmLmiStatsTable,
       "frAtmLmiStatsEntry": frAtmLmiStatsEntry,
       "frAtmLmiKeepAliveStatusToIf": frAtmLmiKeepAliveStatusToIf,
       "frAtmLmiFullStatusToIf": frAtmLmiFullStatusToIf,
       "frAtmLmiKeepAliveStatusEnqFromIf": frAtmLmiKeepAliveStatusEnqFromIf,
       "frAtmLmiFullStatusEnqFromIf": frAtmLmiFullStatusEnqFromIf,
       "frAtmLmiNetworkSideEventHistory": frAtmLmiNetworkSideEventHistory,
       "frAtmLmiProtocolErrors": frAtmLmiProtocolErrors,
       "frAtmLmiUnexpectedIes": frAtmLmiUnexpectedIes,
       "frAtmLmiSequenceErrors": frAtmLmiSequenceErrors,
       "frAtmLmiUnexpectedReports": frAtmLmiUnexpectedReports,
       "frAtmLmiPollingVerifTimeouts": frAtmLmiPollingVerifTimeouts,
       "frAtmLmiKeepAliveEnqToIf": frAtmLmiKeepAliveEnqToIf,
       "frAtmLmiFullStatusEnqToIf": frAtmLmiFullStatusEnqToIf,
       "frAtmLmiUserSideEventHistory": frAtmLmiUserSideEventHistory,
       "frAtmLmiStatusSequenceErrors": frAtmLmiStatusSequenceErrors,
       "frAtmLmiNoStatusReportCount": frAtmLmiNoStatusReportCount,
       "frAtmLmiUspParmsTable": frAtmLmiUspParmsTable,
       "frAtmLmiUspParmsEntry": frAtmLmiUspParmsEntry,
       "frAtmLmiFullStatusPollingCycles": frAtmLmiFullStatusPollingCycles,
       "frAtmLmiLinkVerificationTimer": frAtmLmiLinkVerificationTimer,
       "frAtmDlci": frAtmDlci,
       "frAtmDlciRowStatusTable": frAtmDlciRowStatusTable,
       "frAtmDlciRowStatusEntry": frAtmDlciRowStatusEntry,
       "frAtmDlciRowStatus": frAtmDlciRowStatus,
       "frAtmDlciComponentName": frAtmDlciComponentName,
       "frAtmDlciStorageType": frAtmDlciStorageType,
       "frAtmDlciIndex": frAtmDlciIndex,
       "frAtmDlciSp": frAtmDlciSp,
       "frAtmDlciSpRowStatusTable": frAtmDlciSpRowStatusTable,
       "frAtmDlciSpRowStatusEntry": frAtmDlciSpRowStatusEntry,
       "frAtmDlciSpRowStatus": frAtmDlciSpRowStatus,
       "frAtmDlciSpComponentName": frAtmDlciSpComponentName,
       "frAtmDlciSpStorageType": frAtmDlciSpStorageType,
       "frAtmDlciSpIndex": frAtmDlciSpIndex,
       "frAtmDlciSpProvTable": frAtmDlciSpProvTable,
       "frAtmDlciSpProvEntry": frAtmDlciSpProvEntry,
       "frAtmDlciSpMaximumFrameSize": frAtmDlciSpMaximumFrameSize,
       "frAtmDlciSpRateEnforcement": frAtmDlciSpRateEnforcement,
       "frAtmDlciSpCommittedInformationRate": frAtmDlciSpCommittedInformationRate,
       "frAtmDlciSpCommittedBurstSize": frAtmDlciSpCommittedBurstSize,
       "frAtmDlciSpExcessBurstSize": frAtmDlciSpExcessBurstSize,
       "frAtmDlciSpMeasurementInterval": frAtmDlciSpMeasurementInterval,
       "frAtmDlciSpEmissionPriorityToIf": frAtmDlciSpEmissionPriorityToIf,
       "frAtmDlciSpEmissionPrioToIf": frAtmDlciSpEmissionPrioToIf,
       "frAtmDlciSpAccounting": frAtmDlciSpAccounting,
       "frAtmDlciSiwf": frAtmDlciSiwf,
       "frAtmDlciSiwfRowStatusTable": frAtmDlciSiwfRowStatusTable,
       "frAtmDlciSiwfRowStatusEntry": frAtmDlciSiwfRowStatusEntry,
       "frAtmDlciSiwfRowStatus": frAtmDlciSiwfRowStatus,
       "frAtmDlciSiwfComponentName": frAtmDlciSiwfComponentName,
       "frAtmDlciSiwfStorageType": frAtmDlciSiwfStorageType,
       "frAtmDlciSiwfIndex": frAtmDlciSiwfIndex,
       "frAtmDlciSiwfSd": frAtmDlciSiwfSd,
       "frAtmDlciSiwfSdRowStatusTable": frAtmDlciSiwfSdRowStatusTable,
       "frAtmDlciSiwfSdRowStatusEntry": frAtmDlciSiwfSdRowStatusEntry,
       "frAtmDlciSiwfSdRowStatus": frAtmDlciSiwfSdRowStatus,
       "frAtmDlciSiwfSdComponentName": frAtmDlciSiwfSdComponentName,
       "frAtmDlciSiwfSdStorageType": frAtmDlciSiwfSdStorageType,
       "frAtmDlciSiwfSdIndex": frAtmDlciSiwfSdIndex,
       "frAtmDlciSiwfSdProvTable": frAtmDlciSiwfSdProvTable,
       "frAtmDlciSiwfSdProvEntry": frAtmDlciSiwfSdProvEntry,
       "frAtmDlciSiwfSdMode": frAtmDlciSiwfSdMode,
       "frAtmDlciSiwfSdDeToClpMapping": frAtmDlciSiwfSdDeToClpMapping,
       "frAtmDlciSiwfSdClpToDeMapping": frAtmDlciSiwfSdClpToDeMapping,
       "frAtmDlciSiwfSdFecnToEfciMapping": frAtmDlciSiwfSdFecnToEfciMapping,
       "frAtmDlciSiwfSdCrToUuMapping": frAtmDlciSiwfSdCrToUuMapping,
       "frAtmDlciSiwfNPvc": frAtmDlciSiwfNPvc,
       "frAtmDlciSiwfNPvcRowStatusTable": frAtmDlciSiwfNPvcRowStatusTable,
       "frAtmDlciSiwfNPvcRowStatusEntry": frAtmDlciSiwfNPvcRowStatusEntry,
       "frAtmDlciSiwfNPvcRowStatus": frAtmDlciSiwfNPvcRowStatus,
       "frAtmDlciSiwfNPvcComponentName": frAtmDlciSiwfNPvcComponentName,
       "frAtmDlciSiwfNPvcStorageType": frAtmDlciSiwfNPvcStorageType,
       "frAtmDlciSiwfNPvcIndex": frAtmDlciSiwfNPvcIndex,
       "frAtmDlciSiwfNPvcProvTable": frAtmDlciSiwfNPvcProvTable,
       "frAtmDlciSiwfNPvcProvEntry": frAtmDlciSiwfNPvcProvEntry,
       "frAtmDlciSiwfNPvcAtmConnection": frAtmDlciSiwfNPvcAtmConnection,
       "frAtmDlciSiwfNPvcCorrelationTag": frAtmDlciSiwfNPvcCorrelationTag,
       "frAtmDlciSiwfNPvcSiwfNpvcOpTable": frAtmDlciSiwfNPvcSiwfNpvcOpTable,
       "frAtmDlciSiwfNPvcSiwfNpvcOpEntry": frAtmDlciSiwfNPvcSiwfNpvcOpEntry,
       "frAtmDlciSiwfNPvcConnectionToAtm": frAtmDlciSiwfNPvcConnectionToAtm,
       "frAtmDlciSiwfSPvc": frAtmDlciSiwfSPvc,
       "frAtmDlciSiwfSPvcRowStatusTable": frAtmDlciSiwfSPvcRowStatusTable,
       "frAtmDlciSiwfSPvcRowStatusEntry": frAtmDlciSiwfSPvcRowStatusEntry,
       "frAtmDlciSiwfSPvcRowStatus": frAtmDlciSiwfSPvcRowStatus,
       "frAtmDlciSiwfSPvcComponentName": frAtmDlciSiwfSPvcComponentName,
       "frAtmDlciSiwfSPvcStorageType": frAtmDlciSiwfSPvcStorageType,
       "frAtmDlciSiwfSPvcIndex": frAtmDlciSiwfSPvcIndex,
       "frAtmDlciSiwfSPvcProvTable": frAtmDlciSiwfSPvcProvTable,
       "frAtmDlciSiwfSPvcProvEntry": frAtmDlciSiwfSPvcProvEntry,
       "frAtmDlciSiwfSPvcRemoteAddress": frAtmDlciSiwfSPvcRemoteAddress,
       "frAtmDlciSiwfSPvcRemoteConnectionIdentifier": frAtmDlciSiwfSPvcRemoteConnectionIdentifier,
       "frAtmDlciSiwfSPvcCorrelationTag": frAtmDlciSiwfSPvcCorrelationTag,
       "frAtmDlciSiwfQoS": frAtmDlciSiwfQoS,
       "frAtmDlciSiwfQoSRowStatusTable": frAtmDlciSiwfQoSRowStatusTable,
       "frAtmDlciSiwfQoSRowStatusEntry": frAtmDlciSiwfQoSRowStatusEntry,
       "frAtmDlciSiwfQoSRowStatus": frAtmDlciSiwfQoSRowStatus,
       "frAtmDlciSiwfQoSComponentName": frAtmDlciSiwfQoSComponentName,
       "frAtmDlciSiwfQoSStorageType": frAtmDlciSiwfQoSStorageType,
       "frAtmDlciSiwfQoSIndex": frAtmDlciSiwfQoSIndex,
       "frAtmDlciSiwfQoSProvTable": frAtmDlciSiwfQoSProvTable,
       "frAtmDlciSiwfQoSProvEntry": frAtmDlciSiwfQoSProvEntry,
       "frAtmDlciSiwfQoSEmissionPriorityToIf": frAtmDlciSiwfQoSEmissionPriorityToIf,
       "frAtmDlciSiwfQoSTransferPriority": frAtmDlciSiwfQoSTransferPriority,
       "frAtmDlciSiwfAtmCon": frAtmDlciSiwfAtmCon,
       "frAtmDlciSiwfAtmConRowStatusTable": frAtmDlciSiwfAtmConRowStatusTable,
       "frAtmDlciSiwfAtmConRowStatusEntry": frAtmDlciSiwfAtmConRowStatusEntry,
       "frAtmDlciSiwfAtmConRowStatus": frAtmDlciSiwfAtmConRowStatus,
       "frAtmDlciSiwfAtmConComponentName": frAtmDlciSiwfAtmConComponentName,
       "frAtmDlciSiwfAtmConStorageType": frAtmDlciSiwfAtmConStorageType,
       "frAtmDlciSiwfAtmConIndex": frAtmDlciSiwfAtmConIndex,
       "frAtmDlciSiwfAtmConOperTable": frAtmDlciSiwfAtmConOperTable,
       "frAtmDlciSiwfAtmConOperEntry": frAtmDlciSiwfAtmConOperEntry,
       "frAtmDlciSiwfAtmConNextHop": frAtmDlciSiwfAtmConNextHop,
       "frAtmDlciSiwfConnOpTable": frAtmDlciSiwfConnOpTable,
       "frAtmDlciSiwfConnOpEntry": frAtmDlciSiwfConnOpEntry,
       "frAtmDlciSiwfDiscardPriority": frAtmDlciSiwfDiscardPriority,
       "frAtmDlciSiwfAtmServiceCategory": frAtmDlciSiwfAtmServiceCategory,
       "frAtmDlciSiwfTrafficParmConvPolicy": frAtmDlciSiwfTrafficParmConvPolicy,
       "frAtmDlciSiwfAvgFrameSize": frAtmDlciSiwfAvgFrameSize,
       "frAtmDlciSiwfRemoteAddress": frAtmDlciSiwfRemoteAddress,
       "frAtmDlciSiwfRemoteConnectionIdentifier": frAtmDlciSiwfRemoteConnectionIdentifier,
       "frAtmDlciSiwfSdOpTable": frAtmDlciSiwfSdOpTable,
       "frAtmDlciSiwfSdOpEntry": frAtmDlciSiwfSdOpEntry,
       "frAtmDlciSiwfMode": frAtmDlciSiwfMode,
       "frAtmDlciSiwfDeToClpMapping": frAtmDlciSiwfDeToClpMapping,
       "frAtmDlciSiwfClpToDeMapping": frAtmDlciSiwfClpToDeMapping,
       "frAtmDlciSiwfFecnToEfciMapping": frAtmDlciSiwfFecnToEfciMapping,
       "frAtmDlciSiwfCrToUuMapping": frAtmDlciSiwfCrToUuMapping,
       "frAtmDlciSiwfTransferPriority": frAtmDlciSiwfTransferPriority,
       "frAtmDlciSiwfAssignedBandwidthPool": frAtmDlciSiwfAssignedBandwidthPool,
       "frAtmDlciSiwfSiwfSpvcOpTable": frAtmDlciSiwfSiwfSpvcOpTable,
       "frAtmDlciSiwfSiwfSpvcOpEntry": frAtmDlciSiwfSiwfSpvcOpEntry,
       "frAtmDlciSiwfPeakCellRate0": frAtmDlciSiwfPeakCellRate0,
       "frAtmDlciSiwfPeakCellRate01": frAtmDlciSiwfPeakCellRate01,
       "frAtmDlciSiwfSustainedCellRate0": frAtmDlciSiwfSustainedCellRate0,
       "frAtmDlciSiwfSustainedCellRate01": frAtmDlciSiwfSustainedCellRate01,
       "frAtmDlciSiwfMaximumBurstSize0": frAtmDlciSiwfMaximumBurstSize0,
       "frAtmDlciSiwfMaximumBurstSize01": frAtmDlciSiwfMaximumBurstSize01,
       "frAtmDlciSiwfEquivalentBitRate": frAtmDlciSiwfEquivalentBitRate,
       "frAtmDlciSiwfType": frAtmDlciSiwfType,
       "frAtmDlciSiwfVccClearCause": frAtmDlciSiwfVccClearCause,
       "frAtmDlciSiwfVccCauseDiag": frAtmDlciSiwfVccCauseDiag,
       "frAtmDlciSiwfStatsTable": frAtmDlciSiwfStatsTable,
       "frAtmDlciSiwfStatsEntry": frAtmDlciSiwfStatsEntry,
       "frAtmDlciSiwfUnknown1490Frames": frAtmDlciSiwfUnknown1490Frames,
       "frAtmDlciSiwfInvalid1490Frames": frAtmDlciSiwfInvalid1490Frames,
       "frAtmDlciSiwfLastUnknown1490ProtocolHeader": frAtmDlciSiwfLastUnknown1490ProtocolHeader,
       "frAtmDlciSiwfUnknown1483Frames": frAtmDlciSiwfUnknown1483Frames,
       "frAtmDlciSiwfInvalid1483Frames": frAtmDlciSiwfInvalid1483Frames,
       "frAtmDlciSiwfLastUnknown1483ProtocolHeader": frAtmDlciSiwfLastUnknown1483ProtocolHeader,
       "frAtmDlciNiwf": frAtmDlciNiwf,
       "frAtmDlciNiwfRowStatusTable": frAtmDlciNiwfRowStatusTable,
       "frAtmDlciNiwfRowStatusEntry": frAtmDlciNiwfRowStatusEntry,
       "frAtmDlciNiwfRowStatus": frAtmDlciNiwfRowStatus,
       "frAtmDlciNiwfComponentName": frAtmDlciNiwfComponentName,
       "frAtmDlciNiwfStorageType": frAtmDlciNiwfStorageType,
       "frAtmDlciNiwfIndex": frAtmDlciNiwfIndex,
       "frAtmDlciNiwfSpvc": frAtmDlciNiwfSpvc,
       "frAtmDlciNiwfSpvcRowStatusTable": frAtmDlciNiwfSpvcRowStatusTable,
       "frAtmDlciNiwfSpvcRowStatusEntry": frAtmDlciNiwfSpvcRowStatusEntry,
       "frAtmDlciNiwfSpvcRowStatus": frAtmDlciNiwfSpvcRowStatus,
       "frAtmDlciNiwfSpvcComponentName": frAtmDlciNiwfSpvcComponentName,
       "frAtmDlciNiwfSpvcStorageType": frAtmDlciNiwfSpvcStorageType,
       "frAtmDlciNiwfSpvcIndex": frAtmDlciNiwfSpvcIndex,
       "frAtmDlciNiwfSpvcProvTable": frAtmDlciNiwfSpvcProvTable,
       "frAtmDlciNiwfSpvcProvEntry": frAtmDlciNiwfSpvcProvEntry,
       "frAtmDlciNiwfSpvcRemoteAddress": frAtmDlciNiwfSpvcRemoteAddress,
       "frAtmDlciNiwfSpvcRemoteDlci": frAtmDlciNiwfSpvcRemoteDlci,
       "frAtmDlciNiwfSpvcCorrelationTag": frAtmDlciNiwfSpvcCorrelationTag,
       "frAtmDlciNiwfNd": frAtmDlciNiwfNd,
       "frAtmDlciNiwfNdRowStatusTable": frAtmDlciNiwfNdRowStatusTable,
       "frAtmDlciNiwfNdRowStatusEntry": frAtmDlciNiwfNdRowStatusEntry,
       "frAtmDlciNiwfNdRowStatus": frAtmDlciNiwfNdRowStatus,
       "frAtmDlciNiwfNdComponentName": frAtmDlciNiwfNdComponentName,
       "frAtmDlciNiwfNdStorageType": frAtmDlciNiwfNdStorageType,
       "frAtmDlciNiwfNdIndex": frAtmDlciNiwfNdIndex,
       "frAtmDlciNiwfNdProvTable": frAtmDlciNiwfNdProvTable,
       "frAtmDlciNiwfNdProvEntry": frAtmDlciNiwfNdProvEntry,
       "frAtmDlciNiwfNdDeToClpMapping": frAtmDlciNiwfNdDeToClpMapping,
       "frAtmDlciNiwfNdClpToDeMapping": frAtmDlciNiwfNdClpToDeMapping,
       "frAtmDlciNiwfNdTransferPriority": frAtmDlciNiwfNdTransferPriority,
       "frAtmDlciNiwfQoS": frAtmDlciNiwfQoS,
       "frAtmDlciNiwfQoSRowStatusTable": frAtmDlciNiwfQoSRowStatusTable,
       "frAtmDlciNiwfQoSRowStatusEntry": frAtmDlciNiwfQoSRowStatusEntry,
       "frAtmDlciNiwfQoSRowStatus": frAtmDlciNiwfQoSRowStatus,
       "frAtmDlciNiwfQoSComponentName": frAtmDlciNiwfQoSComponentName,
       "frAtmDlciNiwfQoSStorageType": frAtmDlciNiwfQoSStorageType,
       "frAtmDlciNiwfQoSIndex": frAtmDlciNiwfQoSIndex,
       "frAtmDlciNiwfQoSProvTable": frAtmDlciNiwfQoSProvTable,
       "frAtmDlciNiwfQoSProvEntry": frAtmDlciNiwfQoSProvEntry,
       "frAtmDlciNiwfQoSEmissionPriorityToIf": frAtmDlciNiwfQoSEmissionPriorityToIf,
       "frAtmDlciNiwfQoSTransferPriority": frAtmDlciNiwfQoSTransferPriority,
       "frAtmDlciNiwfOperTable": frAtmDlciNiwfOperTable,
       "frAtmDlciNiwfOperEntry": frAtmDlciNiwfOperEntry,
       "frAtmDlciNiwfDeToClpMapping": frAtmDlciNiwfDeToClpMapping,
       "frAtmDlciNiwfClpToDeMapping": frAtmDlciNiwfClpToDeMapping,
       "frAtmDlciNiwfTransferPriority": frAtmDlciNiwfTransferPriority,
       "frAtmDlciNiwfAtmServiceCategory": frAtmDlciNiwfAtmServiceCategory,
       "frAtmDlciNiwfTrafficParmConvPolicy": frAtmDlciNiwfTrafficParmConvPolicy,
       "frAtmDlciNiwfAvgFrameSize": frAtmDlciNiwfAvgFrameSize,
       "frAtmDlciNiwfEquivalentBitRate": frAtmDlciNiwfEquivalentBitRate,
       "frAtmDlciNiwfAtmDlci": frAtmDlciNiwfAtmDlci,
       "frAtmDlciNiwfAssignedBandwidthPool": frAtmDlciNiwfAssignedBandwidthPool,
       "frAtmDlciEgSp": frAtmDlciEgSp,
       "frAtmDlciEgSpRowStatusTable": frAtmDlciEgSpRowStatusTable,
       "frAtmDlciEgSpRowStatusEntry": frAtmDlciEgSpRowStatusEntry,
       "frAtmDlciEgSpRowStatus": frAtmDlciEgSpRowStatus,
       "frAtmDlciEgSpComponentName": frAtmDlciEgSpComponentName,
       "frAtmDlciEgSpStorageType": frAtmDlciEgSpStorageType,
       "frAtmDlciEgSpIndex": frAtmDlciEgSpIndex,
       "frAtmDlciEgSpProvTable": frAtmDlciEgSpProvTable,
       "frAtmDlciEgSpProvEntry": frAtmDlciEgSpProvEntry,
       "frAtmDlciEgSpCommittedInformationRate": frAtmDlciEgSpCommittedInformationRate,
       "frAtmDlciEgSpCommittedBurstSize": frAtmDlciEgSpCommittedBurstSize,
       "frAtmDlciEgSpExcessBurstSize": frAtmDlciEgSpExcessBurstSize,
       "frAtmDlciEgSpMeasurementInterval": frAtmDlciEgSpMeasurementInterval,
       "frAtmDlciStateTable": frAtmDlciStateTable,
       "frAtmDlciStateEntry": frAtmDlciStateEntry,
       "frAtmDlciAdminState": frAtmDlciAdminState,
       "frAtmDlciOperationalState": frAtmDlciOperationalState,
       "frAtmDlciUsageState": frAtmDlciUsageState,
       "frAtmDlciABitTable": frAtmDlciABitTable,
       "frAtmDlciABitEntry": frAtmDlciABitEntry,
       "frAtmDlciABitStatusToIf": frAtmDlciABitStatusToIf,
       "frAtmDlciABitReasonToIf": frAtmDlciABitReasonToIf,
       "frAtmDlciABitStatusFromIf": frAtmDlciABitStatusFromIf,
       "frAtmDlciABitReasonFromIf": frAtmDlciABitReasonFromIf,
       "frAtmDlciSpOpTable": frAtmDlciSpOpTable,
       "frAtmDlciSpOpEntry": frAtmDlciSpOpEntry,
       "frAtmDlciMaximumFrameSize": frAtmDlciMaximumFrameSize,
       "frAtmDlciRateEnforcement": frAtmDlciRateEnforcement,
       "frAtmDlciCommittedInformationRate": frAtmDlciCommittedInformationRate,
       "frAtmDlciCommittedBurstSize": frAtmDlciCommittedBurstSize,
       "frAtmDlciExcessBurstSize": frAtmDlciExcessBurstSize,
       "frAtmDlciMeasurementInterval": frAtmDlciMeasurementInterval,
       "frAtmDlciEmissionPriorityToIf": frAtmDlciEmissionPriorityToIf,
       "frAtmDlciDlciType": frAtmDlciDlciType,
       "frAtmDlciTroubled": frAtmDlciTroubled,
       "frAtmDlciTroubledReason": frAtmDlciTroubledReason,
       "frAtmDlciStatsTable": frAtmDlciStatsTable,
       "frAtmDlciStatsEntry": frAtmDlciStatsEntry,
       "frAtmDlciFrmToIf": frAtmDlciFrmToIf,
       "frAtmDlciFecnFrmToIf": frAtmDlciFecnFrmToIf,
       "frAtmDlciBecnFrmToIf": frAtmDlciBecnFrmToIf,
       "frAtmDlciDeFrmToIf": frAtmDlciDeFrmToIf,
       "frAtmDlciDiscCongestedToIf": frAtmDlciDiscCongestedToIf,
       "frAtmDlciDiscDeCongestedToIf": frAtmDlciDiscDeCongestedToIf,
       "frAtmDlciFrmFromIf": frAtmDlciFrmFromIf,
       "frAtmDlciFecnFrmFromIf": frAtmDlciFecnFrmFromIf,
       "frAtmDlciBecnFrmFromIf": frAtmDlciBecnFrmFromIf,
       "frAtmDlciEfciFrmFromNetwork": frAtmDlciEfciFrmFromNetwork,
       "frAtmDlciDeFrmFromIf": frAtmDlciDeFrmFromIf,
       "frAtmDlciExcessFrmFromIf": frAtmDlciExcessFrmFromIf,
       "frAtmDlciDiscExcessFromIf": frAtmDlciDiscExcessFromIf,
       "frAtmDlciDiscFrameAbit": frAtmDlciDiscFrameAbit,
       "frAtmDlciDiscCongestedFromIf": frAtmDlciDiscCongestedFromIf,
       "frAtmDlciDiscDeCongestedFromIf": frAtmDlciDiscDeCongestedFromIf,
       "frAtmDlciErrorShortFrmFromIf": frAtmDlciErrorShortFrmFromIf,
       "frAtmDlciErrorLongFrmFromIf": frAtmDlciErrorLongFrmFromIf,
       "frAtmDlciBecnFrmSetByService": frAtmDlciBecnFrmSetByService,
       "frAtmDlciBytesToIf": frAtmDlciBytesToIf,
       "frAtmDlciDeBytesToIf": frAtmDlciDeBytesToIf,
       "frAtmDlciDiscCongestedToIfBytes": frAtmDlciDiscCongestedToIfBytes,
       "frAtmDlciDiscDeCongestedToIfBytes": frAtmDlciDiscDeCongestedToIfBytes,
       "frAtmDlciBytesFromIf": frAtmDlciBytesFromIf,
       "frAtmDlciDeBytesFromIf": frAtmDlciDeBytesFromIf,
       "frAtmDlciExcessBytesFromIf": frAtmDlciExcessBytesFromIf,
       "frAtmDlciDiscExcessFromIfBytes": frAtmDlciDiscExcessFromIfBytes,
       "frAtmDlciDiscByteAbit": frAtmDlciDiscByteAbit,
       "frAtmDlciDiscCongestedFromIfBytes": frAtmDlciDiscCongestedFromIfBytes,
       "frAtmDlciDiscDeCongestedFromIfBytes": frAtmDlciDiscDeCongestedFromIfBytes,
       "frAtmDlciErrorShortBytesFromIf": frAtmDlciErrorShortBytesFromIf,
       "frAtmDlciErrorLongBytesFromIf": frAtmDlciErrorLongBytesFromIf,
       "frAtmDlciCalldTable": frAtmDlciCalldTable,
       "frAtmDlciCalldEntry": frAtmDlciCalldEntry,
       "frAtmDlciAccountingEnabled": frAtmDlciAccountingEnabled,
       "frAtmDlciAccountingEnd": frAtmDlciAccountingEnd,
       "frAtmDlciCorrelationTag": frAtmDlciCorrelationTag,
       "frAtmDlciIntTable": frAtmDlciIntTable,
       "frAtmDlciIntEntry": frAtmDlciIntEntry,
       "frAtmDlciStartTime": frAtmDlciStartTime,
       "frAtmDlciTotalIngressBytes": frAtmDlciTotalIngressBytes,
       "frAtmDlciTotalEgressBytes": frAtmDlciTotalEgressBytes,
       "frAtmDlciEirIngressBytes": frAtmDlciEirIngressBytes,
       "frAtmDlciEirEgressBytes": frAtmDlciEirEgressBytes,
       "frAtmDlciDiscardedBytes": frAtmDlciDiscardedBytes,
       "frAtmDlciTotalIngressFrames": frAtmDlciTotalIngressFrames,
       "frAtmDlciTotalEgressFrames": frAtmDlciTotalEgressFrames,
       "frAtmDlciEirIngressFrames": frAtmDlciEirIngressFrames,
       "frAtmDlciEirEgressFrames": frAtmDlciEirEgressFrames,
       "frAtmDlciDiscardedFrames": frAtmDlciDiscardedFrames,
       "frAtmDlciElapsedDifference": frAtmDlciElapsedDifference,
       "frAtmVFramer": frAtmVFramer,
       "frAtmVFramerRowStatusTable": frAtmVFramerRowStatusTable,
       "frAtmVFramerRowStatusEntry": frAtmVFramerRowStatusEntry,
       "frAtmVFramerRowStatus": frAtmVFramerRowStatus,
       "frAtmVFramerComponentName": frAtmVFramerComponentName,
       "frAtmVFramerStorageType": frAtmVFramerStorageType,
       "frAtmVFramerIndex": frAtmVFramerIndex,
       "frAtmVFramerProvTable": frAtmVFramerProvTable,
       "frAtmVFramerProvEntry": frAtmVFramerProvEntry,
       "frAtmVFramerOtherVirtualFramer": frAtmVFramerOtherVirtualFramer,
       "frAtmVFramerLogicalProcessor": frAtmVFramerLogicalProcessor,
       "frAtmVFramerStateTable": frAtmVFramerStateTable,
       "frAtmVFramerStateEntry": frAtmVFramerStateEntry,
       "frAtmVFramerAdminState": frAtmVFramerAdminState,
       "frAtmVFramerOperationalState": frAtmVFramerOperationalState,
       "frAtmVFramerUsageState": frAtmVFramerUsageState,
       "frAtmVFramerStatsTable": frAtmVFramerStatsTable,
       "frAtmVFramerStatsEntry": frAtmVFramerStatsEntry,
       "frAtmVFramerFrmToOtherVFramer": frAtmVFramerFrmToOtherVFramer,
       "frAtmVFramerFrmFromOtherVFramer": frAtmVFramerFrmFromOtherVFramer,
       "frAtmVFramerOctetFromOtherVFramer": frAtmVFramerOctetFromOtherVFramer,
       "frAtmAddr": frAtmAddr,
       "frAtmAddrRowStatusTable": frAtmAddrRowStatusTable,
       "frAtmAddrRowStatusEntry": frAtmAddrRowStatusEntry,
       "frAtmAddrRowStatus": frAtmAddrRowStatus,
       "frAtmAddrComponentName": frAtmAddrComponentName,
       "frAtmAddrStorageType": frAtmAddrStorageType,
       "frAtmAddrIndex": frAtmAddrIndex,
       "frAtmAddrProvTable": frAtmAddrProvTable,
       "frAtmAddrProvEntry": frAtmAddrProvEntry,
       "frAtmAddrAddress": frAtmAddrAddress,
       "frAtmAddrAddrOpTable": frAtmAddrAddrOpTable,
       "frAtmAddrAddrOpEntry": frAtmAddrAddrOpEntry,
       "frAtmAddrMyAddress": frAtmAddrMyAddress,
       "frAtmCa": frAtmCa,
       "frAtmCaRowStatusTable": frAtmCaRowStatusTable,
       "frAtmCaRowStatusEntry": frAtmCaRowStatusEntry,
       "frAtmCaRowStatus": frAtmCaRowStatus,
       "frAtmCaComponentName": frAtmCaComponentName,
       "frAtmCaStorageType": frAtmCaStorageType,
       "frAtmCaIndex": frAtmCaIndex,
       "frAtmCaTpm": frAtmCaTpm,
       "frAtmCaTpmRowStatusTable": frAtmCaTpmRowStatusTable,
       "frAtmCaTpmRowStatusEntry": frAtmCaTpmRowStatusEntry,
       "frAtmCaTpmRowStatus": frAtmCaTpmRowStatus,
       "frAtmCaTpmComponentName": frAtmCaTpmComponentName,
       "frAtmCaTpmStorageType": frAtmCaTpmStorageType,
       "frAtmCaTpmIndex": frAtmCaTpmIndex,
       "frAtmCaTpmProvTable": frAtmCaTpmProvTable,
       "frAtmCaTpmProvEntry": frAtmCaTpmProvEntry,
       "frAtmCaTpmAssignedBandwidthPool": frAtmCaTpmAssignedBandwidthPool,
       "frAtmCaTpmTrafficParmConvPolicy": frAtmCaTpmTrafficParmConvPolicy,
       "frAtmCaTpmAverageFrameSize": frAtmCaTpmAverageFrameSize,
       "frAtmCaProvTable": frAtmCaProvTable,
       "frAtmCaProvEntry": frAtmCaProvEntry,
       "frAtmCaCallAdmissionControl": frAtmCaCallAdmissionControl,
       "frAtmCaOverrideLinkRate": frAtmCaOverrideLinkRate,
       "frAtmCaSdTable": frAtmCaSdTable,
       "frAtmCaSdEntry": frAtmCaSdEntry,
       "frAtmCaSdMode": frAtmCaSdMode,
       "frAtmCaSdDeToClpMapping": frAtmCaSdDeToClpMapping,
       "frAtmCaSdClpToDeMapping": frAtmCaSdClpToDeMapping,
       "frAtmCaSdFecnToEfciMapping": frAtmCaSdFecnToEfciMapping,
       "frAtmCaSdCrToUuMapping": frAtmCaSdCrToUuMapping,
       "frAtmCaNdTable": frAtmCaNdTable,
       "frAtmCaNdEntry": frAtmCaNdEntry,
       "frAtmCaNdDeToClpMapping": frAtmCaNdDeToClpMapping,
       "frAtmCaNdClpToDeMapping": frAtmCaNdClpToDeMapping,
       "frAtmCaIfQoSTable": frAtmCaIfQoSTable,
       "frAtmCaIfQoSEntry": frAtmCaIfQoSEntry,
       "frAtmCaSiwfEmissionPriorityToIf": frAtmCaSiwfEmissionPriorityToIf,
       "frAtmCaSiwfTransferPriority": frAtmCaSiwfTransferPriority,
       "frAtmCaNiwfEmissionPriorityToIf": frAtmCaNiwfEmissionPriorityToIf,
       "frAtmCaNiwfTransferPriority": frAtmCaNiwfTransferPriority,
       "frAtmCaOpTable": frAtmCaOpTable,
       "frAtmCaOpEntry": frAtmCaOpEntry,
       "frAtmCaLinkRate": frAtmCaLinkRate,
       "frAtmCaNailedUpPvcs": frAtmCaNailedUpPvcs,
       "frAtmCaTroubledDlcis": frAtmCaTroubledDlcis,
       "frAtmCaSoftPvcs": frAtmCaSoftPvcs,
       "frAtmCaAccountingOptionsTable": frAtmCaAccountingOptionsTable,
       "frAtmCaAccountingOptionsEntry": frAtmCaAccountingOptionsEntry,
       "frAtmCaAccountClass": frAtmCaAccountClass,
       "frAtmCaAccountCollection": frAtmCaAccountCollection,
       "frAtmCaServiceExchange": frAtmCaServiceExchange,
       "frAtmCaBwPoolTable": frAtmCaBwPoolTable,
       "frAtmCaBwPoolEntry": frAtmCaBwPoolEntry,
       "frAtmCaBwPoolIndex": frAtmCaBwPoolIndex,
       "frAtmCaBwPoolValue": frAtmCaBwPoolValue,
       "frAtmCaPoolProvBwTable": frAtmCaPoolProvBwTable,
       "frAtmCaPoolProvBwEntry": frAtmCaPoolProvBwEntry,
       "frAtmCaPoolProvBwIndex": frAtmCaPoolProvBwIndex,
       "frAtmCaPoolProvBwValue": frAtmCaPoolProvBwValue,
       "frAtmCaPoolAvailBwTable": frAtmCaPoolAvailBwTable,
       "frAtmCaPoolAvailBwEntry": frAtmCaPoolAvailBwEntry,
       "frAtmCaPoolAvailBwIndex": frAtmCaPoolAvailBwIndex,
       "frAtmCaPoolAvailBwValue": frAtmCaPoolAvailBwValue,
       "frAtmCaPoolAdmitBwTable": frAtmCaPoolAdmitBwTable,
       "frAtmCaPoolAdmitBwEntry": frAtmCaPoolAdmitBwEntry,
       "frAtmCaPoolAdmitBwIndex": frAtmCaPoolAdmitBwIndex,
       "frAtmCaPoolAdmitBwValue": frAtmCaPoolAdmitBwValue,
       "frAtmCidDataTable": frAtmCidDataTable,
       "frAtmCidDataEntry": frAtmCidDataEntry,
       "frAtmCustomerIdentifier": frAtmCustomerIdentifier,
       "frAtmStateTable": frAtmStateTable,
       "frAtmStateEntry": frAtmStateEntry,
       "frAtmAdminState": frAtmAdminState,
       "frAtmOperationalState": frAtmOperationalState,
       "frAtmUsageState": frAtmUsageState,
       "frAtmAvailabilityStatus": frAtmAvailabilityStatus,
       "frAtmProceduralStatus": frAtmProceduralStatus,
       "frAtmControlStatus": frAtmControlStatus,
       "frAtmAlarmStatus": frAtmAlarmStatus,
       "frAtmStandbyStatus": frAtmStandbyStatus,
       "frAtmUnknownStatus": frAtmUnknownStatus,
       "frAtmStatsTable": frAtmStatsTable,
       "frAtmStatsEntry": frAtmStatsEntry,
       "frAtmLastUnknownDlci": frAtmLastUnknownDlci,
       "frAtmUnknownDlciFramesFromIf": frAtmUnknownDlciFramesFromIf,
       "frAtmInvalidHeaderFramesFromIf": frAtmInvalidHeaderFramesFromIf,
       "frAtmIfEntryTable": frAtmIfEntryTable,
       "frAtmIfEntryEntry": frAtmIfEntryEntry,
       "frAtmIfAdminStatus": frAtmIfAdminStatus,
       "frAtmIfIndex": frAtmIfIndex,
       "frAtmOperStatusTable": frAtmOperStatusTable,
       "frAtmOperStatusEntry": frAtmOperStatusEntry,
       "frAtmSnmpOperStatus": frAtmSnmpOperStatus,
       "frAtmEmissionPriorityQsTable": frAtmEmissionPriorityQsTable,
       "frAtmEmissionPriorityQsEntry": frAtmEmissionPriorityQsEntry,
       "frAtmNumberOfEmissionQs": frAtmNumberOfEmissionQs,
       "frAtmFrmToIfByQueueTable": frAtmFrmToIfByQueueTable,
       "frAtmFrmToIfByQueueEntry": frAtmFrmToIfByQueueEntry,
       "frAtmFrmToIfByQueueIndex": frAtmFrmToIfByQueueIndex,
       "frAtmFrmToIfByQueueValue": frAtmFrmToIfByQueueValue,
       "frAtmOctetToIfByQueueTable": frAtmOctetToIfByQueueTable,
       "frAtmOctetToIfByQueueEntry": frAtmOctetToIfByQueueEntry,
       "frAtmOctetToIfByQueueIndex": frAtmOctetToIfByQueueIndex,
       "frAtmOctetToIfByQueueValue": frAtmOctetToIfByQueueValue,
       "frameRelayAtmMIB": frameRelayAtmMIB,
       "frameRelayAtmGroup": frameRelayAtmGroup,
       "frameRelayAtmGroupBE": frameRelayAtmGroupBE,
       "frameRelayAtmGroupBE01": frameRelayAtmGroupBE01,
       "frameRelayAtmGroupBE01A": frameRelayAtmGroupBE01A,
       "frameRelayAtmCapabilities": frameRelayAtmCapabilities,
       "frameRelayAtmCapabilitiesBE": frameRelayAtmCapabilitiesBE,
       "frameRelayAtmCapabilitiesBE01": frameRelayAtmCapabilitiesBE01,
       "frameRelayAtmCapabilitiesBE01A": frameRelayAtmCapabilitiesBE01A}
)
