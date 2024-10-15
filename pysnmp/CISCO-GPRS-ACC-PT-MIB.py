# SNMP MIB module (CISCO-GPRS-ACC-PT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GPRS-ACC-PT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:54 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoInetAddressMask,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoInetAddressMask",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoGprsAccPtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183)
)
ciscoGprsAccPtMIB.setRevisions(
        ("2012-04-04 00:00",
         "2011-09-22 00:00",
         "2011-03-14 00:00",
         "2010-04-29 00:00",
         "2010-04-02 20:00",
         "2008-12-19 00:00",
         "2008-03-03 00:00",
         "2008-02-27 00:00",
         "2006-08-30 00:00",
         "2006-05-18 13:00",
         "2005-11-22 14:00",
         "2005-10-28 17:00",
         "2004-07-26 02:00",
         "2004-02-11 20:00",
         "2002-08-26 18:00",
         "2002-06-13 18:00",
         "2001-12-28 14:30",
         "2000-07-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AccessControlListId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2699),
    )



class AccessControlListOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
        ValueRangeConstraint(1300, 2699),
    )



class AccessControlListName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoGprsAccPtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGprsAccPtMIBObjects = _CiscoGprsAccPtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1)
)
_CiscoGprsAccPtConfig_ObjectIdentity = ObjectIdentity
ciscoGprsAccPtConfig = _CiscoGprsAccPtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1)
)
_CgprsAccPtTable_Object = MibTable
cgprsAccPtTable = _CgprsAccPtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtTable.setStatus("current")
_CgprsAccPtEntry_Object = MibTableRow
cgprsAccPtEntry = _CgprsAccPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1)
)
cgprsAccPtEntry.setIndexNames(
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIndex"),
)
if mibBuilder.loadTexts:
    cgprsAccPtEntry.setStatus("current")


class _CgprsAccPtIndex_Type(Unsigned32):
    """Custom type cgprsAccPtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgprsAccPtIndex_Type.__name__ = "Unsigned32"
_CgprsAccPtIndex_Object = MibTableColumn
cgprsAccPtIndex = _CgprsAccPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 1),
    _CgprsAccPtIndex_Type()
)
cgprsAccPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsAccPtIndex.setStatus("current")
_CgprsAccPtRowStatus_Type = RowStatus
_CgprsAccPtRowStatus_Object = MibTableColumn
cgprsAccPtRowStatus = _CgprsAccPtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 2),
    _CgprsAccPtRowStatus_Type()
)
cgprsAccPtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRowStatus.setStatus("current")


class _CgprsAccPtName_Type(SnmpAdminString):
    """Custom type cgprsAccPtName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CgprsAccPtName_Type.__name__ = "SnmpAdminString"
_CgprsAccPtName_Object = MibTableColumn
cgprsAccPtName = _CgprsAccPtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 3),
    _CgprsAccPtName_Type()
)
cgprsAccPtName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtName.setStatus("current")


class _CgprsAccPtMode_Type(Integer32):
    """Custom type cgprsAccPtMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nontransparent", 2),
          ("transparent", 1))
    )


_CgprsAccPtMode_Type.__name__ = "Integer32"
_CgprsAccPtMode_Object = MibTableColumn
cgprsAccPtMode = _CgprsAccPtMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 4),
    _CgprsAccPtMode_Type()
)
cgprsAccPtMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtMode.setStatus("current")


class _CgprsAccPtIpAddressPool_Type(Integer32):
    """Custom type cgprsAccPtIpAddressPool based on Integer32"""
    defaultValue = 1

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
        *(("dhcp", 2),
          ("disable", 4),
          ("global", 1),
          ("local", 5),
          ("radius", 3))
    )


_CgprsAccPtIpAddressPool_Type.__name__ = "Integer32"
_CgprsAccPtIpAddressPool_Object = MibTableColumn
cgprsAccPtIpAddressPool = _CgprsAccPtIpAddressPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 5),
    _CgprsAccPtIpAddressPool_Type()
)
cgprsAccPtIpAddressPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpAddressPool.setStatus("current")
_CgprsAccPtDHCPServerPri_Type = IpAddress
_CgprsAccPtDHCPServerPri_Object = MibTableColumn
cgprsAccPtDHCPServerPri = _CgprsAccPtDHCPServerPri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 6),
    _CgprsAccPtDHCPServerPri_Type()
)
cgprsAccPtDHCPServerPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtDHCPServerPri.setStatus("current")
_CgprsAccPtDHCPServerSec_Type = IpAddress
_CgprsAccPtDHCPServerSec_Object = MibTableColumn
cgprsAccPtDHCPServerSec = _CgprsAccPtDHCPServerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 7),
    _CgprsAccPtDHCPServerSec_Type()
)
cgprsAccPtDHCPServerSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtDHCPServerSec.setStatus("current")
_CgprsAccPtDHCPGwAddr_Type = IpAddress
_CgprsAccPtDHCPGwAddr_Object = MibTableColumn
cgprsAccPtDHCPGwAddr = _CgprsAccPtDHCPGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 8),
    _CgprsAccPtDHCPGwAddr_Type()
)
cgprsAccPtDHCPGwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtDHCPGwAddr.setStatus("current")
_CgprsAccPtRadiusServerPri_Type = IpAddress
_CgprsAccPtRadiusServerPri_Object = MibTableColumn
cgprsAccPtRadiusServerPri = _CgprsAccPtRadiusServerPri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 9),
    _CgprsAccPtRadiusServerPri_Type()
)
cgprsAccPtRadiusServerPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRadiusServerPri.setStatus("obsolete")
_CgprsAccPtRadiusServerSec_Type = IpAddress
_CgprsAccPtRadiusServerSec_Object = MibTableColumn
cgprsAccPtRadiusServerSec = _CgprsAccPtRadiusServerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 10),
    _CgprsAccPtRadiusServerSec_Type()
)
cgprsAccPtRadiusServerSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRadiusServerSec.setStatus("obsolete")
_CgprsAccPtIPAccListGroupIn_Type = AccessControlListId
_CgprsAccPtIPAccListGroupIn_Object = MibTableColumn
cgprsAccPtIPAccListGroupIn = _CgprsAccPtIPAccListGroupIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 11),
    _CgprsAccPtIPAccListGroupIn_Type()
)
cgprsAccPtIPAccListGroupIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIPAccListGroupIn.setStatus("current")
_CgprsAccPtIPAccListGroupOut_Type = AccessControlListId
_CgprsAccPtIPAccListGroupOut_Object = MibTableColumn
cgprsAccPtIPAccListGroupOut = _CgprsAccPtIPAccListGroupOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 12),
    _CgprsAccPtIPAccListGroupOut_Type()
)
cgprsAccPtIPAccListGroupOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIPAccListGroupOut.setStatus("current")


class _CgprsAccPtIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cgprsAccPtIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CgprsAccPtIfIndex_Object = MibTableColumn
cgprsAccPtIfIndex = _CgprsAccPtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 13),
    _CgprsAccPtIfIndex_Type()
)
cgprsAccPtIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIfIndex.setStatus("obsolete")
_CgprsAccPtIfNextHop_Type = IpAddress
_CgprsAccPtIfNextHop_Object = MibTableColumn
cgprsAccPtIfNextHop = _CgprsAccPtIfNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 14),
    _CgprsAccPtIfNextHop_Type()
)
cgprsAccPtIfNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIfNextHop.setStatus("obsolete")


class _CgprsAccPtAccessViolation_Type(Integer32):
    """Custom type cgprsAccPtAccessViolation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discardPacket", 1),
          ("terminateSession", 2))
    )


_CgprsAccPtAccessViolation_Type.__name__ = "Integer32"
_CgprsAccPtAccessViolation_Object = MibTableColumn
cgprsAccPtAccessViolation = _CgprsAccPtAccessViolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 15),
    _CgprsAccPtAccessViolation_Type()
)
cgprsAccPtAccessViolation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAccessViolation.setStatus("current")


class _CgprsAccPtSubrRequired_Type(TruthValue):
    """Custom type cgprsAccPtSubrRequired based on TruthValue"""


_CgprsAccPtSubrRequired_Object = MibTableColumn
cgprsAccPtSubrRequired = _CgprsAccPtSubrRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 16),
    _CgprsAccPtSubrRequired_Type()
)
cgprsAccPtSubrRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtSubrRequired.setStatus("current")


class _CgprsAccPtNetworkInitiated_Type(TruthValue):
    """Custom type cgprsAccPtNetworkInitiated based on TruthValue"""


_CgprsAccPtNetworkInitiated_Object = MibTableColumn
cgprsAccPtNetworkInitiated = _CgprsAccPtNetworkInitiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 17),
    _CgprsAccPtNetworkInitiated_Type()
)
cgprsAccPtNetworkInitiated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtNetworkInitiated.setStatus("current")
_CgprsAccPtIpAddrAllocations_Type = Gauge32
_CgprsAccPtIpAddrAllocations_Object = MibTableColumn
cgprsAccPtIpAddrAllocations = _CgprsAccPtIpAddrAllocations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 18),
    _CgprsAccPtIpAddrAllocations_Type()
)
cgprsAccPtIpAddrAllocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpAddrAllocations.setStatus("current")
_CgprsAccPtUsers_Type = Gauge32
_CgprsAccPtUsers_Object = MibTableColumn
cgprsAccPtUsers = _CgprsAccPtUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 19),
    _CgprsAccPtUsers_Type()
)
cgprsAccPtUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtUsers.setStatus("obsolete")


class _CgprsAccPtIdlePdpPurgeTimer_Type(Unsigned32):
    """Custom type cgprsAccPtIdlePdpPurgeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_CgprsAccPtIdlePdpPurgeTimer_Type.__name__ = "Unsigned32"
_CgprsAccPtIdlePdpPurgeTimer_Object = MibTableColumn
cgprsAccPtIdlePdpPurgeTimer = _CgprsAccPtIdlePdpPurgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 20),
    _CgprsAccPtIdlePdpPurgeTimer_Type()
)
cgprsAccPtIdlePdpPurgeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIdlePdpPurgeTimer.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtIdlePdpPurgeTimer.setUnits("hours")


class _CgprsAccPtBlockMsRoaming_Type(TruthValue):
    """Custom type cgprsAccPtBlockMsRoaming based on TruthValue"""


_CgprsAccPtBlockMsRoaming_Object = MibTableColumn
cgprsAccPtBlockMsRoaming = _CgprsAccPtBlockMsRoaming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 21),
    _CgprsAccPtBlockMsRoaming_Type()
)
cgprsAccPtBlockMsRoaming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtBlockMsRoaming.setStatus("current")
_CgprsAccPtAnonymousUserName_Type = SnmpAdminString
_CgprsAccPtAnonymousUserName_Object = MibTableColumn
cgprsAccPtAnonymousUserName = _CgprsAccPtAnonymousUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 22),
    _CgprsAccPtAnonymousUserName_Type()
)
cgprsAccPtAnonymousUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAnonymousUserName.setStatus("current")
_CgprsAccPtAnonymousUserPassword_Type = SnmpAdminString
_CgprsAccPtAnonymousUserPassword_Object = MibTableColumn
cgprsAccPtAnonymousUserPassword = _CgprsAccPtAnonymousUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 23),
    _CgprsAccPtAnonymousUserPassword_Type()
)
cgprsAccPtAnonymousUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAnonymousUserPassword.setStatus("current")


class _CgprsAccPtMsIsdnSuppressed_Type(TruthValue):
    """Custom type cgprsAccPtMsIsdnSuppressed based on TruthValue"""


_CgprsAccPtMsIsdnSuppressed_Object = MibTableColumn
cgprsAccPtMsIsdnSuppressed = _CgprsAccPtMsIsdnSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 24),
    _CgprsAccPtMsIsdnSuppressed_Type()
)
cgprsAccPtMsIsdnSuppressed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtMsIsdnSuppressed.setStatus("current")


class _CgprsAccPtMsIsdnSuppressedValue_Type(DisplayString):
    """Custom type cgprsAccPtMsIsdnSuppressedValue based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CgprsAccPtMsIsdnSuppressedValue_Type.__name__ = "DisplayString"
_CgprsAccPtMsIsdnSuppressedValue_Object = MibTableColumn
cgprsAccPtMsIsdnSuppressedValue = _CgprsAccPtMsIsdnSuppressedValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 25),
    _CgprsAccPtMsIsdnSuppressedValue_Type()
)
cgprsAccPtMsIsdnSuppressedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtMsIsdnSuppressedValue.setStatus("current")
_CgprsAccPtAaaAuthServerGroup_Type = SnmpAdminString
_CgprsAccPtAaaAuthServerGroup_Object = MibTableColumn
cgprsAccPtAaaAuthServerGroup = _CgprsAccPtAaaAuthServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 26),
    _CgprsAccPtAaaAuthServerGroup_Type()
)
cgprsAccPtAaaAuthServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAaaAuthServerGroup.setStatus("current")
_CgprsAccPtAaaAccountServerGroup_Type = SnmpAdminString
_CgprsAccPtAaaAccountServerGroup_Object = MibTableColumn
cgprsAccPtAaaAccountServerGroup = _CgprsAccPtAaaAccountServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 27),
    _CgprsAccPtAaaAccountServerGroup_Type()
)
cgprsAccPtAaaAccountServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAaaAccountServerGroup.setStatus("current")
_CgprsAccPtAaaAccountingEnable_Type = TruthValue
_CgprsAccPtAaaAccountingEnable_Object = MibTableColumn
cgprsAccPtAaaAccountingEnable = _CgprsAccPtAaaAccountingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 28),
    _CgprsAccPtAaaAccountingEnable_Type()
)
cgprsAccPtAaaAccountingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAaaAccountingEnable.setStatus("current")


class _CgprsAccPtType_Type(Integer32):
    """Custom type cgprsAccPtType based on Integer32"""
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
        *(("real", 1),
          ("virtual", 2),
          ("virtualPreAuth", 3))
    )


_CgprsAccPtType_Type.__name__ = "Integer32"
_CgprsAccPtType_Object = MibTableColumn
cgprsAccPtType = _CgprsAccPtType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 29),
    _CgprsAccPtType_Type()
)
cgprsAccPtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtType.setStatus("current")
_CgprsAccPtVrfName_Type = SnmpAdminString
_CgprsAccPtVrfName_Object = MibTableColumn
cgprsAccPtVrfName = _CgprsAccPtVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 30),
    _CgprsAccPtVrfName_Type()
)
cgprsAccPtVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtVrfName.setStatus("current")


class _CgprsAccPtDhcpAddrSpace_Type(Integer32):
    """Custom type cgprsAccPtDhcpAddrSpace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("vrf", 2))
    )


_CgprsAccPtDhcpAddrSpace_Type.__name__ = "Integer32"
_CgprsAccPtDhcpAddrSpace_Object = MibTableColumn
cgprsAccPtDhcpAddrSpace = _CgprsAccPtDhcpAddrSpace_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 31),
    _CgprsAccPtDhcpAddrSpace_Type()
)
cgprsAccPtDhcpAddrSpace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpAddrSpace.setStatus("current")


class _CgprsAccPtPppRegenEnable_Type(TruthValue):
    """Custom type cgprsAccPtPppRegenEnable based on TruthValue"""


_CgprsAccPtPppRegenEnable_Object = MibTableColumn
cgprsAccPtPppRegenEnable = _CgprsAccPtPppRegenEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 32),
    _CgprsAccPtPppRegenEnable_Type()
)
cgprsAccPtPppRegenEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPppRegenEnable.setStatus("current")


class _CgprsAccPtPppRegenMaxSessions_Type(Integer32):
    """Custom type cgprsAccPtPppRegenMaxSessions based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgprsAccPtPppRegenMaxSessions_Type.__name__ = "Integer32"
_CgprsAccPtPppRegenMaxSessions_Object = MibTableColumn
cgprsAccPtPppRegenMaxSessions = _CgprsAccPtPppRegenMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 33),
    _CgprsAccPtPppRegenMaxSessions_Type()
)
cgprsAccPtPppRegenMaxSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPppRegenMaxSessions.setStatus("current")


class _CgprsAccPtPppRegenSetupTime_Type(Integer32):
    """Custom type cgprsAccPtPppRegenSetupTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgprsAccPtPppRegenSetupTime_Type.__name__ = "Integer32"
_CgprsAccPtPppRegenSetupTime_Object = MibTableColumn
cgprsAccPtPppRegenSetupTime = _CgprsAccPtPppRegenSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 34),
    _CgprsAccPtPppRegenSetupTime_Type()
)
cgprsAccPtPppRegenSetupTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPppRegenSetupTime.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtPppRegenSetupTime.setUnits("seconds")


class _CgprsAccPtAutoAggregation_Type(TruthValue):
    """Custom type cgprsAccPtAutoAggregation based on TruthValue"""


_CgprsAccPtAutoAggregation_Object = MibTableColumn
cgprsAccPtAutoAggregation = _CgprsAccPtAutoAggregation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 35),
    _CgprsAccPtAutoAggregation_Type()
)
cgprsAccPtAutoAggregation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAutoAggregation.setStatus("current")


class _CgprsAccPtPcscfServerGroupName_Type(SnmpAdminString):
    """Custom type cgprsAccPtPcscfServerGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CgprsAccPtPcscfServerGroupName_Type.__name__ = "SnmpAdminString"
_CgprsAccPtPcscfServerGroupName_Object = MibTableColumn
cgprsAccPtPcscfServerGroupName = _CgprsAccPtPcscfServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 1, 1, 36),
    _CgprsAccPtPcscfServerGroupName_Type()
)
cgprsAccPtPcscfServerGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPcscfServerGroupName.setStatus("current")
_CgprsAccPtAggregTable_Object = MibTable
cgprsAccPtAggregTable = _CgprsAccPtAggregTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cgprsAccPtAggregTable.setStatus("current")
_CgprsAccPtAggregEntry_Object = MibTableRow
cgprsAccPtAggregEntry = _CgprsAccPtAggregEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 2, 1)
)
cgprsAccPtAggregEntry.setIndexNames(
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIndex"),
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAggregIpAddrType"),
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAggregIpAddr"),
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAggregIpMask"),
)
if mibBuilder.loadTexts:
    cgprsAccPtAggregEntry.setStatus("current")
_CgprsAccPtAggregIpAddrType_Type = InetAddressType
_CgprsAccPtAggregIpAddrType_Object = MibTableColumn
cgprsAccPtAggregIpAddrType = _CgprsAccPtAggregIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 2, 1, 1),
    _CgprsAccPtAggregIpAddrType_Type()
)
cgprsAccPtAggregIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsAccPtAggregIpAddrType.setStatus("current")
_CgprsAccPtAggregIpAddr_Type = InetAddress
_CgprsAccPtAggregIpAddr_Object = MibTableColumn
cgprsAccPtAggregIpAddr = _CgprsAccPtAggregIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 2, 1, 2),
    _CgprsAccPtAggregIpAddr_Type()
)
cgprsAccPtAggregIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsAccPtAggregIpAddr.setStatus("current")
_CgprsAccPtAggregIpMask_Type = CiscoInetAddressMask
_CgprsAccPtAggregIpMask_Object = MibTableColumn
cgprsAccPtAggregIpMask = _CgprsAccPtAggregIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 2, 1, 3),
    _CgprsAccPtAggregIpMask_Type()
)
cgprsAccPtAggregIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsAccPtAggregIpMask.setStatus("current")
_CgprsAccPtAggregRowStatus_Type = RowStatus
_CgprsAccPtAggregRowStatus_Object = MibTableColumn
cgprsAccPtAggregRowStatus = _CgprsAccPtAggregRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 2, 1, 4),
    _CgprsAccPtAggregRowStatus_Type()
)
cgprsAccPtAggregRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAggregRowStatus.setStatus("current")
_CgprsAccPtAggregCsgGroup_Type = SnmpAdminString
_CgprsAccPtAggregCsgGroup_Object = MibTableColumn
cgprsAccPtAggregCsgGroup = _CgprsAccPtAggregCsgGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 2, 1, 5),
    _CgprsAccPtAggregCsgGroup_Type()
)
cgprsAccPtAggregCsgGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAggregCsgGroup.setStatus("current")
_CgprsAccPtExtTable_Object = MibTable
cgprsAccPtExtTable = _CgprsAccPtExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cgprsAccPtExtTable.setStatus("current")
_CgprsAccPtExtEntry_Object = MibTableRow
cgprsAccPtExtEntry = _CgprsAccPtExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtExtEntry.setStatus("current")


class _CgprsAccPtIPAccListInEnable_Type(TruthValue):
    """Custom type cgprsAccPtIPAccListInEnable based on TruthValue"""


_CgprsAccPtIPAccListInEnable_Object = MibTableColumn
cgprsAccPtIPAccListInEnable = _CgprsAccPtIPAccListInEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 1),
    _CgprsAccPtIPAccListInEnable_Type()
)
cgprsAccPtIPAccListInEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIPAccListInEnable.setStatus("current")


class _CgprsAccPtIPAccListOutEnable_Type(TruthValue):
    """Custom type cgprsAccPtIPAccListOutEnable based on TruthValue"""


