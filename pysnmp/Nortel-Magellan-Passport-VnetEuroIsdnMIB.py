# SNMP MIB module (Nortel-Magellan-Passport-VnetEuroIsdnMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VnetEuroIsdnMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:36 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
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

_SigChanEIsdn_ObjectIdentity = ObjectIdentity
sigChanEIsdn = _SigChanEIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14)
)
_SigChanEIsdnRowStatusTable_Object = MibTable
sigChanEIsdnRowStatusTable = _SigChanEIsdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 1)
)
if mibBuilder.loadTexts:
    sigChanEIsdnRowStatusTable.setStatus("mandatory")
_SigChanEIsdnRowStatusEntry_Object = MibTableRow
sigChanEIsdnRowStatusEntry = _SigChanEIsdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 1, 1)
)
sigChanEIsdnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnRowStatusEntry.setStatus("mandatory")
_SigChanEIsdnRowStatus_Type = RowStatus
_SigChanEIsdnRowStatus_Object = MibTableColumn
sigChanEIsdnRowStatus = _SigChanEIsdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 1, 1, 1),
    _SigChanEIsdnRowStatus_Type()
)
sigChanEIsdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnRowStatus.setStatus("mandatory")
_SigChanEIsdnComponentName_Type = DisplayString
_SigChanEIsdnComponentName_Object = MibTableColumn
sigChanEIsdnComponentName = _SigChanEIsdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 1, 1, 2),
    _SigChanEIsdnComponentName_Type()
)
sigChanEIsdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnComponentName.setStatus("mandatory")
_SigChanEIsdnStorageType_Type = StorageType
_SigChanEIsdnStorageType_Object = MibTableColumn
sigChanEIsdnStorageType = _SigChanEIsdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 1, 1, 4),
    _SigChanEIsdnStorageType_Type()
)
sigChanEIsdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnStorageType.setStatus("mandatory")
_SigChanEIsdnIndex_Type = NonReplicated
_SigChanEIsdnIndex_Object = MibTableColumn
sigChanEIsdnIndex = _SigChanEIsdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 1, 1, 10),
    _SigChanEIsdnIndex_Type()
)
sigChanEIsdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanEIsdnIndex.setStatus("mandatory")
_SigChanEIsdnFramer_ObjectIdentity = ObjectIdentity
sigChanEIsdnFramer = _SigChanEIsdnFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2)
)
_SigChanEIsdnFramerRowStatusTable_Object = MibTable
sigChanEIsdnFramerRowStatusTable = _SigChanEIsdnFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 1)
)
if mibBuilder.loadTexts:
    sigChanEIsdnFramerRowStatusTable.setStatus("mandatory")
_SigChanEIsdnFramerRowStatusEntry_Object = MibTableRow
sigChanEIsdnFramerRowStatusEntry = _SigChanEIsdnFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 1, 1)
)
sigChanEIsdnFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnFramerRowStatusEntry.setStatus("mandatory")
_SigChanEIsdnFramerRowStatus_Type = RowStatus
_SigChanEIsdnFramerRowStatus_Object = MibTableColumn
sigChanEIsdnFramerRowStatus = _SigChanEIsdnFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 1, 1, 1),
    _SigChanEIsdnFramerRowStatus_Type()
)
sigChanEIsdnFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerRowStatus.setStatus("mandatory")
_SigChanEIsdnFramerComponentName_Type = DisplayString
_SigChanEIsdnFramerComponentName_Object = MibTableColumn
sigChanEIsdnFramerComponentName = _SigChanEIsdnFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 1, 1, 2),
    _SigChanEIsdnFramerComponentName_Type()
)
sigChanEIsdnFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerComponentName.setStatus("mandatory")
_SigChanEIsdnFramerStorageType_Type = StorageType
_SigChanEIsdnFramerStorageType_Object = MibTableColumn
sigChanEIsdnFramerStorageType = _SigChanEIsdnFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 1, 1, 4),
    _SigChanEIsdnFramerStorageType_Type()
)
sigChanEIsdnFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerStorageType.setStatus("mandatory")
_SigChanEIsdnFramerIndex_Type = NonReplicated
_SigChanEIsdnFramerIndex_Object = MibTableColumn
sigChanEIsdnFramerIndex = _SigChanEIsdnFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 1, 1, 10),
    _SigChanEIsdnFramerIndex_Type()
)
sigChanEIsdnFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerIndex.setStatus("mandatory")
_SigChanEIsdnFramerProvTable_Object = MibTable
sigChanEIsdnFramerProvTable = _SigChanEIsdnFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 10)
)
if mibBuilder.loadTexts:
    sigChanEIsdnFramerProvTable.setStatus("mandatory")
