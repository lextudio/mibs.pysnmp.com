# SNMP MIB module (Nortel-Magellan-Passport-DisdnJapanInsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DisdnJapanInsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:35 2024
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

(dataSigChan,
 dataSigChanIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-DataIsdnMIB",
    "dataSigChan",
    "dataSigChanIndex")

(DisplayString,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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

_DataSigChanIns_ObjectIdentity = ObjectIdentity
dataSigChanIns = _DataSigChanIns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11)
)
_DataSigChanInsRowStatusTable_Object = MibTable
dataSigChanInsRowStatusTable = _DataSigChanInsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1)
)
if mibBuilder.loadTexts:
    dataSigChanInsRowStatusTable.setStatus("mandatory")
_DataSigChanInsRowStatusEntry_Object = MibTableRow
dataSigChanInsRowStatusEntry = _DataSigChanInsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1)
)
dataSigChanInsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanInsRowStatusEntry.setStatus("mandatory")
_DataSigChanInsRowStatus_Type = RowStatus
_DataSigChanInsRowStatus_Object = MibTableColumn
dataSigChanInsRowStatus = _DataSigChanInsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1, 1),
    _DataSigChanInsRowStatus_Type()
)
dataSigChanInsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsRowStatus.setStatus("mandatory")
_DataSigChanInsComponentName_Type = DisplayString
_DataSigChanInsComponentName_Object = MibTableColumn
dataSigChanInsComponentName = _DataSigChanInsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1, 2),
    _DataSigChanInsComponentName_Type()
)
dataSigChanInsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsComponentName.setStatus("mandatory")
_DataSigChanInsStorageType_Type = StorageType
_DataSigChanInsStorageType_Object = MibTableColumn
dataSigChanInsStorageType = _DataSigChanInsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1, 4),
    _DataSigChanInsStorageType_Type()
)
dataSigChanInsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsStorageType.setStatus("mandatory")
_DataSigChanInsIndex_Type = NonReplicated
_DataSigChanInsIndex_Object = MibTableColumn
dataSigChanInsIndex = _DataSigChanInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1, 10),
    _DataSigChanInsIndex_Type()
)
dataSigChanInsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanInsIndex.setStatus("mandatory")
_DataSigChanInsFramer_ObjectIdentity = ObjectIdentity
dataSigChanInsFramer = _DataSigChanInsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2)
)
_DataSigChanInsFramerRowStatusTable_Object = MibTable
dataSigChanInsFramerRowStatusTable = _DataSigChanInsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanInsFramerRowStatusTable.setStatus("mandatory")
_DataSigChanInsFramerRowStatusEntry_Object = MibTableRow
dataSigChanInsFramerRowStatusEntry = _DataSigChanInsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1)
)
dataSigChanInsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanInsFramerRowStatusEntry.setStatus("mandatory")
_DataSigChanInsFramerRowStatus_Type = RowStatus
_DataSigChanInsFramerRowStatus_Object = MibTableColumn
dataSigChanInsFramerRowStatus = _DataSigChanInsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1, 1),
    _DataSigChanInsFramerRowStatus_Type()
)
dataSigChanInsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerRowStatus.setStatus("mandatory")
_DataSigChanInsFramerComponentName_Type = DisplayString
_DataSigChanInsFramerComponentName_Object = MibTableColumn
dataSigChanInsFramerComponentName = _DataSigChanInsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1, 2),
    _DataSigChanInsFramerComponentName_Type()
)
dataSigChanInsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerComponentName.setStatus("mandatory")
_DataSigChanInsFramerStorageType_Type = StorageType
_DataSigChanInsFramerStorageType_Object = MibTableColumn
dataSigChanInsFramerStorageType = _DataSigChanInsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1, 4),
    _DataSigChanInsFramerStorageType_Type()
)
dataSigChanInsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerStorageType.setStatus("mandatory")
_DataSigChanInsFramerIndex_Type = NonReplicated
_DataSigChanInsFramerIndex_Object = MibTableColumn
dataSigChanInsFramerIndex = _DataSigChanInsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1, 10),
    _DataSigChanInsFramerIndex_Type()
)
dataSigChanInsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanInsFramerIndex.setStatus("mandatory")
_DataSigChanInsFramerProvTable_Object = MibTable
dataSigChanInsFramerProvTable = _DataSigChanInsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 10)
)
if mibBuilder.loadTexts:
    dataSigChanInsFramerProvTable.setStatus("mandatory")
