# SNMP MIB module (CISCO-BRIDGE-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BRIDGE-DOMAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:21 2024
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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoBridgeDomainMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 642)
)
ciscoBridgeDomainMIB.setRevisions(
        ("2007-12-29 00:00",
         "2007-12-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CbdType(Integer32, TextualConvention):
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
        *(("atmVc", 3),
          ("ether", 2),
          ("frVc", 4),
          ("other", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoBdMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoBdMIBNotifications = _CiscoBdMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 0)
)
_CiscoBdNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoBdNotificationPrefix = _CiscoBdNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 0, 0)
)
_CiscoBdMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBdMIBObjects = _CiscoBdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1)
)
_CbdSystemInfo_ObjectIdentity = ObjectIdentity
cbdSystemInfo = _CbdSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 1)
)
_CbdMembersConfigured_Type = Unsigned32
_CbdMembersConfigured_Object = MibScalar
cbdMembersConfigured = _CbdMembersConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 1, 1),
    _CbdMembersConfigured_Type()
)
cbdMembersConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdMembersConfigured.setStatus("current")
_CbdMemberInfo_ObjectIdentity = ObjectIdentity
cbdMemberInfo = _CbdMemberInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2)
)
_CbdMemberInfoTable_Object = MibTable
cbdMemberInfoTable = _CbdMemberInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cbdMemberInfoTable.setStatus("current")
_CbdMemberInfoEntry_Object = MibTableRow
cbdMemberInfoEntry = _CbdMemberInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1)
)
cbdMemberInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-BRIDGE-DOMAIN-MIB", "cbdSIIndex"),
)
if mibBuilder.loadTexts:
    cbdMemberInfoEntry.setStatus("current")


class _CbdSIIndex_Type(Unsigned32):
    """Custom type cbdSIIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CbdSIIndex_Type.__name__ = "Unsigned32"
_CbdSIIndex_Object = MibTableColumn
cbdSIIndex = _CbdSIIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 1),
    _CbdSIIndex_Type()
)
cbdSIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbdSIIndex.setStatus("current")


class _CbdMemberType_Type(CbdType):
    """Custom type cbdMemberType based on CbdType"""


_CbdMemberType_Object = MibTableColumn
cbdMemberType = _CbdMemberType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 2),
    _CbdMemberType_Type()
)
cbdMemberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbdMemberType.setStatus("current")


class _CbdMemberOperState_Type(Integer32):
    """Custom type cbdMemberOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_CbdMemberOperState_Type.__name__ = "Integer32"
_CbdMemberOperState_Object = MibTableColumn
cbdMemberOperState = _CbdMemberOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 3),
    _CbdMemberOperState_Type()
)
cbdMemberOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbdMemberOperState.setStatus("current")


class _CbdMemberAdminState_Type(Integer32):
    """Custom type cbdMemberAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_CbdMemberAdminState_Type.__name__ = "Integer32"
_CbdMemberAdminState_Object = MibTableColumn
cbdMemberAdminState = _CbdMemberAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 4),
    _CbdMemberAdminState_Type()
)
cbdMemberAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbdMemberAdminState.setStatus("current")
_CbdMemberSplitHorizon_Type = TruthValue
_CbdMemberSplitHorizon_Object = MibTableColumn
cbdMemberSplitHorizon = _CbdMemberSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 5),
    _CbdMemberSplitHorizon_Type()
)
cbdMemberSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbdMemberSplitHorizon.setStatus("current")


class _CbdMemberSplitHorizonNum_Type(Unsigned32):
    """Custom type cbdMemberSplitHorizonNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CbdMemberSplitHorizonNum_Type.__name__ = "Unsigned32"
_CbdMemberSplitHorizonNum_Object = MibTableColumn
cbdMemberSplitHorizonNum = _CbdMemberSplitHorizonNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 6),
    _CbdMemberSplitHorizonNum_Type()
)
cbdMemberSplitHorizonNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbdMemberSplitHorizonNum.setStatus("current")


class _CbdMemberStorageType_Type(StorageType):
    """Custom type cbdMemberStorageType based on StorageType"""


_CbdMemberStorageType_Object = MibTableColumn
cbdMemberStorageType = _CbdMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 7),
    _CbdMemberStorageType_Type()
)
cbdMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbdMemberStorageType.setStatus("current")


class _CbdMemberStatus_Type(RowStatus):
    """Custom type cbdMemberStatus based on RowStatus"""


_CbdMemberStatus_Object = MibTableColumn
cbdMemberStatus = _CbdMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 8),
    _CbdMemberStatus_Type()
)
cbdMemberStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbdMemberStatus.setStatus("current")
_CbdMembercMac_Type = TruthValue
_CbdMembercMac_Object = MibTableColumn
cbdMembercMac = _CbdMembercMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 1, 2, 1, 1, 9),
    _CbdMembercMac_Type()
)
cbdMembercMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbdMembercMac.setStatus("current")
_CiscoBdMIBConformance_ObjectIdentity = ObjectIdentity
ciscoBdMIBConformance = _CiscoBdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 2)
)
_CiscoBdMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBdMIBCompliances = _CiscoBdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 1)
)
_CiscoBdMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBdMIBGroups = _CiscoBdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 2)
)

# Managed Objects groups

cbdSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 2, 1)
)
cbdSystemInfoGroup.setObjects(
    ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMembersConfigured")
)
if mibBuilder.loadTexts:
    cbdSystemInfoGroup.setStatus("current")

cbdMemberInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 2, 2)
)
cbdMemberInfoGroup.setObjects(
      *(("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberType"),
        ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberOperState"),
        ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberAdminState"),
        ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberSplitHorizon"),
        ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberSplitHorizonNum"),
        ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberStorageType"),
        ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMemberStatus"),
        ("CISCO-BRIDGE-DOMAIN-MIB", "cbdMembercMac"))
)
if mibBuilder.loadTexts:
    cbdMemberInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoBdMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 642, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoBdMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BRIDGE-DOMAIN-MIB",
    **{"CbdType": CbdType,
       "ciscoBridgeDomainMIB": ciscoBridgeDomainMIB,
       "ciscoBdMIBNotifications": ciscoBdMIBNotifications,
       "ciscoBdNotificationPrefix": ciscoBdNotificationPrefix,
       "ciscoBdMIBObjects": ciscoBdMIBObjects,
       "cbdSystemInfo": cbdSystemInfo,
       "cbdMembersConfigured": cbdMembersConfigured,
       "cbdMemberInfo": cbdMemberInfo,
       "cbdMemberInfoTable": cbdMemberInfoTable,
       "cbdMemberInfoEntry": cbdMemberInfoEntry,
       "cbdSIIndex": cbdSIIndex,
       "cbdMemberType": cbdMemberType,
       "cbdMemberOperState": cbdMemberOperState,
       "cbdMemberAdminState": cbdMemberAdminState,
       "cbdMemberSplitHorizon": cbdMemberSplitHorizon,
       "cbdMemberSplitHorizonNum": cbdMemberSplitHorizonNum,
       "cbdMemberStorageType": cbdMemberStorageType,
       "cbdMemberStatus": cbdMemberStatus,
       "cbdMembercMac": cbdMembercMac,
       "ciscoBdMIBConformance": ciscoBdMIBConformance,
       "ciscoBdMIBCompliances": ciscoBdMIBCompliances,
       "ciscoBdMIBComplianceRev1": ciscoBdMIBComplianceRev1,
       "ciscoBdMIBGroups": ciscoBdMIBGroups,
       "cbdSystemInfoGroup": cbdSystemInfoGroup,
       "cbdMemberInfoGroup": cbdMemberInfoGroup}
)