_SigChanEIsdnFramerProvEntry_Object = MibTableRow
sigChanEIsdnFramerProvEntry = _SigChanEIsdnFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 10, 1)
)
sigChanEIsdnFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnFramerProvEntry.setStatus("mandatory")
_SigChanEIsdnFramerInterfaceName_Type = Link
_SigChanEIsdnFramerInterfaceName_Object = MibTableColumn
sigChanEIsdnFramerInterfaceName = _SigChanEIsdnFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 10, 1, 1),
    _SigChanEIsdnFramerInterfaceName_Type()
)
sigChanEIsdnFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerInterfaceName.setStatus("mandatory")
_SigChanEIsdnFramerStateTable_Object = MibTable
sigChanEIsdnFramerStateTable = _SigChanEIsdnFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 12)
)
if mibBuilder.loadTexts:
    sigChanEIsdnFramerStateTable.setStatus("mandatory")
_SigChanEIsdnFramerStateEntry_Object = MibTableRow
sigChanEIsdnFramerStateEntry = _SigChanEIsdnFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 12, 1)
)
sigChanEIsdnFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnFramerStateEntry.setStatus("mandatory")


class _SigChanEIsdnFramerAdminState_Type(Integer32):
    """Custom type sigChanEIsdnFramerAdminState based on Integer32"""
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


_SigChanEIsdnFramerAdminState_Type.__name__ = "Integer32"
_SigChanEIsdnFramerAdminState_Object = MibTableColumn
sigChanEIsdnFramerAdminState = _SigChanEIsdnFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 12, 1, 1),
    _SigChanEIsdnFramerAdminState_Type()
)
sigChanEIsdnFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerAdminState.setStatus("mandatory")


class _SigChanEIsdnFramerOperationalState_Type(Integer32):
    """Custom type sigChanEIsdnFramerOperationalState based on Integer32"""
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


_SigChanEIsdnFramerOperationalState_Type.__name__ = "Integer32"
_SigChanEIsdnFramerOperationalState_Object = MibTableColumn
sigChanEIsdnFramerOperationalState = _SigChanEIsdnFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 12, 1, 2),
    _SigChanEIsdnFramerOperationalState_Type()
)
sigChanEIsdnFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerOperationalState.setStatus("mandatory")


class _SigChanEIsdnFramerUsageState_Type(Integer32):
    """Custom type sigChanEIsdnFramerUsageState based on Integer32"""
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


_SigChanEIsdnFramerUsageState_Type.__name__ = "Integer32"
_SigChanEIsdnFramerUsageState_Object = MibTableColumn
sigChanEIsdnFramerUsageState = _SigChanEIsdnFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 12, 1, 3),
    _SigChanEIsdnFramerUsageState_Type()
)
sigChanEIsdnFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerUsageState.setStatus("mandatory")
_SigChanEIsdnFramerStatsTable_Object = MibTable
sigChanEIsdnFramerStatsTable = _SigChanEIsdnFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13)
)
if mibBuilder.loadTexts:
    sigChanEIsdnFramerStatsTable.setStatus("mandatory")
_SigChanEIsdnFramerStatsEntry_Object = MibTableRow
sigChanEIsdnFramerStatsEntry = _SigChanEIsdnFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1)
)
sigChanEIsdnFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnFramerStatsEntry.setStatus("mandatory")
_SigChanEIsdnFramerFrmToIf_Type = Counter32
_SigChanEIsdnFramerFrmToIf_Object = MibTableColumn
sigChanEIsdnFramerFrmToIf = _SigChanEIsdnFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 1),
    _SigChanEIsdnFramerFrmToIf_Type()
)
sigChanEIsdnFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerFrmToIf.setStatus("mandatory")
_SigChanEIsdnFramerFrmFromIf_Type = Counter32
_SigChanEIsdnFramerFrmFromIf_Object = MibTableColumn
sigChanEIsdnFramerFrmFromIf = _SigChanEIsdnFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 2),
    _SigChanEIsdnFramerFrmFromIf_Type()
)
sigChanEIsdnFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerFrmFromIf.setStatus("mandatory")
_SigChanEIsdnFramerOctetFromIf_Type = Counter32
_SigChanEIsdnFramerOctetFromIf_Object = MibTableColumn
sigChanEIsdnFramerOctetFromIf = _SigChanEIsdnFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 3),
    _SigChanEIsdnFramerOctetFromIf_Type()
)
sigChanEIsdnFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerOctetFromIf.setStatus("mandatory")
_SigChanEIsdnFramerAborts_Type = Counter32
_SigChanEIsdnFramerAborts_Object = MibTableColumn
sigChanEIsdnFramerAborts = _SigChanEIsdnFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 4),
    _SigChanEIsdnFramerAborts_Type()
)
sigChanEIsdnFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerAborts.setStatus("mandatory")
_SigChanEIsdnFramerCrcErrors_Type = Counter32
_SigChanEIsdnFramerCrcErrors_Object = MibTableColumn
sigChanEIsdnFramerCrcErrors = _SigChanEIsdnFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 5),
    _SigChanEIsdnFramerCrcErrors_Type()
)
sigChanEIsdnFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerCrcErrors.setStatus("mandatory")
_SigChanEIsdnFramerLrcErrors_Type = Counter32
_SigChanEIsdnFramerLrcErrors_Object = MibTableColumn
sigChanEIsdnFramerLrcErrors = _SigChanEIsdnFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 6),
    _SigChanEIsdnFramerLrcErrors_Type()
)
sigChanEIsdnFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerLrcErrors.setStatus("mandatory")
_SigChanEIsdnFramerNonOctetErrors_Type = Counter32
_SigChanEIsdnFramerNonOctetErrors_Object = MibTableColumn
sigChanEIsdnFramerNonOctetErrors = _SigChanEIsdnFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 7),
    _SigChanEIsdnFramerNonOctetErrors_Type()
)
sigChanEIsdnFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerNonOctetErrors.setStatus("mandatory")
_SigChanEIsdnFramerOverruns_Type = Counter32
_SigChanEIsdnFramerOverruns_Object = MibTableColumn
sigChanEIsdnFramerOverruns = _SigChanEIsdnFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 8),
    _SigChanEIsdnFramerOverruns_Type()
)
sigChanEIsdnFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerOverruns.setStatus("mandatory")
_SigChanEIsdnFramerUnderruns_Type = Counter32
_SigChanEIsdnFramerUnderruns_Object = MibTableColumn
sigChanEIsdnFramerUnderruns = _SigChanEIsdnFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 9),
    _SigChanEIsdnFramerUnderruns_Type()
)
sigChanEIsdnFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerUnderruns.setStatus("mandatory")
_SigChanEIsdnFramerLargeFrmErrors_Type = Counter32
_SigChanEIsdnFramerLargeFrmErrors_Object = MibTableColumn
sigChanEIsdnFramerLargeFrmErrors = _SigChanEIsdnFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 2, 13, 1, 10),
    _SigChanEIsdnFramerLargeFrmErrors_Type()
)
sigChanEIsdnFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnFramerLargeFrmErrors.setStatus("mandatory")
_SigChanEIsdnL2Table_Object = MibTable
sigChanEIsdnL2Table = _SigChanEIsdnL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 11)
)
if mibBuilder.loadTexts:
    sigChanEIsdnL2Table.setStatus("mandatory")
