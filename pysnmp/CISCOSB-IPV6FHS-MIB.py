# SNMP MIB module (CISCOSB-IPV6FHS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-IPV6FHS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:26 2024
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

(VlanList1,
 VlanList2,
 VlanList3,
 VlanList4) = mibBuilder.importSymbols(
    "CISCOSB-BRIDGEMIBOBJECTS-MIB",
    "VlanList1",
    "VlanList2",
    "VlanList3",
    "VlanList4")

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "CISCOSB-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(rlMacMulticast,
 rndNotifications,
 switch001) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "rlMacMulticast",
    "rndNotifications",
    "switch001")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanId,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "VlanIndex")

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

rlIpv6Fhs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215)
)
rlIpv6Fhs.setRevisions(
        ("2012-12-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlIpv6FhsSettingStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unspecified", -1))
    )



class RlIpv6FhsSettingType(Integer32, TextualConvention):
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
        *(("default", 1),
          ("global", 2),
          ("port", 4),
          ("vlan", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RlFirstHopSec_ObjectIdentity = ObjectIdentity
rlFirstHopSec = _RlFirstHopSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1)
)
_RlFirstHopSecPolicyTable_Object = MibTable
rlFirstHopSecPolicyTable = _RlFirstHopSecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 1)
)
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyTable.setStatus("current")
_RlFirstHopSecPolicyEntry_Object = MibTableRow
rlFirstHopSecPolicyEntry = _RlFirstHopSecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 1, 1)
)
rlFirstHopSecPolicyEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecPolicyName"),
)
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyEntry.setStatus("current")


class _RlFirstHopSecPolicyName_Type(DisplayString):
    """Custom type rlFirstHopSecPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlFirstHopSecPolicyName_Type.__name__ = "DisplayString"
_RlFirstHopSecPolicyName_Object = MibTableColumn
rlFirstHopSecPolicyName = _RlFirstHopSecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 1, 1, 1),
    _RlFirstHopSecPolicyName_Type()
)
rlFirstHopSecPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyName.setStatus("current")


class _RlFirstHopSecPolicyLogDrop_Type(RlIpv6FhsSettingStatusType):
    """Custom type rlFirstHopSecPolicyLogDrop based on RlIpv6FhsSettingStatusType"""


_RlFirstHopSecPolicyLogDrop_Object = MibTableColumn
rlFirstHopSecPolicyLogDrop = _RlFirstHopSecPolicyLogDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 1, 1, 2),
    _RlFirstHopSecPolicyLogDrop_Type()
)
rlFirstHopSecPolicyLogDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyLogDrop.setStatus("current")
_RlFirstHopSecPolicyRowStatus_Type = RowStatus
_RlFirstHopSecPolicyRowStatus_Object = MibTableColumn
rlFirstHopSecPolicyRowStatus = _RlFirstHopSecPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 1, 1, 3),
    _RlFirstHopSecPolicyRowStatus_Type()
)
rlFirstHopSecPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyRowStatus.setStatus("current")
_RlFirstHopSecPortPolicyTable_Object = MibTable
rlFirstHopSecPortPolicyTable = _RlFirstHopSecPortPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 2)
)
if mibBuilder.loadTexts:
    rlFirstHopSecPortPolicyTable.setStatus("current")
_RlFirstHopSecPortPolicyEntry_Object = MibTableRow
rlFirstHopSecPortPolicyEntry = _RlFirstHopSecPortPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 2, 1)
)
rlFirstHopSecPortPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecPortPolicyIfIndex"),
    (1, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecPortPolicyName"),
)
if mibBuilder.loadTexts:
    rlFirstHopSecPortPolicyEntry.setStatus("current")
_RlFirstHopSecPortPolicyIfIndex_Type = InterfaceIndex
_RlFirstHopSecPortPolicyIfIndex_Object = MibTableColumn
rlFirstHopSecPortPolicyIfIndex = _RlFirstHopSecPortPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 2, 1, 1),
    _RlFirstHopSecPortPolicyIfIndex_Type()
)
rlFirstHopSecPortPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecPortPolicyIfIndex.setStatus("current")


class _RlFirstHopSecPortPolicyName_Type(DisplayString):
    """Custom type rlFirstHopSecPortPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlFirstHopSecPortPolicyName_Type.__name__ = "DisplayString"
_RlFirstHopSecPortPolicyName_Object = MibTableColumn
rlFirstHopSecPortPolicyName = _RlFirstHopSecPortPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 2, 1, 2),
    _RlFirstHopSecPortPolicyName_Type()
)
rlFirstHopSecPortPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecPortPolicyName.setStatus("current")


class _RlFirstHopSecPortPolicyVlan1to1024_Type(OctetString):
    """Custom type rlFirstHopSecPortPolicyVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPortPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlFirstHopSecPortPolicyVlan1to1024_Object = MibTableColumn
rlFirstHopSecPortPolicyVlan1to1024 = _RlFirstHopSecPortPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 2, 1, 3),
    _RlFirstHopSecPortPolicyVlan1to1024_Type()
)
rlFirstHopSecPortPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecPortPolicyVlan1to1024.setStatus("current")


class _RlFirstHopSecPortPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlFirstHopSecPortPolicyVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPortPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlFirstHopSecPortPolicyVlan1025to2048_Object = MibTableColumn
rlFirstHopSecPortPolicyVlan1025to2048 = _RlFirstHopSecPortPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 2, 1, 4),
    _RlFirstHopSecPortPolicyVlan1025to2048_Type()
)
rlFirstHopSecPortPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecPortPolicyVlan1025to2048.setStatus("current")


class _RlFirstHopSecPortPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlFirstHopSecPortPolicyVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPortPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlFirstHopSecPortPolicyVlan2049to3072_Object = MibTableColumn
rlFirstHopSecPortPolicyVlan2049to3072 = _RlFirstHopSecPortPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 2, 1, 5),
    _RlFirstHopSecPortPolicyVlan2049to3072_Type()
)
rlFirstHopSecPortPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecPortPolicyVlan2049to3072.setStatus("current")


class _RlFirstHopSecPortPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlFirstHopSecPortPolicyVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPortPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlFirstHopSecPortPolicyVlan3073to4094_Object = MibTableColumn
rlFirstHopSecPortPolicyVlan3073to4094 = _RlFirstHopSecPortPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 2, 1, 6),
    _RlFirstHopSecPortPolicyVlan3073to4094_Type()
)
rlFirstHopSecPortPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecPortPolicyVlan3073to4094.setStatus("current")
_RlFirstHopSecPortPolicyRowStatus_Type = RowStatus
_RlFirstHopSecPortPolicyRowStatus_Object = MibTableColumn
rlFirstHopSecPortPolicyRowStatus = _RlFirstHopSecPortPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 2, 1, 7),
    _RlFirstHopSecPortPolicyRowStatus_Type()
)
rlFirstHopSecPortPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlFirstHopSecPortPolicyRowStatus.setStatus("current")
_RlFirstHopSecPolicyPortTable_Object = MibTable
rlFirstHopSecPolicyPortTable = _RlFirstHopSecPolicyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 3)
)
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyPortTable.setStatus("current")
_RlFirstHopSecPolicyPortEntry_Object = MibTableRow
rlFirstHopSecPolicyPortEntry = _RlFirstHopSecPolicyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 3, 1)
)
rlFirstHopSecPolicyPortEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecPolicyPortName"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecPolicyPortIfIndex"),
)
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyPortEntry.setStatus("current")


class _RlFirstHopSecPolicyPortName_Type(DisplayString):
    """Custom type rlFirstHopSecPolicyPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlFirstHopSecPolicyPortName_Type.__name__ = "DisplayString"
_RlFirstHopSecPolicyPortName_Object = MibTableColumn
rlFirstHopSecPolicyPortName = _RlFirstHopSecPolicyPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 3, 1, 1),
    _RlFirstHopSecPolicyPortName_Type()
)
rlFirstHopSecPolicyPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyPortName.setStatus("current")
_RlFirstHopSecPolicyPortIfIndex_Type = InterfaceIndex
_RlFirstHopSecPolicyPortIfIndex_Object = MibTableColumn
rlFirstHopSecPolicyPortIfIndex = _RlFirstHopSecPolicyPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 3, 1, 2),
    _RlFirstHopSecPolicyPortIfIndex_Type()
)
rlFirstHopSecPolicyPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyPortIfIndex.setStatus("current")


class _RlFirstHopSecPolicyPortVlan1to1024_Type(OctetString):
    """Custom type rlFirstHopSecPolicyPortVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPolicyPortVlan1to1024_Type.__name__ = "OctetString"
_RlFirstHopSecPolicyPortVlan1to1024_Object = MibTableColumn
rlFirstHopSecPolicyPortVlan1to1024 = _RlFirstHopSecPolicyPortVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 3, 1, 3),
    _RlFirstHopSecPolicyPortVlan1to1024_Type()
)
rlFirstHopSecPolicyPortVlan1to1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyPortVlan1to1024.setStatus("current")


class _RlFirstHopSecPolicyPortVlan1025to2048_Type(OctetString):
    """Custom type rlFirstHopSecPolicyPortVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPolicyPortVlan1025to2048_Type.__name__ = "OctetString"
_RlFirstHopSecPolicyPortVlan1025to2048_Object = MibTableColumn
rlFirstHopSecPolicyPortVlan1025to2048 = _RlFirstHopSecPolicyPortVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 3, 1, 4),
    _RlFirstHopSecPolicyPortVlan1025to2048_Type()
)
rlFirstHopSecPolicyPortVlan1025to2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyPortVlan1025to2048.setStatus("current")


class _RlFirstHopSecPolicyPortVlan2049to3072_Type(OctetString):
    """Custom type rlFirstHopSecPolicyPortVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPolicyPortVlan2049to3072_Type.__name__ = "OctetString"
_RlFirstHopSecPolicyPortVlan2049to3072_Object = MibTableColumn
rlFirstHopSecPolicyPortVlan2049to3072 = _RlFirstHopSecPolicyPortVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 3, 1, 5),
    _RlFirstHopSecPolicyPortVlan2049to3072_Type()
)
rlFirstHopSecPolicyPortVlan2049to3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyPortVlan2049to3072.setStatus("current")


class _RlFirstHopSecPolicyPortVlan3073to4094_Type(OctetString):
    """Custom type rlFirstHopSecPolicyPortVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPolicyPortVlan3073to4094_Type.__name__ = "OctetString"
_RlFirstHopSecPolicyPortVlan3073to4094_Object = MibTableColumn
rlFirstHopSecPolicyPortVlan3073to4094 = _RlFirstHopSecPolicyPortVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 3, 1, 6),
    _RlFirstHopSecPolicyPortVlan3073to4094_Type()
)
rlFirstHopSecPolicyPortVlan3073to4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyPortVlan3073to4094.setStatus("current")
_RlFirstHopSecVlanPolicyTable_Object = MibTable
rlFirstHopSecVlanPolicyTable = _RlFirstHopSecVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 4)
)
if mibBuilder.loadTexts:
    rlFirstHopSecVlanPolicyTable.setStatus("current")
_RlFirstHopSecVlanPolicyEntry_Object = MibTableRow
rlFirstHopSecVlanPolicyEntry = _RlFirstHopSecVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 4, 1)
)
rlFirstHopSecVlanPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecVlanPolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlFirstHopSecVlanPolicyEntry.setStatus("current")
_RlFirstHopSecVlanPolicyVlanTag_Type = VlanId
_RlFirstHopSecVlanPolicyVlanTag_Object = MibTableColumn
rlFirstHopSecVlanPolicyVlanTag = _RlFirstHopSecVlanPolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 4, 1, 1),
    _RlFirstHopSecVlanPolicyVlanTag_Type()
)
rlFirstHopSecVlanPolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecVlanPolicyVlanTag.setStatus("current")


class _RlFirstHopSecVlanPolicyName_Type(DisplayString):
    """Custom type rlFirstHopSecVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlFirstHopSecVlanPolicyName_Type.__name__ = "DisplayString"
_RlFirstHopSecVlanPolicyName_Object = MibTableColumn
rlFirstHopSecVlanPolicyName = _RlFirstHopSecVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 4, 1, 2),
    _RlFirstHopSecVlanPolicyName_Type()
)
rlFirstHopSecVlanPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecVlanPolicyName.setStatus("current")
_RlFirstHopSecVlanPolicyRowStatus_Type = RowStatus
_RlFirstHopSecVlanPolicyRowStatus_Object = MibTableColumn
rlFirstHopSecVlanPolicyRowStatus = _RlFirstHopSecVlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 4, 1, 3),
    _RlFirstHopSecVlanPolicyRowStatus_Type()
)
rlFirstHopSecVlanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlFirstHopSecVlanPolicyRowStatus.setStatus("current")
_RlFirstHopSecPolicyVlanTable_Object = MibTable
rlFirstHopSecPolicyVlanTable = _RlFirstHopSecPolicyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 5)
)
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyVlanTable.setStatus("current")
_RlFirstHopSecPolicyVlanEntry_Object = MibTableRow
rlFirstHopSecPolicyVlanEntry = _RlFirstHopSecPolicyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 5, 1)
)
rlFirstHopSecPolicyVlanEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecPolicyVlanPolicyName"),
)
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyVlanEntry.setStatus("current")


class _RlFirstHopSecPolicyVlanPolicyName_Type(DisplayString):
    """Custom type rlFirstHopSecPolicyVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlFirstHopSecPolicyVlanPolicyName_Type.__name__ = "DisplayString"
_RlFirstHopSecPolicyVlanPolicyName_Object = MibTableColumn
rlFirstHopSecPolicyVlanPolicyName = _RlFirstHopSecPolicyVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 5, 1, 1),
    _RlFirstHopSecPolicyVlanPolicyName_Type()
)
rlFirstHopSecPolicyVlanPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyVlanPolicyName.setStatus("current")


class _RlFirstHopSecPolicyVlan1to1024_Type(OctetString):
    """Custom type rlFirstHopSecPolicyVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlFirstHopSecPolicyVlan1to1024_Object = MibTableColumn
rlFirstHopSecPolicyVlan1to1024 = _RlFirstHopSecPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 5, 1, 2),
    _RlFirstHopSecPolicyVlan1to1024_Type()
)
rlFirstHopSecPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyVlan1to1024.setStatus("current")


class _RlFirstHopSecPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlFirstHopSecPolicyVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlFirstHopSecPolicyVlan1025to2048_Object = MibTableColumn
rlFirstHopSecPolicyVlan1025to2048 = _RlFirstHopSecPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 5, 1, 3),
    _RlFirstHopSecPolicyVlan1025to2048_Type()
)
rlFirstHopSecPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyVlan1025to2048.setStatus("current")


class _RlFirstHopSecPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlFirstHopSecPolicyVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlFirstHopSecPolicyVlan2049to3072_Object = MibTableColumn
rlFirstHopSecPolicyVlan2049to3072 = _RlFirstHopSecPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 5, 1, 4),
    _RlFirstHopSecPolicyVlan2049to3072_Type()
)
rlFirstHopSecPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyVlan2049to3072.setStatus("current")


class _RlFirstHopSecPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlFirstHopSecPolicyVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlFirstHopSecPolicyVlan3073to4094_Object = MibTableColumn
rlFirstHopSecPolicyVlan3073to4094 = _RlFirstHopSecPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 5, 1, 5),
    _RlFirstHopSecPolicyVlan3073to4094_Type()
)
rlFirstHopSecPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecPolicyVlan3073to4094.setStatus("current")
_RlFirstHopSecEnableVlanTable_Object = MibTable
rlFirstHopSecEnableVlanTable = _RlFirstHopSecEnableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 6)
)
if mibBuilder.loadTexts:
    rlFirstHopSecEnableVlanTable.setStatus("current")
_RlFirstHopSecEnableVlanEntry_Object = MibTableRow
rlFirstHopSecEnableVlanEntry = _RlFirstHopSecEnableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 6, 1)
)
rlFirstHopSecEnableVlanEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecEnableVlanIndex"),
)
if mibBuilder.loadTexts:
    rlFirstHopSecEnableVlanEntry.setStatus("current")


class _RlFirstHopSecEnableVlanIndex_Type(Integer32):
    """Custom type rlFirstHopSecEnableVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )


_RlFirstHopSecEnableVlanIndex_Type.__name__ = "Integer32"
_RlFirstHopSecEnableVlanIndex_Object = MibTableColumn
rlFirstHopSecEnableVlanIndex = _RlFirstHopSecEnableVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 6, 1, 1),
    _RlFirstHopSecEnableVlanIndex_Type()
)
rlFirstHopSecEnableVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecEnableVlanIndex.setStatus("current")


class _RlFirstHopSecEnableVlan1to1024_Type(OctetString):
    """Custom type rlFirstHopSecEnableVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecEnableVlan1to1024_Type.__name__ = "OctetString"
_RlFirstHopSecEnableVlan1to1024_Object = MibTableColumn
rlFirstHopSecEnableVlan1to1024 = _RlFirstHopSecEnableVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 6, 1, 2),
    _RlFirstHopSecEnableVlan1to1024_Type()
)
rlFirstHopSecEnableVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecEnableVlan1to1024.setStatus("current")


class _RlFirstHopSecEnableVlan1025to2048_Type(OctetString):
    """Custom type rlFirstHopSecEnableVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecEnableVlan1025to2048_Type.__name__ = "OctetString"
_RlFirstHopSecEnableVlan1025to2048_Object = MibTableColumn
rlFirstHopSecEnableVlan1025to2048 = _RlFirstHopSecEnableVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 6, 1, 3),
    _RlFirstHopSecEnableVlan1025to2048_Type()
)
rlFirstHopSecEnableVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecEnableVlan1025to2048.setStatus("current")


class _RlFirstHopSecEnableVlan2049to3072_Type(OctetString):
    """Custom type rlFirstHopSecEnableVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecEnableVlan2049to3072_Type.__name__ = "OctetString"
_RlFirstHopSecEnableVlan2049to3072_Object = MibTableColumn
rlFirstHopSecEnableVlan2049to3072 = _RlFirstHopSecEnableVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 6, 1, 4),
    _RlFirstHopSecEnableVlan2049to3072_Type()
)
rlFirstHopSecEnableVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecEnableVlan2049to3072.setStatus("current")


class _RlFirstHopSecEnableVlan3073to4094_Type(OctetString):
    """Custom type rlFirstHopSecEnableVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlFirstHopSecEnableVlan3073to4094_Type.__name__ = "OctetString"
_RlFirstHopSecEnableVlan3073to4094_Object = MibTableColumn
rlFirstHopSecEnableVlan3073to4094 = _RlFirstHopSecEnableVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 6, 1, 5),
    _RlFirstHopSecEnableVlan3073to4094_Type()
)
rlFirstHopSecEnableVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecEnableVlan3073to4094.setStatus("current")
_RlFirstHopSecActivePolicyTable_Object = MibTable
rlFirstHopSecActivePolicyTable = _RlFirstHopSecActivePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 7)
)
if mibBuilder.loadTexts:
    rlFirstHopSecActivePolicyTable.setStatus("current")
_RlFirstHopSecActivePolicyEntry_Object = MibTableRow
rlFirstHopSecActivePolicyEntry = _RlFirstHopSecActivePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 7, 1)
)
rlFirstHopSecActivePolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecActivePolicyIfIndex"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecActivePolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlFirstHopSecActivePolicyEntry.setStatus("current")
_RlFirstHopSecActivePolicyIfIndex_Type = InterfaceIndex
_RlFirstHopSecActivePolicyIfIndex_Object = MibTableColumn
rlFirstHopSecActivePolicyIfIndex = _RlFirstHopSecActivePolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 7, 1, 1),
    _RlFirstHopSecActivePolicyIfIndex_Type()
)
rlFirstHopSecActivePolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecActivePolicyIfIndex.setStatus("current")
_RlFirstHopSecActivePolicyVlanTag_Type = VlanId
_RlFirstHopSecActivePolicyVlanTag_Object = MibTableColumn
rlFirstHopSecActivePolicyVlanTag = _RlFirstHopSecActivePolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 7, 1, 2),
    _RlFirstHopSecActivePolicyVlanTag_Type()
)
rlFirstHopSecActivePolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecActivePolicyVlanTag.setStatus("current")


class _RlFirstHopSecActivePolicyNamePort_Type(DisplayString):
    """Custom type rlFirstHopSecActivePolicyNamePort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlFirstHopSecActivePolicyNamePort_Type.__name__ = "DisplayString"
_RlFirstHopSecActivePolicyNamePort_Object = MibTableColumn
rlFirstHopSecActivePolicyNamePort = _RlFirstHopSecActivePolicyNamePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 7, 1, 3),
    _RlFirstHopSecActivePolicyNamePort_Type()
)
rlFirstHopSecActivePolicyNamePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecActivePolicyNamePort.setStatus("current")


class _RlFirstHopSecActivePolicyNameVlan_Type(DisplayString):
    """Custom type rlFirstHopSecActivePolicyNameVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlFirstHopSecActivePolicyNameVlan_Type.__name__ = "DisplayString"
_RlFirstHopSecActivePolicyNameVlan_Object = MibTableColumn
rlFirstHopSecActivePolicyNameVlan = _RlFirstHopSecActivePolicyNameVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 7, 1, 4),
    _RlFirstHopSecActivePolicyNameVlan_Type()
)
rlFirstHopSecActivePolicyNameVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecActivePolicyNameVlan.setStatus("current")
_RlFirstHopSecActivePolicyLogDrop_Type = RlIpv6FhsSettingStatusType
_RlFirstHopSecActivePolicyLogDrop_Object = MibTableColumn
rlFirstHopSecActivePolicyLogDrop = _RlFirstHopSecActivePolicyLogDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 7, 1, 5),
    _RlFirstHopSecActivePolicyLogDrop_Type()
)
rlFirstHopSecActivePolicyLogDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecActivePolicyLogDrop.setStatus("current")
_RlFirstHopSecActivePolicyLogDropType_Type = RlIpv6FhsSettingType
_RlFirstHopSecActivePolicyLogDropType_Object = MibTableColumn
rlFirstHopSecActivePolicyLogDropType = _RlFirstHopSecActivePolicyLogDropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 7, 1, 6),
    _RlFirstHopSecActivePolicyLogDropType_Type()
)
rlFirstHopSecActivePolicyLogDropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecActivePolicyLogDropType.setStatus("current")
_RlFirstHopSecCountersTable_Object = MibTable
rlFirstHopSecCountersTable = _RlFirstHopSecCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8)
)
if mibBuilder.loadTexts:
    rlFirstHopSecCountersTable.setStatus("current")
_RlFirstHopSecCountersEntry_Object = MibTableRow
rlFirstHopSecCountersEntry = _RlFirstHopSecCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1)
)
rlFirstHopSecCountersEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlFirstHopSecCountersIfIndex"),
)
if mibBuilder.loadTexts:
    rlFirstHopSecCountersEntry.setStatus("current")
