# SNMP MIB module (Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:18 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
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

(mscSigChan,
 mscSigChanIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB",
    "mscSigChan",
    "mscSigChanIndex")

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

_MscSigChanMcdn_ObjectIdentity = ObjectIdentity
mscSigChanMcdn = _MscSigChanMcdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17)
)
_MscSigChanMcdnRowStatusTable_Object = MibTable
mscSigChanMcdnRowStatusTable = _MscSigChanMcdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 1)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnRowStatusTable.setStatus("mandatory")
_MscSigChanMcdnRowStatusEntry_Object = MibTableRow
mscSigChanMcdnRowStatusEntry = _MscSigChanMcdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 1, 1)
)
mscSigChanMcdnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnRowStatusEntry.setStatus("mandatory")
_MscSigChanMcdnRowStatus_Type = RowStatus
_MscSigChanMcdnRowStatus_Object = MibTableColumn
mscSigChanMcdnRowStatus = _MscSigChanMcdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 1, 1, 1),
    _MscSigChanMcdnRowStatus_Type()
)
mscSigChanMcdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnRowStatus.setStatus("mandatory")
_MscSigChanMcdnComponentName_Type = DisplayString
_MscSigChanMcdnComponentName_Object = MibTableColumn
mscSigChanMcdnComponentName = _MscSigChanMcdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 1, 1, 2),
    _MscSigChanMcdnComponentName_Type()
)
mscSigChanMcdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnComponentName.setStatus("mandatory")
_MscSigChanMcdnStorageType_Type = StorageType
_MscSigChanMcdnStorageType_Object = MibTableColumn
mscSigChanMcdnStorageType = _MscSigChanMcdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 1, 1, 4),
    _MscSigChanMcdnStorageType_Type()
)
mscSigChanMcdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnStorageType.setStatus("mandatory")
_MscSigChanMcdnIndex_Type = NonReplicated
_MscSigChanMcdnIndex_Object = MibTableColumn
mscSigChanMcdnIndex = _MscSigChanMcdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 1, 1, 10),
    _MscSigChanMcdnIndex_Type()
)
mscSigChanMcdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanMcdnIndex.setStatus("mandatory")
_MscSigChanMcdnFramer_ObjectIdentity = ObjectIdentity
mscSigChanMcdnFramer = _MscSigChanMcdnFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2)
)
_MscSigChanMcdnFramerRowStatusTable_Object = MibTable
mscSigChanMcdnFramerRowStatusTable = _MscSigChanMcdnFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 1)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerRowStatusTable.setStatus("mandatory")
_MscSigChanMcdnFramerRowStatusEntry_Object = MibTableRow
mscSigChanMcdnFramerRowStatusEntry = _MscSigChanMcdnFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 1, 1)
)
mscSigChanMcdnFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerRowStatusEntry.setStatus("mandatory")
_MscSigChanMcdnFramerRowStatus_Type = RowStatus
_MscSigChanMcdnFramerRowStatus_Object = MibTableColumn
mscSigChanMcdnFramerRowStatus = _MscSigChanMcdnFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 1, 1, 1),
    _MscSigChanMcdnFramerRowStatus_Type()
)
mscSigChanMcdnFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerRowStatus.setStatus("mandatory")
_MscSigChanMcdnFramerComponentName_Type = DisplayString
_MscSigChanMcdnFramerComponentName_Object = MibTableColumn
mscSigChanMcdnFramerComponentName = _MscSigChanMcdnFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 1, 1, 2),
    _MscSigChanMcdnFramerComponentName_Type()
)
mscSigChanMcdnFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerComponentName.setStatus("mandatory")
_MscSigChanMcdnFramerStorageType_Type = StorageType
_MscSigChanMcdnFramerStorageType_Object = MibTableColumn
mscSigChanMcdnFramerStorageType = _MscSigChanMcdnFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 1, 1, 4),
    _MscSigChanMcdnFramerStorageType_Type()
)
mscSigChanMcdnFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerStorageType.setStatus("mandatory")
_MscSigChanMcdnFramerIndex_Type = NonReplicated
_MscSigChanMcdnFramerIndex_Object = MibTableColumn
mscSigChanMcdnFramerIndex = _MscSigChanMcdnFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 1, 1, 10),
    _MscSigChanMcdnFramerIndex_Type()
)
mscSigChanMcdnFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerIndex.setStatus("mandatory")
_MscSigChanMcdnFramerProvTable_Object = MibTable
mscSigChanMcdnFramerProvTable = _MscSigChanMcdnFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 10)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerProvTable.setStatus("mandatory")
_MscSigChanMcdnFramerProvEntry_Object = MibTableRow
mscSigChanMcdnFramerProvEntry = _MscSigChanMcdnFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 10, 1)
)
mscSigChanMcdnFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerProvEntry.setStatus("mandatory")
_MscSigChanMcdnFramerInterfaceName_Type = Link
_MscSigChanMcdnFramerInterfaceName_Object = MibTableColumn
mscSigChanMcdnFramerInterfaceName = _MscSigChanMcdnFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 10, 1, 1),
    _MscSigChanMcdnFramerInterfaceName_Type()
)
mscSigChanMcdnFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerInterfaceName.setStatus("mandatory")
_MscSigChanMcdnFramerStateTable_Object = MibTable
mscSigChanMcdnFramerStateTable = _MscSigChanMcdnFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 12)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerStateTable.setStatus("mandatory")
_MscSigChanMcdnFramerStateEntry_Object = MibTableRow
mscSigChanMcdnFramerStateEntry = _MscSigChanMcdnFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 12, 1)
)
mscSigChanMcdnFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerStateEntry.setStatus("mandatory")


class _MscSigChanMcdnFramerAdminState_Type(Integer32):
    """Custom type mscSigChanMcdnFramerAdminState based on Integer32"""
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


