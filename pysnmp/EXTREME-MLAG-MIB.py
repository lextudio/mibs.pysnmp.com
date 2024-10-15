# SNMP MIB module (EXTREME-MLAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-MLAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:50 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

extremeMlag = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41)
)
extremeMlag.setRevisions(
        ("2012-08-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeMlagObjects_ObjectIdentity = ObjectIdentity
extremeMlagObjects = _ExtremeMlagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1)
)
_ExtremeMlagPeerTable_Object = MibTable
extremeMlagPeerTable = _ExtremeMlagPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1)
)
if mibBuilder.loadTexts:
    extremeMlagPeerTable.setStatus("current")
_ExtremeMlagPeerEntry_Object = MibTableRow
extremeMlagPeerEntry = _ExtremeMlagPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1)
)
extremeMlagPeerEntry.setIndexNames(
    (0, "EXTREME-MLAG-MIB", "extremeMlagPeerName"),
)
if mibBuilder.loadTexts:
    extremeMlagPeerEntry.setStatus("current")


class _ExtremeMlagPeerName_Type(DisplayString):
    """Custom type extremeMlagPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeMlagPeerName_Type.__name__ = "DisplayString"
_ExtremeMlagPeerName_Object = MibTableColumn
extremeMlagPeerName = _ExtremeMlagPeerName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 1),
    _ExtremeMlagPeerName_Type()
)
extremeMlagPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerName.setStatus("current")


class _ExtremeMlagPeerVlan_Type(DisplayString):
    """Custom type extremeMlagPeerVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeMlagPeerVlan_Type.__name__ = "DisplayString"
_ExtremeMlagPeerVlan_Object = MibTableColumn
extremeMlagPeerVlan = _ExtremeMlagPeerVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 2),
    _ExtremeMlagPeerVlan_Type()
)
extremeMlagPeerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerVlan.setStatus("current")


class _ExtremeMlagPeerVR_Type(DisplayString):
    """Custom type extremeMlagPeerVR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeMlagPeerVR_Type.__name__ = "DisplayString"
_ExtremeMlagPeerVR_Object = MibTableColumn
extremeMlagPeerVR = _ExtremeMlagPeerVR_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 3),
    _ExtremeMlagPeerVR_Type()
)
extremeMlagPeerVR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagPeerVR.setStatus("current")
_ExtremeMlagLocalAddrType_Type = InetAddressType
_ExtremeMlagLocalAddrType_Object = MibTableColumn
extremeMlagLocalAddrType = _ExtremeMlagLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 4),
    _ExtremeMlagLocalAddrType_Type()
)
extremeMlagLocalAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagLocalAddrType.setStatus("current")
_ExtremeMlagLocalIP_Type = InetAddress
_ExtremeMlagLocalIP_Object = MibTableColumn
extremeMlagLocalIP = _ExtremeMlagLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 5),
    _ExtremeMlagLocalIP_Type()
)
extremeMlagLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagLocalIP.setStatus("current")
_ExtremeMlagPeerAddrType_Type = InetAddressType
_ExtremeMlagPeerAddrType_Object = MibTableColumn
extremeMlagPeerAddrType = _ExtremeMlagPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 6),
    _ExtremeMlagPeerAddrType_Type()
)
extremeMlagPeerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagPeerAddrType.setStatus("current")
_ExtremeMlagPeerIP_Type = InetAddress
_ExtremeMlagPeerIP_Object = MibTableColumn
extremeMlagPeerIP = _ExtremeMlagPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 7),
    _ExtremeMlagPeerIP_Type()
)
extremeMlagPeerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagPeerIP.setStatus("current")
_ExtremeMlagPeerPortCount_Type = Integer32
_ExtremeMlagPeerPortCount_Object = MibTableColumn
extremeMlagPeerPortCount = _ExtremeMlagPeerPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 8),
    _ExtremeMlagPeerPortCount_Type()
)
extremeMlagPeerPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerPortCount.setStatus("current")


class _ExtremeMlagPeerCheckPointStatus_Type(Integer32):
    """Custom type extremeMlagPeerCheckPointStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ExtremeMlagPeerCheckPointStatus_Type.__name__ = "Integer32"
