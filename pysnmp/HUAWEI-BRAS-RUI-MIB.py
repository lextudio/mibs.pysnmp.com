# SNMP MIB module (HUAWEI-BRAS-RUI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-RUI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:06 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwBRASRui = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwPeerBackupObject_ObjectIdentity = ObjectIdentity
hwPeerBackupObject = _HwPeerBackupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1)
)
_HwPeerBackupEnableTable_ObjectIdentity = ObjectIdentity
hwPeerBackupEnableTable = _HwPeerBackupEnableTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1)
)
_HwPeerBackupEnableEntry_ObjectIdentity = ObjectIdentity
hwPeerBackupEnableEntry = _HwPeerBackupEnableEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1)
)


class _HwPeerBackupEnable_Type(Integer32):
    """Custom type hwPeerBackupEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("hotEnable", 2),
          ("warmEnable", 3))
    )


_HwPeerBackupEnable_Type.__name__ = "Integer32"
_HwPeerBackupEnable_Object = MibScalar
hwPeerBackupEnable = _HwPeerBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 1),
    _HwPeerBackupEnable_Type()
)
hwPeerBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPeerBackupEnable.setStatus("current")
_HwPeerBackupServerTable_Object = MibTable
hwPeerBackupServerTable = _HwPeerBackupServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2)
)
if mibBuilder.loadTexts:
    hwPeerBackupServerTable.setStatus("current")
_HwPeerBackupServerEntry_Object = MibTableRow
hwPeerBackupServerEntry = _HwPeerBackupServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1)
)
hwPeerBackupServerEntry.setIndexNames(
    (0, "HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerPeerIp"),
)
if mibBuilder.loadTexts:
    hwPeerBackupServerEntry.setStatus("current")
_HwPeerBackupServerPeerIp_Type = IpAddress
_HwPeerBackupServerPeerIp_Object = MibTableColumn
hwPeerBackupServerPeerIp = _HwPeerBackupServerPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 1),
    _HwPeerBackupServerPeerIp_Type()
)
hwPeerBackupServerPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPeerBackupServerPeerIp.setStatus("current")
_HwPeerBackupServerLocalIp_Type = IpAddress
_HwPeerBackupServerLocalIp_Object = MibTableColumn
hwPeerBackupServerLocalIp = _HwPeerBackupServerLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 2),
    _HwPeerBackupServerLocalIp_Type()
)
hwPeerBackupServerLocalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPeerBackupServerLocalIp.setStatus("current")


class _HwPeerBackupServerPort_Type(Integer32):
    """Custom type hwPeerBackupServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 55535),
    )


_HwPeerBackupServerPort_Type.__name__ = "Integer32"
_HwPeerBackupServerPort_Object = MibTableColumn
hwPeerBackupServerPort = _HwPeerBackupServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 3),
    _HwPeerBackupServerPort_Type()
)
hwPeerBackupServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPeerBackupServerPort.setStatus("current")


class _HwPeerBackupServerDetectRetransmit_Type(Integer32):
    """Custom type hwPeerBackupServerDetectRetransmit based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 12),
    )


_HwPeerBackupServerDetectRetransmit_Type.__name__ = "Integer32"
_HwPeerBackupServerDetectRetransmit_Object = MibTableColumn
hwPeerBackupServerDetectRetransmit = _HwPeerBackupServerDetectRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 4),
    _HwPeerBackupServerDetectRetransmit_Type()
)
hwPeerBackupServerDetectRetransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPeerBackupServerDetectRetransmit.setStatus("current")


class _HwPeerBackupServerDetectInterval_Type(Integer32):
    """Custom type hwPeerBackupServerDetectInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_HwPeerBackupServerDetectInterval_Type.__name__ = "Integer32"