_MscSigChanMcdnFramerAdminState_Type.__name__ = "Integer32"
_MscSigChanMcdnFramerAdminState_Object = MibTableColumn
mscSigChanMcdnFramerAdminState = _MscSigChanMcdnFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 12, 1, 1),
    _MscSigChanMcdnFramerAdminState_Type()
)
mscSigChanMcdnFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerAdminState.setStatus("mandatory")


class _MscSigChanMcdnFramerOperationalState_Type(Integer32):
    """Custom type mscSigChanMcdnFramerOperationalState based on Integer32"""
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


_MscSigChanMcdnFramerOperationalState_Type.__name__ = "Integer32"
_MscSigChanMcdnFramerOperationalState_Object = MibTableColumn
mscSigChanMcdnFramerOperationalState = _MscSigChanMcdnFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 12, 1, 2),
    _MscSigChanMcdnFramerOperationalState_Type()
)
mscSigChanMcdnFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerOperationalState.setStatus("mandatory")


class _MscSigChanMcdnFramerUsageState_Type(Integer32):
    """Custom type mscSigChanMcdnFramerUsageState based on Integer32"""
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


_MscSigChanMcdnFramerUsageState_Type.__name__ = "Integer32"
_MscSigChanMcdnFramerUsageState_Object = MibTableColumn
mscSigChanMcdnFramerUsageState = _MscSigChanMcdnFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 12, 1, 3),
    _MscSigChanMcdnFramerUsageState_Type()
)
mscSigChanMcdnFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerUsageState.setStatus("mandatory")
_MscSigChanMcdnFramerStatsTable_Object = MibTable
mscSigChanMcdnFramerStatsTable = _MscSigChanMcdnFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerStatsTable.setStatus("mandatory")
_MscSigChanMcdnFramerStatsEntry_Object = MibTableRow
mscSigChanMcdnFramerStatsEntry = _MscSigChanMcdnFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1)
)
mscSigChanMcdnFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerStatsEntry.setStatus("mandatory")
_MscSigChanMcdnFramerFrmToIf_Type = Counter32
_MscSigChanMcdnFramerFrmToIf_Object = MibTableColumn
mscSigChanMcdnFramerFrmToIf = _MscSigChanMcdnFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 1),
    _MscSigChanMcdnFramerFrmToIf_Type()
)
mscSigChanMcdnFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerFrmToIf.setStatus("mandatory")
_MscSigChanMcdnFramerFrmFromIf_Type = Counter32
_MscSigChanMcdnFramerFrmFromIf_Object = MibTableColumn
mscSigChanMcdnFramerFrmFromIf = _MscSigChanMcdnFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 2),
    _MscSigChanMcdnFramerFrmFromIf_Type()
)
mscSigChanMcdnFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerFrmFromIf.setStatus("mandatory")
_MscSigChanMcdnFramerOctetFromIf_Type = Counter32
_MscSigChanMcdnFramerOctetFromIf_Object = MibTableColumn
mscSigChanMcdnFramerOctetFromIf = _MscSigChanMcdnFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 3),
    _MscSigChanMcdnFramerOctetFromIf_Type()
)
mscSigChanMcdnFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerOctetFromIf.setStatus("mandatory")
_MscSigChanMcdnFramerAborts_Type = Counter32
_MscSigChanMcdnFramerAborts_Object = MibTableColumn
mscSigChanMcdnFramerAborts = _MscSigChanMcdnFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 4),
    _MscSigChanMcdnFramerAborts_Type()
)
mscSigChanMcdnFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerAborts.setStatus("mandatory")
_MscSigChanMcdnFramerCrcErrors_Type = Counter32
_MscSigChanMcdnFramerCrcErrors_Object = MibTableColumn
mscSigChanMcdnFramerCrcErrors = _MscSigChanMcdnFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 5),
    _MscSigChanMcdnFramerCrcErrors_Type()
)
mscSigChanMcdnFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerCrcErrors.setStatus("mandatory")
_MscSigChanMcdnFramerLrcErrors_Type = Counter32
_MscSigChanMcdnFramerLrcErrors_Object = MibTableColumn
mscSigChanMcdnFramerLrcErrors = _MscSigChanMcdnFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 6),
    _MscSigChanMcdnFramerLrcErrors_Type()
)
mscSigChanMcdnFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerLrcErrors.setStatus("mandatory")
_MscSigChanMcdnFramerNonOctetErrors_Type = Counter32
_MscSigChanMcdnFramerNonOctetErrors_Object = MibTableColumn
mscSigChanMcdnFramerNonOctetErrors = _MscSigChanMcdnFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 7),
    _MscSigChanMcdnFramerNonOctetErrors_Type()
)
mscSigChanMcdnFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerNonOctetErrors.setStatus("mandatory")
_MscSigChanMcdnFramerOverruns_Type = Counter32
_MscSigChanMcdnFramerOverruns_Object = MibTableColumn
mscSigChanMcdnFramerOverruns = _MscSigChanMcdnFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 8),
    _MscSigChanMcdnFramerOverruns_Type()
)
mscSigChanMcdnFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerOverruns.setStatus("mandatory")
_MscSigChanMcdnFramerUnderruns_Type = Counter32
_MscSigChanMcdnFramerUnderruns_Object = MibTableColumn
mscSigChanMcdnFramerUnderruns = _MscSigChanMcdnFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 9),
    _MscSigChanMcdnFramerUnderruns_Type()
)
mscSigChanMcdnFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerUnderruns.setStatus("mandatory")
_MscSigChanMcdnFramerLargeFrmErrors_Type = Counter32
_MscSigChanMcdnFramerLargeFrmErrors_Object = MibTableColumn
mscSigChanMcdnFramerLargeFrmErrors = _MscSigChanMcdnFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 2, 13, 1, 10),
    _MscSigChanMcdnFramerLargeFrmErrors_Type()
)
mscSigChanMcdnFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnFramerLargeFrmErrors.setStatus("mandatory")
_MscSigChanMcdnL2Table_Object = MibTable
mscSigChanMcdnL2Table = _MscSigChanMcdnL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 11)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnL2Table.setStatus("mandatory")
_MscSigChanMcdnL2Entry_Object = MibTableRow
mscSigChanMcdnL2Entry = _MscSigChanMcdnL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 11, 1)
)
mscSigChanMcdnL2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnL2Entry.setStatus("mandatory")


