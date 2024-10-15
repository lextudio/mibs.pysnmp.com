# SNMP MIB module (IEEE8021-EVB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-EVB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:21 2024
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

(ieee8021BridgePhyPort,) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgePhyPort")

(IEEE8021BridgePortNumber,
 IEEE8021PbbComponentIdentifier,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021PbbComponentIdentifier",
    "ieee802dot1mibs")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021BridgeEvbMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24)
)
ieee8021BridgeEvbMib.setRevisions(
        ("2018-06-21 00:00",
         "2014-12-15 00:00",
         "2012-02-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021BridgeEvbNotifications_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbNotifications = _Ieee8021BridgeEvbNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 0)
)
_Ieee8021BridgeEvbObjects_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbObjects = _Ieee8021BridgeEvbObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 1)
)
_Ieee8021BridgeEvbSys_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbSys = _Ieee8021BridgeEvbSys_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1)
)


class _Ieee8021BridgeEvbSysType_Type(Integer32):
    """Custom type ieee8021BridgeEvbSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("evbBridge", 1),
          ("evbStation", 2))
    )


_Ieee8021BridgeEvbSysType_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSysType_Object = MibScalar
ieee8021BridgeEvbSysType = _Ieee8021BridgeEvbSysType_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1),
    _Ieee8021BridgeEvbSysType_Type()
)
ieee8021BridgeEvbSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysType.setStatus("current")


class _Ieee8021BridgeEvbSysNumExternalPorts_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbSysNumExternalPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Ieee8021BridgeEvbSysNumExternalPorts_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbSysNumExternalPorts_Object = MibScalar
ieee8021BridgeEvbSysNumExternalPorts = _Ieee8021BridgeEvbSysNumExternalPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 2),
    _Ieee8021BridgeEvbSysNumExternalPorts_Type()
)
ieee8021BridgeEvbSysNumExternalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysNumExternalPorts.setStatus("current")


class _Ieee8021BridgeEvbSysEvbLldpTxEnable_Type(TruthValue):
    """Custom type ieee8021BridgeEvbSysEvbLldpTxEnable based on TruthValue"""


_Ieee8021BridgeEvbSysEvbLldpTxEnable_Object = MibScalar
ieee8021BridgeEvbSysEvbLldpTxEnable = _Ieee8021BridgeEvbSysEvbLldpTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 3),
    _Ieee8021BridgeEvbSysEvbLldpTxEnable_Type()
)
ieee8021BridgeEvbSysEvbLldpTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysEvbLldpTxEnable.setStatus("current")


class _Ieee8021BridgeEvbSysEvbLldpManual_Type(TruthValue):
    """Custom type ieee8021BridgeEvbSysEvbLldpManual based on TruthValue"""


_Ieee8021BridgeEvbSysEvbLldpManual_Object = MibScalar
ieee8021BridgeEvbSysEvbLldpManual = _Ieee8021BridgeEvbSysEvbLldpManual_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 4),
    _Ieee8021BridgeEvbSysEvbLldpManual_Type()
)
ieee8021BridgeEvbSysEvbLldpManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysEvbLldpManual.setStatus("current")
_Ieee8021BridgeEvbSysEvbLldpGidCapable_Type = TruthValue
_Ieee8021BridgeEvbSysEvbLldpGidCapable_Object = MibScalar
ieee8021BridgeEvbSysEvbLldpGidCapable = _Ieee8021BridgeEvbSysEvbLldpGidCapable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 5),
    _Ieee8021BridgeEvbSysEvbLldpGidCapable_Type()
)
ieee8021BridgeEvbSysEvbLldpGidCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysEvbLldpGidCapable.setStatus("current")
_Ieee8021BridgeEvbSysEcpAckTimer_Type = Integer32
_Ieee8021BridgeEvbSysEcpAckTimer_Object = MibScalar
ieee8021BridgeEvbSysEcpAckTimer = _Ieee8021BridgeEvbSysEcpAckTimer_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 6),
    _Ieee8021BridgeEvbSysEcpAckTimer_Type()
)
ieee8021BridgeEvbSysEcpAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysEcpAckTimer.setStatus("deprecated")


class _Ieee8021BridgeEvbSysEcpMaxRetries_Type(Integer32):
    """Custom type ieee8021BridgeEvbSysEcpMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ieee8021BridgeEvbSysEcpMaxRetries_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSysEcpMaxRetries_Object = MibScalar
ieee8021BridgeEvbSysEcpMaxRetries = _Ieee8021BridgeEvbSysEcpMaxRetries_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 7),
    _Ieee8021BridgeEvbSysEcpMaxRetries_Type()
)
ieee8021BridgeEvbSysEcpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysEcpMaxRetries.setStatus("current")
_Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay_Type = Integer32
_Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay_Object = MibScalar
ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay = _Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 8),
    _Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay_Type()
)
ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay.setStatus("deprecated")
_Ieee8021BridgeEvbSysVdpDfltReinitKeepAlive_Type = Integer32
_Ieee8021BridgeEvbSysVdpDfltReinitKeepAlive_Object = MibScalar
ieee8021BridgeEvbSysVdpDfltReinitKeepAlive = _Ieee8021BridgeEvbSysVdpDfltReinitKeepAlive_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 9),
    _Ieee8021BridgeEvbSysVdpDfltReinitKeepAlive_Type()
)
ieee8021BridgeEvbSysVdpDfltReinitKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysVdpDfltReinitKeepAlive.setStatus("deprecated")
_Ieee8021BridgeEvbSbpTable_Object = MibTable
ieee8021BridgeEvbSbpTable = _Ieee8021BridgeEvbSbpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpTable.setStatus("current")
_Ieee8021BridgeEvbSbpEntry_Object = MibTableRow
ieee8021BridgeEvbSbpEntry = _Ieee8021BridgeEvbSbpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10, 1)
)
ieee8021BridgeEvbSbpEntry.setIndexNames(
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpComponentID"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpPortNumber"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpEntry.setStatus("current")
_Ieee8021BridgeEvbSbpComponentID_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbSbpComponentID_Object = MibTableColumn
ieee8021BridgeEvbSbpComponentID = _Ieee8021BridgeEvbSbpComponentID_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10, 1, 1),
    _Ieee8021BridgeEvbSbpComponentID_Type()
)
ieee8021BridgeEvbSbpComponentID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpComponentID.setStatus("current")
_Ieee8021BridgeEvbSbpPortNumber_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbSbpPortNumber_Object = MibTableColumn
ieee8021BridgeEvbSbpPortNumber = _Ieee8021BridgeEvbSbpPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10, 1, 2),
    _Ieee8021BridgeEvbSbpPortNumber_Type()
)
ieee8021BridgeEvbSbpPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpPortNumber.setStatus("current")
_Ieee8021BridgeEvbSbpLldpManual_Type = TruthValue
_Ieee8021BridgeEvbSbpLldpManual_Object = MibTableColumn
ieee8021BridgeEvbSbpLldpManual = _Ieee8021BridgeEvbSbpLldpManual_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10, 1, 3),
    _Ieee8021BridgeEvbSbpLldpManual_Type()
)
ieee8021BridgeEvbSbpLldpManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpLldpManual.setStatus("current")
_Ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay_Type = Unsigned32
_Ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay_Object = MibTableColumn
ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay = _Ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10, 1, 4),
    _Ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay_Type()
)
ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay.setUnits("micro-seconds")
_Ieee8021BridgeEvbSbpVdpOperReinitKeepAlive_Type = Unsigned32
_Ieee8021BridgeEvbSbpVdpOperReinitKeepAlive_Object = MibTableColumn
ieee8021BridgeEvbSbpVdpOperReinitKeepAlive = _Ieee8021BridgeEvbSbpVdpOperReinitKeepAlive_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10, 1, 5),
    _Ieee8021BridgeEvbSbpVdpOperReinitKeepAlive_Type()
)
ieee8021BridgeEvbSbpVdpOperReinitKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpVdpOperReinitKeepAlive.setStatus("deprecated")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpVdpOperReinitKeepAlive.setUnits("micro-seconds")
_Ieee8021BridgeEvbSbpVdpOperToutKeepAlive_Type = Unsigned32
_Ieee8021BridgeEvbSbpVdpOperToutKeepAlive_Object = MibTableColumn
ieee8021BridgeEvbSbpVdpOperToutKeepAlive = _Ieee8021BridgeEvbSbpVdpOperToutKeepAlive_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10, 1, 6),
    _Ieee8021BridgeEvbSbpVdpOperToutKeepAlive_Type()
)
ieee8021BridgeEvbSbpVdpOperToutKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpVdpOperToutKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpVdpOperToutKeepAlive.setUnits("micro-seconds")