_SigChanEIsdnL2Entry_Object = MibTableRow
sigChanEIsdnL2Entry = _SigChanEIsdnL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 11, 1)
)
sigChanEIsdnL2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnL2Entry.setStatus("mandatory")


class _SigChanEIsdnT23_Type(Unsigned32):
    """Custom type sigChanEIsdnT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SigChanEIsdnT23_Type.__name__ = "Unsigned32"
_SigChanEIsdnT23_Object = MibTableColumn
sigChanEIsdnT23 = _SigChanEIsdnT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 11, 1, 1),
    _SigChanEIsdnT23_Type()
)
sigChanEIsdnT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnT23.setStatus("mandatory")


class _SigChanEIsdnT200_Type(Unsigned32):
    """Custom type sigChanEIsdnT200 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SigChanEIsdnT200_Type.__name__ = "Unsigned32"
_SigChanEIsdnT200_Object = MibTableColumn
sigChanEIsdnT200 = _SigChanEIsdnT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 11, 1, 2),
    _SigChanEIsdnT200_Type()
)
sigChanEIsdnT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnT200.setStatus("mandatory")


class _SigChanEIsdnN200_Type(Unsigned32):
    """Custom type sigChanEIsdnN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SigChanEIsdnN200_Type.__name__ = "Unsigned32"
_SigChanEIsdnN200_Object = MibTableColumn
sigChanEIsdnN200 = _SigChanEIsdnN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 11, 1, 3),
    _SigChanEIsdnN200_Type()
)
sigChanEIsdnN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnN200.setStatus("mandatory")


class _SigChanEIsdnT203_Type(Unsigned32):
    """Custom type sigChanEIsdnT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_SigChanEIsdnT203_Type.__name__ = "Unsigned32"
_SigChanEIsdnT203_Object = MibTableColumn
sigChanEIsdnT203 = _SigChanEIsdnT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 11, 1, 4),
    _SigChanEIsdnT203_Type()
)
sigChanEIsdnT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnT203.setStatus("mandatory")


class _SigChanEIsdnCircuitSwitchedK_Type(Unsigned32):
    """Custom type sigChanEIsdnCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SigChanEIsdnCircuitSwitchedK_Type.__name__ = "Unsigned32"
_SigChanEIsdnCircuitSwitchedK_Object = MibTableColumn
sigChanEIsdnCircuitSwitchedK = _SigChanEIsdnCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 11, 1, 6),
    _SigChanEIsdnCircuitSwitchedK_Type()
)
sigChanEIsdnCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnCircuitSwitchedK.setStatus("mandatory")
_SigChanEIsdnL3Table_Object = MibTable
sigChanEIsdnL3Table = _SigChanEIsdnL3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 12)
)
if mibBuilder.loadTexts:
    sigChanEIsdnL3Table.setStatus("mandatory")
_SigChanEIsdnL3Entry_Object = MibTableRow
sigChanEIsdnL3Entry = _SigChanEIsdnL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 12, 1)
)
sigChanEIsdnL3Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnL3Entry.setStatus("mandatory")


class _SigChanEIsdnT310_Type(Unsigned32):
    """Custom type sigChanEIsdnT310 based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_SigChanEIsdnT310_Type.__name__ = "Unsigned32"
