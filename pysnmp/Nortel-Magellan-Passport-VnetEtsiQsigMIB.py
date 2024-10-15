# SNMP MIB module (Nortel-Magellan-Passport-VnetEtsiQsigMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VnetEtsiQsigMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:35 2024
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

_SigChanEQsig_ObjectIdentity = ObjectIdentity
sigChanEQsig = _SigChanEQsig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2)
)
_SigChanEQsigRowStatusTable_Object = MibTable
sigChanEQsigRowStatusTable = _SigChanEQsigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 1)
)
if mibBuilder.loadTexts:
    sigChanEQsigRowStatusTable.setStatus("mandatory")
_SigChanEQsigRowStatusEntry_Object = MibTableRow
sigChanEQsigRowStatusEntry = _SigChanEQsigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 1, 1)
)
sigChanEQsigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigRowStatusEntry.setStatus("mandatory")
_SigChanEQsigRowStatus_Type = RowStatus
_SigChanEQsigRowStatus_Object = MibTableColumn
sigChanEQsigRowStatus = _SigChanEQsigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 1, 1, 1),
    _SigChanEQsigRowStatus_Type()
)
sigChanEQsigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigRowStatus.setStatus("mandatory")
_SigChanEQsigComponentName_Type = DisplayString
_SigChanEQsigComponentName_Object = MibTableColumn
sigChanEQsigComponentName = _SigChanEQsigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 1, 1, 2),
    _SigChanEQsigComponentName_Type()
)
sigChanEQsigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigComponentName.setStatus("mandatory")
_SigChanEQsigStorageType_Type = StorageType
_SigChanEQsigStorageType_Object = MibTableColumn
sigChanEQsigStorageType = _SigChanEQsigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 1, 1, 4),
    _SigChanEQsigStorageType_Type()
)
sigChanEQsigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigStorageType.setStatus("mandatory")
_SigChanEQsigIndex_Type = NonReplicated
_SigChanEQsigIndex_Object = MibTableColumn
sigChanEQsigIndex = _SigChanEQsigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 1, 1, 10),
    _SigChanEQsigIndex_Type()
)
sigChanEQsigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanEQsigIndex.setStatus("mandatory")
_SigChanEQsigFramer_ObjectIdentity = ObjectIdentity
sigChanEQsigFramer = _SigChanEQsigFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2)
)
_SigChanEQsigFramerRowStatusTable_Object = MibTable
sigChanEQsigFramerRowStatusTable = _SigChanEQsigFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sigChanEQsigFramerRowStatusTable.setStatus("mandatory")
_SigChanEQsigFramerRowStatusEntry_Object = MibTableRow
sigChanEQsigFramerRowStatusEntry = _SigChanEQsigFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 1, 1)
)
sigChanEQsigFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigFramerRowStatusEntry.setStatus("mandatory")
_SigChanEQsigFramerRowStatus_Type = RowStatus
_SigChanEQsigFramerRowStatus_Object = MibTableColumn
sigChanEQsigFramerRowStatus = _SigChanEQsigFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 1, 1, 1),
    _SigChanEQsigFramerRowStatus_Type()
)
sigChanEQsigFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerRowStatus.setStatus("mandatory")
_SigChanEQsigFramerComponentName_Type = DisplayString
_SigChanEQsigFramerComponentName_Object = MibTableColumn
sigChanEQsigFramerComponentName = _SigChanEQsigFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 1, 1, 2),
    _SigChanEQsigFramerComponentName_Type()
)
sigChanEQsigFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerComponentName.setStatus("mandatory")
_SigChanEQsigFramerStorageType_Type = StorageType
_SigChanEQsigFramerStorageType_Object = MibTableColumn
sigChanEQsigFramerStorageType = _SigChanEQsigFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 1, 1, 4),
    _SigChanEQsigFramerStorageType_Type()
)
sigChanEQsigFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerStorageType.setStatus("mandatory")
_SigChanEQsigFramerIndex_Type = NonReplicated
_SigChanEQsigFramerIndex_Object = MibTableColumn
sigChanEQsigFramerIndex = _SigChanEQsigFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 1, 1, 10),
    _SigChanEQsigFramerIndex_Type()
)
sigChanEQsigFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigChanEQsigFramerIndex.setStatus("mandatory")
_SigChanEQsigFramerProvTable_Object = MibTable
sigChanEQsigFramerProvTable = _SigChanEQsigFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 10)
)
if mibBuilder.loadTexts:
    sigChanEQsigFramerProvTable.setStatus("mandatory")
_SigChanEQsigFramerProvEntry_Object = MibTableRow
sigChanEQsigFramerProvEntry = _SigChanEQsigFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 10, 1)
)
sigChanEQsigFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigFramerProvEntry.setStatus("mandatory")
_SigChanEQsigFramerInterfaceName_Type = Link
_SigChanEQsigFramerInterfaceName_Object = MibTableColumn
sigChanEQsigFramerInterfaceName = _SigChanEQsigFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 10, 1, 1),
    _SigChanEQsigFramerInterfaceName_Type()
)
sigChanEQsigFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigFramerInterfaceName.setStatus("mandatory")
_SigChanEQsigFramerStateTable_Object = MibTable
sigChanEQsigFramerStateTable = _SigChanEQsigFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 12)
)
if mibBuilder.loadTexts:
    sigChanEQsigFramerStateTable.setStatus("mandatory")
