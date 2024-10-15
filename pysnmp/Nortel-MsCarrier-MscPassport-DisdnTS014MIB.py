# SNMP MIB module (Nortel-MsCarrier-MscPassport-DisdnTS014MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DisdnTS014MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:14 2024
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

_MscDataSigChanTS014_ObjectIdentity = ObjectIdentity
mscDataSigChanTS014 = _MscDataSigChanTS014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9)
)
_MscDataSigChanTS014RowStatusTable_Object = MibTable
mscDataSigChanTS014RowStatusTable = _MscDataSigChanTS014RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014RowStatusTable.setStatus("mandatory")
_MscDataSigChanTS014RowStatusEntry_Object = MibTableRow
mscDataSigChanTS014RowStatusEntry = _MscDataSigChanTS014RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1)
)
mscDataSigChanTS014RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014RowStatusEntry.setStatus("mandatory")
_MscDataSigChanTS014RowStatus_Type = RowStatus
_MscDataSigChanTS014RowStatus_Object = MibTableColumn
mscDataSigChanTS014RowStatus = _MscDataSigChanTS014RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1, 1),
    _MscDataSigChanTS014RowStatus_Type()
)
mscDataSigChanTS014RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014RowStatus.setStatus("mandatory")
_MscDataSigChanTS014ComponentName_Type = DisplayString
_MscDataSigChanTS014ComponentName_Object = MibTableColumn
mscDataSigChanTS014ComponentName = _MscDataSigChanTS014ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1, 2),
    _MscDataSigChanTS014ComponentName_Type()
)
mscDataSigChanTS014ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014ComponentName.setStatus("mandatory")
_MscDataSigChanTS014StorageType_Type = StorageType
_MscDataSigChanTS014StorageType_Object = MibTableColumn
mscDataSigChanTS014StorageType = _MscDataSigChanTS014StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1, 4),
    _MscDataSigChanTS014StorageType_Type()
)
mscDataSigChanTS014StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014StorageType.setStatus("mandatory")
_MscDataSigChanTS014Index_Type = NonReplicated
_MscDataSigChanTS014Index_Object = MibTableColumn
mscDataSigChanTS014Index = _MscDataSigChanTS014Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1, 10),
    _MscDataSigChanTS014Index_Type()
)
mscDataSigChanTS014Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanTS014Index.setStatus("mandatory")
_MscDataSigChanTS014Framer_ObjectIdentity = ObjectIdentity
mscDataSigChanTS014Framer = _MscDataSigChanTS014Framer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2)
)
_MscDataSigChanTS014FramerRowStatusTable_Object = MibTable
mscDataSigChanTS014FramerRowStatusTable = _MscDataSigChanTS014FramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerRowStatusTable.setStatus("mandatory")
_MscDataSigChanTS014FramerRowStatusEntry_Object = MibTableRow
mscDataSigChanTS014FramerRowStatusEntry = _MscDataSigChanTS014FramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1)
)
mscDataSigChanTS014FramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014FramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerRowStatusEntry.setStatus("mandatory")
_MscDataSigChanTS014FramerRowStatus_Type = RowStatus
_MscDataSigChanTS014FramerRowStatus_Object = MibTableColumn
mscDataSigChanTS014FramerRowStatus = _MscDataSigChanTS014FramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1, 1),
    _MscDataSigChanTS014FramerRowStatus_Type()
)
mscDataSigChanTS014FramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerRowStatus.setStatus("mandatory")
_MscDataSigChanTS014FramerComponentName_Type = DisplayString
_MscDataSigChanTS014FramerComponentName_Object = MibTableColumn
mscDataSigChanTS014FramerComponentName = _MscDataSigChanTS014FramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1, 2),
    _MscDataSigChanTS014FramerComponentName_Type()
)
mscDataSigChanTS014FramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerComponentName.setStatus("mandatory")
_MscDataSigChanTS014FramerStorageType_Type = StorageType
_MscDataSigChanTS014FramerStorageType_Object = MibTableColumn
mscDataSigChanTS014FramerStorageType = _MscDataSigChanTS014FramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1, 4),
    _MscDataSigChanTS014FramerStorageType_Type()
)
mscDataSigChanTS014FramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerStorageType.setStatus("mandatory")
_MscDataSigChanTS014FramerIndex_Type = NonReplicated
_MscDataSigChanTS014FramerIndex_Object = MibTableColumn
mscDataSigChanTS014FramerIndex = _MscDataSigChanTS014FramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1, 10),
    _MscDataSigChanTS014FramerIndex_Type()
)
mscDataSigChanTS014FramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerIndex.setStatus("mandatory")
_MscDataSigChanTS014FramerProvTable_Object = MibTable
mscDataSigChanTS014FramerProvTable = _MscDataSigChanTS014FramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 10)
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerProvTable.setStatus("mandatory")
_MscDataSigChanTS014FramerProvEntry_Object = MibTableRow
mscDataSigChanTS014FramerProvEntry = _MscDataSigChanTS014FramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 10, 1)
)
mscDataSigChanTS014FramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014FramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerProvEntry.setStatus("mandatory")
_MscDataSigChanTS014FramerInterfaceName_Type = Link
_MscDataSigChanTS014FramerInterfaceName_Object = MibTableColumn
mscDataSigChanTS014FramerInterfaceName = _MscDataSigChanTS014FramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 10, 1, 1),
    _MscDataSigChanTS014FramerInterfaceName_Type()
)
mscDataSigChanTS014FramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerInterfaceName.setStatus("mandatory")
_MscDataSigChanTS014FramerStateTable_Object = MibTable
mscDataSigChanTS014FramerStateTable = _MscDataSigChanTS014FramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12)
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerStateTable.setStatus("mandatory")
_MscDataSigChanTS014FramerStateEntry_Object = MibTableRow
mscDataSigChanTS014FramerStateEntry = _MscDataSigChanTS014FramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12, 1)
)
mscDataSigChanTS014FramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014FramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerStateEntry.setStatus("mandatory")


