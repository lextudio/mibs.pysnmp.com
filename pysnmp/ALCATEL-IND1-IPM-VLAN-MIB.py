# SNMP MIB module (ALCATEL-IND1-IPM-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-IPM-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:13 2024
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

(softentIND1IPMVlanMgt,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1IPMVlanMgt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1IPMVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPMVlanMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPMVlanMIBObjects = _AlcatelIND1IPMVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMVlanMIBObjects.setStatus("current")
_AlaipmvVlanPort_ObjectIdentity = ObjectIdentity
alaipmvVlanPort = _AlaipmvVlanPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1)
)
_AlaipmvVlanPortTable_Object = MibTable
alaipmvVlanPortTable = _AlaipmvVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaipmvVlanPortTable.setStatus("current")
_AlaipmvVlanPortEntry_Object = MibTableRow
alaipmvVlanPortEntry = _AlaipmvVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1)
)
alaipmvVlanPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortIPMVlanNumber"),
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortNumber"),
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortType"),
)
if mibBuilder.loadTexts:
    alaipmvVlanPortEntry.setStatus("current")


class _AlaipmvVlanPortIPMVlanNumber_Type(Integer32):
    """Custom type alaipmvVlanPortIPMVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AlaipmvVlanPortIPMVlanNumber_Type.__name__ = "Integer32"
_AlaipmvVlanPortIPMVlanNumber_Object = MibTableColumn
alaipmvVlanPortIPMVlanNumber = _AlaipmvVlanPortIPMVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 1),
    _AlaipmvVlanPortIPMVlanNumber_Type()
)
alaipmvVlanPortIPMVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaipmvVlanPortIPMVlanNumber.setStatus("current")
_AlaipmvVlanPortNumber_Type = InterfaceIndex
_AlaipmvVlanPortNumber_Object = MibTableColumn
alaipmvVlanPortNumber = _AlaipmvVlanPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 2),
    _AlaipmvVlanPortNumber_Type()
)
alaipmvVlanPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaipmvVlanPortNumber.setStatus("current")


class _AlaipmvVlanPortType_Type(Integer32):
    """Custom type alaipmvVlanPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receiverPort", 1),
          ("senderPort", 2))
    )


_AlaipmvVlanPortType_Type.__name__ = "Integer32"
_AlaipmvVlanPortType_Object = MibTableColumn
alaipmvVlanPortType = _AlaipmvVlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 3),
    _AlaipmvVlanPortType_Type()
)
alaipmvVlanPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaipmvVlanPortType.setStatus("current")
_AlaipmvVlanPortRowStatus_Type = RowStatus
_AlaipmvVlanPortRowStatus_Object = MibTableColumn
alaipmvVlanPortRowStatus = _AlaipmvVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 1, 1, 1, 4),
    _AlaipmvVlanPortRowStatus_Type()
)
alaipmvVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaipmvVlanPortRowStatus.setStatus("current")
_AlaipmvVlanIpAddr_ObjectIdentity = ObjectIdentity
alaipmvVlanIpAddr = _AlaipmvVlanIpAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2)
)
_AlaipmvVlanIpAddrTable_Object = MibTable
alaipmvVlanIpAddrTable = _AlaipmvVlanIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrTable.setStatus("current")
_AlaipmvVlanIpAddrEntry_Object = MibTableRow
alaipmvVlanIpAddrEntry = _AlaipmvVlanIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1)
)
alaipmvVlanIpAddrEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrVlanNumber"),
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrType"),
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddress"),
)
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrEntry.setStatus("current")


class _AlaipmvVlanIpAddrVlanNumber_Type(Integer32):
    """Custom type alaipmvVlanIpAddrVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AlaipmvVlanIpAddrVlanNumber_Type.__name__ = "Integer32"
_AlaipmvVlanIpAddrVlanNumber_Object = MibTableColumn
alaipmvVlanIpAddrVlanNumber = _AlaipmvVlanIpAddrVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 1),
    _AlaipmvVlanIpAddrVlanNumber_Type()
)
alaipmvVlanIpAddrVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrVlanNumber.setStatus("current")


class _AlaipmvVlanIpAddrType_Type(InetAddressType):
    """Custom type alaipmvVlanIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AlaipmvVlanIpAddrType_Type.__name__ = "InetAddressType"
