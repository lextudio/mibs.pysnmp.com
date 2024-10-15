# SNMP MIB module (CADANT-VIRTUAL-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-VIRTUAL-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:25 2024
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

(cadBgIndex,) = mibBuilder.importSymbols(
    "CADANT-CMTS-LAYER2CMTS-MIB",
    "cadBgIndex")

(cadLayer3,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadLayer3")

(CadCpeDeviceTypes,
 InetAddressIPv4or6) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CadCpeDeviceTypes",
    "InetAddressIPv4or6")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressPrefixLength,
 InetAddressType,
 InetScopeType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetScopeType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadVirtualRouterMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3)
)
cadVirtualRouterMibModule.setRevisions(
        ("2015-05-12 00:00",
         "2014-08-18 00:00",
         "2014-08-05 00:00",
         "2014-01-15 00:00",
         "2013-12-13 00:00",
         "2013-11-26 00:00",
         "2013-08-30 00:00",
         "2013-04-16 00:00",
         "2012-04-18 00:00",
         "2012-03-20 00:00",
         "2010-08-11 00:00",
         "2010-07-02 00:00",
         "2010-05-06 00:00",
         "2009-09-17 00:00",
         "2009-09-10 00:00",
         "2009-09-03 00:00",
         "2009-08-28 00:00",
         "2008-02-09 00:00",
         "2007-12-09 00:00",
         "2007-01-18 00:00",
         "2006-11-28 00:00",
         "2006-09-25 00:00",
         "2006-07-17 00:00",
         "2005-11-14 00:00",
         "2005-04-06 00:00",
         "2004-10-27 00:00",
         "2004-03-22 00:00",
         "2004-02-09 00:00",
         "2004-01-28 00:00",
         "2003-07-21 00:00",
         "2003-07-16 00:00",
         "2003-07-01 00:00",
         "2003-06-30 00:00",
         "2003-04-07 00:00",
         "2003-03-06 00:00",
         "2002-12-16 00:00",
         "2002-11-04 00:00",
         "2002-09-20 00:00",
         "2002-08-16 00:00",
         "2002-05-21 00:00",
         "2002-05-07 00:00",
         "2001-08-18 00:00",
         "2001-07-17 00:00",
         "2001-07-13 00:00",
         "2001-07-02 00:00",
         "2001-05-25 00:00",
         "2001-05-21 00:00",
         "2001-04-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadSourceVerifyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("authoritativeDhcp", 7),
          ("dhcp", 3),
          ("internal", 1),
          ("none", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CadVirtualRouter_ObjectIdentity = ObjectIdentity
cadVirtualRouter = _CadVirtualRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1)
)
_CadVrNameTable_Object = MibTable
cadVrNameTable = _CadVrNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cadVrNameTable.setStatus("current")
_CadVrNameEntry_Object = MibTableRow
cadVrNameEntry = _CadVrNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 1, 1)
)
cadVrNameEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrName"),
)
if mibBuilder.loadTexts:
    cadVrNameEntry.setStatus("current")


class _CadVrNameVrIndex_Type(Integer32):
    """Custom type cadVrNameVrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_CadVrNameVrIndex_Type.__name__ = "Integer32"
_CadVrNameVrIndex_Object = MibTableColumn
cadVrNameVrIndex = _CadVrNameVrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 1, 1, 1),
    _CadVrNameVrIndex_Type()
)
cadVrNameVrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrNameVrIndex.setStatus("current")
_CadVrNameRowStatus_Type = RowStatus
_CadVrNameRowStatus_Object = MibTableColumn
cadVrNameRowStatus = _CadVrNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 1, 1, 2),
    _CadVrNameRowStatus_Type()
)
cadVrNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrNameRowStatus.setStatus("current")
_CadVrTable_Object = MibTable
cadVrTable = _CadVrTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cadVrTable.setStatus("current")
_CadVrEntry_Object = MibTableRow
cadVrEntry = _CadVrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1)
)
cadVrEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrIndex"),
)
if mibBuilder.loadTexts:
    cadVrEntry.setStatus("current")


class _CadVrIndex_Type(Integer32):
    """Custom type cadVrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_CadVrIndex_Type.__name__ = "Integer32"
_CadVrIndex_Object = MibTableColumn
cadVrIndex = _CadVrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 1),
    _CadVrIndex_Type()
)
cadVrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrIndex.setStatus("current")


class _CadVrName_Type(DisplayString):
    """Custom type cadVrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadVrName_Type.__name__ = "DisplayString"
_CadVrName_Object = MibTableColumn
cadVrName = _CadVrName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 2),
    _CadVrName_Type()
)
cadVrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrName.setStatus("current")


class _CadVrOspfEnabled_Type(TruthValue):
    """Custom type cadVrOspfEnabled based on TruthValue"""


_CadVrOspfEnabled_Object = MibTableColumn
cadVrOspfEnabled = _CadVrOspfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 3),
    _CadVrOspfEnabled_Type()
)
cadVrOspfEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrOspfEnabled.setStatus("obsolete")


class _CadVrRipEnabled_Type(TruthValue):
    """Custom type cadVrRipEnabled based on TruthValue"""


_CadVrRipEnabled_Object = MibTableColumn
cadVrRipEnabled = _CadVrRipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 4),
    _CadVrRipEnabled_Type()
)
cadVrRipEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrRipEnabled.setStatus("current")
_CadVrRowStatus_Type = RowStatus
_CadVrRowStatus_Object = MibTableColumn
cadVrRowStatus = _CadVrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 5),
    _CadVrRowStatus_Type()
)
cadVrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrRowStatus.setStatus("current")


class _CadVrScmAccessEnabled_Type(TruthValue):
    """Custom type cadVrScmAccessEnabled based on TruthValue"""


_CadVrScmAccessEnabled_Object = MibTableColumn
cadVrScmAccessEnabled = _CadVrScmAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 6),
    _CadVrScmAccessEnabled_Type()
)
cadVrScmAccessEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrScmAccessEnabled.setStatus("current")


class _CadVrScmAccessDirectedBroadcastEnabled_Type(TruthValue):
    """Custom type cadVrScmAccessDirectedBroadcastEnabled based on TruthValue"""


_CadVrScmAccessDirectedBroadcastEnabled_Object = MibTableColumn
cadVrScmAccessDirectedBroadcastEnabled = _CadVrScmAccessDirectedBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 7),
    _CadVrScmAccessDirectedBroadcastEnabled_Type()
)
cadVrScmAccessDirectedBroadcastEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrScmAccessDirectedBroadcastEnabled.setStatus("current")


class _CadVrNullInterface_Type(TruthValue):
    """Custom type cadVrNullInterface based on TruthValue"""


_CadVrNullInterface_Object = MibTableColumn
cadVrNullInterface = _CadVrNullInterface_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 8),
    _CadVrNullInterface_Type()
)
cadVrNullInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrNullInterface.setStatus("current")


class _CadVrICMPTimeExceededEnabled_Type(TruthValue):
    """Custom type cadVrICMPTimeExceededEnabled based on TruthValue"""


_CadVrICMPTimeExceededEnabled_Object = MibTableColumn
cadVrICMPTimeExceededEnabled = _CadVrICMPTimeExceededEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 9),
    _CadVrICMPTimeExceededEnabled_Type()
)
cadVrICMPTimeExceededEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrICMPTimeExceededEnabled.setStatus("current")


class _CadVrOspfGracefulRestartEnabled_Type(TruthValue):
    """Custom type cadVrOspfGracefulRestartEnabled based on TruthValue"""


_CadVrOspfGracefulRestartEnabled_Object = MibTableColumn
cadVrOspfGracefulRestartEnabled = _CadVrOspfGracefulRestartEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 10),
    _CadVrOspfGracefulRestartEnabled_Type()
)
cadVrOspfGracefulRestartEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrOspfGracefulRestartEnabled.setStatus("current")


class _CadVrIPv6ReflectionEnabled_Type(TruthValue):
    """Custom type cadVrIPv6ReflectionEnabled based on TruthValue"""


_CadVrIPv6ReflectionEnabled_Object = MibTableColumn
cadVrIPv6ReflectionEnabled = _CadVrIPv6ReflectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 11),
    _CadVrIPv6ReflectionEnabled_Type()
)
cadVrIPv6ReflectionEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrIPv6ReflectionEnabled.setStatus("current")


class _CadVrICMPv6TimeExceededEnabled_Type(TruthValue):
    """Custom type cadVrICMPv6TimeExceededEnabled based on TruthValue"""


_CadVrICMPv6TimeExceededEnabled_Object = MibTableColumn
cadVrICMPv6TimeExceededEnabled = _CadVrICMPv6TimeExceededEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 12),
    _CadVrICMPv6TimeExceededEnabled_Type()
)
cadVrICMPv6TimeExceededEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrICMPv6TimeExceededEnabled.setStatus("current")


class _CadVrNullInterfacev6_Type(TruthValue):
    """Custom type cadVrNullInterfacev6 based on TruthValue"""


_CadVrNullInterfacev6_Object = MibTableColumn
cadVrNullInterfacev6 = _CadVrNullInterfacev6_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 13),
    _CadVrNullInterfacev6_Type()
)
cadVrNullInterfacev6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrNullInterfacev6.setStatus("current")


class _CadVrPhpEnabled_Type(TruthValue):
    """Custom type cadVrPhpEnabled based on TruthValue"""


_CadVrPhpEnabled_Object = MibTableColumn
cadVrPhpEnabled = _CadVrPhpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 14),
    _CadVrPhpEnabled_Type()
)
cadVrPhpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrPhpEnabled.setStatus("current")


class _CadVrAutoImportEnabled_Type(TruthValue):
    """Custom type cadVrAutoImportEnabled based on TruthValue"""


_CadVrAutoImportEnabled_Object = MibTableColumn
cadVrAutoImportEnabled = _CadVrAutoImportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 2, 1, 15),
    _CadVrAutoImportEnabled_Type()
)
cadVrAutoImportEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAutoImportEnabled.setStatus("current")
_CadVrInterfaceTable_Object = MibTable
cadVrInterfaceTable = _CadVrInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cadVrInterfaceTable.setStatus("current")
_CadVrInterfaceEntry_Object = MibTableRow
cadVrInterfaceEntry = _CadVrInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1)
)
cadVrInterfaceEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceSubifIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadBgIndex"),
)
if mibBuilder.loadTexts:
    cadVrInterfaceEntry.setStatus("current")
_CadVrInterfaceIfIndex_Type = InterfaceIndex
_CadVrInterfaceIfIndex_Object = MibTableColumn
cadVrInterfaceIfIndex = _CadVrInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 1),
    _CadVrInterfaceIfIndex_Type()
)
cadVrInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrInterfaceIfIndex.setStatus("current")


class _CadVrInterfaceIpAddr_Type(InetAddressIPv4or6):
    """Custom type cadVrInterfaceIpAddr based on InetAddressIPv4or6"""
    defaultHexValue = ""


_CadVrInterfaceIpAddr_Object = MibTableColumn
cadVrInterfaceIpAddr = _CadVrInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 2),
    _CadVrInterfaceIpAddr_Type()
)
cadVrInterfaceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIpAddr.setStatus("current")


class _CadVrInterfaceIpMask_Type(InetAddressIPv4or6):
    """Custom type cadVrInterfaceIpMask based on InetAddressIPv4or6"""
    defaultHexValue = ""


_CadVrInterfaceIpMask_Object = MibTableColumn
cadVrInterfaceIpMask = _CadVrInterfaceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 3),
    _CadVrInterfaceIpMask_Type()
)
cadVrInterfaceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIpMask.setStatus("current")


class _CadVrInterfaceDHCPEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceDHCPEnabled based on TruthValue"""


