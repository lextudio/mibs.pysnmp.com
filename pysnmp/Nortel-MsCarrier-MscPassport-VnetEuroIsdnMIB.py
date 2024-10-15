# SNMP MIB module (Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:17 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
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

_MscSigChanEIsdn_ObjectIdentity = ObjectIdentity
mscSigChanEIsdn = _MscSigChanEIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14)
)
_MscSigChanEIsdnRowStatusTable_Object = MibTable
mscSigChanEIsdnRowStatusTable = _MscSigChanEIsdnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 1)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnRowStatusTable.setStatus("mandatory")
_MscSigChanEIsdnRowStatusEntry_Object = MibTableRow
mscSigChanEIsdnRowStatusEntry = _MscSigChanEIsdnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 1, 1)
)
mscSigChanEIsdnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnRowStatusEntry.setStatus("mandatory")
_MscSigChanEIsdnRowStatus_Type = RowStatus
_MscSigChanEIsdnRowStatus_Object = MibTableColumn
mscSigChanEIsdnRowStatus = _MscSigChanEIsdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 1, 1, 1),
    _MscSigChanEIsdnRowStatus_Type()
)
mscSigChanEIsdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnRowStatus.setStatus("mandatory")
_MscSigChanEIsdnComponentName_Type = DisplayString
_MscSigChanEIsdnComponentName_Object = MibTableColumn
mscSigChanEIsdnComponentName = _MscSigChanEIsdnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 1, 1, 2),
    _MscSigChanEIsdnComponentName_Type()
)
mscSigChanEIsdnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnComponentName.setStatus("mandatory")
_MscSigChanEIsdnStorageType_Type = StorageType
_MscSigChanEIsdnStorageType_Object = MibTableColumn
mscSigChanEIsdnStorageType = _MscSigChanEIsdnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 1, 1, 4),
    _MscSigChanEIsdnStorageType_Type()
)
mscSigChanEIsdnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnStorageType.setStatus("mandatory")
_MscSigChanEIsdnIndex_Type = NonReplicated
_MscSigChanEIsdnIndex_Object = MibTableColumn
mscSigChanEIsdnIndex = _MscSigChanEIsdnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 1, 1, 10),
    _MscSigChanEIsdnIndex_Type()
)
mscSigChanEIsdnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanEIsdnIndex.setStatus("mandatory")
_MscSigChanEIsdnFramer_ObjectIdentity = ObjectIdentity
mscSigChanEIsdnFramer = _MscSigChanEIsdnFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2)
)
_MscSigChanEIsdnFramerRowStatusTable_Object = MibTable
mscSigChanEIsdnFramerRowStatusTable = _MscSigChanEIsdnFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 1)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerRowStatusTable.setStatus("mandatory")
_MscSigChanEIsdnFramerRowStatusEntry_Object = MibTableRow
mscSigChanEIsdnFramerRowStatusEntry = _MscSigChanEIsdnFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 1, 1)
)
mscSigChanEIsdnFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerRowStatusEntry.setStatus("mandatory")
_MscSigChanEIsdnFramerRowStatus_Type = RowStatus
_MscSigChanEIsdnFramerRowStatus_Object = MibTableColumn
mscSigChanEIsdnFramerRowStatus = _MscSigChanEIsdnFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 1, 1, 1),
    _MscSigChanEIsdnFramerRowStatus_Type()
)
mscSigChanEIsdnFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerRowStatus.setStatus("mandatory")
_MscSigChanEIsdnFramerComponentName_Type = DisplayString
_MscSigChanEIsdnFramerComponentName_Object = MibTableColumn
mscSigChanEIsdnFramerComponentName = _MscSigChanEIsdnFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 1, 1, 2),
    _MscSigChanEIsdnFramerComponentName_Type()
)
mscSigChanEIsdnFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerComponentName.setStatus("mandatory")
_MscSigChanEIsdnFramerStorageType_Type = StorageType
_MscSigChanEIsdnFramerStorageType_Object = MibTableColumn
mscSigChanEIsdnFramerStorageType = _MscSigChanEIsdnFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 1, 1, 4),
    _MscSigChanEIsdnFramerStorageType_Type()
)
mscSigChanEIsdnFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerStorageType.setStatus("mandatory")
_MscSigChanEIsdnFramerIndex_Type = NonReplicated
_MscSigChanEIsdnFramerIndex_Object = MibTableColumn
mscSigChanEIsdnFramerIndex = _MscSigChanEIsdnFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 1, 1, 10),
    _MscSigChanEIsdnFramerIndex_Type()
)
mscSigChanEIsdnFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerIndex.setStatus("mandatory")
_MscSigChanEIsdnFramerProvTable_Object = MibTable
mscSigChanEIsdnFramerProvTable = _MscSigChanEIsdnFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 10)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerProvTable.setStatus("mandatory")
_MscSigChanEIsdnFramerProvEntry_Object = MibTableRow
mscSigChanEIsdnFramerProvEntry = _MscSigChanEIsdnFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 10, 1)
)
mscSigChanEIsdnFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerProvEntry.setStatus("mandatory")
_MscSigChanEIsdnFramerInterfaceName_Type = Link
_MscSigChanEIsdnFramerInterfaceName_Object = MibTableColumn
mscSigChanEIsdnFramerInterfaceName = _MscSigChanEIsdnFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 10, 1, 1),
    _MscSigChanEIsdnFramerInterfaceName_Type()
)
mscSigChanEIsdnFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerInterfaceName.setStatus("mandatory")
_MscSigChanEIsdnFramerStateTable_Object = MibTable
mscSigChanEIsdnFramerStateTable = _MscSigChanEIsdnFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 12)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerStateTable.setStatus("mandatory")
_MscSigChanEIsdnFramerStateEntry_Object = MibTableRow
mscSigChanEIsdnFramerStateEntry = _MscSigChanEIsdnFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 12, 1)
)
mscSigChanEIsdnFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerStateEntry.setStatus("mandatory")


