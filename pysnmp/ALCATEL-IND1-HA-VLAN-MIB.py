# SNMP MIB module (ALCATEL-IND1-HA-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-HA-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:08 2024
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

(softentIND1HAVlan,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1HAVlan")

(MultiChassisId,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-MULTI-CHASSIS-MIB",
    "MultiChassisId")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1HAVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1)
)
alcatelIND1HAVlanMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1HAVlanMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1HAVlanMIBNotifications = _AlcatelIND1HAVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1HAVlanMIBNotifications.setStatus("current")
_AlcatelIND1HAVlanMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1HAVlanMIBObjects = _AlcatelIND1HAVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1HAVlanMIBObjects.setStatus("current")
_AlaHAVlanCluster_ObjectIdentity = ObjectIdentity
alaHAVlanCluster = _AlaHAVlanCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1)
)
_AlaHAVlanClusterTable_Object = MibTable
alaHAVlanClusterTable = _AlaHAVlanClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaHAVlanClusterTable.setStatus("current")
_AlaHAVlanClusterEntry_Object = MibTableRow
alaHAVlanClusterEntry = _AlaHAVlanClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1)
)
alaHAVlanClusterEntry.setIndexNames(
    (0, "ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"),
)
if mibBuilder.loadTexts:
    alaHAVlanClusterEntry.setStatus("current")


class _AlaHAVlanClusterId_Type(Integer32):
    """Custom type alaHAVlanClusterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AlaHAVlanClusterId_Type.__name__ = "Integer32"
_AlaHAVlanClusterId_Object = MibTableColumn
alaHAVlanClusterId = _AlaHAVlanClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 1),
    _AlaHAVlanClusterId_Type()
)
alaHAVlanClusterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaHAVlanClusterId.setStatus("current")


class _AlaHAVlanClusterName_Type(SnmpAdminString):
    """Custom type alaHAVlanClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaHAVlanClusterName_Type.__name__ = "SnmpAdminString"
_AlaHAVlanClusterName_Object = MibTableColumn
alaHAVlanClusterName = _AlaHAVlanClusterName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 2),
    _AlaHAVlanClusterName_Type()
)
alaHAVlanClusterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterName.setStatus("current")


class _AlaHAVlanClusterAdminStatus_Type(Integer32):
    """Custom type alaHAVlanClusterAdminStatus based on Integer32"""
    defaultValue = 1

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


_AlaHAVlanClusterAdminStatus_Type.__name__ = "Integer32"
_AlaHAVlanClusterAdminStatus_Object = MibTableColumn
alaHAVlanClusterAdminStatus = _AlaHAVlanClusterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 3),
    _AlaHAVlanClusterAdminStatus_Type()
)
alaHAVlanClusterAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterAdminStatus.setStatus("current")


class _AlaHAVlanClusterOperStatus_Type(Integer32):
    """Custom type alaHAVlanClusterOperStatus based on Integer32"""
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


_AlaHAVlanClusterOperStatus_Type.__name__ = "Integer32"
_AlaHAVlanClusterOperStatus_Object = MibTableColumn
alaHAVlanClusterOperStatus = _AlaHAVlanClusterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 4),
    _AlaHAVlanClusterOperStatus_Type()
)
alaHAVlanClusterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaHAVlanClusterOperStatus.setStatus("current")


class _AlaHAVlanClusterOperStatusFlag_Type(Integer32):
    """Custom type alaHAVlanClusterOperStatusFlag based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("ipinterfacedown", 4),
          ("noigmpmembers", 5),
          ("nomacaddress", 6),
          ("nomulticastip", 7),
          ("novlan", 1),
          ("vlandown", 2),
          ("vpanotforwarding", 3))
    )


_AlaHAVlanClusterOperStatusFlag_Type.__name__ = "Integer32"
_AlaHAVlanClusterOperStatusFlag_Object = MibTableColumn
alaHAVlanClusterOperStatusFlag = _AlaHAVlanClusterOperStatusFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 5),
    _AlaHAVlanClusterOperStatusFlag_Type()
)
alaHAVlanClusterOperStatusFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaHAVlanClusterOperStatusFlag.setStatus("current")


class _AlaHAVlanClusterMode_Type(Integer32):
    """Custom type alaHAVlanClusterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2mode", 1),
          ("l3mode", 2))
    )


