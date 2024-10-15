# SNMP MIB module (ZXR10-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:00 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zxr10protocol,) = mibBuilder.importSymbols(
    "ZXR10-PROTOCOL-MIB",
    "zxr10protocol")


# MODULE-IDENTITY


# Types definitions



class Zxr10NatType(Integer32):
    """Custom type Zxr10NatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("ip", 4),
          ("snat", 0),
          ("tcp", 6),
          ("udp", 17))
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zxr10nat_ObjectIdentity = ObjectIdentity
zxr10nat = _Zxr10nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3)
)
_Zxr10natConfig_ObjectIdentity = ObjectIdentity
zxr10natConfig = _Zxr10natConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1)
)


class _Zxr10natConfEnable_Type(Integer32):
    """Custom type zxr10natConfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Zxr10natConfEnable_Type.__name__ = "Integer32"
_Zxr10natConfEnable_Object = MibScalar
zxr10natConfEnable = _Zxr10natConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 1),
    _Zxr10natConfEnable_Type()
)
zxr10natConfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfEnable.setStatus("current")
_Zxr10natInterfaceTable_Object = MibTable
zxr10natInterfaceTable = _Zxr10natInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2)
)
if mibBuilder.loadTexts:
    zxr10natInterfaceTable.setStatus("current")
_Zxr10natInterfaceEntry_Object = MibTableRow
zxr10natInterfaceEntry = _Zxr10natInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2, 1)
)
zxr10natInterfaceEntry.setIndexNames(
    (0, "ZXR10-NAT-MIB", "zxr10natInterfaceIndex"),
)
if mibBuilder.loadTexts:
    zxr10natInterfaceEntry.setStatus("current")
_Zxr10natInterfaceIndex_Type = Integer32
_Zxr10natInterfaceIndex_Object = MibTableColumn
zxr10natInterfaceIndex = _Zxr10natInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2, 1, 1),
    _Zxr10natInterfaceIndex_Type()
)
zxr10natInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natInterfaceIndex.setStatus("current")
_Zxr10natInterfaceName_Type = DisplayString
_Zxr10natInterfaceName_Object = MibTableColumn
zxr10natInterfaceName = _Zxr10natInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2, 1, 2),
    _Zxr10natInterfaceName_Type()
)
zxr10natInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natInterfaceName.setStatus("current")


class _Zxr10natInterfaceStorageType_Type(Integer32):
    """Custom type zxr10natInterfaceStorageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inside", 1),
          ("outside", 2))
    )


_Zxr10natInterfaceStorageType_Type.__name__ = "Integer32"
_Zxr10natInterfaceStorageType_Object = MibTableColumn
zxr10natInterfaceStorageType = _Zxr10natInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2, 1, 3),
    _Zxr10natInterfaceStorageType_Type()
)
zxr10natInterfaceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natInterfaceStorageType.setStatus("current")
_Zxr10natConfigTimeout_ObjectIdentity = ObjectIdentity
zxr10natConfigTimeout = _Zxr10natConfigTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3)
)
_Zxr10natConfTimeoutClassTable_Object = MibTable
zxr10natConfTimeoutClassTable = _Zxr10natConfTimeoutClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zxr10natConfTimeoutClassTable.setStatus("current")
_Zxr10natConfTimeoutClassEntry_Object = MibTableRow
zxr10natConfTimeoutClassEntry = _Zxr10natConfTimeoutClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 1, 1)
)
zxr10natConfTimeoutClassEntry.setIndexNames(
    (0, "ZXR10-NAT-MIB", "zxr10natConfTimeoutClassIndex"),
)
if mibBuilder.loadTexts:
    zxr10natConfTimeoutClassEntry.setStatus("current")


class _Zxr10natConfTimeoutClassIndex_Type(Integer32):
    """Custom type zxr10natConfTimeoutClassIndex based on Integer32"""
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
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3),
          ("e", 4))
    )


_Zxr10natConfTimeoutClassIndex_Type.__name__ = "Integer32"
_Zxr10natConfTimeoutClassIndex_Object = MibTableColumn
zxr10natConfTimeoutClassIndex = _Zxr10natConfTimeoutClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 1, 1, 1),
    _Zxr10natConfTimeoutClassIndex_Type()
)
zxr10natConfTimeoutClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfTimeoutClassIndex.setStatus("current")


class _Zxr10natConfTimeoutClassValue_Type(Integer32):
    """Custom type zxr10natConfTimeoutClassValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2147483647),
    )