class _MscSigChanEIsdnFramerAdminState_Type(Integer32):
    """Custom type mscSigChanEIsdnFramerAdminState based on Integer32"""
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


_MscSigChanEIsdnFramerAdminState_Type.__name__ = "Integer32"
_MscSigChanEIsdnFramerAdminState_Object = MibTableColumn
mscSigChanEIsdnFramerAdminState = _MscSigChanEIsdnFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 12, 1, 1),
    _MscSigChanEIsdnFramerAdminState_Type()
)
mscSigChanEIsdnFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerAdminState.setStatus("mandatory")


class _MscSigChanEIsdnFramerOperationalState_Type(Integer32):
    """Custom type mscSigChanEIsdnFramerOperationalState based on Integer32"""
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


_MscSigChanEIsdnFramerOperationalState_Type.__name__ = "Integer32"
_MscSigChanEIsdnFramerOperationalState_Object = MibTableColumn
mscSigChanEIsdnFramerOperationalState = _MscSigChanEIsdnFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 12, 1, 2),
    _MscSigChanEIsdnFramerOperationalState_Type()
)
mscSigChanEIsdnFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerOperationalState.setStatus("mandatory")


class _MscSigChanEIsdnFramerUsageState_Type(Integer32):
    """Custom type mscSigChanEIsdnFramerUsageState based on Integer32"""
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


_MscSigChanEIsdnFramerUsageState_Type.__name__ = "Integer32"
_MscSigChanEIsdnFramerUsageState_Object = MibTableColumn
mscSigChanEIsdnFramerUsageState = _MscSigChanEIsdnFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 12, 1, 3),
    _MscSigChanEIsdnFramerUsageState_Type()
)
mscSigChanEIsdnFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerUsageState.setStatus("mandatory")
_MscSigChanEIsdnFramerStatsTable_Object = MibTable
mscSigChanEIsdnFramerStatsTable = _MscSigChanEIsdnFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerStatsTable.setStatus("mandatory")
_MscSigChanEIsdnFramerStatsEntry_Object = MibTableRow
mscSigChanEIsdnFramerStatsEntry = _MscSigChanEIsdnFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1)
)
mscSigChanEIsdnFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerStatsEntry.setStatus("mandatory")
_MscSigChanEIsdnFramerFrmToIf_Type = Counter32
_MscSigChanEIsdnFramerFrmToIf_Object = MibTableColumn
mscSigChanEIsdnFramerFrmToIf = _MscSigChanEIsdnFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 1),
    _MscSigChanEIsdnFramerFrmToIf_Type()
)
mscSigChanEIsdnFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerFrmToIf.setStatus("mandatory")
_MscSigChanEIsdnFramerFrmFromIf_Type = Counter32
_MscSigChanEIsdnFramerFrmFromIf_Object = MibTableColumn
mscSigChanEIsdnFramerFrmFromIf = _MscSigChanEIsdnFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 2),
    _MscSigChanEIsdnFramerFrmFromIf_Type()
)
mscSigChanEIsdnFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerFrmFromIf.setStatus("mandatory")
_MscSigChanEIsdnFramerOctetFromIf_Type = Counter32
_MscSigChanEIsdnFramerOctetFromIf_Object = MibTableColumn
mscSigChanEIsdnFramerOctetFromIf = _MscSigChanEIsdnFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 3),
    _MscSigChanEIsdnFramerOctetFromIf_Type()
)
mscSigChanEIsdnFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerOctetFromIf.setStatus("mandatory")
_MscSigChanEIsdnFramerAborts_Type = Counter32
_MscSigChanEIsdnFramerAborts_Object = MibTableColumn
mscSigChanEIsdnFramerAborts = _MscSigChanEIsdnFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 4),
    _MscSigChanEIsdnFramerAborts_Type()
)
mscSigChanEIsdnFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerAborts.setStatus("mandatory")
_MscSigChanEIsdnFramerCrcErrors_Type = Counter32
_MscSigChanEIsdnFramerCrcErrors_Object = MibTableColumn
mscSigChanEIsdnFramerCrcErrors = _MscSigChanEIsdnFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 5),
    _MscSigChanEIsdnFramerCrcErrors_Type()
)
mscSigChanEIsdnFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerCrcErrors.setStatus("mandatory")
_MscSigChanEIsdnFramerLrcErrors_Type = Counter32
_MscSigChanEIsdnFramerLrcErrors_Object = MibTableColumn
mscSigChanEIsdnFramerLrcErrors = _MscSigChanEIsdnFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 6),
    _MscSigChanEIsdnFramerLrcErrors_Type()
)
mscSigChanEIsdnFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerLrcErrors.setStatus("mandatory")
_MscSigChanEIsdnFramerNonOctetErrors_Type = Counter32
_MscSigChanEIsdnFramerNonOctetErrors_Object = MibTableColumn
mscSigChanEIsdnFramerNonOctetErrors = _MscSigChanEIsdnFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 7),
    _MscSigChanEIsdnFramerNonOctetErrors_Type()
)
mscSigChanEIsdnFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerNonOctetErrors.setStatus("mandatory")
_MscSigChanEIsdnFramerOverruns_Type = Counter32
_MscSigChanEIsdnFramerOverruns_Object = MibTableColumn
mscSigChanEIsdnFramerOverruns = _MscSigChanEIsdnFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 8),
    _MscSigChanEIsdnFramerOverruns_Type()
)
mscSigChanEIsdnFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerOverruns.setStatus("mandatory")
_MscSigChanEIsdnFramerUnderruns_Type = Counter32
_MscSigChanEIsdnFramerUnderruns_Object = MibTableColumn
mscSigChanEIsdnFramerUnderruns = _MscSigChanEIsdnFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 9),
    _MscSigChanEIsdnFramerUnderruns_Type()
)
mscSigChanEIsdnFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerUnderruns.setStatus("mandatory")
_MscSigChanEIsdnFramerLargeFrmErrors_Type = Counter32
_MscSigChanEIsdnFramerLargeFrmErrors_Object = MibTableColumn
mscSigChanEIsdnFramerLargeFrmErrors = _MscSigChanEIsdnFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 2, 13, 1, 10),
    _MscSigChanEIsdnFramerLargeFrmErrors_Type()
)
mscSigChanEIsdnFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnFramerLargeFrmErrors.setStatus("mandatory")
_MscSigChanEIsdnL2Table_Object = MibTable
mscSigChanEIsdnL2Table = _MscSigChanEIsdnL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 11)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnL2Table.setStatus("mandatory")
_MscSigChanEIsdnL2Entry_Object = MibTableRow
mscSigChanEIsdnL2Entry = _MscSigChanEIsdnL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 11, 1)
)
mscSigChanEIsdnL2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnL2Entry.setStatus("mandatory")


