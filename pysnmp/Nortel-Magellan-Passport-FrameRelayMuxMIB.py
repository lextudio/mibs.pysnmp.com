# SNMP MIB module (Nortel-Magellan-Passport-FrameRelayMuxMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrameRelayMuxMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:47 2024
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

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
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

_FrMux_ObjectIdentity = ObjectIdentity
frMux = _FrMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112)
)
_FrMuxRowStatusTable_Object = MibTable
frMuxRowStatusTable = _FrMuxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 1)
)
if mibBuilder.loadTexts:
    frMuxRowStatusTable.setStatus("mandatory")
_FrMuxRowStatusEntry_Object = MibTableRow
frMuxRowStatusEntry = _FrMuxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 1, 1)
)
frMuxRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
)
if mibBuilder.loadTexts:
    frMuxRowStatusEntry.setStatus("mandatory")
_FrMuxRowStatus_Type = RowStatus
_FrMuxRowStatus_Object = MibTableColumn
frMuxRowStatus = _FrMuxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 1, 1, 1),
    _FrMuxRowStatus_Type()
)
frMuxRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxRowStatus.setStatus("mandatory")
_FrMuxComponentName_Type = DisplayString
_FrMuxComponentName_Object = MibTableColumn
frMuxComponentName = _FrMuxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 1, 1, 2),
    _FrMuxComponentName_Type()
)
frMuxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxComponentName.setStatus("mandatory")
_FrMuxStorageType_Type = StorageType
_FrMuxStorageType_Object = MibTableColumn
frMuxStorageType = _FrMuxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 1, 1, 4),
    _FrMuxStorageType_Type()
)
frMuxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxStorageType.setStatus("mandatory")


