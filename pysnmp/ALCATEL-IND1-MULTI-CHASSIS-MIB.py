# SNMP MIB module (ALCATEL-IND1-MULTI-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-MULTI-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:03 2024
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

(softentIND1MultiChassisManager,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1MultiChassisManager")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

alcatelIND1MultiChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1)
)
alcatelIND1MultiChassisMIB.setRevisions(
        ("2009-11-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MultiChassisId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )



class MultiChassisLinkIfIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            40000128
        )
    )
    namedValues = NamedValues(
        ("link0", 40000128)
    )



class MultiChassisConsistency(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("consistent", 1),
          ("disabled", 3),
          ("inconsistent", 0),
          ("na", 2))
    )



class MultiChassisLocaleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("peer", 2))
    )



class MultiChassisGroup(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class MultiChassisType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("rushmore", 1),
          ("tor", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1MultiChassisMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1MultiChassisMIBNotifications = _AlcatelIND1MultiChassisMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1MultiChassisMIBNotifications.setStatus("current")
_AlcatelIND1MultiChassisMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1MultiChassisMIBObjects = _AlcatelIND1MultiChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MultiChassisMIBObjects.setStatus("current")
_MultiChassisConfig_ObjectIdentity = ObjectIdentity
multiChassisConfig = _MultiChassisConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 1)
)


class _MultiChassisConfigChassisId_Type(MultiChassisId):
    """Custom type multiChassisConfigChassisId based on MultiChassisId"""
    defaultValue = 0


_MultiChassisConfigChassisId_Object = MibScalar
multiChassisConfigChassisId = _MultiChassisConfigChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 1, 1),
    _MultiChassisConfigChassisId_Type()
)
multiChassisConfigChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiChassisConfigChassisId.setStatus("current")


class _MultiChassisConfigHelloInterval_Type(Integer32):
    """Custom type multiChassisConfigHelloInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MultiChassisConfigHelloInterval_Type.__name__ = "Integer32"
_MultiChassisConfigHelloInterval_Object = MibScalar
multiChassisConfigHelloInterval = _MultiChassisConfigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 1, 2),
    _MultiChassisConfigHelloInterval_Type()
)
multiChassisConfigHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiChassisConfigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    multiChassisConfigHelloInterval.setUnits("seconds")


class _MultiChassisConfigIpcVlan_Type(Integer32):
    """Custom type multiChassisConfigIpcVlan based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MultiChassisConfigIpcVlan_Type.__name__ = "Integer32"
_MultiChassisConfigIpcVlan_Object = MibScalar
multiChassisConfigIpcVlan = _MultiChassisConfigIpcVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 1, 3),
    _MultiChassisConfigIpcVlan_Type()
)
multiChassisConfigIpcVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiChassisConfigIpcVlan.setStatus("current")


class _MultiChassisConfigChassisGroup_Type(MultiChassisGroup):
    """Custom type multiChassisConfigChassisGroup based on MultiChassisGroup"""
    defaultValue = 0


_MultiChassisConfigChassisGroup_Object = MibScalar
multiChassisConfigChassisGroup = _MultiChassisConfigChassisGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 1, 4),
    _MultiChassisConfigChassisGroup_Type()
)
multiChassisConfigChassisGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiChassisConfigChassisGroup.setStatus("current")
_MultiChassisOperation_ObjectIdentity = ObjectIdentity
multiChassisOperation = _MultiChassisOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 2)
)


class _MultiChassisOperChassisId_Type(Integer32):
    """Custom type multiChassisOperChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MultiChassisOperChassisId_Type.__name__ = "Integer32"
_MultiChassisOperChassisId_Object = MibScalar
multiChassisOperChassisId = _MultiChassisOperChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 2, 1),
    _MultiChassisOperChassisId_Type()
)
multiChassisOperChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisOperChassisId.setStatus("current")


class _MultiChassisOperChassisRole_Type(Integer32):
    """Custom type multiChassisOperChassisRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inconsistent", 3),
          ("primary", 1),
          ("secondary", 2),
          ("unassigned", 0))
    )


_MultiChassisOperChassisRole_Type.__name__ = "Integer32"
_MultiChassisOperChassisRole_Object = MibScalar
multiChassisOperChassisRole = _MultiChassisOperChassisRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 2, 2),
    _MultiChassisOperChassisRole_Type()
)
multiChassisOperChassisRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisOperChassisRole.setStatus("current")


class _MultiChassisOperStatus_Type(Integer32):
    """Custom type multiChassisOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("inconsistent", 2),
          ("standalone", 3),
          ("up", 1))
    )


_MultiChassisOperStatus_Type.__name__ = "Integer32"
_MultiChassisOperStatus_Object = MibScalar
multiChassisOperStatus = _MultiChassisOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 2, 3),
    _MultiChassisOperStatus_Type()
)
multiChassisOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisOperStatus.setStatus("current")


class _MultiChassisOperHelloInterval_Type(Integer32):
    """Custom type multiChassisOperHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MultiChassisOperHelloInterval_Type.__name__ = "Integer32"
_MultiChassisOperHelloInterval_Object = MibScalar
multiChassisOperHelloInterval = _MultiChassisOperHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 2, 4),
    _MultiChassisOperHelloInterval_Type()
)
multiChassisOperHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisOperHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    multiChassisOperHelloInterval.setUnits("seconds")


class _MultiChassisOperIpcVlan_Type(Integer32):
    """Custom type multiChassisOperIpcVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MultiChassisOperIpcVlan_Type.__name__ = "Integer32"
_MultiChassisOperIpcVlan_Object = MibScalar
multiChassisOperIpcVlan = _MultiChassisOperIpcVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 2, 5),
    _MultiChassisOperIpcVlan_Type()
)
multiChassisOperIpcVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisOperIpcVlan.setStatus("current")
_MultiChassisOperChassisGroup_Type = MultiChassisGroup
_MultiChassisOperChassisGroup_Object = MibScalar
multiChassisOperChassisGroup = _MultiChassisOperChassisGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 2, 6),
    _MultiChassisOperChassisGroup_Type()
)
multiChassisOperChassisGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisOperChassisGroup.setStatus("current")
_MultiChassisOperChassisType_Type = MultiChassisType
_MultiChassisOperChassisType_Object = MibScalar
multiChassisOperChassisType = _MultiChassisOperChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 2, 7),
    _MultiChassisOperChassisType_Type()
)
multiChassisOperChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisOperChassisType.setStatus("current")
_MultiChassisLinkTable_Object = MibTable
multiChassisLinkTable = _MultiChassisLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3)
)
if mibBuilder.loadTexts:
    multiChassisLinkTable.setStatus("current")
_MultiChassisLinkEntry_Object = MibTableRow
multiChassisLinkEntry = _MultiChassisLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3, 1)
)
multiChassisLinkEntry.setIndexNames(
    (0, "ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkIfIndex"),
)
if mibBuilder.loadTexts:
    multiChassisLinkEntry.setStatus("current")
_MultiChassisLinkIfIndex_Type = MultiChassisLinkIfIndex
_MultiChassisLinkIfIndex_Object = MibTableColumn
multiChassisLinkIfIndex = _MultiChassisLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3, 1, 1),
    _MultiChassisLinkIfIndex_Type()
)
multiChassisLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiChassisLinkIfIndex.setStatus("current")


class _MultiChassisLinkAdminStatus_Type(Integer32):
    """Custom type multiChassisLinkAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MultiChassisLinkAdminStatus_Type.__name__ = "Integer32"
_MultiChassisLinkAdminStatus_Object = MibTableColumn
multiChassisLinkAdminStatus = _MultiChassisLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3, 1, 2),
    _MultiChassisLinkAdminStatus_Type()
)
multiChassisLinkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multiChassisLinkAdminStatus.setStatus("current")


class _MultiChassisLinkOperDefaultVlan_Type(Integer32):
    """Custom type multiChassisLinkOperDefaultVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MultiChassisLinkOperDefaultVlan_Type.__name__ = "Integer32"
_MultiChassisLinkOperDefaultVlan_Object = MibTableColumn
multiChassisLinkOperDefaultVlan = _MultiChassisLinkOperDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3, 1, 3),
    _MultiChassisLinkOperDefaultVlan_Type()
)
multiChassisLinkOperDefaultVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multiChassisLinkOperDefaultVlan.setStatus("current")


class _MultiChassisLinkOperStatus_Type(Integer32):
    """Custom type multiChassisLinkOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_MultiChassisLinkOperStatus_Type.__name__ = "Integer32"
