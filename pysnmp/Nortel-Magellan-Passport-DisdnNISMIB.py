# SNMP MIB module (Nortel-Magellan-Passport-DisdnNISMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DisdnNISMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:37 2024
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

_DataSigChanNis_ObjectIdentity = ObjectIdentity
dataSigChanNis = _DataSigChanNis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13)
)
_DataSigChanNisRowStatusTable_Object = MibTable
dataSigChanNisRowStatusTable = _DataSigChanNisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 1)
)
if mibBuilder.loadTexts:
    dataSigChanNisRowStatusTable.setStatus("mandatory")
_DataSigChanNisRowStatusEntry_Object = MibTableRow
dataSigChanNisRowStatusEntry = _DataSigChanNisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 1, 1)
)
dataSigChanNisRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNisRowStatusEntry.setStatus("mandatory")
_DataSigChanNisRowStatus_Type = RowStatus
_DataSigChanNisRowStatus_Object = MibTableColumn
dataSigChanNisRowStatus = _DataSigChanNisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 1, 1, 1),
    _DataSigChanNisRowStatus_Type()
)
dataSigChanNisRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisRowStatus.setStatus("mandatory")
_DataSigChanNisComponentName_Type = DisplayString
_DataSigChanNisComponentName_Object = MibTableColumn
dataSigChanNisComponentName = _DataSigChanNisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 1, 1, 2),
    _DataSigChanNisComponentName_Type()
)
dataSigChanNisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisComponentName.setStatus("mandatory")
_DataSigChanNisStorageType_Type = StorageType
_DataSigChanNisStorageType_Object = MibTableColumn
dataSigChanNisStorageType = _DataSigChanNisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 1, 1, 4),
    _DataSigChanNisStorageType_Type()
)
dataSigChanNisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisStorageType.setStatus("mandatory")
_DataSigChanNisIndex_Type = NonReplicated
_DataSigChanNisIndex_Object = MibTableColumn
dataSigChanNisIndex = _DataSigChanNisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 1, 1, 10),
    _DataSigChanNisIndex_Type()
)
dataSigChanNisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanNisIndex.setStatus("mandatory")
_DataSigChanNisFramer_ObjectIdentity = ObjectIdentity
dataSigChanNisFramer = _DataSigChanNisFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2)
)
_DataSigChanNisFramerRowStatusTable_Object = MibTable
dataSigChanNisFramerRowStatusTable = _DataSigChanNisFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanNisFramerRowStatusTable.setStatus("mandatory")
_DataSigChanNisFramerRowStatusEntry_Object = MibTableRow
dataSigChanNisFramerRowStatusEntry = _DataSigChanNisFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 1, 1)
)
dataSigChanNisFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNisFramerRowStatusEntry.setStatus("mandatory")
_DataSigChanNisFramerRowStatus_Type = RowStatus
_DataSigChanNisFramerRowStatus_Object = MibTableColumn
dataSigChanNisFramerRowStatus = _DataSigChanNisFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 1, 1, 1),
    _DataSigChanNisFramerRowStatus_Type()
)
dataSigChanNisFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerRowStatus.setStatus("mandatory")
_DataSigChanNisFramerComponentName_Type = DisplayString
_DataSigChanNisFramerComponentName_Object = MibTableColumn
dataSigChanNisFramerComponentName = _DataSigChanNisFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 1, 1, 2),
    _DataSigChanNisFramerComponentName_Type()
)
dataSigChanNisFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerComponentName.setStatus("mandatory")
_DataSigChanNisFramerStorageType_Type = StorageType
_DataSigChanNisFramerStorageType_Object = MibTableColumn
dataSigChanNisFramerStorageType = _DataSigChanNisFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 1, 1, 4),
    _DataSigChanNisFramerStorageType_Type()
)
dataSigChanNisFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerStorageType.setStatus("mandatory")
_DataSigChanNisFramerIndex_Type = NonReplicated
_DataSigChanNisFramerIndex_Object = MibTableColumn
dataSigChanNisFramerIndex = _DataSigChanNisFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 1, 1, 10),
    _DataSigChanNisFramerIndex_Type()
)
dataSigChanNisFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanNisFramerIndex.setStatus("mandatory")
_DataSigChanNisFramerProvTable_Object = MibTable
dataSigChanNisFramerProvTable = _DataSigChanNisFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 10)
)
if mibBuilder.loadTexts:
    dataSigChanNisFramerProvTable.setStatus("mandatory")