_SigChanEIsdnT310_Object = MibTableColumn
sigChanEIsdnT310 = _SigChanEIsdnT310_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 12, 1, 4),
    _SigChanEIsdnT310_Type()
)
sigChanEIsdnT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnT310.setStatus("mandatory")
_SigChanEIsdnProvTable_Object = MibTable
sigChanEIsdnProvTable = _SigChanEIsdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 13)
)
if mibBuilder.loadTexts:
    sigChanEIsdnProvTable.setStatus("mandatory")
_SigChanEIsdnProvEntry_Object = MibTableRow
sigChanEIsdnProvEntry = _SigChanEIsdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 13, 1)
)
sigChanEIsdnProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnProvEntry.setStatus("mandatory")


class _SigChanEIsdnSide_Type(Integer32):
    """Custom type sigChanEIsdnSide based on Integer32"""
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


_SigChanEIsdnSide_Type.__name__ = "Integer32"
_SigChanEIsdnSide_Object = MibTableColumn
sigChanEIsdnSide = _SigChanEIsdnSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 13, 1, 1),
    _SigChanEIsdnSide_Type()
)
sigChanEIsdnSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnSide.setStatus("mandatory")


class _SigChanEIsdnMaxNonCallConcurrent_Type(Unsigned32):
    """Custom type sigChanEIsdnMaxNonCallConcurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SigChanEIsdnMaxNonCallConcurrent_Type.__name__ = "Unsigned32"
_SigChanEIsdnMaxNonCallConcurrent_Object = MibTableColumn
sigChanEIsdnMaxNonCallConcurrent = _SigChanEIsdnMaxNonCallConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 13, 1, 2),
    _SigChanEIsdnMaxNonCallConcurrent_Type()
)
sigChanEIsdnMaxNonCallConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnMaxNonCallConcurrent.setStatus("mandatory")


class _SigChanEIsdnOverlapSending_Type(Integer32):
    """Custom type sigChanEIsdnOverlapSending based on Integer32"""
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


_SigChanEIsdnOverlapSending_Type.__name__ = "Integer32"
_SigChanEIsdnOverlapSending_Object = MibTableColumn
sigChanEIsdnOverlapSending = _SigChanEIsdnOverlapSending_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 13, 1, 3),
    _SigChanEIsdnOverlapSending_Type()
)
sigChanEIsdnOverlapSending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnOverlapSending.setStatus("mandatory")


class _SigChanEIsdnOverlapReceiving_Type(Integer32):
    """Custom type sigChanEIsdnOverlapReceiving based on Integer32"""
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


_SigChanEIsdnOverlapReceiving_Type.__name__ = "Integer32"
_SigChanEIsdnOverlapReceiving_Object = MibTableColumn
sigChanEIsdnOverlapReceiving = _SigChanEIsdnOverlapReceiving_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 13, 1, 4),
    _SigChanEIsdnOverlapReceiving_Type()
)
sigChanEIsdnOverlapReceiving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnOverlapReceiving.setStatus("mandatory")
_SigChanEIsdnStateTable_Object = MibTable
sigChanEIsdnStateTable = _SigChanEIsdnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 14)
)
if mibBuilder.loadTexts:
    sigChanEIsdnStateTable.setStatus("mandatory")
_SigChanEIsdnStateEntry_Object = MibTableRow
sigChanEIsdnStateEntry = _SigChanEIsdnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 14, 1)
)
sigChanEIsdnStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnStateEntry.setStatus("mandatory")


class _SigChanEIsdnAdminState_Type(Integer32):
    """Custom type sigChanEIsdnAdminState based on Integer32"""
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


_SigChanEIsdnAdminState_Type.__name__ = "Integer32"
_SigChanEIsdnAdminState_Object = MibTableColumn
sigChanEIsdnAdminState = _SigChanEIsdnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 14, 1, 1),
    _SigChanEIsdnAdminState_Type()
)
sigChanEIsdnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnAdminState.setStatus("mandatory")


class _SigChanEIsdnOperationalState_Type(Integer32):
    """Custom type sigChanEIsdnOperationalState based on Integer32"""
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


_SigChanEIsdnOperationalState_Type.__name__ = "Integer32"
_SigChanEIsdnOperationalState_Object = MibTableColumn
sigChanEIsdnOperationalState = _SigChanEIsdnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 14, 1, 2),
    _SigChanEIsdnOperationalState_Type()
)
sigChanEIsdnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnOperationalState.setStatus("mandatory")


class _SigChanEIsdnUsageState_Type(Integer32):
    """Custom type sigChanEIsdnUsageState based on Integer32"""
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


_SigChanEIsdnUsageState_Type.__name__ = "Integer32"
_SigChanEIsdnUsageState_Object = MibTableColumn
sigChanEIsdnUsageState = _SigChanEIsdnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 14, 1, 3),
    _SigChanEIsdnUsageState_Type()
)
sigChanEIsdnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnUsageState.setStatus("mandatory")
_SigChanEIsdnStatsTable_Object = MibTable
sigChanEIsdnStatsTable = _SigChanEIsdnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 15)
)
if mibBuilder.loadTexts:
    sigChanEIsdnStatsTable.setStatus("mandatory")
_SigChanEIsdnStatsEntry_Object = MibTableRow
sigChanEIsdnStatsEntry = _SigChanEIsdnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 15, 1)
)
sigChanEIsdnStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnStatsEntry.setStatus("mandatory")
_SigChanEIsdnTotalCallsToIf_Type = Counter32
_SigChanEIsdnTotalCallsToIf_Object = MibTableColumn
sigChanEIsdnTotalCallsToIf = _SigChanEIsdnTotalCallsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 15, 1, 2),
    _SigChanEIsdnTotalCallsToIf_Type()
)
sigChanEIsdnTotalCallsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnTotalCallsToIf.setStatus("mandatory")
_SigChanEIsdnTotalCallsFromIf_Type = Counter32
_SigChanEIsdnTotalCallsFromIf_Object = MibTableColumn
sigChanEIsdnTotalCallsFromIf = _SigChanEIsdnTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 15, 1, 3),
    _SigChanEIsdnTotalCallsFromIf_Type()
)
sigChanEIsdnTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnTotalCallsFromIf.setStatus("mandatory")
_SigChanEIsdnNonCallAssocSessionsToIf_Type = Counter32
_SigChanEIsdnNonCallAssocSessionsToIf_Object = MibTableColumn
sigChanEIsdnNonCallAssocSessionsToIf = _SigChanEIsdnNonCallAssocSessionsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 15, 1, 4),
    _SigChanEIsdnNonCallAssocSessionsToIf_Type()
)
sigChanEIsdnNonCallAssocSessionsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnNonCallAssocSessionsToIf.setStatus("mandatory")
_SigChanEIsdnNonCallAssocSessionsFromIf_Type = Counter32
_SigChanEIsdnNonCallAssocSessionsFromIf_Object = MibTableColumn
sigChanEIsdnNonCallAssocSessionsFromIf = _SigChanEIsdnNonCallAssocSessionsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 15, 1, 5),
    _SigChanEIsdnNonCallAssocSessionsFromIf_Type()
)
sigChanEIsdnNonCallAssocSessionsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnNonCallAssocSessionsFromIf.setStatus("mandatory")
_SigChanEIsdnOperTable_Object = MibTable
sigChanEIsdnOperTable = _SigChanEIsdnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 16)
)
if mibBuilder.loadTexts:
    sigChanEIsdnOperTable.setStatus("mandatory")
_SigChanEIsdnOperEntry_Object = MibTableRow
sigChanEIsdnOperEntry = _SigChanEIsdnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 16, 1)
)
sigChanEIsdnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnOperEntry.setStatus("mandatory")


class _SigChanEIsdnActiveChannels_Type(Gauge32):
    """Custom type sigChanEIsdnActiveChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEIsdnActiveChannels_Type.__name__ = "Gauge32"
