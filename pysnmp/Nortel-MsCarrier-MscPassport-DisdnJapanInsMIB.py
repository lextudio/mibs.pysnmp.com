# SNMP MIB module (Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:11 2024
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

_MscDataSigChanIns_ObjectIdentity = ObjectIdentity
mscDataSigChanIns = _MscDataSigChanIns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11)
)
_MscDataSigChanInsRowStatusTable_Object = MibTable
mscDataSigChanInsRowStatusTable = _MscDataSigChanInsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanInsRowStatusTable.setStatus("mandatory")
_MscDataSigChanInsRowStatusEntry_Object = MibTableRow
mscDataSigChanInsRowStatusEntry = _MscDataSigChanInsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1)
)
mscDataSigChanInsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanInsRowStatusEntry.setStatus("mandatory")
_MscDataSigChanInsRowStatus_Type = RowStatus
_MscDataSigChanInsRowStatus_Object = MibTableColumn
mscDataSigChanInsRowStatus = _MscDataSigChanInsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1, 1),
    _MscDataSigChanInsRowStatus_Type()
)
mscDataSigChanInsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsRowStatus.setStatus("mandatory")
_MscDataSigChanInsComponentName_Type = DisplayString
_MscDataSigChanInsComponentName_Object = MibTableColumn
mscDataSigChanInsComponentName = _MscDataSigChanInsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1, 2),
    _MscDataSigChanInsComponentName_Type()
)
mscDataSigChanInsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsComponentName.setStatus("mandatory")
_MscDataSigChanInsStorageType_Type = StorageType
_MscDataSigChanInsStorageType_Object = MibTableColumn
mscDataSigChanInsStorageType = _MscDataSigChanInsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1, 4),
    _MscDataSigChanInsStorageType_Type()
)
mscDataSigChanInsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsStorageType.setStatus("mandatory")
_MscDataSigChanInsIndex_Type = NonReplicated
_MscDataSigChanInsIndex_Object = MibTableColumn
mscDataSigChanInsIndex = _MscDataSigChanInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 1, 1, 10),
    _MscDataSigChanInsIndex_Type()
)
mscDataSigChanInsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanInsIndex.setStatus("mandatory")
_MscDataSigChanInsFramer_ObjectIdentity = ObjectIdentity
mscDataSigChanInsFramer = _MscDataSigChanInsFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2)
)
_MscDataSigChanInsFramerRowStatusTable_Object = MibTable
mscDataSigChanInsFramerRowStatusTable = _MscDataSigChanInsFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerRowStatusTable.setStatus("mandatory")
_MscDataSigChanInsFramerRowStatusEntry_Object = MibTableRow
mscDataSigChanInsFramerRowStatusEntry = _MscDataSigChanInsFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1)
)
mscDataSigChanInsFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerRowStatusEntry.setStatus("mandatory")
_MscDataSigChanInsFramerRowStatus_Type = RowStatus
_MscDataSigChanInsFramerRowStatus_Object = MibTableColumn
mscDataSigChanInsFramerRowStatus = _MscDataSigChanInsFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1, 1),
    _MscDataSigChanInsFramerRowStatus_Type()
)
mscDataSigChanInsFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerRowStatus.setStatus("mandatory")
_MscDataSigChanInsFramerComponentName_Type = DisplayString
_MscDataSigChanInsFramerComponentName_Object = MibTableColumn
mscDataSigChanInsFramerComponentName = _MscDataSigChanInsFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1, 2),
    _MscDataSigChanInsFramerComponentName_Type()
)
mscDataSigChanInsFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerComponentName.setStatus("mandatory")
_MscDataSigChanInsFramerStorageType_Type = StorageType
_MscDataSigChanInsFramerStorageType_Object = MibTableColumn
mscDataSigChanInsFramerStorageType = _MscDataSigChanInsFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1, 4),
    _MscDataSigChanInsFramerStorageType_Type()
)
mscDataSigChanInsFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerStorageType.setStatus("mandatory")
_MscDataSigChanInsFramerIndex_Type = NonReplicated
_MscDataSigChanInsFramerIndex_Object = MibTableColumn
mscDataSigChanInsFramerIndex = _MscDataSigChanInsFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 1, 1, 10),
    _MscDataSigChanInsFramerIndex_Type()
)
mscDataSigChanInsFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerIndex.setStatus("mandatory")
_MscDataSigChanInsFramerProvTable_Object = MibTable
mscDataSigChanInsFramerProvTable = _MscDataSigChanInsFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 10)
)
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerProvTable.setStatus("mandatory")
_MscDataSigChanInsFramerProvEntry_Object = MibTableRow
mscDataSigChanInsFramerProvEntry = _MscDataSigChanInsFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 10, 1)
)
mscDataSigChanInsFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerProvEntry.setStatus("mandatory")
_MscDataSigChanInsFramerInterfaceName_Type = Link
_MscDataSigChanInsFramerInterfaceName_Object = MibTableColumn
mscDataSigChanInsFramerInterfaceName = _MscDataSigChanInsFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 10, 1, 1),
    _MscDataSigChanInsFramerInterfaceName_Type()
)
mscDataSigChanInsFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerInterfaceName.setStatus("mandatory")
_MscDataSigChanInsFramerStateTable_Object = MibTable
mscDataSigChanInsFramerStateTable = _MscDataSigChanInsFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12)
)
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerStateTable.setStatus("mandatory")
_MscDataSigChanInsFramerStateEntry_Object = MibTableRow
mscDataSigChanInsFramerStateEntry = _MscDataSigChanInsFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12, 1)
)
mscDataSigChanInsFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerStateEntry.setStatus("mandatory")


