# SNMP MIB module (Unisphere-Data-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:14 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdName,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdName")


# MODULE-IDENTITY

usdAaaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20)
)
usdAaaMIB.setRevisions(
        ("2002-08-02 12:50",
         "2002-08-01 19:50",
         "2001-10-05 13:25",
         "2001-10-03 19:05",
         "2001-03-01 17:03",
         "2001-02-12 19:54",
         "2000-05-18 00:00",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdAaaDomainName(OctetString, TextualConvention):
    status = "current"
    displayHint = "63a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class UsdAaaAuthenticationMethods(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("protocolLine", 5),
          ("protocolNone", 4),
          ("protocolRadius", 1))
    )



class UsdAaaAccountingMethods(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("protocolNone", 4),
          ("protocolRadius", 1))
    )



class UsdAddressAssignType(Integer32, TextualConvention):
    status = "current"
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
        *(("dhcp", 3),
          ("localPool", 2),
          ("none", 0),
          ("radius", 1),
          ("user", 4))
    )



class UsdSubscriberState(Bits, TextualConvention):
    status = "current"


class UsdSubscriberClientType(Integer32, TextualConvention):
    status = "current"
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
        *(("config", 3),
          ("ip", 2),
          ("login", 1),
          ("other", 5),
          ("ppp", 0),
          ("tunnel", 4))
    )



class UsdSubscriberLocationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slotPort", 1),
          ("unknown", 0))
    )



class UsdSubscriberLocationValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



# MIB Managed Objects in the order of their OIDs

_UsdAaaObjects_ObjectIdentity = ObjectIdentity
usdAaaObjects = _UsdAaaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1)
)
_UsdAaaAssignment_ObjectIdentity = ObjectIdentity
usdAaaAssignment = _UsdAaaAssignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1)
)
_UsdAaaAssignGeneral_ObjectIdentity = ObjectIdentity
usdAaaAssignGeneral = _UsdAaaAssignGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1)
)


class _UsdAaaAssignBrasLicense_Type(DisplayString):
    """Custom type usdAaaAssignBrasLicense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UsdAaaAssignBrasLicense_Type.__name__ = "DisplayString"
_UsdAaaAssignBrasLicense_Object = MibScalar
usdAaaAssignBrasLicense = _UsdAaaAssignBrasLicense_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 1),
    _UsdAaaAssignBrasLicense_Type()
)
usdAaaAssignBrasLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAssignBrasLicense.setStatus("current")
_UsdAaaAssignBrasLicensedUsers_Type = Integer32
_UsdAaaAssignBrasLicensedUsers_Object = MibScalar
usdAaaAssignBrasLicensedUsers = _UsdAaaAssignBrasLicensedUsers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 2),
    _UsdAaaAssignBrasLicensedUsers_Type()
)
usdAaaAssignBrasLicensedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaAssignBrasLicensedUsers.setStatus("current")


class _UsdAaaAssignDomainDelimiters_Type(DisplayString):
    """Custom type usdAaaAssignDomainDelimiters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UsdAaaAssignDomainDelimiters_Type.__name__ = "DisplayString"
_UsdAaaAssignDomainDelimiters_Object = MibScalar
usdAaaAssignDomainDelimiters = _UsdAaaAssignDomainDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 3),
    _UsdAaaAssignDomainDelimiters_Type()
)
usdAaaAssignDomainDelimiters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAssignDomainDelimiters.setStatus("current")


class _UsdAaaAssignRealmDelimiters_Type(DisplayString):
    """Custom type usdAaaAssignRealmDelimiters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UsdAaaAssignRealmDelimiters_Type.__name__ = "DisplayString"
_UsdAaaAssignRealmDelimiters_Object = MibScalar
usdAaaAssignRealmDelimiters = _UsdAaaAssignRealmDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 4),
    _UsdAaaAssignRealmDelimiters_Type()
)
usdAaaAssignRealmDelimiters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAssignRealmDelimiters.setStatus("current")


class _UsdAaaAssignDomainParseOrder_Type(Integer32):
    """Custom type usdAaaAssignDomainParseOrder based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domainFirst", 1),
          ("realmFirst", 2))
    )


_UsdAaaAssignDomainParseOrder_Type.__name__ = "Integer32"
_UsdAaaAssignDomainParseOrder_Object = MibScalar
usdAaaAssignDomainParseOrder = _UsdAaaAssignDomainParseOrder_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 5),
    _UsdAaaAssignDomainParseOrder_Type()
)
usdAaaAssignDomainParseOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAssignDomainParseOrder.setStatus("current")


class _UsdAaaAssignSubscriberLimit_Type(Integer32):
    """Custom type usdAaaAssignSubscriberLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_UsdAaaAssignSubscriberLimit_Type.__name__ = "Integer32"
_UsdAaaAssignSubscriberLimit_Object = MibScalar
usdAaaAssignSubscriberLimit = _UsdAaaAssignSubscriberLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 6),
    _UsdAaaAssignSubscriberLimit_Type()
)
usdAaaAssignSubscriberLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAssignSubscriberLimit.setStatus("current")
if mibBuilder.loadTexts:
    usdAaaAssignSubscriberLimit.setUnits("users")
_UsdAaaAssignDomain_ObjectIdentity = ObjectIdentity
usdAaaAssignDomain = _UsdAaaAssignDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2)
)
_UsdAaaAssignDomainTable_Object = MibTable
usdAaaAssignDomainTable = _UsdAaaAssignDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdAaaAssignDomainTable.setStatus("current")
_UsdAaaAssignDomainEntry_Object = MibTableRow
usdAaaAssignDomainEntry = _UsdAaaAssignDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1)
)
usdAaaAssignDomainEntry.setIndexNames(
    (1, "Unisphere-Data-AAA-MIB", "usdAaaAssignDomainName"),
)
if mibBuilder.loadTexts:
    usdAaaAssignDomainEntry.setStatus("current")
_UsdAaaAssignDomainName_Type = UsdAaaDomainName
_UsdAaaAssignDomainName_Object = MibTableColumn
usdAaaAssignDomainName = _UsdAaaAssignDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 1),
    _UsdAaaAssignDomainName_Type()
)
usdAaaAssignDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaAssignDomainName.setStatus("current")
_UsdAaaAssignDomainRowStatus_Type = RowStatus
_UsdAaaAssignDomainRowStatus_Object = MibTableColumn
usdAaaAssignDomainRowStatus = _UsdAaaAssignDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 2),
    _UsdAaaAssignDomainRowStatus_Type()
)
usdAaaAssignDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainRowStatus.setStatus("current")
_UsdAaaAssignDomainRouterName_Type = UsdName
_UsdAaaAssignDomainRouterName_Object = MibTableColumn
usdAaaAssignDomainRouterName = _UsdAaaAssignDomainRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 3),
    _UsdAaaAssignDomainRouterName_Type()
)
usdAaaAssignDomainRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainRouterName.setStatus("current")


class _UsdAaaAssignDomainLoopback_Type(Integer32):
    """Custom type usdAaaAssignDomainLoopback based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32000),
    )


_UsdAaaAssignDomainLoopback_Type.__name__ = "Integer32"
_UsdAaaAssignDomainLoopback_Object = MibTableColumn
usdAaaAssignDomainLoopback = _UsdAaaAssignDomainLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 4),
    _UsdAaaAssignDomainLoopback_Type()
)
usdAaaAssignDomainLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainLoopback.setStatus("current")


class _UsdAaaAssignDomainIpHint_Type(TruthValue):
    """Custom type usdAaaAssignDomainIpHint based on TruthValue"""


_UsdAaaAssignDomainIpHint_Object = MibTableColumn
usdAaaAssignDomainIpHint = _UsdAaaAssignDomainIpHint_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 5),
    _UsdAaaAssignDomainIpHint_Type()
)
usdAaaAssignDomainIpHint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainIpHint.setStatus("current")


class _UsdAaaAssignDomainAtmServiceLevel_Type(Integer32):
    """Custom type usdAaaAssignDomainAtmServiceLevel based on Integer32"""
    defaultValue = 0

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
        *(("cbr", 4),
          ("none", 0),
          ("nrtVbr", 3),
          ("ubr", 1),
          ("ubrPcr", 2))
    )


_UsdAaaAssignDomainAtmServiceLevel_Type.__name__ = "Integer32"
_UsdAaaAssignDomainAtmServiceLevel_Object = MibTableColumn
usdAaaAssignDomainAtmServiceLevel = _UsdAaaAssignDomainAtmServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 6),
    _UsdAaaAssignDomainAtmServiceLevel_Type()
)
usdAaaAssignDomainAtmServiceLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainAtmServiceLevel.setStatus("current")


class _UsdAaaAssignDomainAtmPcr_Type(Integer32):
    """Custom type usdAaaAssignDomainAtmPcr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAaaAssignDomainAtmPcr_Type.__name__ = "Integer32"
_UsdAaaAssignDomainAtmPcr_Object = MibTableColumn
usdAaaAssignDomainAtmPcr = _UsdAaaAssignDomainAtmPcr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 7),
    _UsdAaaAssignDomainAtmPcr_Type()
)
usdAaaAssignDomainAtmPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainAtmPcr.setStatus("current")
if mibBuilder.loadTexts:
    usdAaaAssignDomainAtmPcr.setUnits("kbps")


class _UsdAaaAssignDomainAtmScr_Type(Integer32):
    """Custom type usdAaaAssignDomainAtmScr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAaaAssignDomainAtmScr_Type.__name__ = "Integer32"