_SigChanEQsigFramerStateEntry_Object = MibTableRow
sigChanEQsigFramerStateEntry = _SigChanEQsigFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 12, 1)
)
sigChanEQsigFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigFramerStateEntry.setStatus("mandatory")


class _SigChanEQsigFramerAdminState_Type(Integer32):
    """Custom type sigChanEQsigFramerAdminState based on Integer32"""
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


_SigChanEQsigFramerAdminState_Type.__name__ = "Integer32"
_SigChanEQsigFramerAdminState_Object = MibTableColumn
sigChanEQsigFramerAdminState = _SigChanEQsigFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 12, 1, 1),
    _SigChanEQsigFramerAdminState_Type()
)
sigChanEQsigFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerAdminState.setStatus("mandatory")


class _SigChanEQsigFramerOperationalState_Type(Integer32):
    """Custom type sigChanEQsigFramerOperationalState based on Integer32"""
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


_SigChanEQsigFramerOperationalState_Type.__name__ = "Integer32"
_SigChanEQsigFramerOperationalState_Object = MibTableColumn
sigChanEQsigFramerOperationalState = _SigChanEQsigFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 12, 1, 2),
    _SigChanEQsigFramerOperationalState_Type()
)
sigChanEQsigFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerOperationalState.setStatus("mandatory")


class _SigChanEQsigFramerUsageState_Type(Integer32):
    """Custom type sigChanEQsigFramerUsageState based on Integer32"""
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


_SigChanEQsigFramerUsageState_Type.__name__ = "Integer32"
_SigChanEQsigFramerUsageState_Object = MibTableColumn
sigChanEQsigFramerUsageState = _SigChanEQsigFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 12, 1, 3),
    _SigChanEQsigFramerUsageState_Type()
)
sigChanEQsigFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerUsageState.setStatus("mandatory")
_SigChanEQsigFramerStatsTable_Object = MibTable
sigChanEQsigFramerStatsTable = _SigChanEQsigFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13)
)
if mibBuilder.loadTexts:
    sigChanEQsigFramerStatsTable.setStatus("mandatory")
_SigChanEQsigFramerStatsEntry_Object = MibTableRow
sigChanEQsigFramerStatsEntry = _SigChanEQsigFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1)
)
sigChanEQsigFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigFramerIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigFramerStatsEntry.setStatus("mandatory")


class _SigChanEQsigFramerFrmToIf_Type(Unsigned32):
    """Custom type sigChanEQsigFramerFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerFrmToIf_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerFrmToIf_Object = MibTableColumn
sigChanEQsigFramerFrmToIf = _SigChanEQsigFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 1),
    _SigChanEQsigFramerFrmToIf_Type()
)
sigChanEQsigFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerFrmToIf.setStatus("mandatory")


class _SigChanEQsigFramerFrmFromIf_Type(Unsigned32):
    """Custom type sigChanEQsigFramerFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerFrmFromIf_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerFrmFromIf_Object = MibTableColumn
sigChanEQsigFramerFrmFromIf = _SigChanEQsigFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 2),
    _SigChanEQsigFramerFrmFromIf_Type()
)
sigChanEQsigFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerFrmFromIf.setStatus("mandatory")


class _SigChanEQsigFramerOctetFromIf_Type(Unsigned32):
    """Custom type sigChanEQsigFramerOctetFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerOctetFromIf_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerOctetFromIf_Object = MibTableColumn
sigChanEQsigFramerOctetFromIf = _SigChanEQsigFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 3),
    _SigChanEQsigFramerOctetFromIf_Type()
)
sigChanEQsigFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerOctetFromIf.setStatus("mandatory")


class _SigChanEQsigFramerAborts_Type(Unsigned32):
    """Custom type sigChanEQsigFramerAborts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerAborts_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerAborts_Object = MibTableColumn
sigChanEQsigFramerAborts = _SigChanEQsigFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 4),
    _SigChanEQsigFramerAborts_Type()
)
sigChanEQsigFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerAborts.setStatus("mandatory")


class _SigChanEQsigFramerCrcErrors_Type(Unsigned32):
    """Custom type sigChanEQsigFramerCrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerCrcErrors_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerCrcErrors_Object = MibTableColumn
sigChanEQsigFramerCrcErrors = _SigChanEQsigFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 5),
    _SigChanEQsigFramerCrcErrors_Type()
)
sigChanEQsigFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerCrcErrors.setStatus("mandatory")


class _SigChanEQsigFramerLrcErrors_Type(Unsigned32):
    """Custom type sigChanEQsigFramerLrcErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerLrcErrors_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerLrcErrors_Object = MibTableColumn
sigChanEQsigFramerLrcErrors = _SigChanEQsigFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 6),
    _SigChanEQsigFramerLrcErrors_Type()
)
sigChanEQsigFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerLrcErrors.setStatus("mandatory")


class _SigChanEQsigFramerNonOctetErrors_Type(Unsigned32):
    """Custom type sigChanEQsigFramerNonOctetErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerNonOctetErrors_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerNonOctetErrors_Object = MibTableColumn
sigChanEQsigFramerNonOctetErrors = _SigChanEQsigFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 7),
    _SigChanEQsigFramerNonOctetErrors_Type()
)
sigChanEQsigFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerNonOctetErrors.setStatus("mandatory")


class _SigChanEQsigFramerOverruns_Type(Unsigned32):
    """Custom type sigChanEQsigFramerOverruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerOverruns_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerOverruns_Object = MibTableColumn
