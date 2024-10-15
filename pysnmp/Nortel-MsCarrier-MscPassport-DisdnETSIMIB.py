# SNMP MIB module (Nortel-MsCarrier-MscPassport-DisdnETSIMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DisdnETSIMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:10 2024
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

_MscDataSigChanEtsi_ObjectIdentity = ObjectIdentity
mscDataSigChanEtsi = _MscDataSigChanEtsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10)
)
_MscDataSigChanEtsiRowStatusTable_Object = MibTable
mscDataSigChanEtsiRowStatusTable = _MscDataSigChanEtsiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiRowStatusTable.setStatus("mandatory")
_MscDataSigChanEtsiRowStatusEntry_Object = MibTableRow
mscDataSigChanEtsiRowStatusEntry = _MscDataSigChanEtsiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1)
)
mscDataSigChanEtsiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiRowStatusEntry.setStatus("mandatory")
_MscDataSigChanEtsiRowStatus_Type = RowStatus
_MscDataSigChanEtsiRowStatus_Object = MibTableColumn
mscDataSigChanEtsiRowStatus = _MscDataSigChanEtsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1, 1),
    _MscDataSigChanEtsiRowStatus_Type()
)
mscDataSigChanEtsiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiRowStatus.setStatus("mandatory")
_MscDataSigChanEtsiComponentName_Type = DisplayString
_MscDataSigChanEtsiComponentName_Object = MibTableColumn
mscDataSigChanEtsiComponentName = _MscDataSigChanEtsiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1, 2),
    _MscDataSigChanEtsiComponentName_Type()
)
mscDataSigChanEtsiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiComponentName.setStatus("mandatory")
_MscDataSigChanEtsiStorageType_Type = StorageType
_MscDataSigChanEtsiStorageType_Object = MibTableColumn
mscDataSigChanEtsiStorageType = _MscDataSigChanEtsiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1, 4),
    _MscDataSigChanEtsiStorageType_Type()
)
mscDataSigChanEtsiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiStorageType.setStatus("mandatory")
_MscDataSigChanEtsiIndex_Type = NonReplicated
_MscDataSigChanEtsiIndex_Object = MibTableColumn
mscDataSigChanEtsiIndex = _MscDataSigChanEtsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1, 10),
    _MscDataSigChanEtsiIndex_Type()
)
mscDataSigChanEtsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiIndex.setStatus("mandatory")
_MscDataSigChanEtsiFramer_ObjectIdentity = ObjectIdentity
mscDataSigChanEtsiFramer = _MscDataSigChanEtsiFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2)
)
_MscDataSigChanEtsiFramerRowStatusTable_Object = MibTable
mscDataSigChanEtsiFramerRowStatusTable = _MscDataSigChanEtsiFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1)
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerRowStatusTable.setStatus("mandatory")
_MscDataSigChanEtsiFramerRowStatusEntry_Object = MibTableRow
mscDataSigChanEtsiFramerRowStatusEntry = _MscDataSigChanEtsiFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1)
)
mscDataSigChanEtsiFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerRowStatusEntry.setStatus("mandatory")
_MscDataSigChanEtsiFramerRowStatus_Type = RowStatus
_MscDataSigChanEtsiFramerRowStatus_Object = MibTableColumn
mscDataSigChanEtsiFramerRowStatus = _MscDataSigChanEtsiFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1, 1),
    _MscDataSigChanEtsiFramerRowStatus_Type()
)
mscDataSigChanEtsiFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerRowStatus.setStatus("mandatory")
_MscDataSigChanEtsiFramerComponentName_Type = DisplayString
_MscDataSigChanEtsiFramerComponentName_Object = MibTableColumn
mscDataSigChanEtsiFramerComponentName = _MscDataSigChanEtsiFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1, 2),
    _MscDataSigChanEtsiFramerComponentName_Type()
)
mscDataSigChanEtsiFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerComponentName.setStatus("mandatory")
_MscDataSigChanEtsiFramerStorageType_Type = StorageType
_MscDataSigChanEtsiFramerStorageType_Object = MibTableColumn
mscDataSigChanEtsiFramerStorageType = _MscDataSigChanEtsiFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1, 4),
    _MscDataSigChanEtsiFramerStorageType_Type()
)
mscDataSigChanEtsiFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerStorageType.setStatus("mandatory")
_MscDataSigChanEtsiFramerIndex_Type = NonReplicated
_MscDataSigChanEtsiFramerIndex_Object = MibTableColumn
mscDataSigChanEtsiFramerIndex = _MscDataSigChanEtsiFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1, 10),
    _MscDataSigChanEtsiFramerIndex_Type()
)
mscDataSigChanEtsiFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerIndex.setStatus("mandatory")
_MscDataSigChanEtsiFramerProvTable_Object = MibTable
mscDataSigChanEtsiFramerProvTable = _MscDataSigChanEtsiFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 10)
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerProvTable.setStatus("mandatory")
_MscDataSigChanEtsiFramerProvEntry_Object = MibTableRow
mscDataSigChanEtsiFramerProvEntry = _MscDataSigChanEtsiFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 10, 1)
)
mscDataSigChanEtsiFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerProvEntry.setStatus("mandatory")
_MscDataSigChanEtsiFramerInterfaceName_Type = Link
_MscDataSigChanEtsiFramerInterfaceName_Object = MibTableColumn
mscDataSigChanEtsiFramerInterfaceName = _MscDataSigChanEtsiFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 10, 1, 1),
    _MscDataSigChanEtsiFramerInterfaceName_Type()
)
mscDataSigChanEtsiFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerInterfaceName.setStatus("mandatory")
_MscDataSigChanEtsiFramerStateTable_Object = MibTable
mscDataSigChanEtsiFramerStateTable = _MscDataSigChanEtsiFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12)
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerStateTable.setStatus("mandatory")
_MscDataSigChanEtsiFramerStateEntry_Object = MibTableRow
mscDataSigChanEtsiFramerStateEntry = _MscDataSigChanEtsiFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12, 1)
)
mscDataSigChanEtsiFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerStateEntry.setStatus("mandatory")


