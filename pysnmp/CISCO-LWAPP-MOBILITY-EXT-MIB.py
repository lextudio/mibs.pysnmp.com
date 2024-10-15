# SNMP MIB module (CISCO-LWAPP-MOBILITY-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-MOBILITY-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:18 2024
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

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappMobilityExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999)
)
ciscoLwappMobilityExtMIB.setRevisions(
        ("2014-04-14 00:00",
         "2013-01-09 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoAbsZeroBasedCounter64(Counter64, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoLwappMobilityExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtMIBNotifs = _CiscoLwappMobilityExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 0)
)
_CiscoLwappMobilityExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtMIBObjects = _CiscoLwappMobilityExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1)
)
_CiscoLwappMobilityExtGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtGlobalObjects = _CiscoLwappMobilityExtGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1)
)
_CiscoLwappMobilityExtMCGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtMCGlobalObjects = _CiscoLwappMobilityExtMCGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1)
)


class _CLMobilityExtMCMOEnableStatus_Type(TruthValue):
    """Custom type cLMobilityExtMCMOEnableStatus based on TruthValue"""


_CLMobilityExtMCMOEnableStatus_Object = MibScalar
cLMobilityExtMCMOEnableStatus = _CLMobilityExtMCMOEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 1),
    _CLMobilityExtMCMOEnableStatus_Type()
)
cLMobilityExtMCMOEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCMOEnableStatus.setStatus("current")


class _CLMobilityExtMCMOAdminEnableStatus_Type(TruthValue):
    """Custom type cLMobilityExtMCMOAdminEnableStatus based on TruthValue"""


_CLMobilityExtMCMOAdminEnableStatus_Object = MibScalar
cLMobilityExtMCMOAdminEnableStatus = _CLMobilityExtMCMOAdminEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 2),
    _CLMobilityExtMCMOAdminEnableStatus_Type()
)
cLMobilityExtMCMOAdminEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCMOAdminEnableStatus.setStatus("current")


class _CLMobilityExtMCEnableStatus_Type(TruthValue):
    """Custom type cLMobilityExtMCEnableStatus based on TruthValue"""


_CLMobilityExtMCEnableStatus_Object = MibScalar
cLMobilityExtMCEnableStatus = _CLMobilityExtMCEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 3),
    _CLMobilityExtMCEnableStatus_Type()
)
cLMobilityExtMCEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCEnableStatus.setStatus("current")


class _CLMobilityExtMCAdminEnableStatus_Type(TruthValue):
    """Custom type cLMobilityExtMCAdminEnableStatus based on TruthValue"""


_CLMobilityExtMCAdminEnableStatus_Object = MibScalar
cLMobilityExtMCAdminEnableStatus = _CLMobilityExtMCAdminEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 4),
    _CLMobilityExtMCAdminEnableStatus_Type()
)
cLMobilityExtMCAdminEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCAdminEnableStatus.setStatus("current")


class _CLMobilityExtMCMulticastMode_Type(TruthValue):
    """Custom type cLMobilityExtMCMulticastMode based on TruthValue"""


_CLMobilityExtMCMulticastMode_Object = MibScalar
cLMobilityExtMCMulticastMode = _CLMobilityExtMCMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 5),
    _CLMobilityExtMCMulticastMode_Type()
)
cLMobilityExtMCMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCMulticastMode.setStatus("current")


class _CLMobilityExtMCKeepAliveCount_Type(Unsigned32):
    """Custom type cLMobilityExtMCKeepAliveCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_CLMobilityExtMCKeepAliveCount_Type.__name__ = "Unsigned32"
_CLMobilityExtMCKeepAliveCount_Object = MibScalar
cLMobilityExtMCKeepAliveCount = _CLMobilityExtMCKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 6),
    _CLMobilityExtMCKeepAliveCount_Type()
)
cLMobilityExtMCKeepAliveCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCKeepAliveCount.setStatus("current")


class _CLMobilityExtMCKeepAliveInterval_Type(Unsigned32):
    """Custom type cLMobilityExtMCKeepAliveInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CLMobilityExtMCKeepAliveInterval_Type.__name__ = "Unsigned32"
_CLMobilityExtMCKeepAliveInterval_Object = MibScalar
cLMobilityExtMCKeepAliveInterval = _CLMobilityExtMCKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 7),
    _CLMobilityExtMCKeepAliveInterval_Type()
)
cLMobilityExtMCKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCKeepAliveInterval.setStatus("current")


class _CLMobilityExtMCDscpValue_Type(Unsigned32):
    """Custom type cLMobilityExtMCDscpValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CLMobilityExtMCDscpValue_Type.__name__ = "Unsigned32"
_CLMobilityExtMCDscpValue_Object = MibScalar
cLMobilityExtMCDscpValue = _CLMobilityExtMCDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 8),
    _CLMobilityExtMCDscpValue_Type()
)
cLMobilityExtMCDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCDscpValue.setStatus("current")
_CLMobilityExtMCMOPublicAddressType_Type = InetAddressType
_CLMobilityExtMCMOPublicAddressType_Object = MibScalar
cLMobilityExtMCMOPublicAddressType = _CLMobilityExtMCMOPublicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 9),
    _CLMobilityExtMCMOPublicAddressType_Type()
)
cLMobilityExtMCMOPublicAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCMOPublicAddressType.setStatus("current")
_CLMobilityExtMCMOPublicAddress_Type = InetAddress
_CLMobilityExtMCMOPublicAddress_Object = MibScalar
cLMobilityExtMCMOPublicAddress = _CLMobilityExtMCMOPublicAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 10),
    _CLMobilityExtMCMOPublicAddress_Type()
)
cLMobilityExtMCMOPublicAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCMOPublicAddress.setStatus("current")
_CLMobilityExtMCApCountLicensesInUse_Type = Unsigned32
_CLMobilityExtMCApCountLicensesInUse_Object = MibScalar
cLMobilityExtMCApCountLicensesInUse = _CLMobilityExtMCApCountLicensesInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 11),
    _CLMobilityExtMCApCountLicensesInUse_Type()
)
cLMobilityExtMCApCountLicensesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCApCountLicensesInUse.setStatus("current")
_CLMobilityExtMCOwnGroupMulticastAddressType_Type = InetAddressType
_CLMobilityExtMCOwnGroupMulticastAddressType_Object = MibScalar
cLMobilityExtMCOwnGroupMulticastAddressType = _CLMobilityExtMCOwnGroupMulticastAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 12),
    _CLMobilityExtMCOwnGroupMulticastAddressType_Type()
)
cLMobilityExtMCOwnGroupMulticastAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCOwnGroupMulticastAddressType.setStatus("current")
_CLMobilityExtMCOwnGroupMulticastAddress_Type = InetAddress
_CLMobilityExtMCOwnGroupMulticastAddress_Object = MibScalar
cLMobilityExtMCOwnGroupMulticastAddress = _CLMobilityExtMCOwnGroupMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 13),
    _CLMobilityExtMCOwnGroupMulticastAddress_Type()
)
cLMobilityExtMCOwnGroupMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCOwnGroupMulticastAddress.setStatus("current")
_CLMobilityExtMCMobilityGroupName_Type = SnmpAdminString
_CLMobilityExtMCMobilityGroupName_Object = MibScalar
cLMobilityExtMCMobilityGroupName = _CLMobilityExtMCMobilityGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 14),
    _CLMobilityExtMCMobilityGroupName_Type()
)
cLMobilityExtMCMobilityGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMCMobilityGroupName.setStatus("current")
_CiscoLwappMobilityExtMCMAGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtMCMAGlobalObjects = _CiscoLwappMobilityExtMCMAGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2)
)
_CLMobilityExtMgrAddressType_Type = InetAddressType
_CLMobilityExtMgrAddressType_Object = MibScalar
cLMobilityExtMgrAddressType = _CLMobilityExtMgrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 1),
    _CLMobilityExtMgrAddressType_Type()
)
cLMobilityExtMgrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMgrAddressType.setStatus("current")
_CLMobilityExtMgrAddress_Type = InetAddress
_CLMobilityExtMgrAddress_Object = MibScalar
cLMobilityExtMgrAddress = _CLMobilityExtMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 2),
    _CLMobilityExtMgrAddress_Type()
)
cLMobilityExtMgrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMgrAddress.setStatus("current")
_CLMobilityExtMgrNetmaskType_Type = InetAddressType
_CLMobilityExtMgrNetmaskType_Object = MibScalar
cLMobilityExtMgrNetmaskType = _CLMobilityExtMgrNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 3),
    _CLMobilityExtMgrNetmaskType_Type()
)
cLMobilityExtMgrNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMgrNetmaskType.setStatus("current")
_CLMobilityExtMgrNetmask_Type = InetAddress
_CLMobilityExtMgrNetmask_Object = MibScalar
cLMobilityExtMgrNetmask = _CLMobilityExtMgrNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 4),
    _CLMobilityExtMgrNetmask_Type()
)
cLMobilityExtMgrNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMgrNetmask.setStatus("current")
_CLMobilityExtMgrMacAddress_Type = MacAddress
_CLMobilityExtMgrMacAddress_Object = MibScalar
cLMobilityExtMgrMacAddress = _CLMobilityExtMgrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 5),
    _CLMobilityExtMgrMacAddress_Type()
)
cLMobilityExtMgrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMgrMacAddress.setStatus("current")
_CLMobilityExtMgrVlanId_Type = Unsigned32
_CLMobilityExtMgrVlanId_Object = MibScalar
cLMobilityExtMgrVlanId = _CLMobilityExtMgrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 6),
    _CLMobilityExtMgrVlanId_Type()
)
cLMobilityExtMgrVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMgrVlanId.setStatus("current")
_CLMobilityExtMgrName_Type = SnmpAdminString
_CLMobilityExtMgrName_Object = MibScalar
cLMobilityExtMgrName = _CLMobilityExtMgrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 7),
    _CLMobilityExtMgrName_Type()
)
cLMobilityExtMgrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMgrName.setStatus("current")


class _CLMobilityExtMgrInterfaceType_Type(Integer32):
    """Custom type cLMobilityExtMgrInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 2),
          ("management", 1))
    )


_CLMobilityExtMgrInterfaceType_Type.__name__ = "Integer32"
_CLMobilityExtMgrInterfaceType_Object = MibScalar
cLMobilityExtMgrInterfaceType = _CLMobilityExtMgrInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 8),
    _CLMobilityExtMgrInterfaceType_Type()
)
cLMobilityExtMgrInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMgrInterfaceType.setStatus("current")
_CLMobilityExtNewArchitectureEnableStatus_Type = TruthValue
_CLMobilityExtNewArchitectureEnableStatus_Object = MibScalar
cLMobilityExtNewArchitectureEnableStatus = _CLMobilityExtNewArchitectureEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 9),
    _CLMobilityExtNewArchitectureEnableStatus_Type()
)
cLMobilityExtNewArchitectureEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtNewArchitectureEnableStatus.setStatus("current")
_CLMobilityExtNewArchitectureAdminEnableStatus_Type = TruthValue
_CLMobilityExtNewArchitectureAdminEnableStatus_Object = MibScalar
cLMobilityExtNewArchitectureAdminEnableStatus = _CLMobilityExtNewArchitectureAdminEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 2, 10),
    _CLMobilityExtNewArchitectureAdminEnableStatus_Type()
)
cLMobilityExtNewArchitectureAdminEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtNewArchitectureAdminEnableStatus.setStatus("current")
_CiscoLwappMobilityExtMAGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtMAGlobalObjects = _CiscoLwappMobilityExtMAGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3)
)
_CLMobilityExtMAMCPublicAddressType_Type = InetAddressType
_CLMobilityExtMAMCPublicAddressType_Object = MibScalar
cLMobilityExtMAMCPublicAddressType = _CLMobilityExtMAMCPublicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 1),
    _CLMobilityExtMAMCPublicAddressType_Type()
)
cLMobilityExtMAMCPublicAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMAMCPublicAddressType.setStatus("current")
_CLMobilityExtMAMCPublicAddress_Type = InetAddress
_CLMobilityExtMAMCPublicAddress_Object = MibScalar
cLMobilityExtMAMCPublicAddress = _CLMobilityExtMAMCPublicAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 2),
    _CLMobilityExtMAMCPublicAddress_Type()
)
cLMobilityExtMAMCPublicAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMAMCPublicAddress.setStatus("current")
_CLMobilityExtMAMCPrivateAddressType_Type = InetAddressType
_CLMobilityExtMAMCPrivateAddressType_Object = MibScalar
cLMobilityExtMAMCPrivateAddressType = _CLMobilityExtMAMCPrivateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 3),
    _CLMobilityExtMAMCPrivateAddressType_Type()
)
cLMobilityExtMAMCPrivateAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMAMCPrivateAddressType.setStatus("current")
_CLMobilityExtMAMCPrivateAddress_Type = InetAddress
_CLMobilityExtMAMCPrivateAddress_Object = MibScalar
cLMobilityExtMAMCPrivateAddress = _CLMobilityExtMAMCPrivateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 4),
    _CLMobilityExtMAMCPrivateAddress_Type()
)
cLMobilityExtMAMCPrivateAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtMAMCPrivateAddress.setStatus("current")


