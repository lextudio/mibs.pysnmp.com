# SNMP MIB module (SW-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:59 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class VlanIndex(Integer32):
    """Custom type VlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Marconi_ObjectIdentity = ObjectIdentity
marconi = _Marconi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_External_ObjectIdentity = ObjectIdentity
external = _External_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20)
)
_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1)
)
_Dlinkcommon_ObjectIdentity = ObjectIdentity
dlinkcommon = _Dlinkcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1)
)
_Golf_ObjectIdentity = ObjectIdentity
golf = _Golf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2)
)
_Golfproducts_ObjectIdentity = ObjectIdentity
golfproducts = _Golfproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1)
)
_Es2000_ObjectIdentity = ObjectIdentity
es2000 = _Es2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3)
)
_Golfcommon_ObjectIdentity = ObjectIdentity
golfcommon = _Golfcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2)
)
_Marconi_mgmt_ObjectIdentity = ObjectIdentity
marconi_mgmt = _Marconi_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)
)
_Es2000Mgmt_ObjectIdentity = ObjectIdentity
es2000Mgmt = _Es2000Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28)
)
_SwL2Mgmt_ObjectIdentity = ObjectIdentity
swL2Mgmt = _SwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2)
)
_SwVlan_ObjectIdentity = ObjectIdentity
swVlan = _SwVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8)
)
_SwVlanCtrl_ObjectIdentity = ObjectIdentity
swVlanCtrl = _SwVlanCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 1)
)


class _SwVlanCtrlMode_Type(Integer32):
    """Custom type swVlanCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("ieee8021q", 4),
          ("mac-base", 3),
          ("other", 1),
          ("port-base", 5))
    )


_SwVlanCtrlMode_Type.__name__ = "Integer32"
_SwVlanCtrlMode_Object = MibScalar
swVlanCtrlMode = _SwVlanCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 1, 1),
    _SwVlanCtrlMode_Type()
)
swVlanCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVlanCtrlMode.setStatus("mandatory")


class _SwVlanInfoStatus_Type(Integer32):
    """Custom type swVlanInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("ieee8021q", 4),
          ("mac-base", 3),
          ("other", 1),
          ("port-base", 5))
    )


_SwVlanInfoStatus_Type.__name__ = "Integer32"
_SwVlanInfoStatus_Object = MibScalar
swVlanInfoStatus = _SwVlanInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 1, 2),
    _SwVlanInfoStatus_Type()
)
swVlanInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVlanInfoStatus.setStatus("mandatory")
_SwVlanSnmpPortVlan_Type = VlanIndex
_SwVlanSnmpPortVlan_Object = MibScalar
swVlanSnmpPortVlan = _SwVlanSnmpPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 1, 3),
    _SwVlanSnmpPortVlan_Type()
)
swVlanSnmpPortVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVlanSnmpPortVlan.setStatus("mandatory")
_SwMacBaseVlan_ObjectIdentity = ObjectIdentity
swMacBaseVlan = _SwMacBaseVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2)
)
_SwMacBaseVlanInfo_ObjectIdentity = ObjectIdentity
swMacBaseVlanInfo = _SwMacBaseVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 1)
)
_SwMacBaseVlanMaxNum_Type = Integer32
_SwMacBaseVlanMaxNum_Object = MibScalar
swMacBaseVlanMaxNum = _SwMacBaseVlanMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 1, 1),
    _SwMacBaseVlanMaxNum_Type()
)
swMacBaseVlanMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanMaxNum.setStatus("mandatory")
_SwMacBaseVlanAddrMaxNum_Type = Integer32
_SwMacBaseVlanAddrMaxNum_Object = MibScalar
swMacBaseVlanAddrMaxNum = _SwMacBaseVlanAddrMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 1, 2),
    _SwMacBaseVlanAddrMaxNum_Type()
)
swMacBaseVlanAddrMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanAddrMaxNum.setStatus("mandatory")
_SwMacBaseVlanCtrlTable_Object = MibTable
swMacBaseVlanCtrlTable = _SwMacBaseVlanCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 2)
)
if mibBuilder.loadTexts:
    swMacBaseVlanCtrlTable.setStatus("mandatory")
_SwMacBaseVlanCtrlEntry_Object = MibTableRow
swMacBaseVlanCtrlEntry = _SwMacBaseVlanCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 2, 1)
)
swMacBaseVlanCtrlEntry.setIndexNames(
    (0, "SW-VLAN-MIB", "swMacBaseVlanDesc"),
)
if mibBuilder.loadTexts:
    swMacBaseVlanCtrlEntry.setStatus("mandatory")


class _SwMacBaseVlanDesc_Type(DisplayString):
    """Custom type swMacBaseVlanDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwMacBaseVlanDesc_Type.__name__ = "DisplayString"