class _FrMuxIndex_Type(Integer32):
    """Custom type frMuxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrMuxIndex_Type.__name__ = "Integer32"
_FrMuxIndex_Object = MibTableColumn
frMuxIndex = _FrMuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 1, 1, 10),
    _FrMuxIndex_Type()
)
frMuxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frMuxIndex.setStatus("mandatory")
_FrMuxFramer_ObjectIdentity = ObjectIdentity
frMuxFramer = _FrMuxFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2)
)
_FrMuxFramerRowStatusTable_Object = MibTable
frMuxFramerRowStatusTable = _FrMuxFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 1)
)
if mibBuilder.loadTexts:
    frMuxFramerRowStatusTable.setStatus("mandatory")
_FrMuxFramerRowStatusEntry_Object = MibTableRow
frMuxFramerRowStatusEntry = _FrMuxFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 1, 1)
)
frMuxFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    frMuxFramerRowStatusEntry.setStatus("mandatory")
_FrMuxFramerRowStatus_Type = RowStatus
_FrMuxFramerRowStatus_Object = MibTableColumn
frMuxFramerRowStatus = _FrMuxFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 1, 1, 1),
    _FrMuxFramerRowStatus_Type()
)
frMuxFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerRowStatus.setStatus("mandatory")
_FrMuxFramerComponentName_Type = DisplayString
_FrMuxFramerComponentName_Object = MibTableColumn
frMuxFramerComponentName = _FrMuxFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 1, 1, 2),
    _FrMuxFramerComponentName_Type()
)
frMuxFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerComponentName.setStatus("mandatory")
_FrMuxFramerStorageType_Type = StorageType
_FrMuxFramerStorageType_Object = MibTableColumn
frMuxFramerStorageType = _FrMuxFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 1, 1, 4),
    _FrMuxFramerStorageType_Type()
)
frMuxFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerStorageType.setStatus("mandatory")
_FrMuxFramerIndex_Type = NonReplicated
_FrMuxFramerIndex_Object = MibTableColumn
frMuxFramerIndex = _FrMuxFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 1, 1, 10),
    _FrMuxFramerIndex_Type()
)
frMuxFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frMuxFramerIndex.setStatus("mandatory")
_FrMuxFramerProvTable_Object = MibTable
frMuxFramerProvTable = _FrMuxFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 10)
)
if mibBuilder.loadTexts:
    frMuxFramerProvTable.setStatus("mandatory")
_FrMuxFramerProvEntry_Object = MibTableRow
frMuxFramerProvEntry = _FrMuxFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 10, 1)
)
frMuxFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    frMuxFramerProvEntry.setStatus("mandatory")
_FrMuxFramerInterfaceName_Type = Link
_FrMuxFramerInterfaceName_Object = MibTableColumn
frMuxFramerInterfaceName = _FrMuxFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 10, 1, 1),
    _FrMuxFramerInterfaceName_Type()
)
frMuxFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxFramerInterfaceName.setStatus("mandatory")
_FrMuxFramerLinkTable_Object = MibTable
frMuxFramerLinkTable = _FrMuxFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 11)
)
if mibBuilder.loadTexts:
    frMuxFramerLinkTable.setStatus("mandatory")
_FrMuxFramerLinkEntry_Object = MibTableRow
frMuxFramerLinkEntry = _FrMuxFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 11, 1)
)
frMuxFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    frMuxFramerLinkEntry.setStatus("mandatory")


class _FrMuxFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type frMuxFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FrMuxFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_FrMuxFramerFlagsBetweenFrames_Object = MibTableColumn
frMuxFramerFlagsBetweenFrames = _FrMuxFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 11, 1, 4),
    _FrMuxFramerFlagsBetweenFrames_Type()
)
frMuxFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxFramerFlagsBetweenFrames.setStatus("mandatory")
_FrMuxFramerStateTable_Object = MibTable
frMuxFramerStateTable = _FrMuxFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 12)
)
if mibBuilder.loadTexts:
    frMuxFramerStateTable.setStatus("mandatory")
_FrMuxFramerStateEntry_Object = MibTableRow
frMuxFramerStateEntry = _FrMuxFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 12, 1)
)
frMuxFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    frMuxFramerStateEntry.setStatus("mandatory")


class _FrMuxFramerAdminState_Type(Integer32):
    """Custom type frMuxFramerAdminState based on Integer32"""
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


_FrMuxFramerAdminState_Type.__name__ = "Integer32"
_FrMuxFramerAdminState_Object = MibTableColumn
frMuxFramerAdminState = _FrMuxFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 12, 1, 1),
    _FrMuxFramerAdminState_Type()
)
frMuxFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerAdminState.setStatus("mandatory")


class _FrMuxFramerOperationalState_Type(Integer32):
    """Custom type frMuxFramerOperationalState based on Integer32"""
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


_FrMuxFramerOperationalState_Type.__name__ = "Integer32"
_FrMuxFramerOperationalState_Object = MibTableColumn
frMuxFramerOperationalState = _FrMuxFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 12, 1, 2),
    _FrMuxFramerOperationalState_Type()
)
frMuxFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerOperationalState.setStatus("mandatory")


class _FrMuxFramerUsageState_Type(Integer32):
    """Custom type frMuxFramerUsageState based on Integer32"""
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


_FrMuxFramerUsageState_Type.__name__ = "Integer32"
_FrMuxFramerUsageState_Object = MibTableColumn
frMuxFramerUsageState = _FrMuxFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 12, 1, 3),
    _FrMuxFramerUsageState_Type()
)
frMuxFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerUsageState.setStatus("mandatory")
_FrMuxFramerStatsTable_Object = MibTable
frMuxFramerStatsTable = _FrMuxFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13)
)
if mibBuilder.loadTexts:
    frMuxFramerStatsTable.setStatus("mandatory")
_FrMuxFramerStatsEntry_Object = MibTableRow
frMuxFramerStatsEntry = _FrMuxFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1)
)
frMuxFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    frMuxFramerStatsEntry.setStatus("mandatory")
_FrMuxFramerFrmToIf_Type = Counter32
_FrMuxFramerFrmToIf_Object = MibTableColumn
frMuxFramerFrmToIf = _FrMuxFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 1),
    _FrMuxFramerFrmToIf_Type()
)
frMuxFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerFrmToIf.setStatus("mandatory")
_FrMuxFramerFrmFromIf_Type = Counter32
_FrMuxFramerFrmFromIf_Object = MibTableColumn
frMuxFramerFrmFromIf = _FrMuxFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 2),
    _FrMuxFramerFrmFromIf_Type()
)
frMuxFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerFrmFromIf.setStatus("mandatory")
_FrMuxFramerOctetFromIf_Type = Counter32
_FrMuxFramerOctetFromIf_Object = MibTableColumn
frMuxFramerOctetFromIf = _FrMuxFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 3),
    _FrMuxFramerOctetFromIf_Type()
)
frMuxFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerOctetFromIf.setStatus("mandatory")
_FrMuxFramerAborts_Type = Counter32
_FrMuxFramerAborts_Object = MibTableColumn
frMuxFramerAborts = _FrMuxFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 4),
    _FrMuxFramerAborts_Type()
)
frMuxFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerAborts.setStatus("mandatory")
_FrMuxFramerCrcErrors_Type = Counter32
_FrMuxFramerCrcErrors_Object = MibTableColumn
frMuxFramerCrcErrors = _FrMuxFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 5),
    _FrMuxFramerCrcErrors_Type()
)
frMuxFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerCrcErrors.setStatus("mandatory")
_FrMuxFramerLrcErrors_Type = Counter32
_FrMuxFramerLrcErrors_Object = MibTableColumn
frMuxFramerLrcErrors = _FrMuxFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 6),
    _FrMuxFramerLrcErrors_Type()
)
frMuxFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerLrcErrors.setStatus("mandatory")
_FrMuxFramerNonOctetErrors_Type = Counter32
_FrMuxFramerNonOctetErrors_Object = MibTableColumn
frMuxFramerNonOctetErrors = _FrMuxFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 7),
    _FrMuxFramerNonOctetErrors_Type()
)
frMuxFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerNonOctetErrors.setStatus("mandatory")
_FrMuxFramerOverruns_Type = Counter32
_FrMuxFramerOverruns_Object = MibTableColumn
frMuxFramerOverruns = _FrMuxFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 8),
    _FrMuxFramerOverruns_Type()
)
frMuxFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerOverruns.setStatus("mandatory")
_FrMuxFramerUnderruns_Type = Counter32
_FrMuxFramerUnderruns_Object = MibTableColumn
frMuxFramerUnderruns = _FrMuxFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 9),
    _FrMuxFramerUnderruns_Type()
)
frMuxFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerUnderruns.setStatus("mandatory")
_FrMuxFramerLargeFrmErrors_Type = Counter32
_FrMuxFramerLargeFrmErrors_Object = MibTableColumn
frMuxFramerLargeFrmErrors = _FrMuxFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 10),
    _FrMuxFramerLargeFrmErrors_Type()
)
frMuxFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerLargeFrmErrors.setStatus("mandatory")
_FrMuxFramerFrmModeErrors_Type = Counter32
_FrMuxFramerFrmModeErrors_Object = MibTableColumn
frMuxFramerFrmModeErrors = _FrMuxFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 13, 1, 11),
    _FrMuxFramerFrmModeErrors_Type()
)
frMuxFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerFrmModeErrors.setStatus("mandatory")
_FrMuxFramerUtilTable_Object = MibTable
frMuxFramerUtilTable = _FrMuxFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 14)
)
if mibBuilder.loadTexts:
    frMuxFramerUtilTable.setStatus("mandatory")
_FrMuxFramerUtilEntry_Object = MibTableRow
frMuxFramerUtilEntry = _FrMuxFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 14, 1)
)
frMuxFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxFramerIndex"),
)
if mibBuilder.loadTexts:
    frMuxFramerUtilEntry.setStatus("mandatory")


class _FrMuxFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type frMuxFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrMuxFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_FrMuxFramerNormPrioLinkUtilToIf_Object = MibTableColumn
frMuxFramerNormPrioLinkUtilToIf = _FrMuxFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 14, 1, 1),
    _FrMuxFramerNormPrioLinkUtilToIf_Type()
)
frMuxFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _FrMuxFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type frMuxFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrMuxFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_FrMuxFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
frMuxFramerNormPrioLinkUtilFromIf = _FrMuxFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 2, 14, 1, 3),
    _FrMuxFramerNormPrioLinkUtilFromIf_Type()
)
frMuxFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_FrMuxLmi_ObjectIdentity = ObjectIdentity
frMuxLmi = _FrMuxLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3)
)
_FrMuxLmiRowStatusTable_Object = MibTable
frMuxLmiRowStatusTable = _FrMuxLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 1)
)
if mibBuilder.loadTexts:
    frMuxLmiRowStatusTable.setStatus("mandatory")
_FrMuxLmiRowStatusEntry_Object = MibTableRow
frMuxLmiRowStatusEntry = _FrMuxLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 1, 1)
)
frMuxLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    frMuxLmiRowStatusEntry.setStatus("mandatory")
_FrMuxLmiRowStatus_Type = RowStatus
_FrMuxLmiRowStatus_Object = MibTableColumn
frMuxLmiRowStatus = _FrMuxLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 1, 1, 1),
    _FrMuxLmiRowStatus_Type()
)
frMuxLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiRowStatus.setStatus("mandatory")
_FrMuxLmiComponentName_Type = DisplayString
_FrMuxLmiComponentName_Object = MibTableColumn
frMuxLmiComponentName = _FrMuxLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 1, 1, 2),
    _FrMuxLmiComponentName_Type()
)
frMuxLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiComponentName.setStatus("mandatory")
_FrMuxLmiStorageType_Type = StorageType
_FrMuxLmiStorageType_Object = MibTableColumn
frMuxLmiStorageType = _FrMuxLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 1, 1, 4),
    _FrMuxLmiStorageType_Type()
)
frMuxLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiStorageType.setStatus("mandatory")
_FrMuxLmiIndex_Type = NonReplicated
_FrMuxLmiIndex_Object = MibTableColumn
frMuxLmiIndex = _FrMuxLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 1, 1, 10),
    _FrMuxLmiIndex_Type()
)
frMuxLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frMuxLmiIndex.setStatus("mandatory")
_FrMuxLmiProvTable_Object = MibTable
frMuxLmiProvTable = _FrMuxLmiProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 10)
)
if mibBuilder.loadTexts:
    frMuxLmiProvTable.setStatus("mandatory")
_FrMuxLmiProvEntry_Object = MibTableRow
frMuxLmiProvEntry = _FrMuxLmiProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 10, 1)
)
frMuxLmiProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    frMuxLmiProvEntry.setStatus("mandatory")


class _FrMuxLmiProcedures_Type(Integer32):
    """Custom type frMuxLmiProcedures based on Integer32"""
    defaultValue = 3

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
        *(("ansi", 2),
          ("ccitt", 3),
          ("none", 0),
          ("vendorForum", 1))
    )


_FrMuxLmiProcedures_Type.__name__ = "Integer32"
_FrMuxLmiProcedures_Object = MibTableColumn
frMuxLmiProcedures = _FrMuxLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 10, 1, 1),
    _FrMuxLmiProcedures_Type()
)
frMuxLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxLmiProcedures.setStatus("mandatory")


class _FrMuxLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type frMuxLmiLinkVerificationTimer based on Unsigned32"""
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


_FrMuxLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_FrMuxLmiLinkVerificationTimer_Object = MibTableColumn
frMuxLmiLinkVerificationTimer = _FrMuxLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 10, 1, 2),
    _FrMuxLmiLinkVerificationTimer_Type()
)
frMuxLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxLmiLinkVerificationTimer.setStatus("mandatory")


class _FrMuxLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type frMuxLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrMuxLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_FrMuxLmiFullStatusPollingCycles_Object = MibTableColumn
frMuxLmiFullStatusPollingCycles = _FrMuxLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 10, 1, 3),
    _FrMuxLmiFullStatusPollingCycles_Type()
)
frMuxLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxLmiFullStatusPollingCycles.setStatus("mandatory")


class _FrMuxLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type frMuxLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMuxLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_FrMuxLmiErrorEventThreshold_Object = MibTableColumn
frMuxLmiErrorEventThreshold = _FrMuxLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 10, 1, 4),
    _FrMuxLmiErrorEventThreshold_Type()
)
frMuxLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxLmiErrorEventThreshold.setStatus("mandatory")


class _FrMuxLmiEventCount_Type(Unsigned32):
    """Custom type frMuxLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrMuxLmiEventCount_Type.__name__ = "Unsigned32"
_FrMuxLmiEventCount_Object = MibTableColumn
frMuxLmiEventCount = _FrMuxLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 10, 1, 5),
    _FrMuxLmiEventCount_Type()
)
frMuxLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxLmiEventCount.setStatus("mandatory")
_FrMuxLmiStateTable_Object = MibTable
frMuxLmiStateTable = _FrMuxLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 11)
)
if mibBuilder.loadTexts:
    frMuxLmiStateTable.setStatus("mandatory")
_FrMuxLmiStateEntry_Object = MibTableRow
frMuxLmiStateEntry = _FrMuxLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 11, 1)
)
frMuxLmiStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    frMuxLmiStateEntry.setStatus("mandatory")


class _FrMuxLmiAdminState_Type(Integer32):
    """Custom type frMuxLmiAdminState based on Integer32"""
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


_FrMuxLmiAdminState_Type.__name__ = "Integer32"
_FrMuxLmiAdminState_Object = MibTableColumn
frMuxLmiAdminState = _FrMuxLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 11, 1, 1),
    _FrMuxLmiAdminState_Type()
)
frMuxLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiAdminState.setStatus("mandatory")


class _FrMuxLmiOperationalState_Type(Integer32):
    """Custom type frMuxLmiOperationalState based on Integer32"""
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


_FrMuxLmiOperationalState_Type.__name__ = "Integer32"
_FrMuxLmiOperationalState_Object = MibTableColumn
frMuxLmiOperationalState = _FrMuxLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 11, 1, 2),
    _FrMuxLmiOperationalState_Type()
)
frMuxLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiOperationalState.setStatus("mandatory")


class _FrMuxLmiUsageState_Type(Integer32):
    """Custom type frMuxLmiUsageState based on Integer32"""
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


_FrMuxLmiUsageState_Type.__name__ = "Integer32"
_FrMuxLmiUsageState_Object = MibTableColumn
frMuxLmiUsageState = _FrMuxLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 11, 1, 3),
    _FrMuxLmiUsageState_Type()
)
frMuxLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiUsageState.setStatus("mandatory")
_FrMuxLmiPsiTable_Object = MibTable
frMuxLmiPsiTable = _FrMuxLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 12)
)
if mibBuilder.loadTexts:
    frMuxLmiPsiTable.setStatus("mandatory")
_FrMuxLmiPsiEntry_Object = MibTableRow
frMuxLmiPsiEntry = _FrMuxLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 12, 1)
)
frMuxLmiPsiEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    frMuxLmiPsiEntry.setStatus("mandatory")


class _FrMuxLmiProtocolStatus_Type(Integer32):
    """Custom type frMuxLmiProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("errorCondition", 0),
          ("normalCondition", 1))
    )


_FrMuxLmiProtocolStatus_Type.__name__ = "Integer32"
_FrMuxLmiProtocolStatus_Object = MibTableColumn
frMuxLmiProtocolStatus = _FrMuxLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 12, 1, 1),
    _FrMuxLmiProtocolStatus_Type()
)
frMuxLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiProtocolStatus.setStatus("mandatory")
_FrMuxLmiStatsTable_Object = MibTable
frMuxLmiStatsTable = _FrMuxLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 13)
)
if mibBuilder.loadTexts:
    frMuxLmiStatsTable.setStatus("mandatory")
_FrMuxLmiStatsEntry_Object = MibTableRow
frMuxLmiStatsEntry = _FrMuxLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 13, 1)
)
frMuxLmiStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxLmiIndex"),
)
if mibBuilder.loadTexts:
    frMuxLmiStatsEntry.setStatus("mandatory")
_FrMuxLmiKeepAliveStatusEnqToIf_Type = Counter32
_FrMuxLmiKeepAliveStatusEnqToIf_Object = MibTableColumn
frMuxLmiKeepAliveStatusEnqToIf = _FrMuxLmiKeepAliveStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 13, 1, 1),
    _FrMuxLmiKeepAliveStatusEnqToIf_Type()
)
frMuxLmiKeepAliveStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiKeepAliveStatusEnqToIf.setStatus("mandatory")
_FrMuxLmiFullStatusEnqToIf_Type = Counter32
_FrMuxLmiFullStatusEnqToIf_Object = MibTableColumn
frMuxLmiFullStatusEnqToIf = _FrMuxLmiFullStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 13, 1, 2),
    _FrMuxLmiFullStatusEnqToIf_Type()
)
frMuxLmiFullStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiFullStatusEnqToIf.setStatus("mandatory")
_FrMuxLmiProtocolErrors_Type = Counter32
_FrMuxLmiProtocolErrors_Object = MibTableColumn
frMuxLmiProtocolErrors = _FrMuxLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 13, 1, 3),
    _FrMuxLmiProtocolErrors_Type()
)
frMuxLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiProtocolErrors.setStatus("mandatory")
_FrMuxLmiUnexpectedIes_Type = Counter32
_FrMuxLmiUnexpectedIes_Object = MibTableColumn
frMuxLmiUnexpectedIes = _FrMuxLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 13, 1, 4),
    _FrMuxLmiUnexpectedIes_Type()
)
frMuxLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiUnexpectedIes.setStatus("mandatory")
_FrMuxLmiSequenceErrors_Type = Counter32
_FrMuxLmiSequenceErrors_Object = MibTableColumn
frMuxLmiSequenceErrors = _FrMuxLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 13, 1, 5),
    _FrMuxLmiSequenceErrors_Type()
)
frMuxLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiSequenceErrors.setStatus("mandatory")
_FrMuxLmiUnexpectedReports_Type = Counter32
_FrMuxLmiUnexpectedReports_Object = MibTableColumn
frMuxLmiUnexpectedReports = _FrMuxLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 13, 1, 6),
    _FrMuxLmiUnexpectedReports_Type()
)
frMuxLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiUnexpectedReports.setStatus("mandatory")
_FrMuxLmiNoStatusReportCount_Type = Counter32
_FrMuxLmiNoStatusReportCount_Object = MibTableColumn
frMuxLmiNoStatusReportCount = _FrMuxLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 3, 13, 1, 7),
    _FrMuxLmiNoStatusReportCount_Type()
)
frMuxLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLmiNoStatusReportCount.setStatus("mandatory")
_FrMuxDlci_ObjectIdentity = ObjectIdentity
frMuxDlci = _FrMuxDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4)
)
_FrMuxDlciRowStatusTable_Object = MibTable
frMuxDlciRowStatusTable = _FrMuxDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 1)
)
if mibBuilder.loadTexts:
    frMuxDlciRowStatusTable.setStatus("mandatory")
