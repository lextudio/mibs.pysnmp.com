# SNMP MIB module (ZYXEL-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:30 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelCluster = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelClusterSetup_ObjectIdentity = ObjectIdentity
zyxelClusterSetup = _ZyxelClusterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1)
)
_ZyxelClusterManager_ObjectIdentity = ObjectIdentity
zyxelClusterManager = _ZyxelClusterManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 1)
)
_ZyClusterManagerMaxNumberOfManagers_Type = Integer32
_ZyClusterManagerMaxNumberOfManagers_Object = MibScalar
zyClusterManagerMaxNumberOfManagers = _ZyClusterManagerMaxNumberOfManagers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 1, 1),
    _ZyClusterManagerMaxNumberOfManagers_Type()
)
zyClusterManagerMaxNumberOfManagers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterManagerMaxNumberOfManagers.setStatus("current")
_ZyxelClusterManagerTable_Object = MibTable
zyxelClusterManagerTable = _ZyxelClusterManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelClusterManagerTable.setStatus("current")
_ZyxelClusterManagerEntry_Object = MibTableRow
zyxelClusterManagerEntry = _ZyxelClusterManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 1, 2, 1)
)
zyxelClusterManagerEntry.setIndexNames(
    (0, "ZYXEL-CLUSTER-MIB", "zyClusterManagerVid"),
)
if mibBuilder.loadTexts:
    zyxelClusterManagerEntry.setStatus("current")
_ZyClusterManagerVid_Type = Integer32
_ZyClusterManagerVid_Object = MibTableColumn
zyClusterManagerVid = _ZyClusterManagerVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 1, 2, 1, 1),
    _ZyClusterManagerVid_Type()
)
zyClusterManagerVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyClusterManagerVid.setStatus("current")
_ZyClusterManagerName_Type = DisplayString
_ZyClusterManagerName_Object = MibTableColumn
zyClusterManagerName = _ZyClusterManagerName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 1, 2, 1, 2),
    _ZyClusterManagerName_Type()
)
zyClusterManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyClusterManagerName.setStatus("current")
_ZyClusterManagerRowStatus_Type = RowStatus
_ZyClusterManagerRowStatus_Object = MibTableColumn
zyClusterManagerRowStatus = _ZyClusterManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 1, 2, 1, 3),
    _ZyClusterManagerRowStatus_Type()
)
zyClusterManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyClusterManagerRowStatus.setStatus("current")
_ZyxelClusterMembers_ObjectIdentity = ObjectIdentity
zyxelClusterMembers = _ZyxelClusterMembers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 2)
)
_ZyClusterMemberMaxNumberOfMembers_Type = Integer32
_ZyClusterMemberMaxNumberOfMembers_Object = MibScalar
zyClusterMemberMaxNumberOfMembers = _ZyClusterMemberMaxNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 2, 1),
    _ZyClusterMemberMaxNumberOfMembers_Type()
)
zyClusterMemberMaxNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterMemberMaxNumberOfMembers.setStatus("current")
_ZyxelClusterMemberTable_Object = MibTable
zyxelClusterMemberTable = _ZyxelClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelClusterMemberTable.setStatus("current")
_ZyxelClusterMemberEntry_Object = MibTableRow
zyxelClusterMemberEntry = _ZyxelClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 2, 2, 1)
)
zyxelClusterMemberEntry.setIndexNames(
    (0, "ZYXEL-CLUSTER-MIB", "zyClusterMemberMacAddress"),
)
if mibBuilder.loadTexts:
    zyxelClusterMemberEntry.setStatus("current")
