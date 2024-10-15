# SNMP MIB module (Nortel-MsCarrier-MscPassport-DisdnNISMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DisdnNISMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:13 2024
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

(mscDataSigChan,
 mscDataSigChanIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-DataIsdnMIB",
    "mscDataSigChan",
    "mscDataSigChanIndex")

(DisplayString,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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

_MscDataSigChanNis_ObjectIdentity = ObjectIdentity
mscDataSigChanNis = _MscDataSigChanNis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13)
)
_MscDataSigChanNisRowStatusTable_Object = MibTable
mscDataSigChanNisRowStatusTable = _MscDataSigChanNisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanNisRowStatusTable.setStatus("mandatory")
_MscDataSigChanNisRowStatusEntry_Object = MibTableRow
mscDataSigChanNisRowStatusEntry = _MscDataSigChanNisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 1, 1)
)
mscDataSigChanNisRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNisRowStatusEntry.setStatus("mandatory")
_MscDataSigChanNisRowStatus_Type = RowStatus
_MscDataSigChanNisRowStatus_Object = MibTableColumn
mscDataSigChanNisRowStatus = _MscDataSigChanNisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 1, 1, 1),
    _MscDataSigChanNisRowStatus_Type()
)
mscDataSigChanNisRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisRowStatus.setStatus("mandatory")
_MscDataSigChanNisComponentName_Type = DisplayString
_MscDataSigChanNisComponentName_Object = MibTableColumn
mscDataSigChanNisComponentName = _MscDataSigChanNisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 1, 1, 2),
    _MscDataSigChanNisComponentName_Type()
)
mscDataSigChanNisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisComponentName.setStatus("mandatory")
_MscDataSigChanNisStorageType_Type = StorageType
_MscDataSigChanNisStorageType_Object = MibTableColumn
mscDataSigChanNisStorageType = _MscDataSigChanNisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 1, 1, 4),
    _MscDataSigChanNisStorageType_Type()
)
mscDataSigChanNisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisStorageType.setStatus("mandatory")
_MscDataSigChanNisIndex_Type = NonReplicated
_MscDataSigChanNisIndex_Object = MibTableColumn
mscDataSigChanNisIndex = _MscDataSigChanNisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 1, 1, 10),
    _MscDataSigChanNisIndex_Type()
)
mscDataSigChanNisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanNisIndex.setStatus("mandatory")
_MscDataSigChanNisFramer_ObjectIdentity = ObjectIdentity
mscDataSigChanNisFramer = _MscDataSigChanNisFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2)
)
_MscDataSigChanNisFramerRowStatusTable_Object = MibTable
mscDataSigChanNisFramerRowStatusTable = _MscDataSigChanNisFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerRowStatusTable.setStatus("mandatory")
_MscDataSigChanNisFramerRowStatusEntry_Object = MibTableRow
mscDataSigChanNisFramerRowStatusEntry = _MscDataSigChanNisFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 1, 1)
)
mscDataSigChanNisFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerRowStatusEntry.setStatus("mandatory")
_MscDataSigChanNisFramerRowStatus_Type = RowStatus
_MscDataSigChanNisFramerRowStatus_Object = MibTableColumn
mscDataSigChanNisFramerRowStatus = _MscDataSigChanNisFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 1, 1, 1),
    _MscDataSigChanNisFramerRowStatus_Type()
)
mscDataSigChanNisFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerRowStatus.setStatus("mandatory")
_MscDataSigChanNisFramerComponentName_Type = DisplayString
_MscDataSigChanNisFramerComponentName_Object = MibTableColumn
mscDataSigChanNisFramerComponentName = _MscDataSigChanNisFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 1, 1, 2),
    _MscDataSigChanNisFramerComponentName_Type()
)
mscDataSigChanNisFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerComponentName.setStatus("mandatory")
_MscDataSigChanNisFramerStorageType_Type = StorageType
_MscDataSigChanNisFramerStorageType_Object = MibTableColumn
mscDataSigChanNisFramerStorageType = _MscDataSigChanNisFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 1, 1, 4),
    _MscDataSigChanNisFramerStorageType_Type()
)
mscDataSigChanNisFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerStorageType.setStatus("mandatory")
_MscDataSigChanNisFramerIndex_Type = NonReplicated
_MscDataSigChanNisFramerIndex_Object = MibTableColumn
mscDataSigChanNisFramerIndex = _MscDataSigChanNisFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 1, 1, 10),
    _MscDataSigChanNisFramerIndex_Type()
)
mscDataSigChanNisFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerIndex.setStatus("mandatory")
_MscDataSigChanNisFramerProvTable_Object = MibTable
mscDataSigChanNisFramerProvTable = _MscDataSigChanNisFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 10)
)
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerProvTable.setStatus("mandatory")
_MscDataSigChanNisFramerProvEntry_Object = MibTableRow
mscDataSigChanNisFramerProvEntry = _MscDataSigChanNisFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 10, 1)
)
mscDataSigChanNisFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerProvEntry.setStatus("mandatory")
_MscDataSigChanNisFramerInterfaceName_Type = Link
_MscDataSigChanNisFramerInterfaceName_Object = MibTableColumn
mscDataSigChanNisFramerInterfaceName = _MscDataSigChanNisFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 10, 1, 1),
    _MscDataSigChanNisFramerInterfaceName_Type()
)
mscDataSigChanNisFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerInterfaceName.setStatus("mandatory")
_MscDataSigChanNisFramerStateTable_Object = MibTable
mscDataSigChanNisFramerStateTable = _MscDataSigChanNisFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 12)
)
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerStateTable.setStatus("mandatory")
_MscDataSigChanNisFramerStateEntry_Object = MibTableRow
mscDataSigChanNisFramerStateEntry = _MscDataSigChanNisFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 12, 1)
)
mscDataSigChanNisFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerStateEntry.setStatus("mandatory")


