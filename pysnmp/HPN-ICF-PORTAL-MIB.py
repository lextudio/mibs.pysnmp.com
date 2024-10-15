# SNMP MIB module (HPN-ICF-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PORTAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:28 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfPortal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfPortalConfig_ObjectIdentity = ObjectIdentity
hpnicfPortalConfig = _HpnicfPortalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 1)
)
_HpnicfPortalMaxUserNumber_Type = Integer32
_HpnicfPortalMaxUserNumber_Object = MibScalar
hpnicfPortalMaxUserNumber = _HpnicfPortalMaxUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 1, 1),
    _HpnicfPortalMaxUserNumber_Type()
)
hpnicfPortalMaxUserNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortalMaxUserNumber.setStatus("current")
_HpnicfPortalCurrentUserNumber_Type = Integer32
_HpnicfPortalCurrentUserNumber_Object = MibScalar
hpnicfPortalCurrentUserNumber = _HpnicfPortalCurrentUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 1, 2),
    _HpnicfPortalCurrentUserNumber_Type()
)
hpnicfPortalCurrentUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalCurrentUserNumber.setStatus("current")


class _HpnicfPortalStatus_Type(Integer32):
    """Custom type hpnicfPortalStatus based on Integer32"""
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


_HpnicfPortalStatus_Type.__name__ = "Integer32"
_HpnicfPortalStatus_Object = MibScalar
hpnicfPortalStatus = _HpnicfPortalStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 1, 3),
    _HpnicfPortalStatus_Type()
)
hpnicfPortalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatus.setStatus("current")
_HpnicfPortalUserNumberUpperLimit_Type = Integer32
_HpnicfPortalUserNumberUpperLimit_Object = MibScalar
hpnicfPortalUserNumberUpperLimit = _HpnicfPortalUserNumberUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 1, 4),
    _HpnicfPortalUserNumberUpperLimit_Type()
)
hpnicfPortalUserNumberUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalUserNumberUpperLimit.setStatus("current")
_HpnicfPortalNasId_Type = OctetString
_HpnicfPortalNasId_Object = MibScalar
hpnicfPortalNasId = _HpnicfPortalNasId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 1, 5),
    _HpnicfPortalNasId_Type()
)
hpnicfPortalNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortalNasId.setStatus("current")
_HpnicfPortalTables_ObjectIdentity = ObjectIdentity
hpnicfPortalTables = _HpnicfPortalTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2)
)
_HpnicfPortalServerTable_Object = MibTable
hpnicfPortalServerTable = _HpnicfPortalServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfPortalServerTable.setStatus("current")
_HpnicfPortalServerEntry_Object = MibTableRow
hpnicfPortalServerEntry = _HpnicfPortalServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 1, 1)
)
hpnicfPortalServerEntry.setIndexNames(
    (0, "HPN-ICF-PORTAL-MIB", "hpnicfPortalServerName"),
)
if mibBuilder.loadTexts:
    hpnicfPortalServerEntry.setStatus("current")


class _HpnicfPortalServerName_Type(OctetString):
    """Custom type hpnicfPortalServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfPortalServerName_Type.__name__ = "OctetString"
_HpnicfPortalServerName_Object = MibTableColumn
hpnicfPortalServerName = _HpnicfPortalServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 1, 1, 1),
    _HpnicfPortalServerName_Type()
)
hpnicfPortalServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPortalServerName.setStatus("current")


class _HpnicfPortalServerUrl_Type(OctetString):
    """Custom type hpnicfPortalServerUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HpnicfPortalServerUrl_Type.__name__ = "OctetString"
_HpnicfPortalServerUrl_Object = MibTableColumn
hpnicfPortalServerUrl = _HpnicfPortalServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 1, 1, 2),
    _HpnicfPortalServerUrl_Type()
)
hpnicfPortalServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortalServerUrl.setStatus("current")


class _HpnicfPortalServerPort_Type(Integer32):
    """Custom type hpnicfPortalServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HpnicfPortalServerPort_Type.__name__ = "Integer32"
_HpnicfPortalServerPort_Object = MibTableColumn
hpnicfPortalServerPort = _HpnicfPortalServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 1, 1, 3),
    _HpnicfPortalServerPort_Type()
)
hpnicfPortalServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortalServerPort.setStatus("current")
_HpnicfPortalIfInfoTable_Object = MibTable
hpnicfPortalIfInfoTable = _HpnicfPortalIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfPortalIfInfoTable.setStatus("current")
_HpnicfPortalIfInfoEntry_Object = MibTableRow
hpnicfPortalIfInfoEntry = _HpnicfPortalIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 2, 1)
)
hpnicfPortalIfInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortalIfInfoEntry.setStatus("current")
_HpnicfPortalAuthReqNumber_Type = Integer32
_HpnicfPortalAuthReqNumber_Object = MibTableColumn
hpnicfPortalAuthReqNumber = _HpnicfPortalAuthReqNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 2, 1, 1),
    _HpnicfPortalAuthReqNumber_Type()
)
hpnicfPortalAuthReqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalAuthReqNumber.setStatus("current")
_HpnicfPortalAuthSuccNumber_Type = Integer32
_HpnicfPortalAuthSuccNumber_Object = MibTableColumn
hpnicfPortalAuthSuccNumber = _HpnicfPortalAuthSuccNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 2, 1, 2),
    _HpnicfPortalAuthSuccNumber_Type()
)
hpnicfPortalAuthSuccNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalAuthSuccNumber.setStatus("current")
_HpnicfPortalAuthFailNumber_Type = Integer32
_HpnicfPortalAuthFailNumber_Object = MibTableColumn
hpnicfPortalAuthFailNumber = _HpnicfPortalAuthFailNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 2, 1, 3),
    _HpnicfPortalAuthFailNumber_Type()
)
hpnicfPortalAuthFailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalAuthFailNumber.setStatus("current")
_HpnicfPortalIfServerTable_Object = MibTable
hpnicfPortalIfServerTable = _HpnicfPortalIfServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfPortalIfServerTable.setStatus("current")
_HpnicfPortalIfServerEntry_Object = MibTableRow
hpnicfPortalIfServerEntry = _HpnicfPortalIfServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 3, 1)
)
hpnicfPortalIfServerEntry.setIndexNames(
    (0, "HPN-ICF-PORTAL-MIB", "hpnicfPortalIfServerIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortalIfServerEntry.setStatus("current")


class _HpnicfPortalIfServerIndex_Type(Integer32):
    """Custom type hpnicfPortalIfServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPortalIfServerIndex_Type.__name__ = "Integer32"