_UsdAaaAssignDomainAtmScr_Object = MibTableColumn
usdAaaAssignDomainAtmScr = _UsdAaaAssignDomainAtmScr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 8),
    _UsdAaaAssignDomainAtmScr_Type()
)
usdAaaAssignDomainAtmScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainAtmScr.setStatus("current")
if mibBuilder.loadTexts:
    usdAaaAssignDomainAtmScr.setUnits("kbps")


class _UsdAaaAssignDomainAtmMbs_Type(Integer32):
    """Custom type usdAaaAssignDomainAtmMbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdAaaAssignDomainAtmMbs_Type.__name__ = "Integer32"
_UsdAaaAssignDomainAtmMbs_Object = MibTableColumn
usdAaaAssignDomainAtmMbs = _UsdAaaAssignDomainAtmMbs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 9),
    _UsdAaaAssignDomainAtmMbs_Type()
)
usdAaaAssignDomainAtmMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainAtmMbs.setStatus("current")
if mibBuilder.loadTexts:
    usdAaaAssignDomainAtmMbs.setUnits("cells")


class _UsdAaaAssignDomainOverrideUserName_Type(DisplayString):
    """Custom type usdAaaAssignDomainOverrideUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdAaaAssignDomainOverrideUserName_Type.__name__ = "DisplayString"
_UsdAaaAssignDomainOverrideUserName_Object = MibTableColumn
usdAaaAssignDomainOverrideUserName = _UsdAaaAssignDomainOverrideUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 10),
    _UsdAaaAssignDomainOverrideUserName_Type()
)
usdAaaAssignDomainOverrideUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainOverrideUserName.setStatus("current")


class _UsdAaaAssignDomainOverridePassword_Type(OctetString):
    """Custom type usdAaaAssignDomainOverridePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdAaaAssignDomainOverridePassword_Type.__name__ = "OctetString"
_UsdAaaAssignDomainOverridePassword_Object = MibTableColumn
usdAaaAssignDomainOverridePassword = _UsdAaaAssignDomainOverridePassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 11),
    _UsdAaaAssignDomainOverridePassword_Type()
)
usdAaaAssignDomainOverridePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainOverridePassword.setStatus("current")


class _UsdAaaAssignDomainStripDomain_Type(TruthValue):
    """Custom type usdAaaAssignDomainStripDomain based on TruthValue"""


_UsdAaaAssignDomainStripDomain_Object = MibTableColumn
usdAaaAssignDomainStripDomain = _UsdAaaAssignDomainStripDomain_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 12),
    _UsdAaaAssignDomainStripDomain_Type()
)
usdAaaAssignDomainStripDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainStripDomain.setStatus("current")
_UsdAaaAssignDomainTunnelTable_Object = MibTable
usdAaaAssignDomainTunnelTable = _UsdAaaAssignDomainTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelTable.setStatus("current")
_UsdAaaAssignDomainTunnelEntry_Object = MibTableRow
usdAaaAssignDomainTunnelEntry = _UsdAaaAssignDomainTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1)
)
usdAaaAssignDomainTunnelEntry.setIndexNames(
    (0, "Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelName"),
    (0, "Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelTag"),
)
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelEntry.setStatus("current")
_UsdAaaAssignDomainTunnelName_Type = UsdAaaDomainName
_UsdAaaAssignDomainTunnelName_Object = MibTableColumn
usdAaaAssignDomainTunnelName = _UsdAaaAssignDomainTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 1),
    _UsdAaaAssignDomainTunnelName_Type()
)
usdAaaAssignDomainTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelName.setStatus("current")


class _UsdAaaAssignDomainTunnelTag_Type(Integer32):
    """Custom type usdAaaAssignDomainTunnelTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_UsdAaaAssignDomainTunnelTag_Type.__name__ = "Integer32"
_UsdAaaAssignDomainTunnelTag_Object = MibTableColumn
usdAaaAssignDomainTunnelTag = _UsdAaaAssignDomainTunnelTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 2),
    _UsdAaaAssignDomainTunnelTag_Type()
)
usdAaaAssignDomainTunnelTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelTag.setStatus("current")


class _UsdAaaAssignDomainTunnelPreference_Type(Integer32):
    """Custom type usdAaaAssignDomainTunnelPreference based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_UsdAaaAssignDomainTunnelPreference_Type.__name__ = "Integer32"
_UsdAaaAssignDomainTunnelPreference_Object = MibTableColumn
usdAaaAssignDomainTunnelPreference = _UsdAaaAssignDomainTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 3),
    _UsdAaaAssignDomainTunnelPreference_Type()
)
usdAaaAssignDomainTunnelPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelPreference.setStatus("current")


class _UsdAaaAssignDomainTunnelType_Type(Integer32):
    """Custom type usdAaaAssignDomainTunnelType based on Integer32"""
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
        *(("tunnelL2f", 3),
          ("tunnelL2tp", 1),
          ("tunnelUnknown", 2))
    )


_UsdAaaAssignDomainTunnelType_Type.__name__ = "Integer32"
_UsdAaaAssignDomainTunnelType_Object = MibTableColumn
usdAaaAssignDomainTunnelType = _UsdAaaAssignDomainTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 4),
    _UsdAaaAssignDomainTunnelType_Type()
)
usdAaaAssignDomainTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelType.setStatus("current")


class _UsdAaaAssignDomainTunnelMedium_Type(Integer32):
    """Custom type usdAaaAssignDomainTunnelMedium based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnelMediumIPv4", 1),
          ("tunnelMediumUnknown", 2))
    )


_UsdAaaAssignDomainTunnelMedium_Type.__name__ = "Integer32"
_UsdAaaAssignDomainTunnelMedium_Object = MibTableColumn
usdAaaAssignDomainTunnelMedium = _UsdAaaAssignDomainTunnelMedium_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 5),
    _UsdAaaAssignDomainTunnelMedium_Type()
)
usdAaaAssignDomainTunnelMedium.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelMedium.setStatus("current")


class _UsdAaaAssignDomainTunnelAddress_Type(DisplayString):
    """Custom type usdAaaAssignDomainTunnelAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdAaaAssignDomainTunnelAddress_Type.__name__ = "DisplayString"
_UsdAaaAssignDomainTunnelAddress_Object = MibTableColumn
usdAaaAssignDomainTunnelAddress = _UsdAaaAssignDomainTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 6),
    _UsdAaaAssignDomainTunnelAddress_Type()
)
usdAaaAssignDomainTunnelAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelAddress.setStatus("current")


class _UsdAaaAssignDomainTunnelPassword_Type(DisplayString):
    """Custom type usdAaaAssignDomainTunnelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdAaaAssignDomainTunnelPassword_Type.__name__ = "DisplayString"
_UsdAaaAssignDomainTunnelPassword_Object = MibTableColumn
usdAaaAssignDomainTunnelPassword = _UsdAaaAssignDomainTunnelPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 7),
    _UsdAaaAssignDomainTunnelPassword_Type()
)
usdAaaAssignDomainTunnelPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelPassword.setStatus("current")


class _UsdAaaAssignDomainTunnelId_Type(DisplayString):
    """Custom type usdAaaAssignDomainTunnelId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdAaaAssignDomainTunnelId_Type.__name__ = "DisplayString"
_UsdAaaAssignDomainTunnelId_Object = MibTableColumn
usdAaaAssignDomainTunnelId = _UsdAaaAssignDomainTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 8),
    _UsdAaaAssignDomainTunnelId_Type()
)
usdAaaAssignDomainTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelId.setStatus("current")


class _UsdAaaAssignDomainTunnelHostName_Type(DisplayString):
    """Custom type usdAaaAssignDomainTunnelHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UsdAaaAssignDomainTunnelHostName_Type.__name__ = "DisplayString"
_UsdAaaAssignDomainTunnelHostName_Object = MibTableColumn
usdAaaAssignDomainTunnelHostName = _UsdAaaAssignDomainTunnelHostName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 9),
    _UsdAaaAssignDomainTunnelHostName_Type()
)
usdAaaAssignDomainTunnelHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelHostName.setStatus("current")
_UsdAaaAssignDomainTunnelRowStatus_Type = RowStatus
_UsdAaaAssignDomainTunnelRowStatus_Object = MibTableColumn
usdAaaAssignDomainTunnelRowStatus = _UsdAaaAssignDomainTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 10),
    _UsdAaaAssignDomainTunnelRowStatus_Type()
)
usdAaaAssignDomainTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelRowStatus.setStatus("current")


class _UsdAaaAssignDomainTunnelServerName_Type(DisplayString):
    """Custom type usdAaaAssignDomainTunnelServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UsdAaaAssignDomainTunnelServerName_Type.__name__ = "DisplayString"
_UsdAaaAssignDomainTunnelServerName_Object = MibTableColumn
usdAaaAssignDomainTunnelServerName = _UsdAaaAssignDomainTunnelServerName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 11),
    _UsdAaaAssignDomainTunnelServerName_Type()
)
usdAaaAssignDomainTunnelServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelServerName.setStatus("current")


class _UsdAaaAssignDomainTunnelClientAddress_Type(DisplayString):
    """Custom type usdAaaAssignDomainTunnelClientAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdAaaAssignDomainTunnelClientAddress_Type.__name__ = "DisplayString"
