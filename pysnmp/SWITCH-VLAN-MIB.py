# SNMP MIB module (SWITCH-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWITCH-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:14 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(vLanModule,) = mibBuilder.importSymbols(
    "TELESYN-ATI-TC",
    "vLanModule")


# MODULE-IDENTITY

switchVlanMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2)
)
switchVlanMib.setRevisions(
        ("1997-04-10 16:00",
         "1997-02-12 16:00",
         "1996-11-07 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmVci(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )



class VlanAdminStatusCode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )



class VlanOperStatusCode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )



class VlanMode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atmCIP", 4),
          ("standard", 3),
          ("unknown", 1))
    )



class PortFuncCode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("atmLane", 5),
          ("atmMux", 6),
          ("bridge", 3),
          ("cip", 7),
          ("pt2Pt", 8),
          ("router", 2),
          ("trunk", 4),
          ("unknown", 1))
    )



class MACLayerCode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("fddi", 5),
          ("ieee802d3", 3),
          ("ieee802d5", 4),
          ("none", 1),
          ("unknown", 0))
    )



class PhyPortMediaTypeCode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("atm25", 9),
          ("atm50", 10),
          ("cddi", 8),
          ("ds1", 11),
          ("ds3", 12),
          ("eth10", 3),
          ("eth100", 4),
          ("eth100F", 17),
          ("fddi", 7),
          ("oc12", 14),
          ("oc3", 13),
          ("oc48", 15),
          ("other", 2),
          ("tr16", 6),
          ("tr4", 5),
          ("unknown", 1),
          ("wan", 16))
    )



# MIB Managed Objects in the order of their OIDs

_VLanGroup_ObjectIdentity = ObjectIdentity
vLanGroup = _VLanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1)
)
_VLanTable_Object = MibTable
vLanTable = _VLanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vLanTable.setStatus("current")
_VLanEntry_Object = MibTableRow
vLanEntry = _VLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1, 1, 1)
)
vLanEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "vLanNumber"),
)
if mibBuilder.loadTexts:
    vLanEntry.setStatus("current")


class _VLanNumber_Type(Integer32):
    """Custom type vLanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VLanNumber_Type.__name__ = "Integer32"
_VLanNumber_Object = MibTableColumn
vLanNumber = _VLanNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1, 1, 1, 1),
    _VLanNumber_Type()
)
vLanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLanNumber.setStatus("current")


class _VLanMembers_Type(OctetString):
    """Custom type vLanMembers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_VLanMembers_Type.__name__ = "OctetString"
_VLanMembers_Object = MibTableColumn
vLanMembers = _VLanMembers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1, 1, 1, 2),
    _VLanMembers_Type()
)
vLanMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLanMembers.setStatus("current")


class _VLanDescription_Type(DisplayString):
    """Custom type vLanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VLanDescription_Type.__name__ = "DisplayString"
_VLanDescription_Object = MibTableColumn
vLanDescription = _VLanDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1, 1, 1, 5),
    _VLanDescription_Type()
)
vLanDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vLanDescription.setStatus("current")
_VLanAdminStatus_Type = VlanAdminStatusCode
_VLanAdminStatus_Object = MibTableColumn
vLanAdminStatus = _VLanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1, 1, 1, 6),
    _VLanAdminStatus_Type()
)
vLanAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vLanAdminStatus.setStatus("current")
_VLanOperStatus_Type = VlanOperStatusCode
_VLanOperStatus_Object = MibTableColumn
vLanOperStatus = _VLanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1, 1, 1, 7),
    _VLanOperStatus_Type()
)
vLanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLanOperStatus.setStatus("current")
_VLanMode_Type = VlanMode
_VLanMode_Object = MibTableColumn
vLanMode = _VLanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1, 1, 1, 8),
    _VLanMode_Type()
)
vLanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vLanMode.setStatus("deprecated")
_VLanRowStatus_Type = RowStatus
_VLanRowStatus_Object = MibTableColumn
vLanRowStatus = _VLanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 1, 1, 1, 9),
    _VLanRowStatus_Type()
)
vLanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vLanRowStatus.setStatus("current")
_VRouterGroup_ObjectIdentity = ObjectIdentity
vRouterGroup = _VRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2)
)
_VRouterTable_Object = MibTable
vRouterTable = _VRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vRouterTable.setStatus("current")
_VRouterEntry_Object = MibTableRow
vRouterEntry = _VRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1)
)
vRouterEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "vLanNumber"),
)
if mibBuilder.loadTexts:
    vRouterEntry.setStatus("current")


class _VRouterProtocol_Type(Integer32):
    """Custom type vRouterProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRouterProtocol_Type.__name__ = "Integer32"
