# SNMP MIB module (MY-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:14 2024
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex")

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

myAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17)
)
myAclMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyAclMIBObjects_ObjectIdentity = ObjectIdentity
myAclMIBObjects = _MyAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1)
)
_MyAclTable_Object = MibTable
myAclTable = _MyAclTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    myAclTable.setStatus("current")
_MyAclEntry_Object = MibTableRow
myAclEntry = _MyAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1, 1)
)
myAclEntry.setIndexNames(
    (0, "MY-ACL-MIB", "myAclName"),
)
if mibBuilder.loadTexts:
    myAclEntry.setStatus("current")


class _MyAclName_Type(DisplayString):
    """Custom type myAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyAclName_Type.__name__ = "DisplayString"
_MyAclName_Object = MibTableColumn
myAclName = _MyAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1, 1, 1),
    _MyAclName_Type()
)
myAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAclName.setStatus("current")


class _MyAclMode_Type(Integer32):
    """Custom type myAclMode based on Integer32"""
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
        *(("acl-expert", 4),
          ("acl-ip-extended", 2),
          ("acl-ip-standard", 1),
          ("acl-ipv6-extended", 5),
          ("acl-mac-extended", 3))
    )


_MyAclMode_Type.__name__ = "Integer32"
_MyAclMode_Object = MibTableColumn
myAclMode = _MyAclMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1, 1, 2),
    _MyAclMode_Type()
)
myAclMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myAclMode.setStatus("current")
_MyAclEntryStatus_Type = ConfigStatus
_MyAclEntryStatus_Object = MibTableColumn
myAclEntryStatus = _MyAclEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1, 1, 3),
    _MyAclEntryStatus_Type()
)
myAclEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myAclEntryStatus.setStatus("current")
_MyAclIfTable_Object = MibTable
myAclIfTable = _MyAclIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3)
)
if mibBuilder.loadTexts:
    myAclIfTable.setStatus("current")
_MyAclIfEntry_Object = MibTableRow
myAclIfEntry = _MyAclIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1)
)
myAclIfEntry.setIndexNames(
    (0, "MY-ACL-MIB", "myAclIfIndex"),
)
if mibBuilder.loadTexts:
    myAclIfEntry.setStatus("current")
_MyAclIfIndex_Type = IfIndex
_MyAclIfIndex_Object = MibTableColumn
myAclIfIndex = _MyAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 1),
    _MyAclIfIndex_Type()
)
myAclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAclIfIndex.setStatus("current")
_MyAclIfMaxEntryNum_Type = Integer32
_MyAclIfMaxEntryNum_Object = MibTableColumn
myAclIfMaxEntryNum = _MyAclIfMaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 2),
    _MyAclIfMaxEntryNum_Type()
)
myAclIfMaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAclIfMaxEntryNum.setStatus("current")
_MyAclIfCurruntEntryNum_Type = Integer32
_MyAclIfCurruntEntryNum_Object = MibTableColumn
myAclIfCurruntEntryNum = _MyAclIfCurruntEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 3),
    _MyAclIfCurruntEntryNum_Type()
)
myAclIfCurruntEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAclIfCurruntEntryNum.setStatus("current")


class _MyIfInAclName_Type(DisplayString):
    """Custom type myIfInAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyIfInAclName_Type.__name__ = "DisplayString"
_MyIfInAclName_Object = MibTableColumn
myIfInAclName = _MyIfInAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 4),
    _MyIfInAclName_Type()
)
myIfInAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfInAclName.setStatus("current")


class _MyIfOutAclName_Type(DisplayString):
    """Custom type myIfOutAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyIfOutAclName_Type.__name__ = "DisplayString"
_MyIfOutAclName_Object = MibTableColumn
myIfOutAclName = _MyIfOutAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 5),
    _MyIfOutAclName_Type()
)
myIfOutAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfOutAclName.setStatus("current")
_MyAceExtTable_Object = MibTable
myAceExtTable = _MyAceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4)
)
if mibBuilder.loadTexts:
    myAceExtTable.setStatus("current")
_MyAceExtEntry_Object = MibTableRow
myAceExtEntry = _MyAceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1)
)
myAceExtEntry.setIndexNames(
    (0, "MY-ACL-MIB", "myAceExtAclName"),
    (0, "MY-ACL-MIB", "myAceExtIndex"),
)
if mibBuilder.loadTexts:
    myAceExtEntry.setStatus("current")


class _MyAceExtAclName_Type(DisplayString):
    """Custom type myAceExtAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyAceExtAclName_Type.__name__ = "DisplayString"