_HpnicfPortalIfServerIndex_Object = MibTableColumn
hpnicfPortalIfServerIndex = _HpnicfPortalIfServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 3, 1, 1),
    _HpnicfPortalIfServerIndex_Type()
)
hpnicfPortalIfServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortalIfServerIndex.setStatus("current")
_HpnicfPortalIfServerUrl_Type = OctetString
_HpnicfPortalIfServerUrl_Object = MibTableColumn
hpnicfPortalIfServerUrl = _HpnicfPortalIfServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 3, 1, 2),
    _HpnicfPortalIfServerUrl_Type()
)
hpnicfPortalIfServerUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalIfServerUrl.setStatus("current")
_HpnicfPortalIfServerRowStatus_Type = RowStatus
_HpnicfPortalIfServerRowStatus_Object = MibTableColumn
hpnicfPortalIfServerRowStatus = _HpnicfPortalIfServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 3, 1, 3),
    _HpnicfPortalIfServerRowStatus_Type()
)
hpnicfPortalIfServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalIfServerRowStatus.setStatus("current")
_HpnicfPortalIfVlanNasIDTable_Object = MibTable
hpnicfPortalIfVlanNasIDTable = _HpnicfPortalIfVlanNasIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfPortalIfVlanNasIDTable.setStatus("current")
_HpnicfPortalIfVlanNasIDEntry_Object = MibTableRow
hpnicfPortalIfVlanNasIDEntry = _HpnicfPortalIfVlanNasIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 4, 1)
)
hpnicfPortalIfVlanNasIDEntry.setIndexNames(
    (0, "HPN-ICF-PORTAL-MIB", "hpnicfPortalIfVlanNasIDIfIndex"),
    (0, "HPN-ICF-PORTAL-MIB", "hpnicfPortalIfVlanNasIDVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfPortalIfVlanNasIDEntry.setStatus("current")
_HpnicfPortalIfVlanNasIDIfIndex_Type = InterfaceIndex
_HpnicfPortalIfVlanNasIDIfIndex_Object = MibTableColumn
hpnicfPortalIfVlanNasIDIfIndex = _HpnicfPortalIfVlanNasIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 4, 1, 1),
    _HpnicfPortalIfVlanNasIDIfIndex_Type()
)
hpnicfPortalIfVlanNasIDIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortalIfVlanNasIDIfIndex.setStatus("current")


class _HpnicfPortalIfVlanNasIDVlanID_Type(Integer32):
    """Custom type hpnicfPortalIfVlanNasIDVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfPortalIfVlanNasIDVlanID_Type.__name__ = "Integer32"
_HpnicfPortalIfVlanNasIDVlanID_Object = MibTableColumn
hpnicfPortalIfVlanNasIDVlanID = _HpnicfPortalIfVlanNasIDVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 4, 1, 2),
    _HpnicfPortalIfVlanNasIDVlanID_Type()
)
hpnicfPortalIfVlanNasIDVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortalIfVlanNasIDVlanID.setStatus("current")


class _HpnicfPortalIfVlanNasIDNasID_Type(OctetString):
    """Custom type hpnicfPortalIfVlanNasIDNasID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfPortalIfVlanNasIDNasID_Type.__name__ = "OctetString"
_HpnicfPortalIfVlanNasIDNasID_Object = MibTableColumn
hpnicfPortalIfVlanNasIDNasID = _HpnicfPortalIfVlanNasIDNasID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 4, 1, 3),
    _HpnicfPortalIfVlanNasIDNasID_Type()
)
hpnicfPortalIfVlanNasIDNasID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalIfVlanNasIDNasID.setStatus("current")
_HpnicfPortalSSIDFreeRuleTable_Object = MibTable
hpnicfPortalSSIDFreeRuleTable = _HpnicfPortalSSIDFreeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfPortalSSIDFreeRuleTable.setStatus("current")
_HpnicfPortalSSIDFreeRuleEntry_Object = MibTableRow
hpnicfPortalSSIDFreeRuleEntry = _HpnicfPortalSSIDFreeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 5, 1)
)
hpnicfPortalSSIDFreeRuleEntry.setIndexNames(
    (0, "HPN-ICF-PORTAL-MIB", "hpnicfPortalSSIDFreeRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortalSSIDFreeRuleEntry.setStatus("current")


class _HpnicfPortalSSIDFreeRuleIndex_Type(Integer32):
    """Custom type hpnicfPortalSSIDFreeRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPortalSSIDFreeRuleIndex_Type.__name__ = "Integer32"
_HpnicfPortalSSIDFreeRuleIndex_Object = MibTableColumn
hpnicfPortalSSIDFreeRuleIndex = _HpnicfPortalSSIDFreeRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 5, 1, 1),
    _HpnicfPortalSSIDFreeRuleIndex_Type()
)
hpnicfPortalSSIDFreeRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortalSSIDFreeRuleIndex.setStatus("current")


class _HpnicfPortalSSIDFreeRuleSrcSSID_Type(OctetString):
    """Custom type hpnicfPortalSSIDFreeRuleSrcSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfPortalSSIDFreeRuleSrcSSID_Type.__name__ = "OctetString"
_HpnicfPortalSSIDFreeRuleSrcSSID_Object = MibTableColumn
hpnicfPortalSSIDFreeRuleSrcSSID = _HpnicfPortalSSIDFreeRuleSrcSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 5, 1, 2),
    _HpnicfPortalSSIDFreeRuleSrcSSID_Type()
)
hpnicfPortalSSIDFreeRuleSrcSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalSSIDFreeRuleSrcSSID.setStatus("current")
_HpnicfPortalSSIDFreeRuleRowStatus_Type = RowStatus
_HpnicfPortalSSIDFreeRuleRowStatus_Object = MibTableColumn
hpnicfPortalSSIDFreeRuleRowStatus = _HpnicfPortalSSIDFreeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 5, 1, 3),
    _HpnicfPortalSSIDFreeRuleRowStatus_Type()
)
hpnicfPortalSSIDFreeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalSSIDFreeRuleRowStatus.setStatus("current")


class _HpnicfPortalSSIDFreeRuleSrcSpot_Type(OctetString):
    """Custom type hpnicfPortalSSIDFreeRuleSrcSpot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfPortalSSIDFreeRuleSrcSpot_Type.__name__ = "OctetString"
_HpnicfPortalSSIDFreeRuleSrcSpot_Object = MibTableColumn
hpnicfPortalSSIDFreeRuleSrcSpot = _HpnicfPortalSSIDFreeRuleSrcSpot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 5, 1, 4),
    _HpnicfPortalSSIDFreeRuleSrcSpot_Type()
)
hpnicfPortalSSIDFreeRuleSrcSpot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalSSIDFreeRuleSrcSpot.setStatus("current")
_HpnicfPortalMacTriggerSrvTable_Object = MibTable
hpnicfPortalMacTriggerSrvTable = _HpnicfPortalMacTriggerSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerSrvTable.setStatus("current")
_HpnicfPortalMacTriggerSrvEntry_Object = MibTableRow
hpnicfPortalMacTriggerSrvEntry = _HpnicfPortalMacTriggerSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 6, 1)
)
hpnicfPortalMacTriggerSrvEntry.setIndexNames(
    (0, "HPN-ICF-PORTAL-MIB", "hpnicfPortalMacTriggerSrvIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerSrvEntry.setStatus("current")


class _HpnicfPortalMacTriggerSrvIndex_Type(Integer32):
    """Custom type hpnicfPortalMacTriggerSrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPortalMacTriggerSrvIndex_Type.__name__ = "Integer32"
