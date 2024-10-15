# SNMP MIB module (MY-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:26 2024
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

mySecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6)
)
mySecurityMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MySecurityMIBObjects_ObjectIdentity = ObjectIdentity
mySecurityMIBObjects = _MySecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1)
)
_MyUserManagementObjects_ObjectIdentity = ObjectIdentity
myUserManagementObjects = _MyUserManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1)
)
_MyEnableSnmpAgent_Type = EnabledStatus
_MyEnableSnmpAgent_Object = MibScalar
myEnableSnmpAgent = _MyEnableSnmpAgent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 1),
    _MyEnableSnmpAgent_Type()
)
myEnableSnmpAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myEnableSnmpAgent.setStatus("current")
_MyEnableWeb_Type = EnabledStatus
_MyEnableWeb_Object = MibScalar
myEnableWeb = _MyEnableWeb_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 2),
    _MyEnableWeb_Type()
)
myEnableWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myEnableWeb.setStatus("current")
_MyEnableTelnet_Type = EnabledStatus
_MyEnableTelnet_Object = MibScalar
myEnableTelnet = _MyEnableTelnet_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 3),
    _MyEnableTelnet_Type()
)
myEnableTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myEnableTelnet.setStatus("current")
_MyTelnetHostIpTable_Object = MibTable
myTelnetHostIpTable = _MyTelnetHostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    myTelnetHostIpTable.setStatus("current")
_MyTelnetHostIpEntry_Object = MibTableRow
myTelnetHostIpEntry = _MyTelnetHostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 4, 1)
)
myTelnetHostIpEntry.setIndexNames(
    (0, "MY-SECURITY-MIB", "myTelnetHostIpAddress"),
)
if mibBuilder.loadTexts:
    myTelnetHostIpEntry.setStatus("current")
_MyTelnetHostIpAddress_Type = IpAddress
_MyTelnetHostIpAddress_Object = MibTableColumn
myTelnetHostIpAddress = _MyTelnetHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 4, 1, 1),
    _MyTelnetHostIpAddress_Type()
)
myTelnetHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myTelnetHostIpAddress.setStatus("current")


class _MyTelnetHostIpEnable_Type(Integer32):
    """Custom type myTelnetHostIpEnable based on Integer32"""
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


_MyTelnetHostIpEnable_Type.__name__ = "Integer32"
_MyTelnetHostIpEnable_Object = MibTableColumn
myTelnetHostIpEnable = _MyTelnetHostIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 4, 1, 2),
    _MyTelnetHostIpEnable_Type()
)
myTelnetHostIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTelnetHostIpEnable.setStatus("current")
_MyWebHostIpTable_Object = MibTable
myWebHostIpTable = _MyWebHostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    myWebHostIpTable.setStatus("current")
_MyWebHostIpEntry_Object = MibTableRow
myWebHostIpEntry = _MyWebHostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 5, 1)
)
myWebHostIpEntry.setIndexNames(
    (0, "MY-SECURITY-MIB", "myWebHostIpAddress"),
)
if mibBuilder.loadTexts:
    myWebHostIpEntry.setStatus("current")
_MyWebHostIpAddress_Type = IpAddress
_MyWebHostIpAddress_Object = MibTableColumn
myWebHostIpAddress = _MyWebHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 5, 1, 1),
    _MyWebHostIpAddress_Type()
)
myWebHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myWebHostIpAddress.setStatus("current")


class _MyWebHostIpEnable_Type(Integer32):
    """Custom type myWebHostIpEnable based on Integer32"""
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