class _MscDataSigChanTS014FramerAdminState_Type(Integer32):
    """Custom type mscDataSigChanTS014FramerAdminState based on Integer32"""
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


_MscDataSigChanTS014FramerAdminState_Type.__name__ = "Integer32"
_MscDataSigChanTS014FramerAdminState_Object = MibTableColumn
mscDataSigChanTS014FramerAdminState = _MscDataSigChanTS014FramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12, 1, 1),
    _MscDataSigChanTS014FramerAdminState_Type()
)
mscDataSigChanTS014FramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerAdminState.setStatus("mandatory")


class _MscDataSigChanTS014FramerOperationalState_Type(Integer32):
    """Custom type mscDataSigChanTS014FramerOperationalState based on Integer32"""
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


_MscDataSigChanTS014FramerOperationalState_Type.__name__ = "Integer32"
_MscDataSigChanTS014FramerOperationalState_Object = MibTableColumn
mscDataSigChanTS014FramerOperationalState = _MscDataSigChanTS014FramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12, 1, 2),
    _MscDataSigChanTS014FramerOperationalState_Type()
)
mscDataSigChanTS014FramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerOperationalState.setStatus("mandatory")


class _MscDataSigChanTS014FramerUsageState_Type(Integer32):
    """Custom type mscDataSigChanTS014FramerUsageState based on Integer32"""
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


_MscDataSigChanTS014FramerUsageState_Type.__name__ = "Integer32"
_MscDataSigChanTS014FramerUsageState_Object = MibTableColumn
mscDataSigChanTS014FramerUsageState = _MscDataSigChanTS014FramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12, 1, 3),
    _MscDataSigChanTS014FramerUsageState_Type()
)
mscDataSigChanTS014FramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerUsageState.setStatus("mandatory")
_MscDataSigChanTS014FramerStatsTable_Object = MibTable
mscDataSigChanTS014FramerStatsTable = _MscDataSigChanTS014FramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerStatsTable.setStatus("mandatory")
_MscDataSigChanTS014FramerStatsEntry_Object = MibTableRow
mscDataSigChanTS014FramerStatsEntry = _MscDataSigChanTS014FramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1)
)
mscDataSigChanTS014FramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014FramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerStatsEntry.setStatus("mandatory")


class _MscDataSigChanTS014FramerFrmToIf_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerFrmToIf_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerFrmToIf_Object = MibTableColumn
mscDataSigChanTS014FramerFrmToIf = _MscDataSigChanTS014FramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 1),
    _MscDataSigChanTS014FramerFrmToIf_Type()
)
mscDataSigChanTS014FramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerFrmToIf.setStatus("mandatory")