_MyAceExtAclName_Object = MibTableColumn
myAceExtAclName = _MyAceExtAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 1),
    _MyAceExtAclName_Type()
)
myAceExtAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAceExtAclName.setStatus("current")


class _MyAceExtIndex_Type(Integer32):
    """Custom type myAceExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MyAceExtIndex_Type.__name__ = "Integer32"
_MyAceExtIndex_Object = MibTableColumn
myAceExtIndex = _MyAceExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 2),
    _MyAceExtIndex_Type()
)
myAceExtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAceExtIndex.setStatus("current")


class _MyAceExtIfAnyVID_Type(TruthValue):
    """Custom type myAceExtIfAnyVID based on TruthValue"""


_MyAceExtIfAnyVID_Object = MibTableColumn
myAceExtIfAnyVID = _MyAceExtIfAnyVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 3),
    _MyAceExtIfAnyVID_Type()
)
myAceExtIfAnyVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyVID.setStatus("current")


class _MyAceExtVID_Type(Unsigned32):
    """Custom type myAceExtVID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MyAceExtVID_Type.__name__ = "Unsigned32"
_MyAceExtVID_Object = MibTableColumn
myAceExtVID = _MyAceExtVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 4),
    _MyAceExtVID_Type()
)
myAceExtVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtVID.setStatus("current")


class _MyAceExtIfAnySourceIp_Type(TruthValue):
    """Custom type myAceExtIfAnySourceIp based on TruthValue"""


_MyAceExtIfAnySourceIp_Object = MibTableColumn
myAceExtIfAnySourceIp = _MyAceExtIfAnySourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 5),
    _MyAceExtIfAnySourceIp_Type()
)
myAceExtIfAnySourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnySourceIp.setStatus("current")
_MyAceExtSourceIp_Type = IpAddress
_MyAceExtSourceIp_Object = MibTableColumn
myAceExtSourceIp = _MyAceExtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 6),
    _MyAceExtSourceIp_Type()
)
myAceExtSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtSourceIp.setStatus("current")


class _MyAceExtIfAnySourceWildCard_Type(TruthValue):
    """Custom type myAceExtIfAnySourceWildCard based on TruthValue"""


_MyAceExtIfAnySourceWildCard_Object = MibTableColumn
myAceExtIfAnySourceWildCard = _MyAceExtIfAnySourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 7),
    _MyAceExtIfAnySourceWildCard_Type()
)
myAceExtIfAnySourceWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnySourceWildCard.setStatus("current")
_MyAceExtSourceWildCard_Type = IpAddress
_MyAceExtSourceWildCard_Object = MibTableColumn
myAceExtSourceWildCard = _MyAceExtSourceWildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 8),
    _MyAceExtSourceWildCard_Type()
)
myAceExtSourceWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtSourceWildCard.setStatus("current")


class _MyAceExtIfAnySourceMacAddr_Type(TruthValue):
    """Custom type myAceExtIfAnySourceMacAddr based on TruthValue"""


_MyAceExtIfAnySourceMacAddr_Object = MibTableColumn
myAceExtIfAnySourceMacAddr = _MyAceExtIfAnySourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 9),
    _MyAceExtIfAnySourceMacAddr_Type()
)
myAceExtIfAnySourceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnySourceMacAddr.setStatus("current")
_MyAceExtSourceMacAddr_Type = MacAddress
_MyAceExtSourceMacAddr_Object = MibTableColumn
myAceExtSourceMacAddr = _MyAceExtSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 10),
    _MyAceExtSourceMacAddr_Type()
)
myAceExtSourceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtSourceMacAddr.setStatus("current")


class _MyAceExtIfAnyDestIp_Type(TruthValue):
    """Custom type myAceExtIfAnyDestIp based on TruthValue"""


_MyAceExtIfAnyDestIp_Object = MibTableColumn
myAceExtIfAnyDestIp = _MyAceExtIfAnyDestIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 11),
    _MyAceExtIfAnyDestIp_Type()
)
myAceExtIfAnyDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyDestIp.setStatus("current")
_MyAceExtDestIp_Type = IpAddress
_MyAceExtDestIp_Object = MibTableColumn
myAceExtDestIp = _MyAceExtDestIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 12),
    _MyAceExtDestIp_Type()
)
myAceExtDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDestIp.setStatus("current")


