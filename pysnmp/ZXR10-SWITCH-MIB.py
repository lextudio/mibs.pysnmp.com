# SNMP MIB module (ZXR10-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:08 2024
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
 enterprises,
 experimental,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "mgmt")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10switch_ObjectIdentity = ObjectIdentity
zxr10switch = _Zxr10switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102)
)
_Zxr10vlan_ObjectIdentity = ObjectIdentity
zxr10vlan = _Zxr10vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1)
)
_Zxr10CpuVlanPvidTable_Object = MibTable
zxr10CpuVlanPvidTable = _Zxr10CpuVlanPvidTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1)
)
if mibBuilder.loadTexts:
    zxr10CpuVlanPvidTable.setStatus("current")
_Zxr10CpuVlanPvidEntry_Object = MibTableRow
zxr10CpuVlanPvidEntry = _Zxr10CpuVlanPvidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1)
)
zxr10CpuVlanPvidEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10CpuVlanId"),
)
if mibBuilder.loadTexts:
    zxr10CpuVlanPvidEntry.setStatus("current")
_Zxr10CpuVlanId_Type = Integer32
_Zxr10CpuVlanId_Object = MibTableColumn
zxr10CpuVlanId = _Zxr10CpuVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1, 1),
    _Zxr10CpuVlanId_Type()
)
zxr10CpuVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10CpuVlanId.setStatus("current")
_Zxr10CpuVlanIf_Type = Integer32
_Zxr10CpuVlanIf_Object = MibTableColumn
zxr10CpuVlanIf = _Zxr10CpuVlanIf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1, 2),
    _Zxr10CpuVlanIf_Type()
)
zxr10CpuVlanIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10CpuVlanIf.setStatus("current")


class _Zxr10CpuVlanMtu_Type(Integer32):
    """Custom type zxr10CpuVlanMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Zxr10CpuVlanMtu_Type.__name__ = "Integer32"
_Zxr10CpuVlanMtu_Object = MibTableColumn
zxr10CpuVlanMtu = _Zxr10CpuVlanMtu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1, 3),
    _Zxr10CpuVlanMtu_Type()
)
zxr10CpuVlanMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10CpuVlanMtu.setStatus("current")


class _Zxr10CpuVlanState_Type(Integer32):
    """Custom type zxr10CpuVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_Zxr10CpuVlanState_Type.__name__ = "Integer32"
_Zxr10CpuVlanState_Object = MibTableColumn
zxr10CpuVlanState = _Zxr10CpuVlanState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1, 4),
    _Zxr10CpuVlanState_Type()
)
zxr10CpuVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10CpuVlanState.setStatus("current")
_Zxr10CpuVlanSaid_Type = Integer32
_Zxr10CpuVlanSaid_Object = MibTableColumn
zxr10CpuVlanSaid = _Zxr10CpuVlanSaid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1, 5),
    _Zxr10CpuVlanSaid_Type()
)
zxr10CpuVlanSaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10CpuVlanSaid.setStatus("current")
_Zxr10CpuVlanVpnid_Type = Integer32
_Zxr10CpuVlanVpnid_Object = MibTableColumn
zxr10CpuVlanVpnid = _Zxr10CpuVlanVpnid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1, 6),
    _Zxr10CpuVlanVpnid_Type()
)
zxr10CpuVlanVpnid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10CpuVlanVpnid.setStatus("current")
_Zxr10CpuVlanRowStatus_Type = RowStatus
_Zxr10CpuVlanRowStatus_Object = MibTableColumn
zxr10CpuVlanRowStatus = _Zxr10CpuVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1, 7),
    _Zxr10CpuVlanRowStatus_Type()
)
zxr10CpuVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxr10CpuVlanRowStatus.setStatus("current")
_Zxr10CpuVlanName_Type = DisplayString
_Zxr10CpuVlanName_Object = MibTableColumn
zxr10CpuVlanName = _Zxr10CpuVlanName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1, 8),
    _Zxr10CpuVlanName_Type()
)
zxr10CpuVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10CpuVlanName.setStatus("current")
_Zxr10CpuVlanMemPortsPvid_Type = DisplayString
_Zxr10CpuVlanMemPortsPvid_Object = MibTableColumn
zxr10CpuVlanMemPortsPvid = _Zxr10CpuVlanMemPortsPvid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 1, 1, 9),
    _Zxr10CpuVlanMemPortsPvid_Type()
)
zxr10CpuVlanMemPortsPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10CpuVlanMemPortsPvid.setStatus("current")
_Zxr10CpuVlanTagTable_Object = MibTable
zxr10CpuVlanTagTable = _Zxr10CpuVlanTagTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 2)
)
if mibBuilder.loadTexts:
    zxr10CpuVlanTagTable.setStatus("current")
_Zxr10CpuVlanTagEntry_Object = MibTableRow
zxr10CpuVlanTagEntry = _Zxr10CpuVlanTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 2, 1)
)
zxr10CpuVlanTagEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10CpuVlanId"),
)
if mibBuilder.loadTexts:
    zxr10CpuVlanTagEntry.setStatus("current")
_Zxr10CpuVlanid_Type = Integer32
_Zxr10CpuVlanid_Object = MibTableColumn
zxr10CpuVlanid = _Zxr10CpuVlanid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 2, 1, 1),
    _Zxr10CpuVlanid_Type()
)
zxr10CpuVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10CpuVlanid.setStatus("current")
_Zxr10CpuVlanvpnid_Type = Integer32
_Zxr10CpuVlanvpnid_Object = MibTableColumn
zxr10CpuVlanvpnid = _Zxr10CpuVlanvpnid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 2, 1, 2),
    _Zxr10CpuVlanvpnid_Type()
)
zxr10CpuVlanvpnid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10CpuVlanvpnid.setStatus("current")
_Zxr10CpuVlanname_Type = DisplayString
_Zxr10CpuVlanname_Object = MibTableColumn
zxr10CpuVlanname = _Zxr10CpuVlanname_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 2, 1, 3),
    _Zxr10CpuVlanname_Type()
)
zxr10CpuVlanname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10CpuVlanname.setStatus("current")
_Zxr10CpuVlanMemPortsTag_Type = DisplayString
_Zxr10CpuVlanMemPortsTag_Object = MibTableColumn
zxr10CpuVlanMemPortsTag = _Zxr10CpuVlanMemPortsTag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 2, 1, 4),
    _Zxr10CpuVlanMemPortsTag_Type()
)
zxr10CpuVlanMemPortsTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10CpuVlanMemPortsTag.setStatus("current")
_Zxr10QinQ_ObjectIdentity = ObjectIdentity
zxr10QinQ = _Zxr10QinQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 3)
)
_Zxr10QinQTable_Object = MibTable
zxr10QinQTable = _Zxr10QinQTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zxr10QinQTable.setStatus("current")
_Zxr10QinQEntry_Object = MibTableRow
zxr10QinQEntry = _Zxr10QinQEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 3, 1, 1)
)
zxr10QinQEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10QinQEntry.setStatus("current")
_Zxr10QinQPortName_Type = DisplayString
_Zxr10QinQPortName_Object = MibTableColumn
zxr10QinQPortName = _Zxr10QinQPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 3, 1, 1, 1),
    _Zxr10QinQPortName_Type()
)
zxr10QinQPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10QinQPortName.setStatus("current")


class _Zxr10QinQMode_Type(Integer32):
    """Custom type zxr10QinQMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customer", 1),
          ("normal", 0),
          ("uplink", 2))
    )


_Zxr10QinQMode_Type.__name__ = "Integer32"
_Zxr10QinQMode_Object = MibTableColumn
zxr10QinQMode = _Zxr10QinQMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 3, 1, 1, 2),
    _Zxr10QinQMode_Type()
)
zxr10QinQMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10QinQMode.setStatus("current")
_Zxr10QinQTpid_Type = Integer32
_Zxr10QinQTpid_Object = MibTableColumn
zxr10QinQTpid = _Zxr10QinQTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 3, 1, 1, 3),
    _Zxr10QinQTpid_Type()
)
zxr10QinQTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10QinQTpid.setStatus("current")
_Zxr10QinQPvid_Type = Integer32
_Zxr10QinQPvid_Object = MibTableColumn
zxr10QinQPvid = _Zxr10QinQPvid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 3, 1, 1, 4),
    _Zxr10QinQPvid_Type()
)
zxr10QinQPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10QinQPvid.setStatus("current")
_Zxr10QinQExtendTpid_Type = Integer32
_Zxr10QinQExtendTpid_Object = MibScalar
zxr10QinQExtendTpid = _Zxr10QinQExtendTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 3, 2),
    _Zxr10QinQExtendTpid_Type()
)
zxr10QinQExtendTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10QinQExtendTpid.setStatus("current")
_Zxr10QinQStandardTpid_Type = Integer32
_Zxr10QinQStandardTpid_Object = MibScalar
zxr10QinQStandardTpid = _Zxr10QinQStandardTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 3, 3),
    _Zxr10QinQStandardTpid_Type()
)
zxr10QinQStandardTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10QinQStandardTpid.setStatus("current")
_Zxr10MemberShip_ObjectIdentity = ObjectIdentity
zxr10MemberShip = _Zxr10MemberShip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4)
)
_Zxr10MemberShipTable_Object = MibTable
zxr10MemberShipTable = _Zxr10MemberShipTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1)
)
if mibBuilder.loadTexts:
    zxr10MemberShipTable.setStatus("current")
_Zxr10MemberShipEntry_Object = MibTableRow
zxr10MemberShipEntry = _Zxr10MemberShipEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1)
)
zxr10MemberShipEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10MemberShipEntry.setStatus("current")
_Zxr10MemberShipPortName_Type = DisplayString
_Zxr10MemberShipPortName_Object = MibTableColumn
zxr10MemberShipPortName = _Zxr10MemberShipPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 1),
    _Zxr10MemberShipPortName_Type()
)
zxr10MemberShipPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10MemberShipPortName.setStatus("current")
_Zxr10MemberShipPvid_Type = Integer32
_Zxr10MemberShipPvid_Object = MibTableColumn
zxr10MemberShipPvid = _Zxr10MemberShipPvid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 2),
    _Zxr10MemberShipPvid_Type()
)
zxr10MemberShipPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipPvid.setStatus("current")


class _Zxr10MemberShipMode_Type(Integer32):
    """Custom type zxr10MemberShipMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("hybrid", 2),
          ("trunk", 1))
    )


_Zxr10MemberShipMode_Type.__name__ = "Integer32"
_Zxr10MemberShipMode_Object = MibTableColumn
zxr10MemberShipMode = _Zxr10MemberShipMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 3),
    _Zxr10MemberShipMode_Type()
)
zxr10MemberShipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipMode.setStatus("current")


class _Zxr10MemberShipVlansTag_Type(OctetString):
    """Custom type zxr10MemberShipVlansTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Zxr10MemberShipVlansTag_Type.__name__ = "OctetString"
_Zxr10MemberShipVlansTag_Object = MibTableColumn
zxr10MemberShipVlansTag = _Zxr10MemberShipVlansTag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 4),
    _Zxr10MemberShipVlansTag_Type()
)
zxr10MemberShipVlansTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipVlansTag.setStatus("current")


class _Zxr10MemberShipVlansHybridUnTag_Type(OctetString):
    """Custom type zxr10MemberShipVlansHybridUnTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Zxr10MemberShipVlansHybridUnTag_Type.__name__ = "OctetString"
_Zxr10MemberShipVlansHybridUnTag_Object = MibTableColumn
zxr10MemberShipVlansHybridUnTag = _Zxr10MemberShipVlansHybridUnTag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 5),
    _Zxr10MemberShipVlansHybridUnTag_Type()
)
zxr10MemberShipVlansHybridUnTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipVlansHybridUnTag.setStatus("current")


