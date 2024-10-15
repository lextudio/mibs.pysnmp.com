# SNMP MIB module (Nortel-Magellan-Passport-VnetNisSigMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VnetNisSigMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:38 2024
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

(sigChan,
 sigChanIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VoiceNetworkingMIB",
    "sigChan",
    "sigChanIndex")

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

_SigChanNis_ObjectIdentity = ObjectIdentity
sigChanNis = _SigChanNis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8)
)
_SigChanNisRowStatusTable_Object = MibTable
sigChanNisRowStatusTable = _SigChanNisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 1)
)
if mibBuilder.loadTexts:
    sigChanNisRowStatusTable.setStatus("mandatory")
_SigChanNisRowStatusEntry_Object = MibTableRow
sigChanNisRowStatusEntry = _SigChanNisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 1, 1)
)
sigChanNisRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisRowStatusEntry.setStatus("mandatory")
_SigChanNisRowStatus_Type = RowStatus
_SigChanNisRowStatus_Object = MibTableColumn
sigChanNisRowStatus = _SigChanNisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 1, 1, 1),
    _SigChanNisRowStatus_Type()
)
sigChanNisRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisRowStatus.setStatus("mandatory")
_SigChanNisComponentName_Type = DisplayString
_SigChanNisComponentName_Object = MibTableColumn
sigChanNisComponentName = _SigChanNisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 1, 1, 2),
    _SigChanNisComponentName_Type()
)
sigChanNisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisComponentName.setStatus("mandatory")
_SigChanNisStorageType_Type = StorageType
_SigChanNisStorageType_Object = MibTableColumn
sigChanNisStorageType = _SigChanNisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 1, 1, 4),
    _SigChanNisStorageType_Type()
)
sigChanNisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisStorageType.setStatus("mandatory")
_SigChanNisIndex_Type = NonReplicated
_SigChanNisIndex_Object = MibTableColumn
sigChanNisIndex = _SigChanNisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 1, 1, 10),
    _SigChanNisIndex_Type()
)
sigChanNisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanNisIndex.setStatus("mandatory")
_SigChanNisFramer_ObjectIdentity = ObjectIdentity
sigChanNisFramer = _SigChanNisFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2)
)
_SigChanNisFramerRowStatusTable_Object = MibTable
sigChanNisFramerRowStatusTable = _SigChanNisFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 1)
)
if mibBuilder.loadTexts:
    sigChanNisFramerRowStatusTable.setStatus("mandatory")
_SigChanNisFramerRowStatusEntry_Object = MibTableRow
sigChanNisFramerRowStatusEntry = _SigChanNisFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 1, 1)
)
sigChanNisFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisFramerRowStatusEntry.setStatus("mandatory")
_SigChanNisFramerRowStatus_Type = RowStatus
_SigChanNisFramerRowStatus_Object = MibTableColumn
sigChanNisFramerRowStatus = _SigChanNisFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 1, 1, 1),
    _SigChanNisFramerRowStatus_Type()
)
sigChanNisFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerRowStatus.setStatus("mandatory")
_SigChanNisFramerComponentName_Type = DisplayString
_SigChanNisFramerComponentName_Object = MibTableColumn
sigChanNisFramerComponentName = _SigChanNisFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 1, 1, 2),
    _SigChanNisFramerComponentName_Type()
)
sigChanNisFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerComponentName.setStatus("mandatory")
_SigChanNisFramerStorageType_Type = StorageType
_SigChanNisFramerStorageType_Object = MibTableColumn
sigChanNisFramerStorageType = _SigChanNisFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 1, 1, 4),
    _SigChanNisFramerStorageType_Type()
)
sigChanNisFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerStorageType.setStatus("mandatory")
_SigChanNisFramerIndex_Type = NonReplicated
_SigChanNisFramerIndex_Object = MibTableColumn
sigChanNisFramerIndex = _SigChanNisFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 1, 1, 10),
    _SigChanNisFramerIndex_Type()
)
sigChanNisFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanNisFramerIndex.setStatus("mandatory")
_SigChanNisFramerProvTable_Object = MibTable
sigChanNisFramerProvTable = _SigChanNisFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 10)
)
if mibBuilder.loadTexts:
    sigChanNisFramerProvTable.setStatus("mandatory")