_RlFirstHopSecCountersIfIndex_Type = InterfaceIndex
_RlFirstHopSecCountersIfIndex_Object = MibTableColumn
rlFirstHopSecCountersIfIndex = _RlFirstHopSecCountersIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 1),
    _RlFirstHopSecCountersIfIndex_Type()
)
rlFirstHopSecCountersIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersIfIndex.setStatus("current")
_RlFirstHopSecCountersRxNdpRA_Type = Counter32
_RlFirstHopSecCountersRxNdpRA_Object = MibTableColumn
rlFirstHopSecCountersRxNdpRA = _RlFirstHopSecCountersRxNdpRA_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 2),
    _RlFirstHopSecCountersRxNdpRA_Type()
)
rlFirstHopSecCountersRxNdpRA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxNdpRA.setStatus("current")
_RlFirstHopSecCountersDropNdpRA_Type = Counter32
_RlFirstHopSecCountersDropNdpRA_Object = MibTableColumn
rlFirstHopSecCountersDropNdpRA = _RlFirstHopSecCountersDropNdpRA_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 3),
    _RlFirstHopSecCountersDropNdpRA_Type()
)
rlFirstHopSecCountersDropNdpRA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNdpRA.setStatus("current")
_RlFirstHopSecCountersRxNdpRS_Type = Counter32
_RlFirstHopSecCountersRxNdpRS_Object = MibTableColumn
rlFirstHopSecCountersRxNdpRS = _RlFirstHopSecCountersRxNdpRS_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 4),
    _RlFirstHopSecCountersRxNdpRS_Type()
)
rlFirstHopSecCountersRxNdpRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxNdpRS.setStatus("current")
_RlFirstHopSecCountersDropNdpRS_Type = Counter32
_RlFirstHopSecCountersDropNdpRS_Object = MibTableColumn
rlFirstHopSecCountersDropNdpRS = _RlFirstHopSecCountersDropNdpRS_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 5),
    _RlFirstHopSecCountersDropNdpRS_Type()
)
rlFirstHopSecCountersDropNdpRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNdpRS.setStatus("current")
_RlFirstHopSecCountersRxNdpNA_Type = Counter32
_RlFirstHopSecCountersRxNdpNA_Object = MibTableColumn
rlFirstHopSecCountersRxNdpNA = _RlFirstHopSecCountersRxNdpNA_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 6),
    _RlFirstHopSecCountersRxNdpNA_Type()
)
rlFirstHopSecCountersRxNdpNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxNdpNA.setStatus("current")
_RlFirstHopSecCountersDropNdpNA_Type = Counter32
_RlFirstHopSecCountersDropNdpNA_Object = MibTableColumn
rlFirstHopSecCountersDropNdpNA = _RlFirstHopSecCountersDropNdpNA_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 7),
    _RlFirstHopSecCountersDropNdpNA_Type()
)
rlFirstHopSecCountersDropNdpNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNdpNA.setStatus("current")
_RlFirstHopSecCountersRxNdpNS_Type = Counter32
_RlFirstHopSecCountersRxNdpNS_Object = MibTableColumn
rlFirstHopSecCountersRxNdpNS = _RlFirstHopSecCountersRxNdpNS_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 8),
    _RlFirstHopSecCountersRxNdpNS_Type()
)
rlFirstHopSecCountersRxNdpNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxNdpNS.setStatus("current")
_RlFirstHopSecCountersDropNdpNS_Type = Counter32
_RlFirstHopSecCountersDropNdpNS_Object = MibTableColumn
rlFirstHopSecCountersDropNdpNS = _RlFirstHopSecCountersDropNdpNS_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 9),
    _RlFirstHopSecCountersDropNdpNS_Type()
)
rlFirstHopSecCountersDropNdpNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNdpNS.setStatus("current")
_RlFirstHopSecCountersRxNdpRedirect_Type = Counter32
_RlFirstHopSecCountersRxNdpRedirect_Object = MibTableColumn
rlFirstHopSecCountersRxNdpRedirect = _RlFirstHopSecCountersRxNdpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 10),
    _RlFirstHopSecCountersRxNdpRedirect_Type()
)
rlFirstHopSecCountersRxNdpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxNdpRedirect.setStatus("current")
_RlFirstHopSecCountersDropNdpRedirect_Type = Counter32
_RlFirstHopSecCountersDropNdpRedirect_Object = MibTableColumn
rlFirstHopSecCountersDropNdpRedirect = _RlFirstHopSecCountersDropNdpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 11),
    _RlFirstHopSecCountersDropNdpRedirect_Type()
)
rlFirstHopSecCountersDropNdpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNdpRedirect.setStatus("current")
_RlFirstHopSecCountersRxDhcpAdverise_Type = Counter32
_RlFirstHopSecCountersRxDhcpAdverise_Object = MibTableColumn
rlFirstHopSecCountersRxDhcpAdverise = _RlFirstHopSecCountersRxDhcpAdverise_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 12),
    _RlFirstHopSecCountersRxDhcpAdverise_Type()
)
rlFirstHopSecCountersRxDhcpAdverise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxDhcpAdverise.setStatus("current")
_RlFirstHopSecCountersDropDhcpAdverise_Type = Counter32
_RlFirstHopSecCountersDropDhcpAdverise_Object = MibTableColumn
rlFirstHopSecCountersDropDhcpAdverise = _RlFirstHopSecCountersDropDhcpAdverise_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 13),
    _RlFirstHopSecCountersDropDhcpAdverise_Type()
)
rlFirstHopSecCountersDropDhcpAdverise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropDhcpAdverise.setStatus("current")
_RlFirstHopSecCountersRxDhcpReply_Type = Counter32
_RlFirstHopSecCountersRxDhcpReply_Object = MibTableColumn
rlFirstHopSecCountersRxDhcpReply = _RlFirstHopSecCountersRxDhcpReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 14),
    _RlFirstHopSecCountersRxDhcpReply_Type()
)
rlFirstHopSecCountersRxDhcpReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxDhcpReply.setStatus("current")
_RlFirstHopSecCountersDropDhcpReply_Type = Counter32
_RlFirstHopSecCountersDropDhcpReply_Object = MibTableColumn
rlFirstHopSecCountersDropDhcpReply = _RlFirstHopSecCountersDropDhcpReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 15),
    _RlFirstHopSecCountersDropDhcpReply_Type()
)
rlFirstHopSecCountersDropDhcpReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropDhcpReply.setStatus("current")
_RlFirstHopSecCountersRxDhcpReconfigure_Type = Counter32
_RlFirstHopSecCountersRxDhcpReconfigure_Object = MibTableColumn
rlFirstHopSecCountersRxDhcpReconfigure = _RlFirstHopSecCountersRxDhcpReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 16),
    _RlFirstHopSecCountersRxDhcpReconfigure_Type()
)
rlFirstHopSecCountersRxDhcpReconfigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxDhcpReconfigure.setStatus("current")
_RlFirstHopSecCountersDropDhcpReconfigure_Type = Counter32
_RlFirstHopSecCountersDropDhcpReconfigure_Object = MibTableColumn
rlFirstHopSecCountersDropDhcpReconfigure = _RlFirstHopSecCountersDropDhcpReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 17),
    _RlFirstHopSecCountersDropDhcpReconfigure_Type()
)
rlFirstHopSecCountersDropDhcpReconfigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropDhcpReconfigure.setStatus("current")
_RlFirstHopSecCountersRxDhcpRelayReply_Type = Counter32
_RlFirstHopSecCountersRxDhcpRelayReply_Object = MibTableColumn
rlFirstHopSecCountersRxDhcpRelayReply = _RlFirstHopSecCountersRxDhcpRelayReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 18),
    _RlFirstHopSecCountersRxDhcpRelayReply_Type()
)
rlFirstHopSecCountersRxDhcpRelayReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxDhcpRelayReply.setStatus("current")
_RlFirstHopSecCountersDropDhcpRelayReply_Type = Counter32
_RlFirstHopSecCountersDropDhcpRelayReply_Object = MibTableColumn
rlFirstHopSecCountersDropDhcpRelayReply = _RlFirstHopSecCountersDropDhcpRelayReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 19),
    _RlFirstHopSecCountersDropDhcpRelayReply_Type()
)
rlFirstHopSecCountersDropDhcpRelayReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropDhcpRelayReply.setStatus("current")
_RlFirstHopSecCountersRxDhcpLeasequeryReply_Type = Counter32
_RlFirstHopSecCountersRxDhcpLeasequeryReply_Object = MibTableColumn
rlFirstHopSecCountersRxDhcpLeasequeryReply = _RlFirstHopSecCountersRxDhcpLeasequeryReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 20),
    _RlFirstHopSecCountersRxDhcpLeasequeryReply_Type()
)
rlFirstHopSecCountersRxDhcpLeasequeryReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersRxDhcpLeasequeryReply.setStatus("current")
_RlFirstHopSecCountersDropDhcpLeasequeryReply_Type = Counter32
_RlFirstHopSecCountersDropDhcpLeasequeryReply_Object = MibTableColumn
rlFirstHopSecCountersDropDhcpLeasequeryReply = _RlFirstHopSecCountersDropDhcpLeasequeryReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 21),
    _RlFirstHopSecCountersDropDhcpLeasequeryReply_Type()
)
rlFirstHopSecCountersDropDhcpLeasequeryReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropDhcpLeasequeryReply.setStatus("current")
_RlFirstHopSecCountersDropRaGuardUnauthorizedMessage_Type = Counter32
_RlFirstHopSecCountersDropRaGuardUnauthorizedMessage_Object = MibTableColumn
rlFirstHopSecCountersDropRaGuardUnauthorizedMessage = _RlFirstHopSecCountersDropRaGuardUnauthorizedMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 22),
    _RlFirstHopSecCountersDropRaGuardUnauthorizedMessage_Type()
)
rlFirstHopSecCountersDropRaGuardUnauthorizedMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropRaGuardUnauthorizedMessage.setStatus("current")
_RlFirstHopSecCountersDropRaGuardUnauthorizedHopLimit_Type = Counter32
_RlFirstHopSecCountersDropRaGuardUnauthorizedHopLimit_Object = MibTableColumn
rlFirstHopSecCountersDropRaGuardUnauthorizedHopLimit = _RlFirstHopSecCountersDropRaGuardUnauthorizedHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 23),
    _RlFirstHopSecCountersDropRaGuardUnauthorizedHopLimit_Type()
)
rlFirstHopSecCountersDropRaGuardUnauthorizedHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropRaGuardUnauthorizedHopLimit.setStatus("current")
_RlFirstHopSecCountersDropRaGuardUnauthorizedManagedConfigFlag_Type = Counter32
_RlFirstHopSecCountersDropRaGuardUnauthorizedManagedConfigFlag_Object = MibTableColumn
rlFirstHopSecCountersDropRaGuardUnauthorizedManagedConfigFlag = _RlFirstHopSecCountersDropRaGuardUnauthorizedManagedConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 24),
    _RlFirstHopSecCountersDropRaGuardUnauthorizedManagedConfigFlag_Type()
)
rlFirstHopSecCountersDropRaGuardUnauthorizedManagedConfigFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropRaGuardUnauthorizedManagedConfigFlag.setStatus("current")
_RlFirstHopSecCountersDropRaGuardUnauthorizedOtherConfigFlag_Type = Counter32
_RlFirstHopSecCountersDropRaGuardUnauthorizedOtherConfigFlag_Object = MibTableColumn
rlFirstHopSecCountersDropRaGuardUnauthorizedOtherConfigFlag = _RlFirstHopSecCountersDropRaGuardUnauthorizedOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 25),
    _RlFirstHopSecCountersDropRaGuardUnauthorizedOtherConfigFlag_Type()
)
rlFirstHopSecCountersDropRaGuardUnauthorizedOtherConfigFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropRaGuardUnauthorizedOtherConfigFlag.setStatus("current")
_RlFirstHopSecCountersDropRaGuardUnauthorizedRouterPreference_Type = Counter32
_RlFirstHopSecCountersDropRaGuardUnauthorizedRouterPreference_Object = MibTableColumn
rlFirstHopSecCountersDropRaGuardUnauthorizedRouterPreference = _RlFirstHopSecCountersDropRaGuardUnauthorizedRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 26),
    _RlFirstHopSecCountersDropRaGuardUnauthorizedRouterPreference_Type()
)
rlFirstHopSecCountersDropRaGuardUnauthorizedRouterPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropRaGuardUnauthorizedRouterPreference.setStatus("current")
_RlFirstHopSecCountersDropRaGuardUnauthorizedAdvertisedPrefix_Type = Counter32
_RlFirstHopSecCountersDropRaGuardUnauthorizedAdvertisedPrefix_Object = MibTableColumn
rlFirstHopSecCountersDropRaGuardUnauthorizedAdvertisedPrefix = _RlFirstHopSecCountersDropRaGuardUnauthorizedAdvertisedPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 27),
    _RlFirstHopSecCountersDropRaGuardUnauthorizedAdvertisedPrefix_Type()
)
rlFirstHopSecCountersDropRaGuardUnauthorizedAdvertisedPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropRaGuardUnauthorizedAdvertisedPrefix.setStatus("current")
_RlFirstHopSecCountersDropRaGuardUnauthorizedSourceAddress_Type = Counter32
_RlFirstHopSecCountersDropRaGuardUnauthorizedSourceAddress_Object = MibTableColumn
rlFirstHopSecCountersDropRaGuardUnauthorizedSourceAddress = _RlFirstHopSecCountersDropRaGuardUnauthorizedSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 28),
    _RlFirstHopSecCountersDropRaGuardUnauthorizedSourceAddress_Type()
)
rlFirstHopSecCountersDropRaGuardUnauthorizedSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropRaGuardUnauthorizedSourceAddress.setStatus("current")
_RlFirstHopSecCountersDropNdInspectionInvalidSourceMac_Type = Counter32
_RlFirstHopSecCountersDropNdInspectionInvalidSourceMac_Object = MibTableColumn
rlFirstHopSecCountersDropNdInspectionInvalidSourceMac = _RlFirstHopSecCountersDropNdInspectionInvalidSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 29),
    _RlFirstHopSecCountersDropNdInspectionInvalidSourceMac_Type()
)
rlFirstHopSecCountersDropNdInspectionInvalidSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNdInspectionInvalidSourceMac.setStatus("current")
_RlFirstHopSecCountersDropNdInspectionUnsecureMessage_Type = Counter32
_RlFirstHopSecCountersDropNdInspectionUnsecureMessage_Object = MibTableColumn
rlFirstHopSecCountersDropNdInspectionUnsecureMessage = _RlFirstHopSecCountersDropNdInspectionUnsecureMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 30),
    _RlFirstHopSecCountersDropNdInspectionUnsecureMessage_Type()
)
rlFirstHopSecCountersDropNdInspectionUnsecureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNdInspectionUnsecureMessage.setStatus("current")
_RlFirstHopSecCountersDropNdInspectionUnauthorizedSecLevel_Type = Counter32
_RlFirstHopSecCountersDropNdInspectionUnauthorizedSecLevel_Object = MibTableColumn
rlFirstHopSecCountersDropNdInspectionUnauthorizedSecLevel = _RlFirstHopSecCountersDropNdInspectionUnauthorizedSecLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 31),
    _RlFirstHopSecCountersDropNdInspectionUnauthorizedSecLevel_Type()
)
rlFirstHopSecCountersDropNdInspectionUnauthorizedSecLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNdInspectionUnauthorizedSecLevel.setStatus("current")
_RlFirstHopSecCountersDropDhcpGuardUnauthorizedMessage_Type = Counter32
_RlFirstHopSecCountersDropDhcpGuardUnauthorizedMessage_Object = MibTableColumn
rlFirstHopSecCountersDropDhcpGuardUnauthorizedMessage = _RlFirstHopSecCountersDropDhcpGuardUnauthorizedMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 32),
    _RlFirstHopSecCountersDropDhcpGuardUnauthorizedMessage_Type()
)
rlFirstHopSecCountersDropDhcpGuardUnauthorizedMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropDhcpGuardUnauthorizedMessage.setStatus("current")
_RlFirstHopSecCountersDropDhcpGuardUnauthorizedSourceAddress_Type = Counter32
_RlFirstHopSecCountersDropDhcpGuardUnauthorizedSourceAddress_Object = MibTableColumn
rlFirstHopSecCountersDropDhcpGuardUnauthorizedSourceAddress = _RlFirstHopSecCountersDropDhcpGuardUnauthorizedSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 33),
    _RlFirstHopSecCountersDropDhcpGuardUnauthorizedSourceAddress_Type()
)
rlFirstHopSecCountersDropDhcpGuardUnauthorizedSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropDhcpGuardUnauthorizedSourceAddress.setStatus("current")
_RlFirstHopSecCountersDropDhcpGuardUnauthorizedServerPreference_Type = Counter32
_RlFirstHopSecCountersDropDhcpGuardUnauthorizedServerPreference_Object = MibTableColumn
rlFirstHopSecCountersDropDhcpGuardUnauthorizedServerPreference = _RlFirstHopSecCountersDropDhcpGuardUnauthorizedServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 34),
    _RlFirstHopSecCountersDropDhcpGuardUnauthorizedServerPreference_Type()
)
rlFirstHopSecCountersDropDhcpGuardUnauthorizedServerPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropDhcpGuardUnauthorizedServerPreference.setStatus("current")
_RlFirstHopSecCountersDropDhcpGuardUnauthorizedAssignedAddress_Type = Counter32
_RlFirstHopSecCountersDropDhcpGuardUnauthorizedAssignedAddress_Object = MibTableColumn
rlFirstHopSecCountersDropDhcpGuardUnauthorizedAssignedAddress = _RlFirstHopSecCountersDropDhcpGuardUnauthorizedAssignedAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 35),
    _RlFirstHopSecCountersDropDhcpGuardUnauthorizedAssignedAddress_Type()
)
rlFirstHopSecCountersDropDhcpGuardUnauthorizedAssignedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropDhcpGuardUnauthorizedAssignedAddress.setStatus("current")
_RlFirstHopSecCountersDropSourceGuardNoBinding_Type = Counter32
_RlFirstHopSecCountersDropSourceGuardNoBinding_Object = MibTableColumn
rlFirstHopSecCountersDropSourceGuardNoBinding = _RlFirstHopSecCountersDropSourceGuardNoBinding_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 36),
    _RlFirstHopSecCountersDropSourceGuardNoBinding_Type()
)
rlFirstHopSecCountersDropSourceGuardNoBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropSourceGuardNoBinding.setStatus("current")
_RlFirstHopSecCountersDropNbrBindingIntegrityIllegalIcmpv6_Type = Counter32
_RlFirstHopSecCountersDropNbrBindingIntegrityIllegalIcmpv6_Object = MibTableColumn
rlFirstHopSecCountersDropNbrBindingIntegrityIllegalIcmpv6 = _RlFirstHopSecCountersDropNbrBindingIntegrityIllegalIcmpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 37),
    _RlFirstHopSecCountersDropNbrBindingIntegrityIllegalIcmpv6_Type()
)
rlFirstHopSecCountersDropNbrBindingIntegrityIllegalIcmpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNbrBindingIntegrityIllegalIcmpv6.setStatus("current")
_RlFirstHopSecCountersDropNbrBindingIntegrityIllegalDhcpv6_Type = Counter32
_RlFirstHopSecCountersDropNbrBindingIntegrityIllegalDhcpv6_Object = MibTableColumn
rlFirstHopSecCountersDropNbrBindingIntegrityIllegalDhcpv6 = _RlFirstHopSecCountersDropNbrBindingIntegrityIllegalDhcpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 8, 1, 38),
    _RlFirstHopSecCountersDropNbrBindingIntegrityIllegalDhcpv6_Type()
)
rlFirstHopSecCountersDropNbrBindingIntegrityIllegalDhcpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlFirstHopSecCountersDropNbrBindingIntegrityIllegalDhcpv6.setStatus("current")


class _RlFirstHopSecLogDrop_Type(Integer32):
    """Custom type rlFirstHopSecLogDrop based on Integer32"""
    defaultValue = 2

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


_RlFirstHopSecLogDrop_Type.__name__ = "Integer32"
_RlFirstHopSecLogDrop_Object = MibScalar
rlFirstHopSecLogDrop = _RlFirstHopSecLogDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 9),
    _RlFirstHopSecLogDrop_Type()
)
rlFirstHopSecLogDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecLogDrop.setStatus("current")
_RlFirstHopSecClearCounters_Type = InterfaceIndexOrZero
_RlFirstHopSecClearCounters_Object = MibScalar
rlFirstHopSecClearCounters = _RlFirstHopSecClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 1, 10),
    _RlFirstHopSecClearCounters_Type()
)
rlFirstHopSecClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlFirstHopSecClearCounters.setStatus("current")
_RlNdInspection_ObjectIdentity = ObjectIdentity
rlNdInspection = _RlNdInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2)
)
_RlNdInspectionPolicyTable_Object = MibTable
rlNdInspectionPolicyTable = _RlNdInspectionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 1)
)
if mibBuilder.loadTexts:
    rlNdInspectionPolicyTable.setStatus("current")
_RlNdInspectionPolicyEntry_Object = MibTableRow
rlNdInspectionPolicyEntry = _RlNdInspectionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 1, 1)
)
rlNdInspectionPolicyEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionPolicyName"),
)
if mibBuilder.loadTexts:
    rlNdInspectionPolicyEntry.setStatus("current")


class _RlNdInspectionPolicyName_Type(DisplayString):
    """Custom type rlNdInspectionPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNdInspectionPolicyName_Type.__name__ = "DisplayString"
_RlNdInspectionPolicyName_Object = MibTableColumn
rlNdInspectionPolicyName = _RlNdInspectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 1, 1, 1),
    _RlNdInspectionPolicyName_Type()
)
rlNdInspectionPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyName.setStatus("current")


class _RlNdInspectionPolicyDeviceRole_Type(Integer32):
    """Custom type rlNdInspectionPolicyDeviceRole based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2),
          ("unspecified", -1))
    )


_RlNdInspectionPolicyDeviceRole_Type.__name__ = "Integer32"
_RlNdInspectionPolicyDeviceRole_Object = MibTableColumn
rlNdInspectionPolicyDeviceRole = _RlNdInspectionPolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 1, 1, 2),
    _RlNdInspectionPolicyDeviceRole_Type()
)
rlNdInspectionPolicyDeviceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyDeviceRole.setStatus("current")


class _RlNdInspectionPolicyDropUnsecured_Type(RlIpv6FhsSettingStatusType):
    """Custom type rlNdInspectionPolicyDropUnsecured based on RlIpv6FhsSettingStatusType"""


_RlNdInspectionPolicyDropUnsecured_Object = MibTableColumn
rlNdInspectionPolicyDropUnsecured = _RlNdInspectionPolicyDropUnsecured_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 1, 1, 3),
    _RlNdInspectionPolicyDropUnsecured_Type()
)
rlNdInspectionPolicyDropUnsecured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyDropUnsecured.setStatus("current")


class _RlNdInspectionPolicySecLevelMin_Type(Integer32):
    """Custom type rlNdInspectionPolicySecLevelMin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_RlNdInspectionPolicySecLevelMin_Type.__name__ = "Integer32"
_RlNdInspectionPolicySecLevelMin_Object = MibTableColumn
rlNdInspectionPolicySecLevelMin = _RlNdInspectionPolicySecLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 1, 1, 4),
    _RlNdInspectionPolicySecLevelMin_Type()
)
rlNdInspectionPolicySecLevelMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPolicySecLevelMin.setStatus("current")


class _RlNdInspectionPolicyValidateSrcMac_Type(RlIpv6FhsSettingStatusType):
    """Custom type rlNdInspectionPolicyValidateSrcMac based on RlIpv6FhsSettingStatusType"""


_RlNdInspectionPolicyValidateSrcMac_Object = MibTableColumn
rlNdInspectionPolicyValidateSrcMac = _RlNdInspectionPolicyValidateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 1, 1, 5),
    _RlNdInspectionPolicyValidateSrcMac_Type()
)
rlNdInspectionPolicyValidateSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyValidateSrcMac.setStatus("current")
_RlNdInspectionPolicyRowStatus_Type = RowStatus
_RlNdInspectionPolicyRowStatus_Object = MibTableColumn
rlNdInspectionPolicyRowStatus = _RlNdInspectionPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 1, 1, 6),
    _RlNdInspectionPolicyRowStatus_Type()
)
rlNdInspectionPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyRowStatus.setStatus("current")
_RlNdInspectionPortPolicyTable_Object = MibTable
rlNdInspectionPortPolicyTable = _RlNdInspectionPortPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 2)
)
if mibBuilder.loadTexts:
    rlNdInspectionPortPolicyTable.setStatus("current")
_RlNdInspectionPortPolicyEntry_Object = MibTableRow
rlNdInspectionPortPolicyEntry = _RlNdInspectionPortPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 2, 1)
)
rlNdInspectionPortPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionPortPolicyIfIndex"),
    (1, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionPortPolicyName"),
)
if mibBuilder.loadTexts:
    rlNdInspectionPortPolicyEntry.setStatus("current")
_RlNdInspectionPortPolicyIfIndex_Type = InterfaceIndex
_RlNdInspectionPortPolicyIfIndex_Object = MibTableColumn
rlNdInspectionPortPolicyIfIndex = _RlNdInspectionPortPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 2, 1, 1),
    _RlNdInspectionPortPolicyIfIndex_Type()
)
rlNdInspectionPortPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionPortPolicyIfIndex.setStatus("current")


class _RlNdInspectionPortPolicyName_Type(DisplayString):
    """Custom type rlNdInspectionPortPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNdInspectionPortPolicyName_Type.__name__ = "DisplayString"
_RlNdInspectionPortPolicyName_Object = MibTableColumn
rlNdInspectionPortPolicyName = _RlNdInspectionPortPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 2, 1, 2),
    _RlNdInspectionPortPolicyName_Type()
)
rlNdInspectionPortPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionPortPolicyName.setStatus("current")


class _RlNdInspectionPortPolicyVlan1to1024_Type(OctetString):
    """Custom type rlNdInspectionPortPolicyVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPortPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlNdInspectionPortPolicyVlan1to1024_Object = MibTableColumn
rlNdInspectionPortPolicyVlan1to1024 = _RlNdInspectionPortPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 2, 1, 3),
    _RlNdInspectionPortPolicyVlan1to1024_Type()
)
rlNdInspectionPortPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPortPolicyVlan1to1024.setStatus("current")


class _RlNdInspectionPortPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlNdInspectionPortPolicyVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPortPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlNdInspectionPortPolicyVlan1025to2048_Object = MibTableColumn
rlNdInspectionPortPolicyVlan1025to2048 = _RlNdInspectionPortPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 2, 1, 4),
    _RlNdInspectionPortPolicyVlan1025to2048_Type()
)
rlNdInspectionPortPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPortPolicyVlan1025to2048.setStatus("current")


class _RlNdInspectionPortPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlNdInspectionPortPolicyVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPortPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlNdInspectionPortPolicyVlan2049to3072_Object = MibTableColumn
rlNdInspectionPortPolicyVlan2049to3072 = _RlNdInspectionPortPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 2, 1, 5),
    _RlNdInspectionPortPolicyVlan2049to3072_Type()
)
rlNdInspectionPortPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPortPolicyVlan2049to3072.setStatus("current")


class _RlNdInspectionPortPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlNdInspectionPortPolicyVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPortPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlNdInspectionPortPolicyVlan3073to4094_Object = MibTableColumn
rlNdInspectionPortPolicyVlan3073to4094 = _RlNdInspectionPortPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 2, 1, 6),
    _RlNdInspectionPortPolicyVlan3073to4094_Type()
)
rlNdInspectionPortPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPortPolicyVlan3073to4094.setStatus("current")
_RlNdInspectionPortPolicyRowStatus_Type = RowStatus
_RlNdInspectionPortPolicyRowStatus_Object = MibTableColumn
rlNdInspectionPortPolicyRowStatus = _RlNdInspectionPortPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 2, 1, 7),
    _RlNdInspectionPortPolicyRowStatus_Type()
)
rlNdInspectionPortPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlNdInspectionPortPolicyRowStatus.setStatus("current")
_RlNdInspectionPolicyPortTable_Object = MibTable
rlNdInspectionPolicyPortTable = _RlNdInspectionPolicyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 3)
)
if mibBuilder.loadTexts:
    rlNdInspectionPolicyPortTable.setStatus("current")
_RlNdInspectionPolicyPortEntry_Object = MibTableRow
rlNdInspectionPolicyPortEntry = _RlNdInspectionPolicyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 3, 1)
)
rlNdInspectionPolicyPortEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionPolicyPortName"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionPolicyPortIfIndex"),
)
if mibBuilder.loadTexts:
    rlNdInspectionPolicyPortEntry.setStatus("current")


class _RlNdInspectionPolicyPortName_Type(DisplayString):
    """Custom type rlNdInspectionPolicyPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNdInspectionPolicyPortName_Type.__name__ = "DisplayString"
_RlNdInspectionPolicyPortName_Object = MibTableColumn
rlNdInspectionPolicyPortName = _RlNdInspectionPolicyPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 3, 1, 1),
    _RlNdInspectionPolicyPortName_Type()
)
rlNdInspectionPolicyPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyPortName.setStatus("current")
_RlNdInspectionPolicyPortIfIndex_Type = InterfaceIndex
_RlNdInspectionPolicyPortIfIndex_Object = MibTableColumn
rlNdInspectionPolicyPortIfIndex = _RlNdInspectionPolicyPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 3, 1, 2),
    _RlNdInspectionPolicyPortIfIndex_Type()
)
rlNdInspectionPolicyPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyPortIfIndex.setStatus("current")


class _RlNdInspectionPolicyPortVlan1to1024_Type(OctetString):
    """Custom type rlNdInspectionPolicyPortVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPolicyPortVlan1to1024_Type.__name__ = "OctetString"
_RlNdInspectionPolicyPortVlan1to1024_Object = MibTableColumn
rlNdInspectionPolicyPortVlan1to1024 = _RlNdInspectionPolicyPortVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 3, 1, 3),
    _RlNdInspectionPolicyPortVlan1to1024_Type()
)
rlNdInspectionPolicyPortVlan1to1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyPortVlan1to1024.setStatus("current")


class _RlNdInspectionPolicyPortVlan1025to2048_Type(OctetString):
    """Custom type rlNdInspectionPolicyPortVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPolicyPortVlan1025to2048_Type.__name__ = "OctetString"
_RlNdInspectionPolicyPortVlan1025to2048_Object = MibTableColumn
rlNdInspectionPolicyPortVlan1025to2048 = _RlNdInspectionPolicyPortVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 3, 1, 4),
    _RlNdInspectionPolicyPortVlan1025to2048_Type()
)
rlNdInspectionPolicyPortVlan1025to2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyPortVlan1025to2048.setStatus("current")


class _RlNdInspectionPolicyPortVlan2049to3072_Type(OctetString):
    """Custom type rlNdInspectionPolicyPortVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPolicyPortVlan2049to3072_Type.__name__ = "OctetString"
_RlNdInspectionPolicyPortVlan2049to3072_Object = MibTableColumn
rlNdInspectionPolicyPortVlan2049to3072 = _RlNdInspectionPolicyPortVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 3, 1, 5),
    _RlNdInspectionPolicyPortVlan2049to3072_Type()
)
rlNdInspectionPolicyPortVlan2049to3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyPortVlan2049to3072.setStatus("current")


class _RlNdInspectionPolicyPortVlan3073to4094_Type(OctetString):
    """Custom type rlNdInspectionPolicyPortVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPolicyPortVlan3073to4094_Type.__name__ = "OctetString"
_RlNdInspectionPolicyPortVlan3073to4094_Object = MibTableColumn
rlNdInspectionPolicyPortVlan3073to4094 = _RlNdInspectionPolicyPortVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 3, 1, 6),
    _RlNdInspectionPolicyPortVlan3073to4094_Type()
)
rlNdInspectionPolicyPortVlan3073to4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyPortVlan3073to4094.setStatus("current")
_RlNdInspectionVlanPolicyTable_Object = MibTable
rlNdInspectionVlanPolicyTable = _RlNdInspectionVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 4)
)
if mibBuilder.loadTexts:
    rlNdInspectionVlanPolicyTable.setStatus("current")
_RlNdInspectionVlanPolicyEntry_Object = MibTableRow
rlNdInspectionVlanPolicyEntry = _RlNdInspectionVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 4, 1)
)
rlNdInspectionVlanPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionVlanPolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlNdInspectionVlanPolicyEntry.setStatus("current")
_RlNdInspectionVlanPolicyVlanTag_Type = VlanId
_RlNdInspectionVlanPolicyVlanTag_Object = MibTableColumn
rlNdInspectionVlanPolicyVlanTag = _RlNdInspectionVlanPolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 4, 1, 1),
    _RlNdInspectionVlanPolicyVlanTag_Type()
)
rlNdInspectionVlanPolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionVlanPolicyVlanTag.setStatus("current")