class _MscSigChanEIsdnT23_Type(Unsigned32):
    """Custom type mscSigChanEIsdnT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscSigChanEIsdnT23_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnT23_Object = MibTableColumn
mscSigChanEIsdnT23 = _MscSigChanEIsdnT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 11, 1, 1),
    _MscSigChanEIsdnT23_Type()
)
mscSigChanEIsdnT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnT23.setStatus("mandatory")


class _MscSigChanEIsdnT200_Type(Unsigned32):
    """Custom type mscSigChanEIsdnT200 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscSigChanEIsdnT200_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnT200_Object = MibTableColumn
mscSigChanEIsdnT200 = _MscSigChanEIsdnT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 11, 1, 2),
    _MscSigChanEIsdnT200_Type()
)
mscSigChanEIsdnT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnT200.setStatus("mandatory")


class _MscSigChanEIsdnN200_Type(Unsigned32):
    """Custom type mscSigChanEIsdnN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscSigChanEIsdnN200_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnN200_Object = MibTableColumn
mscSigChanEIsdnN200 = _MscSigChanEIsdnN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 11, 1, 3),
    _MscSigChanEIsdnN200_Type()
)
mscSigChanEIsdnN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnN200.setStatus("mandatory")


class _MscSigChanEIsdnT203_Type(Unsigned32):
    """Custom type mscSigChanEIsdnT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_MscSigChanEIsdnT203_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnT203_Object = MibTableColumn
mscSigChanEIsdnT203 = _MscSigChanEIsdnT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 11, 1, 4),
    _MscSigChanEIsdnT203_Type()
)
mscSigChanEIsdnT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnT203.setStatus("mandatory")


class _MscSigChanEIsdnCircuitSwitchedK_Type(Unsigned32):
    """Custom type mscSigChanEIsdnCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscSigChanEIsdnCircuitSwitchedK_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnCircuitSwitchedK_Object = MibTableColumn
mscSigChanEIsdnCircuitSwitchedK = _MscSigChanEIsdnCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 11, 1, 6),
    _MscSigChanEIsdnCircuitSwitchedK_Type()
)
mscSigChanEIsdnCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnCircuitSwitchedK.setStatus("mandatory")
_MscSigChanEIsdnL3Table_Object = MibTable
mscSigChanEIsdnL3Table = _MscSigChanEIsdnL3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 12)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnL3Table.setStatus("mandatory")
_MscSigChanEIsdnL3Entry_Object = MibTableRow
mscSigChanEIsdnL3Entry = _MscSigChanEIsdnL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 12, 1)
)
mscSigChanEIsdnL3Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnL3Entry.setStatus("mandatory")


class _MscSigChanEIsdnT310_Type(Unsigned32):
    """Custom type mscSigChanEIsdnT310 based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_MscSigChanEIsdnT310_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnT310_Object = MibTableColumn
