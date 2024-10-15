# SNMP MIB module (AWC-VLAN-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AWC-VLAN-CFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:51 2024
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

(AwcDot11MicAlgorithm,
 AwcDot11WEPKeyPermuteAlgorithm,
 AwcPfPriority,
 AwcPolId,
 AwcVlanId,
 WEPKeytype128,
 awcVx) = mibBuilder.importSymbols(
    "AWCVX-MIB",
    "AwcDot11MicAlgorithm",
    "AwcDot11WEPKeyPermuteAlgorithm",
    "AwcPfPriority",
    "AwcPolId",
    "AwcVlanId",
    "WEPKeytype128",
    "awcVx")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

awcVlanCfgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 21)
)
awcVlanCfgMIB.setRevisions(
        ("2001-07-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AwcVlanIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class AwcVlanEncapType(Integer32, TextualConvention):
    status = "current"
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
        *(("dot1qDisabled", 1),
          ("dot1qHybrid", 3),
          ("dot1qPriority", 2),
          ("dot1qTrunk", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AwcVlanCfgObjects_ObjectIdentity = ObjectIdentity
awcVlanCfgObjects = _AwcVlanCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1)
)
_AwcMaxVlanIds_Type = Unsigned32
_AwcMaxVlanIds_Object = MibScalar
awcMaxVlanIds = _AwcMaxVlanIds_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 1),
    _AwcMaxVlanIds_Type()
)
awcMaxVlanIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcMaxVlanIds.setStatus("current")


class _AwcVlanEncapMode_Type(AwcVlanEncapType):
    """Custom type awcVlanEncapMode based on AwcVlanEncapType"""


_AwcVlanEncapMode_Object = MibScalar
awcVlanEncapMode = _AwcVlanEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 2),
    _AwcVlanEncapMode_Type()
)
awcVlanEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awcVlanEncapMode.setStatus("current")


class _AwcNativeVlanId_Type(AwcVlanId):
    """Custom type awcNativeVlanId based on AwcVlanId"""
    defaultValue = 0


_AwcNativeVlanId_Object = MibScalar
awcNativeVlanId = _AwcNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 3),
    _AwcNativeVlanId_Type()
)
awcNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcNativeVlanId.setStatus("current")


class _AwcVlanAllowEncrypted_Type(TruthValue):
    """Custom type awcVlanAllowEncrypted based on TruthValue"""


_AwcVlanAllowEncrypted_Object = MibScalar
awcVlanAllowEncrypted = _AwcVlanAllowEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 4),
    _AwcVlanAllowEncrypted_Type()
)
awcVlanAllowEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcVlanAllowEncrypted.setStatus("current")


class _AwcVlanAnyEnabled_Type(TruthValue):
    """Custom type awcVlanAnyEnabled based on TruthValue"""


_AwcVlanAnyEnabled_Object = MibScalar
awcVlanAnyEnabled = _AwcVlanAnyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 5),
    _AwcVlanAnyEnabled_Type()
)
awcVlanAnyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcVlanAnyEnabled.setStatus("current")
_AwcVlanCfgTable_Object = MibTable
awcVlanCfgTable = _AwcVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6)
)
if mibBuilder.loadTexts:
    awcVlanCfgTable.setStatus("current")
_AwcVlanCfgEntry_Object = MibTableRow
awcVlanCfgEntry = _AwcVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1)
)
awcVlanCfgEntry.setIndexNames(
    (0, "AWC-VLAN-CFG-MIB", "awcVlanIndex"),
)
if mibBuilder.loadTexts:
    awcVlanCfgEntry.setStatus("current")
_AwcVlanIndex_Type = AwcVlanIndex
_AwcVlanIndex_Object = MibTableColumn
awcVlanIndex = _AwcVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 1),
    _AwcVlanIndex_Type()
)
awcVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awcVlanIndex.setStatus("current")


class _AwcVlanPolId_Type(AwcPolId):
    """Custom type awcVlanPolId based on AwcPolId"""
    defaultValue = 0


_AwcVlanPolId_Object = MibTableColumn
awcVlanPolId = _AwcVlanPolId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 2),
    _AwcVlanPolId_Type()
)
awcVlanPolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcVlanPolId.setStatus("current")


class _AwcVlanEnabled_Type(TruthValue):
    """Custom type awcVlanEnabled based on TruthValue"""


_AwcVlanEnabled_Object = MibTableColumn
awcVlanEnabled = _AwcVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 3),
    _AwcVlanEnabled_Type()
)
awcVlanEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcVlanEnabled.setStatus("current")