class _RlNdInspectionVlanPolicyName_Type(DisplayString):
    """Custom type rlNdInspectionVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNdInspectionVlanPolicyName_Type.__name__ = "DisplayString"
_RlNdInspectionVlanPolicyName_Object = MibTableColumn
rlNdInspectionVlanPolicyName = _RlNdInspectionVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 4, 1, 2),
    _RlNdInspectionVlanPolicyName_Type()
)
rlNdInspectionVlanPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionVlanPolicyName.setStatus("current")
_RlNdInspectionVlanPolicyRowStatus_Type = RowStatus
_RlNdInspectionVlanPolicyRowStatus_Object = MibTableColumn
rlNdInspectionVlanPolicyRowStatus = _RlNdInspectionVlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 4, 1, 3),
    _RlNdInspectionVlanPolicyRowStatus_Type()
)
rlNdInspectionVlanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlNdInspectionVlanPolicyRowStatus.setStatus("current")
_RlNdInspectionPolicyVlanTable_Object = MibTable
rlNdInspectionPolicyVlanTable = _RlNdInspectionPolicyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 5)
)
if mibBuilder.loadTexts:
    rlNdInspectionPolicyVlanTable.setStatus("current")
_RlNdInspectionPolicyVlanEntry_Object = MibTableRow
rlNdInspectionPolicyVlanEntry = _RlNdInspectionPolicyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 5, 1)
)
rlNdInspectionPolicyVlanEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionPolicyVlanPolicyName"),
)
if mibBuilder.loadTexts:
    rlNdInspectionPolicyVlanEntry.setStatus("current")


class _RlNdInspectionPolicyVlanPolicyName_Type(DisplayString):
    """Custom type rlNdInspectionPolicyVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNdInspectionPolicyVlanPolicyName_Type.__name__ = "DisplayString"
_RlNdInspectionPolicyVlanPolicyName_Object = MibTableColumn
rlNdInspectionPolicyVlanPolicyName = _RlNdInspectionPolicyVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 5, 1, 1),
    _RlNdInspectionPolicyVlanPolicyName_Type()
)
rlNdInspectionPolicyVlanPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyVlanPolicyName.setStatus("current")


class _RlNdInspectionPolicyVlan1to1024_Type(OctetString):
    """Custom type rlNdInspectionPolicyVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlNdInspectionPolicyVlan1to1024_Object = MibTableColumn
rlNdInspectionPolicyVlan1to1024 = _RlNdInspectionPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 5, 1, 2),
    _RlNdInspectionPolicyVlan1to1024_Type()
)
rlNdInspectionPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyVlan1to1024.setStatus("current")


class _RlNdInspectionPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlNdInspectionPolicyVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlNdInspectionPolicyVlan1025to2048_Object = MibTableColumn
rlNdInspectionPolicyVlan1025to2048 = _RlNdInspectionPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 5, 1, 3),
    _RlNdInspectionPolicyVlan1025to2048_Type()
)
rlNdInspectionPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyVlan1025to2048.setStatus("current")


class _RlNdInspectionPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlNdInspectionPolicyVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlNdInspectionPolicyVlan2049to3072_Object = MibTableColumn
rlNdInspectionPolicyVlan2049to3072 = _RlNdInspectionPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 5, 1, 4),
    _RlNdInspectionPolicyVlan2049to3072_Type()
)
rlNdInspectionPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyVlan2049to3072.setStatus("current")


class _RlNdInspectionPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlNdInspectionPolicyVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlNdInspectionPolicyVlan3073to4094_Object = MibTableColumn
rlNdInspectionPolicyVlan3073to4094 = _RlNdInspectionPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 5, 1, 5),
    _RlNdInspectionPolicyVlan3073to4094_Type()
)
rlNdInspectionPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionPolicyVlan3073to4094.setStatus("current")
_RlNdInspectionEnableVlanTable_Object = MibTable
rlNdInspectionEnableVlanTable = _RlNdInspectionEnableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 6)
)
if mibBuilder.loadTexts:
    rlNdInspectionEnableVlanTable.setStatus("current")
_RlNdInspectionEnableVlanEntry_Object = MibTableRow
rlNdInspectionEnableVlanEntry = _RlNdInspectionEnableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 6, 1)
)
rlNdInspectionEnableVlanEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionEnableVlanIndex"),
)
if mibBuilder.loadTexts:
    rlNdInspectionEnableVlanEntry.setStatus("current")


class _RlNdInspectionEnableVlanIndex_Type(Integer32):
    """Custom type rlNdInspectionEnableVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )


_RlNdInspectionEnableVlanIndex_Type.__name__ = "Integer32"
_RlNdInspectionEnableVlanIndex_Object = MibTableColumn
rlNdInspectionEnableVlanIndex = _RlNdInspectionEnableVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 6, 1, 1),
    _RlNdInspectionEnableVlanIndex_Type()
)
rlNdInspectionEnableVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionEnableVlanIndex.setStatus("current")


class _RlNdInspectionEnableVlan1to1024_Type(OctetString):
    """Custom type rlNdInspectionEnableVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionEnableVlan1to1024_Type.__name__ = "OctetString"
_RlNdInspectionEnableVlan1to1024_Object = MibTableColumn
rlNdInspectionEnableVlan1to1024 = _RlNdInspectionEnableVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 6, 1, 2),
    _RlNdInspectionEnableVlan1to1024_Type()
)
rlNdInspectionEnableVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionEnableVlan1to1024.setStatus("current")


class _RlNdInspectionEnableVlan1025to2048_Type(OctetString):
    """Custom type rlNdInspectionEnableVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionEnableVlan1025to2048_Type.__name__ = "OctetString"
_RlNdInspectionEnableVlan1025to2048_Object = MibTableColumn
rlNdInspectionEnableVlan1025to2048 = _RlNdInspectionEnableVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 6, 1, 3),
    _RlNdInspectionEnableVlan1025to2048_Type()
)
rlNdInspectionEnableVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionEnableVlan1025to2048.setStatus("current")


class _RlNdInspectionEnableVlan2049to3072_Type(OctetString):
    """Custom type rlNdInspectionEnableVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionEnableVlan2049to3072_Type.__name__ = "OctetString"
_RlNdInspectionEnableVlan2049to3072_Object = MibTableColumn
rlNdInspectionEnableVlan2049to3072 = _RlNdInspectionEnableVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 6, 1, 4),
    _RlNdInspectionEnableVlan2049to3072_Type()
)
rlNdInspectionEnableVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionEnableVlan2049to3072.setStatus("current")


class _RlNdInspectionEnableVlan3073to4094_Type(OctetString):
    """Custom type rlNdInspectionEnableVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNdInspectionEnableVlan3073to4094_Type.__name__ = "OctetString"
_RlNdInspectionEnableVlan3073to4094_Object = MibTableColumn
rlNdInspectionEnableVlan3073to4094 = _RlNdInspectionEnableVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 6, 1, 5),
    _RlNdInspectionEnableVlan3073to4094_Type()
)
rlNdInspectionEnableVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionEnableVlan3073to4094.setStatus("current")
_RlNdInspectionActivePolicyTable_Object = MibTable
rlNdInspectionActivePolicyTable = _RlNdInspectionActivePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7)
)
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyTable.setStatus("current")
_RlNdInspectionActivePolicyEntry_Object = MibTableRow
rlNdInspectionActivePolicyEntry = _RlNdInspectionActivePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1)
)
rlNdInspectionActivePolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionActivePolicyIfIndex"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlNdInspectionActivePolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyEntry.setStatus("current")
_RlNdInspectionActivePolicyIfIndex_Type = InterfaceIndex
_RlNdInspectionActivePolicyIfIndex_Object = MibTableColumn
rlNdInspectionActivePolicyIfIndex = _RlNdInspectionActivePolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 1),
    _RlNdInspectionActivePolicyIfIndex_Type()
)
rlNdInspectionActivePolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyIfIndex.setStatus("current")
_RlNdInspectionActivePolicyVlanTag_Type = VlanId
_RlNdInspectionActivePolicyVlanTag_Object = MibTableColumn
rlNdInspectionActivePolicyVlanTag = _RlNdInspectionActivePolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 2),
    _RlNdInspectionActivePolicyVlanTag_Type()
)
rlNdInspectionActivePolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyVlanTag.setStatus("current")


class _RlNdInspectionActivePolicyNamePort_Type(DisplayString):
    """Custom type rlNdInspectionActivePolicyNamePort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNdInspectionActivePolicyNamePort_Type.__name__ = "DisplayString"
_RlNdInspectionActivePolicyNamePort_Object = MibTableColumn
rlNdInspectionActivePolicyNamePort = _RlNdInspectionActivePolicyNamePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 3),
    _RlNdInspectionActivePolicyNamePort_Type()
)
rlNdInspectionActivePolicyNamePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyNamePort.setStatus("current")


class _RlNdInspectionActivePolicyNameVlan_Type(DisplayString):
    """Custom type rlNdInspectionActivePolicyNameVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNdInspectionActivePolicyNameVlan_Type.__name__ = "DisplayString"
_RlNdInspectionActivePolicyNameVlan_Object = MibTableColumn
rlNdInspectionActivePolicyNameVlan = _RlNdInspectionActivePolicyNameVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 4),
    _RlNdInspectionActivePolicyNameVlan_Type()
)
rlNdInspectionActivePolicyNameVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyNameVlan.setStatus("current")


class _RlNdInspectionActivePolicyDeviceRole_Type(Integer32):
    """Custom type rlNdInspectionActivePolicyDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2))
    )


_RlNdInspectionActivePolicyDeviceRole_Type.__name__ = "Integer32"
_RlNdInspectionActivePolicyDeviceRole_Object = MibTableColumn
rlNdInspectionActivePolicyDeviceRole = _RlNdInspectionActivePolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 5),
    _RlNdInspectionActivePolicyDeviceRole_Type()
)
rlNdInspectionActivePolicyDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyDeviceRole.setStatus("current")
_RlNdInspectionActivePolicyDeviceRoleType_Type = RlIpv6FhsSettingType
_RlNdInspectionActivePolicyDeviceRoleType_Object = MibTableColumn
rlNdInspectionActivePolicyDeviceRoleType = _RlNdInspectionActivePolicyDeviceRoleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 6),
    _RlNdInspectionActivePolicyDeviceRoleType_Type()
)
rlNdInspectionActivePolicyDeviceRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyDeviceRoleType.setStatus("current")
_RlNdInspectionActivePolicyDropUnsecured_Type = RlIpv6FhsSettingStatusType
_RlNdInspectionActivePolicyDropUnsecured_Object = MibTableColumn
rlNdInspectionActivePolicyDropUnsecured = _RlNdInspectionActivePolicyDropUnsecured_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 7),
    _RlNdInspectionActivePolicyDropUnsecured_Type()
)
rlNdInspectionActivePolicyDropUnsecured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyDropUnsecured.setStatus("current")
_RlNdInspectionActivePolicyDropUnsecuredType_Type = RlIpv6FhsSettingType
_RlNdInspectionActivePolicyDropUnsecuredType_Object = MibTableColumn
rlNdInspectionActivePolicyDropUnsecuredType = _RlNdInspectionActivePolicyDropUnsecuredType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 8),
    _RlNdInspectionActivePolicyDropUnsecuredType_Type()
)
rlNdInspectionActivePolicyDropUnsecuredType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyDropUnsecuredType.setStatus("current")


class _RlNdInspectionActivePolicySecLevelMin_Type(Integer32):
    """Custom type rlNdInspectionActivePolicySecLevelMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 7),
    )


_RlNdInspectionActivePolicySecLevelMin_Type.__name__ = "Integer32"
_RlNdInspectionActivePolicySecLevelMin_Object = MibTableColumn
rlNdInspectionActivePolicySecLevelMin = _RlNdInspectionActivePolicySecLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 9),
    _RlNdInspectionActivePolicySecLevelMin_Type()
)
rlNdInspectionActivePolicySecLevelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicySecLevelMin.setStatus("current")
_RlNdInspectionActivePolicySecLevelMinType_Type = RlIpv6FhsSettingType
_RlNdInspectionActivePolicySecLevelMinType_Object = MibTableColumn
rlNdInspectionActivePolicySecLevelMinType = _RlNdInspectionActivePolicySecLevelMinType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 10),
    _RlNdInspectionActivePolicySecLevelMinType_Type()
)
rlNdInspectionActivePolicySecLevelMinType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicySecLevelMinType.setStatus("current")
_RlNdInspectionActivePolicyValidateSrcMac_Type = RlIpv6FhsSettingStatusType
_RlNdInspectionActivePolicyValidateSrcMac_Object = MibTableColumn
rlNdInspectionActivePolicyValidateSrcMac = _RlNdInspectionActivePolicyValidateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 11),
    _RlNdInspectionActivePolicyValidateSrcMac_Type()
)
rlNdInspectionActivePolicyValidateSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyValidateSrcMac.setStatus("current")
_RlNdInspectionActivePolicyValidateSrcMacType_Type = RlIpv6FhsSettingType
_RlNdInspectionActivePolicyValidateSrcMacType_Object = MibTableColumn
rlNdInspectionActivePolicyValidateSrcMacType = _RlNdInspectionActivePolicyValidateSrcMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 7, 1, 12),
    _RlNdInspectionActivePolicyValidateSrcMacType_Type()
)
rlNdInspectionActivePolicyValidateSrcMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNdInspectionActivePolicyValidateSrcMacType.setStatus("current")


class _RlNdInspectionValidateSrcMac_Type(Integer32):
    """Custom type rlNdInspectionValidateSrcMac based on Integer32"""
    defaultValue = 2

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


_RlNdInspectionValidateSrcMac_Type.__name__ = "Integer32"
_RlNdInspectionValidateSrcMac_Object = MibScalar
rlNdInspectionValidateSrcMac = _RlNdInspectionValidateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 8),
    _RlNdInspectionValidateSrcMac_Type()
)
rlNdInspectionValidateSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionValidateSrcMac.setStatus("current")


class _RlNdInspectionDropUnsecured_Type(TruthValue):
    """Custom type rlNdInspectionDropUnsecured based on TruthValue"""


_RlNdInspectionDropUnsecured_Object = MibScalar
rlNdInspectionDropUnsecured = _RlNdInspectionDropUnsecured_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 9),
    _RlNdInspectionDropUnsecured_Type()
)
rlNdInspectionDropUnsecured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionDropUnsecured.setStatus("current")


class _RlNdInspectionSecLevelMin_Type(Integer32):
    """Custom type rlNdInspectionSecLevelMin based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 7),
    )


_RlNdInspectionSecLevelMin_Type.__name__ = "Integer32"
_RlNdInspectionSecLevelMin_Object = MibScalar
rlNdInspectionSecLevelMin = _RlNdInspectionSecLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 2, 10),
    _RlNdInspectionSecLevelMin_Type()
)
rlNdInspectionSecLevelMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNdInspectionSecLevelMin.setStatus("current")
_RlRaGuard_ObjectIdentity = ObjectIdentity
rlRaGuard = _RlRaGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3)
)
_RlRaGuardPolicyTable_Object = MibTable
rlRaGuardPolicyTable = _RlRaGuardPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1)
)
if mibBuilder.loadTexts:
    rlRaGuardPolicyTable.setStatus("current")
_RlRaGuardPolicyEntry_Object = MibTableRow
rlRaGuardPolicyEntry = _RlRaGuardPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1)
)
rlRaGuardPolicyEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlRaGuardPolicyName"),
)
if mibBuilder.loadTexts:
    rlRaGuardPolicyEntry.setStatus("current")


class _RlRaGuardPolicyName_Type(DisplayString):
    """Custom type rlRaGuardPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRaGuardPolicyName_Type.__name__ = "DisplayString"
_RlRaGuardPolicyName_Object = MibTableColumn
rlRaGuardPolicyName = _RlRaGuardPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 1),
    _RlRaGuardPolicyName_Type()
)
rlRaGuardPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardPolicyName.setStatus("current")


class _RlRaGuardPolicyDeviceRole_Type(Integer32):
    """Custom type rlRaGuardPolicyDeviceRole based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2),
          ("unspecified", -1))
    )


_RlRaGuardPolicyDeviceRole_Type.__name__ = "Integer32"
_RlRaGuardPolicyDeviceRole_Object = MibTableColumn
rlRaGuardPolicyDeviceRole = _RlRaGuardPolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 2),
    _RlRaGuardPolicyDeviceRole_Type()
)
rlRaGuardPolicyDeviceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyDeviceRole.setStatus("current")


class _RlRaGuardPolicyHopLimitMin_Type(Integer32):
    """Custom type rlRaGuardPolicyHopLimitMin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_RlRaGuardPolicyHopLimitMin_Type.__name__ = "Integer32"
_RlRaGuardPolicyHopLimitMin_Object = MibTableColumn
rlRaGuardPolicyHopLimitMin = _RlRaGuardPolicyHopLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 3),
    _RlRaGuardPolicyHopLimitMin_Type()
)
rlRaGuardPolicyHopLimitMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyHopLimitMin.setStatus("current")


class _RlRaGuardPolicyHopLimitMax_Type(Integer32):
    """Custom type rlRaGuardPolicyHopLimitMax based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_RlRaGuardPolicyHopLimitMax_Type.__name__ = "Integer32"
_RlRaGuardPolicyHopLimitMax_Object = MibTableColumn
rlRaGuardPolicyHopLimitMax = _RlRaGuardPolicyHopLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 4),
    _RlRaGuardPolicyHopLimitMax_Type()
)
rlRaGuardPolicyHopLimitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyHopLimitMax.setStatus("current")


class _RlRaGuardPolicyManagedConfigFlag_Type(Integer32):
    """Custom type rlRaGuardPolicyManagedConfigFlag based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled-off", 1),
          ("enabled-on", 2),
          ("unspecified", -1))
    )


_RlRaGuardPolicyManagedConfigFlag_Type.__name__ = "Integer32"
_RlRaGuardPolicyManagedConfigFlag_Object = MibTableColumn
rlRaGuardPolicyManagedConfigFlag = _RlRaGuardPolicyManagedConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 5),
    _RlRaGuardPolicyManagedConfigFlag_Type()
)
rlRaGuardPolicyManagedConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyManagedConfigFlag.setStatus("current")


class _RlRaGuardPolicyMatchRaAddrSpecified_Type(TruthValue):
    """Custom type rlRaGuardPolicyMatchRaAddrSpecified based on TruthValue"""


_RlRaGuardPolicyMatchRaAddrSpecified_Object = MibTableColumn
rlRaGuardPolicyMatchRaAddrSpecified = _RlRaGuardPolicyMatchRaAddrSpecified_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 6),
    _RlRaGuardPolicyMatchRaAddrSpecified_Type()
)
rlRaGuardPolicyMatchRaAddrSpecified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyMatchRaAddrSpecified.setStatus("current")


class _RlRaGuardPolicyMatchRaAddr_Type(DisplayString):
    """Custom type rlRaGuardPolicyMatchRaAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRaGuardPolicyMatchRaAddr_Type.__name__ = "DisplayString"
_RlRaGuardPolicyMatchRaAddr_Object = MibTableColumn
rlRaGuardPolicyMatchRaAddr = _RlRaGuardPolicyMatchRaAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 7),
    _RlRaGuardPolicyMatchRaAddr_Type()
)
rlRaGuardPolicyMatchRaAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyMatchRaAddr.setStatus("current")


class _RlRaGuardPolicyMatchRaPrefixesSpecified_Type(TruthValue):
    """Custom type rlRaGuardPolicyMatchRaPrefixesSpecified based on TruthValue"""


_RlRaGuardPolicyMatchRaPrefixesSpecified_Object = MibTableColumn
rlRaGuardPolicyMatchRaPrefixesSpecified = _RlRaGuardPolicyMatchRaPrefixesSpecified_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 8),
    _RlRaGuardPolicyMatchRaPrefixesSpecified_Type()
)
rlRaGuardPolicyMatchRaPrefixesSpecified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyMatchRaPrefixesSpecified.setStatus("current")


class _RlRaGuardPolicyMatchRaPrefixes_Type(DisplayString):
    """Custom type rlRaGuardPolicyMatchRaPrefixes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRaGuardPolicyMatchRaPrefixes_Type.__name__ = "DisplayString"
_RlRaGuardPolicyMatchRaPrefixes_Object = MibTableColumn
rlRaGuardPolicyMatchRaPrefixes = _RlRaGuardPolicyMatchRaPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 9),
    _RlRaGuardPolicyMatchRaPrefixes_Type()
)
rlRaGuardPolicyMatchRaPrefixes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyMatchRaPrefixes.setStatus("current")


class _RlRaGuardPolicyOtherConfigFlag_Type(Integer32):
    """Custom type rlRaGuardPolicyOtherConfigFlag based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled-off", 1),
          ("enabled-on", 2),
          ("unspecified", -1))
    )


_RlRaGuardPolicyOtherConfigFlag_Type.__name__ = "Integer32"
_RlRaGuardPolicyOtherConfigFlag_Object = MibTableColumn
rlRaGuardPolicyOtherConfigFlag = _RlRaGuardPolicyOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 10),
    _RlRaGuardPolicyOtherConfigFlag_Type()
)
rlRaGuardPolicyOtherConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyOtherConfigFlag.setStatus("current")


class _RlRaGuardPolicyRouterPrefMin_Type(Integer32):
    """Custom type rlRaGuardPolicyRouterPrefMin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2),
          ("unspecified", -1))
    )


_RlRaGuardPolicyRouterPrefMin_Type.__name__ = "Integer32"
_RlRaGuardPolicyRouterPrefMin_Object = MibTableColumn
rlRaGuardPolicyRouterPrefMin = _RlRaGuardPolicyRouterPrefMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 11),
    _RlRaGuardPolicyRouterPrefMin_Type()
)
rlRaGuardPolicyRouterPrefMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyRouterPrefMin.setStatus("current")


class _RlRaGuardPolicyRouterPrefMax_Type(Integer32):
    """Custom type rlRaGuardPolicyRouterPrefMax based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2),
          ("unspecified", -1))
    )


_RlRaGuardPolicyRouterPrefMax_Type.__name__ = "Integer32"
_RlRaGuardPolicyRouterPrefMax_Object = MibTableColumn
rlRaGuardPolicyRouterPrefMax = _RlRaGuardPolicyRouterPrefMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 12),
    _RlRaGuardPolicyRouterPrefMax_Type()
)
rlRaGuardPolicyRouterPrefMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyRouterPrefMax.setStatus("current")
_RlRaGuardPolicyRowStatus_Type = RowStatus
_RlRaGuardPolicyRowStatus_Object = MibTableColumn
rlRaGuardPolicyRowStatus = _RlRaGuardPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 1, 1, 13),
    _RlRaGuardPolicyRowStatus_Type()
)
rlRaGuardPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlRaGuardPolicyRowStatus.setStatus("current")
_RlRaGuardPortPolicyTable_Object = MibTable
rlRaGuardPortPolicyTable = _RlRaGuardPortPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 2)
)
if mibBuilder.loadTexts:
    rlRaGuardPortPolicyTable.setStatus("current")
_RlRaGuardPortPolicyEntry_Object = MibTableRow
rlRaGuardPortPolicyEntry = _RlRaGuardPortPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 2, 1)
)
rlRaGuardPortPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlRaGuardPortPolicyIfIndex"),
    (1, "CISCOSB-IPV6FHS-MIB", "rlRaGuardPortPolicyName"),
)
if mibBuilder.loadTexts:
    rlRaGuardPortPolicyEntry.setStatus("current")
_RlRaGuardPortPolicyIfIndex_Type = InterfaceIndex
_RlRaGuardPortPolicyIfIndex_Object = MibTableColumn
rlRaGuardPortPolicyIfIndex = _RlRaGuardPortPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 2, 1, 1),
    _RlRaGuardPortPolicyIfIndex_Type()
)
rlRaGuardPortPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardPortPolicyIfIndex.setStatus("current")


class _RlRaGuardPortPolicyName_Type(DisplayString):
    """Custom type rlRaGuardPortPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRaGuardPortPolicyName_Type.__name__ = "DisplayString"
_RlRaGuardPortPolicyName_Object = MibTableColumn
rlRaGuardPortPolicyName = _RlRaGuardPortPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 2, 1, 2),
    _RlRaGuardPortPolicyName_Type()
)
rlRaGuardPortPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardPortPolicyName.setStatus("current")


class _RlRaGuardPortPolicyVlan1to1024_Type(OctetString):
    """Custom type rlRaGuardPortPolicyVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPortPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlRaGuardPortPolicyVlan1to1024_Object = MibTableColumn
rlRaGuardPortPolicyVlan1to1024 = _RlRaGuardPortPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 2, 1, 3),
    _RlRaGuardPortPolicyVlan1to1024_Type()
)
rlRaGuardPortPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPortPolicyVlan1to1024.setStatus("current")


class _RlRaGuardPortPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlRaGuardPortPolicyVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPortPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlRaGuardPortPolicyVlan1025to2048_Object = MibTableColumn
rlRaGuardPortPolicyVlan1025to2048 = _RlRaGuardPortPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 2, 1, 4),
    _RlRaGuardPortPolicyVlan1025to2048_Type()
)
rlRaGuardPortPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPortPolicyVlan1025to2048.setStatus("current")


class _RlRaGuardPortPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlRaGuardPortPolicyVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPortPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlRaGuardPortPolicyVlan2049to3072_Object = MibTableColumn
rlRaGuardPortPolicyVlan2049to3072 = _RlRaGuardPortPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 2, 1, 5),
    _RlRaGuardPortPolicyVlan2049to3072_Type()
)
rlRaGuardPortPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPortPolicyVlan2049to3072.setStatus("current")


class _RlRaGuardPortPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlRaGuardPortPolicyVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPortPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlRaGuardPortPolicyVlan3073to4094_Object = MibTableColumn
rlRaGuardPortPolicyVlan3073to4094 = _RlRaGuardPortPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 2, 1, 6),
    _RlRaGuardPortPolicyVlan3073to4094_Type()
)
rlRaGuardPortPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPortPolicyVlan3073to4094.setStatus("current")
_RlRaGuardPortPolicyRowStatus_Type = RowStatus
_RlRaGuardPortPolicyRowStatus_Object = MibTableColumn
rlRaGuardPortPolicyRowStatus = _RlRaGuardPortPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 2, 1, 7),
    _RlRaGuardPortPolicyRowStatus_Type()
)
rlRaGuardPortPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlRaGuardPortPolicyRowStatus.setStatus("current")
_RlRaGuardPolicyPortTable_Object = MibTable
rlRaGuardPolicyPortTable = _RlRaGuardPolicyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 3)
)
if mibBuilder.loadTexts:
    rlRaGuardPolicyPortTable.setStatus("current")
_RlRaGuardPolicyPortEntry_Object = MibTableRow
rlRaGuardPolicyPortEntry = _RlRaGuardPolicyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 3, 1)
)
rlRaGuardPolicyPortEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlRaGuardPolicyPortName"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlRaGuardPolicyPortIfIndex"),
)
if mibBuilder.loadTexts:
    rlRaGuardPolicyPortEntry.setStatus("current")


class _RlRaGuardPolicyPortName_Type(DisplayString):
    """Custom type rlRaGuardPolicyPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRaGuardPolicyPortName_Type.__name__ = "DisplayString"
_RlRaGuardPolicyPortName_Object = MibTableColumn
rlRaGuardPolicyPortName = _RlRaGuardPolicyPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 3, 1, 1),
    _RlRaGuardPolicyPortName_Type()
)
rlRaGuardPolicyPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardPolicyPortName.setStatus("current")
_RlRaGuardPolicyPortIfIndex_Type = InterfaceIndex
_RlRaGuardPolicyPortIfIndex_Object = MibTableColumn
rlRaGuardPolicyPortIfIndex = _RlRaGuardPolicyPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 3, 1, 2),
    _RlRaGuardPolicyPortIfIndex_Type()
)
rlRaGuardPolicyPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardPolicyPortIfIndex.setStatus("current")


class _RlRaGuardPolicyPortVlan1to1024_Type(OctetString):
    """Custom type rlRaGuardPolicyPortVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPolicyPortVlan1to1024_Type.__name__ = "OctetString"
_RlRaGuardPolicyPortVlan1to1024_Object = MibTableColumn
rlRaGuardPolicyPortVlan1to1024 = _RlRaGuardPolicyPortVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 3, 1, 3),
    _RlRaGuardPolicyPortVlan1to1024_Type()
)
rlRaGuardPolicyPortVlan1to1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardPolicyPortVlan1to1024.setStatus("current")


class _RlRaGuardPolicyPortVlan1025to2048_Type(OctetString):
    """Custom type rlRaGuardPolicyPortVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPolicyPortVlan1025to2048_Type.__name__ = "OctetString"