_UsdAaaAssignDomainTunnelClientAddress_Object = MibTableColumn
usdAaaAssignDomainTunnelClientAddress = _UsdAaaAssignDomainTunnelClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 12),
    _UsdAaaAssignDomainTunnelClientAddress_Type()
)
usdAaaAssignDomainTunnelClientAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdAaaAssignDomainTunnelClientAddress.setStatus("current")
_UsdAaaAuthentication_ObjectIdentity = ObjectIdentity
usdAaaAuthentication = _UsdAaaAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2)
)
_UsdAaaAuthGeneral_ObjectIdentity = ObjectIdentity
usdAaaAuthGeneral = _UsdAaaAuthGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 1)
)


class _UsdAaaAuthMethods_Type(OctetString):
    """Custom type usdAaaAuthMethods based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_UsdAaaAuthMethods_Type.__name__ = "OctetString"
_UsdAaaAuthMethods_Object = MibScalar
usdAaaAuthMethods = _UsdAaaAuthMethods_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 1, 1),
    _UsdAaaAuthMethods_Type()
)
usdAaaAuthMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAuthMethods.setStatus("current")
_UsdAaaAccounting_ObjectIdentity = ObjectIdentity
usdAaaAccounting = _UsdAaaAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3)
)
_UsdAaaAcctGeneral_ObjectIdentity = ObjectIdentity
usdAaaAcctGeneral = _UsdAaaAcctGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1)
)


class _UsdAaaAcctInterval_Type(Integer32):
    """Custom type usdAaaAcctInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(600, 86400),
    )


_UsdAaaAcctInterval_Type.__name__ = "Integer32"
_UsdAaaAcctInterval_Object = MibScalar
usdAaaAcctInterval = _UsdAaaAcctInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 1),
    _UsdAaaAcctInterval_Type()
)
usdAaaAcctInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAcctInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdAaaAcctInterval.setUnits("seconds")
_UsdAaaAcctDupServerRouterName_Type = UsdName
_UsdAaaAcctDupServerRouterName_Object = MibScalar
usdAaaAcctDupServerRouterName = _UsdAaaAcctDupServerRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 2),
    _UsdAaaAcctDupServerRouterName_Type()
)
usdAaaAcctDupServerRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAcctDupServerRouterName.setStatus("current")


class _UsdAaaAcctMethods_Type(OctetString):
    """Custom type usdAaaAcctMethods based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_UsdAaaAcctMethods_Type.__name__ = "OctetString"
_UsdAaaAcctMethods_Object = MibScalar
usdAaaAcctMethods = _UsdAaaAcctMethods_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 3),
    _UsdAaaAcctMethods_Type()
)
usdAaaAcctMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAcctMethods.setStatus("current")


class _UsdAaaAcctSendStopOnAaaDeny_Type(TruthValue):
    """Custom type usdAaaAcctSendStopOnAaaDeny based on TruthValue"""


_UsdAaaAcctSendStopOnAaaDeny_Object = MibScalar
usdAaaAcctSendStopOnAaaDeny = _UsdAaaAcctSendStopOnAaaDeny_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 4),
    _UsdAaaAcctSendStopOnAaaDeny_Type()
)
usdAaaAcctSendStopOnAaaDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAcctSendStopOnAaaDeny.setStatus("current")


class _UsdAaaAcctSendStopOnAaaReject_Type(TruthValue):
    """Custom type usdAaaAcctSendStopOnAaaReject based on TruthValue"""


_UsdAaaAcctSendStopOnAaaReject_Object = MibScalar
usdAaaAcctSendStopOnAaaReject = _UsdAaaAcctSendStopOnAaaReject_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 5),
    _UsdAaaAcctSendStopOnAaaReject_Type()
)
usdAaaAcctSendStopOnAaaReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAcctSendStopOnAaaReject.setStatus("current")
_UsdAaaAddress_ObjectIdentity = ObjectIdentity
usdAaaAddress = _UsdAaaAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4)
)
_UsdAaaAddrGeneral_ObjectIdentity = ObjectIdentity
usdAaaAddrGeneral = _UsdAaaAddrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 1)
)


class _UsdAaaAddrPoolDefault_Type(Integer32):
    """Custom type usdAaaAddrPoolDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("local", 1),
          ("none", 0))
    )


_UsdAaaAddrPoolDefault_Type.__name__ = "Integer32"
_UsdAaaAddrPoolDefault_Object = MibScalar
usdAaaAddrPoolDefault = _UsdAaaAddrPoolDefault_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 1, 1),
    _UsdAaaAddrPoolDefault_Type()
)
usdAaaAddrPoolDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAddrPoolDefault.setStatus("current")
_UsdAaaDupAddrCheck_Type = TruthValue
_UsdAaaDupAddrCheck_Object = MibScalar
usdAaaDupAddrCheck = _UsdAaaDupAddrCheck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 1, 2),
    _UsdAaaDupAddrCheck_Type()
)
usdAaaDupAddrCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaDupAddrCheck.setStatus("current")
_UsdAaaAddrNameServer_ObjectIdentity = ObjectIdentity
usdAaaAddrNameServer = _UsdAaaAddrNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2)
)
_UsdAaaAddrDns_ObjectIdentity = ObjectIdentity
usdAaaAddrDns = _UsdAaaAddrDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 1)
)
_UsdAaaAddrDnsPrimary_Type = IpAddress
_UsdAaaAddrDnsPrimary_Object = MibScalar
usdAaaAddrDnsPrimary = _UsdAaaAddrDnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 1, 1),
    _UsdAaaAddrDnsPrimary_Type()
)
usdAaaAddrDnsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAddrDnsPrimary.setStatus("current")
_UsdAaaAddrDnsSecondary_Type = IpAddress
_UsdAaaAddrDnsSecondary_Object = MibScalar
usdAaaAddrDnsSecondary = _UsdAaaAddrDnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 1, 2),
    _UsdAaaAddrDnsSecondary_Type()
)
usdAaaAddrDnsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAddrDnsSecondary.setStatus("current")
_UsdAaaAddrWins_ObjectIdentity = ObjectIdentity
usdAaaAddrWins = _UsdAaaAddrWins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 2)
)
_UsdAaaAddrWinsPrimary_Type = IpAddress
_UsdAaaAddrWinsPrimary_Object = MibScalar
usdAaaAddrWinsPrimary = _UsdAaaAddrWinsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 2, 1),
    _UsdAaaAddrWinsPrimary_Type()
)
usdAaaAddrWinsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAddrWinsPrimary.setStatus("current")
_UsdAaaAddrWinsSecondary_Type = IpAddress
_UsdAaaAddrWinsSecondary_Object = MibScalar
usdAaaAddrWinsSecondary = _UsdAaaAddrWinsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 2, 2),
    _UsdAaaAddrWinsSecondary_Type()
)
usdAaaAddrWinsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaAddrWinsSecondary.setStatus("current")
_UsdAaaStatistics_ObjectIdentity = ObjectIdentity
usdAaaStatistics = _UsdAaaStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5)
)
_UsdAaaIncomingInitiateRequests_Type = Counter32
_UsdAaaIncomingInitiateRequests_Object = MibScalar
usdAaaIncomingInitiateRequests = _UsdAaaIncomingInitiateRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 1),
    _UsdAaaIncomingInitiateRequests_Type()
)
usdAaaIncomingInitiateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaIncomingInitiateRequests.setStatus("current")
_UsdAaaIncomingTerminateRequests_Type = Counter32
_UsdAaaIncomingTerminateRequests_Object = MibScalar
usdAaaIncomingTerminateRequests = _UsdAaaIncomingTerminateRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 2),
    _UsdAaaIncomingTerminateRequests_Type()
)
usdAaaIncomingTerminateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaIncomingTerminateRequests.setStatus("current")
_UsdAaaOutgoingTunnelGrantResponses_Type = Counter32
_UsdAaaOutgoingTunnelGrantResponses_Object = MibScalar
usdAaaOutgoingTunnelGrantResponses = _UsdAaaOutgoingTunnelGrantResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 3),
    _UsdAaaOutgoingTunnelGrantResponses_Type()
)
usdAaaOutgoingTunnelGrantResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaOutgoingTunnelGrantResponses.setStatus("current")
_UsdAaaOutgoingGrantResponses_Type = Counter32
_UsdAaaOutgoingGrantResponses_Object = MibScalar
usdAaaOutgoingGrantResponses = _UsdAaaOutgoingGrantResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 4),
    _UsdAaaOutgoingGrantResponses_Type()
)
usdAaaOutgoingGrantResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaOutgoingGrantResponses.setStatus("current")
_UsdAaaOutgoingDenyResponses_Type = Counter32
_UsdAaaOutgoingDenyResponses_Object = MibScalar
usdAaaOutgoingDenyResponses = _UsdAaaOutgoingDenyResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 5),
    _UsdAaaOutgoingDenyResponses_Type()
)
usdAaaOutgoingDenyResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaOutgoingDenyResponses.setStatus("current")
_UsdAaaOutgoingErrorResponses_Type = Counter32
_UsdAaaOutgoingErrorResponses_Object = MibScalar
usdAaaOutgoingErrorResponses = _UsdAaaOutgoingErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 6),
    _UsdAaaOutgoingErrorResponses_Type()
)
usdAaaOutgoingErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaOutgoingErrorResponses.setStatus("current")
_UsdAaaOutgoingAuthRequests_Type = Counter32
_UsdAaaOutgoingAuthRequests_Object = MibScalar
usdAaaOutgoingAuthRequests = _UsdAaaOutgoingAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 7),
    _UsdAaaOutgoingAuthRequests_Type()
)
usdAaaOutgoingAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaOutgoingAuthRequests.setStatus("current")
_UsdAaaIncomingAuthResponses_Type = Counter32
_UsdAaaIncomingAuthResponses_Object = MibScalar
usdAaaIncomingAuthResponses = _UsdAaaIncomingAuthResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 8),
    _UsdAaaIncomingAuthResponses_Type()
)
usdAaaIncomingAuthResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaIncomingAuthResponses.setStatus("current")
_UsdAaaOutgoingReAuthRequests_Type = Counter32
_UsdAaaOutgoingReAuthRequests_Object = MibScalar
usdAaaOutgoingReAuthRequests = _UsdAaaOutgoingReAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 9),
    _UsdAaaOutgoingReAuthRequests_Type()
)
usdAaaOutgoingReAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaOutgoingReAuthRequests.setStatus("current")
_UsdAaaIncomingReAuthResponses_Type = Counter32
_UsdAaaIncomingReAuthResponses_Object = MibScalar
usdAaaIncomingReAuthResponses = _UsdAaaIncomingReAuthResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 10),
    _UsdAaaIncomingReAuthResponses_Type()
)
usdAaaIncomingReAuthResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaIncomingReAuthResponses.setStatus("current")
_UsdAaaOutgoingAcctRequests_Type = Counter32
_UsdAaaOutgoingAcctRequests_Object = MibScalar
usdAaaOutgoingAcctRequests = _UsdAaaOutgoingAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 11),
    _UsdAaaOutgoingAcctRequests_Type()
)
usdAaaOutgoingAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaOutgoingAcctRequests.setStatus("current")
_UsdAaaIncomingAcctResponses_Type = Counter32
_UsdAaaIncomingAcctResponses_Object = MibScalar
usdAaaIncomingAcctResponses = _UsdAaaIncomingAcctResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 12),
    _UsdAaaIncomingAcctResponses_Type()
)
usdAaaIncomingAcctResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaIncomingAcctResponses.setStatus("current")
_UsdAaaOutgoingDupAcctRequests_Type = Counter32
_UsdAaaOutgoingDupAcctRequests_Object = MibScalar
usdAaaOutgoingDupAcctRequests = _UsdAaaOutgoingDupAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 13),
    _UsdAaaOutgoingDupAcctRequests_Type()
)
usdAaaOutgoingDupAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaOutgoingDupAcctRequests.setStatus("current")
_UsdAaaIncomingDupAcctResponses_Type = Counter32
_UsdAaaIncomingDupAcctResponses_Object = MibScalar
usdAaaIncomingDupAcctResponses = _UsdAaaIncomingDupAcctResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 14),
    _UsdAaaIncomingDupAcctResponses_Type()
)
usdAaaIncomingDupAcctResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaIncomingDupAcctResponses.setStatus("current")
_UsdAaaOutgoingAddrRequests_Type = Counter32
_UsdAaaOutgoingAddrRequests_Object = MibScalar
usdAaaOutgoingAddrRequests = _UsdAaaOutgoingAddrRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 15),
    _UsdAaaOutgoingAddrRequests_Type()
)
usdAaaOutgoingAddrRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaOutgoingAddrRequests.setStatus("current")
_UsdAaaIncomingAddrResponses_Type = Counter32
_UsdAaaIncomingAddrResponses_Object = MibScalar
usdAaaIncomingAddrResponses = _UsdAaaIncomingAddrResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 16),
    _UsdAaaIncomingAddrResponses_Type()
)
usdAaaIncomingAddrResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaIncomingAddrResponses.setStatus("current")
_UsdAaaTimeout_ObjectIdentity = ObjectIdentity
usdAaaTimeout = _UsdAaaTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 6)
)
_UsdAaaTimeoutGeneral_ObjectIdentity = ObjectIdentity
usdAaaTimeoutGeneral = _UsdAaaTimeoutGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 6, 1)
)