sigChanEQsigFramerOverruns = _SigChanEQsigFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 8),
    _SigChanEQsigFramerOverruns_Type()
)
sigChanEQsigFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerOverruns.setStatus("mandatory")


class _SigChanEQsigFramerUnderruns_Type(Unsigned32):
    """Custom type sigChanEQsigFramerUnderruns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerUnderruns_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerUnderruns_Object = MibTableColumn
sigChanEQsigFramerUnderruns = _SigChanEQsigFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 9),
    _SigChanEQsigFramerUnderruns_Type()
)
sigChanEQsigFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerUnderruns.setStatus("mandatory")


class _SigChanEQsigFramerLargeFrmErrors_Type(Unsigned32):
    """Custom type sigChanEQsigFramerLargeFrmErrors based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigFramerLargeFrmErrors_Type.__name__ = "Unsigned32"
_SigChanEQsigFramerLargeFrmErrors_Object = MibTableColumn
sigChanEQsigFramerLargeFrmErrors = _SigChanEQsigFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 2, 13, 1, 10),
    _SigChanEQsigFramerLargeFrmErrors_Type()
)
sigChanEQsigFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigFramerLargeFrmErrors.setStatus("mandatory")
_SigChanEQsigL2Table_Object = MibTable
sigChanEQsigL2Table = _SigChanEQsigL2Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 11)
)
if mibBuilder.loadTexts:
    sigChanEQsigL2Table.setStatus("mandatory")
_SigChanEQsigL2Entry_Object = MibTableRow
sigChanEQsigL2Entry = _SigChanEQsigL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 11, 1)
)
sigChanEQsigL2Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigL2Entry.setStatus("mandatory")


class _SigChanEQsigT23_Type(Unsigned32):
    """Custom type sigChanEQsigT23 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SigChanEQsigT23_Type.__name__ = "Unsigned32"
_SigChanEQsigT23_Object = MibTableColumn
sigChanEQsigT23 = _SigChanEQsigT23_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 11, 1, 1),
    _SigChanEQsigT23_Type()
)
sigChanEQsigT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigT23.setStatus("mandatory")


class _SigChanEQsigT200_Type(Unsigned32):
    """Custom type sigChanEQsigT200 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SigChanEQsigT200_Type.__name__ = "Unsigned32"
_SigChanEQsigT200_Object = MibTableColumn
sigChanEQsigT200 = _SigChanEQsigT200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 11, 1, 2),
    _SigChanEQsigT200_Type()
)
sigChanEQsigT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigT200.setStatus("mandatory")


class _SigChanEQsigN200_Type(Unsigned32):
    """Custom type sigChanEQsigN200 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SigChanEQsigN200_Type.__name__ = "Unsigned32"
_SigChanEQsigN200_Object = MibTableColumn
sigChanEQsigN200 = _SigChanEQsigN200_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 11, 1, 3),
    _SigChanEQsigN200_Type()
)
sigChanEQsigN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigN200.setStatus("mandatory")


class _SigChanEQsigT203_Type(Unsigned32):
    """Custom type sigChanEQsigT203 based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_SigChanEQsigT203_Type.__name__ = "Unsigned32"
_SigChanEQsigT203_Object = MibTableColumn
sigChanEQsigT203 = _SigChanEQsigT203_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 11, 1, 4),
    _SigChanEQsigT203_Type()
)
sigChanEQsigT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigT203.setStatus("mandatory")


class _SigChanEQsigCircuitSwitchedK_Type(Unsigned32):
    """Custom type sigChanEQsigCircuitSwitchedK based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SigChanEQsigCircuitSwitchedK_Type.__name__ = "Unsigned32"
_SigChanEQsigCircuitSwitchedK_Object = MibTableColumn
sigChanEQsigCircuitSwitchedK = _SigChanEQsigCircuitSwitchedK_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 11, 1, 6),
    _SigChanEQsigCircuitSwitchedK_Type()
)
sigChanEQsigCircuitSwitchedK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigCircuitSwitchedK.setStatus("mandatory")
_SigChanEQsigL3Table_Object = MibTable
sigChanEQsigL3Table = _SigChanEQsigL3Table_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 12)
)
if mibBuilder.loadTexts:
    sigChanEQsigL3Table.setStatus("mandatory")
_SigChanEQsigL3Entry_Object = MibTableRow
sigChanEQsigL3Entry = _SigChanEQsigL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 12, 1)
)
sigChanEQsigL3Entry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigL3Entry.setStatus("mandatory")


class _SigChanEQsigT309_Type(Unsigned32):
    """Custom type sigChanEQsigT309 based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 120),
    )


_SigChanEQsigT309_Type.__name__ = "Unsigned32"
_SigChanEQsigT309_Object = MibTableColumn
sigChanEQsigT309 = _SigChanEQsigT309_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 12, 1, 3),
    _SigChanEQsigT309_Type()
)
sigChanEQsigT309.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigT309.setStatus("mandatory")