_MultiChassisLinkOperStatus_Object = MibTableColumn
multiChassisLinkOperStatus = _MultiChassisLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3, 1, 4),
    _MultiChassisLinkOperStatus_Type()
)
multiChassisLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkOperStatus.setStatus("current")
_MultiChassisLinkPrimaryPort_Type = InterfaceIndex
_MultiChassisLinkPrimaryPort_Object = MibTableColumn
multiChassisLinkPrimaryPort = _MultiChassisLinkPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3, 1, 5),
    _MultiChassisLinkPrimaryPort_Type()
)
multiChassisLinkPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkPrimaryPort.setStatus("current")


class _MultiChassisLinkActivePortNum_Type(Integer32):
    """Custom type multiChassisLinkActivePortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MultiChassisLinkActivePortNum_Type.__name__ = "Integer32"
_MultiChassisLinkActivePortNum_Object = MibTableColumn
multiChassisLinkActivePortNum = _MultiChassisLinkActivePortNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3, 1, 6),
    _MultiChassisLinkActivePortNum_Type()
)
multiChassisLinkActivePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkActivePortNum.setStatus("current")


class _MultiChassisLinkConfigPortNum_Type(Integer32):
    """Custom type multiChassisLinkConfigPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MultiChassisLinkConfigPortNum_Type.__name__ = "Integer32"
_MultiChassisLinkConfigPortNum_Object = MibTableColumn
multiChassisLinkConfigPortNum = _MultiChassisLinkConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3, 1, 7),
    _MultiChassisLinkConfigPortNum_Type()
)
multiChassisLinkConfigPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkConfigPortNum.setStatus("current")
_MultiChassisLinkRowStatus_Type = RowStatus
_MultiChassisLinkRowStatus_Object = MibTableColumn
multiChassisLinkRowStatus = _MultiChassisLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 3, 1, 8),
    _MultiChassisLinkRowStatus_Type()
)
multiChassisLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multiChassisLinkRowStatus.setStatus("current")
_MultiChassisLinkMemberPortTable_Object = MibTable
multiChassisLinkMemberPortTable = _MultiChassisLinkMemberPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 4)
)
if mibBuilder.loadTexts:
    multiChassisLinkMemberPortTable.setStatus("current")
_MultiChassisLinkMemberPortEntry_Object = MibTableRow
multiChassisLinkMemberPortEntry = _MultiChassisLinkMemberPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 4, 1)
)
multiChassisLinkMemberPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkMemberPortLinkIfIndex"),
    (0, "ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkMemberPortIfindex"),
)
if mibBuilder.loadTexts:
    multiChassisLinkMemberPortEntry.setStatus("current")
_MultiChassisLinkMemberPortLinkIfIndex_Type = MultiChassisLinkIfIndex
_MultiChassisLinkMemberPortLinkIfIndex_Object = MibTableColumn
multiChassisLinkMemberPortLinkIfIndex = _MultiChassisLinkMemberPortLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 4, 1, 1),
    _MultiChassisLinkMemberPortLinkIfIndex_Type()
)
multiChassisLinkMemberPortLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiChassisLinkMemberPortLinkIfIndex.setStatus("current")
_MultiChassisLinkMemberPortIfindex_Type = InterfaceIndex
_MultiChassisLinkMemberPortIfindex_Object = MibTableColumn
multiChassisLinkMemberPortIfindex = _MultiChassisLinkMemberPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 4, 1, 2),
    _MultiChassisLinkMemberPortIfindex_Type()
)
multiChassisLinkMemberPortIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiChassisLinkMemberPortIfindex.setStatus("current")
_MultiChassisLinkMemberPortIsPrimay_Type = TruthValue
_MultiChassisLinkMemberPortIsPrimay_Object = MibTableColumn
multiChassisLinkMemberPortIsPrimay = _MultiChassisLinkMemberPortIsPrimay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 4, 1, 3),
    _MultiChassisLinkMemberPortIsPrimay_Type()
)
multiChassisLinkMemberPortIsPrimay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkMemberPortIsPrimay.setStatus("current")


class _MultiChassisLinkMemberOperStatus_Type(Integer32):
    """Custom type multiChassisLinkMemberOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_MultiChassisLinkMemberOperStatus_Type.__name__ = "Integer32"
_MultiChassisLinkMemberOperStatus_Object = MibTableColumn
multiChassisLinkMemberOperStatus = _MultiChassisLinkMemberOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 4, 1, 4),
    _MultiChassisLinkMemberOperStatus_Type()
)
multiChassisLinkMemberOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkMemberOperStatus.setStatus("current")
_MultiChassisLinkMemberPortRowStatus_Type = RowStatus
_MultiChassisLinkMemberPortRowStatus_Object = MibTableColumn
multiChassisLinkMemberPortRowStatus = _MultiChassisLinkMemberPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 4, 1, 5),
    _MultiChassisLinkMemberPortRowStatus_Type()
)
multiChassisLinkMemberPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multiChassisLinkMemberPortRowStatus.setStatus("current")
_MultiChassisLoopDetection_ObjectIdentity = ObjectIdentity
multiChassisLoopDetection = _MultiChassisLoopDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 5)
)


class _MultiChassisLoopDetectionAdminStatus_Type(Integer32):
    """Custom type multiChassisLoopDetectionAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MultiChassisLoopDetectionAdminStatus_Type.__name__ = "Integer32"
_MultiChassisLoopDetectionAdminStatus_Object = MibScalar
multiChassisLoopDetectionAdminStatus = _MultiChassisLoopDetectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 5, 1),
    _MultiChassisLoopDetectionAdminStatus_Type()
)
multiChassisLoopDetectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiChassisLoopDetectionAdminStatus.setStatus("current")


class _MultiChassisLoopDetectionTransmitInterval_Type(Integer32):
    """Custom type multiChassisLoopDetectionTransmitInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MultiChassisLoopDetectionTransmitInterval_Type.__name__ = "Integer32"
_MultiChassisLoopDetectionTransmitInterval_Object = MibScalar
multiChassisLoopDetectionTransmitInterval = _MultiChassisLoopDetectionTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 5, 2),
    _MultiChassisLoopDetectionTransmitInterval_Type()
)
multiChassisLoopDetectionTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiChassisLoopDetectionTransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    multiChassisLoopDetectionTransmitInterval.setUnits("seconds")


class _MultiChassisLoopDetectionTransmitCount_Type(Integer32):
    """Custom type multiChassisLoopDetectionTransmitCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MultiChassisLoopDetectionTransmitCount_Type.__name__ = "Integer32"
_MultiChassisLoopDetectionTransmitCount_Object = MibScalar
multiChassisLoopDetectionTransmitCount = _MultiChassisLoopDetectionTransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 5, 3),
    _MultiChassisLoopDetectionTransmitCount_Type()
)
multiChassisLoopDetectionTransmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLoopDetectionTransmitCount.setStatus("current")


class _MultiChassisLoopDetectionCount_Type(Integer32):
    """Custom type multiChassisLoopDetectionCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MultiChassisLoopDetectionCount_Type.__name__ = "Integer32"
_MultiChassisLoopDetectionCount_Object = MibScalar
multiChassisLoopDetectionCount = _MultiChassisLoopDetectionCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 5, 4),
    _MultiChassisLoopDetectionCount_Type()
)
multiChassisLoopDetectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLoopDetectionCount.setStatus("current")


class _MultiChassisLoopDetectionPortDownList_Type(SnmpAdminString):
    """Custom type multiChassisLoopDetectionPortDownList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MultiChassisLoopDetectionPortDownList_Type.__name__ = "SnmpAdminString"
_MultiChassisLoopDetectionPortDownList_Object = MibScalar
multiChassisLoopDetectionPortDownList = _MultiChassisLoopDetectionPortDownList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 5, 5),
    _MultiChassisLoopDetectionPortDownList_Type()
)
multiChassisLoopDetectionPortDownList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLoopDetectionPortDownList.setStatus("current")


class _MultiChassisLoopDetectionClear_Type(Integer32):
    """Custom type multiChassisLoopDetectionClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nonClear", 0))
    )


_MultiChassisLoopDetectionClear_Type.__name__ = "Integer32"
_MultiChassisLoopDetectionClear_Object = MibScalar
multiChassisLoopDetectionClear = _MultiChassisLoopDetectionClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 5, 6),
    _MultiChassisLoopDetectionClear_Type()
)
multiChassisLoopDetectionClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiChassisLoopDetectionClear.setStatus("current")
_MultiChassisGlobalConsistency_ObjectIdentity = ObjectIdentity
multiChassisGlobalConsistency = _MultiChassisGlobalConsistency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6)
)
_MultiChassisLocalChassisId_Type = MultiChassisId
_MultiChassisLocalChassisId_Object = MibScalar
multiChassisLocalChassisId = _MultiChassisLocalChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 1),
    _MultiChassisLocalChassisId_Type()
)
multiChassisLocalChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLocalChassisId.setStatus("current")
_MultiChassisPeerChassisId_Type = MultiChassisId
_MultiChassisPeerChassisId_Object = MibScalar
multiChassisPeerChassisId = _MultiChassisPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 2),
    _MultiChassisPeerChassisId_Type()
)
multiChassisPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisPeerChassisId.setStatus("current")
_MultiChassisIdConsistency_Type = MultiChassisConsistency
_MultiChassisIdConsistency_Object = MibScalar
multiChassisIdConsistency = _MultiChassisIdConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 3),
    _MultiChassisIdConsistency_Type()
)
multiChassisIdConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisIdConsistency.setStatus("current")


class _MultiChassisLocalHelloInterval_Type(Integer32):
    """Custom type multiChassisLocalHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MultiChassisLocalHelloInterval_Type.__name__ = "Integer32"