class _UsdAaaIdleTimeout_Type(Integer32):
    """Custom type usdAaaIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 7200),
    )


_UsdAaaIdleTimeout_Type.__name__ = "Integer32"
_UsdAaaIdleTimeout_Object = MibScalar
usdAaaIdleTimeout = _UsdAaaIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 6, 1, 1),
    _UsdAaaIdleTimeout_Type()
)
usdAaaIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdAaaIdleTimeout.setUnits("seconds")


class _UsdAaaSessionTimeout_Type(Integer32):
    """Custom type usdAaaSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1814400),
    )


_UsdAaaSessionTimeout_Type.__name__ = "Integer32"
_UsdAaaSessionTimeout_Object = MibScalar
usdAaaSessionTimeout = _UsdAaaSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 6, 1, 2),
    _UsdAaaSessionTimeout_Type()
)
usdAaaSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdAaaSessionTimeout.setUnits("seconds")
_UsdAaaTunnel_ObjectIdentity = ObjectIdentity
usdAaaTunnel = _UsdAaaTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7)
)
_UsdAaaTunnelGeneral_ObjectIdentity = ObjectIdentity
usdAaaTunnelGeneral = _UsdAaaTunnelGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1)
)


class _UsdAaaTunnelClientName_Type(DisplayString):
    """Custom type usdAaaTunnelClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UsdAaaTunnelClientName_Type.__name__ = "DisplayString"
_UsdAaaTunnelClientName_Object = MibScalar
usdAaaTunnelClientName = _UsdAaaTunnelClientName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 1),
    _UsdAaaTunnelClientName_Type()
)
usdAaaTunnelClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaTunnelClientName.setStatus("current")


class _UsdAaaTunnelPassword_Type(DisplayString):
    """Custom type usdAaaTunnelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdAaaTunnelPassword_Type.__name__ = "DisplayString"
_UsdAaaTunnelPassword_Object = MibScalar
usdAaaTunnelPassword = _UsdAaaTunnelPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 2),
    _UsdAaaTunnelPassword_Type()
)
usdAaaTunnelPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaTunnelPassword.setStatus("current")


class _UsdAaaTunnelNasPortMethod_Type(Integer32):
    """Custom type usdAaaTunnelNasPortMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ciscoAvp", 1),
          ("none", 0))
    )


_UsdAaaTunnelNasPortMethod_Type.__name__ = "Integer32"
_UsdAaaTunnelNasPortMethod_Object = MibScalar
usdAaaTunnelNasPortMethod = _UsdAaaTunnelNasPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 3),
    _UsdAaaTunnelNasPortMethod_Type()
)
usdAaaTunnelNasPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaTunnelNasPortMethod.setStatus("current")
_UsdAaaTunnelIgnoreNasPort_Type = TruthValue
_UsdAaaTunnelIgnoreNasPort_Object = MibScalar
usdAaaTunnelIgnoreNasPort = _UsdAaaTunnelIgnoreNasPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 4),
    _UsdAaaTunnelIgnoreNasPort_Type()
)
usdAaaTunnelIgnoreNasPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaTunnelIgnoreNasPort.setStatus("current")
_UsdAaaTunnelIgnoreNasPortType_Type = TruthValue
_UsdAaaTunnelIgnoreNasPortType_Object = MibScalar
usdAaaTunnelIgnoreNasPortType = _UsdAaaTunnelIgnoreNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 5),
    _UsdAaaTunnelIgnoreNasPortType_Type()
)
usdAaaTunnelIgnoreNasPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaTunnelIgnoreNasPortType.setStatus("current")


class _UsdAaaTunnelAssignmentIdFormat_Type(Integer32):
    """Custom type usdAaaTunnelAssignmentIdFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("assignmentId", 0),
          ("clientServerId", 1))
    )


_UsdAaaTunnelAssignmentIdFormat_Type.__name__ = "Integer32"
_UsdAaaTunnelAssignmentIdFormat_Object = MibScalar
usdAaaTunnelAssignmentIdFormat = _UsdAaaTunnelAssignmentIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 6),
    _UsdAaaTunnelAssignmentIdFormat_Type()
)
usdAaaTunnelAssignmentIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaTunnelAssignmentIdFormat.setStatus("current")
_UsdAaaSubscribers_ObjectIdentity = ObjectIdentity
usdAaaSubscribers = _UsdAaaSubscribers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8)
)
_UsdAaaSubscriberMaxCount_Type = Integer32
_UsdAaaSubscriberMaxCount_Object = MibScalar
usdAaaSubscriberMaxCount = _UsdAaaSubscriberMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 1),
    _UsdAaaSubscriberMaxCount_Type()
)
usdAaaSubscriberMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberMaxCount.setStatus("current")
_UsdAaaSubscriberPeakCount_Type = Gauge32
_UsdAaaSubscriberPeakCount_Object = MibScalar
usdAaaSubscriberPeakCount = _UsdAaaSubscriberPeakCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 2),
    _UsdAaaSubscriberPeakCount_Type()
)
usdAaaSubscriberPeakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberPeakCount.setStatus("current")
_UsdAaaSubscriberCount_Type = Gauge32
_UsdAaaSubscriberCount_Object = MibScalar
usdAaaSubscriberCount = _UsdAaaSubscriberCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 3),
    _UsdAaaSubscriberCount_Type()
)
usdAaaSubscriberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberCount.setStatus("current")
_UsdAaaSubscriberTable_Object = MibTable
usdAaaSubscriberTable = _UsdAaaSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4)
)
if mibBuilder.loadTexts:
    usdAaaSubscriberTable.setStatus("current")
_UsdAaaSubscriberEntry_Object = MibTableRow
usdAaaSubscriberEntry = _UsdAaaSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1)
)
usdAaaSubscriberEntry.setIndexNames(
    (0, "Unisphere-Data-AAA-MIB", "usdAaaSubscriberHandle"),
)
if mibBuilder.loadTexts:
    usdAaaSubscriberEntry.setStatus("current")