class _MscDataSigChanTS014FramerFrmFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerFrmFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerFrmFromIf_Object = MibTableColumn
mscDataSigChanTS014FramerFrmFromIf = _MscDataSigChanTS014FramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 2),
    _MscDataSigChanTS014FramerFrmFromIf_Type()
)
mscDataSigChanTS014FramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerFrmFromIf.setStatus("mandatory")


class _MscDataSigChanTS014FramerOctetFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerOctetFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerOctetFromIf_Object = MibTableColumn
mscDataSigChanTS014FramerOctetFromIf = _MscDataSigChanTS014FramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 3),
    _MscDataSigChanTS014FramerOctetFromIf_Type()
)
mscDataSigChanTS014FramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerOctetFromIf.setStatus("mandatory")


class _MscDataSigChanTS014FramerAborts_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerAborts_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerAborts_Object = MibTableColumn
mscDataSigChanTS014FramerAborts = _MscDataSigChanTS014FramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 4),
    _MscDataSigChanTS014FramerAborts_Type()
)
mscDataSigChanTS014FramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerAborts.setStatus("mandatory")


class _MscDataSigChanTS014FramerCrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerCrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerCrcErrors_Object = MibTableColumn
mscDataSigChanTS014FramerCrcErrors = _MscDataSigChanTS014FramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 5),
    _MscDataSigChanTS014FramerCrcErrors_Type()
)
mscDataSigChanTS014FramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerCrcErrors.setStatus("mandatory")


class _MscDataSigChanTS014FramerLrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerLrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerLrcErrors_Object = MibTableColumn
mscDataSigChanTS014FramerLrcErrors = _MscDataSigChanTS014FramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 6),
    _MscDataSigChanTS014FramerLrcErrors_Type()
)
mscDataSigChanTS014FramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerLrcErrors.setStatus("mandatory")


class _MscDataSigChanTS014FramerNonOctetErrors_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerNonOctetErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerNonOctetErrors_Object = MibTableColumn
mscDataSigChanTS014FramerNonOctetErrors = _MscDataSigChanTS014FramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 7),
    _MscDataSigChanTS014FramerNonOctetErrors_Type()
)
mscDataSigChanTS014FramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerNonOctetErrors.setStatus("mandatory")


class _MscDataSigChanTS014FramerOverruns_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerOverruns_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerOverruns_Object = MibTableColumn
mscDataSigChanTS014FramerOverruns = _MscDataSigChanTS014FramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 8),
    _MscDataSigChanTS014FramerOverruns_Type()
)
mscDataSigChanTS014FramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerOverruns.setStatus("mandatory")


class _MscDataSigChanTS014FramerUnderruns_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerUnderruns_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerUnderruns_Object = MibTableColumn
mscDataSigChanTS014FramerUnderruns = _MscDataSigChanTS014FramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 9),
    _MscDataSigChanTS014FramerUnderruns_Type()
)
mscDataSigChanTS014FramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerUnderruns.setStatus("mandatory")


class _MscDataSigChanTS014FramerLargeFrmErrors_Type(Unsigned32):
    """Custom type mscDataSigChanTS014FramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanTS014FramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014FramerLargeFrmErrors_Object = MibTableColumn
mscDataSigChanTS014FramerLargeFrmErrors = _MscDataSigChanTS014FramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 10),
    _MscDataSigChanTS014FramerLargeFrmErrors_Type()
)
mscDataSigChanTS014FramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014FramerLargeFrmErrors.setStatus("mandatory")
_MscDataSigChanTS014L2Table_Object = MibTable
mscDataSigChanTS014L2Table = _MscDataSigChanTS014L2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11)
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014L2Table.setStatus("mandatory")
_MscDataSigChanTS014L2Entry_Object = MibTableRow
mscDataSigChanTS014L2Entry = _MscDataSigChanTS014L2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1)
)
mscDataSigChanTS014L2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014L2Entry.setStatus("mandatory")


class _MscDataSigChanTS014T23_Type(Unsigned32):
    """Custom type mscDataSigChanTS014T23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscDataSigChanTS014T23_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014T23_Object = MibTableColumn
mscDataSigChanTS014T23 = _MscDataSigChanTS014T23_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 1),
    _MscDataSigChanTS014T23_Type()
)
mscDataSigChanTS014T23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014T23.setStatus("mandatory")


