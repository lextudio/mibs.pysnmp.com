# SNMP MIB module (EQLACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:57 2024
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

(UTFString,
 eqlGroupId,
 eqlStorageGroupAdminAccountIndex) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString",
    "eqlGroupId",
    "eqlStorageGroupAdminAccountIndex")

(ACLAppliesTo,
 eqliscsiLocalMemberId,
 eqliscsiVolumeIndex) = mibBuilder.importSymbols(
    "EQLVOLUME-MIB",
    "ACLAppliesTo",
    "eqliscsiLocalMemberId",
    "eqliscsiVolumeIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqlAccessModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 24)
)
eqlAccessModule.setRevisions(
        ("2012-05-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqlAccessObjects_ObjectIdentity = ObjectIdentity
eqlAccessObjects = _EqlAccessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1)
)
_EqlAccessGroupTable_Object = MibTable
eqlAccessGroupTable = _EqlAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1)
)
if mibBuilder.loadTexts:
    eqlAccessGroupTable.setStatus("current")
_EqlAccessGroupEntry_Object = MibTableRow
eqlAccessGroupEntry = _EqlAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1)
)
eqlAccessGroupEntry.setIndexNames(
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
)
if mibBuilder.loadTexts:
    eqlAccessGroupEntry.setStatus("current")
_EqlAccessGroupIndex_Type = Unsigned32
_EqlAccessGroupIndex_Object = MibTableColumn
eqlAccessGroupIndex = _EqlAccessGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 1),
    _EqlAccessGroupIndex_Type()
)
eqlAccessGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlAccessGroupIndex.setStatus("current")
_EqlAccessGroupRowStatus_Type = RowStatus
_EqlAccessGroupRowStatus_Object = MibTableColumn
eqlAccessGroupRowStatus = _EqlAccessGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 2),
    _EqlAccessGroupRowStatus_Type()
)
eqlAccessGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupRowStatus.setStatus("current")


class _EqlAccessGroupUUID_Type(UTFString):
    """Custom type eqlAccessGroupUUID based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlAccessGroupUUID_Type.__name__ = "UTFString"
_EqlAccessGroupUUID_Object = MibTableColumn
eqlAccessGroupUUID = _EqlAccessGroupUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 3),
    _EqlAccessGroupUUID_Type()
)
eqlAccessGroupUUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupUUID.setStatus("current")


class _EqlAccessGroupName_Type(UTFString):
    """Custom type eqlAccessGroupName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlAccessGroupName_Type.__name__ = "UTFString"
_EqlAccessGroupName_Object = MibTableColumn
eqlAccessGroupName = _EqlAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 4),
    _EqlAccessGroupName_Type()
)
eqlAccessGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupName.setStatus("current")


class _EqlAccessGroupKeyName_Type(UTFString):
    """Custom type eqlAccessGroupKeyName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlAccessGroupKeyName_Type.__name__ = "UTFString"
_EqlAccessGroupKeyName_Object = MibTableColumn
eqlAccessGroupKeyName = _EqlAccessGroupKeyName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 5),
    _EqlAccessGroupKeyName_Type()
)
eqlAccessGroupKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAccessGroupKeyName.setStatus("current")


class _EqlAccessGroupDescription_Type(UTFString):
    """Custom type eqlAccessGroupDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlAccessGroupDescription_Type.__name__ = "UTFString"
_EqlAccessGroupDescription_Object = MibTableColumn
eqlAccessGroupDescription = _EqlAccessGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 6),
    _EqlAccessGroupDescription_Type()
)
eqlAccessGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupDescription.setStatus("current")


class _EqlAccessGroupAdminKey_Type(Unsigned32):
    """Custom type eqlAccessGroupAdminKey based on Unsigned32"""
    defaultValue = 0


_EqlAccessGroupAdminKey_Object = MibTableColumn
eqlAccessGroupAdminKey = _EqlAccessGroupAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 7),
    _EqlAccessGroupAdminKey_Type()
)
eqlAccessGroupAdminKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupAdminKey.setStatus("current")


class _EqlAccessGroupType_Type(Integer32):
    """Custom type eqlAccessGroupType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access-group", 1),
          ("access-record", 2))
    )


_EqlAccessGroupType_Type.__name__ = "Integer32"
_EqlAccessGroupType_Object = MibTableColumn
eqlAccessGroupType = _EqlAccessGroupType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 8),
    _EqlAccessGroupType_Type()
)
eqlAccessGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupType.setStatus("current")


class _EqlAccessGroupPrivacyFlag_Type(Integer32):
    """Custom type eqlAccessGroupPrivacyFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_EqlAccessGroupPrivacyFlag_Type.__name__ = "Integer32"
_EqlAccessGroupPrivacyFlag_Object = MibTableColumn
eqlAccessGroupPrivacyFlag = _EqlAccessGroupPrivacyFlag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 1, 1, 9),
    _EqlAccessGroupPrivacyFlag_Type()
)
eqlAccessGroupPrivacyFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupPrivacyFlag.setStatus("current")
_EqlAccessGroupByTypeTable_Object = MibTable
eqlAccessGroupByTypeTable = _EqlAccessGroupByTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 2)
)
if mibBuilder.loadTexts:
    eqlAccessGroupByTypeTable.setStatus("current")