class _MscDataSigChanEtsiFramerAdminState_Type(Integer32):
    """Custom type mscDataSigChanEtsiFramerAdminState based on Integer32"""
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


_MscDataSigChanEtsiFramerAdminState_Type.__name__ = "Integer32"
_MscDataSigChanEtsiFramerAdminState_Object = MibTableColumn
mscDataSigChanEtsiFramerAdminState = _MscDataSigChanEtsiFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12, 1, 1),
    _MscDataSigChanEtsiFramerAdminState_Type()
)
mscDataSigChanEtsiFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerAdminState.setStatus("mandatory")


class _MscDataSigChanEtsiFramerOperationalState_Type(Integer32):
    """Custom type mscDataSigChanEtsiFramerOperationalState based on Integer32"""
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


_MscDataSigChanEtsiFramerOperationalState_Type.__name__ = "Integer32"
_MscDataSigChanEtsiFramerOperationalState_Object = MibTableColumn
mscDataSigChanEtsiFramerOperationalState = _MscDataSigChanEtsiFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12, 1, 2),
    _MscDataSigChanEtsiFramerOperationalState_Type()
)
mscDataSigChanEtsiFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerOperationalState.setStatus("mandatory")


class _MscDataSigChanEtsiFramerUsageState_Type(Integer32):
    """Custom type mscDataSigChanEtsiFramerUsageState based on Integer32"""
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


_MscDataSigChanEtsiFramerUsageState_Type.__name__ = "Integer32"
_MscDataSigChanEtsiFramerUsageState_Object = MibTableColumn
mscDataSigChanEtsiFramerUsageState = _MscDataSigChanEtsiFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12, 1, 3),
    _MscDataSigChanEtsiFramerUsageState_Type()
)
mscDataSigChanEtsiFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerUsageState.setStatus("mandatory")
_MscDataSigChanEtsiFramerStatsTable_Object = MibTable
mscDataSigChanEtsiFramerStatsTable = _MscDataSigChanEtsiFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerStatsTable.setStatus("mandatory")
_MscDataSigChanEtsiFramerStatsEntry_Object = MibTableRow
mscDataSigChanEtsiFramerStatsEntry = _MscDataSigChanEtsiFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1)
)
mscDataSigChanEtsiFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiFramerIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerStatsEntry.setStatus("mandatory")


class _MscDataSigChanEtsiFramerFrmToIf_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerFrmToIf_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerFrmToIf_Object = MibTableColumn
mscDataSigChanEtsiFramerFrmToIf = _MscDataSigChanEtsiFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 1),
    _MscDataSigChanEtsiFramerFrmToIf_Type()
)
mscDataSigChanEtsiFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerFrmToIf.setStatus("mandatory")


class _MscDataSigChanEtsiFramerFrmFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerFrmFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerFrmFromIf_Object = MibTableColumn
mscDataSigChanEtsiFramerFrmFromIf = _MscDataSigChanEtsiFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 2),
    _MscDataSigChanEtsiFramerFrmFromIf_Type()
)
mscDataSigChanEtsiFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerFrmFromIf.setStatus("mandatory")


class _MscDataSigChanEtsiFramerOctetFromIf_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerOctetFromIf_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerOctetFromIf_Object = MibTableColumn
mscDataSigChanEtsiFramerOctetFromIf = _MscDataSigChanEtsiFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 3),
    _MscDataSigChanEtsiFramerOctetFromIf_Type()
)
mscDataSigChanEtsiFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerOctetFromIf.setStatus("mandatory")


class _MscDataSigChanEtsiFramerAborts_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerAborts_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerAborts_Object = MibTableColumn
mscDataSigChanEtsiFramerAborts = _MscDataSigChanEtsiFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 4),
    _MscDataSigChanEtsiFramerAborts_Type()
)
mscDataSigChanEtsiFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerAborts.setStatus("mandatory")


class _MscDataSigChanEtsiFramerCrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerCrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerCrcErrors_Object = MibTableColumn
mscDataSigChanEtsiFramerCrcErrors = _MscDataSigChanEtsiFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 5),
    _MscDataSigChanEtsiFramerCrcErrors_Type()
)
mscDataSigChanEtsiFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerCrcErrors.setStatus("mandatory")


class _MscDataSigChanEtsiFramerLrcErrors_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerLrcErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerLrcErrors_Object = MibTableColumn
mscDataSigChanEtsiFramerLrcErrors = _MscDataSigChanEtsiFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 6),
    _MscDataSigChanEtsiFramerLrcErrors_Type()
)
mscDataSigChanEtsiFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerLrcErrors.setStatus("mandatory")


class _MscDataSigChanEtsiFramerNonOctetErrors_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerNonOctetErrors_Object = MibTableColumn
mscDataSigChanEtsiFramerNonOctetErrors = _MscDataSigChanEtsiFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 7),
    _MscDataSigChanEtsiFramerNonOctetErrors_Type()
)
mscDataSigChanEtsiFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerNonOctetErrors.setStatus("mandatory")


class _MscDataSigChanEtsiFramerOverruns_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerOverruns_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerOverruns_Object = MibTableColumn
mscDataSigChanEtsiFramerOverruns = _MscDataSigChanEtsiFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 8),
    _MscDataSigChanEtsiFramerOverruns_Type()
)
mscDataSigChanEtsiFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerOverruns.setStatus("mandatory")


class _MscDataSigChanEtsiFramerUnderruns_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerUnderruns_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerUnderruns_Object = MibTableColumn
mscDataSigChanEtsiFramerUnderruns = _MscDataSigChanEtsiFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 9),
    _MscDataSigChanEtsiFramerUnderruns_Type()
)
mscDataSigChanEtsiFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerUnderruns.setStatus("mandatory")


class _MscDataSigChanEtsiFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscDataSigChanEtsiFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiFramerLargeFrmErrors_Object = MibTableColumn
mscDataSigChanEtsiFramerLargeFrmErrors = _MscDataSigChanEtsiFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 10),
    _MscDataSigChanEtsiFramerLargeFrmErrors_Type()
)
mscDataSigChanEtsiFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiFramerLargeFrmErrors.setStatus("mandatory")
_MscDataSigChanEtsiL2Table_Object = MibTable
mscDataSigChanEtsiL2Table = _MscDataSigChanEtsiL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11)
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiL2Table.setStatus("mandatory")
_MscDataSigChanEtsiL2Entry_Object = MibTableRow
mscDataSigChanEtsiL2Entry = _MscDataSigChanEtsiL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1)
)
mscDataSigChanEtsiL2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiL2Entry.setStatus("mandatory")


class _MscDataSigChanEtsiT23_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscDataSigChanEtsiT23_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiT23_Object = MibTableColumn
mscDataSigChanEtsiT23 = _MscDataSigChanEtsiT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 1),
    _MscDataSigChanEtsiT23_Type()
)
mscDataSigChanEtsiT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiT23.setStatus("mandatory")


class _MscDataSigChanEtsiT200_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiT200 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscDataSigChanEtsiT200_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiT200_Object = MibTableColumn
mscDataSigChanEtsiT200 = _MscDataSigChanEtsiT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 2),
    _MscDataSigChanEtsiT200_Type()
)
mscDataSigChanEtsiT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiT200.setStatus("mandatory")