_DataSigChanNisFramerProvEntry_Object = MibTableRow
dataSigChanNisFramerProvEntry = _DataSigChanNisFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 10, 1)
)
dataSigChanNisFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNisFramerProvEntry.setStatus("mandatory")
_DataSigChanNisFramerInterfaceName_Type = Link
_DataSigChanNisFramerInterfaceName_Object = MibTableColumn
dataSigChanNisFramerInterfaceName = _DataSigChanNisFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 10, 1, 1),
    _DataSigChanNisFramerInterfaceName_Type()
)
dataSigChanNisFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisFramerInterfaceName.setStatus("mandatory")
_DataSigChanNisFramerStateTable_Object = MibTable
dataSigChanNisFramerStateTable = _DataSigChanNisFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 12)
)
if mibBuilder.loadTexts:
    dataSigChanNisFramerStateTable.setStatus("mandatory")
_DataSigChanNisFramerStateEntry_Object = MibTableRow
dataSigChanNisFramerStateEntry = _DataSigChanNisFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 12, 1)
)
dataSigChanNisFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNisFramerStateEntry.setStatus("mandatory")


class _DataSigChanNisFramerAdminState_Type(Integer32):
    """Custom type dataSigChanNisFramerAdminState based on Integer32"""
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


_DataSigChanNisFramerAdminState_Type.__name__ = "Integer32"
_DataSigChanNisFramerAdminState_Object = MibTableColumn
dataSigChanNisFramerAdminState = _DataSigChanNisFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 12, 1, 1),
    _DataSigChanNisFramerAdminState_Type()
)
dataSigChanNisFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerAdminState.setStatus("mandatory")


class _DataSigChanNisFramerOperationalState_Type(Integer32):
    """Custom type dataSigChanNisFramerOperationalState based on Integer32"""
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


_DataSigChanNisFramerOperationalState_Type.__name__ = "Integer32"
_DataSigChanNisFramerOperationalState_Object = MibTableColumn
dataSigChanNisFramerOperationalState = _DataSigChanNisFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 12, 1, 2),
    _DataSigChanNisFramerOperationalState_Type()
)
dataSigChanNisFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerOperationalState.setStatus("mandatory")


class _DataSigChanNisFramerUsageState_Type(Integer32):
    """Custom type dataSigChanNisFramerUsageState based on Integer32"""
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


_DataSigChanNisFramerUsageState_Type.__name__ = "Integer32"
_DataSigChanNisFramerUsageState_Object = MibTableColumn
dataSigChanNisFramerUsageState = _DataSigChanNisFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 12, 1, 3),
    _DataSigChanNisFramerUsageState_Type()
)
dataSigChanNisFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerUsageState.setStatus("mandatory")
_DataSigChanNisFramerStatsTable_Object = MibTable
dataSigChanNisFramerStatsTable = _DataSigChanNisFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13)
)
if mibBuilder.loadTexts:
    dataSigChanNisFramerStatsTable.setStatus("mandatory")
_DataSigChanNisFramerStatsEntry_Object = MibTableRow
dataSigChanNisFramerStatsEntry = _DataSigChanNisFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1)
)
dataSigChanNisFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNisFramerStatsEntry.setStatus("mandatory")


class _DataSigChanNisFramerFrmToIf_Type(Unsigned32):
    """Custom type dataSigChanNisFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerFrmToIf_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerFrmToIf_Object = MibTableColumn
dataSigChanNisFramerFrmToIf = _DataSigChanNisFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 1),
    _DataSigChanNisFramerFrmToIf_Type()
)
dataSigChanNisFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerFrmToIf.setStatus("mandatory")


class _DataSigChanNisFramerFrmFromIf_Type(Unsigned32):
    """Custom type dataSigChanNisFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerFrmFromIf_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerFrmFromIf_Object = MibTableColumn