_SigChanEIsdnActiveChannels_Object = MibTableColumn
sigChanEIsdnActiveChannels = _SigChanEIsdnActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 16, 1, 1),
    _SigChanEIsdnActiveChannels_Type()
)
sigChanEIsdnActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnActiveChannels.setStatus("mandatory")


class _SigChanEIsdnActiveVoiceChannels_Type(Gauge32):
    """Custom type sigChanEIsdnActiveVoiceChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEIsdnActiveVoiceChannels_Type.__name__ = "Gauge32"
_SigChanEIsdnActiveVoiceChannels_Object = MibTableColumn
sigChanEIsdnActiveVoiceChannels = _SigChanEIsdnActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 16, 1, 2),
    _SigChanEIsdnActiveVoiceChannels_Type()
)
sigChanEIsdnActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnActiveVoiceChannels.setStatus("mandatory")


class _SigChanEIsdnActiveDataChannels_Type(Gauge32):
    """Custom type sigChanEIsdnActiveDataChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEIsdnActiveDataChannels_Type.__name__ = "Gauge32"
_SigChanEIsdnActiveDataChannels_Object = MibTableColumn
sigChanEIsdnActiveDataChannels = _SigChanEIsdnActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 16, 1, 3),
    _SigChanEIsdnActiveDataChannels_Type()
)
sigChanEIsdnActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnActiveDataChannels.setStatus("mandatory")


class _SigChanEIsdnPeakActiveChannels_Type(Gauge32):
    """Custom type sigChanEIsdnPeakActiveChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEIsdnPeakActiveChannels_Type.__name__ = "Gauge32"
_SigChanEIsdnPeakActiveChannels_Object = MibTableColumn
sigChanEIsdnPeakActiveChannels = _SigChanEIsdnPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 16, 1, 4),
    _SigChanEIsdnPeakActiveChannels_Type()
)
sigChanEIsdnPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnPeakActiveChannels.setStatus("mandatory")


class _SigChanEIsdnPeakActiveVoiceChannels_Type(Gauge32):
    """Custom type sigChanEIsdnPeakActiveVoiceChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEIsdnPeakActiveVoiceChannels_Type.__name__ = "Gauge32"