class _SigChanEQsigT310_Type(Unsigned32):
    """Custom type sigChanEQsigT310 based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_SigChanEQsigT310_Type.__name__ = "Unsigned32"
_SigChanEQsigT310_Object = MibTableColumn
sigChanEQsigT310 = _SigChanEQsigT310_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 12, 1, 4),
    _SigChanEQsigT310_Type()
)
sigChanEQsigT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigT310.setStatus("mandatory")
_SigChanEQsigProvTable_Object = MibTable
sigChanEQsigProvTable = _SigChanEQsigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 13)
)
if mibBuilder.loadTexts:
    sigChanEQsigProvTable.setStatus("mandatory")
_SigChanEQsigProvEntry_Object = MibTableRow
sigChanEQsigProvEntry = _SigChanEQsigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 13, 1)
)
sigChanEQsigProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigProvEntry.setStatus("mandatory")


class _SigChanEQsigSide_Type(Integer32):
    """Custom type sigChanEQsigSide based on Integer32"""
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


_SigChanEQsigSide_Type.__name__ = "Integer32"
_SigChanEQsigSide_Object = MibTableColumn
sigChanEQsigSide = _SigChanEQsigSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 13, 1, 1),
    _SigChanEQsigSide_Type()
)
sigChanEQsigSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigSide.setStatus("mandatory")


class _SigChanEQsigMaxNonCallConcurrent_Type(Unsigned32):
    """Custom type sigChanEQsigMaxNonCallConcurrent based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SigChanEQsigMaxNonCallConcurrent_Type.__name__ = "Unsigned32"
_SigChanEQsigMaxNonCallConcurrent_Object = MibTableColumn
sigChanEQsigMaxNonCallConcurrent = _SigChanEQsigMaxNonCallConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 13, 1, 2),
    _SigChanEQsigMaxNonCallConcurrent_Type()
)
sigChanEQsigMaxNonCallConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigMaxNonCallConcurrent.setStatus("mandatory")


class _SigChanEQsigOverlapSendingEnabled_Type(Integer32):
    """Custom type sigChanEQsigOverlapSendingEnabled based on Integer32"""
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


_SigChanEQsigOverlapSendingEnabled_Type.__name__ = "Integer32"
_SigChanEQsigOverlapSendingEnabled_Object = MibTableColumn
sigChanEQsigOverlapSendingEnabled = _SigChanEQsigOverlapSendingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 13, 1, 3),
    _SigChanEQsigOverlapSendingEnabled_Type()
)
sigChanEQsigOverlapSendingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigOverlapSendingEnabled.setStatus("mandatory")


class _SigChanEQsigOverlapReceivingEnabled_Type(Integer32):
    """Custom type sigChanEQsigOverlapReceivingEnabled based on Integer32"""
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


_SigChanEQsigOverlapReceivingEnabled_Type.__name__ = "Integer32"
_SigChanEQsigOverlapReceivingEnabled_Object = MibTableColumn
sigChanEQsigOverlapReceivingEnabled = _SigChanEQsigOverlapReceivingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 13, 1, 4),
    _SigChanEQsigOverlapReceivingEnabled_Type()
)
sigChanEQsigOverlapReceivingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigOverlapReceivingEnabled.setStatus("mandatory")
_SigChanEQsigStateTable_Object = MibTable
sigChanEQsigStateTable = _SigChanEQsigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 14)
)
if mibBuilder.loadTexts:
    sigChanEQsigStateTable.setStatus("mandatory")
_SigChanEQsigStateEntry_Object = MibTableRow
sigChanEQsigStateEntry = _SigChanEQsigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 14, 1)
)
sigChanEQsigStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigStateEntry.setStatus("mandatory")


class _SigChanEQsigAdminState_Type(Integer32):
    """Custom type sigChanEQsigAdminState based on Integer32"""
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


_SigChanEQsigAdminState_Type.__name__ = "Integer32"
_SigChanEQsigAdminState_Object = MibTableColumn
sigChanEQsigAdminState = _SigChanEQsigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 14, 1, 1),
    _SigChanEQsigAdminState_Type()
)
sigChanEQsigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigAdminState.setStatus("mandatory")


class _SigChanEQsigOperationalState_Type(Integer32):
    """Custom type sigChanEQsigOperationalState based on Integer32"""
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


_SigChanEQsigOperationalState_Type.__name__ = "Integer32"
_SigChanEQsigOperationalState_Object = MibTableColumn
sigChanEQsigOperationalState = _SigChanEQsigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 14, 1, 2),
    _SigChanEQsigOperationalState_Type()
)
sigChanEQsigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigOperationalState.setStatus("mandatory")


class _SigChanEQsigUsageState_Type(Integer32):
    """Custom type sigChanEQsigUsageState based on Integer32"""
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


_SigChanEQsigUsageState_Type.__name__ = "Integer32"
_SigChanEQsigUsageState_Object = MibTableColumn
sigChanEQsigUsageState = _SigChanEQsigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 14, 1, 3),
    _SigChanEQsigUsageState_Type()
)
sigChanEQsigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigUsageState.setStatus("mandatory")
_SigChanEQsigStatsTable_Object = MibTable
sigChanEQsigStatsTable = _SigChanEQsigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 15)
)
if mibBuilder.loadTexts:
    sigChanEQsigStatsTable.setStatus("mandatory")
_SigChanEQsigStatsEntry_Object = MibTableRow
sigChanEQsigStatsEntry = _SigChanEQsigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 15, 1)
)
sigChanEQsigStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigStatsEntry.setStatus("mandatory")


