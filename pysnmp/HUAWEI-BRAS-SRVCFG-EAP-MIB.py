# SNMP MIB module (HUAWEI-BRAS-SRVCFG-EAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-SRVCFG-EAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:10 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(InterfaceIndex,
 ifDescr) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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

hwBRASSrvcfgEap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSrvcfgEapMibObjects_ObjectIdentity = ObjectIdentity
hwSrvcfgEapMibObjects = _HwSrvcfgEapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1)
)
_HwDot1xSystemConfigTable_Object = MibTable
hwDot1xSystemConfigTable = _HwDot1xSystemConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwDot1xSystemConfigTable.setStatus("current")
_HwDot1xSystemConfigEntry_Object = MibTableRow
hwDot1xSystemConfigEntry = _HwDot1xSystemConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1)
)
hwDot1xSystemConfigEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xTemplateIndex"),
)
if mibBuilder.loadTexts:
    hwDot1xSystemConfigEntry.setStatus("current")


class _HwDot1xTemplateIndex_Type(Integer32):
    """Custom type hwDot1xTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwDot1xTemplateIndex_Type.__name__ = "Integer32"
_HwDot1xTemplateIndex_Object = MibTableColumn
hwDot1xTemplateIndex = _HwDot1xTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 1),
    _HwDot1xTemplateIndex_Type()
)
hwDot1xTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xTemplateIndex.setStatus("current")
_HwDot1xHandshakeSwitch_Type = TruthValue
_HwDot1xHandshakeSwitch_Object = MibTableColumn
hwDot1xHandshakeSwitch = _HwDot1xHandshakeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 2),
    _HwDot1xHandshakeSwitch_Type()
)
hwDot1xHandshakeSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xHandshakeSwitch.setStatus("current")


class _HwDot1xHandshakeCount_Type(Integer32):
    """Custom type hwDot1xHandshakeCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HwDot1xHandshakeCount_Type.__name__ = "Integer32"
_HwDot1xHandshakeCount_Object = MibTableColumn
hwDot1xHandshakeCount = _HwDot1xHandshakeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 3),
    _HwDot1xHandshakeCount_Type()
)
hwDot1xHandshakeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xHandshakeCount.setStatus("current")


class _HwDot1xHandshakeInterval_Type(Integer32):
    """Custom type hwDot1xHandshakeInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_HwDot1xHandshakeInterval_Type.__name__ = "Integer32"
_HwDot1xHandshakeInterval_Object = MibTableColumn
hwDot1xHandshakeInterval = _HwDot1xHandshakeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 4),
    _HwDot1xHandshakeInterval_Type()
)
hwDot1xHandshakeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xHandshakeInterval.setStatus("current")


class _HwDot1xIfEAPEnd_Type(TruthValue):
    """Custom type hwDot1xIfEAPEnd based on TruthValue"""


_HwDot1xIfEAPEnd_Object = MibTableColumn
hwDot1xIfEAPEnd = _HwDot1xIfEAPEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 5),
    _HwDot1xIfEAPEnd_Type()
)
hwDot1xIfEAPEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xIfEAPEnd.setStatus("current")


class _HwDot1xEAPEndPapChap_Type(Integer32):
    """Custom type hwDot1xEAPEndPapChap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("pap", 0))
    )


_HwDot1xEAPEndPapChap_Type.__name__ = "Integer32"
_HwDot1xEAPEndPapChap_Object = MibTableColumn
hwDot1xEAPEndPapChap = _HwDot1xEAPEndPapChap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 6),
    _HwDot1xEAPEndPapChap_Type()
)
hwDot1xEAPEndPapChap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xEAPEndPapChap.setStatus("current")


class _HwDot1xIfSendEAPSIMParameter_Type(TruthValue):
    """Custom type hwDot1xIfSendEAPSIMParameter based on TruthValue"""


_HwDot1xIfSendEAPSIMParameter_Object = MibTableColumn
hwDot1xIfSendEAPSIMParameter = _HwDot1xIfSendEAPSIMParameter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 7),
    _HwDot1xIfSendEAPSIMParameter_Type()
)
hwDot1xIfSendEAPSIMParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xIfSendEAPSIMParameter.setStatus("current")
_HwDot1xRowStatus_Type = RowStatus
_HwDot1xRowStatus_Object = MibTableColumn
hwDot1xRowStatus = _HwDot1xRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 8),
    _HwDot1xRowStatus_Type()
)
hwDot1xRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xRowStatus.setStatus("current")


class _HwDot1xAuthenticationTimeout_Type(Integer32):
    """Custom type hwDot1xAuthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HwDot1xAuthenticationTimeout_Type.__name__ = "Integer32"
_HwDot1xAuthenticationTimeout_Object = MibTableColumn
hwDot1xAuthenticationTimeout = _HwDot1xAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 9),
    _HwDot1xAuthenticationTimeout_Type()
)
hwDot1xAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xAuthenticationTimeout.setStatus("current")


class _HwDot1xRequestCount_Type(Integer32):
    """Custom type hwDot1xRequestCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwDot1xRequestCount_Type.__name__ = "Integer32"
_HwDot1xRequestCount_Object = MibTableColumn
hwDot1xRequestCount = _HwDot1xRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 10),
    _HwDot1xRequestCount_Type()
)
hwDot1xRequestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xRequestCount.setStatus("current")


class _HwDot1xRequestInterval_Type(Integer32):
    """Custom type hwDot1xRequestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HwDot1xRequestInterval_Type.__name__ = "Integer32"
_HwDot1xRequestInterval_Object = MibTableColumn
hwDot1xRequestInterval = _HwDot1xRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 11),
    _HwDot1xRequestInterval_Type()
)
hwDot1xRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xRequestInterval.setStatus("current")


class _HwDot1xReauthenticationTimeout_Type(Integer32):
    """Custom type hwDot1xReauthenticationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwDot1xReauthenticationTimeout_Type.__name__ = "Integer32"
_HwDot1xReauthenticationTimeout_Object = MibTableColumn
hwDot1xReauthenticationTimeout = _HwDot1xReauthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 1, 1, 12),
    _HwDot1xReauthenticationTimeout_Type()
)
hwDot1xReauthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xReauthenticationTimeout.setStatus("current")
_HwDot1xGlobal_Type = EnabledStatus
_HwDot1xGlobal_Object = MibScalar
hwDot1xGlobal = _HwDot1xGlobal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 2),
    _HwDot1xGlobal_Type()
)
hwDot1xGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xGlobal.setStatus("current")


