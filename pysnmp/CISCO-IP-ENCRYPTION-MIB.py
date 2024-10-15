# SNMP MIB module (CISCO-IP-ENCRYPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-ENCRYPTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:36 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(DisplayString,
 RowStatus,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString",
    "RowStatus",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpEncryptionMIB_ObjectIdentity = ObjectIdentity
ciscoIpEncryptionMIB = _CiscoIpEncryptionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52)
)
_CiscoIpEncryptionMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpEncryptionMIBObjects = _CiscoIpEncryptionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1)
)
_CieConfig_ObjectIdentity = ObjectIdentity
cieConfig = _CieConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 1)
)


class _CieConfiguredAlgorithms_Type(OctetString):
    """Custom type cieConfiguredAlgorithms based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CieConfiguredAlgorithms_Type.__name__ = "OctetString"
_CieConfiguredAlgorithms_Object = MibScalar
cieConfiguredAlgorithms = _CieConfiguredAlgorithms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 1, 1),
    _CieConfiguredAlgorithms_Type()
)
cieConfiguredAlgorithms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieConfiguredAlgorithms.setStatus("mandatory")
_CieEncryptionKeyTimeout_Type = Integer32
_CieEncryptionKeyTimeout_Object = MibScalar
cieEncryptionKeyTimeout = _CieEncryptionKeyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 1, 2),
    _CieEncryptionKeyTimeout_Type()
)
cieEncryptionKeyTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieEncryptionKeyTimeout.setStatus("mandatory")
_CieNumberOfCryptoEngines_Type = Gauge32
_CieNumberOfCryptoEngines_Object = MibScalar
cieNumberOfCryptoEngines = _CieNumberOfCryptoEngines_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 1, 3),
    _CieNumberOfCryptoEngines_Type()
)
cieNumberOfCryptoEngines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieNumberOfCryptoEngines.setStatus("mandatory")
_CieEngineStatus_ObjectIdentity = ObjectIdentity
cieEngineStatus = _CieEngineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2)
)
_CieEngineStatusTable_Object = MibTable
cieEngineStatusTable = _CieEngineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cieEngineStatusTable.setStatus("mandatory")
_CieEngineStatusEntry_Object = MibTableRow
cieEngineStatusEntry = _CieEngineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1)
)
cieEngineStatusEntry.setIndexNames(
    (0, "CISCO-IP-ENCRYPTION-MIB", "cieEngineID"),
)
if mibBuilder.loadTexts:
    cieEngineStatusEntry.setStatus("mandatory")


class _CieEngineID_Type(Integer32):
    """Custom type cieEngineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CieEngineID_Type.__name__ = "Integer32"
_CieEngineID_Object = MibTableColumn
cieEngineID = _CieEngineID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 1),
    _CieEngineID_Type()
)
cieEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieEngineID.setStatus("mandatory")
_CieEngineCardIndex_Type = Integer32
_CieEngineCardIndex_Object = MibTableColumn
cieEngineCardIndex = _CieEngineCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 2),
    _CieEngineCardIndex_Type()
)
cieEngineCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieEngineCardIndex.setStatus("mandatory")


class _CieEnginePublicKey_Type(OctetString):
    """Custom type cieEnginePublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CieEnginePublicKey_Type.__name__ = "OctetString"
_CieEnginePublicKey_Object = MibTableColumn
cieEnginePublicKey = _CieEnginePublicKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 3),
    _CieEnginePublicKey_Type()
)
cieEnginePublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieEnginePublicKey.setStatus("mandatory")
_CieEsaTampered_Type = TruthValue
_CieEsaTampered_Object = MibTableColumn
cieEsaTampered = _CieEsaTampered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 4),
    _CieEsaTampered_Type()
)
cieEsaTampered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieEsaTampered.setStatus("mandatory")
_CieEsaAuthenticated_Type = TruthValue
_CieEsaAuthenticated_Object = MibTableColumn
cieEsaAuthenticated = _CieEsaAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 5),
    _CieEsaAuthenticated_Type()
)
cieEsaAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieEsaAuthenticated.setStatus("mandatory")


class _CieEsaMode_Type(Integer32):
    """Custom type cieEsaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot", 2),
          ("enableActive", 1),
          ("error", 3))
    )