_VRouterProtocol_Object = MibTableColumn
vRouterProtocol = _VRouterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 1),
    _VRouterProtocol_Type()
)
vRouterProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRouterProtocol.setStatus("current")
_VRouterIpAddress_Type = IpAddress
_VRouterIpAddress_Object = MibTableColumn
vRouterIpAddress = _VRouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 2),
    _VRouterIpAddress_Type()
)
vRouterIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRouterIpAddress.setStatus("current")
_VRouterSubNetMask_Type = IpAddress
_VRouterSubNetMask_Object = MibTableColumn
vRouterSubNetMask = _VRouterSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 3),
    _VRouterSubNetMask_Type()
)
vRouterSubNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRouterSubNetMask.setStatus("current")
_VRouterBcastAddress_Type = IpAddress
_VRouterBcastAddress_Object = MibTableColumn
vRouterBcastAddress = _VRouterBcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 4),
    _VRouterBcastAddress_Type()
)
vRouterBcastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRouterBcastAddress.setStatus("current")


class _VRouterDescription_Type(DisplayString):
    """Custom type vRouterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VRouterDescription_Type.__name__ = "DisplayString"
_VRouterDescription_Object = MibTableColumn
vRouterDescription = _VRouterDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 5),
    _VRouterDescription_Type()
)
vRouterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRouterDescription.setStatus("current")
_VRouterAdminStatus_Type = VlanAdminStatusCode
_VRouterAdminStatus_Object = MibTableColumn
vRouterAdminStatus = _VRouterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 6),
    _VRouterAdminStatus_Type()
)
vRouterAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRouterAdminStatus.setStatus("current")
_VRouterOperStatus_Type = VlanOperStatusCode
_VRouterOperStatus_Object = MibTableColumn
vRouterOperStatus = _VRouterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 7),
    _VRouterOperStatus_Type()
)
vRouterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouterOperStatus.setStatus("current")
_VRouterRowStatus_Type = RowStatus
_VRouterRowStatus_Object = MibTableColumn
vRouterRowStatus = _VRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 8),
    _VRouterRowStatus_Type()
)
vRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRouterRowStatus.setStatus("current")
_VRouterIfIndex_Type = InterfaceIndex
_VRouterIfIndex_Object = MibTableColumn
vRouterIfIndex = _VRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 9),
    _VRouterIfIndex_Type()
)
vRouterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRouterIfIndex.setStatus("current")


class _VRouterRipMode_Type(Integer32):
    """Custom type vRouterRipMode based on Integer32"""
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
        *(("active", 2),
          ("deaf", 3),
          ("inactive", 4),
          ("silent", 1))
    )


_VRouterRipMode_Type.__name__ = "Integer32"
_VRouterRipMode_Object = MibTableColumn
vRouterRipMode = _VRouterRipMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 2, 1, 1, 10),
    _VRouterRipMode_Type()
)
vRouterRipMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRouterRipMode.setStatus("current")
_PhysicalPortGroup_ObjectIdentity = ObjectIdentity
physicalPortGroup = _PhysicalPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3)
)
_PPortTable_Object = MibTable
pPortTable = _PPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pPortTable.setStatus("current")
_PPortEntry_Object = MibTableRow
pPortEntry = _PPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1)
)
pPortEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "pPortNumber"),
)
if mibBuilder.loadTexts:
    pPortEntry.setStatus("current")


class _PPortNumber_Type(Integer32):
    """Custom type pPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PPortNumber_Type.__name__ = "Integer32"