class _HwDot1xAuthenMethod_Type(Integer32):
    """Custom type hwDot1xAuthenMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("eap", 3),
          ("pap", 2))
    )


_HwDot1xAuthenMethod_Type.__name__ = "Integer32"
_HwDot1xAuthenMethod_Object = MibScalar
hwDot1xAuthenMethod = _HwDot1xAuthenMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 3),
    _HwDot1xAuthenMethod_Type()
)
hwDot1xAuthenMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xAuthenMethod.setStatus("current")
_HwDot1xDhcpTrigger_Type = EnabledStatus
_HwDot1xDhcpTrigger_Object = MibScalar
hwDot1xDhcpTrigger = _HwDot1xDhcpTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 4),
    _HwDot1xDhcpTrigger_Type()
)
hwDot1xDhcpTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xDhcpTrigger.setStatus("current")
_HwDot1xHandshake_Type = EnabledStatus
_HwDot1xHandshake_Object = MibScalar
hwDot1xHandshake = _HwDot1xHandshake_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 5),
    _HwDot1xHandshake_Type()
)
hwDot1xHandshake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xHandshake.setStatus("current")
_HwDot1xQuietPeriod_Type = EnabledStatus
_HwDot1xQuietPeriod_Object = MibScalar
hwDot1xQuietPeriod = _HwDot1xQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 6),
    _HwDot1xQuietPeriod_Type()
)
hwDot1xQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xQuietPeriod.setStatus("current")


class _HwDot1xRetry_Type(Integer32):
    """Custom type hwDot1xRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwDot1xRetry_Type.__name__ = "Integer32"
_HwDot1xRetry_Object = MibScalar
hwDot1xRetry = _HwDot1xRetry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 7),
    _HwDot1xRetry_Type()
)
hwDot1xRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xRetry.setStatus("current")


class _HwDot1xTimerHandshakePeriod_Type(Integer32):
    """Custom type hwDot1xTimerHandshakePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1024),
    )


_HwDot1xTimerHandshakePeriod_Type.__name__ = "Integer32"
_HwDot1xTimerHandshakePeriod_Object = MibScalar
hwDot1xTimerHandshakePeriod = _HwDot1xTimerHandshakePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 8),
    _HwDot1xTimerHandshakePeriod_Type()
)
hwDot1xTimerHandshakePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xTimerHandshakePeriod.setStatus("current")


class _HwDot1xTimerQuietPeriod_Type(Integer32):
    """Custom type hwDot1xTimerQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_HwDot1xTimerQuietPeriod_Type.__name__ = "Integer32"
_HwDot1xTimerQuietPeriod_Object = MibScalar
hwDot1xTimerQuietPeriod = _HwDot1xTimerQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 9),
    _HwDot1xTimerQuietPeriod_Type()
)
hwDot1xTimerQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xTimerQuietPeriod.setStatus("current")


class _HwDot1xTimerServerTimeout_Type(Integer32):
    """Custom type hwDot1xTimerServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwDot1xTimerServerTimeout_Type.__name__ = "Integer32"
_HwDot1xTimerServerTimeout_Object = MibScalar
hwDot1xTimerServerTimeout = _HwDot1xTimerServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 10),
    _HwDot1xTimerServerTimeout_Type()
)
hwDot1xTimerServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xTimerServerTimeout.setStatus("current")


class _HwDot1xTimerClientTimeout_Type(Integer32):
    """Custom type hwDot1xTimerClientTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwDot1xTimerClientTimeout_Type.__name__ = "Integer32"
_HwDot1xTimerClientTimeout_Object = MibScalar
hwDot1xTimerClientTimeout = _HwDot1xTimerClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 11),
    _HwDot1xTimerClientTimeout_Type()
)
hwDot1xTimerClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xTimerClientTimeout.setStatus("current")


class _HwDot1xTimerTxPeriod_Type(Integer32):
    """Custom type hwDot1xTimerTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwDot1xTimerTxPeriod_Type.__name__ = "Integer32"
_HwDot1xTimerTxPeriod_Object = MibScalar
hwDot1xTimerTxPeriod = _HwDot1xTimerTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 12),
    _HwDot1xTimerTxPeriod_Type()
)
hwDot1xTimerTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xTimerTxPeriod.setStatus("current")


class _HwDot1xReauthenPeriod_Type(Integer32):
    """Custom type hwDot1xReauthenPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_HwDot1xReauthenPeriod_Type.__name__ = "Integer32"
_HwDot1xReauthenPeriod_Object = MibScalar
hwDot1xReauthenPeriod = _HwDot1xReauthenPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 13),
    _HwDot1xReauthenPeriod_Type()
)
hwDot1xReauthenPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xReauthenPeriod.setStatus("current")
_HwDot1xPortConfigTable_Object = MibTable
hwDot1xPortConfigTable = _HwDot1xPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14)
)
if mibBuilder.loadTexts:
    hwDot1xPortConfigTable.setStatus("current")
_HwDot1xPortConfigEntry_Object = MibTableRow
hwDot1xPortConfigEntry = _HwDot1xPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1)
)
hwDot1xPortConfigEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xPortIndex"),
)
if mibBuilder.loadTexts:
    hwDot1xPortConfigEntry.setStatus("current")


class _HwDot1xPortIndex_Type(Integer32):
    """Custom type hwDot1xPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_HwDot1xPortIndex_Type.__name__ = "Integer32"
_HwDot1xPortIndex_Object = MibTableColumn
hwDot1xPortIndex = _HwDot1xPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 1),
    _HwDot1xPortIndex_Type()
)
hwDot1xPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1xPortIndex.setStatus("current")


class _HwDot1xPortSwitch_Type(EnabledStatus):
    """Custom type hwDot1xPortSwitch based on EnabledStatus"""


_HwDot1xPortSwitch_Object = MibTableColumn
hwDot1xPortSwitch = _HwDot1xPortSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 2),
    _HwDot1xPortSwitch_Type()
)
hwDot1xPortSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xPortSwitch.setStatus("current")
_HwDot1xPortGuestVlan_Type = VlanIdOrNone
_HwDot1xPortGuestVlan_Object = MibTableColumn
hwDot1xPortGuestVlan = _HwDot1xPortGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 3),
    _HwDot1xPortGuestVlan_Type()
)
hwDot1xPortGuestVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xPortGuestVlan.setStatus("current")


class _HwDot1xPortMaxUser_Type(Integer32):
    """Custom type hwDot1xPortMaxUser based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_HwDot1xPortMaxUser_Type.__name__ = "Integer32"
