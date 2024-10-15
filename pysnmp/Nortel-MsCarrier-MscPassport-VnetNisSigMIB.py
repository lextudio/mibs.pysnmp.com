# SNMP MIB module (Nortel-MsCarrier-MscPassport-VnetNisSigMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VnetNisSigMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:19 2024
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

(mscSigChan,
 mscSigChanIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB",
    "mscSigChan",
    "mscSigChanIndex")

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

_MscSigChanNis_ObjectIdentity = ObjectIdentity
mscSigChanNis = _MscSigChanNis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8)
)
_MscSigChanNisRowStatusTable_Object = MibTable
mscSigChanNisRowStatusTable = _MscSigChanNisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 1)
)
if mibBuilder.loadTexts:
    mscSigChanNisRowStatusTable.setStatus("mandatory")
_MscSigChanNisRowStatusEntry_Object = MibTableRow
mscSigChanNisRowStatusEntry = _MscSigChanNisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 1, 1)
)
mscSigChanNisRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisRowStatusEntry.setStatus("mandatory")
_MscSigChanNisRowStatus_Type = RowStatus
_MscSigChanNisRowStatus_Object = MibTableColumn
mscSigChanNisRowStatus = _MscSigChanNisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 1, 1, 1),
    _MscSigChanNisRowStatus_Type()
)
mscSigChanNisRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisRowStatus.setStatus("mandatory")
_MscSigChanNisComponentName_Type = DisplayString
_MscSigChanNisComponentName_Object = MibTableColumn
mscSigChanNisComponentName = _MscSigChanNisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 1, 1, 2),
    _MscSigChanNisComponentName_Type()
)
mscSigChanNisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisComponentName.setStatus("mandatory")
_MscSigChanNisStorageType_Type = StorageType
_MscSigChanNisStorageType_Object = MibTableColumn
mscSigChanNisStorageType = _MscSigChanNisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 1, 1, 4),
    _MscSigChanNisStorageType_Type()
)
mscSigChanNisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisStorageType.setStatus("mandatory")
_MscSigChanNisIndex_Type = NonReplicated
_MscSigChanNisIndex_Object = MibTableColumn
mscSigChanNisIndex = _MscSigChanNisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 1, 1, 10),
    _MscSigChanNisIndex_Type()
)
mscSigChanNisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanNisIndex.setStatus("mandatory")
_MscSigChanNisFramer_ObjectIdentity = ObjectIdentity
mscSigChanNisFramer = _MscSigChanNisFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2)
)
_MscSigChanNisFramerRowStatusTable_Object = MibTable
mscSigChanNisFramerRowStatusTable = _MscSigChanNisFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscSigChanNisFramerRowStatusTable.setStatus("mandatory")
_MscSigChanNisFramerRowStatusEntry_Object = MibTableRow
mscSigChanNisFramerRowStatusEntry = _MscSigChanNisFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 1, 1)
)
mscSigChanNisFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisFramerRowStatusEntry.setStatus("mandatory")
_MscSigChanNisFramerRowStatus_Type = RowStatus
_MscSigChanNisFramerRowStatus_Object = MibTableColumn
mscSigChanNisFramerRowStatus = _MscSigChanNisFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 1, 1, 1),
    _MscSigChanNisFramerRowStatus_Type()
)
mscSigChanNisFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerRowStatus.setStatus("mandatory")
_MscSigChanNisFramerComponentName_Type = DisplayString
_MscSigChanNisFramerComponentName_Object = MibTableColumn
mscSigChanNisFramerComponentName = _MscSigChanNisFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 1, 1, 2),
    _MscSigChanNisFramerComponentName_Type()
)
mscSigChanNisFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerComponentName.setStatus("mandatory")
_MscSigChanNisFramerStorageType_Type = StorageType
_MscSigChanNisFramerStorageType_Object = MibTableColumn
mscSigChanNisFramerStorageType = _MscSigChanNisFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 1, 1, 4),
    _MscSigChanNisFramerStorageType_Type()
)
mscSigChanNisFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerStorageType.setStatus("mandatory")
_MscSigChanNisFramerIndex_Type = NonReplicated
_MscSigChanNisFramerIndex_Object = MibTableColumn
mscSigChanNisFramerIndex = _MscSigChanNisFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 1, 1, 10),
    _MscSigChanNisFramerIndex_Type()
)
mscSigChanNisFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanNisFramerIndex.setStatus("mandatory")
_MscSigChanNisFramerProvTable_Object = MibTable
mscSigChanNisFramerProvTable = _MscSigChanNisFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 10)
)
if mibBuilder.loadTexts:
    mscSigChanNisFramerProvTable.setStatus("mandatory")
