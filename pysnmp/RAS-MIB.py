# SNMP MIB module (RAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:48 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(MmAliasAddress,
 MmAliasTag,
 MmCallType,
 MmEndpointID,
 MmGatekeeperID,
 MmGlobalIdentifier,
 MmH225Crv,
 MmTAddressTag,
 mmH323Root) = mibBuilder.importSymbols(
    "MULTI-MEDIA-MIB-TC",
    "MmAliasAddress",
    "MmAliasTag",
    "MmCallType",
    "MmEndpointID",
    "MmGatekeeperID",
    "MmGlobalIdentifier",
    "MmH225Crv",
    "MmTAddressTag",
    "mmH323Root")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ras = ModuleIdentity(
    (0, 0, 8, 341, 1, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RasConfiguration_ObjectIdentity = ObjectIdentity
rasConfiguration = _RasConfiguration_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 2, 1)
)
_RasConfigurationTable_Object = MibTable
rasConfigurationTable = _RasConfigurationTable_Object(
    (0, 0, 8, 341, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rasConfigurationTable.setStatus("current")
_RasConfigurationTableEntry_Object = MibTableRow
rasConfigurationTableEntry = _RasConfigurationTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 2, 1, 1, 1)
)
rasConfigurationTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rasConfigurationTableEntry.setStatus("current")
_RasConfigurationGatekeeperIdentifier_Type = MmGatekeeperID
_RasConfigurationGatekeeperIdentifier_Object = MibTableColumn
rasConfigurationGatekeeperIdentifier = _RasConfigurationGatekeeperIdentifier_Object(
    (0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 1),
    _RasConfigurationGatekeeperIdentifier_Type()
)
rasConfigurationGatekeeperIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasConfigurationGatekeeperIdentifier.setStatus("current")


class _RasConfigurationTimer_Type(Integer32):
    """Custom type rasConfigurationTimer based on Integer32"""
    defaultValue = 3


_RasConfigurationTimer_Object = MibTableColumn
rasConfigurationTimer = _RasConfigurationTimer_Object(
    (0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 2),
    _RasConfigurationTimer_Type()
)
rasConfigurationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasConfigurationTimer.setStatus("current")
if mibBuilder.loadTexts:
    rasConfigurationTimer.setUnits("seconds")


class _RasConfigurationMaxNumberOfRetries_Type(Integer32):
    """Custom type rasConfigurationMaxNumberOfRetries based on Integer32"""
    defaultValue = 3


_RasConfigurationMaxNumberOfRetries_Object = MibTableColumn
rasConfigurationMaxNumberOfRetries = _RasConfigurationMaxNumberOfRetries_Object(
    (0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 3),
    _RasConfigurationMaxNumberOfRetries_Type()
)
rasConfigurationMaxNumberOfRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rasConfigurationMaxNumberOfRetries.setStatus("current")
_RasConfigurationGatekeeperDiscoveryAddressTag_Type = MmTAddressTag
_RasConfigurationGatekeeperDiscoveryAddressTag_Object = MibTableColumn
rasConfigurationGatekeeperDiscoveryAddressTag = _RasConfigurationGatekeeperDiscoveryAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 4),
    _RasConfigurationGatekeeperDiscoveryAddressTag_Type()
)
rasConfigurationGatekeeperDiscoveryAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasConfigurationGatekeeperDiscoveryAddressTag.setStatus("current")
_RasConfigurationGatekeeperDiscoveryAddress_Type = TAddress
_RasConfigurationGatekeeperDiscoveryAddress_Object = MibTableColumn
rasConfigurationGatekeeperDiscoveryAddress = _RasConfigurationGatekeeperDiscoveryAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 1, 1, 1, 5),
    _RasConfigurationGatekeeperDiscoveryAddress_Type()
)
rasConfigurationGatekeeperDiscoveryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasConfigurationGatekeeperDiscoveryAddress.setStatus("current")
_RasRegistration_ObjectIdentity = ObjectIdentity
rasRegistration = _RasRegistration_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 2, 2)
)
_RasRegistrationTable_Object = MibTable
rasRegistrationTable = _RasRegistrationTable_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rasRegistrationTable.setStatus("current")
_RasRegistrationTableEntry_Object = MibTableRow
rasRegistrationTableEntry = _RasRegistrationTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1)
)
rasRegistrationTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAS-MIB", "rasRegistrationCallSignallingAddressTag"),
    (0, "RAS-MIB", "rasRegistrationCallSignallingAddress"),
    (0, "RAS-MIB", "rasRegistrationSrcRasAddressTag"),
    (0, "RAS-MIB", "rasRegistrationSrcRasAddress"),
)
if mibBuilder.loadTexts:
    rasRegistrationTableEntry.setStatus("current")