_HwDot1xPortMaxUser_Object = MibTableColumn
hwDot1xPortMaxUser = _HwDot1xPortMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 4),
    _HwDot1xPortMaxUser_Type()
)
hwDot1xPortMaxUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xPortMaxUser.setStatus("current")


class _HwDot1xPortControl_Type(Integer32):
    """Custom type hwDot1xPortControl based on Integer32"""
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
        *(("authorizedForce", 2),
          ("auto", 1),
          ("unauthorizedForce", 3))
    )


_HwDot1xPortControl_Type.__name__ = "Integer32"
_HwDot1xPortControl_Object = MibTableColumn
hwDot1xPortControl = _HwDot1xPortControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 5),
    _HwDot1xPortControl_Type()
)
hwDot1xPortControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xPortControl.setStatus("current")


class _HwDot1xPortMethod_Type(Integer32):
    """Custom type hwDot1xPortMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("port", 2))
    )


_HwDot1xPortMethod_Type.__name__ = "Integer32"
_HwDot1xPortMethod_Object = MibTableColumn
hwDot1xPortMethod = _HwDot1xPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 6),
    _HwDot1xPortMethod_Type()
)
hwDot1xPortMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xPortMethod.setStatus("current")


class _HwDot1xPortReauthen_Type(EnabledStatus):
    """Custom type hwDot1xPortReauthen based on EnabledStatus"""


_HwDot1xPortReauthen_Object = MibTableColumn
hwDot1xPortReauthen = _HwDot1xPortReauthen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 7),
    _HwDot1xPortReauthen_Type()
)
hwDot1xPortReauthen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xPortReauthen.setStatus("current")


class _HwDot1xMacByPass_Type(EnabledStatus):
    """Custom type hwDot1xMacByPass based on EnabledStatus"""


_HwDot1xMacByPass_Object = MibTableColumn
hwDot1xMacByPass = _HwDot1xMacByPass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 8),
    _HwDot1xMacByPass_Type()
)
hwDot1xMacByPass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xMacByPass.setStatus("current")
_HwDot1xModemVersion_Type = DisplayString
_HwDot1xModemVersion_Object = MibTableColumn
hwDot1xModemVersion = _HwDot1xModemVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 9),
    _HwDot1xModemVersion_Type()
)
hwDot1xModemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xModemVersion.setStatus("current")


class _HwDot1xForceDomain_Type(DisplayString):
    """Custom type hwDot1xForceDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwDot1xForceDomain_Type.__name__ = "DisplayString"
_HwDot1xForceDomain_Object = MibTableColumn
hwDot1xForceDomain = _HwDot1xForceDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 10),
    _HwDot1xForceDomain_Type()
)
hwDot1xForceDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xForceDomain.setStatus("current")
_HwDot1xAuthStatus_Type = TruthValue
_HwDot1xAuthStatus_Object = MibTableColumn
hwDot1xAuthStatus = _HwDot1xAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 11),
    _HwDot1xAuthStatus_Type()
)
hwDot1xAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xAuthStatus.setStatus("current")
_HwDot1xPortRowStatus_Type = RowStatus
_HwDot1xPortRowStatus_Object = MibTableColumn
hwDot1xPortRowStatus = _HwDot1xPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 14, 1, 12),
    _HwDot1xPortRowStatus_Type()
)
hwDot1xPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDot1xPortRowStatus.setStatus("current")


class _HwDot1xQuietFailTimes_Type(Integer32):
    """Custom type hwDot1xQuietFailTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwDot1xQuietFailTimes_Type.__name__ = "Integer32"
_HwDot1xQuietFailTimes_Object = MibScalar
hwDot1xQuietFailTimes = _HwDot1xQuietFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 15),
    _HwDot1xQuietFailTimes_Type()
)
hwDot1xQuietFailTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1xQuietFailTimes.setStatus("current")
_HwDot1xSessionDisplayByPortTable_Object = MibTable
hwDot1xSessionDisplayByPortTable = _HwDot1xSessionDisplayByPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16)
)
if mibBuilder.loadTexts:
    hwDot1xSessionDisplayByPortTable.setStatus("current")
_HwDot1xSessionDisplayByPortEntry_Object = MibTableRow
hwDot1xSessionDisplayByPortEntry = _HwDot1xSessionDisplayByPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1)
)
hwDot1xSessionDisplayByPortEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xSessDispByPortIndex"),
    (0, "HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xSessDispByPortUserIndex"),
)
if mibBuilder.loadTexts:
    hwDot1xSessionDisplayByPortEntry.setStatus("current")


class _HwDot1xSessDispByPortIndex_Type(Integer32):
    """Custom type hwDot1xSessDispByPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_HwDot1xSessDispByPortIndex_Type.__name__ = "Integer32"
_HwDot1xSessDispByPortIndex_Object = MibTableColumn
hwDot1xSessDispByPortIndex = _HwDot1xSessDispByPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 1),
    _HwDot1xSessDispByPortIndex_Type()
)
hwDot1xSessDispByPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortIndex.setStatus("current")


class _HwDot1xSessDispByPortUserIndex_Type(Integer32):
    """Custom type hwDot1xSessDispByPortUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49151),
    )


_HwDot1xSessDispByPortUserIndex_Type.__name__ = "Integer32"
_HwDot1xSessDispByPortUserIndex_Object = MibTableColumn
hwDot1xSessDispByPortUserIndex = _HwDot1xSessDispByPortUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 2),
    _HwDot1xSessDispByPortUserIndex_Type()
)
hwDot1xSessDispByPortUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortUserIndex.setStatus("current")
_HwDot1xSessDispByPortIfName_Type = DisplayString
_HwDot1xSessDispByPortIfName_Object = MibTableColumn
hwDot1xSessDispByPortIfName = _HwDot1xSessDispByPortIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 3),
    _HwDot1xSessDispByPortIfName_Type()
)
hwDot1xSessDispByPortIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortIfName.setStatus("current")
_HwDot1xSessDispByPortUserMac_Type = MacAddress
_HwDot1xSessDispByPortUserMac_Object = MibTableColumn
hwDot1xSessDispByPortUserMac = _HwDot1xSessDispByPortUserMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 4),
    _HwDot1xSessDispByPortUserMac_Type()
)
hwDot1xSessDispByPortUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortUserMac.setStatus("current")
_HwDot1xSessDispByPortUserState_Type = TruthValue
_HwDot1xSessDispByPortUserState_Object = MibTableColumn
hwDot1xSessDispByPortUserState = _HwDot1xSessDispByPortUserState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 5),
    _HwDot1xSessDispByPortUserState_Type()
)
hwDot1xSessDispByPortUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortUserState.setStatus("current")


class _HwDot1xSessDispByPortUserVlanId_Type(Integer32):
    """Custom type hwDot1xSessDispByPortUserVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwDot1xSessDispByPortUserVlanId_Type.__name__ = "Integer32"