_CieEsaMode_Type.__name__ = "Integer32"
_CieEsaMode_Object = MibTableColumn
cieEsaMode = _CieEsaMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 6),
    _CieEsaMode_Type()
)
cieEsaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieEsaMode.setStatus("mandatory")
_CieConnections_ObjectIdentity = ObjectIdentity
cieConnections = _CieConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3)
)
_CieNumberOfConnections_Type = Gauge32
_CieNumberOfConnections_Object = MibScalar
cieNumberOfConnections = _CieNumberOfConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 1),
    _CieNumberOfConnections_Type()
)
cieNumberOfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieNumberOfConnections.setStatus("mandatory")
_CieConnTable_Object = MibTable
cieConnTable = _CieConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cieConnTable.setStatus("mandatory")
_CieConnEntry_Object = MibTableRow
cieConnEntry = _CieConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1)
)
cieConnEntry.setIndexNames(
    (0, "CISCO-IP-ENCRYPTION-MIB", "cieEngineID"),
    (0, "CISCO-IP-ENCRYPTION-MIB", "cieConnIndex"),
)
if mibBuilder.loadTexts:
    cieConnEntry.setStatus("mandatory")


class _CieConnIndex_Type(Integer32):
    """Custom type cieConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CieConnIndex_Type.__name__ = "Integer32"
_CieConnIndex_Object = MibTableColumn
cieConnIndex = _CieConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 1),
    _CieConnIndex_Type()
)
cieConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cieConnIndex.setStatus("mandatory")
_CieProtectedAddr_Type = IpAddress
_CieProtectedAddr_Object = MibTableColumn
cieProtectedAddr = _CieProtectedAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 2),
    _CieProtectedAddr_Type()
)
cieProtectedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieProtectedAddr.setStatus("mandatory")
_CieUnprotectedAddr_Type = IpAddress
_CieUnprotectedAddr_Object = MibTableColumn
cieUnprotectedAddr = _CieUnprotectedAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 3),
    _CieUnprotectedAddr_Type()
)
cieUnprotectedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieUnprotectedAddr.setStatus("mandatory")


class _CieConnStatus_Type(Integer32):
    """Custom type cieConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("badConnection", 4),
          ("exchangeKeys", 3),
          ("openConnection", 2),
          ("pendingConnection", 1))
    )


_CieConnStatus_Type.__name__ = "Integer32"
_CieConnStatus_Object = MibTableColumn
cieConnStatus = _CieConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 4),
    _CieConnStatus_Type()
)
cieConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieConnStatus.setStatus("mandatory")
_CiePktsEncrypted_Type = Counter32
_CiePktsEncrypted_Object = MibTableColumn
ciePktsEncrypted = _CiePktsEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 5),
    _CiePktsEncrypted_Type()
)
ciePktsEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciePktsEncrypted.setStatus("mandatory")
_CiePktsDecrypted_Type = Counter32
_CiePktsDecrypted_Object = MibTableColumn
ciePktsDecrypted = _CiePktsDecrypted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 6),
    _CiePktsDecrypted_Type()
)
ciePktsDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciePktsDecrypted.setStatus("mandatory")
_CiePktsDropped_Type = Counter32
_CiePktsDropped_Object = MibTableColumn
ciePktsDropped = _CiePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 7),
    _CiePktsDropped_Type()
)
ciePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciePktsDropped.setStatus("mandatory")
_CieLocalTimeEstablished_Type = TimeStamp
_CieLocalTimeEstablished_Object = MibTableColumn
cieLocalTimeEstablished = _CieLocalTimeEstablished_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 8),
    _CieLocalTimeEstablished_Type()
)
cieLocalTimeEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieLocalTimeEstablished.setStatus("mandatory")


class _CieAlgorithmType_Type(Integer32):
    """Custom type cieAlgorithmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("des40bitCfb64", 3),
          ("des40bitdesCfb8", 4),
          ("des56bitCfb64", 1),
          ("des56bitCfb8", 2))
    )


_CieAlgorithmType_Type.__name__ = "Integer32"
_CieAlgorithmType_Object = MibTableColumn
cieAlgorithmType = _CieAlgorithmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 9),
    _CieAlgorithmType_Type()
)
cieAlgorithmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieAlgorithmType.setStatus("mandatory")
_CieTestConnection_ObjectIdentity = ObjectIdentity
cieTestConnection = _CieTestConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4)
)
_CieTestConnTable_Object = MibTable
cieTestConnTable = _CieTestConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cieTestConnTable.setStatus("mandatory")
_CieTestConnEntry_Object = MibTableRow
cieTestConnEntry = _CieTestConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1)
)
cieTestConnEntry.setIndexNames(
    (0, "CISCO-IP-ENCRYPTION-MIB", "cieTestConnSerialNumber"),
)
if mibBuilder.loadTexts:
    cieTestConnEntry.setStatus("mandatory")


class _CieTestConnSerialNumber_Type(Integer32):
    """Custom type cieTestConnSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CieTestConnSerialNumber_Type.__name__ = "Integer32"