_DataSigChanInsFramerProvEntry_Object = MibTableRow
dataSigChanInsFramerProvEntry = _DataSigChanInsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 10, 1)
)
dataSigChanInsFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanInsFramerProvEntry.setStatus("mandatory")
_DataSigChanInsFramerInterfaceName_Type = Link
_DataSigChanInsFramerInterfaceName_Object = MibTableColumn
dataSigChanInsFramerInterfaceName = _DataSigChanInsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 10, 1, 1),
    _DataSigChanInsFramerInterfaceName_Type()
)
dataSigChanInsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsFramerInterfaceName.setStatus("mandatory")
_DataSigChanInsFramerStateTable_Object = MibTable
dataSigChanInsFramerStateTable = _DataSigChanInsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12)
)
if mibBuilder.loadTexts:
    dataSigChanInsFramerStateTable.setStatus("mandatory")
_DataSigChanInsFramerStateEntry_Object = MibTableRow
dataSigChanInsFramerStateEntry = _DataSigChanInsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12, 1)
)
dataSigChanInsFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanInsFramerStateEntry.setStatus("mandatory")


class _DataSigChanInsFramerAdminState_Type(Integer32):
    """Custom type dataSigChanInsFramerAdminState based on Integer32"""
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


_DataSigChanInsFramerAdminState_Type.__name__ = "Integer32"
_DataSigChanInsFramerAdminState_Object = MibTableColumn
dataSigChanInsFramerAdminState = _DataSigChanInsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12, 1, 1),
    _DataSigChanInsFramerAdminState_Type()
)
dataSigChanInsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerAdminState.setStatus("mandatory")


class _DataSigChanInsFramerOperationalState_Type(Integer32):
    """Custom type dataSigChanInsFramerOperationalState based on Integer32"""
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


_DataSigChanInsFramerOperationalState_Type.__name__ = "Integer32"
_DataSigChanInsFramerOperationalState_Object = MibTableColumn
dataSigChanInsFramerOperationalState = _DataSigChanInsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12, 1, 2),
    _DataSigChanInsFramerOperationalState_Type()
)
dataSigChanInsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerOperationalState.setStatus("mandatory")


class _DataSigChanInsFramerUsageState_Type(Integer32):
    """Custom type dataSigChanInsFramerUsageState based on Integer32"""
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


_DataSigChanInsFramerUsageState_Type.__name__ = "Integer32"
_DataSigChanInsFramerUsageState_Object = MibTableColumn
dataSigChanInsFramerUsageState = _DataSigChanInsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12, 1, 3),
    _DataSigChanInsFramerUsageState_Type()
)
dataSigChanInsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerUsageState.setStatus("mandatory")
_DataSigChanInsFramerStatsTable_Object = MibTable
dataSigChanInsFramerStatsTable = _DataSigChanInsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13)
)
if mibBuilder.loadTexts:
    dataSigChanInsFramerStatsTable.setStatus("mandatory")
_DataSigChanInsFramerStatsEntry_Object = MibTableRow
dataSigChanInsFramerStatsEntry = _DataSigChanInsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1)
)
dataSigChanInsFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanInsFramerStatsEntry.setStatus("mandatory")


class _DataSigChanInsFramerFrmToIf_Type(Unsigned32):
    """Custom type dataSigChanInsFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerFrmToIf_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerFrmToIf_Object = MibTableColumn
dataSigChanInsFramerFrmToIf = _DataSigChanInsFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 1),
    _DataSigChanInsFramerFrmToIf_Type()
)
dataSigChanInsFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerFrmToIf.setStatus("mandatory")


class _DataSigChanInsFramerFrmFromIf_Type(Unsigned32):
    """Custom type dataSigChanInsFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerFrmFromIf_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerFrmFromIf_Object = MibTableColumn
dataSigChanInsFramerFrmFromIf = _DataSigChanInsFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 2),
    _DataSigChanInsFramerFrmFromIf_Type()
)
dataSigChanInsFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerFrmFromIf.setStatus("mandatory")