_AlaHAVlanClusterMode_Type.__name__ = "Integer32"
_AlaHAVlanClusterMode_Object = MibTableColumn
alaHAVlanClusterMode = _AlaHAVlanClusterMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 6),
    _AlaHAVlanClusterMode_Type()
)
alaHAVlanClusterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterMode.setStatus("current")


class _AlaHAVlanClusterVlan_Type(Integer32):
    """Custom type alaHAVlanClusterVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaHAVlanClusterVlan_Type.__name__ = "Integer32"
_AlaHAVlanClusterVlan_Object = MibTableColumn
alaHAVlanClusterVlan = _AlaHAVlanClusterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 7),
    _AlaHAVlanClusterVlan_Type()
)
alaHAVlanClusterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterVlan.setStatus("current")


class _AlaHAVlanClusterMacAddressType_Type(Integer32):
    """Custom type alaHAVlanClusterMacAddressType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 1),
          ("static", 2))
    )


_AlaHAVlanClusterMacAddressType_Type.__name__ = "Integer32"
_AlaHAVlanClusterMacAddressType_Object = MibTableColumn
alaHAVlanClusterMacAddressType = _AlaHAVlanClusterMacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 8),
    _AlaHAVlanClusterMacAddressType_Type()
)
alaHAVlanClusterMacAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterMacAddressType.setStatus("current")


class _AlaHAVlanClusterMacAddress_Type(MacAddress):
    """Custom type alaHAVlanClusterMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaHAVlanClusterMacAddress_Object = MibTableColumn
alaHAVlanClusterMacAddress = _AlaHAVlanClusterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 9),
    _AlaHAVlanClusterMacAddress_Type()
)
alaHAVlanClusterMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterMacAddress.setStatus("current")


class _AlaHAVlanClusterInetAddressType_Type(InetAddressType):
    """Custom type alaHAVlanClusterInetAddressType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AlaHAVlanClusterInetAddressType_Type.__name__ = "InetAddressType"
_AlaHAVlanClusterInetAddressType_Object = MibTableColumn
alaHAVlanClusterInetAddressType = _AlaHAVlanClusterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 10),
    _AlaHAVlanClusterInetAddressType_Type()
)
alaHAVlanClusterInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterInetAddressType.setStatus("current")


class _AlaHAVlanClusterInetAddress_Type(InetAddress):
    """Custom type alaHAVlanClusterInetAddress based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AlaHAVlanClusterInetAddress_Type.__name__ = "InetAddress"
_AlaHAVlanClusterInetAddress_Object = MibTableColumn
alaHAVlanClusterInetAddress = _AlaHAVlanClusterInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 11),
    _AlaHAVlanClusterInetAddress_Type()
)
alaHAVlanClusterInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterInetAddress.setStatus("current")


class _AlaHAVlanClusterMulticastStatus_Type(Integer32):
    """Custom type alaHAVlanClusterMulticastStatus based on Integer32"""
    defaultValue = 2

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


_AlaHAVlanClusterMulticastStatus_Type.__name__ = "Integer32"
_AlaHAVlanClusterMulticastStatus_Object = MibTableColumn
alaHAVlanClusterMulticastStatus = _AlaHAVlanClusterMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 12),
    _AlaHAVlanClusterMulticastStatus_Type()
)
alaHAVlanClusterMulticastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterMulticastStatus.setStatus("current")


class _AlaHAVlanClusterMulticastInetAddressType_Type(InetAddressType):
    """Custom type alaHAVlanClusterMulticastInetAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaHAVlanClusterMulticastInetAddressType_Type.__name__ = "InetAddressType"
_AlaHAVlanClusterMulticastInetAddressType_Object = MibTableColumn
alaHAVlanClusterMulticastInetAddressType = _AlaHAVlanClusterMulticastInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 13),
    _AlaHAVlanClusterMulticastInetAddressType_Type()
)
alaHAVlanClusterMulticastInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterMulticastInetAddressType.setStatus("current")