_AlaipmvVlanIpAddrType_Object = MibTableColumn
alaipmvVlanIpAddrType = _AlaipmvVlanIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 2),
    _AlaipmvVlanIpAddrType_Type()
)
alaipmvVlanIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrType.setStatus("current")
_AlaipmvVlanIpAddress_Type = InetAddress
_AlaipmvVlanIpAddress_Object = MibTableColumn
alaipmvVlanIpAddress = _AlaipmvVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 3),
    _AlaipmvVlanIpAddress_Type()
)
alaipmvVlanIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaipmvVlanIpAddress.setStatus("current")
_AlaipmvVlanIpAddrRowStatus_Type = RowStatus
_AlaipmvVlanIpAddrRowStatus_Object = MibTableColumn
alaipmvVlanIpAddrRowStatus = _AlaipmvVlanIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 1, 1, 4),
    _AlaipmvVlanIpAddrRowStatus_Type()
)
alaipmvVlanIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrRowStatus.setStatus("current")
_AlaipmvVlanIpAddrMaskTable_Object = MibTable
alaipmvVlanIpAddrMaskTable = _AlaipmvVlanIpAddrMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrMaskTable.setStatus("current")
_AlaipmvVlanIpAddrMaskEntry_Object = MibTableRow
alaipmvVlanIpAddrMaskEntry = _AlaipmvVlanIpAddrMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1)
)
alaipmvVlanIpAddrMaskEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskVlanNumber"),
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskType"),
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskAddress"),
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskPrefixLen"),
)
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrMaskEntry.setStatus("current")


class _AlaipmvVlanIpAddrMaskVlanNumber_Type(Integer32):
    """Custom type alaipmvVlanIpAddrMaskVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AlaipmvVlanIpAddrMaskVlanNumber_Type.__name__ = "Integer32"
_AlaipmvVlanIpAddrMaskVlanNumber_Object = MibTableColumn
alaipmvVlanIpAddrMaskVlanNumber = _AlaipmvVlanIpAddrMaskVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 1),
    _AlaipmvVlanIpAddrMaskVlanNumber_Type()
)
alaipmvVlanIpAddrMaskVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrMaskVlanNumber.setStatus("current")


class _AlaipmvVlanIpAddrMaskType_Type(InetAddressType):
    """Custom type alaipmvVlanIpAddrMaskType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AlaipmvVlanIpAddrMaskType_Type.__name__ = "InetAddressType"
_AlaipmvVlanIpAddrMaskType_Object = MibTableColumn
alaipmvVlanIpAddrMaskType = _AlaipmvVlanIpAddrMaskType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 2),
    _AlaipmvVlanIpAddrMaskType_Type()
)
alaipmvVlanIpAddrMaskType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrMaskType.setStatus("current")