_CieTestConnSerialNumber_Object = MibTableColumn
cieTestConnSerialNumber = _CieTestConnSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 1),
    _CieTestConnSerialNumber_Type()
)
cieTestConnSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cieTestConnSerialNumber.setStatus("mandatory")
_CieTestConnProtectedAddr_Type = IpAddress
_CieTestConnProtectedAddr_Object = MibTableColumn
cieTestConnProtectedAddr = _CieTestConnProtectedAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 2),
    _CieTestConnProtectedAddr_Type()
)
cieTestConnProtectedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieTestConnProtectedAddr.setStatus("mandatory")
_CieTestConnUnprotectedAddr_Type = IpAddress
_CieTestConnUnprotectedAddr_Object = MibTableColumn
cieTestConnUnprotectedAddr = _CieTestConnUnprotectedAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 3),
    _CieTestConnUnprotectedAddr_Type()
)
cieTestConnUnprotectedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieTestConnUnprotectedAddr.setStatus("mandatory")


class _CieTestConnTrapOnCompletion_Type(TruthValue):
    """Custom type cieTestConnTrapOnCompletion based on TruthValue"""


_CieTestConnTrapOnCompletion_Object = MibTableColumn
cieTestConnTrapOnCompletion = _CieTestConnTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 4),
    _CieTestConnTrapOnCompletion_Type()
)
cieTestConnTrapOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieTestConnTrapOnCompletion.setStatus("mandatory")
_CieTestConnCryptoMapName_Type = DisplayString
_CieTestConnCryptoMapName_Object = MibTableColumn
cieTestConnCryptoMapName = _CieTestConnCryptoMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 5),
    _CieTestConnCryptoMapName_Type()
)
cieTestConnCryptoMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieTestConnCryptoMapName.setStatus("mandatory")


class _CieTestConnCryptoMapTagNumber_Type(Integer32):
    """Custom type cieTestConnCryptoMapTagNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CieTestConnCryptoMapTagNumber_Type.__name__ = "Integer32"
_CieTestConnCryptoMapTagNumber_Object = MibTableColumn
cieTestConnCryptoMapTagNumber = _CieTestConnCryptoMapTagNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 6),
    _CieTestConnCryptoMapTagNumber_Type()
)
cieTestConnCryptoMapTagNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieTestConnCryptoMapTagNumber.setStatus("mandatory")


class _CieTestConnSessionStatus_Type(Integer32):
    """Custom type cieTestConnSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("badCryptoMapName", 4),
          ("fail", 2),
          ("inProgress", 1),
          ("success", 3))
    )


_CieTestConnSessionStatus_Type.__name__ = "Integer32"
_CieTestConnSessionStatus_Object = MibTableColumn
cieTestConnSessionStatus = _CieTestConnSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 7),
    _CieTestConnSessionStatus_Type()
)
cieTestConnSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieTestConnSessionStatus.setStatus("mandatory")
_CieTestConnEntryOwner_Type = OwnerString
_CieTestConnEntryOwner_Object = MibTableColumn
cieTestConnEntryOwner = _CieTestConnEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 8),
    _CieTestConnEntryOwner_Type()
)
cieTestConnEntryOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieTestConnEntryOwner.setStatus("mandatory")


class _CieTestConnEntryStatus_Type(RowStatus):
    """Custom type cieTestConnEntryStatus based on RowStatus"""