class _Ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp_Object = MibTableColumn
ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp = _Ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10, 1, 7),
    _Ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp_Type()
)
ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp.setStatus("current")


class _Ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp_Object = MibTableColumn
ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp = _Ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 10, 1, 8),
    _Ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp_Type()
)
ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp.setStatus("current")


class _Ieee8021BridgeEvbSysEcpDfltAckTimerExp_Type(Integer32):
    """Custom type ieee8021BridgeEvbSysEcpDfltAckTimerExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Ieee8021BridgeEvbSysEcpDfltAckTimerExp_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSysEcpDfltAckTimerExp_Object = MibScalar
ieee8021BridgeEvbSysEcpDfltAckTimerExp = _Ieee8021BridgeEvbSysEcpDfltAckTimerExp_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 11),
    _Ieee8021BridgeEvbSysEcpDfltAckTimerExp_Type()
)
ieee8021BridgeEvbSysEcpDfltAckTimerExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysEcpDfltAckTimerExp.setStatus("current")


class _Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp_Type(Integer32):
    """Custom type ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp_Object = MibScalar
ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp = _Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 12),
    _Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp_Type()
)
ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp.setStatus("current")


class _Ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp_Type(Integer32):
    """Custom type ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp_Object = MibScalar
ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp = _Ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 13),
    _Ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp_Type()
)
ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp.setStatus("current")
_Ieee8021BridgeEvbVSIDBObjects_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbVSIDBObjects = _Ieee8021BridgeEvbVSIDBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2)
)
_Ieee8021BridgeEvbVSIDBTable_Object = MibTable
ieee8021BridgeEvbVSIDBTable = _Ieee8021BridgeEvbVSIDBTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBTable.setStatus("current")
_Ieee8021BridgeEvbVSIDBEntry_Object = MibTableRow
ieee8021BridgeEvbVSIDBEntry = _Ieee8021BridgeEvbVSIDBEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1)
)
ieee8021BridgeEvbVSIDBEntry.setIndexNames(
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIComponentID"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIPortNumber"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIIDType"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIID"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBEntry.setStatus("current")
_Ieee8021BridgeEvbVSIComponentID_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbVSIComponentID_Object = MibTableColumn
ieee8021BridgeEvbVSIComponentID = _Ieee8021BridgeEvbVSIComponentID_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 1),
    _Ieee8021BridgeEvbVSIComponentID_Type()
)
ieee8021BridgeEvbVSIComponentID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIComponentID.setStatus("current")
_Ieee8021BridgeEvbVSIPortNumber_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbVSIPortNumber_Object = MibTableColumn
ieee8021BridgeEvbVSIPortNumber = _Ieee8021BridgeEvbVSIPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 2),
    _Ieee8021BridgeEvbVSIPortNumber_Type()
)
ieee8021BridgeEvbVSIPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIPortNumber.setStatus("current")


class _Ieee8021BridgeEvbVSIIDType_Type(Integer32):
    """Custom type ieee8021BridgeEvbVSIIDType based on Integer32"""
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
        *(("vsiidIpv4", 1),
          ("vsiidIpv6", 2),
          ("vsiidLocal", 4),
          ("vsiidMAC", 3),
          ("vsiidUUID", 5))
    )


_Ieee8021BridgeEvbVSIIDType_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbVSIIDType_Object = MibTableColumn
ieee8021BridgeEvbVSIIDType = _Ieee8021BridgeEvbVSIIDType_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 3),
    _Ieee8021BridgeEvbVSIIDType_Type()
)
ieee8021BridgeEvbVSIIDType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIIDType.setStatus("current")


class _Ieee8021BridgeEvbVSIID_Type(OctetString):
    """Custom type ieee8021BridgeEvbVSIID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Ieee8021BridgeEvbVSIID_Type.__name__ = "OctetString"
_Ieee8021BridgeEvbVSIID_Object = MibTableColumn
ieee8021BridgeEvbVSIID = _Ieee8021BridgeEvbVSIID_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 4),
    _Ieee8021BridgeEvbVSIID_Type()
)
ieee8021BridgeEvbVSIID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIID.setStatus("current")
_Ieee8021BridgeEvbVSITimeSinceCreate_Type = Unsigned32
_Ieee8021BridgeEvbVSITimeSinceCreate_Object = MibTableColumn
ieee8021BridgeEvbVSITimeSinceCreate = _Ieee8021BridgeEvbVSITimeSinceCreate_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 5),
    _Ieee8021BridgeEvbVSITimeSinceCreate_Type()
)
ieee8021BridgeEvbVSITimeSinceCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSITimeSinceCreate.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSITimeSinceCreate.setUnits("centi-seconds")


class _Ieee8021BridgeEvbVsiVdpOperCmd_Type(Integer32):
    """Custom type ieee8021BridgeEvbVsiVdpOperCmd based on Integer32"""
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
        *(("associate", 3),
          ("deAssociate", 4),
          ("preAssociate", 1),
          ("preAssociateWithRsrcReservation", 2))
    )


_Ieee8021BridgeEvbVsiVdpOperCmd_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbVsiVdpOperCmd_Object = MibTableColumn
ieee8021BridgeEvbVsiVdpOperCmd = _Ieee8021BridgeEvbVsiVdpOperCmd_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 6),
    _Ieee8021BridgeEvbVsiVdpOperCmd_Type()
)
ieee8021BridgeEvbVsiVdpOperCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVsiVdpOperCmd.setStatus("current")
_Ieee8021BridgeEvbVsiOperRevert_Type = TruthValue
_Ieee8021BridgeEvbVsiOperRevert_Object = MibTableColumn
ieee8021BridgeEvbVsiOperRevert = _Ieee8021BridgeEvbVsiOperRevert_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 7),
    _Ieee8021BridgeEvbVsiOperRevert_Type()
)
ieee8021BridgeEvbVsiOperRevert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVsiOperRevert.setStatus("current")
_Ieee8021BridgeEvbVsiOperHard_Type = TruthValue
_Ieee8021BridgeEvbVsiOperHard_Object = MibTableColumn
ieee8021BridgeEvbVsiOperHard = _Ieee8021BridgeEvbVsiOperHard_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 8),
    _Ieee8021BridgeEvbVsiOperHard_Type()
)
ieee8021BridgeEvbVsiOperHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVsiOperHard.setStatus("current")


class _Ieee8021BridgeEvbVsiOperReason_Type(Bits):
    """Custom type ieee8021BridgeEvbVsiOperReason based on Bits"""
    namedValues = NamedValues(
        *(("insufficientResources", 2),
          ("invalidFormat", 1),
          ("otherfailure", 3),
          ("success", 0))
    )

_Ieee8021BridgeEvbVsiOperReason_Type.__name__ = "Bits"
_Ieee8021BridgeEvbVsiOperReason_Object = MibTableColumn
ieee8021BridgeEvbVsiOperReason = _Ieee8021BridgeEvbVsiOperReason_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 9),
    _Ieee8021BridgeEvbVsiOperReason_Type()
)
ieee8021BridgeEvbVsiOperReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVsiOperReason.setStatus("current")