_MscSigChanNisFramerProvEntry_Object = MibTableRow
mscSigChanNisFramerProvEntry = _MscSigChanNisFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 10, 1)
)
mscSigChanNisFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisFramerProvEntry.setStatus("mandatory")
_MscSigChanNisFramerInterfaceName_Type = Link
_MscSigChanNisFramerInterfaceName_Object = MibTableColumn
mscSigChanNisFramerInterfaceName = _MscSigChanNisFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 10, 1, 1),
    _MscSigChanNisFramerInterfaceName_Type()
)
mscSigChanNisFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisFramerInterfaceName.setStatus("mandatory")
_MscSigChanNisFramerStateTable_Object = MibTable
mscSigChanNisFramerStateTable = _MscSigChanNisFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 12)
)
if mibBuilder.loadTexts:
    mscSigChanNisFramerStateTable.setStatus("mandatory")
_MscSigChanNisFramerStateEntry_Object = MibTableRow
mscSigChanNisFramerStateEntry = _MscSigChanNisFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 12, 1)
)
mscSigChanNisFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisFramerStateEntry.setStatus("mandatory")


class _MscSigChanNisFramerAdminState_Type(Integer32):
    """Custom type mscSigChanNisFramerAdminState based on Integer32"""
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


_MscSigChanNisFramerAdminState_Type.__name__ = "Integer32"
_MscSigChanNisFramerAdminState_Object = MibTableColumn
mscSigChanNisFramerAdminState = _MscSigChanNisFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 12, 1, 1),
    _MscSigChanNisFramerAdminState_Type()
)
mscSigChanNisFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerAdminState.setStatus("mandatory")


class _MscSigChanNisFramerOperationalState_Type(Integer32):
    """Custom type mscSigChanNisFramerOperationalState based on Integer32"""
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


_MscSigChanNisFramerOperationalState_Type.__name__ = "Integer32"
_MscSigChanNisFramerOperationalState_Object = MibTableColumn
mscSigChanNisFramerOperationalState = _MscSigChanNisFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 12, 1, 2),
    _MscSigChanNisFramerOperationalState_Type()
)
mscSigChanNisFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerOperationalState.setStatus("mandatory")


class _MscSigChanNisFramerUsageState_Type(Integer32):
    """Custom type mscSigChanNisFramerUsageState based on Integer32"""
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


_MscSigChanNisFramerUsageState_Type.__name__ = "Integer32"
_MscSigChanNisFramerUsageState_Object = MibTableColumn
mscSigChanNisFramerUsageState = _MscSigChanNisFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 12, 1, 3),
    _MscSigChanNisFramerUsageState_Type()
)
mscSigChanNisFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerUsageState.setStatus("mandatory")
_MscSigChanNisFramerStatsTable_Object = MibTable
mscSigChanNisFramerStatsTable = _MscSigChanNisFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13)
)
if mibBuilder.loadTexts:
    mscSigChanNisFramerStatsTable.setStatus("mandatory")
_MscSigChanNisFramerStatsEntry_Object = MibTableRow
mscSigChanNisFramerStatsEntry = _MscSigChanNisFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1)
)
mscSigChanNisFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisFramerStatsEntry.setStatus("mandatory")


class _MscSigChanNisFramerFrmToIf_Type(Unsigned32):
    """Custom type mscSigChanNisFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerFrmToIf_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerFrmToIf_Object = MibTableColumn
mscSigChanNisFramerFrmToIf = _MscSigChanNisFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 1),
    _MscSigChanNisFramerFrmToIf_Type()
)
mscSigChanNisFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerFrmToIf.setStatus("mandatory")


class _MscSigChanNisFramerFrmFromIf_Type(Unsigned32):
    """Custom type mscSigChanNisFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerFrmFromIf_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerFrmFromIf_Object = MibTableColumn
mscSigChanNisFramerFrmFromIf = _MscSigChanNisFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 2),
    _MscSigChanNisFramerFrmFromIf_Type()
)
mscSigChanNisFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerFrmFromIf.setStatus("mandatory")


class _MscSigChanNisFramerOctetFromIf_Type(Unsigned32):
    """Custom type mscSigChanNisFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerOctetFromIf_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerOctetFromIf_Object = MibTableColumn
mscSigChanNisFramerOctetFromIf = _MscSigChanNisFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 3),
    _MscSigChanNisFramerOctetFromIf_Type()
)
mscSigChanNisFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerOctetFromIf.setStatus("mandatory")


class _MscSigChanNisFramerAborts_Type(Unsigned32):
    """Custom type mscSigChanNisFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerAborts_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerAborts_Object = MibTableColumn