class _MscSigChanMcdnT23_Type(Unsigned32):
    """Custom type mscSigChanMcdnT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscSigChanMcdnT23_Type.__name__ = "Unsigned32"
_MscSigChanMcdnT23_Object = MibTableColumn
mscSigChanMcdnT23 = _MscSigChanMcdnT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 11, 1, 1),
    _MscSigChanMcdnT23_Type()
)
mscSigChanMcdnT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnT23.setStatus("mandatory")


class _MscSigChanMcdnT200_Type(Unsigned32):
    """Custom type mscSigChanMcdnT200 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscSigChanMcdnT200_Type.__name__ = "Unsigned32"
_MscSigChanMcdnT200_Object = MibTableColumn
mscSigChanMcdnT200 = _MscSigChanMcdnT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 11, 1, 2),
    _MscSigChanMcdnT200_Type()
)
mscSigChanMcdnT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnT200.setStatus("mandatory")


class _MscSigChanMcdnN200_Type(Unsigned32):
    """Custom type mscSigChanMcdnN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscSigChanMcdnN200_Type.__name__ = "Unsigned32"
_MscSigChanMcdnN200_Object = MibTableColumn
mscSigChanMcdnN200 = _MscSigChanMcdnN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 11, 1, 3),
    _MscSigChanMcdnN200_Type()
)
mscSigChanMcdnN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnN200.setStatus("mandatory")


class _MscSigChanMcdnT203_Type(Unsigned32):
    """Custom type mscSigChanMcdnT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_MscSigChanMcdnT203_Type.__name__ = "Unsigned32"
_MscSigChanMcdnT203_Object = MibTableColumn
mscSigChanMcdnT203 = _MscSigChanMcdnT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 11, 1, 4),
    _MscSigChanMcdnT203_Type()
)
mscSigChanMcdnT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnT203.setStatus("mandatory")


class _MscSigChanMcdnCircuitSwitchedK_Type(Unsigned32):
    """Custom type mscSigChanMcdnCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscSigChanMcdnCircuitSwitchedK_Type.__name__ = "Unsigned32"
_MscSigChanMcdnCircuitSwitchedK_Object = MibTableColumn
mscSigChanMcdnCircuitSwitchedK = _MscSigChanMcdnCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 11, 1, 6),
    _MscSigChanMcdnCircuitSwitchedK_Type()
)
mscSigChanMcdnCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnCircuitSwitchedK.setStatus("mandatory")
_MscSigChanMcdnL3Table_Object = MibTable
mscSigChanMcdnL3Table = _MscSigChanMcdnL3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 12)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnL3Table.setStatus("mandatory")
_MscSigChanMcdnL3Entry_Object = MibTableRow
mscSigChanMcdnL3Entry = _MscSigChanMcdnL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 12, 1)
)
mscSigChanMcdnL3Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnL3Entry.setStatus("mandatory")


class _MscSigChanMcdnT302_Type(Unsigned32):
    """Custom type mscSigChanMcdnT302 based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_MscSigChanMcdnT302_Type.__name__ = "Unsigned32"
_MscSigChanMcdnT302_Object = MibTableColumn
mscSigChanMcdnT302 = _MscSigChanMcdnT302_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 12, 1, 1),
    _MscSigChanMcdnT302_Type()
)
mscSigChanMcdnT302.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnT302.setStatus("mandatory")


class _MscSigChanMcdnT304_Type(Unsigned32):
    """Custom type mscSigChanMcdnT304 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_MscSigChanMcdnT304_Type.__name__ = "Unsigned32"
_MscSigChanMcdnT304_Object = MibTableColumn
mscSigChanMcdnT304 = _MscSigChanMcdnT304_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 12, 1, 2),
    _MscSigChanMcdnT304_Type()
)
mscSigChanMcdnT304.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnT304.setStatus("mandatory")


class _MscSigChanMcdnT309_Type(Unsigned32):
    """Custom type mscSigChanMcdnT309 based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 120),
    )


_MscSigChanMcdnT309_Type.__name__ = "Unsigned32"
_MscSigChanMcdnT309_Object = MibTableColumn
mscSigChanMcdnT309 = _MscSigChanMcdnT309_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 12, 1, 3),
    _MscSigChanMcdnT309_Type()
)
mscSigChanMcdnT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnT309.setStatus("mandatory")


class _MscSigChanMcdnT310_Type(Unsigned32):
    """Custom type mscSigChanMcdnT310 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_MscSigChanMcdnT310_Type.__name__ = "Unsigned32"
_MscSigChanMcdnT310_Object = MibTableColumn
mscSigChanMcdnT310 = _MscSigChanMcdnT310_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 12, 1, 4),
    _MscSigChanMcdnT310_Type()
)
mscSigChanMcdnT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnT310.setStatus("mandatory")


class _MscSigChanMcdnT316_Type(Unsigned32):
    """Custom type mscSigChanMcdnT316 based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(31, 180),
    )


_MscSigChanMcdnT316_Type.__name__ = "Unsigned32"
_MscSigChanMcdnT316_Object = MibTableColumn
mscSigChanMcdnT316 = _MscSigChanMcdnT316_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 12, 1, 5),
    _MscSigChanMcdnT316_Type()
)
mscSigChanMcdnT316.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnT316.setStatus("mandatory")