_ExtremeMlagPeerCheckPointStatus_Object = MibTableColumn
extremeMlagPeerCheckPointStatus = _ExtremeMlagPeerCheckPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 9),
    _ExtremeMlagPeerCheckPointStatus_Type()
)
extremeMlagPeerCheckPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerCheckPointStatus.setStatus("current")
_ExtremeMlagPeerRxHellos_Type = Counter32
_ExtremeMlagPeerRxHellos_Object = MibTableColumn
extremeMlagPeerRxHellos = _ExtremeMlagPeerRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 10),
    _ExtremeMlagPeerRxHellos_Type()
)
extremeMlagPeerRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerRxHellos.setStatus("current")
_ExtremeMlagPeerRxCheckpointMsgs_Type = Counter32
_ExtremeMlagPeerRxCheckpointMsgs_Object = MibTableColumn
extremeMlagPeerRxCheckpointMsgs = _ExtremeMlagPeerRxCheckpointMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 11),
    _ExtremeMlagPeerRxCheckpointMsgs_Type()
)
extremeMlagPeerRxCheckpointMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerRxCheckpointMsgs.setStatus("current")
_ExtremeMlagPeerHelloErrors_Type = Counter32
_ExtremeMlagPeerHelloErrors_Object = MibTableColumn
extremeMlagPeerHelloErrors = _ExtremeMlagPeerHelloErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 12),
    _ExtremeMlagPeerHelloErrors_Type()
)
extremeMlagPeerHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerHelloErrors.setStatus("current")
_ExtremeMlagPeerHelloTimeouts_Type = Counter32
_ExtremeMlagPeerHelloTimeouts_Object = MibTableColumn
extremeMlagPeerHelloTimeouts = _ExtremeMlagPeerHelloTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 13),
    _ExtremeMlagPeerHelloTimeouts_Type()
)
extremeMlagPeerHelloTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerHelloTimeouts.setStatus("current")
_ExtremeMlagPeerUptime_Type = TimeStamp
_ExtremeMlagPeerUptime_Object = MibTableColumn
extremeMlagPeerUptime = _ExtremeMlagPeerUptime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 14),
    _ExtremeMlagPeerUptime_Type()
)
extremeMlagPeerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerUptime.setStatus("current")


class _ExtremeMlagPeerLocalTxInterval_Type(Integer32):
    """Custom type extremeMlagPeerLocalTxInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_ExtremeMlagPeerLocalTxInterval_Type.__name__ = "Integer32"
_ExtremeMlagPeerLocalTxInterval_Object = MibTableColumn
extremeMlagPeerLocalTxInterval = _ExtremeMlagPeerLocalTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 15),
    _ExtremeMlagPeerLocalTxInterval_Type()
)
extremeMlagPeerLocalTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagPeerLocalTxInterval.setStatus("current")


class _ExtremeMlagPeerRemoteTxInterval_Type(Integer32):
    """Custom type extremeMlagPeerRemoteTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_ExtremeMlagPeerRemoteTxInterval_Type.__name__ = "Integer32"