mscSigChanNisFramerAborts = _MscSigChanNisFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 4),
    _MscSigChanNisFramerAborts_Type()
)
mscSigChanNisFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerAborts.setStatus("mandatory")


class _MscSigChanNisFramerCrcErrors_Type(Unsigned32):
    """Custom type mscSigChanNisFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerCrcErrors_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerCrcErrors_Object = MibTableColumn
mscSigChanNisFramerCrcErrors = _MscSigChanNisFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 5),
    _MscSigChanNisFramerCrcErrors_Type()
)
mscSigChanNisFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerCrcErrors.setStatus("mandatory")


class _MscSigChanNisFramerLrcErrors_Type(Unsigned32):
    """Custom type mscSigChanNisFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerLrcErrors_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerLrcErrors_Object = MibTableColumn
mscSigChanNisFramerLrcErrors = _MscSigChanNisFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 6),
    _MscSigChanNisFramerLrcErrors_Type()
)
mscSigChanNisFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerLrcErrors.setStatus("mandatory")


class _MscSigChanNisFramerNonOctetErrors_Type(Unsigned32):
    """Custom type mscSigChanNisFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerNonOctetErrors_Object = MibTableColumn
mscSigChanNisFramerNonOctetErrors = _MscSigChanNisFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 7),
    _MscSigChanNisFramerNonOctetErrors_Type()
)
mscSigChanNisFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerNonOctetErrors.setStatus("mandatory")


class _MscSigChanNisFramerOverruns_Type(Unsigned32):
    """Custom type mscSigChanNisFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerOverruns_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerOverruns_Object = MibTableColumn
mscSigChanNisFramerOverruns = _MscSigChanNisFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 8),
    _MscSigChanNisFramerOverruns_Type()
)
mscSigChanNisFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerOverruns.setStatus("mandatory")


class _MscSigChanNisFramerUnderruns_Type(Unsigned32):
    """Custom type mscSigChanNisFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerUnderruns_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerUnderruns_Object = MibTableColumn
mscSigChanNisFramerUnderruns = _MscSigChanNisFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 9),
    _MscSigChanNisFramerUnderruns_Type()
)
mscSigChanNisFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerUnderruns.setStatus("mandatory")


class _MscSigChanNisFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type mscSigChanNisFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_MscSigChanNisFramerLargeFrmErrors_Object = MibTableColumn
mscSigChanNisFramerLargeFrmErrors = _MscSigChanNisFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 2, 13, 1, 10),
    _MscSigChanNisFramerLargeFrmErrors_Type()
)
mscSigChanNisFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisFramerLargeFrmErrors.setStatus("mandatory")
_MscSigChanNisL2Table_Object = MibTable
mscSigChanNisL2Table = _MscSigChanNisL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 11)
)
if mibBuilder.loadTexts:
    mscSigChanNisL2Table.setStatus("mandatory")
_MscSigChanNisL2Entry_Object = MibTableRow
mscSigChanNisL2Entry = _MscSigChanNisL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 11, 1)
)
mscSigChanNisL2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisL2Entry.setStatus("mandatory")


class _MscSigChanNisT23_Type(Unsigned32):
    """Custom type mscSigChanNisT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscSigChanNisT23_Type.__name__ = "Unsigned32"
_MscSigChanNisT23_Object = MibTableColumn
mscSigChanNisT23 = _MscSigChanNisT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 11, 1, 1),
    _MscSigChanNisT23_Type()
)
mscSigChanNisT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisT23.setStatus("mandatory")


class _MscSigChanNisT200_Type(Unsigned32):
    """Custom type mscSigChanNisT200 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscSigChanNisT200_Type.__name__ = "Unsigned32"
_MscSigChanNisT200_Object = MibTableColumn
mscSigChanNisT200 = _MscSigChanNisT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 11, 1, 2),
    _MscSigChanNisT200_Type()
)
mscSigChanNisT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisT200.setStatus("mandatory")


class _MscSigChanNisN200_Type(Unsigned32):
    """Custom type mscSigChanNisN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscSigChanNisN200_Type.__name__ = "Unsigned32"
_MscSigChanNisN200_Object = MibTableColumn
mscSigChanNisN200 = _MscSigChanNisN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 11, 1, 3),
    _MscSigChanNisN200_Type()
)
mscSigChanNisN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisN200.setStatus("mandatory")


class _MscSigChanNisT203_Type(Unsigned32):
    """Custom type mscSigChanNisT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_MscSigChanNisT203_Type.__name__ = "Unsigned32"
_MscSigChanNisT203_Object = MibTableColumn
mscSigChanNisT203 = _MscSigChanNisT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 11, 1, 4),
    _MscSigChanNisT203_Type()
)
mscSigChanNisT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisT203.setStatus("mandatory")


class _MscSigChanNisCircuitSwitchedK_Type(Unsigned32):
    """Custom type mscSigChanNisCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscSigChanNisCircuitSwitchedK_Type.__name__ = "Unsigned32"