_UsdAaaSubscriberHandle_Type = Unsigned32
_UsdAaaSubscriberHandle_Object = MibTableColumn
usdAaaSubscriberHandle = _UsdAaaSubscriberHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 1),
    _UsdAaaSubscriberHandle_Type()
)
usdAaaSubscriberHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAaaSubscriberHandle.setStatus("current")
_UsdAaaSubscriberUserName_Type = DisplayString
_UsdAaaSubscriberUserName_Object = MibTableColumn
usdAaaSubscriberUserName = _UsdAaaSubscriberUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 2),
    _UsdAaaSubscriberUserName_Type()
)
usdAaaSubscriberUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberUserName.setStatus("current")
_UsdAaaSubscriberRouterName_Type = UsdName
_UsdAaaSubscriberRouterName_Object = MibTableColumn
usdAaaSubscriberRouterName = _UsdAaaSubscriberRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 3),
    _UsdAaaSubscriberRouterName_Type()
)
usdAaaSubscriberRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterName.setStatus("current")
_UsdAaaSubscriberRouterIndex_Type = Unsigned32
_UsdAaaSubscriberRouterIndex_Object = MibTableColumn
usdAaaSubscriberRouterIndex = _UsdAaaSubscriberRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 4),
    _UsdAaaSubscriberRouterIndex_Type()
)
usdAaaSubscriberRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterIndex.setStatus("current")
_UsdAaaSubscriberLoginTime_Type = DisplayString
_UsdAaaSubscriberLoginTime_Object = MibTableColumn
usdAaaSubscriberLoginTime = _UsdAaaSubscriberLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 5),
    _UsdAaaSubscriberLoginTime_Type()
)
usdAaaSubscriberLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberLoginTime.setStatus("current")
_UsdAaaSubscriberIpAddress_Type = IpAddress
_UsdAaaSubscriberIpAddress_Object = MibTableColumn
usdAaaSubscriberIpAddress = _UsdAaaSubscriberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 6),
    _UsdAaaSubscriberIpAddress_Type()
)
usdAaaSubscriberIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberIpAddress.setStatus("current")
_UsdAaaSubscriberIpAddressMask_Type = IpAddress
_UsdAaaSubscriberIpAddressMask_Object = MibTableColumn
usdAaaSubscriberIpAddressMask = _UsdAaaSubscriberIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 7),
    _UsdAaaSubscriberIpAddressMask_Type()
)
usdAaaSubscriberIpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberIpAddressMask.setStatus("current")
_UsdAaaSubscriberAddrAssignType_Type = UsdAddressAssignType
_UsdAaaSubscriberAddrAssignType_Object = MibTableColumn
usdAaaSubscriberAddrAssignType = _UsdAaaSubscriberAddrAssignType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 8),
    _UsdAaaSubscriberAddrAssignType_Type()
)
usdAaaSubscriberAddrAssignType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberAddrAssignType.setStatus("current")
_UsdAaaSubscriberInterfaceId_Type = DisplayString
_UsdAaaSubscriberInterfaceId_Object = MibTableColumn
usdAaaSubscriberInterfaceId = _UsdAaaSubscriberInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 9),
    _UsdAaaSubscriberInterfaceId_Type()
)
usdAaaSubscriberInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberInterfaceId.setStatus("current")
_UsdAaaSubscriberState_Type = UsdSubscriberState
_UsdAaaSubscriberState_Object = MibTableColumn
usdAaaSubscriberState = _UsdAaaSubscriberState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 10),
    _UsdAaaSubscriberState_Type()
)
usdAaaSubscriberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberState.setStatus("current")
_UsdAaaSubscriberClientType_Type = UsdSubscriberClientType
_UsdAaaSubscriberClientType_Object = MibTableColumn
usdAaaSubscriberClientType = _UsdAaaSubscriberClientType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 11),
    _UsdAaaSubscriberClientType_Type()
)
usdAaaSubscriberClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberClientType.setStatus("current")
_UsdAaaSubscriberIngressPolicyName_Type = DisplayString
_UsdAaaSubscriberIngressPolicyName_Object = MibTableColumn
usdAaaSubscriberIngressPolicyName = _UsdAaaSubscriberIngressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 12),
    _UsdAaaSubscriberIngressPolicyName_Type()
)
usdAaaSubscriberIngressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberIngressPolicyName.setStatus("current")
_UsdAaaSubscriberEgressPolicyName_Type = DisplayString
_UsdAaaSubscriberEgressPolicyName_Object = MibTableColumn
usdAaaSubscriberEgressPolicyName = _UsdAaaSubscriberEgressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 13),
    _UsdAaaSubscriberEgressPolicyName_Type()
)
usdAaaSubscriberEgressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberEgressPolicyName.setStatus("current")
_UsdAaaSubscriberQosProfileName_Type = DisplayString
_UsdAaaSubscriberQosProfileName_Object = MibTableColumn
usdAaaSubscriberQosProfileName = _UsdAaaSubscriberQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 14),
    _UsdAaaSubscriberQosProfileName_Type()
)
usdAaaSubscriberQosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberQosProfileName.setStatus("current")
_UsdAaaSubscriberRowStatus_Type = RowStatus
_UsdAaaSubscriberRowStatus_Object = MibTableColumn
usdAaaSubscriberRowStatus = _UsdAaaSubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 15),
    _UsdAaaSubscriberRowStatus_Type()
)
usdAaaSubscriberRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAaaSubscriberRowStatus.setStatus("current")
_UsdAaaSubscriberRouterSummaryTable_Object = MibTable
usdAaaSubscriberRouterSummaryTable = _UsdAaaSubscriberRouterSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 5)
)
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterSummaryTable.setStatus("current")
_UsdAaaSubscriberRouterSummaryEntry_Object = MibTableRow
usdAaaSubscriberRouterSummaryEntry = _UsdAaaSubscriberRouterSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 5, 1)
)
usdAaaSubscriberRouterSummaryEntry.setIndexNames(
    (0, "Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterSummaryRouterIndex"),
)
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterSummaryEntry.setStatus("current")
_UsdAaaSubscriberRouterSummaryRouterIndex_Type = Unsigned32
_UsdAaaSubscriberRouterSummaryRouterIndex_Object = MibTableColumn
usdAaaSubscriberRouterSummaryRouterIndex = _UsdAaaSubscriberRouterSummaryRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 5, 1, 1),
    _UsdAaaSubscriberRouterSummaryRouterIndex_Type()
)
usdAaaSubscriberRouterSummaryRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterSummaryRouterIndex.setStatus("current")
_UsdAaaSubscriberRouterSummaryCount_Type = Gauge32
_UsdAaaSubscriberRouterSummaryCount_Object = MibTableColumn
usdAaaSubscriberRouterSummaryCount = _UsdAaaSubscriberRouterSummaryCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 5, 1, 2),
    _UsdAaaSubscriberRouterSummaryCount_Type()
)
usdAaaSubscriberRouterSummaryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterSummaryCount.setStatus("current")
_UsdAaaSubscriberRouterTable_Object = MibTable
usdAaaSubscriberRouterTable = _UsdAaaSubscriberRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6)
)
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterTable.setStatus("current")
_UsdAaaSubscriberRouterEntry_Object = MibTableRow
usdAaaSubscriberRouterEntry = _UsdAaaSubscriberRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6, 1)
)
usdAaaSubscriberRouterEntry.setIndexNames(
    (0, "Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterRouterIndex"),
    (0, "Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterHandle"),
)
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterEntry.setStatus("current")
_UsdAaaSubscriberRouterRouterIndex_Type = Unsigned32
_UsdAaaSubscriberRouterRouterIndex_Object = MibTableColumn
usdAaaSubscriberRouterRouterIndex = _UsdAaaSubscriberRouterRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6, 1, 1),
    _UsdAaaSubscriberRouterRouterIndex_Type()
)
usdAaaSubscriberRouterRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterRouterIndex.setStatus("current")
_UsdAaaSubscriberRouterHandle_Type = Unsigned32
_UsdAaaSubscriberRouterHandle_Object = MibTableColumn
usdAaaSubscriberRouterHandle = _UsdAaaSubscriberRouterHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6, 1, 2),
    _UsdAaaSubscriberRouterHandle_Type()
)
usdAaaSubscriberRouterHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterHandle.setStatus("current")
_UsdAaaSubscriberRouterRowStatus_Type = RowStatus
_UsdAaaSubscriberRouterRowStatus_Object = MibTableColumn
usdAaaSubscriberRouterRowStatus = _UsdAaaSubscriberRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6, 1, 3),
    _UsdAaaSubscriberRouterRowStatus_Type()
)
usdAaaSubscriberRouterRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberRouterRowStatus.setStatus("current")
_UsdAaaSubscriberLocationType_Type = UsdSubscriberLocationType
_UsdAaaSubscriberLocationType_Object = MibScalar
usdAaaSubscriberLocationType = _UsdAaaSubscriberLocationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 7),
    _UsdAaaSubscriberLocationType_Type()
)
usdAaaSubscriberLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationType.setStatus("current")
_UsdAaaSubscriberLocationSummaryTable_Object = MibTable
usdAaaSubscriberLocationSummaryTable = _UsdAaaSubscriberLocationSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 8)
)
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationSummaryTable.setStatus("current")
_UsdAaaSubscriberLocationSummaryEntry_Object = MibTableRow
usdAaaSubscriberLocationSummaryEntry = _UsdAaaSubscriberLocationSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 8, 1)
)
usdAaaSubscriberLocationSummaryEntry.setIndexNames(
    (0, "Unisphere-Data-AAA-MIB", "usdAaaSubscriberLocationSummaryLocationIndex"),
)
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationSummaryEntry.setStatus("current")
_UsdAaaSubscriberLocationSummaryLocationIndex_Type = UsdSubscriberLocationValue
_UsdAaaSubscriberLocationSummaryLocationIndex_Object = MibTableColumn
usdAaaSubscriberLocationSummaryLocationIndex = _UsdAaaSubscriberLocationSummaryLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 8, 1, 1),
    _UsdAaaSubscriberLocationSummaryLocationIndex_Type()
)
usdAaaSubscriberLocationSummaryLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationSummaryLocationIndex.setStatus("current")
_UsdAaaSubscriberLocationSummaryCount_Type = Gauge32
_UsdAaaSubscriberLocationSummaryCount_Object = MibTableColumn
usdAaaSubscriberLocationSummaryCount = _UsdAaaSubscriberLocationSummaryCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 8, 1, 2),
    _UsdAaaSubscriberLocationSummaryCount_Type()
)
usdAaaSubscriberLocationSummaryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationSummaryCount.setStatus("current")
_UsdAaaSubscriberLocationTable_Object = MibTable
usdAaaSubscriberLocationTable = _UsdAaaSubscriberLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9)
)
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationTable.setStatus("current")
_UsdAaaSubscriberLocationEntry_Object = MibTableRow
usdAaaSubscriberLocationEntry = _UsdAaaSubscriberLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9, 1)
)
usdAaaSubscriberLocationEntry.setIndexNames(
    (0, "Unisphere-Data-AAA-MIB", "usdAaaSubscriberLocationLocationIndex"),
    (0, "Unisphere-Data-AAA-MIB", "usdAaaSubscriberLocationHandle"),
)
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationEntry.setStatus("current")
_UsdAaaSubscriberLocationLocationIndex_Type = UsdSubscriberLocationValue
_UsdAaaSubscriberLocationLocationIndex_Object = MibTableColumn
usdAaaSubscriberLocationLocationIndex = _UsdAaaSubscriberLocationLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9, 1, 1),
    _UsdAaaSubscriberLocationLocationIndex_Type()
)
usdAaaSubscriberLocationLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationLocationIndex.setStatus("current")
_UsdAaaSubscriberLocationHandle_Type = Unsigned32
_UsdAaaSubscriberLocationHandle_Object = MibTableColumn
usdAaaSubscriberLocationHandle = _UsdAaaSubscriberLocationHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9, 1, 2),
    _UsdAaaSubscriberLocationHandle_Type()
)
usdAaaSubscriberLocationHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationHandle.setStatus("current")
_UsdAaaSubscriberLocationRowStatus_Type = RowStatus
_UsdAaaSubscriberLocationRowStatus_Object = MibTableColumn
usdAaaSubscriberLocationRowStatus = _UsdAaaSubscriberLocationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9, 1, 3),
    _UsdAaaSubscriberLocationRowStatus_Type()
)
usdAaaSubscriberLocationRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberLocationRowStatus.setStatus("current")
_UsdAaaSubscriberPseudoPeakCount_Type = Gauge32
_UsdAaaSubscriberPseudoPeakCount_Object = MibScalar
usdAaaSubscriberPseudoPeakCount = _UsdAaaSubscriberPseudoPeakCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 10),
    _UsdAaaSubscriberPseudoPeakCount_Type()
)
usdAaaSubscriberPseudoPeakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberPseudoPeakCount.setStatus("current")
_UsdAaaSubscriberPseudoCount_Type = Gauge32
_UsdAaaSubscriberPseudoCount_Object = MibScalar
usdAaaSubscriberPseudoCount = _UsdAaaSubscriberPseudoCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 11),
    _UsdAaaSubscriberPseudoCount_Type()
)
usdAaaSubscriberPseudoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaSubscriberPseudoCount.setStatus("current")
_UsdAaaCapabilities_ObjectIdentity = ObjectIdentity
usdAaaCapabilities = _UsdAaaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9)
)
_UsdAaaAccountingCapability_Type = TruthValue
_UsdAaaAccountingCapability_Object = MibScalar
usdAaaAccountingCapability = _UsdAaaAccountingCapability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9, 1),
    _UsdAaaAccountingCapability_Type()
)
usdAaaAccountingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaAccountingCapability.setStatus("current")
_UsdAaaAddressAssignmentCapability_Type = TruthValue
_UsdAaaAddressAssignmentCapability_Object = MibScalar
usdAaaAddressAssignmentCapability = _UsdAaaAddressAssignmentCapability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9, 2),
    _UsdAaaAddressAssignmentCapability_Type()
)
usdAaaAddressAssignmentCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaAddressAssignmentCapability.setStatus("current")
_UsdAaaBrasCapability_Type = TruthValue
_UsdAaaBrasCapability_Object = MibScalar
usdAaaBrasCapability = _UsdAaaBrasCapability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9, 3),
    _UsdAaaBrasCapability_Type()
)
usdAaaBrasCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaBrasCapability.setStatus("current")
_UsdAaaTunnelingCapability_Type = TruthValue
_UsdAaaTunnelingCapability_Object = MibScalar
usdAaaTunnelingCapability = _UsdAaaTunnelingCapability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9, 4),
    _UsdAaaTunnelingCapability_Type()
)
usdAaaTunnelingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdAaaTunnelingCapability.setStatus("current")
_UsdAaaMIBConformance_ObjectIdentity = ObjectIdentity
usdAaaMIBConformance = _UsdAaaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4)
)
_UsdAaaMIBCompliances_ObjectIdentity = ObjectIdentity
usdAaaMIBCompliances = _UsdAaaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1)
)
_UsdAaaMIBGroups_ObjectIdentity = ObjectIdentity
usdAaaMIBGroups = _UsdAaaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2)
)