class _SigChanEQsigTotalCallsToIf_Type(Unsigned32):
    """Custom type sigChanEQsigTotalCallsToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigTotalCallsToIf_Type.__name__ = "Unsigned32"
_SigChanEQsigTotalCallsToIf_Object = MibTableColumn
sigChanEQsigTotalCallsToIf = _SigChanEQsigTotalCallsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 15, 1, 2),
    _SigChanEQsigTotalCallsToIf_Type()
)
sigChanEQsigTotalCallsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigTotalCallsToIf.setStatus("mandatory")


class _SigChanEQsigTotalCallsFromIf_Type(Unsigned32):
    """Custom type sigChanEQsigTotalCallsFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigTotalCallsFromIf_Type.__name__ = "Unsigned32"
_SigChanEQsigTotalCallsFromIf_Object = MibTableColumn
sigChanEQsigTotalCallsFromIf = _SigChanEQsigTotalCallsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 15, 1, 3),
    _SigChanEQsigTotalCallsFromIf_Type()
)
sigChanEQsigTotalCallsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigTotalCallsFromIf.setStatus("mandatory")


class _SigChanEQsigNonCallAssocSessionsToIf_Type(Unsigned32):
    """Custom type sigChanEQsigNonCallAssocSessionsToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigNonCallAssocSessionsToIf_Type.__name__ = "Unsigned32"
_SigChanEQsigNonCallAssocSessionsToIf_Object = MibTableColumn
sigChanEQsigNonCallAssocSessionsToIf = _SigChanEQsigNonCallAssocSessionsToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 15, 1, 4),
    _SigChanEQsigNonCallAssocSessionsToIf_Type()
)
sigChanEQsigNonCallAssocSessionsToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigNonCallAssocSessionsToIf.setStatus("mandatory")


class _SigChanEQsigNonCallAssocSessionsFromIf_Type(Unsigned32):
    """Custom type sigChanEQsigNonCallAssocSessionsFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigNonCallAssocSessionsFromIf_Type.__name__ = "Unsigned32"
_SigChanEQsigNonCallAssocSessionsFromIf_Object = MibTableColumn
sigChanEQsigNonCallAssocSessionsFromIf = _SigChanEQsigNonCallAssocSessionsFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 15, 1, 5),
    _SigChanEQsigNonCallAssocSessionsFromIf_Type()
)
sigChanEQsigNonCallAssocSessionsFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigNonCallAssocSessionsFromIf.setStatus("mandatory")
_SigChanEQsigOperTable_Object = MibTable
sigChanEQsigOperTable = _SigChanEQsigOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 16)
)
if mibBuilder.loadTexts:
    sigChanEQsigOperTable.setStatus("mandatory")
_SigChanEQsigOperEntry_Object = MibTableRow
sigChanEQsigOperEntry = _SigChanEQsigOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 16, 1)
)
sigChanEQsigOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigOperEntry.setStatus("mandatory")


class _SigChanEQsigActiveChannels_Type(Unsigned32):
    """Custom type sigChanEQsigActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEQsigActiveChannels_Type.__name__ = "Unsigned32"
_SigChanEQsigActiveChannels_Object = MibTableColumn
sigChanEQsigActiveChannels = _SigChanEQsigActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 16, 1, 1),
    _SigChanEQsigActiveChannels_Type()
)
sigChanEQsigActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigActiveChannels.setStatus("mandatory")


class _SigChanEQsigActiveVoiceChannels_Type(Unsigned32):
    """Custom type sigChanEQsigActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEQsigActiveVoiceChannels_Type.__name__ = "Unsigned32"
_SigChanEQsigActiveVoiceChannels_Object = MibTableColumn
sigChanEQsigActiveVoiceChannels = _SigChanEQsigActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 16, 1, 2),
    _SigChanEQsigActiveVoiceChannels_Type()
)
sigChanEQsigActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigActiveVoiceChannels.setStatus("mandatory")


class _SigChanEQsigActiveDataChannels_Type(Unsigned32):
    """Custom type sigChanEQsigActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEQsigActiveDataChannels_Type.__name__ = "Unsigned32"
_SigChanEQsigActiveDataChannels_Object = MibTableColumn
sigChanEQsigActiveDataChannels = _SigChanEQsigActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 16, 1, 3),
    _SigChanEQsigActiveDataChannels_Type()
)
sigChanEQsigActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigActiveDataChannels.setStatus("mandatory")


class _SigChanEQsigPeakActiveChannels_Type(Unsigned32):
    """Custom type sigChanEQsigPeakActiveChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEQsigPeakActiveChannels_Type.__name__ = "Unsigned32"
_SigChanEQsigPeakActiveChannels_Object = MibTableColumn
sigChanEQsigPeakActiveChannels = _SigChanEQsigPeakActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 16, 1, 4),
    _SigChanEQsigPeakActiveChannels_Type()
)
sigChanEQsigPeakActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigPeakActiveChannels.setStatus("mandatory")