class _DataSigChanInsFramerOctetFromIf_Type(Unsigned32):
    """Custom type dataSigChanInsFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerOctetFromIf_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerOctetFromIf_Object = MibTableColumn
dataSigChanInsFramerOctetFromIf = _DataSigChanInsFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 3),
    _DataSigChanInsFramerOctetFromIf_Type()
)
dataSigChanInsFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerOctetFromIf.setStatus("mandatory")


class _DataSigChanInsFramerAborts_Type(Unsigned32):
    """Custom type dataSigChanInsFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerAborts_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerAborts_Object = MibTableColumn
dataSigChanInsFramerAborts = _DataSigChanInsFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 4),
    _DataSigChanInsFramerAborts_Type()
)
dataSigChanInsFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerAborts.setStatus("mandatory")


class _DataSigChanInsFramerCrcErrors_Type(Unsigned32):
    """Custom type dataSigChanInsFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerCrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerCrcErrors_Object = MibTableColumn
dataSigChanInsFramerCrcErrors = _DataSigChanInsFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 5),
    _DataSigChanInsFramerCrcErrors_Type()
)
dataSigChanInsFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerCrcErrors.setStatus("mandatory")


class _DataSigChanInsFramerLrcErrors_Type(Unsigned32):
    """Custom type dataSigChanInsFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerLrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerLrcErrors_Object = MibTableColumn
dataSigChanInsFramerLrcErrors = _DataSigChanInsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 6),
    _DataSigChanInsFramerLrcErrors_Type()
)
dataSigChanInsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerLrcErrors.setStatus("mandatory")


class _DataSigChanInsFramerNonOctetErrors_Type(Unsigned32):
    """Custom type dataSigChanInsFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerNonOctetErrors_Object = MibTableColumn
dataSigChanInsFramerNonOctetErrors = _DataSigChanInsFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 7),
    _DataSigChanInsFramerNonOctetErrors_Type()
)
dataSigChanInsFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerNonOctetErrors.setStatus("mandatory")


class _DataSigChanInsFramerOverruns_Type(Unsigned32):
    """Custom type dataSigChanInsFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerOverruns_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerOverruns_Object = MibTableColumn
dataSigChanInsFramerOverruns = _DataSigChanInsFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 8),
    _DataSigChanInsFramerOverruns_Type()
)
dataSigChanInsFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerOverruns.setStatus("mandatory")


class _DataSigChanInsFramerUnderruns_Type(Unsigned32):
    """Custom type dataSigChanInsFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerUnderruns_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerUnderruns_Object = MibTableColumn
dataSigChanInsFramerUnderruns = _DataSigChanInsFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 9),
    _DataSigChanInsFramerUnderruns_Type()
)
dataSigChanInsFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerUnderruns.setStatus("mandatory")


class _DataSigChanInsFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type dataSigChanInsFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanInsFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_DataSigChanInsFramerLargeFrmErrors_Object = MibTableColumn
dataSigChanInsFramerLargeFrmErrors = _DataSigChanInsFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 10),
    _DataSigChanInsFramerLargeFrmErrors_Type()
)
dataSigChanInsFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsFramerLargeFrmErrors.setStatus("mandatory")
_DataSigChanInsL2Table_Object = MibTable
dataSigChanInsL2Table = _DataSigChanInsL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11)
)
if mibBuilder.loadTexts:
    dataSigChanInsL2Table.setStatus("mandatory")
_DataSigChanInsL2Entry_Object = MibTableRow
dataSigChanInsL2Entry = _DataSigChanInsL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1)
)
dataSigChanInsL2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanInsL2Entry.setStatus("mandatory")


class _DataSigChanInsT23_Type(Unsigned32):
    """Custom type dataSigChanInsT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DataSigChanInsT23_Type.__name__ = "Unsigned32"
_DataSigChanInsT23_Object = MibTableColumn
dataSigChanInsT23 = _DataSigChanInsT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 1),
    _DataSigChanInsT23_Type()
)
dataSigChanInsT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsT23.setStatus("mandatory")


