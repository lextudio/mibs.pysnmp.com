# SNMP MIB module (ZHONE-COM-IP-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-DHCP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:12 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(cardMfgSerialNumber,
 cardPostResults) = mibBuilder.importSymbols(
    "ZHONE-CARD-RESOURCES-MIB",
    "cardMfgSerialNumber",
    "cardPostResults")

(ZhoneRDIndex,
 rdEntry) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-RD-MIB",
    "ZhoneRDIndex",
    "rdEntry")

(ipIfAddr,
 ipIfLgId,
 ipIfVci,
 ipIfVpi) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-REC-MIB",
    "ipIfAddr",
    "ipIfLgId",
    "ipIfVci",
    "ipIfVpi")

(pportNumber,
 subPortNumber,
 zhoneShelfNumber,
 zhoneSlotNumber) = mibBuilder.importSymbols(
    "ZHONE-INTERFACE-TRANSLATION-MIB",
    "pportNumber",
    "subPortNumber",
    "zhoneShelfNumber",
    "zhoneSlotNumber")

(zhoneSysCardSwSpecificVers,) = mibBuilder.importSymbols(
    "ZHONE-SYSTEM-MIB",
    "zhoneSysCardSwSpecificVers")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")

(ZhoneAdminString,
 ZhoneFileName,
 ZhoneRowStatus,
 ZhoneShelfValue,
 ZhoneSlotValue) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneFileName",
    "ZhoneRowStatus",
    "ZhoneShelfValue",
    "ZhoneSlotValue")


# MODULE-IDENTITY

comIpDhcpServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 61)
)
comIpDhcpServer.setRevisions(
        ("2003-09-10 10:47",
         "2003-04-18 10:10",
         "2000-12-03 14:00",
         "2000-11-28 15:00",
         "2000-12-05 12:11",
         "2000-10-02 12:05",
         "2000-09-15 16:50",
         "2000-09-11 15:41")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11)
)
if mibBuilder.loadTexts:
    dhcpServer.setStatus("current")
_DhcpServerTraps_ObjectIdentity = ObjectIdentity
dhcpServerTraps = _DhcpServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 0)
)
if mibBuilder.loadTexts:
    dhcpServerTraps.setStatus("current")
_DhcpTrapZhoneCpeSysObjectID_Type = ObjectIdentifier
_DhcpTrapZhoneCpeSysObjectID_Object = MibScalar
dhcpTrapZhoneCpeSysObjectID = _DhcpTrapZhoneCpeSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 0, 2),
    _DhcpTrapZhoneCpeSysObjectID_Type()
)
dhcpTrapZhoneCpeSysObjectID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dhcpTrapZhoneCpeSysObjectID.setStatus("current")
_DhcpTrapZhoneIpInterfaceIndex_Type = InterfaceIndex
_DhcpTrapZhoneIpInterfaceIndex_Object = MibScalar
dhcpTrapZhoneIpInterfaceIndex = _DhcpTrapZhoneIpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 0, 4),
    _DhcpTrapZhoneIpInterfaceIndex_Type()
)
dhcpTrapZhoneIpInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dhcpTrapZhoneIpInterfaceIndex.setStatus("current")


class _DhcpServerDefaultLeaseTime_Type(Integer32):
    """Custom type dhcpServerDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpServerDefaultLeaseTime_Type.__name__ = "Integer32"
_DhcpServerDefaultLeaseTime_Object = MibScalar
dhcpServerDefaultLeaseTime = _DhcpServerDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 1),
    _DhcpServerDefaultLeaseTime_Type()
)
dhcpServerDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDefaultLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpServerDefaultLeaseTime.setUnits("seconds")


class _DhcpServerDefaultMinLeaseTime_Type(Integer32):
    """Custom type dhcpServerDefaultMinLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpServerDefaultMinLeaseTime_Type.__name__ = "Integer32"
_DhcpServerDefaultMinLeaseTime_Object = MibScalar
dhcpServerDefaultMinLeaseTime = _DhcpServerDefaultMinLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 2),
    _DhcpServerDefaultMinLeaseTime_Type()
)
dhcpServerDefaultMinLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDefaultMinLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpServerDefaultMinLeaseTime.setUnits("seconds")


class _DhcpServerDefaultMaxLeaseTime_Type(Integer32):
    """Custom type dhcpServerDefaultMaxLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpServerDefaultMaxLeaseTime_Type.__name__ = "Integer32"
_DhcpServerDefaultMaxLeaseTime_Object = MibScalar
dhcpServerDefaultMaxLeaseTime = _DhcpServerDefaultMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 3),
    _DhcpServerDefaultMaxLeaseTime_Type()
)
dhcpServerDefaultMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDefaultMaxLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpServerDefaultMaxLeaseTime.setUnits("seconds")


class _DhcpServerDefaultReserveStart_Type(Integer32):
    """Custom type dhcpServerDefaultReserveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpServerDefaultReserveStart_Type.__name__ = "Integer32"
_DhcpServerDefaultReserveStart_Object = MibScalar
dhcpServerDefaultReserveStart = _DhcpServerDefaultReserveStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 4),
    _DhcpServerDefaultReserveStart_Type()
)
dhcpServerDefaultReserveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDefaultReserveStart.setStatus("current")


class _DhcpServerDefaultReserveEnd_Type(Integer32):
    """Custom type dhcpServerDefaultReserveEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpServerDefaultReserveEnd_Type.__name__ = "Integer32"
_DhcpServerDefaultReserveEnd_Object = MibScalar
dhcpServerDefaultReserveEnd = _DhcpServerDefaultReserveEnd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 5),
    _DhcpServerDefaultReserveEnd_Type()
)
dhcpServerDefaultReserveEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDefaultReserveEnd.setStatus("current")
_DhcpServerLeaseTable_Object = MibTable
dhcpServerLeaseTable = _DhcpServerLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6)
)
if mibBuilder.loadTexts:
    dhcpServerLeaseTable.setStatus("current")
_DhcpServerLeaseEntry_Object = MibTableRow
dhcpServerLeaseEntry = _DhcpServerLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1)
)
dhcpServerLeaseEntry.setIndexNames(
    (0, "ZHONE-COM-IP-DHCP-SERVER-MIB", "dhcpLeaseDomain"),
    (0, "ZHONE-COM-IP-DHCP-SERVER-MIB", "dhcpLeaseIpAddress"),
)
if mibBuilder.loadTexts:
    dhcpServerLeaseEntry.setStatus("current")
_DhcpLeaseDomain_Type = ZhoneRDIndex
_DhcpLeaseDomain_Object = MibTableColumn
dhcpLeaseDomain = _DhcpLeaseDomain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 1),
    _DhcpLeaseDomain_Type()
)
dhcpLeaseDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpLeaseDomain.setStatus("current")
_DhcpLeaseIpAddress_Type = IpAddress
_DhcpLeaseIpAddress_Object = MibTableColumn
dhcpLeaseIpAddress = _DhcpLeaseIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 2),
    _DhcpLeaseIpAddress_Type()
)
dhcpLeaseIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpLeaseIpAddress.setStatus("current")
_DhcpLeaseStarts_Type = Unsigned32
_DhcpLeaseStarts_Object = MibTableColumn
dhcpLeaseStarts = _DhcpLeaseStarts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 3),
    _DhcpLeaseStarts_Type()
)
dhcpLeaseStarts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseStarts.setStatus("current")
_DhcpLeaseEnds_Type = Unsigned32
_DhcpLeaseEnds_Object = MibTableColumn
dhcpLeaseEnds = _DhcpLeaseEnds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 4),
    _DhcpLeaseEnds_Type()
)
dhcpLeaseEnds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseEnds.setStatus("current")


class _DhcpLeaseHardwareAddress_Type(PhysAddress):
    """Custom type dhcpLeaseHardwareAddress based on PhysAddress"""
    defaultHexValue = "0000"

    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DhcpLeaseHardwareAddress_Type.__name__ = "PhysAddress"
_DhcpLeaseHardwareAddress_Object = MibTableColumn
dhcpLeaseHardwareAddress = _DhcpLeaseHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 5),
    _DhcpLeaseHardwareAddress_Type()
)
dhcpLeaseHardwareAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseHardwareAddress.setStatus("current")


class _DhcpLeaseFlags_Type(Bits):
    """Custom type dhcpLeaseFlags based on Bits"""
    namedValues = NamedValues(
        *(("abandoned", 4),
          ("bootp", 1),
          ("static", 0),
          ("unused2", 2),
          ("unused3", 3),
          ("zhoneCPE", 5))
    )

_DhcpLeaseFlags_Type.__name__ = "Bits"
_DhcpLeaseFlags_Object = MibTableColumn
dhcpLeaseFlags = _DhcpLeaseFlags_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 6),
    _DhcpLeaseFlags_Type()
)
dhcpLeaseFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseFlags.setStatus("current")


class _DhcpLeaseClientId_Type(OctetString):
    """Custom type dhcpLeaseClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpLeaseClientId_Type.__name__ = "OctetString"