_RlRaGuardPolicyPortVlan1025to2048_Object = MibTableColumn
rlRaGuardPolicyPortVlan1025to2048 = _RlRaGuardPolicyPortVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 3, 1, 4),
    _RlRaGuardPolicyPortVlan1025to2048_Type()
)
rlRaGuardPolicyPortVlan1025to2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardPolicyPortVlan1025to2048.setStatus("current")


class _RlRaGuardPolicyPortVlan2049to3072_Type(OctetString):
    """Custom type rlRaGuardPolicyPortVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPolicyPortVlan2049to3072_Type.__name__ = "OctetString"
_RlRaGuardPolicyPortVlan2049to3072_Object = MibTableColumn
rlRaGuardPolicyPortVlan2049to3072 = _RlRaGuardPolicyPortVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 3, 1, 5),
    _RlRaGuardPolicyPortVlan2049to3072_Type()
)
rlRaGuardPolicyPortVlan2049to3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardPolicyPortVlan2049to3072.setStatus("current")


class _RlRaGuardPolicyPortVlan3073to4094_Type(OctetString):
    """Custom type rlRaGuardPolicyPortVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPolicyPortVlan3073to4094_Type.__name__ = "OctetString"
_RlRaGuardPolicyPortVlan3073to4094_Object = MibTableColumn
rlRaGuardPolicyPortVlan3073to4094 = _RlRaGuardPolicyPortVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 3, 1, 6),
    _RlRaGuardPolicyPortVlan3073to4094_Type()
)
rlRaGuardPolicyPortVlan3073to4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardPolicyPortVlan3073to4094.setStatus("current")
_RlRaGuardVlanPolicyTable_Object = MibTable
rlRaGuardVlanPolicyTable = _RlRaGuardVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 4)
)
if mibBuilder.loadTexts:
    rlRaGuardVlanPolicyTable.setStatus("current")
_RlRaGuardVlanPolicyEntry_Object = MibTableRow
rlRaGuardVlanPolicyEntry = _RlRaGuardVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 4, 1)
)
rlRaGuardVlanPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlRaGuardVlanPolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlRaGuardVlanPolicyEntry.setStatus("current")
_RlRaGuardVlanPolicyVlanTag_Type = VlanId
_RlRaGuardVlanPolicyVlanTag_Object = MibTableColumn
rlRaGuardVlanPolicyVlanTag = _RlRaGuardVlanPolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 4, 1, 1),
    _RlRaGuardVlanPolicyVlanTag_Type()
)
rlRaGuardVlanPolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardVlanPolicyVlanTag.setStatus("current")


class _RlRaGuardVlanPolicyName_Type(DisplayString):
    """Custom type rlRaGuardVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRaGuardVlanPolicyName_Type.__name__ = "DisplayString"
_RlRaGuardVlanPolicyName_Object = MibTableColumn
rlRaGuardVlanPolicyName = _RlRaGuardVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 4, 1, 2),
    _RlRaGuardVlanPolicyName_Type()
)
rlRaGuardVlanPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardVlanPolicyName.setStatus("current")
_RlRaGuardVlanPolicyRowStatus_Type = RowStatus
_RlRaGuardVlanPolicyRowStatus_Object = MibTableColumn
rlRaGuardVlanPolicyRowStatus = _RlRaGuardVlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 4, 1, 3),
    _RlRaGuardVlanPolicyRowStatus_Type()
)
rlRaGuardVlanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlRaGuardVlanPolicyRowStatus.setStatus("current")
_RlRaGuardPolicyVlanTable_Object = MibTable
rlRaGuardPolicyVlanTable = _RlRaGuardPolicyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 5)
)
if mibBuilder.loadTexts:
    rlRaGuardPolicyVlanTable.setStatus("current")
_RlRaGuardPolicyVlanEntry_Object = MibTableRow
rlRaGuardPolicyVlanEntry = _RlRaGuardPolicyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 5, 1)
)
rlRaGuardPolicyVlanEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlRaGuardPolicyVlanPolicyName"),
)
if mibBuilder.loadTexts:
    rlRaGuardPolicyVlanEntry.setStatus("current")


class _RlRaGuardPolicyVlanPolicyName_Type(DisplayString):
    """Custom type rlRaGuardPolicyVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRaGuardPolicyVlanPolicyName_Type.__name__ = "DisplayString"
_RlRaGuardPolicyVlanPolicyName_Object = MibTableColumn
rlRaGuardPolicyVlanPolicyName = _RlRaGuardPolicyVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 5, 1, 1),
    _RlRaGuardPolicyVlanPolicyName_Type()
)
rlRaGuardPolicyVlanPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardPolicyVlanPolicyName.setStatus("current")


class _RlRaGuardPolicyVlan1to1024_Type(OctetString):
    """Custom type rlRaGuardPolicyVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlRaGuardPolicyVlan1to1024_Object = MibTableColumn
rlRaGuardPolicyVlan1to1024 = _RlRaGuardPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 5, 1, 2),
    _RlRaGuardPolicyVlan1to1024_Type()
)
rlRaGuardPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyVlan1to1024.setStatus("current")


class _RlRaGuardPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlRaGuardPolicyVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlRaGuardPolicyVlan1025to2048_Object = MibTableColumn
rlRaGuardPolicyVlan1025to2048 = _RlRaGuardPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 5, 1, 3),
    _RlRaGuardPolicyVlan1025to2048_Type()
)
rlRaGuardPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyVlan1025to2048.setStatus("current")


class _RlRaGuardPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlRaGuardPolicyVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlRaGuardPolicyVlan2049to3072_Object = MibTableColumn
rlRaGuardPolicyVlan2049to3072 = _RlRaGuardPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 5, 1, 4),
    _RlRaGuardPolicyVlan2049to3072_Type()
)
rlRaGuardPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyVlan2049to3072.setStatus("current")


class _RlRaGuardPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlRaGuardPolicyVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlRaGuardPolicyVlan3073to4094_Object = MibTableColumn
rlRaGuardPolicyVlan3073to4094 = _RlRaGuardPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 5, 1, 5),
    _RlRaGuardPolicyVlan3073to4094_Type()
)
rlRaGuardPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardPolicyVlan3073to4094.setStatus("current")
_RlRaGuardEnableVlanTable_Object = MibTable
rlRaGuardEnableVlanTable = _RlRaGuardEnableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 6)
)
if mibBuilder.loadTexts:
    rlRaGuardEnableVlanTable.setStatus("current")
_RlRaGuardEnableVlanEntry_Object = MibTableRow
rlRaGuardEnableVlanEntry = _RlRaGuardEnableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 6, 1)
)
rlRaGuardEnableVlanEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlRaGuardEnableVlanIndex"),
)
if mibBuilder.loadTexts:
    rlRaGuardEnableVlanEntry.setStatus("current")


class _RlRaGuardEnableVlanIndex_Type(Integer32):
    """Custom type rlRaGuardEnableVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )


_RlRaGuardEnableVlanIndex_Type.__name__ = "Integer32"
_RlRaGuardEnableVlanIndex_Object = MibTableColumn
rlRaGuardEnableVlanIndex = _RlRaGuardEnableVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 6, 1, 1),
    _RlRaGuardEnableVlanIndex_Type()
)
rlRaGuardEnableVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardEnableVlanIndex.setStatus("current")


class _RlRaGuardEnableVlan1to1024_Type(OctetString):
    """Custom type rlRaGuardEnableVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardEnableVlan1to1024_Type.__name__ = "OctetString"
_RlRaGuardEnableVlan1to1024_Object = MibTableColumn
rlRaGuardEnableVlan1to1024 = _RlRaGuardEnableVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 6, 1, 2),
    _RlRaGuardEnableVlan1to1024_Type()
)
rlRaGuardEnableVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardEnableVlan1to1024.setStatus("current")


class _RlRaGuardEnableVlan1025to2048_Type(OctetString):
    """Custom type rlRaGuardEnableVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardEnableVlan1025to2048_Type.__name__ = "OctetString"
_RlRaGuardEnableVlan1025to2048_Object = MibTableColumn
rlRaGuardEnableVlan1025to2048 = _RlRaGuardEnableVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 6, 1, 3),
    _RlRaGuardEnableVlan1025to2048_Type()
)
rlRaGuardEnableVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardEnableVlan1025to2048.setStatus("current")


class _RlRaGuardEnableVlan2049to3072_Type(OctetString):
    """Custom type rlRaGuardEnableVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardEnableVlan2049to3072_Type.__name__ = "OctetString"
_RlRaGuardEnableVlan2049to3072_Object = MibTableColumn
rlRaGuardEnableVlan2049to3072 = _RlRaGuardEnableVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 6, 1, 4),
    _RlRaGuardEnableVlan2049to3072_Type()
)
rlRaGuardEnableVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardEnableVlan2049to3072.setStatus("current")


class _RlRaGuardEnableVlan3073to4094_Type(OctetString):
    """Custom type rlRaGuardEnableVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlRaGuardEnableVlan3073to4094_Type.__name__ = "OctetString"
_RlRaGuardEnableVlan3073to4094_Object = MibTableColumn
rlRaGuardEnableVlan3073to4094 = _RlRaGuardEnableVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 6, 1, 5),
    _RlRaGuardEnableVlan3073to4094_Type()
)
rlRaGuardEnableVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardEnableVlan3073to4094.setStatus("current")
_RlRaGuardActivePolicyTable_Object = MibTable
rlRaGuardActivePolicyTable = _RlRaGuardActivePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7)
)
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyTable.setStatus("current")
_RlRaGuardActivePolicyEntry_Object = MibTableRow
rlRaGuardActivePolicyEntry = _RlRaGuardActivePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1)
)
rlRaGuardActivePolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlRaGuardActivePolicyIfIndex"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlRaGuardActivePolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyEntry.setStatus("current")
_RlRaGuardActivePolicyIfIndex_Type = InterfaceIndex
_RlRaGuardActivePolicyIfIndex_Object = MibTableColumn
rlRaGuardActivePolicyIfIndex = _RlRaGuardActivePolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 1),
    _RlRaGuardActivePolicyIfIndex_Type()
)
rlRaGuardActivePolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyIfIndex.setStatus("current")
_RlRaGuardActivePolicyVlanTag_Type = VlanId
_RlRaGuardActivePolicyVlanTag_Object = MibTableColumn
rlRaGuardActivePolicyVlanTag = _RlRaGuardActivePolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 2),
    _RlRaGuardActivePolicyVlanTag_Type()
)
rlRaGuardActivePolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyVlanTag.setStatus("current")


class _RlRaGuardActivePolicyNamePort_Type(DisplayString):
    """Custom type rlRaGuardActivePolicyNamePort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRaGuardActivePolicyNamePort_Type.__name__ = "DisplayString"
_RlRaGuardActivePolicyNamePort_Object = MibTableColumn
rlRaGuardActivePolicyNamePort = _RlRaGuardActivePolicyNamePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 3),
    _RlRaGuardActivePolicyNamePort_Type()
)
rlRaGuardActivePolicyNamePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyNamePort.setStatus("current")


class _RlRaGuardActivePolicyNameVlan_Type(DisplayString):
    """Custom type rlRaGuardActivePolicyNameVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlRaGuardActivePolicyNameVlan_Type.__name__ = "DisplayString"
_RlRaGuardActivePolicyNameVlan_Object = MibTableColumn
rlRaGuardActivePolicyNameVlan = _RlRaGuardActivePolicyNameVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 4),
    _RlRaGuardActivePolicyNameVlan_Type()
)
rlRaGuardActivePolicyNameVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyNameVlan.setStatus("current")


class _RlRaGuardActivePolicyDeviceRole_Type(Integer32):
    """Custom type rlRaGuardActivePolicyDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2))
    )


_RlRaGuardActivePolicyDeviceRole_Type.__name__ = "Integer32"
_RlRaGuardActivePolicyDeviceRole_Object = MibTableColumn
rlRaGuardActivePolicyDeviceRole = _RlRaGuardActivePolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 5),
    _RlRaGuardActivePolicyDeviceRole_Type()
)
rlRaGuardActivePolicyDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyDeviceRole.setStatus("current")
_RlRaGuardActivePolicyDeviceRoleType_Type = RlIpv6FhsSettingType
_RlRaGuardActivePolicyDeviceRoleType_Object = MibTableColumn
rlRaGuardActivePolicyDeviceRoleType = _RlRaGuardActivePolicyDeviceRoleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 6),
    _RlRaGuardActivePolicyDeviceRoleType_Type()
)
rlRaGuardActivePolicyDeviceRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyDeviceRoleType.setStatus("current")


class _RlRaGuardActivePolicyHopLimitMin_Type(Integer32):
    """Custom type rlRaGuardActivePolicyHopLimitMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_RlRaGuardActivePolicyHopLimitMin_Type.__name__ = "Integer32"
_RlRaGuardActivePolicyHopLimitMin_Object = MibTableColumn
rlRaGuardActivePolicyHopLimitMin = _RlRaGuardActivePolicyHopLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 7),
    _RlRaGuardActivePolicyHopLimitMin_Type()
)
rlRaGuardActivePolicyHopLimitMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyHopLimitMin.setStatus("current")
_RlRaGuardActivePolicyHopLimitMinType_Type = RlIpv6FhsSettingType
_RlRaGuardActivePolicyHopLimitMinType_Object = MibTableColumn
rlRaGuardActivePolicyHopLimitMinType = _RlRaGuardActivePolicyHopLimitMinType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 8),
    _RlRaGuardActivePolicyHopLimitMinType_Type()
)
rlRaGuardActivePolicyHopLimitMinType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyHopLimitMinType.setStatus("current")


class _RlRaGuardActivePolicyHopLimitMax_Type(Integer32):
    """Custom type rlRaGuardActivePolicyHopLimitMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_RlRaGuardActivePolicyHopLimitMax_Type.__name__ = "Integer32"
_RlRaGuardActivePolicyHopLimitMax_Object = MibTableColumn
rlRaGuardActivePolicyHopLimitMax = _RlRaGuardActivePolicyHopLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 9),
    _RlRaGuardActivePolicyHopLimitMax_Type()
)
rlRaGuardActivePolicyHopLimitMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyHopLimitMax.setStatus("current")
_RlRaGuardActivePolicyHopLimitMaxType_Type = RlIpv6FhsSettingType
_RlRaGuardActivePolicyHopLimitMaxType_Object = MibTableColumn
rlRaGuardActivePolicyHopLimitMaxType = _RlRaGuardActivePolicyHopLimitMaxType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 10),
    _RlRaGuardActivePolicyHopLimitMaxType_Type()
)
rlRaGuardActivePolicyHopLimitMaxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyHopLimitMaxType.setStatus("current")


class _RlRaGuardActivePolicyManagedConfigFlag_Type(Integer32):
    """Custom type rlRaGuardActivePolicyManagedConfigFlag based on Integer32"""
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
          ("enabled-off", 1),
          ("enabled-on", 2))
    )


_RlRaGuardActivePolicyManagedConfigFlag_Type.__name__ = "Integer32"
_RlRaGuardActivePolicyManagedConfigFlag_Object = MibTableColumn
rlRaGuardActivePolicyManagedConfigFlag = _RlRaGuardActivePolicyManagedConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 11),
    _RlRaGuardActivePolicyManagedConfigFlag_Type()
)
rlRaGuardActivePolicyManagedConfigFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyManagedConfigFlag.setStatus("current")
_RlRaGuardActivePolicyManagedConfigFlagType_Type = RlIpv6FhsSettingType
_RlRaGuardActivePolicyManagedConfigFlagType_Object = MibTableColumn
rlRaGuardActivePolicyManagedConfigFlagType = _RlRaGuardActivePolicyManagedConfigFlagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 12),
    _RlRaGuardActivePolicyManagedConfigFlagType_Type()
)
rlRaGuardActivePolicyManagedConfigFlagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyManagedConfigFlagType.setStatus("current")


class _RlRaGuardActivePolicyMatchRaAddr_Type(DisplayString):
    """Custom type rlRaGuardActivePolicyMatchRaAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRaGuardActivePolicyMatchRaAddr_Type.__name__ = "DisplayString"
_RlRaGuardActivePolicyMatchRaAddr_Object = MibTableColumn
rlRaGuardActivePolicyMatchRaAddr = _RlRaGuardActivePolicyMatchRaAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 13),
    _RlRaGuardActivePolicyMatchRaAddr_Type()
)
rlRaGuardActivePolicyMatchRaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyMatchRaAddr.setStatus("current")
_RlRaGuardActivePolicyMatchRaAddrType_Type = RlIpv6FhsSettingType
_RlRaGuardActivePolicyMatchRaAddrType_Object = MibTableColumn
rlRaGuardActivePolicyMatchRaAddrType = _RlRaGuardActivePolicyMatchRaAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 14),
    _RlRaGuardActivePolicyMatchRaAddrType_Type()
)
rlRaGuardActivePolicyMatchRaAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyMatchRaAddrType.setStatus("current")


class _RlRaGuardActivePolicyMatchRaPrefixes_Type(DisplayString):
    """Custom type rlRaGuardActivePolicyMatchRaPrefixes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlRaGuardActivePolicyMatchRaPrefixes_Type.__name__ = "DisplayString"
_RlRaGuardActivePolicyMatchRaPrefixes_Object = MibTableColumn
rlRaGuardActivePolicyMatchRaPrefixes = _RlRaGuardActivePolicyMatchRaPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 15),
    _RlRaGuardActivePolicyMatchRaPrefixes_Type()
)
rlRaGuardActivePolicyMatchRaPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyMatchRaPrefixes.setStatus("current")
_RlRaGuardActivePolicyMatchRaPrefixesType_Type = RlIpv6FhsSettingType
_RlRaGuardActivePolicyMatchRaPrefixesType_Object = MibTableColumn
rlRaGuardActivePolicyMatchRaPrefixesType = _RlRaGuardActivePolicyMatchRaPrefixesType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 16),
    _RlRaGuardActivePolicyMatchRaPrefixesType_Type()
)
rlRaGuardActivePolicyMatchRaPrefixesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyMatchRaPrefixesType.setStatus("current")


class _RlRaGuardActivePolicyOtherConfigFlag_Type(Integer32):
    """Custom type rlRaGuardActivePolicyOtherConfigFlag based on Integer32"""
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
          ("enabled-off", 1),
          ("enabled-on", 2))
    )


_RlRaGuardActivePolicyOtherConfigFlag_Type.__name__ = "Integer32"
_RlRaGuardActivePolicyOtherConfigFlag_Object = MibTableColumn
rlRaGuardActivePolicyOtherConfigFlag = _RlRaGuardActivePolicyOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 17),
    _RlRaGuardActivePolicyOtherConfigFlag_Type()
)
rlRaGuardActivePolicyOtherConfigFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyOtherConfigFlag.setStatus("current")
_RlRaGuardActivePolicyOtherConfigFlagType_Type = RlIpv6FhsSettingType
_RlRaGuardActivePolicyOtherConfigFlagType_Object = MibTableColumn
rlRaGuardActivePolicyOtherConfigFlagType = _RlRaGuardActivePolicyOtherConfigFlagType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 18),
    _RlRaGuardActivePolicyOtherConfigFlagType_Type()
)
rlRaGuardActivePolicyOtherConfigFlagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyOtherConfigFlagType.setStatus("current")


class _RlRaGuardActivePolicyRouterPrefMin_Type(Integer32):
    """Custom type rlRaGuardActivePolicyRouterPrefMin based on Integer32"""
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
        *(("disabled", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_RlRaGuardActivePolicyRouterPrefMin_Type.__name__ = "Integer32"
_RlRaGuardActivePolicyRouterPrefMin_Object = MibTableColumn
rlRaGuardActivePolicyRouterPrefMin = _RlRaGuardActivePolicyRouterPrefMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 19),
    _RlRaGuardActivePolicyRouterPrefMin_Type()
)
rlRaGuardActivePolicyRouterPrefMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyRouterPrefMin.setStatus("current")
_RlRaGuardActivePolicyRouterPrefMinType_Type = RlIpv6FhsSettingType
_RlRaGuardActivePolicyRouterPrefMinType_Object = MibTableColumn
rlRaGuardActivePolicyRouterPrefMinType = _RlRaGuardActivePolicyRouterPrefMinType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 20),
    _RlRaGuardActivePolicyRouterPrefMinType_Type()
)
rlRaGuardActivePolicyRouterPrefMinType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyRouterPrefMinType.setStatus("current")


class _RlRaGuardActivePolicyRouterPrefMax_Type(Integer32):
    """Custom type rlRaGuardActivePolicyRouterPrefMax based on Integer32"""
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
        *(("disabled", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_RlRaGuardActivePolicyRouterPrefMax_Type.__name__ = "Integer32"
_RlRaGuardActivePolicyRouterPrefMax_Object = MibTableColumn
rlRaGuardActivePolicyRouterPrefMax = _RlRaGuardActivePolicyRouterPrefMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 21),
    _RlRaGuardActivePolicyRouterPrefMax_Type()
)
rlRaGuardActivePolicyRouterPrefMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyRouterPrefMax.setStatus("current")
_RlRaGuardActivePolicyRouterPrefMaxType_Type = RlIpv6FhsSettingType
_RlRaGuardActivePolicyRouterPrefMaxType_Object = MibTableColumn
rlRaGuardActivePolicyRouterPrefMaxType = _RlRaGuardActivePolicyRouterPrefMaxType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 7, 1, 22),
    _RlRaGuardActivePolicyRouterPrefMaxType_Type()
)
rlRaGuardActivePolicyRouterPrefMaxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlRaGuardActivePolicyRouterPrefMaxType.setStatus("current")


class _RlRaGuardHopLimitMin_Type(Integer32):
    """Custom type rlRaGuardHopLimitMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_RlRaGuardHopLimitMin_Type.__name__ = "Integer32"
_RlRaGuardHopLimitMin_Object = MibScalar
rlRaGuardHopLimitMin = _RlRaGuardHopLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 8),
    _RlRaGuardHopLimitMin_Type()
)
rlRaGuardHopLimitMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardHopLimitMin.setStatus("current")


class _RlRaGuardHopLimitMax_Type(Integer32):
    """Custom type rlRaGuardHopLimitMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_RlRaGuardHopLimitMax_Type.__name__ = "Integer32"
_RlRaGuardHopLimitMax_Object = MibScalar
rlRaGuardHopLimitMax = _RlRaGuardHopLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 9),
    _RlRaGuardHopLimitMax_Type()
)
rlRaGuardHopLimitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardHopLimitMax.setStatus("current")


class _RlRaGuardManagedConfigFlag_Type(Integer32):
    """Custom type rlRaGuardManagedConfigFlag based on Integer32"""
    defaultValue = 0

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
          ("enabled-off", 1),
          ("enabled-on", 2))
    )


_RlRaGuardManagedConfigFlag_Type.__name__ = "Integer32"
_RlRaGuardManagedConfigFlag_Object = MibScalar
rlRaGuardManagedConfigFlag = _RlRaGuardManagedConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 10),
    _RlRaGuardManagedConfigFlag_Type()
)
rlRaGuardManagedConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardManagedConfigFlag.setStatus("current")


class _RlRaGuardOtherConfigFlag_Type(Integer32):
    """Custom type rlRaGuardOtherConfigFlag based on Integer32"""
    defaultValue = 0

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
          ("enabled-off", 1),
          ("enabled-on", 2))
    )


_RlRaGuardOtherConfigFlag_Type.__name__ = "Integer32"
_RlRaGuardOtherConfigFlag_Object = MibScalar
rlRaGuardOtherConfigFlag = _RlRaGuardOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 11),
    _RlRaGuardOtherConfigFlag_Type()
)
rlRaGuardOtherConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardOtherConfigFlag.setStatus("current")


class _RlRaGuardRouterPrefMin_Type(Integer32):
    """Custom type rlRaGuardRouterPrefMin based on Integer32"""
    defaultValue = 0

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
        *(("disabled", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_RlRaGuardRouterPrefMin_Type.__name__ = "Integer32"
_RlRaGuardRouterPrefMin_Object = MibScalar
rlRaGuardRouterPrefMin = _RlRaGuardRouterPrefMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 12),
    _RlRaGuardRouterPrefMin_Type()
)
rlRaGuardRouterPrefMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardRouterPrefMin.setStatus("current")


class _RlRaGuardRouterPrefMax_Type(Integer32):
    """Custom type rlRaGuardRouterPrefMax based on Integer32"""
    defaultValue = 0

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
        *(("disabled", 0),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_RlRaGuardRouterPrefMax_Type.__name__ = "Integer32"
_RlRaGuardRouterPrefMax_Object = MibScalar
rlRaGuardRouterPrefMax = _RlRaGuardRouterPrefMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 3, 13),
    _RlRaGuardRouterPrefMax_Type()
)
rlRaGuardRouterPrefMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlRaGuardRouterPrefMax.setStatus("current")
_RlNbrBindingIntegrity_ObjectIdentity = ObjectIdentity
rlNbrBindingIntegrity = _RlNbrBindingIntegrity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4)
)
_RlNbrBindingIntegrityPolicyTable_Object = MibTable
rlNbrBindingIntegrityPolicyTable = _RlNbrBindingIntegrityPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 1)
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyTable.setStatus("current")
_RlNbrBindingIntegrityPolicyEntry_Object = MibTableRow
rlNbrBindingIntegrityPolicyEntry = _RlNbrBindingIntegrityPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 1, 1)
)
rlNbrBindingIntegrityPolicyEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityPolicyName"),
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyEntry.setStatus("current")


class _RlNbrBindingIntegrityPolicyName_Type(DisplayString):
    """Custom type rlNbrBindingIntegrityPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNbrBindingIntegrityPolicyName_Type.__name__ = "DisplayString"
_RlNbrBindingIntegrityPolicyName_Object = MibTableColumn
rlNbrBindingIntegrityPolicyName = _RlNbrBindingIntegrityPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 1, 1, 1),
    _RlNbrBindingIntegrityPolicyName_Type()
)
rlNbrBindingIntegrityPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyName.setStatus("current")


class _RlNbrBindingIntegrityPolicyDeviceRole_Type(Integer32):
    """Custom type rlNbrBindingIntegrityPolicyDeviceRole based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("perimeter", 1),
          ("unspecified", -1))
    )


_RlNbrBindingIntegrityPolicyDeviceRole_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityPolicyDeviceRole_Object = MibTableColumn
rlNbrBindingIntegrityPolicyDeviceRole = _RlNbrBindingIntegrityPolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 1, 1, 2),
    _RlNbrBindingIntegrityPolicyDeviceRole_Type()
)
rlNbrBindingIntegrityPolicyDeviceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyDeviceRole.setStatus("current")


class _RlNbrBindingIntegrityPolicyLogBinding_Type(RlIpv6FhsSettingStatusType):
    """Custom type rlNbrBindingIntegrityPolicyLogBinding based on RlIpv6FhsSettingStatusType"""


_RlNbrBindingIntegrityPolicyLogBinding_Object = MibTableColumn
rlNbrBindingIntegrityPolicyLogBinding = _RlNbrBindingIntegrityPolicyLogBinding_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 1, 1, 3),
    _RlNbrBindingIntegrityPolicyLogBinding_Type()
)
rlNbrBindingIntegrityPolicyLogBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyLogBinding.setStatus("current")


class _RlNbrBindingIntegrityPolicyMaxEntriesVlanLimit_Type(Integer32):
    """Custom type rlNbrBindingIntegrityPolicyMaxEntriesVlanLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RlNbrBindingIntegrityPolicyMaxEntriesVlanLimit_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityPolicyMaxEntriesVlanLimit_Object = MibTableColumn
rlNbrBindingIntegrityPolicyMaxEntriesVlanLimit = _RlNbrBindingIntegrityPolicyMaxEntriesVlanLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 1, 1, 4),
    _RlNbrBindingIntegrityPolicyMaxEntriesVlanLimit_Type()
)
rlNbrBindingIntegrityPolicyMaxEntriesVlanLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyMaxEntriesVlanLimit.setStatus("current")


class _RlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit_Type(Integer32):
    """Custom type rlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit_Object = MibTableColumn
rlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit = _RlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 1, 1, 5),
    _RlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit_Type()
)
rlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit.setStatus("current")


class _RlNbrBindingIntegrityPolicyMaxEntriesMacLimit_Type(Integer32):
    """Custom type rlNbrBindingIntegrityPolicyMaxEntriesMacLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_RlNbrBindingIntegrityPolicyMaxEntriesMacLimit_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityPolicyMaxEntriesMacLimit_Object = MibTableColumn