class _MscDataSigChanEtsiN200_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscDataSigChanEtsiN200_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiN200_Object = MibTableColumn
mscDataSigChanEtsiN200 = _MscDataSigChanEtsiN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 3),
    _MscDataSigChanEtsiN200_Type()
)
mscDataSigChanEtsiN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiN200.setStatus("mandatory")


class _MscDataSigChanEtsiT203_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_MscDataSigChanEtsiT203_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiT203_Object = MibTableColumn
mscDataSigChanEtsiT203 = _MscDataSigChanEtsiT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 4),
    _MscDataSigChanEtsiT203_Type()
)
mscDataSigChanEtsiT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiT203.setStatus("mandatory")


class _MscDataSigChanEtsiN201_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiN201 based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 260),
    )


_MscDataSigChanEtsiN201_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiN201_Object = MibTableColumn
mscDataSigChanEtsiN201 = _MscDataSigChanEtsiN201_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 5),
    _MscDataSigChanEtsiN201_Type()
)
mscDataSigChanEtsiN201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiN201.setStatus("mandatory")


class _MscDataSigChanEtsiCircuitSwitchedK_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 632),
    )


_MscDataSigChanEtsiCircuitSwitchedK_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiCircuitSwitchedK_Object = MibTableColumn
mscDataSigChanEtsiCircuitSwitchedK = _MscDataSigChanEtsiCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 6),
    _MscDataSigChanEtsiCircuitSwitchedK_Type()
)
mscDataSigChanEtsiCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiCircuitSwitchedK.setStatus("mandatory")
_MscDataSigChanEtsiProvTable_Object = MibTable
mscDataSigChanEtsiProvTable = _MscDataSigChanEtsiProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 13)
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiProvTable.setStatus("mandatory")
_MscDataSigChanEtsiProvEntry_Object = MibTableRow
mscDataSigChanEtsiProvEntry = _MscDataSigChanEtsiProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 13, 1)
)
mscDataSigChanEtsiProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiProvEntry.setStatus("mandatory")


class _MscDataSigChanEtsiSide_Type(Integer32):
    """Custom type mscDataSigChanEtsiSide based on Integer32"""
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


_MscDataSigChanEtsiSide_Type.__name__ = "Integer32"
_MscDataSigChanEtsiSide_Object = MibTableColumn
mscDataSigChanEtsiSide = _MscDataSigChanEtsiSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 13, 1, 1),
    _MscDataSigChanEtsiSide_Type()
)
mscDataSigChanEtsiSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiSide.setStatus("mandatory")
_MscDataSigChanEtsiOperTable_Object = MibTable
mscDataSigChanEtsiOperTable = _MscDataSigChanEtsiOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15)
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiOperTable.setStatus("mandatory")
_MscDataSigChanEtsiOperEntry_Object = MibTableRow
mscDataSigChanEtsiOperEntry = _MscDataSigChanEtsiOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15, 1)
)
mscDataSigChanEtsiOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiOperEntry.setStatus("mandatory")


class _MscDataSigChanEtsiActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanEtsiActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiActiveChannels_Object = MibTableColumn
mscDataSigChanEtsiActiveChannels = _MscDataSigChanEtsiActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15, 1, 1),
    _MscDataSigChanEtsiActiveChannels_Type()
)
mscDataSigChanEtsiActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiActiveChannels.setStatus("mandatory")


class _MscDataSigChanEtsiPeakActiveChannels_Type(Unsigned32):
    """Custom type mscDataSigChanEtsiPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscDataSigChanEtsiPeakActiveChannels_Type.__name__ = "Unsigned32"
_MscDataSigChanEtsiPeakActiveChannels_Object = MibTableColumn
mscDataSigChanEtsiPeakActiveChannels = _MscDataSigChanEtsiPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15, 1, 4),
    _MscDataSigChanEtsiPeakActiveChannels_Type()
)
mscDataSigChanEtsiPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiPeakActiveChannels.setStatus("mandatory")


class _MscDataSigChanEtsiDChanStatus_Type(Integer32):
    """Custom type mscDataSigChanEtsiDChanStatus based on Integer32"""
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


_MscDataSigChanEtsiDChanStatus_Type.__name__ = "Integer32"
_MscDataSigChanEtsiDChanStatus_Object = MibTableColumn
mscDataSigChanEtsiDChanStatus = _MscDataSigChanEtsiDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15, 1, 7),
    _MscDataSigChanEtsiDChanStatus_Type()
)
mscDataSigChanEtsiDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiDChanStatus.setStatus("mandatory")
_MscDataSigChanEtsiToolsTable_Object = MibTable
mscDataSigChanEtsiToolsTable = _MscDataSigChanEtsiToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 16)
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiToolsTable.setStatus("mandatory")
_MscDataSigChanEtsiToolsEntry_Object = MibTableRow
mscDataSigChanEtsiToolsEntry = _MscDataSigChanEtsiToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 16, 1)
)
mscDataSigChanEtsiToolsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"),
)
if mibBuilder.loadTexts:
    mscDataSigChanEtsiToolsEntry.setStatus("mandatory")


class _MscDataSigChanEtsiTracing_Type(OctetString):
    """Custom type mscDataSigChanEtsiTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscDataSigChanEtsiTracing_Type.__name__ = "OctetString"
