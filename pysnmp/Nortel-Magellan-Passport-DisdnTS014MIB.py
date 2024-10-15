# SNMP MIB module (Nortel-Magellan-Passport-DisdnTS014MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DisdnTS014MIB
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

_DataSigChanTS014_ObjectIdentity = ObjectIdentity
dataSigChanTS014 = _DataSigChanTS014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9)
)
_DataSigChanTS014RowStatusTable_Object = MibTable
dataSigChanTS014RowStatusTable = _DataSigChanTS014RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 1)
)
if mibBuilder.loadTexts:
    dataSigChanTS014RowStatusTable.setStatus("mandatory")
_DataSigChanTS014RowStatusEntry_Object = MibTableRow
dataSigChanTS014RowStatusEntry = _DataSigChanTS014RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 1, 1)
)
dataSigChanTS014RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    dataSigChanTS014RowStatusEntry.setStatus("mandatory")
_DataSigChanTS014RowStatus_Type = RowStatus
_DataSigChanTS014RowStatus_Object = MibTableColumn
dataSigChanTS014RowStatus = _DataSigChanTS014RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 1, 1, 1),
    _DataSigChanTS014RowStatus_Type()
)
dataSigChanTS014RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014RowStatus.setStatus("mandatory")
_DataSigChanTS014ComponentName_Type = DisplayString
_DataSigChanTS014ComponentName_Object = MibTableColumn
dataSigChanTS014ComponentName = _DataSigChanTS014ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 1, 1, 2),
    _DataSigChanTS014ComponentName_Type()
)
dataSigChanTS014ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014ComponentName.setStatus("mandatory")
_DataSigChanTS014StorageType_Type = StorageType
_DataSigChanTS014StorageType_Object = MibTableColumn
dataSigChanTS014StorageType = _DataSigChanTS014StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 1, 1, 4),
    _DataSigChanTS014StorageType_Type()
)
dataSigChanTS014StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014StorageType.setStatus("mandatory")
_DataSigChanTS014Index_Type = NonReplicated
_DataSigChanTS014Index_Object = MibTableColumn
dataSigChanTS014Index = _DataSigChanTS014Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 1, 1, 10),
    _DataSigChanTS014Index_Type()
)
dataSigChanTS014Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanTS014Index.setStatus("mandatory")
_DataSigChanTS014Framer_ObjectIdentity = ObjectIdentity
dataSigChanTS014Framer = _DataSigChanTS014Framer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2)
)
_DataSigChanTS014FramerRowStatusTable_Object = MibTable
dataSigChanTS014FramerRowStatusTable = _DataSigChanTS014FramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanTS014FramerRowStatusTable.setStatus("mandatory")
_DataSigChanTS014FramerRowStatusEntry_Object = MibTableRow
dataSigChanTS014FramerRowStatusEntry = _DataSigChanTS014FramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 1, 1)
)
dataSigChanTS014FramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014Index"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014FramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanTS014FramerRowStatusEntry.setStatus("mandatory")
_DataSigChanTS014FramerRowStatus_Type = RowStatus
_DataSigChanTS014FramerRowStatus_Object = MibTableColumn
dataSigChanTS014FramerRowStatus = _DataSigChanTS014FramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 1, 1, 1),
    _DataSigChanTS014FramerRowStatus_Type()
)
dataSigChanTS014FramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerRowStatus.setStatus("mandatory")
_DataSigChanTS014FramerComponentName_Type = DisplayString
_DataSigChanTS014FramerComponentName_Object = MibTableColumn
dataSigChanTS014FramerComponentName = _DataSigChanTS014FramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 1, 1, 2),
    _DataSigChanTS014FramerComponentName_Type()
)
dataSigChanTS014FramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerComponentName.setStatus("mandatory")
_DataSigChanTS014FramerStorageType_Type = StorageType
_DataSigChanTS014FramerStorageType_Object = MibTableColumn
dataSigChanTS014FramerStorageType = _DataSigChanTS014FramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 1, 1, 4),
    _DataSigChanTS014FramerStorageType_Type()
)
dataSigChanTS014FramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerStorageType.setStatus("mandatory")
_DataSigChanTS014FramerIndex_Type = NonReplicated
_DataSigChanTS014FramerIndex_Object = MibTableColumn
dataSigChanTS014FramerIndex = _DataSigChanTS014FramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 1, 1, 10),
    _DataSigChanTS014FramerIndex_Type()
)
dataSigChanTS014FramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerIndex.setStatus("mandatory")
_DataSigChanTS014FramerProvTable_Object = MibTable
dataSigChanTS014FramerProvTable = _DataSigChanTS014FramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 10)
)
if mibBuilder.loadTexts:
    dataSigChanTS014FramerProvTable.setStatus("mandatory")