_SigChanNisFramerProvEntry_Object = MibTableRow
sigChanNisFramerProvEntry = _SigChanNisFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 10, 1)
)
sigChanNisFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisFramerProvEntry.setStatus("mandatory")
_SigChanNisFramerInterfaceName_Type = Link
_SigChanNisFramerInterfaceName_Object = MibTableColumn
sigChanNisFramerInterfaceName = _SigChanNisFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 10, 1, 1),
    _SigChanNisFramerInterfaceName_Type()
)
sigChanNisFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisFramerInterfaceName.setStatus("mandatory")
_SigChanNisFramerStateTable_Object = MibTable
sigChanNisFramerStateTable = _SigChanNisFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 12)
)
if mibBuilder.loadTexts:
    sigChanNisFramerStateTable.setStatus("mandatory")
_SigChanNisFramerStateEntry_Object = MibTableRow
sigChanNisFramerStateEntry = _SigChanNisFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 12, 1)
)
sigChanNisFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisFramerStateEntry.setStatus("mandatory")


class _SigChanNisFramerAdminState_Type(Integer32):
    """Custom type sigChanNisFramerAdminState based on Integer32"""
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


_SigChanNisFramerAdminState_Type.__name__ = "Integer32"
_SigChanNisFramerAdminState_Object = MibTableColumn
sigChanNisFramerAdminState = _SigChanNisFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 12, 1, 1),
    _SigChanNisFramerAdminState_Type()
)
sigChanNisFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerAdminState.setStatus("mandatory")


class _SigChanNisFramerOperationalState_Type(Integer32):
    """Custom type sigChanNisFramerOperationalState based on Integer32"""
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


_SigChanNisFramerOperationalState_Type.__name__ = "Integer32"
_SigChanNisFramerOperationalState_Object = MibTableColumn
sigChanNisFramerOperationalState = _SigChanNisFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 12, 1, 2),
    _SigChanNisFramerOperationalState_Type()
)
sigChanNisFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerOperationalState.setStatus("mandatory")


class _SigChanNisFramerUsageState_Type(Integer32):
    """Custom type sigChanNisFramerUsageState based on Integer32"""
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


_SigChanNisFramerUsageState_Type.__name__ = "Integer32"
_SigChanNisFramerUsageState_Object = MibTableColumn
sigChanNisFramerUsageState = _SigChanNisFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 12, 1, 3),
    _SigChanNisFramerUsageState_Type()
)
sigChanNisFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerUsageState.setStatus("mandatory")
_SigChanNisFramerStatsTable_Object = MibTable
sigChanNisFramerStatsTable = _SigChanNisFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13)
)
if mibBuilder.loadTexts:
    sigChanNisFramerStatsTable.setStatus("mandatory")
_SigChanNisFramerStatsEntry_Object = MibTableRow
sigChanNisFramerStatsEntry = _SigChanNisFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1)
)
sigChanNisFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisFramerStatsEntry.setStatus("mandatory")


class _SigChanNisFramerFrmToIf_Type(Unsigned32):
    """Custom type sigChanNisFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerFrmToIf_Type.__name__ = "Unsigned32"
_SigChanNisFramerFrmToIf_Object = MibTableColumn
sigChanNisFramerFrmToIf = _SigChanNisFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 1),
    _SigChanNisFramerFrmToIf_Type()
)
sigChanNisFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerFrmToIf.setStatus("mandatory")


class _SigChanNisFramerFrmFromIf_Type(Unsigned32):
    """Custom type sigChanNisFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerFrmFromIf_Type.__name__ = "Unsigned32"
_SigChanNisFramerFrmFromIf_Object = MibTableColumn
sigChanNisFramerFrmFromIf = _SigChanNisFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 2),
    _SigChanNisFramerFrmFromIf_Type()
)
sigChanNisFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerFrmFromIf.setStatus("mandatory")


class _SigChanNisFramerOctetFromIf_Type(Unsigned32):
    """Custom type sigChanNisFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerOctetFromIf_Type.__name__ = "Unsigned32"
_SigChanNisFramerOctetFromIf_Object = MibTableColumn
sigChanNisFramerOctetFromIf = _SigChanNisFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 3),
    _SigChanNisFramerOctetFromIf_Type()
)
sigChanNisFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerOctetFromIf.setStatus("mandatory")


class _SigChanNisFramerAborts_Type(Unsigned32):
    """Custom type sigChanNisFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerAborts_Type.__name__ = "Unsigned32"
