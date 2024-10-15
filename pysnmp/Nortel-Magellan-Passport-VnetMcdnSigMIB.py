# SNMP MIB module (Nortel-Magellan-Passport-VnetMcdnSigMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VnetMcdnSigMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:37 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
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

(sigChan,
 sigChanIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VoiceNetworkingMIB",
    "sigChan",
    "sigChanIndex")

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

_SigChanMcdn_ObjectIdentity = ObjectIdentity
sigChanMcdn = _SigChanMcdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17)
)
_SigChanMcdnRowStatusTable_Object = MibTable
sigChanMcdnRowStatusTable = _SigChanMcdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 1)
)
if mibBuilder.loadTexts:
    sigChanMcdnRowStatusTable.setStatus("mandatory")
_SigChanMcdnRowStatusEntry_Object = MibTableRow
sigChanMcdnRowStatusEntry = _SigChanMcdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 1, 1)
)
sigChanMcdnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnRowStatusEntry.setStatus("mandatory")
_SigChanMcdnRowStatus_Type = RowStatus
_SigChanMcdnRowStatus_Object = MibTableColumn
sigChanMcdnRowStatus = _SigChanMcdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 1, 1, 1),
    _SigChanMcdnRowStatus_Type()
)
sigChanMcdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnRowStatus.setStatus("mandatory")
_SigChanMcdnComponentName_Type = DisplayString
_SigChanMcdnComponentName_Object = MibTableColumn
sigChanMcdnComponentName = _SigChanMcdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 1, 1, 2),
    _SigChanMcdnComponentName_Type()
)
sigChanMcdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnComponentName.setStatus("mandatory")
_SigChanMcdnStorageType_Type = StorageType
_SigChanMcdnStorageType_Object = MibTableColumn
sigChanMcdnStorageType = _SigChanMcdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 1, 1, 4),
    _SigChanMcdnStorageType_Type()
)
sigChanMcdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnStorageType.setStatus("mandatory")
_SigChanMcdnIndex_Type = NonReplicated
_SigChanMcdnIndex_Object = MibTableColumn
sigChanMcdnIndex = _SigChanMcdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 1, 1, 10),
    _SigChanMcdnIndex_Type()
)
sigChanMcdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanMcdnIndex.setStatus("mandatory")
_SigChanMcdnFramer_ObjectIdentity = ObjectIdentity
sigChanMcdnFramer = _SigChanMcdnFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2)
)
_SigChanMcdnFramerRowStatusTable_Object = MibTable
sigChanMcdnFramerRowStatusTable = _SigChanMcdnFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 1)
)
if mibBuilder.loadTexts:
    sigChanMcdnFramerRowStatusTable.setStatus("mandatory")
_SigChanMcdnFramerRowStatusEntry_Object = MibTableRow
sigChanMcdnFramerRowStatusEntry = _SigChanMcdnFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 1, 1)
)
sigChanMcdnFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnFramerRowStatusEntry.setStatus("mandatory")
_SigChanMcdnFramerRowStatus_Type = RowStatus
_SigChanMcdnFramerRowStatus_Object = MibTableColumn
sigChanMcdnFramerRowStatus = _SigChanMcdnFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 1, 1, 1),
    _SigChanMcdnFramerRowStatus_Type()
)
sigChanMcdnFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerRowStatus.setStatus("mandatory")
_SigChanMcdnFramerComponentName_Type = DisplayString
_SigChanMcdnFramerComponentName_Object = MibTableColumn
sigChanMcdnFramerComponentName = _SigChanMcdnFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 1, 1, 2),
    _SigChanMcdnFramerComponentName_Type()
)
sigChanMcdnFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerComponentName.setStatus("mandatory")
_SigChanMcdnFramerStorageType_Type = StorageType
_SigChanMcdnFramerStorageType_Object = MibTableColumn
sigChanMcdnFramerStorageType = _SigChanMcdnFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 1, 1, 4),
    _SigChanMcdnFramerStorageType_Type()
)
sigChanMcdnFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerStorageType.setStatus("mandatory")
_SigChanMcdnFramerIndex_Type = NonReplicated
_SigChanMcdnFramerIndex_Object = MibTableColumn
sigChanMcdnFramerIndex = _SigChanMcdnFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 1, 1, 10),
    _SigChanMcdnFramerIndex_Type()
)
sigChanMcdnFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanMcdnFramerIndex.setStatus("mandatory")
_SigChanMcdnFramerProvTable_Object = MibTable
sigChanMcdnFramerProvTable = _SigChanMcdnFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 10)
)
if mibBuilder.loadTexts:
    sigChanMcdnFramerProvTable.setStatus("mandatory")
_SigChanMcdnFramerProvEntry_Object = MibTableRow
sigChanMcdnFramerProvEntry = _SigChanMcdnFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 10, 1)
)
sigChanMcdnFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnFramerProvEntry.setStatus("mandatory")
_SigChanMcdnFramerInterfaceName_Type = Link
_SigChanMcdnFramerInterfaceName_Object = MibTableColumn
sigChanMcdnFramerInterfaceName = _SigChanMcdnFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 10, 1, 1),
    _SigChanMcdnFramerInterfaceName_Type()
)
sigChanMcdnFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnFramerInterfaceName.setStatus("mandatory")
_SigChanMcdnFramerStateTable_Object = MibTable
sigChanMcdnFramerStateTable = _SigChanMcdnFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 12)
)
if mibBuilder.loadTexts:
    sigChanMcdnFramerStateTable.setStatus("mandatory")
_SigChanMcdnFramerStateEntry_Object = MibTableRow
sigChanMcdnFramerStateEntry = _SigChanMcdnFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 12, 1)
)
sigChanMcdnFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnFramerStateEntry.setStatus("mandatory")