_CgprsAccPtIPAccListOutEnable_Object = MibTableColumn
cgprsAccPtIPAccListOutEnable = _CgprsAccPtIPAccListOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 2),
    _CgprsAccPtIPAccListOutEnable_Type()
)
cgprsAccPtIPAccListOutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIPAccListOutEnable.setStatus("current")


class _CgprsAccPtGtpRespMesgWaitAcctng_Type(TruthValue):
    """Custom type cgprsAccPtGtpRespMesgWaitAcctng based on TruthValue"""


_CgprsAccPtGtpRespMesgWaitAcctng_Object = MibTableColumn
cgprsAccPtGtpRespMesgWaitAcctng = _CgprsAccPtGtpRespMesgWaitAcctng_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 3),
    _CgprsAccPtGtpRespMesgWaitAcctng_Type()
)
cgprsAccPtGtpRespMesgWaitAcctng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtGtpRespMesgWaitAcctng.setStatus("current")


class _CgprsAccPtImsiSuppressed_Type(TruthValue):
    """Custom type cgprsAccPtImsiSuppressed based on TruthValue"""


_CgprsAccPtImsiSuppressed_Object = MibTableColumn
cgprsAccPtImsiSuppressed = _CgprsAccPtImsiSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 4),
    _CgprsAccPtImsiSuppressed_Type()
)
cgprsAccPtImsiSuppressed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtImsiSuppressed.setStatus("obsolete")


class _CgprsAccPtVerifyUpStrTpduSrcAddr_Type(TruthValue):
    """Custom type cgprsAccPtVerifyUpStrTpduSrcAddr based on TruthValue"""


_CgprsAccPtVerifyUpStrTpduSrcAddr_Object = MibTableColumn
cgprsAccPtVerifyUpStrTpduSrcAddr = _CgprsAccPtVerifyUpStrTpduSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 5),
    _CgprsAccPtVerifyUpStrTpduSrcAddr_Type()
)
cgprsAccPtVerifyUpStrTpduSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtVerifyUpStrTpduSrcAddr.setStatus("current")


class _CgprsAccPtVerifyUpStrTpduDstAddr_Type(TruthValue):
    """Custom type cgprsAccPtVerifyUpStrTpduDstAddr based on TruthValue"""


_CgprsAccPtVerifyUpStrTpduDstAddr_Object = MibTableColumn
cgprsAccPtVerifyUpStrTpduDstAddr = _CgprsAccPtVerifyUpStrTpduDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 6),
    _CgprsAccPtVerifyUpStrTpduDstAddr_Type()
)
cgprsAccPtVerifyUpStrTpduDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtVerifyUpStrTpduDstAddr.setStatus("current")
_CgprsAccPtRedirInterMobilAddrTyp_Type = InetAddressType
_CgprsAccPtRedirInterMobilAddrTyp_Object = MibTableColumn
cgprsAccPtRedirInterMobilAddrTyp = _CgprsAccPtRedirInterMobilAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 7),
    _CgprsAccPtRedirInterMobilAddrTyp_Type()
)
cgprsAccPtRedirInterMobilAddrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRedirInterMobilAddrTyp.setStatus("current")
_CgprsAccPtRedirInterMobilAddr_Type = InetAddress
_CgprsAccPtRedirInterMobilAddr_Object = MibTableColumn
cgprsAccPtRedirInterMobilAddr = _CgprsAccPtRedirInterMobilAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 8),
    _CgprsAccPtRedirInterMobilAddr_Type()
)
cgprsAccPtRedirInterMobilAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRedirInterMobilAddr.setStatus("current")


class _CgprsAccPtSuppressRadiusAttribs_Type(Bits):
    """Custom type cgprsAccPtSuppressRadiusAttribs based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("imsi", 1),
          ("none", 0),
          ("qos", 3),
          ("sgsnAddr", 2))
    )

_CgprsAccPtSuppressRadiusAttribs_Type.__name__ = "Bits"
_CgprsAccPtSuppressRadiusAttribs_Object = MibTableColumn
cgprsAccPtSuppressRadiusAttribs = _CgprsAccPtSuppressRadiusAttribs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 9),
    _CgprsAccPtSuppressRadiusAttribs_Type()
)
cgprsAccPtSuppressRadiusAttribs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtSuppressRadiusAttribs.setStatus("current")


class _CgprsAccPtInterimAccountinEnable_Type(TruthValue):
    """Custom type cgprsAccPtInterimAccountinEnable based on TruthValue"""


_CgprsAccPtInterimAccountinEnable_Object = MibTableColumn
cgprsAccPtInterimAccountinEnable = _CgprsAccPtInterimAccountinEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 10),
    _CgprsAccPtInterimAccountinEnable_Type()
)
cgprsAccPtInterimAccountinEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtInterimAccountinEnable.setStatus("current")


class _CgprsAccPtSetRadiusAttributes_Type(Bits):
    """Custom type cgprsAccPtSetRadiusAttributes based on Bits"""
    namedValues = NamedValues(
        *(("accSessIdChargingId", 2),
          ("none", 0),
          ("userNameMsisdn", 1))
    )

_CgprsAccPtSetRadiusAttributes_Type.__name__ = "Bits"
_CgprsAccPtSetRadiusAttributes_Object = MibTableColumn
cgprsAccPtSetRadiusAttributes = _CgprsAccPtSetRadiusAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 11),
    _CgprsAccPtSetRadiusAttributes_Type()
)
cgprsAccPtSetRadiusAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtSetRadiusAttributes.setStatus("current")


class _CgprsAccPtOperationMode_Type(Integer32):
    """Custom type cgprsAccPtOperationMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inService", 0),
          ("maintenance", 1))
    )


_CgprsAccPtOperationMode_Type.__name__ = "Integer32"
_CgprsAccPtOperationMode_Object = MibTableColumn
cgprsAccPtOperationMode = _CgprsAccPtOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 12),
    _CgprsAccPtOperationMode_Type()
)
cgprsAccPtOperationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtOperationMode.setStatus("current")


class _CgprsAccPtAbsoluteSessionTimer_Type(Unsigned32):
    """Custom type cgprsAccPtAbsoluteSessionTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 4294967),
    )


_CgprsAccPtAbsoluteSessionTimer_Type.__name__ = "Unsigned32"
_CgprsAccPtAbsoluteSessionTimer_Object = MibTableColumn
cgprsAccPtAbsoluteSessionTimer = _CgprsAccPtAbsoluteSessionTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 13),
    _CgprsAccPtAbsoluteSessionTimer_Type()
)
cgprsAccPtAbsoluteSessionTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAbsoluteSessionTimer.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtAbsoluteSessionTimer.setUnits("seconds")
_CgprsAccPtRadiusAttrNasId_Type = SnmpAdminString
_CgprsAccPtRadiusAttrNasId_Object = MibTableColumn
cgprsAccPtRadiusAttrNasId = _CgprsAccPtRadiusAttrNasId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 14),
    _CgprsAccPtRadiusAttrNasId_Type()
)
cgprsAccPtRadiusAttrNasId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRadiusAttrNasId.setStatus("current")


class _CgprsAccPtPdpInServicePolicyName_Type(SnmpAdminString):
    """Custom type cgprsAccPtPdpInServicePolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CgprsAccPtPdpInServicePolicyName_Type.__name__ = "SnmpAdminString"
_CgprsAccPtPdpInServicePolicyName_Object = MibTableColumn
cgprsAccPtPdpInServicePolicyName = _CgprsAccPtPdpInServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 15),
    _CgprsAccPtPdpInServicePolicyName_Type()
)
cgprsAccPtPdpInServicePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPdpInServicePolicyName.setStatus("current")


class _CgprsAccPtPdpOutServicePolicyNam_Type(SnmpAdminString):
    """Custom type cgprsAccPtPdpOutServicePolicyNam based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CgprsAccPtPdpOutServicePolicyNam_Type.__name__ = "SnmpAdminString"
_CgprsAccPtPdpOutServicePolicyNam_Object = MibTableColumn
cgprsAccPtPdpOutServicePolicyNam = _CgprsAccPtPdpOutServicePolicyNam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 16),
    _CgprsAccPtPdpOutServicePolicyNam_Type()
)
cgprsAccPtPdpOutServicePolicyNam.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPdpOutServicePolicyNam.setStatus("current")


class _CgprsAccPtPppRegenVerifyDomain_Type(TruthValue):
    """Custom type cgprsAccPtPppRegenVerifyDomain based on TruthValue"""


_CgprsAccPtPppRegenVerifyDomain_Object = MibTableColumn
cgprsAccPtPppRegenVerifyDomain = _CgprsAccPtPppRegenVerifyDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 17),
    _CgprsAccPtPppRegenVerifyDomain_Type()
)
cgprsAccPtPppRegenVerifyDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPppRegenVerifyDomain.setStatus("current")
_CgprsAccPtIpAddrLocalPoolName_Type = SnmpAdminString
_CgprsAccPtIpAddrLocalPoolName_Object = MibTableColumn
cgprsAccPtIpAddrLocalPoolName = _CgprsAccPtIpAddrLocalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 18),
    _CgprsAccPtIpAddrLocalPoolName_Type()
)
cgprsAccPtIpAddrLocalPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpAddrLocalPoolName.setStatus("current")


class _CgprsAccPtServiceAware_Type(TruthValue):
    """Custom type cgprsAccPtServiceAware based on TruthValue"""


_CgprsAccPtServiceAware_Object = MibTableColumn
cgprsAccPtServiceAware = _CgprsAccPtServiceAware_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 19),
    _CgprsAccPtServiceAware_Type()
)
cgprsAccPtServiceAware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtServiceAware.setStatus("current")
_CgprsAccPtAdvDownlinkNextHopAddrType_Type = InetAddressType
_CgprsAccPtAdvDownlinkNextHopAddrType_Object = MibTableColumn
cgprsAccPtAdvDownlinkNextHopAddrType = _CgprsAccPtAdvDownlinkNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 20),
    _CgprsAccPtAdvDownlinkNextHopAddrType_Type()
)
cgprsAccPtAdvDownlinkNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAdvDownlinkNextHopAddrType.setStatus("current")
_CgprsAccPtAdvDownlinkNextHopAddr_Type = InetAddress
_CgprsAccPtAdvDownlinkNextHopAddr_Object = MibTableColumn
cgprsAccPtAdvDownlinkNextHopAddr = _CgprsAccPtAdvDownlinkNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 21),
    _CgprsAccPtAdvDownlinkNextHopAddr_Type()
)
cgprsAccPtAdvDownlinkNextHopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAdvDownlinkNextHopAddr.setStatus("current")


class _CgprsAccPtGtpUpdateFailDelete_Type(TruthValue):
    """Custom type cgprsAccPtGtpUpdateFailDelete based on TruthValue"""


_CgprsAccPtGtpUpdateFailDelete_Object = MibTableColumn
cgprsAccPtGtpUpdateFailDelete = _CgprsAccPtGtpUpdateFailDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 22),
    _CgprsAccPtGtpUpdateFailDelete_Type()
)
cgprsAccPtGtpUpdateFailDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtGtpUpdateFailDelete.setStatus("current")


class _CgprsAccPtAaaAccountInterPeriod_Type(Unsigned32):
    """Custom type cgprsAccPtAaaAccountInterPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(15, 71582),
    )


_CgprsAccPtAaaAccountInterPeriod_Type.__name__ = "Unsigned32"
_CgprsAccPtAaaAccountInterPeriod_Object = MibTableColumn
cgprsAccPtAaaAccountInterPeriod = _CgprsAccPtAaaAccountInterPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 23),
    _CgprsAccPtAaaAccountInterPeriod_Type()
)
cgprsAccPtAaaAccountInterPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAaaAccountInterPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtAaaAccountInterPeriod.setUnits("minutes")


class _CgprsAccPtAaaAccountInterRadius_Type(TruthValue):
    """Custom type cgprsAccPtAaaAccountInterRadius based on TruthValue"""


_CgprsAccPtAaaAccountInterRadius_Object = MibTableColumn
cgprsAccPtAaaAccountInterRadius = _CgprsAccPtAaaAccountInterRadius_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 24),
    _CgprsAccPtAaaAccountInterRadius_Type()
)
cgprsAccPtAaaAccountInterRadius.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtAaaAccountInterRadius.setStatus("current")


class _CgprsAccPtGxEnable_Type(TruthValue):
    """Custom type cgprsAccPtGxEnable based on TruthValue"""


_CgprsAccPtGxEnable_Object = MibTableColumn
cgprsAccPtGxEnable = _CgprsAccPtGxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 25),
    _CgprsAccPtGxEnable_Type()
)
cgprsAccPtGxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtGxEnable.setStatus("current")


class _CgprsAccPtPcscfLoadBalance_Type(TruthValue):
    """Custom type cgprsAccPtPcscfLoadBalance based on TruthValue"""


_CgprsAccPtPcscfLoadBalance_Object = MibTableColumn
cgprsAccPtPcscfLoadBalance = _CgprsAccPtPcscfLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 26),
    _CgprsAccPtPcscfLoadBalance_Type()
)
cgprsAccPtPcscfLoadBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPcscfLoadBalance.setStatus("current")


class _CgprsAccPtNetworkBehindMsEnable_Type(TruthValue):
    """Custom type cgprsAccPtNetworkBehindMsEnable based on TruthValue"""


_CgprsAccPtNetworkBehindMsEnable_Object = MibTableColumn
cgprsAccPtNetworkBehindMsEnable = _CgprsAccPtNetworkBehindMsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 27),
    _CgprsAccPtNetworkBehindMsEnable_Type()
)
cgprsAccPtNetworkBehindMsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtNetworkBehindMsEnable.setStatus("current")


class _CgprsAccPtMaxSubnetsBehindMobile_Type(Unsigned32):
    """Custom type cgprsAccPtMaxSubnetsBehindMobile based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CgprsAccPtMaxSubnetsBehindMobile_Type.__name__ = "Unsigned32"
_CgprsAccPtMaxSubnetsBehindMobile_Object = MibTableColumn
cgprsAccPtMaxSubnetsBehindMobile = _CgprsAccPtMaxSubnetsBehindMobile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 28),
    _CgprsAccPtMaxSubnetsBehindMobile_Type()
)
cgprsAccPtMaxSubnetsBehindMobile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtMaxSubnetsBehindMobile.setStatus("current")


class _CgprsAccPtChargingRecordType_Type(Integer32):
    """Custom type cgprsAccPtChargingRecordType based on Integer32"""
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
        *(("egcdr", 3),
          ("gcdr", 2),
          ("noconfig", 0),
          ("none", 1))
    )


_CgprsAccPtChargingRecordType_Type.__name__ = "Integer32"
_CgprsAccPtChargingRecordType_Object = MibTableColumn
cgprsAccPtChargingRecordType = _CgprsAccPtChargingRecordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 29),
    _CgprsAccPtChargingRecordType_Type()
)
cgprsAccPtChargingRecordType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtChargingRecordType.setStatus("current")


class _CgprsAccPtChargingGrp_Type(Unsigned32):
    """Custom type cgprsAccPtChargingGrp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_CgprsAccPtChargingGrp_Type.__name__ = "Unsigned32"
_CgprsAccPtChargingGrp_Object = MibTableColumn
cgprsAccPtChargingGrp = _CgprsAccPtChargingGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 30),
    _CgprsAccPtChargingGrp_Type()
)
cgprsAccPtChargingGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtChargingGrp.setStatus("current")


class _CgprsAccPtIpAddrPoolNoRedistribute_Type(TruthValue):
    """Custom type cgprsAccPtIpAddrPoolNoRedistribute based on TruthValue"""


_CgprsAccPtIpAddrPoolNoRedistribute_Object = MibTableColumn
cgprsAccPtIpAddrPoolNoRedistribute = _CgprsAccPtIpAddrPoolNoRedistribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 31),
    _CgprsAccPtIpAddrPoolNoRedistribute_Type()
)
cgprsAccPtIpAddrPoolNoRedistribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpAddrPoolNoRedistribute.setStatus("current")


class _CgprsAccPtDualAddrEnabled_Type(TruthValue):
    """Custom type cgprsAccPtDualAddrEnabled based on TruthValue"""


_CgprsAccPtDualAddrEnabled_Object = MibTableColumn
cgprsAccPtDualAddrEnabled = _CgprsAccPtDualAddrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 32),
    _CgprsAccPtDualAddrEnabled_Type()
)
cgprsAccPtDualAddrEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtDualAddrEnabled.setStatus("current")


class _CgprsAccPtVerifyDownlinkAddr_Type(TruthValue):
    """Custom type cgprsAccPtVerifyDownlinkAddr based on TruthValue"""


_CgprsAccPtVerifyDownlinkAddr_Object = MibTableColumn
cgprsAccPtVerifyDownlinkAddr = _CgprsAccPtVerifyDownlinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 3, 1, 33),
    _CgprsAccPtVerifyDownlinkAddr_Type()
)
cgprsAccPtVerifyDownlinkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtVerifyDownlinkAddr.setStatus("current")
_CgprsAccPtGenServerConfigs_ObjectIdentity = ObjectIdentity
cgprsAccPtGenServerConfigs = _CgprsAccPtGenServerConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 4)
)
_CgprsAccPtGenServerConfigTable_Object = MibTable
cgprsAccPtGenServerConfigTable = _CgprsAccPtGenServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtGenServerConfigTable.setStatus("current")
_CgprsAccPtGenServerConfigEntry_Object = MibTableRow
cgprsAccPtGenServerConfigEntry = _CgprsAccPtGenServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtGenServerConfigEntry.setStatus("current")
_CgprsAccPtDnsServerAddrType_Type = InetAddressType
_CgprsAccPtDnsServerAddrType_Object = MibTableColumn
cgprsAccPtDnsServerAddrType = _CgprsAccPtDnsServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 4, 1, 1, 1),
    _CgprsAccPtDnsServerAddrType_Type()
)
cgprsAccPtDnsServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtDnsServerAddrType.setStatus("current")
_CgprsAccPtPriDnsServer_Type = InetAddress
_CgprsAccPtPriDnsServer_Object = MibTableColumn
cgprsAccPtPriDnsServer = _CgprsAccPtPriDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 4, 1, 1, 2),
    _CgprsAccPtPriDnsServer_Type()
)
cgprsAccPtPriDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPriDnsServer.setStatus("current")
_CgprsAccPtSecDnsServer_Type = InetAddress
_CgprsAccPtSecDnsServer_Object = MibTableColumn
cgprsAccPtSecDnsServer = _CgprsAccPtSecDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 4, 1, 1, 3),
    _CgprsAccPtSecDnsServer_Type()
)
cgprsAccPtSecDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtSecDnsServer.setStatus("current")
_CgprsAccPtNetbiosServerAddrType_Type = InetAddressType
_CgprsAccPtNetbiosServerAddrType_Object = MibTableColumn
cgprsAccPtNetbiosServerAddrType = _CgprsAccPtNetbiosServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 4, 1, 1, 4),
    _CgprsAccPtNetbiosServerAddrType_Type()
)
cgprsAccPtNetbiosServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtNetbiosServerAddrType.setStatus("current")
_CgprsAccPtPriNetbiosServer_Type = InetAddress
_CgprsAccPtPriNetbiosServer_Object = MibTableColumn
cgprsAccPtPriNetbiosServer = _CgprsAccPtPriNetbiosServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 4, 1, 1, 5),
    _CgprsAccPtPriNetbiosServer_Type()
)
cgprsAccPtPriNetbiosServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPriNetbiosServer.setStatus("current")
_CgprsAccPtSecNetbiosServer_Type = InetAddress
_CgprsAccPtSecNetbiosServer_Object = MibTableColumn
cgprsAccPtSecNetbiosServer = _CgprsAccPtSecNetbiosServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 4, 1, 1, 6),
    _CgprsAccPtSecNetbiosServer_Type()
)
cgprsAccPtSecNetbiosServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtSecNetbiosServer.setStatus("current")
_CgprsAccPtImsConfigs_ObjectIdentity = ObjectIdentity
cgprsAccPtImsConfigs = _CgprsAccPtImsConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 5)
)
_CgprsAccPtImsConfigTable_Object = MibTable
cgprsAccPtImsConfigTable = _CgprsAccPtImsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtImsConfigTable.setStatus("deprecated")
_CgprsAccPtImsConfigEntry_Object = MibTableRow
cgprsAccPtImsConfigEntry = _CgprsAccPtImsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtImsConfigEntry.setStatus("deprecated")


class _CgprsAccPtImsEnable_Type(Bits):
    """Custom type cgprsAccPtImsEnable based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("exclusive", 2),
          ("transformPrimary", 3))
    )

_CgprsAccPtImsEnable_Type.__name__ = "Bits"
_CgprsAccPtImsEnable_Object = MibTableColumn
cgprsAccPtImsEnable = _CgprsAccPtImsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 5, 1, 1, 1),
    _CgprsAccPtImsEnable_Type()
)
cgprsAccPtImsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtImsEnable.setStatus("deprecated")


class _CgprsAccPtPCscfGroupName_Type(SnmpAdminString):
    """Custom type cgprsAccPtPCscfGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CgprsAccPtPCscfGroupName_Type.__name__ = "SnmpAdminString"