_ZyClusterMemberMacAddress_Type = MacAddress
_ZyClusterMemberMacAddress_Object = MibTableColumn
zyClusterMemberMacAddress = _ZyClusterMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 2, 2, 1, 1),
    _ZyClusterMemberMacAddress_Type()
)
zyClusterMemberMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyClusterMemberMacAddress.setStatus("current")
_ZyClusterMemberName_Type = DisplayString
_ZyClusterMemberName_Object = MibTableColumn
zyClusterMemberName = _ZyClusterMemberName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 2, 2, 1, 2),
    _ZyClusterMemberName_Type()
)
zyClusterMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterMemberName.setStatus("current")
_ZyClusterMemberModel_Type = DisplayString
_ZyClusterMemberModel_Object = MibTableColumn
zyClusterMemberModel = _ZyClusterMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 2, 2, 1, 3),
    _ZyClusterMemberModel_Type()
)
zyClusterMemberModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterMemberModel.setStatus("current")
_ZyClusterMemberPassword_Type = DisplayString
_ZyClusterMemberPassword_Object = MibTableColumn
zyClusterMemberPassword = _ZyClusterMemberPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 2, 2, 1, 4),
    _ZyClusterMemberPassword_Type()
)
zyClusterMemberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyClusterMemberPassword.setStatus("current")
_ZyClusterMemberRowStatus_Type = RowStatus
_ZyClusterMemberRowStatus_Object = MibTableColumn
zyClusterMemberRowStatus = _ZyClusterMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 1, 2, 2, 1, 5),
    _ZyClusterMemberRowStatus_Type()
)
zyClusterMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyClusterMemberRowStatus.setStatus("current")
_ZyxelClusterStatus_ObjectIdentity = ObjectIdentity
zyxelClusterStatus = _ZyxelClusterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2)
)
_ZyxelClusterCandidate_ObjectIdentity = ObjectIdentity
zyxelClusterCandidate = _ZyxelClusterCandidate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 1)
)
_ZyxelClusterCandidateTable_Object = MibTable
zyxelClusterCandidateTable = _ZyxelClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelClusterCandidateTable.setStatus("current")
_ZyxelClusterCandidateEntry_Object = MibTableRow
zyxelClusterCandidateEntry = _ZyxelClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 1, 1, 1)
)
zyxelClusterCandidateEntry.setIndexNames(
    (0, "ZYXEL-CLUSTER-MIB", "zyClusterCandidateMacAddress"),
)
if mibBuilder.loadTexts:
    zyxelClusterCandidateEntry.setStatus("current")
_ZyClusterCandidateMacAddress_Type = MacAddress
_ZyClusterCandidateMacAddress_Object = MibTableColumn
zyClusterCandidateMacAddress = _ZyClusterCandidateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 1, 1, 1, 1),
    _ZyClusterCandidateMacAddress_Type()
)
zyClusterCandidateMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyClusterCandidateMacAddress.setStatus("current")
_ZyClusterCandidateName_Type = DisplayString
_ZyClusterCandidateName_Object = MibTableColumn
zyClusterCandidateName = _ZyClusterCandidateName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 1, 1, 1, 2),
    _ZyClusterCandidateName_Type()
)
zyClusterCandidateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterCandidateName.setStatus("current")
_ZyClusterCandidateModel_Type = DisplayString
_ZyClusterCandidateModel_Object = MibTableColumn
zyClusterCandidateModel = _ZyClusterCandidateModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 1, 1, 1, 3),
    _ZyClusterCandidateModel_Type()
)
zyClusterCandidateModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterCandidateModel.setStatus("current")