_SigChanNisFramerAborts_Object = MibTableColumn
sigChanNisFramerAborts = _SigChanNisFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 4),
    _SigChanNisFramerAborts_Type()
)
sigChanNisFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerAborts.setStatus("mandatory")


class _SigChanNisFramerCrcErrors_Type(Unsigned32):
    """Custom type sigChanNisFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerCrcErrors_Type.__name__ = "Unsigned32"
_SigChanNisFramerCrcErrors_Object = MibTableColumn
sigChanNisFramerCrcErrors = _SigChanNisFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 5),
    _SigChanNisFramerCrcErrors_Type()
)
sigChanNisFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerCrcErrors.setStatus("mandatory")


class _SigChanNisFramerLrcErrors_Type(Unsigned32):
    """Custom type sigChanNisFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerLrcErrors_Type.__name__ = "Unsigned32"
_SigChanNisFramerLrcErrors_Object = MibTableColumn
sigChanNisFramerLrcErrors = _SigChanNisFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 6),
    _SigChanNisFramerLrcErrors_Type()
)
sigChanNisFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerLrcErrors.setStatus("mandatory")


class _SigChanNisFramerNonOctetErrors_Type(Unsigned32):
    """Custom type sigChanNisFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_SigChanNisFramerNonOctetErrors_Object = MibTableColumn
sigChanNisFramerNonOctetErrors = _SigChanNisFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 7),
    _SigChanNisFramerNonOctetErrors_Type()
)
sigChanNisFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerNonOctetErrors.setStatus("mandatory")


class _SigChanNisFramerOverruns_Type(Unsigned32):
    """Custom type sigChanNisFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerOverruns_Type.__name__ = "Unsigned32"
_SigChanNisFramerOverruns_Object = MibTableColumn
sigChanNisFramerOverruns = _SigChanNisFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 8),
    _SigChanNisFramerOverruns_Type()
)
sigChanNisFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerOverruns.setStatus("mandatory")


class _SigChanNisFramerUnderruns_Type(Unsigned32):
    """Custom type sigChanNisFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerUnderruns_Type.__name__ = "Unsigned32"
_SigChanNisFramerUnderruns_Object = MibTableColumn
sigChanNisFramerUnderruns = _SigChanNisFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 9),
    _SigChanNisFramerUnderruns_Type()
)
sigChanNisFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerUnderruns.setStatus("mandatory")


class _SigChanNisFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type sigChanNisFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_SigChanNisFramerLargeFrmErrors_Object = MibTableColumn
sigChanNisFramerLargeFrmErrors = _SigChanNisFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 2, 13, 1, 10),
    _SigChanNisFramerLargeFrmErrors_Type()
)
sigChanNisFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisFramerLargeFrmErrors.setStatus("mandatory")
_SigChanNisL2Table_Object = MibTable
sigChanNisL2Table = _SigChanNisL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 11)
)
if mibBuilder.loadTexts:
    sigChanNisL2Table.setStatus("mandatory")
_SigChanNisL2Entry_Object = MibTableRow
sigChanNisL2Entry = _SigChanNisL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 11, 1)
)
sigChanNisL2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisL2Entry.setStatus("mandatory")


class _SigChanNisT23_Type(Unsigned32):
    """Custom type sigChanNisT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SigChanNisT23_Type.__name__ = "Unsigned32"
_SigChanNisT23_Object = MibTableColumn
sigChanNisT23 = _SigChanNisT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 11, 1, 1),
    _SigChanNisT23_Type()
)
sigChanNisT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisT23.setStatus("mandatory")


class _SigChanNisT200_Type(Unsigned32):
    """Custom type sigChanNisT200 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SigChanNisT200_Type.__name__ = "Unsigned32"
_SigChanNisT200_Object = MibTableColumn
sigChanNisT200 = _SigChanNisT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 11, 1, 2),
    _SigChanNisT200_Type()
)
sigChanNisT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisT200.setStatus("mandatory")


class _SigChanNisN200_Type(Unsigned32):
    """Custom type sigChanNisN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SigChanNisN200_Type.__name__ = "Unsigned32"
_SigChanNisN200_Object = MibTableColumn
sigChanNisN200 = _SigChanNisN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 11, 1, 3),
    _SigChanNisN200_Type()
)
sigChanNisN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisN200.setStatus("mandatory")