_DhcpLeaseClientId_Object = MibTableColumn
dhcpLeaseClientId = _DhcpLeaseClientId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 7),
    _DhcpLeaseClientId_Type()
)
dhcpLeaseClientId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseClientId.setStatus("current")


class _DhcpLeaseClientHostname_Type(SnmpAdminString):
    """Custom type dhcpLeaseClientHostname based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpLeaseClientHostname_Type.__name__ = "SnmpAdminString"
_DhcpLeaseClientHostname_Object = MibTableColumn
dhcpLeaseClientHostname = _DhcpLeaseClientHostname_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 8),
    _DhcpLeaseClientHostname_Type()
)
dhcpLeaseClientHostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseClientHostname.setStatus("current")


class _DhcpLeaseHostname_Type(SnmpAdminString):
    """Custom type dhcpLeaseHostname based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpLeaseHostname_Type.__name__ = "SnmpAdminString"
_DhcpLeaseHostname_Object = MibTableColumn
dhcpLeaseHostname = _DhcpLeaseHostname_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 9),
    _DhcpLeaseHostname_Type()
)
dhcpLeaseHostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseHostname.setStatus("current")


class _DhcpLeaseDDNSFwdName_Type(SnmpAdminString):
    """Custom type dhcpLeaseDDNSFwdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpLeaseDDNSFwdName_Type.__name__ = "SnmpAdminString"
_DhcpLeaseDDNSFwdName_Object = MibTableColumn
dhcpLeaseDDNSFwdName = _DhcpLeaseDDNSFwdName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 10),
    _DhcpLeaseDDNSFwdName_Type()
)
dhcpLeaseDDNSFwdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseDDNSFwdName.setStatus("current")


class _DhcpLeaseDDNSRevName_Type(SnmpAdminString):
    """Custom type dhcpLeaseDDNSRevName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpLeaseDDNSRevName_Type.__name__ = "SnmpAdminString"
_DhcpLeaseDDNSRevName_Object = MibTableColumn
dhcpLeaseDDNSRevName = _DhcpLeaseDDNSRevName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 11),
    _DhcpLeaseDDNSRevName_Type()
)
dhcpLeaseDDNSRevName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseDDNSRevName.setStatus("current")
_DhcpLeaseRowStatus_Type = ZhoneRowStatus
_DhcpLeaseRowStatus_Object = MibTableColumn
dhcpLeaseRowStatus = _DhcpLeaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 6, 1, 12),
    _DhcpLeaseRowStatus_Type()
)
dhcpLeaseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpLeaseRowStatus.setStatus("current")


class _DhcpServerNextGroupIndex_Type(Integer32):
    """Custom type dhcpServerNextGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpServerNextGroupIndex_Type.__name__ = "Integer32"
_DhcpServerNextGroupIndex_Object = MibScalar
dhcpServerNextGroupIndex = _DhcpServerNextGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 7),
    _DhcpServerNextGroupIndex_Type()
)
dhcpServerNextGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerNextGroupIndex.setStatus("current")
_DhcpServerGroupTable_Object = MibTable
dhcpServerGroupTable = _DhcpServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8)
)
if mibBuilder.loadTexts:
    dhcpServerGroupTable.setStatus("current")
_DhcpServerGroupEntry_Object = MibTableRow
dhcpServerGroupEntry = _DhcpServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1)
)
dhcpServerGroupEntry.setIndexNames(
    (0, "ZHONE-COM-IP-DHCP-SERVER-MIB", "dhcpGroupIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerGroupEntry.setStatus("current")


class _DhcpGroupIndex_Type(Integer32):
    """Custom type dhcpGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpGroupIndex_Type.__name__ = "Integer32"
_DhcpGroupIndex_Object = MibTableColumn
dhcpGroupIndex = _DhcpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 1),
    _DhcpGroupIndex_Type()
)
dhcpGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpGroupIndex.setStatus("current")
_DhcpGroupName_Type = ZhoneAdminString
_DhcpGroupName_Object = MibTableColumn
dhcpGroupName = _DhcpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 2),
    _DhcpGroupName_Type()
)
dhcpGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpGroupName.setStatus("current")
_DhcpGroupDomain_Type = ZhoneRDIndex
_DhcpGroupDomain_Object = MibTableColumn
dhcpGroupDomain = _DhcpGroupDomain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 3),
    _DhcpGroupDomain_Type()
)
dhcpGroupDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpGroupDomain.setStatus("current")


class _DhcpGroupVendorMatchString_Type(OctetString):
    """Custom type dhcpGroupVendorMatchString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpGroupVendorMatchString_Type.__name__ = "OctetString"
_DhcpGroupVendorMatchString_Object = MibTableColumn
dhcpGroupVendorMatchString = _DhcpGroupVendorMatchString_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 4),
    _DhcpGroupVendorMatchString_Type()
)
dhcpGroupVendorMatchString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpGroupVendorMatchString.setStatus("current")


class _DhcpGroupVendorMatchOffset_Type(Integer32):
    """Custom type dhcpGroupVendorMatchOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpGroupVendorMatchOffset_Type.__name__ = "Integer32"
_DhcpGroupVendorMatchOffset_Object = MibTableColumn
dhcpGroupVendorMatchOffset = _DhcpGroupVendorMatchOffset_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 5),
    _DhcpGroupVendorMatchOffset_Type()
)
dhcpGroupVendorMatchOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpGroupVendorMatchOffset.setStatus("current")


class _DhcpGroupVendorMatchLength_Type(Integer32):
    """Custom type dhcpGroupVendorMatchLength based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_DhcpGroupVendorMatchLength_Type.__name__ = "Integer32"
_DhcpGroupVendorMatchLength_Object = MibTableColumn
dhcpGroupVendorMatchLength = _DhcpGroupVendorMatchLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 6),
    _DhcpGroupVendorMatchLength_Type()
)
dhcpGroupVendorMatchLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpGroupVendorMatchLength.setStatus("current")


class _DhcpGroupClientMatchString_Type(OctetString):
    """Custom type dhcpGroupClientMatchString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpGroupClientMatchString_Type.__name__ = "OctetString"
_DhcpGroupClientMatchString_Object = MibTableColumn
dhcpGroupClientMatchString = _DhcpGroupClientMatchString_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 7),
    _DhcpGroupClientMatchString_Type()
)
dhcpGroupClientMatchString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpGroupClientMatchString.setStatus("current")


class _DhcpGroupClientMatchOffset_Type(Integer32):
    """Custom type dhcpGroupClientMatchOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpGroupClientMatchOffset_Type.__name__ = "Integer32"
_DhcpGroupClientMatchOffset_Object = MibTableColumn
dhcpGroupClientMatchOffset = _DhcpGroupClientMatchOffset_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 8),
    _DhcpGroupClientMatchOffset_Type()
)
dhcpGroupClientMatchOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpGroupClientMatchOffset.setStatus("current")


class _DhcpGroupClientMatchLength_Type(Integer32):
    """Custom type dhcpGroupClientMatchLength based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_DhcpGroupClientMatchLength_Type.__name__ = "Integer32"