_FrMuxDlciRowStatusEntry_Object = MibTableRow
frMuxDlciRowStatusEntry = _FrMuxDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 1, 1)
)
frMuxDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    frMuxDlciRowStatusEntry.setStatus("mandatory")
_FrMuxDlciRowStatus_Type = RowStatus
_FrMuxDlciRowStatus_Object = MibTableColumn
frMuxDlciRowStatus = _FrMuxDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 1, 1, 1),
    _FrMuxDlciRowStatus_Type()
)
frMuxDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxDlciRowStatus.setStatus("mandatory")
_FrMuxDlciComponentName_Type = DisplayString
_FrMuxDlciComponentName_Object = MibTableColumn
frMuxDlciComponentName = _FrMuxDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 1, 1, 2),
    _FrMuxDlciComponentName_Type()
)
frMuxDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciComponentName.setStatus("mandatory")
_FrMuxDlciStorageType_Type = StorageType
_FrMuxDlciStorageType_Object = MibTableColumn
frMuxDlciStorageType = _FrMuxDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 1, 1, 4),
    _FrMuxDlciStorageType_Type()
)
frMuxDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciStorageType.setStatus("mandatory")


class _FrMuxDlciIndex_Type(Integer32):
    """Custom type frMuxDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrMuxDlciIndex_Type.__name__ = "Integer32"
_FrMuxDlciIndex_Object = MibTableColumn
frMuxDlciIndex = _FrMuxDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 1, 1, 10),
    _FrMuxDlciIndex_Type()
)
frMuxDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frMuxDlciIndex.setStatus("mandatory")
_FrMuxDlciApplInfo_ObjectIdentity = ObjectIdentity
frMuxDlciApplInfo = _FrMuxDlciApplInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2)
)
_FrMuxDlciApplInfoRowStatusTable_Object = MibTable
frMuxDlciApplInfoRowStatusTable = _FrMuxDlciApplInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2, 1)
)
if mibBuilder.loadTexts:
    frMuxDlciApplInfoRowStatusTable.setStatus("mandatory")
_FrMuxDlciApplInfoRowStatusEntry_Object = MibTableRow
frMuxDlciApplInfoRowStatusEntry = _FrMuxDlciApplInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2, 1, 1)
)
frMuxDlciApplInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxDlciApplInfoIndex"),
)
if mibBuilder.loadTexts:
    frMuxDlciApplInfoRowStatusEntry.setStatus("mandatory")
_FrMuxDlciApplInfoRowStatus_Type = RowStatus
_FrMuxDlciApplInfoRowStatus_Object = MibTableColumn
frMuxDlciApplInfoRowStatus = _FrMuxDlciApplInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2, 1, 1, 1),
    _FrMuxDlciApplInfoRowStatus_Type()
)
frMuxDlciApplInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciApplInfoRowStatus.setStatus("mandatory")
_FrMuxDlciApplInfoComponentName_Type = DisplayString
_FrMuxDlciApplInfoComponentName_Object = MibTableColumn
frMuxDlciApplInfoComponentName = _FrMuxDlciApplInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2, 1, 1, 2),
    _FrMuxDlciApplInfoComponentName_Type()
)
frMuxDlciApplInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciApplInfoComponentName.setStatus("mandatory")
_FrMuxDlciApplInfoStorageType_Type = StorageType
_FrMuxDlciApplInfoStorageType_Object = MibTableColumn
frMuxDlciApplInfoStorageType = _FrMuxDlciApplInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2, 1, 1, 4),
    _FrMuxDlciApplInfoStorageType_Type()
)
frMuxDlciApplInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciApplInfoStorageType.setStatus("mandatory")
_FrMuxDlciApplInfoIndex_Type = NonReplicated
_FrMuxDlciApplInfoIndex_Object = MibTableColumn
frMuxDlciApplInfoIndex = _FrMuxDlciApplInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2, 1, 1, 10),
    _FrMuxDlciApplInfoIndex_Type()
)
frMuxDlciApplInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frMuxDlciApplInfoIndex.setStatus("mandatory")
_FrMuxDlciApplInfoProvTable_Object = MibTable
frMuxDlciApplInfoProvTable = _FrMuxDlciApplInfoProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2, 11)
)
if mibBuilder.loadTexts:
    frMuxDlciApplInfoProvTable.setStatus("mandatory")
_FrMuxDlciApplInfoProvEntry_Object = MibTableRow
frMuxDlciApplInfoProvEntry = _FrMuxDlciApplInfoProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2, 11, 1)
)
frMuxDlciApplInfoProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxDlciApplInfoIndex"),
)
if mibBuilder.loadTexts:
    frMuxDlciApplInfoProvEntry.setStatus("mandatory")
_FrMuxDlciApplInfoApplicationName_Type = Link
_FrMuxDlciApplInfoApplicationName_Object = MibTableColumn
frMuxDlciApplInfoApplicationName = _FrMuxDlciApplInfoApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 2, 11, 1, 1),
    _FrMuxDlciApplInfoApplicationName_Type()
)
frMuxDlciApplInfoApplicationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxDlciApplInfoApplicationName.setStatus("mandatory")
_FrMuxDlciOperTable_Object = MibTable
frMuxDlciOperTable = _FrMuxDlciOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 10)
)
if mibBuilder.loadTexts:
    frMuxDlciOperTable.setStatus("mandatory")
_FrMuxDlciOperEntry_Object = MibTableRow
frMuxDlciOperEntry = _FrMuxDlciOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 10, 1)
)
frMuxDlciOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    frMuxDlciOperEntry.setStatus("mandatory")
_FrMuxDlciApplicationName_Type = RowPointer
_FrMuxDlciApplicationName_Object = MibTableColumn
frMuxDlciApplicationName = _FrMuxDlciApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 10, 1, 1),
    _FrMuxDlciApplicationName_Type()
)
frMuxDlciApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciApplicationName.setStatus("mandatory")
_FrMuxDlciStateTable_Object = MibTable
frMuxDlciStateTable = _FrMuxDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 11)
)
if mibBuilder.loadTexts:
    frMuxDlciStateTable.setStatus("mandatory")
_FrMuxDlciStateEntry_Object = MibTableRow
frMuxDlciStateEntry = _FrMuxDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 11, 1)
)
frMuxDlciStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    frMuxDlciStateEntry.setStatus("mandatory")


class _FrMuxDlciAdminState_Type(Integer32):
    """Custom type frMuxDlciAdminState based on Integer32"""
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


_FrMuxDlciAdminState_Type.__name__ = "Integer32"
_FrMuxDlciAdminState_Object = MibTableColumn
frMuxDlciAdminState = _FrMuxDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 11, 1, 1),
    _FrMuxDlciAdminState_Type()
)
frMuxDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciAdminState.setStatus("mandatory")


class _FrMuxDlciOperationalState_Type(Integer32):
    """Custom type frMuxDlciOperationalState based on Integer32"""
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


_FrMuxDlciOperationalState_Type.__name__ = "Integer32"
_FrMuxDlciOperationalState_Object = MibTableColumn
frMuxDlciOperationalState = _FrMuxDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 11, 1, 2),
    _FrMuxDlciOperationalState_Type()
)
frMuxDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciOperationalState.setStatus("mandatory")


class _FrMuxDlciUsageState_Type(Integer32):
    """Custom type frMuxDlciUsageState based on Integer32"""
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


_FrMuxDlciUsageState_Type.__name__ = "Integer32"
_FrMuxDlciUsageState_Object = MibTableColumn
frMuxDlciUsageState = _FrMuxDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 11, 1, 3),
    _FrMuxDlciUsageState_Type()
)
frMuxDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciUsageState.setStatus("mandatory")
_FrMuxDlciAbitTable_Object = MibTable
frMuxDlciAbitTable = _FrMuxDlciAbitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 12)
)
if mibBuilder.loadTexts:
    frMuxDlciAbitTable.setStatus("mandatory")
_FrMuxDlciAbitEntry_Object = MibTableRow
frMuxDlciAbitEntry = _FrMuxDlciAbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 12, 1)
)
frMuxDlciAbitEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    frMuxDlciAbitEntry.setStatus("mandatory")


class _FrMuxDlciABitStatusFromIf_Type(Integer32):
    """Custom type frMuxDlciABitStatusFromIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_FrMuxDlciABitStatusFromIf_Type.__name__ = "Integer32"