_HwDot1xSessDispByPortUserVlanId_Object = MibTableColumn
hwDot1xSessDispByPortUserVlanId = _HwDot1xSessDispByPortUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 6),
    _HwDot1xSessDispByPortUserVlanId_Type()
)
hwDot1xSessDispByPortUserVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortUserVlanId.setStatus("current")


class _HwDot1xSessDispByPortUserQinqId_Type(Integer32):
    """Custom type hwDot1xSessDispByPortUserQinqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwDot1xSessDispByPortUserQinqId_Type.__name__ = "Integer32"
_HwDot1xSessDispByPortUserQinqId_Object = MibTableColumn
hwDot1xSessDispByPortUserQinqId = _HwDot1xSessDispByPortUserQinqId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 7),
    _HwDot1xSessDispByPortUserQinqId_Type()
)
hwDot1xSessDispByPortUserQinqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortUserQinqId.setStatus("current")


class _HwDot1xSessDispByPortTemplateIndex_Type(Integer32):
    """Custom type hwDot1xSessDispByPortTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwDot1xSessDispByPortTemplateIndex_Type.__name__ = "Integer32"
_HwDot1xSessDispByPortTemplateIndex_Object = MibTableColumn
hwDot1xSessDispByPortTemplateIndex = _HwDot1xSessDispByPortTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 8),
    _HwDot1xSessDispByPortTemplateIndex_Type()
)
hwDot1xSessDispByPortTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortTemplateIndex.setStatus("current")
_HwDot1xSessDispByPortHandShakeSwitch_Type = TruthValue
_HwDot1xSessDispByPortHandShakeSwitch_Object = MibTableColumn
hwDot1xSessDispByPortHandShakeSwitch = _HwDot1xSessDispByPortHandShakeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 9),
    _HwDot1xSessDispByPortHandShakeSwitch_Type()
)
hwDot1xSessDispByPortHandShakeSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortHandShakeSwitch.setStatus("current")
_HwDot1xSessDispByPortReauth_Type = TruthValue
_HwDot1xSessDispByPortReauth_Object = MibTableColumn
hwDot1xSessDispByPortReauth = _HwDot1xSessDispByPortReauth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 16, 1, 10),
    _HwDot1xSessDispByPortReauth_Type()
)
hwDot1xSessDispByPortReauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByPortReauth.setStatus("current")
_HwDot1xSessionDisplayBySlotTable_Object = MibTable
hwDot1xSessionDisplayBySlotTable = _HwDot1xSessionDisplayBySlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17)
)
if mibBuilder.loadTexts:
    hwDot1xSessionDisplayBySlotTable.setStatus("current")
_HwDot1xSessionDisplayBySlotEntry_Object = MibTableRow
hwDot1xSessionDisplayBySlotEntry = _HwDot1xSessionDisplayBySlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1)
)
hwDot1xSessionDisplayBySlotEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xSessDispBySlotIndex"),
    (0, "HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xSessDispBySlotUserIndex"),
)
if mibBuilder.loadTexts:
    hwDot1xSessionDisplayBySlotEntry.setStatus("current")


class _HwDot1xSessDispBySlotIndex_Type(Integer32):
    """Custom type hwDot1xSessDispBySlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_HwDot1xSessDispBySlotIndex_Type.__name__ = "Integer32"
_HwDot1xSessDispBySlotIndex_Object = MibTableColumn
hwDot1xSessDispBySlotIndex = _HwDot1xSessDispBySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 1),
    _HwDot1xSessDispBySlotIndex_Type()
)
hwDot1xSessDispBySlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotIndex.setStatus("current")


class _HwDot1xSessDispBySlotUserIndex_Type(Integer32):
    """Custom type hwDot1xSessDispBySlotUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49151),
    )


_HwDot1xSessDispBySlotUserIndex_Type.__name__ = "Integer32"
_HwDot1xSessDispBySlotUserIndex_Object = MibTableColumn
hwDot1xSessDispBySlotUserIndex = _HwDot1xSessDispBySlotUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 2),
    _HwDot1xSessDispBySlotUserIndex_Type()
)
hwDot1xSessDispBySlotUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotUserIndex.setStatus("current")
_HwDot1xSessDispBySlotIfName_Type = DisplayString
_HwDot1xSessDispBySlotIfName_Object = MibTableColumn
hwDot1xSessDispBySlotIfName = _HwDot1xSessDispBySlotIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 3),
    _HwDot1xSessDispBySlotIfName_Type()
)
hwDot1xSessDispBySlotIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotIfName.setStatus("current")
_HwDot1xSessDispBySlotUserMac_Type = MacAddress
_HwDot1xSessDispBySlotUserMac_Object = MibTableColumn
hwDot1xSessDispBySlotUserMac = _HwDot1xSessDispBySlotUserMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 4),
    _HwDot1xSessDispBySlotUserMac_Type()
)
hwDot1xSessDispBySlotUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotUserMac.setStatus("current")
_HwDot1xSessDispBySlotUserState_Type = TruthValue
_HwDot1xSessDispBySlotUserState_Object = MibTableColumn
hwDot1xSessDispBySlotUserState = _HwDot1xSessDispBySlotUserState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 5),
    _HwDot1xSessDispBySlotUserState_Type()
)
hwDot1xSessDispBySlotUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotUserState.setStatus("current")


class _HwDot1xSessDispBySlotUserVlanId_Type(Integer32):
    """Custom type hwDot1xSessDispBySlotUserVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwDot1xSessDispBySlotUserVlanId_Type.__name__ = "Integer32"
_HwDot1xSessDispBySlotUserVlanId_Object = MibTableColumn
hwDot1xSessDispBySlotUserVlanId = _HwDot1xSessDispBySlotUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 6),
    _HwDot1xSessDispBySlotUserVlanId_Type()
)
hwDot1xSessDispBySlotUserVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotUserVlanId.setStatus("current")


class _HwDot1xSessDispBySlotUserQinqId_Type(Integer32):
    """Custom type hwDot1xSessDispBySlotUserQinqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwDot1xSessDispBySlotUserQinqId_Type.__name__ = "Integer32"
_HwDot1xSessDispBySlotUserQinqId_Object = MibTableColumn
hwDot1xSessDispBySlotUserQinqId = _HwDot1xSessDispBySlotUserQinqId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 7),
    _HwDot1xSessDispBySlotUserQinqId_Type()
)
hwDot1xSessDispBySlotUserQinqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotUserQinqId.setStatus("current")