class _Zxr10MemberShipVlansTag2k_Type(OctetString):
    """Custom type zxr10MemberShipVlansTag2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Zxr10MemberShipVlansTag2k_Type.__name__ = "OctetString"
_Zxr10MemberShipVlansTag2k_Object = MibTableColumn
zxr10MemberShipVlansTag2k = _Zxr10MemberShipVlansTag2k_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 6),
    _Zxr10MemberShipVlansTag2k_Type()
)
zxr10MemberShipVlansTag2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipVlansTag2k.setStatus("current")


class _Zxr10MemberShipVlansHybridUnTag2k_Type(OctetString):
    """Custom type zxr10MemberShipVlansHybridUnTag2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Zxr10MemberShipVlansHybridUnTag2k_Type.__name__ = "OctetString"
_Zxr10MemberShipVlansHybridUnTag2k_Object = MibTableColumn
zxr10MemberShipVlansHybridUnTag2k = _Zxr10MemberShipVlansHybridUnTag2k_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 7),
    _Zxr10MemberShipVlansHybridUnTag2k_Type()
)
zxr10MemberShipVlansHybridUnTag2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipVlansHybridUnTag2k.setStatus("current")


class _Zxr10MemberShipVlansTag3k_Type(OctetString):
    """Custom type zxr10MemberShipVlansTag3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Zxr10MemberShipVlansTag3k_Type.__name__ = "OctetString"
_Zxr10MemberShipVlansTag3k_Object = MibTableColumn
zxr10MemberShipVlansTag3k = _Zxr10MemberShipVlansTag3k_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 8),
    _Zxr10MemberShipVlansTag3k_Type()
)
zxr10MemberShipVlansTag3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipVlansTag3k.setStatus("current")


class _Zxr10MemberShipVlansHybridUnTag3k_Type(OctetString):
    """Custom type zxr10MemberShipVlansHybridUnTag3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Zxr10MemberShipVlansHybridUnTag3k_Type.__name__ = "OctetString"
_Zxr10MemberShipVlansHybridUnTag3k_Object = MibTableColumn
zxr10MemberShipVlansHybridUnTag3k = _Zxr10MemberShipVlansHybridUnTag3k_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 9),
    _Zxr10MemberShipVlansHybridUnTag3k_Type()
)
zxr10MemberShipVlansHybridUnTag3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipVlansHybridUnTag3k.setStatus("current")


class _Zxr10MemberShipVlansTag4k_Type(OctetString):
    """Custom type zxr10MemberShipVlansTag4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Zxr10MemberShipVlansTag4k_Type.__name__ = "OctetString"
_Zxr10MemberShipVlansTag4k_Object = MibTableColumn
zxr10MemberShipVlansTag4k = _Zxr10MemberShipVlansTag4k_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 10),
    _Zxr10MemberShipVlansTag4k_Type()
)
zxr10MemberShipVlansTag4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipVlansTag4k.setStatus("current")


class _Zxr10MemberShipVlansHybridUnTag4k_Type(OctetString):
    """Custom type zxr10MemberShipVlansHybridUnTag4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Zxr10MemberShipVlansHybridUnTag4k_Type.__name__ = "OctetString"
_Zxr10MemberShipVlansHybridUnTag4k_Object = MibTableColumn
zxr10MemberShipVlansHybridUnTag4k = _Zxr10MemberShipVlansHybridUnTag4k_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 4, 1, 1, 11),
    _Zxr10MemberShipVlansHybridUnTag4k_Type()
)
zxr10MemberShipVlansHybridUnTag4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10MemberShipVlansHybridUnTag4k.setStatus("current")
_Zxr10CpuVlanUntagTable_Object = MibTable
zxr10CpuVlanUntagTable = _Zxr10CpuVlanUntagTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 5)
)
if mibBuilder.loadTexts:
    zxr10CpuVlanUntagTable.setStatus("current")
_Zxr10CpuVlanUntagEntry_Object = MibTableRow
zxr10CpuVlanUntagEntry = _Zxr10CpuVlanUntagEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 5, 1)
)
zxr10CpuVlanUntagEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10CpuVlanId"),
)
if mibBuilder.loadTexts:
    zxr10CpuVlanUntagEntry.setStatus("current")
_Zxr10Cpuvlanid_Type = Integer32
_Zxr10Cpuvlanid_Object = MibTableColumn
zxr10Cpuvlanid = _Zxr10Cpuvlanid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 5, 1, 1),
    _Zxr10Cpuvlanid_Type()
)
zxr10Cpuvlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10Cpuvlanid.setStatus("current")
_Zxr10CpuVlanvpnId_Type = Integer32
_Zxr10CpuVlanvpnId_Object = MibTableColumn
zxr10CpuVlanvpnId = _Zxr10CpuVlanvpnId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 5, 1, 2),
    _Zxr10CpuVlanvpnId_Type()
)
zxr10CpuVlanvpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10CpuVlanvpnId.setStatus("current")
_Zxr10Cpuvlanname_Type = DisplayString
_Zxr10Cpuvlanname_Object = MibTableColumn
zxr10Cpuvlanname = _Zxr10Cpuvlanname_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 5, 1, 3),
    _Zxr10Cpuvlanname_Type()
)
zxr10Cpuvlanname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10Cpuvlanname.setStatus("current")
_Zxr10CpuVlanMemPortsUntag_Type = DisplayString
_Zxr10CpuVlanMemPortsUntag_Object = MibTableColumn
zxr10CpuVlanMemPortsUntag = _Zxr10CpuVlanMemPortsUntag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 1, 5, 1, 4),
    _Zxr10CpuVlanMemPortsUntag_Type()
)
zxr10CpuVlanMemPortsUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10CpuVlanMemPortsUntag.setStatus("current")
_Zxr10igmpSnooping_ObjectIdentity = ObjectIdentity
zxr10igmpSnooping = _Zxr10igmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5)
)
_Zxr10IgmpSnoopingTable_Object = MibTable
zxr10IgmpSnoopingTable = _Zxr10IgmpSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1)
)
if mibBuilder.loadTexts:
    zxr10IgmpSnoopingTable.setStatus("current")
_Zxr10IgmpSnoopingEntry_Object = MibTableRow
zxr10IgmpSnoopingEntry = _Zxr10IgmpSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1)
)
zxr10IgmpSnoopingEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10igmpSnoopingGroupId"),
)
if mibBuilder.loadTexts:
    zxr10IgmpSnoopingEntry.setStatus("current")


class _Zxr10igmpSnoopingValid_Type(Integer32):
    """Custom type zxr10igmpSnoopingValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_Zxr10igmpSnoopingValid_Type.__name__ = "Integer32"
_Zxr10igmpSnoopingValid_Object = MibTableColumn
zxr10igmpSnoopingValid = _Zxr10igmpSnoopingValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 1),
    _Zxr10igmpSnoopingValid_Type()
)
zxr10igmpSnoopingValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingValid.setStatus("current")
_Zxr10igmpSnoopingVlanId_Type = Integer32
_Zxr10igmpSnoopingVlanId_Object = MibTableColumn
zxr10igmpSnoopingVlanId = _Zxr10igmpSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 2),
    _Zxr10igmpSnoopingVlanId_Type()
)
zxr10igmpSnoopingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingVlanId.setStatus("current")
_Zxr10igmpSnoopingGroupId_Type = Integer32
_Zxr10igmpSnoopingGroupId_Object = MibTableColumn
zxr10igmpSnoopingGroupId = _Zxr10igmpSnoopingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 3),
    _Zxr10igmpSnoopingGroupId_Type()
)
zxr10igmpSnoopingGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingGroupId.setStatus("current")


class _Zxr10igmpSnoopingDropEnable_Type(Integer32):
    """Custom type zxr10igmpSnoopingDropEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_Zxr10igmpSnoopingDropEnable_Type.__name__ = "Integer32"
_Zxr10igmpSnoopingDropEnable_Object = MibTableColumn
zxr10igmpSnoopingDropEnable = _Zxr10igmpSnoopingDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 4),
    _Zxr10igmpSnoopingDropEnable_Type()
)
zxr10igmpSnoopingDropEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingDropEnable.setStatus("current")
_Zxr10igmpSnoopingMaxHostNum_Type = Integer32
_Zxr10igmpSnoopingMaxHostNum_Object = MibTableColumn
zxr10igmpSnoopingMaxHostNum = _Zxr10igmpSnoopingMaxHostNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 5),
    _Zxr10igmpSnoopingMaxHostNum_Type()
)
zxr10igmpSnoopingMaxHostNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMaxHostNum.setStatus("current")
_Zxr10igmpSnoopingIpAddr_Type = IpAddress
_Zxr10igmpSnoopingIpAddr_Object = MibTableColumn
zxr10igmpSnoopingIpAddr = _Zxr10igmpSnoopingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 6),
    _Zxr10igmpSnoopingIpAddr_Type()
)
zxr10igmpSnoopingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingIpAddr.setStatus("current")
_Zxr10igmpSnoopingGroupMac_Type = MacAddress
_Zxr10igmpSnoopingGroupMac_Object = MibTableColumn
zxr10igmpSnoopingGroupMac = _Zxr10igmpSnoopingGroupMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 7),
    _Zxr10igmpSnoopingGroupMac_Type()
)
zxr10igmpSnoopingGroupMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingGroupMac.setStatus("current")


class _Zxr10igmpSnoopingMemPorts0_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts0_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts0_Object = MibTableColumn
zxr10igmpSnoopingMemPorts0 = _Zxr10igmpSnoopingMemPorts0_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 8),
    _Zxr10igmpSnoopingMemPorts0_Type()
)
zxr10igmpSnoopingMemPorts0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts0.setStatus("current")


class _Zxr10igmpSnoopingMemPorts1_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts1_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts1_Object = MibTableColumn
zxr10igmpSnoopingMemPorts1 = _Zxr10igmpSnoopingMemPorts1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 9),
    _Zxr10igmpSnoopingMemPorts1_Type()
)
zxr10igmpSnoopingMemPorts1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts1.setStatus("current")


class _Zxr10igmpSnoopingMemPorts2_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts2_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts2_Object = MibTableColumn
zxr10igmpSnoopingMemPorts2 = _Zxr10igmpSnoopingMemPorts2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 10),
    _Zxr10igmpSnoopingMemPorts2_Type()
)
zxr10igmpSnoopingMemPorts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts2.setStatus("current")


class _Zxr10igmpSnoopingMemPorts3_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts3_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts3_Object = MibTableColumn
zxr10igmpSnoopingMemPorts3 = _Zxr10igmpSnoopingMemPorts3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 11),
    _Zxr10igmpSnoopingMemPorts3_Type()
)
zxr10igmpSnoopingMemPorts3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts3.setStatus("current")


class _Zxr10igmpSnoopingMemPorts4_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts4_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts4_Object = MibTableColumn
zxr10igmpSnoopingMemPorts4 = _Zxr10igmpSnoopingMemPorts4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 12),
    _Zxr10igmpSnoopingMemPorts4_Type()
)
zxr10igmpSnoopingMemPorts4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts4.setStatus("current")


class _Zxr10igmpSnoopingMemPorts5_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts5_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts5_Object = MibTableColumn
zxr10igmpSnoopingMemPorts5 = _Zxr10igmpSnoopingMemPorts5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 13),
    _Zxr10igmpSnoopingMemPorts5_Type()
)
zxr10igmpSnoopingMemPorts5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts5.setStatus("current")


class _Zxr10igmpSnoopingMemPorts6_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts6_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts6_Object = MibTableColumn
zxr10igmpSnoopingMemPorts6 = _Zxr10igmpSnoopingMemPorts6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 14),
    _Zxr10igmpSnoopingMemPorts6_Type()
)
zxr10igmpSnoopingMemPorts6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts6.setStatus("current")