_SigChanEIsdnPeakActiveVoiceChannels_Object = MibTableColumn
sigChanEIsdnPeakActiveVoiceChannels = _SigChanEIsdnPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 16, 1, 5),
    _SigChanEIsdnPeakActiveVoiceChannels_Type()
)
sigChanEIsdnPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnPeakActiveVoiceChannels.setStatus("mandatory")


class _SigChanEIsdnPeakActiveDataChannels_Type(Gauge32):
    """Custom type sigChanEIsdnPeakActiveDataChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEIsdnPeakActiveDataChannels_Type.__name__ = "Gauge32"
_SigChanEIsdnPeakActiveDataChannels_Object = MibTableColumn
sigChanEIsdnPeakActiveDataChannels = _SigChanEIsdnPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 16, 1, 6),
    _SigChanEIsdnPeakActiveDataChannels_Type()
)
sigChanEIsdnPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnPeakActiveDataChannels.setStatus("mandatory")


class _SigChanEIsdnDChanStatus_Type(Integer32):
    """Custom type sigChanEIsdnDChanStatus based on Integer32"""
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


_SigChanEIsdnDChanStatus_Type.__name__ = "Integer32"
_SigChanEIsdnDChanStatus_Object = MibTableColumn
sigChanEIsdnDChanStatus = _SigChanEIsdnDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 16, 1, 7),
    _SigChanEIsdnDChanStatus_Type()
)
sigChanEIsdnDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEIsdnDChanStatus.setStatus("mandatory")
_SigChanEIsdnToolsTable_Object = MibTable
sigChanEIsdnToolsTable = _SigChanEIsdnToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 17)
)
if mibBuilder.loadTexts:
    sigChanEIsdnToolsTable.setStatus("mandatory")
_SigChanEIsdnToolsEntry_Object = MibTableRow
sigChanEIsdnToolsEntry = _SigChanEIsdnToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 17, 1)
)
sigChanEIsdnToolsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnToolsEntry.setStatus("mandatory")


class _SigChanEIsdnTracing_Type(OctetString):
    """Custom type sigChanEIsdnTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SigChanEIsdnTracing_Type.__name__ = "OctetString"
_SigChanEIsdnTracing_Object = MibTableColumn
sigChanEIsdnTracing = _SigChanEIsdnTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 17, 1, 1),
    _SigChanEIsdnTracing_Type()
)
sigChanEIsdnTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnTracing.setStatus("mandatory")
_SigChanEIsdnOptTable_Object = MibTable
sigChanEIsdnOptTable = _SigChanEIsdnOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 18)
)
if mibBuilder.loadTexts:
    sigChanEIsdnOptTable.setStatus("mandatory")
_SigChanEIsdnOptEntry_Object = MibTableRow
sigChanEIsdnOptEntry = _SigChanEIsdnOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 18, 1)
)
sigChanEIsdnOptEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEuroIsdnMIB", "sigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    sigChanEIsdnOptEntry.setStatus("mandatory")


class _SigChanEIsdnVariant_Type(Integer32):
    """Custom type sigChanEIsdnVariant based on Integer32"""
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
        *(("austria", 1),
          ("etsiGeneric", 0),
          ("germany", 2))
    )


_SigChanEIsdnVariant_Type.__name__ = "Integer32"
_SigChanEIsdnVariant_Object = MibTableColumn
sigChanEIsdnVariant = _SigChanEIsdnVariant_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 18, 1, 1),
    _SigChanEIsdnVariant_Type()
)
sigChanEIsdnVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnVariant.setStatus("mandatory")


class _SigChanEIsdnConnectServiceTimer_Type(Unsigned32):
    """Custom type sigChanEIsdnConnectServiceTimer based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SigChanEIsdnConnectServiceTimer_Type.__name__ = "Unsigned32"
_SigChanEIsdnConnectServiceTimer_Object = MibTableColumn
sigChanEIsdnConnectServiceTimer = _SigChanEIsdnConnectServiceTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 18, 1, 2),
    _SigChanEIsdnConnectServiceTimer_Type()
)
sigChanEIsdnConnectServiceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnConnectServiceTimer.setStatus("mandatory")


class _SigChanEIsdnResponseServiceTimer_Type(Unsigned32):
    """Custom type sigChanEIsdnResponseServiceTimer based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SigChanEIsdnResponseServiceTimer_Type.__name__ = "Unsigned32"
_SigChanEIsdnResponseServiceTimer_Object = MibTableColumn
sigChanEIsdnResponseServiceTimer = _SigChanEIsdnResponseServiceTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 18, 1, 3),
    _SigChanEIsdnResponseServiceTimer_Type()
)
sigChanEIsdnResponseServiceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnResponseServiceTimer.setStatus("mandatory")