# Managed Objects groups

usdAaaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 1)
)
usdAaaGroup.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicense"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicensedUsers"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainLoopback"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctInterval"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctDupServerRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrPoolDefault"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrDnsPrimary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrDnsSecondary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrWinsPrimary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrWinsSecondary"))
)
if mibBuilder.loadTexts:
    usdAaaGroup.setStatus("obsolete")

usdAaaGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 2)
)
usdAaaGroup2.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicense"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicensedUsers"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainLoopback"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainIpHint"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmServiceLevel"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmPcr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmScr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmMbs"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverrideUserName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverridePassword"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctInterval"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctDupServerRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrPoolDefault"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrDnsPrimary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrDnsSecondary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrWinsPrimary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrWinsSecondary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingInitiateRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingTerminateRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingTunnelGrantResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingGrantResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingDenyResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingErrorResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingAuthRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingAuthResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingReAuthRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingReAuthResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingAcctRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingAcctResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingDupAcctRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingDupAcctResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingAddrRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingAddrResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelTag"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelPreference"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelMedium"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelAddress"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelPassword"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelId"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelHostName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    usdAaaGroup2.setStatus("obsolete")

usdAaaBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 3)
)
usdAaaBasicGroup.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaIncomingInitiateRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingTerminateRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingGrantResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingDenyResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingErrorResponses"))
)
if mibBuilder.loadTexts:
    usdAaaBasicGroup.setStatus("current")

usdAaaBrasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 4)
)
usdAaaBrasGroup.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicense"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicensedUsers"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIdleTimeout"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSessionTimeout"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainLoopback"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainIpHint"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmServiceLevel"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmPcr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmScr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmMbs"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverrideUserName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverridePassword"))
)
if mibBuilder.loadTexts:
    usdAaaBrasGroup.setStatus("obsolete")

usdAaaTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 5)
)
usdAaaTunnelGroup.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelTag"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelPreference"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelMedium"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelAddress"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelPassword"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelId"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelHostName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelServerName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelClientAddress"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainTunnelRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingTunnelGrantResponses"))
)
if mibBuilder.loadTexts:
    usdAaaTunnelGroup.setStatus("current")

usdAaaAuthenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 6)
)
usdAaaAuthenticationGroup.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAuthMethods"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingAuthRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingAuthResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingReAuthRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingReAuthResponses"))
)
if mibBuilder.loadTexts:
    usdAaaAuthenticationGroup.setStatus("current")

usdAaaAccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 7)
)
usdAaaAccountingGroup.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAcctInterval"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctDupServerRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctMethods"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingAcctRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingAcctResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingDupAcctRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingDupAcctResponses"))
)
if mibBuilder.loadTexts:
    usdAaaAccountingGroup.setStatus("obsolete")

usdAaaAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 8)
)
usdAaaAddressGroup.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAddrPoolDefault"),
        ("Unisphere-Data-AAA-MIB", "usdAaaDupAddrCheck"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrDnsPrimary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrDnsSecondary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrWinsPrimary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddrWinsSecondary"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingAddrRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingAddrResponses"))
)
if mibBuilder.loadTexts:
    usdAaaAddressGroup.setStatus("current")

usdAaaBrasGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 9)
)
usdAaaBrasGroup2.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicense"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicensedUsers"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIdleTimeout"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSessionTimeout"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainLoopback"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainIpHint"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmServiceLevel"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmPcr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmScr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmMbs"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverrideUserName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverridePassword"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainStripDomain"))
)
if mibBuilder.loadTexts:
    usdAaaBrasGroup2.setStatus("obsolete")

usdAaaBrasGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 10)
)
usdAaaBrasGroup3.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicense"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicensedUsers"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainDelimiters"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignRealmDelimiters"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainParseOrder"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIdleTimeout"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSessionTimeout"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelClientName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelPassword"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelNasPortMethod"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainLoopback"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainIpHint"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmServiceLevel"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmPcr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmScr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmMbs"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverrideUserName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverridePassword"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainStripDomain"))
)
if mibBuilder.loadTexts:
    usdAaaBrasGroup3.setStatus("obsolete")

usdAaaSubscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 11)
)
usdAaaSubscriberGroup.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaSubscriberMaxCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberPeakCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberUserName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterIndex"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberLoginTime"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberIpAddress"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberIpAddressMask"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberAddrAssignType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberInterfaceId"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberState"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberClientType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberIngressPolicyName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberEgressPolicyName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberQosProfileName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterSummaryCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterRowStatus"))
)
if mibBuilder.loadTexts:
    usdAaaSubscriberGroup.setStatus("obsolete")

usdAaaCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 12)
)
usdAaaCapabilitiesGroup.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAccountingCapability"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAddressAssignmentCapability"),
        ("Unisphere-Data-AAA-MIB", "usdAaaBrasCapability"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelingCapability"))
)
if mibBuilder.loadTexts:
    usdAaaCapabilitiesGroup.setStatus("current")

usdAaaSubscriberGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 13)
)
usdAaaSubscriberGroup2.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaSubscriberMaxCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberPeakCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberUserName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterIndex"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberLoginTime"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberIpAddress"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberIpAddressMask"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberAddrAssignType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberInterfaceId"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberState"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberClientType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberIngressPolicyName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberEgressPolicyName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberQosProfileName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterSummaryCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberLocationType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberLocationSummaryCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberLocationRowStatus"))
)
if mibBuilder.loadTexts:
    usdAaaSubscriberGroup2.setStatus("obsolete")

usdAaaAccountingGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 14)
)
usdAaaAccountingGroup2.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAcctInterval"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctDupServerRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctMethods"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctSendStopOnAaaDeny"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAcctSendStopOnAaaReject"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingAcctRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingAcctResponses"),
        ("Unisphere-Data-AAA-MIB", "usdAaaOutgoingDupAcctRequests"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIncomingDupAcctResponses"))
)
if mibBuilder.loadTexts:
    usdAaaAccountingGroup2.setStatus("current")

usdAaaBrasGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 15)
)
usdAaaBrasGroup4.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicense"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignBrasLicensedUsers"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainDelimiters"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignRealmDelimiters"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainParseOrder"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignSubscriberLimit"),
        ("Unisphere-Data-AAA-MIB", "usdAaaIdleTimeout"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSessionTimeout"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelClientName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelPassword"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelNasPortMethod"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelIgnoreNasPort"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelIgnoreNasPortType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaTunnelAssignmentIdFormat"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainLoopback"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainIpHint"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmServiceLevel"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmPcr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmScr"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainAtmMbs"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverrideUserName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainOverridePassword"),
        ("Unisphere-Data-AAA-MIB", "usdAaaAssignDomainStripDomain"))
)
if mibBuilder.loadTexts:
    usdAaaBrasGroup4.setStatus("current")

usdAaaSubscriberGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 16)
)
usdAaaSubscriberGroup3.setObjects(
      *(("Unisphere-Data-AAA-MIB", "usdAaaSubscriberMaxCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberPeakCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberUserName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterIndex"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberLoginTime"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberIpAddress"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberIpAddressMask"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberAddrAssignType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberInterfaceId"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberState"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberClientType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberIngressPolicyName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberEgressPolicyName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberQosProfileName"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterSummaryCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberRouterRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberLocationType"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberLocationSummaryCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberLocationRowStatus"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberPseudoPeakCount"),
        ("Unisphere-Data-AAA-MIB", "usdAaaSubscriberPseudoCount"))
)
if mibBuilder.loadTexts:
    usdAaaSubscriberGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdAaaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdAaaCompliance.setStatus(
        "obsolete"
    )

usdAaaCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdAaaCompliance2.setStatus(
        "obsolete"
    )

usdAaaCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdAaaCompliance3.setStatus(
        "obsolete"
    )

usdAaaCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 4)
)
if mibBuilder.loadTexts:
    usdAaaCompliance4.setStatus(
        "obsolete"
    )

usdAaaCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 5)
)
if mibBuilder.loadTexts:
    usdAaaCompliance5.setStatus(
        "obsolete"
    )

usdAaaCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 6)
)
if mibBuilder.loadTexts:
    usdAaaCompliance6.setStatus(
        "obsolete"
    )

usdAaaCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 7)
)
if mibBuilder.loadTexts:
    usdAaaCompliance7.setStatus(
        "obsolete"
    )

usdAaaCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 8)
)
if mibBuilder.loadTexts:
    usdAaaCompliance8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-AAA-MIB",
    **{"UsdAaaDomainName": UsdAaaDomainName,
       "UsdAaaAuthenticationMethods": UsdAaaAuthenticationMethods,
       "UsdAaaAccountingMethods": UsdAaaAccountingMethods,
       "UsdAddressAssignType": UsdAddressAssignType,
       "UsdSubscriberState": UsdSubscriberState,
       "UsdSubscriberClientType": UsdSubscriberClientType,
       "UsdSubscriberLocationType": UsdSubscriberLocationType,
       "UsdSubscriberLocationValue": UsdSubscriberLocationValue,
       "usdAaaMIB": usdAaaMIB,
       "usdAaaObjects": usdAaaObjects,
       "usdAaaAssignment": usdAaaAssignment,
       "usdAaaAssignGeneral": usdAaaAssignGeneral,
       "usdAaaAssignBrasLicense": usdAaaAssignBrasLicense,
       "usdAaaAssignBrasLicensedUsers": usdAaaAssignBrasLicensedUsers,
       "usdAaaAssignDomainDelimiters": usdAaaAssignDomainDelimiters,
       "usdAaaAssignRealmDelimiters": usdAaaAssignRealmDelimiters,
       "usdAaaAssignDomainParseOrder": usdAaaAssignDomainParseOrder,
       "usdAaaAssignSubscriberLimit": usdAaaAssignSubscriberLimit,
       "usdAaaAssignDomain": usdAaaAssignDomain,
       "usdAaaAssignDomainTable": usdAaaAssignDomainTable,
       "usdAaaAssignDomainEntry": usdAaaAssignDomainEntry,
       "usdAaaAssignDomainName": usdAaaAssignDomainName,
       "usdAaaAssignDomainRowStatus": usdAaaAssignDomainRowStatus,
       "usdAaaAssignDomainRouterName": usdAaaAssignDomainRouterName,
       "usdAaaAssignDomainLoopback": usdAaaAssignDomainLoopback,
       "usdAaaAssignDomainIpHint": usdAaaAssignDomainIpHint,
       "usdAaaAssignDomainAtmServiceLevel": usdAaaAssignDomainAtmServiceLevel,
       "usdAaaAssignDomainAtmPcr": usdAaaAssignDomainAtmPcr,
       "usdAaaAssignDomainAtmScr": usdAaaAssignDomainAtmScr,
       "usdAaaAssignDomainAtmMbs": usdAaaAssignDomainAtmMbs,
       "usdAaaAssignDomainOverrideUserName": usdAaaAssignDomainOverrideUserName,
       "usdAaaAssignDomainOverridePassword": usdAaaAssignDomainOverridePassword,
       "usdAaaAssignDomainStripDomain": usdAaaAssignDomainStripDomain,
       "usdAaaAssignDomainTunnelTable": usdAaaAssignDomainTunnelTable,
       "usdAaaAssignDomainTunnelEntry": usdAaaAssignDomainTunnelEntry,
       "usdAaaAssignDomainTunnelName": usdAaaAssignDomainTunnelName,
       "usdAaaAssignDomainTunnelTag": usdAaaAssignDomainTunnelTag,
       "usdAaaAssignDomainTunnelPreference": usdAaaAssignDomainTunnelPreference,
       "usdAaaAssignDomainTunnelType": usdAaaAssignDomainTunnelType,
       "usdAaaAssignDomainTunnelMedium": usdAaaAssignDomainTunnelMedium,
       "usdAaaAssignDomainTunnelAddress": usdAaaAssignDomainTunnelAddress,
       "usdAaaAssignDomainTunnelPassword": usdAaaAssignDomainTunnelPassword,
       "usdAaaAssignDomainTunnelId": usdAaaAssignDomainTunnelId,
       "usdAaaAssignDomainTunnelHostName": usdAaaAssignDomainTunnelHostName,
       "usdAaaAssignDomainTunnelRowStatus": usdAaaAssignDomainTunnelRowStatus,
       "usdAaaAssignDomainTunnelServerName": usdAaaAssignDomainTunnelServerName,
       "usdAaaAssignDomainTunnelClientAddress": usdAaaAssignDomainTunnelClientAddress,
       "usdAaaAuthentication": usdAaaAuthentication,
       "usdAaaAuthGeneral": usdAaaAuthGeneral,
       "usdAaaAuthMethods": usdAaaAuthMethods,
       "usdAaaAccounting": usdAaaAccounting,
       "usdAaaAcctGeneral": usdAaaAcctGeneral,
       "usdAaaAcctInterval": usdAaaAcctInterval,
       "usdAaaAcctDupServerRouterName": usdAaaAcctDupServerRouterName,
       "usdAaaAcctMethods": usdAaaAcctMethods,
       "usdAaaAcctSendStopOnAaaDeny": usdAaaAcctSendStopOnAaaDeny,
       "usdAaaAcctSendStopOnAaaReject": usdAaaAcctSendStopOnAaaReject,
       "usdAaaAddress": usdAaaAddress,
       "usdAaaAddrGeneral": usdAaaAddrGeneral,
       "usdAaaAddrPoolDefault": usdAaaAddrPoolDefault,
       "usdAaaDupAddrCheck": usdAaaDupAddrCheck,
       "usdAaaAddrNameServer": usdAaaAddrNameServer,
       "usdAaaAddrDns": usdAaaAddrDns,
       "usdAaaAddrDnsPrimary": usdAaaAddrDnsPrimary,
       "usdAaaAddrDnsSecondary": usdAaaAddrDnsSecondary,
       "usdAaaAddrWins": usdAaaAddrWins,
       "usdAaaAddrWinsPrimary": usdAaaAddrWinsPrimary,
       "usdAaaAddrWinsSecondary": usdAaaAddrWinsSecondary,
       "usdAaaStatistics": usdAaaStatistics,
       "usdAaaIncomingInitiateRequests": usdAaaIncomingInitiateRequests,
       "usdAaaIncomingTerminateRequests": usdAaaIncomingTerminateRequests,
       "usdAaaOutgoingTunnelGrantResponses": usdAaaOutgoingTunnelGrantResponses,
       "usdAaaOutgoingGrantResponses": usdAaaOutgoingGrantResponses,
       "usdAaaOutgoingDenyResponses": usdAaaOutgoingDenyResponses,
       "usdAaaOutgoingErrorResponses": usdAaaOutgoingErrorResponses,
       "usdAaaOutgoingAuthRequests": usdAaaOutgoingAuthRequests,
       "usdAaaIncomingAuthResponses": usdAaaIncomingAuthResponses,
       "usdAaaOutgoingReAuthRequests": usdAaaOutgoingReAuthRequests,
       "usdAaaIncomingReAuthResponses": usdAaaIncomingReAuthResponses,
       "usdAaaOutgoingAcctRequests": usdAaaOutgoingAcctRequests,
       "usdAaaIncomingAcctResponses": usdAaaIncomingAcctResponses,
       "usdAaaOutgoingDupAcctRequests": usdAaaOutgoingDupAcctRequests,
       "usdAaaIncomingDupAcctResponses": usdAaaIncomingDupAcctResponses,
       "usdAaaOutgoingAddrRequests": usdAaaOutgoingAddrRequests,
       "usdAaaIncomingAddrResponses": usdAaaIncomingAddrResponses,
       "usdAaaTimeout": usdAaaTimeout,
       "usdAaaTimeoutGeneral": usdAaaTimeoutGeneral,
       "usdAaaIdleTimeout": usdAaaIdleTimeout,
       "usdAaaSessionTimeout": usdAaaSessionTimeout,
       "usdAaaTunnel": usdAaaTunnel,
       "usdAaaTunnelGeneral": usdAaaTunnelGeneral,
       "usdAaaTunnelClientName": usdAaaTunnelClientName,
       "usdAaaTunnelPassword": usdAaaTunnelPassword,
       "usdAaaTunnelNasPortMethod": usdAaaTunnelNasPortMethod,
       "usdAaaTunnelIgnoreNasPort": usdAaaTunnelIgnoreNasPort,
       "usdAaaTunnelIgnoreNasPortType": usdAaaTunnelIgnoreNasPortType,
       "usdAaaTunnelAssignmentIdFormat": usdAaaTunnelAssignmentIdFormat,
       "usdAaaSubscribers": usdAaaSubscribers,
       "usdAaaSubscriberMaxCount": usdAaaSubscriberMaxCount,
       "usdAaaSubscriberPeakCount": usdAaaSubscriberPeakCount,
       "usdAaaSubscriberCount": usdAaaSubscriberCount,
       "usdAaaSubscriberTable": usdAaaSubscriberTable,
       "usdAaaSubscriberEntry": usdAaaSubscriberEntry,
       "usdAaaSubscriberHandle": usdAaaSubscriberHandle,
       "usdAaaSubscriberUserName": usdAaaSubscriberUserName,
       "usdAaaSubscriberRouterName": usdAaaSubscriberRouterName,
       "usdAaaSubscriberRouterIndex": usdAaaSubscriberRouterIndex,
       "usdAaaSubscriberLoginTime": usdAaaSubscriberLoginTime,
       "usdAaaSubscriberIpAddress": usdAaaSubscriberIpAddress,
       "usdAaaSubscriberIpAddressMask": usdAaaSubscriberIpAddressMask,
       "usdAaaSubscriberAddrAssignType": usdAaaSubscriberAddrAssignType,
       "usdAaaSubscriberInterfaceId": usdAaaSubscriberInterfaceId,
       "usdAaaSubscriberState": usdAaaSubscriberState,
       "usdAaaSubscriberClientType": usdAaaSubscriberClientType,
       "usdAaaSubscriberIngressPolicyName": usdAaaSubscriberIngressPolicyName,
       "usdAaaSubscriberEgressPolicyName": usdAaaSubscriberEgressPolicyName,
       "usdAaaSubscriberQosProfileName": usdAaaSubscriberQosProfileName,
       "usdAaaSubscriberRowStatus": usdAaaSubscriberRowStatus,
       "usdAaaSubscriberRouterSummaryTable": usdAaaSubscriberRouterSummaryTable,
       "usdAaaSubscriberRouterSummaryEntry": usdAaaSubscriberRouterSummaryEntry,
       "usdAaaSubscriberRouterSummaryRouterIndex": usdAaaSubscriberRouterSummaryRouterIndex,
       "usdAaaSubscriberRouterSummaryCount": usdAaaSubscriberRouterSummaryCount,
       "usdAaaSubscriberRouterTable": usdAaaSubscriberRouterTable,
       "usdAaaSubscriberRouterEntry": usdAaaSubscriberRouterEntry,
       "usdAaaSubscriberRouterRouterIndex": usdAaaSubscriberRouterRouterIndex,
       "usdAaaSubscriberRouterHandle": usdAaaSubscriberRouterHandle,
       "usdAaaSubscriberRouterRowStatus": usdAaaSubscriberRouterRowStatus,
       "usdAaaSubscriberLocationType": usdAaaSubscriberLocationType,
       "usdAaaSubscriberLocationSummaryTable": usdAaaSubscriberLocationSummaryTable,
       "usdAaaSubscriberLocationSummaryEntry": usdAaaSubscriberLocationSummaryEntry,
       "usdAaaSubscriberLocationSummaryLocationIndex": usdAaaSubscriberLocationSummaryLocationIndex,
       "usdAaaSubscriberLocationSummaryCount": usdAaaSubscriberLocationSummaryCount,
       "usdAaaSubscriberLocationTable": usdAaaSubscriberLocationTable,
       "usdAaaSubscriberLocationEntry": usdAaaSubscriberLocationEntry,
       "usdAaaSubscriberLocationLocationIndex": usdAaaSubscriberLocationLocationIndex,
       "usdAaaSubscriberLocationHandle": usdAaaSubscriberLocationHandle,
       "usdAaaSubscriberLocationRowStatus": usdAaaSubscriberLocationRowStatus,
       "usdAaaSubscriberPseudoPeakCount": usdAaaSubscriberPseudoPeakCount,
       "usdAaaSubscriberPseudoCount": usdAaaSubscriberPseudoCount,
       "usdAaaCapabilities": usdAaaCapabilities,
       "usdAaaAccountingCapability": usdAaaAccountingCapability,
       "usdAaaAddressAssignmentCapability": usdAaaAddressAssignmentCapability,
       "usdAaaBrasCapability": usdAaaBrasCapability,
       "usdAaaTunnelingCapability": usdAaaTunnelingCapability,
       "usdAaaMIBConformance": usdAaaMIBConformance,
       "usdAaaMIBCompliances": usdAaaMIBCompliances,
       "usdAaaCompliance": usdAaaCompliance,
       "usdAaaCompliance2": usdAaaCompliance2,
       "usdAaaCompliance3": usdAaaCompliance3,
       "usdAaaCompliance4": usdAaaCompliance4,
       "usdAaaCompliance5": usdAaaCompliance5,
       "usdAaaCompliance6": usdAaaCompliance6,
       "usdAaaCompliance7": usdAaaCompliance7,
       "usdAaaCompliance8": usdAaaCompliance8,
       "usdAaaMIBGroups": usdAaaMIBGroups,
       "usdAaaGroup": usdAaaGroup,
       "usdAaaGroup2": usdAaaGroup2,
       "usdAaaBasicGroup": usdAaaBasicGroup,
       "usdAaaBrasGroup": usdAaaBrasGroup,
       "usdAaaTunnelGroup": usdAaaTunnelGroup,
       "usdAaaAuthenticationGroup": usdAaaAuthenticationGroup,
       "usdAaaAccountingGroup": usdAaaAccountingGroup,
       "usdAaaAddressGroup": usdAaaAddressGroup,
       "usdAaaBrasGroup2": usdAaaBrasGroup2,
       "usdAaaBrasGroup3": usdAaaBrasGroup3,
       "usdAaaSubscriberGroup": usdAaaSubscriberGroup,
       "usdAaaCapabilitiesGroup": usdAaaCapabilitiesGroup,
       "usdAaaSubscriberGroup2": usdAaaSubscriberGroup2,
       "usdAaaAccountingGroup2": usdAaaAccountingGroup2,
       "usdAaaBrasGroup4": usdAaaBrasGroup4,
       "usdAaaSubscriberGroup3": usdAaaSubscriberGroup3}
)