_CadVrInterfaceDHCPEnabled_Object = MibTableColumn
cadVrInterfaceDHCPEnabled = _CadVrInterfaceDHCPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 4),
    _CadVrInterfaceDHCPEnabled_Type()
)
cadVrInterfaceDHCPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrInterfaceDHCPEnabled.setStatus("current")


class _CadVrInterfaceFARPEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceFARPEnabled based on TruthValue"""


_CadVrInterfaceFARPEnabled_Object = MibTableColumn
cadVrInterfaceFARPEnabled = _CadVrInterfaceFARPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 5),
    _CadVrInterfaceFARPEnabled_Type()
)
cadVrInterfaceFARPEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceFARPEnabled.setStatus("current")


class _CadVrInterfaceRipEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceRipEnabled based on TruthValue"""


_CadVrInterfaceRipEnabled_Object = MibTableColumn
cadVrInterfaceRipEnabled = _CadVrInterfaceRipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 6),
    _CadVrInterfaceRipEnabled_Type()
)
cadVrInterfaceRipEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceRipEnabled.setStatus("obsolete")


class _CadVrInterfaceRipPassive_Type(TruthValue):
    """Custom type cadVrInterfaceRipPassive based on TruthValue"""


_CadVrInterfaceRipPassive_Object = MibTableColumn
cadVrInterfaceRipPassive = _CadVrInterfaceRipPassive_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 7),
    _CadVrInterfaceRipPassive_Type()
)
cadVrInterfaceRipPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceRipPassive.setStatus("obsolete")


class _CadVrInterfaceIGMPEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceIGMPEnabled based on TruthValue"""


_CadVrInterfaceIGMPEnabled_Object = MibTableColumn
cadVrInterfaceIGMPEnabled = _CadVrInterfaceIGMPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 8),
    _CadVrInterfaceIGMPEnabled_Type()
)
cadVrInterfaceIGMPEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIGMPEnabled.setStatus("obsolete")


class _CadVrInterfaceIRDPEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceIRDPEnabled based on TruthValue"""


_CadVrInterfaceIRDPEnabled_Object = MibTableColumn
cadVrInterfaceIRDPEnabled = _CadVrInterfaceIRDPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 9),
    _CadVrInterfaceIRDPEnabled_Type()
)
cadVrInterfaceIRDPEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIRDPEnabled.setStatus("obsolete")
_CadVrInterfaceRowStatus_Type = RowStatus
_CadVrInterfaceRowStatus_Object = MibTableColumn
cadVrInterfaceRowStatus = _CadVrInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 10),
    _CadVrInterfaceRowStatus_Type()
)
cadVrInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceRowStatus.setStatus("current")


class _CadVrInterfaceDHCPPolicyEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceDHCPPolicyEnabled based on TruthValue"""


_CadVrInterfaceDHCPPolicyEnabled_Object = MibTableColumn
cadVrInterfaceDHCPPolicyEnabled = _CadVrInterfaceDHCPPolicyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 11),
    _CadVrInterfaceDHCPPolicyEnabled_Type()
)
cadVrInterfaceDHCPPolicyEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceDHCPPolicyEnabled.setStatus("current")


class _CadVrInterfaceDirectedBcastEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceDirectedBcastEnabled based on TruthValue"""


_CadVrInterfaceDirectedBcastEnabled_Object = MibTableColumn
cadVrInterfaceDirectedBcastEnabled = _CadVrInterfaceDirectedBcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 12),
    _CadVrInterfaceDirectedBcastEnabled_Type()
)
cadVrInterfaceDirectedBcastEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceDirectedBcastEnabled.setStatus("current")


class _CadVrInterfaceSourceVerify_Type(CadSourceVerifyType):
    """Custom type cadVrInterfaceSourceVerify based on CadSourceVerifyType"""


_CadVrInterfaceSourceVerify_Object = MibTableColumn
cadVrInterfaceSourceVerify = _CadVrInterfaceSourceVerify_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 13),
    _CadVrInterfaceSourceVerify_Type()
)
cadVrInterfaceSourceVerify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceSourceVerify.setStatus("current")


class _CadVrInterfaceSubFilterDownDefault_Type(Integer32):
    """Custom type cadVrInterfaceSubFilterDownDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfaceSubFilterDownDefault_Type.__name__ = "Integer32"
_CadVrInterfaceSubFilterDownDefault_Object = MibTableColumn
cadVrInterfaceSubFilterDownDefault = _CadVrInterfaceSubFilterDownDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 14),
    _CadVrInterfaceSubFilterDownDefault_Type()
)
cadVrInterfaceSubFilterDownDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceSubFilterDownDefault.setStatus("current")


class _CadVrInterfaceSubFilterUpDefault_Type(Integer32):
    """Custom type cadVrInterfaceSubFilterUpDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfaceSubFilterUpDefault_Type.__name__ = "Integer32"
_CadVrInterfaceSubFilterUpDefault_Object = MibTableColumn
cadVrInterfaceSubFilterUpDefault = _CadVrInterfaceSubFilterUpDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 15),
    _CadVrInterfaceSubFilterUpDefault_Type()
)
cadVrInterfaceSubFilterUpDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceSubFilterUpDefault.setStatus("current")


class _CadVrInterfaceCmFilterDownDefault_Type(Integer32):
    """Custom type cadVrInterfaceCmFilterDownDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfaceCmFilterDownDefault_Type.__name__ = "Integer32"
_CadVrInterfaceCmFilterDownDefault_Object = MibTableColumn
cadVrInterfaceCmFilterDownDefault = _CadVrInterfaceCmFilterDownDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 16),
    _CadVrInterfaceCmFilterDownDefault_Type()
)
cadVrInterfaceCmFilterDownDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceCmFilterDownDefault.setStatus("current")


class _CadVrInterfaceCmFilterUpDefault_Type(Integer32):
    """Custom type cadVrInterfaceCmFilterUpDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfaceCmFilterUpDefault_Type.__name__ = "Integer32"
_CadVrInterfaceCmFilterUpDefault_Object = MibTableColumn
cadVrInterfaceCmFilterUpDefault = _CadVrInterfaceCmFilterUpDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 17),
    _CadVrInterfaceCmFilterUpDefault_Type()
)
cadVrInterfaceCmFilterUpDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceCmFilterUpDefault.setStatus("current")


class _CadVrInterfaceSubifIndex_Type(Integer32):
    """Custom type cadVrInterfaceSubifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadVrInterfaceSubifIndex_Type.__name__ = "Integer32"
_CadVrInterfaceSubifIndex_Object = MibTableColumn
cadVrInterfaceSubifIndex = _CadVrInterfaceSubifIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 18),
    _CadVrInterfaceSubifIndex_Type()
)
cadVrInterfaceSubifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrInterfaceSubifIndex.setStatus("current")


class _CadVrInterfaceVrIndex_Type(Integer32):
    """Custom type cadVrInterfaceVrIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_CadVrInterfaceVrIndex_Type.__name__ = "Integer32"
_CadVrInterfaceVrIndex_Object = MibTableColumn
cadVrInterfaceVrIndex = _CadVrInterfaceVrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 19),
    _CadVrInterfaceVrIndex_Type()
)
cadVrInterfaceVrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceVrIndex.setStatus("current")


class _CadVrInterfaceIsLoopback_Type(TruthValue):
    """Custom type cadVrInterfaceIsLoopback based on TruthValue"""


_CadVrInterfaceIsLoopback_Object = MibTableColumn
cadVrInterfaceIsLoopback = _CadVrInterfaceIsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 20),
    _CadVrInterfaceIsLoopback_Type()
)
cadVrInterfaceIsLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrInterfaceIsLoopback.setStatus("current")


class _CadVrInterfaceRestrictedFARPEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceRestrictedFARPEnabled based on TruthValue"""


_CadVrInterfaceRestrictedFARPEnabled_Object = MibTableColumn
cadVrInterfaceRestrictedFARPEnabled = _CadVrInterfaceRestrictedFARPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 21),
    _CadVrInterfaceRestrictedFARPEnabled_Type()
)
cadVrInterfaceRestrictedFARPEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceRestrictedFARPEnabled.setStatus("current")


class _CadVrInterfaceAdminStat_Type(Integer32):
    """Custom type cadVrInterfaceAdminStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CadVrInterfaceAdminStat_Type.__name__ = "Integer32"
_CadVrInterfaceAdminStat_Object = MibTableColumn
cadVrInterfaceAdminStat = _CadVrInterfaceAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 22),
    _CadVrInterfaceAdminStat_Type()
)
cadVrInterfaceAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceAdminStat.setStatus("current")


class _CadVrInterfaceIcmpUnreachablesEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceIcmpUnreachablesEnabled based on TruthValue"""


_CadVrInterfaceIcmpUnreachablesEnabled_Object = MibTableColumn
cadVrInterfaceIcmpUnreachablesEnabled = _CadVrInterfaceIcmpUnreachablesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 23),
    _CadVrInterfaceIcmpUnreachablesEnabled_Type()
)
cadVrInterfaceIcmpUnreachablesEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIcmpUnreachablesEnabled.setStatus("current")


class _CadVrInterfaceDescription_Type(DisplayString):
    """Custom type cadVrInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadVrInterfaceDescription_Type.__name__ = "DisplayString"
_CadVrInterfaceDescription_Object = MibTableColumn
cadVrInterfaceDescription = _CadVrInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 24),
    _CadVrInterfaceDescription_Type()
)
cadVrInterfaceDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceDescription.setStatus("current")


class _CadVrInterfaceEncapType_Type(IANAifType):
    """Custom type cadVrInterfaceEncapType based on IANAifType"""


_CadVrInterfaceEncapType_Object = MibTableColumn
cadVrInterfaceEncapType = _CadVrInterfaceEncapType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 25),
    _CadVrInterfaceEncapType_Type()
)
cadVrInterfaceEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceEncapType.setStatus("current")


class _CadVrInterfaceVlanId_Type(Integer32):
    """Custom type cadVrInterfaceVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CadVrInterfaceVlanId_Type.__name__ = "Integer32"
_CadVrInterfaceVlanId_Object = MibTableColumn
cadVrInterfaceVlanId = _CadVrInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 26),
    _CadVrInterfaceVlanId_Type()
)
cadVrInterfaceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceVlanId.setStatus("current")


class _CadVrInterfacePriority_Type(Integer32):
    """Custom type cadVrInterfacePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CadVrInterfacePriority_Type.__name__ = "Integer32"
_CadVrInterfacePriority_Object = MibTableColumn
cadVrInterfacePriority = _CadVrInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 27),
    _CadVrInterfacePriority_Type()
)
cadVrInterfacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfacePriority.setStatus("current")


class _CadVrInterfaceScmAccess_Type(TruthValue):
    """Custom type cadVrInterfaceScmAccess based on TruthValue"""