_DataSigChanTS014FramerProvEntry_Object = MibTableRow
dataSigChanTS014FramerProvEntry = _DataSigChanTS014FramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 10, 1)
)
dataSigChanTS014FramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014Index"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014FramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanTS014FramerProvEntry.setStatus("mandatory")
_DataSigChanTS014FramerInterfaceName_Type = Link
_DataSigChanTS014FramerInterfaceName_Object = MibTableColumn
dataSigChanTS014FramerInterfaceName = _DataSigChanTS014FramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 10, 1, 1),
    _DataSigChanTS014FramerInterfaceName_Type()
)
dataSigChanTS014FramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerInterfaceName.setStatus("mandatory")
_DataSigChanTS014FramerStateTable_Object = MibTable
dataSigChanTS014FramerStateTable = _DataSigChanTS014FramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 12)
)
if mibBuilder.loadTexts:
    dataSigChanTS014FramerStateTable.setStatus("mandatory")
_DataSigChanTS014FramerStateEntry_Object = MibTableRow
dataSigChanTS014FramerStateEntry = _DataSigChanTS014FramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 12, 1)
)
dataSigChanTS014FramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014Index"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014FramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanTS014FramerStateEntry.setStatus("mandatory")


class _DataSigChanTS014FramerAdminState_Type(Integer32):
    """Custom type dataSigChanTS014FramerAdminState based on Integer32"""
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


_DataSigChanTS014FramerAdminState_Type.__name__ = "Integer32"
_DataSigChanTS014FramerAdminState_Object = MibTableColumn
dataSigChanTS014FramerAdminState = _DataSigChanTS014FramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 12, 1, 1),
    _DataSigChanTS014FramerAdminState_Type()
)
dataSigChanTS014FramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerAdminState.setStatus("mandatory")


class _DataSigChanTS014FramerOperationalState_Type(Integer32):
    """Custom type dataSigChanTS014FramerOperationalState based on Integer32"""
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


_DataSigChanTS014FramerOperationalState_Type.__name__ = "Integer32"
_DataSigChanTS014FramerOperationalState_Object = MibTableColumn
dataSigChanTS014FramerOperationalState = _DataSigChanTS014FramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 12, 1, 2),
    _DataSigChanTS014FramerOperationalState_Type()
)
dataSigChanTS014FramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerOperationalState.setStatus("mandatory")


class _DataSigChanTS014FramerUsageState_Type(Integer32):
    """Custom type dataSigChanTS014FramerUsageState based on Integer32"""
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


_DataSigChanTS014FramerUsageState_Type.__name__ = "Integer32"
_DataSigChanTS014FramerUsageState_Object = MibTableColumn
dataSigChanTS014FramerUsageState = _DataSigChanTS014FramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 12, 1, 3),
    _DataSigChanTS014FramerUsageState_Type()
)
dataSigChanTS014FramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerUsageState.setStatus("mandatory")
_DataSigChanTS014FramerStatsTable_Object = MibTable
dataSigChanTS014FramerStatsTable = _DataSigChanTS014FramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13)
)
if mibBuilder.loadTexts:
    dataSigChanTS014FramerStatsTable.setStatus("mandatory")
_DataSigChanTS014FramerStatsEntry_Object = MibTableRow
dataSigChanTS014FramerStatsEntry = _DataSigChanTS014FramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1)
)
dataSigChanTS014FramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014Index"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014FramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanTS014FramerStatsEntry.setStatus("mandatory")


class _DataSigChanTS014FramerFrmToIf_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerFrmToIf_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerFrmToIf_Object = MibTableColumn
dataSigChanTS014FramerFrmToIf = _DataSigChanTS014FramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 1),
    _DataSigChanTS014FramerFrmToIf_Type()
)
dataSigChanTS014FramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerFrmToIf.setStatus("mandatory")