_PPortNumber_Object = MibTableColumn
pPortNumber = _PPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 1),
    _PPortNumber_Type()
)
pPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pPortNumber.setStatus("current")
_PPortMediaType_Type = PhyPortMediaTypeCode
_PPortMediaType_Object = MibTableColumn
pPortMediaType = _PPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 2),
    _PPortMediaType_Type()
)
pPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPortMediaType.setStatus("current")


class _PPortDescription_Type(DisplayString):
    """Custom type pPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PPortDescription_Type.__name__ = "DisplayString"
_PPortDescription_Object = MibTableColumn
pPortDescription = _PPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 3),
    _PPortDescription_Type()
)
pPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPortDescription.setStatus("current")
_PPortIfIndex_Type = InterfaceIndex
_PPortIfIndex_Object = MibTableColumn
pPortIfIndex = _PPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 4),
    _PPortIfIndex_Type()
)
pPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPortIfIndex.setStatus("current")


class _PPortDuplexity_Type(Integer32):
    """Custom type pPortDuplexity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1))
    )


_PPortDuplexity_Type.__name__ = "Integer32"
_PPortDuplexity_Object = MibTableColumn
pPortDuplexity = _PPortDuplexity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 5),
    _PPortDuplexity_Type()
)
pPortDuplexity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPortDuplexity.setStatus("current")


class _PPortAutoNegotiate_Type(Integer32):
    """Custom type pPortAutoNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PPortAutoNegotiate_Type.__name__ = "Integer32"
_PPortAutoNegotiate_Object = MibTableColumn
pPortAutoNegotiate = _PPortAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 6),
    _PPortAutoNegotiate_Type()
)
pPortAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPortAutoNegotiate.setStatus("current")
_PPortAdminStatus_Type = VlanAdminStatusCode
_PPortAdminStatus_Object = MibTableColumn
pPortAdminStatus = _PPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 7),
    _PPortAdminStatus_Type()
)
pPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPortAdminStatus.setStatus("current")
_PPortOperStatus_Type = VlanOperStatusCode
_PPortOperStatus_Object = MibTableColumn
pPortOperStatus = _PPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 8),
    _PPortOperStatus_Type()
)
pPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPortOperStatus.setStatus("current")
_PPortSpeed_Type = Integer32
_PPortSpeed_Object = MibTableColumn
pPortSpeed = _PPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 9),
    _PPortSpeed_Type()
)
pPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPortSpeed.setStatus("current")


class _PPortCountersStatus_Type(Integer32):
    """Custom type pPortCountersStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("unknown", 0))
    )


_PPortCountersStatus_Type.__name__ = "Integer32"
_PPortCountersStatus_Object = MibTableColumn
pPortCountersStatus = _PPortCountersStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 1, 1, 10),
    _PPortCountersStatus_Type()
)
pPortCountersStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPortCountersStatus.setStatus("current")


class _PEtherCountersStatus_Type(Integer32):
    """Custom type pEtherCountersStatus based on Integer32"""
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


_PEtherCountersStatus_Type.__name__ = "Integer32"
_PEtherCountersStatus_Object = MibScalar
pEtherCountersStatus = _PEtherCountersStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 2),
    _PEtherCountersStatus_Type()
)
pEtherCountersStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pEtherCountersStatus.setStatus("current")
_PStatsPollInterval_Type = Integer32
_PStatsPollInterval_Object = MibScalar
pStatsPollInterval = _PStatsPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 3, 3),
    _PStatsPollInterval_Type()
)
pStatsPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pStatsPollInterval.setStatus("current")
_VirtualPortGroup_ObjectIdentity = ObjectIdentity
virtualPortGroup = _VirtualPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4)
)
_VPortTable_Object = MibTable
vPortTable = _VPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vPortTable.setStatus("current")
_VPortEntry_Object = MibTableRow
vPortEntry = _VPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1)
)
vPortEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "vPortNumber"),
)
if mibBuilder.loadTexts:
    vPortEntry.setStatus("current")


class _VPortNumber_Type(Integer32):
    """Custom type vPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_VPortNumber_Type.__name__ = "Integer32"
_VPortNumber_Object = MibTableColumn
vPortNumber = _VPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 1),
    _VPortNumber_Type()
)
vPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vPortNumber.setStatus("current")


class _VPortPhyPort_Type(Integer32):
    """Custom type vPortPhyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_VPortPhyPort_Type.__name__ = "Integer32"