_DhcpGroupClientMatchLength_Object = MibTableColumn
dhcpGroupClientMatchLength = _DhcpGroupClientMatchLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 9),
    _DhcpGroupClientMatchLength_Type()
)
dhcpGroupClientMatchLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpGroupClientMatchLength.setStatus("current")
_DhcpGroupRowStatus_Type = ZhoneRowStatus
_DhcpGroupRowStatus_Object = MibTableColumn
dhcpGroupRowStatus = _DhcpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 8, 1, 10),
    _DhcpGroupRowStatus_Type()
)
dhcpGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpGroupRowStatus.setStatus("current")
_DhcpServerGroupOptionTable_Object = MibTable
dhcpServerGroupOptionTable = _DhcpServerGroupOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9)
)
if mibBuilder.loadTexts:
    dhcpServerGroupOptionTable.setStatus("current")
_DhcpServerGroupOptionEntry_Object = MibTableRow
dhcpServerGroupOptionEntry = _DhcpServerGroupOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1)
)
if mibBuilder.loadTexts:
    dhcpServerGroupOptionEntry.setStatus("current")


class _DhcpGroupOptionDefaultLeaseTime_Type(Integer32):
    """Custom type dhcpGroupOptionDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpGroupOptionDefaultLeaseTime_Type.__name__ = "Integer32"
_DhcpGroupOptionDefaultLeaseTime_Object = MibTableColumn
dhcpGroupOptionDefaultLeaseTime = _DhcpGroupOptionDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1, 1),
    _DhcpGroupOptionDefaultLeaseTime_Type()
)
dhcpGroupOptionDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGroupOptionDefaultLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpGroupOptionDefaultLeaseTime.setUnits("seconds")


class _DhcpGroupOptionMinLeaseTime_Type(Integer32):
    """Custom type dhcpGroupOptionMinLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpGroupOptionMinLeaseTime_Type.__name__ = "Integer32"
_DhcpGroupOptionMinLeaseTime_Object = MibTableColumn
dhcpGroupOptionMinLeaseTime = _DhcpGroupOptionMinLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1, 2),
    _DhcpGroupOptionMinLeaseTime_Type()
)
dhcpGroupOptionMinLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGroupOptionMinLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpGroupOptionMinLeaseTime.setUnits("seconds")


class _DhcpGroupOptionMaxLeaseTime_Type(Integer32):
    """Custom type dhcpGroupOptionMaxLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpGroupOptionMaxLeaseTime_Type.__name__ = "Integer32"
_DhcpGroupOptionMaxLeaseTime_Object = MibTableColumn
dhcpGroupOptionMaxLeaseTime = _DhcpGroupOptionMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1, 3),
    _DhcpGroupOptionMaxLeaseTime_Type()
)
dhcpGroupOptionMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGroupOptionMaxLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpGroupOptionMaxLeaseTime.setUnits("seconds")
_DhcpGroupOptionBootFile_Type = ZhoneFileName
_DhcpGroupOptionBootFile_Object = MibTableColumn
dhcpGroupOptionBootFile = _DhcpGroupOptionBootFile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1, 4),
    _DhcpGroupOptionBootFile_Type()
)
dhcpGroupOptionBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGroupOptionBootFile.setStatus("current")
_DhcpGroupOptionBootServer_Type = IpAddress
_DhcpGroupOptionBootServer_Object = MibTableColumn
dhcpGroupOptionBootServer = _DhcpGroupOptionBootServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1, 5),
    _DhcpGroupOptionBootServer_Type()
)
dhcpGroupOptionBootServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGroupOptionBootServer.setStatus("current")
_DhcpGroupOptionDefaultRouter_Type = IpAddress
_DhcpGroupOptionDefaultRouter_Object = MibTableColumn
dhcpGroupOptionDefaultRouter = _DhcpGroupOptionDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1, 6),
    _DhcpGroupOptionDefaultRouter_Type()
)
dhcpGroupOptionDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGroupOptionDefaultRouter.setStatus("current")
_DhcpGroupOptionPrimaryNameServer_Type = IpAddress
_DhcpGroupOptionPrimaryNameServer_Object = MibTableColumn
dhcpGroupOptionPrimaryNameServer = _DhcpGroupOptionPrimaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1, 7),
    _DhcpGroupOptionPrimaryNameServer_Type()
)
dhcpGroupOptionPrimaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGroupOptionPrimaryNameServer.setStatus("current")
_DhcpGroupOptionSecondaryNameServer_Type = IpAddress
_DhcpGroupOptionSecondaryNameServer_Object = MibTableColumn
dhcpGroupOptionSecondaryNameServer = _DhcpGroupOptionSecondaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1, 8),
    _DhcpGroupOptionSecondaryNameServer_Type()
)
dhcpGroupOptionSecondaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGroupOptionSecondaryNameServer.setStatus("current")


class _DhcpGroupOptionDomainName_Type(SnmpAdminString):
    """Custom type dhcpGroupOptionDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpGroupOptionDomainName_Type.__name__ = "SnmpAdminString"
_DhcpGroupOptionDomainName_Object = MibTableColumn
dhcpGroupOptionDomainName = _DhcpGroupOptionDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 9, 1, 9),
    _DhcpGroupOptionDomainName_Type()
)
dhcpGroupOptionDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGroupOptionDomainName.setStatus("current")


class _DhcpServerNextSubnetIndex_Type(Integer32):
    """Custom type dhcpServerNextSubnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpServerNextSubnetIndex_Type.__name__ = "Integer32"
_DhcpServerNextSubnetIndex_Object = MibScalar
dhcpServerNextSubnetIndex = _DhcpServerNextSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 10),
    _DhcpServerNextSubnetIndex_Type()
)
dhcpServerNextSubnetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerNextSubnetIndex.setStatus("current")
_DhcpServerSubnetTable_Object = MibTable
dhcpServerSubnetTable = _DhcpServerSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11)
)
if mibBuilder.loadTexts:
    dhcpServerSubnetTable.setStatus("current")
_DhcpServerSubnetEntry_Object = MibTableRow
dhcpServerSubnetEntry = _DhcpServerSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1)
)
dhcpServerSubnetEntry.setIndexNames(
    (0, "ZHONE-COM-IP-DHCP-SERVER-MIB", "dhcpSubnetIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerSubnetEntry.setStatus("current")


class _DhcpSubnetIndex_Type(Integer32):
    """Custom type dhcpSubnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpSubnetIndex_Type.__name__ = "Integer32"
_DhcpSubnetIndex_Object = MibTableColumn
dhcpSubnetIndex = _DhcpSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 1),
    _DhcpSubnetIndex_Type()
)
dhcpSubnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSubnetIndex.setStatus("current")
_DhcpSubnetNetwork_Type = IpAddress
_DhcpSubnetNetwork_Object = MibTableColumn
dhcpSubnetNetwork = _DhcpSubnetNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 2),
    _DhcpSubnetNetwork_Type()
)
dhcpSubnetNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetNetwork.setStatus("current")
_DhcpSubnetNetmask_Type = IpAddress
_DhcpSubnetNetmask_Object = MibTableColumn
dhcpSubnetNetmask = _DhcpSubnetNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 3),
    _DhcpSubnetNetmask_Type()
)
dhcpSubnetNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetNetmask.setStatus("current")
_DhcpSubnetDomain_Type = ZhoneRDIndex
_DhcpSubnetDomain_Object = MibTableColumn
dhcpSubnetDomain = _DhcpSubnetDomain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 4),
    _DhcpSubnetDomain_Type()
)
dhcpSubnetDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetDomain.setStatus("current")
_DhcpSubnetRange1Start_Type = IpAddress
_DhcpSubnetRange1Start_Object = MibTableColumn
dhcpSubnetRange1Start = _DhcpSubnetRange1Start_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 5),
    _DhcpSubnetRange1Start_Type()
)
dhcpSubnetRange1Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRange1Start.setStatus("current")
_DhcpSubnetRange1End_Type = IpAddress
_DhcpSubnetRange1End_Object = MibTableColumn
dhcpSubnetRange1End = _DhcpSubnetRange1End_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 6),
    _DhcpSubnetRange1End_Type()
)
dhcpSubnetRange1End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRange1End.setStatus("current")