_CgprsAccPtPCscfGroupName_Object = MibTableColumn
cgprsAccPtPCscfGroupName = _CgprsAccPtPCscfGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 5, 1, 1, 2),
    _CgprsAccPtPCscfGroupName_Type()
)
cgprsAccPtPCscfGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtPCscfGroupName.setStatus("deprecated")


class _CgprsAccPtImsSigAccGroupIn_Type(AccessControlListOrZero):
    """Custom type cgprsAccPtImsSigAccGroupIn based on AccessControlListOrZero"""
    defaultValue = 0


_CgprsAccPtImsSigAccGroupIn_Object = MibTableColumn
cgprsAccPtImsSigAccGroupIn = _CgprsAccPtImsSigAccGroupIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 5, 1, 1, 3),
    _CgprsAccPtImsSigAccGroupIn_Type()
)
cgprsAccPtImsSigAccGroupIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtImsSigAccGroupIn.setStatus("deprecated")


class _CgprsAccPtImsSigAccGroupOut_Type(AccessControlListOrZero):
    """Custom type cgprsAccPtImsSigAccGroupOut based on AccessControlListOrZero"""
    defaultValue = 0


_CgprsAccPtImsSigAccGroupOut_Object = MibTableColumn
cgprsAccPtImsSigAccGroupOut = _CgprsAccPtImsSigAccGroupOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 5, 1, 1, 4),
    _CgprsAccPtImsSigAccGroupOut_Type()
)
cgprsAccPtImsSigAccGroupOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtImsSigAccGroupOut.setStatus("deprecated")


class _CgprsAccPtRejNonImsPdp_Type(TruthValue):
    """Custom type cgprsAccPtRejNonImsPdp based on TruthValue"""


_CgprsAccPtRejNonImsPdp_Object = MibTableColumn
cgprsAccPtRejNonImsPdp = _CgprsAccPtRejNonImsPdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 5, 1, 1, 5),
    _CgprsAccPtRejNonImsPdp_Type()
)
cgprsAccPtRejNonImsPdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRejNonImsPdp.setStatus("deprecated")
_CgprsAccPtChargingParams_ObjectIdentity = ObjectIdentity
cgprsAccPtChargingParams = _CgprsAccPtChargingParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 6)
)
_CgprsAccPtChgProfTable_Object = MibTable
cgprsAccPtChgProfTable = _CgprsAccPtChgProfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtChgProfTable.setStatus("current")
_CgprsAccPtChgProfEntry_Object = MibTableRow
cgprsAccPtChgProfEntry = _CgprsAccPtChgProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 6, 1, 1)
)
cgprsAccPtChgProfEntry.setIndexNames(
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIndex"),
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsType"),
)
if mibBuilder.loadTexts:
    cgprsAccPtChgProfEntry.setStatus("current")


class _CgprsAccPtMsType_Type(Integer32):
    """Custom type cgprsAccPtMsType based on Integer32"""
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
        *(("all", 1),
          ("home", 2),
          ("roaming", 3),
          ("roamingTrusted", 4),
          ("visiting", 5),
          ("visitingTrusted", 6))
    )


_CgprsAccPtMsType_Type.__name__ = "Integer32"
_CgprsAccPtMsType_Object = MibTableColumn
cgprsAccPtMsType = _CgprsAccPtMsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 6, 1, 1, 1),
    _CgprsAccPtMsType_Type()
)
cgprsAccPtMsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsAccPtMsType.setStatus("current")
_CgprsAccPtChgProfile_Type = Unsigned32
_CgprsAccPtChgProfile_Object = MibTableColumn
cgprsAccPtChgProfile = _CgprsAccPtChgProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 6, 1, 1, 2),
    _CgprsAccPtChgProfile_Type()
)
cgprsAccPtChgProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtChgProfile.setStatus("current")


class _CgprsAccPtChgProfOverride_Type(TruthValue):
    """Custom type cgprsAccPtChgProfOverride based on TruthValue"""


_CgprsAccPtChgProfOverride_Object = MibTableColumn
cgprsAccPtChgProfOverride = _CgprsAccPtChgProfOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 6, 1, 1, 3),
    _CgprsAccPtChgProfOverride_Type()
)
cgprsAccPtChgProfOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtChgProfOverride.setStatus("current")
_CgprsAccPtChgProfRowStatus_Type = RowStatus
_CgprsAccPtChgProfRowStatus_Object = MibTableColumn
cgprsAccPtChgProfRowStatus = _CgprsAccPtChgProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 6, 1, 1, 4),
    _CgprsAccPtChgProfRowStatus_Type()
)
cgprsAccPtChgProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtChgProfRowStatus.setStatus("current")
_CgprsAccPtCacConfigs_ObjectIdentity = ObjectIdentity
cgprsAccPtCacConfigs = _CgprsAccPtCacConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 7)
)
_CgprsAccPtCacTable_Object = MibTable
cgprsAccPtCacTable = _CgprsAccPtCacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtCacTable.setStatus("current")
_CgprsAccPtCacEntry_Object = MibTableRow
cgprsAccPtCacEntry = _CgprsAccPtCacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtCacEntry.setStatus("current")


class _CgprsAccPtCacPolicyName_Type(SnmpAdminString):
    """Custom type cgprsAccPtCacPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CgprsAccPtCacPolicyName_Type.__name__ = "SnmpAdminString"
_CgprsAccPtCacPolicyName_Object = MibTableColumn
cgprsAccPtCacPolicyName = _CgprsAccPtCacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 7, 1, 1, 1),
    _CgprsAccPtCacPolicyName_Type()
)
cgprsAccPtCacPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtCacPolicyName.setStatus("current")


class _CgprsAccPtCacUpStrBandWidthPool_Type(SnmpAdminString):
    """Custom type cgprsAccPtCacUpStrBandWidthPool based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CgprsAccPtCacUpStrBandWidthPool_Type.__name__ = "SnmpAdminString"
_CgprsAccPtCacUpStrBandWidthPool_Object = MibTableColumn
cgprsAccPtCacUpStrBandWidthPool = _CgprsAccPtCacUpStrBandWidthPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 7, 1, 1, 2),
    _CgprsAccPtCacUpStrBandWidthPool_Type()
)
cgprsAccPtCacUpStrBandWidthPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtCacUpStrBandWidthPool.setStatus("current")


class _CgprsAccPtCacDnStrBandWidthPool_Type(SnmpAdminString):
    """Custom type cgprsAccPtCacDnStrBandWidthPool based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CgprsAccPtCacDnStrBandWidthPool_Type.__name__ = "SnmpAdminString"
_CgprsAccPtCacDnStrBandWidthPool_Object = MibTableColumn
cgprsAccPtCacDnStrBandWidthPool = _CgprsAccPtCacDnStrBandWidthPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 7, 1, 1, 3),
    _CgprsAccPtCacDnStrBandWidthPool_Type()
)
cgprsAccPtCacDnStrBandWidthPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtCacDnStrBandWidthPool.setStatus("current")
_CgprsAccPtRouteProbeConfigs_ObjectIdentity = ObjectIdentity
cgprsAccPtRouteProbeConfigs = _CgprsAccPtRouteProbeConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 8)
)
_CgprsAccPtRouteProbeTable_Object = MibTable
cgprsAccPtRouteProbeTable = _CgprsAccPtRouteProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtRouteProbeTable.setStatus("current")
_CgprsAccPtRouteProbeEntry_Object = MibTableRow
cgprsAccPtRouteProbeEntry = _CgprsAccPtRouteProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtRouteProbeEntry.setStatus("current")
_CgprsAccPtRpDestAddrType_Type = InetAddressType
_CgprsAccPtRpDestAddrType_Object = MibTableColumn
cgprsAccPtRpDestAddrType = _CgprsAccPtRpDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 8, 1, 1, 1),
    _CgprsAccPtRpDestAddrType_Type()
)
cgprsAccPtRpDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRpDestAddrType.setStatus("current")
_CgprsAccPtRpDestAddr_Type = InetAddress
_CgprsAccPtRpDestAddr_Object = MibTableColumn
cgprsAccPtRpDestAddr = _CgprsAccPtRpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 8, 1, 1, 2),
    _CgprsAccPtRpDestAddr_Type()
)
cgprsAccPtRpDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRpDestAddr.setStatus("current")


class _CgprsAccPtRpProtocol_Type(Integer32):
    """Custom type cgprsAccPtRpProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 2),
          ("udp", 1))
    )


_CgprsAccPtRpProtocol_Type.__name__ = "Integer32"
_CgprsAccPtRpProtocol_Object = MibTableColumn
cgprsAccPtRpProtocol = _CgprsAccPtRpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 8, 1, 1, 3),
    _CgprsAccPtRpProtocol_Type()
)
cgprsAccPtRpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRpProtocol.setStatus("current")


class _CgprsAccPtRpDestPort_Type(InetPortNumber):
    """Custom type cgprsAccPtRpDestPort based on InetPortNumber"""
    defaultValue = 9


_CgprsAccPtRpDestPort_Object = MibTableColumn
cgprsAccPtRpDestPort = _CgprsAccPtRpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 8, 1, 1, 4),
    _CgprsAccPtRpDestPort_Type()
)
cgprsAccPtRpDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRpDestPort.setStatus("current")


class _CgprsAccPtRpTtl_Type(Unsigned32):
    """Custom type cgprsAccPtRpTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CgprsAccPtRpTtl_Type.__name__ = "Unsigned32"
_CgprsAccPtRpTtl_Object = MibTableColumn
cgprsAccPtRpTtl = _CgprsAccPtRpTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 8, 1, 1, 5),
    _CgprsAccPtRpTtl_Type()
)
cgprsAccPtRpTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtRpTtl.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtRpTtl.setUnits("seconds")
_CgprsAccPtIpv6Configs_ObjectIdentity = ObjectIdentity
cgprsAccPtIpv6Configs = _CgprsAccPtIpv6Configs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9)
)
_CgprsAccPtIpv6Table_Object = MibTable
cgprsAccPtIpv6Table = _CgprsAccPtIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtIpv6Table.setStatus("current")
_CgprsAccPtIpv6Entry_Object = MibTableRow
cgprsAccPtIpv6Entry = _CgprsAccPtIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtIpv6Entry.setStatus("current")
_CgprsAccPtIpv6BaseVTemplate_Type = Unsigned32
_CgprsAccPtIpv6BaseVTemplate_Object = MibTableColumn
cgprsAccPtIpv6BaseVTemplate = _CgprsAccPtIpv6BaseVTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 1),
    _CgprsAccPtIpv6BaseVTemplate_Type()
)
cgprsAccPtIpv6BaseVTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6BaseVTemplate.setStatus("current")
_CgprsAccPtIpv6DnsAddrType_Type = InetAddressType
_CgprsAccPtIpv6DnsAddrType_Object = MibTableColumn
cgprsAccPtIpv6DnsAddrType = _CgprsAccPtIpv6DnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 2),
    _CgprsAccPtIpv6DnsAddrType_Type()
)
cgprsAccPtIpv6DnsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6DnsAddrType.setStatus("current")
_CgprsAccPtIpv6DnsPriAddress_Type = InetAddress
_CgprsAccPtIpv6DnsPriAddress_Object = MibTableColumn
cgprsAccPtIpv6DnsPriAddress = _CgprsAccPtIpv6DnsPriAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 3),
    _CgprsAccPtIpv6DnsPriAddress_Type()
)
cgprsAccPtIpv6DnsPriAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6DnsPriAddress.setStatus("current")
_CgprsAccPtIpv6DnsSecAddress_Type = InetAddress
_CgprsAccPtIpv6DnsSecAddress_Object = MibTableColumn
cgprsAccPtIpv6DnsSecAddress = _CgprsAccPtIpv6DnsSecAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 4),
    _CgprsAccPtIpv6DnsSecAddress_Type()
)
cgprsAccPtIpv6DnsSecAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6DnsSecAddress.setStatus("current")
_CgprsAccPtIpv6Enable_Type = TruthValue
_CgprsAccPtIpv6Enable_Object = MibTableColumn
cgprsAccPtIpv6Enable = _CgprsAccPtIpv6Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 5),
    _CgprsAccPtIpv6Enable_Type()
)
cgprsAccPtIpv6Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6Enable.setStatus("current")
_CgprsAccPtIpv6Exclusive_Type = TruthValue
_CgprsAccPtIpv6Exclusive_Object = MibTableColumn
cgprsAccPtIpv6Exclusive = _CgprsAccPtIpv6Exclusive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 6),
    _CgprsAccPtIpv6Exclusive_Type()
)
cgprsAccPtIpv6Exclusive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6Exclusive.setStatus("current")
_CgprsAccPtIpv6AccessGroupDown_Type = AccessControlListName
_CgprsAccPtIpv6AccessGroupDown_Object = MibTableColumn
cgprsAccPtIpv6AccessGroupDown = _CgprsAccPtIpv6AccessGroupDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 7),
    _CgprsAccPtIpv6AccessGroupDown_Type()
)
cgprsAccPtIpv6AccessGroupDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6AccessGroupDown.setStatus("current")
_CgprsAccPtIpv6AccessGroupUp_Type = AccessControlListName
_CgprsAccPtIpv6AccessGroupUp_Object = MibTableColumn
cgprsAccPtIpv6AccessGroupUp = _CgprsAccPtIpv6AccessGroupUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 8),
    _CgprsAccPtIpv6AccessGroupUp_Type()
)
cgprsAccPtIpv6AccessGroupUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6AccessGroupUp.setStatus("current")


class _CgprsAccPtIpv6AddrPool_Type(Integer32):
    """Custom type cgprsAccPtIpv6AddrPool based on Integer32"""
    defaultValue = 1

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
        *(("dhcp", 2),
          ("disable", 3),
          ("global", 1),
          ("local", 4),
          ("radius", 5))
    )


_CgprsAccPtIpv6AddrPool_Type.__name__ = "Integer32"
_CgprsAccPtIpv6AddrPool_Object = MibTableColumn
cgprsAccPtIpv6AddrPool = _CgprsAccPtIpv6AddrPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 9),
    _CgprsAccPtIpv6AddrPool_Type()
)
cgprsAccPtIpv6AddrPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6AddrPool.setStatus("current")
_CgprsAccPtIpv6AddrLocalPoolName_Type = SnmpAdminString
_CgprsAccPtIpv6AddrLocalPoolName_Object = MibTableColumn
cgprsAccPtIpv6AddrLocalPoolName = _CgprsAccPtIpv6AddrLocalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 10),
    _CgprsAccPtIpv6AddrLocalPoolName_Type()
)
cgprsAccPtIpv6AddrLocalPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6AddrLocalPoolName.setStatus("current")


class _CgprsAccPtIpv6Redirect_Type(Integer32):
    """Custom type cgprsAccPtIpv6Redirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("intermobile", 2),
          ("none", 0))
    )


_CgprsAccPtIpv6Redirect_Type.__name__ = "Integer32"
_CgprsAccPtIpv6Redirect_Object = MibTableColumn
cgprsAccPtIpv6Redirect = _CgprsAccPtIpv6Redirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 11),
    _CgprsAccPtIpv6Redirect_Type()
)
cgprsAccPtIpv6Redirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6Redirect.setStatus("current")
_CgprsAccPtIpv6RedirectAddrType_Type = InetAddressType
_CgprsAccPtIpv6RedirectAddrType_Object = MibTableColumn
cgprsAccPtIpv6RedirectAddrType = _CgprsAccPtIpv6RedirectAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 12),
    _CgprsAccPtIpv6RedirectAddrType_Type()
)
cgprsAccPtIpv6RedirectAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6RedirectAddrType.setStatus("current")
_CgprsAccPtIpv6RedirectAddr_Type = InetAddress
_CgprsAccPtIpv6RedirectAddr_Object = MibTableColumn
cgprsAccPtIpv6RedirectAddr = _CgprsAccPtIpv6RedirectAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 13),
    _CgprsAccPtIpv6RedirectAddr_Type()
)
cgprsAccPtIpv6RedirectAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6RedirectAddr.setStatus("current")


class _CgprsAccPtIpv6SecurityVerifySrc_Type(TruthValue):
    """Custom type cgprsAccPtIpv6SecurityVerifySrc based on TruthValue"""


_CgprsAccPtIpv6SecurityVerifySrc_Object = MibTableColumn
cgprsAccPtIpv6SecurityVerifySrc = _CgprsAccPtIpv6SecurityVerifySrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 14),
    _CgprsAccPtIpv6SecurityVerifySrc_Type()
)
cgprsAccPtIpv6SecurityVerifySrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6SecurityVerifySrc.setStatus("current")


class _CgprsAccPtIpv6SecurityVerifyDst_Type(TruthValue):
    """Custom type cgprsAccPtIpv6SecurityVerifyDst based on TruthValue"""


_CgprsAccPtIpv6SecurityVerifyDst_Object = MibTableColumn
cgprsAccPtIpv6SecurityVerifyDst = _CgprsAccPtIpv6SecurityVerifyDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 15),
    _CgprsAccPtIpv6SecurityVerifyDst_Type()
)
cgprsAccPtIpv6SecurityVerifyDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6SecurityVerifyDst.setStatus("current")
_CgprsAccPtIpv6AddrAllocations_Type = Gauge32
_CgprsAccPtIpv6AddrAllocations_Object = MibTableColumn
cgprsAccPtIpv6AddrAllocations = _CgprsAccPtIpv6AddrAllocations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 16),
    _CgprsAccPtIpv6AddrAllocations_Type()
)
cgprsAccPtIpv6AddrAllocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6AddrAllocations.setStatus("current")
_CgprsAccPtDhcpv6ProxClientIntf_Type = InterfaceIndexOrZero
_CgprsAccPtDhcpv6ProxClientIntf_Object = MibTableColumn
cgprsAccPtDhcpv6ProxClientIntf = _CgprsAccPtDhcpv6ProxClientIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 17),
    _CgprsAccPtDhcpv6ProxClientIntf_Type()
)
cgprsAccPtDhcpv6ProxClientIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxClientIntf.setStatus("current")
_CgprsAccptDhcpv6RapidCommit_Type = TruthValue
_CgprsAccptDhcpv6RapidCommit_Object = MibTableColumn
cgprsAccptDhcpv6RapidCommit = _CgprsAccptDhcpv6RapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 18),
    _CgprsAccptDhcpv6RapidCommit_Type()
)
cgprsAccptDhcpv6RapidCommit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccptDhcpv6RapidCommit.setStatus("current")


class _CgprsAccptDhcpv6PoolName_Type(SnmpAdminString):
    """Custom type cgprsAccptDhcpv6PoolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CgprsAccptDhcpv6PoolName_Type.__name__ = "SnmpAdminString"
_CgprsAccptDhcpv6PoolName_Object = MibTableColumn
cgprsAccptDhcpv6PoolName = _CgprsAccptDhcpv6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 9, 1, 1, 19),
    _CgprsAccptDhcpv6PoolName_Type()
)
cgprsAccptDhcpv6PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccptDhcpv6PoolName.setStatus("current")
_CgprsAccPtCsgGroupTable_Object = MibTable
cgprsAccPtCsgGroupTable = _CgprsAccPtCsgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cgprsAccPtCsgGroupTable.setStatus("current")
_CgprsAccPtCsgGroupEntry_Object = MibTableRow
cgprsAccPtCsgGroupEntry = _CgprsAccPtCsgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 10, 1)
)
cgprsAccPtCsgGroupEntry.setIndexNames(
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIndex"),
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCsgGroupName"),
)
if mibBuilder.loadTexts:
    cgprsAccPtCsgGroupEntry.setStatus("current")
_CgprsAccPtCsgGroupName_Type = SnmpAdminString
_CgprsAccPtCsgGroupName_Object = MibTableColumn
cgprsAccPtCsgGroupName = _CgprsAccPtCsgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 10, 1, 1),
    _CgprsAccPtCsgGroupName_Type()
)
cgprsAccPtCsgGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsAccPtCsgGroupName.setStatus("current")
_CgprsAccPtCsgGroupRowStatus_Type = RowStatus
_CgprsAccPtCsgGroupRowStatus_Object = MibTableColumn
cgprsAccPtCsgGroupRowStatus = _CgprsAccPtCsgGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 1, 10, 1, 2),
    _CgprsAccPtCsgGroupRowStatus_Type()
)
cgprsAccPtCsgGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsAccPtCsgGroupRowStatus.setStatus("current")
_CiscoGprsAccPtCfgNotifInfo_ObjectIdentity = ObjectIdentity
ciscoGprsAccPtCfgNotifInfo = _CiscoGprsAccPtCfgNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 2)
)
_CgprsAccPtCfgNotifHistTable_Object = MibTable
cgprsAccPtCfgNotifHistTable = _CgprsAccPtCfgNotifHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotifHistTable.setStatus("current")
_CgprsAccPtCfgNotifHistEntry_Object = MibTableRow
cgprsAccPtCfgNotifHistEntry = _CgprsAccPtCfgNotifHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 2, 1, 1)
)
cgprsAccPtCfgNotifHistEntry.setIndexNames(
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifIndex"),
)
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotifHistEntry.setStatus("current")


class _CgprsAccPtCfgNotifIndex_Type(Unsigned32):
    """Custom type cgprsAccPtCfgNotifIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsAccPtCfgNotifIndex_Type.__name__ = "Unsigned32"