class _MscDataSigChanTS014T200_Type(Unsigned32):
    """Custom type mscDataSigChanTS014T200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscDataSigChanTS014T200_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014T200_Object = MibTableColumn
mscDataSigChanTS014T200 = _MscDataSigChanTS014T200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 2),
    _MscDataSigChanTS014T200_Type()
)
mscDataSigChanTS014T200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014T200.setStatus("mandatory")


class _MscDataSigChanTS014N200_Type(Unsigned32):
    """Custom type mscDataSigChanTS014N200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscDataSigChanTS014N200_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014N200_Object = MibTableColumn
mscDataSigChanTS014N200 = _MscDataSigChanTS014N200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 3),
    _MscDataSigChanTS014N200_Type()
)
mscDataSigChanTS014N200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014N200.setStatus("mandatory")


class _MscDataSigChanTS014T203_Type(Unsigned32):
    """Custom type mscDataSigChanTS014T203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_MscDataSigChanTS014T203_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014T203_Object = MibTableColumn
mscDataSigChanTS014T203 = _MscDataSigChanTS014T203_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 4),
    _MscDataSigChanTS014T203_Type()
)
mscDataSigChanTS014T203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014T203.setStatus("mandatory")


class _MscDataSigChanTS014N201_Type(Unsigned32):
    """Custom type mscDataSigChanTS014N201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_MscDataSigChanTS014N201_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014N201_Object = MibTableColumn
mscDataSigChanTS014N201 = _MscDataSigChanTS014N201_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 5),
    _MscDataSigChanTS014N201_Type()
)
mscDataSigChanTS014N201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014N201.setStatus("mandatory")


class _MscDataSigChanTS014CircuitSwitchedK_Type(Unsigned32):
    """Custom type mscDataSigChanTS014CircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_MscDataSigChanTS014CircuitSwitchedK_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014CircuitSwitchedK_Object = MibTableColumn
mscDataSigChanTS014CircuitSwitchedK = _MscDataSigChanTS014CircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 6),
    _MscDataSigChanTS014CircuitSwitchedK_Type()
)
mscDataSigChanTS014CircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014CircuitSwitchedK.setStatus("mandatory")
_MscDataSigChanTS014ProvTable_Object = MibTable
mscDataSigChanTS014ProvTable = _MscDataSigChanTS014ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014ProvTable.setStatus("mandatory")
_MscDataSigChanTS014ProvEntry_Object = MibTableRow
mscDataSigChanTS014ProvEntry = _MscDataSigChanTS014ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 13, 1)
)
mscDataSigChanTS014ProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014ProvEntry.setStatus("mandatory")


class _MscDataSigChanTS014Side_Type(Integer32):
    """Custom type mscDataSigChanTS014Side based on Integer32"""
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


_MscDataSigChanTS014Side_Type.__name__ = "Integer32"
_MscDataSigChanTS014Side_Object = MibTableColumn
mscDataSigChanTS014Side = _MscDataSigChanTS014Side_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 13, 1, 1),
    _MscDataSigChanTS014Side_Type()
)
mscDataSigChanTS014Side.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014Side.setStatus("mandatory")
_MscDataSigChanTS014OperTable_Object = MibTable
mscDataSigChanTS014OperTable = _MscDataSigChanTS014OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15)
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014OperTable.setStatus("mandatory")
_MscDataSigChanTS014OperEntry_Object = MibTableRow
mscDataSigChanTS014OperEntry = _MscDataSigChanTS014OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15, 1)
)
mscDataSigChanTS014OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014OperEntry.setStatus("mandatory")


class _MscDataSigChanTS014ActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanTS014ActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanTS014ActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014ActiveChannels_Object = MibTableColumn
mscDataSigChanTS014ActiveChannels = _MscDataSigChanTS014ActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15, 1, 1),
    _MscDataSigChanTS014ActiveChannels_Type()
)
mscDataSigChanTS014ActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014ActiveChannels.setStatus("mandatory")


class _MscDataSigChanTS014PeakActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanTS014PeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanTS014PeakActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanTS014PeakActiveChannels_Object = MibTableColumn
mscDataSigChanTS014PeakActiveChannels = _MscDataSigChanTS014PeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15, 1, 4),
    _MscDataSigChanTS014PeakActiveChannels_Type()
)
mscDataSigChanTS014PeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014PeakActiveChannels.setStatus("mandatory")


class _MscDataSigChanTS014DChanStatus_Type(Integer32):
    """Custom type mscDataSigChanTS014DChanStatus based on Integer32"""
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


_MscDataSigChanTS014DChanStatus_Type.__name__ = "Integer32"
_MscDataSigChanTS014DChanStatus_Object = MibTableColumn
mscDataSigChanTS014DChanStatus = _MscDataSigChanTS014DChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15, 1, 7),
    _MscDataSigChanTS014DChanStatus_Type()
)
mscDataSigChanTS014DChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanTS014DChanStatus.setStatus("mandatory")
_MscDataSigChanTS014ToolsTable_Object = MibTable
mscDataSigChanTS014ToolsTable = _MscDataSigChanTS014ToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 16)
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014ToolsTable.setStatus("mandatory")
_MscDataSigChanTS014ToolsEntry_Object = MibTableRow
mscDataSigChanTS014ToolsEntry = _MscDataSigChanTS014ToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 16, 1)
)
mscDataSigChanTS014ToolsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"),
)
if mibBuilder.loadTexts:
    mscDataSigChanTS014ToolsEntry.setStatus("mandatory")


class _MscDataSigChanTS014Tracing_Type(OctetString):
    """Custom type mscDataSigChanTS014Tracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDataSigChanTS014Tracing_Type.__name__ = "OctetString"
