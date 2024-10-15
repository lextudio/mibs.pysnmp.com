# SNMP MIB module (ENTERASYS-MGMD-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MGMD-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:10 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

etsysMgmdExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71)
)
etsysMgmdExtMIB.setRevisions(
        ("2010-02-08 14:08",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MGMDNumGroupsTc(Integer32, TextualConvention):
    status = "current"
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
        *(("default", 3),
          ("maximum", 4),
          ("minimum", 2),
          ("none", 1))
    )



class MGMDPortModeTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reporter", 1),
          ("source", 2))
    )



class MGMDDiscoveredRouterModeTc(Integer32, TextualConvention):
    status = "current"
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
        *(("multicastRouterDiscovery", 3),
          ("querier", 1),
          ("routingProtocol", 2),
          ("staticallyConfigured", 4))
    )



class MGMDProtocolClassTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("multicastData", 1),
          ("routingProtocol", 2))
    )



class MGMDProtocolIdTc(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EtsysMgmdExtObjects_ObjectIdentity = ObjectIdentity
etsysMgmdExtObjects = _EtsysMgmdExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1)
)
_EtsysMgmdExtConfigGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtConfigGroup = _EtsysMgmdExtConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1)
)
_EtsysMgmdExtConfigRevString_Type = SnmpAdminString
_EtsysMgmdExtConfigRevString_Object = MibScalar
etsysMgmdExtConfigRevString = _EtsysMgmdExtConfigRevString_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 1),
    _EtsysMgmdExtConfigRevString_Type()
)
etsysMgmdExtConfigRevString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigRevString.setStatus("current")


