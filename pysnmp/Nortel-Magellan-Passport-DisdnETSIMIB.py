# SNMP MIB module (Nortel-Magellan-Passport-DisdnETSIMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DisdnETSIMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:34 2024
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

_DataSigChanEtsi_ObjectIdentity = ObjectIdentity
dataSigChanEtsi = _DataSigChanEtsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10)
)
_DataSigChanEtsiRowStatusTable_Object = MibTable
dataSigChanEtsiRowStatusTable = _DataSigChanEtsiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 1)
)
if mibBuilder.loadTexts:
    dataSigChanEtsiRowStatusTable.setStatus("mandatory")
_DataSigChanEtsiRowStatusEntry_Object = MibTableRow
dataSigChanEtsiRowStatusEntry = _DataSigChanEtsiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 1, 1)
)
dataSigChanEtsiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanEtsiRowStatusEntry.setStatus("mandatory")
_DataSigChanEtsiRowStatus_Type = RowStatus
_DataSigChanEtsiRowStatus_Object = MibTableColumn
dataSigChanEtsiRowStatus = _DataSigChanEtsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 1, 1, 1),
    _DataSigChanEtsiRowStatus_Type()
)
dataSigChanEtsiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiRowStatus.setStatus("mandatory")
_DataSigChanEtsiComponentName_Type = DisplayString
_DataSigChanEtsiComponentName_Object = MibTableColumn
dataSigChanEtsiComponentName = _DataSigChanEtsiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 1, 1, 2),
    _DataSigChanEtsiComponentName_Type()
)
dataSigChanEtsiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiComponentName.setStatus("mandatory")
_DataSigChanEtsiStorageType_Type = StorageType
_DataSigChanEtsiStorageType_Object = MibTableColumn
dataSigChanEtsiStorageType = _DataSigChanEtsiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 1, 1, 4),
    _DataSigChanEtsiStorageType_Type()
)
dataSigChanEtsiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiStorageType.setStatus("mandatory")
_DataSigChanEtsiIndex_Type = NonReplicated
_DataSigChanEtsiIndex_Object = MibTableColumn
dataSigChanEtsiIndex = _DataSigChanEtsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 1, 1, 10),
    _DataSigChanEtsiIndex_Type()
)
dataSigChanEtsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanEtsiIndex.setStatus("mandatory")
_DataSigChanEtsiFramer_ObjectIdentity = ObjectIdentity
dataSigChanEtsiFramer = _DataSigChanEtsiFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2)
)
_DataSigChanEtsiFramerRowStatusTable_Object = MibTable
dataSigChanEtsiFramerRowStatusTable = _DataSigChanEtsiFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerRowStatusTable.setStatus("mandatory")
_DataSigChanEtsiFramerRowStatusEntry_Object = MibTableRow
dataSigChanEtsiFramerRowStatusEntry = _DataSigChanEtsiFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 1, 1)
)
dataSigChanEtsiFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerRowStatusEntry.setStatus("mandatory")
_DataSigChanEtsiFramerRowStatus_Type = RowStatus
_DataSigChanEtsiFramerRowStatus_Object = MibTableColumn
dataSigChanEtsiFramerRowStatus = _DataSigChanEtsiFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 1, 1, 1),
    _DataSigChanEtsiFramerRowStatus_Type()
)
dataSigChanEtsiFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerRowStatus.setStatus("mandatory")
_DataSigChanEtsiFramerComponentName_Type = DisplayString
_DataSigChanEtsiFramerComponentName_Object = MibTableColumn
dataSigChanEtsiFramerComponentName = _DataSigChanEtsiFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 1, 1, 2),
    _DataSigChanEtsiFramerComponentName_Type()
)
dataSigChanEtsiFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerComponentName.setStatus("mandatory")
_DataSigChanEtsiFramerStorageType_Type = StorageType
_DataSigChanEtsiFramerStorageType_Object = MibTableColumn
dataSigChanEtsiFramerStorageType = _DataSigChanEtsiFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 1, 1, 4),
    _DataSigChanEtsiFramerStorageType_Type()
)
dataSigChanEtsiFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerStorageType.setStatus("mandatory")
_DataSigChanEtsiFramerIndex_Type = NonReplicated
_DataSigChanEtsiFramerIndex_Object = MibTableColumn
dataSigChanEtsiFramerIndex = _DataSigChanEtsiFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 1, 1, 10),
    _DataSigChanEtsiFramerIndex_Type()
)
dataSigChanEtsiFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerIndex.setStatus("mandatory")
_DataSigChanEtsiFramerProvTable_Object = MibTable
dataSigChanEtsiFramerProvTable = _DataSigChanEtsiFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 10)
)
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerProvTable.setStatus("mandatory")
_DataSigChanEtsiFramerProvEntry_Object = MibTableRow
dataSigChanEtsiFramerProvEntry = _DataSigChanEtsiFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 10, 1)
)
dataSigChanEtsiFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerProvEntry.setStatus("mandatory")
_DataSigChanEtsiFramerInterfaceName_Type = Link
_DataSigChanEtsiFramerInterfaceName_Object = MibTableColumn
dataSigChanEtsiFramerInterfaceName = _DataSigChanEtsiFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 10, 1, 1),
    _DataSigChanEtsiFramerInterfaceName_Type()
)
dataSigChanEtsiFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerInterfaceName.setStatus("mandatory")
_DataSigChanEtsiFramerStateTable_Object = MibTable
dataSigChanEtsiFramerStateTable = _DataSigChanEtsiFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 12)
)
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerStateTable.setStatus("mandatory")
_DataSigChanEtsiFramerStateEntry_Object = MibTableRow
dataSigChanEtsiFramerStateEntry = _DataSigChanEtsiFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 12, 1)
)
dataSigChanEtsiFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerStateEntry.setStatus("mandatory")