_MyWebHostIpEnable_Type.__name__ = "Integer32"
_MyWebHostIpEnable_Object = MibTableColumn
myWebHostIpEnable = _MyWebHostIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 1, 5, 1, 2),
    _MyWebHostIpEnable_Type()
)
myWebHostIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myWebHostIpEnable.setStatus("current")
_MySecurityAddressObjects_ObjectIdentity = ObjectIdentity
mySecurityAddressObjects = _MySecurityAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2)
)
_MySecurityAddressTable_Object = MibTable
mySecurityAddressTable = _MySecurityAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mySecurityAddressTable.setStatus("current")
_MySecurityAddressEntry_Object = MibTableRow
mySecurityAddressEntry = _MySecurityAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1, 1)
)
mySecurityAddressEntry.setIndexNames(
    (0, "MY-SECURITY-MIB", "mySecurityAddressFdbId"),
    (0, "MY-SECURITY-MIB", "mySecurityAddressAddress"),
    (0, "MY-SECURITY-MIB", "mySecurityAddressPort"),
    (0, "MY-SECURITY-MIB", "mySecurityAddressIpAddr"),
)
if mibBuilder.loadTexts:
    mySecurityAddressEntry.setStatus("current")
_MySecurityAddressFdbId_Type = Unsigned32
_MySecurityAddressFdbId_Object = MibTableColumn
mySecurityAddressFdbId = _MySecurityAddressFdbId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1, 1, 1),
    _MySecurityAddressFdbId_Type()
)
mySecurityAddressFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySecurityAddressFdbId.setStatus("current")
_MySecurityAddressAddress_Type = MacAddress
_MySecurityAddressAddress_Object = MibTableColumn
mySecurityAddressAddress = _MySecurityAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1, 1, 2),
    _MySecurityAddressAddress_Type()
)
mySecurityAddressAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySecurityAddressAddress.setStatus("current")
_MySecurityAddressPort_Type = IfIndex
_MySecurityAddressPort_Object = MibTableColumn
mySecurityAddressPort = _MySecurityAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1, 1, 3),
    _MySecurityAddressPort_Type()
)
mySecurityAddressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySecurityAddressPort.setStatus("current")
_MySecurityAddressIpAddr_Type = IpAddress
_MySecurityAddressIpAddr_Object = MibTableColumn
mySecurityAddressIpAddr = _MySecurityAddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1, 1, 4),
    _MySecurityAddressIpAddr_Type()
)
mySecurityAddressIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySecurityAddressIpAddr.setStatus("current")
_MySecurityAddressIfBindIp_Type = TruthValue
_MySecurityAddressIfBindIp_Object = MibTableColumn
mySecurityAddressIfBindIp = _MySecurityAddressIfBindIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1, 1, 5),
    _MySecurityAddressIfBindIp_Type()
)
mySecurityAddressIfBindIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySecurityAddressIfBindIp.setStatus("current")
_MySecurityAddressRemainAge_Type = Integer32
_MySecurityAddressRemainAge_Object = MibTableColumn
mySecurityAddressRemainAge = _MySecurityAddressRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1, 1, 6),
    _MySecurityAddressRemainAge_Type()
)
mySecurityAddressRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySecurityAddressRemainAge.setStatus("current")