class _EtsysMgmdExtConfigFullAction_Type(Integer32):
    """Custom type etsysMgmdExtConfigFullAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flood", 2),
          ("routers", 1))
    )


_EtsysMgmdExtConfigFullAction_Type.__name__ = "Integer32"
_EtsysMgmdExtConfigFullAction_Object = MibScalar
etsysMgmdExtConfigFullAction = _EtsysMgmdExtConfigFullAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 2),
    _EtsysMgmdExtConfigFullAction_Type()
)
etsysMgmdExtConfigFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigFullAction.setStatus("current")
_EtsysMgmdExtConfigMinNumberOfGroups_Type = Integer32
_EtsysMgmdExtConfigMinNumberOfGroups_Object = MibScalar
etsysMgmdExtConfigMinNumberOfGroups = _EtsysMgmdExtConfigMinNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 3),
    _EtsysMgmdExtConfigMinNumberOfGroups_Type()
)
etsysMgmdExtConfigMinNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigMinNumberOfGroups.setStatus("current")
_EtsysMgmdExtConfigDefaultNumberOfGroups_Type = Integer32
_EtsysMgmdExtConfigDefaultNumberOfGroups_Object = MibScalar
etsysMgmdExtConfigDefaultNumberOfGroups = _EtsysMgmdExtConfigDefaultNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 4),
    _EtsysMgmdExtConfigDefaultNumberOfGroups_Type()
)
etsysMgmdExtConfigDefaultNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigDefaultNumberOfGroups.setStatus("current")
_EtsysMgmdExtConfigMaxNumberOfGroups_Type = Integer32
_EtsysMgmdExtConfigMaxNumberOfGroups_Object = MibScalar
etsysMgmdExtConfigMaxNumberOfGroups = _EtsysMgmdExtConfigMaxNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 5),
    _EtsysMgmdExtConfigMaxNumberOfGroups_Type()
)
etsysMgmdExtConfigMaxNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigMaxNumberOfGroups.setStatus("current")


class _EtsysMgmdExtConfigNumberOfGroups_Type(MGMDNumGroupsTc):
    """Custom type etsysMgmdExtConfigNumberOfGroups based on MGMDNumGroupsTc"""


_EtsysMgmdExtConfigNumberOfGroups_Object = MibScalar
etsysMgmdExtConfigNumberOfGroups = _EtsysMgmdExtConfigNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 1, 6),
    _EtsysMgmdExtConfigNumberOfGroups_Type()
)
etsysMgmdExtConfigNumberOfGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtConfigNumberOfGroups.setStatus("current")
_EtsysMgmdExtInterfaceGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtInterfaceGroup = _EtsysMgmdExtInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2)
)
_EtsysMgmdExtInterfaceTable_Object = MibTable
etsysMgmdExtInterfaceTable = _EtsysMgmdExtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceTable.setStatus("current")
_EtsysMgmdExtInterfaceEntry_Object = MibTableRow
etsysMgmdExtInterfaceEntry = _EtsysMgmdExtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1)
)
etsysMgmdExtInterfaceEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceApplication"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceEntry.setStatus("current")
_EtsysMgmdExtInterfaceApplication_Type = InetAddressType
_EtsysMgmdExtInterfaceApplication_Object = MibTableColumn
etsysMgmdExtInterfaceApplication = _EtsysMgmdExtInterfaceApplication_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 1),
    _EtsysMgmdExtInterfaceApplication_Type()
)
etsysMgmdExtInterfaceApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceApplication.setStatus("current")


class _EtsysMgmdExtInterfaceQueryEnableState_Type(EnabledStatus):
    """Custom type etsysMgmdExtInterfaceQueryEnableState based on EnabledStatus"""


_EtsysMgmdExtInterfaceQueryEnableState_Object = MibTableColumn
etsysMgmdExtInterfaceQueryEnableState = _EtsysMgmdExtInterfaceQueryEnableState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 2),
    _EtsysMgmdExtInterfaceQueryEnableState_Type()
)
etsysMgmdExtInterfaceQueryEnableState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceQueryEnableState.setStatus("current")


class _EtsysMgmdExtInterfaceFastLeaveState_Type(EnabledStatus):
    """Custom type etsysMgmdExtInterfaceFastLeaveState based on EnabledStatus"""


_EtsysMgmdExtInterfaceFastLeaveState_Object = MibTableColumn
etsysMgmdExtInterfaceFastLeaveState = _EtsysMgmdExtInterfaceFastLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 3),
    _EtsysMgmdExtInterfaceFastLeaveState_Type()
)
etsysMgmdExtInterfaceFastLeaveState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceFastLeaveState.setStatus("current")
_EtsysMgmdExtInterfaceClearGroups_Type = TruthValue
_EtsysMgmdExtInterfaceClearGroups_Object = MibTableColumn
etsysMgmdExtInterfaceClearGroups = _EtsysMgmdExtInterfaceClearGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 4),
    _EtsysMgmdExtInterfaceClearGroups_Type()
)
etsysMgmdExtInterfaceClearGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceClearGroups.setStatus("current")


class _EtsysMgmdExtRtrAlertRequired_Type(TruthValue):
    """Custom type etsysMgmdExtRtrAlertRequired based on TruthValue"""


_EtsysMgmdExtRtrAlertRequired_Object = MibTableColumn
etsysMgmdExtRtrAlertRequired = _EtsysMgmdExtRtrAlertRequired_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 2, 1, 1, 5),
    _EtsysMgmdExtRtrAlertRequired_Type()
)
etsysMgmdExtRtrAlertRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtRtrAlertRequired.setStatus("current")
_EtsysMgmdExtStaticCacheGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtStaticCacheGroup = _EtsysMgmdExtStaticCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3)
)
_EtsysMgmdExtStaticCacheTable_Object = MibTable
etsysMgmdExtStaticCacheTable = _EtsysMgmdExtStaticCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheTable.setStatus("current")
_EtsysMgmdExtStaticCacheEntry_Object = MibTableRow
etsysMgmdExtStaticCacheEntry = _EtsysMgmdExtStaticCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1)
)
etsysMgmdExtStaticCacheEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIPAddrType"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheGroupIPAddress"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheSourceIPAddress"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheEntry.setStatus("current")
_EtsysMgmdExtStaticCacheIPAddrType_Type = InetAddressType
_EtsysMgmdExtStaticCacheIPAddrType_Object = MibTableColumn
etsysMgmdExtStaticCacheIPAddrType = _EtsysMgmdExtStaticCacheIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 1),
    _EtsysMgmdExtStaticCacheIPAddrType_Type()
)
etsysMgmdExtStaticCacheIPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheIPAddrType.setStatus("current")


class _EtsysMgmdExtStaticCacheGroupIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtStaticCacheGroupIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtStaticCacheGroupIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtStaticCacheGroupIPAddress_Object = MibTableColumn
etsysMgmdExtStaticCacheGroupIPAddress = _EtsysMgmdExtStaticCacheGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 2),
    _EtsysMgmdExtStaticCacheGroupIPAddress_Type()
)
etsysMgmdExtStaticCacheGroupIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheGroupIPAddress.setStatus("current")


class _EtsysMgmdExtStaticCacheSourceIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtStaticCacheSourceIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtStaticCacheSourceIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtStaticCacheSourceIPAddress_Object = MibTableColumn
etsysMgmdExtStaticCacheSourceIPAddress = _EtsysMgmdExtStaticCacheSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 3),
    _EtsysMgmdExtStaticCacheSourceIPAddress_Type()
)
etsysMgmdExtStaticCacheSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheSourceIPAddress.setStatus("current")
_EtsysMgmdExtStaticCacheIncludeList_Type = PortList
_EtsysMgmdExtStaticCacheIncludeList_Object = MibTableColumn
etsysMgmdExtStaticCacheIncludeList = _EtsysMgmdExtStaticCacheIncludeList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 4),
    _EtsysMgmdExtStaticCacheIncludeList_Type()
)
etsysMgmdExtStaticCacheIncludeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheIncludeList.setStatus("current")
_EtsysMgmdExtStaticCacheExcludeList_Type = PortList
_EtsysMgmdExtStaticCacheExcludeList_Object = MibTableColumn
etsysMgmdExtStaticCacheExcludeList = _EtsysMgmdExtStaticCacheExcludeList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 5),
    _EtsysMgmdExtStaticCacheExcludeList_Type()
)
etsysMgmdExtStaticCacheExcludeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheExcludeList.setStatus("current")
_EtsysMgmdExtStaticCacheRowStatus_Type = RowStatus
_EtsysMgmdExtStaticCacheRowStatus_Object = MibTableColumn
etsysMgmdExtStaticCacheRowStatus = _EtsysMgmdExtStaticCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 3, 1, 1, 6),
    _EtsysMgmdExtStaticCacheRowStatus_Type()
)
etsysMgmdExtStaticCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheRowStatus.setStatus("current")
_EtsysMgmdExtCacheGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtCacheGroup = _EtsysMgmdExtCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4)
)
_EtsysMgmdExtCacheTable_Object = MibTable
etsysMgmdExtCacheTable = _EtsysMgmdExtCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtCacheTable.setStatus("current")
_EtsysMgmdExtCacheEntry_Object = MibTableRow
etsysMgmdExtCacheEntry = _EtsysMgmdExtCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1)
)
etsysMgmdExtCacheEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheIPAddrType"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheGroupIPAddress"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheSourceIPAddress"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtCacheEntry.setStatus("current")
_EtsysMgmdExtCacheIPAddrType_Type = InetAddressType
_EtsysMgmdExtCacheIPAddrType_Object = MibTableColumn
etsysMgmdExtCacheIPAddrType = _EtsysMgmdExtCacheIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 1),
    _EtsysMgmdExtCacheIPAddrType_Type()
)
etsysMgmdExtCacheIPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheIPAddrType.setStatus("current")


class _EtsysMgmdExtCacheGroupIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtCacheGroupIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtCacheGroupIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtCacheGroupIPAddress_Object = MibTableColumn
etsysMgmdExtCacheGroupIPAddress = _EtsysMgmdExtCacheGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 2),
    _EtsysMgmdExtCacheGroupIPAddress_Type()
)
etsysMgmdExtCacheGroupIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheGroupIPAddress.setStatus("current")


class _EtsysMgmdExtCacheSourceIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtCacheSourceIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtCacheSourceIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtCacheSourceIPAddress_Object = MibTableColumn
etsysMgmdExtCacheSourceIPAddress = _EtsysMgmdExtCacheSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 3),
    _EtsysMgmdExtCacheSourceIPAddress_Type()
)
etsysMgmdExtCacheSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheSourceIPAddress.setStatus("current")
_EtsysMgmdExtCacheExpiryTime_Type = Integer32
_EtsysMgmdExtCacheExpiryTime_Object = MibTableColumn
etsysMgmdExtCacheExpiryTime = _EtsysMgmdExtCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 4),
    _EtsysMgmdExtCacheExpiryTime_Type()
)
etsysMgmdExtCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheExpiryTime.setUnits("seconds")
_EtsysMgmdExtCacheIncludePortList_Type = PortList
_EtsysMgmdExtCacheIncludePortList_Object = MibTableColumn
etsysMgmdExtCacheIncludePortList = _EtsysMgmdExtCacheIncludePortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 5),
    _EtsysMgmdExtCacheIncludePortList_Type()
)
etsysMgmdExtCacheIncludePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheIncludePortList.setStatus("current")
_EtsysMgmdExtCacheExcludePortList_Type = PortList
_EtsysMgmdExtCacheExcludePortList_Object = MibTableColumn
etsysMgmdExtCacheExcludePortList = _EtsysMgmdExtCacheExcludePortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 6),
    _EtsysMgmdExtCacheExcludePortList_Type()
)
etsysMgmdExtCacheExcludePortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheExcludePortList.setStatus("current")


class _EtsysMgmdExtCacheSrcPort_Type(Integer32):
    """Custom type etsysMgmdExtCacheSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysMgmdExtCacheSrcPort_Type.__name__ = "Integer32"
