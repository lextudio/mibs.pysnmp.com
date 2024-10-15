# SNMP MIB module (Nortel-Magellan-Passport-DisdnNI2MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DisdnNI2MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:36 2024
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

_DataSigChanNi2_ObjectIdentity = ObjectIdentity
dataSigChanNi2 = _DataSigChanNi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12)
)
_DataSigChanNi2RowStatusTable_Object = MibTable
dataSigChanNi2RowStatusTable = _DataSigChanNi2RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 1)
)
if mibBuilder.loadTexts:
    dataSigChanNi2RowStatusTable.setStatus("mandatory")
_DataSigChanNi2RowStatusEntry_Object = MibTableRow
dataSigChanNi2RowStatusEntry = _DataSigChanNi2RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 1, 1)
)
dataSigChanNi2RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    dataSigChanNi2RowStatusEntry.setStatus("mandatory")
_DataSigChanNi2RowStatus_Type = RowStatus
_DataSigChanNi2RowStatus_Object = MibTableColumn
dataSigChanNi2RowStatus = _DataSigChanNi2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 1, 1, 1),
    _DataSigChanNi2RowStatus_Type()
)
dataSigChanNi2RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2RowStatus.setStatus("mandatory")
_DataSigChanNi2ComponentName_Type = DisplayString
_DataSigChanNi2ComponentName_Object = MibTableColumn
dataSigChanNi2ComponentName = _DataSigChanNi2ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 1, 1, 2),
    _DataSigChanNi2ComponentName_Type()
)
dataSigChanNi2ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2ComponentName.setStatus("mandatory")
_DataSigChanNi2StorageType_Type = StorageType
_DataSigChanNi2StorageType_Object = MibTableColumn
dataSigChanNi2StorageType = _DataSigChanNi2StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 1, 1, 4),
    _DataSigChanNi2StorageType_Type()
)
dataSigChanNi2StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2StorageType.setStatus("mandatory")
_DataSigChanNi2Index_Type = NonReplicated
_DataSigChanNi2Index_Object = MibTableColumn
dataSigChanNi2Index = _DataSigChanNi2Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 1, 1, 10),
    _DataSigChanNi2Index_Type()
)
dataSigChanNi2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanNi2Index.setStatus("mandatory")
_DataSigChanNi2Framer_ObjectIdentity = ObjectIdentity
dataSigChanNi2Framer = _DataSigChanNi2Framer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2)
)
_DataSigChanNi2FramerRowStatusTable_Object = MibTable
dataSigChanNi2FramerRowStatusTable = _DataSigChanNi2FramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 1)
)
if mibBuilder.loadTexts:
    dataSigChanNi2FramerRowStatusTable.setStatus("mandatory")
_DataSigChanNi2FramerRowStatusEntry_Object = MibTableRow
dataSigChanNi2FramerRowStatusEntry = _DataSigChanNi2FramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 1, 1)
)
dataSigChanNi2FramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2Index"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2FramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNi2FramerRowStatusEntry.setStatus("mandatory")
_DataSigChanNi2FramerRowStatus_Type = RowStatus
_DataSigChanNi2FramerRowStatus_Object = MibTableColumn
dataSigChanNi2FramerRowStatus = _DataSigChanNi2FramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 1, 1, 1),
    _DataSigChanNi2FramerRowStatus_Type()
)
dataSigChanNi2FramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerRowStatus.setStatus("mandatory")
_DataSigChanNi2FramerComponentName_Type = DisplayString
_DataSigChanNi2FramerComponentName_Object = MibTableColumn
dataSigChanNi2FramerComponentName = _DataSigChanNi2FramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 1, 1, 2),
    _DataSigChanNi2FramerComponentName_Type()
)
dataSigChanNi2FramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerComponentName.setStatus("mandatory")
_DataSigChanNi2FramerStorageType_Type = StorageType
_DataSigChanNi2FramerStorageType_Object = MibTableColumn
dataSigChanNi2FramerStorageType = _DataSigChanNi2FramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 1, 1, 4),
    _DataSigChanNi2FramerStorageType_Type()
)
dataSigChanNi2FramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerStorageType.setStatus("mandatory")
_DataSigChanNi2FramerIndex_Type = NonReplicated
_DataSigChanNi2FramerIndex_Object = MibTableColumn
dataSigChanNi2FramerIndex = _DataSigChanNi2FramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 1, 1, 10),
    _DataSigChanNi2FramerIndex_Type()
)
dataSigChanNi2FramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerIndex.setStatus("mandatory")
_DataSigChanNi2FramerProvTable_Object = MibTable
dataSigChanNi2FramerProvTable = _DataSigChanNi2FramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 10)
)
if mibBuilder.loadTexts:
    dataSigChanNi2FramerProvTable.setStatus("mandatory")
