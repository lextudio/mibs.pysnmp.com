# SNMP MIB module (Nortel-MsCarrier-MscPassport-DisdnNI2MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DisdnNI2MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:12 2024
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

_MscDataSigChanNi2_ObjectIdentity = ObjectIdentity
mscDataSigChanNi2 = _MscDataSigChanNi2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12)
)
_MscDataSigChanNi2RowStatusTable_Object = MibTable
mscDataSigChanNi2RowStatusTable = _MscDataSigChanNi2RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2RowStatusTable.setStatus("mandatory")
_MscDataSigChanNi2RowStatusEntry_Object = MibTableRow
mscDataSigChanNi2RowStatusEntry = _MscDataSigChanNi2RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1)
)
mscDataSigChanNi2RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2RowStatusEntry.setStatus("mandatory")
_MscDataSigChanNi2RowStatus_Type = RowStatus
_MscDataSigChanNi2RowStatus_Object = MibTableColumn
mscDataSigChanNi2RowStatus = _MscDataSigChanNi2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 1),
    _MscDataSigChanNi2RowStatus_Type()
)
mscDataSigChanNi2RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2RowStatus.setStatus("mandatory")
_MscDataSigChanNi2ComponentName_Type = DisplayString
_MscDataSigChanNi2ComponentName_Object = MibTableColumn
mscDataSigChanNi2ComponentName = _MscDataSigChanNi2ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 2),
    _MscDataSigChanNi2ComponentName_Type()
)
mscDataSigChanNi2ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2ComponentName.setStatus("mandatory")
_MscDataSigChanNi2StorageType_Type = StorageType
_MscDataSigChanNi2StorageType_Object = MibTableColumn
mscDataSigChanNi2StorageType = _MscDataSigChanNi2StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 4),
    _MscDataSigChanNi2StorageType_Type()
)
mscDataSigChanNi2StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2StorageType.setStatus("mandatory")
_MscDataSigChanNi2Index_Type = NonReplicated
_MscDataSigChanNi2Index_Object = MibTableColumn
mscDataSigChanNi2Index = _MscDataSigChanNi2Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 10),
    _MscDataSigChanNi2Index_Type()
)
mscDataSigChanNi2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanNi2Index.setStatus("mandatory")
_MscDataSigChanNi2Framer_ObjectIdentity = ObjectIdentity
mscDataSigChanNi2Framer = _MscDataSigChanNi2Framer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2)
)
_MscDataSigChanNi2FramerRowStatusTable_Object = MibTable
mscDataSigChanNi2FramerRowStatusTable = _MscDataSigChanNi2FramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerRowStatusTable.setStatus("mandatory")
_MscDataSigChanNi2FramerRowStatusEntry_Object = MibTableRow
mscDataSigChanNi2FramerRowStatusEntry = _MscDataSigChanNi2FramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1)
)
mscDataSigChanNi2FramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerRowStatusEntry.setStatus("mandatory")
_MscDataSigChanNi2FramerRowStatus_Type = RowStatus
_MscDataSigChanNi2FramerRowStatus_Object = MibTableColumn
mscDataSigChanNi2FramerRowStatus = _MscDataSigChanNi2FramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 1),
    _MscDataSigChanNi2FramerRowStatus_Type()
)
mscDataSigChanNi2FramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerRowStatus.setStatus("mandatory")
_MscDataSigChanNi2FramerComponentName_Type = DisplayString
_MscDataSigChanNi2FramerComponentName_Object = MibTableColumn
mscDataSigChanNi2FramerComponentName = _MscDataSigChanNi2FramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 2),
    _MscDataSigChanNi2FramerComponentName_Type()
)
mscDataSigChanNi2FramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerComponentName.setStatus("mandatory")
_MscDataSigChanNi2FramerStorageType_Type = StorageType
_MscDataSigChanNi2FramerStorageType_Object = MibTableColumn
mscDataSigChanNi2FramerStorageType = _MscDataSigChanNi2FramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 4),
    _MscDataSigChanNi2FramerStorageType_Type()
)
mscDataSigChanNi2FramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerStorageType.setStatus("mandatory")
_MscDataSigChanNi2FramerIndex_Type = NonReplicated
_MscDataSigChanNi2FramerIndex_Object = MibTableColumn
mscDataSigChanNi2FramerIndex = _MscDataSigChanNi2FramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 10),
    _MscDataSigChanNi2FramerIndex_Type()
)
mscDataSigChanNi2FramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerIndex.setStatus("mandatory")
_MscDataSigChanNi2FramerProvTable_Object = MibTable
mscDataSigChanNi2FramerProvTable = _MscDataSigChanNi2FramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 10)
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerProvTable.setStatus("mandatory")
_MscDataSigChanNi2FramerProvEntry_Object = MibTableRow
mscDataSigChanNi2FramerProvEntry = _MscDataSigChanNi2FramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 10, 1)
)
mscDataSigChanNi2FramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerProvEntry.setStatus("mandatory")
_MscDataSigChanNi2FramerInterfaceName_Type = Link
_MscDataSigChanNi2FramerInterfaceName_Object = MibTableColumn
mscDataSigChanNi2FramerInterfaceName = _MscDataSigChanNi2FramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 10, 1, 1),
    _MscDataSigChanNi2FramerInterfaceName_Type()
)
mscDataSigChanNi2FramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerInterfaceName.setStatus("mandatory")
_MscDataSigChanNi2FramerStateTable_Object = MibTable
mscDataSigChanNi2FramerStateTable = _MscDataSigChanNi2FramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12)
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerStateTable.setStatus("mandatory")
_MscDataSigChanNi2FramerStateEntry_Object = MibTableRow
mscDataSigChanNi2FramerStateEntry = _MscDataSigChanNi2FramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1)
)
mscDataSigChanNi2FramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerStateEntry.setStatus("mandatory")