_RasRegistrationCallSignallingAddressTag_Type = MmTAddressTag
_RasRegistrationCallSignallingAddressTag_Object = MibTableColumn
rasRegistrationCallSignallingAddressTag = _RasRegistrationCallSignallingAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 1),
    _RasRegistrationCallSignallingAddressTag_Type()
)
rasRegistrationCallSignallingAddressTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasRegistrationCallSignallingAddressTag.setStatus("current")
_RasRegistrationCallSignallingAddress_Type = TAddress
_RasRegistrationCallSignallingAddress_Object = MibTableColumn
rasRegistrationCallSignallingAddress = _RasRegistrationCallSignallingAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 2),
    _RasRegistrationCallSignallingAddress_Type()
)
rasRegistrationCallSignallingAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasRegistrationCallSignallingAddress.setStatus("current")
_RasRegistrationSrcRasAddressTag_Type = MmTAddressTag
_RasRegistrationSrcRasAddressTag_Object = MibTableColumn
rasRegistrationSrcRasAddressTag = _RasRegistrationSrcRasAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 3),
    _RasRegistrationSrcRasAddressTag_Type()
)
rasRegistrationSrcRasAddressTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasRegistrationSrcRasAddressTag.setStatus("current")
_RasRegistrationSrcRasAddress_Type = TAddress
_RasRegistrationSrcRasAddress_Object = MibTableColumn
rasRegistrationSrcRasAddress = _RasRegistrationSrcRasAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 4),
    _RasRegistrationSrcRasAddress_Type()
)
rasRegistrationSrcRasAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasRegistrationSrcRasAddress.setStatus("current")
_RasRegistrationIsGatekeeper_Type = TruthValue
_RasRegistrationIsGatekeeper_Object = MibTableColumn
rasRegistrationIsGatekeeper = _RasRegistrationIsGatekeeper_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 5),
    _RasRegistrationIsGatekeeper_Type()
)
rasRegistrationIsGatekeeper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationIsGatekeeper.setStatus("current")
_RasRegistrationGatekeeperId_Type = MmGatekeeperID
_RasRegistrationGatekeeperId_Object = MibTableColumn
rasRegistrationGatekeeperId = _RasRegistrationGatekeeperId_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 6),
    _RasRegistrationGatekeeperId_Type()
)
rasRegistrationGatekeeperId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationGatekeeperId.setStatus("current")
_RasRegistrationEndpointId_Type = MmEndpointID
_RasRegistrationEndpointId_Object = MibTableColumn
rasRegistrationEndpointId = _RasRegistrationEndpointId_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 7),
    _RasRegistrationEndpointId_Type()
)
rasRegistrationEndpointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationEndpointId.setStatus("current")
_RasRegistrationEncryption_Type = TruthValue
_RasRegistrationEncryption_Object = MibTableColumn
rasRegistrationEncryption = _RasRegistrationEncryption_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 8),
    _RasRegistrationEncryption_Type()
)
rasRegistrationEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationEncryption.setStatus("current")
_RasRegistrationWillSupplyUUIE_Type = TruthValue
_RasRegistrationWillSupplyUUIE_Object = MibTableColumn
rasRegistrationWillSupplyUUIE = _RasRegistrationWillSupplyUUIE_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 9),
    _RasRegistrationWillSupplyUUIE_Type()
)
rasRegistrationWillSupplyUUIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationWillSupplyUUIE.setStatus("current")
_RasRegistrationIntegrityCheckValue_Type = TruthValue
_RasRegistrationIntegrityCheckValue_Object = MibTableColumn
rasRegistrationIntegrityCheckValue = _RasRegistrationIntegrityCheckValue_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 10),
    _RasRegistrationIntegrityCheckValue_Type()
)
rasRegistrationIntegrityCheckValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationIntegrityCheckValue.setStatus("current")
_RasRegistrationTableNumberOfAliases_Type = Integer32
_RasRegistrationTableNumberOfAliases_Object = MibTableColumn
rasRegistrationTableNumberOfAliases = _RasRegistrationTableNumberOfAliases_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 11),
    _RasRegistrationTableNumberOfAliases_Type()
)
rasRegistrationTableNumberOfAliases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationTableNumberOfAliases.setStatus("current")
_RasRegistrationTableRowStatus_Type = RowStatus
_RasRegistrationTableRowStatus_Object = MibTableColumn
rasRegistrationTableRowStatus = _RasRegistrationTableRowStatus_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 12),
    _RasRegistrationTableRowStatus_Type()
)
rasRegistrationTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rasRegistrationTableRowStatus.setStatus("current")
_RasRegistrationEndpointType_Type = Integer32
_RasRegistrationEndpointType_Object = MibTableColumn
rasRegistrationEndpointType = _RasRegistrationEndpointType_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 13),
    _RasRegistrationEndpointType_Type()
)
rasRegistrationEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationEndpointType.setStatus("current")
_RasRegistrationPregrantedARQ_Type = TruthValue
_RasRegistrationPregrantedARQ_Object = MibTableColumn
rasRegistrationPregrantedARQ = _RasRegistrationPregrantedARQ_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 14),
    _RasRegistrationPregrantedARQ_Type()
)
rasRegistrationPregrantedARQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationPregrantedARQ.setStatus("current")
_RasRegistrationIsregisteredByRRQ_Type = TruthValue
_RasRegistrationIsregisteredByRRQ_Object = MibTableColumn
rasRegistrationIsregisteredByRRQ = _RasRegistrationIsregisteredByRRQ_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 1, 1, 15),
    _RasRegistrationIsregisteredByRRQ_Type()
)
rasRegistrationIsregisteredByRRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationIsregisteredByRRQ.setStatus("current")
_RasRegistrationAliasTable_Object = MibTable
rasRegistrationAliasTable = _RasRegistrationAliasTable_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rasRegistrationAliasTable.setStatus("current")
_RasRegistrationAliasTableEntry_Object = MibTableRow
rasRegistrationAliasTableEntry = _RasRegistrationAliasTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 2, 1)
)
rasRegistrationAliasTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAS-MIB", "rasRegistrationCallSignallingAddressTag"),
    (0, "RAS-MIB", "rasRegistrationCallSignallingAddress"),
    (0, "RAS-MIB", "rasRegistrationAliasTableIndex"),
)
if mibBuilder.loadTexts:
    rasRegistrationAliasTableEntry.setStatus("current")
_RasRegistrationAliasTableIndex_Type = Integer32
_RasRegistrationAliasTableIndex_Object = MibTableColumn
rasRegistrationAliasTableIndex = _RasRegistrationAliasTableIndex_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 2, 1, 1),
    _RasRegistrationAliasTableIndex_Type()
)
rasRegistrationAliasTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasRegistrationAliasTableIndex.setStatus("current")
_RasRegistrationAliasTag_Type = MmAliasTag
_RasRegistrationAliasTag_Object = MibTableColumn
rasRegistrationAliasTag = _RasRegistrationAliasTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 2, 1, 2),
    _RasRegistrationAliasTag_Type()
)
rasRegistrationAliasTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationAliasTag.setStatus("current")
_RasRegistrationAlias_Type = MmAliasAddress
_RasRegistrationAlias_Object = MibTableColumn
rasRegistrationAlias = _RasRegistrationAlias_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 2, 1, 3),
    _RasRegistrationAlias_Type()
)
rasRegistrationAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationAlias.setStatus("current")
_RasRegistrationRasAddressTable_Object = MibTable
rasRegistrationRasAddressTable = _RasRegistrationRasAddressTable_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    rasRegistrationRasAddressTable.setStatus("current")
_RasRegistrationRasAddressTableEntry_Object = MibTableRow
rasRegistrationRasAddressTableEntry = _RasRegistrationRasAddressTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 3, 1)
)
rasRegistrationRasAddressTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAS-MIB", "rasRegistrationCallSignallingAddressTag"),
    (0, "RAS-MIB", "rasRegistrationCallSignallingAddress"),
    (0, "RAS-MIB", "rasRegistrationRasAddressTableIndex"),
)
if mibBuilder.loadTexts:
    rasRegistrationRasAddressTableEntry.setStatus("current")