class _SigChanEQsigPeakActiveVoiceChannels_Type(Unsigned32):
    """Custom type sigChanEQsigPeakActiveVoiceChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEQsigPeakActiveVoiceChannels_Type.__name__ = "Unsigned32"
_SigChanEQsigPeakActiveVoiceChannels_Object = MibTableColumn
sigChanEQsigPeakActiveVoiceChannels = _SigChanEQsigPeakActiveVoiceChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 16, 1, 5),
    _SigChanEQsigPeakActiveVoiceChannels_Type()
)
sigChanEQsigPeakActiveVoiceChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigPeakActiveVoiceChannels.setStatus("mandatory")


class _SigChanEQsigPeakActiveDataChannels_Type(Unsigned32):
    """Custom type sigChanEQsigPeakActiveDataChannels based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SigChanEQsigPeakActiveDataChannels_Type.__name__ = "Unsigned32"
_SigChanEQsigPeakActiveDataChannels_Object = MibTableColumn
sigChanEQsigPeakActiveDataChannels = _SigChanEQsigPeakActiveDataChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 16, 1, 6),
    _SigChanEQsigPeakActiveDataChannels_Type()
)
sigChanEQsigPeakActiveDataChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigPeakActiveDataChannels.setStatus("mandatory")


class _SigChanEQsigDChanStatus_Type(Integer32):
    """Custom type sigChanEQsigDChanStatus based on Integer32"""
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


_SigChanEQsigDChanStatus_Type.__name__ = "Integer32"
_SigChanEQsigDChanStatus_Object = MibTableColumn
sigChanEQsigDChanStatus = _SigChanEQsigDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 16, 1, 7),
    _SigChanEQsigDChanStatus_Type()
)
sigChanEQsigDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigDChanStatus.setStatus("mandatory")
_SigChanEQsigToolsTable_Object = MibTable
sigChanEQsigToolsTable = _SigChanEQsigToolsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 17)
)
if mibBuilder.loadTexts:
    sigChanEQsigToolsTable.setStatus("mandatory")
_SigChanEQsigToolsEntry_Object = MibTableRow
sigChanEQsigToolsEntry = _SigChanEQsigToolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 17, 1)
)
sigChanEQsigToolsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigToolsEntry.setStatus("mandatory")


class _SigChanEQsigTracing_Type(OctetString):
    """Custom type sigChanEQsigTracing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SigChanEQsigTracing_Type.__name__ = "OctetString"
_SigChanEQsigTracing_Object = MibTableColumn
sigChanEQsigTracing = _SigChanEQsigTracing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 17, 1, 1),
    _SigChanEQsigTracing_Type()
)
sigChanEQsigTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigTracing.setStatus("mandatory")
_SigChanEQsigEQsigSpecificProvTable_Object = MibTable
sigChanEQsigEQsigSpecificProvTable = _SigChanEQsigEQsigSpecificProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 18)
)
if mibBuilder.loadTexts:
    sigChanEQsigEQsigSpecificProvTable.setStatus("mandatory")
_SigChanEQsigEQsigSpecificProvEntry_Object = MibTableRow
sigChanEQsigEQsigSpecificProvEntry = _SigChanEQsigEQsigSpecificProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 18, 1)
)
sigChanEQsigEQsigSpecificProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigEQsigSpecificProvEntry.setStatus("mandatory")


class _SigChanEQsigMsgSegmentation_Type(Integer32):
    """Custom type sigChanEQsigMsgSegmentation based on Integer32"""
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


_SigChanEQsigMsgSegmentation_Type.__name__ = "Integer32"
_SigChanEQsigMsgSegmentation_Object = MibTableColumn
sigChanEQsigMsgSegmentation = _SigChanEQsigMsgSegmentation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 18, 1, 1),
    _SigChanEQsigMsgSegmentation_Type()
)
sigChanEQsigMsgSegmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigMsgSegmentation.setStatus("mandatory")


class _SigChanEQsigE1ChannelNumbers_Type(Integer32):
    """Custom type sigChanEQsigE1ChannelNumbers based on Integer32"""
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


_SigChanEQsigE1ChannelNumbers_Type.__name__ = "Integer32"
_SigChanEQsigE1ChannelNumbers_Object = MibTableColumn
sigChanEQsigE1ChannelNumbers = _SigChanEQsigE1ChannelNumbers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 18, 1, 2),
    _SigChanEQsigE1ChannelNumbers_Type()
)
sigChanEQsigE1ChannelNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigChanEQsigE1ChannelNumbers.setStatus("mandatory")
_SigChanEQsigEQsigSpecificOpTable_Object = MibTable
sigChanEQsigEQsigSpecificOpTable = _SigChanEQsigEQsigSpecificOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 19)
)
if mibBuilder.loadTexts:
    sigChanEQsigEQsigSpecificOpTable.setStatus("mandatory")
_SigChanEQsigEQsigSpecificOpEntry_Object = MibTableRow
sigChanEQsigEQsigSpecificOpEntry = _SigChanEQsigEQsigSpecificOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 19, 1)
)
sigChanEQsigEQsigSpecificOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VoiceNetworkingMIB", "sigChanIndex"),
    (0, "Nortel-Magellan-Passport-VnetEtsiQsigMIB", "sigChanEQsigIndex"),
)
if mibBuilder.loadTexts:
    sigChanEQsigEQsigSpecificOpEntry.setStatus("mandatory")


class _SigChanEQsigSegmentationAccepted_Type(Unsigned32):
    """Custom type sigChanEQsigSegmentationAccepted based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigSegmentationAccepted_Type.__name__ = "Unsigned32"
