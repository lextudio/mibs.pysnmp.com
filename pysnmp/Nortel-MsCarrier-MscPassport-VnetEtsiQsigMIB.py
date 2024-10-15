# SNMP MIB module (Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:16 2024
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

_MscSigChanEQsig_ObjectIdentity = ObjectIdentity
mscSigChanEQsig = _MscSigChanEQsig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2)
)
_MscSigChanEQsigRowStatusTable_Object = MibTable
mscSigChanEQsigRowStatusTable = _MscSigChanEQsigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 1)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigRowStatusTable.setStatus("mandatory")
_MscSigChanEQsigRowStatusEntry_Object = MibTableRow
mscSigChanEQsigRowStatusEntry = _MscSigChanEQsigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 1, 1)
)
mscSigChanEQsigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigRowStatusEntry.setStatus("mandatory")
_MscSigChanEQsigRowStatus_Type = RowStatus
_MscSigChanEQsigRowStatus_Object = MibTableColumn
mscSigChanEQsigRowStatus = _MscSigChanEQsigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 1, 1, 1),
    _MscSigChanEQsigRowStatus_Type()
)
mscSigChanEQsigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigRowStatus.setStatus("mandatory")
_MscSigChanEQsigComponentName_Type = DisplayString
_MscSigChanEQsigComponentName_Object = MibTableColumn
mscSigChanEQsigComponentName = _MscSigChanEQsigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 1, 1, 2),
    _MscSigChanEQsigComponentName_Type()
)
mscSigChanEQsigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigComponentName.setStatus("mandatory")
_MscSigChanEQsigStorageType_Type = StorageType
_MscSigChanEQsigStorageType_Object = MibTableColumn
mscSigChanEQsigStorageType = _MscSigChanEQsigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 1, 1, 4),
    _MscSigChanEQsigStorageType_Type()
)
mscSigChanEQsigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigStorageType.setStatus("mandatory")
_MscSigChanEQsigIndex_Type = NonReplicated
_MscSigChanEQsigIndex_Object = MibTableColumn
mscSigChanEQsigIndex = _MscSigChanEQsigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 1, 1, 10),
    _MscSigChanEQsigIndex_Type()
)
mscSigChanEQsigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanEQsigIndex.setStatus("mandatory")
_MscSigChanEQsigFramer_ObjectIdentity = ObjectIdentity
mscSigChanEQsigFramer = _MscSigChanEQsigFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2)
)
_MscSigChanEQsigFramerRowStatusTable_Object = MibTable
mscSigChanEQsigFramerRowStatusTable = _MscSigChanEQsigFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerRowStatusTable.setStatus("mandatory")
_MscSigChanEQsigFramerRowStatusEntry_Object = MibTableRow
mscSigChanEQsigFramerRowStatusEntry = _MscSigChanEQsigFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 1, 1)
)
mscSigChanEQsigFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerRowStatusEntry.setStatus("mandatory")
_MscSigChanEQsigFramerRowStatus_Type = RowStatus
_MscSigChanEQsigFramerRowStatus_Object = MibTableColumn
mscSigChanEQsigFramerRowStatus = _MscSigChanEQsigFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 1, 1, 1),
    _MscSigChanEQsigFramerRowStatus_Type()
)
mscSigChanEQsigFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerRowStatus.setStatus("mandatory")
_MscSigChanEQsigFramerComponentName_Type = DisplayString
_MscSigChanEQsigFramerComponentName_Object = MibTableColumn
mscSigChanEQsigFramerComponentName = _MscSigChanEQsigFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 1, 1, 2),
    _MscSigChanEQsigFramerComponentName_Type()
)
mscSigChanEQsigFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerComponentName.setStatus("mandatory")
_MscSigChanEQsigFramerStorageType_Type = StorageType
_MscSigChanEQsigFramerStorageType_Object = MibTableColumn
mscSigChanEQsigFramerStorageType = _MscSigChanEQsigFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 1, 1, 4),
    _MscSigChanEQsigFramerStorageType_Type()
)
mscSigChanEQsigFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerStorageType.setStatus("mandatory")
_MscSigChanEQsigFramerIndex_Type = NonReplicated
_MscSigChanEQsigFramerIndex_Object = MibTableColumn
mscSigChanEQsigFramerIndex = _MscSigChanEQsigFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 1, 1, 10),
    _MscSigChanEQsigFramerIndex_Type()
)
mscSigChanEQsigFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerIndex.setStatus("mandatory")
_MscSigChanEQsigFramerProvTable_Object = MibTable
mscSigChanEQsigFramerProvTable = _MscSigChanEQsigFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerProvTable.setStatus("mandatory")
_MscSigChanEQsigFramerProvEntry_Object = MibTableRow
mscSigChanEQsigFramerProvEntry = _MscSigChanEQsigFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 10, 1)
)
mscSigChanEQsigFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerProvEntry.setStatus("mandatory")
_MscSigChanEQsigFramerInterfaceName_Type = Link
_MscSigChanEQsigFramerInterfaceName_Object = MibTableColumn
mscSigChanEQsigFramerInterfaceName = _MscSigChanEQsigFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 10, 1, 1),
    _MscSigChanEQsigFramerInterfaceName_Type()
)
mscSigChanEQsigFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerInterfaceName.setStatus("mandatory")
_MscSigChanEQsigFramerStateTable_Object = MibTable
mscSigChanEQsigFramerStateTable = _MscSigChanEQsigFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerStateTable.setStatus("mandatory")
_MscSigChanEQsigFramerStateEntry_Object = MibTableRow
mscSigChanEQsigFramerStateEntry = _MscSigChanEQsigFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 12, 1)
)
mscSigChanEQsigFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerStateEntry.setStatus("mandatory")