class _CLMobilityExtMAToMCLinkStatus_Type(Integer32):
    """Custom type cLMobilityExtMAToMCLinkStatus based on Integer32"""
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
        *(("bothdown", 3),
          ("controlpathdown", 2),
          ("datapathdown", 1),
          ("notconfigured", 0),
          ("up", 4))
    )


_CLMobilityExtMAToMCLinkStatus_Type.__name__ = "Integer32"
_CLMobilityExtMAToMCLinkStatus_Object = MibScalar
cLMobilityExtMAToMCLinkStatus = _CLMobilityExtMAToMCLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 5),
    _CLMobilityExtMAToMCLinkStatus_Type()
)
cLMobilityExtMAToMCLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMAToMCLinkStatus.setStatus("current")
_CLMobilityExtMASpgPeerCount_Type = Unsigned32
_CLMobilityExtMASpgPeerCount_Object = MibScalar
cLMobilityExtMASpgPeerCount = _CLMobilityExtMASpgPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 6),
    _CLMobilityExtMASpgPeerCount_Type()
)
cLMobilityExtMASpgPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMASpgPeerCount.setStatus("current")


class _CLMobilityExtMASpgName_Type(SnmpAdminString):
    """Custom type cLMobilityExtMASpgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLMobilityExtMASpgName_Type.__name__ = "SnmpAdminString"
_CLMobilityExtMASpgName_Object = MibScalar
cLMobilityExtMASpgName = _CLMobilityExtMASpgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 7),
    _CLMobilityExtMASpgName_Type()
)
cLMobilityExtMASpgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMASpgName.setStatus("current")
_CLMobilityExtMAOwnMulticastAddressType_Type = InetAddressType
_CLMobilityExtMAOwnMulticastAddressType_Object = MibScalar
cLMobilityExtMAOwnMulticastAddressType = _CLMobilityExtMAOwnMulticastAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 8),
    _CLMobilityExtMAOwnMulticastAddressType_Type()
)
cLMobilityExtMAOwnMulticastAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMAOwnMulticastAddressType.setStatus("current")
_CLMobilityExtMAOwnMulticastAddress_Type = InetAddress
_CLMobilityExtMAOwnMulticastAddress_Object = MibScalar
cLMobilityExtMAOwnMulticastAddress = _CLMobilityExtMAOwnMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 9),
    _CLMobilityExtMAOwnMulticastAddress_Type()
)
cLMobilityExtMAOwnMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMAOwnMulticastAddress.setStatus("current")


class _CLMobilityExtMAKeepAliveCount_Type(Unsigned32):
    """Custom type cLMobilityExtMAKeepAliveCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_CLMobilityExtMAKeepAliveCount_Type.__name__ = "Unsigned32"
_CLMobilityExtMAKeepAliveCount_Object = MibScalar
cLMobilityExtMAKeepAliveCount = _CLMobilityExtMAKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 10),
    _CLMobilityExtMAKeepAliveCount_Type()
)
cLMobilityExtMAKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMAKeepAliveCount.setStatus("current")


class _CLMobilityExtMAKeepAliveInterval_Type(Unsigned32):
    """Custom type cLMobilityExtMAKeepAliveInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CLMobilityExtMAKeepAliveInterval_Type.__name__ = "Unsigned32"
_CLMobilityExtMAKeepAliveInterval_Object = MibScalar
cLMobilityExtMAKeepAliveInterval = _CLMobilityExtMAKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 11),
    _CLMobilityExtMAKeepAliveInterval_Type()
)
cLMobilityExtMAKeepAliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMAKeepAliveInterval.setStatus("current")


class _CLMobilityExtMADscpValue_Type(Unsigned32):
    """Custom type cLMobilityExtMADscpValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CLMobilityExtMADscpValue_Type.__name__ = "Unsigned32"
_CLMobilityExtMADscpValue_Object = MibScalar
cLMobilityExtMADscpValue = _CLMobilityExtMADscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 3, 12),
    _CLMobilityExtMADscpValue_Type()
)
cLMobilityExtMADscpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMADscpValue.setStatus("current")
_CiscoLwappMobilityExtMCStats_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtMCStats = _CiscoLwappMobilityExtMCStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4)
)
_CLMobilityExtMCReceivedTotal_Type = Counter32
_CLMobilityExtMCReceivedTotal_Object = MibScalar
cLMobilityExtMCReceivedTotal = _CLMobilityExtMCReceivedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 1),
    _CLMobilityExtMCReceivedTotal_Type()
)
cLMobilityExtMCReceivedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCReceivedTotal.setStatus("current")
_CLMobilityExtMCReceivedDrops_Type = Counter32
_CLMobilityExtMCReceivedDrops_Object = MibScalar
cLMobilityExtMCReceivedDrops = _CLMobilityExtMCReceivedDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 2),
    _CLMobilityExtMCReceivedDrops_Type()
)
cLMobilityExtMCReceivedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCReceivedDrops.setStatus("current")
_CLMobilityExtMCProtocolReceiveErrors_Type = Counter32
_CLMobilityExtMCProtocolReceiveErrors_Object = MibScalar
cLMobilityExtMCProtocolReceiveErrors = _CLMobilityExtMCProtocolReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 3),
    _CLMobilityExtMCProtocolReceiveErrors_Type()
)
cLMobilityExtMCProtocolReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCProtocolReceiveErrors.setStatus("current")
_CLMobilityExtMCProtocolTransmitErrors_Type = Counter32
_CLMobilityExtMCProtocolTransmitErrors_Object = MibScalar
cLMobilityExtMCProtocolTransmitErrors = _CLMobilityExtMCProtocolTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 4),
    _CLMobilityExtMCProtocolTransmitErrors_Type()
)
cLMobilityExtMCProtocolTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCProtocolTransmitErrors.setStatus("current")
_CLMobilityExtMCStateErrors_Type = Counter32
_CLMobilityExtMCStateErrors_Object = MibScalar
cLMobilityExtMCStateErrors = _CLMobilityExtMCStateErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 5),
    _CLMobilityExtMCStateErrors_Type()
)
cLMobilityExtMCStateErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCStateErrors.setStatus("current")
_CLMobilityExtMCProtocolRetransmitted_Type = Counter32
_CLMobilityExtMCProtocolRetransmitted_Object = MibScalar
cLMobilityExtMCProtocolRetransmitted = _CLMobilityExtMCProtocolRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 6),
    _CLMobilityExtMCProtocolRetransmitted_Type()
)
cLMobilityExtMCProtocolRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCProtocolRetransmitted.setStatus("current")
_CLMobilityExtMCHandoffRequestsReceived_Type = Counter32
_CLMobilityExtMCHandoffRequestsReceived_Object = MibScalar
cLMobilityExtMCHandoffRequestsReceived = _CLMobilityExtMCHandoffRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 7),
    _CLMobilityExtMCHandoffRequestsReceived_Type()
)
cLMobilityExtMCHandoffRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCHandoffRequestsReceived.setStatus("current")
_CLMobilityExtMCHandoffCmplReceived_Type = Counter32
_CLMobilityExtMCHandoffCmplReceived_Object = MibScalar
cLMobilityExtMCHandoffCmplReceived = _CLMobilityExtMCHandoffCmplReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 8),
    _CLMobilityExtMCHandoffCmplReceived_Type()
)
cLMobilityExtMCHandoffCmplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCHandoffCmplReceived.setStatus("current")
_CLMobilityExtMCHandoffClientDeleteReceived_Type = Counter32
_CLMobilityExtMCHandoffClientDeleteReceived_Object = MibScalar
cLMobilityExtMCHandoffClientDeleteReceived = _CLMobilityExtMCHandoffClientDeleteReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 9),
    _CLMobilityExtMCHandoffClientDeleteReceived_Type()
)
cLMobilityExtMCHandoffClientDeleteReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCHandoffClientDeleteReceived.setStatus("current")
_CLMobilityExtMCHandoffRequestsTransmitted_Type = Counter32
_CLMobilityExtMCHandoffRequestsTransmitted_Object = MibScalar
cLMobilityExtMCHandoffRequestsTransmitted = _CLMobilityExtMCHandoffRequestsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 10),
    _CLMobilityExtMCHandoffRequestsTransmitted_Type()
)
cLMobilityExtMCHandoffRequestsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCHandoffRequestsTransmitted.setStatus("current")
_CLMobilityExtMCHandoffCmplTransmitted_Type = Counter32
_CLMobilityExtMCHandoffCmplTransmitted_Object = MibScalar
cLMobilityExtMCHandoffCmplTransmitted = _CLMobilityExtMCHandoffCmplTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 11),
    _CLMobilityExtMCHandoffCmplTransmitted_Type()
)
cLMobilityExtMCHandoffCmplTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCHandoffCmplTransmitted.setStatus("current")
_CLMobilityExtMCHandoffClientDeleteTransmitted_Type = Counter32
_CLMobilityExtMCHandoffClientDeleteTransmitted_Object = MibScalar
cLMobilityExtMCHandoffClientDeleteTransmitted = _CLMobilityExtMCHandoffClientDeleteTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 12),
    _CLMobilityExtMCHandoffClientDeleteTransmitted_Type()
)
cLMobilityExtMCHandoffClientDeleteTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCHandoffClientDeleteTransmitted.setStatus("current")
_CLMobilityExtMCTotalClientCount_Type = Counter32
_CLMobilityExtMCTotalClientCount_Object = MibScalar
cLMobilityExtMCTotalClientCount = _CLMobilityExtMCTotalClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 13),
    _CLMobilityExtMCTotalClientCount_Type()
)
cLMobilityExtMCTotalClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCTotalClientCount.setStatus("current")
_CLMobilityExtMCWgbCount_Type = Counter32
_CLMobilityExtMCWgbCount_Object = MibScalar
cLMobilityExtMCWgbCount = _CLMobilityExtMCWgbCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 4, 14),
    _CLMobilityExtMCWgbCount_Type()
)
cLMobilityExtMCWgbCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCWgbCount.setStatus("current")
_CiscoLwappMobilityExtTableObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtTableObjects = _CiscoLwappMobilityExtTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2)
)
_CLMobilityExtSpgTable_Object = MibTable
cLMobilityExtSpgTable = _CLMobilityExtSpgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLMobilityExtSpgTable.setStatus("current")
_CLMobilityExtSpgEntry_Object = MibTableRow
cLMobilityExtSpgEntry = _CLMobilityExtSpgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1, 1)
)
cLMobilityExtSpgEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgGroupName"),
)
if mibBuilder.loadTexts:
    cLMobilityExtSpgEntry.setStatus("current")