dataSigChanNisFramerFrmFromIf = _DataSigChanNisFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 2),
    _DataSigChanNisFramerFrmFromIf_Type()
)
dataSigChanNisFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerFrmFromIf.setStatus("mandatory")


class _DataSigChanNisFramerOctetFromIf_Type(Unsigned32):
    """Custom type dataSigChanNisFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerOctetFromIf_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerOctetFromIf_Object = MibTableColumn
dataSigChanNisFramerOctetFromIf = _DataSigChanNisFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 3),
    _DataSigChanNisFramerOctetFromIf_Type()
)
dataSigChanNisFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerOctetFromIf.setStatus("mandatory")


class _DataSigChanNisFramerAborts_Type(Unsigned32):
    """Custom type dataSigChanNisFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerAborts_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerAborts_Object = MibTableColumn
dataSigChanNisFramerAborts = _DataSigChanNisFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 4),
    _DataSigChanNisFramerAborts_Type()
)
dataSigChanNisFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerAborts.setStatus("mandatory")


class _DataSigChanNisFramerCrcErrors_Type(Unsigned32):
    """Custom type dataSigChanNisFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerCrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerCrcErrors_Object = MibTableColumn
dataSigChanNisFramerCrcErrors = _DataSigChanNisFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 5),
    _DataSigChanNisFramerCrcErrors_Type()
)
dataSigChanNisFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerCrcErrors.setStatus("mandatory")


class _DataSigChanNisFramerLrcErrors_Type(Unsigned32):
    """Custom type dataSigChanNisFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerLrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerLrcErrors_Object = MibTableColumn
dataSigChanNisFramerLrcErrors = _DataSigChanNisFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 6),
    _DataSigChanNisFramerLrcErrors_Type()
)
dataSigChanNisFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerLrcErrors.setStatus("mandatory")


class _DataSigChanNisFramerNonOctetErrors_Type(Unsigned32):
    """Custom type dataSigChanNisFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerNonOctetErrors_Object = MibTableColumn
dataSigChanNisFramerNonOctetErrors = _DataSigChanNisFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 7),
    _DataSigChanNisFramerNonOctetErrors_Type()
)
dataSigChanNisFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerNonOctetErrors.setStatus("mandatory")


class _DataSigChanNisFramerOverruns_Type(Unsigned32):
    """Custom type dataSigChanNisFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerOverruns_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerOverruns_Object = MibTableColumn
dataSigChanNisFramerOverruns = _DataSigChanNisFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 8),
    _DataSigChanNisFramerOverruns_Type()
)
dataSigChanNisFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerOverruns.setStatus("mandatory")


class _DataSigChanNisFramerUnderruns_Type(Unsigned32):
    """Custom type dataSigChanNisFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerUnderruns_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerUnderruns_Object = MibTableColumn
dataSigChanNisFramerUnderruns = _DataSigChanNisFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 9),
    _DataSigChanNisFramerUnderruns_Type()
)
dataSigChanNisFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerUnderruns.setStatus("mandatory")


class _DataSigChanNisFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type dataSigChanNisFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNisFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_DataSigChanNisFramerLargeFrmErrors_Object = MibTableColumn
dataSigChanNisFramerLargeFrmErrors = _DataSigChanNisFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 2, 13, 1, 10),
    _DataSigChanNisFramerLargeFrmErrors_Type()
)
dataSigChanNisFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisFramerLargeFrmErrors.setStatus("mandatory")
_DataSigChanNisL2Table_Object = MibTable
dataSigChanNisL2Table = _DataSigChanNisL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 11)
)
if mibBuilder.loadTexts:
    dataSigChanNisL2Table.setStatus("mandatory")
_DataSigChanNisL2Entry_Object = MibTableRow
dataSigChanNisL2Entry = _DataSigChanNisL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 11, 1)
)
dataSigChanNisL2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNisL2Entry.setStatus("mandatory")


class _DataSigChanNisT23_Type(Unsigned32):
    """Custom type dataSigChanNisT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DataSigChanNisT23_Type.__name__ = "Unsigned32"
_DataSigChanNisT23_Object = MibTableColumn
dataSigChanNisT23 = _DataSigChanNisT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 11, 1, 1),
    _DataSigChanNisT23_Type()
)
dataSigChanNisT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisT23.setStatus("mandatory")