_DataSigChanNi2FramerProvEntry_Object = MibTableRow
dataSigChanNi2FramerProvEntry = _DataSigChanNi2FramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 10, 1)
)
dataSigChanNi2FramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2Index"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2FramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNi2FramerProvEntry.setStatus("mandatory")
_DataSigChanNi2FramerInterfaceName_Type = Link
_DataSigChanNi2FramerInterfaceName_Object = MibTableColumn
dataSigChanNi2FramerInterfaceName = _DataSigChanNi2FramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 10, 1, 1),
    _DataSigChanNi2FramerInterfaceName_Type()
)
dataSigChanNi2FramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerInterfaceName.setStatus("mandatory")
_DataSigChanNi2FramerStateTable_Object = MibTable
dataSigChanNi2FramerStateTable = _DataSigChanNi2FramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 12)
)
if mibBuilder.loadTexts:
    dataSigChanNi2FramerStateTable.setStatus("mandatory")
_DataSigChanNi2FramerStateEntry_Object = MibTableRow
dataSigChanNi2FramerStateEntry = _DataSigChanNi2FramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 12, 1)
)
dataSigChanNi2FramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2Index"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2FramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNi2FramerStateEntry.setStatus("mandatory")


class _DataSigChanNi2FramerAdminState_Type(Integer32):
    """Custom type dataSigChanNi2FramerAdminState based on Integer32"""
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


_DataSigChanNi2FramerAdminState_Type.__name__ = "Integer32"
_DataSigChanNi2FramerAdminState_Object = MibTableColumn
dataSigChanNi2FramerAdminState = _DataSigChanNi2FramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 12, 1, 1),
    _DataSigChanNi2FramerAdminState_Type()
)
dataSigChanNi2FramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerAdminState.setStatus("mandatory")


class _DataSigChanNi2FramerOperationalState_Type(Integer32):
    """Custom type dataSigChanNi2FramerOperationalState based on Integer32"""
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


_DataSigChanNi2FramerOperationalState_Type.__name__ = "Integer32"
_DataSigChanNi2FramerOperationalState_Object = MibTableColumn
dataSigChanNi2FramerOperationalState = _DataSigChanNi2FramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 12, 1, 2),
    _DataSigChanNi2FramerOperationalState_Type()
)
dataSigChanNi2FramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerOperationalState.setStatus("mandatory")


class _DataSigChanNi2FramerUsageState_Type(Integer32):
    """Custom type dataSigChanNi2FramerUsageState based on Integer32"""
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


_DataSigChanNi2FramerUsageState_Type.__name__ = "Integer32"
_DataSigChanNi2FramerUsageState_Object = MibTableColumn
dataSigChanNi2FramerUsageState = _DataSigChanNi2FramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 12, 1, 3),
    _DataSigChanNi2FramerUsageState_Type()
)
dataSigChanNi2FramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerUsageState.setStatus("mandatory")
_DataSigChanNi2FramerStatsTable_Object = MibTable
dataSigChanNi2FramerStatsTable = _DataSigChanNi2FramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13)
)
if mibBuilder.loadTexts:
    dataSigChanNi2FramerStatsTable.setStatus("mandatory")
_DataSigChanNi2FramerStatsEntry_Object = MibTableRow
dataSigChanNi2FramerStatsEntry = _DataSigChanNi2FramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1)
)
dataSigChanNi2FramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2Index"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2FramerIndex"),
)
if mibBuilder.loadTexts:
    dataSigChanNi2FramerStatsEntry.setStatus("mandatory")


class _DataSigChanNi2FramerFrmToIf_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerFrmToIf_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerFrmToIf_Object = MibTableColumn
dataSigChanNi2FramerFrmToIf = _DataSigChanNi2FramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 1),
    _DataSigChanNi2FramerFrmToIf_Type()
)
dataSigChanNi2FramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerFrmToIf.setStatus("mandatory")