class _SigChanMcdnFramerAdminState_Type(Integer32):
    """Custom type sigChanMcdnFramerAdminState based on Integer32"""
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


_SigChanMcdnFramerAdminState_Type.__name__ = "Integer32"
_SigChanMcdnFramerAdminState_Object = MibTableColumn
sigChanMcdnFramerAdminState = _SigChanMcdnFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 12, 1, 1),
    _SigChanMcdnFramerAdminState_Type()
)
sigChanMcdnFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerAdminState.setStatus("mandatory")


class _SigChanMcdnFramerOperationalState_Type(Integer32):
    """Custom type sigChanMcdnFramerOperationalState based on Integer32"""
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


_SigChanMcdnFramerOperationalState_Type.__name__ = "Integer32"
_SigChanMcdnFramerOperationalState_Object = MibTableColumn
sigChanMcdnFramerOperationalState = _SigChanMcdnFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 12, 1, 2),
    _SigChanMcdnFramerOperationalState_Type()
)
sigChanMcdnFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerOperationalState.setStatus("mandatory")


class _SigChanMcdnFramerUsageState_Type(Integer32):
    """Custom type sigChanMcdnFramerUsageState based on Integer32"""
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


_SigChanMcdnFramerUsageState_Type.__name__ = "Integer32"
_SigChanMcdnFramerUsageState_Object = MibTableColumn
sigChanMcdnFramerUsageState = _SigChanMcdnFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 12, 1, 3),
    _SigChanMcdnFramerUsageState_Type()
)
sigChanMcdnFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerUsageState.setStatus("mandatory")
_SigChanMcdnFramerStatsTable_Object = MibTable
sigChanMcdnFramerStatsTable = _SigChanMcdnFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13)
)
if mibBuilder.loadTexts:
    sigChanMcdnFramerStatsTable.setStatus("mandatory")
_SigChanMcdnFramerStatsEntry_Object = MibTableRow
sigChanMcdnFramerStatsEntry = _SigChanMcdnFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1)
)
sigChanMcdnFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnFramerStatsEntry.setStatus("mandatory")
_SigChanMcdnFramerFrmToIf_Type = Counter32
_SigChanMcdnFramerFrmToIf_Object = MibTableColumn
sigChanMcdnFramerFrmToIf = _SigChanMcdnFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 1),
    _SigChanMcdnFramerFrmToIf_Type()
)
sigChanMcdnFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerFrmToIf.setStatus("mandatory")
_SigChanMcdnFramerFrmFromIf_Type = Counter32
_SigChanMcdnFramerFrmFromIf_Object = MibTableColumn
sigChanMcdnFramerFrmFromIf = _SigChanMcdnFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 2),
    _SigChanMcdnFramerFrmFromIf_Type()
)
sigChanMcdnFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerFrmFromIf.setStatus("mandatory")
_SigChanMcdnFramerOctetFromIf_Type = Counter32
_SigChanMcdnFramerOctetFromIf_Object = MibTableColumn
sigChanMcdnFramerOctetFromIf = _SigChanMcdnFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 3),
    _SigChanMcdnFramerOctetFromIf_Type()
)
sigChanMcdnFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerOctetFromIf.setStatus("mandatory")
_SigChanMcdnFramerAborts_Type = Counter32
_SigChanMcdnFramerAborts_Object = MibTableColumn
sigChanMcdnFramerAborts = _SigChanMcdnFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 4),
    _SigChanMcdnFramerAborts_Type()
)
sigChanMcdnFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerAborts.setStatus("mandatory")
_SigChanMcdnFramerCrcErrors_Type = Counter32
_SigChanMcdnFramerCrcErrors_Object = MibTableColumn
sigChanMcdnFramerCrcErrors = _SigChanMcdnFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 5),
    _SigChanMcdnFramerCrcErrors_Type()
)
sigChanMcdnFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerCrcErrors.setStatus("mandatory")
_SigChanMcdnFramerLrcErrors_Type = Counter32
_SigChanMcdnFramerLrcErrors_Object = MibTableColumn
sigChanMcdnFramerLrcErrors = _SigChanMcdnFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 6),
    _SigChanMcdnFramerLrcErrors_Type()
)
sigChanMcdnFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerLrcErrors.setStatus("mandatory")
_SigChanMcdnFramerNonOctetErrors_Type = Counter32
_SigChanMcdnFramerNonOctetErrors_Object = MibTableColumn
sigChanMcdnFramerNonOctetErrors = _SigChanMcdnFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 7),
    _SigChanMcdnFramerNonOctetErrors_Type()
)
sigChanMcdnFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerNonOctetErrors.setStatus("mandatory")
_SigChanMcdnFramerOverruns_Type = Counter32
_SigChanMcdnFramerOverruns_Object = MibTableColumn
sigChanMcdnFramerOverruns = _SigChanMcdnFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 8),
    _SigChanMcdnFramerOverruns_Type()
)
sigChanMcdnFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerOverruns.setStatus("mandatory")
_SigChanMcdnFramerUnderruns_Type = Counter32
_SigChanMcdnFramerUnderruns_Object = MibTableColumn
sigChanMcdnFramerUnderruns = _SigChanMcdnFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 9),
    _SigChanMcdnFramerUnderruns_Type()
)
sigChanMcdnFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerUnderruns.setStatus("mandatory")
_SigChanMcdnFramerLargeFrmErrors_Type = Counter32
_SigChanMcdnFramerLargeFrmErrors_Object = MibTableColumn
sigChanMcdnFramerLargeFrmErrors = _SigChanMcdnFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 2, 13, 1, 10),
    _SigChanMcdnFramerLargeFrmErrors_Type()
)
sigChanMcdnFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnFramerLargeFrmErrors.setStatus("mandatory")
_SigChanMcdnL2Table_Object = MibTable
sigChanMcdnL2Table = _SigChanMcdnL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 11)
)
if mibBuilder.loadTexts:
    sigChanMcdnL2Table.setStatus("mandatory")