_HwPeerBackupServerDetectInterval_Object = MibTableColumn
hwPeerBackupServerDetectInterval = _HwPeerBackupServerDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 5),
    _HwPeerBackupServerDetectInterval_Type()
)
hwPeerBackupServerDetectInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPeerBackupServerDetectInterval.setStatus("current")
_HwPeerBackupServerRowStatus_Type = RowStatus
_HwPeerBackupServerRowStatus_Object = MibTableColumn
hwPeerBackupServerRowStatus = _HwPeerBackupServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 2, 1, 6),
    _HwPeerBackupServerRowStatus_Type()
)
hwPeerBackupServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPeerBackupServerRowStatus.setStatus("current")
_HwRemoteBackupProfileTable_Object = MibTable
hwRemoteBackupProfileTable = _HwRemoteBackupProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3)
)
if mibBuilder.loadTexts:
    hwRemoteBackupProfileTable.setStatus("current")
_HwRemoteBackupProfileEntry_Object = MibTableRow
hwRemoteBackupProfileEntry = _HwRemoteBackupProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1)
)
hwRemoteBackupProfileEntry.setIndexNames(
    (0, "HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIndex"),
)
if mibBuilder.loadTexts:
    hwRemoteBackupProfileEntry.setStatus("current")


class _HwRemoteBackupProfileIndex_Type(Integer32):
    """Custom type hwRemoteBackupProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwRemoteBackupProfileIndex_Type.__name__ = "Integer32"
_HwRemoteBackupProfileIndex_Object = MibTableColumn
hwRemoteBackupProfileIndex = _HwRemoteBackupProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 1),
    _HwRemoteBackupProfileIndex_Type()
)
hwRemoteBackupProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRemoteBackupProfileIndex.setStatus("current")


class _HwRemoteBackupProfileName_Type(DisplayString):
    """Custom type hwRemoteBackupProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwRemoteBackupProfileName_Type.__name__ = "DisplayString"
_HwRemoteBackupProfileName_Object = MibTableColumn
hwRemoteBackupProfileName = _HwRemoteBackupProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 2),
    _HwRemoteBackupProfileName_Type()
)
hwRemoteBackupProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteBackupProfileName.setStatus("current")
_HwRemoteBackupProfilePeerIP_Type = IpAddress
_HwRemoteBackupProfilePeerIP_Object = MibTableColumn
hwRemoteBackupProfilePeerIP = _HwRemoteBackupProfilePeerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 3),
    _HwRemoteBackupProfilePeerIP_Type()
)
hwRemoteBackupProfilePeerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteBackupProfilePeerIP.setStatus("current")


class _HwRemoteBackupProfileVrrpID_Type(Integer32):
    """Custom type hwRemoteBackupProfileVrrpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwRemoteBackupProfileVrrpID_Type.__name__ = "Integer32"
_HwRemoteBackupProfileVrrpID_Object = MibTableColumn
hwRemoteBackupProfileVrrpID = _HwRemoteBackupProfileVrrpID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 4),
    _HwRemoteBackupProfileVrrpID_Type()
)
hwRemoteBackupProfileVrrpID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteBackupProfileVrrpID.setStatus("current")


class _HwRemoteBackupProfileBackupID_Type(Integer32):
    """Custom type hwRemoteBackupProfileBackupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_HwRemoteBackupProfileBackupID_Type.__name__ = "Integer32"
_HwRemoteBackupProfileBackupID_Object = MibTableColumn
hwRemoteBackupProfileBackupID = _HwRemoteBackupProfileBackupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 5),
    _HwRemoteBackupProfileBackupID_Type()
)
hwRemoteBackupProfileBackupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteBackupProfileBackupID.setStatus("current")
_HwRemoteBackupProfileRowStatus_Type = RowStatus
_HwRemoteBackupProfileRowStatus_Object = MibTableColumn
hwRemoteBackupProfileRowStatus = _HwRemoteBackupProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 3, 1, 6),
    _HwRemoteBackupProfileRowStatus_Type()
)
hwRemoteBackupProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteBackupProfileRowStatus.setStatus("current")
_HwRemoteBackupProfileExtTable_Object = MibTable
hwRemoteBackupProfileExtTable = _HwRemoteBackupProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4)
)
if mibBuilder.loadTexts:
    hwRemoteBackupProfileExtTable.setStatus("current")