class _MscDataSigChanInsFramerAdminState_Type(Integer32):
    """Custom type mscDataSigChanInsFramerAdminState based on Integer32"""
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


_MscDataSigChanInsFramerAdminState_Type.__name__ = "Integer32"
_MscDataSigChanInsFramerAdminState_Object = MibTableColumn
mscDataSigChanInsFramerAdminState = _MscDataSigChanInsFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12, 1, 1),
    _MscDataSigChanInsFramerAdminState_Type()
)
mscDataSigChanInsFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerAdminState.setStatus("mandatory")


class _MscDataSigChanInsFramerOperationalState_Type(Integer32):
    """Custom type mscDataSigChanInsFramerOperationalState based on Integer32"""
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


_MscDataSigChanInsFramerOperationalState_Type.__name__ = "Integer32"
_MscDataSigChanInsFramerOperationalState_Object = MibTableColumn
mscDataSigChanInsFramerOperationalState = _MscDataSigChanInsFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12, 1, 2),
    _MscDataSigChanInsFramerOperationalState_Type()
)
mscDataSigChanInsFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerOperationalState.setStatus("mandatory")


class _MscDataSigChanInsFramerUsageState_Type(Integer32):
    """Custom type mscDataSigChanInsFramerUsageState based on Integer32"""
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


_MscDataSigChanInsFramerUsageState_Type.__name__ = "Integer32"
_MscDataSigChanInsFramerUsageState_Object = MibTableColumn
mscDataSigChanInsFramerUsageState = _MscDataSigChanInsFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 12, 1, 3),
    _MscDataSigChanInsFramerUsageState_Type()
)
mscDataSigChanInsFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerUsageState.setStatus("mandatory")
_MscDataSigChanInsFramerStatsTable_Object = MibTable
mscDataSigChanInsFramerStatsTable = _MscDataSigChanInsFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerStatsTable.setStatus("mandatory")
_MscDataSigChanInsFramerStatsEntry_Object = MibTableRow
mscDataSigChanInsFramerStatsEntry = _MscDataSigChanInsFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1)
)
mscDataSigChanInsFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerStatsEntry.setStatus("mandatory")


class _MscDataSigChanInsFramerFrmToIf_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerFrmToIf_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerFrmToIf_Object = MibTableColumn
mscDataSigChanInsFramerFrmToIf = _MscDataSigChanInsFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 1),
    _MscDataSigChanInsFramerFrmToIf_Type()
)
mscDataSigChanInsFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerFrmToIf.setStatus("mandatory")


class _MscDataSigChanInsFramerFrmFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerFrmFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerFrmFromIf_Object = MibTableColumn
mscDataSigChanInsFramerFrmFromIf = _MscDataSigChanInsFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 2),
    _MscDataSigChanInsFramerFrmFromIf_Type()
)
mscDataSigChanInsFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerFrmFromIf.setStatus("mandatory")


class _MscDataSigChanInsFramerOctetFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerOctetFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerOctetFromIf_Object = MibTableColumn
mscDataSigChanInsFramerOctetFromIf = _MscDataSigChanInsFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 3),
    _MscDataSigChanInsFramerOctetFromIf_Type()
)
mscDataSigChanInsFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerOctetFromIf.setStatus("mandatory")


class _MscDataSigChanInsFramerAborts_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerAborts_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerAborts_Object = MibTableColumn
mscDataSigChanInsFramerAborts = _MscDataSigChanInsFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 4),
    _MscDataSigChanInsFramerAborts_Type()
)
mscDataSigChanInsFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerAborts.setStatus("mandatory")


class _MscDataSigChanInsFramerCrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerCrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerCrcErrors_Object = MibTableColumn
mscDataSigChanInsFramerCrcErrors = _MscDataSigChanInsFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 5),
    _MscDataSigChanInsFramerCrcErrors_Type()
)
mscDataSigChanInsFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerCrcErrors.setStatus("mandatory")


class _MscDataSigChanInsFramerLrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerLrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerLrcErrors_Object = MibTableColumn
mscDataSigChanInsFramerLrcErrors = _MscDataSigChanInsFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 6),
    _MscDataSigChanInsFramerLrcErrors_Type()
)
mscDataSigChanInsFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerLrcErrors.setStatus("mandatory")


class _MscDataSigChanInsFramerNonOctetErrors_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerNonOctetErrors_Object = MibTableColumn
mscDataSigChanInsFramerNonOctetErrors = _MscDataSigChanInsFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 7),
    _MscDataSigChanInsFramerNonOctetErrors_Type()
)
mscDataSigChanInsFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerNonOctetErrors.setStatus("mandatory")


class _MscDataSigChanInsFramerOverruns_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerOverruns_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerOverruns_Object = MibTableColumn
mscDataSigChanInsFramerOverruns = _MscDataSigChanInsFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 8),
    _MscDataSigChanInsFramerOverruns_Type()
)
mscDataSigChanInsFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerOverruns.setStatus("mandatory")


class _MscDataSigChanInsFramerUnderruns_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerUnderruns_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerUnderruns_Object = MibTableColumn
mscDataSigChanInsFramerUnderruns = _MscDataSigChanInsFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 9),
    _MscDataSigChanInsFramerUnderruns_Type()
)
mscDataSigChanInsFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerUnderruns.setStatus("mandatory")


class _MscDataSigChanInsFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type mscDataSigChanInsFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanInsFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanInsFramerLargeFrmErrors_Object = MibTableColumn
mscDataSigChanInsFramerLargeFrmErrors = _MscDataSigChanInsFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 2, 13, 1, 10),
    _MscDataSigChanInsFramerLargeFrmErrors_Type()
)
mscDataSigChanInsFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsFramerLargeFrmErrors.setStatus("mandatory")
_MscDataSigChanInsL2Table_Object = MibTable
mscDataSigChanInsL2Table = _MscDataSigChanInsL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11)
)
if mibBuilder.loadTexts:
    mscDataSigChanInsL2Table.setStatus("mandatory")
_MscDataSigChanInsL2Entry_Object = MibTableRow
mscDataSigChanInsL2Entry = _MscDataSigChanInsL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1)
)
mscDataSigChanInsL2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanInsL2Entry.setStatus("mandatory")


class _MscDataSigChanInsT23_Type(Unsigned32):
    """Custom type mscDataSigChanInsT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscDataSigChanInsT23_Type.__name__ = "Unsigned32"
_MscDataSigChanInsT23_Object = MibTableColumn
mscDataSigChanInsT23 = _MscDataSigChanInsT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 1),
    _MscDataSigChanInsT23_Type()
)
mscDataSigChanInsT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsT23.setStatus("mandatory")


class _MscDataSigChanInsT200_Type(Unsigned32):
    """Custom type mscDataSigChanInsT200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscDataSigChanInsT200_Type.__name__ = "Unsigned32"
_MscDataSigChanInsT200_Object = MibTableColumn
mscDataSigChanInsT200 = _MscDataSigChanInsT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 2),
    _MscDataSigChanInsT200_Type()
)
mscDataSigChanInsT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsT200.setStatus("mandatory")