mscSigChanEIsdnT310 = _MscSigChanEIsdnT310_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 12, 1, 4),
    _MscSigChanEIsdnT310_Type()
)
mscSigChanEIsdnT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnT310.setStatus("mandatory")
_MscSigChanEIsdnProvTable_Object = MibTable
mscSigChanEIsdnProvTable = _MscSigChanEIsdnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 13)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnProvTable.setStatus("mandatory")
_MscSigChanEIsdnProvEntry_Object = MibTableRow
mscSigChanEIsdnProvEntry = _MscSigChanEIsdnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 13, 1)
)
mscSigChanEIsdnProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnProvEntry.setStatus("mandatory")


class _MscSigChanEIsdnSide_Type(Integer32):
    """Custom type mscSigChanEIsdnSide based on Integer32"""
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


_MscSigChanEIsdnSide_Type.__name__ = "Integer32"
_MscSigChanEIsdnSide_Object = MibTableColumn
mscSigChanEIsdnSide = _MscSigChanEIsdnSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 13, 1, 1),
    _MscSigChanEIsdnSide_Type()
)
mscSigChanEIsdnSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnSide.setStatus("mandatory")


class _MscSigChanEIsdnMaxNonCallConcurrent_Type(Unsigned32):
    """Custom type mscSigChanEIsdnMaxNonCallConcurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MscSigChanEIsdnMaxNonCallConcurrent_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnMaxNonCallConcurrent_Object = MibTableColumn
mscSigChanEIsdnMaxNonCallConcurrent = _MscSigChanEIsdnMaxNonCallConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 13, 1, 2),
    _MscSigChanEIsdnMaxNonCallConcurrent_Type()
)
mscSigChanEIsdnMaxNonCallConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnMaxNonCallConcurrent.setStatus("mandatory")


class _MscSigChanEIsdnOverlapSending_Type(Integer32):
    """Custom type mscSigChanEIsdnOverlapSending based on Integer32"""
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


_MscSigChanEIsdnOverlapSending_Type.__name__ = "Integer32"
_MscSigChanEIsdnOverlapSending_Object = MibTableColumn
mscSigChanEIsdnOverlapSending = _MscSigChanEIsdnOverlapSending_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 13, 1, 3),
    _MscSigChanEIsdnOverlapSending_Type()
)
mscSigChanEIsdnOverlapSending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnOverlapSending.setStatus("mandatory")


class _MscSigChanEIsdnOverlapReceiving_Type(Integer32):
    """Custom type mscSigChanEIsdnOverlapReceiving based on Integer32"""
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


_MscSigChanEIsdnOverlapReceiving_Type.__name__ = "Integer32"
_MscSigChanEIsdnOverlapReceiving_Object = MibTableColumn
mscSigChanEIsdnOverlapReceiving = _MscSigChanEIsdnOverlapReceiving_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 13, 1, 4),
    _MscSigChanEIsdnOverlapReceiving_Type()
)
mscSigChanEIsdnOverlapReceiving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnOverlapReceiving.setStatus("mandatory")
_MscSigChanEIsdnStateTable_Object = MibTable
mscSigChanEIsdnStateTable = _MscSigChanEIsdnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 14)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnStateTable.setStatus("mandatory")
_MscSigChanEIsdnStateEntry_Object = MibTableRow
mscSigChanEIsdnStateEntry = _MscSigChanEIsdnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 14, 1)
)
mscSigChanEIsdnStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnStateEntry.setStatus("mandatory")


class _MscSigChanEIsdnAdminState_Type(Integer32):
    """Custom type mscSigChanEIsdnAdminState based on Integer32"""
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


_MscSigChanEIsdnAdminState_Type.__name__ = "Integer32"
_MscSigChanEIsdnAdminState_Object = MibTableColumn
mscSigChanEIsdnAdminState = _MscSigChanEIsdnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 14, 1, 1),
    _MscSigChanEIsdnAdminState_Type()
)
mscSigChanEIsdnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnAdminState.setStatus("mandatory")


class _MscSigChanEIsdnOperationalState_Type(Integer32):
    """Custom type mscSigChanEIsdnOperationalState based on Integer32"""
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


_MscSigChanEIsdnOperationalState_Type.__name__ = "Integer32"
_MscSigChanEIsdnOperationalState_Object = MibTableColumn
mscSigChanEIsdnOperationalState = _MscSigChanEIsdnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 14, 1, 2),
    _MscSigChanEIsdnOperationalState_Type()
)
mscSigChanEIsdnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnOperationalState.setStatus("mandatory")


class _MscSigChanEIsdnUsageState_Type(Integer32):
    """Custom type mscSigChanEIsdnUsageState based on Integer32"""
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


_MscSigChanEIsdnUsageState_Type.__name__ = "Integer32"
_MscSigChanEIsdnUsageState_Object = MibTableColumn
mscSigChanEIsdnUsageState = _MscSigChanEIsdnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 14, 1, 3),
    _MscSigChanEIsdnUsageState_Type()
)
mscSigChanEIsdnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnUsageState.setStatus("mandatory")
_MscSigChanEIsdnStatsTable_Object = MibTable
mscSigChanEIsdnStatsTable = _MscSigChanEIsdnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 15)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnStatsTable.setStatus("mandatory")
_MscSigChanEIsdnStatsEntry_Object = MibTableRow
mscSigChanEIsdnStatsEntry = _MscSigChanEIsdnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 15, 1)
)
mscSigChanEIsdnStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnStatsEntry.setStatus("mandatory")
_MscSigChanEIsdnTotalCallsToIf_Type = Counter32
_MscSigChanEIsdnTotalCallsToIf_Object = MibTableColumn
mscSigChanEIsdnTotalCallsToIf = _MscSigChanEIsdnTotalCallsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 15, 1, 2),
    _MscSigChanEIsdnTotalCallsToIf_Type()
)
mscSigChanEIsdnTotalCallsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnTotalCallsToIf.setStatus("mandatory")
_MscSigChanEIsdnTotalCallsFromIf_Type = Counter32
_MscSigChanEIsdnTotalCallsFromIf_Object = MibTableColumn
mscSigChanEIsdnTotalCallsFromIf = _MscSigChanEIsdnTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 15, 1, 3),
    _MscSigChanEIsdnTotalCallsFromIf_Type()
)
mscSigChanEIsdnTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnTotalCallsFromIf.setStatus("mandatory")
_MscSigChanEIsdnNonCallAssocSessionsToIf_Type = Counter32
_MscSigChanEIsdnNonCallAssocSessionsToIf_Object = MibTableColumn
mscSigChanEIsdnNonCallAssocSessionsToIf = _MscSigChanEIsdnNonCallAssocSessionsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 15, 1, 4),
    _MscSigChanEIsdnNonCallAssocSessionsToIf_Type()
)
mscSigChanEIsdnNonCallAssocSessionsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnNonCallAssocSessionsToIf.setStatus("mandatory")
_MscSigChanEIsdnNonCallAssocSessionsFromIf_Type = Counter32
_MscSigChanEIsdnNonCallAssocSessionsFromIf_Object = MibTableColumn
mscSigChanEIsdnNonCallAssocSessionsFromIf = _MscSigChanEIsdnNonCallAssocSessionsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 15, 1, 5),
    _MscSigChanEIsdnNonCallAssocSessionsFromIf_Type()
)
mscSigChanEIsdnNonCallAssocSessionsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnNonCallAssocSessionsFromIf.setStatus("mandatory")
_MscSigChanEIsdnOperTable_Object = MibTable
mscSigChanEIsdnOperTable = _MscSigChanEIsdnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 16)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnOperTable.setStatus("mandatory")
_MscSigChanEIsdnOperEntry_Object = MibTableRow
mscSigChanEIsdnOperEntry = _MscSigChanEIsdnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 16, 1)
)
mscSigChanEIsdnOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnOperEntry.setStatus("mandatory")


class _MscSigChanEIsdnActiveChannels_Type(Gauge32):
    """Custom type mscSigChanEIsdnActiveChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEIsdnActiveChannels_Type.__name__ = "Gauge32"