_EtsysMgmdExtCacheSrcPort_Object = MibTableColumn
etsysMgmdExtCacheSrcPort = _EtsysMgmdExtCacheSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 4, 1, 1, 7),
    _EtsysMgmdExtCacheSrcPort_Type()
)
etsysMgmdExtCacheSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtCacheSrcPort.setStatus("current")
_EtsysMgmdExtDiscoveredRouterGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtDiscoveredRouterGroup = _EtsysMgmdExtDiscoveredRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5)
)
_EtsysMgmdExtDiscoveredRouterTable_Object = MibTable
etsysMgmdExtDiscoveredRouterTable = _EtsysMgmdExtDiscoveredRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterTable.setStatus("current")
_EtsysMgmdExtDiscoveredRouterEntry_Object = MibTableRow
etsysMgmdExtDiscoveredRouterEntry = _EtsysMgmdExtDiscoveredRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1)
)
etsysMgmdExtDiscoveredRouterEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterApplication"),
    (0, "IF-MIB", "ifIndex"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterEntry.setStatus("current")
_EtsysMgmdExtDiscoveredRouterApplication_Type = InetAddressType
_EtsysMgmdExtDiscoveredRouterApplication_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterApplication = _EtsysMgmdExtDiscoveredRouterApplication_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 1),
    _EtsysMgmdExtDiscoveredRouterApplication_Type()
)
etsysMgmdExtDiscoveredRouterApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterApplication.setStatus("current")
_EtsysMgmdExtDiscoveredRouterLearnedMethod_Type = MGMDDiscoveredRouterModeTc
_EtsysMgmdExtDiscoveredRouterLearnedMethod_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterLearnedMethod = _EtsysMgmdExtDiscoveredRouterLearnedMethod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 2),
    _EtsysMgmdExtDiscoveredRouterLearnedMethod_Type()
)
etsysMgmdExtDiscoveredRouterLearnedMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterLearnedMethod.setStatus("current")
_EtsysMgmdExtDiscoveredRouterEgressing_Type = TruthValue
_EtsysMgmdExtDiscoveredRouterEgressing_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterEgressing = _EtsysMgmdExtDiscoveredRouterEgressing_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 3),
    _EtsysMgmdExtDiscoveredRouterEgressing_Type()
)
etsysMgmdExtDiscoveredRouterEgressing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterEgressing.setStatus("current")


class _EtsysMgmdExtDiscoveredRouterStaticPortList_Type(EnabledStatus):
    """Custom type etsysMgmdExtDiscoveredRouterStaticPortList based on EnabledStatus"""


