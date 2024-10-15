# SNMP MIB module (H3C-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-PORTAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:07 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

h3cPortal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cPortalConfig_ObjectIdentity = ObjectIdentity
h3cPortalConfig = _H3cPortalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 1)
)
_H3cPortalMaxUserNumber_Type = Integer32
_H3cPortalMaxUserNumber_Object = MibScalar
h3cPortalMaxUserNumber = _H3cPortalMaxUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 1, 1),
    _H3cPortalMaxUserNumber_Type()
)
h3cPortalMaxUserNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPortalMaxUserNumber.setStatus("current")
_H3cPortalCurrentUserNumber_Type = Integer32
_H3cPortalCurrentUserNumber_Object = MibScalar
h3cPortalCurrentUserNumber = _H3cPortalCurrentUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 1, 2),
    _H3cPortalCurrentUserNumber_Type()
)
h3cPortalCurrentUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalCurrentUserNumber.setStatus("current")


class _H3cPortalStatus_Type(Integer32):
    """Custom type h3cPortalStatus based on Integer32"""
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


_H3cPortalStatus_Type.__name__ = "Integer32"
_H3cPortalStatus_Object = MibScalar
h3cPortalStatus = _H3cPortalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 1, 3),
    _H3cPortalStatus_Type()
)
h3cPortalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatus.setStatus("current")
_H3cPortalUserNumberUpperLimit_Type = Integer32
_H3cPortalUserNumberUpperLimit_Object = MibScalar
h3cPortalUserNumberUpperLimit = _H3cPortalUserNumberUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 1, 4),
    _H3cPortalUserNumberUpperLimit_Type()
)
h3cPortalUserNumberUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalUserNumberUpperLimit.setStatus("current")
_H3cPortalNasId_Type = OctetString
_H3cPortalNasId_Object = MibScalar
h3cPortalNasId = _H3cPortalNasId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 1, 5),
    _H3cPortalNasId_Type()
)
h3cPortalNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPortalNasId.setStatus("current")
_H3cPortalTables_ObjectIdentity = ObjectIdentity
h3cPortalTables = _H3cPortalTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2)
)
_H3cPortalServerTable_Object = MibTable
h3cPortalServerTable = _H3cPortalServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 1)
)
if mibBuilder.loadTexts:
    h3cPortalServerTable.setStatus("current")
_H3cPortalServerEntry_Object = MibTableRow
h3cPortalServerEntry = _H3cPortalServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 1, 1)
)
h3cPortalServerEntry.setIndexNames(
    (0, "H3C-PORTAL-MIB", "h3cPortalServerName"),
)
if mibBuilder.loadTexts:
    h3cPortalServerEntry.setStatus("current")


class _H3cPortalServerName_Type(OctetString):
    """Custom type h3cPortalServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cPortalServerName_Type.__name__ = "OctetString"
_H3cPortalServerName_Object = MibTableColumn
h3cPortalServerName = _H3cPortalServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 1, 1, 1),
    _H3cPortalServerName_Type()
)
h3cPortalServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPortalServerName.setStatus("current")


class _H3cPortalServerUrl_Type(OctetString):
    """Custom type h3cPortalServerUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_H3cPortalServerUrl_Type.__name__ = "OctetString"
_H3cPortalServerUrl_Object = MibTableColumn
h3cPortalServerUrl = _H3cPortalServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 1, 1, 2),
    _H3cPortalServerUrl_Type()
)
h3cPortalServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPortalServerUrl.setStatus("current")


class _H3cPortalServerPort_Type(Integer32):
    """Custom type h3cPortalServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_H3cPortalServerPort_Type.__name__ = "Integer32"
_H3cPortalServerPort_Object = MibTableColumn
h3cPortalServerPort = _H3cPortalServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 1, 1, 3),
    _H3cPortalServerPort_Type()
)
h3cPortalServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPortalServerPort.setStatus("current")
_H3cPortalIfInfoTable_Object = MibTable
h3cPortalIfInfoTable = _H3cPortalIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 2)
)
if mibBuilder.loadTexts:
    h3cPortalIfInfoTable.setStatus("current")
_H3cPortalIfInfoEntry_Object = MibTableRow
h3cPortalIfInfoEntry = _H3cPortalIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 2, 1)
)
h3cPortalIfInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cPortalIfInfoEntry.setStatus("current")
_H3cPortalAuthReqNumber_Type = Integer32
_H3cPortalAuthReqNumber_Object = MibTableColumn
h3cPortalAuthReqNumber = _H3cPortalAuthReqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 2, 1, 1),
    _H3cPortalAuthReqNumber_Type()
)
h3cPortalAuthReqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalAuthReqNumber.setStatus("current")
_H3cPortalAuthSuccNumber_Type = Integer32
_H3cPortalAuthSuccNumber_Object = MibTableColumn
h3cPortalAuthSuccNumber = _H3cPortalAuthSuccNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 2, 1, 2),
    _H3cPortalAuthSuccNumber_Type()
)
h3cPortalAuthSuccNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalAuthSuccNumber.setStatus("current")
_H3cPortalAuthFailNumber_Type = Integer32
_H3cPortalAuthFailNumber_Object = MibTableColumn
h3cPortalAuthFailNumber = _H3cPortalAuthFailNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 2, 1, 3),
    _H3cPortalAuthFailNumber_Type()
)
h3cPortalAuthFailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalAuthFailNumber.setStatus("current")
_H3cPortalIfServerTable_Object = MibTable
h3cPortalIfServerTable = _H3cPortalIfServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 3)
)
if mibBuilder.loadTexts:
    h3cPortalIfServerTable.setStatus("current")
_H3cPortalIfServerEntry_Object = MibTableRow
h3cPortalIfServerEntry = _H3cPortalIfServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 3, 1)
)
h3cPortalIfServerEntry.setIndexNames(
    (0, "H3C-PORTAL-MIB", "h3cPortalIfServerIndex"),
)
if mibBuilder.loadTexts:
    h3cPortalIfServerEntry.setStatus("current")


class _H3cPortalIfServerIndex_Type(Integer32):
    """Custom type h3cPortalIfServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cPortalIfServerIndex_Type.__name__ = "Integer32"