class _MscSigChanEQsigFramerAdminState_Type(Integer32):
    """Custom type mscSigChanEQsigFramerAdminState based on Integer32"""
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


_MscSigChanEQsigFramerAdminState_Type.__name__ = "Integer32"
_MscSigChanEQsigFramerAdminState_Object = MibTableColumn
mscSigChanEQsigFramerAdminState = _MscSigChanEQsigFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 12, 1, 1),
    _MscSigChanEQsigFramerAdminState_Type()
)
mscSigChanEQsigFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerAdminState.setStatus("mandatory")


class _MscSigChanEQsigFramerOperationalState_Type(Integer32):
    """Custom type mscSigChanEQsigFramerOperationalState based on Integer32"""
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


_MscSigChanEQsigFramerOperationalState_Type.__name__ = "Integer32"
_MscSigChanEQsigFramerOperationalState_Object = MibTableColumn
mscSigChanEQsigFramerOperationalState = _MscSigChanEQsigFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 12, 1, 2),
    _MscSigChanEQsigFramerOperationalState_Type()
)
mscSigChanEQsigFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerOperationalState.setStatus("mandatory")


class _MscSigChanEQsigFramerUsageState_Type(Integer32):
    """Custom type mscSigChanEQsigFramerUsageState based on Integer32"""
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


_MscSigChanEQsigFramerUsageState_Type.__name__ = "Integer32"
_MscSigChanEQsigFramerUsageState_Object = MibTableColumn
mscSigChanEQsigFramerUsageState = _MscSigChanEQsigFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 12, 1, 3),
    _MscSigChanEQsigFramerUsageState_Type()
)
mscSigChanEQsigFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerUsageState.setStatus("mandatory")
_MscSigChanEQsigFramerStatsTable_Object = MibTable
mscSigChanEQsigFramerStatsTable = _MscSigChanEQsigFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerStatsTable.setStatus("mandatory")
_MscSigChanEQsigFramerStatsEntry_Object = MibTableRow
mscSigChanEQsigFramerStatsEntry = _MscSigChanEQsigFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1)
)
mscSigChanEQsigFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigFramerIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerStatsEntry.setStatus("mandatory")


class _MscSigChanEQsigFramerFrmToIf_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerFrmToIf_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerFrmToIf_Object = MibTableColumn
mscSigChanEQsigFramerFrmToIf = _MscSigChanEQsigFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 1),
    _MscSigChanEQsigFramerFrmToIf_Type()
)
mscSigChanEQsigFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerFrmToIf.setStatus("mandatory")


class _MscSigChanEQsigFramerFrmFromIf_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerFrmFromIf_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerFrmFromIf_Object = MibTableColumn
mscSigChanEQsigFramerFrmFromIf = _MscSigChanEQsigFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 2),
    _MscSigChanEQsigFramerFrmFromIf_Type()
)
mscSigChanEQsigFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerFrmFromIf.setStatus("mandatory")


class _MscSigChanEQsigFramerOctetFromIf_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerOctetFromIf_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerOctetFromIf_Object = MibTableColumn
mscSigChanEQsigFramerOctetFromIf = _MscSigChanEQsigFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 3),
    _MscSigChanEQsigFramerOctetFromIf_Type()
)
mscSigChanEQsigFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerOctetFromIf.setStatus("mandatory")


class _MscSigChanEQsigFramerAborts_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerAborts_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerAborts_Object = MibTableColumn
mscSigChanEQsigFramerAborts = _MscSigChanEQsigFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 4),
    _MscSigChanEQsigFramerAborts_Type()
)
mscSigChanEQsigFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerAborts.setStatus("mandatory")


class _MscSigChanEQsigFramerCrcErrors_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerCrcErrors_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerCrcErrors_Object = MibTableColumn
mscSigChanEQsigFramerCrcErrors = _MscSigChanEQsigFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 5),
    _MscSigChanEQsigFramerCrcErrors_Type()
)
mscSigChanEQsigFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerCrcErrors.setStatus("mandatory")


class _MscSigChanEQsigFramerLrcErrors_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerLrcErrors_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerLrcErrors_Object = MibTableColumn
mscSigChanEQsigFramerLrcErrors = _MscSigChanEQsigFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 6),
    _MscSigChanEQsigFramerLrcErrors_Type()
)
mscSigChanEQsigFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerLrcErrors.setStatus("mandatory")


class _MscSigChanEQsigFramerNonOctetErrors_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerNonOctetErrors_Object = MibTableColumn
mscSigChanEQsigFramerNonOctetErrors = _MscSigChanEQsigFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 7),
    _MscSigChanEQsigFramerNonOctetErrors_Type()
)
mscSigChanEQsigFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerNonOctetErrors.setStatus("mandatory")


class _MscSigChanEQsigFramerOverruns_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerOverruns_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerOverruns_Object = MibTableColumn
mscSigChanEQsigFramerOverruns = _MscSigChanEQsigFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 8),
    _MscSigChanEQsigFramerOverruns_Type()
)
mscSigChanEQsigFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerOverruns.setStatus("mandatory")