class _MscSigChanMcdnT317_Type(Unsigned32):
    """Custom type mscSigChanMcdnT317 based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 179),
    )


_MscSigChanMcdnT317_Type.__name__ = "Unsigned32"
_MscSigChanMcdnT317_Object = MibTableColumn
mscSigChanMcdnT317 = _MscSigChanMcdnT317_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 12, 1, 6),
    _MscSigChanMcdnT317_Type()
)
mscSigChanMcdnT317.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnT317.setStatus("mandatory")
_MscSigChanMcdnProvTable_Object = MibTable
mscSigChanMcdnProvTable = _MscSigChanMcdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 13)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnProvTable.setStatus("mandatory")
_MscSigChanMcdnProvEntry_Object = MibTableRow
mscSigChanMcdnProvEntry = _MscSigChanMcdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 13, 1)
)
mscSigChanMcdnProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnProvEntry.setStatus("mandatory")


class _MscSigChanMcdnSide_Type(Integer32):
    """Custom type mscSigChanMcdnSide based on Integer32"""
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


_MscSigChanMcdnSide_Type.__name__ = "Integer32"
_MscSigChanMcdnSide_Object = MibTableColumn
mscSigChanMcdnSide = _MscSigChanMcdnSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 13, 1, 1),
    _MscSigChanMcdnSide_Type()
)
mscSigChanMcdnSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnSide.setStatus("mandatory")


class _MscSigChanMcdnMaxNonCallConcurrent_Type(Unsigned32):
    """Custom type mscSigChanMcdnMaxNonCallConcurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MscSigChanMcdnMaxNonCallConcurrent_Type.__name__ = "Unsigned32"
_MscSigChanMcdnMaxNonCallConcurrent_Object = MibTableColumn
mscSigChanMcdnMaxNonCallConcurrent = _MscSigChanMcdnMaxNonCallConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 13, 1, 2),
    _MscSigChanMcdnMaxNonCallConcurrent_Type()
)
mscSigChanMcdnMaxNonCallConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnMaxNonCallConcurrent.setStatus("mandatory")


class _MscSigChanMcdnOverlapSending_Type(Integer32):
    """Custom type mscSigChanMcdnOverlapSending based on Integer32"""
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


_MscSigChanMcdnOverlapSending_Type.__name__ = "Integer32"
_MscSigChanMcdnOverlapSending_Object = MibTableColumn
mscSigChanMcdnOverlapSending = _MscSigChanMcdnOverlapSending_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 13, 1, 3),
    _MscSigChanMcdnOverlapSending_Type()
)
mscSigChanMcdnOverlapSending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnOverlapSending.setStatus("mandatory")


class _MscSigChanMcdnOverlapReceiving_Type(Integer32):
    """Custom type mscSigChanMcdnOverlapReceiving based on Integer32"""
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


_MscSigChanMcdnOverlapReceiving_Type.__name__ = "Integer32"
_MscSigChanMcdnOverlapReceiving_Object = MibTableColumn
mscSigChanMcdnOverlapReceiving = _MscSigChanMcdnOverlapReceiving_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 13, 1, 4),
    _MscSigChanMcdnOverlapReceiving_Type()
)
mscSigChanMcdnOverlapReceiving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnOverlapReceiving.setStatus("mandatory")


class _MscSigChanMcdnChanMaintenanceHandling_Type(Integer32):
    """Custom type mscSigChanMcdnChanMaintenanceHandling based on Integer32"""
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


_MscSigChanMcdnChanMaintenanceHandling_Type.__name__ = "Integer32"
_MscSigChanMcdnChanMaintenanceHandling_Object = MibTableColumn
mscSigChanMcdnChanMaintenanceHandling = _MscSigChanMcdnChanMaintenanceHandling_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 13, 1, 5),
    _MscSigChanMcdnChanMaintenanceHandling_Type()
)
mscSigChanMcdnChanMaintenanceHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnChanMaintenanceHandling.setStatus("mandatory")
_MscSigChanMcdnStateTable_Object = MibTable
mscSigChanMcdnStateTable = _MscSigChanMcdnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 14)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnStateTable.setStatus("mandatory")
_MscSigChanMcdnStateEntry_Object = MibTableRow
mscSigChanMcdnStateEntry = _MscSigChanMcdnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 14, 1)
)
mscSigChanMcdnStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnStateEntry.setStatus("mandatory")


class _MscSigChanMcdnAdminState_Type(Integer32):
    """Custom type mscSigChanMcdnAdminState based on Integer32"""
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


_MscSigChanMcdnAdminState_Type.__name__ = "Integer32"
_MscSigChanMcdnAdminState_Object = MibTableColumn
mscSigChanMcdnAdminState = _MscSigChanMcdnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 14, 1, 1),
    _MscSigChanMcdnAdminState_Type()
)
mscSigChanMcdnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnAdminState.setStatus("mandatory")


class _MscSigChanMcdnOperationalState_Type(Integer32):
    """Custom type mscSigChanMcdnOperationalState based on Integer32"""
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


_MscSigChanMcdnOperationalState_Type.__name__ = "Integer32"
_MscSigChanMcdnOperationalState_Object = MibTableColumn
mscSigChanMcdnOperationalState = _MscSigChanMcdnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 14, 1, 2),
    _MscSigChanMcdnOperationalState_Type()
)
mscSigChanMcdnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnOperationalState.setStatus("mandatory")


class _MscSigChanMcdnUsageState_Type(Integer32):
    """Custom type mscSigChanMcdnUsageState based on Integer32"""
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