class _MySecurityAddressType_Type(Integer32):
    """Custom type mySecurityAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicLearn", 2),
          ("secureConfigured", 1))
    )


_MySecurityAddressType_Type.__name__ = "Integer32"
_MySecurityAddressType_Object = MibTableColumn
mySecurityAddressType = _MySecurityAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1, 1, 7),
    _MySecurityAddressType_Type()
)
mySecurityAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySecurityAddressType.setStatus("current")
_MySecurityAddressStatus_Type = RowStatus
_MySecurityAddressStatus_Object = MibTableColumn
mySecurityAddressStatus = _MySecurityAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 1, 1, 8),
    _MySecurityAddressStatus_Type()
)
mySecurityAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mySecurityAddressStatus.setStatus("current")
_MyBindAddressTable_Object = MibTable
myBindAddressTable = _MyBindAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    myBindAddressTable.setStatus("current")
_MyBindAddressEntry_Object = MibTableRow
myBindAddressEntry = _MyBindAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 2, 1)
)
myBindAddressEntry.setIndexNames(
    (0, "MY-SECURITY-MIB", "myBindAddressIpAddr"),
)
if mibBuilder.loadTexts:
    myBindAddressEntry.setStatus("current")
_MyBindAddressIpAddr_Type = IpAddress
_MyBindAddressIpAddr_Object = MibTableColumn
myBindAddressIpAddr = _MyBindAddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 2, 1, 1),
    _MyBindAddressIpAddr_Type()
)
myBindAddressIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myBindAddressIpAddr.setStatus("current")
_MyBindMacAddress_Type = MacAddress
_MyBindMacAddress_Object = MibTableColumn
myBindMacAddress = _MyBindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 2, 1, 2),
    _MyBindMacAddress_Type()
)
myBindMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myBindMacAddress.setStatus("current")
_MyBindAddressStatus_Type = ConfigStatus
_MyBindAddressStatus_Object = MibTableColumn
myBindAddressStatus = _MyBindAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 2, 2, 1, 3),
    _MyBindAddressStatus_Type()
)
myBindAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myBindAddressStatus.setStatus("current")
_MyPortSecrrityObjects_ObjectIdentity = ObjectIdentity
myPortSecrrityObjects = _MyPortSecrrityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3)
)
_MyPortSecurityTable_Object = MibTable
myPortSecurityTable = _MyPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    myPortSecurityTable.setStatus("current")
_MyPortSecurityEntry_Object = MibTableRow
myPortSecurityEntry = _MyPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1)
)
myPortSecurityEntry.setIndexNames(
    (0, "MY-SECURITY-MIB", "myPortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    myPortSecurityEntry.setStatus("current")
_MyPortSecurityPortIndex_Type = IfIndex
_MyPortSecurityPortIndex_Object = MibTableColumn
myPortSecurityPortIndex = _MyPortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1, 1),
    _MyPortSecurityPortIndex_Type()
)
myPortSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPortSecurityPortIndex.setStatus("current")


class _MyPortSecurityStatus_Type(EnabledStatus):
    """Custom type myPortSecurityStatus based on EnabledStatus"""


_MyPortSecurityStatus_Object = MibTableColumn
myPortSecurityStatus = _MyPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1, 2),
    _MyPortSecurityStatus_Type()
)
myPortSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPortSecurityStatus.setStatus("current")


class _MyPortSecurViolationType_Type(Integer32):
    """Custom type myPortSecurViolationType based on Integer32"""
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
        *(("violation-protect", 1),
          ("violation-restrict", 2),
          ("violation-shutdown", 3))
    )


_MyPortSecurViolationType_Type.__name__ = "Integer32"
_MyPortSecurViolationType_Object = MibTableColumn
myPortSecurViolationType = _MyPortSecurViolationType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1, 3),
    _MyPortSecurViolationType_Type()
)
myPortSecurViolationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPortSecurViolationType.setStatus("current")
_MyPortSecurityAddrNum_Type = Integer32
_MyPortSecurityAddrNum_Object = MibTableColumn
myPortSecurityAddrNum = _MyPortSecurityAddrNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1, 4),
    _MyPortSecurityAddrNum_Type()
)
myPortSecurityAddrNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPortSecurityAddrNum.setStatus("current")
_MyPortSecurityAddrAge_Type = Integer32
_MyPortSecurityAddrAge_Object = MibTableColumn
myPortSecurityAddrAge = _MyPortSecurityAddrAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1, 5),
    _MyPortSecurityAddrAge_Type()
)
myPortSecurityAddrAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPortSecurityAddrAge.setStatus("current")
_MyPortStaticSecurAddrIfAge_Type = EnabledStatus
_MyPortStaticSecurAddrIfAge_Object = MibTableColumn
myPortStaticSecurAddrIfAge = _MyPortStaticSecurAddrIfAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1, 6),
    _MyPortStaticSecurAddrIfAge_Type()
)
myPortStaticSecurAddrIfAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPortStaticSecurAddrIfAge.setStatus("current")
_MyPortSecurityAddressCurrentNum_Type = Integer32
_MyPortSecurityAddressCurrentNum_Object = MibTableColumn
myPortSecurityAddressCurrentNum = _MyPortSecurityAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1, 7),
    _MyPortSecurityAddressCurrentNum_Type()
)
myPortSecurityAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPortSecurityAddressCurrentNum.setStatus("current")
_MyPortStaticSecurAddrCurrentNum_Type = Integer32
_MyPortStaticSecurAddrCurrentNum_Object = MibTableColumn
myPortStaticSecurAddrCurrentNum = _MyPortStaticSecurAddrCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1, 8),
    _MyPortStaticSecurAddrCurrentNum_Type()
)
myPortStaticSecurAddrCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPortStaticSecurAddrCurrentNum.setStatus("current")


class _MyPortSecurityIpDistrMode_Type(Integer32):
    """Custom type myPortSecurityIpDistrMode based on Integer32"""
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
        *(("dynamic", 2),
          ("static", 1),
          ("staticAndDynamic", 3),
          ("unSpecified", 4))
    )


_MyPortSecurityIpDistrMode_Type.__name__ = "Integer32"
_MyPortSecurityIpDistrMode_Object = MibTableColumn
myPortSecurityIpDistrMode = _MyPortSecurityIpDistrMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 1, 3, 1, 1, 9),
    _MyPortSecurityIpDistrMode_Type()
)
myPortSecurityIpDistrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPortSecurityIpDistrMode.setStatus("current")
_MySecurityTraps_ObjectIdentity = ObjectIdentity
mySecurityTraps = _MySecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 2)
)
_MySecurityMIBConformance_ObjectIdentity = ObjectIdentity
mySecurityMIBConformance = _MySecurityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 3)
)
_MySecurityMIBCompliances_ObjectIdentity = ObjectIdentity
mySecurityMIBCompliances = _MySecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 3, 1)
)
_MySecurityMIBGroups_ObjectIdentity = ObjectIdentity
mySecurityMIBGroups = _MySecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 3, 2)
)

# Managed Objects groups

myUserManageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 3, 2, 1)
)
myUserManageMIBGroup.setObjects(
      *(("MY-SECURITY-MIB", "myEnableSnmpAgent"),
        ("MY-SECURITY-MIB", "myEnableWeb"),
        ("MY-SECURITY-MIB", "myEnableTelnet"))
)
if mibBuilder.loadTexts:
    myUserManageMIBGroup.setStatus("current")

mySecurityAddressMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 3, 2, 2)
)
mySecurityAddressMIBGroup.setObjects(
      *(("MY-SECURITY-MIB", "mySecurityAddressIfBindIp"),
        ("MY-SECURITY-MIB", "mySecurityAddressRemainAge"),
        ("MY-SECURITY-MIB", "mySecurityAddressType"),
        ("MY-SECURITY-MIB", "mySecurityAddressStatus"),
        ("MY-SECURITY-MIB", "myBindMacAddress"),
        ("MY-SECURITY-MIB", "myBindAddressStatus"))
)
if mibBuilder.loadTexts:
    mySecurityAddressMIBGroup.setStatus("current")

myPortSecurityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 3, 2, 3)
)
myPortSecurityMIBGroup.setObjects(
      *(("MY-SECURITY-MIB", "myPortSecurityPortIndex"),
        ("MY-SECURITY-MIB", "myPortSecurityStatus"),
        ("MY-SECURITY-MIB", "myPortSecurViolationType"),
        ("MY-SECURITY-MIB", "myPortSecurityAddrNum"),
        ("MY-SECURITY-MIB", "myPortSecurityAddrAge"),
        ("MY-SECURITY-MIB", "myPortStaticSecurAddrIfAge"),
        ("MY-SECURITY-MIB", "myPortSecurityAddressCurrentNum"),
        ("MY-SECURITY-MIB", "myPortStaticSecurAddrCurrentNum"),
        ("MY-SECURITY-MIB", "myPortSecurityIpDistrMode"))
)
if mibBuilder.loadTexts:
    myPortSecurityMIBGroup.setStatus("current")


# Notification objects

portSecurityViolate = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 2, 1)
)
portSecurityViolate.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portSecurityViolate.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

mySecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mySecurityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-SECURITY-MIB",
    **{"mySecurityMIB": mySecurityMIB,
       "mySecurityMIBObjects": mySecurityMIBObjects,
       "myUserManagementObjects": myUserManagementObjects,
       "myEnableSnmpAgent": myEnableSnmpAgent,
       "myEnableWeb": myEnableWeb,
       "myEnableTelnet": myEnableTelnet,
       "myTelnetHostIpTable": myTelnetHostIpTable,
       "myTelnetHostIpEntry": myTelnetHostIpEntry,
       "myTelnetHostIpAddress": myTelnetHostIpAddress,
       "myTelnetHostIpEnable": myTelnetHostIpEnable,
       "myWebHostIpTable": myWebHostIpTable,
       "myWebHostIpEntry": myWebHostIpEntry,
       "myWebHostIpAddress": myWebHostIpAddress,
       "myWebHostIpEnable": myWebHostIpEnable,
       "mySecurityAddressObjects": mySecurityAddressObjects,
       "mySecurityAddressTable": mySecurityAddressTable,
       "mySecurityAddressEntry": mySecurityAddressEntry,
       "mySecurityAddressFdbId": mySecurityAddressFdbId,
       "mySecurityAddressAddress": mySecurityAddressAddress,
       "mySecurityAddressPort": mySecurityAddressPort,
       "mySecurityAddressIpAddr": mySecurityAddressIpAddr,
       "mySecurityAddressIfBindIp": mySecurityAddressIfBindIp,
       "mySecurityAddressRemainAge": mySecurityAddressRemainAge,
       "mySecurityAddressType": mySecurityAddressType,
       "mySecurityAddressStatus": mySecurityAddressStatus,
       "myBindAddressTable": myBindAddressTable,
       "myBindAddressEntry": myBindAddressEntry,
       "myBindAddressIpAddr": myBindAddressIpAddr,
       "myBindMacAddress": myBindMacAddress,
       "myBindAddressStatus": myBindAddressStatus,
       "myPortSecrrityObjects": myPortSecrrityObjects,
       "myPortSecurityTable": myPortSecurityTable,
       "myPortSecurityEntry": myPortSecurityEntry,
       "myPortSecurityPortIndex": myPortSecurityPortIndex,
       "myPortSecurityStatus": myPortSecurityStatus,
       "myPortSecurViolationType": myPortSecurViolationType,
       "myPortSecurityAddrNum": myPortSecurityAddrNum,
       "myPortSecurityAddrAge": myPortSecurityAddrAge,
       "myPortStaticSecurAddrIfAge": myPortStaticSecurAddrIfAge,
       "myPortSecurityAddressCurrentNum": myPortSecurityAddressCurrentNum,
       "myPortStaticSecurAddrCurrentNum": myPortStaticSecurAddrCurrentNum,
       "myPortSecurityIpDistrMode": myPortSecurityIpDistrMode,
       "mySecurityTraps": mySecurityTraps,
       "portSecurityViolate": portSecurityViolate,
       "mySecurityMIBConformance": mySecurityMIBConformance,
       "mySecurityMIBCompliances": mySecurityMIBCompliances,
       "mySecurityMIBCompliance": mySecurityMIBCompliance,
       "mySecurityMIBGroups": mySecurityMIBGroups,
       "myUserManageMIBGroup": myUserManageMIBGroup,
       "mySecurityAddressMIBGroup": mySecurityAddressMIBGroup,
       "myPortSecurityMIBGroup": myPortSecurityMIBGroup}
)