_CgprsAccPtCfgNotifIndex_Object = MibTableColumn
cgprsAccPtCfgNotifIndex = _CgprsAccPtCfgNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 2, 1, 1, 1),
    _CgprsAccPtCfgNotifIndex_Type()
)
cgprsAccPtCfgNotifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotifIndex.setStatus("current")


class _CgprsAccPtCfgNotifAccPtIndex_Type(Unsigned32):
    """Custom type cgprsAccPtCfgNotifAccPtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgprsAccPtCfgNotifAccPtIndex_Type.__name__ = "Unsigned32"
_CgprsAccPtCfgNotifAccPtIndex_Object = MibTableColumn
cgprsAccPtCfgNotifAccPtIndex = _CgprsAccPtCfgNotifAccPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 2, 1, 1, 2),
    _CgprsAccPtCfgNotifAccPtIndex_Type()
)
cgprsAccPtCfgNotifAccPtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotifAccPtIndex.setStatus("current")


class _CgprsAccPtCfgNotifReason_Type(Integer32):
    """Custom type cgprsAccPtCfgNotifReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("creation", 2),
          ("deletion", 3),
          ("modification", 1))
    )


_CgprsAccPtCfgNotifReason_Type.__name__ = "Integer32"
_CgprsAccPtCfgNotifReason_Object = MibTableColumn
cgprsAccPtCfgNotifReason = _CgprsAccPtCfgNotifReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 2, 1, 1, 3),
    _CgprsAccPtCfgNotifReason_Type()
)
cgprsAccPtCfgNotifReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotifReason.setStatus("current")


class _CgprsAccPtCfgNotifEnable_Type(TruthValue):
    """Custom type cgprsAccPtCfgNotifEnable based on TruthValue"""


_CgprsAccPtCfgNotifEnable_Object = MibScalar
cgprsAccPtCfgNotifEnable = _CgprsAccPtCfgNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 2, 2),
    _CgprsAccPtCfgNotifEnable_Type()
)
cgprsAccPtCfgNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotifEnable.setStatus("current")


class _CgprsAccPtCfgNotifHistMax_Type(Unsigned32):
    """Custom type cgprsAccPtCfgNotifHistMax based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_CgprsAccPtCfgNotifHistMax_Type.__name__ = "Unsigned32"
_CgprsAccPtCfgNotifHistMax_Object = MibScalar
cgprsAccPtCfgNotifHistMax = _CgprsAccPtCfgNotifHistMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 2, 3),
    _CgprsAccPtCfgNotifHistMax_Type()
)
cgprsAccPtCfgNotifHistMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotifHistMax.setStatus("current")


class _CgprsAccPtCfgNotifLatestIndex_Type(Unsigned32):
    """Custom type cgprsAccPtCfgNotifLatestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgprsAccPtCfgNotifLatestIndex_Type.__name__ = "Unsigned32"
_CgprsAccPtCfgNotifLatestIndex_Object = MibScalar
cgprsAccPtCfgNotifLatestIndex = _CgprsAccPtCfgNotifLatestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 2, 4),
    _CgprsAccPtCfgNotifLatestIndex_Type()
)
cgprsAccPtCfgNotifLatestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotifLatestIndex.setStatus("current")
_CiscoGprsAccPtStatistics_ObjectIdentity = ObjectIdentity
ciscoGprsAccPtStatistics = _CiscoGprsAccPtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3)
)
_CgprsAccPtStatisticsTable_Object = MibTable
cgprsAccPtStatisticsTable = _CgprsAccPtStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsTable.setStatus("current")
_CgprsAccPtStatisticsEntry_Object = MibTableRow
cgprsAccPtStatisticsEntry = _CgprsAccPtStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsEntry.setStatus("current")
_CgprsAccPtMsActivatedPdps_Type = Counter32
_CgprsAccPtMsActivatedPdps_Object = MibTableColumn
cgprsAccPtMsActivatedPdps = _CgprsAccPtMsActivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 1),
    _CgprsAccPtMsActivatedPdps_Type()
)
cgprsAccPtMsActivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtMsActivatedPdps.setStatus("current")
_CgprsAccPtSuccMsActivatedPdps_Type = Counter32
_CgprsAccPtSuccMsActivatedPdps_Object = MibTableColumn
cgprsAccPtSuccMsActivatedPdps = _CgprsAccPtSuccMsActivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 2),
    _CgprsAccPtSuccMsActivatedPdps_Type()
)
cgprsAccPtSuccMsActivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccMsActivatedPdps.setStatus("current")
_CgprsAccPtMsActivatedDynPdps_Type = Counter32
_CgprsAccPtMsActivatedDynPdps_Object = MibTableColumn
cgprsAccPtMsActivatedDynPdps = _CgprsAccPtMsActivatedDynPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 3),
    _CgprsAccPtMsActivatedDynPdps_Type()
)
cgprsAccPtMsActivatedDynPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtMsActivatedDynPdps.setStatus("current")
_CgprsAccPtSuccMsActivatedDynPdps_Type = Counter32
_CgprsAccPtSuccMsActivatedDynPdps_Object = MibTableColumn
cgprsAccPtSuccMsActivatedDynPdps = _CgprsAccPtSuccMsActivatedDynPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 4),
    _CgprsAccPtSuccMsActivatedDynPdps_Type()
)
cgprsAccPtSuccMsActivatedDynPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccMsActivatedDynPdps.setStatus("current")
_CgprsAccPtMsDeactivatedPdps_Type = Counter32
_CgprsAccPtMsDeactivatedPdps_Object = MibTableColumn
cgprsAccPtMsDeactivatedPdps = _CgprsAccPtMsDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 5),
    _CgprsAccPtMsDeactivatedPdps_Type()
)
cgprsAccPtMsDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtMsDeactivatedPdps.setStatus("current")
_CgprsAccPtSuccMsDeactivatedPdps_Type = Counter32
_CgprsAccPtSuccMsDeactivatedPdps_Object = MibTableColumn
cgprsAccPtSuccMsDeactivatedPdps = _CgprsAccPtSuccMsDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 6),
    _CgprsAccPtSuccMsDeactivatedPdps_Type()
)
cgprsAccPtSuccMsDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccMsDeactivatedPdps.setStatus("current")
_CgprsAccPtNetworkInitPdps_Type = Counter32
_CgprsAccPtNetworkInitPdps_Object = MibTableColumn
cgprsAccPtNetworkInitPdps = _CgprsAccPtNetworkInitPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 7),
    _CgprsAccPtNetworkInitPdps_Type()
)
cgprsAccPtNetworkInitPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtNetworkInitPdps.setStatus("current")
_CgprsAccPtSuccNetworkInitPdps_Type = Counter32
_CgprsAccPtSuccNetworkInitPdps_Object = MibTableColumn
cgprsAccPtSuccNetworkInitPdps = _CgprsAccPtSuccNetworkInitPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 8),
    _CgprsAccPtSuccNetworkInitPdps_Type()
)
cgprsAccPtSuccNetworkInitPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccNetworkInitPdps.setStatus("current")
_CgprsAccPtGgsnDeactivatedPdps_Type = Counter32
_CgprsAccPtGgsnDeactivatedPdps_Object = MibTableColumn
cgprsAccPtGgsnDeactivatedPdps = _CgprsAccPtGgsnDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 9),
    _CgprsAccPtGgsnDeactivatedPdps_Type()
)
cgprsAccPtGgsnDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtGgsnDeactivatedPdps.setStatus("current")
_CgprsAccPtSuccGgsDeactivatedPdps_Type = Counter32
_CgprsAccPtSuccGgsDeactivatedPdps_Object = MibTableColumn
cgprsAccPtSuccGgsDeactivatedPdps = _CgprsAccPtSuccGgsDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 10),
    _CgprsAccPtSuccGgsDeactivatedPdps_Type()
)
cgprsAccPtSuccGgsDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccGgsDeactivatedPdps.setStatus("current")
_CgprsAccPtActivePdps_Type = Gauge32
_CgprsAccPtActivePdps_Object = MibTableColumn
cgprsAccPtActivePdps = _CgprsAccPtActivePdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 11),
    _CgprsAccPtActivePdps_Type()
)
cgprsAccPtActivePdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtActivePdps.setStatus("current")
_CgprsAccPtUpstreamTrafficVol_Type = Counter32
_CgprsAccPtUpstreamTrafficVol_Object = MibTableColumn
cgprsAccPtUpstreamTrafficVol = _CgprsAccPtUpstreamTrafficVol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 12),
    _CgprsAccPtUpstreamTrafficVol_Type()
)
cgprsAccPtUpstreamTrafficVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtUpstreamTrafficVol.setStatus("deprecated")
if mibBuilder.loadTexts:
    cgprsAccPtUpstreamTrafficVol.setUnits("bytes")
_CgprsAccPtDownstreamTrafficVol_Type = Counter32
_CgprsAccPtDownstreamTrafficVol_Object = MibTableColumn
cgprsAccPtDownstreamTrafficVol = _CgprsAccPtDownstreamTrafficVol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 13),
    _CgprsAccPtDownstreamTrafficVol_Type()
)
cgprsAccPtDownstreamTrafficVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDownstreamTrafficVol.setStatus("deprecated")
if mibBuilder.loadTexts:
    cgprsAccPtDownstreamTrafficVol.setUnits("bytes")