class _Zxr10igmpSnoopingMemPorts7_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts7_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts7_Object = MibTableColumn
zxr10igmpSnoopingMemPorts7 = _Zxr10igmpSnoopingMemPorts7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 15),
    _Zxr10igmpSnoopingMemPorts7_Type()
)
zxr10igmpSnoopingMemPorts7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts7.setStatus("current")


class _Zxr10igmpSnoopingMemPorts8_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts8_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts8_Object = MibTableColumn
zxr10igmpSnoopingMemPorts8 = _Zxr10igmpSnoopingMemPorts8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 16),
    _Zxr10igmpSnoopingMemPorts8_Type()
)
zxr10igmpSnoopingMemPorts8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts8.setStatus("current")


class _Zxr10igmpSnoopingMemPorts9_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts9 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts9_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts9_Object = MibTableColumn
zxr10igmpSnoopingMemPorts9 = _Zxr10igmpSnoopingMemPorts9_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 17),
    _Zxr10igmpSnoopingMemPorts9_Type()
)
zxr10igmpSnoopingMemPorts9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts9.setStatus("current")


class _Zxr10igmpSnoopingMemPorts10_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts10 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts10_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts10_Object = MibTableColumn
zxr10igmpSnoopingMemPorts10 = _Zxr10igmpSnoopingMemPorts10_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 18),
    _Zxr10igmpSnoopingMemPorts10_Type()
)
zxr10igmpSnoopingMemPorts10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts10.setStatus("current")


class _Zxr10igmpSnoopingMemPorts11_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts11 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts11_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts11_Object = MibTableColumn
zxr10igmpSnoopingMemPorts11 = _Zxr10igmpSnoopingMemPorts11_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 19),
    _Zxr10igmpSnoopingMemPorts11_Type()
)
zxr10igmpSnoopingMemPorts11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts11.setStatus("current")


class _Zxr10igmpSnoopingMemPorts12_Type(OctetString):
    """Custom type zxr10igmpSnoopingMemPorts12 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10igmpSnoopingMemPorts12_Type.__name__ = "OctetString"
_Zxr10igmpSnoopingMemPorts12_Object = MibTableColumn
zxr10igmpSnoopingMemPorts12 = _Zxr10igmpSnoopingMemPorts12_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 20),
    _Zxr10igmpSnoopingMemPorts12_Type()
)
zxr10igmpSnoopingMemPorts12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMemPorts12.setStatus("current")


class _Zxr10pimSnoopingMemPorts0_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts0_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts0_Object = MibTableColumn
zxr10pimSnoopingMemPorts0 = _Zxr10pimSnoopingMemPorts0_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 31),
    _Zxr10pimSnoopingMemPorts0_Type()
)
zxr10pimSnoopingMemPorts0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts0.setStatus("current")


class _Zxr10pimSnoopingMemPorts1_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts1_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts1_Object = MibTableColumn
zxr10pimSnoopingMemPorts1 = _Zxr10pimSnoopingMemPorts1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 32),
    _Zxr10pimSnoopingMemPorts1_Type()
)
zxr10pimSnoopingMemPorts1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts1.setStatus("current")


class _Zxr10pimSnoopingMemPorts2_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts2_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts2_Object = MibTableColumn
zxr10pimSnoopingMemPorts2 = _Zxr10pimSnoopingMemPorts2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 33),
    _Zxr10pimSnoopingMemPorts2_Type()
)
zxr10pimSnoopingMemPorts2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts2.setStatus("current")


class _Zxr10pimSnoopingMemPorts3_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts3_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts3_Object = MibTableColumn
zxr10pimSnoopingMemPorts3 = _Zxr10pimSnoopingMemPorts3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 34),
    _Zxr10pimSnoopingMemPorts3_Type()
)
zxr10pimSnoopingMemPorts3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts3.setStatus("current")


class _Zxr10pimSnoopingMemPorts4_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts4_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts4_Object = MibTableColumn
zxr10pimSnoopingMemPorts4 = _Zxr10pimSnoopingMemPorts4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 35),
    _Zxr10pimSnoopingMemPorts4_Type()
)
zxr10pimSnoopingMemPorts4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts4.setStatus("current")


class _Zxr10pimSnoopingMemPorts5_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts5_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts5_Object = MibTableColumn
zxr10pimSnoopingMemPorts5 = _Zxr10pimSnoopingMemPorts5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 36),
    _Zxr10pimSnoopingMemPorts5_Type()
)
zxr10pimSnoopingMemPorts5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts5.setStatus("current")


class _Zxr10pimSnoopingMemPorts6_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts6_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts6_Object = MibTableColumn
zxr10pimSnoopingMemPorts6 = _Zxr10pimSnoopingMemPorts6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 37),
    _Zxr10pimSnoopingMemPorts6_Type()
)
zxr10pimSnoopingMemPorts6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts6.setStatus("current")


class _Zxr10pimSnoopingMemPorts7_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts7_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts7_Object = MibTableColumn
zxr10pimSnoopingMemPorts7 = _Zxr10pimSnoopingMemPorts7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 38),
    _Zxr10pimSnoopingMemPorts7_Type()
)
zxr10pimSnoopingMemPorts7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts7.setStatus("current")


class _Zxr10pimSnoopingMemPorts8_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts8_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts8_Object = MibTableColumn
zxr10pimSnoopingMemPorts8 = _Zxr10pimSnoopingMemPorts8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 39),
    _Zxr10pimSnoopingMemPorts8_Type()
)
zxr10pimSnoopingMemPorts8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts8.setStatus("current")


class _Zxr10pimSnoopingMemPorts9_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts9 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts9_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts9_Object = MibTableColumn
zxr10pimSnoopingMemPorts9 = _Zxr10pimSnoopingMemPorts9_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 40),
    _Zxr10pimSnoopingMemPorts9_Type()
)
zxr10pimSnoopingMemPorts9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts9.setStatus("current")


class _Zxr10pimSnoopingMemPorts10_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts10 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts10_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts10_Object = MibTableColumn
zxr10pimSnoopingMemPorts10 = _Zxr10pimSnoopingMemPorts10_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 41),
    _Zxr10pimSnoopingMemPorts10_Type()
)
zxr10pimSnoopingMemPorts10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts10.setStatus("current")


class _Zxr10pimSnoopingMemPorts11_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts11 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts11_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts11_Object = MibTableColumn
zxr10pimSnoopingMemPorts11 = _Zxr10pimSnoopingMemPorts11_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 42),
    _Zxr10pimSnoopingMemPorts11_Type()
)
zxr10pimSnoopingMemPorts11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts11.setStatus("current")


class _Zxr10pimSnoopingMemPorts12_Type(OctetString):
    """Custom type zxr10pimSnoopingMemPorts12 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Zxr10pimSnoopingMemPorts12_Type.__name__ = "OctetString"
_Zxr10pimSnoopingMemPorts12_Object = MibTableColumn
zxr10pimSnoopingMemPorts12 = _Zxr10pimSnoopingMemPorts12_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 1, 1, 43),
    _Zxr10pimSnoopingMemPorts12_Type()
)
zxr10pimSnoopingMemPorts12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingMemPorts12.setStatus("current")
_Zxr10PimSnoopingNeighborTable_Object = MibTable
zxr10PimSnoopingNeighborTable = _Zxr10PimSnoopingNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 2)
)
if mibBuilder.loadTexts:
    zxr10PimSnoopingNeighborTable.setStatus("current")
_Zxr10PimSnoopingNeighborEntry_Object = MibTableRow
zxr10PimSnoopingNeighborEntry = _Zxr10PimSnoopingNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 2, 1)
)
zxr10PimSnoopingNeighborEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10pimSnoopingNeighborId"),
)
if mibBuilder.loadTexts:
    zxr10PimSnoopingNeighborEntry.setStatus("current")


class _Zxr10pimSnoopingNeighborValid_Type(Integer32):
    """Custom type zxr10pimSnoopingNeighborValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_Zxr10pimSnoopingNeighborValid_Type.__name__ = "Integer32"
_Zxr10pimSnoopingNeighborValid_Object = MibTableColumn
zxr10pimSnoopingNeighborValid = _Zxr10pimSnoopingNeighborValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 2, 1, 1),
    _Zxr10pimSnoopingNeighborValid_Type()
)
zxr10pimSnoopingNeighborValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingNeighborValid.setStatus("current")
_Zxr10pimSnoopingNeighborVlanId_Type = Integer32
_Zxr10pimSnoopingNeighborVlanId_Object = MibTableColumn
zxr10pimSnoopingNeighborVlanId = _Zxr10pimSnoopingNeighborVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 2, 1, 2),
    _Zxr10pimSnoopingNeighborVlanId_Type()
)
zxr10pimSnoopingNeighborVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingNeighborVlanId.setStatus("current")
_Zxr10pimSnoopingNeighborVpnId_Type = Integer32
_Zxr10pimSnoopingNeighborVpnId_Object = MibTableColumn
zxr10pimSnoopingNeighborVpnId = _Zxr10pimSnoopingNeighborVpnId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 2, 1, 3),
    _Zxr10pimSnoopingNeighborVpnId_Type()
)
zxr10pimSnoopingNeighborVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingNeighborVpnId.setStatus("current")
_Zxr10pimSnoopingNeighborId_Type = Integer32
_Zxr10pimSnoopingNeighborId_Object = MibTableColumn
zxr10pimSnoopingNeighborId = _Zxr10pimSnoopingNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 2, 1, 4),
    _Zxr10pimSnoopingNeighborId_Type()
)
zxr10pimSnoopingNeighborId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingNeighborId.setStatus("current")
_Zxr10pimSnoopingNeighborSourceIpAddr_Type = IpAddress
_Zxr10pimSnoopingNeighborSourceIpAddr_Object = MibTableColumn
zxr10pimSnoopingNeighborSourceIpAddr = _Zxr10pimSnoopingNeighborSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 2, 1, 5),
    _Zxr10pimSnoopingNeighborSourceIpAddr_Type()
)
zxr10pimSnoopingNeighborSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingNeighborSourceIpAddr.setStatus("current")
_Zxr10pimSnoopingNeighborPort_Type = OctetString
_Zxr10pimSnoopingNeighborPort_Object = MibTableColumn
zxr10pimSnoopingNeighborPort = _Zxr10pimSnoopingNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 2, 1, 6),
    _Zxr10pimSnoopingNeighborPort_Type()
)
zxr10pimSnoopingNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingNeighborPort.setStatus("current")
_Zxr10IgmpSnoopingVlanTable_Object = MibTable
zxr10IgmpSnoopingVlanTable = _Zxr10IgmpSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3)
)
if mibBuilder.loadTexts:
    zxr10IgmpSnoopingVlanTable.setStatus("current")
_Zxr10IgmpSnoopingVlanEntry_Object = MibTableRow
zxr10IgmpSnoopingVlanEntry = _Zxr10IgmpSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1)
)
zxr10IgmpSnoopingVlanEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10igmpSnoopingVlanId"),
)
if mibBuilder.loadTexts:
    zxr10IgmpSnoopingVlanEntry.setStatus("current")
_Zxr10igmpSnoopingVlanEntryVlanId_Type = Integer32
_Zxr10igmpSnoopingVlanEntryVlanId_Object = MibTableColumn
zxr10igmpSnoopingVlanEntryVlanId = _Zxr10igmpSnoopingVlanEntryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1, 1),
    _Zxr10igmpSnoopingVlanEntryVlanId_Type()
)
zxr10igmpSnoopingVlanEntryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingVlanEntryVlanId.setStatus("current")


class _Zxr10igmpSnoopingVlanEntryEnable_Type(Integer32):
    """Custom type zxr10igmpSnoopingVlanEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_Zxr10igmpSnoopingVlanEntryEnable_Type.__name__ = "Integer32"