class _Ieee8021BridgeEvbVSIMgrID_Type(OctetString):
    """Custom type ieee8021BridgeEvbVSIMgrID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ieee8021BridgeEvbVSIMgrID_Type.__name__ = "OctetString"
_Ieee8021BridgeEvbVSIMgrID_Object = MibTableColumn
ieee8021BridgeEvbVSIMgrID = _Ieee8021BridgeEvbVSIMgrID_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 10),
    _Ieee8021BridgeEvbVSIMgrID_Type()
)
ieee8021BridgeEvbVSIMgrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIMgrID.setStatus("deprecated")
_Ieee8021BridgeEvbVSIType_Type = Integer32
_Ieee8021BridgeEvbVSIType_Object = MibTableColumn
ieee8021BridgeEvbVSIType = _Ieee8021BridgeEvbVSIType_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 11),
    _Ieee8021BridgeEvbVSIType_Type()
)
ieee8021BridgeEvbVSIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIType.setStatus("current")


class _Ieee8021BridgeEvbVSITypeVersion_Type(OctetString):
    """Custom type ieee8021BridgeEvbVSITypeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ieee8021BridgeEvbVSITypeVersion_Type.__name__ = "OctetString"
_Ieee8021BridgeEvbVSITypeVersion_Object = MibTableColumn
ieee8021BridgeEvbVSITypeVersion = _Ieee8021BridgeEvbVSITypeVersion_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 12),
    _Ieee8021BridgeEvbVSITypeVersion_Type()
)
ieee8021BridgeEvbVSITypeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSITypeVersion.setStatus("current")


class _Ieee8021BridgeEvbVSIMvFormat_Type(Integer32):
    """Custom type ieee8021BridgeEvbVSIMvFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("partial", 2),
          ("vlanOnly", 3))
    )


_Ieee8021BridgeEvbVSIMvFormat_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbVSIMvFormat_Object = MibTableColumn
ieee8021BridgeEvbVSIMvFormat = _Ieee8021BridgeEvbVSIMvFormat_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 13),
    _Ieee8021BridgeEvbVSIMvFormat_Type()
)
ieee8021BridgeEvbVSIMvFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIMvFormat.setStatus("deprecated")
_Ieee8021BridgeEvbVSINumMACs_Type = Integer32
_Ieee8021BridgeEvbVSINumMACs_Object = MibTableColumn
ieee8021BridgeEvbVSINumMACs = _Ieee8021BridgeEvbVSINumMACs_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 14),
    _Ieee8021BridgeEvbVSINumMACs_Type()
)
ieee8021BridgeEvbVSINumMACs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSINumMACs.setStatus("current")


class _Ieee8021BridgeEvbVDPMachineState_Type(Integer32):
    """Custom type ieee8021BridgeEvbVDPMachineState based on Integer32"""
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
        *(("associate", 3),
          ("deAssociate", 4),
          ("preAssociate", 1),
          ("preAssociateWithRsrcReservation", 2))
    )


_Ieee8021BridgeEvbVDPMachineState_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbVDPMachineState_Object = MibTableColumn
ieee8021BridgeEvbVDPMachineState = _Ieee8021BridgeEvbVDPMachineState_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 15),
    _Ieee8021BridgeEvbVDPMachineState_Type()
)
ieee8021BridgeEvbVDPMachineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPMachineState.setStatus("current")
_Ieee8021BridgeEvbVDPCommandsSucceeded_Type = Counter32
_Ieee8021BridgeEvbVDPCommandsSucceeded_Object = MibTableColumn
ieee8021BridgeEvbVDPCommandsSucceeded = _Ieee8021BridgeEvbVDPCommandsSucceeded_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 16),
    _Ieee8021BridgeEvbVDPCommandsSucceeded_Type()
)
ieee8021BridgeEvbVDPCommandsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPCommandsSucceeded.setStatus("current")
_Ieee8021BridgeEvbVDPCommandsFailed_Type = Counter32
_Ieee8021BridgeEvbVDPCommandsFailed_Object = MibTableColumn
ieee8021BridgeEvbVDPCommandsFailed = _Ieee8021BridgeEvbVDPCommandsFailed_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 17),
    _Ieee8021BridgeEvbVDPCommandsFailed_Type()
)
ieee8021BridgeEvbVDPCommandsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPCommandsFailed.setStatus("current")
_Ieee8021BridgeEvbVDPCommandReverts_Type = Counter32
_Ieee8021BridgeEvbVDPCommandReverts_Object = MibTableColumn
ieee8021BridgeEvbVDPCommandReverts = _Ieee8021BridgeEvbVDPCommandReverts_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 18),
    _Ieee8021BridgeEvbVDPCommandReverts_Type()
)
ieee8021BridgeEvbVDPCommandReverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPCommandReverts.setStatus("current")
_Ieee8021BridgeEvbVDPCounterDiscontinuity_Type = TimeTicks
_Ieee8021BridgeEvbVDPCounterDiscontinuity_Object = MibTableColumn
ieee8021BridgeEvbVDPCounterDiscontinuity = _Ieee8021BridgeEvbVDPCounterDiscontinuity_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 19),
    _Ieee8021BridgeEvbVDPCounterDiscontinuity_Type()
)
ieee8021BridgeEvbVDPCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPCounterDiscontinuity.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPCounterDiscontinuity.setUnits("hundredths of a second")


class _Ieee8021BridgeEvbVSIMgrID16_Type(OctetString):
    """Custom type ieee8021BridgeEvbVSIMgrID16 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Ieee8021BridgeEvbVSIMgrID16_Type.__name__ = "OctetString"
_Ieee8021BridgeEvbVSIMgrID16_Object = MibTableColumn
ieee8021BridgeEvbVSIMgrID16 = _Ieee8021BridgeEvbVSIMgrID16_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 20),
    _Ieee8021BridgeEvbVSIMgrID16_Type()
)
ieee8021BridgeEvbVSIMgrID16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIMgrID16.setStatus("current")


class _Ieee8021BridgeEvbVSIFilterFormat_Type(Integer32):
    """Custom type ieee8021BridgeEvbVSIFilterFormat based on Integer32"""
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
        *(("groupidMacVid", 4),
          ("groupidVid", 3),
          ("macVid", 2),
          ("vid", 1))
    )