_MultiChassisLocalHelloInterval_Object = MibScalar
multiChassisLocalHelloInterval = _MultiChassisLocalHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 4),
    _MultiChassisLocalHelloInterval_Type()
)
multiChassisLocalHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLocalHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    multiChassisLocalHelloInterval.setUnits("seconds")


class _MultiChassisPeerHelloInterval_Type(Integer32):
    """Custom type multiChassisPeerHelloInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MultiChassisPeerHelloInterval_Type.__name__ = "Integer32"
_MultiChassisPeerHelloInterval_Object = MibScalar
multiChassisPeerHelloInterval = _MultiChassisPeerHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 5),
    _MultiChassisPeerHelloInterval_Type()
)
multiChassisPeerHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisPeerHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    multiChassisPeerHelloInterval.setUnits("seconds")
_MultiChassisHelloIntervalConsistency_Type = MultiChassisConsistency
_MultiChassisHelloIntervalConsistency_Object = MibScalar
multiChassisHelloIntervalConsistency = _MultiChassisHelloIntervalConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 6),
    _MultiChassisHelloIntervalConsistency_Type()
)
multiChassisHelloIntervalConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisHelloIntervalConsistency.setStatus("current")


class _MultiChassisLocalIpcVlan_Type(Integer32):
    """Custom type multiChassisLocalIpcVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MultiChassisLocalIpcVlan_Type.__name__ = "Integer32"
_MultiChassisLocalIpcVlan_Object = MibScalar
multiChassisLocalIpcVlan = _MultiChassisLocalIpcVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 7),
    _MultiChassisLocalIpcVlan_Type()
)
multiChassisLocalIpcVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLocalIpcVlan.setStatus("current")


class _MultiChassisPeerIpcVlan_Type(Integer32):
    """Custom type multiChassisPeerIpcVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MultiChassisPeerIpcVlan_Type.__name__ = "Integer32"
_MultiChassisPeerIpcVlan_Object = MibScalar
multiChassisPeerIpcVlan = _MultiChassisPeerIpcVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 8),
    _MultiChassisPeerIpcVlan_Type()
)
multiChassisPeerIpcVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisPeerIpcVlan.setStatus("current")
_MultiChassisIpcVlanConsistency_Type = MultiChassisConsistency
_MultiChassisIpcVlanConsistency_Object = MibScalar
multiChassisIpcVlanConsistency = _MultiChassisIpcVlanConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 9),
    _MultiChassisIpcVlanConsistency_Type()
)
multiChassisIpcVlanConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisIpcVlanConsistency.setStatus("current")


class _MultiChassisLocalStpPathCostMode_Type(Integer32):
    """Custom type multiChassisLocalStpPathCostMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("thrityTwoBit", 1))
    )


_MultiChassisLocalStpPathCostMode_Type.__name__ = "Integer32"
_MultiChassisLocalStpPathCostMode_Object = MibScalar
multiChassisLocalStpPathCostMode = _MultiChassisLocalStpPathCostMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 10),
    _MultiChassisLocalStpPathCostMode_Type()
)
multiChassisLocalStpPathCostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLocalStpPathCostMode.setStatus("current")


class _MultiChassisPeerStpPathCostMode_Type(Integer32):
    """Custom type multiChassisPeerStpPathCostMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("invalid", 0),
          ("thrityTwoBit", 1))
    )


_MultiChassisPeerStpPathCostMode_Type.__name__ = "Integer32"
_MultiChassisPeerStpPathCostMode_Object = MibScalar
multiChassisPeerStpPathCostMode = _MultiChassisPeerStpPathCostMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 11),
    _MultiChassisPeerStpPathCostMode_Type()
)
multiChassisPeerStpPathCostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisPeerStpPathCostMode.setStatus("current")
_MultiChassisStpPathCostModeConsistency_Type = MultiChassisConsistency
_MultiChassisStpPathCostModeConsistency_Object = MibScalar
multiChassisStpPathCostModeConsistency = _MultiChassisStpPathCostModeConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 12),
    _MultiChassisStpPathCostModeConsistency_Type()
)
multiChassisStpPathCostModeConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisStpPathCostModeConsistency.setStatus("current")


class _MultiChassisLocalStpMode_Type(Integer32):
    """Custom type multiChassisLocalStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flat", 1),
          ("onePerVlan", 2))
    )


_MultiChassisLocalStpMode_Type.__name__ = "Integer32"
_MultiChassisLocalStpMode_Object = MibScalar
multiChassisLocalStpMode = _MultiChassisLocalStpMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 13),
    _MultiChassisLocalStpMode_Type()
)
multiChassisLocalStpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLocalStpMode.setStatus("current")


class _MultiChassisPeerStpMode_Type(Integer32):
    """Custom type multiChassisPeerStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flat", 1),
          ("invalid", 0),
          ("onePerVlan", 2))
    )


_MultiChassisPeerStpMode_Type.__name__ = "Integer32"
_MultiChassisPeerStpMode_Object = MibScalar
multiChassisPeerStpMode = _MultiChassisPeerStpMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 14),
    _MultiChassisPeerStpMode_Type()
)
multiChassisPeerStpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisPeerStpMode.setStatus("current")
_MultiChassisStpModeConsistency_Type = MultiChassisConsistency
_MultiChassisStpModeConsistency_Object = MibScalar
multiChassisStpModeConsistency = _MultiChassisStpModeConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 15),
    _MultiChassisStpModeConsistency_Type()
)
multiChassisStpModeConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisStpModeConsistency.setStatus("current")
_MultiChassisLocalChassisGroup_Type = MultiChassisGroup
_MultiChassisLocalChassisGroup_Object = MibScalar
multiChassisLocalChassisGroup = _MultiChassisLocalChassisGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 16),
    _MultiChassisLocalChassisGroup_Type()
)
multiChassisLocalChassisGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLocalChassisGroup.setStatus("current")
_MultiChassisPeerChassisGroup_Type = MultiChassisGroup
_MultiChassisPeerChassisGroup_Object = MibScalar
multiChassisPeerChassisGroup = _MultiChassisPeerChassisGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 17),
    _MultiChassisPeerChassisGroup_Type()
)
multiChassisPeerChassisGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisPeerChassisGroup.setStatus("current")
_MultiChassisGroupConsistency_Type = MultiChassisConsistency
_MultiChassisGroupConsistency_Object = MibScalar
multiChassisGroupConsistency = _MultiChassisGroupConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 18),
    _MultiChassisGroupConsistency_Type()
)
multiChassisGroupConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisGroupConsistency.setStatus("current")
_MultiChassisLocalChassisType_Type = MultiChassisType
_MultiChassisLocalChassisType_Object = MibScalar
multiChassisLocalChassisType = _MultiChassisLocalChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 19),
    _MultiChassisLocalChassisType_Type()
)
multiChassisLocalChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLocalChassisType.setStatus("current")
_MultiChassisPeerChassisType_Type = MultiChassisType
_MultiChassisPeerChassisType_Object = MibScalar
multiChassisPeerChassisType = _MultiChassisPeerChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 20),
    _MultiChassisPeerChassisType_Type()
)
multiChassisPeerChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisPeerChassisType.setStatus("current")
_MultiChassisTypeConsistency_Type = MultiChassisConsistency
_MultiChassisTypeConsistency_Object = MibScalar
multiChassisTypeConsistency = _MultiChassisTypeConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 6, 21),
    _MultiChassisTypeConsistency_Type()
)
multiChassisTypeConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisTypeConsistency.setStatus("current")
_MultiChassisLinkaggConsistencyTable_Object = MibTable
multiChassisLinkaggConsistencyTable = _MultiChassisLinkaggConsistencyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7)
)
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyTable.setStatus("current")
_MultiChassisLinkaggConsistencyEntry_Object = MibTableRow
multiChassisLinkaggConsistencyEntry = _MultiChassisLinkaggConsistencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1)
)
multiChassisLinkaggConsistencyEntry.setIndexNames(
    (0, "ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyAggIndex"),
)
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyEntry.setStatus("current")
_MultiChassisLinkaggConsistencyAggIndex_Type = InterfaceIndex
_MultiChassisLinkaggConsistencyAggIndex_Object = MibTableColumn
multiChassisLinkaggConsistencyAggIndex = _MultiChassisLinkaggConsistencyAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 1),
    _MultiChassisLinkaggConsistencyAggIndex_Type()
)
multiChassisLinkaggConsistencyAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyAggIndex.setStatus("current")
_MultiChassisLinkaggConsistency_Type = MultiChassisConsistency
_MultiChassisLinkaggConsistency_Object = MibTableColumn
multiChassisLinkaggConsistency = _MultiChassisLinkaggConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 2),
    _MultiChassisLinkaggConsistency_Type()
)
multiChassisLinkaggConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistency.setStatus("current")


class _MultiChassisLinkaggLocalAggType_Type(Integer32):
    """Custom type multiChassisLinkaggLocalAggType based on Integer32"""
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
        *(("lacp", 2),
          ("mcLacp", 4),
          ("mcStatic", 3),
          ("static", 1))
    )


_MultiChassisLinkaggLocalAggType_Type.__name__ = "Integer32"
_MultiChassisLinkaggLocalAggType_Object = MibTableColumn
multiChassisLinkaggLocalAggType = _MultiChassisLinkaggLocalAggType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 3),
    _MultiChassisLinkaggLocalAggType_Type()
)
multiChassisLinkaggLocalAggType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggLocalAggType.setStatus("current")


class _MultiChassisLinkaggPeerAggType_Type(Integer32):
    """Custom type multiChassisLinkaggPeerAggType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("lacp", 2),
          ("mcLacp", 4),
          ("mcStatic", 3),
          ("static", 1))
    )