class _MscDataSigChanNi2FramerAdminState_Type(Integer32):
    """Custom type mscDataSigChanNi2FramerAdminState based on Integer32"""
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


_MscDataSigChanNi2FramerAdminState_Type.__name__ = "Integer32"
_MscDataSigChanNi2FramerAdminState_Object = MibTableColumn
mscDataSigChanNi2FramerAdminState = _MscDataSigChanNi2FramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1, 1),
    _MscDataSigChanNi2FramerAdminState_Type()
)
mscDataSigChanNi2FramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerAdminState.setStatus("mandatory")


class _MscDataSigChanNi2FramerOperationalState_Type(Integer32):
    """Custom type mscDataSigChanNi2FramerOperationalState based on Integer32"""
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


_MscDataSigChanNi2FramerOperationalState_Type.__name__ = "Integer32"
_MscDataSigChanNi2FramerOperationalState_Object = MibTableColumn
mscDataSigChanNi2FramerOperationalState = _MscDataSigChanNi2FramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1, 2),
    _MscDataSigChanNi2FramerOperationalState_Type()
)
mscDataSigChanNi2FramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerOperationalState.setStatus("mandatory")


class _MscDataSigChanNi2FramerUsageState_Type(Integer32):
    """Custom type mscDataSigChanNi2FramerUsageState based on Integer32"""
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


_MscDataSigChanNi2FramerUsageState_Type.__name__ = "Integer32"
_MscDataSigChanNi2FramerUsageState_Object = MibTableColumn
mscDataSigChanNi2FramerUsageState = _MscDataSigChanNi2FramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1, 3),
    _MscDataSigChanNi2FramerUsageState_Type()
)
mscDataSigChanNi2FramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerUsageState.setStatus("mandatory")
_MscDataSigChanNi2FramerStatsTable_Object = MibTable
mscDataSigChanNi2FramerStatsTable = _MscDataSigChanNi2FramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerStatsTable.setStatus("mandatory")
_MscDataSigChanNi2FramerStatsEntry_Object = MibTableRow
mscDataSigChanNi2FramerStatsEntry = _MscDataSigChanNi2FramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1)
)
mscDataSigChanNi2FramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerStatsEntry.setStatus("mandatory")


class _MscDataSigChanNi2FramerFrmToIf_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerFrmToIf_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerFrmToIf_Object = MibTableColumn
mscDataSigChanNi2FramerFrmToIf = _MscDataSigChanNi2FramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 1),
    _MscDataSigChanNi2FramerFrmToIf_Type()
)
mscDataSigChanNi2FramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerFrmToIf.setStatus("mandatory")


class _MscDataSigChanNi2FramerFrmFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerFrmFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerFrmFromIf_Object = MibTableColumn
mscDataSigChanNi2FramerFrmFromIf = _MscDataSigChanNi2FramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 2),
    _MscDataSigChanNi2FramerFrmFromIf_Type()
)
mscDataSigChanNi2FramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerFrmFromIf.setStatus("mandatory")