_MscSigChanNisCircuitSwitchedK_Object = MibTableColumn
mscSigChanNisCircuitSwitchedK = _MscSigChanNisCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 11, 1, 6),
    _MscSigChanNisCircuitSwitchedK_Type()
)
mscSigChanNisCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisCircuitSwitchedK.setStatus("mandatory")
_MscSigChanNisL3Table_Object = MibTable
mscSigChanNisL3Table = _MscSigChanNisL3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 12)
)
if mibBuilder.loadTexts:
    mscSigChanNisL3Table.setStatus("mandatory")
_MscSigChanNisL3Entry_Object = MibTableRow
mscSigChanNisL3Entry = _MscSigChanNisL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 12, 1)
)
mscSigChanNisL3Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisL3Entry.setStatus("mandatory")


class _MscSigChanNisT309_Type(Unsigned32):
    """Custom type mscSigChanNisT309 based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 120),
    )


_MscSigChanNisT309_Type.__name__ = "Unsigned32"
_MscSigChanNisT309_Object = MibTableColumn
mscSigChanNisT309 = _MscSigChanNisT309_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 12, 1, 3),
    _MscSigChanNisT309_Type()
)
mscSigChanNisT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisT309.setStatus("mandatory")


class _MscSigChanNisT310_Type(Unsigned32):
    """Custom type mscSigChanNisT310 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_MscSigChanNisT310_Type.__name__ = "Unsigned32"
_MscSigChanNisT310_Object = MibTableColumn
mscSigChanNisT310 = _MscSigChanNisT310_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 12, 1, 4),
    _MscSigChanNisT310_Type()
)
mscSigChanNisT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisT310.setStatus("mandatory")
_MscSigChanNisProvTable_Object = MibTable
mscSigChanNisProvTable = _MscSigChanNisProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 13)
)
if mibBuilder.loadTexts:
    mscSigChanNisProvTable.setStatus("mandatory")
_MscSigChanNisProvEntry_Object = MibTableRow
mscSigChanNisProvEntry = _MscSigChanNisProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 13, 1)
)
mscSigChanNisProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisProvEntry.setStatus("mandatory")


class _MscSigChanNisSide_Type(Integer32):
    """Custom type mscSigChanNisSide based on Integer32"""
    defaultValue = 1

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


_MscSigChanNisSide_Type.__name__ = "Integer32"
_MscSigChanNisSide_Object = MibTableColumn
mscSigChanNisSide = _MscSigChanNisSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 13, 1, 1),
    _MscSigChanNisSide_Type()
)
mscSigChanNisSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisSide.setStatus("mandatory")


class _MscSigChanNisMaxNonCallConcurrent_Type(Unsigned32):
    """Custom type mscSigChanNisMaxNonCallConcurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MscSigChanNisMaxNonCallConcurrent_Type.__name__ = "Unsigned32"
_MscSigChanNisMaxNonCallConcurrent_Object = MibTableColumn
mscSigChanNisMaxNonCallConcurrent = _MscSigChanNisMaxNonCallConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 13, 1, 2),
    _MscSigChanNisMaxNonCallConcurrent_Type()
)
mscSigChanNisMaxNonCallConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisMaxNonCallConcurrent.setStatus("mandatory")
_MscSigChanNisStateTable_Object = MibTable
mscSigChanNisStateTable = _MscSigChanNisStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 14)
)
if mibBuilder.loadTexts:
    mscSigChanNisStateTable.setStatus("mandatory")
_MscSigChanNisStateEntry_Object = MibTableRow
mscSigChanNisStateEntry = _MscSigChanNisStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 14, 1)
)
mscSigChanNisStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisStateEntry.setStatus("mandatory")


class _MscSigChanNisAdminState_Type(Integer32):
    """Custom type mscSigChanNisAdminState based on Integer32"""
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


_MscSigChanNisAdminState_Type.__name__ = "Integer32"
_MscSigChanNisAdminState_Object = MibTableColumn
mscSigChanNisAdminState = _MscSigChanNisAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 14, 1, 1),
    _MscSigChanNisAdminState_Type()
)
mscSigChanNisAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisAdminState.setStatus("mandatory")


class _MscSigChanNisOperationalState_Type(Integer32):
    """Custom type mscSigChanNisOperationalState based on Integer32"""
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


_MscSigChanNisOperationalState_Type.__name__ = "Integer32"
_MscSigChanNisOperationalState_Object = MibTableColumn
mscSigChanNisOperationalState = _MscSigChanNisOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 14, 1, 2),
    _MscSigChanNisOperationalState_Type()
)
mscSigChanNisOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisOperationalState.setStatus("mandatory")


class _MscSigChanNisUsageState_Type(Integer32):
    """Custom type mscSigChanNisUsageState based on Integer32"""
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


_MscSigChanNisUsageState_Type.__name__ = "Integer32"
_MscSigChanNisUsageState_Object = MibTableColumn
mscSigChanNisUsageState = _MscSigChanNisUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 14, 1, 3),
    _MscSigChanNisUsageState_Type()
)
mscSigChanNisUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisUsageState.setStatus("mandatory")
_MscSigChanNisStatsTable_Object = MibTable
mscSigChanNisStatsTable = _MscSigChanNisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 15)
)
if mibBuilder.loadTexts:
    mscSigChanNisStatsTable.setStatus("mandatory")
_MscSigChanNisStatsEntry_Object = MibTableRow
mscSigChanNisStatsEntry = _MscSigChanNisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 15, 1)
)
mscSigChanNisStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisStatsEntry.setStatus("mandatory")


class _MscSigChanNisTotalCallsToIf_Type(Unsigned32):
    """Custom type mscSigChanNisTotalCallsToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisTotalCallsToIf_Type.__name__ = "Unsigned32"