_MscSigChanMcdnUsageState_Type.__name__ = "Integer32"
_MscSigChanMcdnUsageState_Object = MibTableColumn
mscSigChanMcdnUsageState = _MscSigChanMcdnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 14, 1, 3),
    _MscSigChanMcdnUsageState_Type()
)
mscSigChanMcdnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnUsageState.setStatus("mandatory")
_MscSigChanMcdnStatsTable_Object = MibTable
mscSigChanMcdnStatsTable = _MscSigChanMcdnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 15)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnStatsTable.setStatus("mandatory")
_MscSigChanMcdnStatsEntry_Object = MibTableRow
mscSigChanMcdnStatsEntry = _MscSigChanMcdnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 15, 1)
)
mscSigChanMcdnStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnStatsEntry.setStatus("mandatory")
_MscSigChanMcdnTotalCallsToIf_Type = Counter32
_MscSigChanMcdnTotalCallsToIf_Object = MibTableColumn
mscSigChanMcdnTotalCallsToIf = _MscSigChanMcdnTotalCallsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 15, 1, 2),
    _MscSigChanMcdnTotalCallsToIf_Type()
)
mscSigChanMcdnTotalCallsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnTotalCallsToIf.setStatus("mandatory")
_MscSigChanMcdnTotalCallsFromIf_Type = Counter32
_MscSigChanMcdnTotalCallsFromIf_Object = MibTableColumn
mscSigChanMcdnTotalCallsFromIf = _MscSigChanMcdnTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 15, 1, 3),
    _MscSigChanMcdnTotalCallsFromIf_Type()
)
mscSigChanMcdnTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnTotalCallsFromIf.setStatus("mandatory")
_MscSigChanMcdnNonCallAssocSessionsToIf_Type = Counter32
_MscSigChanMcdnNonCallAssocSessionsToIf_Object = MibTableColumn
mscSigChanMcdnNonCallAssocSessionsToIf = _MscSigChanMcdnNonCallAssocSessionsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 15, 1, 4),
    _MscSigChanMcdnNonCallAssocSessionsToIf_Type()
)
mscSigChanMcdnNonCallAssocSessionsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnNonCallAssocSessionsToIf.setStatus("mandatory")
_MscSigChanMcdnNonCallAssocSessionsFromIf_Type = Counter32
_MscSigChanMcdnNonCallAssocSessionsFromIf_Object = MibTableColumn
mscSigChanMcdnNonCallAssocSessionsFromIf = _MscSigChanMcdnNonCallAssocSessionsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 15, 1, 5),
    _MscSigChanMcdnNonCallAssocSessionsFromIf_Type()
)
mscSigChanMcdnNonCallAssocSessionsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnNonCallAssocSessionsFromIf.setStatus("mandatory")
_MscSigChanMcdnOperTable_Object = MibTable
mscSigChanMcdnOperTable = _MscSigChanMcdnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 16)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnOperTable.setStatus("mandatory")
_MscSigChanMcdnOperEntry_Object = MibTableRow
mscSigChanMcdnOperEntry = _MscSigChanMcdnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 16, 1)
)
mscSigChanMcdnOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnOperEntry.setStatus("mandatory")


class _MscSigChanMcdnActiveChannels_Type(Unsigned32):
    """Custom type mscSigChanMcdnActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanMcdnActiveChannels_Type.__name__ = "Unsigned32"
_MscSigChanMcdnActiveChannels_Object = MibTableColumn
mscSigChanMcdnActiveChannels = _MscSigChanMcdnActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 16, 1, 1),
    _MscSigChanMcdnActiveChannels_Type()
)
mscSigChanMcdnActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnActiveChannels.setStatus("mandatory")


class _MscSigChanMcdnActiveVoiceChannels_Type(Unsigned32):
    """Custom type mscSigChanMcdnActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanMcdnActiveVoiceChannels_Type.__name__ = "Unsigned32"
_MscSigChanMcdnActiveVoiceChannels_Object = MibTableColumn
mscSigChanMcdnActiveVoiceChannels = _MscSigChanMcdnActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 16, 1, 2),
    _MscSigChanMcdnActiveVoiceChannels_Type()
)
mscSigChanMcdnActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnActiveVoiceChannels.setStatus("mandatory")


class _MscSigChanMcdnActiveDataChannels_Type(Unsigned32):
    """Custom type mscSigChanMcdnActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanMcdnActiveDataChannels_Type.__name__ = "Unsigned32"
_MscSigChanMcdnActiveDataChannels_Object = MibTableColumn
mscSigChanMcdnActiveDataChannels = _MscSigChanMcdnActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 16, 1, 3),
    _MscSigChanMcdnActiveDataChannels_Type()
)
mscSigChanMcdnActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnActiveDataChannels.setStatus("mandatory")


class _MscSigChanMcdnPeakActiveChannels_Type(Unsigned32):
    """Custom type mscSigChanMcdnPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanMcdnPeakActiveChannels_Type.__name__ = "Unsigned32"
_MscSigChanMcdnPeakActiveChannels_Object = MibTableColumn
mscSigChanMcdnPeakActiveChannels = _MscSigChanMcdnPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 16, 1, 4),
    _MscSigChanMcdnPeakActiveChannels_Type()
)
mscSigChanMcdnPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnPeakActiveChannels.setStatus("mandatory")


class _MscSigChanMcdnPeakActiveVoiceChannels_Type(Unsigned32):
    """Custom type mscSigChanMcdnPeakActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanMcdnPeakActiveVoiceChannels_Type.__name__ = "Unsigned32"
_MscSigChanMcdnPeakActiveVoiceChannels_Object = MibTableColumn
mscSigChanMcdnPeakActiveVoiceChannels = _MscSigChanMcdnPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 16, 1, 5),
    _MscSigChanMcdnPeakActiveVoiceChannels_Type()
)
mscSigChanMcdnPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnPeakActiveVoiceChannels.setStatus("mandatory")


class _MscSigChanMcdnPeakActiveDataChannels_Type(Unsigned32):
    """Custom type mscSigChanMcdnPeakActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanMcdnPeakActiveDataChannels_Type.__name__ = "Unsigned32"
_MscSigChanMcdnPeakActiveDataChannels_Object = MibTableColumn
mscSigChanMcdnPeakActiveDataChannels = _MscSigChanMcdnPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 16, 1, 6),
    _MscSigChanMcdnPeakActiveDataChannels_Type()
)
mscSigChanMcdnPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnPeakActiveDataChannels.setStatus("mandatory")


class _MscSigChanMcdnDChanStatus_Type(Integer32):
    """Custom type mscSigChanMcdnDChanStatus based on Integer32"""
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