class _DataSigChanTS014FramerFrmFromIf_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerFrmFromIf_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerFrmFromIf_Object = MibTableColumn
dataSigChanTS014FramerFrmFromIf = _DataSigChanTS014FramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 2),
    _DataSigChanTS014FramerFrmFromIf_Type()
)
dataSigChanTS014FramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerFrmFromIf.setStatus("mandatory")


class _DataSigChanTS014FramerOctetFromIf_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerOctetFromIf_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerOctetFromIf_Object = MibTableColumn
dataSigChanTS014FramerOctetFromIf = _DataSigChanTS014FramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 3),
    _DataSigChanTS014FramerOctetFromIf_Type()
)
dataSigChanTS014FramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerOctetFromIf.setStatus("mandatory")


class _DataSigChanTS014FramerAborts_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerAborts_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerAborts_Object = MibTableColumn
dataSigChanTS014FramerAborts = _DataSigChanTS014FramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 4),
    _DataSigChanTS014FramerAborts_Type()
)
dataSigChanTS014FramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerAborts.setStatus("mandatory")


class _DataSigChanTS014FramerCrcErrors_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerCrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerCrcErrors_Object = MibTableColumn
dataSigChanTS014FramerCrcErrors = _DataSigChanTS014FramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 5),
    _DataSigChanTS014FramerCrcErrors_Type()
)
dataSigChanTS014FramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerCrcErrors.setStatus("mandatory")


class _DataSigChanTS014FramerLrcErrors_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerLrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerLrcErrors_Object = MibTableColumn
dataSigChanTS014FramerLrcErrors = _DataSigChanTS014FramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 6),
    _DataSigChanTS014FramerLrcErrors_Type()
)
dataSigChanTS014FramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerLrcErrors.setStatus("mandatory")


class _DataSigChanTS014FramerNonOctetErrors_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerNonOctetErrors_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerNonOctetErrors_Object = MibTableColumn
dataSigChanTS014FramerNonOctetErrors = _DataSigChanTS014FramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 7),
    _DataSigChanTS014FramerNonOctetErrors_Type()
)
dataSigChanTS014FramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerNonOctetErrors.setStatus("mandatory")


class _DataSigChanTS014FramerOverruns_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerOverruns_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerOverruns_Object = MibTableColumn
dataSigChanTS014FramerOverruns = _DataSigChanTS014FramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 8),
    _DataSigChanTS014FramerOverruns_Type()
)
dataSigChanTS014FramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerOverruns.setStatus("mandatory")


class _DataSigChanTS014FramerUnderruns_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerUnderruns_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerUnderruns_Object = MibTableColumn
dataSigChanTS014FramerUnderruns = _DataSigChanTS014FramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 9),
    _DataSigChanTS014FramerUnderruns_Type()
)
dataSigChanTS014FramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerUnderruns.setStatus("mandatory")


class _DataSigChanTS014FramerLargeFrmErrors_Type(Unsigned32):
    """Custom type dataSigChanTS014FramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanTS014FramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_DataSigChanTS014FramerLargeFrmErrors_Object = MibTableColumn
dataSigChanTS014FramerLargeFrmErrors = _DataSigChanTS014FramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 2, 13, 1, 10),
    _DataSigChanTS014FramerLargeFrmErrors_Type()
)
dataSigChanTS014FramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014FramerLargeFrmErrors.setStatus("mandatory")
_DataSigChanTS014L2Table_Object = MibTable
dataSigChanTS014L2Table = _DataSigChanTS014L2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 11)
)
if mibBuilder.loadTexts:
    dataSigChanTS014L2Table.setStatus("mandatory")
_DataSigChanTS014L2Entry_Object = MibTableRow
dataSigChanTS014L2Entry = _DataSigChanTS014L2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 11, 1)
)
dataSigChanTS014L2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    dataSigChanTS014L2Entry.setStatus("mandatory")


class _DataSigChanTS014T23_Type(Unsigned32):
    """Custom type dataSigChanTS014T23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DataSigChanTS014T23_Type.__name__ = "Unsigned32"
_DataSigChanTS014T23_Object = MibTableColumn
dataSigChanTS014T23 = _DataSigChanTS014T23_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 11, 1, 1),
    _DataSigChanTS014T23_Type()
)
dataSigChanTS014T23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014T23.setStatus("mandatory")