_VPortPhyPort_Object = MibTableColumn
vPortPhyPort = _VPortPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 2),
    _VPortPhyPort_Type()
)
vPortPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortPhyPort.setStatus("current")
_VPortFuncType_Type = PortFuncCode
_VPortFuncType_Object = MibTableColumn
vPortFuncType = _VPortFuncType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 3),
    _VPortFuncType_Type()
)
vPortFuncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortFuncType.setStatus("current")


class _VPortVlanNumber_Type(Integer32):
    """Custom type vPortVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VPortVlanNumber_Type.__name__ = "Integer32"
_VPortVlanNumber_Object = MibTableColumn
vPortVlanNumber = _VPortVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 4),
    _VPortVlanNumber_Type()
)
vPortVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortVlanNumber.setStatus("current")


class _VPortDomain_Type(Integer32):
    """Custom type vPortDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VPortDomain_Type.__name__ = "Integer32"
_VPortDomain_Object = MibTableColumn
vPortDomain = _VPortDomain_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 5),
    _VPortDomain_Type()
)
vPortDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortDomain.setStatus("current")
_VPortMACaddress_Type = MacAddress
_VPortMACaddress_Object = MibTableColumn
vPortMACaddress = _VPortMACaddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 6),
    _VPortMACaddress_Type()
)
vPortMACaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortMACaddress.setStatus("current")
_VPortDefaultMacLayer_Type = MACLayerCode
_VPortDefaultMacLayer_Object = MibTableColumn
vPortDefaultMacLayer = _VPortDefaultMacLayer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 7),
    _VPortDefaultMacLayer_Type()
)
vPortDefaultMacLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortDefaultMacLayer.setStatus("current")


class _VPortBridgeMode_Type(Integer32):
    """Custom type vPortBridgeMode based on Integer32"""
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
        *(("autoSwitch", 2),
          ("forceBridge", 3),
          ("forceSwitch", 4),
          ("unknown", 1))
    )


_VPortBridgeMode_Type.__name__ = "Integer32"
_VPortBridgeMode_Object = MibTableColumn
vPortBridgeMode = _VPortBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 8),
    _VPortBridgeMode_Type()
)
vPortBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortBridgeMode.setStatus("deprecated")


class _VPortSwitchTimer_Type(Integer32):
    """Custom type vPortSwitchTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VPortSwitchTimer_Type.__name__ = "Integer32"
_VPortSwitchTimer_Object = MibTableColumn
vPortSwitchTimer = _VPortSwitchTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 9),
    _VPortSwitchTimer_Type()
)
vPortSwitchTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortSwitchTimer.setStatus("deprecated")


class _VPortDescription_Type(DisplayString):
    """Custom type vPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VPortDescription_Type.__name__ = "DisplayString"
_VPortDescription_Object = MibTableColumn
vPortDescription = _VPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 10),
    _VPortDescription_Type()
)
vPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortDescription.setStatus("current")
_VPortAdminStatus_Type = VlanAdminStatusCode
_VPortAdminStatus_Object = MibTableColumn
vPortAdminStatus = _VPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 11),
    _VPortAdminStatus_Type()
)
vPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortAdminStatus.setStatus("current")
_VPortOperStatus_Type = VlanOperStatusCode
_VPortOperStatus_Object = MibTableColumn
vPortOperStatus = _VPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 12),
    _VPortOperStatus_Type()
)
vPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortOperStatus.setStatus("current")
_VPortIfIndex_Type = InterfaceIndex
_VPortIfIndex_Object = MibTableColumn
vPortIfIndex = _VPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 4, 1, 1, 13),
    _VPortIfIndex_Type()
)
vPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortIfIndex.setStatus("current")
_IpRouteCacheGroup_ObjectIdentity = ObjectIdentity
ipRouteCacheGroup = _IpRouteCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5)
)