class _MscSigChanEQsigFramerUnderruns_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerUnderruns_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerUnderruns_Object = MibTableColumn
mscSigChanEQsigFramerUnderruns = _MscSigChanEQsigFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 9),
    _MscSigChanEQsigFramerUnderruns_Type()
)
mscSigChanEQsigFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerUnderruns.setStatus("mandatory")


class _MscSigChanEQsigFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type mscSigChanEQsigFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_MscSigChanEQsigFramerLargeFrmErrors_Object = MibTableColumn
mscSigChanEQsigFramerLargeFrmErrors = _MscSigChanEQsigFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 2, 13, 1, 10),
    _MscSigChanEQsigFramerLargeFrmErrors_Type()
)
mscSigChanEQsigFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigFramerLargeFrmErrors.setStatus("mandatory")
_MscSigChanEQsigL2Table_Object = MibTable
mscSigChanEQsigL2Table = _MscSigChanEQsigL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 11)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigL2Table.setStatus("mandatory")
_MscSigChanEQsigL2Entry_Object = MibTableRow
mscSigChanEQsigL2Entry = _MscSigChanEQsigL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 11, 1)
)
mscSigChanEQsigL2Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigL2Entry.setStatus("mandatory")


class _MscSigChanEQsigT23_Type(Unsigned32):
    """Custom type mscSigChanEQsigT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MscSigChanEQsigT23_Type.__name__ = "Unsigned32"
_MscSigChanEQsigT23_Object = MibTableColumn
mscSigChanEQsigT23 = _MscSigChanEQsigT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 11, 1, 1),
    _MscSigChanEQsigT23_Type()
)
mscSigChanEQsigT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigT23.setStatus("mandatory")


class _MscSigChanEQsigT200_Type(Unsigned32):
    """Custom type mscSigChanEQsigT200 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscSigChanEQsigT200_Type.__name__ = "Unsigned32"
_MscSigChanEQsigT200_Object = MibTableColumn
mscSigChanEQsigT200 = _MscSigChanEQsigT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 11, 1, 2),
    _MscSigChanEQsigT200_Type()
)
mscSigChanEQsigT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigT200.setStatus("mandatory")


class _MscSigChanEQsigN200_Type(Unsigned32):
    """Custom type mscSigChanEQsigN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscSigChanEQsigN200_Type.__name__ = "Unsigned32"
_MscSigChanEQsigN200_Object = MibTableColumn
mscSigChanEQsigN200 = _MscSigChanEQsigN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 11, 1, 3),
    _MscSigChanEQsigN200_Type()
)
mscSigChanEQsigN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigN200.setStatus("mandatory")


class _MscSigChanEQsigT203_Type(Unsigned32):
    """Custom type mscSigChanEQsigT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_MscSigChanEQsigT203_Type.__name__ = "Unsigned32"
_MscSigChanEQsigT203_Object = MibTableColumn
mscSigChanEQsigT203 = _MscSigChanEQsigT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 11, 1, 4),
    _MscSigChanEQsigT203_Type()
)
mscSigChanEQsigT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigT203.setStatus("mandatory")


class _MscSigChanEQsigCircuitSwitchedK_Type(Unsigned32):
    """Custom type mscSigChanEQsigCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscSigChanEQsigCircuitSwitchedK_Type.__name__ = "Unsigned32"
_MscSigChanEQsigCircuitSwitchedK_Object = MibTableColumn
mscSigChanEQsigCircuitSwitchedK = _MscSigChanEQsigCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 11, 1, 6),
    _MscSigChanEQsigCircuitSwitchedK_Type()
)
mscSigChanEQsigCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigCircuitSwitchedK.setStatus("mandatory")
_MscSigChanEQsigL3Table_Object = MibTable
mscSigChanEQsigL3Table = _MscSigChanEQsigL3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 12)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigL3Table.setStatus("mandatory")
_MscSigChanEQsigL3Entry_Object = MibTableRow
mscSigChanEQsigL3Entry = _MscSigChanEQsigL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 12, 1)
)
mscSigChanEQsigL3Entry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigL3Entry.setStatus("mandatory")


class _MscSigChanEQsigT309_Type(Unsigned32):
    """Custom type mscSigChanEQsigT309 based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 120),
    )


_MscSigChanEQsigT309_Type.__name__ = "Unsigned32"
_MscSigChanEQsigT309_Object = MibTableColumn
mscSigChanEQsigT309 = _MscSigChanEQsigT309_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 12, 1, 3),
    _MscSigChanEQsigT309_Type()
)
mscSigChanEQsigT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigT309.setStatus("mandatory")


class _MscSigChanEQsigT310_Type(Unsigned32):
    """Custom type mscSigChanEQsigT310 based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_MscSigChanEQsigT310_Type.__name__ = "Unsigned32"
_MscSigChanEQsigT310_Object = MibTableColumn
mscSigChanEQsigT310 = _MscSigChanEQsigT310_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 12, 1, 4),
    _MscSigChanEQsigT310_Type()
)
mscSigChanEQsigT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigT310.setStatus("mandatory")
_MscSigChanEQsigProvTable_Object = MibTable
mscSigChanEQsigProvTable = _MscSigChanEQsigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 13)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigProvTable.setStatus("mandatory")
_MscSigChanEQsigProvEntry_Object = MibTableRow
mscSigChanEQsigProvEntry = _MscSigChanEQsigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 13, 1)
)
mscSigChanEQsigProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigProvEntry.setStatus("mandatory")


class _MscSigChanEQsigSide_Type(Integer32):
    """Custom type mscSigChanEQsigSide based on Integer32"""
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


_MscSigChanEQsigSide_Type.__name__ = "Integer32"
_MscSigChanEQsigSide_Object = MibTableColumn
mscSigChanEQsigSide = _MscSigChanEQsigSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 13, 1, 1),
    _MscSigChanEQsigSide_Type()
)
mscSigChanEQsigSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigSide.setStatus("mandatory")


class _MscSigChanEQsigMaxNonCallConcurrent_Type(Unsigned32):
    """Custom type mscSigChanEQsigMaxNonCallConcurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MscSigChanEQsigMaxNonCallConcurrent_Type.__name__ = "Unsigned32"