class _HwDot1xSessDispBySlotTemplateIndex_Type(Integer32):
    """Custom type hwDot1xSessDispBySlotTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwDot1xSessDispBySlotTemplateIndex_Type.__name__ = "Integer32"
_HwDot1xSessDispBySlotTemplateIndex_Object = MibTableColumn
hwDot1xSessDispBySlotTemplateIndex = _HwDot1xSessDispBySlotTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 8),
    _HwDot1xSessDispBySlotTemplateIndex_Type()
)
hwDot1xSessDispBySlotTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotTemplateIndex.setStatus("current")
_HwDot1xSessDispBySlotHandShakeSwitch_Type = TruthValue
_HwDot1xSessDispBySlotHandShakeSwitch_Object = MibTableColumn
hwDot1xSessDispBySlotHandShakeSwitch = _HwDot1xSessDispBySlotHandShakeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 9),
    _HwDot1xSessDispBySlotHandShakeSwitch_Type()
)
hwDot1xSessDispBySlotHandShakeSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotHandShakeSwitch.setStatus("current")
_HwDot1xSessDispBySlotReauth_Type = TruthValue
_HwDot1xSessDispBySlotReauth_Object = MibTableColumn
hwDot1xSessDispBySlotReauth = _HwDot1xSessDispBySlotReauth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 17, 1, 10),
    _HwDot1xSessDispBySlotReauth_Type()
)
hwDot1xSessDispBySlotReauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispBySlotReauth.setStatus("current")
_HwDot1xSessionDisplayByMacTable_Object = MibTable
hwDot1xSessionDisplayByMacTable = _HwDot1xSessionDisplayByMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18)
)
if mibBuilder.loadTexts:
    hwDot1xSessionDisplayByMacTable.setStatus("current")
_HwDot1xSessionDisplayByMacEntry_Object = MibTableRow
hwDot1xSessionDisplayByMacEntry = _HwDot1xSessionDisplayByMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1)
)
hwDot1xSessionDisplayByMacEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xSessDispByMacUserMac"),
)
if mibBuilder.loadTexts:
    hwDot1xSessionDisplayByMacEntry.setStatus("current")


class _HwDot1xSessDispByMacUserIndex_Type(Integer32):
    """Custom type hwDot1xSessDispByMacUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49151),
    )


_HwDot1xSessDispByMacUserIndex_Type.__name__ = "Integer32"
_HwDot1xSessDispByMacUserIndex_Object = MibTableColumn
hwDot1xSessDispByMacUserIndex = _HwDot1xSessDispByMacUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1, 1),
    _HwDot1xSessDispByMacUserIndex_Type()
)
hwDot1xSessDispByMacUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByMacUserIndex.setStatus("current")
_HwDot1xSessDispByMacIfName_Type = DisplayString
_HwDot1xSessDispByMacIfName_Object = MibTableColumn
hwDot1xSessDispByMacIfName = _HwDot1xSessDispByMacIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1, 2),
    _HwDot1xSessDispByMacIfName_Type()
)
hwDot1xSessDispByMacIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByMacIfName.setStatus("current")
_HwDot1xSessDispByMacUserMac_Type = MacAddress
_HwDot1xSessDispByMacUserMac_Object = MibTableColumn
hwDot1xSessDispByMacUserMac = _HwDot1xSessDispByMacUserMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1, 3),
    _HwDot1xSessDispByMacUserMac_Type()
)
hwDot1xSessDispByMacUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByMacUserMac.setStatus("current")
_HwDot1xSessDispByMacUserState_Type = TruthValue
_HwDot1xSessDispByMacUserState_Object = MibTableColumn
hwDot1xSessDispByMacUserState = _HwDot1xSessDispByMacUserState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1, 4),
    _HwDot1xSessDispByMacUserState_Type()
)
hwDot1xSessDispByMacUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByMacUserState.setStatus("current")


class _HwDot1xSessDispByMacUserVlanId_Type(Integer32):
    """Custom type hwDot1xSessDispByMacUserVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwDot1xSessDispByMacUserVlanId_Type.__name__ = "Integer32"
_HwDot1xSessDispByMacUserVlanId_Object = MibTableColumn
hwDot1xSessDispByMacUserVlanId = _HwDot1xSessDispByMacUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1, 5),
    _HwDot1xSessDispByMacUserVlanId_Type()
)
hwDot1xSessDispByMacUserVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByMacUserVlanId.setStatus("current")


class _HwDot1xSessDispByMacUserQinqId_Type(Integer32):
    """Custom type hwDot1xSessDispByMacUserQinqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwDot1xSessDispByMacUserQinqId_Type.__name__ = "Integer32"
_HwDot1xSessDispByMacUserQinqId_Object = MibTableColumn
hwDot1xSessDispByMacUserQinqId = _HwDot1xSessDispByMacUserQinqId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1, 6),
    _HwDot1xSessDispByMacUserQinqId_Type()
)
hwDot1xSessDispByMacUserQinqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByMacUserQinqId.setStatus("current")


class _HwDot1xSessDispByMacTemplateIndex_Type(Integer32):
    """Custom type hwDot1xSessDispByMacTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwDot1xSessDispByMacTemplateIndex_Type.__name__ = "Integer32"
_HwDot1xSessDispByMacTemplateIndex_Object = MibTableColumn
hwDot1xSessDispByMacTemplateIndex = _HwDot1xSessDispByMacTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1, 7),
    _HwDot1xSessDispByMacTemplateIndex_Type()
)
hwDot1xSessDispByMacTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByMacTemplateIndex.setStatus("current")
_HwDot1xSessDispByMacHandShakeSwitch_Type = TruthValue
_HwDot1xSessDispByMacHandShakeSwitch_Object = MibTableColumn
hwDot1xSessDispByMacHandShakeSwitch = _HwDot1xSessDispByMacHandShakeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1, 8),
    _HwDot1xSessDispByMacHandShakeSwitch_Type()
)
hwDot1xSessDispByMacHandShakeSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByMacHandShakeSwitch.setStatus("current")
_HwDot1xSessDispByMacReauth_Type = TruthValue
_HwDot1xSessDispByMacReauth_Object = MibTableColumn
hwDot1xSessDispByMacReauth = _HwDot1xSessDispByMacReauth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 18, 1, 9),
    _HwDot1xSessDispByMacReauth_Type()
)
hwDot1xSessDispByMacReauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDot1xSessDispByMacReauth.setStatus("current")
_HwPacketStatisticsTable_Object = MibTable
hwPacketStatisticsTable = _HwPacketStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19)
)
if mibBuilder.loadTexts:
    hwPacketStatisticsTable.setStatus("current")
_HwPacketStatisticsEntry_Object = MibTableRow
hwPacketStatisticsEntry = _HwPacketStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1)
)
hwPacketStatisticsEntry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwSlotIndex"),
)
if mibBuilder.loadTexts:
    hwPacketStatisticsEntry.setStatus("current")


class _HwSlotIndex_Type(Integer32):
    """Custom type hwSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSlotIndex_Type.__name__ = "Integer32"