class _MscDataSigChanNisFramerAdminState_Type(Integer32):
    """Custom type mscDataSigChanNisFramerAdminState based on Integer32"""
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


_MscDataSigChanNisFramerAdminState_Type.__name__ = "Integer32"
_MscDataSigChanNisFramerAdminState_Object = MibTableColumn
mscDataSigChanNisFramerAdminState = _MscDataSigChanNisFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 12, 1, 1),
    _MscDataSigChanNisFramerAdminState_Type()
)
mscDataSigChanNisFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerAdminState.setStatus("mandatory")


class _MscDataSigChanNisFramerOperationalState_Type(Integer32):
    """Custom type mscDataSigChanNisFramerOperationalState based on Integer32"""
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


_MscDataSigChanNisFramerOperationalState_Type.__name__ = "Integer32"
_MscDataSigChanNisFramerOperationalState_Object = MibTableColumn
mscDataSigChanNisFramerOperationalState = _MscDataSigChanNisFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 12, 1, 2),
    _MscDataSigChanNisFramerOperationalState_Type()
)
mscDataSigChanNisFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerOperationalState.setStatus("mandatory")


class _MscDataSigChanNisFramerUsageState_Type(Integer32):
    """Custom type mscDataSigChanNisFramerUsageState based on Integer32"""
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


_MscDataSigChanNisFramerUsageState_Type.__name__ = "Integer32"
_MscDataSigChanNisFramerUsageState_Object = MibTableColumn
mscDataSigChanNisFramerUsageState = _MscDataSigChanNisFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 12, 1, 3),
    _MscDataSigChanNisFramerUsageState_Type()
)
mscDataSigChanNisFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerUsageState.setStatus("mandatory")
_MscDataSigChanNisFramerStatsTable_Object = MibTable
mscDataSigChanNisFramerStatsTable = _MscDataSigChanNisFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerStatsTable.setStatus("mandatory")
_MscDataSigChanNisFramerStatsEntry_Object = MibTableRow
mscDataSigChanNisFramerStatsEntry = _MscDataSigChanNisFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1)
)
mscDataSigChanNisFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerStatsEntry.setStatus("mandatory")


class _MscDataSigChanNisFramerFrmToIf_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerFrmToIf_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerFrmToIf_Object = MibTableColumn
mscDataSigChanNisFramerFrmToIf = _MscDataSigChanNisFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 1),
    _MscDataSigChanNisFramerFrmToIf_Type()
)
mscDataSigChanNisFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerFrmToIf.setStatus("mandatory")


class _MscDataSigChanNisFramerFrmFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerFrmFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerFrmFromIf_Object = MibTableColumn
mscDataSigChanNisFramerFrmFromIf = _MscDataSigChanNisFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 2),
    _MscDataSigChanNisFramerFrmFromIf_Type()
)
mscDataSigChanNisFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerFrmFromIf.setStatus("mandatory")


class _MscDataSigChanNisFramerOctetFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerOctetFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerOctetFromIf_Object = MibTableColumn
mscDataSigChanNisFramerOctetFromIf = _MscDataSigChanNisFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 3),
    _MscDataSigChanNisFramerOctetFromIf_Type()
)
mscDataSigChanNisFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerOctetFromIf.setStatus("mandatory")


class _MscDataSigChanNisFramerAborts_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerAborts_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerAborts_Object = MibTableColumn
mscDataSigChanNisFramerAborts = _MscDataSigChanNisFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 4),
    _MscDataSigChanNisFramerAborts_Type()
)
mscDataSigChanNisFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerAborts.setStatus("mandatory")


class _MscDataSigChanNisFramerCrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerCrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerCrcErrors_Object = MibTableColumn
mscDataSigChanNisFramerCrcErrors = _MscDataSigChanNisFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 5),
    _MscDataSigChanNisFramerCrcErrors_Type()
)
mscDataSigChanNisFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerCrcErrors.setStatus("mandatory")


class _MscDataSigChanNisFramerLrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerLrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerLrcErrors_Object = MibTableColumn
mscDataSigChanNisFramerLrcErrors = _MscDataSigChanNisFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 6),
    _MscDataSigChanNisFramerLrcErrors_Type()
)
mscDataSigChanNisFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerLrcErrors.setStatus("mandatory")


class _MscDataSigChanNisFramerNonOctetErrors_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerNonOctetErrors_Object = MibTableColumn
mscDataSigChanNisFramerNonOctetErrors = _MscDataSigChanNisFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 7),
    _MscDataSigChanNisFramerNonOctetErrors_Type()
)
mscDataSigChanNisFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerNonOctetErrors.setStatus("mandatory")


class _MscDataSigChanNisFramerOverruns_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerOverruns_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerOverruns_Object = MibTableColumn
mscDataSigChanNisFramerOverruns = _MscDataSigChanNisFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 8),
    _MscDataSigChanNisFramerOverruns_Type()
)
mscDataSigChanNisFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerOverruns.setStatus("mandatory")


class _MscDataSigChanNisFramerUnderruns_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerUnderruns_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerUnderruns_Object = MibTableColumn
mscDataSigChanNisFramerUnderruns = _MscDataSigChanNisFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 9),
    _MscDataSigChanNisFramerUnderruns_Type()
)
mscDataSigChanNisFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerUnderruns.setStatus("mandatory")


class _MscDataSigChanNisFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type mscDataSigChanNisFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNisFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanNisFramerLargeFrmErrors_Object = MibTableColumn
mscDataSigChanNisFramerLargeFrmErrors = _MscDataSigChanNisFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 2, 13, 1, 10),
    _MscDataSigChanNisFramerLargeFrmErrors_Type()
)
mscDataSigChanNisFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisFramerLargeFrmErrors.setStatus("mandatory")
_MscDataSigChanNisL2Table_Object = MibTable
mscDataSigChanNisL2Table = _MscDataSigChanNisL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 11)
)
if mibBuilder.loadTexts:
    mscDataSigChanNisL2Table.setStatus("mandatory")
_MscDataSigChanNisL2Entry_Object = MibTableRow
mscDataSigChanNisL2Entry = _MscDataSigChanNisL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 11, 1)
)
mscDataSigChanNisL2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNisL2Entry.setStatus("mandatory")


class _MscDataSigChanNisT23_Type(Unsigned32):
    """Custom type mscDataSigChanNisT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscDataSigChanNisT23_Type.__name__ = "Unsigned32"
_MscDataSigChanNisT23_Object = MibTableColumn
mscDataSigChanNisT23 = _MscDataSigChanNisT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 11, 1, 1),
    _MscDataSigChanNisT23_Type()
)
mscDataSigChanNisT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisT23.setStatus("mandatory")


class _MscDataSigChanNisT200_Type(Unsigned32):
    """Custom type mscDataSigChanNisT200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscDataSigChanNisT200_Type.__name__ = "Unsigned32"
_MscDataSigChanNisT200_Object = MibTableColumn
mscDataSigChanNisT200 = _MscDataSigChanNisT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 11, 1, 2),
    _MscDataSigChanNisT200_Type()
)
mscDataSigChanNisT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisT200.setStatus("mandatory")