_MscSigChanNisTotalCallsToIf_Object = MibTableColumn
mscSigChanNisTotalCallsToIf = _MscSigChanNisTotalCallsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 15, 1, 2),
    _MscSigChanNisTotalCallsToIf_Type()
)
mscSigChanNisTotalCallsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisTotalCallsToIf.setStatus("mandatory")


class _MscSigChanNisTotalCallsFromIf_Type(Unsigned32):
    """Custom type mscSigChanNisTotalCallsFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisTotalCallsFromIf_Type.__name__ = "Unsigned32"
_MscSigChanNisTotalCallsFromIf_Object = MibTableColumn
mscSigChanNisTotalCallsFromIf = _MscSigChanNisTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 15, 1, 3),
    _MscSigChanNisTotalCallsFromIf_Type()
)
mscSigChanNisTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisTotalCallsFromIf.setStatus("mandatory")


class _MscSigChanNisNonCallAssocSessionsToIf_Type(Unsigned32):
    """Custom type mscSigChanNisNonCallAssocSessionsToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisNonCallAssocSessionsToIf_Type.__name__ = "Unsigned32"
_MscSigChanNisNonCallAssocSessionsToIf_Object = MibTableColumn
mscSigChanNisNonCallAssocSessionsToIf = _MscSigChanNisNonCallAssocSessionsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 15, 1, 4),
    _MscSigChanNisNonCallAssocSessionsToIf_Type()
)
mscSigChanNisNonCallAssocSessionsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisNonCallAssocSessionsToIf.setStatus("mandatory")


class _MscSigChanNisNonCallAssocSessionsFromIf_Type(Unsigned32):
    """Custom type mscSigChanNisNonCallAssocSessionsFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanNisNonCallAssocSessionsFromIf_Type.__name__ = "Unsigned32"
_MscSigChanNisNonCallAssocSessionsFromIf_Object = MibTableColumn
mscSigChanNisNonCallAssocSessionsFromIf = _MscSigChanNisNonCallAssocSessionsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 15, 1, 5),
    _MscSigChanNisNonCallAssocSessionsFromIf_Type()
)
mscSigChanNisNonCallAssocSessionsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisNonCallAssocSessionsFromIf.setStatus("mandatory")
_MscSigChanNisOperTable_Object = MibTable
mscSigChanNisOperTable = _MscSigChanNisOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 16)
)
if mibBuilder.loadTexts:
    mscSigChanNisOperTable.setStatus("mandatory")
_MscSigChanNisOperEntry_Object = MibTableRow
mscSigChanNisOperEntry = _MscSigChanNisOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 16, 1)
)
mscSigChanNisOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisOperEntry.setStatus("mandatory")


class _MscSigChanNisActiveChannels_Type(Unsigned32):
    """Custom type mscSigChanNisActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanNisActiveChannels_Type.__name__ = "Unsigned32"
_MscSigChanNisActiveChannels_Object = MibTableColumn
mscSigChanNisActiveChannels = _MscSigChanNisActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 16, 1, 1),
    _MscSigChanNisActiveChannels_Type()
)
mscSigChanNisActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisActiveChannels.setStatus("mandatory")