_SwMacBaseVlanDesc_Object = MibTableColumn
swMacBaseVlanDesc = _SwMacBaseVlanDesc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 2, 1, 1),
    _SwMacBaseVlanDesc_Type()
)
swMacBaseVlanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanDesc.setStatus("mandatory")
_SwMacBaseVlanMacMember_Type = Integer32
_SwMacBaseVlanMacMember_Object = MibTableColumn
swMacBaseVlanMacMember = _SwMacBaseVlanMacMember_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 2, 1, 2),
    _SwMacBaseVlanMacMember_Type()
)
swMacBaseVlanMacMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanMacMember.setStatus("mandatory")


class _SwMacBaseVlanCtrlState_Type(Integer32):
    """Custom type swMacBaseVlanCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMacBaseVlanCtrlState_Type.__name__ = "Integer32"
_SwMacBaseVlanCtrlState_Object = MibTableColumn
swMacBaseVlanCtrlState = _SwMacBaseVlanCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 2, 1, 3),
    _SwMacBaseVlanCtrlState_Type()
)
swMacBaseVlanCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBaseVlanCtrlState.setStatus("mandatory")
_SwMacBaseVlanAddrTable_Object = MibTable
swMacBaseVlanAddrTable = _SwMacBaseVlanAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 3)
)
if mibBuilder.loadTexts:
    swMacBaseVlanAddrTable.setStatus("mandatory")
_SwMacBaseVlanAddrEntry_Object = MibTableRow
swMacBaseVlanAddrEntry = _SwMacBaseVlanAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 3, 1)
)
swMacBaseVlanAddrEntry.setIndexNames(
    (0, "SW-VLAN-MIB", "swMacBaseVlanAddr"),
)
if mibBuilder.loadTexts:
    swMacBaseVlanAddrEntry.setStatus("mandatory")
_SwMacBaseVlanAddr_Type = MacAddress
_SwMacBaseVlanAddr_Object = MibTableColumn
swMacBaseVlanAddr = _SwMacBaseVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 3, 1, 1),
    _SwMacBaseVlanAddr_Type()
)
swMacBaseVlanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanAddr.setStatus("mandatory")


class _SwMacBaseVlanAddrVlanDesc_Type(DisplayString):
    """Custom type swMacBaseVlanAddrVlanDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SwMacBaseVlanAddrVlanDesc_Type.__name__ = "DisplayString"
_SwMacBaseVlanAddrVlanDesc_Object = MibTableColumn
swMacBaseVlanAddrVlanDesc = _SwMacBaseVlanAddrVlanDesc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 3, 1, 2),
    _SwMacBaseVlanAddrVlanDesc_Type()
)
swMacBaseVlanAddrVlanDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBaseVlanAddrVlanDesc.setStatus("mandatory")


class _SwMacBaseVlanAddrState_Type(Integer32):
    """Custom type swMacBaseVlanAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwMacBaseVlanAddrState_Type.__name__ = "Integer32"
_SwMacBaseVlanAddrState_Object = MibTableColumn
swMacBaseVlanAddrState = _SwMacBaseVlanAddrState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 3, 1, 3),
    _SwMacBaseVlanAddrState_Type()
)
swMacBaseVlanAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBaseVlanAddrState.setStatus("mandatory")


class _SwMacBaseVlanAddrStatus_Type(Integer32):
    """Custom type swMacBaseVlanAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("not-apply", 3),
          ("other", 1))
    )