class _DataSigChanInsT200_Type(Unsigned32):
    """Custom type dataSigChanInsT200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DataSigChanInsT200_Type.__name__ = "Unsigned32"
_DataSigChanInsT200_Object = MibTableColumn
dataSigChanInsT200 = _DataSigChanInsT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 2),
    _DataSigChanInsT200_Type()
)
dataSigChanInsT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsT200.setStatus("mandatory")


class _DataSigChanInsN200_Type(Unsigned32):
    """Custom type dataSigChanInsN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DataSigChanInsN200_Type.__name__ = "Unsigned32"
_DataSigChanInsN200_Object = MibTableColumn
dataSigChanInsN200 = _DataSigChanInsN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 3),
    _DataSigChanInsN200_Type()
)
dataSigChanInsN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsN200.setStatus("mandatory")


class _DataSigChanInsT203_Type(Unsigned32):
    """Custom type dataSigChanInsT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_DataSigChanInsT203_Type.__name__ = "Unsigned32"
_DataSigChanInsT203_Object = MibTableColumn
dataSigChanInsT203 = _DataSigChanInsT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 4),
    _DataSigChanInsT203_Type()
)
dataSigChanInsT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsT203.setStatus("mandatory")


class _DataSigChanInsN201_Type(Unsigned32):
    """Custom type dataSigChanInsN201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_DataSigChanInsN201_Type.__name__ = "Unsigned32"
_DataSigChanInsN201_Object = MibTableColumn
dataSigChanInsN201 = _DataSigChanInsN201_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 5),
    _DataSigChanInsN201_Type()
)
dataSigChanInsN201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsN201.setStatus("mandatory")


class _DataSigChanInsCircuitSwitchedK_Type(Unsigned32):
    """Custom type dataSigChanInsCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_DataSigChanInsCircuitSwitchedK_Type.__name__ = "Unsigned32"
_DataSigChanInsCircuitSwitchedK_Object = MibTableColumn
dataSigChanInsCircuitSwitchedK = _DataSigChanInsCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 6),
    _DataSigChanInsCircuitSwitchedK_Type()
)
dataSigChanInsCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsCircuitSwitchedK.setStatus("mandatory")
_DataSigChanInsProvTable_Object = MibTable
dataSigChanInsProvTable = _DataSigChanInsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 13)
)
if mibBuilder.loadTexts:
    dataSigChanInsProvTable.setStatus("mandatory")
_DataSigChanInsProvEntry_Object = MibTableRow
dataSigChanInsProvEntry = _DataSigChanInsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 13, 1)
)
dataSigChanInsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanInsProvEntry.setStatus("mandatory")


class _DataSigChanInsSide_Type(Integer32):
    """Custom type dataSigChanInsSide based on Integer32"""
    defaultValue = 2

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


_DataSigChanInsSide_Type.__name__ = "Integer32"
_DataSigChanInsSide_Object = MibTableColumn
dataSigChanInsSide = _DataSigChanInsSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 13, 1, 1),
    _DataSigChanInsSide_Type()
)
dataSigChanInsSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsSide.setStatus("mandatory")
_DataSigChanInsOperTable_Object = MibTable
dataSigChanInsOperTable = _DataSigChanInsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15)
)
if mibBuilder.loadTexts:
    dataSigChanInsOperTable.setStatus("mandatory")
_DataSigChanInsOperEntry_Object = MibTableRow
dataSigChanInsOperEntry = _DataSigChanInsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15, 1)
)
dataSigChanInsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanInsOperEntry.setStatus("mandatory")


class _DataSigChanInsActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanInsActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanInsActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanInsActiveChannels_Object = MibTableColumn
dataSigChanInsActiveChannels = _DataSigChanInsActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15, 1, 1),
    _DataSigChanInsActiveChannels_Type()
)
dataSigChanInsActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsActiveChannels.setStatus("mandatory")


class _DataSigChanInsPeakActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanInsPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanInsPeakActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanInsPeakActiveChannels_Object = MibTableColumn
dataSigChanInsPeakActiveChannels = _DataSigChanInsPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15, 1, 4),
    _DataSigChanInsPeakActiveChannels_Type()
)
dataSigChanInsPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsPeakActiveChannels.setStatus("mandatory")


class _DataSigChanInsDChanStatus_Type(Integer32):
    """Custom type dataSigChanInsDChanStatus based on Integer32"""
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


_DataSigChanInsDChanStatus_Type.__name__ = "Integer32"
_DataSigChanInsDChanStatus_Object = MibTableColumn
dataSigChanInsDChanStatus = _DataSigChanInsDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15, 1, 7),
    _DataSigChanInsDChanStatus_Type()
)
dataSigChanInsDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanInsDChanStatus.setStatus("mandatory")
_DataSigChanInsToolsTable_Object = MibTable
dataSigChanInsToolsTable = _DataSigChanInsToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 16)
)
if mibBuilder.loadTexts:
    dataSigChanInsToolsTable.setStatus("mandatory")
_DataSigChanInsToolsEntry_Object = MibTableRow
dataSigChanInsToolsEntry = _DataSigChanInsToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 16, 1)
)
dataSigChanInsToolsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanInsToolsEntry.setStatus("mandatory")


class _DataSigChanInsTracing_Type(OctetString):
    """Custom type dataSigChanInsTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DataSigChanInsTracing_Type.__name__ = "OctetString"