class _AwcVlanNUcastKeyRotationInterval_Type(Integer32):
    """Custom type awcVlanNUcastKeyRotationInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_AwcVlanNUcastKeyRotationInterval_Type.__name__ = "Integer32"
_AwcVlanNUcastKeyRotationInterval_Object = MibTableColumn
awcVlanNUcastKeyRotationInterval = _AwcVlanNUcastKeyRotationInterval_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 4),
    _AwcVlanNUcastKeyRotationInterval_Type()
)
awcVlanNUcastKeyRotationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcVlanNUcastKeyRotationInterval.setStatus("current")
if mibBuilder.loadTexts:
    awcVlanNUcastKeyRotationInterval.setUnits("seconds")
_AwcVlanRowStatus_Type = RowStatus
_AwcVlanRowStatus_Object = MibTableColumn
awcVlanRowStatus = _AwcVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 5),
    _AwcVlanRowStatus_Type()
)
awcVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcVlanRowStatus.setStatus("current")


class _AwcVlanMicAlgorithm_Type(AwcDot11MicAlgorithm):
    """Custom type awcVlanMicAlgorithm based on AwcDot11MicAlgorithm"""


_AwcVlanMicAlgorithm_Object = MibTableColumn
awcVlanMicAlgorithm = _AwcVlanMicAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 6),
    _AwcVlanMicAlgorithm_Type()
)
awcVlanMicAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcVlanMicAlgorithm.setStatus("current")


class _AwcVlanWEPKeyPermuteAlgorithm_Type(AwcDot11WEPKeyPermuteAlgorithm):
    """Custom type awcVlanWEPKeyPermuteAlgorithm based on AwcDot11WEPKeyPermuteAlgorithm"""


_AwcVlanWEPKeyPermuteAlgorithm_Object = MibTableColumn
awcVlanWEPKeyPermuteAlgorithm = _AwcVlanWEPKeyPermuteAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 7),
    _AwcVlanWEPKeyPermuteAlgorithm_Type()
)
awcVlanWEPKeyPermuteAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcVlanWEPKeyPermuteAlgorithm.setStatus("current")
_AwcVlanName_Type = OctetString
_AwcVlanName_Object = MibTableColumn
awcVlanName = _AwcVlanName_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 8),
    _AwcVlanName_Type()
)
awcVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcVlanName.setStatus("current")


class _AwcVlanDefaultUserPriority_Type(AwcPfPriority):
    """Custom type awcVlanDefaultUserPriority based on AwcPfPriority"""


_AwcVlanDefaultUserPriority_Object = MibTableColumn
awcVlanDefaultUserPriority = _AwcVlanDefaultUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 9),
    _AwcVlanDefaultUserPriority_Type()
)
awcVlanDefaultUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcVlanDefaultUserPriority.setStatus("current")


class _AwcVlanAlert_Type(TruthValue):
    """Custom type awcVlanAlert based on TruthValue"""


_AwcVlanAlert_Object = MibTableColumn
awcVlanAlert = _AwcVlanAlert_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 6, 1, 10),
    _AwcVlanAlert_Type()
)
awcVlanAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    awcVlanAlert.setStatus("current")
_AwcVlanNUcastKeyTable_Object = MibTable
awcVlanNUcastKeyTable = _AwcVlanNUcastKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7)
)
if mibBuilder.loadTexts:
    awcVlanNUcastKeyTable.setStatus("current")
_AwcVlanNUcastKeyEntry_Object = MibTableRow
awcVlanNUcastKeyEntry = _AwcVlanNUcastKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7, 1)
)
awcVlanNUcastKeyEntry.setIndexNames(
    (0, "AWC-VLAN-CFG-MIB", "awcVlanIndex"),
    (0, "AWC-VLAN-CFG-MIB", "awcVlanNUcastKeyIndex"),
)
if mibBuilder.loadTexts:
    awcVlanNUcastKeyEntry.setStatus("current")


class _AwcVlanNUcastKeyIndex_Type(Integer32):
    """Custom type awcVlanNUcastKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwcVlanNUcastKeyIndex_Type.__name__ = "Integer32"
_AwcVlanNUcastKeyIndex_Object = MibTableColumn
awcVlanNUcastKeyIndex = _AwcVlanNUcastKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7, 1, 1),
    _AwcVlanNUcastKeyIndex_Type()
)
awcVlanNUcastKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awcVlanNUcastKeyIndex.setStatus("current")