class _MscSigChanNisActiveVoiceChannels_Type(Unsigned32):
    """Custom type mscSigChanNisActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanNisActiveVoiceChannels_Type.__name__ = "Unsigned32"
_MscSigChanNisActiveVoiceChannels_Object = MibTableColumn
mscSigChanNisActiveVoiceChannels = _MscSigChanNisActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 16, 1, 2),
    _MscSigChanNisActiveVoiceChannels_Type()
)
mscSigChanNisActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisActiveVoiceChannels.setStatus("mandatory")


class _MscSigChanNisActiveDataChannels_Type(Unsigned32):
    """Custom type mscSigChanNisActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanNisActiveDataChannels_Type.__name__ = "Unsigned32"
_MscSigChanNisActiveDataChannels_Object = MibTableColumn
mscSigChanNisActiveDataChannels = _MscSigChanNisActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 16, 1, 3),
    _MscSigChanNisActiveDataChannels_Type()
)
mscSigChanNisActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisActiveDataChannels.setStatus("mandatory")


class _MscSigChanNisPeakActiveChannels_Type(Unsigned32):
    """Custom type mscSigChanNisPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanNisPeakActiveChannels_Type.__name__ = "Unsigned32"
_MscSigChanNisPeakActiveChannels_Object = MibTableColumn
mscSigChanNisPeakActiveChannels = _MscSigChanNisPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 16, 1, 4),
    _MscSigChanNisPeakActiveChannels_Type()
)
mscSigChanNisPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisPeakActiveChannels.setStatus("mandatory")


class _MscSigChanNisPeakActiveVoiceChannels_Type(Unsigned32):
    """Custom type mscSigChanNisPeakActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanNisPeakActiveVoiceChannels_Type.__name__ = "Unsigned32"
_MscSigChanNisPeakActiveVoiceChannels_Object = MibTableColumn
mscSigChanNisPeakActiveVoiceChannels = _MscSigChanNisPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 16, 1, 5),
    _MscSigChanNisPeakActiveVoiceChannels_Type()
)
mscSigChanNisPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisPeakActiveVoiceChannels.setStatus("mandatory")


class _MscSigChanNisPeakActiveDataChannels_Type(Unsigned32):
    """Custom type mscSigChanNisPeakActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanNisPeakActiveDataChannels_Type.__name__ = "Unsigned32"
_MscSigChanNisPeakActiveDataChannels_Object = MibTableColumn
mscSigChanNisPeakActiveDataChannels = _MscSigChanNisPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 16, 1, 6),
    _MscSigChanNisPeakActiveDataChannels_Type()
)
mscSigChanNisPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisPeakActiveDataChannels.setStatus("mandatory")


class _MscSigChanNisDChanStatus_Type(Integer32):
    """Custom type mscSigChanNisDChanStatus based on Integer32"""
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


_MscSigChanNisDChanStatus_Type.__name__ = "Integer32"
_MscSigChanNisDChanStatus_Object = MibTableColumn
mscSigChanNisDChanStatus = _MscSigChanNisDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 16, 1, 7),
    _MscSigChanNisDChanStatus_Type()
)
mscSigChanNisDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanNisDChanStatus.setStatus("mandatory")
_MscSigChanNisToolsTable_Object = MibTable
mscSigChanNisToolsTable = _MscSigChanNisToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 17)
)
if mibBuilder.loadTexts:
    mscSigChanNisToolsTable.setStatus("mandatory")
_MscSigChanNisToolsEntry_Object = MibTableRow
mscSigChanNisToolsEntry = _MscSigChanNisToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 17, 1)
)
mscSigChanNisToolsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisToolsEntry.setStatus("mandatory")


class _MscSigChanNisTracing_Type(OctetString):
    """Custom type mscSigChanNisTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscSigChanNisTracing_Type.__name__ = "OctetString"
_MscSigChanNisTracing_Object = MibTableColumn
mscSigChanNisTracing = _MscSigChanNisTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 17, 1, 1),
    _MscSigChanNisTracing_Type()
)
mscSigChanNisTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisTracing.setStatus("mandatory")
_MscSigChanNisNisSpecificProvTable_Object = MibTable
mscSigChanNisNisSpecificProvTable = _MscSigChanNisNisSpecificProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 18)
)
if mibBuilder.loadTexts:
    mscSigChanNisNisSpecificProvTable.setStatus("mandatory")
_MscSigChanNisNisSpecificProvEntry_Object = MibTableRow
mscSigChanNisNisSpecificProvEntry = _MscSigChanNisNisSpecificProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 18, 1)
)
mscSigChanNisNisSpecificProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetNisSigMIB", "mscSigChanNisIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanNisNisSpecificProvEntry.setStatus("mandatory")