_H3cPortalIfServerIndex_Object = MibTableColumn
h3cPortalIfServerIndex = _H3cPortalIfServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 3, 1, 1),
    _H3cPortalIfServerIndex_Type()
)
h3cPortalIfServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPortalIfServerIndex.setStatus("current")
_H3cPortalIfServerUrl_Type = OctetString
_H3cPortalIfServerUrl_Object = MibTableColumn
h3cPortalIfServerUrl = _H3cPortalIfServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 3, 1, 2),
    _H3cPortalIfServerUrl_Type()
)
h3cPortalIfServerUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalIfServerUrl.setStatus("current")
_H3cPortalIfServerRowStatus_Type = RowStatus
_H3cPortalIfServerRowStatus_Object = MibTableColumn
h3cPortalIfServerRowStatus = _H3cPortalIfServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 3, 1, 3),
    _H3cPortalIfServerRowStatus_Type()
)
h3cPortalIfServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalIfServerRowStatus.setStatus("current")
_H3cPortalIfVlanNasIDTable_Object = MibTable
h3cPortalIfVlanNasIDTable = _H3cPortalIfVlanNasIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 4)
)
if mibBuilder.loadTexts:
    h3cPortalIfVlanNasIDTable.setStatus("current")
_H3cPortalIfVlanNasIDEntry_Object = MibTableRow
h3cPortalIfVlanNasIDEntry = _H3cPortalIfVlanNasIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 4, 1)
)
h3cPortalIfVlanNasIDEntry.setIndexNames(
    (0, "H3C-PORTAL-MIB", "h3cPortalIfVlanNasIDIfIndex"),
    (0, "H3C-PORTAL-MIB", "h3cPortalIfVlanNasIDVlanID"),
)
if mibBuilder.loadTexts:
    h3cPortalIfVlanNasIDEntry.setStatus("current")
_H3cPortalIfVlanNasIDIfIndex_Type = InterfaceIndex
_H3cPortalIfVlanNasIDIfIndex_Object = MibTableColumn
h3cPortalIfVlanNasIDIfIndex = _H3cPortalIfVlanNasIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 4, 1, 1),
    _H3cPortalIfVlanNasIDIfIndex_Type()
)
h3cPortalIfVlanNasIDIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPortalIfVlanNasIDIfIndex.setStatus("current")


class _H3cPortalIfVlanNasIDVlanID_Type(Integer32):
    """Custom type h3cPortalIfVlanNasIDVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cPortalIfVlanNasIDVlanID_Type.__name__ = "Integer32"
_H3cPortalIfVlanNasIDVlanID_Object = MibTableColumn
h3cPortalIfVlanNasIDVlanID = _H3cPortalIfVlanNasIDVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 4, 1, 2),
    _H3cPortalIfVlanNasIDVlanID_Type()
)
h3cPortalIfVlanNasIDVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPortalIfVlanNasIDVlanID.setStatus("current")


class _H3cPortalIfVlanNasIDNasID_Type(OctetString):
    """Custom type h3cPortalIfVlanNasIDNasID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cPortalIfVlanNasIDNasID_Type.__name__ = "OctetString"
_H3cPortalIfVlanNasIDNasID_Object = MibTableColumn
h3cPortalIfVlanNasIDNasID = _H3cPortalIfVlanNasIDNasID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 4, 1, 3),
    _H3cPortalIfVlanNasIDNasID_Type()
)
h3cPortalIfVlanNasIDNasID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalIfVlanNasIDNasID.setStatus("current")
_H3cPortalSSIDFreeRuleTable_Object = MibTable
h3cPortalSSIDFreeRuleTable = _H3cPortalSSIDFreeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 5)
)
if mibBuilder.loadTexts:
    h3cPortalSSIDFreeRuleTable.setStatus("current")
_H3cPortalSSIDFreeRuleEntry_Object = MibTableRow
h3cPortalSSIDFreeRuleEntry = _H3cPortalSSIDFreeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 5, 1)
)
h3cPortalSSIDFreeRuleEntry.setIndexNames(
    (0, "H3C-PORTAL-MIB", "h3cPortalSSIDFreeRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cPortalSSIDFreeRuleEntry.setStatus("current")


class _H3cPortalSSIDFreeRuleIndex_Type(Integer32):
    """Custom type h3cPortalSSIDFreeRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cPortalSSIDFreeRuleIndex_Type.__name__ = "Integer32"
_H3cPortalSSIDFreeRuleIndex_Object = MibTableColumn
h3cPortalSSIDFreeRuleIndex = _H3cPortalSSIDFreeRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 5, 1, 1),
    _H3cPortalSSIDFreeRuleIndex_Type()
)
h3cPortalSSIDFreeRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPortalSSIDFreeRuleIndex.setStatus("current")


class _H3cPortalSSIDFreeRuleSrcSSID_Type(OctetString):
    """Custom type h3cPortalSSIDFreeRuleSrcSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_H3cPortalSSIDFreeRuleSrcSSID_Type.__name__ = "OctetString"
_H3cPortalSSIDFreeRuleSrcSSID_Object = MibTableColumn
h3cPortalSSIDFreeRuleSrcSSID = _H3cPortalSSIDFreeRuleSrcSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 5, 1, 2),
    _H3cPortalSSIDFreeRuleSrcSSID_Type()
)
h3cPortalSSIDFreeRuleSrcSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalSSIDFreeRuleSrcSSID.setStatus("current")
_H3cPortalSSIDFreeRuleRowStatus_Type = RowStatus
_H3cPortalSSIDFreeRuleRowStatus_Object = MibTableColumn
h3cPortalSSIDFreeRuleRowStatus = _H3cPortalSSIDFreeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 5, 1, 3),
    _H3cPortalSSIDFreeRuleRowStatus_Type()
)
h3cPortalSSIDFreeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalSSIDFreeRuleRowStatus.setStatus("current")
_H3cPortalMacTriggerSrvTable_Object = MibTable
h3cPortalMacTriggerSrvTable = _H3cPortalMacTriggerSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 6)
)
if mibBuilder.loadTexts:
    h3cPortalMacTriggerSrvTable.setStatus("current")
_H3cPortalMacTriggerSrvEntry_Object = MibTableRow
h3cPortalMacTriggerSrvEntry = _H3cPortalMacTriggerSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 6, 1)
)
h3cPortalMacTriggerSrvEntry.setIndexNames(
    (0, "H3C-PORTAL-MIB", "h3cPortalMacTriggerSrvIndex"),
)
if mibBuilder.loadTexts:
    h3cPortalMacTriggerSrvEntry.setStatus("current")