_ExtremeMlagPeerRemoteTxInterval_Object = MibTableColumn
extremeMlagPeerRemoteTxInterval = _ExtremeMlagPeerRemoteTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 16),
    _ExtremeMlagPeerRemoteTxInterval_Type()
)
extremeMlagPeerRemoteTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerRemoteTxInterval.setStatus("current")
_ExtremeMlagPeerTxHellos_Type = Counter32
_ExtremeMlagPeerTxHellos_Object = MibTableColumn
extremeMlagPeerTxHellos = _ExtremeMlagPeerTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 17),
    _ExtremeMlagPeerTxHellos_Type()
)
extremeMlagPeerTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerTxHellos.setStatus("current")
_ExtremeMlagPeerTxCheckpoints_Type = Counter32
_ExtremeMlagPeerTxCheckpoints_Object = MibTableColumn
extremeMlagPeerTxCheckpoints = _ExtremeMlagPeerTxCheckpoints_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 18),
    _ExtremeMlagPeerTxCheckpoints_Type()
)
extremeMlagPeerTxCheckpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerTxCheckpoints.setStatus("current")
_ExtremeMlagPeerCheckpointErrors_Type = Counter32
_ExtremeMlagPeerCheckpointErrors_Object = MibTableColumn
extremeMlagPeerCheckpointErrors = _ExtremeMlagPeerCheckpointErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 19),
    _ExtremeMlagPeerCheckpointErrors_Type()
)
extremeMlagPeerCheckpointErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerCheckpointErrors.setStatus("current")
_ExtremeMlagPeerConnnectErrors_Type = Counter32
_ExtremeMlagPeerConnnectErrors_Object = MibTableColumn
extremeMlagPeerConnnectErrors = _ExtremeMlagPeerConnnectErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 20),
    _ExtremeMlagPeerConnnectErrors_Type()
)
extremeMlagPeerConnnectErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerConnnectErrors.setStatus("current")
_ExtremeMlagPeerRowStatus_Type = RowStatus
_ExtremeMlagPeerRowStatus_Object = MibTableColumn
extremeMlagPeerRowStatus = _ExtremeMlagPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 21),
    _ExtremeMlagPeerRowStatus_Type()
)
extremeMlagPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerRowStatus.setStatus("current")
_ExtremeMlagPeerCfgLacpMac_Type = MacAddress
_ExtremeMlagPeerCfgLacpMac_Object = MibTableColumn
extremeMlagPeerCfgLacpMac = _ExtremeMlagPeerCfgLacpMac_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 22),
    _ExtremeMlagPeerCfgLacpMac_Type()
)
extremeMlagPeerCfgLacpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerCfgLacpMac.setStatus("current")
_ExtremeMlagPeerOperLacpMac_Type = MacAddress
_ExtremeMlagPeerOperLacpMac_Object = MibTableColumn
extremeMlagPeerOperLacpMac = _ExtremeMlagPeerOperLacpMac_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 23),
    _ExtremeMlagPeerOperLacpMac_Type()
)
extremeMlagPeerOperLacpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerOperLacpMac.setStatus("current")
_ExtremeMlagPortTable_Object = MibTable
extremeMlagPortTable = _ExtremeMlagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2)
)
if mibBuilder.loadTexts:
    extremeMlagPortTable.setStatus("current")
_ExtremeMlagPortEntry_Object = MibTableRow
extremeMlagPortEntry = _ExtremeMlagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1)
)
extremeMlagPortEntry.setIndexNames(
    (0, "EXTREME-MLAG-MIB", "extremeMlagPortLocalPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeMlagPortEntry.setStatus("current")
_ExtremeMlagPortLocalPortIfIndex_Type = Unsigned32
_ExtremeMlagPortLocalPortIfIndex_Object = MibTableColumn
extremeMlagPortLocalPortIfIndex = _ExtremeMlagPortLocalPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 1),
    _ExtremeMlagPortLocalPortIfIndex_Type()
)
extremeMlagPortLocalPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagPortLocalPortIfIndex.setStatus("current")