class _MscDataSigChanNi2FramerOctetFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerOctetFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerOctetFromIf_Object = MibTableColumn
mscDataSigChanNi2FramerOctetFromIf = _MscDataSigChanNi2FramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 3),
    _MscDataSigChanNi2FramerOctetFromIf_Type()
)
mscDataSigChanNi2FramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerOctetFromIf.setStatus("mandatory")


class _MscDataSigChanNi2FramerAborts_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerAborts_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerAborts_Object = MibTableColumn
mscDataSigChanNi2FramerAborts = _MscDataSigChanNi2FramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 4),
    _MscDataSigChanNi2FramerAborts_Type()
)
mscDataSigChanNi2FramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerAborts.setStatus("mandatory")


class _MscDataSigChanNi2FramerCrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerCrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerCrcErrors_Object = MibTableColumn
mscDataSigChanNi2FramerCrcErrors = _MscDataSigChanNi2FramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 5),
    _MscDataSigChanNi2FramerCrcErrors_Type()
)
mscDataSigChanNi2FramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerCrcErrors.setStatus("mandatory")


class _MscDataSigChanNi2FramerLrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerLrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerLrcErrors_Object = MibTableColumn
mscDataSigChanNi2FramerLrcErrors = _MscDataSigChanNi2FramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 6),
    _MscDataSigChanNi2FramerLrcErrors_Type()
)
mscDataSigChanNi2FramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerLrcErrors.setStatus("mandatory")


class _MscDataSigChanNi2FramerNonOctetErrors_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerNonOctetErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerNonOctetErrors_Object = MibTableColumn
mscDataSigChanNi2FramerNonOctetErrors = _MscDataSigChanNi2FramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 7),
    _MscDataSigChanNi2FramerNonOctetErrors_Type()
)
mscDataSigChanNi2FramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerNonOctetErrors.setStatus("mandatory")


class _MscDataSigChanNi2FramerOverruns_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerOverruns_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerOverruns_Object = MibTableColumn
mscDataSigChanNi2FramerOverruns = _MscDataSigChanNi2FramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 8),
    _MscDataSigChanNi2FramerOverruns_Type()
)
mscDataSigChanNi2FramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerOverruns.setStatus("mandatory")


class _MscDataSigChanNi2FramerUnderruns_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerUnderruns_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerUnderruns_Object = MibTableColumn
mscDataSigChanNi2FramerUnderruns = _MscDataSigChanNi2FramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 9),
    _MscDataSigChanNi2FramerUnderruns_Type()
)
mscDataSigChanNi2FramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerUnderruns.setStatus("mandatory")


class _MscDataSigChanNi2FramerLargeFrmErrors_Type(Unsigned32):
    """Custom type mscDataSigChanNi2FramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanNi2FramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2FramerLargeFrmErrors_Object = MibTableColumn
mscDataSigChanNi2FramerLargeFrmErrors = _MscDataSigChanNi2FramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 10),
    _MscDataSigChanNi2FramerLargeFrmErrors_Type()
)
mscDataSigChanNi2FramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2FramerLargeFrmErrors.setStatus("mandatory")
_MscDataSigChanNi2L2Table_Object = MibTable
mscDataSigChanNi2L2Table = _MscDataSigChanNi2L2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11)
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2L2Table.setStatus("mandatory")
_MscDataSigChanNi2L2Entry_Object = MibTableRow
mscDataSigChanNi2L2Entry = _MscDataSigChanNi2L2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1)
)
mscDataSigChanNi2L2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2L2Entry.setStatus("mandatory")


class _MscDataSigChanNi2T23_Type(Unsigned32):
    """Custom type mscDataSigChanNi2T23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscDataSigChanNi2T23_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2T23_Object = MibTableColumn
mscDataSigChanNi2T23 = _MscDataSigChanNi2T23_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 1),
    _MscDataSigChanNi2T23_Type()
)
mscDataSigChanNi2T23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2T23.setStatus("mandatory")