_HpnicfPortalMacTriggerSrvIndex_Object = MibTableColumn
hpnicfPortalMacTriggerSrvIndex = _HpnicfPortalMacTriggerSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 6, 1, 1),
    _HpnicfPortalMacTriggerSrvIndex_Type()
)
hpnicfPortalMacTriggerSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerSrvIndex.setStatus("current")
_HpnicfPortalMacTriggerSrvIPAddrType_Type = InetAddressType
_HpnicfPortalMacTriggerSrvIPAddrType_Object = MibTableColumn
hpnicfPortalMacTriggerSrvIPAddrType = _HpnicfPortalMacTriggerSrvIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 6, 1, 2),
    _HpnicfPortalMacTriggerSrvIPAddrType_Type()
)
hpnicfPortalMacTriggerSrvIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerSrvIPAddrType.setStatus("current")
_HpnicfPortalMacTriggerSrvIP_Type = InetAddress
_HpnicfPortalMacTriggerSrvIP_Object = MibTableColumn
hpnicfPortalMacTriggerSrvIP = _HpnicfPortalMacTriggerSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 6, 1, 3),
    _HpnicfPortalMacTriggerSrvIP_Type()
)
hpnicfPortalMacTriggerSrvIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerSrvIP.setStatus("current")


class _HpnicfPortalMacTriggerSrvPort_Type(Integer32):
    """Custom type hpnicfPortalMacTriggerSrvPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HpnicfPortalMacTriggerSrvPort_Type.__name__ = "Integer32"
_HpnicfPortalMacTriggerSrvPort_Object = MibTableColumn
hpnicfPortalMacTriggerSrvPort = _HpnicfPortalMacTriggerSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 6, 1, 4),
    _HpnicfPortalMacTriggerSrvPort_Type()
)
hpnicfPortalMacTriggerSrvPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerSrvPort.setStatus("current")
_HpnicfPortalMacTriggerSrvRowStatus_Type = RowStatus
_HpnicfPortalMacTriggerSrvRowStatus_Object = MibTableColumn
hpnicfPortalMacTriggerSrvRowStatus = _HpnicfPortalMacTriggerSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 6, 1, 5),
    _HpnicfPortalMacTriggerSrvRowStatus_Type()
)
hpnicfPortalMacTriggerSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerSrvRowStatus.setStatus("current")
_HpnicfPortalMacTriggerOnIfTable_Object = MibTable
hpnicfPortalMacTriggerOnIfTable = _HpnicfPortalMacTriggerOnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerOnIfTable.setStatus("current")
_HpnicfPortalMacTriggerOnIfEntry_Object = MibTableRow
hpnicfPortalMacTriggerOnIfEntry = _HpnicfPortalMacTriggerOnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 7, 1)
)
hpnicfPortalMacTriggerOnIfEntry.setIndexNames(
    (0, "HPN-ICF-PORTAL-MIB", "hpnicfPortalMacTriggerOnIfIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerOnIfEntry.setStatus("current")
_HpnicfPortalMacTriggerOnIfIfIndex_Type = InterfaceIndex
_HpnicfPortalMacTriggerOnIfIfIndex_Object = MibTableColumn
hpnicfPortalMacTriggerOnIfIfIndex = _HpnicfPortalMacTriggerOnIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 7, 1, 1),
    _HpnicfPortalMacTriggerOnIfIfIndex_Type()
)
hpnicfPortalMacTriggerOnIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerOnIfIfIndex.setStatus("current")
_HpnicfPortalMacTriggerOnIfDetctFlowPeriod_Type = Integer32
_HpnicfPortalMacTriggerOnIfDetctFlowPeriod_Object = MibTableColumn
hpnicfPortalMacTriggerOnIfDetctFlowPeriod = _HpnicfPortalMacTriggerOnIfDetctFlowPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 7, 1, 2),
    _HpnicfPortalMacTriggerOnIfDetctFlowPeriod_Type()
)
hpnicfPortalMacTriggerOnIfDetctFlowPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerOnIfDetctFlowPeriod.setStatus("current")
_HpnicfPortalMacTriggerOnIfThresholdFlow_Type = Unsigned32
_HpnicfPortalMacTriggerOnIfThresholdFlow_Object = MibTableColumn
hpnicfPortalMacTriggerOnIfThresholdFlow = _HpnicfPortalMacTriggerOnIfThresholdFlow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 7, 1, 3),
    _HpnicfPortalMacTriggerOnIfThresholdFlow_Type()
)
hpnicfPortalMacTriggerOnIfThresholdFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerOnIfThresholdFlow.setStatus("current")
_HpnicfPortalMacTriggerOnIfRowStatus_Type = RowStatus
_HpnicfPortalMacTriggerOnIfRowStatus_Object = MibTableColumn
hpnicfPortalMacTriggerOnIfRowStatus = _HpnicfPortalMacTriggerOnIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 7, 1, 4),
    _HpnicfPortalMacTriggerOnIfRowStatus_Type()
)
hpnicfPortalMacTriggerOnIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalMacTriggerOnIfRowStatus.setStatus("current")
_HpnicfPortalFreeRuleTable_Object = MibTable
hpnicfPortalFreeRuleTable = _HpnicfPortalFreeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleTable.setStatus("current")
_HpnicfPortalFreeRuleEntry_Object = MibTableRow
hpnicfPortalFreeRuleEntry = _HpnicfPortalFreeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1)
)
hpnicfPortalFreeRuleEntry.setIndexNames(
    (0, "HPN-ICF-PORTAL-MIB", "hpnicfPortalFreeRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleEntry.setStatus("current")


class _HpnicfPortalFreeRuleIndex_Type(Integer32):
    """Custom type hpnicfPortalFreeRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPortalFreeRuleIndex_Type.__name__ = "Integer32"