_MscSigChanEQsigMaxNonCallConcurrent_Object = MibTableColumn
mscSigChanEQsigMaxNonCallConcurrent = _MscSigChanEQsigMaxNonCallConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 13, 1, 2),
    _MscSigChanEQsigMaxNonCallConcurrent_Type()
)
mscSigChanEQsigMaxNonCallConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigMaxNonCallConcurrent.setStatus("mandatory")


class _MscSigChanEQsigOverlapSendingEnabled_Type(Integer32):
    """Custom type mscSigChanEQsigOverlapSendingEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscSigChanEQsigOverlapSendingEnabled_Type.__name__ = "Integer32"
_MscSigChanEQsigOverlapSendingEnabled_Object = MibTableColumn
mscSigChanEQsigOverlapSendingEnabled = _MscSigChanEQsigOverlapSendingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 13, 1, 3),
    _MscSigChanEQsigOverlapSendingEnabled_Type()
)
mscSigChanEQsigOverlapSendingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigOverlapSendingEnabled.setStatus("mandatory")


class _MscSigChanEQsigOverlapReceivingEnabled_Type(Integer32):
    """Custom type mscSigChanEQsigOverlapReceivingEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscSigChanEQsigOverlapReceivingEnabled_Type.__name__ = "Integer32"
_MscSigChanEQsigOverlapReceivingEnabled_Object = MibTableColumn
mscSigChanEQsigOverlapReceivingEnabled = _MscSigChanEQsigOverlapReceivingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 13, 1, 4),
    _MscSigChanEQsigOverlapReceivingEnabled_Type()
)
mscSigChanEQsigOverlapReceivingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigOverlapReceivingEnabled.setStatus("mandatory")
_MscSigChanEQsigStateTable_Object = MibTable
mscSigChanEQsigStateTable = _MscSigChanEQsigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 14)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigStateTable.setStatus("mandatory")
_MscSigChanEQsigStateEntry_Object = MibTableRow
mscSigChanEQsigStateEntry = _MscSigChanEQsigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 14, 1)
)
mscSigChanEQsigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigStateEntry.setStatus("mandatory")


class _MscSigChanEQsigAdminState_Type(Integer32):
    """Custom type mscSigChanEQsigAdminState based on Integer32"""
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


_MscSigChanEQsigAdminState_Type.__name__ = "Integer32"
_MscSigChanEQsigAdminState_Object = MibTableColumn
mscSigChanEQsigAdminState = _MscSigChanEQsigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 14, 1, 1),
    _MscSigChanEQsigAdminState_Type()
)
mscSigChanEQsigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigAdminState.setStatus("mandatory")


class _MscSigChanEQsigOperationalState_Type(Integer32):
    """Custom type mscSigChanEQsigOperationalState based on Integer32"""
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


_MscSigChanEQsigOperationalState_Type.__name__ = "Integer32"
_MscSigChanEQsigOperationalState_Object = MibTableColumn
mscSigChanEQsigOperationalState = _MscSigChanEQsigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 14, 1, 2),
    _MscSigChanEQsigOperationalState_Type()
)
mscSigChanEQsigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigOperationalState.setStatus("mandatory")


class _MscSigChanEQsigUsageState_Type(Integer32):
    """Custom type mscSigChanEQsigUsageState based on Integer32"""
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


_MscSigChanEQsigUsageState_Type.__name__ = "Integer32"
_MscSigChanEQsigUsageState_Object = MibTableColumn
mscSigChanEQsigUsageState = _MscSigChanEQsigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 14, 1, 3),
    _MscSigChanEQsigUsageState_Type()
)
mscSigChanEQsigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigUsageState.setStatus("mandatory")
_MscSigChanEQsigStatsTable_Object = MibTable
mscSigChanEQsigStatsTable = _MscSigChanEQsigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 15)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigStatsTable.setStatus("mandatory")
_MscSigChanEQsigStatsEntry_Object = MibTableRow
mscSigChanEQsigStatsEntry = _MscSigChanEQsigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 15, 1)
)
mscSigChanEQsigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigStatsEntry.setStatus("mandatory")


class _MscSigChanEQsigTotalCallsToIf_Type(Unsigned32):
    """Custom type mscSigChanEQsigTotalCallsToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigTotalCallsToIf_Type.__name__ = "Unsigned32"
_MscSigChanEQsigTotalCallsToIf_Object = MibTableColumn
mscSigChanEQsigTotalCallsToIf = _MscSigChanEQsigTotalCallsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 15, 1, 2),
    _MscSigChanEQsigTotalCallsToIf_Type()
)
mscSigChanEQsigTotalCallsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigTotalCallsToIf.setStatus("mandatory")


class _MscSigChanEQsigTotalCallsFromIf_Type(Unsigned32):
    """Custom type mscSigChanEQsigTotalCallsFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigTotalCallsFromIf_Type.__name__ = "Unsigned32"