class _DataSigChanNi2FramerFrmFromIf_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerFrmFromIf_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerFrmFromIf_Object = MibTableColumn
dataSigChanNi2FramerFrmFromIf = _DataSigChanNi2FramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 2),
    _DataSigChanNi2FramerFrmFromIf_Type()
)
dataSigChanNi2FramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerFrmFromIf.setStatus("mandatory")


class _DataSigChanNi2FramerOctetFromIf_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerOctetFromIf_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerOctetFromIf_Object = MibTableColumn
dataSigChanNi2FramerOctetFromIf = _DataSigChanNi2FramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 3),
    _DataSigChanNi2FramerOctetFromIf_Type()
)
dataSigChanNi2FramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerOctetFromIf.setStatus("mandatory")


class _DataSigChanNi2FramerAborts_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerAborts_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerAborts_Object = MibTableColumn
dataSigChanNi2FramerAborts = _DataSigChanNi2FramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 4),
    _DataSigChanNi2FramerAborts_Type()
)
dataSigChanNi2FramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerAborts.setStatus("mandatory")


class _DataSigChanNi2FramerCrcErrors_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerCrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerCrcErrors_Object = MibTableColumn
dataSigChanNi2FramerCrcErrors = _DataSigChanNi2FramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 5),
    _DataSigChanNi2FramerCrcErrors_Type()
)
dataSigChanNi2FramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerCrcErrors.setStatus("mandatory")


class _DataSigChanNi2FramerLrcErrors_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerLrcErrors_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerLrcErrors_Object = MibTableColumn
dataSigChanNi2FramerLrcErrors = _DataSigChanNi2FramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 6),
    _DataSigChanNi2FramerLrcErrors_Type()
)
dataSigChanNi2FramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerLrcErrors.setStatus("mandatory")


class _DataSigChanNi2FramerNonOctetErrors_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerNonOctetErrors_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerNonOctetErrors_Object = MibTableColumn
dataSigChanNi2FramerNonOctetErrors = _DataSigChanNi2FramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 7),
    _DataSigChanNi2FramerNonOctetErrors_Type()
)
dataSigChanNi2FramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerNonOctetErrors.setStatus("mandatory")


class _DataSigChanNi2FramerOverruns_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerOverruns_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerOverruns_Object = MibTableColumn
dataSigChanNi2FramerOverruns = _DataSigChanNi2FramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 8),
    _DataSigChanNi2FramerOverruns_Type()
)
dataSigChanNi2FramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerOverruns.setStatus("mandatory")


class _DataSigChanNi2FramerUnderruns_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerUnderruns_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerUnderruns_Object = MibTableColumn
dataSigChanNi2FramerUnderruns = _DataSigChanNi2FramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 9),
    _DataSigChanNi2FramerUnderruns_Type()
)
dataSigChanNi2FramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerUnderruns.setStatus("mandatory")


class _DataSigChanNi2FramerLargeFrmErrors_Type(Unsigned32):
    """Custom type dataSigChanNi2FramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DataSigChanNi2FramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_DataSigChanNi2FramerLargeFrmErrors_Object = MibTableColumn
dataSigChanNi2FramerLargeFrmErrors = _DataSigChanNi2FramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 2, 13, 1, 10),
    _DataSigChanNi2FramerLargeFrmErrors_Type()
)
dataSigChanNi2FramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2FramerLargeFrmErrors.setStatus("mandatory")
_DataSigChanNi2L2Table_Object = MibTable
dataSigChanNi2L2Table = _DataSigChanNi2L2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 11)
)
if mibBuilder.loadTexts:
    dataSigChanNi2L2Table.setStatus("mandatory")
_DataSigChanNi2L2Entry_Object = MibTableRow
dataSigChanNi2L2Entry = _DataSigChanNi2L2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 11, 1)
)
dataSigChanNi2L2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    dataSigChanNi2L2Entry.setStatus("mandatory")


class _DataSigChanNi2T23_Type(Unsigned32):
    """Custom type dataSigChanNi2T23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DataSigChanNi2T23_Type.__name__ = "Unsigned32"
_DataSigChanNi2T23_Object = MibTableColumn
dataSigChanNi2T23 = _DataSigChanNi2T23_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 11, 1, 1),
    _DataSigChanNi2T23_Type()
)
dataSigChanNi2T23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2T23.setStatus("mandatory")