class _SigChanNisT203_Type(Unsigned32):
    """Custom type sigChanNisT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_SigChanNisT203_Type.__name__ = "Unsigned32"
_SigChanNisT203_Object = MibTableColumn
sigChanNisT203 = _SigChanNisT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 11, 1, 4),
    _SigChanNisT203_Type()
)
sigChanNisT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisT203.setStatus("mandatory")


class _SigChanNisCircuitSwitchedK_Type(Unsigned32):
    """Custom type sigChanNisCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SigChanNisCircuitSwitchedK_Type.__name__ = "Unsigned32"
_SigChanNisCircuitSwitchedK_Object = MibTableColumn
sigChanNisCircuitSwitchedK = _SigChanNisCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 11, 1, 6),
    _SigChanNisCircuitSwitchedK_Type()
)
sigChanNisCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisCircuitSwitchedK.setStatus("mandatory")
_SigChanNisL3Table_Object = MibTable
sigChanNisL3Table = _SigChanNisL3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 12)
)
if mibBuilder.loadTexts:
    sigChanNisL3Table.setStatus("mandatory")
_SigChanNisL3Entry_Object = MibTableRow
sigChanNisL3Entry = _SigChanNisL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 12, 1)
)
sigChanNisL3Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisL3Entry.setStatus("mandatory")


class _SigChanNisT309_Type(Unsigned32):
    """Custom type sigChanNisT309 based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 120),
    )


_SigChanNisT309_Type.__name__ = "Unsigned32"
_SigChanNisT309_Object = MibTableColumn
sigChanNisT309 = _SigChanNisT309_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 12, 1, 3),
    _SigChanNisT309_Type()
)
sigChanNisT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisT309.setStatus("mandatory")


class _SigChanNisT310_Type(Unsigned32):
    """Custom type sigChanNisT310 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_SigChanNisT310_Type.__name__ = "Unsigned32"
_SigChanNisT310_Object = MibTableColumn
sigChanNisT310 = _SigChanNisT310_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 12, 1, 4),
    _SigChanNisT310_Type()
)
sigChanNisT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisT310.setStatus("mandatory")
_SigChanNisProvTable_Object = MibTable
sigChanNisProvTable = _SigChanNisProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 13)
)
if mibBuilder.loadTexts:
    sigChanNisProvTable.setStatus("mandatory")
_SigChanNisProvEntry_Object = MibTableRow
sigChanNisProvEntry = _SigChanNisProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 13, 1)
)
sigChanNisProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisProvEntry.setStatus("mandatory")


class _SigChanNisSide_Type(Integer32):
    """Custom type sigChanNisSide based on Integer32"""
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


_SigChanNisSide_Type.__name__ = "Integer32"
_SigChanNisSide_Object = MibTableColumn
sigChanNisSide = _SigChanNisSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 13, 1, 1),
    _SigChanNisSide_Type()
)
sigChanNisSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisSide.setStatus("mandatory")


class _SigChanNisMaxNonCallConcurrent_Type(Unsigned32):
    """Custom type sigChanNisMaxNonCallConcurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SigChanNisMaxNonCallConcurrent_Type.__name__ = "Unsigned32"
_SigChanNisMaxNonCallConcurrent_Object = MibTableColumn
sigChanNisMaxNonCallConcurrent = _SigChanNisMaxNonCallConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 13, 1, 2),
    _SigChanNisMaxNonCallConcurrent_Type()
)
sigChanNisMaxNonCallConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisMaxNonCallConcurrent.setStatus("mandatory")
_SigChanNisStateTable_Object = MibTable
sigChanNisStateTable = _SigChanNisStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 14)
)
if mibBuilder.loadTexts:
    sigChanNisStateTable.setStatus("mandatory")
_SigChanNisStateEntry_Object = MibTableRow
sigChanNisStateEntry = _SigChanNisStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 14, 1)
)
sigChanNisStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisStateEntry.setStatus("mandatory")


class _SigChanNisAdminState_Type(Integer32):
    """Custom type sigChanNisAdminState based on Integer32"""
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


_SigChanNisAdminState_Type.__name__ = "Integer32"
_SigChanNisAdminState_Object = MibTableColumn
sigChanNisAdminState = _SigChanNisAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 14, 1, 1),
    _SigChanNisAdminState_Type()
)
sigChanNisAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisAdminState.setStatus("mandatory")


class _SigChanNisOperationalState_Type(Integer32):
    """Custom type sigChanNisOperationalState based on Integer32"""
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


_SigChanNisOperationalState_Type.__name__ = "Integer32"
_SigChanNisOperationalState_Object = MibTableColumn
sigChanNisOperationalState = _SigChanNisOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 14, 1, 2),
    _SigChanNisOperationalState_Type()
)
sigChanNisOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisOperationalState.setStatus("mandatory")


class _SigChanNisUsageState_Type(Integer32):
    """Custom type sigChanNisUsageState based on Integer32"""
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


_SigChanNisUsageState_Type.__name__ = "Integer32"
_SigChanNisUsageState_Object = MibTableColumn
sigChanNisUsageState = _SigChanNisUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 14, 1, 3),
    _SigChanNisUsageState_Type()
)
sigChanNisUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisUsageState.setStatus("mandatory")
_SigChanNisStatsTable_Object = MibTable
sigChanNisStatsTable = _SigChanNisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 15)
)
if mibBuilder.loadTexts:
    sigChanNisStatsTable.setStatus("mandatory")
_SigChanNisStatsEntry_Object = MibTableRow
sigChanNisStatsEntry = _SigChanNisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 15, 1)
)
sigChanNisStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisStatsEntry.setStatus("mandatory")


class _SigChanNisTotalCallsToIf_Type(Unsigned32):
    """Custom type sigChanNisTotalCallsToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisTotalCallsToIf_Type.__name__ = "Unsigned32"