_MscSigChanEQsigTotalCallsFromIf_Object = MibTableColumn
mscSigChanEQsigTotalCallsFromIf = _MscSigChanEQsigTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 15, 1, 3),
    _MscSigChanEQsigTotalCallsFromIf_Type()
)
mscSigChanEQsigTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigTotalCallsFromIf.setStatus("mandatory")


class _MscSigChanEQsigNonCallAssocSessionsToIf_Type(Unsigned32):
    """Custom type mscSigChanEQsigNonCallAssocSessionsToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigNonCallAssocSessionsToIf_Type.__name__ = "Unsigned32"
_MscSigChanEQsigNonCallAssocSessionsToIf_Object = MibTableColumn
mscSigChanEQsigNonCallAssocSessionsToIf = _MscSigChanEQsigNonCallAssocSessionsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 15, 1, 4),
    _MscSigChanEQsigNonCallAssocSessionsToIf_Type()
)
mscSigChanEQsigNonCallAssocSessionsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigNonCallAssocSessionsToIf.setStatus("mandatory")


class _MscSigChanEQsigNonCallAssocSessionsFromIf_Type(Unsigned32):
    """Custom type mscSigChanEQsigNonCallAssocSessionsFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigNonCallAssocSessionsFromIf_Type.__name__ = "Unsigned32"
_MscSigChanEQsigNonCallAssocSessionsFromIf_Object = MibTableColumn
mscSigChanEQsigNonCallAssocSessionsFromIf = _MscSigChanEQsigNonCallAssocSessionsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 15, 1, 5),
    _MscSigChanEQsigNonCallAssocSessionsFromIf_Type()
)
mscSigChanEQsigNonCallAssocSessionsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigNonCallAssocSessionsFromIf.setStatus("mandatory")
_MscSigChanEQsigOperTable_Object = MibTable
mscSigChanEQsigOperTable = _MscSigChanEQsigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 16)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigOperTable.setStatus("mandatory")
_MscSigChanEQsigOperEntry_Object = MibTableRow
mscSigChanEQsigOperEntry = _MscSigChanEQsigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 16, 1)
)
mscSigChanEQsigOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigOperEntry.setStatus("mandatory")


class _MscSigChanEQsigActiveChannels_Type(Unsigned32):
    """Custom type mscSigChanEQsigActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEQsigActiveChannels_Type.__name__ = "Unsigned32"
_MscSigChanEQsigActiveChannels_Object = MibTableColumn
mscSigChanEQsigActiveChannels = _MscSigChanEQsigActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 16, 1, 1),
    _MscSigChanEQsigActiveChannels_Type()
)
mscSigChanEQsigActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigActiveChannels.setStatus("mandatory")


class _MscSigChanEQsigActiveVoiceChannels_Type(Unsigned32):
    """Custom type mscSigChanEQsigActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEQsigActiveVoiceChannels_Type.__name__ = "Unsigned32"
_MscSigChanEQsigActiveVoiceChannels_Object = MibTableColumn
mscSigChanEQsigActiveVoiceChannels = _MscSigChanEQsigActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 16, 1, 2),
    _MscSigChanEQsigActiveVoiceChannels_Type()
)
mscSigChanEQsigActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigActiveVoiceChannels.setStatus("mandatory")


class _MscSigChanEQsigActiveDataChannels_Type(Unsigned32):
    """Custom type mscSigChanEQsigActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEQsigActiveDataChannels_Type.__name__ = "Unsigned32"
_MscSigChanEQsigActiveDataChannels_Object = MibTableColumn
mscSigChanEQsigActiveDataChannels = _MscSigChanEQsigActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 16, 1, 3),
    _MscSigChanEQsigActiveDataChannels_Type()
)
mscSigChanEQsigActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigActiveDataChannels.setStatus("mandatory")


class _MscSigChanEQsigPeakActiveChannels_Type(Unsigned32):
    """Custom type mscSigChanEQsigPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEQsigPeakActiveChannels_Type.__name__ = "Unsigned32"
_MscSigChanEQsigPeakActiveChannels_Object = MibTableColumn
mscSigChanEQsigPeakActiveChannels = _MscSigChanEQsigPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 16, 1, 4),
    _MscSigChanEQsigPeakActiveChannels_Type()
)
mscSigChanEQsigPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigPeakActiveChannels.setStatus("mandatory")


class _MscSigChanEQsigPeakActiveVoiceChannels_Type(Unsigned32):
    """Custom type mscSigChanEQsigPeakActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEQsigPeakActiveVoiceChannels_Type.__name__ = "Unsigned32"
_MscSigChanEQsigPeakActiveVoiceChannels_Object = MibTableColumn
mscSigChanEQsigPeakActiveVoiceChannels = _MscSigChanEQsigPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 16, 1, 5),
    _MscSigChanEQsigPeakActiveVoiceChannels_Type()
)
mscSigChanEQsigPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigPeakActiveVoiceChannels.setStatus("mandatory")


class _MscSigChanEQsigPeakActiveDataChannels_Type(Unsigned32):
    """Custom type mscSigChanEQsigPeakActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscSigChanEQsigPeakActiveDataChannels_Type.__name__ = "Unsigned32"