class _MscDataSigChanNisN200_Type(Unsigned32):
    """Custom type mscDataSigChanNisN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscDataSigChanNisN200_Type.__name__ = "Unsigned32"
_MscDataSigChanNisN200_Object = MibTableColumn
mscDataSigChanNisN200 = _MscDataSigChanNisN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 11, 1, 3),
    _MscDataSigChanNisN200_Type()
)
mscDataSigChanNisN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisN200.setStatus("mandatory")


class _MscDataSigChanNisT203_Type(Unsigned32):
    """Custom type mscDataSigChanNisT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_MscDataSigChanNisT203_Type.__name__ = "Unsigned32"
_MscDataSigChanNisT203_Object = MibTableColumn
mscDataSigChanNisT203 = _MscDataSigChanNisT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 11, 1, 4),
    _MscDataSigChanNisT203_Type()
)
mscDataSigChanNisT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisT203.setStatus("mandatory")


class _MscDataSigChanNisN201_Type(Unsigned32):
    """Custom type mscDataSigChanNisN201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_MscDataSigChanNisN201_Type.__name__ = "Unsigned32"
_MscDataSigChanNisN201_Object = MibTableColumn
mscDataSigChanNisN201 = _MscDataSigChanNisN201_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 11, 1, 5),
    _MscDataSigChanNisN201_Type()
)
mscDataSigChanNisN201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisN201.setStatus("mandatory")


class _MscDataSigChanNisCircuitSwitchedK_Type(Unsigned32):
    """Custom type mscDataSigChanNisCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_MscDataSigChanNisCircuitSwitchedK_Type.__name__ = "Unsigned32"
_MscDataSigChanNisCircuitSwitchedK_Object = MibTableColumn
mscDataSigChanNisCircuitSwitchedK = _MscDataSigChanNisCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 11, 1, 6),
    _MscDataSigChanNisCircuitSwitchedK_Type()
)
mscDataSigChanNisCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisCircuitSwitchedK.setStatus("mandatory")
_MscDataSigChanNisProvTable_Object = MibTable
mscDataSigChanNisProvTable = _MscDataSigChanNisProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanNisProvTable.setStatus("mandatory")
_MscDataSigChanNisProvEntry_Object = MibTableRow
mscDataSigChanNisProvEntry = _MscDataSigChanNisProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 13, 1)
)
mscDataSigChanNisProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNisProvEntry.setStatus("mandatory")


class _MscDataSigChanNisSide_Type(Integer32):
    """Custom type mscDataSigChanNisSide based on Integer32"""
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


_MscDataSigChanNisSide_Type.__name__ = "Integer32"
_MscDataSigChanNisSide_Object = MibTableColumn
mscDataSigChanNisSide = _MscDataSigChanNisSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 13, 1, 1),
    _MscDataSigChanNisSide_Type()
)
mscDataSigChanNisSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisSide.setStatus("mandatory")
_MscDataSigChanNisOperTable_Object = MibTable
mscDataSigChanNisOperTable = _MscDataSigChanNisOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 15)
)
if mibBuilder.loadTexts:
    mscDataSigChanNisOperTable.setStatus("mandatory")
_MscDataSigChanNisOperEntry_Object = MibTableRow
mscDataSigChanNisOperEntry = _MscDataSigChanNisOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 15, 1)
)
mscDataSigChanNisOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNisOperEntry.setStatus("mandatory")


class _MscDataSigChanNisActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanNisActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanNisActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanNisActiveChannels_Object = MibTableColumn
mscDataSigChanNisActiveChannels = _MscDataSigChanNisActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 15, 1, 1),
    _MscDataSigChanNisActiveChannels_Type()
)
mscDataSigChanNisActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisActiveChannels.setStatus("mandatory")


class _MscDataSigChanNisPeakActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanNisPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanNisPeakActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanNisPeakActiveChannels_Object = MibTableColumn
mscDataSigChanNisPeakActiveChannels = _MscDataSigChanNisPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 15, 1, 4),
    _MscDataSigChanNisPeakActiveChannels_Type()
)
mscDataSigChanNisPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisPeakActiveChannels.setStatus("mandatory")