class _H3cPortalMacTriggerSrvIndex_Type(Integer32):
    """Custom type h3cPortalMacTriggerSrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cPortalMacTriggerSrvIndex_Type.__name__ = "Integer32"
_H3cPortalMacTriggerSrvIndex_Object = MibTableColumn
h3cPortalMacTriggerSrvIndex = _H3cPortalMacTriggerSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 6, 1, 1),
    _H3cPortalMacTriggerSrvIndex_Type()
)
h3cPortalMacTriggerSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPortalMacTriggerSrvIndex.setStatus("current")
_H3cPortalMacTriggerSrvIPAddrType_Type = InetAddressType
_H3cPortalMacTriggerSrvIPAddrType_Object = MibTableColumn
h3cPortalMacTriggerSrvIPAddrType = _H3cPortalMacTriggerSrvIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 6, 1, 2),
    _H3cPortalMacTriggerSrvIPAddrType_Type()
)
h3cPortalMacTriggerSrvIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalMacTriggerSrvIPAddrType.setStatus("current")
_H3cPortalMacTriggerSrvIP_Type = InetAddress
_H3cPortalMacTriggerSrvIP_Object = MibTableColumn
h3cPortalMacTriggerSrvIP = _H3cPortalMacTriggerSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 6, 1, 3),
    _H3cPortalMacTriggerSrvIP_Type()
)
h3cPortalMacTriggerSrvIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalMacTriggerSrvIP.setStatus("current")


class _H3cPortalMacTriggerSrvPort_Type(Integer32):
    """Custom type h3cPortalMacTriggerSrvPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_H3cPortalMacTriggerSrvPort_Type.__name__ = "Integer32"
_H3cPortalMacTriggerSrvPort_Object = MibTableColumn
h3cPortalMacTriggerSrvPort = _H3cPortalMacTriggerSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 6, 1, 4),
    _H3cPortalMacTriggerSrvPort_Type()
)
h3cPortalMacTriggerSrvPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalMacTriggerSrvPort.setStatus("current")
_H3cPortalMacTriggerSrvRowStatus_Type = RowStatus
_H3cPortalMacTriggerSrvRowStatus_Object = MibTableColumn
h3cPortalMacTriggerSrvRowStatus = _H3cPortalMacTriggerSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 6, 1, 5),
    _H3cPortalMacTriggerSrvRowStatus_Type()
)
h3cPortalMacTriggerSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalMacTriggerSrvRowStatus.setStatus("current")
_H3cPortalMacTriggerOnIfTable_Object = MibTable
h3cPortalMacTriggerOnIfTable = _H3cPortalMacTriggerOnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 7)
)
if mibBuilder.loadTexts:
    h3cPortalMacTriggerOnIfTable.setStatus("current")
_H3cPortalMacTriggerOnIfEntry_Object = MibTableRow
h3cPortalMacTriggerOnIfEntry = _H3cPortalMacTriggerOnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 7, 1)
)
h3cPortalMacTriggerOnIfEntry.setIndexNames(
    (0, "H3C-PORTAL-MIB", "h3cPortalMacTriggerOnIfIfIndex"),
)
if mibBuilder.loadTexts:
    h3cPortalMacTriggerOnIfEntry.setStatus("current")
_H3cPortalMacTriggerOnIfIfIndex_Type = InterfaceIndex
_H3cPortalMacTriggerOnIfIfIndex_Object = MibTableColumn
h3cPortalMacTriggerOnIfIfIndex = _H3cPortalMacTriggerOnIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 7, 1, 1),
    _H3cPortalMacTriggerOnIfIfIndex_Type()
)
h3cPortalMacTriggerOnIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPortalMacTriggerOnIfIfIndex.setStatus("current")
_H3cPortalMacTriggerOnIfDetctFlowPeriod_Type = Integer32
_H3cPortalMacTriggerOnIfDetctFlowPeriod_Object = MibTableColumn
h3cPortalMacTriggerOnIfDetctFlowPeriod = _H3cPortalMacTriggerOnIfDetctFlowPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 7, 1, 2),
    _H3cPortalMacTriggerOnIfDetctFlowPeriod_Type()
)
h3cPortalMacTriggerOnIfDetctFlowPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalMacTriggerOnIfDetctFlowPeriod.setStatus("current")
_H3cPortalMacTriggerOnIfThresholdFlow_Type = Unsigned32
_H3cPortalMacTriggerOnIfThresholdFlow_Object = MibTableColumn
h3cPortalMacTriggerOnIfThresholdFlow = _H3cPortalMacTriggerOnIfThresholdFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 7, 1, 3),
    _H3cPortalMacTriggerOnIfThresholdFlow_Type()
)
h3cPortalMacTriggerOnIfThresholdFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalMacTriggerOnIfThresholdFlow.setStatus("current")
_H3cPortalMacTriggerOnIfRowStatus_Type = RowStatus
_H3cPortalMacTriggerOnIfRowStatus_Object = MibTableColumn
h3cPortalMacTriggerOnIfRowStatus = _H3cPortalMacTriggerOnIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 7, 1, 4),
    _H3cPortalMacTriggerOnIfRowStatus_Type()
)
h3cPortalMacTriggerOnIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalMacTriggerOnIfRowStatus.setStatus("current")
_H3cPortalFreeRuleTable_Object = MibTable
h3cPortalFreeRuleTable = _H3cPortalFreeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8)
)
if mibBuilder.loadTexts:
    h3cPortalFreeRuleTable.setStatus("current")