_EqlAccessGroupByTypeEntry_Object = MibTableRow
eqlAccessGroupByTypeEntry = _EqlAccessGroupByTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1)
)
eqlAccessGroupByTypeEntry.setIndexNames(
    (0, "EQLACCESS-MIB", "eqlAccessGroupType"),
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
)
if mibBuilder.loadTexts:
    eqlAccessGroupByTypeEntry.setStatus("current")


class _EqlAccessGroupByTypeUUID_Type(UTFString):
    """Custom type eqlAccessGroupByTypeUUID based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlAccessGroupByTypeUUID_Type.__name__ = "UTFString"
_EqlAccessGroupByTypeUUID_Object = MibTableColumn
eqlAccessGroupByTypeUUID = _EqlAccessGroupByTypeUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1, 1),
    _EqlAccessGroupByTypeUUID_Type()
)
eqlAccessGroupByTypeUUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupByTypeUUID.setStatus("current")


class _EqlAccessGroupByTypeName_Type(UTFString):
    """Custom type eqlAccessGroupByTypeName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlAccessGroupByTypeName_Type.__name__ = "UTFString"
_EqlAccessGroupByTypeName_Object = MibTableColumn
eqlAccessGroupByTypeName = _EqlAccessGroupByTypeName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1, 2),
    _EqlAccessGroupByTypeName_Type()
)
eqlAccessGroupByTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupByTypeName.setStatus("current")


class _EqlAccessGroupByTypeDescription_Type(UTFString):
    """Custom type eqlAccessGroupByTypeDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlAccessGroupByTypeDescription_Type.__name__ = "UTFString"
_EqlAccessGroupByTypeDescription_Object = MibTableColumn
eqlAccessGroupByTypeDescription = _EqlAccessGroupByTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1, 3),
    _EqlAccessGroupByTypeDescription_Type()
)
eqlAccessGroupByTypeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupByTypeDescription.setStatus("current")


class _EqlAccessGroupByTypeAdminKey_Type(Unsigned32):
    """Custom type eqlAccessGroupByTypeAdminKey based on Unsigned32"""
    defaultValue = 0


_EqlAccessGroupByTypeAdminKey_Object = MibTableColumn
eqlAccessGroupByTypeAdminKey = _EqlAccessGroupByTypeAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 2, 1, 4),
    _EqlAccessGroupByTypeAdminKey_Type()
)
eqlAccessGroupByTypeAdminKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupByTypeAdminKey.setStatus("current")
_EqlAccessGroupMemberTable_Object = MibTable
eqlAccessGroupMemberTable = _EqlAccessGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 3)
)
if mibBuilder.loadTexts:
    eqlAccessGroupMemberTable.setStatus("current")
_EqlAccessGroupMemberEntry_Object = MibTableRow
eqlAccessGroupMemberEntry = _EqlAccessGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 3, 1)
)
eqlAccessGroupMemberEntry.setIndexNames(
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
    (0, "EQLACCESS-MIB", "eqlAccessGroupChildIndex"),
)
if mibBuilder.loadTexts:
    eqlAccessGroupMemberEntry.setStatus("current")
_EqlAccessGroupChildIndex_Type = Unsigned32
_EqlAccessGroupChildIndex_Object = MibTableColumn
eqlAccessGroupChildIndex = _EqlAccessGroupChildIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 3, 1, 1),
    _EqlAccessGroupChildIndex_Type()
)
eqlAccessGroupChildIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupChildIndex.setStatus("current")
_EqlAccessGroupMemberRowStatus_Type = RowStatus
_EqlAccessGroupMemberRowStatus_Object = MibTableColumn
eqlAccessGroupMemberRowStatus = _EqlAccessGroupMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 3, 1, 2),
    _EqlAccessGroupMemberRowStatus_Type()
)
eqlAccessGroupMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupMemberRowStatus.setStatus("current")
_EqlAccessPointTable_Object = MibTable
eqlAccessPointTable = _EqlAccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 4)
)
if mibBuilder.loadTexts:
    eqlAccessPointTable.setStatus("current")
_EqlAccessPointEntry_Object = MibTableRow
eqlAccessPointEntry = _EqlAccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1)
)
eqlAccessPointEntry.setIndexNames(
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
    (0, "EQLACCESS-MIB", "eqlAccessPointIndex"),
)
if mibBuilder.loadTexts:
    eqlAccessPointEntry.setStatus("current")
_EqlAccessPointIndex_Type = Unsigned32
_EqlAccessPointIndex_Object = MibTableColumn
eqlAccessPointIndex = _EqlAccessPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 1),
    _EqlAccessPointIndex_Type()
)
eqlAccessPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlAccessPointIndex.setStatus("current")
_EqlAccessPointRowStatus_Type = RowStatus
_EqlAccessPointRowStatus_Object = MibTableColumn
eqlAccessPointRowStatus = _EqlAccessPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 2),
    _EqlAccessPointRowStatus_Type()
)
eqlAccessPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessPointRowStatus.setStatus("current")


class _EqlAccessPointInitiatorName_Type(UTFString):
    """Custom type eqlAccessPointInitiatorName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqlAccessPointInitiatorName_Type.__name__ = "UTFString"