_CieTestConnEntryStatus_Object = MibTableColumn
cieTestConnEntryStatus = _CieTestConnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 9),
    _CieTestConnEntryStatus_Type()
)
cieTestConnEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieTestConnEntryStatus.setStatus("mandatory")
_CieMIBTrapPrefix_ObjectIdentity = ObjectIdentity
cieMIBTrapPrefix = _CieMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 2)
)
_CieMIBTraps_ObjectIdentity = ObjectIdentity
cieMIBTraps = _CieMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 2, 0)
)
_CieMIBConformance_ObjectIdentity = ObjectIdentity
cieMIBConformance = _CieMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 3)
)
_CieMIBCompliances_ObjectIdentity = ObjectIdentity
cieMIBCompliances = _CieMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 3, 1)
)
_CieMIBCompliance_ObjectIdentity = ObjectIdentity
cieMIBCompliance = _CieMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 3, 1, 1)
)
_CieMIBGroups_ObjectIdentity = ObjectIdentity
cieMIBGroups = _CieMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 3, 2)
)
_CieMIBGroup_ObjectIdentity = ObjectIdentity
cieMIBGroup = _CieMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 3, 2, 1)
)

# Managed Objects groups


# Notification objects

cieTestCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 52, 2, 0, 1)
)
cieTestCompletion.setObjects(
      *(("CISCO-IP-ENCRYPTION-MIB", "cieTestConnSessionStatus"),
        ("CISCO-IP-ENCRYPTION-MIB", "cieTestConnProtectedAddr"),
        ("CISCO-IP-ENCRYPTION-MIB", "cieTestConnUnprotectedAddr"))
)
if mibBuilder.loadTexts:
    cieTestCompletion.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-ENCRYPTION-MIB",
    **{"ciscoIpEncryptionMIB": ciscoIpEncryptionMIB,
       "ciscoIpEncryptionMIBObjects": ciscoIpEncryptionMIBObjects,
       "cieConfig": cieConfig,
       "cieConfiguredAlgorithms": cieConfiguredAlgorithms,
       "cieEncryptionKeyTimeout": cieEncryptionKeyTimeout,
       "cieNumberOfCryptoEngines": cieNumberOfCryptoEngines,
       "cieEngineStatus": cieEngineStatus,
       "cieEngineStatusTable": cieEngineStatusTable,
       "cieEngineStatusEntry": cieEngineStatusEntry,
       "cieEngineID": cieEngineID,
       "cieEngineCardIndex": cieEngineCardIndex,
       "cieEnginePublicKey": cieEnginePublicKey,
       "cieEsaTampered": cieEsaTampered,
       "cieEsaAuthenticated": cieEsaAuthenticated,
       "cieEsaMode": cieEsaMode,
       "cieConnections": cieConnections,
       "cieNumberOfConnections": cieNumberOfConnections,
       "cieConnTable": cieConnTable,
       "cieConnEntry": cieConnEntry,
       "cieConnIndex": cieConnIndex,
       "cieProtectedAddr": cieProtectedAddr,
       "cieUnprotectedAddr": cieUnprotectedAddr,
       "cieConnStatus": cieConnStatus,
       "ciePktsEncrypted": ciePktsEncrypted,
       "ciePktsDecrypted": ciePktsDecrypted,
       "ciePktsDropped": ciePktsDropped,
       "cieLocalTimeEstablished": cieLocalTimeEstablished,
       "cieAlgorithmType": cieAlgorithmType,
       "cieTestConnection": cieTestConnection,
       "cieTestConnTable": cieTestConnTable,
       "cieTestConnEntry": cieTestConnEntry,
       "cieTestConnSerialNumber": cieTestConnSerialNumber,
       "cieTestConnProtectedAddr": cieTestConnProtectedAddr,
       "cieTestConnUnprotectedAddr": cieTestConnUnprotectedAddr,
       "cieTestConnTrapOnCompletion": cieTestConnTrapOnCompletion,
       "cieTestConnCryptoMapName": cieTestConnCryptoMapName,
       "cieTestConnCryptoMapTagNumber": cieTestConnCryptoMapTagNumber,
       "cieTestConnSessionStatus": cieTestConnSessionStatus,
       "cieTestConnEntryOwner": cieTestConnEntryOwner,
       "cieTestConnEntryStatus": cieTestConnEntryStatus,
       "cieMIBTrapPrefix": cieMIBTrapPrefix,
       "cieMIBTraps": cieMIBTraps,
       "cieTestCompletion": cieTestCompletion,
       "cieMIBConformance": cieMIBConformance,
       "cieMIBCompliances": cieMIBCompliances,
       "cieMIBCompliance": cieMIBCompliance,
       "cieMIBGroups": cieMIBGroups,
       "cieMIBGroup": cieMIBGroup}
)