_H3cPortalFreeRuleEntry_Object = MibTableRow
h3cPortalFreeRuleEntry = _H3cPortalFreeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1)
)
h3cPortalFreeRuleEntry.setIndexNames(
    (0, "H3C-PORTAL-MIB", "h3cPortalFreeRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cPortalFreeRuleEntry.setStatus("current")


class _H3cPortalFreeRuleIndex_Type(Integer32):
    """Custom type h3cPortalFreeRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cPortalFreeRuleIndex_Type.__name__ = "Integer32"
_H3cPortalFreeRuleIndex_Object = MibTableColumn
h3cPortalFreeRuleIndex = _H3cPortalFreeRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 1),
    _H3cPortalFreeRuleIndex_Type()
)
h3cPortalFreeRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleIndex.setStatus("current")
_H3cPortalFreeRuleSrcIfIndex_Type = InterfaceIndex
_H3cPortalFreeRuleSrcIfIndex_Object = MibTableColumn
h3cPortalFreeRuleSrcIfIndex = _H3cPortalFreeRuleSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 2),
    _H3cPortalFreeRuleSrcIfIndex_Type()
)
h3cPortalFreeRuleSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleSrcIfIndex.setStatus("current")
_H3cPortalFreeRuleSrcVlanID_Type = Integer32
_H3cPortalFreeRuleSrcVlanID_Object = MibTableColumn
h3cPortalFreeRuleSrcVlanID = _H3cPortalFreeRuleSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 3),
    _H3cPortalFreeRuleSrcVlanID_Type()
)
h3cPortalFreeRuleSrcVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleSrcVlanID.setStatus("current")
_H3cPortalFreeRuleSrcMac_Type = MacAddress
_H3cPortalFreeRuleSrcMac_Object = MibTableColumn
h3cPortalFreeRuleSrcMac = _H3cPortalFreeRuleSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 4),
    _H3cPortalFreeRuleSrcMac_Type()
)
h3cPortalFreeRuleSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleSrcMac.setStatus("current")
_H3cPortalFreeRuleAddrType_Type = InetAddressType
_H3cPortalFreeRuleAddrType_Object = MibTableColumn
h3cPortalFreeRuleAddrType = _H3cPortalFreeRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 5),
    _H3cPortalFreeRuleAddrType_Type()
)
h3cPortalFreeRuleAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleAddrType.setStatus("current")
_H3cPortalFreeRuleSrcAddr_Type = InetAddress
_H3cPortalFreeRuleSrcAddr_Object = MibTableColumn
h3cPortalFreeRuleSrcAddr = _H3cPortalFreeRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 6),
    _H3cPortalFreeRuleSrcAddr_Type()
)
h3cPortalFreeRuleSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleSrcAddr.setStatus("current")
_H3cPortalFreeRuleSrcPrefix_Type = InetAddressPrefixLength
_H3cPortalFreeRuleSrcPrefix_Object = MibTableColumn
h3cPortalFreeRuleSrcPrefix = _H3cPortalFreeRuleSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 7),
    _H3cPortalFreeRuleSrcPrefix_Type()
)
h3cPortalFreeRuleSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleSrcPrefix.setStatus("current")
_H3cPortalFreeRuleDstAddr_Type = InetAddress
_H3cPortalFreeRuleDstAddr_Object = MibTableColumn
h3cPortalFreeRuleDstAddr = _H3cPortalFreeRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 8),
    _H3cPortalFreeRuleDstAddr_Type()
)
h3cPortalFreeRuleDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleDstAddr.setStatus("current")
_H3cPortalFreeRuleDstPrefix_Type = InetAddressPrefixLength
_H3cPortalFreeRuleDstPrefix_Object = MibTableColumn
h3cPortalFreeRuleDstPrefix = _H3cPortalFreeRuleDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 9),
    _H3cPortalFreeRuleDstPrefix_Type()
)
h3cPortalFreeRuleDstPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleDstPrefix.setStatus("current")


class _H3cPortalFreeRuleProtocol_Type(Integer32):
    """Custom type h3cPortalFreeRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_H3cPortalFreeRuleProtocol_Type.__name__ = "Integer32"
_H3cPortalFreeRuleProtocol_Object = MibTableColumn
h3cPortalFreeRuleProtocol = _H3cPortalFreeRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 10),
    _H3cPortalFreeRuleProtocol_Type()
)
h3cPortalFreeRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleProtocol.setStatus("current")
_H3cPortalFreeRuleSrcPort_Type = Integer32
_H3cPortalFreeRuleSrcPort_Object = MibTableColumn
h3cPortalFreeRuleSrcPort = _H3cPortalFreeRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 11),
    _H3cPortalFreeRuleSrcPort_Type()
)
h3cPortalFreeRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleSrcPort.setStatus("current")
_H3cPortalFreeRuleDstPort_Type = Integer32
_H3cPortalFreeRuleDstPort_Object = MibTableColumn
h3cPortalFreeRuleDstPort = _H3cPortalFreeRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 12),
    _H3cPortalFreeRuleDstPort_Type()
)
h3cPortalFreeRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleDstPort.setStatus("current")
_H3cPortalFreeRuleRowStatus_Type = RowStatus
_H3cPortalFreeRuleRowStatus_Object = MibTableColumn
h3cPortalFreeRuleRowStatus = _H3cPortalFreeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 8, 1, 13),
    _H3cPortalFreeRuleRowStatus_Type()
)
h3cPortalFreeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalFreeRuleRowStatus.setStatus("current")
_H3cPortalForbiddenRuleTable_Object = MibTable
h3cPortalForbiddenRuleTable = _H3cPortalForbiddenRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9)
)
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleTable.setStatus("current")
_H3cPortalForbiddenRuleEntry_Object = MibTableRow
h3cPortalForbiddenRuleEntry = _H3cPortalForbiddenRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1)
)
h3cPortalForbiddenRuleEntry.setIndexNames(
    (0, "H3C-PORTAL-MIB", "h3cPortalForbiddenRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleEntry.setStatus("current")


class _H3cPortalForbiddenRuleIndex_Type(Integer32):
    """Custom type h3cPortalForbiddenRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cPortalForbiddenRuleIndex_Type.__name__ = "Integer32"
_H3cPortalForbiddenRuleIndex_Object = MibTableColumn
h3cPortalForbiddenRuleIndex = _H3cPortalForbiddenRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 1),
    _H3cPortalForbiddenRuleIndex_Type()
)
h3cPortalForbiddenRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleIndex.setStatus("current")
_H3cPortalForbiddenRuleSrcIfIndex_Type = InterfaceIndex
_H3cPortalForbiddenRuleSrcIfIndex_Object = MibTableColumn
h3cPortalForbiddenRuleSrcIfIndex = _H3cPortalForbiddenRuleSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 2),
    _H3cPortalForbiddenRuleSrcIfIndex_Type()
)
h3cPortalForbiddenRuleSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleSrcIfIndex.setStatus("current")
_H3cPortalForbiddenRuleSrcVlanID_Type = Integer32
_H3cPortalForbiddenRuleSrcVlanID_Object = MibTableColumn
h3cPortalForbiddenRuleSrcVlanID = _H3cPortalForbiddenRuleSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 3),
    _H3cPortalForbiddenRuleSrcVlanID_Type()
)
h3cPortalForbiddenRuleSrcVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleSrcVlanID.setStatus("current")
_H3cPortalForbiddenRuleSrcMac_Type = MacAddress
_H3cPortalForbiddenRuleSrcMac_Object = MibTableColumn
h3cPortalForbiddenRuleSrcMac = _H3cPortalForbiddenRuleSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 4),
    _H3cPortalForbiddenRuleSrcMac_Type()
)
h3cPortalForbiddenRuleSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleSrcMac.setStatus("current")
_H3cPortalForbiddenRuleAddrType_Type = InetAddressType
_H3cPortalForbiddenRuleAddrType_Object = MibTableColumn
h3cPortalForbiddenRuleAddrType = _H3cPortalForbiddenRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 5),
    _H3cPortalForbiddenRuleAddrType_Type()
)
h3cPortalForbiddenRuleAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleAddrType.setStatus("current")
_H3cPortalForbiddenRuleSrcAddr_Type = InetAddress
_H3cPortalForbiddenRuleSrcAddr_Object = MibTableColumn
h3cPortalForbiddenRuleSrcAddr = _H3cPortalForbiddenRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 6),
    _H3cPortalForbiddenRuleSrcAddr_Type()
)
h3cPortalForbiddenRuleSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleSrcAddr.setStatus("current")
_H3cPortalForbiddenRuleSrcPrefix_Type = InetAddressPrefixLength
_H3cPortalForbiddenRuleSrcPrefix_Object = MibTableColumn
h3cPortalForbiddenRuleSrcPrefix = _H3cPortalForbiddenRuleSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 7),
    _H3cPortalForbiddenRuleSrcPrefix_Type()
)
h3cPortalForbiddenRuleSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleSrcPrefix.setStatus("current")
_H3cPortalForbiddenRuleDstAddr_Type = InetAddress
_H3cPortalForbiddenRuleDstAddr_Object = MibTableColumn
h3cPortalForbiddenRuleDstAddr = _H3cPortalForbiddenRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 8),
    _H3cPortalForbiddenRuleDstAddr_Type()
)
h3cPortalForbiddenRuleDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleDstAddr.setStatus("current")
_H3cPortalForbiddenRuleDstPrefix_Type = InetAddressPrefixLength
_H3cPortalForbiddenRuleDstPrefix_Object = MibTableColumn
h3cPortalForbiddenRuleDstPrefix = _H3cPortalForbiddenRuleDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 9),
    _H3cPortalForbiddenRuleDstPrefix_Type()
)
h3cPortalForbiddenRuleDstPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleDstPrefix.setStatus("current")


class _H3cPortalForbiddenRuleProtocol_Type(Integer32):
    """Custom type h3cPortalForbiddenRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_H3cPortalForbiddenRuleProtocol_Type.__name__ = "Integer32"
_H3cPortalForbiddenRuleProtocol_Object = MibTableColumn
h3cPortalForbiddenRuleProtocol = _H3cPortalForbiddenRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 10),
    _H3cPortalForbiddenRuleProtocol_Type()
)
h3cPortalForbiddenRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleProtocol.setStatus("current")
_H3cPortalForbiddenRuleSrcPort_Type = Integer32
_H3cPortalForbiddenRuleSrcPort_Object = MibTableColumn
h3cPortalForbiddenRuleSrcPort = _H3cPortalForbiddenRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 11),
    _H3cPortalForbiddenRuleSrcPort_Type()
)
h3cPortalForbiddenRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleSrcPort.setStatus("current")
_H3cPortalForbiddenRuleDstPort_Type = Integer32
_H3cPortalForbiddenRuleDstPort_Object = MibTableColumn
h3cPortalForbiddenRuleDstPort = _H3cPortalForbiddenRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 12),
    _H3cPortalForbiddenRuleDstPort_Type()
)
h3cPortalForbiddenRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleDstPort.setStatus("current")
_H3cPortalForbiddenRuleRowStatus_Type = RowStatus
_H3cPortalForbiddenRuleRowStatus_Object = MibTableColumn
h3cPortalForbiddenRuleRowStatus = _H3cPortalForbiddenRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 2, 9, 1, 13),
    _H3cPortalForbiddenRuleRowStatus_Type()
)
h3cPortalForbiddenRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPortalForbiddenRuleRowStatus.setStatus("current")
_H3cPortalTraps_ObjectIdentity = ObjectIdentity
h3cPortalTraps = _H3cPortalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 3)
)
_H3cPortalTrapPrefix_ObjectIdentity = ObjectIdentity
h3cPortalTrapPrefix = _H3cPortalTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 3, 0)
)
_H3cPortalTrapVarObjects_ObjectIdentity = ObjectIdentity
h3cPortalTrapVarObjects = _H3cPortalTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 3, 1)
)
_H3cPortalFirstTrapTime_Type = TimeTicks
_H3cPortalFirstTrapTime_Object = MibScalar
h3cPortalFirstTrapTime = _H3cPortalFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 3, 1, 1),
    _H3cPortalFirstTrapTime_Type()
)
h3cPortalFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPortalFirstTrapTime.setStatus("current")
_H3cPortalStatistic_ObjectIdentity = ObjectIdentity
h3cPortalStatistic = _H3cPortalStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4)
)
_H3cPortalStatAuthReq_Type = Counter64
_H3cPortalStatAuthReq_Object = MibScalar
h3cPortalStatAuthReq = _H3cPortalStatAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 1),
    _H3cPortalStatAuthReq_Type()
)
h3cPortalStatAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatAuthReq.setStatus("current")
_H3cPortalStatAckLogout_Type = Counter64
_H3cPortalStatAckLogout_Object = MibScalar
h3cPortalStatAckLogout = _H3cPortalStatAckLogout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 2),
    _H3cPortalStatAckLogout_Type()
)
h3cPortalStatAckLogout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatAckLogout.setStatus("current")
_H3cPortalStatNotifyLogout_Type = Counter64
_H3cPortalStatNotifyLogout_Object = MibScalar
h3cPortalStatNotifyLogout = _H3cPortalStatNotifyLogout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 3),
    _H3cPortalStatNotifyLogout_Type()
)
h3cPortalStatNotifyLogout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatNotifyLogout.setStatus("current")
_H3cPortalStatChallengeTimeout_Type = Counter64
_H3cPortalStatChallengeTimeout_Object = MibScalar
h3cPortalStatChallengeTimeout = _H3cPortalStatChallengeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 4),
    _H3cPortalStatChallengeTimeout_Type()
)
h3cPortalStatChallengeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatChallengeTimeout.setStatus("current")
_H3cPortalStatChallengeBusy_Type = Counter64
_H3cPortalStatChallengeBusy_Object = MibScalar
h3cPortalStatChallengeBusy = _H3cPortalStatChallengeBusy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 5),
    _H3cPortalStatChallengeBusy_Type()
)
h3cPortalStatChallengeBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatChallengeBusy.setStatus("current")
_H3cPortalStatChallengeFail_Type = Counter64
_H3cPortalStatChallengeFail_Object = MibScalar
h3cPortalStatChallengeFail = _H3cPortalStatChallengeFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 6),
    _H3cPortalStatChallengeFail_Type()
)
h3cPortalStatChallengeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatChallengeFail.setStatus("current")
_H3cPortalStatAuthTimeout_Type = Counter64
_H3cPortalStatAuthTimeout_Object = MibScalar
h3cPortalStatAuthTimeout = _H3cPortalStatAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 7),
    _H3cPortalStatAuthTimeout_Type()
)
h3cPortalStatAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatAuthTimeout.setStatus("current")
_H3cPortalStatAuthFail_Type = Counter64
_H3cPortalStatAuthFail_Object = MibScalar
h3cPortalStatAuthFail = _H3cPortalStatAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 8),
    _H3cPortalStatAuthFail_Type()
)
h3cPortalStatAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatAuthFail.setStatus("current")
_H3cPortalStatPwdError_Type = Counter64
_H3cPortalStatPwdError_Object = MibScalar
h3cPortalStatPwdError = _H3cPortalStatPwdError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 9),
    _H3cPortalStatPwdError_Type()
)
h3cPortalStatPwdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatPwdError.setStatus("current")
_H3cPortalStatAuthBusy_Type = Counter64
_H3cPortalStatAuthBusy_Object = MibScalar
h3cPortalStatAuthBusy = _H3cPortalStatAuthBusy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 10),
    _H3cPortalStatAuthBusy_Type()
)
h3cPortalStatAuthBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatAuthBusy.setStatus("current")
_H3cPortalStatAuthDisordered_Type = Counter64
_H3cPortalStatAuthDisordered_Object = MibScalar
h3cPortalStatAuthDisordered = _H3cPortalStatAuthDisordered_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 11),
    _H3cPortalStatAuthDisordered_Type()
)
h3cPortalStatAuthDisordered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatAuthDisordered.setStatus("current")
_H3cPortalStatAuthUnknownError_Type = Counter64
_H3cPortalStatAuthUnknownError_Object = MibScalar
h3cPortalStatAuthUnknownError = _H3cPortalStatAuthUnknownError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 12),
    _H3cPortalStatAuthUnknownError_Type()
)
h3cPortalStatAuthUnknownError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatAuthUnknownError.setStatus("current")
_H3cPortalStatAuthResp_Type = Counter64
_H3cPortalStatAuthResp_Object = MibScalar
h3cPortalStatAuthResp = _H3cPortalStatAuthResp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 13),
    _H3cPortalStatAuthResp_Type()
)
h3cPortalStatAuthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatAuthResp.setStatus("current")
_H3cPortalStatChallengeReq_Type = Counter64
_H3cPortalStatChallengeReq_Object = MibScalar
h3cPortalStatChallengeReq = _H3cPortalStatChallengeReq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 14),
    _H3cPortalStatChallengeReq_Type()
)
h3cPortalStatChallengeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatChallengeReq.setStatus("current")
_H3cPortalStatChallengeResp_Type = Counter64
_H3cPortalStatChallengeResp_Object = MibScalar
h3cPortalStatChallengeResp = _H3cPortalStatChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 4, 15),
    _H3cPortalStatChallengeResp_Type()
)
h3cPortalStatChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalStatChallengeResp.setStatus("current")
_H3cPortalPktStatistic_ObjectIdentity = ObjectIdentity
h3cPortalPktStatistic = _H3cPortalPktStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5)
)
_H3cPortalPktStaReqAuthNum_Type = Counter64
_H3cPortalPktStaReqAuthNum_Object = MibScalar
h3cPortalPktStaReqAuthNum = _H3cPortalPktStaReqAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 1),
    _H3cPortalPktStaReqAuthNum_Type()
)
h3cPortalPktStaReqAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaReqAuthNum.setStatus("current")
_H3cPortalPktStaAckAuthSuccess_Type = Counter64
_H3cPortalPktStaAckAuthSuccess_Object = MibScalar
h3cPortalPktStaAckAuthSuccess = _H3cPortalPktStaAckAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 2),
    _H3cPortalPktStaAckAuthSuccess_Type()
)
h3cPortalPktStaAckAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckAuthSuccess.setStatus("current")
_H3cPortalPktStaAckAuthReject_Type = Counter64
_H3cPortalPktStaAckAuthReject_Object = MibScalar
h3cPortalPktStaAckAuthReject = _H3cPortalPktStaAckAuthReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 3),
    _H3cPortalPktStaAckAuthReject_Type()
)
h3cPortalPktStaAckAuthReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckAuthReject.setStatus("current")
_H3cPortalPktStaAckAuthEstablish_Type = Counter64
_H3cPortalPktStaAckAuthEstablish_Object = MibScalar
h3cPortalPktStaAckAuthEstablish = _H3cPortalPktStaAckAuthEstablish_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 4),
    _H3cPortalPktStaAckAuthEstablish_Type()
)
h3cPortalPktStaAckAuthEstablish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckAuthEstablish.setStatus("current")
_H3cPortalPktStaAckAuthBusy_Type = Counter64
_H3cPortalPktStaAckAuthBusy_Object = MibScalar
h3cPortalPktStaAckAuthBusy = _H3cPortalPktStaAckAuthBusy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 5),
    _H3cPortalPktStaAckAuthBusy_Type()
)
h3cPortalPktStaAckAuthBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckAuthBusy.setStatus("current")
_H3cPortalPktStaAckAuthAuthFail_Type = Counter64
_H3cPortalPktStaAckAuthAuthFail_Object = MibScalar
h3cPortalPktStaAckAuthAuthFail = _H3cPortalPktStaAckAuthAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 6),
    _H3cPortalPktStaAckAuthAuthFail_Type()
)
h3cPortalPktStaAckAuthAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckAuthAuthFail.setStatus("current")
_H3cPortalPktStaReqChallengeNum_Type = Counter64
_H3cPortalPktStaReqChallengeNum_Object = MibScalar
h3cPortalPktStaReqChallengeNum = _H3cPortalPktStaReqChallengeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 7),
    _H3cPortalPktStaReqChallengeNum_Type()
)
h3cPortalPktStaReqChallengeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaReqChallengeNum.setStatus("current")
_H3cPortalPktStaAckChallengeSuccess_Type = Counter64
_H3cPortalPktStaAckChallengeSuccess_Object = MibScalar
h3cPortalPktStaAckChallengeSuccess = _H3cPortalPktStaAckChallengeSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 8),
    _H3cPortalPktStaAckChallengeSuccess_Type()
)
h3cPortalPktStaAckChallengeSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckChallengeSuccess.setStatus("current")
_H3cPortalPktStaAckChallengeReject_Type = Counter64
_H3cPortalPktStaAckChallengeReject_Object = MibScalar
h3cPortalPktStaAckChallengeReject = _H3cPortalPktStaAckChallengeReject_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 9),
    _H3cPortalPktStaAckChallengeReject_Type()
)
h3cPortalPktStaAckChallengeReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckChallengeReject.setStatus("current")
_H3cPortalPktStaAckChallengeEstablish_Type = Counter64
_H3cPortalPktStaAckChallengeEstablish_Object = MibScalar
h3cPortalPktStaAckChallengeEstablish = _H3cPortalPktStaAckChallengeEstablish_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 10),
    _H3cPortalPktStaAckChallengeEstablish_Type()
)
h3cPortalPktStaAckChallengeEstablish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckChallengeEstablish.setStatus("current")
_H3cPortalPktStaAckChallengeBusy_Type = Counter64
_H3cPortalPktStaAckChallengeBusy_Object = MibScalar
h3cPortalPktStaAckChallengeBusy = _H3cPortalPktStaAckChallengeBusy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 11),
    _H3cPortalPktStaAckChallengeBusy_Type()
)
h3cPortalPktStaAckChallengeBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckChallengeBusy.setStatus("current")
_H3cPortalPktStaAckChallengeAuthFail_Type = Counter64
_H3cPortalPktStaAckChallengeAuthFail_Object = MibScalar
h3cPortalPktStaAckChallengeAuthFail = _H3cPortalPktStaAckChallengeAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 5, 12),
    _H3cPortalPktStaAckChallengeAuthFail_Type()
)
h3cPortalPktStaAckChallengeAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPortalPktStaAckChallengeAuthFail.setStatus("current")