_EqlAccessPointInitiatorName_Object = MibTableColumn
eqlAccessPointInitiatorName = _EqlAccessPointInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 3),
    _EqlAccessPointInitiatorName_Type()
)
eqlAccessPointInitiatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessPointInitiatorName.setStatus("current")


class _EqlAccessPointInitiatorCHAPUserName_Type(UTFString):
    """Custom type eqlAccessPointInitiatorCHAPUserName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlAccessPointInitiatorCHAPUserName_Type.__name__ = "UTFString"
_EqlAccessPointInitiatorCHAPUserName_Object = MibTableColumn
eqlAccessPointInitiatorCHAPUserName = _EqlAccessPointInitiatorCHAPUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 4),
    _EqlAccessPointInitiatorCHAPUserName_Type()
)
eqlAccessPointInitiatorCHAPUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessPointInitiatorCHAPUserName.setStatus("current")


class _EqlAccessPointDescription_Type(UTFString):
    """Custom type eqlAccessPointDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlAccessPointDescription_Type.__name__ = "UTFString"
_EqlAccessPointDescription_Object = MibTableColumn
eqlAccessPointDescription = _EqlAccessPointDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 4, 1, 5),
    _EqlAccessPointDescription_Type()
)
eqlAccessPointDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessPointDescription.setStatus("current")
_EqlAccessPointAddrTable_Object = MibTable
eqlAccessPointAddrTable = _EqlAccessPointAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 5)
)
if mibBuilder.loadTexts:
    eqlAccessPointAddrTable.setStatus("current")
_EqlAccessPointAddrEntry_Object = MibTableRow
eqlAccessPointAddrEntry = _EqlAccessPointAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1)
)
eqlAccessPointAddrEntry.setIndexNames(
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
    (0, "EQLACCESS-MIB", "eqlAccessPointIndex"),
    (0, "EQLACCESS-MIB", "eqlAccessPointAddrIndex"),
)
if mibBuilder.loadTexts:
    eqlAccessPointAddrEntry.setStatus("current")
_EqlAccessPointAddrIndex_Type = Unsigned32
_EqlAccessPointAddrIndex_Object = MibTableColumn
eqlAccessPointAddrIndex = _EqlAccessPointAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 1),
    _EqlAccessPointAddrIndex_Type()
)
eqlAccessPointAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlAccessPointAddrIndex.setStatus("current")
_EqlAccessPointAddrRowStatus_Type = RowStatus
_EqlAccessPointAddrRowStatus_Object = MibTableColumn
eqlAccessPointAddrRowStatus = _EqlAccessPointAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 2),
    _EqlAccessPointAddrRowStatus_Type()
)
eqlAccessPointAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessPointAddrRowStatus.setStatus("current")


class _EqlAccessPointAddrInitiatorAddrType_Type(InetAddressType):
    """Custom type eqlAccessPointAddrInitiatorAddrType based on InetAddressType"""


_EqlAccessPointAddrInitiatorAddrType_Object = MibTableColumn
eqlAccessPointAddrInitiatorAddrType = _EqlAccessPointAddrInitiatorAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 3),
    _EqlAccessPointAddrInitiatorAddrType_Type()
)
eqlAccessPointAddrInitiatorAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessPointAddrInitiatorAddrType.setStatus("current")
_EqlAccessPointAddrInitiatorAddr_Type = InetAddress
_EqlAccessPointAddrInitiatorAddr_Object = MibTableColumn
eqlAccessPointAddrInitiatorAddr = _EqlAccessPointAddrInitiatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 4),
    _EqlAccessPointAddrInitiatorAddr_Type()
)
eqlAccessPointAddrInitiatorAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessPointAddrInitiatorAddr.setStatus("current")


class _EqlAccessPointAddrInitiatorAddrWildcardType_Type(InetAddressType):
    """Custom type eqlAccessPointAddrInitiatorAddrWildcardType based on InetAddressType"""


_EqlAccessPointAddrInitiatorAddrWildcardType_Object = MibTableColumn
eqlAccessPointAddrInitiatorAddrWildcardType = _EqlAccessPointAddrInitiatorAddrWildcardType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 5),
    _EqlAccessPointAddrInitiatorAddrWildcardType_Type()
)
eqlAccessPointAddrInitiatorAddrWildcardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessPointAddrInitiatorAddrWildcardType.setStatus("current")
_EqlAccessPointAddrInitiatorAddrWildcard_Type = InetAddress
_EqlAccessPointAddrInitiatorAddrWildcard_Object = MibTableColumn
eqlAccessPointAddrInitiatorAddrWildcard = _EqlAccessPointAddrInitiatorAddrWildcard_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 5, 1, 6),
    _EqlAccessPointAddrInitiatorAddrWildcard_Type()
)
eqlAccessPointAddrInitiatorAddrWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessPointAddrInitiatorAddrWildcard.setStatus("current")
_EqlAccessGroupObjectAssocTable_Object = MibTable
eqlAccessGroupObjectAssocTable = _EqlAccessGroupObjectAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 6)
)
if mibBuilder.loadTexts:
    eqlAccessGroupObjectAssocTable.setStatus("current")