_SigChanMcdnL2Entry_Object = MibTableRow
sigChanMcdnL2Entry = _SigChanMcdnL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 11, 1)
)
sigChanMcdnL2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnL2Entry.setStatus("mandatory")


class _SigChanMcdnT23_Type(Unsigned32):
    """Custom type sigChanMcdnT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SigChanMcdnT23_Type.__name__ = "Unsigned32"
_SigChanMcdnT23_Object = MibTableColumn
sigChanMcdnT23 = _SigChanMcdnT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 11, 1, 1),
    _SigChanMcdnT23_Type()
)
sigChanMcdnT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnT23.setStatus("mandatory")


class _SigChanMcdnT200_Type(Unsigned32):
    """Custom type sigChanMcdnT200 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SigChanMcdnT200_Type.__name__ = "Unsigned32"
_SigChanMcdnT200_Object = MibTableColumn
sigChanMcdnT200 = _SigChanMcdnT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 11, 1, 2),
    _SigChanMcdnT200_Type()
)
sigChanMcdnT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnT200.setStatus("mandatory")


class _SigChanMcdnN200_Type(Unsigned32):
    """Custom type sigChanMcdnN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SigChanMcdnN200_Type.__name__ = "Unsigned32"
_SigChanMcdnN200_Object = MibTableColumn
sigChanMcdnN200 = _SigChanMcdnN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 11, 1, 3),
    _SigChanMcdnN200_Type()
)
sigChanMcdnN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnN200.setStatus("mandatory")


class _SigChanMcdnT203_Type(Unsigned32):
    """Custom type sigChanMcdnT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_SigChanMcdnT203_Type.__name__ = "Unsigned32"
_SigChanMcdnT203_Object = MibTableColumn
sigChanMcdnT203 = _SigChanMcdnT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 11, 1, 4),
    _SigChanMcdnT203_Type()
)
sigChanMcdnT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnT203.setStatus("mandatory")


class _SigChanMcdnCircuitSwitchedK_Type(Unsigned32):
    """Custom type sigChanMcdnCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SigChanMcdnCircuitSwitchedK_Type.__name__ = "Unsigned32"
_SigChanMcdnCircuitSwitchedK_Object = MibTableColumn
sigChanMcdnCircuitSwitchedK = _SigChanMcdnCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 11, 1, 6),
    _SigChanMcdnCircuitSwitchedK_Type()
)
sigChanMcdnCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnCircuitSwitchedK.setStatus("mandatory")
_SigChanMcdnL3Table_Object = MibTable
sigChanMcdnL3Table = _SigChanMcdnL3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 12)
)
if mibBuilder.loadTexts:
    sigChanMcdnL3Table.setStatus("mandatory")
_SigChanMcdnL3Entry_Object = MibTableRow
sigChanMcdnL3Entry = _SigChanMcdnL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 12, 1)
)
sigChanMcdnL3Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnL3Entry.setStatus("mandatory")


class _SigChanMcdnT302_Type(Unsigned32):
    """Custom type sigChanMcdnT302 based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_SigChanMcdnT302_Type.__name__ = "Unsigned32"
_SigChanMcdnT302_Object = MibTableColumn
sigChanMcdnT302 = _SigChanMcdnT302_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 12, 1, 1),
    _SigChanMcdnT302_Type()
)
sigChanMcdnT302.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnT302.setStatus("mandatory")


class _SigChanMcdnT304_Type(Unsigned32):
    """Custom type sigChanMcdnT304 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_SigChanMcdnT304_Type.__name__ = "Unsigned32"
_SigChanMcdnT304_Object = MibTableColumn
sigChanMcdnT304 = _SigChanMcdnT304_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 12, 1, 2),
    _SigChanMcdnT304_Type()
)
sigChanMcdnT304.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnT304.setStatus("mandatory")


class _SigChanMcdnT309_Type(Unsigned32):
    """Custom type sigChanMcdnT309 based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 120),
    )


_SigChanMcdnT309_Type.__name__ = "Unsigned32"
_SigChanMcdnT309_Object = MibTableColumn
sigChanMcdnT309 = _SigChanMcdnT309_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 12, 1, 3),
    _SigChanMcdnT309_Type()
)
sigChanMcdnT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnT309.setStatus("mandatory")


class _SigChanMcdnT310_Type(Unsigned32):
    """Custom type sigChanMcdnT310 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_SigChanMcdnT310_Type.__name__ = "Unsigned32"
_SigChanMcdnT310_Object = MibTableColumn
sigChanMcdnT310 = _SigChanMcdnT310_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 12, 1, 4),
    _SigChanMcdnT310_Type()
)
sigChanMcdnT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnT310.setStatus("mandatory")


class _SigChanMcdnT316_Type(Unsigned32):
    """Custom type sigChanMcdnT316 based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(31, 180),
    )


_SigChanMcdnT316_Type.__name__ = "Unsigned32"
_SigChanMcdnT316_Object = MibTableColumn
sigChanMcdnT316 = _SigChanMcdnT316_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 12, 1, 5),
    _SigChanMcdnT316_Type()
)
sigChanMcdnT316.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnT316.setStatus("mandatory")