class _DataSigChanNi2T200_Type(Unsigned32):
    """Custom type dataSigChanNi2T200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DataSigChanNi2T200_Type.__name__ = "Unsigned32"
_DataSigChanNi2T200_Object = MibTableColumn
dataSigChanNi2T200 = _DataSigChanNi2T200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 11, 1, 2),
    _DataSigChanNi2T200_Type()
)
dataSigChanNi2T200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2T200.setStatus("mandatory")


class _DataSigChanNi2N200_Type(Unsigned32):
    """Custom type dataSigChanNi2N200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DataSigChanNi2N200_Type.__name__ = "Unsigned32"
_DataSigChanNi2N200_Object = MibTableColumn
dataSigChanNi2N200 = _DataSigChanNi2N200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 11, 1, 3),
    _DataSigChanNi2N200_Type()
)
dataSigChanNi2N200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2N200.setStatus("mandatory")


class _DataSigChanNi2T203_Type(Unsigned32):
    """Custom type dataSigChanNi2T203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_DataSigChanNi2T203_Type.__name__ = "Unsigned32"
_DataSigChanNi2T203_Object = MibTableColumn
dataSigChanNi2T203 = _DataSigChanNi2T203_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 11, 1, 4),
    _DataSigChanNi2T203_Type()
)
dataSigChanNi2T203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2T203.setStatus("mandatory")


class _DataSigChanNi2N201_Type(Unsigned32):
    """Custom type dataSigChanNi2N201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_DataSigChanNi2N201_Type.__name__ = "Unsigned32"
_DataSigChanNi2N201_Object = MibTableColumn
dataSigChanNi2N201 = _DataSigChanNi2N201_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 11, 1, 5),
    _DataSigChanNi2N201_Type()
)
dataSigChanNi2N201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2N201.setStatus("mandatory")


class _DataSigChanNi2CircuitSwitchedK_Type(Unsigned32):
    """Custom type dataSigChanNi2CircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_DataSigChanNi2CircuitSwitchedK_Type.__name__ = "Unsigned32"
_DataSigChanNi2CircuitSwitchedK_Object = MibTableColumn
dataSigChanNi2CircuitSwitchedK = _DataSigChanNi2CircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 11, 1, 6),
    _DataSigChanNi2CircuitSwitchedK_Type()
)
dataSigChanNi2CircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2CircuitSwitchedK.setStatus("mandatory")
_DataSigChanNi2ProvTable_Object = MibTable
dataSigChanNi2ProvTable = _DataSigChanNi2ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 13)
)
if mibBuilder.loadTexts:
    dataSigChanNi2ProvTable.setStatus("mandatory")
_DataSigChanNi2ProvEntry_Object = MibTableRow
dataSigChanNi2ProvEntry = _DataSigChanNi2ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 13, 1)
)
dataSigChanNi2ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    dataSigChanNi2ProvEntry.setStatus("mandatory")


class _DataSigChanNi2Side_Type(Integer32):
    """Custom type dataSigChanNi2Side based on Integer32"""
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


_DataSigChanNi2Side_Type.__name__ = "Integer32"
_DataSigChanNi2Side_Object = MibTableColumn
dataSigChanNi2Side = _DataSigChanNi2Side_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 13, 1, 1),
    _DataSigChanNi2Side_Type()
)
dataSigChanNi2Side.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2Side.setStatus("mandatory")
_DataSigChanNi2OperTable_Object = MibTable
dataSigChanNi2OperTable = _DataSigChanNi2OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 15)
)
if mibBuilder.loadTexts:
    dataSigChanNi2OperTable.setStatus("mandatory")
_DataSigChanNi2OperEntry_Object = MibTableRow
dataSigChanNi2OperEntry = _DataSigChanNi2OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 15, 1)
)
dataSigChanNi2OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    dataSigChanNi2OperEntry.setStatus("mandatory")


class _DataSigChanNi2ActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanNi2ActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanNi2ActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanNi2ActiveChannels_Object = MibTableColumn
dataSigChanNi2ActiveChannels = _DataSigChanNi2ActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 15, 1, 1),
    _DataSigChanNi2ActiveChannels_Type()
)
dataSigChanNi2ActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2ActiveChannels.setStatus("mandatory")


class _DataSigChanNi2PeakActiveChannels_Type(Unsigned32):
    """Custom type dataSigChanNi2PeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DataSigChanNi2PeakActiveChannels_Type.__name__ = "Unsigned32"
_DataSigChanNi2PeakActiveChannels_Object = MibTableColumn
dataSigChanNi2PeakActiveChannels = _DataSigChanNi2PeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 15, 1, 4),
    _DataSigChanNi2PeakActiveChannels_Type()
)
dataSigChanNi2PeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2PeakActiveChannels.setStatus("mandatory")