class _IpRouteState_Type(Integer32):
    """Custom type ipRouteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipForwarding", 1),
          ("ipRouteCacheForward", 2))
    )


_IpRouteState_Type.__name__ = "Integer32"
_IpRouteState_Object = MibScalar
ipRouteState = _IpRouteState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 1),
    _IpRouteState_Type()
)
ipRouteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteState.setStatus("current")
_IpRouteCacheTable_Object = MibTable
ipRouteCacheTable = _IpRouteCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ipRouteCacheTable.setStatus("current")
_IpRouteCacheEntry_Object = MibTableRow
ipRouteCacheEntry = _IpRouteCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2, 1)
)
ipRouteCacheEntry.setIndexNames(
    (0, "SWITCH-VLAN-MIB", "ipRouteCacheIndex"),
)
if mibBuilder.loadTexts:
    ipRouteCacheEntry.setStatus("current")
_IpRouteCacheIndex_Type = Integer32
_IpRouteCacheIndex_Object = MibTableColumn
ipRouteCacheIndex = _IpRouteCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2, 1, 1),
    _IpRouteCacheIndex_Type()
)
ipRouteCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteCacheIndex.setStatus("current")
_IpRouteCacheDstIpAddress_Type = IpAddress
_IpRouteCacheDstIpAddress_Object = MibTableColumn
ipRouteCacheDstIpAddress = _IpRouteCacheDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2, 1, 2),
    _IpRouteCacheDstIpAddress_Type()
)
ipRouteCacheDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteCacheDstIpAddress.setStatus("current")
_IpRouteCacheSrcIpAddress_Type = IpAddress
_IpRouteCacheSrcIpAddress_Object = MibTableColumn
ipRouteCacheSrcIpAddress = _IpRouteCacheSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2, 1, 3),
    _IpRouteCacheSrcIpAddress_Type()
)
ipRouteCacheSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteCacheSrcIpAddress.setStatus("current")


class _IpRouteCacheDstPort_Type(Integer32):
    """Custom type ipRouteCacheDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpRouteCacheDstPort_Type.__name__ = "Integer32"
_IpRouteCacheDstPort_Object = MibTableColumn
ipRouteCacheDstPort = _IpRouteCacheDstPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2, 1, 4),
    _IpRouteCacheDstPort_Type()
)
ipRouteCacheDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteCacheDstPort.setStatus("current")


class _IpRouteCacheSrcPort_Type(Integer32):
    """Custom type ipRouteCacheSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpRouteCacheSrcPort_Type.__name__ = "Integer32"
_IpRouteCacheSrcPort_Object = MibTableColumn
ipRouteCacheSrcPort = _IpRouteCacheSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2, 1, 5),
    _IpRouteCacheSrcPort_Type()
)
ipRouteCacheSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteCacheSrcPort.setStatus("current")


class _IpRouteCacheMedia_Type(Integer32):
    """Custom type ipRouteCacheMedia based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("atmtrunk", 7),
          ("cip", 3),
          ("csr", 5),
          ("fddi", 6),
          ("fdditrunk", 8),
          ("ptop", 4),
          ("unknown", 1),
          ("vlan", 2))
    )


_IpRouteCacheMedia_Type.__name__ = "Integer32"
_IpRouteCacheMedia_Object = MibTableColumn
ipRouteCacheMedia = _IpRouteCacheMedia_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2, 1, 6),
    _IpRouteCacheMedia_Type()
)
ipRouteCacheMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteCacheMedia.setStatus("current")