class _SigChanMcdnT317_Type(Unsigned32):
    """Custom type sigChanMcdnT317 based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 179),
    )


_SigChanMcdnT317_Type.__name__ = "Unsigned32"
_SigChanMcdnT317_Object = MibTableColumn
sigChanMcdnT317 = _SigChanMcdnT317_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 12, 1, 6),
    _SigChanMcdnT317_Type()
)
sigChanMcdnT317.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnT317.setStatus("mandatory")
_SigChanMcdnProvTable_Object = MibTable
sigChanMcdnProvTable = _SigChanMcdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 13)
)
if mibBuilder.loadTexts:
    sigChanMcdnProvTable.setStatus("mandatory")
_SigChanMcdnProvEntry_Object = MibTableRow
sigChanMcdnProvEntry = _SigChanMcdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 13, 1)
)
sigChanMcdnProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnProvEntry.setStatus("mandatory")


class _SigChanMcdnSide_Type(Integer32):
    """Custom type sigChanMcdnSide based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("user", 2))
    )


_SigChanMcdnSide_Type.__name__ = "Integer32"
_SigChanMcdnSide_Object = MibTableColumn
sigChanMcdnSide = _SigChanMcdnSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 13, 1, 1),
    _SigChanMcdnSide_Type()
)
sigChanMcdnSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnSide.setStatus("mandatory")


class _SigChanMcdnMaxNonCallConcurrent_Type(Unsigned32):
    """Custom type sigChanMcdnMaxNonCallConcurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SigChanMcdnMaxNonCallConcurrent_Type.__name__ = "Unsigned32"
_SigChanMcdnMaxNonCallConcurrent_Object = MibTableColumn
sigChanMcdnMaxNonCallConcurrent = _SigChanMcdnMaxNonCallConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 13, 1, 2),
    _SigChanMcdnMaxNonCallConcurrent_Type()
)
sigChanMcdnMaxNonCallConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnMaxNonCallConcurrent.setStatus("mandatory")


class _SigChanMcdnOverlapSending_Type(Integer32):
    """Custom type sigChanMcdnOverlapSending based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_SigChanMcdnOverlapSending_Type.__name__ = "Integer32"
_SigChanMcdnOverlapSending_Object = MibTableColumn
sigChanMcdnOverlapSending = _SigChanMcdnOverlapSending_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 13, 1, 3),
    _SigChanMcdnOverlapSending_Type()
)
sigChanMcdnOverlapSending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnOverlapSending.setStatus("mandatory")


class _SigChanMcdnOverlapReceiving_Type(Integer32):
    """Custom type sigChanMcdnOverlapReceiving based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_SigChanMcdnOverlapReceiving_Type.__name__ = "Integer32"
_SigChanMcdnOverlapReceiving_Object = MibTableColumn
sigChanMcdnOverlapReceiving = _SigChanMcdnOverlapReceiving_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 13, 1, 4),
    _SigChanMcdnOverlapReceiving_Type()
)
sigChanMcdnOverlapReceiving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnOverlapReceiving.setStatus("mandatory")


class _SigChanMcdnChanMaintenanceHandling_Type(Integer32):
    """Custom type sigChanMcdnChanMaintenanceHandling based on Integer32"""
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
        *(("globalOnStartup", 0),
          ("restartMessage", 2),
          ("serviceMessage", 1))
    )


_SigChanMcdnChanMaintenanceHandling_Type.__name__ = "Integer32"
_SigChanMcdnChanMaintenanceHandling_Object = MibTableColumn
sigChanMcdnChanMaintenanceHandling = _SigChanMcdnChanMaintenanceHandling_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 13, 1, 5),
    _SigChanMcdnChanMaintenanceHandling_Type()
)
sigChanMcdnChanMaintenanceHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnChanMaintenanceHandling.setStatus("mandatory")
_SigChanMcdnStateTable_Object = MibTable
sigChanMcdnStateTable = _SigChanMcdnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 14)
)
if mibBuilder.loadTexts:
    sigChanMcdnStateTable.setStatus("mandatory")
_SigChanMcdnStateEntry_Object = MibTableRow
sigChanMcdnStateEntry = _SigChanMcdnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 14, 1)
)
sigChanMcdnStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnStateEntry.setStatus("mandatory")


class _SigChanMcdnAdminState_Type(Integer32):
    """Custom type sigChanMcdnAdminState based on Integer32"""
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


_SigChanMcdnAdminState_Type.__name__ = "Integer32"
_SigChanMcdnAdminState_Object = MibTableColumn
sigChanMcdnAdminState = _SigChanMcdnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 14, 1, 1),
    _SigChanMcdnAdminState_Type()
)
sigChanMcdnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnAdminState.setStatus("mandatory")


class _SigChanMcdnOperationalState_Type(Integer32):
    """Custom type sigChanMcdnOperationalState based on Integer32"""
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


_SigChanMcdnOperationalState_Type.__name__ = "Integer32"
_SigChanMcdnOperationalState_Object = MibTableColumn
sigChanMcdnOperationalState = _SigChanMcdnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 14, 1, 2),
    _SigChanMcdnOperationalState_Type()
)
sigChanMcdnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnOperationalState.setStatus("mandatory")


class _SigChanMcdnUsageState_Type(Integer32):
    """Custom type sigChanMcdnUsageState based on Integer32"""
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


_SigChanMcdnUsageState_Type.__name__ = "Integer32"
_SigChanMcdnUsageState_Object = MibTableColumn
sigChanMcdnUsageState = _SigChanMcdnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 14, 1, 3),
    _SigChanMcdnUsageState_Type()
)
sigChanMcdnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnUsageState.setStatus("mandatory")
_SigChanMcdnStatsTable_Object = MibTable
sigChanMcdnStatsTable = _SigChanMcdnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 15)
)
if mibBuilder.loadTexts:
    sigChanMcdnStatsTable.setStatus("mandatory")
_SigChanMcdnStatsEntry_Object = MibTableRow
sigChanMcdnStatsEntry = _SigChanMcdnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 15, 1)
)
sigChanMcdnStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnStatsEntry.setStatus("mandatory")
_SigChanMcdnTotalCallsToIf_Type = Counter32
_SigChanMcdnTotalCallsToIf_Object = MibTableColumn
sigChanMcdnTotalCallsToIf = _SigChanMcdnTotalCallsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 15, 1, 2),
    _SigChanMcdnTotalCallsToIf_Type()
)
sigChanMcdnTotalCallsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnTotalCallsToIf.setStatus("mandatory")
_SigChanMcdnTotalCallsFromIf_Type = Counter32
_SigChanMcdnTotalCallsFromIf_Object = MibTableColumn
sigChanMcdnTotalCallsFromIf = _SigChanMcdnTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 15, 1, 3),
    _SigChanMcdnTotalCallsFromIf_Type()
)
sigChanMcdnTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnTotalCallsFromIf.setStatus("mandatory")
_SigChanMcdnNonCallAssocSessionsToIf_Type = Counter32
_SigChanMcdnNonCallAssocSessionsToIf_Object = MibTableColumn
sigChanMcdnNonCallAssocSessionsToIf = _SigChanMcdnNonCallAssocSessionsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 15, 1, 4),
    _SigChanMcdnNonCallAssocSessionsToIf_Type()
)
sigChanMcdnNonCallAssocSessionsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnNonCallAssocSessionsToIf.setStatus("mandatory")
_SigChanMcdnNonCallAssocSessionsFromIf_Type = Counter32
_SigChanMcdnNonCallAssocSessionsFromIf_Object = MibTableColumn
sigChanMcdnNonCallAssocSessionsFromIf = _SigChanMcdnNonCallAssocSessionsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 15, 1, 5),
    _SigChanMcdnNonCallAssocSessionsFromIf_Type()
)
sigChanMcdnNonCallAssocSessionsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnNonCallAssocSessionsFromIf.setStatus("mandatory")
_SigChanMcdnOperTable_Object = MibTable
sigChanMcdnOperTable = _SigChanMcdnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 16)
)
if mibBuilder.loadTexts:
    sigChanMcdnOperTable.setStatus("mandatory")
_SigChanMcdnOperEntry_Object = MibTableRow
sigChanMcdnOperEntry = _SigChanMcdnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 16, 1)
)
sigChanMcdnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnOperEntry.setStatus("mandatory")


class _SigChanMcdnActiveChannels_Type(Unsigned32):
    """Custom type sigChanMcdnActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanMcdnActiveChannels_Type.__name__ = "Unsigned32"