_MscSigChanEIsdnActiveChannels_Object = MibTableColumn
mscSigChanEIsdnActiveChannels = _MscSigChanEIsdnActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 16, 1, 1),
    _MscSigChanEIsdnActiveChannels_Type()
)
mscSigChanEIsdnActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnActiveChannels.setStatus("mandatory")


class _MscSigChanEIsdnActiveVoiceChannels_Type(Gauge32):
    """Custom type mscSigChanEIsdnActiveVoiceChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEIsdnActiveVoiceChannels_Type.__name__ = "Gauge32"
_MscSigChanEIsdnActiveVoiceChannels_Object = MibTableColumn
mscSigChanEIsdnActiveVoiceChannels = _MscSigChanEIsdnActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 16, 1, 2),
    _MscSigChanEIsdnActiveVoiceChannels_Type()
)
mscSigChanEIsdnActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnActiveVoiceChannels.setStatus("mandatory")


class _MscSigChanEIsdnActiveDataChannels_Type(Gauge32):
    """Custom type mscSigChanEIsdnActiveDataChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEIsdnActiveDataChannels_Type.__name__ = "Gauge32"
_MscSigChanEIsdnActiveDataChannels_Object = MibTableColumn
mscSigChanEIsdnActiveDataChannels = _MscSigChanEIsdnActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 16, 1, 3),
    _MscSigChanEIsdnActiveDataChannels_Type()
)
mscSigChanEIsdnActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnActiveDataChannels.setStatus("mandatory")


class _MscSigChanEIsdnPeakActiveChannels_Type(Gauge32):
    """Custom type mscSigChanEIsdnPeakActiveChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEIsdnPeakActiveChannels_Type.__name__ = "Gauge32"
_MscSigChanEIsdnPeakActiveChannels_Object = MibTableColumn
mscSigChanEIsdnPeakActiveChannels = _MscSigChanEIsdnPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 16, 1, 4),
    _MscSigChanEIsdnPeakActiveChannels_Type()
)
mscSigChanEIsdnPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnPeakActiveChannels.setStatus("mandatory")


class _MscSigChanEIsdnPeakActiveVoiceChannels_Type(Gauge32):
    """Custom type mscSigChanEIsdnPeakActiveVoiceChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEIsdnPeakActiveVoiceChannels_Type.__name__ = "Gauge32"
_MscSigChanEIsdnPeakActiveVoiceChannels_Object = MibTableColumn
mscSigChanEIsdnPeakActiveVoiceChannels = _MscSigChanEIsdnPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 16, 1, 5),
    _MscSigChanEIsdnPeakActiveVoiceChannels_Type()
)
mscSigChanEIsdnPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnPeakActiveVoiceChannels.setStatus("mandatory")