_SigChanNisTotalCallsToIf_Object = MibTableColumn
sigChanNisTotalCallsToIf = _SigChanNisTotalCallsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 15, 1, 2),
    _SigChanNisTotalCallsToIf_Type()
)
sigChanNisTotalCallsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisTotalCallsToIf.setStatus("mandatory")


class _SigChanNisTotalCallsFromIf_Type(Unsigned32):
    """Custom type sigChanNisTotalCallsFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisTotalCallsFromIf_Type.__name__ = "Unsigned32"
_SigChanNisTotalCallsFromIf_Object = MibTableColumn
sigChanNisTotalCallsFromIf = _SigChanNisTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 15, 1, 3),
    _SigChanNisTotalCallsFromIf_Type()
)
sigChanNisTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisTotalCallsFromIf.setStatus("mandatory")


class _SigChanNisNonCallAssocSessionsToIf_Type(Unsigned32):
    """Custom type sigChanNisNonCallAssocSessionsToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisNonCallAssocSessionsToIf_Type.__name__ = "Unsigned32"
_SigChanNisNonCallAssocSessionsToIf_Object = MibTableColumn
sigChanNisNonCallAssocSessionsToIf = _SigChanNisNonCallAssocSessionsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 15, 1, 4),
    _SigChanNisNonCallAssocSessionsToIf_Type()
)
sigChanNisNonCallAssocSessionsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisNonCallAssocSessionsToIf.setStatus("mandatory")


class _SigChanNisNonCallAssocSessionsFromIf_Type(Unsigned32):
    """Custom type sigChanNisNonCallAssocSessionsFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanNisNonCallAssocSessionsFromIf_Type.__name__ = "Unsigned32"
_SigChanNisNonCallAssocSessionsFromIf_Object = MibTableColumn
sigChanNisNonCallAssocSessionsFromIf = _SigChanNisNonCallAssocSessionsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 15, 1, 5),
    _SigChanNisNonCallAssocSessionsFromIf_Type()
)
sigChanNisNonCallAssocSessionsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisNonCallAssocSessionsFromIf.setStatus("mandatory")
_SigChanNisOperTable_Object = MibTable
sigChanNisOperTable = _SigChanNisOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 16)
)
if mibBuilder.loadTexts:
    sigChanNisOperTable.setStatus("mandatory")
_SigChanNisOperEntry_Object = MibTableRow
sigChanNisOperEntry = _SigChanNisOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 16, 1)
)
sigChanNisOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisOperEntry.setStatus("mandatory")


class _SigChanNisActiveChannels_Type(Unsigned32):
    """Custom type sigChanNisActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanNisActiveChannels_Type.__name__ = "Unsigned32"
_SigChanNisActiveChannels_Object = MibTableColumn
sigChanNisActiveChannels = _SigChanNisActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 16, 1, 1),
    _SigChanNisActiveChannels_Type()
)
sigChanNisActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisActiveChannels.setStatus("mandatory")