_FrMuxDlciABitStatusFromIf_Object = MibTableColumn
frMuxDlciABitStatusFromIf = _FrMuxDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 12, 1, 1),
    _FrMuxDlciABitStatusFromIf_Type()
)
frMuxDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciABitStatusFromIf.setStatus("mandatory")
_FrMuxDlciStatsTable_Object = MibTable
frMuxDlciStatsTable = _FrMuxDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13)
)
if mibBuilder.loadTexts:
    frMuxDlciStatsTable.setStatus("mandatory")
_FrMuxDlciStatsEntry_Object = MibTableRow
frMuxDlciStatsEntry = _FrMuxDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1)
)
frMuxDlciStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxDlciIndex"),
)
if mibBuilder.loadTexts:
    frMuxDlciStatsEntry.setStatus("mandatory")
_FrMuxDlciFrmToIf_Type = Counter32
_FrMuxDlciFrmToIf_Object = MibTableColumn
frMuxDlciFrmToIf = _FrMuxDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 1),
    _FrMuxDlciFrmToIf_Type()
)
frMuxDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciFrmToIf.setStatus("mandatory")
_FrMuxDlciBytesToIf_Type = PassportCounter64
_FrMuxDlciBytesToIf_Object = MibTableColumn
frMuxDlciBytesToIf = _FrMuxDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 2),
    _FrMuxDlciBytesToIf_Type()
)
frMuxDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciBytesToIf.setStatus("mandatory")
_FrMuxDlciFrmFromIf_Type = Counter32
_FrMuxDlciFrmFromIf_Object = MibTableColumn
frMuxDlciFrmFromIf = _FrMuxDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 3),
    _FrMuxDlciFrmFromIf_Type()
)
frMuxDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciFrmFromIf.setStatus("mandatory")
_FrMuxDlciDeFrmFromIf_Type = Counter32
_FrMuxDlciDeFrmFromIf_Object = MibTableColumn
frMuxDlciDeFrmFromIf = _FrMuxDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 4),
    _FrMuxDlciDeFrmFromIf_Type()
)
frMuxDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciDeFrmFromIf.setStatus("mandatory")
_FrMuxDlciBytesFromIf_Type = PassportCounter64
_FrMuxDlciBytesFromIf_Object = MibTableColumn
frMuxDlciBytesFromIf = _FrMuxDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 5),
    _FrMuxDlciBytesFromIf_Type()
)
frMuxDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciBytesFromIf.setStatus("mandatory")
_FrMuxDlciDeBytesFromIf_Type = PassportCounter64
_FrMuxDlciDeBytesFromIf_Object = MibTableColumn
frMuxDlciDeBytesFromIf = _FrMuxDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 6),
    _FrMuxDlciDeBytesFromIf_Type()
)
frMuxDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciDeBytesFromIf.setStatus("mandatory")
_FrMuxDlciFecnFrmToIf_Type = Counter32
_FrMuxDlciFecnFrmToIf_Object = MibTableColumn
frMuxDlciFecnFrmToIf = _FrMuxDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 7),
    _FrMuxDlciFecnFrmToIf_Type()
)
frMuxDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciFecnFrmToIf.setStatus("mandatory")
_FrMuxDlciFecnFrmFromIf_Type = Counter32
_FrMuxDlciFecnFrmFromIf_Object = MibTableColumn
frMuxDlciFecnFrmFromIf = _FrMuxDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 8),
    _FrMuxDlciFecnFrmFromIf_Type()
)
frMuxDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciFecnFrmFromIf.setStatus("mandatory")
_FrMuxDlciBecnFrmToIf_Type = Counter32
_FrMuxDlciBecnFrmToIf_Object = MibTableColumn
frMuxDlciBecnFrmToIf = _FrMuxDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 9),
    _FrMuxDlciBecnFrmToIf_Type()
)
frMuxDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciBecnFrmToIf.setStatus("mandatory")
_FrMuxDlciBecnFrmFromIf_Type = Counter32
_FrMuxDlciBecnFrmFromIf_Object = MibTableColumn
frMuxDlciBecnFrmFromIf = _FrMuxDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 10),
    _FrMuxDlciBecnFrmFromIf_Type()
)
frMuxDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciBecnFrmFromIf.setStatus("mandatory")
_FrMuxDlciDiscCongestedFromIf_Type = Counter32
_FrMuxDlciDiscCongestedFromIf_Object = MibTableColumn
frMuxDlciDiscCongestedFromIf = _FrMuxDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 11),
    _FrMuxDlciDiscCongestedFromIf_Type()
)
frMuxDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciDiscCongestedFromIf.setStatus("mandatory")
_FrMuxDlciDiscCongestedFromIfBytes_Type = Counter32
_FrMuxDlciDiscCongestedFromIfBytes_Object = MibTableColumn
frMuxDlciDiscCongestedFromIfBytes = _FrMuxDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 12),
    _FrMuxDlciDiscCongestedFromIfBytes_Type()
)
frMuxDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciDiscCongestedFromIfBytes.setStatus("mandatory")
_FrMuxDlciDiscDeCongestedFromIf_Type = Counter32
_FrMuxDlciDiscDeCongestedFromIf_Object = MibTableColumn
frMuxDlciDiscDeCongestedFromIf = _FrMuxDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 13),
    _FrMuxDlciDiscDeCongestedFromIf_Type()
)
frMuxDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciDiscDeCongestedFromIf.setStatus("mandatory")
_FrMuxDlciDiscDeCongestedFromIfBytes_Type = Counter32
_FrMuxDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
frMuxDlciDiscDeCongestedFromIfBytes = _FrMuxDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 14),
    _FrMuxDlciDiscDeCongestedFromIfBytes_Type()
)
frMuxDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")
_FrMuxDlciErrorShortFrmFromIf_Type = Counter32
_FrMuxDlciErrorShortFrmFromIf_Object = MibTableColumn
frMuxDlciErrorShortFrmFromIf = _FrMuxDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 15),
    _FrMuxDlciErrorShortFrmFromIf_Type()
)
frMuxDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciErrorShortFrmFromIf.setStatus("mandatory")
_FrMuxDlciErrorLongFrmFromIf_Type = Counter32
_FrMuxDlciErrorLongFrmFromIf_Object = MibTableColumn
frMuxDlciErrorLongFrmFromIf = _FrMuxDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 4, 13, 1, 16),
    _FrMuxDlciErrorLongFrmFromIf_Type()
)
frMuxDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxDlciErrorLongFrmFromIf.setStatus("mandatory")
_FrMuxOperStatusTable_Object = MibTable
frMuxOperStatusTable = _FrMuxOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 8)
)
if mibBuilder.loadTexts:
    frMuxOperStatusTable.setStatus("mandatory")