_RasRegistrationRasAddressTableIndex_Type = Integer32
_RasRegistrationRasAddressTableIndex_Object = MibTableColumn
rasRegistrationRasAddressTableIndex = _RasRegistrationRasAddressTableIndex_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 3, 1, 1),
    _RasRegistrationRasAddressTableIndex_Type()
)
rasRegistrationRasAddressTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasRegistrationRasAddressTableIndex.setStatus("current")
_RasRegistrationAdditionalSrcRasAddressTag_Type = MmTAddressTag
_RasRegistrationAdditionalSrcRasAddressTag_Object = MibTableColumn
rasRegistrationAdditionalSrcRasAddressTag = _RasRegistrationAdditionalSrcRasAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 3, 1, 2),
    _RasRegistrationAdditionalSrcRasAddressTag_Type()
)
rasRegistrationAdditionalSrcRasAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationAdditionalSrcRasAddressTag.setStatus("current")
_RasRegistrationAdditionalSrcRasAddress_Type = TAddress
_RasRegistrationAdditionalSrcRasAddress_Object = MibTableColumn
rasRegistrationAdditionalSrcRasAddress = _RasRegistrationAdditionalSrcRasAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 3, 1, 3),
    _RasRegistrationAdditionalSrcRasAddress_Type()
)
rasRegistrationAdditionalSrcRasAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationAdditionalSrcRasAddress.setStatus("current")
_RasRegistrationCallSignalingAddressTable_Object = MibTable
rasRegistrationCallSignalingAddressTable = _RasRegistrationCallSignalingAddressTable_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    rasRegistrationCallSignalingAddressTable.setStatus("current")
_RasRegistrationCallSignalingAddressTableEntry_Object = MibTableRow
rasRegistrationCallSignalingAddressTableEntry = _RasRegistrationCallSignalingAddressTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 4, 1)
)
rasRegistrationCallSignalingAddressTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAS-MIB", "rasRegistrationCallSignallingAddressTag"),
    (0, "RAS-MIB", "rasRegistrationCallSignallingAddress"),
    (0, "RAS-MIB", "rasRegistrationCallSignalingAddressTableIndex"),
)
if mibBuilder.loadTexts:
    rasRegistrationCallSignalingAddressTableEntry.setStatus("current")
_RasRegistrationCallSignalingAddressTableIndex_Type = Integer32
_RasRegistrationCallSignalingAddressTableIndex_Object = MibTableColumn
rasRegistrationCallSignalingAddressTableIndex = _RasRegistrationCallSignalingAddressTableIndex_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 4, 1, 1),
    _RasRegistrationCallSignalingAddressTableIndex_Type()
)
rasRegistrationCallSignalingAddressTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasRegistrationCallSignalingAddressTableIndex.setStatus("current")
_RasRegistrationAdditionalCallSignalingAddressTag_Type = MmTAddressTag
_RasRegistrationAdditionalCallSignalingAddressTag_Object = MibTableColumn
rasRegistrationAdditionalCallSignalingAddressTag = _RasRegistrationAdditionalCallSignalingAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 4, 1, 2),
    _RasRegistrationAdditionalCallSignalingAddressTag_Type()
)
rasRegistrationAdditionalCallSignalingAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationAdditionalCallSignalingAddressTag.setStatus("current")
_RasRegistrationAdditionalCallSignalingAddress_Type = TAddress
_RasRegistrationAdditionalCallSignalingAddress_Object = MibTableColumn
rasRegistrationAdditionalCallSignalingAddress = _RasRegistrationAdditionalCallSignalingAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 2, 4, 1, 3),
    _RasRegistrationAdditionalCallSignalingAddress_Type()
)
rasRegistrationAdditionalCallSignalingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasRegistrationAdditionalCallSignalingAddress.setStatus("current")
_RasAdmission_ObjectIdentity = ObjectIdentity
rasAdmission = _RasAdmission_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 2, 3)
)
_RasAdmissionTable_Object = MibTable
rasAdmissionTable = _RasAdmissionTable_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rasAdmissionTable.setStatus("current")
_RasAdmissionTableEntry_Object = MibTableRow
rasAdmissionTableEntry = _RasAdmissionTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1)
)
rasAdmissionTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAS-MIB", "rasAdmissionSrcCallSignallingAddress"),
    (0, "RAS-MIB", "rasAdmissionRasAddress"),
    (0, "RAS-MIB", "rasAdmissionCallIdentifier"),
)
if mibBuilder.loadTexts:
    rasAdmissionTableEntry.setStatus("current")
_RasAdmissionSrcCallSignallingAddressTag_Type = MmTAddressTag
_RasAdmissionSrcCallSignallingAddressTag_Object = MibTableColumn
rasAdmissionSrcCallSignallingAddressTag = _RasAdmissionSrcCallSignallingAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 1),
    _RasAdmissionSrcCallSignallingAddressTag_Type()
)
rasAdmissionSrcCallSignallingAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionSrcCallSignallingAddressTag.setStatus("current")
_RasAdmissionSrcCallSignallingAddress_Type = TAddress
_RasAdmissionSrcCallSignallingAddress_Object = MibTableColumn
rasAdmissionSrcCallSignallingAddress = _RasAdmissionSrcCallSignallingAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 2),
    _RasAdmissionSrcCallSignallingAddress_Type()
)
rasAdmissionSrcCallSignallingAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasAdmissionSrcCallSignallingAddress.setStatus("current")
_RasAdmissionDestCallSignallingAddressTag_Type = MmTAddressTag
_RasAdmissionDestCallSignallingAddressTag_Object = MibTableColumn
rasAdmissionDestCallSignallingAddressTag = _RasAdmissionDestCallSignallingAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 3),
    _RasAdmissionDestCallSignallingAddressTag_Type()
)
rasAdmissionDestCallSignallingAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionDestCallSignallingAddressTag.setStatus("current")
_RasAdmissionDestCallSignallingAddress_Type = TAddress
_RasAdmissionDestCallSignallingAddress_Object = MibTableColumn
rasAdmissionDestCallSignallingAddress = _RasAdmissionDestCallSignallingAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 4),
    _RasAdmissionDestCallSignallingAddress_Type()
)
rasAdmissionDestCallSignallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionDestCallSignallingAddress.setStatus("current")
_RasAdmissionCallIdentifier_Type = MmGlobalIdentifier
_RasAdmissionCallIdentifier_Object = MibTableColumn
rasAdmissionCallIdentifier = _RasAdmissionCallIdentifier_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 5),
    _RasAdmissionCallIdentifier_Type()
)
rasAdmissionCallIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasAdmissionCallIdentifier.setStatus("current")
_RasAdmissionConferenceId_Type = MmGlobalIdentifier
_RasAdmissionConferenceId_Object = MibTableColumn
rasAdmissionConferenceId = _RasAdmissionConferenceId_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 6),
    _RasAdmissionConferenceId_Type()
)
rasAdmissionConferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionConferenceId.setStatus("current")
_RasAdmissionRasAddressTag_Type = MmTAddressTag
_RasAdmissionRasAddressTag_Object = MibTableColumn
rasAdmissionRasAddressTag = _RasAdmissionRasAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 7),
    _RasAdmissionRasAddressTag_Type()
)
rasAdmissionRasAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionRasAddressTag.setStatus("current")
_RasAdmissionRasAddress_Type = TAddress
_RasAdmissionRasAddress_Object = MibTableColumn
rasAdmissionRasAddress = _RasAdmissionRasAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 8),
    _RasAdmissionRasAddress_Type()
)
rasAdmissionRasAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rasAdmissionRasAddress.setStatus("current")
_RasAdmissionCRV_Type = MmH225Crv
_RasAdmissionCRV_Object = MibTableColumn
rasAdmissionCRV = _RasAdmissionCRV_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 9),
    _RasAdmissionCRV_Type()
)
rasAdmissionCRV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionCRV.setStatus("current")
_RasAdmissionIsGatekeeper_Type = TruthValue
_RasAdmissionIsGatekeeper_Object = MibTableColumn
rasAdmissionIsGatekeeper = _RasAdmissionIsGatekeeper_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 10),
    _RasAdmissionIsGatekeeper_Type()
)
rasAdmissionIsGatekeeper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionIsGatekeeper.setStatus("current")
_RasAdmissionSrcAliasAddressTag_Type = MmAliasTag
_RasAdmissionSrcAliasAddressTag_Object = MibTableColumn
rasAdmissionSrcAliasAddressTag = _RasAdmissionSrcAliasAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 11),
    _RasAdmissionSrcAliasAddressTag_Type()
)
rasAdmissionSrcAliasAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionSrcAliasAddressTag.setStatus("current")
_RasAdmissionSrcAliasAddress_Type = MmAliasAddress
_RasAdmissionSrcAliasAddress_Object = MibTableColumn
rasAdmissionSrcAliasAddress = _RasAdmissionSrcAliasAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 12),
    _RasAdmissionSrcAliasAddress_Type()
)
rasAdmissionSrcAliasAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionSrcAliasAddress.setStatus("current")
_RasAdmissionDestAliasAddressTag_Type = MmAliasTag
_RasAdmissionDestAliasAddressTag_Object = MibTableColumn
rasAdmissionDestAliasAddressTag = _RasAdmissionDestAliasAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 13),
    _RasAdmissionDestAliasAddressTag_Type()
)
rasAdmissionDestAliasAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionDestAliasAddressTag.setStatus("current")
_RasAdmissionDestAliasAddress_Type = MmAliasAddress
_RasAdmissionDestAliasAddress_Object = MibTableColumn
rasAdmissionDestAliasAddress = _RasAdmissionDestAliasAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 14),
    _RasAdmissionDestAliasAddress_Type()
)
rasAdmissionDestAliasAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionDestAliasAddress.setStatus("current")