_Ieee8021BridgeEvbVSIFilterFormat_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbVSIFilterFormat_Object = MibTableColumn
ieee8021BridgeEvbVSIFilterFormat = _Ieee8021BridgeEvbVSIFilterFormat_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1, 21),
    _Ieee8021BridgeEvbVSIFilterFormat_Type()
)
ieee8021BridgeEvbVSIFilterFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIFilterFormat.setStatus("current")
_Ieee8021BridgeEvbVSIDBMacTable_Object = MibTable
ieee8021BridgeEvbVSIDBMacTable = _Ieee8021BridgeEvbVSIDBMacTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBMacTable.setStatus("current")
_Ieee8021BridgeEvbVSIDBMacEntry_Object = MibTableRow
ieee8021BridgeEvbVSIDBMacEntry = _Ieee8021BridgeEvbVSIDBMacEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 2, 1)
)
ieee8021BridgeEvbVSIDBMacEntry.setIndexNames(
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIComponentID"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIPortNumber"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIIDType"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIID"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbGroupID"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIMac"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIVlanId"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBMacEntry.setStatus("current")
_Ieee8021BridgeEvbGroupID_Type = Unsigned32
_Ieee8021BridgeEvbGroupID_Object = MibTableColumn
ieee8021BridgeEvbGroupID = _Ieee8021BridgeEvbGroupID_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 2, 1, 1),
    _Ieee8021BridgeEvbGroupID_Type()
)
ieee8021BridgeEvbGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbGroupID.setStatus("current")
_Ieee8021BridgeEvbVSIMac_Type = MacAddress
_Ieee8021BridgeEvbVSIMac_Object = MibTableColumn
ieee8021BridgeEvbVSIMac = _Ieee8021BridgeEvbVSIMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 2, 1, 2),
    _Ieee8021BridgeEvbVSIMac_Type()
)
ieee8021BridgeEvbVSIMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIMac.setStatus("current")
_Ieee8021BridgeEvbVSIVlanId_Type = VlanIndex
_Ieee8021BridgeEvbVSIVlanId_Object = MibTableColumn
ieee8021BridgeEvbVSIVlanId = _Ieee8021BridgeEvbVSIVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 2, 1, 3),
    _Ieee8021BridgeEvbVSIVlanId_Type()
)
ieee8021BridgeEvbVSIVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIVlanId.setStatus("current")
_Ieee8021BridgeEvbSChannelObjects_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbSChannelObjects = _Ieee8021BridgeEvbSChannelObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3)
)
_Ieee8021BridgeEvbUAPConfigTable_Object = MibTable
ieee8021BridgeEvbUAPConfigTable = _Ieee8021BridgeEvbUAPConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPConfigTable.setStatus("current")
_Ieee8021BridgeEvbUAPConfigEntry_Object = MibTableRow
ieee8021BridgeEvbUAPConfigEntry = _Ieee8021BridgeEvbUAPConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1)
)
ieee8021BridgeEvbUAPConfigEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePhyPort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPConfigEntry.setStatus("current")
_Ieee8021BridgeEvbUAPComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbUAPComponentId_Object = MibTableColumn
ieee8021BridgeEvbUAPComponentId = _Ieee8021BridgeEvbUAPComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 1),
    _Ieee8021BridgeEvbUAPComponentId_Type()
)
ieee8021BridgeEvbUAPComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPComponentId.setStatus("current")
_Ieee8021BridgeEvbUAPPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbUAPPort_Object = MibTableColumn
ieee8021BridgeEvbUAPPort = _Ieee8021BridgeEvbUAPPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 2),
    _Ieee8021BridgeEvbUAPPort_Type()
)
ieee8021BridgeEvbUAPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPPort.setStatus("current")
_Ieee8021BridgeEvbUapConfigIfIndex_Type = InterfaceIndexOrZero
_Ieee8021BridgeEvbUapConfigIfIndex_Object = MibTableColumn
ieee8021BridgeEvbUapConfigIfIndex = _Ieee8021BridgeEvbUapConfigIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 3),
    _Ieee8021BridgeEvbUapConfigIfIndex_Type()
)
ieee8021BridgeEvbUapConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUapConfigIfIndex.setStatus("current")


class _Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchCdcpAdminEnable based on Integer32"""
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


_Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Object = MibTableColumn
ieee8021BridgeEvbUAPSchCdcpAdminEnable = _Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 4),
    _Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Type()
)
ieee8021BridgeEvbUAPSchCdcpAdminEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchCdcpAdminEnable.setStatus("current")


class _Ieee8021BridgeEvbUAPSchAdminCDCPRole_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchAdminCDCPRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdcpRoleB", 1),
          ("cdcpRoleS", 2))
    )


_Ieee8021BridgeEvbUAPSchAdminCDCPRole_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchAdminCDCPRole_Object = MibTableColumn
ieee8021BridgeEvbUAPSchAdminCDCPRole = _Ieee8021BridgeEvbUAPSchAdminCDCPRole_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 5),
    _Ieee8021BridgeEvbUAPSchAdminCDCPRole_Type()
)
ieee8021BridgeEvbUAPSchAdminCDCPRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchAdminCDCPRole.setStatus("current")


class _Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchAdminCDCPChanCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 167),
    )


_Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Object = MibTableColumn
ieee8021BridgeEvbUAPSchAdminCDCPChanCap = _Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 6),
    _Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Type()
)
ieee8021BridgeEvbUAPSchAdminCDCPChanCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchAdminCDCPChanCap.setStatus("current")


class _Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchOperCDCPChanCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 167),
    )


_Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Object = MibTableColumn
ieee8021BridgeEvbUAPSchOperCDCPChanCap = _Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 7),
    _Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Type()
)
ieee8021BridgeEvbUAPSchOperCDCPChanCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchOperCDCPChanCap.setStatus("current")
_Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow_Type = VlanIndex
_Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow_Object = MibTableColumn
ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow = _Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 8),
    _Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow_Type()
)
ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow.setStatus("current")
_Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh_Type = VlanIndex
_Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh_Object = MibTableColumn
ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh = _Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 9),
    _Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh_Type()
)
ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh.setStatus("current")


class _Ieee8021BridgeEvbUAPSchOperState_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 2),
          ("running", 1))
    )


_Ieee8021BridgeEvbUAPSchOperState_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchOperState_Object = MibTableColumn
ieee8021BridgeEvbUAPSchOperState = _Ieee8021BridgeEvbUAPSchOperState_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 10),
    _Ieee8021BridgeEvbUAPSchOperState_Type()
)
ieee8021BridgeEvbUAPSchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchOperState.setStatus("current")


class _Ieee8021BridgeEvbSchCdcpRemoteEnabled_Type(Integer32):
    """Custom type ieee8021BridgeEvbSchCdcpRemoteEnabled based on Integer32"""
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


_Ieee8021BridgeEvbSchCdcpRemoteEnabled_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSchCdcpRemoteEnabled_Object = MibTableColumn
ieee8021BridgeEvbSchCdcpRemoteEnabled = _Ieee8021BridgeEvbSchCdcpRemoteEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 11),
    _Ieee8021BridgeEvbSchCdcpRemoteEnabled_Type()
)
ieee8021BridgeEvbSchCdcpRemoteEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSchCdcpRemoteEnabled.setStatus("current")


class _Ieee8021BridgeEvbSchCdcpRemoteRole_Type(Integer32):
    """Custom type ieee8021BridgeEvbSchCdcpRemoteRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdcpRoleB", 1),
          ("cdcpRoleS", 2))
    )


_Ieee8021BridgeEvbSchCdcpRemoteRole_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSchCdcpRemoteRole_Object = MibTableColumn
ieee8021BridgeEvbSchCdcpRemoteRole = _Ieee8021BridgeEvbSchCdcpRemoteRole_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 12),
    _Ieee8021BridgeEvbSchCdcpRemoteRole_Type()
)
ieee8021BridgeEvbSchCdcpRemoteRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSchCdcpRemoteRole.setStatus("current")


class _Ieee8021BridgeEvbUAPConfigStorageType_Type(StorageType):
    """Custom type ieee8021BridgeEvbUAPConfigStorageType based on StorageType"""


_Ieee8021BridgeEvbUAPConfigStorageType_Object = MibTableColumn
ieee8021BridgeEvbUAPConfigStorageType = _Ieee8021BridgeEvbUAPConfigStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 13),
    _Ieee8021BridgeEvbUAPConfigStorageType_Type()
)
ieee8021BridgeEvbUAPConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPConfigStorageType.setStatus("current")
_Ieee8021BridgeEvbUAPConfigRowStatus_Type = RowStatus
_Ieee8021BridgeEvbUAPConfigRowStatus_Object = MibTableColumn
ieee8021BridgeEvbUAPConfigRowStatus = _Ieee8021BridgeEvbUAPConfigRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1, 14),
    _Ieee8021BridgeEvbUAPConfigRowStatus_Type()
)
ieee8021BridgeEvbUAPConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPConfigRowStatus.setStatus("current")
_Ieee8021BridgeEvbCAPConfigTable_Object = MibTable
ieee8021BridgeEvbCAPConfigTable = _Ieee8021BridgeEvbCAPConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPConfigTable.setStatus("current")
_Ieee8021BridgeEvbCAPConfigEntry_Object = MibTableRow
ieee8021BridgeEvbCAPConfigEntry = _Ieee8021BridgeEvbCAPConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2, 1)
)
ieee8021BridgeEvbCAPConfigEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePhyPort"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbSchID"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPConfigEntry.setStatus("current")


