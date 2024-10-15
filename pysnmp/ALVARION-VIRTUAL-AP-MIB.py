# SNMP MIB module (ALVARION-VIRTUAL-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-VIRTUAL-AP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:28 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionPriorityQueue,
 AlvarionProfileIndexOrZero,
 AlvarionSSID,
 AlvarionSecurity,
 AlvarionUsersAuthenticationMode) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionPriorityQueue",
    "AlvarionProfileIndexOrZero",
    "AlvarionSSID",
    "AlvarionSecurity",
    "AlvarionUsersAuthenticationMode")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alvarionVirtualApMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionVirtualApMIBObjects_ObjectIdentity = ObjectIdentity
alvarionVirtualApMIBObjects = _AlvarionVirtualApMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1)
)
_CoVirtualApConfig_ObjectIdentity = ObjectIdentity
coVirtualApConfig = _CoVirtualApConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1)
)
_CoVirtualAccessPointConfigTable_Object = MibTable
coVirtualAccessPointConfigTable = _CoVirtualAccessPointConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coVirtualAccessPointConfigTable.setStatus("current")
_CoVirtualAccessPointConfigEntry_Object = MibTableRow
coVirtualAccessPointConfigEntry = _CoVirtualAccessPointConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1)
)
coVirtualAccessPointConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALVARION-VIRTUAL-AP-MIB", "coVirtualApWlanProfileIndex"),
)
if mibBuilder.loadTexts:
    coVirtualAccessPointConfigEntry.setStatus("current")


class _CoVirtualApWlanProfileIndex_Type(Integer32):
    """Custom type coVirtualApWlanProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoVirtualApWlanProfileIndex_Type.__name__ = "Integer32"
_CoVirtualApWlanProfileIndex_Object = MibTableColumn
coVirtualApWlanProfileIndex = _CoVirtualApWlanProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 1),
    _CoVirtualApWlanProfileIndex_Type()
)
coVirtualApWlanProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coVirtualApWlanProfileIndex.setStatus("current")
_CoVirtualApSSID_Type = AlvarionSSID
_CoVirtualApSSID_Object = MibTableColumn
coVirtualApSSID = _CoVirtualApSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 2),
    _CoVirtualApSSID_Type()
)
coVirtualApSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coVirtualApSSID.setStatus("current")
_CoVirtualApBroadcastSSID_Type = TruthValue
_CoVirtualApBroadcastSSID_Object = MibTableColumn
coVirtualApBroadcastSSID = _CoVirtualApBroadcastSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 3),
    _CoVirtualApBroadcastSSID_Type()
)
coVirtualApBroadcastSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coVirtualApBroadcastSSID.setStatus("current")


class _CoVirtualApMaximumNumberOfUsers_Type(Integer32):
    """Custom type coVirtualApMaximumNumberOfUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CoVirtualApMaximumNumberOfUsers_Type.__name__ = "Integer32"
_CoVirtualApMaximumNumberOfUsers_Object = MibTableColumn
coVirtualApMaximumNumberOfUsers = _CoVirtualApMaximumNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 4),
    _CoVirtualApMaximumNumberOfUsers_Type()
)
coVirtualApMaximumNumberOfUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coVirtualApMaximumNumberOfUsers.setStatus("current")