class _AlaipmvVlanIpAddrMaskAddress_Type(InetAddress):
    """Custom type alaipmvVlanIpAddrMaskAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaipmvVlanIpAddrMaskAddress_Type.__name__ = "InetAddress"
_AlaipmvVlanIpAddrMaskAddress_Object = MibTableColumn
alaipmvVlanIpAddrMaskAddress = _AlaipmvVlanIpAddrMaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 3),
    _AlaipmvVlanIpAddrMaskAddress_Type()
)
alaipmvVlanIpAddrMaskAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrMaskAddress.setStatus("current")
_AlaipmvVlanIpAddrMaskPrefixLen_Type = InetAddressPrefixLength
_AlaipmvVlanIpAddrMaskPrefixLen_Object = MibTableColumn
alaipmvVlanIpAddrMaskPrefixLen = _AlaipmvVlanIpAddrMaskPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 4),
    _AlaipmvVlanIpAddrMaskPrefixLen_Type()
)
alaipmvVlanIpAddrMaskPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrMaskPrefixLen.setStatus("current")
_AlaipmvVlanIpAddrMaskRowStatus_Type = RowStatus
_AlaipmvVlanIpAddrMaskRowStatus_Object = MibTableColumn
alaipmvVlanIpAddrMaskRowStatus = _AlaipmvVlanIpAddrMaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 2, 2, 1, 5),
    _AlaipmvVlanIpAddrMaskRowStatus_Type()
)
alaipmvVlanIpAddrMaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaipmvVlanIpAddrMaskRowStatus.setStatus("current")
_AlaipmvVlanCtagT_ObjectIdentity = ObjectIdentity
alaipmvVlanCtagT = _AlaipmvVlanCtagT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3)
)
_AlaipmvVlanCtagTable_Object = MibTable
alaipmvVlanCtagTable = _AlaipmvVlanCtagTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaipmvVlanCtagTable.setStatus("current")
_AlaipmvVlanCtagEntry_Object = MibTableRow
alaipmvVlanCtagEntry = _AlaipmvVlanCtagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1)
)
alaipmvVlanCtagEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanNumber"),
    (0, "ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanCtag"),
)
if mibBuilder.loadTexts:
    alaipmvVlanCtagEntry.setStatus("current")


class _AlaipmvVlanNumber_Type(Integer32):
    """Custom type alaipmvVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AlaipmvVlanNumber_Type.__name__ = "Integer32"
_AlaipmvVlanNumber_Object = MibTableColumn
alaipmvVlanNumber = _AlaipmvVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1, 1),
    _AlaipmvVlanNumber_Type()
)
alaipmvVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaipmvVlanNumber.setStatus("current")