class _Ieee8021BridgeEvbSchID_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbSchID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Ieee8021BridgeEvbSchID_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbSchID_Object = MibTableColumn
ieee8021BridgeEvbSchID = _Ieee8021BridgeEvbSchID_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2, 1, 1),
    _Ieee8021BridgeEvbSchID_Type()
)
ieee8021BridgeEvbSchID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSchID.setStatus("current")
_Ieee8021BridgeEvbCAPComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbCAPComponentId_Object = MibTableColumn
ieee8021BridgeEvbCAPComponentId = _Ieee8021BridgeEvbCAPComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2, 1, 2),
    _Ieee8021BridgeEvbCAPComponentId_Type()
)
ieee8021BridgeEvbCAPComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPComponentId.setStatus("current")
_Ieee8021BridgeEvbCapConfigIfIndex_Type = InterfaceIndexOrZero
_Ieee8021BridgeEvbCapConfigIfIndex_Object = MibTableColumn
ieee8021BridgeEvbCapConfigIfIndex = _Ieee8021BridgeEvbCapConfigIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2, 1, 3),
    _Ieee8021BridgeEvbCapConfigIfIndex_Type()
)
ieee8021BridgeEvbCapConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCapConfigIfIndex.setStatus("current")
_Ieee8021BridgeEvbCAPPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbCAPPort_Object = MibTableColumn
ieee8021BridgeEvbCAPPort = _Ieee8021BridgeEvbCAPPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2, 1, 4),
    _Ieee8021BridgeEvbCAPPort_Type()
)
ieee8021BridgeEvbCAPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPPort.setStatus("current")
_Ieee8021BridgeEvbCAPSChannelID_Type = Unsigned32
_Ieee8021BridgeEvbCAPSChannelID_Object = MibTableColumn
ieee8021BridgeEvbCAPSChannelID = _Ieee8021BridgeEvbCAPSChannelID_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2, 1, 5),
    _Ieee8021BridgeEvbCAPSChannelID_Type()
)
ieee8021BridgeEvbCAPSChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPSChannelID.setStatus("current")
_Ieee8021BridgeEvbCAPAssociateSBPOrURPCompID_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbCAPAssociateSBPOrURPCompID_Object = MibTableColumn
ieee8021BridgeEvbCAPAssociateSBPOrURPCompID = _Ieee8021BridgeEvbCAPAssociateSBPOrURPCompID_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2, 1, 6),
    _Ieee8021BridgeEvbCAPAssociateSBPOrURPCompID_Type()
)
ieee8021BridgeEvbCAPAssociateSBPOrURPCompID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPAssociateSBPOrURPCompID.setStatus("current")
_Ieee8021BridgeEvbCAPAssociateSBPOrURPPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbCAPAssociateSBPOrURPPort_Object = MibTableColumn
ieee8021BridgeEvbCAPAssociateSBPOrURPPort = _Ieee8021BridgeEvbCAPAssociateSBPOrURPPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2, 1, 7),
    _Ieee8021BridgeEvbCAPAssociateSBPOrURPPort_Type()
)
ieee8021BridgeEvbCAPAssociateSBPOrURPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPAssociateSBPOrURPPort.setStatus("current")
_Ieee8021BridgeEvbCAPRowStatus_Type = RowStatus
_Ieee8021BridgeEvbCAPRowStatus_Object = MibTableColumn
ieee8021BridgeEvbCAPRowStatus = _Ieee8021BridgeEvbCAPRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 2, 1, 8),
    _Ieee8021BridgeEvbCAPRowStatus_Type()
)
ieee8021BridgeEvbCAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPRowStatus.setStatus("current")
_Ieee8021BridgeEvbURPTable_Object = MibTable
ieee8021BridgeEvbURPTable = _Ieee8021BridgeEvbURPTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPTable.setStatus("current")
_Ieee8021BridgeEvbURPEntry_Object = MibTableRow
ieee8021BridgeEvbURPEntry = _Ieee8021BridgeEvbURPEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1)
)
ieee8021BridgeEvbURPEntry.setIndexNames(
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPComponentId"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPPort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPEntry.setStatus("current")
_Ieee8021BridgeEvbURPComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbURPComponentId_Object = MibTableColumn
ieee8021BridgeEvbURPComponentId = _Ieee8021BridgeEvbURPComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 1),
    _Ieee8021BridgeEvbURPComponentId_Type()
)
ieee8021BridgeEvbURPComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPComponentId.setStatus("current")
_Ieee8021BridgeEvbURPPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbURPPort_Object = MibTableColumn
ieee8021BridgeEvbURPPort = _Ieee8021BridgeEvbURPPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 2),
    _Ieee8021BridgeEvbURPPort_Type()
)
ieee8021BridgeEvbURPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPPort.setStatus("current")
_Ieee8021BridgeEvbURPIfIndex_Type = InterfaceIndexOrZero
_Ieee8021BridgeEvbURPIfIndex_Object = MibTableColumn
ieee8021BridgeEvbURPIfIndex = _Ieee8021BridgeEvbURPIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 3),
    _Ieee8021BridgeEvbURPIfIndex_Type()
)
ieee8021BridgeEvbURPIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPIfIndex.setStatus("current")
_Ieee8021BridgeEvbURPBindToISSPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbURPBindToISSPort_Object = MibTableColumn
ieee8021BridgeEvbURPBindToISSPort = _Ieee8021BridgeEvbURPBindToISSPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 4),
    _Ieee8021BridgeEvbURPBindToISSPort_Type()
)
ieee8021BridgeEvbURPBindToISSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPBindToISSPort.setStatus("current")
_Ieee8021BridgeEvbURPLldpManual_Type = TruthValue
_Ieee8021BridgeEvbURPLldpManual_Object = MibTableColumn
ieee8021BridgeEvbURPLldpManual = _Ieee8021BridgeEvbURPLldpManual_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 6),
    _Ieee8021BridgeEvbURPLldpManual_Type()
)
ieee8021BridgeEvbURPLldpManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPLldpManual.setStatus("current")
_Ieee8021BridgeEvbURPVdpOperRsrcWaitDelay_Type = Unsigned32
_Ieee8021BridgeEvbURPVdpOperRsrcWaitDelay_Object = MibTableColumn
ieee8021BridgeEvbURPVdpOperRsrcWaitDelay = _Ieee8021BridgeEvbURPVdpOperRsrcWaitDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 9),
    _Ieee8021BridgeEvbURPVdpOperRsrcWaitDelay_Type()
)
ieee8021BridgeEvbURPVdpOperRsrcWaitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPVdpOperRsrcWaitDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPVdpOperRsrcWaitDelay.setUnits("micro-seconds")
_Ieee8021BridgeEvbURPVdpOperRespWaitDelay_Type = Unsigned32
_Ieee8021BridgeEvbURPVdpOperRespWaitDelay_Object = MibTableColumn
ieee8021BridgeEvbURPVdpOperRespWaitDelay = _Ieee8021BridgeEvbURPVdpOperRespWaitDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 10),
    _Ieee8021BridgeEvbURPVdpOperRespWaitDelay_Type()
)
ieee8021BridgeEvbURPVdpOperRespWaitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPVdpOperRespWaitDelay.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPVdpOperRespWaitDelay.setUnits("micro-seconds")
_Ieee8021BridgeEvbURPVdpOperReinitKeepAlive_Type = Unsigned32
_Ieee8021BridgeEvbURPVdpOperReinitKeepAlive_Object = MibTableColumn
ieee8021BridgeEvbURPVdpOperReinitKeepAlive = _Ieee8021BridgeEvbURPVdpOperReinitKeepAlive_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 11),
    _Ieee8021BridgeEvbURPVdpOperReinitKeepAlive_Type()
)
ieee8021BridgeEvbURPVdpOperReinitKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPVdpOperReinitKeepAlive.setStatus("deprecated")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPVdpOperReinitKeepAlive.setUnits("micro-seconds")


class _Ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp_Object = MibTableColumn
ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp = _Ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 12),
    _Ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp_Type()
)
ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp.setStatus("current")