_Zxr10igmpSnoopingVlanEntryEnable_Object = MibTableColumn
zxr10igmpSnoopingVlanEntryEnable = _Zxr10igmpSnoopingVlanEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1, 2),
    _Zxr10igmpSnoopingVlanEntryEnable_Type()
)
zxr10igmpSnoopingVlanEntryEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingVlanEntryEnable.setStatus("current")


class _Zxr10pimSnoopingVlanEntryEnable_Type(Integer32):
    """Custom type zxr10pimSnoopingVlanEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_Zxr10pimSnoopingVlanEntryEnable_Type.__name__ = "Integer32"
_Zxr10pimSnoopingVlanEntryEnable_Object = MibTableColumn
zxr10pimSnoopingVlanEntryEnable = _Zxr10pimSnoopingVlanEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1, 3),
    _Zxr10pimSnoopingVlanEntryEnable_Type()
)
zxr10pimSnoopingVlanEntryEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingVlanEntryEnable.setStatus("current")


class _Zxr10igmpSnoopingFastLeave_Type(Integer32):
    """Custom type zxr10igmpSnoopingFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fast-leave", 0),
          ("slow-leave", 1))
    )


_Zxr10igmpSnoopingFastLeave_Type.__name__ = "Integer32"
_Zxr10igmpSnoopingFastLeave_Object = MibTableColumn
zxr10igmpSnoopingFastLeave = _Zxr10igmpSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1, 4),
    _Zxr10igmpSnoopingFastLeave_Type()
)
zxr10igmpSnoopingFastLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingFastLeave.setStatus("current")
_Zxr10igmpSnoopingLastMemberQueryInterval_Type = Integer32
_Zxr10igmpSnoopingLastMemberQueryInterval_Object = MibTableColumn
zxr10igmpSnoopingLastMemberQueryInterval = _Zxr10igmpSnoopingLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1, 5),
    _Zxr10igmpSnoopingLastMemberQueryInterval_Type()
)
zxr10igmpSnoopingLastMemberQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingLastMemberQueryInterval.setStatus("current")
_Zxr10igmpSnoopingMaxGroupNum_Type = Integer32
_Zxr10igmpSnoopingMaxGroupNum_Object = MibTableColumn
zxr10igmpSnoopingMaxGroupNum = _Zxr10igmpSnoopingMaxGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1, 6),
    _Zxr10igmpSnoopingMaxGroupNum_Type()
)
zxr10igmpSnoopingMaxGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMaxGroupNum.setStatus("current")
_Zxr10igmpSnoopingGroupNum_Type = Integer32
_Zxr10igmpSnoopingGroupNum_Object = MibTableColumn
zxr10igmpSnoopingGroupNum = _Zxr10igmpSnoopingGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1, 7),
    _Zxr10igmpSnoopingGroupNum_Type()
)
zxr10igmpSnoopingGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingGroupNum.setStatus("current")
_Zxr10igmpSnoopingHostTimeOut_Type = Integer32
_Zxr10igmpSnoopingHostTimeOut_Object = MibTableColumn
zxr10igmpSnoopingHostTimeOut = _Zxr10igmpSnoopingHostTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1, 8),
    _Zxr10igmpSnoopingHostTimeOut_Type()
)
zxr10igmpSnoopingHostTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingHostTimeOut.setStatus("current")
_Zxr10igmpSnoopingMrTimeOut_Type = Integer32
_Zxr10igmpSnoopingMrTimeOut_Object = MibTableColumn
zxr10igmpSnoopingMrTimeOut = _Zxr10igmpSnoopingMrTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 3, 1, 9),
    _Zxr10igmpSnoopingMrTimeOut_Type()
)
zxr10igmpSnoopingMrTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingMrTimeOut.setStatus("current")


class _Zxr10igmpSnoopingEnable_Type(Integer32):
    """Custom type zxr10igmpSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_Zxr10igmpSnoopingEnable_Type.__name__ = "Integer32"
_Zxr10igmpSnoopingEnable_Object = MibScalar
zxr10igmpSnoopingEnable = _Zxr10igmpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 4),
    _Zxr10igmpSnoopingEnable_Type()
)
zxr10igmpSnoopingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingEnable.setStatus("current")


class _Zxr10pimSnoopingEnable_Type(Integer32):
    """Custom type zxr10pimSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_Zxr10pimSnoopingEnable_Type.__name__ = "Integer32"
_Zxr10pimSnoopingEnable_Object = MibScalar
zxr10pimSnoopingEnable = _Zxr10pimSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 5),
    _Zxr10pimSnoopingEnable_Type()
)
zxr10pimSnoopingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10pimSnoopingEnable.setStatus("current")


class _Zxr10igmpSnoopingGlobalQuery_Type(Integer32):
    """Custom type zxr10igmpSnoopingGlobalQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_Zxr10igmpSnoopingGlobalQuery_Type.__name__ = "Integer32"
_Zxr10igmpSnoopingGlobalQuery_Object = MibScalar
zxr10igmpSnoopingGlobalQuery = _Zxr10igmpSnoopingGlobalQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 6),
    _Zxr10igmpSnoopingGlobalQuery_Type()
)
zxr10igmpSnoopingGlobalQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingGlobalQuery.setStatus("current")
_Zxr10igmpSnoopingQueryInterval_Type = Integer32
_Zxr10igmpSnoopingQueryInterval_Object = MibScalar
zxr10igmpSnoopingQueryInterval = _Zxr10igmpSnoopingQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 7),
    _Zxr10igmpSnoopingQueryInterval_Type()
)
zxr10igmpSnoopingQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingQueryInterval.setStatus("current")
_Zxr10igmpSnoopingQueryResponseInterval_Type = Integer32
_Zxr10igmpSnoopingQueryResponseInterval_Object = MibScalar
zxr10igmpSnoopingQueryResponseInterval = _Zxr10igmpSnoopingQueryResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 5, 8),
    _Zxr10igmpSnoopingQueryResponseInterval_Type()
)
zxr10igmpSnoopingQueryResponseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10igmpSnoopingQueryResponseInterval.setStatus("current")
_Zxr10extAlarm_ObjectIdentity = ObjectIdentity
zxr10extAlarm = _Zxr10extAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6)
)
_Zxr10InputAlarmTable_Object = MibTable
zxr10InputAlarmTable = _Zxr10InputAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 1)
)
if mibBuilder.loadTexts:
    zxr10InputAlarmTable.setStatus("current")
_Zxr10InputAlarmEntry_Object = MibTableRow
zxr10InputAlarmEntry = _Zxr10InputAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 1, 1)
)
zxr10InputAlarmEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10InputAlarmIndex"),
)
if mibBuilder.loadTexts:
    zxr10InputAlarmEntry.setStatus("current")
_Zxr10InputAlarmIndex_Type = Integer32
_Zxr10InputAlarmIndex_Object = MibTableColumn
zxr10InputAlarmIndex = _Zxr10InputAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 1, 1, 1),
    _Zxr10InputAlarmIndex_Type()
)
zxr10InputAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10InputAlarmIndex.setStatus("current")


class _Zxr10InputAlarmStatus_Type(Integer32):
    """Custom type zxr10InputAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("clear", 0))
    )


_Zxr10InputAlarmStatus_Type.__name__ = "Integer32"
_Zxr10InputAlarmStatus_Object = MibTableColumn
zxr10InputAlarmStatus = _Zxr10InputAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 1, 1, 2),
    _Zxr10InputAlarmStatus_Type()
)
zxr10InputAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10InputAlarmStatus.setStatus("current")


class _Zxr10InputAlarmDescription_Type(DisplayString):
    """Custom type zxr10InputAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Zxr10InputAlarmDescription_Type.__name__ = "DisplayString"
_Zxr10InputAlarmDescription_Object = MibTableColumn
zxr10InputAlarmDescription = _Zxr10InputAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 1, 1, 3),
    _Zxr10InputAlarmDescription_Type()
)
zxr10InputAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10InputAlarmDescription.setStatus("current")
_Zxr10OutputAlarmTable_Object = MibTable
zxr10OutputAlarmTable = _Zxr10OutputAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 2)
)
if mibBuilder.loadTexts:
    zxr10OutputAlarmTable.setStatus("current")
_Zxr10OutputAlarmEntry_Object = MibTableRow
zxr10OutputAlarmEntry = _Zxr10OutputAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 2, 1)
)
zxr10OutputAlarmEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10OutputAlarmIndex"),
)
if mibBuilder.loadTexts:
    zxr10OutputAlarmEntry.setStatus("current")
_Zxr10OutputAlarmIndex_Type = Integer32
_Zxr10OutputAlarmIndex_Object = MibTableColumn
zxr10OutputAlarmIndex = _Zxr10OutputAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 2, 1, 1),
    _Zxr10OutputAlarmIndex_Type()
)
zxr10OutputAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OutputAlarmIndex.setStatus("current")


class _Zxr10OutputAlarmStatus_Type(Integer32):
    """Custom type zxr10OutputAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("clear", 0))
    )


_Zxr10OutputAlarmStatus_Type.__name__ = "Integer32"
_Zxr10OutputAlarmStatus_Object = MibTableColumn
zxr10OutputAlarmStatus = _Zxr10OutputAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 2, 1, 2),
    _Zxr10OutputAlarmStatus_Type()
)
zxr10OutputAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10OutputAlarmStatus.setStatus("current")


class _Zxr10OutputAlarmDescription_Type(DisplayString):
    """Custom type zxr10OutputAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Zxr10OutputAlarmDescription_Type.__name__ = "DisplayString"
_Zxr10OutputAlarmDescription_Object = MibTableColumn
zxr10OutputAlarmDescription = _Zxr10OutputAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 6, 2, 1, 3),
    _Zxr10OutputAlarmDescription_Type()
)
zxr10OutputAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10OutputAlarmDescription.setStatus("current")
_Zess_ObjectIdentity = ObjectIdentity
zess = _Zess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13)
)


class _ZessClearAllChangeTimes_Type(Integer32):
    """Custom type zessClearAllChangeTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZessClearAllChangeTimes_Type.__name__ = "Integer32"
_ZessClearAllChangeTimes_Object = MibScalar
zessClearAllChangeTimes = _ZessClearAllChangeTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 1),
    _ZessClearAllChangeTimes_Type()
)
zessClearAllChangeTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zessClearAllChangeTimes.setStatus("current")
_ZessDomainTable_Object = MibTable
zessDomainTable = _ZessDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2)
)
if mibBuilder.loadTexts:
    zessDomainTable.setStatus("current")
_ZessDomainEntry_Object = MibTableRow
zessDomainEntry = _ZessDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1)
)
zessDomainEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zessDomainId"),
)
if mibBuilder.loadTexts:
    zessDomainEntry.setStatus("current")


class _ZessDomainId_Type(Integer32):
    """Custom type zessDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZessDomainId_Type.__name__ = "Integer32"
_ZessDomainId_Object = MibTableColumn
zessDomainId = _ZessDomainId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 1),
    _ZessDomainId_Type()
)
zessDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zessDomainId.setStatus("current")


class _ZessProtectInstanceId_Type(Integer32):
    """Custom type zessProtectInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ZessProtectInstanceId_Type.__name__ = "Integer32"
_ZessProtectInstanceId_Object = MibTableColumn
zessProtectInstanceId = _ZessProtectInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 2),
    _ZessProtectInstanceId_Type()
)
zessProtectInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zessProtectInstanceId.setStatus("current")
_ZessPrimaryPort_Type = DisplayString
_ZessPrimaryPort_Object = MibTableColumn
zessPrimaryPort = _ZessPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 3),
    _ZessPrimaryPort_Type()
)
zessPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zessPrimaryPort.setStatus("current")
_ZessSecondaryPort_Type = DisplayString
_ZessSecondaryPort_Object = MibTableColumn
zessSecondaryPort = _ZessSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 4),
    _ZessSecondaryPort_Type()
)
zessSecondaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zessSecondaryPort.setStatus("current")