class _MscSigChanNisChanMaintenanceHandling_Type(Integer32):
    """Custom type mscSigChanNisChanMaintenanceHandling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalOnStartup", 0),
          ("restartMessage", 2),
          ("serviceMessage", 1))
    )


_MscSigChanNisChanMaintenanceHandling_Type.__name__ = "Integer32"
_MscSigChanNisChanMaintenanceHandling_Object = MibTableColumn
mscSigChanNisChanMaintenanceHandling = _MscSigChanNisChanMaintenanceHandling_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 8, 18, 1, 1),
    _MscSigChanNisChanMaintenanceHandling_Type()
)
mscSigChanNisChanMaintenanceHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanNisChanMaintenanceHandling.setStatus("mandatory")
_VnetNisSigMIB_ObjectIdentity = ObjectIdentity
vnetNisSigMIB = _VnetNisSigMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 112)
)
_VnetNisSigGroup_ObjectIdentity = ObjectIdentity
vnetNisSigGroup = _VnetNisSigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 112, 1)
)
_VnetNisSigGroupCA_ObjectIdentity = ObjectIdentity
vnetNisSigGroupCA = _VnetNisSigGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 112, 1, 1)
)
_VnetNisSigGroupCA02_ObjectIdentity = ObjectIdentity
vnetNisSigGroupCA02 = _VnetNisSigGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 112, 1, 1, 3)
)
_VnetNisSigGroupCA02A_ObjectIdentity = ObjectIdentity
vnetNisSigGroupCA02A = _VnetNisSigGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 112, 1, 1, 3, 2)
)
_VnetNisSigCapabilities_ObjectIdentity = ObjectIdentity
vnetNisSigCapabilities = _VnetNisSigCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 112, 3)
)
_VnetNisSigCapabilitiesCA_ObjectIdentity = ObjectIdentity
vnetNisSigCapabilitiesCA = _VnetNisSigCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 112, 3, 1)
)
_VnetNisSigCapabilitiesCA02_ObjectIdentity = ObjectIdentity
vnetNisSigCapabilitiesCA02 = _VnetNisSigCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 112, 3, 1, 3)
)
_VnetNisSigCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
vnetNisSigCapabilitiesCA02A = _VnetNisSigCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 112, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VnetNisSigMIB",
    **{"mscSigChanNis": mscSigChanNis,
       "mscSigChanNisRowStatusTable": mscSigChanNisRowStatusTable,
       "mscSigChanNisRowStatusEntry": mscSigChanNisRowStatusEntry,
       "mscSigChanNisRowStatus": mscSigChanNisRowStatus,
       "mscSigChanNisComponentName": mscSigChanNisComponentName,
       "mscSigChanNisStorageType": mscSigChanNisStorageType,
       "mscSigChanNisIndex": mscSigChanNisIndex,
       "mscSigChanNisFramer": mscSigChanNisFramer,
       "mscSigChanNisFramerRowStatusTable": mscSigChanNisFramerRowStatusTable,
       "mscSigChanNisFramerRowStatusEntry": mscSigChanNisFramerRowStatusEntry,
       "mscSigChanNisFramerRowStatus": mscSigChanNisFramerRowStatus,
       "mscSigChanNisFramerComponentName": mscSigChanNisFramerComponentName,
       "mscSigChanNisFramerStorageType": mscSigChanNisFramerStorageType,
       "mscSigChanNisFramerIndex": mscSigChanNisFramerIndex,
       "mscSigChanNisFramerProvTable": mscSigChanNisFramerProvTable,
       "mscSigChanNisFramerProvEntry": mscSigChanNisFramerProvEntry,
       "mscSigChanNisFramerInterfaceName": mscSigChanNisFramerInterfaceName,
       "mscSigChanNisFramerStateTable": mscSigChanNisFramerStateTable,
       "mscSigChanNisFramerStateEntry": mscSigChanNisFramerStateEntry,
       "mscSigChanNisFramerAdminState": mscSigChanNisFramerAdminState,
       "mscSigChanNisFramerOperationalState": mscSigChanNisFramerOperationalState,
       "mscSigChanNisFramerUsageState": mscSigChanNisFramerUsageState,
       "mscSigChanNisFramerStatsTable": mscSigChanNisFramerStatsTable,
       "mscSigChanNisFramerStatsEntry": mscSigChanNisFramerStatsEntry,
       "mscSigChanNisFramerFrmToIf": mscSigChanNisFramerFrmToIf,
       "mscSigChanNisFramerFrmFromIf": mscSigChanNisFramerFrmFromIf,
       "mscSigChanNisFramerOctetFromIf": mscSigChanNisFramerOctetFromIf,
       "mscSigChanNisFramerAborts": mscSigChanNisFramerAborts,
       "mscSigChanNisFramerCrcErrors": mscSigChanNisFramerCrcErrors,
       "mscSigChanNisFramerLrcErrors": mscSigChanNisFramerLrcErrors,
       "mscSigChanNisFramerNonOctetErrors": mscSigChanNisFramerNonOctetErrors,
       "mscSigChanNisFramerOverruns": mscSigChanNisFramerOverruns,
       "mscSigChanNisFramerUnderruns": mscSigChanNisFramerUnderruns,
       "mscSigChanNisFramerLargeFrmErrors": mscSigChanNisFramerLargeFrmErrors,
       "mscSigChanNisL2Table": mscSigChanNisL2Table,
       "mscSigChanNisL2Entry": mscSigChanNisL2Entry,
       "mscSigChanNisT23": mscSigChanNisT23,
       "mscSigChanNisT200": mscSigChanNisT200,
       "mscSigChanNisN200": mscSigChanNisN200,
       "mscSigChanNisT203": mscSigChanNisT203,
       "mscSigChanNisCircuitSwitchedK": mscSigChanNisCircuitSwitchedK,
       "mscSigChanNisL3Table": mscSigChanNisL3Table,
       "mscSigChanNisL3Entry": mscSigChanNisL3Entry,
       "mscSigChanNisT309": mscSigChanNisT309,
       "mscSigChanNisT310": mscSigChanNisT310,
       "mscSigChanNisProvTable": mscSigChanNisProvTable,
       "mscSigChanNisProvEntry": mscSigChanNisProvEntry,
       "mscSigChanNisSide": mscSigChanNisSide,
       "mscSigChanNisMaxNonCallConcurrent": mscSigChanNisMaxNonCallConcurrent,
       "mscSigChanNisStateTable": mscSigChanNisStateTable,
       "mscSigChanNisStateEntry": mscSigChanNisStateEntry,
       "mscSigChanNisAdminState": mscSigChanNisAdminState,
       "mscSigChanNisOperationalState": mscSigChanNisOperationalState,
       "mscSigChanNisUsageState": mscSigChanNisUsageState,
       "mscSigChanNisStatsTable": mscSigChanNisStatsTable,
       "mscSigChanNisStatsEntry": mscSigChanNisStatsEntry,
       "mscSigChanNisTotalCallsToIf": mscSigChanNisTotalCallsToIf,
       "mscSigChanNisTotalCallsFromIf": mscSigChanNisTotalCallsFromIf,
       "mscSigChanNisNonCallAssocSessionsToIf": mscSigChanNisNonCallAssocSessionsToIf,
       "mscSigChanNisNonCallAssocSessionsFromIf": mscSigChanNisNonCallAssocSessionsFromIf,
       "mscSigChanNisOperTable": mscSigChanNisOperTable,
       "mscSigChanNisOperEntry": mscSigChanNisOperEntry,
       "mscSigChanNisActiveChannels": mscSigChanNisActiveChannels,
       "mscSigChanNisActiveVoiceChannels": mscSigChanNisActiveVoiceChannels,
       "mscSigChanNisActiveDataChannels": mscSigChanNisActiveDataChannels,
       "mscSigChanNisPeakActiveChannels": mscSigChanNisPeakActiveChannels,
       "mscSigChanNisPeakActiveVoiceChannels": mscSigChanNisPeakActiveVoiceChannels,
       "mscSigChanNisPeakActiveDataChannels": mscSigChanNisPeakActiveDataChannels,
       "mscSigChanNisDChanStatus": mscSigChanNisDChanStatus,
       "mscSigChanNisToolsTable": mscSigChanNisToolsTable,
       "mscSigChanNisToolsEntry": mscSigChanNisToolsEntry,
       "mscSigChanNisTracing": mscSigChanNisTracing,
       "mscSigChanNisNisSpecificProvTable": mscSigChanNisNisSpecificProvTable,
       "mscSigChanNisNisSpecificProvEntry": mscSigChanNisNisSpecificProvEntry,
       "mscSigChanNisChanMaintenanceHandling": mscSigChanNisChanMaintenanceHandling,
       "vnetNisSigMIB": vnetNisSigMIB,
       "vnetNisSigGroup": vnetNisSigGroup,
       "vnetNisSigGroupCA": vnetNisSigGroupCA,
       "vnetNisSigGroupCA02": vnetNisSigGroupCA02,
       "vnetNisSigGroupCA02A": vnetNisSigGroupCA02A,
       "vnetNisSigCapabilities": vnetNisSigCapabilities,
       "vnetNisSigCapabilitiesCA": vnetNisSigCapabilitiesCA,
       "vnetNisSigCapabilitiesCA02": vnetNisSigCapabilitiesCA02,
       "vnetNisSigCapabilitiesCA02A": vnetNisSigCapabilitiesCA02A}
)