_CgprsAccPtSourceAddrViolTpdus_Type = Counter32
_CgprsAccPtSourceAddrViolTpdus_Object = MibTableColumn
cgprsAccPtSourceAddrViolTpdus = _CgprsAccPtSourceAddrViolTpdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 14),
    _CgprsAccPtSourceAddrViolTpdus_Type()
)
cgprsAccPtSourceAddrViolTpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSourceAddrViolTpdus.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtSourceAddrViolTpdus.setUnits("packets")
_CgprsAccPtDestAddrViolTpdus_Type = Counter32
_CgprsAccPtDestAddrViolTpdus_Object = MibTableColumn
cgprsAccPtDestAddrViolTpdus = _CgprsAccPtDestAddrViolTpdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 15),
    _CgprsAccPtDestAddrViolTpdus_Type()
)
cgprsAccPtDestAddrViolTpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDestAddrViolTpdus.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtDestAddrViolTpdus.setUnits("packets")
_CgprsAccPtRedirInterMobilTraffic_Type = Counter32
_CgprsAccPtRedirInterMobilTraffic_Object = MibTableColumn
cgprsAccPtRedirInterMobilTraffic = _CgprsAccPtRedirInterMobilTraffic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 16),
    _CgprsAccPtRedirInterMobilTraffic_Type()
)
cgprsAccPtRedirInterMobilTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtRedirInterMobilTraffic.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtRedirInterMobilTraffic.setUnits("packets")
_CgprsAccPtRevUpstreamTrafficVol_Type = Counter64
_CgprsAccPtRevUpstreamTrafficVol_Object = MibTableColumn
cgprsAccPtRevUpstreamTrafficVol = _CgprsAccPtRevUpstreamTrafficVol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 17),
    _CgprsAccPtRevUpstreamTrafficVol_Type()
)
cgprsAccPtRevUpstreamTrafficVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtRevUpstreamTrafficVol.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtRevUpstreamTrafficVol.setUnits("bytes")
_CgprsAccPtRevDownstrTrafficVol_Type = Counter64
_CgprsAccPtRevDownstrTrafficVol_Object = MibTableColumn
cgprsAccPtRevDownstrTrafficVol = _CgprsAccPtRevDownstrTrafficVol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 18),
    _CgprsAccPtRevDownstrTrafficVol_Type()
)
cgprsAccPtRevDownstrTrafficVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtRevDownstrTrafficVol.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtRevDownstrTrafficVol.setUnits("bytes")
_CgprsAccPtUpstreamPacketCount_Type = Counter32
_CgprsAccPtUpstreamPacketCount_Object = MibTableColumn
cgprsAccPtUpstreamPacketCount = _CgprsAccPtUpstreamPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 19),
    _CgprsAccPtUpstreamPacketCount_Type()
)
cgprsAccPtUpstreamPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtUpstreamPacketCount.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtUpstreamPacketCount.setUnits("packets")
_CgprsAccPtDownstreamPacketCount_Type = Counter32
_CgprsAccPtDownstreamPacketCount_Object = MibTableColumn
cgprsAccPtDownstreamPacketCount = _CgprsAccPtDownstreamPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 20),
    _CgprsAccPtDownstreamPacketCount_Type()
)
cgprsAccPtDownstreamPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDownstreamPacketCount.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtDownstreamPacketCount.setUnits("packets")
_CgprsAccPtDhcpAddrRequests_Type = Counter32
_CgprsAccPtDhcpAddrRequests_Object = MibTableColumn
cgprsAccPtDhcpAddrRequests = _CgprsAccPtDhcpAddrRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 21),
    _CgprsAccPtDhcpAddrRequests_Type()
)
cgprsAccPtDhcpAddrRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpAddrRequests.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpAddrRequests.setUnits("packets")
_CgprsAccPtSuccDhcpAddrRequests_Type = Counter32
_CgprsAccPtSuccDhcpAddrRequests_Object = MibTableColumn
cgprsAccPtSuccDhcpAddrRequests = _CgprsAccPtSuccDhcpAddrRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 22),
    _CgprsAccPtSuccDhcpAddrRequests_Type()
)
cgprsAccPtSuccDhcpAddrRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccDhcpAddrRequests.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtSuccDhcpAddrRequests.setUnits("packets")
_CgprsAccPtDhcpAddrReleases_Type = Counter32
_CgprsAccPtDhcpAddrReleases_Object = MibTableColumn
cgprsAccPtDhcpAddrReleases = _CgprsAccPtDhcpAddrReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 23),
    _CgprsAccPtDhcpAddrReleases_Type()
)
cgprsAccPtDhcpAddrReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpAddrReleases.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpAddrReleases.setUnits("packets")
_CgprsAccPtIpv6MsActivatedPdps_Type = Counter32
_CgprsAccPtIpv6MsActivatedPdps_Object = MibTableColumn
cgprsAccPtIpv6MsActivatedPdps = _CgprsAccPtIpv6MsActivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 24),
    _CgprsAccPtIpv6MsActivatedPdps_Type()
)
cgprsAccPtIpv6MsActivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6MsActivatedPdps.setStatus("current")
_CgprsAccPtIpv6MsSuccActivatedPdps_Type = Counter32
_CgprsAccPtIpv6MsSuccActivatedPdps_Object = MibTableColumn
cgprsAccPtIpv6MsSuccActivatedPdps = _CgprsAccPtIpv6MsSuccActivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 25),
    _CgprsAccPtIpv6MsSuccActivatedPdps_Type()
)
cgprsAccPtIpv6MsSuccActivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6MsSuccActivatedPdps.setStatus("current")
_CgprsAccPtIpv6NetworkInitDeactPdps_Type = Counter32
_CgprsAccPtIpv6NetworkInitDeactPdps_Object = MibTableColumn
cgprsAccPtIpv6NetworkInitDeactPdps = _CgprsAccPtIpv6NetworkInitDeactPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 26),
    _CgprsAccPtIpv6NetworkInitDeactPdps_Type()
)
cgprsAccPtIpv6NetworkInitDeactPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6NetworkInitDeactPdps.setStatus("current")
_CgprsAccPtIpv6NetworkInitDeactSuccPdps_Type = Counter32
_CgprsAccPtIpv6NetworkInitDeactSuccPdps_Object = MibTableColumn
cgprsAccPtIpv6NetworkInitDeactSuccPdps = _CgprsAccPtIpv6NetworkInitDeactSuccPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 27),
    _CgprsAccPtIpv6NetworkInitDeactSuccPdps_Type()
)
cgprsAccPtIpv6NetworkInitDeactSuccPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6NetworkInitDeactSuccPdps.setStatus("current")
_CgprsAccPtIpv6MsActivatedDynPdps_Type = Counter32
_CgprsAccPtIpv6MsActivatedDynPdps_Object = MibTableColumn
cgprsAccPtIpv6MsActivatedDynPdps = _CgprsAccPtIpv6MsActivatedDynPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 28),
    _CgprsAccPtIpv6MsActivatedDynPdps_Type()
)
cgprsAccPtIpv6MsActivatedDynPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6MsActivatedDynPdps.setStatus("current")
_CgprsAccPtIpv6MsSuccActivatedDynPdps_Type = Counter32
_CgprsAccPtIpv6MsSuccActivatedDynPdps_Object = MibTableColumn
cgprsAccPtIpv6MsSuccActivatedDynPdps = _CgprsAccPtIpv6MsSuccActivatedDynPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 29),
    _CgprsAccPtIpv6MsSuccActivatedDynPdps_Type()
)
cgprsAccPtIpv6MsSuccActivatedDynPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6MsSuccActivatedDynPdps.setStatus("current")
_CgprsAccPtIpv6MsDeactivatedPdps_Type = Counter32
_CgprsAccPtIpv6MsDeactivatedPdps_Object = MibTableColumn
cgprsAccPtIpv6MsDeactivatedPdps = _CgprsAccPtIpv6MsDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 30),
    _CgprsAccPtIpv6MsDeactivatedPdps_Type()
)
cgprsAccPtIpv6MsDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6MsDeactivatedPdps.setStatus("current")
_CgprsAccPtIpv6MsSuccDeactivatedPdps_Type = Counter32
_CgprsAccPtIpv6MsSuccDeactivatedPdps_Object = MibTableColumn
cgprsAccPtIpv6MsSuccDeactivatedPdps = _CgprsAccPtIpv6MsSuccDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 31),
    _CgprsAccPtIpv6MsSuccDeactivatedPdps_Type()
)
cgprsAccPtIpv6MsSuccDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6MsSuccDeactivatedPdps.setStatus("current")
_CgprsAccPtIpv6GgsnDeactivatedPdps_Type = Counter32
_CgprsAccPtIpv6GgsnDeactivatedPdps_Object = MibTableColumn
cgprsAccPtIpv6GgsnDeactivatedPdps = _CgprsAccPtIpv6GgsnDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 32),
    _CgprsAccPtIpv6GgsnDeactivatedPdps_Type()
)
cgprsAccPtIpv6GgsnDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6GgsnDeactivatedPdps.setStatus("current")
_CgprsAccPtIpv6GgsnSuccDeactivatedPdps_Type = Counter32
_CgprsAccPtIpv6GgsnSuccDeactivatedPdps_Object = MibTableColumn
cgprsAccPtIpv6GgsnSuccDeactivatedPdps = _CgprsAccPtIpv6GgsnSuccDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 33),
    _CgprsAccPtIpv6GgsnSuccDeactivatedPdps_Type()
)
cgprsAccPtIpv6GgsnSuccDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6GgsnSuccDeactivatedPdps.setStatus("current")
_CgprsAccPtIpv6UpstreamTrafficVolume_Type = Counter64
_CgprsAccPtIpv6UpstreamTrafficVolume_Object = MibTableColumn
cgprsAccPtIpv6UpstreamTrafficVolume = _CgprsAccPtIpv6UpstreamTrafficVolume_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 34),
    _CgprsAccPtIpv6UpstreamTrafficVolume_Type()
)
cgprsAccPtIpv6UpstreamTrafficVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6UpstreamTrafficVolume.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6UpstreamTrafficVolume.setUnits("bytes")
_CgprsAccPtIpv6DownstreamTrafficVolume_Type = Counter64
_CgprsAccPtIpv6DownstreamTrafficVolume_Object = MibTableColumn
cgprsAccPtIpv6DownstreamTrafficVolume = _CgprsAccPtIpv6DownstreamTrafficVolume_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 35),
    _CgprsAccPtIpv6DownstreamTrafficVolume_Type()
)
cgprsAccPtIpv6DownstreamTrafficVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6DownstreamTrafficVolume.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6DownstreamTrafficVolume.setUnits("bytes")
_CgprsAccPtIpv6UpstreamPackets_Type = Counter32
_CgprsAccPtIpv6UpstreamPackets_Object = MibTableColumn
cgprsAccPtIpv6UpstreamPackets = _CgprsAccPtIpv6UpstreamPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 36),
    _CgprsAccPtIpv6UpstreamPackets_Type()
)
cgprsAccPtIpv6UpstreamPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6UpstreamPackets.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6UpstreamPackets.setUnits("packets")
_CgprsAccPtIpv6DownstreamPackets_Type = Counter32
_CgprsAccPtIpv6DownstreamPackets_Object = MibTableColumn
cgprsAccPtIpv6DownstreamPackets = _CgprsAccPtIpv6DownstreamPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 37),
    _CgprsAccPtIpv6DownstreamPackets_Type()
)
cgprsAccPtIpv6DownstreamPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6DownstreamPackets.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtIpv6DownstreamPackets.setUnits("packets")
_CgprsAccPtPdpUpdateReqSent_Type = Counter32
_CgprsAccPtPdpUpdateReqSent_Object = MibTableColumn
cgprsAccPtPdpUpdateReqSent = _CgprsAccPtPdpUpdateReqSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 38),
    _CgprsAccPtPdpUpdateReqSent_Type()
)
cgprsAccPtPdpUpdateReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtPdpUpdateReqSent.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtPdpUpdateReqSent.setUnits("messages")
_CgprsAccPtSuccPdpUpdateResRcvd_Type = Counter32
_CgprsAccPtSuccPdpUpdateResRcvd_Object = MibTableColumn
cgprsAccPtSuccPdpUpdateResRcvd = _CgprsAccPtSuccPdpUpdateResRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 39),
    _CgprsAccPtSuccPdpUpdateResRcvd_Type()
)
cgprsAccPtSuccPdpUpdateResRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccPdpUpdateResRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtSuccPdpUpdateResRcvd.setUnits("messages")
_CgprsAccPtCoaRcvd_Type = Counter32
_CgprsAccPtCoaRcvd_Object = MibTableColumn
cgprsAccPtCoaRcvd = _CgprsAccPtCoaRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 40),
    _CgprsAccPtCoaRcvd_Type()
)
cgprsAccPtCoaRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtCoaRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtCoaRcvd.setUnits("messages")
_CgprsAccPtCoaSuccess_Type = Counter32
_CgprsAccPtCoaSuccess_Object = MibTableColumn
cgprsAccPtCoaSuccess = _CgprsAccPtCoaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 41),
    _CgprsAccPtCoaSuccess_Type()
)
cgprsAccPtCoaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtCoaSuccess.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtCoaSuccess.setUnits("messages")
_CgprsAccPtDtEnabled_Type = Counter32
_CgprsAccPtDtEnabled_Object = MibTableColumn
cgprsAccPtDtEnabled = _CgprsAccPtDtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 42),
    _CgprsAccPtDtEnabled_Type()
)
cgprsAccPtDtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDtEnabled.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtDtEnabled.setUnits("pdps")
_CgprsAccPtTotalBearers_Type = Counter32
_CgprsAccPtTotalBearers_Object = MibTableColumn
cgprsAccPtTotalBearers = _CgprsAccPtTotalBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 43),
    _CgprsAccPtTotalBearers_Type()
)
cgprsAccPtTotalBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtTotalBearers.setStatus("current")
_CgprsAccPtTotRmtInitCreateBearers_Type = Counter32
_CgprsAccPtTotRmtInitCreateBearers_Object = MibTableColumn
cgprsAccPtTotRmtInitCreateBearers = _CgprsAccPtTotRmtInitCreateBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 44),
    _CgprsAccPtTotRmtInitCreateBearers_Type()
)
cgprsAccPtTotRmtInitCreateBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtTotRmtInitCreateBearers.setStatus("current")
_CgprsAccPtSuccRmtInitCreateBearers_Type = Counter32
_CgprsAccPtSuccRmtInitCreateBearers_Object = MibTableColumn
cgprsAccPtSuccRmtInitCreateBearers = _CgprsAccPtSuccRmtInitCreateBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 45),
    _CgprsAccPtSuccRmtInitCreateBearers_Type()
)
cgprsAccPtSuccRmtInitCreateBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccRmtInitCreateBearers.setStatus("current")
_CgprsAccPtNetworkInitDeleteBearers_Type = Counter32
_CgprsAccPtNetworkInitDeleteBearers_Object = MibTableColumn
cgprsAccPtNetworkInitDeleteBearers = _CgprsAccPtNetworkInitDeleteBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 46),
    _CgprsAccPtNetworkInitDeleteBearers_Type()
)
cgprsAccPtNetworkInitDeleteBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtNetworkInitDeleteBearers.setStatus("current")
_CgprsAccPtTotRmtInitModifyBearers_Type = Counter32
_CgprsAccPtTotRmtInitModifyBearers_Object = MibTableColumn
cgprsAccPtTotRmtInitModifyBearers = _CgprsAccPtTotRmtInitModifyBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 47),
    _CgprsAccPtTotRmtInitModifyBearers_Type()
)
cgprsAccPtTotRmtInitModifyBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtTotRmtInitModifyBearers.setStatus("current")
_CgprsAccPtSuccRmtInitModifyBearers_Type = Counter32
_CgprsAccPtSuccRmtInitModifyBearers_Object = MibTableColumn
cgprsAccPtSuccRmtInitModifyBearers = _CgprsAccPtSuccRmtInitModifyBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 48),
    _CgprsAccPtSuccRmtInitModifyBearers_Type()
)
cgprsAccPtSuccRmtInitModifyBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccRmtInitModifyBearers.setStatus("current")
_CgprsAccPtTotNetworkInitUpdateBearers_Type = Counter32
_CgprsAccPtTotNetworkInitUpdateBearers_Object = MibTableColumn
cgprsAccPtTotNetworkInitUpdateBearers = _CgprsAccPtTotNetworkInitUpdateBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 49),
    _CgprsAccPtTotNetworkInitUpdateBearers_Type()
)
cgprsAccPtTotNetworkInitUpdateBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtTotNetworkInitUpdateBearers.setStatus("current")
_CgprsAccPtSuccNetworkInitUpdateBearers_Type = Counter32
_CgprsAccPtSuccNetworkInitUpdateBearers_Object = MibTableColumn
cgprsAccPtSuccNetworkInitUpdateBearers = _CgprsAccPtSuccNetworkInitUpdateBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 50),
    _CgprsAccPtSuccNetworkInitUpdateBearers_Type()
)
cgprsAccPtSuccNetworkInitUpdateBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccNetworkInitUpdateBearers.setStatus("current")
_CgprsAccPtTotNetworkInitCreateDedBearers_Type = Counter32
_CgprsAccPtTotNetworkInitCreateDedBearers_Object = MibTableColumn
cgprsAccPtTotNetworkInitCreateDedBearers = _CgprsAccPtTotNetworkInitCreateDedBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 51),
    _CgprsAccPtTotNetworkInitCreateDedBearers_Type()
)
cgprsAccPtTotNetworkInitCreateDedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtTotNetworkInitCreateDedBearers.setStatus("current")
_CgprsAccPtSuccNetworkInitCreateDedBearers_Type = Counter32
_CgprsAccPtSuccNetworkInitCreateDedBearers_Object = MibTableColumn
cgprsAccPtSuccNetworkInitCreateDedBearers = _CgprsAccPtSuccNetworkInitCreateDedBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 52),
    _CgprsAccPtSuccNetworkInitCreateDedBearers_Type()
)
cgprsAccPtSuccNetworkInitCreateDedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccNetworkInitCreateDedBearers.setStatus("current")
_CgprsAccPtTotNetworkInitCreateIPv6DedBearers_Type = Counter32
_CgprsAccPtTotNetworkInitCreateIPv6DedBearers_Object = MibTableColumn
cgprsAccPtTotNetworkInitCreateIPv6DedBearers = _CgprsAccPtTotNetworkInitCreateIPv6DedBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 53),
    _CgprsAccPtTotNetworkInitCreateIPv6DedBearers_Type()
)
cgprsAccPtTotNetworkInitCreateIPv6DedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtTotNetworkInitCreateIPv6DedBearers.setStatus("current")
_CgprsAccPtSuccNetworkInitCreateIPv6DedBearers_Type = Counter32
_CgprsAccPtSuccNetworkInitCreateIPv6DedBearers_Object = MibTableColumn
cgprsAccPtSuccNetworkInitCreateIPv6DedBearers = _CgprsAccPtSuccNetworkInitCreateIPv6DedBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 54),
    _CgprsAccPtSuccNetworkInitCreateIPv6DedBearers_Type()
)
cgprsAccPtSuccNetworkInitCreateIPv6DedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtSuccNetworkInitCreateIPv6DedBearers.setStatus("current")
_CgprsAccPtv4v6MsActivatedPdps_Type = Counter32
_CgprsAccPtv4v6MsActivatedPdps_Object = MibTableColumn
cgprsAccPtv4v6MsActivatedPdps = _CgprsAccPtv4v6MsActivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 55),
    _CgprsAccPtv4v6MsActivatedPdps_Type()
)
cgprsAccPtv4v6MsActivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtv4v6MsActivatedPdps.setStatus("current")
_CgprsAccPtv4v6SuccMsActivatedPdps_Type = Counter32
_CgprsAccPtv4v6SuccMsActivatedPdps_Object = MibTableColumn
cgprsAccPtv4v6SuccMsActivatedPdps = _CgprsAccPtv4v6SuccMsActivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 56),
    _CgprsAccPtv4v6SuccMsActivatedPdps_Type()
)
cgprsAccPtv4v6SuccMsActivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtv4v6SuccMsActivatedPdps.setStatus("current")
_CgprsAccPtv4v6MsDeactivatedPdps_Type = Counter32
_CgprsAccPtv4v6MsDeactivatedPdps_Object = MibTableColumn
cgprsAccPtv4v6MsDeactivatedPdps = _CgprsAccPtv4v6MsDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 57),
    _CgprsAccPtv4v6MsDeactivatedPdps_Type()
)
cgprsAccPtv4v6MsDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtv4v6MsDeactivatedPdps.setStatus("current")
_CgprsAccPtv4v6SuccMsDeactivatedPdps_Type = Counter32
_CgprsAccPtv4v6SuccMsDeactivatedPdps_Object = MibTableColumn
cgprsAccPtv4v6SuccMsDeactivatedPdps = _CgprsAccPtv4v6SuccMsDeactivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 58),
    _CgprsAccPtv4v6SuccMsDeactivatedPdps_Type()
)
cgprsAccPtv4v6SuccMsDeactivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtv4v6SuccMsDeactivatedPdps.setStatus("current")
_CgprsAccPtv4v6ActDedbearerPdps_Type = Counter32
_CgprsAccPtv4v6ActDedbearerPdps_Object = MibTableColumn
cgprsAccPtv4v6ActDedbearerPdps = _CgprsAccPtv4v6ActDedbearerPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 59),
    _CgprsAccPtv4v6ActDedbearerPdps_Type()
)
cgprsAccPtv4v6ActDedbearerPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtv4v6ActDedbearerPdps.setStatus("current")
_CgprsAccPtv4v6SuccActDedbearerPdps_Type = Counter32
_CgprsAccPtv4v6SuccActDedbearerPdps_Object = MibTableColumn
cgprsAccPtv4v6SuccActDedbearerPdps = _CgprsAccPtv4v6SuccActDedbearerPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 60),
    _CgprsAccPtv4v6SuccActDedbearerPdps_Type()
)
cgprsAccPtv4v6SuccActDedbearerPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtv4v6SuccActDedbearerPdps.setStatus("current")
_CgprsAccPtDhcpProxServDiscover_Type = Counter32
_CgprsAccPtDhcpProxServDiscover_Object = MibTableColumn
cgprsAccPtDhcpProxServDiscover = _CgprsAccPtDhcpProxServDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 61),
    _CgprsAccPtDhcpProxServDiscover_Type()
)
cgprsAccPtDhcpProxServDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServDiscover.setStatus("current")
_CgprsAccPtDhcpProxServRequest_Type = Counter32
_CgprsAccPtDhcpProxServRequest_Object = MibTableColumn
cgprsAccPtDhcpProxServRequest = _CgprsAccPtDhcpProxServRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 62),
    _CgprsAccPtDhcpProxServRequest_Type()
)
cgprsAccPtDhcpProxServRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServRequest.setStatus("current")
_CgprsAccPtDhcpProxServDeclines_Type = Counter32
_CgprsAccPtDhcpProxServDeclines_Object = MibTableColumn
cgprsAccPtDhcpProxServDeclines = _CgprsAccPtDhcpProxServDeclines_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 63),
    _CgprsAccPtDhcpProxServDeclines_Type()
)
cgprsAccPtDhcpProxServDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServDeclines.setStatus("current")
_CgprsAccPtDhcpProxServRelease_Type = Counter32
_CgprsAccPtDhcpProxServRelease_Object = MibTableColumn
cgprsAccPtDhcpProxServRelease = _CgprsAccPtDhcpProxServRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 64),
    _CgprsAccPtDhcpProxServRelease_Type()
)
cgprsAccPtDhcpProxServRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServRelease.setStatus("current")
_CgprsAccPtDhcpProxServOffer_Type = Counter32
_CgprsAccPtDhcpProxServOffer_Object = MibTableColumn
cgprsAccPtDhcpProxServOffer = _CgprsAccPtDhcpProxServOffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 65),
    _CgprsAccPtDhcpProxServOffer_Type()
)
cgprsAccPtDhcpProxServOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServOffer.setStatus("current")
_CgprsAccPtDhcpProxServAcks_Type = Counter32
_CgprsAccPtDhcpProxServAcks_Object = MibTableColumn
cgprsAccPtDhcpProxServAcks = _CgprsAccPtDhcpProxServAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 66),
    _CgprsAccPtDhcpProxServAcks_Type()
)
cgprsAccPtDhcpProxServAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServAcks.setStatus("current")
_CgprsAccPtDhcpProxServNaks_Type = Counter32
_CgprsAccPtDhcpProxServNaks_Object = MibTableColumn
cgprsAccPtDhcpProxServNaks = _CgprsAccPtDhcpProxServNaks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 67),
    _CgprsAccPtDhcpProxServNaks_Type()
)
cgprsAccPtDhcpProxServNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServNaks.setStatus("current")
_CgprsAccPtDhcpProxServInform_Type = Counter32
_CgprsAccPtDhcpProxServInform_Object = MibTableColumn
cgprsAccPtDhcpProxServInform = _CgprsAccPtDhcpProxServInform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 68),
    _CgprsAccPtDhcpProxServInform_Type()
)
cgprsAccPtDhcpProxServInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServInform.setStatus("current")
_CgprsAccPtDhcpProxServUnknowMsg_Type = Counter32
_CgprsAccPtDhcpProxServUnknowMsg_Object = MibTableColumn
cgprsAccPtDhcpProxServUnknowMsg = _CgprsAccPtDhcpProxServUnknowMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 69),
    _CgprsAccPtDhcpProxServUnknowMsg_Type()
)
cgprsAccPtDhcpProxServUnknowMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServUnknowMsg.setStatus("current")
_CgprsAccPtDhcpProxServRetryDrops_Type = Counter32
_CgprsAccPtDhcpProxServRetryDrops_Object = MibTableColumn
cgprsAccPtDhcpProxServRetryDrops = _CgprsAccPtDhcpProxServRetryDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 70),
    _CgprsAccPtDhcpProxServRetryDrops_Type()
)
cgprsAccPtDhcpProxServRetryDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServRetryDrops.setStatus("current")
_CgprsAccPtDhcpProxServErrDrops_Type = Counter32
_CgprsAccPtDhcpProxServErrDrops_Object = MibTableColumn
cgprsAccPtDhcpProxServErrDrops = _CgprsAccPtDhcpProxServErrDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 71),
    _CgprsAccPtDhcpProxServErrDrops_Type()
)
cgprsAccPtDhcpProxServErrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServErrDrops.setStatus("current")
_CgprsAccPtActiveBearers_Type = Gauge32
_CgprsAccPtActiveBearers_Object = MibTableColumn
cgprsAccPtActiveBearers = _CgprsAccPtActiveBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 72),
    _CgprsAccPtActiveBearers_Type()
)
cgprsAccPtActiveBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtActiveBearers.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtActiveBearers.setUnits("bearers")
_CgprsAccPtDhcpProxServTxErrDrops_Type = Counter32
_CgprsAccPtDhcpProxServTxErrDrops_Object = MibTableColumn
cgprsAccPtDhcpProxServTxErrDrops = _CgprsAccPtDhcpProxServTxErrDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 73),
    _CgprsAccPtDhcpProxServTxErrDrops_Type()
)
cgprsAccPtDhcpProxServTxErrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServTxErrDrops.setStatus("current")
_CgprsAccPtDhcpProxServIpAllocErr_Type = Counter32
_CgprsAccPtDhcpProxServIpAllocErr_Object = MibTableColumn
cgprsAccPtDhcpProxServIpAllocErr = _CgprsAccPtDhcpProxServIpAllocErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 74),
    _CgprsAccPtDhcpProxServIpAllocErr_Type()
)
cgprsAccPtDhcpProxServIpAllocErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpProxServIpAllocErr.setStatus("current")
_CgprsAccPtDedBearerDeactivations_Type = Counter32
_CgprsAccPtDedBearerDeactivations_Object = MibTableColumn
cgprsAccPtDedBearerDeactivations = _CgprsAccPtDedBearerDeactivations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 75),
    _CgprsAccPtDedBearerDeactivations_Type()
)
cgprsAccPtDedBearerDeactivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDedBearerDeactivations.setStatus("current")
_CgprsAccPtDedBearerQosUpdate_Type = Counter32
_CgprsAccPtDedBearerQosUpdate_Object = MibTableColumn
cgprsAccPtDedBearerQosUpdate = _CgprsAccPtDedBearerQosUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 76),
    _CgprsAccPtDedBearerQosUpdate_Type()
)
cgprsAccPtDedBearerQosUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDedBearerQosUpdate.setStatus("current")
_CgprsAccPtDedBearerSucQosUpdate_Type = Counter32
_CgprsAccPtDedBearerSucQosUpdate_Object = MibTableColumn
cgprsAccPtDedBearerSucQosUpdate = _CgprsAccPtDedBearerSucQosUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 77),
    _CgprsAccPtDedBearerSucQosUpdate_Type()
)
cgprsAccPtDedBearerSucQosUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDedBearerSucQosUpdate.setStatus("current")
_CgprsAccPtDedBearerNoQosUpdate_Type = Counter32
_CgprsAccPtDedBearerNoQosUpdate_Object = MibTableColumn
cgprsAccPtDedBearerNoQosUpdate = _CgprsAccPtDedBearerNoQosUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 78),
    _CgprsAccPtDedBearerNoQosUpdate_Type()
)
cgprsAccPtDedBearerNoQosUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDedBearerNoQosUpdate.setStatus("current")
_CgprsAccPtDedBearerSucNoQosUpdate_Type = Counter32
_CgprsAccPtDedBearerSucNoQosUpdate_Object = MibTableColumn
cgprsAccPtDedBearerSucNoQosUpdate = _CgprsAccPtDedBearerSucNoQosUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 79),
    _CgprsAccPtDedBearerSucNoQosUpdate_Type()
)
cgprsAccPtDedBearerSucNoQosUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDedBearerSucNoQosUpdate.setStatus("current")
_CgprsAccPtIpv4v6MsActivatedDynamicPdps_Type = Counter32
_CgprsAccPtIpv4v6MsActivatedDynamicPdps_Object = MibTableColumn
cgprsAccPtIpv4v6MsActivatedDynamicPdps = _CgprsAccPtIpv4v6MsActivatedDynamicPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 80),
    _CgprsAccPtIpv4v6MsActivatedDynamicPdps_Type()
)
cgprsAccPtIpv4v6MsActivatedDynamicPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv4v6MsActivatedDynamicPdps.setStatus("current")
_CgprsAccPtIpv4v6MsSuccActivatedDynamicPdps_Type = Counter32
_CgprsAccPtIpv4v6MsSuccActivatedDynamicPdps_Object = MibTableColumn
cgprsAccPtIpv4v6MsSuccActivatedDynamicPdps = _CgprsAccPtIpv4v6MsSuccActivatedDynamicPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 81),
    _CgprsAccPtIpv4v6MsSuccActivatedDynamicPdps_Type()
)
cgprsAccPtIpv4v6MsSuccActivatedDynamicPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtIpv4v6MsSuccActivatedDynamicPdps.setStatus("current")
_CgprsAccPtFailMsActivatedPdps_Type = Counter32
_CgprsAccPtFailMsActivatedPdps_Object = MibTableColumn
cgprsAccPtFailMsActivatedPdps = _CgprsAccPtFailMsActivatedPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 82),
    _CgprsAccPtFailMsActivatedPdps_Type()
)
cgprsAccPtFailMsActivatedPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtFailMsActivatedPdps.setStatus("current")
_CgprsAccPtFailPdpUpdate_Type = Counter32
_CgprsAccPtFailPdpUpdate_Object = MibTableColumn
cgprsAccPtFailPdpUpdate = _CgprsAccPtFailPdpUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 83),
    _CgprsAccPtFailPdpUpdate_Type()
)
cgprsAccPtFailPdpUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtFailPdpUpdate.setStatus("current")
_CgprsAccPtUpdateRspTimeOut_Type = Counter32
_CgprsAccPtUpdateRspTimeOut_Object = MibTableColumn
cgprsAccPtUpdateRspTimeOut = _CgprsAccPtUpdateRspTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 1, 1, 84),
    _CgprsAccPtUpdateRspTimeOut_Type()
)
cgprsAccPtUpdateRspTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtUpdateRspTimeOut.setStatus("current")
_CgprsAccPtDhcpv6ProxyStatsTable_Object = MibTable
cgprsAccPtDhcpv6ProxyStatsTable = _CgprsAccPtDhcpv6ProxyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxyStatsTable.setStatus("current")
_CgprsAccPtDhcpv6ProxyStatsEntry_Object = MibTableRow
cgprsAccPtDhcpv6ProxyStatsEntry = _CgprsAccPtDhcpv6ProxyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxyStatsEntry.setStatus("current")
_CgprsAccPtDhcpv6ProxInforeqRcvd_Type = Counter32
_CgprsAccPtDhcpv6ProxInforeqRcvd_Object = MibTableColumn
cgprsAccPtDhcpv6ProxInforeqRcvd = _CgprsAccPtDhcpv6ProxInforeqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1, 1),
    _CgprsAccPtDhcpv6ProxInforeqRcvd_Type()
)
cgprsAccPtDhcpv6ProxInforeqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxInforeqRcvd.setStatus("current")
_CgprsAccPtDhcpv6ProxInforeqRply_Type = Counter32
_CgprsAccPtDhcpv6ProxInforeqRply_Object = MibTableColumn
cgprsAccPtDhcpv6ProxInforeqRply = _CgprsAccPtDhcpv6ProxInforeqRply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1, 2),
    _CgprsAccPtDhcpv6ProxInforeqRply_Type()
)
cgprsAccPtDhcpv6ProxInforeqRply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxInforeqRply.setStatus("current")
_CgprsAccPtDhcpv6ProxInforeqLocRply_Type = Counter32
_CgprsAccPtDhcpv6ProxInforeqLocRply_Object = MibTableColumn
cgprsAccPtDhcpv6ProxInforeqLocRply = _CgprsAccPtDhcpv6ProxInforeqLocRply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1, 3),
    _CgprsAccPtDhcpv6ProxInforeqLocRply_Type()
)
cgprsAccPtDhcpv6ProxInforeqLocRply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxInforeqLocRply.setStatus("current")
_CgprsAccPtDhcpv6ProxIpAllocSuc_Type = Counter32
_CgprsAccPtDhcpv6ProxIpAllocSuc_Object = MibTableColumn
cgprsAccPtDhcpv6ProxIpAllocSuc = _CgprsAccPtDhcpv6ProxIpAllocSuc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1, 4),
    _CgprsAccPtDhcpv6ProxIpAllocSuc_Type()
)
cgprsAccPtDhcpv6ProxIpAllocSuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxIpAllocSuc.setStatus("current")
_CgprsAccPtDhcpv6ProxIpAllocFail_Type = Counter32
_CgprsAccPtDhcpv6ProxIpAllocFail_Object = MibTableColumn
cgprsAccPtDhcpv6ProxIpAllocFail = _CgprsAccPtDhcpv6ProxIpAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1, 5),
    _CgprsAccPtDhcpv6ProxIpAllocFail_Type()
)
cgprsAccPtDhcpv6ProxIpAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxIpAllocFail.setStatus("current")
_CgprsAccPtDhcpv6ProxIpRelease_Type = Counter32
_CgprsAccPtDhcpv6ProxIpRelease_Object = MibTableColumn
cgprsAccPtDhcpv6ProxIpRelease = _CgprsAccPtDhcpv6ProxIpRelease_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1, 6),
    _CgprsAccPtDhcpv6ProxIpRelease_Type()
)
cgprsAccPtDhcpv6ProxIpRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxIpRelease.setStatus("current")
_CgprsAccPtDhcpv6ProxIpRenewFail_Type = Counter32
_CgprsAccPtDhcpv6ProxIpRenewFail_Object = MibTableColumn
cgprsAccPtDhcpv6ProxIpRenewFail = _CgprsAccPtDhcpv6ProxIpRenewFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1, 7),
    _CgprsAccPtDhcpv6ProxIpRenewFail_Type()
)
cgprsAccPtDhcpv6ProxIpRenewFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxIpRenewFail.setStatus("current")
_CgprsAccPtDhcpv6ProxUnkwnMsg_Type = Counter32
_CgprsAccPtDhcpv6ProxUnkwnMsg_Object = MibTableColumn
cgprsAccPtDhcpv6ProxUnkwnMsg = _CgprsAccPtDhcpv6ProxUnkwnMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1, 8),
    _CgprsAccPtDhcpv6ProxUnkwnMsg_Type()
)
cgprsAccPtDhcpv6ProxUnkwnMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxUnkwnMsg.setStatus("current")
_CgprsAccPtDhcpv6ProxErrs_Type = Counter32
_CgprsAccPtDhcpv6ProxErrs_Object = MibTableColumn
cgprsAccPtDhcpv6ProxErrs = _CgprsAccPtDhcpv6ProxErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 2, 1, 9),
    _CgprsAccPtDhcpv6ProxErrs_Type()
)
cgprsAccPtDhcpv6ProxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxErrs.setStatus("current")
_CgprsAccPtThruputStatsTable_Object = MibTable
cgprsAccPtThruputStatsTable = _CgprsAccPtThruputStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cgprsAccPtThruputStatsTable.setStatus("current")
_CgprsAccPtThruputStatsEntry_Object = MibTableRow
cgprsAccPtThruputStatsEntry = _CgprsAccPtThruputStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 3, 1)
)
cgprsAccPtThruputStatsEntry.setIndexNames(
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIndex"),
    (0, "CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtThruputInterval"),
)
if mibBuilder.loadTexts:
    cgprsAccPtThruputStatsEntry.setStatus("current")