_SigChanMcdnActiveChannels_Object = MibTableColumn
sigChanMcdnActiveChannels = _SigChanMcdnActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 16, 1, 1),
    _SigChanMcdnActiveChannels_Type()
)
sigChanMcdnActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnActiveChannels.setStatus("mandatory")


class _SigChanMcdnActiveVoiceChannels_Type(Unsigned32):
    """Custom type sigChanMcdnActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanMcdnActiveVoiceChannels_Type.__name__ = "Unsigned32"
_SigChanMcdnActiveVoiceChannels_Object = MibTableColumn
sigChanMcdnActiveVoiceChannels = _SigChanMcdnActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 16, 1, 2),
    _SigChanMcdnActiveVoiceChannels_Type()
)
sigChanMcdnActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnActiveVoiceChannels.setStatus("mandatory")


class _SigChanMcdnActiveDataChannels_Type(Unsigned32):
    """Custom type sigChanMcdnActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanMcdnActiveDataChannels_Type.__name__ = "Unsigned32"
_SigChanMcdnActiveDataChannels_Object = MibTableColumn
sigChanMcdnActiveDataChannels = _SigChanMcdnActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 16, 1, 3),
    _SigChanMcdnActiveDataChannels_Type()
)
sigChanMcdnActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnActiveDataChannels.setStatus("mandatory")


class _SigChanMcdnPeakActiveChannels_Type(Unsigned32):
    """Custom type sigChanMcdnPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanMcdnPeakActiveChannels_Type.__name__ = "Unsigned32"
_SigChanMcdnPeakActiveChannels_Object = MibTableColumn
sigChanMcdnPeakActiveChannels = _SigChanMcdnPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 16, 1, 4),
    _SigChanMcdnPeakActiveChannels_Type()
)
sigChanMcdnPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnPeakActiveChannels.setStatus("mandatory")


class _SigChanMcdnPeakActiveVoiceChannels_Type(Unsigned32):
    """Custom type sigChanMcdnPeakActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanMcdnPeakActiveVoiceChannels_Type.__name__ = "Unsigned32"
_SigChanMcdnPeakActiveVoiceChannels_Object = MibTableColumn
sigChanMcdnPeakActiveVoiceChannels = _SigChanMcdnPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 16, 1, 5),
    _SigChanMcdnPeakActiveVoiceChannels_Type()
)
sigChanMcdnPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnPeakActiveVoiceChannels.setStatus("mandatory")


class _SigChanMcdnPeakActiveDataChannels_Type(Unsigned32):
    """Custom type sigChanMcdnPeakActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanMcdnPeakActiveDataChannels_Type.__name__ = "Unsigned32"
_SigChanMcdnPeakActiveDataChannels_Object = MibTableColumn
sigChanMcdnPeakActiveDataChannels = _SigChanMcdnPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 16, 1, 6),
    _SigChanMcdnPeakActiveDataChannels_Type()
)
sigChanMcdnPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnPeakActiveDataChannels.setStatus("mandatory")


class _SigChanMcdnDChanStatus_Type(Integer32):
    """Custom type sigChanMcdnDChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("enabling", 3),
          ("established", 2),
          ("establishing", 1),
          ("inService", 4),
          ("outOfService", 0),
          ("restarting", 5))
    )