class _DataSigChanEtsiFramerAdminState_Type(Integer32):
    """Custom type dataSigChanEtsiFramerAdminState based on Integer32"""
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


_DataSigChanEtsiFramerAdminState_Type.__name__ = "Integer32"
_DataSigChanEtsiFramerAdminState_Object = MibTableColumn
dataSigChanEtsiFramerAdminState = _DataSigChanEtsiFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 12, 1, 1),
    _DataSigChanEtsiFramerAdminState_Type()
)
dataSigChanEtsiFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerAdminState.setStatus("mandatory")


class _DataSigChanEtsiFramerOperationalState_Type(Integer32):
    """Custom type dataSigChanEtsiFramerOperationalState based on Integer32"""
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


_DataSigChanEtsiFramerOperationalState_Type.__name__ = "Integer32"
_DataSigChanEtsiFramerOperationalState_Object = MibTableColumn
dataSigChanEtsiFramerOperationalState = _DataSigChanEtsiFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 12, 1, 2),
    _DataSigChanEtsiFramerOperationalState_Type()
)
dataSigChanEtsiFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerOperationalState.setStatus("mandatory")


class _DataSigChanEtsiFramerUsageState_Type(Integer32):
    """Custom type dataSigChanEtsiFramerUsageState based on Integer32"""
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


_DataSigChanEtsiFramerUsageState_Type.__name__ = "Integer32"
_DataSigChanEtsiFramerUsageState_Object = MibTableColumn
dataSigChanEtsiFramerUsageState = _DataSigChanEtsiFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 12, 1, 3),
    _DataSigChanEtsiFramerUsageState_Type()
)
dataSigChanEtsiFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerUsageState.setStatus("mandatory")
_DataSigChanEtsiFramerStatsTable_Object = MibTable
dataSigChanEtsiFramerStatsTable = _DataSigChanEtsiFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13)
)
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerStatsTable.setStatus("mandatory")
_DataSigChanEtsiFramerStatsEntry_Object = MibTableRow
dataSigChanEtsiFramerStatsEntry = _DataSigChanEtsiFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1)
)
dataSigChanEtsiFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiFramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerStatsEntry.setStatus("mandatory")


class _DataSigChanEtsiFramerFrmToIf_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerFrmToIf_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerFrmToIf_Object = MibTableColumn
dataSigChanEtsiFramerFrmToIf = _DataSigChanEtsiFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 1),
    _DataSigChanEtsiFramerFrmToIf_Type()
)
dataSigChanEtsiFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerFrmToIf.setStatus("mandatory")


class _DataSigChanEtsiFramerFrmFromIf_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerFrmFromIf_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerFrmFromIf_Object = MibTableColumn
dataSigChanEtsiFramerFrmFromIf = _DataSigChanEtsiFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 2),
    _DataSigChanEtsiFramerFrmFromIf_Type()
)
dataSigChanEtsiFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerFrmFromIf.setStatus("mandatory")