_EqlAccessGroupObjectAssocEntry_Object = MibTableRow
eqlAccessGroupObjectAssocEntry = _EqlAccessGroupObjectAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1)
)
eqlAccessGroupObjectAssocEntry.setIndexNames(
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
    (0, "EQLACCESS-MIB", "eqlAccessGroupObjectAssocIndex"),
)
if mibBuilder.loadTexts:
    eqlAccessGroupObjectAssocEntry.setStatus("current")
_EqlAccessGroupObjectAssocIndex_Type = Unsigned32
_EqlAccessGroupObjectAssocIndex_Object = MibTableColumn
eqlAccessGroupObjectAssocIndex = _EqlAccessGroupObjectAssocIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 1),
    _EqlAccessGroupObjectAssocIndex_Type()
)
eqlAccessGroupObjectAssocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlAccessGroupObjectAssocIndex.setStatus("current")
_EqlAccessGroupObjectAssocRowStatus_Type = RowStatus
_EqlAccessGroupObjectAssocRowStatus_Object = MibTableColumn
eqlAccessGroupObjectAssocRowStatus = _EqlAccessGroupObjectAssocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 2),
    _EqlAccessGroupObjectAssocRowStatus_Type()
)
eqlAccessGroupObjectAssocRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupObjectAssocRowStatus.setStatus("current")
_EqlAccessGroupObjectAssocOID_Type = RowPointer
_EqlAccessGroupObjectAssocOID_Object = MibTableColumn
eqlAccessGroupObjectAssocOID = _EqlAccessGroupObjectAssocOID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 3),
    _EqlAccessGroupObjectAssocOID_Type()
)
eqlAccessGroupObjectAssocOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupObjectAssocOID.setStatus("current")
_EqlAccessGroupObjectAssocFlag_Type = ACLAppliesTo
_EqlAccessGroupObjectAssocFlag_Object = MibTableColumn
eqlAccessGroupObjectAssocFlag = _EqlAccessGroupObjectAssocFlag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 4),
    _EqlAccessGroupObjectAssocFlag_Type()
)
eqlAccessGroupObjectAssocFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupObjectAssocFlag.setStatus("current")


class _EqlAccessGroupObjectAssocCreator_Type(Integer32):
    """Custom type eqlAccessGroupObjectAssocCreator based on Integer32"""
    defaultValue = 4

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
        *(("cli", 3),
          ("gui", 2),
          ("other", 4),
          ("vCenter", 1))
    )


_EqlAccessGroupObjectAssocCreator_Type.__name__ = "Integer32"
_EqlAccessGroupObjectAssocCreator_Object = MibTableColumn
eqlAccessGroupObjectAssocCreator = _EqlAccessGroupObjectAssocCreator_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 6, 1, 5),
    _EqlAccessGroupObjectAssocCreator_Type()
)
eqlAccessGroupObjectAssocCreator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlAccessGroupObjectAssocCreator.setStatus("current")
_EqlAccessGroupVolumeAssocTable_Object = MibTable
eqlAccessGroupVolumeAssocTable = _EqlAccessGroupVolumeAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 7)
)
if mibBuilder.loadTexts:
    eqlAccessGroupVolumeAssocTable.setStatus("current")
_EqlAccessGroupVolumeAssocEntry_Object = MibTableRow
eqlAccessGroupVolumeAssocEntry = _EqlAccessGroupVolumeAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 7, 1)
)
eqlAccessGroupVolumeAssocEntry.setIndexNames(
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlAccessGroupVolumeAssocEntry.setStatus("current")
_EqlAccessGroupVolumeAssocFlag_Type = ACLAppliesTo
_EqlAccessGroupVolumeAssocFlag_Object = MibTableColumn
eqlAccessGroupVolumeAssocFlag = _EqlAccessGroupVolumeAssocFlag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 7, 1, 1),
    _EqlAccessGroupVolumeAssocFlag_Type()
)
eqlAccessGroupVolumeAssocFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAccessGroupVolumeAssocFlag.setStatus("current")
_EqlAccessGroupVolumeAssocObjectIndex_Type = Unsigned32
_EqlAccessGroupVolumeAssocObjectIndex_Object = MibTableColumn
eqlAccessGroupVolumeAssocObjectIndex = _EqlAccessGroupVolumeAssocObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 7, 1, 2),
    _EqlAccessGroupVolumeAssocObjectIndex_Type()
)
eqlAccessGroupVolumeAssocObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAccessGroupVolumeAssocObjectIndex.setStatus("current")
_EqlVolumeAccessGroupAssocTable_Object = MibTable
eqlVolumeAccessGroupAssocTable = _EqlVolumeAccessGroupAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 8)
)
if mibBuilder.loadTexts:
    eqlVolumeAccessGroupAssocTable.setStatus("current")
_EqlVolumeAccessGroupAssocEntry_Object = MibTableRow
eqlVolumeAccessGroupAssocEntry = _EqlVolumeAccessGroupAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 8, 1)
)
eqlVolumeAccessGroupAssocEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
)
if mibBuilder.loadTexts:
    eqlVolumeAccessGroupAssocEntry.setStatus("current")