_MultiChassisLinkaggPeerAggType_Type.__name__ = "Integer32"
_MultiChassisLinkaggPeerAggType_Object = MibTableColumn
multiChassisLinkaggPeerAggType = _MultiChassisLinkaggPeerAggType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 4),
    _MultiChassisLinkaggPeerAggType_Type()
)
multiChassisLinkaggPeerAggType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggPeerAggType.setStatus("current")
_MultiChassisLinkaggAggTypeConsistency_Type = MultiChassisConsistency
_MultiChassisLinkaggAggTypeConsistency_Object = MibTableColumn
multiChassisLinkaggAggTypeConsistency = _MultiChassisLinkaggAggTypeConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 5),
    _MultiChassisLinkaggAggTypeConsistency_Type()
)
multiChassisLinkaggAggTypeConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggAggTypeConsistency.setStatus("current")


class _MultiChassisLinkaggLocalDefaultVlan_Type(Integer32):
    """Custom type multiChassisLinkaggLocalDefaultVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MultiChassisLinkaggLocalDefaultVlan_Type.__name__ = "Integer32"
_MultiChassisLinkaggLocalDefaultVlan_Object = MibTableColumn
multiChassisLinkaggLocalDefaultVlan = _MultiChassisLinkaggLocalDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 6),
    _MultiChassisLinkaggLocalDefaultVlan_Type()
)
multiChassisLinkaggLocalDefaultVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggLocalDefaultVlan.setStatus("current")


class _MultiChassisLinkaggPeerDefaultVlan_Type(Integer32):
    """Custom type multiChassisLinkaggPeerDefaultVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MultiChassisLinkaggPeerDefaultVlan_Type.__name__ = "Integer32"
_MultiChassisLinkaggPeerDefaultVlan_Object = MibTableColumn
multiChassisLinkaggPeerDefaultVlan = _MultiChassisLinkaggPeerDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 7),
    _MultiChassisLinkaggPeerDefaultVlan_Type()
)
multiChassisLinkaggPeerDefaultVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggPeerDefaultVlan.setStatus("current")
_MultiChassisLinkaggDefaultVlanConsistency_Type = MultiChassisConsistency
_MultiChassisLinkaggDefaultVlanConsistency_Object = MibTableColumn
multiChassisLinkaggDefaultVlanConsistency = _MultiChassisLinkaggDefaultVlanConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 8),
    _MultiChassisLinkaggDefaultVlanConsistency_Type()
)
multiChassisLinkaggDefaultVlanConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggDefaultVlanConsistency.setStatus("current")


class _MultiChassisLinkaggLocalVlanListConfigured_Type(Integer32):
    """Custom type multiChassisLinkaggLocalVlanListConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MultiChassisLinkaggLocalVlanListConfigured_Type.__name__ = "Integer32"
_MultiChassisLinkaggLocalVlanListConfigured_Object = MibTableColumn
multiChassisLinkaggLocalVlanListConfigured = _MultiChassisLinkaggLocalVlanListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 9),
    _MultiChassisLinkaggLocalVlanListConfigured_Type()
)
multiChassisLinkaggLocalVlanListConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggLocalVlanListConfigured.setStatus("current")


class _MultiChassisLinkaggPeerVlanListConfigured_Type(Integer32):
    """Custom type multiChassisLinkaggPeerVlanListConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("no", 2),
          ("yes", 1))
    )


_MultiChassisLinkaggPeerVlanListConfigured_Type.__name__ = "Integer32"
_MultiChassisLinkaggPeerVlanListConfigured_Object = MibTableColumn
multiChassisLinkaggPeerVlanListConfigured = _MultiChassisLinkaggPeerVlanListConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 10),
    _MultiChassisLinkaggPeerVlanListConfigured_Type()
)
multiChassisLinkaggPeerVlanListConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggPeerVlanListConfigured.setStatus("current")
_MultiChassisLinkaggVlanListConfiguredConsistency_Type = MultiChassisConsistency
_MultiChassisLinkaggVlanListConfiguredConsistency_Object = MibTableColumn
multiChassisLinkaggVlanListConfiguredConsistency = _MultiChassisLinkaggVlanListConfiguredConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 11),
    _MultiChassisLinkaggVlanListConfiguredConsistency_Type()
)
multiChassisLinkaggVlanListConfiguredConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggVlanListConfiguredConsistency.setStatus("current")
_MultiChassisLinkaggLocalAggActorSystemID_Type = MacAddress
_MultiChassisLinkaggLocalAggActorSystemID_Object = MibTableColumn
multiChassisLinkaggLocalAggActorSystemID = _MultiChassisLinkaggLocalAggActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 12),
    _MultiChassisLinkaggLocalAggActorSystemID_Type()
)
multiChassisLinkaggLocalAggActorSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggLocalAggActorSystemID.setStatus("current")
_MultiChassisLinkaggPeerAggActorSystemID_Type = MacAddress
_MultiChassisLinkaggPeerAggActorSystemID_Object = MibTableColumn
multiChassisLinkaggPeerAggActorSystemID = _MultiChassisLinkaggPeerAggActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 13),
    _MultiChassisLinkaggPeerAggActorSystemID_Type()
)
multiChassisLinkaggPeerAggActorSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggPeerAggActorSystemID.setStatus("current")
_MultiChassisLinkaggAggActorSystemIDConsistency_Type = MultiChassisConsistency
_MultiChassisLinkaggAggActorSystemIDConsistency_Object = MibTableColumn
multiChassisLinkaggAggActorSystemIDConsistency = _MultiChassisLinkaggAggActorSystemIDConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 14),
    _MultiChassisLinkaggAggActorSystemIDConsistency_Type()
)
multiChassisLinkaggAggActorSystemIDConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggAggActorSystemIDConsistency.setStatus("current")


class _MultiChassisLinkaggLocalAggActorSystemPriority_Type(Integer32):
    """Custom type multiChassisLinkaggLocalAggActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MultiChassisLinkaggLocalAggActorSystemPriority_Type.__name__ = "Integer32"
_MultiChassisLinkaggLocalAggActorSystemPriority_Object = MibTableColumn
multiChassisLinkaggLocalAggActorSystemPriority = _MultiChassisLinkaggLocalAggActorSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 15),
    _MultiChassisLinkaggLocalAggActorSystemPriority_Type()
)
multiChassisLinkaggLocalAggActorSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggLocalAggActorSystemPriority.setStatus("current")


class _MultiChassisLinkaggPeerAggActorSystemPriority_Type(Integer32):
    """Custom type multiChassisLinkaggPeerAggActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MultiChassisLinkaggPeerAggActorSystemPriority_Type.__name__ = "Integer32"