class _CoVirtualApDefaultVLAN_Type(Integer32):
    """Custom type coVirtualApDefaultVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CoVirtualApDefaultVLAN_Type.__name__ = "Integer32"
_CoVirtualApDefaultVLAN_Object = MibTableColumn
coVirtualApDefaultVLAN = _CoVirtualApDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 5),
    _CoVirtualApDefaultVLAN_Type()
)
coVirtualApDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coVirtualApDefaultVLAN.setStatus("current")
_CoVirtualApSecurity_Type = AlvarionSecurity
_CoVirtualApSecurity_Object = MibTableColumn
coVirtualApSecurity = _CoVirtualApSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 6),
    _CoVirtualApSecurity_Type()
)
coVirtualApSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVirtualApSecurity.setStatus("current")
_CoVirtualApAuthenMode_Type = AlvarionUsersAuthenticationMode
_CoVirtualApAuthenMode_Object = MibTableColumn
coVirtualApAuthenMode = _CoVirtualApAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 7),
    _CoVirtualApAuthenMode_Type()
)
coVirtualApAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVirtualApAuthenMode.setStatus("current")
_CoVirtualApAuthenProfileIndex_Type = AlvarionProfileIndexOrZero
_CoVirtualApAuthenProfileIndex_Object = MibTableColumn
coVirtualApAuthenProfileIndex = _CoVirtualApAuthenProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 8),
    _CoVirtualApAuthenProfileIndex_Type()
)
coVirtualApAuthenProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVirtualApAuthenProfileIndex.setStatus("current")


class _CoVirtualApUserAccountingEnabled_Type(Integer32):
    """Custom type coVirtualApUserAccountingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CoVirtualApUserAccountingEnabled_Type.__name__ = "Integer32"
_CoVirtualApUserAccountingEnabled_Object = MibTableColumn
coVirtualApUserAccountingEnabled = _CoVirtualApUserAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 9),
    _CoVirtualApUserAccountingEnabled_Type()
)
coVirtualApUserAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVirtualApUserAccountingEnabled.setStatus("current")
_CoVirtualApUserAccountingProfileIndex_Type = AlvarionProfileIndexOrZero
_CoVirtualApUserAccountingProfileIndex_Object = MibTableColumn
coVirtualApUserAccountingProfileIndex = _CoVirtualApUserAccountingProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 10),
    _CoVirtualApUserAccountingProfileIndex_Type()
)
coVirtualApUserAccountingProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVirtualApUserAccountingProfileIndex.setStatus("current")
_CoVirtualApDefaultUserRateLimitationEnabled_Type = TruthValue
_CoVirtualApDefaultUserRateLimitationEnabled_Object = MibTableColumn
coVirtualApDefaultUserRateLimitationEnabled = _CoVirtualApDefaultUserRateLimitationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 11),
    _CoVirtualApDefaultUserRateLimitationEnabled_Type()
)
coVirtualApDefaultUserRateLimitationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVirtualApDefaultUserRateLimitationEnabled.setStatus("current")
_CoVirtualApDefaultUserMaxTransmitRate_Type = Integer32
_CoVirtualApDefaultUserMaxTransmitRate_Object = MibTableColumn
coVirtualApDefaultUserMaxTransmitRate = _CoVirtualApDefaultUserMaxTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 12),
    _CoVirtualApDefaultUserMaxTransmitRate_Type()
)
coVirtualApDefaultUserMaxTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVirtualApDefaultUserMaxTransmitRate.setStatus("current")
_CoVirtualApDefaultUserMaxReceiveRate_Type = Integer32
_CoVirtualApDefaultUserMaxReceiveRate_Object = MibTableColumn
coVirtualApDefaultUserMaxReceiveRate = _CoVirtualApDefaultUserMaxReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 13),
    _CoVirtualApDefaultUserMaxReceiveRate_Type()
)
coVirtualApDefaultUserMaxReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVirtualApDefaultUserMaxReceiveRate.setStatus("current")
_CoVirtualApDefaultUserBandwidthLevel_Type = AlvarionPriorityQueue
_CoVirtualApDefaultUserBandwidthLevel_Object = MibTableColumn
coVirtualApDefaultUserBandwidthLevel = _CoVirtualApDefaultUserBandwidthLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 14),
    _CoVirtualApDefaultUserBandwidthLevel_Type()
)
coVirtualApDefaultUserBandwidthLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coVirtualApDefaultUserBandwidthLevel.setStatus("current")