class _CLMobilityExtSpgGroupName_Type(SnmpAdminString):
    """Custom type cLMobilityExtSpgGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLMobilityExtSpgGroupName_Type.__name__ = "SnmpAdminString"
_CLMobilityExtSpgGroupName_Object = MibTableColumn
cLMobilityExtSpgGroupName = _CLMobilityExtSpgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1, 1, 1),
    _CLMobilityExtSpgGroupName_Type()
)
cLMobilityExtSpgGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtSpgGroupName.setStatus("current")
_CLMobilityExtSpgGroupId_Type = Unsigned32
_CLMobilityExtSpgGroupId_Object = MibTableColumn
cLMobilityExtSpgGroupId = _CLMobilityExtSpgGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1, 1, 2),
    _CLMobilityExtSpgGroupId_Type()
)
cLMobilityExtSpgGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtSpgGroupId.setStatus("current")
_CLMobilityExtSpgBridgeDomainId_Type = Unsigned32
_CLMobilityExtSpgBridgeDomainId_Object = MibTableColumn
cLMobilityExtSpgBridgeDomainId = _CLMobilityExtSpgBridgeDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1, 1, 3),
    _CLMobilityExtSpgBridgeDomainId_Type()
)
cLMobilityExtSpgBridgeDomainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtSpgBridgeDomainId.setStatus("current")
_CLMobilityExtSpgMemberCount_Type = Unsigned32
_CLMobilityExtSpgMemberCount_Object = MibTableColumn
cLMobilityExtSpgMemberCount = _CLMobilityExtSpgMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1, 1, 4),
    _CLMobilityExtSpgMemberCount_Type()
)
cLMobilityExtSpgMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMemberCount.setStatus("current")
_CLMobilityExtSpgMulticastAddressType_Type = InetAddressType
_CLMobilityExtSpgMulticastAddressType_Object = MibTableColumn
cLMobilityExtSpgMulticastAddressType = _CLMobilityExtSpgMulticastAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1, 1, 5),
    _CLMobilityExtSpgMulticastAddressType_Type()
)
cLMobilityExtSpgMulticastAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMulticastAddressType.setStatus("current")
_CLMobilityExtSpgMulticastAddress_Type = InetAddress
_CLMobilityExtSpgMulticastAddress_Object = MibTableColumn
cLMobilityExtSpgMulticastAddress = _CLMobilityExtSpgMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1, 1, 6),
    _CLMobilityExtSpgMulticastAddress_Type()
)
cLMobilityExtSpgMulticastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMulticastAddress.setStatus("current")
_CLMobilityExtSpgMulticastMode_Type = TruthValue
_CLMobilityExtSpgMulticastMode_Object = MibTableColumn
cLMobilityExtSpgMulticastMode = _CLMobilityExtSpgMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1, 1, 7),
    _CLMobilityExtSpgMulticastMode_Type()
)
cLMobilityExtSpgMulticastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMulticastMode.setStatus("current")
_CLMobilityExtSpgRowStatus_Type = RowStatus
_CLMobilityExtSpgRowStatus_Object = MibTableColumn
cLMobilityExtSpgRowStatus = _CLMobilityExtSpgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 1, 1, 8),
    _CLMobilityExtSpgRowStatus_Type()
)
cLMobilityExtSpgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtSpgRowStatus.setStatus("current")
_CLMobilityExtSpgMemberTable_Object = MibTable
cLMobilityExtSpgMemberTable = _CLMobilityExtSpgMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLMobilityExtSpgMemberTable.setStatus("current")
_CLMobilityExtSpgMemberEntry_Object = MibTableRow
cLMobilityExtSpgMemberEntry = _CLMobilityExtSpgMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 2, 1)
)
cLMobilityExtSpgMemberEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgGroupName"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberPrivateAddressType"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberPrivateAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityExtSpgMemberEntry.setStatus("current")
_CLMobilityExtSpgMemberPrivateAddressType_Type = InetAddressType
_CLMobilityExtSpgMemberPrivateAddressType_Object = MibTableColumn
cLMobilityExtSpgMemberPrivateAddressType = _CLMobilityExtSpgMemberPrivateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 2, 1, 1),
    _CLMobilityExtSpgMemberPrivateAddressType_Type()
)
cLMobilityExtSpgMemberPrivateAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMemberPrivateAddressType.setStatus("current")
_CLMobilityExtSpgMemberPrivateAddress_Type = InetAddress
_CLMobilityExtSpgMemberPrivateAddress_Object = MibTableColumn
cLMobilityExtSpgMemberPrivateAddress = _CLMobilityExtSpgMemberPrivateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 2, 1, 2),
    _CLMobilityExtSpgMemberPrivateAddress_Type()
)
cLMobilityExtSpgMemberPrivateAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMemberPrivateAddress.setStatus("current")


class _CLMobilityExtSpgMemberStatus_Type(Integer32):
    """Custom type cLMobilityExtSpgMemberStatus based on Integer32"""
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
        *(("bothdown", 3),
          ("controlpathdown", 2),
          ("datapathdown", 1),
          ("notconfigured", 0),
          ("up", 4))
    )


_CLMobilityExtSpgMemberStatus_Type.__name__ = "Integer32"
_CLMobilityExtSpgMemberStatus_Object = MibTableColumn
cLMobilityExtSpgMemberStatus = _CLMobilityExtSpgMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 2, 1, 3),
    _CLMobilityExtSpgMemberStatus_Type()
)
cLMobilityExtSpgMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMemberStatus.setStatus("current")
_CLMobilityExtSpgMemberPublicAddressType_Type = InetAddressType
_CLMobilityExtSpgMemberPublicAddressType_Object = MibTableColumn
cLMobilityExtSpgMemberPublicAddressType = _CLMobilityExtSpgMemberPublicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 2, 1, 4),
    _CLMobilityExtSpgMemberPublicAddressType_Type()
)
cLMobilityExtSpgMemberPublicAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMemberPublicAddressType.setStatus("current")
_CLMobilityExtSpgMemberPublicAddress_Type = InetAddress
_CLMobilityExtSpgMemberPublicAddress_Object = MibTableColumn
cLMobilityExtSpgMemberPublicAddress = _CLMobilityExtSpgMemberPublicAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 2, 1, 5),
    _CLMobilityExtSpgMemberPublicAddress_Type()
)
cLMobilityExtSpgMemberPublicAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMemberPublicAddress.setStatus("current")
_CLMobilityExtSpgMemberRowStatus_Type = RowStatus
_CLMobilityExtSpgMemberRowStatus_Object = MibTableColumn
cLMobilityExtSpgMemberRowStatus = _CLMobilityExtSpgMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 2, 1, 6),
    _CLMobilityExtSpgMemberRowStatus_Type()
)
cLMobilityExtSpgMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtSpgMemberRowStatus.setStatus("current")
_CLMobilityExtGroupMemberTable_Object = MibTable
cLMobilityExtGroupMemberTable = _CLMobilityExtGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberTable.setStatus("current")
_CLMobilityExtGroupMemberEntry_Object = MibTableRow
cLMobilityExtGroupMemberEntry = _CLMobilityExtGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1)
)
cLMobilityExtGroupMemberEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberPrivateAddressType"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberPrivateAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberEntry.setStatus("current")
_CLMobilityExtGroupMemberPrivateAddressType_Type = InetAddressType
_CLMobilityExtGroupMemberPrivateAddressType_Object = MibTableColumn
cLMobilityExtGroupMemberPrivateAddressType = _CLMobilityExtGroupMemberPrivateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 1),
    _CLMobilityExtGroupMemberPrivateAddressType_Type()
)
cLMobilityExtGroupMemberPrivateAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberPrivateAddressType.setStatus("current")
_CLMobilityExtGroupMemberPrivateAddress_Type = InetAddress
_CLMobilityExtGroupMemberPrivateAddress_Object = MibTableColumn
cLMobilityExtGroupMemberPrivateAddress = _CLMobilityExtGroupMemberPrivateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 2),
    _CLMobilityExtGroupMemberPrivateAddress_Type()
)
cLMobilityExtGroupMemberPrivateAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberPrivateAddress.setStatus("current")


class _CLMobilityExtGroupMemberGroupName_Type(SnmpAdminString):
    """Custom type cLMobilityExtGroupMemberGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLMobilityExtGroupMemberGroupName_Type.__name__ = "SnmpAdminString"
_CLMobilityExtGroupMemberGroupName_Object = MibTableColumn
cLMobilityExtGroupMemberGroupName = _CLMobilityExtGroupMemberGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 3),
    _CLMobilityExtGroupMemberGroupName_Type()
)
cLMobilityExtGroupMemberGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberGroupName.setStatus("current")
_CLMobilityExtGroupMemberPublicAddressType_Type = InetAddressType
_CLMobilityExtGroupMemberPublicAddressType_Object = MibTableColumn
cLMobilityExtGroupMemberPublicAddressType = _CLMobilityExtGroupMemberPublicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 4),
    _CLMobilityExtGroupMemberPublicAddressType_Type()
)
cLMobilityExtGroupMemberPublicAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberPublicAddressType.setStatus("current")
_CLMobilityExtGroupMemberPublicAddress_Type = InetAddress
_CLMobilityExtGroupMemberPublicAddress_Object = MibTableColumn
cLMobilityExtGroupMemberPublicAddress = _CLMobilityExtGroupMemberPublicAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 5),
    _CLMobilityExtGroupMemberPublicAddress_Type()
)
cLMobilityExtGroupMemberPublicAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberPublicAddress.setStatus("current")


class _CLMobilityExtGroupMemberStatus_Type(Integer32):
    """Custom type cLMobilityExtGroupMemberStatus based on Integer32"""
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
        *(("bothdown", 3),
          ("controlpathdown", 2),
          ("datapathdown", 1),
          ("notconfigured", 0),
          ("up", 4))
    )


_CLMobilityExtGroupMemberStatus_Type.__name__ = "Integer32"
_CLMobilityExtGroupMemberStatus_Object = MibTableColumn
cLMobilityExtGroupMemberStatus = _CLMobilityExtGroupMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 6),
    _CLMobilityExtGroupMemberStatus_Type()
)
cLMobilityExtGroupMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberStatus.setStatus("current")
_CLMobilityExtGroupMemberMacAddress_Type = MacAddress
_CLMobilityExtGroupMemberMacAddress_Object = MibTableColumn
cLMobilityExtGroupMemberMacAddress = _CLMobilityExtGroupMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 7),
    _CLMobilityExtGroupMemberMacAddress_Type()
)
cLMobilityExtGroupMemberMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberMacAddress.setStatus("current")
_CLMobilityExtGroupMemberMulticastAddressType_Type = InetAddressType
_CLMobilityExtGroupMemberMulticastAddressType_Object = MibTableColumn
cLMobilityExtGroupMemberMulticastAddressType = _CLMobilityExtGroupMemberMulticastAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 8),
    _CLMobilityExtGroupMemberMulticastAddressType_Type()
)
cLMobilityExtGroupMemberMulticastAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberMulticastAddressType.setStatus("current")
_CLMobilityExtGroupMemberMulticastAddress_Type = InetAddress
_CLMobilityExtGroupMemberMulticastAddress_Object = MibTableColumn
cLMobilityExtGroupMemberMulticastAddress = _CLMobilityExtGroupMemberMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 9),
    _CLMobilityExtGroupMemberMulticastAddress_Type()
)
cLMobilityExtGroupMemberMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberMulticastAddress.setStatus("current")