class _MyAceExtIfAnyDestWildCard_Type(TruthValue):
    """Custom type myAceExtIfAnyDestWildCard based on TruthValue"""


_MyAceExtIfAnyDestWildCard_Object = MibTableColumn
myAceExtIfAnyDestWildCard = _MyAceExtIfAnyDestWildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 13),
    _MyAceExtIfAnyDestWildCard_Type()
)
myAceExtIfAnyDestWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyDestWildCard.setStatus("current")
_MyAceExtDestIpWildCard_Type = IpAddress
_MyAceExtDestIpWildCard_Object = MibTableColumn
myAceExtDestIpWildCard = _MyAceExtDestIpWildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 14),
    _MyAceExtDestIpWildCard_Type()
)
myAceExtDestIpWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDestIpWildCard.setStatus("current")


class _MyAceExtIfAnyDestMacAddr_Type(TruthValue):
    """Custom type myAceExtIfAnyDestMacAddr based on TruthValue"""


_MyAceExtIfAnyDestMacAddr_Object = MibTableColumn
myAceExtIfAnyDestMacAddr = _MyAceExtIfAnyDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 15),
    _MyAceExtIfAnyDestMacAddr_Type()
)
myAceExtIfAnyDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyDestMacAddr.setStatus("current")
_MyAceExtDestMacAddr_Type = MacAddress
_MyAceExtDestMacAddr_Object = MibTableColumn
myAceExtDestMacAddr = _MyAceExtDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 16),
    _MyAceExtDestMacAddr_Type()
)
myAceExtDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDestMacAddr.setStatus("current")


class _MyAceExtIfAnyEtherLikeType_Type(TruthValue):
    """Custom type myAceExtIfAnyEtherLikeType based on TruthValue"""


_MyAceExtIfAnyEtherLikeType_Object = MibTableColumn
myAceExtIfAnyEtherLikeType = _MyAceExtIfAnyEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 17),
    _MyAceExtIfAnyEtherLikeType_Type()
)
myAceExtIfAnyEtherLikeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyEtherLikeType.setStatus("current")
_MyAceExtEtherLikeType_Type = Integer32
_MyAceExtEtherLikeType_Object = MibTableColumn
myAceExtEtherLikeType = _MyAceExtEtherLikeType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 18),
    _MyAceExtEtherLikeType_Type()
)
myAceExtEtherLikeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtEtherLikeType.setStatus("current")


class _MyAceExtIfAnyIpProtocolField_Type(TruthValue):
    """Custom type myAceExtIfAnyIpProtocolField based on TruthValue"""


_MyAceExtIfAnyIpProtocolField_Object = MibTableColumn
myAceExtIfAnyIpProtocolField = _MyAceExtIfAnyIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 19),
    _MyAceExtIfAnyIpProtocolField_Type()
)
myAceExtIfAnyIpProtocolField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyIpProtocolField.setStatus("current")
_MyAceExtIpProtocolField_Type = Integer32
_MyAceExtIpProtocolField_Object = MibTableColumn
myAceExtIpProtocolField = _MyAceExtIpProtocolField_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 20),
    _MyAceExtIpProtocolField_Type()
)
myAceExtIpProtocolField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIpProtocolField.setStatus("current")
_MyAceExtSourceProtocolPort_Type = Integer32
_MyAceExtSourceProtocolPort_Object = MibTableColumn
myAceExtSourceProtocolPort = _MyAceExtSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 21),
    _MyAceExtSourceProtocolPort_Type()
)
myAceExtSourceProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtSourceProtocolPort.setStatus("current")
_MyAceExtDestProtocolPort_Type = Integer32
_MyAceExtDestProtocolPort_Object = MibTableColumn
myAceExtDestProtocolPort = _MyAceExtDestProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 22),
    _MyAceExtDestProtocolPort_Type()
)
myAceExtDestProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDestProtocolPort.setStatus("current")


class _MyAceExtIfAnyProtocolType_Type(TruthValue):
    """Custom type myAceExtIfAnyProtocolType based on TruthValue"""


_MyAceExtIfAnyProtocolType_Object = MibTableColumn
myAceExtIfAnyProtocolType = _MyAceExtIfAnyProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 23),
    _MyAceExtIfAnyProtocolType_Type()
)
myAceExtIfAnyProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyProtocolType.setStatus("current")
_MyAceExtProtocolType_Type = Integer32
_MyAceExtProtocolType_Object = MibTableColumn
myAceExtProtocolType = _MyAceExtProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 24),
    _MyAceExtProtocolType_Type()
)
myAceExtProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtProtocolType.setStatus("current")