_MscSigChanMcdnDChanStatus_Type.__name__ = "Integer32"
_MscSigChanMcdnDChanStatus_Object = MibTableColumn
mscSigChanMcdnDChanStatus = _MscSigChanMcdnDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 16, 1, 7),
    _MscSigChanMcdnDChanStatus_Type()
)
mscSigChanMcdnDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanMcdnDChanStatus.setStatus("mandatory")
_MscSigChanMcdnToolsTable_Object = MibTable
mscSigChanMcdnToolsTable = _MscSigChanMcdnToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 17)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnToolsTable.setStatus("mandatory")
_MscSigChanMcdnToolsEntry_Object = MibTableRow
mscSigChanMcdnToolsEntry = _MscSigChanMcdnToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 17, 1)
)
mscSigChanMcdnToolsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnToolsEntry.setStatus("mandatory")


class _MscSigChanMcdnTracing_Type(OctetString):
    """Custom type mscSigChanMcdnTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscSigChanMcdnTracing_Type.__name__ = "OctetString"
_MscSigChanMcdnTracing_Object = MibTableColumn
mscSigChanMcdnTracing = _MscSigChanMcdnTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 17, 1, 1),
    _MscSigChanMcdnTracing_Type()
)
mscSigChanMcdnTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnTracing.setStatus("mandatory")


class _MscSigChanMcdnMessageTraced_Type(OctetString):
    """Custom type mscSigChanMcdnMessageTraced based on OctetString"""
    defaultHexValue = "ffffff80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscSigChanMcdnMessageTraced_Type.__name__ = "OctetString"
_MscSigChanMcdnMessageTraced_Object = MibTableColumn
mscSigChanMcdnMessageTraced = _MscSigChanMcdnMessageTraced_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 17, 1, 2),
    _MscSigChanMcdnMessageTraced_Type()
)
mscSigChanMcdnMessageTraced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnMessageTraced.setStatus("mandatory")


class _MscSigChanMcdnDirectionTraced_Type(OctetString):
    """Custom type mscSigChanMcdnDirectionTraced based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscSigChanMcdnDirectionTraced_Type.__name__ = "OctetString"
_MscSigChanMcdnDirectionTraced_Object = MibTableColumn
mscSigChanMcdnDirectionTraced = _MscSigChanMcdnDirectionTraced_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 17, 1, 3),
    _MscSigChanMcdnDirectionTraced_Type()
)
mscSigChanMcdnDirectionTraced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnDirectionTraced.setStatus("mandatory")
_MscSigChanMcdnClsTable_Object = MibTable
mscSigChanMcdnClsTable = _MscSigChanMcdnClsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 18)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnClsTable.setStatus("mandatory")
_MscSigChanMcdnClsEntry_Object = MibTableRow
mscSigChanMcdnClsEntry = _MscSigChanMcdnClsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 18, 1)
)
mscSigChanMcdnClsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnClsEntry.setStatus("mandatory")


class _MscSigChanMcdnClsFeaturesSupported_Type(OctetString):
    """Custom type mscSigChanMcdnClsFeaturesSupported based on OctetString"""
    defaultHexValue = "ffc1"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscSigChanMcdnClsFeaturesSupported_Type.__name__ = "OctetString"
_MscSigChanMcdnClsFeaturesSupported_Object = MibTableColumn
mscSigChanMcdnClsFeaturesSupported = _MscSigChanMcdnClsFeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 18, 1, 2),
    _MscSigChanMcdnClsFeaturesSupported_Type()
)
mscSigChanMcdnClsFeaturesSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnClsFeaturesSupported.setStatus("mandatory")
_MscSigChanMcdnCoTable_Object = MibTable
mscSigChanMcdnCoTable = _MscSigChanMcdnCoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 19)
)
if mibBuilder.loadTexts:
    mscSigChanMcdnCoTable.setStatus("mandatory")
_MscSigChanMcdnCoEntry_Object = MibTableRow
mscSigChanMcdnCoEntry = _MscSigChanMcdnCoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 19, 1)
)
mscSigChanMcdnCoEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB", "mscSigChanMcdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanMcdnCoEntry.setStatus("mandatory")


class _MscSigChanMcdnDropBackCongestion_Type(Integer32):
    """Custom type mscSigChanMcdnDropBackCongestion based on Integer32"""
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
        *(("dropBackToOriginator", 1),
          ("dropBackToPriorNode", 2),
          ("noDropBackAllowed", 0))
    )


_MscSigChanMcdnDropBackCongestion_Type.__name__ = "Integer32"
_MscSigChanMcdnDropBackCongestion_Object = MibTableColumn
mscSigChanMcdnDropBackCongestion = _MscSigChanMcdnDropBackCongestion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 19, 1, 1),
    _MscSigChanMcdnDropBackCongestion_Type()
)
mscSigChanMcdnDropBackCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnDropBackCongestion.setStatus("mandatory")