class _AlaipmvVlanCtag_Type(Integer32):
    """Custom type alaipmvVlanCtag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaipmvVlanCtag_Type.__name__ = "Integer32"
_AlaipmvVlanCtag_Object = MibTableColumn
alaipmvVlanCtag = _AlaipmvVlanCtag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1, 2),
    _AlaipmvVlanCtag_Type()
)
alaipmvVlanCtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaipmvVlanCtag.setStatus("current")
_AlaipmvVlanCtagRowStatus_Type = RowStatus
_AlaipmvVlanCtagRowStatus_Object = MibTableColumn
alaipmvVlanCtagRowStatus = _AlaipmvVlanCtagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 3, 1, 1, 3),
    _AlaipmvVlanCtagRowStatus_Type()
)
alaipmvVlanCtagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaipmvVlanCtagRowStatus.setStatus("current")
_AlaipmvVlanIpAddrMask_ObjectIdentity = ObjectIdentity
alaipmvVlanIpAddrMask = _AlaipmvVlanIpAddrMask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 1, 4)
)
_AlcatelIND1IPMVlanMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPMVlanMIBConformance = _AlcatelIND1IPMVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMVlanMIBConformance.setStatus("current")
_AlcatelIND1IPMVlanMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPMVlanMIBGroups = _AlcatelIND1IPMVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMVlanMIBGroups.setStatus("current")
_AlcatelIND1IPMVlanMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPMVlanMIBCompliances = _AlcatelIND1IPMVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMVlanMIBCompliances.setStatus("current")

# Managed Objects groups

alaipmvlanPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 1)
)
alaipmvlanPortGroup.setObjects(
      *(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortIPMVlanNumber"),
        ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortNumber"),
        ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortType"),
        ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanPortRowStatus"))
)
if mibBuilder.loadTexts:
    alaipmvlanPortGroup.setStatus("current")

alaipmvlanIPAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 2)
)
alaipmvlanIPAddressGroup.setObjects(
      *(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrVlanNumber"),
        ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrType"),
        ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddress"),
        ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    alaipmvlanIPAddressGroup.setStatus("current")

alaipmvlanCtagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 3)
)
alaipmvlanCtagGroup.setObjects(
      *(("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanNumber"),
        ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanCtag"),
        ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanCtagRowStatus"))
)
if mibBuilder.loadTexts:
    alaipmvlanCtagGroup.setStatus("current")

alaipmvlanIPAddrMaskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 1, 4)
)
alaipmvlanIPAddrMaskGroup.setObjects(
    ("ALCATEL-IND1-IPM-VLAN-MIB", "alaipmvVlanIpAddrMaskRowStatus")
)
if mibBuilder.loadTexts:
    alaipmvlanIPAddrMaskGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1IPMVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 41, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPM-VLAN-MIB",
    **{"alcatelIND1IPMVlanMIB": alcatelIND1IPMVlanMIB,
       "alcatelIND1IPMVlanMIBObjects": alcatelIND1IPMVlanMIBObjects,
       "alaipmvVlanPort": alaipmvVlanPort,
       "alaipmvVlanPortTable": alaipmvVlanPortTable,
       "alaipmvVlanPortEntry": alaipmvVlanPortEntry,
       "alaipmvVlanPortIPMVlanNumber": alaipmvVlanPortIPMVlanNumber,
       "alaipmvVlanPortNumber": alaipmvVlanPortNumber,
       "alaipmvVlanPortType": alaipmvVlanPortType,
       "alaipmvVlanPortRowStatus": alaipmvVlanPortRowStatus,
       "alaipmvVlanIpAddr": alaipmvVlanIpAddr,
       "alaipmvVlanIpAddrTable": alaipmvVlanIpAddrTable,
       "alaipmvVlanIpAddrEntry": alaipmvVlanIpAddrEntry,
       "alaipmvVlanIpAddrVlanNumber": alaipmvVlanIpAddrVlanNumber,
       "alaipmvVlanIpAddrType": alaipmvVlanIpAddrType,
       "alaipmvVlanIpAddress": alaipmvVlanIpAddress,
       "alaipmvVlanIpAddrRowStatus": alaipmvVlanIpAddrRowStatus,
       "alaipmvVlanIpAddrMaskTable": alaipmvVlanIpAddrMaskTable,
       "alaipmvVlanIpAddrMaskEntry": alaipmvVlanIpAddrMaskEntry,
       "alaipmvVlanIpAddrMaskVlanNumber": alaipmvVlanIpAddrMaskVlanNumber,
       "alaipmvVlanIpAddrMaskType": alaipmvVlanIpAddrMaskType,
       "alaipmvVlanIpAddrMaskAddress": alaipmvVlanIpAddrMaskAddress,
       "alaipmvVlanIpAddrMaskPrefixLen": alaipmvVlanIpAddrMaskPrefixLen,
       "alaipmvVlanIpAddrMaskRowStatus": alaipmvVlanIpAddrMaskRowStatus,
       "alaipmvVlanCtagT": alaipmvVlanCtagT,
       "alaipmvVlanCtagTable": alaipmvVlanCtagTable,
       "alaipmvVlanCtagEntry": alaipmvVlanCtagEntry,
       "alaipmvVlanNumber": alaipmvVlanNumber,
       "alaipmvVlanCtag": alaipmvVlanCtag,
       "alaipmvVlanCtagRowStatus": alaipmvVlanCtagRowStatus,
       "alaipmvVlanIpAddrMask": alaipmvVlanIpAddrMask,
       "alcatelIND1IPMVlanMIBConformance": alcatelIND1IPMVlanMIBConformance,
       "alcatelIND1IPMVlanMIBGroups": alcatelIND1IPMVlanMIBGroups,
       "alaipmvlanPortGroup": alaipmvlanPortGroup,
       "alaipmvlanIPAddressGroup": alaipmvlanIPAddressGroup,
       "alaipmvlanCtagGroup": alaipmvlanCtagGroup,
       "alaipmvlanIPAddrMaskGroup": alaipmvlanIPAddrMaskGroup,
       "alcatelIND1IPMVlanMIBCompliances": alcatelIND1IPMVlanMIBCompliances,
       "alcatelIND1IPMVlanMIBCompliance": alcatelIND1IPMVlanMIBCompliance}
)