_MultiChassisLinkaggPeerAggActorSystemPriority_Object = MibTableColumn
multiChassisLinkaggPeerAggActorSystemPriority = _MultiChassisLinkaggPeerAggActorSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 16),
    _MultiChassisLinkaggPeerAggActorSystemPriority_Type()
)
multiChassisLinkaggPeerAggActorSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggPeerAggActorSystemPriority.setStatus("current")
_MultiChassisLinkaggAggActorSystemPriorityConsistency_Type = MultiChassisConsistency
_MultiChassisLinkaggAggActorSystemPriorityConsistency_Object = MibTableColumn
multiChassisLinkaggAggActorSystemPriorityConsistency = _MultiChassisLinkaggAggActorSystemPriorityConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 17),
    _MultiChassisLinkaggAggActorSystemPriorityConsistency_Type()
)
multiChassisLinkaggAggActorSystemPriorityConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggAggActorSystemPriorityConsistency.setStatus("current")
_MultiChassisLinkaggLocalExist_Type = TruthValue
_MultiChassisLinkaggLocalExist_Object = MibTableColumn
multiChassisLinkaggLocalExist = _MultiChassisLinkaggLocalExist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 18),
    _MultiChassisLinkaggLocalExist_Type()
)
multiChassisLinkaggLocalExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggLocalExist.setStatus("current")
_MultiChassisLinkaggPeerExist_Type = TruthValue
_MultiChassisLinkaggPeerExist_Object = MibTableColumn
multiChassisLinkaggPeerExist = _MultiChassisLinkaggPeerExist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 19),
    _MultiChassisLinkaggPeerExist_Type()
)
multiChassisLinkaggPeerExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggPeerExist.setStatus("current")
_MultiChassisLinkaggAggAllConsistency_Type = MultiChassisConsistency
_MultiChassisLinkaggAggAllConsistency_Object = MibTableColumn
multiChassisLinkaggAggAllConsistency = _MultiChassisLinkaggAggAllConsistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 20),
    _MultiChassisLinkaggAggAllConsistency_Type()
)
multiChassisLinkaggAggAllConsistency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggAggAllConsistency.setStatus("current")
_MultiChassisLinkaggLocalListVlanSize_Type = Integer32
_MultiChassisLinkaggLocalListVlanSize_Object = MibTableColumn
multiChassisLinkaggLocalListVlanSize = _MultiChassisLinkaggLocalListVlanSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 21),
    _MultiChassisLinkaggLocalListVlanSize_Type()
)
multiChassisLinkaggLocalListVlanSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggLocalListVlanSize.setStatus("current")
_MultiChassisLinkaggPeerListVlanSize_Type = Integer32
_MultiChassisLinkaggPeerListVlanSize_Object = MibTableColumn
multiChassisLinkaggPeerListVlanSize = _MultiChassisLinkaggPeerListVlanSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 7, 1, 22),
    _MultiChassisLinkaggPeerListVlanSize_Type()
)
multiChassisLinkaggPeerListVlanSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggPeerListVlanSize.setStatus("current")
_MultiChassisTrapInfo_ObjectIdentity = ObjectIdentity
multiChassisTrapInfo = _MultiChassisTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 8)
)


class _MultiChassisTrapIpcVlan_Type(Integer32):
    """Custom type multiChassisTrapIpcVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MultiChassisTrapIpcVlan_Type.__name__ = "Integer32"
_MultiChassisTrapIpcVlan_Object = MibScalar
multiChassisTrapIpcVlan = _MultiChassisTrapIpcVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 8, 1),
    _MultiChassisTrapIpcVlan_Type()
)
multiChassisTrapIpcVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisTrapIpcVlan.setStatus("current")


class _MultiChassisTrapStpBlockingVlanList_Type(SnmpAdminString):
    """Custom type multiChassisTrapStpBlockingVlanList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MultiChassisTrapStpBlockingVlanList_Type.__name__ = "SnmpAdminString"
_MultiChassisTrapStpBlockingVlanList_Object = MibScalar
multiChassisTrapStpBlockingVlanList = _MultiChassisTrapStpBlockingVlanList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 8, 2),
    _MultiChassisTrapStpBlockingVlanList_Type()
)
multiChassisTrapStpBlockingVlanList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisTrapStpBlockingVlanList.setStatus("current")


class _MultiChassisTrapFailure_Type(Integer32):
    """Custom type multiChassisTrapFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("failure", 1)
    )


_MultiChassisTrapFailure_Type.__name__ = "Integer32"
_MultiChassisTrapFailure_Object = MibScalar
multiChassisTrapFailure = _MultiChassisTrapFailure_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 8, 3),
    _MultiChassisTrapFailure_Type()
)
multiChassisTrapFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisTrapFailure.setStatus("current")
_MultiChassisTrapVFL_Type = MultiChassisLinkIfIndex
_MultiChassisTrapVFL_Object = MibScalar
multiChassisTrapVFL = _MultiChassisTrapVFL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 8, 4),
    _MultiChassisTrapVFL_Type()
)
multiChassisTrapVFL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisTrapVFL.setStatus("current")
_MultiChassisTrapVFLMemberPort_Type = InterfaceIndex
_MultiChassisTrapVFLMemberPort_Object = MibScalar
multiChassisTrapVFLMemberPort = _MultiChassisTrapVFLMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 8, 5),
    _MultiChassisTrapVFLMemberPort_Type()
)
multiChassisTrapVFLMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisTrapVFLMemberPort.setStatus("current")


class _MultiChassisTrapDiagnostic_Type(Integer32):
    """Custom type multiChassisTrapDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplexMode", 1),
          ("speed", 2))
    )


_MultiChassisTrapDiagnostic_Type.__name__ = "Integer32"
_MultiChassisTrapDiagnostic_Object = MibScalar
multiChassisTrapDiagnostic = _MultiChassisTrapDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 8, 6),
    _MultiChassisTrapDiagnostic_Type()
)
multiChassisTrapDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisTrapDiagnostic.setStatus("current")


class _MultiChassisStpStatus_Type(Integer32):
    """Custom type multiChassisStpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("forwarding", 0))
    )


_MultiChassisStpStatus_Type.__name__ = "Integer32"
_MultiChassisStpStatus_Object = MibScalar
multiChassisStpStatus = _MultiChassisStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 8, 7),
    _MultiChassisStpStatus_Type()
)
multiChassisStpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisStpStatus.setStatus("current")


class _MultiChassisTrapRecovered_Type(Integer32):
    """Custom type multiChassisTrapRecovered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("recovered", 1)
    )


_MultiChassisTrapRecovered_Type.__name__ = "Integer32"
_MultiChassisTrapRecovered_Object = MibScalar
multiChassisTrapRecovered = _MultiChassisTrapRecovered_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 8, 8),
    _MultiChassisTrapRecovered_Type()
)
multiChassisTrapRecovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisTrapRecovered.setStatus("current")
_MultiChassisLinkaggConsistencyVlanTable_Object = MibTable
multiChassisLinkaggConsistencyVlanTable = _MultiChassisLinkaggConsistencyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9)
)
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanTable.setStatus("current")
_MultiChassisLinkaggConsistencyVlanEntry_Object = MibTableRow
multiChassisLinkaggConsistencyVlanEntry = _MultiChassisLinkaggConsistencyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1)
)
multiChassisLinkaggConsistencyVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanAggIndex"),
    (0, "ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanId"),
    (0, "ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanLocaleType"),
)
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanEntry.setStatus("current")
_MultiChassisLinkaggConsistencyVlanAggIndex_Type = InterfaceIndex
_MultiChassisLinkaggConsistencyVlanAggIndex_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanAggIndex = _MultiChassisLinkaggConsistencyVlanAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 1),
    _MultiChassisLinkaggConsistencyVlanAggIndex_Type()
)
multiChassisLinkaggConsistencyVlanAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanAggIndex.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanId_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MultiChassisLinkaggConsistencyVlanId_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanId_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanId = _MultiChassisLinkaggConsistencyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 2),
    _MultiChassisLinkaggConsistencyVlanId_Type()
)
multiChassisLinkaggConsistencyVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanId.setStatus("current")
_MultiChassisLinkaggConsistencyVlanLocaleType_Type = MultiChassisLocaleType
_MultiChassisLinkaggConsistencyVlanLocaleType_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanLocaleType = _MultiChassisLinkaggConsistencyVlanLocaleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 3),
    _MultiChassisLinkaggConsistencyVlanLocaleType_Type()
)
multiChassisLinkaggConsistencyVlanLocaleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanLocaleType.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanType_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 4),
          ("erpVlan", 8),
          ("invalid", 0),
          ("ipc", 6),
          ("mtpVlan", 9),
          ("multicastEnt", 2),
          ("multicastService", 3),
          ("service", 1),
          ("standard", 5),
          ("vipVlan", 7))
    )