class _IpRouteCacheVPortNumber_Type(Integer32):
    """Custom type ipRouteCacheVPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_IpRouteCacheVPortNumber_Type.__name__ = "Integer32"
_IpRouteCacheVPortNumber_Object = MibTableColumn
ipRouteCacheVPortNumber = _IpRouteCacheVPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2, 1, 7),
    _IpRouteCacheVPortNumber_Type()
)
ipRouteCacheVPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteCacheVPortNumber.setStatus("current")
_IpRouteCacheVCI_Type = AtmVci
_IpRouteCacheVCI_Object = MibTableColumn
ipRouteCacheVCI = _IpRouteCacheVCI_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 2, 5, 2, 5, 2, 1, 8),
    _IpRouteCacheVCI_Type()
)
ipRouteCacheVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteCacheVCI.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-VLAN-MIB",
    **{"AtmVci": AtmVci,
       "VlanAdminStatusCode": VlanAdminStatusCode,
       "VlanOperStatusCode": VlanOperStatusCode,
       "VlanMode": VlanMode,
       "PortFuncCode": PortFuncCode,
       "MACLayerCode": MACLayerCode,
       "PhyPortMediaTypeCode": PhyPortMediaTypeCode,
       "switchVlanMib": switchVlanMib,
       "vLanGroup": vLanGroup,
       "vLanTable": vLanTable,
       "vLanEntry": vLanEntry,
       "vLanNumber": vLanNumber,
       "vLanMembers": vLanMembers,
       "vLanDescription": vLanDescription,
       "vLanAdminStatus": vLanAdminStatus,
       "vLanOperStatus": vLanOperStatus,
       "vLanMode": vLanMode,
       "vLanRowStatus": vLanRowStatus,
       "vRouterGroup": vRouterGroup,
       "vRouterTable": vRouterTable,
       "vRouterEntry": vRouterEntry,
       "vRouterProtocol": vRouterProtocol,
       "vRouterIpAddress": vRouterIpAddress,
       "vRouterSubNetMask": vRouterSubNetMask,
       "vRouterBcastAddress": vRouterBcastAddress,
       "vRouterDescription": vRouterDescription,
       "vRouterAdminStatus": vRouterAdminStatus,
       "vRouterOperStatus": vRouterOperStatus,
       "vRouterRowStatus": vRouterRowStatus,
       "vRouterIfIndex": vRouterIfIndex,
       "vRouterRipMode": vRouterRipMode,
       "physicalPortGroup": physicalPortGroup,
       "pPortTable": pPortTable,
       "pPortEntry": pPortEntry,
       "pPortNumber": pPortNumber,
       "pPortMediaType": pPortMediaType,
       "pPortDescription": pPortDescription,
       "pPortIfIndex": pPortIfIndex,
       "pPortDuplexity": pPortDuplexity,
       "pPortAutoNegotiate": pPortAutoNegotiate,
       "pPortAdminStatus": pPortAdminStatus,
       "pPortOperStatus": pPortOperStatus,
       "pPortSpeed": pPortSpeed,
       "pPortCountersStatus": pPortCountersStatus,
       "pEtherCountersStatus": pEtherCountersStatus,
       "pStatsPollInterval": pStatsPollInterval,
       "virtualPortGroup": virtualPortGroup,
       "vPortTable": vPortTable,
       "vPortEntry": vPortEntry,
       "vPortNumber": vPortNumber,
       "vPortPhyPort": vPortPhyPort,
       "vPortFuncType": vPortFuncType,
       "vPortVlanNumber": vPortVlanNumber,
       "vPortDomain": vPortDomain,
       "vPortMACaddress": vPortMACaddress,
       "vPortDefaultMacLayer": vPortDefaultMacLayer,
       "vPortBridgeMode": vPortBridgeMode,
       "vPortSwitchTimer": vPortSwitchTimer,
       "vPortDescription": vPortDescription,
       "vPortAdminStatus": vPortAdminStatus,
       "vPortOperStatus": vPortOperStatus,
       "vPortIfIndex": vPortIfIndex,
       "ipRouteCacheGroup": ipRouteCacheGroup,
       "ipRouteState": ipRouteState,
       "ipRouteCacheTable": ipRouteCacheTable,
       "ipRouteCacheEntry": ipRouteCacheEntry,
       "ipRouteCacheIndex": ipRouteCacheIndex,
       "ipRouteCacheDstIpAddress": ipRouteCacheDstIpAddress,
       "ipRouteCacheSrcIpAddress": ipRouteCacheSrcIpAddress,
       "ipRouteCacheDstPort": ipRouteCacheDstPort,
       "ipRouteCacheSrcPort": ipRouteCacheSrcPort,
       "ipRouteCacheMedia": ipRouteCacheMedia,
       "ipRouteCacheVPortNumber": ipRouteCacheVPortNumber,
       "ipRouteCacheVCI": ipRouteCacheVCI}
)