_SwMacBaseVlanAddrStatus_Type.__name__ = "Integer32"
_SwMacBaseVlanAddrStatus_Object = MibTableColumn
swMacBaseVlanAddrStatus = _SwMacBaseVlanAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 2, 3, 1, 4),
    _SwMacBaseVlanAddrStatus_Type()
)
swMacBaseVlanAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBaseVlanAddrStatus.setStatus("mandatory")
_SwPortBaseVlan_ObjectIdentity = ObjectIdentity
swPortBaseVlan = _SwPortBaseVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3)
)
_SwPortBaseVlanTotalNum_Type = Integer32
_SwPortBaseVlanTotalNum_Object = MibScalar
swPortBaseVlanTotalNum = _SwPortBaseVlanTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 1),
    _SwPortBaseVlanTotalNum_Type()
)
swPortBaseVlanTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanTotalNum.setStatus("mandatory")
_SwPortBaseVlanDefaultVlanTable_Object = MibTable
swPortBaseVlanDefaultVlanTable = _SwPortBaseVlanDefaultVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultVlanTable.setStatus("mandatory")
_SwPortBaseVlanDefaultVlanEntry_Object = MibTableRow
swPortBaseVlanDefaultVlanEntry = _SwPortBaseVlanDefaultVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 2, 1)
)
swPortBaseVlanDefaultVlanEntry.setIndexNames(
    (0, "SW-VLAN-MIB", "swPortBaseVlanDefaultPvid"),
)
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultVlanEntry.setStatus("mandatory")
_SwPortBaseVlanDefaultPvid_Type = Integer32
_SwPortBaseVlanDefaultPvid_Object = MibTableColumn
swPortBaseVlanDefaultPvid = _SwPortBaseVlanDefaultPvid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 2, 1, 1),
    _SwPortBaseVlanDefaultPvid_Type()
)
swPortBaseVlanDefaultPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultPvid.setStatus("mandatory")


class _SwPortBaseVlanDefaultDesc_Type(DisplayString):
    """Custom type swPortBaseVlanDefaultDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwPortBaseVlanDefaultDesc_Type.__name__ = "DisplayString"
_SwPortBaseVlanDefaultDesc_Object = MibTableColumn
swPortBaseVlanDefaultDesc = _SwPortBaseVlanDefaultDesc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 2, 1, 2),
    _SwPortBaseVlanDefaultDesc_Type()
)
swPortBaseVlanDefaultDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultDesc.setStatus("mandatory")
_SwPortBaseVlanDefaultPortList_Type = PortList
_SwPortBaseVlanDefaultPortList_Object = MibTableColumn
swPortBaseVlanDefaultPortList = _SwPortBaseVlanDefaultPortList_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 2, 1, 3),
    _SwPortBaseVlanDefaultPortList_Type()
)
swPortBaseVlanDefaultPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultPortList.setStatus("mandatory")
_SwPortBaseVlanDefaultPortNumber_Type = Integer32
_SwPortBaseVlanDefaultPortNumber_Object = MibTableColumn
swPortBaseVlanDefaultPortNumber = _SwPortBaseVlanDefaultPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 2, 1, 4),
    _SwPortBaseVlanDefaultPortNumber_Type()
)
swPortBaseVlanDefaultPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanDefaultPortNumber.setStatus("mandatory")
_SwPortBaseVlanConfigTable_Object = MibTable
swPortBaseVlanConfigTable = _SwPortBaseVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 3)
)
if mibBuilder.loadTexts:
    swPortBaseVlanConfigTable.setStatus("mandatory")
_SwPortBaseVlanConfigEntry_Object = MibTableRow
swPortBaseVlanConfigEntry = _SwPortBaseVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 3, 1)
)
swPortBaseVlanConfigEntry.setIndexNames(
    (0, "SW-VLAN-MIB", "swPortBaseVlanConfigPvid"),
)
if mibBuilder.loadTexts:
    swPortBaseVlanConfigEntry.setStatus("mandatory")


class _SwPortBaseVlanConfigPvid_Type(Integer32):
    """Custom type swPortBaseVlanConfigPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 12),
    )


_SwPortBaseVlanConfigPvid_Type.__name__ = "Integer32"
_SwPortBaseVlanConfigPvid_Object = MibTableColumn
swPortBaseVlanConfigPvid = _SwPortBaseVlanConfigPvid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 3, 1, 1),
    _SwPortBaseVlanConfigPvid_Type()
)
swPortBaseVlanConfigPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanConfigPvid.setStatus("mandatory")