_MscDataSigChanEtsiTracing_Object = MibTableColumn
mscDataSigChanEtsiTracing = _MscDataSigChanEtsiTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 16, 1, 1),
    _MscDataSigChanEtsiTracing_Type()
)
mscDataSigChanEtsiTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscDataSigChanEtsiTracing.setStatus("mandatory")
_DisdnETSIMIB_ObjectIdentity = ObjectIdentity
disdnETSIMIB = _DisdnETSIMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117)
)
_DisdnETSIGroup_ObjectIdentity = ObjectIdentity
disdnETSIGroup = _DisdnETSIGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 1)
)
_DisdnETSIGroupCA_ObjectIdentity = ObjectIdentity
disdnETSIGroupCA = _DisdnETSIGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 1, 1)
)
_DisdnETSIGroupCA02_ObjectIdentity = ObjectIdentity
disdnETSIGroupCA02 = _DisdnETSIGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 1, 1, 3)
)
_DisdnETSIGroupCA02A_ObjectIdentity = ObjectIdentity
disdnETSIGroupCA02A = _DisdnETSIGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 1, 1, 3, 2)
)
_DisdnETSICapabilities_ObjectIdentity = ObjectIdentity
disdnETSICapabilities = _DisdnETSICapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 3)
)
_DisdnETSICapabilitiesCA_ObjectIdentity = ObjectIdentity
disdnETSICapabilitiesCA = _DisdnETSICapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 3, 1)
)
_DisdnETSICapabilitiesCA02_ObjectIdentity = ObjectIdentity
disdnETSICapabilitiesCA02 = _DisdnETSICapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 3, 1, 3)
)
_DisdnETSICapabilitiesCA02A_ObjectIdentity = ObjectIdentity
disdnETSICapabilitiesCA02A = _DisdnETSICapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DisdnETSIMIB",
    **{"mscDataSigChanEtsi": mscDataSigChanEtsi,
       "mscDataSigChanEtsiRowStatusTable": mscDataSigChanEtsiRowStatusTable,
       "mscDataSigChanEtsiRowStatusEntry": mscDataSigChanEtsiRowStatusEntry,
       "mscDataSigChanEtsiRowStatus": mscDataSigChanEtsiRowStatus,
       "mscDataSigChanEtsiComponentName": mscDataSigChanEtsiComponentName,
       "mscDataSigChanEtsiStorageType": mscDataSigChanEtsiStorageType,
       "mscDataSigChanEtsiIndex": mscDataSigChanEtsiIndex,
       "mscDataSigChanEtsiFramer": mscDataSigChanEtsiFramer,
       "mscDataSigChanEtsiFramerRowStatusTable": mscDataSigChanEtsiFramerRowStatusTable,
       "mscDataSigChanEtsiFramerRowStatusEntry": mscDataSigChanEtsiFramerRowStatusEntry,
       "mscDataSigChanEtsiFramerRowStatus": mscDataSigChanEtsiFramerRowStatus,
       "mscDataSigChanEtsiFramerComponentName": mscDataSigChanEtsiFramerComponentName,
       "mscDataSigChanEtsiFramerStorageType": mscDataSigChanEtsiFramerStorageType,
       "mscDataSigChanEtsiFramerIndex": mscDataSigChanEtsiFramerIndex,
       "mscDataSigChanEtsiFramerProvTable": mscDataSigChanEtsiFramerProvTable,
       "mscDataSigChanEtsiFramerProvEntry": mscDataSigChanEtsiFramerProvEntry,
       "mscDataSigChanEtsiFramerInterfaceName": mscDataSigChanEtsiFramerInterfaceName,
       "mscDataSigChanEtsiFramerStateTable": mscDataSigChanEtsiFramerStateTable,
       "mscDataSigChanEtsiFramerStateEntry": mscDataSigChanEtsiFramerStateEntry,
       "mscDataSigChanEtsiFramerAdminState": mscDataSigChanEtsiFramerAdminState,
       "mscDataSigChanEtsiFramerOperationalState": mscDataSigChanEtsiFramerOperationalState,
       "mscDataSigChanEtsiFramerUsageState": mscDataSigChanEtsiFramerUsageState,
       "mscDataSigChanEtsiFramerStatsTable": mscDataSigChanEtsiFramerStatsTable,
       "mscDataSigChanEtsiFramerStatsEntry": mscDataSigChanEtsiFramerStatsEntry,
       "mscDataSigChanEtsiFramerFrmToIf": mscDataSigChanEtsiFramerFrmToIf,
       "mscDataSigChanEtsiFramerFrmFromIf": mscDataSigChanEtsiFramerFrmFromIf,
       "mscDataSigChanEtsiFramerOctetFromIf": mscDataSigChanEtsiFramerOctetFromIf,
       "mscDataSigChanEtsiFramerAborts": mscDataSigChanEtsiFramerAborts,
       "mscDataSigChanEtsiFramerCrcErrors": mscDataSigChanEtsiFramerCrcErrors,
       "mscDataSigChanEtsiFramerLrcErrors": mscDataSigChanEtsiFramerLrcErrors,
       "mscDataSigChanEtsiFramerNonOctetErrors": mscDataSigChanEtsiFramerNonOctetErrors,
       "mscDataSigChanEtsiFramerOverruns": mscDataSigChanEtsiFramerOverruns,
       "mscDataSigChanEtsiFramerUnderruns": mscDataSigChanEtsiFramerUnderruns,
       "mscDataSigChanEtsiFramerLargeFrmErrors": mscDataSigChanEtsiFramerLargeFrmErrors,
       "mscDataSigChanEtsiL2Table": mscDataSigChanEtsiL2Table,
       "mscDataSigChanEtsiL2Entry": mscDataSigChanEtsiL2Entry,
       "mscDataSigChanEtsiT23": mscDataSigChanEtsiT23,
       "mscDataSigChanEtsiT200": mscDataSigChanEtsiT200,
       "mscDataSigChanEtsiN200": mscDataSigChanEtsiN200,
       "mscDataSigChanEtsiT203": mscDataSigChanEtsiT203,
       "mscDataSigChanEtsiN201": mscDataSigChanEtsiN201,
       "mscDataSigChanEtsiCircuitSwitchedK": mscDataSigChanEtsiCircuitSwitchedK,
       "mscDataSigChanEtsiProvTable": mscDataSigChanEtsiProvTable,
       "mscDataSigChanEtsiProvEntry": mscDataSigChanEtsiProvEntry,
       "mscDataSigChanEtsiSide": mscDataSigChanEtsiSide,
       "mscDataSigChanEtsiOperTable": mscDataSigChanEtsiOperTable,
       "mscDataSigChanEtsiOperEntry": mscDataSigChanEtsiOperEntry,
       "mscDataSigChanEtsiActiveChannels": mscDataSigChanEtsiActiveChannels,
       "mscDataSigChanEtsiPeakActiveChannels": mscDataSigChanEtsiPeakActiveChannels,
       "mscDataSigChanEtsiDChanStatus": mscDataSigChanEtsiDChanStatus,
       "mscDataSigChanEtsiToolsTable": mscDataSigChanEtsiToolsTable,
       "mscDataSigChanEtsiToolsEntry": mscDataSigChanEtsiToolsEntry,
       "mscDataSigChanEtsiTracing": mscDataSigChanEtsiTracing,
       "disdnETSIMIB": disdnETSIMIB,
       "disdnETSIGroup": disdnETSIGroup,
       "disdnETSIGroupCA": disdnETSIGroupCA,
       "disdnETSIGroupCA02": disdnETSIGroupCA02,
       "disdnETSIGroupCA02A": disdnETSIGroupCA02A,
       "disdnETSICapabilities": disdnETSICapabilities,
       "disdnETSICapabilitiesCA": disdnETSICapabilitiesCA,
       "disdnETSICapabilitiesCA02": disdnETSICapabilitiesCA02,
       "disdnETSICapabilitiesCA02A": disdnETSICapabilitiesCA02A}
)