class _MscSigChanMcdnNetworkNameDisplay_Type(OctetString):
    """Custom type mscSigChanMcdnNetworkNameDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscSigChanMcdnNetworkNameDisplay_Type.__name__ = "OctetString"
_MscSigChanMcdnNetworkNameDisplay_Object = MibTableColumn
mscSigChanMcdnNetworkNameDisplay = _MscSigChanMcdnNetworkNameDisplay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 19, 1, 4),
    _MscSigChanMcdnNetworkNameDisplay_Type()
)
mscSigChanMcdnNetworkNameDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnNetworkNameDisplay.setStatus("mandatory")


class _MscSigChanMcdnMultisiteBusinessGroup_Type(Integer32):
    """Custom type mscSigChanMcdnMultisiteBusinessGroup based on Integer32"""
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


_MscSigChanMcdnMultisiteBusinessGroup_Type.__name__ = "Integer32"
_MscSigChanMcdnMultisiteBusinessGroup_Object = MibTableColumn
mscSigChanMcdnMultisiteBusinessGroup = _MscSigChanMcdnMultisiteBusinessGroup_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 19, 1, 7),
    _MscSigChanMcdnMultisiteBusinessGroup_Type()
)
mscSigChanMcdnMultisiteBusinessGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnMultisiteBusinessGroup.setStatus("mandatory")


class _MscSigChanMcdnConOrFeaturesSupported_Type(OctetString):
    """Custom type mscSigChanMcdnConOrFeaturesSupported based on OctetString"""
    defaultHexValue = "fff8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscSigChanMcdnConOrFeaturesSupported_Type.__name__ = "OctetString"
_MscSigChanMcdnConOrFeaturesSupported_Object = MibTableColumn
mscSigChanMcdnConOrFeaturesSupported = _MscSigChanMcdnConOrFeaturesSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 17, 19, 1, 8),
    _MscSigChanMcdnConOrFeaturesSupported_Type()
)
mscSigChanMcdnConOrFeaturesSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanMcdnConOrFeaturesSupported.setStatus("mandatory")
_VnetMcdnSigMIB_ObjectIdentity = ObjectIdentity
vnetMcdnSigMIB = _VnetMcdnSigMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 142)
)
_VnetMcdnSigGroup_ObjectIdentity = ObjectIdentity
vnetMcdnSigGroup = _VnetMcdnSigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 142, 1)
)
_VnetMcdnSigGroupCA_ObjectIdentity = ObjectIdentity
vnetMcdnSigGroupCA = _VnetMcdnSigGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 142, 1, 1)
)
_VnetMcdnSigGroupCA02_ObjectIdentity = ObjectIdentity
vnetMcdnSigGroupCA02 = _VnetMcdnSigGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 142, 1, 1, 3)
)
_VnetMcdnSigGroupCA02A_ObjectIdentity = ObjectIdentity
vnetMcdnSigGroupCA02A = _VnetMcdnSigGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 142, 1, 1, 3, 2)
)
_VnetMcdnSigCapabilities_ObjectIdentity = ObjectIdentity
vnetMcdnSigCapabilities = _VnetMcdnSigCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 142, 3)
)
_VnetMcdnSigCapabilitiesCA_ObjectIdentity = ObjectIdentity
vnetMcdnSigCapabilitiesCA = _VnetMcdnSigCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 142, 3, 1)
)
_VnetMcdnSigCapabilitiesCA02_ObjectIdentity = ObjectIdentity
vnetMcdnSigCapabilitiesCA02 = _VnetMcdnSigCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 142, 3, 1, 3)
)
_VnetMcdnSigCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
vnetMcdnSigCapabilitiesCA02A = _VnetMcdnSigCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 142, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VnetMcdnSigMIB",
    **{"mscSigChanMcdn": mscSigChanMcdn,
       "mscSigChanMcdnRowStatusTable": mscSigChanMcdnRowStatusTable,
       "mscSigChanMcdnRowStatusEntry": mscSigChanMcdnRowStatusEntry,
       "mscSigChanMcdnRowStatus": mscSigChanMcdnRowStatus,
       "mscSigChanMcdnComponentName": mscSigChanMcdnComponentName,
       "mscSigChanMcdnStorageType": mscSigChanMcdnStorageType,
       "mscSigChanMcdnIndex": mscSigChanMcdnIndex,
       "mscSigChanMcdnFramer": mscSigChanMcdnFramer,
       "mscSigChanMcdnFramerRowStatusTable": mscSigChanMcdnFramerRowStatusTable,
       "mscSigChanMcdnFramerRowStatusEntry": mscSigChanMcdnFramerRowStatusEntry,
       "mscSigChanMcdnFramerRowStatus": mscSigChanMcdnFramerRowStatus,
       "mscSigChanMcdnFramerComponentName": mscSigChanMcdnFramerComponentName,
       "mscSigChanMcdnFramerStorageType": mscSigChanMcdnFramerStorageType,
       "mscSigChanMcdnFramerIndex": mscSigChanMcdnFramerIndex,
       "mscSigChanMcdnFramerProvTable": mscSigChanMcdnFramerProvTable,
       "mscSigChanMcdnFramerProvEntry": mscSigChanMcdnFramerProvEntry,
       "mscSigChanMcdnFramerInterfaceName": mscSigChanMcdnFramerInterfaceName,
       "mscSigChanMcdnFramerStateTable": mscSigChanMcdnFramerStateTable,
       "mscSigChanMcdnFramerStateEntry": mscSigChanMcdnFramerStateEntry,
       "mscSigChanMcdnFramerAdminState": mscSigChanMcdnFramerAdminState,
       "mscSigChanMcdnFramerOperationalState": mscSigChanMcdnFramerOperationalState,
       "mscSigChanMcdnFramerUsageState": mscSigChanMcdnFramerUsageState,
       "mscSigChanMcdnFramerStatsTable": mscSigChanMcdnFramerStatsTable,
       "mscSigChanMcdnFramerStatsEntry": mscSigChanMcdnFramerStatsEntry,
       "mscSigChanMcdnFramerFrmToIf": mscSigChanMcdnFramerFrmToIf,
       "mscSigChanMcdnFramerFrmFromIf": mscSigChanMcdnFramerFrmFromIf,
       "mscSigChanMcdnFramerOctetFromIf": mscSigChanMcdnFramerOctetFromIf,
       "mscSigChanMcdnFramerAborts": mscSigChanMcdnFramerAborts,
       "mscSigChanMcdnFramerCrcErrors": mscSigChanMcdnFramerCrcErrors,
       "mscSigChanMcdnFramerLrcErrors": mscSigChanMcdnFramerLrcErrors,
       "mscSigChanMcdnFramerNonOctetErrors": mscSigChanMcdnFramerNonOctetErrors,
       "mscSigChanMcdnFramerOverruns": mscSigChanMcdnFramerOverruns,
       "mscSigChanMcdnFramerUnderruns": mscSigChanMcdnFramerUnderruns,
       "mscSigChanMcdnFramerLargeFrmErrors": mscSigChanMcdnFramerLargeFrmErrors,
       "mscSigChanMcdnL2Table": mscSigChanMcdnL2Table,
       "mscSigChanMcdnL2Entry": mscSigChanMcdnL2Entry,
       "mscSigChanMcdnT23": mscSigChanMcdnT23,
       "mscSigChanMcdnT200": mscSigChanMcdnT200,
       "mscSigChanMcdnN200": mscSigChanMcdnN200,
       "mscSigChanMcdnT203": mscSigChanMcdnT203,
       "mscSigChanMcdnCircuitSwitchedK": mscSigChanMcdnCircuitSwitchedK,
       "mscSigChanMcdnL3Table": mscSigChanMcdnL3Table,
       "mscSigChanMcdnL3Entry": mscSigChanMcdnL3Entry,
       "mscSigChanMcdnT302": mscSigChanMcdnT302,
       "mscSigChanMcdnT304": mscSigChanMcdnT304,
       "mscSigChanMcdnT309": mscSigChanMcdnT309,
       "mscSigChanMcdnT310": mscSigChanMcdnT310,
       "mscSigChanMcdnT316": mscSigChanMcdnT316,
       "mscSigChanMcdnT317": mscSigChanMcdnT317,
       "mscSigChanMcdnProvTable": mscSigChanMcdnProvTable,
       "mscSigChanMcdnProvEntry": mscSigChanMcdnProvEntry,
       "mscSigChanMcdnSide": mscSigChanMcdnSide,
       "mscSigChanMcdnMaxNonCallConcurrent": mscSigChanMcdnMaxNonCallConcurrent,
       "mscSigChanMcdnOverlapSending": mscSigChanMcdnOverlapSending,
       "mscSigChanMcdnOverlapReceiving": mscSigChanMcdnOverlapReceiving,
       "mscSigChanMcdnChanMaintenanceHandling": mscSigChanMcdnChanMaintenanceHandling,
       "mscSigChanMcdnStateTable": mscSigChanMcdnStateTable,
       "mscSigChanMcdnStateEntry": mscSigChanMcdnStateEntry,
       "mscSigChanMcdnAdminState": mscSigChanMcdnAdminState,
       "mscSigChanMcdnOperationalState": mscSigChanMcdnOperationalState,
       "mscSigChanMcdnUsageState": mscSigChanMcdnUsageState,
       "mscSigChanMcdnStatsTable": mscSigChanMcdnStatsTable,
       "mscSigChanMcdnStatsEntry": mscSigChanMcdnStatsEntry,
       "mscSigChanMcdnTotalCallsToIf": mscSigChanMcdnTotalCallsToIf,
       "mscSigChanMcdnTotalCallsFromIf": mscSigChanMcdnTotalCallsFromIf,
       "mscSigChanMcdnNonCallAssocSessionsToIf": mscSigChanMcdnNonCallAssocSessionsToIf,
       "mscSigChanMcdnNonCallAssocSessionsFromIf": mscSigChanMcdnNonCallAssocSessionsFromIf,
       "mscSigChanMcdnOperTable": mscSigChanMcdnOperTable,
       "mscSigChanMcdnOperEntry": mscSigChanMcdnOperEntry,
       "mscSigChanMcdnActiveChannels": mscSigChanMcdnActiveChannels,
       "mscSigChanMcdnActiveVoiceChannels": mscSigChanMcdnActiveVoiceChannels,
       "mscSigChanMcdnActiveDataChannels": mscSigChanMcdnActiveDataChannels,
       "mscSigChanMcdnPeakActiveChannels": mscSigChanMcdnPeakActiveChannels,
       "mscSigChanMcdnPeakActiveVoiceChannels": mscSigChanMcdnPeakActiveVoiceChannels,
       "mscSigChanMcdnPeakActiveDataChannels": mscSigChanMcdnPeakActiveDataChannels,
       "mscSigChanMcdnDChanStatus": mscSigChanMcdnDChanStatus,
       "mscSigChanMcdnToolsTable": mscSigChanMcdnToolsTable,
       "mscSigChanMcdnToolsEntry": mscSigChanMcdnToolsEntry,
       "mscSigChanMcdnTracing": mscSigChanMcdnTracing,
       "mscSigChanMcdnMessageTraced": mscSigChanMcdnMessageTraced,
       "mscSigChanMcdnDirectionTraced": mscSigChanMcdnDirectionTraced,
       "mscSigChanMcdnClsTable": mscSigChanMcdnClsTable,
       "mscSigChanMcdnClsEntry": mscSigChanMcdnClsEntry,
       "mscSigChanMcdnClsFeaturesSupported": mscSigChanMcdnClsFeaturesSupported,
       "mscSigChanMcdnCoTable": mscSigChanMcdnCoTable,
       "mscSigChanMcdnCoEntry": mscSigChanMcdnCoEntry,
       "mscSigChanMcdnDropBackCongestion": mscSigChanMcdnDropBackCongestion,
       "mscSigChanMcdnNetworkNameDisplay": mscSigChanMcdnNetworkNameDisplay,
       "mscSigChanMcdnMultisiteBusinessGroup": mscSigChanMcdnMultisiteBusinessGroup,
       "mscSigChanMcdnConOrFeaturesSupported": mscSigChanMcdnConOrFeaturesSupported,
       "vnetMcdnSigMIB": vnetMcdnSigMIB,
       "vnetMcdnSigGroup": vnetMcdnSigGroup,
       "vnetMcdnSigGroupCA": vnetMcdnSigGroupCA,
       "vnetMcdnSigGroupCA02": vnetMcdnSigGroupCA02,
       "vnetMcdnSigGroupCA02A": vnetMcdnSigGroupCA02A,
       "vnetMcdnSigCapabilities": vnetMcdnSigCapabilities,
       "vnetMcdnSigCapabilitiesCA": vnetMcdnSigCapabilitiesCA,
       "vnetMcdnSigCapabilitiesCA02": vnetMcdnSigCapabilitiesCA02,
       "vnetMcdnSigCapabilitiesCA02A": vnetMcdnSigCapabilitiesCA02A}
)