_MultiChassisLinkaggConsistencyVlanType_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanType_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanType = _MultiChassisLinkaggConsistencyVlanType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 4),
    _MultiChassisLinkaggConsistencyVlanType_Type()
)
multiChassisLinkaggConsistencyVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanType.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanAdminStatus_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", 0))
    )


_MultiChassisLinkaggConsistencyVlanAdminStatus_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanAdminStatus_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanAdminStatus = _MultiChassisLinkaggConsistencyVlanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 5),
    _MultiChassisLinkaggConsistencyVlanAdminStatus_Type()
)
multiChassisLinkaggConsistencyVlanAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanAdminStatus.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanOperStatus_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", 0))
    )


_MultiChassisLinkaggConsistencyVlanOperStatus_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanOperStatus_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanOperStatus = _MultiChassisLinkaggConsistencyVlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 6),
    _MultiChassisLinkaggConsistencyVlanOperStatus_Type()
)
multiChassisLinkaggConsistencyVlanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanOperStatus.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanIpEnable_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanIpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", 0))
    )


_MultiChassisLinkaggConsistencyVlanIpEnable_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanIpEnable_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanIpEnable = _MultiChassisLinkaggConsistencyVlanIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 7),
    _MultiChassisLinkaggConsistencyVlanIpEnable_Type()
)
multiChassisLinkaggConsistencyVlanIpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanIpEnable.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanMtu_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 10222),
    )


_MultiChassisLinkaggConsistencyVlanMtu_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanMtu_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanMtu = _MultiChassisLinkaggConsistencyVlanMtu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 8),
    _MultiChassisLinkaggConsistencyVlanMtu_Type()
)
multiChassisLinkaggConsistencyVlanMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanMtu.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanSrcLearningStatus_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanSrcLearningStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", 0))
    )


_MultiChassisLinkaggConsistencyVlanSrcLearningStatus_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanSrcLearningStatus_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanSrcLearningStatus = _MultiChassisLinkaggConsistencyVlanSrcLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 9),
    _MultiChassisLinkaggConsistencyVlanSrcLearningStatus_Type()
)
multiChassisLinkaggConsistencyVlanSrcLearningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanSrcLearningStatus.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanVpaType_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanVpaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cfgDefault", 1),
          ("dynamic", 3),
          ("forbidden", 6),
          ("invalid", 0),
          ("qTagged", 2),
          ("vstkDoubleTag", 4),
          ("vstkTranslate", 5))
    )


_MultiChassisLinkaggConsistencyVlanVpaType_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanVpaType_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanVpaType = _MultiChassisLinkaggConsistencyVlanVpaType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 10),
    _MultiChassisLinkaggConsistencyVlanVpaType_Type()
)
multiChassisLinkaggConsistencyVlanVpaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanVpaType.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanVpaState_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanVpaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("forwarding", 0),
          ("inactive", 2),
          ("invalid", 3))
    )


_MultiChassisLinkaggConsistencyVlanVpaState_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanVpaState_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanVpaState = _MultiChassisLinkaggConsistencyVlanVpaState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 11),
    _MultiChassisLinkaggConsistencyVlanVpaState_Type()
)
multiChassisLinkaggConsistencyVlanVpaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanVpaState.setStatus("current")
_MultiChassisLinkaggConsistencyVlanVRF_Type = Integer32
_MultiChassisLinkaggConsistencyVlanVRF_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanVRF = _MultiChassisLinkaggConsistencyVlanVRF_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 12),
    _MultiChassisLinkaggConsistencyVlanVRF_Type()
)
multiChassisLinkaggConsistencyVlanVRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanVRF.setStatus("current")