class _ZessPreupDelayTime_Type(Integer32):
    """Custom type zessPreupDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_ZessPreupDelayTime_Type.__name__ = "Integer32"
_ZessPreupDelayTime_Object = MibTableColumn
zessPreupDelayTime = _ZessPreupDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 5),
    _ZessPreupDelayTime_Type()
)
zessPreupDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zessPreupDelayTime.setStatus("current")


class _ZessDomainMode_Type(Integer32):
    """Custom type zessDomainMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 0))
    )


_ZessDomainMode_Type.__name__ = "Integer32"
_ZessDomainMode_Object = MibTableColumn
zessDomainMode = _ZessDomainMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 6),
    _ZessDomainMode_Type()
)
zessDomainMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zessDomainMode.setStatus("current")


class _ZessDomainState_Type(Integer32):
    """Custom type zessDomainState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("preup", 4),
          ("unknown", 0),
          ("up", 1))
    )


_ZessDomainState_Type.__name__ = "Integer32"
_ZessDomainState_Object = MibTableColumn
zessDomainState = _ZessDomainState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 7),
    _ZessDomainState_Type()
)
zessDomainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zessDomainState.setStatus("current")


class _ZessPriIfState_Type(Integer32):
    """Custom type zessPriIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 3),
          ("unknown", 0))
    )


_ZessPriIfState_Type.__name__ = "Integer32"
_ZessPriIfState_Object = MibTableColumn
zessPriIfState = _ZessPriIfState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 8),
    _ZessPriIfState_Type()
)
zessPriIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zessPriIfState.setStatus("current")


class _ZessSecIfState_Type(Integer32):
    """Custom type zessSecIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("forward", 3),
          ("unknown", 0))
    )


_ZessSecIfState_Type.__name__ = "Integer32"
_ZessSecIfState_Object = MibTableColumn
zessSecIfState = _ZessSecIfState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 9),
    _ZessSecIfState_Type()
)
zessSecIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zessSecIfState.setStatus("current")
_ZessChangeTimes_Type = Integer32
_ZessChangeTimes_Object = MibTableColumn
zessChangeTimes = _ZessChangeTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 10),
    _ZessChangeTimes_Type()
)
zessChangeTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zessChangeTimes.setStatus("current")


class _ZessClearChangeTimes_Type(Integer32):
    """Custom type zessClearChangeTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZessClearChangeTimes_Type.__name__ = "Integer32"
_ZessClearChangeTimes_Object = MibTableColumn
zessClearChangeTimes = _ZessClearChangeTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 11),
    _ZessClearChangeTimes_Type()
)
zessClearChangeTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zessClearChangeTimes.setStatus("current")
_ZessDomainRowStatus_Type = RowStatus
_ZessDomainRowStatus_Object = MibTableColumn
zessDomainRowStatus = _ZessDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 13, 2, 1, 12),
    _ZessDomainRowStatus_Type()
)
zessDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zessDomainRowStatus.setStatus("current")
_Vct_ObjectIdentity = ObjectIdentity
vct = _Vct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14)
)
_VctPortTable_Object = MibTable
vctPortTable = _VctPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1)
)
if mibBuilder.loadTexts:
    vctPortTable.setStatus("current")
_VctPortEntry_Object = MibTableRow
vctPortEntry = _VctPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1)
)
vctPortEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "vctPortName"),
)
if mibBuilder.loadTexts:
    vctPortEntry.setStatus("current")


class _VctPortName_Type(DisplayString):
    """Custom type vctPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VctPortName_Type.__name__ = "DisplayString"
_VctPortName_Object = MibTableColumn
vctPortName = _VctPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 1),
    _VctPortName_Type()
)
vctPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPortName.setStatus("current")


class _VctIsValid_Type(Integer32):
    """Custom type vctIsValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_VctIsValid_Type.__name__ = "Integer32"
_VctIsValid_Object = MibTableColumn
vctIsValid = _VctIsValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 2),
    _VctIsValid_Type()
)
vctIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctIsValid.setStatus("current")


class _VctCableStatus_Type(Integer32):
    """Custom type vctCableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("good", 0),
          ("not-support", 2))
    )


_VctCableStatus_Type.__name__ = "Integer32"
_VctCableStatus_Object = MibTableColumn
vctCableStatus = _VctCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 3),
    _VctCableStatus_Type()
)
vctCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctCableStatus.setStatus("current")


class _VctPair1Result_Type(DisplayString):
    """Custom type vctPair1Result based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VctPair1Result_Type.__name__ = "DisplayString"
_VctPair1Result_Object = MibTableColumn
vctPair1Result = _VctPair1Result_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 4),
    _VctPair1Result_Type()
)
vctPair1Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair1Result.setStatus("current")


class _VctPair1Lenth_Type(DisplayString):
    """Custom type vctPair1Lenth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VctPair1Lenth_Type.__name__ = "DisplayString"
_VctPair1Lenth_Object = MibTableColumn
vctPair1Lenth = _VctPair1Lenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 5),
    _VctPair1Lenth_Type()
)
vctPair1Lenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair1Lenth.setStatus("current")


class _VctPair2Result_Type(DisplayString):
    """Custom type vctPair2Result based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VctPair2Result_Type.__name__ = "DisplayString"
_VctPair2Result_Object = MibTableColumn
vctPair2Result = _VctPair2Result_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 6),
    _VctPair2Result_Type()
)
vctPair2Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair2Result.setStatus("current")


class _VctPair2Lenth_Type(DisplayString):
    """Custom type vctPair2Lenth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VctPair2Lenth_Type.__name__ = "DisplayString"
_VctPair2Lenth_Object = MibTableColumn
vctPair2Lenth = _VctPair2Lenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 7),
    _VctPair2Lenth_Type()
)
vctPair2Lenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair2Lenth.setStatus("current")


class _VctPair3Result_Type(DisplayString):
    """Custom type vctPair3Result based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VctPair3Result_Type.__name__ = "DisplayString"
_VctPair3Result_Object = MibTableColumn
vctPair3Result = _VctPair3Result_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 8),
    _VctPair3Result_Type()
)
vctPair3Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair3Result.setStatus("current")


class _VctPair3Lenth_Type(DisplayString):
    """Custom type vctPair3Lenth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VctPair3Lenth_Type.__name__ = "DisplayString"
_VctPair3Lenth_Object = MibTableColumn
vctPair3Lenth = _VctPair3Lenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 9),
    _VctPair3Lenth_Type()
)
vctPair3Lenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair3Lenth.setStatus("current")


class _VctPair4Result_Type(DisplayString):
    """Custom type vctPair4Result based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VctPair4Result_Type.__name__ = "DisplayString"
_VctPair4Result_Object = MibTableColumn
vctPair4Result = _VctPair4Result_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 10),
    _VctPair4Result_Type()
)
vctPair4Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair4Result.setStatus("current")


class _VctPair4Lenth_Type(DisplayString):
    """Custom type vctPair4Lenth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VctPair4Lenth_Type.__name__ = "DisplayString"
_VctPair4Lenth_Object = MibTableColumn
vctPair4Lenth = _VctPair4Lenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 11),
    _VctPair4Lenth_Type()
)
vctPair4Lenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair4Lenth.setStatus("current")
_VctRowStatus_Type = RowStatus
_VctRowStatus_Object = MibTableColumn
vctRowStatus = _VctRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 1, 1, 12),
    _VctRowStatus_Type()
)
vctRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vctRowStatus.setStatus("current")
_VctTable_Object = MibTable
vctTable = _VctTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2)
)
if mibBuilder.loadTexts:
    vctTable.setStatus("current")
_VctEntry_Object = MibTableRow
vctEntry = _VctEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1)
)
vctEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "vctIfindex"),
)
if mibBuilder.loadTexts:
    vctEntry.setStatus("current")
_VctIfindex_Type = Integer32
_VctIfindex_Object = MibTableColumn
vctIfindex = _VctIfindex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 1),
    _VctIfindex_Type()
)
vctIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctIfindex.setStatus("current")


class _VctSetIfindex_Type(Integer32):
    """Custom type vctSetIfindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VctSetIfindex_Type.__name__ = "Integer32"
_VctSetIfindex_Object = MibTableColumn
vctSetIfindex = _VctSetIfindex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 2),
    _VctSetIfindex_Type()
)
vctSetIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctSetIfindex.setStatus("current")


class _CableStatus_Type(Integer32):
    """Custom type cableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fault", 0),
          ("good", 1))
    )


_CableStatus_Type.__name__ = "Integer32"
_CableStatus_Object = MibTableColumn
cableStatus = _CableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 3),
    _CableStatus_Type()
)
cableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableStatus.setStatus("current")


class _DoubleCableStatus1_2_Type(Integer32):
    """Custom type doubleCableStatus1_2 based on Integer32"""
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
        *(("broken", 3),
          ("fail", 5),
          ("good", 0),
          ("mismatch", 4),
          ("null", 7),
          ("open", 1),
          ("short", 2),
          ("unknown", 6))
    )


_DoubleCableStatus1_2_Type.__name__ = "Integer32"
_DoubleCableStatus1_2_Object = MibScalar
doubleCableStatus1_2 = _DoubleCableStatus1_2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 4),
    _DoubleCableStatus1_2_Type()
)
doubleCableStatus1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableStatus1_2.setStatus("current")


class _DoubleCableStatus3_6_Type(Integer32):
    """Custom type doubleCableStatus3_6 based on Integer32"""
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
        *(("broken", 3),
          ("fail", 5),
          ("good", 0),
          ("mismatch", 4),
          ("null", 7),
          ("open", 1),
          ("short", 2),
          ("unknown", 6))
    )


_DoubleCableStatus3_6_Type.__name__ = "Integer32"
_DoubleCableStatus3_6_Object = MibScalar
doubleCableStatus3_6 = _DoubleCableStatus3_6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 5),
    _DoubleCableStatus3_6_Type()
)
doubleCableStatus3_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableStatus3_6.setStatus("current")


class _DoubleCableStatus4_5_Type(Integer32):
    """Custom type doubleCableStatus4_5 based on Integer32"""
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
        *(("broken", 3),
          ("fail", 5),
          ("good", 0),
          ("mismatch", 4),
          ("null", 7),
          ("open", 1),
          ("short", 2),
          ("unknown", 6))
    )


_DoubleCableStatus4_5_Type.__name__ = "Integer32"
_DoubleCableStatus4_5_Object = MibScalar
doubleCableStatus4_5 = _DoubleCableStatus4_5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 6),
    _DoubleCableStatus4_5_Type()
)
doubleCableStatus4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableStatus4_5.setStatus("current")


class _DoubleCableStatus7_8_Type(Integer32):
    """Custom type doubleCableStatus7_8 based on Integer32"""
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
        *(("broken", 3),
          ("fail", 5),
          ("good", 0),
          ("mismatch", 4),
          ("null", 7),
          ("open", 1),
          ("short", 2),
          ("unknown", 6))
    )


_DoubleCableStatus7_8_Type.__name__ = "Integer32"
_DoubleCableStatus7_8_Object = MibScalar
doubleCableStatus7_8 = _DoubleCableStatus7_8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 7),
    _DoubleCableStatus7_8_Type()
)
doubleCableStatus7_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableStatus7_8.setStatus("current")


class _DoubleCableLength1_2_Type(Integer32):
    """Custom type doubleCableLength1_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              201,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("from110to140", 203),
          ("from50to80", 201),
          ("from80to110", 202),
          ("lessthan50", 200),
          ("morethan140", 204),
          ("null", 206),
          ("unknow", 205))
    )