class _CLMobilityExtGroupMemberHashKey_Type(OctetString):
    """Custom type cLMobilityExtGroupMemberHashKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 40),
    )


_CLMobilityExtGroupMemberHashKey_Type.__name__ = "OctetString"
_CLMobilityExtGroupMemberHashKey_Object = MibTableColumn
cLMobilityExtGroupMemberHashKey = _CLMobilityExtGroupMemberHashKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 10),
    _CLMobilityExtGroupMemberHashKey_Type()
)
cLMobilityExtGroupMemberHashKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberHashKey.setStatus("current")
_CLMobilityExtGroupMemberRowStatus_Type = RowStatus
_CLMobilityExtGroupMemberRowStatus_Object = MibTableColumn
cLMobilityExtGroupMemberRowStatus = _CLMobilityExtGroupMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 3, 1, 11),
    _CLMobilityExtGroupMemberRowStatus_Type()
)
cLMobilityExtGroupMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMemberRowStatus.setStatus("current")
_CLMobilityExtAnchorTable_Object = MibTable
cLMobilityExtAnchorTable = _CLMobilityExtAnchorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cLMobilityExtAnchorTable.setStatus("current")
_CLMobilityExtAnchorEntry_Object = MibTableRow
cLMobilityExtAnchorEntry = _CLMobilityExtAnchorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 4, 1)
)
cLMobilityExtAnchorEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtAnchorAssociatedMCAddressType"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtAnchorAssociatedMCAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityExtAnchorEntry.setStatus("current")
_CLMobilityExtAnchorAssociatedMCAddressType_Type = InetAddressType
_CLMobilityExtAnchorAssociatedMCAddressType_Object = MibTableColumn
cLMobilityExtAnchorAssociatedMCAddressType = _CLMobilityExtAnchorAssociatedMCAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 4, 1, 1),
    _CLMobilityExtAnchorAssociatedMCAddressType_Type()
)
cLMobilityExtAnchorAssociatedMCAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtAnchorAssociatedMCAddressType.setStatus("current")
_CLMobilityExtAnchorAssociatedMCAddress_Type = InetAddress
_CLMobilityExtAnchorAssociatedMCAddress_Object = MibTableColumn
cLMobilityExtAnchorAssociatedMCAddress = _CLMobilityExtAnchorAssociatedMCAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 4, 1, 2),
    _CLMobilityExtAnchorAssociatedMCAddress_Type()
)
cLMobilityExtAnchorAssociatedMCAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtAnchorAssociatedMCAddress.setStatus("current")


class _CLMobilityExtAnchorStatus_Type(Integer32):
    """Custom type cLMobilityExtAnchorStatus based on Integer32"""
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
        *(("bothdown", 3),
          ("controlpathdown", 2),
          ("datapathdown", 1),
          ("notconfigured", 0),
          ("up", 4))
    )


_CLMobilityExtAnchorStatus_Type.__name__ = "Integer32"
_CLMobilityExtAnchorStatus_Object = MibTableColumn
cLMobilityExtAnchorStatus = _CLMobilityExtAnchorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 4, 1, 3),
    _CLMobilityExtAnchorStatus_Type()
)
cLMobilityExtAnchorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtAnchorStatus.setStatus("current")
_CLMobilityExtAnchorRowStatus_Type = RowStatus
_CLMobilityExtAnchorRowStatus_Object = MibTableColumn
cLMobilityExtAnchorRowStatus = _CLMobilityExtAnchorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 4, 1, 4),
    _CLMobilityExtAnchorRowStatus_Type()
)
cLMobilityExtAnchorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtAnchorRowStatus.setStatus("current")
_CLMobilityExtMOMCTable_Object = MibTable
cLMobilityExtMOMCTable = _CLMobilityExtMOMCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cLMobilityExtMOMCTable.setStatus("current")
_CLMobilityExtMOMCEntry_Object = MibTableRow
cLMobilityExtMOMCEntry = _CLMobilityExtMOMCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 5, 1)
)
cLMobilityExtMOMCEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOMCAddressType"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOMCAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityExtMOMCEntry.setStatus("current")
_CLMobilityExtMOMCAddressType_Type = InetAddressType
_CLMobilityExtMOMCAddressType_Object = MibTableColumn
cLMobilityExtMOMCAddressType = _CLMobilityExtMOMCAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 5, 1, 1),
    _CLMobilityExtMOMCAddressType_Type()
)
cLMobilityExtMOMCAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtMOMCAddressType.setStatus("current")
_CLMobilityExtMOMCAddress_Type = InetAddress
_CLMobilityExtMOMCAddress_Object = MibTableColumn
cLMobilityExtMOMCAddress = _CLMobilityExtMOMCAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 5, 1, 2),
    _CLMobilityExtMOMCAddress_Type()
)
cLMobilityExtMOMCAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtMOMCAddress.setStatus("current")
_CLMobilityExtMOMCMacAddress_Type = MacAddress
_CLMobilityExtMOMCMacAddress_Object = MibTableColumn
cLMobilityExtMOMCMacAddress = _CLMobilityExtMOMCMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 5, 1, 3),
    _CLMobilityExtMOMCMacAddress_Type()
)
cLMobilityExtMOMCMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOMCMacAddress.setStatus("current")


class _CLMobilityExtMOMCLinkStatus_Type(Integer32):
    """Custom type cLMobilityExtMOMCLinkStatus based on Integer32"""
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
        *(("bothdown", 3),
          ("controlpathdown", 2),
          ("datapathdown", 1),
          ("notconfigured", 0),
          ("up", 4))
    )


_CLMobilityExtMOMCLinkStatus_Type.__name__ = "Integer32"
_CLMobilityExtMOMCLinkStatus_Object = MibTableColumn
cLMobilityExtMOMCLinkStatus = _CLMobilityExtMOMCLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 5, 1, 4),
    _CLMobilityExtMOMCLinkStatus_Type()
)
cLMobilityExtMOMCLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOMCLinkStatus.setStatus("current")
_CLMobilityExtMOMCClientCount_Type = Unsigned32
_CLMobilityExtMOMCClientCount_Object = MibTableColumn
cLMobilityExtMOMCClientCount = _CLMobilityExtMOMCClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 5, 1, 5),
    _CLMobilityExtMOMCClientCount_Type()
)
cLMobilityExtMOMCClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOMCClientCount.setStatus("current")
_CLMobilityExtMCClientTable_Object = MibTable
cLMobilityExtMCClientTable = _CLMobilityExtMCClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cLMobilityExtMCClientTable.setStatus("current")
_CLMobilityExtMCClientEntry_Object = MibTableRow
cLMobilityExtMCClientEntry = _CLMobilityExtMCClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1)
)
cLMobilityExtMCClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityExtMCClientEntry.setStatus("current")
_CLMobilityExtMCClientMacAddress_Type = MacAddress
_CLMobilityExtMCClientMacAddress_Object = MibTableColumn
cLMobilityExtMCClientMacAddress = _CLMobilityExtMCClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 1),
    _CLMobilityExtMCClientMacAddress_Type()
)
cLMobilityExtMCClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientMacAddress.setStatus("current")
_CLMobilityExtMCClientAnchorMCPrivateAddressType_Type = InetAddressType
_CLMobilityExtMCClientAnchorMCPrivateAddressType_Object = MibTableColumn
cLMobilityExtMCClientAnchorMCPrivateAddressType = _CLMobilityExtMCClientAnchorMCPrivateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 2),
    _CLMobilityExtMCClientAnchorMCPrivateAddressType_Type()
)
cLMobilityExtMCClientAnchorMCPrivateAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAnchorMCPrivateAddressType.setStatus("current")
_CLMobilityExtMCClientAnchorMCPrivateAddress_Type = InetAddress
_CLMobilityExtMCClientAnchorMCPrivateAddress_Object = MibTableColumn
cLMobilityExtMCClientAnchorMCPrivateAddress = _CLMobilityExtMCClientAnchorMCPrivateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 3),
    _CLMobilityExtMCClientAnchorMCPrivateAddress_Type()
)
cLMobilityExtMCClientAnchorMCPrivateAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAnchorMCPrivateAddress.setStatus("current")
_CLMobilityExtMCClientAssociatedMCAddressType_Type = InetAddressType
_CLMobilityExtMCClientAssociatedMCAddressType_Object = MibTableColumn
cLMobilityExtMCClientAssociatedMCAddressType = _CLMobilityExtMCClientAssociatedMCAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 4),
    _CLMobilityExtMCClientAssociatedMCAddressType_Type()
)
cLMobilityExtMCClientAssociatedMCAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAssociatedMCAddressType.setStatus("current")
_CLMobilityExtMCClientAssociatedMCAddress_Type = InetAddress
_CLMobilityExtMCClientAssociatedMCAddress_Object = MibTableColumn
cLMobilityExtMCClientAssociatedMCAddress = _CLMobilityExtMCClientAssociatedMCAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 5),
    _CLMobilityExtMCClientAssociatedMCAddress_Type()
)
cLMobilityExtMCClientAssociatedMCAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAssociatedMCAddress.setStatus("current")
_CLMobilityExtMCClientAddressType_Type = InetAddressType
_CLMobilityExtMCClientAddressType_Object = MibTableColumn
cLMobilityExtMCClientAddressType = _CLMobilityExtMCClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 6),
    _CLMobilityExtMCClientAddressType_Type()
)
cLMobilityExtMCClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAddressType.setStatus("current")
_CLMobilityExtMCClientAddress_Type = InetAddress
_CLMobilityExtMCClientAddress_Object = MibTableColumn
cLMobilityExtMCClientAddress = _CLMobilityExtMCClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 7),
    _CLMobilityExtMCClientAddress_Type()
)
cLMobilityExtMCClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAddress.setStatus("current")


class _CLMobilityExtMCClientState_Type(Integer32):
    """Custom type cLMobilityExtMCClientState based on Integer32"""
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
        *(("anchor", 3),
          ("foreign", 2),
          ("init", 0),
          ("local", 1))
    )


_CLMobilityExtMCClientState_Type.__name__ = "Integer32"
_CLMobilityExtMCClientState_Object = MibTableColumn
cLMobilityExtMCClientState = _CLMobilityExtMCClientState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 8),
    _CLMobilityExtMCClientState_Type()
)
cLMobilityExtMCClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientState.setStatus("current")
_CLMobilityExtMCClientAssociationTime_Type = DateAndTime
_CLMobilityExtMCClientAssociationTime_Object = MibTableColumn
cLMobilityExtMCClientAssociationTime = _CLMobilityExtMCClientAssociationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 9),
    _CLMobilityExtMCClientAssociationTime_Type()
)
cLMobilityExtMCClientAssociationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAssociationTime.setStatus("deprecated")
_CLMobilityExtMCClientLocalClient_Type = TruthValue
_CLMobilityExtMCClientLocalClient_Object = MibTableColumn
cLMobilityExtMCClientLocalClient = _CLMobilityExtMCClientLocalClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 10),
    _CLMobilityExtMCClientLocalClient_Type()
)
cLMobilityExtMCClientLocalClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientLocalClient.setStatus("current")
_CLMobilityExtMCClientAnchorMCGroupId_Type = Unsigned32
_CLMobilityExtMCClientAnchorMCGroupId_Object = MibTableColumn
cLMobilityExtMCClientAnchorMCGroupId = _CLMobilityExtMCClientAnchorMCGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 11),
    _CLMobilityExtMCClientAnchorMCGroupId_Type()
)
cLMobilityExtMCClientAnchorMCGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAnchorMCGroupId.setStatus("current")
_CLMobilityExtMCClientAssociatedMCGroupId_Type = Unsigned32
_CLMobilityExtMCClientAssociatedMCGroupId_Object = MibTableColumn
cLMobilityExtMCClientAssociatedMCGroupId = _CLMobilityExtMCClientAssociatedMCGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 12),
    _CLMobilityExtMCClientAssociatedMCGroupId_Type()
)
cLMobilityExtMCClientAssociatedMCGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAssociatedMCGroupId.setStatus("current")
_CLMobilityExtMCClientAssociatedMAAddressType_Type = InetAddressType
_CLMobilityExtMCClientAssociatedMAAddressType_Object = MibTableColumn
cLMobilityExtMCClientAssociatedMAAddressType = _CLMobilityExtMCClientAssociatedMAAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 13),
    _CLMobilityExtMCClientAssociatedMAAddressType_Type()
)
cLMobilityExtMCClientAssociatedMAAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAssociatedMAAddressType.setStatus("current")
_CLMobilityExtMCClientAssociatedMAAddress_Type = InetAddress
_CLMobilityExtMCClientAssociatedMAAddress_Object = MibTableColumn
cLMobilityExtMCClientAssociatedMAAddress = _CLMobilityExtMCClientAssociatedMAAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 14),
    _CLMobilityExtMCClientAssociatedMAAddress_Type()
)
cLMobilityExtMCClientAssociatedMAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAssociatedMAAddress.setStatus("current")
_CLMobilityExtMCClientAnchorMAAddressType_Type = InetAddressType
_CLMobilityExtMCClientAnchorMAAddressType_Object = MibTableColumn
cLMobilityExtMCClientAnchorMAAddressType = _CLMobilityExtMCClientAnchorMAAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 15),
    _CLMobilityExtMCClientAnchorMAAddressType_Type()
)
cLMobilityExtMCClientAnchorMAAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAnchorMAAddressType.setStatus("current")
_CLMobilityExtMCClientAnchorMAAddress_Type = InetAddress
_CLMobilityExtMCClientAnchorMAAddress_Object = MibTableColumn
cLMobilityExtMCClientAnchorMAAddress = _CLMobilityExtMCClientAnchorMAAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 16),
    _CLMobilityExtMCClientAnchorMAAddress_Type()
)
cLMobilityExtMCClientAnchorMAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientAnchorMAAddress.setStatus("current")
_CLMobilityExtMCClientUpTime_Type = CiscoAbsZeroBasedCounter64
_CLMobilityExtMCClientUpTime_Object = MibTableColumn
cLMobilityExtMCClientUpTime = _CLMobilityExtMCClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 6, 1, 17),
    _CLMobilityExtMCClientUpTime_Type()
)
cLMobilityExtMCClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCClientUpTime.setStatus("current")
_CLMobilityExtMOClientTable_Object = MibTable
cLMobilityExtMOClientTable = _CLMobilityExtMOClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cLMobilityExtMOClientTable.setStatus("current")
_CLMobilityExtMOClientEntry_Object = MibTableRow
cLMobilityExtMOClientEntry = _CLMobilityExtMOClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1)
)
cLMobilityExtMOClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityExtMOClientEntry.setStatus("current")
_CLMobilityExtMOClientMacAddress_Type = MacAddress
_CLMobilityExtMOClientMacAddress_Object = MibTableColumn
cLMobilityExtMOClientMacAddress = _CLMobilityExtMOClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 1),
    _CLMobilityExtMOClientMacAddress_Type()
)
cLMobilityExtMOClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientMacAddress.setStatus("current")
_CLMobilityExtMOClientAnchorMCPublicAddressType_Type = InetAddressType
_CLMobilityExtMOClientAnchorMCPublicAddressType_Object = MibTableColumn
cLMobilityExtMOClientAnchorMCPublicAddressType = _CLMobilityExtMOClientAnchorMCPublicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 2),
    _CLMobilityExtMOClientAnchorMCPublicAddressType_Type()
)
cLMobilityExtMOClientAnchorMCPublicAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAnchorMCPublicAddressType.setStatus("current")
_CLMobilityExtMOClientAnchorMCPublicAddress_Type = InetAddress
_CLMobilityExtMOClientAnchorMCPublicAddress_Object = MibTableColumn
cLMobilityExtMOClientAnchorMCPublicAddress = _CLMobilityExtMOClientAnchorMCPublicAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 3),
    _CLMobilityExtMOClientAnchorMCPublicAddress_Type()
)
cLMobilityExtMOClientAnchorMCPublicAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAnchorMCPublicAddress.setStatus("current")
_CLMobilityExtMOClientAnchorMCPrivateAddressType_Type = InetAddressType
_CLMobilityExtMOClientAnchorMCPrivateAddressType_Object = MibTableColumn
cLMobilityExtMOClientAnchorMCPrivateAddressType = _CLMobilityExtMOClientAnchorMCPrivateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 4),
    _CLMobilityExtMOClientAnchorMCPrivateAddressType_Type()
)
cLMobilityExtMOClientAnchorMCPrivateAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAnchorMCPrivateAddressType.setStatus("current")
_CLMobilityExtMOClientAnchorMCPrivateAddress_Type = InetAddress
_CLMobilityExtMOClientAnchorMCPrivateAddress_Object = MibTableColumn
cLMobilityExtMOClientAnchorMCPrivateAddress = _CLMobilityExtMOClientAnchorMCPrivateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 5),
    _CLMobilityExtMOClientAnchorMCPrivateAddress_Type()
)
cLMobilityExtMOClientAnchorMCPrivateAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAnchorMCPrivateAddress.setStatus("current")
_CLMobilityExtMOClientAssociatedMCPublicAddressType_Type = InetAddressType
_CLMobilityExtMOClientAssociatedMCPublicAddressType_Object = MibTableColumn
cLMobilityExtMOClientAssociatedMCPublicAddressType = _CLMobilityExtMOClientAssociatedMCPublicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 6),
    _CLMobilityExtMOClientAssociatedMCPublicAddressType_Type()
)
cLMobilityExtMOClientAssociatedMCPublicAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAssociatedMCPublicAddressType.setStatus("current")
_CLMobilityExtMOClientAssociatedMCPublicAddress_Type = InetAddress
_CLMobilityExtMOClientAssociatedMCPublicAddress_Object = MibTableColumn
cLMobilityExtMOClientAssociatedMCPublicAddress = _CLMobilityExtMOClientAssociatedMCPublicAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 7),
    _CLMobilityExtMOClientAssociatedMCPublicAddress_Type()
)
cLMobilityExtMOClientAssociatedMCPublicAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAssociatedMCPublicAddress.setStatus("current")
_CLMobilityExtMOClientAssociatedMCPrivateAddressType_Type = InetAddressType
_CLMobilityExtMOClientAssociatedMCPrivateAddressType_Object = MibTableColumn
cLMobilityExtMOClientAssociatedMCPrivateAddressType = _CLMobilityExtMOClientAssociatedMCPrivateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 8),
    _CLMobilityExtMOClientAssociatedMCPrivateAddressType_Type()
)
cLMobilityExtMOClientAssociatedMCPrivateAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAssociatedMCPrivateAddressType.setStatus("current")
_CLMobilityExtMOClientAssociatedMCPrivateAddress_Type = InetAddress
_CLMobilityExtMOClientAssociatedMCPrivateAddress_Object = MibTableColumn
cLMobilityExtMOClientAssociatedMCPrivateAddress = _CLMobilityExtMOClientAssociatedMCPrivateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 9),
    _CLMobilityExtMOClientAssociatedMCPrivateAddress_Type()
)
cLMobilityExtMOClientAssociatedMCPrivateAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAssociatedMCPrivateAddress.setStatus("current")
_CLMobilityExtMOClientAddressType_Type = InetAddressType
_CLMobilityExtMOClientAddressType_Object = MibTableColumn
cLMobilityExtMOClientAddressType = _CLMobilityExtMOClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 10),
    _CLMobilityExtMOClientAddressType_Type()
)
cLMobilityExtMOClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAddressType.setStatus("current")
_CLMobilityExtMOClientAddress_Type = InetAddress
_CLMobilityExtMOClientAddress_Object = MibTableColumn
cLMobilityExtMOClientAddress = _CLMobilityExtMOClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 11),
    _CLMobilityExtMOClientAddress_Type()
)
cLMobilityExtMOClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAddress.setStatus("current")
_CLMobilityExtMOClientLocalTime_Type = DateAndTime
_CLMobilityExtMOClientLocalTime_Object = MibTableColumn
cLMobilityExtMOClientLocalTime = _CLMobilityExtMOClientLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 12),
    _CLMobilityExtMOClientLocalTime_Type()
)
cLMobilityExtMOClientLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientLocalTime.setStatus("current")
_CLMobilityExtMOClientAssociationTime_Type = DateAndTime
_CLMobilityExtMOClientAssociationTime_Object = MibTableColumn
cLMobilityExtMOClientAssociationTime = _CLMobilityExtMOClientAssociationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 13),
    _CLMobilityExtMOClientAssociationTime_Type()
)
cLMobilityExtMOClientAssociationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAssociationTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientAssociationTime.setUnits("seconds")
_CLMobilityExtMOClientUpTime_Type = CiscoAbsZeroBasedCounter64
_CLMobilityExtMOClientUpTime_Object = MibTableColumn
cLMobilityExtMOClientUpTime = _CLMobilityExtMOClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 7, 1, 14),
    _CLMobilityExtMOClientUpTime_Type()
)
cLMobilityExtMOClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMOClientUpTime.setStatus("current")
_CLMobilityExtApMgrTable_Object = MibTable
cLMobilityExtApMgrTable = _CLMobilityExtApMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cLMobilityExtApMgrTable.setStatus("current")
_CLMobilityExtApMgrEntry_Object = MibTableRow
cLMobilityExtApMgrEntry = _CLMobilityExtApMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1)
)
cLMobilityExtApMgrEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrName"),
)
if mibBuilder.loadTexts:
    cLMobilityExtApMgrEntry.setStatus("current")
_CLMobilityExtApMgrName_Type = SnmpAdminString
_CLMobilityExtApMgrName_Object = MibTableColumn
cLMobilityExtApMgrName = _CLMobilityExtApMgrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1, 1),
    _CLMobilityExtApMgrName_Type()
)
cLMobilityExtApMgrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtApMgrName.setStatus("current")
_CLMobilityExtApMgrAddressType_Type = InetAddressType
_CLMobilityExtApMgrAddressType_Object = MibTableColumn
cLMobilityExtApMgrAddressType = _CLMobilityExtApMgrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1, 2),
    _CLMobilityExtApMgrAddressType_Type()
)
cLMobilityExtApMgrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtApMgrAddressType.setStatus("current")
_CLMobilityExtApMgrAddress_Type = InetAddress
_CLMobilityExtApMgrAddress_Object = MibTableColumn
cLMobilityExtApMgrAddress = _CLMobilityExtApMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1, 3),
    _CLMobilityExtApMgrAddress_Type()
)
cLMobilityExtApMgrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtApMgrAddress.setStatus("current")
_CLMobilityExtApMgrNetmaskType_Type = InetAddressType
_CLMobilityExtApMgrNetmaskType_Object = MibTableColumn
cLMobilityExtApMgrNetmaskType = _CLMobilityExtApMgrNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1, 4),
    _CLMobilityExtApMgrNetmaskType_Type()
)
cLMobilityExtApMgrNetmaskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtApMgrNetmaskType.setStatus("current")
_CLMobilityExtApMgrNetmask_Type = InetAddress
_CLMobilityExtApMgrNetmask_Object = MibTableColumn
cLMobilityExtApMgrNetmask = _CLMobilityExtApMgrNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1, 5),
    _CLMobilityExtApMgrNetmask_Type()
)
cLMobilityExtApMgrNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtApMgrNetmask.setStatus("current")
_CLMobilityExtApMgrMacAddress_Type = MacAddress
_CLMobilityExtApMgrMacAddress_Object = MibTableColumn
cLMobilityExtApMgrMacAddress = _CLMobilityExtApMgrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1, 6),
    _CLMobilityExtApMgrMacAddress_Type()
)
cLMobilityExtApMgrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtApMgrMacAddress.setStatus("current")
_CLMobilityExtApMgrVlanId_Type = Unsigned32
_CLMobilityExtApMgrVlanId_Object = MibTableColumn
cLMobilityExtApMgrVlanId = _CLMobilityExtApMgrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1, 7),
    _CLMobilityExtApMgrVlanId_Type()
)
cLMobilityExtApMgrVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtApMgrVlanId.setStatus("current")


class _CLMobilityExtApMgrInterfaceType_Type(Integer32):
    """Custom type cLMobilityExtApMgrInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 2),
          ("management", 1))
    )