class _DataSigChanEtsiFramerOctetFromIf_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerOctetFromIf_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerOctetFromIf_Object = MibTableColumn
dataSigChanEtsiFramerOctetFromIf = _DataSigChanEtsiFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 3),
    _DataSigChanEtsiFramerOctetFromIf_Type()
)
dataSigChanEtsiFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerOctetFromIf.setStatus("mandatory")


class _DataSigChanEtsiFramerAborts_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerAborts_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerAborts_Object = MibTableColumn
dataSigChanEtsiFramerAborts = _DataSigChanEtsiFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 4),
    _DataSigChanEtsiFramerAborts_Type()
)
dataSigChanEtsiFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerAborts.setStatus("mandatory")


class _DataSigChanEtsiFramerCrcErrors_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerCrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerCrcErrors_Object = MibTableColumn
dataSigChanEtsiFramerCrcErrors = _DataSigChanEtsiFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 5),
    _DataSigChanEtsiFramerCrcErrors_Type()
)
dataSigChanEtsiFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerCrcErrors.setStatus("mandatory")


class _DataSigChanEtsiFramerLrcErrors_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerLrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerLrcErrors_Object = MibTableColumn
dataSigChanEtsiFramerLrcErrors = _DataSigChanEtsiFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 6),
    _DataSigChanEtsiFramerLrcErrors_Type()
)
dataSigChanEtsiFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerLrcErrors.setStatus("mandatory")


class _DataSigChanEtsiFramerNonOctetErrors_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerNonOctetErrors_Object = MibTableColumn
dataSigChanEtsiFramerNonOctetErrors = _DataSigChanEtsiFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 7),
    _DataSigChanEtsiFramerNonOctetErrors_Type()
)
dataSigChanEtsiFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerNonOctetErrors.setStatus("mandatory")


class _DataSigChanEtsiFramerOverruns_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerOverruns_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerOverruns_Object = MibTableColumn
dataSigChanEtsiFramerOverruns = _DataSigChanEtsiFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 8),
    _DataSigChanEtsiFramerOverruns_Type()
)
dataSigChanEtsiFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerOverruns.setStatus("mandatory")


class _DataSigChanEtsiFramerUnderruns_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerUnderruns_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerUnderruns_Object = MibTableColumn
dataSigChanEtsiFramerUnderruns = _DataSigChanEtsiFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 9),
    _DataSigChanEtsiFramerUnderruns_Type()
)
dataSigChanEtsiFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerUnderruns.setStatus("mandatory")


class _DataSigChanEtsiFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type dataSigChanEtsiFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanEtsiFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_DataSigChanEtsiFramerLargeFrmErrors_Object = MibTableColumn
dataSigChanEtsiFramerLargeFrmErrors = _DataSigChanEtsiFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 2, 13, 1, 10),
    _DataSigChanEtsiFramerLargeFrmErrors_Type()
)
dataSigChanEtsiFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiFramerLargeFrmErrors.setStatus("mandatory")
_DataSigChanEtsiL2Table_Object = MibTable
dataSigChanEtsiL2Table = _DataSigChanEtsiL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 11)
)
if mibBuilder.loadTexts:
    dataSigChanEtsiL2Table.setStatus("mandatory")
_DataSigChanEtsiL2Entry_Object = MibTableRow
dataSigChanEtsiL2Entry = _DataSigChanEtsiL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 11, 1)
)
dataSigChanEtsiL2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanEtsiL2Entry.setStatus("mandatory")


class _DataSigChanEtsiT23_Type(Unsigned32):
    """Custom type dataSigChanEtsiT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DataSigChanEtsiT23_Type.__name__ = "Unsigned32"
_DataSigChanEtsiT23_Object = MibTableColumn
dataSigChanEtsiT23 = _DataSigChanEtsiT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 11, 1, 1),
    _DataSigChanEtsiT23_Type()
)
dataSigChanEtsiT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiT23.setStatus("mandatory")


class _DataSigChanEtsiT200_Type(Unsigned32):
    """Custom type dataSigChanEtsiT200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DataSigChanEtsiT200_Type.__name__ = "Unsigned32"
_DataSigChanEtsiT200_Object = MibTableColumn
dataSigChanEtsiT200 = _DataSigChanEtsiT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 11, 1, 2),
    _DataSigChanEtsiT200_Type()
)
dataSigChanEtsiT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiT200.setStatus("mandatory")