_DoubleCableLength1_2_Type.__name__ = "Integer32"
_DoubleCableLength1_2_Object = MibScalar
doubleCableLength1_2 = _DoubleCableLength1_2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 8),
    _DoubleCableLength1_2_Type()
)
doubleCableLength1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableLength1_2.setStatus("current")


class _DoubleCableLength3_6_Type(Integer32):
    """Custom type doubleCableLength3_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              201,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("from110to140", 203),
          ("from50to80", 201),
          ("from80to110", 202),
          ("lessthan50", 200),
          ("morethan140", 204),
          ("null", 206),
          ("unknow", 205))
    )


_DoubleCableLength3_6_Type.__name__ = "Integer32"
_DoubleCableLength3_6_Object = MibScalar
doubleCableLength3_6 = _DoubleCableLength3_6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 9),
    _DoubleCableLength3_6_Type()
)
doubleCableLength3_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableLength3_6.setStatus("current")


class _DoubleCableLength4_5_Type(Integer32):
    """Custom type doubleCableLength4_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              201,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("from110to140", 203),
          ("from50to80", 201),
          ("from80to110", 202),
          ("lessthan50", 200),
          ("morethan140", 204),
          ("null", 206),
          ("unknow", 205))
    )


_DoubleCableLength4_5_Type.__name__ = "Integer32"
_DoubleCableLength4_5_Object = MibScalar
doubleCableLength4_5 = _DoubleCableLength4_5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 10),
    _DoubleCableLength4_5_Type()
)
doubleCableLength4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableLength4_5.setStatus("current")


class _DoubleCableLength7_8_Type(Integer32):
    """Custom type doubleCableLength7_8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              201,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("from110to140", 203),
          ("from50to80", 201),
          ("from80to110", 202),
          ("lessthan50", 200),
          ("morethan140", 204),
          ("null", 206),
          ("unknow", 205))
    )


_DoubleCableLength7_8_Type.__name__ = "Integer32"
_DoubleCableLength7_8_Object = MibScalar
doubleCableLength7_8 = _DoubleCableLength7_8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 14, 2, 1, 11),
    _DoubleCableLength7_8_Type()
)
doubleCableLength7_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doubleCableLength7_8.setStatus("current")
_Loopdetect_ObjectIdentity = ObjectIdentity
loopdetect = _Loopdetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15)
)


class _LoopdetectReopenTime_Type(Integer32):
    """Custom type loopdetectReopenTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777216),
    )


_LoopdetectReopenTime_Type.__name__ = "Integer32"
_LoopdetectReopenTime_Object = MibScalar
loopdetectReopenTime = _LoopdetectReopenTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 1),
    _LoopdetectReopenTime_Type()
)
loopdetectReopenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopdetectReopenTime.setStatus("current")
_LoopdetectTable_Object = MibTable
loopdetectTable = _LoopdetectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 2)
)
if mibBuilder.loadTexts:
    loopdetectTable.setStatus("current")
_LoopdetectEntry_Object = MibTableRow
loopdetectEntry = _LoopdetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 2, 1)
)
loopdetectEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "loopdetectPanelNum"),
    (0, "ZXR10-SWITCH-MIB", "loopdetectPortNum"),
)
if mibBuilder.loadTexts:
    loopdetectEntry.setStatus("current")


class _LoopdetectPanelNum_Type(Integer32):
    """Custom type loopdetectPanelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_LoopdetectPanelNum_Type.__name__ = "Integer32"
_LoopdetectPanelNum_Object = MibTableColumn
loopdetectPanelNum = _LoopdetectPanelNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 2, 1, 1),
    _LoopdetectPanelNum_Type()
)
loopdetectPanelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopdetectPanelNum.setStatus("current")


class _LoopdetectPortNum_Type(Integer32):
    """Custom type loopdetectPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_LoopdetectPortNum_Type.__name__ = "Integer32"
_LoopdetectPortNum_Object = MibTableColumn
loopdetectPortNum = _LoopdetectPortNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 2, 1, 2),
    _LoopdetectPortNum_Type()
)
loopdetectPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopdetectPortNum.setStatus("current")


class _LoopdetectPortName_Type(DisplayString):
    """Custom type loopdetectPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LoopdetectPortName_Type.__name__ = "DisplayString"
_LoopdetectPortName_Object = MibTableColumn
loopdetectPortName = _LoopdetectPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 2, 1, 3),
    _LoopdetectPortName_Type()
)
loopdetectPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopdetectPortName.setStatus("current")


class _LoopdetectPortOperStatus_Type(Integer32):
    """Custom type loopdetectPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("normal", 0),
          ("protect", 1))
    )


_LoopdetectPortOperStatus_Type.__name__ = "Integer32"
_LoopdetectPortOperStatus_Object = MibTableColumn
loopdetectPortOperStatus = _LoopdetectPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 2, 1, 4),
    _LoopdetectPortOperStatus_Type()
)
loopdetectPortOperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    loopdetectPortOperStatus.setStatus("current")


class _LoopdetectPortVlan_Type(DisplayString):
    """Custom type loopdetectPortVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LoopdetectPortVlan_Type.__name__ = "DisplayString"
_LoopdetectPortVlan_Object = MibTableColumn
loopdetectPortVlan = _LoopdetectPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 2, 1, 5),
    _LoopdetectPortVlan_Type()
)
loopdetectPortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    loopdetectPortVlan.setStatus("current")


class _LoopdetectPortMonitor_Type(Integer32):
    """Custom type loopdetectPortMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LoopdetectPortMonitor_Type.__name__ = "Integer32"
_LoopdetectPortMonitor_Object = MibTableColumn
loopdetectPortMonitor = _LoopdetectPortMonitor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 2, 1, 6),
    _LoopdetectPortMonitor_Type()
)
loopdetectPortMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    loopdetectPortMonitor.setStatus("current")
_LoopdetectPortRowStatus_Type = RowStatus
_LoopdetectPortRowStatus_Object = MibTableColumn
loopdetectPortRowStatus = _LoopdetectPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 15, 2, 1, 7),
    _LoopdetectPortRowStatus_Type()
)
loopdetectPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    loopdetectPortRowStatus.setStatus("current")
_Svlan_ObjectIdentity = ObjectIdentity
svlan = _Svlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17)
)


class _Zxr10svlanCount_Type(Integer32):
    """Custom type zxr10svlanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_Zxr10svlanCount_Type.__name__ = "Integer32"
_Zxr10svlanCount_Object = MibScalar
zxr10svlanCount = _Zxr10svlanCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 10),
    _Zxr10svlanCount_Type()
)
zxr10svlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanCount.setStatus("current")


class _Zxr10svlanFreeCount_Type(Integer32):
    """Custom type zxr10svlanFreeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_Zxr10svlanFreeCount_Type.__name__ = "Integer32"
_Zxr10svlanFreeCount_Object = MibScalar
zxr10svlanFreeCount = _Zxr10svlanFreeCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 11),
    _Zxr10svlanFreeCount_Type()
)
zxr10svlanFreeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanFreeCount.setStatus("current")
_Zxr10svlanTable_Object = MibTable
zxr10svlanTable = _Zxr10svlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12)
)
if mibBuilder.loadTexts:
    zxr10svlanTable.setStatus("current")
_Zxr10svlanEntry_Object = MibTableRow
zxr10svlanEntry = _Zxr10svlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1)
)
zxr10svlanEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10svlanSessionNo"),
)
if mibBuilder.loadTexts:
    zxr10svlanEntry.setStatus("current")


class _Zxr10svlanSessionNo_Type(Integer32):
    """Custom type zxr10svlanSessionNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_Zxr10svlanSessionNo_Type.__name__ = "Integer32"
_Zxr10svlanSessionNo_Object = MibTableColumn
zxr10svlanSessionNo = _Zxr10svlanSessionNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 1),
    _Zxr10svlanSessionNo_Type()
)
zxr10svlanSessionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanSessionNo.setStatus("current")


class _Zxr10svlanDescription_Type(DisplayString):
    """Custom type zxr10svlanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_Zxr10svlanDescription_Type.__name__ = "DisplayString"
_Zxr10svlanDescription_Object = MibTableColumn
zxr10svlanDescription = _Zxr10svlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 2),
    _Zxr10svlanDescription_Type()
)
zxr10svlanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanDescription.setStatus("current")


class _Zxr10svlanCustomerPort_Type(DisplayString):
    """Custom type zxr10svlanCustomerPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Zxr10svlanCustomerPort_Type.__name__ = "DisplayString"
_Zxr10svlanCustomerPort_Object = MibTableColumn
zxr10svlanCustomerPort = _Zxr10svlanCustomerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 3),
    _Zxr10svlanCustomerPort_Type()
)
zxr10svlanCustomerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanCustomerPort.setStatus("current")


class _Zxr10svlanUplinkPort_Type(DisplayString):
    """Custom type zxr10svlanUplinkPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Zxr10svlanUplinkPort_Type.__name__ = "DisplayString"
_Zxr10svlanUplinkPort_Object = MibTableColumn
zxr10svlanUplinkPort = _Zxr10svlanUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 4),
    _Zxr10svlanUplinkPort_Type()
)
zxr10svlanUplinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanUplinkPort.setStatus("current")


class _Zxr10svlanInvlan_Type(DisplayString):
    """Custom type zxr10svlanInvlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_Zxr10svlanInvlan_Type.__name__ = "DisplayString"
_Zxr10svlanInvlan_Object = MibTableColumn
zxr10svlanInvlan = _Zxr10svlanInvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 5),
    _Zxr10svlanInvlan_Type()
)
zxr10svlanInvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanInvlan.setStatus("current")


class _Zxr10svlanOvlan_Type(DisplayString):
    """Custom type zxr10svlanOvlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Zxr10svlanOvlan_Type.__name__ = "DisplayString"
_Zxr10svlanOvlan_Object = MibTableColumn
zxr10svlanOvlan = _Zxr10svlanOvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 6),
    _Zxr10svlanOvlan_Type()
)
zxr10svlanOvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanOvlan.setStatus("current")


class _Zxr10svlanRedirect_Type(Integer32):
    """Custom type zxr10svlanRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("undirect", 1)
    )


_Zxr10svlanRedirect_Type.__name__ = "Integer32"
_Zxr10svlanRedirect_Object = MibTableColumn
zxr10svlanRedirect = _Zxr10svlanRedirect_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 7),
    _Zxr10svlanRedirect_Type()
)
zxr10svlanRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanRedirect.setStatus("current")


class _Zxr10svlanAdvanced_Type(Integer32):
    """Custom type zxr10svlanAdvanced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("special", 1))
    )


_Zxr10svlanAdvanced_Type.__name__ = "Integer32"
_Zxr10svlanAdvanced_Object = MibTableColumn
zxr10svlanAdvanced = _Zxr10svlanAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 8),
    _Zxr10svlanAdvanced_Type()
)
zxr10svlanAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanAdvanced.setStatus("current")


class _Zxr10svlanPriority_Type(Integer32):
    """Custom type zxr10svlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Zxr10svlanPriority_Type.__name__ = "Integer32"
_Zxr10svlanPriority_Object = MibTableColumn
zxr10svlanPriority = _Zxr10svlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 9),
    _Zxr10svlanPriority_Type()
)
zxr10svlanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanPriority.setStatus("current")


class _Zxr10svlanHelperVlan_Type(DisplayString):
    """Custom type zxr10svlanHelperVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Zxr10svlanHelperVlan_Type.__name__ = "DisplayString"
_Zxr10svlanHelperVlan_Object = MibTableColumn
zxr10svlanHelperVlan = _Zxr10svlanHelperVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 17, 12, 1, 10),
    _Zxr10svlanHelperVlan_Type()
)
zxr10svlanHelperVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10svlanHelperVlan.setStatus("current")
_Vfp_ObjectIdentity = ObjectIdentity
vfp = _Vfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18)
)
_Zxr10vfpTable_Object = MibTable
zxr10vfpTable = _Zxr10vfpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1)
)
if mibBuilder.loadTexts:
    zxr10vfpTable.setStatus("current")