class _ExtremeMlagPortId_Type(Integer32):
    """Custom type extremeMlagPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_ExtremeMlagPortId_Type.__name__ = "Integer32"
_ExtremeMlagPortId_Object = MibTableColumn
extremeMlagPortId = _ExtremeMlagPortId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 2),
    _ExtremeMlagPortId_Type()
)
extremeMlagPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPortId.setStatus("current")
_ExtremeMlagPortPeer_Type = DisplayString
_ExtremeMlagPortPeer_Object = MibTableColumn
extremeMlagPortPeer = _ExtremeMlagPortPeer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 3),
    _ExtremeMlagPortPeer_Type()
)
extremeMlagPortPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagPortPeer.setStatus("current")


class _ExtremeMlagPortLocalLinkStatus_Type(Integer32):
    """Custom type extremeMlagPortLocalLinkStatus based on Integer32"""
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
        *(("active", 1),
          ("disabled", 2),
          ("portNotPresent", 4),
          ("ready", 3))
    )


_ExtremeMlagPortLocalLinkStatus_Type.__name__ = "Integer32"
_ExtremeMlagPortLocalLinkStatus_Object = MibTableColumn
extremeMlagPortLocalLinkStatus = _ExtremeMlagPortLocalLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 4),
    _ExtremeMlagPortLocalLinkStatus_Type()
)
extremeMlagPortLocalLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortLocalLinkStatus.setStatus("current")


class _ExtremeMlagPortRemoteLinkStatus_Type(Integer32):
    """Custom type extremeMlagPortRemoteLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notAvailable", 3),
          ("up", 1))
    )


_ExtremeMlagPortRemoteLinkStatus_Type.__name__ = "Integer32"
_ExtremeMlagPortRemoteLinkStatus_Object = MibTableColumn
extremeMlagPortRemoteLinkStatus = _ExtremeMlagPortRemoteLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 5),
    _ExtremeMlagPortRemoteLinkStatus_Type()
)
extremeMlagPortRemoteLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortRemoteLinkStatus.setStatus("current")


class _ExtremeMlagPortPeerState_Type(Integer32):
    """Custom type extremeMlagPortPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ExtremeMlagPortPeerState_Type.__name__ = "Integer32"
_ExtremeMlagPortPeerState_Object = MibTableColumn
extremeMlagPortPeerState = _ExtremeMlagPortPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 6),
    _ExtremeMlagPortPeerState_Type()
)
extremeMlagPortPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortPeerState.setStatus("current")
_ExtremeMlagPortLocalFailures_Type = Counter32
_ExtremeMlagPortLocalFailures_Object = MibTableColumn
extremeMlagPortLocalFailures = _ExtremeMlagPortLocalFailures_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 7),
    _ExtremeMlagPortLocalFailures_Type()
)
extremeMlagPortLocalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortLocalFailures.setStatus("current")
_ExtremeMlagPortRemoteFailures_Type = Counter32
_ExtremeMlagPortRemoteFailures_Object = MibTableColumn
extremeMlagPortRemoteFailures = _ExtremeMlagPortRemoteFailures_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 8),
    _ExtremeMlagPortRemoteFailures_Type()
)
extremeMlagPortRemoteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortRemoteFailures.setStatus("current")
_ExtremeMlagPortRowStatus_Type = RowStatus
_ExtremeMlagPortRowStatus_Object = MibTableColumn
extremeMlagPortRowStatus = _ExtremeMlagPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 9),
    _ExtremeMlagPortRowStatus_Type()
)
extremeMlagPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPortRowStatus.setStatus("current")


class _ExtremeMlagConvergenceControl_Type(Integer32):
    """Custom type extremeMlagConvergenceControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conserveAccessLists", 2),
          ("fastConvergence", 1))
    )


_ExtremeMlagConvergenceControl_Type.__name__ = "Integer32"
_ExtremeMlagConvergenceControl_Object = MibScalar
extremeMlagConvergenceControl = _ExtremeMlagConvergenceControl_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 3),
    _ExtremeMlagConvergenceControl_Type()
)
extremeMlagConvergenceControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagConvergenceControl.setStatus("current")
_ExtremeMlagNotificationObjects_ObjectIdentity = ObjectIdentity
extremeMlagNotificationObjects = _ExtremeMlagNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 2)
)
_ExtremeMlagNotifications_ObjectIdentity = ObjectIdentity
extremeMlagNotifications = _ExtremeMlagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3)
)
_ExtremeMlagNotificationsPrefix_ObjectIdentity = ObjectIdentity
extremeMlagNotificationsPrefix = _ExtremeMlagNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3, 0)
)

# Managed Objects groups


# Notification objects

extremeMlagPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3, 0, 1)
)
extremeMlagPeerUp.setObjects(
    ("EXTREME-MLAG-MIB", "extremeMlagPeerName")
)
if mibBuilder.loadTexts:
    extremeMlagPeerUp.setStatus(
        "current"
    )

extremeMlagPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3, 0, 2)
)
extremeMlagPeerDown.setObjects(
    ("EXTREME-MLAG-MIB", "extremeMlagPeerName")
)
if mibBuilder.loadTexts:
    extremeMlagPeerDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-MLAG-MIB",
    **{"extremeMlag": extremeMlag,
       "extremeMlagObjects": extremeMlagObjects,
       "extremeMlagPeerTable": extremeMlagPeerTable,
       "extremeMlagPeerEntry": extremeMlagPeerEntry,
       "extremeMlagPeerName": extremeMlagPeerName,
       "extremeMlagPeerVlan": extremeMlagPeerVlan,
       "extremeMlagPeerVR": extremeMlagPeerVR,
       "extremeMlagLocalAddrType": extremeMlagLocalAddrType,
       "extremeMlagLocalIP": extremeMlagLocalIP,
       "extremeMlagPeerAddrType": extremeMlagPeerAddrType,
       "extremeMlagPeerIP": extremeMlagPeerIP,
       "extremeMlagPeerPortCount": extremeMlagPeerPortCount,
       "extremeMlagPeerCheckPointStatus": extremeMlagPeerCheckPointStatus,
       "extremeMlagPeerRxHellos": extremeMlagPeerRxHellos,
       "extremeMlagPeerRxCheckpointMsgs": extremeMlagPeerRxCheckpointMsgs,
       "extremeMlagPeerHelloErrors": extremeMlagPeerHelloErrors,
       "extremeMlagPeerHelloTimeouts": extremeMlagPeerHelloTimeouts,
       "extremeMlagPeerUptime": extremeMlagPeerUptime,
       "extremeMlagPeerLocalTxInterval": extremeMlagPeerLocalTxInterval,
       "extremeMlagPeerRemoteTxInterval": extremeMlagPeerRemoteTxInterval,
       "extremeMlagPeerTxHellos": extremeMlagPeerTxHellos,
       "extremeMlagPeerTxCheckpoints": extremeMlagPeerTxCheckpoints,
       "extremeMlagPeerCheckpointErrors": extremeMlagPeerCheckpointErrors,
       "extremeMlagPeerConnnectErrors": extremeMlagPeerConnnectErrors,
       "extremeMlagPeerRowStatus": extremeMlagPeerRowStatus,
       "extremeMlagPeerCfgLacpMac": extremeMlagPeerCfgLacpMac,
       "extremeMlagPeerOperLacpMac": extremeMlagPeerOperLacpMac,
       "extremeMlagPortTable": extremeMlagPortTable,
       "extremeMlagPortEntry": extremeMlagPortEntry,
       "extremeMlagPortLocalPortIfIndex": extremeMlagPortLocalPortIfIndex,
       "extremeMlagPortId": extremeMlagPortId,
       "extremeMlagPortPeer": extremeMlagPortPeer,
       "extremeMlagPortLocalLinkStatus": extremeMlagPortLocalLinkStatus,
       "extremeMlagPortRemoteLinkStatus": extremeMlagPortRemoteLinkStatus,
       "extremeMlagPortPeerState": extremeMlagPortPeerState,
       "extremeMlagPortLocalFailures": extremeMlagPortLocalFailures,
       "extremeMlagPortRemoteFailures": extremeMlagPortRemoteFailures,
       "extremeMlagPortRowStatus": extremeMlagPortRowStatus,
       "extremeMlagConvergenceControl": extremeMlagConvergenceControl,
       "extremeMlagNotificationObjects": extremeMlagNotificationObjects,
       "extremeMlagNotifications": extremeMlagNotifications,
       "extremeMlagNotificationsPrefix": extremeMlagNotificationsPrefix,
       "extremeMlagPeerUp": extremeMlagPeerUp,
       "extremeMlagPeerDown": extremeMlagPeerDown}
)