class _DhcpSubnetRange2Start_Type(IpAddress):
    """Custom type dhcpSubnetRange2Start based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpSubnetRange2Start_Object = MibTableColumn
dhcpSubnetRange2Start = _DhcpSubnetRange2Start_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 7),
    _DhcpSubnetRange2Start_Type()
)
dhcpSubnetRange2Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRange2Start.setStatus("current")


class _DhcpSubnetRange2End_Type(IpAddress):
    """Custom type dhcpSubnetRange2End based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpSubnetRange2End_Object = MibTableColumn
dhcpSubnetRange2End = _DhcpSubnetRange2End_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 8),
    _DhcpSubnetRange2End_Type()
)
dhcpSubnetRange2End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRange2End.setStatus("current")


class _DhcpSubnetRange3Start_Type(IpAddress):
    """Custom type dhcpSubnetRange3Start based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpSubnetRange3Start_Object = MibTableColumn
dhcpSubnetRange3Start = _DhcpSubnetRange3Start_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 9),
    _DhcpSubnetRange3Start_Type()
)
dhcpSubnetRange3Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRange3Start.setStatus("current")


class _DhcpSubnetRange3End_Type(IpAddress):
    """Custom type dhcpSubnetRange3End based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpSubnetRange3End_Object = MibTableColumn
dhcpSubnetRange3End = _DhcpSubnetRange3End_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 10),
    _DhcpSubnetRange3End_Type()
)
dhcpSubnetRange3End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRange3End.setStatus("current")


class _DhcpSubnetRange4Start_Type(IpAddress):
    """Custom type dhcpSubnetRange4Start based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpSubnetRange4Start_Object = MibTableColumn
dhcpSubnetRange4Start = _DhcpSubnetRange4Start_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 11),
    _DhcpSubnetRange4Start_Type()
)
dhcpSubnetRange4Start.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRange4Start.setStatus("current")


class _DhcpSubnetRange4End_Type(IpAddress):
    """Custom type dhcpSubnetRange4End based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpSubnetRange4End_Object = MibTableColumn
dhcpSubnetRange4End = _DhcpSubnetRange4End_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 12),
    _DhcpSubnetRange4End_Type()
)
dhcpSubnetRange4End.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRange4End.setStatus("current")
_DhcpSubnetRowStatus_Type = ZhoneRowStatus
_DhcpSubnetRowStatus_Object = MibTableColumn
dhcpSubnetRowStatus = _DhcpSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 13),
    _DhcpSubnetRowStatus_Type()
)
dhcpSubnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetRowStatus.setStatus("current")


class _DhcpSubnetGroup2_Type(Integer32):
    """Custom type dhcpSubnetGroup2 based on Integer32"""
    defaultBinValue = 0


_DhcpSubnetGroup2_Object = MibTableColumn
dhcpSubnetGroup2 = _DhcpSubnetGroup2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 14),
    _DhcpSubnetGroup2_Type()
)
dhcpSubnetGroup2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetGroup2.setStatus("current")


class _DhcpStickyAddr_Type(TruthValue):
    """Custom type dhcpStickyAddr based on TruthValue"""
    defaultValue = 1


_DhcpStickyAddr_Object = MibTableColumn
dhcpStickyAddr = _DhcpStickyAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 15),
    _DhcpStickyAddr_Type()
)
dhcpStickyAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpStickyAddr.setStatus("current")


class _DhcpSubnetExternalServer_Type(IpAddress):
    """Custom type dhcpSubnetExternalServer based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpSubnetExternalServer_Object = MibTableColumn
dhcpSubnetExternalServer = _DhcpSubnetExternalServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 16),
    _DhcpSubnetExternalServer_Type()
)
dhcpSubnetExternalServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetExternalServer.setStatus("current")


class _DhcpSubnetExternalServerAlt_Type(IpAddress):
    """Custom type dhcpSubnetExternalServerAlt based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpSubnetExternalServerAlt_Object = MibTableColumn
dhcpSubnetExternalServerAlt = _DhcpSubnetExternalServerAlt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 11, 1, 17),
    _DhcpSubnetExternalServerAlt_Type()
)
dhcpSubnetExternalServerAlt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSubnetExternalServerAlt.setStatus("current")
_DhcpServerSubnetOptionTable_Object = MibTable
dhcpServerSubnetOptionTable = _DhcpServerSubnetOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12)
)
if mibBuilder.loadTexts:
    dhcpServerSubnetOptionTable.setStatus("current")
_DhcpServerSubnetOptionEntry_Object = MibTableRow
dhcpServerSubnetOptionEntry = _DhcpServerSubnetOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1)
)
if mibBuilder.loadTexts:
    dhcpServerSubnetOptionEntry.setStatus("current")


class _DhcpSubnetOptionDefaultLeaseTime_Type(Integer32):
    """Custom type dhcpSubnetOptionDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpSubnetOptionDefaultLeaseTime_Type.__name__ = "Integer32"
_DhcpSubnetOptionDefaultLeaseTime_Object = MibTableColumn
dhcpSubnetOptionDefaultLeaseTime = _DhcpSubnetOptionDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1, 1),
    _DhcpSubnetOptionDefaultLeaseTime_Type()
)
dhcpSubnetOptionDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetOptionDefaultLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpSubnetOptionDefaultLeaseTime.setUnits("seconds")


class _DhcpSubnetOptionMinLeaseTime_Type(Integer32):
    """Custom type dhcpSubnetOptionMinLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpSubnetOptionMinLeaseTime_Type.__name__ = "Integer32"
_DhcpSubnetOptionMinLeaseTime_Object = MibTableColumn
dhcpSubnetOptionMinLeaseTime = _DhcpSubnetOptionMinLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1, 2),
    _DhcpSubnetOptionMinLeaseTime_Type()
)
dhcpSubnetOptionMinLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetOptionMinLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpSubnetOptionMinLeaseTime.setUnits("seconds")


class _DhcpSubnetOptionMaxLeaseTime_Type(Integer32):
    """Custom type dhcpSubnetOptionMaxLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpSubnetOptionMaxLeaseTime_Type.__name__ = "Integer32"
_DhcpSubnetOptionMaxLeaseTime_Object = MibTableColumn
dhcpSubnetOptionMaxLeaseTime = _DhcpSubnetOptionMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1, 3),
    _DhcpSubnetOptionMaxLeaseTime_Type()
)
dhcpSubnetOptionMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetOptionMaxLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpSubnetOptionMaxLeaseTime.setUnits("seconds")
_DhcpSubnetOptionBootFile_Type = ZhoneFileName
_DhcpSubnetOptionBootFile_Object = MibTableColumn
dhcpSubnetOptionBootFile = _DhcpSubnetOptionBootFile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1, 4),
    _DhcpSubnetOptionBootFile_Type()
)
dhcpSubnetOptionBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetOptionBootFile.setStatus("current")
_DhcpSubnetOptionBootServer_Type = IpAddress
_DhcpSubnetOptionBootServer_Object = MibTableColumn
dhcpSubnetOptionBootServer = _DhcpSubnetOptionBootServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1, 5),
    _DhcpSubnetOptionBootServer_Type()
)
dhcpSubnetOptionBootServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetOptionBootServer.setStatus("current")
_DhcpSubnetOptionDefaultRouter_Type = IpAddress
_DhcpSubnetOptionDefaultRouter_Object = MibTableColumn
dhcpSubnetOptionDefaultRouter = _DhcpSubnetOptionDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1, 6),
    _DhcpSubnetOptionDefaultRouter_Type()
)
dhcpSubnetOptionDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetOptionDefaultRouter.setStatus("current")
_DhcpSubnetOptionPrimaryNameServer_Type = IpAddress
_DhcpSubnetOptionPrimaryNameServer_Object = MibTableColumn
dhcpSubnetOptionPrimaryNameServer = _DhcpSubnetOptionPrimaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1, 7),
    _DhcpSubnetOptionPrimaryNameServer_Type()
)
dhcpSubnetOptionPrimaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetOptionPrimaryNameServer.setStatus("current")
_DhcpSubnetOptionSecondaryNameServer_Type = IpAddress
_DhcpSubnetOptionSecondaryNameServer_Object = MibTableColumn
dhcpSubnetOptionSecondaryNameServer = _DhcpSubnetOptionSecondaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1, 8),
    _DhcpSubnetOptionSecondaryNameServer_Type()
)
dhcpSubnetOptionSecondaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetOptionSecondaryNameServer.setStatus("current")


class _DhcpSubnetOptionDomainName_Type(SnmpAdminString):
    """Custom type dhcpSubnetOptionDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpSubnetOptionDomainName_Type.__name__ = "SnmpAdminString"