class _DataSigChanNisT200_Type(Unsigned32):
    """Custom type dataSigChanNisT200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DataSigChanNisT200_Type.__name__ = "Unsigned32"
_DataSigChanNisT200_Object = MibTableColumn
dataSigChanNisT200 = _DataSigChanNisT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 11, 1, 2),
    _DataSigChanNisT200_Type()
)
dataSigChanNisT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisT200.setStatus("mandatory")


class _DataSigChanNisN200_Type(Unsigned32):
    """Custom type dataSigChanNisN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DataSigChanNisN200_Type.__name__ = "Unsigned32"
_DataSigChanNisN200_Object = MibTableColumn
dataSigChanNisN200 = _DataSigChanNisN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 11, 1, 3),
    _DataSigChanNisN200_Type()
)
dataSigChanNisN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisN200.setStatus("mandatory")


class _DataSigChanNisT203_Type(Unsigned32):
    """Custom type dataSigChanNisT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_DataSigChanNisT203_Type.__name__ = "Unsigned32"
_DataSigChanNisT203_Object = MibTableColumn
dataSigChanNisT203 = _DataSigChanNisT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 11, 1, 4),
    _DataSigChanNisT203_Type()
)
dataSigChanNisT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisT203.setStatus("mandatory")


class _DataSigChanNisN201_Type(Unsigned32):
    """Custom type dataSigChanNisN201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_DataSigChanNisN201_Type.__name__ = "Unsigned32"
_DataSigChanNisN201_Object = MibTableColumn
dataSigChanNisN201 = _DataSigChanNisN201_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 11, 1, 5),
    _DataSigChanNisN201_Type()
)
dataSigChanNisN201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisN201.setStatus("mandatory")


class _DataSigChanNisCircuitSwitchedK_Type(Unsigned32):
    """Custom type dataSigChanNisCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_DataSigChanNisCircuitSwitchedK_Type.__name__ = "Unsigned32"
_DataSigChanNisCircuitSwitchedK_Object = MibTableColumn
dataSigChanNisCircuitSwitchedK = _DataSigChanNisCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 11, 1, 6),
    _DataSigChanNisCircuitSwitchedK_Type()
)
dataSigChanNisCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisCircuitSwitchedK.setStatus("mandatory")
_DataSigChanNisProvTable_Object = MibTable
dataSigChanNisProvTable = _DataSigChanNisProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 13)
)
if mibBuilder.loadTexts:
    dataSigChanNisProvTable.setStatus("mandatory")
_DataSigChanNisProvEntry_Object = MibTableRow
dataSigChanNisProvEntry = _DataSigChanNisProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 13, 1)
)
dataSigChanNisProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNisProvEntry.setStatus("mandatory")


class _DataSigChanNisSide_Type(Integer32):
    """Custom type dataSigChanNisSide based on Integer32"""
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


_DataSigChanNisSide_Type.__name__ = "Integer32"
_DataSigChanNisSide_Object = MibTableColumn
dataSigChanNisSide = _DataSigChanNisSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 13, 1, 1),
    _DataSigChanNisSide_Type()
)
dataSigChanNisSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisSide.setStatus("mandatory")
_DataSigChanNisOperTable_Object = MibTable
dataSigChanNisOperTable = _DataSigChanNisOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 15)
)
if mibBuilder.loadTexts:
    dataSigChanNisOperTable.setStatus("mandatory")
_DataSigChanNisOperEntry_Object = MibTableRow
dataSigChanNisOperEntry = _DataSigChanNisOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 15, 1)
)
dataSigChanNisOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNisOperEntry.setStatus("mandatory")


class _DataSigChanNisActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanNisActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanNisActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanNisActiveChannels_Object = MibTableColumn
dataSigChanNisActiveChannels = _DataSigChanNisActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 15, 1, 1),
    _DataSigChanNisActiveChannels_Type()
)
dataSigChanNisActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisActiveChannels.setStatus("mandatory")


class _DataSigChanNisPeakActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanNisPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanNisPeakActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanNisPeakActiveChannels_Object = MibTableColumn
dataSigChanNisPeakActiveChannels = _DataSigChanNisPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 15, 1, 4),
    _DataSigChanNisPeakActiveChannels_Type()
)
dataSigChanNisPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisPeakActiveChannels.setStatus("mandatory")


class _DataSigChanNisDChanStatus_Type(Integer32):
    """Custom type dataSigChanNisDChanStatus based on Integer32"""
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


_DataSigChanNisDChanStatus_Type.__name__ = "Integer32"
_DataSigChanNisDChanStatus_Object = MibTableColumn
dataSigChanNisDChanStatus = _DataSigChanNisDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 15, 1, 7),
    _DataSigChanNisDChanStatus_Type()
)
dataSigChanNisDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNisDChanStatus.setStatus("mandatory")
_DataSigChanNisToolsTable_Object = MibTable
dataSigChanNisToolsTable = _DataSigChanNisToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 16)
)
if mibBuilder.loadTexts:
    dataSigChanNisToolsTable.setStatus("mandatory")
_DataSigChanNisToolsEntry_Object = MibTableRow
dataSigChanNisToolsEntry = _DataSigChanNisToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 16, 1)
)
dataSigChanNisToolsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNISMIB", "dataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNisToolsEntry.setStatus("mandatory")


class _DataSigChanNisTracing_Type(OctetString):
    """Custom type dataSigChanNisTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DataSigChanNisTracing_Type.__name__ = "OctetString"