class _AlaHAVlanClusterMulticastInetAddress_Type(InetAddress):
    """Custom type alaHAVlanClusterMulticastInetAddress based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AlaHAVlanClusterMulticastInetAddress_Type.__name__ = "InetAddress"
_AlaHAVlanClusterMulticastInetAddress_Object = MibTableColumn
alaHAVlanClusterMulticastInetAddress = _AlaHAVlanClusterMulticastInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 14),
    _AlaHAVlanClusterMulticastInetAddress_Type()
)
alaHAVlanClusterMulticastInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterMulticastInetAddress.setStatus("current")
_AlaHAVlanClusterRowStatus_Type = RowStatus
_AlaHAVlanClusterRowStatus_Object = MibTableColumn
alaHAVlanClusterRowStatus = _AlaHAVlanClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 15),
    _AlaHAVlanClusterRowStatus_Type()
)
alaHAVlanClusterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterRowStatus.setStatus("current")


class _AlaHAVlanClusterMcmStatus_Type(Integer32):
    """Custom type alaHAVlanClusterMcmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("outofSync", 2))
    )


_AlaHAVlanClusterMcmStatus_Type.__name__ = "Integer32"
_AlaHAVlanClusterMcmStatus_Object = MibTableColumn
alaHAVlanClusterMcmStatus = _AlaHAVlanClusterMcmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 16),
    _AlaHAVlanClusterMcmStatus_Type()
)
alaHAVlanClusterMcmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaHAVlanClusterMcmStatus.setStatus("current")


class _AlaHAVlanClusterMcmStatusFlag_Type(Integer32):
    """Custom type alaHAVlanClusterMcmStatusFlag based on Integer32"""
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
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("allportmodenotsupported", 3),
          ("arptypemismatch", 8),
          ("igmpstatusmismatch", 9),
          ("invalidmac", 12),
          ("ipmismatch", 7),
          ("macmismatch", 6),
          ("mcastipmismatch", 10),
          ("mcdown", 1),
          ("modemismatch", 4),
          ("noflag", 14),
          ("nonvipvlannotsupportedinl3mode", 13),
          ("operationaldown", 2),
          ("syncinprogress", 11),
          ("vlanmismatch", 5))
    )


_AlaHAVlanClusterMcmStatusFlag_Type.__name__ = "Integer32"
_AlaHAVlanClusterMcmStatusFlag_Object = MibTableColumn
alaHAVlanClusterMcmStatusFlag = _AlaHAVlanClusterMcmStatusFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 17),
    _AlaHAVlanClusterMcmStatusFlag_Type()
)
alaHAVlanClusterMcmStatusFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaHAVlanClusterMcmStatusFlag.setStatus("current")


class _AlaHAVlanClusterVflStatus_Type(Integer32):
    """Custom type alaHAVlanClusterVflStatus based on Integer32"""
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


_AlaHAVlanClusterVflStatus_Type.__name__ = "Integer32"
_AlaHAVlanClusterVflStatus_Object = MibTableColumn
alaHAVlanClusterVflStatus = _AlaHAVlanClusterVflStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 1, 1, 1, 18),
    _AlaHAVlanClusterVflStatus_Type()
)
alaHAVlanClusterVflStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaHAVlanClusterVflStatus.setStatus("current")
_AlaHAVlanClusterPort_ObjectIdentity = ObjectIdentity
alaHAVlanClusterPort = _AlaHAVlanClusterPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2)
)
_AlaHAVlanClusterPortTable_Object = MibTable
alaHAVlanClusterPortTable = _AlaHAVlanClusterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaHAVlanClusterPortTable.setStatus("current")
_AlaHAVlanClusterPortEntry_Object = MibTableRow
alaHAVlanClusterPortEntry = _AlaHAVlanClusterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1)
)
alaHAVlanClusterPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"),
    (0, "ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortIfIndex"),
)
if mibBuilder.loadTexts:
    alaHAVlanClusterPortEntry.setStatus("current")
_AlaHAVlanClusterPortIfIndex_Type = InterfaceIndex
_AlaHAVlanClusterPortIfIndex_Object = MibTableColumn
alaHAVlanClusterPortIfIndex = _AlaHAVlanClusterPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1, 1),
    _AlaHAVlanClusterPortIfIndex_Type()
)
alaHAVlanClusterPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaHAVlanClusterPortIfIndex.setStatus("current")
_AlaHAVlanClusterPortRowStatus_Type = RowStatus
_AlaHAVlanClusterPortRowStatus_Object = MibTableColumn
alaHAVlanClusterPortRowStatus = _AlaHAVlanClusterPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1, 2),
    _AlaHAVlanClusterPortRowStatus_Type()
)
alaHAVlanClusterPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaHAVlanClusterPortRowStatus.setStatus("current")