_MscSigChanEQsigPeakActiveDataChannels_Object = MibTableColumn
mscSigChanEQsigPeakActiveDataChannels = _MscSigChanEQsigPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 16, 1, 6),
    _MscSigChanEQsigPeakActiveDataChannels_Type()
)
mscSigChanEQsigPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigPeakActiveDataChannels.setStatus("mandatory")


class _MscSigChanEQsigDChanStatus_Type(Integer32):
    """Custom type mscSigChanEQsigDChanStatus based on Integer32"""
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


_MscSigChanEQsigDChanStatus_Type.__name__ = "Integer32"
_MscSigChanEQsigDChanStatus_Object = MibTableColumn
mscSigChanEQsigDChanStatus = _MscSigChanEQsigDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 16, 1, 7),
    _MscSigChanEQsigDChanStatus_Type()
)
mscSigChanEQsigDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigDChanStatus.setStatus("mandatory")
_MscSigChanEQsigToolsTable_Object = MibTable
mscSigChanEQsigToolsTable = _MscSigChanEQsigToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 17)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigToolsTable.setStatus("mandatory")
_MscSigChanEQsigToolsEntry_Object = MibTableRow
mscSigChanEQsigToolsEntry = _MscSigChanEQsigToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 17, 1)
)
mscSigChanEQsigToolsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigToolsEntry.setStatus("mandatory")


class _MscSigChanEQsigTracing_Type(OctetString):
    """Custom type mscSigChanEQsigTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscSigChanEQsigTracing_Type.__name__ = "OctetString"
_MscSigChanEQsigTracing_Object = MibTableColumn
mscSigChanEQsigTracing = _MscSigChanEQsigTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 17, 1, 1),
    _MscSigChanEQsigTracing_Type()
)
mscSigChanEQsigTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigTracing.setStatus("mandatory")
_MscSigChanEQsigEQsigSpecificProvTable_Object = MibTable
mscSigChanEQsigEQsigSpecificProvTable = _MscSigChanEQsigEQsigSpecificProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 18)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigEQsigSpecificProvTable.setStatus("mandatory")
_MscSigChanEQsigEQsigSpecificProvEntry_Object = MibTableRow
mscSigChanEQsigEQsigSpecificProvEntry = _MscSigChanEQsigEQsigSpecificProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 18, 1)
)
mscSigChanEQsigEQsigSpecificProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigEQsigSpecificProvEntry.setStatus("mandatory")


class _MscSigChanEQsigMsgSegmentation_Type(Integer32):
    """Custom type mscSigChanEQsigMsgSegmentation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_MscSigChanEQsigMsgSegmentation_Type.__name__ = "Integer32"
_MscSigChanEQsigMsgSegmentation_Object = MibTableColumn
mscSigChanEQsigMsgSegmentation = _MscSigChanEQsigMsgSegmentation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 18, 1, 1),
    _MscSigChanEQsigMsgSegmentation_Type()
)
mscSigChanEQsigMsgSegmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigMsgSegmentation.setStatus("mandatory")


class _MscSigChanEQsigE1ChannelNumbers_Type(Integer32):
    """Custom type mscSigChanEQsigE1ChannelNumbers based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("contiguous", 2),
          ("skip16", 1))
    )


_MscSigChanEQsigE1ChannelNumbers_Type.__name__ = "Integer32"
_MscSigChanEQsigE1ChannelNumbers_Object = MibTableColumn
mscSigChanEQsigE1ChannelNumbers = _MscSigChanEQsigE1ChannelNumbers_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 18, 1, 2),
    _MscSigChanEQsigE1ChannelNumbers_Type()
)
mscSigChanEQsigE1ChannelNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscSigChanEQsigE1ChannelNumbers.setStatus("mandatory")
_MscSigChanEQsigEQsigSpecificOpTable_Object = MibTable
mscSigChanEQsigEQsigSpecificOpTable = _MscSigChanEQsigEQsigSpecificOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 19)
)
if mibBuilder.loadTexts:
    mscSigChanEQsigEQsigSpecificOpTable.setStatus("mandatory")
_MscSigChanEQsigEQsigSpecificOpEntry_Object = MibTableRow
mscSigChanEQsigEQsigSpecificOpEntry = _MscSigChanEQsigEQsigSpecificOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 19, 1)
)
mscSigChanEQsigEQsigSpecificOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VoiceNetworkingMIB", "mscSigChanIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB", "mscSigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    mscSigChanEQsigEQsigSpecificOpEntry.setStatus("mandatory")


class _MscSigChanEQsigSegmentationAccepted_Type(Unsigned32):
    """Custom type mscSigChanEQsigSegmentationAccepted based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigSegmentationAccepted_Type.__name__ = "Unsigned32"
_MscSigChanEQsigSegmentationAccepted_Object = MibTableColumn
mscSigChanEQsigSegmentationAccepted = _MscSigChanEQsigSegmentationAccepted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 19, 1, 1),
    _MscSigChanEQsigSegmentationAccepted_Type()
)
mscSigChanEQsigSegmentationAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigSegmentationAccepted.setStatus("mandatory")