_CadVrInterfaceScmAccess_Object = MibTableColumn
cadVrInterfaceScmAccess = _CadVrInterfaceScmAccess_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 28),
    _CadVrInterfaceScmAccess_Type()
)
cadVrInterfaceScmAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceScmAccess.setStatus("current")


class _CadVrInterfaceIpAddrType_Type(InetAddressType):
    """Custom type cadVrInterfaceIpAddrType based on InetAddressType"""


_CadVrInterfaceIpAddrType_Object = MibTableColumn
cadVrInterfaceIpAddrType = _CadVrInterfaceIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 29),
    _CadVrInterfaceIpAddrType_Type()
)
cadVrInterfaceIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIpAddrType.setStatus("current")


class _CadVrInterfaceIpPrefixLength_Type(Integer32):
    """Custom type cadVrInterfaceIpPrefixLength based on Integer32"""
    defaultValue = 0


_CadVrInterfaceIpPrefixLength_Object = MibTableColumn
cadVrInterfaceIpPrefixLength = _CadVrInterfaceIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 30),
    _CadVrInterfaceIpPrefixLength_Type()
)
cadVrInterfaceIpPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIpPrefixLength.setStatus("current")


class _CadVrInterfaceIpScopeType_Type(InetScopeType):
    """Custom type cadVrInterfaceIpScopeType based on InetScopeType"""


_CadVrInterfaceIpScopeType_Object = MibTableColumn
cadVrInterfaceIpScopeType = _CadVrInterfaceIpScopeType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 31),
    _CadVrInterfaceIpScopeType_Type()
)
cadVrInterfaceIpScopeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIpScopeType.setStatus("current")


class _CadVrInterfaceIpv6Addr_Type(InetAddressIPv4or6):
    """Custom type cadVrInterfaceIpv6Addr based on InetAddressIPv4or6"""
    defaultHexValue = ""


_CadVrInterfaceIpv6Addr_Object = MibTableColumn
cadVrInterfaceIpv6Addr = _CadVrInterfaceIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 32),
    _CadVrInterfaceIpv6Addr_Type()
)
cadVrInterfaceIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIpv6Addr.setStatus("current")


class _CadVrInterfaceIpv6PrefixLength_Type(Integer32):
    """Custom type cadVrInterfaceIpv6PrefixLength based on Integer32"""
    defaultValue = 0


_CadVrInterfaceIpv6PrefixLength_Object = MibTableColumn
cadVrInterfaceIpv6PrefixLength = _CadVrInterfaceIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 33),
    _CadVrInterfaceIpv6PrefixLength_Type()
)
cadVrInterfaceIpv6PrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIpv6PrefixLength.setStatus("current")


class _CadVrInterfaceDADAttempts_Type(Unsigned32):
    """Custom type cadVrInterfaceDADAttempts based on Unsigned32"""
    defaultValue = 1


_CadVrInterfaceDADAttempts_Object = MibTableColumn
cadVrInterfaceDADAttempts = _CadVrInterfaceDADAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 34),
    _CadVrInterfaceDADAttempts_Type()
)
cadVrInterfaceDADAttempts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceDADAttempts.setStatus("current")


class _CadVrInterfaceIpv6Forwarding_Type(Integer32):
    """Custom type cadVrInterfaceIpv6Forwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notforwarding", 2))
    )


_CadVrInterfaceIpv6Forwarding_Type.__name__ = "Integer32"
_CadVrInterfaceIpv6Forwarding_Object = MibTableColumn
cadVrInterfaceIpv6Forwarding = _CadVrInterfaceIpv6Forwarding_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 35),
    _CadVrInterfaceIpv6Forwarding_Type()
)
cadVrInterfaceIpv6Forwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrInterfaceIpv6Forwarding.setStatus("current")


class _CadVrInterfacePsFilterDownDefault_Type(Integer32):
    """Custom type cadVrInterfacePsFilterDownDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfacePsFilterDownDefault_Type.__name__ = "Integer32"
_CadVrInterfacePsFilterDownDefault_Object = MibTableColumn
cadVrInterfacePsFilterDownDefault = _CadVrInterfacePsFilterDownDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 36),
    _CadVrInterfacePsFilterDownDefault_Type()
)
cadVrInterfacePsFilterDownDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfacePsFilterDownDefault.setStatus("current")


class _CadVrInterfacePsFilterUpDefault_Type(Integer32):
    """Custom type cadVrInterfacePsFilterUpDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfacePsFilterUpDefault_Type.__name__ = "Integer32"
_CadVrInterfacePsFilterUpDefault_Object = MibTableColumn
cadVrInterfacePsFilterUpDefault = _CadVrInterfacePsFilterUpDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 37),
    _CadVrInterfacePsFilterUpDefault_Type()
)
cadVrInterfacePsFilterUpDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfacePsFilterUpDefault.setStatus("current")


class _CadVrInterfaceMtaFilterDownDefault_Type(Integer32):
    """Custom type cadVrInterfaceMtaFilterDownDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfaceMtaFilterDownDefault_Type.__name__ = "Integer32"
_CadVrInterfaceMtaFilterDownDefault_Object = MibTableColumn
cadVrInterfaceMtaFilterDownDefault = _CadVrInterfaceMtaFilterDownDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 38),
    _CadVrInterfaceMtaFilterDownDefault_Type()
)
cadVrInterfaceMtaFilterDownDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceMtaFilterDownDefault.setStatus("current")


class _CadVrInterfaceMtaFilterUpDefault_Type(Integer32):
    """Custom type cadVrInterfaceMtaFilterUpDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfaceMtaFilterUpDefault_Type.__name__ = "Integer32"
_CadVrInterfaceMtaFilterUpDefault_Object = MibTableColumn
cadVrInterfaceMtaFilterUpDefault = _CadVrInterfaceMtaFilterUpDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 39),
    _CadVrInterfaceMtaFilterUpDefault_Type()
)
cadVrInterfaceMtaFilterUpDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceMtaFilterUpDefault.setStatus("current")


class _CadVrInterfaceStbFilterDownDefault_Type(Integer32):
    """Custom type cadVrInterfaceStbFilterDownDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfaceStbFilterDownDefault_Type.__name__ = "Integer32"
_CadVrInterfaceStbFilterDownDefault_Object = MibTableColumn
cadVrInterfaceStbFilterDownDefault = _CadVrInterfaceStbFilterDownDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 40),
    _CadVrInterfaceStbFilterDownDefault_Type()
)
cadVrInterfaceStbFilterDownDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceStbFilterDownDefault.setStatus("current")


class _CadVrInterfaceStbFilterUpDefault_Type(Integer32):
    """Custom type cadVrInterfaceStbFilterUpDefault based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadVrInterfaceStbFilterUpDefault_Type.__name__ = "Integer32"
_CadVrInterfaceStbFilterUpDefault_Object = MibTableColumn
cadVrInterfaceStbFilterUpDefault = _CadVrInterfaceStbFilterUpDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 41),
    _CadVrInterfaceStbFilterUpDefault_Type()
)
cadVrInterfaceStbFilterUpDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceStbFilterUpDefault.setStatus("current")


class _CadVrInterfaceIcmpv6UnreachablesEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceIcmpv6UnreachablesEnabled based on TruthValue"""


_CadVrInterfaceIcmpv6UnreachablesEnabled_Object = MibTableColumn
cadVrInterfaceIcmpv6UnreachablesEnabled = _CadVrInterfaceIcmpv6UnreachablesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 46),
    _CadVrInterfaceIcmpv6UnreachablesEnabled_Type()
)
cadVrInterfaceIcmpv6UnreachablesEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIcmpv6UnreachablesEnabled.setStatus("current")


class _CadVrInterfaceIcmpv6TooBigEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceIcmpv6TooBigEnabled based on TruthValue"""


_CadVrInterfaceIcmpv6TooBigEnabled_Object = MibTableColumn
cadVrInterfaceIcmpv6TooBigEnabled = _CadVrInterfaceIcmpv6TooBigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 47),
    _CadVrInterfaceIcmpv6TooBigEnabled_Type()
)
cadVrInterfaceIcmpv6TooBigEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIcmpv6TooBigEnabled.setStatus("current")


class _CadVrInterfaceIcmpv6ParameterProblemEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceIcmpv6ParameterProblemEnabled based on TruthValue"""


_CadVrInterfaceIcmpv6ParameterProblemEnabled_Object = MibTableColumn
cadVrInterfaceIcmpv6ParameterProblemEnabled = _CadVrInterfaceIcmpv6ParameterProblemEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 48),
    _CadVrInterfaceIcmpv6ParameterProblemEnabled_Type()
)
cadVrInterfaceIcmpv6ParameterProblemEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIcmpv6ParameterProblemEnabled.setStatus("current")


class _CadVrInterfacePdRiEnabled_Type(TruthValue):
    """Custom type cadVrInterfacePdRiEnabled based on TruthValue"""


_CadVrInterfacePdRiEnabled_Object = MibTableColumn
cadVrInterfacePdRiEnabled = _CadVrInterfacePdRiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 49),
    _CadVrInterfacePdRiEnabled_Type()
)
cadVrInterfacePdRiEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfacePdRiEnabled.setStatus("current")


class _CadVrInterfacePolicyRouteMap_Type(Integer32):
    """Custom type cadVrInterfacePolicyRouteMap based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CadVrInterfacePolicyRouteMap_Type.__name__ = "Integer32"
_CadVrInterfacePolicyRouteMap_Object = MibTableColumn
cadVrInterfacePolicyRouteMap = _CadVrInterfacePolicyRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 50),
    _CadVrInterfacePolicyRouteMap_Type()
)
cadVrInterfacePolicyRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfacePolicyRouteMap.setStatus("current")


class _CadVrInterfaceMplsEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceMplsEnabled based on TruthValue"""


_CadVrInterfaceMplsEnabled_Object = MibTableColumn
cadVrInterfaceMplsEnabled = _CadVrInterfaceMplsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 51),
    _CadVrInterfaceMplsEnabled_Type()
)
cadVrInterfaceMplsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceMplsEnabled.setStatus("obsolete")


class _CadVrInterfaceLdpEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceLdpEnabled based on TruthValue"""


_CadVrInterfaceLdpEnabled_Object = MibTableColumn
cadVrInterfaceLdpEnabled = _CadVrInterfaceLdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 52),
    _CadVrInterfaceLdpEnabled_Type()
)
cadVrInterfaceLdpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceLdpEnabled.setStatus("obsolete")


class _CadVrInterfaceGratuitousArpEnabled_Type(TruthValue):
    """Custom type cadVrInterfaceGratuitousArpEnabled based on TruthValue"""


_CadVrInterfaceGratuitousArpEnabled_Object = MibTableColumn
cadVrInterfaceGratuitousArpEnabled = _CadVrInterfaceGratuitousArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 53),
    _CadVrInterfaceGratuitousArpEnabled_Type()
)
cadVrInterfaceGratuitousArpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceGratuitousArpEnabled.setStatus("current")


class _CadVrInterfaceIsSdv_Type(TruthValue):
    """Custom type cadVrInterfaceIsSdv based on TruthValue"""


_CadVrInterfaceIsSdv_Object = MibTableColumn
cadVrInterfaceIsSdv = _CadVrInterfaceIsSdv_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 3, 1, 54),
    _CadVrInterfaceIsSdv_Type()
)
cadVrInterfaceIsSdv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrInterfaceIsSdv.setStatus("current")
_CadVrSecondaryIpAddrTable_Object = MibTable
cadVrSecondaryIpAddrTable = _CadVrSecondaryIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cadVrSecondaryIpAddrTable.setStatus("current")
_CadVrSecondaryIpAddrEntry_Object = MibTableRow
cadVrSecondaryIpAddrEntry = _CadVrSecondaryIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 4, 1)
)
cadVrSecondaryIpAddrEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceSubifIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadBgIndex"),
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceIpAddr"),
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrSecondaryIpMask"),
)
if mibBuilder.loadTexts:
    cadVrSecondaryIpAddrEntry.setStatus("current")
_CadVrSecondaryIpMask_Type = InetAddressIPv4or6
_CadVrSecondaryIpMask_Object = MibTableColumn
cadVrSecondaryIpMask = _CadVrSecondaryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 4, 1, 1),
    _CadVrSecondaryIpMask_Type()
)
cadVrSecondaryIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrSecondaryIpMask.setStatus("current")
_CadVrSecondaryIpAddrRowStatus_Type = RowStatus
_CadVrSecondaryIpAddrRowStatus_Object = MibTableColumn
cadVrSecondaryIpAddrRowStatus = _CadVrSecondaryIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 4, 1, 2),
    _CadVrSecondaryIpAddrRowStatus_Type()
)
cadVrSecondaryIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrSecondaryIpAddrRowStatus.setStatus("current")


class _CadVrSecondaryIpAddrDHCPPolicyEnabled_Type(TruthValue):
    """Custom type cadVrSecondaryIpAddrDHCPPolicyEnabled based on TruthValue"""


_CadVrSecondaryIpAddrDHCPPolicyEnabled_Object = MibTableColumn
cadVrSecondaryIpAddrDHCPPolicyEnabled = _CadVrSecondaryIpAddrDHCPPolicyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 4, 1, 4),
    _CadVrSecondaryIpAddrDHCPPolicyEnabled_Type()
)
cadVrSecondaryIpAddrDHCPPolicyEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrSecondaryIpAddrDHCPPolicyEnabled.setStatus("deprecated")


class _CadVrSecondaryIpPrefixLength_Type(Integer32):
    """Custom type cadVrSecondaryIpPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CadVrSecondaryIpPrefixLength_Type.__name__ = "Integer32"
_CadVrSecondaryIpPrefixLength_Object = MibTableColumn
cadVrSecondaryIpPrefixLength = _CadVrSecondaryIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 4, 1, 5),
    _CadVrSecondaryIpPrefixLength_Type()
)
cadVrSecondaryIpPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrSecondaryIpPrefixLength.setStatus("current")


class _CadVrSecondaryIpAddrType_Type(InetAddressType):
    """Custom type cadVrSecondaryIpAddrType based on InetAddressType"""


_CadVrSecondaryIpAddrType_Object = MibTableColumn
cadVrSecondaryIpAddrType = _CadVrSecondaryIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 4, 1, 6),
    _CadVrSecondaryIpAddrType_Type()
)
cadVrSecondaryIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrSecondaryIpAddrType.setStatus("current")


class _CadVrSecondaryIpScopeType_Type(InetScopeType):
    """Custom type cadVrSecondaryIpScopeType based on InetScopeType"""


_CadVrSecondaryIpScopeType_Object = MibTableColumn
cadVrSecondaryIpScopeType = _CadVrSecondaryIpScopeType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 4, 1, 7),
    _CadVrSecondaryIpScopeType_Type()
)
cadVrSecondaryIpScopeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrSecondaryIpScopeType.setStatus("current")


class _CadVrSecondaryIpAddrDHCPGiaddr_Type(CadCpeDeviceTypes):
    """Custom type cadVrSecondaryIpAddrDHCPGiaddr based on CadCpeDeviceTypes"""
    defaultBinValue = "0"


_CadVrSecondaryIpAddrDHCPGiaddr_Object = MibTableColumn
cadVrSecondaryIpAddrDHCPGiaddr = _CadVrSecondaryIpAddrDHCPGiaddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 4, 1, 8),
    _CadVrSecondaryIpAddrDHCPGiaddr_Type()
)
cadVrSecondaryIpAddrDHCPGiaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrSecondaryIpAddrDHCPGiaddr.setStatus("current")
_CadVrStatusTable_Object = MibTable
cadVrStatusTable = _CadVrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cadVrStatusTable.setStatus("current")
_CadVrStatusEntry_Object = MibTableRow
cadVrStatusEntry = _CadVrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1)
)
cadVrStatusEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrStatusVrIndex"),
)
if mibBuilder.loadTexts:
    cadVrStatusEntry.setStatus("current")