class _MscDataSigChanInsN200_Type(Unsigned32):
    """Custom type mscDataSigChanInsN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscDataSigChanInsN200_Type.__name__ = "Unsigned32"
_MscDataSigChanInsN200_Object = MibTableColumn
mscDataSigChanInsN200 = _MscDataSigChanInsN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 3),
    _MscDataSigChanInsN200_Type()
)
mscDataSigChanInsN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsN200.setStatus("mandatory")


class _MscDataSigChanInsT203_Type(Unsigned32):
    """Custom type mscDataSigChanInsT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_MscDataSigChanInsT203_Type.__name__ = "Unsigned32"
_MscDataSigChanInsT203_Object = MibTableColumn
mscDataSigChanInsT203 = _MscDataSigChanInsT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 4),
    _MscDataSigChanInsT203_Type()
)
mscDataSigChanInsT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsT203.setStatus("mandatory")


class _MscDataSigChanInsN201_Type(Unsigned32):
    """Custom type mscDataSigChanInsN201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_MscDataSigChanInsN201_Type.__name__ = "Unsigned32"
_MscDataSigChanInsN201_Object = MibTableColumn
mscDataSigChanInsN201 = _MscDataSigChanInsN201_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 5),
    _MscDataSigChanInsN201_Type()
)
mscDataSigChanInsN201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsN201.setStatus("mandatory")


class _MscDataSigChanInsCircuitSwitchedK_Type(Unsigned32):
    """Custom type mscDataSigChanInsCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_MscDataSigChanInsCircuitSwitchedK_Type.__name__ = "Unsigned32"
_MscDataSigChanInsCircuitSwitchedK_Object = MibTableColumn
mscDataSigChanInsCircuitSwitchedK = _MscDataSigChanInsCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 11, 1, 6),
    _MscDataSigChanInsCircuitSwitchedK_Type()
)
mscDataSigChanInsCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsCircuitSwitchedK.setStatus("mandatory")
_MscDataSigChanInsProvTable_Object = MibTable
mscDataSigChanInsProvTable = _MscDataSigChanInsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanInsProvTable.setStatus("mandatory")
_MscDataSigChanInsProvEntry_Object = MibTableRow
mscDataSigChanInsProvEntry = _MscDataSigChanInsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 13, 1)
)
mscDataSigChanInsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanInsProvEntry.setStatus("mandatory")


class _MscDataSigChanInsSide_Type(Integer32):
    """Custom type mscDataSigChanInsSide based on Integer32"""
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


_MscDataSigChanInsSide_Type.__name__ = "Integer32"
_MscDataSigChanInsSide_Object = MibTableColumn
mscDataSigChanInsSide = _MscDataSigChanInsSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 13, 1, 1),
    _MscDataSigChanInsSide_Type()
)
mscDataSigChanInsSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsSide.setStatus("mandatory")
_MscDataSigChanInsOperTable_Object = MibTable
mscDataSigChanInsOperTable = _MscDataSigChanInsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15)
)
if mibBuilder.loadTexts:
    mscDataSigChanInsOperTable.setStatus("mandatory")
_MscDataSigChanInsOperEntry_Object = MibTableRow
mscDataSigChanInsOperEntry = _MscDataSigChanInsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15, 1)
)
mscDataSigChanInsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanInsOperEntry.setStatus("mandatory")


class _MscDataSigChanInsActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanInsActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanInsActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanInsActiveChannels_Object = MibTableColumn
mscDataSigChanInsActiveChannels = _MscDataSigChanInsActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15, 1, 1),
    _MscDataSigChanInsActiveChannels_Type()
)
mscDataSigChanInsActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsActiveChannels.setStatus("mandatory")


class _MscDataSigChanInsPeakActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanInsPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanInsPeakActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanInsPeakActiveChannels_Object = MibTableColumn
mscDataSigChanInsPeakActiveChannels = _MscDataSigChanInsPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15, 1, 4),
    _MscDataSigChanInsPeakActiveChannels_Type()
)
mscDataSigChanInsPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsPeakActiveChannels.setStatus("mandatory")


class _MscDataSigChanInsDChanStatus_Type(Integer32):
    """Custom type mscDataSigChanInsDChanStatus based on Integer32"""
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