class _MscDataSigChanNi2T200_Type(Unsigned32):
    """Custom type mscDataSigChanNi2T200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscDataSigChanNi2T200_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2T200_Object = MibTableColumn
mscDataSigChanNi2T200 = _MscDataSigChanNi2T200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 2),
    _MscDataSigChanNi2T200_Type()
)
mscDataSigChanNi2T200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2T200.setStatus("mandatory")


class _MscDataSigChanNi2N200_Type(Unsigned32):
    """Custom type mscDataSigChanNi2N200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscDataSigChanNi2N200_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2N200_Object = MibTableColumn
mscDataSigChanNi2N200 = _MscDataSigChanNi2N200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 3),
    _MscDataSigChanNi2N200_Type()
)
mscDataSigChanNi2N200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2N200.setStatus("mandatory")


class _MscDataSigChanNi2T203_Type(Unsigned32):
    """Custom type mscDataSigChanNi2T203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_MscDataSigChanNi2T203_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2T203_Object = MibTableColumn
mscDataSigChanNi2T203 = _MscDataSigChanNi2T203_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 4),
    _MscDataSigChanNi2T203_Type()
)
mscDataSigChanNi2T203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2T203.setStatus("mandatory")


class _MscDataSigChanNi2N201_Type(Unsigned32):
    """Custom type mscDataSigChanNi2N201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_MscDataSigChanNi2N201_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2N201_Object = MibTableColumn
mscDataSigChanNi2N201 = _MscDataSigChanNi2N201_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 5),
    _MscDataSigChanNi2N201_Type()
)
mscDataSigChanNi2N201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2N201.setStatus("mandatory")


class _MscDataSigChanNi2CircuitSwitchedK_Type(Unsigned32):
    """Custom type mscDataSigChanNi2CircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_MscDataSigChanNi2CircuitSwitchedK_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2CircuitSwitchedK_Object = MibTableColumn
mscDataSigChanNi2CircuitSwitchedK = _MscDataSigChanNi2CircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 6),
    _MscDataSigChanNi2CircuitSwitchedK_Type()
)
mscDataSigChanNi2CircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2CircuitSwitchedK.setStatus("mandatory")
_MscDataSigChanNi2ProvTable_Object = MibTable
mscDataSigChanNi2ProvTable = _MscDataSigChanNi2ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2ProvTable.setStatus("mandatory")
_MscDataSigChanNi2ProvEntry_Object = MibTableRow
mscDataSigChanNi2ProvEntry = _MscDataSigChanNi2ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 13, 1)
)
mscDataSigChanNi2ProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2ProvEntry.setStatus("mandatory")


class _MscDataSigChanNi2Side_Type(Integer32):
    """Custom type mscDataSigChanNi2Side based on Integer32"""
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


_MscDataSigChanNi2Side_Type.__name__ = "Integer32"
_MscDataSigChanNi2Side_Object = MibTableColumn
mscDataSigChanNi2Side = _MscDataSigChanNi2Side_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 13, 1, 1),
    _MscDataSigChanNi2Side_Type()
)
mscDataSigChanNi2Side.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2Side.setStatus("mandatory")
_MscDataSigChanNi2OperTable_Object = MibTable
mscDataSigChanNi2OperTable = _MscDataSigChanNi2OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15)
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2OperTable.setStatus("mandatory")
_MscDataSigChanNi2OperEntry_Object = MibTableRow
mscDataSigChanNi2OperEntry = _MscDataSigChanNi2OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1)
)
mscDataSigChanNi2OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2OperEntry.setStatus("mandatory")


class _MscDataSigChanNi2ActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanNi2ActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanNi2ActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2ActiveChannels_Object = MibTableColumn
mscDataSigChanNi2ActiveChannels = _MscDataSigChanNi2ActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1, 1),
    _MscDataSigChanNi2ActiveChannels_Type()
)
mscDataSigChanNi2ActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2ActiveChannels.setStatus("mandatory")


class _MscDataSigChanNi2PeakActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanNi2PeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanNi2PeakActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanNi2PeakActiveChannels_Object = MibTableColumn
mscDataSigChanNi2PeakActiveChannels = _MscDataSigChanNi2PeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1, 4),
    _MscDataSigChanNi2PeakActiveChannels_Type()
)
mscDataSigChanNi2PeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2PeakActiveChannels.setStatus("mandatory")


class _MscDataSigChanNi2DChanStatus_Type(Integer32):
    """Custom type mscDataSigChanNi2DChanStatus based on Integer32"""
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


_MscDataSigChanNi2DChanStatus_Type.__name__ = "Integer32"
_MscDataSigChanNi2DChanStatus_Object = MibTableColumn
mscDataSigChanNi2DChanStatus = _MscDataSigChanNi2DChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1, 7),
    _MscDataSigChanNi2DChanStatus_Type()
)
mscDataSigChanNi2DChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanNi2DChanStatus.setStatus("mandatory")
_MscDataSigChanNi2ToolsTable_Object = MibTable
mscDataSigChanNi2ToolsTable = _MscDataSigChanNi2ToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 16)
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2ToolsTable.setStatus("mandatory")
_MscDataSigChanNi2ToolsEntry_Object = MibTableRow
mscDataSigChanNi2ToolsEntry = _MscDataSigChanNi2ToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 16, 1)
)
mscDataSigChanNi2ToolsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanNi2ToolsEntry.setStatus("mandatory")


class _MscDataSigChanNi2Tracing_Type(OctetString):
    """Custom type mscDataSigChanNi2Tracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDataSigChanNi2Tracing_Type.__name__ = "OctetString"