class _RasAdmissionAnswerCallIndicator_Type(Integer32):
    """Custom type rasAdmissionAnswerCallIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callee", 2),
          ("caller", 1))
    )


_RasAdmissionAnswerCallIndicator_Type.__name__ = "Integer32"
_RasAdmissionAnswerCallIndicator_Object = MibTableColumn
rasAdmissionAnswerCallIndicator = _RasAdmissionAnswerCallIndicator_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 15),
    _RasAdmissionAnswerCallIndicator_Type()
)
rasAdmissionAnswerCallIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionAnswerCallIndicator.setStatus("current")
_RasAdmissionTime_Type = DateAndTime
_RasAdmissionTime_Object = MibTableColumn
rasAdmissionTime = _RasAdmissionTime_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 16),
    _RasAdmissionTime_Type()
)
rasAdmissionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionTime.setStatus("current")
_RasAdmissionEndpointId_Type = MmEndpointID
_RasAdmissionEndpointId_Object = MibTableColumn
rasAdmissionEndpointId = _RasAdmissionEndpointId_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 17),
    _RasAdmissionEndpointId_Type()
)
rasAdmissionEndpointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionEndpointId.setStatus("current")
_RasAdmissionBandwidth_Type = Integer32
_RasAdmissionBandwidth_Object = MibTableColumn
rasAdmissionBandwidth = _RasAdmissionBandwidth_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 18),
    _RasAdmissionBandwidth_Type()
)
rasAdmissionBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionBandwidth.setStatus("current")
_RasAdmissionIRRFrequency_Type = Integer32
_RasAdmissionIRRFrequency_Object = MibTableColumn
rasAdmissionIRRFrequency = _RasAdmissionIRRFrequency_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 19),
    _RasAdmissionIRRFrequency_Type()
)
rasAdmissionIRRFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionIRRFrequency.setStatus("current")
_RasAdmissionCallType_Type = MmCallType
_RasAdmissionCallType_Object = MibTableColumn
rasAdmissionCallType = _RasAdmissionCallType_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 20),
    _RasAdmissionCallType_Type()
)
rasAdmissionCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionCallType.setStatus("current")


class _RasAdmissionCallModel_Type(Integer32):
    """Custom type rasAdmissionCallModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("gatekeeperRouted", 2))
    )