class _AwcVlanNUcastKeyLen_Type(Integer32):
    """Custom type awcVlanNUcastKeyLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_AwcVlanNUcastKeyLen_Type.__name__ = "Integer32"
_AwcVlanNUcastKeyLen_Object = MibTableColumn
awcVlanNUcastKeyLen = _AwcVlanNUcastKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7, 1, 2),
    _AwcVlanNUcastKeyLen_Type()
)
awcVlanNUcastKeyLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcVlanNUcastKeyLen.setStatus("current")
_AwcVlanNUcastKeyValue_Type = WEPKeytype128
_AwcVlanNUcastKeyValue_Object = MibTableColumn
awcVlanNUcastKeyValue = _AwcVlanNUcastKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 7, 1, 3),
    _AwcVlanNUcastKeyValue_Type()
)
awcVlanNUcastKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcVlanNUcastKeyValue.setStatus("current")


class _AwcVlanAllowUnencryptedVlanId_Type(AwcVlanId):
    """Custom type awcVlanAllowUnencryptedVlanId based on AwcVlanId"""
    defaultValue = 0


_AwcVlanAllowUnencryptedVlanId_Object = MibScalar
awcVlanAllowUnencryptedVlanId = _AwcVlanAllowUnencryptedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 1, 8),
    _AwcVlanAllowUnencryptedVlanId_Type()
)
awcVlanAllowUnencryptedVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awcVlanAllowUnencryptedVlanId.setStatus("current")
_AwcVlanCfgNotifications_ObjectIdentity = ObjectIdentity
awcVlanCfgNotifications = _AwcVlanCfgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 2)
)
_AwcVlanCfgConformance_ObjectIdentity = ObjectIdentity
awcVlanCfgConformance = _AwcVlanCfgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 3)
)
_AwcVlanCfgCompliances_ObjectIdentity = ObjectIdentity
awcVlanCfgCompliances = _AwcVlanCfgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 3, 1)
)
_AwcVlanCfgGroups_ObjectIdentity = ObjectIdentity
awcVlanCfgGroups = _AwcVlanCfgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 3, 2)
)

# Managed Objects groups

awcVlanCfgObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 3, 2, 1)
)
awcVlanCfgObjectsGroup.setObjects(
      *(("AWC-VLAN-CFG-MIB", "awcMaxVlanIds"),
        ("AWC-VLAN-CFG-MIB", "awcVlanEncapMode"),
        ("AWC-VLAN-CFG-MIB", "awcNativeVlanId"),
        ("AWC-VLAN-CFG-MIB", "awcVlanAllowEncrypted"),
        ("AWC-VLAN-CFG-MIB", "awcVlanPolId"),
        ("AWC-VLAN-CFG-MIB", "awcVlanEnabled"),
        ("AWC-VLAN-CFG-MIB", "awcVlanNUcastKeyRotationInterval"),
        ("AWC-VLAN-CFG-MIB", "awcVlanRowStatus"),
        ("AWC-VLAN-CFG-MIB", "awcVlanMicAlgorithm"),
        ("AWC-VLAN-CFG-MIB", "awcVlanWEPKeyPermuteAlgorithm"),
        ("AWC-VLAN-CFG-MIB", "awcVlanName"),
        ("AWC-VLAN-CFG-MIB", "awcVlanDefaultUserPriority"),
        ("AWC-VLAN-CFG-MIB", "awcVlanAlert"),
        ("AWC-VLAN-CFG-MIB", "awcVlanNUcastKeyLen"),
        ("AWC-VLAN-CFG-MIB", "awcVlanNUcastKeyValue"),
        ("AWC-VLAN-CFG-MIB", "awcVlanAllowUnencryptedVlanId"))
)
if mibBuilder.loadTexts:
    awcVlanCfgObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

awcVlanCfgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 522, 3, 21, 3, 1, 1)
)
if mibBuilder.loadTexts:
    awcVlanCfgCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AWC-VLAN-CFG-MIB",
    **{"AwcVlanIndex": AwcVlanIndex,
       "AwcVlanEncapType": AwcVlanEncapType,
       "awcVlanCfgMIB": awcVlanCfgMIB,
       "awcVlanCfgObjects": awcVlanCfgObjects,
       "awcMaxVlanIds": awcMaxVlanIds,
       "awcVlanEncapMode": awcVlanEncapMode,
       "awcNativeVlanId": awcNativeVlanId,
       "awcVlanAllowEncrypted": awcVlanAllowEncrypted,
       "awcVlanAnyEnabled": awcVlanAnyEnabled,
       "awcVlanCfgTable": awcVlanCfgTable,
       "awcVlanCfgEntry": awcVlanCfgEntry,
       "awcVlanIndex": awcVlanIndex,
       "awcVlanPolId": awcVlanPolId,
       "awcVlanEnabled": awcVlanEnabled,
       "awcVlanNUcastKeyRotationInterval": awcVlanNUcastKeyRotationInterval,
       "awcVlanRowStatus": awcVlanRowStatus,
       "awcVlanMicAlgorithm": awcVlanMicAlgorithm,
       "awcVlanWEPKeyPermuteAlgorithm": awcVlanWEPKeyPermuteAlgorithm,
       "awcVlanName": awcVlanName,
       "awcVlanDefaultUserPriority": awcVlanDefaultUserPriority,
       "awcVlanAlert": awcVlanAlert,
       "awcVlanNUcastKeyTable": awcVlanNUcastKeyTable,
       "awcVlanNUcastKeyEntry": awcVlanNUcastKeyEntry,
       "awcVlanNUcastKeyIndex": awcVlanNUcastKeyIndex,
       "awcVlanNUcastKeyLen": awcVlanNUcastKeyLen,
       "awcVlanNUcastKeyValue": awcVlanNUcastKeyValue,
       "awcVlanAllowUnencryptedVlanId": awcVlanAllowUnencryptedVlanId,
       "awcVlanCfgNotifications": awcVlanCfgNotifications,
       "awcVlanCfgConformance": awcVlanCfgConformance,
       "awcVlanCfgCompliances": awcVlanCfgCompliances,
       "awcVlanCfgCompliance": awcVlanCfgCompliance,
       "awcVlanCfgGroups": awcVlanCfgGroups,
       "awcVlanCfgObjectsGroup": awcVlanCfgObjectsGroup}
)