rlNbrBindingIntegrityPolicyMaxEntriesMacLimit = _RlNbrBindingIntegrityPolicyMaxEntriesMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 1, 1, 6),
    _RlNbrBindingIntegrityPolicyMaxEntriesMacLimit_Type()
)
rlNbrBindingIntegrityPolicyMaxEntriesMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyMaxEntriesMacLimit.setStatus("current")
_RlNbrBindingIntegrityPolicyRowStatus_Type = RowStatus
_RlNbrBindingIntegrityPolicyRowStatus_Object = MibTableColumn
rlNbrBindingIntegrityPolicyRowStatus = _RlNbrBindingIntegrityPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 1, 1, 7),
    _RlNbrBindingIntegrityPolicyRowStatus_Type()
)
rlNbrBindingIntegrityPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyRowStatus.setStatus("current")
_RlNbrBindingIntegrityPortPolicyTable_Object = MibTable
rlNbrBindingIntegrityPortPolicyTable = _RlNbrBindingIntegrityPortPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 2)
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPortPolicyTable.setStatus("current")
_RlNbrBindingIntegrityPortPolicyEntry_Object = MibTableRow
rlNbrBindingIntegrityPortPolicyEntry = _RlNbrBindingIntegrityPortPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 2, 1)
)
rlNbrBindingIntegrityPortPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityPortPolicyIfIndex"),
    (1, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityPortPolicyName"),
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPortPolicyEntry.setStatus("current")
_RlNbrBindingIntegrityPortPolicyIfIndex_Type = InterfaceIndex
_RlNbrBindingIntegrityPortPolicyIfIndex_Object = MibTableColumn
rlNbrBindingIntegrityPortPolicyIfIndex = _RlNbrBindingIntegrityPortPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 2, 1, 1),
    _RlNbrBindingIntegrityPortPolicyIfIndex_Type()
)
rlNbrBindingIntegrityPortPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPortPolicyIfIndex.setStatus("current")


class _RlNbrBindingIntegrityPortPolicyName_Type(DisplayString):
    """Custom type rlNbrBindingIntegrityPortPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNbrBindingIntegrityPortPolicyName_Type.__name__ = "DisplayString"
_RlNbrBindingIntegrityPortPolicyName_Object = MibTableColumn
rlNbrBindingIntegrityPortPolicyName = _RlNbrBindingIntegrityPortPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 2, 1, 2),
    _RlNbrBindingIntegrityPortPolicyName_Type()
)
rlNbrBindingIntegrityPortPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPortPolicyName.setStatus("current")


class _RlNbrBindingIntegrityPortPolicyVlan1to1024_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPortPolicyVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPortPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPortPolicyVlan1to1024_Object = MibTableColumn
rlNbrBindingIntegrityPortPolicyVlan1to1024 = _RlNbrBindingIntegrityPortPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 2, 1, 3),
    _RlNbrBindingIntegrityPortPolicyVlan1to1024_Type()
)
rlNbrBindingIntegrityPortPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPortPolicyVlan1to1024.setStatus("current")


class _RlNbrBindingIntegrityPortPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPortPolicyVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPortPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPortPolicyVlan1025to2048_Object = MibTableColumn
rlNbrBindingIntegrityPortPolicyVlan1025to2048 = _RlNbrBindingIntegrityPortPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 2, 1, 4),
    _RlNbrBindingIntegrityPortPolicyVlan1025to2048_Type()
)
rlNbrBindingIntegrityPortPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPortPolicyVlan1025to2048.setStatus("current")


class _RlNbrBindingIntegrityPortPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPortPolicyVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPortPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPortPolicyVlan2049to3072_Object = MibTableColumn
rlNbrBindingIntegrityPortPolicyVlan2049to3072 = _RlNbrBindingIntegrityPortPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 2, 1, 5),
    _RlNbrBindingIntegrityPortPolicyVlan2049to3072_Type()
)
rlNbrBindingIntegrityPortPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPortPolicyVlan2049to3072.setStatus("current")


class _RlNbrBindingIntegrityPortPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPortPolicyVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPortPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPortPolicyVlan3073to4094_Object = MibTableColumn
rlNbrBindingIntegrityPortPolicyVlan3073to4094 = _RlNbrBindingIntegrityPortPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 2, 1, 6),
    _RlNbrBindingIntegrityPortPolicyVlan3073to4094_Type()
)
rlNbrBindingIntegrityPortPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPortPolicyVlan3073to4094.setStatus("current")
_RlNbrBindingIntegrityPortPolicyRowStatus_Type = RowStatus
_RlNbrBindingIntegrityPortPolicyRowStatus_Object = MibTableColumn
rlNbrBindingIntegrityPortPolicyRowStatus = _RlNbrBindingIntegrityPortPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 2, 1, 7),
    _RlNbrBindingIntegrityPortPolicyRowStatus_Type()
)
rlNbrBindingIntegrityPortPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPortPolicyRowStatus.setStatus("current")
_RlNbrBindingIntegrityPolicyPortTable_Object = MibTable
rlNbrBindingIntegrityPolicyPortTable = _RlNbrBindingIntegrityPolicyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 3)
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyPortTable.setStatus("current")
_RlNbrBindingIntegrityPolicyPortEntry_Object = MibTableRow
rlNbrBindingIntegrityPolicyPortEntry = _RlNbrBindingIntegrityPolicyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 3, 1)
)
rlNbrBindingIntegrityPolicyPortEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityPolicyPortName"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityPolicyPortIfIndex"),
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyPortEntry.setStatus("current")


class _RlNbrBindingIntegrityPolicyPortName_Type(DisplayString):
    """Custom type rlNbrBindingIntegrityPolicyPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNbrBindingIntegrityPolicyPortName_Type.__name__ = "DisplayString"
_RlNbrBindingIntegrityPolicyPortName_Object = MibTableColumn
rlNbrBindingIntegrityPolicyPortName = _RlNbrBindingIntegrityPolicyPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 3, 1, 1),
    _RlNbrBindingIntegrityPolicyPortName_Type()
)
rlNbrBindingIntegrityPolicyPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyPortName.setStatus("current")
_RlNbrBindingIntegrityPolicyPortIfIndex_Type = InterfaceIndex
_RlNbrBindingIntegrityPolicyPortIfIndex_Object = MibTableColumn
rlNbrBindingIntegrityPolicyPortIfIndex = _RlNbrBindingIntegrityPolicyPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 3, 1, 2),
    _RlNbrBindingIntegrityPolicyPortIfIndex_Type()
)
rlNbrBindingIntegrityPolicyPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyPortIfIndex.setStatus("current")


class _RlNbrBindingIntegrityPolicyPortVlan1to1024_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPolicyPortVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPolicyPortVlan1to1024_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPolicyPortVlan1to1024_Object = MibTableColumn
rlNbrBindingIntegrityPolicyPortVlan1to1024 = _RlNbrBindingIntegrityPolicyPortVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 3, 1, 3),
    _RlNbrBindingIntegrityPolicyPortVlan1to1024_Type()
)
rlNbrBindingIntegrityPolicyPortVlan1to1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyPortVlan1to1024.setStatus("current")


class _RlNbrBindingIntegrityPolicyPortVlan1025to2048_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPolicyPortVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPolicyPortVlan1025to2048_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPolicyPortVlan1025to2048_Object = MibTableColumn
rlNbrBindingIntegrityPolicyPortVlan1025to2048 = _RlNbrBindingIntegrityPolicyPortVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 3, 1, 4),
    _RlNbrBindingIntegrityPolicyPortVlan1025to2048_Type()
)
rlNbrBindingIntegrityPolicyPortVlan1025to2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyPortVlan1025to2048.setStatus("current")


class _RlNbrBindingIntegrityPolicyPortVlan2049to3072_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPolicyPortVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPolicyPortVlan2049to3072_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPolicyPortVlan2049to3072_Object = MibTableColumn
rlNbrBindingIntegrityPolicyPortVlan2049to3072 = _RlNbrBindingIntegrityPolicyPortVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 3, 1, 5),
    _RlNbrBindingIntegrityPolicyPortVlan2049to3072_Type()
)
rlNbrBindingIntegrityPolicyPortVlan2049to3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyPortVlan2049to3072.setStatus("current")


class _RlNbrBindingIntegrityPolicyPortVlan3073to4094_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPolicyPortVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPolicyPortVlan3073to4094_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPolicyPortVlan3073to4094_Object = MibTableColumn
rlNbrBindingIntegrityPolicyPortVlan3073to4094 = _RlNbrBindingIntegrityPolicyPortVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 3, 1, 6),
    _RlNbrBindingIntegrityPolicyPortVlan3073to4094_Type()
)
rlNbrBindingIntegrityPolicyPortVlan3073to4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyPortVlan3073to4094.setStatus("current")
_RlNbrBindingIntegrityVlanPolicyTable_Object = MibTable
rlNbrBindingIntegrityVlanPolicyTable = _RlNbrBindingIntegrityVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 4)
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityVlanPolicyTable.setStatus("current")
_RlNbrBindingIntegrityVlanPolicyEntry_Object = MibTableRow
rlNbrBindingIntegrityVlanPolicyEntry = _RlNbrBindingIntegrityVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 4, 1)
)
rlNbrBindingIntegrityVlanPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityVlanPolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityVlanPolicyEntry.setStatus("current")
_RlNbrBindingIntegrityVlanPolicyVlanTag_Type = VlanId
_RlNbrBindingIntegrityVlanPolicyVlanTag_Object = MibTableColumn
rlNbrBindingIntegrityVlanPolicyVlanTag = _RlNbrBindingIntegrityVlanPolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 4, 1, 1),
    _RlNbrBindingIntegrityVlanPolicyVlanTag_Type()
)
rlNbrBindingIntegrityVlanPolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityVlanPolicyVlanTag.setStatus("current")


class _RlNbrBindingIntegrityVlanPolicyName_Type(DisplayString):
    """Custom type rlNbrBindingIntegrityVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNbrBindingIntegrityVlanPolicyName_Type.__name__ = "DisplayString"
_RlNbrBindingIntegrityVlanPolicyName_Object = MibTableColumn
rlNbrBindingIntegrityVlanPolicyName = _RlNbrBindingIntegrityVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 4, 1, 2),
    _RlNbrBindingIntegrityVlanPolicyName_Type()
)
rlNbrBindingIntegrityVlanPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityVlanPolicyName.setStatus("current")
_RlNbrBindingIntegrityVlanPolicyRowStatus_Type = RowStatus
_RlNbrBindingIntegrityVlanPolicyRowStatus_Object = MibTableColumn
rlNbrBindingIntegrityVlanPolicyRowStatus = _RlNbrBindingIntegrityVlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 4, 1, 3),
    _RlNbrBindingIntegrityVlanPolicyRowStatus_Type()
)
rlNbrBindingIntegrityVlanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityVlanPolicyRowStatus.setStatus("current")
_RlNbrBindingIntegrityPolicyVlanTable_Object = MibTable
rlNbrBindingIntegrityPolicyVlanTable = _RlNbrBindingIntegrityPolicyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 5)
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyVlanTable.setStatus("current")
_RlNbrBindingIntegrityPolicyVlanEntry_Object = MibTableRow
rlNbrBindingIntegrityPolicyVlanEntry = _RlNbrBindingIntegrityPolicyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 5, 1)
)
rlNbrBindingIntegrityPolicyVlanEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityPolicyVlanPolicyName"),
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyVlanEntry.setStatus("current")


class _RlNbrBindingIntegrityPolicyVlanPolicyName_Type(DisplayString):
    """Custom type rlNbrBindingIntegrityPolicyVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNbrBindingIntegrityPolicyVlanPolicyName_Type.__name__ = "DisplayString"
_RlNbrBindingIntegrityPolicyVlanPolicyName_Object = MibTableColumn
rlNbrBindingIntegrityPolicyVlanPolicyName = _RlNbrBindingIntegrityPolicyVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 5, 1, 1),
    _RlNbrBindingIntegrityPolicyVlanPolicyName_Type()
)
rlNbrBindingIntegrityPolicyVlanPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyVlanPolicyName.setStatus("current")


class _RlNbrBindingIntegrityPolicyVlan1to1024_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPolicyVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPolicyVlan1to1024_Object = MibTableColumn
rlNbrBindingIntegrityPolicyVlan1to1024 = _RlNbrBindingIntegrityPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 5, 1, 2),
    _RlNbrBindingIntegrityPolicyVlan1to1024_Type()
)
rlNbrBindingIntegrityPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyVlan1to1024.setStatus("current")


class _RlNbrBindingIntegrityPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPolicyVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPolicyVlan1025to2048_Object = MibTableColumn
rlNbrBindingIntegrityPolicyVlan1025to2048 = _RlNbrBindingIntegrityPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 5, 1, 3),
    _RlNbrBindingIntegrityPolicyVlan1025to2048_Type()
)
rlNbrBindingIntegrityPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyVlan1025to2048.setStatus("current")


class _RlNbrBindingIntegrityPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPolicyVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPolicyVlan2049to3072_Object = MibTableColumn
rlNbrBindingIntegrityPolicyVlan2049to3072 = _RlNbrBindingIntegrityPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 5, 1, 4),
    _RlNbrBindingIntegrityPolicyVlan2049to3072_Type()
)
rlNbrBindingIntegrityPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyVlan2049to3072.setStatus("current")


class _RlNbrBindingIntegrityPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlNbrBindingIntegrityPolicyVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityPolicyVlan3073to4094_Object = MibTableColumn
rlNbrBindingIntegrityPolicyVlan3073to4094 = _RlNbrBindingIntegrityPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 5, 1, 5),
    _RlNbrBindingIntegrityPolicyVlan3073to4094_Type()
)
rlNbrBindingIntegrityPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityPolicyVlan3073to4094.setStatus("current")
_RlNbrBindingIntegrityEnableVlanTable_Object = MibTable
rlNbrBindingIntegrityEnableVlanTable = _RlNbrBindingIntegrityEnableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 6)
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEnableVlanTable.setStatus("current")
_RlNbrBindingIntegrityEnableVlanEntry_Object = MibTableRow
rlNbrBindingIntegrityEnableVlanEntry = _RlNbrBindingIntegrityEnableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 6, 1)
)
rlNbrBindingIntegrityEnableVlanEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityEnableVlanIndex"),
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEnableVlanEntry.setStatus("current")


class _RlNbrBindingIntegrityEnableVlanIndex_Type(Integer32):
    """Custom type rlNbrBindingIntegrityEnableVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )


_RlNbrBindingIntegrityEnableVlanIndex_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityEnableVlanIndex_Object = MibTableColumn
rlNbrBindingIntegrityEnableVlanIndex = _RlNbrBindingIntegrityEnableVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 6, 1, 1),
    _RlNbrBindingIntegrityEnableVlanIndex_Type()
)
rlNbrBindingIntegrityEnableVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEnableVlanIndex.setStatus("current")


class _RlNbrBindingIntegrityEnableVlan1to1024_Type(OctetString):
    """Custom type rlNbrBindingIntegrityEnableVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityEnableVlan1to1024_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityEnableVlan1to1024_Object = MibTableColumn
rlNbrBindingIntegrityEnableVlan1to1024 = _RlNbrBindingIntegrityEnableVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 6, 1, 2),
    _RlNbrBindingIntegrityEnableVlan1to1024_Type()
)
rlNbrBindingIntegrityEnableVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEnableVlan1to1024.setStatus("current")


class _RlNbrBindingIntegrityEnableVlan1025to2048_Type(OctetString):
    """Custom type rlNbrBindingIntegrityEnableVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityEnableVlan1025to2048_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityEnableVlan1025to2048_Object = MibTableColumn
rlNbrBindingIntegrityEnableVlan1025to2048 = _RlNbrBindingIntegrityEnableVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 6, 1, 3),
    _RlNbrBindingIntegrityEnableVlan1025to2048_Type()
)
rlNbrBindingIntegrityEnableVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEnableVlan1025to2048.setStatus("current")


class _RlNbrBindingIntegrityEnableVlan2049to3072_Type(OctetString):
    """Custom type rlNbrBindingIntegrityEnableVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityEnableVlan2049to3072_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityEnableVlan2049to3072_Object = MibTableColumn
rlNbrBindingIntegrityEnableVlan2049to3072 = _RlNbrBindingIntegrityEnableVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 6, 1, 4),
    _RlNbrBindingIntegrityEnableVlan2049to3072_Type()
)
rlNbrBindingIntegrityEnableVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEnableVlan2049to3072.setStatus("current")


class _RlNbrBindingIntegrityEnableVlan3073to4094_Type(OctetString):
    """Custom type rlNbrBindingIntegrityEnableVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlNbrBindingIntegrityEnableVlan3073to4094_Type.__name__ = "OctetString"
_RlNbrBindingIntegrityEnableVlan3073to4094_Object = MibTableColumn
rlNbrBindingIntegrityEnableVlan3073to4094 = _RlNbrBindingIntegrityEnableVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 6, 1, 5),
    _RlNbrBindingIntegrityEnableVlan3073to4094_Type()
)
rlNbrBindingIntegrityEnableVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEnableVlan3073to4094.setStatus("current")
_RlNbrBindingIntegrityBindingTable_Object = MibTable
rlNbrBindingIntegrityBindingTable = _RlNbrBindingIntegrityBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7)
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingTable.setStatus("current")
_RlNbrBindingIntegrityBindingEntry_Object = MibTableRow
rlNbrBindingIntegrityBindingEntry = _RlNbrBindingIntegrityBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1)
)
rlNbrBindingIntegrityBindingEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityBindingVlanTag"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityBindingSourceAddressType"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityBindingSourceAddress"),
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingEntry.setStatus("current")
_RlNbrBindingIntegrityBindingVlanTag_Type = VlanId
_RlNbrBindingIntegrityBindingVlanTag_Object = MibTableColumn
rlNbrBindingIntegrityBindingVlanTag = _RlNbrBindingIntegrityBindingVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1, 1),
    _RlNbrBindingIntegrityBindingVlanTag_Type()
)
rlNbrBindingIntegrityBindingVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingVlanTag.setStatus("current")
_RlNbrBindingIntegrityBindingSourceAddressType_Type = InetAddressType
_RlNbrBindingIntegrityBindingSourceAddressType_Object = MibTableColumn
rlNbrBindingIntegrityBindingSourceAddressType = _RlNbrBindingIntegrityBindingSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1, 2),
    _RlNbrBindingIntegrityBindingSourceAddressType_Type()
)
rlNbrBindingIntegrityBindingSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingSourceAddressType.setStatus("current")
_RlNbrBindingIntegrityBindingSourceAddress_Type = InetAddress
_RlNbrBindingIntegrityBindingSourceAddress_Object = MibTableColumn
rlNbrBindingIntegrityBindingSourceAddress = _RlNbrBindingIntegrityBindingSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1, 3),
    _RlNbrBindingIntegrityBindingSourceAddress_Type()
)
rlNbrBindingIntegrityBindingSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingSourceAddress.setStatus("current")
_RlNbrBindingIntegrityBindingIfIndex_Type = InterfaceIndex
_RlNbrBindingIntegrityBindingIfIndex_Object = MibTableColumn
rlNbrBindingIntegrityBindingIfIndex = _RlNbrBindingIntegrityBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1, 4),
    _RlNbrBindingIntegrityBindingIfIndex_Type()
)
rlNbrBindingIntegrityBindingIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingIfIndex.setStatus("current")
_RlNbrBindingIntegrityBindingMacAddress_Type = MacAddress
_RlNbrBindingIntegrityBindingMacAddress_Object = MibTableColumn
rlNbrBindingIntegrityBindingMacAddress = _RlNbrBindingIntegrityBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1, 5),
    _RlNbrBindingIntegrityBindingMacAddress_Type()
)
rlNbrBindingIntegrityBindingMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingMacAddress.setStatus("current")


class _RlNbrBindingIntegrityBindingOrigin_Type(Integer32):
    """Custom type rlNbrBindingIntegrityBindingOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 3),
          ("ndp", 2),
          ("static", 1))
    )


_RlNbrBindingIntegrityBindingOrigin_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityBindingOrigin_Object = MibTableColumn
rlNbrBindingIntegrityBindingOrigin = _RlNbrBindingIntegrityBindingOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1, 6),
    _RlNbrBindingIntegrityBindingOrigin_Type()
)
rlNbrBindingIntegrityBindingOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingOrigin.setStatus("current")


class _RlNbrBindingIntegrityBindingState_Type(Integer32):
    """Custom type rlNbrBindingIntegrityBindingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tentative", 1),
          ("valid", 0))
    )


_RlNbrBindingIntegrityBindingState_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityBindingState_Object = MibTableColumn
rlNbrBindingIntegrityBindingState = _RlNbrBindingIntegrityBindingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1, 7),
    _RlNbrBindingIntegrityBindingState_Type()
)
rlNbrBindingIntegrityBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingState.setStatus("current")
_RlNbrBindingIntegrityBindingExpiryTime_Type = Integer32
_RlNbrBindingIntegrityBindingExpiryTime_Object = MibTableColumn
rlNbrBindingIntegrityBindingExpiryTime = _RlNbrBindingIntegrityBindingExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1, 8),
    _RlNbrBindingIntegrityBindingExpiryTime_Type()
)
rlNbrBindingIntegrityBindingExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingExpiryTime.setStatus("current")
_RlNbrBindingIntegrityBindingRowStatus_Type = RowStatus
_RlNbrBindingIntegrityBindingRowStatus_Object = MibTableColumn
rlNbrBindingIntegrityBindingRowStatus = _RlNbrBindingIntegrityBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 7, 1, 9),
    _RlNbrBindingIntegrityBindingRowStatus_Type()
)
rlNbrBindingIntegrityBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingRowStatus.setStatus("current")
_RlNbrBindingIntegrityClearTable_Object = MibTable
rlNbrBindingIntegrityClearTable = _RlNbrBindingIntegrityClearTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 8)
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityClearTable.setStatus("current")
_RlNbrBindingIntegrityClearEntry_Object = MibTableRow
rlNbrBindingIntegrityClearEntry = _RlNbrBindingIntegrityClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 8, 1)
)
rlNbrBindingIntegrityClearEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityClearIndex"),
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityClearEntry.setStatus("current")


class _RlNbrBindingIntegrityClearIndex_Type(Integer32):
    """Custom type rlNbrBindingIntegrityClearIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )


_RlNbrBindingIntegrityClearIndex_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityClearIndex_Object = MibTableColumn
rlNbrBindingIntegrityClearIndex = _RlNbrBindingIntegrityClearIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 8, 1, 1),
    _RlNbrBindingIntegrityClearIndex_Type()
)
rlNbrBindingIntegrityClearIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityClearIndex.setStatus("current")
_RlNbrBindingIntegrityClearVlanTag_Type = VlanId
_RlNbrBindingIntegrityClearVlanTag_Object = MibTableColumn
rlNbrBindingIntegrityClearVlanTag = _RlNbrBindingIntegrityClearVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 8, 1, 2),
    _RlNbrBindingIntegrityClearVlanTag_Type()
)
rlNbrBindingIntegrityClearVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityClearVlanTag.setStatus("current")
_RlNbrBindingIntegrityClearSourceAddressType_Type = InetAddressType
_RlNbrBindingIntegrityClearSourceAddressType_Object = MibTableColumn
rlNbrBindingIntegrityClearSourceAddressType = _RlNbrBindingIntegrityClearSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 8, 1, 3),
    _RlNbrBindingIntegrityClearSourceAddressType_Type()
)
rlNbrBindingIntegrityClearSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityClearSourceAddressType.setStatus("current")
_RlNbrBindingIntegrityClearSourceAddress_Type = InetAddress
_RlNbrBindingIntegrityClearSourceAddress_Object = MibTableColumn
rlNbrBindingIntegrityClearSourceAddress = _RlNbrBindingIntegrityClearSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 8, 1, 4),
    _RlNbrBindingIntegrityClearSourceAddress_Type()
)
rlNbrBindingIntegrityClearSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityClearSourceAddress.setStatus("current")
_RlNbrBindingIntegrityClearIfIndex_Type = InterfaceIndex
_RlNbrBindingIntegrityClearIfIndex_Object = MibTableColumn
rlNbrBindingIntegrityClearIfIndex = _RlNbrBindingIntegrityClearIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 8, 1, 5),
    _RlNbrBindingIntegrityClearIfIndex_Type()
)
rlNbrBindingIntegrityClearIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityClearIfIndex.setStatus("current")
_RlNbrBindingIntegrityClearMacAddress_Type = MacAddress
_RlNbrBindingIntegrityClearMacAddress_Object = MibTableColumn
rlNbrBindingIntegrityClearMacAddress = _RlNbrBindingIntegrityClearMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 8, 1, 6),
    _RlNbrBindingIntegrityClearMacAddress_Type()
)
rlNbrBindingIntegrityClearMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityClearMacAddress.setStatus("current")
_RlNbrBindingIntegrityClearRowStatus_Type = RowStatus
_RlNbrBindingIntegrityClearRowStatus_Object = MibTableColumn
rlNbrBindingIntegrityClearRowStatus = _RlNbrBindingIntegrityClearRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 8, 1, 7),
    _RlNbrBindingIntegrityClearRowStatus_Type()
)
rlNbrBindingIntegrityClearRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityClearRowStatus.setStatus("current")
_RlNbrBindingIntegrityActivePolicyTable_Object = MibTable
rlNbrBindingIntegrityActivePolicyTable = _RlNbrBindingIntegrityActivePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9)
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyTable.setStatus("current")
_RlNbrBindingIntegrityActivePolicyEntry_Object = MibTableRow
rlNbrBindingIntegrityActivePolicyEntry = _RlNbrBindingIntegrityActivePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1)
)
rlNbrBindingIntegrityActivePolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityActivePolicyIfIndex"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlNbrBindingIntegrityActivePolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyEntry.setStatus("current")
_RlNbrBindingIntegrityActivePolicyIfIndex_Type = InterfaceIndex
_RlNbrBindingIntegrityActivePolicyIfIndex_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyIfIndex = _RlNbrBindingIntegrityActivePolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 1),
    _RlNbrBindingIntegrityActivePolicyIfIndex_Type()
)
rlNbrBindingIntegrityActivePolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyIfIndex.setStatus("current")
_RlNbrBindingIntegrityActivePolicyVlanTag_Type = VlanId
_RlNbrBindingIntegrityActivePolicyVlanTag_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyVlanTag = _RlNbrBindingIntegrityActivePolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 2),
    _RlNbrBindingIntegrityActivePolicyVlanTag_Type()
)
rlNbrBindingIntegrityActivePolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyVlanTag.setStatus("current")


class _RlNbrBindingIntegrityActivePolicyNamePort_Type(DisplayString):
    """Custom type rlNbrBindingIntegrityActivePolicyNamePort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNbrBindingIntegrityActivePolicyNamePort_Type.__name__ = "DisplayString"
_RlNbrBindingIntegrityActivePolicyNamePort_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyNamePort = _RlNbrBindingIntegrityActivePolicyNamePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 3),
    _RlNbrBindingIntegrityActivePolicyNamePort_Type()
)
rlNbrBindingIntegrityActivePolicyNamePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyNamePort.setStatus("current")


class _RlNbrBindingIntegrityActivePolicyNameVlan_Type(DisplayString):
    """Custom type rlNbrBindingIntegrityActivePolicyNameVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlNbrBindingIntegrityActivePolicyNameVlan_Type.__name__ = "DisplayString"
_RlNbrBindingIntegrityActivePolicyNameVlan_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyNameVlan = _RlNbrBindingIntegrityActivePolicyNameVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 4),
    _RlNbrBindingIntegrityActivePolicyNameVlan_Type()
)
rlNbrBindingIntegrityActivePolicyNameVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyNameVlan.setStatus("current")