_HwRemoteBackupProfileExtEntry_Object = MibTableRow
hwRemoteBackupProfileExtEntry = _HwRemoteBackupProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1)
)
hwRemoteBackupProfileExtEntry.setIndexNames(
    (0, "HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIndex"),
    (0, "HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIPPoolBindIndex"),
)
if mibBuilder.loadTexts:
    hwRemoteBackupProfileExtEntry.setStatus("current")


class _HwRemoteBackupProfileIPPoolBindIndex_Type(Integer32):
    """Custom type hwRemoteBackupProfileIPPoolBindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwRemoteBackupProfileIPPoolBindIndex_Type.__name__ = "Integer32"
_HwRemoteBackupProfileIPPoolBindIndex_Object = MibTableColumn
hwRemoteBackupProfileIPPoolBindIndex = _HwRemoteBackupProfileIPPoolBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1, 1),
    _HwRemoteBackupProfileIPPoolBindIndex_Type()
)
hwRemoteBackupProfileIPPoolBindIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRemoteBackupProfileIPPoolBindIndex.setStatus("current")


class _HwRemoteBackupProfileIPPoolIndex_Type(Integer32):
    """Custom type hwRemoteBackupProfileIPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
        ValueRangeConstraint(65535, 65535),
    )


_HwRemoteBackupProfileIPPoolIndex_Type.__name__ = "Integer32"
_HwRemoteBackupProfileIPPoolIndex_Object = MibTableColumn
hwRemoteBackupProfileIPPoolIndex = _HwRemoteBackupProfileIPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1, 2),
    _HwRemoteBackupProfileIPPoolIndex_Type()
)
hwRemoteBackupProfileIPPoolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteBackupProfileIPPoolIndex.setStatus("current")