_DhcpSubnetOptionDomainName_Object = MibTableColumn
dhcpSubnetOptionDomainName = _DhcpSubnetOptionDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 12, 1, 9),
    _DhcpSubnetOptionDomainName_Type()
)
dhcpSubnetOptionDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetOptionDomainName.setStatus("current")


class _DhcpServerNextHostIndex_Type(Integer32):
    """Custom type dhcpServerNextHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpServerNextHostIndex_Type.__name__ = "Integer32"
_DhcpServerNextHostIndex_Object = MibScalar
dhcpServerNextHostIndex = _DhcpServerNextHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 13),
    _DhcpServerNextHostIndex_Type()
)
dhcpServerNextHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerNextHostIndex.setStatus("current")
_DhcpServerHostTable_Object = MibTable
dhcpServerHostTable = _DhcpServerHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14)
)
if mibBuilder.loadTexts:
    dhcpServerHostTable.setStatus("current")
_DhcpServerHostEntry_Object = MibTableRow
dhcpServerHostEntry = _DhcpServerHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1)
)
dhcpServerHostEntry.setIndexNames(
    (0, "ZHONE-COM-IP-DHCP-SERVER-MIB", "dhcpHostIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerHostEntry.setStatus("current")


class _DhcpHostIndex_Type(Integer32):
    """Custom type dhcpHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpHostIndex_Type.__name__ = "Integer32"
_DhcpHostIndex_Object = MibTableColumn
dhcpHostIndex = _DhcpHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 1),
    _DhcpHostIndex_Type()
)
dhcpHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpHostIndex.setStatus("current")
_DhcpHostHostname_Type = ZhoneAdminString
_DhcpHostHostname_Object = MibTableColumn
dhcpHostHostname = _DhcpHostHostname_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 2),
    _DhcpHostHostname_Type()
)
dhcpHostHostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpHostHostname.setStatus("current")
_DhcpHostDomain_Type = ZhoneRDIndex
_DhcpHostDomain_Object = MibTableColumn
dhcpHostDomain = _DhcpHostDomain_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 3),
    _DhcpHostDomain_Type()
)
dhcpHostDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpHostDomain.setStatus("current")


class _DhcpHostHardwareAddress_Type(PhysAddress):
    """Custom type dhcpHostHardwareAddress based on PhysAddress"""
    defaultHexValue = "0000"

    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DhcpHostHardwareAddress_Type.__name__ = "PhysAddress"
_DhcpHostHardwareAddress_Object = MibTableColumn
dhcpHostHardwareAddress = _DhcpHostHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 4),
    _DhcpHostHardwareAddress_Type()
)
dhcpHostHardwareAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpHostHardwareAddress.setStatus("current")


class _DhcpHostClientId_Type(OctetString):
    """Custom type dhcpHostClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpHostClientId_Type.__name__ = "OctetString"
_DhcpHostClientId_Object = MibTableColumn
dhcpHostClientId = _DhcpHostClientId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 5),
    _DhcpHostClientId_Type()
)
dhcpHostClientId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpHostClientId.setStatus("current")


class _DhcpHostIpAddress1_Type(IpAddress):
    """Custom type dhcpHostIpAddress1 based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpHostIpAddress1_Object = MibTableColumn
dhcpHostIpAddress1 = _DhcpHostIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 6),
    _DhcpHostIpAddress1_Type()
)
dhcpHostIpAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpHostIpAddress1.setStatus("current")


class _DhcpHostIpAddress2_Type(IpAddress):
    """Custom type dhcpHostIpAddress2 based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpHostIpAddress2_Object = MibTableColumn
dhcpHostIpAddress2 = _DhcpHostIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 7),
    _DhcpHostIpAddress2_Type()
)
dhcpHostIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpHostIpAddress2.setStatus("current")


class _DhcpHostIpAddress3_Type(IpAddress):
    """Custom type dhcpHostIpAddress3 based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpHostIpAddress3_Object = MibTableColumn
dhcpHostIpAddress3 = _DhcpHostIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 8),
    _DhcpHostIpAddress3_Type()
)
dhcpHostIpAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpHostIpAddress3.setStatus("current")


class _DhcpHostIpAddress4_Type(IpAddress):
    """Custom type dhcpHostIpAddress4 based on IpAddress"""
    defaultHexValue = "00000000"


_DhcpHostIpAddress4_Object = MibTableColumn
dhcpHostIpAddress4 = _DhcpHostIpAddress4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 9),
    _DhcpHostIpAddress4_Type()
)
dhcpHostIpAddress4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpHostIpAddress4.setStatus("current")
_DhcpHostRowStatus_Type = ZhoneRowStatus
_DhcpHostRowStatus_Object = MibTableColumn
dhcpHostRowStatus = _DhcpHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 14, 1, 10),
    _DhcpHostRowStatus_Type()
)
dhcpHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpHostRowStatus.setStatus("current")
_DhcpServerHostOptionTable_Object = MibTable
dhcpServerHostOptionTable = _DhcpServerHostOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15)
)
if mibBuilder.loadTexts:
    dhcpServerHostOptionTable.setStatus("current")
_DhcpServerHostOptionEntry_Object = MibTableRow
dhcpServerHostOptionEntry = _DhcpServerHostOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1)
)
if mibBuilder.loadTexts:
    dhcpServerHostOptionEntry.setStatus("current")


class _DhcpHostOptionDefaultLeaseTime_Type(Integer32):
    """Custom type dhcpHostOptionDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpHostOptionDefaultLeaseTime_Type.__name__ = "Integer32"
_DhcpHostOptionDefaultLeaseTime_Object = MibTableColumn
dhcpHostOptionDefaultLeaseTime = _DhcpHostOptionDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1, 1),
    _DhcpHostOptionDefaultLeaseTime_Type()
)
dhcpHostOptionDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpHostOptionDefaultLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpHostOptionDefaultLeaseTime.setUnits("seconds")


class _DhcpHostOptionMinLeaseTime_Type(Integer32):
    """Custom type dhcpHostOptionMinLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpHostOptionMinLeaseTime_Type.__name__ = "Integer32"
_DhcpHostOptionMinLeaseTime_Object = MibTableColumn
dhcpHostOptionMinLeaseTime = _DhcpHostOptionMinLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1, 2),
    _DhcpHostOptionMinLeaseTime_Type()
)
dhcpHostOptionMinLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpHostOptionMinLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpHostOptionMinLeaseTime.setUnits("seconds")