class _RlNbrBindingIntegrityActivePolicyDeviceRole_Type(Integer32):
    """Custom type rlNbrBindingIntegrityActivePolicyDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("perimeter", 1))
    )


_RlNbrBindingIntegrityActivePolicyDeviceRole_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityActivePolicyDeviceRole_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyDeviceRole = _RlNbrBindingIntegrityActivePolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 5),
    _RlNbrBindingIntegrityActivePolicyDeviceRole_Type()
)
rlNbrBindingIntegrityActivePolicyDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyDeviceRole.setStatus("current")
_RlNbrBindingIntegrityActivePolicyDeviceRoleType_Type = RlIpv6FhsSettingType
_RlNbrBindingIntegrityActivePolicyDeviceRoleType_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyDeviceRoleType = _RlNbrBindingIntegrityActivePolicyDeviceRoleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 6),
    _RlNbrBindingIntegrityActivePolicyDeviceRoleType_Type()
)
rlNbrBindingIntegrityActivePolicyDeviceRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyDeviceRoleType.setStatus("current")
_RlNbrBindingIntegrityActivePolicyLogBinding_Type = RlIpv6FhsSettingStatusType
_RlNbrBindingIntegrityActivePolicyLogBinding_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyLogBinding = _RlNbrBindingIntegrityActivePolicyLogBinding_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 7),
    _RlNbrBindingIntegrityActivePolicyLogBinding_Type()
)
rlNbrBindingIntegrityActivePolicyLogBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyLogBinding.setStatus("current")
_RlNbrBindingIntegrityActivePolicyLogBindingType_Type = RlIpv6FhsSettingType
_RlNbrBindingIntegrityActivePolicyLogBindingType_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyLogBindingType = _RlNbrBindingIntegrityActivePolicyLogBindingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 8),
    _RlNbrBindingIntegrityActivePolicyLogBindingType_Type()
)
rlNbrBindingIntegrityActivePolicyLogBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyLogBindingType.setStatus("current")


class _RlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit_Type(Integer32):
    """Custom type rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 2147483647),
    )


_RlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit = _RlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 9),
    _RlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit_Type()
)
rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit.setStatus("current")
_RlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimitType_Type = RlIpv6FhsSettingType
_RlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimitType_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimitType = _RlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 10),
    _RlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimitType_Type()
)
rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimitType.setStatus("current")


class _RlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit_Type(Integer32):
    """Custom type rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 2147483647),
    )


_RlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit = _RlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 11),
    _RlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit_Type()
)
rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit.setStatus("current")
_RlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimitType_Type = RlIpv6FhsSettingType
_RlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimitType_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimitType = _RlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 12),
    _RlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimitType_Type()
)
rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimitType.setStatus("current")


class _RlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit_Type(Integer32):
    """Custom type rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 2147483647),
    )


_RlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit = _RlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 13),
    _RlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit_Type()
)
rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit.setStatus("current")
_RlNbrBindingIntegrityActivePolicyMaxEntriesMacLimitType_Type = RlIpv6FhsSettingType
_RlNbrBindingIntegrityActivePolicyMaxEntriesMacLimitType_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimitType = _RlNbrBindingIntegrityActivePolicyMaxEntriesMacLimitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 14),
    _RlNbrBindingIntegrityActivePolicyMaxEntriesMacLimitType_Type()
)
rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimitType.setStatus("current")


class _RlNbrBindingIntegrityActivePolicyBindingLifetime_Type(Integer32):
    """Custom type rlNbrBindingIntegrityActivePolicyBindingLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RlNbrBindingIntegrityActivePolicyBindingLifetime_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityActivePolicyBindingLifetime_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyBindingLifetime = _RlNbrBindingIntegrityActivePolicyBindingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 15),
    _RlNbrBindingIntegrityActivePolicyBindingLifetime_Type()
)
rlNbrBindingIntegrityActivePolicyBindingLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyBindingLifetime.setStatus("current")
_RlNbrBindingIntegrityActivePolicyBindingLifetimeType_Type = RlIpv6FhsSettingType
_RlNbrBindingIntegrityActivePolicyBindingLifetimeType_Object = MibTableColumn
rlNbrBindingIntegrityActivePolicyBindingLifetimeType = _RlNbrBindingIntegrityActivePolicyBindingLifetimeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 9, 1, 16),
    _RlNbrBindingIntegrityActivePolicyBindingLifetimeType_Type()
)
rlNbrBindingIntegrityActivePolicyBindingLifetimeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityActivePolicyBindingLifetimeType.setStatus("current")


class _RlNbrBindingIntegrityBindingLifetime_Type(Integer32):
    """Custom type rlNbrBindingIntegrityBindingLifetime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RlNbrBindingIntegrityBindingLifetime_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityBindingLifetime_Object = MibScalar
rlNbrBindingIntegrityBindingLifetime = _RlNbrBindingIntegrityBindingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 10),
    _RlNbrBindingIntegrityBindingLifetime_Type()
)
rlNbrBindingIntegrityBindingLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityBindingLifetime.setStatus("current")


class _RlNbrBindingIntegrityLogBinding_Type(TruthValue):
    """Custom type rlNbrBindingIntegrityLogBinding based on TruthValue"""


_RlNbrBindingIntegrityLogBinding_Object = MibScalar
rlNbrBindingIntegrityLogBinding = _RlNbrBindingIntegrityLogBinding_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 11),
    _RlNbrBindingIntegrityLogBinding_Type()
)
rlNbrBindingIntegrityLogBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityLogBinding.setStatus("current")


class _RlNbrBindingIntegrityMaxEntriesVlanLimit_Type(Integer32):
    """Custom type rlNbrBindingIntegrityMaxEntriesVlanLimit based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 2147483647),
    )


_RlNbrBindingIntegrityMaxEntriesVlanLimit_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityMaxEntriesVlanLimit_Object = MibScalar
rlNbrBindingIntegrityMaxEntriesVlanLimit = _RlNbrBindingIntegrityMaxEntriesVlanLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 12),
    _RlNbrBindingIntegrityMaxEntriesVlanLimit_Type()
)
rlNbrBindingIntegrityMaxEntriesVlanLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityMaxEntriesVlanLimit.setStatus("current")


class _RlNbrBindingIntegrityMaxEntriesInterfaceLimit_Type(Integer32):
    """Custom type rlNbrBindingIntegrityMaxEntriesInterfaceLimit based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 2147483647),
    )


_RlNbrBindingIntegrityMaxEntriesInterfaceLimit_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityMaxEntriesInterfaceLimit_Object = MibScalar
rlNbrBindingIntegrityMaxEntriesInterfaceLimit = _RlNbrBindingIntegrityMaxEntriesInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 13),
    _RlNbrBindingIntegrityMaxEntriesInterfaceLimit_Type()
)
rlNbrBindingIntegrityMaxEntriesInterfaceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityMaxEntriesInterfaceLimit.setStatus("current")


class _RlNbrBindingIntegrityMaxEntriesMacLimit_Type(Integer32):
    """Custom type rlNbrBindingIntegrityMaxEntriesMacLimit based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 2147483647),
    )


_RlNbrBindingIntegrityMaxEntriesMacLimit_Type.__name__ = "Integer32"
_RlNbrBindingIntegrityMaxEntriesMacLimit_Object = MibScalar
rlNbrBindingIntegrityMaxEntriesMacLimit = _RlNbrBindingIntegrityMaxEntriesMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 14),
    _RlNbrBindingIntegrityMaxEntriesMacLimit_Type()
)
rlNbrBindingIntegrityMaxEntriesMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityMaxEntriesMacLimit.setStatus("current")
_RlNbrBindingIntegrityEntriesNum_Type = Integer32
_RlNbrBindingIntegrityEntriesNum_Object = MibScalar
rlNbrBindingIntegrityEntriesNum = _RlNbrBindingIntegrityEntriesNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 4, 15),
    _RlNbrBindingIntegrityEntriesNum_Type()
)
rlNbrBindingIntegrityEntriesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEntriesNum.setStatus("current")
_RlDhcpGuard_ObjectIdentity = ObjectIdentity
rlDhcpGuard = _RlDhcpGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5)
)
_RlDhcpGuardPolicyTable_Object = MibTable
rlDhcpGuardPolicyTable = _RlDhcpGuardPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1)
)
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyTable.setStatus("current")
_RlDhcpGuardPolicyEntry_Object = MibTableRow
rlDhcpGuardPolicyEntry = _RlDhcpGuardPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1)
)
rlDhcpGuardPolicyEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardPolicyName"),
)
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyEntry.setStatus("current")


class _RlDhcpGuardPolicyName_Type(DisplayString):
    """Custom type rlDhcpGuardPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpGuardPolicyName_Type.__name__ = "DisplayString"
_RlDhcpGuardPolicyName_Object = MibTableColumn
rlDhcpGuardPolicyName = _RlDhcpGuardPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1, 1),
    _RlDhcpGuardPolicyName_Type()
)
rlDhcpGuardPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyName.setStatus("current")


class _RlDhcpGuardPolicyDeviceRole_Type(Integer32):
    """Custom type rlDhcpGuardPolicyDeviceRole based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2),
          ("unspecified", -1))
    )


_RlDhcpGuardPolicyDeviceRole_Type.__name__ = "Integer32"
_RlDhcpGuardPolicyDeviceRole_Object = MibTableColumn
rlDhcpGuardPolicyDeviceRole = _RlDhcpGuardPolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1, 2),
    _RlDhcpGuardPolicyDeviceRole_Type()
)
rlDhcpGuardPolicyDeviceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyDeviceRole.setStatus("current")


class _RlDhcpGuardPolicyMatchServerAddrSpecified_Type(TruthValue):
    """Custom type rlDhcpGuardPolicyMatchServerAddrSpecified based on TruthValue"""


_RlDhcpGuardPolicyMatchServerAddrSpecified_Object = MibTableColumn
rlDhcpGuardPolicyMatchServerAddrSpecified = _RlDhcpGuardPolicyMatchServerAddrSpecified_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1, 3),
    _RlDhcpGuardPolicyMatchServerAddrSpecified_Type()
)
rlDhcpGuardPolicyMatchServerAddrSpecified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyMatchServerAddrSpecified.setStatus("current")


class _RlDhcpGuardPolicyMatchServerAddr_Type(DisplayString):
    """Custom type rlDhcpGuardPolicyMatchServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpGuardPolicyMatchServerAddr_Type.__name__ = "DisplayString"
_RlDhcpGuardPolicyMatchServerAddr_Object = MibTableColumn
rlDhcpGuardPolicyMatchServerAddr = _RlDhcpGuardPolicyMatchServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1, 4),
    _RlDhcpGuardPolicyMatchServerAddr_Type()
)
rlDhcpGuardPolicyMatchServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyMatchServerAddr.setStatus("current")


class _RlDhcpGuardPolicyMatchReplyAddrSpecified_Type(TruthValue):
    """Custom type rlDhcpGuardPolicyMatchReplyAddrSpecified based on TruthValue"""


_RlDhcpGuardPolicyMatchReplyAddrSpecified_Object = MibTableColumn
rlDhcpGuardPolicyMatchReplyAddrSpecified = _RlDhcpGuardPolicyMatchReplyAddrSpecified_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1, 5),
    _RlDhcpGuardPolicyMatchReplyAddrSpecified_Type()
)
rlDhcpGuardPolicyMatchReplyAddrSpecified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyMatchReplyAddrSpecified.setStatus("current")


class _RlDhcpGuardPolicyMatchReplyAddr_Type(DisplayString):
    """Custom type rlDhcpGuardPolicyMatchReplyAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpGuardPolicyMatchReplyAddr_Type.__name__ = "DisplayString"
_RlDhcpGuardPolicyMatchReplyAddr_Object = MibTableColumn
rlDhcpGuardPolicyMatchReplyAddr = _RlDhcpGuardPolicyMatchReplyAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1, 6),
    _RlDhcpGuardPolicyMatchReplyAddr_Type()
)
rlDhcpGuardPolicyMatchReplyAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyMatchReplyAddr.setStatus("current")


class _RlDhcpGuardPolicyPrefMin_Type(Integer32):
    """Custom type rlDhcpGuardPolicyPrefMin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_RlDhcpGuardPolicyPrefMin_Type.__name__ = "Integer32"
_RlDhcpGuardPolicyPrefMin_Object = MibTableColumn
rlDhcpGuardPolicyPrefMin = _RlDhcpGuardPolicyPrefMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1, 7),
    _RlDhcpGuardPolicyPrefMin_Type()
)
rlDhcpGuardPolicyPrefMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPrefMin.setStatus("current")


class _RlDhcpGuardPolicyPrefMax_Type(Integer32):
    """Custom type rlDhcpGuardPolicyPrefMax based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_RlDhcpGuardPolicyPrefMax_Type.__name__ = "Integer32"
_RlDhcpGuardPolicyPrefMax_Object = MibTableColumn
rlDhcpGuardPolicyPrefMax = _RlDhcpGuardPolicyPrefMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1, 8),
    _RlDhcpGuardPolicyPrefMax_Type()
)
rlDhcpGuardPolicyPrefMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPrefMax.setStatus("current")
_RlDhcpGuardPolicyRowStatus_Type = RowStatus
_RlDhcpGuardPolicyRowStatus_Object = MibTableColumn
rlDhcpGuardPolicyRowStatus = _RlDhcpGuardPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 1, 1, 9),
    _RlDhcpGuardPolicyRowStatus_Type()
)
rlDhcpGuardPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyRowStatus.setStatus("current")
_RlDhcpGuardPortPolicyTable_Object = MibTable
rlDhcpGuardPortPolicyTable = _RlDhcpGuardPortPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 2)
)
if mibBuilder.loadTexts:
    rlDhcpGuardPortPolicyTable.setStatus("current")
_RlDhcpGuardPortPolicyEntry_Object = MibTableRow
rlDhcpGuardPortPolicyEntry = _RlDhcpGuardPortPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 2, 1)
)
rlDhcpGuardPortPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardPortPolicyIfIndex"),
    (1, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardPortPolicyName"),
)
if mibBuilder.loadTexts:
    rlDhcpGuardPortPolicyEntry.setStatus("current")
_RlDhcpGuardPortPolicyIfIndex_Type = InterfaceIndex
_RlDhcpGuardPortPolicyIfIndex_Object = MibTableColumn
rlDhcpGuardPortPolicyIfIndex = _RlDhcpGuardPortPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 2, 1, 1),
    _RlDhcpGuardPortPolicyIfIndex_Type()
)
rlDhcpGuardPortPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardPortPolicyIfIndex.setStatus("current")


class _RlDhcpGuardPortPolicyName_Type(DisplayString):
    """Custom type rlDhcpGuardPortPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpGuardPortPolicyName_Type.__name__ = "DisplayString"
_RlDhcpGuardPortPolicyName_Object = MibTableColumn
rlDhcpGuardPortPolicyName = _RlDhcpGuardPortPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 2, 1, 2),
    _RlDhcpGuardPortPolicyName_Type()
)
rlDhcpGuardPortPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardPortPolicyName.setStatus("current")


class _RlDhcpGuardPortPolicyVlan1to1024_Type(OctetString):
    """Custom type rlDhcpGuardPortPolicyVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPortPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlDhcpGuardPortPolicyVlan1to1024_Object = MibTableColumn
rlDhcpGuardPortPolicyVlan1to1024 = _RlDhcpGuardPortPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 2, 1, 3),
    _RlDhcpGuardPortPolicyVlan1to1024_Type()
)
rlDhcpGuardPortPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPortPolicyVlan1to1024.setStatus("current")


class _RlDhcpGuardPortPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlDhcpGuardPortPolicyVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPortPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlDhcpGuardPortPolicyVlan1025to2048_Object = MibTableColumn
rlDhcpGuardPortPolicyVlan1025to2048 = _RlDhcpGuardPortPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 2, 1, 4),
    _RlDhcpGuardPortPolicyVlan1025to2048_Type()
)
rlDhcpGuardPortPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPortPolicyVlan1025to2048.setStatus("current")


class _RlDhcpGuardPortPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlDhcpGuardPortPolicyVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPortPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlDhcpGuardPortPolicyVlan2049to3072_Object = MibTableColumn
rlDhcpGuardPortPolicyVlan2049to3072 = _RlDhcpGuardPortPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 2, 1, 5),
    _RlDhcpGuardPortPolicyVlan2049to3072_Type()
)
rlDhcpGuardPortPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPortPolicyVlan2049to3072.setStatus("current")


class _RlDhcpGuardPortPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlDhcpGuardPortPolicyVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPortPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlDhcpGuardPortPolicyVlan3073to4094_Object = MibTableColumn
rlDhcpGuardPortPolicyVlan3073to4094 = _RlDhcpGuardPortPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 2, 1, 6),
    _RlDhcpGuardPortPolicyVlan3073to4094_Type()
)
rlDhcpGuardPortPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPortPolicyVlan3073to4094.setStatus("current")
_RlDhcpGuardPortPolicyRowStatus_Type = RowStatus
_RlDhcpGuardPortPolicyRowStatus_Object = MibTableColumn
rlDhcpGuardPortPolicyRowStatus = _RlDhcpGuardPortPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 2, 1, 7),
    _RlDhcpGuardPortPolicyRowStatus_Type()
)
rlDhcpGuardPortPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpGuardPortPolicyRowStatus.setStatus("current")
_RlDhcpGuardPolicyPortTable_Object = MibTable
rlDhcpGuardPolicyPortTable = _RlDhcpGuardPolicyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 3)
)
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPortTable.setStatus("current")
_RlDhcpGuardPolicyPortEntry_Object = MibTableRow
rlDhcpGuardPolicyPortEntry = _RlDhcpGuardPolicyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 3, 1)
)
rlDhcpGuardPolicyPortEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardPolicyPortName"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardPolicyPortIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPortEntry.setStatus("current")


class _RlDhcpGuardPolicyPortName_Type(DisplayString):
    """Custom type rlDhcpGuardPolicyPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpGuardPolicyPortName_Type.__name__ = "DisplayString"
_RlDhcpGuardPolicyPortName_Object = MibTableColumn
rlDhcpGuardPolicyPortName = _RlDhcpGuardPolicyPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 3, 1, 1),
    _RlDhcpGuardPolicyPortName_Type()
)
rlDhcpGuardPolicyPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPortName.setStatus("current")
_RlDhcpGuardPolicyPortIfIndex_Type = InterfaceIndex
_RlDhcpGuardPolicyPortIfIndex_Object = MibTableColumn
rlDhcpGuardPolicyPortIfIndex = _RlDhcpGuardPolicyPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 3, 1, 2),
    _RlDhcpGuardPolicyPortIfIndex_Type()
)
rlDhcpGuardPolicyPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPortIfIndex.setStatus("current")


class _RlDhcpGuardPolicyPortVlan1to1024_Type(OctetString):
    """Custom type rlDhcpGuardPolicyPortVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPolicyPortVlan1to1024_Type.__name__ = "OctetString"
_RlDhcpGuardPolicyPortVlan1to1024_Object = MibTableColumn
rlDhcpGuardPolicyPortVlan1to1024 = _RlDhcpGuardPolicyPortVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 3, 1, 3),
    _RlDhcpGuardPolicyPortVlan1to1024_Type()
)
rlDhcpGuardPolicyPortVlan1to1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPortVlan1to1024.setStatus("current")


class _RlDhcpGuardPolicyPortVlan1025to2048_Type(OctetString):
    """Custom type rlDhcpGuardPolicyPortVlan1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPolicyPortVlan1025to2048_Type.__name__ = "OctetString"
_RlDhcpGuardPolicyPortVlan1025to2048_Object = MibTableColumn
rlDhcpGuardPolicyPortVlan1025to2048 = _RlDhcpGuardPolicyPortVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 3, 1, 4),
    _RlDhcpGuardPolicyPortVlan1025to2048_Type()
)
rlDhcpGuardPolicyPortVlan1025to2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPortVlan1025to2048.setStatus("current")


class _RlDhcpGuardPolicyPortVlan2049to3072_Type(OctetString):
    """Custom type rlDhcpGuardPolicyPortVlan2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPolicyPortVlan2049to3072_Type.__name__ = "OctetString"
_RlDhcpGuardPolicyPortVlan2049to3072_Object = MibTableColumn
rlDhcpGuardPolicyPortVlan2049to3072 = _RlDhcpGuardPolicyPortVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 3, 1, 5),
    _RlDhcpGuardPolicyPortVlan2049to3072_Type()
)
rlDhcpGuardPolicyPortVlan2049to3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPortVlan2049to3072.setStatus("current")


class _RlDhcpGuardPolicyPortVlan3073to4094_Type(OctetString):
    """Custom type rlDhcpGuardPolicyPortVlan3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPolicyPortVlan3073to4094_Type.__name__ = "OctetString"
_RlDhcpGuardPolicyPortVlan3073to4094_Object = MibTableColumn
rlDhcpGuardPolicyPortVlan3073to4094 = _RlDhcpGuardPolicyPortVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 3, 1, 6),
    _RlDhcpGuardPolicyPortVlan3073to4094_Type()
)
rlDhcpGuardPolicyPortVlan3073to4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyPortVlan3073to4094.setStatus("current")
_RlDhcpGuardVlanPolicyTable_Object = MibTable
rlDhcpGuardVlanPolicyTable = _RlDhcpGuardVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 4)
)
if mibBuilder.loadTexts:
    rlDhcpGuardVlanPolicyTable.setStatus("current")
_RlDhcpGuardVlanPolicyEntry_Object = MibTableRow
rlDhcpGuardVlanPolicyEntry = _RlDhcpGuardVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 4, 1)
)
rlDhcpGuardVlanPolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardVlanPolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlDhcpGuardVlanPolicyEntry.setStatus("current")
_RlDhcpGuardVlanPolicyVlanTag_Type = VlanId
_RlDhcpGuardVlanPolicyVlanTag_Object = MibTableColumn
rlDhcpGuardVlanPolicyVlanTag = _RlDhcpGuardVlanPolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 4, 1, 1),
    _RlDhcpGuardVlanPolicyVlanTag_Type()
)
rlDhcpGuardVlanPolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardVlanPolicyVlanTag.setStatus("current")


class _RlDhcpGuardVlanPolicyName_Type(DisplayString):
    """Custom type rlDhcpGuardVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpGuardVlanPolicyName_Type.__name__ = "DisplayString"
_RlDhcpGuardVlanPolicyName_Object = MibTableColumn
rlDhcpGuardVlanPolicyName = _RlDhcpGuardVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 4, 1, 2),
    _RlDhcpGuardVlanPolicyName_Type()
)
rlDhcpGuardVlanPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardVlanPolicyName.setStatus("current")
_RlDhcpGuardVlanPolicyRowStatus_Type = RowStatus
_RlDhcpGuardVlanPolicyRowStatus_Object = MibTableColumn
rlDhcpGuardVlanPolicyRowStatus = _RlDhcpGuardVlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 4, 1, 3),
    _RlDhcpGuardVlanPolicyRowStatus_Type()
)
rlDhcpGuardVlanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpGuardVlanPolicyRowStatus.setStatus("current")
_RlDhcpGuardPolicyVlanTable_Object = MibTable
rlDhcpGuardPolicyVlanTable = _RlDhcpGuardPolicyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 5)
)
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyVlanTable.setStatus("current")
_RlDhcpGuardPolicyVlanEntry_Object = MibTableRow
rlDhcpGuardPolicyVlanEntry = _RlDhcpGuardPolicyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 5, 1)
)
rlDhcpGuardPolicyVlanEntry.setIndexNames(
    (1, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardPolicyVlanPolicyName"),
)
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyVlanEntry.setStatus("current")


class _RlDhcpGuardPolicyVlanPolicyName_Type(DisplayString):
    """Custom type rlDhcpGuardPolicyVlanPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpGuardPolicyVlanPolicyName_Type.__name__ = "DisplayString"
_RlDhcpGuardPolicyVlanPolicyName_Object = MibTableColumn
rlDhcpGuardPolicyVlanPolicyName = _RlDhcpGuardPolicyVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 5, 1, 1),
    _RlDhcpGuardPolicyVlanPolicyName_Type()
)
rlDhcpGuardPolicyVlanPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyVlanPolicyName.setStatus("current")


class _RlDhcpGuardPolicyVlan1to1024_Type(OctetString):
    """Custom type rlDhcpGuardPolicyVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPolicyVlan1to1024_Type.__name__ = "OctetString"
_RlDhcpGuardPolicyVlan1to1024_Object = MibTableColumn
rlDhcpGuardPolicyVlan1to1024 = _RlDhcpGuardPolicyVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 5, 1, 2),
    _RlDhcpGuardPolicyVlan1to1024_Type()
)
rlDhcpGuardPolicyVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyVlan1to1024.setStatus("current")


class _RlDhcpGuardPolicyVlan1025to2048_Type(OctetString):
    """Custom type rlDhcpGuardPolicyVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPolicyVlan1025to2048_Type.__name__ = "OctetString"
_RlDhcpGuardPolicyVlan1025to2048_Object = MibTableColumn
rlDhcpGuardPolicyVlan1025to2048 = _RlDhcpGuardPolicyVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 5, 1, 3),
    _RlDhcpGuardPolicyVlan1025to2048_Type()
)
rlDhcpGuardPolicyVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyVlan1025to2048.setStatus("current")


class _RlDhcpGuardPolicyVlan2049to3072_Type(OctetString):
    """Custom type rlDhcpGuardPolicyVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPolicyVlan2049to3072_Type.__name__ = "OctetString"
_RlDhcpGuardPolicyVlan2049to3072_Object = MibTableColumn
rlDhcpGuardPolicyVlan2049to3072 = _RlDhcpGuardPolicyVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 5, 1, 4),
    _RlDhcpGuardPolicyVlan2049to3072_Type()
)
rlDhcpGuardPolicyVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyVlan2049to3072.setStatus("current")


class _RlDhcpGuardPolicyVlan3073to4094_Type(OctetString):
    """Custom type rlDhcpGuardPolicyVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardPolicyVlan3073to4094_Type.__name__ = "OctetString"
_RlDhcpGuardPolicyVlan3073to4094_Object = MibTableColumn
rlDhcpGuardPolicyVlan3073to4094 = _RlDhcpGuardPolicyVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 5, 1, 5),
    _RlDhcpGuardPolicyVlan3073to4094_Type()
)
rlDhcpGuardPolicyVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPolicyVlan3073to4094.setStatus("current")
_RlDhcpGuardEnableVlanTable_Object = MibTable
rlDhcpGuardEnableVlanTable = _RlDhcpGuardEnableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 6)
)
if mibBuilder.loadTexts:
    rlDhcpGuardEnableVlanTable.setStatus("current")
_RlDhcpGuardEnableVlanEntry_Object = MibTableRow
rlDhcpGuardEnableVlanEntry = _RlDhcpGuardEnableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 6, 1)
)
rlDhcpGuardEnableVlanEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardEnableVlanIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpGuardEnableVlanEntry.setStatus("current")


class _RlDhcpGuardEnableVlanIndex_Type(Integer32):
    """Custom type rlDhcpGuardEnableVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )


_RlDhcpGuardEnableVlanIndex_Type.__name__ = "Integer32"
_RlDhcpGuardEnableVlanIndex_Object = MibTableColumn
rlDhcpGuardEnableVlanIndex = _RlDhcpGuardEnableVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 6, 1, 1),
    _RlDhcpGuardEnableVlanIndex_Type()
)
rlDhcpGuardEnableVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardEnableVlanIndex.setStatus("current")


class _RlDhcpGuardEnableVlan1to1024_Type(OctetString):
    """Custom type rlDhcpGuardEnableVlan1to1024 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardEnableVlan1to1024_Type.__name__ = "OctetString"
_RlDhcpGuardEnableVlan1to1024_Object = MibTableColumn
rlDhcpGuardEnableVlan1to1024 = _RlDhcpGuardEnableVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 6, 1, 2),
    _RlDhcpGuardEnableVlan1to1024_Type()
)
rlDhcpGuardEnableVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardEnableVlan1to1024.setStatus("current")


class _RlDhcpGuardEnableVlan1025to2048_Type(OctetString):
    """Custom type rlDhcpGuardEnableVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardEnableVlan1025to2048_Type.__name__ = "OctetString"
_RlDhcpGuardEnableVlan1025to2048_Object = MibTableColumn
rlDhcpGuardEnableVlan1025to2048 = _RlDhcpGuardEnableVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 6, 1, 3),
    _RlDhcpGuardEnableVlan1025to2048_Type()
)
rlDhcpGuardEnableVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardEnableVlan1025to2048.setStatus("current")


class _RlDhcpGuardEnableVlan2049to3072_Type(OctetString):
    """Custom type rlDhcpGuardEnableVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardEnableVlan2049to3072_Type.__name__ = "OctetString"