_HpnicfPortalFreeRuleIndex_Object = MibTableColumn
hpnicfPortalFreeRuleIndex = _HpnicfPortalFreeRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 1),
    _HpnicfPortalFreeRuleIndex_Type()
)
hpnicfPortalFreeRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleIndex.setStatus("current")
_HpnicfPortalFreeRuleSrcIfIndex_Type = InterfaceIndex
_HpnicfPortalFreeRuleSrcIfIndex_Object = MibTableColumn
hpnicfPortalFreeRuleSrcIfIndex = _HpnicfPortalFreeRuleSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 2),
    _HpnicfPortalFreeRuleSrcIfIndex_Type()
)
hpnicfPortalFreeRuleSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleSrcIfIndex.setStatus("current")
_HpnicfPortalFreeRuleSrcVlanID_Type = Integer32
_HpnicfPortalFreeRuleSrcVlanID_Object = MibTableColumn
hpnicfPortalFreeRuleSrcVlanID = _HpnicfPortalFreeRuleSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 3),
    _HpnicfPortalFreeRuleSrcVlanID_Type()
)
hpnicfPortalFreeRuleSrcVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleSrcVlanID.setStatus("current")
_HpnicfPortalFreeRuleSrcMac_Type = MacAddress
_HpnicfPortalFreeRuleSrcMac_Object = MibTableColumn
hpnicfPortalFreeRuleSrcMac = _HpnicfPortalFreeRuleSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 4),
    _HpnicfPortalFreeRuleSrcMac_Type()
)
hpnicfPortalFreeRuleSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleSrcMac.setStatus("current")
_HpnicfPortalFreeRuleAddrType_Type = InetAddressType
_HpnicfPortalFreeRuleAddrType_Object = MibTableColumn
hpnicfPortalFreeRuleAddrType = _HpnicfPortalFreeRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 5),
    _HpnicfPortalFreeRuleAddrType_Type()
)
hpnicfPortalFreeRuleAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleAddrType.setStatus("current")
_HpnicfPortalFreeRuleSrcAddr_Type = InetAddress
_HpnicfPortalFreeRuleSrcAddr_Object = MibTableColumn
hpnicfPortalFreeRuleSrcAddr = _HpnicfPortalFreeRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 6),
    _HpnicfPortalFreeRuleSrcAddr_Type()
)
hpnicfPortalFreeRuleSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleSrcAddr.setStatus("current")
_HpnicfPortalFreeRuleSrcPrefix_Type = InetAddressPrefixLength
_HpnicfPortalFreeRuleSrcPrefix_Object = MibTableColumn
hpnicfPortalFreeRuleSrcPrefix = _HpnicfPortalFreeRuleSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 7),
    _HpnicfPortalFreeRuleSrcPrefix_Type()
)
hpnicfPortalFreeRuleSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleSrcPrefix.setStatus("current")
_HpnicfPortalFreeRuleDstAddr_Type = InetAddress
_HpnicfPortalFreeRuleDstAddr_Object = MibTableColumn
hpnicfPortalFreeRuleDstAddr = _HpnicfPortalFreeRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 8),
    _HpnicfPortalFreeRuleDstAddr_Type()
)
hpnicfPortalFreeRuleDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleDstAddr.setStatus("current")
_HpnicfPortalFreeRuleDstPrefix_Type = InetAddressPrefixLength
_HpnicfPortalFreeRuleDstPrefix_Object = MibTableColumn
hpnicfPortalFreeRuleDstPrefix = _HpnicfPortalFreeRuleDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 9),
    _HpnicfPortalFreeRuleDstPrefix_Type()
)
hpnicfPortalFreeRuleDstPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleDstPrefix.setStatus("current")


class _HpnicfPortalFreeRuleProtocol_Type(Integer32):
    """Custom type hpnicfPortalFreeRuleProtocol based on Integer32"""
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