_EqlVolumeAccessGroupAssocFlag_Type = ACLAppliesTo
_EqlVolumeAccessGroupAssocFlag_Object = MibTableColumn
eqlVolumeAccessGroupAssocFlag = _EqlVolumeAccessGroupAssocFlag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 8, 1, 1),
    _EqlVolumeAccessGroupAssocFlag_Type()
)
eqlVolumeAccessGroupAssocFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolumeAccessGroupAssocFlag.setStatus("current")
_EqlVolumeAccessGroupAssocObjectIndex_Type = Unsigned32
_EqlVolumeAccessGroupAssocObjectIndex_Object = MibTableColumn
eqlVolumeAccessGroupAssocObjectIndex = _EqlVolumeAccessGroupAssocObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 8, 1, 2),
    _EqlVolumeAccessGroupAssocObjectIndex_Type()
)
eqlVolumeAccessGroupAssocObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolumeAccessGroupAssocObjectIndex.setStatus("current")
_EqlAccessGroupSharedVolumeAssocTable_Object = MibTable
eqlAccessGroupSharedVolumeAssocTable = _EqlAccessGroupSharedVolumeAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 9)
)
if mibBuilder.loadTexts:
    eqlAccessGroupSharedVolumeAssocTable.setStatus("current")
_EqlAccessGroupSharedVolumeAssocEntry_Object = MibTableRow
eqlAccessGroupSharedVolumeAssocEntry = _EqlAccessGroupSharedVolumeAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 9, 1)
)
eqlAccessGroupSharedVolumeAssocEntry.setIndexNames(
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlAccessGroupSharedVolumeAssocEntry.setStatus("current")
_EqlAccessGroupSharedVolumeAssocFlag_Type = ACLAppliesTo
_EqlAccessGroupSharedVolumeAssocFlag_Object = MibTableColumn
eqlAccessGroupSharedVolumeAssocFlag = _EqlAccessGroupSharedVolumeAssocFlag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 9, 1, 1),
    _EqlAccessGroupSharedVolumeAssocFlag_Type()
)
eqlAccessGroupSharedVolumeAssocFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAccessGroupSharedVolumeAssocFlag.setStatus("current")
_EqlAccessGroupSharedVolumeAssocObjectIndex_Type = Unsigned32
_EqlAccessGroupSharedVolumeAssocObjectIndex_Object = MibTableColumn
eqlAccessGroupSharedVolumeAssocObjectIndex = _EqlAccessGroupSharedVolumeAssocObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 9, 1, 2),
    _EqlAccessGroupSharedVolumeAssocObjectIndex_Type()
)
eqlAccessGroupSharedVolumeAssocObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAccessGroupSharedVolumeAssocObjectIndex.setStatus("current")
_EqlSharedVolumeAccessGroupAssocTable_Object = MibTable
eqlSharedVolumeAccessGroupAssocTable = _EqlSharedVolumeAccessGroupAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 10)
)
if mibBuilder.loadTexts:
    eqlSharedVolumeAccessGroupAssocTable.setStatus("current")
_EqlSharedVolumeAccessGroupAssocEntry_Object = MibTableRow
eqlSharedVolumeAccessGroupAssocEntry = _EqlSharedVolumeAccessGroupAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 10, 1)
)
eqlSharedVolumeAccessGroupAssocEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
)
if mibBuilder.loadTexts:
    eqlSharedVolumeAccessGroupAssocEntry.setStatus("current")
_EqlSharedVolumeAccessGroupAssocFlag_Type = ACLAppliesTo
_EqlSharedVolumeAccessGroupAssocFlag_Object = MibTableColumn
eqlSharedVolumeAccessGroupAssocFlag = _EqlSharedVolumeAccessGroupAssocFlag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 10, 1, 1),
    _EqlSharedVolumeAccessGroupAssocFlag_Type()
)
eqlSharedVolumeAccessGroupAssocFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSharedVolumeAccessGroupAssocFlag.setStatus("current")
_EqlSharedVolumeAccessGroupAssocObjectIndex_Type = Unsigned32
_EqlSharedVolumeAccessGroupAssocObjectIndex_Object = MibTableColumn
eqlSharedVolumeAccessGroupAssocObjectIndex = _EqlSharedVolumeAccessGroupAssocObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 10, 1, 2),
    _EqlSharedVolumeAccessGroupAssocObjectIndex_Type()
)
eqlSharedVolumeAccessGroupAssocObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlSharedVolumeAccessGroupAssocObjectIndex.setStatus("current")
_EqlAdminAccountAccessGroupTable_Object = MibTable
eqlAdminAccountAccessGroupTable = _EqlAdminAccountAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 11)
)
if mibBuilder.loadTexts:
    eqlAdminAccountAccessGroupTable.setStatus("current")
_EqlAdminAccountAccessGroupEntry_Object = MibTableRow
eqlAdminAccountAccessGroupEntry = _EqlAdminAccountAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 11, 1)
)
eqlAdminAccountAccessGroupEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
    (0, "EQLACCESS-MIB", "eqlAccessGroupIndex"),
)
if mibBuilder.loadTexts:
    eqlAdminAccountAccessGroupEntry.setStatus("current")