class _DataSigChanNi2DChanStatus_Type(Integer32):
    """Custom type dataSigChanNi2DChanStatus based on Integer32"""
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


_DataSigChanNi2DChanStatus_Type.__name__ = "Integer32"
_DataSigChanNi2DChanStatus_Object = MibTableColumn
dataSigChanNi2DChanStatus = _DataSigChanNi2DChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 15, 1, 7),
    _DataSigChanNi2DChanStatus_Type()
)
dataSigChanNi2DChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSigChanNi2DChanStatus.setStatus("mandatory")
_DataSigChanNi2ToolsTable_Object = MibTable
dataSigChanNi2ToolsTable = _DataSigChanNi2ToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 16)
)
if mibBuilder.loadTexts:
    dataSigChanNi2ToolsTable.setStatus("mandatory")
_DataSigChanNi2ToolsEntry_Object = MibTableRow
dataSigChanNi2ToolsEntry = _DataSigChanNi2ToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 16, 1)
)
dataSigChanNi2ToolsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"),
    (0, "Nortel-Magellan-Passport-DisdnNI2MIB", "dataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    dataSigChanNi2ToolsEntry.setStatus("mandatory")


class _DataSigChanNi2Tracing_Type(OctetString):
    """Custom type dataSigChanNi2Tracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DataSigChanNi2Tracing_Type.__name__ = "OctetString"
_DataSigChanNi2Tracing_Object = MibTableColumn
dataSigChanNi2Tracing = _DataSigChanNi2Tracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 12, 16, 1, 1),
    _DataSigChanNi2Tracing_Type()
)
dataSigChanNi2Tracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataSigChanNi2Tracing.setStatus("mandatory")
_DisdnNI2MIB_ObjectIdentity = ObjectIdentity
disdnNI2MIB = _DisdnNI2MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 126)
)
_DisdnNI2Group_ObjectIdentity = ObjectIdentity
disdnNI2Group = _DisdnNI2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 126, 1)
)
_DisdnNI2GroupBE_ObjectIdentity = ObjectIdentity
disdnNI2GroupBE = _DisdnNI2GroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 126, 1, 5)
)
_DisdnNI2GroupBE00_ObjectIdentity = ObjectIdentity
disdnNI2GroupBE00 = _DisdnNI2GroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 126, 1, 5, 1)
)
_DisdnNI2GroupBE00A_ObjectIdentity = ObjectIdentity
disdnNI2GroupBE00A = _DisdnNI2GroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 126, 1, 5, 1, 2)
)
_DisdnNI2Capabilities_ObjectIdentity = ObjectIdentity
disdnNI2Capabilities = _DisdnNI2Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 126, 3)
)
_DisdnNI2CapabilitiesBE_ObjectIdentity = ObjectIdentity
disdnNI2CapabilitiesBE = _DisdnNI2CapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 126, 3, 5)
)
_DisdnNI2CapabilitiesBE00_ObjectIdentity = ObjectIdentity
disdnNI2CapabilitiesBE00 = _DisdnNI2CapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 126, 3, 5, 1)
)
_DisdnNI2CapabilitiesBE00A_ObjectIdentity = ObjectIdentity
disdnNI2CapabilitiesBE00A = _DisdnNI2CapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 126, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DisdnNI2MIB",
    **{"dataSigChanNi2": dataSigChanNi2,
       "dataSigChanNi2RowStatusTable": dataSigChanNi2RowStatusTable,
       "dataSigChanNi2RowStatusEntry": dataSigChanNi2RowStatusEntry,
       "dataSigChanNi2RowStatus": dataSigChanNi2RowStatus,
       "dataSigChanNi2ComponentName": dataSigChanNi2ComponentName,
       "dataSigChanNi2StorageType": dataSigChanNi2StorageType,
       "dataSigChanNi2Index": dataSigChanNi2Index,
       "dataSigChanNi2Framer": dataSigChanNi2Framer,
       "dataSigChanNi2FramerRowStatusTable": dataSigChanNi2FramerRowStatusTable,
       "dataSigChanNi2FramerRowStatusEntry": dataSigChanNi2FramerRowStatusEntry,
       "dataSigChanNi2FramerRowStatus": dataSigChanNi2FramerRowStatus,
       "dataSigChanNi2FramerComponentName": dataSigChanNi2FramerComponentName,
       "dataSigChanNi2FramerStorageType": dataSigChanNi2FramerStorageType,
       "dataSigChanNi2FramerIndex": dataSigChanNi2FramerIndex,
       "dataSigChanNi2FramerProvTable": dataSigChanNi2FramerProvTable,
       "dataSigChanNi2FramerProvEntry": dataSigChanNi2FramerProvEntry,
       "dataSigChanNi2FramerInterfaceName": dataSigChanNi2FramerInterfaceName,
       "dataSigChanNi2FramerStateTable": dataSigChanNi2FramerStateTable,
       "dataSigChanNi2FramerStateEntry": dataSigChanNi2FramerStateEntry,
       "dataSigChanNi2FramerAdminState": dataSigChanNi2FramerAdminState,
       "dataSigChanNi2FramerOperationalState": dataSigChanNi2FramerOperationalState,
       "dataSigChanNi2FramerUsageState": dataSigChanNi2FramerUsageState,
       "dataSigChanNi2FramerStatsTable": dataSigChanNi2FramerStatsTable,
       "dataSigChanNi2FramerStatsEntry": dataSigChanNi2FramerStatsEntry,
       "dataSigChanNi2FramerFrmToIf": dataSigChanNi2FramerFrmToIf,
       "dataSigChanNi2FramerFrmFromIf": dataSigChanNi2FramerFrmFromIf,
       "dataSigChanNi2FramerOctetFromIf": dataSigChanNi2FramerOctetFromIf,
       "dataSigChanNi2FramerAborts": dataSigChanNi2FramerAborts,
       "dataSigChanNi2FramerCrcErrors": dataSigChanNi2FramerCrcErrors,
       "dataSigChanNi2FramerLrcErrors": dataSigChanNi2FramerLrcErrors,
       "dataSigChanNi2FramerNonOctetErrors": dataSigChanNi2FramerNonOctetErrors,
       "dataSigChanNi2FramerOverruns": dataSigChanNi2FramerOverruns,
       "dataSigChanNi2FramerUnderruns": dataSigChanNi2FramerUnderruns,
       "dataSigChanNi2FramerLargeFrmErrors": dataSigChanNi2FramerLargeFrmErrors,
       "dataSigChanNi2L2Table": dataSigChanNi2L2Table,
       "dataSigChanNi2L2Entry": dataSigChanNi2L2Entry,
       "dataSigChanNi2T23": dataSigChanNi2T23,
       "dataSigChanNi2T200": dataSigChanNi2T200,
       "dataSigChanNi2N200": dataSigChanNi2N200,
       "dataSigChanNi2T203": dataSigChanNi2T203,
       "dataSigChanNi2N201": dataSigChanNi2N201,
       "dataSigChanNi2CircuitSwitchedK": dataSigChanNi2CircuitSwitchedK,
       "dataSigChanNi2ProvTable": dataSigChanNi2ProvTable,
       "dataSigChanNi2ProvEntry": dataSigChanNi2ProvEntry,
       "dataSigChanNi2Side": dataSigChanNi2Side,
       "dataSigChanNi2OperTable": dataSigChanNi2OperTable,
       "dataSigChanNi2OperEntry": dataSigChanNi2OperEntry,
       "dataSigChanNi2ActiveChannels": dataSigChanNi2ActiveChannels,
       "dataSigChanNi2PeakActiveChannels": dataSigChanNi2PeakActiveChannels,
       "dataSigChanNi2DChanStatus": dataSigChanNi2DChanStatus,
       "dataSigChanNi2ToolsTable": dataSigChanNi2ToolsTable,
       "dataSigChanNi2ToolsEntry": dataSigChanNi2ToolsEntry,
       "dataSigChanNi2Tracing": dataSigChanNi2Tracing,
       "disdnNI2MIB": disdnNI2MIB,
       "disdnNI2Group": disdnNI2Group,
       "disdnNI2GroupBE": disdnNI2GroupBE,
       "disdnNI2GroupBE00": disdnNI2GroupBE00,
       "disdnNI2GroupBE00A": disdnNI2GroupBE00A,
       "disdnNI2Capabilities": disdnNI2Capabilities,
       "disdnNI2CapabilitiesBE": disdnNI2CapabilitiesBE,
       "disdnNI2CapabilitiesBE00": disdnNI2CapabilitiesBE00,
       "disdnNI2CapabilitiesBE00A": disdnNI2CapabilitiesBE00A}
)