_HpnicfPortalFreeRuleProtocol_Type.__name__ = "Integer32"
_HpnicfPortalFreeRuleProtocol_Object = MibTableColumn
hpnicfPortalFreeRuleProtocol = _HpnicfPortalFreeRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 10),
    _HpnicfPortalFreeRuleProtocol_Type()
)
hpnicfPortalFreeRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleProtocol.setStatus("current")
_HpnicfPortalFreeRuleSrcPort_Type = Integer32
_HpnicfPortalFreeRuleSrcPort_Object = MibTableColumn
hpnicfPortalFreeRuleSrcPort = _HpnicfPortalFreeRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 11),
    _HpnicfPortalFreeRuleSrcPort_Type()
)
hpnicfPortalFreeRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleSrcPort.setStatus("current")
_HpnicfPortalFreeRuleDstPort_Type = Integer32
_HpnicfPortalFreeRuleDstPort_Object = MibTableColumn
hpnicfPortalFreeRuleDstPort = _HpnicfPortalFreeRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 12),
    _HpnicfPortalFreeRuleDstPort_Type()
)
hpnicfPortalFreeRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleDstPort.setStatus("current")
_HpnicfPortalFreeRuleRowStatus_Type = RowStatus
_HpnicfPortalFreeRuleRowStatus_Object = MibTableColumn
hpnicfPortalFreeRuleRowStatus = _HpnicfPortalFreeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 8, 1, 13),
    _HpnicfPortalFreeRuleRowStatus_Type()
)
hpnicfPortalFreeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalFreeRuleRowStatus.setStatus("current")
_HpnicfPortalForbiddenRuleTable_Object = MibTable
hpnicfPortalForbiddenRuleTable = _HpnicfPortalForbiddenRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleTable.setStatus("current")
_HpnicfPortalForbiddenRuleEntry_Object = MibTableRow
hpnicfPortalForbiddenRuleEntry = _HpnicfPortalForbiddenRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1)
)
hpnicfPortalForbiddenRuleEntry.setIndexNames(
    (0, "HPN-ICF-PORTAL-MIB", "hpnicfPortalForbiddenRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleEntry.setStatus("current")


class _HpnicfPortalForbiddenRuleIndex_Type(Integer32):
    """Custom type hpnicfPortalForbiddenRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfPortalForbiddenRuleIndex_Type.__name__ = "Integer32"
_HpnicfPortalForbiddenRuleIndex_Object = MibTableColumn
hpnicfPortalForbiddenRuleIndex = _HpnicfPortalForbiddenRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 1),
    _HpnicfPortalForbiddenRuleIndex_Type()
)
hpnicfPortalForbiddenRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleIndex.setStatus("current")
_HpnicfPortalForbiddenRuleSrcIfIndex_Type = InterfaceIndex
_HpnicfPortalForbiddenRuleSrcIfIndex_Object = MibTableColumn
hpnicfPortalForbiddenRuleSrcIfIndex = _HpnicfPortalForbiddenRuleSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 2),
    _HpnicfPortalForbiddenRuleSrcIfIndex_Type()
)
hpnicfPortalForbiddenRuleSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleSrcIfIndex.setStatus("current")
_HpnicfPortalForbiddenRuleSrcVlanID_Type = Integer32
_HpnicfPortalForbiddenRuleSrcVlanID_Object = MibTableColumn
hpnicfPortalForbiddenRuleSrcVlanID = _HpnicfPortalForbiddenRuleSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 3),
    _HpnicfPortalForbiddenRuleSrcVlanID_Type()
)
hpnicfPortalForbiddenRuleSrcVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleSrcVlanID.setStatus("current")
_HpnicfPortalForbiddenRuleSrcMac_Type = MacAddress
_HpnicfPortalForbiddenRuleSrcMac_Object = MibTableColumn
hpnicfPortalForbiddenRuleSrcMac = _HpnicfPortalForbiddenRuleSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 4),
    _HpnicfPortalForbiddenRuleSrcMac_Type()
)
hpnicfPortalForbiddenRuleSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleSrcMac.setStatus("current")
_HpnicfPortalForbiddenRuleAddrType_Type = InetAddressType
_HpnicfPortalForbiddenRuleAddrType_Object = MibTableColumn
hpnicfPortalForbiddenRuleAddrType = _HpnicfPortalForbiddenRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 5),
    _HpnicfPortalForbiddenRuleAddrType_Type()
)
hpnicfPortalForbiddenRuleAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleAddrType.setStatus("current")
_HpnicfPortalForbiddenRuleSrcAddr_Type = InetAddress
_HpnicfPortalForbiddenRuleSrcAddr_Object = MibTableColumn
hpnicfPortalForbiddenRuleSrcAddr = _HpnicfPortalForbiddenRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 6),
    _HpnicfPortalForbiddenRuleSrcAddr_Type()
)
hpnicfPortalForbiddenRuleSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleSrcAddr.setStatus("current")
_HpnicfPortalForbiddenRuleSrcPrefix_Type = InetAddressPrefixLength
_HpnicfPortalForbiddenRuleSrcPrefix_Object = MibTableColumn
hpnicfPortalForbiddenRuleSrcPrefix = _HpnicfPortalForbiddenRuleSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 7),
    _HpnicfPortalForbiddenRuleSrcPrefix_Type()
)
hpnicfPortalForbiddenRuleSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleSrcPrefix.setStatus("current")
_HpnicfPortalForbiddenRuleDstAddr_Type = InetAddress
_HpnicfPortalForbiddenRuleDstAddr_Object = MibTableColumn
hpnicfPortalForbiddenRuleDstAddr = _HpnicfPortalForbiddenRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 8),
    _HpnicfPortalForbiddenRuleDstAddr_Type()
)
hpnicfPortalForbiddenRuleDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleDstAddr.setStatus("current")
_HpnicfPortalForbiddenRuleDstPrefix_Type = InetAddressPrefixLength
_HpnicfPortalForbiddenRuleDstPrefix_Object = MibTableColumn
hpnicfPortalForbiddenRuleDstPrefix = _HpnicfPortalForbiddenRuleDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 9),
    _HpnicfPortalForbiddenRuleDstPrefix_Type()
)
hpnicfPortalForbiddenRuleDstPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleDstPrefix.setStatus("current")


class _HpnicfPortalForbiddenRuleProtocol_Type(Integer32):
    """Custom type hpnicfPortalForbiddenRuleProtocol based on Integer32"""
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


_HpnicfPortalForbiddenRuleProtocol_Type.__name__ = "Integer32"
_HpnicfPortalForbiddenRuleProtocol_Object = MibTableColumn
hpnicfPortalForbiddenRuleProtocol = _HpnicfPortalForbiddenRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 10),
    _HpnicfPortalForbiddenRuleProtocol_Type()
)
hpnicfPortalForbiddenRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleProtocol.setStatus("current")
_HpnicfPortalForbiddenRuleSrcPort_Type = Integer32
_HpnicfPortalForbiddenRuleSrcPort_Object = MibTableColumn
hpnicfPortalForbiddenRuleSrcPort = _HpnicfPortalForbiddenRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 11),
    _HpnicfPortalForbiddenRuleSrcPort_Type()
)
hpnicfPortalForbiddenRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleSrcPort.setStatus("current")
_HpnicfPortalForbiddenRuleDstPort_Type = Integer32
_HpnicfPortalForbiddenRuleDstPort_Object = MibTableColumn
hpnicfPortalForbiddenRuleDstPort = _HpnicfPortalForbiddenRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 12),
    _HpnicfPortalForbiddenRuleDstPort_Type()
)
hpnicfPortalForbiddenRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleDstPort.setStatus("current")
_HpnicfPortalForbiddenRuleRowStatus_Type = RowStatus
_HpnicfPortalForbiddenRuleRowStatus_Object = MibTableColumn
hpnicfPortalForbiddenRuleRowStatus = _HpnicfPortalForbiddenRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 2, 9, 1, 13),
    _HpnicfPortalForbiddenRuleRowStatus_Type()
)
hpnicfPortalForbiddenRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortalForbiddenRuleRowStatus.setStatus("current")
_HpnicfPortalTraps_ObjectIdentity = ObjectIdentity
hpnicfPortalTraps = _HpnicfPortalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 3)
)
_HpnicfPortalTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfPortalTrapPrefix = _HpnicfPortalTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 3, 0)
)
_HpnicfPortalTrapVarObjects_ObjectIdentity = ObjectIdentity
hpnicfPortalTrapVarObjects = _HpnicfPortalTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 3, 1)
)
_HpnicfPortalFirstTrapTime_Type = TimeTicks
_HpnicfPortalFirstTrapTime_Object = MibScalar
hpnicfPortalFirstTrapTime = _HpnicfPortalFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 3, 1, 1),
    _HpnicfPortalFirstTrapTime_Type()
)
hpnicfPortalFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPortalFirstTrapTime.setStatus("current")
_HpnicfPortalServerIP_Type = InetAddressIPv4
_HpnicfPortalServerIP_Object = MibScalar
hpnicfPortalServerIP = _HpnicfPortalServerIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 3, 1, 2),
    _HpnicfPortalServerIP_Type()
)
hpnicfPortalServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPortalServerIP.setStatus("current")
_HpnicfPortalStatistic_ObjectIdentity = ObjectIdentity
hpnicfPortalStatistic = _HpnicfPortalStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4)
)
_HpnicfPortalStatAuthReq_Type = Counter64
_HpnicfPortalStatAuthReq_Object = MibScalar
hpnicfPortalStatAuthReq = _HpnicfPortalStatAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 1),
    _HpnicfPortalStatAuthReq_Type()
)
hpnicfPortalStatAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatAuthReq.setStatus("current")
_HpnicfPortalStatAckLogout_Type = Counter64
_HpnicfPortalStatAckLogout_Object = MibScalar
hpnicfPortalStatAckLogout = _HpnicfPortalStatAckLogout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 2),
    _HpnicfPortalStatAckLogout_Type()
)
hpnicfPortalStatAckLogout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatAckLogout.setStatus("current")
_HpnicfPortalStatNotifyLogout_Type = Counter64
_HpnicfPortalStatNotifyLogout_Object = MibScalar
hpnicfPortalStatNotifyLogout = _HpnicfPortalStatNotifyLogout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 3),
    _HpnicfPortalStatNotifyLogout_Type()
)
hpnicfPortalStatNotifyLogout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatNotifyLogout.setStatus("current")
_HpnicfPortalStatChallengeTimeout_Type = Counter64
_HpnicfPortalStatChallengeTimeout_Object = MibScalar
hpnicfPortalStatChallengeTimeout = _HpnicfPortalStatChallengeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 4),
    _HpnicfPortalStatChallengeTimeout_Type()
)
hpnicfPortalStatChallengeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatChallengeTimeout.setStatus("current")
_HpnicfPortalStatChallengeBusy_Type = Counter64
_HpnicfPortalStatChallengeBusy_Object = MibScalar
hpnicfPortalStatChallengeBusy = _HpnicfPortalStatChallengeBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 5),
    _HpnicfPortalStatChallengeBusy_Type()
)
hpnicfPortalStatChallengeBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatChallengeBusy.setStatus("current")
_HpnicfPortalStatChallengeFail_Type = Counter64
_HpnicfPortalStatChallengeFail_Object = MibScalar
hpnicfPortalStatChallengeFail = _HpnicfPortalStatChallengeFail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 6),
    _HpnicfPortalStatChallengeFail_Type()
)
hpnicfPortalStatChallengeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatChallengeFail.setStatus("current")
_HpnicfPortalStatAuthTimeout_Type = Counter64
_HpnicfPortalStatAuthTimeout_Object = MibScalar
hpnicfPortalStatAuthTimeout = _HpnicfPortalStatAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 7),
    _HpnicfPortalStatAuthTimeout_Type()
)
hpnicfPortalStatAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatAuthTimeout.setStatus("current")
_HpnicfPortalStatAuthFail_Type = Counter64
_HpnicfPortalStatAuthFail_Object = MibScalar
hpnicfPortalStatAuthFail = _HpnicfPortalStatAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 8),
    _HpnicfPortalStatAuthFail_Type()
)
hpnicfPortalStatAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatAuthFail.setStatus("current")
_HpnicfPortalStatPwdError_Type = Counter64
_HpnicfPortalStatPwdError_Object = MibScalar
hpnicfPortalStatPwdError = _HpnicfPortalStatPwdError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 9),
    _HpnicfPortalStatPwdError_Type()
)
hpnicfPortalStatPwdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatPwdError.setStatus("current")
_HpnicfPortalStatAuthBusy_Type = Counter64
_HpnicfPortalStatAuthBusy_Object = MibScalar
hpnicfPortalStatAuthBusy = _HpnicfPortalStatAuthBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 10),
    _HpnicfPortalStatAuthBusy_Type()
)
hpnicfPortalStatAuthBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatAuthBusy.setStatus("current")
_HpnicfPortalStatAuthDisordered_Type = Counter64
_HpnicfPortalStatAuthDisordered_Object = MibScalar
hpnicfPortalStatAuthDisordered = _HpnicfPortalStatAuthDisordered_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 11),
    _HpnicfPortalStatAuthDisordered_Type()
)
hpnicfPortalStatAuthDisordered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatAuthDisordered.setStatus("current")
_HpnicfPortalStatAuthUnknownError_Type = Counter64
_HpnicfPortalStatAuthUnknownError_Object = MibScalar
hpnicfPortalStatAuthUnknownError = _HpnicfPortalStatAuthUnknownError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 12),
    _HpnicfPortalStatAuthUnknownError_Type()
)
hpnicfPortalStatAuthUnknownError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatAuthUnknownError.setStatus("current")
_HpnicfPortalStatAuthResp_Type = Counter64
_HpnicfPortalStatAuthResp_Object = MibScalar
hpnicfPortalStatAuthResp = _HpnicfPortalStatAuthResp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 13),
    _HpnicfPortalStatAuthResp_Type()
)
hpnicfPortalStatAuthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatAuthResp.setStatus("current")
_HpnicfPortalStatChallengeReq_Type = Counter64
_HpnicfPortalStatChallengeReq_Object = MibScalar
hpnicfPortalStatChallengeReq = _HpnicfPortalStatChallengeReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 14),
    _HpnicfPortalStatChallengeReq_Type()
)
hpnicfPortalStatChallengeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatChallengeReq.setStatus("current")
_HpnicfPortalStatChallengeResp_Type = Counter64
_HpnicfPortalStatChallengeResp_Object = MibScalar
hpnicfPortalStatChallengeResp = _HpnicfPortalStatChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 15),
    _HpnicfPortalStatChallengeResp_Type()
)
hpnicfPortalStatChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatChallengeResp.setStatus("current")
_HpnicfPortalStatHttpReq_Type = Counter64
_HpnicfPortalStatHttpReq_Object = MibScalar
hpnicfPortalStatHttpReq = _HpnicfPortalStatHttpReq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 16),
    _HpnicfPortalStatHttpReq_Type()
)
hpnicfPortalStatHttpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatHttpReq.setStatus("current")
_HpnicfPortalStatHttpResp_Type = Counter64
_HpnicfPortalStatHttpResp_Object = MibScalar
hpnicfPortalStatHttpResp = _HpnicfPortalStatHttpResp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 4, 17),
    _HpnicfPortalStatHttpResp_Type()
)
hpnicfPortalStatHttpResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalStatHttpResp.setStatus("current")
_HpnicfPortalPktStatistic_ObjectIdentity = ObjectIdentity
hpnicfPortalPktStatistic = _HpnicfPortalPktStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5)
)
_HpnicfPortalPktStaReqAuthNum_Type = Counter64
_HpnicfPortalPktStaReqAuthNum_Object = MibScalar
hpnicfPortalPktStaReqAuthNum = _HpnicfPortalPktStaReqAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 1),
    _HpnicfPortalPktStaReqAuthNum_Type()
)
hpnicfPortalPktStaReqAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaReqAuthNum.setStatus("current")
_HpnicfPortalPktStaAckAuthSuccess_Type = Counter64
_HpnicfPortalPktStaAckAuthSuccess_Object = MibScalar
hpnicfPortalPktStaAckAuthSuccess = _HpnicfPortalPktStaAckAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 2),
    _HpnicfPortalPktStaAckAuthSuccess_Type()
)
hpnicfPortalPktStaAckAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckAuthSuccess.setStatus("current")
_HpnicfPortalPktStaAckAuthReject_Type = Counter64
_HpnicfPortalPktStaAckAuthReject_Object = MibScalar
hpnicfPortalPktStaAckAuthReject = _HpnicfPortalPktStaAckAuthReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 3),
    _HpnicfPortalPktStaAckAuthReject_Type()
)
hpnicfPortalPktStaAckAuthReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckAuthReject.setStatus("current")
_HpnicfPortalPktStaAckAuthEstablish_Type = Counter64
_HpnicfPortalPktStaAckAuthEstablish_Object = MibScalar
hpnicfPortalPktStaAckAuthEstablish = _HpnicfPortalPktStaAckAuthEstablish_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 4),
    _HpnicfPortalPktStaAckAuthEstablish_Type()
)
hpnicfPortalPktStaAckAuthEstablish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckAuthEstablish.setStatus("current")
_HpnicfPortalPktStaAckAuthBusy_Type = Counter64
_HpnicfPortalPktStaAckAuthBusy_Object = MibScalar
hpnicfPortalPktStaAckAuthBusy = _HpnicfPortalPktStaAckAuthBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 5),
    _HpnicfPortalPktStaAckAuthBusy_Type()
)
hpnicfPortalPktStaAckAuthBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckAuthBusy.setStatus("current")
_HpnicfPortalPktStaAckAuthAuthFail_Type = Counter64
_HpnicfPortalPktStaAckAuthAuthFail_Object = MibScalar
hpnicfPortalPktStaAckAuthAuthFail = _HpnicfPortalPktStaAckAuthAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 6),
    _HpnicfPortalPktStaAckAuthAuthFail_Type()
)
hpnicfPortalPktStaAckAuthAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckAuthAuthFail.setStatus("current")
_HpnicfPortalPktStaReqChallengeNum_Type = Counter64
_HpnicfPortalPktStaReqChallengeNum_Object = MibScalar
hpnicfPortalPktStaReqChallengeNum = _HpnicfPortalPktStaReqChallengeNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 7),
    _HpnicfPortalPktStaReqChallengeNum_Type()
)
hpnicfPortalPktStaReqChallengeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaReqChallengeNum.setStatus("current")
_HpnicfPortalPktStaAckChallengeSuccess_Type = Counter64
_HpnicfPortalPktStaAckChallengeSuccess_Object = MibScalar
hpnicfPortalPktStaAckChallengeSuccess = _HpnicfPortalPktStaAckChallengeSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 8),
    _HpnicfPortalPktStaAckChallengeSuccess_Type()
)
hpnicfPortalPktStaAckChallengeSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckChallengeSuccess.setStatus("current")
_HpnicfPortalPktStaAckChallengeReject_Type = Counter64
_HpnicfPortalPktStaAckChallengeReject_Object = MibScalar
hpnicfPortalPktStaAckChallengeReject = _HpnicfPortalPktStaAckChallengeReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 9),
    _HpnicfPortalPktStaAckChallengeReject_Type()
)
hpnicfPortalPktStaAckChallengeReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckChallengeReject.setStatus("current")
_HpnicfPortalPktStaAckChallengeEstablish_Type = Counter64
_HpnicfPortalPktStaAckChallengeEstablish_Object = MibScalar
hpnicfPortalPktStaAckChallengeEstablish = _HpnicfPortalPktStaAckChallengeEstablish_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 10),
    _HpnicfPortalPktStaAckChallengeEstablish_Type()
)
hpnicfPortalPktStaAckChallengeEstablish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckChallengeEstablish.setStatus("current")
_HpnicfPortalPktStaAckChallengeBusy_Type = Counter64
_HpnicfPortalPktStaAckChallengeBusy_Object = MibScalar
hpnicfPortalPktStaAckChallengeBusy = _HpnicfPortalPktStaAckChallengeBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 11),
    _HpnicfPortalPktStaAckChallengeBusy_Type()
)
hpnicfPortalPktStaAckChallengeBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckChallengeBusy.setStatus("current")
_HpnicfPortalPktStaAckChallengeAuthFail_Type = Counter64
_HpnicfPortalPktStaAckChallengeAuthFail_Object = MibScalar
hpnicfPortalPktStaAckChallengeAuthFail = _HpnicfPortalPktStaAckChallengeAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 5, 12),
    _HpnicfPortalPktStaAckChallengeAuthFail_Type()
)
hpnicfPortalPktStaAckChallengeAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortalPktStaAckChallengeAuthFail.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfPortalServerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 3, 0, 1)
)
hpnicfPortalServerLost.setObjects(
      *(("HPN-ICF-PORTAL-MIB", "hpnicfPortalServerName"),
        ("HPN-ICF-PORTAL-MIB", "hpnicfPortalFirstTrapTime"),
        ("HPN-ICF-PORTAL-MIB", "hpnicfPortalServerIP"),
        ("HPN-ICF-PORTAL-MIB", "hpnicfPortalServerPort"))
)
if mibBuilder.loadTexts:
    hpnicfPortalServerLost.setStatus(
        "current"
    )

hpnicfPortalServerGet = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99, 3, 0, 2)
)
hpnicfPortalServerGet.setObjects(
      *(("HPN-ICF-PORTAL-MIB", "hpnicfPortalServerName"),
        ("HPN-ICF-PORTAL-MIB", "hpnicfPortalFirstTrapTime"),
        ("HPN-ICF-PORTAL-MIB", "hpnicfPortalServerIP"),
        ("HPN-ICF-PORTAL-MIB", "hpnicfPortalServerPort"))
)
if mibBuilder.loadTexts:
    hpnicfPortalServerGet.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PORTAL-MIB",
    **{"hpnicfPortal": hpnicfPortal,
       "hpnicfPortalConfig": hpnicfPortalConfig,
       "hpnicfPortalMaxUserNumber": hpnicfPortalMaxUserNumber,
       "hpnicfPortalCurrentUserNumber": hpnicfPortalCurrentUserNumber,
       "hpnicfPortalStatus": hpnicfPortalStatus,
       "hpnicfPortalUserNumberUpperLimit": hpnicfPortalUserNumberUpperLimit,
       "hpnicfPortalNasId": hpnicfPortalNasId,
       "hpnicfPortalTables": hpnicfPortalTables,
       "hpnicfPortalServerTable": hpnicfPortalServerTable,
       "hpnicfPortalServerEntry": hpnicfPortalServerEntry,
       "hpnicfPortalServerName": hpnicfPortalServerName,
       "hpnicfPortalServerUrl": hpnicfPortalServerUrl,
       "hpnicfPortalServerPort": hpnicfPortalServerPort,
       "hpnicfPortalIfInfoTable": hpnicfPortalIfInfoTable,
       "hpnicfPortalIfInfoEntry": hpnicfPortalIfInfoEntry,
       "hpnicfPortalAuthReqNumber": hpnicfPortalAuthReqNumber,
       "hpnicfPortalAuthSuccNumber": hpnicfPortalAuthSuccNumber,
       "hpnicfPortalAuthFailNumber": hpnicfPortalAuthFailNumber,
       "hpnicfPortalIfServerTable": hpnicfPortalIfServerTable,
       "hpnicfPortalIfServerEntry": hpnicfPortalIfServerEntry,
       "hpnicfPortalIfServerIndex": hpnicfPortalIfServerIndex,
       "hpnicfPortalIfServerUrl": hpnicfPortalIfServerUrl,
       "hpnicfPortalIfServerRowStatus": hpnicfPortalIfServerRowStatus,
       "hpnicfPortalIfVlanNasIDTable": hpnicfPortalIfVlanNasIDTable,
       "hpnicfPortalIfVlanNasIDEntry": hpnicfPortalIfVlanNasIDEntry,
       "hpnicfPortalIfVlanNasIDIfIndex": hpnicfPortalIfVlanNasIDIfIndex,
       "hpnicfPortalIfVlanNasIDVlanID": hpnicfPortalIfVlanNasIDVlanID,
       "hpnicfPortalIfVlanNasIDNasID": hpnicfPortalIfVlanNasIDNasID,
       "hpnicfPortalSSIDFreeRuleTable": hpnicfPortalSSIDFreeRuleTable,
       "hpnicfPortalSSIDFreeRuleEntry": hpnicfPortalSSIDFreeRuleEntry,
       "hpnicfPortalSSIDFreeRuleIndex": hpnicfPortalSSIDFreeRuleIndex,
       "hpnicfPortalSSIDFreeRuleSrcSSID": hpnicfPortalSSIDFreeRuleSrcSSID,
       "hpnicfPortalSSIDFreeRuleRowStatus": hpnicfPortalSSIDFreeRuleRowStatus,
       "hpnicfPortalSSIDFreeRuleSrcSpot": hpnicfPortalSSIDFreeRuleSrcSpot,
       "hpnicfPortalMacTriggerSrvTable": hpnicfPortalMacTriggerSrvTable,
       "hpnicfPortalMacTriggerSrvEntry": hpnicfPortalMacTriggerSrvEntry,
       "hpnicfPortalMacTriggerSrvIndex": hpnicfPortalMacTriggerSrvIndex,
       "hpnicfPortalMacTriggerSrvIPAddrType": hpnicfPortalMacTriggerSrvIPAddrType,
       "hpnicfPortalMacTriggerSrvIP": hpnicfPortalMacTriggerSrvIP,
       "hpnicfPortalMacTriggerSrvPort": hpnicfPortalMacTriggerSrvPort,
       "hpnicfPortalMacTriggerSrvRowStatus": hpnicfPortalMacTriggerSrvRowStatus,
       "hpnicfPortalMacTriggerOnIfTable": hpnicfPortalMacTriggerOnIfTable,
       "hpnicfPortalMacTriggerOnIfEntry": hpnicfPortalMacTriggerOnIfEntry,
       "hpnicfPortalMacTriggerOnIfIfIndex": hpnicfPortalMacTriggerOnIfIfIndex,
       "hpnicfPortalMacTriggerOnIfDetctFlowPeriod": hpnicfPortalMacTriggerOnIfDetctFlowPeriod,
       "hpnicfPortalMacTriggerOnIfThresholdFlow": hpnicfPortalMacTriggerOnIfThresholdFlow,
       "hpnicfPortalMacTriggerOnIfRowStatus": hpnicfPortalMacTriggerOnIfRowStatus,
       "hpnicfPortalFreeRuleTable": hpnicfPortalFreeRuleTable,
       "hpnicfPortalFreeRuleEntry": hpnicfPortalFreeRuleEntry,
       "hpnicfPortalFreeRuleIndex": hpnicfPortalFreeRuleIndex,
       "hpnicfPortalFreeRuleSrcIfIndex": hpnicfPortalFreeRuleSrcIfIndex,
       "hpnicfPortalFreeRuleSrcVlanID": hpnicfPortalFreeRuleSrcVlanID,
       "hpnicfPortalFreeRuleSrcMac": hpnicfPortalFreeRuleSrcMac,
       "hpnicfPortalFreeRuleAddrType": hpnicfPortalFreeRuleAddrType,
       "hpnicfPortalFreeRuleSrcAddr": hpnicfPortalFreeRuleSrcAddr,
       "hpnicfPortalFreeRuleSrcPrefix": hpnicfPortalFreeRuleSrcPrefix,
       "hpnicfPortalFreeRuleDstAddr": hpnicfPortalFreeRuleDstAddr,
       "hpnicfPortalFreeRuleDstPrefix": hpnicfPortalFreeRuleDstPrefix,
       "hpnicfPortalFreeRuleProtocol": hpnicfPortalFreeRuleProtocol,
       "hpnicfPortalFreeRuleSrcPort": hpnicfPortalFreeRuleSrcPort,
       "hpnicfPortalFreeRuleDstPort": hpnicfPortalFreeRuleDstPort,
       "hpnicfPortalFreeRuleRowStatus": hpnicfPortalFreeRuleRowStatus,
       "hpnicfPortalForbiddenRuleTable": hpnicfPortalForbiddenRuleTable,
       "hpnicfPortalForbiddenRuleEntry": hpnicfPortalForbiddenRuleEntry,
       "hpnicfPortalForbiddenRuleIndex": hpnicfPortalForbiddenRuleIndex,
       "hpnicfPortalForbiddenRuleSrcIfIndex": hpnicfPortalForbiddenRuleSrcIfIndex,
       "hpnicfPortalForbiddenRuleSrcVlanID": hpnicfPortalForbiddenRuleSrcVlanID,
       "hpnicfPortalForbiddenRuleSrcMac": hpnicfPortalForbiddenRuleSrcMac,
       "hpnicfPortalForbiddenRuleAddrType": hpnicfPortalForbiddenRuleAddrType,
       "hpnicfPortalForbiddenRuleSrcAddr": hpnicfPortalForbiddenRuleSrcAddr,
       "hpnicfPortalForbiddenRuleSrcPrefix": hpnicfPortalForbiddenRuleSrcPrefix,
       "hpnicfPortalForbiddenRuleDstAddr": hpnicfPortalForbiddenRuleDstAddr,
       "hpnicfPortalForbiddenRuleDstPrefix": hpnicfPortalForbiddenRuleDstPrefix,
       "hpnicfPortalForbiddenRuleProtocol": hpnicfPortalForbiddenRuleProtocol,
       "hpnicfPortalForbiddenRuleSrcPort": hpnicfPortalForbiddenRuleSrcPort,
       "hpnicfPortalForbiddenRuleDstPort": hpnicfPortalForbiddenRuleDstPort,
       "hpnicfPortalForbiddenRuleRowStatus": hpnicfPortalForbiddenRuleRowStatus,
       "hpnicfPortalTraps": hpnicfPortalTraps,
       "hpnicfPortalTrapPrefix": hpnicfPortalTrapPrefix,
       "hpnicfPortalServerLost": hpnicfPortalServerLost,
       "hpnicfPortalServerGet": hpnicfPortalServerGet,
       "hpnicfPortalTrapVarObjects": hpnicfPortalTrapVarObjects,
       "hpnicfPortalFirstTrapTime": hpnicfPortalFirstTrapTime,
       "hpnicfPortalServerIP": hpnicfPortalServerIP,
       "hpnicfPortalStatistic": hpnicfPortalStatistic,
       "hpnicfPortalStatAuthReq": hpnicfPortalStatAuthReq,
       "hpnicfPortalStatAckLogout": hpnicfPortalStatAckLogout,
       "hpnicfPortalStatNotifyLogout": hpnicfPortalStatNotifyLogout,
       "hpnicfPortalStatChallengeTimeout": hpnicfPortalStatChallengeTimeout,
       "hpnicfPortalStatChallengeBusy": hpnicfPortalStatChallengeBusy,
       "hpnicfPortalStatChallengeFail": hpnicfPortalStatChallengeFail,
       "hpnicfPortalStatAuthTimeout": hpnicfPortalStatAuthTimeout,
       "hpnicfPortalStatAuthFail": hpnicfPortalStatAuthFail,
       "hpnicfPortalStatPwdError": hpnicfPortalStatPwdError,
       "hpnicfPortalStatAuthBusy": hpnicfPortalStatAuthBusy,
       "hpnicfPortalStatAuthDisordered": hpnicfPortalStatAuthDisordered,
       "hpnicfPortalStatAuthUnknownError": hpnicfPortalStatAuthUnknownError,
       "hpnicfPortalStatAuthResp": hpnicfPortalStatAuthResp,
       "hpnicfPortalStatChallengeReq": hpnicfPortalStatChallengeReq,
       "hpnicfPortalStatChallengeResp": hpnicfPortalStatChallengeResp,
       "hpnicfPortalStatHttpReq": hpnicfPortalStatHttpReq,
       "hpnicfPortalStatHttpResp": hpnicfPortalStatHttpResp,
       "hpnicfPortalPktStatistic": hpnicfPortalPktStatistic,
       "hpnicfPortalPktStaReqAuthNum": hpnicfPortalPktStaReqAuthNum,
       "hpnicfPortalPktStaAckAuthSuccess": hpnicfPortalPktStaAckAuthSuccess,
       "hpnicfPortalPktStaAckAuthReject": hpnicfPortalPktStaAckAuthReject,
       "hpnicfPortalPktStaAckAuthEstablish": hpnicfPortalPktStaAckAuthEstablish,
       "hpnicfPortalPktStaAckAuthBusy": hpnicfPortalPktStaAckAuthBusy,
       "hpnicfPortalPktStaAckAuthAuthFail": hpnicfPortalPktStaAckAuthAuthFail,
       "hpnicfPortalPktStaReqChallengeNum": hpnicfPortalPktStaReqChallengeNum,
       "hpnicfPortalPktStaAckChallengeSuccess": hpnicfPortalPktStaAckChallengeSuccess,
       "hpnicfPortalPktStaAckChallengeReject": hpnicfPortalPktStaAckChallengeReject,
       "hpnicfPortalPktStaAckChallengeEstablish": hpnicfPortalPktStaAckChallengeEstablish,
       "hpnicfPortalPktStaAckChallengeBusy": hpnicfPortalPktStaAckChallengeBusy,
       "hpnicfPortalPktStaAckChallengeAuthFail": hpnicfPortalPktStaAckChallengeAuthFail}
)