_CLMobilityExtApMgrInterfaceType_Type.__name__ = "Integer32"
_CLMobilityExtApMgrInterfaceType_Object = MibTableColumn
cLMobilityExtApMgrInterfaceType = _CLMobilityExtApMgrInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1, 8),
    _CLMobilityExtApMgrInterfaceType_Type()
)
cLMobilityExtApMgrInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtApMgrInterfaceType.setStatus("current")
_CLMobilityExtApMgrRowStatus_Type = RowStatus
_CLMobilityExtApMgrRowStatus_Object = MibTableColumn
cLMobilityExtApMgrRowStatus = _CLMobilityExtApMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 8, 1, 9),
    _CLMobilityExtApMgrRowStatus_Type()
)
cLMobilityExtApMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtApMgrRowStatus.setStatus("current")
_CLMobilityExtForeignWlcMapTable_Object = MibTable
cLMobilityExtForeignWlcMapTable = _CLMobilityExtForeignWlcMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cLMobilityExtForeignWlcMapTable.setStatus("current")
_CLMobilityExtForeignWlcMapEntry_Object = MibTableRow
cLMobilityExtForeignWlcMapEntry = _CLMobilityExtForeignWlcMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 9, 1)
)
cLMobilityExtForeignWlcMapEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtForeignWlcAddressType"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtForeignWlcAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityExtForeignWlcMapEntry.setStatus("current")
_CLMobilityExtForeignWlcAddressType_Type = InetAddressType
_CLMobilityExtForeignWlcAddressType_Object = MibTableColumn
cLMobilityExtForeignWlcAddressType = _CLMobilityExtForeignWlcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 9, 1, 1),
    _CLMobilityExtForeignWlcAddressType_Type()
)
cLMobilityExtForeignWlcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtForeignWlcAddressType.setStatus("current")
_CLMobilityExtForeignWlcAddress_Type = InetAddress
_CLMobilityExtForeignWlcAddress_Object = MibTableColumn
cLMobilityExtForeignWlcAddress = _CLMobilityExtForeignWlcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 9, 1, 2),
    _CLMobilityExtForeignWlcAddress_Type()
)
cLMobilityExtForeignWlcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtForeignWlcAddress.setStatus("current")
_CLMobilityExtForeignWlcMapIf_Type = SnmpAdminString
_CLMobilityExtForeignWlcMapIf_Object = MibTableColumn
cLMobilityExtForeignWlcMapIf = _CLMobilityExtForeignWlcMapIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 9, 1, 3),
    _CLMobilityExtForeignWlcMapIf_Type()
)
cLMobilityExtForeignWlcMapIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtForeignWlcMapIf.setStatus("current")
_CLMobilityExtForeignWlcMapRowStatus_Type = RowStatus
_CLMobilityExtForeignWlcMapRowStatus_Object = MibTableColumn
cLMobilityExtForeignWlcMapRowStatus = _CLMobilityExtForeignWlcMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 9, 1, 4),
    _CLMobilityExtForeignWlcMapRowStatus_Type()
)
cLMobilityExtForeignWlcMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityExtForeignWlcMapRowStatus.setStatus("current")
_CLMobilityExtGroupTable_Object = MibTable
cLMobilityExtGroupTable = _CLMobilityExtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cLMobilityExtGroupTable.setStatus("current")
_CLMobilityExtGroupEntry_Object = MibTableRow
cLMobilityExtGroupEntry = _CLMobilityExtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 10, 1)
)
cLMobilityExtGroupEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupName"),
)
if mibBuilder.loadTexts:
    cLMobilityExtGroupEntry.setStatus("current")