_MscDataSigChanInsDChanStatus_Type.__name__ = "Integer32"
_MscDataSigChanInsDChanStatus_Object = MibTableColumn
mscDataSigChanInsDChanStatus = _MscDataSigChanInsDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 15, 1, 7),
    _MscDataSigChanInsDChanStatus_Type()
)
mscDataSigChanInsDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanInsDChanStatus.setStatus("mandatory")
_MscDataSigChanInsToolsTable_Object = MibTable
mscDataSigChanInsToolsTable = _MscDataSigChanInsToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 16)
)
if mibBuilder.loadTexts:
    mscDataSigChanInsToolsTable.setStatus("mandatory")
_MscDataSigChanInsToolsEntry_Object = MibTableRow
mscDataSigChanInsToolsEntry = _MscDataSigChanInsToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 16, 1)
)
mscDataSigChanInsToolsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB", "mscDataSigChanInsIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanInsToolsEntry.setStatus("mandatory")


class _MscDataSigChanInsTracing_Type(OctetString):
    """Custom type mscDataSigChanInsTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDataSigChanInsTracing_Type.__name__ = "OctetString"
_MscDataSigChanInsTracing_Object = MibTableColumn
mscDataSigChanInsTracing = _MscDataSigChanInsTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 11, 16, 1, 1),
    _MscDataSigChanInsTracing_Type()
)
mscDataSigChanInsTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanInsTracing.setStatus("mandatory")
_DisdnJapanInsMIB_ObjectIdentity = ObjectIdentity
disdnJapanInsMIB = _DisdnJapanInsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118)
)
_DisdnJapanInsGroup_ObjectIdentity = ObjectIdentity
disdnJapanInsGroup = _DisdnJapanInsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 1)
)
_DisdnJapanInsGroupCA_ObjectIdentity = ObjectIdentity
disdnJapanInsGroupCA = _DisdnJapanInsGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 1, 1)
)
_DisdnJapanInsGroupCA02_ObjectIdentity = ObjectIdentity
disdnJapanInsGroupCA02 = _DisdnJapanInsGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 1, 1, 3)
)
_DisdnJapanInsGroupCA02A_ObjectIdentity = ObjectIdentity
disdnJapanInsGroupCA02A = _DisdnJapanInsGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 1, 1, 3, 2)
)
_DisdnJapanInsCapabilities_ObjectIdentity = ObjectIdentity
disdnJapanInsCapabilities = _DisdnJapanInsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 3)
)
_DisdnJapanInsCapabilitiesCA_ObjectIdentity = ObjectIdentity
disdnJapanInsCapabilitiesCA = _DisdnJapanInsCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 3, 1)
)
_DisdnJapanInsCapabilitiesCA02_ObjectIdentity = ObjectIdentity
disdnJapanInsCapabilitiesCA02 = _DisdnJapanInsCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 3, 1, 3)
)
_DisdnJapanInsCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
disdnJapanInsCapabilitiesCA02A = _DisdnJapanInsCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 118, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DisdnJapanInsMIB",
    **{"mscDataSigChanIns": mscDataSigChanIns,
       "mscDataSigChanInsRowStatusTable": mscDataSigChanInsRowStatusTable,
       "mscDataSigChanInsRowStatusEntry": mscDataSigChanInsRowStatusEntry,
       "mscDataSigChanInsRowStatus": mscDataSigChanInsRowStatus,
       "mscDataSigChanInsComponentName": mscDataSigChanInsComponentName,
       "mscDataSigChanInsStorageType": mscDataSigChanInsStorageType,
       "mscDataSigChanInsIndex": mscDataSigChanInsIndex,
       "mscDataSigChanInsFramer": mscDataSigChanInsFramer,
       "mscDataSigChanInsFramerRowStatusTable": mscDataSigChanInsFramerRowStatusTable,
       "mscDataSigChanInsFramerRowStatusEntry": mscDataSigChanInsFramerRowStatusEntry,
       "mscDataSigChanInsFramerRowStatus": mscDataSigChanInsFramerRowStatus,
       "mscDataSigChanInsFramerComponentName": mscDataSigChanInsFramerComponentName,
       "mscDataSigChanInsFramerStorageType": mscDataSigChanInsFramerStorageType,
       "mscDataSigChanInsFramerIndex": mscDataSigChanInsFramerIndex,
       "mscDataSigChanInsFramerProvTable": mscDataSigChanInsFramerProvTable,
       "mscDataSigChanInsFramerProvEntry": mscDataSigChanInsFramerProvEntry,
       "mscDataSigChanInsFramerInterfaceName": mscDataSigChanInsFramerInterfaceName,
       "mscDataSigChanInsFramerStateTable": mscDataSigChanInsFramerStateTable,
       "mscDataSigChanInsFramerStateEntry": mscDataSigChanInsFramerStateEntry,
       "mscDataSigChanInsFramerAdminState": mscDataSigChanInsFramerAdminState,
       "mscDataSigChanInsFramerOperationalState": mscDataSigChanInsFramerOperationalState,
       "mscDataSigChanInsFramerUsageState": mscDataSigChanInsFramerUsageState,
       "mscDataSigChanInsFramerStatsTable": mscDataSigChanInsFramerStatsTable,
       "mscDataSigChanInsFramerStatsEntry": mscDataSigChanInsFramerStatsEntry,
       "mscDataSigChanInsFramerFrmToIf": mscDataSigChanInsFramerFrmToIf,
       "mscDataSigChanInsFramerFrmFromIf": mscDataSigChanInsFramerFrmFromIf,
       "mscDataSigChanInsFramerOctetFromIf": mscDataSigChanInsFramerOctetFromIf,
       "mscDataSigChanInsFramerAborts": mscDataSigChanInsFramerAborts,
       "mscDataSigChanInsFramerCrcErrors": mscDataSigChanInsFramerCrcErrors,
       "mscDataSigChanInsFramerLrcErrors": mscDataSigChanInsFramerLrcErrors,
       "mscDataSigChanInsFramerNonOctetErrors": mscDataSigChanInsFramerNonOctetErrors,
       "mscDataSigChanInsFramerOverruns": mscDataSigChanInsFramerOverruns,
       "mscDataSigChanInsFramerUnderruns": mscDataSigChanInsFramerUnderruns,
       "mscDataSigChanInsFramerLargeFrmErrors": mscDataSigChanInsFramerLargeFrmErrors,
       "mscDataSigChanInsL2Table": mscDataSigChanInsL2Table,
       "mscDataSigChanInsL2Entry": mscDataSigChanInsL2Entry,
       "mscDataSigChanInsT23": mscDataSigChanInsT23,
       "mscDataSigChanInsT200": mscDataSigChanInsT200,
       "mscDataSigChanInsN200": mscDataSigChanInsN200,
       "mscDataSigChanInsT203": mscDataSigChanInsT203,
       "mscDataSigChanInsN201": mscDataSigChanInsN201,
       "mscDataSigChanInsCircuitSwitchedK": mscDataSigChanInsCircuitSwitchedK,
       "mscDataSigChanInsProvTable": mscDataSigChanInsProvTable,
       "mscDataSigChanInsProvEntry": mscDataSigChanInsProvEntry,
       "mscDataSigChanInsSide": mscDataSigChanInsSide,
       "mscDataSigChanInsOperTable": mscDataSigChanInsOperTable,
       "mscDataSigChanInsOperEntry": mscDataSigChanInsOperEntry,
       "mscDataSigChanInsActiveChannels": mscDataSigChanInsActiveChannels,
       "mscDataSigChanInsPeakActiveChannels": mscDataSigChanInsPeakActiveChannels,
       "mscDataSigChanInsDChanStatus": mscDataSigChanInsDChanStatus,
       "mscDataSigChanInsToolsTable": mscDataSigChanInsToolsTable,
       "mscDataSigChanInsToolsEntry": mscDataSigChanInsToolsEntry,
       "mscDataSigChanInsTracing": mscDataSigChanInsTracing,
       "disdnJapanInsMIB": disdnJapanInsMIB,
       "disdnJapanInsGroup": disdnJapanInsGroup,
       "disdnJapanInsGroupCA": disdnJapanInsGroupCA,
       "disdnJapanInsGroupCA02": disdnJapanInsGroupCA02,
       "disdnJapanInsGroupCA02A": disdnJapanInsGroupCA02A,
       "disdnJapanInsCapabilities": disdnJapanInsCapabilities,
       "disdnJapanInsCapabilitiesCA": disdnJapanInsCapabilitiesCA,
       "disdnJapanInsCapabilitiesCA02": disdnJapanInsCapabilitiesCA02,
       "disdnJapanInsCapabilitiesCA02A": disdnJapanInsCapabilitiesCA02A}
)