class _DataSigChanEtsiN200_Type(Unsigned32):
    """Custom type dataSigChanEtsiN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DataSigChanEtsiN200_Type.__name__ = "Unsigned32"
_DataSigChanEtsiN200_Object = MibTableColumn
dataSigChanEtsiN200 = _DataSigChanEtsiN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 11, 1, 3),
    _DataSigChanEtsiN200_Type()
)
dataSigChanEtsiN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiN200.setStatus("mandatory")


class _DataSigChanEtsiT203_Type(Unsigned32):
    """Custom type dataSigChanEtsiT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_DataSigChanEtsiT203_Type.__name__ = "Unsigned32"
_DataSigChanEtsiT203_Object = MibTableColumn
dataSigChanEtsiT203 = _DataSigChanEtsiT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 11, 1, 4),
    _DataSigChanEtsiT203_Type()
)
dataSigChanEtsiT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiT203.setStatus("mandatory")


class _DataSigChanEtsiN201_Type(Unsigned32):
    """Custom type dataSigChanEtsiN201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_DataSigChanEtsiN201_Type.__name__ = "Unsigned32"
_DataSigChanEtsiN201_Object = MibTableColumn
dataSigChanEtsiN201 = _DataSigChanEtsiN201_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 11, 1, 5),
    _DataSigChanEtsiN201_Type()
)
dataSigChanEtsiN201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiN201.setStatus("mandatory")


class _DataSigChanEtsiCircuitSwitchedK_Type(Unsigned32):
    """Custom type dataSigChanEtsiCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_DataSigChanEtsiCircuitSwitchedK_Type.__name__ = "Unsigned32"
_DataSigChanEtsiCircuitSwitchedK_Object = MibTableColumn
dataSigChanEtsiCircuitSwitchedK = _DataSigChanEtsiCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 11, 1, 6),
    _DataSigChanEtsiCircuitSwitchedK_Type()
)
dataSigChanEtsiCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiCircuitSwitchedK.setStatus("mandatory")
_DataSigChanEtsiProvTable_Object = MibTable
dataSigChanEtsiProvTable = _DataSigChanEtsiProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 13)
)
if mibBuilder.loadTexts:
    dataSigChanEtsiProvTable.setStatus("mandatory")
_DataSigChanEtsiProvEntry_Object = MibTableRow
dataSigChanEtsiProvEntry = _DataSigChanEtsiProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 13, 1)
)
dataSigChanEtsiProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanEtsiProvEntry.setStatus("mandatory")


class _DataSigChanEtsiSide_Type(Integer32):
    """Custom type dataSigChanEtsiSide based on Integer32"""
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


_DataSigChanEtsiSide_Type.__name__ = "Integer32"
_DataSigChanEtsiSide_Object = MibTableColumn
dataSigChanEtsiSide = _DataSigChanEtsiSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 13, 1, 1),
    _DataSigChanEtsiSide_Type()
)
dataSigChanEtsiSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiSide.setStatus("mandatory")
_DataSigChanEtsiOperTable_Object = MibTable
dataSigChanEtsiOperTable = _DataSigChanEtsiOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 15)
)
if mibBuilder.loadTexts:
    dataSigChanEtsiOperTable.setStatus("mandatory")
_DataSigChanEtsiOperEntry_Object = MibTableRow
dataSigChanEtsiOperEntry = _DataSigChanEtsiOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 15, 1)
)
dataSigChanEtsiOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanEtsiOperEntry.setStatus("mandatory")


class _DataSigChanEtsiActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanEtsiActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanEtsiActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanEtsiActiveChannels_Object = MibTableColumn
dataSigChanEtsiActiveChannels = _DataSigChanEtsiActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 15, 1, 1),
    _DataSigChanEtsiActiveChannels_Type()
)
dataSigChanEtsiActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiActiveChannels.setStatus("mandatory")


class _DataSigChanEtsiPeakActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanEtsiPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanEtsiPeakActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanEtsiPeakActiveChannels_Object = MibTableColumn
dataSigChanEtsiPeakActiveChannels = _DataSigChanEtsiPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 15, 1, 4),
    _DataSigChanEtsiPeakActiveChannels_Type()
)
dataSigChanEtsiPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiPeakActiveChannels.setStatus("mandatory")


class _DataSigChanEtsiDChanStatus_Type(Integer32):
    """Custom type dataSigChanEtsiDChanStatus based on Integer32"""
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