class _DhcpHostOptionMaxLeaseTime_Type(Integer32):
    """Custom type dhcpHostOptionMaxLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpHostOptionMaxLeaseTime_Type.__name__ = "Integer32"
_DhcpHostOptionMaxLeaseTime_Object = MibTableColumn
dhcpHostOptionMaxLeaseTime = _DhcpHostOptionMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1, 3),
    _DhcpHostOptionMaxLeaseTime_Type()
)
dhcpHostOptionMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpHostOptionMaxLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    dhcpHostOptionMaxLeaseTime.setUnits("seconds")
_DhcpHostOptionBootFile_Type = ZhoneFileName
_DhcpHostOptionBootFile_Object = MibTableColumn
dhcpHostOptionBootFile = _DhcpHostOptionBootFile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1, 4),
    _DhcpHostOptionBootFile_Type()
)
dhcpHostOptionBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpHostOptionBootFile.setStatus("current")
_DhcpHostOptionBootServer_Type = IpAddress
_DhcpHostOptionBootServer_Object = MibTableColumn
dhcpHostOptionBootServer = _DhcpHostOptionBootServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1, 5),
    _DhcpHostOptionBootServer_Type()
)
dhcpHostOptionBootServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpHostOptionBootServer.setStatus("current")
_DhcpHostOptionDefaultRouter_Type = IpAddress
_DhcpHostOptionDefaultRouter_Object = MibTableColumn
dhcpHostOptionDefaultRouter = _DhcpHostOptionDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1, 6),
    _DhcpHostOptionDefaultRouter_Type()
)
dhcpHostOptionDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpHostOptionDefaultRouter.setStatus("current")
_DhcpHostOptionPrimaryNameServer_Type = IpAddress
_DhcpHostOptionPrimaryNameServer_Object = MibTableColumn
dhcpHostOptionPrimaryNameServer = _DhcpHostOptionPrimaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1, 7),
    _DhcpHostOptionPrimaryNameServer_Type()
)
dhcpHostOptionPrimaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpHostOptionPrimaryNameServer.setStatus("current")
_DhcpHostOptionSecondaryNameServer_Type = IpAddress
_DhcpHostOptionSecondaryNameServer_Object = MibTableColumn
dhcpHostOptionSecondaryNameServer = _DhcpHostOptionSecondaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1, 8),
    _DhcpHostOptionSecondaryNameServer_Type()
)
dhcpHostOptionSecondaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpHostOptionSecondaryNameServer.setStatus("current")


class _DhcpHostOptionDomainName_Type(SnmpAdminString):
    """Custom type dhcpHostOptionDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DhcpHostOptionDomainName_Type.__name__ = "SnmpAdminString"
_DhcpHostOptionDomainName_Object = MibTableColumn
dhcpHostOptionDomainName = _DhcpHostOptionDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 15, 1, 9),
    _DhcpHostOptionDomainName_Type()
)
dhcpHostOptionDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpHostOptionDomainName.setStatus("current")
_DhcpServerStatistics_ObjectIdentity = ObjectIdentity
dhcpServerStatistics = _DhcpServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16)
)
if mibBuilder.loadTexts:
    dhcpServerStatistics.setStatus("current")
_ServerSystem_ObjectIdentity = ObjectIdentity
serverSystem = _ServerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 1)
)
if mibBuilder.loadTexts:
    serverSystem.setStatus("current")
_ServerSystemDescr_Type = ZhoneAdminString
_ServerSystemDescr_Object = MibScalar
serverSystemDescr = _ServerSystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 1, 1),
    _ServerSystemDescr_Type()
)
serverSystemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSystemDescr.setStatus("current")
_ServerSystemObjectID_Type = ObjectIdentifier
_ServerSystemObjectID_Object = MibScalar
serverSystemObjectID = _ServerSystemObjectID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 1, 2),
    _ServerSystemObjectID_Type()
)
serverSystemObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSystemObjectID.setStatus("current")
_ServerUptime_Type = TimeTicks
_ServerUptime_Object = MibScalar
serverUptime = _ServerUptime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 1, 3),
    _ServerUptime_Type()
)
serverUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverUptime.setStatus("current")
_ServerActiveShelf_Type = ZhoneShelfValue
_ServerActiveShelf_Object = MibScalar
serverActiveShelf = _ServerActiveShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 1, 4),
    _ServerActiveShelf_Type()
)
serverActiveShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverActiveShelf.setStatus("current")
_ServerActiveSlot_Type = ZhoneSlotValue
_ServerActiveSlot_Object = MibScalar
serverActiveSlot = _ServerActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 1, 5),
    _ServerActiveSlot_Type()
)
serverActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverActiveSlot.setStatus("current")
_ServerStandbyShelf_Type = ZhoneShelfValue
_ServerStandbyShelf_Object = MibScalar
serverStandbyShelf = _ServerStandbyShelf_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 1, 6),
    _ServerStandbyShelf_Type()
)
serverStandbyShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverStandbyShelf.setStatus("current")
_ServerStandbySlot_Type = ZhoneSlotValue
_ServerStandbySlot_Object = MibScalar
serverStandbySlot = _ServerStandbySlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 1, 7),
    _ServerStandbySlot_Type()
)
serverStandbySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverStandbySlot.setStatus("current")
_BootpCountersTable_Object = MibTable
bootpCountersTable = _BootpCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 2)
)
if mibBuilder.loadTexts:
    bootpCountersTable.setStatus("current")
_BootpCountersEntry_Object = MibTableRow
bootpCountersEntry = _BootpCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 2, 1)
)
if mibBuilder.loadTexts:
    bootpCountersEntry.setStatus("current")
_BootpCountRequests_Type = Counter32
_BootpCountRequests_Object = MibTableColumn
bootpCountRequests = _BootpCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 2, 1, 1),
    _BootpCountRequests_Type()
)
bootpCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpCountRequests.setStatus("current")
_BootpCountInvalids_Type = Counter32
_BootpCountInvalids_Object = MibTableColumn
bootpCountInvalids = _BootpCountInvalids_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 2, 1, 2),
    _BootpCountInvalids_Type()
)
bootpCountInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpCountInvalids.setStatus("current")
_BootpCountReplies_Type = Counter32
_BootpCountReplies_Object = MibTableColumn
bootpCountReplies = _BootpCountReplies_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 2, 1, 3),
    _BootpCountReplies_Type()
)
bootpCountReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpCountReplies.setStatus("current")
_BootpCountDroppedUnknownClients_Type = Counter32
_BootpCountDroppedUnknownClients_Object = MibTableColumn
bootpCountDroppedUnknownClients = _BootpCountDroppedUnknownClients_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 2, 1, 4),
    _BootpCountDroppedUnknownClients_Type()
)
bootpCountDroppedUnknownClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpCountDroppedUnknownClients.setStatus("current")
_BootpCountDroppedNotServingSubnet_Type = Counter32
_BootpCountDroppedNotServingSubnet_Object = MibTableColumn
bootpCountDroppedNotServingSubnet = _BootpCountDroppedNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 2, 1, 5),
    _BootpCountDroppedNotServingSubnet_Type()
)
bootpCountDroppedNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpCountDroppedNotServingSubnet.setStatus("current")
_DhcpCountersTable_Object = MibTable
dhcpCountersTable = _DhcpCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3)
)
if mibBuilder.loadTexts:
    dhcpCountersTable.setStatus("current")