_EtsysMgmdExtDiscoveredRouterStaticPortList_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterStaticPortList = _EtsysMgmdExtDiscoveredRouterStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 4),
    _EtsysMgmdExtDiscoveredRouterStaticPortList_Type()
)
etsysMgmdExtDiscoveredRouterStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterStaticPortList.setStatus("current")
_EtsysMgmdExtDiscoveredRouterBridgePortAgeTime_Type = TimeTicks
_EtsysMgmdExtDiscoveredRouterBridgePortAgeTime_Object = MibTableColumn
etsysMgmdExtDiscoveredRouterBridgePortAgeTime = _EtsysMgmdExtDiscoveredRouterBridgePortAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 5, 1, 1, 5),
    _EtsysMgmdExtDiscoveredRouterBridgePortAgeTime_Type()
)
etsysMgmdExtDiscoveredRouterBridgePortAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterBridgePortAgeTime.setStatus("current")
_EtsysMgmdExtPortGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtPortGroup = _EtsysMgmdExtPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6)
)
_EtsysMgmdExtPortTable_Object = MibTable
etsysMgmdExtPortTable = _EtsysMgmdExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortTable.setStatus("current")
_EtsysMgmdExtPortTableEntry_Object = MibTableRow
etsysMgmdExtPortTableEntry = _EtsysMgmdExtPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1)
)
etsysMgmdExtPortTableEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortMode"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortIPAddressType"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortTableGroupIPAddress"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortTableSourceIPAddress"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableEntry.setStatus("current")
_EtsysMgmdExtPortMode_Type = MGMDPortModeTc
_EtsysMgmdExtPortMode_Object = MibTableColumn
etsysMgmdExtPortMode = _EtsysMgmdExtPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 1),
    _EtsysMgmdExtPortMode_Type()
)
etsysMgmdExtPortMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtPortMode.setStatus("current")
_EtsysMgmdExtPortIPAddressType_Type = InetAddressType
_EtsysMgmdExtPortIPAddressType_Object = MibTableColumn
etsysMgmdExtPortIPAddressType = _EtsysMgmdExtPortIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 2),
    _EtsysMgmdExtPortIPAddressType_Type()
)
etsysMgmdExtPortIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtPortIPAddressType.setStatus("current")


class _EtsysMgmdExtPortTableGroupIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtPortTableGroupIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtPortTableGroupIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtPortTableGroupIPAddress_Object = MibTableColumn
etsysMgmdExtPortTableGroupIPAddress = _EtsysMgmdExtPortTableGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 3),
    _EtsysMgmdExtPortTableGroupIPAddress_Type()
)
etsysMgmdExtPortTableGroupIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableGroupIPAddress.setStatus("current")