class _CadVrStatusVrIndex_Type(Integer32):
    """Custom type cadVrStatusVrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_CadVrStatusVrIndex_Type.__name__ = "Integer32"
_CadVrStatusVrIndex_Object = MibTableColumn
cadVrStatusVrIndex = _CadVrStatusVrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 1),
    _CadVrStatusVrIndex_Type()
)
cadVrStatusVrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrStatusVrIndex.setStatus("current")
_CadVrStatusNumLocalRoutes_Type = Gauge32
_CadVrStatusNumLocalRoutes_Object = MibTableColumn
cadVrStatusNumLocalRoutes = _CadVrStatusNumLocalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 2),
    _CadVrStatusNumLocalRoutes_Type()
)
cadVrStatusNumLocalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumLocalRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumLocalRoutes.setUnits("routes")
_CadVrStatusNumNetmgmtRoutes_Type = Gauge32
_CadVrStatusNumNetmgmtRoutes_Object = MibTableColumn
cadVrStatusNumNetmgmtRoutes = _CadVrStatusNumNetmgmtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 3),
    _CadVrStatusNumNetmgmtRoutes_Type()
)
cadVrStatusNumNetmgmtRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumNetmgmtRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumNetmgmtRoutes.setUnits("routes")
_CadVrStatusNumRipRoutes_Type = Gauge32
_CadVrStatusNumRipRoutes_Object = MibTableColumn
cadVrStatusNumRipRoutes = _CadVrStatusNumRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 4),
    _CadVrStatusNumRipRoutes_Type()
)
cadVrStatusNumRipRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumRipRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumRipRoutes.setUnits("routes")
_CadVrStatusNumIsisInternal1Routes_Type = Gauge32
_CadVrStatusNumIsisInternal1Routes_Object = MibTableColumn
cadVrStatusNumIsisInternal1Routes = _CadVrStatusNumIsisInternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 5),
    _CadVrStatusNumIsisInternal1Routes_Type()
)
cadVrStatusNumIsisInternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIsisInternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIsisInternal1Routes.setUnits("routes")
_CadVrStatusNumIsisInternal2Routes_Type = Gauge32
_CadVrStatusNumIsisInternal2Routes_Object = MibTableColumn
cadVrStatusNumIsisInternal2Routes = _CadVrStatusNumIsisInternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 6),
    _CadVrStatusNumIsisInternal2Routes_Type()
)
cadVrStatusNumIsisInternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIsisInternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIsisInternal2Routes.setUnits("routes")
_CadVrStatusNumIsisExternal1Routes_Type = Gauge32
_CadVrStatusNumIsisExternal1Routes_Object = MibTableColumn
cadVrStatusNumIsisExternal1Routes = _CadVrStatusNumIsisExternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 7),
    _CadVrStatusNumIsisExternal1Routes_Type()
)
cadVrStatusNumIsisExternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIsisExternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIsisExternal1Routes.setUnits("routes")
_CadVrStatusNumIsisExternal2Routes_Type = Gauge32
_CadVrStatusNumIsisExternal2Routes_Object = MibTableColumn
cadVrStatusNumIsisExternal2Routes = _CadVrStatusNumIsisExternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 8),
    _CadVrStatusNumIsisExternal2Routes_Type()
)
cadVrStatusNumIsisExternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIsisExternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIsisExternal2Routes.setUnits("routes")
_CadVrStatusNumBgpIntRoutes_Type = Gauge32
_CadVrStatusNumBgpIntRoutes_Object = MibTableColumn
cadVrStatusNumBgpIntRoutes = _CadVrStatusNumBgpIntRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 9),
    _CadVrStatusNumBgpIntRoutes_Type()
)
cadVrStatusNumBgpIntRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumBgpIntRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumBgpIntRoutes.setUnits("routes")
_CadVrStatusNumBgpExtRoutes_Type = Gauge32
_CadVrStatusNumBgpExtRoutes_Object = MibTableColumn
cadVrStatusNumBgpExtRoutes = _CadVrStatusNumBgpExtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 10),
    _CadVrStatusNumBgpExtRoutes_Type()
)
cadVrStatusNumBgpExtRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumBgpExtRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumBgpExtRoutes.setUnits("routes")
_CadVrStatusNumBgpVpnRoutes_Type = Gauge32
_CadVrStatusNumBgpVpnRoutes_Object = MibTableColumn
cadVrStatusNumBgpVpnRoutes = _CadVrStatusNumBgpVpnRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 11),
    _CadVrStatusNumBgpVpnRoutes_Type()
)
cadVrStatusNumBgpVpnRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumBgpVpnRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumBgpVpnRoutes.setUnits("routes")
_CadVrStatusNumOspfIntraAreaRoutes_Type = Gauge32
_CadVrStatusNumOspfIntraAreaRoutes_Object = MibTableColumn
cadVrStatusNumOspfIntraAreaRoutes = _CadVrStatusNumOspfIntraAreaRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 12),
    _CadVrStatusNumOspfIntraAreaRoutes_Type()
)
cadVrStatusNumOspfIntraAreaRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfIntraAreaRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfIntraAreaRoutes.setUnits("routes")
_CadVrStatusNumOspfInterAreaRoutes_Type = Gauge32
_CadVrStatusNumOspfInterAreaRoutes_Object = MibTableColumn
cadVrStatusNumOspfInterAreaRoutes = _CadVrStatusNumOspfInterAreaRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 13),
    _CadVrStatusNumOspfInterAreaRoutes_Type()
)
cadVrStatusNumOspfInterAreaRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfInterAreaRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfInterAreaRoutes.setUnits("routes")
_CadVrStatusNumOspfInternal1Routes_Type = Gauge32
_CadVrStatusNumOspfInternal1Routes_Object = MibTableColumn
cadVrStatusNumOspfInternal1Routes = _CadVrStatusNumOspfInternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 14),
    _CadVrStatusNumOspfInternal1Routes_Type()
)
cadVrStatusNumOspfInternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfInternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfInternal1Routes.setUnits("routes")
_CadVrStatusNumOspfInternal2Routes_Type = Gauge32
_CadVrStatusNumOspfInternal2Routes_Object = MibTableColumn
cadVrStatusNumOspfInternal2Routes = _CadVrStatusNumOspfInternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 15),
    _CadVrStatusNumOspfInternal2Routes_Type()
)
cadVrStatusNumOspfInternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfInternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfInternal2Routes.setUnits("routes")
_CadVrStatusNumOspfExternal1Routes_Type = Gauge32
_CadVrStatusNumOspfExternal1Routes_Object = MibTableColumn
cadVrStatusNumOspfExternal1Routes = _CadVrStatusNumOspfExternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 16),
    _CadVrStatusNumOspfExternal1Routes_Type()
)
cadVrStatusNumOspfExternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfExternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfExternal1Routes.setUnits("routes")
_CadVrStatusNumOspfExternal2Routes_Type = Gauge32
_CadVrStatusNumOspfExternal2Routes_Object = MibTableColumn
cadVrStatusNumOspfExternal2Routes = _CadVrStatusNumOspfExternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 17),
    _CadVrStatusNumOspfExternal2Routes_Type()
)
cadVrStatusNumOspfExternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfExternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfExternal2Routes.setUnits("routes")
_CadVrStatusNumOspfNssaExternal1Routes_Type = Gauge32
_CadVrStatusNumOspfNssaExternal1Routes_Object = MibTableColumn
cadVrStatusNumOspfNssaExternal1Routes = _CadVrStatusNumOspfNssaExternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 18),
    _CadVrStatusNumOspfNssaExternal1Routes_Type()
)
cadVrStatusNumOspfNssaExternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfNssaExternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfNssaExternal1Routes.setUnits("routes")
_CadVrStatusNumOspfNssaExternal2Routes_Type = Gauge32
_CadVrStatusNumOspfNssaExternal2Routes_Object = MibTableColumn
cadVrStatusNumOspfNssaExternal2Routes = _CadVrStatusNumOspfNssaExternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 19),
    _CadVrStatusNumOspfNssaExternal2Routes_Type()
)
cadVrStatusNumOspfNssaExternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfNssaExternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumOspfNssaExternal2Routes.setUnits("routes")
_CadVrStatusNumOtherRoutes_Type = Gauge32
_CadVrStatusNumOtherRoutes_Object = MibTableColumn
cadVrStatusNumOtherRoutes = _CadVrStatusNumOtherRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 20),
    _CadVrStatusNumOtherRoutes_Type()
)
cadVrStatusNumOtherRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumOtherRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumOtherRoutes.setUnits("routes")
_CadVrStatusNumIpv6LocalRoutes_Type = Gauge32
_CadVrStatusNumIpv6LocalRoutes_Object = MibTableColumn
cadVrStatusNumIpv6LocalRoutes = _CadVrStatusNumIpv6LocalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 21),
    _CadVrStatusNumIpv6LocalRoutes_Type()
)
cadVrStatusNumIpv6LocalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6LocalRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6LocalRoutes.setUnits("routes")
_CadVrStatusNumIpv6NetmgmtRoutes_Type = Gauge32
_CadVrStatusNumIpv6NetmgmtRoutes_Object = MibTableColumn
cadVrStatusNumIpv6NetmgmtRoutes = _CadVrStatusNumIpv6NetmgmtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 22),
    _CadVrStatusNumIpv6NetmgmtRoutes_Type()
)
cadVrStatusNumIpv6NetmgmtRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6NetmgmtRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6NetmgmtRoutes.setUnits("routes")
_CadVrStatusNumIpv6IsisInternal1Routes_Type = Gauge32
_CadVrStatusNumIpv6IsisInternal1Routes_Object = MibTableColumn
cadVrStatusNumIpv6IsisInternal1Routes = _CadVrStatusNumIpv6IsisInternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 23),
    _CadVrStatusNumIpv6IsisInternal1Routes_Type()
)
cadVrStatusNumIpv6IsisInternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6IsisInternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6IsisInternal1Routes.setUnits("routes")
_CadVrStatusNumIpv6IsisInternal2Routes_Type = Gauge32
_CadVrStatusNumIpv6IsisInternal2Routes_Object = MibTableColumn
cadVrStatusNumIpv6IsisInternal2Routes = _CadVrStatusNumIpv6IsisInternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 24),
    _CadVrStatusNumIpv6IsisInternal2Routes_Type()
)
cadVrStatusNumIpv6IsisInternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6IsisInternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6IsisInternal2Routes.setUnits("routes")
_CadVrStatusNumIpv6IsisExternal1Routes_Type = Gauge32
_CadVrStatusNumIpv6IsisExternal1Routes_Object = MibTableColumn
cadVrStatusNumIpv6IsisExternal1Routes = _CadVrStatusNumIpv6IsisExternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 25),
    _CadVrStatusNumIpv6IsisExternal1Routes_Type()
)
cadVrStatusNumIpv6IsisExternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6IsisExternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6IsisExternal1Routes.setUnits("routes")
_CadVrStatusNumIpv6IsisExternal2Routes_Type = Gauge32
_CadVrStatusNumIpv6IsisExternal2Routes_Object = MibTableColumn
cadVrStatusNumIpv6IsisExternal2Routes = _CadVrStatusNumIpv6IsisExternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 26),
    _CadVrStatusNumIpv6IsisExternal2Routes_Type()
)
cadVrStatusNumIpv6IsisExternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6IsisExternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6IsisExternal2Routes.setUnits("routes")
_CadVrStatusNumIpv6OspfIntraAreaRoutes_Type = Gauge32
_CadVrStatusNumIpv6OspfIntraAreaRoutes_Object = MibTableColumn
cadVrStatusNumIpv6OspfIntraAreaRoutes = _CadVrStatusNumIpv6OspfIntraAreaRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 27),
    _CadVrStatusNumIpv6OspfIntraAreaRoutes_Type()
)
cadVrStatusNumIpv6OspfIntraAreaRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfIntraAreaRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfIntraAreaRoutes.setUnits("routes")
_CadVrStatusNumIpv6OspfInterAreaRoutes_Type = Gauge32
_CadVrStatusNumIpv6OspfInterAreaRoutes_Object = MibTableColumn
cadVrStatusNumIpv6OspfInterAreaRoutes = _CadVrStatusNumIpv6OspfInterAreaRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 28),
    _CadVrStatusNumIpv6OspfInterAreaRoutes_Type()
)
cadVrStatusNumIpv6OspfInterAreaRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfInterAreaRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfInterAreaRoutes.setUnits("routes")
_CadVrStatusNumIpv6OspfInternal1Routes_Type = Gauge32
_CadVrStatusNumIpv6OspfInternal1Routes_Object = MibTableColumn
cadVrStatusNumIpv6OspfInternal1Routes = _CadVrStatusNumIpv6OspfInternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 29),
    _CadVrStatusNumIpv6OspfInternal1Routes_Type()
)
cadVrStatusNumIpv6OspfInternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfInternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfInternal1Routes.setUnits("routes")
_CadVrStatusNumIpv6OspfInternal2Routes_Type = Gauge32
_CadVrStatusNumIpv6OspfInternal2Routes_Object = MibTableColumn
cadVrStatusNumIpv6OspfInternal2Routes = _CadVrStatusNumIpv6OspfInternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 30),
    _CadVrStatusNumIpv6OspfInternal2Routes_Type()
)
cadVrStatusNumIpv6OspfInternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfInternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfInternal2Routes.setUnits("routes")
_CadVrStatusNumIpv6OspfExternal1Routes_Type = Gauge32
_CadVrStatusNumIpv6OspfExternal1Routes_Object = MibTableColumn
cadVrStatusNumIpv6OspfExternal1Routes = _CadVrStatusNumIpv6OspfExternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 31),
    _CadVrStatusNumIpv6OspfExternal1Routes_Type()
)
cadVrStatusNumIpv6OspfExternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfExternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfExternal1Routes.setUnits("routes")
_CadVrStatusNumIpv6OspfExternal2Routes_Type = Gauge32
_CadVrStatusNumIpv6OspfExternal2Routes_Object = MibTableColumn
cadVrStatusNumIpv6OspfExternal2Routes = _CadVrStatusNumIpv6OspfExternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 32),
    _CadVrStatusNumIpv6OspfExternal2Routes_Type()
)
cadVrStatusNumIpv6OspfExternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfExternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfExternal2Routes.setUnits("routes")
_CadVrStatusNumIpv6OspfNssaExternal1Routes_Type = Gauge32
_CadVrStatusNumIpv6OspfNssaExternal1Routes_Object = MibTableColumn
cadVrStatusNumIpv6OspfNssaExternal1Routes = _CadVrStatusNumIpv6OspfNssaExternal1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 33),
    _CadVrStatusNumIpv6OspfNssaExternal1Routes_Type()
)
cadVrStatusNumIpv6OspfNssaExternal1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfNssaExternal1Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfNssaExternal1Routes.setUnits("routes")
_CadVrStatusNumIpv6OspfNssaExternal2Routes_Type = Gauge32
_CadVrStatusNumIpv6OspfNssaExternal2Routes_Object = MibTableColumn
cadVrStatusNumIpv6OspfNssaExternal2Routes = _CadVrStatusNumIpv6OspfNssaExternal2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 34),
    _CadVrStatusNumIpv6OspfNssaExternal2Routes_Type()
)
cadVrStatusNumIpv6OspfNssaExternal2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfNssaExternal2Routes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OspfNssaExternal2Routes.setUnits("routes")
_CadVrStatusNumIpv6PdRoutes_Type = Gauge32
_CadVrStatusNumIpv6PdRoutes_Object = MibTableColumn
cadVrStatusNumIpv6PdRoutes = _CadVrStatusNumIpv6PdRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 35),
    _CadVrStatusNumIpv6PdRoutes_Type()
)
cadVrStatusNumIpv6PdRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6PdRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6PdRoutes.setUnits("routes")
_CadVrStatusNumIpv6OtherRoutes_Type = Gauge32
_CadVrStatusNumIpv6OtherRoutes_Object = MibTableColumn
cadVrStatusNumIpv6OtherRoutes = _CadVrStatusNumIpv6OtherRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 36),
    _CadVrStatusNumIpv6OtherRoutes_Type()
)
cadVrStatusNumIpv6OtherRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OtherRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6OtherRoutes.setUnits("routes")
_CadVrStatusNumIpv6BgpIntRoutes_Type = Gauge32
_CadVrStatusNumIpv6BgpIntRoutes_Object = MibTableColumn
cadVrStatusNumIpv6BgpIntRoutes = _CadVrStatusNumIpv6BgpIntRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 37),
    _CadVrStatusNumIpv6BgpIntRoutes_Type()
)
cadVrStatusNumIpv6BgpIntRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6BgpIntRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6BgpIntRoutes.setUnits("routes")
_CadVrStatusNumIpv6BgpExtRoutes_Type = Gauge32
_CadVrStatusNumIpv6BgpExtRoutes_Object = MibTableColumn
cadVrStatusNumIpv6BgpExtRoutes = _CadVrStatusNumIpv6BgpExtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 38),
    _CadVrStatusNumIpv6BgpExtRoutes_Type()
)
cadVrStatusNumIpv6BgpExtRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6BgpExtRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6BgpExtRoutes.setUnits("routes")
_CadVrStatusNumIpv6BgpVpnRoutes_Type = Gauge32
_CadVrStatusNumIpv6BgpVpnRoutes_Object = MibTableColumn
cadVrStatusNumIpv6BgpVpnRoutes = _CadVrStatusNumIpv6BgpVpnRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 5, 1, 39),
    _CadVrStatusNumIpv6BgpVpnRoutes_Type()
)
cadVrStatusNumIpv6BgpVpnRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6BgpVpnRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cadVrStatusNumIpv6BgpVpnRoutes.setUnits("routes")
_CadVrInterfaceStatusTable_Object = MibTable
cadVrInterfaceStatusTable = _CadVrInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cadVrInterfaceStatusTable.setStatus("current")
_CadVrInterfaceStatusEntry_Object = MibTableRow
cadVrInterfaceStatusEntry = _CadVrInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 6, 1)
)
cadVrInterfaceStatusEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceStatusIfIndex"),
)
if mibBuilder.loadTexts:
    cadVrInterfaceStatusEntry.setStatus("current")
_CadVrInterfaceStatusIfIndex_Type = InterfaceIndex
_CadVrInterfaceStatusIfIndex_Object = MibTableColumn
cadVrInterfaceStatusIfIndex = _CadVrInterfaceStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 6, 1, 1),
    _CadVrInterfaceStatusIfIndex_Type()
)
cadVrInterfaceStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrInterfaceStatusIfIndex.setStatus("current")
_CadVrInterfaceStatusIcmpUnreachablesDropped_Type = Counter32
_CadVrInterfaceStatusIcmpUnreachablesDropped_Object = MibTableColumn
cadVrInterfaceStatusIcmpUnreachablesDropped = _CadVrInterfaceStatusIcmpUnreachablesDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 6, 1, 2),
    _CadVrInterfaceStatusIcmpUnreachablesDropped_Type()
)
cadVrInterfaceStatusIcmpUnreachablesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrInterfaceStatusIcmpUnreachablesDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadVrInterfaceStatusIcmpUnreachablesDropped.setUnits("packets")
_CadVrInterfaceStatusIcmpv6UnreachablesDropped_Type = Counter32
_CadVrInterfaceStatusIcmpv6UnreachablesDropped_Object = MibTableColumn
cadVrInterfaceStatusIcmpv6UnreachablesDropped = _CadVrInterfaceStatusIcmpv6UnreachablesDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 6, 1, 3),
    _CadVrInterfaceStatusIcmpv6UnreachablesDropped_Type()
)
cadVrInterfaceStatusIcmpv6UnreachablesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrInterfaceStatusIcmpv6UnreachablesDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadVrInterfaceStatusIcmpv6UnreachablesDropped.setUnits("packets")
_CadVrGlobals_ObjectIdentity = ObjectIdentity
cadVrGlobals = _CadVrGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7)
)


class _CadVrGlobalIcmpUnreachablesEnabled_Type(TruthValue):
    """Custom type cadVrGlobalIcmpUnreachablesEnabled based on TruthValue"""


_CadVrGlobalIcmpUnreachablesEnabled_Object = MibScalar
cadVrGlobalIcmpUnreachablesEnabled = _CadVrGlobalIcmpUnreachablesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7, 1),
    _CadVrGlobalIcmpUnreachablesEnabled_Type()
)
cadVrGlobalIcmpUnreachablesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrGlobalIcmpUnreachablesEnabled.setStatus("current")


class _CadVrGlobalIpForwarding_Type(Integer32):
    """Custom type cadVrGlobalIpForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_CadVrGlobalIpForwarding_Type.__name__ = "Integer32"