_DhcpCountersEntry_Object = MibTableRow
dhcpCountersEntry = _DhcpCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpCountersEntry.setStatus("current")
_DhcpCountDiscovers_Type = Counter32
_DhcpCountDiscovers_Object = MibTableColumn
dhcpCountDiscovers = _DhcpCountDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 1),
    _DhcpCountDiscovers_Type()
)
dhcpCountDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountDiscovers.setStatus("current")
_DhcpCountRequests_Type = Counter32
_DhcpCountRequests_Object = MibTableColumn
dhcpCountRequests = _DhcpCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 2),
    _DhcpCountRequests_Type()
)
dhcpCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountRequests.setStatus("current")
_DhcpCountReleases_Type = Counter32
_DhcpCountReleases_Object = MibTableColumn
dhcpCountReleases = _DhcpCountReleases_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 3),
    _DhcpCountReleases_Type()
)
dhcpCountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountReleases.setStatus("current")
_DhcpCountDeclines_Type = Counter32
_DhcpCountDeclines_Object = MibTableColumn
dhcpCountDeclines = _DhcpCountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 4),
    _DhcpCountDeclines_Type()
)
dhcpCountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountDeclines.setStatus("current")
_DhcpCountInforms_Type = Counter32
_DhcpCountInforms_Object = MibTableColumn
dhcpCountInforms = _DhcpCountInforms_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 5),
    _DhcpCountInforms_Type()
)
dhcpCountInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountInforms.setStatus("current")
_DhcpCountInvalids_Type = Counter32
_DhcpCountInvalids_Object = MibTableColumn
dhcpCountInvalids = _DhcpCountInvalids_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 6),
    _DhcpCountInvalids_Type()
)
dhcpCountInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountInvalids.setStatus("current")
_DhcpCountOffers_Type = Counter32
_DhcpCountOffers_Object = MibTableColumn
dhcpCountOffers = _DhcpCountOffers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 7),
    _DhcpCountOffers_Type()
)
dhcpCountOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountOffers.setStatus("current")
_DhcpCountAcks_Type = Counter32
_DhcpCountAcks_Object = MibTableColumn
dhcpCountAcks = _DhcpCountAcks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 8),
    _DhcpCountAcks_Type()
)
dhcpCountAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountAcks.setStatus("current")
_DhcpCountNacks_Type = Counter32
_DhcpCountNacks_Object = MibTableColumn
dhcpCountNacks = _DhcpCountNacks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 9),
    _DhcpCountNacks_Type()
)
dhcpCountNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountNacks.setStatus("current")
_DhcpCountDroppedUnknownClient_Type = Counter32
_DhcpCountDroppedUnknownClient_Object = MibTableColumn
dhcpCountDroppedUnknownClient = _DhcpCountDroppedUnknownClient_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 10),
    _DhcpCountDroppedUnknownClient_Type()
)
dhcpCountDroppedUnknownClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountDroppedUnknownClient.setStatus("current")
_DhcpCountDroppedNotServingSubnet_Type = Counter32
_DhcpCountDroppedNotServingSubnet_Object = MibTableColumn
dhcpCountDroppedNotServingSubnet = _DhcpCountDroppedNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 16, 3, 1, 11),
    _DhcpCountDroppedNotServingSubnet_Type()
)
dhcpCountDroppedNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountDroppedNotServingSubnet.setStatus("current")
_DhcpServerConfigurationVersion_Type = Unsigned32
_DhcpServerConfigurationVersion_Object = MibScalar
dhcpServerConfigurationVersion = _DhcpServerConfigurationVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 17),
    _DhcpServerConfigurationVersion_Type()
)
dhcpServerConfigurationVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerConfigurationVersion.setStatus("deprecated")