class _MultiChassisLinkaggConsistencyVlanIcmpRedirectStatus_Type(Integer32):
    """Custom type multiChassisLinkaggConsistencyVlanIcmpRedirectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", 0))
    )


_MultiChassisLinkaggConsistencyVlanIcmpRedirectStatus_Type.__name__ = "Integer32"
_MultiChassisLinkaggConsistencyVlanIcmpRedirectStatus_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanIcmpRedirectStatus = _MultiChassisLinkaggConsistencyVlanIcmpRedirectStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 13),
    _MultiChassisLinkaggConsistencyVlanIcmpRedirectStatus_Type()
)
multiChassisLinkaggConsistencyVlanIcmpRedirectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanIcmpRedirectStatus.setStatus("current")
_MultiChassisLinkaggConsistencyVlanStatus_Type = MultiChassisConsistency
_MultiChassisLinkaggConsistencyVlanStatus_Object = MibTableColumn
multiChassisLinkaggConsistencyVlanStatus = _MultiChassisLinkaggConsistencyVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 1, 9, 1, 14),
    _MultiChassisLinkaggConsistencyVlanStatus_Type()
)
multiChassisLinkaggConsistencyVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanStatus.setStatus("current")
_AlcatelIND1MultiChassisMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1MultiChassisMIBConformance = _AlcatelIND1MultiChassisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MultiChassisMIBConformance.setStatus("current")
_AlcatelIND1MultiChassisMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1MultiChassisMIBGroups = _AlcatelIND1MultiChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MultiChassisMIBGroups.setStatus("current")
_AlcatelIND1MultiChassisMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1MultiChassisMIBCompliances = _AlcatelIND1MultiChassisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MultiChassisMIBCompliances.setStatus("current")

# Managed Objects groups

multiChassisConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 1)
)
multiChassisConfigGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisConfigChassisId"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisConfigHelloInterval"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisConfigIpcVlan"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisConfigChassisGroup"))
)
if mibBuilder.loadTexts:
    multiChassisConfigGroup.setStatus("current")

multiChassisOperationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 2)
)
multiChassisOperationGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisOperChassisId"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisOperChassisRole"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisOperStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisOperHelloInterval"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisOperIpcVlan"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisOperChassisGroup"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisOperChassisType"))
)
if mibBuilder.loadTexts:
    multiChassisOperationGroup.setStatus("current")

multiChassisLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 3)
)
multiChassisLinkGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkAdminStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkOperDefaultVlan"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkOperStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkPrimaryPort"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkActivePortNum"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkConfigPortNum"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkRowStatus"))
)
if mibBuilder.loadTexts:
    multiChassisLinkGroup.setStatus("current")

multiChassisLinkMemberPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 4)
)
multiChassisLinkMemberPortGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkMemberPortIsPrimay"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkMemberOperStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkMemberPortRowStatus"))
)
if mibBuilder.loadTexts:
    multiChassisLinkMemberPortGroup.setStatus("current")

multiChassisLoopDetectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 5)
)
multiChassisLoopDetectionGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLoopDetectionAdminStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLoopDetectionTransmitInterval"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLoopDetectionTransmitCount"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLoopDetectionCount"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLoopDetectionPortDownList"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLoopDetectionClear"))
)
if mibBuilder.loadTexts:
    multiChassisLoopDetectionGroup.setStatus("current")

multiChassisGlobalConsistencyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 6)
)
multiChassisGlobalConsistencyGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLocalChassisId"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisPeerChassisId"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisIdConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLocalHelloInterval"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisPeerHelloInterval"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisHelloIntervalConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLocalIpcVlan"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisPeerIpcVlan"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisIpcVlanConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLocalStpPathCostMode"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisPeerStpPathCostMode"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisStpPathCostModeConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLocalStpMode"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisPeerStpMode"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisStpModeConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLocalChassisGroup"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisPeerChassisGroup"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisGroupConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLocalChassisType"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisPeerChassisType"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTypeConsistency"))
)
if mibBuilder.loadTexts:
    multiChassisGlobalConsistencyGroup.setStatus("current")

multiChassisLinkaggConsistencyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 7)
)
multiChassisLinkaggConsistencyGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggLocalAggType"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggPeerAggType"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggAggTypeConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggLocalDefaultVlan"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggPeerDefaultVlan"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggDefaultVlanConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggLocalVlanListConfigured"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggPeerVlanListConfigured"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggVlanListConfiguredConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggLocalAggActorSystemID"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggPeerAggActorSystemID"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggAggActorSystemIDConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggLocalAggActorSystemPriority"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggPeerAggActorSystemPriority"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggAggActorSystemPriorityConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggLocalExist"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggPeerExist"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggAggAllConsistency"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggLocalListVlanSize"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggPeerListVlanSize"))
)
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyGroup.setStatus("current")

multiChassisTrapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 8)
)
multiChassisTrapInfoGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapIpcVlan"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapStpBlockingVlanList"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapVFL"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapVFLMemberPort"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapDiagnostic"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisStpStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapRecovered"))
)
if mibBuilder.loadTexts:
    multiChassisTrapInfoGroup.setStatus("current")

multiChassisLinkaggConsistencyVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 10)
)
multiChassisLinkaggConsistencyVlanGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanType"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanAdminStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanOperStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanIpEnable"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanMtu"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanSrcLearningStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanVpaType"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanVpaState"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanVRF"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanIcmpRedirectStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLinkaggConsistencyVlanStatus"))
)
if mibBuilder.loadTexts:
    multiChassisLinkaggConsistencyVlanGroup.setStatus("current")


# Notification objects

multiChassisIpcVlanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 1)
)
multiChassisIpcVlanDown.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapIpcVlan")
)
if mibBuilder.loadTexts:
    multiChassisIpcVlanDown.setStatus(
        "deprecated"
    )

multiChassisIpcVlanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 2)
)
multiChassisIpcVlanUp.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapIpcVlan")
)
if mibBuilder.loadTexts:
    multiChassisIpcVlanUp.setStatus(
        "deprecated"
    )

multiChassisMisconfigurationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 3)
)
multiChassisMisconfigurationFailure.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisMisconfigurationFailure.setStatus(
        "current"
    )

multiChassisHelloIntervalConsisFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 4)
)
multiChassisHelloIntervalConsisFailure.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisHelloIntervalConsisFailure.setStatus(
        "current"
    )

multiChassisStpModeConsisFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 5)
)
multiChassisStpModeConsisFailure.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisStpModeConsisFailure.setStatus(
        "current"
    )

multiChassisStpPathCostModeConsisFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 6)
)
multiChassisStpPathCostModeConsisFailure.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisStpPathCostModeConsisFailure.setStatus(
        "current"
    )

multiChassisVflinkStatusConsisFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 7)
)
multiChassisVflinkStatusConsisFailure.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisVflinkStatusConsisFailure.setStatus(
        "deprecated"
    )

multiChassisStpBlockingStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 8)
)
multiChassisStpBlockingStatus.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapStpBlockingVlanList"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapVFL"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisStpStatus"))
)
if mibBuilder.loadTexts:
    multiChassisStpBlockingStatus.setStatus(
        "current"
    )

multiChassisLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 9)
)
multiChassisLoopDetected.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisLoopDetected.setStatus(
        "current"
    )

multiChassisHelloTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 10)
)
multiChassisHelloTimeout.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisHelloTimeout.setStatus(
        "current"
    )

multiChassisVflinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 11)
)
multiChassisVflinkDown.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisVflinkDown.setStatus(
        "current"
    )

multiChassisVFLMemberJoinFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 12)
)
multiChassisVFLMemberJoinFailure.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapVFL"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapVFLMemberPort"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapDiagnostic"))
)
if mibBuilder.loadTexts:
    multiChassisVFLMemberJoinFailure.setStatus(
        "current"
    )

multiChassisGroupConsisFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 13)
)
multiChassisGroupConsisFailure.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisGroupConsisFailure.setStatus(
        "current"
    )

multiChassisTypeConsisFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 14)
)
multiChassisTypeConsisFailure.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapFailure")
)
if mibBuilder.loadTexts:
    multiChassisTypeConsisFailure.setStatus(
        "current"
    )

multiChassisConsisFailureRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 0, 15)
)
multiChassisConsisFailureRecovered.setObjects(
    ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTrapRecovered")
)
if mibBuilder.loadTexts:
    multiChassisConsisFailureRecovered.setStatus(
        "current"
    )


# Notifications groups

multiChassisTrapOBJGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 1, 9)
)
multiChassisTrapOBJGroup.setObjects(
      *(("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisIpcVlanDown"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisIpcVlanUp"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisMisconfigurationFailure"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisHelloIntervalConsisFailure"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisStpModeConsisFailure"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisStpPathCostModeConsisFailure"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisVflinkStatusConsisFailure"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisStpBlockingStatus"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisLoopDetected"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisHelloTimeout"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisVflinkDown"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisVFLMemberJoinFailure"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisGroupConsisFailure"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisTypeConsisFailure"),
        ("ALCATEL-IND1-MULTI-CHASSIS-MIB", "multiChassisConsisFailureRecovered"))
)
if mibBuilder.loadTexts:
    multiChassisTrapOBJGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1MultiChassisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 55, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MultiChassisMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-MULTI-CHASSIS-MIB",
    **{"MultiChassisId": MultiChassisId,
       "MultiChassisLinkIfIndex": MultiChassisLinkIfIndex,
       "MultiChassisConsistency": MultiChassisConsistency,
       "MultiChassisLocaleType": MultiChassisLocaleType,
       "MultiChassisGroup": MultiChassisGroup,
       "MultiChassisType": MultiChassisType,
       "alcatelIND1MultiChassisMIB": alcatelIND1MultiChassisMIB,
       "alcatelIND1MultiChassisMIBNotifications": alcatelIND1MultiChassisMIBNotifications,
       "multiChassisIpcVlanDown": multiChassisIpcVlanDown,
       "multiChassisIpcVlanUp": multiChassisIpcVlanUp,
       "multiChassisMisconfigurationFailure": multiChassisMisconfigurationFailure,
       "multiChassisHelloIntervalConsisFailure": multiChassisHelloIntervalConsisFailure,
       "multiChassisStpModeConsisFailure": multiChassisStpModeConsisFailure,
       "multiChassisStpPathCostModeConsisFailure": multiChassisStpPathCostModeConsisFailure,
       "multiChassisVflinkStatusConsisFailure": multiChassisVflinkStatusConsisFailure,
       "multiChassisStpBlockingStatus": multiChassisStpBlockingStatus,
       "multiChassisLoopDetected": multiChassisLoopDetected,
       "multiChassisHelloTimeout": multiChassisHelloTimeout,
       "multiChassisVflinkDown": multiChassisVflinkDown,
       "multiChassisVFLMemberJoinFailure": multiChassisVFLMemberJoinFailure,
       "multiChassisGroupConsisFailure": multiChassisGroupConsisFailure,
       "multiChassisTypeConsisFailure": multiChassisTypeConsisFailure,
       "multiChassisConsisFailureRecovered": multiChassisConsisFailureRecovered,
       "alcatelIND1MultiChassisMIBObjects": alcatelIND1MultiChassisMIBObjects,
       "multiChassisConfig": multiChassisConfig,
       "multiChassisConfigChassisId": multiChassisConfigChassisId,
       "multiChassisConfigHelloInterval": multiChassisConfigHelloInterval,
       "multiChassisConfigIpcVlan": multiChassisConfigIpcVlan,
       "multiChassisConfigChassisGroup": multiChassisConfigChassisGroup,
       "multiChassisOperation": multiChassisOperation,
       "multiChassisOperChassisId": multiChassisOperChassisId,
       "multiChassisOperChassisRole": multiChassisOperChassisRole,
       "multiChassisOperStatus": multiChassisOperStatus,
       "multiChassisOperHelloInterval": multiChassisOperHelloInterval,
       "multiChassisOperIpcVlan": multiChassisOperIpcVlan,
       "multiChassisOperChassisGroup": multiChassisOperChassisGroup,
       "multiChassisOperChassisType": multiChassisOperChassisType,
       "multiChassisLinkTable": multiChassisLinkTable,
       "multiChassisLinkEntry": multiChassisLinkEntry,
       "multiChassisLinkIfIndex": multiChassisLinkIfIndex,
       "multiChassisLinkAdminStatus": multiChassisLinkAdminStatus,
       "multiChassisLinkOperDefaultVlan": multiChassisLinkOperDefaultVlan,
       "multiChassisLinkOperStatus": multiChassisLinkOperStatus,
       "multiChassisLinkPrimaryPort": multiChassisLinkPrimaryPort,
       "multiChassisLinkActivePortNum": multiChassisLinkActivePortNum,
       "multiChassisLinkConfigPortNum": multiChassisLinkConfigPortNum,
       "multiChassisLinkRowStatus": multiChassisLinkRowStatus,
       "multiChassisLinkMemberPortTable": multiChassisLinkMemberPortTable,
       "multiChassisLinkMemberPortEntry": multiChassisLinkMemberPortEntry,
       "multiChassisLinkMemberPortLinkIfIndex": multiChassisLinkMemberPortLinkIfIndex,
       "multiChassisLinkMemberPortIfindex": multiChassisLinkMemberPortIfindex,
       "multiChassisLinkMemberPortIsPrimay": multiChassisLinkMemberPortIsPrimay,
       "multiChassisLinkMemberOperStatus": multiChassisLinkMemberOperStatus,
       "multiChassisLinkMemberPortRowStatus": multiChassisLinkMemberPortRowStatus,
       "multiChassisLoopDetection": multiChassisLoopDetection,
       "multiChassisLoopDetectionAdminStatus": multiChassisLoopDetectionAdminStatus,
       "multiChassisLoopDetectionTransmitInterval": multiChassisLoopDetectionTransmitInterval,
       "multiChassisLoopDetectionTransmitCount": multiChassisLoopDetectionTransmitCount,
       "multiChassisLoopDetectionCount": multiChassisLoopDetectionCount,
       "multiChassisLoopDetectionPortDownList": multiChassisLoopDetectionPortDownList,
       "multiChassisLoopDetectionClear": multiChassisLoopDetectionClear,
       "multiChassisGlobalConsistency": multiChassisGlobalConsistency,
       "multiChassisLocalChassisId": multiChassisLocalChassisId,
       "multiChassisPeerChassisId": multiChassisPeerChassisId,
       "multiChassisIdConsistency": multiChassisIdConsistency,
       "multiChassisLocalHelloInterval": multiChassisLocalHelloInterval,
       "multiChassisPeerHelloInterval": multiChassisPeerHelloInterval,
       "multiChassisHelloIntervalConsistency": multiChassisHelloIntervalConsistency,
       "multiChassisLocalIpcVlan": multiChassisLocalIpcVlan,
       "multiChassisPeerIpcVlan": multiChassisPeerIpcVlan,
       "multiChassisIpcVlanConsistency": multiChassisIpcVlanConsistency,
       "multiChassisLocalStpPathCostMode": multiChassisLocalStpPathCostMode,
       "multiChassisPeerStpPathCostMode": multiChassisPeerStpPathCostMode,
       "multiChassisStpPathCostModeConsistency": multiChassisStpPathCostModeConsistency,
       "multiChassisLocalStpMode": multiChassisLocalStpMode,
       "multiChassisPeerStpMode": multiChassisPeerStpMode,
       "multiChassisStpModeConsistency": multiChassisStpModeConsistency,
       "multiChassisLocalChassisGroup": multiChassisLocalChassisGroup,
       "multiChassisPeerChassisGroup": multiChassisPeerChassisGroup,
       "multiChassisGroupConsistency": multiChassisGroupConsistency,
       "multiChassisLocalChassisType": multiChassisLocalChassisType,
       "multiChassisPeerChassisType": multiChassisPeerChassisType,
       "multiChassisTypeConsistency": multiChassisTypeConsistency,
       "multiChassisLinkaggConsistencyTable": multiChassisLinkaggConsistencyTable,
       "multiChassisLinkaggConsistencyEntry": multiChassisLinkaggConsistencyEntry,
       "multiChassisLinkaggConsistencyAggIndex": multiChassisLinkaggConsistencyAggIndex,
       "multiChassisLinkaggConsistency": multiChassisLinkaggConsistency,
       "multiChassisLinkaggLocalAggType": multiChassisLinkaggLocalAggType,
       "multiChassisLinkaggPeerAggType": multiChassisLinkaggPeerAggType,
       "multiChassisLinkaggAggTypeConsistency": multiChassisLinkaggAggTypeConsistency,
       "multiChassisLinkaggLocalDefaultVlan": multiChassisLinkaggLocalDefaultVlan,
       "multiChassisLinkaggPeerDefaultVlan": multiChassisLinkaggPeerDefaultVlan,
       "multiChassisLinkaggDefaultVlanConsistency": multiChassisLinkaggDefaultVlanConsistency,
       "multiChassisLinkaggLocalVlanListConfigured": multiChassisLinkaggLocalVlanListConfigured,
       "multiChassisLinkaggPeerVlanListConfigured": multiChassisLinkaggPeerVlanListConfigured,
       "multiChassisLinkaggVlanListConfiguredConsistency": multiChassisLinkaggVlanListConfiguredConsistency,
       "multiChassisLinkaggLocalAggActorSystemID": multiChassisLinkaggLocalAggActorSystemID,
       "multiChassisLinkaggPeerAggActorSystemID": multiChassisLinkaggPeerAggActorSystemID,
       "multiChassisLinkaggAggActorSystemIDConsistency": multiChassisLinkaggAggActorSystemIDConsistency,
       "multiChassisLinkaggLocalAggActorSystemPriority": multiChassisLinkaggLocalAggActorSystemPriority,
       "multiChassisLinkaggPeerAggActorSystemPriority": multiChassisLinkaggPeerAggActorSystemPriority,
       "multiChassisLinkaggAggActorSystemPriorityConsistency": multiChassisLinkaggAggActorSystemPriorityConsistency,
       "multiChassisLinkaggLocalExist": multiChassisLinkaggLocalExist,
       "multiChassisLinkaggPeerExist": multiChassisLinkaggPeerExist,
       "multiChassisLinkaggAggAllConsistency": multiChassisLinkaggAggAllConsistency,
       "multiChassisLinkaggLocalListVlanSize": multiChassisLinkaggLocalListVlanSize,
       "multiChassisLinkaggPeerListVlanSize": multiChassisLinkaggPeerListVlanSize,
       "multiChassisTrapInfo": multiChassisTrapInfo,
       "multiChassisTrapIpcVlan": multiChassisTrapIpcVlan,
       "multiChassisTrapStpBlockingVlanList": multiChassisTrapStpBlockingVlanList,
       "multiChassisTrapFailure": multiChassisTrapFailure,
       "multiChassisTrapVFL": multiChassisTrapVFL,
       "multiChassisTrapVFLMemberPort": multiChassisTrapVFLMemberPort,
       "multiChassisTrapDiagnostic": multiChassisTrapDiagnostic,
       "multiChassisStpStatus": multiChassisStpStatus,
       "multiChassisTrapRecovered": multiChassisTrapRecovered,
       "multiChassisLinkaggConsistencyVlanTable": multiChassisLinkaggConsistencyVlanTable,
       "multiChassisLinkaggConsistencyVlanEntry": multiChassisLinkaggConsistencyVlanEntry,
       "multiChassisLinkaggConsistencyVlanAggIndex": multiChassisLinkaggConsistencyVlanAggIndex,
       "multiChassisLinkaggConsistencyVlanId": multiChassisLinkaggConsistencyVlanId,
       "multiChassisLinkaggConsistencyVlanLocaleType": multiChassisLinkaggConsistencyVlanLocaleType,
       "multiChassisLinkaggConsistencyVlanType": multiChassisLinkaggConsistencyVlanType,
       "multiChassisLinkaggConsistencyVlanAdminStatus": multiChassisLinkaggConsistencyVlanAdminStatus,
       "multiChassisLinkaggConsistencyVlanOperStatus": multiChassisLinkaggConsistencyVlanOperStatus,
       "multiChassisLinkaggConsistencyVlanIpEnable": multiChassisLinkaggConsistencyVlanIpEnable,
       "multiChassisLinkaggConsistencyVlanMtu": multiChassisLinkaggConsistencyVlanMtu,
       "multiChassisLinkaggConsistencyVlanSrcLearningStatus": multiChassisLinkaggConsistencyVlanSrcLearningStatus,
       "multiChassisLinkaggConsistencyVlanVpaType": multiChassisLinkaggConsistencyVlanVpaType,
       "multiChassisLinkaggConsistencyVlanVpaState": multiChassisLinkaggConsistencyVlanVpaState,
       "multiChassisLinkaggConsistencyVlanVRF": multiChassisLinkaggConsistencyVlanVRF,
       "multiChassisLinkaggConsistencyVlanIcmpRedirectStatus": multiChassisLinkaggConsistencyVlanIcmpRedirectStatus,
       "multiChassisLinkaggConsistencyVlanStatus": multiChassisLinkaggConsistencyVlanStatus,
       "alcatelIND1MultiChassisMIBConformance": alcatelIND1MultiChassisMIBConformance,
       "alcatelIND1MultiChassisMIBGroups": alcatelIND1MultiChassisMIBGroups,
       "multiChassisConfigGroup": multiChassisConfigGroup,
       "multiChassisOperationGroup": multiChassisOperationGroup,
       "multiChassisLinkGroup": multiChassisLinkGroup,
       "multiChassisLinkMemberPortGroup": multiChassisLinkMemberPortGroup,
       "multiChassisLoopDetectionGroup": multiChassisLoopDetectionGroup,
       "multiChassisGlobalConsistencyGroup": multiChassisGlobalConsistencyGroup,
       "multiChassisLinkaggConsistencyGroup": multiChassisLinkaggConsistencyGroup,
       "multiChassisTrapInfoGroup": multiChassisTrapInfoGroup,
       "multiChassisTrapOBJGroup": multiChassisTrapOBJGroup,
       "multiChassisLinkaggConsistencyVlanGroup": multiChassisLinkaggConsistencyVlanGroup,
       "alcatelIND1MultiChassisMIBCompliances": alcatelIND1MultiChassisMIBCompliances,
       "alcatelIND1MultiChassisMIBCompliance": alcatelIND1MultiChassisMIBCompliance}
)