_DataSigChanInsTracing_Object = MibTableColumn
dataSigChanInsTracing = _DataSigChanInsTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 16, 1, 1),
    _DataSigChanInsTracing_Type()
)
dataSigChanInsTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanInsTracing.setStatus("mandatory")
_DisdnJapanInsMIB_ObjectIdentity = ObjectIdentity
disdnJapanInsMIB = _DisdnJapanInsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118)
)
_DisdnJapanInsGroup_ObjectIdentity = ObjectIdentity
disdnJapanInsGroup = _DisdnJapanInsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 1)
)
_DisdnJapanInsGroupBE_ObjectIdentity = ObjectIdentity
disdnJapanInsGroupBE = _DisdnJapanInsGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 1, 5)
)
_DisdnJapanInsGroupBE00_ObjectIdentity = ObjectIdentity
disdnJapanInsGroupBE00 = _DisdnJapanInsGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 1, 5, 1)
)
_DisdnJapanInsGroupBE00A_ObjectIdentity = ObjectIdentity
disdnJapanInsGroupBE00A = _DisdnJapanInsGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 1, 5, 1, 2)
)
_DisdnJapanInsCapabilities_ObjectIdentity = ObjectIdentity
disdnJapanInsCapabilities = _DisdnJapanInsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 3)
)
_DisdnJapanInsCapabilitiesBE_ObjectIdentity = ObjectIdentity
disdnJapanInsCapabilitiesBE = _DisdnJapanInsCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 3, 5)
)
_DisdnJapanInsCapabilitiesBE00_ObjectIdentity = ObjectIdentity
disdnJapanInsCapabilitiesBE00 = _DisdnJapanInsCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 3, 5, 1)
)
_DisdnJapanInsCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
disdnJapanInsCapabilitiesBE00A = _DisdnJapanInsCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DisdnJapanInsMIB",
    **{"dataSigChanIns": dataSigChanIns,
       "dataSigChanInsRowStatusTable": dataSigChanInsRowStatusTable,
       "dataSigChanInsRowStatusEntry": dataSigChanInsRowStatusEntry,
       "dataSigChanInsRowStatus": dataSigChanInsRowStatus,
       "dataSigChanInsComponentName": dataSigChanInsComponentName,
       "dataSigChanInsStorageType": dataSigChanInsStorageType,
       "dataSigChanInsIndex": dataSigChanInsIndex,
       "dataSigChanInsFramer": dataSigChanInsFramer,
       "dataSigChanInsFramerRowStatusTable": dataSigChanInsFramerRowStatusTable,
       "dataSigChanInsFramerRowStatusEntry": dataSigChanInsFramerRowStatusEntry,
       "dataSigChanInsFramerRowStatus": dataSigChanInsFramerRowStatus,
       "dataSigChanInsFramerComponentName": dataSigChanInsFramerComponentName,
       "dataSigChanInsFramerStorageType": dataSigChanInsFramerStorageType,
       "dataSigChanInsFramerIndex": dataSigChanInsFramerIndex,
       "dataSigChanInsFramerProvTable": dataSigChanInsFramerProvTable,
       "dataSigChanInsFramerProvEntry": dataSigChanInsFramerProvEntry,
       "dataSigChanInsFramerInterfaceName": dataSigChanInsFramerInterfaceName,
       "dataSigChanInsFramerStateTable": dataSigChanInsFramerStateTable,
       "dataSigChanInsFramerStateEntry": dataSigChanInsFramerStateEntry,
       "dataSigChanInsFramerAdminState": dataSigChanInsFramerAdminState,
       "dataSigChanInsFramerOperationalState": dataSigChanInsFramerOperationalState,
       "dataSigChanInsFramerUsageState": dataSigChanInsFramerUsageState,
       "dataSigChanInsFramerStatsTable": dataSigChanInsFramerStatsTable,
       "dataSigChanInsFramerStatsEntry": dataSigChanInsFramerStatsEntry,
       "dataSigChanInsFramerFrmToIf": dataSigChanInsFramerFrmToIf,
       "dataSigChanInsFramerFrmFromIf": dataSigChanInsFramerFrmFromIf,
       "dataSigChanInsFramerOctetFromIf": dataSigChanInsFramerOctetFromIf,
       "dataSigChanInsFramerAborts": dataSigChanInsFramerAborts,
       "dataSigChanInsFramerCrcErrors": dataSigChanInsFramerCrcErrors,
       "dataSigChanInsFramerLrcErrors": dataSigChanInsFramerLrcErrors,
       "dataSigChanInsFramerNonOctetErrors": dataSigChanInsFramerNonOctetErrors,
       "dataSigChanInsFramerOverruns": dataSigChanInsFramerOverruns,
       "dataSigChanInsFramerUnderruns": dataSigChanInsFramerUnderruns,
       "dataSigChanInsFramerLargeFrmErrors": dataSigChanInsFramerLargeFrmErrors,
       "dataSigChanInsL2Table": dataSigChanInsL2Table,
       "dataSigChanInsL2Entry": dataSigChanInsL2Entry,
       "dataSigChanInsT23": dataSigChanInsT23,
       "dataSigChanInsT200": dataSigChanInsT200,
       "dataSigChanInsN200": dataSigChanInsN200,
       "dataSigChanInsT203": dataSigChanInsT203,
       "dataSigChanInsN201": dataSigChanInsN201,
       "dataSigChanInsCircuitSwitchedK": dataSigChanInsCircuitSwitchedK,
       "dataSigChanInsProvTable": dataSigChanInsProvTable,
       "dataSigChanInsProvEntry": dataSigChanInsProvEntry,
       "dataSigChanInsSide": dataSigChanInsSide,
       "dataSigChanInsOperTable": dataSigChanInsOperTable,
       "dataSigChanInsOperEntry": dataSigChanInsOperEntry,
       "dataSigChanInsActiveChannels": dataSigChanInsActiveChannels,
       "dataSigChanInsPeakActiveChannels": dataSigChanInsPeakActiveChannels,
       "dataSigChanInsDChanStatus": dataSigChanInsDChanStatus,
       "dataSigChanInsToolsTable": dataSigChanInsToolsTable,
       "dataSigChanInsToolsEntry": dataSigChanInsToolsEntry,
       "dataSigChanInsTracing": dataSigChanInsTracing,
       "disdnJapanInsMIB": disdnJapanInsMIB,
       "disdnJapanInsGroup": disdnJapanInsGroup,
       "disdnJapanInsGroupBE": disdnJapanInsGroupBE,
       "disdnJapanInsGroupBE00": disdnJapanInsGroupBE00,
       "disdnJapanInsGroupBE00A": disdnJapanInsGroupBE00A,
       "disdnJapanInsCapabilities": disdnJapanInsCapabilities,
       "disdnJapanInsCapabilitiesBE": disdnJapanInsCapabilitiesBE,
       "disdnJapanInsCapabilitiesBE00": disdnJapanInsCapabilitiesBE00,
       "disdnJapanInsCapabilitiesBE00A": disdnJapanInsCapabilitiesBE00A}
)