class _MscSigChanEIsdnPeakActiveDataChannels_Type(Gauge32):
    """Custom type mscSigChanEIsdnPeakActiveDataChannels based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEIsdnPeakActiveDataChannels_Type.__name__ = "Gauge32"
_MscSigChanEIsdnPeakActiveDataChannels_Object = MibTableColumn
mscSigChanEIsdnPeakActiveDataChannels = _MscSigChanEIsdnPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 16, 1, 6),
    _MscSigChanEIsdnPeakActiveDataChannels_Type()
)
mscSigChanEIsdnPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnPeakActiveDataChannels.setStatus("mandatory")


class _MscSigChanEIsdnDChanStatus_Type(Integer32):
    """Custom type mscSigChanEIsdnDChanStatus based on Integer32"""
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


_MscSigChanEIsdnDChanStatus_Type.__name__ = "Integer32"
_MscSigChanEIsdnDChanStatus_Object = MibTableColumn
mscSigChanEIsdnDChanStatus = _MscSigChanEIsdnDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 16, 1, 7),
    _MscSigChanEIsdnDChanStatus_Type()
)
mscSigChanEIsdnDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEIsdnDChanStatus.setStatus("mandatory")
_MscSigChanEIsdnToolsTable_Object = MibTable
mscSigChanEIsdnToolsTable = _MscSigChanEIsdnToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 17)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnToolsTable.setStatus("mandatory")
_MscSigChanEIsdnToolsEntry_Object = MibTableRow
mscSigChanEIsdnToolsEntry = _MscSigChanEIsdnToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 17, 1)
)
mscSigChanEIsdnToolsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnToolsEntry.setStatus("mandatory")


class _MscSigChanEIsdnTracing_Type(OctetString):
    """Custom type mscSigChanEIsdnTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscSigChanEIsdnTracing_Type.__name__ = "OctetString"
_MscSigChanEIsdnTracing_Object = MibTableColumn
mscSigChanEIsdnTracing = _MscSigChanEIsdnTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 17, 1, 1),
    _MscSigChanEIsdnTracing_Type()
)
mscSigChanEIsdnTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnTracing.setStatus("mandatory")
_MscSigChanEIsdnOptTable_Object = MibTable
mscSigChanEIsdnOptTable = _MscSigChanEIsdnOptTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 18)
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnOptTable.setStatus("mandatory")
_MscSigChanEIsdnOptEntry_Object = MibTableRow
mscSigChanEIsdnOptEntry = _MscSigChanEIsdnOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 18, 1)
)
mscSigChanEIsdnOptEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB", "mscSigChanEIsdnIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEIsdnOptEntry.setStatus("mandatory")


class _MscSigChanEIsdnVariant_Type(Integer32):
    """Custom type mscSigChanEIsdnVariant based on Integer32"""
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


_MscSigChanEIsdnVariant_Type.__name__ = "Integer32"
_MscSigChanEIsdnVariant_Object = MibTableColumn
mscSigChanEIsdnVariant = _MscSigChanEIsdnVariant_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 18, 1, 1),
    _MscSigChanEIsdnVariant_Type()
)
mscSigChanEIsdnVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnVariant.setStatus("mandatory")


class _MscSigChanEIsdnConnectServiceTimer_Type(Unsigned32):
    """Custom type mscSigChanEIsdnConnectServiceTimer based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscSigChanEIsdnConnectServiceTimer_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnConnectServiceTimer_Object = MibTableColumn
mscSigChanEIsdnConnectServiceTimer = _MscSigChanEIsdnConnectServiceTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 18, 1, 2),
    _MscSigChanEIsdnConnectServiceTimer_Type()
)
mscSigChanEIsdnConnectServiceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnConnectServiceTimer.setStatus("mandatory")


class _MscSigChanEIsdnResponseServiceTimer_Type(Unsigned32):
    """Custom type mscSigChanEIsdnResponseServiceTimer based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscSigChanEIsdnResponseServiceTimer_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnResponseServiceTimer_Object = MibTableColumn
mscSigChanEIsdnResponseServiceTimer = _MscSigChanEIsdnResponseServiceTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 18, 1, 3),
    _MscSigChanEIsdnResponseServiceTimer_Type()
)
mscSigChanEIsdnResponseServiceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnResponseServiceTimer.setStatus("mandatory")