_FrMuxOperStatusEntry_Object = MibTableRow
frMuxOperStatusEntry = _FrMuxOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 8, 1)
)
frMuxOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
)
if mibBuilder.loadTexts:
    frMuxOperStatusEntry.setStatus("mandatory")


class _FrMuxSnmpOperStatus_Type(Integer32):
    """Custom type frMuxSnmpOperStatus based on Integer32"""
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


_FrMuxSnmpOperStatus_Type.__name__ = "Integer32"
_FrMuxSnmpOperStatus_Object = MibTableColumn
frMuxSnmpOperStatus = _FrMuxSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 8, 1, 1),
    _FrMuxSnmpOperStatus_Type()
)
frMuxSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxSnmpOperStatus.setStatus("mandatory")
_FrMuxIfEntryTable_Object = MibTable
frMuxIfEntryTable = _FrMuxIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 9)
)
if mibBuilder.loadTexts:
    frMuxIfEntryTable.setStatus("mandatory")
_FrMuxIfEntryEntry_Object = MibTableRow
frMuxIfEntryEntry = _FrMuxIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 9, 1)
)
frMuxIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
)
if mibBuilder.loadTexts:
    frMuxIfEntryEntry.setStatus("mandatory")


class _FrMuxIfAdminStatus_Type(Integer32):
    """Custom type frMuxIfAdminStatus based on Integer32"""
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


_FrMuxIfAdminStatus_Type.__name__ = "Integer32"
_FrMuxIfAdminStatus_Object = MibTableColumn
frMuxIfAdminStatus = _FrMuxIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 9, 1, 1),
    _FrMuxIfAdminStatus_Type()
)
frMuxIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxIfAdminStatus.setStatus("mandatory")


class _FrMuxIfIndex_Type(InterfaceIndex):
    """Custom type frMuxIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrMuxIfIndex_Type.__name__ = "InterfaceIndex"
_FrMuxIfIndex_Object = MibTableColumn
frMuxIfIndex = _FrMuxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 9, 1, 2),
    _FrMuxIfIndex_Type()
)
frMuxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxIfIndex.setStatus("mandatory")
_FrMuxCidDataTable_Object = MibTable
frMuxCidDataTable = _FrMuxCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 10)
)
if mibBuilder.loadTexts:
    frMuxCidDataTable.setStatus("mandatory")
_FrMuxCidDataEntry_Object = MibTableRow
frMuxCidDataEntry = _FrMuxCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 10, 1)
)
frMuxCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
)
if mibBuilder.loadTexts:
    frMuxCidDataEntry.setStatus("mandatory")


class _FrMuxCustomerIdentifier_Type(Unsigned32):
    """Custom type frMuxCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_FrMuxCustomerIdentifier_Type.__name__ = "Unsigned32"
_FrMuxCustomerIdentifier_Object = MibTableColumn
frMuxCustomerIdentifier = _FrMuxCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 10, 1, 1),
    _FrMuxCustomerIdentifier_Type()
)
frMuxCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMuxCustomerIdentifier.setStatus("mandatory")
_FrMuxStateTable_Object = MibTable
frMuxStateTable = _FrMuxStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11)
)
if mibBuilder.loadTexts:
    frMuxStateTable.setStatus("mandatory")
_FrMuxStateEntry_Object = MibTableRow
frMuxStateEntry = _FrMuxStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1)
)
frMuxStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
)
if mibBuilder.loadTexts:
    frMuxStateEntry.setStatus("mandatory")


class _FrMuxAdminState_Type(Integer32):
    """Custom type frMuxAdminState based on Integer32"""
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


_FrMuxAdminState_Type.__name__ = "Integer32"
_FrMuxAdminState_Object = MibTableColumn
frMuxAdminState = _FrMuxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1, 1),
    _FrMuxAdminState_Type()
)
frMuxAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxAdminState.setStatus("mandatory")


class _FrMuxOperationalState_Type(Integer32):
    """Custom type frMuxOperationalState based on Integer32"""
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


_FrMuxOperationalState_Type.__name__ = "Integer32"
_FrMuxOperationalState_Object = MibTableColumn
frMuxOperationalState = _FrMuxOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1, 2),
    _FrMuxOperationalState_Type()
)
frMuxOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxOperationalState.setStatus("mandatory")


class _FrMuxUsageState_Type(Integer32):
    """Custom type frMuxUsageState based on Integer32"""
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


_FrMuxUsageState_Type.__name__ = "Integer32"
_FrMuxUsageState_Object = MibTableColumn
frMuxUsageState = _FrMuxUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1, 3),
    _FrMuxUsageState_Type()
)
frMuxUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxUsageState.setStatus("mandatory")


class _FrMuxAvailabilityStatus_Type(OctetString):
    """Custom type frMuxAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FrMuxAvailabilityStatus_Type.__name__ = "OctetString"
_FrMuxAvailabilityStatus_Object = MibTableColumn
frMuxAvailabilityStatus = _FrMuxAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1, 4),
    _FrMuxAvailabilityStatus_Type()
)
frMuxAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxAvailabilityStatus.setStatus("mandatory")


class _FrMuxProceduralStatus_Type(OctetString):
    """Custom type frMuxProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrMuxProceduralStatus_Type.__name__ = "OctetString"
_FrMuxProceduralStatus_Object = MibTableColumn
frMuxProceduralStatus = _FrMuxProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1, 5),
    _FrMuxProceduralStatus_Type()
)
frMuxProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxProceduralStatus.setStatus("mandatory")


class _FrMuxControlStatus_Type(OctetString):
    """Custom type frMuxControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrMuxControlStatus_Type.__name__ = "OctetString"
_FrMuxControlStatus_Object = MibTableColumn
frMuxControlStatus = _FrMuxControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1, 6),
    _FrMuxControlStatus_Type()
)
frMuxControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxControlStatus.setStatus("mandatory")


class _FrMuxAlarmStatus_Type(OctetString):
    """Custom type frMuxAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrMuxAlarmStatus_Type.__name__ = "OctetString"
_FrMuxAlarmStatus_Object = MibTableColumn
frMuxAlarmStatus = _FrMuxAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1, 7),
    _FrMuxAlarmStatus_Type()
)
frMuxAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxAlarmStatus.setStatus("mandatory")


class _FrMuxStandbyStatus_Type(Integer32):
    """Custom type frMuxStandbyStatus based on Integer32"""
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


_FrMuxStandbyStatus_Type.__name__ = "Integer32"
_FrMuxStandbyStatus_Object = MibTableColumn
frMuxStandbyStatus = _FrMuxStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1, 8),
    _FrMuxStandbyStatus_Type()
)
frMuxStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxStandbyStatus.setStatus("mandatory")


class _FrMuxUnknownStatus_Type(Integer32):
    """Custom type frMuxUnknownStatus based on Integer32"""
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


_FrMuxUnknownStatus_Type.__name__ = "Integer32"
_FrMuxUnknownStatus_Object = MibTableColumn
frMuxUnknownStatus = _FrMuxUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 11, 1, 9),
    _FrMuxUnknownStatus_Type()
)
frMuxUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxUnknownStatus.setStatus("mandatory")
_FrMuxStatsTable_Object = MibTable
frMuxStatsTable = _FrMuxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 12)
)
if mibBuilder.loadTexts:
    frMuxStatsTable.setStatus("mandatory")
_FrMuxStatsEntry_Object = MibTableRow
frMuxStatsEntry = _FrMuxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 12, 1)
)
frMuxStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayMuxMIB", "frMuxIndex"),
)
if mibBuilder.loadTexts:
    frMuxStatsEntry.setStatus("mandatory")