_CadVrGlobalIpForwarding_Object = MibScalar
cadVrGlobalIpForwarding = _CadVrGlobalIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7, 2),
    _CadVrGlobalIpForwarding_Type()
)
cadVrGlobalIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrGlobalIpForwarding.setStatus("current")


class _CadVrGlobalIpDefaultTTL_Type(Integer32):
    """Custom type cadVrGlobalIpDefaultTTL based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadVrGlobalIpDefaultTTL_Type.__name__ = "Integer32"
_CadVrGlobalIpDefaultTTL_Object = MibScalar
cadVrGlobalIpDefaultTTL = _CadVrGlobalIpDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7, 3),
    _CadVrGlobalIpDefaultTTL_Type()
)
cadVrGlobalIpDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrGlobalIpDefaultTTL.setStatus("current")


class _CadVrGlobalIpv6IpForwarding_Type(Integer32):
    """Custom type cadVrGlobalIpv6IpForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_CadVrGlobalIpv6IpForwarding_Type.__name__ = "Integer32"
_CadVrGlobalIpv6IpForwarding_Object = MibScalar
cadVrGlobalIpv6IpForwarding = _CadVrGlobalIpv6IpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7, 4),
    _CadVrGlobalIpv6IpForwarding_Type()
)
cadVrGlobalIpv6IpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrGlobalIpv6IpForwarding.setStatus("current")


class _CadVrGlobalIpv6IpDefaultHopLimit_Type(Integer32):
    """Custom type cadVrGlobalIpv6IpDefaultHopLimit based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadVrGlobalIpv6IpDefaultHopLimit_Type.__name__ = "Integer32"
_CadVrGlobalIpv6IpDefaultHopLimit_Object = MibScalar
cadVrGlobalIpv6IpDefaultHopLimit = _CadVrGlobalIpv6IpDefaultHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7, 5),
    _CadVrGlobalIpv6IpDefaultHopLimit_Type()
)
cadVrGlobalIpv6IpDefaultHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrGlobalIpv6IpDefaultHopLimit.setStatus("current")


class _CadVrGlobalIcmpv6UnreachablesEnabled_Type(TruthValue):
    """Custom type cadVrGlobalIcmpv6UnreachablesEnabled based on TruthValue"""


_CadVrGlobalIcmpv6UnreachablesEnabled_Object = MibScalar
cadVrGlobalIcmpv6UnreachablesEnabled = _CadVrGlobalIcmpv6UnreachablesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7, 6),
    _CadVrGlobalIcmpv6UnreachablesEnabled_Type()
)
cadVrGlobalIcmpv6UnreachablesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrGlobalIcmpv6UnreachablesEnabled.setStatus("current")


class _CadVrGlobalIcmpv6TooBigEnabled_Type(TruthValue):
    """Custom type cadVrGlobalIcmpv6TooBigEnabled based on TruthValue"""


_CadVrGlobalIcmpv6TooBigEnabled_Object = MibScalar
cadVrGlobalIcmpv6TooBigEnabled = _CadVrGlobalIcmpv6TooBigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7, 7),
    _CadVrGlobalIcmpv6TooBigEnabled_Type()
)
cadVrGlobalIcmpv6TooBigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrGlobalIcmpv6TooBigEnabled.setStatus("current")


class _CadVrGlobalIcmpv6ParameterProblemEnabled_Type(TruthValue):
    """Custom type cadVrGlobalIcmpv6ParameterProblemEnabled based on TruthValue"""


_CadVrGlobalIcmpv6ParameterProblemEnabled_Object = MibScalar
cadVrGlobalIcmpv6ParameterProblemEnabled = _CadVrGlobalIcmpv6ParameterProblemEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7, 8),
    _CadVrGlobalIcmpv6ParameterProblemEnabled_Type()
)
cadVrGlobalIcmpv6ParameterProblemEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrGlobalIcmpv6ParameterProblemEnabled.setStatus("current")


class _CadVrGlobalAllowAnyCableMac_Type(TruthValue):
    """Custom type cadVrGlobalAllowAnyCableMac based on TruthValue"""


_CadVrGlobalAllowAnyCableMac_Object = MibScalar
cadVrGlobalAllowAnyCableMac = _CadVrGlobalAllowAnyCableMac_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 7, 10),
    _CadVrGlobalAllowAnyCableMac_Type()
)
cadVrGlobalAllowAnyCableMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadVrGlobalAllowAnyCableMac.setStatus("current")
_CadVrGlobalStatus_ObjectIdentity = ObjectIdentity
cadVrGlobalStatus = _CadVrGlobalStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 8)
)
_CadVrGlobalStatusIcmpUnreachablesDropped_Type = Counter32
_CadVrGlobalStatusIcmpUnreachablesDropped_Object = MibScalar
cadVrGlobalStatusIcmpUnreachablesDropped = _CadVrGlobalStatusIcmpUnreachablesDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 8, 1),
    _CadVrGlobalStatusIcmpUnreachablesDropped_Type()
)
cadVrGlobalStatusIcmpUnreachablesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrGlobalStatusIcmpUnreachablesDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadVrGlobalStatusIcmpUnreachablesDropped.setUnits("packets")
_CadVrGlobalStatusIcmpv6UnreachablesDropped_Type = Counter32
_CadVrGlobalStatusIcmpv6UnreachablesDropped_Object = MibScalar
cadVrGlobalStatusIcmpv6UnreachablesDropped = _CadVrGlobalStatusIcmpv6UnreachablesDropped_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 8, 2),
    _CadVrGlobalStatusIcmpv6UnreachablesDropped_Type()
)
cadVrGlobalStatusIcmpv6UnreachablesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrGlobalStatusIcmpv6UnreachablesDropped.setStatus("current")
if mibBuilder.loadTexts:
    cadVrGlobalStatusIcmpv6UnreachablesDropped.setUnits("packets")
_CadVrAddressPrefixTable_Object = MibTable
cadVrAddressPrefixTable = _CadVrAddressPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cadVrAddressPrefixTable.setStatus("current")
_CadVrAddressPrefixEntry_Object = MibTableRow
cadVrAddressPrefixEntry = _CadVrAddressPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1)
)
cadVrAddressPrefixEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrInterfaceSubifIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadBgIndex"),
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrAddressPrefixType"),
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrAddressPrefixPrefix"),
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrAddressPrefixLength"),
)
if mibBuilder.loadTexts:
    cadVrAddressPrefixEntry.setStatus("current")
_CadVrAddressPrefixType_Type = InetAddressType
_CadVrAddressPrefixType_Object = MibTableColumn
cadVrAddressPrefixType = _CadVrAddressPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 1),
    _CadVrAddressPrefixType_Type()
)
cadVrAddressPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixType.setStatus("current")
_CadVrAddressPrefixPrefix_Type = InetAddressIPv4or6
_CadVrAddressPrefixPrefix_Object = MibTableColumn
cadVrAddressPrefixPrefix = _CadVrAddressPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 2),
    _CadVrAddressPrefixPrefix_Type()
)
cadVrAddressPrefixPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixPrefix.setStatus("current")
_CadVrAddressPrefixLength_Type = InetAddressPrefixLength
_CadVrAddressPrefixLength_Object = MibTableColumn
cadVrAddressPrefixLength = _CadVrAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 3),
    _CadVrAddressPrefixLength_Type()
)
cadVrAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixLength.setStatus("current")


class _CadVrAddressPrefixAdvertiseFlag_Type(TruthValue):
    """Custom type cadVrAddressPrefixAdvertiseFlag based on TruthValue"""


_CadVrAddressPrefixAdvertiseFlag_Object = MibTableColumn
cadVrAddressPrefixAdvertiseFlag = _CadVrAddressPrefixAdvertiseFlag_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 4),
    _CadVrAddressPrefixAdvertiseFlag_Type()
)
cadVrAddressPrefixAdvertiseFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixAdvertiseFlag.setStatus("current")


class _CadVrAddressPrefixOnLinkFlag_Type(TruthValue):
    """Custom type cadVrAddressPrefixOnLinkFlag based on TruthValue"""


_CadVrAddressPrefixOnLinkFlag_Object = MibTableColumn
cadVrAddressPrefixOnLinkFlag = _CadVrAddressPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 5),
    _CadVrAddressPrefixOnLinkFlag_Type()
)
cadVrAddressPrefixOnLinkFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixOnLinkFlag.setStatus("current")


class _CadVrAddressPrefixAutonomousFlag_Type(TruthValue):
    """Custom type cadVrAddressPrefixAutonomousFlag based on TruthValue"""


_CadVrAddressPrefixAutonomousFlag_Object = MibTableColumn
cadVrAddressPrefixAutonomousFlag = _CadVrAddressPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 6),
    _CadVrAddressPrefixAutonomousFlag_Type()
)
cadVrAddressPrefixAutonomousFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixAutonomousFlag.setStatus("current")


class _CadVrAddressPrefixAdvPreferredLifetime_Type(Unsigned32):
    """Custom type cadVrAddressPrefixAdvPreferredLifetime based on Unsigned32"""
    defaultValue = 2592000


_CadVrAddressPrefixAdvPreferredLifetime_Object = MibTableColumn
cadVrAddressPrefixAdvPreferredLifetime = _CadVrAddressPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 7),
    _CadVrAddressPrefixAdvPreferredLifetime_Type()
)
cadVrAddressPrefixAdvPreferredLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixAdvPreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cadVrAddressPrefixAdvPreferredLifetime.setUnits("seconds")


class _CadVrAddressPrefixAdvValidLifetime_Type(Unsigned32):
    """Custom type cadVrAddressPrefixAdvValidLifetime based on Unsigned32"""
    defaultValue = 2592000


_CadVrAddressPrefixAdvValidLifetime_Object = MibTableColumn
cadVrAddressPrefixAdvValidLifetime = _CadVrAddressPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 8),
    _CadVrAddressPrefixAdvValidLifetime_Type()
)
cadVrAddressPrefixAdvValidLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixAdvValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cadVrAddressPrefixAdvValidLifetime.setUnits("seconds")


class _CadVrAddressPrefixAdvPreferredDate_Type(DateAndTime):
    """Custom type cadVrAddressPrefixAdvPreferredDate based on DateAndTime"""
    defaultHexValue = ""


_CadVrAddressPrefixAdvPreferredDate_Object = MibTableColumn
cadVrAddressPrefixAdvPreferredDate = _CadVrAddressPrefixAdvPreferredDate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 9),
    _CadVrAddressPrefixAdvPreferredDate_Type()
)
cadVrAddressPrefixAdvPreferredDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixAdvPreferredDate.setStatus("current")


class _CadVrAddressPrefixAdvValidDate_Type(DateAndTime):
    """Custom type cadVrAddressPrefixAdvValidDate based on DateAndTime"""
    defaultHexValue = ""


_CadVrAddressPrefixAdvValidDate_Object = MibTableColumn
cadVrAddressPrefixAdvValidDate = _CadVrAddressPrefixAdvValidDate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 10),
    _CadVrAddressPrefixAdvValidDate_Type()
)
cadVrAddressPrefixAdvValidDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixAdvValidDate.setStatus("current")
_CadVrAddressPrefixRowStatus_Type = RowStatus
_CadVrAddressPrefixRowStatus_Object = MibTableColumn
cadVrAddressPrefixRowStatus = _CadVrAddressPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 9, 1, 11),
    _CadVrAddressPrefixRowStatus_Type()
)
cadVrAddressPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrAddressPrefixRowStatus.setStatus("current")
_CadVrRtLookupTable_Object = MibTable
cadVrRtLookupTable = _CadVrRtLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cadVrRtLookupTable.setStatus("current")
_CadVrRtLookupEntry_Object = MibTableRow
cadVrRtLookupEntry = _CadVrRtLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 10, 1)
)
cadVrRtLookupEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrRtLookupVrIndex"),
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrRtLookupInetAddrType"),
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrRtLookupInetAddr"),
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrRtLookupPrefixLength"),
)
if mibBuilder.loadTexts:
    cadVrRtLookupEntry.setStatus("current")


class _CadVrRtLookupVrIndex_Type(Integer32):
    """Custom type cadVrRtLookupVrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_CadVrRtLookupVrIndex_Type.__name__ = "Integer32"