_DataSigChanNisTracing_Object = MibTableColumn
dataSigChanNisTracing = _DataSigChanNisTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 13, 16, 1, 1),
    _DataSigChanNisTracing_Type()
)
dataSigChanNisTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNisTracing.setStatus("mandatory")
_DisdnNISMIB_ObjectIdentity = ObjectIdentity
disdnNISMIB = _DisdnNISMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 127)
)
_DisdnNISGroup_ObjectIdentity = ObjectIdentity
disdnNISGroup = _DisdnNISGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 127, 1)
)
_DisdnNISGroupBE_ObjectIdentity = ObjectIdentity
disdnNISGroupBE = _DisdnNISGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 127, 1, 5)
)
_DisdnNISGroupBE00_ObjectIdentity = ObjectIdentity
disdnNISGroupBE00 = _DisdnNISGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 127, 1, 5, 1)
)
_DisdnNISGroupBE00A_ObjectIdentity = ObjectIdentity
disdnNISGroupBE00A = _DisdnNISGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 127, 1, 5, 1, 2)
)
_DisdnNISCapabilities_ObjectIdentity = ObjectIdentity
disdnNISCapabilities = _DisdnNISCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 127, 3)
)
_DisdnNISCapabilitiesBE_ObjectIdentity = ObjectIdentity
disdnNISCapabilitiesBE = _DisdnNISCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 127, 3, 5)
)
_DisdnNISCapabilitiesBE00_ObjectIdentity = ObjectIdentity
disdnNISCapabilitiesBE00 = _DisdnNISCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 127, 3, 5, 1)
)
_DisdnNISCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
disdnNISCapabilitiesBE00A = _DisdnNISCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 127, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DisdnNISMIB",
    **{"dataSigChanNis": dataSigChanNis,
       "dataSigChanNisRowStatusTable": dataSigChanNisRowStatusTable,
       "dataSigChanNisRowStatusEntry": dataSigChanNisRowStatusEntry,
       "dataSigChanNisRowStatus": dataSigChanNisRowStatus,
       "dataSigChanNisComponentName": dataSigChanNisComponentName,
       "dataSigChanNisStorageType": dataSigChanNisStorageType,
       "dataSigChanNisIndex": dataSigChanNisIndex,
       "dataSigChanNisFramer": dataSigChanNisFramer,
       "dataSigChanNisFramerRowStatusTable": dataSigChanNisFramerRowStatusTable,
       "dataSigChanNisFramerRowStatusEntry": dataSigChanNisFramerRowStatusEntry,
       "dataSigChanNisFramerRowStatus": dataSigChanNisFramerRowStatus,
       "dataSigChanNisFramerComponentName": dataSigChanNisFramerComponentName,
       "dataSigChanNisFramerStorageType": dataSigChanNisFramerStorageType,
       "dataSigChanNisFramerIndex": dataSigChanNisFramerIndex,
       "dataSigChanNisFramerProvTable": dataSigChanNisFramerProvTable,
       "dataSigChanNisFramerProvEntry": dataSigChanNisFramerProvEntry,
       "dataSigChanNisFramerInterfaceName": dataSigChanNisFramerInterfaceName,
       "dataSigChanNisFramerStateTable": dataSigChanNisFramerStateTable,
       "dataSigChanNisFramerStateEntry": dataSigChanNisFramerStateEntry,
       "dataSigChanNisFramerAdminState": dataSigChanNisFramerAdminState,
       "dataSigChanNisFramerOperationalState": dataSigChanNisFramerOperationalState,
       "dataSigChanNisFramerUsageState": dataSigChanNisFramerUsageState,
       "dataSigChanNisFramerStatsTable": dataSigChanNisFramerStatsTable,
       "dataSigChanNisFramerStatsEntry": dataSigChanNisFramerStatsEntry,
       "dataSigChanNisFramerFrmToIf": dataSigChanNisFramerFrmToIf,
       "dataSigChanNisFramerFrmFromIf": dataSigChanNisFramerFrmFromIf,
       "dataSigChanNisFramerOctetFromIf": dataSigChanNisFramerOctetFromIf,
       "dataSigChanNisFramerAborts": dataSigChanNisFramerAborts,
       "dataSigChanNisFramerCrcErrors": dataSigChanNisFramerCrcErrors,
       "dataSigChanNisFramerLrcErrors": dataSigChanNisFramerLrcErrors,
       "dataSigChanNisFramerNonOctetErrors": dataSigChanNisFramerNonOctetErrors,
       "dataSigChanNisFramerOverruns": dataSigChanNisFramerOverruns,
       "dataSigChanNisFramerUnderruns": dataSigChanNisFramerUnderruns,
       "dataSigChanNisFramerLargeFrmErrors": dataSigChanNisFramerLargeFrmErrors,
       "dataSigChanNisL2Table": dataSigChanNisL2Table,
       "dataSigChanNisL2Entry": dataSigChanNisL2Entry,
       "dataSigChanNisT23": dataSigChanNisT23,
       "dataSigChanNisT200": dataSigChanNisT200,
       "dataSigChanNisN200": dataSigChanNisN200,
       "dataSigChanNisT203": dataSigChanNisT203,
       "dataSigChanNisN201": dataSigChanNisN201,
       "dataSigChanNisCircuitSwitchedK": dataSigChanNisCircuitSwitchedK,
       "dataSigChanNisProvTable": dataSigChanNisProvTable,
       "dataSigChanNisProvEntry": dataSigChanNisProvEntry,
       "dataSigChanNisSide": dataSigChanNisSide,
       "dataSigChanNisOperTable": dataSigChanNisOperTable,
       "dataSigChanNisOperEntry": dataSigChanNisOperEntry,
       "dataSigChanNisActiveChannels": dataSigChanNisActiveChannels,
       "dataSigChanNisPeakActiveChannels": dataSigChanNisPeakActiveChannels,
       "dataSigChanNisDChanStatus": dataSigChanNisDChanStatus,
       "dataSigChanNisToolsTable": dataSigChanNisToolsTable,
       "dataSigChanNisToolsEntry": dataSigChanNisToolsEntry,
       "dataSigChanNisTracing": dataSigChanNisTracing,
       "disdnNISMIB": disdnNISMIB,
       "disdnNISGroup": disdnNISGroup,
       "disdnNISGroupBE": disdnNISGroupBE,
       "disdnNISGroupBE00": disdnNISGroupBE00,
       "disdnNISGroupBE00A": disdnNISGroupBE00A,
       "disdnNISCapabilities": disdnNISCapabilities,
       "disdnNISCapabilitiesBE": disdnNISCapabilitiesBE,
       "disdnNISCapabilitiesBE00": disdnNISCapabilitiesBE00,
       "disdnNISCapabilitiesBE00A": disdnNISCapabilitiesBE00A}
)