class _AlaHAVlanClusterPortType_Type(Integer32):
    """Custom type alaHAVlanClusterPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_AlaHAVlanClusterPortType_Type.__name__ = "Integer32"
_AlaHAVlanClusterPortType_Object = MibTableColumn
alaHAVlanClusterPortType = _AlaHAVlanClusterPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1, 3),
    _AlaHAVlanClusterPortType_Type()
)
alaHAVlanClusterPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaHAVlanClusterPortType.setStatus("current")


class _AlaHAVlanClusterPortValid_Type(Integer32):
    """Custom type alaHAVlanClusterPortValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AlaHAVlanClusterPortValid_Type.__name__ = "Integer32"
_AlaHAVlanClusterPortValid_Object = MibTableColumn
alaHAVlanClusterPortValid = _AlaHAVlanClusterPortValid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 2, 1, 1, 4),
    _AlaHAVlanClusterPortValid_Type()
)
alaHAVlanClusterPortValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaHAVlanClusterPortValid.setStatus("current")
_AlaHAVlanNotificationObj_ObjectIdentity = ObjectIdentity
alaHAVlanNotificationObj = _AlaHAVlanNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 3)
)
_AlaHAVlanMultiChassisId_Type = MultiChassisId
_AlaHAVlanMultiChassisId_Object = MibScalar
alaHAVlanMultiChassisId = _AlaHAVlanMultiChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 1, 3, 1),
    _AlaHAVlanMultiChassisId_Type()
)
alaHAVlanMultiChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaHAVlanMultiChassisId.setStatus("current")
_AlcatelIND1HAVlanMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1HAVlanMIBConformance = _AlcatelIND1HAVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1HAVlanMIBConformance.setStatus("current")
_AlcatelIND1HAVlanMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1HAVlanMIBGroups = _AlcatelIND1HAVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1HAVlanMIBGroups.setStatus("current")
_AlcatelIND1HAVlanMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1HAVlanMIBCompliances = _AlcatelIND1HAVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1HAVlanMIBCompliances.setStatus("current")

# Managed Objects groups

alaHAVlanClusterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1, 1)
)
alaHAVlanClusterGroup.setObjects(
      *(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterName"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterAdminStatus"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterOperStatus"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterOperStatusFlag"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMode"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterVlan"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMacAddressType"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMacAddress"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterInetAddressType"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterInetAddress"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMulticastStatus"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMulticastInetAddressType"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMulticastInetAddress"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterRowStatus"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMcmStatus"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMcmStatusFlag"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterVflStatus"))
)
if mibBuilder.loadTexts:
    alaHAVlanClusterGroup.setStatus("current")

alaHAVlanClusterPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1, 2)
)
alaHAVlanClusterPortGroup.setObjects(
      *(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortIfIndex"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortRowStatus"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortType"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortValid"))
)
if mibBuilder.loadTexts:
    alaHAVlanClusterPortGroup.setStatus("current")

alaHAVlanNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1, 3)
)
alaHAVlanNotificationObjectGroup.setObjects(
    ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanMultiChassisId")
)
if mibBuilder.loadTexts:
    alaHAVlanNotificationObjectGroup.setStatus("current")


# Notification objects

alaHAVlanClusterPeerMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 0, 1)
)
alaHAVlanClusterPeerMismatch.setObjects(
    ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId")
)
if mibBuilder.loadTexts:
    alaHAVlanClusterPeerMismatch.setStatus(
        "current"
    )

alaHAVlanMCPeerMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 0, 2)
)
alaHAVlanMCPeerMismatch.setObjects(
      *(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanMultiChassisId"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortIfIndex"))
)
if mibBuilder.loadTexts:
    alaHAVlanMCPeerMismatch.setStatus(
        "current"
    )

alaHAVlanDynamicMAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 0, 3)
)
alaHAVlanDynamicMAC.setObjects(
      *(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterId"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterInetAddress"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterMacAddress"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPortIfIndex"))
)
if mibBuilder.loadTexts:
    alaHAVlanDynamicMAC.setStatus(
        "current"
    )


# Notifications groups

alaHAVlanNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 1, 4)
)
alaHAVlanNotificationGroup.setObjects(
      *(("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanClusterPeerMismatch"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanMCPeerMismatch"),
        ("ALCATEL-IND1-HA-VLAN-MIB", "alaHAVlanDynamicMAC"))
)
if mibBuilder.loadTexts:
    alaHAVlanNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1HAVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 64, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1HAVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-HA-VLAN-MIB",
    **{"alcatelIND1HAVlanMIB": alcatelIND1HAVlanMIB,
       "alcatelIND1HAVlanMIBNotifications": alcatelIND1HAVlanMIBNotifications,
       "alaHAVlanClusterPeerMismatch": alaHAVlanClusterPeerMismatch,
       "alaHAVlanMCPeerMismatch": alaHAVlanMCPeerMismatch,
       "alaHAVlanDynamicMAC": alaHAVlanDynamicMAC,
       "alcatelIND1HAVlanMIBObjects": alcatelIND1HAVlanMIBObjects,
       "alaHAVlanCluster": alaHAVlanCluster,
       "alaHAVlanClusterTable": alaHAVlanClusterTable,
       "alaHAVlanClusterEntry": alaHAVlanClusterEntry,
       "alaHAVlanClusterId": alaHAVlanClusterId,
       "alaHAVlanClusterName": alaHAVlanClusterName,
       "alaHAVlanClusterAdminStatus": alaHAVlanClusterAdminStatus,
       "alaHAVlanClusterOperStatus": alaHAVlanClusterOperStatus,
       "alaHAVlanClusterOperStatusFlag": alaHAVlanClusterOperStatusFlag,
       "alaHAVlanClusterMode": alaHAVlanClusterMode,
       "alaHAVlanClusterVlan": alaHAVlanClusterVlan,
       "alaHAVlanClusterMacAddressType": alaHAVlanClusterMacAddressType,
       "alaHAVlanClusterMacAddress": alaHAVlanClusterMacAddress,
       "alaHAVlanClusterInetAddressType": alaHAVlanClusterInetAddressType,
       "alaHAVlanClusterInetAddress": alaHAVlanClusterInetAddress,
       "alaHAVlanClusterMulticastStatus": alaHAVlanClusterMulticastStatus,
       "alaHAVlanClusterMulticastInetAddressType": alaHAVlanClusterMulticastInetAddressType,
       "alaHAVlanClusterMulticastInetAddress": alaHAVlanClusterMulticastInetAddress,
       "alaHAVlanClusterRowStatus": alaHAVlanClusterRowStatus,
       "alaHAVlanClusterMcmStatus": alaHAVlanClusterMcmStatus,
       "alaHAVlanClusterMcmStatusFlag": alaHAVlanClusterMcmStatusFlag,
       "alaHAVlanClusterVflStatus": alaHAVlanClusterVflStatus,
       "alaHAVlanClusterPort": alaHAVlanClusterPort,
       "alaHAVlanClusterPortTable": alaHAVlanClusterPortTable,
       "alaHAVlanClusterPortEntry": alaHAVlanClusterPortEntry,
       "alaHAVlanClusterPortIfIndex": alaHAVlanClusterPortIfIndex,
       "alaHAVlanClusterPortRowStatus": alaHAVlanClusterPortRowStatus,
       "alaHAVlanClusterPortType": alaHAVlanClusterPortType,
       "alaHAVlanClusterPortValid": alaHAVlanClusterPortValid,
       "alaHAVlanNotificationObj": alaHAVlanNotificationObj,
       "alaHAVlanMultiChassisId": alaHAVlanMultiChassisId,
       "alcatelIND1HAVlanMIBConformance": alcatelIND1HAVlanMIBConformance,
       "alcatelIND1HAVlanMIBGroups": alcatelIND1HAVlanMIBGroups,
       "alaHAVlanClusterGroup": alaHAVlanClusterGroup,
       "alaHAVlanClusterPortGroup": alaHAVlanClusterPortGroup,
       "alaHAVlanNotificationObjectGroup": alaHAVlanNotificationObjectGroup,
       "alaHAVlanNotificationGroup": alaHAVlanNotificationGroup,
       "alcatelIND1HAVlanMIBCompliances": alcatelIND1HAVlanMIBCompliances,
       "alcatelIND1HAVlanMIBCompliance": alcatelIND1HAVlanMIBCompliance}
)