class _MyAceExtFlowAction_Type(Integer32):
    """Custom type myAceExtFlowAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_MyAceExtFlowAction_Type.__name__ = "Integer32"
_MyAceExtFlowAction_Object = MibTableColumn
myAceExtFlowAction = _MyAceExtFlowAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 25),
    _MyAceExtFlowAction_Type()
)
myAceExtFlowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtFlowAction.setStatus("current")
_MyAceExtEntryStauts_Type = RowStatus
_MyAceExtEntryStauts_Object = MibTableColumn
myAceExtEntryStauts = _MyAceExtEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 26),
    _MyAceExtEntryStauts_Type()
)
myAceExtEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myAceExtEntryStauts.setStatus("current")


class _MyAceExtTimeRangeName_Type(DisplayString):
    """Custom type myAceExtTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyAceExtTimeRangeName_Type.__name__ = "DisplayString"
_MyAceExtTimeRangeName_Object = MibTableColumn
myAceExtTimeRangeName = _MyAceExtTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 27),
    _MyAceExtTimeRangeName_Type()
)
myAceExtTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtTimeRangeName.setStatus("current")


class _MyAceExtSourcePortOp_Type(Integer32):
    """Custom type myAceExtSourcePortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eq", 4),
          ("gt", 3),
          ("lt", 2),
          ("neq", 5),
          ("noOperator", 1),
          ("range", 6))
    )


_MyAceExtSourcePortOp_Type.__name__ = "Integer32"
_MyAceExtSourcePortOp_Object = MibTableColumn
myAceExtSourcePortOp = _MyAceExtSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 28),
    _MyAceExtSourcePortOp_Type()
)
myAceExtSourcePortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtSourcePortOp.setStatus("current")
_MyAceExtSourceProtocolPortRange_Type = Integer32
_MyAceExtSourceProtocolPortRange_Object = MibTableColumn
myAceExtSourceProtocolPortRange = _MyAceExtSourceProtocolPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 29),
    _MyAceExtSourceProtocolPortRange_Type()
)
myAceExtSourceProtocolPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtSourceProtocolPortRange.setStatus("current")


class _MyAceExtDestPortOp_Type(Integer32):
    """Custom type myAceExtDestPortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eq", 4),
          ("gt", 3),
          ("lt", 2),
          ("neq", 5),
          ("noOperator", 1),
          ("range", 6))
    )


_MyAceExtDestPortOp_Type.__name__ = "Integer32"
_MyAceExtDestPortOp_Object = MibTableColumn
myAceExtDestPortOp = _MyAceExtDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 30),
    _MyAceExtDestPortOp_Type()
)
myAceExtDestPortOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDestPortOp.setStatus("current")
_MyAceExtDestProtocolPortRange_Type = Integer32
_MyAceExtDestProtocolPortRange_Object = MibTableColumn
myAceExtDestProtocolPortRange = _MyAceExtDestProtocolPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 31),
    _MyAceExtDestProtocolPortRange_Type()
)
myAceExtDestProtocolPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDestProtocolPortRange.setStatus("current")


class _MyAceExtIfAnyCos_Type(TruthValue):
    """Custom type myAceExtIfAnyCos based on TruthValue"""


_MyAceExtIfAnyCos_Object = MibTableColumn
myAceExtIfAnyCos = _MyAceExtIfAnyCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 32),
    _MyAceExtIfAnyCos_Type()
)
myAceExtIfAnyCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyCos.setStatus("current")
_MyAceExtCos_Type = Integer32
_MyAceExtCos_Object = MibTableColumn
myAceExtCos = _MyAceExtCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 33),
    _MyAceExtCos_Type()
)
myAceExtCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtCos.setStatus("current")


class _MyAceExtIfAnyIpPrec_Type(TruthValue):
    """Custom type myAceExtIfAnyIpPrec based on TruthValue"""


_MyAceExtIfAnyIpPrec_Object = MibTableColumn
myAceExtIfAnyIpPrec = _MyAceExtIfAnyIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 34),
    _MyAceExtIfAnyIpPrec_Type()
)
myAceExtIfAnyIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyIpPrec.setStatus("current")
_MyAceExtIpPrec_Type = Integer32
_MyAceExtIpPrec_Object = MibTableColumn
myAceExtIpPrec = _MyAceExtIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 35),
    _MyAceExtIpPrec_Type()
)
myAceExtIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIpPrec.setStatus("current")