class _DhcpServerRestart_Type(Integer32):
    """Custom type dhcpServerRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_DhcpServerRestart_Type.__name__ = "Integer32"
_DhcpServerRestart_Object = MibScalar
dhcpServerRestart = _DhcpServerRestart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 18),
    _DhcpServerRestart_Type()
)
dhcpServerRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerRestart.setStatus("current")
dhcpServerGroupEntry.registerAugmentions(
    ("ZHONE-COM-IP-DHCP-SERVER-MIB",
     "dhcpServerGroupOptionEntry")
)
dhcpServerGroupOptionEntry.setIndexNames(*dhcpServerGroupEntry.getIndexNames())
dhcpServerSubnetEntry.registerAugmentions(
    ("ZHONE-COM-IP-DHCP-SERVER-MIB",
     "dhcpServerSubnetOptionEntry")
)
dhcpServerSubnetOptionEntry.setIndexNames(*dhcpServerSubnetEntry.getIndexNames())
dhcpServerHostEntry.registerAugmentions(
    ("ZHONE-COM-IP-DHCP-SERVER-MIB",
     "dhcpServerHostOptionEntry")
)
dhcpServerHostOptionEntry.setIndexNames(*dhcpServerHostEntry.getIndexNames())
rdEntry.registerAugmentions(
    ("ZHONE-COM-IP-DHCP-SERVER-MIB",
     "bootpCountersEntry")
)
bootpCountersEntry.setIndexNames(*rdEntry.getIndexNames())
rdEntry.registerAugmentions(
    ("ZHONE-COM-IP-DHCP-SERVER-MIB",
     "dhcpCountersEntry")
)
dhcpCountersEntry.setIndexNames(*rdEntry.getIndexNames())

# Managed Objects groups


# Notification objects

dhcpTrapZhoneCpeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 0, 1)
)
dhcpTrapZhoneCpeDetected.setObjects(
      *(("ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneShelfNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "zhoneSlotNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "pportNumber"),
        ("ZHONE-INTERFACE-TRANSLATION-MIB", "subPortNumber"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfVpi"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfVci"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfLgId"),
        ("ZHONE-COM-IP-DHCP-SERVER-MIB", "dhcpTrapZhoneCpeSysObjectID"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardMfgSerialNumber"),
        ("ZHONE-CARD-RESOURCES-MIB", "cardPostResults"),
        ("ZHONE-SYSTEM-MIB", "zhoneSysCardSwSpecificVers"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfAddr"))
)
if mibBuilder.loadTexts:
    dhcpTrapZhoneCpeDetected.setStatus(
        "current"
    )

dhcpTrapZhoneIpAddressUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 11, 0, 3)
)
dhcpTrapZhoneIpAddressUpdate.setObjects(
      *(("ZHONE-COM-IP-DHCP-SERVER-MIB", "dhcpTrapZhoneIpInterfaceIndex"),
        ("ZHONE-COM-IP-REC-MIB", "ipIfAddr"))
)
if mibBuilder.loadTexts:
    dhcpTrapZhoneIpAddressUpdate.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-DHCP-SERVER-MIB",
    **{"dhcpServer": dhcpServer,
       "dhcpServerTraps": dhcpServerTraps,
       "dhcpTrapZhoneCpeDetected": dhcpTrapZhoneCpeDetected,
       "dhcpTrapZhoneCpeSysObjectID": dhcpTrapZhoneCpeSysObjectID,
       "dhcpTrapZhoneIpAddressUpdate": dhcpTrapZhoneIpAddressUpdate,
       "dhcpTrapZhoneIpInterfaceIndex": dhcpTrapZhoneIpInterfaceIndex,
       "dhcpServerDefaultLeaseTime": dhcpServerDefaultLeaseTime,
       "dhcpServerDefaultMinLeaseTime": dhcpServerDefaultMinLeaseTime,
       "dhcpServerDefaultMaxLeaseTime": dhcpServerDefaultMaxLeaseTime,
       "dhcpServerDefaultReserveStart": dhcpServerDefaultReserveStart,
       "dhcpServerDefaultReserveEnd": dhcpServerDefaultReserveEnd,
       "dhcpServerLeaseTable": dhcpServerLeaseTable,
       "dhcpServerLeaseEntry": dhcpServerLeaseEntry,
       "dhcpLeaseDomain": dhcpLeaseDomain,
       "dhcpLeaseIpAddress": dhcpLeaseIpAddress,
       "dhcpLeaseStarts": dhcpLeaseStarts,
       "dhcpLeaseEnds": dhcpLeaseEnds,
       "dhcpLeaseHardwareAddress": dhcpLeaseHardwareAddress,
       "dhcpLeaseFlags": dhcpLeaseFlags,
       "dhcpLeaseClientId": dhcpLeaseClientId,
       "dhcpLeaseClientHostname": dhcpLeaseClientHostname,
       "dhcpLeaseHostname": dhcpLeaseHostname,
       "dhcpLeaseDDNSFwdName": dhcpLeaseDDNSFwdName,
       "dhcpLeaseDDNSRevName": dhcpLeaseDDNSRevName,
       "dhcpLeaseRowStatus": dhcpLeaseRowStatus,
       "dhcpServerNextGroupIndex": dhcpServerNextGroupIndex,
       "dhcpServerGroupTable": dhcpServerGroupTable,
       "dhcpServerGroupEntry": dhcpServerGroupEntry,
       "dhcpGroupIndex": dhcpGroupIndex,
       "dhcpGroupName": dhcpGroupName,
       "dhcpGroupDomain": dhcpGroupDomain,
       "dhcpGroupVendorMatchString": dhcpGroupVendorMatchString,
       "dhcpGroupVendorMatchOffset": dhcpGroupVendorMatchOffset,
       "dhcpGroupVendorMatchLength": dhcpGroupVendorMatchLength,
       "dhcpGroupClientMatchString": dhcpGroupClientMatchString,
       "dhcpGroupClientMatchOffset": dhcpGroupClientMatchOffset,
       "dhcpGroupClientMatchLength": dhcpGroupClientMatchLength,
       "dhcpGroupRowStatus": dhcpGroupRowStatus,
       "dhcpServerGroupOptionTable": dhcpServerGroupOptionTable,
       "dhcpServerGroupOptionEntry": dhcpServerGroupOptionEntry,
       "dhcpGroupOptionDefaultLeaseTime": dhcpGroupOptionDefaultLeaseTime,
       "dhcpGroupOptionMinLeaseTime": dhcpGroupOptionMinLeaseTime,
       "dhcpGroupOptionMaxLeaseTime": dhcpGroupOptionMaxLeaseTime,
       "dhcpGroupOptionBootFile": dhcpGroupOptionBootFile,
       "dhcpGroupOptionBootServer": dhcpGroupOptionBootServer,
       "dhcpGroupOptionDefaultRouter": dhcpGroupOptionDefaultRouter,
       "dhcpGroupOptionPrimaryNameServer": dhcpGroupOptionPrimaryNameServer,
       "dhcpGroupOptionSecondaryNameServer": dhcpGroupOptionSecondaryNameServer,
       "dhcpGroupOptionDomainName": dhcpGroupOptionDomainName,
       "dhcpServerNextSubnetIndex": dhcpServerNextSubnetIndex,
       "dhcpServerSubnetTable": dhcpServerSubnetTable,
       "dhcpServerSubnetEntry": dhcpServerSubnetEntry,
       "dhcpSubnetIndex": dhcpSubnetIndex,
       "dhcpSubnetNetwork": dhcpSubnetNetwork,
       "dhcpSubnetNetmask": dhcpSubnetNetmask,
       "dhcpSubnetDomain": dhcpSubnetDomain,
       "dhcpSubnetRange1Start": dhcpSubnetRange1Start,
       "dhcpSubnetRange1End": dhcpSubnetRange1End,
       "dhcpSubnetRange2Start": dhcpSubnetRange2Start,
       "dhcpSubnetRange2End": dhcpSubnetRange2End,
       "dhcpSubnetRange3Start": dhcpSubnetRange3Start,
       "dhcpSubnetRange3End": dhcpSubnetRange3End,
       "dhcpSubnetRange4Start": dhcpSubnetRange4Start,
       "dhcpSubnetRange4End": dhcpSubnetRange4End,
       "dhcpSubnetRowStatus": dhcpSubnetRowStatus,
       "dhcpSubnetGroup2": dhcpSubnetGroup2,
       "dhcpStickyAddr": dhcpStickyAddr,
       "dhcpSubnetExternalServer": dhcpSubnetExternalServer,
       "dhcpSubnetExternalServerAlt": dhcpSubnetExternalServerAlt,
       "dhcpServerSubnetOptionTable": dhcpServerSubnetOptionTable,
       "dhcpServerSubnetOptionEntry": dhcpServerSubnetOptionEntry,
       "dhcpSubnetOptionDefaultLeaseTime": dhcpSubnetOptionDefaultLeaseTime,
       "dhcpSubnetOptionMinLeaseTime": dhcpSubnetOptionMinLeaseTime,
       "dhcpSubnetOptionMaxLeaseTime": dhcpSubnetOptionMaxLeaseTime,
       "dhcpSubnetOptionBootFile": dhcpSubnetOptionBootFile,
       "dhcpSubnetOptionBootServer": dhcpSubnetOptionBootServer,
       "dhcpSubnetOptionDefaultRouter": dhcpSubnetOptionDefaultRouter,
       "dhcpSubnetOptionPrimaryNameServer": dhcpSubnetOptionPrimaryNameServer,
       "dhcpSubnetOptionSecondaryNameServer": dhcpSubnetOptionSecondaryNameServer,
       "dhcpSubnetOptionDomainName": dhcpSubnetOptionDomainName,
       "dhcpServerNextHostIndex": dhcpServerNextHostIndex,
       "dhcpServerHostTable": dhcpServerHostTable,
       "dhcpServerHostEntry": dhcpServerHostEntry,
       "dhcpHostIndex": dhcpHostIndex,
       "dhcpHostHostname": dhcpHostHostname,
       "dhcpHostDomain": dhcpHostDomain,
       "dhcpHostHardwareAddress": dhcpHostHardwareAddress,
       "dhcpHostClientId": dhcpHostClientId,
       "dhcpHostIpAddress1": dhcpHostIpAddress1,
       "dhcpHostIpAddress2": dhcpHostIpAddress2,
       "dhcpHostIpAddress3": dhcpHostIpAddress3,
       "dhcpHostIpAddress4": dhcpHostIpAddress4,
       "dhcpHostRowStatus": dhcpHostRowStatus,
       "dhcpServerHostOptionTable": dhcpServerHostOptionTable,
       "dhcpServerHostOptionEntry": dhcpServerHostOptionEntry,
       "dhcpHostOptionDefaultLeaseTime": dhcpHostOptionDefaultLeaseTime,
       "dhcpHostOptionMinLeaseTime": dhcpHostOptionMinLeaseTime,
       "dhcpHostOptionMaxLeaseTime": dhcpHostOptionMaxLeaseTime,
       "dhcpHostOptionBootFile": dhcpHostOptionBootFile,
       "dhcpHostOptionBootServer": dhcpHostOptionBootServer,
       "dhcpHostOptionDefaultRouter": dhcpHostOptionDefaultRouter,
       "dhcpHostOptionPrimaryNameServer": dhcpHostOptionPrimaryNameServer,
       "dhcpHostOptionSecondaryNameServer": dhcpHostOptionSecondaryNameServer,
       "dhcpHostOptionDomainName": dhcpHostOptionDomainName,
       "dhcpServerStatistics": dhcpServerStatistics,
       "serverSystem": serverSystem,
       "serverSystemDescr": serverSystemDescr,
       "serverSystemObjectID": serverSystemObjectID,
       "serverUptime": serverUptime,
       "serverActiveShelf": serverActiveShelf,
       "serverActiveSlot": serverActiveSlot,
       "serverStandbyShelf": serverStandbyShelf,
       "serverStandbySlot": serverStandbySlot,
       "bootpCountersTable": bootpCountersTable,
       "bootpCountersEntry": bootpCountersEntry,
       "bootpCountRequests": bootpCountRequests,
       "bootpCountInvalids": bootpCountInvalids,
       "bootpCountReplies": bootpCountReplies,
       "bootpCountDroppedUnknownClients": bootpCountDroppedUnknownClients,
       "bootpCountDroppedNotServingSubnet": bootpCountDroppedNotServingSubnet,
       "dhcpCountersTable": dhcpCountersTable,
       "dhcpCountersEntry": dhcpCountersEntry,
       "dhcpCountDiscovers": dhcpCountDiscovers,
       "dhcpCountRequests": dhcpCountRequests,
       "dhcpCountReleases": dhcpCountReleases,
       "dhcpCountDeclines": dhcpCountDeclines,
       "dhcpCountInforms": dhcpCountInforms,
       "dhcpCountInvalids": dhcpCountInvalids,
       "dhcpCountOffers": dhcpCountOffers,
       "dhcpCountAcks": dhcpCountAcks,
       "dhcpCountNacks": dhcpCountNacks,
       "dhcpCountDroppedUnknownClient": dhcpCountDroppedUnknownClient,
       "dhcpCountDroppedNotServingSubnet": dhcpCountDroppedNotServingSubnet,
       "dhcpServerConfigurationVersion": dhcpServerConfigurationVersion,
       "dhcpServerRestart": dhcpServerRestart,
       "comIpDhcpServer": comIpDhcpServer}
)