class _EtsysMgmdExtPortTableSourceIPAddress_Type(InetAddress):
    """Custom type etsysMgmdExtPortTableSourceIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EtsysMgmdExtPortTableSourceIPAddress_Type.__name__ = "InetAddress"
_EtsysMgmdExtPortTableSourceIPAddress_Object = MibTableColumn
etsysMgmdExtPortTableSourceIPAddress = _EtsysMgmdExtPortTableSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 4),
    _EtsysMgmdExtPortTableSourceIPAddress_Type()
)
etsysMgmdExtPortTableSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableSourceIPAddress.setStatus("current")
_EtsysMgmdExtPortTableExpireTime_Type = Integer32
_EtsysMgmdExtPortTableExpireTime_Object = MibTableColumn
etsysMgmdExtPortTableExpireTime = _EtsysMgmdExtPortTableExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 6, 1, 1, 5),
    _EtsysMgmdExtPortTableExpireTime_Type()
)
etsysMgmdExtPortTableExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysMgmdExtPortTableExpireTime.setUnits("seconds")
_EtsysMgmdExtPortFastLeaveGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtPortFastLeaveGroup = _EtsysMgmdExtPortFastLeaveGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 7)
)
_EtsysMgmdExtPortFastLeaveTable_Object = MibTable
etsysMgmdExtPortFastLeaveTable = _EtsysMgmdExtPortFastLeaveTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 7, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortFastLeaveTable.setStatus("current")
_EtsysMgmdExtPortFastLeaveTableEntry_Object = MibTableRow
etsysMgmdExtPortFastLeaveTableEntry = _EtsysMgmdExtPortFastLeaveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 7, 1, 1)
)
etsysMgmdExtPortFastLeaveTableEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortFastLeaveTableEntry.setStatus("current")


class _EtsysMgmdExtPortFastLeaveState_Type(EnabledStatus):
    """Custom type etsysMgmdExtPortFastLeaveState based on EnabledStatus"""


_EtsysMgmdExtPortFastLeaveState_Object = MibTableColumn
etsysMgmdExtPortFastLeaveState = _EtsysMgmdExtPortFastLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 7, 1, 1, 1),
    _EtsysMgmdExtPortFastLeaveState_Type()
)
etsysMgmdExtPortFastLeaveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtPortFastLeaveState.setStatus("current")
_EtsysMgmdExtStatsCntrsGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtStatsCntrsGroup = _EtsysMgmdExtStatsCntrsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8)
)
_EtsysMgmdExtStatsCntrsTable_Object = MibTable
etsysMgmdExtStatsCntrsTable = _EtsysMgmdExtStatsCntrsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsTable.setStatus("current")
_EtsysMgmdExtStatsCntrsEntry_Object = MibTableRow
etsysMgmdExtStatsCntrsEntry = _EtsysMgmdExtStatsCntrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1)
)
etsysMgmdExtStatsCntrsEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsApplication"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsEntry.setStatus("current")
_EtsysMgmdExtStatsCntrsApplication_Type = InetAddressType
_EtsysMgmdExtStatsCntrsApplication_Object = MibTableColumn
etsysMgmdExtStatsCntrsApplication = _EtsysMgmdExtStatsCntrsApplication_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 1),
    _EtsysMgmdExtStatsCntrsApplication_Type()
)
etsysMgmdExtStatsCntrsApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsApplication.setStatus("current")
_EtsysMgmdExtStatsCntrsGroupFull_Type = TruthValue
_EtsysMgmdExtStatsCntrsGroupFull_Object = MibTableColumn
etsysMgmdExtStatsCntrsGroupFull = _EtsysMgmdExtStatsCntrsGroupFull_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 2),
    _EtsysMgmdExtStatsCntrsGroupFull_Type()
)
etsysMgmdExtStatsCntrsGroupFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsGroupFull.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV1QueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV1QueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV1QueriesSent = _EtsysMgmdExtStatsCntrsNumV1QueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 3),
    _EtsysMgmdExtStatsCntrsNumV1QueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumV1QueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV1QueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV2QueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV2QueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV2QueriesSent = _EtsysMgmdExtStatsCntrsNumV2QueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 4),
    _EtsysMgmdExtStatsCntrsNumV2QueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumV2QueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV2QueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV3QueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV3QueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV3QueriesSent = _EtsysMgmdExtStatsCntrsNumV3QueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 5),
    _EtsysMgmdExtStatsCntrsNumV3QueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumV3QueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV3QueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumGSQueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumGSQueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumGSQueriesSent = _EtsysMgmdExtStatsCntrsNumGSQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 6),
    _EtsysMgmdExtStatsCntrsNumGSQueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumGSQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumGSQueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumGAndSQueriesSent_Type = Counter32
_EtsysMgmdExtStatsCntrsNumGAndSQueriesSent_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumGAndSQueriesSent = _EtsysMgmdExtStatsCntrsNumGAndSQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 7),
    _EtsysMgmdExtStatsCntrsNumGAndSQueriesSent_Type()
)
etsysMgmdExtStatsCntrsNumGAndSQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumGAndSQueriesSent.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV1QueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV1QueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV1QueriesRcvd = _EtsysMgmdExtStatsCntrsNumV1QueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 8),
    _EtsysMgmdExtStatsCntrsNumV1QueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV1QueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV1QueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV2QueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV2QueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV2QueriesRcvd = _EtsysMgmdExtStatsCntrsNumV2QueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 9),
    _EtsysMgmdExtStatsCntrsNumV2QueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV2QueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV2QueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV3QueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV3QueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV3QueriesRcvd = _EtsysMgmdExtStatsCntrsNumV3QueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 10),
    _EtsysMgmdExtStatsCntrsNumV3QueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV3QueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV3QueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumGSQueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumGSQueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumGSQueriesRcvd = _EtsysMgmdExtStatsCntrsNumGSQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 11),
    _EtsysMgmdExtStatsCntrsNumGSQueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumGSQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumGSQueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumGAndSQueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumGAndSQueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd = _EtsysMgmdExtStatsCntrsNumGAndSQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 12),
    _EtsysMgmdExtStatsCntrsNumGAndSQueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd = _EtsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 13),
    _EtsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV1ReportsRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV1ReportsRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV1ReportsRcvd = _EtsysMgmdExtStatsCntrsNumV1ReportsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 14),
    _EtsysMgmdExtStatsCntrsNumV1ReportsRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV1ReportsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV1ReportsRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV2ReportsRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV2ReportsRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV2ReportsRcvd = _EtsysMgmdExtStatsCntrsNumV2ReportsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 15),
    _EtsysMgmdExtStatsCntrsNumV2ReportsRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV2ReportsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV2ReportsRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumV3ReportsRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumV3ReportsRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumV3ReportsRcvd = _EtsysMgmdExtStatsCntrsNumV3ReportsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 16),
    _EtsysMgmdExtStatsCntrsNumV3ReportsRcvd_Type()
)
etsysMgmdExtStatsCntrsNumV3ReportsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumV3ReportsRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumLeavesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumLeavesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumLeavesRcvd = _EtsysMgmdExtStatsCntrsNumLeavesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 17),
    _EtsysMgmdExtStatsCntrsNumLeavesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumLeavesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumLeavesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsNumBadFramesRcvd_Type = Counter32
_EtsysMgmdExtStatsCntrsNumBadFramesRcvd_Object = MibTableColumn
etsysMgmdExtStatsCntrsNumBadFramesRcvd = _EtsysMgmdExtStatsCntrsNumBadFramesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 18),
    _EtsysMgmdExtStatsCntrsNumBadFramesRcvd_Type()
)
etsysMgmdExtStatsCntrsNumBadFramesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsNumBadFramesRcvd.setStatus("current")
_EtsysMgmdExtStatsCntrsClear_Type = TruthValue
_EtsysMgmdExtStatsCntrsClear_Object = MibTableColumn
etsysMgmdExtStatsCntrsClear = _EtsysMgmdExtStatsCntrsClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 8, 1, 1, 19),
    _EtsysMgmdExtStatsCntrsClear_Type()
)
etsysMgmdExtStatsCntrsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntrsClear.setStatus("current")
_EtsysMgmdExtProtocolClassificationGroup_ObjectIdentity = ObjectIdentity
etsysMgmdExtProtocolClassificationGroup = _EtsysMgmdExtProtocolClassificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9)
)
_EtsysMgmdExtProtocolClassificationTable_Object = MibTable
etsysMgmdExtProtocolClassificationTable = _EtsysMgmdExtProtocolClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolClassificationTable.setStatus("current")
_EtsysMgmdExtProtocolClassificationEntry_Object = MibTableRow
etsysMgmdExtProtocolClassificationEntry = _EtsysMgmdExtProtocolClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9, 1, 1)
)
etsysMgmdExtProtocolClassificationEntry.setIndexNames(
    (0, "ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtProtocolClassification"),
)
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolClassificationEntry.setStatus("current")
_EtsysMgmdExtProtocolClassification_Type = MGMDProtocolClassTc
_EtsysMgmdExtProtocolClassification_Object = MibTableColumn
etsysMgmdExtProtocolClassification = _EtsysMgmdExtProtocolClassification_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9, 1, 1, 1),
    _EtsysMgmdExtProtocolClassification_Type()
)
etsysMgmdExtProtocolClassification.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolClassification.setStatus("current")
_EtsysMgmdExtProtocolIdentifier_Type = MGMDProtocolIdTc
_EtsysMgmdExtProtocolIdentifier_Object = MibTableColumn
etsysMgmdExtProtocolIdentifier = _EtsysMgmdExtProtocolIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 1, 9, 1, 1, 2),
    _EtsysMgmdExtProtocolIdentifier_Type()
)
etsysMgmdExtProtocolIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolIdentifier.setStatus("current")
_EtsysMgmdExtConformance_ObjectIdentity = ObjectIdentity
etsysMgmdExtConformance = _EtsysMgmdExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2)
)
_EtsysMgmdExtGroups_ObjectIdentity = ObjectIdentity
etsysMgmdExtGroups = _EtsysMgmdExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1)
)
_EtsysMgmdExtCompliances_ObjectIdentity = ObjectIdentity
etsysMgmdExtCompliances = _EtsysMgmdExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 2)
)

# Managed Objects groups

etsysMgmdExtConfigGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 1)
)
etsysMgmdExtConfigGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigRevString"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFullAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMinNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigDefaultNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMaxNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigNumberOfGroups"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtConfigGroups.setStatus("current")

etsysMgmdExtInterfaceGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 2)
)
etsysMgmdExtInterfaceGroups.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFastLeaveState")
)
if mibBuilder.loadTexts:
    etsysMgmdExtInterfaceGroups.setStatus("current")

etsysMgmdExtStaticCacheGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 3)
)
etsysMgmdExtStaticCacheGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIncludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheExcludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheRowStatus"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtStaticCacheGroups.setStatus("current")

etsysMgmdExtCacheGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 4)
)
etsysMgmdExtCacheGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExpiryTime"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheIncludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExcludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheSrcPort"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtCacheGroups.setStatus("current")

etsysMgmdExtDiscoveredRouterGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 5)
)
etsysMgmdExtDiscoveredRouterGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterLearnedMethod"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterEgressing"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterStaticPortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterBridgePortAgeTime"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtDiscoveredRouterGroups.setStatus("current")

etsysMgmdExtPortGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 6)
)
etsysMgmdExtPortGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortTableGroupIPAddress"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortTableSourceIPAddress"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortTableExpireTime"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortGroups.setStatus("current")

etsysMgmdExtPortFastLeaveGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 7)
)
etsysMgmdExtPortFastLeaveGroups.setObjects(
    ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortFastLeaveState")
)
if mibBuilder.loadTexts:
    etsysMgmdExtPortFastLeaveGroups.setStatus("current")

etsysMgmdExtStatsCntsGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 8)
)
etsysMgmdExtStatsCntsGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsApplication"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsGroupFull"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumLeavesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumBadFramesRcvd"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtStatsCntsGroups.setStatus("current")

etsysMgmdExtProtocolClassificationGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 9)
)
etsysMgmdExtProtocolClassificationGroups.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtProtocolClassification"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtProtocolIdentifier"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtProtocolClassificationGroups.setStatus("current")

etsysMgmdExtReadBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 10)
)
etsysMgmdExtReadBaseGroup.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigRevString"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFullAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMinNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigDefaultNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigMaxNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIncludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheExcludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheRowStatus"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExpiryTime"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheIncludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheExcludePortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtCacheSrcPort"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterLearnedMethod"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterEgressing"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterStaticPortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterBridgePortAgeTime"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsGroupFull"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesSent"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3QueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV1ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV2ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumV3ReportsRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumLeavesRcvd"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStatsCntrsNumBadFramesRcvd"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtReadBaseGroup.setStatus("current")

etsysMgmdExtWriteBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 1, 11)
)
etsysMgmdExtWriteBaseGroup.setObjects(
      *(("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigFullAction"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtConfigNumberOfGroups"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtInterfaceFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheIncludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheExcludeList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtStaticCacheRowStatus"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtDiscoveredRouterStaticPortList"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtPortFastLeaveState"),
        ("ENTERASYS-MGMD-EXT-MIB", "etsysMgmdExtProtocolIdentifier"))
)
if mibBuilder.loadTexts:
    etsysMgmdExtWriteBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysMgmdExtReadCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMgmdExtReadCompliance.setStatus(
        "current"
    )

etsysMgmdExtWriteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 71, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysMgmdExtWriteCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MGMD-EXT-MIB",
    **{"MGMDNumGroupsTc": MGMDNumGroupsTc,
       "MGMDPortModeTc": MGMDPortModeTc,
       "MGMDDiscoveredRouterModeTc": MGMDDiscoveredRouterModeTc,
       "MGMDProtocolClassTc": MGMDProtocolClassTc,
       "MGMDProtocolIdTc": MGMDProtocolIdTc,
       "etsysMgmdExtMIB": etsysMgmdExtMIB,
       "etsysMgmdExtObjects": etsysMgmdExtObjects,
       "etsysMgmdExtConfigGroup": etsysMgmdExtConfigGroup,
       "etsysMgmdExtConfigRevString": etsysMgmdExtConfigRevString,
       "etsysMgmdExtConfigFullAction": etsysMgmdExtConfigFullAction,
       "etsysMgmdExtConfigMinNumberOfGroups": etsysMgmdExtConfigMinNumberOfGroups,
       "etsysMgmdExtConfigDefaultNumberOfGroups": etsysMgmdExtConfigDefaultNumberOfGroups,
       "etsysMgmdExtConfigMaxNumberOfGroups": etsysMgmdExtConfigMaxNumberOfGroups,
       "etsysMgmdExtConfigNumberOfGroups": etsysMgmdExtConfigNumberOfGroups,
       "etsysMgmdExtInterfaceGroup": etsysMgmdExtInterfaceGroup,
       "etsysMgmdExtInterfaceTable": etsysMgmdExtInterfaceTable,
       "etsysMgmdExtInterfaceEntry": etsysMgmdExtInterfaceEntry,
       "etsysMgmdExtInterfaceApplication": etsysMgmdExtInterfaceApplication,
       "etsysMgmdExtInterfaceQueryEnableState": etsysMgmdExtInterfaceQueryEnableState,
       "etsysMgmdExtInterfaceFastLeaveState": etsysMgmdExtInterfaceFastLeaveState,
       "etsysMgmdExtInterfaceClearGroups": etsysMgmdExtInterfaceClearGroups,
       "etsysMgmdExtRtrAlertRequired": etsysMgmdExtRtrAlertRequired,
       "etsysMgmdExtStaticCacheGroup": etsysMgmdExtStaticCacheGroup,
       "etsysMgmdExtStaticCacheTable": etsysMgmdExtStaticCacheTable,
       "etsysMgmdExtStaticCacheEntry": etsysMgmdExtStaticCacheEntry,
       "etsysMgmdExtStaticCacheIPAddrType": etsysMgmdExtStaticCacheIPAddrType,
       "etsysMgmdExtStaticCacheGroupIPAddress": etsysMgmdExtStaticCacheGroupIPAddress,
       "etsysMgmdExtStaticCacheSourceIPAddress": etsysMgmdExtStaticCacheSourceIPAddress,
       "etsysMgmdExtStaticCacheIncludeList": etsysMgmdExtStaticCacheIncludeList,
       "etsysMgmdExtStaticCacheExcludeList": etsysMgmdExtStaticCacheExcludeList,
       "etsysMgmdExtStaticCacheRowStatus": etsysMgmdExtStaticCacheRowStatus,
       "etsysMgmdExtCacheGroup": etsysMgmdExtCacheGroup,
       "etsysMgmdExtCacheTable": etsysMgmdExtCacheTable,
       "etsysMgmdExtCacheEntry": etsysMgmdExtCacheEntry,
       "etsysMgmdExtCacheIPAddrType": etsysMgmdExtCacheIPAddrType,
       "etsysMgmdExtCacheGroupIPAddress": etsysMgmdExtCacheGroupIPAddress,
       "etsysMgmdExtCacheSourceIPAddress": etsysMgmdExtCacheSourceIPAddress,
       "etsysMgmdExtCacheExpiryTime": etsysMgmdExtCacheExpiryTime,
       "etsysMgmdExtCacheIncludePortList": etsysMgmdExtCacheIncludePortList,
       "etsysMgmdExtCacheExcludePortList": etsysMgmdExtCacheExcludePortList,
       "etsysMgmdExtCacheSrcPort": etsysMgmdExtCacheSrcPort,
       "etsysMgmdExtDiscoveredRouterGroup": etsysMgmdExtDiscoveredRouterGroup,
       "etsysMgmdExtDiscoveredRouterTable": etsysMgmdExtDiscoveredRouterTable,
       "etsysMgmdExtDiscoveredRouterEntry": etsysMgmdExtDiscoveredRouterEntry,
       "etsysMgmdExtDiscoveredRouterApplication": etsysMgmdExtDiscoveredRouterApplication,
       "etsysMgmdExtDiscoveredRouterLearnedMethod": etsysMgmdExtDiscoveredRouterLearnedMethod,
       "etsysMgmdExtDiscoveredRouterEgressing": etsysMgmdExtDiscoveredRouterEgressing,
       "etsysMgmdExtDiscoveredRouterStaticPortList": etsysMgmdExtDiscoveredRouterStaticPortList,
       "etsysMgmdExtDiscoveredRouterBridgePortAgeTime": etsysMgmdExtDiscoveredRouterBridgePortAgeTime,
       "etsysMgmdExtPortGroup": etsysMgmdExtPortGroup,
       "etsysMgmdExtPortTable": etsysMgmdExtPortTable,
       "etsysMgmdExtPortTableEntry": etsysMgmdExtPortTableEntry,
       "etsysMgmdExtPortMode": etsysMgmdExtPortMode,
       "etsysMgmdExtPortIPAddressType": etsysMgmdExtPortIPAddressType,
       "etsysMgmdExtPortTableGroupIPAddress": etsysMgmdExtPortTableGroupIPAddress,
       "etsysMgmdExtPortTableSourceIPAddress": etsysMgmdExtPortTableSourceIPAddress,
       "etsysMgmdExtPortTableExpireTime": etsysMgmdExtPortTableExpireTime,
       "etsysMgmdExtPortFastLeaveGroup": etsysMgmdExtPortFastLeaveGroup,
       "etsysMgmdExtPortFastLeaveTable": etsysMgmdExtPortFastLeaveTable,
       "etsysMgmdExtPortFastLeaveTableEntry": etsysMgmdExtPortFastLeaveTableEntry,
       "etsysMgmdExtPortFastLeaveState": etsysMgmdExtPortFastLeaveState,
       "etsysMgmdExtStatsCntrsGroup": etsysMgmdExtStatsCntrsGroup,
       "etsysMgmdExtStatsCntrsTable": etsysMgmdExtStatsCntrsTable,
       "etsysMgmdExtStatsCntrsEntry": etsysMgmdExtStatsCntrsEntry,
       "etsysMgmdExtStatsCntrsApplication": etsysMgmdExtStatsCntrsApplication,
       "etsysMgmdExtStatsCntrsGroupFull": etsysMgmdExtStatsCntrsGroupFull,
       "etsysMgmdExtStatsCntrsNumV1QueriesSent": etsysMgmdExtStatsCntrsNumV1QueriesSent,
       "etsysMgmdExtStatsCntrsNumV2QueriesSent": etsysMgmdExtStatsCntrsNumV2QueriesSent,
       "etsysMgmdExtStatsCntrsNumV3QueriesSent": etsysMgmdExtStatsCntrsNumV3QueriesSent,
       "etsysMgmdExtStatsCntrsNumGSQueriesSent": etsysMgmdExtStatsCntrsNumGSQueriesSent,
       "etsysMgmdExtStatsCntrsNumGAndSQueriesSent": etsysMgmdExtStatsCntrsNumGAndSQueriesSent,
       "etsysMgmdExtStatsCntrsNumV1QueriesRcvd": etsysMgmdExtStatsCntrsNumV1QueriesRcvd,
       "etsysMgmdExtStatsCntrsNumV2QueriesRcvd": etsysMgmdExtStatsCntrsNumV2QueriesRcvd,
       "etsysMgmdExtStatsCntrsNumV3QueriesRcvd": etsysMgmdExtStatsCntrsNumV3QueriesRcvd,
       "etsysMgmdExtStatsCntrsNumGSQueriesRcvd": etsysMgmdExtStatsCntrsNumGSQueriesRcvd,
       "etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd": etsysMgmdExtStatsCntrsNumGAndSQueriesRcvd,
       "etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd": etsysMgmdExtStatsCntrsNumWrongVersionQueriesRcvd,
       "etsysMgmdExtStatsCntrsNumV1ReportsRcvd": etsysMgmdExtStatsCntrsNumV1ReportsRcvd,
       "etsysMgmdExtStatsCntrsNumV2ReportsRcvd": etsysMgmdExtStatsCntrsNumV2ReportsRcvd,
       "etsysMgmdExtStatsCntrsNumV3ReportsRcvd": etsysMgmdExtStatsCntrsNumV3ReportsRcvd,
       "etsysMgmdExtStatsCntrsNumLeavesRcvd": etsysMgmdExtStatsCntrsNumLeavesRcvd,
       "etsysMgmdExtStatsCntrsNumBadFramesRcvd": etsysMgmdExtStatsCntrsNumBadFramesRcvd,
       "etsysMgmdExtStatsCntrsClear": etsysMgmdExtStatsCntrsClear,
       "etsysMgmdExtProtocolClassificationGroup": etsysMgmdExtProtocolClassificationGroup,
       "etsysMgmdExtProtocolClassificationTable": etsysMgmdExtProtocolClassificationTable,
       "etsysMgmdExtProtocolClassificationEntry": etsysMgmdExtProtocolClassificationEntry,
       "etsysMgmdExtProtocolClassification": etsysMgmdExtProtocolClassification,
       "etsysMgmdExtProtocolIdentifier": etsysMgmdExtProtocolIdentifier,
       "etsysMgmdExtConformance": etsysMgmdExtConformance,
       "etsysMgmdExtGroups": etsysMgmdExtGroups,
       "etsysMgmdExtConfigGroups": etsysMgmdExtConfigGroups,
       "etsysMgmdExtInterfaceGroups": etsysMgmdExtInterfaceGroups,
       "etsysMgmdExtStaticCacheGroups": etsysMgmdExtStaticCacheGroups,
       "etsysMgmdExtCacheGroups": etsysMgmdExtCacheGroups,
       "etsysMgmdExtDiscoveredRouterGroups": etsysMgmdExtDiscoveredRouterGroups,
       "etsysMgmdExtPortGroups": etsysMgmdExtPortGroups,
       "etsysMgmdExtPortFastLeaveGroups": etsysMgmdExtPortFastLeaveGroups,
       "etsysMgmdExtStatsCntsGroups": etsysMgmdExtStatsCntsGroups,
       "etsysMgmdExtProtocolClassificationGroups": etsysMgmdExtProtocolClassificationGroups,
       "etsysMgmdExtReadBaseGroup": etsysMgmdExtReadBaseGroup,
       "etsysMgmdExtWriteBaseGroup": etsysMgmdExtWriteBaseGroup,
       "etsysMgmdExtCompliances": etsysMgmdExtCompliances,
       "etsysMgmdExtReadCompliance": etsysMgmdExtReadCompliance,
       "etsysMgmdExtWriteCompliance": etsysMgmdExtWriteCompliance}
)