_MscDataSigChanNi2Tracing_Object = MibTableColumn
mscDataSigChanNi2Tracing = _MscDataSigChanNi2Tracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 16, 1, 1),
    _MscDataSigChanNi2Tracing_Type()
)
mscDataSigChanNi2Tracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanNi2Tracing.setStatus("mandatory")
_DisdnNI2MIB_ObjectIdentity = ObjectIdentity
disdnNI2MIB = _DisdnNI2MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126)
)
_DisdnNI2Group_ObjectIdentity = ObjectIdentity
disdnNI2Group = _DisdnNI2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1)
)
_DisdnNI2GroupCA_ObjectIdentity = ObjectIdentity
disdnNI2GroupCA = _DisdnNI2GroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1, 1)
)
_DisdnNI2GroupCA02_ObjectIdentity = ObjectIdentity
disdnNI2GroupCA02 = _DisdnNI2GroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1, 1, 3)
)
_DisdnNI2GroupCA02A_ObjectIdentity = ObjectIdentity
disdnNI2GroupCA02A = _DisdnNI2GroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1, 1, 3, 2)
)
_DisdnNI2Capabilities_ObjectIdentity = ObjectIdentity
disdnNI2Capabilities = _DisdnNI2Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3)
)
_DisdnNI2CapabilitiesCA_ObjectIdentity = ObjectIdentity
disdnNI2CapabilitiesCA = _DisdnNI2CapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3, 1)
)
_DisdnNI2CapabilitiesCA02_ObjectIdentity = ObjectIdentity
disdnNI2CapabilitiesCA02 = _DisdnNI2CapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3, 1, 3)
)
_DisdnNI2CapabilitiesCA02A_ObjectIdentity = ObjectIdentity
disdnNI2CapabilitiesCA02A = _DisdnNI2CapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DisdnNI2MIB",
    **{"mscDataSigChanNi2": mscDataSigChanNi2,
       "mscDataSigChanNi2RowStatusTable": mscDataSigChanNi2RowStatusTable,
       "mscDataSigChanNi2RowStatusEntry": mscDataSigChanNi2RowStatusEntry,
       "mscDataSigChanNi2RowStatus": mscDataSigChanNi2RowStatus,
       "mscDataSigChanNi2ComponentName": mscDataSigChanNi2ComponentName,
       "mscDataSigChanNi2StorageType": mscDataSigChanNi2StorageType,
       "mscDataSigChanNi2Index": mscDataSigChanNi2Index,
       "mscDataSigChanNi2Framer": mscDataSigChanNi2Framer,
       "mscDataSigChanNi2FramerRowStatusTable": mscDataSigChanNi2FramerRowStatusTable,
       "mscDataSigChanNi2FramerRowStatusEntry": mscDataSigChanNi2FramerRowStatusEntry,
       "mscDataSigChanNi2FramerRowStatus": mscDataSigChanNi2FramerRowStatus,
       "mscDataSigChanNi2FramerComponentName": mscDataSigChanNi2FramerComponentName,
       "mscDataSigChanNi2FramerStorageType": mscDataSigChanNi2FramerStorageType,
       "mscDataSigChanNi2FramerIndex": mscDataSigChanNi2FramerIndex,
       "mscDataSigChanNi2FramerProvTable": mscDataSigChanNi2FramerProvTable,
       "mscDataSigChanNi2FramerProvEntry": mscDataSigChanNi2FramerProvEntry,
       "mscDataSigChanNi2FramerInterfaceName": mscDataSigChanNi2FramerInterfaceName,
       "mscDataSigChanNi2FramerStateTable": mscDataSigChanNi2FramerStateTable,
       "mscDataSigChanNi2FramerStateEntry": mscDataSigChanNi2FramerStateEntry,
       "mscDataSigChanNi2FramerAdminState": mscDataSigChanNi2FramerAdminState,
       "mscDataSigChanNi2FramerOperationalState": mscDataSigChanNi2FramerOperationalState,
       "mscDataSigChanNi2FramerUsageState": mscDataSigChanNi2FramerUsageState,
       "mscDataSigChanNi2FramerStatsTable": mscDataSigChanNi2FramerStatsTable,
       "mscDataSigChanNi2FramerStatsEntry": mscDataSigChanNi2FramerStatsEntry,
       "mscDataSigChanNi2FramerFrmToIf": mscDataSigChanNi2FramerFrmToIf,
       "mscDataSigChanNi2FramerFrmFromIf": mscDataSigChanNi2FramerFrmFromIf,
       "mscDataSigChanNi2FramerOctetFromIf": mscDataSigChanNi2FramerOctetFromIf,
       "mscDataSigChanNi2FramerAborts": mscDataSigChanNi2FramerAborts,
       "mscDataSigChanNi2FramerCrcErrors": mscDataSigChanNi2FramerCrcErrors,
       "mscDataSigChanNi2FramerLrcErrors": mscDataSigChanNi2FramerLrcErrors,
       "mscDataSigChanNi2FramerNonOctetErrors": mscDataSigChanNi2FramerNonOctetErrors,
       "mscDataSigChanNi2FramerOverruns": mscDataSigChanNi2FramerOverruns,
       "mscDataSigChanNi2FramerUnderruns": mscDataSigChanNi2FramerUnderruns,
       "mscDataSigChanNi2FramerLargeFrmErrors": mscDataSigChanNi2FramerLargeFrmErrors,
       "mscDataSigChanNi2L2Table": mscDataSigChanNi2L2Table,
       "mscDataSigChanNi2L2Entry": mscDataSigChanNi2L2Entry,
       "mscDataSigChanNi2T23": mscDataSigChanNi2T23,
       "mscDataSigChanNi2T200": mscDataSigChanNi2T200,
       "mscDataSigChanNi2N200": mscDataSigChanNi2N200,
       "mscDataSigChanNi2T203": mscDataSigChanNi2T203,
       "mscDataSigChanNi2N201": mscDataSigChanNi2N201,
       "mscDataSigChanNi2CircuitSwitchedK": mscDataSigChanNi2CircuitSwitchedK,
       "mscDataSigChanNi2ProvTable": mscDataSigChanNi2ProvTable,
       "mscDataSigChanNi2ProvEntry": mscDataSigChanNi2ProvEntry,
       "mscDataSigChanNi2Side": mscDataSigChanNi2Side,
       "mscDataSigChanNi2OperTable": mscDataSigChanNi2OperTable,
       "mscDataSigChanNi2OperEntry": mscDataSigChanNi2OperEntry,
       "mscDataSigChanNi2ActiveChannels": mscDataSigChanNi2ActiveChannels,
       "mscDataSigChanNi2PeakActiveChannels": mscDataSigChanNi2PeakActiveChannels,
       "mscDataSigChanNi2DChanStatus": mscDataSigChanNi2DChanStatus,
       "mscDataSigChanNi2ToolsTable": mscDataSigChanNi2ToolsTable,
       "mscDataSigChanNi2ToolsEntry": mscDataSigChanNi2ToolsEntry,
       "mscDataSigChanNi2Tracing": mscDataSigChanNi2Tracing,
       "disdnNI2MIB": disdnNI2MIB,
       "disdnNI2Group": disdnNI2Group,
       "disdnNI2GroupCA": disdnNI2GroupCA,
       "disdnNI2GroupCA02": disdnNI2GroupCA02,
       "disdnNI2GroupCA02A": disdnNI2GroupCA02A,
       "disdnNI2Capabilities": disdnNI2Capabilities,
       "disdnNI2CapabilitiesCA": disdnNI2CapabilitiesCA,
       "disdnNI2CapabilitiesCA02": disdnNI2CapabilitiesCA02,
       "disdnNI2CapabilitiesCA02A": disdnNI2CapabilitiesCA02A}
)