class _CoVirtualApOperState_Type(Integer32):
    """Custom type coVirtualApOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CoVirtualApOperState_Type.__name__ = "Integer32"
_CoVirtualApOperState_Object = MibTableColumn
coVirtualApOperState = _CoVirtualApOperState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 1, 1, 1, 1, 15),
    _CoVirtualApOperState_Type()
)
coVirtualApOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coVirtualApOperState.setStatus("current")
_AlvarionVirtualApMIBConformance_ObjectIdentity = ObjectIdentity
alvarionVirtualApMIBConformance = _AlvarionVirtualApMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 2)
)
_AlvarionVirtualApMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionVirtualApMIBCompliances = _AlvarionVirtualApMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 2, 1)
)
_AlvarionVirtualApMIBGroups_ObjectIdentity = ObjectIdentity
alvarionVirtualApMIBGroups = _AlvarionVirtualApMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 2, 2)
)

# Managed Objects groups

alvarionVirtualApMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 2, 2, 1)
)
alvarionVirtualApMIBGroup.setObjects(
      *(("ALVARION-VIRTUAL-AP-MIB", "coVirtualApSSID"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApBroadcastSSID"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApMaximumNumberOfUsers"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApDefaultVLAN"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApSecurity"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApAuthenMode"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApAuthenProfileIndex"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApUserAccountingEnabled"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApUserAccountingProfileIndex"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApDefaultUserRateLimitationEnabled"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApDefaultUserMaxTransmitRate"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApDefaultUserMaxReceiveRate"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApDefaultUserBandwidthLevel"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApOperState"))
)
if mibBuilder.loadTexts:
    alvarionVirtualApMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alvarionVirtualApMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionVirtualApMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-VIRTUAL-AP-MIB",
    **{"alvarionVirtualApMIB": alvarionVirtualApMIB,
       "alvarionVirtualApMIBObjects": alvarionVirtualApMIBObjects,
       "coVirtualApConfig": coVirtualApConfig,
       "coVirtualAccessPointConfigTable": coVirtualAccessPointConfigTable,
       "coVirtualAccessPointConfigEntry": coVirtualAccessPointConfigEntry,
       "coVirtualApWlanProfileIndex": coVirtualApWlanProfileIndex,
       "coVirtualApSSID": coVirtualApSSID,
       "coVirtualApBroadcastSSID": coVirtualApBroadcastSSID,
       "coVirtualApMaximumNumberOfUsers": coVirtualApMaximumNumberOfUsers,
       "coVirtualApDefaultVLAN": coVirtualApDefaultVLAN,
       "coVirtualApSecurity": coVirtualApSecurity,
       "coVirtualApAuthenMode": coVirtualApAuthenMode,
       "coVirtualApAuthenProfileIndex": coVirtualApAuthenProfileIndex,
       "coVirtualApUserAccountingEnabled": coVirtualApUserAccountingEnabled,
       "coVirtualApUserAccountingProfileIndex": coVirtualApUserAccountingProfileIndex,
       "coVirtualApDefaultUserRateLimitationEnabled": coVirtualApDefaultUserRateLimitationEnabled,
       "coVirtualApDefaultUserMaxTransmitRate": coVirtualApDefaultUserMaxTransmitRate,
       "coVirtualApDefaultUserMaxReceiveRate": coVirtualApDefaultUserMaxReceiveRate,
       "coVirtualApDefaultUserBandwidthLevel": coVirtualApDefaultUserBandwidthLevel,
       "coVirtualApOperState": coVirtualApOperState,
       "alvarionVirtualApMIBConformance": alvarionVirtualApMIBConformance,
       "alvarionVirtualApMIBCompliances": alvarionVirtualApMIBCompliances,
       "alvarionVirtualApMIBCompliance": alvarionVirtualApMIBCompliance,
       "alvarionVirtualApMIBGroups": alvarionVirtualApMIBGroups,
       "alvarionVirtualApMIBGroup": alvarionVirtualApMIBGroup}
)