# Managed Objects groups


# Notification objects

h3cPortalServerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 3, 0, 1)
)
h3cPortalServerLost.setObjects(
      *(("H3C-PORTAL-MIB", "h3cPortalServerName"),
        ("H3C-PORTAL-MIB", "h3cPortalFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cPortalServerLost.setStatus(
        "current"
    )

h3cPortalServerGet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 99, 3, 0, 2)
)
h3cPortalServerGet.setObjects(
      *(("H3C-PORTAL-MIB", "h3cPortalServerName"),
        ("H3C-PORTAL-MIB", "h3cPortalFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cPortalServerGet.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-PORTAL-MIB",
    **{"h3cPortal": h3cPortal,
       "h3cPortalConfig": h3cPortalConfig,
       "h3cPortalMaxUserNumber": h3cPortalMaxUserNumber,
       "h3cPortalCurrentUserNumber": h3cPortalCurrentUserNumber,
       "h3cPortalStatus": h3cPortalStatus,
       "h3cPortalUserNumberUpperLimit": h3cPortalUserNumberUpperLimit,
       "h3cPortalNasId": h3cPortalNasId,
       "h3cPortalTables": h3cPortalTables,
       "h3cPortalServerTable": h3cPortalServerTable,
       "h3cPortalServerEntry": h3cPortalServerEntry,
       "h3cPortalServerName": h3cPortalServerName,
       "h3cPortalServerUrl": h3cPortalServerUrl,
       "h3cPortalServerPort": h3cPortalServerPort,
       "h3cPortalIfInfoTable": h3cPortalIfInfoTable,
       "h3cPortalIfInfoEntry": h3cPortalIfInfoEntry,
       "h3cPortalAuthReqNumber": h3cPortalAuthReqNumber,
       "h3cPortalAuthSuccNumber": h3cPortalAuthSuccNumber,
       "h3cPortalAuthFailNumber": h3cPortalAuthFailNumber,
       "h3cPortalIfServerTable": h3cPortalIfServerTable,
       "h3cPortalIfServerEntry": h3cPortalIfServerEntry,
       "h3cPortalIfServerIndex": h3cPortalIfServerIndex,
       "h3cPortalIfServerUrl": h3cPortalIfServerUrl,
       "h3cPortalIfServerRowStatus": h3cPortalIfServerRowStatus,
       "h3cPortalIfVlanNasIDTable": h3cPortalIfVlanNasIDTable,
       "h3cPortalIfVlanNasIDEntry": h3cPortalIfVlanNasIDEntry,
       "h3cPortalIfVlanNasIDIfIndex": h3cPortalIfVlanNasIDIfIndex,
       "h3cPortalIfVlanNasIDVlanID": h3cPortalIfVlanNasIDVlanID,
       "h3cPortalIfVlanNasIDNasID": h3cPortalIfVlanNasIDNasID,
       "h3cPortalSSIDFreeRuleTable": h3cPortalSSIDFreeRuleTable,
       "h3cPortalSSIDFreeRuleEntry": h3cPortalSSIDFreeRuleEntry,
       "h3cPortalSSIDFreeRuleIndex": h3cPortalSSIDFreeRuleIndex,
       "h3cPortalSSIDFreeRuleSrcSSID": h3cPortalSSIDFreeRuleSrcSSID,
       "h3cPortalSSIDFreeRuleRowStatus": h3cPortalSSIDFreeRuleRowStatus,
       "h3cPortalMacTriggerSrvTable": h3cPortalMacTriggerSrvTable,
       "h3cPortalMacTriggerSrvEntry": h3cPortalMacTriggerSrvEntry,
       "h3cPortalMacTriggerSrvIndex": h3cPortalMacTriggerSrvIndex,
       "h3cPortalMacTriggerSrvIPAddrType": h3cPortalMacTriggerSrvIPAddrType,
       "h3cPortalMacTriggerSrvIP": h3cPortalMacTriggerSrvIP,
       "h3cPortalMacTriggerSrvPort": h3cPortalMacTriggerSrvPort,
       "h3cPortalMacTriggerSrvRowStatus": h3cPortalMacTriggerSrvRowStatus,
       "h3cPortalMacTriggerOnIfTable": h3cPortalMacTriggerOnIfTable,
       "h3cPortalMacTriggerOnIfEntry": h3cPortalMacTriggerOnIfEntry,
       "h3cPortalMacTriggerOnIfIfIndex": h3cPortalMacTriggerOnIfIfIndex,
       "h3cPortalMacTriggerOnIfDetctFlowPeriod": h3cPortalMacTriggerOnIfDetctFlowPeriod,
       "h3cPortalMacTriggerOnIfThresholdFlow": h3cPortalMacTriggerOnIfThresholdFlow,
       "h3cPortalMacTriggerOnIfRowStatus": h3cPortalMacTriggerOnIfRowStatus,
       "h3cPortalFreeRuleTable": h3cPortalFreeRuleTable,
       "h3cPortalFreeRuleEntry": h3cPortalFreeRuleEntry,
       "h3cPortalFreeRuleIndex": h3cPortalFreeRuleIndex,
       "h3cPortalFreeRuleSrcIfIndex": h3cPortalFreeRuleSrcIfIndex,
       "h3cPortalFreeRuleSrcVlanID": h3cPortalFreeRuleSrcVlanID,
       "h3cPortalFreeRuleSrcMac": h3cPortalFreeRuleSrcMac,
       "h3cPortalFreeRuleAddrType": h3cPortalFreeRuleAddrType,
       "h3cPortalFreeRuleSrcAddr": h3cPortalFreeRuleSrcAddr,
       "h3cPortalFreeRuleSrcPrefix": h3cPortalFreeRuleSrcPrefix,
       "h3cPortalFreeRuleDstAddr": h3cPortalFreeRuleDstAddr,
       "h3cPortalFreeRuleDstPrefix": h3cPortalFreeRuleDstPrefix,
       "h3cPortalFreeRuleProtocol": h3cPortalFreeRuleProtocol,
       "h3cPortalFreeRuleSrcPort": h3cPortalFreeRuleSrcPort,
       "h3cPortalFreeRuleDstPort": h3cPortalFreeRuleDstPort,
       "h3cPortalFreeRuleRowStatus": h3cPortalFreeRuleRowStatus,
       "h3cPortalForbiddenRuleTable": h3cPortalForbiddenRuleTable,
       "h3cPortalForbiddenRuleEntry": h3cPortalForbiddenRuleEntry,
       "h3cPortalForbiddenRuleIndex": h3cPortalForbiddenRuleIndex,
       "h3cPortalForbiddenRuleSrcIfIndex": h3cPortalForbiddenRuleSrcIfIndex,
       "h3cPortalForbiddenRuleSrcVlanID": h3cPortalForbiddenRuleSrcVlanID,
       "h3cPortalForbiddenRuleSrcMac": h3cPortalForbiddenRuleSrcMac,
       "h3cPortalForbiddenRuleAddrType": h3cPortalForbiddenRuleAddrType,
       "h3cPortalForbiddenRuleSrcAddr": h3cPortalForbiddenRuleSrcAddr,
       "h3cPortalForbiddenRuleSrcPrefix": h3cPortalForbiddenRuleSrcPrefix,
       "h3cPortalForbiddenRuleDstAddr": h3cPortalForbiddenRuleDstAddr,
       "h3cPortalForbiddenRuleDstPrefix": h3cPortalForbiddenRuleDstPrefix,
       "h3cPortalForbiddenRuleProtocol": h3cPortalForbiddenRuleProtocol,
       "h3cPortalForbiddenRuleSrcPort": h3cPortalForbiddenRuleSrcPort,
       "h3cPortalForbiddenRuleDstPort": h3cPortalForbiddenRuleDstPort,
       "h3cPortalForbiddenRuleRowStatus": h3cPortalForbiddenRuleRowStatus,
       "h3cPortalTraps": h3cPortalTraps,
       "h3cPortalTrapPrefix": h3cPortalTrapPrefix,
       "h3cPortalServerLost": h3cPortalServerLost,
       "h3cPortalServerGet": h3cPortalServerGet,
       "h3cPortalTrapVarObjects": h3cPortalTrapVarObjects,
       "h3cPortalFirstTrapTime": h3cPortalFirstTrapTime,
       "h3cPortalStatistic": h3cPortalStatistic,
       "h3cPortalStatAuthReq": h3cPortalStatAuthReq,
       "h3cPortalStatAckLogout": h3cPortalStatAckLogout,
       "h3cPortalStatNotifyLogout": h3cPortalStatNotifyLogout,
       "h3cPortalStatChallengeTimeout": h3cPortalStatChallengeTimeout,
       "h3cPortalStatChallengeBusy": h3cPortalStatChallengeBusy,
       "h3cPortalStatChallengeFail": h3cPortalStatChallengeFail,
       "h3cPortalStatAuthTimeout": h3cPortalStatAuthTimeout,
       "h3cPortalStatAuthFail": h3cPortalStatAuthFail,
       "h3cPortalStatPwdError": h3cPortalStatPwdError,
       "h3cPortalStatAuthBusy": h3cPortalStatAuthBusy,
       "h3cPortalStatAuthDisordered": h3cPortalStatAuthDisordered,
       "h3cPortalStatAuthUnknownError": h3cPortalStatAuthUnknownError,
       "h3cPortalStatAuthResp": h3cPortalStatAuthResp,
       "h3cPortalStatChallengeReq": h3cPortalStatChallengeReq,
       "h3cPortalStatChallengeResp": h3cPortalStatChallengeResp,
       "h3cPortalPktStatistic": h3cPortalPktStatistic,
       "h3cPortalPktStaReqAuthNum": h3cPortalPktStaReqAuthNum,
       "h3cPortalPktStaAckAuthSuccess": h3cPortalPktStaAckAuthSuccess,
       "h3cPortalPktStaAckAuthReject": h3cPortalPktStaAckAuthReject,
       "h3cPortalPktStaAckAuthEstablish": h3cPortalPktStaAckAuthEstablish,
       "h3cPortalPktStaAckAuthBusy": h3cPortalPktStaAckAuthBusy,
       "h3cPortalPktStaAckAuthAuthFail": h3cPortalPktStaAckAuthAuthFail,
       "h3cPortalPktStaReqChallengeNum": h3cPortalPktStaReqChallengeNum,
       "h3cPortalPktStaAckChallengeSuccess": h3cPortalPktStaAckChallengeSuccess,
       "h3cPortalPktStaAckChallengeReject": h3cPortalPktStaAckChallengeReject,
       "h3cPortalPktStaAckChallengeEstablish": h3cPortalPktStaAckChallengeEstablish,
       "h3cPortalPktStaAckChallengeBusy": h3cPortalPktStaAckChallengeBusy,
       "h3cPortalPktStaAckChallengeAuthFail": h3cPortalPktStaAckChallengeAuthFail}
)