_Zxr10vfpEntry_Object = MibTableRow
zxr10vfpEntry = _Zxr10vfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1)
)
zxr10vfpEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "zxr10vfpInterfaceName"),
    (0, "ZXR10-SWITCH-MIB", "zxr10vfpSessionId"),
)
if mibBuilder.loadTexts:
    zxr10vfpEntry.setStatus("current")


class _Zxr10vfpInterfaceName_Type(DisplayString):
    """Custom type zxr10vfpInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Zxr10vfpInterfaceName_Type.__name__ = "DisplayString"
_Zxr10vfpInterfaceName_Object = MibTableColumn
zxr10vfpInterfaceName = _Zxr10vfpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 1),
    _Zxr10vfpInterfaceName_Type()
)
zxr10vfpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpInterfaceName.setStatus("current")


class _Zxr10vfpSessionId_Type(Integer32):
    """Custom type zxr10vfpSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_Zxr10vfpSessionId_Type.__name__ = "Integer32"
_Zxr10vfpSessionId_Object = MibTableColumn
zxr10vfpSessionId = _Zxr10vfpSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 2),
    _Zxr10vfpSessionId_Type()
)
zxr10vfpSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpSessionId.setStatus("current")


class _Zxr10vfpDescription_Type(DisplayString):
    """Custom type zxr10vfpDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_Zxr10vfpDescription_Type.__name__ = "DisplayString"
_Zxr10vfpDescription_Object = MibTableColumn
zxr10vfpDescription = _Zxr10vfpDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 3),
    _Zxr10vfpDescription_Type()
)
zxr10vfpDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpDescription.setStatus("current")


class _Zxr10vfpInVlan_Type(DisplayString):
    """Custom type zxr10vfpInVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_Zxr10vfpInVlan_Type.__name__ = "DisplayString"
_Zxr10vfpInVlan_Object = MibTableColumn
zxr10vfpInVlan = _Zxr10vfpInVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 4),
    _Zxr10vfpInVlan_Type()
)
zxr10vfpInVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpInVlan.setStatus("current")


class _Zxr10vfpAclNO_Type(Integer32):
    """Custom type zxr10vfpAclNO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2999),
    )


_Zxr10vfpAclNO_Type.__name__ = "Integer32"
_Zxr10vfpAclNO_Object = MibTableColumn
zxr10vfpAclNO = _Zxr10vfpAclNO_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 5),
    _Zxr10vfpAclNO_Type()
)
zxr10vfpAclNO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpAclNO.setStatus("current")


class _Zxr10vfpRuleNo_Type(Integer32):
    """Custom type zxr10vfpRuleNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Zxr10vfpRuleNo_Type.__name__ = "Integer32"
_Zxr10vfpRuleNo_Object = MibTableColumn
zxr10vfpRuleNo = _Zxr10vfpRuleNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 6),
    _Zxr10vfpRuleNo_Type()
)
zxr10vfpRuleNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpRuleNo.setStatus("current")


class _Zxr10vfpOvlan_Type(DisplayString):
    """Custom type zxr10vfpOvlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Zxr10vfpOvlan_Type.__name__ = "DisplayString"
_Zxr10vfpOvlan_Object = MibTableColumn
zxr10vfpOvlan = _Zxr10vfpOvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 7),
    _Zxr10vfpOvlan_Type()
)
zxr10vfpOvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpOvlan.setStatus("current")


class _Zxr10vfpPriority_Type(Integer32):
    """Custom type zxr10vfpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Zxr10vfpPriority_Type.__name__ = "Integer32"
_Zxr10vfpPriority_Object = MibTableColumn
zxr10vfpPriority = _Zxr10vfpPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 8),
    _Zxr10vfpPriority_Type()
)
zxr10vfpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpPriority.setStatus("current")


class _Zxr10vfpUntagAppFlag_Type(Integer32):
    """Custom type zxr10vfpUntagAppFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("pinpoint", 1))
    )


_Zxr10vfpUntagAppFlag_Type.__name__ = "Integer32"
_Zxr10vfpUntagAppFlag_Object = MibTableColumn
zxr10vfpUntagAppFlag = _Zxr10vfpUntagAppFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 9),
    _Zxr10vfpUntagAppFlag_Type()
)
zxr10vfpUntagAppFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpUntagAppFlag.setStatus("current")


class _Zxr10vfpClassId_Type(Integer32):
    """Custom type zxr10vfpClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Zxr10vfpClassId_Type.__name__ = "Integer32"
_Zxr10vfpClassId_Object = MibTableColumn
zxr10vfpClassId = _Zxr10vfpClassId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 10),
    _Zxr10vfpClassId_Type()
)
zxr10vfpClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpClassId.setStatus("current")