_RasAdmissionCallModel_Type.__name__ = "Integer32"
_RasAdmissionCallModel_Object = MibTableColumn
rasAdmissionCallModel = _RasAdmissionCallModel_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 21),
    _RasAdmissionCallModel_Type()
)
rasAdmissionCallModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionCallModel.setStatus("current")
_RasAdmissionSrcHandlesBandwidth_Type = TruthValue
_RasAdmissionSrcHandlesBandwidth_Object = MibTableColumn
rasAdmissionSrcHandlesBandwidth = _RasAdmissionSrcHandlesBandwidth_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 22),
    _RasAdmissionSrcHandlesBandwidth_Type()
)
rasAdmissionSrcHandlesBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionSrcHandlesBandwidth.setStatus("current")
_RasAdmissionDestHandlesBandwidth_Type = TruthValue
_RasAdmissionDestHandlesBandwidth_Object = MibTableColumn
rasAdmissionDestHandlesBandwidth = _RasAdmissionDestHandlesBandwidth_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 23),
    _RasAdmissionDestHandlesBandwidth_Type()
)
rasAdmissionDestHandlesBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionDestHandlesBandwidth.setStatus("current")
_RasAdmissionSecurity_Type = TruthValue
_RasAdmissionSecurity_Object = MibTableColumn
rasAdmissionSecurity = _RasAdmissionSecurity_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 24),
    _RasAdmissionSecurity_Type()
)
rasAdmissionSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionSecurity.setStatus("current")
_RasAdmissionSrcWillSupplyUUIE_Type = TruthValue
_RasAdmissionSrcWillSupplyUUIE_Object = MibTableColumn
rasAdmissionSrcWillSupplyUUIE = _RasAdmissionSrcWillSupplyUUIE_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 25),
    _RasAdmissionSrcWillSupplyUUIE_Type()
)
rasAdmissionSrcWillSupplyUUIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionSrcWillSupplyUUIE.setStatus("current")
_RasAdmissionDestWillSupplyUUIE_Type = TruthValue
_RasAdmissionDestWillSupplyUUIE_Object = MibTableColumn
rasAdmissionDestWillSupplyUUIE = _RasAdmissionDestWillSupplyUUIE_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 26),
    _RasAdmissionDestWillSupplyUUIE_Type()
)
rasAdmissionDestWillSupplyUUIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasAdmissionDestWillSupplyUUIE.setStatus("current")
_RasAdmissionTableRowStatus_Type = RowStatus
_RasAdmissionTableRowStatus_Object = MibTableColumn
rasAdmissionTableRowStatus = _RasAdmissionTableRowStatus_Object(
    (0, 0, 8, 341, 1, 1, 2, 3, 1, 1, 27),
    _RasAdmissionTableRowStatus_Type()
)
rasAdmissionTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rasAdmissionTableRowStatus.setStatus("current")
_RasStats_ObjectIdentity = ObjectIdentity
rasStats = _RasStats_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 2, 4)
)
_RasStatsTable_Object = MibTable
rasStatsTable = _RasStatsTable_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    rasStatsTable.setStatus("current")
_RasStatsTableEntry_Object = MibTableRow
rasStatsTableEntry = _RasStatsTableEntry_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1)
)
rasStatsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rasStatsTableEntry.setStatus("current")
_RasStatsGatekeeperConfirms_Type = Counter32
_RasStatsGatekeeperConfirms_Object = MibTableColumn
rasStatsGatekeeperConfirms = _RasStatsGatekeeperConfirms_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 1),
    _RasStatsGatekeeperConfirms_Type()
)
rasStatsGatekeeperConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsGatekeeperConfirms.setStatus("current")
_RasStatsGatekeeperRejects_Type = Counter32
_RasStatsGatekeeperRejects_Object = MibTableColumn
rasStatsGatekeeperRejects = _RasStatsGatekeeperRejects_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 2),
    _RasStatsGatekeeperRejects_Type()
)
rasStatsGatekeeperRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsGatekeeperRejects.setStatus("current")
_RasStatsRegistrationConfirms_Type = Counter32
_RasStatsRegistrationConfirms_Object = MibTableColumn
rasStatsRegistrationConfirms = _RasStatsRegistrationConfirms_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 3),
    _RasStatsRegistrationConfirms_Type()
)
rasStatsRegistrationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsRegistrationConfirms.setStatus("current")
_RasStatsRegistrationRejects_Type = Counter32
_RasStatsRegistrationRejects_Object = MibTableColumn
rasStatsRegistrationRejects = _RasStatsRegistrationRejects_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 4),
    _RasStatsRegistrationRejects_Type()
)
rasStatsRegistrationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsRegistrationRejects.setStatus("current")
_RasStatsUnregistrationConfirms_Type = Counter32
_RasStatsUnregistrationConfirms_Object = MibTableColumn
rasStatsUnregistrationConfirms = _RasStatsUnregistrationConfirms_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 5),
    _RasStatsUnregistrationConfirms_Type()
)
rasStatsUnregistrationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsUnregistrationConfirms.setStatus("current")
_RasStatsUnregistrationRejects_Type = Counter32
_RasStatsUnregistrationRejects_Object = MibTableColumn
rasStatsUnregistrationRejects = _RasStatsUnregistrationRejects_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 6),
    _RasStatsUnregistrationRejects_Type()
)
rasStatsUnregistrationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsUnregistrationRejects.setStatus("current")
_RasStatsAdmissionConfirms_Type = Counter32
_RasStatsAdmissionConfirms_Object = MibTableColumn
rasStatsAdmissionConfirms = _RasStatsAdmissionConfirms_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 7),
    _RasStatsAdmissionConfirms_Type()
)
rasStatsAdmissionConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsAdmissionConfirms.setStatus("current")
_RasStatsAdmissionRejects_Type = Counter32
_RasStatsAdmissionRejects_Object = MibTableColumn
rasStatsAdmissionRejects = _RasStatsAdmissionRejects_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 8),
    _RasStatsAdmissionRejects_Type()
)
rasStatsAdmissionRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsAdmissionRejects.setStatus("current")
_RasStatsBandwidthConfirms_Type = Counter32
_RasStatsBandwidthConfirms_Object = MibTableColumn
rasStatsBandwidthConfirms = _RasStatsBandwidthConfirms_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 9),
    _RasStatsBandwidthConfirms_Type()
)
rasStatsBandwidthConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsBandwidthConfirms.setStatus("current")
_RasStatsBandwidthRejects_Type = Counter32
_RasStatsBandwidthRejects_Object = MibTableColumn
rasStatsBandwidthRejects = _RasStatsBandwidthRejects_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 10),
    _RasStatsBandwidthRejects_Type()
)
rasStatsBandwidthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsBandwidthRejects.setStatus("current")
_RasStatsDisengageConfirms_Type = Counter32
_RasStatsDisengageConfirms_Object = MibTableColumn
rasStatsDisengageConfirms = _RasStatsDisengageConfirms_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 11),
    _RasStatsDisengageConfirms_Type()
)
rasStatsDisengageConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsDisengageConfirms.setStatus("current")
_RasStatsDisengageRejects_Type = Counter32
_RasStatsDisengageRejects_Object = MibTableColumn
rasStatsDisengageRejects = _RasStatsDisengageRejects_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 12),
    _RasStatsDisengageRejects_Type()
)
rasStatsDisengageRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsDisengageRejects.setStatus("current")
_RasStatsLocationConfirms_Type = Counter32
_RasStatsLocationConfirms_Object = MibTableColumn
rasStatsLocationConfirms = _RasStatsLocationConfirms_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 13),
    _RasStatsLocationConfirms_Type()
)
rasStatsLocationConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsLocationConfirms.setStatus("current")
_RasStatsLocationRejects_Type = Counter32
_RasStatsLocationRejects_Object = MibTableColumn
rasStatsLocationRejects = _RasStatsLocationRejects_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 14),
    _RasStatsLocationRejects_Type()
)
rasStatsLocationRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsLocationRejects.setStatus("current")
_RasStatsInfoRequests_Type = Counter32
_RasStatsInfoRequests_Object = MibTableColumn
rasStatsInfoRequests = _RasStatsInfoRequests_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 15),
    _RasStatsInfoRequests_Type()
)
rasStatsInfoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsInfoRequests.setStatus("current")
_RasStatsInfoRequestResponses_Type = Counter32
_RasStatsInfoRequestResponses_Object = MibTableColumn
rasStatsInfoRequestResponses = _RasStatsInfoRequestResponses_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 16),
    _RasStatsInfoRequestResponses_Type()
)
rasStatsInfoRequestResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsInfoRequestResponses.setStatus("current")
_RasStatsnonStandardMessages_Type = Counter32
_RasStatsnonStandardMessages_Object = MibTableColumn
rasStatsnonStandardMessages = _RasStatsnonStandardMessages_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 17),
    _RasStatsnonStandardMessages_Type()
)
rasStatsnonStandardMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsnonStandardMessages.setStatus("current")
_RasStatsUnknownMessages_Type = Counter32
_RasStatsUnknownMessages_Object = MibTableColumn
rasStatsUnknownMessages = _RasStatsUnknownMessages_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 18),
    _RasStatsUnknownMessages_Type()
)
rasStatsUnknownMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsUnknownMessages.setStatus("current")
_RasStatsRequestInProgress_Type = Counter32
_RasStatsRequestInProgress_Object = MibTableColumn
rasStatsRequestInProgress = _RasStatsRequestInProgress_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 19),
    _RasStatsRequestInProgress_Type()
)
rasStatsRequestInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsRequestInProgress.setStatus("current")
_RasStatsResourceAvailabilityIndicator_Type = Counter32
_RasStatsResourceAvailabilityIndicator_Object = MibTableColumn
rasStatsResourceAvailabilityIndicator = _RasStatsResourceAvailabilityIndicator_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 20),
    _RasStatsResourceAvailabilityIndicator_Type()
)
rasStatsResourceAvailabilityIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsResourceAvailabilityIndicator.setStatus("current")
_RasStatsResourceAvailabilityConfirm_Type = Counter32
_RasStatsResourceAvailabilityConfirm_Object = MibTableColumn
rasStatsResourceAvailabilityConfirm = _RasStatsResourceAvailabilityConfirm_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 21),
    _RasStatsResourceAvailabilityConfirm_Type()
)
rasStatsResourceAvailabilityConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsResourceAvailabilityConfirm.setStatus("current")
_RasStatsRegisteredEndpointsNo_Type = Counter32
_RasStatsRegisteredEndpointsNo_Object = MibTableColumn
rasStatsRegisteredEndpointsNo = _RasStatsRegisteredEndpointsNo_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 22),
    _RasStatsRegisteredEndpointsNo_Type()
)
rasStatsRegisteredEndpointsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsRegisteredEndpointsNo.setStatus("current")
_RasStatsAdmittedEndpointsNo_Type = Counter32
_RasStatsAdmittedEndpointsNo_Object = MibTableColumn
rasStatsAdmittedEndpointsNo = _RasStatsAdmittedEndpointsNo_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 23),
    _RasStatsAdmittedEndpointsNo_Type()
)
rasStatsAdmittedEndpointsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsAdmittedEndpointsNo.setStatus("current")
_RasStatsINAKs_Type = Counter32
_RasStatsINAKs_Object = MibTableColumn
rasStatsINAKs = _RasStatsINAKs_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 24),
    _RasStatsINAKs_Type()
)
rasStatsINAKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsINAKs.setStatus("current")
_RasStatsIACKs_Type = Counter32
_RasStatsIACKs_Object = MibTableColumn
rasStatsIACKs = _RasStatsIACKs_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 25),
    _RasStatsIACKs_Type()
)
rasStatsIACKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsIACKs.setStatus("current")
_RasStatsGkRoutedCalls_Type = Counter32
_RasStatsGkRoutedCalls_Object = MibTableColumn
rasStatsGkRoutedCalls = _RasStatsGkRoutedCalls_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 26),
    _RasStatsGkRoutedCalls_Type()
)
rasStatsGkRoutedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsGkRoutedCalls.setStatus("current")
_RasStatsResourceAvailabilityIndications_Type = Counter32
_RasStatsResourceAvailabilityIndications_Object = MibTableColumn
rasStatsResourceAvailabilityIndications = _RasStatsResourceAvailabilityIndications_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 27),
    _RasStatsResourceAvailabilityIndications_Type()
)
rasStatsResourceAvailabilityIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsResourceAvailabilityIndications.setStatus("current")
_RasStatsResourceAvailabilityConfirmations_Type = Counter32
_RasStatsResourceAvailabilityConfirmations_Object = MibTableColumn
rasStatsResourceAvailabilityConfirmations = _RasStatsResourceAvailabilityConfirmations_Object(
    (0, 0, 8, 341, 1, 1, 2, 4, 1, 1, 28),
    _RasStatsResourceAvailabilityConfirmations_Type()
)
rasStatsResourceAvailabilityConfirmations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rasStatsResourceAvailabilityConfirmations.setStatus("current")
_RasEvents_ObjectIdentity = ObjectIdentity
rasEvents = _RasEvents_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 2, 5, 0)
)