_Zxr10natConfTimeoutClassValue_Type.__name__ = "Integer32"
_Zxr10natConfTimeoutClassValue_Object = MibTableColumn
zxr10natConfTimeoutClassValue = _Zxr10natConfTimeoutClassValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 1, 1, 2),
    _Zxr10natConfTimeoutClassValue_Type()
)
zxr10natConfTimeoutClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfTimeoutClassValue.setStatus("current")
_Zxr10natConfTimeoutProtocolTable_Object = MibTable
zxr10natConfTimeoutProtocolTable = _Zxr10natConfTimeoutProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    zxr10natConfTimeoutProtocolTable.setStatus("current")
_Zxr10natConfTimeoutProtocolEntry_Object = MibTableRow
zxr10natConfTimeoutProtocolEntry = _Zxr10natConfTimeoutProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1)
)
zxr10natConfTimeoutProtocolEntry.setIndexNames(
    (0, "ZXR10-NAT-MIB", "zxr10natConfTimeoutProtocolIndex"),
)
if mibBuilder.loadTexts:
    zxr10natConfTimeoutProtocolEntry.setStatus("current")


class _Zxr10natConfTimeoutProtocolIndex_Type(Integer32):
    """Custom type zxr10natConfTimeoutProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Zxr10natConfTimeoutProtocolIndex_Type.__name__ = "Integer32"
_Zxr10natConfTimeoutProtocolIndex_Object = MibTableColumn
zxr10natConfTimeoutProtocolIndex = _Zxr10natConfTimeoutProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1, 1),
    _Zxr10natConfTimeoutProtocolIndex_Type()
)
zxr10natConfTimeoutProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfTimeoutProtocolIndex.setStatus("current")
_Zxr10natConfTimeoutProtocol_Type = Zxr10NatType
_Zxr10natConfTimeoutProtocol_Object = MibTableColumn
zxr10natConfTimeoutProtocol = _Zxr10natConfTimeoutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1, 2),
    _Zxr10natConfTimeoutProtocol_Type()
)
zxr10natConfTimeoutProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfTimeoutProtocol.setStatus("current")


class _Zxr10natConfTimeoutPort_Type(Integer32):
    """Custom type zxr10natConfTimeoutPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Zxr10natConfTimeoutPort_Type.__name__ = "Integer32"
_Zxr10natConfTimeoutPort_Object = MibTableColumn
zxr10natConfTimeoutPort = _Zxr10natConfTimeoutPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1, 3),
    _Zxr10natConfTimeoutPort_Type()
)
zxr10natConfTimeoutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfTimeoutPort.setStatus("current")


class _Zxr10natConfTimeoutClass_Type(Integer32):
    """Custom type zxr10natConfTimeoutClass based on Integer32"""
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
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3),
          ("e", 4))
    )


_Zxr10natConfTimeoutClass_Type.__name__ = "Integer32"
_Zxr10natConfTimeoutClass_Object = MibTableColumn
zxr10natConfTimeoutClass = _Zxr10natConfTimeoutClass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1, 4),
    _Zxr10natConfTimeoutClass_Type()
)
zxr10natConfTimeoutClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfTimeoutClass.setStatus("current")
_Zxr10natConfigMaximal_ObjectIdentity = ObjectIdentity
zxr10natConfigMaximal = _Zxr10natConfigMaximal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4)
)
_Zxr10natConfMaximalDefault_Type = Integer32
_Zxr10natConfMaximalDefault_Object = MibScalar
zxr10natConfMaximalDefault = _Zxr10natConfMaximalDefault_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 1),
    _Zxr10natConfMaximalDefault_Type()
)
zxr10natConfMaximalDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfMaximalDefault.setStatus("current")
_Zxr10natConfMaximalTable_Object = MibTable
zxr10natConfMaximalTable = _Zxr10natConfMaximalTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    zxr10natConfMaximalTable.setStatus("current")
_Zxr10natConfMaximalEntry_Object = MibTableRow
zxr10natConfMaximalEntry = _Zxr10natConfMaximalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 2, 1)
)
zxr10natConfMaximalEntry.setIndexNames(
    (0, "ZXR10-NAT-MIB", "zxr10natConfMaximalAclNo"),
)
if mibBuilder.loadTexts:
    zxr10natConfMaximalEntry.setStatus("current")