class _SigChanNisActiveVoiceChannels_Type(Unsigned32):
    """Custom type sigChanNisActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanNisActiveVoiceChannels_Type.__name__ = "Unsigned32"
_SigChanNisActiveVoiceChannels_Object = MibTableColumn
sigChanNisActiveVoiceChannels = _SigChanNisActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 16, 1, 2),
    _SigChanNisActiveVoiceChannels_Type()
)
sigChanNisActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisActiveVoiceChannels.setStatus("mandatory")


class _SigChanNisActiveDataChannels_Type(Unsigned32):
    """Custom type sigChanNisActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanNisActiveDataChannels_Type.__name__ = "Unsigned32"
_SigChanNisActiveDataChannels_Object = MibTableColumn
sigChanNisActiveDataChannels = _SigChanNisActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 16, 1, 3),
    _SigChanNisActiveDataChannels_Type()
)
sigChanNisActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisActiveDataChannels.setStatus("mandatory")


class _SigChanNisPeakActiveChannels_Type(Unsigned32):
    """Custom type sigChanNisPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanNisPeakActiveChannels_Type.__name__ = "Unsigned32"
_SigChanNisPeakActiveChannels_Object = MibTableColumn
sigChanNisPeakActiveChannels = _SigChanNisPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 16, 1, 4),
    _SigChanNisPeakActiveChannels_Type()
)
sigChanNisPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisPeakActiveChannels.setStatus("mandatory")


class _SigChanNisPeakActiveVoiceChannels_Type(Unsigned32):
    """Custom type sigChanNisPeakActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanNisPeakActiveVoiceChannels_Type.__name__ = "Unsigned32"
_SigChanNisPeakActiveVoiceChannels_Object = MibTableColumn
sigChanNisPeakActiveVoiceChannels = _SigChanNisPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 16, 1, 5),
    _SigChanNisPeakActiveVoiceChannels_Type()
)
sigChanNisPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisPeakActiveVoiceChannels.setStatus("mandatory")


class _SigChanNisPeakActiveDataChannels_Type(Unsigned32):
    """Custom type sigChanNisPeakActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanNisPeakActiveDataChannels_Type.__name__ = "Unsigned32"
_SigChanNisPeakActiveDataChannels_Object = MibTableColumn
sigChanNisPeakActiveDataChannels = _SigChanNisPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 16, 1, 6),
    _SigChanNisPeakActiveDataChannels_Type()
)
sigChanNisPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisPeakActiveDataChannels.setStatus("mandatory")


class _SigChanNisDChanStatus_Type(Integer32):
    """Custom type sigChanNisDChanStatus based on Integer32"""
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


_SigChanNisDChanStatus_Type.__name__ = "Integer32"
_SigChanNisDChanStatus_Object = MibTableColumn
sigChanNisDChanStatus = _SigChanNisDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 16, 1, 7),
    _SigChanNisDChanStatus_Type()
)
sigChanNisDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanNisDChanStatus.setStatus("mandatory")
_SigChanNisToolsTable_Object = MibTable
sigChanNisToolsTable = _SigChanNisToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 17)
)
if mibBuilder.loadTexts:
    sigChanNisToolsTable.setStatus("mandatory")
_SigChanNisToolsEntry_Object = MibTableRow
sigChanNisToolsEntry = _SigChanNisToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 17, 1)
)
sigChanNisToolsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisToolsEntry.setStatus("mandatory")


class _SigChanNisTracing_Type(OctetString):
    """Custom type sigChanNisTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SigChanNisTracing_Type.__name__ = "OctetString"
_SigChanNisTracing_Object = MibTableColumn
sigChanNisTracing = _SigChanNisTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 17, 1, 1),
    _SigChanNisTracing_Type()
)
sigChanNisTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisTracing.setStatus("mandatory")
_SigChanNisNisSpecificProvTable_Object = MibTable
sigChanNisNisSpecificProvTable = _SigChanNisNisSpecificProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 18)
)
if mibBuilder.loadTexts:
    sigChanNisNisSpecificProvTable.setStatus("mandatory")
_SigChanNisNisSpecificProvEntry_Object = MibTableRow
sigChanNisNisSpecificProvEntry = _SigChanNisNisSpecificProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 18, 1)
)
sigChanNisNisSpecificProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetNisSigMIB", "sigChanNisIndex"),
)
if mibBuilder.loadTexts:
    sigChanNisNisSpecificProvEntry.setStatus("mandatory")