_DataSigChanEtsiDChanStatus_Type.__name__ = "Integer32"
_DataSigChanEtsiDChanStatus_Object = MibTableColumn
dataSigChanEtsiDChanStatus = _DataSigChanEtsiDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 15, 1, 7),
    _DataSigChanEtsiDChanStatus_Type()
)
dataSigChanEtsiDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanEtsiDChanStatus.setStatus("mandatory")
_DataSigChanEtsiToolsTable_Object = MibTable
dataSigChanEtsiToolsTable = _DataSigChanEtsiToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 16)
)
if mibBuilder.loadTexts:
    dataSigChanEtsiToolsTable.setStatus("mandatory")
_DataSigChanEtsiToolsEntry_Object = MibTableRow
dataSigChanEtsiToolsEntry = _DataSigChanEtsiToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 16, 1)
)
dataSigChanEtsiToolsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnETSIMIB", "dataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanEtsiToolsEntry.setStatus("mandatory")


class _DataSigChanEtsiTracing_Type(OctetString):
    """Custom type dataSigChanEtsiTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DataSigChanEtsiTracing_Type.__name__ = "OctetString"
_DataSigChanEtsiTracing_Object = MibTableColumn
dataSigChanEtsiTracing = _DataSigChanEtsiTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 10, 16, 1, 1),
    _DataSigChanEtsiTracing_Type()
)
dataSigChanEtsiTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanEtsiTracing.setStatus("mandatory")
_DisdnETSIMIB_ObjectIdentity = ObjectIdentity
disdnETSIMIB = _DisdnETSIMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 117)
)
_DisdnETSIGroup_ObjectIdentity = ObjectIdentity
disdnETSIGroup = _DisdnETSIGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 117, 1)
)
_DisdnETSIGroupBE_ObjectIdentity = ObjectIdentity
disdnETSIGroupBE = _DisdnETSIGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 117, 1, 5)
)
_DisdnETSIGroupBE00_ObjectIdentity = ObjectIdentity
disdnETSIGroupBE00 = _DisdnETSIGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 117, 1, 5, 1)
)
_DisdnETSIGroupBE00A_ObjectIdentity = ObjectIdentity
disdnETSIGroupBE00A = _DisdnETSIGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 117, 1, 5, 1, 2)
)
_DisdnETSICapabilities_ObjectIdentity = ObjectIdentity
disdnETSICapabilities = _DisdnETSICapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 117, 3)
)
_DisdnETSICapabilitiesBE_ObjectIdentity = ObjectIdentity
disdnETSICapabilitiesBE = _DisdnETSICapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 117, 3, 5)
)
_DisdnETSICapabilitiesBE00_ObjectIdentity = ObjectIdentity
disdnETSICapabilitiesBE00 = _DisdnETSICapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 117, 3, 5, 1)
)
_DisdnETSICapabilitiesBE00A_ObjectIdentity = ObjectIdentity
disdnETSICapabilitiesBE00A = _DisdnETSICapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 117, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DisdnETSIMIB",
    **{"dataSigChanEtsi": dataSigChanEtsi,
       "dataSigChanEtsiRowStatusTable": dataSigChanEtsiRowStatusTable,
       "dataSigChanEtsiRowStatusEntry": dataSigChanEtsiRowStatusEntry,
       "dataSigChanEtsiRowStatus": dataSigChanEtsiRowStatus,
       "dataSigChanEtsiComponentName": dataSigChanEtsiComponentName,
       "dataSigChanEtsiStorageType": dataSigChanEtsiStorageType,
       "dataSigChanEtsiIndex": dataSigChanEtsiIndex,
       "dataSigChanEtsiFramer": dataSigChanEtsiFramer,
       "dataSigChanEtsiFramerRowStatusTable": dataSigChanEtsiFramerRowStatusTable,
       "dataSigChanEtsiFramerRowStatusEntry": dataSigChanEtsiFramerRowStatusEntry,
       "dataSigChanEtsiFramerRowStatus": dataSigChanEtsiFramerRowStatus,
       "dataSigChanEtsiFramerComponentName": dataSigChanEtsiFramerComponentName,
       "dataSigChanEtsiFramerStorageType": dataSigChanEtsiFramerStorageType,
       "dataSigChanEtsiFramerIndex": dataSigChanEtsiFramerIndex,
       "dataSigChanEtsiFramerProvTable": dataSigChanEtsiFramerProvTable,
       "dataSigChanEtsiFramerProvEntry": dataSigChanEtsiFramerProvEntry,
       "dataSigChanEtsiFramerInterfaceName": dataSigChanEtsiFramerInterfaceName,
       "dataSigChanEtsiFramerStateTable": dataSigChanEtsiFramerStateTable,
       "dataSigChanEtsiFramerStateEntry": dataSigChanEtsiFramerStateEntry,
       "dataSigChanEtsiFramerAdminState": dataSigChanEtsiFramerAdminState,
       "dataSigChanEtsiFramerOperationalState": dataSigChanEtsiFramerOperationalState,
       "dataSigChanEtsiFramerUsageState": dataSigChanEtsiFramerUsageState,
       "dataSigChanEtsiFramerStatsTable": dataSigChanEtsiFramerStatsTable,
       "dataSigChanEtsiFramerStatsEntry": dataSigChanEtsiFramerStatsEntry,
       "dataSigChanEtsiFramerFrmToIf": dataSigChanEtsiFramerFrmToIf,
       "dataSigChanEtsiFramerFrmFromIf": dataSigChanEtsiFramerFrmFromIf,
       "dataSigChanEtsiFramerOctetFromIf": dataSigChanEtsiFramerOctetFromIf,
       "dataSigChanEtsiFramerAborts": dataSigChanEtsiFramerAborts,
       "dataSigChanEtsiFramerCrcErrors": dataSigChanEtsiFramerCrcErrors,
       "dataSigChanEtsiFramerLrcErrors": dataSigChanEtsiFramerLrcErrors,
       "dataSigChanEtsiFramerNonOctetErrors": dataSigChanEtsiFramerNonOctetErrors,
       "dataSigChanEtsiFramerOverruns": dataSigChanEtsiFramerOverruns,
       "dataSigChanEtsiFramerUnderruns": dataSigChanEtsiFramerUnderruns,
       "dataSigChanEtsiFramerLargeFrmErrors": dataSigChanEtsiFramerLargeFrmErrors,
       "dataSigChanEtsiL2Table": dataSigChanEtsiL2Table,
       "dataSigChanEtsiL2Entry": dataSigChanEtsiL2Entry,
       "dataSigChanEtsiT23": dataSigChanEtsiT23,
       "dataSigChanEtsiT200": dataSigChanEtsiT200,
       "dataSigChanEtsiN200": dataSigChanEtsiN200,
       "dataSigChanEtsiT203": dataSigChanEtsiT203,
       "dataSigChanEtsiN201": dataSigChanEtsiN201,
       "dataSigChanEtsiCircuitSwitchedK": dataSigChanEtsiCircuitSwitchedK,
       "dataSigChanEtsiProvTable": dataSigChanEtsiProvTable,
       "dataSigChanEtsiProvEntry": dataSigChanEtsiProvEntry,
       "dataSigChanEtsiSide": dataSigChanEtsiSide,
       "dataSigChanEtsiOperTable": dataSigChanEtsiOperTable,
       "dataSigChanEtsiOperEntry": dataSigChanEtsiOperEntry,
       "dataSigChanEtsiActiveChannels": dataSigChanEtsiActiveChannels,
       "dataSigChanEtsiPeakActiveChannels": dataSigChanEtsiPeakActiveChannels,
       "dataSigChanEtsiDChanStatus": dataSigChanEtsiDChanStatus,
       "dataSigChanEtsiToolsTable": dataSigChanEtsiToolsTable,
       "dataSigChanEtsiToolsEntry": dataSigChanEtsiToolsEntry,
       "dataSigChanEtsiTracing": dataSigChanEtsiTracing,
       "disdnETSIMIB": disdnETSIMIB,
       "disdnETSIGroup": disdnETSIGroup,
       "disdnETSIGroupBE": disdnETSIGroupBE,
       "disdnETSIGroupBE00": disdnETSIGroupBE00,
       "disdnETSIGroupBE00A": disdnETSIGroupBE00A,
       "disdnETSICapabilities": disdnETSICapabilities,
       "disdnETSICapabilitiesBE": disdnETSICapabilitiesBE,
       "disdnETSICapabilitiesBE00": disdnETSICapabilitiesBE00,
       "disdnETSICapabilitiesBE00A": disdnETSICapabilitiesBE00A}
)