_Zxr10natConfMaximalAclNo_Type = Integer32
_Zxr10natConfMaximalAclNo_Object = MibTableColumn
zxr10natConfMaximalAclNo = _Zxr10natConfMaximalAclNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 2, 1, 1),
    _Zxr10natConfMaximalAclNo_Type()
)
zxr10natConfMaximalAclNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfMaximalAclNo.setStatus("current")
_Zxr10natConfMaximalVlaue_Type = Integer32
_Zxr10natConfMaximalVlaue_Object = MibTableColumn
zxr10natConfMaximalVlaue = _Zxr10natConfMaximalVlaue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 2, 1, 2),
    _Zxr10natConfMaximalVlaue_Type()
)
zxr10natConfMaximalVlaue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfMaximalVlaue.setStatus("current")
_Zxr10natConfStaticAddrMapTable_Object = MibTable
zxr10natConfStaticAddrMapTable = _Zxr10natConfStaticAddrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5)
)
if mibBuilder.loadTexts:
    zxr10natConfStaticAddrMapTable.setStatus("current")
_Zxr10natConfStaticAddrMapEntry_Object = MibTableRow
zxr10natConfStaticAddrMapEntry = _Zxr10natConfStaticAddrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1)
)
zxr10natConfStaticAddrMapEntry.setIndexNames(
    (0, "ZXR10-NAT-MIB", "zxr10natConfStaticRuleIndex"),
)
if mibBuilder.loadTexts:
    zxr10natConfStaticAddrMapEntry.setStatus("current")
_Zxr10natConfStaticRuleIndex_Type = Integer32
_Zxr10natConfStaticRuleIndex_Object = MibTableColumn
zxr10natConfStaticRuleIndex = _Zxr10natConfStaticRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 1),
    _Zxr10natConfStaticRuleIndex_Type()
)
zxr10natConfStaticRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfStaticRuleIndex.setStatus("current")
_Zxr10natConfStaticLocalAddr_Type = IpAddress
_Zxr10natConfStaticLocalAddr_Object = MibTableColumn
zxr10natConfStaticLocalAddr = _Zxr10natConfStaticLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 2),
    _Zxr10natConfStaticLocalAddr_Type()
)
zxr10natConfStaticLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfStaticLocalAddr.setStatus("current")
_Zxr10natConfStaticLocalPort_Type = Integer32
_Zxr10natConfStaticLocalPort_Object = MibTableColumn
zxr10natConfStaticLocalPort = _Zxr10natConfStaticLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 3),
    _Zxr10natConfStaticLocalPort_Type()
)
zxr10natConfStaticLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfStaticLocalPort.setStatus("current")
_Zxr10natConfStaticGlobalAddr_Type = IpAddress
_Zxr10natConfStaticGlobalAddr_Object = MibTableColumn
zxr10natConfStaticGlobalAddr = _Zxr10natConfStaticGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 4),
    _Zxr10natConfStaticGlobalAddr_Type()
)
zxr10natConfStaticGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfStaticGlobalAddr.setStatus("current")
_Zxr10natConfStaticGlobalPort_Type = Integer32
_Zxr10natConfStaticGlobalPort_Object = MibTableColumn
zxr10natConfStaticGlobalPort = _Zxr10natConfStaticGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 5),
    _Zxr10natConfStaticGlobalPort_Type()
)
zxr10natConfStaticGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfStaticGlobalPort.setStatus("current")
_Zxr10natConfStaticProtoType_Type = Zxr10NatType
_Zxr10natConfStaticProtoType_Object = MibTableColumn
zxr10natConfStaticProtoType = _Zxr10natConfStaticProtoType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 6),
    _Zxr10natConfStaticProtoType_Type()
)
zxr10natConfStaticProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfStaticProtoType.setStatus("current")
_Zxr10natConfDynAddrMapTable_Object = MibTable
zxr10natConfDynAddrMapTable = _Zxr10natConfDynAddrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6)
)
if mibBuilder.loadTexts:
    zxr10natConfDynAddrMapTable.setStatus("current")