_SigChanMcdnDChanStatus_Type.__name__ = "Integer32"
_SigChanMcdnDChanStatus_Object = MibTableColumn
sigChanMcdnDChanStatus = _SigChanMcdnDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 16, 1, 7),
    _SigChanMcdnDChanStatus_Type()
)
sigChanMcdnDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanMcdnDChanStatus.setStatus("mandatory")
_SigChanMcdnToolsTable_Object = MibTable
sigChanMcdnToolsTable = _SigChanMcdnToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 17)
)
if mibBuilder.loadTexts:
    sigChanMcdnToolsTable.setStatus("mandatory")
_SigChanMcdnToolsEntry_Object = MibTableRow
sigChanMcdnToolsEntry = _SigChanMcdnToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 17, 1)
)
sigChanMcdnToolsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnToolsEntry.setStatus("mandatory")


class _SigChanMcdnTracing_Type(OctetString):
    """Custom type sigChanMcdnTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SigChanMcdnTracing_Type.__name__ = "OctetString"
_SigChanMcdnTracing_Object = MibTableColumn
sigChanMcdnTracing = _SigChanMcdnTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 17, 1, 1),
    _SigChanMcdnTracing_Type()
)
sigChanMcdnTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnTracing.setStatus("mandatory")


class _SigChanMcdnMessageTraced_Type(OctetString):
    """Custom type sigChanMcdnMessageTraced based on OctetString"""
    defaultHexValue = "ffffff80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SigChanMcdnMessageTraced_Type.__name__ = "OctetString"
_SigChanMcdnMessageTraced_Object = MibTableColumn
sigChanMcdnMessageTraced = _SigChanMcdnMessageTraced_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 17, 1, 2),
    _SigChanMcdnMessageTraced_Type()
)
sigChanMcdnMessageTraced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnMessageTraced.setStatus("mandatory")


class _SigChanMcdnDirectionTraced_Type(OctetString):
    """Custom type sigChanMcdnDirectionTraced based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SigChanMcdnDirectionTraced_Type.__name__ = "OctetString"
_SigChanMcdnDirectionTraced_Object = MibTableColumn
sigChanMcdnDirectionTraced = _SigChanMcdnDirectionTraced_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 17, 1, 3),
    _SigChanMcdnDirectionTraced_Type()
)
sigChanMcdnDirectionTraced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnDirectionTraced.setStatus("mandatory")
_SigChanMcdnClsTable_Object = MibTable
sigChanMcdnClsTable = _SigChanMcdnClsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 18)
)
if mibBuilder.loadTexts:
    sigChanMcdnClsTable.setStatus("mandatory")
_SigChanMcdnClsEntry_Object = MibTableRow
sigChanMcdnClsEntry = _SigChanMcdnClsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 18, 1)
)
sigChanMcdnClsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnClsEntry.setStatus("mandatory")


class _SigChanMcdnClsFeaturesSupported_Type(OctetString):
    """Custom type sigChanMcdnClsFeaturesSupported based on OctetString"""
    defaultHexValue = "ffc1"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SigChanMcdnClsFeaturesSupported_Type.__name__ = "OctetString"
_SigChanMcdnClsFeaturesSupported_Object = MibTableColumn
sigChanMcdnClsFeaturesSupported = _SigChanMcdnClsFeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 18, 1, 2),
    _SigChanMcdnClsFeaturesSupported_Type()
)
sigChanMcdnClsFeaturesSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnClsFeaturesSupported.setStatus("mandatory")
_SigChanMcdnCoTable_Object = MibTable
sigChanMcdnCoTable = _SigChanMcdnCoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 19)
)
if mibBuilder.loadTexts:
    sigChanMcdnCoTable.setStatus("mandatory")
_SigChanMcdnCoEntry_Object = MibTableRow
sigChanMcdnCoEntry = _SigChanMcdnCoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 19, 1)
)
sigChanMcdnCoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetMcdnSigMIB", "sigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanMcdnCoEntry.setStatus("mandatory")


class _SigChanMcdnDropBackCongestion_Type(Integer32):
    """Custom type sigChanMcdnDropBackCongestion based on Integer32"""
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
        *(("dropBackToOriginator", 1),
          ("dropBackToPriorNode", 2),
          ("noDropBackAllowed", 0))
    )


_SigChanMcdnDropBackCongestion_Type.__name__ = "Integer32"
_SigChanMcdnDropBackCongestion_Object = MibTableColumn
sigChanMcdnDropBackCongestion = _SigChanMcdnDropBackCongestion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 19, 1, 1),
    _SigChanMcdnDropBackCongestion_Type()
)
sigChanMcdnDropBackCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnDropBackCongestion.setStatus("mandatory")


class _SigChanMcdnNetworkNameDisplay_Type(OctetString):
    """Custom type sigChanMcdnNetworkNameDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SigChanMcdnNetworkNameDisplay_Type.__name__ = "OctetString"
_SigChanMcdnNetworkNameDisplay_Object = MibTableColumn
sigChanMcdnNetworkNameDisplay = _SigChanMcdnNetworkNameDisplay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 19, 1, 4),
    _SigChanMcdnNetworkNameDisplay_Type()
)
sigChanMcdnNetworkNameDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnNetworkNameDisplay.setStatus("mandatory")


class _SigChanMcdnMultisiteBusinessGroup_Type(Integer32):
    """Custom type sigChanMcdnMultisiteBusinessGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("transport", 0))
    )