class _CgprsAccPtThruputInterval_Type(Integer32):
    """Custom type cgprsAccPtThruputInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CgprsAccPtThruputInterval_Type.__name__ = "Integer32"
_CgprsAccPtThruputInterval_Object = MibTableColumn
cgprsAccPtThruputInterval = _CgprsAccPtThruputInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 3, 1, 1),
    _CgprsAccPtThruputInterval_Type()
)
cgprsAccPtThruputInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsAccPtThruputInterval.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtThruputInterval.setUnits("minutes")


class _CgprsAccPtThruPutLastCollected_Type(Integer32):
    """Custom type cgprsAccPtThruPutLastCollected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgprsAccPtThruPutLastCollected_Type.__name__ = "Integer32"
_CgprsAccPtThruPutLastCollected_Object = MibTableColumn
cgprsAccPtThruPutLastCollected = _CgprsAccPtThruPutLastCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 3, 1, 2),
    _CgprsAccPtThruPutLastCollected_Type()
)
cgprsAccPtThruPutLastCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtThruPutLastCollected.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtThruPutLastCollected.setUnits("minutes")
_CgprsAccPtUpstrByteCount_Type = Gauge32
_CgprsAccPtUpstrByteCount_Object = MibTableColumn
cgprsAccPtUpstrByteCount = _CgprsAccPtUpstrByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 3, 1, 3),
    _CgprsAccPtUpstrByteCount_Type()
)
cgprsAccPtUpstrByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtUpstrByteCount.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtUpstrByteCount.setUnits("bytes")
_CgprsAccPtDownstrByteCount_Type = Gauge32
_CgprsAccPtDownstrByteCount_Object = MibTableColumn
cgprsAccPtDownstrByteCount = _CgprsAccPtDownstrByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 3, 1, 4),
    _CgprsAccPtDownstrByteCount_Type()
)
cgprsAccPtDownstrByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDownstrByteCount.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtDownstrByteCount.setUnits("bytes")
_CgprsAccPtUpstrPktCount_Type = Gauge32
_CgprsAccPtUpstrPktCount_Object = MibTableColumn
cgprsAccPtUpstrPktCount = _CgprsAccPtUpstrPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 3, 1, 5),
    _CgprsAccPtUpstrPktCount_Type()
)
cgprsAccPtUpstrPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtUpstrPktCount.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtUpstrPktCount.setUnits("packets")
_CgprsAccPtDownstrPktCount_Type = Gauge32
_CgprsAccPtDownstrPktCount_Object = MibTableColumn
cgprsAccPtDownstrPktCount = _CgprsAccPtDownstrPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 3, 3, 1, 6),
    _CgprsAccPtDownstrPktCount_Type()
)
cgprsAccPtDownstrPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsAccPtDownstrPktCount.setStatus("current")
if mibBuilder.loadTexts:
    cgprsAccPtDownstrPktCount.setUnits("packets")
_CiscoGprsAccPtNotifInfo_ObjectIdentity = ObjectIdentity
ciscoGprsAccPtNotifInfo = _CiscoGprsAccPtNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 4)
)
_CgprsAccPtMsAddrType_Type = InetAddressType
_CgprsAccPtMsAddrType_Object = MibScalar
cgprsAccPtMsAddrType = _CgprsAccPtMsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 4, 1),
    _CgprsAccPtMsAddrType_Type()
)
cgprsAccPtMsAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgprsAccPtMsAddrType.setStatus("current")
_CgprsAccPtMsAllocAddr_Type = InetAddress
_CgprsAccPtMsAllocAddr_Object = MibScalar
cgprsAccPtMsAllocAddr = _CgprsAccPtMsAllocAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 4, 2),
    _CgprsAccPtMsAllocAddr_Type()
)
cgprsAccPtMsAllocAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgprsAccPtMsAllocAddr.setStatus("current")
_CgprsAccPtMsNewAddr_Type = InetAddress
_CgprsAccPtMsNewAddr_Object = MibScalar
cgprsAccPtMsNewAddr = _CgprsAccPtMsNewAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 4, 3),
    _CgprsAccPtMsNewAddr_Type()
)
cgprsAccPtMsNewAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgprsAccPtMsNewAddr.setStatus("current")
_CgprsAccPtMsTpduDstAddr_Type = InetAddress
_CgprsAccPtMsTpduDstAddr_Object = MibScalar
cgprsAccPtMsTpduDstAddr = _CgprsAccPtMsTpduDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 1, 4, 4),
    _CgprsAccPtMsTpduDstAddr_Type()
)
cgprsAccPtMsTpduDstAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgprsAccPtMsTpduDstAddr.setStatus("current")
_CgprsAccPtMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cgprsAccPtMIBNotificationPrefix = _CgprsAccPtMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 2)
)
_CgprsAccPtMIBNotifications_ObjectIdentity = ObjectIdentity
cgprsAccPtMIBNotifications = _CgprsAccPtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 2, 0)
)
_CgprsAccPtConformances_ObjectIdentity = ObjectIdentity
cgprsAccPtConformances = _CgprsAccPtConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3)
)
_CgprsAccPtMIBCompliances_ObjectIdentity = ObjectIdentity
cgprsAccPtMIBCompliances = _CgprsAccPtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1)
)
_CgprsAccPtMIBGroups_ObjectIdentity = ObjectIdentity
cgprsAccPtMIBGroups = _CgprsAccPtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2)
)
cgprsAccPtEntry.registerAugmentions(
    ("CISCO-GPRS-ACC-PT-MIB",
     "cgprsAccPtExtEntry")
)
cgprsAccPtExtEntry.setIndexNames(*cgprsAccPtEntry.getIndexNames())
cgprsAccPtEntry.registerAugmentions(
    ("CISCO-GPRS-ACC-PT-MIB",
     "cgprsAccPtGenServerConfigEntry")
)
cgprsAccPtGenServerConfigEntry.setIndexNames(*cgprsAccPtEntry.getIndexNames())
cgprsAccPtEntry.registerAugmentions(
    ("CISCO-GPRS-ACC-PT-MIB",
     "cgprsAccPtImsConfigEntry")
)
cgprsAccPtImsConfigEntry.setIndexNames(*cgprsAccPtEntry.getIndexNames())
cgprsAccPtEntry.registerAugmentions(
    ("CISCO-GPRS-ACC-PT-MIB",
     "cgprsAccPtCacEntry")
)
cgprsAccPtCacEntry.setIndexNames(*cgprsAccPtEntry.getIndexNames())
cgprsAccPtEntry.registerAugmentions(
    ("CISCO-GPRS-ACC-PT-MIB",
     "cgprsAccPtRouteProbeEntry")
)
cgprsAccPtRouteProbeEntry.setIndexNames(*cgprsAccPtEntry.getIndexNames())
cgprsAccPtEntry.registerAugmentions(
    ("CISCO-GPRS-ACC-PT-MIB",
     "cgprsAccPtIpv6Entry")
)
cgprsAccPtIpv6Entry.setIndexNames(*cgprsAccPtEntry.getIndexNames())
cgprsAccPtEntry.registerAugmentions(
    ("CISCO-GPRS-ACC-PT-MIB",
     "cgprsAccPtStatisticsEntry")
)
cgprsAccPtStatisticsEntry.setIndexNames(*cgprsAccPtEntry.getIndexNames())
cgprsAccPtEntry.registerAugmentions(
    ("CISCO-GPRS-ACC-PT-MIB",
     "cgprsAccPtDhcpv6ProxyStatsEntry")
)
cgprsAccPtDhcpv6ProxyStatsEntry.setIndexNames(*cgprsAccPtEntry.getIndexNames())

# Managed Objects groups

cgprsAccPtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 1)
)
cgprsAccPtMIBGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRowStatus"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtName"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMode"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpAddressPool"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDHCPServerPri"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDHCPServerSec"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDHCPGwAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRadiusServerPri"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRadiusServerSec"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListGroupIn"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListGroupOut"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIfIndex"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIfNextHop"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAccessViolation"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSubrRequired"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkInitiated"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpAddrAllocations"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtUsers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIdlePdpPurgeTimer"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtBlockMsRoaming"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAnonymousUserName"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAnonymousUserPassword"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsIsdnSuppressed"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsIsdnSuppressedValue"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAaaAuthServerGroup"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAaaAccountServerGroup"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAaaAccountingEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAggregRowStatus"))
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBGroup.setStatus("obsolete")

cgprsAccPtCfgNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 2)
)
cgprsAccPtCfgNotifGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifAccPtIndex"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifReason"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifHistMax"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifLatestIndex"))
)
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotifGroup.setStatus("current")

cgprsAccPtStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 3)
)
cgprsAccPtStatisticsGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkInitPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGgsnDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccGgsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtActivePdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtUpstreamTrafficVol"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDownstreamTrafficVol"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroup.setStatus("obsolete")

cgprsAccPtMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 4)
)
cgprsAccPtMIBGroupRev1.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRowStatus"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtName"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMode"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpAddressPool"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDHCPServerPri"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDHCPServerSec"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDHCPGwAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListGroupIn"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListGroupOut"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAccessViolation"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSubrRequired"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkInitiated"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpAddrAllocations"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIdlePdpPurgeTimer"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtBlockMsRoaming"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAnonymousUserName"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAnonymousUserPassword"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsIsdnSuppressed"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsIsdnSuppressedValue"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAaaAuthServerGroup"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAaaAccountServerGroup"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAaaAccountingEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtVrfName"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpAddrSpace"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPppRegenEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPppRegenMaxSessions"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPppRegenSetupTime"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAutoAggregation"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAggregRowStatus"))
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBGroupRev1.setStatus("current")

cgprsAccPtExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 5)
)
cgprsAccPtExtMIBGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListInEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListOutEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGtpRespMesgWaitAcctng"))
)
if mibBuilder.loadTexts:
    cgprsAccPtExtMIBGroup.setStatus("obsolete")

cgprsAccPtExtMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 7)
)
cgprsAccPtExtMIBGroupRev1.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListInEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListOutEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGtpRespMesgWaitAcctng"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtImsiSuppressed"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtVerifyUpStrTpduSrcAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtVerifyUpStrTpduDstAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRedirInterMobilAddrTyp"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRedirInterMobilAddr"))
)
if mibBuilder.loadTexts:
    cgprsAccPtExtMIBGroupRev1.setStatus("obsolete")

cgprsAccPtStatisticsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 8)
)
cgprsAccPtStatisticsGroupRev1.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkInitPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGgsnDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccGgsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtActivePdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtUpstreamTrafficVol"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDownstreamTrafficVol"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSourceAddrViolTpdus"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDestAddrViolTpdus"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRedirInterMobilTraffic"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroupRev1.setStatus("deprecated")

cgprsAccPtExtMIBGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 9)
)
cgprsAccPtExtMIBGroupRev2.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListInEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListOutEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGtpRespMesgWaitAcctng"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtVerifyUpStrTpduSrcAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtVerifyUpStrTpduDstAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRedirInterMobilAddrTyp"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRedirInterMobilAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuppressRadiusAttribs"))
)
if mibBuilder.loadTexts:
    cgprsAccPtExtMIBGroupRev2.setStatus("deprecated")

cgprsAccPtExtMIBGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 10)
)
cgprsAccPtExtMIBGroupRev3.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListInEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIPAccListOutEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGtpRespMesgWaitAcctng"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtVerifyUpStrTpduSrcAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtVerifyUpStrTpduDstAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRedirInterMobilAddrTyp"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRedirInterMobilAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuppressRadiusAttribs"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtInterimAccountinEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSetRadiusAttributes"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtOperationMode"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAbsoluteSessionTimer"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRadiusAttrNasId"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPdpInServicePolicyName"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPdpOutServicePolicyNam"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPppRegenVerifyDomain"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpAddrLocalPoolName"))
)
if mibBuilder.loadTexts:
    cgprsAccPtExtMIBGroupRev3.setStatus("current")

cgprsAccPtGenServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 11)
)
cgprsAccPtGenServerGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDnsServerAddrType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPriDnsServer"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSecDnsServer"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetbiosServerAddrType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPriNetbiosServer"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSecNetbiosServer"))
)
if mibBuilder.loadTexts:
    cgprsAccPtGenServerGroup.setStatus("current")

cgprsAccPtImsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 12)
)
cgprsAccPtImsGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtImsEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPCscfGroupName"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtImsSigAccGroupIn"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtImsSigAccGroupOut"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRejNonImsPdp"))
)
if mibBuilder.loadTexts:
    cgprsAccPtImsGroup.setStatus("deprecated")

cgprsAccPtChargingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 13)
)
cgprsAccPtChargingGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtChgProfile"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtChgProfOverride"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtChgProfRowStatus"))
)
if mibBuilder.loadTexts:
    cgprsAccPtChargingGroup.setStatus("current")

cgprsAccPtCacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 14)
)
cgprsAccPtCacGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCacPolicyName"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCacUpStrBandWidthPool"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCacDnStrBandWidthPool"))
)
if mibBuilder.loadTexts:
    cgprsAccPtCacGroup.setStatus("current")

cgprsAccPtRouteProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 15)
)
cgprsAccPtRouteProbeGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRpDestAddrType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRpDestAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRpProtocol"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRpDestPort"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRpTtl"))
)
if mibBuilder.loadTexts:
    cgprsAccPtRouteProbeGroup.setStatus("current")

cgprsAccPtStatisticsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 16)
)
cgprsAccPtStatisticsGroupRev2.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkInitPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGgsnDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccGgsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtActivePdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSourceAddrViolTpdus"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDestAddrViolTpdus"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRedirInterMobilTraffic"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRevUpstreamTrafficVol"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRevDownstrTrafficVol"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtUpstreamPacketCount"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDownstreamPacketCount"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpAddrRequests"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccDhcpAddrRequests"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpAddrReleases"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroupRev2.setStatus("deprecated")

cgprsAccPtThruPutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 17)
)
cgprsAccPtThruPutGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtThruPutLastCollected"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtUpstrByteCount"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDownstrByteCount"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtUpstrPktCount"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDownstrPktCount"))
)
if mibBuilder.loadTexts:
    cgprsAccPtThruPutGroup.setStatus("current")

cgprsAccPtNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 18)
)
cgprsAccPtNotifInfoGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsAddrType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsAllocAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsNewAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsTpduDstAddr"))
)
if mibBuilder.loadTexts:
    cgprsAccPtNotifInfoGroup.setStatus("current")

cgprsAccPtMIBR60Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 20)
)
cgprsAccPtMIBR60Group.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtServiceAware"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAdvDownlinkNextHopAddrType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAdvDownlinkNextHopAddr"))
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBR60Group.setStatus("current")

cgprsAccPtIpv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 21)
)
cgprsAccPtIpv6Group.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6BaseVTemplate"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6DnsAddrType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6DnsPriAddress"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6DnsSecAddress"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6Enable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6Exclusive"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6AccessGroupDown"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6AccessGroupUp"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6AddrPool"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6AddrLocalPoolName"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6Redirect"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6RedirectAddrType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6RedirectAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6SecurityVerifySrc"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6SecurityVerifyDst"))
)
if mibBuilder.loadTexts:
    cgprsAccPtIpv6Group.setStatus("current")

cgprsAccPtStatisticsGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 22)
)
cgprsAccPtStatisticsGroupRev3.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccMsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkInitPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGgsnDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccGgsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtActivePdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSourceAddrViolTpdus"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDestAddrViolTpdus"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRedirInterMobilTraffic"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRevUpstreamTrafficVol"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtRevDownstrTrafficVol"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtUpstreamPacketCount"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDownstreamPacketCount"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpAddrRequests"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccDhcpAddrRequests"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpAddrReleases"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6MsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6MsSuccActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6NetworkInitDeactPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6NetworkInitDeactSuccPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6MsActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6MsSuccActivatedDynPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6MsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6MsSuccDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6GgsnDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6GgsnSuccDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6UpstreamTrafficVolume"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6DownstreamTrafficVolume"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6UpstreamPackets"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6DownstreamPackets"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroupRev3.setStatus("current")

cgprsAccPtPcscfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 23)
)
cgprsAccPtPcscfGroup.setObjects(
    ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPcscfServerGroupName")
)
if mibBuilder.loadTexts:
    cgprsAccPtPcscfGroup.setStatus("current")

cgprsAccPtMIBR80Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 24)
)
cgprsAccPtMIBR80Group.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGtpUpdateFailDelete"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAaaAccountInterPeriod"))
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBR80Group.setStatus("current")

cgprsAccPtStatisticsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 25)
)
cgprsAccPtStatisticsGroupSup1.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPdpUpdateReqSent"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccPdpUpdateResRcvd"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCoaRcvd"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCoaSuccess"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDtEnabled"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroupSup1.setStatus("deprecated")

cgprsAccPtMIBR80GroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 26)
)
cgprsAccPtMIBR80GroupSup1.setObjects(
    ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAaaAccountInterRadius")
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBR80GroupSup1.setStatus("current")

cgprsAccPtMIBR90Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 27)
)
cgprsAccPtMIBR90Group.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGxEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPcscfLoadBalance"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkBehindMsEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMaxSubnetsBehindMobile"))
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBR90Group.setStatus("deprecated")

cgprsAccPtStatisticsGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 28)
)
cgprsAccPtStatisticsGroupSup2.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPdpUpdateReqSent"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccPdpUpdateResRcvd"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCoaRcvd"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCoaSuccess"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDtEnabled"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotalBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotRmtInitCreateBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccRmtInitCreateBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkInitDeleteBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotNetworkInitUpdateBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitUpdateBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotNetworkInitCreateDedBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitCreateDedBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotRmtInitModifyBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccRmtInitModifyBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotNetworkInitCreateIPv6DedBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitCreateIPv6DedBearers"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroupSup2.setStatus("deprecated")

cgprsAccPtMIBR92Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 29)
)
cgprsAccPtMIBR92Group.setObjects(
    ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtChargingRecordType")
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBR92Group.setStatus("current")

cgprsAccPtMIBR90GroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 30)
)
cgprsAccPtMIBR90GroupRev1.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtGxEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPcscfLoadBalance"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkBehindMsEnable"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMaxSubnetsBehindMobile"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtChargingGrp"))
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBR90GroupRev1.setStatus("current")

cgprsAccPtMIBR100Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 31)
)
cgprsAccPtMIBR100Group.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtAggregCsgGroup"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCsgGroupRowStatus"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpAddrPoolNoRedistribute"))
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBR100Group.setStatus("current")

cgprsAccPtStatisticsGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 32)
)
cgprsAccPtStatisticsGroupSup3.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtPdpUpdateReqSent"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccPdpUpdateResRcvd"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCoaRcvd"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCoaSuccess"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDtEnabled"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotalBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotRmtInitCreateBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccRmtInitCreateBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtNetworkInitDeleteBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotNetworkInitUpdateBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitUpdateBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotNetworkInitCreateDedBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitCreateDedBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotRmtInitModifyBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccRmtInitModifyBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtTotNetworkInitCreateIPv6DedBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSuccNetworkInitCreateIPv6DedBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtv4v6MsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtv4v6SuccMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtv4v6MsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtv4v6SuccMsDeactivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtv4v6ActDedbearerPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtv4v6SuccActDedbearerPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServDiscover"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServRequest"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServDeclines"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServRelease"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServOffer"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServAcks"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServNaks"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServInform"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServUnknowMsg"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServRetryDrops"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServErrDrops"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroupSup3.setStatus("current")

cgprsAccPtExtMIBGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 33)
)
cgprsAccPtExtMIBGroupSup1.setObjects(
    ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDualAddrEnabled")
)
if mibBuilder.loadTexts:
    cgprsAccPtExtMIBGroupSup1.setStatus("current")

cgprsAccPtIpv6GroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 34)
)
cgprsAccPtIpv6GroupSup1.setObjects(
    ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv6AddrAllocations")
)
if mibBuilder.loadTexts:
    cgprsAccPtIpv6GroupSup1.setStatus("current")

cgprsAccPtStatisticsGroupSup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 35)
)
cgprsAccPtStatisticsGroupSup4.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtActiveBearers"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServTxErrDrops"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpProxServIpAllocErr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDedBearerDeactivations"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDedBearerQosUpdate"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDedBearerSucQosUpdate"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDedBearerNoQosUpdate"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDedBearerSucNoQosUpdate"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroupSup4.setStatus("current")

cgprsAccPtDhcpv6ProxyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 36)
)
cgprsAccPtDhcpv6ProxyStatsGroup.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxInforeqRcvd"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxInforeqRply"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxInforeqLocRply"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxIpAllocSuc"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxIpAllocFail"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxIpRelease"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxIpRenewFail"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxUnkwnMsg"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxErrs"))
)
if mibBuilder.loadTexts:
    cgprsAccPtDhcpv6ProxyStatsGroup.setStatus("current")

cgprsAccPtExtMIBGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 37)
)
cgprsAccPtExtMIBGroupSup2.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtVerifyDownlinkAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtDhcpv6ProxClientIntf"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccptDhcpv6RapidCommit"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccptDhcpv6PoolName"))
)
if mibBuilder.loadTexts:
    cgprsAccPtExtMIBGroupSup2.setStatus("current")

cgprsAccPtStatisticsGroupSup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 38)
)
cgprsAccPtStatisticsGroupSup5.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv4v6MsActivatedDynamicPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtIpv4v6MsSuccActivatedDynamicPdps"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroupSup5.setStatus("current")

cgprsAccPtStatisticsGroupSup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 39)
)
cgprsAccPtStatisticsGroupSup6.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtFailMsActivatedPdps"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtFailPdpUpdate"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtUpdateRspTimeOut"))
)
if mibBuilder.loadTexts:
    cgprsAccPtStatisticsGroupSup6.setStatus("current")


# Notification objects

cgprsAccPtCfgNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 2, 0, 1)
)
cgprsAccPtCfgNotif.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifAccPtIndex"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifReason"))
)
if mibBuilder.loadTexts:
    cgprsAccPtCfgNotif.setStatus(
        "current"
    )

cgprsAccPtSecSrcViolNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 2, 0, 2)
)
cgprsAccPtSecSrcViolNotif.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifAccPtIndex"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsAddrType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsAllocAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsNewAddr"))
)
if mibBuilder.loadTexts:
    cgprsAccPtSecSrcViolNotif.setStatus(
        "current"
    )

cgprsAccPtSecDestViolNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 2, 0, 3)
)
cgprsAccPtSecDestViolNotif.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifAccPtIndex"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsAddrType"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsAllocAddr"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMsTpduDstAddr"))
)
if mibBuilder.loadTexts:
    cgprsAccPtSecDestViolNotif.setStatus(
        "current"
    )

cgprsAccPtMaintenanceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 2, 0, 4)
)
cgprsAccPtMaintenanceNotif.setObjects(
    ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifAccPtIndex")
)
if mibBuilder.loadTexts:
    cgprsAccPtMaintenanceNotif.setStatus(
        "current"
    )

cgprsAccPtInServiceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 2, 0, 5)
)
cgprsAccPtInServiceNotif.setObjects(
    ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotifAccPtIndex")
)
if mibBuilder.loadTexts:
    cgprsAccPtInServiceNotif.setStatus(
        "current"
    )


# Notifications groups

cgprsAccPtMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 6)
)
cgprsAccPtMIBNotifGroup.setObjects(
    ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotif")
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBNotifGroup.setStatus(
        "deprecated"
    )

cgprsAccPtMIBNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 2, 19)
)
cgprsAccPtMIBNotifGroupRev1.setObjects(
      *(("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtCfgNotif"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSecSrcViolNotif"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtSecDestViolNotif"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtMaintenanceNotif"),
        ("CISCO-GPRS-ACC-PT-MIB", "cgprsAccPtInServiceNotif"))
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBNotifGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cgprsAccPtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBCompliance.setStatus(
        "obsolete"
    )

cgprsAccPtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev1.setStatus(
        "obsolete"
    )

cgprsAccPtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev2.setStatus(
        "obsolete"
    )

cgprsAccPtMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev3.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev4.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev5.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev6.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev7.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev8.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev9.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 11)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev10.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 12)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev11.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 13)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev12.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 14)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev13.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 15)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev14.setStatus(
        "deprecated"
    )