class _FrMuxLastUnknownDlci_Type(Unsigned32):
    """Custom type frMuxLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_FrMuxLastUnknownDlci_Type.__name__ = "Unsigned32"
_FrMuxLastUnknownDlci_Object = MibTableColumn
frMuxLastUnknownDlci = _FrMuxLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 12, 1, 1),
    _FrMuxLastUnknownDlci_Type()
)
frMuxLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxLastUnknownDlci.setStatus("mandatory")
_FrMuxUnknownDlciFramesFromIf_Type = Counter32
_FrMuxUnknownDlciFramesFromIf_Object = MibTableColumn
frMuxUnknownDlciFramesFromIf = _FrMuxUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 12, 1, 2),
    _FrMuxUnknownDlciFramesFromIf_Type()
)
frMuxUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxUnknownDlciFramesFromIf.setStatus("mandatory")
_FrMuxInvalidHeaderFramesFromIf_Type = Counter32
_FrMuxInvalidHeaderFramesFromIf_Object = MibTableColumn
frMuxInvalidHeaderFramesFromIf = _FrMuxInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 12, 1, 3),
    _FrMuxInvalidHeaderFramesFromIf_Type()
)
frMuxInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxInvalidHeaderFramesFromIf.setStatus("mandatory")
_FrMuxTimeFramerCongested_Type = Counter32
_FrMuxTimeFramerCongested_Object = MibTableColumn
frMuxTimeFramerCongested = _FrMuxTimeFramerCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 112, 12, 1, 4),
    _FrMuxTimeFramerCongested_Type()
)
frMuxTimeFramerCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frMuxTimeFramerCongested.setStatus("mandatory")
_FrameRelayMuxMIB_ObjectIdentity = ObjectIdentity
frameRelayMuxMIB = _FrameRelayMuxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 38)
)
_FrameRelayMuxGroup_ObjectIdentity = ObjectIdentity
frameRelayMuxGroup = _FrameRelayMuxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 38, 1)
)
_FrameRelayMuxGroupBE_ObjectIdentity = ObjectIdentity
frameRelayMuxGroupBE = _FrameRelayMuxGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 38, 1, 5)
)
_FrameRelayMuxGroupBE00_ObjectIdentity = ObjectIdentity
frameRelayMuxGroupBE00 = _FrameRelayMuxGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 38, 1, 5, 1)
)
_FrameRelayMuxGroupBE00A_ObjectIdentity = ObjectIdentity
frameRelayMuxGroupBE00A = _FrameRelayMuxGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 38, 1, 5, 1, 2)
)
_FrameRelayMuxCapabilities_ObjectIdentity = ObjectIdentity
frameRelayMuxCapabilities = _FrameRelayMuxCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 38, 3)
)
_FrameRelayMuxCapabilitiesBE_ObjectIdentity = ObjectIdentity
frameRelayMuxCapabilitiesBE = _FrameRelayMuxCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 38, 3, 5)
)
_FrameRelayMuxCapabilitiesBE00_ObjectIdentity = ObjectIdentity
frameRelayMuxCapabilitiesBE00 = _FrameRelayMuxCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 38, 3, 5, 1)
)
_FrameRelayMuxCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
frameRelayMuxCapabilitiesBE00A = _FrameRelayMuxCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 38, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrameRelayMuxMIB",
    **{"frMux": frMux,
       "frMuxRowStatusTable": frMuxRowStatusTable,
       "frMuxRowStatusEntry": frMuxRowStatusEntry,
       "frMuxRowStatus": frMuxRowStatus,
       "frMuxComponentName": frMuxComponentName,
       "frMuxStorageType": frMuxStorageType,
       "frMuxIndex": frMuxIndex,
       "frMuxFramer": frMuxFramer,
       "frMuxFramerRowStatusTable": frMuxFramerRowStatusTable,
       "frMuxFramerRowStatusEntry": frMuxFramerRowStatusEntry,
       "frMuxFramerRowStatus": frMuxFramerRowStatus,
       "frMuxFramerComponentName": frMuxFramerComponentName,
       "frMuxFramerStorageType": frMuxFramerStorageType,
       "frMuxFramerIndex": frMuxFramerIndex,
       "frMuxFramerProvTable": frMuxFramerProvTable,
       "frMuxFramerProvEntry": frMuxFramerProvEntry,
       "frMuxFramerInterfaceName": frMuxFramerInterfaceName,
       "frMuxFramerLinkTable": frMuxFramerLinkTable,
       "frMuxFramerLinkEntry": frMuxFramerLinkEntry,
       "frMuxFramerFlagsBetweenFrames": frMuxFramerFlagsBetweenFrames,
       "frMuxFramerStateTable": frMuxFramerStateTable,
       "frMuxFramerStateEntry": frMuxFramerStateEntry,
       "frMuxFramerAdminState": frMuxFramerAdminState,
       "frMuxFramerOperationalState": frMuxFramerOperationalState,
       "frMuxFramerUsageState": frMuxFramerUsageState,
       "frMuxFramerStatsTable": frMuxFramerStatsTable,
       "frMuxFramerStatsEntry": frMuxFramerStatsEntry,
       "frMuxFramerFrmToIf": frMuxFramerFrmToIf,
       "frMuxFramerFrmFromIf": frMuxFramerFrmFromIf,
       "frMuxFramerOctetFromIf": frMuxFramerOctetFromIf,
       "frMuxFramerAborts": frMuxFramerAborts,
       "frMuxFramerCrcErrors": frMuxFramerCrcErrors,
       "frMuxFramerLrcErrors": frMuxFramerLrcErrors,
       "frMuxFramerNonOctetErrors": frMuxFramerNonOctetErrors,
       "frMuxFramerOverruns": frMuxFramerOverruns,
       "frMuxFramerUnderruns": frMuxFramerUnderruns,
       "frMuxFramerLargeFrmErrors": frMuxFramerLargeFrmErrors,
       "frMuxFramerFrmModeErrors": frMuxFramerFrmModeErrors,
       "frMuxFramerUtilTable": frMuxFramerUtilTable,
       "frMuxFramerUtilEntry": frMuxFramerUtilEntry,
       "frMuxFramerNormPrioLinkUtilToIf": frMuxFramerNormPrioLinkUtilToIf,
       "frMuxFramerNormPrioLinkUtilFromIf": frMuxFramerNormPrioLinkUtilFromIf,
       "frMuxLmi": frMuxLmi,
       "frMuxLmiRowStatusTable": frMuxLmiRowStatusTable,
       "frMuxLmiRowStatusEntry": frMuxLmiRowStatusEntry,
       "frMuxLmiRowStatus": frMuxLmiRowStatus,
       "frMuxLmiComponentName": frMuxLmiComponentName,
       "frMuxLmiStorageType": frMuxLmiStorageType,
       "frMuxLmiIndex": frMuxLmiIndex,
       "frMuxLmiProvTable": frMuxLmiProvTable,
       "frMuxLmiProvEntry": frMuxLmiProvEntry,
       "frMuxLmiProcedures": frMuxLmiProcedures,
       "frMuxLmiLinkVerificationTimer": frMuxLmiLinkVerificationTimer,
       "frMuxLmiFullStatusPollingCycles": frMuxLmiFullStatusPollingCycles,
       "frMuxLmiErrorEventThreshold": frMuxLmiErrorEventThreshold,
       "frMuxLmiEventCount": frMuxLmiEventCount,
       "frMuxLmiStateTable": frMuxLmiStateTable,
       "frMuxLmiStateEntry": frMuxLmiStateEntry,
       "frMuxLmiAdminState": frMuxLmiAdminState,
       "frMuxLmiOperationalState": frMuxLmiOperationalState,
       "frMuxLmiUsageState": frMuxLmiUsageState,
       "frMuxLmiPsiTable": frMuxLmiPsiTable,
       "frMuxLmiPsiEntry": frMuxLmiPsiEntry,
       "frMuxLmiProtocolStatus": frMuxLmiProtocolStatus,
       "frMuxLmiStatsTable": frMuxLmiStatsTable,
       "frMuxLmiStatsEntry": frMuxLmiStatsEntry,
       "frMuxLmiKeepAliveStatusEnqToIf": frMuxLmiKeepAliveStatusEnqToIf,
       "frMuxLmiFullStatusEnqToIf": frMuxLmiFullStatusEnqToIf,
       "frMuxLmiProtocolErrors": frMuxLmiProtocolErrors,
       "frMuxLmiUnexpectedIes": frMuxLmiUnexpectedIes,
       "frMuxLmiSequenceErrors": frMuxLmiSequenceErrors,
       "frMuxLmiUnexpectedReports": frMuxLmiUnexpectedReports,
       "frMuxLmiNoStatusReportCount": frMuxLmiNoStatusReportCount,
       "frMuxDlci": frMuxDlci,
       "frMuxDlciRowStatusTable": frMuxDlciRowStatusTable,
       "frMuxDlciRowStatusEntry": frMuxDlciRowStatusEntry,
       "frMuxDlciRowStatus": frMuxDlciRowStatus,
       "frMuxDlciComponentName": frMuxDlciComponentName,
       "frMuxDlciStorageType": frMuxDlciStorageType,
       "frMuxDlciIndex": frMuxDlciIndex,
       "frMuxDlciApplInfo": frMuxDlciApplInfo,
       "frMuxDlciApplInfoRowStatusTable": frMuxDlciApplInfoRowStatusTable,
       "frMuxDlciApplInfoRowStatusEntry": frMuxDlciApplInfoRowStatusEntry,
       "frMuxDlciApplInfoRowStatus": frMuxDlciApplInfoRowStatus,
       "frMuxDlciApplInfoComponentName": frMuxDlciApplInfoComponentName,
       "frMuxDlciApplInfoStorageType": frMuxDlciApplInfoStorageType,
       "frMuxDlciApplInfoIndex": frMuxDlciApplInfoIndex,
       "frMuxDlciApplInfoProvTable": frMuxDlciApplInfoProvTable,
       "frMuxDlciApplInfoProvEntry": frMuxDlciApplInfoProvEntry,
       "frMuxDlciApplInfoApplicationName": frMuxDlciApplInfoApplicationName,
       "frMuxDlciOperTable": frMuxDlciOperTable,
       "frMuxDlciOperEntry": frMuxDlciOperEntry,
       "frMuxDlciApplicationName": frMuxDlciApplicationName,
       "frMuxDlciStateTable": frMuxDlciStateTable,
       "frMuxDlciStateEntry": frMuxDlciStateEntry,
       "frMuxDlciAdminState": frMuxDlciAdminState,
       "frMuxDlciOperationalState": frMuxDlciOperationalState,
       "frMuxDlciUsageState": frMuxDlciUsageState,
       "frMuxDlciAbitTable": frMuxDlciAbitTable,
       "frMuxDlciAbitEntry": frMuxDlciAbitEntry,
       "frMuxDlciABitStatusFromIf": frMuxDlciABitStatusFromIf,
       "frMuxDlciStatsTable": frMuxDlciStatsTable,
       "frMuxDlciStatsEntry": frMuxDlciStatsEntry,
       "frMuxDlciFrmToIf": frMuxDlciFrmToIf,
       "frMuxDlciBytesToIf": frMuxDlciBytesToIf,
       "frMuxDlciFrmFromIf": frMuxDlciFrmFromIf,
       "frMuxDlciDeFrmFromIf": frMuxDlciDeFrmFromIf,
       "frMuxDlciBytesFromIf": frMuxDlciBytesFromIf,
       "frMuxDlciDeBytesFromIf": frMuxDlciDeBytesFromIf,
       "frMuxDlciFecnFrmToIf": frMuxDlciFecnFrmToIf,
       "frMuxDlciFecnFrmFromIf": frMuxDlciFecnFrmFromIf,
       "frMuxDlciBecnFrmToIf": frMuxDlciBecnFrmToIf,
       "frMuxDlciBecnFrmFromIf": frMuxDlciBecnFrmFromIf,
       "frMuxDlciDiscCongestedFromIf": frMuxDlciDiscCongestedFromIf,
       "frMuxDlciDiscCongestedFromIfBytes": frMuxDlciDiscCongestedFromIfBytes,
       "frMuxDlciDiscDeCongestedFromIf": frMuxDlciDiscDeCongestedFromIf,
       "frMuxDlciDiscDeCongestedFromIfBytes": frMuxDlciDiscDeCongestedFromIfBytes,
       "frMuxDlciErrorShortFrmFromIf": frMuxDlciErrorShortFrmFromIf,
       "frMuxDlciErrorLongFrmFromIf": frMuxDlciErrorLongFrmFromIf,
       "frMuxOperStatusTable": frMuxOperStatusTable,
       "frMuxOperStatusEntry": frMuxOperStatusEntry,
       "frMuxSnmpOperStatus": frMuxSnmpOperStatus,
       "frMuxIfEntryTable": frMuxIfEntryTable,
       "frMuxIfEntryEntry": frMuxIfEntryEntry,
       "frMuxIfAdminStatus": frMuxIfAdminStatus,
       "frMuxIfIndex": frMuxIfIndex,
       "frMuxCidDataTable": frMuxCidDataTable,
       "frMuxCidDataEntry": frMuxCidDataEntry,
       "frMuxCustomerIdentifier": frMuxCustomerIdentifier,
       "frMuxStateTable": frMuxStateTable,
       "frMuxStateEntry": frMuxStateEntry,
       "frMuxAdminState": frMuxAdminState,
       "frMuxOperationalState": frMuxOperationalState,
       "frMuxUsageState": frMuxUsageState,
       "frMuxAvailabilityStatus": frMuxAvailabilityStatus,
       "frMuxProceduralStatus": frMuxProceduralStatus,
       "frMuxControlStatus": frMuxControlStatus,
       "frMuxAlarmStatus": frMuxAlarmStatus,
       "frMuxStandbyStatus": frMuxStandbyStatus,
       "frMuxUnknownStatus": frMuxUnknownStatus,
       "frMuxStatsTable": frMuxStatsTable,
       "frMuxStatsEntry": frMuxStatsEntry,
       "frMuxLastUnknownDlci": frMuxLastUnknownDlci,
       "frMuxUnknownDlciFramesFromIf": frMuxUnknownDlciFramesFromIf,
       "frMuxInvalidHeaderFramesFromIf": frMuxInvalidHeaderFramesFromIf,
       "frMuxTimeFramerCongested": frMuxTimeFramerCongested,
       "frameRelayMuxMIB": frameRelayMuxMIB,
       "frameRelayMuxGroup": frameRelayMuxGroup,
       "frameRelayMuxGroupBE": frameRelayMuxGroupBE,
       "frameRelayMuxGroupBE00": frameRelayMuxGroupBE00,
       "frameRelayMuxGroupBE00A": frameRelayMuxGroupBE00A,
       "frameRelayMuxCapabilities": frameRelayMuxCapabilities,
       "frameRelayMuxCapabilitiesBE": frameRelayMuxCapabilitiesBE,
       "frameRelayMuxCapabilitiesBE00": frameRelayMuxCapabilitiesBE00,
       "frameRelayMuxCapabilitiesBE00A": frameRelayMuxCapabilitiesBE00A}
)