_Zxr10natConfDynAddrMapEntry_Object = MibTableRow
zxr10natConfDynAddrMapEntry = _Zxr10natConfDynAddrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1)
)
zxr10natConfDynAddrMapEntry.setIndexNames(
    (0, "ZXR10-NAT-MIB", "zxr10natConfDynRuleIndex"),
)
if mibBuilder.loadTexts:
    zxr10natConfDynAddrMapEntry.setStatus("current")
_Zxr10natConfDynRuleIndex_Type = Integer32
_Zxr10natConfDynRuleIndex_Object = MibTableColumn
zxr10natConfDynRuleIndex = _Zxr10natConfDynRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 1),
    _Zxr10natConfDynRuleIndex_Type()
)
zxr10natConfDynRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfDynRuleIndex.setStatus("current")
_Zxr10natConfDynAccessListNum_Type = Integer32
_Zxr10natConfDynAccessListNum_Object = MibTableColumn
zxr10natConfDynAccessListNum = _Zxr10natConfDynAccessListNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 2),
    _Zxr10natConfDynAccessListNum_Type()
)
zxr10natConfDynAccessListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfDynAccessListNum.setStatus("current")


class _Zxr10natConfDynRuleOverlay_Type(Integer32):
    """Custom type zxr10natConfDynRuleOverlay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nooverlay", 0),
          ("overlay", 1))
    )


_Zxr10natConfDynRuleOverlay_Type.__name__ = "Integer32"
_Zxr10natConfDynRuleOverlay_Object = MibTableColumn
zxr10natConfDynRuleOverlay = _Zxr10natConfDynRuleOverlay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 3),
    _Zxr10natConfDynRuleOverlay_Type()
)
zxr10natConfDynRuleOverlay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfDynRuleOverlay.setStatus("current")
_Zxr10natConfDynInterfaceName_Type = DisplayString
_Zxr10natConfDynInterfaceName_Object = MibTableColumn
zxr10natConfDynInterfaceName = _Zxr10natConfDynInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 4),
    _Zxr10natConfDynInterfaceName_Type()
)
zxr10natConfDynInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfDynInterfaceName.setStatus("current")
_Zxr10natConfDynGlobalIpStart_Type = IpAddress
_Zxr10natConfDynGlobalIpStart_Object = MibTableColumn
zxr10natConfDynGlobalIpStart = _Zxr10natConfDynGlobalIpStart_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 5),
    _Zxr10natConfDynGlobalIpStart_Type()
)
zxr10natConfDynGlobalIpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfDynGlobalIpStart.setStatus("current")
_Zxr10natConfDynGlobalIpRange_Type = Integer32
_Zxr10natConfDynGlobalIpRange_Object = MibTableColumn
zxr10natConfDynGlobalIpRange = _Zxr10natConfDynGlobalIpRange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 6),
    _Zxr10natConfDynGlobalIpRange_Type()
)
zxr10natConfDynGlobalIpRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natConfDynGlobalIpRange.setStatus("current")
_Zxr10natStatistic_ObjectIdentity = ObjectIdentity
zxr10natStatistic = _Zxr10natStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2)
)
_Zxr10natHitStatsTotal_Type = Integer32
_Zxr10natHitStatsTotal_Object = MibScalar
zxr10natHitStatsTotal = _Zxr10natHitStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 1),
    _Zxr10natHitStatsTotal_Type()
)
zxr10natHitStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natHitStatsTotal.setStatus("current")
_Zxr10natHitStatsFwd_Type = Integer32
_Zxr10natHitStatsFwd_Object = MibScalar
zxr10natHitStatsFwd = _Zxr10natHitStatsFwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 2),
    _Zxr10natHitStatsFwd_Type()
)
zxr10natHitStatsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natHitStatsFwd.setStatus("current")
_Zxr10natHitStatsProtocl_Type = Integer32
_Zxr10natHitStatsProtocl_Object = MibScalar
zxr10natHitStatsProtocl = _Zxr10natHitStatsProtocl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 3),
    _Zxr10natHitStatsProtocl_Type()
)
zxr10natHitStatsProtocl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natHitStatsProtocl.setStatus("current")
_Zxr10natHitStatsUEng_Type = Integer32
_Zxr10natHitStatsUEng_Object = MibScalar
zxr10natHitStatsUEng = _Zxr10natHitStatsUEng_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 4),
    _Zxr10natHitStatsUEng_Type()
)
zxr10natHitStatsUEng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natHitStatsUEng.setStatus("current")
_Zxr10natMissStatsTotal_Type = Integer32
_Zxr10natMissStatsTotal_Object = MibScalar
zxr10natMissStatsTotal = _Zxr10natMissStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 5),
    _Zxr10natMissStatsTotal_Type()
)
zxr10natMissStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natMissStatsTotal.setStatus("current")
_Zxr10natMissStatsFwd_Type = Integer32
_Zxr10natMissStatsFwd_Object = MibScalar
zxr10natMissStatsFwd = _Zxr10natMissStatsFwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 6),
    _Zxr10natMissStatsFwd_Type()
)
zxr10natMissStatsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natMissStatsFwd.setStatus("current")
_Zxr10natMissStatsProtocol_Type = Integer32
_Zxr10natMissStatsProtocol_Object = MibScalar
zxr10natMissStatsProtocol = _Zxr10natMissStatsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 7),
    _Zxr10natMissStatsProtocol_Type()
)
zxr10natMissStatsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natMissStatsProtocol.setStatus("current")
_Zxr10natMissStatsUEng_Type = Integer32
_Zxr10natMissStatsUEng_Object = MibScalar
zxr10natMissStatsUEng = _Zxr10natMissStatsUEng_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 8),
    _Zxr10natMissStatsUEng_Type()
)
zxr10natMissStatsUEng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natMissStatsUEng.setStatus("current")
_Zxr10natTimeoutStatsTotal_Type = Integer32
_Zxr10natTimeoutStatsTotal_Object = MibScalar
zxr10natTimeoutStatsTotal = _Zxr10natTimeoutStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 9),
    _Zxr10natTimeoutStatsTotal_Type()
)
zxr10natTimeoutStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natTimeoutStatsTotal.setStatus("current")
_Zxr10natMappingStatsTotal_Type = Integer32
_Zxr10natMappingStatsTotal_Object = MibScalar
zxr10natMappingStatsTotal = _Zxr10natMappingStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 10),
    _Zxr10natMappingStatsTotal_Type()
)
zxr10natMappingStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natMappingStatsTotal.setStatus("current")
_Zxr10natMappingUsedStatsTotal_Type = Integer32
_Zxr10natMappingUsedStatsTotal_Object = MibScalar
zxr10natMappingUsedStatsTotal = _Zxr10natMappingUsedStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 11),
    _Zxr10natMappingUsedStatsTotal_Type()
)
zxr10natMappingUsedStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natMappingUsedStatsTotal.setStatus("current")
_Zxr10natMappingStatsStaticRule_Type = Integer32
_Zxr10natMappingStatsStaticRule_Object = MibScalar
zxr10natMappingStatsStaticRule = _Zxr10natMappingStatsStaticRule_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 12),
    _Zxr10natMappingStatsStaticRule_Type()
)
zxr10natMappingStatsStaticRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natMappingStatsStaticRule.setStatus("current")
_Zxr10natMappingStatsDynRule_Type = Integer32
_Zxr10natMappingStatsDynRule_Object = MibScalar
zxr10natMappingStatsDynRule = _Zxr10natMappingStatsDynRule_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 13),
    _Zxr10natMappingStatsDynRule_Type()
)
zxr10natMappingStatsDynRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natMappingStatsDynRule.setStatus("current")
_Zxr10natMappingStatsMax_Type = Integer32
_Zxr10natMappingStatsMax_Object = MibScalar
zxr10natMappingStatsMax = _Zxr10natMappingStatsMax_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 14),
    _Zxr10natMappingStatsMax_Type()
)
zxr10natMappingStatsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natMappingStatsMax.setStatus("current")
_Zxr10natStaticMapping_ObjectIdentity = ObjectIdentity
zxr10natStaticMapping = _Zxr10natStaticMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3)
)
_Zxr10natStaticMappingTable_Object = MibTable
zxr10natStaticMappingTable = _Zxr10natStaticMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1)
)
if mibBuilder.loadTexts:
    zxr10natStaticMappingTable.setStatus("current")
_Zxr10natStaticMappingEntry_Object = MibTableRow
zxr10natStaticMappingEntry = _Zxr10natStaticMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1)
)
zxr10natStaticMappingEntry.setIndexNames(
    (0, "ZXR10-NAT-MIB", "zxr10natStaticRuleIndex"),
)
if mibBuilder.loadTexts:
    zxr10natStaticMappingEntry.setStatus("current")
_Zxr10natStaticRuleIndex_Type = Integer32
_Zxr10natStaticRuleIndex_Object = MibTableColumn
zxr10natStaticRuleIndex = _Zxr10natStaticRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 1),
    _Zxr10natStaticRuleIndex_Type()
)
zxr10natStaticRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natStaticRuleIndex.setStatus("current")
_Zxr10natStaticMappingLocalIpaddr_Type = IpAddress
_Zxr10natStaticMappingLocalIpaddr_Object = MibTableColumn
zxr10natStaticMappingLocalIpaddr = _Zxr10natStaticMappingLocalIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 2),
    _Zxr10natStaticMappingLocalIpaddr_Type()
)
zxr10natStaticMappingLocalIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natStaticMappingLocalIpaddr.setStatus("current")
_Zxr10natStaticMappingLocalPort_Type = Integer32
_Zxr10natStaticMappingLocalPort_Object = MibTableColumn
zxr10natStaticMappingLocalPort = _Zxr10natStaticMappingLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 3),
    _Zxr10natStaticMappingLocalPort_Type()
)
zxr10natStaticMappingLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natStaticMappingLocalPort.setStatus("current")
_Zxr10natStaticMappingGlobalIpaddr_Type = IpAddress
_Zxr10natStaticMappingGlobalIpaddr_Object = MibTableColumn
zxr10natStaticMappingGlobalIpaddr = _Zxr10natStaticMappingGlobalIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 4),
    _Zxr10natStaticMappingGlobalIpaddr_Type()
)
zxr10natStaticMappingGlobalIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natStaticMappingGlobalIpaddr.setStatus("current")
_Zxr10natStaticMappingGlobalPort_Type = Integer32
_Zxr10natStaticMappingGlobalPort_Object = MibTableColumn
zxr10natStaticMappingGlobalPort = _Zxr10natStaticMappingGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 5),
    _Zxr10natStaticMappingGlobalPort_Type()
)
zxr10natStaticMappingGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10natStaticMappingGlobalPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-NAT-MIB",
    **{"Zxr10NatType": Zxr10NatType,
       "DisplayString": DisplayString,
       "zxr10nat": zxr10nat,
       "zxr10natConfig": zxr10natConfig,
       "zxr10natConfEnable": zxr10natConfEnable,
       "zxr10natInterfaceTable": zxr10natInterfaceTable,
       "zxr10natInterfaceEntry": zxr10natInterfaceEntry,
       "zxr10natInterfaceIndex": zxr10natInterfaceIndex,
       "zxr10natInterfaceName": zxr10natInterfaceName,
       "zxr10natInterfaceStorageType": zxr10natInterfaceStorageType,
       "zxr10natConfigTimeout": zxr10natConfigTimeout,
       "zxr10natConfTimeoutClassTable": zxr10natConfTimeoutClassTable,
       "zxr10natConfTimeoutClassEntry": zxr10natConfTimeoutClassEntry,
       "zxr10natConfTimeoutClassIndex": zxr10natConfTimeoutClassIndex,
       "zxr10natConfTimeoutClassValue": zxr10natConfTimeoutClassValue,
       "zxr10natConfTimeoutProtocolTable": zxr10natConfTimeoutProtocolTable,
       "zxr10natConfTimeoutProtocolEntry": zxr10natConfTimeoutProtocolEntry,
       "zxr10natConfTimeoutProtocolIndex": zxr10natConfTimeoutProtocolIndex,
       "zxr10natConfTimeoutProtocol": zxr10natConfTimeoutProtocol,
       "zxr10natConfTimeoutPort": zxr10natConfTimeoutPort,
       "zxr10natConfTimeoutClass": zxr10natConfTimeoutClass,
       "zxr10natConfigMaximal": zxr10natConfigMaximal,
       "zxr10natConfMaximalDefault": zxr10natConfMaximalDefault,
       "zxr10natConfMaximalTable": zxr10natConfMaximalTable,
       "zxr10natConfMaximalEntry": zxr10natConfMaximalEntry,
       "zxr10natConfMaximalAclNo": zxr10natConfMaximalAclNo,
       "zxr10natConfMaximalVlaue": zxr10natConfMaximalVlaue,
       "zxr10natConfStaticAddrMapTable": zxr10natConfStaticAddrMapTable,
       "zxr10natConfStaticAddrMapEntry": zxr10natConfStaticAddrMapEntry,
       "zxr10natConfStaticRuleIndex": zxr10natConfStaticRuleIndex,
       "zxr10natConfStaticLocalAddr": zxr10natConfStaticLocalAddr,
       "zxr10natConfStaticLocalPort": zxr10natConfStaticLocalPort,
       "zxr10natConfStaticGlobalAddr": zxr10natConfStaticGlobalAddr,
       "zxr10natConfStaticGlobalPort": zxr10natConfStaticGlobalPort,
       "zxr10natConfStaticProtoType": zxr10natConfStaticProtoType,
       "zxr10natConfDynAddrMapTable": zxr10natConfDynAddrMapTable,
       "zxr10natConfDynAddrMapEntry": zxr10natConfDynAddrMapEntry,
       "zxr10natConfDynRuleIndex": zxr10natConfDynRuleIndex,
       "zxr10natConfDynAccessListNum": zxr10natConfDynAccessListNum,
       "zxr10natConfDynRuleOverlay": zxr10natConfDynRuleOverlay,
       "zxr10natConfDynInterfaceName": zxr10natConfDynInterfaceName,
       "zxr10natConfDynGlobalIpStart": zxr10natConfDynGlobalIpStart,
       "zxr10natConfDynGlobalIpRange": zxr10natConfDynGlobalIpRange,
       "zxr10natStatistic": zxr10natStatistic,
       "zxr10natHitStatsTotal": zxr10natHitStatsTotal,
       "zxr10natHitStatsFwd": zxr10natHitStatsFwd,
       "zxr10natHitStatsProtocl": zxr10natHitStatsProtocl,
       "zxr10natHitStatsUEng": zxr10natHitStatsUEng,
       "zxr10natMissStatsTotal": zxr10natMissStatsTotal,
       "zxr10natMissStatsFwd": zxr10natMissStatsFwd,
       "zxr10natMissStatsProtocol": zxr10natMissStatsProtocol,
       "zxr10natMissStatsUEng": zxr10natMissStatsUEng,
       "zxr10natTimeoutStatsTotal": zxr10natTimeoutStatsTotal,
       "zxr10natMappingStatsTotal": zxr10natMappingStatsTotal,
       "zxr10natMappingUsedStatsTotal": zxr10natMappingUsedStatsTotal,
       "zxr10natMappingStatsStaticRule": zxr10natMappingStatsStaticRule,
       "zxr10natMappingStatsDynRule": zxr10natMappingStatsDynRule,
       "zxr10natMappingStatsMax": zxr10natMappingStatsMax,
       "zxr10natStaticMapping": zxr10natStaticMapping,
       "zxr10natStaticMappingTable": zxr10natStaticMappingTable,
       "zxr10natStaticMappingEntry": zxr10natStaticMappingEntry,
       "zxr10natStaticRuleIndex": zxr10natStaticRuleIndex,
       "zxr10natStaticMappingLocalIpaddr": zxr10natStaticMappingLocalIpaddr,
       "zxr10natStaticMappingLocalPort": zxr10natStaticMappingLocalPort,
       "zxr10natStaticMappingGlobalIpaddr": zxr10natStaticMappingGlobalIpaddr,
       "zxr10natStaticMappingGlobalPort": zxr10natStaticMappingGlobalPort}
)