cgprsAccPtMIBComplianceRev15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 183, 3, 1, 16)
)
if mibBuilder.loadTexts:
    cgprsAccPtMIBComplianceRev15.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GPRS-ACC-PT-MIB",
    **{"AccessControlListId": AccessControlListId,
       "AccessControlListOrZero": AccessControlListOrZero,
       "AccessControlListName": AccessControlListName,
       "ciscoGprsAccPtMIB": ciscoGprsAccPtMIB,
       "ciscoGprsAccPtMIBObjects": ciscoGprsAccPtMIBObjects,
       "ciscoGprsAccPtConfig": ciscoGprsAccPtConfig,
       "cgprsAccPtTable": cgprsAccPtTable,
       "cgprsAccPtEntry": cgprsAccPtEntry,
       "cgprsAccPtIndex": cgprsAccPtIndex,
       "cgprsAccPtRowStatus": cgprsAccPtRowStatus,
       "cgprsAccPtName": cgprsAccPtName,
       "cgprsAccPtMode": cgprsAccPtMode,
       "cgprsAccPtIpAddressPool": cgprsAccPtIpAddressPool,
       "cgprsAccPtDHCPServerPri": cgprsAccPtDHCPServerPri,
       "cgprsAccPtDHCPServerSec": cgprsAccPtDHCPServerSec,
       "cgprsAccPtDHCPGwAddr": cgprsAccPtDHCPGwAddr,
       "cgprsAccPtRadiusServerPri": cgprsAccPtRadiusServerPri,
       "cgprsAccPtRadiusServerSec": cgprsAccPtRadiusServerSec,
       "cgprsAccPtIPAccListGroupIn": cgprsAccPtIPAccListGroupIn,
       "cgprsAccPtIPAccListGroupOut": cgprsAccPtIPAccListGroupOut,
       "cgprsAccPtIfIndex": cgprsAccPtIfIndex,
       "cgprsAccPtIfNextHop": cgprsAccPtIfNextHop,
       "cgprsAccPtAccessViolation": cgprsAccPtAccessViolation,
       "cgprsAccPtSubrRequired": cgprsAccPtSubrRequired,
       "cgprsAccPtNetworkInitiated": cgprsAccPtNetworkInitiated,
       "cgprsAccPtIpAddrAllocations": cgprsAccPtIpAddrAllocations,
       "cgprsAccPtUsers": cgprsAccPtUsers,
       "cgprsAccPtIdlePdpPurgeTimer": cgprsAccPtIdlePdpPurgeTimer,
       "cgprsAccPtBlockMsRoaming": cgprsAccPtBlockMsRoaming,
       "cgprsAccPtAnonymousUserName": cgprsAccPtAnonymousUserName,
       "cgprsAccPtAnonymousUserPassword": cgprsAccPtAnonymousUserPassword,
       "cgprsAccPtMsIsdnSuppressed": cgprsAccPtMsIsdnSuppressed,
       "cgprsAccPtMsIsdnSuppressedValue": cgprsAccPtMsIsdnSuppressedValue,
       "cgprsAccPtAaaAuthServerGroup": cgprsAccPtAaaAuthServerGroup,
       "cgprsAccPtAaaAccountServerGroup": cgprsAccPtAaaAccountServerGroup,
       "cgprsAccPtAaaAccountingEnable": cgprsAccPtAaaAccountingEnable,
       "cgprsAccPtType": cgprsAccPtType,
       "cgprsAccPtVrfName": cgprsAccPtVrfName,
       "cgprsAccPtDhcpAddrSpace": cgprsAccPtDhcpAddrSpace,
       "cgprsAccPtPppRegenEnable": cgprsAccPtPppRegenEnable,
       "cgprsAccPtPppRegenMaxSessions": cgprsAccPtPppRegenMaxSessions,
       "cgprsAccPtPppRegenSetupTime": cgprsAccPtPppRegenSetupTime,
       "cgprsAccPtAutoAggregation": cgprsAccPtAutoAggregation,
       "cgprsAccPtPcscfServerGroupName": cgprsAccPtPcscfServerGroupName,
       "cgprsAccPtAggregTable": cgprsAccPtAggregTable,
       "cgprsAccPtAggregEntry": cgprsAccPtAggregEntry,
       "cgprsAccPtAggregIpAddrType": cgprsAccPtAggregIpAddrType,
       "cgprsAccPtAggregIpAddr": cgprsAccPtAggregIpAddr,
       "cgprsAccPtAggregIpMask": cgprsAccPtAggregIpMask,
       "cgprsAccPtAggregRowStatus": cgprsAccPtAggregRowStatus,
       "cgprsAccPtAggregCsgGroup": cgprsAccPtAggregCsgGroup,
       "cgprsAccPtExtTable": cgprsAccPtExtTable,
       "cgprsAccPtExtEntry": cgprsAccPtExtEntry,
       "cgprsAccPtIPAccListInEnable": cgprsAccPtIPAccListInEnable,
       "cgprsAccPtIPAccListOutEnable": cgprsAccPtIPAccListOutEnable,
       "cgprsAccPtGtpRespMesgWaitAcctng": cgprsAccPtGtpRespMesgWaitAcctng,
       "cgprsAccPtImsiSuppressed": cgprsAccPtImsiSuppressed,
       "cgprsAccPtVerifyUpStrTpduSrcAddr": cgprsAccPtVerifyUpStrTpduSrcAddr,
       "cgprsAccPtVerifyUpStrTpduDstAddr": cgprsAccPtVerifyUpStrTpduDstAddr,
       "cgprsAccPtRedirInterMobilAddrTyp": cgprsAccPtRedirInterMobilAddrTyp,
       "cgprsAccPtRedirInterMobilAddr": cgprsAccPtRedirInterMobilAddr,
       "cgprsAccPtSuppressRadiusAttribs": cgprsAccPtSuppressRadiusAttribs,
       "cgprsAccPtInterimAccountinEnable": cgprsAccPtInterimAccountinEnable,
       "cgprsAccPtSetRadiusAttributes": cgprsAccPtSetRadiusAttributes,
       "cgprsAccPtOperationMode": cgprsAccPtOperationMode,
       "cgprsAccPtAbsoluteSessionTimer": cgprsAccPtAbsoluteSessionTimer,
       "cgprsAccPtRadiusAttrNasId": cgprsAccPtRadiusAttrNasId,
       "cgprsAccPtPdpInServicePolicyName": cgprsAccPtPdpInServicePolicyName,
       "cgprsAccPtPdpOutServicePolicyNam": cgprsAccPtPdpOutServicePolicyNam,
       "cgprsAccPtPppRegenVerifyDomain": cgprsAccPtPppRegenVerifyDomain,
       "cgprsAccPtIpAddrLocalPoolName": cgprsAccPtIpAddrLocalPoolName,
       "cgprsAccPtServiceAware": cgprsAccPtServiceAware,
       "cgprsAccPtAdvDownlinkNextHopAddrType": cgprsAccPtAdvDownlinkNextHopAddrType,
       "cgprsAccPtAdvDownlinkNextHopAddr": cgprsAccPtAdvDownlinkNextHopAddr,
       "cgprsAccPtGtpUpdateFailDelete": cgprsAccPtGtpUpdateFailDelete,
       "cgprsAccPtAaaAccountInterPeriod": cgprsAccPtAaaAccountInterPeriod,
       "cgprsAccPtAaaAccountInterRadius": cgprsAccPtAaaAccountInterRadius,
       "cgprsAccPtGxEnable": cgprsAccPtGxEnable,
       "cgprsAccPtPcscfLoadBalance": cgprsAccPtPcscfLoadBalance,
       "cgprsAccPtNetworkBehindMsEnable": cgprsAccPtNetworkBehindMsEnable,
       "cgprsAccPtMaxSubnetsBehindMobile": cgprsAccPtMaxSubnetsBehindMobile,
       "cgprsAccPtChargingRecordType": cgprsAccPtChargingRecordType,
       "cgprsAccPtChargingGrp": cgprsAccPtChargingGrp,
       "cgprsAccPtIpAddrPoolNoRedistribute": cgprsAccPtIpAddrPoolNoRedistribute,
       "cgprsAccPtDualAddrEnabled": cgprsAccPtDualAddrEnabled,
       "cgprsAccPtVerifyDownlinkAddr": cgprsAccPtVerifyDownlinkAddr,
       "cgprsAccPtGenServerConfigs": cgprsAccPtGenServerConfigs,
       "cgprsAccPtGenServerConfigTable": cgprsAccPtGenServerConfigTable,
       "cgprsAccPtGenServerConfigEntry": cgprsAccPtGenServerConfigEntry,
       "cgprsAccPtDnsServerAddrType": cgprsAccPtDnsServerAddrType,
       "cgprsAccPtPriDnsServer": cgprsAccPtPriDnsServer,
       "cgprsAccPtSecDnsServer": cgprsAccPtSecDnsServer,
       "cgprsAccPtNetbiosServerAddrType": cgprsAccPtNetbiosServerAddrType,
       "cgprsAccPtPriNetbiosServer": cgprsAccPtPriNetbiosServer,
       "cgprsAccPtSecNetbiosServer": cgprsAccPtSecNetbiosServer,
       "cgprsAccPtImsConfigs": cgprsAccPtImsConfigs,
       "cgprsAccPtImsConfigTable": cgprsAccPtImsConfigTable,
       "cgprsAccPtImsConfigEntry": cgprsAccPtImsConfigEntry,
       "cgprsAccPtImsEnable": cgprsAccPtImsEnable,
       "cgprsAccPtPCscfGroupName": cgprsAccPtPCscfGroupName,
       "cgprsAccPtImsSigAccGroupIn": cgprsAccPtImsSigAccGroupIn,
       "cgprsAccPtImsSigAccGroupOut": cgprsAccPtImsSigAccGroupOut,
       "cgprsAccPtRejNonImsPdp": cgprsAccPtRejNonImsPdp,
       "cgprsAccPtChargingParams": cgprsAccPtChargingParams,
       "cgprsAccPtChgProfTable": cgprsAccPtChgProfTable,
       "cgprsAccPtChgProfEntry": cgprsAccPtChgProfEntry,
       "cgprsAccPtMsType": cgprsAccPtMsType,
       "cgprsAccPtChgProfile": cgprsAccPtChgProfile,
       "cgprsAccPtChgProfOverride": cgprsAccPtChgProfOverride,
       "cgprsAccPtChgProfRowStatus": cgprsAccPtChgProfRowStatus,
       "cgprsAccPtCacConfigs": cgprsAccPtCacConfigs,
       "cgprsAccPtCacTable": cgprsAccPtCacTable,
       "cgprsAccPtCacEntry": cgprsAccPtCacEntry,
       "cgprsAccPtCacPolicyName": cgprsAccPtCacPolicyName,
       "cgprsAccPtCacUpStrBandWidthPool": cgprsAccPtCacUpStrBandWidthPool,
       "cgprsAccPtCacDnStrBandWidthPool": cgprsAccPtCacDnStrBandWidthPool,
       "cgprsAccPtRouteProbeConfigs": cgprsAccPtRouteProbeConfigs,
       "cgprsAccPtRouteProbeTable": cgprsAccPtRouteProbeTable,
       "cgprsAccPtRouteProbeEntry": cgprsAccPtRouteProbeEntry,
       "cgprsAccPtRpDestAddrType": cgprsAccPtRpDestAddrType,
       "cgprsAccPtRpDestAddr": cgprsAccPtRpDestAddr,
       "cgprsAccPtRpProtocol": cgprsAccPtRpProtocol,
       "cgprsAccPtRpDestPort": cgprsAccPtRpDestPort,
       "cgprsAccPtRpTtl": cgprsAccPtRpTtl,
       "cgprsAccPtIpv6Configs": cgprsAccPtIpv6Configs,
       "cgprsAccPtIpv6Table": cgprsAccPtIpv6Table,
       "cgprsAccPtIpv6Entry": cgprsAccPtIpv6Entry,
       "cgprsAccPtIpv6BaseVTemplate": cgprsAccPtIpv6BaseVTemplate,
       "cgprsAccPtIpv6DnsAddrType": cgprsAccPtIpv6DnsAddrType,
       "cgprsAccPtIpv6DnsPriAddress": cgprsAccPtIpv6DnsPriAddress,
       "cgprsAccPtIpv6DnsSecAddress": cgprsAccPtIpv6DnsSecAddress,
       "cgprsAccPtIpv6Enable": cgprsAccPtIpv6Enable,
       "cgprsAccPtIpv6Exclusive": cgprsAccPtIpv6Exclusive,
       "cgprsAccPtIpv6AccessGroupDown": cgprsAccPtIpv6AccessGroupDown,
       "cgprsAccPtIpv6AccessGroupUp": cgprsAccPtIpv6AccessGroupUp,
       "cgprsAccPtIpv6AddrPool": cgprsAccPtIpv6AddrPool,
       "cgprsAccPtIpv6AddrLocalPoolName": cgprsAccPtIpv6AddrLocalPoolName,
       "cgprsAccPtIpv6Redirect": cgprsAccPtIpv6Redirect,
       "cgprsAccPtIpv6RedirectAddrType": cgprsAccPtIpv6RedirectAddrType,
       "cgprsAccPtIpv6RedirectAddr": cgprsAccPtIpv6RedirectAddr,
       "cgprsAccPtIpv6SecurityVerifySrc": cgprsAccPtIpv6SecurityVerifySrc,
       "cgprsAccPtIpv6SecurityVerifyDst": cgprsAccPtIpv6SecurityVerifyDst,
       "cgprsAccPtIpv6AddrAllocations": cgprsAccPtIpv6AddrAllocations,
       "cgprsAccPtDhcpv6ProxClientIntf": cgprsAccPtDhcpv6ProxClientIntf,
       "cgprsAccptDhcpv6RapidCommit": cgprsAccptDhcpv6RapidCommit,
       "cgprsAccptDhcpv6PoolName": cgprsAccptDhcpv6PoolName,
       "cgprsAccPtCsgGroupTable": cgprsAccPtCsgGroupTable,
       "cgprsAccPtCsgGroupEntry": cgprsAccPtCsgGroupEntry,
       "cgprsAccPtCsgGroupName": cgprsAccPtCsgGroupName,
       "cgprsAccPtCsgGroupRowStatus": cgprsAccPtCsgGroupRowStatus,
       "ciscoGprsAccPtCfgNotifInfo": ciscoGprsAccPtCfgNotifInfo,
       "cgprsAccPtCfgNotifHistTable": cgprsAccPtCfgNotifHistTable,
       "cgprsAccPtCfgNotifHistEntry": cgprsAccPtCfgNotifHistEntry,
       "cgprsAccPtCfgNotifIndex": cgprsAccPtCfgNotifIndex,
       "cgprsAccPtCfgNotifAccPtIndex": cgprsAccPtCfgNotifAccPtIndex,
       "cgprsAccPtCfgNotifReason": cgprsAccPtCfgNotifReason,
       "cgprsAccPtCfgNotifEnable": cgprsAccPtCfgNotifEnable,
       "cgprsAccPtCfgNotifHistMax": cgprsAccPtCfgNotifHistMax,
       "cgprsAccPtCfgNotifLatestIndex": cgprsAccPtCfgNotifLatestIndex,
       "ciscoGprsAccPtStatistics": ciscoGprsAccPtStatistics,
       "cgprsAccPtStatisticsTable": cgprsAccPtStatisticsTable,
       "cgprsAccPtStatisticsEntry": cgprsAccPtStatisticsEntry,
       "cgprsAccPtMsActivatedPdps": cgprsAccPtMsActivatedPdps,
       "cgprsAccPtSuccMsActivatedPdps": cgprsAccPtSuccMsActivatedPdps,
       "cgprsAccPtMsActivatedDynPdps": cgprsAccPtMsActivatedDynPdps,
       "cgprsAccPtSuccMsActivatedDynPdps": cgprsAccPtSuccMsActivatedDynPdps,
       "cgprsAccPtMsDeactivatedPdps": cgprsAccPtMsDeactivatedPdps,
       "cgprsAccPtSuccMsDeactivatedPdps": cgprsAccPtSuccMsDeactivatedPdps,
       "cgprsAccPtNetworkInitPdps": cgprsAccPtNetworkInitPdps,
       "cgprsAccPtSuccNetworkInitPdps": cgprsAccPtSuccNetworkInitPdps,
       "cgprsAccPtGgsnDeactivatedPdps": cgprsAccPtGgsnDeactivatedPdps,
       "cgprsAccPtSuccGgsDeactivatedPdps": cgprsAccPtSuccGgsDeactivatedPdps,
       "cgprsAccPtActivePdps": cgprsAccPtActivePdps,
       "cgprsAccPtUpstreamTrafficVol": cgprsAccPtUpstreamTrafficVol,
       "cgprsAccPtDownstreamTrafficVol": cgprsAccPtDownstreamTrafficVol,
       "cgprsAccPtSourceAddrViolTpdus": cgprsAccPtSourceAddrViolTpdus,
       "cgprsAccPtDestAddrViolTpdus": cgprsAccPtDestAddrViolTpdus,
       "cgprsAccPtRedirInterMobilTraffic": cgprsAccPtRedirInterMobilTraffic,
       "cgprsAccPtRevUpstreamTrafficVol": cgprsAccPtRevUpstreamTrafficVol,
       "cgprsAccPtRevDownstrTrafficVol": cgprsAccPtRevDownstrTrafficVol,
       "cgprsAccPtUpstreamPacketCount": cgprsAccPtUpstreamPacketCount,
       "cgprsAccPtDownstreamPacketCount": cgprsAccPtDownstreamPacketCount,
       "cgprsAccPtDhcpAddrRequests": cgprsAccPtDhcpAddrRequests,
       "cgprsAccPtSuccDhcpAddrRequests": cgprsAccPtSuccDhcpAddrRequests,
       "cgprsAccPtDhcpAddrReleases": cgprsAccPtDhcpAddrReleases,
       "cgprsAccPtIpv6MsActivatedPdps": cgprsAccPtIpv6MsActivatedPdps,
       "cgprsAccPtIpv6MsSuccActivatedPdps": cgprsAccPtIpv6MsSuccActivatedPdps,
       "cgprsAccPtIpv6NetworkInitDeactPdps": cgprsAccPtIpv6NetworkInitDeactPdps,
       "cgprsAccPtIpv6NetworkInitDeactSuccPdps": cgprsAccPtIpv6NetworkInitDeactSuccPdps,
       "cgprsAccPtIpv6MsActivatedDynPdps": cgprsAccPtIpv6MsActivatedDynPdps,
       "cgprsAccPtIpv6MsSuccActivatedDynPdps": cgprsAccPtIpv6MsSuccActivatedDynPdps,
       "cgprsAccPtIpv6MsDeactivatedPdps": cgprsAccPtIpv6MsDeactivatedPdps,
       "cgprsAccPtIpv6MsSuccDeactivatedPdps": cgprsAccPtIpv6MsSuccDeactivatedPdps,
       "cgprsAccPtIpv6GgsnDeactivatedPdps": cgprsAccPtIpv6GgsnDeactivatedPdps,
       "cgprsAccPtIpv6GgsnSuccDeactivatedPdps": cgprsAccPtIpv6GgsnSuccDeactivatedPdps,
       "cgprsAccPtIpv6UpstreamTrafficVolume": cgprsAccPtIpv6UpstreamTrafficVolume,
       "cgprsAccPtIpv6DownstreamTrafficVolume": cgprsAccPtIpv6DownstreamTrafficVolume,
       "cgprsAccPtIpv6UpstreamPackets": cgprsAccPtIpv6UpstreamPackets,
       "cgprsAccPtIpv6DownstreamPackets": cgprsAccPtIpv6DownstreamPackets,
       "cgprsAccPtPdpUpdateReqSent": cgprsAccPtPdpUpdateReqSent,
       "cgprsAccPtSuccPdpUpdateResRcvd": cgprsAccPtSuccPdpUpdateResRcvd,
       "cgprsAccPtCoaRcvd": cgprsAccPtCoaRcvd,
       "cgprsAccPtCoaSuccess": cgprsAccPtCoaSuccess,
       "cgprsAccPtDtEnabled": cgprsAccPtDtEnabled,
       "cgprsAccPtTotalBearers": cgprsAccPtTotalBearers,
       "cgprsAccPtTotRmtInitCreateBearers": cgprsAccPtTotRmtInitCreateBearers,
       "cgprsAccPtSuccRmtInitCreateBearers": cgprsAccPtSuccRmtInitCreateBearers,
       "cgprsAccPtNetworkInitDeleteBearers": cgprsAccPtNetworkInitDeleteBearers,
       "cgprsAccPtTotRmtInitModifyBearers": cgprsAccPtTotRmtInitModifyBearers,
       "cgprsAccPtSuccRmtInitModifyBearers": cgprsAccPtSuccRmtInitModifyBearers,
       "cgprsAccPtTotNetworkInitUpdateBearers": cgprsAccPtTotNetworkInitUpdateBearers,
       "cgprsAccPtSuccNetworkInitUpdateBearers": cgprsAccPtSuccNetworkInitUpdateBearers,
       "cgprsAccPtTotNetworkInitCreateDedBearers": cgprsAccPtTotNetworkInitCreateDedBearers,
       "cgprsAccPtSuccNetworkInitCreateDedBearers": cgprsAccPtSuccNetworkInitCreateDedBearers,
       "cgprsAccPtTotNetworkInitCreateIPv6DedBearers": cgprsAccPtTotNetworkInitCreateIPv6DedBearers,
       "cgprsAccPtSuccNetworkInitCreateIPv6DedBearers": cgprsAccPtSuccNetworkInitCreateIPv6DedBearers,
       "cgprsAccPtv4v6MsActivatedPdps": cgprsAccPtv4v6MsActivatedPdps,
       "cgprsAccPtv4v6SuccMsActivatedPdps": cgprsAccPtv4v6SuccMsActivatedPdps,
       "cgprsAccPtv4v6MsDeactivatedPdps": cgprsAccPtv4v6MsDeactivatedPdps,
       "cgprsAccPtv4v6SuccMsDeactivatedPdps": cgprsAccPtv4v6SuccMsDeactivatedPdps,
       "cgprsAccPtv4v6ActDedbearerPdps": cgprsAccPtv4v6ActDedbearerPdps,
       "cgprsAccPtv4v6SuccActDedbearerPdps": cgprsAccPtv4v6SuccActDedbearerPdps,
       "cgprsAccPtDhcpProxServDiscover": cgprsAccPtDhcpProxServDiscover,
       "cgprsAccPtDhcpProxServRequest": cgprsAccPtDhcpProxServRequest,
       "cgprsAccPtDhcpProxServDeclines": cgprsAccPtDhcpProxServDeclines,
       "cgprsAccPtDhcpProxServRelease": cgprsAccPtDhcpProxServRelease,
       "cgprsAccPtDhcpProxServOffer": cgprsAccPtDhcpProxServOffer,
       "cgprsAccPtDhcpProxServAcks": cgprsAccPtDhcpProxServAcks,
       "cgprsAccPtDhcpProxServNaks": cgprsAccPtDhcpProxServNaks,
       "cgprsAccPtDhcpProxServInform": cgprsAccPtDhcpProxServInform,
       "cgprsAccPtDhcpProxServUnknowMsg": cgprsAccPtDhcpProxServUnknowMsg,
       "cgprsAccPtDhcpProxServRetryDrops": cgprsAccPtDhcpProxServRetryDrops,
       "cgprsAccPtDhcpProxServErrDrops": cgprsAccPtDhcpProxServErrDrops,
       "cgprsAccPtActiveBearers": cgprsAccPtActiveBearers,
       "cgprsAccPtDhcpProxServTxErrDrops": cgprsAccPtDhcpProxServTxErrDrops,
       "cgprsAccPtDhcpProxServIpAllocErr": cgprsAccPtDhcpProxServIpAllocErr,
       "cgprsAccPtDedBearerDeactivations": cgprsAccPtDedBearerDeactivations,
       "cgprsAccPtDedBearerQosUpdate": cgprsAccPtDedBearerQosUpdate,
       "cgprsAccPtDedBearerSucQosUpdate": cgprsAccPtDedBearerSucQosUpdate,
       "cgprsAccPtDedBearerNoQosUpdate": cgprsAccPtDedBearerNoQosUpdate,
       "cgprsAccPtDedBearerSucNoQosUpdate": cgprsAccPtDedBearerSucNoQosUpdate,
       "cgprsAccPtIpv4v6MsActivatedDynamicPdps": cgprsAccPtIpv4v6MsActivatedDynamicPdps,
       "cgprsAccPtIpv4v6MsSuccActivatedDynamicPdps": cgprsAccPtIpv4v6MsSuccActivatedDynamicPdps,
       "cgprsAccPtFailMsActivatedPdps": cgprsAccPtFailMsActivatedPdps,
       "cgprsAccPtFailPdpUpdate": cgprsAccPtFailPdpUpdate,
       "cgprsAccPtUpdateRspTimeOut": cgprsAccPtUpdateRspTimeOut,
       "cgprsAccPtDhcpv6ProxyStatsTable": cgprsAccPtDhcpv6ProxyStatsTable,
       "cgprsAccPtDhcpv6ProxyStatsEntry": cgprsAccPtDhcpv6ProxyStatsEntry,
       "cgprsAccPtDhcpv6ProxInforeqRcvd": cgprsAccPtDhcpv6ProxInforeqRcvd,
       "cgprsAccPtDhcpv6ProxInforeqRply": cgprsAccPtDhcpv6ProxInforeqRply,
       "cgprsAccPtDhcpv6ProxInforeqLocRply": cgprsAccPtDhcpv6ProxInforeqLocRply,
       "cgprsAccPtDhcpv6ProxIpAllocSuc": cgprsAccPtDhcpv6ProxIpAllocSuc,
       "cgprsAccPtDhcpv6ProxIpAllocFail": cgprsAccPtDhcpv6ProxIpAllocFail,
       "cgprsAccPtDhcpv6ProxIpRelease": cgprsAccPtDhcpv6ProxIpRelease,
       "cgprsAccPtDhcpv6ProxIpRenewFail": cgprsAccPtDhcpv6ProxIpRenewFail,
       "cgprsAccPtDhcpv6ProxUnkwnMsg": cgprsAccPtDhcpv6ProxUnkwnMsg,
       "cgprsAccPtDhcpv6ProxErrs": cgprsAccPtDhcpv6ProxErrs,
       "cgprsAccPtThruputStatsTable": cgprsAccPtThruputStatsTable,
       "cgprsAccPtThruputStatsEntry": cgprsAccPtThruputStatsEntry,
       "cgprsAccPtThruputInterval": cgprsAccPtThruputInterval,
       "cgprsAccPtThruPutLastCollected": cgprsAccPtThruPutLastCollected,
       "cgprsAccPtUpstrByteCount": cgprsAccPtUpstrByteCount,
       "cgprsAccPtDownstrByteCount": cgprsAccPtDownstrByteCount,
       "cgprsAccPtUpstrPktCount": cgprsAccPtUpstrPktCount,
       "cgprsAccPtDownstrPktCount": cgprsAccPtDownstrPktCount,
       "ciscoGprsAccPtNotifInfo": ciscoGprsAccPtNotifInfo,
       "cgprsAccPtMsAddrType": cgprsAccPtMsAddrType,
       "cgprsAccPtMsAllocAddr": cgprsAccPtMsAllocAddr,
       "cgprsAccPtMsNewAddr": cgprsAccPtMsNewAddr,
       "cgprsAccPtMsTpduDstAddr": cgprsAccPtMsTpduDstAddr,
       "cgprsAccPtMIBNotificationPrefix": cgprsAccPtMIBNotificationPrefix,
       "cgprsAccPtMIBNotifications": cgprsAccPtMIBNotifications,
       "cgprsAccPtCfgNotif": cgprsAccPtCfgNotif,
       "cgprsAccPtSecSrcViolNotif": cgprsAccPtSecSrcViolNotif,
       "cgprsAccPtSecDestViolNotif": cgprsAccPtSecDestViolNotif,
       "cgprsAccPtMaintenanceNotif": cgprsAccPtMaintenanceNotif,
       "cgprsAccPtInServiceNotif": cgprsAccPtInServiceNotif,
       "cgprsAccPtConformances": cgprsAccPtConformances,
       "cgprsAccPtMIBCompliances": cgprsAccPtMIBCompliances,
       "cgprsAccPtMIBCompliance": cgprsAccPtMIBCompliance,
       "cgprsAccPtMIBComplianceRev1": cgprsAccPtMIBComplianceRev1,
       "cgprsAccPtMIBComplianceRev2": cgprsAccPtMIBComplianceRev2,
       "cgprsAccPtMIBComplianceRev3": cgprsAccPtMIBComplianceRev3,
       "cgprsAccPtMIBComplianceRev4": cgprsAccPtMIBComplianceRev4,
       "cgprsAccPtMIBComplianceRev5": cgprsAccPtMIBComplianceRev5,
       "cgprsAccPtMIBComplianceRev6": cgprsAccPtMIBComplianceRev6,
       "cgprsAccPtMIBComplianceRev7": cgprsAccPtMIBComplianceRev7,
       "cgprsAccPtMIBComplianceRev8": cgprsAccPtMIBComplianceRev8,
       "cgprsAccPtMIBComplianceRev9": cgprsAccPtMIBComplianceRev9,
       "cgprsAccPtMIBComplianceRev10": cgprsAccPtMIBComplianceRev10,
       "cgprsAccPtMIBComplianceRev11": cgprsAccPtMIBComplianceRev11,
       "cgprsAccPtMIBComplianceRev12": cgprsAccPtMIBComplianceRev12,
       "cgprsAccPtMIBComplianceRev13": cgprsAccPtMIBComplianceRev13,
       "cgprsAccPtMIBComplianceRev14": cgprsAccPtMIBComplianceRev14,
       "cgprsAccPtMIBComplianceRev15": cgprsAccPtMIBComplianceRev15,
       "cgprsAccPtMIBGroups": cgprsAccPtMIBGroups,
       "cgprsAccPtMIBGroup": cgprsAccPtMIBGroup,
       "cgprsAccPtCfgNotifGroup": cgprsAccPtCfgNotifGroup,
       "cgprsAccPtStatisticsGroup": cgprsAccPtStatisticsGroup,
       "cgprsAccPtMIBGroupRev1": cgprsAccPtMIBGroupRev1,
       "cgprsAccPtExtMIBGroup": cgprsAccPtExtMIBGroup,
       "cgprsAccPtMIBNotifGroup": cgprsAccPtMIBNotifGroup,
       "cgprsAccPtExtMIBGroupRev1": cgprsAccPtExtMIBGroupRev1,
       "cgprsAccPtStatisticsGroupRev1": cgprsAccPtStatisticsGroupRev1,
       "cgprsAccPtExtMIBGroupRev2": cgprsAccPtExtMIBGroupRev2,
       "cgprsAccPtExtMIBGroupRev3": cgprsAccPtExtMIBGroupRev3,
       "cgprsAccPtGenServerGroup": cgprsAccPtGenServerGroup,
       "cgprsAccPtImsGroup": cgprsAccPtImsGroup,
       "cgprsAccPtChargingGroup": cgprsAccPtChargingGroup,
       "cgprsAccPtCacGroup": cgprsAccPtCacGroup,
       "cgprsAccPtRouteProbeGroup": cgprsAccPtRouteProbeGroup,
       "cgprsAccPtStatisticsGroupRev2": cgprsAccPtStatisticsGroupRev2,
       "cgprsAccPtThruPutGroup": cgprsAccPtThruPutGroup,
       "cgprsAccPtNotifInfoGroup": cgprsAccPtNotifInfoGroup,
       "cgprsAccPtMIBNotifGroupRev1": cgprsAccPtMIBNotifGroupRev1,
       "cgprsAccPtMIBR60Group": cgprsAccPtMIBR60Group,
       "cgprsAccPtIpv6Group": cgprsAccPtIpv6Group,
       "cgprsAccPtStatisticsGroupRev3": cgprsAccPtStatisticsGroupRev3,
       "cgprsAccPtPcscfGroup": cgprsAccPtPcscfGroup,
       "cgprsAccPtMIBR80Group": cgprsAccPtMIBR80Group,
       "cgprsAccPtStatisticsGroupSup1": cgprsAccPtStatisticsGroupSup1,
       "cgprsAccPtMIBR80GroupSup1": cgprsAccPtMIBR80GroupSup1,
       "cgprsAccPtMIBR90Group": cgprsAccPtMIBR90Group,
       "cgprsAccPtStatisticsGroupSup2": cgprsAccPtStatisticsGroupSup2,
       "cgprsAccPtMIBR92Group": cgprsAccPtMIBR92Group,
       "cgprsAccPtMIBR90GroupRev1": cgprsAccPtMIBR90GroupRev1,
       "cgprsAccPtMIBR100Group": cgprsAccPtMIBR100Group,
       "cgprsAccPtStatisticsGroupSup3": cgprsAccPtStatisticsGroupSup3,
       "cgprsAccPtExtMIBGroupSup1": cgprsAccPtExtMIBGroupSup1,
       "cgprsAccPtIpv6GroupSup1": cgprsAccPtIpv6GroupSup1,
       "cgprsAccPtStatisticsGroupSup4": cgprsAccPtStatisticsGroupSup4,
       "cgprsAccPtDhcpv6ProxyStatsGroup": cgprsAccPtDhcpv6ProxyStatsGroup,
       "cgprsAccPtExtMIBGroupSup2": cgprsAccPtExtMIBGroupSup2,
       "cgprsAccPtStatisticsGroupSup5": cgprsAccPtStatisticsGroupSup5,
       "cgprsAccPtStatisticsGroupSup6": cgprsAccPtStatisticsGroupSup6}
)