_SigChanMcdnMultisiteBusinessGroup_Type.__name__ = "Integer32"
_SigChanMcdnMultisiteBusinessGroup_Object = MibTableColumn
sigChanMcdnMultisiteBusinessGroup = _SigChanMcdnMultisiteBusinessGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 19, 1, 7),
    _SigChanMcdnMultisiteBusinessGroup_Type()
)
sigChanMcdnMultisiteBusinessGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnMultisiteBusinessGroup.setStatus("mandatory")


class _SigChanMcdnConOrFeaturesSupported_Type(OctetString):
    """Custom type sigChanMcdnConOrFeaturesSupported based on OctetString"""
    defaultHexValue = "fff8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SigChanMcdnConOrFeaturesSupported_Type.__name__ = "OctetString"
_SigChanMcdnConOrFeaturesSupported_Object = MibTableColumn
sigChanMcdnConOrFeaturesSupported = _SigChanMcdnConOrFeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 17, 19, 1, 8),
    _SigChanMcdnConOrFeaturesSupported_Type()
)
sigChanMcdnConOrFeaturesSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanMcdnConOrFeaturesSupported.setStatus("mandatory")
_VnetMcdnSigMIB_ObjectIdentity = ObjectIdentity
vnetMcdnSigMIB = _VnetMcdnSigMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 142)
)
_VnetMcdnSigGroup_ObjectIdentity = ObjectIdentity
vnetMcdnSigGroup = _VnetMcdnSigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 142, 1)
)
_VnetMcdnSigGroupBE_ObjectIdentity = ObjectIdentity
vnetMcdnSigGroupBE = _VnetMcdnSigGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 142, 1, 5)
)
_VnetMcdnSigGroupBE01_ObjectIdentity = ObjectIdentity
vnetMcdnSigGroupBE01 = _VnetMcdnSigGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 142, 1, 5, 2)
)
_VnetMcdnSigGroupBE01A_ObjectIdentity = ObjectIdentity
vnetMcdnSigGroupBE01A = _VnetMcdnSigGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 142, 1, 5, 2, 2)
)
_VnetMcdnSigCapabilities_ObjectIdentity = ObjectIdentity
vnetMcdnSigCapabilities = _VnetMcdnSigCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 142, 3)
)
_VnetMcdnSigCapabilitiesBE_ObjectIdentity = ObjectIdentity
vnetMcdnSigCapabilitiesBE = _VnetMcdnSigCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 142, 3, 5)
)
_VnetMcdnSigCapabilitiesBE01_ObjectIdentity = ObjectIdentity
vnetMcdnSigCapabilitiesBE01 = _VnetMcdnSigCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 142, 3, 5, 2)
)
_VnetMcdnSigCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
vnetMcdnSigCapabilitiesBE01A = _VnetMcdnSigCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 142, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VnetMcdnSigMIB",
    **{"sigChanMcdn": sigChanMcdn,
       "sigChanMcdnRowStatusTable": sigChanMcdnRowStatusTable,
       "sigChanMcdnRowStatusEntry": sigChanMcdnRowStatusEntry,
       "sigChanMcdnRowStatus": sigChanMcdnRowStatus,
       "sigChanMcdnComponentName": sigChanMcdnComponentName,
       "sigChanMcdnStorageType": sigChanMcdnStorageType,
       "sigChanMcdnIndex": sigChanMcdnIndex,
       "sigChanMcdnFramer": sigChanMcdnFramer,
       "sigChanMcdnFramerRowStatusTable": sigChanMcdnFramerRowStatusTable,
       "sigChanMcdnFramerRowStatusEntry": sigChanMcdnFramerRowStatusEntry,
       "sigChanMcdnFramerRowStatus": sigChanMcdnFramerRowStatus,
       "sigChanMcdnFramerComponentName": sigChanMcdnFramerComponentName,
       "sigChanMcdnFramerStorageType": sigChanMcdnFramerStorageType,
       "sigChanMcdnFramerIndex": sigChanMcdnFramerIndex,
       "sigChanMcdnFramerProvTable": sigChanMcdnFramerProvTable,
       "sigChanMcdnFramerProvEntry": sigChanMcdnFramerProvEntry,
       "sigChanMcdnFramerInterfaceName": sigChanMcdnFramerInterfaceName,
       "sigChanMcdnFramerStateTable": sigChanMcdnFramerStateTable,
       "sigChanMcdnFramerStateEntry": sigChanMcdnFramerStateEntry,
       "sigChanMcdnFramerAdminState": sigChanMcdnFramerAdminState,
       "sigChanMcdnFramerOperationalState": sigChanMcdnFramerOperationalState,
       "sigChanMcdnFramerUsageState": sigChanMcdnFramerUsageState,
       "sigChanMcdnFramerStatsTable": sigChanMcdnFramerStatsTable,
       "sigChanMcdnFramerStatsEntry": sigChanMcdnFramerStatsEntry,
       "sigChanMcdnFramerFrmToIf": sigChanMcdnFramerFrmToIf,
       "sigChanMcdnFramerFrmFromIf": sigChanMcdnFramerFrmFromIf,
       "sigChanMcdnFramerOctetFromIf": sigChanMcdnFramerOctetFromIf,
       "sigChanMcdnFramerAborts": sigChanMcdnFramerAborts,
       "sigChanMcdnFramerCrcErrors": sigChanMcdnFramerCrcErrors,
       "sigChanMcdnFramerLrcErrors": sigChanMcdnFramerLrcErrors,
       "sigChanMcdnFramerNonOctetErrors": sigChanMcdnFramerNonOctetErrors,
       "sigChanMcdnFramerOverruns": sigChanMcdnFramerOverruns,
       "sigChanMcdnFramerUnderruns": sigChanMcdnFramerUnderruns,
       "sigChanMcdnFramerLargeFrmErrors": sigChanMcdnFramerLargeFrmErrors,
       "sigChanMcdnL2Table": sigChanMcdnL2Table,
       "sigChanMcdnL2Entry": sigChanMcdnL2Entry,
       "sigChanMcdnT23": sigChanMcdnT23,
       "sigChanMcdnT200": sigChanMcdnT200,
       "sigChanMcdnN200": sigChanMcdnN200,
       "sigChanMcdnT203": sigChanMcdnT203,
       "sigChanMcdnCircuitSwitchedK": sigChanMcdnCircuitSwitchedK,
       "sigChanMcdnL3Table": sigChanMcdnL3Table,
       "sigChanMcdnL3Entry": sigChanMcdnL3Entry,
       "sigChanMcdnT302": sigChanMcdnT302,
       "sigChanMcdnT304": sigChanMcdnT304,
       "sigChanMcdnT309": sigChanMcdnT309,
       "sigChanMcdnT310": sigChanMcdnT310,
       "sigChanMcdnT316": sigChanMcdnT316,
       "sigChanMcdnT317": sigChanMcdnT317,
       "sigChanMcdnProvTable": sigChanMcdnProvTable,
       "sigChanMcdnProvEntry": sigChanMcdnProvEntry,
       "sigChanMcdnSide": sigChanMcdnSide,
       "sigChanMcdnMaxNonCallConcurrent": sigChanMcdnMaxNonCallConcurrent,
       "sigChanMcdnOverlapSending": sigChanMcdnOverlapSending,
       "sigChanMcdnOverlapReceiving": sigChanMcdnOverlapReceiving,
       "sigChanMcdnChanMaintenanceHandling": sigChanMcdnChanMaintenanceHandling,
       "sigChanMcdnStateTable": sigChanMcdnStateTable,
       "sigChanMcdnStateEntry": sigChanMcdnStateEntry,
       "sigChanMcdnAdminState": sigChanMcdnAdminState,
       "sigChanMcdnOperationalState": sigChanMcdnOperationalState,
       "sigChanMcdnUsageState": sigChanMcdnUsageState,
       "sigChanMcdnStatsTable": sigChanMcdnStatsTable,
       "sigChanMcdnStatsEntry": sigChanMcdnStatsEntry,
       "sigChanMcdnTotalCallsToIf": sigChanMcdnTotalCallsToIf,
       "sigChanMcdnTotalCallsFromIf": sigChanMcdnTotalCallsFromIf,
       "sigChanMcdnNonCallAssocSessionsToIf": sigChanMcdnNonCallAssocSessionsToIf,
       "sigChanMcdnNonCallAssocSessionsFromIf": sigChanMcdnNonCallAssocSessionsFromIf,
       "sigChanMcdnOperTable": sigChanMcdnOperTable,
       "sigChanMcdnOperEntry": sigChanMcdnOperEntry,
       "sigChanMcdnActiveChannels": sigChanMcdnActiveChannels,
       "sigChanMcdnActiveVoiceChannels": sigChanMcdnActiveVoiceChannels,
       "sigChanMcdnActiveDataChannels": sigChanMcdnActiveDataChannels,
       "sigChanMcdnPeakActiveChannels": sigChanMcdnPeakActiveChannels,
       "sigChanMcdnPeakActiveVoiceChannels": sigChanMcdnPeakActiveVoiceChannels,
       "sigChanMcdnPeakActiveDataChannels": sigChanMcdnPeakActiveDataChannels,
       "sigChanMcdnDChanStatus": sigChanMcdnDChanStatus,
       "sigChanMcdnToolsTable": sigChanMcdnToolsTable,
       "sigChanMcdnToolsEntry": sigChanMcdnToolsEntry,
       "sigChanMcdnTracing": sigChanMcdnTracing,
       "sigChanMcdnMessageTraced": sigChanMcdnMessageTraced,
       "sigChanMcdnDirectionTraced": sigChanMcdnDirectionTraced,
       "sigChanMcdnClsTable": sigChanMcdnClsTable,
       "sigChanMcdnClsEntry": sigChanMcdnClsEntry,
       "sigChanMcdnClsFeaturesSupported": sigChanMcdnClsFeaturesSupported,
       "sigChanMcdnCoTable": sigChanMcdnCoTable,
       "sigChanMcdnCoEntry": sigChanMcdnCoEntry,
       "sigChanMcdnDropBackCongestion": sigChanMcdnDropBackCongestion,
       "sigChanMcdnNetworkNameDisplay": sigChanMcdnNetworkNameDisplay,
       "sigChanMcdnMultisiteBusinessGroup": sigChanMcdnMultisiteBusinessGroup,
       "sigChanMcdnConOrFeaturesSupported": sigChanMcdnConOrFeaturesSupported,
       "vnetMcdnSigMIB": vnetMcdnSigMIB,
       "vnetMcdnSigGroup": vnetMcdnSigGroup,
       "vnetMcdnSigGroupBE": vnetMcdnSigGroupBE,
       "vnetMcdnSigGroupBE01": vnetMcdnSigGroupBE01,
       "vnetMcdnSigGroupBE01A": vnetMcdnSigGroupBE01A,
       "vnetMcdnSigCapabilities": vnetMcdnSigCapabilities,
       "vnetMcdnSigCapabilitiesBE": vnetMcdnSigCapabilitiesBE,
       "vnetMcdnSigCapabilitiesBE01": vnetMcdnSigCapabilitiesBE01,
       "vnetMcdnSigCapabilitiesBE01A": vnetMcdnSigCapabilitiesBE01A}
)