class _ZyClusterRole_Type(Integer32):
    """Custom type zyClusterRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manager", 1),
          ("member", 2),
          ("none", 0))
    )


_ZyClusterRole_Type.__name__ = "Integer32"
_ZyClusterRole_Object = MibScalar
zyClusterRole = _ZyClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 2),
    _ZyClusterRole_Type()
)
zyClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterRole.setStatus("current")
_ZyClusterInfoManager_Type = DisplayString
_ZyClusterInfoManager_Object = MibScalar
zyClusterInfoManager = _ZyClusterInfoManager_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 3),
    _ZyClusterInfoManager_Type()
)
zyClusterInfoManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterInfoManager.setStatus("current")
_ZyxelClusterInfoMemberTable_Object = MibTable
zyxelClusterInfoMemberTable = _ZyxelClusterInfoMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 4)
)
if mibBuilder.loadTexts:
    zyxelClusterInfoMemberTable.setStatus("current")
_ZyxelClusterInfoMemberEntry_Object = MibTableRow
zyxelClusterInfoMemberEntry = _ZyxelClusterInfoMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 4, 1)
)
zyxelClusterInfoMemberEntry.setIndexNames(
    (0, "ZYXEL-CLUSTER-MIB", "zyClusterInfoMemberMacAddress"),
)
if mibBuilder.loadTexts:
    zyxelClusterInfoMemberEntry.setStatus("current")
_ZyClusterInfoMemberMacAddress_Type = MacAddress
_ZyClusterInfoMemberMacAddress_Object = MibTableColumn
zyClusterInfoMemberMacAddress = _ZyClusterInfoMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 4, 1, 1),
    _ZyClusterInfoMemberMacAddress_Type()
)
zyClusterInfoMemberMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyClusterInfoMemberMacAddress.setStatus("current")
_ZyClusterInfoMemberName_Type = DisplayString
_ZyClusterInfoMemberName_Object = MibTableColumn
zyClusterInfoMemberName = _ZyClusterInfoMemberName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 4, 1, 2),
    _ZyClusterInfoMemberName_Type()
)
zyClusterInfoMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterInfoMemberName.setStatus("current")
_ZyClusterInfoMemberModel_Type = DisplayString
_ZyClusterInfoMemberModel_Object = MibTableColumn
zyClusterInfoMemberModel = _ZyClusterInfoMemberModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 4, 1, 3),
    _ZyClusterInfoMemberModel_Type()
)
zyClusterInfoMemberModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterInfoMemberModel.setStatus("current")


class _ZyClusterInfoMemberStatus_Type(Integer32):
    """Custom type zyClusterInfoMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("offline", 2),
          ("online", 1))
    )


_ZyClusterInfoMemberStatus_Type.__name__ = "Integer32"
_ZyClusterInfoMemberStatus_Object = MibTableColumn
zyClusterInfoMemberStatus = _ZyClusterInfoMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 14, 2, 4, 1, 4),
    _ZyClusterInfoMemberStatus_Type()
)
zyClusterInfoMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyClusterInfoMemberStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-CLUSTER-MIB",
    **{"zyxelCluster": zyxelCluster,
       "zyxelClusterSetup": zyxelClusterSetup,
       "zyxelClusterManager": zyxelClusterManager,
       "zyClusterManagerMaxNumberOfManagers": zyClusterManagerMaxNumberOfManagers,
       "zyxelClusterManagerTable": zyxelClusterManagerTable,
       "zyxelClusterManagerEntry": zyxelClusterManagerEntry,
       "zyClusterManagerVid": zyClusterManagerVid,
       "zyClusterManagerName": zyClusterManagerName,
       "zyClusterManagerRowStatus": zyClusterManagerRowStatus,
       "zyxelClusterMembers": zyxelClusterMembers,
       "zyClusterMemberMaxNumberOfMembers": zyClusterMemberMaxNumberOfMembers,
       "zyxelClusterMemberTable": zyxelClusterMemberTable,
       "zyxelClusterMemberEntry": zyxelClusterMemberEntry,
       "zyClusterMemberMacAddress": zyClusterMemberMacAddress,
       "zyClusterMemberName": zyClusterMemberName,
       "zyClusterMemberModel": zyClusterMemberModel,
       "zyClusterMemberPassword": zyClusterMemberPassword,
       "zyClusterMemberRowStatus": zyClusterMemberRowStatus,
       "zyxelClusterStatus": zyxelClusterStatus,
       "zyxelClusterCandidate": zyxelClusterCandidate,
       "zyxelClusterCandidateTable": zyxelClusterCandidateTable,
       "zyxelClusterCandidateEntry": zyxelClusterCandidateEntry,
       "zyClusterCandidateMacAddress": zyClusterCandidateMacAddress,
       "zyClusterCandidateName": zyClusterCandidateName,
       "zyClusterCandidateModel": zyClusterCandidateModel,
       "zyClusterRole": zyClusterRole,
       "zyClusterInfoManager": zyClusterInfoManager,
       "zyxelClusterInfoMemberTable": zyxelClusterInfoMemberTable,
       "zyxelClusterInfoMemberEntry": zyxelClusterInfoMemberEntry,
       "zyClusterInfoMemberMacAddress": zyClusterInfoMemberMacAddress,
       "zyClusterInfoMemberName": zyClusterInfoMemberName,
       "zyClusterInfoMemberModel": zyClusterInfoMemberModel,
       "zyClusterInfoMemberStatus": zyClusterInfoMemberStatus}
)