class _MscSigChanEIsdnLifetimeServiceTimer_Type(Unsigned32):
    """Custom type mscSigChanEIsdnLifetimeServiceTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_MscSigChanEIsdnLifetimeServiceTimer_Type.__name__ = "Unsigned32"
_MscSigChanEIsdnLifetimeServiceTimer_Object = MibTableColumn
mscSigChanEIsdnLifetimeServiceTimer = _MscSigChanEIsdnLifetimeServiceTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 14, 18, 1, 4),
    _MscSigChanEIsdnLifetimeServiceTimer_Type()
)
mscSigChanEIsdnLifetimeServiceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEIsdnLifetimeServiceTimer.setStatus("mandatory")
_VnetEuroIsdnMIB_ObjectIdentity = ObjectIdentity
vnetEuroIsdnMIB = _VnetEuroIsdnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 138)
)
_VnetEuroIsdnGroup_ObjectIdentity = ObjectIdentity
vnetEuroIsdnGroup = _VnetEuroIsdnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 138, 1)
)
_VnetEuroIsdnGroupCA_ObjectIdentity = ObjectIdentity
vnetEuroIsdnGroupCA = _VnetEuroIsdnGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 138, 1, 1)
)
_VnetEuroIsdnGroupCA02_ObjectIdentity = ObjectIdentity
vnetEuroIsdnGroupCA02 = _VnetEuroIsdnGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 138, 1, 1, 3)
)
_VnetEuroIsdnGroupCA02A_ObjectIdentity = ObjectIdentity
vnetEuroIsdnGroupCA02A = _VnetEuroIsdnGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 138, 1, 1, 3, 2)
)
_VnetEuroIsdnCapabilities_ObjectIdentity = ObjectIdentity
vnetEuroIsdnCapabilities = _VnetEuroIsdnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 138, 3)
)
_VnetEuroIsdnCapabilitiesCA_ObjectIdentity = ObjectIdentity
vnetEuroIsdnCapabilitiesCA = _VnetEuroIsdnCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 138, 3, 1)
)
_VnetEuroIsdnCapabilitiesCA02_ObjectIdentity = ObjectIdentity
vnetEuroIsdnCapabilitiesCA02 = _VnetEuroIsdnCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 138, 3, 1, 3)
)
_VnetEuroIsdnCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
vnetEuroIsdnCapabilitiesCA02A = _VnetEuroIsdnCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 138, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VnetEuroIsdnMIB",
    **{"mscSigChanEIsdn": mscSigChanEIsdn,
       "mscSigChanEIsdnRowStatusTable": mscSigChanEIsdnRowStatusTable,
       "mscSigChanEIsdnRowStatusEntry": mscSigChanEIsdnRowStatusEntry,
       "mscSigChanEIsdnRowStatus": mscSigChanEIsdnRowStatus,
       "mscSigChanEIsdnComponentName": mscSigChanEIsdnComponentName,
       "mscSigChanEIsdnStorageType": mscSigChanEIsdnStorageType,
       "mscSigChanEIsdnIndex": mscSigChanEIsdnIndex,
       "mscSigChanEIsdnFramer": mscSigChanEIsdnFramer,
       "mscSigChanEIsdnFramerRowStatusTable": mscSigChanEIsdnFramerRowStatusTable,
       "mscSigChanEIsdnFramerRowStatusEntry": mscSigChanEIsdnFramerRowStatusEntry,
       "mscSigChanEIsdnFramerRowStatus": mscSigChanEIsdnFramerRowStatus,
       "mscSigChanEIsdnFramerComponentName": mscSigChanEIsdnFramerComponentName,
       "mscSigChanEIsdnFramerStorageType": mscSigChanEIsdnFramerStorageType,
       "mscSigChanEIsdnFramerIndex": mscSigChanEIsdnFramerIndex,
       "mscSigChanEIsdnFramerProvTable": mscSigChanEIsdnFramerProvTable,
       "mscSigChanEIsdnFramerProvEntry": mscSigChanEIsdnFramerProvEntry,
       "mscSigChanEIsdnFramerInterfaceName": mscSigChanEIsdnFramerInterfaceName,
       "mscSigChanEIsdnFramerStateTable": mscSigChanEIsdnFramerStateTable,
       "mscSigChanEIsdnFramerStateEntry": mscSigChanEIsdnFramerStateEntry,
       "mscSigChanEIsdnFramerAdminState": mscSigChanEIsdnFramerAdminState,
       "mscSigChanEIsdnFramerOperationalState": mscSigChanEIsdnFramerOperationalState,
       "mscSigChanEIsdnFramerUsageState": mscSigChanEIsdnFramerUsageState,
       "mscSigChanEIsdnFramerStatsTable": mscSigChanEIsdnFramerStatsTable,
       "mscSigChanEIsdnFramerStatsEntry": mscSigChanEIsdnFramerStatsEntry,
       "mscSigChanEIsdnFramerFrmToIf": mscSigChanEIsdnFramerFrmToIf,
       "mscSigChanEIsdnFramerFrmFromIf": mscSigChanEIsdnFramerFrmFromIf,
       "mscSigChanEIsdnFramerOctetFromIf": mscSigChanEIsdnFramerOctetFromIf,
       "mscSigChanEIsdnFramerAborts": mscSigChanEIsdnFramerAborts,
       "mscSigChanEIsdnFramerCrcErrors": mscSigChanEIsdnFramerCrcErrors,
       "mscSigChanEIsdnFramerLrcErrors": mscSigChanEIsdnFramerLrcErrors,
       "mscSigChanEIsdnFramerNonOctetErrors": mscSigChanEIsdnFramerNonOctetErrors,
       "mscSigChanEIsdnFramerOverruns": mscSigChanEIsdnFramerOverruns,
       "mscSigChanEIsdnFramerUnderruns": mscSigChanEIsdnFramerUnderruns,
       "mscSigChanEIsdnFramerLargeFrmErrors": mscSigChanEIsdnFramerLargeFrmErrors,
       "mscSigChanEIsdnL2Table": mscSigChanEIsdnL2Table,
       "mscSigChanEIsdnL2Entry": mscSigChanEIsdnL2Entry,
       "mscSigChanEIsdnT23": mscSigChanEIsdnT23,
       "mscSigChanEIsdnT200": mscSigChanEIsdnT200,
       "mscSigChanEIsdnN200": mscSigChanEIsdnN200,
       "mscSigChanEIsdnT203": mscSigChanEIsdnT203,
       "mscSigChanEIsdnCircuitSwitchedK": mscSigChanEIsdnCircuitSwitchedK,
       "mscSigChanEIsdnL3Table": mscSigChanEIsdnL3Table,
       "mscSigChanEIsdnL3Entry": mscSigChanEIsdnL3Entry,
       "mscSigChanEIsdnT310": mscSigChanEIsdnT310,
       "mscSigChanEIsdnProvTable": mscSigChanEIsdnProvTable,
       "mscSigChanEIsdnProvEntry": mscSigChanEIsdnProvEntry,
       "mscSigChanEIsdnSide": mscSigChanEIsdnSide,
       "mscSigChanEIsdnMaxNonCallConcurrent": mscSigChanEIsdnMaxNonCallConcurrent,
       "mscSigChanEIsdnOverlapSending": mscSigChanEIsdnOverlapSending,
       "mscSigChanEIsdnOverlapReceiving": mscSigChanEIsdnOverlapReceiving,
       "mscSigChanEIsdnStateTable": mscSigChanEIsdnStateTable,
       "mscSigChanEIsdnStateEntry": mscSigChanEIsdnStateEntry,
       "mscSigChanEIsdnAdminState": mscSigChanEIsdnAdminState,
       "mscSigChanEIsdnOperationalState": mscSigChanEIsdnOperationalState,
       "mscSigChanEIsdnUsageState": mscSigChanEIsdnUsageState,
       "mscSigChanEIsdnStatsTable": mscSigChanEIsdnStatsTable,
       "mscSigChanEIsdnStatsEntry": mscSigChanEIsdnStatsEntry,
       "mscSigChanEIsdnTotalCallsToIf": mscSigChanEIsdnTotalCallsToIf,
       "mscSigChanEIsdnTotalCallsFromIf": mscSigChanEIsdnTotalCallsFromIf,
       "mscSigChanEIsdnNonCallAssocSessionsToIf": mscSigChanEIsdnNonCallAssocSessionsToIf,
       "mscSigChanEIsdnNonCallAssocSessionsFromIf": mscSigChanEIsdnNonCallAssocSessionsFromIf,
       "mscSigChanEIsdnOperTable": mscSigChanEIsdnOperTable,
       "mscSigChanEIsdnOperEntry": mscSigChanEIsdnOperEntry,
       "mscSigChanEIsdnActiveChannels": mscSigChanEIsdnActiveChannels,
       "mscSigChanEIsdnActiveVoiceChannels": mscSigChanEIsdnActiveVoiceChannels,
       "mscSigChanEIsdnActiveDataChannels": mscSigChanEIsdnActiveDataChannels,
       "mscSigChanEIsdnPeakActiveChannels": mscSigChanEIsdnPeakActiveChannels,
       "mscSigChanEIsdnPeakActiveVoiceChannels": mscSigChanEIsdnPeakActiveVoiceChannels,
       "mscSigChanEIsdnPeakActiveDataChannels": mscSigChanEIsdnPeakActiveDataChannels,
       "mscSigChanEIsdnDChanStatus": mscSigChanEIsdnDChanStatus,
       "mscSigChanEIsdnToolsTable": mscSigChanEIsdnToolsTable,
       "mscSigChanEIsdnToolsEntry": mscSigChanEIsdnToolsEntry,
       "mscSigChanEIsdnTracing": mscSigChanEIsdnTracing,
       "mscSigChanEIsdnOptTable": mscSigChanEIsdnOptTable,
       "mscSigChanEIsdnOptEntry": mscSigChanEIsdnOptEntry,
       "mscSigChanEIsdnVariant": mscSigChanEIsdnVariant,
       "mscSigChanEIsdnConnectServiceTimer": mscSigChanEIsdnConnectServiceTimer,
       "mscSigChanEIsdnResponseServiceTimer": mscSigChanEIsdnResponseServiceTimer,
       "mscSigChanEIsdnLifetimeServiceTimer": mscSigChanEIsdnLifetimeServiceTimer,
       "vnetEuroIsdnMIB": vnetEuroIsdnMIB,
       "vnetEuroIsdnGroup": vnetEuroIsdnGroup,
       "vnetEuroIsdnGroupCA": vnetEuroIsdnGroupCA,
       "vnetEuroIsdnGroupCA02": vnetEuroIsdnGroupCA02,
       "vnetEuroIsdnGroupCA02A": vnetEuroIsdnGroupCA02A,
       "vnetEuroIsdnCapabilities": vnetEuroIsdnCapabilities,
       "vnetEuroIsdnCapabilitiesCA": vnetEuroIsdnCapabilitiesCA,
       "vnetEuroIsdnCapabilitiesCA02": vnetEuroIsdnCapabilitiesCA02,
       "vnetEuroIsdnCapabilitiesCA02A": vnetEuroIsdnCapabilitiesCA02A}
)