_HwSlotIndex_Object = MibTableColumn
hwSlotIndex = _HwSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 1),
    _HwSlotIndex_Type()
)
hwSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotIndex.setStatus("current")


class _HwEapReqID_Type(Integer32):
    """Custom type hwEapReqID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEapReqID_Type.__name__ = "Integer32"
_HwEapReqID_Object = MibTableColumn
hwEapReqID = _HwEapReqID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 2),
    _HwEapReqID_Type()
)
hwEapReqID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEapReqID.setStatus("current")


class _HwEapRespID_Type(Integer32):
    """Custom type hwEapRespID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEapRespID_Type.__name__ = "Integer32"
_HwEapRespID_Object = MibTableColumn
hwEapRespID = _HwEapRespID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 3),
    _HwEapRespID_Type()
)
hwEapRespID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEapRespID.setStatus("current")


class _HwEapReqChallenge_Type(Integer32):
    """Custom type hwEapReqChallenge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEapReqChallenge_Type.__name__ = "Integer32"
_HwEapReqChallenge_Object = MibTableColumn
hwEapReqChallenge = _HwEapReqChallenge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 4),
    _HwEapReqChallenge_Type()
)
hwEapReqChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEapReqChallenge.setStatus("current")


class _HwEapRespChallenge_Type(Integer32):
    """Custom type hwEapRespChallenge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEapRespChallenge_Type.__name__ = "Integer32"
_HwEapRespChallenge_Object = MibTableColumn
hwEapRespChallenge = _HwEapRespChallenge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 5),
    _HwEapRespChallenge_Type()
)
hwEapRespChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEapRespChallenge.setStatus("current")


class _HwEapSuccess_Type(Integer32):
    """Custom type hwEapSuccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEapSuccess_Type.__name__ = "Integer32"
_HwEapSuccess_Object = MibTableColumn
hwEapSuccess = _HwEapSuccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 6),
    _HwEapSuccess_Type()
)
hwEapSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEapSuccess.setStatus("current")


class _HwEapFailure_Type(Integer32):
    """Custom type hwEapFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEapFailure_Type.__name__ = "Integer32"
_HwEapFailure_Object = MibTableColumn
hwEapFailure = _HwEapFailure_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 7),
    _HwEapFailure_Type()
)
hwEapFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEapFailure.setStatus("current")


class _HwEapStart_Type(Integer32):
    """Custom type hwEapStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEapStart_Type.__name__ = "Integer32"
_HwEapStart_Object = MibTableColumn
hwEapStart = _HwEapStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 8),
    _HwEapStart_Type()
)
hwEapStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEapStart.setStatus("current")


class _HwEapLogOff_Type(Integer32):
    """Custom type hwEapLogOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEapLogOff_Type.__name__ = "Integer32"
_HwEapLogOff_Object = MibTableColumn
hwEapLogOff = _HwEapLogOff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 9),
    _HwEapLogOff_Type()
)
hwEapLogOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEapLogOff.setStatus("current")