class _DataSigChanTS014T200_Type(Unsigned32):
    """Custom type dataSigChanTS014T200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DataSigChanTS014T200_Type.__name__ = "Unsigned32"
_DataSigChanTS014T200_Object = MibTableColumn
dataSigChanTS014T200 = _DataSigChanTS014T200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 11, 1, 2),
    _DataSigChanTS014T200_Type()
)
dataSigChanTS014T200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014T200.setStatus("mandatory")


class _DataSigChanTS014N200_Type(Unsigned32):
    """Custom type dataSigChanTS014N200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DataSigChanTS014N200_Type.__name__ = "Unsigned32"
_DataSigChanTS014N200_Object = MibTableColumn
dataSigChanTS014N200 = _DataSigChanTS014N200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 11, 1, 3),
    _DataSigChanTS014N200_Type()
)
dataSigChanTS014N200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014N200.setStatus("mandatory")


class _DataSigChanTS014T203_Type(Unsigned32):
    """Custom type dataSigChanTS014T203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_DataSigChanTS014T203_Type.__name__ = "Unsigned32"
_DataSigChanTS014T203_Object = MibTableColumn
dataSigChanTS014T203 = _DataSigChanTS014T203_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 11, 1, 4),
    _DataSigChanTS014T203_Type()
)
dataSigChanTS014T203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014T203.setStatus("mandatory")


class _DataSigChanTS014N201_Type(Unsigned32):
    """Custom type dataSigChanTS014N201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_DataSigChanTS014N201_Type.__name__ = "Unsigned32"
_DataSigChanTS014N201_Object = MibTableColumn
dataSigChanTS014N201 = _DataSigChanTS014N201_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 11, 1, 5),
    _DataSigChanTS014N201_Type()
)
dataSigChanTS014N201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014N201.setStatus("mandatory")


class _DataSigChanTS014CircuitSwitchedK_Type(Unsigned32):
    """Custom type dataSigChanTS014CircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_DataSigChanTS014CircuitSwitchedK_Type.__name__ = "Unsigned32"
_DataSigChanTS014CircuitSwitchedK_Object = MibTableColumn
dataSigChanTS014CircuitSwitchedK = _DataSigChanTS014CircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 11, 1, 6),
    _DataSigChanTS014CircuitSwitchedK_Type()
)
dataSigChanTS014CircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014CircuitSwitchedK.setStatus("mandatory")
_DataSigChanTS014ProvTable_Object = MibTable
dataSigChanTS014ProvTable = _DataSigChanTS014ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 13)
)
if mibBuilder.loadTexts:
    dataSigChanTS014ProvTable.setStatus("mandatory")
_DataSigChanTS014ProvEntry_Object = MibTableRow
dataSigChanTS014ProvEntry = _DataSigChanTS014ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 13, 1)
)
dataSigChanTS014ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    dataSigChanTS014ProvEntry.setStatus("mandatory")


class _DataSigChanTS014Side_Type(Integer32):
    """Custom type dataSigChanTS014Side based on Integer32"""
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


_DataSigChanTS014Side_Type.__name__ = "Integer32"
_DataSigChanTS014Side_Object = MibTableColumn
dataSigChanTS014Side = _DataSigChanTS014Side_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 13, 1, 1),
    _DataSigChanTS014Side_Type()
)
dataSigChanTS014Side.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014Side.setStatus("mandatory")
_DataSigChanTS014OperTable_Object = MibTable
dataSigChanTS014OperTable = _DataSigChanTS014OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 15)
)
if mibBuilder.loadTexts:
    dataSigChanTS014OperTable.setStatus("mandatory")
_DataSigChanTS014OperEntry_Object = MibTableRow
dataSigChanTS014OperEntry = _DataSigChanTS014OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 15, 1)
)
dataSigChanTS014OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    dataSigChanTS014OperEntry.setStatus("mandatory")


class _DataSigChanTS014ActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanTS014ActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanTS014ActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanTS014ActiveChannels_Object = MibTableColumn
dataSigChanTS014ActiveChannels = _DataSigChanTS014ActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 15, 1, 1),
    _DataSigChanTS014ActiveChannels_Type()
)
dataSigChanTS014ActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014ActiveChannels.setStatus("mandatory")


class _DataSigChanTS014PeakActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanTS014PeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanTS014PeakActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanTS014PeakActiveChannels_Object = MibTableColumn
dataSigChanTS014PeakActiveChannels = _DataSigChanTS014PeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 15, 1, 4),
    _DataSigChanTS014PeakActiveChannels_Type()
)
dataSigChanTS014PeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014PeakActiveChannels.setStatus("mandatory")


class _DataSigChanTS014DChanStatus_Type(Integer32):
    """Custom type dataSigChanTS014DChanStatus based on Integer32"""
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


_DataSigChanTS014DChanStatus_Type.__name__ = "Integer32"
_DataSigChanTS014DChanStatus_Object = MibTableColumn
dataSigChanTS014DChanStatus = _DataSigChanTS014DChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 15, 1, 7),
    _DataSigChanTS014DChanStatus_Type()
)
dataSigChanTS014DChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanTS014DChanStatus.setStatus("mandatory")
_DataSigChanTS014ToolsTable_Object = MibTable
dataSigChanTS014ToolsTable = _DataSigChanTS014ToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 16)
)
if mibBuilder.loadTexts:
    dataSigChanTS014ToolsTable.setStatus("mandatory")
_DataSigChanTS014ToolsEntry_Object = MibTableRow
dataSigChanTS014ToolsEntry = _DataSigChanTS014ToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 16, 1)
)
dataSigChanTS014ToolsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnTS014MIB", "dataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    dataSigChanTS014ToolsEntry.setStatus("mandatory")


class _DataSigChanTS014Tracing_Type(OctetString):
    """Custom type dataSigChanTS014Tracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DataSigChanTS014Tracing_Type.__name__ = "OctetString"