class _SigChanEIsdnLifetimeServiceTimer_Type(Unsigned32):
    """Custom type sigChanEIsdnLifetimeServiceTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_SigChanEIsdnLifetimeServiceTimer_Type.__name__ = "Unsigned32"
_SigChanEIsdnLifetimeServiceTimer_Object = MibTableColumn
sigChanEIsdnLifetimeServiceTimer = _SigChanEIsdnLifetimeServiceTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 14, 18, 1, 4),
    _SigChanEIsdnLifetimeServiceTimer_Type()
)
sigChanEIsdnLifetimeServiceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEIsdnLifetimeServiceTimer.setStatus("mandatory")
_VnetEuroIsdnMIB_ObjectIdentity = ObjectIdentity
vnetEuroIsdnMIB = _VnetEuroIsdnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 138)
)
_VnetEuroIsdnGroup_ObjectIdentity = ObjectIdentity
vnetEuroIsdnGroup = _VnetEuroIsdnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 138, 1)
)
_VnetEuroIsdnGroupBE_ObjectIdentity = ObjectIdentity
vnetEuroIsdnGroupBE = _VnetEuroIsdnGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 138, 1, 5)
)
_VnetEuroIsdnGroupBE01_ObjectIdentity = ObjectIdentity
vnetEuroIsdnGroupBE01 = _VnetEuroIsdnGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 138, 1, 5, 2)
)
_VnetEuroIsdnGroupBE01A_ObjectIdentity = ObjectIdentity
vnetEuroIsdnGroupBE01A = _VnetEuroIsdnGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 138, 1, 5, 2, 2)
)
_VnetEuroIsdnCapabilities_ObjectIdentity = ObjectIdentity
vnetEuroIsdnCapabilities = _VnetEuroIsdnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 138, 3)
)
_VnetEuroIsdnCapabilitiesBE_ObjectIdentity = ObjectIdentity
vnetEuroIsdnCapabilitiesBE = _VnetEuroIsdnCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 138, 3, 5)
)
_VnetEuroIsdnCapabilitiesBE01_ObjectIdentity = ObjectIdentity
vnetEuroIsdnCapabilitiesBE01 = _VnetEuroIsdnCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 138, 3, 5, 2)
)
_VnetEuroIsdnCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
vnetEuroIsdnCapabilitiesBE01A = _VnetEuroIsdnCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 138, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VnetEuroIsdnMIB",
    **{"sigChanEIsdn": sigChanEIsdn,
       "sigChanEIsdnRowStatusTable": sigChanEIsdnRowStatusTable,
       "sigChanEIsdnRowStatusEntry": sigChanEIsdnRowStatusEntry,
       "sigChanEIsdnRowStatus": sigChanEIsdnRowStatus,
       "sigChanEIsdnComponentName": sigChanEIsdnComponentName,
       "sigChanEIsdnStorageType": sigChanEIsdnStorageType,
       "sigChanEIsdnIndex": sigChanEIsdnIndex,
       "sigChanEIsdnFramer": sigChanEIsdnFramer,
       "sigChanEIsdnFramerRowStatusTable": sigChanEIsdnFramerRowStatusTable,
       "sigChanEIsdnFramerRowStatusEntry": sigChanEIsdnFramerRowStatusEntry,
       "sigChanEIsdnFramerRowStatus": sigChanEIsdnFramerRowStatus,
       "sigChanEIsdnFramerComponentName": sigChanEIsdnFramerComponentName,
       "sigChanEIsdnFramerStorageType": sigChanEIsdnFramerStorageType,
       "sigChanEIsdnFramerIndex": sigChanEIsdnFramerIndex,
       "sigChanEIsdnFramerProvTable": sigChanEIsdnFramerProvTable,
       "sigChanEIsdnFramerProvEntry": sigChanEIsdnFramerProvEntry,
       "sigChanEIsdnFramerInterfaceName": sigChanEIsdnFramerInterfaceName,
       "sigChanEIsdnFramerStateTable": sigChanEIsdnFramerStateTable,
       "sigChanEIsdnFramerStateEntry": sigChanEIsdnFramerStateEntry,
       "sigChanEIsdnFramerAdminState": sigChanEIsdnFramerAdminState,
       "sigChanEIsdnFramerOperationalState": sigChanEIsdnFramerOperationalState,
       "sigChanEIsdnFramerUsageState": sigChanEIsdnFramerUsageState,
       "sigChanEIsdnFramerStatsTable": sigChanEIsdnFramerStatsTable,
       "sigChanEIsdnFramerStatsEntry": sigChanEIsdnFramerStatsEntry,
       "sigChanEIsdnFramerFrmToIf": sigChanEIsdnFramerFrmToIf,
       "sigChanEIsdnFramerFrmFromIf": sigChanEIsdnFramerFrmFromIf,
       "sigChanEIsdnFramerOctetFromIf": sigChanEIsdnFramerOctetFromIf,
       "sigChanEIsdnFramerAborts": sigChanEIsdnFramerAborts,
       "sigChanEIsdnFramerCrcErrors": sigChanEIsdnFramerCrcErrors,
       "sigChanEIsdnFramerLrcErrors": sigChanEIsdnFramerLrcErrors,
       "sigChanEIsdnFramerNonOctetErrors": sigChanEIsdnFramerNonOctetErrors,
       "sigChanEIsdnFramerOverruns": sigChanEIsdnFramerOverruns,
       "sigChanEIsdnFramerUnderruns": sigChanEIsdnFramerUnderruns,
       "sigChanEIsdnFramerLargeFrmErrors": sigChanEIsdnFramerLargeFrmErrors,
       "sigChanEIsdnL2Table": sigChanEIsdnL2Table,
       "sigChanEIsdnL2Entry": sigChanEIsdnL2Entry,
       "sigChanEIsdnT23": sigChanEIsdnT23,
       "sigChanEIsdnT200": sigChanEIsdnT200,
       "sigChanEIsdnN200": sigChanEIsdnN200,
       "sigChanEIsdnT203": sigChanEIsdnT203,
       "sigChanEIsdnCircuitSwitchedK": sigChanEIsdnCircuitSwitchedK,
       "sigChanEIsdnL3Table": sigChanEIsdnL3Table,
       "sigChanEIsdnL3Entry": sigChanEIsdnL3Entry,
       "sigChanEIsdnT310": sigChanEIsdnT310,
       "sigChanEIsdnProvTable": sigChanEIsdnProvTable,
       "sigChanEIsdnProvEntry": sigChanEIsdnProvEntry,
       "sigChanEIsdnSide": sigChanEIsdnSide,
       "sigChanEIsdnMaxNonCallConcurrent": sigChanEIsdnMaxNonCallConcurrent,
       "sigChanEIsdnOverlapSending": sigChanEIsdnOverlapSending,
       "sigChanEIsdnOverlapReceiving": sigChanEIsdnOverlapReceiving,
       "sigChanEIsdnStateTable": sigChanEIsdnStateTable,
       "sigChanEIsdnStateEntry": sigChanEIsdnStateEntry,
       "sigChanEIsdnAdminState": sigChanEIsdnAdminState,
       "sigChanEIsdnOperationalState": sigChanEIsdnOperationalState,
       "sigChanEIsdnUsageState": sigChanEIsdnUsageState,
       "sigChanEIsdnStatsTable": sigChanEIsdnStatsTable,
       "sigChanEIsdnStatsEntry": sigChanEIsdnStatsEntry,
       "sigChanEIsdnTotalCallsToIf": sigChanEIsdnTotalCallsToIf,
       "sigChanEIsdnTotalCallsFromIf": sigChanEIsdnTotalCallsFromIf,
       "sigChanEIsdnNonCallAssocSessionsToIf": sigChanEIsdnNonCallAssocSessionsToIf,
       "sigChanEIsdnNonCallAssocSessionsFromIf": sigChanEIsdnNonCallAssocSessionsFromIf,
       "sigChanEIsdnOperTable": sigChanEIsdnOperTable,
       "sigChanEIsdnOperEntry": sigChanEIsdnOperEntry,
       "sigChanEIsdnActiveChannels": sigChanEIsdnActiveChannels,
       "sigChanEIsdnActiveVoiceChannels": sigChanEIsdnActiveVoiceChannels,
       "sigChanEIsdnActiveDataChannels": sigChanEIsdnActiveDataChannels,
       "sigChanEIsdnPeakActiveChannels": sigChanEIsdnPeakActiveChannels,
       "sigChanEIsdnPeakActiveVoiceChannels": sigChanEIsdnPeakActiveVoiceChannels,
       "sigChanEIsdnPeakActiveDataChannels": sigChanEIsdnPeakActiveDataChannels,
       "sigChanEIsdnDChanStatus": sigChanEIsdnDChanStatus,
       "sigChanEIsdnToolsTable": sigChanEIsdnToolsTable,
       "sigChanEIsdnToolsEntry": sigChanEIsdnToolsEntry,
       "sigChanEIsdnTracing": sigChanEIsdnTracing,
       "sigChanEIsdnOptTable": sigChanEIsdnOptTable,
       "sigChanEIsdnOptEntry": sigChanEIsdnOptEntry,
       "sigChanEIsdnVariant": sigChanEIsdnVariant,
       "sigChanEIsdnConnectServiceTimer": sigChanEIsdnConnectServiceTimer,
       "sigChanEIsdnResponseServiceTimer": sigChanEIsdnResponseServiceTimer,
       "sigChanEIsdnLifetimeServiceTimer": sigChanEIsdnLifetimeServiceTimer,
       "vnetEuroIsdnMIB": vnetEuroIsdnMIB,
       "vnetEuroIsdnGroup": vnetEuroIsdnGroup,
       "vnetEuroIsdnGroupBE": vnetEuroIsdnGroupBE,
       "vnetEuroIsdnGroupBE01": vnetEuroIsdnGroupBE01,
       "vnetEuroIsdnGroupBE01A": vnetEuroIsdnGroupBE01A,
       "vnetEuroIsdnCapabilities": vnetEuroIsdnCapabilities,
       "vnetEuroIsdnCapabilitiesBE": vnetEuroIsdnCapabilitiesBE,
       "vnetEuroIsdnCapabilitiesBE01": vnetEuroIsdnCapabilitiesBE01,
       "vnetEuroIsdnCapabilitiesBE01A": vnetEuroIsdnCapabilitiesBE01A}
)