class _HwEapKey_Type(Integer32):
    """Custom type hwEapKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwEapKey_Type.__name__ = "Integer32"
_HwEapKey_Object = MibTableColumn
hwEapKey = _HwEapKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 1, 19, 1, 10),
    _HwEapKey_Type()
)
hwEapKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEapKey.setStatus("current")
_HwSrvcfgEapMibTraps_ObjectIdentity = ObjectIdentity
hwSrvcfgEapMibTraps = _HwSrvcfgEapMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 2)
)
_HwSrvcfgEapMibUserLimitTraps_ObjectIdentity = ObjectIdentity
hwSrvcfgEapMibUserLimitTraps = _HwSrvcfgEapMibUserLimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3)
)
_HwEapTrapOid_ObjectIdentity = ObjectIdentity
hwEapTrapOid = _HwEapTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 1)
)
_HwEapUserPortMaxNumThreshold_Type = Integer32
_HwEapUserPortMaxNumThreshold_Object = MibScalar
hwEapUserPortMaxNumThreshold = _HwEapUserPortMaxNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 1, 1),
    _HwEapUserPortMaxNumThreshold_Type()
)
hwEapUserPortMaxNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEapUserPortMaxNumThreshold.setStatus("current")
_HwEapUserPortMaxNumThresholdResume_Type = Integer32
_HwEapUserPortMaxNumThresholdResume_Object = MibScalar
hwEapUserPortMaxNumThresholdResume = _HwEapUserPortMaxNumThresholdResume_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 1, 2),
    _HwEapUserPortMaxNumThresholdResume_Type()
)
hwEapUserPortMaxNumThresholdResume.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEapUserPortMaxNumThresholdResume.setStatus("current")
_HwEapUserSlot_Type = Integer32
_HwEapUserSlot_Object = MibScalar
hwEapUserSlot = _HwEapUserSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 1, 3),
    _HwEapUserSlot_Type()
)
hwEapUserSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEapUserSlot.setStatus("current")
_HwEapUserSlotMaxNumThreshold_Type = Integer32
_HwEapUserSlotMaxNumThreshold_Object = MibScalar
hwEapUserSlotMaxNumThreshold = _HwEapUserSlotMaxNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 1, 4),
    _HwEapUserSlotMaxNumThreshold_Type()
)
hwEapUserSlotMaxNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEapUserSlotMaxNumThreshold.setStatus("current")
_HwEapUserTotalMaxNumThreshold_Type = Integer32
_HwEapUserTotalMaxNumThreshold_Object = MibScalar
hwEapUserTotalMaxNumThreshold = _HwEapUserTotalMaxNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 1, 5),
    _HwEapUserTotalMaxNumThreshold_Type()
)
hwEapUserTotalMaxNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEapUserTotalMaxNumThreshold.setStatus("current")
_HwEapTrapsDefine_ObjectIdentity = ObjectIdentity
hwEapTrapsDefine = _HwEapTrapsDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 2)
)
_HwEapTraps_ObjectIdentity = ObjectIdentity
hwEapTraps = _HwEapTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 2, 0)
)
_HwSrvcfgEapConformance_ObjectIdentity = ObjectIdentity
hwSrvcfgEapConformance = _HwSrvcfgEapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 4)
)
_HwSrvcfgEapCompliances_ObjectIdentity = ObjectIdentity
hwSrvcfgEapCompliances = _HwSrvcfgEapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 4, 1)
)
_HwDot1xSystemConfigGroups_ObjectIdentity = ObjectIdentity
hwDot1xSystemConfigGroups = _HwDot1xSystemConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 4, 2)
)

# Managed Objects groups

hwDot1xSystemConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 4, 2, 1)
)
hwDot1xSystemConfigGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xTemplateIndex"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xHandshakeSwitch"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xHandshakeCount"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xHandshakeInterval"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xIfEAPEnd"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xEAPEndPapChap"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xIfSendEAPSIMParameter"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xRowStatus"))
)
if mibBuilder.loadTexts:
    hwDot1xSystemConfigGroup.setStatus("current")

hwDot1xPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 4, 2, 2)
)
hwDot1xPortConfigGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xGlobal"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xAuthenMethod"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xDhcpTrigger"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xHandshake"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xQuietPeriod"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xRetry"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xTimerHandshakePeriod"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xTimerQuietPeriod"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xTimerServerTimeout"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xTimerClientTimeout"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xTimerTxPeriod"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xReauthenPeriod"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xPortSwitch"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xPortGuestVlan"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xPortMaxUser"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xPortControl"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xPortMethod"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xPortReauthen"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xMacByPass"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xModemVersion"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwDot1xQuietFailTimes"))
)
if mibBuilder.loadTexts:
    hwDot1xPortConfigGroup.setStatus("current")


# Notification objects

hwSrvcfgEapMaxUserAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 2, 1)
)
hwSrvcfgEapMaxUserAlarm.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    hwSrvcfgEapMaxUserAlarm.setStatus(
        "current"
    )

hwEapUserPortMaxNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 2, 0, 1)
)
hwEapUserPortMaxNum.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwEapUserPortMaxNumThreshold"))
)
if mibBuilder.loadTexts:
    hwEapUserPortMaxNum.setStatus(
        "current"
    )

hwEapUserPortMaxNumResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 2, 0, 2)
)
hwEapUserPortMaxNumResume.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwEapUserPortMaxNumThresholdResume"))
)
if mibBuilder.loadTexts:
    hwEapUserPortMaxNumResume.setStatus(
        "current"
    )

hwEapUserSlotMaxNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 2, 0, 3)
)
hwEapUserSlotMaxNum.setObjects(
      *(("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwEapUserSlot"),
        ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwEapUserSlotMaxNumThreshold"))
)
if mibBuilder.loadTexts:
    hwEapUserSlotMaxNum.setStatus(
        "current"
    )

hwEapUserTotalMaxNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 3, 2, 0, 4)
)
hwEapUserTotalMaxNum.setObjects(
    ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwEapUserTotalMaxNumThreshold")
)
if mibBuilder.loadTexts:
    hwEapUserTotalMaxNum.setStatus(
        "current"
    )


# Notifications groups

hwDot1xPortTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 4, 2, 3)
)
hwDot1xPortTrapGroup.setObjects(
    ("HUAWEI-BRAS-SRVCFG-EAP-MIB", "hwSrvcfgEapMaxUserAlarm")
)
if mibBuilder.loadTexts:
    hwDot1xPortTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwSrvcfgEapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwSrvcfgEapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-SRVCFG-EAP-MIB",
    **{"hwBRASSrvcfgEap": hwBRASSrvcfgEap,
       "hwSrvcfgEapMibObjects": hwSrvcfgEapMibObjects,
       "hwDot1xSystemConfigTable": hwDot1xSystemConfigTable,
       "hwDot1xSystemConfigEntry": hwDot1xSystemConfigEntry,
       "hwDot1xTemplateIndex": hwDot1xTemplateIndex,
       "hwDot1xHandshakeSwitch": hwDot1xHandshakeSwitch,
       "hwDot1xHandshakeCount": hwDot1xHandshakeCount,
       "hwDot1xHandshakeInterval": hwDot1xHandshakeInterval,
       "hwDot1xIfEAPEnd": hwDot1xIfEAPEnd,
       "hwDot1xEAPEndPapChap": hwDot1xEAPEndPapChap,
       "hwDot1xIfSendEAPSIMParameter": hwDot1xIfSendEAPSIMParameter,
       "hwDot1xRowStatus": hwDot1xRowStatus,
       "hwDot1xAuthenticationTimeout": hwDot1xAuthenticationTimeout,
       "hwDot1xRequestCount": hwDot1xRequestCount,
       "hwDot1xRequestInterval": hwDot1xRequestInterval,
       "hwDot1xReauthenticationTimeout": hwDot1xReauthenticationTimeout,
       "hwDot1xGlobal": hwDot1xGlobal,
       "hwDot1xAuthenMethod": hwDot1xAuthenMethod,
       "hwDot1xDhcpTrigger": hwDot1xDhcpTrigger,
       "hwDot1xHandshake": hwDot1xHandshake,
       "hwDot1xQuietPeriod": hwDot1xQuietPeriod,
       "hwDot1xRetry": hwDot1xRetry,
       "hwDot1xTimerHandshakePeriod": hwDot1xTimerHandshakePeriod,
       "hwDot1xTimerQuietPeriod": hwDot1xTimerQuietPeriod,
       "hwDot1xTimerServerTimeout": hwDot1xTimerServerTimeout,
       "hwDot1xTimerClientTimeout": hwDot1xTimerClientTimeout,
       "hwDot1xTimerTxPeriod": hwDot1xTimerTxPeriod,
       "hwDot1xReauthenPeriod": hwDot1xReauthenPeriod,
       "hwDot1xPortConfigTable": hwDot1xPortConfigTable,
       "hwDot1xPortConfigEntry": hwDot1xPortConfigEntry,
       "hwDot1xPortIndex": hwDot1xPortIndex,
       "hwDot1xPortSwitch": hwDot1xPortSwitch,
       "hwDot1xPortGuestVlan": hwDot1xPortGuestVlan,
       "hwDot1xPortMaxUser": hwDot1xPortMaxUser,
       "hwDot1xPortControl": hwDot1xPortControl,
       "hwDot1xPortMethod": hwDot1xPortMethod,
       "hwDot1xPortReauthen": hwDot1xPortReauthen,
       "hwDot1xMacByPass": hwDot1xMacByPass,
       "hwDot1xModemVersion": hwDot1xModemVersion,
       "hwDot1xForceDomain": hwDot1xForceDomain,
       "hwDot1xAuthStatus": hwDot1xAuthStatus,
       "hwDot1xPortRowStatus": hwDot1xPortRowStatus,
       "hwDot1xQuietFailTimes": hwDot1xQuietFailTimes,
       "hwDot1xSessionDisplayByPortTable": hwDot1xSessionDisplayByPortTable,
       "hwDot1xSessionDisplayByPortEntry": hwDot1xSessionDisplayByPortEntry,
       "hwDot1xSessDispByPortIndex": hwDot1xSessDispByPortIndex,
       "hwDot1xSessDispByPortUserIndex": hwDot1xSessDispByPortUserIndex,
       "hwDot1xSessDispByPortIfName": hwDot1xSessDispByPortIfName,
       "hwDot1xSessDispByPortUserMac": hwDot1xSessDispByPortUserMac,
       "hwDot1xSessDispByPortUserState": hwDot1xSessDispByPortUserState,
       "hwDot1xSessDispByPortUserVlanId": hwDot1xSessDispByPortUserVlanId,
       "hwDot1xSessDispByPortUserQinqId": hwDot1xSessDispByPortUserQinqId,
       "hwDot1xSessDispByPortTemplateIndex": hwDot1xSessDispByPortTemplateIndex,
       "hwDot1xSessDispByPortHandShakeSwitch": hwDot1xSessDispByPortHandShakeSwitch,
       "hwDot1xSessDispByPortReauth": hwDot1xSessDispByPortReauth,
       "hwDot1xSessionDisplayBySlotTable": hwDot1xSessionDisplayBySlotTable,
       "hwDot1xSessionDisplayBySlotEntry": hwDot1xSessionDisplayBySlotEntry,
       "hwDot1xSessDispBySlotIndex": hwDot1xSessDispBySlotIndex,
       "hwDot1xSessDispBySlotUserIndex": hwDot1xSessDispBySlotUserIndex,
       "hwDot1xSessDispBySlotIfName": hwDot1xSessDispBySlotIfName,
       "hwDot1xSessDispBySlotUserMac": hwDot1xSessDispBySlotUserMac,
       "hwDot1xSessDispBySlotUserState": hwDot1xSessDispBySlotUserState,
       "hwDot1xSessDispBySlotUserVlanId": hwDot1xSessDispBySlotUserVlanId,
       "hwDot1xSessDispBySlotUserQinqId": hwDot1xSessDispBySlotUserQinqId,
       "hwDot1xSessDispBySlotTemplateIndex": hwDot1xSessDispBySlotTemplateIndex,
       "hwDot1xSessDispBySlotHandShakeSwitch": hwDot1xSessDispBySlotHandShakeSwitch,
       "hwDot1xSessDispBySlotReauth": hwDot1xSessDispBySlotReauth,
       "hwDot1xSessionDisplayByMacTable": hwDot1xSessionDisplayByMacTable,
       "hwDot1xSessionDisplayByMacEntry": hwDot1xSessionDisplayByMacEntry,
       "hwDot1xSessDispByMacUserIndex": hwDot1xSessDispByMacUserIndex,
       "hwDot1xSessDispByMacIfName": hwDot1xSessDispByMacIfName,
       "hwDot1xSessDispByMacUserMac": hwDot1xSessDispByMacUserMac,
       "hwDot1xSessDispByMacUserState": hwDot1xSessDispByMacUserState,
       "hwDot1xSessDispByMacUserVlanId": hwDot1xSessDispByMacUserVlanId,
       "hwDot1xSessDispByMacUserQinqId": hwDot1xSessDispByMacUserQinqId,
       "hwDot1xSessDispByMacTemplateIndex": hwDot1xSessDispByMacTemplateIndex,
       "hwDot1xSessDispByMacHandShakeSwitch": hwDot1xSessDispByMacHandShakeSwitch,
       "hwDot1xSessDispByMacReauth": hwDot1xSessDispByMacReauth,
       "hwPacketStatisticsTable": hwPacketStatisticsTable,
       "hwPacketStatisticsEntry": hwPacketStatisticsEntry,
       "hwSlotIndex": hwSlotIndex,
       "hwEapReqID": hwEapReqID,
       "hwEapRespID": hwEapRespID,
       "hwEapReqChallenge": hwEapReqChallenge,
       "hwEapRespChallenge": hwEapRespChallenge,
       "hwEapSuccess": hwEapSuccess,
       "hwEapFailure": hwEapFailure,
       "hwEapStart": hwEapStart,
       "hwEapLogOff": hwEapLogOff,
       "hwEapKey": hwEapKey,
       "hwSrvcfgEapMibTraps": hwSrvcfgEapMibTraps,
       "hwSrvcfgEapMaxUserAlarm": hwSrvcfgEapMaxUserAlarm,
       "hwSrvcfgEapMibUserLimitTraps": hwSrvcfgEapMibUserLimitTraps,
       "hwEapTrapOid": hwEapTrapOid,
       "hwEapUserPortMaxNumThreshold": hwEapUserPortMaxNumThreshold,
       "hwEapUserPortMaxNumThresholdResume": hwEapUserPortMaxNumThresholdResume,
       "hwEapUserSlot": hwEapUserSlot,
       "hwEapUserSlotMaxNumThreshold": hwEapUserSlotMaxNumThreshold,
       "hwEapUserTotalMaxNumThreshold": hwEapUserTotalMaxNumThreshold,
       "hwEapTrapsDefine": hwEapTrapsDefine,
       "hwEapTraps": hwEapTraps,
       "hwEapUserPortMaxNum": hwEapUserPortMaxNum,
       "hwEapUserPortMaxNumResume": hwEapUserPortMaxNumResume,
       "hwEapUserSlotMaxNum": hwEapUserSlotMaxNum,
       "hwEapUserTotalMaxNum": hwEapUserTotalMaxNum,
       "hwSrvcfgEapConformance": hwSrvcfgEapConformance,
       "hwSrvcfgEapCompliances": hwSrvcfgEapCompliances,
       "hwSrvcfgEapCompliance": hwSrvcfgEapCompliance,
       "hwDot1xSystemConfigGroups": hwDot1xSystemConfigGroups,
       "hwDot1xSystemConfigGroup": hwDot1xSystemConfigGroup,
       "hwDot1xPortConfigGroup": hwDot1xPortConfigGroup,
       "hwDot1xPortTrapGroup": hwDot1xPortTrapGroup}
)