_CadVrRtLookupVrIndex_Object = MibTableColumn
cadVrRtLookupVrIndex = _CadVrRtLookupVrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 10, 1, 1),
    _CadVrRtLookupVrIndex_Type()
)
cadVrRtLookupVrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadVrRtLookupVrIndex.setStatus("current")
_CadVrRtLookupInetAddrType_Type = InetAddressType
_CadVrRtLookupInetAddrType_Object = MibTableColumn
cadVrRtLookupInetAddrType = _CadVrRtLookupInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 10, 1, 2),
    _CadVrRtLookupInetAddrType_Type()
)
cadVrRtLookupInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrRtLookupInetAddrType.setStatus("current")


class _CadVrRtLookupInetAddr_Type(InetAddressIPv4or6):
    """Custom type cadVrRtLookupInetAddr based on InetAddressIPv4or6"""
    defaultHexValue = ""


_CadVrRtLookupInetAddr_Object = MibTableColumn
cadVrRtLookupInetAddr = _CadVrRtLookupInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 10, 1, 3),
    _CadVrRtLookupInetAddr_Type()
)
cadVrRtLookupInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrRtLookupInetAddr.setStatus("current")
_CadVrRtLookupPrefixLength_Type = InetAddressPrefixLength
_CadVrRtLookupPrefixLength_Object = MibTableColumn
cadVrRtLookupPrefixLength = _CadVrRtLookupPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 10, 1, 4),
    _CadVrRtLookupPrefixLength_Type()
)
cadVrRtLookupPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadVrRtLookupPrefixLength.setStatus("current")


class _CadVrRtLookupInetAddrResult_Type(InetAddressIPv4or6):
    """Custom type cadVrRtLookupInetAddrResult based on InetAddressIPv4or6"""
    defaultHexValue = ""