class _HwRemoteBackupProfileDomainName_Type(DisplayString):
    """Custom type hwRemoteBackupProfileDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwRemoteBackupProfileDomainName_Type.__name__ = "DisplayString"
_HwRemoteBackupProfileDomainName_Object = MibTableColumn
hwRemoteBackupProfileDomainName = _HwRemoteBackupProfileDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1, 3),
    _HwRemoteBackupProfileDomainName_Type()
)
hwRemoteBackupProfileDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteBackupProfileDomainName.setStatus("current")
_HwRemoteBackupProfileExtRowStatus_Type = RowStatus
_HwRemoteBackupProfileExtRowStatus_Object = MibTableColumn
hwRemoteBackupProfileExtRowStatus = _HwRemoteBackupProfileExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 4, 1, 4),
    _HwRemoteBackupProfileExtRowStatus_Type()
)
hwRemoteBackupProfileExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteBackupProfileExtRowStatus.setStatus("current")
_HwRuiConformance_ObjectIdentity = ObjectIdentity
hwRuiConformance = _HwRuiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2)
)
_HwRuiCompliances_ObjectIdentity = ObjectIdentity
hwRuiCompliances = _HwRuiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 1)
)
_HwRuiGroups_ObjectIdentity = ObjectIdentity
hwRuiGroups = _HwRuiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2)
)

# Managed Objects groups

hwPeerBackupEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2, 1)
)
hwPeerBackupEnableGroup.setObjects(
    ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupEnable")
)
if mibBuilder.loadTexts:
    hwPeerBackupEnableGroup.setStatus("current")

hwPeerBackupServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2, 2)
)
hwPeerBackupServerGroup.setObjects(
      *(("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerPeerIp"),
        ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerLocalIp"),
        ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerPort"),
        ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerDetectRetransmit"),
        ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerDetectInterval"),
        ("HUAWEI-BRAS-RUI-MIB", "hwPeerBackupServerRowStatus"))
)
if mibBuilder.loadTexts:
    hwPeerBackupServerGroup.setStatus("current")

hwRemoteBackupProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2, 3)
)
hwRemoteBackupProfileGroup.setObjects(
      *(("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIndex"),
        ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileName"),
        ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfilePeerIP"),
        ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileVrrpID"),
        ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileBackupID"),
        ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwRemoteBackupProfileGroup.setStatus("current")

hwRemoteBackupProfileExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 2, 4)
)
hwRemoteBackupProfileExtGroup.setObjects(
      *(("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIPPoolBindIndex"),
        ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileIPPoolIndex"),
        ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileDomainName"),
        ("HUAWEI-BRAS-RUI-MIB", "hwRemoteBackupProfileExtRowStatus"))
)
if mibBuilder.loadTexts:
    hwRemoteBackupProfileExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwRuiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwRuiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-RUI-MIB",
    **{"hwBRASRui": hwBRASRui,
       "hwPeerBackupObject": hwPeerBackupObject,
       "hwPeerBackupEnableTable": hwPeerBackupEnableTable,
       "hwPeerBackupEnableEntry": hwPeerBackupEnableEntry,
       "hwPeerBackupEnable": hwPeerBackupEnable,
       "hwPeerBackupServerTable": hwPeerBackupServerTable,
       "hwPeerBackupServerEntry": hwPeerBackupServerEntry,
       "hwPeerBackupServerPeerIp": hwPeerBackupServerPeerIp,
       "hwPeerBackupServerLocalIp": hwPeerBackupServerLocalIp,
       "hwPeerBackupServerPort": hwPeerBackupServerPort,
       "hwPeerBackupServerDetectRetransmit": hwPeerBackupServerDetectRetransmit,
       "hwPeerBackupServerDetectInterval": hwPeerBackupServerDetectInterval,
       "hwPeerBackupServerRowStatus": hwPeerBackupServerRowStatus,
       "hwRemoteBackupProfileTable": hwRemoteBackupProfileTable,
       "hwRemoteBackupProfileEntry": hwRemoteBackupProfileEntry,
       "hwRemoteBackupProfileIndex": hwRemoteBackupProfileIndex,
       "hwRemoteBackupProfileName": hwRemoteBackupProfileName,
       "hwRemoteBackupProfilePeerIP": hwRemoteBackupProfilePeerIP,
       "hwRemoteBackupProfileVrrpID": hwRemoteBackupProfileVrrpID,
       "hwRemoteBackupProfileBackupID": hwRemoteBackupProfileBackupID,
       "hwRemoteBackupProfileRowStatus": hwRemoteBackupProfileRowStatus,
       "hwRemoteBackupProfileExtTable": hwRemoteBackupProfileExtTable,
       "hwRemoteBackupProfileExtEntry": hwRemoteBackupProfileExtEntry,
       "hwRemoteBackupProfileIPPoolBindIndex": hwRemoteBackupProfileIPPoolBindIndex,
       "hwRemoteBackupProfileIPPoolIndex": hwRemoteBackupProfileIPPoolIndex,
       "hwRemoteBackupProfileDomainName": hwRemoteBackupProfileDomainName,
       "hwRemoteBackupProfileExtRowStatus": hwRemoteBackupProfileExtRowStatus,
       "hwRuiConformance": hwRuiConformance,
       "hwRuiCompliances": hwRuiCompliances,
       "hwRuiCompliance": hwRuiCompliance,
       "hwRuiGroups": hwRuiGroups,
       "hwPeerBackupEnableGroup": hwPeerBackupEnableGroup,
       "hwPeerBackupServerGroup": hwPeerBackupServerGroup,
       "hwRemoteBackupProfileGroup": hwRemoteBackupProfileGroup,
       "hwRemoteBackupProfileExtGroup": hwRemoteBackupProfileExtGroup}
)