_EqlAdminAccountAccessGroupRowStatus_Type = RowStatus
_EqlAdminAccountAccessGroupRowStatus_Object = MibTableColumn
eqlAdminAccountAccessGroupRowStatus = _EqlAdminAccountAccessGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 11, 1, 1),
    _EqlAdminAccountAccessGroupRowStatus_Type()
)
eqlAdminAccountAccessGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAdminAccountAccessGroupRowStatus.setStatus("current")


class _EqlAdminAccountAccessGroupAccess_Type(Integer32):
    """Custom type eqlAdminAccountAccessGroupAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_EqlAdminAccountAccessGroupAccess_Type.__name__ = "Integer32"
_EqlAdminAccountAccessGroupAccess_Object = MibTableColumn
eqlAdminAccountAccessGroupAccess = _EqlAdminAccountAccessGroupAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 11, 1, 2),
    _EqlAdminAccountAccessGroupAccess_Type()
)
eqlAdminAccountAccessGroupAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAdminAccountAccessGroupAccess.setStatus("current")
_EqlACLCountTable_Object = MibTable
eqlACLCountTable = _EqlACLCountTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12)
)
if mibBuilder.loadTexts:
    eqlACLCountTable.setStatus("current")
_EqlACLCountEntry_Object = MibTableRow
eqlACLCountEntry = _EqlACLCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1)
)
eqlACLCountEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
)
if mibBuilder.loadTexts:
    eqlACLCountEntry.setStatus("current")
_EqlACLCountUserDefined_Type = Unsigned32
_EqlACLCountUserDefined_Object = MibTableColumn
eqlACLCountUserDefined = _EqlACLCountUserDefined_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 1),
    _EqlACLCountUserDefined_Type()
)
eqlACLCountUserDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlACLCountUserDefined.setStatus("current")
_EqlACLCountMPIO_Type = Unsigned32
_EqlACLCountMPIO_Object = MibTableColumn
eqlACLCountMPIO = _EqlACLCountMPIO_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 2),
    _EqlACLCountMPIO_Type()
)
eqlACLCountMPIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlACLCountMPIO.setStatus("current")
_EqlACLCountTotal_Type = Unsigned32
_EqlACLCountTotal_Object = MibTableColumn
eqlACLCountTotal = _EqlACLCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 3),
    _EqlACLCountTotal_Type()
)
eqlACLCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlACLCountTotal.setStatus("current")
_EqlMaxAccessGroupCount_Type = Unsigned32
_EqlMaxAccessGroupCount_Object = MibTableColumn
eqlMaxAccessGroupCount = _EqlMaxAccessGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 4),
    _EqlMaxAccessGroupCount_Type()
)
eqlMaxAccessGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMaxAccessGroupCount.setStatus("current")
_EqlMaxAccessRecordCount_Type = Unsigned32
_EqlMaxAccessRecordCount_Object = MibTableColumn
eqlMaxAccessRecordCount = _EqlMaxAccessRecordCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 5),
    _EqlMaxAccessRecordCount_Type()
)
eqlMaxAccessRecordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMaxAccessRecordCount.setStatus("current")
_EqlMaxAccessPointCount_Type = Unsigned32
_EqlMaxAccessPointCount_Object = MibTableColumn
eqlMaxAccessPointCount = _EqlMaxAccessPointCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 6),
    _EqlMaxAccessPointCount_Type()
)
eqlMaxAccessPointCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMaxAccessPointCount.setStatus("current")
_EqlMaxAccessPointIPAddrCount_Type = Unsigned32
_EqlMaxAccessPointIPAddrCount_Object = MibTableColumn
eqlMaxAccessPointIPAddrCount = _EqlMaxAccessPointIPAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 7),
    _EqlMaxAccessPointIPAddrCount_Type()
)
eqlMaxAccessPointIPAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMaxAccessPointIPAddrCount.setStatus("current")
_EqlMaxAssociationCount_Type = Unsigned32
_EqlMaxAssociationCount_Object = MibTableColumn
eqlMaxAssociationCount = _EqlMaxAssociationCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 8),
    _EqlMaxAssociationCount_Type()
)
eqlMaxAssociationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlMaxAssociationCount.setStatus("current")
_EqlAccessGroupCount_Type = Unsigned32
_EqlAccessGroupCount_Object = MibTableColumn
eqlAccessGroupCount = _EqlAccessGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 9),
    _EqlAccessGroupCount_Type()
)
eqlAccessGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAccessGroupCount.setStatus("current")
_EqlAccessRecordCount_Type = Unsigned32
_EqlAccessRecordCount_Object = MibTableColumn
eqlAccessRecordCount = _EqlAccessRecordCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 10),
    _EqlAccessRecordCount_Type()
)
eqlAccessRecordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAccessRecordCount.setStatus("current")
_EqlAccessPointCount_Type = Unsigned32
_EqlAccessPointCount_Object = MibTableColumn
eqlAccessPointCount = _EqlAccessPointCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 11),
    _EqlAccessPointCount_Type()
)
eqlAccessPointCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAccessPointCount.setStatus("current")
_EqlAccessPointIPAddrCount_Type = Unsigned32
_EqlAccessPointIPAddrCount_Object = MibTableColumn
eqlAccessPointIPAddrCount = _EqlAccessPointIPAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 12),
    _EqlAccessPointIPAddrCount_Type()
)
eqlAccessPointIPAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAccessPointIPAddrCount.setStatus("current")
_EqlAssociationCount_Type = Unsigned32
_EqlAssociationCount_Object = MibTableColumn
eqlAssociationCount = _EqlAssociationCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 12, 1, 13),
    _EqlAssociationCount_Type()
)
eqlAssociationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAssociationCount.setStatus("current")
_EqlVolumeAccessGroupAssocCountTable_Object = MibTable
eqlVolumeAccessGroupAssocCountTable = _EqlVolumeAccessGroupAssocCountTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 13)
)
if mibBuilder.loadTexts:
    eqlVolumeAccessGroupAssocCountTable.setStatus("current")
_EqlVolumeAccessGroupAssocCountEntry_Object = MibTableRow
eqlVolumeAccessGroupAssocCountEntry = _EqlVolumeAccessGroupAssocCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 13, 1)
)
eqlVolumeAccessGroupAssocCountEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlVolumeAccessGroupAssocCountEntry.setStatus("current")
_EqlVolumeAccessGroupAssocCount_Type = Unsigned32
_EqlVolumeAccessGroupAssocCount_Object = MibTableColumn
eqlVolumeAccessGroupAssocCount = _EqlVolumeAccessGroupAssocCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 13, 1, 1),
    _EqlVolumeAccessGroupAssocCount_Type()
)
eqlVolumeAccessGroupAssocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolumeAccessGroupAssocCount.setStatus("current")
_EqlVolumeAccessRecordAssocCount_Type = Unsigned32
_EqlVolumeAccessRecordAssocCount_Object = MibTableColumn
eqlVolumeAccessRecordAssocCount = _EqlVolumeAccessRecordAssocCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 24, 1, 13, 1, 2),
    _EqlVolumeAccessRecordAssocCount_Type()
)
eqlVolumeAccessRecordAssocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVolumeAccessRecordAssocCount.setStatus("current")
_EqlAccessNotifications_ObjectIdentity = ObjectIdentity
eqlAccessNotifications = _EqlAccessNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 24, 2)
)
_EqlAccessConformance_ObjectIdentity = ObjectIdentity
eqlAccessConformance = _EqlAccessConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 24, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLACCESS-MIB",
    **{"eqlAccessModule": eqlAccessModule,
       "eqlAccessObjects": eqlAccessObjects,
       "eqlAccessGroupTable": eqlAccessGroupTable,
       "eqlAccessGroupEntry": eqlAccessGroupEntry,
       "eqlAccessGroupIndex": eqlAccessGroupIndex,
       "eqlAccessGroupRowStatus": eqlAccessGroupRowStatus,
       "eqlAccessGroupUUID": eqlAccessGroupUUID,
       "eqlAccessGroupName": eqlAccessGroupName,
       "eqlAccessGroupKeyName": eqlAccessGroupKeyName,
       "eqlAccessGroupDescription": eqlAccessGroupDescription,
       "eqlAccessGroupAdminKey": eqlAccessGroupAdminKey,
       "eqlAccessGroupType": eqlAccessGroupType,
       "eqlAccessGroupPrivacyFlag": eqlAccessGroupPrivacyFlag,
       "eqlAccessGroupByTypeTable": eqlAccessGroupByTypeTable,
       "eqlAccessGroupByTypeEntry": eqlAccessGroupByTypeEntry,
       "eqlAccessGroupByTypeUUID": eqlAccessGroupByTypeUUID,
       "eqlAccessGroupByTypeName": eqlAccessGroupByTypeName,
       "eqlAccessGroupByTypeDescription": eqlAccessGroupByTypeDescription,
       "eqlAccessGroupByTypeAdminKey": eqlAccessGroupByTypeAdminKey,
       "eqlAccessGroupMemberTable": eqlAccessGroupMemberTable,
       "eqlAccessGroupMemberEntry": eqlAccessGroupMemberEntry,
       "eqlAccessGroupChildIndex": eqlAccessGroupChildIndex,
       "eqlAccessGroupMemberRowStatus": eqlAccessGroupMemberRowStatus,
       "eqlAccessPointTable": eqlAccessPointTable,
       "eqlAccessPointEntry": eqlAccessPointEntry,
       "eqlAccessPointIndex": eqlAccessPointIndex,
       "eqlAccessPointRowStatus": eqlAccessPointRowStatus,
       "eqlAccessPointInitiatorName": eqlAccessPointInitiatorName,
       "eqlAccessPointInitiatorCHAPUserName": eqlAccessPointInitiatorCHAPUserName,
       "eqlAccessPointDescription": eqlAccessPointDescription,
       "eqlAccessPointAddrTable": eqlAccessPointAddrTable,
       "eqlAccessPointAddrEntry": eqlAccessPointAddrEntry,
       "eqlAccessPointAddrIndex": eqlAccessPointAddrIndex,
       "eqlAccessPointAddrRowStatus": eqlAccessPointAddrRowStatus,
       "eqlAccessPointAddrInitiatorAddrType": eqlAccessPointAddrInitiatorAddrType,
       "eqlAccessPointAddrInitiatorAddr": eqlAccessPointAddrInitiatorAddr,
       "eqlAccessPointAddrInitiatorAddrWildcardType": eqlAccessPointAddrInitiatorAddrWildcardType,
       "eqlAccessPointAddrInitiatorAddrWildcard": eqlAccessPointAddrInitiatorAddrWildcard,
       "eqlAccessGroupObjectAssocTable": eqlAccessGroupObjectAssocTable,
       "eqlAccessGroupObjectAssocEntry": eqlAccessGroupObjectAssocEntry,
       "eqlAccessGroupObjectAssocIndex": eqlAccessGroupObjectAssocIndex,
       "eqlAccessGroupObjectAssocRowStatus": eqlAccessGroupObjectAssocRowStatus,
       "eqlAccessGroupObjectAssocOID": eqlAccessGroupObjectAssocOID,
       "eqlAccessGroupObjectAssocFlag": eqlAccessGroupObjectAssocFlag,
       "eqlAccessGroupObjectAssocCreator": eqlAccessGroupObjectAssocCreator,
       "eqlAccessGroupVolumeAssocTable": eqlAccessGroupVolumeAssocTable,
       "eqlAccessGroupVolumeAssocEntry": eqlAccessGroupVolumeAssocEntry,
       "eqlAccessGroupVolumeAssocFlag": eqlAccessGroupVolumeAssocFlag,
       "eqlAccessGroupVolumeAssocObjectIndex": eqlAccessGroupVolumeAssocObjectIndex,
       "eqlVolumeAccessGroupAssocTable": eqlVolumeAccessGroupAssocTable,
       "eqlVolumeAccessGroupAssocEntry": eqlVolumeAccessGroupAssocEntry,
       "eqlVolumeAccessGroupAssocFlag": eqlVolumeAccessGroupAssocFlag,
       "eqlVolumeAccessGroupAssocObjectIndex": eqlVolumeAccessGroupAssocObjectIndex,
       "eqlAccessGroupSharedVolumeAssocTable": eqlAccessGroupSharedVolumeAssocTable,
       "eqlAccessGroupSharedVolumeAssocEntry": eqlAccessGroupSharedVolumeAssocEntry,
       "eqlAccessGroupSharedVolumeAssocFlag": eqlAccessGroupSharedVolumeAssocFlag,
       "eqlAccessGroupSharedVolumeAssocObjectIndex": eqlAccessGroupSharedVolumeAssocObjectIndex,
       "eqlSharedVolumeAccessGroupAssocTable": eqlSharedVolumeAccessGroupAssocTable,
       "eqlSharedVolumeAccessGroupAssocEntry": eqlSharedVolumeAccessGroupAssocEntry,
       "eqlSharedVolumeAccessGroupAssocFlag": eqlSharedVolumeAccessGroupAssocFlag,
       "eqlSharedVolumeAccessGroupAssocObjectIndex": eqlSharedVolumeAccessGroupAssocObjectIndex,
       "eqlAdminAccountAccessGroupTable": eqlAdminAccountAccessGroupTable,
       "eqlAdminAccountAccessGroupEntry": eqlAdminAccountAccessGroupEntry,
       "eqlAdminAccountAccessGroupRowStatus": eqlAdminAccountAccessGroupRowStatus,
       "eqlAdminAccountAccessGroupAccess": eqlAdminAccountAccessGroupAccess,
       "eqlACLCountTable": eqlACLCountTable,
       "eqlACLCountEntry": eqlACLCountEntry,
       "eqlACLCountUserDefined": eqlACLCountUserDefined,
       "eqlACLCountMPIO": eqlACLCountMPIO,
       "eqlACLCountTotal": eqlACLCountTotal,
       "eqlMaxAccessGroupCount": eqlMaxAccessGroupCount,
       "eqlMaxAccessRecordCount": eqlMaxAccessRecordCount,
       "eqlMaxAccessPointCount": eqlMaxAccessPointCount,
       "eqlMaxAccessPointIPAddrCount": eqlMaxAccessPointIPAddrCount,
       "eqlMaxAssociationCount": eqlMaxAssociationCount,
       "eqlAccessGroupCount": eqlAccessGroupCount,
       "eqlAccessRecordCount": eqlAccessRecordCount,
       "eqlAccessPointCount": eqlAccessPointCount,
       "eqlAccessPointIPAddrCount": eqlAccessPointIPAddrCount,
       "eqlAssociationCount": eqlAssociationCount,
       "eqlVolumeAccessGroupAssocCountTable": eqlVolumeAccessGroupAssocCountTable,
       "eqlVolumeAccessGroupAssocCountEntry": eqlVolumeAccessGroupAssocCountEntry,
       "eqlVolumeAccessGroupAssocCount": eqlVolumeAccessGroupAssocCount,
       "eqlVolumeAccessRecordAssocCount": eqlVolumeAccessRecordAssocCount,
       "eqlAccessNotifications": eqlAccessNotifications,
       "eqlAccessConformance": eqlAccessConformance}
)