class _LastArjReason_Type(Integer32):
    """Custom type lastArjReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("calledPartyNotRegistered", 1),
          ("callerNotRegistered", 5),
          ("incompleteAddress", 11),
          ("invalidEndpointIdentifier", 7),
          ("invalidPermission", 2),
          ("qosControlNotSupported", 10),
          ("requestDenied", 3),
          ("resourceUnavailable", 8),
          ("routeCallToGatekeeper", 6),
          ("securityDenial", 9),
          ("undefinedReason", 4))
    )


_LastArjReason_Type.__name__ = "Integer32"
_LastArjReason_Object = MibScalar
lastArjReason = _LastArjReason_Object(
    (0, 0, 8, 341, 1, 1, 2, 5, 0, 1),
    _LastArjReason_Type()
)
lastArjReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastArjReason.setStatus("current")
_LastArjRasAddressTag_Type = MmTAddressTag
_LastArjRasAddressTag_Object = MibScalar
lastArjRasAddressTag = _LastArjRasAddressTag_Object(
    (0, 0, 8, 341, 1, 1, 2, 5, 0, 2),
    _LastArjRasAddressTag_Type()
)
lastArjRasAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastArjRasAddressTag.setStatus("current")
_LastArjRasAddress_Type = TAddress
_LastArjRasAddress_Object = MibScalar
lastArjRasAddress = _LastArjRasAddress_Object(
    (0, 0, 8, 341, 1, 1, 2, 5, 0, 3),
    _LastArjRasAddress_Type()
)
lastArjRasAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastArjRasAddress.setStatus("current")
_RasMIBConformance_ObjectIdentity = ObjectIdentity
rasMIBConformance = _RasMIBConformance_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 2, 6)
)
_RasMIBGroups_ObjectIdentity = ObjectIdentity
rasMIBGroups = _RasMIBGroups_ObjectIdentity(
    (0, 0, 8, 341, 1, 1, 2, 6, 1)
)

# Managed Objects groups

rasConfigurationGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 2, 6, 1, 1)
)
rasConfigurationGroup.setObjects(
      *(("RAS-MIB", "rasConfigurationTimer"),
        ("RAS-MIB", "rasConfigurationMaxNumberOfRetries"))
)
if mibBuilder.loadTexts:
    rasConfigurationGroup.setStatus("current")

rasRegistrationGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 2, 6, 1, 2)
)
rasRegistrationGroup.setObjects(
      *(("RAS-MIB", "rasRegistrationIsGatekeeper"),
        ("RAS-MIB", "rasRegistrationGatekeeperId"),
        ("RAS-MIB", "rasRegistrationEndpointId"),
        ("RAS-MIB", "rasRegistrationEncryption"),
        ("RAS-MIB", "rasRegistrationWillSupplyUUIE"),
        ("RAS-MIB", "rasRegistrationIntegrityCheckValue"),
        ("RAS-MIB", "rasRegistrationTableNumberOfAliases"),
        ("RAS-MIB", "rasRegistrationEndpointType"),
        ("RAS-MIB", "rasRegistrationPregrantedARQ"),
        ("RAS-MIB", "rasRegistrationAlias"))
)
if mibBuilder.loadTexts:
    rasRegistrationGroup.setStatus("current")

rasAdmissionGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 2, 6, 1, 3)
)
rasAdmissionGroup.setObjects(
      *(("RAS-MIB", "rasAdmissionConferenceId"),
        ("RAS-MIB", "rasAdmissionRasAddressTag"),
        ("RAS-MIB", "rasAdmissionCRV"),
        ("RAS-MIB", "rasAdmissionIsGatekeeper"),
        ("RAS-MIB", "rasAdmissionSrcCallSignallingAddressTag"),
        ("RAS-MIB", "rasAdmissionDestCallSignallingAddressTag"),
        ("RAS-MIB", "rasAdmissionDestCallSignallingAddress"),
        ("RAS-MIB", "rasAdmissionSrcAliasAddressTag"),
        ("RAS-MIB", "rasAdmissionSrcAliasAddress"),
        ("RAS-MIB", "rasAdmissionDestAliasAddressTag"),
        ("RAS-MIB", "rasAdmissionDestAliasAddress"),
        ("RAS-MIB", "rasAdmissionAnswerCallIndicator"),
        ("RAS-MIB", "rasAdmissionTime"),
        ("RAS-MIB", "rasAdmissionEndpointId"),
        ("RAS-MIB", "rasAdmissionBandwidth"),
        ("RAS-MIB", "rasAdmissionIRRFrequency"),
        ("RAS-MIB", "rasAdmissionCallType"),
        ("RAS-MIB", "rasAdmissionCallModel"),
        ("RAS-MIB", "rasAdmissionSrcHandlesBandwidth"),
        ("RAS-MIB", "rasAdmissionDestHandlesBandwidth"),
        ("RAS-MIB", "rasAdmissionSecurity"),
        ("RAS-MIB", "rasAdmissionSrcWillSupplyUUIE"),
        ("RAS-MIB", "rasAdmissionDestWillSupplyUUIE"))
)
if mibBuilder.loadTexts:
    rasAdmissionGroup.setStatus("current")

rasStatsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 2, 6, 1, 4)
)
rasStatsGroup.setObjects(
      *(("RAS-MIB", "rasStatsGatekeeperConfirms"),
        ("RAS-MIB", "rasStatsGatekeeperRejects"),
        ("RAS-MIB", "rasStatsRegistrationConfirms"),
        ("RAS-MIB", "rasStatsRegistrationRejects"),
        ("RAS-MIB", "rasStatsUnregistrationConfirms"),
        ("RAS-MIB", "rasStatsUnregistrationRejects"),
        ("RAS-MIB", "rasStatsAdmissionConfirms"),
        ("RAS-MIB", "rasStatsAdmissionRejects"),
        ("RAS-MIB", "rasStatsBandwidthConfirms"),
        ("RAS-MIB", "rasStatsBandwidthRejects"),
        ("RAS-MIB", "rasStatsDisengageConfirms"),
        ("RAS-MIB", "rasStatsDisengageRejects"),
        ("RAS-MIB", "rasStatsLocationConfirms"),
        ("RAS-MIB", "rasStatsLocationRejects"),
        ("RAS-MIB", "rasStatsInfoRequests"),
        ("RAS-MIB", "rasStatsInfoRequestResponses"),
        ("RAS-MIB", "rasStatsnonStandardMessages"),
        ("RAS-MIB", "rasStatsUnknownMessages"),
        ("RAS-MIB", "rasStatsRequestInProgress"),
        ("RAS-MIB", "rasStatsResourceAvailabilityIndicator"),
        ("RAS-MIB", "rasStatsResourceAvailabilityConfirm"),
        ("RAS-MIB", "rasStatsRegisteredEndpointsNo"),
        ("RAS-MIB", "rasStatsAdmittedEndpointsNo"),
        ("RAS-MIB", "rasStatsINAKs"),
        ("RAS-MIB", "rasStatsIACKs"),
        ("RAS-MIB", "rasStatsGkRoutedCalls"),
        ("RAS-MIB", "rasStatsResourceAvailabilityIndications"),
        ("RAS-MIB", "rasStatsResourceAvailabilityConfirmations"))
)
if mibBuilder.loadTexts:
    rasStatsGroup.setStatus("current")

rasEventsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 1, 2, 6, 1, 5)
)
rasEventsGroup.setObjects(
      *(("RAS-MIB", "lastArjReason"),
        ("RAS-MIB", "lastArjRasAddressTag"),
        ("RAS-MIB", "lastArjRasAddress"))
)
if mibBuilder.loadTexts:
    rasEventsGroup.setStatus("current")


# Notification objects

admissionReject = NotificationType(
    (0, 0, 8, 341, 1, 1, 2, 5, 0, 4)
)
admissionReject.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RAS-MIB", "lastArjReason"),
        ("RAS-MIB", "lastArjRasAddressTag"),
        ("RAS-MIB", "lastArjRasAddress"))
)
if mibBuilder.loadTexts:
    admissionReject.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

rasMIBCompliance = ModuleCompliance(
    (0, 0, 8, 341, 1, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    rasMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAS-MIB",
    **{"ras": ras,
       "rasConfiguration": rasConfiguration,
       "rasConfigurationTable": rasConfigurationTable,
       "rasConfigurationTableEntry": rasConfigurationTableEntry,
       "rasConfigurationGatekeeperIdentifier": rasConfigurationGatekeeperIdentifier,
       "rasConfigurationTimer": rasConfigurationTimer,
       "rasConfigurationMaxNumberOfRetries": rasConfigurationMaxNumberOfRetries,
       "rasConfigurationGatekeeperDiscoveryAddressTag": rasConfigurationGatekeeperDiscoveryAddressTag,
       "rasConfigurationGatekeeperDiscoveryAddress": rasConfigurationGatekeeperDiscoveryAddress,
       "rasRegistration": rasRegistration,
       "rasRegistrationTable": rasRegistrationTable,
       "rasRegistrationTableEntry": rasRegistrationTableEntry,
       "rasRegistrationCallSignallingAddressTag": rasRegistrationCallSignallingAddressTag,
       "rasRegistrationCallSignallingAddress": rasRegistrationCallSignallingAddress,
       "rasRegistrationSrcRasAddressTag": rasRegistrationSrcRasAddressTag,
       "rasRegistrationSrcRasAddress": rasRegistrationSrcRasAddress,
       "rasRegistrationIsGatekeeper": rasRegistrationIsGatekeeper,
       "rasRegistrationGatekeeperId": rasRegistrationGatekeeperId,
       "rasRegistrationEndpointId": rasRegistrationEndpointId,
       "rasRegistrationEncryption": rasRegistrationEncryption,
       "rasRegistrationWillSupplyUUIE": rasRegistrationWillSupplyUUIE,
       "rasRegistrationIntegrityCheckValue": rasRegistrationIntegrityCheckValue,
       "rasRegistrationTableNumberOfAliases": rasRegistrationTableNumberOfAliases,
       "rasRegistrationTableRowStatus": rasRegistrationTableRowStatus,
       "rasRegistrationEndpointType": rasRegistrationEndpointType,
       "rasRegistrationPregrantedARQ": rasRegistrationPregrantedARQ,
       "rasRegistrationIsregisteredByRRQ": rasRegistrationIsregisteredByRRQ,
       "rasRegistrationAliasTable": rasRegistrationAliasTable,
       "rasRegistrationAliasTableEntry": rasRegistrationAliasTableEntry,
       "rasRegistrationAliasTableIndex": rasRegistrationAliasTableIndex,
       "rasRegistrationAliasTag": rasRegistrationAliasTag,
       "rasRegistrationAlias": rasRegistrationAlias,
       "rasRegistrationRasAddressTable": rasRegistrationRasAddressTable,
       "rasRegistrationRasAddressTableEntry": rasRegistrationRasAddressTableEntry,
       "rasRegistrationRasAddressTableIndex": rasRegistrationRasAddressTableIndex,
       "rasRegistrationAdditionalSrcRasAddressTag": rasRegistrationAdditionalSrcRasAddressTag,
       "rasRegistrationAdditionalSrcRasAddress": rasRegistrationAdditionalSrcRasAddress,
       "rasRegistrationCallSignalingAddressTable": rasRegistrationCallSignalingAddressTable,
       "rasRegistrationCallSignalingAddressTableEntry": rasRegistrationCallSignalingAddressTableEntry,
       "rasRegistrationCallSignalingAddressTableIndex": rasRegistrationCallSignalingAddressTableIndex,
       "rasRegistrationAdditionalCallSignalingAddressTag": rasRegistrationAdditionalCallSignalingAddressTag,
       "rasRegistrationAdditionalCallSignalingAddress": rasRegistrationAdditionalCallSignalingAddress,
       "rasAdmission": rasAdmission,
       "rasAdmissionTable": rasAdmissionTable,
       "rasAdmissionTableEntry": rasAdmissionTableEntry,
       "rasAdmissionSrcCallSignallingAddressTag": rasAdmissionSrcCallSignallingAddressTag,
       "rasAdmissionSrcCallSignallingAddress": rasAdmissionSrcCallSignallingAddress,
       "rasAdmissionDestCallSignallingAddressTag": rasAdmissionDestCallSignallingAddressTag,
       "rasAdmissionDestCallSignallingAddress": rasAdmissionDestCallSignallingAddress,
       "rasAdmissionCallIdentifier": rasAdmissionCallIdentifier,
       "rasAdmissionConferenceId": rasAdmissionConferenceId,
       "rasAdmissionRasAddressTag": rasAdmissionRasAddressTag,
       "rasAdmissionRasAddress": rasAdmissionRasAddress,
       "rasAdmissionCRV": rasAdmissionCRV,
       "rasAdmissionIsGatekeeper": rasAdmissionIsGatekeeper,
       "rasAdmissionSrcAliasAddressTag": rasAdmissionSrcAliasAddressTag,
       "rasAdmissionSrcAliasAddress": rasAdmissionSrcAliasAddress,
       "rasAdmissionDestAliasAddressTag": rasAdmissionDestAliasAddressTag,
       "rasAdmissionDestAliasAddress": rasAdmissionDestAliasAddress,
       "rasAdmissionAnswerCallIndicator": rasAdmissionAnswerCallIndicator,
       "rasAdmissionTime": rasAdmissionTime,
       "rasAdmissionEndpointId": rasAdmissionEndpointId,
       "rasAdmissionBandwidth": rasAdmissionBandwidth,
       "rasAdmissionIRRFrequency": rasAdmissionIRRFrequency,
       "rasAdmissionCallType": rasAdmissionCallType,
       "rasAdmissionCallModel": rasAdmissionCallModel,
       "rasAdmissionSrcHandlesBandwidth": rasAdmissionSrcHandlesBandwidth,
       "rasAdmissionDestHandlesBandwidth": rasAdmissionDestHandlesBandwidth,
       "rasAdmissionSecurity": rasAdmissionSecurity,
       "rasAdmissionSrcWillSupplyUUIE": rasAdmissionSrcWillSupplyUUIE,
       "rasAdmissionDestWillSupplyUUIE": rasAdmissionDestWillSupplyUUIE,
       "rasAdmissionTableRowStatus": rasAdmissionTableRowStatus,
       "rasStats": rasStats,
       "rasStatsTable": rasStatsTable,
       "rasStatsTableEntry": rasStatsTableEntry,
       "rasStatsGatekeeperConfirms": rasStatsGatekeeperConfirms,
       "rasStatsGatekeeperRejects": rasStatsGatekeeperRejects,
       "rasStatsRegistrationConfirms": rasStatsRegistrationConfirms,
       "rasStatsRegistrationRejects": rasStatsRegistrationRejects,
       "rasStatsUnregistrationConfirms": rasStatsUnregistrationConfirms,
       "rasStatsUnregistrationRejects": rasStatsUnregistrationRejects,
       "rasStatsAdmissionConfirms": rasStatsAdmissionConfirms,
       "rasStatsAdmissionRejects": rasStatsAdmissionRejects,
       "rasStatsBandwidthConfirms": rasStatsBandwidthConfirms,
       "rasStatsBandwidthRejects": rasStatsBandwidthRejects,
       "rasStatsDisengageConfirms": rasStatsDisengageConfirms,
       "rasStatsDisengageRejects": rasStatsDisengageRejects,
       "rasStatsLocationConfirms": rasStatsLocationConfirms,
       "rasStatsLocationRejects": rasStatsLocationRejects,
       "rasStatsInfoRequests": rasStatsInfoRequests,
       "rasStatsInfoRequestResponses": rasStatsInfoRequestResponses,
       "rasStatsnonStandardMessages": rasStatsnonStandardMessages,
       "rasStatsUnknownMessages": rasStatsUnknownMessages,
       "rasStatsRequestInProgress": rasStatsRequestInProgress,
       "rasStatsResourceAvailabilityIndicator": rasStatsResourceAvailabilityIndicator,
       "rasStatsResourceAvailabilityConfirm": rasStatsResourceAvailabilityConfirm,
       "rasStatsRegisteredEndpointsNo": rasStatsRegisteredEndpointsNo,
       "rasStatsAdmittedEndpointsNo": rasStatsAdmittedEndpointsNo,
       "rasStatsINAKs": rasStatsINAKs,
       "rasStatsIACKs": rasStatsIACKs,
       "rasStatsGkRoutedCalls": rasStatsGkRoutedCalls,
       "rasStatsResourceAvailabilityIndications": rasStatsResourceAvailabilityIndications,
       "rasStatsResourceAvailabilityConfirmations": rasStatsResourceAvailabilityConfirmations,
       "rasEvents": rasEvents,
       "lastArjReason": lastArjReason,
       "lastArjRasAddressTag": lastArjRasAddressTag,
       "lastArjRasAddress": lastArjRasAddress,
       "admissionReject": admissionReject,
       "rasMIBConformance": rasMIBConformance,
       "rasMIBGroups": rasMIBGroups,
       "rasConfigurationGroup": rasConfigurationGroup,
       "rasRegistrationGroup": rasRegistrationGroup,
       "rasAdmissionGroup": rasAdmissionGroup,
       "rasStatsGroup": rasStatsGroup,
       "rasEventsGroup": rasEventsGroup,
       "rasMIBCompliance": rasMIBCompliance}
)