class _MscSigChanEQsigSegmentationFailed_Type(Unsigned32):
    """Custom type mscSigChanEQsigSegmentationFailed based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscSigChanEQsigSegmentationFailed_Type.__name__ = "Unsigned32"
_MscSigChanEQsigSegmentationFailed_Object = MibTableColumn
mscSigChanEQsigSegmentationFailed = _MscSigChanEQsigSegmentationFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 115, 2, 19, 1, 2),
    _MscSigChanEQsigSegmentationFailed_Type()
)
mscSigChanEQsigSegmentationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscSigChanEQsigSegmentationFailed.setStatus("mandatory")
_VnetEtsiQsigMIB_ObjectIdentity = ObjectIdentity
vnetEtsiQsigMIB = _VnetEtsiQsigMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 110)
)
_VnetEtsiQsigGroup_ObjectIdentity = ObjectIdentity
vnetEtsiQsigGroup = _VnetEtsiQsigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 110, 1)
)
_VnetEtsiQsigGroupCA_ObjectIdentity = ObjectIdentity
vnetEtsiQsigGroupCA = _VnetEtsiQsigGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 110, 1, 1)
)
_VnetEtsiQsigGroupCA02_ObjectIdentity = ObjectIdentity
vnetEtsiQsigGroupCA02 = _VnetEtsiQsigGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 110, 1, 1, 3)
)
_VnetEtsiQsigGroupCA02A_ObjectIdentity = ObjectIdentity
vnetEtsiQsigGroupCA02A = _VnetEtsiQsigGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 110, 1, 1, 3, 2)
)
_VnetEtsiQsigCapabilities_ObjectIdentity = ObjectIdentity
vnetEtsiQsigCapabilities = _VnetEtsiQsigCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 110, 3)
)
_VnetEtsiQsigCapabilitiesCA_ObjectIdentity = ObjectIdentity
vnetEtsiQsigCapabilitiesCA = _VnetEtsiQsigCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 110, 3, 1)
)
_VnetEtsiQsigCapabilitiesCA02_ObjectIdentity = ObjectIdentity
vnetEtsiQsigCapabilitiesCA02 = _VnetEtsiQsigCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 110, 3, 1, 3)
)
_VnetEtsiQsigCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
vnetEtsiQsigCapabilitiesCA02A = _VnetEtsiQsigCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 110, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VnetEtsiQsigMIB",
    **{"mscSigChanEQsig": mscSigChanEQsig,
       "mscSigChanEQsigRowStatusTable": mscSigChanEQsigRowStatusTable,
       "mscSigChanEQsigRowStatusEntry": mscSigChanEQsigRowStatusEntry,
       "mscSigChanEQsigRowStatus": mscSigChanEQsigRowStatus,
       "mscSigChanEQsigComponentName": mscSigChanEQsigComponentName,
       "mscSigChanEQsigStorageType": mscSigChanEQsigStorageType,
       "mscSigChanEQsigIndex": mscSigChanEQsigIndex,
       "mscSigChanEQsigFramer": mscSigChanEQsigFramer,
       "mscSigChanEQsigFramerRowStatusTable": mscSigChanEQsigFramerRowStatusTable,
       "mscSigChanEQsigFramerRowStatusEntry": mscSigChanEQsigFramerRowStatusEntry,
       "mscSigChanEQsigFramerRowStatus": mscSigChanEQsigFramerRowStatus,
       "mscSigChanEQsigFramerComponentName": mscSigChanEQsigFramerComponentName,
       "mscSigChanEQsigFramerStorageType": mscSigChanEQsigFramerStorageType,
       "mscSigChanEQsigFramerIndex": mscSigChanEQsigFramerIndex,
       "mscSigChanEQsigFramerProvTable": mscSigChanEQsigFramerProvTable,
       "mscSigChanEQsigFramerProvEntry": mscSigChanEQsigFramerProvEntry,
       "mscSigChanEQsigFramerInterfaceName": mscSigChanEQsigFramerInterfaceName,
       "mscSigChanEQsigFramerStateTable": mscSigChanEQsigFramerStateTable,
       "mscSigChanEQsigFramerStateEntry": mscSigChanEQsigFramerStateEntry,
       "mscSigChanEQsigFramerAdminState": mscSigChanEQsigFramerAdminState,
       "mscSigChanEQsigFramerOperationalState": mscSigChanEQsigFramerOperationalState,
       "mscSigChanEQsigFramerUsageState": mscSigChanEQsigFramerUsageState,
       "mscSigChanEQsigFramerStatsTable": mscSigChanEQsigFramerStatsTable,
       "mscSigChanEQsigFramerStatsEntry": mscSigChanEQsigFramerStatsEntry,
       "mscSigChanEQsigFramerFrmToIf": mscSigChanEQsigFramerFrmToIf,
       "mscSigChanEQsigFramerFrmFromIf": mscSigChanEQsigFramerFrmFromIf,
       "mscSigChanEQsigFramerOctetFromIf": mscSigChanEQsigFramerOctetFromIf,
       "mscSigChanEQsigFramerAborts": mscSigChanEQsigFramerAborts,
       "mscSigChanEQsigFramerCrcErrors": mscSigChanEQsigFramerCrcErrors,
       "mscSigChanEQsigFramerLrcErrors": mscSigChanEQsigFramerLrcErrors,
       "mscSigChanEQsigFramerNonOctetErrors": mscSigChanEQsigFramerNonOctetErrors,
       "mscSigChanEQsigFramerOverruns": mscSigChanEQsigFramerOverruns,
       "mscSigChanEQsigFramerUnderruns": mscSigChanEQsigFramerUnderruns,
       "mscSigChanEQsigFramerLargeFrmErrors": mscSigChanEQsigFramerLargeFrmErrors,
       "mscSigChanEQsigL2Table": mscSigChanEQsigL2Table,
       "mscSigChanEQsigL2Entry": mscSigChanEQsigL2Entry,
       "mscSigChanEQsigT23": mscSigChanEQsigT23,
       "mscSigChanEQsigT200": mscSigChanEQsigT200,
       "mscSigChanEQsigN200": mscSigChanEQsigN200,
       "mscSigChanEQsigT203": mscSigChanEQsigT203,
       "mscSigChanEQsigCircuitSwitchedK": mscSigChanEQsigCircuitSwitchedK,
       "mscSigChanEQsigL3Table": mscSigChanEQsigL3Table,
       "mscSigChanEQsigL3Entry": mscSigChanEQsigL3Entry,
       "mscSigChanEQsigT309": mscSigChanEQsigT309,
       "mscSigChanEQsigT310": mscSigChanEQsigT310,
       "mscSigChanEQsigProvTable": mscSigChanEQsigProvTable,
       "mscSigChanEQsigProvEntry": mscSigChanEQsigProvEntry,
       "mscSigChanEQsigSide": mscSigChanEQsigSide,
       "mscSigChanEQsigMaxNonCallConcurrent": mscSigChanEQsigMaxNonCallConcurrent,
       "mscSigChanEQsigOverlapSendingEnabled": mscSigChanEQsigOverlapSendingEnabled,
       "mscSigChanEQsigOverlapReceivingEnabled": mscSigChanEQsigOverlapReceivingEnabled,
       "mscSigChanEQsigStateTable": mscSigChanEQsigStateTable,
       "mscSigChanEQsigStateEntry": mscSigChanEQsigStateEntry,
       "mscSigChanEQsigAdminState": mscSigChanEQsigAdminState,
       "mscSigChanEQsigOperationalState": mscSigChanEQsigOperationalState,
       "mscSigChanEQsigUsageState": mscSigChanEQsigUsageState,
       "mscSigChanEQsigStatsTable": mscSigChanEQsigStatsTable,
       "mscSigChanEQsigStatsEntry": mscSigChanEQsigStatsEntry,
       "mscSigChanEQsigTotalCallsToIf": mscSigChanEQsigTotalCallsToIf,
       "mscSigChanEQsigTotalCallsFromIf": mscSigChanEQsigTotalCallsFromIf,
       "mscSigChanEQsigNonCallAssocSessionsToIf": mscSigChanEQsigNonCallAssocSessionsToIf,
       "mscSigChanEQsigNonCallAssocSessionsFromIf": mscSigChanEQsigNonCallAssocSessionsFromIf,
       "mscSigChanEQsigOperTable": mscSigChanEQsigOperTable,
       "mscSigChanEQsigOperEntry": mscSigChanEQsigOperEntry,
       "mscSigChanEQsigActiveChannels": mscSigChanEQsigActiveChannels,
       "mscSigChanEQsigActiveVoiceChannels": mscSigChanEQsigActiveVoiceChannels,
       "mscSigChanEQsigActiveDataChannels": mscSigChanEQsigActiveDataChannels,
       "mscSigChanEQsigPeakActiveChannels": mscSigChanEQsigPeakActiveChannels,
       "mscSigChanEQsigPeakActiveVoiceChannels": mscSigChanEQsigPeakActiveVoiceChannels,
       "mscSigChanEQsigPeakActiveDataChannels": mscSigChanEQsigPeakActiveDataChannels,
       "mscSigChanEQsigDChanStatus": mscSigChanEQsigDChanStatus,
       "mscSigChanEQsigToolsTable": mscSigChanEQsigToolsTable,
       "mscSigChanEQsigToolsEntry": mscSigChanEQsigToolsEntry,
       "mscSigChanEQsigTracing": mscSigChanEQsigTracing,
       "mscSigChanEQsigEQsigSpecificProvTable": mscSigChanEQsigEQsigSpecificProvTable,
       "mscSigChanEQsigEQsigSpecificProvEntry": mscSigChanEQsigEQsigSpecificProvEntry,
       "mscSigChanEQsigMsgSegmentation": mscSigChanEQsigMsgSegmentation,
       "mscSigChanEQsigE1ChannelNumbers": mscSigChanEQsigE1ChannelNumbers,
       "mscSigChanEQsigEQsigSpecificOpTable": mscSigChanEQsigEQsigSpecificOpTable,
       "mscSigChanEQsigEQsigSpecificOpEntry": mscSigChanEQsigEQsigSpecificOpEntry,
       "mscSigChanEQsigSegmentationAccepted": mscSigChanEQsigSegmentationAccepted,
       "mscSigChanEQsigSegmentationFailed": mscSigChanEQsigSegmentationFailed,
       "vnetEtsiQsigMIB": vnetEtsiQsigMIB,
       "vnetEtsiQsigGroup": vnetEtsiQsigGroup,
       "vnetEtsiQsigGroupCA": vnetEtsiQsigGroupCA,
       "vnetEtsiQsigGroupCA02": vnetEtsiQsigGroupCA02,
       "vnetEtsiQsigGroupCA02A": vnetEtsiQsigGroupCA02A,
       "vnetEtsiQsigCapabilities": vnetEtsiQsigCapabilities,
       "vnetEtsiQsigCapabilitiesCA": vnetEtsiQsigCapabilitiesCA,
       "vnetEtsiQsigCapabilitiesCA02": vnetEtsiQsigCapabilitiesCA02,
       "vnetEtsiQsigCapabilitiesCA02A": vnetEtsiQsigCapabilitiesCA02A}
)