class _Ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp_Object = MibTableColumn
ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp = _Ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 3, 1, 13),
    _Ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp_Type()
)
ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp.setStatus("current")
_Ieee8021BridgeEvbEcpTable_Object = MibTable
ieee8021BridgeEvbEcpTable = _Ieee8021BridgeEvbEcpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpTable.setStatus("current")
_Ieee8021BridgeEvbEcpEntry_Object = MibTableRow
ieee8021BridgeEvbEcpEntry = _Ieee8021BridgeEvbEcpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1)
)
ieee8021BridgeEvbEcpEntry.setIndexNames(
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpComponentId"),
    (0, "IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpPort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpEntry.setStatus("current")
_Ieee8021BridgeEvbEcpComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbEcpComponentId_Object = MibTableColumn
ieee8021BridgeEvbEcpComponentId = _Ieee8021BridgeEvbEcpComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1, 1),
    _Ieee8021BridgeEvbEcpComponentId_Type()
)
ieee8021BridgeEvbEcpComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpComponentId.setStatus("current")
_Ieee8021BridgeEvbEcpPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbEcpPort_Object = MibTableColumn
ieee8021BridgeEvbEcpPort = _Ieee8021BridgeEvbEcpPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1, 2),
    _Ieee8021BridgeEvbEcpPort_Type()
)
ieee8021BridgeEvbEcpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpPort.setStatus("current")
_Ieee8021BridgeEvbEcpOperAckTimerInit_Type = Unsigned32
_Ieee8021BridgeEvbEcpOperAckTimerInit_Object = MibTableColumn
ieee8021BridgeEvbEcpOperAckTimerInit = _Ieee8021BridgeEvbEcpOperAckTimerInit_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1, 3),
    _Ieee8021BridgeEvbEcpOperAckTimerInit_Type()
)
ieee8021BridgeEvbEcpOperAckTimerInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpOperAckTimerInit.setStatus("deprecated")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpOperAckTimerInit.setUnits("micro-seconds")
_Ieee8021BridgeEvbEcpOperMaxRetries_Type = Unsigned32
_Ieee8021BridgeEvbEcpOperMaxRetries_Object = MibTableColumn
ieee8021BridgeEvbEcpOperMaxRetries = _Ieee8021BridgeEvbEcpOperMaxRetries_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1, 4),
    _Ieee8021BridgeEvbEcpOperMaxRetries_Type()
)
ieee8021BridgeEvbEcpOperMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpOperMaxRetries.setStatus("current")
_Ieee8021BridgeEvbEcpTxFrameCount_Type = Counter32
_Ieee8021BridgeEvbEcpTxFrameCount_Object = MibTableColumn
ieee8021BridgeEvbEcpTxFrameCount = _Ieee8021BridgeEvbEcpTxFrameCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1, 5),
    _Ieee8021BridgeEvbEcpTxFrameCount_Type()
)
ieee8021BridgeEvbEcpTxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpTxFrameCount.setStatus("current")
_Ieee8021BridgeEvbEcpTxRetryCount_Type = Counter32
_Ieee8021BridgeEvbEcpTxRetryCount_Object = MibTableColumn
ieee8021BridgeEvbEcpTxRetryCount = _Ieee8021BridgeEvbEcpTxRetryCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1, 6),
    _Ieee8021BridgeEvbEcpTxRetryCount_Type()
)
ieee8021BridgeEvbEcpTxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpTxRetryCount.setStatus("current")
_Ieee8021BridgeEvbEcpTxFailures_Type = Counter32
_Ieee8021BridgeEvbEcpTxFailures_Object = MibTableColumn
ieee8021BridgeEvbEcpTxFailures = _Ieee8021BridgeEvbEcpTxFailures_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1, 7),
    _Ieee8021BridgeEvbEcpTxFailures_Type()
)
ieee8021BridgeEvbEcpTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpTxFailures.setStatus("current")
_Ieee8021BridgeEvbEcpRxFrameCount_Type = Counter32
_Ieee8021BridgeEvbEcpRxFrameCount_Object = MibTableColumn
ieee8021BridgeEvbEcpRxFrameCount = _Ieee8021BridgeEvbEcpRxFrameCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1, 8),
    _Ieee8021BridgeEvbEcpRxFrameCount_Type()
)
ieee8021BridgeEvbEcpRxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpRxFrameCount.setStatus("current")


class _Ieee8021BridgeEvbEcpOperAckTimerInitExp_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbEcpOperAckTimerInitExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Ieee8021BridgeEvbEcpOperAckTimerInitExp_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbEcpOperAckTimerInitExp_Object = MibTableColumn
ieee8021BridgeEvbEcpOperAckTimerInitExp = _Ieee8021BridgeEvbEcpOperAckTimerInitExp_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 4, 1, 9),
    _Ieee8021BridgeEvbEcpOperAckTimerInitExp_Type()
)
ieee8021BridgeEvbEcpOperAckTimerInitExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpOperAckTimerInitExp.setStatus("current")
_Ieee8021BridgeEvbConformance_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbConformance = _Ieee8021BridgeEvbConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 2)
)
_Ieee8021BridgeEvbGroups_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbGroups = _Ieee8021BridgeEvbGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1)
)
_Ieee8021BridgeEvbCompliances_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbCompliances = _Ieee8021BridgeEvbCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2)
)

# Managed Objects groups

ieee8021BridgeEvbSysGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 1)
)
ieee8021BridgeEvbSysGroup.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysType"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysNumExternalPorts"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEvbLldpTxEnable"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEvbLldpGidCapable"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEvbLldpManual"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEcpAckTimer"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEcpMaxRetries"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysVdpDfltReinitKeepAlive"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysGroup.setStatus("deprecated")

ieee8021BridgeEvbSbpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 3)
)
ieee8021BridgeEvbSbpGroup.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpLldpManual"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpVdpOperReinitKeepAlive"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpVdpOperToutKeepAlive"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpGroup.setStatus("deprecated")

ieee8021BridgeEvbVSIDBGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 4)
)
ieee8021BridgeEvbVSIDBGroup.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSITimeSinceCreate"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVsiVdpOperCmd"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVsiOperRevert"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVsiOperHard"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVsiOperReason"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIMgrID"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIType"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSITypeVersion"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIMvFormat"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSINumMACs"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPMachineState"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPCommandsSucceeded"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPCommandsFailed"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPCommandReverts"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPCounterDiscontinuity"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIVlanId"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBGroup.setStatus("deprecated")

ieee8021BridgeEvbUAPGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 5)
)
ieee8021BridgeEvbUAPGroup.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPComponentId"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPPort"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUapConfigIfIndex"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPSchCdcpAdminEnable"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPSchAdminCDCPRole"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPSchAdminCDCPChanCap"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPSchOperCDCPChanCap"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPSchOperState"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSchCdcpRemoteEnabled"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSchCdcpRemoteRole"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPConfigStorageType"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbUAPConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPGroup.setStatus("current")

ieee8021BridgeEvbCAPConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 6)
)
ieee8021BridgeEvbCAPConfigGroup.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbCAPComponentId"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbCapConfigIfIndex"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbCAPPort"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbCAPSChannelID"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbCAPAssociateSBPOrURPCompID"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbCAPAssociateSBPOrURPPort"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbCAPRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPConfigGroup.setStatus("current")

ieee8021BridgeEvbsURPGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 7)
)
ieee8021BridgeEvbsURPGroup.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPIfIndex"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPBindToISSPort"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPLldpManual"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPVdpOperRsrcWaitDelay"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPVdpOperRespWaitDelay"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPVdpOperReinitKeepAlive"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbsURPGroup.setStatus("deprecated")

ieee8021BridgeEvbEcpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 8)
)
ieee8021BridgeEvbEcpGroup.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpOperAckTimerInit"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpOperMaxRetries"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpTxFrameCount"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpTxRetryCount"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpTxFailures"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpRxFrameCount"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpGroup.setStatus("deprecated")