_MscDataSigChanTS014Tracing_Object = MibTableColumn
mscDataSigChanTS014Tracing = _MscDataSigChanTS014Tracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 16, 1, 1),
    _MscDataSigChanTS014Tracing_Type()
)
mscDataSigChanTS014Tracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanTS014Tracing.setStatus("mandatory")
_DisdnTS014MIB_ObjectIdentity = ObjectIdentity
disdnTS014MIB = _DisdnTS014MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114)
)
_DisdnTS014Group_ObjectIdentity = ObjectIdentity
disdnTS014Group = _DisdnTS014Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 1)
)
_DisdnTS014GroupCA_ObjectIdentity = ObjectIdentity
disdnTS014GroupCA = _DisdnTS014GroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 1, 1)
)
_DisdnTS014GroupCA02_ObjectIdentity = ObjectIdentity
disdnTS014GroupCA02 = _DisdnTS014GroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 1, 1, 3)
)
_DisdnTS014GroupCA02A_ObjectIdentity = ObjectIdentity
disdnTS014GroupCA02A = _DisdnTS014GroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 1, 1, 3, 2)
)
_DisdnTS014Capabilities_ObjectIdentity = ObjectIdentity
disdnTS014Capabilities = _DisdnTS014Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 3)
)
_DisdnTS014CapabilitiesCA_ObjectIdentity = ObjectIdentity
disdnTS014CapabilitiesCA = _DisdnTS014CapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 3, 1)
)
_DisdnTS014CapabilitiesCA02_ObjectIdentity = ObjectIdentity
disdnTS014CapabilitiesCA02 = _DisdnTS014CapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 3, 1, 3)
)
_DisdnTS014CapabilitiesCA02A_ObjectIdentity = ObjectIdentity
disdnTS014CapabilitiesCA02A = _DisdnTS014CapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DisdnTS014MIB",
    **{"mscDataSigChanTS014": mscDataSigChanTS014,
       "mscDataSigChanTS014RowStatusTable": mscDataSigChanTS014RowStatusTable,
       "mscDataSigChanTS014RowStatusEntry": mscDataSigChanTS014RowStatusEntry,
       "mscDataSigChanTS014RowStatus": mscDataSigChanTS014RowStatus,
       "mscDataSigChanTS014ComponentName": mscDataSigChanTS014ComponentName,
       "mscDataSigChanTS014StorageType": mscDataSigChanTS014StorageType,
       "mscDataSigChanTS014Index": mscDataSigChanTS014Index,
       "mscDataSigChanTS014Framer": mscDataSigChanTS014Framer,
       "mscDataSigChanTS014FramerRowStatusTable": mscDataSigChanTS014FramerRowStatusTable,
       "mscDataSigChanTS014FramerRowStatusEntry": mscDataSigChanTS014FramerRowStatusEntry,
       "mscDataSigChanTS014FramerRowStatus": mscDataSigChanTS014FramerRowStatus,
       "mscDataSigChanTS014FramerComponentName": mscDataSigChanTS014FramerComponentName,
       "mscDataSigChanTS014FramerStorageType": mscDataSigChanTS014FramerStorageType,
       "mscDataSigChanTS014FramerIndex": mscDataSigChanTS014FramerIndex,
       "mscDataSigChanTS014FramerProvTable": mscDataSigChanTS014FramerProvTable,
       "mscDataSigChanTS014FramerProvEntry": mscDataSigChanTS014FramerProvEntry,
       "mscDataSigChanTS014FramerInterfaceName": mscDataSigChanTS014FramerInterfaceName,
       "mscDataSigChanTS014FramerStateTable": mscDataSigChanTS014FramerStateTable,
       "mscDataSigChanTS014FramerStateEntry": mscDataSigChanTS014FramerStateEntry,
       "mscDataSigChanTS014FramerAdminState": mscDataSigChanTS014FramerAdminState,
       "mscDataSigChanTS014FramerOperationalState": mscDataSigChanTS014FramerOperationalState,
       "mscDataSigChanTS014FramerUsageState": mscDataSigChanTS014FramerUsageState,
       "mscDataSigChanTS014FramerStatsTable": mscDataSigChanTS014FramerStatsTable,
       "mscDataSigChanTS014FramerStatsEntry": mscDataSigChanTS014FramerStatsEntry,
       "mscDataSigChanTS014FramerFrmToIf": mscDataSigChanTS014FramerFrmToIf,
       "mscDataSigChanTS014FramerFrmFromIf": mscDataSigChanTS014FramerFrmFromIf,
       "mscDataSigChanTS014FramerOctetFromIf": mscDataSigChanTS014FramerOctetFromIf,
       "mscDataSigChanTS014FramerAborts": mscDataSigChanTS014FramerAborts,
       "mscDataSigChanTS014FramerCrcErrors": mscDataSigChanTS014FramerCrcErrors,
       "mscDataSigChanTS014FramerLrcErrors": mscDataSigChanTS014FramerLrcErrors,
       "mscDataSigChanTS014FramerNonOctetErrors": mscDataSigChanTS014FramerNonOctetErrors,
       "mscDataSigChanTS014FramerOverruns": mscDataSigChanTS014FramerOverruns,
       "mscDataSigChanTS014FramerUnderruns": mscDataSigChanTS014FramerUnderruns,
       "mscDataSigChanTS014FramerLargeFrmErrors": mscDataSigChanTS014FramerLargeFrmErrors,
       "mscDataSigChanTS014L2Table": mscDataSigChanTS014L2Table,
       "mscDataSigChanTS014L2Entry": mscDataSigChanTS014L2Entry,
       "mscDataSigChanTS014T23": mscDataSigChanTS014T23,
       "mscDataSigChanTS014T200": mscDataSigChanTS014T200,
       "mscDataSigChanTS014N200": mscDataSigChanTS014N200,
       "mscDataSigChanTS014T203": mscDataSigChanTS014T203,
       "mscDataSigChanTS014N201": mscDataSigChanTS014N201,
       "mscDataSigChanTS014CircuitSwitchedK": mscDataSigChanTS014CircuitSwitchedK,
       "mscDataSigChanTS014ProvTable": mscDataSigChanTS014ProvTable,
       "mscDataSigChanTS014ProvEntry": mscDataSigChanTS014ProvEntry,
       "mscDataSigChanTS014Side": mscDataSigChanTS014Side,
       "mscDataSigChanTS014OperTable": mscDataSigChanTS014OperTable,
       "mscDataSigChanTS014OperEntry": mscDataSigChanTS014OperEntry,
       "mscDataSigChanTS014ActiveChannels": mscDataSigChanTS014ActiveChannels,
       "mscDataSigChanTS014PeakActiveChannels": mscDataSigChanTS014PeakActiveChannels,
       "mscDataSigChanTS014DChanStatus": mscDataSigChanTS014DChanStatus,
       "mscDataSigChanTS014ToolsTable": mscDataSigChanTS014ToolsTable,
       "mscDataSigChanTS014ToolsEntry": mscDataSigChanTS014ToolsEntry,
       "mscDataSigChanTS014Tracing": mscDataSigChanTS014Tracing,
       "disdnTS014MIB": disdnTS014MIB,
       "disdnTS014Group": disdnTS014Group,
       "disdnTS014GroupCA": disdnTS014GroupCA,
       "disdnTS014GroupCA02": disdnTS014GroupCA02,
       "disdnTS014GroupCA02A": disdnTS014GroupCA02A,
       "disdnTS014Capabilities": disdnTS014Capabilities,
       "disdnTS014CapabilitiesCA": disdnTS014CapabilitiesCA,
       "disdnTS014CapabilitiesCA02": disdnTS014CapabilitiesCA02,
       "disdnTS014CapabilitiesCA02A": disdnTS014CapabilitiesCA02A}
)