class _SwPortBaseVlanConfigDesc_Type(DisplayString):
    """Custom type swPortBaseVlanConfigDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwPortBaseVlanConfigDesc_Type.__name__ = "DisplayString"
_SwPortBaseVlanConfigDesc_Object = MibTableColumn
swPortBaseVlanConfigDesc = _SwPortBaseVlanConfigDesc_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 3, 1, 2),
    _SwPortBaseVlanConfigDesc_Type()
)
swPortBaseVlanConfigDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBaseVlanConfigDesc.setStatus("mandatory")
_SwPortBaseVlanConfigPortList_Type = PortList
_SwPortBaseVlanConfigPortList_Object = MibTableColumn
swPortBaseVlanConfigPortList = _SwPortBaseVlanConfigPortList_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 3, 1, 3),
    _SwPortBaseVlanConfigPortList_Type()
)
swPortBaseVlanConfigPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortBaseVlanConfigPortList.setStatus("mandatory")
_SwPortBaseVlanConfigPortNumber_Type = Integer32
_SwPortBaseVlanConfigPortNumber_Object = MibTableColumn
swPortBaseVlanConfigPortNumber = _SwPortBaseVlanConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 8, 3, 3, 1, 4),
    _SwPortBaseVlanConfigPortNumber_Type()
)
swPortBaseVlanConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBaseVlanConfigPortNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-VLAN-MIB",
    **{"MacAddress": MacAddress,
       "VlanIndex": VlanIndex,
       "PortList": PortList,
       "marconi": marconi,
       "systems": systems,
       "external": external,
       "dlink": dlink,
       "dlinkcommon": dlinkcommon,
       "golf": golf,
       "golfproducts": golfproducts,
       "es2000": es2000,
       "golfcommon": golfcommon,
       "marconi-mgmt": marconi_mgmt,
       "es2000Mgmt": es2000Mgmt,
       "swL2Mgmt": swL2Mgmt,
       "swVlan": swVlan,
       "swVlanCtrl": swVlanCtrl,
       "swVlanCtrlMode": swVlanCtrlMode,
       "swVlanInfoStatus": swVlanInfoStatus,
       "swVlanSnmpPortVlan": swVlanSnmpPortVlan,
       "swMacBaseVlan": swMacBaseVlan,
       "swMacBaseVlanInfo": swMacBaseVlanInfo,
       "swMacBaseVlanMaxNum": swMacBaseVlanMaxNum,
       "swMacBaseVlanAddrMaxNum": swMacBaseVlanAddrMaxNum,
       "swMacBaseVlanCtrlTable": swMacBaseVlanCtrlTable,
       "swMacBaseVlanCtrlEntry": swMacBaseVlanCtrlEntry,
       "swMacBaseVlanDesc": swMacBaseVlanDesc,
       "swMacBaseVlanMacMember": swMacBaseVlanMacMember,
       "swMacBaseVlanCtrlState": swMacBaseVlanCtrlState,
       "swMacBaseVlanAddrTable": swMacBaseVlanAddrTable,
       "swMacBaseVlanAddrEntry": swMacBaseVlanAddrEntry,
       "swMacBaseVlanAddr": swMacBaseVlanAddr,
       "swMacBaseVlanAddrVlanDesc": swMacBaseVlanAddrVlanDesc,
       "swMacBaseVlanAddrState": swMacBaseVlanAddrState,
       "swMacBaseVlanAddrStatus": swMacBaseVlanAddrStatus,
       "swPortBaseVlan": swPortBaseVlan,
       "swPortBaseVlanTotalNum": swPortBaseVlanTotalNum,
       "swPortBaseVlanDefaultVlanTable": swPortBaseVlanDefaultVlanTable,
       "swPortBaseVlanDefaultVlanEntry": swPortBaseVlanDefaultVlanEntry,
       "swPortBaseVlanDefaultPvid": swPortBaseVlanDefaultPvid,
       "swPortBaseVlanDefaultDesc": swPortBaseVlanDefaultDesc,
       "swPortBaseVlanDefaultPortList": swPortBaseVlanDefaultPortList,
       "swPortBaseVlanDefaultPortNumber": swPortBaseVlanDefaultPortNumber,
       "swPortBaseVlanConfigTable": swPortBaseVlanConfigTable,
       "swPortBaseVlanConfigEntry": swPortBaseVlanConfigEntry,
       "swPortBaseVlanConfigPvid": swPortBaseVlanConfigPvid,
       "swPortBaseVlanConfigDesc": swPortBaseVlanConfigDesc,
       "swPortBaseVlanConfigPortList": swPortBaseVlanConfigPortList,
       "swPortBaseVlanConfigPortNumber": swPortBaseVlanConfigPortNumber}
)