class _MyAceExtIfAnyDscp_Type(TruthValue):
    """Custom type myAceExtIfAnyDscp based on TruthValue"""


_MyAceExtIfAnyDscp_Object = MibTableColumn
myAceExtIfAnyDscp = _MyAceExtIfAnyDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 36),
    _MyAceExtIfAnyDscp_Type()
)
myAceExtIfAnyDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyDscp.setStatus("current")
_MyAceExtDscp_Type = Integer32
_MyAceExtDscp_Object = MibTableColumn
myAceExtDscp = _MyAceExtDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 37),
    _MyAceExtDscp_Type()
)
myAceExtDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDscp.setStatus("current")


class _MyAceExtIfAnyTcpFlag_Type(TruthValue):
    """Custom type myAceExtIfAnyTcpFlag based on TruthValue"""


_MyAceExtIfAnyTcpFlag_Object = MibTableColumn
myAceExtIfAnyTcpFlag = _MyAceExtIfAnyTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 38),
    _MyAceExtIfAnyTcpFlag_Type()
)
myAceExtIfAnyTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyTcpFlag.setStatus("current")
_MyAceExtTcpFlag_Type = Integer32
_MyAceExtTcpFlag_Object = MibTableColumn
myAceExtTcpFlag = _MyAceExtTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 39),
    _MyAceExtTcpFlag_Type()
)
myAceExtTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtTcpFlag.setStatus("current")


class _MyAceExtIfAnySourceMacAddrWildCard_Type(TruthValue):
    """Custom type myAceExtIfAnySourceMacAddrWildCard based on TruthValue"""


_MyAceExtIfAnySourceMacAddrWildCard_Object = MibTableColumn
myAceExtIfAnySourceMacAddrWildCard = _MyAceExtIfAnySourceMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 40),
    _MyAceExtIfAnySourceMacAddrWildCard_Type()
)
myAceExtIfAnySourceMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnySourceMacAddrWildCard.setStatus("current")
_MyAceExtSourceMacAddrWildCard_Type = MacAddress
_MyAceExtSourceMacAddrWildCard_Object = MibTableColumn
myAceExtSourceMacAddrWildCard = _MyAceExtSourceMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 41),
    _MyAceExtSourceMacAddrWildCard_Type()
)
myAceExtSourceMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtSourceMacAddrWildCard.setStatus("current")


class _MyAceExtIfAnyDestMacAddrWildCard_Type(TruthValue):
    """Custom type myAceExtIfAnyDestMacAddrWildCard based on TruthValue"""


_MyAceExtIfAnyDestMacAddrWildCard_Object = MibTableColumn
myAceExtIfAnyDestMacAddrWildCard = _MyAceExtIfAnyDestMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 42),
    _MyAceExtIfAnyDestMacAddrWildCard_Type()
)
myAceExtIfAnyDestMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyDestMacAddrWildCard.setStatus("current")
_MyAceExtDestMacAddrWildCard_Type = MacAddress
_MyAceExtDestMacAddrWildCard_Object = MibTableColumn
myAceExtDestMacAddrWildCard = _MyAceExtDestMacAddrWildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 43),
    _MyAceExtDestMacAddrWildCard_Type()
)
myAceExtDestMacAddrWildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDestMacAddrWildCard.setStatus("current")


class _MyAceExtIfAnySourceIp6_Type(TruthValue):
    """Custom type myAceExtIfAnySourceIp6 based on TruthValue"""


_MyAceExtIfAnySourceIp6_Object = MibTableColumn
myAceExtIfAnySourceIp6 = _MyAceExtIfAnySourceIp6_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 44),
    _MyAceExtIfAnySourceIp6_Type()
)
myAceExtIfAnySourceIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnySourceIp6.setStatus("current")