ieee8021BridgeEvbSysV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 9)
)
ieee8021BridgeEvbSysV2Group.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysType"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysNumExternalPorts"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEvbLldpTxEnable"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEvbLldpGidCapable"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEvbLldpManual"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEcpDfltAckTimerExp"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysEcpMaxRetries"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysV2Group.setStatus("current")

ieee8021BridgeEvbSbpV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 10)
)
ieee8021BridgeEvbSbpV2Group.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpLldpManual"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbSbpVdpOperToutKeepAlive"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSbpV2Group.setStatus("current")

ieee8021BridgeEvbVSIDBV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 11)
)
ieee8021BridgeEvbVSIDBV2Group.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSITimeSinceCreate"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVsiVdpOperCmd"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVsiOperRevert"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVsiOperHard"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVsiOperReason"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIMgrID16"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIType"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSITypeVersion"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIFilterFormat"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSINumMACs"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPMachineState"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPCommandsSucceeded"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPCommandsFailed"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPCommandReverts"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVDPCounterDiscontinuity"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbVSIVlanId"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBV2Group.setStatus("current")

ieee8021BridgeEvbsURPV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 12)
)
ieee8021BridgeEvbsURPV2Group.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPIfIndex"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPBindToISSPort"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPLldpManual"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPVdpOperRespWaitDelay"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbsURPV2Group.setStatus("current")