class _MscDataSigChanNisDChanStatus_Type(Integer32):
    """Custom type mscDataSigChanNisDChanStatus based on Integer32"""
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


_MscDataSigChanNisDChanStatus_Type.__name__ = "Integer32"
_MscDataSigChanNisDChanStatus_Object = MibTableColumn
mscDataSigChanNisDChanStatus = _MscDataSigChanNisDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 15, 1, 7),
    _MscDataSigChanNisDChanStatus_Type()
)
mscDataSigChanNisDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNisDChanStatus.setStatus("mandatory")
_MscDataSigChanNisToolsTable_Object = MibTable
mscDataSigChanNisToolsTable = _MscDataSigChanNisToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 16)
)
if mibBuilder.loadTexts:
    mscDataSigChanNisToolsTable.setStatus("mandatory")
_MscDataSigChanNisToolsEntry_Object = MibTableRow
mscDataSigChanNisToolsEntry = _MscDataSigChanNisToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 16, 1)
)
mscDataSigChanNisToolsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNISMIB", "mscDataSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNisToolsEntry.setStatus("mandatory")


class _MscDataSigChanNisTracing_Type(OctetString):
    """Custom type mscDataSigChanNisTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDataSigChanNisTracing_Type.__name__ = "OctetString"
_MscDataSigChanNisTracing_Object = MibTableColumn
mscDataSigChanNisTracing = _MscDataSigChanNisTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 13, 16, 1, 1),
    _MscDataSigChanNisTracing_Type()
)
mscDataSigChanNisTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNisTracing.setStatus("mandatory")
_DisdnNISMIB_ObjectIdentity = ObjectIdentity
disdnNISMIB = _DisdnNISMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 127)
)
_DisdnNISGroup_ObjectIdentity = ObjectIdentity
disdnNISGroup = _DisdnNISGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 127, 1)
)
_DisdnNISGroupCA_ObjectIdentity = ObjectIdentity
disdnNISGroupCA = _DisdnNISGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 127, 1, 1)
)
_DisdnNISGroupCA02_ObjectIdentity = ObjectIdentity
disdnNISGroupCA02 = _DisdnNISGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 127, 1, 1, 3)
)
_DisdnNISGroupCA02A_ObjectIdentity = ObjectIdentity
disdnNISGroupCA02A = _DisdnNISGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 127, 1, 1, 3, 2)
)
_DisdnNISCapabilities_ObjectIdentity = ObjectIdentity
disdnNISCapabilities = _DisdnNISCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 127, 3)
)
_DisdnNISCapabilitiesCA_ObjectIdentity = ObjectIdentity
disdnNISCapabilitiesCA = _DisdnNISCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 127, 3, 1)
)
_DisdnNISCapabilitiesCA02_ObjectIdentity = ObjectIdentity
disdnNISCapabilitiesCA02 = _DisdnNISCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 127, 3, 1, 3)
)
_DisdnNISCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
disdnNISCapabilitiesCA02A = _DisdnNISCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 127, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DisdnNISMIB",
    **{"mscDataSigChanNis": mscDataSigChanNis,
       "mscDataSigChanNisRowStatusTable": mscDataSigChanNisRowStatusTable,
       "mscDataSigChanNisRowStatusEntry": mscDataSigChanNisRowStatusEntry,
       "mscDataSigChanNisRowStatus": mscDataSigChanNisRowStatus,
       "mscDataSigChanNisComponentName": mscDataSigChanNisComponentName,
       "mscDataSigChanNisStorageType": mscDataSigChanNisStorageType,
       "mscDataSigChanNisIndex": mscDataSigChanNisIndex,
       "mscDataSigChanNisFramer": mscDataSigChanNisFramer,
       "mscDataSigChanNisFramerRowStatusTable": mscDataSigChanNisFramerRowStatusTable,
       "mscDataSigChanNisFramerRowStatusEntry": mscDataSigChanNisFramerRowStatusEntry,
       "mscDataSigChanNisFramerRowStatus": mscDataSigChanNisFramerRowStatus,
       "mscDataSigChanNisFramerComponentName": mscDataSigChanNisFramerComponentName,
       "mscDataSigChanNisFramerStorageType": mscDataSigChanNisFramerStorageType,
       "mscDataSigChanNisFramerIndex": mscDataSigChanNisFramerIndex,
       "mscDataSigChanNisFramerProvTable": mscDataSigChanNisFramerProvTable,
       "mscDataSigChanNisFramerProvEntry": mscDataSigChanNisFramerProvEntry,
       "mscDataSigChanNisFramerInterfaceName": mscDataSigChanNisFramerInterfaceName,
       "mscDataSigChanNisFramerStateTable": mscDataSigChanNisFramerStateTable,
       "mscDataSigChanNisFramerStateEntry": mscDataSigChanNisFramerStateEntry,
       "mscDataSigChanNisFramerAdminState": mscDataSigChanNisFramerAdminState,
       "mscDataSigChanNisFramerOperationalState": mscDataSigChanNisFramerOperationalState,
       "mscDataSigChanNisFramerUsageState": mscDataSigChanNisFramerUsageState,
       "mscDataSigChanNisFramerStatsTable": mscDataSigChanNisFramerStatsTable,
       "mscDataSigChanNisFramerStatsEntry": mscDataSigChanNisFramerStatsEntry,
       "mscDataSigChanNisFramerFrmToIf": mscDataSigChanNisFramerFrmToIf,
       "mscDataSigChanNisFramerFrmFromIf": mscDataSigChanNisFramerFrmFromIf,
       "mscDataSigChanNisFramerOctetFromIf": mscDataSigChanNisFramerOctetFromIf,
       "mscDataSigChanNisFramerAborts": mscDataSigChanNisFramerAborts,
       "mscDataSigChanNisFramerCrcErrors": mscDataSigChanNisFramerCrcErrors,
       "mscDataSigChanNisFramerLrcErrors": mscDataSigChanNisFramerLrcErrors,
       "mscDataSigChanNisFramerNonOctetErrors": mscDataSigChanNisFramerNonOctetErrors,
       "mscDataSigChanNisFramerOverruns": mscDataSigChanNisFramerOverruns,
       "mscDataSigChanNisFramerUnderruns": mscDataSigChanNisFramerUnderruns,
       "mscDataSigChanNisFramerLargeFrmErrors": mscDataSigChanNisFramerLargeFrmErrors,
       "mscDataSigChanNisL2Table": mscDataSigChanNisL2Table,
       "mscDataSigChanNisL2Entry": mscDataSigChanNisL2Entry,
       "mscDataSigChanNisT23": mscDataSigChanNisT23,
       "mscDataSigChanNisT200": mscDataSigChanNisT200,
       "mscDataSigChanNisN200": mscDataSigChanNisN200,
       "mscDataSigChanNisT203": mscDataSigChanNisT203,
       "mscDataSigChanNisN201": mscDataSigChanNisN201,
       "mscDataSigChanNisCircuitSwitchedK": mscDataSigChanNisCircuitSwitchedK,
       "mscDataSigChanNisProvTable": mscDataSigChanNisProvTable,
       "mscDataSigChanNisProvEntry": mscDataSigChanNisProvEntry,
       "mscDataSigChanNisSide": mscDataSigChanNisSide,
       "mscDataSigChanNisOperTable": mscDataSigChanNisOperTable,
       "mscDataSigChanNisOperEntry": mscDataSigChanNisOperEntry,
       "mscDataSigChanNisActiveChannels": mscDataSigChanNisActiveChannels,
       "mscDataSigChanNisPeakActiveChannels": mscDataSigChanNisPeakActiveChannels,
       "mscDataSigChanNisDChanStatus": mscDataSigChanNisDChanStatus,
       "mscDataSigChanNisToolsTable": mscDataSigChanNisToolsTable,
       "mscDataSigChanNisToolsEntry": mscDataSigChanNisToolsEntry,
       "mscDataSigChanNisTracing": mscDataSigChanNisTracing,
       "disdnNISMIB": disdnNISMIB,
       "disdnNISGroup": disdnNISGroup,
       "disdnNISGroupCA": disdnNISGroupCA,
       "disdnNISGroupCA02": disdnNISGroupCA02,
       "disdnNISGroupCA02A": disdnNISGroupCA02A,
       "disdnNISCapabilities": disdnNISCapabilities,
       "disdnNISCapabilitiesCA": disdnNISCapabilitiesCA,
       "disdnNISCapabilitiesCA02": disdnNISCapabilitiesCA02,
       "disdnNISCapabilitiesCA02A": disdnNISCapabilitiesCA02A}
)