_CLMobilityExtGroupName_Type = SnmpAdminString
_CLMobilityExtGroupName_Object = MibTableColumn
cLMobilityExtGroupName = _CLMobilityExtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 10, 1, 1),
    _CLMobilityExtGroupName_Type()
)
cLMobilityExtGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtGroupName.setStatus("current")
_CLMobilityExtGroupMulticastAddressType_Type = InetAddressType
_CLMobilityExtGroupMulticastAddressType_Object = MibTableColumn
cLMobilityExtGroupMulticastAddressType = _CLMobilityExtGroupMulticastAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 10, 1, 2),
    _CLMobilityExtGroupMulticastAddressType_Type()
)
cLMobilityExtGroupMulticastAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMulticastAddressType.setStatus("current")
_CLMobilityExtGroupMulticastAddress_Type = InetAddress
_CLMobilityExtGroupMulticastAddress_Object = MibTableColumn
cLMobilityExtGroupMulticastAddress = _CLMobilityExtGroupMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 10, 1, 3),
    _CLMobilityExtGroupMulticastAddress_Type()
)
cLMobilityExtGroupMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityExtGroupMulticastAddress.setStatus("current")
_CLMobilityExtMAPeerTable_Object = MibTable
cLMobilityExtMAPeerTable = _CLMobilityExtMAPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cLMobilityExtMAPeerTable.setStatus("current")
_CLMobilityExtMAPeerEntry_Object = MibTableRow
cLMobilityExtMAPeerEntry = _CLMobilityExtMAPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 11, 1)
)
cLMobilityExtMAPeerEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAPeerPrivateAddressType"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAPeerPrivateAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityExtMAPeerEntry.setStatus("current")
_CLMobilityExtMAPeerPrivateAddressType_Type = InetAddressType
_CLMobilityExtMAPeerPrivateAddressType_Object = MibTableColumn
cLMobilityExtMAPeerPrivateAddressType = _CLMobilityExtMAPeerPrivateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 11, 1, 1),
    _CLMobilityExtMAPeerPrivateAddressType_Type()
)
cLMobilityExtMAPeerPrivateAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtMAPeerPrivateAddressType.setStatus("current")
_CLMobilityExtMAPeerPrivateAddress_Type = InetAddress
_CLMobilityExtMAPeerPrivateAddress_Object = MibTableColumn
cLMobilityExtMAPeerPrivateAddress = _CLMobilityExtMAPeerPrivateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 11, 1, 2),
    _CLMobilityExtMAPeerPrivateAddress_Type()
)
cLMobilityExtMAPeerPrivateAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtMAPeerPrivateAddress.setStatus("current")
_CLMobilityExtMAPeerPublicAddressType_Type = InetAddressType
_CLMobilityExtMAPeerPublicAddressType_Object = MibTableColumn
cLMobilityExtMAPeerPublicAddressType = _CLMobilityExtMAPeerPublicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 11, 1, 3),
    _CLMobilityExtMAPeerPublicAddressType_Type()
)
cLMobilityExtMAPeerPublicAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMAPeerPublicAddressType.setStatus("current")
_CLMobilityExtMAPeerPublicAddress_Type = InetAddress
_CLMobilityExtMAPeerPublicAddress_Object = MibTableColumn
cLMobilityExtMAPeerPublicAddress = _CLMobilityExtMAPeerPublicAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 11, 1, 4),
    _CLMobilityExtMAPeerPublicAddress_Type()
)
cLMobilityExtMAPeerPublicAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMAPeerPublicAddress.setStatus("current")


class _CLMobilityExtMAPeerLinkStatus_Type(Integer32):
    """Custom type cLMobilityExtMAPeerLinkStatus based on Integer32"""
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
        *(("bothdown", 3),
          ("controlpathdown", 2),
          ("datapathdown", 1),
          ("notconfigured", 0),
          ("up", 4))
    )


_CLMobilityExtMAPeerLinkStatus_Type.__name__ = "Integer32"
_CLMobilityExtMAPeerLinkStatus_Object = MibTableColumn
cLMobilityExtMAPeerLinkStatus = _CLMobilityExtMAPeerLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 11, 1, 5),
    _CLMobilityExtMAPeerLinkStatus_Type()
)
cLMobilityExtMAPeerLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMAPeerLinkStatus.setStatus("current")
_CLMobilityExtMCMAStatisticsTable_Object = MibTable
cLMobilityExtMCMAStatisticsTable = _CLMobilityExtMCMAStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cLMobilityExtMCMAStatisticsTable.setStatus("current")
_CLMobilityExtMCMAStatisticsEntry_Object = MibTableRow
cLMobilityExtMCMAStatisticsEntry = _CLMobilityExtMCMAStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 12, 1)
)
cLMobilityExtMCMAStatisticsEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMAPrivateAddressType"),
    (0, "CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMAPrivateAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityExtMCMAStatisticsEntry.setStatus("current")
_CLMobilityExtMCMAPrivateAddressType_Type = InetAddressType
_CLMobilityExtMCMAPrivateAddressType_Object = MibTableColumn
cLMobilityExtMCMAPrivateAddressType = _CLMobilityExtMCMAPrivateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 12, 1, 1),
    _CLMobilityExtMCMAPrivateAddressType_Type()
)
cLMobilityExtMCMAPrivateAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtMCMAPrivateAddressType.setStatus("current")
_CLMobilityExtMCMAPrivateAddress_Type = InetAddress
_CLMobilityExtMCMAPrivateAddress_Object = MibTableColumn
cLMobilityExtMCMAPrivateAddress = _CLMobilityExtMCMAPrivateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 12, 1, 2),
    _CLMobilityExtMCMAPrivateAddress_Type()
)
cLMobilityExtMCMAPrivateAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityExtMCMAPrivateAddress.setStatus("current")
_CLMobilityExtMCMAClientCount_Type = Unsigned32
_CLMobilityExtMCMAClientCount_Object = MibTableColumn
cLMobilityExtMCMAClientCount = _CLMobilityExtMCMAClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 2, 12, 1, 3),
    _CLMobilityExtMCMAClientCount_Type()
)
cLMobilityExtMCMAClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityExtMCMAClientCount.setStatus("current")
_CiscoLwappMobilityExtNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtNotifObjects = _CiscoLwappMobilityExtNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 3)
)
_CLMobilityExtNotifyObjectSourceIPAddressType_Type = InetAddressType
_CLMobilityExtNotifyObjectSourceIPAddressType_Object = MibScalar
cLMobilityExtNotifyObjectSourceIPAddressType = _CLMobilityExtNotifyObjectSourceIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 3, 1),
    _CLMobilityExtNotifyObjectSourceIPAddressType_Type()
)
cLMobilityExtNotifyObjectSourceIPAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityExtNotifyObjectSourceIPAddressType.setStatus("current")
_CLMobilityExtNotifyObjectSourceIPAddress_Type = InetAddress
_CLMobilityExtNotifyObjectSourceIPAddress_Object = MibScalar
cLMobilityExtNotifyObjectSourceIPAddress = _CLMobilityExtNotifyObjectSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 3, 2),
    _CLMobilityExtNotifyObjectSourceIPAddress_Type()
)
cLMobilityExtNotifyObjectSourceIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityExtNotifyObjectSourceIPAddress.setStatus("current")


class _CLMobilityExtNotifyObjectSourceType_Type(Integer32):
    """Custom type cLMobilityExtNotifyObjectSourceType based on Integer32"""
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
        *(("mobilityAgent", 1),
          ("mobilityController", 2),
          ("mobilityOracle", 3),
          ("unknown", 0))
    )


_CLMobilityExtNotifyObjectSourceType_Type.__name__ = "Integer32"
_CLMobilityExtNotifyObjectSourceType_Object = MibScalar
cLMobilityExtNotifyObjectSourceType = _CLMobilityExtNotifyObjectSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 3, 3),
    _CLMobilityExtNotifyObjectSourceType_Type()
)
cLMobilityExtNotifyObjectSourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityExtNotifyObjectSourceType.setStatus("current")


class _CLMobilityExtNotifyObjectDestinationType_Type(Integer32):
    """Custom type cLMobilityExtNotifyObjectDestinationType based on Integer32"""
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
        *(("mobilityAgent", 1),
          ("mobilityController", 2),
          ("mobilityOracle", 3),
          ("unknown", 0))
    )


_CLMobilityExtNotifyObjectDestinationType_Type.__name__ = "Integer32"
_CLMobilityExtNotifyObjectDestinationType_Object = MibScalar
cLMobilityExtNotifyObjectDestinationType = _CLMobilityExtNotifyObjectDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 3, 4),
    _CLMobilityExtNotifyObjectDestinationType_Type()
)
cLMobilityExtNotifyObjectDestinationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityExtNotifyObjectDestinationType.setStatus("current")
_CiscoLwappMobilityExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtMIBConform = _CiscoLwappMobilityExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2)
)
_CiscoLwappMobilityExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtMIBCompliances = _CiscoLwappMobilityExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1)
)
_CiscoLwappMobilityExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityExtMIBGroups = _CiscoLwappMobilityExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2)
)

# Managed Objects groups

cLMobilityExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2, 1)
)
cLMobilityExtConfigGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMOEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMOAdminEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCAdminEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMulticastMode"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCKeepAliveCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCKeepAliveInterval"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCDscpValue"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMOPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMOPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCApCountLicensesInUse"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCOwnGroupMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCOwnGroupMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMobilityGroupName"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrNetmaskType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrNetmask"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrMacAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrVlanId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrName"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrInterfaceType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNewArchitectureEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNewArchitectureAdminEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMCPrivateAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMCPrivateAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMCGroupId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMCGroupId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMAAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMAAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMAAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMAAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgGroupId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgBridgeDomainId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMulticastMode"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberGroupName"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberMacAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberHashKey"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtAnchorStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtAnchorRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOMCMacAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOMCLinkStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOMCClientCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMCAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMCAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientState"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociationTime"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientLocalClient"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAnchorMCPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAnchorMCPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAnchorMCPrivateAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAnchorMCPrivateAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAssociatedMCPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAssociatedMCPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAssociatedMCPrivateAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAssociatedMCPrivateAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientLocalTime"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAssociationTime"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrNetmaskType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrNetmask"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrMacAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrVlanId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrInterfaceType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtForeignWlcMapIf"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtForeignWlcMapRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAPeerPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAPeerPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAPeerLinkStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMAClientCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAMCPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAMCPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAMCPrivateAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAMCPrivateAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAToMCLinkStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMASpgPeerCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMASpgName"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAOwnMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAOwnMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAKeepAliveCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAKeepAliveInterval"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMADscpValue"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCReceivedTotal"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCReceivedDrops"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCProtocolReceiveErrors"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCProtocolTransmitErrors"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCStateErrors"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCProtocolRetransmitted"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffRequestsReceived"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffCmplReceived"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffClientDeleteReceived"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffRequestsTransmitted"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffCmplTransmitted"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffClientDeleteTransmitted"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCTotalClientCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCWgbCount"))
)
if mibBuilder.loadTexts:
    cLMobilityExtConfigGroup.setStatus("deprecated")

ciscoLwappMobilityExtNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2, 2)
)
ciscoLwappMobilityExtNotifyObjectsGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectDestinationType"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityExtNotifyObjectsGroup.setStatus("current")

cLMobilityExtConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2, 4)
)
cLMobilityExtConfigGroupRev1.setObjects(
      *(("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMOEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMOAdminEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCAdminEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMulticastMode"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCKeepAliveCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCKeepAliveInterval"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCDscpValue"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMOPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMOPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCApCountLicensesInUse"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCOwnGroupMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCOwnGroupMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMobilityGroupName"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrNetmaskType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrNetmask"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrMacAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrVlanId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrName"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMgrInterfaceType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNewArchitectureEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNewArchitectureAdminEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMCPrivateAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMCPrivateAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMCGroupId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMCGroupId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMAAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMAAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMAAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAnchorMAAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgGroupId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgBridgeDomainId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMulticastMode"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtSpgMemberRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberGroupName"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberMacAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberHashKey"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMemberRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtAnchorStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtAnchorRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOMCMacAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOMCLinkStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOMCClientCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMCAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAssociatedMCAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientState"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientLocalClient"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAnchorMCPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAnchorMCPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAnchorMCPrivateAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAnchorMCPrivateAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAssociatedMCPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAssociatedMCPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAssociatedMCPrivateAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAssociatedMCPrivateAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientLocalTime"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrNetmaskType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrNetmask"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrMacAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrVlanId"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrInterfaceType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtApMgrRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtForeignWlcMapIf"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtForeignWlcMapRowStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtGroupMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAPeerPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAPeerPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAPeerLinkStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCMAClientCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAMCPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAMCPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAMCPrivateAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAMCPrivateAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAToMCLinkStatus"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMASpgPeerCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMASpgName"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAOwnMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAOwnMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAKeepAliveCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMAKeepAliveInterval"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMADscpValue"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCReceivedTotal"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCReceivedDrops"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCProtocolReceiveErrors"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCProtocolTransmitErrors"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCStateErrors"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCProtocolRetransmitted"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffRequestsReceived"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffCmplReceived"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffClientDeleteReceived"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffRequestsTransmitted"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffCmplTransmitted"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCHandoffClientDeleteTransmitted"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCTotalClientCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCWgbCount"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMOClientUpTime"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtMCClientUpTime"))
)
if mibBuilder.loadTexts:
    cLMobilityExtConfigGroupRev1.setStatus("current")


# Notification objects

ciscoLwappMobilityControlPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 0, 1)
)
ciscoLwappMobilityControlPathDown.setObjects(
      *(("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectDestinationType"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityControlPathDown.setStatus(
        "current"
    )

ciscoLwappMobilityControlPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 0, 2)
)
ciscoLwappMobilityControlPathUp.setObjects(
      *(("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectDestinationType"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityControlPathUp.setStatus(
        "current"
    )

ciscoLwappMobilityDataPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 0, 3)
)
ciscoLwappMobilityDataPathDown.setObjects(
      *(("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectDestinationType"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityDataPathDown.setStatus(
        "current"
    )

ciscoLwappMobilityDataPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 0, 4)
)
ciscoLwappMobilityDataPathUp.setObjects(
      *(("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceIPAddress"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectSourceType"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "cLMobilityExtNotifyObjectDestinationType"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityDataPathUp.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappMobilityExtNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2, 3)
)
ciscoLwappMobilityExtNotifsGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-EXT-MIB", "ciscoLwappMobilityControlPathDown"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "ciscoLwappMobilityControlPathUp"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "ciscoLwappMobilityDataPathDown"),
        ("CISCO-LWAPP-MOBILITY-EXT-MIB", "ciscoLwappMobilityDataPathUp"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityExtNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappMobilityExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappMobilityExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityExtMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MOBILITY-EXT-MIB",
    **{"CiscoAbsZeroBasedCounter64": CiscoAbsZeroBasedCounter64,
       "ciscoLwappMobilityExtMIB": ciscoLwappMobilityExtMIB,
       "ciscoLwappMobilityExtMIBNotifs": ciscoLwappMobilityExtMIBNotifs,
       "ciscoLwappMobilityControlPathDown": ciscoLwappMobilityControlPathDown,
       "ciscoLwappMobilityControlPathUp": ciscoLwappMobilityControlPathUp,
       "ciscoLwappMobilityDataPathDown": ciscoLwappMobilityDataPathDown,
       "ciscoLwappMobilityDataPathUp": ciscoLwappMobilityDataPathUp,
       "ciscoLwappMobilityExtMIBObjects": ciscoLwappMobilityExtMIBObjects,
       "ciscoLwappMobilityExtGlobalObjects": ciscoLwappMobilityExtGlobalObjects,
       "ciscoLwappMobilityExtMCGlobalObjects": ciscoLwappMobilityExtMCGlobalObjects,
       "cLMobilityExtMCMOEnableStatus": cLMobilityExtMCMOEnableStatus,
       "cLMobilityExtMCMOAdminEnableStatus": cLMobilityExtMCMOAdminEnableStatus,
       "cLMobilityExtMCEnableStatus": cLMobilityExtMCEnableStatus,
       "cLMobilityExtMCAdminEnableStatus": cLMobilityExtMCAdminEnableStatus,
       "cLMobilityExtMCMulticastMode": cLMobilityExtMCMulticastMode,
       "cLMobilityExtMCKeepAliveCount": cLMobilityExtMCKeepAliveCount,
       "cLMobilityExtMCKeepAliveInterval": cLMobilityExtMCKeepAliveInterval,
       "cLMobilityExtMCDscpValue": cLMobilityExtMCDscpValue,
       "cLMobilityExtMCMOPublicAddressType": cLMobilityExtMCMOPublicAddressType,
       "cLMobilityExtMCMOPublicAddress": cLMobilityExtMCMOPublicAddress,
       "cLMobilityExtMCApCountLicensesInUse": cLMobilityExtMCApCountLicensesInUse,
       "cLMobilityExtMCOwnGroupMulticastAddressType": cLMobilityExtMCOwnGroupMulticastAddressType,
       "cLMobilityExtMCOwnGroupMulticastAddress": cLMobilityExtMCOwnGroupMulticastAddress,
       "cLMobilityExtMCMobilityGroupName": cLMobilityExtMCMobilityGroupName,
       "ciscoLwappMobilityExtMCMAGlobalObjects": ciscoLwappMobilityExtMCMAGlobalObjects,
       "cLMobilityExtMgrAddressType": cLMobilityExtMgrAddressType,
       "cLMobilityExtMgrAddress": cLMobilityExtMgrAddress,
       "cLMobilityExtMgrNetmaskType": cLMobilityExtMgrNetmaskType,
       "cLMobilityExtMgrNetmask": cLMobilityExtMgrNetmask,
       "cLMobilityExtMgrMacAddress": cLMobilityExtMgrMacAddress,
       "cLMobilityExtMgrVlanId": cLMobilityExtMgrVlanId,
       "cLMobilityExtMgrName": cLMobilityExtMgrName,
       "cLMobilityExtMgrInterfaceType": cLMobilityExtMgrInterfaceType,
       "cLMobilityExtNewArchitectureEnableStatus": cLMobilityExtNewArchitectureEnableStatus,
       "cLMobilityExtNewArchitectureAdminEnableStatus": cLMobilityExtNewArchitectureAdminEnableStatus,
       "ciscoLwappMobilityExtMAGlobalObjects": ciscoLwappMobilityExtMAGlobalObjects,
       "cLMobilityExtMAMCPublicAddressType": cLMobilityExtMAMCPublicAddressType,
       "cLMobilityExtMAMCPublicAddress": cLMobilityExtMAMCPublicAddress,
       "cLMobilityExtMAMCPrivateAddressType": cLMobilityExtMAMCPrivateAddressType,
       "cLMobilityExtMAMCPrivateAddress": cLMobilityExtMAMCPrivateAddress,
       "cLMobilityExtMAToMCLinkStatus": cLMobilityExtMAToMCLinkStatus,
       "cLMobilityExtMASpgPeerCount": cLMobilityExtMASpgPeerCount,
       "cLMobilityExtMASpgName": cLMobilityExtMASpgName,
       "cLMobilityExtMAOwnMulticastAddressType": cLMobilityExtMAOwnMulticastAddressType,
       "cLMobilityExtMAOwnMulticastAddress": cLMobilityExtMAOwnMulticastAddress,
       "cLMobilityExtMAKeepAliveCount": cLMobilityExtMAKeepAliveCount,
       "cLMobilityExtMAKeepAliveInterval": cLMobilityExtMAKeepAliveInterval,
       "cLMobilityExtMADscpValue": cLMobilityExtMADscpValue,
       "ciscoLwappMobilityExtMCStats": ciscoLwappMobilityExtMCStats,
       "cLMobilityExtMCReceivedTotal": cLMobilityExtMCReceivedTotal,
       "cLMobilityExtMCReceivedDrops": cLMobilityExtMCReceivedDrops,
       "cLMobilityExtMCProtocolReceiveErrors": cLMobilityExtMCProtocolReceiveErrors,
       "cLMobilityExtMCProtocolTransmitErrors": cLMobilityExtMCProtocolTransmitErrors,
       "cLMobilityExtMCStateErrors": cLMobilityExtMCStateErrors,
       "cLMobilityExtMCProtocolRetransmitted": cLMobilityExtMCProtocolRetransmitted,
       "cLMobilityExtMCHandoffRequestsReceived": cLMobilityExtMCHandoffRequestsReceived,
       "cLMobilityExtMCHandoffCmplReceived": cLMobilityExtMCHandoffCmplReceived,
       "cLMobilityExtMCHandoffClientDeleteReceived": cLMobilityExtMCHandoffClientDeleteReceived,
       "cLMobilityExtMCHandoffRequestsTransmitted": cLMobilityExtMCHandoffRequestsTransmitted,
       "cLMobilityExtMCHandoffCmplTransmitted": cLMobilityExtMCHandoffCmplTransmitted,
       "cLMobilityExtMCHandoffClientDeleteTransmitted": cLMobilityExtMCHandoffClientDeleteTransmitted,
       "cLMobilityExtMCTotalClientCount": cLMobilityExtMCTotalClientCount,
       "cLMobilityExtMCWgbCount": cLMobilityExtMCWgbCount,
       "ciscoLwappMobilityExtTableObjects": ciscoLwappMobilityExtTableObjects,
       "cLMobilityExtSpgTable": cLMobilityExtSpgTable,
       "cLMobilityExtSpgEntry": cLMobilityExtSpgEntry,
       "cLMobilityExtSpgGroupName": cLMobilityExtSpgGroupName,
       "cLMobilityExtSpgGroupId": cLMobilityExtSpgGroupId,
       "cLMobilityExtSpgBridgeDomainId": cLMobilityExtSpgBridgeDomainId,
       "cLMobilityExtSpgMemberCount": cLMobilityExtSpgMemberCount,
       "cLMobilityExtSpgMulticastAddressType": cLMobilityExtSpgMulticastAddressType,
       "cLMobilityExtSpgMulticastAddress": cLMobilityExtSpgMulticastAddress,
       "cLMobilityExtSpgMulticastMode": cLMobilityExtSpgMulticastMode,
       "cLMobilityExtSpgRowStatus": cLMobilityExtSpgRowStatus,
       "cLMobilityExtSpgMemberTable": cLMobilityExtSpgMemberTable,
       "cLMobilityExtSpgMemberEntry": cLMobilityExtSpgMemberEntry,
       "cLMobilityExtSpgMemberPrivateAddressType": cLMobilityExtSpgMemberPrivateAddressType,
       "cLMobilityExtSpgMemberPrivateAddress": cLMobilityExtSpgMemberPrivateAddress,
       "cLMobilityExtSpgMemberStatus": cLMobilityExtSpgMemberStatus,
       "cLMobilityExtSpgMemberPublicAddressType": cLMobilityExtSpgMemberPublicAddressType,
       "cLMobilityExtSpgMemberPublicAddress": cLMobilityExtSpgMemberPublicAddress,
       "cLMobilityExtSpgMemberRowStatus": cLMobilityExtSpgMemberRowStatus,
       "cLMobilityExtGroupMemberTable": cLMobilityExtGroupMemberTable,
       "cLMobilityExtGroupMemberEntry": cLMobilityExtGroupMemberEntry,
       "cLMobilityExtGroupMemberPrivateAddressType": cLMobilityExtGroupMemberPrivateAddressType,
       "cLMobilityExtGroupMemberPrivateAddress": cLMobilityExtGroupMemberPrivateAddress,
       "cLMobilityExtGroupMemberGroupName": cLMobilityExtGroupMemberGroupName,
       "cLMobilityExtGroupMemberPublicAddressType": cLMobilityExtGroupMemberPublicAddressType,
       "cLMobilityExtGroupMemberPublicAddress": cLMobilityExtGroupMemberPublicAddress,
       "cLMobilityExtGroupMemberStatus": cLMobilityExtGroupMemberStatus,
       "cLMobilityExtGroupMemberMacAddress": cLMobilityExtGroupMemberMacAddress,
       "cLMobilityExtGroupMemberMulticastAddressType": cLMobilityExtGroupMemberMulticastAddressType,
       "cLMobilityExtGroupMemberMulticastAddress": cLMobilityExtGroupMemberMulticastAddress,
       "cLMobilityExtGroupMemberHashKey": cLMobilityExtGroupMemberHashKey,
       "cLMobilityExtGroupMemberRowStatus": cLMobilityExtGroupMemberRowStatus,
       "cLMobilityExtAnchorTable": cLMobilityExtAnchorTable,
       "cLMobilityExtAnchorEntry": cLMobilityExtAnchorEntry,
       "cLMobilityExtAnchorAssociatedMCAddressType": cLMobilityExtAnchorAssociatedMCAddressType,
       "cLMobilityExtAnchorAssociatedMCAddress": cLMobilityExtAnchorAssociatedMCAddress,
       "cLMobilityExtAnchorStatus": cLMobilityExtAnchorStatus,
       "cLMobilityExtAnchorRowStatus": cLMobilityExtAnchorRowStatus,
       "cLMobilityExtMOMCTable": cLMobilityExtMOMCTable,
       "cLMobilityExtMOMCEntry": cLMobilityExtMOMCEntry,
       "cLMobilityExtMOMCAddressType": cLMobilityExtMOMCAddressType,
       "cLMobilityExtMOMCAddress": cLMobilityExtMOMCAddress,
       "cLMobilityExtMOMCMacAddress": cLMobilityExtMOMCMacAddress,
       "cLMobilityExtMOMCLinkStatus": cLMobilityExtMOMCLinkStatus,
       "cLMobilityExtMOMCClientCount": cLMobilityExtMOMCClientCount,
       "cLMobilityExtMCClientTable": cLMobilityExtMCClientTable,
       "cLMobilityExtMCClientEntry": cLMobilityExtMCClientEntry,
       "cLMobilityExtMCClientMacAddress": cLMobilityExtMCClientMacAddress,
       "cLMobilityExtMCClientAnchorMCPrivateAddressType": cLMobilityExtMCClientAnchorMCPrivateAddressType,
       "cLMobilityExtMCClientAnchorMCPrivateAddress": cLMobilityExtMCClientAnchorMCPrivateAddress,
       "cLMobilityExtMCClientAssociatedMCAddressType": cLMobilityExtMCClientAssociatedMCAddressType,
       "cLMobilityExtMCClientAssociatedMCAddress": cLMobilityExtMCClientAssociatedMCAddress,
       "cLMobilityExtMCClientAddressType": cLMobilityExtMCClientAddressType,
       "cLMobilityExtMCClientAddress": cLMobilityExtMCClientAddress,
       "cLMobilityExtMCClientState": cLMobilityExtMCClientState,
       "cLMobilityExtMCClientAssociationTime": cLMobilityExtMCClientAssociationTime,
       "cLMobilityExtMCClientLocalClient": cLMobilityExtMCClientLocalClient,
       "cLMobilityExtMCClientAnchorMCGroupId": cLMobilityExtMCClientAnchorMCGroupId,
       "cLMobilityExtMCClientAssociatedMCGroupId": cLMobilityExtMCClientAssociatedMCGroupId,
       "cLMobilityExtMCClientAssociatedMAAddressType": cLMobilityExtMCClientAssociatedMAAddressType,
       "cLMobilityExtMCClientAssociatedMAAddress": cLMobilityExtMCClientAssociatedMAAddress,
       "cLMobilityExtMCClientAnchorMAAddressType": cLMobilityExtMCClientAnchorMAAddressType,
       "cLMobilityExtMCClientAnchorMAAddress": cLMobilityExtMCClientAnchorMAAddress,
       "cLMobilityExtMCClientUpTime": cLMobilityExtMCClientUpTime,
       "cLMobilityExtMOClientTable": cLMobilityExtMOClientTable,
       "cLMobilityExtMOClientEntry": cLMobilityExtMOClientEntry,
       "cLMobilityExtMOClientMacAddress": cLMobilityExtMOClientMacAddress,
       "cLMobilityExtMOClientAnchorMCPublicAddressType": cLMobilityExtMOClientAnchorMCPublicAddressType,
       "cLMobilityExtMOClientAnchorMCPublicAddress": cLMobilityExtMOClientAnchorMCPublicAddress,
       "cLMobilityExtMOClientAnchorMCPrivateAddressType": cLMobilityExtMOClientAnchorMCPrivateAddressType,
       "cLMobilityExtMOClientAnchorMCPrivateAddress": cLMobilityExtMOClientAnchorMCPrivateAddress,
       "cLMobilityExtMOClientAssociatedMCPublicAddressType": cLMobilityExtMOClientAssociatedMCPublicAddressType,
       "cLMobilityExtMOClientAssociatedMCPublicAddress": cLMobilityExtMOClientAssociatedMCPublicAddress,
       "cLMobilityExtMOClientAssociatedMCPrivateAddressType": cLMobilityExtMOClientAssociatedMCPrivateAddressType,
       "cLMobilityExtMOClientAssociatedMCPrivateAddress": cLMobilityExtMOClientAssociatedMCPrivateAddress,
       "cLMobilityExtMOClientAddressType": cLMobilityExtMOClientAddressType,
       "cLMobilityExtMOClientAddress": cLMobilityExtMOClientAddress,
       "cLMobilityExtMOClientLocalTime": cLMobilityExtMOClientLocalTime,
       "cLMobilityExtMOClientAssociationTime": cLMobilityExtMOClientAssociationTime,
       "cLMobilityExtMOClientUpTime": cLMobilityExtMOClientUpTime,
       "cLMobilityExtApMgrTable": cLMobilityExtApMgrTable,
       "cLMobilityExtApMgrEntry": cLMobilityExtApMgrEntry,
       "cLMobilityExtApMgrName": cLMobilityExtApMgrName,
       "cLMobilityExtApMgrAddressType": cLMobilityExtApMgrAddressType,
       "cLMobilityExtApMgrAddress": cLMobilityExtApMgrAddress,
       "cLMobilityExtApMgrNetmaskType": cLMobilityExtApMgrNetmaskType,
       "cLMobilityExtApMgrNetmask": cLMobilityExtApMgrNetmask,
       "cLMobilityExtApMgrMacAddress": cLMobilityExtApMgrMacAddress,
       "cLMobilityExtApMgrVlanId": cLMobilityExtApMgrVlanId,
       "cLMobilityExtApMgrInterfaceType": cLMobilityExtApMgrInterfaceType,
       "cLMobilityExtApMgrRowStatus": cLMobilityExtApMgrRowStatus,
       "cLMobilityExtForeignWlcMapTable": cLMobilityExtForeignWlcMapTable,
       "cLMobilityExtForeignWlcMapEntry": cLMobilityExtForeignWlcMapEntry,
       "cLMobilityExtForeignWlcAddressType": cLMobilityExtForeignWlcAddressType,
       "cLMobilityExtForeignWlcAddress": cLMobilityExtForeignWlcAddress,
       "cLMobilityExtForeignWlcMapIf": cLMobilityExtForeignWlcMapIf,
       "cLMobilityExtForeignWlcMapRowStatus": cLMobilityExtForeignWlcMapRowStatus,
       "cLMobilityExtGroupTable": cLMobilityExtGroupTable,
       "cLMobilityExtGroupEntry": cLMobilityExtGroupEntry,
       "cLMobilityExtGroupName": cLMobilityExtGroupName,
       "cLMobilityExtGroupMulticastAddressType": cLMobilityExtGroupMulticastAddressType,
       "cLMobilityExtGroupMulticastAddress": cLMobilityExtGroupMulticastAddress,
       "cLMobilityExtMAPeerTable": cLMobilityExtMAPeerTable,
       "cLMobilityExtMAPeerEntry": cLMobilityExtMAPeerEntry,
       "cLMobilityExtMAPeerPrivateAddressType": cLMobilityExtMAPeerPrivateAddressType,
       "cLMobilityExtMAPeerPrivateAddress": cLMobilityExtMAPeerPrivateAddress,
       "cLMobilityExtMAPeerPublicAddressType": cLMobilityExtMAPeerPublicAddressType,
       "cLMobilityExtMAPeerPublicAddress": cLMobilityExtMAPeerPublicAddress,
       "cLMobilityExtMAPeerLinkStatus": cLMobilityExtMAPeerLinkStatus,
       "cLMobilityExtMCMAStatisticsTable": cLMobilityExtMCMAStatisticsTable,
       "cLMobilityExtMCMAStatisticsEntry": cLMobilityExtMCMAStatisticsEntry,
       "cLMobilityExtMCMAPrivateAddressType": cLMobilityExtMCMAPrivateAddressType,
       "cLMobilityExtMCMAPrivateAddress": cLMobilityExtMCMAPrivateAddress,
       "cLMobilityExtMCMAClientCount": cLMobilityExtMCMAClientCount,
       "ciscoLwappMobilityExtNotifObjects": ciscoLwappMobilityExtNotifObjects,
       "cLMobilityExtNotifyObjectSourceIPAddressType": cLMobilityExtNotifyObjectSourceIPAddressType,
       "cLMobilityExtNotifyObjectSourceIPAddress": cLMobilityExtNotifyObjectSourceIPAddress,
       "cLMobilityExtNotifyObjectSourceType": cLMobilityExtNotifyObjectSourceType,
       "cLMobilityExtNotifyObjectDestinationType": cLMobilityExtNotifyObjectDestinationType,
       "ciscoLwappMobilityExtMIBConform": ciscoLwappMobilityExtMIBConform,
       "ciscoLwappMobilityExtMIBCompliances": ciscoLwappMobilityExtMIBCompliances,
       "ciscoLwappMobilityExtMIBCompliance": ciscoLwappMobilityExtMIBCompliance,
       "ciscoLwappMobilityExtMIBComplianceRev1": ciscoLwappMobilityExtMIBComplianceRev1,
       "ciscoLwappMobilityExtMIBGroups": ciscoLwappMobilityExtMIBGroups,
       "cLMobilityExtConfigGroup": cLMobilityExtConfigGroup,
       "ciscoLwappMobilityExtNotifyObjectsGroup": ciscoLwappMobilityExtNotifyObjectsGroup,
       "ciscoLwappMobilityExtNotifsGroup": ciscoLwappMobilityExtNotifsGroup,
       "cLMobilityExtConfigGroupRev1": cLMobilityExtConfigGroupRev1}
)