ieee8021BridgeEvbEcpV2Group = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 13)
)
ieee8021BridgeEvbEcpV2Group.setObjects(
      *(("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpOperAckTimerInitExp"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpOperMaxRetries"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpTxFrameCount"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpTxRetryCount"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpTxFailures"),
        ("IEEE8021-EVB-MIB", "ieee8021BridgeEvbEcpRxFrameCount"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbEcpV2Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021BridgeEvbbCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbbCompliance.setStatus(
        "deprecated"
    )

ieee8021BridgeEvbsCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbsCompliance.setStatus(
        "deprecated"
    )

ieee8021BridgeEvbbComplianceV2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 3)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbbComplianceV2.setStatus(
        "current"
    )

ieee8021BridgeEvbsComplianceV2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbsComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-EVB-MIB",
    **{"ieee8021BridgeEvbMib": ieee8021BridgeEvbMib,
       "ieee8021BridgeEvbNotifications": ieee8021BridgeEvbNotifications,
       "ieee8021BridgeEvbObjects": ieee8021BridgeEvbObjects,
       "ieee8021BridgeEvbSys": ieee8021BridgeEvbSys,
       "ieee8021BridgeEvbSysType": ieee8021BridgeEvbSysType,
       "ieee8021BridgeEvbSysNumExternalPorts": ieee8021BridgeEvbSysNumExternalPorts,
       "ieee8021BridgeEvbSysEvbLldpTxEnable": ieee8021BridgeEvbSysEvbLldpTxEnable,
       "ieee8021BridgeEvbSysEvbLldpManual": ieee8021BridgeEvbSysEvbLldpManual,
       "ieee8021BridgeEvbSysEvbLldpGidCapable": ieee8021BridgeEvbSysEvbLldpGidCapable,
       "ieee8021BridgeEvbSysEcpAckTimer": ieee8021BridgeEvbSysEcpAckTimer,
       "ieee8021BridgeEvbSysEcpMaxRetries": ieee8021BridgeEvbSysEcpMaxRetries,
       "ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay": ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay,
       "ieee8021BridgeEvbSysVdpDfltReinitKeepAlive": ieee8021BridgeEvbSysVdpDfltReinitKeepAlive,
       "ieee8021BridgeEvbSbpTable": ieee8021BridgeEvbSbpTable,
       "ieee8021BridgeEvbSbpEntry": ieee8021BridgeEvbSbpEntry,
       "ieee8021BridgeEvbSbpComponentID": ieee8021BridgeEvbSbpComponentID,
       "ieee8021BridgeEvbSbpPortNumber": ieee8021BridgeEvbSbpPortNumber,
       "ieee8021BridgeEvbSbpLldpManual": ieee8021BridgeEvbSbpLldpManual,
       "ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay": ieee8021BridgeEvbSbpVdpOperRsrcWaitDelay,
       "ieee8021BridgeEvbSbpVdpOperReinitKeepAlive": ieee8021BridgeEvbSbpVdpOperReinitKeepAlive,
       "ieee8021BridgeEvbSbpVdpOperToutKeepAlive": ieee8021BridgeEvbSbpVdpOperToutKeepAlive,
       "ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp": ieee8021BridgeEvbSbpVdpOperRsrcWaitDelayExp,
       "ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp": ieee8021BridgeEvbSbpVdpOperReinitKeepAliveExp,
       "ieee8021BridgeEvbSysEcpDfltAckTimerExp": ieee8021BridgeEvbSysEcpDfltAckTimerExp,
       "ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp": ieee8021BridgeEvbSysVdpDfltRsrcWaitDelayExp,
       "ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp": ieee8021BridgeEvbSysVdpDfltReinitKeepAliveExp,
       "ieee8021BridgeEvbVSIDBObjects": ieee8021BridgeEvbVSIDBObjects,
       "ieee8021BridgeEvbVSIDBTable": ieee8021BridgeEvbVSIDBTable,
       "ieee8021BridgeEvbVSIDBEntry": ieee8021BridgeEvbVSIDBEntry,
       "ieee8021BridgeEvbVSIComponentID": ieee8021BridgeEvbVSIComponentID,
       "ieee8021BridgeEvbVSIPortNumber": ieee8021BridgeEvbVSIPortNumber,
       "ieee8021BridgeEvbVSIIDType": ieee8021BridgeEvbVSIIDType,
       "ieee8021BridgeEvbVSIID": ieee8021BridgeEvbVSIID,
       "ieee8021BridgeEvbVSITimeSinceCreate": ieee8021BridgeEvbVSITimeSinceCreate,
       "ieee8021BridgeEvbVsiVdpOperCmd": ieee8021BridgeEvbVsiVdpOperCmd,
       "ieee8021BridgeEvbVsiOperRevert": ieee8021BridgeEvbVsiOperRevert,
       "ieee8021BridgeEvbVsiOperHard": ieee8021BridgeEvbVsiOperHard,
       "ieee8021BridgeEvbVsiOperReason": ieee8021BridgeEvbVsiOperReason,
       "ieee8021BridgeEvbVSIMgrID": ieee8021BridgeEvbVSIMgrID,
       "ieee8021BridgeEvbVSIType": ieee8021BridgeEvbVSIType,
       "ieee8021BridgeEvbVSITypeVersion": ieee8021BridgeEvbVSITypeVersion,
       "ieee8021BridgeEvbVSIMvFormat": ieee8021BridgeEvbVSIMvFormat,
       "ieee8021BridgeEvbVSINumMACs": ieee8021BridgeEvbVSINumMACs,
       "ieee8021BridgeEvbVDPMachineState": ieee8021BridgeEvbVDPMachineState,
       "ieee8021BridgeEvbVDPCommandsSucceeded": ieee8021BridgeEvbVDPCommandsSucceeded,
       "ieee8021BridgeEvbVDPCommandsFailed": ieee8021BridgeEvbVDPCommandsFailed,
       "ieee8021BridgeEvbVDPCommandReverts": ieee8021BridgeEvbVDPCommandReverts,
       "ieee8021BridgeEvbVDPCounterDiscontinuity": ieee8021BridgeEvbVDPCounterDiscontinuity,
       "ieee8021BridgeEvbVSIMgrID16": ieee8021BridgeEvbVSIMgrID16,
       "ieee8021BridgeEvbVSIFilterFormat": ieee8021BridgeEvbVSIFilterFormat,
       "ieee8021BridgeEvbVSIDBMacTable": ieee8021BridgeEvbVSIDBMacTable,
       "ieee8021BridgeEvbVSIDBMacEntry": ieee8021BridgeEvbVSIDBMacEntry,
       "ieee8021BridgeEvbGroupID": ieee8021BridgeEvbGroupID,
       "ieee8021BridgeEvbVSIMac": ieee8021BridgeEvbVSIMac,
       "ieee8021BridgeEvbVSIVlanId": ieee8021BridgeEvbVSIVlanId,
       "ieee8021BridgeEvbSChannelObjects": ieee8021BridgeEvbSChannelObjects,
       "ieee8021BridgeEvbUAPConfigTable": ieee8021BridgeEvbUAPConfigTable,
       "ieee8021BridgeEvbUAPConfigEntry": ieee8021BridgeEvbUAPConfigEntry,
       "ieee8021BridgeEvbUAPComponentId": ieee8021BridgeEvbUAPComponentId,
       "ieee8021BridgeEvbUAPPort": ieee8021BridgeEvbUAPPort,
       "ieee8021BridgeEvbUapConfigIfIndex": ieee8021BridgeEvbUapConfigIfIndex,
       "ieee8021BridgeEvbUAPSchCdcpAdminEnable": ieee8021BridgeEvbUAPSchCdcpAdminEnable,
       "ieee8021BridgeEvbUAPSchAdminCDCPRole": ieee8021BridgeEvbUAPSchAdminCDCPRole,
       "ieee8021BridgeEvbUAPSchAdminCDCPChanCap": ieee8021BridgeEvbUAPSchAdminCDCPChanCap,
       "ieee8021BridgeEvbUAPSchOperCDCPChanCap": ieee8021BridgeEvbUAPSchOperCDCPChanCap,
       "ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow": ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow,
       "ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh": ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh,
       "ieee8021BridgeEvbUAPSchOperState": ieee8021BridgeEvbUAPSchOperState,
       "ieee8021BridgeEvbSchCdcpRemoteEnabled": ieee8021BridgeEvbSchCdcpRemoteEnabled,
       "ieee8021BridgeEvbSchCdcpRemoteRole": ieee8021BridgeEvbSchCdcpRemoteRole,
       "ieee8021BridgeEvbUAPConfigStorageType": ieee8021BridgeEvbUAPConfigStorageType,
       "ieee8021BridgeEvbUAPConfigRowStatus": ieee8021BridgeEvbUAPConfigRowStatus,
       "ieee8021BridgeEvbCAPConfigTable": ieee8021BridgeEvbCAPConfigTable,
       "ieee8021BridgeEvbCAPConfigEntry": ieee8021BridgeEvbCAPConfigEntry,
       "ieee8021BridgeEvbSchID": ieee8021BridgeEvbSchID,
       "ieee8021BridgeEvbCAPComponentId": ieee8021BridgeEvbCAPComponentId,
       "ieee8021BridgeEvbCapConfigIfIndex": ieee8021BridgeEvbCapConfigIfIndex,
       "ieee8021BridgeEvbCAPPort": ieee8021BridgeEvbCAPPort,
       "ieee8021BridgeEvbCAPSChannelID": ieee8021BridgeEvbCAPSChannelID,
       "ieee8021BridgeEvbCAPAssociateSBPOrURPCompID": ieee8021BridgeEvbCAPAssociateSBPOrURPCompID,
       "ieee8021BridgeEvbCAPAssociateSBPOrURPPort": ieee8021BridgeEvbCAPAssociateSBPOrURPPort,
       "ieee8021BridgeEvbCAPRowStatus": ieee8021BridgeEvbCAPRowStatus,
       "ieee8021BridgeEvbURPTable": ieee8021BridgeEvbURPTable,
       "ieee8021BridgeEvbURPEntry": ieee8021BridgeEvbURPEntry,
       "ieee8021BridgeEvbURPComponentId": ieee8021BridgeEvbURPComponentId,
       "ieee8021BridgeEvbURPPort": ieee8021BridgeEvbURPPort,
       "ieee8021BridgeEvbURPIfIndex": ieee8021BridgeEvbURPIfIndex,
       "ieee8021BridgeEvbURPBindToISSPort": ieee8021BridgeEvbURPBindToISSPort,
       "ieee8021BridgeEvbURPLldpManual": ieee8021BridgeEvbURPLldpManual,
       "ieee8021BridgeEvbURPVdpOperRsrcWaitDelay": ieee8021BridgeEvbURPVdpOperRsrcWaitDelay,
       "ieee8021BridgeEvbURPVdpOperRespWaitDelay": ieee8021BridgeEvbURPVdpOperRespWaitDelay,
       "ieee8021BridgeEvbURPVdpOperReinitKeepAlive": ieee8021BridgeEvbURPVdpOperReinitKeepAlive,
       "ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp": ieee8021BridgeEvbURPVdpOperRsrcWaitDelayExp,
       "ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp": ieee8021BridgeEvbURPVdpOperReinitKeepAliveExp,
       "ieee8021BridgeEvbEcpTable": ieee8021BridgeEvbEcpTable,
       "ieee8021BridgeEvbEcpEntry": ieee8021BridgeEvbEcpEntry,
       "ieee8021BridgeEvbEcpComponentId": ieee8021BridgeEvbEcpComponentId,
       "ieee8021BridgeEvbEcpPort": ieee8021BridgeEvbEcpPort,
       "ieee8021BridgeEvbEcpOperAckTimerInit": ieee8021BridgeEvbEcpOperAckTimerInit,
       "ieee8021BridgeEvbEcpOperMaxRetries": ieee8021BridgeEvbEcpOperMaxRetries,
       "ieee8021BridgeEvbEcpTxFrameCount": ieee8021BridgeEvbEcpTxFrameCount,
       "ieee8021BridgeEvbEcpTxRetryCount": ieee8021BridgeEvbEcpTxRetryCount,
       "ieee8021BridgeEvbEcpTxFailures": ieee8021BridgeEvbEcpTxFailures,
       "ieee8021BridgeEvbEcpRxFrameCount": ieee8021BridgeEvbEcpRxFrameCount,
       "ieee8021BridgeEvbEcpOperAckTimerInitExp": ieee8021BridgeEvbEcpOperAckTimerInitExp,
       "ieee8021BridgeEvbConformance": ieee8021BridgeEvbConformance,
       "ieee8021BridgeEvbGroups": ieee8021BridgeEvbGroups,
       "ieee8021BridgeEvbSysGroup": ieee8021BridgeEvbSysGroup,
       "ieee8021BridgeEvbSbpGroup": ieee8021BridgeEvbSbpGroup,
       "ieee8021BridgeEvbVSIDBGroup": ieee8021BridgeEvbVSIDBGroup,
       "ieee8021BridgeEvbUAPGroup": ieee8021BridgeEvbUAPGroup,
       "ieee8021BridgeEvbCAPConfigGroup": ieee8021BridgeEvbCAPConfigGroup,
       "ieee8021BridgeEvbsURPGroup": ieee8021BridgeEvbsURPGroup,
       "ieee8021BridgeEvbEcpGroup": ieee8021BridgeEvbEcpGroup,
       "ieee8021BridgeEvbSysV2Group": ieee8021BridgeEvbSysV2Group,
       "ieee8021BridgeEvbSbpV2Group": ieee8021BridgeEvbSbpV2Group,
       "ieee8021BridgeEvbVSIDBV2Group": ieee8021BridgeEvbVSIDBV2Group,
       "ieee8021BridgeEvbsURPV2Group": ieee8021BridgeEvbsURPV2Group,
       "ieee8021BridgeEvbEcpV2Group": ieee8021BridgeEvbEcpV2Group,
       "ieee8021BridgeEvbCompliances": ieee8021BridgeEvbCompliances,
       "ieee8021BridgeEvbbCompliance": ieee8021BridgeEvbbCompliance,
       "ieee8021BridgeEvbsCompliance": ieee8021BridgeEvbsCompliance,
       "ieee8021BridgeEvbbComplianceV2": ieee8021BridgeEvbbComplianceV2,
       "ieee8021BridgeEvbsComplianceV2": ieee8021BridgeEvbsComplianceV2}
)