_RlDhcpGuardEnableVlan2049to3072_Object = MibTableColumn
rlDhcpGuardEnableVlan2049to3072 = _RlDhcpGuardEnableVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 6, 1, 4),
    _RlDhcpGuardEnableVlan2049to3072_Type()
)
rlDhcpGuardEnableVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardEnableVlan2049to3072.setStatus("current")


class _RlDhcpGuardEnableVlan3073to4094_Type(OctetString):
    """Custom type rlDhcpGuardEnableVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpGuardEnableVlan3073to4094_Type.__name__ = "OctetString"
_RlDhcpGuardEnableVlan3073to4094_Object = MibTableColumn
rlDhcpGuardEnableVlan3073to4094 = _RlDhcpGuardEnableVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 6, 1, 5),
    _RlDhcpGuardEnableVlan3073to4094_Type()
)
rlDhcpGuardEnableVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardEnableVlan3073to4094.setStatus("current")
_RlDhcpGuardActivePolicyTable_Object = MibTable
rlDhcpGuardActivePolicyTable = _RlDhcpGuardActivePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7)
)
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyTable.setStatus("current")
_RlDhcpGuardActivePolicyEntry_Object = MibTableRow
rlDhcpGuardActivePolicyEntry = _RlDhcpGuardActivePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1)
)
rlDhcpGuardActivePolicyEntry.setIndexNames(
    (0, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardActivePolicyIfIndex"),
    (0, "CISCOSB-IPV6FHS-MIB", "rlDhcpGuardActivePolicyVlanTag"),
)
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyEntry.setStatus("current")
_RlDhcpGuardActivePolicyIfIndex_Type = InterfaceIndex
_RlDhcpGuardActivePolicyIfIndex_Object = MibTableColumn
rlDhcpGuardActivePolicyIfIndex = _RlDhcpGuardActivePolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 1),
    _RlDhcpGuardActivePolicyIfIndex_Type()
)
rlDhcpGuardActivePolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyIfIndex.setStatus("current")
_RlDhcpGuardActivePolicyVlanTag_Type = VlanId
_RlDhcpGuardActivePolicyVlanTag_Object = MibTableColumn
rlDhcpGuardActivePolicyVlanTag = _RlDhcpGuardActivePolicyVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 2),
    _RlDhcpGuardActivePolicyVlanTag_Type()
)
rlDhcpGuardActivePolicyVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyVlanTag.setStatus("current")


class _RlDhcpGuardActivePolicyNamePort_Type(DisplayString):
    """Custom type rlDhcpGuardActivePolicyNamePort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpGuardActivePolicyNamePort_Type.__name__ = "DisplayString"
_RlDhcpGuardActivePolicyNamePort_Object = MibTableColumn
rlDhcpGuardActivePolicyNamePort = _RlDhcpGuardActivePolicyNamePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 3),
    _RlDhcpGuardActivePolicyNamePort_Type()
)
rlDhcpGuardActivePolicyNamePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyNamePort.setStatus("current")


class _RlDhcpGuardActivePolicyNameVlan_Type(DisplayString):
    """Custom type rlDhcpGuardActivePolicyNameVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpGuardActivePolicyNameVlan_Type.__name__ = "DisplayString"
_RlDhcpGuardActivePolicyNameVlan_Object = MibTableColumn
rlDhcpGuardActivePolicyNameVlan = _RlDhcpGuardActivePolicyNameVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 4),
    _RlDhcpGuardActivePolicyNameVlan_Type()
)
rlDhcpGuardActivePolicyNameVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyNameVlan.setStatus("current")


class _RlDhcpGuardActivePolicyDeviceRole_Type(Integer32):
    """Custom type rlDhcpGuardActivePolicyDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_RlDhcpGuardActivePolicyDeviceRole_Type.__name__ = "Integer32"
_RlDhcpGuardActivePolicyDeviceRole_Object = MibTableColumn
rlDhcpGuardActivePolicyDeviceRole = _RlDhcpGuardActivePolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 5),
    _RlDhcpGuardActivePolicyDeviceRole_Type()
)
rlDhcpGuardActivePolicyDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyDeviceRole.setStatus("current")
_RlDhcpGuardActivePolicyDeviceRoleType_Type = RlIpv6FhsSettingType
_RlDhcpGuardActivePolicyDeviceRoleType_Object = MibTableColumn
rlDhcpGuardActivePolicyDeviceRoleType = _RlDhcpGuardActivePolicyDeviceRoleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 6),
    _RlDhcpGuardActivePolicyDeviceRoleType_Type()
)
rlDhcpGuardActivePolicyDeviceRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyDeviceRoleType.setStatus("current")


class _RlDhcpGuardActivePolicyMatchServerAddr_Type(DisplayString):
    """Custom type rlDhcpGuardActivePolicyMatchServerAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpGuardActivePolicyMatchServerAddr_Type.__name__ = "DisplayString"
_RlDhcpGuardActivePolicyMatchServerAddr_Object = MibTableColumn
rlDhcpGuardActivePolicyMatchServerAddr = _RlDhcpGuardActivePolicyMatchServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 7),
    _RlDhcpGuardActivePolicyMatchServerAddr_Type()
)
rlDhcpGuardActivePolicyMatchServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyMatchServerAddr.setStatus("current")
_RlDhcpGuardActivePolicyMatchServerAddrType_Type = RlIpv6FhsSettingType
_RlDhcpGuardActivePolicyMatchServerAddrType_Object = MibTableColumn
rlDhcpGuardActivePolicyMatchServerAddrType = _RlDhcpGuardActivePolicyMatchServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 8),
    _RlDhcpGuardActivePolicyMatchServerAddrType_Type()
)
rlDhcpGuardActivePolicyMatchServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyMatchServerAddrType.setStatus("current")


class _RlDhcpGuardActivePolicyMatchReplyAddr_Type(DisplayString):
    """Custom type rlDhcpGuardActivePolicyMatchReplyAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpGuardActivePolicyMatchReplyAddr_Type.__name__ = "DisplayString"
_RlDhcpGuardActivePolicyMatchReplyAddr_Object = MibTableColumn
rlDhcpGuardActivePolicyMatchReplyAddr = _RlDhcpGuardActivePolicyMatchReplyAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 9),
    _RlDhcpGuardActivePolicyMatchReplyAddr_Type()
)
rlDhcpGuardActivePolicyMatchReplyAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyMatchReplyAddr.setStatus("current")
_RlDhcpGuardActivePolicyMatchReplyAddrType_Type = RlIpv6FhsSettingType
_RlDhcpGuardActivePolicyMatchReplyAddrType_Object = MibTableColumn
rlDhcpGuardActivePolicyMatchReplyAddrType = _RlDhcpGuardActivePolicyMatchReplyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 10),
    _RlDhcpGuardActivePolicyMatchReplyAddrType_Type()
)
rlDhcpGuardActivePolicyMatchReplyAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyMatchReplyAddrType.setStatus("current")


class _RlDhcpGuardActivePolicyPrefMin_Type(Integer32):
    """Custom type rlDhcpGuardActivePolicyPrefMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 255),
    )


_RlDhcpGuardActivePolicyPrefMin_Type.__name__ = "Integer32"
_RlDhcpGuardActivePolicyPrefMin_Object = MibTableColumn
rlDhcpGuardActivePolicyPrefMin = _RlDhcpGuardActivePolicyPrefMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 11),
    _RlDhcpGuardActivePolicyPrefMin_Type()
)
rlDhcpGuardActivePolicyPrefMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyPrefMin.setStatus("current")
_RlDhcpGuardActivePolicyPrefMinType_Type = RlIpv6FhsSettingType
_RlDhcpGuardActivePolicyPrefMinType_Object = MibTableColumn
rlDhcpGuardActivePolicyPrefMinType = _RlDhcpGuardActivePolicyPrefMinType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 12),
    _RlDhcpGuardActivePolicyPrefMinType_Type()
)
rlDhcpGuardActivePolicyPrefMinType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyPrefMinType.setStatus("current")


class _RlDhcpGuardActivePolicyPrefMax_Type(Integer32):
    """Custom type rlDhcpGuardActivePolicyPrefMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 255),
    )


_RlDhcpGuardActivePolicyPrefMax_Type.__name__ = "Integer32"
_RlDhcpGuardActivePolicyPrefMax_Object = MibTableColumn
rlDhcpGuardActivePolicyPrefMax = _RlDhcpGuardActivePolicyPrefMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 13),
    _RlDhcpGuardActivePolicyPrefMax_Type()
)
rlDhcpGuardActivePolicyPrefMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyPrefMax.setStatus("current")
_RlDhcpGuardActivePolicyPrefMaxType_Type = RlIpv6FhsSettingType
_RlDhcpGuardActivePolicyPrefMaxType_Object = MibTableColumn
rlDhcpGuardActivePolicyPrefMaxType = _RlDhcpGuardActivePolicyPrefMaxType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 7, 1, 14),
    _RlDhcpGuardActivePolicyPrefMaxType_Type()
)
rlDhcpGuardActivePolicyPrefMaxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpGuardActivePolicyPrefMaxType.setStatus("current")


class _RlDhcpGuardPrefMin_Type(Integer32):
    """Custom type rlDhcpGuardPrefMin based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 255),
    )


_RlDhcpGuardPrefMin_Type.__name__ = "Integer32"
_RlDhcpGuardPrefMin_Object = MibScalar
rlDhcpGuardPrefMin = _RlDhcpGuardPrefMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 8),
    _RlDhcpGuardPrefMin_Type()
)
rlDhcpGuardPrefMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPrefMin.setStatus("current")


class _RlDhcpGuardPrefMax_Type(Integer32):
    """Custom type rlDhcpGuardPrefMax based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(0, 255),
    )


_RlDhcpGuardPrefMax_Type.__name__ = "Integer32"
_RlDhcpGuardPrefMax_Object = MibScalar
rlDhcpGuardPrefMax = _RlDhcpGuardPrefMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215, 5, 9),
    _RlDhcpGuardPrefMax_Type()
)
rlDhcpGuardPrefMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpGuardPrefMax.setStatus("current")

# Managed Objects groups


# Notification objects

rlNdInspectionMessageDropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 228)
)
rlNdInspectionMessageDropTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlNdInspectionMessageDropTrap.setStatus(
        "current"
    )

rlRaGuardMessageDropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 229)
)
rlRaGuardMessageDropTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlRaGuardMessageDropTrap.setStatus(
        "current"
    )

rlNbrBindingIntegrityEntryAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 230)
)
rlNbrBindingIntegrityEntryAddedTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEntryAddedTrap.setStatus(
        "current"
    )

rlNbrBindingIntegrityEntryStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 231)
)
rlNbrBindingIntegrityEntryStateChangeTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEntryStateChangeTrap.setStatus(
        "current"
    )

rlNbrBindingIntegrityEntryAnchorChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 232)
)
rlNbrBindingIntegrityEntryAnchorChangeTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEntryAnchorChangeTrap.setStatus(
        "current"
    )

rlNbrBindingIntegrityEntryDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 233)
)
rlNbrBindingIntegrityEntryDeletedTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEntryDeletedTrap.setStatus(
        "current"
    )

rlNbrBindingIntegrityEntryLimitReachTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 234)
)
rlNbrBindingIntegrityEntryLimitReachTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityEntryLimitReachTrap.setStatus(
        "current"
    )

rlNbrBindingIntegrityOverflowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 235)
)
rlNbrBindingIntegrityOverflowTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlNbrBindingIntegrityOverflowTrap.setStatus(
        "current"
    )

rlDhcpGuardMessageDropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 236)
)
rlDhcpGuardMessageDropTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlDhcpGuardMessageDropTrap.setStatus(
        "current"
    )

rlSrcGuardMessageDropTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 237)
)
rlSrcGuardMessageDropTrap.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlSrcGuardMessageDropTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-IPV6FHS-MIB",
    **{"RlIpv6FhsSettingStatusType": RlIpv6FhsSettingStatusType,
       "RlIpv6FhsSettingType": RlIpv6FhsSettingType,
       "rlNdInspectionMessageDropTrap": rlNdInspectionMessageDropTrap,
       "rlRaGuardMessageDropTrap": rlRaGuardMessageDropTrap,
       "rlNbrBindingIntegrityEntryAddedTrap": rlNbrBindingIntegrityEntryAddedTrap,
       "rlNbrBindingIntegrityEntryStateChangeTrap": rlNbrBindingIntegrityEntryStateChangeTrap,
       "rlNbrBindingIntegrityEntryAnchorChangeTrap": rlNbrBindingIntegrityEntryAnchorChangeTrap,
       "rlNbrBindingIntegrityEntryDeletedTrap": rlNbrBindingIntegrityEntryDeletedTrap,
       "rlNbrBindingIntegrityEntryLimitReachTrap": rlNbrBindingIntegrityEntryLimitReachTrap,
       "rlNbrBindingIntegrityOverflowTrap": rlNbrBindingIntegrityOverflowTrap,
       "rlDhcpGuardMessageDropTrap": rlDhcpGuardMessageDropTrap,
       "rlSrcGuardMessageDropTrap": rlSrcGuardMessageDropTrap,
       "rlIpv6Fhs": rlIpv6Fhs,
       "rlFirstHopSec": rlFirstHopSec,
       "rlFirstHopSecPolicyTable": rlFirstHopSecPolicyTable,
       "rlFirstHopSecPolicyEntry": rlFirstHopSecPolicyEntry,
       "rlFirstHopSecPolicyName": rlFirstHopSecPolicyName,
       "rlFirstHopSecPolicyLogDrop": rlFirstHopSecPolicyLogDrop,
       "rlFirstHopSecPolicyRowStatus": rlFirstHopSecPolicyRowStatus,
       "rlFirstHopSecPortPolicyTable": rlFirstHopSecPortPolicyTable,
       "rlFirstHopSecPortPolicyEntry": rlFirstHopSecPortPolicyEntry,
       "rlFirstHopSecPortPolicyIfIndex": rlFirstHopSecPortPolicyIfIndex,
       "rlFirstHopSecPortPolicyName": rlFirstHopSecPortPolicyName,
       "rlFirstHopSecPortPolicyVlan1to1024": rlFirstHopSecPortPolicyVlan1to1024,
       "rlFirstHopSecPortPolicyVlan1025to2048": rlFirstHopSecPortPolicyVlan1025to2048,
       "rlFirstHopSecPortPolicyVlan2049to3072": rlFirstHopSecPortPolicyVlan2049to3072,
       "rlFirstHopSecPortPolicyVlan3073to4094": rlFirstHopSecPortPolicyVlan3073to4094,
       "rlFirstHopSecPortPolicyRowStatus": rlFirstHopSecPortPolicyRowStatus,
       "rlFirstHopSecPolicyPortTable": rlFirstHopSecPolicyPortTable,
       "rlFirstHopSecPolicyPortEntry": rlFirstHopSecPolicyPortEntry,
       "rlFirstHopSecPolicyPortName": rlFirstHopSecPolicyPortName,
       "rlFirstHopSecPolicyPortIfIndex": rlFirstHopSecPolicyPortIfIndex,
       "rlFirstHopSecPolicyPortVlan1to1024": rlFirstHopSecPolicyPortVlan1to1024,
       "rlFirstHopSecPolicyPortVlan1025to2048": rlFirstHopSecPolicyPortVlan1025to2048,
       "rlFirstHopSecPolicyPortVlan2049to3072": rlFirstHopSecPolicyPortVlan2049to3072,
       "rlFirstHopSecPolicyPortVlan3073to4094": rlFirstHopSecPolicyPortVlan3073to4094,
       "rlFirstHopSecVlanPolicyTable": rlFirstHopSecVlanPolicyTable,
       "rlFirstHopSecVlanPolicyEntry": rlFirstHopSecVlanPolicyEntry,
       "rlFirstHopSecVlanPolicyVlanTag": rlFirstHopSecVlanPolicyVlanTag,
       "rlFirstHopSecVlanPolicyName": rlFirstHopSecVlanPolicyName,
       "rlFirstHopSecVlanPolicyRowStatus": rlFirstHopSecVlanPolicyRowStatus,
       "rlFirstHopSecPolicyVlanTable": rlFirstHopSecPolicyVlanTable,
       "rlFirstHopSecPolicyVlanEntry": rlFirstHopSecPolicyVlanEntry,
       "rlFirstHopSecPolicyVlanPolicyName": rlFirstHopSecPolicyVlanPolicyName,
       "rlFirstHopSecPolicyVlan1to1024": rlFirstHopSecPolicyVlan1to1024,
       "rlFirstHopSecPolicyVlan1025to2048": rlFirstHopSecPolicyVlan1025to2048,
       "rlFirstHopSecPolicyVlan2049to3072": rlFirstHopSecPolicyVlan2049to3072,
       "rlFirstHopSecPolicyVlan3073to4094": rlFirstHopSecPolicyVlan3073to4094,
       "rlFirstHopSecEnableVlanTable": rlFirstHopSecEnableVlanTable,
       "rlFirstHopSecEnableVlanEntry": rlFirstHopSecEnableVlanEntry,
       "rlFirstHopSecEnableVlanIndex": rlFirstHopSecEnableVlanIndex,
       "rlFirstHopSecEnableVlan1to1024": rlFirstHopSecEnableVlan1to1024,
       "rlFirstHopSecEnableVlan1025to2048": rlFirstHopSecEnableVlan1025to2048,
       "rlFirstHopSecEnableVlan2049to3072": rlFirstHopSecEnableVlan2049to3072,
       "rlFirstHopSecEnableVlan3073to4094": rlFirstHopSecEnableVlan3073to4094,
       "rlFirstHopSecActivePolicyTable": rlFirstHopSecActivePolicyTable,
       "rlFirstHopSecActivePolicyEntry": rlFirstHopSecActivePolicyEntry,
       "rlFirstHopSecActivePolicyIfIndex": rlFirstHopSecActivePolicyIfIndex,
       "rlFirstHopSecActivePolicyVlanTag": rlFirstHopSecActivePolicyVlanTag,
       "rlFirstHopSecActivePolicyNamePort": rlFirstHopSecActivePolicyNamePort,
       "rlFirstHopSecActivePolicyNameVlan": rlFirstHopSecActivePolicyNameVlan,
       "rlFirstHopSecActivePolicyLogDrop": rlFirstHopSecActivePolicyLogDrop,
       "rlFirstHopSecActivePolicyLogDropType": rlFirstHopSecActivePolicyLogDropType,
       "rlFirstHopSecCountersTable": rlFirstHopSecCountersTable,
       "rlFirstHopSecCountersEntry": rlFirstHopSecCountersEntry,
       "rlFirstHopSecCountersIfIndex": rlFirstHopSecCountersIfIndex,
       "rlFirstHopSecCountersRxNdpRA": rlFirstHopSecCountersRxNdpRA,
       "rlFirstHopSecCountersDropNdpRA": rlFirstHopSecCountersDropNdpRA,
       "rlFirstHopSecCountersRxNdpRS": rlFirstHopSecCountersRxNdpRS,
       "rlFirstHopSecCountersDropNdpRS": rlFirstHopSecCountersDropNdpRS,
       "rlFirstHopSecCountersRxNdpNA": rlFirstHopSecCountersRxNdpNA,
       "rlFirstHopSecCountersDropNdpNA": rlFirstHopSecCountersDropNdpNA,
       "rlFirstHopSecCountersRxNdpNS": rlFirstHopSecCountersRxNdpNS,
       "rlFirstHopSecCountersDropNdpNS": rlFirstHopSecCountersDropNdpNS,
       "rlFirstHopSecCountersRxNdpRedirect": rlFirstHopSecCountersRxNdpRedirect,
       "rlFirstHopSecCountersDropNdpRedirect": rlFirstHopSecCountersDropNdpRedirect,
       "rlFirstHopSecCountersRxDhcpAdverise": rlFirstHopSecCountersRxDhcpAdverise,
       "rlFirstHopSecCountersDropDhcpAdverise": rlFirstHopSecCountersDropDhcpAdverise,
       "rlFirstHopSecCountersRxDhcpReply": rlFirstHopSecCountersRxDhcpReply,
       "rlFirstHopSecCountersDropDhcpReply": rlFirstHopSecCountersDropDhcpReply,
       "rlFirstHopSecCountersRxDhcpReconfigure": rlFirstHopSecCountersRxDhcpReconfigure,
       "rlFirstHopSecCountersDropDhcpReconfigure": rlFirstHopSecCountersDropDhcpReconfigure,
       "rlFirstHopSecCountersRxDhcpRelayReply": rlFirstHopSecCountersRxDhcpRelayReply,
       "rlFirstHopSecCountersDropDhcpRelayReply": rlFirstHopSecCountersDropDhcpRelayReply,
       "rlFirstHopSecCountersRxDhcpLeasequeryReply": rlFirstHopSecCountersRxDhcpLeasequeryReply,
       "rlFirstHopSecCountersDropDhcpLeasequeryReply": rlFirstHopSecCountersDropDhcpLeasequeryReply,
       "rlFirstHopSecCountersDropRaGuardUnauthorizedMessage": rlFirstHopSecCountersDropRaGuardUnauthorizedMessage,
       "rlFirstHopSecCountersDropRaGuardUnauthorizedHopLimit": rlFirstHopSecCountersDropRaGuardUnauthorizedHopLimit,
       "rlFirstHopSecCountersDropRaGuardUnauthorizedManagedConfigFlag": rlFirstHopSecCountersDropRaGuardUnauthorizedManagedConfigFlag,
       "rlFirstHopSecCountersDropRaGuardUnauthorizedOtherConfigFlag": rlFirstHopSecCountersDropRaGuardUnauthorizedOtherConfigFlag,
       "rlFirstHopSecCountersDropRaGuardUnauthorizedRouterPreference": rlFirstHopSecCountersDropRaGuardUnauthorizedRouterPreference,
       "rlFirstHopSecCountersDropRaGuardUnauthorizedAdvertisedPrefix": rlFirstHopSecCountersDropRaGuardUnauthorizedAdvertisedPrefix,
       "rlFirstHopSecCountersDropRaGuardUnauthorizedSourceAddress": rlFirstHopSecCountersDropRaGuardUnauthorizedSourceAddress,
       "rlFirstHopSecCountersDropNdInspectionInvalidSourceMac": rlFirstHopSecCountersDropNdInspectionInvalidSourceMac,
       "rlFirstHopSecCountersDropNdInspectionUnsecureMessage": rlFirstHopSecCountersDropNdInspectionUnsecureMessage,
       "rlFirstHopSecCountersDropNdInspectionUnauthorizedSecLevel": rlFirstHopSecCountersDropNdInspectionUnauthorizedSecLevel,
       "rlFirstHopSecCountersDropDhcpGuardUnauthorizedMessage": rlFirstHopSecCountersDropDhcpGuardUnauthorizedMessage,
       "rlFirstHopSecCountersDropDhcpGuardUnauthorizedSourceAddress": rlFirstHopSecCountersDropDhcpGuardUnauthorizedSourceAddress,
       "rlFirstHopSecCountersDropDhcpGuardUnauthorizedServerPreference": rlFirstHopSecCountersDropDhcpGuardUnauthorizedServerPreference,
       "rlFirstHopSecCountersDropDhcpGuardUnauthorizedAssignedAddress": rlFirstHopSecCountersDropDhcpGuardUnauthorizedAssignedAddress,
       "rlFirstHopSecCountersDropSourceGuardNoBinding": rlFirstHopSecCountersDropSourceGuardNoBinding,
       "rlFirstHopSecCountersDropNbrBindingIntegrityIllegalIcmpv6": rlFirstHopSecCountersDropNbrBindingIntegrityIllegalIcmpv6,
       "rlFirstHopSecCountersDropNbrBindingIntegrityIllegalDhcpv6": rlFirstHopSecCountersDropNbrBindingIntegrityIllegalDhcpv6,
       "rlFirstHopSecLogDrop": rlFirstHopSecLogDrop,
       "rlFirstHopSecClearCounters": rlFirstHopSecClearCounters,
       "rlNdInspection": rlNdInspection,
       "rlNdInspectionPolicyTable": rlNdInspectionPolicyTable,
       "rlNdInspectionPolicyEntry": rlNdInspectionPolicyEntry,
       "rlNdInspectionPolicyName": rlNdInspectionPolicyName,
       "rlNdInspectionPolicyDeviceRole": rlNdInspectionPolicyDeviceRole,
       "rlNdInspectionPolicyDropUnsecured": rlNdInspectionPolicyDropUnsecured,
       "rlNdInspectionPolicySecLevelMin": rlNdInspectionPolicySecLevelMin,
       "rlNdInspectionPolicyValidateSrcMac": rlNdInspectionPolicyValidateSrcMac,
       "rlNdInspectionPolicyRowStatus": rlNdInspectionPolicyRowStatus,
       "rlNdInspectionPortPolicyTable": rlNdInspectionPortPolicyTable,
       "rlNdInspectionPortPolicyEntry": rlNdInspectionPortPolicyEntry,
       "rlNdInspectionPortPolicyIfIndex": rlNdInspectionPortPolicyIfIndex,
       "rlNdInspectionPortPolicyName": rlNdInspectionPortPolicyName,
       "rlNdInspectionPortPolicyVlan1to1024": rlNdInspectionPortPolicyVlan1to1024,
       "rlNdInspectionPortPolicyVlan1025to2048": rlNdInspectionPortPolicyVlan1025to2048,
       "rlNdInspectionPortPolicyVlan2049to3072": rlNdInspectionPortPolicyVlan2049to3072,
       "rlNdInspectionPortPolicyVlan3073to4094": rlNdInspectionPortPolicyVlan3073to4094,
       "rlNdInspectionPortPolicyRowStatus": rlNdInspectionPortPolicyRowStatus,
       "rlNdInspectionPolicyPortTable": rlNdInspectionPolicyPortTable,
       "rlNdInspectionPolicyPortEntry": rlNdInspectionPolicyPortEntry,
       "rlNdInspectionPolicyPortName": rlNdInspectionPolicyPortName,
       "rlNdInspectionPolicyPortIfIndex": rlNdInspectionPolicyPortIfIndex,
       "rlNdInspectionPolicyPortVlan1to1024": rlNdInspectionPolicyPortVlan1to1024,
       "rlNdInspectionPolicyPortVlan1025to2048": rlNdInspectionPolicyPortVlan1025to2048,
       "rlNdInspectionPolicyPortVlan2049to3072": rlNdInspectionPolicyPortVlan2049to3072,
       "rlNdInspectionPolicyPortVlan3073to4094": rlNdInspectionPolicyPortVlan3073to4094,
       "rlNdInspectionVlanPolicyTable": rlNdInspectionVlanPolicyTable,
       "rlNdInspectionVlanPolicyEntry": rlNdInspectionVlanPolicyEntry,
       "rlNdInspectionVlanPolicyVlanTag": rlNdInspectionVlanPolicyVlanTag,
       "rlNdInspectionVlanPolicyName": rlNdInspectionVlanPolicyName,
       "rlNdInspectionVlanPolicyRowStatus": rlNdInspectionVlanPolicyRowStatus,
       "rlNdInspectionPolicyVlanTable": rlNdInspectionPolicyVlanTable,
       "rlNdInspectionPolicyVlanEntry": rlNdInspectionPolicyVlanEntry,
       "rlNdInspectionPolicyVlanPolicyName": rlNdInspectionPolicyVlanPolicyName,
       "rlNdInspectionPolicyVlan1to1024": rlNdInspectionPolicyVlan1to1024,
       "rlNdInspectionPolicyVlan1025to2048": rlNdInspectionPolicyVlan1025to2048,
       "rlNdInspectionPolicyVlan2049to3072": rlNdInspectionPolicyVlan2049to3072,
       "rlNdInspectionPolicyVlan3073to4094": rlNdInspectionPolicyVlan3073to4094,
       "rlNdInspectionEnableVlanTable": rlNdInspectionEnableVlanTable,
       "rlNdInspectionEnableVlanEntry": rlNdInspectionEnableVlanEntry,
       "rlNdInspectionEnableVlanIndex": rlNdInspectionEnableVlanIndex,
       "rlNdInspectionEnableVlan1to1024": rlNdInspectionEnableVlan1to1024,
       "rlNdInspectionEnableVlan1025to2048": rlNdInspectionEnableVlan1025to2048,
       "rlNdInspectionEnableVlan2049to3072": rlNdInspectionEnableVlan2049to3072,
       "rlNdInspectionEnableVlan3073to4094": rlNdInspectionEnableVlan3073to4094,
       "rlNdInspectionActivePolicyTable": rlNdInspectionActivePolicyTable,
       "rlNdInspectionActivePolicyEntry": rlNdInspectionActivePolicyEntry,
       "rlNdInspectionActivePolicyIfIndex": rlNdInspectionActivePolicyIfIndex,
       "rlNdInspectionActivePolicyVlanTag": rlNdInspectionActivePolicyVlanTag,
       "rlNdInspectionActivePolicyNamePort": rlNdInspectionActivePolicyNamePort,
       "rlNdInspectionActivePolicyNameVlan": rlNdInspectionActivePolicyNameVlan,
       "rlNdInspectionActivePolicyDeviceRole": rlNdInspectionActivePolicyDeviceRole,
       "rlNdInspectionActivePolicyDeviceRoleType": rlNdInspectionActivePolicyDeviceRoleType,
       "rlNdInspectionActivePolicyDropUnsecured": rlNdInspectionActivePolicyDropUnsecured,
       "rlNdInspectionActivePolicyDropUnsecuredType": rlNdInspectionActivePolicyDropUnsecuredType,
       "rlNdInspectionActivePolicySecLevelMin": rlNdInspectionActivePolicySecLevelMin,
       "rlNdInspectionActivePolicySecLevelMinType": rlNdInspectionActivePolicySecLevelMinType,
       "rlNdInspectionActivePolicyValidateSrcMac": rlNdInspectionActivePolicyValidateSrcMac,
       "rlNdInspectionActivePolicyValidateSrcMacType": rlNdInspectionActivePolicyValidateSrcMacType,
       "rlNdInspectionValidateSrcMac": rlNdInspectionValidateSrcMac,
       "rlNdInspectionDropUnsecured": rlNdInspectionDropUnsecured,
       "rlNdInspectionSecLevelMin": rlNdInspectionSecLevelMin,
       "rlRaGuard": rlRaGuard,
       "rlRaGuardPolicyTable": rlRaGuardPolicyTable,
       "rlRaGuardPolicyEntry": rlRaGuardPolicyEntry,
       "rlRaGuardPolicyName": rlRaGuardPolicyName,
       "rlRaGuardPolicyDeviceRole": rlRaGuardPolicyDeviceRole,
       "rlRaGuardPolicyHopLimitMin": rlRaGuardPolicyHopLimitMin,
       "rlRaGuardPolicyHopLimitMax": rlRaGuardPolicyHopLimitMax,
       "rlRaGuardPolicyManagedConfigFlag": rlRaGuardPolicyManagedConfigFlag,
       "rlRaGuardPolicyMatchRaAddrSpecified": rlRaGuardPolicyMatchRaAddrSpecified,
       "rlRaGuardPolicyMatchRaAddr": rlRaGuardPolicyMatchRaAddr,
       "rlRaGuardPolicyMatchRaPrefixesSpecified": rlRaGuardPolicyMatchRaPrefixesSpecified,
       "rlRaGuardPolicyMatchRaPrefixes": rlRaGuardPolicyMatchRaPrefixes,
       "rlRaGuardPolicyOtherConfigFlag": rlRaGuardPolicyOtherConfigFlag,
       "rlRaGuardPolicyRouterPrefMin": rlRaGuardPolicyRouterPrefMin,
       "rlRaGuardPolicyRouterPrefMax": rlRaGuardPolicyRouterPrefMax,
       "rlRaGuardPolicyRowStatus": rlRaGuardPolicyRowStatus,
       "rlRaGuardPortPolicyTable": rlRaGuardPortPolicyTable,
       "rlRaGuardPortPolicyEntry": rlRaGuardPortPolicyEntry,
       "rlRaGuardPortPolicyIfIndex": rlRaGuardPortPolicyIfIndex,
       "rlRaGuardPortPolicyName": rlRaGuardPortPolicyName,
       "rlRaGuardPortPolicyVlan1to1024": rlRaGuardPortPolicyVlan1to1024,
       "rlRaGuardPortPolicyVlan1025to2048": rlRaGuardPortPolicyVlan1025to2048,
       "rlRaGuardPortPolicyVlan2049to3072": rlRaGuardPortPolicyVlan2049to3072,
       "rlRaGuardPortPolicyVlan3073to4094": rlRaGuardPortPolicyVlan3073to4094,
       "rlRaGuardPortPolicyRowStatus": rlRaGuardPortPolicyRowStatus,
       "rlRaGuardPolicyPortTable": rlRaGuardPolicyPortTable,
       "rlRaGuardPolicyPortEntry": rlRaGuardPolicyPortEntry,
       "rlRaGuardPolicyPortName": rlRaGuardPolicyPortName,
       "rlRaGuardPolicyPortIfIndex": rlRaGuardPolicyPortIfIndex,
       "rlRaGuardPolicyPortVlan1to1024": rlRaGuardPolicyPortVlan1to1024,
       "rlRaGuardPolicyPortVlan1025to2048": rlRaGuardPolicyPortVlan1025to2048,
       "rlRaGuardPolicyPortVlan2049to3072": rlRaGuardPolicyPortVlan2049to3072,
       "rlRaGuardPolicyPortVlan3073to4094": rlRaGuardPolicyPortVlan3073to4094,
       "rlRaGuardVlanPolicyTable": rlRaGuardVlanPolicyTable,
       "rlRaGuardVlanPolicyEntry": rlRaGuardVlanPolicyEntry,
       "rlRaGuardVlanPolicyVlanTag": rlRaGuardVlanPolicyVlanTag,
       "rlRaGuardVlanPolicyName": rlRaGuardVlanPolicyName,
       "rlRaGuardVlanPolicyRowStatus": rlRaGuardVlanPolicyRowStatus,
       "rlRaGuardPolicyVlanTable": rlRaGuardPolicyVlanTable,
       "rlRaGuardPolicyVlanEntry": rlRaGuardPolicyVlanEntry,
       "rlRaGuardPolicyVlanPolicyName": rlRaGuardPolicyVlanPolicyName,
       "rlRaGuardPolicyVlan1to1024": rlRaGuardPolicyVlan1to1024,
       "rlRaGuardPolicyVlan1025to2048": rlRaGuardPolicyVlan1025to2048,
       "rlRaGuardPolicyVlan2049to3072": rlRaGuardPolicyVlan2049to3072,
       "rlRaGuardPolicyVlan3073to4094": rlRaGuardPolicyVlan3073to4094,
       "rlRaGuardEnableVlanTable": rlRaGuardEnableVlanTable,
       "rlRaGuardEnableVlanEntry": rlRaGuardEnableVlanEntry,
       "rlRaGuardEnableVlanIndex": rlRaGuardEnableVlanIndex,
       "rlRaGuardEnableVlan1to1024": rlRaGuardEnableVlan1to1024,
       "rlRaGuardEnableVlan1025to2048": rlRaGuardEnableVlan1025to2048,
       "rlRaGuardEnableVlan2049to3072": rlRaGuardEnableVlan2049to3072,
       "rlRaGuardEnableVlan3073to4094": rlRaGuardEnableVlan3073to4094,
       "rlRaGuardActivePolicyTable": rlRaGuardActivePolicyTable,
       "rlRaGuardActivePolicyEntry": rlRaGuardActivePolicyEntry,
       "rlRaGuardActivePolicyIfIndex": rlRaGuardActivePolicyIfIndex,
       "rlRaGuardActivePolicyVlanTag": rlRaGuardActivePolicyVlanTag,
       "rlRaGuardActivePolicyNamePort": rlRaGuardActivePolicyNamePort,
       "rlRaGuardActivePolicyNameVlan": rlRaGuardActivePolicyNameVlan,
       "rlRaGuardActivePolicyDeviceRole": rlRaGuardActivePolicyDeviceRole,
       "rlRaGuardActivePolicyDeviceRoleType": rlRaGuardActivePolicyDeviceRoleType,
       "rlRaGuardActivePolicyHopLimitMin": rlRaGuardActivePolicyHopLimitMin,
       "rlRaGuardActivePolicyHopLimitMinType": rlRaGuardActivePolicyHopLimitMinType,
       "rlRaGuardActivePolicyHopLimitMax": rlRaGuardActivePolicyHopLimitMax,
       "rlRaGuardActivePolicyHopLimitMaxType": rlRaGuardActivePolicyHopLimitMaxType,
       "rlRaGuardActivePolicyManagedConfigFlag": rlRaGuardActivePolicyManagedConfigFlag,
       "rlRaGuardActivePolicyManagedConfigFlagType": rlRaGuardActivePolicyManagedConfigFlagType,
       "rlRaGuardActivePolicyMatchRaAddr": rlRaGuardActivePolicyMatchRaAddr,
       "rlRaGuardActivePolicyMatchRaAddrType": rlRaGuardActivePolicyMatchRaAddrType,
       "rlRaGuardActivePolicyMatchRaPrefixes": rlRaGuardActivePolicyMatchRaPrefixes,
       "rlRaGuardActivePolicyMatchRaPrefixesType": rlRaGuardActivePolicyMatchRaPrefixesType,
       "rlRaGuardActivePolicyOtherConfigFlag": rlRaGuardActivePolicyOtherConfigFlag,
       "rlRaGuardActivePolicyOtherConfigFlagType": rlRaGuardActivePolicyOtherConfigFlagType,
       "rlRaGuardActivePolicyRouterPrefMin": rlRaGuardActivePolicyRouterPrefMin,
       "rlRaGuardActivePolicyRouterPrefMinType": rlRaGuardActivePolicyRouterPrefMinType,
       "rlRaGuardActivePolicyRouterPrefMax": rlRaGuardActivePolicyRouterPrefMax,
       "rlRaGuardActivePolicyRouterPrefMaxType": rlRaGuardActivePolicyRouterPrefMaxType,
       "rlRaGuardHopLimitMin": rlRaGuardHopLimitMin,
       "rlRaGuardHopLimitMax": rlRaGuardHopLimitMax,
       "rlRaGuardManagedConfigFlag": rlRaGuardManagedConfigFlag,
       "rlRaGuardOtherConfigFlag": rlRaGuardOtherConfigFlag,
       "rlRaGuardRouterPrefMin": rlRaGuardRouterPrefMin,
       "rlRaGuardRouterPrefMax": rlRaGuardRouterPrefMax,
       "rlNbrBindingIntegrity": rlNbrBindingIntegrity,
       "rlNbrBindingIntegrityPolicyTable": rlNbrBindingIntegrityPolicyTable,
       "rlNbrBindingIntegrityPolicyEntry": rlNbrBindingIntegrityPolicyEntry,
       "rlNbrBindingIntegrityPolicyName": rlNbrBindingIntegrityPolicyName,
       "rlNbrBindingIntegrityPolicyDeviceRole": rlNbrBindingIntegrityPolicyDeviceRole,
       "rlNbrBindingIntegrityPolicyLogBinding": rlNbrBindingIntegrityPolicyLogBinding,
       "rlNbrBindingIntegrityPolicyMaxEntriesVlanLimit": rlNbrBindingIntegrityPolicyMaxEntriesVlanLimit,
       "rlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit": rlNbrBindingIntegrityPolicyMaxEntriesInterfaceLimit,
       "rlNbrBindingIntegrityPolicyMaxEntriesMacLimit": rlNbrBindingIntegrityPolicyMaxEntriesMacLimit,
       "rlNbrBindingIntegrityPolicyRowStatus": rlNbrBindingIntegrityPolicyRowStatus,
       "rlNbrBindingIntegrityPortPolicyTable": rlNbrBindingIntegrityPortPolicyTable,
       "rlNbrBindingIntegrityPortPolicyEntry": rlNbrBindingIntegrityPortPolicyEntry,
       "rlNbrBindingIntegrityPortPolicyIfIndex": rlNbrBindingIntegrityPortPolicyIfIndex,
       "rlNbrBindingIntegrityPortPolicyName": rlNbrBindingIntegrityPortPolicyName,
       "rlNbrBindingIntegrityPortPolicyVlan1to1024": rlNbrBindingIntegrityPortPolicyVlan1to1024,
       "rlNbrBindingIntegrityPortPolicyVlan1025to2048": rlNbrBindingIntegrityPortPolicyVlan1025to2048,
       "rlNbrBindingIntegrityPortPolicyVlan2049to3072": rlNbrBindingIntegrityPortPolicyVlan2049to3072,
       "rlNbrBindingIntegrityPortPolicyVlan3073to4094": rlNbrBindingIntegrityPortPolicyVlan3073to4094,
       "rlNbrBindingIntegrityPortPolicyRowStatus": rlNbrBindingIntegrityPortPolicyRowStatus,
       "rlNbrBindingIntegrityPolicyPortTable": rlNbrBindingIntegrityPolicyPortTable,
       "rlNbrBindingIntegrityPolicyPortEntry": rlNbrBindingIntegrityPolicyPortEntry,
       "rlNbrBindingIntegrityPolicyPortName": rlNbrBindingIntegrityPolicyPortName,
       "rlNbrBindingIntegrityPolicyPortIfIndex": rlNbrBindingIntegrityPolicyPortIfIndex,
       "rlNbrBindingIntegrityPolicyPortVlan1to1024": rlNbrBindingIntegrityPolicyPortVlan1to1024,
       "rlNbrBindingIntegrityPolicyPortVlan1025to2048": rlNbrBindingIntegrityPolicyPortVlan1025to2048,
       "rlNbrBindingIntegrityPolicyPortVlan2049to3072": rlNbrBindingIntegrityPolicyPortVlan2049to3072,
       "rlNbrBindingIntegrityPolicyPortVlan3073to4094": rlNbrBindingIntegrityPolicyPortVlan3073to4094,
       "rlNbrBindingIntegrityVlanPolicyTable": rlNbrBindingIntegrityVlanPolicyTable,
       "rlNbrBindingIntegrityVlanPolicyEntry": rlNbrBindingIntegrityVlanPolicyEntry,
       "rlNbrBindingIntegrityVlanPolicyVlanTag": rlNbrBindingIntegrityVlanPolicyVlanTag,
       "rlNbrBindingIntegrityVlanPolicyName": rlNbrBindingIntegrityVlanPolicyName,
       "rlNbrBindingIntegrityVlanPolicyRowStatus": rlNbrBindingIntegrityVlanPolicyRowStatus,
       "rlNbrBindingIntegrityPolicyVlanTable": rlNbrBindingIntegrityPolicyVlanTable,
       "rlNbrBindingIntegrityPolicyVlanEntry": rlNbrBindingIntegrityPolicyVlanEntry,
       "rlNbrBindingIntegrityPolicyVlanPolicyName": rlNbrBindingIntegrityPolicyVlanPolicyName,
       "rlNbrBindingIntegrityPolicyVlan1to1024": rlNbrBindingIntegrityPolicyVlan1to1024,
       "rlNbrBindingIntegrityPolicyVlan1025to2048": rlNbrBindingIntegrityPolicyVlan1025to2048,
       "rlNbrBindingIntegrityPolicyVlan2049to3072": rlNbrBindingIntegrityPolicyVlan2049to3072,
       "rlNbrBindingIntegrityPolicyVlan3073to4094": rlNbrBindingIntegrityPolicyVlan3073to4094,
       "rlNbrBindingIntegrityEnableVlanTable": rlNbrBindingIntegrityEnableVlanTable,
       "rlNbrBindingIntegrityEnableVlanEntry": rlNbrBindingIntegrityEnableVlanEntry,
       "rlNbrBindingIntegrityEnableVlanIndex": rlNbrBindingIntegrityEnableVlanIndex,
       "rlNbrBindingIntegrityEnableVlan1to1024": rlNbrBindingIntegrityEnableVlan1to1024,
       "rlNbrBindingIntegrityEnableVlan1025to2048": rlNbrBindingIntegrityEnableVlan1025to2048,
       "rlNbrBindingIntegrityEnableVlan2049to3072": rlNbrBindingIntegrityEnableVlan2049to3072,
       "rlNbrBindingIntegrityEnableVlan3073to4094": rlNbrBindingIntegrityEnableVlan3073to4094,
       "rlNbrBindingIntegrityBindingTable": rlNbrBindingIntegrityBindingTable,
       "rlNbrBindingIntegrityBindingEntry": rlNbrBindingIntegrityBindingEntry,
       "rlNbrBindingIntegrityBindingVlanTag": rlNbrBindingIntegrityBindingVlanTag,
       "rlNbrBindingIntegrityBindingSourceAddressType": rlNbrBindingIntegrityBindingSourceAddressType,
       "rlNbrBindingIntegrityBindingSourceAddress": rlNbrBindingIntegrityBindingSourceAddress,
       "rlNbrBindingIntegrityBindingIfIndex": rlNbrBindingIntegrityBindingIfIndex,
       "rlNbrBindingIntegrityBindingMacAddress": rlNbrBindingIntegrityBindingMacAddress,
       "rlNbrBindingIntegrityBindingOrigin": rlNbrBindingIntegrityBindingOrigin,
       "rlNbrBindingIntegrityBindingState": rlNbrBindingIntegrityBindingState,
       "rlNbrBindingIntegrityBindingExpiryTime": rlNbrBindingIntegrityBindingExpiryTime,
       "rlNbrBindingIntegrityBindingRowStatus": rlNbrBindingIntegrityBindingRowStatus,
       "rlNbrBindingIntegrityClearTable": rlNbrBindingIntegrityClearTable,
       "rlNbrBindingIntegrityClearEntry": rlNbrBindingIntegrityClearEntry,
       "rlNbrBindingIntegrityClearIndex": rlNbrBindingIntegrityClearIndex,
       "rlNbrBindingIntegrityClearVlanTag": rlNbrBindingIntegrityClearVlanTag,
       "rlNbrBindingIntegrityClearSourceAddressType": rlNbrBindingIntegrityClearSourceAddressType,
       "rlNbrBindingIntegrityClearSourceAddress": rlNbrBindingIntegrityClearSourceAddress,
       "rlNbrBindingIntegrityClearIfIndex": rlNbrBindingIntegrityClearIfIndex,
       "rlNbrBindingIntegrityClearMacAddress": rlNbrBindingIntegrityClearMacAddress,
       "rlNbrBindingIntegrityClearRowStatus": rlNbrBindingIntegrityClearRowStatus,
       "rlNbrBindingIntegrityActivePolicyTable": rlNbrBindingIntegrityActivePolicyTable,
       "rlNbrBindingIntegrityActivePolicyEntry": rlNbrBindingIntegrityActivePolicyEntry,
       "rlNbrBindingIntegrityActivePolicyIfIndex": rlNbrBindingIntegrityActivePolicyIfIndex,
       "rlNbrBindingIntegrityActivePolicyVlanTag": rlNbrBindingIntegrityActivePolicyVlanTag,
       "rlNbrBindingIntegrityActivePolicyNamePort": rlNbrBindingIntegrityActivePolicyNamePort,
       "rlNbrBindingIntegrityActivePolicyNameVlan": rlNbrBindingIntegrityActivePolicyNameVlan,
       "rlNbrBindingIntegrityActivePolicyDeviceRole": rlNbrBindingIntegrityActivePolicyDeviceRole,
       "rlNbrBindingIntegrityActivePolicyDeviceRoleType": rlNbrBindingIntegrityActivePolicyDeviceRoleType,
       "rlNbrBindingIntegrityActivePolicyLogBinding": rlNbrBindingIntegrityActivePolicyLogBinding,
       "rlNbrBindingIntegrityActivePolicyLogBindingType": rlNbrBindingIntegrityActivePolicyLogBindingType,
       "rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit": rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimit,
       "rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimitType": rlNbrBindingIntegrityActivePolicyMaxEntriesVlanLimitType,
       "rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit": rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimit,
       "rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimitType": rlNbrBindingIntegrityActivePolicyMaxEntriesInterfaceLimitType,
       "rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit": rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimit,
       "rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimitType": rlNbrBindingIntegrityActivePolicyMaxEntriesMacLimitType,
       "rlNbrBindingIntegrityActivePolicyBindingLifetime": rlNbrBindingIntegrityActivePolicyBindingLifetime,
       "rlNbrBindingIntegrityActivePolicyBindingLifetimeType": rlNbrBindingIntegrityActivePolicyBindingLifetimeType,
       "rlNbrBindingIntegrityBindingLifetime": rlNbrBindingIntegrityBindingLifetime,
       "rlNbrBindingIntegrityLogBinding": rlNbrBindingIntegrityLogBinding,
       "rlNbrBindingIntegrityMaxEntriesVlanLimit": rlNbrBindingIntegrityMaxEntriesVlanLimit,
       "rlNbrBindingIntegrityMaxEntriesInterfaceLimit": rlNbrBindingIntegrityMaxEntriesInterfaceLimit,
       "rlNbrBindingIntegrityMaxEntriesMacLimit": rlNbrBindingIntegrityMaxEntriesMacLimit,
       "rlNbrBindingIntegrityEntriesNum": rlNbrBindingIntegrityEntriesNum,
       "rlDhcpGuard": rlDhcpGuard,
       "rlDhcpGuardPolicyTable": rlDhcpGuardPolicyTable,
       "rlDhcpGuardPolicyEntry": rlDhcpGuardPolicyEntry,
       "rlDhcpGuardPolicyName": rlDhcpGuardPolicyName,
       "rlDhcpGuardPolicyDeviceRole": rlDhcpGuardPolicyDeviceRole,
       "rlDhcpGuardPolicyMatchServerAddrSpecified": rlDhcpGuardPolicyMatchServerAddrSpecified,
       "rlDhcpGuardPolicyMatchServerAddr": rlDhcpGuardPolicyMatchServerAddr,
       "rlDhcpGuardPolicyMatchReplyAddrSpecified": rlDhcpGuardPolicyMatchReplyAddrSpecified,
       "rlDhcpGuardPolicyMatchReplyAddr": rlDhcpGuardPolicyMatchReplyAddr,
       "rlDhcpGuardPolicyPrefMin": rlDhcpGuardPolicyPrefMin,
       "rlDhcpGuardPolicyPrefMax": rlDhcpGuardPolicyPrefMax,
       "rlDhcpGuardPolicyRowStatus": rlDhcpGuardPolicyRowStatus,
       "rlDhcpGuardPortPolicyTable": rlDhcpGuardPortPolicyTable,
       "rlDhcpGuardPortPolicyEntry": rlDhcpGuardPortPolicyEntry,
       "rlDhcpGuardPortPolicyIfIndex": rlDhcpGuardPortPolicyIfIndex,
       "rlDhcpGuardPortPolicyName": rlDhcpGuardPortPolicyName,
       "rlDhcpGuardPortPolicyVlan1to1024": rlDhcpGuardPortPolicyVlan1to1024,
       "rlDhcpGuardPortPolicyVlan1025to2048": rlDhcpGuardPortPolicyVlan1025to2048,
       "rlDhcpGuardPortPolicyVlan2049to3072": rlDhcpGuardPortPolicyVlan2049to3072,
       "rlDhcpGuardPortPolicyVlan3073to4094": rlDhcpGuardPortPolicyVlan3073to4094,
       "rlDhcpGuardPortPolicyRowStatus": rlDhcpGuardPortPolicyRowStatus,
       "rlDhcpGuardPolicyPortTable": rlDhcpGuardPolicyPortTable,
       "rlDhcpGuardPolicyPortEntry": rlDhcpGuardPolicyPortEntry,
       "rlDhcpGuardPolicyPortName": rlDhcpGuardPolicyPortName,
       "rlDhcpGuardPolicyPortIfIndex": rlDhcpGuardPolicyPortIfIndex,
       "rlDhcpGuardPolicyPortVlan1to1024": rlDhcpGuardPolicyPortVlan1to1024,
       "rlDhcpGuardPolicyPortVlan1025to2048": rlDhcpGuardPolicyPortVlan1025to2048,
       "rlDhcpGuardPolicyPortVlan2049to3072": rlDhcpGuardPolicyPortVlan2049to3072,
       "rlDhcpGuardPolicyPortVlan3073to4094": rlDhcpGuardPolicyPortVlan3073to4094,
       "rlDhcpGuardVlanPolicyTable": rlDhcpGuardVlanPolicyTable,
       "rlDhcpGuardVlanPolicyEntry": rlDhcpGuardVlanPolicyEntry,
       "rlDhcpGuardVlanPolicyVlanTag": rlDhcpGuardVlanPolicyVlanTag,
       "rlDhcpGuardVlanPolicyName": rlDhcpGuardVlanPolicyName,
       "rlDhcpGuardVlanPolicyRowStatus": rlDhcpGuardVlanPolicyRowStatus,
       "rlDhcpGuardPolicyVlanTable": rlDhcpGuardPolicyVlanTable,
       "rlDhcpGuardPolicyVlanEntry": rlDhcpGuardPolicyVlanEntry,
       "rlDhcpGuardPolicyVlanPolicyName": rlDhcpGuardPolicyVlanPolicyName,
       "rlDhcpGuardPolicyVlan1to1024": rlDhcpGuardPolicyVlan1to1024,
       "rlDhcpGuardPolicyVlan1025to2048": rlDhcpGuardPolicyVlan1025to2048,
       "rlDhcpGuardPolicyVlan2049to3072": rlDhcpGuardPolicyVlan2049to3072,
       "rlDhcpGuardPolicyVlan3073to4094": rlDhcpGuardPolicyVlan3073to4094,
       "rlDhcpGuardEnableVlanTable": rlDhcpGuardEnableVlanTable,
       "rlDhcpGuardEnableVlanEntry": rlDhcpGuardEnableVlanEntry,
       "rlDhcpGuardEnableVlanIndex": rlDhcpGuardEnableVlanIndex,
       "rlDhcpGuardEnableVlan1to1024": rlDhcpGuardEnableVlan1to1024,
       "rlDhcpGuardEnableVlan1025to2048": rlDhcpGuardEnableVlan1025to2048,
       "rlDhcpGuardEnableVlan2049to3072": rlDhcpGuardEnableVlan2049to3072,
       "rlDhcpGuardEnableVlan3073to4094": rlDhcpGuardEnableVlan3073to4094,
       "rlDhcpGuardActivePolicyTable": rlDhcpGuardActivePolicyTable,
       "rlDhcpGuardActivePolicyEntry": rlDhcpGuardActivePolicyEntry,
       "rlDhcpGuardActivePolicyIfIndex": rlDhcpGuardActivePolicyIfIndex,
       "rlDhcpGuardActivePolicyVlanTag": rlDhcpGuardActivePolicyVlanTag,
       "rlDhcpGuardActivePolicyNamePort": rlDhcpGuardActivePolicyNamePort,
       "rlDhcpGuardActivePolicyNameVlan": rlDhcpGuardActivePolicyNameVlan,
       "rlDhcpGuardActivePolicyDeviceRole": rlDhcpGuardActivePolicyDeviceRole,
       "rlDhcpGuardActivePolicyDeviceRoleType": rlDhcpGuardActivePolicyDeviceRoleType,
       "rlDhcpGuardActivePolicyMatchServerAddr": rlDhcpGuardActivePolicyMatchServerAddr,
       "rlDhcpGuardActivePolicyMatchServerAddrType": rlDhcpGuardActivePolicyMatchServerAddrType,
       "rlDhcpGuardActivePolicyMatchReplyAddr": rlDhcpGuardActivePolicyMatchReplyAddr,
       "rlDhcpGuardActivePolicyMatchReplyAddrType": rlDhcpGuardActivePolicyMatchReplyAddrType,
       "rlDhcpGuardActivePolicyPrefMin": rlDhcpGuardActivePolicyPrefMin,
       "rlDhcpGuardActivePolicyPrefMinType": rlDhcpGuardActivePolicyPrefMinType,
       "rlDhcpGuardActivePolicyPrefMax": rlDhcpGuardActivePolicyPrefMax,
       "rlDhcpGuardActivePolicyPrefMaxType": rlDhcpGuardActivePolicyPrefMaxType,
       "rlDhcpGuardPrefMin": rlDhcpGuardPrefMin,
       "rlDhcpGuardPrefMax": rlDhcpGuardPrefMax}
)