class _MyAceExtSourceIp6_Type(OctetString):
    """Custom type myAceExtSourceIp6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MyAceExtSourceIp6_Type.__name__ = "OctetString"
_MyAceExtSourceIp6_Object = MibTableColumn
myAceExtSourceIp6 = _MyAceExtSourceIp6_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 45),
    _MyAceExtSourceIp6_Type()
)
myAceExtSourceIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtSourceIp6.setStatus("current")


class _MyAceExtIfAnySourceIp6WildCard_Type(TruthValue):
    """Custom type myAceExtIfAnySourceIp6WildCard based on TruthValue"""


_MyAceExtIfAnySourceIp6WildCard_Object = MibTableColumn
myAceExtIfAnySourceIp6WildCard = _MyAceExtIfAnySourceIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 46),
    _MyAceExtIfAnySourceIp6WildCard_Type()
)
myAceExtIfAnySourceIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnySourceIp6WildCard.setStatus("current")


class _MyAceExtSourceIp6WildCard_Type(OctetString):
    """Custom type myAceExtSourceIp6WildCard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MyAceExtSourceIp6WildCard_Type.__name__ = "OctetString"
_MyAceExtSourceIp6WildCard_Object = MibTableColumn
myAceExtSourceIp6WildCard = _MyAceExtSourceIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 47),
    _MyAceExtSourceIp6WildCard_Type()
)
myAceExtSourceIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtSourceIp6WildCard.setStatus("current")


class _MyAceExtIfAnyDestIp6_Type(TruthValue):
    """Custom type myAceExtIfAnyDestIp6 based on TruthValue"""


_MyAceExtIfAnyDestIp6_Object = MibTableColumn
myAceExtIfAnyDestIp6 = _MyAceExtIfAnyDestIp6_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 48),
    _MyAceExtIfAnyDestIp6_Type()
)
myAceExtIfAnyDestIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyDestIp6.setStatus("current")


class _MyAceExtDestIp6_Type(OctetString):
    """Custom type myAceExtDestIp6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MyAceExtDestIp6_Type.__name__ = "OctetString"
_MyAceExtDestIp6_Object = MibTableColumn
myAceExtDestIp6 = _MyAceExtDestIp6_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 49),
    _MyAceExtDestIp6_Type()
)
myAceExtDestIp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDestIp6.setStatus("current")


class _MyAceExtIfAnyDestIp6WildCard_Type(TruthValue):
    """Custom type myAceExtIfAnyDestIp6WildCard based on TruthValue"""


_MyAceExtIfAnyDestIp6WildCard_Object = MibTableColumn
myAceExtIfAnyDestIp6WildCard = _MyAceExtIfAnyDestIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 50),
    _MyAceExtIfAnyDestIp6WildCard_Type()
)
myAceExtIfAnyDestIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtIfAnyDestIp6WildCard.setStatus("current")


class _MyAceExtDestIp6WildCard_Type(OctetString):
    """Custom type myAceExtDestIp6WildCard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MyAceExtDestIp6WildCard_Type.__name__ = "OctetString"
_MyAceExtDestIp6WildCard_Object = MibTableColumn
myAceExtDestIp6WildCard = _MyAceExtDestIp6WildCard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 51),
    _MyAceExtDestIp6WildCard_Type()
)
myAceExtDestIp6WildCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAceExtDestIp6WildCard.setStatus("current")
_MyAclMIBConformance_ObjectIdentity = ObjectIdentity
myAclMIBConformance = _MyAclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2)
)
_MyAclMIBCompliances_ObjectIdentity = ObjectIdentity
myAclMIBCompliances = _MyAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2, 1)
)
_MyAclMIBGroups_ObjectIdentity = ObjectIdentity
myAclMIBGroups = _MyAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2, 2)
)

# Managed Objects groups

myAclMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2, 2, 1)
)
myAclMIBGroup.setObjects(
      *(("MY-ACL-MIB", "myAclName"),
        ("MY-ACL-MIB", "myAclMode"),
        ("MY-ACL-MIB", "myAclEntryStatus"),
        ("MY-ACL-MIB", "myAceExtAclName"),
        ("MY-ACL-MIB", "myAceExtIndex"),
        ("MY-ACL-MIB", "myAceExtIfAnyVID"),
        ("MY-ACL-MIB", "myAceExtVID"),
        ("MY-ACL-MIB", "myAceExtIfAnySourceIp"),
        ("MY-ACL-MIB", "myAceExtSourceIp"),
        ("MY-ACL-MIB", "myAceExtIfAnySourceWildCard"),
        ("MY-ACL-MIB", "myAceExtSourceWildCard"),
        ("MY-ACL-MIB", "myAceExtIfAnySourceMacAddr"),
        ("MY-ACL-MIB", "myAceExtSourceMacAddr"),
        ("MY-ACL-MIB", "myAceExtIfAnyDestIp"),
        ("MY-ACL-MIB", "myAceExtDestIp"),
        ("MY-ACL-MIB", "myAceExtIfAnyDestWildCard"),
        ("MY-ACL-MIB", "myAceExtDestIpWildCard"),
        ("MY-ACL-MIB", "myAceExtIfAnyDestMacAddr"),
        ("MY-ACL-MIB", "myAceExtDestMacAddr"),
        ("MY-ACL-MIB", "myAceExtIfAnyEtherLikeType"),
        ("MY-ACL-MIB", "myAceExtEtherLikeType"),
        ("MY-ACL-MIB", "myAceExtIfAnyIpProtocolField"),
        ("MY-ACL-MIB", "myAceExtIpProtocolField"),
        ("MY-ACL-MIB", "myAceExtSourceProtocolPort"),
        ("MY-ACL-MIB", "myAceExtDestProtocolPort"),
        ("MY-ACL-MIB", "myAceExtProtocolType"),
        ("MY-ACL-MIB", "myAceExtProtocolType"),
        ("MY-ACL-MIB", "myAceExtFlowAction"),
        ("MY-ACL-MIB", "myAceExtEntryStauts"),
        ("MY-ACL-MIB", "myAceExtTimeRangeName"),
        ("MY-ACL-MIB", "myAceExtSourcePortOp"),
        ("MY-ACL-MIB", "myAceExtSourceProtocolPortRange"),
        ("MY-ACL-MIB", "myAceExtDestPortOp"),
        ("MY-ACL-MIB", "myAceExtDestProtocolPortRange"),
        ("MY-ACL-MIB", "myAceExtIfAnyCos"),
        ("MY-ACL-MIB", "myAceExtCos"),
        ("MY-ACL-MIB", "myAceExtIfAnyIpPrec"),
        ("MY-ACL-MIB", "myAceExtIpPrec"),
        ("MY-ACL-MIB", "myAceExtIfAnyDscp"),
        ("MY-ACL-MIB", "myAceExtDscp"),
        ("MY-ACL-MIB", "myAceExtIfAnyTcpFlag"),
        ("MY-ACL-MIB", "myAceExtTcpFlag"),
        ("MY-ACL-MIB", "myAceExtIfAnySourceMacAddrWildCard"),
        ("MY-ACL-MIB", "myAceExtSourceMacAddrWildCard"),
        ("MY-ACL-MIB", "myAceExtIfAnyDestMacAddrWildCard"),
        ("MY-ACL-MIB", "myAceExtDestMacAddrWildCard"),
        ("MY-ACL-MIB", "myAceExtIfAnySourceIp6"),
        ("MY-ACL-MIB", "myAceExtSourceIp6"),
        ("MY-ACL-MIB", "myAceExtIfAnySourceIp6WildCard"),
        ("MY-ACL-MIB", "myAceExtSourceIp6WildCard"),
        ("MY-ACL-MIB", "myAceExtIfAnyDestIp6"),
        ("MY-ACL-MIB", "myAceExtDestIp6"),
        ("MY-ACL-MIB", "myAceExtIfAnyDestIp6WildCard"),
        ("MY-ACL-MIB", "myAceExtDestIp6WildCard"),
        ("MY-ACL-MIB", "myAclIfIndex"),
        ("MY-ACL-MIB", "myAclIfMaxEntryNum"),
        ("MY-ACL-MIB", "myAclIfCurruntEntryNum"),
        ("MY-ACL-MIB", "myIfInAclName"),
        ("MY-ACL-MIB", "myIfOutAclName"))
)
if mibBuilder.loadTexts:
    myAclMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    myAclMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-ACL-MIB",
    **{"myAclMIB": myAclMIB,
       "myAclMIBObjects": myAclMIBObjects,
       "myAclTable": myAclTable,
       "myAclEntry": myAclEntry,
       "myAclName": myAclName,
       "myAclMode": myAclMode,
       "myAclEntryStatus": myAclEntryStatus,
       "myAclIfTable": myAclIfTable,
       "myAclIfEntry": myAclIfEntry,
       "myAclIfIndex": myAclIfIndex,
       "myAclIfMaxEntryNum": myAclIfMaxEntryNum,
       "myAclIfCurruntEntryNum": myAclIfCurruntEntryNum,
       "myIfInAclName": myIfInAclName,
       "myIfOutAclName": myIfOutAclName,
       "myAceExtTable": myAceExtTable,
       "myAceExtEntry": myAceExtEntry,
       "myAceExtAclName": myAceExtAclName,
       "myAceExtIndex": myAceExtIndex,
       "myAceExtIfAnyVID": myAceExtIfAnyVID,
       "myAceExtVID": myAceExtVID,
       "myAceExtIfAnySourceIp": myAceExtIfAnySourceIp,
       "myAceExtSourceIp": myAceExtSourceIp,
       "myAceExtIfAnySourceWildCard": myAceExtIfAnySourceWildCard,
       "myAceExtSourceWildCard": myAceExtSourceWildCard,
       "myAceExtIfAnySourceMacAddr": myAceExtIfAnySourceMacAddr,
       "myAceExtSourceMacAddr": myAceExtSourceMacAddr,
       "myAceExtIfAnyDestIp": myAceExtIfAnyDestIp,
       "myAceExtDestIp": myAceExtDestIp,
       "myAceExtIfAnyDestWildCard": myAceExtIfAnyDestWildCard,
       "myAceExtDestIpWildCard": myAceExtDestIpWildCard,
       "myAceExtIfAnyDestMacAddr": myAceExtIfAnyDestMacAddr,
       "myAceExtDestMacAddr": myAceExtDestMacAddr,
       "myAceExtIfAnyEtherLikeType": myAceExtIfAnyEtherLikeType,
       "myAceExtEtherLikeType": myAceExtEtherLikeType,
       "myAceExtIfAnyIpProtocolField": myAceExtIfAnyIpProtocolField,
       "myAceExtIpProtocolField": myAceExtIpProtocolField,
       "myAceExtSourceProtocolPort": myAceExtSourceProtocolPort,
       "myAceExtDestProtocolPort": myAceExtDestProtocolPort,
       "myAceExtIfAnyProtocolType": myAceExtIfAnyProtocolType,
       "myAceExtProtocolType": myAceExtProtocolType,
       "myAceExtFlowAction": myAceExtFlowAction,
       "myAceExtEntryStauts": myAceExtEntryStauts,
       "myAceExtTimeRangeName": myAceExtTimeRangeName,
       "myAceExtSourcePortOp": myAceExtSourcePortOp,
       "myAceExtSourceProtocolPortRange": myAceExtSourceProtocolPortRange,
       "myAceExtDestPortOp": myAceExtDestPortOp,
       "myAceExtDestProtocolPortRange": myAceExtDestProtocolPortRange,
       "myAceExtIfAnyCos": myAceExtIfAnyCos,
       "myAceExtCos": myAceExtCos,
       "myAceExtIfAnyIpPrec": myAceExtIfAnyIpPrec,
       "myAceExtIpPrec": myAceExtIpPrec,
       "myAceExtIfAnyDscp": myAceExtIfAnyDscp,
       "myAceExtDscp": myAceExtDscp,
       "myAceExtIfAnyTcpFlag": myAceExtIfAnyTcpFlag,
       "myAceExtTcpFlag": myAceExtTcpFlag,
       "myAceExtIfAnySourceMacAddrWildCard": myAceExtIfAnySourceMacAddrWildCard,
       "myAceExtSourceMacAddrWildCard": myAceExtSourceMacAddrWildCard,
       "myAceExtIfAnyDestMacAddrWildCard": myAceExtIfAnyDestMacAddrWildCard,
       "myAceExtDestMacAddrWildCard": myAceExtDestMacAddrWildCard,
       "myAceExtIfAnySourceIp6": myAceExtIfAnySourceIp6,
       "myAceExtSourceIp6": myAceExtSourceIp6,
       "myAceExtIfAnySourceIp6WildCard": myAceExtIfAnySourceIp6WildCard,
       "myAceExtSourceIp6WildCard": myAceExtSourceIp6WildCard,
       "myAceExtIfAnyDestIp6": myAceExtIfAnyDestIp6,
       "myAceExtDestIp6": myAceExtDestIp6,
       "myAceExtIfAnyDestIp6WildCard": myAceExtIfAnyDestIp6WildCard,
       "myAceExtDestIp6WildCard": myAceExtDestIp6WildCard,
       "myAclMIBConformance": myAclMIBConformance,
       "myAclMIBCompliances": myAclMIBCompliances,
       "myAclMIBCompliance": myAclMIBCompliance,
       "myAclMIBGroups": myAclMIBGroups,
       "myAclMIBGroup": myAclMIBGroup}
)