_DataSigChanTS014Tracing_Object = MibTableColumn
dataSigChanTS014Tracing = _DataSigChanTS014Tracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 9, 16, 1, 1),
    _DataSigChanTS014Tracing_Type()
)
dataSigChanTS014Tracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanTS014Tracing.setStatus("mandatory")
_DisdnTS014MIB_ObjectIdentity = ObjectIdentity
disdnTS014MIB = _DisdnTS014MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 114)
)
_DisdnTS014Group_ObjectIdentity = ObjectIdentity
disdnTS014Group = _DisdnTS014Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 114, 1)
)
_DisdnTS014GroupBE_ObjectIdentity = ObjectIdentity
disdnTS014GroupBE = _DisdnTS014GroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 114, 1, 5)
)
_DisdnTS014GroupBE00_ObjectIdentity = ObjectIdentity
disdnTS014GroupBE00 = _DisdnTS014GroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 114, 1, 5, 1)
)
_DisdnTS014GroupBE00A_ObjectIdentity = ObjectIdentity
disdnTS014GroupBE00A = _DisdnTS014GroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 114, 1, 5, 1, 2)
)
_DisdnTS014Capabilities_ObjectIdentity = ObjectIdentity
disdnTS014Capabilities = _DisdnTS014Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 114, 3)
)
_DisdnTS014CapabilitiesBE_ObjectIdentity = ObjectIdentity
disdnTS014CapabilitiesBE = _DisdnTS014CapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 114, 3, 5)
)
_DisdnTS014CapabilitiesBE00_ObjectIdentity = ObjectIdentity
disdnTS014CapabilitiesBE00 = _DisdnTS014CapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 114, 3, 5, 1)
)
_DisdnTS014CapabilitiesBE00A_ObjectIdentity = ObjectIdentity
disdnTS014CapabilitiesBE00A = _DisdnTS014CapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 114, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DisdnTS014MIB",
    **{"dataSigChanTS014": dataSigChanTS014,
       "dataSigChanTS014RowStatusTable": dataSigChanTS014RowStatusTable,
       "dataSigChanTS014RowStatusEntry": dataSigChanTS014RowStatusEntry,
       "dataSigChanTS014RowStatus": dataSigChanTS014RowStatus,
       "dataSigChanTS014ComponentName": dataSigChanTS014ComponentName,
       "dataSigChanTS014StorageType": dataSigChanTS014StorageType,
       "dataSigChanTS014Index": dataSigChanTS014Index,
       "dataSigChanTS014Framer": dataSigChanTS014Framer,
       "dataSigChanTS014FramerRowStatusTable": dataSigChanTS014FramerRowStatusTable,
       "dataSigChanTS014FramerRowStatusEntry": dataSigChanTS014FramerRowStatusEntry,
       "dataSigChanTS014FramerRowStatus": dataSigChanTS014FramerRowStatus,
       "dataSigChanTS014FramerComponentName": dataSigChanTS014FramerComponentName,
       "dataSigChanTS014FramerStorageType": dataSigChanTS014FramerStorageType,
       "dataSigChanTS014FramerIndex": dataSigChanTS014FramerIndex,
       "dataSigChanTS014FramerProvTable": dataSigChanTS014FramerProvTable,
       "dataSigChanTS014FramerProvEntry": dataSigChanTS014FramerProvEntry,
       "dataSigChanTS014FramerInterfaceName": dataSigChanTS014FramerInterfaceName,
       "dataSigChanTS014FramerStateTable": dataSigChanTS014FramerStateTable,
       "dataSigChanTS014FramerStateEntry": dataSigChanTS014FramerStateEntry,
       "dataSigChanTS014FramerAdminState": dataSigChanTS014FramerAdminState,
       "dataSigChanTS014FramerOperationalState": dataSigChanTS014FramerOperationalState,
       "dataSigChanTS014FramerUsageState": dataSigChanTS014FramerUsageState,
       "dataSigChanTS014FramerStatsTable": dataSigChanTS014FramerStatsTable,
       "dataSigChanTS014FramerStatsEntry": dataSigChanTS014FramerStatsEntry,
       "dataSigChanTS014FramerFrmToIf": dataSigChanTS014FramerFrmToIf,
       "dataSigChanTS014FramerFrmFromIf": dataSigChanTS014FramerFrmFromIf,
       "dataSigChanTS014FramerOctetFromIf": dataSigChanTS014FramerOctetFromIf,
       "dataSigChanTS014FramerAborts": dataSigChanTS014FramerAborts,
       "dataSigChanTS014FramerCrcErrors": dataSigChanTS014FramerCrcErrors,
       "dataSigChanTS014FramerLrcErrors": dataSigChanTS014FramerLrcErrors,
       "dataSigChanTS014FramerNonOctetErrors": dataSigChanTS014FramerNonOctetErrors,
       "dataSigChanTS014FramerOverruns": dataSigChanTS014FramerOverruns,
       "dataSigChanTS014FramerUnderruns": dataSigChanTS014FramerUnderruns,
       "dataSigChanTS014FramerLargeFrmErrors": dataSigChanTS014FramerLargeFrmErrors,
       "dataSigChanTS014L2Table": dataSigChanTS014L2Table,
       "dataSigChanTS014L2Entry": dataSigChanTS014L2Entry,
       "dataSigChanTS014T23": dataSigChanTS014T23,
       "dataSigChanTS014T200": dataSigChanTS014T200,
       "dataSigChanTS014N200": dataSigChanTS014N200,
       "dataSigChanTS014T203": dataSigChanTS014T203,
       "dataSigChanTS014N201": dataSigChanTS014N201,
       "dataSigChanTS014CircuitSwitchedK": dataSigChanTS014CircuitSwitchedK,
       "dataSigChanTS014ProvTable": dataSigChanTS014ProvTable,
       "dataSigChanTS014ProvEntry": dataSigChanTS014ProvEntry,
       "dataSigChanTS014Side": dataSigChanTS014Side,
       "dataSigChanTS014OperTable": dataSigChanTS014OperTable,
       "dataSigChanTS014OperEntry": dataSigChanTS014OperEntry,
       "dataSigChanTS014ActiveChannels": dataSigChanTS014ActiveChannels,
       "dataSigChanTS014PeakActiveChannels": dataSigChanTS014PeakActiveChannels,
       "dataSigChanTS014DChanStatus": dataSigChanTS014DChanStatus,
       "dataSigChanTS014ToolsTable": dataSigChanTS014ToolsTable,
       "dataSigChanTS014ToolsEntry": dataSigChanTS014ToolsEntry,
       "dataSigChanTS014Tracing": dataSigChanTS014Tracing,
       "disdnTS014MIB": disdnTS014MIB,
       "disdnTS014Group": disdnTS014Group,
       "disdnTS014GroupBE": disdnTS014GroupBE,
       "disdnTS014GroupBE00": disdnTS014GroupBE00,
       "disdnTS014GroupBE00A": disdnTS014GroupBE00A,
       "disdnTS014Capabilities": disdnTS014Capabilities,
       "disdnTS014CapabilitiesBE": disdnTS014CapabilitiesBE,
       "disdnTS014CapabilitiesBE00": disdnTS014CapabilitiesBE00,
       "disdnTS014CapabilitiesBE00A": disdnTS014CapabilitiesBE00A}
)