_SigChanEQsigSegmentationAccepted_Object = MibTableColumn
sigChanEQsigSegmentationAccepted = _SigChanEQsigSegmentationAccepted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 19, 1, 1),
    _SigChanEQsigSegmentationAccepted_Type()
)
sigChanEQsigSegmentationAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigSegmentationAccepted.setStatus("mandatory")


class _SigChanEQsigSegmentationFailed_Type(Unsigned32):
    """Custom type sigChanEQsigSegmentationFailed based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SigChanEQsigSegmentationFailed_Type.__name__ = "Unsigned32"
_SigChanEQsigSegmentationFailed_Object = MibTableColumn
sigChanEQsigSegmentationFailed = _SigChanEQsigSegmentationFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 115, 2, 19, 1, 2),
    _SigChanEQsigSegmentationFailed_Type()
)
sigChanEQsigSegmentationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sigChanEQsigSegmentationFailed.setStatus("mandatory")
_VnetEtsiQsigMIB_ObjectIdentity = ObjectIdentity
vnetEtsiQsigMIB = _VnetEtsiQsigMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 110)
)
_VnetEtsiQsigGroup_ObjectIdentity = ObjectIdentity
vnetEtsiQsigGroup = _VnetEtsiQsigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 110, 1)
)
_VnetEtsiQsigGroupBE_ObjectIdentity = ObjectIdentity
vnetEtsiQsigGroupBE = _VnetEtsiQsigGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 110, 1, 5)
)
_VnetEtsiQsigGroupBE01_ObjectIdentity = ObjectIdentity
vnetEtsiQsigGroupBE01 = _VnetEtsiQsigGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 110, 1, 5, 2)
)
_VnetEtsiQsigGroupBE01A_ObjectIdentity = ObjectIdentity
vnetEtsiQsigGroupBE01A = _VnetEtsiQsigGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 110, 1, 5, 2, 2)
)
_VnetEtsiQsigCapabilities_ObjectIdentity = ObjectIdentity
vnetEtsiQsigCapabilities = _VnetEtsiQsigCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 110, 3)
)
_VnetEtsiQsigCapabilitiesBE_ObjectIdentity = ObjectIdentity
vnetEtsiQsigCapabilitiesBE = _VnetEtsiQsigCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 110, 3, 5)
)
_VnetEtsiQsigCapabilitiesBE01_ObjectIdentity = ObjectIdentity
vnetEtsiQsigCapabilitiesBE01 = _VnetEtsiQsigCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 110, 3, 5, 2)
)
_VnetEtsiQsigCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
vnetEtsiQsigCapabilitiesBE01A = _VnetEtsiQsigCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 110, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VnetEtsiQsigMIB",
    **{"sigChanEQsig": sigChanEQsig,
       "sigChanEQsigRowStatusTable": sigChanEQsigRowStatusTable,
       "sigChanEQsigRowStatusEntry": sigChanEQsigRowStatusEntry,
       "sigChanEQsigRowStatus": sigChanEQsigRowStatus,
       "sigChanEQsigComponentName": sigChanEQsigComponentName,
       "sigChanEQsigStorageType": sigChanEQsigStorageType,
       "sigChanEQsigIndex": sigChanEQsigIndex,
       "sigChanEQsigFramer": sigChanEQsigFramer,
       "sigChanEQsigFramerRowStatusTable": sigChanEQsigFramerRowStatusTable,
       "sigChanEQsigFramerRowStatusEntry": sigChanEQsigFramerRowStatusEntry,
       "sigChanEQsigFramerRowStatus": sigChanEQsigFramerRowStatus,
       "sigChanEQsigFramerComponentName": sigChanEQsigFramerComponentName,
       "sigChanEQsigFramerStorageType": sigChanEQsigFramerStorageType,
       "sigChanEQsigFramerIndex": sigChanEQsigFramerIndex,
       "sigChanEQsigFramerProvTable": sigChanEQsigFramerProvTable,
       "sigChanEQsigFramerProvEntry": sigChanEQsigFramerProvEntry,
       "sigChanEQsigFramerInterfaceName": sigChanEQsigFramerInterfaceName,
       "sigChanEQsigFramerStateTable": sigChanEQsigFramerStateTable,
       "sigChanEQsigFramerStateEntry": sigChanEQsigFramerStateEntry,
       "sigChanEQsigFramerAdminState": sigChanEQsigFramerAdminState,
       "sigChanEQsigFramerOperationalState": sigChanEQsigFramerOperationalState,
       "sigChanEQsigFramerUsageState": sigChanEQsigFramerUsageState,
       "sigChanEQsigFramerStatsTable": sigChanEQsigFramerStatsTable,
       "sigChanEQsigFramerStatsEntry": sigChanEQsigFramerStatsEntry,
       "sigChanEQsigFramerFrmToIf": sigChanEQsigFramerFrmToIf,
       "sigChanEQsigFramerFrmFromIf": sigChanEQsigFramerFrmFromIf,
       "sigChanEQsigFramerOctetFromIf": sigChanEQsigFramerOctetFromIf,
       "sigChanEQsigFramerAborts": sigChanEQsigFramerAborts,
       "sigChanEQsigFramerCrcErrors": sigChanEQsigFramerCrcErrors,
       "sigChanEQsigFramerLrcErrors": sigChanEQsigFramerLrcErrors,
       "sigChanEQsigFramerNonOctetErrors": sigChanEQsigFramerNonOctetErrors,
       "sigChanEQsigFramerOverruns": sigChanEQsigFramerOverruns,
       "sigChanEQsigFramerUnderruns": sigChanEQsigFramerUnderruns,
       "sigChanEQsigFramerLargeFrmErrors": sigChanEQsigFramerLargeFrmErrors,
       "sigChanEQsigL2Table": sigChanEQsigL2Table,
       "sigChanEQsigL2Entry": sigChanEQsigL2Entry,
       "sigChanEQsigT23": sigChanEQsigT23,
       "sigChanEQsigT200": sigChanEQsigT200,
       "sigChanEQsigN200": sigChanEQsigN200,
       "sigChanEQsigT203": sigChanEQsigT203,
       "sigChanEQsigCircuitSwitchedK": sigChanEQsigCircuitSwitchedK,
       "sigChanEQsigL3Table": sigChanEQsigL3Table,
       "sigChanEQsigL3Entry": sigChanEQsigL3Entry,
       "sigChanEQsigT309": sigChanEQsigT309,
       "sigChanEQsigT310": sigChanEQsigT310,
       "sigChanEQsigProvTable": sigChanEQsigProvTable,
       "sigChanEQsigProvEntry": sigChanEQsigProvEntry,
       "sigChanEQsigSide": sigChanEQsigSide,
       "sigChanEQsigMaxNonCallConcurrent": sigChanEQsigMaxNonCallConcurrent,
       "sigChanEQsigOverlapSendingEnabled": sigChanEQsigOverlapSendingEnabled,
       "sigChanEQsigOverlapReceivingEnabled": sigChanEQsigOverlapReceivingEnabled,
       "sigChanEQsigStateTable": sigChanEQsigStateTable,
       "sigChanEQsigStateEntry": sigChanEQsigStateEntry,
       "sigChanEQsigAdminState": sigChanEQsigAdminState,
       "sigChanEQsigOperationalState": sigChanEQsigOperationalState,
       "sigChanEQsigUsageState": sigChanEQsigUsageState,
       "sigChanEQsigStatsTable": sigChanEQsigStatsTable,
       "sigChanEQsigStatsEntry": sigChanEQsigStatsEntry,
       "sigChanEQsigTotalCallsToIf": sigChanEQsigTotalCallsToIf,
       "sigChanEQsigTotalCallsFromIf": sigChanEQsigTotalCallsFromIf,
       "sigChanEQsigNonCallAssocSessionsToIf": sigChanEQsigNonCallAssocSessionsToIf,
       "sigChanEQsigNonCallAssocSessionsFromIf": sigChanEQsigNonCallAssocSessionsFromIf,
       "sigChanEQsigOperTable": sigChanEQsigOperTable,
       "sigChanEQsigOperEntry": sigChanEQsigOperEntry,
       "sigChanEQsigActiveChannels": sigChanEQsigActiveChannels,
       "sigChanEQsigActiveVoiceChannels": sigChanEQsigActiveVoiceChannels,
       "sigChanEQsigActiveDataChannels": sigChanEQsigActiveDataChannels,
       "sigChanEQsigPeakActiveChannels": sigChanEQsigPeakActiveChannels,
       "sigChanEQsigPeakActiveVoiceChannels": sigChanEQsigPeakActiveVoiceChannels,
       "sigChanEQsigPeakActiveDataChannels": sigChanEQsigPeakActiveDataChannels,
       "sigChanEQsigDChanStatus": sigChanEQsigDChanStatus,
       "sigChanEQsigToolsTable": sigChanEQsigToolsTable,
       "sigChanEQsigToolsEntry": sigChanEQsigToolsEntry,
       "sigChanEQsigTracing": sigChanEQsigTracing,
       "sigChanEQsigEQsigSpecificProvTable": sigChanEQsigEQsigSpecificProvTable,
       "sigChanEQsigEQsigSpecificProvEntry": sigChanEQsigEQsigSpecificProvEntry,
       "sigChanEQsigMsgSegmentation": sigChanEQsigMsgSegmentation,
       "sigChanEQsigE1ChannelNumbers": sigChanEQsigE1ChannelNumbers,
       "sigChanEQsigEQsigSpecificOpTable": sigChanEQsigEQsigSpecificOpTable,
       "sigChanEQsigEQsigSpecificOpEntry": sigChanEQsigEQsigSpecificOpEntry,
       "sigChanEQsigSegmentationAccepted": sigChanEQsigSegmentationAccepted,
       "sigChanEQsigSegmentationFailed": sigChanEQsigSegmentationFailed,
       "vnetEtsiQsigMIB": vnetEtsiQsigMIB,
       "vnetEtsiQsigGroup": vnetEtsiQsigGroup,
       "vnetEtsiQsigGroupBE": vnetEtsiQsigGroupBE,
       "vnetEtsiQsigGroupBE01": vnetEtsiQsigGroupBE01,
       "vnetEtsiQsigGroupBE01A": vnetEtsiQsigGroupBE01A,
       "vnetEtsiQsigCapabilities": vnetEtsiQsigCapabilities,
       "vnetEtsiQsigCapabilitiesBE": vnetEtsiQsigCapabilitiesBE,
       "vnetEtsiQsigCapabilitiesBE01": vnetEtsiQsigCapabilitiesBE01,
       "vnetEtsiQsigCapabilitiesBE01A": vnetEtsiQsigCapabilitiesBE01A}
)