class _SigChanNisChanMaintenanceHandling_Type(Integer32):
    """Custom type sigChanNisChanMaintenanceHandling based on Integer32"""
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


_SigChanNisChanMaintenanceHandling_Type.__name__ = "Integer32"
_SigChanNisChanMaintenanceHandling_Object = MibTableColumn
sigChanNisChanMaintenanceHandling = _SigChanNisChanMaintenanceHandling_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 8, 18, 1, 1),
    _SigChanNisChanMaintenanceHandling_Type()
)
sigChanNisChanMaintenanceHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanNisChanMaintenanceHandling.setStatus("mandatory")
_VnetNisSigMIB_ObjectIdentity = ObjectIdentity
vnetNisSigMIB = _VnetNisSigMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 112)
)
_VnetNisSigGroup_ObjectIdentity = ObjectIdentity
vnetNisSigGroup = _VnetNisSigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 112, 1)
)
_VnetNisSigGroupBE_ObjectIdentity = ObjectIdentity
vnetNisSigGroupBE = _VnetNisSigGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 112, 1, 5)
)
_VnetNisSigGroupBE01_ObjectIdentity = ObjectIdentity
vnetNisSigGroupBE01 = _VnetNisSigGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 112, 1, 5, 2)
)
_VnetNisSigGroupBE01A_ObjectIdentity = ObjectIdentity
vnetNisSigGroupBE01A = _VnetNisSigGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 112, 1, 5, 2, 2)
)
_VnetNisSigCapabilities_ObjectIdentity = ObjectIdentity
vnetNisSigCapabilities = _VnetNisSigCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 112, 3)
)
_VnetNisSigCapabilitiesBE_ObjectIdentity = ObjectIdentity
vnetNisSigCapabilitiesBE = _VnetNisSigCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 112, 3, 5)
)
_VnetNisSigCapabilitiesBE01_ObjectIdentity = ObjectIdentity
vnetNisSigCapabilitiesBE01 = _VnetNisSigCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 112, 3, 5, 2)
)
_VnetNisSigCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
vnetNisSigCapabilitiesBE01A = _VnetNisSigCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 112, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VnetNisSigMIB",
    **{"sigChanNis": sigChanNis,
       "sigChanNisRowStatusTable": sigChanNisRowStatusTable,
       "sigChanNisRowStatusEntry": sigChanNisRowStatusEntry,
       "sigChanNisRowStatus": sigChanNisRowStatus,
       "sigChanNisComponentName": sigChanNisComponentName,
       "sigChanNisStorageType": sigChanNisStorageType,
       "sigChanNisIndex": sigChanNisIndex,
       "sigChanNisFramer": sigChanNisFramer,
       "sigChanNisFramerRowStatusTable": sigChanNisFramerRowStatusTable,
       "sigChanNisFramerRowStatusEntry": sigChanNisFramerRowStatusEntry,
       "sigChanNisFramerRowStatus": sigChanNisFramerRowStatus,
       "sigChanNisFramerComponentName": sigChanNisFramerComponentName,
       "sigChanNisFramerStorageType": sigChanNisFramerStorageType,
       "sigChanNisFramerIndex": sigChanNisFramerIndex,
       "sigChanNisFramerProvTable": sigChanNisFramerProvTable,
       "sigChanNisFramerProvEntry": sigChanNisFramerProvEntry,
       "sigChanNisFramerInterfaceName": sigChanNisFramerInterfaceName,
       "sigChanNisFramerStateTable": sigChanNisFramerStateTable,
       "sigChanNisFramerStateEntry": sigChanNisFramerStateEntry,
       "sigChanNisFramerAdminState": sigChanNisFramerAdminState,
       "sigChanNisFramerOperationalState": sigChanNisFramerOperationalState,
       "sigChanNisFramerUsageState": sigChanNisFramerUsageState,
       "sigChanNisFramerStatsTable": sigChanNisFramerStatsTable,
       "sigChanNisFramerStatsEntry": sigChanNisFramerStatsEntry,
       "sigChanNisFramerFrmToIf": sigChanNisFramerFrmToIf,
       "sigChanNisFramerFrmFromIf": sigChanNisFramerFrmFromIf,
       "sigChanNisFramerOctetFromIf": sigChanNisFramerOctetFromIf,
       "sigChanNisFramerAborts": sigChanNisFramerAborts,
       "sigChanNisFramerCrcErrors": sigChanNisFramerCrcErrors,
       "sigChanNisFramerLrcErrors": sigChanNisFramerLrcErrors,
       "sigChanNisFramerNonOctetErrors": sigChanNisFramerNonOctetErrors,
       "sigChanNisFramerOverruns": sigChanNisFramerOverruns,
       "sigChanNisFramerUnderruns": sigChanNisFramerUnderruns,
       "sigChanNisFramerLargeFrmErrors": sigChanNisFramerLargeFrmErrors,
       "sigChanNisL2Table": sigChanNisL2Table,
       "sigChanNisL2Entry": sigChanNisL2Entry,
       "sigChanNisT23": sigChanNisT23,
       "sigChanNisT200": sigChanNisT200,
       "sigChanNisN200": sigChanNisN200,
       "sigChanNisT203": sigChanNisT203,
       "sigChanNisCircuitSwitchedK": sigChanNisCircuitSwitchedK,
       "sigChanNisL3Table": sigChanNisL3Table,
       "sigChanNisL3Entry": sigChanNisL3Entry,
       "sigChanNisT309": sigChanNisT309,
       "sigChanNisT310": sigChanNisT310,
       "sigChanNisProvTable": sigChanNisProvTable,
       "sigChanNisProvEntry": sigChanNisProvEntry,
       "sigChanNisSide": sigChanNisSide,
       "sigChanNisMaxNonCallConcurrent": sigChanNisMaxNonCallConcurrent,
       "sigChanNisStateTable": sigChanNisStateTable,
       "sigChanNisStateEntry": sigChanNisStateEntry,
       "sigChanNisAdminState": sigChanNisAdminState,
       "sigChanNisOperationalState": sigChanNisOperationalState,
       "sigChanNisUsageState": sigChanNisUsageState,
       "sigChanNisStatsTable": sigChanNisStatsTable,
       "sigChanNisStatsEntry": sigChanNisStatsEntry,
       "sigChanNisTotalCallsToIf": sigChanNisTotalCallsToIf,
       "sigChanNisTotalCallsFromIf": sigChanNisTotalCallsFromIf,
       "sigChanNisNonCallAssocSessionsToIf": sigChanNisNonCallAssocSessionsToIf,
       "sigChanNisNonCallAssocSessionsFromIf": sigChanNisNonCallAssocSessionsFromIf,
       "sigChanNisOperTable": sigChanNisOperTable,
       "sigChanNisOperEntry": sigChanNisOperEntry,
       "sigChanNisActiveChannels": sigChanNisActiveChannels,
       "sigChanNisActiveVoiceChannels": sigChanNisActiveVoiceChannels,
       "sigChanNisActiveDataChannels": sigChanNisActiveDataChannels,
       "sigChanNisPeakActiveChannels": sigChanNisPeakActiveChannels,
       "sigChanNisPeakActiveVoiceChannels": sigChanNisPeakActiveVoiceChannels,
       "sigChanNisPeakActiveDataChannels": sigChanNisPeakActiveDataChannels,
       "sigChanNisDChanStatus": sigChanNisDChanStatus,
       "sigChanNisToolsTable": sigChanNisToolsTable,
       "sigChanNisToolsEntry": sigChanNisToolsEntry,
       "sigChanNisTracing": sigChanNisTracing,
       "sigChanNisNisSpecificProvTable": sigChanNisNisSpecificProvTable,
       "sigChanNisNisSpecificProvEntry": sigChanNisNisSpecificProvEntry,
       "sigChanNisChanMaintenanceHandling": sigChanNisChanMaintenanceHandling,
       "vnetNisSigMIB": vnetNisSigMIB,
       "vnetNisSigGroup": vnetNisSigGroup,
       "vnetNisSigGroupBE": vnetNisSigGroupBE,
       "vnetNisSigGroupBE01": vnetNisSigGroupBE01,
       "vnetNisSigGroupBE01A": vnetNisSigGroupBE01A,
       "vnetNisSigCapabilities": vnetNisSigCapabilities,
       "vnetNisSigCapabilitiesBE": vnetNisSigCapabilitiesBE,
       "vnetNisSigCapabilitiesBE01": vnetNisSigCapabilitiesBE01,
       "vnetNisSigCapabilitiesBE01A": vnetNisSigCapabilitiesBE01A}
)