_CadVrRtLookupInetAddrResult_Object = MibTableColumn
cadVrRtLookupInetAddrResult = _CadVrRtLookupInetAddrResult_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 10, 1, 5),
    _CadVrRtLookupInetAddrResult_Type()
)
cadVrRtLookupInetAddrResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrRtLookupInetAddrResult.setStatus("current")
_CadVrRtLookupPrefixLengthResult_Type = InetAddressPrefixLength
_CadVrRtLookupPrefixLengthResult_Object = MibTableColumn
cadVrRtLookupPrefixLengthResult = _CadVrRtLookupPrefixLengthResult_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 3, 1, 10, 1, 6),
    _CadVrRtLookupPrefixLengthResult_Type()
)
cadVrRtLookupPrefixLengthResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadVrRtLookupPrefixLengthResult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-VIRTUAL-ROUTER-MIB",
    **{"CadSourceVerifyType": CadSourceVerifyType,
       "cadVirtualRouterMibModule": cadVirtualRouterMibModule,
       "cadVirtualRouter": cadVirtualRouter,
       "cadVrNameTable": cadVrNameTable,
       "cadVrNameEntry": cadVrNameEntry,
       "cadVrNameVrIndex": cadVrNameVrIndex,
       "cadVrNameRowStatus": cadVrNameRowStatus,
       "cadVrTable": cadVrTable,
       "cadVrEntry": cadVrEntry,
       "cadVrIndex": cadVrIndex,
       "cadVrName": cadVrName,
       "cadVrOspfEnabled": cadVrOspfEnabled,
       "cadVrRipEnabled": cadVrRipEnabled,
       "cadVrRowStatus": cadVrRowStatus,
       "cadVrScmAccessEnabled": cadVrScmAccessEnabled,
       "cadVrScmAccessDirectedBroadcastEnabled": cadVrScmAccessDirectedBroadcastEnabled,
       "cadVrNullInterface": cadVrNullInterface,
       "cadVrICMPTimeExceededEnabled": cadVrICMPTimeExceededEnabled,
       "cadVrOspfGracefulRestartEnabled": cadVrOspfGracefulRestartEnabled,
       "cadVrIPv6ReflectionEnabled": cadVrIPv6ReflectionEnabled,
       "cadVrICMPv6TimeExceededEnabled": cadVrICMPv6TimeExceededEnabled,
       "cadVrNullInterfacev6": cadVrNullInterfacev6,
       "cadVrPhpEnabled": cadVrPhpEnabled,
       "cadVrAutoImportEnabled": cadVrAutoImportEnabled,
       "cadVrInterfaceTable": cadVrInterfaceTable,
       "cadVrInterfaceEntry": cadVrInterfaceEntry,
       "cadVrInterfaceIfIndex": cadVrInterfaceIfIndex,
       "cadVrInterfaceIpAddr": cadVrInterfaceIpAddr,
       "cadVrInterfaceIpMask": cadVrInterfaceIpMask,
       "cadVrInterfaceDHCPEnabled": cadVrInterfaceDHCPEnabled,
       "cadVrInterfaceFARPEnabled": cadVrInterfaceFARPEnabled,
       "cadVrInterfaceRipEnabled": cadVrInterfaceRipEnabled,
       "cadVrInterfaceRipPassive": cadVrInterfaceRipPassive,
       "cadVrInterfaceIGMPEnabled": cadVrInterfaceIGMPEnabled,
       "cadVrInterfaceIRDPEnabled": cadVrInterfaceIRDPEnabled,
       "cadVrInterfaceRowStatus": cadVrInterfaceRowStatus,
       "cadVrInterfaceDHCPPolicyEnabled": cadVrInterfaceDHCPPolicyEnabled,
       "cadVrInterfaceDirectedBcastEnabled": cadVrInterfaceDirectedBcastEnabled,
       "cadVrInterfaceSourceVerify": cadVrInterfaceSourceVerify,
       "cadVrInterfaceSubFilterDownDefault": cadVrInterfaceSubFilterDownDefault,
       "cadVrInterfaceSubFilterUpDefault": cadVrInterfaceSubFilterUpDefault,
       "cadVrInterfaceCmFilterDownDefault": cadVrInterfaceCmFilterDownDefault,
       "cadVrInterfaceCmFilterUpDefault": cadVrInterfaceCmFilterUpDefault,
       "cadVrInterfaceSubifIndex": cadVrInterfaceSubifIndex,
       "cadVrInterfaceVrIndex": cadVrInterfaceVrIndex,
       "cadVrInterfaceIsLoopback": cadVrInterfaceIsLoopback,
       "cadVrInterfaceRestrictedFARPEnabled": cadVrInterfaceRestrictedFARPEnabled,
       "cadVrInterfaceAdminStat": cadVrInterfaceAdminStat,
       "cadVrInterfaceIcmpUnreachablesEnabled": cadVrInterfaceIcmpUnreachablesEnabled,
       "cadVrInterfaceDescription": cadVrInterfaceDescription,
       "cadVrInterfaceEncapType": cadVrInterfaceEncapType,
       "cadVrInterfaceVlanId": cadVrInterfaceVlanId,
       "cadVrInterfacePriority": cadVrInterfacePriority,
       "cadVrInterfaceScmAccess": cadVrInterfaceScmAccess,
       "cadVrInterfaceIpAddrType": cadVrInterfaceIpAddrType,
       "cadVrInterfaceIpPrefixLength": cadVrInterfaceIpPrefixLength,
       "cadVrInterfaceIpScopeType": cadVrInterfaceIpScopeType,
       "cadVrInterfaceIpv6Addr": cadVrInterfaceIpv6Addr,
       "cadVrInterfaceIpv6PrefixLength": cadVrInterfaceIpv6PrefixLength,
       "cadVrInterfaceDADAttempts": cadVrInterfaceDADAttempts,
       "cadVrInterfaceIpv6Forwarding": cadVrInterfaceIpv6Forwarding,
       "cadVrInterfacePsFilterDownDefault": cadVrInterfacePsFilterDownDefault,
       "cadVrInterfacePsFilterUpDefault": cadVrInterfacePsFilterUpDefault,
       "cadVrInterfaceMtaFilterDownDefault": cadVrInterfaceMtaFilterDownDefault,
       "cadVrInterfaceMtaFilterUpDefault": cadVrInterfaceMtaFilterUpDefault,
       "cadVrInterfaceStbFilterDownDefault": cadVrInterfaceStbFilterDownDefault,
       "cadVrInterfaceStbFilterUpDefault": cadVrInterfaceStbFilterUpDefault,
       "cadVrInterfaceIcmpv6UnreachablesEnabled": cadVrInterfaceIcmpv6UnreachablesEnabled,
       "cadVrInterfaceIcmpv6TooBigEnabled": cadVrInterfaceIcmpv6TooBigEnabled,
       "cadVrInterfaceIcmpv6ParameterProblemEnabled": cadVrInterfaceIcmpv6ParameterProblemEnabled,
       "cadVrInterfacePdRiEnabled": cadVrInterfacePdRiEnabled,
       "cadVrInterfacePolicyRouteMap": cadVrInterfacePolicyRouteMap,
       "cadVrInterfaceMplsEnabled": cadVrInterfaceMplsEnabled,
       "cadVrInterfaceLdpEnabled": cadVrInterfaceLdpEnabled,
       "cadVrInterfaceGratuitousArpEnabled": cadVrInterfaceGratuitousArpEnabled,
       "cadVrInterfaceIsSdv": cadVrInterfaceIsSdv,
       "cadVrSecondaryIpAddrTable": cadVrSecondaryIpAddrTable,
       "cadVrSecondaryIpAddrEntry": cadVrSecondaryIpAddrEntry,
       "cadVrSecondaryIpMask": cadVrSecondaryIpMask,
       "cadVrSecondaryIpAddrRowStatus": cadVrSecondaryIpAddrRowStatus,
       "cadVrSecondaryIpAddrDHCPPolicyEnabled": cadVrSecondaryIpAddrDHCPPolicyEnabled,
       "cadVrSecondaryIpPrefixLength": cadVrSecondaryIpPrefixLength,
       "cadVrSecondaryIpAddrType": cadVrSecondaryIpAddrType,
       "cadVrSecondaryIpScopeType": cadVrSecondaryIpScopeType,
       "cadVrSecondaryIpAddrDHCPGiaddr": cadVrSecondaryIpAddrDHCPGiaddr,
       "cadVrStatusTable": cadVrStatusTable,
       "cadVrStatusEntry": cadVrStatusEntry,
       "cadVrStatusVrIndex": cadVrStatusVrIndex,
       "cadVrStatusNumLocalRoutes": cadVrStatusNumLocalRoutes,
       "cadVrStatusNumNetmgmtRoutes": cadVrStatusNumNetmgmtRoutes,
       "cadVrStatusNumRipRoutes": cadVrStatusNumRipRoutes,
       "cadVrStatusNumIsisInternal1Routes": cadVrStatusNumIsisInternal1Routes,
       "cadVrStatusNumIsisInternal2Routes": cadVrStatusNumIsisInternal2Routes,
       "cadVrStatusNumIsisExternal1Routes": cadVrStatusNumIsisExternal1Routes,
       "cadVrStatusNumIsisExternal2Routes": cadVrStatusNumIsisExternal2Routes,
       "cadVrStatusNumBgpIntRoutes": cadVrStatusNumBgpIntRoutes,
       "cadVrStatusNumBgpExtRoutes": cadVrStatusNumBgpExtRoutes,
       "cadVrStatusNumBgpVpnRoutes": cadVrStatusNumBgpVpnRoutes,
       "cadVrStatusNumOspfIntraAreaRoutes": cadVrStatusNumOspfIntraAreaRoutes,
       "cadVrStatusNumOspfInterAreaRoutes": cadVrStatusNumOspfInterAreaRoutes,
       "cadVrStatusNumOspfInternal1Routes": cadVrStatusNumOspfInternal1Routes,
       "cadVrStatusNumOspfInternal2Routes": cadVrStatusNumOspfInternal2Routes,
       "cadVrStatusNumOspfExternal1Routes": cadVrStatusNumOspfExternal1Routes,
       "cadVrStatusNumOspfExternal2Routes": cadVrStatusNumOspfExternal2Routes,
       "cadVrStatusNumOspfNssaExternal1Routes": cadVrStatusNumOspfNssaExternal1Routes,
       "cadVrStatusNumOspfNssaExternal2Routes": cadVrStatusNumOspfNssaExternal2Routes,
       "cadVrStatusNumOtherRoutes": cadVrStatusNumOtherRoutes,
       "cadVrStatusNumIpv6LocalRoutes": cadVrStatusNumIpv6LocalRoutes,
       "cadVrStatusNumIpv6NetmgmtRoutes": cadVrStatusNumIpv6NetmgmtRoutes,
       "cadVrStatusNumIpv6IsisInternal1Routes": cadVrStatusNumIpv6IsisInternal1Routes,
       "cadVrStatusNumIpv6IsisInternal2Routes": cadVrStatusNumIpv6IsisInternal2Routes,
       "cadVrStatusNumIpv6IsisExternal1Routes": cadVrStatusNumIpv6IsisExternal1Routes,
       "cadVrStatusNumIpv6IsisExternal2Routes": cadVrStatusNumIpv6IsisExternal2Routes,
       "cadVrStatusNumIpv6OspfIntraAreaRoutes": cadVrStatusNumIpv6OspfIntraAreaRoutes,
       "cadVrStatusNumIpv6OspfInterAreaRoutes": cadVrStatusNumIpv6OspfInterAreaRoutes,
       "cadVrStatusNumIpv6OspfInternal1Routes": cadVrStatusNumIpv6OspfInternal1Routes,
       "cadVrStatusNumIpv6OspfInternal2Routes": cadVrStatusNumIpv6OspfInternal2Routes,
       "cadVrStatusNumIpv6OspfExternal1Routes": cadVrStatusNumIpv6OspfExternal1Routes,
       "cadVrStatusNumIpv6OspfExternal2Routes": cadVrStatusNumIpv6OspfExternal2Routes,
       "cadVrStatusNumIpv6OspfNssaExternal1Routes": cadVrStatusNumIpv6OspfNssaExternal1Routes,
       "cadVrStatusNumIpv6OspfNssaExternal2Routes": cadVrStatusNumIpv6OspfNssaExternal2Routes,
       "cadVrStatusNumIpv6PdRoutes": cadVrStatusNumIpv6PdRoutes,
       "cadVrStatusNumIpv6OtherRoutes": cadVrStatusNumIpv6OtherRoutes,
       "cadVrStatusNumIpv6BgpIntRoutes": cadVrStatusNumIpv6BgpIntRoutes,
       "cadVrStatusNumIpv6BgpExtRoutes": cadVrStatusNumIpv6BgpExtRoutes,
       "cadVrStatusNumIpv6BgpVpnRoutes": cadVrStatusNumIpv6BgpVpnRoutes,
       "cadVrInterfaceStatusTable": cadVrInterfaceStatusTable,
       "cadVrInterfaceStatusEntry": cadVrInterfaceStatusEntry,
       "cadVrInterfaceStatusIfIndex": cadVrInterfaceStatusIfIndex,
       "cadVrInterfaceStatusIcmpUnreachablesDropped": cadVrInterfaceStatusIcmpUnreachablesDropped,
       "cadVrInterfaceStatusIcmpv6UnreachablesDropped": cadVrInterfaceStatusIcmpv6UnreachablesDropped,
       "cadVrGlobals": cadVrGlobals,
       "cadVrGlobalIcmpUnreachablesEnabled": cadVrGlobalIcmpUnreachablesEnabled,
       "cadVrGlobalIpForwarding": cadVrGlobalIpForwarding,
       "cadVrGlobalIpDefaultTTL": cadVrGlobalIpDefaultTTL,
       "cadVrGlobalIpv6IpForwarding": cadVrGlobalIpv6IpForwarding,
       "cadVrGlobalIpv6IpDefaultHopLimit": cadVrGlobalIpv6IpDefaultHopLimit,
       "cadVrGlobalIcmpv6UnreachablesEnabled": cadVrGlobalIcmpv6UnreachablesEnabled,
       "cadVrGlobalIcmpv6TooBigEnabled": cadVrGlobalIcmpv6TooBigEnabled,
       "cadVrGlobalIcmpv6ParameterProblemEnabled": cadVrGlobalIcmpv6ParameterProblemEnabled,
       "cadVrGlobalAllowAnyCableMac": cadVrGlobalAllowAnyCableMac,
       "cadVrGlobalStatus": cadVrGlobalStatus,
       "cadVrGlobalStatusIcmpUnreachablesDropped": cadVrGlobalStatusIcmpUnreachablesDropped,
       "cadVrGlobalStatusIcmpv6UnreachablesDropped": cadVrGlobalStatusIcmpv6UnreachablesDropped,
       "cadVrAddressPrefixTable": cadVrAddressPrefixTable,
       "cadVrAddressPrefixEntry": cadVrAddressPrefixEntry,
       "cadVrAddressPrefixType": cadVrAddressPrefixType,
       "cadVrAddressPrefixPrefix": cadVrAddressPrefixPrefix,
       "cadVrAddressPrefixLength": cadVrAddressPrefixLength,
       "cadVrAddressPrefixAdvertiseFlag": cadVrAddressPrefixAdvertiseFlag,
       "cadVrAddressPrefixOnLinkFlag": cadVrAddressPrefixOnLinkFlag,
       "cadVrAddressPrefixAutonomousFlag": cadVrAddressPrefixAutonomousFlag,
       "cadVrAddressPrefixAdvPreferredLifetime": cadVrAddressPrefixAdvPreferredLifetime,
       "cadVrAddressPrefixAdvValidLifetime": cadVrAddressPrefixAdvValidLifetime,
       "cadVrAddressPrefixAdvPreferredDate": cadVrAddressPrefixAdvPreferredDate,
       "cadVrAddressPrefixAdvValidDate": cadVrAddressPrefixAdvValidDate,
       "cadVrAddressPrefixRowStatus": cadVrAddressPrefixRowStatus,
       "cadVrRtLookupTable": cadVrRtLookupTable,
       "cadVrRtLookupEntry": cadVrRtLookupEntry,
       "cadVrRtLookupVrIndex": cadVrRtLookupVrIndex,
       "cadVrRtLookupInetAddrType": cadVrRtLookupInetAddrType,
       "cadVrRtLookupInetAddr": cadVrRtLookupInetAddr,
       "cadVrRtLookupPrefixLength": cadVrRtLookupPrefixLength,
       "cadVrRtLookupInetAddrResult": cadVrRtLookupInetAddrResult,
       "cadVrRtLookupPrefixLengthResult": cadVrRtLookupPrefixLengthResult}
)