class _Zxr10vfpVrfId_Type(Integer32):
    """Custom type zxr10vfpVrfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Zxr10vfpVrfId_Type.__name__ = "Integer32"
_Zxr10vfpVrfId_Object = MibTableColumn
zxr10vfpVrfId = _Zxr10vfpVrfId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 18, 1, 1, 11),
    _Zxr10vfpVrfId_Type()
)
zxr10vfpVrfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10vfpVrfId.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 23)
)
_DhcpIpSourceGuardIfNumber_Type = Integer32
_DhcpIpSourceGuardIfNumber_Object = MibScalar
dhcpIpSourceGuardIfNumber = _DhcpIpSourceGuardIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 23, 1),
    _DhcpIpSourceGuardIfNumber_Type()
)
dhcpIpSourceGuardIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpIpSourceGuardIfNumber.setStatus("current")
_DhcpIpSourceGuardTable_Object = MibTable
dhcpIpSourceGuardTable = _DhcpIpSourceGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 23, 2)
)
if mibBuilder.loadTexts:
    dhcpIpSourceGuardTable.setStatus("current")
_DhcpIpSourceGuardEntry_Object = MibTableRow
dhcpIpSourceGuardEntry = _DhcpIpSourceGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 23, 2, 1)
)
dhcpIpSourceGuardEntry.setIndexNames(
    (0, "ZXR10-SWITCH-MIB", "dhcpIpSourceGuardSlot"),
    (0, "ZXR10-SWITCH-MIB", "dhcpIpSourceGuardPort"),
)
if mibBuilder.loadTexts:
    dhcpIpSourceGuardEntry.setStatus("current")
_DhcpIpSourceGuardSlot_Type = Integer32
_DhcpIpSourceGuardSlot_Object = MibTableColumn
dhcpIpSourceGuardSlot = _DhcpIpSourceGuardSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 23, 2, 1, 1),
    _DhcpIpSourceGuardSlot_Type()
)
dhcpIpSourceGuardSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpIpSourceGuardSlot.setStatus("current")
_DhcpIpSourceGuardPort_Type = Integer32
_DhcpIpSourceGuardPort_Object = MibTableColumn
dhcpIpSourceGuardPort = _DhcpIpSourceGuardPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 23, 2, 1, 2),
    _DhcpIpSourceGuardPort_Type()
)
dhcpIpSourceGuardPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpIpSourceGuardPort.setStatus("current")


class _DhcpIpSourceGuardControl_Type(Integer32):
    """Custom type dhcpIpSourceGuardControl based on Integer32"""
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
        *(("disable", 0),
          ("ip-base", 1),
          ("mac-base", 2),
          ("mac-ip-base", 3))
    )


_DhcpIpSourceGuardControl_Type.__name__ = "Integer32"
_DhcpIpSourceGuardControl_Object = MibTableColumn
dhcpIpSourceGuardControl = _DhcpIpSourceGuardControl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 23, 2, 1, 3),
    _DhcpIpSourceGuardControl_Type()
)
dhcpIpSourceGuardControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpIpSourceGuardControl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-SWITCH-MIB",
    **{"DisplayString": DisplayString,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10switch": zxr10switch,
       "zxr10vlan": zxr10vlan,
       "zxr10CpuVlanPvidTable": zxr10CpuVlanPvidTable,
       "zxr10CpuVlanPvidEntry": zxr10CpuVlanPvidEntry,
       "zxr10CpuVlanId": zxr10CpuVlanId,
       "zxr10CpuVlanIf": zxr10CpuVlanIf,
       "zxr10CpuVlanMtu": zxr10CpuVlanMtu,
       "zxr10CpuVlanState": zxr10CpuVlanState,
       "zxr10CpuVlanSaid": zxr10CpuVlanSaid,
       "zxr10CpuVlanVpnid": zxr10CpuVlanVpnid,
       "zxr10CpuVlanRowStatus": zxr10CpuVlanRowStatus,
       "zxr10CpuVlanName": zxr10CpuVlanName,
       "zxr10CpuVlanMemPortsPvid": zxr10CpuVlanMemPortsPvid,
       "zxr10CpuVlanTagTable": zxr10CpuVlanTagTable,
       "zxr10CpuVlanTagEntry": zxr10CpuVlanTagEntry,
       "zxr10CpuVlanid": zxr10CpuVlanid,
       "zxr10CpuVlanvpnid": zxr10CpuVlanvpnid,
       "zxr10CpuVlanname": zxr10CpuVlanname,
       "zxr10CpuVlanMemPortsTag": zxr10CpuVlanMemPortsTag,
       "zxr10QinQ": zxr10QinQ,
       "zxr10QinQTable": zxr10QinQTable,
       "zxr10QinQEntry": zxr10QinQEntry,
       "zxr10QinQPortName": zxr10QinQPortName,
       "zxr10QinQMode": zxr10QinQMode,
       "zxr10QinQTpid": zxr10QinQTpid,
       "zxr10QinQPvid": zxr10QinQPvid,
       "zxr10QinQExtendTpid": zxr10QinQExtendTpid,
       "zxr10QinQStandardTpid": zxr10QinQStandardTpid,
       "zxr10MemberShip": zxr10MemberShip,
       "zxr10MemberShipTable": zxr10MemberShipTable,
       "zxr10MemberShipEntry": zxr10MemberShipEntry,
       "zxr10MemberShipPortName": zxr10MemberShipPortName,
       "zxr10MemberShipPvid": zxr10MemberShipPvid,
       "zxr10MemberShipMode": zxr10MemberShipMode,
       "zxr10MemberShipVlansTag": zxr10MemberShipVlansTag,
       "zxr10MemberShipVlansHybridUnTag": zxr10MemberShipVlansHybridUnTag,
       "zxr10MemberShipVlansTag2k": zxr10MemberShipVlansTag2k,
       "zxr10MemberShipVlansHybridUnTag2k": zxr10MemberShipVlansHybridUnTag2k,
       "zxr10MemberShipVlansTag3k": zxr10MemberShipVlansTag3k,
       "zxr10MemberShipVlansHybridUnTag3k": zxr10MemberShipVlansHybridUnTag3k,
       "zxr10MemberShipVlansTag4k": zxr10MemberShipVlansTag4k,
       "zxr10MemberShipVlansHybridUnTag4k": zxr10MemberShipVlansHybridUnTag4k,
       "zxr10CpuVlanUntagTable": zxr10CpuVlanUntagTable,
       "zxr10CpuVlanUntagEntry": zxr10CpuVlanUntagEntry,
       "zxr10Cpuvlanid": zxr10Cpuvlanid,
       "zxr10CpuVlanvpnId": zxr10CpuVlanvpnId,
       "zxr10Cpuvlanname": zxr10Cpuvlanname,
       "zxr10CpuVlanMemPortsUntag": zxr10CpuVlanMemPortsUntag,
       "zxr10igmpSnooping": zxr10igmpSnooping,
       "zxr10IgmpSnoopingTable": zxr10IgmpSnoopingTable,
       "zxr10IgmpSnoopingEntry": zxr10IgmpSnoopingEntry,
       "zxr10igmpSnoopingValid": zxr10igmpSnoopingValid,
       "zxr10igmpSnoopingVlanId": zxr10igmpSnoopingVlanId,
       "zxr10igmpSnoopingGroupId": zxr10igmpSnoopingGroupId,
       "zxr10igmpSnoopingDropEnable": zxr10igmpSnoopingDropEnable,
       "zxr10igmpSnoopingMaxHostNum": zxr10igmpSnoopingMaxHostNum,
       "zxr10igmpSnoopingIpAddr": zxr10igmpSnoopingIpAddr,
       "zxr10igmpSnoopingGroupMac": zxr10igmpSnoopingGroupMac,
       "zxr10igmpSnoopingMemPorts0": zxr10igmpSnoopingMemPorts0,
       "zxr10igmpSnoopingMemPorts1": zxr10igmpSnoopingMemPorts1,
       "zxr10igmpSnoopingMemPorts2": zxr10igmpSnoopingMemPorts2,
       "zxr10igmpSnoopingMemPorts3": zxr10igmpSnoopingMemPorts3,
       "zxr10igmpSnoopingMemPorts4": zxr10igmpSnoopingMemPorts4,
       "zxr10igmpSnoopingMemPorts5": zxr10igmpSnoopingMemPorts5,
       "zxr10igmpSnoopingMemPorts6": zxr10igmpSnoopingMemPorts6,
       "zxr10igmpSnoopingMemPorts7": zxr10igmpSnoopingMemPorts7,
       "zxr10igmpSnoopingMemPorts8": zxr10igmpSnoopingMemPorts8,
       "zxr10igmpSnoopingMemPorts9": zxr10igmpSnoopingMemPorts9,
       "zxr10igmpSnoopingMemPorts10": zxr10igmpSnoopingMemPorts10,
       "zxr10igmpSnoopingMemPorts11": zxr10igmpSnoopingMemPorts11,
       "zxr10igmpSnoopingMemPorts12": zxr10igmpSnoopingMemPorts12,
       "zxr10pimSnoopingMemPorts0": zxr10pimSnoopingMemPorts0,
       "zxr10pimSnoopingMemPorts1": zxr10pimSnoopingMemPorts1,
       "zxr10pimSnoopingMemPorts2": zxr10pimSnoopingMemPorts2,
       "zxr10pimSnoopingMemPorts3": zxr10pimSnoopingMemPorts3,
       "zxr10pimSnoopingMemPorts4": zxr10pimSnoopingMemPorts4,
       "zxr10pimSnoopingMemPorts5": zxr10pimSnoopingMemPorts5,
       "zxr10pimSnoopingMemPorts6": zxr10pimSnoopingMemPorts6,
       "zxr10pimSnoopingMemPorts7": zxr10pimSnoopingMemPorts7,
       "zxr10pimSnoopingMemPorts8": zxr10pimSnoopingMemPorts8,
       "zxr10pimSnoopingMemPorts9": zxr10pimSnoopingMemPorts9,
       "zxr10pimSnoopingMemPorts10": zxr10pimSnoopingMemPorts10,
       "zxr10pimSnoopingMemPorts11": zxr10pimSnoopingMemPorts11,
       "zxr10pimSnoopingMemPorts12": zxr10pimSnoopingMemPorts12,
       "zxr10PimSnoopingNeighborTable": zxr10PimSnoopingNeighborTable,
       "zxr10PimSnoopingNeighborEntry": zxr10PimSnoopingNeighborEntry,
       "zxr10pimSnoopingNeighborValid": zxr10pimSnoopingNeighborValid,
       "zxr10pimSnoopingNeighborVlanId": zxr10pimSnoopingNeighborVlanId,
       "zxr10pimSnoopingNeighborVpnId": zxr10pimSnoopingNeighborVpnId,
       "zxr10pimSnoopingNeighborId": zxr10pimSnoopingNeighborId,
       "zxr10pimSnoopingNeighborSourceIpAddr": zxr10pimSnoopingNeighborSourceIpAddr,
       "zxr10pimSnoopingNeighborPort": zxr10pimSnoopingNeighborPort,
       "zxr10IgmpSnoopingVlanTable": zxr10IgmpSnoopingVlanTable,
       "zxr10IgmpSnoopingVlanEntry": zxr10IgmpSnoopingVlanEntry,
       "zxr10igmpSnoopingVlanEntryVlanId": zxr10igmpSnoopingVlanEntryVlanId,
       "zxr10igmpSnoopingVlanEntryEnable": zxr10igmpSnoopingVlanEntryEnable,
       "zxr10pimSnoopingVlanEntryEnable": zxr10pimSnoopingVlanEntryEnable,
       "zxr10igmpSnoopingFastLeave": zxr10igmpSnoopingFastLeave,
       "zxr10igmpSnoopingLastMemberQueryInterval": zxr10igmpSnoopingLastMemberQueryInterval,
       "zxr10igmpSnoopingMaxGroupNum": zxr10igmpSnoopingMaxGroupNum,
       "zxr10igmpSnoopingGroupNum": zxr10igmpSnoopingGroupNum,
       "zxr10igmpSnoopingHostTimeOut": zxr10igmpSnoopingHostTimeOut,
       "zxr10igmpSnoopingMrTimeOut": zxr10igmpSnoopingMrTimeOut,
       "zxr10igmpSnoopingEnable": zxr10igmpSnoopingEnable,
       "zxr10pimSnoopingEnable": zxr10pimSnoopingEnable,
       "zxr10igmpSnoopingGlobalQuery": zxr10igmpSnoopingGlobalQuery,
       "zxr10igmpSnoopingQueryInterval": zxr10igmpSnoopingQueryInterval,
       "zxr10igmpSnoopingQueryResponseInterval": zxr10igmpSnoopingQueryResponseInterval,
       "zxr10extAlarm": zxr10extAlarm,
       "zxr10InputAlarmTable": zxr10InputAlarmTable,
       "zxr10InputAlarmEntry": zxr10InputAlarmEntry,
       "zxr10InputAlarmIndex": zxr10InputAlarmIndex,
       "zxr10InputAlarmStatus": zxr10InputAlarmStatus,
       "zxr10InputAlarmDescription": zxr10InputAlarmDescription,
       "zxr10OutputAlarmTable": zxr10OutputAlarmTable,
       "zxr10OutputAlarmEntry": zxr10OutputAlarmEntry,
       "zxr10OutputAlarmIndex": zxr10OutputAlarmIndex,
       "zxr10OutputAlarmStatus": zxr10OutputAlarmStatus,
       "zxr10OutputAlarmDescription": zxr10OutputAlarmDescription,
       "zess": zess,
       "zessClearAllChangeTimes": zessClearAllChangeTimes,
       "zessDomainTable": zessDomainTable,
       "zessDomainEntry": zessDomainEntry,
       "zessDomainId": zessDomainId,
       "zessProtectInstanceId": zessProtectInstanceId,
       "zessPrimaryPort": zessPrimaryPort,
       "zessSecondaryPort": zessSecondaryPort,
       "zessPreupDelayTime": zessPreupDelayTime,
       "zessDomainMode": zessDomainMode,
       "zessDomainState": zessDomainState,
       "zessPriIfState": zessPriIfState,
       "zessSecIfState": zessSecIfState,
       "zessChangeTimes": zessChangeTimes,
       "zessClearChangeTimes": zessClearChangeTimes,
       "zessDomainRowStatus": zessDomainRowStatus,
       "vct": vct,
       "vctPortTable": vctPortTable,
       "vctPortEntry": vctPortEntry,
       "vctPortName": vctPortName,
       "vctIsValid": vctIsValid,
       "vctCableStatus": vctCableStatus,
       "vctPair1Result": vctPair1Result,
       "vctPair1Lenth": vctPair1Lenth,
       "vctPair2Result": vctPair2Result,
       "vctPair2Lenth": vctPair2Lenth,
       "vctPair3Result": vctPair3Result,
       "vctPair3Lenth": vctPair3Lenth,
       "vctPair4Result": vctPair4Result,
       "vctPair4Lenth": vctPair4Lenth,
       "vctRowStatus": vctRowStatus,
       "vctTable": vctTable,
       "vctEntry": vctEntry,
       "vctIfindex": vctIfindex,
       "vctSetIfindex": vctSetIfindex,
       "cableStatus": cableStatus,
       "doubleCableStatus1-2": doubleCableStatus1_2,
       "doubleCableStatus3-6": doubleCableStatus3_6,
       "doubleCableStatus4-5": doubleCableStatus4_5,
       "doubleCableStatus7-8": doubleCableStatus7_8,
       "doubleCableLength1-2": doubleCableLength1_2,
       "doubleCableLength3-6": doubleCableLength3_6,
       "doubleCableLength4-5": doubleCableLength4_5,
       "doubleCableLength7-8": doubleCableLength7_8,
       "loopdetect": loopdetect,
       "loopdetectReopenTime": loopdetectReopenTime,
       "loopdetectTable": loopdetectTable,
       "loopdetectEntry": loopdetectEntry,
       "loopdetectPanelNum": loopdetectPanelNum,
       "loopdetectPortNum": loopdetectPortNum,
       "loopdetectPortName": loopdetectPortName,
       "loopdetectPortOperStatus": loopdetectPortOperStatus,
       "loopdetectPortVlan": loopdetectPortVlan,
       "loopdetectPortMonitor": loopdetectPortMonitor,
       "loopdetectPortRowStatus": loopdetectPortRowStatus,
       "svlan": svlan,
       "zxr10svlanCount": zxr10svlanCount,
       "zxr10svlanFreeCount": zxr10svlanFreeCount,
       "zxr10svlanTable": zxr10svlanTable,
       "zxr10svlanEntry": zxr10svlanEntry,
       "zxr10svlanSessionNo": zxr10svlanSessionNo,
       "zxr10svlanDescription": zxr10svlanDescription,
       "zxr10svlanCustomerPort": zxr10svlanCustomerPort,
       "zxr10svlanUplinkPort": zxr10svlanUplinkPort,
       "zxr10svlanInvlan": zxr10svlanInvlan,
       "zxr10svlanOvlan": zxr10svlanOvlan,
       "zxr10svlanRedirect": zxr10svlanRedirect,
       "zxr10svlanAdvanced": zxr10svlanAdvanced,
       "zxr10svlanPriority": zxr10svlanPriority,
       "zxr10svlanHelperVlan": zxr10svlanHelperVlan,
       "vfp": vfp,
       "zxr10vfpTable": zxr10vfpTable,
       "zxr10vfpEntry": zxr10vfpEntry,
       "zxr10vfpInterfaceName": zxr10vfpInterfaceName,
       "zxr10vfpSessionId": zxr10vfpSessionId,
       "zxr10vfpDescription": zxr10vfpDescription,
       "zxr10vfpInVlan": zxr10vfpInVlan,
       "zxr10vfpAclNO": zxr10vfpAclNO,
       "zxr10vfpRuleNo": zxr10vfpRuleNo,
       "zxr10vfpOvlan": zxr10vfpOvlan,
       "zxr10vfpPriority": zxr10vfpPriority,
       "zxr10vfpUntagAppFlag": zxr10vfpUntagAppFlag,
       "zxr10vfpClassId": zxr10vfpClassId,
       "zxr10vfpVrfId": zxr10vfpVrfId,
       "dhcp": dhcp,
       "dhcpIpSourceGuardIfNumber": dhcpIpSourceGuardIfNumber,
       "dhcpIpSourceGuardTable": dhcpIpSourceGuardTable,
       "dhcpIpSourceGuardEntry": dhcpIpSourceGuardEntry,
       "dhcpIpSourceGuardSlot": dhcpIpSourceGuardSlot,
       "dhcpIpSourceGuardPort": dhcpIpSourceGuardPort,
       "dhcpIpSourceGuardControl": dhcpIpSourceGuardControl}
)
